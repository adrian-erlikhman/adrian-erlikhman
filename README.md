<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/adrian-erlikhman/adrian-erlikhman/main/assets/hero-dark.svg">
  <img alt="Adrian Erlikhman — Los Angeles, senior at LACES, class of 2027. First-author NLP research, quant models, civic tools built on public data. Paper under review at JUDGe 2026; 1st at Decode the Ocean; 3rd at Code for Transportation." src="https://raw.githubusercontent.com/adrian-erlikhman/adrian-erlikhman/main/assets/hero-light.svg">
</picture>

Senior at LACES in Los Angeles, working on applied NLP and quantitative
modeling. Most of the effort goes into evaluation: metrics that don't flatter
the model, and baselines it actually has to beat.

**[adrianerlikhman.is-a.dev](https://adrianerlikhman.is-a.dev)** ·
[LinkedIn](https://www.linkedin.com/in/adrian-erlikhman-55489620b) ·
[Résumé](https://adrianerlikhman.is-a.dev/resume.pdf) ·
[erlikhman.adrian@gmail.com](mailto:erlikhman.adrian@gmail.com)

---

### `[01]` What I'm working on

**A first-author paper on model self-recognition.** Language models are poor at
identifying their own output, and the errors are systematic rather than random:
misattributions concentrate on GPT-4o and Claude. Under review at JUDGe 2026, a
NeurIPS workshop.
[Write-up and a live stylometry demo](https://adrianerlikhman.is-a.dev/#papers).

**An AI/ML course now piloting in LAUSD.** I co-wrote the curriculum.

**Internships.** A venture fund, an edtech ML team, and a space lab at Caltech
studying data centers in orbit.

---

### `[02]` Things I've built

The first two placed in competition. The rest I built on my own time.

| | |
|---|---|
| **[eDNAtlas](https://github.com/adrian-erlikhman/eDNAtlas)**<br>`1st · Decode the Ocean` | Turns environmental DNA into a plain-language health score for coastal sites, with Darwin Core exports for anyone who wants the underlying records. First at Lovable × United Nations. |
| **[safe-routes-to-school](https://github.com/adrian-erlikhman/safe-routes-to-school)**<br>`3rd · Code for Transportation` | Risk-weighted walking directions for LA students. A\* over 431,599 blocks, with edge costs derived from 85,634 LAPD incident records. Runs entirely client-side. |
| **[why-wrong](https://github.com/adrian-erlikhman/why-wrong)** | Classifies the specific misconception behind each wrong answer, clusters a class into shared failure modes, then audits whether the test measured anything in the first place. |
| **[regime-aware-portfolio-optimizer](https://github.com/adrian-erlikhman/regime-aware-portfolio-optimizer)** | A Hidden Markov Model infers latent market regimes and shifts allocation when the state turns turbulent. Evaluated on Sharpe against a static 60/40. |
| **[lstm-equity-forecaster](https://github.com/adrian-erlikhman/lstm-equity-forecaster)** | Stacked LSTM on rolling windows, scored on directional accuracy against a linear baseline, not on error alone. |
| **[finbert-sentiment-analyzer](https://github.com/adrian-erlikhman/finbert-sentiment-analyzer)** | FinBERT over financial headlines, aggregated into a daily sentiment signal, with a lexicon fallback so the pipeline still runs without network access. |
| **[fraud-detection-system](https://github.com/adrian-erlikhman/fraud-detection-system)** | Random Forest against Gradient Boosting on 1%-positive data, scored on PR-AUC rather than accuracy and thresholded for recall. |

The site is open too:
[adrian-erlikhman.github.io](https://github.com/adrian-erlikhman/adrian-erlikhman.github.io),
one hand-written `index.html`, no framework. So is the banner above.
[`tools/build.py`](tools/build.py) converts every glyph to an outline and emits
each one once into `<defs>`, so the type renders identically without loading a
webfont.

---

### `[03]` Tooling

Python for modeling: PyTorch, scikit-learn, pandas, Transformers. TypeScript and
plain JavaScript when it has to run in the browser. Postgres and Supabase for
anything that holds state.

---

### `[04]` Reach me

**[erlikhman.adrian@gmail.com](mailto:erlikhman.adrian@gmail.com)** is the
fastest way to get me.
