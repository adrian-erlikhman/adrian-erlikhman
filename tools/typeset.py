# -*- coding: utf-8 -*-
"""Text -> SVG, using real font outlines so GitHub renders it identically
everywhere without loading a webfont.

Each distinct glyph is emitted once into <defs> and then placed with <use>,
which is what keeps the banner small: the mono strings reuse the same handful
of letters dozens of times.
"""
import os
import re
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform

_faces = {}
_reg = None

_SAFE = re.compile(r'[^A-Za-z0-9_-]')


class Face:
    def __init__(self, path):
        self.font = TTFont(path)
        self.upem = self.font['head'].unitsPerEm
        self.cmap = self.font.getBestCmap()
        self.gs = self.font.getGlyphSet()
        self.hmtx = self.font['hmtx']
        self.kern = {}
        if 'kern' in self.font:
            for st in self.font['kern'].kernTables:
                self.kern.update(st.kernTable)

    def gname(self, ch):
        n = self.cmap.get(ord(ch))
        if n is None:
            raise KeyError('missing glyph %r (U+%04X)' % (ch, ord(ch)))
        return n

    def outline(self, gname):
        """Glyph path in font units, y already flipped for SVG."""
        pen = SVGPathPen(self.gs, ntos=lambda v: str(int(round(v))))
        self.gs[gname].draw(TransformPen(pen, Transform(1, 0, 0, -1, 0, 0)))
        return pen.getCommands()

    def width(self, text, size, tracking=0.0):
        s = size / self.upem
        total = 0.0
        prev = None
        for ch in text:
            g = self.gname(ch)
            if prev is not None:
                total += self.kern.get((prev, g), 0)
            total += self.hmtx[g][0]
            prev = g
        return total * s + tracking * size * max(len(text) - 1, 0)


def face(path):
    if path not in _faces:
        _faces[path] = Face(path)
    return _faces[path]


class Registry:
    """Collects the unique glyph outlines used by one SVG."""

    def __init__(self):
        self.defs = {}          # id -> path data
        self.order = []

    def gid(self, fontpath, gname):
        # keyed on the font's basename only — an absolute path here would bloat
        # every id and bake the build machine's directory layout into the SVG
        base = os.path.splitext(os.path.basename(fontpath))[0]
        key = 'g%s_%s' % (_SAFE.sub('_', base), _SAFE.sub('_', gname))
        if key not in self.defs:
            d = face(fontpath).outline(gname)
            self.defs[key] = d
            self.order.append(key)
        return key, self.defs[key]

    def render(self):
        return ''.join('<path id="%s" d="%s"/>' % (k, self.defs[k])
                       for k in self.order if self.defs[k])


def new_registry():
    global _reg
    _reg = Registry()
    return _reg


def registry():
    return _reg


def measure(fontpath, text, size, tracking=0.0):
    return face(fontpath).width(text, size, tracking)


def text_path(fontpath, text, size, x, y, tracking=0.0, fill='#000', anchor='start',
              opacity=None, extra=''):
    """Emit a <g> of <use>d glyphs. y is the baseline. Returns (element, width)."""
    f = face(fontpath)
    s = size / f.upem
    w = f.width(text, size, tracking)
    if anchor == 'middle':
        x -= w / 2
    elif anchor == 'end':
        x -= w

    uses = []
    pen_x = 0.0
    prev = None
    track_units = tracking * f.upem
    for ch in text:
        g = f.gname(ch)
        if prev is not None:
            pen_x += f.kern.get((prev, g), 0)
        gid, d = _reg.gid(fontpath, g)
        if d:
            uses.append('<use href="#%s" x="%d"/>' % (gid, round(pen_x))
                        if pen_x else '<use href="#%s"/>' % gid)
        pen_x += f.hmtx[g][0] + track_units
        prev = g

    if not uses:
        return '', w
    op = ' opacity="%s"' % opacity if opacity is not None else ''
    el = ('<g transform="translate(%s %s) scale(%s)" fill="%s"%s%s>%s</g>'
          % (round(x, 2), round(y, 2), round(s, 6), fill, op,
             (' ' + extra) if extra else '', ''.join(uses)))
    return el, w
