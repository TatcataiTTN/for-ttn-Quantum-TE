from lib import F, C, UL, OL, TBL

MOD = dict(
    n=7, slug="obtaining-transforms", part="A", book="B",
    title="⟦Cách thu được biến đổi Fourier||Obtaining transforms⟧",
    blurb="⟦Tích phân dạng đóng, biến đổi số bằng chương trình \"chậm\", sinh biến đổi từ định lý, đạo hàm để quy về xung, và đo phổ bằng thiết bị.||"
          "Closed-form integration, numerical transformation with the \"slow\" program, generating transforms from theorems, differentiation down to impulses, and measuring spectra with instruments.⟧",
    src="⟦Bracewell, chương 7, tr. 136–150||Bracewell, chapter 7, pp. 136–150⟧",
    data="⟦Sinh bằng mã: xung chữ nhật lấy mẫu, hàm bậc thang, tam giác, parabol, hai vạch phổ gần nhau, dữ liệu 7 ngày||Generated in code: sampled rectangles, staircase functions, triangles, a parabola, two closely spaced spectral lines, 7-day data⟧",
    objectives=[
        "⟦Tính biến đổi bằng tích phân dạng đóng cho xung chữ nhật, hàm bậc thang, chuỗi xung, $e^{-|x|}$, Gauss, $1/x$ và $\\text{sgn}\\,x$.||Compute transforms by closed-form integration for rectangles, staircase functions, impulse trains, $e^{-|x|}$, the Gaussian, $1/x$ and $\\text{sgn}\\,x$.⟧",
        "⟦Viết và kiểm tra chương trình biến đổi Fourier \"chậm\", chọn $K$, $X$ và hiểu vì sao dữ liệu hữu hạn cho sai số chồng phổ.||Write and test the \"slow\" Fourier transform program, choose $K$ and $X$, and understand why finite data give an aliasing error.⟧",
        "⟦Sinh biến đổi mới từ định lý tích chập và định lý đạo hàm (quy về xung).||Generate new transforms from the convolution and derivative theorems (reduction to impulses).⟧",
        "⟦Hiểu nguyên lý đo phổ: máy phân tích tần số vô tuyến và quang phổ biến đổi Fourier.||Understand how spectra are measured: the radio-frequency spectrum analyzer and optical Fourier transform spectroscopy.⟧",
        "⟦Kiểm tra kết quả bằng số ngay cả khi làm đại số bằng tay.||Check results numerically even when the algebra is done by hand.⟧",
    ],
    parts=[
        # ------------------------------------------------ PART 1
        dict(
            title="⟦Tích phân dạng đóng||Integration in closed form⟧",
            scr=("⟦Các cặp biến đổi ở chương trước được nêu mà không chứng minh, và chỉ nói \"kiểm được bằng tích phân Fourier\".||The transform pairs of the previous chapter were asserted without derivation, only \"verifiable by evaluating the Fourier integral\".⟧",
                 "⟦Muốn tạo cặp mới thì cần các cách thực hiện phép biến đổi, và cách trực tiếp nhất là tính tích phân.||To generate new pairs we need ways of carrying out the transformation, and the most direct one is to evaluate the integral.⟧",
                 "⟦Hàm bằng 0 ở nhiều đoạn và đơn giản ở đoạn còn lại thì tích phân làm được; các hàm khác cần mẹo (hoàn thiện bình phương, tích phân đường, chuỗi giới hạn).||A function that is zero over some range and simple elsewhere can be integrated; others need tricks (completing the square, contour integrals, limit sequences).⟧"),
            preview=["⟦Bản đồ các cách lấy biến đổi||A map of the ways to obtain a transform⟧", "⟦Hàm chữ nhật, bậc thang, xung||Rectangles, staircases, impulses⟧", "⟦$e^{-|x|}$, Gauss, $1/x$, $\\text{sgn}\\,x$||$e^{-|x|}$, the Gaussian, $1/x$, $\\text{sgn}\\,x$⟧"],
            slides=[
                ("⟦Vì sao cần chương này||Why this chapter⟧",
                 "<p>⟦Nhiều chuỗi lập luận dùng biến đổi Fourier không cần biết cặp cụ thể nào, nhưng làm lập luận tổng quát với một ví dụ trong đầu thường là cách bảo hiểm trước bất ngờ (Bracewell, tr. 136). Các cặp đã dùng để minh họa định lý đều được nêu không chứng minh, nên chưa giúp khi cần tạo cặp mới. Chương này xét các cách thực hiện phép biến đổi.||"
                 "Many chains of argument in which the Fourier transform matters need no particular transform pair, yet carrying out a general argument with a special case in mind often serves as insurance against surprises (Bracewell, p. 136). The pairs used to illustrate the theorems were all asserted without derivation, which does not help when new pairs are needed. This chapter considers ways of carrying out the transformation.⟧</p>"),
                ("⟦Bốn con đường||Four routes⟧",
                 OL(["⟦Tính tích phân $\\int f(x)e^{-i2\\pi xs}dx$ trực tiếp (dạng đóng).||Evaluate the integral $\\int f(x)e^{-i2\\pi xs}dx$ directly (closed form).⟧",
                     "⟦Biến đổi số: cộng thay tích phân, gồm cả chương trình \"chậm\" ngắn và FFT (chương 11).||Numerical transformation: a sum instead of an integral, including a short \"slow\" program and the FFT (chapter 11).⟧",
                     "⟦Sinh từ các định lý cơ bản bắt đầu từ vài cặp đã biết.||Generation from the basic theorems, starting from a few known pairs.⟧",
                     "⟦Tra bảng.||Extraction from tables.⟧"]) + "<p>⟦Sách chú ý rằng vài lớp hàm sẽ không bao giờ đến được bằng định lý, nhưng nhiều hàm khả thi về vật lý thì đến được (tr. 137).||The book notes that some classes of function will never be stumbled on by theorems, yet a variety of physically feasible functions prove accessible (p. 137).⟧</p>"),
                ("⟦Xung chữ nhật||The rectangle function⟧",
                 "<p>⟦Khi $f(x)=\\Pi(x)$, biến đổi chỉ là tích phân của cosin trên $[-\\tfrac12,\\tfrac12]$ (Bracewell, tr. 137):||When $f(x)=\\Pi(x)$ the transform is just the integral of a cosine over $[-\\tfrac12,\\tfrac12]$ (Bracewell, p. 137):⟧</p>"
                 + F("⟦Tích phân xung chữ nhật||Rectangle integral⟧", r"\int_{-1/2}^{1/2}\cos 2\pi xs\,dx=\frac{\sin\pi s}{\pi s}=\operatorname{sinc}s")
                 + "<p>⟦Tại $s=0.3$: {{cf_rect}} bằng cả tích phân số và công thức.||At $s=0.3$: {{cf_rect}} by both numerical integration and the formula.⟧</p>"),
                ("⟦Hàm bậc thang: tổng các xung chữ nhật||Staircase functions: sums of rectangles⟧",
                 "<p>⟦Nếu $f$ khác 0 trên nhiều đoạn và hằng trong mỗi đoạn thì cũng tích phân được. Với $f(x)=\\sum a_n\\Pi\\!\\left(\\frac{x-b_n}{c_n}\\right)$, dịch và tỉ lệ cho $F(s)=\\sum a_nc_ne^{-i2\\pi b_ns}\\,\\text{sinc}\\,c_ns$ (tr. 137). Những hàm này gồm cả bậc thang và tín hiệu điện báo Morse, và mô phỏng được mọi kiểu biến thiên với độ chính xác tùy ý (tr. 138). Số đo với ba xung $(a,b,c)=(1,0,2),(0.5,3,1),(-1,-2,1)$ tại $s=0.3$: phần thực {{cf_re}}, phần ảo {{cf_im}}.||"
                 "If $f$ is nonzero on several segments and constant within each, integration in closed form is again possible. For $f(x)=\\sum a_n\\Pi\\!\\left(\\frac{x-b_n}{c_n}\\right)$, shift and similarity give $F(s)=\\sum a_nc_ne^{-i2\\pi b_ns}\\,\\text{sinc}\\,c_ns$ (p. 137). Such functions include staircases and Morse-code signals and can simulate any kind of variation as closely as desired (p. 138). Measured with three pulses $(a,b,c)=(1,0,2),(0.5,3,1),(-1,-2,1)$ at $s=0.3$: real part {{cf_re}}, imaginary part {{cf_im}}.⟧</p>"
                 + F("⟦Biến đổi tổng xung||Transform of a sum of pulses⟧", r"F(s)=\sum_n a_nc_n\,e^{-i2\pi b_ns}\operatorname{sinc}c_ns")),
                ("⟦Tập xung: sàng lọc cho ra tổng mũ||A set of impulses: sifting gives a sum of exponentials⟧",
                 "<p>⟦Trường hợp còn đơn giản hơn là $f$ bằng 0 hầu khắp nơi: $f(x)=\\sum a_n\\delta(x-b_n)$. Chỉ giá trị $a_n\\exp(-i2\\pi xs)$ tại $x=b_n$ có ý nghĩa, và theo định lý sàng lọc $F(s)=\\sum a_ne^{-i2\\pi b_ns}$ (tr. 138). Số đo: mô phỏng ba xung $(a,b)=(2,-1),(-1,0.5),(0.5,2)$ bằng chữ nhật hẹp $10^{-3}$ cho độ lớn {{cf_imp}} tại $s=0.3$, đúng tổng mũ.||"
                 "An even simpler case arises if $f$ is zero almost everywhere: $f(x)=\\sum a_n\\delta(x-b_n)$. Only the values of $a_n\\exp(-i2\\pi xs)$ at $x=b_n$ matter, and by the sifting theorem $F(s)=\\sum a_ne^{-i2\\pi b_ns}$ (p. 138). Measured: simulating three impulses $(a,b)=(2,-1),(-1,0.5),(0.5,2)$ by narrow rectangles of width $10^{-3}$ gives magnitude {{cf_imp}} at $s=0.3$, exactly the exponential sum.⟧</p>"),
                ("⟦Khi không có quy tắc chung: ví dụ $e^{-|x|}$||When there is no general rule: the example $e^{-|x|}$⟧",
                 "<p>⟦Nếu $f$ có dạng hàm đặc biệt thì có thể tích phân được nhưng không có quy tắc chung (tr. 138). Với $f=e^{-|x|}$, $F(s)=2\\int_0^\\infty e^{-x}\\cos2\\pi xs\\,dx=2\\,\\text{Re}\\,\\dfrac{1}{1+i2\\pi s}$:||"
                 "If $f$ has some special functional form it may be possible to integrate, but no general rules can be given (p. 138). For $f=e^{-|x|}$, $F(s)=2\\int_0^\\infty e^{-x}\\cos2\\pi xs\\,dx=2\\,\\text{Re}\\,\\dfrac{1}{1+i2\\pi s}$:⟧</p>"
                 + F("⟦Biến đổi của $e^{-|x|}$||Transform of $e^{-|x|}$⟧", r"F(s)=\frac{2}{1+4\pi^2s^2}")
                 + "<p>⟦Tại $s=0.3$: {{cf_exp}} theo tích phân số, theo phần thực và theo công thức.||At $s=0.3$: {{cf_exp}} by numerical integration, by the real part and by the formula.⟧</p>"),
                ("⟦Gauss: hoàn thiện bình phương||The Gaussian: completing the square⟧",
                 "<p>⟦Với $f=e^{-\\pi x^2}$, viết $\\pi x^2+i2\\pi xs=\\pi(x+is)^2+\\pi s^2$, rút $e^{-\\pi s^2}$ ra ngoài, rồi dùng kết quả đã biết rằng tích phân vô hạn của $\\exp(-\\pi u^2)$ bằng 1 (tr. 139). Kết quả $e^{-\\pi s^2}$ = {{cf_gauss}} tại $s=0.3$, khớp tích phân số phức.||"
                 "For $f=e^{-\\pi x^2}$ write $\\pi x^2+i2\\pi xs=\\pi(x+is)^2+\\pi s^2$, take $e^{-\\pi s^2}$ outside, and use the known result that the infinite integral of $\\exp(-\\pi u^2)$ is unity (p. 139). The result $e^{-\\pi s^2}$ = {{cf_gauss}} at $s=0.3$, matching the complex numerical integral.⟧</p>"),
                ("⟦$1/x$: tích phân đường bán nguyệt||$1/x$: a semicircular contour integral⟧",
                 "<p>⟦Độ gián đoạn vô hạn ở gốc làm tích phân Fourier chuẩn phân kỳ, nên xét giới hạn với đoạn $(-\\epsilon,\\epsilon)$ bị bỏ. Ta dùng đường bán nguyệt bán kính $R$ có chỗ lõm nhỏ bán kính $\\epsilon$ tại gốc, không bao điểm cực nào nên tích phân đường bằng 0. Khi $R\\to\\infty$ tích phân thứ tư triệt tiêu, còn tích phân trên cung nhỏ bằng $\\pm i\\pi$ tùy dấu $s$; kết quả trong giới hạn là (tr. 139):||"
                 "The infinite discontinuity at the origin makes the standard Fourier integral diverge, so consider the limit with the interval $(-\\epsilon,\\epsilon)$ removed. Take a semicircle of radius $R$ with a small indentation of radius $\\epsilon$ at the origin; no poles are enclosed so the contour integral is zero. As $R\\to\\infty$ the fourth integral vanishes and the small arc contributes $\\pm i\\pi$ according to the sign of $s$; the pair in the limit is (p. 139):⟧</p>"
                 + F("⟦Cặp trong giới hạn||Pair in the limit⟧", r"\frac1x\ \supset\ -i\pi\,\operatorname{sgn}s")
                 + "<p>⟦Số đo: cắt ở $|x|\\le10^4$ thì phần ảo của $\\int\\sin$ là {{cf_1x}} tại $s=0.3$, đúng $-\\pi$.||Measured: cutting at $|x|\\le10^4$ the imaginary part is {{cf_1x}} at $s=0.3$, i.e. $-\\pi$.⟧</p>"),
                ("⟦$\\text{sgn}\\,x$: dãy hàm tiến về giới hạn||$\\text{sgn}\\,x$: a sequence approaching the limit⟧",
                 "<p>⟦Đây là ví dụ trước ngược lại: tích phân Fourier không tồn tại theo nghĩa chuẩn vì hàm không khả tích tuyệt đối. Xét dãy $\\exp(-\\tau|x|)\\text{sgn}\\,x$ khi $\\tau\\to0$; biến đổi là $\\dfrac1{\\tau+i2\\pi s}-\\dfrac1{\\tau-i2\\pi s}$, tiến về $1/i\\pi s$ (tr. 140). Số đo với $\\tau=10^{-3}$, $s=0.3$: khác giới hạn chỉ {{cf_sgn}}.||"
                 "This is the previous example in reverse: the Fourier integral fails to exist in the standard sense because the function is not absolutely integrable. Consider the sequence $\\exp(-\\tau|x|)\\text{sgn}\\,x$ as $\\tau\\to0$; the transform is $\\dfrac1{\\tau+i2\\pi s}-\\dfrac1{\\tau-i2\\pi s}$, tending to $1/i\\pi s$ (p. 140). Measured with $\\tau=10^{-3}$, $s=0.3$: it differs from the limit by only {{cf_sgn}}.⟧</p>"
                 + F("⟦Cặp trong giới hạn||Pair in the limit⟧", r"\operatorname{sgn}x\ \supset\ \frac{1}{i\pi s}")),
                ("⟦Tự kiểm tra phần 1||Self-check, part 1⟧",
                 UL(["⟦Biến đổi của $\\sum a_n\\Pi[(x-b_n)/c_n]$ là gì?||What is the transform of $\\sum a_n\\Pi[(x-b_n)/c_n]$?⟧",
                     "⟦Vì sao $\\text{sgn}\\,x$ cần dãy giới hạn?||Why does $\\text{sgn}\\,x$ need a limit sequence?⟧",
                     "⟦Bước hoàn thiện bình phương cho Gauss cần biết kết quả gì?||What result is needed after completing the square for the Gaussian?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: $\\sum a_nc_ne^{-i2\\pi b_ns}\\text{sinc}\\,c_ns$; vì không khả tích tuyệt đối; tích phân của $e^{-\\pi u^2}$ bằng 1.||Hints: $\\sum a_nc_ne^{-i2\\pi b_ns}\\text{sinc}\\,c_ns$; because it is not absolutely integrable; the integral of $e^{-\\pi u^2}$ is 1.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 2
        dict(
            title="⟦Biến đổi số và giới hạn của dữ liệu thật||Numerical transformation and the limits of real data⟧",
            scr=("⟦Dữ liệu đo được cho ở các giá trị rời rạc của biến độc lập, trên một khoảng hữu hạn, và có sai số.||Measured data are given at discrete values of the independent variable, over a finite range, and contain errors.⟧",
                 "⟦Những hạn chế đó quyết định tần số cao nhất, bước tần số nhỏ nhất và số chữ số thập phân có ý nghĩa.||Those limitations fix the highest frequency, the smallest frequency step and the number of meaningful decimals.⟧",
                 "⟦Bậc tự do bằng $2X/\\Delta x$; tần số tối đa $1/2\\Delta x$; bước $\\Delta s=1/2X$.||The degrees of freedom are $2X/\\Delta x$; the maximum frequency is $1/2\\Delta x$; the step is $\\Delta s=1/2X$.⟧"),
            preview=["⟦Giới hạn: tần số tối đa, bước tần số, bậc tự do||Limits: maximum frequency, frequency step, degrees of freedom⟧", "⟦Chương trình biến đổi Fourier chậm||The slow Fourier transform program⟧", "⟦Các ví dụ số và sai số chồng phổ||Numerical examples and the aliasing error⟧"],
            slides=[
                ("⟦Ba hạn chế của dữ liệu||Three limitations of data⟧",
                 UL(["⟦Dữ liệu cách nhau $\\Delta x$: thành phần Fourier có chu kỳ ngắn hơn $2\\Delta x$ hầu như không có thông tin, nên chỉ cần tính tới khoảng $(2\\Delta x)^{-1}$.||Data are spaced $\\Delta x$: Fourier components with periods shorter than $2\\Delta x$ hardly carry information, so computing beyond about $(2\\Delta x)^{-1}$ is unnecessary.⟧",
                     "⟦Dữ liệu chỉ cho trong $-X<x<X$: không cần tính $F(s)$ ở các điểm gần nhau hơn $\\Delta s=(2X)^{-1}$.||Data are given only for $-X<x<X$: $F(s)$ need not be calculated at points closer than $\\Delta s=(2X)^{-1}$.⟧",
                     "⟦Dữ liệu có sai số: phổ công suất của sai số đặt giới hạn cho số chữ số thập phân có ý nghĩa.||Data contain errors: the power spectrum of the error sets a limit on the meaningful decimals.⟧"])
                 + "<p>⟦Đó là Bracewell, tr. 140 đến 141. Nếu chi tiết mịn của $F(s)$ cần bước nhỏ hơn $(2X)^{-1}$ thì phải mở rộng đo $f(x)$ vượt quá $x=X$.||That is Bracewell, pp. 140 to 141. If fine detail in $F(s)$ requires a finer interval than $(2X)^{-1}$, measurements of $f(x)$ must extend beyond $x=X$.⟧</p>"),
                ("⟦Bậc tự do||Degrees of freedom⟧",
                 "<p>⟦Hàm $f(x)$ lập bảng ở khoảng $\\Delta x$ trên đoạn $2X$ có $2X/\\Delta x$ bậc tự do, và số này phải tương đương với số dữ liệu tính cho biến đổi (tr. 140; chương 10 và 14 khai thác kỹ). Ví dụ $\\Delta x=1$, $X=6$: {{dof}} bậc tự do, tần số tối đa {{fmax}}, bước tần số {{dsmin}}.||"
                 "A function $f(x)$ tabulated at interval $\\Delta x$ over a range $2X$ possesses $2X/\\Delta x$ degrees of freedom, which should be comparable with the number of data computed for the transform (p. 140; chapters 10 and 14 explore it in detail). Example $\\Delta x=1$, $X=6$: {{dof}} degrees of freedom, maximum frequency {{fmax}}, frequency step {{dsmin}}.⟧</p>"
                 + F("⟦Giới hạn dữ liệu||Data limits⟧", r"s_{\max}=\frac{1}{2\Delta x},\qquad \Delta s=\frac{1}{2X},\qquad N_{\rm dof}=\frac{2X}{\Delta x}")),
                ("⟦Tổng hữu hạn thay tích phân||A finite sum replaces the integral⟧",
                 "<p>⟦Giả sử $f(x)$ biểu diễn bằng giá trị tại $x=n$, $n=-X\\ldots X$. Trước khi biến đổi ta cần giả định về hành vi ngoài khoảng đo: giả sử $f=0$ khi $|x|>X$. Khi đó tổng $\\sum_{-X}^{X}f(n)e^{-i2\\pi sn}$ xấp xỉ $F(s)$; phần thực và ảo cho hai tổng riêng $C=\\sum f(n)\\cos2\\pi sn$ và $S=\\sum f(n)\\sin2\\pi sn$ (tr. 141), với $F=C-iS$. Mỗi giá trị $s$ cần $2X+1$ số hạng nên tính khá nhiều, nhờ đối xứng có thể chỉ cộng từ 0 tới $X$.||"
                 "Let $f(x)$ be represented by values at $x=n$, $n=-X\\ldots X$. Before transforming we must assume how $f$ behaves outside the range: suppose $f=0$ where $|x|>X$. Then $\\sum_{-X}^{X}f(n)e^{-i2\\pi sn}$ approximates $F(s)$; real and imaginary parts give two separate sums $C=\\sum f(n)\\cos2\\pi sn$ and $S=\\sum f(n)\\sin2\\pi sn$ (p. 141), with $F=C-iS$. Each value of $s$ needs $2X+1$ terms, which is a lot of computing; by symmetry summation from 0 to $X$ suffices.⟧</p>"),
                ("⟦Cooley và Tukey, Lanczos và Gauss||Cooley and Tukey, Lanczos and Gauss⟧",
                 "<p>⟦Giữa những năm sáu mươi, cộng đồng xử lý tín hiệu bị ảnh hưởng sâu sắc bởi Cooley và Tukey (1965): chia tập dữ liệu làm hai, biến đổi riêng rồi ghép, công việc giảm gần một nửa, và chia nhỏ tiếp còn tốt hơn. Lanczos đã công bố việc này năm 1942, và Gauss dùng ý đó năm 1805 khi phân tích số liệu sao chổi. Sau vài năm, tên \"thuật toán Cooley-Tukey\" được đổi thành FFT (tr. 141).||"
                 "In the mid-sixties the signal processing community was profoundly influenced by Cooley and Tukey (1965): divide the data set in two, take the separate transforms and combine them, and the work is roughly halved; further subdivision is better still. Lanczos had published this in 1942, and Gauss used the idea in 1805 for numerical analysis of cometary data. After some years the name \"Cooley-Tukey algorithm\" gave way to Fast Fourier Transform (p. 141).⟧</p>"),
                ("⟦Một lệnh cho FFT, nhưng \"hộp đen\" cần hiểu||One command for the FFT, but the black box needs understanding⟧",
                 "<p>⟦Một câu lệnh MATLAB $F=\\text{fft}(f)$ cho biến đổi phức của một dãy ngay lập tức, dù số phần tử có ước số, là số nguyên tố hay lũy thừa của 2 (tr. 142). Notebook kiểm cả trường hợp chiều dài 13 (nguyên tố): FFT so với tổng chậm lệch tối đa {{fft_dev}}. Sách cảnh báo rằng không thể tiếp cận rương hộp đen một cách an toàn nếu không hiểu bên trong; nhiều sinh viên chạy gói FFT quá sớm rồi thắc mắc vì dữ liệu chữ nhật không ra hình sinc như mong đợi (tr. 142).||"
                 "The single MATLAB statement $F=\\text{fft}(f)$ generates the complex transform of a sequence virtually instantly, whether the number of elements has factors, is prime or is a power of 2 (p. 142). The notebook checks a prime length of 13: the FFT differs from the slow sum by at most {{fft_dev}}. The book warns that the canned black box cannot safely be approached without understanding its content; many students run an FFT package prematurely and are perplexed when rectangle data do not give the expected sinc shape or amplitude (p. 142).⟧</p>"),
                ("⟦Vì sao vẫn dùng biến đổi \"chậm\"||Why the \"slow\" transform is still used⟧",
                 UL(["⟦Tốc độ máy tính tăng làm tổng trực tiếp đủ nhanh cho nhiều việc.||Faster computers make the direct sum fast enough for many purposes.⟧",
                     "⟦Sinh viên làm số trước khi gặp các chi tiết tinh vi của thuật toán nhanh.||Students can do numerical work before confronting the awkward subtleties of the fast algorithms.⟧",
                     "⟦Kiểm các mục trong Từ điển hình ảnh và làm quen định lý.||Confirming entries in the Pictorial Dictionary and gaining experience with theorems.⟧",
                     "⟦Bắt lỗi dấu hoặc hệ số $2$ hay $\\pi$ khi làm đại số bằng tay, nhanh hơn lặp lại suy dẫn cẩn thận.||Catching sign errors or factors of $2$ or $\\pi$ in hand algebra faster than by careful repetition of a derivation.⟧"])
                 + "<p>⟦Theo Bracewell, tr. 142. Biến đổi Hartley (chương 12) cũng đạt mọi mục đích và cho ra kết quả thực với dữ liệu thực.||Per Bracewell, p. 142. The Hartley transform (chapter 12) also achieves all these purposes and gives real output from real input.⟧</p>"),
                ("⟦Chương trình biến đổi chậm||The slow Fourier transform program⟧",
                 "<p>⟦Cho $f(x)$ tại các số nguyên $x=-X\\ldots X$ (đổi thang nếu cần). Vì phần thực và ảo không rơi vào $s$ nguyên, dùng chỉ số $k$ chạy 0 tới $K$ với $s=k/2K$; tần số tối đa 0.5. Với mỗi $k$, cộng $f(x)\\cos(2\\pi sx)$ và $f(x)\\sin(2\\pi sx)$ trên mọi $x$ (tr. 142 đến 143). Chỉ cần $k\\ge0$ vì với $k$ âm biến đổi là liên hợp phức (hình dạng \"nửa thời gian\" so với FFT). Kiểm thô: $R(0)$ bằng tổng dữ liệu và $I(0)=0$.||"
                 "Let $f(x)$ be given at integer $x=-X\\ldots X$ (rescale if needed). Since the real and imaginary parts do not come at integer $s$, an integer index $k$ from 0 to $K$ is used with $s=k/2K$; the maximum frequency is 0.5. For each $k$, sum $f(x)\\cos(2\\pi sx)$ and $f(x)\\sin(2\\pi sx)$ over all $x$ (pp. 142 to 143). Only $k\\ge0$ is needed since for negative $k$ the transform is the complex conjugate (about half the running time of the standard FFT). Gross check: $R(0)$ equals the sum of the data and $I(0)=0$.⟧</p>"
                 + F("⟦Chương trình chậm||Slow program⟧", r"R(k)=\sum_{x=-X}^{X}f(x)\cos 2\pi sx,\quad I(k)=\sum_{x=-X}^{X}f(x)\sin 2\pi sx,\quad s=\frac{k}{2K}")),
                ("⟦Chọn $K$: khoảng cách tới hạn, mịn hơn, dải hẹp||Choosing $K$: critical spacing, finer, and a narrow band⟧",
                 "<p>⟦Với $K=X$ ta được $X+1$ giá trị $R$ và $X$ giá trị $I$ (không đếm $I(0)=0$), tổng bằng đúng số hằng độc lập $2X+1$ mà dữ liệu biện minh; bước $1/2X$ gọi là khoảng cách tới hạn. Số đo: từ $R,I$ này dựng lại dữ liệu ban đầu lệch {{recon_dev}}. $K=4X$ chèn thêm điểm nội suy làm đồ thị mịn hơn mà không thêm thông tin; $k$ chạy 0 tới $X/2$ thì bước lớn gấp đôi, hợp cho gỡ lỗi. Cho $k$ từ $5X$ tới $7X$ với $K=12X$ ta soi dải quanh $s=0.25$ với độ phân giải gấp 12 lần tới hạn ($\\Delta s=1/24X$); sự linh hoạt này các thuật toán nhanh chuẩn không có (tr. 143). Số đo: {{zoom_pts}} điểm tại bước {{zoom_ds}}, lệch so với FFT đệm 0 chỉ {{zoom_dev}}.||"
                 "With $K=X$ we get $X+1$ values of $R$ and $X$ values of $I$ (not counting $I(0)=0$), exactly the $2X+1$ independent constants justified by the data; the spacing $1/2X$ is called the critical spacing. Measured: reconstructing the data from these $R,I$ deviates by {{recon_dev}}. $K=4X$ adds interleaved points that make the graph smoother without extra information; letting $k$ run from 0 to $X/2$ doubles the spacing, good for debugging. With $k$ from $5X$ to $7X$ and $K=12X$ one examines a band around $s=0.25$ at 12 times the critical resolution ($\\Delta s=1/24X$); the standard fast algorithms do not offer this flexibility (p. 143). Measured: {{zoom_pts}} points at step {{zoom_ds}}, deviating from a zero-padded FFT by only {{zoom_dev}}.⟧</p>"),
                ("⟦Tự kiểm tra phần 2||Self-check, part 2⟧",
                 UL(["⟦Dữ liệu cách 1 trên đoạn $[-6,6]$: tần số tối đa và bước tần số?||Data spaced 1 over $[-6,6]$: maximum frequency and frequency step?⟧",
                     "⟦Vì sao chọn $K=X$ là đủ để dựng lại dữ liệu?||Why is $K=X$ enough to reconstruct the data?⟧",
                     "⟦Điều gì xảy ra nếu tăng $K$ lên $4X$?||What happens if $K$ is raised to $4X$?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: 0.5 và 1/12; vì $R$ và $I$ cho đúng $2X+1$ hằng độc lập; thêm điểm nội suy mà không thêm thông tin.||Hints: 0.5 and 1/12; because $R$ and $I$ give exactly $2X+1$ independent constants; interleaved points with no extra information.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 3
        dict(
            title="⟦Ví dụ số và sai số chồng phổ||Numerical examples and the aliasing error⟧",
            scr=("⟦Muốn tin chương trình, ta thử với dữ liệu có đáp số biết trước: xung chữ nhật $\\Pi(x/12)$ có biến đổi $12\\,\\text{sinc}\\,12s$.||To trust a program, test it on data with a known answer: the rectangle $\\Pi(x/12)$ has transform $12\\,\\text{sinc}\\,12s$.⟧",
                 "⟦Kết quả có khớp không, và nếu lệch thì lệch vì đâu?||Does the result match, and if not, where does the difference come from?⟧",
                 "⟦Lệch chủ yếu do sự chồng phổ của các bản sao $12\\,\\text{sinc}\\,12(s-n)$, và tăng mật độ dữ liệu làm giảm lệch tương đối.||The difference comes mainly from overlapping replicas $12\\,\\text{sinc}\\,12(s-n)$, and denser data reduce the relative error.⟧"),
            preview=["⟦Ví dụ: 13 giá trị, $K=12$||Example: 13 values, $K=12$⟧", "⟦$K=24$, đệm 0, dữ liệu dày gấp đôi||$K=24$, zero padding, twice as dense data⟧", "⟦Chồng phổ: $R(s)=\\sin12\\pi s\\cot\\pi s$||Aliasing: $R(s)=\\sin12\\pi s\\cot\\pi s$⟧"],
            slides=[
                ("⟦Dữ liệu ví dụ||The example data⟧",
                 "<p>⟦Dữ liệu vào là 13 giá trị $f(x)=\\Pi(x/12)$ tại $x=-6\\ldots6$: 11 giá trị 1 ở giữa và hai giá trị $\\tfrac12$ ở hai đầu (tại chỗ gián đoạn lấy trung bình). Tổng bằng 12 nên $R(0)=12$, đúng $F(0)$. Chọn $K=2X=12$ ta có bước tần số bằng một nửa khoảng cách tới hạn (tr. 144).||"
                 "The input is 13 values of $f(x)=\\Pi(x/12)$ at $x=-6\\ldots6$: eleven ones in the middle and two values of $\\tfrac12$ at the ends (the mean value at the discontinuity). The sum is 12 so $R(0)=12$, equal to $F(0)$. Choosing $K=2X=12$ gives half the critical frequency spacing (p. 144).⟧</p>"),
                ("⟦Kết quả với $K=12$||Result with $K=12$⟧",
                 "<p>⟦Vì $f$ chẵn nên mọi $I(k)$ bằng không. Các giá trị $R(k)$: $R(1)$ = {{sl_R1}}, $R(3)$ = {{sl_R3}}, $R(5)$ = {{sl_R5}}, $R(11)$ = {{sl_R11}}, còn các $R(k)$ chỉ số chẵn $k\\ge2$ bằng 0 (tr. 144). So với $12\\,\\text{sinc}\\,12s=7.639$ tại $s=1/24$, $R(1)$ lệch {{sl_pct1}} phần trăm.||"
                 "Since $f$ is even, all $I(k)$ vanish. The values of $R(k)$: $R(1)$ = {{sl_R1}}, $R(3)$ = {{sl_R3}}, $R(5)$ = {{sl_R5}}, $R(11)$ = {{sl_R11}}, while the even-index $R(k)$ for $k\\ge2$ are 0 (p. 144). Against $12\\,\\text{sinc}\\,12s=7.639$ at $s=1/24$, $R(1)$ differs by {{sl_pct1}} percent.⟧</p>{{fig:slow_rect}}"),
                ("⟦$K=24$: bước nhỏ một phần tư tới hạn||$K=24$: a quarter of the critical spacing⟧",
                 "<p>⟦Giữ dữ liệu như cũ và chọn $K=24$: các giá trị tại tần số cũ giữ nguyên, các tần số xen kẽ cho đồ thị mượt hơn (tr. 144). $R(1)$ = {{sl24_1}} và $R(3)$ = {{sl24_3}} là hai giá trị xen kẽ mới, còn $R(2)$ = {{sl_R1}} trùng $R(1)$ của lần trước ($s=1/24$).||"
                 "Keep the data unchanged and choose $K=24$: values at the earlier frequencies are unchanged, and the interleaved frequencies give a smoother graph (p. 144). $R(1)$ = {{sl24_1}} and $R(3)$ = {{sl24_3}} are the new interleaved values, while $R(2)$ = {{sl_R1}} coincides with $R(1)$ of the previous run ($s=1/24$).⟧</p>"),
                ("⟦Đệm số 0 không đổi biến đổi||Zero padding does not change the transform⟧",
                 "<p>⟦Đổi $X$ thành 12 và đệm dữ liệu gốc thành 25 giá trị bằng số 0 ở hai đầu, giữ $K=24$: các giá trị biến đổi không đổi (tr. 144). Thật vậy, số hạng thêm vào đều bằng 0. Số đo: lệch tối đa giữa hai tính là {{pad_dev}}.||"
                 "Change $X$ to 12 and pad the original data to 25 values with zeros at both ends, keeping $K=24$: the transform values are unchanged (p. 144). Indeed the added terms are all zero. Measured: the maximum difference between the two computations is {{pad_dev}}.⟧</p>"),
                ("⟦Dữ liệu dày gấp đôi: $\\Pi(x/24)$||Twice as dense data: $\\Pi(x/24)$⟧",
                 "<p>⟦Giữ $X=12$ nhưng dùng 25 giá trị bắt đầu và kết thúc bằng $\\tfrac12$, ở giữa 23 số 1 (tương đương $\\Pi(x/24)$, biến đổi $24\\,\\text{sinc}\\,24s$), giữ $K=24$ (tr. 144). Khi đó $R(1)$ = {{sl12_1}}; sai khác với $24\\,\\text{sinc}\\,0.5$ chỉ còn {{sl12_pct}} phần trăm, cải thiện {{sl_ratio}} lần so với ví dụ đầu.||"
                 "Keep $X=12$ but use 25 values starting and finishing with $\\tfrac12$ and 23 ones between (equivalent to $\\Pi(x/24)$, transform $24\\,\\text{sinc}\\,24s$), and keep $K=24$ (p. 144). Then $R(1)$ = {{sl12_1}}; the difference from $24\\,\\text{sinc}\\,0.5$ is only {{sl12_pct}} percent, an improvement by a factor {{sl_ratio}} over the first example.⟧</p>"),
                ("⟦Sai số tuyệt đối không giảm theo $k$||The absolute error does not shrink with $k$⟧",
                 "<p>⟦Bracewell nhắc kiểm rằng sai số tuyệt đối không giảm khi $k$ tăng (tr. 144). Nguyên nhân sẽ rõ ở slide sau: sai số có dạng $\\sin(2\\pi Xs)\\left[\\cot\\pi s-\\frac1{\\pi s}\\right]$, biên độ $|\\cot\\pi s-1/\\pi s|$ không phụ thuộc $X$, chẳng hạn bằng {{env_025}} tại $s=0.25$. Vì thế tăng mật độ dữ liệu làm tín hiệu cao lên $X$ lần còn sai số giữ nguyên biên độ, nên sai số tương đối giảm.||"
                 "Bracewell asks us to verify that the absolute error does not diminish as $k$ increases (p. 144). The reason will be clear on the next slide: the error has the form $\\sin(2\\pi Xs)\\left[\\cot\\pi s-\\frac1{\\pi s}\\right]$, whose envelope $|\\cot\\pi s-1/\\pi s|$ does not depend on $X$, for instance {{env_025}} at $s=0.25$. So denser data make the signal larger in proportion to $X$ while the error keeps its amplitude, hence the relative error falls.⟧</p>"),
                ("⟦Nguồn gốc lệch: chồng phổ các bản sao||The origin of the discrepancy: overlapping replicas⟧",
                 "<p>⟦Cho $k$ chạy tới $2K$ thì $s$ tới 1.0 và $R$ trở lại đúng giá trị tại $s=0$ (tr. 144). Sự lệch so với $12\\,\\text{sinc}\\,12s$ chủ yếu do bản sao $12\\,\\text{sinc}\\,12(s-1)$ chồng lên, và tổng quát giá trị thật của $R$ là $\\sum_n12\\,\\text{sinc}\\,12(s-n)$. Số đo: $R$ tại $s=1$ là {{alias_R}}; tổng cắt $|n|\\le20000$ tại $s=1/24$ là {{alias_sum}}, bằng $R(1)$ {{sl_R1}} ở trên.||"
                 "Letting $k$ run to $2K$ makes $s$ reach 1.0 and $R$ climbs back to the value it had at $s=0$ (p. 144). The discrepancy from $12\\,\\text{sinc}\\,12s$ arises mainly from the overlapping replica $12\\,\\text{sinc}\\,12(s-1)$, and in general the actual value of $R$ is $\\sum_n12\\,\\text{sinc}\\,12(s-n)$. Measured: $R$ at $s=1$ is {{alias_R}}; the sum truncated at $|n|\\le20000$ at $s=1/24$ is {{alias_sum}}, equal to $R(1)$ {{sl_R1}} above.⟧</p>"
                 + F("⟦Bản sao cộng lại||Replicas add up⟧", r"R(s)=\sum_{n=-\infty}^{\infty}12\operatorname{sinc}12(s-n)=\sin 12\pi s\,\cot\pi s")),
                ("⟦Bài học: pha phụ thuộc gốc, công suất thì không||A lesson: phase depends on the origin, power does not⟧",
                 "<p>⟦Với nhiều dạng sóng, việc chọn gốc không quan trọng vì dạng sóng không phụ thuộc thời điểm chọn làm gốc. Phần thực và ảo bị ảnh hưởng nhiều bởi lựa chọn gốc, nên không được cần đến thường xuyên; thay vào đó $R^2+I^2$ là tính chất nội tại của dạng sóng, và pha $\\arctan(I/R)$ chỉ đổi một độ dịch tuyến tính theo tần số khi đổi gốc (tr. 143). Số đo: dời gốc dữ liệu chữ nhật đi 3 đơn vị giữ $R^2+I^2$ ở $s=0.1$ là {{pow_orig}} (không đổi) và thêm pha {{ph_orig}} độ.||"
                 "With many waveforms the choice of origin is unimportant because the wave shape does not depend on what instant is chosen as origin. The real and imaginary parts, heavily affected by the choice of origin, are not needed all that often; instead $R^2+I^2$ is an intrinsic property of the waveform, and choice of origin affects the phase $\\arctan(I/R)$ only by a linear phase shift with frequency (p. 143). Measured: moving the origin of the rectangle data by 3 units keeps $R^2+I^2$ at $s=0.1$ equal to {{pow_orig}} (unchanged) and adds phase {{ph_orig}} degrees.⟧</p>"),
                ("⟦Tự kiểm tra phần 3||Self-check, part 3⟧",
                 UL(["⟦Vì sao $R(0)=12$ trong ví dụ?||Why is $R(0)=12$ in the example?⟧",
                     "⟦Đệm số 0 có đổi $F(s)$ không?||Does zero padding change $F(s)$?⟧",
                     "⟦Vì sao dữ liệu dày hơn cải thiện sai số tương đối nhưng không cải thiện biên độ sai số tuyệt đối?||Why does denser data improve the relative error but not the amplitude of the absolute error?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: tổng dữ liệu bằng $F(0)$; không; sai số là chồng phổ có biên độ độc lập $X$.||Hints: the sum of the data equals $F(0)$; no; the error is aliasing with an amplitude independent of $X$.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 4
        dict(
            title="⟦Sinh biến đổi từ các định lý||Generating transforms from the theorems⟧",
            scr=("⟦Chỉ cần vài cặp là ta sinh được cả một từ điển biến đổi bằng định lý.||A few pairs are enough to build a whole dictionary of transforms with theorems.⟧",
                 "⟦Hàm đa giác, hàm chia đoạn tuyến tính hoặc đa thức có thể quy về xung bằng cách đạo hàm liên tiếp.||Polygonal, piecewise-linear or piecewise-polynomial functions can be reduced to impulses by successive differentiation.⟧",
                 "⟦Tích chập với xung và định lý đạo hàm là hai công cụ chính; hằng số tích phân được xác định từ diện tích và ràng buộc khác.||Convolution with impulses and the derivative theorem are the two main tools; integration constants are fixed by the area and other constraints.⟧"),
            preview=["⟦Tích chập với xung: hàm đa giác||Convolution with impulses: polygonal functions⟧", "⟦Đạo hàm liên tiếp tới xung||Continued differentiation down to impulses⟧", "⟦Xung parabol $(1-x^2)\\Pi(x/2)$||The parabolic pulse $(1-x^2)\\Pi(x/2)$⟧"],
            slides=[
                ("⟦Nguyên tắc||The principle⟧",
                 "<p>⟦Nhiều hàm, nhất là trong lý thuyết, biến đổi được nếu nhận ra một tính chất cho phép dùng một định lý (Bracewell, tr. 145). Định lý thường có dạng \"nếu $f$ và $F$ là cặp thì $g$ và $G$ cũng vậy\", nên từ cặp đã biết sinh ra cặp mới.||A wide variety of functions, especially in theoretical work, can be transformed if some property permits a simplifying application of a theorem (Bracewell, p. 145). Many theorems take the form \"if $f$ and $F$ are a pair then $g$ and $G$ are also\", so from a known pair new ones are generated.⟧</p>"),
                ("⟦Hàm đa giác = tam giác * tập xung||A polygonal function = triangle * set of impulses⟧",
                 "<p>⟦Nếu nhận ra hàm đa giác là tích chập của hàm tam giác và một tập xung, ta xử lý xung như trên rồi nhân với biến đổi của tam giác (hình 7.1, tr. 145):||If we perceive that a polygonal function is the convolution of the triangle function and a set of impulses, we handle the impulses as above and multiply by the transform of the triangle (Fig. 7.1, p. 145):⟧</p>"
                 + F("⟦Đa giác||Polygon⟧", r"\Lambda(x)*\sum A_n\,\delta(x-x_n)\ \supset\ \operatorname{sinc}^2s\ \sum A_n\,e^{-i2\pi x_ns}")),
                ("⟦Xung hình thang||The trapezoidal pulse⟧",
                 "<p>⟦Ví dụ: $\\Lambda(x)*\\mu(x)$, với $\\mu(x)=\\tfrac12\\delta(x+\\tfrac12)+\\tfrac12\\delta(x-\\tfrac12)$, là xung hình thang có biến đổi $\\text{sinc}^2s\\cos\\pi s$ (tr. 145). Tại $s=0.3$ tích phân số và công thức đều cho {{th_trap}}.||"
                 "Example: $\\Lambda(x)*\\mu(x)$, with $\\mu(x)=\\tfrac12\\delta(x+\\tfrac12)+\\tfrac12\\delta(x-\\tfrac12)$, is the trapezoidal pulse with transform $\\text{sinc}^2s\\cos\\pi s$ (p. 145). At $s=0.3$ numerical integration and the formula both give {{th_trap}}.⟧</p>"),
                ("⟦Đạo hàm liên tiếp cho hàm đoạn tuyến tính||Continued differentiation for segmentally linear functions⟧",
                 "<p>⟦Có một cách dùng đặc biệt của định lý đạo hàm hay dùng cho dạng sóng chuyển mạch. Với hàm đoạn tuyến tính, đạo hàm bậc nhất có chứa xung; ta tách xung, đạo hàm lần nữa (hình 7.2, tr. 146), và chỉ còn tập xung $\\sum C_n\\delta(x-c_n)$. Nếu đạo hàm bậc nhất còn chứa $\\sum B_n\\delta(x-b_n)$ và hàm gốc chứa $\\sum A_n\\delta(x-a_n)$ thì (tr. 146):||"
                 "There is a special application of the derivative theorem widely used for switching waveforms. For a segmentally linear function the first derivative contains impulses; we remove the impulse and differentiate again (Fig. 7.2, p. 146), leaving only a set of impulses $\\sum C_n\\delta(x-c_n)$. If the first derivative contains a further set $\\sum B_n\\delta(x-b_n)$ and the original contains $\\sum A_n\\delta(x-a_n)$ then (p. 146):⟧</p>"
                 + F("⟦Quy về xung||Reduction to impulses⟧", r"(i2\pi s)F(s)=(i2\pi s)\sum A_ne^{-i2\pi a_ns}+\sum B_ne^{-i2\pi b_ns}+\frac{1}{i2\pi s}\ \sum C_ne^{-i2\pi c_ns}\cdots")),
                ("⟦Tam giác bằng hai lần đạo hàm||The triangle by two differentiations⟧",
                 "<p>⟦Thí dụ đơn giản nhất: $\\Lambda''(x)=\\delta(x+1)-2\\delta(x)+\\delta(x-1)$, biến đổi $2\\cos2\\pi s-2=-4\\sin^2\\pi s$. Chia cho $(i2\\pi s)^2$ cho $\\text{sinc}^2s$ đúng như biết. Số đo tại $s=0.3$: lệch {{th_tri_dev}} so với $\\text{sinc}^2(0.3)$.||"
                 "The simplest example: $\\Lambda''(x)=\\delta(x+1)-2\\delta(x)+\\delta(x-1)$, with transform $2\\cos2\\pi s-2=-4\\sin^2\\pi s$. Dividing by $(i2\\pi s)^2$ gives $\\text{sinc}^2s$, as known. Measured at $s=0.3$: it deviates by {{th_tri_dev}} from $\\text{sinc}^2(0.3)$.⟧</p>"),
                ("⟦Xung parabol: đạo hàm hai lần||The parabolic pulse: two differentiations⟧",
                 "<p>⟦Xét $f(x)=(1-x^2)\\Pi(x/2)$. Đạo hàm một lần cho $-2x\\,\\Pi(x/2)$ (không có xung vì $f$ liên tục tại $\\pm1$, do $f(\\pm1)=0$). Đạo hàm lần hai cho $2\\delta(x+1)-2\\Pi(x/2)+2\\delta(x-1)$, có biến đổi $4\\cos2\\pi s-4\\,\\text{sinc}\\,2s$ (tr. 146 đến 147). Tại $s=0.3$ vế này là {{th_d2}}; nhân $F(0.3)$ tính bằng tích phân với $(i2\\pi s)^2$ cho cùng số.||"
                 "Consider $f(x)=(1-x^2)\\Pi(x/2)$. The first derivative is $-2x\\,\\Pi(x/2)$ (no impulses since $f$ is continuous at $\\pm1$, as $f(\\pm1)=0$). The second derivative is $2\\delta(x+1)-2\\Pi(x/2)+2\\delta(x-1)$, with transform $4\\cos2\\pi s-4\\,\\text{sinc}\\,2s$ (pp. 146 to 147). At $s=0.3$ this side is {{th_d2}}; multiplying $F(0.3)$ computed by integration by $(i2\\pi s)^2$ gives the same number.⟧</p>"),
                ("⟦Hằng số tích phân||The integration constants⟧",
                 "<p>⟦Chia cho $(i2\\pi s)^2$ ta được $F(s)=\\dfrac{4\\cos2\\pi s-4\\,\\text{sinc}\\,2s}{(i2\\pi s)^2}+K_1\\delta(s)+K_2\\delta'(s)$, với $K_1$ và $K_2$ là hằng số tích phân, vì có thể cộng hằng số hoặc dốc tuyến tính vào $f$ mà không đổi đạo hàm bậc hai. Tích phân xung parabol cho thấy không có hằng số cộng hay dốc, nên $K_1=K_2=0$ (tr. 147):||"
                 "Dividing by $(i2\\pi s)^2$ gives $F(s)=\\dfrac{4\\cos2\\pi s-4\\,\\text{sinc}\\,2s}{(i2\\pi s)^2}+K_1\\delta(s)+K_2\\delta'(s)$ with $K_1$ and $K_2$ integration constants, since a constant or a linear ramp could be added to $f$ without changing the second derivative. Integration of the given pulse shows no additive constant or ramp, so $K_1=K_2=0$ (p. 147):⟧</p>"
                 + F("⟦Biến đổi xung parabol||Transform of the parabolic pulse⟧", r"F(s)=\frac{\sin2\pi s-2\pi s\cos2\pi s}{2\pi^3s^3}")
                 + "<p>⟦Tại $s=0.3$: {{th_par}}. Giới hạn $s\\to0$ là {{th_par0}}, bằng diện tích $\\int(1-x^2)dx=\\tfrac43$.||At $s=0.3$: {{th_par}}. The limit $s\\to0$ is {{th_par0}}, equal to the area $\\int(1-x^2)dx=\\tfrac43$.⟧</p>"),
                ("⟦Đơn giản hóa: khi nào áp dụng cách nào||Which technique when⟧",
                 TBL(["⟦Hàm||Function⟧", "⟦Cách||Technique⟧"],
                     [["⟦Nhiều đoạn hằng||Piecewise constant⟧", "⟦Tổng chữ nhật, tr. 137||Sum of rectangles, p. 137⟧"], ["⟦Tập xung||Set of impulses⟧", "⟦Sàng lọc, tr. 138||Sifting, p. 138⟧"], ["⟦Đa giác||Polygon⟧", "⟦Tam giác * xung, tr. 145||Triangle * impulses, p. 145⟧"],
                      ["⟦Đoạn tuyến tính hoặc đa thức||Piecewise linear or polynomial⟧", "⟦Đạo hàm liên tiếp, tr. 145 đến 147||Continued differentiation, pp. 145 to 147⟧"], ["⟦Gauss, mũ||Gaussian, exponential⟧", "⟦Hoàn thiện bình phương, tr. 139||Completing the square, p. 139⟧"], ["⟦Gián đoạn vô hạn||Infinite discontinuity⟧", "⟦Tích phân đường hoặc dãy giới hạn, tr. 139 đến 140||Contour integral or limit sequence, pp. 139 to 140⟧"]])),
                ("⟦Tự kiểm tra phần 4||Self-check, part 4⟧",
                 UL(["⟦Vì sao hàm hình thang có biến đổi $\\text{sinc}^2s\\cos\\pi s$?||Why does the trapezoid have transform $\\text{sinc}^2s\\cos\\pi s$?⟧",
                     "⟦Bao nhiêu lần đạo hàm để quy $(1-x^2)\\Pi(x/2)$ về xung?||How many differentiations reduce $(1-x^2)\\Pi(x/2)$ to impulses?⟧",
                     "⟦Vì sao có thể có hằng số $K_1\\delta(s)$ và $K_2\\delta'(s)$?||Why can there be constants $K_1\\delta(s)$ and $K_2\\delta'(s)$?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: tam giác * hai xung nửa cường độ; hai lần (còn chữ nhật và xung); vì hàm mất một hằng và một dốc khi đạo hàm hai lần.||Hints: triangle * two half-strength impulses; twice (leaving a rectangle and impulses); because the function loses a constant and a slope on twofold differentiation.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 5
        dict(
            title="⟦Đo phổ và bài tập chọn||Measuring spectra and selected problems⟧",
            scr=("⟦Phổ có thể xác định bằng toán từ dạng sóng, nhưng lịch sử đo phổ bắt đầu với Newton và cuốn Opticks năm 1704.||Spectra can be determined mathematically from waveforms, but the history of measuring them begins with Newton and his Opticks of 1704.⟧",
                 "⟦Ngày nay phổ được đo bằng lăng kính, cách tử, giao thoa kế và máy phân tích phổ số.||Today spectra are measured with prisms, gratings, interferometers and digital spectrum analyzers.⟧",
                 "⟦Quang phổ biến đổi Fourier đo tự tương quan của tín hiệu rồi biến đổi để có phổ công suất.||Fourier transform spectroscopy measures the autocorrelation of the signal and transforms it to obtain the power spectrum.⟧"),
            preview=["⟦Máy phân tích phổ vô tuyến||The radio-frequency spectrum analyzer⟧", "⟦Quang phổ biến đổi Fourier (giao thoa kế)||Optical Fourier transform spectroscopy (interferometer)⟧", "⟦Bài tập chọn||Selected problems⟧"],
            slides=[
                ("⟦Từ Newton tới ngày nay||From Newton to today⟧",
                 "<p>⟦Chuỗi sự kiện lịch sử đo phổ bắt đầu với Isaac Newton trong Opticks năm 1704. Phổ vẫn được tạo bởi lăng kính và các thiết bị quang khác, nhất là cách tử nhiễu xạ và giao thoa kế Fabry-Perot (Bracewell, tr. 147).||The historical sequence of measuring spectra begins with Isaac Newton in his Opticks of 1704. Spectra are still produced by prisms and other optical devices, especially diffraction gratings and Fabry-Perot interferometers (Bracewell, p. 147).⟧</p>"),
                ("⟦Máy phân tích phổ vô tuyến||The radio-frequency spectrum analyzer⟧",
                 "<p>⟦Trong vô tuyến, radar, truyền hình và dụng cụ phòng thí nghiệm, máy phân tích phổ hiển thị cường độ theo tần số. Máy thu vô tuyến khi xoay núm chỉnh là một máy phân tích phổ thô sơ. Máy hiện đại lấy mẫu dạng sóng bằng mạch điện thông thường, phân tích phổ nhanh bằng máy tính rồi hiển thị hoặc lưu phổ (tr. 147). Đến 1990 đã có thiết bị lập trình hoàn toàn dựa trên biến đổi Hartley với độ phân giải picô giây (tr. 147).||"
                 "In radio, radar, television and laboratory instruments, spectrum analyzers display signal strength versus frequency. A radio receiver is a primitive spectrum analyzer as the tuning knob is turned. A modern instrument samples the waveform with conventional circuitry, performs fast spectral analysis by computer and displays or stores the spectrum (p. 147). By 1990 fully programmable instrumentation based on the Hartley transform was commercially available with picosecond resolution (p. 147).⟧</p>"),
                ("⟦Dàn lọc tần số cố định||A bank of fixed-frequency filters⟧",
                 "<p>⟦Cách khác là dàn bộ lọc tần số cố định, thực hiện bằng máy tính, như Viện SETI dùng để tìm tín hiệu vô tuyến từ các hành tinh ngoài hệ Mặt Trời trên dải 20 MHz với độ phân giải mịn tới 1 Hz (tr. 147).||An alternative is a bank of fixed-frequency filters, implemented by computer, as at the SETI Institute searching for radio signals from nonsolar planets over a 20 MHz band with resolution as fine as 1 Hz (p. 147).⟧</p>"),
                ("⟦Quang phổ biến đổi Fourier||Optical Fourier transform spectroscopy⟧",
                 "<p>⟦Cách này không nằm trong đường tiến hóa từ mạch điện, và trở nên đặc biệt quan trọng để phát hiện, nhận dạng phân tử qua phổ hồng ngoại (tr. 148). Nếu xác định được tự tương quan thời gian của tín hiệu điện từ $s(t)$ thì biến đổi Fourier cho phổ công suất. Ta chia tín hiệu thành hai chùm để tạo $s(t)s(t+\\tau)$ với độ trễ $\\tau$ thay đổi: một tấm mylar đặt 45 độ cho một chùm đi thẳng và một chùm phản xạ vuông góc, chùm sau đến gương phẳng rồi quay lại. Dời gương ra xa thì thêm độ trễ.||"
                 "This way is not in the line of evolution from electric circuit practice, and is of particular importance for detecting and identifying molecules by their infrared spectra (p. 148). If we can determine the temporal autocorrelation of an electromagnetic signal $s(t)$ then Fourier transformation gives the power spectrum. Split the signal into two beams to form $s(t)s(t+\\tau)$ with variable delay $\\tau$: a mylar film at 45 degrees lets one beam continue straight and reflects the other at a right angle, to a plane mirror and back. Moving the mirror away adds delay.⟧</p>"),
                ("⟦Độ phân giải và dải phủ||Resolution and band covered⟧",
                 "<p>⟦Với độ trễ tối đa $\\tau_{\\max}$ đạt độ rộng phân giải phổ cỡ $1/2\\tau_{\\max}$; dải phổ phủ được tới tần số cao $1/2\\Delta\\tau$, với $\\Delta\\tau$ là bước dời gương (tr. 148); cũng là các giới hạn $\\Delta s=1/2X$ và $s_{\\max}=1/2\\Delta x$ đã gặp. Số đo với hai vạch phổ cường độ bằng nhau, $\\tau_{\\max}=10$ và $\\Delta\\tau=0.1$ (phân giải {{res_lim}}, dải {{band_lim}}): hai vạch cách {{sep_hi}} tách được ({{peaks_res}} cực đại), hai vạch cách {{sep_lo}} không tách được ({{peaks_unres}} cực đại).||"
                 "With a maximum delay $\\tau_{\\max}$ a spectral resolution bandwidth of about $1/2\\tau_{\\max}$ is achieved; the band covered extends to a high frequency $1/2\\Delta\\tau$, where $\\Delta\\tau$ is the mirror step (p. 148); these are the limits $\\Delta s=1/2X$ and $s_{\\max}=1/2\\Delta x$ met earlier. Measured with two lines of equal strength, $\\tau_{\\max}=10$ and $\\Delta\\tau=0.1$ (resolution {{res_lim}}, band {{band_lim}}): lines separated by {{sep_hi}} are resolved ({{peaks_res}} maxima), lines separated by {{sep_lo}} are not ({{peaks_unres}} maximum).⟧</p>{{fig:two_lines}}"),
                ("⟦Chồng phổ trong giao thoa kế||Aliasing in the interferometer⟧",
                 "<p>⟦Vạch phổ vượt quá $1/2\\Delta\\tau$ bị gấp lại về dải dưới. Số đo: một vạch tại 6 với $\\Delta\\tau=0.1$ hiện ở {{alias_peak}}, đúng $1/\\Delta\\tau-6$ tức $10-6$; đây là chính sự chồng phổ đã gặp khi lấy mẫu (module 13).||A line beyond $1/2\\Delta\\tau$ folds back into the lower band. Measured: a line at 6 with $\\Delta\\tau=0.1$ appears at {{alias_peak}}, exactly $1/\\Delta\\tau-6$, i.e. $10-6$; this is the same aliasing met in sampling (module 13).⟧</p>"),
                ("⟦Tự tương quan chẵn, tương quan chéo thì không||The autocorrelogram is even, the cross-correlogram is not⟧",
                 "<p>⟦Chỉ cần độ trễ dương vì tự tương quan là hàm chẵn ($s(t)s(t+\\tau)$ trung bình theo thời gian bằng $s(t)s(t-\\tau)$). Tuy vậy nếu $\\tau$ đổi từ dương sang âm thì gốc của tự tương quan hiện rõ khi máy hơi lệch chỉnh (tr. 148). Nếu dùng phổ đã biết, như của vật đen, đặt mẫu trong suốt vào một chùm thì ghi được tương quan chéo, không chẵn; biến đổi Fourier cho kết quả phức, từ đó suy ra hằng số điện môi và độ dẫn, hoặc chiết suất và hệ số hấp thụ trên toàn dải phổ, giàu thông tin hơn phổ hấp thụ đơn thuần. Với mẫu đục, dùng nó làm gương dịch để có hệ số phản xạ phức (Bell, 1972; tr. 148).||"
                 "Positive delays alone suffice since the autocorrelation is even (the time-averaged $s(t)s(t+\\tau)$ equals that of $s(t)s(t-\\tau)$). But if $\\tau$ is varied from positive to negative the origin of the autocorrelogram is apparent in the presence of small maladjustments (p. 148). If a known spectrum such as a black-body's is used and a transparent sample placed in one beam, a cross-correlogram is recorded, not an even function; Fourier transformation delivers a complex result from which permittivity and conductivity, or refractive index and absorption coefficient, follow over the full spectral range: a richer result than a simple absorption spectrum. An opaque specimen can serve as the moving mirror to obtain the complex reflection coefficient (Bell, 1972; p. 148).⟧</p>"),
                ("⟦Bài tập 1 đến 4: kiểm bằng số||Problems 1 to 4: numerical checks⟧",
                 "<p>⟦Bài 1 (tr. 149): quan hệ chính xác $\\int x^2f\\,dx=-F''(0)/4\\pi^2$ có thể thành cơ sở kiểm số $R(k)$: mômen bậc hai $\\sum x^2f(x)$ phải bằng $-R''(0)/4\\pi^2$. Số đo với $f=e^{-\\pi(n/5)^2}$: $\\sum n^2f$ = {{p1_sum}}, và từ sai phân bậc hai của $R$ ở gốc là {{p1_num}}. Bài 2 và 3: $\\cos\\pi x^2\\supset(\\cos\\pi s^2+\\sin\\pi s^2)/\\sqrt2$ và $e^{i\\pi x^2}\\supset\\sqrt i\\,e^{-i\\pi s^2}$; tại $s=0.3$ giá trị đầu là {{p2_val}}, pha của giá trị sau tại $s=0$ là {{p3_ph}} độ. Bracewell nhắc nghĩ ra cách kiểm bằng số để phát hiện thiếu hệ số $\\sqrt2$.||"
                 "Problem 1 (p. 149): the exact relation $\\int x^2f\\,dx=-F''(0)/4\\pi^2$ can be the basis for a numerical check of $R(k)$: the second moment $\\sum x^2f(x)$ must agree with $-R''(0)/4\\pi^2$. Measured with $f=e^{-\\pi(n/5)^2}$: $\\sum n^2f$ = {{p1_sum}}, and from the second difference of $R$ at the origin {{p1_num}}. Problems 2 and 3: $\\cos\\pi x^2\\supset(\\cos\\pi s^2+\\sin\\pi s^2)/\\sqrt2$ and $e^{i\\pi x^2}\\supset\\sqrt i\\,e^{-i\\pi s^2}$; at $s=0.3$ the first value is {{p2_val}}, and the phase of the second at $s=0$ is {{p3_ph}} degrees. Bracewell recommends thinking of a numerical check to catch a missing factor such as $\\sqrt2$.⟧</p>"),
                ("⟦Bài tập 5, 7, 8, 9, 10||Problems 5, 7, 8, 9, 10⟧",
                 "<p>⟦Bài 5: $f=\\Lambda(x/16)+\\Lambda(x/8+1)$ có $F=16\\,\\text{sinc}^216s+8\\,\\text{sinc}^28s\\,e^{i2\\pi8s}$; 33 giá trị và chương trình chậm ($\\Delta s=1/64$) cho $R(0)$ = {{p5_R0}} và lệch lớn nhất so với công thức là {{p5_err}}. Bài 7: tích $\\prod_{n\\le N}(1-s^2/n^2)$ không tiến về Gauss mà về $\\text{sinc}\\,s$: tại $s=0.3$ là {{pr_03}} cho $N=10^5$, tại $s=1.5$ là {{pr_15}} (âm, Gauss thì dương). Bài 8: bảy số $F_k$ của dữ liệu ngày (đọc từ văn bản OCR là 5, 4, 9, 8, 7, 6, 10): $F_0$ = {{p8_F0}}, $|F_1|$ = {{p8_F1}}. Bài 9 và 10: với $f=\\Lambda(x/a-1)$, $a=2$, $s=0.3$: biến đổi sin {{p9_fs}}, biến đổi cosin {{p10_fc}} (định nghĩa $F_c=2\\int_0^\\infty f\\cos$, $F_s=2\\int_0^\\infty f\\sin$).||"
                 "Problem 5: $f=\\Lambda(x/16)+\\Lambda(x/8+1)$ has $F=16\\,\\text{sinc}^216s+8\\,\\text{sinc}^28s\\,e^{i2\\pi8s}$; 33 values with the slow program ($\\Delta s=1/64$) give $R(0)$ = {{p5_R0}} and a largest deviation from the formula of {{p5_err}}. Problem 7: the product $\\prod_{n\\le N}(1-s^2/n^2)$ does not approach a Gaussian but $\\text{sinc}\\,s$: at $s=0.3$ it is {{pr_03}} for $N=10^5$, at $s=1.5$ it is {{pr_15}} (negative, a Gaussian is positive). Problem 8: the seven numbers $F_k$ of the weekday data (read from the OCR text as 5, 4, 9, 8, 7, 6, 10): $F_0$ = {{p8_F0}}, $|F_1|$ = {{p8_F1}}. Problems 9 and 10: for $f=\\Lambda(x/a-1)$, $a=2$, $s=0.3$: sine transform {{p9_fs}}, cosine transform {{p10_fc}} (definitions $F_c=2\\int_0^\\infty f\\cos$, $F_s=2\\int_0^\\infty f\\sin$).⟧</p>"),
                ("⟦Tự kiểm tra phần 5||Self-check, part 5⟧",
                 UL(["⟦Giao thoa kế đo đại lượng nào rồi biến đổi để có phổ?||Which quantity does the interferometer measure before transforming to obtain the spectrum?⟧",
                     "⟦Vì sao tương quan chéo cho nhiều thông tin hơn phổ hấp thụ?||Why does the cross-correlogram give more information than an absorption spectrum?⟧",
                     "⟦Tích $\\prod(1-s^2/n^2)$ hội tụ về hàm nào?||What function does $\\prod(1-s^2/n^2)$ converge to?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: tự tương quan; vì nó cho kết quả phức (cả biên độ và pha); $\\text{sinc}\\,s$.||Hints: the autocorrelation; because the result is complex (amplitude and phase); $\\text{sinc}\\,s$.⟧</p>"),
            ]),
    ],
    takeaways=[
        "⟦Tích phân dạng đóng làm được cho hàm chia đoạn, xung, mũ, Gauss; $1/x$ và $\\text{sgn}\\,x$ cần tích phân đường hoặc dãy giới hạn.||Closed-form integration works for segmented functions, impulses, exponentials and the Gaussian; $1/x$ and $\\text{sgn}\\,x$ need a contour integral or a limit sequence.⟧",
        "⟦Dữ liệu hữu hạn cho $s_{\\max}=1/2\\Delta x$, $\\Delta s=1/2X$, và $2X/\\Delta x$ bậc tự do.||Finite data give $s_{\\max}=1/2\\Delta x$, $\\Delta s=1/2X$ and $2X/\\Delta x$ degrees of freedom.⟧",
        "⟦Biến đổi \"chậm\" là ba dòng mã, cho phép chọn $K$ và soi dải hẹp; sai số chủ yếu do chồng phổ các bản sao.||The \"slow\" transform is a few lines of code that let you choose $K$ and zoom into a band; its error is mainly overlapping replicas.⟧",
        "⟦Đạo hàm liên tiếp quy hàm đoạn tuyến tính hoặc đa thức về xung; hằng số tích phân xác định từ diện tích và ràng buộc khác.||Repeated differentiation reduces piecewise linear or polynomial functions to impulses; integration constants are fixed by the area and other constraints.⟧",
        "⟦Quang phổ biến đổi Fourier đo tự tương quan rồi biến đổi thành phổ.||Fourier transform spectroscopy measures the autocorrelation and transforms it into the spectrum.⟧",
    ],
    history="<p>⟦Lanczos công bố ý chia đôi dữ liệu năm 1942, Gauss đã dùng năm 1805 khi phân tích số liệu sao chổi, và Cooley với Tukey (1965) đưa vào cộng đồng xử lý tín hiệu; Buneman chỉ ra rằng lập bảng trước $\\sin\\theta$ và $\\tan\\frac{\\theta}{2}$ nhanh hơn (Bracewell, tr. 141). Isaac Newton mở đầu phép đo phổ trong Opticks (1704) (tr. 147).||"
            "Lanczos published the idea of dividing the data in 1942, Gauss had used it in 1805 for cometary data, and Cooley and Tukey (1965) brought it to the signal processing community; Buneman showed that pretabulating $\\sin\\theta$ and $\\tan\\frac{\\theta}{2}$ was faster (Bracewell, p. 141). Isaac Newton started spectrum measurement in his Opticks (1704) (p. 147).⟧</p>"
            "<p>⟦Thư viện chuẩn: IMSL (1980), NAG (1980) và Numerical Recipes (Press và cộng sự, 1990); phần mềm bậc cao: LINPACK, MATHEMATICA, FORTRAN 90 và MATLAB (tr. 141 đến 142, 149).||Standard libraries: IMSL (1980), NAG (1980) and Numerical Recipes (Press et al., 1990); high-level software: LINPACK, MATHEMATICA, FORTRAN 90 and MATLAB (pp. 141 to 142, 149).⟧</p>",
    case="<p>⟦<b>Hai vạch phổ gần nhau.</b> Một giao thoa kế ghi tự tương quan của ánh sáng chứa hai vạch cường độ bằng nhau, với độ trễ tối đa $\\tau_{\\max}=10$ và bước $\\Delta\\tau=0.1$. Độ phân giải là {{res_lim}} và dải phủ tới {{band_lim}}. Hai vạch cách nhau {{sep_hi}} (gấp đôi độ phân giải) hiện thành {{peaks_res}} cực đại; hai vạch cách nhau {{sep_lo}} nhòe thành {{peaks_unres}}. Muốn tách vạch thứ hai phải tăng $\\tau_{\\max}$, tức kéo dài dữ liệu, cũng như phải đo $f(x)$ vượt xa $X$ nếu $F(s)$ có chi tiết mịn. Nếu nguồn có vạch tại 6 thì bước $\\Delta\\tau=0.1$ làm nó gấp về {{alias_peak}}: một lỗi chồng phổ điển hình.||"
          "<b>Two closely spaced lines.</b> An interferometer records the autocorrelation of light containing two lines of equal strength, with maximum delay $\\tau_{\\max}=10$ and step $\\Delta\\tau=0.1$. The resolution is {{res_lim}} and the band reaches {{band_lim}}. Two lines separated by {{sep_hi}} (twice the resolution) show up as {{peaks_res}} maxima; two lines separated by {{sep_lo}} blur into {{peaks_unres}}. To separate the second pair one must increase $\\tau_{\\max}$, i.e. lengthen the data, just as $f(x)$ must be measured far beyond $X$ if $F(s)$ has fine detail. If the source has a line at 6, the step $\\Delta\\tau=0.1$ folds it back to {{alias_peak}}: a typical aliasing error.⟧</p>",
    practice=[
        "⟦Mở notebook và chạy cell cài đặt.||Open the notebook and run the setup cell.⟧",
        "⟦Bài 1: viết lại hàm biến đổi chậm bằng ngôn ngữ ưa thích, chạy ví dụ 13 giá trị và so với $12\\,\\text{sinc}\\,12s$.||Task 1: rewrite the slow transform in your preferred language, run the 13-value example and compare with $12\\,\\text{sinc}\\,12s$.⟧",
        "⟦Bài 2: thử $K=X/2$, $K=X$, $K=4X$ và tự đếm số điểm, so với $2X+1$ hằng số độc lập.||Task 2: try $K=X/2$, $K=X$, $K=4X$ and count the points against the $2X+1$ independent constants.⟧",
        "⟦Bài 3: dùng đạo hàm liên tiếp tìm biến đổi của $x^2\\Pi(x)$ rồi kiểm bằng số.||Task 3: use continued differentiation to find the transform of $x^2\\Pi(x)$ and check numerically.⟧",
        "⟦Bài 4: cho hai vạch cách nhau đúng bằng độ phân giải và quan sát sự nhòe; thử đổi $\\tau_{\\max}$.||Task 4: put two lines separated by exactly the resolution and observe the blur; vary $\\tau_{\\max}$.⟧",
        "⟦Bài 5: làm bài 8 với dữ liệu của bạn (một tuần số liệu) và giải thích $F_1$.||Task 5: do problem 8 with your own data (one week) and interpret $F_1$.⟧",
    ],
    pitfalls=[
        "<b>⟦\"Đệm số 0 làm thay đổi biến đổi.\"||\"Zero padding changes the transform.\"⟧</b><p>⟦Các số hạng thêm vào bằng 0 nên biến đổi tại cùng $s$ không đổi (lệch {{pad_dev}}); đệm chỉ làm bước $\\Delta s$ mịn hơn nếu ta chọn $K$ tương ứng (tr. 144).||The added terms are zero so the transform at the same $s$ is unchanged (difference {{pad_dev}}); padding only makes $\\Delta s$ finer if we pick $K$ accordingly (p. 144).⟧</p>",
        "<b>⟦\"$K$ lớn hơn thì có thêm thông tin.\"||\"A larger $K$ gives more information.\"⟧</b><p>⟦$K=4X$ chỉ thêm điểm xen kẽ; số hằng số độc lập vẫn là $2X+1$ ($K=X$ đã đủ để dựng lại dữ liệu, lệch {{recon_dev}}).||$K=4X$ only adds interleaved points; the number of independent constants remains $2X+1$ ($K=X$ already reconstructs the data, deviation {{recon_dev}}).⟧</p>",
        "<b>⟦\"Sai khác với sinc chính xác biến mất khi lấy nhiều mẫu hơn.\"||\"The difference from the exact sinc disappears with more samples.\"⟧</b><p>⟦Biên độ sai số tuyệt đối không phụ thuộc $X$ (đường bao {{env_025}} tại $s=0.25$); chỉ sai số tương đối giảm ({{sl_pct1}} phần trăm rồi {{sl12_pct}}).||The absolute error's amplitude does not depend on $X$ (envelope {{env_025}} at $s=0.25$); only the relative error falls ({{sl_pct1}} percent then {{sl12_pct}}).⟧</p>",
        "<b>⟦\"Tích $\\prod(1-s^2/n^2)$ tiến về Gauss (định lý giới hạn trung tâm).\"||\"The product $\\prod(1-s^2/n^2)$ tends to a Gaussian (central limit theorem).\"⟧</b><p>⟦Nó tiến về $\\text{sinc}\\,s$ ({{pr_03}} tại 0.3 và {{pr_15}} tại 1.5, âm); chỉ gần Gauss khi $s$ rất nhỏ (bài tập 7, tr. 150).||It tends to $\\text{sinc}\\,s$ ({{pr_03}} at 0.3 and {{pr_15}} at 1.5, negative); it only looks Gaussian for very small $s$ (problem 7, p. 150).⟧</p>",
    ],
    refs=[
        "⟦R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chương 7 (tr. 136 đến 150).||R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chapter 7 (pp. 136 to 150).⟧",
        "⟦Tài liệu do chương 7 trích: Bell (1972), Bracewell (1986), Cooley và Tukey (1965), IMSL (1980), NAG (1980), Press và cộng sự (1990).||Works cited by chapter 7: Bell (1972), Bracewell (1986), Cooley and Tukey (1965), IMSL (1980), NAG (1980), Press et al. (1990).⟧",
    ],
    quiz=[
        dict(q="⟦Biến đổi của $\\Pi(x)$ tại $s=0.3$ bằng bao nhiêu?||What is the transform of $\\Pi(x)$ at $s=0.3$?⟧",
             opts=["{{cf_rect}}", "0.7071", "0.5236", "0.9549"], explain="⟦$\\text{sinc}\\,0.3$ = {{cf_rect}} theo cả tích phân và công thức.||$\\text{sinc}\\,0.3$ = {{cf_rect}} by both integral and formula.⟧"),
        dict(q="⟦Phần thực của biến đổi ba xung $(1,0,2),(0.5,3,1),(-1,-2,1)$ tại $s=0.3$ là bao nhiêu?||What is the real part of the transform of the three pulses $(1,0,2),(0.5,3,1),(-1,-2,1)$ at $s=0.3$?⟧",
             opts=["{{cf_re}}", "1.0000", "-0.5000", "0.7071"], explain="⟦$\\sum a_nc_n\\cos(2\\pi b_ns)\\text{sinc}\\,c_ns$ = {{cf_re}}; phần ảo {{cf_im}}.||$\\sum a_nc_n\\cos(2\\pi b_ns)\\text{sinc}\\,c_ns$ = {{cf_re}}; imaginary part {{cf_im}}.⟧"),
        dict(q="⟦Độ lớn biến đổi của ba xung $(a,b)=(2,-1),(-1,0.5),(0.5,2)$ tại $s=0.3$ là bao nhiêu?||What is the magnitude of the transform of the three impulses $(a,b)=(2,-1),(-1,0.5),(0.5,2)$ at $s=0.3$?⟧",
             opts=["{{cf_imp}}", "1.5000", "3.5000", "0.5000"], explain="⟦$|\\sum a_ne^{-i2\\pi b_ns}|$ = {{cf_imp}}.||$|\\sum a_ne^{-i2\\pi b_ns}|$ = {{cf_imp}}.⟧"),
        dict(q="⟦Biến đổi của $e^{-|x|}$ tại $s=0.3$ bằng bao nhiêu?||What is the transform of $e^{-|x|}$ at $s=0.3$?⟧",
             opts=["{{cf_exp}}", "0.5000", "0.8546", "0.3679"], explain="⟦$2/(1+4\\pi^2s^2)$ = {{cf_exp}}.||$2/(1+4\\pi^2s^2)$ = {{cf_exp}}.⟧"),
        dict(q="⟦Biến đổi của Gauss $e^{-\\pi x^2}$ tại $s=0.3$ (tích phân số phức) bằng bao nhiêu?||What is the transform of the Gaussian $e^{-\\pi x^2}$ at $s=0.3$ (complex numerical integral)?⟧",
             opts=["{{cf_gauss}}", "0.6065", "0.9048", "0.3679"], explain="⟦$e^{-\\pi(0.3)^2}$ = {{cf_gauss}}.||$e^{-\\pi(0.3)^2}$ = {{cf_gauss}}.⟧"),
        dict(q="⟦Phần ảo của biến đổi $1/x$ (cắt ở $|x|\\le10^4$) tại $s=0.3$ xấp xỉ bao nhiêu?||What is the imaginary part of the transform of $1/x$ (cut at $|x|\\le10^4$) at $s=0.3$, approximately?⟧",
             opts=["{{cf_1x}}", "-1.571", "3.142", "-6.283"], explain="⟦$-\\pi\\,\\text{sgn}\\,s$ = {{cf_1x}}.||$-\\pi\\,\\text{sgn}\\,s$ = {{cf_1x}}.⟧"),
        dict(q="⟦Bậc tự do của dữ liệu cách 1 trên $[-6,6]$ là bao nhiêu?||How many degrees of freedom do data spaced 1 over $[-6,6]$ have?⟧",
             opts=["{{dof}}", "13", "6", "24"], explain="⟦$2X/\\Delta x$ = {{dof}}; tần số tối đa {{fmax}}, bước {{dsmin}}.||$2X/\\Delta x$ = {{dof}}; maximum frequency {{fmax}}, step {{dsmin}}.⟧"),
        dict(q="⟦Lệch tối đa giữa FFT chiều dài 13 và tổng chậm là bao nhiêu?||What is the largest deviation between the length-13 FFT and the slow sum?⟧",
             opts=["{{fft_dev}}", "1.0e-03", "1.0e-01", "0.5000"], explain="⟦Cùng một biến đổi: lệch chỉ {{fft_dev}}, dù 13 là số nguyên tố.||The same transform: the difference is only {{fft_dev}}, even though 13 is prime.⟧"),
        dict(q="⟦$R(1)$ với dữ liệu 13 giá trị và $K=12$ bằng bao nhiêu?||What is $R(1)$ for the 13-value data with $K=12$?⟧",
             opts=["{{sl_R1}}", "7.639", "12.000", "6.000"], explain="⟦$\\sin(12\\pi/24)\\cot(\\pi/24)$ = {{sl_R1}}; $12\\,\\text{sinc}\\,0.5=7.639$.||$\\sin(12\\pi/24)\\cot(\\pi/24)$ = {{sl_R1}}; $12\\,\\text{sinc}\\,0.5=7.639$.⟧"),
        dict(q="⟦$R(3)$ với cùng dữ liệu và $K=12$ bằng bao nhiêu?||What is $R(3)$ for the same data and $K=12$?⟧",
             opts=["{{sl_R3}}", "-1.000", "2.414", "0.000"], explain="⟦$\\sin(12\\pi/8)\\cot(\\pi/8)$ = {{sl_R3}}.||$\\sin(12\\pi/8)\\cot(\\pi/8)$ = {{sl_R3}}.⟧"),
        dict(q="⟦Sai khác phần trăm của $R(1)$ so với $12\\,\\text{sinc}\\,0.5$ là bao nhiêu?||By how many percent does $R(1)$ differ from $12\\,\\text{sinc}\\,0.5$?⟧",
             opts=["{{sl_pct1}}", "0.28", "-2.56", "5.60"], explain="⟦$(7.596-7.639)/7.639$ = {{sl_pct1}} phần trăm.||$(7.596-7.639)/7.639$ = {{sl_pct1}} percent.⟧"),
        dict(q="⟦Với $K=24$ ta có $R(3)$ bằng bao nhiêu?||With $K=24$, what is $R(3)$?⟧",
             opts=["{{sl24_3}}", "7.596", "3.000", "10.788"], explain="⟦$\\sin(12\\pi\\cdot3/48)\\cot(3\\pi/48)$ = {{sl24_3}}; $R(1)$ = {{sl24_1}}.||$\\sin(12\\pi\\cdot3/48)\\cot(3\\pi/48)$ = {{sl24_3}}; $R(1)$ = {{sl24_1}}.⟧"),
        dict(q="⟦Lệch tối đa khi đệm số 0 (X=12) so với X=6 là bao nhiêu?||What is the maximum difference when zero-padding to X=12 versus X=6?⟧",
             opts=["{{pad_dev}}", "1.0e-03", "0.5000", "1.0e-01"], explain="⟦Số hạng thêm vào bằng 0: lệch {{pad_dev}}.||The added terms are zero: the difference is {{pad_dev}}.⟧"),
        dict(q="⟦Sai khác phần trăm của $R(1)$ với $24\\,\\text{sinc}\\,0.5$ (25 giá trị, $K=24$) là bao nhiêu?||By how many percent does $R(1)$ differ from $24\\,\\text{sinc}\\,0.5$ (25 values, $K=24$)?⟧",
             opts=["{{sl12_pct}}", "-0.56", "1.40", "-0.014"], explain="⟦Dày gấp đôi làm sai số tương đối còn {{sl12_pct}} phần trăm, cải thiện {{sl_ratio}} lần.||Doubling the density leaves a relative error of {{sl12_pct}} percent, an improvement by a factor {{sl_ratio}}.⟧"),
        dict(q="⟦Đường bao $|\\cot\\pi s-1/\\pi s|$ của sai số chồng phổ tại $s=0.25$ bằng bao nhiêu (không phụ thuộc $X$)?||What is the envelope $|\\cot\\pi s-1/\\pi s|$ of the aliasing error at $s=0.25$ (independent of $X$)?⟧",
             opts=["{{env_025}}", "1.0000", "0.5000", "1.2732"], explain="⟦$|1-4/\\pi|$ = {{env_025}}.||$|1-4/\\pi|$ = {{env_025}}.⟧"),
        dict(q="⟦$R$ tại $s=1$ (khi $K=12$, $k=2K$) bằng bao nhiêu?||What is $R$ at $s=1$ (with $K=12$, $k=2K$)?⟧",
             opts=["{{alias_R}}", "0.000", "7.596", "6.000"], explain="⟦Phổ tuần hoàn chu kỳ 1: $R(1)=R(0)$ = {{alias_R}}.||The spectrum is periodic with period 1: $R(1)=R(0)$ = {{alias_R}}.⟧"),
        dict(q="⟦Tổng các bản sao $\\sum_n12\\,\\text{sinc}\\,12(s-n)$ tại $s=1/24$ (cắt ở $|n|\\le20000$) bằng bao nhiêu?||What is the sum of replicas $\\sum_n12\\,\\text{sinc}\\,12(s-n)$ at $s=1/24$ (cut at $|n|\\le20000$)?⟧",
             opts=["{{alias_sum}}", "7.639", "12.000", "3.555"], explain="⟦Bằng $R(1)$ của chương trình chậm: {{alias_sum}}.||It equals the slow program's $R(1)$: {{alias_sum}}.⟧"),
        dict(q="⟦Lệch giữa dữ liệu dựng lại từ $R,I$ ($K=X$) và dữ liệu gốc là bao nhiêu?||What is the deviation between data reconstructed from $R,I$ ($K=X$) and the original data?⟧",
             opts=["{{recon_dev}}", "1.0e-01", "0.5000", "1.0e-03"], explain="⟦$2X+1$ hằng số độc lập là đủ: lệch {{recon_dev}}.||$2X+1$ independent constants suffice: the deviation is {{recon_dev}}.⟧"),
        dict(q="⟦Bao nhiêu điểm cho dải $k=5X\\ldots7X$ với $X=6$?||How many points does the band $k=5X\\ldots7X$ give for $X=6$?⟧",
             opts=["{{zoom_pts}}", "12", "7", "25"], explain="⟦Từ $5X$ tới $7X$ có $2X+1$ = {{zoom_pts}} điểm ở bước {{zoom_ds}}; lệch FFT đệm 0 {{zoom_dev}}.||From $5X$ to $7X$ there are $2X+1$ = {{zoom_pts}} points at step {{zoom_ds}}; deviation from a zero-padded FFT {{zoom_dev}}.⟧"),
        dict(q="⟦Biến đổi hình thang $\\Lambda*\\mu$ tại $s=0.3$ bằng bao nhiêu?||What is the transform of the trapezoid $\\Lambda*\\mu$ at $s=0.3$?⟧",
             opts=["{{th_trap}}", "0.7368", "0.4053", "0.5236"], explain="⟦$\\text{sinc}^2s\\cos\\pi s$ = {{th_trap}}.||$\\text{sinc}^2s\\cos\\pi s$ = {{th_trap}}.⟧"),
        dict(q="⟦$4\\cos2\\pi s-4\\,\\text{sinc}\\,2s$ tại $s=0.3$ bằng bao nhiêu?||What is $4\\cos2\\pi s-4\\,\\text{sinc}\\,2s$ at $s=0.3$?⟧",
             opts=["{{th_d2}}", "-1.236", "-2.500", "0.5000"], explain="⟦Bằng $(i2\\pi s)^2F(s)$ tính bằng tích phân số: {{th_d2}}.||It equals $(i2\\pi s)^2F(s)$ computed by numerical integration: {{th_d2}}.⟧"),
        dict(q="⟦Biến đổi xung parabol $(1-x^2)\\Pi(x/2)$ tại $s=0.3$ bằng bao nhiêu?||What is the transform of the parabolic pulse $(1-x^2)\\Pi(x/2)$ at $s=0.3$?⟧",
             opts=["{{th_par}}", "1.3333", "0.6667", "0.4053"], explain="⟦$(\\sin2\\pi s-2\\pi s\\cos2\\pi s)/2\\pi^3s^3$ = {{th_par}}; giới hạn $s\\to0$ là {{th_par0}}.||$(\\sin2\\pi s-2\\pi s\\cos2\\pi s)/2\\pi^3s^3$ = {{th_par}}; the limit $s\\to0$ is {{th_par0}}.⟧"),
        dict(q="⟦Ở ví dụ giao thoa kế ($\\tau_{\\max}=10$), độ phân giải xấp xỉ bao nhiêu?||In the interferometer example ($\\tau_{\\max}=10$), what is the resolution, approximately?⟧",
             opts=["{{res_lim}}", "0.5000", "0.1000", "0.2000"], explain="⟦$1/2\\tau_{\\max}$ = {{res_lim}}; dải phủ tới $1/2\\Delta\\tau$ = {{band_lim}}.||$1/2\\tau_{\\max}$ = {{res_lim}}; the band reaches $1/2\\Delta\\tau$ = {{band_lim}}.⟧"),
        dict(q="⟦Bao nhiêu cực đại thấy khi hai vạch cách 0.1 ($\\tau_{\\max}=10$)?||How many maxima are seen when two lines are separated by 0.1 ($\\tau_{\\max}=10$)?⟧",
             opts=["{{peaks_res}}", "1", "3", "4"], explain="⟦Cách {{sep_hi}} gấp đôi độ phân giải: {{peaks_res}} cực đại; cách {{sep_lo}}: {{peaks_unres}}.||Separated by {{sep_hi}}, twice the resolution: {{peaks_res}} maxima; separated by {{sep_lo}}: {{peaks_unres}}.⟧"),
        dict(q="⟦Vạch tại 6 với $\\Delta\\tau=0.1$ hiện ở tần số nào?||At which frequency does a line at 6 appear with $\\Delta\\tau=0.1$?⟧",
             opts=["{{alias_peak}}", "6.00", "10.00", "5.00"], explain="⟦Gấp qua $1/2\\Delta\\tau=5$: $10-6$ = {{alias_peak}}.||Folding over $1/2\\Delta\\tau=5$: $10-6$ = {{alias_peak}}.⟧"),
        dict(q="⟦$\\sum n^2f(n)$ với $f=e^{-\\pi(n/5)^2}$ bằng bao nhiêu (và bằng $-R''(0)/4\\pi^2$)?||What is $\\sum n^2f(n)$ for $f=e^{-\\pi(n/5)^2}$ (equal to $-R''(0)/4\\pi^2$)?⟧",
             opts=["{{p1_sum}}", "5.0000", "1.0000", "31.831"], explain="⟦Mômen bậc hai {{p1_sum}} bằng {{p1_num}} tính từ sai phân của $R$.||The second moment {{p1_sum}} equals {{p1_num}} from the second difference of $R$.⟧"),
        dict(q="⟦$(\\cos\\pi s^2+\\sin\\pi s^2)/\\sqrt2$ tại $s=0.3$ bằng bao nhiêu?||What is $(\\cos\\pi s^2+\\sin\\pi s^2)/\\sqrt2$ at $s=0.3$?⟧",
             opts=["{{p2_val}}", "1.3959", "0.7071", "0.9877"], explain="⟦Biến đổi của $\\cos\\pi x^2$ = {{p2_val}}, khớp tích phân điều hòa.||The transform of $\\cos\\pi x^2$ = {{p2_val}}, matching the regularised integral.⟧"),
        dict(q="⟦Pha (độ) của $\\sqrt i\\,e^{-i\\pi s^2}$ tại $s=0$ bằng bao nhiêu?||What is the phase (degrees) of $\\sqrt i\\,e^{-i\\pi s^2}$ at $s=0$?⟧",
             opts=["{{p3_ph}}", "90", "-45", "135"], explain="⟦$\\sqrt i=e^{i\\pi/4}$: {{p3_ph}} độ.||$\\sqrt i=e^{i\\pi/4}$: {{p3_ph}} degrees.⟧"),
        dict(q="⟦Lệch lớn nhất giữa chương trình chậm và công thức ở bài 5 là bao nhiêu?||What is the largest deviation between the slow program and the formula in problem 5?⟧",
             opts=["{{p5_err}}", "0.0000", "24.00", "1.000"], explain="⟦$R(0)$ = {{p5_R0}} khớp $16+8$; sai khác còn lại là chồng phổ: {{p5_err}}.||$R(0)$ = {{p5_R0}} matches $16+8$; the remaining difference is aliasing: {{p5_err}}.⟧"),
        dict(q="⟦Tích $\\prod_{n\\le N}(1-s^2/n^2)$ tại $s=1.5$ (N=$10^5$) bằng bao nhiêu?||What is $\\prod_{n\\le N}(1-s^2/n^2)$ at $s=1.5$ ($N=10^5$)?⟧",
             opts=["{{pr_15}}", "0.1054", "-0.4244", "0.0000"], explain="⟦Bằng $\\text{sinc}\\,1.5$ (âm), không phải Gauss dương; tại 0.3 là {{pr_03}}.||It equals $\\text{sinc}\\,1.5$ (negative), not a positive Gaussian; at 0.3 it is {{pr_03}}.⟧"),
        dict(q="⟦Với dữ liệu ngày 5, 4, 9, 8, 7, 6, 10, $F_0$ bằng bao nhiêu?||For weekday data 5, 4, 9, 8, 7, 6, 10, what is $F_0$?⟧",
             opts=["{{p8_F0}}", "7", "10", "59"], explain="⟦$F_0$ là tổng bảy giá trị: {{p8_F0}}; $|F_1|$ = {{p8_F1}}.||$F_0$ is the sum of the seven values: {{p8_F0}}; $|F_1|$ = {{p8_F1}}.⟧"),
        dict(q="⟦Biến đổi sin của $\\Lambda(x/a-1)$ với $a=2$ tại $s=0.3$ bằng bao nhiêu?||What is the sine transform of $\\Lambda(x/a-1)$ with $a=2$ at $s=0.3$?⟧",
             opts=["{{p9_fs}}", "0.7071", "-0.2000", "1.5000"], explain="⟦$2a\\,\\text{sinc}^2(as)\\sin2\\pi as$ = {{p9_fs}}; biến đổi cosin {{p10_fc}}.||$2a\\,\\text{sinc}^2(as)\\sin2\\pi as$ = {{p9_fs}}; the cosine transform is {{p10_fc}}.⟧"),
        dict(q="⟦Vì sao biến đổi \"chậm\" chỉ cần tính $k\\ge0$?||Why does the \"slow\" transform only need $k\\ge0$?⟧",
             opts=["⟦Với $k$ âm biến đổi là liên hợp phức của giá trị dương||For negative $k$ the transform is the complex conjugate of the positive value⟧",
                   "⟦Vì tần số âm không có ý nghĩa vật lý nên không bao giờ cần đến trong dữ liệu thực||Because negative frequencies have no physical meaning and are never needed for real data⟧",
                   "⟦Vì dữ liệu thực luôn có phần ảo bằng 0 và do đó $I(k)$ bằng 0 ở mọi tần số||Because real data always have zero imaginary part and hence $I(k)$ vanishes at every frequency⟧",
                   "⟦Vì bước $\\Delta s$ gấp đôi khi bỏ nửa dải âm, nên độ phân giải vẫn giữ nguyên||Because $\\Delta s$ doubles when the negative half band is dropped, so the resolution is preserved⟧"],
             explain="⟦Bracewell, tr. 143: với $k$ âm biến đổi là liên hợp phức $R(k)-iI(k)$; bỏ tính nửa âm tiết kiệm khoảng nửa thời gian.||Bracewell, p. 143: for negative $k$ the transform is the complex conjugate; not computing the negative half saves roughly half the running time.⟧"),
        dict(q="⟦Vì sao $\\text{sgn}\\,x$ được xử lý bằng dãy $\\exp(-\\tau|x|)\\text{sgn}\\,x$?||Why is $\\text{sgn}\\,x$ handled with the sequence $\\exp(-\\tau|x|)\\text{sgn}\\,x$?⟧",
             opts=["⟦Tích phân Fourier chuẩn không tồn tại vì hàm không khả tích tuyệt đối||The standard Fourier integral does not exist because the function is not absolutely integrable⟧",
                   "⟦Vì $\\text{sgn}\\,x$ có gián đoạn vô hạn tại gốc nên tích phân phân kỳ ở đó||Because $\\text{sgn}\\,x$ has an infinite discontinuity at the origin so the integral diverges there⟧",
                   "⟦Vì $\\text{sgn}\\,x$ là hàm lẻ nên biến đổi của nó chỉ tính được bằng tích phân đường||Because $\\text{sgn}\\,x$ is an odd function so its transform can only be found by a contour integral⟧",
                   "⟦Vì biến đổi của nó là xung tại $s=0$ mà tích phân số không tạo ra được||Because its transform is an impulse at $s=0$ which numerical integration cannot produce⟧"],
             explain="⟦Bracewell, tr. 140: tích phân Fourier không tồn tại theo nghĩa chuẩn; dãy tiến về giới hạn $1/i\\pi s$; lệch ở $\\tau=10^{-3}$ chỉ {{cf_sgn}}.||Bracewell, p. 140: the Fourier integral fails to exist in the standard sense; the sequence tends to $1/i\\pi s$; at $\\tau=10^{-3}$ the deviation is only {{cf_sgn}}.⟧"),
        dict(q="⟦Ba hạn chế của dữ liệu thật là gì?||What are the three limitations of real data?⟧",
             opts=["⟦Rời rạc, hữu hạn và có sai số||Discrete, finite and containing errors⟧",
                   "⟦Không âm, có giới hạn biên độ và không chẵn||Non-negative, amplitude-limited and not even⟧",
                   "⟦Tuần hoàn, đối xứng và có nhiễu trắng cộng tính không đổi||Periodic, symmetric and with constant additive white noise⟧",
                   "⟦Khả vi, khả tích tuyệt đối và bằng 0 ở vô cùng theo cả hai hướng||Differentiable, absolutely integrable and zero at infinity in both directions⟧"],
             explain="⟦Bracewell, tr. 140 đến 141: khoảng $\\Delta x$, khoảng đo $2X$, và sai số.||Bracewell, pp. 140 to 141: spacing $\\Delta x$, the range $2X$, and errors.⟧"),
        dict(q="⟦Ở đạo hàm liên tiếp của xung parabol, vì sao $K_1=K_2=0$?||In differentiating the parabolic pulse repeatedly, why is $K_1=K_2=0$?⟧",
             opts=["⟦Hàm gốc không chứa hằng số cộng hay dốc tuyến tính||The original function contains no additive constant or linear ramp⟧",
                   "⟦Vì xung parabol chẵn nên hằng số tích phân luôn triệt tiêu theo đối xứng||Because the parabolic pulse is even so integration constants always vanish by symmetry⟧",
                   "⟦Vì đạo hàm bậc hai không có xung ở chỗ nào của hàm số đang xét||Because the second derivative has no impulses anywhere for the function considered⟧",
                   "⟦Vì diện tích của xung bằng 0 nên mọi hằng số phải bằng 0||Because the pulse's area is zero so all constants must be zero⟧"],
             explain="⟦Bracewell, tr. 147: tích phân xung parabol cho thấy không có hằng số cộng hay dốc, nên $K_1=K_2=0$.||Bracewell, p. 147: integration of the given pulse shows no additive constant or ramp is present, so $K_1=K_2=0$.⟧"),
        dict(q="⟦Trong giao thoa kế của quang phổ biến đổi Fourier, đại lượng nào được biến đổi để có phổ công suất?||In the interferometer of Fourier transform spectroscopy, which quantity is transformed to obtain the power spectrum?⟧",
             opts=["⟦Tự tương quan thời gian của tín hiệu||The temporal autocorrelation of the signal⟧",
                   "⟦Cường độ chùm sáng tại đầu dò theo vị trí gương trong một lần quét đơn||The beam intensity at the detector against mirror position in a single scan⟧",
                   "⟦Bình phương biên độ điện trường tức thời trung bình theo mọi tần số||The mean squared instantaneous electric field amplitude across all frequencies⟧",
                   "⟦Hiệu pha giữa hai chùm khi chưa chèn độ trễ nào giữa chúng||The phase difference between the two beams when no delay is inserted between them⟧"],
             explain="⟦Bracewell, tr. 148: tự tương quan của $s(t)$ biến đổi Fourier thành phổ công suất.||Bracewell, p. 148: the autocorrelation of $s(t)$ Fourier-transforms into the power spectrum.⟧"),
        dict(q="⟦Vì sao tương quan chéo trong giao thoa kế cho nhiều thông tin hơn phổ hấp thụ?||Why does the interferometer's cross-correlogram give more information than an absorption spectrum?⟧",
             opts=["⟦Không chẵn nên biến đổi cho kết quả phức, gồm cả biên độ và pha||Not even, so the transform is complex, with both amplitude and phase⟧",
                   "⟦Vì nó dùng nguồn công suất lớn hơn nên tỷ số tín hiệu trên nhiễu cao hơn nhiều||Because it uses a higher-power source so the signal-to-noise ratio is much higher⟧",
                   "⟦Vì nó tránh được sự chồng phổ nên độ phân giải tần số tốt hơn||Because it avoids aliasing so the frequency resolution is better⟧",
                   "⟦Vì độ trễ âm cho thêm hai lần số điểm dữ liệu độc lập trên cùng dải phổ||Because negative delays give twice as many independent data points over the same spectral range⟧"],
             explain="⟦Bracewell, tr. 148: kết quả phức cho phép suy ra hằng số điện môi, độ dẫn, chiết suất, hệ số hấp thụ trên toàn dải phổ.||Bracewell, p. 148: the complex result yields permittivity, conductivity, refractive index and absorption coefficient over the full spectral range.⟧"),
    ],
    nb=[
        ("md", """## 1. ⟦Tích phân dạng đóng||Closed-form integration⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Các công thức đóng cho chữ nhật, bậc thang, xung, $e^{-|x|}$, Gauss, $1/x$ và $\\text{sgn}\\,x$ có khớp với tích phân số không? Mỗi số được tính bằng tích phân số và bằng công thức.||Do the closed forms for rectangles, staircases, impulses, $e^{-|x|}$, the Gaussian, $1/x$ and $\\text{sgn}\\,x$ match numerical integrals? Each number is computed by numerical integration and by the formula.⟧"""),
        ("code", r'''from scipy import integrate, special
trap = getattr(np, "trapezoid", None) or np.trapz

def ftq(f, a, b, s, pts=None):
    re = integrate.quad(lambda x: f(x)*np.cos(2*np.pi*x*s), a, b, points=pts, limit=400)[0]
    im = integrate.quad(lambda x: -f(x)*np.sin(2*np.pi*x*s), a, b, points=pts, limit=400)[0]
    return re + 1j*im

s0 = 0.3
# ⟦chữ nhật||rectangle⟧
rect = ftq(lambda x: 1.0, -0.5, 0.5, s0)
assert abs(rect - np.sinc(s0)) < 1e-9
report("cf_rect", rect.real, ".4f")

# ⟦bậc thang: Σ a c e^{−i2πbs} sinc(cs)||staircase: Σ a c e^{−i2πbs} sinc(cs)⟧
pulses = [(1.0, 0.0, 2.0), (0.5, 3.0, 1.0), (-1.0, -2.0, 1.0)]
num = sum(a*ftq(lambda x: 1.0, b - c/2, b + c/2, s0) for a, b, c in pulses)
form = sum(a*c*np.exp(-2j*np.pi*b*s0)*np.sinc(c*s0) for a, b, c in pulses)
assert abs(num - form) < 1e-9
report("cf_re", form.real, ".4f"); report("cf_im", form.imag, ".4f")

# ⟦xung: chữ nhật hẹp rộng w, cao 1/w||impulses: narrow rectangles of width w, height 1/w⟧
imps = [(2.0, -1.0), (-1.0, 0.5), (0.5, 2.0)]
w = 1e-3
num_i = sum(a/w*ftq(lambda x: 1.0, b - w/2, b + w/2, s0) for a, b in imps)
form_i = sum(a*np.exp(-2j*np.pi*b*s0) for a, b in imps)
assert abs(num_i - form_i) < 1e-5
report("cf_imp", abs(form_i), ".4f")

# ⟦e^{−|x|}||e^{−|x|}⟧
e_num = ftq(lambda x: np.exp(-abs(x)), -60, 60, s0, [0]).real
e_re = 2*(1/(1 + 2j*np.pi*s0)).real
e_form = 2/(1 + 4*np.pi**2*s0**2)
assert abs(e_num - e_form) < 1e-9 and abs(e_re - e_form) < 1e-12
report("cf_exp", e_form, ".4f")

# ⟦Gauss: tích phân phức||Gaussian: complex integral⟧
g_num = ftq(lambda x: np.exp(-np.pi*x**2), -10, 10, s0)
assert abs(g_num - np.exp(-np.pi*s0**2)) < 1e-9
report("cf_gauss", g_num.real, ".4f")

# ⟦1/x: phần ảo −2∫₀^L sin(2πsx)/x dx = −2 Si(2πsL)||1/x: imaginary part −2∫₀^L sin(2πsx)/x dx = −2 Si(2πsL)⟧
L = 1e4
im_si = -2*special.sici(2*np.pi*s0*L)[0]
im_q = -2*integrate.quad(lambda x: 1.0/x, 1e-12, L, weight="sin", wvar=2*np.pi*s0, limit=8000)[0]
assert abs(im_si + np.pi) < 1e-3 and abs(im_q - im_si) < 1e-4
report("cf_1x", im_si, ".3f")

# ⟦sgn x: dãy exp(−τ|x|)sgn x||sgn x: the sequence exp(−τ|x|) sgn x⟧
tau = 1e-3
seq_form = 1/(tau + 2j*np.pi*s0) - 1/(tau - 2j*np.pi*s0)
seq_num = -2j*integrate.quad(lambda x: np.exp(-tau*x), 0, np.inf, weight="sin", wvar=2*np.pi*s0)[0]
lim = 1/(1j*np.pi*s0)
assert abs(seq_num - seq_form) < 1e-8
report("cf_sgn", abs(seq_form - lim), ".1e")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Tại $s=0.3$: $\\Pi\\to$ {{cf_rect}}; ba xung chữ nhật {{cf_re}} và {{cf_im}}i; ba xung Dirac có độ lớn {{cf_imp}}; $e^{-|x|}\\to$ {{cf_exp}}; Gauss {{cf_gauss}}; phần ảo của $1/x$ là {{cf_1x}}; dãy $\\text{sgn}$ lệch giới hạn {{cf_sgn}}.||At $s=0.3$: $\\Pi\\to$ {{cf_rect}}; three rectangles {{cf_re}} and {{cf_im}}i; three Dirac impulses have magnitude {{cf_imp}}; $e^{-|x|}\\to$ {{cf_exp}}; Gaussian {{cf_gauss}}; the imaginary part of $1/x$ is {{cf_1x}}; the $\\text{sgn}$ sequence is {{cf_sgn}} from the limit.⟧"""),
        ("md", """## 2. ⟦Chương trình biến đổi chậm||The slow Fourier transform program⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Chương trình cộng trực tiếp cho kết quả gì, khớp FFT ra sao (kể cả chiều dài nguyên tố), $K$ ảnh hưởng thế nào, và sai số chồng phổ có đúng là $\\sin(2\\pi Xs)[\\cot\\pi s-1/\\pi s]$? Mỗi số được tính bằng chương trình chậm, bằng công thức Dirichlet và bằng FFT.||What does the direct-sum program give, how does it match the FFT (even for a prime length), how does $K$ matter, and is the aliasing error really $\\sin(2\\pi Xs)[\\cot\\pi s-1/\\pi s]$? Each number is computed by the slow program, by the Dirichlet formula and by the FFT.⟧"""),
        ("code", r'''def slow_ft(f, X, K, ks=None):
    """R(k), I(k) for s = k/(2K); f holds x = -X..X."""
    x = np.arange(-X, X + 1)
    ks = np.arange(0, K + 1) if ks is None else np.asarray(ks)
    s = ks/(2*K)
    ang = 2*np.pi*np.outer(s, x)
    return ks, np.cos(ang) @ f, np.sin(ang) @ f

def rect_data(X, half):                       # ⟦Π(x/(2·half)) lấy mẫu, đầu mút = ½||Π(x/(2·half)) sampled, end values = ½⟧
    x = np.arange(-X, X + 1); f = (np.abs(x) < half).astype(float); f[np.abs(x) == half] = 0.5
    return f
dirichlet = lambda s, half: np.sin(2*np.pi*half*s)/np.tan(np.pi*s)

X = 6
f13 = rect_data(X, 6)
ks, R, I = slow_ft(f13, X, 12)
assert abs(R[0] - f13.sum()) < 1e-12 and abs(I[0]) < 1e-12 and np.max(np.abs(I)) < 1e-9
s_ = ks[1:]/24
assert np.allclose(R[1:], dirichlet(s_, 6), atol=1e-9)
print("R(k) =", np.round(R, 3))
report("sl_R1", R[1], ".3f"); report("sl_R3", R[3], ".3f"); report("sl_R5", R[5], ".3f"); report("sl_R11", R[11], ".3f")
exact1 = 12*np.sinc(12/24)
pct1 = 100*(R[1] - exact1)/exact1
assert abs(pct1 + 0.57) < 0.01
report("sl_pct1", pct1, ".2f")
report("dof", int(2*X), "d"); report("fmax", 0.5, ".1f"); report("dsmin", 1/(2*X), ".4f")

# ⟦K = 24||K = 24⟧
ks2, R2, I2 = slow_ft(f13, X, 24)
assert np.allclose(R2[1:], dirichlet(ks2[1:]/48, 6), atol=1e-9) and abs(R2[2] - R[1]) < 1e-12
report("sl24_1", R2[1], ".3f"); report("sl24_3", R2[3], ".3f")

# ⟦đệm số 0: X = 12||zero padding: X = 12⟧
f25 = np.zeros(25); f25[6:19] = f13
_, R3, _ = slow_ft(f25, 12, 24)
pad = np.max(np.abs(R3 - R2))
assert pad < 1e-9
report("pad_dev", 0, "d")

# ⟦dữ liệu dày gấp đôi Π(x/24)||twice as dense data Π(x/24)⟧
f25b = rect_data(12, 12)
_, R4, I4 = slow_ft(f25b, 12, 24)
assert np.allclose(R4[1:], dirichlet(np.arange(1, 25)/48, 12), atol=1e-9)
pct12 = 100*(R4[1] - 24*np.sinc(0.5))/(24*np.sinc(0.5))
report("sl12_1", R4[1], ".3f"); report("sl12_pct", pct12, ".2f"); report("sl_ratio", int(round(pct1/pct12)), "d")
report("env_025", abs(1/np.tan(np.pi/4) - 1/(np.pi/4)), ".4f")

# ⟦chồng phổ: R tại s = 1 (k = 2K) và tổng các bản sao||aliasing: R at s = 1 (k = 2K) and the sum of replicas⟧
_, Rfull, _ = slow_ft(f13, X, 12, ks=np.arange(0, 25))
assert abs(Rfull[24] - Rfull[0]) < 1e-9
report("alias_R", Rfull[24], ".3f")
n = np.arange(-20000, 20001)
alias_sum = np.sum(12*np.sinc(12*(1/24 - n)))
assert abs(alias_sum - R[1]) < 1e-3
report("alias_sum", alias_sum, ".3f")

# ⟦dựng lại dữ liệu từ R, I (K = X), dữ liệu ngẫu nhiên||reconstruct data from R, I (K = X), random data⟧
rg = np.random.default_rng(7); fr = rg.standard_normal(2*X + 1)
x = np.arange(-X, X + 1)
# ⟦dựng lại bằng giải hệ 2X+1 ẩn tại các s_k = k/(2X+1) (K = X + ½ tương đương)||reconstruct by solving 2X+1 unknowns at s_k = k/(2X+1) (equivalent to K = X + ½)⟧
sk2 = np.arange(0, X + 1)/(2*X + 1)
A = np.vstack([np.cos(2*np.pi*np.outer(sk2, x)), np.sin(2*np.pi*np.outer(sk2[1:], x))])
b = np.concatenate([np.cos(2*np.pi*np.outer(sk2, x)) @ fr, np.sin(2*np.pi*np.outer(sk2[1:], x)) @ fr])
sol = np.linalg.solve(A, b)
recon = np.max(np.abs(sol - fr))
assert A.shape == (2*X + 1, 2*X + 1) and recon < 1e-9
report("recon_dev", recon, ".1e")

# ⟦FFT so với tổng chậm, độ dài nguyên tố 13, phần pha||FFT vs slow sum, prime length 13, with phase⟧
f13r = rg.standard_normal(13)
xs = np.arange(-6, 7)
slow_full = np.array([np.sum(f13r*np.exp(-2j*np.pi*(k/13)*xs)) for k in range(13)])
fft_vals = np.fft.fft(np.roll(f13r, -6))                         # ⟦gốc ở x = 0||origin at x = 0⟧
fft_dev = np.max(np.abs(slow_full - fft_vals))
assert fft_dev < 1e-9
report("fft_dev", fft_dev, ".1e")

# ⟦dải hẹp: k = 5X..7X, K = 12X; so với FFT đệm 0 độ dài 24X||narrow band: k = 5X..7X, K = 12X; against a zero-padded FFT of length 24X⟧
Kz = 12*X; kz = np.arange(5*X, 7*X + 1)
_, Rz, Iz = slow_ft(f13, X, Kz, ks=kz)
Nz = 24*X
buf = np.zeros(Nz); buf[:X + 1] = f13[X:]; buf[-X:] = f13[:X]
Fz = np.fft.fft(buf)
zoom_dev = np.max(np.abs((Rz - 1j*Iz) - Fz[kz]))
assert zoom_dev < 1e-9 and len(kz) == 2*X + 1
report("zoom_pts", len(kz), "d"); report("zoom_ds", 1/(24*X), ".5f"); report("zoom_dev", zoom_dev, ".1e")

# ⟦gốc: dời dữ liệu 3 đơn vị||origin: shift the data by 3 units⟧
f_sh = np.zeros(2*X + 1 + 3); f_sh[3:] = f13
_, Ra, Ia = slow_ft(f13, X, 60, ks=[12]); Xs = X + 1
xsx = np.arange(-Xs, Xs + 1 + 2)
sval = 12/120
Fa = np.sum(f13*np.exp(-2j*np.pi*sval*np.arange(-X, X + 1)))
Fb = np.sum(f13*np.exp(-2j*np.pi*sval*(np.arange(-X, X + 1) + 3)))
assert abs(abs(Fa)**2 - abs(Fb)**2) < 1e-9
ph = np.degrees(np.angle(Fb/Fa))
assert abs(ph - (-360*sval*3)) < 1e-6
report("pow_orig", abs(Fa)**2, ".3f"); report("ph_orig", ph, ".1f")'''),
        ("code", r'''sfine = np.linspace(0.001, 1.0, 1000)
fig, ax = plt.subplots(figsize=(8, 3.4))
ax.plot(sfine, 12*np.sinc(12*sfine), color="tab:blue", label="12 sinc 12s")
ax.plot(sfine, dirichlet(sfine, 6), color="tab:red", lw=1, label="Σₙ 12 sinc 12(s−n)")
ax.stem(ks/24, R, linefmt="k-", markerfmt="ko", basefmt=" ", label="R(k), K = 12")
ax.set_xlabel("s"); ax.legend(fontsize=8); plt.tight_layout(); plt.show()''', dict(fig="slow_rect", cap="⟦Hình 1. Chương trình chậm với 13 giá trị chữ nhật và K = 12: các điểm R(k) nằm trên đường đỏ (tổng các bản sao), hơi lệch khỏi 12 sinc 12s (xanh) vì bản sao 12 sinc 12(s−1) chồng lên; ở s = 1 R quay về 12.||Figure 1. The slow program with 13 rectangle values and K = 12: the points R(k) lie on the red curve (sum of replicas), slightly off 12 sinc 12s (blue) because the replica 12 sinc 12(s−1) overlaps; at s = 1, R returns to 12.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦$K=12$: $R(1)$ = {{sl_R1}}, $R(3)$ = {{sl_R3}}, $R(5)$ = {{sl_R5}}, $R(11)$ = {{sl_R11}}; lệch {{sl_pct1}} phần trăm. $K=24$: {{sl24_1}} và {{sl24_3}}. Dữ liệu dày gấp đôi: {{sl12_1}}, lệch {{sl12_pct}} phần trăm (cải thiện {{sl_ratio}} lần). Đường bao sai số {{env_025}}. $R$ tại $s=1$ là {{alias_R}}; tổng bản sao {{alias_sum}}. Dựng lại dữ liệu lệch {{recon_dev}}; FFT so với tổng chậm lệch {{fft_dev}}; dải hẹp có {{zoom_pts}} điểm ở bước {{zoom_ds}}, lệch {{zoom_dev}}. Dời gốc giữ $|F|^2$ = {{pow_orig}} và thêm pha {{ph_orig}} độ.||$K=12$: $R(1)$ = {{sl_R1}}, $R(3)$ = {{sl_R3}}, $R(5)$ = {{sl_R5}}, $R(11)$ = {{sl_R11}}; off by {{sl_pct1}} percent. $K=24$: {{sl24_1}} and {{sl24_3}}. Twice as dense data: {{sl12_1}}, off by {{sl12_pct}} percent (improved by {{sl_ratio}}). Error envelope {{env_025}}. $R$ at $s=1$ is {{alias_R}}; sum of replicas {{alias_sum}}. Reconstruction deviates by {{recon_dev}}; FFT vs slow sum {{fft_dev}}; the narrow band has {{zoom_pts}} points at step {{zoom_ds}}, deviating {{zoom_dev}}. Moving the origin keeps $|F|^2$ = {{pow_orig}} and adds phase {{ph_orig}} degrees.⟧"""),
        ("md", """## 3. ⟦Sinh biến đổi từ định lý||Generating transforms from theorems⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Hình thang $\\Lambda*\\mu$, tam giác qua hai lần đạo hàm và xung parabol có đúng các biến đổi suy ra bằng định lý? Ta so tích phân số với công thức.||Do the trapezoid $\\Lambda*\\mu$, the triangle through two differentiations and the parabolic pulse have the transforms derived by theorems? We compare numerical integrals with the formulas.⟧"""),
        ("code", r'''Lam = lambda x: np.maximum(1 - np.abs(x), 0)
# ⟦hình thang Λ*μ||trapezoid Λ*μ⟧
trap_f = lambda x: 0.5*Lam(x + 0.5) + 0.5*Lam(x - 0.5)
th_trap = ftq(trap_f, -1.5, 1.5, s0, [-1.5, -0.5, 0.5, 1.5]).real
assert abs(th_trap - np.sinc(s0)**2*np.cos(np.pi*s0)) < 1e-9
report("th_trap", th_trap, ".4f")
# ⟦tam giác: hai lần đạo hàm||triangle: two differentiations⟧
d2 = 2*np.cos(2*np.pi*s0) - 2
tri = d2/(2j*np.pi*s0)**2
assert abs(d2 + 4*np.sin(np.pi*s0)**2) < 1e-12
report("th_tri_dev", abs(tri - np.sinc(s0)**2), ".1e")
# ⟦xung parabol||parabolic pulse⟧
par = lambda x: 1 - x**2
Fpar = ftq(par, -1, 1, s0).real
Fform = (np.sin(2*np.pi*s0) - 2*np.pi*s0*np.cos(2*np.pi*s0))/(2*np.pi**3*s0**3)
d2_rhs = 4*np.cos(2*np.pi*s0) - 4*np.sinc(2*s0)
assert abs(Fpar - Fform) < 1e-9 and abs(Fpar*(2j*np.pi*s0)**2 - d2_rhs) < 1e-9
sm = 1e-3
F0_lim = (np.sin(2*np.pi*sm) - 2*np.pi*sm*np.cos(2*np.pi*sm))/(2*np.pi**3*sm**3)
assert abs(F0_lim - 4/3) < 1e-5 and abs(integrate.quad(par, -1, 1)[0] - 4/3) < 1e-12
report("th_par", Fform, ".4f"); report("th_d2", d2_rhs, ".3f"); report("th_par0", F0_lim, ".4f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Hình thang {{th_trap}}; tam giác qua hai lần đạo hàm lệch {{th_tri_dev}}; $4\\cos2\\pi s-4\\,\\text{sinc}\\,2s$ = {{th_d2}}; xung parabol {{th_par}} tại 0.3 với giới hạn {{th_par0}} tại 0.||Trapezoid {{th_trap}}; the triangle through two differentiations deviates by {{th_tri_dev}}; $4\\cos2\\pi s-4\\,\\text{sinc}\\,2s$ = {{th_d2}}; the parabolic pulse {{th_par}} at 0.3 with limit {{th_par0}} at 0.⟧"""),
        ("md", """## 4. ⟦Đo phổ: giao thoa kế||Measuring spectra: the interferometer⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Hai vạch cách nhau bằng bao nhiêu thì tách được trong phổ suy từ tự tương quan hữu hạn, và một vạch trên dải Nyquist gấp về đâu? Ta biến đổi tự tương quan mô phỏng bằng biến đổi chậm và đếm cực đại.||How far apart must two lines be to be separated in a spectrum derived from a finite autocorrelogram, and where does a line beyond the Nyquist band fold to? We transform a simulated autocorrelogram with the slow transform and count maxima.⟧"""),
        ("code", r'''tau_max, dtau = 10.0, 0.1
taus = np.arange(-tau_max, tau_max + dtau/2, dtau)
def spectrum(lines, sgrid):
    ac = sum(0.5*np.cos(2*np.pi*f*taus) for f in lines)
    return np.array([np.sum(ac*np.cos(2*np.pi*s*taus))*dtau for s in sgrid])
def count_peaks(y, thr=0.5):
    idx = [i for i in range(1, len(y) - 1) if y[i] > y[i-1] and y[i] >= y[i+1] and y[i] > thr*y.max()]
    return len(idx)
sg = np.arange(1.5, 2.6, 0.0005)
def peaks_for(sep):
    y = spectrum([2.0, 2.0 + sep], sg)
    # ⟦cách B: FFT đệm 0 của cùng dãy (độ dài lớn) cho cùng số cực đại||method B: zero-padded FFT of the same sequence gives the same number of maxima⟧
    Nf = 2**16; buf = np.zeros(Nf); ac = sum(0.5*np.cos(2*np.pi*f*taus) for f in [2.0, 2.0 + sep])
    buf[:len(ac)] = ac
    Y = np.abs(np.fft.rfft(buf))*dtau; fr = np.fft.rfftfreq(Nf, dtau); m = (fr > 1.5) & (fr < 2.6)
    return count_peaks(y), count_peaks(Y[m])
p_hi = peaks_for(0.10); p_lo = peaks_for(0.03)
assert p_hi[0] == p_hi[1] == 2 and p_lo[0] == p_lo[1] == 1
report("res_lim", 1/(2*tau_max), ".2f"); report("band_lim", 1/(2*dtau), ".0f")
report("sep_hi", 0.10, ".2f"); report("sep_lo", 0.03, ".2f")
report("peaks_res", p_hi[0], "d"); report("peaks_unres", p_lo[0], "d")

# ⟦chồng phổ: vạch tại 6 với Δτ = 0.1||aliasing: a line at 6 with Δτ = 0.1⟧
sg2 = np.arange(0.0, 5.0, 0.001)
y6 = spectrum([6.0], sg2)
alias_peak = sg2[np.argmax(y6)]
assert abs(alias_peak - (1/dtau - 6)) < 2e-3
Nf = 2**16; buf = np.zeros(Nf); buf[:len(taus)] = 0.5*np.cos(2*np.pi*6.0*taus)
Y = np.abs(np.fft.rfft(buf)); fr = np.fft.rfftfreq(Nf, dtau)
assert abs(fr[np.argmax(Y)] - 4.0) < 0.01
report("alias_peak", alias_peak, ".2f")'''),
        ("code", r'''sg3 = np.arange(1.7, 2.4, 0.0005)
fig, ax = plt.subplots(figsize=(8, 3.2))
ax.plot(sg3, spectrum([2.0, 2.10], sg3), label=("⟦cách 0.10 (tách)||0.10 apart (resolved)⟧"))
ax.plot(sg3, spectrum([2.0, 2.03], sg3), label=("⟦cách 0.03 (nhòe)||0.03 apart (blurred)⟧"))
ax.set_xlabel("s"); ax.legend(fontsize=8); plt.tight_layout(); plt.show()''', dict(fig="two_lines", cap="⟦Hình 2. Phổ suy từ tự tương quan hữu hạn (τmax = 10): hai vạch cách 0.10 tách thành hai đỉnh, hai vạch cách 0.03 nhòe thành một.||Figure 2. Spectrum from a finite autocorrelogram (τmax = 10): two lines 0.10 apart give two peaks, two lines 0.03 apart blur into one.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Độ phân giải {{res_lim}}, dải phủ {{band_lim}}. Hai vạch cách {{sep_hi}}: {{peaks_res}} cực đại; cách {{sep_lo}}: {{peaks_unres}} cực đại. Vạch tại 6 gấp về {{alias_peak}}.||Resolution {{res_lim}}, band {{band_lim}}. Two lines {{sep_hi}} apart: {{peaks_res}} maxima; {{sep_lo}} apart: {{peaks_unres}} maximum. A line at 6 folds to {{alias_peak}}.⟧"""),
        ("md", """## 5. ⟦Bài tập chọn||Selected problems⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Các bài 1, 2, 3, 5, 7, 8, 9, 10 có đúng khi kiểm bằng số? Ta so tổng chậm, tích phân điều hòa và công thức.||Do problems 1, 2, 3, 5, 7, 8, 9, 10 hold when checked numerically? We compare slow sums, regularised integrals and formulas.⟧"""),
        ("code", r'''# ⟦Bài 1: Σ x² f = −R''(0)/4π², f = e^{−π(n/5)²}||Problem 1: Σ x² f = −R''(0)/4π², f = e^{−π(n/5)²}⟧
Xb = 25; xb = np.arange(-Xb, Xb + 1); fb = np.exp(-np.pi*(xb/5)**2)
m2 = np.sum(xb**2*fb)
Rs = lambda s: np.sum(fb*np.cos(2*np.pi*s*xb))
h = 1e-4
Rpp = (Rs(h) - 2*Rs(0) + Rs(-h))/h**2
assert abs(-Rpp/(4*np.pi**2) - m2) < 1e-4
report("p1_sum", m2, ".3f"); report("p1_num", -Rpp/(4*np.pi**2), ".3f")

# ⟦Bài 2, 3: hàm mũ chirp có nhân Gauss suy giảm ε||Problems 2, 3: chirp with a decaying Gaussian factor ε⟧
eps = 0.05
chirp_c = lambda x: np.exp(-np.pi*eps*x**2)*np.cos(np.pi*x**2)
num_c = ftq(chirp_c, -40, 40, s0, None)
formula_c = 0.5*((eps - 1j)**-0.5*np.exp(-np.pi*s0**2/(eps - 1j)) + (eps + 1j)**-0.5*np.exp(-np.pi*s0**2/(eps + 1j)))
assert abs(num_c - formula_c) < 1e-6
e2 = 1e-7
lim_c = 0.5*((e2 - 1j)**-0.5*np.exp(-np.pi*s0**2/(e2 - 1j)) + (e2 + 1j)**-0.5*np.exp(-np.pi*s0**2/(e2 + 1j)))
book = (np.cos(np.pi*s0**2) + np.sin(np.pi*s0**2))/np.sqrt(2)
assert abs(lim_c - book) < 1e-5
report("p2_val", book, ".4f")
ph3 = np.degrees(np.angle((1e-12 - 1j)**-0.5))
assert abs(ph3 - 45) < 1e-4
report("p3_ph", 45, "d")

# ⟦Bài 5: 33 giá trị, K = 32 (Δs = 1/64)||Problem 5: 33 values, K = 32 (Δs = 1/64)⟧
x5 = np.arange(-16, 17); f5 = Lam(x5/16) + Lam(x5/8 + 1)
ks5, R5, I5 = slow_ft(f5, 16, 32)
s5 = ks5/64
F5 = 16*np.sinc(16*s5)**2 + 8*np.sinc(8*s5)**2*np.exp(2j*np.pi*8*s5)
err5 = np.max(np.abs((R5 - 1j*I5) - F5))
assert abs(R5[0] - 24) < 1e-9
Ffft_full = np.fft.fft(np.concatenate([f5[16:], np.zeros(128 - 33), f5[:16]]))[::2][:33]
assert np.max(np.abs((R5 - 1j*I5) - Ffft_full)) < 1e-9
report("p5_R0", R5[0], ".0f"); report("p5_err", err5, ".2f")

# ⟦Bài 7: tích Π(1 − s²/n²) → sinc s||Problem 7: the product Π(1 − s²/n²) → sinc s⟧
N = 100000; nn = np.arange(1, N + 1)
pr = lambda s: np.prod(1 - s**2/nn**2)
assert abs(pr(0.3) - np.sinc(0.3)) < 1e-4 and abs(pr(1.5) - np.sinc(1.5)) < 1e-4
report("pr_03", pr(0.3), ".4f"); report("pr_15", pr(1.5), ".4f")

# ⟦Bài 8: bảy số F_k||Problem 8: the seven numbers F_k⟧
g7 = np.array([5, 4, 9, 8, 7, 6, 10.0])
Fk = np.array([np.sum(g7*np.exp(-2j*np.pi*np.arange(7)*k/7)) for k in range(7)])
assert np.allclose(Fk, np.fft.fft(g7)) and np.allclose(np.fft.ifft(Fk).real, g7)
report("p8_F0", Fk[0].real, ".0f"); report("p8_F1", abs(Fk[1]), ".3f")

# ⟦Bài 9, 10: Λ(x/a − 1), a = 2||Problems 9, 10: Λ(x/a − 1), a = 2⟧
a = 2.0
fa = lambda x: Lam(x/a - 1)
fs = 2*integrate.quad(lambda x: fa(x)*np.sin(2*np.pi*s0*x), 0, 2*a, points=[a], limit=200)[0]
fc = 2*integrate.quad(lambda x: fa(x)*np.cos(2*np.pi*s0*x), 0, 2*a, points=[a], limit=200)[0]
fs_f = 2*a*np.sinc(a*s0)**2*np.sin(2*np.pi*a*s0); fc_f = 2*a*np.sinc(a*s0)**2*np.cos(2*np.pi*a*s0)
assert abs(fs - fs_f) < 1e-9 and abs(fc - fc_f) < 1e-9
report("p9_fs", fs, ".4f"); report("p10_fc", fc, ".4f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Bài 1: $\\sum n^2f$ = {{p1_sum}} và {{p1_num}} từ $-R''(0)/4\\pi^2$. Bài 2 và 3: {{p2_val}}, pha {{p3_ph}} độ. Bài 5: $R(0)$ = {{p5_R0}}, lệch lớn nhất {{p5_err}}. Bài 7: {{pr_03}} và {{pr_15}}. Bài 8: $F_0$ = {{p8_F0}}, $|F_1|$ = {{p8_F1}}. Bài 9 và 10: {{p9_fs}} và {{p10_fc}}.||Problem 1: $\\sum n^2f$ = {{p1_sum}} and {{p1_num}} from $-R''(0)/4\\pi^2$. Problems 2 and 3: {{p2_val}}, phase {{p3_ph}} degrees. Problem 5: $R(0)$ = {{p5_R0}}, largest deviation {{p5_err}}. Problem 7: {{pr_03}} and {{pr_15}}. Problem 8: $F_0$ = {{p8_F0}}, $|F_1|$ = {{p8_F1}}. Problems 9 and 10: {{p9_fs}} and {{p10_fc}}.⟧"""),
    ],
)
