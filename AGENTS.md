# Summit Wall Solutions — Website Project Brief

Read this first. Multi-page static site, brand-aligned, deployed on Vercel.

## Business
- Company: Summit Wall Solutions · Owner: Rodrigo Gadelha (Founder & Owner)
- Edmonton, AB — Canada · Founded 2017
- Phone: 587-357-8181 · Email: Summitwallsolutions@gmail.com
- Instagram: @summitwallsolutins  (real handle — "solutins", no second "o")
- Slogan: "Building Your Dream, One Wall at a Time"
  (Logo art shows "One Wall a Time" — confirm which is official.)
- Service area: Edmonton, St. Albert, Sherwood Park, Spruce Grove, Leduc, Fort Saskatchewan, Stony Plain
- Services: Steel Frame · Insulation · Drywall · Taping & Mudding · Painting · Texture (residential + commercial)

## Brand
- Maroon #6E1A22 (primary) · deep #54121A · bright #8B2030
- Cold White #FFFFFF (secondary) · Charcoal #2D2D2D (detail only) · grey #8D857C
- Fonts: Playfair Display (display) + Lora (body) — loaded from Google Fonts
- Rule: maroon backgrounds, white elements; logo always dominant
- Logo: /assets/logo-icon.png (mark) + /assets/logo-lockup.png (mark+name). Maroon on transparent.
  White version via CSS: filter: brightness(0) invert(1);  (class .logo-white)
- For print/large format get the original VECTOR (SVG/AI/EPS) from the designer.

## Architecture — IMPORTANT
This is a BUILT static site. **Do not hand-edit the generated .html files** — they are
regenerated from templates. Edit the sources, then run the build:

    python3 build.py

- `build.py`      — assembles head + shared header + body + shared footer into each page
- `pages/bodies.py` — the body content for every page (home, services, about, contact,
                      locations index, and one city page per city) + reusable blocks
                      (svc_grid, promises, calculator, testimonials, faq, cta_strip)
- `css/style.css` — all styles (global, header, footer, hero, sections, calculator, faq, form, responsive)
- `js/main.js`    — header scroll, mobile menu, active link, FAQ, reveal, calculator, contact form
- `assets/`       — logo files
- `robots.txt`, `sitemap.xml` — SEO

Header & footer live ONCE in build.py and are baked into every page (static = best SEO + speed).
To change the nav or footer, edit build.py and re-run.

## Pages
- index.html — home (hero, ticker, services preview, promises, testimonials, CTA)
- services.html — 6 services + estimate calculator + process
- about.html — Rodrigo / story / stats / promises / FAQ
- contact.html — contact form (+ info, hours, FAQ)
- locations.html — service-areas index
- locations/drywall-<city>.html — per-city SEO landing pages (Edmonton, St Albert, Sherwood Park, Spruce Grove, Leduc)

Add a new city: append to CITIES in build.py, re-run. Add it to sitemap.xml too.

## TODOs before launch
1. Replace PLACEHOLDER testimonials (in pages/bodies.py -> testimonials()) with real Google reviews.
2. Contact form: get a free Web3Forms key (https://web3forms.com) and paste it into
   FORM_ACCESS_KEY in js/main.js to enable silent submit (falls back to mailto otherwise).
3. Confirm slogan wording ("One Wall a Time" vs "One Wall at a Time").
4. Add real project photos / a gallery.
5. Update the domain in build.py (SITE), sitemap.xml and robots.txt once live.
6. Generate a proper favicon set from the logo.
7. Consider per-service + per-city combo pages (e.g. framing-sherwood-park) for deeper local SEO.

## Run / Deploy
Local preview:  npx serve .   (or open index.html)
Build pages:    python3 build.py
Deploy:         npm i -g vercel && vercel --prod   (or connect the repo in Vercel; preset "Other")
