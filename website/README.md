# OnyxAutomate — client website

A static, dependency-free marketing site for OnyxAutomate (automation & AI
integration, United Arab Emirates).

```
website/
├── index.html          the entire page — nav, hero, all content sections
├── assets/site.css     design system + layout (no framework)
└── assets/site.js      menu, hero log reveal, scroll reveal, section gauge
```

## Content sources

Everything on the page is drawn from two internal documents:

- **OnyxAutomate Automation Portfolio** — the five service practices and the
  featured Tax Auditing SaaS Engine build.
- **ASHKAL FZE Work Experience & Automation Report** — the "In Production"
  case study, including the six delivered systems and their time-saved figures.

Vision, mission, operating principles, process, outlook and engagement models
were written for this site and are the sections most worth reviewing before
the site goes public.

## Running it

No build step. Open `index.html`, or serve the folder:

```sh
npx serve website        # or: python3 -m http.server -d website 8000
```

## Deploying

Any static host works (GitHub Pages, Netlify, Vercel, Cloudflare Pages, S3).
For GitHub Pages, either publish from `/docs` (rename this folder) or point a
Pages workflow at `website/`.

The only external dependency is Google Fonts (Archivo, IBM Plex Sans, IBM
Plex Mono). Every face has a real fallback stack, so the page degrades cleanly
if fonts are blocked. To go fully self-hosted, download the three families
into `assets/fonts/` and replace the `<link>` in `index.html` with local
`@font-face` rules.

## Design notes

- Single committed dark theme ("polished obsidian, machined brass"). Every
  colour is painted explicitly, so the page holds regardless of host theme.
- Type is Archivo for headings, IBM Plex Sans for text, IBM Plex Mono for
  data only (the log, metric columns, small labels) — no serif, no width-axis
  stretching.
- All text meets WCAG AA contrast against its actual background.
- Content is not dependent on JavaScript: reveal animations are gated behind
  a `js` class, and a head-script failsafe reveals everything if `site.js`
  never finishes.
- Colour tokens live in `:root` at the top of `site.css` — change the brand
  accent in one place (`--brass`).
- Semantic colours are separate from the accent: `--patina` (passed / live),
  `--oxide` (flagged / held).
- Responsive down to 390px; no horizontal page scroll at any width. Wide
  content (the hero log, the case-study table, the architecture diagram)
  scrolls inside its own container.
- Respects `prefers-reduced-motion`: all reveals resolve immediately.

## Before publishing — please review

- **Contact details** — `sales@onyx-automate.com` and `+971 58 894 1825`
  appear in the hero CTA, contact section and footer.
- **The ASHKAL FZE case study** names the client. Confirm you have their
  permission to reference them publicly, and check the engagement wording.
- **Metrics** are quoted from the ASHKAL report as written (30–45 min daily,
  20 min → seconds per certificate, 1–2 hours at peak dispatch).
