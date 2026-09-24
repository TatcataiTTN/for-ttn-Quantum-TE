# Sổ tay viết module (đọc file này trước khi viết module mới; mẫu đầy đủ: build/modules/m01.py)

## Cấu trúc file `build/modules/mNN.py`
`from lib import F, C, UL, OL, TBL` rồi `MOD = dict(n, slug, part ("A".."E"), book ("B"|"K"|"BK"), title, blurb, src,
objectives[4-5], parts[5], takeaways[5-6], history, case, practice[4-5 bước], pitfalls[3-4], refs[], quiz[14-15], nb[...])`.
- Mỗi `parts[i] = dict(title, scr=(S,C,R), preview=[3-4 gạch], slides=[(tiêu đề, html), ...])`.
- Quy mô: module một sách ~40 slide TỔNG (5 phần x 6-7 slide nội dung + 5 divider + tiêu đề + tổng kết); module ghép hai sách (book="BK") ~60 slide (5 phần x 10-11). build.py bắt buộc >=36 (một sách) / >=56 (ghép).
- Mỗi slide MỘT ý (40-90 chữ mỗi ngôn ngữ) + công thức `F()` / bảng `TBL()` / hình `{{fig:tên}}` / callout `C()`.

## Đánh dấu
- Song ngữ trong một chuỗi: `⟦tiếng Việt||English⟧` (không dùng `||` bên trong công thức, dùng `\Vert`).
- Số từ notebook: `{{khoá}}` (notebook in `report("khoá", giá_trị, ".6f")`, dòng `▸ khoá = ...`); hình: `{{fig:tên}}`.
- Toán: `$...$` và `$$...$$` (KaTeX). Số thập phân dùng DẤU CHẤM ở cả hai ngôn ngữ.
- Chuỗi Python có `\\` nếu không phải raw string (vd `"$\\Pi$"`); công thức trong `F()` nên dùng raw string `r"..."`.
- Trích dẫn trang chỉ khi đã đọc trang đó trong OCR/text: `(Bracewell, tr. 5)`, `(Barkat, mục 3.5)`.

## Notebook (`nb=[("md", ...), ("code", r'''...''', dict(fig="tên", cap="⟦..||..⟧")), ...]`)
- Mỗi phần: md `## N. Tên` + `🎯 **Phương pháp này trả lời câu hỏi gì?**` -> code (in số bằng `report`) -> (code hình) -> md `#### 📤 Đầu ra thật` giải thích số bằng `{{khoá}}`.
- Có sẵn trong cell đầu (SETUP): `np`, `plt`, `amplitude_spectrum(x)`, `report(key, value, fmt)`. Tự import scipy trong cell.
- MỌI số hiển thị phải tính bằng >=2 phương pháp độc lập và `assert` khớp. Không dùng số ngẫu nhiên nếu tránh được; nếu cần, `np.random.default_rng(seed)`.
- Cell hình: đúng một hình (`plt.show()`), truyền `dict(fig=..., cap=...)`. Nhãn hình dùng `⟦vi||en⟧`.
- `report` tự cắt số 0 thừa ở cuối (0.500000 thành 0.5). Dùng tối đa `.4f` (hoặc `.4g`); số rất nhỏ dùng `.1e`. Tránh "-0": dùng `abs()` hoặc `round(v, 4) + 0.0`.
- Quiz: TỐI THIỂU 30 câu/module (chương 1 khoảng 50), gồm cả câu tính toán triển khai (đáp án in từ notebook).

## Quiz (14-15 câu, `opts[0]` LÀ ĐÁP ÁN ĐÚNG, build.py tự xáo)
- Đáp án đúng KHÔNG được là phương án dài nhất (ngưỡng <5% toàn bộ). Viết đáp án đúng ngắn gọn, phương án nhiễu dài hơn kèm một mệnh đề lý do sai nghe hợp lý. Không độn chữ máy móc.
- Câu số: đáp án đúng `{{khoá}}`, nhiễu lấy từ các khoá khác hoặc số cố định.
- `explain` nêu trang sách hoặc con số từ notebook.

## Kiểm tra
`python3 build/build.py` (chạy notebook thật, kiểm quiz, đếm slide, parse HTML). `--force` để chạy lại toàn bộ notebook.
Xem trang: `python3 -m http.server 8765` trong thư mục dự án; `node /tmp/pp/check.js URL out.png SLIDE_INDEX` (puppeteer-core) nếu còn.
