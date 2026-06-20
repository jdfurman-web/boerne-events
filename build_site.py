#!/usr/bin/env python3
"""Builds a self-contained index.html from events.json.
Run after the scraper updates events.json. Data is embedded so the page works
as a standalone file AND on static hosting with no fetch/CORS issues."""
import json, datetime, html, pathlib

BASE = pathlib.Path(__file__).parent
data = json.loads((BASE/"events.json").read_text(encoding="utf-8"))
events = data["events"]
gen = data.get("generated","")
try:
    gen_disp = datetime.datetime.fromisoformat(gen).strftime("%b %-d, %Y at %-I:%M %p")
except Exception:
    gen_disp = gen

# ---- summary stats for the hero ----
venue_count = len({e.get("venue","") for e in events if e.get("venue")})
try:
    dates = sorted(e["date"] for e in events if e.get("date"))
    span_days = (datetime.date.fromisoformat(dates[-1]) - datetime.date.today()).days
    span_days = max(span_days, 0)
except Exception:
    span_days = 0

payload = json.dumps(events, ensure_ascii=False)

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Boerne Area Live Music &amp; Events</title>
<meta name="description" content="A daily-updated calendar of live music, festivals, markets, and theater across Boerne, Gruene, Comfort, and the northern San Antonio Hill Country.">
<meta name="theme-color" content="#7a3a14">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700;9..144,900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#f6f1e8; --card:#fffefb; --ink:#241d14; --muted:#7c7060;
  --line:#e7ddca; --line2:#efe7d6;
  --accent:#b0531f; --accent-d:#8a3d12; --accent2:#2f6b48; --accent3:#5a4a82;
  --gold:#dd9b53;
  --chip:#f1e8d7;
  --shadow:0 1px 2px rgba(60,40,15,.05),0 6px 18px rgba(60,40,15,.06);
  --shadow-h:0 2px 4px rgba(60,40,15,.07),0 14px 32px rgba(60,40,15,.12);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);
  font-family:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  line-height:1.45;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}

/* ---------- HERO ---------- */
header.hero{position:relative;overflow:hidden;color:#fdf3e6;
  background:linear-gradient(165deg,#a8511f 0%,#7e3a14 48%,#532a10 100%);
  border-bottom:1px solid #43230d}
.hero svg.scene{position:absolute;left:0;right:0;bottom:-1px;width:100%;height:auto;display:block;z-index:1}
.hero-inner{position:relative;z-index:3;max-width:1000px;margin:0 auto;padding:34px 20px 78px}
.brandrow{display:flex;align-items:center;gap:13px}
.logo{flex:0 0 auto;width:46px;height:46px;display:grid;place-items:center;
  background:rgba(255,244,230,.12);border:1px solid rgba(255,244,230,.25);border-radius:13px;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.15)}
.hero h1{margin:0;font-family:"Fraunces",Georgia,serif;font-weight:900;font-size:2.05rem;
  letter-spacing:-.01em;line-height:1.02}
.hero h1 .sub{display:block;font-size:1.05rem;font-weight:600;color:#f6d9bd;letter-spacing:.01em;margin-top:3px}
.tagline{margin:15px 0 0;color:#f4dcc4;font-size:.98rem;max-width:640px}
.statrow{display:flex;flex-wrap:wrap;gap:8px;margin-top:17px}
.stat{display:inline-flex;align-items:center;gap:7px;background:rgba(255,244,230,.13);
  border:1px solid rgba(255,244,230,.22);padding:6px 13px;border-radius:999px;font-size:.83rem;
  font-weight:600;color:#fcefdd;backdrop-filter:blur(2px)}
.stat b{font-weight:800;color:#fff}
.updated{margin-top:14px;font-size:.79rem;color:#eccba8;display:flex;align-items:center;gap:6px}
.dot{width:7px;height:7px;border-radius:50%;background:#8fd6a3;box-shadow:0 0 0 3px rgba(143,214,163,.25)}

/* ---------- LAYOUT ---------- */
.wrap{max-width:1000px;margin:0 auto;padding:0 16px 70px}
.controls{position:sticky;top:0;z-index:30;margin:0 -16px;padding:13px 16px 11px;
  background:rgba(246,241,232,.92);backdrop-filter:blur(10px);
  border-bottom:1px solid var(--line)}
.searchwrap{position:relative}
.searchwrap svg{position:absolute;left:13px;top:50%;transform:translateY(-50%);opacity:.45}
.search{width:100%;padding:12px 14px 12px 40px;border:1px solid var(--line);border-radius:12px;
  font-size:1rem;background:var(--card);color:var(--ink);font-family:inherit;
  transition:border-color .15s,box-shadow .15s}
.search:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 3px rgba(176,83,31,.13)}
.search::placeholder{color:#a99c87}
.pillrow{display:flex;flex-wrap:wrap;gap:7px;margin-top:9px}
.pill{border:1px solid var(--line);background:var(--card);color:var(--muted);
  padding:6px 13px;border-radius:999px;font-size:.83rem;font-weight:600;cursor:pointer;
  white-space:nowrap;transition:all .13s;font-family:inherit}
.pill:hover{border-color:#cdbfa6;color:var(--ink)}
.pill.on{background:var(--ink);color:#fdf3e6;border-color:var(--ink);box-shadow:0 2px 8px rgba(40,30,15,.18)}
.pill.cat-Music.on{background:var(--accent);border-color:var(--accent)}
.pill.cat-Festival\\/Market.on{background:var(--accent2);border-color:var(--accent2)}
.pill.cat-TheaterArts.on{background:var(--accent3);border-color:var(--accent3)}
.label{font-size:.7rem;text-transform:uppercase;letter-spacing:.7px;color:#a4977f;
  margin:11px 4px 0;font-weight:700}
.count{margin:16px 4px 2px;font-size:.84rem;color:var(--muted);font-weight:600}

/* ---------- DAY GROUPS ---------- */
.daygroup{margin-top:14px}
.dayhead{position:sticky;top:150px;z-index:10;display:flex;align-items:center;gap:10px;
  background:linear-gradient(var(--bg),var(--bg) 70%,rgba(246,241,232,0));
  padding:10px 2px 8px;margin-top:8px}
.dayhead h2{margin:0;font-family:"Fraunces",Georgia,serif;font-weight:700;font-size:1.12rem;
  color:var(--accent-d)}
.dayhead .rule{flex:1;height:1px;background:var(--line)}
.wknd{color:#fff;background:var(--accent2);font-weight:700;font-size:.64rem;letter-spacing:.6px;
  padding:3px 8px;border-radius:999px;text-transform:uppercase}

/* ---------- CARDS ---------- */
.card{position:relative;display:flex;gap:14px;align-items:flex-start;background:var(--card);
  border:1px solid var(--line);border-radius:14px;padding:14px 16px 14px 15px;margin-top:10px;
  box-shadow:var(--shadow);transition:transform .14s,box-shadow .14s,border-color .14s}
.card:hover{transform:translateY(-2px);box-shadow:var(--shadow-h);border-color:#dcd0b8}
.card::before{content:"";position:absolute;left:0;top:14px;bottom:14px;width:4px;border-radius:0 4px 4px 0}
.card.c-Music::before{background:var(--accent)}
.card.c-FestivalMarket::before{background:var(--accent2)}
.card.c-TheaterArts::before{background:var(--accent3)}
.med{flex:0 0 auto;width:46px;height:46px;border-radius:12px;display:grid;place-items:center;margin-top:1px}
.med.c-Music{background:#f7e4d4;color:#a4480f}
.med.c-FestivalMarket{background:#daeede;color:#236b46}
.med.c-TheaterArts{background:#e6def3;color:#4a3a72}
.left{flex:0 0 auto;display:flex;flex-direction:column;align-items:center;gap:6px;width:46px}
.time{font-size:.72rem;color:var(--muted);font-weight:700;text-align:center;line-height:1.15}
.body{flex:1;min-width:0}
.act{font-family:"Fraunces",Georgia,serif;font-weight:600;font-size:1.12rem;margin:0 0 3px;
  line-height:1.22;color:var(--ink)}
.venue{font-size:.88rem;color:var(--muted);display:flex;align-items:center;gap:5px}
.venue svg{flex:0 0 auto;opacity:.6}
.tags{margin-top:9px;display:flex;flex-wrap:wrap;gap:7px;align-items:center}
.tag{font-size:.69rem;padding:3px 10px;border-radius:999px;font-weight:700;letter-spacing:.3px;
  display:inline-flex;align-items:center;gap:5px}
.tag.Music{background:#f7e3d3;color:#8a3d12}
.tag.FestivalMarket{background:#d9ecdf;color:#1f5e3f}
.tag.TheaterArts{background:#e4def0;color:#4a3a72}
.price{font-size:.72rem;color:#6f6552;background:var(--chip);padding:3px 10px;border-radius:999px;font-weight:700}
.price.free{background:#dcefdc;color:#1d6a38}
.tix{margin-left:auto;font-size:.82rem;font-weight:700;color:var(--accent);text-decoration:none;
  border:1px solid #e6caae;padding:7px 14px;border-radius:9px;white-space:nowrap;
  display:inline-flex;align-items:center;gap:4px;transition:all .13s}
.tix:hover{background:var(--accent);color:#fff;border-color:var(--accent);box-shadow:0 4px 12px rgba(176,83,31,.25)}
.empty{text-align:center;color:var(--muted);padding:56px 14px;font-size:1rem}
.empty svg{opacity:.4;margin-bottom:10px}

/* ---------- FOOTER ---------- */
footer{max-width:1000px;margin:0 auto;padding:28px 18px 56px;color:var(--muted);font-size:.79rem;
  border-top:1px solid var(--line);line-height:1.6}
footer strong{color:var(--ink)}
footer a{color:var(--accent)}

@media(max-width:560px){
  .hero-inner{padding:26px 18px 66px}
  .hero h1{font-size:1.62rem}
  .hero h1 .sub{font-size:.92rem}
  .dayhead{top:172px}
  .card{padding:13px 14px}
  .med,.left{width:40px}
  .med{height:40px}
  .tix{margin-left:0}
}
</style>
</head>
<body>
<header class="hero">
  <svg class="scene" viewBox="0 0 1440 150" preserveAspectRatio="none" aria-hidden="true">
    <circle cx="1120" cy="70" r="46" fill="#f0b463" opacity=".55"/>
    <circle cx="1120" cy="70" r="30" fill="#f6cd87" opacity=".7"/>
    <path d="M0 96 C 220 60 360 92 560 80 C 780 67 900 38 1120 56 C 1300 71 1380 86 1440 80 L1440 150 L0 150 Z" fill="#6e3413" opacity=".55"/>
    <path d="M0 112 C 200 86 380 116 600 104 C 820 92 1020 70 1240 90 C 1340 99 1400 108 1440 104 L1440 150 L0 150 Z" fill="#5a2a0f" opacity=".7"/>
    <path d="M0 128 C 240 110 420 132 660 126 C 900 120 1100 104 1340 120 C 1390 123 1420 126 1440 125 L1440 150 L0 150 Z" fill="#46210c"/>
  </svg>
  <div class="hero-inner">
    <div class="brandrow">
      <span class="logo" aria-hidden="true">
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fdf3e6" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
          <path d="M9 18V5l11-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="17" cy="16" r="3"/>
        </svg>
      </span>
      <h1>Boerne Live Music &amp; Events<span class="sub">Hill Country happenings, refreshed every morning</span></h1>
    </div>
    <p class="tagline">Live music, festivals &amp; markets, and theater across Boerne, Gruene &amp; New Braunfels, Comfort, and the northern San Antonio Hill Country.</p>
    <div class="statrow">
      <span class="stat"><b id="stEvents">__NEVENTS__</b> upcoming events</span>
      <span class="stat"><b>__NVENUES__</b> venues</span>
      <span class="stat">next <b>__SPAN__</b> days</span>
    </div>
    <div class="updated"><span class="dot"></span> Updated daily &middot; last refreshed __GEN__</div>
  </div>
</header>
<div class="wrap">
  <div class="controls">
    <div class="searchwrap">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#7c7060" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
      <input id="q" class="search" type="search" placeholder="Search acts, venues, towns&hellip;" autocomplete="off">
    </div>
    <div class="label">When</div>
    <div class="pillrow" id="when">
      <button class="pill on" data-when="upcoming">All upcoming</button>
      <button class="pill" data-when="today">Today</button>
      <button class="pill" data-when="weekend">This weekend</button>
      <button class="pill" data-when="week">Next 7 days</button>
    </div>
    <div class="label">Area</div>
    <div class="pillrow" id="area">
      <button class="pill on" data-area="all">All areas</button>
      <button class="pill" data-area="Boerne">Boerne</button>
      <button class="pill" data-area="Comfort">Comfort</button>
      <button class="pill" data-area="Gruene / New Braunfels">Gruene / New Braunfels</button>
      <button class="pill" data-area="Hill Country / N. San Antonio">Hill Country / N. SA</button>
    </div>
    <div class="label">Type</div>
    <div class="pillrow" id="cat">
      <button class="pill on" data-cat="all">All types</button>
      <button class="pill cat-Music" data-cat="Music">Music</button>
      <button class="pill cat-Festival/Market" data-cat="Festival/Market">Festivals &amp; Markets</button>
      <button class="pill cat-TheaterArts" data-cat="Theater/Arts">Theater &amp; Arts</button>
    </div>
  </div>
  <div class="count" id="count"></div>
  <div id="list"></div>
</div>
<footer>
  <p><strong>About:</strong> A community calendar auto-compiled each morning from venue calendars. Always confirm date, time &amp; tickets on the venue&rsquo;s own page before heading out &mdash; lineups change. Not affiliated with any venue.</p>
  <p><strong>Venues tracked:</strong> Gruene Hall, John T. Floore&rsquo;s, Whitewater Amphitheater, Brauntex Theatre, Sam&rsquo;s Burger Joint, Cave Without a Name, Cibolo Center (Moondance), Tapatio Springs, Free Roam Brewing, The Pearl, San Pedro Playhouse, Old Gruene Market Days, Boerne &amp; Comfort markets, and more.</p>
  <p id="srcline"></p>
</footer>
<script id="data" type="application/json">__DATA__</script>
<script>
const EVENTS = JSON.parse(document.getElementById('data').textContent);
const state = {when:'upcoming', area:'all', cat:'all', q:''};
const $ = s=>document.querySelector(s);
const listEl=$('#list'), countEl=$('#count');

const ICONS = {
  Music:'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l11-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="17" cy="16" r="3"/></svg>',
  FestivalMarket:'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l1.5-5h15L21 9"/><path d="M4 9h16v11H4z"/><path d="M4 9c0 1.5 1 2.5 2.5 2.5S9 10.5 9 9c0 1.5 1 2.5 2.5 2.5S14 10.5 14 9c0 1.5 1 2.5 2.5 2.5S19 10.5 20 9"/><path d="M9 20v-5h6v5"/></svg>',
  TheaterArts:'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 5s2 3 6 3 6-3 6-3v5a6 6 0 0 1-12 0z"/><path d="M15 9c1.5.4 3 .4 4 0v3a5 5 0 0 1-8 2.5"/><path d="M6.5 11h.01M10.5 11h.01"/></svg>'
};
const PIN='<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="2.5"/></svg>';

function todayStr(){const d=new Date();return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');}
function parseD(s){const [y,m,d]=s.split('-').map(Number);return new Date(y,m-1,d);}
function fmtDay(s){return parseD(s).toLocaleDateString('en-US',{weekday:'long',month:'long',day:'numeric'});}
function isWeekend(s){const wd=parseD(s).getDay();return wd===5||wd===6||wd===0;}
function catClass(c){return c.replace(/[^A-Za-z]/g,'');}

function weekendRange(){
  const now=new Date(); now.setHours(0,0,0,0);
  const wd=now.getDay();
  let start=new Date(now);
  if(wd===0){start.setDate(now.getDate()-2);}
  else if(wd===6){start.setDate(now.getDate()-1);}
  else if(wd<5){start.setDate(now.getDate()+(5-wd));}
  const end=new Date(start); end.setDate(start.getDate()+2);
  const f=d=>d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
  return [f(start),f(end)];
}
function passesWhen(ev){
  const t=todayStr();
  if(state.when==='upcoming') return ev.date>=t;
  if(state.when==='today') return ev.date===t;
  if(state.when==='week'){const e=new Date();e.setDate(e.getDate()+7);
    const es=e.getFullYear()+'-'+String(e.getMonth()+1).padStart(2,'0')+'-'+String(e.getDate()).padStart(2,'0');
    return ev.date>=t && ev.date<=es;}
  if(state.when==='weekend'){const [a,b]=weekendRange();return ev.date>=a&&ev.date<=b;}
  return true;
}
function passes(ev){
  if(!passesWhen(ev)) return false;
  if(state.area!=='all' && ev.group!==state.area) return false;
  if(state.cat!=='all' && ev.category!==state.cat) return false;
  if(state.q){const q=state.q.toLowerCase();
    if(!(ev.act+' '+ev.venue+' '+ev.area+' '+ev.group).toLowerCase().includes(q)) return false;}
  return true;
}
function render(){
  const rows=EVENTS.filter(passes);
  countEl.textContent = rows.length + (rows.length===1?' event':' events') + ' found';
  if(!rows.length){listEl.innerHTML='<div class="empty"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#b0531f" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg><br>No events match these filters.<br>Try widening the area or date range.</div>';return;}
  let h='', curDay='';
  for(const ev of rows){
    const cc=catClass(ev.category);
    if(ev.date!==curDay){
      if(curDay!=='') h+='</div>';
      curDay=ev.date;
      h+='<div class="daygroup"><div class="dayhead"><h2>'+fmtDay(ev.date)+'</h2>'+
         (isWeekend(ev.date)?'<span class="wknd">Weekend</span>':'')+'<span class="rule"></span></div>';
    }
    const freeCls = (ev.price||'').toLowerCase().includes('free')?' free':'';
    const priceTxt = ev.price? ev.price : '';
    const icon = ICONS[cc]||ICONS.Music;
    h+='<div class="card c-'+cc+'">'+
        '<div class="left">'+
          '<div class="med c-'+cc+'">'+icon+'</div>'+
          (ev.time?'<div class="time">'+esc(ev.time)+'</div>':'')+
        '</div>'+
        '<div class="body">'+
          '<p class="act">'+esc(ev.act)+'</p>'+
          '<div class="venue">'+PIN+'<span>'+esc(ev.venue)+' &middot; '+esc(ev.area)+'</span></div>'+
          '<div class="tags">'+
            '<span class="tag '+cc+'">'+esc(ev.category)+'</span>'+
            (priceTxt?'<span class="price'+freeCls+'">'+esc(priceTxt)+'</span>':'')+
            (ev.ticket?'<a class="tix" href="'+esc(ev.ticket)+'" target="_blank" rel="noopener">Details <span aria-hidden="true">&rsaquo;</span></a>':'')+
          '</div>'+
        '</div>'+
       '</div>';
  }
  if(curDay!=='') h+='</div>';
  listEl.innerHTML=h;
}
function esc(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
function wire(group,key){
  document.querySelectorAll('#'+group+' .pill').forEach(b=>{
    b.addEventListener('click',()=>{
      document.querySelectorAll('#'+group+' .pill').forEach(x=>x.classList.remove('on'));
      b.classList.add('on');
      state[key]=b.dataset[key]; render();
    });
  });
}
wire('when','when'); wire('area','area'); wire('cat','cat');
$('#q').addEventListener('input',e=>{state.q=e.target.value;render();});
$('#srcline').textContent='Sources include each venue\\'s official calendar and ticketing pages. Data snapshot generated __GEN__.';
render();
</script>
</body>
</html>"""

HTML = (HTML.replace("__DATA__", payload)
            .replace("__GEN__", html.escape(gen_disp))
            .replace("__NEVENTS__", str(len(events)))
            .replace("__NVENUES__", str(venue_count))
            .replace("__SPAN__", str(span_days)))
(BASE/"index.html").write_text(HTML, encoding="utf-8")
print("Wrote index.html (", len(HTML), "bytes ) with", len(events), "events;", venue_count, "venues; generated", gen_disp)
