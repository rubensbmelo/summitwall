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


def build(page, CITIES, PHONE, EMAIL, EMAIL_DIRECT,
          ld=None, biz=None, bc=None, faq_sc=None, site=""):
    _ld  = ld     or (lambda *a: "")
    _biz = biz    or (lambda: {})
    _bc  = bc     or (lambda c: {})
    _faq = faq_sc or (lambda f: {})
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
          <form id="quote-form">
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
    for slug,name in CITIES:
        body = f'''
  <section class="hero compact"><div class="hero-bg"><div class="sweep s1"></div><div class="sweep s2"></div></div>
    <div class="wrap"><div class="eyebrow-badge reveal in"><i></i> {name}, AB</div>
      <h1 class="reveal in">Drywall <em>Contractor</em><br>in {name}</h1>
      <p class="lead reveal in">Your trusted drywall contractor in {name} for steel framing, insulation, drywall installation, taping and painting. Free estimates · WCB insured · Since 2017.</p>
      <div class="hero-actions reveal in"><a href="tel:5873578181" class="btn btn-primary">Call {PHONE}</a><a href="../contact.html" class="btn btn-ghost">Free Estimate</a></div></div></section>
  <section class="section"><div class="wrap">
    <div class="reveal"><div class="eyebrow">{name} Wall Services</div><h2>Your drywall contractor in {name}, AB.</h2>
    <p class="intro">Summit Wall Solutions is {name}'s trusted drywall contractor. Whether it's a basement development, a renovation or a new build, our crew delivers clean, code-compliant work — on time and on budget.</p></div>
    {svc_grid()}</div></section>
  {promises()}
  {testimonials()}
  {cta_strip(PHONE)}
'''
        page(f"locations/drywall-{slug}.html",
             f"Drywall Contractor in {name}, AB | Framing, Taping & Painting",
             f"Drywall contractor in {name}, AB — steel framing, insulation, drywall installation, taping & painting. Free estimates. Call {PHONE}.",
             body, rel="../", canonical=f"locations/drywall-{slug}.html", body_class="dark-hero",
             schema=_ld(_biz(), _bc([
                 ("Home",          site+"/"),
                 ("Service Areas", site+"/locations.html"),
                 (f"Drywall {name}", site+f"/locations/drywall-{slug}.html"),
             ])))
