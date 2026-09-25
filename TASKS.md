# TASKS: Signal Processing (mảng 01)

Hai giáo trình gốc (chỉ dùng hai quyển này, không đọc thêm nguồn khác):

- **B** = R. N. Bracewell, *The Fourier Transform and Its Applications*, 3rd ed. (19 chương nội dung; chương 20 đến 23 là phụ lục)
- **K** = M. Barkat, *Signal Detection and Estimation*, 2nd ed. (12 chương)

## Kết quả đọc mục lục

| Nhóm | Số module | Ghi chú |
|---|---|---|
| Chung của cả hai sách (ghép chương) | 4 | B16+K1, B17+K3, B10+K8, B11+K4 |
| Riêng Bracewell | 15 | B1 đến B9, B12, B13, B14, B15, B18, B19 |
| Riêng Barkat | 7 | K2, K5, K6, K7, K9, K10, K11+K12 (K12 chỉ 7 trang nên gộp với K11) |
| **Tổng** | **26** | 31 chương gốc, ghép còn 26 |

Giao thoa ở mức mục (không ghép chương, chỉ có khung "Liên hệ chéo"): xung B5 và K1.3.1; Hilbert/tín hiệu giải tích B13 và K3.10; lọc B9 và K3.6; Laplace B14 và Wiener khả thực K7.3; khuếch tán B18 và quá trình Wiener K3.4.7; phổ động B19 và K3.5/K3.7; phát hiện dạng sóng nhiễu B17 và K10.

## Bảng module (thứ tự học)

Trạng thái: 🟢 xong (VI + EN + notebook) · 🟡 đang làm · ⚪ chưa làm

| # | Slug | Nguồn | Loại | VI | EN |
|---|---|---|---|---|---|
| 01 | introduction | B1 | riêng B | 🟢 | 🟢 |
| 02 | groundwork | B2 | riêng B | 🟢 | 🟢 |
| 03 | convolution | B3 | riêng B | 🟢 | 🟢 |
| 04 | notation | B4 | riêng B | 🟢 | 🟢 |
| 05 | impulse | B5 | riêng B | 🟢 | 🟢 |
| 06 | theorems | B6 | riêng B | 🟢 | 🟢 |
| 07 | obtaining-transforms | B7 | riêng B | 🟢 | 🟢 |
| 08 | two-domains | B8 | riêng B | 🟢 | 🟢 |
| 09 | filters-linearity | B9 | riêng B | 🟢 | 🟢 |
| 10 | probability-cf | B16 + K1 | CHUNG | 🟢 | 🟢 |
| 11 | distributions | K2 | riêng K | 🟢 | 🟢 |
| 12 | random-processes-noise | B17 + K3 | CHUNG | 🟢 | 🟢 |
| 13 | sampling-series-orthogonal | B10 + K8 | CHUNG | 🟢 | 🟢 |
| 14 | dft-fft-discrete-processes | B11 + K4 | CHUNG | 🟢 | 🟢 |
| 15 | hartley | B12 | riêng B | 🟢 | 🟢 |
| 16 | relatives-of-ft | B13 | riêng B | ⚪ | ⚪ |
| 17 | laplace | B14 | riêng B | ⚪ | ⚪ |
| 18 | antennas-optics | B15 | riêng B | ⚪ | ⚪ |
| 19 | diffusion | B18 | riêng B | ⚪ | ⚪ |
| 20 | dynamic-spectra-wavelets | B19 | riêng B | ⚪ | ⚪ |
| 21 | decision-theory | K5 | riêng K | ⚪ | ⚪ |
| 22 | parameter-estimation | K6 | riêng K | ⚪ | ⚪ |
| 23 | wiener-kalman | K7 | riêng K | ⚪ | ⚪ |
| 24 | general-gaussian | K9 | riêng K | ⚪ | ⚪ |
| 25 | detection-estimation | K10 | riêng K | ⚪ | ⚪ |
| 26 | cfar | K11 + K12 | riêng K | ⚪ | ⚪ |

## Epic

- 🟢 Khung dự án: `_shared/` (CSS, JS, KaTeX cục bộ), `build/build.py` (sinh trang + notebook, chạy notebook thật, điền số liệu), `.nojekyll`
- 🟡 Sản xuất 26 module (mỗi module: 5 phần slide, công thức, lịch sử, case study, notebook VI + EN, quiz, bẫy diễn giải)
- ⚪ Trang chủ nhóm theo sách, portal 4 mảng (mảng 2 đến 4 chỉ là trang "Sắp có")
- ⚪ Kiểm thử: nbconvert toàn bộ, quiz audit, parse HTML, serve-test, chụp trang
- ⚪ Deploy GitHub Pages `TatcataiTTN/for-ttn-Quantum-TE`, kiểm tra URL thật

## Quy ước

- Viết một lần song ngữ bằng `⟦tiếng Việt||English⟧`; số liệu lấy từ `{{khoá}}` do notebook in ra (`▸ khoá = giá trị`), không gõ tay.
- Số thập phân dùng dấu chấm ở cả hai ngôn ngữ để khớp đầu ra notebook.
- Mọi con số phải đối chiếu bằng hai phương pháp độc lập trong notebook (assert).
- Quiz: đáp án đúng không được là phương án dài nhất (kiểm bằng `build.py`, ngưỡng dưới 5%), vị trí đáp án đúng rải đều.
- Chỉ trích dẫn số trang đã đọc trực tiếp trong văn bản OCR/text của hai sách.
