#!/usr/bin/env python3
"""Boerne-area events scraper.

AUTO venues expose iCalendar feeds (WordPress "The Events Calendar", ?ical=1):
  Gruene Hall, Brauntex Theatre, The Pearl, The Bevy Hotel, Singing Water Vineyards.
CURATED venues (no feed) live in curated.json and are merged verbatim:
  Floore's, Sam's, Whitewater, Tapatio, Comfort, Cibolo, Free Roam Brewing, etc.
Resilience: each feed is wrapped in try/except; on failure we keep the last-good
events for that venue (from existing events.json) so an outage never blanks the page.
Window: rolling [today-1 .. today+HORIZON]. Output: events.json (build_site.py renders).
"""
import json, sys, datetime, pathlib, traceback

BASE = pathlib.Path(__file__).parent
HORIZON_DAYS = 45

AREA_GROUP = {
    "Boerne": "Boerne", "Comfort": "Comfort",
    "Gruene": "Gruene / New Braunfels", "New Braunfels": "Gruene / New Braunfels",
    "Helotes": "Hill Country / N. San Antonio",
    "San Antonio - Pearl": "Hill Country / N. San Antonio",
    "San Antonio – Pearl": "Hill Country / N. San Antonio",
    "San Antonio – near Pearl": "Hill Country / N. San Antonio",
    "San Antonio – San Pedro": "Hill Country / N. San Antonio",
}

ICAL_VENUES = [
    {
        "venue": "Gruene Hall", "area": "Gruene", "category": "Music",
        "url": "https://gruenehall.com/events/?ical=1",
        "exclude": ["dance lesson", "two step lesson", "two-step lesson",
                    "line dance", "swing dance", "yoga", "schlather day",
                    "trivia", "bingo", "market"],
    },
    {
        "venue": "Brauntex Theatre", "area": "New Braunfels", "category": "Theater/Arts",
        "url": "https://brauntex.org/events/?ical=1",
        "exclude": ["camp", "rental", "private"],
    },
    {
        "venue": "The Pearl", "area": "San Antonio – Pearl", "category": "Festival/Market",
        "url": "https://events.atpearl.com/events/?ical=1",
        "include": ["farmers market", "makers market", "night market"],
        "include_loc": ["stable hall"],
        "exclude": ["two-step", "two step", "latin dance", "watch party", "yoga",
                    "boot camp", "bootcamp", "cycle", "fitness", "tasting",
                    "sternewirth", "otto", "happy hour", "class at", "pasta",
                    "vinyl series", "ice cream", "launch party", "showdown",
                    "aperitivo", "world cup"],
    },
    {
        "venue": "The Bevy Hotel", "area": "Boerne", "category": "Music",
        "url": "https://theboernelife.com/venue/the-bevy-hotel-boerne/?ical=1",
        "exclude": ["first look", "luncheon", "preview", "the vistas", "trivia",
                    "job fair", "career", "chamber"],
        "retag_market": ["market", "festival", "celebration", "tasting", "brunch"],
    },
    {
        "venue": "Singing Water Vineyards", "area": "Comfort", "category": "Music",
        "url": "https://theboernelife.com/venue/singing-water-vineyards/?ical=1",
        "exclude": ["trivia", "private"],
        "retag_market": ["market", "festival", "celebration", "burger", "tasting", "brunch"],
    },
]

MUSIC_HINTS = ["tribute", "band", "concert", "live music", "country club",
               "jazz", "buffett", "mccoy", "americana", "acoustic"]


def log(*a):
    print("[scraper]", *a, file=sys.stderr)


def fetch(url):
    import requests
    r = requests.get(url, timeout=30, headers={
        "User-Agent": "Mozilla/5.0 (BoerneEventsBot; +https://example.org)"})
    r.raise_for_status()
    return r.text


def parse_ical(text):
    from icalendar import Calendar
    cal = Calendar.from_ical(text)
    out = []
    for comp in cal.walk("VEVENT"):
        dt = comp.get("DTSTART")
        if dt is None:
            continue
        d = dt.dt
        start = d if isinstance(d, datetime.datetime) else datetime.datetime(d.year, d.month, d.day)
        cats = comp.get("CATEGORIES")
        catlist = []
        if cats is not None:
            try:
                catlist = [str(c) for c in cats.cats]
            except Exception:
                catlist = [str(cats)]
        out.append({
            "summary": str(comp.get("SUMMARY", "")).strip(),
            "start": start,
            "all_day": not isinstance(d, datetime.datetime),
            "categories": catlist,
            "location": str(comp.get("LOCATION", "")),
            "url": str(comp.get("URL", "")),
        })
    return out


def fmt_time(ev):
    if ev["all_day"]:
        return "All day"
    return ev["start"].strftime("%-I:%M%p").lower().replace(":00", "")


def price_from(ev):
    cats = " ".join(ev["categories"]).lower()
    if "free" in cats:
        return "Free"
    if "ticketed" in cats:
        return "Ticketed"
    return ""


def keep(ev, cfg):
    s = ev["summary"].lower()
    loc = ev["location"].lower()
    for x in cfg.get("exclude", []):
        if x in s:
            return False
    inc = cfg.get("include")
    inc_loc = cfg.get("include_loc")
    if inc or inc_loc:
        ok = False
        if inc and any(x in s for x in inc):
            ok = True
        if inc_loc and any(x in loc for x in inc_loc):
            ok = True
        if not ok:
            return False
    return True


def scrape_ical_venue(cfg):
    raw = parse_ical(fetch(cfg["url"]))
    rows = []
    for ev in raw:
        if not ev["summary"] or not keep(ev, cfg):
            continue
        cat = cfg["category"]
        if cfg["venue"] == "Brauntex Theatre":
            s = ev["summary"].lower()
            cat = "Music" if any(h in s for h in MUSIC_HINTS) and "cinema" not in s else "Theater/Arts"
        if cfg["venue"] == "The Pearl":
            cat = "Music" if "stable hall" in ev["location"].lower() else "Festival/Market"
        if cfg.get("retag_market") and any(h in ev["summary"].lower() for h in cfg["retag_market"]):
            cat = "Festival/Market"
        rows.append({
            "date": ev["start"].strftime("%Y-%m-%d"),
            "venue": cfg["venue"], "area": cfg["area"], "category": cat,
            "act": ev["summary"], "time": fmt_time(ev),
            "ticket": ev["url"] or cfg["url"].split("?")[0],
            "source": cfg["url"].split("?")[0], "price": price_from(ev),
        })
    return rows


def main():
    today = datetime.date.today()
    lo = (today - datetime.timedelta(days=1)).isoformat()
    hi = (today + datetime.timedelta(days=HORIZON_DAYS)).isoformat()

    prev = {}
    pf = BASE / "events.json"
    if pf.exists():
        for e in json.load(open(pf)).get("events", []):
            prev.setdefault(e["venue"], []).append(e)

    events = []
    cur = json.load(open(BASE / "curated.json"))["events"]
    events += cur
    log("curated: %d events" % len(cur))

    for cfg in ICAL_VENUES:
        try:
            rows = scrape_ical_venue(cfg)
            if not rows:
                raise RuntimeError("0 rows after filter")
            log("%s: %d events (live)" % (cfg["venue"], len(rows)))
            events += rows
        except Exception as e:
            fb = prev.get(cfg["venue"], [])
            log("!! %s failed (%s); keeping %d cached" % (cfg["venue"], e, len(fb)))
            traceback.print_exc()
            events += fb

    for e in events:
        e["group"] = AREA_GROUP.get(e["area"], e["area"])
    events = [e for e in events if lo <= e["date"] <= hi]
    seen, dedup = set(), []
    for e in sorted(events, key=lambda e: (e["date"], e.get("time", ""), e["venue"], e["act"])):
        k = (e["date"], e["venue"], e["act"].lower())
        if k in seen:
            continue
        seen.add(k)
        dedup.append(e)

    out = {
        "generated": datetime.datetime.now().isoformat(timespec="seconds"),
        "window": {"start": lo, "end": hi},
        "count": len(dedup), "events": dedup,
    }
    json.dump(out, open(pf, "w"), indent=2, ensure_ascii=False)
    log("WROTE events.json: %d events (%s .. %s)" % (len(dedup), lo, hi))


if __name__ == "__main__":
    main()
