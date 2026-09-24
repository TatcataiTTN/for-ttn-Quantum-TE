from lib import F, C, UL, OL, TBL

MOD = dict(
    n=3, slug="convolution", part="A", book="B",
    title="⟦Tích chập, tích chập nối tiếp và tương quan||Convolution, serial products and correlation⟧",
    blurb="⟦Tích chập là phép làm việc chung của mọi hệ tuyến tính bất biến; chương này dạy cách hình dung, tính tay, tính bằng máy, và các họ hàng của nó: tự tương quan, tương quan chéo, phổ năng lượng.||"
          "Convolution is the common operation of every linear invariant system; this chapter teaches how to picture it, compute it by hand and by machine, and its relatives: autocorrelation, cross correlation and the energy spectrum.⟧",
    src="⟦Bracewell, chương 3, tr. 24–50||Bracewell, chapter 3, pp. 24–50⟧",
    data="⟦Sinh bằng mã: hai hàm mũ cắt cụt, xung chữ nhật lặp, các dãy số của Bracewell, chuỗi nhiệt độ ngày, ba sóng hình sin với pha khác nhau, dãy xung $\\{1100101\\}$||Generated in code: truncated exponentials, repeated rectangles, Bracewell's number sequences, a daily-temperature series, three sinusoids with different phases, the pulse sequence $\\{1100101\\}$⟧",
    objectives=[
        "⟦Định nghĩa tích chập và hình dung nó bằng bốn cách: diện tích, làm mượt, chồng chất, gập.||Define convolution and picture it four ways: area, smoothing, superposition, folding.⟧",
        "⟦Tính tích chập của hàm mũ cắt cụt và của các dãy số bằng tay, kiểm bằng tổng các số hạng.||Compute the convolution of truncated exponentials and of number sequences by hand, checked by the sum of terms.⟧",
        "⟦Đảo tích chập nối tiếp (chia dãy), dùng bảng dãy nghịch đảo, và viết tích chập dưới dạng ma trận.||Invert a serial product (serial division), use the table of reciprocal sequences and write convolution as a matrix.⟧",
        "⟦Tính tích chập bằng máy, biết khi nào FFT bị cuộn vòng.||Compute convolution by machine and know when an FFT wraps around.⟧",
        "⟦Dùng tự tương quan, tương quan chéo, tương quan bậc ba và phổ năng lượng, và biết chúng bỏ mất thông tin gì.||Use autocorrelation, cross correlation, triple correlation and the energy spectrum, and know what information they discard.⟧",
    ],
    parts=[
        # ------------------------------------------------------------ PART 1
        dict(
            title="⟦Định nghĩa và các cách hình dung tích chập||Definition and pictures of convolution⟧",
            scr=("⟦Bạn đã thấy ở module 1 rằng đáp ứng của hệ tuyến tính bất biến là một tích chập.||Module 1 showed that the response of a linear invariant system is a convolution.⟧",
                 "⟦Nhưng khi trình bày thẳng bằng tích phân, tích chập là một khái niệm khá khó nắm.||Yet presented bluntly as an integral, convolution is a fairly tricky concept.⟧",
                 "⟦Bracewell dạy nó bằng bốn cách nhìn bổ sung nhau, cùng các tính chất đại số như phép nhân.||Bracewell teaches it through four complementary views and algebraic rules that behave like multiplication.⟧"),
            preview=["⟦Định nghĩa và các tên gọi khác||The definition and its other names⟧",
                     "⟦Bốn cách hình dung với số đo||Four pictures with numbers⟧",
                     "⟦Giao hoán, kết hợp, phân phối||Commutative, associative, distributive⟧"],
            slides=[
                ("⟦Một khái niệm nhiều tên||One concept, many names⟧",
                 "<p>⟦Tích chập xuất hiện ở nhiều nơi với nhiều tên: Faltung (tiếng Đức), tích thành phần (\"composition product\"), tích phân chồng chất, tích phân Duhamel, định lý Borel, trung bình trượt (có trọng số), hàm tương quan chéo, làm mượt, làm nhòe, quét (Bracewell, tr. 24).||"
                 "Convolution occurs widely under many aliases: Faltung (German), composition product, superposition integral, Duhamel integral, Borel's theorem, (weighted) running mean, cross-correlation function, smoothing, blurring, scanning, smearing (Bracewell, p. 24).⟧</p>"),
                ("⟦Định nghĩa||Definition⟧",
                 "<p>⟦Tích chập của $f(x)$ và $g(x)$ cũng là một hàm của $x$, gọi là $h(x)$ (tr. 24).||The convolution of $f(x)$ and $g(x)$ is itself a function of $x$, called $h(x)$ (p. 24).⟧</p>"
                 + F("⟦Tích chập||Convolution⟧", r"h(x)=f(x)*g(x)=\int_{-\infty}^{\infty}f(u)\,g(x-u)\,du",
                     [("u", "⟦biến giả để lấy tích phân||dummy variable of integration⟧"), ("g(x-u)", "⟦$g$ đã được đảo chiều rồi dịch tới $x$||$g$ reversed and shifted to $x$⟧")])),
                ("⟦Hàm của hàm: cần biết $f$ trên cả một khoảng||A functional: it needs $f$ over a whole range⟧",
                 "<p>⟦Theo Volterra, $h$ là một phiếm hàm của $f$. Để tính $h(x_1)$ ta cần biết $f$ trên cả một khoảng $x$, trong khi một hàm của hàm $f$ tại $x=x_1$ chỉ cần $f(x_1)$ (tr. 25). Đây là lý do tích chập mô tả \"trí nhớ\" của hệ.||"
                 "Following Volterra, $h$ is a functional of $f$. To calculate $h(x_1)$ we need $f$ over a whole range of $x$, whereas a function of the function $f$ at $x=x_1$ needs only $f(x_1)$ (p. 25). That is why convolution describes the \"memory\" of a system.⟧</p>"),
                ("⟦Cách nhìn 1: diện tích của tích $f(u)g(x-u)$||View 1: the area of the product $f(u)g(x-u)$⟧",
                 "<p>⟦Trong hình 3.1, tích $f(u)g(x-u)$ được tô bóng và tung độ $h(x)$ bằng diện tích phần tô (tr. 25). Ví dụ số: $f=\\Pi$ và $g=e^{-u}H(u)$; tại $x=1$ diện tích chồng lấn là $e^{-1/2}-e^{-3/2}$ = {{ov_x1}} (tích phân số và công thức đóng trùng nhau).||"
                 "In Fig. 3.1 the product $f(u)g(x-u)$ is shaded and the ordinate $h(x)$ equals the shaded area (p. 25). Numerical example: $f=\\Pi$ and $g=e^{-u}H(u)$; at $x=1$ the overlap area is $e^{-1/2}-e^{-3/2}$ = {{ov_x1}} (numerical integral and closed form agree).⟧</p>"),
                ("⟦Cách nhìn 2: làm mượt||View 2: smoothing⟧",
                 "<p>⟦So với $f$, hàm $h=f*g$ mượt hơn, rộng hơn và có tổng biến thiên nhỏ hơn (hình 3.2, tr. 25). Ví dụ: chuỗi $\\pm1$ đảo dấu liên tục có tổng biến thiên {{tv_f}}; sau khi làm trung bình trượt 5 điểm còn {{tv_h}}.||"
                 "Compared with $f$, the function $h=f*g$ is smoother in detail, more spread out and has less total variation (Fig. 3.2, p. 25). Example: a $\\pm1$ series that flips sign constantly has total variation {{tv_f}}; after a 5-point running mean it has {{tv_h}}.⟧</p>"),
                ("⟦Cách nhìn 3 và 4: chồng chất và gập||Views 3 and 4: superposition and folding⟧",
                 "<p>⟦Cách 3: chia $f$ thành các cột nhỏ, mỗi cột \"tan\" thành một đống có dạng $g$ đặt tại vị trí cột, rồi $h(x)$ là tổng các đóng góp tại $x$ (hình 3.3). Cách 4: gập $g(u)$ quanh đường $u=x/2$, diện tích dưới tích $f(u)g(x-u)$ chính là $h(x)$ (hình 3.4) (tr. 25 đến 26).||"
                 "View 3: resolve $f$ into infinitesimal columns, each \"melted out\" into a heap shaped like $g$ centred at the column, and $h(x)$ is the sum of contributions at $x$ (Fig. 3.3). View 4: fold $g(u)$ about the line $u=x/2$; the area under the product is $h(x)$ (Fig. 3.4) (pp. 25 to 26).⟧</p>"
                 + F("⟦Cách nhìn chồng chất||The superposition view⟧", r"h(x)=\int_{-\infty}^{\infty}f(x_1)\,g(x-x_1)\,dx_1")),
                ("⟦Đại số: giao hoán, kết hợp, phân phối||Algebra: commutative, associative, distributive⟧",
                 "<p>⟦Vì $g$ bị đảo chiều trước khi nhân, tích chập giao hoán. Nó còn kết hợp (khi các tích phân tồn tại) và phân phối trên phép cộng, nên dấu $*$ cư xử như dấu nhân trong biến đổi hình thức (tr. 26 đến 27). Notebook kiểm cả ba tính chất trên dãy ngẫu nhiên: {{props_ok}} trên 3 đều đúng.||"
                 "Because $g$ is reversed before multiplying, convolution is commutative. It is also associative (when the integrals exist) and distributive over addition, so the asterisks behave like multiplication signs in formal manipulation (pp. 26 to 27). The notebook checks all three on random sequences: {{props_ok}} of 3 hold.⟧</p>"
                 + F("⟦Ba tính chất||Three properties⟧", r"f*g=g*f,\qquad f*(g*h)=(f*g)*h,\qquad f*(g+h)=f*g+f*h")),
                ("⟦Ý nghĩa vật lý: mọi phép quan sát đều là một tích chập||Physical meaning: every observation is a convolution⟧",
                 "<p>⟦Tích chập mô tả tác động của một dụng cụ khi lấy trung bình có trọng số một đại lượng vật lý trên một khoảng hẹp của một biến. Khi dạng của hàm trọng số không đổi theo vị trí, đại lượng quan sát được là tích chập chứ không phải đại lượng cần đo. Mọi phép quan sát đều bị giới hạn bởi độ phân giải của dụng cụ, chỉ riêng điều này đã làm tích chập có mặt khắp nơi (tr. 24). Sự xuất hiện của tích chập trùng với tuyến tính cộng bất biến, và với \"đáp ứng điều hòa với kích thích điều hòa\".||"
                 "Convolution describes the action of an observing instrument when it takes a weighted mean of some physical quantity over a narrow range of a variable. When the weighting function does not change with position, the observed quantity is a convolution rather than the desired quantity itself. All physical observations are limited by the resolving power of instruments, and for this reason alone convolution is ubiquitous (p. 24). Its appearance is coterminous with linearity plus invariance, and with harmonic response to harmonic stimulus.⟧</p>"),
                ("⟦Tự kiểm tra phần 1||Self-check, part 1⟧",
                 UL(["⟦Vì sao tích chập giao hoán dù $g$ bị đảo chiều còn $f$ thì không?||Why is convolution commutative even though $g$ is reversed and $f$ is not?⟧",
                     "⟦Vì sao gọi $h(x)$ là một phiếm hàm của $f$?||Why is $h(x)$ called a functional of $f$?⟧",
                     "⟦Khi nào ảnh quan sát được là tích chập của vật với dụng cụ?||When is an observed image the convolution of the object with the instrument?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: đổi biến $u\\to x-u$; cần $f$ trên cả khoảng; khi hàm trọng số không đổi theo vị trí.||Hints: substitute $u\\to x-u$; it needs $f$ over a range; when the weighting function does not change with position.⟧</p>"),
            ]),
        # ------------------------------------------------------------ PART 2
        dict(
            title="⟦Các ví dụ tích chập và cách dựng đồ thị||Examples of convolution and the graphical construction⟧",
            scr=("⟦Công thức tích chập dễ sai cận tích phân và dấu.||It is easy to get the limits and signs of a convolution integral wrong.⟧",
                 "⟦Một phép tính đại số sai một chút có thể đổi hoàn toàn kết quả.||An ordinary algebraic slip can change the result radically.⟧",
                 "⟦Tính vài ví dụ kinh điển rồi kiểm bằng cách dựng đồ thị (tờ giấy trượt) và bằng các quy tắc diện tích, phương sai.||Work a few classic examples and check them by the graphical construction (the sliding paper) and by the rules for area and variance.⟧"),
            preview=["⟦Hai hàm mũ cắt cụt và các giới hạn||Two truncated exponentials and their limits⟧",
                     "⟦Tờ giấy trượt||The sliding paper⟧",
                     "⟦Lặp tích chập và quy tắc phương sai||Repeated convolution and the variance rule⟧"],
            slides=[
                ("⟦Tích chập của hai hàm mũ cắt cụt||Convolution of two truncated exponentials⟧",
                 "<p>⟦Đặt $E(x)=e^{-x}H(x)$. Với hai hằng số suy giảm dương khác nhau $\\alpha,\\beta$, Bracewell tính (tr. 27):||Let $E(x)=e^{-x}H(x)$. For two different positive decay constants $\\alpha,\\beta$, Bracewell computes (p. 27):⟧</p>"
                 + F("⟦Hai hàm mũ cắt cụt||Two truncated exponentials⟧", r"\alpha E(\alpha x)*\beta E(\beta x)=\alpha\beta\,\frac{E(\alpha x)-E(\beta x)}{\beta-\alpha}",
                     [(r"\alpha,\beta", "⟦hằng số suy giảm||decay constants⟧")])),
                ("⟦Số đo: chuỗi phân rã phóng xạ||Numbers: a radioactive decay chain⟧",
                 "<p>⟦Kết quả là hiệu của hai hàm mũ cắt cụt cùng biên độ. Nó mô tả nồng độ một đồng vị phân rã với hằng số $\\alpha$ trong khi được bổ sung từ đồng vị mẹ phân rã với hằng số $\\beta$. Với $\\alpha=1,\\beta=2$ tại $x=1$: tích phân số và công thức cho {{ex_x1}}. Khi $x\\to\\infty$ chỉ còn số hạng suy giảm chậm hơn (tr. 28).||"
                 "The result is the difference of two truncated exponentials with the same amplitude. It describes the concentration of an isotope decaying with constant $\\alpha$ while replenished as the decay product of a parent isotope decaying with constant $\\beta$. With $\\alpha=1,\\beta=2$ at $x=1$: numerical integration and the formula give {{ex_x1}}. As $x\\to\\infty$ only the more slowly decaying term survives (p. 28).⟧</p>{{fig:exp_conv}}"),
                ("⟦Giới hạn $\\beta\\to\\alpha$: bộ cộng hưởng tới hạn||The limit $\\beta\\to\\alpha$: the critically damped resonator⟧",
                 "<p>⟦Lấy giới hạn $\\beta-\\alpha\\to0$ ta có $\\alpha E(\\alpha x)*\\alpha E(\\alpha x)=\\alpha^2xE(\\alpha x)$. Hàm này mô tả đáp ứng của bộ cộng hưởng tắt dần tới hạn, như điện kế không dao động, với một xung tác động (tr. 28). Với $\\alpha=1$ tại $x=2$: {{crit_x2}}.||"
                 "Taking $\\beta-\\alpha\\to0$ gives $\\alpha E(\\alpha x)*\\alpha E(\\alpha x)=\\alpha^2xE(\\alpha x)$. This function describes the response of a critically damped resonator, such as a dead-beat galvanometer, to an impulsive disturbance (p. 28). With $\\alpha=1$ at $x=2$: {{crit_x2}}.⟧</p>"
                 + F("⟦Giới hạn tới hạn||The critical limit⟧", r"\alpha E(\alpha x)*\alpha E(\alpha x)=\alpha^{2}\,x\,E(\alpha x)")),
                ("⟦Hai đuôi ngược chiều||Two opposed tails⟧",
                 "<p>⟦$\\alpha E(-\\alpha x)*\\beta E(\\beta x)$ cho một hàm nhọn tại gốc, suy giảm với hằng số $\\alpha$ về bên trái và $\\beta$ về bên phải (tr. 28 đến 29). Với $\\alpha=1,\\beta=2$: tại $x=-1$ là {{opp_l1}}, tại $x=+1$ là {{opp_r1}}, nên bên phải rơi nhanh hơn.||"
                 "$\\alpha E(-\\alpha x)*\\beta E(\\beta x)$ gives a function peaked at the origin dying away with constant $\\alpha$ to the left and $\\beta$ to the right (pp. 28 to 29). With $\\alpha=1,\\beta=2$: at $x=-1$ it is {{opp_l1}}, at $x=+1$ it is {{opp_r1}}, so the right side falls faster.⟧</p>"
                 + F("⟦Hai đuôi||Two tails⟧", r"\alpha E(-\alpha x)*\beta E(\beta x)=\frac{\alpha\beta}{\alpha+\beta}\left[E(-\alpha x)+E(\beta x)\right]")),
                ("⟦Dựng đồ thị: tờ giấy trượt||Graphical construction: the sliding paper⟧",
                 "<p>⟦Để kiểm phép tính, vẽ một hàm đảo ngược lên một tờ giấy rồi trượt dọc trục hoành. Khi tờ giấy ở bên trái, tích bằng 0. Rồi tích phân bắt đầu khác 0, tăng gần tuyến tính, đạt cực đại rồi giảm. Bằng cách này ta thấy ngay các đuôi ngược chiều, chỗ không có đoạn bằng 0 và bước nhảy độ dốc tại gốc (tr. 29 đến 30). Chuyên gia làm việc này trong đầu.||"
                 "To check a calculation, plot one function backward on a movable piece of paper and slide it along the abscissa. To the left, the product is zero. Then the integral starts to be nonzero, increases nearly linearly, reaches a maximum and dies away. This shows at once the opposed tails, the absence of a zero stretch and the jump in slope at the origin (pp. 29 to 30). Experts do this in their heads.⟧</p>"),
                ("⟦Lặp tích chập xung chữ nhật||Repeated convolution of the rectangle⟧",
                 "<p>⟦$\\Pi*\\Pi=\\Lambda$ (tam giác), rồi $\\Pi*\\Pi*\\Pi$ là một đường parabol từng khúc. Notebook lặp tích chập trên lưới mịn: tại $x=0$ giá trị là {{b3_0}} (đúng $3/4$) và tại $x=1$ là {{b3_1}} (đúng $1/8$). Mỗi lần tích chập, hình dạng mượt hơn và trông giống Gauss hơn.||"
                 "$\\Pi*\\Pi=\\Lambda$ (a triangle), then $\\Pi*\\Pi*\\Pi$ is a piecewise parabola. The notebook repeats the convolution on a fine grid: at $x=0$ the value is {{b3_0}} (exactly $3/4$) and at $x=1$ it is {{b3_1}} (exactly $1/8$). Each convolution makes the shape smoother and more Gaussian.⟧</p>{{fig:pi_repeat}}"),
                ("⟦Quy tắc diện tích và phương sai||Rules for area and variance⟧",
                 "<p>⟦Với các hàm diện tích 1, tích chập nhân diện tích (nên vẫn diện tích 1) và cộng phương sai. Ví dụ $e^{-x}H(x)$ (phương sai 1) chập với $\\Pi$ (phương sai $1/12$) cho phương sai {{var_conv}} và diện tích {{area_conv}}. Lặp $n$ lần $\\Pi$ có phương sai $n/12$; độ lệch tối đa so với Gauss cùng phương sai là {{gauss_dev4}} khi $n=4$ và {{gauss_dev8}} khi $n=8$.||"
                 "For unit-area functions, convolution multiplies areas (so the area stays 1) and adds variances. For example $e^{-x}H(x)$ (variance 1) convolved with $\\Pi$ (variance $1/12$) gives variance {{var_conv}} and area {{area_conv}}. Repeating $\\Pi$ $n$ times has variance $n/12$; the largest deviation from a Gaussian of the same variance is {{gauss_dev4}} for $n=4$ and {{gauss_dev8}} for $n=8$.⟧</p>"
                 + F("⟦Cộng phương sai||Variances add⟧", r"\sigma^2_{f*g}=\sigma^2_f+\sigma^2_g\quad(\text{⟦với diện tích 1||for unit area⟧})")),
                ("⟦Tự kiểm tra phần 2||Self-check, part 2⟧",
                 UL(["⟦Khi $\\beta\\to\\alpha$ kết quả tiến về hàm nào?||Which function does the result approach as $\\beta\\to\\alpha$?⟧",
                     "⟦Bên nào của $\\alpha E(-\\alpha x)*\\beta E(\\beta x)$ suy giảm nhanh hơn nếu $\\beta>\\alpha$?||Which side of $\\alpha E(-\\alpha x)*\\beta E(\\beta x)$ decays faster if $\\beta>\\alpha$?⟧",
                     "⟦Phương sai của tích chập của ba xung chữ nhật là bao nhiêu?||What is the variance of the convolution of three rectangles?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: $\\alpha^2xE(\\alpha x)$; bên phải; $3/12=1/4$.||Hints: $\\alpha^2xE(\\alpha x)$; the right side; $3/12=1/4$.⟧</p>"),
            ]),
        # ------------------------------------------------------------ PART 3
        dict(
            title="⟦Tích chập nối tiếp: dãy số, phép chia và ma trận||Serial products: sequences, division and matrices⟧",
            scr=("⟦Khi tính số, ta thay hàm bằng dãy giá trị cách đều.||For numerical work we replace functions by equally spaced values.⟧",
                 "⟦Phép tính đó trùng với nhân đa thức, và ta muốn cả chiều ngược lại: biết tích và một thừa số, tìm thừa số còn lại.||That calculation coincides with polynomial multiplication, and we want the reverse direction too: given the product and one factor, find the other.⟧",
                 "⟦Tích chập nối tiếp, bảng dãy nghịch đảo và biểu diễn ma trận trả lời cả hai.||Serial products, the table of reciprocal sequences and the matrix form answer both.⟧"),
            preview=["⟦Đa thức và dãy số||Polynomials and sequences⟧",
                     "⟦Chia dãy và bảng 3.1||Serial division and Table 3.1⟧",
                     "⟦Ma trận Toeplitz và hệ thay đổi theo thời gian||Toeplitz matrices and time-varying systems⟧"],
            slides=[
                ("⟦Nhân đa thức chính là tích chập nối tiếp||Multiplying polynomials is a serial product⟧",
                 "<p>⟦Tích của hai đa thức $a_0+a_1x+\\dots$ và $b_0+b_1x+\\dots$ có hệ số $c_0=a_0b_0$, $c_1=a_0b_1+a_1b_0$, $c_2=a_0b_2+a_1b_1+a_2b_0$, ... Đó chính là các tổng của tích chập rời rạc (Bracewell, tr. 30). Notebook so <code>polymul</code> với <code>convolve</code> và thấy trùng.||"
                 "The product of two polynomials $a_0+a_1x+\\dots$ and $b_0+b_1x+\\dots$ has coefficients $c_0=a_0b_0$, $c_1=a_0b_1+a_1b_0$, $c_2=a_0b_2+a_1b_1+a_2b_0$, ... These are exactly the sums of discrete convolution (Bracewell, p. 30). The notebook compares <code>polymul</code> with <code>convolve</code> and finds them equal.⟧</p>"
                 + F("⟦Tích chập nối tiếp||Serial product⟧", r"h_i=\sum_{j}f_j\,g_{i-j},\qquad \{h\}=\{f\}*\{g\}")),
                ("⟦Độ dài và tổng: hai phép kiểm nhanh||Length and sum: two quick checks⟧",
                 "<p>⟦Tích chập nối tiếp dài hơn từng thành phần: số số hạng bằng tổng hai độ dài trừ một. Tổng các số hạng bằng tích hai tổng, một phép kiểm số rất quý. Nếu một dãy có tổng bằng 1 thì tổng tích bằng tổng dãy kia (tr. 32). Ví dụ: dãy 7 số hạng chập dãy 4 số hạng cho {{len74}} số hạng.||"
                 "The serial product is longer than either component: the number of terms is the sum of the lengths minus one. The sum of the terms equals the product of the sums, a very valuable numerical check. If one sequence sums to unity the product sums to the same as the other (p. 32). Example: a 7-term sequence with a 4-term one gives {{len74}} terms.⟧</p>"),
                ("⟦Dãy nửa vô hạn và hai phía||Semi-infinite and two-sided sequences⟧",
                 "<p>⟦Dãy nửa vô hạn như $\\{1,1\\}*\\{1,2,3,\\dots\\}=\\{1,3,5,7,\\dots\\}$ vẫn cho tích chập nối tiếp hợp lệ vì mỗi số hạng chỉ có hữu hạn số hạng cộng lại. Nhưng nếu hai dãy kéo dài ngược chiều thì mỗi số hạng là tổng vô hạn và có thể không tồn tại. Với dãy hai phía phải nêu rõ gốc, ví dụ bằng mũi tên (tr. 32 đến 33).||"
                 "A semi-infinite sequence such as $\\{1,1\\}*\\{1,2,3,\\dots\\}=\\{1,3,5,7,\\dots\\}$ still gives a valid serial product since each term sums only finitely many terms. But if two sequences run on in opposite directions each term is an infinite sum that may not exist. Two-sided sequences need the origin stated explicitly, for example by an arrow (pp. 32 to 33).⟧</p>"),
                ("⟦Các dãy đặc biệt||Special sequences⟧",
                 "<p>⟦Dãy $\\{\\dots0,0,1,0,0,\\dots\\}$ đóng vai trò như xung: chập với nó không đổi gì. $\\{1,-1\\}$ lấy sai phân bậc nhất. $\\frac1n\\{1,\\dots,1\\}$ ($n$ số hạng) là trung bình trượt; ví dụ trung bình tuần của số liệu ngày là $\\frac17\\{1,1,1,1,1,1,1\\}$. $\\{1,1,1,\\dots\\}$ cho tổng chạy (tr. 33).||"
                 "The sequence $\\{\\dots0,0,1,0,0,\\dots\\}$ plays the role of the impulse: convolving with it changes nothing. $\\{1,-1\\}$ takes the first difference. $\\frac1n\\{1,\\dots,1\\}$ ($n$ terms) is a running mean; for example a weekly mean of daily values is $\\frac17\\{1,1,1,1,1,1,1\\}$. $\\{1,1,1,\\dots\\}$ gives running sums (p. 33).⟧</p>"),
                ("⟦Thử số: tổng chạy và sai phân là hai phép nghịch đảo||Numerical test: running sums and differences invert each other⟧",
                 "<p>⟦Với dãy $\\{3,1,4,1,5,9,2,6\\}$, tổng chạy có số cuối {{run_last}}, và lấy sai phân bằng $\\{1,-1\\}*$ trả lại đúng dãy gốc. Đây là hệ thức $\\{1,1,1,\\dots\\}*\\{1,-1\\}=\\{1,0,0,\\dots\\}$ (tr. 34): hai dãy nghịch đảo của nhau, như tích phân và đạo hàm.||"
                 "For the sequence $\\{3,1,4,1,5,9,2,6\\}$ the running sum ends at {{run_last}}, and taking differences with $\\{1,-1\\}*$ returns exactly the original. This is the relation $\\{1,1,1,\\dots\\}*\\{1,-1\\}=\\{1,0,0,\\dots\\}$ (p. 34): the two sequences are reciprocal, like integration and differentiation.⟧</p>"),
                ("⟦Dãy nghịch đảo||Reciprocal sequences⟧",
                 "<p>⟦Dãy nghịch đảo $\\{f\\}^{-1}$ của $\\{f\\}$ thỏa $\\{f\\}^{-1}*\\{f\\}=\\{1,0,0,\\dots\\}$. Nếu $\\{f\\}*\\{g\\}=\\{h\\}$ và biết $\\{f\\}$, $\\{h\\}$ thì $\\{g\\}=\\{f\\}^{-1}*\\{h\\}$. Ví dụ $\\{1,2,3,4,\\dots\\}$ và $\\{1,-2,1\\}$ là cặp nghịch đảo (tr. 34). Notebook kiểm: {{recip_ok}} trên 2 cặp đúng.||"
                 "The reciprocal sequence $\\{f\\}^{-1}$ of $\\{f\\}$ satisfies $\\{f\\}^{-1}*\\{f\\}=\\{1,0,0,\\dots\\}$. If $\\{f\\}*\\{g\\}=\\{h\\}$ and $\\{f\\}$, $\\{h\\}$ are known, then $\\{g\\}=\\{f\\}^{-1}*\\{h\\}$. For example $\\{1,2,3,4,\\dots\\}$ and $\\{1,-2,1\\}$ are a reciprocal pair (p. 34). The notebook checks: {{recip_ok}} of 2 pairs hold.⟧</p>"),
                ("⟦Chia dãy: tìm thừa số còn lại||Serial division: finding the other factor⟧",
                 "<p>⟦Muốn giải $\\{1,1\\}*\\{g\\}=\\{1,3,3,1\\}$, có thể chia đa thức hoặc dùng cách của Bracewell: $g_0=h_0/f_0$, rồi mỗi số hạng tiếp theo bằng $h_k$ trừ tổng các tích đã biết, chia cho $f_0$ (tr. 34 đến 36). Cả hai cho $\\{g\\}$ = ({{div_g}}).||"
                 "To solve $\\{1,1\\}*\\{g\\}=\\{1,3,3,1\\}$ one can do long division of polynomials or use Bracewell's method: $g_0=h_0/f_0$, then each next term is $h_k$ minus the sum of the known products, divided by $f_0$ (pp. 34 to 36). Both give $\\{g\\}$ = ({{div_g}}).⟧</p>"
                 + F("⟦Đệ quy chia dãy||Serial-division recursion⟧", r"g_k=\frac{h_k-\sum_{j=1}^{k}f_j\,g_{k-j}}{f_0}")),
                ("⟦Bảng 3.1: các dãy và nghịch đảo||Table 3.1: sequences and their inverses⟧",
                 "<p>⟦Bracewell liệt kê các cặp thường gặp (tr. 37); notebook kiểm {{tab_ok}} trên 6 cặp đầu bằng nhân rồi xem {1, 0, 0, ...}.||"
                 "Bracewell lists common pairs (p. 37); the notebook checks {{tab_ok}} of the first 6 pairs by multiplying and looking for {1, 0, 0, ...}.⟧</p>"
                 + TBL(["⟦Dãy||Sequence⟧", "⟦Nghịch đảo||Inverse⟧"],
                       [["$\\{1,1\\}$", "$\\{1,-1,1,-1,\\dots\\}$"], ["$\\{1,-1\\}$", "$\\{1,1,1,1,\\dots\\}$"], ["$\\{1,0,1\\}$", "$\\{1,0,-1,0,1,\\dots\\}$"],
                        ["$\\{1,2,1\\}$", "$\\{1,-2,3,-4,\\dots\\}$"], ["$\\{1,-a\\}$", "$\\{1,a,a^2,\\dots\\}$"], ["$\\{1,-a\\}^{*2}$", "$\\{1,2a,3a^2,\\dots\\}$"]])),
                ("⟦Dạng ma trận và hệ thay đổi theo thời gian||Matrix form and time-varying systems⟧",
                 "<p>⟦Tích chập nối tiếp viết được thành nhân một ma trận vuông (mỗi hàng là dãy $\\{f\\}$ đảo ngược, dịch một bước) với một vector cột. Ma trận này là ma trận Toeplitz. Cách viết hy sinh tính giao hoán nhưng cho phép tổng quát hóa: nếu các hàng thay đổi ta được phép biến đổi tuyến tính tổng quát, không phải bất biến. Với hệ thay đổi theo thời gian (như chiết áp chạy bằng động cơ), đáp ứng không còn là tích chập và \"đáp ứng điều hòa với kích thích điều hòa\" cũng hỏng (tr. 37 đến 39). Notebook kiểm: nhân ma trận Toeplitz và <code>convolve</code> trùng nhau ({{toep_ok}}).||"
                 "The serial product can be written as a square matrix (each row the sequence $\\{f\\}$ reversed and shifted one step) multiplying a column vector. That matrix is a Toeplitz matrix. The notation sacrifices commutativity but generalises: if the rows change we get the general linear transformation, not shift-invariant. For a time-varying system (such as motor-driven potentiometers) the response is no longer a convolution and \"harmonic response to harmonic excitation\" also breaks down (pp. 37 to 39). The notebook checks: the Toeplitz matrix product and <code>convolve</code> agree ({{toep_ok}}).⟧</p>"),
            ]),
        # ------------------------------------------------------------ PART 4
        dict(
            title="⟦Tích chập bằng máy tính||Convolution by computer⟧",
            scr=("⟦Định lý tích chập (chương 6) gợi ý tính tích chập qua FFT.||The convolution theorem (chapter 6) suggests computing convolution through an FFT.⟧",
                 "⟦Nhưng không phải lúc nào FFT cũng nhanh hơn, và dùng sai sẽ cho kết quả cuộn vòng.||But the FFT is not always faster, and misuse gives wrapped-around results.⟧",
                 "⟦Viết trực tiếp phép tính tay, đếm phép nhân, biết các chế độ độ dài, và tránh bẫy cuộn vòng.||Code the hand calculation directly, count the multiplications, know the length modes, and avoid the wrap-around trap.⟧"),
            preview=["⟦Đoạn mã trực tiếp và các chế độ độ dài||The direct code and the length modes⟧",
                     "⟦Đếm phép nhân: trực tiếp so với FFT||Counting multiplications: direct versus FFT⟧",
                     "⟦Bẫy cuộn vòng và ví dụ trung bình tuần||The wrap-around trap and a weekly-mean example⟧"],
            slides=[
                ("⟦Mã tính trực tiếp||The direct code⟧",
                 "<p>⟦Bracewell viết đoạn mã ngắn cho tích chập trực tiếp: với hai dãy độ dài $l_f$ và $l_g$, tích chập có độ dài $l_h=l_f+l_g-1$, và mỗi $h(I)$ cộng các tích $f(J)g(K)$ với $K=I-J+1$ (tr. 40). Trong ứng dụng lọc dữ liệu dài, đoạn mã này thường chạy nhanh hơn phương pháp biến đổi viết cùng ngôn ngữ (tr. 40).||"
                 "Bracewell gives a short code for direct convolution: for sequences of lengths $l_f$ and $l_g$ the convolution has length $l_h=l_f+l_g-1$, and each $h(I)$ sums the products $f(J)g(K)$ with $K=I-J+1$ (p. 40). In applications to filtering long data sets this code will usually run faster than a transform method written in the same language (p. 40).⟧</p>"),
                ("⟦Thử số: mã tay so với <code>convolve</code>||Numerical test: hand code versus <code>convolve</code>⟧",
                 "<p>⟦Notebook dịch đoạn mã sang Python và so với <code>numpy.convolve</code> trên hai cặp dãy ngẫu nhiên (độ dài 200 và 37, rồi 5 và 5): kết quả trùng tới sai số làm tròn, lệch lớn nhất {{code_diff}}.||"
                 "The notebook translates the code to Python and compares it with <code>numpy.convolve</code> on two pairs of random sequences (lengths 200 and 37, then 5 and 5): the results agree to rounding error, largest deviation {{code_diff}}.⟧</p>"),
                ("⟦Ba chế độ độ dài||Three length modes⟧",
                 "<p>⟦Với hai dãy độ dài 10 và 4: chế độ <em>full</em> (mọi vị trí chồng lấn) cho {{len_full}} số hạng, <em>same</em> cho {{len_same}} (cùng độ dài dãy dài) và <em>valid</em> (chỉ nơi hai dãy chồng lấn hoàn toàn) cho {{len_valid}}. Khi làm mượt số liệu, hãy nhớ rằng bờ dữ liệu bị ảnh hưởng.||"
                 "For sequences of length 10 and 4: <em>full</em> mode (every overlapping position) gives {{len_full}} terms, <em>same</em> gives {{len_same}} (the length of the longer) and <em>valid</em> (only where they overlap completely) gives {{len_valid}}. When smoothing data, remember that the edges are affected.⟧</p>"
                 + F("⟦Độ dài||Lengths⟧", r"l_{\text{full}}=l_f+l_g-1,\qquad l_{\text{valid}}=l_f-l_g+1")),
                ("⟦Đếm phép nhân: trực tiếp so với FFT||Counting multiplications: direct versus FFT⟧",
                 "<p>⟦Trực tiếp cần $l_fl_g$ phép nhân. Qua FFT cần ba phép biến đổi độ dài $N\\ge l_f+l_g-1$, cỡ $3N\\log_2N$ phép tính (ước lượng bậc độ lớn). Với $l_f=10^5$ và bộ lọc ngắn $l_g=32$: trực tiếp {{ops_direct_short}}, FFT cỡ {{ops_fft}}, cùng bậc. Với bộ lọc dài $l_g=2000$: trực tiếp {{ops_direct_long}}, FFT vẫn cỡ {{ops_fft2}}, nhanh hơn rõ rệt.||"
                 "Direct convolution needs $l_fl_g$ multiplications. Through the FFT it needs three transforms of length $N\\ge l_f+l_g-1$, of order $3N\\log_2N$ operations (an order-of-magnitude estimate). With $l_f=10^5$ and a short filter $l_g=32$: direct {{ops_direct_short}}, FFT about {{ops_fft}}, the same order. With a long filter $l_g=2000$: direct {{ops_direct_long}}, the FFT still about {{ops_fft2}}, clearly faster.⟧</p>"
                 + C("info", "⟦Lưu ý||Note⟧", "<p>⟦Đây là số phép tính ước lượng chứ không phải thời gian chạy. Thời gian thật còn phụ thuộc phần cứng và thư viện; hãy đo trên máy của bạn.||These are estimated operation counts, not run times. Real time also depends on hardware and library; measure on your own machine.⟧</p>")),
                ("⟦Bẫy cuộn vòng||The wrap-around trap⟧",
                 "<p>⟦Nhân hai FFT có độ dài $N$ nhỏ hơn $l_f+l_g-1$ cho tích chập vòng, không phải tích chập thẳng: phần đuôi cuộn về đầu (chương 11 sẽ gọi là tích chập tuần hoàn). Với $f$ dài 8, $g$ dài 3 và $N=8$, hai kết quả lệch nhau tới {{wrap_err}} ở các số hạng đầu. Đệm số 0 tới $N\\ge l_f+l_g-1$ thì lệch chỉ {{pad_err}}.||"
                 "Multiplying two FFTs of length $N$ smaller than $l_f+l_g-1$ gives a circular convolution, not a linear one: the tail wraps around to the start (chapter 11 calls it cyclic convolution). With $f$ of length 8, $g$ of length 3 and $N=8$, the two results differ by up to {{wrap_err}} in the first terms. Zero-padding to $N\\ge l_f+l_g-1$ leaves a difference of only {{pad_err}}.⟧</p>"),
                ("⟦Ví dụ: trung bình 7 ngày loại chu kỳ tuần||Example: a 7-day mean removes the weekly cycle⟧",
                 "<p>⟦Bracewell nhắc rằng trung bình trượt dùng để làm mượt số liệu khí tượng (tr. 33). Với chuỗi 364 ngày có xu hướng mùa biên độ 3 và chu kỳ tuần biên độ 2, trung bình 7 ngày (đóng vòng) đưa biên độ tuần từ {{wk_before}} xuống {{wk_after}} và giữ biên độ mùa {{season_after}} (lý thuyết {{season_th}}). Hai cách tính, tích chập vòng và FFT, trùng nhau.||"
                 "Bracewell mentions that running means smooth meteorological data (p. 33). For a 364-day series with a seasonal trend of amplitude 3 and a weekly cycle of amplitude 2, a 7-day mean (circular) takes the weekly amplitude from {{wk_before}} to {{wk_after}} and keeps the seasonal amplitude {{season_after}} (theory {{season_th}}). The two computations, circular convolution and FFT, agree.⟧</p>{{fig:weekly}}"),
                ("⟦Thư viện ma trận và tích chập||Matrix packages and convolution⟧",
                 "<p>⟦Trong các gói phần mềm dựa trên phép toán ma trận, tích chập thường được dựng thành tích của một ma trận vuông với một vector cột, và người ta coi thời gian mất vì kém hiệu quả là không đáng kể (tr. 38). Thực hành hiện nay dùng hàm chuyên dụng (<code>convolve</code>, <code>fftconvolve</code>) vì chúng chọn cách tính hợp lý theo độ dài.||"
                 "In computer packages based on matrix operations, convolution is often constructed as the product of a square matrix and a column vector, and the time lost to inefficiency is deemed negligible (p. 38). Current practice uses dedicated functions (<code>convolve</code>, <code>fftconvolve</code>) because they pick a sensible method by length.⟧</p>"),
                ("⟦Tự kiểm tra phần 4||Self-check, part 4⟧",
                 UL(["⟦Tích chập hai dãy độ dài 12 và 5 có bao nhiêu số hạng ở chế độ full và valid?||How many terms does the convolution of sequences of lengths 12 and 5 have in full and valid modes?⟧",
                     "⟦Vì sao nhân hai FFT độ dài $N=8$ của dãy dài 8 và dãy dài 3 cho kết quả sai?||Why does multiplying two length-8 FFTs of a length-8 and a length-3 sequence give a wrong result?⟧",
                     "⟦Với bộ lọc rất ngắn, phương pháp nào thường kinh tế hơn?||With a very short filter, which method is usually cheaper?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: 16 và 8; vì tích chập vòng cuộn đuôi; tính trực tiếp.||Hints: 16 and 8; because circular convolution wraps the tail; the direct method.⟧</p>"),
            ]),
        # ------------------------------------------------------------ PART 5
        dict(
            title="⟦Tự tương quan, tương quan chéo và phổ năng lượng||Autocorrelation, cross correlation and the energy spectrum⟧",
            scr=("⟦Nếu không đảo chiều một thừa số trước khi nhân và lấy tích phân, ta được tương quan chứ không phải tích chập.||If we do not reverse one factor before multiplying and integrating, we get correlation rather than convolution.⟧",
                 "⟦Tương quan đo độ giống nhau khi dịch, nhưng bỏ mất một phần thông tin (pha, chiều thời gian).||Correlation measures similarity under displacement, but discards some information (phase, the arrow of time).⟧",
                 "⟦Tự tương quan, tương quan bậc ba, tương quan chéo và phổ năng lượng, cùng cái giá của chúng.||Autocorrelation, triple correlation, cross correlation and the energy spectrum, and their price.⟧"),
            preview=["⟦Tự tương quan: định nghĩa, ví dụ, cực đại tại gốc||Autocorrelation: definition, examples, maximum at the origin⟧",
                     "⟦Mất pha, tương quan bậc ba, tương quan chéo||Phase loss, triple correlation, cross correlation⟧",
                     "⟦Phổ năng lượng và dãy xung có tự tương quan tốt||The energy spectrum and pulse sequences with good autocorrelation⟧"],
            slides=[
                ("⟦Tự tương quan: định nghĩa||Autocorrelation: definition⟧",
                 "<p>⟦Tự chập của $f$ là $\\int f(u)f(x-u)du$. Nếu trước khi nhân ta không đảo một thừa số thì có tích phân dưới đây, viết là $f\\star f$ (dấu sao năm cánh, \"pentagram\"). Nếu $f$ thực thì $f\\star f$ là hàm chẵn, điều không đúng với tích chập nói chung (Bracewell, tr. 40 đến 41).||"
                 "The self-convolution of $f$ is $\\int f(u)f(x-u)du$. If prior to multiplication we do not reverse one factor we get the integral below, written $f\\star f$ (the five-pointed star, \"pentagram\"). If $f$ is real then $f\\star f$ is an even function, which is not true of convolution in general (pp. 40 to 41).⟧</p>"
                 + F("⟦Tự tương quan||Autocorrelation⟧", r"f\star f(x)=\int_{-\infty}^{\infty}f(u)\,f(u-x)\,du=\int_{-\infty}^{\infty}f(u)\,f(u+x)\,du")),
                ("⟦Chuẩn hóa và cực đại tại gốc||Normalisation and maximum at the origin⟧",
                 "<p>⟦Chia cho giá trị tại gốc ta có $\\gamma(x)$ với $\\gamma(0)=1$. Phụ lục chứng minh tự tương quan không vượt giá trị tại gốc: xét $\\int[f(u)+\\varepsilon f(u+x)]^2du\\ge0$, tam thức bậc hai theo $\\varepsilon$ không có nghiệm thực nên $b^2-4ac<0$, cùng lý luận với bất đẳng thức Schwarz (tr. 41, 48 đến 49). Notebook kiểm trên dãy ngẫu nhiên: tỉ số lớn nhất của các thùy phụ với đỉnh là {{ac_ratio}}.||"
                 "Dividing by the central value gives $\\gamma(x)$ with $\\gamma(0)=1$. The appendix proves that the autocorrelation never exceeds its value at the origin: consider $\\int[f(u)+\\varepsilon f(u+x)]^2du\\ge0$, a quadratic in $\\varepsilon$ with no real root, so $b^2-4ac<0$, the same argument as the Schwarz inequality (pp. 41, 48 to 49). The notebook checks on a random sequence: the largest ratio of a side value to the peak is {{ac_ratio}}.⟧</p>"
                 + F("⟦Tự tương quan chuẩn hóa||Normalised autocorrelation⟧", r"\gamma(x)=\frac{\int f(u)f(u+x)\,du}{\int f(u)^2\,du},\qquad |\gamma(x)|\le\gamma(0)=1")),
                ("⟦Ví dụ 1: $f=1-x$ trên $(0,1)$||Example 1: $f=1-x$ on $(0,1)$⟧",
                 "<p>⟦Với $0<x<1$: $\\int f(u)f(u+x)du=\\tfrac13-\\tfrac x2+\\tfrac{x^3}6$, giá trị tại gốc là $\\tfrac13$, nên $\\gamma(x)=1-\\tfrac32|x|+\\tfrac12|x|^3$ và $\\gamma=0$ khi $|x|>1$. Tại $x=0.25$: {{g_025}}; tại $x=0.5$: {{g_05}}. Diện tích của tử số là {{area_ac}}, đúng bình phương diện tích của $f$ ($1/2$)$^2$ (tr. 41 đến 42).||"
                 "For $0<x<1$: $\\int f(u)f(u+x)du=\\tfrac13-\\tfrac x2+\\tfrac{x^3}6$, the central value is $\\tfrac13$, so $\\gamma(x)=1-\\tfrac32|x|+\\tfrac12|x|^3$ and $\\gamma=0$ for $|x|>1$. At $x=0.25$: {{g_025}}; at $x=0.5$: {{g_05}}. The area of the numerator is {{area_ac}}, exactly the square of the area of $f$, $(1/2)^2$ (pp. 41 to 42).⟧</p>{{fig:autocorr}}"),
                ("⟦Ví dụ 2: $f=e^{-x}H(x)$||Example 2: $f=e^{-x}H(x)$⟧",
                 "<p>⟦Với $f(x)=e^{-x}H(x)$: $\\int f(u)f(u+x)du=\\tfrac12e^{-|x|}$ nên $\\gamma(x)=e^{-|x|}$ (tr. 42). Tại $x=1$: tích phân số cho {{g_exp}}, đúng $e^{-1}$. Tự tương quan là hàm chẵn dù $f$ chỉ nằm ở nửa dương.||"
                 "For $f(x)=e^{-x}H(x)$: $\\int f(u)f(u+x)du=\\tfrac12e^{-|x|}$ so $\\gamma(x)=e^{-|x|}$ (p. 42). At $x=1$: numerical integration gives {{g_exp}}, exactly $e^{-1}$. The autocorrelation is even although $f$ lives only on the positive side.⟧</p>"),
                ("⟦Dữ liệu chạy mãi: đoạn hữu hạn và giới hạn $C(x)$||Data that run on: finite segments and the limit $C(x)$⟧",
                 "<p>⟦Hàm chạy vô hạn thường làm tích phân vô hạn không tồn tại. Cách xử lý là xét một đoạn độ dài $X$ và thay giá trị ngoài đoạn bằng 0, đúng như khi tính trên dữ liệu quan sát hữu hạn. Khi $X$ tăng, $\\gamma$ có thể tiến về giới hạn $C(x)$ (tr. 42 đến 43). Khi biến là thời gian, ta viết bằng trung bình thời gian $\\langle V(t)V(t+\\tau)\\rangle$ (tr. 44).||"
                 "A function that runs on indefinitely often has no infinite integral. The remedy is to take a segment of length $X$ and replace the values outside it by zero, exactly as in a calculation on a finite quantity of observational data. As $X$ increases $\\gamma$ may settle to a limit $C(x)$ (pp. 42 to 43). When the variable is time we write it as the time average $\\langle V(t)V(t+\\tau)\\rangle$ (p. 44).⟧</p>"
                 + F("⟦Giới hạn và trung bình thời gian||The limit and the time average⟧", r"C(x)=\lim_{X\to\infty}\frac{\int_{-X/2}^{X/2}f(u)f(u+x)\,du}{\int_{-X/2}^{X/2}f(u)^2\,du},\qquad \langle V(t)V(t+\tau)\rangle=\lim_{T\to\infty}\frac1T\int_0^{T}V(t)V(t+\tau)\,dt")),
                ("⟦Ba sóng hình sin: pha biến mất||Three sinusoids: the phases vanish⟧",
                 "<p>⟦Với $V=A\\sin(\\alpha t+\\phi)+B\\sin(\\beta t+\\chi)+C\\sin(\\gamma t+\\psi)$, tự tương quan giới hạn là chồng ba cosin cùng tần số nhưng biên độ tương đối khác, không còn dấu vết của pha (tr. 43 đến 45). Số đo: $A,B,C=2,1,0.5$ ở 3, 5, 8 Hz; $C(0.05)$ = {{c_tau}} với cả hai bộ pha khác nhau (lệch tối đa {{phase_diff}}).||"
                 "For $V=A\\sin(\\alpha t+\\phi)+B\\sin(\\beta t+\\chi)+C\\sin(\\gamma t+\\psi)$ the limiting autocorrelation is a superposition of three cosines at the same frequencies with different relative amplitudes and no trace of the phases (pp. 43 to 45). Numbers: $A,B,C=2,1,0.5$ at 3, 5, 8 Hz; $C(0.05)$ = {{c_tau}} for two different sets of phases (largest difference {{phase_diff}}).⟧</p>"
                 + F("⟦Tự tương quan của ba sóng||Autocorrelation of three waves⟧", r"C(t)=\frac{A^2\cos\alpha t+B^2\cos\beta t+C^2\cos\gamma t}{A^2+B^2+C^2}")),
                ("⟦Tự tương quan không khả nghịch||Autocorrelation is not reversible⟧",
                 "<p>⟦Vì pha bị mất, không thể từ tự tương quan quay về hàm gốc: tự tương quan là một mất mát thông tin. Trong giao thoa vô tuyến và nhiễu xạ tia X, quan sát tự tương quan dễ hơn quan sát chính hàm, và người ta dồn nhiều công sức để khôi phục thông tin mất (tr. 45). Từ mọi hàm có cùng tự tương quan, hàm gồm toàn cosin có tính duy nhất riêng.||"
                 "Because the phases are lost, one cannot go back from the autocorrelation to the original function: autocorrelation involves a loss of information. In radio interferometry and X-ray diffraction it is easier to observe the autocorrelation than the function itself, and much ingenuity is spent recovering the lost information (p. 45). Among all functions with the same autocorrelation, the one made of cosines only has a certain uniqueness.⟧</p>"),
                ("⟦Tương quan bậc ba: giữ chiều của thời gian||Triple correlation: keeping the arrow of time⟧",
                 "<p>⟦Tự tương quan không biết chiều thời gian: nhiễu qua bộ lọc RC $e^{-t/RC}H(t)$ thống kê có thể khác khi phát ngược, nhưng tự tương quan không thấy. Tương quan bậc ba $U(x_1,x_2)=\\int f(x)f(x+x_1)f(x+x_2)dx$ thì thấy (tr. 45 đến 46). Bracewell ghi rằng $\\{1,2,3\\}$ và $\\{3,2,1\\}$ cho hai mảng khác nhau. Notebook xác nhận: hai dãy có cùng tự tương quan ({{ac_same}}) nhưng mảng bậc ba khác nhau ({{tc_diff}}); tâm $U(0,0)=\\sum f^3$ = {{tc_center}} và tổng mọi phần tử $(\\sum f)^3$ = {{tc_sum}}.||"
                 "Autocorrelation does not know the arrow of time: noise passed through an RC filter $e^{-t/RC}H(t)$ may be statistically different played backwards, yet autocorrelation cannot see it. The triple correlation $U(x_1,x_2)=\\int f(x)f(x+x_1)f(x+x_2)dx$ can (pp. 45 to 46). Bracewell notes that $\\{1,2,3\\}$ and $\\{3,2,1\\}$ give two different arrays. The notebook confirms: the two sequences have the same autocorrelation ({{ac_same}}) but different triple-correlation arrays ({{tc_diff}}); the centre $U(0,0)=\\sum f^3$ = {{tc_center}} and the sum of all entries $(\\sum f)^3$ = {{tc_sum}}.⟧</p>"
                 + "<p>⟦Mảng của $\\{1,2,3\\}$ (hàng $x_1=-2,\\dots,2$, cột $x_2=-2,\\dots,2$):||The array of $\\{1,2,3\\}$ (rows $x_1=-2,\\dots,2$, columns $x_2=-2,\\dots,2$):⟧</p><pre>{{tc_r0}}\n{{tc_r1}}\n{{tc_r2}}\n{{tc_r3}}\n{{tc_r4}}</pre>"),
                ("⟦Tương quan chéo và ký hiệu sao năm cánh||Cross correlation and the pentagram⟧",
                 "<p>⟦Tương quan chéo của $g$ và $h$ là $g\\star h=\\int g(u-x)h(u)du$: giống tích chập nhưng $g$ chỉ dịch, không đảo. Đọc là \"$g$ quét $h$\". Nó không giao hoán, nhưng $g\\star h(x)=h\\star g(-x)$ (tr. 46). Với hàm phức phải dùng $g^*$, và đặt sai vị trí dấu sao sẽ cho liên hợp của kết quả chuẩn (tr. 41, 47).||"
                 "The cross correlation of $g$ and $h$ is $g\\star h=\\int g(u-x)h(u)du$: like convolution except that $g$ is only displaced, not reversed. Read it as \"$g$ scans $h$\". It is not commutative, but $g\\star h(x)=h\\star g(-x)$ (p. 46). For complex functions use $g^*$, and placing the asterisk wrongly yields the conjugate of the standard version (pp. 41, 47).⟧</p>"
                 + F("⟦Tương quan chéo||Cross correlation⟧", r"g\star h(x)=\int_{-\infty}^{\infty}g(u-x)\,h(u)\,du=h\star g(-x)")
                 + "<p>⟦Notebook kiểm hệ thức với dãy rời rạc: đúng ({{xc_ok}}), và $g\\star h\\ne h\\star g$ nói chung ({{xc_ne}}).||The notebook checks the relation with discrete sequences: it holds ({{xc_ok}}), and $g\\star h\\ne h\\star g$ in general ({{xc_ne}}).⟧</p>"),
                ("⟦Phổ năng lượng||The energy spectrum⟧",
                 "<p>⟦Bình phương môđun của biến đổi, $|F(s)|^2$, là phổ năng lượng. Không có tương ứng một-một với $f$: cần cả pha. Thông tin mất giống hệt thông tin mất khi dùng tự tương quan, và định lý tự tương quan (chương 6) diễn đạt sự tương đương đó (tr. 47). Notebook kiểm bản rời rạc: biến đổi ngược của $|X|^2$ trùng tự tương quan vòng (lệch {{wk_diff}}), và hai tín hiệu khác pha có cùng phổ năng lượng (lệch {{pha_diff}}).||"
                 "The squared modulus of the transform, $|F(s)|^2$, is the energy spectrum. There is no one-to-one relation with $f$: the phase is needed too. The information lost is of exactly the same character as that lost when autocorrelation stands in for the function, and the autocorrelation theorem (chapter 6) expresses this equivalence (p. 47). The notebook checks the discrete version: the inverse transform of $|X|^2$ equals the circular autocorrelation (deviation {{wk_diff}}), and two signals with different phases have the same energy spectrum (deviation {{pha_diff}}).⟧</p>"
                 + F("⟦Phổ năng lượng và tự tương quan||Energy spectrum and autocorrelation⟧", r"f\star f\ \supset\ |F(s)|^2")),
                ("⟦Phổ năng lượng tích lũy và vạch phổ||The cumulative energy spectrum and spectral lines⟧",
                 "<p>⟦Vì $|F|^2$ là mật độ năng lượng theo $s$, một vạch phổ mang năng lượng hữu hạn làm mật độ vô hạn. Ta dùng phổ tích lũy $\\int_0^s|F|^2ds$: mỗi vạch là một bước nhảy hữu hạn (hình 3.12, tr. 47 đến 48). Số đo: tín hiệu gồm sóng 50 Hz biên độ 3 cộng nhiễu, phần năng lượng tích lũy trước 49 Hz là {{cum_before}} và sau 51 Hz là {{cum_after}}: bước nhảy tại vạch 50 Hz là {{cum_jump}} tổng năng lượng.||"
                 "Since $|F|^2$ is energy density per unit $s$, a spectral line carrying finite energy makes the density infinite. We use the cumulative spectrum $\\int_0^s|F|^2ds$: each line is a finite discontinuity (Fig. 3.12, pp. 47 to 48). Numbers: a signal made of a 50 Hz wave of amplitude 3 plus noise has cumulative energy fraction {{cum_before}} below 49 Hz and {{cum_after}} above 51 Hz: the step at the 50 Hz line is {{cum_jump}} of the total energy.⟧</p>"),
                ("⟦Dãy xung có tự tương quan tốt: $\\{1100101\\}$||A pulse sequence with good autocorrelation: $\\{1100101\\}$⟧",
                 "<p>⟦Bài tập 1(j), (k) và tài liệu Pettit (1967) trong thư mục nhắc tới dãy xung có tính tự tương quan tốt. Với $\\{1,1,0,0,1,0,1\\}$, tự tương quan thẳng có đỉnh {{ac_peak}} tại gốc và thùy phụ lớn nhất {{ac_side}}; tự tương quan vòng bằng {{ac_circ}} tại mọi độ dịch khác 0, gần như phẳng. Tính chất này là lý do dãy như vậy dùng cho radar và đồng bộ.||"
                 "Problem 1(j), (k) and Pettit's paper (1967) in the bibliography point at pulse sequences with good autocorrelation properties. For $\\{1,1,0,0,1,0,1\\}$ the linear autocorrelation has peak {{ac_peak}} at the origin and largest side value {{ac_side}}; the circular autocorrelation equals {{ac_circ}} at every nonzero shift, almost flat. This property is why such sequences are used in radar and synchronisation.⟧</p>"
                 + C("info", "⟦Liên hệ chéo||Cross-reference⟧", "<p>⟦Barkat dùng đúng các hàm này cho quá trình ngẫu nhiên: mục 3.3 (tính chất của hàm tương quan, gồm cực đại tại gốc) và mục 3.5 (mật độ phổ công suất). Module 12 ghép hai sách ở điểm này.||Barkat uses exactly these functions for random processes: section 3.3 (properties of correlation functions, including the maximum at the origin) and section 3.5 (power spectral density). Module 12 merges the two books here.⟧</p>")),
            ]),
    ],
    takeaways=[
        "⟦Tích chập có bốn cách nhìn (diện tích, làm mượt, chồng chất, gập) và cư xử như phép nhân: giao hoán, kết hợp, phân phối.||Convolution has four pictures (area, smoothing, superposition, folding) and behaves like multiplication: commutative, associative, distributive.⟧",
        "⟦Với diện tích 1, tích chập nhân diện tích và cộng phương sai; lặp lại nhiều lần tiến về Gauss.||For unit areas, convolution multiplies areas and adds variances; repeated convolution tends to a Gaussian.⟧",
        "⟦Tích chập nối tiếp là nhân đa thức; kiểm bằng tổng và độ dài; đảo bằng chia dãy hoặc bảng nghịch đảo.||The serial product is polynomial multiplication; check it by sum and length; invert it by serial division or the table of inverses.⟧",
        "⟦Tính bằng máy: mã trực tiếp cần $l_fl_g$ phép nhân; FFT phải đệm số 0 để tránh cuộn vòng.||By machine: the direct code needs $l_fl_g$ multiplications; an FFT must be zero-padded to avoid wrap-around.⟧",
        "⟦Tự tương quan có cực đại tại gốc, chẵn với hàm thực, và mất pha; tương quan bậc ba giữ chiều thời gian; phổ năng lượng $|F|^2$ tương đương tự tương quan.||Autocorrelation peaks at the origin, is even for real functions and loses phase; triple correlation keeps the arrow of time; the energy spectrum $|F|^2$ is equivalent to autocorrelation.⟧",
    ],
    history="<p>⟦Chương 3 mở đầu bằng loạt tên gọi của tích chập ở các ngành: Faltung của tiếng Đức, \"composition product\" thích nghi từ tiếng Pháp, tích phân Duhamel, định lý Borel (tr. 24). Việc quy về một khái niệm duy nhất là điều Bracewell muốn khuyến khích khi nói rằng ý thức về \"tính đồng nhất\" của tích chập đang lan rộng.||"
            "Chapter 3 opens with a list of names for convolution in different fields: the German Faltung, \"composition product\" adapted from the French, the Duhamel integral, Borel's theorem (p. 24). Recognising them as one concept is what Bracewell encourages when he says awareness of its oneness is spreading.⟧</p>"
            "<p>⟦Ký hiệu sao năm cánh cho tương quan chéo và cách đọc \"$g$ quét $h$\" là đề xuất của giáo trình (tr. 46). Tương quan bậc ba được nhắc tới cùng tài liệu của Weigelt (1991), và dãy xung có tự tương quan tốt cùng tài liệu của Pettit (1967) (tr. 49).||"
            "The five-pointed-star notation for cross correlation and the reading \"$g$ scans $h$\" are the book's proposal (p. 46). Triple correlation is cited with Weigelt (1991), and pulse sequences with good autocorrelation with Pettit (1967) (p. 49).⟧</p>"
            "<p>⟦Bibliography cũng nêu bài của Bracewell và Roberts (1954) về làm mượt ăng-ten trong thiên văn vô tuyến, một ví dụ cụ thể của tích chập giữa bầu trời và chùm ăng-ten (tr. 49).||The bibliography also cites Bracewell and Roberts (1954) on aerial smoothing in radio astronomy, a concrete example of convolution between the sky and the antenna beam (p. 49).⟧</p>",
    case="<p>⟦<b>Làm mượt số liệu khí tượng.</b> Một chuỗi nhiệt độ ngày (364 ngày) có xu hướng mùa biên độ 3 và chu kỳ tuần biên độ 2. Trung bình trượt 7 ngày là tích chập với $\\frac17\\{1,1,1,1,1,1,1\\}$. Nó đưa thành phần tuần từ {{wk_before}} xuống {{wk_after}} (một điểm không của đáp ứng tần số) mà vẫn giữ {{season_after}} trên {{season_th}} lý thuyết của thành phần mùa. Đây đúng là điều Bracewell mô tả khi nói trung bình tuần của số liệu ngày.||"
          "<b>Smoothing weather data.</b> A daily-temperature series (364 days) has a seasonal trend of amplitude 3 and a weekly cycle of amplitude 2. A 7-day running mean is a convolution with $\\frac17\\{1,1,1,1,1,1,1\\}$. It takes the weekly component from {{wk_before}} to {{wk_after}} (a zero of the frequency response) while keeping {{season_after}} out of the theoretical {{season_th}} of the seasonal component. This is exactly what Bracewell describes when he speaks of weekly means of daily values.⟧</p>"
         "<p>⟦Kết luận chung: chọn độ dài cửa sổ bằng đúng chu kỳ cần loại thì tích chập có điểm không tại chu kỳ đó. Đó là ý nghĩa thực dụng của việc nhìn tích chập trong miền tần số.||General conclusion: choose the window length equal to the period to remove and the convolution has a zero at that period. That is the practical meaning of viewing convolution in the frequency domain.⟧</p>",
    practice=[
        "⟦Mở notebook và chạy cell cài đặt.||Open the notebook and run the setup cell.⟧",
        "⟦Bài 1: kiểm công thức hai hàm mũ cắt cụt, giới hạn tới hạn và hai đuôi bằng tích phân số; thử $\\alpha=0.5,\\beta=3$.||Task 1: check the two-truncated-exponentials formula, the critical limit and the two tails by numerical integration; try $\\alpha=0.5,\\beta=3$.⟧",
        "⟦Bài 2: lặp tích chập xung chữ nhật $n=2,\\dots,8$ lần, vẽ và so với Gauss; xem độ lệch giảm thế nào.||Task 2: repeat the rectangle convolution $n=2,\\dots,8$ times, plot and compare with a Gaussian; watch how the deviation falls.⟧",
        "⟦Bài 3: giải bài tập 1 của Bracewell (a) đến (e) bằng tay rồi kiểm bằng <code>convolve</code> và tổng các số hạng; thử chia dãy ngược lại.||Task 3: do Bracewell's problem 1 (a) to (e) by hand then check with <code>convolve</code> and the sum of terms; try serial division backwards.⟧",
        "⟦Bài 4: thử FFT không đệm số 0 để thấy cuộn vòng, rồi đệm và so sánh.||Task 4: try an FFT without zero-padding to see the wrap-around, then pad and compare.⟧",
        "⟦Bài 5: tính tự tương quan của một dãy tự chọn, thử đổi pha các thành phần và kiểm nó không đổi.||Task 5: compute the autocorrelation of a sequence of your own, change the phases of its components and check it does not change.⟧",
    ],
    pitfalls=[
        "<b>⟦\"Tích chập là nhân từng điểm hai hàm.\"||\"Convolution is pointwise multiplication of two functions.\"⟧</b><p>⟦Tích chập cần $f$ trên cả một khoảng để tính một giá trị $h(x)$. Chỉ trong miền tần số nó mới trở thành phép nhân từng điểm (module 6).||Convolution needs $f$ over a whole range to compute one value $h(x)$. Only in the frequency domain does it become pointwise multiplication (module 6).⟧</p>",
        "<b>⟦\"Tự tương quan và tích chập là một.\"||\"Autocorrelation and convolution are the same.\"⟧</b><p>⟦Khác ở chỗ có đảo chiều hay không. Tự tương quan của hàm thực luôn chẵn ({{g_exp}} cho $e^{-x}H(x)$ tại $x=1$ và cũng tại $-1$), còn tích chập nói chung thì không (tr. 40 đến 41).||They differ in whether one factor is reversed. The autocorrelation of a real function is always even ({{g_exp}} for $e^{-x}H(x)$ at $x=1$ and also at $-1$), whereas convolution generally is not (pp. 40 to 41).⟧</p>",
        "<b>⟦\"Nhân hai FFT luôn cho tích chập thẳng.\"||\"Multiplying two FFTs always gives the linear convolution.\"⟧</b><p>⟦Chỉ khi độ dài $N\\ge l_f+l_g-1$ (đệm số 0). Nếu không có cuộn vòng: lệch {{wrap_err}} trong ví dụ của module.||Only when $N\\ge l_f+l_g-1$ (zero-padding). Otherwise there is wrap-around: a deviation of {{wrap_err}} in this module's example.⟧</p>",
        "<b>⟦\"Từ tự tương quan có thể khôi phục tín hiệu.\"||\"The signal can be recovered from its autocorrelation.\"⟧</b><p>⟦Pha bị mất: hai bộ pha khác nhau cho cùng $C(0.05)$ = {{c_tau}} (lệch {{phase_diff}}). Chỉ thu được biên độ phổ, không có pha (tr. 45).||The phase is lost: two different sets of phases give the same $C(0.05)$ = {{c_tau}} (difference {{phase_diff}}). Only spectral amplitudes are obtained, not phases (p. 45).⟧</p>",
    ],
    refs=[
        "⟦R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chương 3 (tr. 24 đến 50, gồm phụ lục, thư mục và bài tập 1).||R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chapter 3 (pp. 24 to 50, including the appendix, bibliography and problem 1).⟧",
        "⟦M. Barkat, <i>Signal Detection and Estimation</i>, 2nd ed., Artech House, 2005, mục 3.3 và 3.5, chỉ dẫn tới ở phần liên hệ chéo.||M. Barkat, <i>Signal Detection and Estimation</i>, 2nd ed., Artech House, 2005, sections 3.3 and 3.5, cited only in the cross-reference.⟧",
    ],
    quiz=[
        dict(q="⟦Tại $x=1$, diện tích chồng lấn của $\\Pi(u)$ và $e^{-(x-u)}H(x-u)$ (tức $\\Pi*e^{-x}H$) bằng bao nhiêu?||At $x=1$, what is the overlap area of $\\Pi(u)$ and $e^{-(x-u)}H(x-u)$ (i.e. $\\Pi*e^{-x}H$)?⟧",
             opts=["{{ov_x1}}", "0.6321", "0.3679", "0.8647"],
             explain="⟦$\\int_0^{1/2}\\ldots$ cho $e^{-1/2}-e^{-3/2}$ = {{ov_x1}}.||The integral gives $e^{-1/2}-e^{-3/2}$ = {{ov_x1}}.⟧"),
        dict(q="⟦Với $\\alpha=1,\\beta=2$, tích chập $\\alpha E(\\alpha x)*\\beta E(\\beta x)$ tại $x=1$ bằng bao nhiêu?||With $\\alpha=1,\\beta=2$, what is $\\alpha E(\\alpha x)*\\beta E(\\beta x)$ at $x=1$?⟧",
             opts=["{{ex_x1}}", "0.2325", "0.9302", "0.3679"],
             explain="⟦$\\alpha\\beta[e^{-\\alpha x}-e^{-\\beta x}]/(\\beta-\\alpha)$ = $2(e^{-1}-e^{-2})$ = {{ex_x1}}.||$\\alpha\\beta[e^{-\\alpha x}-e^{-\\beta x}]/(\\beta-\\alpha)$ = $2(e^{-1}-e^{-2})$ = {{ex_x1}}.⟧"),
        dict(q="⟦Bộ cộng hưởng tắt dần tới hạn $E(x)*E(x)$ ($\\alpha=1$) tại $x=2$ bằng bao nhiêu?||What is the critically damped $E(x)*E(x)$ ($\\alpha=1$) at $x=2$?⟧",
             opts=["{{crit_x2}}", "0.1353", "0.5413", "0.3679"],
             explain="⟦$xe^{-x}$ tại 2 là $2e^{-2}$ = {{crit_x2}}.||$xe^{-x}$ at 2 is $2e^{-2}$ = {{crit_x2}}.⟧"),
        dict(q="⟦Với $\\alpha=1,\\beta=2$, giá trị của $\\alpha E(-\\alpha x)*\\beta E(\\beta x)$ tại $x=-1$ (bên trái) là bao nhiêu?||With $\\alpha=1,\\beta=2$, what is $\\alpha E(-\\alpha x)*\\beta E(\\beta x)$ at $x=-1$ (the left side)?⟧",
             opts=["{{opp_l1}}", "0.0902", "0.3679", "0.4906"],
             explain="⟦Bên trái suy giảm với hằng số $\\alpha$: $\\frac{\\alpha\\beta}{\\alpha+\\beta}e^{-1}$ = {{opp_l1}}.||The left side decays with constant $\\alpha$: $\\frac{\\alpha\\beta}{\\alpha+\\beta}e^{-1}$ = {{opp_l1}}.⟧"),
        dict(q="⟦Cũng hàm đó tại $x=+1$ (bên phải) bằng bao nhiêu?||What is the same function at $x=+1$ (the right side)?⟧",
             opts=["{{opp_r1}}", "0.2453", "0.1353", "0.0451"],
             explain="⟦Bên phải suy giảm nhanh hơn với $\\beta=2$: $\\frac23e^{-2}$ = {{opp_r1}}.||The right side falls faster with $\\beta=2$: $\\frac23e^{-2}$ = {{opp_r1}}.⟧"),
        dict(q="⟦Giá trị của $\\Pi*\\Pi*\\Pi$ tại $x=0$ là bao nhiêu?||What is $\\Pi*\\Pi*\\Pi$ at $x=0$?⟧",
             opts=["{{b3_0}}", "0.5", "1", "0.6667"],
             explain="⟦Parabol từng khúc $3/4-x^2$ trong $|x|\\le1/2$: tại 0 là {{b3_0}}.||The piecewise parabola $3/4-x^2$ for $|x|\\le1/2$: at 0 it is {{b3_0}}.⟧"),
        dict(q="⟦Giá trị của $\\Pi*\\Pi*\\Pi$ tại $x=1$ là bao nhiêu?||What is $\\Pi*\\Pi*\\Pi$ at $x=1$?⟧",
             opts=["{{b3_1}}", "0.25", "0.0625", "0.375"],
             explain="⟦Nhánh ngoài $(3/2-|x|)^2/2$: tại 1 là $1/8$ = {{b3_1}}.||The outer branch $(3/2-|x|)^2/2$: at 1 it is $1/8$ = {{b3_1}}.⟧"),
        dict(q="⟦Phương sai của $e^{-x}H(x)*\\Pi(x)$ bằng bao nhiêu (phương sai từng hàm: 1 và $1/12$)?||What is the variance of $e^{-x}H(x)*\\Pi(x)$ (variances of the two: 1 and $1/12$)?⟧",
             opts=["{{var_conv}}", "1.1667", "0.0833", "1.5"],
             explain="⟦Phương sai cộng: $1+1/12$ = {{var_conv}}; diện tích vẫn {{area_conv}}.||Variances add: $1+1/12$ = {{var_conv}}; the area stays {{area_conv}}.⟧"),
        dict(q="⟦Tích chập nối tiếp của dãy 7 số hạng và dãy 4 số hạng có bao nhiêu số hạng?||How many terms does the serial product of a 7-term and a 4-term sequence have?⟧",
             opts=["{{len74}}", "11", "28", "3"],
             explain="⟦$7+4-1$ = {{len74}}.||$7+4-1$ = {{len74}}.⟧"),
        dict(q="⟦Tổng chạy của $\\{3,1,4,1,5,9,2,6\\}$ kết thúc ở giá trị nào?||At what value does the running sum of $\\{3,1,4,1,5,9,2,6\\}$ end?⟧",
             opts=["{{run_last}}", "26", "5", "8"],
             explain="⟦3+1+4+1+5+9+2+6 = {{run_last}}; lấy sai phân bằng $\\{1,-1\\}$ trả lại dãy gốc.||3+1+4+1+5+9+2+6 = {{run_last}}; differencing with $\\{1,-1\\}$ returns the original.⟧"),
        dict(q="⟦Giải $\\{1,1\\}*\\{g\\}=\\{1,3,3,1\\}$: $\\{g\\}$ là dãy nào?||Solve $\\{1,1\\}*\\{g\\}=\\{1,3,3,1\\}$: which sequence is $\\{g\\}$?⟧",
             opts=["{{div_g}}", "1 3 1", "2 1 1", "1 2 2 1"],
             explain="⟦$g_0=1$, $g_1=3-1=2$, $g_2=3-2=1$: {{div_g}}; chia đa thức cho cùng đáp số.||$g_0=1$, $g_1=3-1=2$, $g_2=3-2=1$: {{div_g}}; polynomial division gives the same.⟧"),
        dict(q="⟦Dãy nghịch đảo của $\\{1,-a\\}$ là dãy nào?||What is the reciprocal sequence of $\\{1,-a\\}$?⟧",
             opts=["$\\{1,a,a^2,a^3,\\dots\\}$", "$\\{1,-a,a^2,-a^3,\\dots\\}$ ⟦vì hai dấu trừ liên tiếp phải luân phiên||since two consecutive minus signs must alternate⟧",
                   "$\\{1,1/a,1/a^2,\\dots\\}$ ⟦vì nghịch đảo là lấy số mũ ngược||since the reciprocal takes reversed exponents⟧",
                   "$\\{1,a\\}$ ⟦vì chỉ cần đổi dấu số hạng thứ hai||since it is enough to flip the sign of the second term⟧"],
             explain="⟦Bảng 3.1 (tr. 37): $\\{1,-a\\}^{-1}=\\{1,a,a^2,\\dots\\}$; notebook kiểm {{tab_ok}} trên 6 cặp.||Table 3.1 (p. 37): $\\{1,-a\\}^{-1}=\\{1,a,a^2,\\dots\\}$; the notebook checks {{tab_ok}} of 6 pairs.⟧"),
        dict(q="⟦Ma trận nào biểu diễn tích chập nối tiếp với một dãy cố định?||Which matrix represents serial multiplication by a fixed sequence?⟧",
             opts=["⟦Ma trận Toeplitz tam giác dưới||A lower-triangular Toeplitz matrix⟧",
                   "⟦Ma trận đường chéo, vì mỗi số hạng ra chỉ phụ thuộc số hạng vào cùng vị trí||A diagonal matrix, since each output term depends only on the input term at the same position⟧",
                   "⟦Ma trận đối xứng bất kỳ, vì tích chập là phép toán giao hoán||Any symmetric matrix, since convolution is a commutative operation⟧",
                   "⟦Ma trận trực giao, vì tích chập bảo toàn độ dài của mọi vector||An orthogonal matrix, since convolution preserves the length of every vector⟧"],
             explain="⟦Bracewell, tr. 37 đến 38: mỗi hàng là $\\{f\\}$ đảo ngược, dịch một bước; các hàng thay đổi là biến đổi tuyến tính tổng quát.||Bracewell, pp. 37 to 38: each row is $\\{f\\}$ reversed and shifted one step; changing rows give a general linear transformation.⟧"),
        dict(q="⟦Khi hệ có phần tử thay đổi theo thời gian, đáp ứng còn là tích chập không?||When a system has time-varying elements, is the response still a convolution?⟧",
             opts=["⟦Không, và đáp ứng điều hòa với kích thích điều hòa cũng hỏng||No, and harmonic response to harmonic excitation also breaks down⟧",
                   "⟦Vẫn có, chỉ cần dùng đáp ứng xung trung bình trên toàn bộ thời gian quan sát||Yes, one only has to use the impulse response averaged over the whole observation time⟧",
                   "⟦Vẫn có, nhưng phải chập với đáp ứng xung đảo chiều thay vì đáp ứng xung||Yes, but one convolves with the reversed impulse response instead of the impulse response⟧",
                   "⟦Không, nhưng sóng hình sin vào vẫn cho sóng hình sin ra cùng tần số||No, but a sinusoid in still gives a sinusoid out at the same frequency⟧"],
             explain="⟦Bracewell, tr. 39: nếu các phần tử thay đổi thì quan hệ vào-ra không viết được như tích chập, và đáp ứng điều hòa cũng hỏng.||Bracewell, p. 39: if elements vary, the input-output relation cannot be written as a serial product, and harmonic response also breaks down.⟧"),
        dict(q="⟦Tích chập hai dãy độ dài 10 và 4: chế độ <em>valid</em> cho bao nhiêu số hạng?||Convolving sequences of lengths 10 and 4: how many terms does <em>valid</em> mode give?⟧",
             opts=["{{len_valid}}", "10", "13", "4"],
             explain="⟦$10-4+1$ = {{len_valid}} ({{len_full}} ở chế độ full, {{len_same}} ở same).||$10-4+1$ = {{len_valid}} ({{len_full}} in full mode, {{len_same}} in same).⟧"),
        dict(q="⟦Bộ lọc dài $l_g=2000$ trên chuỗi $l_f=10^5$: số phép nhân của cách trực tiếp là bao nhiêu?||A long filter $l_g=2000$ on a series $l_f=10^5$: how many multiplications does the direct method need?⟧",
             opts=["{{ops_direct_long}}", "20,000,000", "2,000,000", "2,000,000,000"],
             explain="⟦$l_fl_g$ = {{ops_direct_long}}, so với cỡ {{ops_fft2}} của FFT.||$l_fl_g$ = {{ops_direct_long}}, versus about {{ops_fft2}} for the FFT.⟧"),
        dict(q="⟦Nhân hai FFT độ dài 8 của $f$ (dài 8) và $g$ (dài 3) cho kết quả lệch so với tích chập thẳng tới mức nào?||Multiplying two length-8 FFTs of $f$ (length 8) and $g$ (length 3) deviates from the linear convolution by how much?⟧",
             opts=["{{wrap_err}}", "0", "{{pad_err}}", "0.001"],
             explain="⟦Cần $N\\ge10$; với $N=8$ đuôi cuộn vòng làm lệch {{wrap_err}}; đệm số 0 thì chỉ {{pad_err}}.||We need $N\\ge10$; with $N=8$ the tail wraps and deviates by {{wrap_err}}; zero-padding leaves only {{pad_err}}.⟧"),
        dict(q="⟦Sau khi trung bình 7 ngày, biên độ chu kỳ tuần (ban đầu {{wk_before}}) gần bằng bao nhiêu?||After the 7-day mean, what is the weekly-cycle amplitude (originally {{wk_before}}), approximately?⟧",
             opts=["{{wk_after}}", "1", "2", "0.5"],
             explain="⟦Trung bình 7 điểm có điểm không tại chu kỳ 7 ngày: biên độ còn {{wk_after}}, trong khi mùa giữ {{season_after}}.||A 7-point mean has a zero at the 7-day period: the amplitude falls to {{wk_after}}, while the seasonal part keeps {{season_after}}.⟧"),
        dict(q="⟦Tự tương quan chuẩn hóa $\\gamma(x)$ của $f=1-x$ trên $(0,1)$ tại $x=0.5$ bằng bao nhiêu?||What is the normalised autocorrelation $\\gamma(x)$ of $f=1-x$ on $(0,1)$ at $x=0.5$?⟧",
             opts=["{{g_05}}", "0.5", "0.6328", "0.1875"],
             explain="⟦$1-\\tfrac32(0.5)+\\tfrac12(0.5)^3$ = {{g_05}}; tại $x=0.25$ là {{g_025}}.||$1-\\tfrac32(0.5)+\\tfrac12(0.5)^3$ = {{g_05}}; at $x=0.25$ it is {{g_025}}.⟧"),
        dict(q="⟦Diện tích của tử số tự tương quan của $f=1-x$ trên $(0,1)$ bằng bao nhiêu?||What is the area of the autocorrelation numerator of $f=1-x$ on $(0,1)$?⟧",
             opts=["{{area_ac}}", "0.5", "0.3333", "1"],
             explain="⟦Bằng bình phương diện tích của $f$: $(1/2)^2$ = {{area_ac}} (tr. 42).||Equal to the square of the area of $f$: $(1/2)^2$ = {{area_ac}} (p. 42).⟧"),
        dict(q="⟦Tự tương quan chuẩn hóa của $e^{-x}H(x)$ tại $x=1$ bằng bao nhiêu?||What is the normalised autocorrelation of $e^{-x}H(x)$ at $x=1$?⟧",
             opts=["{{g_exp}}", "0.1353", "0.6065", "0.5"],
             explain="⟦$\\gamma(x)=e^{-|x|}$ nên $e^{-1}$ = {{g_exp}}.||$\\gamma(x)=e^{-|x|}$ so $e^{-1}$ = {{g_exp}}.⟧"),
        dict(q="⟦Chuẩn hóa tự tương quan của ba sóng ($A,B,C=2,1,0.5$ tại 3, 5, 8 Hz) tại $\\tau=0.05$ s cho $C(\\tau)$ bằng bao nhiêu?||The normalised autocorrelation of the three waves ($A,B,C=2,1,0.5$ at 3, 5, 8 Hz) at $\\tau=0.05$ s gives $C(\\tau)$ equal to what?⟧",
             opts=["{{c_tau}}", "0.5878", "0.7071", "0.8090"],
             explain="⟦$(4\\cos0.3\\pi+\\cos0.5\\pi+0.25\\cos0.8\\pi)/(5.25)$ = {{c_tau}}, và không phụ thuộc pha (lệch {{phase_diff}}).||$(4\\cos0.3\\pi+\\cos0.5\\pi+0.25\\cos0.8\\pi)/(5.25)$ = {{c_tau}}, and independent of the phases (difference {{phase_diff}}).⟧"),
        dict(q="⟦Giá trị trung tâm $U(0,0)$ của tương quan bậc ba của $\\{1,2,3\\}$ là bao nhiêu?||What is the central value $U(0,0)$ of the triple correlation of $\\{1,2,3\\}$?⟧",
             opts=["{{tc_center}}", "6", "14", "216"],
             explain="⟦$\\sum f^3=1+8+27$ = {{tc_center}}; tổng mọi phần tử là $(\\sum f)^3$ = {{tc_sum}}.||$\\sum f^3=1+8+27$ = {{tc_center}}; the sum of all entries is $(\\sum f)^3$ = {{tc_sum}}.⟧"),
        dict(q="⟦Dãy $\\{1,1,0,0,1,0,1\\}$ có tự tương quan vòng bằng bao nhiêu tại mọi độ dịch khác 0?||What is the circular autocorrelation of $\\{1,1,0,0,1,0,1\\}$ at every nonzero shift?⟧",
             opts=["{{ac_circ}}", "1", "0", "4"],
             explain="⟦Đỉnh {{ac_peak}} tại 0 và {{ac_circ}} ở mọi độ dịch khác: gần như phẳng.||The peak is {{ac_peak}} at zero and {{ac_circ}} at every other shift: nearly flat.⟧"),
        dict(q="⟦Tích chập cần phép làm gì mà tự tương quan thì không?||What does convolution do that autocorrelation does not?⟧",
             opts=["⟦Đảo chiều một thừa số trước khi nhân||Reverse one factor before multiplying⟧",
                   "⟦Lấy liên hợp phức của cả hai thừa số trước khi nhân rồi mới lấy tích phân||Take the complex conjugate of both factors before multiplying and then integrate⟧",
                   "⟦Chuẩn hóa để giá trị tại gốc luôn bằng 1 trước khi lấy tích phân||Normalise so the value at the origin is always 1 before integrating⟧",
                   "⟦Cắt hàm ở độ dài hữu hạn $X$ để tích phân vô hạn luôn tồn tại||Truncate the function at a finite length $X$ so the infinite integral always exists⟧"],
             explain="⟦Bracewell, tr. 40: nếu trước khi nhân và lấy tích phân ta không đảo một thừa số thì được tự tương quan.||Bracewell, p. 40: if prior to multiplication and integration we do not reverse one factor we get the autocorrelation.⟧"),
        dict(q="⟦Vì sao tự tương quan của hàm thực là hàm chẵn?||Why is the autocorrelation of a real function even?⟧",
             opts=["⟦Dịch $f$ sang phải hay trái một lượng $x$ cho cùng giá trị tích phân của tích||Displacing $f$ by $x$ to the right or to the left gives the same integral of the product⟧",
                   "⟦Vì mọi hàm thực đều chẵn nên tích chập hai hàm thực luôn chẵn||Because every real function is even, so the convolution of two real functions is always even⟧",
                   "⟦Vì $f$ thực làm biến đổi Fourier của nó chẵn, và chẵn được truyền sang tự tương quan||Because a real $f$ makes its Fourier transform even, and evenness carries over to the autocorrelation⟧",
                   "⟦Vì tích phân từ $-\\infty$ tới $\\infty$ của một hàm thực luôn là một hàm chẵn của cận||Because an integral from $-\\infty$ to $\\infty$ of a real function is always an even function of its limits⟧"],
             explain="⟦Bracewell, tr. 40 đến 41: dịch $f$ so với chính nó một lượng $x$ (không đảo) cho cùng tích phân dù $x$ dương hay âm.||Bracewell, pp. 40 to 41: displacing $f$ relative to itself by $x$ (without reversal) gives the same integral whether $x$ is positive or negative.⟧"),
        dict(q="⟦Hệ thức nào đúng cho tương quan chéo?||Which relation holds for cross correlation?⟧",
             opts=["$g\\star h(x)=h\\star g(-x)$",
                   "$g\\star h(x)=h\\star g(x)$ ⟦vì tương quan chéo giao hoán như tích chập||because cross correlation is commutative like convolution⟧",
                   "$g\\star h(x)=-h\\star g(x)$ ⟦vì đổi vai trò làm đổi dấu kết quả||because swapping the roles flips the sign of the result⟧",
                   "$g\\star h(x)=g*h(-x)$ ⟦vì tương quan chéo bằng tích chập đảo biến||because cross correlation equals convolution with the variable reversed⟧"],
             explain="⟦Bracewell, tr. 46: $g\\star h=h\\star g(-x)$; nó không giao hoán. Notebook kiểm: {{xc_ok}}.||Bracewell, p. 46: $g\\star h=h\\star g(-x)$; it is not commutative. The notebook checks: {{xc_ok}}.⟧"),
        dict(q="⟦Vì sao Bracewell đưa ra tương quan bậc ba?||Why does Bracewell introduce the triple correlation?⟧",
             opts=["⟦Nó phân biệt được chiều của thời gian mà tự tương quan bỏ mất||It distinguishes the direction of time that autocorrelation discards⟧",
                   "⟦Nó tính nhanh hơn tự tương quan vì chỉ cần một biến dịch thay vì hai||It is faster to compute than autocorrelation since it needs one displacement instead of two⟧",
                   "⟦Nó luôn là hàm chẵn theo cả hai biến nên chứa nhiều thông tin đối xứng hơn||It is always even in both variables, so it carries more information about symmetry⟧",
                   "⟦Nó cho phổ năng lượng chính xác hơn khi có nhiễu cộng vào dữ liệu||It gives a more accurate energy spectrum when noise is added to the data⟧"],
             explain="⟦Bracewell, tr. 45 đến 46: tự tương quan không cho biết mũi tên thời gian, tương quan bậc ba thì có; $\\{1,2,3\\}$ và $\\{3,2,1\\}$ cho cùng tự tương quan ({{ac_same}}) nhưng hai mảng bậc ba khác nhau.||Bracewell, pp. 45 to 46: autocorrelation tells nothing about the arrow of time, the triple correlation does; $\\{1,2,3\\}$ and $\\{3,2,1\\}$ share an autocorrelation ({{ac_same}}) but have different triple-correlation arrays.⟧"),
        dict(q="⟦Phổ năng lượng của $f(x)$ là gì và nó bỏ mất thông tin nào?||What is the energy spectrum of $f(x)$ and what information does it lose?⟧",
             opts=["$|F(s)|^2$, ⟦bỏ mất pha||$|F(s)|^2$, it loses the phase⟧",
                   "$|F(s)|$ ⟦chia cho độ dài quan sát, và bỏ mất giá trị tại tần số 0||$|F(s)|$ divided by the observation length, and it loses the value at zero frequency⟧",
                   "$F(s)^2$ ⟦không lấy môđun, và bỏ mất phần thực của biến đổi||$F(s)^2$ without the modulus, and it loses the real part of the transform⟧",
                   "$\\int|f|^2dx$ ⟦một con số duy nhất, và bỏ mất mọi thông tin về tần số||$\\int|f|^2dx$, a single number, and it loses all frequency information⟧"],
             explain="⟦Bracewell, tr. 47: phổ năng lượng là $|F(s)|^2$; cần cả pha mới dựng lại $f$. Notebook: hai tín hiệu khác pha có cùng phổ (lệch {{pha_diff}}).||Bracewell, p. 47: the energy spectrum is $|F(s)|^2$; the phase is needed to reconstitute $f$. Notebook: two signals with different phases share the spectrum (deviation {{pha_diff}}).⟧"),
        dict(q="⟦Phổ năng lượng tích lũy giúp biểu diễn vạch phổ như thế nào?||How does the cumulative energy spectrum represent a spectral line?⟧",
             opts=["⟦Là một bước nhảy hữu hạn||As a finite step⟧",
                   "⟦Là một đỉnh vô hạn cao nhưng có diện tích bằng 0 dưới đường tích lũy||As an infinitely tall peak with zero area under the cumulative curve⟧",
                   "⟦Là một đoạn dốc đều kéo dài trên cả dải tần số quanh vạch phổ đó||As a uniformly sloped segment extending over the whole frequency band around that line⟧",
                   "⟦Là một điểm không liên tục kiểu vô hạn mà không thể biểu diễn được||As an infinite discontinuity that cannot be represented at all⟧"],
             explain="⟦Bracewell, tr. 48: vạch phổ xuất hiện như gián đoạn hữu hạn trong phổ tích lũy; số đo: bước nhảy {{cum_jump}} tại 50 Hz.||Bracewell, p. 48: spectral lines appear as finite discontinuities in the cumulative energy spectrum; measured step {{cum_jump}} at 50 Hz.⟧"),
        dict(q="⟦Chương nào của Barkat dùng tự tương quan và phổ công suất cho quá trình ngẫu nhiên (ghép ở module 12)?||Which chapter of Barkat uses autocorrelation and the power spectrum for random processes (merged in module 12)?⟧",
             opts=["⟦Chương 3||Chapter 3⟧",
                   "⟦Chương 5, vì tự tương quan xuất hiện đầu tiên trong lý thuyết quyết định thống kê||Chapter 5, since autocorrelation first appears in statistical decision theory⟧",
                   "⟦Chương 6, vì ước lượng tham số cần tự tương quan của tham số chưa biết||Chapter 6, since parameter estimation needs the autocorrelation of the unknown parameter⟧",
                   "⟦Chương 12, vì phát hiện CFAR phân tán dựa trên tự tương quan của các ô||Chapter 12, since distributed CFAR detection rests on the autocorrelation of the cells⟧"],
             explain="⟦Barkat: mục 3.3 (tính chất hàm tương quan) và 3.5 (mật độ phổ công suất) nằm ở chương 3, ghép với Bracewell chương 17.||Barkat: section 3.3 (properties of correlation functions) and 3.5 (power spectral density) are in chapter 3, merged with Bracewell chapter 17.⟧"),
    ],
    nb=[
        ("md", """## 1. ⟦Định nghĩa, các cách nhìn và đại số||Definition, pictures and algebra⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Các công thức tích chập trong chương (hai hàm mũ cắt cụt, giới hạn tới hạn, hai đuôi ngược chiều) có đúng không, và ba tính chất đại số có đúng cho dãy số không? Ta so tích phân số với công thức đóng, và các tính chất bằng tính trên dãy ngẫu nhiên.||Are the chapter's convolution formulas (two truncated exponentials, the critical limit, the opposed tails) correct, and do the three algebraic properties hold for sequences? We compare numerical integrals with closed forms, and check the properties on random sequences.⟧"""),
        ("code", r'''from scipy import integrate
trap = getattr(np, "trapezoid", None) or np.trapz

# ⟦Tích chập αE(αx) * βE(βx) tại x > 0: tích phân số so với công thức||αE(αx) * βE(βx) at x > 0: numerical integral versus the formula⟧
def exp_conv(al, be, x):
    return integrate.quad(lambda u: al*np.exp(-al*u)*be*np.exp(-be*(x - u)), 0, x)[0]
def exp_formula(al, be, x):
    return al*be*(np.exp(-al*x) - np.exp(-be*x))/(be - al)
assert abs(exp_conv(1, 2, 1) - exp_formula(1, 2, 1)) < 1e-12 and abs(exp_conv(0.5, 3, 2) - exp_formula(0.5, 3, 2)) < 1e-12
report("ex_x1", exp_formula(1, 2, 1), ".4f")

# ⟦Giới hạn tới hạn β → α: α²·x·e^{−αx}||Critical limit β → α: α²·x·e^{−αx}⟧
assert abs(exp_conv(1, 1, 2) - 1*2*np.exp(-2)) < 1e-12 and abs(exp_formula(1, 1.000001, 2) - 2*np.exp(-2)) < 1e-5
report("crit_x2", 2*np.exp(-2), ".4f")

# ⟦Hai đuôi ngược chiều: αE(−αx) * βE(βx)||Opposed tails: αE(−αx) * βE(βx)⟧
def opp_num(al, be, x):
    hi = min(0.0, x)
    return integrate.quad(lambda u: al*np.exp(al*u)*be*np.exp(-be*(x - u)), -60, hi)[0]
def opp_formula(al, be, x):
    return al*be/(al + be)*(np.exp(al*x) if x < 0 else np.exp(-be*x))
for xv in (-1.0, 1.0):
    assert abs(opp_num(1, 2, xv) - opp_formula(1, 2, xv)) < 1e-9
report("opp_l1", opp_formula(1, 2, -1.0), ".4f"); report("opp_r1", opp_formula(1, 2, 1.0), ".4f")

# ⟦Cách nhìn 1: diện tích chồng lấn của Π và e^{−(x−u)}H(x−u) tại x = 1||View 1: overlap area of Π and e^{−(x−u)}H(x−u) at x = 1⟧
ov = integrate.quad(lambda u: np.exp(-(1 - u)), -0.5, 0.5)[0]
assert abs(ov - (np.exp(-0.5) - np.exp(-1.5))) < 1e-12
report("ov_x1", ov, ".4f")

# ⟦Cách nhìn 2: làm mượt giảm tổng biến thiên||View 2: smoothing lowers the total variation⟧
sq = np.sign(np.sin(np.arange(60)**2 + 1.0))
sm = np.convolve(sq, np.ones(5)/5, "valid")
tv = lambda z: np.sum(np.abs(np.diff(z)))
assert tv(sm) <= tv(sq)
report("tv_f", tv(sq), ".1f"); report("tv_h", tv(sm), ".1f")

# ⟦Ba tính chất đại số||Three algebraic properties⟧
rg = np.random.default_rng(5)
a_, b_, c_ = rg.standard_normal(9), rg.standard_normal(7), rg.standard_normal(5)
p1 = np.allclose(np.convolve(a_, b_), np.convolve(b_, a_))
p2 = np.allclose(np.convolve(a_, np.convolve(b_, c_)), np.convolve(np.convolve(a_, b_), c_))
p3 = np.allclose(np.convolve(a_, b_ + np.pad(c_, (0, 2))), np.convolve(a_, b_) + np.convolve(a_, np.pad(c_, (0, 2))))
assert p1 and p2 and p3
report("props_ok", int(p1) + int(p2) + int(p3), "d")'''),
        ("code", r'''xs = np.linspace(-1, 6, 701)
plt.figure(figsize=(7, 3.3))
for al, be, c in ((1, 2, "tab:blue"), (1, 4, "tab:orange")):
    plt.plot(xs[xs >= 0], exp_formula(al, be, xs[xs >= 0]), color=c, label=f"α={al}, β={be}")
plt.plot(xs[xs >= 0], xs[xs >= 0]*np.exp(-xs[xs >= 0]), "k--", label=("⟦giới hạn tới hạn||critical limit⟧"))
plt.xlabel("x"); plt.legend(); plt.tight_layout(); plt.show()''', dict(fig="exp_conv", cap="⟦Hình 1. Tích chập của hai hàm mũ cắt cụt: hiệu hai hàm mũ (đường màu) tăng rồi giảm; khi β tiến về α (đường đứt) thành x·e^{−x}.||Figure 1. The convolution of two truncated exponentials: a difference of two exponentials (coloured curves) rising then falling; as β approaches α (dashed) it becomes x·e^{−x}.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Tại $x=1$: $\\Pi*e^{-x}H$ cho {{ov_x1}}, hai hàm mũ cắt cụt ($\\alpha=1,\\beta=2$) cho {{ex_x1}}, bộ cộng hưởng tới hạn tại $x=2$ cho {{crit_x2}}, hai đuôi ngược chiều cho {{opp_l1}} ở $x=-1$ và {{opp_r1}} ở $x=+1$ (bên phải rơi nhanh hơn). Làm mượt bằng trung bình 5 điểm giảm tổng biến thiên từ {{tv_f}} xuống {{tv_h}}, và {{props_ok}} trên 3 tính chất đại số đúng.||At $x=1$: $\\Pi*e^{-x}H$ gives {{ov_x1}}, two truncated exponentials ($\\alpha=1,\\beta=2$) give {{ex_x1}}, the critical resonator at $x=2$ gives {{crit_x2}}, the opposed tails give {{opp_l1}} at $x=-1$ and {{opp_r1}} at $x=+1$ (the right side falls faster). A 5-point running mean lowers the total variation from {{tv_f}} to {{tv_h}}, and {{props_ok}} of 3 algebraic properties hold.⟧"""),
        ("md", """## 2. ⟦Lặp tích chập và các quy tắc diện tích, phương sai||Repeated convolution and the area and variance rules⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Tích chập của các hàm diện tích 1 giữ diện tích, cộng phương sai, và lặp nhiều lần tiến về Gauss như thế nào? Ta lặp tích chập trên lưới mịn và so với công thức đóng (spline bậc hai) và với Gauss.||How do convolutions of unit-area functions keep the area, add variances, and tend to a Gaussian when repeated? We repeat the convolution on a fine grid and compare with the closed form (quadratic spline) and with a Gaussian.⟧"""),
        ("code", r'''dxg = 0.001
cell = np.ones(1000)                                             # ⟦Π trên lưới: 1000 ô rộng 0.001||Π on a grid: 1000 cells of width 0.001⟧
def repeated(n):
    z = cell.copy()
    for _ in range(n - 1):
        z = np.convolve(z, cell)*dxg
    return z
def value_at(z, x):                                              # ⟦nội suy tại x (tâm lưới ở giữa mảng)||interpolate at x (grid centre in the middle of the array)⟧
    xs_ = (np.arange(len(z)) - (len(z) - 1)/2)*dxg
    return np.interp(x, xs_, z)
b3 = repeated(3)
spline = lambda x: 0.75 - x**2 if abs(x) <= 0.5 else (1.5 - abs(x))**2/2
assert abs(value_at(b3, 0) - 0.75) < 2e-3 and abs(value_at(b3, 1) - 0.125) < 2e-3
assert abs(value_at(b3, 0.3) - spline(0.3)) < 2e-3
report("b3_0", value_at(b3, 0), ".3f"); report("b3_1", value_at(b3, 1), ".3f")

# ⟦Diện tích và phương sai của e^{−x}H(x) * Π||Area and variance of e^{−x}H(x) * Π⟧
xg = np.arange(0, 40, 0.002); fe = np.exp(-xg)
gp = np.ones(500)
conv = np.convolve(fe, gp)*0.002
xc = (np.arange(len(conv)) - 250)*0.002 + 0.001
area_c = trap(conv, xc); mean_c = trap(xc*conv, xc)/area_c
var_c = trap((xc - mean_c)**2*conv, xc)/area_c
assert abs(area_c - 1) < 5e-3 and abs(var_c - (1 + 1/12)) < 5e-3
report("area_conv", area_c, ".2f"); report("var_conv", var_c, ".4f")

# ⟦Tiến về Gauss: độ lệch tối đa với Gauss cùng phương sai||Tending to a Gaussian: largest deviation from a Gaussian of equal variance⟧
devs = {}
for n in (4, 8):
    z = repeated(n); xs_ = (np.arange(len(z)) - (len(z) - 1)/2)*dxg
    var = n/12.0; g = np.exp(-xs_**2/(2*var))/np.sqrt(2*np.pi*var)
    assert abs(trap(z, xs_) - 1) < 1e-3
    devs[n] = np.max(np.abs(z - g))
report("gauss_dev4", devs[4], ".4f"); report("gauss_dev8", devs[8], ".4f")'''),
        ("code", r'''plt.figure(figsize=(7, 3.3))
for n, c in ((1, "gray"), (2, "tab:green"), (3, "tab:blue"), (4, "tab:red")):
    z = repeated(n); xs_ = (np.arange(len(z)) - (len(z) - 1)/2)*dxg
    plt.plot(xs_, z, color=c, label=f"n = {n}")
var = 4/12.0; xs_ = np.linspace(-2.5, 2.5, 1000)
plt.plot(xs_, np.exp(-xs_**2/(2*var))/np.sqrt(2*np.pi*var), "k--", lw=0.8, label=("⟦Gauss (n=4)||Gaussian (n=4)⟧"))
plt.xlim(-2.5, 2.5); plt.xlabel("x"); plt.legend(); plt.tight_layout(); plt.show()''', dict(fig="pi_repeat", cap="⟦Hình 2. Lặp tích chập của xung chữ nhật: xung, tam giác, parabol từng khúc, rồi n = 4 gần trùng đường Gauss cùng phương sai (nét đứt).||Figure 2. Repeated convolution of the rectangle: the pulse, the triangle, the piecewise parabola, then n = 4 nearly coincides with the Gaussian of equal variance (dashed).⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Lặp ba lần, $\\Pi*\\Pi*\\Pi$ cho {{b3_0}} tại 0 và {{b3_1}} tại 1, khớp spline bậc hai $3/4-x^2$ và $1/8$. $e^{-x}H(x)*\\Pi$ giữ diện tích {{area_conv}} và có phương sai {{var_conv}} $=1+1/12$. Độ lệch tối đa so với Gauss cùng phương sai là {{gauss_dev4}} khi $n=4$ và chỉ {{gauss_dev8}} khi $n=8$: lặp tích chập tiến rất nhanh về Gauss.||Three repetitions, $\\Pi*\\Pi*\\Pi$, give {{b3_0}} at 0 and {{b3_1}} at 1, matching the quadratic spline $3/4-x^2$ and $1/8$. $e^{-x}H(x)*\\Pi$ keeps area {{area_conv}} and has variance {{var_conv}} $=1+1/12$. The largest deviation from the equal-variance Gaussian is {{gauss_dev4}} for $n=4$ and only {{gauss_dev8}} for $n=8$: repeated convolution approaches a Gaussian very quickly.⟧"""),
        ("md", """## 3. ⟦Tích chập nối tiếp: nhân đa thức, chia dãy, bảng nghịch đảo, ma trận||Serial products: polynomial multiplication, division, the table of inverses, matrices⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Tích chập nối tiếp có trùng nhân đa thức, tổng chạy và sai phân có nghịch đảo nhau không, chia dãy có tìm lại thừa số, bảng 3.1 có đúng và ma trận Toeplitz có tái tạo tích chập không? Mỗi điều được kiểm bằng hai cách.||Does the serial product coincide with polynomial multiplication, are running sums and differences inverses, does serial division recover the factor, is Table 3.1 correct and does the Toeplitz matrix reproduce the convolution? Each is checked two ways.⟧"""),
        ("code", r'''from scipy.linalg import toeplitz

# ⟦Nhân đa thức = tích chập nối tiếp||Polynomial multiplication = serial product⟧
pa, pb = np.array([2, 2, 3, 3, 4]), np.array([1, 1, 2])
assert np.array_equal(np.polymul(pa, pb), np.convolve(pa, pb))
report("len74", len(np.convolve(np.arange(1, 8), np.arange(1, 5))), "d")

# ⟦Tổng chạy và sai phân||Running sums and differences⟧
d0 = np.array([3, 1, 4, 1, 5, 9, 2, 6])
S = np.cumsum(d0)
diff_back = np.convolve(S, [1, -1])[:len(d0)]
assert np.array_equal(diff_back, d0) and np.array_equal(np.convolve(np.ones(len(d0)), d0)[:len(d0)], S)
report("run_last", S[-1], "d")

# ⟦Dãy nghịch đảo: {1,2,3,4,...}*{1,-2,1} và {1,-1}*{1,-1}||Reciprocal sequences: {1,2,3,4,...}*{1,-2,1} and {1,-1}*{1,-1}⟧
r1 = np.convolve(np.arange(1, 11), [1, -2, 1])[:10]
r2 = np.convolve([1, -1], [1, -1])
recip_ok = int(np.array_equal(r1, [1] + [0]*9)) + int(np.array_equal(r2, [1, -2, 1]))
assert recip_ok == 2
report("recip_ok", recip_ok, "d")

# ⟦Chia dãy: {1,1}*{g} = {1,3,3,1}. Cách A: đệ quy của Bracewell; cách B: chia đa thức||Serial division: {1,1}*{g} = {1,3,3,1}. Method A: Bracewell's recursion; method B: polynomial division⟧
f_, h_ = [1, 1], [1, 3, 3, 1]
g_ = []
for k in range(len(h_) - len(f_) + 1):
    g_.append((h_[k] - sum(f_[j]*g_[k - j] for j in range(1, min(k, len(f_) - 1) + 1)))/f_[0])
q_, r_ = np.polydiv(h_, f_)
assert np.allclose(g_, q_) and np.allclose(r_, 0)
report("div_g", " ".join(str(int(z)) for z in g_), "s")

# ⟦Bảng 3.1: kiểm sáu cặp (chỉ N số hạng đầu, vì dãy nghịch đảo vô hạn)||Table 3.1: check six pairs (first N terms only, as the inverses are infinite)⟧
Nn = 12; nnn = np.arange(Nn); a_t = 0.5
pairs = [([1, 1], (-1.0)**nnn), ([1, -1], np.ones(Nn)), ([1, 0, 1], np.array([1, 0, -1, 0]*3, float)),
         ([1, 2, 1], (-1.0)**nnn*(nnn + 1)), ([1, -a_t], a_t**nnn), (np.convolve([1, -a_t], [1, -a_t]), (nnn + 1)*a_t**nnn)]
tab_ok = sum(bool(np.allclose(np.convolve(f_t, g_t)[:Nn], [1] + [0]*(Nn - 1))) for f_t, g_t in pairs)
assert tab_ok == 6
report("tab_ok", tab_ok, "d")

# ⟦Dạng ma trận: ma trận Toeplitz tam giác dưới nhân vector||Matrix form: lower-triangular Toeplitz matrix times a vector⟧
ff, gg = np.array([2, 2, 3, 3, 4.0]), np.array([1, 1, 2.0])
L_ = len(ff) + len(gg) - 1
T = toeplitz(np.r_[ff, np.zeros(L_ - len(ff))], np.r_[ff[0], np.zeros(L_ - 1)])
toep = np.allclose(T @ np.r_[gg, np.zeros(L_ - len(gg))], np.convolve(ff, gg))
assert toep
report("toep_ok", "yes" if toep else "no", "s")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Nhân đa thức và <code>convolve</code> trùng nhau; dãy 7 chập dãy 4 cho {{len74}} số hạng. Tổng chạy của $\\{3,1,4,1,5,9,2,6\\}$ kết thúc ở {{run_last}} và lấy sai phân trả lại dãy gốc. {{recip_ok}} trên 2 cặp nghịch đảo đúng. Chia dãy cho $\\{g\\}$ = ({{div_g}}) bằng cả đệ quy và chia đa thức. Bảng 3.1: {{tab_ok}} trên 6 cặp đúng. Ma trận Toeplitz tái tạo tích chập: {{toep_ok}}.||Polynomial multiplication and <code>convolve</code> agree; a 7-term with a 4-term sequence gives {{len74}} terms. The running sum of $\\{3,1,4,1,5,9,2,6\\}$ ends at {{run_last}} and taking differences returns the original. {{recip_ok}} of 2 reciprocal pairs hold. Serial division gives $\\{g\\}$ = ({{div_g}}) by both the recursion and polynomial division. Table 3.1: {{tab_ok}} of 6 pairs hold. The Toeplitz matrix reproduces the convolution: {{toep_ok}}.⟧"""),
        ("md", """## 4. ⟦Tích chập bằng máy tính||Convolution by computer⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Đoạn mã trực tiếp của Bracewell có đúng không, các chế độ độ dài là gì, khi nào FFT cuộn vòng, và trung bình 7 ngày làm gì với chu kỳ tuần? Ta so mã tay với <code>convolve</code>, đếm phép nhân, và so tích chập vòng với FFT.||Is Bracewell's direct code correct, what are the length modes, when does the FFT wrap around, and what does a 7-day mean do to a weekly cycle? We compare the hand code with <code>convolve</code>, count multiplications, and compare circular convolution with the FFT.⟧"""),
        ("code", r'''import math

def direct_conv(f, g):
    """⟦Dịch từ đoạn mã của Bracewell (tr. 40)||Translated from Bracewell's code (p. 40)⟧"""
    lf, lg = len(f), len(g); lh = lf + lg - 1
    h = np.zeros(lh)
    for i in range(lh):
        for j in range(max(i - lg + 1, 0), min(lf - 1, i) + 1):
            h[i] += f[j]*g[i - j]
    return h

rgc = np.random.default_rng(3)
cd = 0.0
for la, lb in ((200, 37), (5, 5)):
    fa, gb = rgc.standard_normal(la), rgc.standard_normal(lb)
    cd = max(cd, np.max(np.abs(direct_conv(fa, gb) - np.convolve(fa, gb))))
assert cd < 1e-12
report("code_diff", cd, ".1e")

x10, x4 = np.arange(10.0), np.arange(4.0)
report("len_full", len(np.convolve(x10, x4, "full")), "d"); report("len_same", len(np.convolve(x10, x4, "same")), "d")
report("len_valid", len(np.convolve(x10, x4, "valid")), "d")

# ⟦Đếm phép nhân (ước lượng bậc độ lớn)||Counting multiplications (order-of-magnitude estimate)⟧
def next_pow2(n): return 1 << (n - 1).bit_length()
lf = 10**5
for lg, tag in ((32, "short"), (2000, "long")):
    N_ = next_pow2(lf + lg - 1)
    report(f"ops_direct_{tag}", lf*lg, ",.0f")
    report("ops_fft" if tag == "short" else "ops_fft2", 3*N_*math.log2(N_), ",.0f")

# ⟦Bẫy cuộn vòng||The wrap-around trap⟧
fw, gw = rgc.standard_normal(8), rgc.standard_normal(3)
lin = np.convolve(fw, gw)
circ = np.fft.ifft(np.fft.fft(fw, 8)*np.fft.fft(gw, 8)).real
wrap = np.max(np.abs(circ - lin[:8]))                            # ⟦so với 8 số hạng đầu của tích chập thẳng||against the first 8 terms of the linear convolution⟧
padded = np.fft.ifft(np.fft.fft(fw, 16)*np.fft.fft(gw, 16)).real[:10]
pad = np.max(np.abs(padded - lin))
assert wrap > 0.1 and pad < 1e-12
report("wrap_err", wrap, ".2f"); report("pad_err", pad, ".1e")

# ⟦Trung bình 7 ngày trên chuỗi 364 ngày (đóng vòng): tích chập vòng so với FFT||7-day mean on a 364-day series (circular): circular convolution versus FFT⟧
dd = np.arange(364)
temp = 20 + 3*np.sin(2*np.pi*dd/364) + 2*np.sin(2*np.pi*dd/7)
smooth_c = np.convolve(np.pad(temp, (3, 3), mode="wrap"), np.ones(7)/7, "valid")
hker = np.zeros(364); hker[[364 - 3, 364 - 2, 364 - 1, 0, 1, 2, 3]] = 1/7
smooth_f = np.fft.ifft(np.fft.fft(temp)*np.fft.fft(hker)).real
assert np.allclose(smooth_c, smooth_f)
A_b, A_a = amplitude_spectrum(temp), amplitude_spectrum(smooth_c)
season_th = 3*abs(np.sin(7*np.pi/364)/(7*np.sin(np.pi/364)))
assert abs(A_a[1] - season_th) < 1e-9 and A_a[52] < 1e-9
report("wk_before", A_b[52], ".2f"); report("wk_after", A_a[52], ".2f")
report("season_after", A_a[1], ".4f"); report("season_th", season_th, ".4f")'''),
        ("code", r'''plt.figure(figsize=(8, 3.3))
plt.plot(dd[:100], temp[:100], color="lightgray", label=("⟦chuỗi gốc||original series⟧"))
plt.plot(dd[:100], smooth_c[:100], "tab:red", label=("⟦trung bình 7 ngày||7-day mean⟧"))
plt.xlabel(("⟦ngày||day⟧")); plt.legend(); plt.tight_layout(); plt.show()''', dict(fig="weekly", cap="⟦Hình 3. Chuỗi nhiệt độ ngày có chu kỳ tuần (xám) và sau trung bình 7 ngày (đỏ): chu kỳ tuần biến mất, xu hướng mùa còn nguyên.||Figure 3. A daily-temperature series with a weekly cycle (gray) and after the 7-day mean (red): the weekly cycle vanishes and the seasonal trend remains.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Mã tay của Bracewell trùng <code>convolve</code> (lệch {{code_diff}}). Với hai dãy 10 và 4: {{len_full}}, {{len_same}}, {{len_valid}} số hạng ở ba chế độ full, same, valid. Số phép nhân: {{ops_direct_short}} so với cỡ {{ops_fft}} của FFT cho bộ lọc ngắn, và {{ops_direct_long}} so với {{ops_fft2}} cho bộ lọc dài. FFT không đệm số 0 lệch {{wrap_err}} (cuộn vòng), đệm rồi lệch chỉ {{pad_err}}. Trung bình 7 ngày đưa biên độ tuần từ {{wk_before}} xuống {{wk_after}} và giữ mùa ở {{season_after}} (lý thuyết {{season_th}}).||Bracewell's hand code matches <code>convolve</code> (deviation {{code_diff}}). For sequences of 10 and 4: {{len_full}}, {{len_same}}, {{len_valid}} terms in full, same, valid modes. Multiplication counts: {{ops_direct_short}} versus about {{ops_fft}} for the FFT with a short filter, and {{ops_direct_long}} versus {{ops_fft2}} with a long one. An FFT without zero-padding deviates by {{wrap_err}} (wrap-around), padded it deviates by only {{pad_err}}. The 7-day mean takes the weekly amplitude from {{wk_before}} to {{wk_after}} and keeps the season at {{season_after}} (theory {{season_th}}).⟧"""),
        ("md", """## 5. ⟦Tự tương quan, tương quan chéo, bậc ba và phổ năng lượng||Autocorrelation, cross correlation, triple correlation and the energy spectrum⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Các công thức tự tương quan trong chương có đúng không, pha có thật sự bị mất, tương quan bậc ba có phân biệt chiều thời gian, và phổ năng lượng có tương đương tự tương quan? Ta so tích phân số với công thức, và tính trực tiếp với tính qua FFT.||Are the chapter's autocorrelation formulas correct, is the phase really lost, does the triple correlation tell the direction of time, and is the energy spectrum equivalent to the autocorrelation? We compare numerical integrals with formulas, and direct computation with the FFT route.⟧"""),
        ("code", r'''def autocorr_tri(x):                                             # ⟦f = 1 − u trên (0, 1): tích phân số||f = 1 − u on (0, 1): numerical integral⟧
    x = abs(x)
    return integrate.quad(lambda u: (1 - u)*(1 - u - x), 0, 1 - x)[0] if x < 1 else 0.0
g_formula = lambda x: 1 - 1.5*abs(x) + 0.5*abs(x)**3
for xv in (0.0, 0.25, 0.5, 0.9):
    assert abs(autocorr_tri(xv)/autocorr_tri(0) - g_formula(xv)) < 1e-12
area_num = integrate.quad(autocorr_tri, -1, 1, points=[0])[0]
assert abs(area_num - 0.25) < 1e-9
report("g_025", g_formula(0.25), ".4f"); report("g_05", g_formula(0.5), ".4f"); report("area_ac", area_num, ".4f")

num = integrate.quad(lambda u: np.exp(-u)*np.exp(-(u + 1.0)), 0, np.inf)[0]     # ⟦e^{−x}H(x): γ(1)||e^{−x}H(x): γ(1)⟧
assert abs(num/0.5 - np.exp(-1)) < 1e-12
report("g_exp", num/0.5, ".4f")

# ⟦Cực đại tại gốc, trên dãy xác định||Maximum at the origin, on a deterministic sequence⟧
sig = np.sin(np.arange(200)**1.3) + 0.3*np.cos(np.arange(200)/3)
ac = np.correlate(sig, sig, "full"); mid = len(sig) - 1
ratio = np.max(np.abs(np.delete(ac, mid)))/ac[mid]
assert ratio < 1 and abs(ac[mid] - np.sum(sig**2)) < 1e-9
report("ac_ratio", ratio, ".4f")

# ⟦Ba sóng hình sin: C(τ) không phụ thuộc pha||Three sinusoids: C(τ) is independent of the phases⟧
tt = np.arange(1000)/1000
def three(ph):
    return 2*np.sin(2*np.pi*3*tt + ph[0]) + 1*np.sin(2*np.pi*5*tt + ph[1]) + 0.5*np.sin(2*np.pi*8*tt + ph[2])
def C_circ(v, k):                                                # ⟦tự tương quan chuẩn hóa (chu kỳ 1 s)||normalised autocorrelation (period 1 s)⟧
    return np.mean(v*np.roll(v, -k))/np.mean(v*v)
C_th = lambda tau: (4*np.cos(2*np.pi*3*tau) + np.cos(2*np.pi*5*tau) + 0.25*np.cos(2*np.pi*8*tau))/5.25
ph1, ph2 = (0.3, 1.1, 2.0), (2.5, 0.2, 4.0)
diffs = [abs(C_circ(three(p), k) - C_th(k/1000)) for p in (ph1, ph2) for k in (0, 50, 137, 400)]
assert max(diffs) < 1e-9
pd_ = max(abs(C_circ(three(ph1), k) - C_circ(three(ph2), k)) for k in range(0, 1000, 50))
report("c_tau", C_th(0.05), ".4f"); report("phase_diff", pd_, ".1e")'''),
        ("code", r'''xs = np.linspace(-1.3, 1.3, 521)
plt.figure(figsize=(7, 3.3))
plt.plot(xs, [g_formula(x) if abs(x) < 1 else 0 for x in xs], label=("⟦f = 1−x: γ(x)||f = 1−x: γ(x)⟧"))
plt.plot(xs, np.exp(-np.abs(xs)), label=("⟦f = e^{−x}H(x): γ(x)||f = e^{−x}H(x): γ(x)⟧"))
plt.axhline(0, color="gray", lw=0.6); plt.xlabel("x"); plt.legend(); plt.tight_layout(); plt.show()''', dict(fig="autocorr", cap="⟦Hình 4. Hai tự tương quan chuẩn hóa của chương: đa thức bậc ba cắt tại |x| = 1 và hàm mũ đối xứng, cả hai có cực đại 1 tại gốc.||Figure 4. The chapter's two normalised autocorrelations: a cubic polynomial cut at |x| = 1 and a symmetric exponential, both with a maximum of 1 at the origin.⟧")),
        ("code", r'''# ⟦Tương quan bậc ba U(x1, x2) = Σ f(x) f(x+x1) f(x+x2). Cách A: vòng lặp; cách B: einsum||Triple correlation U(x1, x2) = Σ f(x) f(x+x1) f(x+x2). Method A: loops; method B: einsum⟧
def triple_loops(f, m):
    n = len(f); P = np.zeros(n + 2*m); P[m:m + n] = f
    U = np.zeros((2*m + 1, 2*m + 1))
    for i, x1 in enumerate(range(-m, m + 1)):
        for j, x2 in enumerate(range(-m, m + 1)):
            U[i, j] = sum(P[m + x]*P[m + x + x1]*P[m + x + x2] for x in range(-m, n + m) if 0 <= m + x < n + 2*m and 0 <= m + x + x1 < n + 2*m and 0 <= m + x + x2 < n + 2*m)
    return U
def triple_einsum(f, m):
    n = len(f); P = np.zeros(n + 6*m); P[3*m:3*m + n] = f
    S = np.stack([np.roll(P, -s) for s in range(-m, m + 1)])
    return np.einsum("x,ix,jx->ij", P, S, S)
f123, f321 = np.array([1, 2, 3.0]), np.array([3, 2, 1.0])
U123, U321 = triple_loops(f123, 2), triple_loops(f321, 2)
assert np.allclose(U123, triple_einsum(f123, 2)) and np.allclose(U321, U123[::-1, ::-1])
assert U123[2, 2] == 36 and U123.sum() == 216 and not np.allclose(U123, U321)
assert np.allclose(np.correlate(f123, f123, "full"), np.correlate(f321, f321, "full"))
report("ac_same", "yes", "s"); report("tc_diff", "yes", "s")
report("tc_center", U123[2, 2], ".0f"); report("tc_sum", U123.sum(), ".0f")
for r in range(5):
    report(f"tc_r{r}", " ".join(f"{z:.0f}" for z in U123[r]), "s")

# ⟦Tương quan chéo: g⋆h(x) = h⋆g(−x), và không giao hoán||Cross correlation: g⋆h(x) = h⋆g(−x), and not commutative⟧
def xcorr(g, h):
    n = len(g); P = lambda z, k: z[k] if 0 <= k < n else 0.0
    return {x: sum(P(g, u - x)*P(h, u) for u in range(-n, 2*n)) for x in range(-(n - 1), n)}
ga, hb = np.array([1.0, 2, 4, 3]), np.array([2.0, 0, 1, 5])
c_gh, c_hg = xcorr(ga, hb), xcorr(hb, ga)
xc_ok = all(abs(c_gh[x] - c_hg[-x]) < 1e-12 for x in c_gh); xc_ne = any(abs(c_gh[x] - c_hg[x]) > 1e-9 for x in c_gh)
assert xc_ok and xc_ne
report("xc_ok", "yes", "s"); report("xc_ne", "yes", "s")

# ⟦Phổ năng lượng: IDFT(|X|²) = tự tương quan vòng; hai tín hiệu khác pha cùng phổ||Energy spectrum: IDFT(|X|²) = circular autocorrelation; two signals with different phases share it⟧
v = np.sin(np.arange(64)**1.2) + 0.5
ac_direct = np.array([np.sum(v*np.roll(v, -k)) for k in range(64)])
ac_fft = np.fft.ifft(np.abs(np.fft.fft(v))**2).real
assert np.allclose(ac_direct, ac_fft)
report("wk_diff", np.max(np.abs(ac_direct - ac_fft)), ".1e")
xa, xb = three(ph1), three(ph2)
assert np.allclose(np.abs(np.fft.fft(xa)), np.abs(np.fft.fft(xb)))
report("pha_diff", np.max(np.abs(np.abs(np.fft.fft(xa))**2 - np.abs(np.fft.fft(xb))**2)), ".1e")

# ⟦Phổ năng lượng tích lũy: vạch 50 Hz cộng nhiễu||Cumulative energy spectrum: a 50 Hz line plus noise⟧
rgn = np.random.default_rng(11)
tn = np.arange(1000)/1000
yn = 3*np.sin(2*np.pi*50*tn) + rgn.normal(0, 0.5, 1000)
En = np.abs(np.fft.rfft(yn))**2; cum = np.cumsum(En)/np.sum(En)
assert abs(np.sum(En[1:500])*2/1000/1000 - np.mean(yn**2)) < 5e-2
report("cum_before", cum[49], ".3f"); report("cum_after", cum[51], ".3f"); report("cum_jump", cum[51] - cum[49], ".3f")

# ⟦Dãy xung {1100101}||The pulse sequence {1100101}⟧
pj = np.array([1, 1, 0, 0, 1, 0, 1.0])
lin_ac = np.correlate(pj, pj, "full")
circ_ac = np.array([np.sum(pj*np.roll(pj, -k)) for k in range(7)])
assert lin_ac[6] == 4 and np.all(circ_ac[1:] == 2)
report("ac_peak", lin_ac[6], ".0f"); report("ac_side", np.max(np.delete(lin_ac, 6)), ".0f"); report("ac_circ", circ_ac[1], ".0f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Với $f=1-x$: $\\gamma(0.25)$ = {{g_025}}, $\\gamma(0.5)$ = {{g_05}}, diện tích tử số {{area_ac}}; với $e^{-x}H(x)$: $\\gamma(1)$ = {{g_exp}}. Tự tương quan không vượt đỉnh (tỉ số thùy phụ {{ac_ratio}}). Với ba sóng, $C(0.05)$ = {{c_tau}} và không phụ thuộc pha (lệch {{phase_diff}}). Tương quan bậc ba của $\\{1,2,3\\}$ có tâm {{tc_center}}, tổng {{tc_sum}}, và khác của $\\{3,2,1\\}$ dù tự tương quan hai dãy giống nhau ({{ac_same}}). Tương quan chéo thỏa $g\\star h(x)=h\\star g(-x)$ ({{xc_ok}}) nhưng không giao hoán ({{xc_ne}}). Biến đổi ngược $|X|^2$ trùng tự tương quan vòng (lệch {{wk_diff}}), và hai tín hiệu khác pha có cùng phổ năng lượng (lệch {{pha_diff}}). Phổ tích lũy nhảy {{cum_jump}} tại vạch 50 Hz. Dãy $\\{1100101\\}$ có đỉnh {{ac_peak}}, thùy phụ {{ac_side}} và tự tương quan vòng {{ac_circ}}.||For $f=1-x$: $\\gamma(0.25)$ = {{g_025}}, $\\gamma(0.5)$ = {{g_05}}, numerator area {{area_ac}}; for $e^{-x}H(x)$: $\\gamma(1)$ = {{g_exp}}. The autocorrelation never exceeds its peak (side ratio {{ac_ratio}}). For three waves, $C(0.05)$ = {{c_tau}} and is independent of the phases (difference {{phase_diff}}). The triple correlation of $\\{1,2,3\\}$ has centre {{tc_center}}, sum {{tc_sum}}, and differs from that of $\\{3,2,1\\} although the two autocorrelations are identical ({{ac_same}}). Cross correlation satisfies $g\\star h(x)=h\\star g(-x)$ ({{xc_ok}}) but is not commutative ({{xc_ne}}). The inverse transform of $|X|^2$ equals the circular autocorrelation (deviation {{wk_diff}}), and two signals with different phases share the energy spectrum (deviation {{pha_diff}}). The cumulative spectrum jumps by {{cum_jump}} at the 50 Hz line. The sequence $\\{1100101\\}$ has peak {{ac_peak}}, side value {{ac_side}} and circular autocorrelation {{ac_circ}}.⟧"""),
    ],
)
