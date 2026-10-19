"""Build assets/sites.svg: a browser window cycling through the live sites."""
import base64, io, pathlib, sys
from PIL import Image
SRC = pathlib.Path(sys.argv[1])  # portfolio repo img/cases
SITES = [("hivemind-q17i.onrender.com","hivemind-ad.webp"),("ace-eta-beryl.vercel.app","monte-film.webp"),
 ("safejew.org","safejew-incident.webp"),("aiml-initiative.org","aimlli-home.webp"),
 ("visionhack-nu.vercel.app","ledger-dashboard.webp"),("safe-routes-la.github.io","saferoutes-walk.webp"),
 ("adrianerlikhman.is-a.dev/eDNAtlas","ednatlas.webp")]
W,H,BAR,STEP=800,450,40,3.5
n=len(SITES); T=n*STEP; f=100/n; fade=0.4/T*100
css=[f"@keyframes s{{0%{{opacity:1}}{f-fade:.2f}%{{opacity:1}}{f:.2f}%{{opacity:0}}{100-fade:.2f}%{{opacity:0}}100%{{opacity:1}}}}",
 ".s{opacity:0;animation:s %.1fs infinite}"%T,
 "@keyframes p{from{width:0}to{width:%dpx}}.p{animation:p %.1fs linear infinite}"%(W,STEP)]
body=[]
for i,(url,fn) in enumerate(SITES):
    im=Image.open(SRC/fn).convert("RGB"); r=max(W/im.width,H/im.height)
    im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS)
    l,t=(im.width-W)//2,0; im=im.crop((l,t,l+W,t+H))
    b=io.BytesIO(); im.save(b,"JPEG",quality=72,optimize=True)
    d=base64.b64encode(b.getvalue()).decode()
    body.append(f'<g class="s" style="animation-delay:{i*STEP-T if i else 0:.1f}s{";opacity:1" if False else ""}">'
      f'<image x="0" y="{BAR}" width="{W}" height="{H}" href="data:image/jpeg;base64,{d}"/>'
      f'<text x="150" y="25" font-family="ui-monospace,Menlo,Consolas,monospace" font-size="13" fill="#c9d4e5">{url}</text></g>')
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H+BAR}" width="{W}" height="{H+BAR}">
<style>{"".join(css)}</style>
<defs><clipPath id="c"><rect width="{W}" height="{H+BAR}" rx="12"/></clipPath></defs>
<g clip-path="url(#c)"><rect width="{W}" height="{H+BAR}" fill="#1f3a5f"/>
<circle cx="20" cy="20" r="6" fill="#ff5f57"/><circle cx="40" cy="20" r="6" fill="#febc2e"/><circle cx="60" cy="20" r="6" fill="#28c840"/>
<rect x="138" y="9" width="{W-160}" height="22" rx="11" fill="#14273f"/>
{"".join(body)}
<rect class="p" x="0" y="{BAR-2}" height="2" width="0" fill="#9db8e0"/></g></svg>'''
pathlib.Path("assets/sites.svg").write_text(svg)
print(len(svg)//1024,"KB")
