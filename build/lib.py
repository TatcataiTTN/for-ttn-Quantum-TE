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
        "info_btn": "Thông tin và liên hệ",
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
        "info_btn": "Info and contact",
        "how": "How to study a module",
        "how_steps": ["Read the objectives and step through all slides (each module has 5 parts).",
                      "Open the notebook, run each cell and read the 📤 Real output note after it.",
                      "Take the quiz to check yourself, then revisit whatever you missed."],
        "path": "Study path",
        "path_txt": "Study parts A to E in order: Fourier foundations, probability and noise, discretisation and representation, physical applications, then detection and estimation. Modules tagged \"Both books\" are where the two texts meet, so take those slowly.",
    },
}

HEAD_THEME = ("<script>(function(){var D=document.documentElement;"
              "var FONTS={montserrat:'Montserrat:wght@400;600;800',bevietnam:'Be+Vietnam+Pro:wght@400;600;800',lora:'Lora:wght@400;600;700'};"
              "window.siteLoadFont=function(f){if(!FONTS[f]||document.getElementById('gf-'+f))return;var l=document.createElement('link');"
              "l.id='gf-'+f;l.rel='stylesheet';l.href='https://fonts.googleapis.com/css2?family='+FONTS[f]+'&display=swap';document.head.appendChild(l);};"
              "try{var t=localStorage.getItem('site-theme');if(t&&t!=='auto')D.setAttribute('data-theme',t);"
              "var f=localStorage.getItem('site-font');if(f&&f!=='sans'){D.setAttribute('data-font',f);window.siteLoadFont(f);}"
              "var z=localStorage.getItem('site-size');if(z&&z!=='md')D.setAttribute('data-size',z);}catch(e){}})();</script>")

# ---- contact details (edit here; shown in the info dialog of every page)
CONTACT_NAME = "Trương Tuấn Nghĩa"
CONTACT_PHONE = "(+84) 973 958 574"
CONTACT_PHONE_TEL = "+84973958574"
CONTACT_EMAIL = "truongtuannghia1248@gmail.com"
GITHUB_URL = "https://github.com/TatcataiTTN/for-ttn-Quantum-TE"

THEMES = [("auto", "⟦Tự động||Auto⟧", "conic-gradient(#ffffff 50%,#0f1420 0)"), ("light", "⟦Sáng||Light⟧", "#ffffff"),
          ("dark", "⟦Tối||Dark⟧", "#0f1420"), ("pink", "⟦Hồng||Pink⟧", "#d6336c"), ("blue", "⟦Lam||Blue⟧", "#1d6fd6"),
          ("green", "⟦Lục||Green⟧", "#238b4c"), ("sepia", "⟦Giấy||Sepia⟧", "#9a5b0f"), ("purple", "⟦Tím||Purple⟧", "#6b3fd4")]
FONTS = [("sans", "⟦Hệ thống||System⟧"), ("serif", "Times New Roman"), ("montserrat", "Montserrat"),
         ("bevietnam", "Be Vietnam Pro"), ("lora", "Lora"), ("mono", "Mono")]
SIZES = [("sm", "A−"), ("md", "A"), ("lg", "A+"), ("xl", "A++")]


def appearance_menu():
    th = "".join('<button type="button" data-v="%s"><span class="sw" style="background:%s"></span>%s</button>' % (k, c, n) for k, n, c in THEMES)
    fo = "".join('<button type="button" data-v="%s">%s</button>' % (k, n) for k, n in FONTS)
    sz = "".join('<button type="button" data-v="%s">%s</button>' % (k, n) for k, n in SIZES)
    return ('<details class="menu" data-appearance><summary class="btn">🎨 ⟦Giao diện||Appearance⟧</summary><div class="menu-panel">'
            '<div class="menu-h">⟦Màu nền||Colour theme⟧</div><div class="menu-row" data-group="theme">%s</div>'
            '<div class="menu-h">⟦Phông chữ||Typeface⟧</div><div class="menu-row" data-group="font">%s</div>'
            '<div class="menu-h">⟦Cỡ chữ||Text size⟧</div><div class="menu-row" data-group="size">%s</div>'
            '<p class="lang-note">⟦Lựa chọn được nhớ trên trình duyệt này. Các phông Montserrat, Be Vietnam Pro và Lora chỉ tải từ Google Fonts khi bạn chọn.||'
            'Your choice is remembered in this browser. Montserrat, Be Vietnam Pro and Lora are only loaded from Google Fonts when you pick them.⟧</p>'
            '</div></details>') % (th, fo, sz)


def info_modal():
    return ('<div id="info-modal" class="modal" hidden><div class="modal-card" role="dialog" aria-modal="true">'
            '<button class="modal-x" type="button" data-info-close aria-label="Close">×</button>'
            '<h3>⟦Về nội dung này||About this content⟧</h3>'
            '<p>⟦Nội dung được viết với sự hỗ trợ của AI (Claude), rồi được kiểm lại. Mọi con số do notebook Jupyter tính ra và đối chiếu bằng hai phương pháp độc lập; số trang trích dẫn lấy từ văn bản OCR của hai giáo trình gốc. Vẫn có thể còn sai sót, mong bạn báo lại.||'
            'The content was written with AI assistance (Claude) and then checked. Every number is produced by a Jupyter notebook and cross-checked by two independent methods; page citations come from the OCR text of the two source books. Mistakes may remain, so please report them.⟧</p>'
            '<h3>⟦Liên hệ||Contact⟧</h3>'
            '<ul><li>%(name)s</li><li>⟦Điện thoại / Zalo / Telegram||Phone / Zalo / Telegram⟧: <a href="tel:%(tel)s">%(phone)s</a></li>'
            '<li>Email: <a href="mailto:%(email)s">%(email)s</a></li></ul>'
            '<h3>⟦Sách nguồn||Source books⟧</h3>'
            '<ul><li>R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000.</li>'
            '<li>M. Barkat, <i>Signal Detection and Estimation</i>, 2nd ed., Artech House, 2005.</li></ul>'
            '<p class="lang-note">⟦Trang này chỉ tóm tắt, diễn giải và kiểm số; hãy đọc sách gốc qua thư viện hoặc nhà xuất bản.||'
            'This site only summarises, explains and checks numbers; please read the original books through a library or the publisher.⟧</p>'
            '<h3>⟦Đóng góp||Contribute⟧</h3>'
            '<p>⟦Bạn có thể báo lỗi, đề xuất module mới hoặc bản dịch tại kho mã <a href="%(gh)s" target="_blank" rel="noopener">GitHub</a>, và fork hoặc clone để tự học. Khi chia sẻ lại, hãy ghi nguồn.||'
            'Report errors, suggest modules or translations in the <a href="%(gh)s" target="_blank" rel="noopener">GitHub</a> repository, and fork or clone it for your own study. Please credit the source when sharing.⟧</p>'
            '</div></div>') % dict(name=CONTACT_NAME, tel=CONTACT_PHONE_TEL, phone=CONTACT_PHONE, email=CONTACT_EMAIL, gh=GITHUB_URL)


FAB = '<button class="fab" type="button" data-info-open aria-label="Info" title="Info">ℹ️</button>'
