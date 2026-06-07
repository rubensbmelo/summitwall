"""Body fragments for each page. Imported by build.py."""

CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>'

SERVICES = [
    ("01","Steel Stud Framing","Precise light-gauge steel stud framing for interior partitions, load-bearing walls and complex layouts — straight, square and code-compliant.",["Interior","Exterior","Load-Bearing"]),
    ("02","Insulation","Batt and sound attenuation insulation installed for energy efficiency, fire separation and noise control — fully code-compliant for Alberta.",["Batt","Sound","Fire Separation"]),
    ("03","Drywall Installation","Professional hanging of standard, moisture-resistant and fire-rated gypsum board. Clean cuts, tight joints, solid fastening.",["Standard","Moisture-Resist","Fire-Rated"]),
    ("04","Taping and Finishing","Seamless taping, mudding and sanding that eliminates visible joints — glass-smooth walls ready to paint.",["Taping","Mudding","Sanding"]),
    ("05","Painting","Interior painting with premium primers and topcoats. Clean lines, even coverage and a finish that lasts.",["Interior","Primer","Commercial"]),
    ("06","Site Cleanup","Full jobsite cleanup after every phase — debris removed, surfaces protected and your space left ready for the next trade or final walk-through.",["Daily Cleanup","Debris Removal","Final Clean"]),
]

def svc_grid():
    cards = ""
    for num,name,desc,tags in SERVICES:
        t = "".join(f"<span>{x}</span>" for x in tags)
        cards += f'<div class="svc reveal"><span class="num">{num}</span><h3>{name}</h3><p>{desc}</p><div class="svc-tags">{t}</div></div>'
    return f'<div class="svc-grid">{cards}</div>'

def promises():
    items = [
        ("1-Year Warranty","All our work is backed by a full 12-month workmanship warranty. If something isn't right, we fix it — no questions asked."),
        ("Booked in 48 hrs","Most projects are scheduled within 48 hours of estimate approval. We respect your timeline."),
        ("Clean Jobsite Daily","Our crew cleans up at the end of every work day. No mess left behind, no dust through your home."),
        ("No Surprise Charges","You get a written estimate before any work begins. The price we quote is the price you pay."),
    ]
    icons = [
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>',
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>',
    ]
    cards = "".join(f'<div class="pr reveal">{icons[i]}<h3>{h}</h3><p>{p}</p></div>' for i,(h,p) in enumerate(items))
    return f'''<section class="section maroon"><div class="wrap"><div class="reveal"><div class="eyebrow">Our Commitment</div><h2 style="color:#fff">What you can always count on.</h2></div><div class="pr-grid">{cards}</div></div></section>'''

def calculator():
    return '''<section class="section dark" id="estimate"><div class="wrap">
      <div class="reveal"><div class="eyebrow">Free Estimator</div><h2>How much will your project cost?</h2>
      <p class="intro">Select your services and project size for an instant price range. A free in-home estimate confirms exact pricing.</p></div>
      <div class="calc-box reveal">
        <div class="calc-step"><label>1 — Services needed</label><div class="chip-row" data-group="multi">
          <button class="chip" data-svc="frame">Steel Stud Framing</button><button class="chip" data-svc="insulation">Insulation</button>
          <button class="chip" data-svc="drywall">Drywall Installation</button><button class="chip" data-svc="taping">Taping and Finishing</button>
          <button class="chip" data-svc="painting">Painting</button><button class="chip" data-svc="cleanup">Site Cleanup</button></div></div>
        <div class="calc-step"><label>2 — Project size</label><div class="chip-row" data-group="single">
          <button class="chip active" data-size="small">Small · 1–2 rooms</button>
          <button class="chip" data-size="medium">Medium · Basement</button>
          <button class="chip" data-size="large">Large · Full home</button></div></div>
        <div class="calc-step"><label>3 — Project type</label><div class="chip-row" data-group="single">
          <button class="chip active" data-type="res">Residential</button>
          <button class="chip" data-type="com">Commercial</button></div></div>
        <button class="calc-cta" id="calc-run">Calculate My Estimate &rarr;</button>
        <div class="calc-result" id="calc-result">
          <div class="range">$<span id="calc-lo">0</span> – $<span id="calc-hi">0</span> <em>CAD</em></div>
          <p class="note">Based on approx. <span id="calc-sqft">0</span> sq ft. Final price confirmed at your free in-home estimate.</p>
          <a href="contact.html" class="btn btn-primary">Book My Free Estimate</a>
        </div>
      </div></div></section>'''

def testimonials():
    revs = [
        ("J","Jason M.","West Edmonton","Rodrigo and his team did an exceptional job on our basement. Framing was precise, drywall seamless, taping flawless — and they left the site cleaner than they found it every day."),
        ("S","Sarah K.","Sherwood Park","Professional and reliable from start to finish. Showed up on time every day. The finish work on our ceilings and walls is absolutely perfect."),
        ("C","Carlos B.","St. Albert","Best drywall contractor we've used in Edmonton. Fair pricing, great communication and zero surprises on the invoice. Highly recommend."),
    ]
    cards = "".join(f'<div class="tcard reveal"><div class="stars">★★★★★</div><blockquote>"{q}"</blockquote><div class="who"><div class="avatar">{a}</div><div><b>{n}</b><span>{loc}, AB</span></div></div></div>' for a,n,loc,q in revs)
    return f'''<section class="section alt"><div class="wrap"><div class="reveal"><div class="eyebrow">Client Reviews</div><h2>What Edmonton homeowners say.</h2><p class="intro">Replace these with your real Google reviews before launch.</p></div><div class="tcards">{cards}</div></div></section>'''

def cta_strip(phone):
    return f'''<section class="cta-strip"><div class="wrap reveal"><h2>Let's get your project moving.</h2><p>Free, no-obligation estimates. WCB insured. Booked within 48 hours.</p><a href="tel:5873578181" class="phone">{phone}</a></div></section>'''

FAQS = [
    ("How much does drywall installation cost in Edmonton?","Costs vary by scope. Drywall installation and taping typically runs <strong>$2–$4 per sq ft</strong>. A full project with framing, insulation, drywall and paint can range from <strong>$3,000 to $25,000+</strong>. Use our estimator or call for a free quote."),
    ("Are you WCB insured and licensed in Alberta?","Yes. Summit Wall Solutions carries <strong>full WCB coverage</strong> and holds a valid Edmonton business licence. Documentation available on request."),
    ("Do you offer a warranty?","Every project is backed by a <strong>1-year workmanship warranty</strong>. If anything isn't right, we come back and fix it at no cost."),
    ("How long does a project take?","A single room is typically <strong>2–4 days</strong>; a full basement <strong>1–2 weeks</strong>. We give you a clear timeline before any work begins."),
    ("Which areas do you serve?","Edmonton plus <strong>St. Albert, Sherwood Park, Spruce Grove, Leduc, Fort Saskatchewan and Stony Plain</strong>."),
    ("Residential and commercial?","Both. Custom homes, basement developments, condo renovations, office fit-outs and commercial interiors."),
]
def faq():
    items = "".join(f'<div class="faq-item"><div class="faq-q"><h3>{q}</h3><span class="pm">+</span></div><div class="faq-a"><p>{a}</p></div></div>' for q,a in FAQS)
    return f'''<section class="section"><div class="wrap"><div class="reveal"><div class="eyebrow">FAQ</div><h2>Common questions, straight answers.</h2></div><div class="faq reveal">{items}</div></div></section>'''


SVC_PAGE_DATA = [
    {
        "slug":      "drywall-installation",
        "name":      "Drywall Installation",
        "h1":        "Drywall <em>Installation</em><br>in Edmonton",
        "badge":     "Drywall Installation · Edmonton, AB",
        "meta":      "Professional drywall installation in Edmonton, AB — standard, moisture-resistant and fire-rated gypsum board. Residential & commercial. Free estimates.",
        "hero_lead": "Professional drywall installation for Edmonton homes, basements and commercial spaces — standard, moisture-resistant and fire-rated board, hung tight and ready for finishing. Free estimates · WCB insured · Since 2017.",
        "intro":     "Summit Wall Solutions provides professional drywall installation in Edmonton for basement developments, new builds, condo renovations and commercial tenant improvements. We hang standard 1/2\" and 5/8\" gypsum board, moisture-resistant (MR) board for kitchens and bathrooms, and fire-rated Type X board wherever code requires — cut tight, fastened solid and squared up so the finishing coat looks as good as it lasts.",
        "includes":  [
            "Standard 1/2\" and 5/8\" gypsum board installation",
            "Moisture-resistant (MR/green board) for wet areas",
            "Fire-rated Type X board for code-required assemblies",
            "Stairwells, vaulted ceilings and curved walls",
            "All fastening to Alberta building code",
            "Coordinated with our taping crew for a seamless finish",
        ],
        "faq_h2":    "Common questions about drywall installation in Edmonton.",
        "faqs":      [
            ("How much does drywall installation cost in Edmonton?",
             "Drywall installation typically runs <strong>$1.75–$3.00 per sq ft</strong> depending on board type and project complexity. A full basement (800–1,000 sq ft) can range from $1,400–$3,000 for installation alone. Call for a free, no-obligation estimate."),
            ("Do you use moisture-resistant or fire-rated drywall where required?",
             "Yes. We specify and install the correct board type for each area — standard 1/2\", 5/8\" Type X (fire-rated) and MR board — to meet Alberta building code. We won't cut corners on fire-rated assemblies."),
            ("Do you supply the drywall or does the homeowner provide materials?",
             "We typically supply all materials as part of our project pricing. If you have materials on site already, we can work with what you have — just let us know upfront."),
        ],
        "link_desc": "Standard, moisture-resistant and fire-rated board — cut tight and code-compliant.",
    },
    {
        "slug":      "steel-stud-framing",
        "name":      "Steel Stud Framing",
        "h1":        "Steel Stud <em>Framing</em><br>in Edmonton",
        "badge":     "Steel Stud Framing · Edmonton, AB",
        "meta":      "Light-gauge steel stud framing in Edmonton, AB — interior partitions, load-bearing walls and complex layouts. Residential & commercial. Free estimates.",
        "hero_lead": "Precise light-gauge steel stud framing for Edmonton homes and commercial spaces — partition walls, load-bearing assemblies, curved features and complex layouts, straight and square every time. Free estimates · WCB insured · Since 2017.",
        "intro":     "Summit Wall Solutions frames interior partitions, load-bearing walls and complex layouts using light-gauge galvanized steel studs — a durable, moisture-resistant alternative to wood that stays straight and plumb for the long term. We frame for basement developments, new builds, condo renovations and commercial TIs across Edmonton. Whether it's a simple partition wall or a multi-room basement layout with bulkheads and curved features, our framing crew delivers clean, code-compliant work.",
        "includes":  [
            "Interior partition walls (residential and commercial)",
            "Load-bearing and exterior wall framing",
            "Ceiling, soffit and bulkhead framing",
            "Curved walls, radius features and coffered ceilings",
            "Window and door rough openings framed to spec",
            "All work to Alberta building code",
        ],
        "faq_h2":    "Common questions about steel stud framing in Edmonton.",
        "faqs":      [
            ("Why steel studs instead of wood framing for basements?",
             "Steel studs don't warp, shrink or crack over time — they stay straight and plumb. They're lighter, easier to cut, non-combustible and preferred for commercial construction. For Edmonton basements, steel is especially popular because it won't absorb moisture the way wood can against a concrete foundation wall."),
            ("Do you do steel stud framing for basement developments in Edmonton?",
             "Yes — basement framing is one of our most common projects. We frame all partition walls, utility areas, egress windows and bedroom walls to Alberta building code. Framing a standard 800–1,000 sq ft basement typically takes <strong>1–2 days</strong>."),
            ("Can you frame curved walls, bulkheads or non-standard layouts?",
             "Yes. We regularly work on curved features, bulkheads, coffered ceilings and other non-standard layouts. Bring us the plans and we'll build it."),
        ],
        "link_desc": "Interior partitions, load-bearing walls and complex layouts — straight and square.",
    },
    {
        "slug":      "taping-and-finishing",
        "name":      "Taping & Finishing",
        "h1":        "Taping &amp; <em>Finishing</em><br>in Edmonton",
        "badge":     "Taping & Finishing · Edmonton, AB",
        "meta":      "Professional drywall taping and finishing in Edmonton, AB — seamless joints, mudding and sanding for a paint-ready surface. Residential & commercial.",
        "hero_lead": "Seamless drywall taping and finishing for Edmonton homes and businesses — tape, mud and sand to a Level 4 or Level 5 finish that's paint-ready and stands up to scrutiny under raking light. Free estimates · WCB insured · Since 2017.",
        "intro":     "Summit Wall Solutions delivers clean, professional drywall taping and finishing for Edmonton basements, new builds, renovations and commercial spaces. Our finishers apply tape, compound and finish coats to eliminate every visible joint and seam — leaving walls and ceilings paint-ready with a flat, smooth surface. We work to Level 4 finish (standard residential) or Level 5 (premium/gloss applications) depending on the project specification.",
        "includes":  [
            "Paper and fibreglass mesh tape application",
            "First coat, second coat and skim coat mudding",
            "Sanding between coats for a smooth surface",
            "Corner bead installation and finishing",
            "Nail, screw and fastener dimple filling",
            "Level 4 (residential) and Level 5 (premium/gloss) finishes available",
        ],
        "faq_h2":    "Common questions about drywall taping and finishing in Edmonton.",
        "faqs":      [
            ("What is the difference between Level 4 and Level 5 drywall finish?",
             "Level 4 is standard residential quality — joints, fasteners and tape are filled and sanded smooth, suitable for flat or eggshell paint. Level 5 adds a full skim coat over the entire surface for a flawless result under gloss paint or critical lighting. We recommend Level 5 for ceilings with downlights and premium living spaces."),
            ("How long does taping and finishing take in Edmonton?",
             "A typical basement (800–1,000 sq ft) takes <strong>3–5 days</strong> for taping and finishing, including dry time between coats. We'll give you a clear timeline before work begins."),
            ("Can you match existing wall texture on a renovation?",
             "Yes. If you're renovating and need new drywall to blend with existing texture — orange peel, knockdown, smooth or anything in between — we can match it. Send us photos and we'll assess the work required."),
        ],
        "link_desc": "Seamless joints, mudding and sanding to Level 4 and Level 5 finishes.",
    },
    {
        "slug":      "insulation",
        "name":      "Insulation",
        "h1":        "Insulation <em>Services</em><br>in Edmonton",
        "badge":     "Insulation · Edmonton, AB",
        "meta":      "Batt and sound attenuation insulation in Edmonton, AB — energy efficiency, fire separation and noise control. Installed to Alberta code. Free estimates.",
        "hero_lead": "Code-compliant batt and sound-attenuation insulation for Edmonton homes — exterior walls, basement walls, party walls and ceiling assemblies, all installed to Alberta's energy code. Free estimates · WCB insured · Since 2017.",
        "intro":     "Summit Wall Solutions installs batt and sound-attenuation insulation for Edmonton residential and commercial projects — exterior walls, basement frost walls, ceilings and interior partitions — all to Alberta's energy code and National Building Code requirements. We coordinate insulation with our framing and drywall crews so your wall assembly is handled by one accountable team, keeping the project moving without gaps between trades.",
        "includes":  [
            "Exterior wall batt insulation (Alberta R-20+ requirements)",
            "Basement frost wall insulation",
            "Sound attenuation insulation for bedrooms, bathrooms and media rooms",
            "Fire-separation insulation for party walls and floor assemblies",
            "Vapour barrier installation, sealed to code",
            "All work to Alberta Building Code and NBC requirements",
        ],
        "faq_h2":    "Common questions about insulation in Edmonton.",
        "faqs":      [
            ("What R-value is required for Edmonton basement walls?",
             "Edmonton's cold climate and Alberta's energy code require <strong>R-14 minimum</strong> for basement walls, though R-20 is strongly recommended for comfort and energy savings. Requirements vary by wall assembly type. We'll specify the right product and thickness for your project and permit."),
            ("Do you supply and install the insulation?",
             "Yes — we supply and install as part of our full wall package. There's no need to source materials separately. If you have materials already on site, we can work with those too. Just let us know when you call."),
            ("Do you install vapour barrier as part of the insulation work?",
             "Yes. Vapour barrier is a critical part of Alberta wall assemblies — we install it correctly as part of every insulation package, sealed at all edges and penetrations to code."),
        ],
        "link_desc": "Batt and sound insulation for energy efficiency, noise control and fire separation.",
    },
    {
        "slug":      "painting",
        "name":      "Interior Painting",
        "h1":        "Interior <em>Painting</em><br>in Edmonton",
        "badge":     "Interior Painting · Edmonton, AB",
        "meta":      "Interior painting in Edmonton, AB — primer, walls, ceilings and trim. Clean lines, even coverage and a finish that lasts. Free estimates · WCB insured.",
        "hero_lead": "Interior painting for Edmonton homes and businesses — primer and finish coats on new drywall or renovation surfaces, clean lines and even coverage. We paint after our own taping or yours. Free estimates · WCB insured · Since 2017.",
        "intro":     "Summit Wall Solutions provides interior painting for Edmonton homes, basements, condo renovations and commercial tenant improvements. We finish every wall project with quality primer and topcoats — clean brush lines, roller texture matched to specification and a durable finish that holds up to daily life. Our painting crew works directly with our taping team, so we know the surface quality before the first primer coat goes on.",
        "includes":  [
            "Primer coat on all new drywall surfaces",
            "Two finish coats on walls and ceilings",
            "Trim, baseboard and door casing paint",
            "Colour-matching on renovations",
            "Drop cloth protection and clean setup/teardown",
            "Low-VOC premium paints available on request",
        ],
        "faq_h2":    "Common questions about interior painting in Edmonton.",
        "faqs":      [
            ("Do you supply paint or does the homeowner choose and buy it?",
             "You choose the colour and brand, we supply and apply it as part of our project pricing. If you have specific paint on hand, we can work with what you have. We recommend mid-sheen or eggshell for basements and high-traffic areas."),
            ("Do you paint ceilings and trim as well as walls?",
             "Yes — walls, ceilings, baseboards, trim and doors are all within our painting scope. We prime all new drywall first to seal the surface, then apply two finish coats for even, consistent coverage."),
            ("Can you paint over another contractor's drywall work?",
             "Yes. If your drywall was installed and taped by someone else, we'll assess the surface finish before starting and flag anything that needs attention. We can do touch-up skim coats if needed before priming."),
        ],
        "link_desc": "Primer, walls, ceilings and trim — quality finish coats on new drywall or renovations.",
    },
]


def build(page, CITIES, PHONE, EMAIL, EMAIL_DIRECT,
          ld=None, biz=None, bc=None, faq_sc=None, site=""):
    _ld  = ld     or (lambda *a: "")
    _biz = biz    or (lambda: {})
    _bc  = bc     or (lambda c: {})
    _faq = faq_sc or (lambda f: {})

    # Service guide link cards — used in services.html and generated as individual pages below
    svc_guide_cards = "".join(
        f'<div class="svc reveal">'
        f'<span class="num">0{i+1}</span>'
        f'<h3>{d["name"]}</h3>'
        f'<p>{d["link_desc"]}</p>'
        f'<div style="margin-top:18px"><a href="services/{d["slug"]}-edmonton.html" class="btn btn-dark">Full Guide &rarr;</a></div>'
        f'</div>'
        for i, d in enumerate(SVC_PAGE_DATA)
    )

    # ---------- HOME ----------
    home = f'''
  <div class="ticker-wrap"><div class="ticker-track" id="tick">
    {"".join(f"<span>{x}</span>" for x in ["★ Google Reviewed","✓ Free Estimates","✓ 1-Year Warranty","✓ WCB Insured","✓ Clean Jobsite Daily","✓ Edmonton & Area","✓ Since 2017","✓ Booked in 48 Hours","✓ No Surprise Charges","✓ Residential & Commercial"]*2)}
  </div></div>
  <section class="hero"><div class="hero-bg">
    <picture>
      <source srcset="assets/van.webp" type="image/webp">
      <img src="assets/van.jpg" alt="" aria-hidden="true" class="hero-photo-img" width="1536" height="1024" loading="eager">
    </picture>
    <div class="hero-photo-overlay"></div>
    <div class="sweep s1"></div><div class="sweep s2"></div><div class="sweep s3"></div></div>
    <div class="wrap">
      <div class="eyebrow-badge reveal in"><i></i> Building Your Dream, One Wall at a Time — Since 2017</div>
      <h1 class="reveal in">Edmonton's<br>Trusted <em>Drywall</em><br>Contractor.</h1>
      <p class="lead reveal in">Your local drywall contractor for steel framing, insulation, drywall installation, taping and painting. Residential and commercial — one accountable team, start to finish.</p>
      <div class="hero-actions reveal in">
        <a href="tel:5873578181" class="btn btn-primary">Call {PHONE}</a>
        <a href="services.html#estimate" class="btn btn-ghost">Get Instant Estimate</a>
      </div>
      <div class="hero-promises reveal in">
        <div>{CHECK} Free Estimates</div><div>{CHECK} 1-Year Warranty</div><div>{CHECK} WCB Insured</div><div>{CHECK} Booked in 48 hrs</div>
      </div>
    </div></section>
  <section class="section"><div class="wrap"><div class="reveal"><div class="eyebrow">What We Do</div><h2>One crew. Every layer of the wall.</h2></div>{svc_grid()}
    <div style="margin-top:40px"><a href="services.html" class="btn btn-dark">See All Services &rarr;</a></div></div></section>
  {promises()}
  {testimonials()}
  {cta_strip(PHONE)}
'''
    page("index.html", "Drywall Contractor in Edmonton, AB | Summit Wall Solutions",
         "Edmonton's trusted drywall contractor — steel framing, insulation, drywall installation, taping & painting. Free estimates. WCB insured.", home,
         canonical="",
         schema=_ld(_biz()))

    # ---------- SERVICES ----------
    services = f'''
  <section class="hero compact"><div class="hero-bg"><div class="sweep s1"></div><div class="sweep s2"></div></div>
    <div class="wrap"><div class="eyebrow-badge reveal in"><i></i> Services</div>
      <h1 class="reveal in">Drywall &amp;<br><em>Framing</em><br>Services.</h1>
      <p class="lead reveal in">Edmonton's full-service drywall contractor. From the first steel stud to the final coat of paint — one accountable team, start to finish.</p></div></section>
  <section class="section"><div class="wrap">{svc_grid()}</div></section>
  {calculator()}
  <section class="section alt"><div class="wrap"><div class="reveal"><div class="eyebrow">How It Works</div><h2>Simple from first call to final coat.</h2></div>
    <div class="steps">
      <div class="step reveal"><b>01</b><h3>Consult</h3><p>We visit your site, assess the scope and answer every question. No pressure.</p></div>
      <div class="step reveal"><b>02</b><h3>Quote</h3><p>A clear written estimate — itemized, honest, no hidden charges.</p></div>
      <div class="step reveal"><b>03</b><h3>Build</h3><p>Our crew arrives on schedule, works clean and communicates throughout.</p></div>
      <div class="step reveal"><b>04</b><h3>Sign Off</h3><p>We walk the finished job with you. Not done until you're satisfied.</p></div>
    </div></div></section>
  <section class="section"><div class="wrap">
    <div class="reveal"><div class="eyebrow">Edmonton Service Guides</div>
    <h2>Go deeper on any service.</h2>
    <p class="intro">Detailed pages for Edmonton homeowners and contractors — what each service includes, pricing guidance and specific FAQs.</p></div>
    <div class="svc-grid" style="margin-top:32px">{svc_guide_cards}</div>
  </div></section>
  {cta_strip(PHONE)}
'''
    page("services.html", "Drywall &amp; Steel Framing Services in Edmonton | Summit Wall Solutions",
         "Expert drywall contractor in Edmonton — steel stud framing, insulation, drywall installation, taping & painting. Free estimate calculator.", services,
         body_class="dark-hero",
         schema=_ld(_biz(), _bc([("Home", site+"/"), ("Services", site+"/services.html")])))

    # ---------- ABOUT ----------
    about = f'''
  <section class="hero compact"><div class="hero-bg"><div class="sweep s1"></div><div class="sweep s2"></div></div>
    <div class="wrap"><div class="eyebrow-badge reveal in"><i></i> About Us</div>
      <h1 class="reveal in">Edmonton's<br>Drywall Crew<br>You Can <em>Trust</em></h1></div></section>
  <section class="section"><div class="wrap about-grid">
    <div class="about-copy reveal">
      <div class="eyebrow">Who We Are</div>
      <p class="lead-line">We treat every wall like it's going in our own home.</p>
      <p>Founded by <strong>Rodrigo Gadelha Bandeira</strong> in Edmonton, AB, Summit Wall Solutions has built its reputation one clean corner at a time since 2017. We handle the full wall — framing, insulation, drywall, taping and paint — so you deal with one accountable team from start to finish.</p>
      <p>We start every job with a clear scope, stick to the schedule we commit to, and leave your site clean at the end of every day. Most of our business comes from repeat clients and referrals — that's the standard we hold ourselves to.</p>
      <p style="margin-top:20px;font-size:15px">Reach Rodrigo directly: <a href="mailto:{EMAIL_DIRECT}" style="color:#6E1A22;font-weight:600">{EMAIL_DIRECT}</a></p>
    </div>
    <div class="stats reveal">
      <div class="stat"><b>2017</b><span>Established</span></div>
      <div class="stat"><b>100%</b><span>Satisfaction</span></div>
      <div class="stat"><b>Full</b><span>Wall Service</span></div>
      <div class="stat"><b>Free</b><span>Estimates</span></div>
    </div></div></section>
  <section class="section tight alt">
    <figure class="photo-block reveal">
      <picture>
        <source srcset="assets/sign-jobsite.webp" type="image/webp">
        <img src="assets/sign-jobsite.jpg" alt="Summit Wall Solutions sign at an Edmonton jobsite" width="1536" height="1024" loading="lazy">
      </picture>
      <figcaption>Serving Edmonton &amp; surrounding areas — St. Albert, Sherwood Park, Spruce Grove, Leduc &amp; beyond</figcaption>
    </figure>
  </section>
  {promises()}
  {faq()}
  {cta_strip(PHONE)}
'''
    page("about.html", "Edmonton Drywall Contractor Since 2017 | Summit Wall Solutions",
         "Edmonton drywall contractor since 2017. Founded by Rodrigo Gadelha Bandeira — full-wall services, WCB insured, 1-year workmanship warranty.", about,
         body_class="dark-hero",
         schema=_ld(_biz(), _faq(FAQS), _bc([("Home", site+"/"), ("About", site+"/about.html")])))

    # ---------- CONTACT ----------
    contact = f'''
  <section class="hero compact"><div class="hero-bg"><div class="sweep s1"></div><div class="sweep s2"></div></div>
    <div class="wrap"><div class="eyebrow-badge reveal in"><i></i> Contact</div>
      <h1 class="reveal in">Get Your <em>Free</em><br>Drywall Estimate</h1></div></section>
  <section class="section dark"><div class="wrap">
    <div class="contact-grid">
      <div class="reveal">
        <div class="eyebrow">Get In Touch</div>
        <h2 style="color:#fff">Let's talk about your project.</h2>
        <p class="intro">We'll visit your site, assess the scope and give you an exact written quote — no obligation.</p>
        <div style="margin-top:30px">
          <a href="tel:5873578181" class="ci"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3-8.6A2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/></svg><span><span class="lbl">Phone</span><span class="val">{PHONE}</span></span></a>
          <a href="mailto:{EMAIL}" class="ci"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/></svg><span><span class="lbl">Email</span><span class="val">{EMAIL}</span></span></a>
          <a href="https://instagram.com/summitwallsolutins" class="ci"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor" stroke="none"/></svg><span><span class="lbl">Instagram</span><span class="val">@summitwallsolutins</span></span></a>
          <div class="ci" style="cursor:default"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg><span><span class="lbl">Location</span><span class="val">Edmonton, AB — Canada</span></span></div>
        </div>
        <div class="badge-row"><span>WCB Insured</span><span>Licensed in Alberta</span><span>Mon–Fri 7AM–5PM</span></div>
      </div>
      <div class="reveal">
        <div class="qform">
          <h3>Request a Free Estimate</h3>
          <div id="form-success" style="display:none;text-align:center;padding:24px;color:#fff"><h3>✓ Request Sent!</h3><p style="color:rgba(255,255,255,.7)">We'll be in touch within a few hours.</p></div>
          <form id="quote-form" data-subject="New Quote Request — Summit Wall" data-from-name="Contact Form — Summit Wall Solutions">
            <div class="chip-row" data-group="single" style="margin-bottom:16px">
              <button type="button" class="chip active" data-ptype="res">Residential</button>
              <button type="button" class="chip" data-ptype="com">Commercial</button>
            </div>
            <div class="form-row">
              <div class="field"><label>Name</label><input name="name" type="text" placeholder="Your full name" required></div>
              <div class="field"><label>Phone</label><input name="phone" type="tel" placeholder="587 000-0000" required></div>
            </div>
            <div class="field"><label>Service needed</label><select name="service">
              <option value="">Select a service…</option><option>Steel Stud Framing</option><option>Insulation</option><option>Drywall Installation</option><option>Taping and Finishing</option><option>Painting</option><option>Site Cleanup</option><option>Full Package</option><option>Not sure — need a consult</option></select></div>
            <div class="field"><label>Project details</label><textarea name="message" placeholder="Tell us about your project — size, location, timeline…"></textarea></div>
            <button type="submit" class="form-submit">Send My Request &rarr;</button>
          </form>
        </div>
      </div>
    </div></div></section>
  {faq()}
'''
    page("contact.html", "Free Drywall Estimate in Edmonton | Summit Wall Solutions",
         "Request a free drywall estimate from Edmonton's trusted contractor. Call 587-357-8181 or fill out the form. WCB insured, 1-year warranty.", contact,
         body_class="dark-hero",
         schema=_ld(_biz(), _faq(FAQS), _bc([("Home", site+"/"), ("Contact", site+"/contact.html")])))

    # ---------- FOR CONTRACTORS ----------
    contractors = f'''
  <section class="hero compact"><div class="hero-bg"><div class="sweep s1"></div><div class="sweep s2"></div></div>
    <div class="wrap">
      <div class="eyebrow-badge reveal in"><i></i> For General Contractors &amp; Builders</div>
      <h1 class="reveal in">A Drywall Sub<br>You Can <em>Count On</em></h1>
      <p class="lead reveal in">Quality workmanship, reliable schedules and clear communication — every project, every time. Summit Wall Solutions partners with GCs and builders across Edmonton to deliver full-scope wall packages on time and on budget.</p>
      <div class="hero-actions reveal in">
        <a href="tel:5873578181" class="btn btn-primary">Call {PHONE}</a>
        <a href="#sub-quote" class="btn btn-ghost">Request Sub Quote</a>
      </div>
      <div class="hero-promises reveal in">
        <div>{CHECK} WCB + Liability Insured</div><div>{CHECK} Schedule Committed</div><div>{CHECK} Clean Jobsite Daily</div><div>{CHECK} Edmonton &amp; Area</div>
      </div>
    </div>
  </section>

  <section class="section"><div class="wrap">
    <div class="reveal">
      <div class="eyebrow">What We Bring to Your Project</div>
      <h2>One wall crew. Full scope. No surprises.</h2>
      <p class="intro">We've built our reputation on three things: quality workmanship, meeting schedules, and clear communication. When you bring Summit Wall onto your project, you get a sub who shows up, performs, and keeps your foreman informed — not one you have to chase.</p>
    </div>
    <div class="svc-grid">
      <div class="svc reveal"><span class="num">01</span><h3>Full Drywall Packages</h3><p>Supply-and-install or labour-only packages covering framing, insulation, board, taping, finishing and cleanup — one sub, full scope, single point of contact.</p><div class="svc-tags"><span>Supply+Install</span><span>Labour-Only</span><span>Full Scope</span></div></div>
      <div class="svc reveal"><span class="num">02</span><h3>Framing Crews</h3><p>Experienced steel stud framing crews for light-gauge interior work on residential, commercial and TI projects. Square, plumb and code-compliant, every time.</p><div class="svc-tags"><span>Steel Stud</span><span>Light-Gauge</span><span>TI Ready</span></div></div>
      <div class="svc reveal"><span class="num">03</span><h3>Taping &amp; Finishing</h3><p>Level 4 and Level 5 finish available. Seamless joints, skim coat and sanding — walls ready for your painter the moment we are done.</p><div class="svc-tags"><span>Level 4</span><span>Level 5</span><span>Paint-Ready</span></div></div>
      <div class="svc reveal"><span class="num">04</span><h3>Additional Manpower</h3><p>Need to push a phase and hit a hard deadline? We scale crew size on short notice to keep your project on schedule without adding a new sub relationship.</p><div class="svc-tags"><span>Scalable</span><span>Short Notice</span><span>Flexible</span></div></div>
    </div>
  </div></section>

  <section class="section alt"><div class="wrap">
    <div class="reveal"><div class="eyebrow">Project Types</div><h2>The work we do with our GC partners.</h2>
    <p class="intro">From single-family new builds to multi-unit commercial interiors, we have the crew and the experience to deliver.</p></div>
    <div class="svc-grid">
      <div class="svc reveal"><span class="num">01</span><h3>Residential</h3><p>New builds, infills and multi-unit residential — full wall packages from first stud to final coat.</p><div class="svc-tags"><span>New Build</span><span>Infill</span><span>Multi-Unit</span></div></div>
      <div class="svc reveal"><span class="num">02</span><h3>Commercial</h3><p>Office buildings, retail fit-outs and commercial interiors — steel stud framing and drywall installation to spec and on schedule.</p><div class="svc-tags"><span>Office</span><span>Retail</span><span>Industrial</span></div></div>
      <div class="svc reveal"><span class="num">03</span><h3>Tenant Improvement</h3><p>TI work in occupied buildings: staged phasing, clean daily jobsite and minimal disruption to neighbouring tenants.</p><div class="svc-tags"><span>TI</span><span>Occupied</span><span>Phased</span></div></div>
      <div class="svc reveal"><span class="num">04</span><h3>Basement Development</h3><p>Basement developments for volume builders and renovation contractors — fast turnaround, consistent finish standard every time.</p><div class="svc-tags"><span>Volume</span><span>Fast Turnaround</span><span>Consistent</span></div></div>
      <div class="svc reveal"><span class="num">05</span><h3>Renovation</h3><p>Partial demolition, reframing, patching, full re-drywall and finishing for gut-reno and partial renovation scopes.</p><div class="svc-tags"><span>Gut-Reno</span><span>Patch</span><span>Reframe</span></div></div>
    </div>
  </div></section>

  <section class="section tight">
    <figure class="photo-block reveal">
      <picture>
        <source srcset="assets/van.webp" type="image/webp">
        <img src="assets/van.jpg" alt="Summit Wall Solutions crew van ready for an Edmonton project" width="1536" height="1024" loading="lazy">
      </picture>
      <figcaption>Edmonton-based. Professional. Dependable on every project.</figcaption>
    </figure>
  </section>

  <section class="section maroon"><div class="wrap">
    <div class="reveal"><div class="eyebrow" style="color:rgba(255,255,255,.6)">Why GCs Choose Us</div>
    <h2 style="color:#fff">Three things every GC needs from a sub.</h2></div>
    <div class="pr-grid">
      <div class="pr reveal">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        <h3>Quality Workmanship</h3>
        <p>Clean installs, tight board, level finish — done right the first time so your inspection passes and your client is impressed.</p>
      </div>
      <div class="pr reveal">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>
        <h3>Meeting Schedules</h3>
        <p>We commit to your timeline and we keep it. If anything changes, you hear from us first — you are never left waiting to find out where we stand.</p>
      </div>
      <div class="pr reveal">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
        <h3>Clear Communication</h3>
        <p>One point of contact, direct answers. You reach Rodrigo, you get answers — not a dispatcher who does not know the job.</p>
      </div>
      <div class="pr reveal">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
        <h3>Fully Insured</h3>
        <p>WCB coverage and liability insurance on every project. Documentation available on request — no delays getting your job started.</p>
      </div>
    </div>
    <div class="reveal" style="text-align:center;margin-top:36px">
      <div class="badge-row" style="justify-content:center"><span>WCB Coverage</span><span>Liability Insurance</span><span>Edmonton Business Licence</span><span>Since 2017</span></div>
    </div>
  </div></section>

  <section class="section dark" id="sub-quote"><div class="wrap">
    <div class="contact-grid">
      <div class="reveal">
        <div class="eyebrow">Work With Us</div>
        <h2 style="color:#fff">Let's build something together.</h2>
        <p class="intro">Send us a project scope and schedule. We will confirm availability and turn around a number fast — usually same or next business day.</p>
        <div style="margin-top:24px">
          <a href="tel:5873578181" class="ci"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3-8.6A2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/></svg><span><span class="lbl">Call Rodrigo directly</span><span class="val">{PHONE}</span></span></a>
          <a href="mailto:{EMAIL_DIRECT}" class="ci"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/></svg><span><span class="lbl">Email Rodrigo</span><span class="val">{EMAIL_DIRECT}</span></span></a>
        </div>
        <blockquote style="margin:28px 0 0;padding:20px;background:rgba(255,255,255,.05);border-radius:8px;border-left:3px solid #8B2030">
          <p style="color:rgba(255,255,255,.8);font-style:italic;margin:0">"We provide professional, dependable service on every project — quality workmanship, meeting schedules, and clear communication."</p>
          <footer style="color:rgba(255,255,255,.45);font-size:13px;margin:8px 0 0">— Rodrigo Gadelha Bandeira, Founder</footer>
        </blockquote>
      </div>
      <div class="reveal">
        <div class="qform">
          <h3>Request a Sub Quote</h3>
          <div id="form-success" style="display:none;text-align:center;padding:24px;color:#fff"><h3>&#10003; Request Sent!</h3><p style="color:rgba(255,255,255,.7)">Rodrigo will be in touch within one business day.</p></div>
          <form id="quote-form" data-subject="New Subcontractor Inquiry — Summit Wall" data-from-name="Sub Quote Form — Summit Wall Solutions">
            <div class="chip-row" data-group="single" style="margin-bottom:16px">
              <button type="button" class="chip active" data-ptype="res">Residential</button>
              <button type="button" class="chip" data-ptype="com">Commercial</button>
              <button type="button" class="chip" data-ptype="ti">Tenant Improvement</button>
            </div>
            <div class="form-row">
              <div class="field"><label>Company / Name</label><input name="name" type="text" placeholder="Your company or name" required></div>
              <div class="field"><label>Phone</label><input name="phone" type="tel" placeholder="587 000-0000" required></div>
            </div>
            <div class="field"><label>Project type</label><select name="service">
              <option value="">Select type&#8230;</option>
              <option>Residential New Build</option>
              <option>Commercial</option>
              <option>Tenant Improvement (TI)</option>
              <option>Basement Development</option>
              <option>Renovation</option>
              <option>Multiple / Ongoing Work</option>
            </select></div>
            <div class="field"><label>Project details</label><textarea name="message" placeholder="Scope, location, start date, approximate size &#8212; anything that helps us respond faster&#8230;"></textarea></div>
            <button type="submit" class="form-submit">Send Sub Request &rarr;</button>
          </form>
        </div>
      </div>
    </div>
  </div></section>
'''
    page("for-contractors.html",
         "Drywall Subcontractor for GCs &amp; Builders | Summit Wall Solutions",
         "Reliable drywall subcontractor for GCs and builders in Edmonton. Full packages, framing crews, taping & finishing. WCB + liability insured.",
         contractors, body_class="dark-hero",
         schema=_ld(_biz(), _bc([("Home", site+"/"), ("For Contractors", site+"/for-contractors.html")])))

    # ---------- LOCATIONS INDEX ----------
    city_cards = "".join(
        f'<div class="svc reveal"><span class="num">📍</span><h3>{name}</h3><p>Steel framing, drywall installation, taping and painting for {name} homes and businesses.</p><div style="margin-top:18px"><a href="locations/drywall-{slug}.html" class="btn btn-dark">{name} Drywall &rarr;</a></div></div>'
        for slug,name in CITIES)
    locations = f'''
  <section class="hero compact"><div class="hero-bg"><div class="sweep s1"></div><div class="sweep s2"></div></div>
    <div class="wrap"><div class="eyebrow-badge reveal in"><i></i> Service Areas</div>
      <h1 class="reveal in">Serving <em>Greater</em><br>Edmonton</h1>
      <p class="lead reveal in">Your Edmonton drywall contractor, serving the surrounding communities with the same standard of work on every project.</p></div></section>
  <section class="section"><div class="wrap"><div class="svc-grid">{city_cards}</div></div></section>
  {cta_strip(PHONE)}
'''
    page("locations.html", "Drywall Contractor Service Areas — Edmonton &amp; Area | Summit Wall Solutions",
         "Local drywall contractor serving Edmonton, St. Albert, Sherwood Park, Spruce Grove, Leduc and surrounding Alberta communities.", locations,
         body_class="dark-hero",
         schema=_ld(_biz(), _bc([("Home", site+"/"), ("Service Areas", site+"/locations.html")])))

    # ---------- CITY PAGES (SEO) ----------
    city_data = {
        "edmonton": {
            "meta": "Drywall contractor in Edmonton, AB — basement development, infill rebuilds, new builds in Keswick, Rosenthal and Chappelle. Free estimates · WCB insured.",
            "hero_lead": "Serving Edmonton's established neighbourhoods and fast-growing new communities — basement finishing in mature areas, infill rebuilds, and full drywall packages in Keswick, Glenridding Ravine, Rosenthal, Secord, Chappelle and Edgemont. Free estimates · WCB insured · Since 2017.",
            "h2": "Edmonton's drywall contractor — from mature neighbourhood to new build.",
            "intro": "Summit Wall Solutions works across Edmonton's full housing spectrum: finishing basements in mature southwest and west-end neighbourhoods, taking on infill rebuilds throughout the city, and delivering complete drywall packages — framing through final paint — on new builds in fast-growing communities like Keswick, Glenridding Ravine, Rosenthal, Secord, Laurel, Cy Becker, Chappelle and Edgemont. We also handle condo renovations and commercial tenant improvements across Edmonton's growing core.",
            "nbhds": ["Keswick","Glenridding Ravine","Rosenthal","Secord","Laurel","Cy Becker","Chappelle","Edgemont"],
            "faq_h2": "Common questions about drywall work in Edmonton.",
            "faqs": [
                ("Do you do basement development in Edmonton?",
                 "Yes — basement development is one of our most common projects. We handle the full scope: framing, insulation, drywall, taping, painting and cleanup. Most Edmonton basements take <strong>1–2 weeks</strong> depending on size. Call for a free, no-obligation estimate."),
                ("Do you work on infill or mature-neighbourhood renovations?",
                 "Absolutely. We regularly work in Edmonton's established neighbourhoods on infill rebuilds, gut-and-redo renovations and room additions. Our crew knows how to work in occupied homes and can match existing textures and finish levels."),
                ("Can you handle condo or commercial tenant improvements in Edmonton?",
                 "Yes. We take on condo renovations and commercial TI projects throughout Edmonton — partition walls, fire-rated assemblies and finish work. Call or email for a commercial quote."),
            ],
        },
        "st-albert": {
            "meta": "Drywall contractor in St. Albert — new builds in Jensen Lakes, Riverside & Cherot, plus basement development and legal secondary suites. Free estimates.",
            "hero_lead": "Serving St. Albert's growing communities — Riverside, Cherot, Jensen Lakes, Erin Ridge North and North Ridge — with full drywall packages, basement finishing and legal secondary suites. Free estimates · WCB insured · Since 2017.",
            "h2": "St. Albert's drywall contractor for new builds, basements and secondary suites.",
            "intro": "Summit Wall Solutions is a trusted drywall contractor in St. Albert, working with homeowners and builders across the city. We install full drywall packages for new-home builders in St. Albert's newest communities — Riverside, Cherot, Jensen Lakes, Erin Ridge North and North Ridge — and we finish basements and legal secondary suites in established neighbourhoods throughout the city. With St. Albert's continued growth, we understand the demand for reliable trades who show up on time, communicate clearly and deliver code-compliant work.",
            "nbhds": ["Riverside","Cherot","Jensen Lakes","Erin Ridge North","North Ridge"],
            "faq_h2": "Common questions about drywall in St. Albert.",
            "faqs": [
                ("Do you build legal secondary suites in St. Albert?",
                 "Yes. Secondary suites require fire-rated wall assemblies, proper insulation and permit-ready workmanship — all areas we cover. We work with St. Albert's building requirements and can deliver documentation your inspection needs. Call to discuss your project."),
                ("Do you supply drywall for new homes in St. Albert's new communities?",
                 "Yes. We're active in Jensen Lakes, Riverside and Cherot, working with builders or homeowners on full packages from framing through paint. Ask about our production-build scheduling and pricing."),
                ("Is there a travel fee to reach St. Albert?",
                 "No — St. Albert is part of our regular service area with no travel surcharge. Most projects are scheduled within <strong>48 hours of estimate approval</strong>."),
            ],
        },
        "sherwood-park": {
            "meta": "Drywall contractor in Sherwood Park — basements, bonus rooms and renovations in Hillshire West, Summerwood and Aspen Trail. Free estimates · WCB insured.",
            "hero_lead": "Serving Strathcona County's growing communities — Hillshire West, Cambrian, Summerwood and Aspen Trail — for basement development, bonus-room finishing and commercial drywall. Free estimates · WCB insured · Since 2017.",
            "h2": "Sherwood Park's drywall contractor — big homes, quality finishing.",
            "intro": "Summit Wall Solutions brings professional drywall contractor service to Sherwood Park and Strathcona County. We're active in communities like Hillshire West, Cambrian, Summerwood and Aspen Trail, where many of the area's larger family homes have full undeveloped basements ready to finish. We handle basement developments, bonus-room finishing, garage conversions and full renovation drywall — and we take on commercial and office TI work in Strathcona County's business developments.",
            "nbhds": ["Hillshire West","Cambrian","Summerwood","Aspen Trail","Emerald Hills"],
            "faq_h2": "Common questions about drywall in Sherwood Park.",
            "faqs": [
                ("Do you develop basements in Sherwood Park?",
                 "Yes — basement development is very common in Sherwood Park's larger homes. We handle the full scope: framing, insulation, drywall, taping, painting and cleanup. Most basements in the 800–1,200 sq ft range take <strong>1–2 weeks</strong>. Call for a free, no-obligation estimate."),
                ("Can you finish a garage, bonus room or home office in Sherwood Park?",
                 "Absolutely. Garage conversions, bonus-room finishing and home-office build-outs are projects we handle regularly — framing, insulation and drywall work to get the space code-ready and move-in ready."),
                ("Do you do commercial drywall in Strathcona County?",
                 "Yes. We handle commercial projects — partition walls, T-bar ceilings, fire-rated assemblies and tenant improvements — in Strathcona County's business parks and commercial developments. Call for a commercial quote."),
            ],
        },
        "spruce-grove": {
            "meta": "Drywall contractor in Spruce Grove — new-build drywall packages, basement development and renovations. Free estimates · WCB insured · Since 2017.",
            "hero_lead": "Serving Spruce Grove's new-build communities and established homes with full drywall packages for builders, basement development and residential renovations. Free estimates · WCB insured · Since 2017.",
            "h2": "Spruce Grove's drywall contractor for new builds, basements and renovations.",
            "intro": "As Spruce Grove continues to grow as one of Edmonton's most active bedroom communities, Summit Wall Solutions supports both the new-home construction market and the renovation scene. We work with Spruce Grove area builders on complete new-build drywall packages — framing through final paint — and we develop basements in completed homes throughout the city. Whether you're finishing a new home or adding living space below grade, we deliver clean, code-compliant drywall work on schedule.",
            "nbhds": ["Jesperdale","Kingswood","Broxton Park","Grove Meadows","Calahoo"],
            "faq_h2": "Common questions about drywall in Spruce Grove.",
            "faqs": [
                ("Do you do drywall for new homes in Spruce Grove?",
                 "Yes. We work with Spruce Grove area builders on full new-build drywall packages — framing through final paint. We understand production-build timelines and can coordinate with other trades. Call to discuss scheduling and pricing."),
                ("Can you develop a basement in Spruce Grove?",
                 "Absolutely. Basement development in Spruce Grove includes framing, insulation (to Alberta code), drywall, taping and painting — full scope, clean site after every phase. Most basements take <strong>1–2 weeks</strong>. Call for a free estimate."),
                ("Do you also serve Stony Plain?",
                 "Yes — we serve both Spruce Grove and Stony Plain with no travel surcharge. Call 587-357-8181 to schedule your free estimate."),
            ],
        },
        "leduc": {
            "meta": "Drywall contractor in Leduc — new builds and basements in Southfork &amp; Robinson, plus commercial TI work near Nisku. Free estimates · WCB insured.",
            "hero_lead": "Serving Leduc's growing communities — Southfork, Robinson, West Haven and Meadowview — plus commercial and tenant improvement work in Nisku and the Edmonton International Airport corridor. Free estimates · WCB insured · Since 2017.",
            "h2": "Leduc's drywall contractor — residential and commercial.",
            "intro": "Leduc sits at the heart of one of Alberta's most active construction corridors — fast-growing residential communities alongside a major industrial and commercial zone anchored by Edmonton International Airport and Nisku. Summit Wall Solutions serves both sides: full drywall packages (new builds and basement development) in Leduc communities like Southfork, Robinson, West Haven and Meadowview, and commercial and tenant improvement projects in the Nisku industrial area and along the Highway 2 corridor.",
            "nbhds": ["Southfork","Robinson","West Haven","Meadowview","Woodbend"],
            "faq_h2": "Common questions about drywall in Leduc.",
            "faqs": [
                ("Do you do commercial drywall near Nisku and the airport?",
                 "Yes. We handle commercial drywall — partition walls, drop ceilings, fire-rated assemblies and tenant improvements — for industrial offices, warehouse interiors and commercial properties in the Nisku zone and Edmonton International Airport corridor. Call for a commercial quote."),
                ("Do you develop basements in Leduc?",
                 "Yes — we develop basements in Leduc communities including Southfork, Robinson and West Haven. Full scope: framing, insulation, drywall, taping, painting and cleanup. Call for a free, no-obligation estimate."),
                ("Is there a travel surcharge for Leduc?",
                 "No — Leduc is part of our regular service area with no travel surcharge. We're on the road south regularly. Call 587-357-8181 or email to schedule your free estimate."),
            ],
        },
    }
    for slug, name in CITIES:
        d = city_data.get(slug, {})
        meta       = d.get("meta",      f"Drywall contractor in {name}, AB — steel framing, insulation, drywall installation, taping & painting. Free estimates. Call {PHONE}.")
        hero_lead  = d.get("hero_lead", f"Your trusted drywall contractor in {name} for steel framing, insulation, drywall, taping and painting. Free estimates · WCB insured · Since 2017.")
        h2         = d.get("h2",        f"Your drywall contractor in {name}, AB.")
        intro      = d.get("intro",     f"Summit Wall Solutions is {name}'s trusted drywall contractor for basement development, renovations and new builds.")
        faq_h2     = d.get("faq_h2",    f"Common questions about drywall in {name}.")
        faqs       = d.get("faqs",      [])
        nbhds      = d.get("nbhds",     [])

        nbhd_tags  = "".join(f"<span>{n}</span>" for n in nbhds)
        nbhd_block = (f'<div class="eyebrow" style="margin-top:32px">Neighbourhoods we serve</div>'
                      f'<div class="svc-tags" style="margin-top:10px">{nbhd_tags}</div>') if nbhd_tags else ""

        faq_items  = "".join(
            f'<div class="faq-item"><div class="faq-q"><h3>{q}</h3><span class="pm">+</span></div>'
            f'<div class="faq-a"><p>{a}</p></div></div>'
            for q, a in faqs
        )
        faq_block  = (f'<section class="section alt"><div class="wrap">'
                      f'<div class="reveal"><div class="eyebrow">FAQ</div><h2>{faq_h2}</h2></div>'
                      f'<div class="faq reveal">{faq_items}</div></div></section>') if faq_items else ""

        schema_parts = [_biz()]
        if faqs:
            schema_parts.append(_faq(faqs))
        schema_parts.append(_bc([
            ("Home",            site+"/"),
            ("Service Areas",   site+"/locations.html"),
            (f"Drywall {name}", site+f"/locations/drywall-{slug}.html"),
        ]))

        body = f'''
  <section class="hero compact"><div class="hero-bg"><div class="sweep s1"></div><div class="sweep s2"></div></div>
    <div class="wrap"><div class="eyebrow-badge reveal in"><i></i> {name}, AB</div>
      <h1 class="reveal in">Drywall <em>Contractor</em><br>in {name}</h1>
      <p class="lead reveal in">{hero_lead}</p>
      <div class="hero-actions reveal in"><a href="tel:5873578181" class="btn btn-primary">Call {PHONE}</a><a href="../contact.html" class="btn btn-ghost">Free Estimate</a></div></div></section>
  <section class="section"><div class="wrap">
    <div class="reveal"><div class="eyebrow">{name} Wall Services</div><h2>{h2}</h2>
    <p class="intro">{intro}</p>
    {nbhd_block}</div>
    {svc_grid()}</div></section>
  {promises()}
  {faq_block}
  {testimonials()}
  {cta_strip(PHONE)}
'''
        page(f"locations/drywall-{slug}.html",
             f"Drywall Contractor in {name}, AB | Framing, Taping & Painting",
             meta,
             body, rel="../", canonical=f"locations/drywall-{slug}.html", body_class="dark-hero",
             schema=_ld(*schema_parts))

    # ---------- SERVICE SEO PAGES (/services/) ----------
    chk = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"'
           ' width="18" height="18" style="flex-shrink:0;color:var(--maroon);margin-top:2px">'
           '<polyline points="20 6 9 17 4 12"/></svg>')
    for d in SVC_PAGE_DATA:
        inc_items = "".join(
            f'<li style="display:flex;align-items:flex-start;gap:12px;padding:9px 0;'
            f'font-size:15px;color:#4a4340;border-bottom:1px solid rgba(139,99,78,.08)">'
            f'{chk}<span>{item}</span></li>'
            for item in d["includes"]
        )
        includes_html = f'<ul style="list-style:none;padding:0;margin:24px 0 0;max-width:680px">{inc_items}</ul>'

        faq_items = "".join(
            f'<div class="faq-item"><div class="faq-q"><h3>{q}</h3><span class="pm">+</span></div>'
            f'<div class="faq-a"><p>{a}</p></div></div>'
            for q, a in d["faqs"]
        )
        faq_block = (
            f'<section class="section alt"><div class="wrap">'
            f'<div class="reveal"><div class="eyebrow">FAQ</div><h2>{d["faq_h2"]}</h2></div>'
            f'<div class="faq reveal">{faq_items}</div></div></section>'
        )

        svc_body = f'''
  <section class="hero compact"><div class="hero-bg"><div class="sweep s1"></div><div class="sweep s2"></div></div>
    <div class="wrap"><div class="eyebrow-badge reveal in"><i></i> {d["badge"]}</div>
      <h1 class="reveal in">{d["h1"]}</h1>
      <p class="lead reveal in">{d["hero_lead"]}</p>
      <div class="hero-actions reveal in">
        <a href="tel:5873578181" class="btn btn-primary">Call {PHONE}</a>
        <a href="../contact.html" class="btn btn-ghost">Free Estimate</a>
      </div></div></section>
  <section class="section"><div class="wrap">
    <div class="reveal">
      <div class="eyebrow">{d["name"]} · Edmonton, AB</div>
      <h2>What&rsquo;s included.</h2>
      <p class="intro">{d["intro"]}</p>
      {includes_html}
    </div>
  </div></section>
  {promises()}
  {faq_block}
  {cta_strip(PHONE)}
'''
        svc_file = f'services/{d["slug"]}-edmonton.html'
        page(svc_file,
             f'{d["name"]} in Edmonton, AB | Summit Wall Solutions',
             d["meta"],
             svc_body,
             rel="../",
             canonical=svc_file,
             body_class="dark-hero",
             schema=_ld(_biz(), _faq(d["faqs"]), _bc([
                 ("Home",         site+"/"),
                 ("Services",     site+"/services.html"),
                 (f'{d["name"]} in Edmonton', site+f'/{svc_file}'),
             ])))
