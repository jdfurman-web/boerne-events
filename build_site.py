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

payload = json.dumps(events, ensure_ascii=False)

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Boerne Area Live Music &amp; Events</title>
<meta name="description" content="A daily-updated calendar of live music, festivals, markets, and theater across Boerne, Gruene, Comfort, and the northern San Antonio Hill Country.">
<style>
:root{
  --bg:#faf6ef; --card:#fffdf9; --ink:#2b2218; --muted:#7a6f5f;
  --line:#e7ddcb; --accent:#9c4a1a; --accent2:#1f5e3f; --accent3:#5a4a82;
  --chip:#f0e7d6; --shadow:0 1px 2px rgba(60,40,15,.06),0 4px 14px rgba(60,40,15,.05);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  line-height:1.45;-webkit-font-smoothing:antialiased}
header.hero{background:linear-gradient(160deg,#9c4a1a 0%,#7a3a14 55%,#5e2d10 100%);color:#fdf3e6;
  padding:30px 18px 22px;border-bottom:4px solid #d98f4f}
.hero-inner{max-width:980px;margin:0 auto}
.hero h1{margin:0 0 4px;font-size:1.72rem;letter-spacing:.2px;font-weight:800}
.hero p{margin:0;color:#f3dcc4;font-size:.96rem}
.updated{margin-top:8px;font-size:.8rem;color:#eccba8}
.wrap{max-width:980px;margin:0 auto;padding:0 14px 60px}
.controls{position:sticky;top:0;z-index:20;background:var(--bg);
  padding:12px 0 8px;border-bottom:1px solid var(--line);margin-bottom:6px}
.search{width:100%;padding:11px 13px;border:1px solid var(--line);border-radius:10px;
  font-size:1rem;background:var(--card);color:var(--ink)}
.search::placeholder{color:#a99c87}
.pillrow{display:flex;flex-wrap:wrap;gap:6px;margin-top:9px}
.pill{border:1px solid var(--line);background:var(--card);color:var(--muted);
  padding:6px 12px;border-radius:999px;font-size:.83rem;cursor:pointer;white-space:nowrap;
  transition:all .12s}
.pill:hover{border-color:#cdbfa6}
.pill.on{background:var(--ink);color:#fdf3e6;border-color:var(--ink)}
.pill.cat-Music.on{background:var(--accent)}
.pill.cat-Festival\\/Market.on{background:var(--accent2)}
.pill.cat-TheaterArts.on{background:var(--accent3)}
.label{font-size:.72rem;text-transform:uppercase;letter-spacing:.6px;color:#a99c87;
  margin:10px 4px 0;font-weight:700}
.count{margin:14px 4px 4px;font-size:.85rem;color:var(--muted)}
.daygroup{margin-top:18px}
.dayhead{position:sticky;top:118px;background:var(--bg);padding:7px 4px 6px;
  font-size:1.02rem;font-weight:800;color:var(--accent);border-bottom:2px solid var(--line);
  z-index:10}
.dayhead .wknd{color:var(--accent2);font-weight:700;font-size:.78rem;margin-left:8px}
.card{display:flex;gap:13px;align-items:flex-start;background:var(--card);
  border:1px solid var(--line);border-radius:12px;padding:13px 14px;margin-top:9px;
  box-shadow:var(--shadow)}
.time{flex:0 0 92px;font-size:.82rem;color:var(--muted);font-weight:600;padding-top:2px}
.body{flex:1;min-width:0}
.act{font-weight:700;font-size:1.04rem;margin:0 0 2px;line-height:1.25}
.venue{font-size:.88rem;color:var(--muted)}
.tags{margin-top:7px;display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.tag{font-size:.7rem;padding:3px 9px;border-radius:999px;font-weight:700;letter-spacing:.3px}
.tag.Music{background:#f6e3d4;color:#8a3d12}
.tag.Festival\\/Market{background:#d9ecdf;color:#1f5e3f}
.tag.TheaterArts{background:#e4def0;color:#4a3a72}
.price{font-size:.74rem;color:#6f6552;background:var(--chip);padding:3px 9px;border-radius:999px;font-weight:600}
.price.free{background:#dff0df;color:#216c3a}
.tix{margin-left:auto;font-size:.82rem;font-weight:700;color:var(--accent);text-decoration:none;
  border:1px solid #e3c7ad;padding:5px 12px;border-radius:8px;white-space:nowrap}
.tix:hover{background:#9c4a1a;color:#fff;border-color:#9c4a1a}
.empty{text-align:center;color:var(--muted);padding:50px 10px;font-size:1rem}
footer{max-width:980px;margin:0 auto;padding:24px 16px 50px;color:var(--muted);font-size:.78rem;
  border-top:1px solid var(--line)}
footer a{color:var(--accent)}
.toggle{font-size:.8rem;color:var(--accent);cursor:pointer;text-decoration:underline;background:none;border:none;padding:0}
@media(max-width:560px){
  .hero h1{font-size:1.4rem}
  .time{flex-basis:74px;font-size:.76rem}
  .dayhead{top:150px}
  .tix{margin-left:0}
  .card{flex-direction:column;gap:6px}
  .time{flex-basis:auto}
}
</style>
</head>
<body>
<header class="hero">
  <div class="hero-inner">
    <h1>&#127865; Boerne Area Live Music &amp; Events</h1>
    <p>Live music, festivals &amp; markets, and theater &mdash; Boerne &middot; Gruene &amp; New Braunfels &middot; Comfort &middot; northern San Antonio Hill Country.</p>
    <div class="updated">Updated daily &middot; Last refreshed __GEN__</div>
  </div>
</header>
<div class="wrap">
  <div class="controls">
    <input id="q" class="search" type="search" placeholder="Search acts, venues, towns&hellip;" autocomplete="off">
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
  <p><strong>Venues tracked:</strong> Gruene Hall, John T. Floore&rsquo;s, Whitewater Amphitheater, Brauntex Theatre, Sam&rsquo;s Burger Joint, Cave Without a Name, Cibolo Center (Moondance), Tapatio Springs, The Pearl, San Pedro Playhouse, Old Gruene Market Days, Boerne &amp; Comfort markets, and more.</p>
  <p id="srcline"></p>
</footer>
<script id="data" type="application/json">__DATA__</script>
<script>
const EVENTS = JSON.parse(document.getElementById('data').textContent);
const state = {when:'upcoming', area:'all', cat:'all', q:'', showPast:false};
const $ = s=>document.querySelector(s);
const listEl=$('#list'), countEl=$('#count');

function todayStr(){const d=new Date();return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');}
function parseD(s){const [y,m,d]=s.split('-').map(Number);return new Date(y,m-1,d);}
function fmtDay(s){return parseD(s).toLocaleDateString('en-US',{weekday:'long',month:'long',day:'numeric'});}
function isWeekend(s){const wd=parseD(s).getDay();return wd===5||wd===6||wd===0;}
function catClass(c){return c.replace(/[^A-Za-z]/g,'');}

function weekendRange(){
  const now=new Date(); now.setHours(0,0,0,0);
  const wd=now.getDay();
  // upcoming Fri..Sun. If today is Fri/Sat/Sun, use current weekend.
  let start=new Date(now);
  if(wd===0){start.setDate(now.getDate()-2);} // Sun -> back to Fri
  else if(wd===6){start.setDate(now.getDate()-1);} // Sat -> Fri
  else if(wd<5){start.setDate(now.getDate()+(5-wd));} // before Fri -> this Fri
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
  if(!rows.length){listEl.innerHTML='<div class="empty">No events match these filters.<br>Try widening the area or date range.</div>';return;}
  let h='', curDay='';
  for(const ev of rows){
    if(ev.date!==curDay){
      curDay=ev.date;
      h+='<div class="daygroup"><div class="dayhead">'+fmtDay(ev.date)+
         (isWeekend(ev.date)?'<span class="wknd">WEEKEND</span>':'')+'</div>';
    }
    const cc=catClass(ev.category);
    const freeCls = (ev.price||'').toLowerCase().includes('free')?' free':'';
    const priceTxt = ev.price? ev.price : '';
    h+='<div class="card">'+
        '<div class="time">'+esc(ev.time)+'</div>'+
        '<div class="body">'+
          '<p class="act">'+esc(ev.act)+'</p>'+
          '<div class="venue">'+esc(ev.venue)+' &middot; '+esc(ev.area)+'</div>'+
          '<div class="tags">'+
            '<span class="tag '+cc+'">'+esc(ev.category)+'</span>'+
            (priceTxt?'<span class="price'+freeCls+'">'+esc(priceTxt)+'</span>':'')+
            (ev.ticket?'<a class="tix" href="'+esc(ev.ticket)+'" target="_blank" rel="noopener">Details &rsaquo;</a>':'')+
          '</div>'+
        '</div>'+
       '</div>';
  }
  // close last daygroup wrapper implicitly (cards are inside)
  listEl.innerHTML=h+'</div>';
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

HTML = HTML.replace("__DATA__", payload).replace("__GEN__", html.escape(gen_disp))
(BASE/"index.html").write_text(HTML, encoding="utf-8")
print("Wrote index.html (", len(HTML), "bytes ) with", len(events), "events; generated", gen_disp)
