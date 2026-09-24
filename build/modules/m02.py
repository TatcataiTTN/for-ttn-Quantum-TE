from lib import F, C, UL, OL, TBL

MOD = dict(
    n=2, slug="groundwork", part="A", book="B",
    title="⟦Nền tảng: biến đổi, điều kiện tồn tại và đối xứng||Groundwork: the transform, existence and symmetry⟧",
    blurb="⟦Định nghĩa biến đổi Fourier, khi nào nó tồn tại, biến đổi trong giới hạn, và bảng đối xứng chẵn, lẻ, Hermitian.||"
          "The definition of the Fourier transform, when it exists, transforms in the limit, and the table of even, odd and Hermitian symmetries.⟧",
    src="⟦Bracewell, chương 2, tr. 5–23||Bracewell, chapter 2, pp. 5–23⟧",
    data="⟦Sinh bằng mã: Gauss, sech, xung chữ nhật và tam giác, $e^{-x}H(x)$, Gauss điều chế, dãy ngẫu nhiên có đối xứng||Generated in code: Gaussian, sech, rectangle and triangle, $e^{-x}H(x)$, modulated Gaussians, symmetric random sequences⟧",
    objectives=[
        "⟦Viết và dùng cặp biến đổi Fourier, hiểu tính tuần hoàn $\\mathcal F\\mathcal Ff=f(-x)$.||Write and use the Fourier pair, and understand the cyclic property $\\mathcal F\\mathcal Ff=f(-x)$.⟧",
        "⟦Nêu điều kiện tồn tại và giải thích \"biến đổi trong giới hạn\" bằng dãy Gauss điều chế.||State the existence conditions and explain \"transforms in the limit\" through modulated Gaussians.⟧",
        "⟦Tách hàm thành phần chẵn và lẻ, và đọc bảng đối xứng của Bracewell.||Split a function into even and odd parts and read Bracewell's symmetry table.⟧",
        "⟦Dùng liên hợp phức, biến đổi cosin và sin, và hàm Hermitian.||Use complex conjugates, the cosine and sine transforms and Hermitian functions.⟧",
        "⟦Diễn giải tích phân Fourier bằng ba hình: diện tích, cosinusoid và xoắn ốc trên mặt phẳng phức.||Interpret the Fourier integral through three pictures: area, cosinusoid and a spiral on the complex plane.⟧",
    ],
    parts=[
        # ---------------------------------------------------------------- PART 1
        dict(
            title="⟦Biến đổi Fourier và định lý tích phân Fourier||The Fourier transform and Fourier's integral theorem⟧",
            scr=("⟦Chương 1 cho biết biến đổi là công cụ đổi miền để giải bài toán tuyến tính.||Chapter 1 told us a transform is a domain-changing tool for linear problems.⟧",
                 "⟦Để dùng được nó ta cần công thức chính xác, quy ước hằng số và biết chiều ngược lại đúng đến mức nào.||To use it we need the exact formula, the constant convention and to know how exactly the reverse direction works.⟧",
                 "⟦Bracewell chọn hệ 1, cho biến đổi ngược qua định lý tích phân Fourier, và nêu tính tuần hoàn của phép biến đổi.||Bracewell picks system 1, gets the inverse from Fourier's integral theorem and states the cyclic property of the transform.⟧"),
            preview=["⟦Định nghĩa, tính tuần hoàn và tương hỗ||Definition, cyclic and reciprocal properties⟧",
                     "⟦Định lý tích phân Fourier tại điểm gián đoạn||Fourier's integral theorem at a discontinuity⟧",
                     "⟦Ba hệ hằng số và các ký hiệu||Three constant systems and the notations⟧"],
            slides=[
                ("⟦Định nghĩa biến đổi Fourier||Definition of the Fourier transform⟧",
                 "<p>⟦Biến đổi Fourier của $f(x)$ là tích phân dưới đây, một hàm của $s$ và có thể viết $F(s)$ (Bracewell, tr. 5).||The Fourier transform of $f(x)$ is the integral below, a function of $s$ that may be written $F(s)$ (Bracewell, p. 5).⟧</p>"
                 + F("⟦Biến đổi thuận||Forward transform⟧", r"F(s)=\int_{-\infty}^{\infty}f(x)\,e^{-i2\pi xs}\,dx",
                     [("f(x)", "⟦hàm gốc||the original function⟧"), ("s", "⟦tần số, chu kỳ trên đơn vị của $x$||frequency, cycles per unit of $x$⟧"), ("F(s)", "⟦biến đổi Fourier||the Fourier transform⟧")])),
                ("⟦Tính tuần hoàn: hai lần biến đổi||The cyclic property: two transforms⟧",
                 "<p>⟦Biến đổi $F(s)$ thêm một lần nữa bằng cùng công thức, ta được $f(-x)$. Với hàm chẵn ta thu lại đúng $f(x)$, đó là tính tuần hoàn hai bước và kéo theo tính tương hỗ: nếu $F$ là biến đổi của $f$ thì $f$ là biến đổi của $F$ (tr. 5). Với hàm lẻ hoặc bất kỳ, kết quả là $f(-x)$ (tr. 6).||"
                 "Transforming $F(s)$ once more with the same formula gives $f(-x)$. For an even function we recover exactly $f(x)$: that is the two-step cyclic property and it implies reciprocity, if $F$ is the transform of $f$ then $f$ is the transform of $F$ (p. 5). For an odd or general function the result is $f(-x)$ (p. 6).⟧</p>"
                 + F("⟦Hai lần biến đổi||Two transforms⟧", r"\mathcal F\mathcal F f=f(-x)")),
                ("⟦Thử số: hai lần biến đổi trả về $f(-x)$||Numerical test: two transforms return $f(-x)$⟧",
                 "<p>⟦Với một dãy 64 điểm không chẵn không lẻ, $\\frac1N\\,\\text{DFT}(\\text{DFT}(v))$ trùng dãy đảo $v[-n]$ (lệch tối đa {{cyc_err}}) và bốn lần biến đổi trả lại đúng $v$ (lệch {{cyc4_err}}). Phép kiểm dùng cả FFT lẫn ma trận DFT dựng tay.||"
                 "For a 64-point sequence that is neither even nor odd, $\\frac1N\\,\\text{DFT}(\\text{DFT}(v))$ equals the reversed sequence $v[-n]$ (largest deviation {{cyc_err}}) and four transforms return exactly $v$ (deviation {{cyc4_err}}). The check uses both the FFT and a hand-built DFT matrix.⟧</p>"),
                ("⟦Biến đổi \"trừ i\" và \"cộng i\"||The \"minus-i\" and \"plus-i\" transforms⟧",
                 "<p>⟦Hai lần biến đổi bằng cùng một công thức không trả đúng hàm gốc. Muốn đảo ngược, dùng dấu mũ ngược lại. Bracewell gọi $F$ là biến đổi \"trừ i\" của $f$ và $f$ là biến đổi \"cộng i\" của $F$ (tr. 6).||"
                 "Two transforms with the same formula do not return the original function. To invert, use the opposite exponent sign. Bracewell calls $F$ the \"minus-i\" transform of $f$ and $f$ the \"plus-i\" transform of $F$ (p. 6).⟧</p>"
                 + F("⟦Cặp thuận và ngược||Forward and inverse pair⟧", r"F(s)=\int f(x)e^{-i2\pi xs}dx,\qquad f(x)=\int F(s)e^{+i2\pi xs}ds")),
                ("⟦Định lý tích phân Fourier||Fourier's integral theorem⟧",
                 "<p>⟦Viết hai phép biến đổi liên tiếp thành một tích phân lặp ta có phát biểu quen thuộc. Tại điểm gián đoạn, vế trái phải thay bằng trung bình của hai giới hạn hai phía (tr. 6).||"
                 "Writing the two successive transformations as a repeated integral gives the usual statement. At a discontinuity the left side must be replaced by the mean of the two one-sided limits (p. 6).⟧</p>"
                 + F("⟦Định lý tích phân Fourier||Fourier's integral theorem⟧", r"\tfrac12\left[f(x^+)+f(x^-)\right]=\int_{-\infty}^{\infty}\left[\int_{-\infty}^{\infty}f(u)\,e^{-i2\pi us}\,du\right]e^{i2\pi xs}\,ds")),
                ("⟦Thử số: tái dựng xung chữ nhật tại điểm gián đoạn||Numerical test: rebuilding the rectangle at its jump⟧",
                 "<p>⟦Biến đổi của $\\Pi(x)$ là $\\text{sinc}\\,s$. Cắt phép biến đổi ngược ở $|s|\\le S$ rồi tính tại $x=0.5$ (chỗ nhảy của $\\Pi$): $S=5$ cho {{thm_s5}}, $S=20$ cho {{thm_s20}}, $S=100$ cho {{thm_s100}}, tiến về 0.5, đúng trung bình của 1 và 0. Tại $x=0.25$ (trong xung) được {{thm_in}}, tại $x=1$ (ngoài xung) được {{thm_out}}.||"
                 "The transform of $\\Pi(x)$ is $\\text{sinc}\\,s$. Cut the inverse transform at $|s|\\le S$ and evaluate at $x=0.5$ (the jump of $\\Pi$): $S=5$ gives {{thm_s5}}, $S=20$ gives {{thm_s20}}, $S=100$ gives {{thm_s100}}, approaching 0.5, the mean of 1 and 0. At $x=0.25$ (inside the pulse) we get {{thm_in}}, at $x=1$ (outside) we get {{thm_out}}.⟧</p>{{fig:theorem}}"),
                ("⟦Ba hệ hằng số||Three systems of constants⟧",
                 "<p>⟦Hằng số $2\\pi$ có thể đặt trong số mũ (hệ 1), đặt vào biến (hệ 2) hoặc chia đều bằng $1/\\sqrt{2\\pi}$ (hệ 3). Khóa này giữ hệ 1 như giáo trình. Nếu $f(x)$ và $F(s)$ là một cặp ở hệ 1 thì $f(x)$ và $F(s/2\\pi)$ là một cặp ở hệ 2 (tr. 6).||"
                 "The constant $2\\pi$ can sit in the exponent (system 1), in the variable (system 2), or be split evenly by $1/\\sqrt{2\\pi}$ (system 3). This course keeps system 1 like the book. If $f(x)$ and $F(s)$ are a pair in system 1 then $f(x)$ and $F(s/2\\pi)$ are a pair in system 2 (p. 6).⟧</p>"
                 + TBL(["⟦Hệ||System⟧", "$F$", "$f$"],
                       [["1", r"$\int f\,e^{-i2\pi xs}dx$", r"$\int F\,e^{i2\pi xs}ds$"],
                        ["2", r"$\int f\,e^{-isx}dx$", r"$\frac1{2\pi}\int F\,e^{isx}ds$"],
                        ["3", r"$\frac1{\sqrt{2\pi}}\int f\,e^{-isx}dx$", r"$\frac1{\sqrt{2\pi}}\int F\,e^{isx}ds$"]])),
                ("⟦Ký hiệu: $F(s)$, gạch ngang và toán tử $\\mathcal F$||Notation: $F(s)$, the bar and the operator $\\mathcal F$⟧",
                 "<p>⟦Bracewell dùng ba cách viết, mỗi cách có ưu điểm riêng. Chữ hoa $F(s)$ hợp khi có dấu liên hợp và đạo hàm. Gạch ngang trên $f$ gọn cho các phát biểu như định lý tích chập. Toán tử $\\mathcal F$ hợp khi viết biến đổi của một hàm cụ thể (tr. 7 đến 8). Ký hiệu $\\supset$ chỉ chiều thuận, còn $\\leftrightarrow$ dùng cho các phép biến đổi khả đảo đối xứng như cosin, Hilbert và Hartley (tr. 8).||"
                 "Bracewell uses three notations, each with merits. The capital $F(s)$ suits conjugates and derivatives. The bar over $f$ is compact for statements such as the convolution theorem. The operator $\\mathcal F$ suits the transform of a specific function (pp. 7 to 8). The sign $\\supset$ marks the forward direction, while $\\leftrightarrow$ is for symmetric reversible transforms such as cosine, Hilbert and Hartley (p. 8).⟧</p>"
                 + F("⟦Cặp tự biến đổi||A self-transforming pair⟧", r"e^{-\pi x^2}\ \supset\ e^{-\pi s^2}")),
                ("⟦Thử số: Gauss và sech tự biến đổi||Numerical test: Gaussian and sech transform into themselves⟧",
                 "<p>⟦Tích phân số cho biến đổi của $e^{-\\pi x^2}$ tại $s=0.5$ là {{gauss_05}}, đúng $e^{-\\pi/4}$. Biến đổi của $\\text{sech}(\\pi x)$ tại $s=0.5$ là {{sech_05}}, đúng $\\text{sech}(\\pi/2)$. Hai hàm này (cùng với $\\text{III}$) là các hàm tự biến đổi Bracewell nêu ở bài tập 20 (tr. 23).||"
                 "Numerical integration gives the transform of $e^{-\\pi x^2}$ at $s=0.5$ as {{gauss_05}}, exactly $e^{-\\pi/4}$. The transform of $\\text{sech}(\\pi x)$ at $s=0.5$ is {{sech_05}}, exactly $\\text{sech}(\\pi/2)$. These two functions (with $\\text{III}$) are the self-transforming functions Bracewell lists in problem 20 (p. 23).⟧</p>"),
            ]),
        # ---------------------------------------------------------------- PART 2
        dict(
            title="⟦Điều kiện tồn tại và biến đổi trong giới hạn||Existence conditions and transforms in the limit⟧",
            scr=("⟦Người làm mạch tin rằng mọi dạng sóng đều có phổ.||A circuit designer takes it for granted that every waveform has a spectrum.⟧",
                 "⟦Về toán học có những hàm quen thuộc như $\\sin t$, bước nhảy và xung lại không có biến đổi Fourier thường.||Mathematically, familiar functions such as $\\sin t$, the step and the impulse have no ordinary Fourier transform.⟧",
                 "⟦Vật lý cho phép luôn bảo đảm tồn tại, và các hàm còn lại được thu nạp bằng biến đổi trong giới hạn.||Physical possibility always guarantees existence, and the remaining functions are admitted through transforms in the limit.⟧"),
            preview=["⟦Điều kiện đủ và đối ngẫu năng lượng vô hạn||Sufficient conditions and infinite-energy duality⟧",
                     "⟦Dãy Gauss điều chế và hàm suy rộng||Modulated Gaussians and generalized functions⟧",
                     "⟦Hàm dấu và bài tập 3||The sign function and problem 3⟧"],
            slides=[
                ("⟦Vật lý cho phép là điều kiện đủ||Physical possibility is a sufficient condition⟧",
                 "<p>⟦Người làm mạch chắc chắn mọi dạng sóng đều có phổ, người thiết kế ăng-ten chắc chắn mọi ăng-ten đều có giản đồ bức xạ. Không ai tạo được dạng sóng không có phổ. Khi hàm mô tả chính xác một đại lượng vật lý, ta có thể bỏ qua câu hỏi tồn tại (Bracewell, tr. 8).||"
                 "A circuit expert finds it obvious that every waveform has a spectrum, and the antenna designer is confident that every antenna has a radiation pattern. No one can generate a waveform without a spectrum. When the function describes a physical quantity accurately, the question of existence can be ignored (Bracewell, p. 8).⟧</p>"),
                ("⟦Ba hàm quen thuộc không có biến đổi thường||Three familiar functions without an ordinary transform⟧",
                 "<p>⟦Ta hay thay đại lượng vật lý bằng một biểu thức toán gọn như $\\sin t$, $H(t)$ và $\\delta(t)$. Không cái nào thực sự có biến đổi Fourier, vì tích phân Fourier không hội tụ với mọi $s$. Về vật lý cũng không tạo được: $\\sin t$ phải bật từ vô hạn trước đó, $H(t)$ phải giữ không đổi vô hạn lâu, $\\delta(t)$ phải vô cùng lớn trong thời gian vô cùng ngắn (tr. 8).||"
                 "We often replace a physical quantity by a neat expression such as $\\sin t$, $H(t)$ and $\\delta(t)$. None strictly has a Fourier transform because the Fourier integral does not converge for all $s$. Physically none can be made either: $\\sin t$ would have to be switched on an infinite time ago, $H(t)$ held steady for an infinite time, $\\delta(t)$ infinitely large for an infinitely short time (p. 8).⟧</p>"),
                ("⟦Hai điều kiện đủ||Two sufficient conditions⟧",
                 "<p>⟦Biến đổi rồi biến đổi ngược một hàm đơn trị $f(x)$ trả lại $f(x)$, hoặc $\\tfrac12[f(x^+)+f(x^-)]$ tại điểm gián đoạn, với điều kiện (tr. 9):||"
                 "Transforming and retransforming a single-valued function $f(x)$ returns $f(x)$, or $\\tfrac12[f(x^+)+f(x^-)]$ at a discontinuity, provided (p. 9):⟧</p>"
                 + OL(["⟦Tích phân của $|f(x)|$ trên toàn trục tồn tại.||The integral of $|f(x)|$ over the whole axis exists.⟧", "⟦Mọi điểm gián đoạn của $f(x)$ đều hữu hạn.||Any discontinuities of $f(x)$ are finite.⟧"])
                 + F("⟦Điều kiện khả tích tuyệt đối||Absolute integrability⟧", r"\int_{-\infty}^{\infty}|f(x)|\,dx<\infty")),
                ("⟦Đối ngẫu: năng lượng vô hạn vi phạm cả hai||Duality: infinite energy violates both⟧",
                 "<p>⟦Trong thực tế hai điều kiện bị vi phạm khi năng lượng vô hạn. Dòng điện một chiều chảy mãi mãi có năng lượng vô hạn nên vi phạm điều kiện thứ nhất; phân bố năng lượng theo tần số khi đó dồn vô hạn vào tần số 0, vi phạm điều kiện thứ hai. Sóng điều hòa cũng vậy (tr. 9).||"
                 "In physical terms the conditions are violated when there is infinite energy. Direct current that has always flowed represents infinite energy and violates the first condition; the energy distribution over frequency would have infinite energy concentrated at zero frequency and violates the second. The same applies to harmonic waves (p. 9).⟧</p>"),
                ("⟦Vô số cực đại: $\\sin(1/x)$ và biến phân bị chặn||Infinitely many maxima: $\\sin(1/x)$ and bounded variation⟧",
                 "<p>⟦Thường có người nói hàm có vô số cực đại và cực tiểu trong một đoạn hữu hạn thì không có biến đổi, ví dụ $\\sin(1/x)$. Bracewell ghi nhận điều đó không quan trọng trong thực tế, và một số hàm như vậy vẫn có biến đổi. Điều kiện biến phân bị chặn, điều kiện Lipschitz và điều kiện Dini là các mức nới rộng khác (tr. 9).||"
                 "It is sometimes stated that infinitely many maxima and minima in a finite interval disqualify a function, the stock example being $\\sin(1/x)$. Bracewell notes this is unimportant in real life and that some such functions do have transforms. Bounded variation, a Lipschitz condition and Dini's condition are further relaxations (p. 9).⟧</p>"),
                ("⟦Biến đổi trong giới hạn: nhân với hàm tắt dần||Transforms in the limit: multiply by a decaying factor⟧",
                 "<p>⟦Hàm tuần hoàn $P(x)$ không có biến đổi vì $\\int|P|$ không tồn tại. Nhân với $e^{-\\alpha x^2}$ ($\\alpha$ nhỏ dương) thì hàm mới có thể có biến đổi. Cho $\\alpha\\to0$, dãy hàm tiến về $P(x)$, và dãy biến đổi tương ứng định nghĩa một hàm suy rộng. Cặp gồm hàm tuần hoàn và hàm suy rộng đó là một cặp biến đổi trong giới hạn (tr. 10).||"
                 "A periodic function $P(x)$ has no transform because $\\int|P|$ does not exist. Multiply by $e^{-\\alpha x^2}$ ($\\alpha$ small and positive) and the modified function may have one. As $\\alpha\\to0$ the modified functions approach $P(x)$, and the corresponding sequence of transforms defines a generalized function. The periodic function and the generalized function form a transform pair in the limit (p. 10).⟧</p>"
                 + F("⟦Dãy hàm điều chế||Modulating sequence⟧", r"P_\alpha(x)=e^{-\alpha x^2}P(x)\ \xrightarrow{\ \alpha\to0\ }\ P(x)")),
                ("⟦Thử số: $e^{-\\alpha x^2}\\cos(10\\pi x)$ khi $\\alpha\\to0$||Numerical test: $e^{-\\alpha x^2}\\cos(10\\pi x)$ as $\\alpha\\to0$⟧",
                 "<p>⟦Phổ có hai đỉnh tại $s=\\pm5$. Chiều cao đỉnh tại $s=5$ là {{peak_a1}} ($\\alpha=1$), {{peak_a01}} ($\\alpha=0.1$), {{peak_a001}} ($\\alpha=0.01$), tăng như $\\tfrac12\\sqrt{\\pi/\\alpha}$ không có giới hạn. Độ rộng đỉnh co lại {{width_a1}}, {{width_a01}}, {{width_a001}}. Diện tích mỗi đỉnh luôn là {{area_peak}}. Dãy không có giới hạn theo từng điểm nhưng tiến về cặp xung $\\tfrac12\\delta(s-5)+\\tfrac12\\delta(s+5)$.||"
                 "The spectrum has two peaks at $s=\\pm5$. The height at $s=5$ is {{peak_a1}} ($\\alpha=1$), {{peak_a01}} ($\\alpha=0.1$), {{peak_a001}} ($\\alpha=0.01$), growing like $\\tfrac12\\sqrt{\\pi/\\alpha}$ without limit. The peak width shrinks {{width_a1}}, {{width_a01}}, {{width_a001}}. The area of each peak is always {{area_peak}}. The sequence has no pointwise limit but tends to the impulse pair $\\tfrac12\\delta(s-5)+\\tfrac12\\delta(s+5)$.⟧</p>{{fig:limit_gauss}}"),
                ("⟦Hàm suy rộng và cặp giới hạn||Generalized functions and limit pairs⟧",
                 "<p>⟦Ý tưởng làm việc với thứ không phải hàm nhưng mô tả được bằng dãy hàm đã quen trong vật lý qua ký hiệu xung. Trong cặp giới hạn của hàm tuần hoàn, chỉ một thành viên là hàm suy rộng có xung. Nếu vừa xung vừa tuần hoàn thì cả hai thành viên đều là hàm suy rộng. Định nghĩa chặt chẽ được hoãn tới chương 5 và 6 (tr. 10 đến 11).||"
                 "Dealing with things that are not functions but are describable by sequences of functions is familiar in physics through the impulse symbol. In the limit pair of a periodic function, only one member is a generalized function involving impulses. If something is both impulsive and periodic, both members are generalized functions. The rigorous definition is deferred to chapters 5 and 6 (pp. 10 to 11).⟧</p>"),
                ("⟦Thử số và bài tập 3: hàm dấu||Numerical test and problem 3: the sign function⟧",
                 "<p>⟦Bài tập 3 cho biết biến đổi trong giới hạn của $\\text{sgn}\\,x$ là $(i\\pi s)^{-1}$. Nhân với $e^{-\\alpha|x|}$: phần ảo của biến đổi tại $s=0.5$ là {{sgn_a01}} ($\\alpha=0.1$), {{sgn_a001}} ($\\alpha=0.01$), {{sgn_a0001}} ($\\alpha=0.001$), tiến về {{sgn_limit}} $=-1/(\\pi s)$. Tích phân số và công thức đóng trùng nhau ở mọi $\\alpha$.||"
                 "Problem 3 states that the transform in the limit of $\\text{sgn}\\,x$ is $(i\\pi s)^{-1}$. With the factor $e^{-\\alpha|x|}$: the imaginary part of the transform at $s=0.5$ is {{sgn_a01}} ($\\alpha=0.1$), {{sgn_a001}} ($\\alpha=0.01$), {{sgn_a0001}} ($\\alpha=0.001$), approaching {{sgn_limit}} $=-1/(\\pi s)$. Numerical integration and the closed form agree at every $\\alpha$.⟧</p>"
                 + F("⟦Biến đổi của $\\text{sgn}\\,x\\,e^{-\\alpha|x|}$||Transform of $\\text{sgn}\\,x\\,e^{-\\alpha|x|}$⟧", r"\frac{-i\,4\pi s}{\alpha^2+4\pi^2s^2}\ \xrightarrow{\ \alpha\to0\ }\ \frac{1}{i\pi s}")),
            ]),
        # ---------------------------------------------------------------- PART 3
        dict(
            title="⟦Chẵn, lẻ và đối xứng||Even, odd and symmetry⟧",
            scr=("⟦Lập luận đối xứng cho thấy nhiều tích phân triệt tiêu mà không cần tính.||Symmetry arguments show that many integrals vanish without evaluating them.⟧",
                 "⟦Nhưng cần tỉnh táo để khai thác đủ đối xứng, cả ở hàm lẫn ở biến đổi của nó.||But it takes alertness to exploit the symmetry fully, in the function and in its transform.⟧",
                 "⟦Tách thành phần chẵn và lẻ, rồi đọc bảng đối xứng thực, ảo, chẵn, lẻ, Hermitian.||Split into even and odd parts, then read the table of real, imaginary, even, odd and Hermitian symmetry.⟧"),
            preview=["⟦Tách chẵn lẻ duy nhất và phụ thuộc gốc||The unique even-odd split and its dependence on the origin⟧",
                     "⟦Bảng đối xứng và kiểm số||The symmetry table and its numerical check⟧",
                     "⟦Hàm Hermitian||Hermitian functions⟧"],
            slides=[
                ("⟦Hàm chẵn và hàm lẻ||Even and odd functions⟧",
                 "<p>⟦Hàm $E(x)$ mà $E(-x)=E(x)$ là đối xứng hay chẵn; hàm $O(x)$ mà $O(-x)=-O(x)$ là phản đối xứng hay lẻ. Tổng của hàm chẵn và hàm lẻ nói chung không chẵn cũng không lẻ (Bracewell, tr. 11).||"
                 "A function $E(x)$ with $E(-x)=E(x)$ is symmetrical or even; $O(x)$ with $O(-x)=-O(x)$ is antisymmetrical or odd. The sum of even and odd functions is in general neither (Bracewell, p. 11).⟧</p>"),
                ("⟦Tách duy nhất thành phần chẵn và lẻ||The unique even and odd parts⟧",
                 "<p>⟦Mọi hàm tách được duy nhất thành phần chẵn và lẻ. Chứng minh: nếu $f=E_1+O_1=E_2+O_2$ thì $E_1-E_2=O_2-O_1$ vừa chẵn vừa lẻ nên bằng 0 (tr. 11). Phần chẵn là trung bình của hàm và ảnh phản chiếu qua trục đứng, phần lẻ là trung bình của hàm và ảnh phản chiếu âm (tr. 12).||"
                 "Any function splits uniquely into even and odd parts. Proof: if $f=E_1+O_1=E_2+O_2$ then $E_1-E_2=O_2-O_1$ is both even and odd, hence zero (p. 11). The even part is the mean of the function and its reflection in the vertical axis, the odd part is the mean of the function and its negative reflection (p. 12).⟧</p>"
                 + F("⟦Tách chẵn lẻ||Even-odd split⟧", r"E(x)=\tfrac12\left[f(x)+f(-x)\right],\qquad O(x)=\tfrac12\left[f(x)-f(-x)\right]")),
                ("⟦Ví dụ: $e^{-x}H(x)$ và $e^{x}$||Examples: $e^{-x}H(x)$ and $e^{x}$⟧",
                 "<p>⟦Với $e^{-x}H(x)$: phần chẵn là $\\tfrac12e^{-|x|}$, phần lẻ là $\\tfrac12\\text{sgn}(x)e^{-|x|}$. Tại $x=1$ cả hai bằng {{ev1}}; tại $x=-1$ phần chẵn vẫn {{ev1}} còn phần lẻ là {{od_m1}}. Với $e^{x}$: phần chẵn là $\\cosh x$ ({{cosh1}} tại $x=1$) và phần lẻ là $\\sinh x$ ({{sinh1}}). Đây là bài tập 6 của Bracewell.||"
                 "For $e^{-x}H(x)$: the even part is $\\tfrac12e^{-|x|}$, the odd part $\\tfrac12\\text{sgn}(x)e^{-|x|}$. At $x=1$ both equal {{ev1}}; at $x=-1$ the even part is still {{ev1}} while the odd part is {{od_m1}}. For $e^{x}$: the even part is $\\cosh x$ ({{cosh1}} at $x=1$) and the odd part $\\sinh x$ ({{sinh1}}). This is Bracewell's problem 6.⟧</p>{{fig:symmetry}}"),
                ("⟦Phụ thuộc vào gốc tọa độ||Dependence on the origin⟧",
                 "<p>⟦Việc tách chẵn lẻ đổi theo gốc của $x$. Hàm $\\cos x$ hoàn toàn chẵn, nhưng dịch gốc một phần tư chu kỳ thì thành $\\sin x$ hoàn toàn lẻ (tr. 12). Vì thế \"chẵn hay lẻ\" luôn phải nói kèm gốc.||"
                 "The even-odd split changes with the origin of $x$. The function $\\cos x$ is fully even, but shifting the origin by a quarter period turns it into $\\sin x$, fully odd (p. 12). So \"even or odd\" must always be stated with the origin.⟧</p>"),
                ("⟦Bài tập 17: tổng năng lượng chẵn và lẻ bất biến||Problem 17: the even-plus-odd energy is invariant⟧",
                 "<p>⟦Tổng $\\int|o|^2dx+\\int|e|^2dx$ không đổi khi dịch gốc, và bằng $\\int|f|^2dx$ vì tích chéo chẵn nhân lẻ tích phân bằng 0. Với $f=e^{-x^2}$ hằng số đó là $\\sqrt{\\pi/2}$ = {{energy_const}}. Phần năng lượng chẵn là {{ev_share_a0}} khi $a=0$, {{ev_share_a05}} khi $a=0.5$, {{ev_share_a1}} khi $a=1$, {{ev_share_a2}} khi $a=2$ (dịch xa gốc thì chia đều).||"
                 "The sum $\\int|o|^2dx+\\int|e|^2dx$ does not change when the origin shifts and equals $\\int|f|^2dx$ because the cross term even times odd integrates to zero. For $f=e^{-x^2}$ that constant is $\\sqrt{\\pi/2}$ = {{energy_const}}. The even share of the energy is {{ev_share_a0}} for $a=0$, {{ev_share_a05}} for $a=0.5$, {{ev_share_a1}} for $a=1$, {{ev_share_a2}} for $a=2$ (far from the origin it splits evenly).⟧</p>"),
                ("⟦Ý nghĩa: biến đổi của phần chẵn và lẻ||Meaning: the transforms of the even and odd parts⟧",
                 "<p>⟦Viết $f=E+O$ với $E,O$ có thể phức. Biến đổi Fourier rút về hai tích phân cosin và sin. Từ đó hàm chẵn có biến đổi chẵn, hàm lẻ có biến đổi lẻ (tr. 13).||"
                 "Write $f=E+O$ with $E,O$ possibly complex. The Fourier transform reduces to a cosine and a sine integral. Hence an even function has an even transform and an odd function an odd transform (p. 13).⟧</p>"
                 + F("⟦Biến đổi qua cosin và sin||Transform through cosine and sine⟧", r"F(s)=2\int_0^{\infty}E(x)\cos2\pi xs\,dx\;-\;2i\int_0^{\infty}O(x)\sin2\pi xs\,dx")),
                ("⟦Bảng đối xứng của Bracewell||Bracewell's symmetry table⟧",
                 "<p>⟦Bảng ở trang 13 đến 14 cho biết dạng đối xứng của $F(s)$ theo dạng đối xứng của $f(x)$ (hình 2.5, tr. 15):||The table on pp. 13 to 14 gives the symmetry of $F(s)$ from the symmetry of $f(x)$ (Fig. 2.5, p. 15):⟧</p>"
                 + TBL(["$f(x)$", "$F(s)$"],
                       [["⟦thực và chẵn||real and even⟧", "⟦thực và chẵn||real and even⟧"], ["⟦thực và lẻ||real and odd⟧", "⟦ảo và lẻ||imaginary and odd⟧"],
                        ["⟦ảo và chẵn||imaginary and even⟧", "⟦ảo và chẵn||imaginary and even⟧"], ["⟦ảo và lẻ||imaginary and odd⟧", "⟦thực và lẻ||real and odd⟧"],
                        ["⟦thực và không đối xứng||real and asymmetrical⟧", "Hermitian"], ["⟦thực chẵn cộng ảo lẻ (Hermitian)||real even plus imaginary odd (Hermitian)⟧", "⟦thực||real⟧"],
                        ["⟦thực lẻ cộng ảo chẵn (phản Hermitian)||real odd plus imaginary even (anti-Hermitian)⟧", "⟦ảo||imaginary⟧"]])),
                ("⟦Thử số: kiểm bảng bằng DFT||Numerical test: checking the table with the DFT⟧",
                 "<p>⟦Với dãy ngẫu nhiên có đối xứng dựng sẵn, DFT thoả mãn {{sym_ok}} trên {{sym_total}} dòng của bảng. Hệ quả kỹ thuật: tín hiệu thực có phổ Hermitian nên chỉ cần lưu nửa phổ. Tín hiệu thực 1000 mẫu có {{herm_full}} hệ số FFT nhưng chỉ {{herm_half}} hệ số độc lập, mà năng lượng {{herm_energy}} vẫn tính lại được đủ từ nửa phổ.||"
                 "With random sequences built to have each symmetry, the DFT satisfies {{sym_ok}} of {{sym_total}} rows of the table. An engineering consequence: a real signal has a Hermitian spectrum so only half of it need be stored. A real 1000-sample signal has {{herm_full}} FFT coefficients but only {{herm_half}} independent ones, and the energy {{herm_energy}} is fully recovered from the half spectrum.⟧</p>"),
            ]),
        # ---------------------------------------------------------------- PART 4
        dict(
            title="⟦Liên hợp phức, biến đổi cosin và sin||Complex conjugates, cosine and sine transforms⟧",
            scr=("⟦Bảng đối xứng chỉ cho biết dạng, chưa cho quan hệ chính xác giữa $f$, $f^*$ và $F$.||The symmetry table gives only the form, not the exact relations between $f$, $f^*$ and $F$.⟧",
                 "⟦Với hàm chỉ xác định ở nửa trục dương, biến đổi Fourier thường được thay bằng biến đổi cosin hoặc sin.||For a function defined only on the positive axis, the Fourier transform is often replaced by the cosine or sine transform.⟧",
                 "⟦Liên hợp phức cho tám quan hệ gọn, và biến đổi cosin và sin là biến đổi của các mở rộng chẵn và lẻ.||Conjugation gives eight compact relations, and the cosine and sine transforms are transforms of the even and odd extensions.⟧"),
            preview=["⟦Biến đổi của liên hợp phức và bảng quan hệ||Transform of the complex conjugate and the relation table⟧",
                     "⟦Biến đổi cosin và sin tự nghịch đảo||Cosine and sine transforms, each its own inverse⟧",
                     "⟦Hàm nhân quả||Causal functions⟧"],
            slides=[
                ("⟦Biến đổi của liên hợp phức||Transform of the complex conjugate⟧",
                 "<p>⟦Biến đổi Fourier của $f^*(x)$ là $F^*(-s)$, tức ảnh phản chiếu của liên hợp biến đổi. Với $f$ thực thì biến đổi của $f^*=f$ là $F(s)$, suy ra $F(s)=F^*(-s)$ (Bracewell, tr. 14).||"
                 "The Fourier transform of $f^*(x)$ is $F^*(-s)$, the reflection of the conjugate of the transform. For real $f$, the transform of $f^*=f$ is $F(s)$, so $F(s)=F^*(-s)$ (Bracewell, p. 14).⟧</p>"
                 + F("⟦Liên hợp phức||Complex conjugate⟧", r"f^*(x)\ \supset\ F^*(-s)")),
                ("⟦Hàm Hermitian||Hermitian functions⟧",
                 "<p>⟦Hàm có phần thực chẵn và phần ảo lẻ gọi là Hermitian, định nghĩa gọn bằng $f(x)=f^*(-x)$. Biến đổi của nó là thực. Chứng minh: $f=E+O+iE'+iO'$ thì $f^*(-x)=E-O-iE'+iO'$; đòi $f=f^*(-x)$ buộc $O=0$ và $E'=0$, còn $f=E+iO'$ (tr. 14).||"
                 "A function whose real part is even and imaginary part odd is called Hermitian, defined compactly by $f(x)=f^*(-x)$. Its transform is real. Proof: for $f=E+O+iE'+iO'$ we have $f^*(-x)=E-O-iE'+iO'$; requiring $f=f^*(-x)$ forces $O=0$ and $E'=0$, leaving $f=E+iO'$ (p. 14).⟧</p>"
                 + F("⟦Hermitian||Hermitian⟧", r"f(x)=f^*(-x)\;\Longrightarrow\;F(s)\ \text{real}")),
                ("⟦Bảng quan hệ tám dòng||The eight-line relation table⟧",
                 "<p>⟦Bracewell tổng hợp các cặp liên quan (tr. 16):||Bracewell tabulates the related pairs (p. 16):⟧</p>"
                 + TBL(["$f(x)$", "$F(s)$"],
                       [["$f(x)$", "$F(s)$"], ["$f^*(x)$", "$F^*(-s)$"], ["$f^*(-x)$", "$F^*(s)$"], ["$f(-x)$", "$F(-s)$"], ["$2\\,\\text{Re}\\,f$", "$F(s)+F^*(-s)$"],
                        ["$2i\\,\\text{Im}\\,f$", "$F(s)-F^*(-s)$"], ["$f(x)+f^*(-x)$", "$2\\,\\text{Re}\\,F$"], ["$f(x)-f^*(-x)$", "$2i\\,\\text{Im}\\,F$"]])),
                ("⟦Thử số: kiểm bảng bằng DFT||Numerical test: checking the table with the DFT⟧",
                 "<p>⟦Với dãy phức ngẫu nhiên, {{conj_ok}} trên 7 quan hệ không tầm thường trong bảng đều đúng tới sai số làm tròn, mỗi quan hệ được kiểm bằng phép so sánh trực tiếp hai vế qua DFT.||"
                 "For a random complex sequence, {{conj_ok}} of the 7 non-trivial relations in the table hold to rounding error, each checked by comparing both sides directly through the DFT.⟧</p>"),
                ("⟦Biến đổi cosin||The cosine transform⟧",
                 "<p>⟦Biến đổi cosin của $f(x)$ xác định cho $s>0$, chỉ dùng $f$ ở nửa dương. Nó trùng biến đổi Fourier nếu $f$ chẵn. Điều đặc biệt: phép thuận và ngược có cùng công thức nên biến đổi cosin tự nghịch đảo (tr. 16 đến 17).||"
                 "The cosine transform of $f(x)$ is defined for $s>0$ and uses $f$ only on the positive side. It agrees with the Fourier transform when $f$ is even. Notably, the forward and reverse operations have the same formula, so the cosine transform is its own inverse (pp. 16 to 17).⟧</p>"
                 + F("⟦Biến đổi cosin||Cosine transform⟧", r"F_c(s)=2\int_0^{\infty}f(x)\cos2\pi sx\,dx,\qquad f(x)=2\int_0^{\infty}F_c(s)\cos2\pi sx\,ds")),
                ("⟦Biến đổi sin||The sine transform⟧",
                 "<p>⟦Biến đổi sin cũng tự nghịch đảo. $i$ lần phần lẻ của biến đổi Fourier của $f$ bằng biến đổi sin của phần lẻ của $f$ khi $s>0$ (tr. 17). Nhờ đó tra bảng Fourier của hàm chẵn và lẻ ở chương 22 cho ra bảng cosin và sin.||"
                 "The sine transform is also its own inverse. $i$ times the odd part of the Fourier transform of $f$ equals the sine transform of the odd part of $f$, for $s>0$ (p. 17). So the Fourier tables of even and odd functions in chapter 22 give cosine and sine tables.⟧</p>"
                 + F("⟦Biến đổi sin||Sine transform⟧", r"F_s(s)=2\int_0^{\infty}f(x)\sin2\pi sx\,dx,\qquad f(x)=2\int_0^{\infty}F_s(s)\sin2\pi sx\,ds")),
                ("⟦Hàm nhân quả: ghép cosin và sin||Causal functions: combining cosine and sine⟧",
                 "<p>⟦Nếu $f(x)=0$ với $x<0$ thì $F(s)=\\tfrac12F_c(s)-\\tfrac12iF_s(s)$ (tr. 17). Với $f=e^{-x}H(x)$ tại $s=0.2$: $F_c={{fc_02}}$, $F_s={{fs_02}}$, nên $F={{f_re_02}}+({{f_im_02}})\\,i$, trùng $1/(1+i2\\pi s)$. Biến đổi Fourier của phần mở rộng chẵn $e^{-|x|}$ cũng cho {{fc_02}}, đúng $F_c$; và biến đổi cosin ngược thu lại $f(1)={{f1_rec}}$.||"
                 "If $f(x)=0$ for $x<0$ then $F(s)=\\tfrac12F_c(s)-\\tfrac12iF_s(s)$ (p. 17). For $f=e^{-x}H(x)$ at $s=0.2$: $F_c={{fc_02}}$, $F_s={{fs_02}}$, so $F={{f_re_02}}+({{f_im_02}})\\,i$, matching $1/(1+i2\\pi s)$. The Fourier transform of the even extension $e^{-|x|}$ also gives {{fc_02}}, exactly $F_c$; and the inverse cosine transform recovers $f(1)={{f1_rec}}$.⟧</p>"),
                ("⟦Cẩn thận khi đọc bảng cosin và sin||Care when reading cosine and sine tables⟧",
                 "<p>⟦Các bảng lớn thường định nghĩa $g(\\omega)=\\int_0^\\infty f(x)\\sin\\omega x\\,dx$, tức dùng tần số góc và không có hệ số 2. Bracewell lưu ý một hằng số bị \"giấu\" sẽ trở lại khi đảo phép biến đổi (tr. 17). Trước khi dùng bảng ngoài, hãy đối chiếu định nghĩa và hệ số $2\\pi$.||"
                 "Major tables often define $g(\\omega)=\\int_0^\\infty f(x)\\sin\\omega x\\,dx$, i.e. with angular frequency and no factor 2. Bracewell warns that an apparently suppressed constant raises its head when the transformation is reversed (p. 17). Before using an outside table, compare the definition and the $2\\pi$ factor.⟧</p>"),
            ]),
        # ---------------------------------------------------------------- PART 5
        dict(
            title="⟦Diễn giải tích phân Fourier bằng hình||Interpreting the Fourier integral pictorially⟧",
            scr=("⟦Người quen với phân tích Fourier thường hình dung tích phân Fourier chứ không đọc công thức.||Habitués of Fourier analysis picture the Fourier integral rather than read the formula.⟧",
                 "⟦Có ba cách hình dung và mỗi cách trả lời một câu hỏi khác nhau về cùng một tích phân.||There are three pictures and each answers a different question about the same integral.⟧",
                 "⟦Diện tích dưới $f\\cos$, cosinusoid theo $s$, và xoắn ốc trên mặt phẳng phức, cùng thư mục và bài tập của chương.||The area under $f\\cos$, the cosinusoid as a function of $s$, and the spiral on the complex plane, plus the chapter's bibliography and problems.⟧"),
            preview=["⟦Ba hình và số đo kèm theo||Three pictures and their numbers⟧",
                     "⟦Ứng dụng của giản đồ xoắn ốc||Applications of the spiral diagram⟧",
                     "⟦Thư mục và bài tập||Bibliography and problems⟧"],
            slides=[
                ("⟦Hình thứ nhất: diện tích dưới $f(x)\\cos2\\pi sx$||Picture one: the area under $f(x)\\cos2\\pi sx$⟧",
                 "<p>⟦Với $f(x)$ cho trước, hình dung $f(x)\\cos2\\pi sx$ là dao động nằm trong đường bao $\\pm f(x)$. Hai lần diện tích phía dưới (với $x>0$) là $F_c(s)$. Tần số $s$ là số chu kỳ trên một đơn vị của $x$ (Bracewell, tr. 18).||"
                 "Given $f(x)$, picture $f(x)\\cos2\\pi sx$ as an oscillation within the envelope $\\pm f(x)$. Twice the area under it (for $x>0$) is $F_c(s)$. The frequency $s$ is the number of cycles per unit of $x$ (Bracewell, p. 18).⟧</p>"),
                ("⟦Thử số: diện tích thấp và cao tần||Numerical test: area at low and high frequency⟧",
                 "<p>⟦Với $f=e^{-\\pi x^2}$: tại $s=0.25$ diện tích (chính là $F$) là {{area_low}}, còn tại $s=2$ chỉ {{area_high}}, gần như bằng 0 vì dao động nhanh làm các nửa chu kỳ dương và âm triệt tiêu nhau. Tại $s=0$, diện tích là $\\int f$.||"
                 "For $f=e^{-\\pi x^2}$: at $s=0.25$ the area (which is $F$) is {{area_low}}, while at $s=2$ it is only {{area_high}}, almost zero because rapid oscillation makes the positive and negative half-cycles cancel. At $s=0$ the area is $\\int f$.⟧</p>{{fig:interpretation}}"
                 + F("⟦Hai giá trị biên||Two limiting values⟧", r"F(s)\to0\ (s\to\infty),\qquad F(0)=\int_{-\infty}^{\infty}f(x)\,dx")),
                ("⟦Hình thứ hai: cosinusoid biên độ $f(x)\\,dx$ theo $s$||Picture two: a cosinusoid of amplitude $f(x)\\,dx$ as a function of $s$⟧",
                 "<p>⟦Ngược lại, coi $f(x)\\cos2\\pi xs\\,dx$ là một cosinusoid theo $s$ với biên độ $f(x)\\,dx$ và tần số $x$. Cộng các đường như vậy cho mọi $x$ ta được $F_c(s)$ (hình 2.8, tr. 18 đến 19). Đây là cách nhìn quen thuộc khi cộng đồ thị các cosin có tần số tăng dần trong chuỗi Fourier.||"
                 "Conversely, regard $f(x)\\cos2\\pi xs\\,dx$ as a cosinusoid in $s$ with amplitude $f(x)\\,dx$ and frequency $x$. Summing such curves over all $x$ gives $F_c(s)$ (Fig. 2.8, pp. 18 to 19). This is the familiar picture from graphically adding cosinusoids of arithmetically increasing frequency in Fourier series.⟧</p>"),
                ("⟦Phân tích và tổng hợp là cùng một phép làm||Analysis and synthesis are the same operation⟧",
                 "<p>⟦Mỗi cách nhìn có hai mặt: phân tích hàm thành thành phần, hoặc tổng hợp hàm từ thành phần. Việc phân tích hay tổng hợp đều làm cùng một việc phản ánh tính tương hỗ của biến đổi Fourier. Mặt $f(x)\\cos2\\pi sx$ cắt theo hai cách, theo $s$ cố định hoặc theo $x$ cố định (tr. 19 đến 20, hình 2.9).||"
                 "Each viewpoint has dual aspects: analysis of a function into components or synthesis from components. That analyzing and synthesizing do the same thing simply reflects the reciprocal property of the transform. The surface $f(x)\\cos2\\pi sx$ can be sliced two ways, at fixed $s$ or at fixed $x$ (pp. 19 to 20, Fig. 2.9).⟧</p>"),
                ("⟦Hình thứ ba: xoắn ốc trên mặt phẳng phức||Picture three: the spiral on the complex plane⟧",
                 "<p>⟦Cố định $s$. Vector $f(x)\\,dx$ bị quay góc $2\\pi sx$ bởi $\\exp(-i2\\pi sx)$. Khi $x\\to\\pm\\infty$, biên độ co lại và góc quay tiếp tục nên tích phân xoắn vào hai điểm giới hạn $A$ và $B$, và vector $AB$ là $F(s)$. Với $s$ lớn, xoắn ốc cuộn nhanh hơn (hình 2.10, tr. 20).||"
                 "Fix $s$. The vector $f(x)\\,dx$ is rotated through an angle $2\\pi sx$ by $\\exp(-i2\\pi sx)$. As $x\\to\\pm\\infty$ the amplitude shrinks and the angle keeps turning, so the integral spirals into two limiting points $A$ and $B$, and the vector $AB$ is $F(s)$. For larger $s$ the spiral coils faster (Fig. 2.10, p. 20).⟧</p>"),
                ("⟦Thử số: xoắn ốc của $e^{-x}H(x)$||Numerical test: the spiral of $e^{-x}H(x)$⟧",
                 "<p>⟦Tích phân tích lũy $\\int_0^Xe^{-x}e^{-i2\\pi sx}dx$ xoắn về $1/(1+i2\\pi s)$. Độ dài vector giới hạn là {{spiral_abs_01}} khi $s=0.1$ và chỉ {{spiral_abs_05}} khi $s=0.5$: $s$ lớn cuộn nhanh hơn và $|F|$ nhỏ hơn. Tích phân số tích lũy trùng công thức đóng.||"
                 "The cumulative integral $\\int_0^Xe^{-x}e^{-i2\\pi sx}dx$ spirals into $1/(1+i2\\pi s)$. The limiting vector has length {{spiral_abs_01}} for $s=0.1$ and only {{spiral_abs_05}} for $s=0.5$: larger $s$ coils faster and $|F|$ is smaller. The cumulative numerical integral matches the closed form.⟧</p>{{fig:spiral}}"),
                ("⟦Giản đồ xoắn ốc trong quang học và vô tuyến||Spiral diagrams in optics and radio⟧",
                 "<p>⟦Loại giản đồ này gần với xoắn ốc Cornu, quen thuộc trong nhiễu xạ quang học. Nó là công cụ hữu ích cho tư duy định tính lẫn tính số trong quang học và ăng-ten, xuất hiện khi sóng vô tuyến lan truyền, và tóm gọn cách các tiếng vọng vô tuyến phản xạ từ vệt sao băng ion hóa hình thành (tr. 20). Chương 15 sẽ dùng lại.||"
                 "This kind of diagram is related to Cornu's spiral, familiar from optical diffraction. It is a useful tool for qualitative thinking and numerical work in optics and antennas, arises in radio-wave propagation, and neatly summarises the behaviour of radio echoes reflected from ionized meteor trails as they form (p. 20). Chapter 15 will reuse it.⟧</p>"),
                ("⟦Thư mục của chương||The chapter's bibliography⟧",
                 "<p>⟦Chương liệt kê các sách chuẩn về tích phân Fourier và các sách hướng kỹ thuật điện: Wiener (1933), Titchmarsh (1937), Bochner (1948), Bochner và Chandrasekharan (1949), Lighthill (1958), Papoulis (1962), Champeney (1973) và nhiều sách khác. Cũng có các bảng tích phân Fourier như Campbell và Foster (1948), Erdélyi (1954). Bảng biến đổi Laplace một phía chỉ cho biến đổi Fourier của hàm bằng 0 với đối số âm (tr. 21 đến 22).||"
                 "The chapter lists standard texts on the Fourier integral and later books oriented to electrical engineering: Wiener (1933), Titchmarsh (1937), Bochner (1948), Bochner and Chandrasekharan (1949), Lighthill (1958), Papoulis (1962), Champeney (1973) and more. It also lists tables of Fourier integrals such as Campbell and Foster (1948) and Erdélyi (1954). Tables of the one-sided Laplace transform are sources of Fourier transforms only of functions zero for negative arguments (pp. 21 to 22).⟧</p>"),
                ("⟦Bài tập chương 2 và cách khóa dùng chúng||Chapter 2 problems and how this course uses them⟧",
                 "<p>⟦Chương có 21 bài tập (tr. 22 đến 23). Notebook của module này kiểm số cho một số bài: bài 3 (biến đổi trong giới hạn của $\\text{sgn}\\,x$), bài 6 (phần chẵn và lẻ), bài 10 (bốn lần biến đổi trả lại $f$), bài 13 và 14 (đối xứng), bài 17 (hằng số năng lượng), bài 19 (xoắn ốc), bài 20 (hàm tự biến đổi). Lời giải các bài chọn nằm ở chương 21 của sách.||"
                 "The chapter has 21 problems (pp. 22 to 23). This module's notebook checks numerically several of them: problem 3 (transform in the limit of $\\text{sgn}\\,x$), 6 (even and odd parts), 10 (four transforms return $f$), 13 and 14 (symmetry), 17 (energy constant), 19 (the spiral), 20 (self-transforming functions). Solutions to selected problems are in chapter 21 of the book.⟧</p>"
                 + C("info", "⟦Liên hệ chéo||Cross-reference⟧", "<p>⟦Hàm đặc trưng trong Barkat (mục 1.4.2) chính là một biến đổi Fourier của mật độ xác suất; module 10 ghép hai sách ở điểm này.||The characteristic function in Barkat (section 1.4.2) is a Fourier transform of the probability density; module 10 merges the two books at this point.⟧</p>")),
            ]),
    ],
    takeaways=[
        "⟦Hai lần biến đổi bằng cùng công thức trả về $f(-x)$; muốn đảo ngược dùng biến đổi \"cộng i\".||Two transforms with the same formula return $f(-x)$; to invert, use the \"plus-i\" transform.⟧",
        "⟦Tại điểm gián đoạn, biến đổi ngược trả về trung bình hai giới hạn.||At a discontinuity the inverse transform returns the mean of the two limits.⟧",
        "⟦Điều kiện đủ: $\\int|f|$ tồn tại và gián đoạn hữu hạn; các hàm còn lại dùng biến đổi trong giới hạn.||Sufficient: $\\int|f|$ exists and discontinuities are finite; other functions use transforms in the limit.⟧",
        "⟦Mọi hàm tách duy nhất thành phần chẵn và lẻ, và bảng đối xứng cho dạng của phổ.||Every function splits uniquely into even and odd parts, and the symmetry table gives the form of the spectrum.⟧",
        "⟦Tín hiệu thực có phổ Hermitian: chỉ cần nửa phổ.||A real signal has a Hermitian spectrum: half the spectrum suffices.⟧",
        "⟦Ba hình: diện tích dưới $f\\cos$, cosinusoid theo $s$, xoắn ốc trên mặt phẳng phức.||Three pictures: area under $f\\cos$, cosinusoid in $s$, spiral on the complex plane.⟧",
    ],
    history="<p>⟦Chương 2 nói rõ ngay từ đầu rằng phần lớn nội dung được nêu không chứng minh, vì chứng minh dài và là phần chính của các giáo trình chuỗi Fourier cổ điển (tr. 5). Bracewell muốn lấy công thức và điều kiện đã biết làm điểm xuất phát cho bàn về ứng dụng.||"
            "Chapter 2 says from the start that most of its material is stated without proof, because the proofs are lengthy and form the bulk of conventional Fourier studies (p. 5). Bracewell wants to take the formulas and their known conditions as the point of departure for applications.⟧</p>"
            "<p>⟦Các điều kiện tồn tại gắn với nhiều tên tuổi: khái niệm biến phân bị chặn, điều kiện Lipschitz và điều kiện Dini xuất hiện như những mức nới rộng khác nhau (tr. 9). Định lý tích phân Fourier có mặt trong các giáo trình chuẩn của Wiener (1933), Titchmarsh (1937) và Bochner (1948) mà chương liệt kê ở thư mục (tr. 21).||"
            "The existence conditions are tied to several names: bounded variation, a Lipschitz condition and Dini's condition appear as different relaxations (p. 9). Fourier's integral theorem appears in the standard texts of Wiener (1933), Titchmarsh (1937) and Bochner (1948) listed in the chapter's bibliography (p. 21).⟧</p>"
            "<p>⟦Hình xoắn ốc trên mặt phẳng phức gần với xoắn ốc Cornu của quang học và được dùng cho tiếng vọng vô tuyến từ vệt sao băng (tr. 20).||The spiral on the complex plane is related to Cornu's spiral of optics and is used for radio echoes from meteor trails (p. 20).⟧</p>",
    case="<p>⟦<b>Lưu một nửa phổ.</b> Một cảm biến ghi tín hiệu thực 1000 mẫu (tổng hai sóng hình sin). FFT đầy đủ có {{herm_full}} hệ số phức, nhưng nhờ đối xứng Hermitian của bảng chương 2 chỉ cần {{herm_half}} hệ số (<code>rfft</code>), tiết kiệm gần một nửa bộ nhớ và thời gian. Năng lượng {{herm_energy}} của tín hiệu tính lại đủ từ nửa phổ (cộng đôi các ô trung gian), nên không mất thông tin.||"
          "<b>Storing half a spectrum.</b> A sensor records a real 1000-sample signal (a sum of two sinusoids). The full FFT has {{herm_full}} complex coefficients, but thanks to the Hermitian symmetry in chapter 2's table only {{herm_half}} are needed (<code>rfft</code>), saving nearly half the memory and time. The signal energy {{herm_energy}} is fully recovered from the half spectrum (doubling the interior bins), so no information is lost.⟧</p>"
         "<p>⟦Cùng một nguyên lý giải thích vì sao phổ biên độ của tín hiệu thực chẵn và phổ pha lẻ, và vì sao ở tiếp theo ta chỉ vẽ tần số dương.||The same principle explains why the amplitude spectrum of a real signal is even and its phase spectrum odd, and why we later plot only positive frequencies.⟧</p>",
    practice=[
        "⟦Mở notebook và chạy cell cài đặt.||Open the notebook and run the setup cell.⟧",
        "⟦Bài 1: tính tích phân số biến đổi Fourier của Gauss, sech, $\\Pi$, $\\Lambda$ và so với công thức đóng; thử thêm hàm $e^{-2|x|}$ và dự đoán trước.||Task 1: numerically integrate the Fourier transform of the Gaussian, sech, $\\Pi$, $\\Lambda$ and compare with the closed forms; try $e^{-2|x|}$ and predict first.⟧",
        "⟦Bài 2: cắt biến đổi ngược ở $S$ khác nhau và quan sát giá trị tại chỗ nhảy của $\\Pi$.||Task 2: cut the inverse transform at different $S$ and watch the value at the jump of $\\Pi$.⟧",
        "⟦Bài 3: đổi $\\alpha$ và tần số 5 của dãy Gauss điều chế, kiểm chiều cao, độ rộng và diện tích đỉnh.||Task 3: change $\\alpha$ and the frequency 5 of the modulated Gaussians and check the height, width and area of the peak.⟧",
        "⟦Bài 4: tự dựng dãy có mỗi loại đối xứng và kiểm bảng bằng DFT; tự viết thêm dòng $f(x)\\cdot$ thực lẻ của riêng bạn.||Task 4: build a sequence with each symmetry and check the table with the DFT; write your own extra row for a real odd $f$.⟧",
        "⟦Bài 5: vẽ xoắn ốc cho $s$ khác và đoán đường đi trước khi vẽ.||Task 5: plot the spiral for other $s$ and guess the path before plotting.⟧",
    ],
    pitfalls=[
        "<b>⟦\"Hai lần biến đổi luôn trả về $f(x)$.\"||\"Two transforms always return $f(x)$.\"⟧</b><p>⟦Chỉ đúng với hàm chẵn. Nói chung kết quả là $f(-x)$; muốn $f(x)$ phải dùng biến đổi \"cộng i\" hoặc làm bốn lần (tr. 5 đến 6).||True only for even functions. In general the result is $f(-x)$; to get $f(x)$ use the \"plus-i\" transform or apply it four times (pp. 5 to 6).⟧</p>",
        "<b>⟦\"Tích phân Fourier tại điểm gián đoạn cho giá trị của hàm.\"||\"The Fourier integral at a discontinuity returns the function value.\"⟧</b><p>⟦Nó cho trung bình hai giới hạn hai phía: {{thm_s100}} tại chỗ nhảy của $\\Pi$ thay vì 1 hoặc 0.||It returns the mean of the two one-sided limits: {{thm_s100}} at the jump of $\\Pi$ instead of 1 or 0.⟧</p>",
        "<b>⟦\"Dãy biến đổi của hàm điều chế phải hội tụ từng điểm.\"||\"The sequence of transforms of the modulated functions must converge pointwise.\"⟧</b><p>⟦Không: đỉnh tại $s=5$ tăng tới {{peak_a001}} và hơn nữa khi $\\alpha\\to0$. Chỉ diện tích ({{area_peak}}) ổn định, và dãy định nghĩa một hàm suy rộng (tr. 10).||No: the peak at $s=5$ grows to {{peak_a001}} and beyond as $\\alpha\\to0$. Only the area ({{area_peak}}) is stable, and the sequence defines a generalized function (p. 10).⟧</p>",
        "<b>⟦\"Chẵn hay lẻ là tính chất cố hữu của hàm.\"||\"Even or odd is an intrinsic property of a function.\"⟧</b><p>⟦Nó phụ thuộc gốc tọa độ: $\\cos x$ chẵn, nhưng dịch gốc thì thành $\\sin x$ lẻ (tr. 12). Tổng năng lượng chẵn và lẻ ({{energy_const}} với $e^{-x^2}$) mới là bất biến.||It depends on the origin: $\\cos x$ is even, but shifting the origin makes it odd $\\sin x$ (p. 12). Only the sum of even and odd energies ({{energy_const}} for $e^{-x^2}$) is invariant.⟧</p>",
        "<b>⟦\"Bảng cosin và sin từ sách khác dùng ngay được.\"||\"Cosine and sine tables from other books can be used directly.\"⟧</b><p>⟦Định nghĩa có thể khác hệ số 2 và $2\\pi$; hãy đối chiếu trước (tr. 17).||The definitions may differ by factors of 2 and $2\\pi$; compare them first (p. 17).⟧</p>",
    ],
    refs=[
        "⟦R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chương 2 (tr. 5 đến 23).||R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chapter 2 (pp. 5 to 23).⟧",
        "⟦M. Barkat, <i>Signal Detection and Estimation</i>, 2nd ed., Artech House, 2005, mục 1.4.2 (hàm đặc trưng), chỉ dẫn tới ở phần liên hệ chéo.||M. Barkat, <i>Signal Detection and Estimation</i>, 2nd ed., Artech House, 2005, section 1.4.2 (characteristic function), cited only in the cross-reference.⟧",
    ],
    quiz=[
        dict(q="⟦Biến đổi Fourier của xung chữ nhật $\\Pi(x)$ tại $s=0.5$ bằng bao nhiêu?||What is the Fourier transform of the rectangle $\\Pi(x)$ at $s=0.5$?⟧",
             opts=["{{pi_05}}", "0.3183", "0.7854", "0.4053"],
             explain="⟦Biến đổi của $\\Pi$ là $\\text{sinc}\\,s$, nên $\\text{sinc}(0.5)=2/\\pi$ = {{pi_05}}; tích phân số trùng.||The transform of $\\Pi$ is $\\text{sinc}\\,s$, so $\\text{sinc}(0.5)=2/\\pi$ = {{pi_05}}; numerical integration agrees.⟧"),
        dict(q="⟦Biến đổi của $\\Pi(x)$ tại $s=2$ bằng bao nhiêu?||What is the transform of $\\Pi(x)$ at $s=2$?⟧",
             opts=["{{pi_2}}", "0.5", "0.1592", "0.3183"],
             explain="⟦$\\text{sinc}\\,s$ triệt tiêu tại mọi số nguyên khác 0, nên tại $s=2$ giá trị là {{pi_2}}.||$\\text{sinc}\\,s$ vanishes at every nonzero integer, so at $s=2$ the value is {{pi_2}}.⟧"),
        dict(q="⟦Biến đổi của xung tam giác $\\Lambda(x)$ tại $s=0.5$ bằng bao nhiêu?||What is the transform of the triangle $\\Lambda(x)$ at $s=0.5$?⟧",
             opts=["{{tri_05}}", "0.6366", "0.2026", "0.7071"],
             explain="⟦$\\Lambda\\supset\\text{sinc}^2s$, nên $(2/\\pi)^2$ = {{tri_05}}.||$\\Lambda\\supset\\text{sinc}^2s$, so $(2/\\pi)^2$ = {{tri_05}}.⟧"),
        dict(q="⟦Biến đổi của $e^{-|x|}$ tại $s=0.25$ bằng bao nhiêu?||What is the transform of $e^{-|x|}$ at $s=0.25$?⟧",
             opts=["{{expabs_025}}", "0.7071", "0.4559", "0.2884"],
             explain="⟦Công thức $2/(1+4\\pi^2s^2)$ cho {{expabs_025}}; tích phân số trùng.||The formula $2/(1+4\\pi^2s^2)$ gives {{expabs_025}}; numerical integration agrees.⟧"),
        dict(q="⟦Độ lớn $|F(0.1)|$ của biến đổi $e^{-x}H(x)$ là bao nhiêu?||What is the magnitude $|F(0.1)|$ of the transform of $e^{-x}H(x)$?⟧",
             opts=["{{causal_mag_01}}", "0.9524", "0.7071", "0.6283"],
             explain="⟦$|1/(1+i2\\pi s)|=1/\\sqrt{1+(0.2\\pi)^2}$ = {{causal_mag_01}}.||$|1/(1+i2\\pi s)|=1/\\sqrt{1+(0.2\\pi)^2}$ = {{causal_mag_01}}.⟧"),
        dict(q="⟦Pha của $F(0.1)$ (độ) với $f=e^{-x}H(x)$ là bao nhiêu?||What is the phase of $F(0.1)$ (degrees) for $f=e^{-x}H(x)$?⟧",
             opts=["{{causal_ph_01}}", "32.14", "-57.86", "-12.57"],
             explain="⟦$\\arg\\frac1{1+i2\\pi s}=-\\arctan(0.2\\pi)$ = {{causal_ph_01}} độ.||$\\arg\\frac1{1+i2\\pi s}=-\\arctan(0.2\\pi)$ = {{causal_ph_01}} degrees.⟧"),
        dict(q="⟦Biến đổi của $e^{-\\pi x^2}$ tại $s=0.5$ bằng bao nhiêu?||What is the transform of $e^{-\\pi x^2}$ at $s=0.5$?⟧",
             opts=["{{gauss_05}}", "0.6065", "0.3679", "0.7788"],
             explain="⟦Hàm này tự biến đổi: $e^{-\\pi/4}$ = {{gauss_05}}.||This function is self-transforming: $e^{-\\pi/4}$ = {{gauss_05}}.⟧"),
        dict(q="⟦Biến đổi của $\\text{sech}(\\pi x)$ tại $s=0.5$ bằng bao nhiêu?||What is the transform of $\\text{sech}(\\pi x)$ at $s=0.5$?⟧",
             opts=["{{sech_05}}", "0.4559", "0.6366", "0.4213"],
             explain="⟦$\\text{sech}(\\pi x)$ cũng tự biến đổi: $\\text{sech}(\\pi/2)$ = {{sech_05}}.||$\\text{sech}(\\pi x)$ is also self-transforming: $\\text{sech}(\\pi/2)$ = {{sech_05}}.⟧"),
        dict(q="⟦Cắt biến đổi ngược của $\\text{sinc}\\,s$ ở $|s|\\le100$ rồi tính tại chỗ nhảy $x=0.5$ của $\\Pi$: kết quả gần bằng bao nhiêu?||Truncate the inverse transform of $\\text{sinc}\\,s$ at $|s|\\le100$ and evaluate at the jump $x=0.5$ of $\\Pi$: what is the result, approximately?⟧",
             opts=["{{thm_s100}}", "0.9995", "0.2498", "0.7496"],
             explain="⟦Định lý tích phân Fourier cho trung bình $\\tfrac12(1+0)$; với $S=100$ đo được {{thm_s100}}.||Fourier's integral theorem gives the mean $\\tfrac12(1+0)$; for $S=100$ we measure {{thm_s100}}.⟧"),
        dict(q="⟦Với $e^{-\\alpha x^2}\\cos(10\\pi x)$, chiều cao đỉnh phổ tại $s=5$ khi $\\alpha=0.01$ là bao nhiêu?||For $e^{-\\alpha x^2}\\cos(10\\pi x)$, what is the spectral peak height at $s=5$ when $\\alpha=0.01$?⟧",
             opts=["{{peak_a001}}", "2.8025", "0.8862", "28.025"],
             explain="⟦$\\tfrac12\\sqrt{\\pi/\\alpha}$ = {{peak_a001}}; đo bằng quy tắc hình thang và bằng FFT đều trùng.||$\\tfrac12\\sqrt{\\pi/\\alpha}$ = {{peak_a001}}; the trapezoid rule and the FFT both agree.⟧"),
        dict(q="⟦Diện tích của mỗi đỉnh phổ trong dãy Gauss điều chế đó là bao nhiêu (mọi $\\alpha$)?||What is the area of each spectral peak in that modulated-Gaussian sequence (for every $\\alpha$)?⟧",
             opts=["{{area_peak}}", "1", "0.25", "2"],
             explain="⟦$f(0)=1$ chia đều cho hai đỉnh $\\pm5$ nên mỗi đỉnh có diện tích {{area_peak}}: đây là cặp xung $\\tfrac12\\delta(s\\mp5)$ khi $\\alpha\\to0$.||$f(0)=1$ splits evenly between the two peaks $\\pm5$ so each has area {{area_peak}}: the impulse pair $\\tfrac12\\delta(s\\mp5)$ as $\\alpha\\to0$.⟧"),
        dict(q="⟦Phần ảo của biến đổi $\\text{sgn}\\,x\\,e^{-\\alpha|x|}$ tại $s=0.5$ khi $\\alpha\\to0$ tiến về giá trị nào?||The imaginary part of the transform of $\\text{sgn}\\,x\\,e^{-\\alpha|x|}$ at $s=0.5$ tends to which value as $\\alpha\\to0$?⟧",
             opts=["{{sgn_limit}}", "0.6366", "-1.2732", "-0.3183"],
             explain="⟦Giới hạn là $(i\\pi s)^{-1}=-i/(\\pi s)$, phần ảo {{sgn_limit}} tại $s=0.5$ (bài tập 3).||The limit is $(i\\pi s)^{-1}=-i/(\\pi s)$, imaginary part {{sgn_limit}} at $s=0.5$ (problem 3).⟧"),
        dict(q="⟦Phần chẵn của $e^{-x}H(x)$ tại $x=1$ bằng bao nhiêu?||What is the even part of $e^{-x}H(x)$ at $x=1$?⟧",
             opts=["{{ev1}}", "0.3679", "0.0920", "0.2707"],
             explain="⟦$\\tfrac12e^{-|x|}$ = {{ev1}}.||$\\tfrac12e^{-|x|}$ = {{ev1}}.⟧"),
        dict(q="⟦Phần lẻ của $e^{-x}H(x)$ tại $x=-1$ bằng bao nhiêu?||What is the odd part of $e^{-x}H(x)$ at $x=-1$?⟧",
             opts=["{{od_m1}}", "0.1839", "-0.3679", "0"],
             explain="⟦$\\tfrac12\\text{sgn}(x)e^{-|x|}$ tại $-1$ là {{od_m1}} (lẻ nên đổi dấu so với $x=1$).||$\\tfrac12\\text{sgn}(x)e^{-|x|}$ at $-1$ is {{od_m1}} (odd, so the sign flips relative to $x=1$).⟧"),
        dict(q="⟦Phần chẵn của $e^{x}$ tại $x=1$ bằng bao nhiêu?||What is the even part of $e^{x}$ at $x=1$?⟧",
             opts=["{{cosh1}}", "1.1752", "2.7183", "1.3591"],
             explain="⟦Phần chẵn của $e^x$ là $\\cosh x$ = {{cosh1}}; phần lẻ $\\sinh x$ = {{sinh1}}.||The even part of $e^x$ is $\\cosh x$ = {{cosh1}}; the odd part $\\sinh x$ = {{sinh1}}.⟧"),
        dict(q="⟦Với $f=e^{-(x-a)^2}$, tổng năng lượng phần chẵn và phần lẻ (không phụ thuộc $a$) là bao nhiêu?||For $f=e^{-(x-a)^2}$, what is the total energy of the even and odd parts (independent of $a$)?⟧",
             opts=["{{energy_const}}", "1.7725", "0.8862", "0.6267"],
             explain="⟦Bằng $\\int f^2dx=\\sqrt{\\pi/2}$ = {{energy_const}} (bài tập 17).||Equal to $\\int f^2dx=\\sqrt{\\pi/2}$ = {{energy_const}} (problem 17).⟧"),
        dict(q="⟦Tín hiệu thực 1000 mẫu cần bao nhiêu hệ số FFT độc lập (nhờ đối xứng Hermitian)?||A real 1000-sample signal needs how many independent FFT coefficients (thanks to Hermitian symmetry)?⟧",
             opts=["{{herm_half}}", "500", "1000", "250"],
             explain="⟦$N/2+1$ = {{herm_half}} hệ số từ <code>rfft</code>; các hệ số còn lại là liên hợp của chúng.||$N/2+1$ = {{herm_half}} coefficients from <code>rfft</code>; the rest are their conjugates.⟧"),
        dict(q="⟦Biến đổi cosin của $e^{-x}$ tại $s=0.2$ ($F_c=2\\int_0^\\infty\\ldots$) bằng bao nhiêu?||What is the cosine transform of $e^{-x}$ at $s=0.2$ ($F_c=2\\int_0^\\infty\\ldots$)?⟧",
             opts=["{{fc_02}}", "0.9745", "0.3877", "0.6366"],
             explain="⟦$F_c=2/(1+4\\pi^2s^2)$ = {{fc_02}}.||$F_c=2/(1+4\\pi^2s^2)$ = {{fc_02}}.⟧"),
        dict(q="⟦Biến đổi sin của $e^{-x}$ tại $s=0.2$ bằng bao nhiêu?||What is the sine transform of $e^{-x}$ at $s=0.2$?⟧",
             opts=["{{fs_02}}", "0.7755", "0.4872", "0.3877"],
             explain="⟦$F_s=2\\cdot2\\pi s/(1+4\\pi^2s^2)$ = {{fs_02}}.||$F_s=2\\cdot2\\pi s/(1+4\\pi^2s^2)$ = {{fs_02}}.⟧"),
        dict(q="⟦Phần ảo của biến đổi Fourier $F(0.2)$ của $e^{-x}H(x)$ bằng bao nhiêu?||What is the imaginary part of the Fourier transform $F(0.2)$ of $e^{-x}H(x)$?⟧",
             opts=["{{f_im_02}}", "0.4872", "-0.9745", "-0.7755"],
             explain="⟦$F=\\tfrac12F_c-\\tfrac12iF_s$ nên phần ảo là $-\\tfrac12F_s$ = {{f_im_02}}.||$F=\\tfrac12F_c-\\tfrac12iF_s$ so the imaginary part is $-\\tfrac12F_s$ = {{f_im_02}}.⟧"),
        dict(q="⟦Với $f=e^{-\\pi x^2}$, diện tích $\\int f\\cos2\\pi sx\\,dx$ tại $s=0.25$ bằng bao nhiêu?||For $f=e^{-\\pi x^2}$, what is the area $\\int f\\cos2\\pi sx\\,dx$ at $s=0.25$?⟧",
             opts=["{{area_low}}", "0.4559", "0.9394", "0.6065"],
             explain="⟦Diện tích chính là $F(0.25)=e^{-\\pi/16}$ = {{area_low}}.||The area is just $F(0.25)=e^{-\\pi/16}$ = {{area_low}}.⟧"),
        dict(q="⟦Cũng với $f$ đó, diện tích tại $s=2$ (dao động nhanh) gần bằng bao nhiêu?||For the same $f$, what is the area at $s=2$ (fast oscillation), approximately?⟧",
             opts=["{{area_high}}", "1.83e-02", "3.49e-03", "3.49e-09"],
             explain="⟦$e^{-4\\pi}$ = {{area_high}}: các nửa chu kỳ dương và âm gần như triệt tiêu.||$e^{-4\\pi}$ = {{area_high}}: the positive and negative half-cycles almost cancel.⟧"),
        dict(q="⟦Vector giới hạn của xoắn ốc $\\int_0^Xe^{-x}e^{-i2\\pi sx}dx$ có độ dài bao nhiêu khi $s=0.5$?||What is the length of the limiting vector of the spiral $\\int_0^Xe^{-x}e^{-i2\\pi sx}dx$ when $s=0.5$?⟧",
             opts=["{{spiral_abs_05}}", "0.8467", "0.6366", "0.1592"],
             explain="⟦$|1/(1+i\\pi)|$ = {{spiral_abs_05}}, nhỏ hơn {{spiral_abs_01}} của $s=0.1$: $s$ lớn cuộn nhanh hơn.||$|1/(1+i\\pi)|$ = {{spiral_abs_05}}, smaller than {{spiral_abs_01}} for $s=0.1$: larger $s$ coils faster.⟧"),
        dict(q="⟦Biến đổi Fourier hai lần liên tiếp (cùng công thức) của $f(x)$ tổng quát cho kết quả nào?||Applying the Fourier transform twice (same formula) to a general $f(x)$ gives what?⟧",
             opts=["$f(-x)$", "⟦$f(x)$ với mọi $f$, vì biến đổi là nghịch đảo của chính nó khi hằng số $2\\pi$ nằm trong số mũ||$f(x)$ for every $f$, since the transform is its own inverse when the $2\\pi$ sits in the exponent⟧",
                   "⟦$F(s)$ lần nữa, vì lần biến đổi thứ hai chỉ đổi tên biến $x$ thành $s$||$F(s)$ again, since the second transform merely renames the variable $x$ to $s$⟧",
                   "⟦$-f(x)$, vì dấu của số mũ đảo lần thứ hai và kéo theo đổi dấu cả hàm||$-f(x)$, since the exponent sign flips the second time and drags the sign of the function along⟧"],
             explain="⟦Bracewell, tr. 5 đến 6: kết quả là $f(-x)$; chỉ với hàm chẵn mới trả lại $f(x)$.||Bracewell, pp. 5 to 6: the result is $f(-x)$; only for even functions is it $f(x)$.⟧"),
        dict(q="⟦Đâu là các điều kiện đủ cho biến đổi ngược trả lại $f(x)$ (Bracewell, tr. 9)?||Which are the sufficient conditions for the inverse transform to return $f(x)$ (Bracewell, p. 9)?⟧",
             opts=["⟦$\\int|f|dx$ tồn tại và mọi gián đoạn hữu hạn||$\\int|f|dx$ exists and all discontinuities are finite⟧",
                   "⟦$f$ tuần hoàn, bị chặn và có đạo hàm liên tục ở mọi điểm của một chu kỳ||$f$ periodic, bounded and with a continuous derivative at every point of a period⟧",
                   "⟦$f$ chẵn và có năng lượng vô hạn tập trung hoàn toàn tại tần số 0||$f$ even and with infinite energy concentrated entirely at zero frequency⟧",
                   "⟦$f$ thực và biến đổi của nó cũng phải thực, không có phần ảo ở bất kỳ tần số nào||$f$ real and its transform also real, with no imaginary part at any frequency⟧"],
             explain="⟦Tích phân của $|f|$ tồn tại và các gián đoạn hữu hạn (tr. 9). Tuần hoàn hay năng lượng vô hạn vi phạm điều kiện đó.||The integral of $|f|$ exists and the discontinuities are finite (p. 9). Periodicity or infinite energy violates them.⟧"),
        dict(q="⟦Cách nào của Bracewell để thu nạp hàm tuần hoàn vào lý thuyết biến đổi?||What is Bracewell's way of admitting periodic functions into transform theory?⟧",
             opts=["⟦Nhân với $e^{-\\alpha x^2}$ rồi cho $\\alpha\\to0$ để được cặp biến đổi trong giới hạn||Multiply by $e^{-\\alpha x^2}$ and let $\\alpha\\to0$ to get a transform pair in the limit⟧",
                   "⟦Chỉ lấy một chu kỳ rồi coi hàm bằng 0 ngoài chu kỳ đó trong mọi tính toán về sau||Keep a single period and take the function to be zero outside it in all later calculations⟧",
                   "⟦Đổi biến $x\\to1/x$ để đưa vô hạn về hữu hạn rồi áp dụng định lý tích phân Fourier||Substitute $x\\to1/x$ to bring infinity to a finite point and then apply Fourier's integral theorem⟧",
                   "⟦Loại các hàm tuần hoàn khỏi lý thuyết vì vật lý không có hàm tuần hoàn nào tồn tại thật sự trong tự nhiên||Exclude periodic functions from the theory because physics contains no periodic function that truly exists in nature⟧"],
             explain="⟦Bracewell, tr. 10: dãy biến đổi của các hàm đã nhân định nghĩa một hàm suy rộng, và hai thành viên tạo thành cặp trong giới hạn.||Bracewell, p. 10: the sequence of transforms of the modified functions defines a generalized function and the two members form a pair in the limit.⟧"),
        dict(q="⟦Hàm thực và lẻ có biến đổi Fourier thuộc loại nào?||Which kind of Fourier transform does a real odd function have?⟧",
             opts=["⟦Ảo và lẻ||Imaginary and odd⟧",
                   "⟦Thực và lẻ, vì biến đổi giữ nguyên cả tính thực lẫn tính lẻ của hàm gốc||Real and odd, since the transform keeps both the reality and the oddness of the original⟧",
                   "⟦Thực và chẵn, vì tích phân trên miền đối xứng chỉ còn lại phần chẵn của tích||Real and even, since integrating over a symmetric domain leaves only the even part of the product⟧",
                   "⟦Ảo và chẵn, vì phần ảo $-i\\sin$ đổi tính chẵn lẻ của hàm đem biến đổi||Imaginary and even, since the imaginary $-i\\sin$ flips the parity of the transformed function⟧"],
             explain="⟦$F=-2i\\int O\\sin$: thuần ảo và lẻ (bảng tr. 13 và bài tập 13).||$F=-2i\\int O\\sin$: purely imaginary and odd (table p. 13 and problem 13).⟧"),
        dict(q="⟦Hàm Hermitian được định nghĩa và có biến đổi thế nào?||How is a Hermitian function defined and what is its transform?⟧",
             opts=["⟦$f(x)=f^*(-x)$; biến đổi thực||$f(x)=f^*(-x)$; the transform is real⟧",
                   "⟦$f(x)=-f^*(-x)$, phần thực lẻ và phần ảo chẵn; biến đổi hoàn toàn ảo||$f(x)=-f^*(-x)$, real part odd and imaginary part even; the transform is purely imaginary⟧",
                   "⟦$f(x)=f^*(x)$, tức hàm thực bất kỳ; biến đổi luôn thực và chẵn||$f(x)=f^*(x)$, i.e. any real function; the transform is always real and even⟧",
                   "⟦$f(x)=f(-x)$, phần thực chẵn; biến đổi có phần ảo bằng phần thực||$f(x)=f(-x)$, real part even; the transform has an imaginary part equal to its real part⟧"],
             explain="⟦Bracewell, tr. 14: Hermitian là phần thực chẵn và phần ảo lẻ, $f=f^*(-x)$, và biến đổi thực.||Bracewell, p. 14: Hermitian means real part even and imaginary part odd, $f=f^*(-x)$, and the transform is real.⟧"),
        dict(q="⟦Biến đổi Fourier của $f^*(x)$ là gì?||What is the Fourier transform of $f^*(x)$?⟧",
             opts=["$F^*(-s)$", "$F^*(s)$", "⟦$F(-s)$, vì liên hợp phức chỉ đổi dấu phần ảo của tín hiệu chứ không đổi của phổ||$F(-s)$, since conjugation only changes the sign of the signal's imaginary part, not the spectrum's⟧",
                   "⟦$-F(s)$, vì liên hợp đổi dấu mũ và do đó đổi dấu toàn bộ tích phân||$-F(s)$, since conjugation flips the exponent sign and hence the sign of the whole integral⟧"],
             explain="⟦Bracewell, tr. 14: biến đổi của $f^*(x)$ là $F^*(-s)$.||Bracewell, p. 14: the transform of $f^*(x)$ is $F^*(-s)$.⟧"),
        dict(q="⟦Biến đổi cosin đặc biệt ở điểm nào?||What is special about the cosine transform?⟧",
             opts=["⟦Tự nghịch đảo||It is its own inverse⟧",
                   "⟦Cho kết quả luôn thực và dương với mọi hàm thực, nên dùng làm thước đo năng lượng||It always gives a real and positive result for any real function, so it serves as an energy measure⟧",
                   "⟦Chỉ áp dụng được cho hàm tuần hoàn vì cần biết hàm ở cả hai nửa trục||It applies only to periodic functions since it needs the function on both half-axes⟧",
                   "⟦Không cần hằng số $2\\pi$ trong đối số cosin nên đơn giản hơn biến đổi Fourier||It needs no $2\\pi$ in the cosine argument, so it is simpler than the Fourier transform⟧"],
             explain="⟦Bracewell, tr. 17: biến đổi cosin thuận và ngược có cùng công thức.||Bracewell, p. 17: the forward and reverse cosine transformations are identical.⟧"),
        dict(q="⟦Hàm nhân quả ($f=0$ với $x<0$) có biến đổi Fourier liên hệ với $F_c$ và $F_s$ thế nào?||For a causal function ($f=0$ for $x<0$), how is the Fourier transform related to $F_c$ and $F_s$?⟧",
             opts=["$F=\\tfrac12F_c-\\tfrac12iF_s$",
                   "$F=F_c+iF_s$ ⟦vì mỗi biến đổi chỉ lấy một nửa và không cần chia đôi||because each transform takes only one half and needs no halving⟧",
                   "$F=\\tfrac12F_c+\\tfrac12iF_s$ ⟦vì dấu của $i$ luôn dương với hàm nhân quả||because the sign of $i$ is always positive for a causal function⟧",
                   "$F=F_c\\cdot F_s$ ⟦vì hai biến đổi kết hợp bằng phép nhân như tích chập||because the two transforms combine by multiplication like a convolution⟧"],
             explain="⟦Bracewell, tr. 17: $F(s)=\\tfrac12F_c(s)-\\tfrac12iF_s(s)$; với $e^{-x}$ tại 0.2 ta có {{f_re_02}} và phần ảo {{f_im_02}}.||Bracewell, p. 17: $F(s)=\\tfrac12F_c(s)-\\tfrac12iF_s(s)$; for $e^{-x}$ at 0.2 we get {{f_re_02}} with imaginary part {{f_im_02}}.⟧"),
        dict(q="⟦Vì sao $\\cos x$ có thể chuyển từ hoàn toàn chẵn sang hoàn toàn lẻ?||Why can $\\cos x$ change from fully even to fully odd?⟧",
             opts=["⟦Vì chẵn lẻ phụ thuộc vào gốc tọa độ và dịch gốc làm $\\cos x$ thành $\\sin x$||Because parity depends on the origin and shifting it turns $\\cos x$ into $\\sin x$⟧",
                   "⟦Vì $\\cos x$ có biến đổi Fourier là cặp xung nên tính chẵn lẻ đổi khi lấy biến đổi||Because $\\cos x$ has an impulse pair as its Fourier transform, so parity flips when transforming⟧",
                   "⟦Vì hàm tuần hoàn luôn có phần chẵn và phần lẻ bằng nhau về năng lượng ở mọi gốc||Because a periodic function always has equal even and odd energy at every origin⟧",
                   "⟦Vì $\\cos x$ không thỏa điều kiện tồn tại nên không có tính chẵn lẻ xác định||Because $\\cos x$ fails the existence condition and so has no definite parity⟧"],
             explain="⟦Bracewell, tr. 12: dịch gốc làm phần chẵn nhỏ dần và phần lẻ lớn dần cho tới khi hàm hoàn toàn lẻ.||Bracewell, p. 12: shifting the origin makes the even part wane and the odd part grow until the function is fully odd.⟧"),
        dict(q="⟦Nếu $f(x)$ và $F(s)$ là một cặp ở hệ 1, thì cặp nào là cặp ở hệ 2?||If $f(x)$ and $F(s)$ are a pair in system 1, which is a pair in system 2?⟧",
             opts=["$f(x)$ ⟦và||and⟧ $F(s/2\\pi)$",
                   "$f(x)$ ⟦và||and⟧ $F(2\\pi s)$ ⟦vì hằng số phải nhân lên khi chuyển sang tần số góc||since the constant must be multiplied up when moving to angular frequency⟧",
                   "$f(2\\pi x)$ ⟦và||and⟧ $F(s)$ ⟦vì biến gốc mới là biến đổi tỉ lệ||since the original variable is the one rescaled⟧",
                   "$f(x)/2\\pi$ ⟦và||and⟧ $F(s)$ ⟦vì chỉ cần chuẩn hóa biên độ của hàm gốc||since only the amplitude of the original function needs normalising⟧"],
             explain="⟦Bracewell, tr. 6: cặp hệ 1 $f(x)$, $F(s)$ thành cặp hệ 2 $f(x)$, $F(s/2\\pi)$.||Bracewell, p. 6: the system-1 pair $f(x)$, $F(s)$ becomes the system-2 pair $f(x)$, $F(s/2\\pi)$.⟧"),
        dict(q="⟦Khi $s$ tăng, xoắn ốc biểu diễn $F(s)$ trên mặt phẳng phức thay đổi thế nào?||When $s$ increases, how does the spiral representing $F(s)$ on the complex plane change?⟧",
             opts=["⟦Cuộn nhanh hơn và vector $AB$ ngắn đi||It coils faster and the vector $AB$ gets shorter⟧",
                   "⟦Cuộn chậm hơn và vector $AB$ dài ra, vì góc quay $2\\pi sx$ tăng chậm khi $s$ lớn||It coils more slowly and the vector $AB$ grows, since the angle $2\\pi sx$ advances more slowly for large $s$⟧",
                   "⟦Giữ nguyên hình dạng nhưng quay đi một góc bằng $2\\pi s$ quanh gốc tọa độ||It keeps its shape but rotates by an angle $2\\pi s$ about the origin⟧",
                   "⟦Biến thành đường thẳng vì thành phần ảo triệt tiêu ở tần số cao||It collapses to a straight line because the imaginary part vanishes at high frequency⟧"],
             explain="⟦Bracewell, tr. 20 (hình 2.10): $s$ lớn cuộn nhanh hơn; số đo: {{spiral_abs_01}} khi $s=0.1$ so với {{spiral_abs_05}} khi $s=0.5$.||Bracewell, p. 20 (Fig. 2.10): larger $s$ coils faster; measured: {{spiral_abs_01}} for $s=0.1$ versus {{spiral_abs_05}} for $s=0.5$.⟧"),
        dict(q="⟦Hàm có năng lượng vô hạn như dòng điện một chiều vi phạm điều kiện nào?||A function with infinite energy such as a direct current violates which condition?⟧",
             opts=["⟦Điều kiện thứ nhất (khả tích tuyệt đối), và phổ dồn vô hạn vào tần số 0||The first condition (absolute integrability), with the spectrum piling up infinitely at zero frequency⟧",
                   "⟦Chỉ điều kiện thứ hai (gián đoạn hữu hạn), vì dòng một chiều không đổi có gián đoạn vô hạn tại điểm bật||Only the second condition (finite discontinuities), because a constant current has an infinite jump at switch-on⟧",
                   "⟦Không điều kiện nào, vì dòng một chiều là tín hiệu thực và mọi tín hiệu thực đều có biến đổi thường||Neither, because a direct current is a real signal and every real signal has an ordinary transform⟧",
                   "⟦Điều kiện biến phân bị chặn, vì dòng một chiều dao động vô hạn lần trong một đoạn||The bounded-variation condition, because a direct current oscillates infinitely often in an interval⟧"],
             explain="⟦Bracewell, tr. 9: dòng một chiều luôn chảy vi phạm điều kiện thứ nhất, và phân bố năng lượng dồn vào tần số 0 vi phạm điều kiện thứ hai.||Bracewell, p. 9: direct current that always flows violates the first condition, and the energy concentrated at zero frequency violates the second.⟧"),
        dict(q="⟦Trong ba hàm $\\sin t$, $H(t)$ và $\\delta(t)$, hàm nào có biến đổi Fourier thường?||Among $\\sin t$, $H(t)$ and $\\delta(t)$, which has an ordinary Fourier transform?⟧",
             opts=["⟦Không hàm nào||None of them⟧",
                   "⟦Cả ba, vì cả ba đều bị chặn bởi một hằng số nên tích phân Fourier hội tụ||All three, because each is bounded by a constant so the Fourier integral converges⟧",
                   "⟦Chỉ $H(t)$ và $\\delta(t)$, vì $\\sin t$ tuần hoàn nên không có phổ vạch xác định||Only $H(t)$ and $\\delta(t)$, since $\\sin t$ is periodic and has no well-defined line spectrum⟧",
                   "⟦Chỉ $\\sin t$, vì nó là sóng điều hòa và mọi sóng điều hòa đều có phổ một vạch||Only $\\sin t$, since it is a harmonic wave and every harmonic wave has a single-line spectrum⟧"],
             explain="⟦Bracewell, tr. 8: tích phân Fourier không hội tụ với mọi $s$ đối với cả ba; ta dùng biến đổi trong giới hạn.||Bracewell, p. 8: the Fourier integral does not converge for all $s$ for any of the three; we use transforms in the limit.⟧"),
        dict(q="⟦Theo Bracewell, quan hệ nào của biến đổi Fourier phản ánh việc phân tích và tổng hợp là cùng một phép làm?||According to Bracewell, which property of the Fourier transform reflects that analysing and synthesising do the same thing?⟧",
             opts=["⟦Tính tương hỗ||Reciprocity⟧",
                   "⟦Tính tuyến tính của phép biến đổi, vì tổng hợp là cộng còn phân tích là tách ra||Linearity of the transform, since synthesis is adding and analysis is splitting up⟧",
                   "⟦Tính bảo toàn năng lượng, vì phân tích và tổng hợp không làm mất năng lượng||Energy conservation, since analysis and synthesis lose no energy⟧",
                   "⟦Tính dịch chuyển, vì phân tích dịch hàm sang tần số còn tổng hợp dịch ngược lại||The shift property, since analysis shifts the function to frequency and synthesis shifts it back⟧"],
             explain="⟦Bracewell, tr. 19 đến 20: việc phân tích hay tổng hợp đều làm cùng một việc phản ánh tính tương hỗ của biến đổi Fourier.||Bracewell, pp. 19 to 20: that whether you analyze or synthesize you do the same thing reflects the reciprocal property of the Fourier transform.⟧"),
    ],
    nb=[
        ("md", """## 1. ⟦Cặp biến đổi và định lý tích phân Fourier||The transform pair and Fourier's integral theorem⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Các biến đổi quen thuộc (Gauss, sech, $\\Pi$, $\\Lambda$, hàm nhân quả) có đúng như công thức đóng không, hai lần biến đổi có trả về $f(-x)$ không, và biến đổi ngược thu lại gì ở chỗ gián đoạn? Ta so tích phân số với công thức, và DFT với ma trận DFT dựng tay.||Do the familiar transforms (Gaussian, sech, $\\Pi$, $\\Lambda$, a causal function) match their closed forms, do two transforms return $f(-x)$, and what does the inverse transform recover at a discontinuity? We compare numerical integration with formulas, and the DFT with a hand-built DFT matrix.⟧"""),
        ("code", r'''from scipy import integrate, special
from scipy.signal import lfilter
trap = getattr(np, "trapezoid", None) or np.trapz

def ft_support(f, a, b, s, pts=None):
    """⟦Biến đổi Fourier (hệ 1) của f trên [a, b] bằng tích phân số||Fourier transform (system 1) of f on [a, b] by numerical integration⟧"""
    re = integrate.quad(lambda x: f(x)*np.cos(2*np.pi*x*s), a, b, points=pts, limit=400)[0]
    im = integrate.quad(lambda x: -f(x)*np.sin(2*np.pi*x*s), a, b, points=pts, limit=400)[0]
    return re + 1j*im

gauss = lambda x: np.exp(-np.pi*x**2)
sech = lambda x: 1/np.cosh(np.pi*x)
for s in (0.0, 0.5, 1.0):
    assert abs(ft_support(gauss, -40, 40, s) - np.exp(-np.pi*s**2)) < 1e-8
    assert abs(ft_support(sech, -40, 40, s) - 1/np.cosh(np.pi*s)) < 1e-8
report("gauss_05", ft_support(gauss, -40, 40, 0.5).real, ".4f")
report("sech_05", ft_support(sech, -40, 40, 0.5).real, ".4f")

pi05 = ft_support(lambda x: 1.0, -0.5, 0.5, 0.5); pi2 = ft_support(lambda x: 1.0, -0.5, 0.5, 2.0)
assert abs(pi05 - np.sinc(0.5)) < 1e-9 and abs(pi2) < 1e-9
report("pi_05", pi05.real, ".4f"); report("pi_2", abs(pi2), ".4f")
tri05 = ft_support(lambda x: 1 - abs(x), -1, 1, 0.5, [0])
assert abs(tri05 - np.sinc(0.5)**2) < 1e-9
report("tri_05", tri05.real, ".4f")
ea = ft_support(lambda x: np.exp(-abs(x)), -40, 40, 0.25, [0]).real
assert abs(ea - 2/(1 + 4*np.pi**2*0.25**2)) < 1e-8
report("expabs_025", ea, ".4f")
Fc1 = ft_support(lambda x: np.exp(-x), 0, 40, 0.1)               # ⟦hàm nhân quả e^{-x}H(x)||causal function e^{-x}H(x)⟧
assert abs(Fc1 - 1/(1 + 2j*np.pi*0.1)) < 1e-8
report("causal_mag_01", abs(Fc1), ".4f"); report("causal_ph_01", np.degrees(np.angle(Fc1)), ".2f")

# ⟦Tính tuần hoàn: F F f = f(−x). Cách A: FFT; cách B: ma trận DFT dựng tay||Cyclic property: F F f = f(−x). Method A: FFT; method B: hand-built DFT matrix⟧
N = 64; nn = np.arange(N)
v = np.sin(nn**1.5) + 0.2*nn/N                                   # ⟦dãy không chẵn không lẻ||neither even nor odd⟧
W = np.exp(-2j*np.pi*np.outer(nn, nn)/N)
rev = v[(-nn) % N]
ffA = np.fft.fft(np.fft.fft(v))/N; ffB = (W @ (W @ v))/N
assert np.allclose(ffA, rev) and np.allclose(ffB, rev)
f4 = np.fft.fft(np.fft.fft(np.fft.fft(np.fft.fft(v))))/N**2
assert np.allclose(f4, v)
report("cyc_err", max(np.max(np.abs(ffA - rev)), np.max(np.abs(ffB - rev))), ".1e"); report("cyc4_err", np.max(np.abs(f4 - v)), ".1e")

# ⟦Định lý tích phân Fourier tại điểm nhảy của Π: cắt biến đổi ngược ở |s| ≤ S||Fourier's integral theorem at the jump of Π: truncate the inverse at |s| ≤ S⟧
def inv_num(x, S):      # ⟦cách A: tích phân số dao động||method A: oscillatory numerical integral⟧
    return 2*integrate.quad(np.sinc, 0, S, weight="cos", wvar=2*np.pi*x, limit=2000)[0]
def inv_si(x, S):       # ⟦cách B: công thức đóng qua hàm Si||method B: closed form through the Si function⟧
    return (special.sici(np.pi*S*(1 + 2*x))[0] + special.sici(np.pi*S*(1 - 2*x))[0])/np.pi
for S in (5, 20, 100):
    assert abs(inv_num(0.5, S) - inv_si(0.5, S)) < 1e-6
    report(f"thm_s{S}", inv_si(0.5, S), ".4f")
assert abs(inv_num(0.25, 100) - inv_si(0.25, 100)) < 1e-6 and abs(inv_num(1.0, 100) - inv_si(1.0, 100)) < 1e-6
report("thm_in", inv_si(0.25, 100), ".4f"); report("thm_out", inv_si(1.0, 100), ".4f")'''),
        ("code", r'''xx = np.linspace(-1, 1, 1001)
plt.figure(figsize=(7, 3.3))
plt.plot(xx, np.where(np.abs(xx) < 0.5 - 1e-12, 1.0, np.where(np.abs(np.abs(xx) - 0.5) <= 1e-12, 0.5, 0.0)), "k--", label="Π(x)")
for S, c in ((5, "tab:orange"), (20, "tab:blue")):
    plt.plot(xx, inv_si(xx, S), color=c, label=f"S = {S}")
plt.axhline(0.5, color="gray", lw=0.6); plt.xlabel("x"); plt.legend()
plt.tight_layout(); plt.show()''', dict(fig="theorem", cap="⟦Hình 1. Biến đổi ngược của sinc cắt ở |s| ≤ S tiến về Π(x); tại chỗ nhảy x = ±0.5 mọi đường đều đi qua giá trị 0.5, trung bình của 1 và 0.||Figure 1. The inverse transform of sinc truncated at |s| ≤ S tends to Π(x); at the jump x = ±0.5 every curve passes through 0.5, the mean of 1 and 0.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Tích phân số trùng công thức đóng: Gauss cho {{gauss_05}} và sech cho {{sech_05}} tại $s=0.5$, $\\Pi$ cho {{pi_05}} và {{pi_2}} tại $s=0.5$ và $s=2$, $\\Lambda$ cho {{tri_05}}. Hàm nhân quả $e^{-x}H(x)$ tại $s=0.1$ có độ lớn {{causal_mag_01}} và pha {{causal_ph_01}} độ. Hai lần DFT trả về dãy đảo (lệch {{cyc_err}}) bằng cả FFT lẫn ma trận tự dựng, và bốn lần trả về đúng dãy gốc (lệch {{cyc4_err}}). Tại chỗ nhảy, biến đổi ngược cắt ở $S=5,20,100$ cho {{thm_s5}}, {{thm_s20}}, {{thm_s100}}, tiến về 0.5; bên trong xung được {{thm_in}}, bên ngoài được {{thm_out}}.||Numerical integration matches the closed forms: the Gaussian gives {{gauss_05}} and sech gives {{sech_05}} at $s=0.5$, $\\Pi$ gives {{pi_05}} and {{pi_2}} at $s=0.5$ and $s=2$, $\\Lambda$ gives {{tri_05}}. The causal function $e^{-x}H(x)$ at $s=0.1$ has magnitude {{causal_mag_01}} and phase {{causal_ph_01}} degrees. Two DFTs return the reversed sequence (deviation {{cyc_err}}) with both the FFT and the hand-built matrix, and four return the original (deviation {{cyc4_err}}). At the jump, the inverse truncated at $S=5,20,100$ gives {{thm_s5}}, {{thm_s20}}, {{thm_s100}}, approaching 0.5; inside the pulse we get {{thm_in}}, outside {{thm_out}}.⟧"""),
        ("md", """## 2. ⟦Biến đổi trong giới hạn||Transforms in the limit⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Khi nhân một hàm tuần hoàn hoặc hàm dấu với thừa số tắt dần rồi cho hệ số về 0, dãy biến đổi tiến về đâu? Ta tính đỉnh, độ rộng và diện tích bằng hai cách (quy tắc hình thang và FFT), và so hàm dấu với công thức đóng.||When a periodic function or the sign function is multiplied by a decaying factor and the factor is sent to zero, where does the sequence of transforms go? We compute the peak, width and area two ways (trapezoid rule and FFT), and compare the sign function with its closed form.⟧"""),
        ("code", r'''dx = 0.002
xg = np.arange(-150, 150, dx)
assert abs(xg[len(xg)//2]) < 1e-9
sk_all = np.fft.fftshift(np.fft.fftfreq(len(xg), dx)); ds = sk_all[1] - sk_all[0]
Fdict = {}
for tag, al in (("a1", 1.0), ("a01", 0.1), ("a001", 0.01)):
    g = np.exp(-al*xg**2)*np.cos(2*np.pi*5*xg)
    F5_trap = trap(g*np.cos(2*np.pi*5*xg), xg)                                  # ⟦cách A: quy tắc hình thang||method A: trapezoid rule⟧
    F5_exact = 0.5*np.sqrt(np.pi/al)
    Fk = np.fft.fftshift(np.fft.fft(np.fft.ifftshift(g))).real*dx                 # ⟦cách B: FFT cả đoạn||method B: FFT of the whole record⟧
    i5 = np.argmin(np.abs(sk_all - 5))
    assert abs(F5_trap - F5_exact)/F5_exact < 1e-6 and abs(Fk[i5] - F5_exact)/F5_exact < 1e-6
    m = (sk_all > 3) & (sk_all < 7)
    area = Fk[m].sum()*ds
    width = np.sqrt(np.sum((sk_all[m] - 5)**2*Fk[m])/np.sum(Fk[m]))
    assert abs(area - 0.5) < 5e-3 and abs(width - np.sqrt(al)/(np.pi*np.sqrt(2)))/width < 0.02
    report(f"peak_{tag}", F5_trap, ".4f"); report(f"width_{tag}", width, ".4f")
    m2 = (sk_all > 3.5) & (sk_all < 6.5); Fdict[tag] = (sk_all[m2], Fk[m2])
report("area_peak", area, ".4f")

# ⟦Hàm dấu: sgn(x)·exp(−α|x|) tại s = 0.5||Sign function: sgn(x)·exp(−α|x|) at s = 0.5⟧
def sgn_ft(al, s):
    return -2j*integrate.quad(lambda x: np.exp(-al*x), 0, np.inf, weight="sin", wvar=2*np.pi*s)[0]
closed = lambda al, s: -1j*4*np.pi*s/(al**2 + 4*np.pi**2*s**2)
for al, tag in ((0.1, "a01"), (0.01, "a001"), (0.001, "a0001")):
    assert abs(sgn_ft(al, 0.5) - closed(al, 0.5)) < 1e-9
    report(f"sgn_{tag}", sgn_ft(al, 0.5).imag, ".4f")
report("sgn_limit", (-1j/(np.pi*0.5)).imag, ".4f")'''),
        ("code", r'''plt.figure(figsize=(7, 3.3))
for tag, al, c in (("a1", 1.0, "tab:green"), ("a01", 0.1, "tab:blue"), ("a001", 0.01, "tab:red")):
    plt.plot(Fdict[tag][0], Fdict[tag][1], color=c, label=f"α = {al}")
plt.xlabel("s"); plt.ylabel("F(s)"); plt.legend()
plt.tight_layout(); plt.show()''', dict(fig="limit_gauss", cap="⟦Hình 2. Biến đổi của e^{−αx²}cos(10πx) quanh s = 5: khi α giảm, đỉnh cao lên và hẹp lại nhưng diện tích giữ nguyên, tiến về một xung.||Figure 2. The transform of e^{−αx²}cos(10πx) near s = 5: as α decreases the peak grows taller and narrower with the area unchanged, tending to an impulse.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Chiều cao đỉnh {{peak_a1}}, {{peak_a01}}, {{peak_a001}} tăng như $\\tfrac12\\sqrt{\\pi/\\alpha}$, độ rộng co lại {{width_a1}}, {{width_a01}}, {{width_a001}}, còn diện tích luôn {{area_peak}}: dãy không hội tụ từng điểm nhưng định nghĩa một hàm suy rộng (cặp xung). Với hàm dấu, phần ảo {{sgn_a01}}, {{sgn_a001}}, {{sgn_a0001}} tiến về {{sgn_limit}}, đúng $-1/(\\pi s)$ của bài tập 3.||The peak heights {{peak_a1}}, {{peak_a01}}, {{peak_a001}} grow like $\\tfrac12\\sqrt{\\pi/\\alpha}$, the widths shrink {{width_a1}}, {{width_a01}}, {{width_a001}}, and the area stays {{area_peak}}: the sequence has no pointwise limit but defines a generalized function (an impulse pair). For the sign function the imaginary parts {{sgn_a01}}, {{sgn_a001}}, {{sgn_a0001}} approach {{sgn_limit}}, exactly the $-1/(\\pi s)$ of problem 3.⟧"""),
        ("md", """## 3. ⟦Chẵn, lẻ và bảng đối xứng||Even, odd and the symmetry table⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Tách hàm thành phần chẵn và lẻ như thế nào, thành phần nào phụ thuộc gốc, và bảng đối xứng của Bracewell có đúng với DFT không? Ta kiểm bằng công thức giải tích, bằng tích phân số năng lượng, và bằng DFT của các dãy có đối xứng dựng sẵn.||How do we split a function into even and odd parts, which part depends on the origin, and does Bracewell's symmetry table hold for the DFT? We check with analytic formulas, numerical energy integrals, and the DFT of sequences built with each symmetry.⟧"""),
        ("code", r'''xg2 = np.linspace(-6, 6, 12001)
H = np.where(xg2 > 1e-12, 1.0, np.where(np.abs(xg2) <= 1e-12, 0.5, 0.0))
f = np.exp(-xg2)*H
ev, od = 0.5*(f + f[::-1]), 0.5*(f - f[::-1])
assert np.allclose(ev, 0.5*np.exp(-np.abs(xg2))) and np.allclose(od, 0.5*np.sign(xg2)*np.exp(-np.abs(xg2)))
i1, im1 = np.argmin(np.abs(xg2 - 1)), np.argmin(np.abs(xg2 + 1))
report("ev1", ev[i1], ".4f"); report("od1", od[i1], ".4f"); report("od_m1", od[im1], ".4f")
fe = np.exp(xg2)
assert np.allclose(0.5*(fe + fe[::-1]), np.cosh(xg2)) and np.allclose(0.5*(fe - fe[::-1]), np.sinh(xg2))
report("cosh1", np.cosh(1.0), ".4f"); report("sinh1", np.sinh(1.0), ".4f")

# ⟦Bài tập 17: tổng năng lượng chẵn và lẻ không phụ thuộc gốc||Problem 17: the even plus odd energy is independent of the origin⟧
xg3 = np.linspace(-15, 15, 300001)
for a_, tag in ((0, "a0"), (0.5, "a05"), (1, "a1"), (2, "a2")):
    g_, gm_ = np.exp(-(xg3 - a_)**2), np.exp(-(-xg3 - a_)**2)
    ee, oo = trap((0.5*(g_ + gm_))**2, xg3), trap((0.5*(g_ - gm_))**2, xg3)
    assert abs(ee + oo - np.sqrt(np.pi/2)) < 1e-6
    report(f"ev_share_{tag}", ee/(ee + oo), ".4f")
report("energy_const", np.sqrt(np.pi/2), ".4f")

# ⟦Bảng đối xứng bằng DFT (sáu dòng)||The symmetry table with the DFT (six rows)⟧
Nq = 128; nq = np.arange(Nq); rv = (-nq) % Nq
rng = np.random.default_rng(7); a_r, b_r = rng.standard_normal(Nq), rng.standard_normal(Nq)
ev_ = lambda z: 0.5*(z + z[rv]); od_ = lambda z: 0.5*(z - z[rv])
isre = lambda z: np.max(np.abs(z.imag)) < 1e-10; isim = lambda z: np.max(np.abs(z.real)) < 1e-10
isev = lambda z: np.allclose(z, z[rv]); isod = lambda z: np.allclose(z, -z[rv])
cases = [(ev_(a_r), lambda F_: isre(F_) and isev(F_)), (od_(a_r), lambda F_: isim(F_) and isod(F_)),
         (1j*ev_(b_r), lambda F_: isim(F_) and isev(F_)), (1j*od_(b_r), lambda F_: isre(F_) and isod(F_)),
         (ev_(a_r) + 1j*od_(b_r), isre), (od_(a_r) + 1j*ev_(b_r), isim)]
Wq = np.exp(-2j*np.pi*np.outer(nq, nq)/Nq)
assert np.allclose(Wq @ cases[4][0], np.fft.fft(cases[4][0]))     # ⟦đối chiếu với ma trận DFT||cross-check against the DFT matrix⟧
ok = sum(bool(chk(np.fft.fft(v_))) for v_, chk in cases)
assert ok == len(cases)
report("sym_ok", ok, "d"); report("sym_total", len(cases), "d")

# ⟦Tín hiệu thực: chỉ cần nửa phổ||A real signal: half the spectrum suffices⟧
nr = np.arange(1000)
xr = np.cos(2*np.pi*13*nr/1000) + 0.5*np.sin(2*np.pi*77*nr/1000 + 0.4)
Xr = np.fft.fft(xr)
assert np.allclose(Xr[1:], np.conj(Xr[:0:-1]))
e_time = np.sum(xr**2)
e_half = (abs(Xr[0])**2 + 2*np.sum(abs(Xr[1:500])**2) + abs(Xr[500])**2)/1000
assert abs(e_time - e_half) < 1e-9
report("herm_full", len(Xr), "d"); report("herm_half", len(np.fft.rfft(xr)), "d"); report("herm_energy", e_time, ".4f")'''),
        ("code", r'''xp = np.linspace(-4, 4, 4001)
Hp = np.where(xp > 1e-12, 1.0, np.where(np.abs(xp) <= 1e-12, 0.5, 0.0)); fp = np.exp(-xp)*Hp
plt.figure(figsize=(7, 3.3))
plt.plot(xp, fp, "k", label="f(x) = e^{-x}H(x)")
plt.plot(xp, 0.5*(fp + fp[::-1]), "tab:blue", label=("⟦phần chẵn||even part⟧"))
plt.plot(xp, 0.5*(fp - fp[::-1]), "tab:red", label=("⟦phần lẻ||odd part⟧"))
plt.axhline(0, color="gray", lw=0.6); plt.xlabel("x"); plt.legend()
plt.tight_layout(); plt.show()''', dict(fig="symmetry", cap="⟦Hình 3. Hàm nhân quả e^{−x}H(x) (đen) tách duy nhất thành phần chẵn (xanh) và phần lẻ (đỏ); cộng lại cho ra hàm ban đầu.||Figure 3. The causal function e^{−x}H(x) (black) splits uniquely into an even part (blue) and an odd part (red); adding them returns the original.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Với $e^{-x}H(x)$, phần chẵn và phần lẻ tại $x=1$ là {{ev1}} và {{od1}}, tại $x=-1$ phần lẻ đổi dấu thành {{od_m1}}. Với $e^x$ ta được $\\cosh 1$ = {{cosh1}} và $\\sinh 1$ = {{sinh1}}. Tổng năng lượng chẵn và lẻ của $e^{-(x-a)^2}$ luôn là {{energy_const}} dù dịch gốc, trong khi phần chẵn chiếm {{ev_share_a0}}, {{ev_share_a05}}, {{ev_share_a1}}, {{ev_share_a2}} khi $a=0,0.5,1,2$. DFT thỏa {{sym_ok}} trên {{sym_total}} dòng bảng đối xứng. Tín hiệu thực có {{herm_full}} hệ số nhưng chỉ {{herm_half}} độc lập, và năng lượng {{herm_energy}} phục hồi đủ từ nửa phổ.||For $e^{-x}H(x)$ the even and odd parts at $x=1$ are {{ev1}} and {{od1}}, and at $x=-1$ the odd part flips to {{od_m1}}. For $e^x$ we get $\\cosh 1$ = {{cosh1}} and $\\sinh 1$ = {{sinh1}}. The even plus odd energy of $e^{-(x-a)^2}$ is always {{energy_const}} whatever the shift, while the even share is {{ev_share_a0}}, {{ev_share_a05}}, {{ev_share_a1}}, {{ev_share_a2}} for $a=0,0.5,1,2$. The DFT satisfies {{sym_ok}} of {{sym_total}} symmetry rows. A real signal has {{herm_full}} coefficients but only {{herm_half}} independent ones, and the energy {{herm_energy}} is fully recovered from half the spectrum.⟧"""),
        ("md", """## 4. ⟦Liên hợp phức, biến đổi cosin và sin||Complex conjugates, cosine and sine transforms⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Bảng tám dòng về liên hợp phức có đúng không, và với hàm nhân quả $e^{-x}H(x)$, biến đổi Fourier có đúng bằng $\\tfrac12F_c-\\tfrac12iF_s$ không? Ta kiểm bảng bằng DFT và các biến đổi cosin và sin bằng tích phân số so với công thức đóng.||Is the eight-line table on complex conjugates correct, and for the causal $e^{-x}H(x)$ does the Fourier transform equal $\\tfrac12F_c-\\tfrac12iF_s$? We check the table with the DFT and the cosine and sine transforms by numerical integration against closed forms.⟧"""),
        ("code", r'''fz = a_r + 1j*b_r
Fz = np.fft.fft(fz); cj = np.conj
rows = [(np.fft.fft(cj(fz)), cj(Fz)[rv]), (np.fft.fft(cj(fz)[rv]), cj(Fz)), (np.fft.fft(fz[rv]), Fz[rv]),
        (np.fft.fft(2*fz.real), Fz + cj(Fz)[rv]), (np.fft.fft(2j*fz.imag), Fz - cj(Fz)[rv]),
        (np.fft.fft(fz + cj(fz)[rv]), 2*Fz.real), (np.fft.fft(fz - cj(fz)[rv]), 2j*Fz.imag)]
conj_ok = sum(bool(np.allclose(l_, r_)) for l_, r_ in rows)
assert conj_ok == 7
report("conj_ok", conj_ok, "d")

s0 = 0.2                                                          # ⟦biến đổi cosin và sin của e^{-x}||cosine and sine transforms of e^{-x}⟧
Fc = 2*integrate.quad(lambda x: np.exp(-x), 0, np.inf, weight="cos", wvar=2*np.pi*s0)[0]
Fs = 2*integrate.quad(lambda x: np.exp(-x), 0, np.inf, weight="sin", wvar=2*np.pi*s0)[0]
Fc_ex, Fs_ex = 2/(1 + 4*np.pi**2*s0**2), 2*(2*np.pi*s0)/(1 + 4*np.pi**2*s0**2)
assert abs(Fc - Fc_ex) < 1e-9 and abs(Fs - Fs_ex) < 1e-9
F_caus = 1/(1 + 2j*np.pi*s0)
assert abs(0.5*Fc - 0.5j*Fs - F_caus) < 1e-9                       # ⟦F = ½Fc − ½iFs||F = ½Fc − ½iFs⟧
F_even = ft_support(lambda x: np.exp(-abs(x)), -40, 40, s0, [0]).real
assert abs(F_even - Fc_ex) < 1e-8                                  # ⟦biến đổi Fourier của mở rộng chẵn = Fc||Fourier transform of the even extension = Fc⟧
f1 = 2*integrate.quad(lambda s: 2/(1 + 4*np.pi**2*s**2), 0, np.inf, weight="cos", wvar=2*np.pi*1.0)[0]
assert abs(f1 - np.exp(-1)) < 1e-6                                 # ⟦tự nghịch đảo: thu lại f(1)||self-inverse: recover f(1)⟧
report("fc_02", Fc, ".4f"); report("fs_02", Fs, ".4f")
report("f_re_02", F_caus.real, ".4f"); report("f_im_02", F_caus.imag, ".4f")
report("f1_rec", f1, ".4f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Cả {{conj_ok}} trên 7 quan hệ không tầm thường của bảng liên hợp đều đúng. Với $e^{-x}$ tại $s=0.2$: $F_c$ = {{fc_02}}, $F_s$ = {{fs_02}}, nên $F$ có phần thực {{f_re_02}} và phần ảo {{f_im_02}}, đúng $\\tfrac12F_c-\\tfrac12iF_s$ và đúng $1/(1+i2\\pi s)$. Biến đổi Fourier của mở rộng chẵn $e^{-|x|}$ cho {{fc_02}}, và phép cosin ngược thu lại $f(1)$ = {{f1_rec}}, đúng $e^{-1}$: biến đổi cosin tự nghịch đảo.||All {{conj_ok}} of 7 non-trivial relations in the conjugate table hold. For $e^{-x}$ at $s=0.2$: $F_c$ = {{fc_02}}, $F_s$ = {{fs_02}}, so $F$ has real part {{f_re_02}} and imaginary part {{f_im_02}}, exactly $\\tfrac12F_c-\\tfrac12iF_s$ and exactly $1/(1+i2\\pi s)$. The Fourier transform of the even extension $e^{-|x|}$ gives {{fc_02}}, and the inverse cosine transform recovers $f(1)$ = {{f1_rec}}, exactly $e^{-1}$: the cosine transform is its own inverse.⟧"""),
        ("md", """## 5. ⟦Ba cách hình dung tích phân Fourier||Three pictures of the Fourier integral⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Vì sao $F(s)$ nhỏ ở tần số cao, $F(0)$ là gì, và xoắn ốc trên mặt phẳng phức biểu diễn $F(s)$ ra sao? Ta tính diện tích dưới $f\\cos2\\pi sx$ và tích phân tích lũy trên mặt phẳng phức, mỗi thứ bằng hai cách.||Why is $F(s)$ small at high frequency, what is $F(0)$, and how does the spiral on the complex plane represent $F(s)$? We compute the area under $f\\cos2\\pi sx$ and the cumulative integral on the complex plane, each two ways.⟧"""),
        ("code", r'''fg = lambda x: np.exp(-np.pi*x**2)
area_low = ft_support(fg, -8, 8, 0.25).real; area_high = ft_support(fg, -8, 8, 2.0).real
assert abs(area_low - np.exp(-np.pi*0.25**2)) < 1e-9 and abs(area_high - np.exp(-4*np.pi)) < 1e-9
assert abs(ft_support(fg, -8, 8, 0.0).real - 1) < 1e-9             # ⟦F(0) = ∫ f||F(0) = ∫ f⟧
report("area_low", area_low, ".4f"); report("area_high", area_high, ".2e")

def locus(s, X=15.0, n=200001):                                     # ⟦tích phân tích lũy ∫_0^X e^{-x}e^{-i2πsx}dx||cumulative integral ∫_0^X e^{-x}e^{-i2πsx}dx⟧
    x = np.linspace(0, X, n); w = np.exp(-x)*np.exp(-2j*np.pi*s*x)
    return x, np.concatenate([[0], np.cumsum((w[1:] + w[:-1])/2*np.diff(x))])
loci = {}
for s_, tag in ((0.1, "01"), (0.5, "05")):
    x_, cum = locus(s_); exact = 1/(1 + 2j*np.pi*s_)
    assert abs(cum[-1] - exact) < 1e-6
    loci[tag] = cum; report(f"spiral_abs_{tag}", abs(exact), ".4f")'''),
        ("code", r'''xs_ = np.linspace(-3, 3, 1201)
fig, ax = plt.subplots(1, 3, figsize=(12, 3.2))
for s_, c in ((0.25, "tab:blue"), (2.0, "tab:red")):
    ax[0].plot(xs_, fg(xs_)*np.cos(2*np.pi*s_*xs_), color=c, label=f"s = {s_}")
ax[0].plot(xs_, fg(xs_), "k--", lw=0.8); ax[0].legend(); ax[0].set_title("f(x) cos 2πsx", fontsize=9)
ss = np.linspace(0, 2.5, 400); ax[1].plot(ss, np.exp(-np.pi*ss**2)); ax[1].set_title("F(s)", fontsize=9); ax[1].set_xlabel("s")
for tag, c in (("01", "tab:blue"), ("05", "tab:red")):
    ax[2].plot(loci[tag].real, loci[tag].imag, color=c, label=f"s = {int(tag)/10}")
ax[2].set_aspect("equal"); ax[2].legend(); ax[2].set_title("⟦xoắn ốc trên mặt phẳng phức||spiral on the complex plane⟧", fontsize=9)
plt.tight_layout(); plt.show()''', dict(fig="interpretation", cap="⟦Hình 4. Trái: f cos 2πsx ở tần số thấp (xanh) giữ diện tích, ở tần số cao (đỏ) tự triệt tiêu. Giữa: F(s) của Gauss. Phải: xoắn ốc của e^{−x}H(x) trên mặt phẳng phức.||Figure 4. Left: f cos 2πsx at low frequency (blue) keeps its area, at high frequency (red) it cancels itself. Middle: F(s) of the Gaussian. Right: the spiral of e^{−x}H(x) on the complex plane.⟧")),
        ("code", r'''xs2 = np.linspace(-3, 3, 1201)
plt.figure(figsize=(5.5, 3.3))
for s_, c in ((0.1, "tab:blue"), (0.5, "tab:red")):
    x_, cum = locus(s_, 12, 4001)
    plt.plot(cum.real, cum.imag, color=c, label=f"s = {s_}")
plt.gca().set_aspect("equal"); plt.legend(); plt.xlabel("Re"); plt.ylabel("Im")
plt.tight_layout(); plt.show()''', dict(fig="spiral", cap="⟦Hình 5. Xoắn ốc của tích phân tích lũy ∫₀^X e^{−x}e^{−i2πsx}dx. Với s = 0.5 (đỏ) đường cuộn nhanh và điểm cuối gần gốc hơn so với s = 0.1 (xanh).||Figure 5. The spiral of the cumulative integral ∫₀^X e^{−x}e^{−i2πsx}dx. For s = 0.5 (red) the path coils faster and ends nearer the origin than for s = 0.1 (blue).⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Với Gauss, diện tích dưới $f\\cos2\\pi sx$ là {{area_low}} tại $s=0.25$ nhưng chỉ {{area_high}} tại $s=2$: dao động nhanh làm các nửa chu kỳ dương và âm triệt tiêu, nên $F(s)\\to0$ khi $s\\to\\infty$, còn $F(0)=\\int f$. Xoắn ốc của $e^{-x}H(x)$ kết thúc ở vector có độ dài {{spiral_abs_01}} khi $s=0.1$ và {{spiral_abs_05}} khi $s=0.5$; tích phân tích lũy trùng công thức đóng $1/(1+i2\\pi s)$.||For the Gaussian, the area under $f\\cos2\\pi sx$ is {{area_low}} at $s=0.25$ but only {{area_high}} at $s=2$: fast oscillation makes the positive and negative half-cycles cancel, so $F(s)\\to0$ as $s\\to\\infty$, and $F(0)=\\int f$. The spiral of $e^{-x}H(x)$ ends at a vector of length {{spiral_abs_01}} for $s=0.1$ and {{spiral_abs_05}} for $s=0.5$; the cumulative integral matches the closed form $1/(1+i2\\pi s)$.⟧"""),
    ],
)
