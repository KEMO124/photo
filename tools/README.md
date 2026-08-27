# Portfolio PDF build

`Onyx-Automate-Portfolio.pdf` (15pp, US Letter) is generated from the same
content as `portfolio.html`, laid out for print with explicit pagination.

## Regenerating

1. Fetch and inline the webfonts (needs network access to Google Fonts):

       curl -sS -A "Mozilla/5.0" \
         "https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@85..125,400..800&family=Source+Serif+4:opsz,wght@8..60,400..600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" \
         -o gf.css
       python3 embed_fonts.py          # writes fonts.css (base64 woff2, latin subsets)

2. Build the paginated HTML and render it:

       python3 build_portfolio_pdf.py                       # writes print.html
       chrome --headless --no-pdf-header-footer \
              --print-to-pdf=Onyx-Automate-Portfolio.pdf print.html

## Checking the layout

`build_portfolio_pdf.py` injects a measurement script by default. Dumping the
DOM prints one `used/available` pair per sheet:

    chrome --headless --dump-dom print.html | grep -o 'OVERFLOW [0-9][^<]*'

Any `used` greater than `available` means that page overflows its box and the
content needs rebalancing (each service has a `split` key controlling how many
"what we built" items sit on its first page). Set `MEASURE=0` before the final
render so the probe element does not add a blank page.

`SHEETS=3` builds a single sheet, which is useful for screenshotting one page.
