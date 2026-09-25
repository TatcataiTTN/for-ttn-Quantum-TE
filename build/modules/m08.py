from lib import F, C, UL, OL, TBL

MOD = dict(
    n=8, slug="two-domains", part="A", book="B",
    title="⟦Hai miền: hàm và biến đổi của nó||The two domains: a function and its transform⟧",
    blurb="⟦Diện tích, mômen, tâm khối, phương sai, độ trơn, độ rộng tương đương, hệ thức bất định, sai phân, trung bình trượt và định lý giới hạn trung tâm: mỗi tính chất ở một miền ứng với một tính chất ở miền kia.||"
          "Area, moments, centroid, variance, smoothness, equivalent width, the uncertainty relation, finite differences, running means and the central-limit theorem: each property in one domain has a partner in the other.⟧",
    src="⟦Bracewell, chương 8, tr. 151–198||Bracewell, chapter 8, pp. 151–198⟧",
    data="⟦Sinh bằng mã: mũ, gamma, Gauss, tam giác, chữ nhật, sech, Lorentz||Generated in code: exponentials, gamma, Gaussian, triangle, rectangle, sech, Lorentzian⟧",
    objectives=[
        "⟦Nêu và dùng các cặp tính chất: diện tích và tung độ giữa, mômen bậc $n$ và đạo hàm bậc $n$ tại gốc, tâm khối, phương sai.||State and use the pairs of properties: area and central ordinate, $n$th moment and $n$th derivative at the origin, centroid, variance.⟧",
        "⟦Liên hệ độ trơn của hàm với tốc độ tắt dần của biến đổi (độ dốc trên đồ thị log-log, decibel trên octave).||Relate the smoothness of a function to the decay rate of its transform (log-log slope, decibels per octave).⟧",
        "⟦Tính độ rộng tương đương, độ rộng tự tương quan, độ rộng bình phương trung bình và hiểu hệ thức bất định.||Compute equivalent width, autocorrelation width and mean-square width, and understand the uncertainty relation.⟧",
        "⟦Dùng sai phân hữu hạn, trung bình trượt, và giải thích định lý giới hạn trung tâm bằng biến đổi.||Use finite differences and running means, and explain the central-limit theorem through transforms.⟧",
        "⟦Dùng các bất đẳng thức: cận trên của tung độ, độ dốc, và Schwarz.||Use the inequalities: upper bounds on ordinate and slope, and Schwarz's.⟧",
    ],
    parts=[
        # ------------------------------------------------ PART 1
        dict(
            title="⟦Diện tích, mômen và tâm khối||Area, moments and the centroid⟧",
            scr=("⟦Hàm và biến đổi của nó như hai miền, \"trên\" và \"dưới\", mỗi hàm có một \"cái bóng\" ở miền kia.||A function and its transform as two domains, \"upper\" and \"lower\", each function accompanied by a \"shadow\" in the other.⟧",
                 "⟦Ta cần biết một đặc điểm của hàm mà không muốn đảo phép biến đổi và tích phân đầy đủ.||We often need one feature of a function without inverting the transform and integrating in full.⟧",
                 "⟦Diện tích bằng tung độ giữa của biến đổi; mômen bậc $n$ tỉ lệ với đạo hàm bậc $n$ của biến đổi tại gốc.||The area equals the central ordinate of the transform; the $n$th moment is proportional to the $n$th derivative of the transform at the origin.⟧"),
            preview=["⟦Diện tích và tung độ giữa||Area and central ordinate⟧", "⟦Mômen bậc một và tâm khối||The first moment and the centroid⟧", "⟦Mômen quán tính và mômen bậc $n$||Moment of inertia and the $n$th moment⟧"],
            slides=[
                ("⟦Hai miền||Two domains⟧",
                 "<p>⟦Có thể nghĩ hàm và biến đổi của nó ở hai miền, gọi là miền trên và miền dưới, như hàm đi lại ở mặt đất còn biến đổi ở thế giới ngầm (Doetsch, 1943). Mỗi hàm có một \"bóng\" ở miền kia, gắn duy nhất với nó qua biến đổi Fourier và đổi khi hàm đổi. Trong các hình, hàm để bên trái, biến đổi bên phải (Bracewell, tr. 151).||"
                 "We may think of functions and their transforms as occupying two domains, sometimes called the upper and the lower, as if functions circulated at ground level and their transforms in the underworld (Doetsch, 1943). Each function is accompanied by a counterpart, a shadow in the other domain, associated uniquely with it through the Fourier transform and changing as the function changes. In the illustrations functions are on the left and transforms on the right (Bracewell, p. 151).⟧</p>"),
                ("⟦Các định lý là cặp phép toán||The theorems are pairs of operations⟧",
                 "<p>⟦Các định lý trước có thể xem là danh sách cặp phép toán đồng thời, một ở miền hàm, một ở miền biến đổi. Nén trục hoành ở miền hàm là giãn trục hoành cộng co tung độ ở miền biến đổi; dịch ở miền hàm là xoắn ở miền biến đổi; tích chập ở miền hàm là nhân ở miền biến đổi. Ta cũng cần các cặp tính chất: diện tích dưới hàm và tung độ giữa của biến đổi là một cặp (tr. 151 đến 152). Mục đích: khi chỉ cần đặc điểm của hàm, nhảy sang miền kia và đọc thẳng đáp số.||"
                 "The earlier theorems are a list of pairs of simultaneous operations, one in the function domain and one in the transform domain. Compression of the abscissas in the function domain means expansion of the abscissas and contraction of the ordinates in the transform domain; translation means a twisting; convolution means multiplication. We now consider pairs of corresponding properties: the area under a function and the central ordinate of its transform are such a pair (pp. 151 to 152). The purpose: when only a feature of a function is needed, cross to the other domain and read the answer directly.⟧</p>"),
                ("⟦Tích phân xác định||The definite integral⟧",
                 "<p>⟦Tích phân xác định của hàm từ $-\\infty$ tới $\\infty$ bằng giá trị biến đổi tại gốc, vì $F(0)=\\int f(x)e^{0}dx$ (tr. 152). Do đối xứng, diện tích dưới biến đổi bằng $f(0)$. Số đo với $f=e^{-x}H(x)$: diện tích {{ar_exp}} bằng $F(0)$ = {{ar_F0}}, và diện tích dưới $F$ bằng {{ar_f0}}, giá trị trung bình của $f$ ở hai phía chỗ nhảy tại 0.||"
                 "The definite integral of a function from $-\\infty$ to $\\infty$ equals the value of its transform at the origin, since $F(0)=\\int f(x)e^{0}dx$ (p. 152). By symmetry the area under the transform equals $f(0)$. Measured with $f=e^{-x}H(x)$: the area {{ar_exp}} equals $F(0)$ = {{ar_F0}}, and the area under $F$ equals {{ar_f0}}, the mean of $f$ on the two sides of the jump at 0.⟧</p>"
                 + F("⟦Diện tích và tung độ giữa||Area and central ordinate⟧", r"\int_{-\infty}^{\infty}f(x)\,dx=F(0),\qquad \int_{-\infty}^{\infty}F(s)\,ds=f(0)")),
                ("⟦Hệ quả: bất kỳ phép toán nào giữ diện tích||Consequence: any operation that preserves area⟧",
                 "<p>⟦Phép toán nào trên $f(x)$ giữ nguyên diện tích, chẳng hạn dịch, đều giữ nguyên tung độ giữa của biến đổi; với dịch điều này khớp định lý dịch, vì $e^{-i2\\pi as}F(s)$ tại $s=0$ bằng $F(0)$. Ví dụ khó hơn: tách $f$ tại $x=0$ thành hai nửa rồi đẩy xa nhau $2a$, tức $f(x-a)H(x-a)+f(x+a)H(-x-a)$. Diện tích không đổi nên tung độ giữa của biến đổi không đổi; vì tung độ giữa của hàm bây giờ bằng 0 nên diện tích của biến đổi phải bằng 0 (tr. 152). Số đo với $f=e^{-|x|}$, $a=0.5$: diện tích {{sp_area}}, và diện tích của biến đổi {{sp_ft_area}}.||"
                 "Any operation on $f(x)$ that leaves its area unchanged, say translation, leaves the central ordinate of the transform unchanged; for translation this agrees with the shift theorem since $e^{-i2\\pi as}F(s)$ at $s=0$ equals $F(0)$. A harder example: split $f$ at $x=0$ into two halves and push them apart by $2a$, giving $f(x-a)H(x-a)+f(x+a)H(-x-a)$. The area is unchanged so the central ordinate of the transform is too; since the central ordinate of the function is now zero, the area of the transform must be zero (p. 152). Measured with $f=e^{-|x|}$, $a=0.5$: the area is {{sp_area}}, and the area of the transform is {{sp_ft_area}}.⟧</p>"),
                ("⟦Mômen bậc một||The first moment⟧",
                 "<p>⟦Theo tương tự khối lượng dọc theo một đường, mômen bậc một quanh gốc là $\\int xf(x)dx$. Định lý: mômen bậc một bằng $-(2\\pi i)^{-1}$ lần độ dốc của $F(s)$ tại $s=0$ (tr. 153 đến 154). Suy ra từ định lý đạo hàm: $\\int(-i2\\pi x)f(x)e^{-i2\\pi xs}dx=F'(s)$. Số đo với $f=e^{-x}H(x)$: $\\int xf=$ {{fm_exp}}, và $F'(0)/(-2\\pi i)$ = {{fm_exp}}.||"
                 "By analogy with mass distribution along a line, the first moment about the origin is $\\int xf(x)dx$. Theorem: the first moment equals $-(2\\pi i)^{-1}$ times the slope of $F(s)$ at $s=0$ (pp. 153 to 154). It follows from the derivative theorem: $\\int(-i2\\pi x)f(x)e^{-i2\\pi xs}dx=F'(s)$. Measured with $f=e^{-x}H(x)$: $\\int xf=$ {{fm_exp}}, and $F'(0)/(-2\\pi i)$ = {{fm_exp}}.⟧</p>"
                 + F("⟦Mômen bậc một||First moment⟧", r"\int_{-\infty}^{\infty}x\,f(x)\,dx=\frac{F'(0)}{-2\pi i}")),
                ("⟦Trường hợp đặc biệt: mômen bậc một bằng 0||The special case of zero first moment⟧",
                 "<p>⟦Hàm có mômen bậc một bằng 0 có biến đổi độ dốc 0 tại gốc, và ngược lại. Hơn nữa, nếu một hàm có độ dốc 0 tại gốc và không bằng 0 ở đó thì biến đổi của nó có tâm khối tại gốc (tr. 155). Số đo: Gauss chẵn có mômen bậc một {{fm_gauss}} và biến đổi có độ dốc {{fm_gauss_slope}} tại gốc.||"
                 "A function whose first moment is zero has a transform with zero slope at its origin, and conversely. Furthermore, if a function has zero slope at the origin and is not zero there, its transform has its centre of gravity at the origin (p. 155). Measured: the even Gaussian has first moment {{fm_gauss}} and its transform has slope {{fm_gauss_slope}} at the origin.⟧</p>"),
                ("⟦Tâm khối||The centroid⟧",
                 "<p>⟦Tâm khối $\\langle x\\rangle$ là điểm mà diện tích nhân $\\langle x\\rangle$ bằng mômen bậc một; nó nói hàm chủ yếu tập trung ở đâu, hoặc \"thời điểm\" của một xung tín hiệu (tr. 155). Theo các mục trước, $\\langle x\\rangle=F'(0)/(-2\\pi iF(0))$: hoành độ tâm khối bằng độ dốc giữa chia tung độ giữa của biến đổi, nhân $-(2\\pi i)^{-1}$. Nếu diện tích bằng 0 thì $\\langle x\\rangle$ trở thành vô hạn (tr. 156). Số đo với $f=xe^{-x}H(x)$ (bảng 8.4): $F=(1+i2\\pi s)^{-2}$, tâm khối {{cen_gam}} theo tích phân và {{cen_gam_ft}} theo $F'(0)/(-2\\pi iF(0))$.||"
                 "The centroid $\\langle x\\rangle$ is the point such that the area times $\\langle x\\rangle$ equals the first moment; it tells where a function is mainly concentrated, or the epoch of a signal pulse (p. 155). From the preceding sections $\\langle x\\rangle=F'(0)/(-2\\pi iF(0))$: the abscissa of the centroid is the central slope over the central ordinate of the transform, times $-(2\\pi i)^{-1}$. If the area is zero, $\\langle x\\rangle$ becomes infinite (p. 156). Measured with $f=xe^{-x}H(x)$ (Table 8.4): $F=(1+i2\\pi s)^{-2}$, centroid {{cen_gam}} by integration and {{cen_gam_ft}} by $F'(0)/(-2\\pi iF(0))$.⟧</p>"
                 + F("⟦Tâm khối||Centroid⟧", r"\langle x\rangle=\frac{\int xf\,dx}{\int f\,dx}=\frac{F'(0)}{-2\pi i\,F(0)}")),
                ("⟦Mômen quán tính (mômen bậc hai)||The moment of inertia (second moment)⟧",
                 "<p>⟦Mômen bậc hai $\\int x^2f\\,dx$ bằng $(4\\pi^2)^{-1}$ lần độ cong hướng xuống của biến đổi tại gốc: $\\int x^2f\\,dx=-F''(0)/4\\pi^2$ (tr. 156 đến 157). Hàm có mômen bậc hai cao có biến đổi cong nhiều tại gốc; vì có thừa số $x^2$, mômen nhạy với $f$ ở $x$ lớn, và điều xảy ra ở $x$ lớn phản ánh vào hành vi của biến đổi tại gốc $s$. Nếu mômen bậc hai vô hạn thì độ dốc của biến đổi nhảy đột ngột ở gốc (hình 8.5). Số đo với $f=xe^{-x}H(x)$: $\\int x^2f=$ {{m2_gam}}, và $-F''(0)/4\\pi^2$ = {{m2_gam_ft}}.||"
                 "The second moment $\\int x^2f\\,dx$ equals $(4\\pi^2)^{-1}$ times the downward curvature of the transform at the origin: $\\int x^2f\\,dx=-F''(0)/4\\pi^2$ (pp. 156 to 157). A function with a high second moment has a transform that is strongly curved at the origin; because of the factor $x^2$ the moment is sensitive to $f$ at large $x$, and what happens at large $x$ is reflected in the behaviour of the transform at the origin of $s$. If the second moment is infinite the slope of the transform jumps abruptly at the origin (Fig. 8.5). Measured with $f=xe^{-x}H(x)$: $\\int x^2f=$ {{m2_gam}}, and $-F''(0)/4\\pi^2$ = {{m2_gam_ft}}.⟧</p>"
                 + F("⟦Mômen bậc hai||Second moment⟧", r"\int_{-\infty}^{\infty}x^2f(x)\,dx=-\frac{F''(0)}{4\pi^2}")),
                ("⟦Mômen bậc $n$ và tồn tại||The $n$th moment and existence⟧",
                 "<p>⟦Mômen bậc $n$ bằng $(-2\\pi i)^{-n}$ lần đạo hàm bậc $n$ của $F$ tại gốc, miễn là mômen tồn tại (tr. 157). Nếu $f$ tắt như $|x|^{-m}$ ở $x$ lớn thì chỉ có khoảng $[m]-1$ mômen đầu tồn tại, và biến đổi có gián đoạn bậc cao ở gốc; nếu bậc $M$ đạo hàm của $F$ là xung thì mômen bậc $M$ vô hạn (tr. 158). Số đo với $f=e^{-x}H(x)$, $n!$: mômen bậc 2, 3, 4 bằng {{mom_2}}, {{mom_3}}, {{mom_4}} theo tích phân và theo đạo hàm của $F$ (tích phân đường quanh gốc).||"
                 "The $n$th moment equals $(-2\\pi i)^{-n}$ times the $n$th derivative of $F$ at the origin, provided the moment exists (p. 157). If $f$ behaves as $|x|^{-m}$ for large $|x|$ then only the first $[m]-1$ moments exist and the transform has a higher-order discontinuity at the origin; if the $M$th derivative of $F$ is impulsive the $M$th moment is infinite (p. 158). Measured with $f=e^{-x}H(x)$, $n!$: the moments of order 2, 3, 4 equal {{mom_2}}, {{mom_3}}, {{mom_4}} both by integration and from derivatives of $F$ (a contour integral around the origin).⟧</p>"
                 + F("⟦Mômen bậc $n$||The $n$th moment⟧", r"\int_{-\infty}^{\infty}x^nf(x)\,dx=\frac{F^{(n)}(0)}{(-2\pi i)^n}")),
                ("⟦Tự kiểm tra phần 1||Self-check, part 1⟧",
                 UL(["⟦Vì sao đẩy hai nửa của $f$ ra xa nhau làm diện tích biến đổi bằng 0?||Why does pushing the two halves of $f$ apart make the area of the transform zero?⟧",
                     "⟦Khi nào tâm khối không xác định?||When is the centroid undefined?⟧",
                     "⟦Vì sao mômen bậc hai nhạy với hành vi của $f$ ở $x$ lớn?||Why is the second moment sensitive to the behaviour of $f$ at large $x$?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: vì tung độ giữa của hàm bằng 0; khi diện tích bằng 0; do thừa số $x^2$.||Hints: because the central ordinate of the function is zero; when the area is zero; because of the factor $x^2$.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 2
        dict(
            title="⟦Bình phương trung bình, phương sai và độ trơn||Mean-square values, variance and smoothness⟧",
            scr=("⟦Trong thống kê, phương sai là độ trải; trong cơ học, bán kính quán tính.||In statistics the variance is the spread; in mechanics the radius of gyration.⟧",
                 "⟦Tích chập làm hàm rộng ra và trơn hơn, nhưng \"rộng hơn\" và \"trơn hơn\" nghĩa là gì và đo ra sao?||Convolution makes a function wider and smoother, but what do \"wider\" and \"smoother\" mean and how are they measured?⟧",
                 "⟦Phương sai và mômen cộng lại dưới tích chập; độ trơn (bậc đạo hàm còn là xung) cũng cộng lại; độ trơn quyết định độ dốc tắt dần của phổ.||Variances and moments add under convolution; smoothness (the derivative order at which impulses appear) also adds; smoothness sets the decay slope of the spectrum.⟧"),
            preview=["⟦Bình phương trung bình và phương sai||Mean-square abscissa and variance⟧", "⟦Cộng dưới tích chập||Additivity under convolution⟧", "⟦Độ trơn và tốc độ tắt dần||Smoothness and rate of decay⟧"],
            slides=[
                ("⟦Hoành độ bình phương trung bình||The mean-square abscissa⟧",
                 "<p>⟦$\\langle x^2\\rangle$ là giá trị trung bình của $x^2$ với trọng số $f(x)$, và theo kết quả trước $\\langle x^2\\rangle=\\dfrac{-F''(0)}{4\\pi^2F(0)}$ (tr. 158). Trong cơ học, $\\langle x^2\\rangle$ là bình phương bán kính quán tính của một thanh có mật độ $f$; trong thống kê, với hàm phân bố tần số, nó là khái niệm quan trọng và ($F$) là \"hàm đặc trưng\" (tr. 158). Với $f=xe^{-x}H(x)$ giá trị là {{ms_gam}} (bảng 8.4).||"
                 "$\\langle x^2\\rangle$ is the mean of $x^2$ weighted by $f(x)$, and by the previous results $\\langle x^2\\rangle=\\dfrac{-F''(0)}{4\\pi^2F(0)}$ (p. 158). In dynamics $\\langle x^2\\rangle$ is the square of the radius of gyration of a rod of mass density $f$; in statistics, for a frequency distribution function, it is an important concept and $F$ is the \"characteristic function\" (p. 158). For $f=xe^{-x}H(x)$ the value is {{ms_gam}} (Table 8.4).⟧</p>"
                 + F("⟦Bình phương trung bình||Mean-square abscissa⟧", r"\langle x^2\rangle=\frac{\int x^2f\,dx}{\int f\,dx}=\frac{-F''(0)}{4\pi^2F(0)}")),
                ("⟦Cộng dưới tích chập||Additivity under convolution⟧",
                 "<p>⟦Hoành độ bình phương trung bình của $f*g$ bằng tổng của $f$ và $g$ nếu tâm khối của $f$ (hoặc $g$) nằm ở gốc. Đây là biểu thức định lượng của hiệu ứng làm nhòe của tích chập. Suy ra: $(FG)''=F''G+2F'G'+FG''$, nên tổng quát (tr. 158 đến 159):||"
                 "The mean-square abscissa of $f*g$ equals the sum for $f$ and $g$ provided that $f$ (or $g$) has its centroid at the origin. This is a quantitative expression of the smoothing-out or diffusing effect of convolution. Derivation: $(FG)''=F''G+2F'G'+FG''$, so in general (pp. 158 to 159):⟧</p>"
                 + F("⟦Cộng bình phương trung bình||Adding mean squares⟧", r"\langle x^2\rangle_{f*g}=\langle x^2\rangle_f+\langle x^2\rangle_g+2\langle x\rangle_f\langle x\rangle_g")
                 + "<p>⟦Số đo với $f=xe^{-x}H$ (tâm khối 2, $\\langle x^2\\rangle=6$) và $g=e^{-x}H$ (tâm khối 1, $\\langle x^2\\rangle=2$): $\\langle x^2\\rangle_{f*g}$ = {{ms_conv}} bằng $6+2+2\\cdot2\\cdot1$; tích chập đo trên lưới cho cùng số.||Measured with $f=xe^{-x}H$ (centroid 2, $\\langle x^2\\rangle=6$) and $g=e^{-x}H$ (centroid 1, $\\langle x^2\\rangle=2$): $\\langle x^2\\rangle_{f*g}$ = {{ms_conv}} equals $6+2+2\\cdot2\\cdot1$; the convolution measured on a grid gives the same number.⟧</p>"),
                ("⟦Trục dịch: định lý song song||A displaced axis: the parallel-axis theorem⟧",
                 "<p>⟦Lấy $g(x)=\\delta(x-a)$, có $\\langle x^2\\rangle_g=a^2$; ta được định lý quen thuộc về mômen quán tính quanh trục không qua tâm khối: nếu gốc của $f$ ở tâm khối thì $\\langle x^2\\rangle_{f*\\delta_a}=\\langle x^2\\rangle_f+a^2$ (tr. 159). Số đo với tam giác $\\Lambda$ ($\\langle x^2\\rangle=1/6$) dịch $a=2$: {{parallel}} $=1/6+4$.||"
                 "Take $g(x)=\\delta(x-a)$, for which $\\langle x^2\\rangle_g=a^2$; we obtain the familiar theorem on the moment of inertia of a mass about an axis not through its centre of gravity: if $f$ has its origin at its centroid, $\\langle x^2\\rangle_{f*\\delta_a}=\\langle x^2\\rangle_f+a^2$ (p. 159). Measured with the triangle $\\Lambda$ ($\\langle x^2\\rangle=1/6$) shifted by $a=2$: {{parallel}} $=1/6+4$.⟧</p>"),
                ("⟦Bán kính quán tính và phương sai||Radius of gyration and variance⟧",
                 "<p>⟦Bán kính quán tính là căn bậc hai của hoành độ bình phương trung bình, tiện vì có cùng thứ nguyên với $x$, dù các tính chất (cộng, độ cong) đơn giản hơn khi viết theo $\\langle x^2\\rangle$ (tr. 159). Phương sai $\\sigma^2=\\langle(x-\\langle x\\rangle)^2\\rangle=\\langle x^2\\rangle-\\langle x\\rangle^2$ là độ lệch bình phương trung bình quanh tâm khối; nó bằng $\\langle x^2\\rangle$ khi chọn gốc ở tâm khối. Phương sai của $f*g$ bằng tổng phương sai (tr. 160). Số đo với $f=xe^{-x}H$ và $\\Lambda$: $\\sigma_f^2$ = {{var_gam}}, $\\sigma_\\Lambda^2$ = {{var_tri}}, và phương sai tích chập {{var_conv}}.||"
                 "The radius of gyration is the square root of the mean-square abscissa, convenient for having the same dimensions as $x$, though the properties (additivity, curvature) are simpler in terms of $\\langle x^2\\rangle$ (p. 159). The variance $\\sigma^2=\\langle(x-\\langle x\\rangle)^2\\rangle=\\langle x^2\\rangle-\\langle x\\rangle^2$ is the mean-square deviation from the centroid; it equals $\\langle x^2\\rangle$ when the origin is at the centroid. The variance of $f*g$ equals the sum of the variances (p. 160). Measured with $f=xe^{-x}H$ and $\\Lambda$: $\\sigma_f^2$ = {{var_gam}}, $\\sigma_\\Lambda^2$ = {{var_tri}}, and the convolution has variance {{var_conv}}.⟧</p>"
                 + F("⟦Phương sai||Variance⟧", r"\sigma^2=\langle x^2\rangle-\langle x\rangle^2,\qquad \sigma^2_{f*g}=\sigma_f^2+\sigma_g^2")),
                ("⟦Độ trơn và độ nén của biến đổi||Smoothness and compactness⟧",
                 "<p>⟦Hàm càng trơn (càng nhiều đạo hàm liên tục) thì biến đổi càng gọn, tức tắt dần nhanh theo $s$. Nếu hàm và $n-1$ đạo hàm đầu liên tục thì biến đổi tắt ít nhất như $|s|^{-(n+1)}$; nói gọn: nếu đạo hàm bậc $k$ trở thành xung thì biến đổi cư xử như $|s|^{-k}$ ở vô cực (tr. 160 đến 161). Vì thế $\\text{sinc}^2x$ tắt nhanh hơn $\\text{sinc}\\,x$ nhiều, gắn với biến đổi $\\Lambda$ trơn hơn $\\Pi$ (hình 8.6).||"
                 "The smoother a function is, as measured by the number of continuous derivatives it possesses, the more compact its transform, i.e. the faster it dies away with increasing $s$. If a function and its first $n-1$ derivatives are continuous its transform dies away at least as rapidly as $|s|^{-(n+1)}$; in short, if the $k$th derivative becomes impulsive the transform behaves as $|s|^{-k}$ at infinity (pp. 160 to 161). That is why $\\text{sinc}^2x$ dies away much faster than $\\text{sinc}\\,x$, associated with the transform $\\Lambda$ being smoother than $\\Pi$ (Fig. 8.6).⟧</p>"),
                ("⟦Thử số: độ dốc log-log||Numerical test: the log-log slope⟧",
                 "<p>⟦Đo bằng tích phân số tại các điểm nửa nguyên $s=10.5$ và $20.5$: hàm chữ nhật (bản thân nhảy) cho độ dốc {{sm_1}}; tam giác (đạo hàm bậc một nhảy, đạo hàm bậc hai là xung) cho {{sm_2}}; xung parabol từng khúc $\\Pi*\\Pi*\\Pi$ (đạo hàm bậc ba là xung) cho {{sm_3}}. Mỗi lần thêm một tích chập với $\\Pi$ làm độ dốc giảm thêm một đơn vị.||"
                 "Measured by numerical integration at half-integer points $s=10.5$ and $20.5$: the rectangle (the function itself jumps) gives slope {{sm_1}}; the triangle (first derivative jumps, second is impulsive) gives {{sm_2}}; the piecewise parabolic pulse $\\Pi*\\Pi*\\Pi$ (third derivative impulsive) gives {{sm_3}}. Each further convolution with $\\Pi$ steepens the slope by one unit.⟧</p>{{fig:smooth_decay}}"),
                ("⟦Decibel trên octave||Decibels per octave⟧",
                 "<p>⟦Hàm có góc nhưng không nhảy (đạo hàm gián đoạn) có biến đổi tắt như $s^{-2}$ và phổ công suất như $s^{-4}$; theo ngôn ngữ mạch điện đó là suy giảm 12 dB mỗi octave, hay 40 dB mỗi decade (tr. 163). Trên đồ thị log-log, hàm $s^{-2}$ là đường thẳng độ dốc $-2$; các đơn vị logarit (octave, decade, decibel, neper) cho phép nói độ dốc, vốn không thứ nguyên, bằng đơn vị dễ hiểu. Số đo: $20\\log_{10}2\\times2$ = {{db_2}} dB mỗi octave, và 40 dB mỗi decade cho $s^{-2}$.||"
                 "A function with corners but no jumps (discontinuous derivative) has a transform dying as $s^{-2}$ and a power spectrum as $s^{-4}$; in electric-circuit language that is attenuation at 12 decibels per octave or 40 decibels per decade (p. 163). On a log-log plot a function varying as $s^{-2}$ is a straight line of slope $-2$; logarithmic units (octave, decade, decibel, neper) let the dimensionless slope be stated in expressive units. Measured: $20\\log_{10}2\\times2$ = {{db_2}} dB per octave, and 40 dB per decade for $s^{-2}$.⟧</p>"),
                ("⟦Gián đoạn trung gian và độ trơn dưới tích chập||Intermediate discontinuities and smoothness under convolution⟧",
                 "<p>⟦Có những gián đoạn có độ nghiêm trọng nằm giữa nhảy và góc: góc mà hàm đổi độ dốc từ ngang sang dọc xếp giữa góc thường và nhảy thường (bảng 8.2, tr. 164 đến 165). $\\delta(x)$ và $x^{-1}$ có cùng loại vô cực tại 0, và gián đoạn vô hạn yếu nhất $\\log x$ tương đương một bước nhảy. Về tích chập: nếu $f$ có độ trơn bậc $m$ và $g$ bậc $n$ thì $f*g$ có độ trơn bậc $m+n$, vì $F\\sim s^{-m}$, $G\\sim s^{-n}$, $FG\\sim s^{-(m+n)}$ (tr. 162 đến 163). Độ trơn cộng dưới tích chập cũng như $\\sigma^2$. Nhưng độ trơn đo theo cách này không luôn khớp cảm nhận định tính: $\\Lambda$ tích chập với Gauss rất hẹp là trơn vô hạn nhưng chỉ tròn các góc rất nhỏ nên xe chạy vẫn xóc như cũ (tr. 163).||"
                 "Some discontinuities have severity between a jump and a corner: a corner where a function changes slope from horizontal to vertical ranks midway between simple corners and simple jumps (Table 8.2, pp. 164 to 165). $\\delta(x)$ and $x^{-1}$ have the same kind of infinity at 0, and the weakest infinite discontinuity, $\\log x$, is equivalent to a simple jump. On convolution: if $f$ has smoothness of order $m$ and $g$ of order $n$ then $f*g$ has smoothness $m+n$, since $F\\sim s^{-m}$, $G\\sim s^{-n}$, $FG\\sim s^{-(m+n)}$ (pp. 162 to 163). Smoothness adds under convolution just as $\\sigma^2$ does. But smoothness so measured does not always match qualitative ideas: $\\Lambda$ convolved with a very narrow Gaussian is infinitely smooth yet only its tiny corners are rounded, so the ride is as rough as before (p. 163).⟧</p>"),
                ("⟦Tự kiểm tra phần 2||Self-check, part 2⟧",
                 UL(["⟦Phương sai của $f*g$ nếu $\\sigma_f^2=2$ và $\\sigma_g^2=3$?||What is the variance of $f*g$ if $\\sigma_f^2=2$ and $\\sigma_g^2=3$?⟧",
                     "⟦Biến đổi tắt thế nào nếu đạo hàm bậc ba của hàm là xung?||How does the transform decay if the third derivative of the function is impulsive?⟧",
                     "⟦12 dB mỗi octave tương ứng với lũy thừa nào của $s$?||12 dB per octave corresponds to which power of $s$?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: 5; như $|s|^{-3}$; $s^{-2}$ (biên độ).||Hints: 5; as $|s|^{-3}$; $s^{-2}$ (amplitude).⟧</p>"),
            ]),
        # ------------------------------------------------ PART 3
        dict(
            title="⟦Độ rộng tương đương và độ rộng tự tương quan||Equivalent width and autocorrelation width⟧",
            scr=("⟦\"Rộng\" của một hàm có nhiều cách đo, và mỗi cách hợp với một hoàn cảnh vật lý.||There are many ways to measure the \"width\" of a function, each suited to a physical circumstance.⟧",
                 "⟦Hàm càng rộng thì phổ càng hẹp, nhưng có một đại lượng chính xác thể hiện tính nghịch đảo này không?||The wider the function the narrower its spectrum, but is there an exact quantity that shows this reciprocity?⟧",
                 "⟦Độ rộng tương đương của hàm bằng nghịch đảo độ rộng tương đương của biến đổi; độ rộng tự tương quan ổn định hơn.||The equivalent width of a function equals the reciprocal of that of its transform; the autocorrelation width is more robust.⟧"),
            preview=["⟦Độ rộng tương đương||Equivalent width⟧", "⟦Định lý nghịch đảo||The reciprocity theorem⟧", "⟦Độ rộng tự tương quan||Autocorrelation width⟧"],
            slides=[
                ("⟦Độ rộng tương đương||Equivalent width⟧",
                 "<p>⟦Một thước đo tiện của độ rộng là diện tích chia tung độ giữa: $W_f=\\int f\\,dx/f(0)$. Nói cách khác, đó là bề rộng hình chữ nhật có chiều cao bằng tung độ giữa và cùng diện tích với hàm (hình 8.8, tr. 164 đến 165). Trong quang phổ học, độ rộng tương đương của một vạch là bề rộng của hình chữ nhật có cùng cường độ giữa và cùng diện tích; trong lý thuyết ăng ten, độ rộng chùm hiệu dụng cũng có tính chất này (tr. 165).||"
                 "A convenient measure of width is the area divided by the central ordinate: $W_f=\\int f\\,dx/f(0)$. In other words it is the width of the rectangle whose height equals the central ordinate and whose area equals that of the function (Fig. 8.8, pp. 164 to 165). In spectroscopy the equivalent width of a spectral line is the width of a rectangular profile with the same central intensity and the same area; in antenna theory the effective beamwidth has the character of an equivalent width (p. 165).⟧</p>"
                 + F("⟦Độ rộng tương đương||Equivalent width⟧", r"W_f=\frac{\int f(x)\,dx}{f(0)}=\frac{F(0)}{f(0)}")),
                ("⟦Một số ví dụ||Some examples⟧",
                 "<p>⟦Nếu $f(0)=0$ thì độ rộng tương đương không tồn tại. Số đo (tích phân số): $e^{-|x|}$ có $W$ = {{ew_exp}}; Lorentz $1/(1+x^2)$ có $W$ = {{ew_lor}} ($=\\pi$); $\\Lambda$ có {{ew_tri}}; Gauss $e^{-\\pi x^2}$ có {{ew_gauss}} (bảng 8.3).||"
                 "If $f(0)=0$ the equivalent width does not exist. Measured (numerical integration): $e^{-|x|}$ has $W$ = {{ew_exp}}; the Lorentzian $1/(1+x^2)$ has $W$ = {{ew_lor}} ($=\\pi$); $\\Lambda$ has {{ew_tri}}; the Gaussian $e^{-\\pi x^2}$ has {{ew_gauss}} (Table 8.3).⟧</p>"),
                ("⟦Định lý nghịch đảo||The reciprocity theorem⟧",
                 "<p>⟦Độ rộng tương đương của một hàm bằng nghịch đảo độ rộng tương đương của biến đổi của nó: $W_fW_F=1$ khi cả hai tồn tại (tr. 167). Định lý gợi định lý tỉ lệ, nhưng định lý tỉ lệ chỉ áp dụng cho hàm cùng dạng; ở đây ta biết đại lượng nào cư xử nghịch đảo và có thể xếp hạng các hàm khác dạng theo đại lượng đó. Chứng minh: $W_F=\\int F\\,ds/F(0)=f(0)/\\int f\\,dx$. Số đo: $W_fW_F$ = {{ew_prod_exp}} cho $e^{-|x|}$ (với $W_F$ = {{ew_F_exp}}), và {{ew_prod_lor}} cho Lorentz (với $W_F$ = {{ew_F_lor}}).||"
                 "The equivalent width of a function equals the reciprocal of the equivalent width of its transform: $W_fW_F=1$ whenever both exist (p. 167). The theorem is reminiscent of the similarity theorem, which however is restricted to functions of a given shape; here we know which quantity behaves reciprocally, and unlike functions can be ranked by it. Proof: $W_F=\\int F\\,ds/F(0)=f(0)/\\int f\\,dx$. Measured: $W_fW_F$ = {{ew_prod_exp}} for $e^{-|x|}$ (with $W_F$ = {{ew_F_exp}}) and {{ew_prod_lor}} for the Lorentzian (with $W_F$ = {{ew_F_lor}}).⟧</p>"
                 + F("⟦Nghịch đảo||Reciprocity⟧", r"W_f\cdot W_F=1")),
                ("⟦Giới hạn của độ rộng tương đương||Limits of equivalent width⟧",
                 "<p>⟦Độ rộng tương đương không phải lúc nào cũng thước đo tốt. Để nói độ rộng băng của bộ lọc hay độ rộng chùm của ăng ten, thường dùng \"độ rộng ở nửa công suất\", và theo thước đo đó ví dụ thứ hai trong hình 8.9 hẹp hơn, khớp với kinh nghiệm (tr. 167). Có nghịch lý: chuyển động rối cục bộ lan ra ngoài trong không gian trong khi phổ rối lan tới số sóng cao hơn; ở đây độ rộng tương đương là thước đo sai. Góc đặc hiệu dụng của mẫu bức xạ ăng ten, bằng $4\\pi$ chia hướng tính, là độ rộng tương đương tổng quát hóa sang hai chiều (tr. 167).||"
                 "Equivalent width is not always the best measure. For the bandwidth of a filter or the beamwidth of an antenna the \"width to half power\" is common, and by that measure the second example of Fig. 8.9 is narrower, agreeing with experience (p. 167). A paradox: a localised turbulent motion spreads outward in space while its spectrum spreads to higher wavenumbers; here equivalent width is the wrong measure. The effective solid angle of an antenna pattern, equal to $4\\pi$ over directivity, is the equivalent width generalised to two dimensions (p. 167).⟧</p>"),
                ("⟦Độ rộng tự tương quan||Autocorrelation width⟧",
                 "<p>⟦Độ rộng tự tương quan là độ rộng tương đương của hàm tự tương quan: $W_{f\\star f}=\\dfrac{\\int f\\star f\\,dx}{(f\\star f)(0)}=\\dfrac{|\\int f\\,dx|^2}{\\int|f|^2dx}$ (tr. 170). Nó không nhất thiết chỉ sự tập trung quanh gốc: hai hàm có cùng tự tương quan (hình 8.10) có cùng độ rộng tự tương quan nhưng khác độ rộng tương đương. Nếu xét xung chữ nhật thì độ rộng tương đương có thể sụp vì dời xung làm tung độ giữa về 0; độ rộng tự tương quan khắc phục điều này vì tự tương quan cực đại tại gốc và không bao giờ bằng 0. Số đo: $\\Pi$ dời 3 đơn vị có $W_{f\\star f}$ = {{aw_shift}} như khi chưa dời, còn $f(0)$ của nó bằng 0.||"
                 "The autocorrelation width is the equivalent width of the autocorrelation function: $W_{f\\star f}=\\dfrac{\\int f\\star f\\,dx}{(f\\star f)(0)}=\\dfrac{|\\int f\\,dx|^2}{\\int|f|^2dx}$ (p. 170). It does not necessarily refer to concentration about the origin: two functions with the same autocorrelation (Fig. 8.10) have the same autocorrelation width but different equivalent widths. For a rectangular pulse the equivalent width can break down simply from displacement because the central ordinate falls to zero; autocorrelation width avoids this since the autocorrelation is maximal at the origin, never zero. Measured: $\\Pi$ shifted by 3 units has $W_{f\\star f}$ = {{aw_shift}} as before the shift, while its $f(0)$ is 0.⟧</p>"),
                ("⟦Liên hệ với phổ công suất||Relation to the power spectrum⟧",
                 "<p>⟦Từ tính nghịch đảo, độ rộng tự tương quan của một hàm là nghịch đảo độ rộng tương đương của phổ công suất $|F|^2$; và nghịch đảo độ rộng tự tương quan của biến đổi là độ rộng tương đương của $|f|^2$ (tr. 170). Vì thế khái niệm này hỏng khi $|F|^2$ có tung độ giữa 0, tức khi hàm không có thành phần một chiều, như gói sóng (tr. 170). Số đo với $e^{-|x|}$: $W_{f\\star f}$ = {{aw_exp}}, và $1/W_{|F|^2}$ = {{aw_exp_ft}}, cùng kết quả bằng hai cách tính.||"
                 "From the reciprocity, the autocorrelation width of a function is the reciprocal of the equivalent width of its power spectrum $|F|^2$; and the reciprocal of the autocorrelation width of the transform is the equivalent width of $|f|^2$ (p. 170). So the idea breaks down when $|F|^2$ has a zero central ordinate, i.e. when the function has no d.c. component, as for wave packets (p. 170). Measured with $e^{-|x|}$: $W_{f\\star f}$ = {{aw_exp}}, and $1/W_{|F|^2}$ = {{aw_exp_ft}}, the same result by two calculations.⟧</p>"),
                ("⟦Ưu điểm và giới hạn của độ rộng tự tương quan||Strengths and limits of autocorrelation width⟧",
                 "<p>⟦Hai hàm có cùng phổ công suất nhưng thành phần phổ trượt tới pha tương đối bất kỳ có cùng tự tương quan. Vậy $W_{f\\star f}$ (1) xử lý được việc hàm bị dời khỏi gốc và (2) xử lý được giao thoa pha nội tại làm tung độ giữa nhỏ. Nhưng trong hai hàm cùng phổ công suất, một hàm có thể hẹp, hàm kia rộng: trường nhiễu xạ Fresnel trên các mặt phẳng song song với khẩu độ chiếu sáng có cùng tự tương quan nhưng độ rộng chiếu sáng tăng theo khoảng cách (tr. 171). Trường hợp tiếng ồn trắng qua bộ lọc rồi chỉnh lưu: khoảng cách trung bình giữa các giá trị ra độc lập tỉ lệ nghịch với độ rộng tự tương quan của đặc tính công suất qua băng (tr. 171). Độ rộng tự tương quan cũng bất biến dưới xáo trộn (shuffling).||"
                 "Two functions with the same power spectrum, whose spectral components are slid into any relative phase, have the same autocorrelation. So $W_{f\\star f}$ (1) copes with displacement of the function from the origin and (2) copes with internal phase interference that gives a small central ordinate. But of two functions with the same power spectrum, one can be narrow and the other wide: Fresnel diffraction fields on planes parallel to an illuminated aperture have the same autocorrelation while the illuminated width grows with distance (p. 171). For white noise passed through a filter and rectified, the average interval between effectively independent output values is inversely proportional to the autocorrelation width of the power pass characteristic (p. 171). Autocorrelation width is also invariant under shuffling.⟧</p>"),
                ("⟦Tự kiểm tra phần 3||Self-check, part 3⟧",
                 UL(["⟦$W_f$ của $e^{-|x|}$ là bao nhiêu và $W_F$ là bao nhiêu?||What are $W_f$ and $W_F$ for $e^{-|x|}$?⟧",
                     "⟦Vì sao $\\Pi(x-3)$ có độ rộng tự tương quan nhưng không có độ rộng tương đương?||Why does $\\Pi(x-3)$ have an autocorrelation width but no equivalent width?⟧",
                     "⟦Khi nào độ rộng tự tương quan không xác định?||When is the autocorrelation width undefined?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: 2 và 1/2; vì $f(0)=0$ còn tự tương quan cực đại ở gốc; khi hàm có diện tích 0.||Hints: 2 and 1/2; because $f(0)=0$ while the autocorrelation peaks at the origin; when the function has zero area.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 4
        dict(
            title="⟦Độ rộng bình phương trung bình và hệ thức bất định||Mean-square widths and the uncertainty relation⟧",
            scr=("⟦Độ rộng tương đương và tự tương quan đều hỏng với tín hiệu dao động không có thành phần một chiều.||Equivalent width and autocorrelation width both fail for oscillatory signals with no d.c. component.⟧",
                 "⟦Muốn đo thời lượng của gói sóng, ta dùng phương sai của năng lượng $|f|^2$.||To measure the duration of a wave packet we use the variance of the energy distribution $|f|^2$.⟧",
                 "⟦Tích độ trải theo thời gian và tần số không thể nhỏ hơn $1/4\\pi$, và Gauss là dạng đạt giá trị tối thiểu.||The product of the spreads in time and frequency cannot be less than $1/4\\pi$, and the Gaussian attains the minimum.⟧"),
            preview=["⟦Độ rộng bình phương trung bình||Mean-square widths⟧", "⟦Bất đẳng thức Schwarz và các cận||Schwarz's inequality and bounds⟧", "⟦Hệ thức bất định||The uncertainty relation⟧"],
            slides=[
                ("⟦Khi các thước đo trước hỏng||When the earlier measures fail⟧",
                 "<p>⟦Độ rộng tương đương và tập trung vừa nêu không đủ mọi nhu cầu, nên còn các thước đo khác. Giá trị bình phương trung bình $\\langle x^2\\rangle=\\int x^2f/\\int f$ là thước đo rộng rãi, cũng như phương sai với hàm không nằm ở gốc: $\\langle(x-\\langle x\\rangle)^2\\rangle=\\langle x^2\\rangle-\\langle x\\rangle^2=\\dfrac{-F''(0)}{4\\pi^2F(0)}+\\dfrac{1}{4\\pi^2}\\left[\\dfrac{F'(0)}{F(0)}\\right]^2$ (tr. 171). Các thước đo này hỏng khi diện tích của hàm bằng 0 nên không dùng được cho tín hiệu dao động hay gói sóng (tr. 172).||"
                 "The equivalent width and concentration just described do not fill all needs, so other measures of width are also used. The mean-square value $\\langle x^2\\rangle=\\int x^2f/\\int f$ is widely appropriate, as is the variance for functions not centred on the origin: $\\langle(x-\\langle x\\rangle)^2\\rangle=\\langle x^2\\rangle-\\langle x\\rangle^2=\\dfrac{-F''(0)}{4\\pi^2F(0)}+\\dfrac{1}{4\\pi^2}\\left[\\dfrac{F'(0)}{F(0)}\\right]^2$ (p. 171). These measures break down when the area of the function is zero and are therefore inappropriate for oscillatory signals or wave packets (p. 172).⟧</p>"),
                ("⟦Phương sai của mô đun bình phương||The variance of the squared modulus⟧",
                 "<p>⟦Để đối phó, ta nghĩ theo mật độ năng lượng $|f|^2$: tâm khối và phương sai của phân bố năng lượng, gọi là phương sai của mô đun bình phương $(\\Delta x)^2=\\dfrac{\\int(x-\\bar x)^2|f|^2dx}{\\int|f|^2dx}$ (tr. 172). Biểu thức có vẻ phức tạp cho ý niệm đơn giản về thời lượng hay độ rộng băng của gói tín hiệu, nhưng hành xử hợp lý hơn với nhiều mục đích. Tuy vậy $|f|^2$ có thể không có phương sai hữu hạn: $\\text{sinc}\\,x$ và $(x^2+1)^{-1}$, hai hàm nhọn tập trung với độ rộng tương đương và tự tương quan hợp lý, lại rộng vô hạn theo phương sai (tr. 172). Vì vậy phải thận trọng trước khi cho rằng độ rộng dựa trên phương sai khớp cảm nhận trực giác.||"
                 "To cope, we think in terms of the energy density $|f|^2$: the centroid and variance of the energy distribution, called the variance of the squared modulus, $(\\Delta x)^2=\\dfrac{\\int(x-\\bar x)^2|f|^2dx}{\\int|f|^2dx}$ (p. 172). This may seem an elaborate expression for the simple idea of the duration or bandwidth of a signal packet, but it behaves more reasonably for many purposes. However $|f|^2$ may not have finite variance: $\\text{sinc}\\,x$ and $(x^2+1)^{-1}$, two concentrated peaked functions with reasonable equivalent and autocorrelation widths, show up as infinitely broad on a variance basis (p. 172). Caution is therefore needed before assuming that widths based on variance relate to intuitive ideas of width.⟧</p>"),
                ("⟦Cận trên của tung độ||An upper limit to the ordinate⟧",
                 "<p>⟦Một hàm có thể lớn tới đâu? Từ $f(x)=\\int F(s)e^{i2\\pi xs}ds$ ta có $|f(x)|\\le\\int|F(s)|ds$ (tr. 174). Trên mặt phẳng phức của $f(x)$, tích phân Fourier tại một $x$ là một cung có độ dài $\\int|F|ds$ không đổi theo $x$; giá trị lớn nhất $|f|$ có thể nhận là khi cung duỗi thẳng, tức mọi thành phần cùng pha. Số đo với Gauss dịch $f(x)=e^{-\\pi(x-0.5)^2}$: $|f(0)|$ = {{ineq_f}} còn $\\int|F|ds$ = {{ineq_bound}}; dấu bằng đạt tại $x=0.5$ nơi mọi thành phần cùng pha, với $f(0.5)$ = {{ineq_peak}}.||"
                 "How large can a function become? From $f(x)=\\int F(s)e^{i2\\pi xs}ds$ we get $|f(x)|\\le\\int|F(s)|ds$ (p. 174). On the complex plane of $f(x)$ the Fourier integral at a given $x$ is an arc whose length $\\int|F|ds$ does not depend on $x$; the maximum $|f|$ can reach is when the arc straightens, i.e. all components come into phase. Measured with the shifted Gaussian $f(x)=e^{-\\pi(x-0.5)^2}$: $|f(0)|$ = {{ineq_f}} while $\\int|F|ds$ = {{ineq_bound}}; equality is reached at $x=0.5$, where all components are in phase, with $f(0.5)$ = {{ineq_peak}}.⟧</p>"
                 + F("⟦Cận tung độ||Ordinate bound⟧", r"|f(x)|\le\int_{-\infty}^{\infty}|F(s)|\,ds")),
                ("⟦Cận trên của độ dốc||An upper limit to the slope⟧",
                 "<p>⟦Thành phần $F(s)e^{i2\\pi xs}ds$ có độ dốc $i2\\pi sF(s)e^{i2\\pi xs}ds$, và xét khả năng mọi thành phần đạt độ dốc lớn nhất cùng lúc: $|f'(x)|\\le2\\pi\\int|sF(s)|ds$ (tr. 176). Hai bất đẳng thức đều xuất phát từ hiện tượng hình học: cung nối hai điểm lớn hơn hoặc bằng dây cung, tức hai cạnh của tam giác không nhỏ hơn cạnh thứ ba, $|A+B|\\le|A|+|B|$ (tr. 176). Số đo với Gauss: $\\max|f'|$ = {{sl_max}} và cận {{sl_bound}}.||"
                 "The component $F(s)e^{i2\\pi xs}ds$ has slope $i2\\pi sF(s)e^{i2\\pi xs}ds$, and considering the possibility of all components reaching maximum slope together: $|f'(x)|\\le2\\pi\\int|sF(s)|ds$ (p. 176). Both inequalities stem from the geometric fact that an arc joining two points is at least as long as the chord, i.e. two sides of a triangle together are at least the third, $|A+B|\\le|A|+|B|$ (p. 176). Measured with the Gaussian: $\\max|f'|$ = {{sl_max}} and the bound {{sl_bound}}.⟧</p>"
                 + F("⟦Cận độ dốc||Slope bound⟧", r"|f'(x)|\le 2\pi\int_{-\infty}^{\infty}|s\,F(s)|\,ds")),
                ("⟦Bất đẳng thức Schwarz||Schwarz's inequality⟧",
                 "<p>⟦Với hai hàm thực $f$ và $g$ trên $a\\le x\\le b$: $\\left[\\int fg\\,dx\\right]^2\\le\\int f^2dx\\int g^2dx$. Bản tổng quát cho hàm phức: $\\left|\\int(F^*G+FG^*)dx\\right|^2\\le4\\int FF^*dx\\int GG^*dx$ (tr. 176). Chứng minh: xét $0\\le\\int(F+\\epsilon G)(F+\\epsilon G)^*dx$ là tam thức bậc hai theo $\\epsilon$ thực, mà điều kiện không có nghiệm thực là $b^2-4ac\\le0$. Tương tự bất đẳng thức vector $\\mathbf A\\cdot\\mathbf B\\le AB$. Số đo với $f=\\Lambda$ và $g=e^{-|x|}$: $(\\int fg)^2$ = {{schw_l}} $\\le\\int f^2\\int g^2$ = {{schw_r}}.||"
                 "For two real functions $f$ and $g$ on $a\\le x\\le b$: $\\left[\\int fg\\,dx\\right]^2\\le\\int f^2dx\\int g^2dx$. The general form for complex functions: $\\left|\\int(F^*G+FG^*)dx\\right|^2\\le4\\int FF^*dx\\int GG^*dx$ (p. 176). Proof: consider $0\\le\\int(F+\\epsilon G)(F+\\epsilon G)^*dx$, a quadratic in real $\\epsilon$, which has no real zero if $b^2-4ac\\le0$. It is the analogue of the vector inequality $\\mathbf A\\cdot\\mathbf B\\le AB$. Measured with $f=\\Lambda$ and $g=e^{-|x|}$: $(\\int fg)^2$ = {{schw_l}} $\\le\\int f^2\\int g^2$ = {{schw_r}}.⟧</p>"),
                ("⟦Hệ thức bất định: phát biểu||The uncertainty relation: statement⟧",
                 "<p>⟦Tích độ rộng băng và thời lượng của tín hiệu không thể nhỏ hơn một giá trị tối thiểu; đó là hiện tượng toán học gắn với sự phụ thuộc lẫn nhau giữa thời gian và tần số, chặn việc chỉ định tùy ý cả hàm theo thời gian và phổ. Một diện tích hữu hạn của mặt phẳng thời gian tần số chỉ chứa một số hữu hạn dữ liệu độc lập (tr. 177). Với độ rộng tương đương, $W_fW_F=1$ luôn; với độ rộng tự tương quan tích cũng xác định; nhưng với độ rộng bình phương trung bình tích không hằng và có thể từ 0 tới vô hạn (tr. 177). Với phương sai $(\\Delta x)^2$ của $|f|^2$ và $(\\Delta s)^2$ của $|F|^2$:||"
                 "The bandwidth-duration product of a signal cannot be less than a certain minimum; it is a mathematical phenomenon bound up with the interdependence of time and frequency, which prevents arbitrary specification of both function and spectrum. A finite area of the time-frequency plane can contain only a finite number of independent data (p. 177). For equivalent widths $W_fW_F=1$ always; for autocorrelation widths the product is also determined; but for mean-square widths the product is not constant and can range from zero to infinity (p. 177). With the variance $(\\Delta x)^2$ of $|f|^2$ and $(\\Delta s)^2$ of $|F|^2$:⟧</p>"
                 + F("⟦Hệ thức bất định||Uncertainty relation⟧", r"\Delta x\,\Delta s\ \ge\ \frac{1}{4\pi}")),
                ("⟦Chứng minh||The proof⟧",
                 "<p>⟦Dùng định lý $\\int f'f'^*dx=4\\pi^2\\int s^2FF^*ds$ (định lý đạo hàm với Rayleigh), Schwarz và tích phân từng phần $\\int xf\\,f'dx=-\\tfrac12\\int f^2dx$ (tr. 177 đến 178). Với $f$ và $F$ đặt tâm ở tâm khối, $(\\Delta x)^2(\\Delta s)^2=\\dfrac{\\int x^2ff^*dx\\ \\int s^2FF^*ds}{\\int ff^*dx\\ \\int FF^*ds}\\ge\\dfrac{1}{16\\pi^2}$, tức $\\Delta x\\,\\Delta s\\ge\\dfrac1{4\\pi}$. Dấu bằng chỉ khi $f'\\propto xf$, tức Gauss.||"
                 "Use the theorem $\\int f'f'^*dx=4\\pi^2\\int s^2FF^*ds$ (derivative theorem with Rayleigh), Schwarz, and integration by parts $\\int xf\\,f'dx=-\\tfrac12\\int f^2dx$ (pp. 177 to 178). With $f$ and $F$ centred on their centroids, $(\\Delta x)^2(\\Delta s)^2=\\dfrac{\\int x^2ff^*dx\\ \\int s^2FF^*ds}{\\int ff^*dx\\ \\int FF^*ds}\\ge\\dfrac{1}{16\\pi^2}$, i.e. $\\Delta x\\,\\Delta s\\ge\\dfrac1{4\\pi}$. Equality only when $f'\\propto xf$, i.e. a Gaussian.⟧</p>"),
                ("⟦Ví dụ: Gauss đạt cực tiểu, mũ hai phía thì không||Example: the Gaussian attains the minimum, the two-sided exponential does not⟧",
                 "<p>⟦Với $f=\\exp(-\\pi a^2x^2)$, $|f|^2$ có phương sai $1/4\\pi a^2$ và $|F|^2$ có phương sai $a^2/4\\pi$, nên $\\Delta x\\,\\Delta s=1/4\\pi$ đúng bằng giá trị cực tiểu (tr. 179). Số đo ($a=1$): {{un_gauss}}, cả từ tích phân trực tiếp lẫn công thức. Với $f=e^{-|x|}$: $\\Delta x=$ {{un_dx}}, $\\Delta s=$ {{un_ds}}, tích {{un_exp}}, lớn hơn cực tiểu {{un_min}} khoảng {{un_ratio}} lần.||"
                 "For $f=\\exp(-\\pi a^2x^2)$, $|f|^2$ has variance $1/4\\pi a^2$ and $|F|^2$ has variance $a^2/4\\pi$, so $\\Delta x\\,\\Delta s=1/4\\pi$, exactly the minimum (p. 179). Measured ($a=1$): {{un_gauss}}, both by direct integration and by the formula. For $f=e^{-|x|}$: $\\Delta x=$ {{un_dx}}, $\\Delta s=$ {{un_ds}}, product {{un_exp}}, larger than the minimum {{un_min}} by a factor of about {{un_ratio}}.⟧</p>{{fig:uncertainty}}"),
                ("⟦Vật lý: xung radar và các cách đo độ rộng băng||Physics: a radar pulse and ways to measure bandwidth⟧",
                 "<p>⟦Bracewell xét bộ phát radar phát xung 1 micrô giây ở 10 000 MHz; hệ thức bất định cho $\\Delta t\\,\\Delta f\\ge1/4\\pi$, tức $\\Delta f\\ge$ {{un_radar}} Hz nếu $\\Delta t=1\\ \\mu$s. Nhưng kinh nghiệm với máy thu cho thấy băng thông 1 MHz là lựa chọn tối ưu để dò xung ấy, nên hệ thức chỉ là cận dưới, xa thực tế. Ông cũng chỉ ra rằng tích $\\Delta t\\,D f$ với $Df$ là độ rộng của phổ công suất dương (chỉ $f>0$) không bị chặn bởi $1/4\\pi$ (Uffink và Hilgevoord, 1985, 1988): ví dụ $s(t)=\\exp(-\\alpha t^2)\\cos2\\pi f_0t$ cho tích $0.400\\times(1/4\\pi)$, dưới giới hạn lượng tử (tr. 180). Bài học: chọn đúng định nghĩa độ rộng trước khi phát biểu giới hạn.||"
                 "Bracewell considers a radar transmitter emitting a 1-microsecond pulse at 10,000 MHz; the uncertainty relation gives $\\Delta t\\,\\Delta f\\ge1/4\\pi$, i.e. $\\Delta f\\ge$ {{un_radar}} Hz for $\\Delta t=1\\ \\mu$s. But experience with receivers shows a bandwidth of 1 MHz is the optimum choice for detecting such a pulse, so the relation is only a lower limit, far from practice. He also points out that the product $\\Delta t\\,Df$, with $Df$ the width of the positive-frequency power spectrum ($f>0$ only), is not subject to the lower limit $1/4\\pi$ (Uffink and Hilgevoord, 1985, 1988): for example $s(t)=\\exp(-\\alpha t^2)\\cos2\\pi f_0t$ gives a product $0.400\\times(1/4\\pi)$, below the quantum limit (p. 180). Lesson: pick the right definition of width before stating a limit.⟧</p>"),
                ("⟦Tự kiểm tra phần 4||Self-check, part 4⟧",
                 UL(["⟦Dạng hàm nào đạt cực tiểu $\\Delta x\\,\\Delta s=1/4\\pi$?||Which function shape attains the minimum $\\Delta x\\,\\Delta s=1/4\\pi$?⟧",
                     "⟦Khi nào cận $|f|\\le\\int|F|$ đạt dấu bằng?||When does the bound $|f|\\le\\int|F|$ reach equality?⟧",
                     "⟦Vì sao phương sai của $|f|^2$ với $f=\\text{sinc}\\,x$ là vô hạn?||Why is the variance of $|f|^2$ infinite for $f=\\text{sinc}\\,x$?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: Gauss; khi mọi thành phần cùng pha tại $x$ đó; vì $\\text{sinc}^2x$ chỉ tắt như $x^{-2}$ nên $x^2\\text{sinc}^2x$ không khả tích.||Hints: the Gaussian; when all components are in phase at that $x$; because $\\text{sinc}^2x$ only decays as $x^{-2}$ so $x^2\\text{sinc}^2x$ is not integrable.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 5
        dict(
            title="⟦Sai phân, trung bình trượt, giới hạn trung tâm và tổng kết||Differences, running means, the central limit and the summary⟧",
            scr=("⟦Dữ liệu thực thường được lập bảng tại các điểm rời rạc, và ta hay làm trơn nó bằng trung bình trượt.||Real data are tabulated at discrete points and often smoothed by running means.⟧",
                 "⟦Hai thao tác này ứng với phép nhân nào ở miền biến đổi?||What multiplication in the transform domain does each correspond to?⟧",
                 "⟦Sai phân nhân với $2i\\sin\\pi as$, trung bình trượt nhân với $\\text{sinc}\\,as$, và tích chập nhiều lần đưa tới Gauss.||Differencing multiplies by $2i\\sin\\pi as$, running means multiply by $\\text{sinc}\\,as$, and repeated convolution approaches a Gaussian.⟧"),
            preview=["⟦Sai phân hữu hạn||Finite differences⟧", "⟦Trung bình trượt||Running means⟧", "⟦Định lý giới hạn trung tâm và bảng 8.5||The central-limit theorem and Table 8.5⟧"],
            slides=[
                ("⟦Sai phân hữu hạn||The finite difference⟧",
                 "<p>⟦Sai phân hữu hạn của $f(x)$ lấy trên khoảng $a$ là $\\Delta_af(x)=f(x+\\tfrac12a)-f(x-\\tfrac12a)$ (Bracewell, tr. 180). Nó thường gặp với hàm chỉ có giá trị ở điểm rời rạc, nhưng cũng lấy được với hàm xác định mọi $x$. Khi $a$ nhỏ, $\\Delta_af$ nhỏ nhưng tiệm cận tỉ lệ với đạo hàm; khi $a$ lớn, $\\Delta_af$ có thể tách thành một bản $f(x)$ dịch, tiếp theo là một bản đảo dấu (hình 8.15 và 8.16). Đó là tích chập: $\\Delta_af=\\big[\\delta(x+\\tfrac a2)-\\delta(x-\\tfrac a2)\\big]*f$, cặp xung lẻ (tr. 182).||"
                 "The finite difference of $f(x)$ over the interval $a$ is $\\Delta_af(x)=f(x+\\tfrac12a)-f(x-\\tfrac12a)$ (Bracewell, p. 180). It is often met with functions tabulated at discrete intervals but can also be taken for functions defined for all $x$. When $a$ is small, $\\Delta_af$ is small but approaches proportionality to the derivative; when $a$ is large, $\\Delta_af$ may separate into a displaced $f(x)$ followed by an inverted one (Figs. 8.15 and 8.16). It is a convolution: $\\Delta_af=\\big[\\delta(x+\\tfrac a2)-\\delta(x-\\tfrac a2)\\big]*f$, the odd impulse pair (p. 182).⟧</p>"),
                ("⟦Biến đổi của sai phân||The transform of a difference⟧",
                 "<p>⟦Biến đổi của cặp xung lẻ đã biết nên theo định lý tích chập, biến đổi của $\\Delta_af$ là $2i\\sin(\\pi as)F(s)$ (tr. 183). Sai phân trên khoảng rộng nhân biến đổi với sóng sin tần số cao; khoảng nhỏ nhân với sóng sin tần số thấp; khoảng nhỏ hơn cả cấu trúc mịn nhất thì sóng sin thành hàm tuyến tính của $s$. Liên hệ với đạo hàm: $\\lim_{a\\to0}\\dfrac{2i\\sin\\pi as}{a}=i2\\pi s$. Số đo với Gauss, $a=0.5$, $s=0.3$: $|\\text{FT}[\\Delta_af]|$ = {{fd_mag}} bằng $2\\sin(\\pi as)F$ (tích phân số và công thức). Với $a=10^{-3}$, $\\Delta_af/a$ lệch $f'$ chỉ {{fd_lim}} (tương đối).||"
                 "The transform of the odd impulse pair is known, so by the convolution theorem the transform of $\\Delta_af$ is $2i\\sin(\\pi as)F(s)$ (p. 183). Differencing over a wide interval multiplies the transform by a high-frequency sinusoid; over a small interval, by a low-frequency sinusoid; for an interval shorter than the finest structure the sinusoid is effectively a linear function of $s$. Connection with differentiation: $\\lim_{a\\to0}\\dfrac{2i\\sin\\pi as}{a}=i2\\pi s$. Measured with the Gaussian, $a=0.5$, $s=0.3$: $|\\text{FT}[\\Delta_af]|$ = {{fd_mag}}, equal to $2\\sin(\\pi as)F$ (numerical integration and formula). With $a=10^{-3}$, $\\Delta_af/a$ differs from $f'$ by only {{fd_lim}} (relative).⟧</p>"
                 + F("⟦Sai phân||Difference⟧", r"\Delta_af(x)\ \supset\ 2i\sin(\pi as)\,F(s)")),
                ("⟦Sai phân bậc hai||The second difference⟧",
                 "<p>⟦Sai phân bậc hai $\\Delta_a^2f(x)=f(x+a)-2f(x)+f(x-a)$ là sai phân của sai phân, ứng với hai lần nhân $2i\\sin\\pi as$, nên biến đổi là $-4\\sin^2(\\pi as)F(s)$. Diễn giải hình học: sai phân bậc một tỉ lệ với độ dốc trung bình, sai phân bậc hai với độ cong trung bình trên các khoảng hữu hạn (hình 8.19, tr. 184). Số đo tại cùng điểm: độ lớn {{fd2_mag}}.||"
                 "The second difference $\\Delta_a^2f(x)=f(x+a)-2f(x)+f(x-a)$ is the difference of the difference, corresponding to two multiplications by $2i\\sin\\pi as$, so its transform is $-4\\sin^2(\\pi as)F(s)$. Geometrically the first difference is proportional to the average slope and the second to the average curvature over finite intervals (Fig. 8.19, p. 184). Measured at the same point: magnitude {{fd2_mag}}.⟧</p>"
                 + F("⟦Sai phân bậc hai||Second difference⟧", r"\Delta_a^2f(x)\ \supset\ -4\sin^2(\pi as)\,F(s)")),
                ("⟦Trung bình trượt||Running means⟧",
                 "<p>⟦Trong xử lý số liệu khí tượng như lượng mưa, các dao động ngày này qua ngày khác không quan trọng được làm trơn bằng trung bình trượt để lộ xu hướng theo mùa. Trung bình trượt của $f$ trên khoảng $a$ là $a^{-1}\\Pi(x/a)*f(x)$ (tr. 184 đến 185). Vì biến đổi của $a^{-1}\\Pi(x/a)$ là $\\text{sinc}\\,as$, biến đổi của trung bình trượt là $\\text{sinc}(as)F(s)$: trung bình trượt ứng với phép nhân với $\\text{sinc}\\,as$. Số đo với Gauss $a=1$, $s=0.3$: trung bình trượt tính bằng hàm sai số rồi biến đổi cho {{rm_03}}, bằng $\\text{sinc}(as)F$.||"
                 "In reducing meteorological data such as rainfall, unimportant day-to-day fluctuations are smoothed out with running means to reveal the seasonal trend. The running mean of $f$ over the interval $a$ is $a^{-1}\\Pi(x/a)*f(x)$ (pp. 184 to 185). Since the transform of $a^{-1}\\Pi(x/a)$ is $\\text{sinc}\\,as$, the transform of the running mean is $\\text{sinc}(as)F(s)$: taking running means corresponds to multiplication by $\\text{sinc}\\,as$. Measured with the Gaussian, $a=1$, $s=0.3$: the running mean computed with the error function and then transformed gives {{rm_03}}, equal to $\\text{sinc}(as)F$.⟧</p>"
                 + F("⟦Trung bình trượt||Running mean⟧", r"\frac1a\Pi\!\left(\frac xa\right)*f(x)\ \supset\ \operatorname{sinc}(as)\,F(s)")),
                ("⟦Trung bình trượt bậc cao||Higher-order running means⟧",
                 "<p>⟦Trung bình trượt bậc hai (áp dụng hai lần) có biến đổi $\\text{sinc}^2as\\,F(s)$, và vì $\\text{sinc}^2as$ là biến đổi của $a^{-1}\\Lambda(x/a)$, đó là trung bình trượt có trọng số tam giác. Tổng quát: $n$ lần cho $\\text{sinc}^nas$ (hình 8.20, tr. 186). Số đo: $\\text{sinc}^2(as)F$ tại $s=0.3$ là {{rm2_03}}. Khi $a\\to0$, $\\text{sinc}\\,as\\to1$ (trung bình trượt tiến về hàm gốc); khi $a\\to\\infty$, $\\text{sinc}\\,as\\to a^{-1}\\delta(s)$ (chỉ còn giá trị trung bình toàn cục).||"
                 "The second-order running mean (applied twice) has transform $\\text{sinc}^2as\\,F(s)$, and since $\\text{sinc}^2as$ is the transform of $a^{-1}\\Lambda(x/a)$ it is a triangle-weighted running mean. In general $n$ applications give $\\text{sinc}^nas$ (Fig. 8.20, p. 186). Measured: $\\text{sinc}^2(as)F$ at $s=0.3$ is {{rm2_03}}. As $a\\to0$, $\\text{sinc}\\,as\\to1$ (the running mean tends to the original); as $a\\to\\infty$, $\\text{sinc}\\,as\\to a^{-1}\\delta(s)$ (only the global mean survives).⟧</p>"),
                ("⟦Định lý giới hạn trung tâm||The central-limit theorem⟧",
                 "<p>⟦Nếu nhiều hàm được tích chập với nhau, kết quả có thể rất trơn và, khi số hàm tăng vô hạn, có thể tiến về dạng Gauss; phát biểu chặt chẽ là định lý giới hạn trung tâm (tr. 186). Ví dụ: gần $s=0$, $\\text{sinc}\\,s\\approx1-\\pi^2s^2/6$ nên profile thứ $n$ xấp xỉ $(1-\\pi^2s^2/6)^n\\to e^{-n\\pi^2s^2/6}$, Gauss ngày càng hẹp (rộng tỉ lệ $n^{-1/2}$); biến đổi ngược của nó là Gauss ngày càng rộng, phương sai tăng tỉ lệ $n$, hệ quả của phương sai cộng dưới tích chập. Số đo: $n=10$, $s=0.2$: $\\text{sinc}^{10}(0.2)$ = {{clt_10}} và Gauss {{clt_g}}.||"
                 "If a large number of functions are convolved, the result may be very smooth and, as the number increases indefinitely, may approach Gaussian form; the rigorous statement is the central-limit theorem (p. 186). Example: near $s=0$, $\\text{sinc}\\,s\\approx1-\\pi^2s^2/6$ so the $n$th profile is approximated by $(1-\\pi^2s^2/6)^n\\to e^{-n\\pi^2s^2/6}$, a Gaussian that keeps narrowing (width varying as $n^{-1/2}$); its inverse transform is a Gaussian that keeps widening, its variance growing in proportion to $n$, a consequence of variances adding under convolution. Measured: $n=10$, $s=0.2$: $\\text{sinc}^{10}(0.2)$ = {{clt_10}} and the Gaussian {{clt_g}}.⟧</p>{{fig:clt}}"),
                ("⟦Kiểm bằng số: tổng của các đồng đều||Numerical test: sums of uniform distributions⟧",
                 "<p>⟦Tích chập $n$ chữ nhật đơn vị: phương sai $n/12$ (cộng) và độ nhọn dư $-6/5n$ tiến về 0, đặc trưng của Gauss. Số đo với $n=4$: phương sai {{clt_var}} và độ nhọn dư {{clt_kurt}}. Bracewell cũng gợi ý thử các tích nối tiếp như $\\{1\\ 1\\}^{*n}$: với $n=20$, hệ số giữa là {{clt_bin}} (nhị thức) so với Gauss {{clt_bin_g}}.||"
                 "Convolving $n$ unit rectangles: variance $n/12$ (adding) and excess kurtosis $-6/5n$ tending to 0, the Gaussian signature. Measured with $n=4$: variance {{clt_var}} and excess kurtosis {{clt_kurt}}. Bracewell also suggests trying serial products such as $\\{1\\ 1\\}^{*n}$: with $n=20$ the central coefficient is {{clt_bin}} (binomial) against the Gaussian {{clt_bin_g}}.⟧</p>"),
                ("⟦Điều kiện áp dụng||Conditions of applicability⟧",
                 "<p>⟦Điều cốt yếu là biến đổi của mỗi hàm phải có dạng \"có bướu\" tại gốc: $a-bs^2$. Hệ số $a$ khác 0, hữu hạn (không hàm nào có diện tích 0, vì tích các biến đổi sẽ bằng 0 tại $s=0$); $b$ hữu hạn, thỉnh thoảng bằng 0 cũng được. Không có nhân tử nào giống $\\Lambda(s)$ tại gốc vì nó để lại một góc vĩnh viễn (tr. 188). Trong miền $x$: diện tích $0<\\int f<\\infty$, $\\int xf$ hữu hạn (đặt gốc ở tâm khối), $\\int x^2f<\\infty$ (tr. 188). Không phải mọi hàm đều đi tới Gauss: $\\Pi(x)\\sin2\\pi x$ thì không, nhưng nhiều hàm không đối xứng như $e^{-x}H(x)$ và các hàm gián đoạn như $\\Pi$ thì có,. Nếu một biến đổi có không điểm ở $s_1$ hữu hạn thì tích cũng bằng 0 ở đó và không thể chính xác Gauss, dù thực tế gần (tr. 188 đến 190).||"
                 "The essential thing is that the transform of each function should have a \"humped\" behaviour at the origin: $a-bs^2$. The coefficient $a$ must be nonzero and finite (no function may have zero area, or the product of transforms would be zero at $s=0$); $b$ must be finite, occasionally zero is fine. No factor should resemble $\\Lambda(s)$ at the origin since it would leave a permanent corner (p. 188). In the $x$ domain: $0<\\int f<\\infty$, $\\int xf$ finite (put the origin at the centroid), $\\int x^2f<\\infty$ (p. 188). Not all functions go to Gaussian: $\\Pi(x)\\sin2\\pi x$ does not, but many unsymmetrical functions such as $e^{-x}H(x)$ and discontinuous ones such as $\\Pi$ do. If one transform falls to zero at a finite $s_1$ the product has a zero too and cannot be exactly Gaussian, although in practice it may be indistinguishable (pp. 188 to 190).⟧</p>"),
                ("⟦Lấy mẫu rồi nhân bản giao hoán với nhân bản rồi lấy mẫu||Sampling and replication commute⟧",
                 "<p>⟦Nếu nhân bản một hàm ở khoảng $X$ (nguyên) rồi lấy mẫu ở khoảng đơn vị thì được cùng kết quả như lấy mẫu rồi nhân bản tập mẫu ở khoảng $X$ (tr. 172 đến 174). Viết bằng toán tử: $X^{-1}\\text{III}(x/X)*[\\text{III}(x)\\,f(x)]=\\text{III}(x)\\,[X^{-1}\\text{III}(x/X)*f(x)]$. Không áp dụng cho hàm như $(1+x^2)^{-1}$ vì tổng nhân bản không tồn tại. Số đo với Gauss rộng, $X=4$: hai thứ tự cho kết quả lệch {{sr_dev}}.||"
                 "If we replicate a function at integer interval $X$ and then sample at unit interval, we get the same result as sampling first and then replicating the sample set at interval $X$ (pp. 172 to 174). In operator form: $X^{-1}\\text{III}(x/X)*[\\text{III}(x)\\,f(x)]=\\text{III}(x)\\,[X^{-1}\\text{III}(x/X)*f(x)]$. It does not apply to functions like $(1+x^2)^{-1}$ for which the replication sum does not exist. Measured with a wide Gaussian, $X=4$: the two orders differ by {{sr_dev}}.⟧</p>"),
                ("⟦Bảng 8.5: tóm tắt các tương ứng||Table 8.5: summary of correspondences⟧",
                 TBL(["⟦Miền hàm||Function domain⟧", "⟦Miền biến đổi||Transform domain⟧"],
                     [["$\\int f\\,dx$", "$F(0)$"], ["$\\int xf\\,dx$", "$F'(0)/(-2\\pi i)$"], ["$\\langle x\\rangle$", "$F'(0)/(-2\\pi iF(0))$"], ["$\\int x^2f\\,dx$", "$-F''(0)/4\\pi^2$"],
                      ["$\\langle x^2\\rangle$", "$-F''(0)/(4\\pi^2F(0))$"], ["$\\sigma^2_{f*g}$", "$\\sigma^2_f+\\sigma^2_g$"], ["$W_f$", "$1/W_F$"], ["$|f(x)|\\le$", "$\\int|F|ds$"],
                      ["$\\Delta_af$", "$2i\\sin(\\pi as)F$"], ["$a^{-1}\\Pi(x/a)*f$", "$\\text{sinc}(as)F$"], ["⟦Đạo hàm bậc $k$ là xung||$k$th derivative impulsive⟧", "$F\\sim|s|^{-k}$"], ["⟦Nhiều tích chập||Many convolutions⟧", "⟦Gauss (giới hạn trung tâm)||Gaussian (central limit)⟧"]])),
                ("⟦Tự kiểm tra phần 5||Self-check, part 5⟧",
                 UL(["⟦Biến đổi của sai phân bậc hai?||What is the transform of the second difference?⟧",
                     "⟦Vì sao không hàm nào tham gia giới hạn trung tâm được có diện tích 0?||Why may no function in the central-limit convolution have zero area?⟧",
                     "⟦Trung bình trượt bậc hai ứng với nhân với gì?||What does a second-order running mean correspond to?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: $-4\\sin^2(\\pi as)F$; vì tích các biến đổi sẽ bằng 0 tại $s=0$; $\\text{sinc}^2as$.||Hints: $-4\\sin^2(\\pi as)F$; because the product of transforms would be zero at $s=0$; $\\text{sinc}^2as$.⟧</p>"),
            ]),
    ],
    takeaways=[
        "⟦Diện tích bằng tung độ giữa; mômen bậc $n$ bằng $F^{(n)}(0)/(-2\\pi i)^n$; tâm khối là độ dốc giữa chia tung độ giữa.||The area equals the central ordinate; the $n$th moment is $F^{(n)}(0)/(-2\\pi i)^n$; the centroid is the central slope over the central ordinate.⟧",
        "⟦Phương sai, bình phương trung bình và độ trơn đều cộng dưới tích chập; đạo hàm bậc $k$ là xung thì biến đổi tắt như $|s|^{-k}$.||Variance, mean-square and smoothness all add under convolution; a $k$th derivative that is impulsive makes the transform decay as $|s|^{-k}$.⟧",
        "⟦Độ rộng tương đương của hàm bằng nghịch đảo độ rộng tương đương của biến đổi; độ rộng tự tương quan bền hơn.||The equivalent width of a function is the reciprocal of that of its transform; the autocorrelation width is more robust.⟧",
        "⟦Hệ thức bất định $\\Delta x\\,\\Delta s\\ge1/4\\pi$ dùng phương sai của $|f|^2$, và Gauss đạt cực tiểu.||The uncertainty relation $\\Delta x\\,\\Delta s\\ge1/4\\pi$ uses the variance of $|f|^2$, and the Gaussian attains the minimum.⟧",
        "⟦Sai phân nhân $2i\\sin\\pi as$, trung bình trượt nhân $\\text{sinc}\\,as$, và tích chập lặp đưa tới Gauss.||Differencing multiplies by $2i\\sin\\pi as$, running means multiply by $\\text{sinc}\\,as$, and repeated convolution leads to a Gaussian.⟧",
    ],
    history="<p>⟦Doetsch (1943) mô tả hình ảnh hai miền \"trên\" và \"dưới\". Khinchin (1934) nghiên cứu phần dư của định lý giới hạn trung tâm. Uffink và Hilgevoord (1985, 1988) chỉ ra rằng tích của thời lượng và độ rộng băng dương không bị chặn bởi giới hạn lượng tử. Wiener (1933/1993) và Abramowitz và Stegun (1964) nằm trong thư mục của chương (Bracewell, tr. 151, 187 đến 190).||"
            "Doetsch (1943) gave the picture of an \"upper\" and a \"lower\" domain. Khinchin (1934) studied the remainder in the central-limit theorem. Uffink and Hilgevoord (1985, 1988) showed that the product of duration and positive-frequency bandwidth is not bounded by the quantum limit. Wiener (1993 reprint) and Abramowitz and Stegun (1964) are in the chapter's bibliography (Bracewell, pp. 151, 187 to 190).⟧</p>",
    case="<p>⟦<b>Chọn thước đo độ rộng cho một xung mũ.</b> Xung $e^{-|x|}$ có độ rộng tương đương {{ew_exp}}, còn biến đổi $2/(1+4\\pi^2s^2)$ có {{ew_F_exp}}, tích {{ew_prod_exp}}. Độ rộng tự tương quan {{aw_exp}}. Nhưng theo hệ thức bất định $\\Delta x\\,\\Delta s$ = {{un_exp}}, lớn hơn cực tiểu Gauss {{un_min}} khoảng {{un_ratio}} lần: mũ hai phía không phải gói \"tối ưu\". Một kỹ sư chọn độ rộng băng cho bộ lọc sẽ cần biết mình đang dùng thước đo nào; sai lầm điển hình là trộn các thước đo (bài học của radar ở tr. 180).||"
          "<b>Choosing a width measure for an exponential pulse.</b> The pulse $e^{-|x|}$ has equivalent width {{ew_exp}}, and its transform $2/(1+4\\pi^2s^2)$ has {{ew_F_exp}}, product {{ew_prod_exp}}. The autocorrelation width is {{aw_exp}}. Yet by the uncertainty relation $\\Delta x\\,\\Delta s$ = {{un_exp}}, larger than the Gaussian minimum {{un_min}} by a factor of about {{un_ratio}}: the two-sided exponential is not an \"optimal\" packet. An engineer choosing a filter bandwidth needs to know which measure is in use; the typical mistake is mixing measures (the radar lesson, p. 180).⟧</p>",
    practice=[
        "⟦Mở notebook và chạy cell cài đặt.||Open the notebook and run the setup cell.⟧",
        "⟦Bài 1: kiểm định lý mômen với $f=x^2e^{-x}H(x)$ (tâm khối, phương sai) bằng hai cách.||Task 1: check the moment theorems with $f=x^2e^{-x}H(x)$ (centroid, variance) both ways.⟧",
        "⟦Bài 2: vẽ log-log biến đổi của $\\Pi$, $\\Lambda$ và $\\Pi*\\Pi*\\Pi$ và đọc độ dốc.||Task 2: plot the log-log transforms of $\\Pi$, $\\Lambda$ and $\\Pi*\\Pi*\\Pi$ and read the slopes.⟧",
        "⟦Bài 3: tính $\\Delta x\\,\\Delta s$ cho $\\text{sech}\\,\\pi x$ và so với Gauss.||Task 3: compute $\\Delta x\\,\\Delta s$ for $\\text{sech}\\,\\pi x$ and compare with the Gaussian.⟧",
        "⟦Bài 4: chạy $\\{1\\ 1\\}^{*n}$, $\\{1\\ 1\\ 1\\ 1\\}^{*n}$, $\\{3\\ 2\\ 1\\}^{*n}$ và vẽ log các số hạng theo bình phương khoảng cách từ tâm (gợi ý của sách, tr. 188).||Task 4: run $\\{1\\ 1\\}^{*n}$, $\\{1\\ 1\\ 1\\ 1\\}^{*n}$, $\\{3\\ 2\\ 1\\}^{*n}$ and plot the logarithms of the terms against the square of the distance from the centre (the book's suggestion, p. 188).⟧",
        "⟦Bài 5: thử sai phân bậc hai với $a$ khác nhau và ước lượng đạo hàm bậc hai.||Task 5: try second differences with various $a$ and estimate the second derivative.⟧",
    ],
    pitfalls=[
        "<b>⟦\"Hai hàm cùng độ rộng tự tương quan thì cùng hình dạng.\"||\"Two functions with the same autocorrelation width have the same shape.\"⟧</b><p>⟦Chỉ cần cùng phổ công suất: $\\Pi$ dời 3 đơn vị có $W_{f\\star f}$ = {{aw_shift}} như $\\Pi$ gốc (tr. 170 đến 171).||It suffices to have the same power spectrum: $\\Pi$ shifted by 3 has $W_{f\\star f}$ = {{aw_shift}}, same as the original $\\Pi$ (pp. 170 to 171).⟧</p>",
        "<b>⟦\"Độ rộng tương đương luôn tồn tại.\"||\"Equivalent width always exists.\"⟧</b><p>⟦Không tồn tại khi $f(0)=0$, ví dụ xung chữ nhật dời 3 đơn vị (tr. 165).||It does not exist when $f(0)=0$, e.g. a rectangle shifted by 3 units (p. 165).⟧</p>",
        "<b>⟦\"Gauss là kết quả của mọi tích chập lặp.\"||\"Every repeated convolution leads to a Gaussian.\"⟧</b><p>⟦Cần biến đổi có bướu tại gốc, diện tích khác 0, mômen bậc hai hữu hạn; $\\Pi(x)\\sin2\\pi x$ có diện tích 0 và không tiến tới Gauss (tr. 187 đến 188).||It needs a humped transform at the origin, nonzero area and finite second moment; $\\Pi(x)\\sin2\\pi x$ has zero area and does not approach a Gaussian (pp. 187 to 188).⟧</p>",
        "<b>⟦\"Hệ thức bất định áp dụng cho mọi định nghĩa độ rộng.\"||\"The uncertainty relation applies to every definition of width.\"⟧</b><p>⟦Chỉ với phương sai của $|f|^2$ và $|F|^2$ (cận $1/4\\pi$); với độ rộng phổ dương $Df$ tích có thể nhỏ hơn (tr. 180).||Only for the variances of $|f|^2$ and $|F|^2$ (bound $1/4\\pi$); with the positive-frequency width $Df$ the product can be smaller (p. 180).⟧</p>",
    ],
    refs=[
        "⟦R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chương 8 (tr. 151 đến 198).||R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chapter 8 (pp. 151 to 198).⟧",
        "⟦Tài liệu do chương 8 trích: Abramowitz và Stegun (1964), Doetsch (1943), Jones (1959), Khinchin (1934), Uffink và Hilgevoord (1985), Van der Merwe (1988), Wiener (1993).||Works cited by chapter 8: Abramowitz and Stegun (1964), Doetsch (1943), Jones (1959), Khinchin (1934), Uffink and Hilgevoord (1985), Van der Merwe (1988), Wiener (1993).⟧",
    ],
    quiz=[
        dict(q="⟦Diện tích của $f=e^{-x}H(x)$ bằng bao nhiêu (và bằng $F(0)$)?||What is the area of $f=e^{-x}H(x)$ (equal to $F(0)$)?⟧",
             opts=["{{ar_exp}}", "0.5000", "2.0000", "0.3679"], explain="⟦$\\int_0^\\infty e^{-x}dx$ = {{ar_exp}}; $F(0)$ = {{ar_F0}}; area under $F$ = {{ar_f0}}.||$\\int_0^\\infty e^{-x}dx$ = {{ar_exp}}; $F(0)$ = {{ar_F0}}; area under $F$ = {{ar_f0}}.⟧"),
        dict(q="⟦Diện tích của biến đổi của $f(x-a)H(x-a)+f(x+a)H(-x-a)$ với $f=e^{-|x|}$ bằng bao nhiêu?||What is the area of the transform of $f(x-a)H(x-a)+f(x+a)H(-x-a)$ with $f=e^{-|x|}$?⟧",
             opts=["{{sp_ft_area}}", "2.0000", "1.0000", "0.6065"], explain="⟦Tung độ giữa của hàm là 0 sau khi đẩy ra, nên diện tích biến đổi là {{sp_ft_area}}; diện tích hàm giữ {{sp_area}}.||After pushing apart the central ordinate of the function is 0, so the area of the transform is {{sp_ft_area}}; the area of the function stays {{sp_area}}.⟧"),
        dict(q="⟦Mômen bậc một $\\int xf\\,dx$ của $f=e^{-x}H(x)$ bằng bao nhiêu?||What is the first moment $\\int xf\\,dx$ of $f=e^{-x}H(x)$?⟧",
             opts=["{{fm_exp}}", "0.5000", "2.0000", "0.0000"], explain="⟦$\\int xe^{-x}dx$ = {{fm_exp}} = $F'(0)/(-2\\pi i)$.||$\\int xe^{-x}dx$ = {{fm_exp}} = $F'(0)/(-2\\pi i)$.⟧"),
        dict(q="⟦Độ dốc của biến đổi của Gauss chẵn tại gốc là bao nhiêu?||What is the slope of the transform of an even Gaussian at the origin?⟧",
             opts=["{{fm_gauss_slope}}", "1.0000", "-6.2832", "0.5000"], explain="⟦Mômen bậc một {{fm_gauss}} nên độ dốc {{fm_gauss_slope}}.||The first moment {{fm_gauss}} so the slope is {{fm_gauss_slope}}.⟧"),
        dict(q="⟦Tâm khối của $f=xe^{-x}H(x)$ bằng bao nhiêu?||What is the centroid of $f=xe^{-x}H(x)$?⟧",
             opts=["{{cen_gam}}", "1.0000", "3.0000", "6.0000"], explain="⟦$\\int x^2e^{-x}/\\int xe^{-x}$ = {{cen_gam}}; theo $F'(0)/(-2\\pi iF(0))$ cũng {{cen_gam_ft}}.||$\\int x^2e^{-x}/\\int xe^{-x}$ = {{cen_gam}}; by $F'(0)/(-2\\pi iF(0))$ also {{cen_gam_ft}}.⟧"),
        dict(q="⟦Mômen bậc hai $\\int x^2f\\,dx$ của $f=xe^{-x}H(x)$ bằng bao nhiêu?||What is the second moment $\\int x^2f\\,dx$ of $f=xe^{-x}H(x)$?⟧",
             opts=["{{m2_gam}}", "2.0000", "24.0000", "12.0000"], explain="⟦$\\int x^3e^{-x}dx=3!$ = {{m2_gam}} = $-F''(0)/4\\pi^2$ = {{m2_gam_ft}}.||$\\int x^3e^{-x}dx=3!$ = {{m2_gam}} = $-F''(0)/4\\pi^2$ = {{m2_gam_ft}}.⟧"),
        dict(q="⟦Mômen bậc 4 $\\int x^4e^{-x}H(x)dx$ bằng bao nhiêu?||What is the fourth moment $\\int x^4e^{-x}H(x)dx$?⟧",
             opts=["{{mom_4}}", "12", "120", "16"], explain="⟦$4!$ = {{mom_4}}; bậc 2 và 3: {{mom_2}}, {{mom_3}}; cũng từ đạo hàm của $F$.||$4!$ = {{mom_4}}; orders 2 and 3: {{mom_2}}, {{mom_3}}; also from derivatives of $F$.⟧"),
        dict(q="⟦$\\langle x^2\\rangle$ của $f=xe^{-x}H(x)$ bằng bao nhiêu?||What is $\\langle x^2\\rangle$ of $f=xe^{-x}H(x)$?⟧",
             opts=["{{ms_gam}}", "2.0000", "4.0000", "12.000"], explain="⟦$\\int x^3e^{-x}/\\int xe^{-x}$ = {{ms_gam}}.||$\\int x^3e^{-x}/\\int xe^{-x}$ = {{ms_gam}}.⟧"),
        dict(q="⟦$\\langle x^2\\rangle$ của $f*g$ ($f=xe^{-x}H$, $g=e^{-x}H$) bằng bao nhiêu?||What is $\\langle x^2\\rangle$ of $f*g$ ($f=xe^{-x}H$, $g=e^{-x}H$)?⟧",
             opts=["{{ms_conv}}", "8.0000", "6.0000", "16.000"], explain="⟦$6+2+2\\cdot2\\cdot1$ = {{ms_conv}}: có số hạng chéo vì tâm khối khác 0.||$6+2+2\\cdot2\\cdot1$ = {{ms_conv}}: the cross term is present because the centroids are nonzero.⟧"),
        dict(q="⟦$\\langle x^2\\rangle$ của $\\Lambda$ dịch 2 đơn vị bằng bao nhiêu?||What is $\\langle x^2\\rangle$ of $\\Lambda$ shifted by 2 units?⟧",
             opts=["{{parallel}}", "4.0000", "0.1667", "2.1667"], explain="⟦Định lý song song: $1/6+a^2$ = {{parallel}}.||Parallel-axis theorem: $1/6+a^2$ = {{parallel}}.⟧"),
        dict(q="⟦Phương sai của $f*g$ với $f=xe^{-x}H$ và $g=\\Lambda$ bằng bao nhiêu?||What is the variance of $f*g$ with $f=xe^{-x}H$ and $g=\\Lambda$?⟧",
             opts=["{{var_conv}}", "2.0000", "0.1667", "1.8333"], explain="⟦$\\sigma_f^2$ = {{var_gam}} cộng $\\sigma_\\Lambda^2$ = {{var_tri}} = {{var_conv}}.||$\\sigma_f^2$ = {{var_gam}} plus $\\sigma_\\Lambda^2$ = {{var_tri}} = {{var_conv}}.⟧"),
        dict(q="⟦Độ dốc log-log của biến đổi tam giác $\\Lambda$ ở $s$ lớn bằng bao nhiêu?||What is the log-log slope of the transform of the triangle $\\Lambda$ at large $s$?⟧",
             opts=["{{sm_2}}", "-1.0000", "-3.0000", "-4.0000"], explain="⟦Đạo hàm bậc hai là xung: $|s|^{-2}$, độ dốc {{sm_2}}; chữ nhật {{sm_1}}, $\\Pi*\\Pi*\\Pi$ {{sm_3}}.||The second derivative is impulsive: $|s|^{-2}$, slope {{sm_2}}; rectangle {{sm_1}}, $\\Pi*\\Pi*\\Pi$ {{sm_3}}.⟧"),
        dict(q="⟦Suy giảm $s^{-2}$ tương ứng bao nhiêu dB mỗi octave?||How many dB per octave does $s^{-2}$ attenuation correspond to?⟧",
             opts=["{{db_2}}", "6.0", "24.1", "3.0"], explain="⟦$2\\times20\\log_{10}2$ = {{db_2}} dB mỗi octave (40 dB mỗi decade).||$2\\times20\\log_{10}2$ = {{db_2}} dB per octave (40 dB per decade).⟧"),
        dict(q="⟦Độ rộng tương đương $W_f$ của $e^{-|x|}$ bằng bao nhiêu?||What is the equivalent width $W_f$ of $e^{-|x|}$?⟧",
             opts=["{{ew_exp}}", "1.0000", "0.5000", "3.1416"], explain="⟦Diện tích 2 chia $f(0)=1$ = {{ew_exp}}; $W_F$ = {{ew_F_exp}}.||Area 2 divided by $f(0)=1$ = {{ew_exp}}; $W_F$ = {{ew_F_exp}}.⟧"),
        dict(q="⟦Độ rộng tương đương của Lorentz $1/(1+x^2)$ bằng bao nhiêu?||What is the equivalent width of the Lorentzian $1/(1+x^2)$?⟧",
             opts=["{{ew_lor}}", "1.0000", "2.0000", "1.5708"], explain="⟦Diện tích $\\pi$ chia $f(0)=1$ = {{ew_lor}}; tích với $W_F$ = {{ew_F_lor}} bằng {{ew_prod_lor}}.||Area $\\pi$ divided by $f(0)=1$ = {{ew_lor}}; the product with $W_F$ = {{ew_F_lor}} is {{ew_prod_lor}}.⟧"),
        dict(q="⟦$W_fW_F$ của $e^{-|x|}$ bằng bao nhiêu?||What is $W_fW_F$ for $e^{-|x|}$?⟧",
             opts=["{{ew_prod_exp}}", "2.0000", "0.5000", "4.0000"], explain="⟦Định lý nghịch đảo: $W_f\\cdot W_F$ = {{ew_prod_exp}}.||Reciprocity: $W_f\\cdot W_F$ = {{ew_prod_exp}}.⟧"),
        dict(q="⟦Độ rộng tự tương quan của $e^{-|x|}$ bằng bao nhiêu?||What is the autocorrelation width of $e^{-|x|}$?⟧",
             opts=["{{aw_exp}}", "2.0000", "1.0000", "0.2500"], explain="⟦$|\\int f|^2/\\int|f|^2=4/1$ = {{aw_exp}}; bằng $1/W_{|F|^2}$ = {{aw_exp_ft}}.||$|\\int f|^2/\\int|f|^2=4/1$ = {{aw_exp}}; equal to $1/W_{|F|^2}$ = {{aw_exp_ft}}.⟧"),
        dict(q="⟦Độ rộng tự tương quan của $\\Pi(x-3)$ bằng bao nhiêu?||What is the autocorrelation width of $\\Pi(x-3)$?⟧",
             opts=["{{aw_shift}}", "3.0000", "0.0000", "2.0000"], explain="⟦Dời không đổi tự tương quan: {{aw_shift}}, dù $f(0)=0$.||Shifting does not change the autocorrelation: {{aw_shift}}, even though $f(0)=0$.⟧"),
        dict(q="⟦$\\Delta x\\,\\Delta s$ của Gauss $e^{-\\pi x^2}$ bằng bao nhiêu?||What is $\\Delta x\\,\\Delta s$ for the Gaussian $e^{-\\pi x^2}$?⟧",
             opts=["{{un_gauss}}", "0.1125", "0.2500", "0.3183"], explain="⟦$1/4\\pi$ = {{un_gauss}}, cực tiểu của hệ thức bất định.||$1/4\\pi$ = {{un_gauss}}, the minimum of the uncertainty relation.⟧"),
        dict(q="⟦$\\Delta x\\,\\Delta s$ của $e^{-|x|}$ bằng bao nhiêu?||What is $\\Delta x\\,\\Delta s$ for $e^{-|x|}$?⟧",
             opts=["{{un_exp}}", "0.0796", "0.2500", "0.0562"], explain="⟦$\\Delta x=$ {{un_dx}}, $\\Delta s=$ {{un_ds}}: tích {{un_exp}}, lớn hơn {{un_min}} khoảng {{un_ratio}} lần.||$\\Delta x=$ {{un_dx}}, $\\Delta s=$ {{un_ds}}: product {{un_exp}}, larger than {{un_min}} by about {{un_ratio}}.⟧"),
        dict(q="⟦Cận dưới của $\\Delta f$ (Hz) với $\\Delta t=1\\ \\mu$s theo $\\Delta t\\,\\Delta f\\ge1/4\\pi$ là bao nhiêu?||What is the lower bound on $\\Delta f$ (Hz) for $\\Delta t=1\\ \\mu$s by $\\Delta t\\,\\Delta f\\ge1/4\\pi$?⟧",
             opts=["{{un_radar}}", "1000000", "159155", "796"], explain="⟦$1/(4\\pi\\times10^{-6})$ = {{un_radar}} Hz.||$1/(4\\pi\\times10^{-6})$ = {{un_radar}} Hz.⟧"),
        dict(q="⟦$\\int|F|ds$ (cận của $|f|$) của $f=e^{-\\pi(x-0.5)^2}$ bằng bao nhiêu?||What is $\\int|F|ds$ (the bound on $|f|$) for $f=e^{-\\pi(x-0.5)^2}$?⟧",
             opts=["{{ineq_bound}}", "0.4559", "0.5000", "2.0000"], explain="⟦Cận là {{ineq_bound}}; $|f(0)|$ = {{ineq_f}} còn $f(0.5)$ = {{ineq_peak}} đạt cận.||The bound is {{ineq_bound}}; $|f(0)|$ = {{ineq_f}} while $f(0.5)$ = {{ineq_peak}} reaches it.⟧"),
        dict(q="⟦$\\max|f'|$ của Gauss $e^{-\\pi x^2}$ bằng bao nhiêu?||What is $\\max|f'|$ for the Gaussian $e^{-\\pi x^2}$?⟧",
             opts=["{{sl_max}}", "2.0000", "1.0000", "3.1416"], explain="⟦$\\max|f'|$ = {{sl_max}} không vượt cận $2\\pi\\int|sF|$ = {{sl_bound}}.||$\\max|f'|$ = {{sl_max}} does not exceed the bound $2\\pi\\int|sF|$ = {{sl_bound}}.⟧"),
        dict(q="⟦$\\int f^2\\int g^2$ với $f=\\Lambda$, $g=e^{-|x|}$ bằng bao nhiêu?||What is $\\int f^2\\int g^2$ for $f=\\Lambda$, $g=e^{-|x|}$?⟧",
             opts=["{{schw_r}}", "0.6000", "1.0000", "0.4000"], explain="⟦$\\tfrac23\\times1$ = {{schw_r}} $\\ge(\\int fg)^2$ = {{schw_l}}.||$\\tfrac23\\times1$ = {{schw_r}} $\\ge(\\int fg)^2$ = {{schw_l}}.⟧"),
        dict(q="⟦Độ lớn biến đổi của $\\Delta_af$ (Gauss, $a=0.5$) tại $s=0.3$ bằng bao nhiêu?||What is the magnitude of the transform of $\\Delta_af$ (Gaussian, $a=0.5$) at $s=0.3$?⟧",
             opts=["{{fd_mag}}", "0.7537", "0.9511", "0.5000"], explain="⟦$2\\sin(\\pi as)F$ = {{fd_mag}}.||$2\\sin(\\pi as)F$ = {{fd_mag}}.⟧"),
        dict(q="⟦Độ lớn biến đổi của sai phân bậc hai (cùng tham số) bằng bao nhiêu?||What is the magnitude of the transform of the second difference (same parameters)?⟧",
             opts=["{{fd2_mag}}", "0.7537", "0.1500", "1.0000"], explain="⟦$4\\sin^2(\\pi as)F$ = {{fd2_mag}}.||$4\\sin^2(\\pi as)F$ = {{fd2_mag}}.⟧"),
        dict(q="⟦Biến đổi của trung bình trượt Gauss ($a=1$) tại $s=0.3$ bằng bao nhiêu?||What is the transform of the Gaussian's running mean ($a=1$) at $s=0.3$?⟧",
             opts=["{{rm_03}}", "0.7537", "0.6468", "0.5551"], explain="⟦$\\text{sinc}(0.3)e^{-\\pi(0.3)^2}$ = {{rm_03}}; bậc hai: {{rm2_03}}.||$\\text{sinc}(0.3)e^{-\\pi(0.3)^2}$ = {{rm_03}}; second order: {{rm2_03}}.⟧"),
        dict(q="⟦$\\text{sinc}^{10}(0.2)$ bằng bao nhiêu?||What is $\\text{sinc}^{10}(0.2)$?⟧",
             opts=["{{clt_10}}", "0.5180", "0.9355", "0.4670"], explain="⟦{{clt_10}}, gần Gauss $e^{-10\\pi^2(0.2)^2/6}$ = {{clt_g}}.||{{clt_10}}, close to the Gaussian $e^{-10\\pi^2(0.2)^2/6}$ = {{clt_g}}.⟧"),
        dict(q="⟦Phương sai của tích chập bốn chữ nhật đơn vị bằng bao nhiêu?||What is the variance of the convolution of four unit rectangles?⟧",
             opts=["{{clt_var}}", "1.0000", "0.0833", "0.2500"], explain="⟦Cộng: $4/12$ = {{clt_var}}; độ nhọn dư {{clt_kurt}} ($-6/5n$).||They add: $4/12$ = {{clt_var}}; excess kurtosis {{clt_kurt}} ($-6/5n$).⟧"),
        dict(q="⟦Hệ số giữa của $\\{1\\ 1\\}^{*20}$ chuẩn hóa (nhị thức) bằng bao nhiêu?||What is the central coefficient of the normalised $\\{1\\ 1\\}^{*20}$ (binomial)?⟧",
             opts=["{{clt_bin}}", "0.1784", "0.2500", "0.0500"], explain="⟦$\\binom{20}{10}/2^{20}$ = {{clt_bin}}, gần Gauss {{clt_bin_g}}.||$\\binom{20}{10}/2^{20}$ = {{clt_bin}}, near the Gaussian {{clt_bin_g}}.⟧"),
        dict(q="⟦Lệch giữa lấy mẫu-rồi-nhân-bản và nhân-bản-rồi-lấy-mẫu là bao nhiêu?||What is the difference between sample-then-replicate and replicate-then-sample?⟧",
             opts=["{{sr_dev}}", "1.0e-03", "1.0e-01", "0.5000"], explain="⟦Hai phép giao hoán: lệch chỉ {{sr_dev}}.||The two operations commute: the difference is only {{sr_dev}}.⟧"),
        dict(q="⟦Tâm khối của $f$ liên hệ thế nào với biến đổi?||How is the centroid of $f$ related to the transform?⟧",
             opts=["⟦Độ dốc giữa chia tung độ giữa, nhân $-(2\\pi i)^{-1}$||The central slope over the central ordinate, times $-(2\\pi i)^{-1}$⟧",
                   "⟦Tung độ giữa của biến đổi nhân với đạo hàm bậc hai chia cho $4\\pi^2$ của biến đổi||The central ordinate of the transform times its second derivative divided by $4\\pi^2$⟧",
                   "⟦Vị trí cực đại của mô đun biến đổi trên trục tần số, tính bằng đơn vị $s$||The position of the maximum of the transform's modulus on the frequency axis, in units of $s$⟧",
                   "⟦Diện tích dưới biến đổi chia cho $f(0)$ nhân thêm hệ số $2\\pi$ của tần số góc||The area under the transform divided by $f(0)$ with an extra factor $2\\pi$ for angular frequency⟧"],
             explain="⟦Bracewell, tr. 155 đến 156: $\\langle x\\rangle=F'(0)/(-2\\pi iF(0))$.||Bracewell, pp. 155 to 156: $\\langle x\\rangle=F'(0)/(-2\\pi iF(0))$.⟧"),
        dict(q="⟦Nếu đạo hàm bậc $k$ của $f$ là xung thì $F(s)$ tắt thế nào ở vô cực?||If the $k$th derivative of $f$ is impulsive, how does $F(s)$ decay at infinity?⟧",
             opts=["⟦Như $|s|^{-k}$||As $|s|^{-k}$⟧",
                   "⟦Như $|s|^{-(k+1)}$, vì có thêm một thừa số $s$ từ đạo hàm cuối||As $|s|^{-(k+1)}$, because the last derivative contributes an extra factor $s$⟧",
                   "⟦Như $e^{-k|s|}$, nhanh hơn mọi lũy thừa của $s$ khi $k$ đủ lớn||As $e^{-k|s|}$, faster than any power of $s$ once $k$ is large enough⟧",
                   "⟦Như $|s|^{-k/2}$, vì phổ công suất mới tắt như $|s|^{-k}$||As $|s|^{-k/2}$, because only the power spectrum decays as $|s|^{-k}$⟧"],
             explain="⟦Bracewell, tr. 160 đến 161: đạo hàm bậc $k$ là xung thì biến đổi cư xử như $|s|^{-k}$.||Bracewell, pp. 160 to 161: if the $k$th derivative is impulsive the transform behaves as $|s|^{-k}$.⟧"),
        dict(q="⟦Vì sao độ rộng tự tương quan không hỏng khi dời xung chữ nhật?||Why does the autocorrelation width not break down when a rectangular pulse is displaced?⟧",
             opts=["⟦Tự tương quan cực đại ở gốc và không bao giờ bằng 0||The autocorrelation is maximum at the origin and never zero⟧",
                   "⟦Vì độ rộng tự tương quan đo quanh tâm khối của xung chứ không quanh gốc trục||Because it is measured about the pulse's centroid, not about the axis origin⟧",
                   "⟦Vì tự tương quan của xung chữ nhật dời luôn có dạng tam giác có diện tích bằng 0||Because the autocorrelation of a displaced rectangle is always a triangle of zero area⟧",
                   "⟦Vì phổ công suất của xung dời bằng phổ công suất của nó nhân với hệ số pha||Because the power spectrum of the displaced pulse equals the original times a phase factor⟧"],
             explain="⟦Bracewell, tr. 170: tự tương quan cực đại tại gốc, không bao giờ bằng 0.||Bracewell, p. 170: the autocorrelation is a maximum at the origin, never zero.⟧"),
        dict(q="⟦Dạng hàm nào đạt cực tiểu của hệ thức bất định $\\Delta x\\,\\Delta s=1/4\\pi$?||Which function shape attains the minimum of the uncertainty relation $\\Delta x\\,\\Delta s=1/4\\pi$?⟧",
             opts=["⟦Gauss||The Gaussian⟧",
                   "⟦Hàm chữ nhật, vì có độ rộng tương đương nhỏ nhất trong mọi hàm không âm||The rectangle, because it has the smallest equivalent width of all nonnegative functions⟧",
                   "⟦Hàm sech, vì nó là hàm tự nghịch đảo ngoài Gauss||The sech function, since it is self-reciprocal besides the Gaussian⟧",
                   "⟦Mũ hai phía, vì phương sai của nó cộng đơn giản dưới tích chập||The two-sided exponential, since its variance adds simply under convolution⟧"],
             explain="⟦Bracewell, tr. 179: Gauss cho $\\Delta x\\,\\Delta s=1/4\\pi$, đúng cực tiểu.||Bracewell, p. 179: the Gaussian gives $\\Delta x\\,\\Delta s=1/4\\pi$, exactly the minimum.⟧"),
        dict(q="⟦Điều kiện nào cần cho giới hạn trung tâm?||Which condition is needed for the central-limit theorem?⟧",
             opts=["⟦Biến đổi mỗi hàm có bướu $a-bs^2$ tại gốc với $a$ khác 0 hữu hạn||Each transform is humped, $a-bs^2$, at the origin with $a$ nonzero and finite⟧",
                   "⟦Mọi hàm đều đối xứng chẵn và không âm, và có cùng độ rộng tương đương||All functions are even, nonnegative and have the same equivalent width⟧",
                   "⟦Mỗi hàm có biến đổi bằng 0 tại $s=0$ để tích không bị chi phối bởi thành phần một chiều||Each function has a transform equal to zero at $s=0$ so that the product is not dominated by the d.c. component⟧",
                   "⟦Mỗi hàm có một góc tại gốc biến đổi, vì góc giúp hội tụ nhanh về Gauss||Each function has a corner at the origin of its transform, since a corner speeds convergence to the Gaussian⟧"],
             explain="⟦Bracewell, tr. 188: cần dạng có bướu $a-bs^2$ với $a$ khác 0 hữu hạn; nhân tử giống $\\Lambda(s)$ để lại góc vĩnh viễn.||Bracewell, p. 188: the humped form $a-bs^2$ with $a$ nonzero and finite is needed; a factor like $\\Lambda(s)$ leaves a permanent corner.⟧"),
        dict(q="⟦Sai phân hữu hạn $\\Delta_af$ ứng với phép nhân nào ở miền biến đổi?||Which multiplication in the transform domain does the finite difference $\\Delta_af$ correspond to?⟧",
             opts=["$2i\\sin(\\pi as)$",
                   "$2i\\cos(\\pi as)$ ⟦vì sai phân là cặp xung lẻ với biến đổi cosin||since the difference is a pair of impulses with a cosine transform⟧",
                   "$\\text{sinc}(as)$ ⟦vì sai phân cũng là một phép làm trơn theo khoảng $a$||since a difference is also smoothing over the interval $a$⟧",
                   "$i2\\pi s$ ⟦vì sai phân luôn bằng đạo hàm nhân với khoảng $a$||since a difference always equals the derivative times the interval $a$⟧"],
             explain="⟦Bracewell, tr. 183: cặp xung lẻ có biến đổi $2i\\sin\\pi as$; chỉ khi $a\\to0$ chia cho $a$ mới về $i2\\pi s$.||Bracewell, p. 183: the odd impulse pair has transform $2i\\sin\\pi as$; only as $a\\to0$ does dividing by $a$ tend to $i2\\pi s$.⟧"),
    ],
    nb=[
        ("md", """## 1. ⟦Diện tích, mômen, tâm khối||Area, moments, centroid⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Các đặc điểm của hàm (diện tích, mômen, tâm khối) có bằng các đặc điểm tương ứng của biến đổi tại gốc (giá trị, độ dốc, độ cong)? Mỗi số tính bằng tích phân trực tiếp và bằng đạo hàm của $F$.||Are the features of a function (area, moments, centroid) equal to the corresponding features of the transform at the origin (value, slope, curvature)? Each number is computed by direct integration and from derivatives of $F$.⟧"""),
        ("code", r'''from scipy import integrate
trap = getattr(np, "trapezoid", None) or np.trapz
def ftq(f, a, b, s, pts=None):
    re = integrate.quad(lambda x: f(x)*np.cos(2*np.pi*x*s), a, b, points=pts, limit=400)[0]
    im = integrate.quad(lambda x: -f(x)*np.sin(2*np.pi*x*s), a, b, points=pts, limit=400)[0]
    return re + 1j*im

def taylor_derivs(Ffun, n_max, r=0.05, N=64):
    """F^(n)(0) by the Cauchy integral on a circle of radius r (FFT): second method for derivatives."""
    th = 2*np.pi*np.arange(N)/N
    vals = Ffun(r*np.exp(1j*th))
    coef = np.fft.fft(vals)/N                       # coef[n] = F^(n)(0) r^n / n!
    from math import factorial
    return [coef[n]*factorial(n)/r**n for n in range(n_max + 1)]

F_exp = lambda s: 1/(1 + 2j*np.pi*s)               # e^{-x}H(x)
F_gam = lambda s: 1/(1 + 2j*np.pi*s)**2            # x e^{-x}H(x)
d_exp = taylor_derivs(F_exp, 4); d_gam = taylor_derivs(F_gam, 3)

# ⟦diện tích||area⟧
a_exp = integrate.quad(lambda x: np.exp(-x), 0, np.inf)[0]
assert abs(a_exp - F_exp(0).real) < 1e-12 and abs(integrate.quad(lambda s: F_exp(s).real, -np.inf, np.inf, limit=400)[0] - 0.5) < 1e-6
report("ar_exp", a_exp, ".4f"); report("ar_F0", F_exp(0).real, ".4f"); report("ar_f0", 0.5, ".4f")

# ⟦đẩy hai nửa ra xa: f = e^{−|x|}, a = 0.5||push the halves apart: f = e^{−|x|}, a = 0.5⟧
a = 0.5
fsplit = lambda x: np.exp(-abs(x - a)) if x > a else (np.exp(-abs(x + a)) if x < -a else 0.0)
sp_area = integrate.quad(fsplit, -60, 60, points=[-a, a], limit=400)[0]
Fsplit = lambda s: 2*np.cos(2*np.pi*a*s)*0 + (np.exp(-1j*2*np.pi*a*s)*(1/(1 + 2j*np.pi*s)) + np.exp(1j*2*np.pi*a*s)*(1/(1 - 2j*np.pi*s)))
# ⟦biến đổi của hai nửa: e^{−i2πas}/(1+i2πs) + e^{i2πas}/(1−i2πs). F(0) = 2||transform of the two halves: e^{−i2πas}/(1+i2πs) + e^{i2πas}/(1−i2πs). F(0) = 2⟧
assert abs(Fsplit(0) - 2) < 1e-12 and abs(sp_area - 2) < 1e-8
# ⟦tung độ giữa của hàm = 0 nên diện tích của biến đổi = f(0) = 0||central ordinate of the function is 0 so the area of the transform = f(0) = 0⟧
ft_area = integrate.quad(lambda s: Fsplit(s).real, -300, 300, limit=2000)[0]
assert abs(fsplit(0.0)) < 1e-15 and abs(ft_area) < 2e-2
report("sp_area", sp_area, ".4f"); report("sp_ft_area", 0.0, ".4f")

# ⟦mômen bậc một: e^{−x}H||first moment: e^{−x}H⟧
m1 = integrate.quad(lambda x: x*np.exp(-x), 0, np.inf)[0]
assert abs(m1 - (d_exp[1]/(-2j*np.pi)).real) < 1e-9
report("fm_exp", m1, ".4f")
mg1 = integrate.quad(lambda x: x*np.exp(-np.pi*x**2), -10, 10)[0]
Fg = lambda s: np.exp(-np.pi*s**2)
dsl = (Fg(1e-5) - Fg(-1e-5))/2e-5
assert abs(mg1) < 1e-12 and abs(dsl) < 1e-9
report("fm_gauss", 0.0, ".4f"); report("fm_gauss_slope", 0.0, ".4f")

# ⟦tâm khối, mômen bậc hai: x e^{−x}H||centroid, second moment: x e^{−x}H⟧
A = integrate.quad(lambda x: x*np.exp(-x), 0, np.inf)[0]
cen = integrate.quad(lambda x: x*x*np.exp(-x), 0, np.inf)[0]/A
cen_ft = (d_gam[1]/(-2j*np.pi*d_gam[0])).real
assert abs(cen - 2) < 1e-9 and abs(cen_ft - 2) < 1e-9
report("cen_gam", cen, ".4f"); report("cen_gam_ft", cen_ft, ".4f")
m2 = integrate.quad(lambda x: x**3*np.exp(-x), 0, np.inf)[0]
m2_ft = (-d_gam[2]/(4*np.pi**2)).real
assert abs(m2 - 6) < 1e-8 and abs(m2_ft - 6) < 1e-8
report("m2_gam", m2, ".4f"); report("m2_gam_ft", m2_ft, ".4f")
ms = m2/A
assert abs(ms - 6) < 1e-8
report("ms_gam", ms, ".4f")

# ⟦mômen bậc n: n! cho e^{−x}H||nth moment: n! for e^{−x}H⟧
from math import factorial
for n, key in ((2, "mom_2"), (3, "mom_3"), (4, "mom_4")):
    mn = integrate.quad(lambda x: x**n*np.exp(-x), 0, np.inf)[0]
    mn_ft = (d_exp[n]/(-2j*np.pi)**n).real
    assert abs(mn - factorial(n)) < 1e-6 and abs(mn_ft - factorial(n)) < 1e-6
    report(key, mn, ".0f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦$e^{-x}H$: diện tích {{ar_exp}}, $F(0)$ = {{ar_F0}}, area under $F$ = {{ar_f0}}; mômen bậc một {{fm_exp}}; mômen bậc 2, 3, 4: {{mom_2}}, {{mom_3}}, {{mom_4}}. Gauss chẵn: mômen bậc một {{fm_gauss}}, độ dốc {{fm_gauss_slope}}. $xe^{-x}H$: tâm khối {{cen_gam}} ({{cen_gam_ft}} từ $F$), mômen bậc hai {{m2_gam}} ({{m2_gam_ft}} từ $F''$), $\\langle x^2\\rangle$ = {{ms_gam}}. Tách và đẩy ra: diện tích {{sp_area}} giữ nguyên còn diện tích biến đổi {{sp_ft_area}}.||$e^{-x}H$: area {{ar_exp}}, $F(0)$ = {{ar_F0}}, area under $F$ = {{ar_f0}}; first moment {{fm_exp}}; moments of order 2, 3, 4: {{mom_2}}, {{mom_3}}, {{mom_4}}. Even Gaussian: first moment {{fm_gauss}}, slope {{fm_gauss_slope}}. $xe^{-x}H$: centroid {{cen_gam}} ({{cen_gam_ft}} from $F$), second moment {{m2_gam}} ({{m2_gam_ft}} from $F''$), $\\langle x^2\\rangle$ = {{ms_gam}}. Split and pushed apart: the area {{sp_area}} is unchanged while the area of the transform is {{sp_ft_area}}.⟧"""),
        ("md", """## 2. ⟦Cộng dưới tích chập và độ trơn||Additivity under convolution and smoothness⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Bình phương trung bình và phương sai có cộng dưới tích chập (kể cả số hạng chéo), và độ dốc log-log của phổ có bằng số đạo hàm còn là xung không? Mỗi số đo bằng tích chập trên lưới và bằng công thức, hoặc bằng tích phân số và bằng công thức đóng.||Do mean squares and variances add under convolution (including the cross term), and is the log-log slope of the spectrum equal to the order at which impulses appear? Each number is measured by grid convolution and by formula, or by numerical integration and by closed form.⟧"""),
        ("code", r'''dx = 0.002
xg = np.arange(0, 60, dx)
fgam = xg*np.exp(-xg)
gexp = np.exp(-xg)
conv = np.convolve(fgam, gexp)[:len(xg)]*dx                # f*g = x²e^{−x}/2
xs = xg
area_c = trap(conv, xs)
ms_c = trap(xs**2*conv, xs)/area_c
assert abs(area_c - 1) < 1e-2 and abs(ms_c - (6 + 2 + 2*2*1)) < 5e-2 and np.max(np.abs(conv - xs**2*np.exp(-xs)/2)) < 5e-3
report("ms_conv", ms_c, ".3f")

# ⟦trục dịch: Λ dịch 2||parallel axis: Λ shifted by 2⟧
Lam = lambda x: np.maximum(1 - np.abs(x), 0)
xl = np.arange(-1, 1 + 1e-9, 1e-4)
ms_tri = trap(xl**2*Lam(xl), xl)/trap(Lam(xl), xl)
assert abs(ms_tri - 1/6) < 1e-6
sh = trap((xl + 2)**2*Lam(xl), xl)/trap(Lam(xl), xl)
assert abs(sh - (1/6 + 4)) < 1e-6
report("parallel", sh, ".4f")

# ⟦phương sai||variance⟧
var_gam = 6 - 2**2
var_tri = ms_tri
xc = np.arange(-1, 61, dx)
# ⟦tích chập f*Λ trên lưới||convolution f*Λ on a grid⟧
lam_grid = Lam(np.arange(-1, 1 + dx/2, dx))
fg2 = np.convolve(fgam, lam_grid)*dx
xg2 = np.arange(len(fg2))*dx - 1.0
A2 = trap(fg2, xg2); mu2 = trap(xg2*fg2, xg2)/A2; v2 = trap((xg2 - mu2)**2*fg2, xg2)/A2
assert abs(v2 - (var_gam + var_tri)) < 5e-3
report("var_gam", var_gam, ".4f"); report("var_tri", var_tri, ".4f"); report("var_conv", v2, ".4f")

# ⟦độ dốc log-log tại s = 10.5 và 20.5||log-log slope at s = 10.5 and 20.5⟧
def B2(x):                                                   # ⟦Π*Π*Π||Π*Π*Π⟧
    ax = abs(x)
    return 0.75 - x*x if ax < 0.5 else (0.5*(1.5 - ax)**2 if ax < 1.5 else 0.0)
slopes = {}
for k, (f, lo, hi, pts) in {1: (lambda x: 1.0, -0.5, 0.5, None),
                            2: (lambda x: max(1 - abs(x), 0), -1, 1, [0]),
                            3: (B2, -1.5, 1.5, [-0.5, 0.5])}.items():
    v1 = ftq(f, lo, hi, 10.5, pts).real; v2_ = ftq(f, lo, hi, 20.5, pts).real
    slopes[k] = np.log(abs(v2_/v1))/np.log(20.5/10.5)
    assert abs(abs(v1) - abs(np.sinc(10.5))**k) < 1e-7 and abs(slopes[k] + k) < 1e-6
report("sm_1", slopes[1], ".2f"); report("sm_2", slopes[2], ".2f"); report("sm_3", slopes[3], ".2f")
db_2 = 2*20*np.log10(2)
assert abs(db_2 - 12.04) < 0.01 and abs(40 - 2*20) < 1e-12
report("db_2", db_2, ".1f")'''),
        ("code", r'''sgrid = np.logspace(0, 2, 400)
fig, ax = plt.subplots(figsize=(8, 3.4))
for k, c in ((1, "tab:blue"), (2, "tab:orange"), (3, "tab:red")):
    ax.loglog(sgrid, np.abs(np.sinc(sgrid))**k*0 + 1/(np.pi*sgrid)**k, color=c, label=f"|s|^-{k}")
ax.set_xlabel("s"); ax.set_ylabel("envelope"); ax.legend(); plt.tight_layout(); plt.show()''', dict(fig="smooth_decay", cap="⟦Hình 1. Đường bao |sinc|ᵏ trên đồ thị log-log là các đường thẳng độ dốc −1, −2, −3 khi hàm gốc lần lượt là Π (nhảy), Λ (góc), Π*Π*Π (đạo hàm bậc ba là xung).||Figure 1. The envelope of |sinc|ᵏ on a log-log plot is a set of straight lines of slope −1, −2, −3 when the function is Π (jump), Λ (corner), Π*Π*Π (third derivative impulsive).⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦$\\langle x^2\\rangle_{f*g}$ = {{ms_conv}} ($=6+2+2\\cdot2\\cdot1$). $\\Lambda$ dịch 2: {{parallel}}. Phương sai {{var_gam}} và {{var_tri}} cộng thành {{var_conv}}. Độ dốc log-log: {{sm_1}}, {{sm_2}}, {{sm_3}}; $s^{-2}$ là {{db_2}} dB mỗi octave.||$\\langle x^2\\rangle_{f*g}$ = {{ms_conv}} ($=6+2+2\\cdot2\\cdot1$). $\\Lambda$ shifted by 2: {{parallel}}. Variances {{var_gam}} and {{var_tri}} add to {{var_conv}}. Log-log slopes: {{sm_1}}, {{sm_2}}, {{sm_3}}; $s^{-2}$ is {{db_2}} dB per octave.⟧"""),
        ("md", """## 3. ⟦Độ rộng tương đương và tự tương quan||Equivalent and autocorrelation widths⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Tích $W_fW_F$ có bằng 1 và độ rộng tự tương quan có bằng nghịch đảo độ rộng tương đương của $|F|^2$? Mỗi số tính trong miền $x$ và miền $s$.||Is $W_fW_F=1$ and is the autocorrelation width the reciprocal of the equivalent width of $|F|^2$? Each number is computed in the $x$ domain and in the $s$ domain.⟧"""),
        ("code", r'''# ⟦độ rộng tương đương và nghịch đảo||equivalent width and reciprocity⟧
def ew(f, F):
    Wf = integrate.quad(f, -np.inf, np.inf, limit=400)[0]/f(0.0)
    WF = integrate.quad(F, -np.inf, np.inf, limit=400)[0]/F(0.0)
    return Wf, WF
Wf, WF = ew(lambda x: np.exp(-abs(x)), lambda s: 2/(1 + 4*np.pi**2*s**2))
assert abs(Wf - 2) < 1e-8 and abs(WF - 0.5) < 1e-8 and abs(Wf*WF - 1) < 1e-8
report("ew_exp", Wf, ".4f"); report("ew_F_exp", WF, ".4f"); report("ew_prod_exp", Wf*WF, ".4f")
Wl, WFl = ew(lambda x: 1/(1 + x*x), lambda s: np.pi*np.exp(-2*np.pi*abs(s)))
assert abs(Wl - np.pi) < 1e-8 and abs(Wl*WFl - 1) < 1e-8
report("ew_lor", Wl, ".4f"); report("ew_F_lor", WFl, ".4f"); report("ew_prod_lor", Wl*WFl, ".4f")
Wt = integrate.quad(lambda x: max(1 - abs(x), 0), -1, 1, points=[0])[0]/1.0
Wg = integrate.quad(lambda x: np.exp(-np.pi*x*x), -10, 10)[0]/1.0
assert abs(Wt - 1) < 1e-9 and abs(Wg - 1) < 1e-9
report("ew_tri", Wt, ".4f"); report("ew_gauss", Wg, ".4f")

# ⟦độ rộng tự tương quan: |∫f|²/∫|f|²; cách hai: 1/(độ rộng tương đương của |F|²)||autocorrelation width: |∫f|²/∫|f|²; method two: 1/(equivalent width of |F|²)⟧
aw = (integrate.quad(lambda x: np.exp(-abs(x)), -60, 60, points=[0])[0])**2/integrate.quad(lambda x: np.exp(-2*abs(x)), -40, 40, points=[0])[0]
P = lambda s: (2/(1 + 4*np.pi**2*s**2))**2
aw_ft = 1/(integrate.quad(P, -np.inf, np.inf, limit=400)[0]/P(0.0))
assert abs(aw - 4) < 1e-8 and abs(aw_ft - 4) < 1e-6
# ⟦cách ba: tự tương quan trên lưới||method three: autocorrelation on a grid⟧
dxa = 0.005; xa = np.arange(-30, 30, dxa); fa_ = np.exp(-np.abs(xa))
ac = np.correlate(fa_, fa_, "full")*dxa
lags = (np.arange(len(ac)) - (len(fa_) - 1))*dxa
assert abs(trap(ac, lags)/ac.max() - 4) < 2e-2
report("aw_exp", aw, ".4f"); report("aw_exp_ft", aw_ft, ".4f")

# ⟦Π dời 3 đơn vị||Π shifted by 3 units⟧
xp = np.arange(-6, 6, dxa); f0 = ((xp > -0.5) & (xp < 0.5)).astype(float); f3 = ((xp > 2.5) & (xp < 3.5)).astype(float)
def aw_grid(f):
    a = np.correlate(f, f, "full")*dxa; l = (np.arange(len(a)) - (len(f) - 1))*dxa
    return trap(a, l)/a.max()
assert abs(aw_grid(f0) - 1) < 1e-2 and abs(aw_grid(f3) - aw_grid(f0)) < 1e-9
report("aw_shift", aw_grid(f3), ".3f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦$e^{-|x|}$: $W_f$ = {{ew_exp}}, $W_F$ = {{ew_F_exp}}, tích {{ew_prod_exp}}. Lorentz: {{ew_lor}}, {{ew_F_lor}}, tích {{ew_prod_lor}}. $\\Lambda$: {{ew_tri}}; Gauss: {{ew_gauss}}. Độ rộng tự tương quan của $e^{-|x|}$: {{aw_exp}} và {{aw_exp_ft}} từ $|F|^2$; $\\Pi$ dời 3: {{aw_shift}}.||$e^{-|x|}$: $W_f$ = {{ew_exp}}, $W_F$ = {{ew_F_exp}}, product {{ew_prod_exp}}. Lorentzian: {{ew_lor}}, {{ew_F_lor}}, product {{ew_prod_lor}}. $\\Lambda$: {{ew_tri}}; Gaussian: {{ew_gauss}}. Autocorrelation width of $e^{-|x|}$: {{aw_exp}} and {{aw_exp_ft}} from $|F|^2$; $\\Pi$ shifted by 3: {{aw_shift}}.⟧"""),
        ("md", """## 4. ⟦Bất đẳng thức và hệ thức bất định||Inequalities and the uncertainty relation⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Gauss có đạt cực tiểu $1/4\\pi$, mũ hai phía lớn hơn bao nhiêu, và các cận tung độ, độ dốc, Schwarz có đúng? Ta tính $\\Delta x$ và $\\Delta s$ từ hai miền.||Does the Gaussian attain the minimum $1/4\\pi$, by how much does the two-sided exponential exceed it, and do the ordinate, slope and Schwarz bounds hold? We compute $\\Delta x$ and $\\Delta s$ from both domains.⟧"""),
        ("code", r'''def spread(w, lim=np.inf, pts=None):
    num = integrate.quad(lambda t: t*t*w(t), -lim, lim, points=pts, limit=400)[0]
    den = integrate.quad(w, -lim, lim, points=pts, limit=400)[0]
    return np.sqrt(num/den)
# ⟦Gauss a = 1||Gaussian a = 1⟧
dxg = spread(lambda x: np.exp(-2*np.pi*x*x), 10); dsg = spread(lambda s: np.exp(-2*np.pi*s*s), 10)
un_g = dxg*dsg
assert abs(un_g - 1/(4*np.pi)) < 1e-9 and abs(dxg - 1/np.sqrt(4*np.pi)) < 1e-9
report("un_gauss", un_g, ".4f")
# ⟦e^{−|x|}||e^{−|x|}⟧
dxe = spread(lambda x: np.exp(-2*abs(x)), 40, [0])
dse = spread(lambda s: (2/(1 + 4*np.pi**2*s**2))**2, np.inf)
assert abs(dxe - np.sqrt(0.5)) < 1e-8 and abs(dse - 1/(2*np.pi)) < 1e-6
un_e = dxe*dse
assert un_e > 1/(4*np.pi)
report("un_dx", dxe, ".4f"); report("un_ds", dse, ".4f"); report("un_exp", un_e, ".4f"); report("un_min", 1/(4*np.pi), ".4f")
report("un_ratio", un_e*4*np.pi, ".2f")
report("un_radar", 1/(4*np.pi*1e-6), ".0f")

# ⟦cận tung độ: f = e^{−π(x−0.5)²}||ordinate bound: f = e^{−π(x−0.5)²}⟧
fS = lambda x: np.exp(-np.pi*(x - 0.5)**2)
bound = integrate.quad(lambda s: np.exp(-np.pi*s*s), -10, 10)[0]
assert abs(bound - 1) < 1e-9 and fS(0.0) < bound and abs(fS(0.5) - bound) < 1e-12
report("ineq_f", fS(0.0), ".4f"); report("ineq_bound", bound, ".4f"); report("ineq_peak", fS(0.5), ".4f")
# ⟦cận độ dốc||slope bound⟧
xs_ = np.linspace(-3, 3, 600001); dfs = -2*np.pi*xs_*np.exp(-np.pi*xs_**2)
smax = np.max(np.abs(dfs)); sbound = 2*np.pi*integrate.quad(lambda s: abs(s)*np.exp(-np.pi*s*s), -10, 10)[0]
assert abs(smax - np.sqrt(2*np.pi/np.e)) < 1e-6 and smax <= sbound + 1e-12 and abs(sbound - 2) < 1e-9
report("sl_max", smax, ".4f"); report("sl_bound", sbound, ".4f")
# ⟦Schwarz: Λ và e^{−|x|}||Schwarz: Λ and e^{−|x|}⟧
fl = lambda x: max(1 - abs(x), 0)
lhs = integrate.quad(lambda x: fl(x)*np.exp(-abs(x)), -1, 1, points=[0])[0]**2
rhs = integrate.quad(lambda x: fl(x)**2, -1, 1, points=[0])[0]*integrate.quad(lambda x: np.exp(-2*abs(x)), -40, 40, points=[0])[0]
assert lhs <= rhs and abs(rhs - 2/3) < 1e-8
report("schw_l", lhs, ".4f"); report("schw_r", rhs, ".4f")'''),
        ("code", r'''xg_ = np.linspace(-3, 3, 600)
fig, ax = plt.subplots(1, 2, figsize=(9, 3.2))
ax[0].plot(xg_, np.exp(-2*np.pi*xg_**2), label=("⟦Gauss||Gaussian⟧")); ax[0].plot(xg_, np.exp(-2*np.abs(xg_)), label="e^{-2|x|}")
ax[0].set_title("|f|²"); ax[0].legend(fontsize=8)
sg_ = np.linspace(-1, 1, 600)
ax[1].plot(sg_, np.exp(-2*np.pi*sg_**2)); ax[1].plot(sg_, (2/(1 + 4*np.pi**2*sg_**2))**2/4)
ax[1].set_title("|F|² (⟦chuẩn hóa||normalised⟧)")
plt.tight_layout(); plt.show()''', dict(fig="uncertainty", cap="⟦Hình 2. Năng lượng |f|² (trái) và |F|² (phải, chuẩn hóa) của Gauss và mũ hai phía: mũ có đỉnh nhọn và đuôi dài nên tích độ trải lớn hơn cực tiểu 1/4π của Gauss.||Figure 2. Energy |f|² (left) and |F|² (right, normalised) of the Gaussian and the two-sided exponential: the exponential has a sharp peak and long tails so its spread product exceeds the Gaussian's minimum 1/4π.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Gauss: {{un_gauss}}. $e^{-|x|}$: $\\Delta x$ = {{un_dx}}, $\\Delta s$ = {{un_ds}}, tích {{un_exp}} ({{un_ratio}} lần cực tiểu {{un_min}}). Cận radar {{un_radar}} Hz. Cận tung độ {{ineq_bound}} so với {{ineq_f}} và đỉnh {{ineq_peak}}; độ dốc {{sl_max}} $\\le$ {{sl_bound}}; Schwarz {{schw_l}} $\\le$ {{schw_r}}.||Gaussian: {{un_gauss}}. $e^{-|x|}$: $\\Delta x$ = {{un_dx}}, $\\Delta s$ = {{un_ds}}, product {{un_exp}} ({{un_ratio}} times the minimum {{un_min}}). Radar bound {{un_radar}} Hz. Ordinate bound {{ineq_bound}} against {{ineq_f}} and the peak {{ineq_peak}}; slope {{sl_max}} $\\le$ {{sl_bound}}; Schwarz {{schw_l}} $\\le$ {{schw_r}}.⟧"""),
        ("md", """## 5. ⟦Sai phân, trung bình trượt, giới hạn trung tâm||Differences, running means, central limit⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Sai phân có nhân biến đổi với $2i\\sin\\pi as$, trung bình trượt có nhân với sinc, tích chập lặp có tiến về Gauss, và lấy mẫu giao hoán với nhân bản? Mỗi điều kiểm bằng tích phân số và công thức, hoặc bằng lưới.||Does differencing multiply the transform by $2i\\sin\\pi as$, does a running mean multiply it by sinc, does repeated convolution approach a Gaussian, and do sampling and replication commute? Each is checked by numerical integration and formula, or on a grid.⟧"""),
        ("code", r'''from scipy import special
gS = lambda x: np.exp(-np.pi*x*x); s0, aa = 0.3, 0.5
# ⟦sai phân Δ_a f = f(x+a/2) − f(x−a/2)||difference Δ_a f = f(x+a/2) − f(x−a/2)⟧
d1 = ftq(lambda x: gS(x + aa/2) - gS(x - aa/2), -10, 10, s0)
d1_f = 2j*np.sin(np.pi*aa*s0)*np.exp(-np.pi*s0**2)
assert abs(d1 - d1_f) < 1e-9
report("fd_mag", abs(d1), ".4f")
d2 = ftq(lambda x: gS(x + aa) - 2*gS(x) + gS(x - aa), -10, 10, s0)
assert abs(d2 + 4*np.sin(np.pi*aa*s0)**2*np.exp(-np.pi*s0**2)) < 1e-9
report("fd2_mag", abs(d2), ".4f")
# ⟦giới hạn a → 0||the limit a → 0⟧
ak = 1e-3
lim = (2j*np.sin(np.pi*ak*s0)/ak)/(2j*np.pi*s0)
assert abs(lim - 1) < 1e-6
report("fd_lim", abs(lim - 1), ".1e")

# ⟦trung bình trượt của Gauss, a = 1: (1/a)∫_{x−a/2}^{x+a/2} f = (1/2a)[erf(√π(x+a/2)) − erf(√π(x−a/2))]||running mean of the Gaussian, a = 1: (1/2a)[erf(√π(x+a/2)) − erf(√π(x−a/2))]⟧
aa1 = 1.0
rm = lambda x: (special.erf(np.sqrt(np.pi)*(x + aa1/2)) - special.erf(np.sqrt(np.pi)*(x - aa1/2)))/(2*aa1)
rm_num = ftq(rm, -12, 12, s0).real
rm_form = np.sinc(aa1*s0)*np.exp(-np.pi*s0**2)
assert abs(rm_num - rm_form) < 1e-8
report("rm_03", rm_form, ".4f")
rm2 = np.sinc(s0)**2*np.exp(-np.pi*s0**2)
# ⟦hai lần: chập tam giác Λ(x)/1 với Gauss trên lưới||twice: convolve the triangle with the Gaussian on a grid⟧
dxr = 0.002; xr = np.arange(-8, 8, dxr)
tri_w = np.maximum(1 - np.abs(np.arange(-1, 1 + dxr/2, dxr)), 0)
g2 = np.convolve(np.exp(-np.pi*xr**2), tri_w, "same")*dxr
rm2_num = trap(g2*np.cos(2*np.pi*s0*xr), xr)
assert abs(rm2_num - rm2) < 1e-5
report("rm2_03", rm2, ".4f")

# ⟦giới hạn trung tâm: sinc^n||central limit: sinc^n⟧
n_, sc = 10, 0.2
clt10 = np.sinc(sc)**n_; cltg = np.exp(-n_*np.pi**2*sc**2/6)
assert abs(clt10 - cltg) < 0.01
report("clt_10", clt10, ".4f"); report("clt_g", cltg, ".4f")
# ⟦n = 4 chữ nhật trên lưới: phương sai và độ nhọn dư||n = 4 rectangles on a grid: variance and excess kurtosis⟧
d = 0.005; base = np.ones(int(1/d))*d
cur = base.copy()
for _ in range(3): cur = np.convolve(cur, base)
xx = (np.arange(len(cur)) - (len(cur) - 1)/2)*d
mass = cur.sum()
var4 = (xx**2*cur).sum()/mass; kurt = (xx**4*cur).sum()/mass/var4**2 - 3
assert abs(var4 - 4/12) < 5e-3 and abs(kurt + 6/(5*4)) < 1e-2
report("clt_var", 4/12, ".4f"); report("clt_kurt", -0.3, ".2f")
# ⟦{1 1}^{*20}||{1 1}^{*20}⟧
b = np.array([1.0])
for _ in range(20): b = np.convolve(b, [1, 1])
b /= b.sum()
from math import comb
assert abs(b[10] - comb(20, 10)/2**20) < 1e-15
report("clt_bin", b[10], ".4f"); report("clt_bin_g", 1/np.sqrt(2*np.pi*5), ".4f")

# ⟦lấy mẫu và nhân bản giao hoán||sampling and replication commute⟧
fw = lambda x: np.exp(-np.pi*(x/3.0)**2)
Xr = 4; ks = np.arange(-60, 61); n0 = np.arange(-40, 41)
rep_then_sample = np.array([sum(fw(n + m*Xr) for m in ks) for n in n0])
sample_then_rep = np.array([sum(fw(n + m*Xr) for m in ks) for n in n0])
# ⟦cách độc lập: mẫu trước, rồi cộng các mẫu cách X||independent way: sample first, then add samples spaced X apart⟧
samples = {int(k): fw(k) for k in range(-300, 301)}
str_ = np.array([sum(samples[int(n + m*Xr)] for m in ks if -300 <= n + m*Xr <= 300) for n in n0])
sr_dev = np.max(np.abs(rep_then_sample - str_))
assert sr_dev < 1e-9
report("sr_dev", sr_dev, ".1e")'''),
        ("code", r'''fig, ax = plt.subplots(figsize=(8, 3.3))
sg_ = np.linspace(-2, 2, 600)
for n, c in ((1, "tab:blue"), (2, "tab:orange"), (4, "tab:green"), (10, "tab:red")):
    ax.plot(sg_, np.sinc(sg_)**n, color=c, label=f"sinc^{n}")
ax.plot(sg_, np.exp(-10*np.pi**2*sg_**2/6), "k--", lw=0.8, label="exp(−10π²s²/6)")
ax.set_ylim(-0.3, 1.05); ax.set_xlabel("s"); ax.legend(fontsize=8); plt.tight_layout(); plt.show()''', dict(fig="clt", cap="⟦Hình 3. Biến đổi của n lần tích chập chữ nhật, sincⁿ s: khi n tăng, phần giữa tiến về Gauss (nét đứt cho n = 10) và các cánh tắt nhanh.||Figure 3. The transform of n-fold rectangle convolution, sincⁿ s: as n grows the central part approaches a Gaussian (dashed for n = 10) and the wings die away.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Sai phân: {{fd_mag}}, sai phân bậc hai: {{fd2_mag}}, giới hạn $a\\to0$ lệch {{fd_lim}}. Trung bình trượt: {{rm_03}} và bậc hai {{rm2_03}}. Giới hạn trung tâm: $\\text{sinc}^{10}(0.2)$ = {{clt_10}} so với Gauss {{clt_g}}; $n=4$ phương sai {{clt_var}} và độ nhọn dư {{clt_kurt}}; $\\{1\\ 1\\}^{*20}$: {{clt_bin}} so với {{clt_bin_g}}. Lấy mẫu và nhân bản giao hoán, lệch {{sr_dev}}.||Difference: {{fd_mag}}, second difference: {{fd2_mag}}, the $a\\to0$ limit deviates by {{fd_lim}}. Running mean: {{rm_03}} and second order {{rm2_03}}. Central limit: $\\text{sinc}^{10}(0.2)$ = {{clt_10}} against the Gaussian {{clt_g}}; $n=4$ variance {{clt_var}} and excess kurtosis {{clt_kurt}}; $\\{1\\ 1\\}^{*20}$: {{clt_bin}} against {{clt_bin_g}}. Sampling and replication commute, deviation {{sr_dev}}.⟧"""),
    ],
)
