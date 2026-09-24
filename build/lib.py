"""Helpers shared by the site generator.

Authoring convention: every user-visible string is written once with inline bilingual markup
    ⟦tiếng Việt||English⟧
and is resolved per output language. Numbers that come from notebooks are written as {{key}}
and filled from the executed notebook output (never typed by hand). Math is $...$ / $$...$$.
"""
import html
import re

LANGS = ("vi", "en")
_BI = re.compile(r"⟦(.*?)\|\|(.*?)⟧", re.S)
_PH = re.compile(r"\{\{(fig:)?(\w+)\}\}")


def resolve_lang(s, lang):
    idx = 1 if lang == "vi" else 2
    return _BI.sub(lambda m: m.group(idx), s)


def _tex_block(m):
    return '<div class="tex" data-display="1">%s</div>' % html.escape(m.group(1).strip(), quote=False)


def _tex_inline(m):
    return '<span class="tex">%s</span>' % html.escape(m.group(1), quote=False)


def convert_math(s):
    s = re.sub(r"\$\$(.+?)\$\$", _tex_block, s, flags=re.S)
    return re.sub(r"\$(.+?)\$", _tex_inline, s, flags=re.S)


def fill(s, results, figs, where):
    """Replace {{key}} with executed-notebook values and {{fig:name}} with <figure>."""
    def rep(m):
        if m.group(1):
            if m.group(2) not in figs:
                raise KeyError("%s: missing figure '%s'" % (where, m.group(2)))
            return figs[m.group(2)]
        if m.group(2) not in results:
            raise KeyError("%s: missing result key '%s'" % (where, m.group(2)))
        return results[m.group(2)]
    return _PH.sub(rep, s)


def render(s, lang, results, figs, where):
    return convert_math(fill(resolve_lang(s, lang), results, figs, where))


# ---------- content builders (return strings with ⟦⟧ markup) ----------
def F(label, tex, legend=None):
    """Framed formula block + legend of symbols. legend = [(tex_symbol, explanation), ...]"""
    out = '<div class="pd-formula"><div class="pd-formula-label">%s</div>$$%s$$</div>' % (label, tex)
    if legend:
        out += '<ul class="pd-legend">' + "".join(
            "<li><b>$%s$</b><span>%s</span></li>" % (sym, txt) for sym, txt in legend) + "</ul>"
    return out


def C(kind, title, body):
    """Callout. kind: info | good | warn | bad"""
    return '<div class="callout %s"><b class="h">%s</b>%s</div>' % (kind, title, body)


def UL(items):
    return "<ul>" + "".join("<li>%s</li>" % i for i in items) + "</ul>"


def OL(items):
    return "<ol>" + "".join("<li>%s</li>" % i for i in items) + "</ol>"


def TBL(head, rows):
    h = "<tr>" + "".join("<th>%s</th>" % c for c in head) + "</tr>"
    r = "".join("<tr>" + "".join("<td>%s</td>" % c for c in row) + "</tr>" for row in rows)
    return '<table class="t">%s%s</table>' % (h, r)


def fig_html(src, cap):
    return '<figure class="fig"><img src="%s" alt="%s" loading="lazy"><figcaption>%s</figcaption></figure>' % (
        src, html.escape(re.sub("<.*?>", "", cap), quote=True), cap)


# ---------- UI strings ----------
T = {
    "vi": {
        "site": "Tự học Quantum · Technology Engineering",
        "section": "Xử lý tín hiệu",
        "home": "Trang chủ",
        "modules": "Danh sách module",
        "module": "Module",
        "source": "Nguồn sách",
        "support": "Nguồn bổ trợ",
        "objectives": "Mục tiêu học",
        "lecture": "Bài giảng (slide)",
        "lecture_hint": "Dùng nút, chấm tròn hoặc phím ← → để chuyển slide.",
        "prev": "◀ Trước", "next": "Sau ▶", "fs": "⛶ Toàn màn hình",
        "history": "📜 Bối cảnh lý thuyết & lịch sử",
        "case": "🔎 Case study thực tế",
        "formulas": "🧮 Bảng công thức của module",
        "practice": "🧪 Thực hành với Jupyter Notebook",
        "pitfalls": "⚠️ Những bẫy diễn giải sai",
        "quiz": "✅ Quiz tự kiểm tra",
        "quiz_hint": "Bấm một đáp án để chấm ngay và xem giải thích. Kết quả không được lưu.",
        "score": "Điểm: {s}/{a} đã trả lời (tổng {n} câu)",
        "restart": "Làm lại từ đầu",
        "confirm": "Làm lại sẽ xóa các câu đã trả lời. Tiếp tục?",
        "nb_open": "Mở trên Google Colab",
        "nb_dl": "Tải notebook (.ipynb)",
        "nb_note": "Notebook tự sinh dữ liệu bằng mã, không cần tải file ngoài. Mọi con số trên trang này được in ra từ notebook và đối chiếu bằng hai phương pháp độc lập.",
        "srcs": "Nguồn tham khảo",
        "prevmod": "← Module trước", "nextmod": "Module sau →",
        "other_lang": "English", "other_lang_full": "English edition",
        "lang_note": "Bản tiếng Việt là bản gốc. Bản tiếng Anh viết song song với bản gốc.",
        "open": "Mở bài giảng →",
        "how": "Cách học một module",
        "how_steps": ["Đọc mục tiêu và chạy hết slide (mỗi module có 5 phần).",
                      "Mở notebook, chạy từng cell và đọc phần 📤 Đầu ra thật sau mỗi cell.",
                      "Làm quiz để kiểm tra, rồi đọc lại những phần còn sai."],
        "path": "Lộ trình",
        "path_txt": "Học theo thứ tự các phần A đến E: nền tảng Fourier, xác suất và nhiễu, rời rạc hóa và biểu diễn, ứng dụng vật lý, rồi phát hiện và ước lượng. Module có nhãn \"Cả hai sách\" là nơi hai giáo trình gặp nhau, nên nên học chậm ở đó.",
    },
    "en": {
        "site": "Quantum Self-Study · Technology Engineering",
        "section": "Signal Processing",
        "home": "Home",
        "modules": "Modules",
        "module": "Module",
        "source": "Book source",
        "support": "Supporting sources",
        "objectives": "Learning objectives",
        "lecture": "Lecture (slides)",
        "lecture_hint": "Use the buttons, the dots or the ← → keys to move between slides.",
        "prev": "◀ Prev", "next": "Next ▶", "fs": "⛶ Fullscreen",
        "history": "📜 Theory & historical background",
        "case": "🔎 Real-world case study",
        "formulas": "🧮 Formula sheet for this module",
        "practice": "🧪 Hands-on with the Jupyter Notebook",
        "pitfalls": "⚠️ Common misreadings",
        "quiz": "✅ Self-check quiz",
        "quiz_hint": "Click an answer to grade it immediately and read the explanation. Results are not saved.",
        "score": "Score: {s}/{a} answered (out of {n})",
        "restart": "Start over",
        "confirm": "Starting over clears the answers so far. Continue?",
        "nb_open": "Open in Google Colab",
        "nb_dl": "Download notebook (.ipynb)",
        "nb_note": "The notebook generates its own data in code, so no external files are needed. Every number on this page is printed by the notebook and cross-checked with two independent methods.",
        "srcs": "References",
        "prevmod": "← Previous module", "nextmod": "Next module →",
        "other_lang": "Tiếng Việt", "other_lang_full": "Bản tiếng Việt",
        "lang_note": "The Vietnamese edition is the source text. This English edition was written in parallel with it.",
        "open": "Open lecture →",
        "how": "How to study a module",
        "how_steps": ["Read the objectives and step through all slides (each module has 5 parts).",
                      "Open the notebook, run each cell and read the 📤 Real output note after it.",
                      "Take the quiz to check yourself, then revisit whatever you missed."],
        "path": "Study path",
        "path_txt": "Study parts A to E in order: Fourier foundations, probability and noise, discretisation and representation, physical applications, then detection and estimation. Modules tagged \"Both books\" are where the two texts meet, so take those slowly.",
    },
}

HEAD_THEME = ("<script>(function(){try{var t=localStorage.getItem('site-theme');"
              "if(t&&t!=='auto')document.documentElement.setAttribute('data-theme',t);}catch(e){}})();</script>")
