#!/usr/bin/env python3
"""Seed dataset of REAL verified events (pulled 2026-06-19) for the Boerne-area
entertainment calendar. The daily scraper replaces this file's output (events.json)
with freshly scraped data; this seed is the v1 hand-verified baseline."""
import json, datetime

# area buckets -> display group
AREAS = {
    "Boerne": "Boerne", "Comfort": "Comfort",
    "Gruene": "Gruene / New Braunfels", "New Braunfels": "Gruene / New Braunfels",
    "Helotes": "Hill Country / N. San Antonio", "San Antonio – Pearl": "Hill Country / N. San Antonio",
    "San Antonio – near Pearl": "Hill Country / N. San Antonio",
    "San Antonio – San Pedro": "Hill Country / N. San Antonio",
}

def E(date, venue, area, category, act, time, ticket, source, price=""):
    return {"date": date, "venue": venue, "area": area, "category": category,
            "act": act, "time": time, "ticket": ticket, "source": source, "price": price}

events = []

# ---------------- GRUENE HALL (Gruene) ----------------
GH = "https://gruenehall.com/events/"
def gh(date, time, act, url=None, price="Free"):
    events.append(E(date, "Gruene Hall", "Gruene", "Music", act, time,
                    url or "https://gruenehall.com/events/", GH, price))
gh("2026-06-19","12:00pm–4:00pm","Jace Nunnelly","https://gruenehall.com/event/jace-nunnelly-2/")
gh("2026-06-19","4:00pm–7:00pm","Friday Afternoon Club","https://gruenehall.com/event/friday-afternoon-club-13/2026-06-19/")
gh("2026-06-19","Doors 7pm / 9:15pm","Larry Joe Taylor w/ Presley Haile","https://www.prekindle.com/event/68629-larry-joe-taylor-with-special-guest-presley-haile-new-braunfels","Ticketed")
gh("2026-06-20","11:00am–1:00pm","Lindsay Beaver","https://gruenehall.com/event/lindsay-beaver-12/")
gh("2026-06-20","1:00pm–5:00pm","Broken Arrow Band","https://gruenehall.com/event/broken-arrow-band-3/")
gh("2026-06-20","7:00pm–9:00pm","Hunter Hicks","https://gruenehall.com/event/hunter-hicks/")
gh("2026-06-20","9:30pm","JRHB","https://gruenehall.com/event/jrhb/")
gh("2026-06-21","11:30am–2:30pm","Kayla Jane","https://gruenehall.com/event/kayla-jane-11/")
gh("2026-06-21","3:00pm–6:00pm","South Austin Moonlighters","https://gruenehall.com/event/south-austin-moonlighters-10/")
gh("2026-06-21","6:30pm–9:30pm","Michael Monroe Goodman","https://gruenehall.com/event/michael-monroe-goodman-21/")
gh("2026-06-22","6:00pm–8:00pm","Bret Graham","https://gruenehall.com/event/bret-graham-138/")
gh("2026-06-22","8:30pm–10:30pm","Paige Price","https://gruenehall.com/event/paige-price-2/")
gh("2026-06-23","7:00pm–11:00pm","Two Ton Tuesday","https://www.gruenetexas.com/two-ton-tuesdays/","$15")
gh("2026-06-24","6:00pm–8:00pm","Joel Hoffman","https://gruenehall.com/event/joel-hoffman-2/")
gh("2026-06-25","7:00pm–8:00pm","Clay Gibson","https://gruenehall.com/event/clay-gibson/")
gh("2026-06-25","8:30pm–10:30pm","Hill Country Revival","https://gruenehall.com/event/hill-country-revival-2/")
gh("2026-06-26","12:00pm–4:00pm","Shay Domann","https://gruenehall.com/event/shay-domann/")
gh("2026-06-26","4:00pm–7:00pm","Friday Afternoon Club","https://gruenehall.com/event/friday-afternoon-club-13/2026-06-26/")
gh("2026-06-26","Doors 7pm / 9:30pm","Billie Jo Jones","https://www.prekindle.com/event/55144-billie-jo-jones-new-braunfels","$15")
gh("2026-06-27","11:00am–1:00pm","Allan Hendrickson","https://gruenehall.com/event/allan-hendrickson-12/")
gh("2026-06-27","1:00pm–5:00pm","Red Iron Push","https://gruenehall.com/event/red-iron-push-20/")
gh("2026-06-27","Doors 8pm / 9pm","Cooder Graw","https://www.prekindle.com/event/73873-cooder-graw-new-braunfels","$20")
gh("2026-06-28","11:30am–2:30pm","River Town Relics","https://gruenehall.com/event/river-town-relics-5/")
gh("2026-06-28","3:00pm–6:00pm","Trevor Underwood Band","https://gruenehall.com/event/trevor-underwood-band-2/")
gh("2026-06-28","6:30pm–9:30pm","Bret Graham","https://gruenehall.com/event/bret-graham-139/")
gh("2026-06-29","6:00pm–8:00pm","JESKA Songswap with Special Guests","https://gruenehall.com/event/jeska-songswap-with-special-guests-3/")
gh("2026-06-30","7:00pm–11:00pm","Two Ton Tuesday","https://www.gruenetexas.com/two-ton-tuesdays/","$15")
gh("2026-07-01","12:00pm–2:00pm","Tony Taylor Acoustic","https://gruenehall.com/event/tony-taylor-acoustic/")
gh("2026-07-01","2:30pm–5:30pm","Hannah Swann","https://gruenehall.com/event/hannah-swann/")
gh("2026-07-01","6:00pm–8:00pm","The Blokes","https://gruenehall.com/event/the-blokes-2/")
gh("2026-07-01","8:30pm–10:30pm","Soul Ethos","https://gruenehall.com/event/soul-ethos/")
gh("2026-07-02","12:00pm–3:00pm","Andi Holleman & Friends","https://gruenehall.com/event/andi-holleman-friends-4/")
gh("2026-07-02","Doors 7pm / 9:30pm","Silverada","https://www.prekindle.com/event/98731-silverada-new-braunfels","$25")
gh("2026-07-03","12:00pm–4:00pm","Dean Paul Willeford","https://gruenehall.com/event/dean-paul-willeford-3/")
gh("2026-07-03","4:00pm–7:00pm","Friday Afternoon Club","https://gruenehall.com/event/friday-afternoon-club-13/2026-07-03/")
gh("2026-07-03","Doors 7pm / 9:30pm","Silverada","https://www.prekindle.com/event/69239-silverada-new-braunfels","$25")
gh("2026-07-04","11:00am–1:00pm","Kayla Jane","https://gruenehall.com/event/kayla-jane-12/")
gh("2026-07-04","1:00pm–5:00pm","Dusty Moats","https://gruenehall.com/event/dusty-moats-4/")
gh("2026-07-04","8:00pm–9:30pm","Drew Oliver","https://gruenehall.com/event/drew-oliver/")
gh("2026-07-04","10:00pm","David Adam Byrnes","https://gruenehall.com/event/david-adam-byrnes/")
gh("2026-07-05","3:00pm–6:00pm","Adam Johnson Band","https://gruenehall.com/event/adam-johnson-band-12/")
gh("2026-07-05","6:30pm–9:30pm","Tiffiny Dawn Band","https://gruenehall.com/event/tiffiny-dawn-band-2/")
gh("2026-07-06","6:00pm–8:00pm","Jordan Minor","https://gruenehall.com/event/jordan-minor-2/")
gh("2026-07-06","8:30pm–10:30pm","Slim Bawb","https://gruenehall.com/event/slim-bawb-8/")
gh("2026-07-07","7:00pm–11:00pm","Two Ton Tuesday","https://www.gruenetexas.com/two-ton-tuesdays/","$15")
gh("2026-07-08","6:00pm–8:00pm","Marc Sauceda","https://gruenehall.com/event/marc-sauceda-10/")
gh("2026-07-08","8:30pm–10:30pm","Neal Stranahan","https://gruenehall.com/event/neal-stranahan-4/")
gh("2026-07-09","7:00pm–8:00pm","Brodie Lane","https://gruenehall.com/event/brodie-lane-2/")
gh("2026-07-09","8:30pm–10:30pm","Jessee Lee — Honky Tonk Thursday","https://gruenehall.com/event/jessee-lee/")
gh("2026-07-10","12:00pm–4:00pm","Eric Heideman Band","https://gruenehall.com/event/eric-heideman-band-3/")
gh("2026-07-10","4:00pm–7:00pm","Friday Afternoon Club","https://gruenehall.com/event/friday-afternoon-club-13/2026-07-10/")
gh("2026-07-10","Doors 7pm / 9:30pm","Bleu Edmondson","https://www.prekindle.com/event/17481-bleu-edmondson-new-braunfels","$20")
gh("2026-07-11","11:00am–1:00pm","Andi Holleman","https://gruenehall.com/event/andi-holleman-6/")
gh("2026-07-11","1:00pm–5:00pm","Heath Walker Band","https://gruenehall.com/event/heath-walker-band/")
gh("2026-07-11","Doors 8pm / 10:30pm","Them Dirty Roses","https://www.prekindle.com/event/17898-them-dirty-roses-new-braunfels","$25")
gh("2026-07-12","11:30am–2:30pm","Clayton Chapin","https://gruenehall.com/event/clayton-chapin-9/")
gh("2026-07-12","3:00pm–6:00pm","Bret Graham","https://gruenehall.com/event/bret-graham-141/")
gh("2026-07-12","6:30pm–9:30pm","Spencer Johnson","https://gruenehall.com/event/spencer-johnson-2/")
gh("2026-07-13","6:00pm–8:00pm","JESKA Songswap with Special Guests","https://gruenehall.com/event/jeska-songswap-with-special-guests-4/")
gh("2026-07-13","8:30pm–10:30pm","Owen Stroud","https://gruenehall.com/event/owen-stroud-4/")
gh("2026-07-14","7:00pm–11:00pm","Two Ton Tuesday","https://www.gruenetexas.com/two-ton-tuesdays/","$15")
gh("2026-07-15","6:00pm–10:00pm","The Georges","https://gruenehall.com/event/the-georges-101/")
gh("2026-07-16","Doors 7pm / 9pm","Billy Bob Thornton & The Boxmasters — Morro Rock Tour","https://www.prekindle.com/event/53319-billy-bob-thornton-and-the-boxmasters-2026-morro-rock-tour-new-braunfels","$75 SOLD OUT")
gh("2026-07-17","11:00am–2:30pm","Kayla Jane","https://gruenehall.com/event/kayla-jane-13/")
gh("2026-07-17","4:00pm–7:00pm","Friday Afternoon Club","https://gruenehall.com/event/friday-afternoon-club-13/2026-07-17/")
gh("2026-07-17","Doors 7pm / 9pm","Gary P. Nunn","https://www.prekindle.com/event/62779-gary-p-nunn-new-braunfels","$30 / VIP $125")
gh("2026-07-18","11:00am–1:00pm","Elysha LeMaster","https://gruenehall.com/event/elysha-lemaster-5/")
gh("2026-07-18","1:00pm–5:00pm","Red Iron Push","https://gruenehall.com/event/red-iron-push-21/")
gh("2026-07-18","Doors 8pm / 10:30pm","Stoney LaRue","https://www.prekindle.com/event/64281-stoney-larue-new-braunfels","$30")
gh("2026-07-19","11:30am–2:30pm","Lindsay Beaver","https://gruenehall.com/event/lindsay-beaver-13/")
gh("2026-07-19","3:00pm–6:00pm","Mike McLoud Dean","https://gruenehall.com/event/mike-mcloud-dean/")
gh("2026-07-19","6:30pm–9:30pm","Bradley Thomas","https://gruenehall.com/event/bradley-thomas-9/")
gh("2026-07-20","6:00pm–8:00pm","Bret Graham","https://gruenehall.com/event/bret-graham-142/")
gh("2026-07-20","8:30pm–10:30pm","Ruben V","https://gruenehall.com/event/ruben-v-3/")
gh("2026-07-21","7:00pm–11:00pm","Two Ton Tuesday","https://www.gruenetexas.com/two-ton-tuesdays/","$15")
gh("2026-07-22","Doors 7pm / 8pm","Roger Creager's Birthday Show (Acoustic)","https://www.prekindle.com/event/57678-roger-creagers-birthday-show-acoustic-with-special-guest-new-braunfels","$20")
gh("2026-07-23","Doors 7pm / 9:30pm","Roger Creager's Birthday Show (Full Band)","https://www.prekindle.com/event/43648-roger-creagers-birthday-show-full-band-new-braunfels","$25")
gh("2026-07-24","1:00pm–4:00pm","Chuck Wimer","https://gruenehall.com/event/chuck-wimer-2/")
gh("2026-07-24","4:00pm–7:00pm","Friday Afternoon Club","https://gruenehall.com/event/friday-afternoon-club-13/2026-07-24/")
gh("2026-07-24","Doors 7pm / 9:30pm","Roger Creager's Birthday Show (Full Band)","https://www.prekindle.com/event/49726-roger-creagers-birthday-show-full-band-new-braunfels","$25")
gh("2026-07-25","11:00am–1:00pm","Paige Price","https://gruenehall.com/event/paige-price-3/")
gh("2026-07-25","1:00pm–5:00pm","Lee Mathis & The Brutally Handsome","https://gruenehall.com/event/lee-mathis-the-brutally-handsome-2/")
gh("2026-07-25","Doors 8pm / 10:30pm","Roger Creager's Birthday Show (Full Band)","https://www.prekindle.com/event/44958-roger-creagers-birthday-show-full-band-new-braunfels","$25")
gh("2026-07-26","11:30am–2:30pm","Allan Hendrickson","https://gruenehall.com/event/allan-hendrickson-13/")
gh("2026-07-26","3:00pm–6:00pm","Michael Monroe Goodman","https://gruenehall.com/event/michael-monroe-goodman-22/")
gh("2026-07-26","6:30pm–9:30pm","Shay Domann","https://gruenehall.com/event/shay-domann-2/")
gh("2026-07-27","6:00pm–8:00pm","JESKA Songswap with Special Guests","https://gruenehall.com/event/jeska-songswap-with-special-guests-5/")
gh("2026-07-27","8:30pm–10:30pm","Tony Taylor & Friends","https://gruenehall.com/event/tony-taylor-friends-30/")
gh("2026-07-29","6:00pm–10:00pm","The Georges","https://gruenehall.com/event/the-georges-102/")
gh("2026-07-30","7:00pm–8:00pm","Kyle Gates","https://gruenehall.com/event/kyle-gates/")
gh("2026-07-30","8:30pm–10:30pm","Luke Prater — Honky Tonk Thursday","https://gruenehall.com/event/luke-prater/")
gh("2026-07-31","12:00pm–4:00pm","Jesse Stratton Band","https://gruenehall.com/event/jesse-stratton-band-6/")
gh("2026-07-31","4:00pm–7:00pm","Friday Afternoon Club","https://gruenehall.com/event/friday-afternoon-club-13/2026-07-31/")
gh("2026-07-31","Doors 7pm / 9:30pm","Matt Kirk & The Güeyfarers","https://www.prekindle.com/event/32621-matt-kirk-and-the-geyfarers-new-braunfels","$15")

# ---------------- WHITEWATER AMPHITHEATER (New Braunfels) ----------------
WW="https://www.whitewaterrocks.com/upcoming-shows"
events += [
 E("2026-06-30","Whitewater Amphitheater","New Braunfels","Music","Bob Dylan w/ Lucinda Williams, The John Doe Folk Trio","7:00pm","https://www.tixr.com/groups/whitewaterrocks/events/bob-dylan-184409",WW,"Ticketed"),
 E("2026-07-11","Whitewater Amphitheater","New Braunfels","Music","Randy Rogers Band w/ Pat Green, Slade Coulter","7:30pm","https://www.tixr.com/groups/whitewaterrocks/events/randy-rogers-band-172752",WW,"Ticketed"),
 E("2026-07-17","Whitewater Amphitheater","New Braunfels","Music","Flatland Cavalry w/ Bottomland, Telander","8:00pm","https://www.tixr.com/groups/whitewaterrocks/events/flatland-cavalry-176642",WW,"Ticketed"),
 E("2026-07-18","Whitewater Amphitheater","New Braunfels","Music","Dwight Yoakam","Gates TBD","https://www.tixr.com/groups/whitewaterrocks/events/dwight-yoakam-186162",WW,"Ticketed"),
 E("2026-07-25","Whitewater Amphitheater","New Braunfels","Music","The Black Keys: Peaches N Kream w/ Eddie 9V","Gates TBD","https://www.tixr.com/groups/whitewaterrocks/events/the-black-keys-peaches-n-kream-175962",WW,"Ticketed"),
]

# ---------------- BRAUNTEX THEATRE (New Braunfels) ----------------
BT="https://brauntex.org/brauntex-upcoming-events/"
events += [
 E("2026-06-24","Brauntex Theatre","New Braunfels","Theater/Arts","Summer Cinema: A League of Their Own (1992)","6:30pm","https://brauntex.org/event/summer-cinema-a-league-of-their-own-1992/",BT),
 E("2026-06-27","Brauntex Theatre","New Braunfels","Theater/Arts","Buckets N Boards: Comedy Percussion Show","7:30pm","https://brauntex.org/event/buckets-n-boards-comedy-percussion-show/",BT,"Ticketed"),
 E("2026-07-01","Brauntex Theatre","New Braunfels","Music","SA Jazz Society: Will Holiday's Grand Ol' Americana Show","7:30pm","https://brauntex.org/event/san-antonio-jazz-society-presents-will-holidays-grand-ol-americana-show/",BT,"Ticketed"),
 E("2026-07-02","Brauntex Theatre","New Braunfels","Music","Neal McCoy","7:30pm","https://brauntex.org/event/neal-mccoy/",BT,"Ticketed"),
 E("2026-07-08","Brauntex Theatre","New Braunfels","Theater/Arts","Summer Cinema: High School Musical","6:30pm",BT,BT),
 E("2026-07-10","Brauntex Theatre","New Braunfels","Music","Hindley Street Country Club","7:30pm","https://brauntex.org/event/hindley-street-country-club-2/",BT,"Ticketed"),
 E("2026-07-15","Brauntex Theatre","New Braunfels","Theater/Arts","Summer Cinema: Trolls","6:30pm",BT,BT),
 E("2026-07-18","Brauntex Theatre","New Braunfels","Music","Jimmy's Buffet — Celebrating the Music of Jimmy Buffett","7:30pm","https://brauntex.org/event/jimmys-buffet-celebrating-the-music-of-jimmy-buffett/",BT,"Ticketed"),
 E("2026-07-22","Brauntex Theatre","New Braunfels","Theater/Arts","Summer Cinema: Hairspray","6:30pm",BT,BT),
 E("2026-07-25","Brauntex Theatre","New Braunfels","Music","Already Gone: A Tribute to the Eagles","7:30pm","https://brauntex.org/event/midales-entertainment-presents-already-gone-a-tribute-to-the-eagles/",BT,"Ticketed"),
 E("2026-07-29","Brauntex Theatre","New Braunfels","Theater/Arts","Summer Cinema: Grease 2","6:30pm",BT,BT),
]

# ---------------- OLD GRUENE MARKET DAYS ----------------
GM="https://www.gruenetexas.com/market-days/"
events += [
 E("2026-06-20","Old Gruene Market Days","Gruene","Festival/Market","Artisan market (Day 1)","10:00am–5:00pm",GM,GM,"Free"),
 E("2026-06-21","Old Gruene Market Days","Gruene","Festival/Market","Artisan market (Day 2)","10:00am–5:00pm",GM,GM,"Free"),
 E("2026-07-18","Old Gruene Market Days","Gruene","Festival/Market","Artisan market (Day 1)","10:00am–5:00pm",GM,GM,"Free"),
 E("2026-07-19","Old Gruene Market Days","Gruene","Festival/Market","Artisan market (Day 2)","10:00am–5:00pm",GM,GM,"Free"),
]

# ---------------- NB COFFEE FESTIVAL ----------------
events.append(E("2026-07-11","13 Trees Coffee Haus & Roastery","New Braunfels","Festival/Market","2nd Annual New Braunfels Coffee Festival","8:00am–1:00pm","https://www.visitnbtx.com/events/2nd-annual-new-braunfels-coffee-festival","https://www.visitnbtx.com/events"))

# ---------------- JOHN T. FLOORE'S (Helotes) ----------------
FL="https://www.prekindle.com/events/john-t-floores-country-store"
def fl(date,act,url,time="8:30pm (Doors 7:00)",price="Ticketed"):
    events.append(E(date,"John T. Floore's Country Store","Helotes","Music",act,time,url,FL,price))
fl("2026-06-19","Casey Donahew","https://www.prekindle.com/event/48668-casey-donahew-helotes")
fl("2026-06-20","Tyler Halverson","https://www.prekindle.com/event/11167-tyler-halverson-helotes")
fl("2026-06-21","Dine and Dance","https://www.prekindle.com/event/38878-dine-and-dance-free-all-ages-helotes","4:00pm (Doors 3:00)","Free")
fl("2026-06-26","Dylan Wheeler","https://www.prekindle.com/event/63836-dylan-wheeler-helotes")
fl("2026-07-03","Carson Jeffrey","https://www.prekindle.com/event/67368-carson-jeffrey-helotes")
fl("2026-07-05","Dine and Dance","https://www.prekindle.com/event/34527-dine-and-dance-free-all-ages-helotes","4:00pm (Doors 3:00)","Free")
fl("2026-07-10","Josh Weathers","https://www.prekindle.com/event/66343-josh-weathers-helotes")
fl("2026-07-17","Clay Hollis","https://www.prekindle.com/event/91674-clay-hollis-helotes")
fl("2026-07-18","Cole Barnhill","https://www.prekindle.com/event/98949-cole-barnhill-helotes")
fl("2026-07-19","Dine and Dance","https://www.prekindle.com/event/89567-dine-and-dance-free-all-ages-helotes","4:00pm (Doors 3:00)","Free")

# ---------------- SAM'S BURGER JOINT (San Antonio – near Pearl) ----------------
SB="https://samsburgerjoint.com/calendar/"
def sb(date,act,url,time):
    events.append(E(date,"Sam's Burger Joint","San Antonio – near Pearl","Music",act,time,url,SB,"Ticketed"))
sb("2026-06-19","Ruben V","https://wl.seetickets.us/event/ruben-v/689011","8:30pm (Doors 7:30)")
sb("2026-06-20","THIRD EYE – Tribute to TOOL/A Perfect Circle/Puscifer (w/ ABACAB)","https://wl.seetickets.us/event/third-eye-a-live-tribute-to-tool-a-perfect-circle-and-pusci/683287","8:30pm (Doors 7:30)")
sb("2026-06-23","Live and Local with 210 Jazz Orchestra","https://wl.seetickets.us/event/live-and-local-with-210-jazz-orchestra/690994","7:30pm (Doors 6:30)")
sb("2026-06-25","Los #3 Dinners","https://wl.seetickets.us/event/los-3-dinners/690058","8:00pm (Doors 7:00)")
sb("2026-06-26","Blackbird Sing","https://wl.seetickets.us/event/blackbird-sing/694410","8:00pm (Doors 7:00)")
sb("2026-06-27","DeadEye – Grateful Dead Tribute Band","https://wl.seetickets.us/event/deadeye-grateful-dead-tribute-band/684445","8:30pm (Doors 7:30)")
sb("2026-07-02","Bonner Rhae","https://wl.seetickets.us/event/bonner-rhae/687297","8:00pm (Doors 7:00)")
sb("2026-07-03","Jimmy Spacek and Bobby Mack","https://wl.seetickets.us/event/jimmy-spacek-and-bobby-mack/691915","8:00pm (Doors 7:00)")
sb("2026-07-04","Hayes Duffy","https://wl.seetickets.us/event/hayes-duffy/693041","3:00pm (Doors 2:00)")
sb("2026-07-08","Tunnel Vision","https://wl.seetickets.us/event/tunnel-vision/690467","8:00pm (Doors 7:00)")
sb("2026-07-09","The Last Jimenez + The Chris Cuevas Project","https://wl.seetickets.us/event/the-last-jimenez-plus-the-chris-cuevas-project/693227","7:30pm (Doors 7:00)")
sb("2026-07-10","Finding Friday","https://wl.seetickets.us/event/finding-friday/692468","8:30pm (Doors 7:30)")
sb("2026-07-11","Passing Strangers 'The High School Reunion Show'","https://wl.seetickets.us/event/passing-strangers-the-high-school-reunion-show/691314","8:00pm (Doors 7:00)")
sb("2026-07-12","Eric Schwartz (comedy/music)","https://wl.seetickets.us/event/eric-schwartz/692089","6:30pm (Doors 6:00)")
sb("2026-07-16","Gavin Story","https://wl.seetickets.us/event/gavin-story/694319","8:00pm (Doors 7:00)")
sb("2026-07-17","Texas Headhunters","https://wl.seetickets.us/event/texas-headhunters/692820","8:30pm (Doors 7:30)")
sb("2026-07-18","Rock and Roll Over (KISS Tribute)","https://wl.seetickets.us/event/rock-and-roll-over-tribute-to-kiss/691558","8:30pm (Doors 7:30)")
sb("2026-07-19","The Iguanas","https://wl.seetickets.us/event/the-iguanas/687878","8:00pm (Doors 7:00)")
sb("2026-07-21","School of Rock All-Stars","https://wl.seetickets.us/event/school-of-rock-allstars/690853","6:30pm (Doors 6:00)")
sb("2026-07-23","Pat Travers Band (w/ Eye of the Storm, Rock The Nation)","https://wl.seetickets.us/event/pat-travers-band/685276","7:30pm (Doors 7:00)")
sb("2026-07-24","ondaStereo – Soda Stereo Tribute","https://wl.seetickets.us/event/ondastereo-soda-stereo-tribute/691754","8:00pm (Doors 7:00)")
sb("2026-07-25","Bloody Cape – Deftones Tribute (w/ The English Channels)","https://wl.seetickets.us/event/bloody-cape-deftones-tribute/690565","8:30pm (Doors 7:30)")
sb("2026-07-26","Exit Stage Left – Tribute to RUSH","https://wl.seetickets.us/event/exit-stage-left-a-tribute-to-rush/692344","7:30pm (Doors 6:30)")
sb("2026-07-28","Live and Local with DiversiD","https://wl.seetickets.us/event/live-and-local-with-diversid/693044","7:30pm (Doors 6:30)")
sb("2026-07-31","Ellis Bullard","https://wl.seetickets.us/event/ellis-bullard/692631","8:30pm (Doors 7:30)")

# ---------------- SAN PEDRO PLAYHOUSE (San Antonio – San Pedro) ----------------
events.append(E("2026-06-26","San Pedro Playhouse","San Antonio – San Pedro","Theater/Arts","Evita (runs Jun 26–Jul 26)","See showtimes","https://ci.ovationtix.com/35749/production/1229046","https://www.sanpedroplayhouse.org/","Ticketed"))

# ---------------- THE PEARL (recurring markets) ----------------
PM="https://events.atpearl.com/series/farmers-market/"
for d in ["2026-06-20","2026-06-27","2026-07-04","2026-07-11","2026-07-18","2026-07-25"]:
    events.append(E(d,"The Pearl","San Antonio – Pearl","Festival/Market","Pearl Farmers Market","9:00am–1:00pm","https://atpearl.com/weekend-market/",PM,"Free"))
for d in ["2026-06-21","2026-06-28","2026-07-05","2026-07-12","2026-07-19","2026-07-26"]:
    events.append(E(d,"The Pearl","San Antonio – Pearl","Festival/Market","Pearl Makers Market","10:00am–2:00pm","https://atpearl.com/weekend-market/",PM,"Free"))
events.append(E("2026-07-15","The Pearl","San Antonio – Pearl","Festival/Market","Children's Entrepreneur Night Market","5:00–8:00pm","https://events.atpearl.com/series/childrens-entrepreneur-night-market/","https://events.atpearl.com/events/","Free"))

# ---------------- CAVE WITHOUT A NAME (Boerne) ----------------
events += [
 E("2026-06-20","Cave Without a Name","Boerne","Music","Summer Solstice – Rudi & the Rudiments","7:30pm","https://www.cavewithoutaname.com/content/summer-solstice-rudi-rudiments-2026","https://www.cavewithoutaname.com/event-calendar","Ticketed"),
 E("2026-07-03","Cave Without a Name","Boerne","Music","Summer Classics – The Tinsel Singers","7:30pm","https://www.cavewithoutaname.com/","https://www.cavewithoutaname.com/event-calendar","Ticketed"),
]

# ---------------- CIBOLO CENTER FOR CONSERVATION — MOONDANCE (Boerne) ----------------
MD="https://cibolo.org/moondance/"
events += [
 E("2026-06-27","Cibolo Center for Conservation","Boerne","Music","Moondance Series — Texas String Assembly","7:00–9:00pm (Doors 6)","https://secure.qgiv.com/for/thecibolocenterforconservation/event/moondance-2026/",MD,"$15"),
 E("2026-07-25","Cibolo Center for Conservation","Boerne","Music","Moondance Series — Band in Black","7:00–9:00pm (Doors 6)","https://secure.qgiv.com/for/thecibolocenterforconservation/event/moondance-2026/",MD,"$15"),
]

# ---------------- BOERNE MARKET DAYS / FESTIVALS ----------------
events += [
 E("2026-06-19","Boerne Main Plaza Park","Boerne","Festival/Market","Das Festival of Kendall 2026 (runs Jun 19–21)","5:00–11:30pm","https://theboernelife.com/events/das-festival-of-kendall-2026-at-main-plaza-park/2026-06-19/","https://theboernelife.com/events/"),
 E("2026-07-11","Boerne Market Days (Main Plaza)","Boerne","Festival/Market","2nd-weekend artisan market w/ live Texas musicians (Day 1)","10:00am–5:00pm","https://eventsoffmain.com/market-days/","https://business.boerne.org/events/calendar","Free"),
 E("2026-07-12","Boerne Market Days (Main Plaza)","Boerne","Festival/Market","2nd-weekend artisan market w/ live Texas musicians (Day 2)","10:00am–4:00pm","https://eventsoffmain.com/market-days/","https://business.boerne.org/events/calendar","Free"),
 E("2026-06-30","Boerne Main Plaza","Boerne","Music","Abendkonzert – Boerne Village Band","7:30–9:00pm","https://www.ci.boerne.tx.us/m/newsflash/home/detail/720","https://www.ci.boerne.tx.us/m/newsflash/home/detail/720","Free"),
 E("2026-07-28","Boerne Main Plaza","Boerne","Music","Abendkonzert – Boerne Village Band","7:30–9:00pm","https://www.ci.boerne.tx.us/m/newsflash/home/detail/720","https://www.ci.boerne.tx.us/m/newsflash/home/detail/720","Free"),
]

# ---------------- TAPATIO SPRINGS (Boerne) — La Cascada Live Music ----------------
TS="https://www.tapatioclub.com/Signature_Events/Live_Music_Series_(1)"
def ts(date,act):
    events.append(E(date,"Tapatio Springs Resort","Boerne","Music",act,"6:30–10:30pm",TS,TS,"Free"))
ts("2026-06-19","Chris Lopez"); ts("2026-06-20","Ruben Pacheco"); ts("2026-06-21","Jaime Valera (Father's Day)")
ts("2026-06-26","Noah Kurtis"); ts("2026-06-27","Johnny Murphy"); ts("2026-07-03","Austin Forrest")
ts("2026-07-04","Juanski"); ts("2026-07-10","Lacy Brinson"); ts("2026-07-11","Faith Jacobs")
ts("2026-07-17","Chris Lopez"); ts("2026-07-18","Ruben Pacheco"); ts("2026-07-24","Wally Robles")
ts("2026-07-25","Anthony Wright"); ts("2026-07-31","Sierra Lynn")

# ---------------- COMFORT ----------------
CC="https://business.comfortchamber.com/calendar"
events += [
 E("2026-06-19","Bending Branch Winery","Comfort","Theater/Arts","Quarterly Reading: Sarah Bird (author event)","6:00–7:30pm","https://www.bendingbranchwinery.com/events/Quarterly-Reading-Sarah-Bird","https://www.bendingbranchwinery.com/Visit/Events","Free"),
 E("2026-06-20","Shopping with Siobhain","Comfort","Music","Live Music Saturday — Homer Whisenant","12:00–3:00pm","https://business.comfortchamber.com/calendar/Details/live-music-at-shopping-with-siobhain-1752982",CC,"Free"),
 E("2026-06-20","Cocky Rooster Bar","Comfort","Music","Kyle William Lindley","8:00pm–12:00am","https://business.comfortchamber.com/calendar/Details/kyle-william-lindley-cocky-rooster-1762744",CC),
 E("2026-06-25","8th Street Market","Comfort","Festival/Market","Trunk Show with C. Wilson Studios (also Jun 26)","10:00am–5:00pm","https://business.comfortchamber.com/calendar/Details/trunk-show-with-c-wilson-studios-at-8th-street-market-1758049",CC,"Free"),
 E("2026-06-25","Shopping with Siobhain","Comfort","Music","Steak Night Social (live music)","6:00–9:00pm","https://business.comfortchamber.com/calendar/Details/steak-night-social-at-shopping-with-siobhain-1695466",CC),
 E("2026-06-26","Cocky Rooster Bar","Comfort","Music","C-Rock","8:00pm–12:00am","https://business.comfortchamber.com/calendar/Details/c-rock-cocky-rooster-1748094",CC),
 E("2026-06-27","Shopping with Siobhain","Comfort","Music","Live Music Saturday — Homer Whisenant","12:00–3:00pm","https://business.comfortchamber.com/calendar/Details/live-music-at-shopping-with-siobhain-1752992",CC,"Free"),
 E("2026-06-27","Cocky Rooster Bar","Comfort","Music","Josh Murley","8:00pm–12:00am","https://business.comfortchamber.com/calendar/Details/josh-murley-cocky-rooster-1768352",CC),
 E("2026-07-09","Shopping with Siobhain","Comfort","Music","Steak Night Social (live music)","6:00–9:00pm",CC,CC),
 E("2026-07-23","Shopping with Siobhain","Comfort","Music","Steak Night Social (live music)","6:00–9:00pm",CC,CC),
 E("2026-07-25","Bending Branch Winery","Comfort","Theater/Arts","A Taste of Texas & Italy (guided tasting)","1:00–3:00pm","https://www.eventbrite.com/e/a-taste-of-texas-italy-tickets-1992233677559","https://www.bendingbranchwinery.com/Visit/Events","$75–85"),
]

# assign display group
for e in events:
    e["group"] = AREAS.get(e["area"], e["area"])

events.sort(key=lambda e: (e["date"], e["time"]))
out = {
    "generated": datetime.datetime.now().isoformat(timespec="seconds"),
    "window": {"start": "2026-06-19", "end": "2026-07-31"},
    "count": len(events),
    "events": events,
}
with open("/sessions/keen-elegant-curie/mnt/Knox/Knox/Projects/boerne-events/events.json","w") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)
print("Wrote events.json with", len(events), "events")
# quick category/group tallies
from collections import Counter
print("By group:", dict(Counter(e["group"] for e in events)))
print("By category:", dict(Counter(e["category"] for e in events)))
