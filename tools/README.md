# tools

The two SVGs in `assets/` are generated, not drawn by hand:

```
python tools/build.py
```

It fetches Fraunces and IBM Plex Mono from Google Fonts (both OFL) into
`tools/fonts/`, converts every glyph to an outline, and writes the light and
dark variants of the banner.

Text is vectorized rather than set in `<text>` so the artwork renders
identically everywhere without GitHub loading a webfont. Each distinct glyph is
emitted once into `<defs>` and placed with `<use>`, which is what keeps the
files small.

Motion is additive only: every element declares its final state and the
keyframes supply just a `from`. If a renderer never starts the animation, the
artwork still reads correctly.

Edit the copy at the top of `hero.py` and re-run the build.
