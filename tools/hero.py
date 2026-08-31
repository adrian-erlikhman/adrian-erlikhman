# -*- coding: utf-8 -*-
"""Identity banner for the GitHub profile README, in the design language of
adrianerlikhman.is-a.dev. All text is vectorized from the real fonts."""
import os
import io
from typeset import text_path, measure, new_registry, registry

_F = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts')

FR = os.path.join(_F, 'Fraunces900.ttf')
M4 = os.path.join(_F, 'PlexMono400.ttf')
M5 = os.path.join(_F, 'PlexMono500.ttf')

NAME = 'hero'

W, H = 1200, 376

LIGHT = dict(
    key='light',
    bg='#e8e4d6', ink='#211f18', dim='#6b6857', acc='#c1543a',
    line='#211f18', line_op=.13, line_strong_op=.26, vig='#c1543a', vig_op=.07,
    dot_op=.16,
)
DARK = dict(
    key='dark',
    bg='#17150f', ink='#ece6d6', dim='#a8a28d', acc='#e0724f',
    line='#ece6d6', line_op=.14, line_strong_op=.28, vig='#e0724f', vig_op=.07,
    dot_op=.15,
)

TAGS = ['LOS ANGELES', 'SENIOR AT LACES', 'CLASS OF ’27']
NAME1 = 'hi, i’m'
NAME2 = 'adrian'
ROLE = 'first-author nlp research. quant models. civic tools'
ROLE2 = 'built on public data.'
FIELDS = [('01', 'ai/ml'), ('02', 'applied math'), ('03', 'computer science'),
          ('04', 'quant finance'), ('05', 'data science'), ('06', 'startups')]
STATS = [
    ('neurips', 'first-author paper', 'under review · judge 2026'),
    ('1st', 'decode the ocean', 'lovable × united nations'),
    ('3rd', 'code for transportation', 'young coders’ sphere'),
]


def build(P):
    new_registry()
    o = []
    a = o.append
    acc, ink, dim = P['acc'], P['ink'], P['dim']
    line, lop, lsop = P['line'], P['line_op'], P['line_strong_op']

    a('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
      'role="img" aria-label="Adrian Erlikhman — Los Angeles. First-author NLP '
      'research, quant models, civic tools built on public data. Paper under '
      'review at JUDGe 2026; 1st at Decode the Ocean; 3rd at Code for '
      'Transportation.">' % (W, H, W, H))

    a('<defs>')
    a('<!--G-->')
    a('<pattern id="dots" width="26" height="26" patternUnits="userSpaceOnUse">'
      '<circle cx="1" cy="1" r="1" fill="%s" opacity="%s"/></pattern>' % (line, P['dot_op']))
    a('<linearGradient id="dotfade" x1="0" y1="0" x2="0" y2="1">'
      '<stop offset="0" stop-color="#fff" stop-opacity="1"/>'
      '<stop offset=".62" stop-color="#fff" stop-opacity=".35"/>'
      '<stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>')
    a('<mask id="dotmask"><rect width="%d" height="%d" fill="url(#dotfade)"/></mask>' % (W, H))
    a('<radialGradient id="vig" cx=".5" cy="0" r=".78">'
      '<stop offset="0" stop-color="%s" stop-opacity="%s"/>'
      '<stop offset="1" stop-color="%s" stop-opacity="0"/></radialGradient>'
      % (P['vig'], P['vig_op'], P['vig']))
    a('<clipPath id="c1"><rect x="56" y="86" width="700" height="82"/></clipPath>')
    a('<clipPath id="c2"><rect x="56" y="168" width="700" height="86"/></clipPath>')
    a('</defs>')

    # Motion is additive only: every element declares its FINAL state, and the
    # keyframes supply just a "from". If a renderer never starts the animation
    # (or freezes it at t=0) the banner still reads correctly.
    a('<style>'
      '@keyframes rise{from{transform:translateY(104%)}}'
      '@keyframes blink{50%{opacity:.45}}'
      '@keyframes draw{from{stroke-dashoffset:var(--l)}}'
      '@keyframes sweep{0%{transform:translateX(0);opacity:0}'
      '10%{opacity:.55}90%{opacity:.55}'
      '100%{transform:translateX(982px);opacity:0}}'
      '.n1{animation:rise 1s cubic-bezier(.16,1,.3,1)}'
      '.n2{animation:rise 1.18s cubic-bezier(.16,1,.3,1)}'
      '.sq{animation:blink 2.8s ease-in-out infinite}'
      '.rule{stroke-dasharray:var(--l);stroke-dashoffset:0;'
      'animation:draw 1.5s cubic-bezier(.16,1,.3,1)}'
      '.swp{opacity:0;animation:sweep 7s ease-in-out 1.2s infinite}'
      '@media(prefers-reduced-motion:reduce){'
      '.n1,.n2,.rule{animation:none}.swp{display:none}}'
      '</style>')

    a('<rect width="%d" height="%d" fill="%s"/>' % (W, H, P['bg']))
    a('<rect width="%d" height="%d" fill="url(#dots)" mask="url(#dotmask)"/>' % (W, H))
    a('<rect width="%d" height="%d" fill="url(#vig)"/>' % (W, H))
    a('<rect x=".5" y=".5" width="%s" height="%s" fill="none" stroke="%s" stroke-opacity="%s"/>'
      % (W - 1, H - 1, line, lsop))
    for (cx, cy, dx, dy) in [(14, 14, 1, 1), (W - 14, 14, -1, 1), (14, H - 14, 1, -1), (W - 14, H - 14, -1, -1)]:
        a('<path d="M%s %s h%s M%s %s v%s" stroke="%s" stroke-width="2" fill="none"/>'
          % (cx, cy, 16 * dx, cx, cy, 16 * dy, acc))

    # tag row
    x = 64
    ty = 60
    a('<rect class="sq" x="%s" y="%s" width="8" height="8" fill="%s"/>' % (x, ty - 8, acc))
    x += 20
    for i, t in enumerate(TAGS):
        if i:
            el, w = text_path(M4, '/', 12, x, ty, tracking=.2, fill=dim, opacity='.5')
            a(el)
            x += w + 14
        el, w = text_path(M5, t, 12, x, ty, tracking=.2, fill=dim)
        a(el)
        x += w + 14

    # name
    el, _ = text_path(FR, NAME1, 74, 62, 152, tracking=-.02, fill=ink)
    a('<g clip-path="url(#c1)"><g class="n1">%s</g></g>' % el)
    el, _ = text_path(FR, NAME2, 74, 62, 234, tracking=-.02, fill=acc)
    a('<g clip-path="url(#c2)"><g class="n2">%s</g></g>' % el)

    # role
    el, _ = text_path(M4, ROLE, 14.5, 64, 272, tracking=.01, fill=dim)
    a('<g class="f f2">%s</g>' % el)
    el, _ = text_path(M4, ROLE2, 14.5, 64, 293, tracking=.01, fill=dim)
    a('<g class="f f2">%s</g>' % el)

    # bottom rule + field bus
    ry = 324
    a('<line class="rule" style="--l:%s" x1="64" y1="%s" x2="%s" y2="%s" stroke="%s" '
      'stroke-opacity="%s"/>' % (W - 128, ry, W - 64, ry, line, lop))
    a('<g class="swp"><rect x="64" y="%s" width="90" height="1" fill="%s" opacity=".55"/></g>'
      % (ry - .5, acc))
    x = 64
    for (num, lab) in FIELDS:
        el, w = text_path(M5, num, 11, x, ry + 23, tracking=.06, fill=acc)
        a('<g class="f f3">%s</g>' % el)
        x += w + 7
        el, w = text_path(M4, lab, 13, x, ry + 23, tracking=.01, fill=ink, opacity='.86')
        a('<g class="f f3">%s</g>' % el)
        x += w + 22

    # right stat stack
    # the stat block is measured and right-aligned to the margin, so the value
    # column and the label column each share one edge no matter the copy
    LABX = max(measure(FR, v, 42, -.02) for v, _, _ in STATS) + 18
    labw = max(max(measure(M5, l, 14, .02), measure(M4, sb, 11.5, .06))
               for _, l, sb in STATS)
    sx = (W - 64) - labw - LABX
    a('<line class="rule" style="--l:252" x1="%s" y1="52" x2="%s" y2="304" stroke="%s" '
      'stroke-opacity="%s"/>' % (sx - 34, sx - 34, line, lsop))
    sy = 104
    for i, (val, lab, sub) in enumerate(STATS):
        cls = 'f f%d' % (2 + i)
        el, w = text_path(FR, val, 42, sx, sy, tracking=-.02, fill=acc)
        a('<g class="%s">%s</g>' % (cls, el))
        el, _ = text_path(M5, lab, 14, sx + LABX, sy - 10, tracking=.02, fill=ink)
        a('<g class="%s">%s</g>' % (cls, el))
        el, _ = text_path(M4, sub, 11.5, sx + LABX, sy + 8, tracking=.06, fill=dim)
        a('<g class="%s">%s</g>' % (cls, el))
        sy += 78

    a('</svg>')
    return '\n'.join(o).replace('<!--G-->', registry().render())
