#!/usr/bin/env python3
"""Static site builder for Summit Wall Solutions.
Assembles shared header/footer into each page so the shipped files are
pure static HTML (best for SEO + Vercel). Run:  python3 build.py
"""
import os, pathlib, json

OUT = pathlib.Path(__file__).parent
SITE = "https://summitwallsolutions.com"
PHONE = "587-357-8181"
EMAIL = "contact@summitwallsolutions.com"
EMAIL_DIRECT = "Rodrigo@summitwallsolutions.com"

CITIES = [
    ("edmonton", "Edmonton"),
    ("st-albert", "St. Albert"),
    ("sherwood-park", "Sherwood Park"),
    ("spruce-grove", "Spruce Grove"),
    ("leduc", "Leduc"),
]

NAV = [
    ("index.html", "Home"),
    ("services.html", "Services"),
    ("about.html", "About"),
    ("locations.html", "Service Areas"),
    ("for-contractors.html", "For Contractors"),
    ("contact.html", "Contact"),
]

AREA_SERVED = ["Edmonton","St. Albert","Sherwood Park","Spruce Grove",
               "Leduc","Fort Saskatchewan","Stony Plain"]
SVC_TYPES   = ["Steel Stud Framing","Drywall Installation","Taping and Finishing",
               "Insulation","Painting","Site Cleanup"]

def _biz():
    return {
        "@context": "https://schema.org",
        "@type": ["HomeAndConstructionBusiness", "LocalBusiness"],
        "name": "Summit Wall Solutions",
        "founder": {"@type": "Person", "name": "Rodrigo Gadelha Bandeira"},
        "telephone": "+1-587-357-8181",
        "email": EMAIL,
        "url": SITE,
        "logo": f"{SITE}/assets/logo-lockup.png",
        "image": f"{SITE}/assets/van.webp",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Edmonton",
            "addressRegion": "AB",
            "addressCountry": "CA"
        },
        "areaServed": [{"@type": "City", "name": a} for a in AREA_SERVED],
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
            "opens": "07:00",
            "closes": "17:00"
        },
        "priceRange": "$$",
        "sameAs": ["https://www.instagram.com/summitwallsolutins"],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Wall Solutions Services",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s}}
                for s in SVC_TYPES
            ]
        }
    }

def _bc(crumbs):
    """BreadcrumbList. crumbs = [(name, url), ...]"""
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": u}
            for i, (n, u) in enumerate(crumbs)
        ]
    }

def _faq(pairs):
    """FAQPage. Strips HTML tags from answers before serialising."""
    import re
    strip = lambda t: re.sub(r'<[^>]+>', '', t)
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": strip(a)}}
            for q, a in pairs
        ]
    }

def ld(*dicts):
    """Wrap each schema dict in its own <script type=application/ld+json> block."""
    parts = []
    for d in dicts:
        parts.append(
            '  <script type="application/ld+json">\n' +
            json.dumps(d, ensure_ascii=False, indent=2) +
            '\n  </script>'
        )
    return "\n".join(parts)

def head(title, desc, rel="", canonical="", body_class="", schema=""):
    links = "\n".join(f'    <link rel="stylesheet" href="{rel}css/style.css">' for _ in [0])
    body_tag = f'<body class="{body_class}">' if body_class else '<body>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{SITE}/{canonical}">
  <link rel="icon" type="image/x-icon" href="{rel}assets/favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="{rel}assets/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="{rel}assets/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="{rel}assets/apple-touch-icon.png">
  <link rel="manifest" href="{rel}assets/site.webmanifest">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{SITE}/{canonical}">
  <meta property="og:image" content="https://summitwallsolutions.com/assets/van.webp">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://summitwallsolutions.com/assets/van.webp">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,800;0,900;1,400;1,600&family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">
{links}
{schema}
</head>
{body_tag}"""

def header(rel=""):
    items = "\n".join(
        f'        <li><a href="{rel}{href}"{" class=\"nav-cta\"" if href=="contact.html" else ""}>{label if href!="contact.html" else "Free Quote"}</a></li>'
        for href, label in NAV
    )
    return f"""
  <header class="site-header">
    <div class="wrap nav">
      <a href="{rel}index.html" class="brand">
        <img src="{rel}assets/logo-icon.png" alt="Summit Wall Solutions logo">
        <span class="brand-txt"><b>Summit Wall Solutions</b><span>Building Your Dream, One Wall at a Time</span></span>
      </a>
      <nav>
        <ul class="nav-links">
{items}
        </ul>
      </nav>
      <button class="burger" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </header>"""

def footer(rel=""):
    svc = "".join(f'<a href="{rel}services.html">{s}</a>' for s in ["Steel Stud Framing","Insulation","Drywall Installation","Taping and Finishing","Painting","Site Cleanup"])
    areas = "".join(f'<a href="{rel}locations/drywall-{slug}.html">{name}</a>' for slug,name in CITIES)
    return f"""
  <footer class="site-footer">
    <div class="wrap">
      <div class="foot-grid">
        <div class="foot-brand">
          <img src="{rel}assets/logo-lockup.png" alt="Summit Wall Solutions" class="logo-white">
          <p>Proudly serving Edmonton and surrounding Alberta communities with expert residential & commercial wall solutions — on time, on budget, always up to code.</p>
          <div class="foot-social">
            <a href="tel:5873578181" aria-label="Call"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3-8.6A2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/></svg></a>
            <a href="https://instagram.com/summitwallsolutins" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor" stroke="none"/></svg></a>
            <a href="mailto:{EMAIL}" aria-label="Email"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/></svg></a>
          </div>
        </div>
        <div class="foot-col"><h4>Services</h4>{svc}</div>
        <div class="foot-col"><h4>Service Areas</h4>{areas}</div>
        <div class="foot-col">
          <h4>Contact</h4>
          <a href="tel:5873578181">{PHONE}</a>
          <a href="mailto:{EMAIL}">Email Us</a>
          <a href="{rel}contact.html">Free Estimate</a>
          <p style="font-size:13px;margin-top:10px;color:rgba(255,255,255,.5)">Mon–Fri 7AM–5PM<br>Edmonton, AB · WCB Insured</p>
        </div>
      </div>
      <div class="foot-bottom">
        <span>&copy; <span id="year"></span> Summit Wall Solutions — Rodrigo Gadelha Bandeira. All rights reserved.</span>
        <span>Edmonton, AB · {PHONE} · Licensed &amp; WCB Insured</span>
        <a href="{rel}privacy.html">Privacy Policy</a>
        <span class="foot-credit">Website by <a href="https://www.linkedin.com/in/rubensbandeira" target="_blank" rel="noopener noreferrer">Rubens Bandeira</a></span>
      </div>
    </div>
  </footer>
  <a class="wa-fab" href="https://wa.me/15873578181?text=Hi%20Summit%20Wall%20Solutions%2C%20I%27d%20like%20a%20quote" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp">
    <svg class="wa-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>
    <span class="wa-label">Chat with us</span>
  </a>
  <script src="{rel}js/main.js"></script>
</body>
</html>"""

def page(filename, title, desc, body, rel="", canonical=None, subdir=False, body_class="", schema=""):
    canonical = canonical if canonical is not None else filename
    html = head(title, desc, rel, canonical, body_class, schema) + header(rel) + body + footer(rel)
    target = OUT / filename
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")
    print("wrote", filename)

def build_extra_pages():
    """404 and Privacy pages — defined inline, not in bodies.py."""

    # ── 404 ──────────────────────────────────────────────────────────────
    body_404 = """
  <section class="hero compact"><div class="hero-bg">
    <div class="sweep s1"></div><div class="sweep s2"></div><div class="sweep s3"></div></div>
    <div class="wrap">
      <div class="eyebrow-badge reveal in"><i></i> 404 — Page Not Found</div>
      <h1 class="reveal in">This Page<br>Doesn't <em>Exist</em></h1>
      <p class="lead reveal in">Looks like this page was removed or never existed.<br>Let's get you back on solid ground.</p>
      <div class="hero-actions reveal in">
        <a href="index.html" class="btn btn-primary">Back to Home</a>
        <a href="services.html" class="btn btn-ghost">Our Services</a>
        <a href="contact.html" class="btn btn-ghost">Get a Quote</a>
      </div>
    </div>
  </section>
"""
    page("404.html",
         "Page Not Found | Summit Wall Solutions",
         "The page you're looking for doesn't exist. Head back to Summit Wall Solutions — Edmonton's trusted drywall contractor.",
         body_404,
         body_class="dark-hero",
         schema=ld(_biz()))

    # ── Privacy Policy ────────────────────────────────────────────────────
    body_privacy = f"""
  <section class="hero compact"><div class="hero-bg">
    <div class="sweep s1"></div><div class="sweep s2"></div><div class="sweep s3"></div></div>
    <div class="wrap">
      <div class="eyebrow-badge reveal in"><i></i> Legal</div>
      <h1 class="reveal in">Privacy<br><em>Policy</em></h1>
    </div>
  </section>

  <section class="section">
    <div class="wrap" style="max-width:780px">
      <div class="reveal">
        <p style="font-size:14px;color:var(--grey);margin:0 0 40px">Effective June 2026 &mdash; Summit Wall Solutions, Edmonton, AB, Canada</p>

        <h3 style="font-family:var(--D);font-size:18px;text-transform:uppercase;letter-spacing:.06em;color:var(--maroon);margin:36px 0 10px">1. Who We Are</h3>
        <p style="font-size:16px;line-height:1.75;color:#4a4340;margin-bottom:20px">Summit Wall Solutions is a drywall and wall-finishing contractor based in Edmonton, Alberta, Canada. Our website is <strong>summitwallsolutions.com</strong>. We are owned and operated by Rodrigo Gadelha Bandeira.</p>

        <h3 style="font-family:var(--D);font-size:18px;text-transform:uppercase;letter-spacing:.06em;color:var(--maroon);margin:36px 0 10px">2. What Information We Collect</h3>
        <p style="font-size:16px;line-height:1.75;color:#4a4340;margin-bottom:12px">When you submit a quote request or contact form on our site, we collect the following information that you voluntarily provide:</p>
        <ul style="font-size:16px;line-height:2;color:#4a4340;margin:0 0 20px;padding-left:24px">
          <li>Full name</li>
          <li>Phone number</li>
          <li>Email address (if provided)</li>
          <li>Project details (type, location, scope, timeline, and any notes you include)</li>
        </ul>
        <p style="font-size:16px;line-height:1.75;color:#4a4340;margin-bottom:20px">We do not use tracking cookies, third-party analytics, or advertising pixels. We do not automatically collect IP addresses or device information beyond what your browser transmits as part of a standard web request.</p>

        <h3 style="font-family:var(--D);font-size:18px;text-transform:uppercase;letter-spacing:.06em;color:var(--maroon);margin:36px 0 10px">3. How We Use Your Information</h3>
        <p style="font-size:16px;line-height:1.75;color:#4a4340;margin-bottom:12px">We use the information you submit solely to:</p>
        <ul style="font-size:16px;line-height:2;color:#4a4340;margin:0 0 20px;padding-left:24px">
          <li>Respond to your estimate request or inquiry</li>
          <li>Contact you to schedule a site visit or discuss your project</li>
          <li>Follow up on prior conversations at your request</li>
        </ul>
        <p style="font-size:16px;line-height:1.75;color:#4a4340;margin-bottom:20px">We do not send marketing emails, newsletters, or unsolicited communications.</p>

        <h3 style="font-family:var(--D);font-size:18px;text-transform:uppercase;letter-spacing:.06em;color:var(--maroon);margin:36px 0 10px">4. How We Share Your Information</h3>
        <p style="font-size:16px;line-height:1.75;color:#4a4340;margin-bottom:12px">We do not sell, rent, or share your personal information with third parties, with the following exceptions:</p>
        <ul style="font-size:16px;line-height:2;color:#4a4340;margin:0 0 20px;padding-left:24px">
          <li><strong>Web3Forms:</strong> If our contact form is configured to use Web3Forms (<a href="https://web3forms.com" style="color:var(--maroon)">web3forms.com</a>), your submitted information is routed through their service to deliver it to our inbox. Web3Forms acts as a data processor on our behalf and is bound by their own privacy policy.</li>
          <li><strong>Legal requirements:</strong> If required by law, court order, or to protect our legal rights.</li>
        </ul>

        <h3 style="font-family:var(--D);font-size:18px;text-transform:uppercase;letter-spacing:.06em;color:var(--maroon);margin:36px 0 10px">5. Data Retention</h3>
        <p style="font-size:16px;line-height:1.75;color:#4a4340;margin-bottom:20px">We retain your contact information for as long as is necessary to complete your project or respond to your inquiry. You may ask us to delete your information at any time by contacting us directly.</p>

        <h3 style="font-family:var(--D);font-size:18px;text-transform:uppercase;letter-spacing:.06em;color:var(--maroon);margin:36px 0 10px">6. Your Rights (PIPA)</h3>
        <p style="font-size:16px;line-height:1.75;color:#4a4340;margin-bottom:12px">Under Alberta&rsquo;s <em>Personal Information Protection Act</em> (PIPA) and applicable Canadian privacy law, you have the right to:</p>
        <ul style="font-size:16px;line-height:2;color:#4a4340;margin:0 0 20px;padding-left:24px">
          <li>Know what personal information we hold about you</li>
          <li>Request correction of inaccurate information</li>
          <li>Request deletion of your information</li>
          <li>Withdraw consent to its use at any time</li>
        </ul>

        <h3 style="font-family:var(--D);font-size:18px;text-transform:uppercase;letter-spacing:.06em;color:var(--maroon);margin:36px 0 10px">7. Contact Us</h3>
        <p style="font-size:16px;line-height:1.75;color:#4a4340;margin-bottom:6px">For any privacy questions or to exercise your rights:</p>
        <p style="font-size:16px;line-height:2;color:#4a4340;margin-bottom:40px">
          Email: <a href="mailto:{EMAIL}" style="color:var(--maroon)">{EMAIL}</a><br>
          Phone: <a href="tel:5873578181" style="color:var(--maroon)">{PHONE}</a><br>
          Edmonton, AB, Canada
        </p>
      </div>
    </div>
  </section>
"""
    page("privacy.html",
         "Privacy Policy | Summit Wall Solutions",
         "Summit Wall Solutions privacy policy — what we collect, how we use it, and your rights under Alberta's PIPA.",
         body_privacy,
         schema=ld(_biz(), _bc([("Home", SITE+"/"), ("Privacy Policy", SITE+"/privacy.html")])))


# Import body fragments
from pages import bodies  # noqa

if __name__ == "__main__":
    bodies.build(page, CITIES, PHONE, EMAIL, EMAIL_DIRECT,
                 ld=ld, biz=_biz, bc=_bc, faq_sc=_faq, site=SITE)
    build_extra_pages()
    print("Done.")
