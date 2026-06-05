#!/usr/bin/env python3
"""Static site builder for Summit Wall Solutions.
Assembles shared header/footer into each page so the shipped files are
pure static HTML (best for SEO + Vercel). Run:  python3 build.py
"""
import os, pathlib

OUT = pathlib.Path(__file__).parent
SITE = "https://summitwallsolutions.com"
PHONE = "587-357-8181"
EMAIL = "Rodrigo@summitwallsolutions.com"

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
    ("contact.html", "Contact"),
]

def head(title, desc, rel="", canonical="", body_class=""):
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
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,800;0,900;1,400;1,600&family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">
{links}
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
        <span>Edmonton, AB · {PHONE} · Licensed & WCB Insured</span>
      </div>
    </div>
  </footer>
  <script src="{rel}js/main.js"></script>
</body>
</html>"""

def page(filename, title, desc, body, rel="", canonical=None, subdir=False, body_class=""):
    canonical = canonical if canonical is not None else filename
    html = head(title, desc, rel, canonical, body_class) + header(rel) + body + footer(rel)
    target = OUT / filename
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")
    print("wrote", filename)

# Import body fragments
from pages import bodies  # noqa

if __name__ == "__main__":
    bodies.build(page, CITIES, PHONE, EMAIL)
    print("Done.")
