# Summit Wall Solutions — Website

Static website for Summit Wall Solutions (Edmonton, AB). Plain HTML/CSS/JS, deployed on Vercel.

## Run locally
Just open `index.html` in a browser, or serve it:
```bash
npx serve .
```

## Deploy to Vercel
```bash
npm i -g vercel
vercel          # preview
vercel --prod   # production
```
Or connect this folder's Git repo in the Vercel dashboard (Framework Preset: "Other").

## Structure
- `index.html` — the whole site (self-contained)
- `assets/` — logo files (icon + lockup)
- `CLAUDE.md` — full project brief, brand guidelines & TODOs (read this first)

## Working with Claude Code
Open this folder in VS Code and start Claude Code. It will read `CLAUDE.md` automatically.
Good first prompts:
- "Read CLAUDE.md, then migrate the fonts to Playfair Display + Lora."
- "Swap the inline SVG logo for /assets/logo-lockup.png in the header and footer."
- "Wire the contact form to Web3Forms."
