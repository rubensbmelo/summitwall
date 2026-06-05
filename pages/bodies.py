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


def build(page, CITIES, PHONE, EMAIL):
    # ---------- HOME ----------
    home = f'''
  <div class="ticker-wrap"><div class="ticker-track" id="tick">
    {"".join(f"<span>{x}</span>" for x in ["★ Google Reviewed","✓ Free Estimates","✓ 1-Year Warranty","✓ WCB Insured","✓ Clean Jobsite Daily","✓ Edmonton & Area","✓ Since 2017","✓ Booked in 48 Hours","✓ No Surprise Charges","✓ Residential & Commercial"]*2)}
  </div></div>
  <section class="hero"><div class="hero-bg"><div class="sweep s1"></div><div class="sweep s2"></div><div class="sweep s3"></div></div>
    <div class="wrap">
      <div class="eyebrow-badge reveal in"><i></i> Building Your Dream, One Wall at a Time — Since 2017</div>
      <h1 class="reveal in">Walls Built<br>To Last. <em>Finished</em><br>To Impress.</h1>
      <p class="lead reveal in">Edmonton's trusted crew for steel framing, insulation, drywall, taping and painting. Residential and commercial — one team, start to finish.</p>
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
    page("index.html", "Summit Wall Solutions | Drywall, Steel Stud Framing & Finishing — Edmonton, AB",
         "Edmonton's trusted drywall, steel framing, insulation, taping and painting experts. Free estimates. WCB insured. Since 2017.", home)

    # ---------- SERVICES ----------
    services = f'''
  <section class="hero compact"><div class="hero-bg"><div class="sweep s1"></div><div class="sweep s2"></div></div>
    <div class="wrap"><div class="eyebrow-badge reveal in"><i></i> Services</div>
      <h1 class="reveal in">Full-Wall <em>Solutions</em></h1>
      <p class="lead reveal in">From the first steel stud to the final coat of paint, we handle every layer — so you deal with one accountable team.</p></div></section>
  <section class="section"><div class="wrap">{svc_grid()}</div></section>
  {calculator()}
  <section class="section alt"><div class="wrap"><div class="reveal"><div class="eyebrow">How It Works</div><h2>Simple from first call to final coat.</h2></div>
    <div class="steps">
      <div class="step reveal"><b>01</b><h3>Consult</h3><p>We visit your site, assess the scope and answer every question. No pressure.</p></div>
      <div class="step reveal"><b>02</b><h3>Quote</h3><p>A clear written estimate — itemized, honest, no hidden charges.</p></div>
      <div class="step reveal"><b>03</b><h3>Build</h3><p>Our crew arrives on schedule, works clean and communicates throughout.</p></div>
      <div class="step reveal"><b>04</b><h3>Sign Off</h3><p>We walk the finished job with you. Not done until you're satisfied.</p></div>
    </div></div></section>
  {cta_strip(PHONE)}
'''
    page("services.html", "Services — Steel Stud Framing, Drywall, Painting & More | Summit Wall Solutions",
         "Steel stud framing, insulation, drywall installation, taping and painting for Edmonton homes and businesses. Free estimate calculator inside.", services,
         body_class="dark-hero")

    # ---------- ABOUT ----------
    about = f'''
  <section class="hero compact"><div class="hero-bg"><div class="sweep s1"></div><div class="sweep s2"></div></div>
    <div class="wrap"><div class="eyebrow-badge reveal in"><i></i> About Us</div>
      <h1 class="reveal in">A Local Crew<br>You Can <em>Trust</em></h1></div></section>
  <section class="section"><div class="wrap about-grid">
    <div class="about-copy reveal">
      <div class="eyebrow">Who We Are</div>
      <p class="lead-line">We treat every wall like it's going in our own home.</p>
      <p>Founded by <strong>Rodrigo Gadelha Bandeira</strong> in Edmonton, AB, Summit Wall Solutions has built its reputation one clean corner at a time since 2017. We handle the full wall — framing, insulation, drywall, taping and paint — so you deal with one accountable team from start to finish.</p>
      <p>We start every job with a clear scope, stick to the schedule we commit to, and leave your site clean at the end of every day. Most of our business comes from repeat clients and referrals — that's the standard we hold ourselves to.</p>
    </div>
    <div class="stats reveal">
      <div class="stat"><b>2017</b><span>Established</span></div>
      <div class="stat"><b>100%</b><span>Satisfaction</span></div>
      <div class="stat"><b>Full</b><span>Wall Service</span></div>
      <div class="stat"><b>Free</b><span>Estimates</span></div>
    </div></div></section>
  {promises()}
  {faq()}
  {cta_strip(PHONE)}
'''
    page("about.html", "About Summit Wall Solutions | Edmonton Drywall Since 2017",
         "Founded by Rodrigo Gadelha Bandeira in 2017, Summit Wall Solutions is Edmonton's trusted full-wall contractor. WCB insured, 1-year warranty.", about,
         body_class="dark-hero")

    # ---------- CONTACT ----------
    contact = f'''
  <section class="hero compact"><div class="hero-bg"><div class="sweep s1"></div><div class="sweep s2"></div></div>
    <div class="wrap"><div class="eyebrow-badge reveal in"><i></i> Contact</div>
      <h1 class="reveal in">Get Your <em>Free</em><br>Estimate</h1></div></section>
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
          <form id="quote-form">
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
    page("contact.html", "Contact & Free Estimate | Summit Wall Solutions Edmonton",
         "Request a free, no-obligation drywall estimate in Edmonton. Call 587-357-8181 or fill out the form. WCB insured, 1-year warranty.", contact,
         body_class="dark-hero")

    # ---------- LOCATIONS INDEX ----------
    city_cards = "".join(
        f'<div class="svc reveal"><span class="num">📍</span><h3>{name}</h3><p>Steel framing, drywall installation, taping and painting for {name} homes and businesses.</p><div style="margin-top:18px"><a href="locations/drywall-{slug}.html" class="btn btn-dark">{name} Drywall &rarr;</a></div></div>'
        for slug,name in CITIES)
    locations = f'''
  <section class="hero compact"><div class="hero-bg"><div class="sweep s1"></div><div class="sweep s2"></div></div>
    <div class="wrap"><div class="eyebrow-badge reveal in"><i></i> Service Areas</div>
      <h1 class="reveal in">Serving <em>Greater</em><br>Edmonton</h1>
      <p class="lead reveal in">Based in Edmonton, we serve the surrounding communities with the same standard of work on every job.</p></div></section>
  <section class="section"><div class="wrap"><div class="svc-grid">{city_cards}</div></div></section>
  {cta_strip(PHONE)}
'''
    page("locations.html", "Service Areas — Edmonton & Area | Summit Wall Solutions",
         "Summit Wall Solutions serves Edmonton, St. Albert, Sherwood Park, Spruce Grove and Leduc with drywall, framing and finishing.", locations,
         body_class="dark-hero")

    # ---------- CITY PAGES (SEO) ----------
    for slug,name in CITIES:
        body = f'''
  <section class="hero compact"><div class="hero-bg"><div class="sweep s1"></div><div class="sweep s2"></div></div>
    <div class="wrap"><div class="eyebrow-badge reveal in"><i></i> {name}, AB</div>
      <h1 class="reveal in">Drywall &amp;<br>Framing in <em>{name}</em></h1>
      <p class="lead reveal in">Steel framing, insulation, drywall installation, taping and painting for {name} homes and businesses. Free estimates · WCB insured · Since 2017.</p>
      <div class="hero-actions reveal in"><a href="tel:5873578181" class="btn btn-primary">Call {PHONE}</a><a href="../contact.html" class="btn btn-ghost">Free Estimate</a></div></div></section>
  <section class="section"><div class="wrap">
    <div class="reveal"><div class="eyebrow">{name} Wall Services</div><h2>Your full-wall contractor in {name}.</h2>
    <p class="intro">Summit Wall Solutions is proud to serve {name} and the surrounding area. Whether it's a basement development, a renovation or a new build, our crew delivers clean, code-compliant work — on time and on budget.</p></div>
    {svc_grid()}</div></section>
  {promises()}
  {testimonials()}
  {cta_strip(PHONE)}
'''
        page(f"locations/drywall-{slug}.html",
             f"Drywall & Framing in {name}, AB | Summit Wall Solutions",
             f"Drywall installation, steel framing, insulation, taping and painting in {name}, AB. Free estimates, WCB insured. Call {PHONE}.",
             body, rel="../", canonical=f"locations/drywall-{slug}.html", body_class="dark-hero")
