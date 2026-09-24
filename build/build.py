#!/usr/bin/env python3
"""Site generator for for-ttn-Quantum-TE / Signal Processing.

    python3 build/build.py            # build everything (uses execution cache)
    python3 build/build.py --force    # re-execute every notebook
    python3 build/build.py --only 3   # only module 3

Pipeline per module and language:
  1. build notebook from modules/mNN.py  ->  execute it (kernel python3)
  2. read `▸ key = value` lines + figures out of the executed notebook
  3. fill {{key}} / {{fig:name}} into the notebook markdown and into the HTML page
  4. quiz: seeded shuffle + position/length-bias audit
Numbers on the page therefore always come from code that actually ran.
"""
import argparse
import base64
import hashlib
import html
import importlib.util
import json
import random
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

import nbformat
from nbclient.exceptions import CellExecutionError
from nbconvert.preprocessors import ExecutePreprocessor

sys.path.insert(0, str(Path(__file__).parent))
from lib import (LANGS, T, HEAD_THEME, render, resolve_lang, fig_html)  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SP = ROOT / "signal-processing"
CACHE = ROOT / "build" / ".cache"
REPO = "TatcataiTTN/for-ttn-Quantum-TE"
SETUP = '''import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"figure.figsize": (7.5, 3.3), "axes.grid": True, "grid.alpha": 0.3, "figure.dpi": 110})


def amplitude_spectrum(x):
    """⟦Phổ biên độ một phía: sóng hình sin biên độ A cho vạch A, thành phần một chiều cho đúng giá trị của nó||One-sided amplitude spectrum: a sinusoid of amplitude A gives a line of height A, DC gives exactly its value⟧"""
    a = 2*np.abs(np.fft.rfft(x))/len(x)
    a[0] /= 2
    return a


def report(key, value, fmt=".6g"):
    """⟦In một kết quả có tên (trang web đọc các dòng bắt đầu bằng ▸)||Print a named result (the website reads the lines that start with ▸)⟧."""
    print(f"▸ {key} = {value:{fmt}}")
'''


# ------------------------------------------------------------------ modules
def load_modules(only=None):
    mods = []
    for p in sorted((ROOT / "build" / "modules").glob("m[0-9][0-9].py")):
        spec = importlib.util.spec_from_file_location(p.stem, p)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        d = m.MOD
        d["_file"] = p
        d["dir"] = "%02d-%s" % (d["n"], d["slug"])
        d["nbname"] = "%02d_%s" % (d["n"], d["slug"].replace("-", "_"))
        if only is None or d["n"] == only:
            mods.append(d)
    return mods


def nbfile(mod, lang):
    return mod["nbname"] + ("" if lang == "vi" else "_en") + ".ipynb"


# ------------------------------------------------------------------ notebooks
def make_notebook(mod, lang):
    t = T[lang]
    r = lambda s: resolve_lang(s, lang)  # noqa: E731
    nb = nbformat.v4.new_notebook()
    cells = []
    head = "# %s %02d · %s\n\n**%s:** %s\n\n%s" % (
        t["module"], mod["n"], r(mod["title"]), t["source"], r(mod["src"]),
        r("⟦Notebook đi kèm bài giảng cùng số module. Chạy lần lượt từng cell; sau mỗi cell có phần **📤 Đầu ra thật** giải thích con số.||"
          "Companion notebook of the lecture with the same module number. Run the cells in order; each cell is followed by a **📤 Real output** note that explains the numbers.⟧"))
    cells.append(nbformat.v4.new_markdown_cell(head))
    cells.append(nbformat.v4.new_code_cell(r(SETUP)))
    for c in mod["nb"]:
        if c[0] == "md":
            cells.append(nbformat.v4.new_markdown_cell(r(c[1]).strip("\n")))
        else:
            cell = nbformat.v4.new_code_cell(r(c[1]).strip("\n"))
            if len(c) > 2 and c[2].get("fig"):
                cell.metadata["fig"] = c[2]["fig"]
                cell.metadata["cap"] = r(c[2]["cap"])
            cells.append(cell)
    nb.cells = cells
    nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
    nb.metadata["language_info"] = {"name": "python"}
    return nb


def execute(mod, lang, force):
    """Return (executed_nb, results, figs) using a cache keyed by the module source hash."""
    CACHE.mkdir(exist_ok=True)
    key = hashlib.sha256((mod["_file"].read_text(encoding="utf-8") + SETUP + lang).encode()).hexdigest()[:16]
    cpath = CACHE / ("%s_%s.ipynb" % (mod["dir"], lang))
    kpath = CACHE / ("%s_%s.key" % (mod["dir"], lang))
    if not force and cpath.exists() and kpath.exists() and kpath.read_text() == key:
        return nbformat.read(cpath, as_version=4)
    nb = make_notebook(mod, lang)
    ep = ExecutePreprocessor(timeout=300, kernel_name="python3")
    try:
        ep.preprocess(nb, {"metadata": {"path": str(CACHE)}})
    except CellExecutionError as e:
        print("\nNOTEBOOK FAILED: module %d (%s)\n%s" % (mod["n"], lang, e), file=sys.stderr)
        raise
    nbformat.write(nb, cpath)
    kpath.write_text(key)
    return nb


_LINE = re.compile(r"^▸ (\w+) = (.*)$", re.M)


def harvest(nb, mod, lang):
    results, figs = {}, {}
    figdir = SP / "assets" / "figures"
    figdir.mkdir(parents=True, exist_ok=True)
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        for out in cell.get("outputs", []):
            if out.get("output_type") == "stream":
                for k, v in _LINE.findall(out["text"]):
                    if k in results and results[k] != v.strip():
                        raise ValueError("duplicate result key with different value: %s" % k)
                    results[k] = v.strip()
        name = cell.metadata.get("fig")
        if name:
            png = None
            for out in cell.get("outputs", []):
                if out.get("output_type") in ("display_data", "execute_result") and "image/png" in out.get("data", {}):
                    png = out["data"]["image/png"]
            if png is None:
                raise ValueError("module %d: figure cell '%s' produced no image" % (mod["n"], name))
            fname = "%02d_%s_%s.png" % (mod["n"], name, lang)
            (figdir / fname).write_bytes(base64.b64decode(png))
            figs[name] = (fname, cell.metadata["cap"])
    return results, figs


def write_final_notebook(nb, mod, lang, results):
    """Fill {{key}} placeholders in markdown cells, then write to signal-processing/notebooks."""
    out = nbformat.from_dict(json.loads(json.dumps(nb)))
    for cell in out.cells:
        if cell.cell_type == "markdown":
            def rep(m):
                if m.group(2) not in results:
                    raise KeyError("notebook md of module %d (%s): missing key %s" % (mod["n"], lang, m.group(2)))
                return results[m.group(2)]
            cell.source = re.sub(r"\{\{(fig:)?(\w+)\}\}", rep, cell.source)
    d = SP / "notebooks"
    d.mkdir(exist_ok=True)
    nbformat.write(out, d / nbfile(mod, lang))


# ------------------------------------------------------------------ quiz
def build_quiz_sets(mods, results):
    """Seeded, globally balanced answer positions + length-bias audit (authors rewrite offenders; nothing is padded)."""
    allq = [(m["n"], i, q) for m in mods for i, q in enumerate(m["quiz"])]
    rng = random.Random(20260924)
    targets = [i % 4 for i in range(len(allq))]
    rng.shuffle(targets)
    out = {}
    stats = {}
    for lang in LANGS:
        n_long = 0
        offenders = []
        pos = [0, 0, 0, 0]
        for (n, i, q), tgt in zip(allq, targets):
            opts = [fill_only(o, lang, results[n], {}, "quiz m%02d" % n) for o in q["opts"]]
            correct = opts[0]
            others = opts[1:]
            orng = random.Random(n * 1000 + i)  # same order in both languages
            order = list(range(3))
            orng.shuffle(order)
            others = [others[k] for k in order]
            strip = lambda s: re.sub(r"<.*?>", "", s)  # noqa: E731
            final = others[:tgt] + [correct] + others[tgt:]
            item = {"q": resolve_lang(q["q"], lang), "opts": final, "correct": tgt,
                    "explain": resolve_lang(q["explain"], lang)}
            out.setdefault((n, lang), []).append(item)
            pos[tgt] += 1
            if all(len(strip(final[tgt])) > len(strip(o)) for j, o in enumerate(final) if j != tgt):
                n_long += 1
                offenders.append("m%02d q%d" % (n, i + 1))
        N = len(allq)
        exp = N / 4
        chi2 = sum((p - exp) ** 2 / exp for p in pos)
        stats[lang] = (N, n_long, pos, chi2, offenders)
    print("\nQUIZ AUDIT (strictly-longest = correct answer is longer than all 3 distractors)")
    for lang, (N, nl, pos, chi2, offenders) in stats.items():
        print("  %s: %d questions | correct==strictly longest: %d (%.1f%%) | positions %s | chi2=%.2f (df=3, crit 7.81)" % (
            lang, N, nl, 100 * nl / N, pos, chi2))
        if offenders:
            print("     rewrite so the correct option is not the longest:", ", ".join(offenders))
        assert 100 * nl / N < 5, "length bias above 5%% for %s" % lang
        assert chi2 < 7.81, "position distribution not uniform for %s" % lang
    return out


# ------------------------------------------------------------------ html
class _P(HTMLParser):
    VOID = {"meta", "link", "br", "img", "hr", "input"}

    def __init__(self):
        super().__init__()
        self.stack = []

    def handle_starttag(self, tag, attrs):
        if tag not in self.VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        if not self.stack or self.stack.pop() != tag:
            raise ValueError("unbalanced </%s>" % tag)


def check_html(s, where):
    p = _P()
    p.feed(s)
    if p.stack:
        raise ValueError("%s: unclosed tags %s" % (where, p.stack))


def page(lang, title, body, root, other_href=None, crumbs="", desc=""):
    t = T[lang]
    desc = html.escape(re.sub(r"<.*?>", "", desc), quote=True)
    other = ""
    if other_href:
        other = '<a class="btn" href="%s" hreflang="%s">%s</a>' % (other_href, "en" if lang == "vi" else "vi", t["other_lang"])
    return """<!DOCTYPE html>
<html lang="%(lang)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="icon" href="data:,">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
%(theme)s
<link rel="stylesheet" href="%(root)s_shared/katex/katex.min.css">
<link rel="stylesheet" href="%(root)s_shared/common.css">
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="%(root)sindex.html">⚛ %(site)s</a>
<nav>%(other)s<button class="btn" type="button" data-theme-toggle aria-label="Theme">◑</button></nav>
</div></header>
<main class="wrap">
%(crumbs)s
%(body)s
<footer class="foot">%(note)s</footer>
</main>
<script src="%(root)s_shared/katex/katex.min.js"></script>
<script src="%(root)s_shared/site.js"></script>
</body>
</html>
""" % dict(lang=lang, title=title, desc=desc, theme=HEAD_THEME, root=root, site=t["site"], other=other,
           crumbs=crumbs, body=body, note=t["lang_note"])


FORMULA_RE = re.compile(
    r'<div class="pd-formula"><div class="pd-formula-label">.*?</div>\$\$.*?\$\$</div>(?:<ul class="pd-legend">.*?</ul>)?',
    re.S)


def build_module_page(mod, lang, mods, results, figs, quiz):
    t = T[lang]
    where = "module %d (%s)" % (mod["n"], lang)
    figs_html = {k: fig_html("../../../assets/figures/" + fn, cap) for k, (fn, cap) in figs.items()}
    R = lambda s: render(s, lang, results, figs_html, where)  # noqa: E731
    rr = lambda s: fill_only(s, lang, results, figs_html, where)  # noqa: E731

    # ---- deck
    slides = []
    obj = "<ul class='obj'>" + "".join("<li>%s</li>" % o for o in mod["objectives"]) + "</ul>"
    slides.append('<div class="mdeck-slide" data-title="%s"><div class="kicker">%s %02d · %s</div><h3>%s</h3>%s'
                  '<p class="lang-note">%s</p></div>' % (
                      plain(mod["title"]), t["module"].upper(), mod["n"], mod["src"], mod["title"], obj, t["lecture_hint"]))
    for pi, p in enumerate(mod["parts"], 1):
        s, c, r_ = p["scr"]
        prev = "".join("<li>%s</li>" % x for x in p["preview"])
        slides.append(
            '<div class="mdeck-slide part-divider" data-title="%s"><div class="kicker">%s %d/5</div><div class="part-num">%02d</div>'
            '<h2>%s</h2><div class="scr"><div><b>%s</b> %s</div><div><b>%s</b> %s</div><div><b>%s</b> %s</div></div>'
            '<ul class="part-list">%s</ul></div>' % (
                plain(p["title"]), "⟦PHẦN||PART⟧", pi, pi, p["title"],
                "⟦Bối cảnh:||Situation:⟧", s, "⟦Vướng mắc:||Complication:⟧", c, "⟦Giải pháp:||Resolution:⟧", r_, prev))
        for st_title, st_body in p["slides"]:
            slides.append('<div class="mdeck-slide" data-title="%s"><div class="kicker">%d/5 · %s</div><h3>%s</h3>%s</div>' % (
                plain(st_title), pi, p["title"], st_title, st_body))
    slides.append('<div class="mdeck-slide" data-title="%s"><div class="kicker">%s</div><h3>%s</h3><ul>%s</ul></div>' % (
        "⟦Tổng kết||Summary⟧", "⟦TỔNG KẾT||SUMMARY⟧", "⟦Điều cần mang theo||Takeaways⟧",
        "".join("<li>%s</li>" % x for x in mod["takeaways"])))
    deck_raw = "".join(slides)
    deck = ('<div class="mdeck"><div class="mdeck-progress"><i></i></div><div class="mdeck-viewport">%s</div><div class="mdeck-bar">'
            '<button class="mdeck-prev" type="button">%s</button><button class="mdeck-next" type="button">%s</button>'
            '<span class="mdeck-count"></span><select class="mdeck-jump" aria-label="Slide"></select>'
            '<button class="mdeck-fs" type="button">%s</button></div></div>') % (
        deck_raw, t["prev"], t["next"], t["fs"])

    # ---- formula sheet (auto-collected from slides)
    resolved_deck = rr(deck_raw)
    formulas = FORMULA_RE.findall(resolved_deck)
    sheet = "".join(formulas)

    nbrel = "../../../notebooks/" + nbfile(mod, lang)
    colab = "https://colab.research.google.com/github/%s/blob/main/signal-processing/notebooks/%s" % (REPO, nbfile(mod, lang))
    practice = ('<div class="callout good"><b class="h">%s</b>%s</div>'
                '<p><a class="btn primary" href="%s" target="_blank" rel="noopener">%s</a> '
                '<a class="btn" href="%s" download>%s</a></p><p class="lang-note">%s</p>') % (
        "⟦Các bước thực hành||Steps⟧", "<ol>" + "".join("<li>%s</li>" % s for s in mod["practice"]) + "</ol>",
        colab, t["nb_open"], nbrel, t["nb_dl"], t["nb_note"])
    pitfalls = "".join('<div class="callout warn">%s</div>' % p for p in mod["pitfalls"])
    refs = "<ul>" + "".join("<li>%s</li>" % x for x in mod.get("refs", [])) + "</ul>"
    quiz_json = json.dumps({"scoreLabel": t["score"], "restart": t["restart"], "confirm": t["confirm"],
                            "items": [dict(i, q=render(i["q"], lang, results, {}, where),
                                           opts=[render(o, lang, results, {}, where) for o in i["opts"]],
                                           explain=render(i["explain"], lang, results, {}, where))
                                      for i in quiz]}, ensure_ascii=False).replace("</", "<\\/")

    idx = [m["n"] for m in mods].index(mod["n"])
    pn = ""
    if idx > 0:
        pm = mods[idx - 1]
        pn += '<a class="btn" href="../%s/index.html">%s</a> ' % (pm["dir"], t["prevmod"])
    if idx < len(mods) - 1:
        nm = mods[idx + 1]
        pn += '<a class="btn primary" href="../%s/index.html">%s</a>' % (nm["dir"], t["nextmod"])

    support = ('<p><span class="tag">%s</span> %s</p>' % (t["support"], mod["support"])) if mod.get("support") else ""
    body = """
<div class="hero">
<span class="tag">%(module)s %(n)02d</span><span class="tag">%(src)s</span>
<h1>%(title)s</h1>
<p class="lead">%(blurb)s</p>
%(support)s
<p><a class="btn primary" href="#lecture">%(lecture)s</a> <a class="btn" href="#practice">%(practice_s)s</a> <a class="btn" href="#quiz">%(quiz_s)s</a></p>
</div>
<h2 class="sec" id="lecture">%(lecture)s</h2>
%(deck)s
<h2 class="sec">%(history_t)s</h2><div class="card">%(history)s</div>
<h2 class="sec">%(case_t)s</h2><div class="card">%(case)s</div>
<h2 class="sec">%(formulas_t)s</h2>%(sheet)s
<h2 class="sec" id="practice">%(practice_t)s</h2>%(practice)s
<h2 class="sec">%(pitfalls_t)s</h2>%(pitfalls)s
<h2 class="sec" id="quiz">%(quiz_t)s</h2><p class="lang-note">%(quiz_hint)s</p>
<div class="quiz"><div id="quiz-root"></div></div>
<script type="application/json" id="quiz-data">%(quiz_json)s</script>
<h2 class="sec">%(srcs)s</h2>%(refs)s
<p>%(pn)s</p>
""" % dict(module=t["module"], n=mod["n"], src=mod["src"], title=mod["title"], blurb=mod["blurb"], support=support,
           lecture=t["lecture"], practice_s=t["practice"].split(" ", 1)[1], quiz_s=t["quiz"].split(" ", 1)[1],
           deck=deck, history_t=t["history"], history=mod["history"], case_t=t["case"], case=mod["case"],
           formulas_t=t["formulas"], sheet="__SHEET__", practice_t=t["practice"], practice=practice,
           pitfalls_t=t["pitfalls"], pitfalls=pitfalls, quiz_t=t["quiz"], quiz_hint=t["quiz_hint"],
           quiz_json="__QUIZ__", srcs=t["srcs"], refs=refs, pn=pn)
    # resolve language / placeholders / math everywhere except the JSON (already rendered) and the sheet
    body = body.replace("__SHEET__", sheet)
    quiz_token = "\x00QUIZ\x00"
    body = body.replace("__QUIZ__", quiz_token)
    body = R(body)
    body = body.replace(quiz_token, quiz_json)
    title = "%s %02d · %s" % (t["module"], mod["n"], resolve_lang(mod["title"], lang))
    crumbs = '<div class="crumbs"><a href="../../../../index.html">%s</a> / <a href="../../../index.html">%s</a> / <a href="../../index.html">%s</a></div>' % (
        t["home"], t["section"], t["modules"])
    other_lang = "en" if lang == "vi" else "vi"
    html_out = page(lang, title, body, "../../../../", "../../../%s/modules/%s/index.html" % (other_lang, mod["dir"]),
                    crumbs, desc=resolve_lang(mod["blurb"], lang))
    return html_out


def plain(s):
    """Slide title as plain text for the jump list (no tags, no math markers)."""
    return html.escape(re.sub(r"<.*?>|\$", "", s), quote=True)


def fill_only(s, lang, results, figs, where):
    from lib import fill
    return fill(resolve_lang(s, lang), results, figs, where)


PLAN = [  # (n, slug, part, book, title, source)
    (1, "introduction", "A", "B", "⟦Giới thiệu: vì sao dùng biến đổi Fourier||Introduction: why transform methods⟧", "⟦Bracewell, chương 1||Bracewell, chapter 1⟧"),
    (2, "groundwork", "A", "B", "⟦Nền tảng: biến đổi, tồn tại, đối xứng||Groundwork: transform, existence, symmetry⟧", "⟦Bracewell, chương 2||Bracewell, chapter 2⟧"),
    (3, "convolution", "A", "B", "⟦Tích chập||Convolution⟧", "⟦Bracewell, chương 3||Bracewell, chapter 3⟧"),
    (4, "notation", "A", "B", "⟦Ký hiệu cho các hàm hữu ích||Notation for some useful functions⟧", "⟦Bracewell, chương 4||Bracewell, chapter 4⟧"),
    (5, "impulse", "A", "B", "⟦Ký hiệu xung||The impulse symbol⟧", "⟦Bracewell, chương 5||Bracewell, chapter 5⟧"),
    (6, "theorems", "A", "B", "⟦Các định lý cơ bản||The basic theorems⟧", "⟦Bracewell, chương 6||Bracewell, chapter 6⟧"),
    (7, "obtaining-transforms", "A", "B", "⟦Cách tìm biến đổi||Obtaining transforms⟧", "⟦Bracewell, chương 7||Bracewell, chapter 7⟧"),
    (8, "two-domains", "A", "B", "⟦Hai miền||The two domains⟧", "⟦Bracewell, chương 8||Bracewell, chapter 8⟧"),
    (9, "filters-linearity", "A", "B", "⟦Dạng sóng, phổ, bộ lọc và tuyến tính||Waveforms, spectra, filters and linearity⟧", "⟦Bracewell, chương 9||Bracewell, chapter 9⟧"),
    (10, "probability-cf", "B", "BK", "⟦Xác suất và hàm đặc trưng||Probability and the characteristic function⟧", "⟦Bracewell chương 16 + Barkat chương 1||Bracewell ch. 16 + Barkat ch. 1⟧"),
    (11, "distributions", "B", "K", "⟦Các phân phối xác suất||Probability distributions⟧", "⟦Barkat, chương 2||Barkat, chapter 2⟧"),
    (12, "random-processes-noise", "B", "BK", "⟦Quá trình ngẫu nhiên, nhiễu và phổ công suất||Random processes, noise and power spectra⟧", "⟦Bracewell chương 17 + Barkat chương 3||Bracewell ch. 17 + Barkat ch. 3⟧"),
    (13, "sampling-series-orthogonal", "C", "BK", "⟦Lấy mẫu, chuỗi Fourier và khai triển trực giao||Sampling, Fourier series and orthogonal expansions⟧", "⟦Bracewell chương 10 + Barkat chương 8||Bracewell ch. 10 + Barkat ch. 8⟧"),
    (14, "dft-fft-discrete-processes", "C", "BK", "⟦DFT, FFT và quá trình ngẫu nhiên rời rạc||DFT, FFT and discrete-time random processes⟧", "⟦Bracewell chương 11 + Barkat chương 4||Bracewell ch. 11 + Barkat ch. 4⟧"),
    (15, "hartley", "C", "B", "⟦Biến đổi Hartley||The Hartley transform⟧", "⟦Bracewell, chương 12||Bracewell, chapter 12⟧"),
    (16, "relatives-of-ft", "C", "B", "⟦Họ hàng của biến đổi Fourier||Relatives of the Fourier transform⟧", "⟦Bracewell, chương 13||Bracewell, chapter 13⟧"),
    (17, "laplace", "C", "B", "⟦Biến đổi Laplace||The Laplace transform⟧", "⟦Bracewell, chương 14||Bracewell, chapter 14⟧"),
    (18, "antennas-optics", "D", "B", "⟦Ăng-ten và quang học||Antennas and optics⟧", "⟦Bracewell, chương 15||Bracewell, chapter 15⟧"),
    (19, "diffusion", "D", "B", "⟦Dẫn nhiệt và khuếch tán||Heat conduction and diffusion⟧", "⟦Bracewell, chương 18||Bracewell, chapter 18⟧"),
    (20, "dynamic-spectra-wavelets", "D", "B", "⟦Phổ động và wavelet||Dynamic spectra and wavelets⟧", "⟦Bracewell, chương 19||Bracewell, chapter 19⟧"),
    (21, "decision-theory", "E", "K", "⟦Lý thuyết quyết định thống kê||Statistical decision theory⟧", "⟦Barkat, chương 5||Barkat, chapter 5⟧"),
    (22, "parameter-estimation", "E", "K", "⟦Ước lượng tham số||Parameter estimation⟧", "⟦Barkat, chương 6||Barkat, chapter 6⟧"),
    (23, "wiener-kalman", "E", "K", "⟦Lọc Wiener và Kalman||Wiener and Kalman filtering⟧", "⟦Barkat, chương 7||Barkat, chapter 7⟧"),
    (24, "general-gaussian", "E", "K", "⟦Bài toán Gauss tổng quát||The general Gaussian problem⟧", "⟦Barkat, chương 9||Barkat, chapter 9⟧"),
    (25, "detection-estimation", "E", "K", "⟦Phát hiện và ước lượng tham số||Detection and parameter estimation⟧", "⟦Barkat, chương 10||Barkat, chapter 10⟧"),
    (26, "cfar", "E", "K", "⟦Phát hiện CFAR thích nghi và phân tán||Adaptive and distributed CFAR detection⟧", "⟦Barkat, chương 11 và 12||Barkat, chapters 11 and 12⟧"),
]
COMING = "⟦Sắp có||Coming soon⟧"


PARTS = {
    "A": ("⟦Phần A · Nền tảng và bộ công cụ Fourier||Part A · Fourier foundations and toolkit⟧",),
    "B": ("⟦Phần B · Xác suất, phân phối và nhiễu||Part B · Probability, distributions and noise⟧",),
    "C": ("⟦Phần C · Rời rạc hóa, biểu diễn và các phép biến đổi họ hàng||Part C · Discretisation, representation and related transforms⟧",),
    "D": ("⟦Phần D · Ứng dụng vật lý||Part D · Physical applications⟧",),
    "E": ("⟦Phần E · Phát hiện và ước lượng tín hiệu||Part E · Signal detection and estimation⟧",),
}
BOOKBADGE = {
    "B": ("⟦Bracewell||Bracewell⟧", ""),
    "K": ("⟦Barkat||Barkat⟧", ""),
    "BK": ("⟦Cả hai sách||Both books⟧", "background:var(--good-bg);color:var(--good)"),
}


def build_lang_index(lang, mods):
    t = T[lang]
    built = {m["n"]: m for m in mods}
    groups = ""
    for pk, (ptitle,) in PARTS.items():
        cards = ""
        for n, slug, part, book, title, src in PLAN:
            if part != pk:
                continue
            bt, bstyle = BOOKBADGE[book]
            if n in built:
                m = built[n]
                cards += ('<a class="mod-card" href="modules/%s/index.html"><span class="num">%s %02d</span>'
                          '<h3>%s</h3><p>%s</p><p><span class="tag" style="%s">%s</span><span class="tag">%s</span></p></a>') % (
                    m["dir"], t["module"].upper(), n, m["title"], m["blurb"], bstyle, bt, m["src"])
            else:
                cards += ('<div class="mod-card soon"><span class="num">%s %02d</span><h3>%s</h3>'
                          '<p><span class="tag" style="%s">%s</span><span class="tag">%s</span></p><p>%s</p></div>') % (
                    t["module"].upper(), n, title, bstyle, bt, src, COMING)
        groups += '<h2 class="sec">%s</h2><div class="grid">%s</div>' % (ptitle, cards)
    nbk = len([p for p in PLAN if p[3] == "BK"]); nb_ = len([p for p in PLAN if p[3] == "B"]); nk_ = len([p for p in PLAN if p[3] == "K"])
    stats = ("⟦%d module (đã xong %d): %d chung của cả hai sách, %d riêng Bracewell, %d riêng Barkat.||"
             "%d modules (%d done): %d shared by both books, %d Bracewell only, %d Barkat only.⟧")
    stats = resolve_lang(stats, lang) % (len(PLAN), len(built), nbk, nb_, nk_)
    steps = "".join("<li>%s</li>" % s for s in t["how_steps"])
    body = ('<div class="hero"><h1>%s</h1><p class="lead">%s</p><p class="lead">%s</p></div>'
            '<div class="card"><b>%s</b><ol>%s</ol><b>%s</b><p>%s</p></div>%s') % (
        t["section"],
        "⟦Hai giáo trình gốc: R. N. Bracewell, <i>The Fourier Transform and Its Applications</i> (3rd ed.) và M. Barkat, <i>Signal Detection and Estimation</i> (2nd ed.). Mỗi chương là một module; các chương trùng chủ đề được ghép làm một.||"
        "Two source books: R. N. Bracewell, <i>The Fourier Transform and Its Applications</i> (3rd ed.) and M. Barkat, <i>Signal Detection and Estimation</i> (2nd ed.). Each chapter is a module; chapters on the same topic are merged into one.⟧",
        stats, t["how"], steps, t["path"], t["path_txt"], groups)
    body = resolve_lang(body, lang)
    crumbs = '<div class="crumbs"><a href="../../index.html">%s</a> / %s</div>' % (t["home"], t["section"])
    other = "en" if lang == "vi" else "vi"
    return page(lang, t["section"], body, "../../", "../%s/index.html" % other, crumbs)


# ------------------------------------------------------------------ portal
PORTAL_CSS_TOGGLE = ('<style>html[data-ui="vi"] [lang="en"].bi{display:none}html[data-ui="en"] [lang="vi"].bi{display:none}</style>'
                     '<script>(function(){var u="vi";try{u=localStorage.getItem("site-ui")||((navigator.language||"vi").slice(0,2)==="en"?"en":"vi")}catch(e){}'
                     'document.documentElement.setAttribute("data-ui",u);})();</script>')
PORTAL_JS = ('<script>document.querySelectorAll("[data-ui-toggle]").forEach(function(b){b.addEventListener("click",function(){'
             'var u=document.documentElement.getAttribute("data-ui")==="vi"?"en":"vi";'
             'try{localStorage.setItem("site-ui",u)}catch(e){}document.documentElement.setAttribute("data-ui",u);});});</script>')

SECTIONS = [
    dict(dir="signal-processing", num="1", vi="Xử lý tín hiệu", en="Signal Processing", live=True,
         vi_d="Biến đổi Fourier, xác suất, phát hiện và ước lượng từ hai giáo trình Bracewell và Barkat: 26 module song ngữ, có slide, notebook và quiz.",
         en_d="Fourier transforms, probability, detection and estimation from Bracewell and Barkat: 26 bilingual modules with slides, notebooks and quizzes.",
         books=["R. N. Bracewell, The Fourier Transform and Its Applications (3rd ed.)", "M. Barkat, Signal Detection and Estimation (2nd ed., 2005)"]),
    dict(dir="quantum-mechanics", num="2", vi="Cơ học lượng tử", en="Quantum Mechanics", live=False,
         vi_d="Sắp có.", en_d="Coming soon.",
         books=["D. J. Griffiths and D. F. Schroeter, Introduction to Quantum Mechanics (Cambridge University Press)", "J. J. Sakurai and J. Napolitano, Modern Quantum Mechanics, 3rd ed. (Cambridge University Press)"]),
    dict(dir="quantum-computing", num="3", vi="Tính toán lượng tử", en="Quantum Computing", live=False,
         vi_d="Sắp có.", en_d="Coming soon.",
         books=["M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, 2010)", "W. Scherer, Mathematics of Quantum Computing"]),
    dict(dir="quantum-optics", num="4", vi="Quang học lượng tử", en="Quantum Optics", live=False,
         vi_d="Sắp có.", en_d="Coming soon.",
         books=["Introductory Quantum Optics (Cambridge University Press)", "D. A. Steck, Quantum and Atom Optics (revision 0.8.3, 2012)"]),
]


def portal_page(title, body, root):
    return """<!DOCTYPE html>
<html lang="vi" data-ui="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="icon" href="data:,">
<title>%s</title>
%s
%s
<link rel="stylesheet" href="%s_shared/common.css">
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="%sindex.html">⚛ Quantum · Technology Engineering</a>
<nav><button class="btn" type="button" data-ui-toggle>VI / EN</button><button class="btn" type="button" data-theme-toggle aria-label="Theme">◑</button></nav>
</div></header>
<main class="wrap">%s</main>
<script src="%s_shared/site.js"></script>
%s
</body>
</html>
""" % (title, HEAD_THEME, PORTAL_CSS_TOGGLE, root, root, body, root, PORTAL_JS)


def bi(vi, en, tag="span"):
    return '<%s class="bi" lang="vi">%s</%s><%s class="bi" lang="en">%s</%s>' % (tag, vi, tag, tag, en, tag)


def build_portal(n_modules, n_done):
    cards = ""
    for s in SECTIONS:
        st = "" if s["live"] else " soon"
        cards += ('<a class="mod-card%s" href="%s/index.html"><span class="num">%s</span><h3>%s</h3><p>%s</p></a>' % (
            st, s["dir"], "0" + s["num"], bi(s["vi"], s["en"]), bi(s["vi_d"], s["en_d"])))
    body = ('<div class="hero"><h1>%s</h1><p class="lead">%s</p></div><div class="grid">%s</div>'
            '<footer class="foot">%s</footer>') % (
        bi("Chuỗi series tự học Technology Engineering · Quantum", "Technology Engineering self-study series · Quantum", "span"),
        bi("Bốn mảng kiến thức nền cho hướng công nghệ lượng tử. Hiện mới hoàn thiện mảng 01, các mảng còn lại đang chờ.",
           "Four foundation areas for quantum technology. Only area 01 is complete so far; the others are on the way.", "span"),
        cards,
        bi("Chạy 100% trong trình duyệt, không cần máy chủ. Chọn VI / EN ở góc trên.", "Runs 100% in the browser, no server needed. Switch VI / EN at the top.", "span"))
    (ROOT / "index.html").write_text(portal_page("Quantum · Technology Engineering", body, ""), encoding="utf-8")

    for s in SECTIONS:
        d = ROOT / s["dir"]
        d.mkdir(exist_ok=True)
        books = "".join("<li>%s</li>" % b for b in s["books"])
        if s["live"]:
            btns = ('<p><a class="btn primary" href="vi/index.html">Tiếng Việt · %d/%d module</a> '
                    '<a class="btn primary" href="en/index.html">English · %d/%d modules</a></p>') % (n_done, n_modules, n_done, n_modules)
            status = ""
        else:
            btns = ""
            status = '<div class="callout warn"><b class="h">%s</b>%s</div>' % (
                bi("Sắp có", "Coming soon"),
                bi("Mảng này chưa được xây dựng. Các sách nguồn đã chuẩn bị:", "This area has not been built yet. Source books on hand:", "span"))
        body = ('<div class="crumbs"><a href="../index.html">Home</a></div><div class="hero"><h1>%s</h1><p class="lead">%s</p></div>%s%s'
                '<div class="card"><b>%s</b><ul>%s</ul></div>') % (
            bi(s["vi"], s["en"]), bi(s["vi_d"], s["en_d"]), btns, status, bi("Sách nguồn", "Source books"), books)
        (d / "index.html").write_text(portal_page(s["en"], body, "../"), encoding="utf-8")


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--only", type=int)
    a = ap.parse_args()
    all_mods = load_modules()
    ns = [m["n"] for m in all_mods]
    assert len(ns) == len(set(ns)), "duplicate module numbers"
    R, FG, NB = {}, {}, {}
    for mod in all_mods:
        res, figs, nbs = {}, {}, {}
        for lang in LANGS:
            print("· module %02d %s: notebook (%s)" % (mod["n"], mod["slug"], lang), flush=True)
            nb = execute(mod, lang, a.force)
            r, f = harvest(nb, mod, lang)
            res[lang], figs[lang], nbs[lang] = r, f, nb
        if res["vi"] != res["en"]:
            diff = {k: (res["vi"].get(k), res["en"].get(k)) for k in set(res["vi"]) | set(res["en"])
                    if res["vi"].get(k) != res["en"].get(k)}
            raise SystemExit("module %d: VI and EN notebooks disagree: %s" % (mod["n"], diff))
        R[mod["n"]], FG[mod["n"]], NB[mod["n"]] = res["vi"], figs, nbs
    quiz_sets = build_quiz_sets(all_mods, R)

    for mod in all_mods:
        if a.only is not None and mod["n"] != a.only:
            continue
        for lang in LANGS:
            write_final_notebook(NB[mod["n"]][lang], mod, lang, R[mod["n"]])
            html_out = build_module_page(mod, lang, all_mods, R[mod["n"]], FG[mod["n"]][lang], quiz_sets[(mod["n"], lang)])
            check_html(html_out, "module %d %s" % (mod["n"], lang))
            n_sl = html_out.count('class="mdeck-slide')
            need = 56 if mod["book"] == "BK" else 36
            print("  module %02d %s: %d slides (min %d)" % (mod["n"], lang, n_sl, need))
            assert n_sl >= need, "module %d has too few slides" % mod["n"]
            d = SP / lang / "modules" / mod["dir"]
            d.mkdir(parents=True, exist_ok=True)
            (d / "index.html").write_text(html_out, encoding="utf-8")
    for lang in LANGS:
        d = SP / lang
        d.mkdir(parents=True, exist_ok=True)
        s_ = build_lang_index(lang, all_mods)
        check_html(s_, "index " + lang)
        (d / "index.html").write_text(s_, encoding="utf-8")
    build_portal(len(PLAN), len(all_mods))
    print("OK: %d module(s) in the index" % len(all_mods))


if __name__ == "__main__":
    main()
