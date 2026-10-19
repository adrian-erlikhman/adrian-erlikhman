"""Build assets/sites.svg: every live site as a browser window, all floating in one collage."""
import base64, io, pathlib, sys
from PIL import Image
SRC = pathlib.Path(sys.argv[1])  # portfolio repo img/cases
W, H = 900, 520
# url, file, x, y, width (16:9 page + 18px bar), float delay
WINS = [
 ("safe-routes-la.github.io", "saferoutes-walk.webp", 20, 40, 260, 0.0),
 ("aiml-initiative.org", "aimlli-home.webp", 620, 30, 260, 1.1),
 ("adrianerlikhman.is-a.dev/eDNAtlas", "ednatlas.webp", 40, 330, 250, 2.3),
 ("visionhack-nu.vercel.app", "ledger-dashboard.webp", 610, 320, 260, 0.7),
 ("ace-eta-beryl.vercel.app", "monte-film.webp", 120, 175, 290, 1.8),
 ("safejew.org", "safejew-incident.webp", 490, 170, 290, 2.9),
 ("hivemind-q17i.onrender.com", "hivemind-ad.webp", 285, 110, 340, 0.4),
]
BAR = 18
out = []
for i, (url, fn, x, y, w, dl) in enumerate(WINS):
    h = round(w * 9 / 16)
    im = Image.open(SRC / fn).convert("RGB"); r = max(2*w/im.width, 2*h/im.height)
    im = im.resize((round(im.width*r), round(im.height*r)), Image.LANCZOS)
    l = (im.width - 2*w)//2; im = im.crop((l, 0, l+2*w, 2*h))
    b = io.BytesIO(); im.save(b, "JPEG", quality=70, optimize=True)
    d = base64.b64encode(b.getvalue()).decode()
    out.append(f'''<g class="f" style="animation-delay:-{dl}s"><g transform="translate({x},{y})">
<rect x="3" y="6" width="{w}" height="{h+BAR}" rx="8" fill="#0b1626" opacity=".35"/>
<clipPath id="c{i}"><rect width="{w}" height="{h+BAR}" rx="8"/></clipPath>
<g clip-path="url(#c{i})"><rect width="{w}" height="{h+BAR}" fill="#1f3a5f"/>
<circle cx="10" cy="9" r="3" fill="#ff5f57"/><circle cx="20" cy="9" r="3" fill="#febc2e"/><circle cx="30" cy="9" r="3" fill="#28c840"/>
<rect x="42" y="3" width="{w-50}" height="12" rx="6" fill="#14273f"/>
<text x="50" y="12" font-family="ui-monospace,Menlo,Consolas,monospace" font-size="8" fill="#c9d4e5">{url}</text>
<image y="{BAR}" width="{w}" height="{h}" href="data:image/jpeg;base64,{d}"/></g></g></g>''')
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<style>@keyframes f{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-7px)}}}}.f{{animation:f 4.2s ease-in-out infinite}}</style>
{"".join(out)}</svg>'''
pathlib.Path("assets/sites.svg").write_text(svg)
print(len(svg)//1024, "KB")
