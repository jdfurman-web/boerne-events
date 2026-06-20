# Boerne Area Live Music & Events

A daily-updated, shareable web calendar of live music, festivals & markets, and theater across **Boerne, Gruene/New Braunfels, Comfort, and the northern San Antonio Hill Country**.

**To publish it, see [SETUP.md](SETUP.md).**

## How it works
| File | Role |
|------|------|
| `index.html` | The public page (self-contained: search + area/type/date filters, mobile-friendly). |
| `events.json` | The current event data the page reads. Rebuilt daily. |
| `curated.json` | Hand-verified venues that lack a machine feed; merged in each run. |
| `scraper.py` | Pulls live iCal feeds (Gruene Hall, Brauntex, The Pearl), filters noise, merges curated, writes `events.json`. Resilient: if a feed is down it keeps the last good data. |
| `build_site.py` | Renders `events.json` → `index.html`. |
| `.github/workflows/daily.yml` | Runs the two scripts every morning (6 AM CT) and publishes. |

## Run it locally
```bash
pip install -r requirements.txt
python scraper.py && python build_site.py
open index.html
```

## Adding a venue
- **Has a "The Events Calendar" site (`?ical=1` works)?** Add a config block to `ICAL_VENUES` in `scraper.py`.
- **No feed?** Add rows to `curated.json`.

## Notes
- Window: rolling, today through ~45 days out.
- Always verify date/time/tickets on the venue's own page before going out — lineups change.
- Not affiliated with any venue. Community resource.
