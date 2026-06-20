import sys, pathlib, datetime
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import scraper

# Representative iCal covering every filter branch (real feed structures)
SAMPLE = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//test//EN
BEGIN:VEVENT
DTSTART;TZID=America/Chicago:20260620T190000
SUMMARY:Hunter Hicks
CATEGORIES:Free Event
URL:https://gruenehall.com/event/hunter-hicks/
LOCATION:Gruene Hall
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=America/Chicago:20260623T180000
SUMMARY:Swing Dance Lessons
CATEGORIES:Free Event
LOCATION:Gruene Hall
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=America/Chicago:20260627T210000
SUMMARY:Cooder Graw
CATEGORIES:Ticketed Event
LOCATION:Gruene Hall
END:VEVENT
END:VCALENDAR"""

PEARL = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//test//EN
BEGIN:VEVENT
DTSTART;TZID=America/Chicago:20260620T090000
SUMMARY:Farmers Market
CATEGORIES:Community,Markets
LOCATION:Pearl
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=America/Chicago:20260622T200000
SUMMARY:Phantom Planet & Augustana
CATEGORIES:Music,Stable Hall
LOCATION:Stable Hall\\, 307 Pearl Parkway
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=America/Chicago:20260622T180000
SUMMARY:Amor X Pearl Cycle & Bootcamp Classes
CATEGORIES:Community,Fitness
LOCATION:Pearl Park
END:VEVENT
BEGIN:VEVENT
DTSTART;TZID=America/Chicago:20260623T190000
SUMMARY:Two-Step Tuesdays at Stable Hall
CATEGORIES:Community,Music,Stable Hall
LOCATION:Stable Hall
END:VEVENT
END:VCALENDAR"""

def run(cfgname, text):
    cfg = next(c for c in scraper.ICAL_VENUES if c["venue"]==cfgname)
    raw = scraper.parse_ical(text)
    kept=[]
    for ev in raw:
        if not ev["summary"]: continue
        if not scraper.keep(ev, cfg): continue
        cat = cfg["category"]
        if cfg["venue"]=="The Pearl":
            cat = "Music" if "stable hall" in ev["location"].lower() else "Festival/Market"
        kept.append((ev["summary"], cat, scraper.fmt_time(ev), scraper.price_from(ev,cfg)))
    return kept

gh = run("Gruene Hall", SAMPLE)
print("GRUENE:", gh)
assert [k[0] for k in gh]==["Hunter Hicks","Cooder Graw"], "Gruene filter failed"
assert gh[0][3]=="Free" and gh[1][3]=="Ticketed", "price tag failed"

pearl = run("The Pearl", PEARL)
print("PEARL :", pearl)
names=[k[0] for k in pearl]
assert "Farmers Market" in names, "market dropped"
assert "Phantom Planet & Augustana" in names, "Stable Hall concert dropped"
assert "Amor X Pearl Cycle & Bootcamp Classes" not in names, "fitness not excluded"
assert "Two-Step Tuesdays at Stable Hall" not in names, "two-step not excluded"
# Stable Hall concert categorized as Music
assert dict((n,c) for n,c,_,_ in pearl)["Phantom Planet & Augustana"]=="Music"
assert dict((n,c) for n,c,_,_ in pearl)["Farmers Market"]=="Festival/Market"
print("\nALL PARSER TESTS PASSED")
