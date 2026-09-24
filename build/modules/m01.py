from lib import F, C, UL, OL, TBL

MOD = dict(
    n=1, slug="introduction", part="A", book="B",
    title="⟦Giới thiệu: vì sao dùng biến đổi Fourier||Introduction: why transform methods⟧",
    blurb="⟦Biến đổi là công cụ đưa bài toán tuyến tính về dạng dễ giải; dạng sóng và phổ là hai mặt của cùng một đối tượng vật lý.||"
          "A transform turns a linear problem into an easier one; a waveform and its spectrum are two faces of the same physical object.⟧",
    src="⟦Bracewell, chương 1, tr. 1–4||Bracewell, chapter 1, pp. 1–4⟧",
    objectives=[
        "⟦Giải thích được ý tưởng \"đổi miền rồi giải\" của mọi phép biến đổi tuyến tính.||Explain the \"change domain, then solve\" idea behind every linear transform.⟧",
        "⟦Nêu hai điều kiện (tuyến tính, bất biến theo thời gian) để sóng điều hòa vào cho sóng điều hòa cùng tần số ra.||State the two conditions (linearity, time invariance) under which a harmonic input gives a harmonic output at the same frequency.⟧",
        "⟦Đọc phổ từ FFT, biết rò phổ và pha, và kiểm tra bằng phép tính trực tiếp.||Read a spectrum from an FFT, know leakage and phase, and check it with a direct sum.⟧",
        "⟦Nhận ra ký hiệu $\\Pi$, $\\delta$, $\\text{III}$ và dấu $*$ mà cả giáo trình sẽ dùng.||Recognise the symbols $\\Pi$, $\\delta$, $\\text{III}$ and the asterisk $*$ used throughout the book.⟧",
        "⟦Biết hai giáo trình gốc của khóa (Bracewell và Barkat) gặp nhau ở đâu.||Know where the two source books of this course (Bracewell and Barkat) meet.⟧",
    ],
    parts=[
        # ------------------------------------------------------------ PART 1
        dict(
            title="⟦Biến đổi là công cụ giải bài toán tuyến tính||Transforms as a tool for linear problems⟧",
            scr=("⟦Bạn quen giải bài toán tuyến tính trực tiếp trong miền thời gian hoặc không gian.||You are used to solving linear problems directly in the time or space domain.⟧",
                 "⟦Khi hệ có \"trí nhớ\" hoặc tín hiệu phức tạp, phép giải trực tiếp nhanh chóng rối.||Once the system has memory or the signal is complicated, the direct solution gets messy fast.⟧",
                 "⟦Đổi sang miền biến đổi, giải ở đó, rồi đổi ngược về.||Move to the transform domain, solve there, and transform back.⟧"),
            preview=["⟦Ba bước: biến đổi, giải, biến đổi ngược||Three steps: transform, solve, invert⟧",
                     "⟦Ví dụ số: tích chập thành phép nhân||A numerical example: convolution becomes multiplication⟧",
                     "⟦Vì sao Fourier đứng trước Laplace và chuỗi Fourier||Why Fourier comes before Laplace and Fourier series⟧"],
            slides=[
                ("⟦Đổi miền, giải, rồi đổi ngược||Change domain, solve, change back⟧",
                 "<p>⟦Bracewell mở đầu: các phép biến đổi tuyến tính mang tên Fourier và Laplace là kỹ thuật giải bài toán trong hệ tuyến tính. Ta dùng phép biến đổi như một công cụ toán học hoặc vật lý để đổi bài toán thành một bài toán giải được (tr. 1).||"
                 "Bracewell opens by saying that linear transforms named for Fourier and Laplace are techniques for solving problems in linear systems. The transform is a mathematical or physical tool that alters the problem into one that can be solved (p. 1).⟧</p>"
                 + OL(["⟦Biến đổi bài toán sang miền tần số.||Transform the problem to the frequency domain.⟧", "⟦Giải ở đó, thường chỉ cần nhân và chia.||Solve there, usually with just multiplication and division.⟧", "⟦Biến đổi ngược để lấy đáp án trong miền gốc.||Invert to get the answer in the original domain.⟧"])),
                ("⟦Cặp biến đổi Fourier||The Fourier transform pair⟧",
                 F("⟦Hệ 1 của Bracewell (hằng số $2\\pi$ nằm trong số mũ)||Bracewell's system 1 (the $2\\pi$ sits in the exponent)⟧",
                   r"F(s)=\int_{-\infty}^{\infty} f(x)\,e^{-i2\pi xs}\,dx,\qquad f(x)=\int_{-\infty}^{\infty} F(s)\,e^{i2\pi xs}\,ds",
                   [("f(x)", "⟦hàm gốc theo biến $x$ (thời gian hoặc không gian)||original function of the variable $x$ (time or space)⟧"),
                    ("F(s)", "⟦biến đổi Fourier, hàm của tần số $s$||the Fourier transform, a function of frequency $s$⟧"),
                    ("s", "⟦tần số: số chu kỳ trên một đơn vị của $x$||frequency: cycles per unit of $x$⟧")])),
                ("⟦Ví dụ số: tích chập thành phép nhân||Numerical example: convolution becomes multiplication⟧",
                 "<p>⟦Tích chập nối tiếp (\"serial product\") của $\\{2,2,3,3,4\\}$ và $\\{1,1,2\\}$ được Bracewell tính tay ở tr. 32. Notebook tính bằng hai cách: tổng trực tiếp và nhân hai FFT rồi biến đổi ngược. Cả hai cho dãy {{conv_direct}}.||"
                 "Bracewell computes the serial product of $\\{2,2,3,3,4\\}$ and $\\{1,1,2\\}$ by hand on p. 32. The notebook does it two ways: the direct sum, and multiplying two FFTs then inverting. Both give the sequence {{conv_direct}}.⟧</p>"
                 + C("good", "⟦Kiểm tra nhanh||Quick check⟧", "<p>⟦Tổng các số hạng của tích chập bằng tích hai tổng: {{sum_f}} nhân {{sum_g}} bằng {{conv_sum}}.||The sum of the terms of the serial product equals the product of the two sums: {{sum_f}} times {{sum_g}} equals {{conv_sum}}.⟧</p>")),
                ("⟦Fourier đi trước Laplace||Fourier before Laplace⟧",
                 "<p>⟦Đi qua Fourier trước, nên khi Laplace tổng quát hơn xuất hiện ở chương sau, nhiều tính chất đã quen. Ta chỉ còn phải chú ý câu hỏi mới và thiết yếu: dải hội tụ trên mặt phẳng phức (tr. 1).||"
                 "Going through Fourier first means that when the more general Laplace transform arrives later, many properties are already familiar. Only the new and essential question remains: the strip of convergence in the complex plane (p. 1).⟧</p>"
                 + C("info", "⟦Trong khóa này||In this course⟧", "<p>⟦Module 17 quay lại Laplace. Khi đó bạn học thêm đúng một ý mới thay vì học lại cả bộ tính chất.||Module 17 returns to Laplace. You then learn exactly one new idea instead of relearning the whole set of properties.⟧</p>")),
                ("⟦Một định lý, nhiều hóa thân||One theorem, many physical embodiments⟧",
                 "<p>⟦Bracewell nhận xét rằng cùng một khái niệm hay xuất hiện dưới dạng khác ở lĩnh vực khác: nguyên lý kính hiển vi tương phản pha gợi nhớ mạch tách điều tần, và cả hai được giải thích bằng cùng cách dùng biến đổi. Một bài toán thống kê có thể giải bằng cách quen thuộc từ các tầng khuếch đại nối tiếp (tr. 1).||"
                 "Bracewell notes that a concept familiar in one branch often appears in a different guise in another: the phase-contrast microscope is reminiscent of the circuit that detects frequency modulation, and both are explained by transforms along the same lines. A statistics problem may yield to an approach familiar from cascaded amplifiers (p. 1).⟧</p>"
                 "<p>⟦Đây cũng là lý do khóa này ghép Bracewell với Barkat: cùng một tích chập xuất hiện trong lọc tín hiệu và trong phân phối của tổng các biến ngẫu nhiên.||"
                 "It is also why this course pairs Bracewell with Barkat: the same convolution appears in signal filtering and in the distribution of a sum of random variables.⟧</p>"),
                ("⟦Đảo thứ tự truyền thống||Reversing the traditional order⟧",
                 "<p>⟦Trong các giáo trình cổ điển, biến đổi Fourier thường xuất hiện ở bài giảng cuối của một khóa dài về chuỗi Fourier. Nếu đảo thứ tự, chuỗi Fourier trở thành trường hợp cực đoan trong khuôn khổ biến đổi Fourier, và khó khăn toán học của chuỗi gắn với tính cực đoan phi vật lý của nó (tr. 2).||"
                 "In traditional courses the Fourier transform shows up in the last lecture of a long course on Fourier series. Reverse the order and the series falls into place as an extreme case within transform theory, and its mathematical difficulties are tied to its non-physical extreme nature (p. 2).⟧</p>"
                 "<p>⟦Module 13 sẽ dựng lại chuỗi Fourier từ nhân với chuỗi xung $\\text{III}$.||Module 13 rebuilds the Fourier series from multiplication by the impulse train $\\text{III}$.⟧</p>"),
                ("⟦Hai đại lượng mang cùng thông tin: bảo toàn năng lượng||Same information in both domains: energy conservation⟧",
                 "<p>⟦Với một tín hiệu mẫu 1000 điểm, tổng bình phương theo thời gian là {{energy_time}} và $\\frac1N\\sum|X_k|^2$ theo tần số là {{energy_freq}}. Hai số bằng nhau (định lý Rayleigh, module 6).||"
                 "For a 1000-point test signal, the sum of squares in time is {{energy_time}} and $\\frac1N\\sum|X_k|^2$ in frequency is {{energy_freq}}. The two are equal (Rayleigh's theorem, module 6).⟧</p>"
                 + F("⟦Bảo toàn năng lượng (dạng rời rạc)||Energy conservation (discrete form)⟧", r"\sum_{n=0}^{N-1}|x_n|^2=\frac1N\sum_{k=0}^{N-1}|X_k|^2")),
                ("⟦Tự kiểm tra phần 1||Self-check, part 1⟧",
                 UL(["⟦Vì sao tổng các số hạng của tích chập bằng tích hai tổng? (Gợi ý: đặt $s=0$ trong biến đổi của tích chập.)||Why does the sum of the terms of a convolution equal the product of the two sums? (Hint: set $s=0$ in the transform of the convolution.)⟧",
                     "⟦Nếu một tín hiệu có năng lượng theo thời gian là {{energy_time}}, năng lượng theo tần số phải là bao nhiêu?||If a signal has time-domain energy {{energy_time}}, what must its frequency-domain energy be?⟧",
                     "⟦Vì sao Bracewell nói chuỗi Fourier là trường hợp \"cực đoan\"?||Why does Bracewell call the Fourier series an \"extreme\" case?⟧"])
                 + "<p class='lang-note'>⟦Đáp án gợi ý: $F(0)=\\int f$, nên biến đổi của tích chập tại $s=0$ bằng $F(0)G(0)$; đáp án hai bằng đúng {{energy_freq}}; đáp án ba: vì tuần hoàn vô hạn không có biến đổi thường (module 2).||Hints: $F(0)=\\int f$, so the transform of the convolution at $s=0$ equals $F(0)G(0)$; the second answer is exactly {{energy_freq}}; the third: because an infinite periodic signal has no ordinary transform (module 2).⟧</p>"),
            ]),
        # ------------------------------------------------------------ PART 2
        dict(
            title="⟦Dạng sóng và phổ||Waveforms and spectra⟧",
            scr=("⟦Ta nhìn dạng sóng trên máy hiện sóng và nghe âm thanh bằng tai.||We see a waveform on an oscilloscope and hear sound with our ears.⟧",
                 "⟦\"Phổ\" có phải chỉ là một đại lượng toán học trừu tượng không?||Is the \"spectrum\" just an abstract mathematical quantity?⟧",
                 "⟦Dạng sóng và phổ là biến đổi Fourier của nhau, đều đo được, và đọc phổ đòi hỏi vài quy ước cần nắm.||A waveform and its spectrum are Fourier transforms of each other, both measurable, and reading a spectrum needs a few conventions.⟧"),
            preview=["⟦Ba sóng hình sin và phổ của chúng||Three sinusoids and their spectrum⟧",
                     "⟦Hai cách tính phổ, độ phân giải và rò phổ||Two ways to compute a spectrum, resolution and leakage⟧",
                     "⟦Pha, đơn vị tần số và tính tuyến tính của phổ||Phase, frequency units and linearity of the spectrum⟧"],
            slides=[
                ("⟦Ba sóng hình sin: đọc phổ từ FFT||Three sinusoids: reading the spectrum from an FFT⟧",
                 "<p>⟦Tín hiệu mẫu gồm 1.0 tại 50 Hz, 0.5 tại 120 Hz và 0.25 tại 300 Hz. FFT phục hồi các biên độ {{a50}}, {{a120}} và {{a300}}.||"
                 "The test signal has 1.0 at 50 Hz, 0.5 at 120 Hz and 0.25 at 300 Hz. The FFT recovers the amplitudes {{a50}}, {{a120}} and {{a300}}.⟧</p>{{fig:waveform_spectrum}}"),
                ("⟦Phổ là thứ đo được, không chỉ là công thức||The spectrum is something you can measure⟧",
                 "<p>⟦Máy hiện sóng cho ta thấy dạng sóng điện, máy phân tích phổ cho ta thấy phổ điện hoặc phổ quang, và tai người nghe được phổ (Bracewell, tr. 1).||"
                 "An oscilloscope shows an electrical waveform, a spectrum analyzer shows electrical or optical spectra, and the ear hears spectra (Bracewell, p. 1).⟧</p>"
                 + UL(["⟦Dạng sóng: $x(t)$, đo bằng máy hiện sóng.||Waveform: $x(t)$, measured with an oscilloscope.⟧",
                       "⟦Phổ: $X(f)$, đo bằng máy phân tích phổ hoặc bằng tai.||Spectrum: $X(f)$, measured with a spectrum analyzer or by ear.⟧",
                       "⟦Hai đại lượng là biến đổi Fourier của nhau, nên mang cùng lượng thông tin.||The two are Fourier transforms of each other, so they carry the same information.⟧"])),
                ("⟦Hai cách tính phổ cho cùng đáp số||Two ways to compute a spectrum, one answer⟧",
                 "<p>⟦Cách A dùng FFT. Cách B cộng trực tiếp theo định nghĩa $X_k=\\sum_n x_ne^{-i2\\pi kn/N}$ (\"biến đổi Fourier chậm\" của Bracewell, chương 7). Chúng lệch nhau tối đa {{fft_direct_diff}}, tức là trùng tới sai số làm tròn.||"
                 "Method A uses the FFT. Method B sums directly from the definition $X_k=\\sum_n x_ne^{-i2\\pi kn/N}$ (Bracewell's \"slow Fourier transform\", chapter 7). They differ by at most {{fft_direct_diff}}, i.e. they agree to rounding error.⟧</p>"
                 + F("⟦Biên độ một phía||One-sided amplitude⟧", r"A_k=\frac{2\,|X_k|}{N}\quad(k\ge1),\qquad A_0=\frac{|X_0|}{N}",
                     [("N", "⟦số mẫu||number of samples⟧"), ("X_k", "⟦hệ số DFT thứ $k$||the $k$-th DFT coefficient⟧"), ("A_k", "⟦biên độ của sóng hình sin tại tần số $k\\,f_s/N$||amplitude of the sinusoid at frequency $k\\,f_s/N$⟧")])),
                ("⟦Độ phân giải tần số||Frequency resolution⟧",
                 "<p>⟦Quan sát 1 giây với tần số lấy mẫu 1000 Hz cho 1000 mẫu và các ô tần số cách nhau $f_s/N=1$ Hz. Muốn tách hai vạch cách nhau 0.5 Hz phải quan sát ít nhất 2 giây.||"
                 "Observing 1 second at 1000 Hz sampling gives 1000 samples and frequency bins spaced $f_s/N=1$ Hz apart. To separate two lines 0.5 Hz apart you must observe for at least 2 seconds.⟧</p>"
                 + F("⟦Khoảng cách ô tần số||Bin spacing⟧", r"\Delta f=\frac{f_s}{N}=\frac{1}{T}",
                     [("T", "⟦thời gian quan sát||observation time⟧"), ("f_s", "⟦tần số lấy mẫu||sampling rate⟧")])),
                ("⟦Rò phổ: khi tần số rơi giữa hai ô||Leakage: when the frequency falls between two bins⟧",
                 "<p>⟦Sóng 50.5 Hz phân tích trong 1 giây không rơi đúng vào ô nào. Biên độ tại ô 50 chỉ còn {{leak_peak}} (thay vì 1), dự đoán $|\\text{sinc}(0.5)|$ là {{leak_theory}}, và ngay cả tại ô 80 vẫn còn {{leak_far}}.||"
                 "A 50.5 Hz wave analysed over 1 second falls on no bin. The amplitude at bin 50 is only {{leak_peak}} (instead of 1), the prediction $|\\text{sinc}(0.5)|$ is {{leak_theory}}, and even at bin 80 there is still {{leak_far}}.⟧</p>{{fig:leakage}}"),
                ("⟦Pha: sin và cos khác nhau ở đâu||Phase: how sin and cos differ⟧",
                 "<p>⟦Phổ biên độ không phân biệt $\\sin$ và $\\cos$; pha mới phân biệt. FFT cho pha {{ph_sin}} độ tại ô 50 của $\\sin$ và {{ph_cos}} độ tại ô 120 của $\\cos$.||"
                 "The amplitude spectrum does not tell $\\sin$ from $\\cos$; the phase does. The FFT gives phase {{ph_sin}} degrees at bin 50 for the $\\sin$ and {{ph_cos}} degrees at bin 120 for the $\\cos$.⟧</p>"
                 + F("⟦Liên hệ pha||Phase relation⟧", r"\sin(2\pi f t)\leftrightarrow -90^\circ,\qquad \cos(2\pi f t)\leftrightarrow 0^\circ")),
                ("⟦Tần số $s$ là chu kỳ trên đơn vị, không phải rad/s||Frequency $s$ is cycles per unit, not rad/s⟧",
                 "<p>⟦Giáo trình giữ $2\\pi$ trong số mũ nên $s$ là số chu kỳ trên một đơn vị của $x$ (tr. 6, 18). Nếu bạn đọc tài liệu khác dùng $\\omega$ thì đổi bằng $\\omega=2\\pi s$.||"
                 "The book keeps $2\\pi$ in the exponent so $s$ is the number of cycles per unit of $x$ (pp. 6, 18). If another text uses $\\omega$, convert with $\\omega=2\\pi s$.⟧</p>"
                 + TBL(["⟦Hệ||System⟧", "$F(s)$", "$f(x)$"],
                       [["1", r"$\int f(x)e^{-i2\pi xs}dx$", r"$\int F(s)e^{i2\pi xs}ds$"],
                        ["2", r"$\int f(x)e^{-i\omega x}dx$", r"$\frac1{2\pi}\int F(\omega)e^{i\omega x}d\omega$"],
                        ["3", r"$\frac1{\sqrt{2\pi}}\int f(x)e^{-i\omega x}dx$", r"$\frac1{\sqrt{2\pi}}\int F(\omega)e^{i\omega x}d\omega$"]])),
                ("⟦Phổ của tổng bằng tổng các phổ||The spectrum of a sum is the sum of the spectra⟧",
                 "<p>⟦Biến đổi Fourier là tuyến tính: $\\mathcal F\\{x_1+x_2\\}=\\mathcal F\\{x_1\\}+\\mathcal F\\{x_2\\}$. Notebook kiểm tra với hai tín hiệu, sai lệch lớn nhất là {{lin_err}}, cỡ sai số làm tròn.||"
                 "The Fourier transform is linear: $\\mathcal F\\{x_1+x_2\\}=\\mathcal F\\{x_1\\}+\\mathcal F\\{x_2\\}$. The notebook checks it with two signals; the largest deviation is {{lin_err}}, of the order of rounding error.⟧</p>"
                 + C("warn", "⟦Đừng nhầm||Do not confuse⟧", "<p>⟦Tuyến tính của phép biến đổi khác với tuyến tính của một hệ. Phần 3 sẽ tách hai khái niệm này.||Linearity of the transform is different from linearity of a system. Part 3 separates the two.⟧</p>")),
            ]),
        # ------------------------------------------------------------ PART 3
        dict(
            title="⟦Tuyến tính, bất biến và tích chập||Linearity, invariance and convolution⟧",
            scr=("⟦Bộ khuếch đại được mô tả bằng đáp ứng tần số, và sóng hình sin vào thường cho sóng hình sin ra.||An amplifier is specified by its frequency response, and a sinusoid in usually gives a sinusoid out.⟧",
                 "⟦Điều đó đúng khi nào, và khi nào sai?||When is that true, and when does it fail?⟧",
                 "⟦Đúng khi hệ tuyến tính và bất biến; khi đó đáp ứng liên hệ với kích thích bằng tích chập.||It holds for linear, invariant systems; then the response is related to the stimulus by convolution.⟧"),
            preview=["⟦Hai điều kiện và bộ lọc thử nghiệm||The two conditions and a test filter⟧",
                     "⟦Đáp ứng xung, đáp ứng tần số||Impulse response and frequency response⟧",
                     "⟦Phi tuyến, thay đổi theo thời gian và méo hài||Nonlinearity, time variation and harmonic distortion⟧"],
            slides=[
                ("⟦Đáp ứng điều hòa với kích thích điều hòa||Harmonic response to harmonic stimulus⟧",
                 "<p>⟦Đáp ứng của một hệ với sóng điều hòa vẫn là điều hòa, cùng tần số, với hai điều kiện: tuyến tính và bất biến theo thời gian (Bracewell, tr. 3). Vì vậy ta mô tả bộ khuếch đại bằng đáp ứng tần số.||"
                 "The response of a system to harmonic input is itself harmonic, at the same frequency, under two conditions: linearity and time invariance (Bracewell, p. 3). That is why an amplifier is specified by its frequency response.⟧</p>"),
                ("⟦Gộp hai điều kiện thành một: tích chập||Two conditions merged into one: convolution⟧",
                 "<p>⟦Hai điều kiện có thể phát biểu thành một: đáp ứng liên hệ với kích thích bằng tích chập (tr. 3).||The two conditions can be restated as one: the response is relatable to the stimulus by convolution (p. 3).⟧</p>"
                 + F("⟦Đáp ứng của hệ tuyến tính bất biến||Response of a linear invariant system⟧", r"y(t)=(h*x)(t)=\int_{-\infty}^{\infty}h(u)\,x(t-u)\,du",
                     [("x(t)", "⟦kích thích (tín hiệu vào)||stimulus (input signal)⟧"), ("h(t)", "⟦đáp ứng xung của hệ||impulse response of the system⟧"), ("y(t)", "⟦đáp ứng (tín hiệu ra)||response (output signal)⟧")])),
                ("⟦Đáp ứng xung của bộ lọc thông thấp bậc một||Impulse response of a first-order low-pass filter⟧",
                 "<p>⟦Bộ lọc $y[n]=a\\,y[n-1]+(1-a)\\,x[n]$ với $a=0.9$ có đáp ứng xung $h[n]=(1-a)a^n$. Tích chập trực tiếp với $h$ và hàm <code>lfilter</code> cho cùng đáp số (lệch tối đa {{conv_lfilter_diff}}), và tổng của $h$ là {{h_sum}}, tức độ lợi một chiều bằng 1.||"
                 "The filter $y[n]=a\\,y[n-1]+(1-a)\\,x[n]$ with $a=0.9$ has impulse response $h[n]=(1-a)a^n$. Direct convolution with $h$ and the <code>lfilter</code> function give the same answer (largest deviation {{conv_lfilter_diff}}), and the sum of $h$ is {{h_sum}}, i.e. unit DC gain.⟧</p>"),
                ("⟦Thử với sóng 50 Hz||Test with a 50 Hz wave⟧",
                 "<p>⟦Đầu vào 50 Hz, lấy mẫu 1000 Hz. Tần số ra là {{f_out}} Hz. Độ lợi đo được {{gain_meas}}, theo lý thuyết {{gain_theory}}. Pha đo được {{phase_meas_deg}} độ, theo lý thuyết {{phase_theory_deg}} độ (dấu âm nghĩa là sóng ra trễ).||"
                 "Input at 50 Hz, sampled at 1000 Hz. The output frequency is {{f_out}} Hz. The measured gain is {{gain_meas}}, the theoretical gain {{gain_theory}}. The measured phase is {{phase_meas_deg}} degrees, the theoretical {{phase_theory_deg}} degrees (negative means the output lags).⟧</p>"
                 + F("⟦Đáp ứng tần số của bộ lọc||Frequency response of the filter⟧", r"H(\omega)=\frac{1-a}{1-a\,e^{-i\omega}},\qquad \omega=\frac{2\pi f}{f_s}")),
                ("⟦Đáp ứng tần số ở nhiều tần số||Frequency response at several frequencies⟧",
                 "<p>⟦Đo bằng FFT tại 25, 50, 100 và 200 Hz: độ lợi lần lượt {{gain_25}}, {{gain_meas}}, {{gain_100}} và {{gain_200}}, khớp đường lý thuyết. Bộ lọc thông thấp: tần số càng cao, biên độ càng giảm.||"
                 "Measured by FFT at 25, 50, 100 and 200 Hz, the gains are {{gain_25}}, {{gain_meas}}, {{gain_100}} and {{gain_200}}, matching the theoretical curve. A low-pass filter: the higher the frequency, the smaller the amplitude.⟧</p>{{fig:lowpass_response}}"),
                ("⟦Khi điều kiện bị phá vỡ, tần số mới xuất hiện||When the conditions fail, new frequencies appear⟧",
                 "<p>⟦Sóng 50 Hz qua khâu bình phương (phi tuyến): thành phần một chiều {{nl_dc}}, thành phần 100 Hz biên độ {{nl_a100}}, còn 50 Hz chỉ {{nl_a50}}. Nhân với $\\cos(2\\pi\\,20t)$ (tuyến tính nhưng thay đổi theo thời gian): hai thành phần 30 Hz và 70 Hz biên độ {{tv_a30}} và {{tv_a70}}.||"
                 "A 50 Hz wave through a squarer (nonlinear): DC component {{nl_dc}}, a 100 Hz component of amplitude {{nl_a100}}, and only {{nl_a50}} left at 50 Hz. Multiplied by $\\cos(2\\pi\\,20t)$ (linear but time-varying): two components at 30 Hz and 70 Hz with amplitudes {{tv_a30}} and {{tv_a70}}.⟧</p>{{fig:linear_vs_nonlinear}}"),
                ("⟦Méo hài của một khuếch đại có số hạng bậc ba||Harmonic distortion of an amplifier with a cubic term⟧",
                 "<p>⟦Khâu $y=x+0.1x^3$ cho sóng 50 Hz: thành phần cơ bản {{cubic_fund}} và hài bậc ba tại 150 Hz là {{cubic_h3}}. Hệ số méo hài $\\text{THD}=A_3/A_1$ là {{cubic_thd_pct}}%.||"
                 "The stage $y=x+0.1x^3$ driven at 50 Hz gives a fundamental {{cubic_fund}} and a third harmonic at 150 Hz of {{cubic_h3}}. The total harmonic distortion $\\text{THD}=A_3/A_1$ is {{cubic_thd_pct}}%.⟧</p>"
                 + F("⟦Vì sao có hài bậc ba||Why a third harmonic appears⟧", r"\sin^3\theta=\tfrac34\sin\theta-\tfrac14\sin3\theta")),
                ("⟦Ba bẫy hay gặp khi nói \"tuyến tính\"||Three traps with the word \"linear\"⟧",
                 UL(["⟦Chỉ tuyến tính chưa đủ: bộ nhân $\\cos(2\\pi\\,20t)$ tuyến tính nhưng thay đổi theo thời gian, nên tạo tần số mới.||Linearity alone is not enough: the $\\cos(2\\pi\\,20t)$ multiplier is linear but time-varying, so it creates new frequencies.⟧",
                     "⟦Bất biến theo thời gian đôi khi còn đúng khi tuyến tính hỏng, còn bất biến theo không gian không phổ biến: độ võng cầu không được tách thành hình sin theo không gian (tr. 3).||Time invariance often survives when linearity fails, but space invariance is far less common: bridge deflection is not split into spatial sinusoids (p. 3).⟧",
                     "⟦Khi tính tuyến tính hỏng (servo phi tuyến), phải xem lại việc phân tích thành thành phần điều hòa (tr. 3).||When linearity fails (nonlinear servomechanism), harmonic analysis must be reconsidered (p. 3).⟧"])),
            ]),
        # ------------------------------------------------------------ PART 4
        dict(
            title="⟦Ký hiệu và hàm suy rộng||Notation and generalized functions⟧",
            scr=("⟦Các hàm như xung chữ nhật thường phải định nghĩa từng khúc, rất cồng kềnh.||Functions such as the rectangular pulse are usually defined piecewise, which is clumsy.⟧",
                 "⟦Hàm xung $\\delta(x)$ không phải hàm thông thường nhưng vẫn rất hữu ích.||The impulse $\\delta(x)$ is not an ordinary function yet it is enormously useful.⟧",
                 "⟦Dùng ký hiệu gọn và coi biểu thức chứa xung là giới hạn của dãy xung có bề rộng.||Use compact notation and treat any expression containing an impulse as the limit of a sequence of pulses of finite width.⟧"),
            preview=["⟦Bốn ký hiệu cốt lõi và cách dùng||Four core symbols and how to use them⟧",
                     "⟦Xung là giới hạn: bảng số||The impulse as a limit: a table of numbers⟧",
                     "⟦Hàm suy rộng và chương 5 đến 6||Generalized functions and chapters 5 to 6⟧"],
            slides=[
                ("⟦Bốn ký hiệu dùng xuyên suốt||Four symbols used throughout⟧",
                 TBL(["⟦Ký hiệu||Symbol⟧", "⟦Tên||Name⟧", "⟦Vai trò||Role⟧"],
                     [["$\\Pi(x)$", "⟦xung chữ nhật (\"hàm cổng\")||rectangle (\"gate\") function⟧", "⟦nhân vào dạng sóng để cắt lấy một đoạn||multiplied onto a waveform to gate out a segment⟧"],
                      ["$\\delta(x)$", "⟦ký hiệu xung||impulse symbol⟧", "⟦đáp ứng xung, tải điểm, điện tích điểm||impulse response, point load, point charge⟧"],
                      ["$\\text{III}(x)$", "⟦chuỗi xung (\"shah\")||impulse train (\"shah\")⟧", "⟦lấy mẫu đều và hàm tuần hoàn||regular sampling and periodic functions⟧"],
                      ["$f*g$", "⟦tích chập||convolution⟧", "⟦thay tích phân có biến giả bằng một ký hiệu gọn||replaces an integral with a dummy variable by a compact symbol⟧"]])),
                ("⟦Xung chữ nhật là \"hàm cổng\"||The rectangle is a \"gate\" function⟧",
                 "<p>⟦Xung chữ nhật đơn giản không kém xung Gauss, nên Bracewell đặt tên riêng $\\Pi(x)$. Tên \"hàm cổng\" của ngành điện tử gợi ý cách dùng: nhân $\\Pi(t)$ vào dạng sóng để mở van cho một đoạn đi qua (tr. 2).||"
                 "The rectangular pulse is at least as simple as a Gaussian pulse, so Bracewell gives it its own name $\\Pi(x)$. The electronics term \"gate function\" suggests the use: multiply a waveform by $\\Pi(t)$ to open a valve for one segment (p. 2).⟧</p>"
                 + F("⟦Xung chữ nhật||Rectangle function⟧", r"\Pi(x)=\begin{cases}1,&|x|<\tfrac12\\0,&|x|>\tfrac12\end{cases}")
                 + "<p>⟦Ví dụ: tích phân $\\int\\Pi(x)\\cos(\\pi x)\\,dx$ bằng {{gate_area}}, đúng $2/\\pi$.||Example: the integral $\\int\\Pi(x)\\cos(\\pi x)\\,dx$ equals {{gate_area}}, exactly $2/\\pi$.⟧</p>"),
                ("⟦Ký hiệu $*$ thay cho tích phân có biến giả||The asterisk replaces an integral with a dummy variable⟧",
                 "<p>⟦Viết $\\Pi*f$ hay $\\Pi(x)*f(x)$ thay cho $\\int_{x-1/2}^{x+1/2}f(u)\\,du$ chỉ là bước nhỏ, nhưng biến giả và cận biến mất, và bản chất \"trung bình trượt\" hiện ra (tr. 3). Với $f(u)=e^{-u^2}$ tại $x=0$: tích phân số cho {{run_mean_num}}, công thức $\\sqrt\\pi\\,\\text{erf}(1/2)$ cho {{run_mean_exact}}.||"
                 "Writing $\\Pi*f$ or $\\Pi(x)*f(x)$ for $\\int_{x-1/2}^{x+1/2}f(u)\\,du$ is a small step, but the dummy variable and limits vanish and the running-mean character shows (p. 3). For $f(u)=e^{-u^2}$ at $x=0$: numerical integration gives {{run_mean_num}}, the formula $\\sqrt\\pi\\,\\text{erf}(1/2)$ gives {{run_mean_exact}}.⟧</p>"),
                ("⟦Xung là giới hạn, không phải một hàm||The impulse is a limit, not a function⟧",
                 "<p>⟦Từ \"ký hiệu xung\" nhắc rằng $\\delta(x)$ không phải hàm. Biểu thức chứa nó có nghĩa như giới hạn của dãy xung (không phải xung nhọn) hẹp dần và cao dần, và giới hạn thường tồn tại (tr. 4).||"
                 "The term \"impulse symbol\" reminds us that $\\delta(x)$ is not a function. An expression containing it has meaning as the limit of a sequence of pulses (not impulses) growing narrower and taller, and that limit often exists (p. 4).⟧</p>"
                 + F("⟦Xung là giới hạn của xung chữ nhật diện tích 1||The impulse as a limit of unit-area rectangles⟧",
                     r"\delta_\varepsilon(x)=\frac1\varepsilon\Pi\!\left(\frac x\varepsilon\right),\quad\int\delta_\varepsilon\,dx=1,\quad \delta=\lim_{\varepsilon\to0}\delta_\varepsilon",
                     [(r"\varepsilon", "⟦bề rộng xung, cho tiến về 0||pulse width, made to approach 0⟧")])),
                ("⟦Thử số: xung \"lấy mẫu\" giá trị tại gốc||Numerical test: the impulse \"sifts\" the value at the origin⟧",
                 "<p>⟦Với $f=\\cos x$, tích phân $\\int f\\,\\delta_\\varepsilon\\,dx$ tiến dần tới $f(0)=1$ khi $\\varepsilon$ giảm:||"
                 "With $f=\\cos x$, the integral $\\int f\\,\\delta_\\varepsilon\\,dx$ approaches $f(0)=1$ as $\\varepsilon$ shrinks:⟧</p>"
                 + TBL(["$\\varepsilon$", "$\\int f\\,\\delta_\\varepsilon\\,dx$"], [["0.5", "{{sift_e05}}"], ["0.1", "{{sift_e01}}"], ["0.01", "{{sift_e001}}"]])
                 + "<p>⟦Đây là tính chất \"sàng\" (sifting) mà chương 5 phát triển.||This is the \"sifting\" property developed in chapter 5.⟧</p>{{fig:impulse_limit}}"),
                ("⟦Vì sao gọi là \"ký hiệu\" xung||Why it is called an impulse \"symbol\"⟧",
                 "<p>⟦Trong vật lý, hàm Green và đáp ứng xung thường tạo ra hoặc quan sát được, trong giới hạn phân giải của thiết bị đo, còn xung thật thì hư cấu. Ví dụ quen thuộc là mô men do một khối điểm đặt trên dầm, hay điện trường của điện tích điểm (tr. 4).||"
                 "In physics, Green's functions and impulse responses can often be produced or observed within the resolving power of the equipment, while impulses themselves are fictitious. Familiar examples are the moment produced by a point mass on a beam and the electric field of a point charge (p. 4).⟧</p>"),
                ("⟦Chuỗi xung $\\text{III}$ (shah): lấy mẫu và tuần hoàn||The impulse train $\\text{III}$ (shah): sampling and periodicity⟧",
                 "<p>⟦Shah được định nghĩa là $\\text{III}(x)=\\sum_n\\delta(x-n)$. Lấy mẫu đều (tra bảng) tương đương nhân với shah, còn hàm tuần hoàn biểu diễn được bằng tích chập với shah. Vì shah là biến đổi Fourier của chính nó, nó hữu ích gấp đôi mong đợi (tr. 2 đến 3).||"
                 "Shah is defined as $\\text{III}(x)=\\sum_n\\delta(x-n)$. Regular sampling (tabulation) is multiplication by shah, and periodic functions are convolutions with shah. Since shah is its own Fourier transform, it is twice as useful as might be expected (pp. 2 to 3).⟧</p>"
                 + F("⟦Shah||Shah⟧", r"\text{III}(x)=\sum_{n=-\infty}^{\infty}\delta(x-n),\qquad \mathcal F\{\text{III}\}=\text{III}")),
                ("⟦Hàm suy rộng: chương 5 và 6||Generalized functions: chapters 5 and 6⟧",
                 "<p>⟦Bracewell chọn cách trình bày bằng \"hàm suy rộng\" theo Temple và Lighthill (chương 5 và 6). Nhờ đó ta giữ được cả tính chặt chẽ lẫn cách thao tác trực tiếp với $\\delta$ vốn rất hiệu quả (tr. 4).||"
                 "Bracewell prefers the presentation through \"generalized functions\" following Temple and Lighthill (chapters 5 and 6). It retains both rigor and the direct procedures of manipulating $\\delta$ that have been so successful (p. 4).⟧</p>"
                 + C("info", "⟦Trong khóa này||In this course⟧", "<p>⟦Module 5 xây dựng $\\delta$ và $\\text{III}$ chi tiết. Barkat cũng dùng hàm bước và xung ở mục 1.3.1 để viết mật độ xác suất của biến ngẫu nhiên rời rạc (module 10).||Module 5 builds $\\delta$ and $\\text{III}$ in detail. Barkat also uses step and impulse functions in section 1.3.1 to write the density of a discrete random variable (module 10).⟧</p>")),
            ]),
        # ------------------------------------------------------------ PART 5
        dict(
            title="⟦Bản đồ hai giáo trình và cách làm việc bằng số||Map of the two books and working numerically⟧",
            scr=("⟦Bạn sắp đi qua 26 module lấy từ hai giáo trình có mục tiêu khác nhau.||You are about to cross 26 modules drawn from two books with different aims.⟧",
                 "⟦Không có bản đồ thì rất dễ lạc, và \"biến đổi\" dễ bị hiểu nhầm là luôn phải tính số.||Without a map it is easy to get lost, and \"transform\" is easily mistaken for something you must always compute numerically.⟧",
                 "⟦Có lộ trình theo phần A đến E, biết chỗ hai sách gặp nhau, và một quy trình kiểm số cố định.||There is a route through parts A to E, you know where the two books meet, and a fixed routine for checking numbers.⟧"),
            preview=["⟦Bracewell và Barkat: hai giáo trình gốc||Bracewell and Barkat: the two source books⟧",
                     "⟦Năm phần A đến E||Five parts, A to E⟧",
                     "⟦Tư duy biến đổi khác với tính biến đổi||Thinking in transforms is not computing them⟧",
                     "⟦Quy trình kiểm số của khóa||This course's routine for checking numbers⟧"],
            slides=[
                ("⟦Hai giáo trình gốc||The two source books⟧",
                 TBL(["", "Bracewell", "Barkat"],
                     [["⟦Tên||Title⟧", "<i>The Fourier Transform and Its Applications</i>", "<i>Signal Detection and Estimation</i>"],
                      ["⟦Chương nội dung||Content chapters⟧", "19", "12"],
                      ["⟦Trọng tâm||Focus⟧", "⟦biến đổi, tích chập, lấy mẫu, phổ||transforms, convolution, sampling, spectra⟧", "⟦xác suất, quá trình ngẫu nhiên, phát hiện, ước lượng||probability, random processes, detection, estimation⟧"],
                      ["⟦Ngôn ngữ chính||Main language⟧", "⟦hàm tất định||deterministic functions⟧", "⟦biến và quá trình ngẫu nhiên||random variables and processes⟧"]])),
                ("⟦26 module: 4 chung, 15 riêng Bracewell, 7 riêng Barkat||26 modules: 4 shared, 15 Bracewell only, 7 Barkat only⟧",
                 "<p>⟦Mỗi chương là một module. Bốn cặp chương có cùng chủ đề được ghép làm một module dài hơn (khoảng 60 slide thay vì 40):||Each chapter is a module. Four pairs of chapters on the same topic are merged into one longer module (about 60 slides instead of 40):⟧</p>"
                 + TBL(["⟦Module||Module⟧", "Bracewell", "Barkat", "⟦Chủ đề chung||Shared topic⟧"],
                       [["10", "16", "1", "⟦xác suất qua hàm đặc trưng||probability through the characteristic function⟧"],
                        ["12", "17", "3", "⟦quá trình ngẫu nhiên, nhiễu, phổ công suất||random processes, noise, power spectrum⟧"],
                        ["13", "10", "8", "⟦lấy mẫu, chuỗi Fourier, khai triển trực giao||sampling, Fourier series, orthogonal expansions⟧"],
                        ["14", "11", "4", "⟦DFT/FFT và quá trình rời rạc||DFT/FFT and discrete-time processes⟧"]])),
                ("⟦Năm phần A đến E||Five parts, A to E⟧",
                 TBL(["⟦Phần||Part⟧", "⟦Module||Modules⟧", "⟦Nội dung||Content⟧"],
                     [["A", "1 – 9", "⟦nền tảng Fourier: tích chập, xung, các định lý, bộ lọc||Fourier foundations: convolution, impulse, theorems, filters⟧"],
                      ["B", "10 – 12", "⟦xác suất, phân phối, quá trình ngẫu nhiên và nhiễu||probability, distributions, random processes and noise⟧"],
                      ["C", "13 – 17", "⟦lấy mẫu, DFT/FFT, Hartley, họ hàng Fourier, Laplace||sampling, DFT/FFT, Hartley, relatives of Fourier, Laplace⟧"],
                      ["D", "18 – 20", "⟦ăng-ten và quang học, khuếch tán, phổ động||antennas and optics, diffusion, dynamic spectra⟧"],
                      ["E", "21 – 26", "⟦quyết định thống kê, ước lượng, lọc, phát hiện, CFAR||statistical decision, estimation, filtering, detection, CFAR⟧"]])),
                ("⟦Tư duy biến đổi khác với tính biến đổi||Thinking in transforms is not computing them⟧",
                 "<p>⟦Phương pháp biến đổi không nhất thiết đòi tính biến đổi bằng số. Một số phương pháp tốt nhất cho bài toán tuyến tính không áp dụng biến đổi lên dữ liệu, nhưng cơ sở của chúng được làm sáng tỏ nhờ miền biến đổi (tr. 3).||"
                 "Transform methods do not necessarily involve taking transforms numerically. Some of the best methods for linear problems do not apply the transform to the data at all, though their basis is clarified by appeal to the transform domain (p. 3).⟧</p>"
                 "<p>⟦Với tính số, ta thường thích đáp án hiện ra dưới dạng tích chập của hai hàm hơn là một biến đổi Fourier (tr. 3). Đó là lý do module 3 đứng ngay trước bộ định lý.||"
                 "For numerical work one normally prefers the answer as the convolution of two functions rather than as a Fourier transform (p. 3). That is why module 3 comes right before the theorems.⟧</p>"),
                ("⟦Quy trình kiểm số của khóa: hai phương pháp độc lập||This course's routine: two independent methods⟧",
                 UL(["⟦Mọi con số trên trang được notebook in ra, không gõ tay.||Every number on the page is printed by the notebook, never typed by hand.⟧",
                     "⟦Mỗi số được tính bằng ít nhất hai phương pháp độc lập (ví dụ FFT và tổng trực tiếp, tích phân số và công thức đóng), và notebook dừng nếu chúng lệch nhau.||Each number is computed by at least two independent methods (for example FFT and direct sum, numerical integral and closed form), and the notebook stops if they disagree.⟧",
                     "⟦Bản tiếng Việt và tiếng Anh dùng cùng mã, và phải in ra đúng cùng các số.||The Vietnamese and English editions use the same code and must print exactly the same numbers.⟧"])
                 + "<p>⟦Ví dụ ngay trong module này: FFT và tổng trực tiếp lệch {{fft_direct_diff}}; bộ lọc tích chập và <code>lfilter</code> lệch {{conv_lfilter_diff}}.||Examples from this very module: FFT and direct sum differ by {{fft_direct_diff}}; the convolution filter and <code>lfilter</code> differ by {{conv_lfilter_diff}}.⟧</p>"),
                ("⟦Cách học một module||How to study a module⟧",
                 OL(["⟦Đọc mục tiêu và duyệt các slide theo 5 phần. Dùng danh sách chọn slide để nhảy.||Read the objectives and step through the slides in 5 parts. Use the slide list to jump.⟧",
                     "⟦Đọc mục lịch sử, case study và bảng công thức.||Read the history, the case study and the formula sheet.⟧",
                     "⟦Mở notebook, chạy từng cell, đọc phần \"Đầu ra thật\" sau mỗi cell rồi tự đổi tham số.||Open the notebook, run each cell, read the \"Real output\" note after it, then change the parameters yourself.⟧",
                     "⟦Làm quiz, đọc giải thích các câu sai, quay lại slide tương ứng.||Take the quiz, read the explanations of wrong answers, and return to the matching slides.⟧"])),
                ("⟦Bảng ký hiệu và quy ước của giáo trình||Notation and conventions of the book⟧",
                 TBL(["⟦Ký hiệu||Symbol⟧", "⟦Ý nghĩa||Meaning⟧"],
                     [["$x,\\ s$", "⟦biến gốc và biến tần số (chu kỳ trên đơn vị)||original variable and frequency variable (cycles per unit)⟧"],
                      ["$f(x)\\supset F(s)$", "⟦cặp biến đổi Fourier||a Fourier transform pair⟧"],
                      ["$\\Pi,\\ \\Lambda$", "⟦xung chữ nhật, xung tam giác||rectangle, triangle⟧"],
                      ["$H(x),\\ \\text{sgn}\\,x$", "⟦hàm bậc thang đơn vị, hàm dấu||unit step, sign function⟧"],
                      ["$\\text{sinc}\\,x$", "$\\sin(\\pi x)/(\\pi x)$"],
                      ["$\\delta,\\ \\text{III}$", "⟦xung, chuỗi xung (shah)||impulse, impulse train (shah)⟧"],
                      ["$*$", "⟦tích chập||convolution⟧"]])),
                ("⟦Tự kiểm tra phần 5||Self-check, part 5⟧",
                 UL(["⟦Chương nào của Bracewell và Barkat được ghép để dạy về quá trình ngẫu nhiên và nhiễu?||Which chapters of Bracewell and Barkat are merged to teach random processes and noise?⟧",
                     "⟦Vì sao \"tư duy biến đổi\" không có nghĩa là luôn phải tính FFT?||Why does \"thinking in transforms\" not mean you must always compute an FFT?⟧",
                     "⟦Nếu FFT và tổng trực tiếp lệch nhau nhiều, bạn làm gì trước khi tin con số?||If the FFT and the direct sum disagree by a lot, what do you do before trusting the number?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: chương 17 và chương 3; vì đôi khi đáp án ra thẳng dạng tích chập; điều tra nguyên nhân tới cùng.||Hints: chapter 17 and chapter 3; because the answer sometimes comes out directly as a convolution; investigate the cause to the end.⟧</p>"),
            ]),
    ],
    takeaways=[
        "⟦Biến đổi là công cụ: đổi miền, giải, đổi ngược.||A transform is a tool: change domain, solve, change back.⟧",
        "⟦Dạng sóng và phổ mang cùng thông tin (bảo toàn năng lượng), và cả hai đo được.||A waveform and its spectrum carry the same information (energy is conserved), and both are measurable.⟧",
        "⟦Đọc phổ cần chú ý độ phân giải $f_s/N$, rò phổ và pha.||Reading a spectrum needs care with the resolution $f_s/N$, leakage and phase.⟧",
        "⟦Sóng điều hòa vào cho sóng điều hòa ra cùng tần số khi hệ tuyến tính và bất biến; khi đó đáp ứng là một tích chập.||A harmonic input gives a harmonic output at the same frequency when the system is linear and invariant; the response is then a convolution.⟧",
        "⟦$\\delta(x)$ là giới hạn của dãy xung, không phải hàm thông thường.||$\\delta(x)$ is a limit of pulse sequences, not an ordinary function.⟧",
        "⟦Khóa có 26 module, ghép hai giáo trình, và mọi số liệu đều được kiểm bằng hai phương pháp.||The course has 26 modules pairing two books, and every number is checked by two methods.⟧",
    ],
    history="<p>⟦Joseph Fourier sinh ngày 21/3/1768 và mất ngày 16/5/1830 (trang đầu sách). Lord Kelvin viết rằng định lý Fourier không chỉ là một trong những kết quả đẹp nhất của giải tích hiện đại mà còn là công cụ không thể thiếu khi xử lý hầu như mọi vấn đề sâu của vật lý hiện đại (lời đề từ của Bracewell).||"
            "Joseph Fourier lived from 21 March 1768 to 16 May 1830 (frontispiece). Lord Kelvin wrote that Fourier's theorem is not only one of the most beautiful results of modern analysis but also furnishes an indispensable instrument in the treatment of nearly every recondite question in modern physics (Bracewell's epigraph).⟧</p>"
            "<p>⟦Ronald Bracewell là giáo sư kỹ thuật điện tại Stanford, người thiết kế kính thiên văn vô tuyến và dùng phân tích Fourier trong cả thiết kế thiết bị lẫn xử lý dữ liệu, kể cả chụp cắt lớp (phần giới thiệu tác giả). Vì vậy giáo trình đặt trọng tâm vào diễn giải vật lý.||"
            "Ronald Bracewell was a professor of electrical engineering at Stanford who designed radio telescopes and used Fourier analysis in both instrument design and data processing, including tomographic imaging (author's note). That is why the book puts its weight on physical interpretation.⟧</p>"
            "<p>⟦Bracewell cũng cho biết cuốn sách khởi đầu như một bộ tranh minh họa các cặp biến đổi, rồi phần bình luận nhanh chóng vượt về giá trị (tr. 2). Bạn sẽ dùng bộ tranh đó (chương 22) ở nhiều module sau.||"
            "Bracewell also reports that the book began as a pictorial guide to transform pairs, and the commentary quickly outweighed the pictures in value (p. 2). You will use that pictorial dictionary (chapter 22) in many later modules.⟧</p>",
    case="<p>⟦<b>Bộ khuếch đại bị méo.</b> Bộ khuếch đại lý tưởng là hệ tuyến tính: sóng 50 Hz vào thì chỉ có sóng 50 Hz ra. Nếu một tầng có đặc tính bình phương (mô hình đơn giản của méo phi tuyến), phổ ngõ ra có thành phần một chiều {{nl_dc}} và hài bậc hai 100 Hz biên độ {{nl_a100}}, còn thành phần gốc 50 Hz gần như biến mất ({{nl_a50}}). Với tầng có số hạng bậc ba $y=x+0.1x^3$, phổ có hài bậc ba {{cubic_h3}} và THD {{cubic_thd_pct}}%. Chỉ cần nhìn phổ là biết hệ đã phi tuyến, không cần biết mạch bên trong.||"
          "<b>A distorting amplifier.</b> An ideal amplifier is a linear system: a 50 Hz wave in gives only a 50 Hz wave out. If one stage has a square-law characteristic (a simple model of nonlinear distortion), the output spectrum shows a DC component {{nl_dc}} and a second harmonic at 100 Hz of amplitude {{nl_a100}}, while the original 50 Hz component almost vanishes ({{nl_a50}}). With a cubic term $y=x+0.1x^3$ the spectrum has a third harmonic {{cubic_h3}} and a THD of {{cubic_thd_pct}}%. Looking at the spectrum alone tells you the system is nonlinear, without knowing the circuit inside.⟧</p>"
         "<p>⟦Đây là cách kỹ sư đo méo: đưa vào sóng hình sin sạch, đọc phổ ra, và mọi vạch phổ ngoài tần số vào là dấu hiệu của phi tuyến hoặc của hệ thay đổi theo thời gian.||"
         "This is how engineers measure distortion: feed in a clean sinusoid, read the output spectrum, and any line away from the input frequency signals nonlinearity or time variation.⟧</p>",
    practice=[
        "⟦Mở notebook và chạy cell cài đặt (cần NumPy, Matplotlib và SciPy).||Open the notebook and run the setup cell (NumPy, Matplotlib and SciPy are needed).⟧",
        "⟦Bài 1: tạo tín hiệu ba sóng hình sin, tính phổ bằng FFT và bằng tổng trực tiếp, xác nhận hai kết quả trùng nhau. Thử tần số 50.5 Hz để thấy rò phổ.||Task 1: build the three-sinusoid signal, compute the spectrum by FFT and by direct sum, and confirm they agree. Try 50.5 Hz to see leakage.⟧",
        "⟦Bài 2: kiểm bảo toàn năng lượng và tích chập nối tiếp $\\{2,2,3,3,4\\}*\\{1,1,2\\}$ bằng hai cách.||Task 2: check energy conservation and the serial product $\\{2,2,3,3,4\\}*\\{1,1,2\\}$ two ways.⟧",
        "⟦Bài 3: cho sóng qua bộ lọc thông thấp, so độ lợi và pha đo bằng FFT với công thức, rồi thử khâu bình phương, khâu bậc ba và bộ nhân cosin.||Task 3: pass a wave through a low-pass filter, compare the gain and phase measured by FFT with the formula, then try the squarer, the cubic stage and the cosine multiplier.⟧",
        "⟦Bài 4: kiểm bảng \"sàng\" của xung với $\\varepsilon=0.5,\\ 0.1,\\ 0.01$, rồi tự thử $f=x^2+1$ và dự đoán trước kết quả.||Task 4: check the sifting table of the impulse for $\\varepsilon=0.5,\\ 0.1,\\ 0.01$, then try $f=x^2+1$ yourself and predict the result first.⟧",
    ],
    pitfalls=[
        "<b>⟦\"$\\sin t$, bước nhảy và xung đều có biến đổi Fourier.\"||\"$\\sin t$, the step and the impulse all have Fourier transforms.\"⟧</b><p>⟦Nói chặt chẽ thì cả ba không có: tích phân Fourier không hội tụ với mọi $s$ (tr. 8). Về mặt vật lý chúng không thể tạo ra và ta dùng chúng như xấp xỉ gọn. Module 2 xử lý bằng \"biến đổi trong giới hạn\".||Strictly speaking none of the three has one: the Fourier integral does not converge for all $s$ (p. 8). They are not physically realizable and are used as convenient approximations. Module 2 handles them as \"transforms in the limit\".⟧</p>",
        "<b>⟦\"Chỉ cần hệ tuyến tính là sóng hình sin vào cho sóng hình sin ra.\"||\"Linearity alone guarantees a sinusoid out for a sinusoid in.\"⟧</b><p>⟦Cần cả bất biến theo thời gian. Bộ nhân với $\\cos(2\\pi\\,20t)$ là tuyến tính nhưng thay đổi theo thời gian, và biến sóng 50 Hz thành hai thành phần {{tv_a30}} tại 30 Hz và {{tv_a70}} tại 70 Hz.||Time invariance is needed too. The multiplier by $\\cos(2\\pi\\,20t)$ is linear but time-varying, and it turns a 50 Hz wave into two components, {{tv_a30}} at 30 Hz and {{tv_a70}} at 70 Hz.⟧</p>",
        "<b>⟦\"Biên độ tại ô FFT luôn bằng biên độ sóng.\"||\"The FFT bin amplitude always equals the wave amplitude.\"⟧</b><p>⟦Chỉ đúng khi tần số rơi đúng vào một ô. Sóng 50.5 Hz cho {{leak_peak}} thay vì 1, và phổ rò tới cả những ô xa.||Only true when the frequency falls exactly on a bin. A 50.5 Hz wave gives {{leak_peak}} instead of 1, and the spectrum leaks even into far bins.⟧</p>",
        "<b>⟦\"Phân tích thành hài hòa luôn dùng được cho mọi hệ vật lý.\"||\"Harmonic analysis works for every physical system.\"⟧</b><p>⟦Khi tính tuyến tính hỏng, như trong servo phi tuyến, phải xem lại việc tách thành thành phần điều hòa. Bất biến theo không gian cũng không phổ biến, vì thế độ võng của cầu không được nghiên cứu bằng cách tách tải thành thành phần hình sin theo không gian (tr. 3).||When linearity fails, as in a nonlinear servomechanism, the analysis into harmonic components must be reconsidered. Space invariance is also far less common, which is why bridge deflections are not studied by splitting the load into sinusoidal space components (p. 3).⟧</p>",
    ],
    refs=[
        "⟦R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chương 1 (tr. 1 đến 4), chương 2 (tr. 5 đến 8), chương 3 (tr. 24, 30 đến 34) và lời đề từ.||R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chapter 1 (pp. 1 to 4), chapter 2 (pp. 5 to 8), chapter 3 (pp. 24, 30 to 34) and epigraph.⟧",
        "⟦M. Barkat, <i>Signal Detection and Estimation</i>, 2nd ed., Artech House, 2005, mục 1.3.1 (hàm bước và xung) và mục lục chương 1 đến 12.||M. Barkat, <i>Signal Detection and Estimation</i>, 2nd ed., Artech House, 2005, section 1.3.1 (step and impulse functions) and the table of contents of chapters 1 to 12.⟧",
    ],
    quiz=[
        dict(q="⟦Theo Bracewell, vì sao học Fourier trước rồi mới tới Laplace?||According to Bracewell, why is Fourier studied before Laplace?⟧",
             opts=["⟦Nhiều tính chất đã quen, chỉ còn học thêm dải hội tụ||Many properties are familiar, leaving only the strip of convergence⟧",
                   "⟦Vì Fourier bao hàm Laplace như trường hợp riêng nên không cần chứng minh gì thêm về Laplace||Because Fourier contains Laplace as a special case, so nothing more about Laplace needs proving⟧",
                   "⟦Vì Laplace chỉ xử lý được tín hiệu rời rạc, nên tín hiệu liên tục phải đi qua Fourier trước||Because Laplace only handles discrete signals, so continuous signals must go through Fourier first⟧",
                   "⟦Vì Laplace buộc phải dùng máy tính để tính còn Fourier luôn làm tay được với mọi dạng sóng||Because Laplace must be evaluated by computer while Fourier can always be done by hand for any waveform⟧"],
             explain="⟦Bracewell, tr. 1: khi Laplace được bàn sau, nhiều tính chất đã quen và không gây xao nhãng câu hỏi mới và thiết yếu về dải hội tụ.||Bracewell, p. 1: when Laplace is discussed later many properties are already familiar and do not distract from the new and essential question of the strip of convergence.⟧"),
        dict(q="⟦Hai điều kiện nào bảo đảm đáp ứng với sóng điều hòa vẫn là sóng điều hòa cùng tần số?||Which two conditions guarantee that a harmonic input gives a harmonic output at the same frequency?⟧",
             opts=["⟦Tuyến tính và bất biến theo thời gian||Linearity and time invariance⟧",
                   "⟦Ổn định trong nghĩa BIBO và tín hiệu vào có năng lượng hữu hạn trên toàn trục thời gian||BIBO stability and an input signal with finite energy over the whole time axis⟧",
                   "⟦Nhân quả và tín hiệu vào là hàm chẵn theo thời gian, để phổ ra luôn là số thực||Causality and an even input signal, so that the output spectrum is always real⟧",
                   "⟦Đáp ứng xung luôn dương và tần số vào đủ thấp so với tần số lấy mẫu của hệ||A positive impulse response and an input frequency low enough compared with the system sampling rate⟧"],
             explain="⟦Bracewell, tr. 3: cần tuyến tính và bất biến theo thời gian. Ổn định hay nhân quả không phải điều kiện của phát biểu này.||Bracewell, p. 3: linearity and time invariance are needed. Stability and causality are not conditions of this statement.⟧"),
        dict(q="⟦Bộ lọc $y[n]=0.9\\,y[n-1]+0.1\\,x[n]$ nhận sóng 50 Hz (lấy mẫu 1000 Hz). Sóng ra có tần số nào?||The filter $y[n]=0.9\\,y[n-1]+0.1\\,x[n]$ receives a 50 Hz wave (sampled at 1000 Hz). Which frequency does the output have?⟧",
             opts=["{{f_out}} Hz", "100 Hz", "25 Hz", "500 Hz"],
             explain="⟦Hệ tuyến tính bất biến giữ nguyên tần số; notebook đọc đỉnh phổ ra tại {{f_out}} Hz.||A linear invariant system preserves frequency; the notebook reads the output spectral peak at {{f_out}} Hz.⟧"),
        dict(q="⟦Đưa sóng 50 Hz qua khâu bình phương $y=x^2$. Phổ ra có gì?||A 50 Hz wave goes through a squarer $y=x^2$. What does the output spectrum contain?⟧",
             opts=["⟦Thành phần một chiều và 100 Hz, hầu như hết 50 Hz||DC and 100 Hz, with almost nothing left at 50 Hz⟧",
                   "⟦Chỉ còn thành phần 50 Hz nhưng biên độ giảm đi một nửa do phép bình phương làm nhỏ tín hiệu||Only the 50 Hz component remains, with half its amplitude, because squaring shrinks the signal⟧",
                   "⟦Một dải liên tục quanh 50 Hz với biên độ giảm dần vì bình phương làm rộng phổ||A continuous band around 50 Hz with decaying amplitude, because squaring broadens the spectrum⟧",
                   "⟦Thành phần 50 Hz và thành phần 25 Hz cùng biên độ, vì bình phương chia đôi tần số||Components at 50 Hz and 25 Hz with equal amplitude, because squaring halves the frequency⟧"],
             explain="⟦$\\sin^2 = \\tfrac12-\\tfrac12\\cos 2\\theta$. Notebook đo một chiều {{nl_dc}}, 100 Hz {{nl_a100}}, 50 Hz {{nl_a50}}.||$\\sin^2 = \\tfrac12-\\tfrac12\\cos 2\\theta$. The notebook measures DC {{nl_dc}}, 100 Hz {{nl_a100}}, 50 Hz {{nl_a50}}.⟧"),
        dict(q="⟦Bộ nhân $y(t)=x(t)\\cos(2\\pi\\,20t)$ là hệ nào?||What kind of system is the multiplier $y(t)=x(t)\\cos(2\\pi\\,20t)$?⟧",
             opts=["⟦Tuyến tính nhưng thay đổi theo thời gian, nên tạo tần số mới||Linear but time-varying, so it creates new frequencies⟧",
                   "⟦Phi tuyến nhưng bất biến theo thời gian, nên nó giữ nguyên tần số của tín hiệu vào||Nonlinear but time-invariant, so it keeps the frequency of the input signal⟧",
                   "⟦Vừa tuyến tính vừa bất biến, vì vậy tần số ra luôn bằng đúng tần số vào của hệ||Both linear and invariant, so the output frequency always equals the input frequency⟧",
                   "⟦Không phải một hệ, vì phép nhân với hàm cho trước không có đáp ứng xung để mô tả||Not a system at all, because multiplying by a given function has no impulse response to describe⟧"],
             explain="⟦Nhân với hàm thay đổi theo thời gian là tuyến tính (cộng và nhân hằng số đều bảo toàn) nhưng không bất biến. Notebook thấy {{tv_a30}} tại 30 Hz và {{tv_a70}} tại 70 Hz.||Multiplying by a time-varying function is linear (sums and constant factors are preserved) but not invariant. The notebook sees {{tv_a30}} at 30 Hz and {{tv_a70}} at 70 Hz.⟧"),
        dict(q="⟦Đáp ứng của một hệ tuyến tính bất biến liên hệ với kích thích bằng phép nào?||By which operation is the response of a linear invariant system related to the stimulus?⟧",
             opts=["⟦Tích chập với đáp ứng xung||Convolution with the impulse response⟧",
                   "⟦Nhân từng điểm kích thích với đáp ứng xung rồi lấy giá trị trung bình theo thời gian||Pointwise multiplication of the stimulus by the impulse response, then a time average⟧",
                   "⟦Lấy đạo hàm của kích thích theo thời gian rồi nhân với hệ số khuếch đại của hệ||Differentiating the stimulus with respect to time and then scaling by the gain of the system⟧",
                   "⟦Cộng kích thích với bản sao dịch thời gian của chính nó, mỗi bản có trọng số riêng||Adding the stimulus to time-shifted copies of itself, each with its own weight⟧"],
             explain="⟦Bracewell, tr. 3: hai điều kiện gộp thành một, đáp ứng liên hệ với kích thích bằng tích chập.||Bracewell, p. 3: the two conditions merge into one, the response is relatable to the stimulus by convolution.⟧"),
        dict(q="⟦Bracewell đề xuất đảo thứ tự trình bày truyền thống như thế nào?||How does Bracewell propose to reverse the traditional order of presentation?⟧",
             opts=["⟦Học biến đổi Fourier trước, chuỗi Fourier là trường hợp cực đoan||Study the Fourier transform first, with the series as an extreme case⟧",
                   "⟦Học chuỗi Fourier thật kỹ trước, sau đó biến đổi Fourier chỉ là bài tập nhỏ ở cuối phần||Study Fourier series in depth first, so the transform is only a short exercise at the end⟧",
                   "⟦Học Laplace trước vì đơn giản hơn, rồi thu về trục ảo để có Fourier như một hệ quả||Study Laplace first because it is simpler, then restrict to the imaginary axis to obtain Fourier⟧",
                   "⟦Học phép tính số trước, rồi mới học ý nghĩa vật lý của phổ khi đã quen với FFT||Study numerical computation first and the physical meaning of the spectrum once FFT is familiar⟧"],
             explain="⟦Bracewell, tr. 2: nếu đảo thứ tự thông thường, chuỗi Fourier trở thành trường hợp cực đoan trong khuôn khổ biến đổi Fourier.||Bracewell, p. 2: reversing the customary order lets the Fourier series fall into place as an extreme case within Fourier transform theory.⟧"),
        dict(q="⟦Về bản chất, $\\delta(x)$ trong giáo trình là gì?||What is $\\delta(x)$ in the book, in essence?⟧",
             opts=["⟦Ký hiệu có nghĩa qua giới hạn của dãy xung hẹp dần||A symbol whose meaning comes from a limit of narrowing pulses⟧",
                   "⟦Một hàm bình thường bằng vô cùng tại gốc và bằng 0 ở mọi nơi khác, có diện tích bằng 1||An ordinary function equal to infinity at the origin and zero elsewhere, with area equal to 1⟧",
                   "⟦Một hàm liên tục có diện tích 1 và bề rộng đúng bằng 0, được định nghĩa bằng tích phân Riemann||A continuous function of area 1 and width exactly 0, defined through the Riemann integral⟧",
                   "⟦Một hằng số bằng 1 tại gốc và không xác định ở nơi khác, chỉ dùng trong lý thuyết chuỗi||A constant equal to 1 at the origin and undefined elsewhere, used only in series theory⟧"],
             explain="⟦Bracewell, tr. 4: \"ký hiệu xung\" nhấn mạnh $\\delta$ không phải hàm; ý nghĩa nằm ở giới hạn của dãy xung.||Bracewell, p. 4: the term \"impulse symbol\" stresses that $\\delta$ is not a function; the meaning lies in the limit of pulse sequences.⟧"),
        dict(q="⟦$\\text{III}(x)$ (\"shah\") là gì và dùng để làm gì?||What is $\\text{III}(x)$ (\"shah\") and what is it used for?⟧",
             opts=["⟦Chuỗi xung $\\sum_n\\delta(x-n)$, dùng để lấy mẫu và biểu diễn hàm tuần hoàn||The impulse train $\\sum_n\\delta(x-n)$, used for sampling and periodic functions⟧",
                   "⟦Một xung chữ nhật rộng 3 đơn vị, dùng làm cửa sổ để cắt lấy một đoạn của tín hiệu||A rectangular pulse 3 units wide, used as a window that gates out a segment of the signal⟧",
                   "⟦Hàm bậc thang đơn vị, dùng để biểu diễn tín hiệu được bật lên tại thời điểm bằng 0||The unit step function, used to represent a signal that is switched on at time zero⟧",
                   "⟦Đạo hàm bậc ba của hàm Gauss, dùng để phát hiện biên trong xử lý ảnh số||The third derivative of the Gaussian, used to detect edges in digital image processing⟧"],
             explain="⟦Bracewell, tr. 2 đến 3: lấy mẫu tương đương phép nhân với shah, hàm tuần hoàn là tích chập với shah, và shah là biến đổi Fourier của chính nó.||Bracewell, pp. 2 to 3: sampling is multiplication by shah, periodic functions are convolutions with shah, and shah is its own Fourier transform.⟧"),
        dict(q="⟦Vì sao độ võng của cầu không được nghiên cứu bằng cách tách tải thành thành phần hình sin theo không gian?||Why are bridge deflections not studied by splitting the load into sinusoidal space components?⟧",
             opts=["⟦Bất biến theo không gian không đúng với cầu||Space invariance fails for a bridge⟧",
                   "⟦Tải trên cầu luôn là hàm không khả tích tuyệt đối nên hoàn toàn không có biến đổi Fourier||The load on a bridge is always a non-absolutely-integrable function with no Fourier transform at all⟧",
                   "⟦Độ võng của cầu là một đại lượng phức nên không thể phân tích hài hòa theo bất kỳ biến nào||Bridge deflection is a complex quantity, so it cannot be harmonically analysed in any variable⟧",
                   "⟦Sóng hình sin theo không gian không tồn tại trong cơ học vật rắn của các kết cấu thực||Spatial sinusoids do not exist in the solid mechanics of real structures⟧"],
             explain="⟦Bracewell, tr. 3: bất biến theo thời gian thường còn đúng ngay cả khi tuyến tính hỏng, nhưng bất biến theo không gian thì không phổ biến như vậy.||Bracewell, p. 3: time invariance can often be counted on even when linearity fails, but space invariance is by no means as common.⟧"),
        dict(q="⟦Notebook đo được biên độ FFT tại 120 Hz của tín hiệu ba sóng hình sin là bao nhiêu?||What FFT amplitude does the notebook measure at 120 Hz for the three-sinusoid signal?⟧",
             opts=["{{a120}}", "{{a50}}", "{{a300}}", "0.707107"],
             explain="⟦Thành phần 120 Hz được tạo với biên độ 0.5. Biên độ 1.0 thuộc 50 Hz và 0.25 thuộc 300 Hz.||The 120 Hz component was built with amplitude 0.5. Amplitude 1.0 belongs to 50 Hz and 0.25 to 300 Hz.⟧"),
        dict(q="⟦Bracewell nói gì về việc tính biến đổi bằng số?||What does Bracewell say about computing transforms numerically?⟧",
             opts=["⟦Không nhất thiết phải tính biến đổi bằng số||Numerical transforms are not always needed⟧",
                   "⟦Mọi bài toán tuyến tính đều bắt buộc phải tính biến đổi Fourier bằng số thì mới giải được||Every linear problem must be solved by computing a numerical Fourier transform⟧",
                   "⟦Tính biến đổi bằng số luôn nhanh hơn tích chập trực tiếp nên nên luôn được ưu tiên dùng||Numerical transforms are always faster than direct convolution and should always be preferred⟧",
                   "⟦Tính số chỉ đáng tin khi dữ liệu là hàm chẵn có đối xứng hoàn hảo quanh gốc thời gian||Numerical work is only trustworthy when the data is an even function perfectly symmetric about the origin⟧"],
             explain="⟦Bracewell, tr. 3: một số phương pháp tốt nhất không áp dụng biến đổi lên dữ liệu; về tính số, người ta thường thích đáp án ra dưới dạng tích chập hơn.||Bracewell, p. 3: some of the best methods do not apply the transform to the data; for numerical work one normally prefers the answer as a convolution.⟧"),
        dict(q="⟦Tích chập nối tiếp $\\{2,2,3,3,4\\}*\\{1,1,2\\}$ cho dãy nào?||Which sequence is the serial product $\\{2,2,3,3,4\\}*\\{1,1,2\\}$?⟧",
             opts=["{{conv_direct}}", "⟦2 4 9 10 13 10 8 14 (thêm một số hạng cuối, vì độ dài phải bằng tổng độ dài cộng 1)||2 4 9 10 13 10 8 14 (an extra last term, since the length must be the sum of the lengths plus one)⟧",
                   "⟦2 2 6 9 12 (nhân từng cặp số cùng vị trí rồi bỏ phần thừa của dãy dài hơn)||2 2 6 9 12 (multiply pairs in the same position and drop the excess of the longer sequence)⟧",
                   "⟦3 3 5 5 6 (cộng từng số của dãy dài với tổng của dãy ngắn chia đều)||3 3 5 5 6 (add to each term of the long sequence an even share of the short sequence's total)⟧"],
             explain="⟦Độ dài là 5+3−1=7 và tổng các số hạng bằng tích hai tổng, {{sum_f}} nhân {{sum_g}} bằng {{conv_sum}}.||The length is 5+3−1=7 and the sum of the terms equals the product of the sums, {{sum_f}} times {{sum_g}} equals {{conv_sum}}.⟧"),
        dict(q="⟦Trong hệ quy ước 1 của Bracewell, biến tần số $s$ đo bằng gì?||In Bracewell's system 1, what is the frequency variable $s$ measured in?⟧",
             opts=["⟦Số chu kỳ trên một đơn vị của $x$||Cycles per unit of $x$⟧",
                   "⟦Radian trên giây, tức là $s=2\\pi f$ với $f$ là số chu kỳ trên giây||Radians per second, i.e. $s=2\\pi f$ with $f$ the number of cycles per second⟧",
                   "⟦Số dao động trên một đơn vị của $x$ nhân với hệ số chuẩn hóa $1/\\sqrt{2\\pi}$||Oscillations per unit of $x$ times the normalising factor $1/\\sqrt{2\\pi}$⟧",
                   "⟦Đơn vị không thứ nguyên, vì $s$ luôn được chuẩn hóa theo bề rộng của tín hiệu||Dimensionless, because $s$ is always normalised by the width of the signal⟧"],
             explain="⟦Bracewell, tr. 6 và 18: hằng số $2\\pi$ nằm trong số mũ nên $s$ là số chu kỳ trên đơn vị của $x$; đổi sang $\\omega=2\\pi s$ khi đọc tài liệu khác.||Bracewell, pp. 6 and 18: the $2\\pi$ sits in the exponent so $s$ counts cycles per unit of $x$; convert with $\\omega=2\\pi s$ when reading other texts.⟧"),
    ],
    nb=[
        ("md", """## 1. ⟦Dạng sóng và phổ||Waveform and spectrum⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Trong tín hiệu gồm nhiều sóng hình sin trộn lẫn, mỗi tần số đóng góp bao nhiêu biên độ, và khi nào phép đọc phổ sai lệch? Ta tính bằng hai cách độc lập: FFT và tổng trực tiếp $X_k=\\sum_n x_n e^{-i2\\pi kn/N}$ (\"biến đổi Fourier chậm\" của Bracewell).||In a signal made of several mixed sinusoids, how much amplitude does each frequency contribute, and when does reading the spectrum go wrong? We compute it two independent ways: the FFT and the direct sum $X_k=\\sum_n x_n e^{-i2\\pi kn/N}$ (Bracewell's \"slow Fourier transform\").⟧"""),
        ("code", r'''fs, N = 1000, 1000                       # ⟦tần số lấy mẫu (Hz) và số mẫu: đúng 1 giây, nên 1 ô tần số = 1 Hz||sampling rate (Hz) and number of samples: exactly 1 second, so 1 frequency bin = 1 Hz⟧
t = np.arange(N) / fs
x = 1.0*np.sin(2*np.pi*50*t) + 0.5*np.cos(2*np.pi*120*t) + 0.25*np.sin(2*np.pi*300*t)

# ⟦Cách A: FFT||Method A: FFT⟧
amp_fft = amplitude_spectrum(x)

# ⟦Cách B: tổng trực tiếp theo định nghĩa (không dùng FFT)||Method B: direct sum from the definition (no FFT)⟧
n = np.arange(N)
amp_direct = np.array([2*abs(np.sum(x*np.exp(-2j*np.pi*k*n/N)))/N for k in range(N//2 + 1)])
amp_direct[0] /= 2

diff = np.max(np.abs(amp_fft - amp_direct))
assert diff < 1e-9
report("fft_direct_diff", diff, ".1e")
for f in (50, 120, 300):
    report(f"a{f}", amp_fft[f], ".6f")

others = np.ones(len(amp_fft), bool); others[[50, 120, 300]] = False
assert amp_fft[others].max() < 1e-9      # ⟦mọi ô tần số khác đều bằng 0||every other bin is zero⟧'''),
        ("code", r'''fig, ax = plt.subplots(1, 2, figsize=(9, 3.2))
ax[0].plot(t[:150]*1000, x[:150])
ax[0].set_xlabel("⟦thời gian (ms)||time (ms)⟧"); ax[0].set_title("⟦Dạng sóng x(t)||Waveform x(t)⟧")
ax[1].vlines(np.arange(400), 0, amp_fft[:400])
ax[1].set_xlabel("⟦tần số (Hz)||frequency (Hz)⟧"); ax[1].set_title("⟦Phổ biên độ||Amplitude spectrum⟧")
plt.tight_layout(); plt.show()''', dict(fig="waveform_spectrum", cap="⟦Hình 1. Dạng sóng (trái) trông phức tạp, nhưng phổ (phải) chỉ có ba vạch đúng tại 50, 120 và 300 Hz.||Figure 1. The waveform (left) looks complicated, but the spectrum (right) has just three lines at exactly 50, 120 and 300 Hz.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Ba biên độ phục hồi được là {{a50}} (50 Hz), {{a120}} (120 Hz) và {{a300}} (300 Hz), đúng bằng các hệ số đã cài vào tín hiệu. Hai phương pháp độc lập lệch nhau tối đa {{fft_direct_diff}}, tức là chỉ khác nhau ở sai số làm tròn, và mọi ô tần số còn lại bằng 0. Đây là ý nghĩa của \"dạng sóng và phổ mang cùng thông tin\": từ 1000 mẫu phức tạp ta rút ra đúng 6 con số (3 biên độ, 3 tần số).||The three recovered amplitudes are {{a50}} (50 Hz), {{a120}} (120 Hz) and {{a300}} (300 Hz), exactly the coefficients built into the signal. The two independent methods differ by at most {{fft_direct_diff}}, i.e. only by rounding error, and every other bin is zero. That is what \"a waveform and its spectrum carry the same information\" means: from 1000 messy samples we extract just 6 numbers (3 amplitudes, 3 frequencies).⟧"""),
        ("code", r'''# ⟦Rò phổ: 50.5 Hz không rơi đúng vào ô tần số nào (nằm giữa ô 50 và ô 51)||Leakage: 50.5 Hz falls on no bin (it sits between bins 50 and 51)⟧
xl = np.sin(2*np.pi*50.5*t)
al = amplitude_spectrum(xl)
pred = abs(np.sinc(0.5))                 # ⟦dự đoán A|sinc(δ)| với δ = 0.5 ô||prediction A|sinc(δ)| with δ = 0.5 bin⟧
assert abs(al[50] - pred) < 0.01 and abs(al[51] - pred) < 0.01
report("leak_peak", al[50], ".4f"); report("leak_theory", pred, ".4f"); report("leak_far", al[80], ".4f")

# ⟦Pha của sin và cos||Phase of sin and cos⟧
ph_sin = np.degrees(np.angle(np.fft.rfft(np.sin(2*np.pi*50*t))[50]))
ph_cos = np.degrees(np.angle(np.fft.rfft(np.cos(2*np.pi*120*t))[120]))
assert abs(ph_sin + 90) < 1e-6 and abs(ph_cos) < 1e-6
report("ph_sin", round(ph_sin, 1) + 0.0, ".1f"); report("ph_cos", round(ph_cos, 1) + 0.0, ".1f")

# ⟦Tính tuyến tính của phép biến đổi||Linearity of the transform⟧
x1, x2 = np.sin(2*np.pi*50*t), np.cos(2*np.pi*120*t)
lin_err = np.max(np.abs(np.fft.rfft(x1 + x2) - (np.fft.rfft(x1) + np.fft.rfft(x2))))
assert lin_err < 1e-9
report("lin_err", lin_err, ".1e")'''),
        ("code", r'''fig, ax = plt.subplots(1, 2, figsize=(9, 3.2))
ax[0].vlines(np.arange(0, 101), 0, amplitude_spectrum(np.sin(2*np.pi*50*t))[:101], colors="tab:green")
ax[0].set_title("⟦50 Hz: đúng vào một ô||50 Hz: exactly on a bin⟧")
ax[1].vlines(np.arange(0, 101), 0, al[:101], colors="tab:red")
ax[1].set_title("⟦50.5 Hz: rò sang mọi ô||50.5 Hz: leaks into every bin⟧")
for a_ in ax: a_.set_xlabel("⟦tần số (Hz)||frequency (Hz)⟧"); a_.set_ylim(0, 1.05)
plt.tight_layout(); plt.show()''', dict(fig="leakage", cap="⟦Hình 2. Cùng một sóng hình sin biên độ 1: nếu tần số rơi đúng vào ô (trái) ta thấy một vạch, nếu rơi giữa hai ô (phải) năng lượng loang sang các ô lân cận.||Figure 2. The same unit-amplitude sinusoid: on a bin (left) we see one line, between two bins (right) the energy smears into neighbouring bins.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Sóng 50.5 Hz cho biên độ ô 50 là {{leak_peak}} thay vì 1; dự đoán $|\\text{sinc}(0.5)|$ là {{leak_theory}}, khớp trong 0.01. Ngay cả ô 80, cách đỉnh 30 ô, vẫn còn {{leak_far}}: đây là rò phổ, hệ quả của việc cắt tín hiệu bằng cửa sổ chữ nhật. Pha của $\\sin$ tại ô 50 là {{ph_sin}} độ và của $\\cos$ tại ô 120 là {{ph_cos}} độ. Tính tuyến tính của phép biến đổi được xác nhận: sai lệch {{lin_err}}.||The 50.5 Hz wave gives bin-50 amplitude {{leak_peak}} instead of 1; the prediction $|\\text{sinc}(0.5)|$ is {{leak_theory}}, matching within 0.01. Even bin 80, 30 bins from the peak, still holds {{leak_far}}: this is leakage, the consequence of cutting the signal with a rectangular window. The phase of $\\sin$ at bin 50 is {{ph_sin}} degrees and of $\\cos$ at bin 120 is {{ph_cos}} degrees. Linearity of the transform is confirmed: deviation {{lin_err}}.⟧"""),
        ("md", """## 2. ⟦Năng lượng và tích chập: hai phép kiểm số cổ điển||Energy and convolution: two classic numerical checks⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Đổi miền có làm mất hay thêm thông tin không, và tích chập trong miền gốc có đúng là phép nhân trong miền tần số không? Ta kiểm bằng bảo toàn năng lượng và bằng ví dụ tích chập nối tiếp của Bracewell (tr. 32).||Does changing domain lose or add information, and is convolution in the original domain really multiplication in the frequency domain? We check with energy conservation and with Bracewell's serial-product example (p. 32).⟧"""),
        ("code", r'''# ⟦Tín hiệu xác định (không ngẫu nhiên) để kết quả tái lập được||A deterministic (non-random) signal so results are reproducible⟧
n = np.arange(1000)
xr = np.cos(2*np.pi*7*n/1000)*np.exp(-n/300) + 0.3*np.sin(2*np.pi*41*n/1000)
e_time = np.sum(xr**2)
e_freq = np.sum(np.abs(np.fft.fft(xr))**2)/len(xr)
assert np.isclose(e_time, e_freq)
report("energy_time", e_time, ".6f"); report("energy_freq", e_freq, ".6f")

# ⟦Tích chập nối tiếp của Bracewell (tr. 32)||Bracewell's serial product (p. 32)⟧
f = np.array([2, 2, 3, 3, 4]); g = np.array([1, 1, 2])
c_direct = np.convolve(f, g)                                   # ⟦cách A: tổng trực tiếp||method A: direct sum⟧
L = len(f) + len(g) - 1
c_fft = np.fft.irfft(np.fft.rfft(f, L)*np.fft.rfft(g, L), L)   # ⟦cách B: nhân hai FFT rồi biến đổi ngược||method B: multiply two FFTs then invert⟧
assert np.allclose(c_direct, c_fft)
assert c_direct.sum() == f.sum()*g.sum()
report("conv_direct", " ".join(str(v) for v in c_direct), "s")
report("sum_f", int(f.sum()), "d"); report("sum_g", int(g.sum()), "d"); report("conv_sum", int(c_direct.sum()), "d")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Năng lượng theo thời gian {{energy_time}} bằng năng lượng theo tần số {{energy_freq}}: đổi miền không làm mất thông tin. Tích chập nối tiếp cho dãy {{conv_direct}} bằng cả hai cách, đúng như Bracewell tính tay, và tổng các số hạng {{conv_sum}} bằng tích hai tổng {{sum_f}} nhân {{sum_g}}.||The time-domain energy {{energy_time}} equals the frequency-domain energy {{energy_freq}}: changing domain loses no information. The serial product gives the sequence {{conv_direct}} by both methods, as Bracewell computes by hand, and the sum of terms {{conv_sum}} equals the product of the sums {{sum_f}} times {{sum_g}}.⟧"""),
        ("md", """## 3. ⟦Hệ tuyến tính bất biến giữ nguyên tần số||A linear invariant system keeps the frequency⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Bộ lọc thông thấp $y[n]=a\\,y[n-1]+(1-a)x[n]$ làm gì với sóng hình sin? Ta đo độ lợi và pha bằng FFT, đối chiếu công thức đáp ứng tần số $H(\\omega)=\\dfrac{1-a}{1-a\\,e^{-i\\omega}}$, và đối chiếu đáp ứng xung $h[n]=(1-a)a^n$ với hàm <code>lfilter</code>.||What does the low-pass filter $y[n]=a\\,y[n-1]+(1-a)x[n]$ do to a sinusoid? We measure gain and phase with an FFT, compare with the frequency response $H(\\omega)=\\dfrac{1-a}{1-a\\,e^{-i\\omega}}$, and compare the impulse response $h[n]=(1-a)a^n$ with the <code>lfilter</code> function.⟧"""),
        ("code", r'''from scipy.signal import lfilter

a = 0.9                                  # ⟦hệ số bộ lọc||filter coefficient⟧

def lowpass_loop(x, a):                  # ⟦cách viết tay bằng vòng lặp, độc lập với SciPy||hand-written loop, independent of SciPy⟧
    y, prev = np.zeros_like(x), 0.0
    for i, xi in enumerate(x):
        prev = a*prev + (1 - a)*xi
        y[i] = prev
    return y

x0 = np.sin(2*np.pi*50*np.arange(2000)/fs + 0.3)   # ⟦sóng 50 Hz, pha đầu 0.3 rad, dài 2 s||50 Hz wave, initial phase 0.3 rad, 2 s long⟧
y_scipy = lfilter([1 - a], [1, -a], x0)
y_loop = lowpass_loop(x0, a)
assert np.allclose(y_scipy, y_loop)

# ⟦Đáp ứng xung h[n] và tích chập trực tiếp||Impulse response h[n] and direct convolution⟧
h = (1 - a)*a**np.arange(300)
y_conv = np.convolve(x0, h)[:len(x0)]
conv_diff = np.max(np.abs(y_conv - y_scipy))
assert conv_diff < 1e-9
report("conv_lfilter_diff", conv_diff, ".1e"); report("h_sum", h.sum(), ".6f")

xs, ys = x0[1000:], y_scipy[1000:]       # ⟦bỏ 1 s đầu (quá độ), phân tích 1 s ổn định||drop the first second (transient), analyse the steady second⟧
Xs, Ys = np.fft.rfft(xs), np.fft.rfft(ys)
f_out = int(np.argmax(np.abs(Ys)))
gain_meas = abs(Ys[50]) / abs(Xs[50])
phase_meas = np.angle(np.exp(1j*(np.angle(Ys[50]) - np.angle(Xs[50]))))

w = 2*np.pi*50/fs
H = (1 - a)/(1 - a*np.exp(-1j*w))        # ⟦đáp ứng tần số theo lý thuyết||theoretical frequency response⟧
assert abs(gain_meas - abs(H)) < 1e-6 and abs(phase_meas - np.angle(H)) < 1e-6

report("f_out", f_out, "d")
report("gain_meas", gain_meas, ".6f");   report("gain_theory", abs(H), ".6f")
report("phase_meas_deg", np.degrees(phase_meas), ".3f");  report("phase_theory_deg", np.degrees(np.angle(H)), ".3f")

# ⟦Đo độ lợi ở nhiều tần số||Measure the gain at several frequencies⟧
meas = {50: gain_meas}
for fq in (25, 100, 200):
    xin = np.sin(2*np.pi*fq*np.arange(2000)/fs)
    yout = lfilter([1 - a], [1, -a], xin)[1000:]
    G = abs(np.fft.rfft(yout)[fq]) / abs(np.fft.rfft(xin[1000:])[fq])
    Ht = abs((1 - a)/(1 - a*np.exp(-1j*2*np.pi*fq/fs)))
    assert abs(G - Ht) < 1e-6
    meas[fq] = G
    report(f"gain_{fq}", G, ".6f")'''),
        ("code", r'''ff = np.linspace(0, 500, 501)
Hc = np.abs((1 - a)/(1 - a*np.exp(-1j*2*np.pi*ff/fs)))
plt.figure(figsize=(6.5, 3.2))
plt.plot(ff, Hc, label="⟦lý thuyết |H|||theory |H|⟧")
plt.plot(list(meas), list(meas.values()), "o", label="⟦đo bằng FFT||measured by FFT⟧")
plt.xlabel("⟦tần số (Hz)||frequency (Hz)⟧"); plt.ylabel("⟦độ lợi||gain⟧"); plt.legend()
plt.tight_layout(); plt.show()''', dict(fig="lowpass_response", cap="⟦Hình 3. Đường lý thuyết của bộ lọc thông thấp và bốn điểm đo bằng FFT (25, 50, 100, 200 Hz) nằm trên cùng một đường.||Figure 3. The theoretical curve of the low-pass filter and four FFT measurements (25, 50, 100, 200 Hz) lie on the same curve.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Sóng ra vẫn có đỉnh tại {{f_out}} Hz: tần số không đổi. Bộ lọc chỉ đổi biên độ (độ lợi đo {{gain_meas}}, lý thuyết {{gain_theory}}) và pha (đo {{phase_meas_deg}} độ, lý thuyết {{phase_theory_deg}} độ, dấu âm nghĩa là sóng ra trễ pha). Vòng lặp viết tay, <code>lfilter</code> và tích chập với $h[n]$ cho cùng đáp số (lệch {{conv_lfilter_diff}}), và tổng của $h$ là {{h_sum}} nên độ lợi một chiều bằng 1. Độ lợi giảm dần theo tần số: {{gain_25}} tại 25 Hz, {{gain_100}} tại 100 Hz, {{gain_200}} tại 200 Hz.||The output still peaks at {{f_out}} Hz: the frequency is unchanged. The filter only changes the amplitude (measured gain {{gain_meas}}, theory {{gain_theory}}) and the phase (measured {{phase_meas_deg}} degrees, theory {{phase_theory_deg}} degrees; negative means the output lags). The hand-written loop, <code>lfilter</code> and convolution with $h[n]$ give the same answer (difference {{conv_lfilter_diff}}), and the sum of $h$ is {{h_sum}} so the DC gain is 1. The gain falls with frequency: {{gain_25}} at 25 Hz, {{gain_100}} at 100 Hz, {{gain_200}} at 200 Hz.⟧"""),
        ("md", """## 4. ⟦Khi điều kiện bị phá vỡ||When the conditions fail⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Nếu hệ phi tuyến (khâu bình phương, khâu bậc ba) hoặc thay đổi theo thời gian (bộ nhân với cosin) thì phổ ra khác gì hệ tuyến tính bất biến? Khác với phần 3, ở đây tần số ra không còn bằng tần số vào.||If the system is nonlinear (a squarer, a cubic stage) or time-varying (a cosine multiplier), how does the output spectrum differ from that of a linear invariant system? Unlike part 3, the output frequency no longer equals the input frequency.⟧"""),
        ("code", r'''xt = np.sin(2*np.pi*50*np.arange(1000)/fs)

# ⟦Hệ phi tuyến: khâu bình phương||Nonlinear system: a squarer⟧
An = amplitude_spectrum(xt**2)
nl_dc, nl_a100, nl_a50 = An[0], An[100], An[50]

# ⟦Hệ tuyến tính nhưng thay đổi theo thời gian: nhân với cos(2π·20t)||Linear but time-varying: multiply by cos(2π·20t)⟧
At = amplitude_spectrum(xt*np.cos(2*np.pi*20*np.arange(1000)/fs))
tv_a30, tv_a70, tv_a50 = At[30], At[70], At[50]

assert abs(nl_dc - 0.5) < 1e-9 and abs(nl_a100 - 0.5) < 1e-9 and nl_a50 < 1e-9
assert abs(tv_a30 - 0.5) < 1e-9 and abs(tv_a70 - 0.5) < 1e-9 and tv_a50 < 1e-9
for k, v in dict(nl_dc=nl_dc, nl_a100=nl_a100, nl_a50=nl_a50, tv_a30=tv_a30, tv_a70=tv_a70).items():
    report(k, abs(v), ".6f")

# ⟦Khâu bậc ba y = x + 0.1x³ và méo hài||Cubic stage y = x + 0.1x³ and harmonic distortion⟧
Ac = amplitude_spectrum(xt + 0.1*xt**3)
fund, h3 = Ac[50], Ac[150]
assert abs(fund - 1.075) < 1e-9 and abs(h3 - 0.025) < 1e-9     # ⟦sin³θ = (3 sinθ − sin3θ)/4||sin³θ = (3 sinθ − sin3θ)/4⟧
report("cubic_fund", fund, ".6f"); report("cubic_h3", h3, ".6f"); report("cubic_thd_pct", 100*h3/fund, ".4f")'''),
        ("code", r'''fr = np.arange(0, 201)
fig, ax = plt.subplots(1, 4, figsize=(12, 3), sharey=True)
panels = [(amplitude_spectrum(ys), "⟦Lọc tuyến tính bất biến||Linear invariant filter⟧"),
          (An, "⟦Khâu bình phương||Squarer⟧"),
          (Ac, "⟦Khâu bậc ba||Cubic stage⟧"),
          (At, "⟦Nhân với cos(2π·20t)||Multiply by cos(2π·20t)⟧")]
for a_, (s, ttl) in zip(ax, panels):
    a_.vlines(fr, 0, s[:201]); a_.set_title(ttl, fontsize=9); a_.set_xlabel("⟦tần số (Hz)||frequency (Hz)⟧")
ax[0].set_ylabel("⟦biên độ||amplitude⟧")
plt.tight_layout(); plt.show()''', dict(fig="linear_vs_nonlinear", cap="⟦Hình 4. Cùng sóng vào 50 Hz: hệ tuyến tính bất biến giữ vạch 50 Hz; khâu bình phương tạo 0 và 100 Hz; khâu bậc ba tạo hài 150 Hz; bộ nhân tạo 30 và 70 Hz.||Figure 4. Same 50 Hz input: the linear invariant system keeps the 50 Hz line; the squarer creates 0 and 100 Hz; the cubic stage creates a 150 Hz harmonic; the multiplier creates 30 and 70 Hz.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Khâu bình phương cho một chiều {{nl_dc}} và 100 Hz biên độ {{nl_a100}}, còn 50 Hz chỉ {{nl_a50}}. Bộ nhân với cosin cho 30 Hz và 70 Hz cùng biên độ {{tv_a30}} và {{tv_a70}} (công thức $\\cos A\\cos B=\\tfrac12[\\cos(A-B)+\\cos(A+B)]$). Khâu bậc ba cho cơ bản {{cubic_fund}} và hài bậc ba {{cubic_h3}}, tức THD {{cubic_thd_pct}}%, đúng theo $\\sin^3\\theta=\\tfrac34\\sin\\theta-\\tfrac14\\sin3\\theta$. Kết luận: vạch phổ tại tần số lạ là chữ ký của phi tuyến hoặc của hệ thay đổi theo thời gian. Đó là lý do lý thuyết trong giáo trình đặt nền trên hệ tuyến tính bất biến, nơi đáp ứng là một tích chập.||The squarer gives DC {{nl_dc}} and 100 Hz with amplitude {{nl_a100}}, with only {{nl_a50}} left at 50 Hz. The cosine multiplier gives 30 Hz and 70 Hz with equal amplitudes {{tv_a30}} and {{tv_a70}} (from $\\cos A\\cos B=\\tfrac12[\\cos(A-B)+\\cos(A+B)]$). The cubic stage gives a fundamental {{cubic_fund}} and a third harmonic {{cubic_h3}}, i.e. a THD of {{cubic_thd_pct}}%, exactly as $\\sin^3\\theta=\\tfrac34\\sin\\theta-\\tfrac14\\sin3\\theta$ predicts. Conclusion: a spectral line at a foreign frequency is the signature of nonlinearity or time variation. That is why the theory in the book rests on linear invariant systems, where the response is a convolution.⟧"""),
        ("md", """## 5. ⟦Ký hiệu: hàm cổng, tích chập và xung||Notation: gate, convolution and impulse⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Các ký hiệu $\\Pi$, $*$ và $\\delta$ có đúng như giáo trình mô tả không? Ta kiểm bằng tích phân số so với công thức đóng, và bằng dãy xung chữ nhật $\\delta_\\varepsilon$ hẹp dần.||Do the symbols $\\Pi$, $*$ and $\\delta$ behave as the book describes? We check with numerical integrals against closed forms, and with a sequence of narrowing rectangular pulses $\\delta_\\varepsilon$.⟧"""),
        ("code", r'''from scipy import integrate, special

# ⟦Hàm cổng: ∫ Π(x) cos(πx) dx = ∫ từ −1/2 đến 1/2 của cos(πx) = 2/π||Gate: ∫ Π(x) cos(πx) dx = integral from −1/2 to 1/2 of cos(πx) = 2/π⟧
gate_area, _ = integrate.quad(lambda u: np.cos(np.pi*u), -0.5, 0.5)
assert abs(gate_area - 2/np.pi) < 1e-12
report("gate_area", gate_area, ".6f")

# ⟦Trung bình trượt Π*f tại x = 0 với f(u) = exp(−u²): tích phân số so với √π·erf(1/2)||Running mean Π*f at x = 0 with f(u) = exp(−u²): numerical integral versus √π·erf(1/2)⟧
run_num, _ = integrate.quad(lambda u: np.exp(-u**2), -0.5, 0.5)
run_exact = np.sqrt(np.pi)*special.erf(0.5)
assert abs(run_num - run_exact) < 1e-12
report("run_mean_num", run_num, ".6f"); report("run_mean_exact", run_exact, ".6f")

# ⟦Tính chất "sàng" của xung: ∫ cos(x) δ_ε(x) dx → cos(0) = 1||Sifting property: ∫ cos(x) δ_ε(x) dx → cos(0) = 1⟧
for tag, eps in (("e05", 0.5), ("e01", 0.1), ("e001", 0.01)):
    val, _ = integrate.quad(lambda u: np.cos(u)/eps, -eps/2, eps/2)
    exact = 2*np.sin(eps/2)/eps
    assert abs(val - exact) < 1e-12
    report(f"sift_{tag}", val, ".6f")'''),
        ("code", r'''xx = np.linspace(-1, 1, 2001)
plt.figure(figsize=(6.5, 3.2))
for eps, c in ((0.5, "tab:blue"), (0.2, "tab:orange"), (0.1, "tab:green")):
    plt.plot(xx, np.where(np.abs(xx) < eps/2, 1/eps, 0.0), color=c, label=f"ε = {eps}")
plt.xlabel("x"); plt.ylabel("δ_ε(x)"); plt.legend()
plt.tight_layout(); plt.show()''', dict(fig="impulse_limit", cap="⟦Hình 5. Dãy xung chữ nhật diện tích 1: bề rộng ε giảm thì chiều cao 1/ε tăng. Giới hạn của dãy là xung δ.||Figure 5. A sequence of unit-area rectangles: as the width ε shrinks the height 1/ε grows. The limit of the sequence is the impulse δ.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Tích phân $\\int\\Pi(x)\\cos(\\pi x)\\,dx$ bằng {{gate_area}}, đúng $2/\\pi$. Trung bình trượt của $e^{-u^2}$ tại gốc là {{run_mean_num}} bằng tích phân số và {{run_mean_exact}} bằng công thức đóng. Bảng \"sàng\": {{sift_e05}} với ε=0.5, {{sift_e01}} với ε=0.1, {{sift_e001}} với ε=0.01, tiến dần tới $\\cos 0=1$. Vậy biểu thức chứa $\\delta$ có nghĩa đúng như Bracewell mô tả: là giới hạn của dãy xung có bề rộng, không phải một hàm tại một điểm.||The integral $\\int\\Pi(x)\\cos(\\pi x)\\,dx$ equals {{gate_area}}, exactly $2/\\pi$. The running mean of $e^{-u^2}$ at the origin is {{run_mean_num}} by numerical integration and {{run_mean_exact}} by the closed form. The sifting table gives {{sift_e05}} for ε=0.5, {{sift_e01}} for ε=0.1, {{sift_e001}} for ε=0.01, approaching $\\cos 0=1$. So an expression containing $\\delta$ has meaning exactly as Bracewell describes: as the limit of a sequence of pulses of finite width, not as a function at a point.⟧"""),
    ],
)
