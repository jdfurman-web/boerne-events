# Go-live setup — Boerne Area Events page

**One-time, ~10 minutes, no coding.** After this, the page lives at a public URL and rebuilds itself every morning at 6 AM Central. Nothing to maintain.

---

## Step 1 — Create a free GitHub account
Go to **github.com** → Sign up. Use **furmanjd@gmail.com**. Pick a username — it becomes part of your web address (e.g. username `jfurman` → site at `jfurman.github.io/boerne-events`).

**Why it matters:** GitHub hosts the page free *and* runs the daily refresh in its own cloud — your computer never has to be on.

## Step 2 — Make the repository
Top-right **+** → **New repository**.
- **Name:** `boerne-events`
- **Public** (required for free Pages)
- Don't add a README (we have the files)
- **Create repository**

## Step 3 — Upload the files
On the empty repo page: **uploading an existing file**.
Drag in **everything** from this folder:

```
index.html   events.json   curated.json
scraper.py   build_site.py  requirements.txt
.gitignore   README.md
the .github folder (with workflows/daily.yml inside)
```

> If the drag-drop won't take the `.github` folder, create it manually: **Add file → Create new file**, type `.github/workflows/daily.yml` as the name, paste the file's contents, commit.

Click **Commit changes**.

## Step 4 — Turn on GitHub Pages
Repo **Settings** → **Pages** (left sidebar).
- **Source:** Deploy from a branch
- **Branch:** `main` / `/(root)` → **Save**

Wait ~1 minute. The page goes live at:
**`https://<your-username>.github.io/boerne-events/`**

That's the link you share. 🎉

## Step 5 — Confirm the daily refresh
Repo **Actions** tab → you'll see **"Daily events refresh."** Click it → **Run workflow** to test it now. Green check = it scraped the venues, rebuilt the page, and published. From here it runs itself every morning.

---

## What runs automatically vs. what's curated
- **Auto every morning (live calendar feeds):** Gruene Hall, Brauntex Theatre, The Pearl. These are the venues that change most — pulled fresh daily, zero effort.
- **Curated (`curated.json`):** Floore's, Sam's Burger Joint, Whitewater, Tapatio Springs, Cibolo/Moondance, Cave Without a Name, Comfort venues, area markets. These have no machine-readable feed, so they're hand-verified. Ask Knox to "refresh the Boerne events curated list" anytime (worth doing ~weekly) and the new file gets pushed.

**Bottom line:** Share the `.github.io` link. The big-volume venues stay current on their own; ping me weekly to top off the rest.
