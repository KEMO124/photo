import re, base64, subprocess, os
css = open('gf.css').read()
# split into (comment-label, @font-face block) pairs
blocks = re.split(r'/\*\s*([\w-]+)\s*\*/', css)
out = []
kept = 0
for i in range(1, len(blocks), 2):
    label = blocks[i].strip()
    body = blocks[i+1]
    if label not in ('latin', 'latin-ext'):
        continue
    m = re.search(r'@font-face\s*\{(.*?)\}', body, re.S)
    if not m:
        continue
    face = m.group(1)
    url = re.search(r"url\((https://fonts\.gstatic\.com[^)]+)\)", face).group(1)
    fn = url.rsplit('/', 1)[-1]
    if not os.path.exists(fn):
        subprocess.run(['curl','-sS','-o',fn,url], check=True)
    b64 = base64.b64encode(open(fn,'rb').read()).decode()
    face = re.sub(r"url\(https://fonts\.gstatic\.com[^)]+\)",
                  "url(data:font/woff2;base64,%s)" % b64, face)
    face = re.sub(r"unicode-range:[^;]+;", "", face)
    out.append("@font-face{%s}" % face.strip())
    kept += 1
open('fonts.css','w').write("\n".join(out))
print("faces embedded:", kept, "bytes:", os.path.getsize('fonts.css'))
