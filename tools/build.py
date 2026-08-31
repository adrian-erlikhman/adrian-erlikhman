# -*- coding: utf-8 -*-
"""Regenerate the README artwork.

    python tools/build.py

Downloads the two fonts on first run (Fraunces and IBM Plex Mono, both OFL,
from Google Fonts) into tools/fonts/, then writes the two banner variants
into assets/. Nothing is hand-edited: change the copy at the top of hero.py and
re-run this.
"""
import os
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FONTDIR = os.path.join(HERE, 'fonts')
OUT = os.path.join(ROOT, 'assets')

# Static instances served by Google Fonts. Pinned so the outlines, and so the
# measured layout, never shift underneath the committed SVGs.
FONTS = {
    'Fraunces900.ttf':
        'https://fonts.gstatic.com/s/fraunces/v38/6NUh8FyLNQOQZAnv9bYEvDiIdE9Ea92ue'
        'mAk_WBq8U_9v0c2Wa0K7iN7hzFUPJH58nib1603gg7S2nfgRYIcHhyjDg.ttf',
    'PlexMono400.ttf':
        'https://fonts.gstatic.com/s/ibmplexmono/v20/-F63fjptAgt5VM-kVkqdyU8n5ig.ttf',
    'PlexMono500.ttf':
        'https://fonts.gstatic.com/s/ibmplexmono/v20/-F6qfjptAgt5VM-kVkqdyU8n3twJ8lc.ttf',
}


def fetch_fonts():
    os.makedirs(FONTDIR, exist_ok=True)
    for name, url in FONTS.items():
        dest = os.path.join(FONTDIR, name)
        if os.path.exists(dest):
            continue
        print('fetching', name)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as r, open(dest, 'wb') as f:
            f.write(r.read())


def main():
    fetch_fonts()
    sys.path.insert(0, HERE)
    os.makedirs(OUT, exist_ok=True)
    import hero
    for mod in (hero,):
        for palette in (mod.LIGHT, mod.DARK):
            svg = mod.build(palette)
            path = os.path.join(OUT, '%s-%s.svg' % (mod.NAME, palette['key']))
            with open(path, 'w', encoding='utf-8') as f:
                f.write(svg)
            print('%-28s %6d bytes' % (os.path.relpath(path, ROOT), len(svg)))


if __name__ == '__main__':
    main()
