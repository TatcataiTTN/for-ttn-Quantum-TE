from lib import F, C, UL, OL, TBL

MOD = dict(
    n=4, slug="notation", part="A", book="B",
    title="⟦Ký hiệu cho các hàm hữu ích: Π, Λ, H, sgn, sinc, Gauss||Notation for useful functions: Π, Λ, H, sgn, sinc, Gaussian⟧",
    blurb="⟦Bộ ký hiệu gọn cho các hàm có bước nhảy: xung chữ nhật, tam giác, bậc thang, dấu, sinc và Gauss, cùng tính chất số của chúng.||"
          "A compact notation for functions with abrupt changes: rectangle, triangle, step, sign, sinc and Gaussian, with their numerical properties.⟧",
    src="⟦Bracewell, chương 4, tr. 55–70||Bracewell, chapter 4, pp. 55–70⟧",
    data="⟦Sinh bằng mã: các hàm cổng, tam giác, bậc thang, dốc, Gauss 2 chiều mô phỏng (Rayleigh), sinc lọc thông thấp, cửa sổ, khe quét||Generated in code: gate, triangle, step and ramp functions, simulated 2D Gaussian (Rayleigh), sinc low-pass filtering, windows, a scanning slit⟧",
    objectives=[
        "⟦Viết được hàm từng khúc bằng $\\Pi$, $\\Lambda$, $H$, $\\text{sgn}$, $R$ thay vì các điều kiện tách khúc.||Write piecewise functions with $\\Pi$, $\\Lambda$, $H$, $\\text{sgn}$, $R$ instead of case-by-case conditions.⟧",
        "⟦Dùng chuẩn hóa Gauss $e^{-\\pi x^2}$ và đọc các thông số phân tán của nó.||Use the Gaussian normalisation $e^{-\\pi x^2}$ and read its dispersion parameters.⟧",
        "⟦Nêu tính chất của $\\text{sinc}$ và $\\text{sinc}^2$: điểm không, diện tích, tần số cắt, vai trò lọc thông thấp.||State the properties of $\\text{sinc}$ and $\\text{sinc}^2$: zeros, area, cutoff, role as a low-pass filter.⟧",
        "⟦Hiểu vì sao tích chập với $H$ là tích phân, và vì sao hiếm khi cần nêu $H(0)$.||Understand why convolution with $H$ is integration, and why $H(0)$ rarely needs stating.⟧",
        "⟦So sánh các cửa sổ chữ nhật, tam giác và Gauss qua thùy phụ của biến đổi.||Compare rectangular, triangular and Gaussian windows through the sidelobes of their transforms.⟧",
    ],
    parts=[
        # ------------------------------------------------------------ PART 1
        dict(
            title="⟦Xung chữ nhật và tam giác||The rectangle and the triangle⟧",
            scr=("⟦Nhiều hàm hữu ích trong phân tích Fourier phải định nghĩa từng khúc vì thay đổi đột ngột.||Many useful functions in Fourier analysis must be defined piecewise because of abrupt changes.⟧",
                 "⟦Một hàm như \"bậc thang có dốc\" đơn giản về vật lý nhưng cồng kềnh khi viết từng khúc, khó so với $1+x^2$.||A \"sloping step function\" is simple physically but clumsy when written piecewise, unlike $1+x^2$.⟧",
                 "⟦Đưa ra ký hiệu riêng cho vài hàm cơ bản để lấy lại sự gọn gàng.||Introduce dedicated symbols for a few basic functions to regain compactness.⟧"),
            preview=["⟦Vì sao cần ký hiệu||Why notation is needed⟧", "⟦Xung chữ nhật $\\Pi$ như một cổng||The rectangle $\\Pi$ as a gate⟧", "⟦Xung tam giác $\\Lambda$ và hàm đa giác||The triangle $\\Lambda$ and polygonal functions⟧"],
            slides=[
                ("⟦Bài toán: hàm cho bằng đồ thị||The problem: functions given graphically⟧",
                 "<p>⟦Hàm $f(x)$ bằng 0 khi $x<0$, bằng $x$ khi $0\\le x\\le1$ và bằng 1 khi $x>1$ đơn giản nhưng viết từng khúc thì cồng kềnh, so với biểu thức gọn của $1+x^2$. Về mặt vật lý, một \"bậc thang có dốc\" có thể đơn giản không kém một hàm trơn (Bracewell, tr. 55).||"
                 "The function $f(x)$ equal to 0 for $x<0$, $x$ for $0\\le x\\le1$ and 1 for $x>1$ is simple yet awkward to write piecewise, compared with the compact expression $1+x^2$. Physically a \"sloping step function\" may be at least as simple as a smoother function (Bracewell, p. 55).⟧</p>"),
                ("⟦Fourier và hàm cho bằng đồ thị||Fourier and functions given by a graph⟧",
                 "<p>⟦Chính Fourier quan tâm tới việc biểu diễn các hàm cho bằng đồ thị. Theo nhà toán học và sử học người Anh E. W. Hobson, ông là người đầu tiên hiểu trọn vẹn rằng một hàm có thể gồm các phần rời nhau cho tùy ý bằng đồ thị (tr. 55). Chương này giới thiệu ký hiệu để lấy lại sự gọn và rõ.||"
                 "Fourier himself was concerned with representing functions given graphically, and according to the English mathematician and historian E. W. Hobson was the first fully to grasp that a single function may consist of detached portions given arbitrarily by a graph (p. 55). This chapter introduces notation to regain compactness and clarity.⟧</p>"),
                ("⟦Xung chữ nhật $\\Pi(x)$||The rectangle function $\\Pi(x)$⟧",
                 "<p>⟦Xung chữ nhật đơn vị cao 1 và đáy 1, tâm ở gốc (hình 4.1, tr. 55 đến 56):||The rectangle function of unit height and base, centred at the origin (Fig. 4.1, pp. 55 to 56):⟧</p>"
                 + F("⟦Xung chữ nhật||Rectangle function⟧", r"\Pi(x)=\begin{cases}0,&|x|>\tfrac12\\1,&|x|<\tfrac12\end{cases}")),
                ("⟦Nhân với $\\Pi$ là cắt một đoạn||Multiplying by $\\Pi$ gates a segment⟧",
                 "<p>⟦$f(x)=\\Pi(x)\\cos\\pi x$ là ký hiệu gọn cho hàm bằng $\\cos\\pi x$ trong $|x|<\\tfrac12$ và 0 ở ngoài (hình 4.2). Nhân với $\\Pi$ chọn (\"cổng\") một đoạn của hàm bất kỳ. Năng lượng của đoạn đó là $\\int\\Pi(x)\\cos^2\\pi x\\,dx$ = {{gate_energy}} (tr. 56).||"
                 "$f(x)=\\Pi(x)\\cos\\pi x$ is compact notation for a function equal to $\\cos\\pi x$ in $|x|<\\tfrac12$ and 0 outside (Fig. 4.2). Multiplying by $\\Pi$ selects (\"gates\") a segment of any function. The energy of that segment is $\\int\\Pi(x)\\cos^2\\pi x\\,dx$ = {{gate_energy}} (p. 56).⟧</p>"),
                ("⟦Xung dịch, cao $h$, đáy $b$||A displaced rectangle of height $h$ and base $b$⟧",
                 "<p>⟦Hàm $h\\,\\Pi[(x-c)/b]$ là xung chữ nhật cao $h$, đáy $b$, tâm tại $x=c$ (hình 4.3). Chỉ bằng nhân với một xung dịch phù hợp ta chọn được mọi đoạn với mọi biên độ và đưa phần còn lại về 0 (tr. 56). Ví dụ $h=3$, $b=2$, $c=1$: diện tích $hb$ = {{rect_area}}, tích phân số trùng.||"
                 "The function $h\\,\\Pi[(x-c)/b]$ is a rectangle of height $h$ and base $b$ centred at $x=c$ (Fig. 4.3). Purely by multiplying by a suitably displaced rectangle we can select any segment with any amplitude and reduce the rest to zero (p. 56). Example $h=3$, $b=2$, $c=1$: area $hb$ = {{rect_area}}, numerical integration agrees.⟧</p>"
                 + F("⟦Xung chữ nhật tổng quát||General rectangle⟧", r"h\,\Pi\!\left(\frac{x-c}{b}\right):\quad\text{⟦cao||height⟧}\ h,\ \text{⟦đáy||base⟧}\ b,\ \text{⟦tâm||centre⟧}\ c")),
                ("⟦Xung chữ nhật đi vào đâu: trung bình trượt và lọc||Where the rectangle appears: running means and filtering⟧",
                 UL(["⟦Qua tích chập, nó cho trung bình trượt (module 3).||Through convolution it gives running means (module 3).⟧",
                     "⟦Ở miền tần số, nhân với nó là lọc thông thấp lý tưởng.||In the frequency domain multiplying by it is ideal low-pass filtering.⟧",
                     "⟦Nó là \"thừa số gián đoạn Dirichlet\" trong lý thuyết hội tụ chuỗi Fourier.||It is \"Dirichlet's discontinuous factor\" in the theory of convergence of Fourier series.⟧",
                     "⟦Các tên khác: rect $x$, hàm cổng, hàm cửa sổ, hàm boxcar (tr. 57).||Other names: rect $x$, gate function, window function, boxcar function (p. 57).⟧"])),
                ("⟦Giá trị tại chỗ nhảy hầu như không quan trọng||The value at the jump hardly matters⟧",
                 "<p>⟦Bracewell hầu như không nêu $\\Pi(\\pm\\tfrac12)$, và cũng không nên nhấn mạnh giá trị $\\tfrac12$ ở giữa bước nhảy khi vẽ, giống một dao động ký chất lượng cao không hiện điểm sáng thêm giữa bước nhảy (tr. 57). Lý do: một điểm không đổi tích phân. Số đo: diện tích với $\\Pi(\\pm\\tfrac12)=0$, $\\tfrac12$ hoặc 1 khác nhau tối đa {{edge_diff}}, cỡ sai số của lưới.||"
                 "Bracewell almost never states $\\Pi(\\pm\\tfrac12)$, and it is undesirable to emphasise the value $\\tfrac12$ halfway up the jump when drawing, like a high-quality oscillogram that never shows extra brightening halfway up the discontinuity (p. 57). The reason: a single point does not change an integral. Measured: the area with $\\Pi(\\pm\\tfrac12)=0$, $\\tfrac12$ or 1 differs by at most {{edge_diff}}, the size of the grid error.⟧</p>"),
                ("⟦Xung tam giác $\\Lambda(x)$||The triangle function $\\Lambda(x)$⟧",
                 "<p>⟦Xung tam giác cao 1 và diện tích 1. Nó quan trọng chủ yếu vì là tự tích chập của $\\Pi(x)$, và còn cho ký hiệu gọn cho hàm đa giác, tức hàm liên tục gồm các đoạn thẳng (tr. 57). $h\\Lambda(x/b)$ có chiều cao $h$, đáy $2b$ và diện tích $hb$.||"
                 "The triangle function has unit height and area. It gains its importance largely from being the self-convolution of $\\Pi(x)$, and it gives compact notation for polygonal functions, continuous functions made of linear segments (p. 57). $h\\Lambda(x/b)$ has height $h$, base $2b$ and area $hb$.⟧</p>"
                 + F("⟦Xung tam giác||Triangle function⟧", r"\Lambda(x)=\begin{cases}0,&|x|>1\\1-|x|,&|x|<1\end{cases}=\Pi*\Pi")),
                ("⟦Thử số: $\\Lambda=\\Pi*\\Pi$ và hàm đa giác||Numerical test: $\\Lambda=\\Pi*\\Pi$ and polygonal functions⟧",
                 "<p>⟦Tích chập số của $\\Pi$ với chính nó trên lưới mịn lệch $1-|x|$ tối đa {{tri_dev}}, diện tích {{tri_area}}. Hàm đa giác qua các điểm $(0,0),(1,2),(2,1),(3,3),(4,0)$ bằng $\\sum y_k\\Lambda(x-k)$: lệch <code>interp</code> tối đa {{poly_err}}, và tại $x=2.5$ bằng {{poly_25}}.||"
                 "The numerical convolution of $\\Pi$ with itself on a fine grid deviates from $1-|x|$ by at most {{tri_dev}}, area {{tri_area}}. The polygonal function through $(0,0),(1,2),(2,1),(3,3),(4,0)$ equals $\\sum y_k\\Lambda(x-k)$: deviation from <code>interp</code> at most {{poly_err}}, and at $x=2.5$ it equals {{poly_25}}.⟧</p>{{fig:poly}}"),
            ]),
        # ------------------------------------------------------------ PART 2
        dict(
            title="⟦Hàm mũ, Gauss và Rayleigh||Exponentials, the Gaussian and the Rayleigh curve⟧",
            scr=("⟦Gauss xuất hiện khắp nơi, nhưng mỗi ngành chuẩn hóa nó một kiểu.||The Gaussian is everywhere, but each field normalises it differently.⟧",
                 "⟦Chuẩn hóa thống kê (diện tích 1 và $\\sigma=1$) làm biến đổi Fourier của Gauss không cùng dạng với chính nó.||The statistical normalisation (area 1 and $\\sigma=1$) makes the Fourier transform of a Gaussian a different-looking Gaussian.⟧",
                 "⟦Bracewell chọn $e^{-\\pi x^2}$: tung độ trung tâm bằng 1, diện tích bằng 1, và tự biến đổi.||Bracewell picks $e^{-\\pi x^2}$: central ordinate 1, area 1, and self-transforming.⟧"),
            preview=["⟦Bốn hàm mũ||Four exponentials⟧", "⟦Chuẩn hóa Gauss và các thông số phân tán||Gaussian normalisation and dispersion parameters⟧", "⟦Rayleigh và bước đi của người say||Rayleigh and the drunkard's walk⟧"],
            slides=[
                ("⟦Bốn hàm mũ||Four exponentials⟧",
                 "<p>⟦Hình 4.5 cho từ trái sang phải: hàm mũ tăng, hàm mũ giảm, hàm mũ giảm cắt cụt và hàm mũ giảm hai phía (tr. 57).||Fig. 4.5 shows from left to right: a rising exponential, a falling exponential, a truncated falling exponential and a double-sided falling exponential (p. 57).⟧</p>"
                 + TBL(["⟦Tên||Name⟧", "⟦Công thức||Formula⟧"], [["⟦tăng||rising⟧", "$e^{x}$"], ["⟦giảm||falling⟧", "$e^{-x}$"], ["⟦giảm cắt cụt||truncated falling⟧", "$e^{-x}H(x)$"], ["⟦hai phía||double-sided⟧", "$e^{-|x|}$"]])),
                ("⟦Chuẩn hóa Gauss của Bracewell||Bracewell's Gaussian normalisation⟧",
                 "<p>⟦Hàm $\\exp(-\\pi x^2)$ được chọn để cả tung độ trung tâm lẫn diện tích dưới đường cong đều bằng 1, và biến đổi Fourier của nó cũng là Gauss chuẩn hóa y hệt (tr. 58). Notebook đo diện tích {{g_area}}, tung độ trung tâm 1, và giá trị trung bình của $x^2$ là {{g_var}}.||"
                 "The function $\\exp(-\\pi x^2)$ is chosen so that both the central ordinate and the area under the curve equal 1, and its Fourier transform is the same normalised Gaussian (p. 58). The notebook measures area {{g_area}}, central ordinate 1, and the mean of $x^2$ equal to {{g_var}}.⟧</p>"
                 + F("⟦Gauss chuẩn hóa||Normalised Gaussian⟧", r"e^{-\pi x^2}\ \supset\ e^{-\pi s^2},\qquad \int_{-\infty}^{\infty}e^{-\pi x^2}\,dx=1")),
                ("⟦Dạng thống kê và tung độ xác suất||The statistical form and the probability ordinate⟧",
                 "<p>⟦Trong thống kê, Gauss là \"phân phối chuẩn (sai số) trung bình 0\" chuẩn hóa để diện tích và độ lệch chuẩn bằng 1. Khi độ lệch chuẩn là $\\sigma$, tung độ xác suất là $\\frac{1}{\\sigma\\sqrt{2\\pi}}e^{-x^2/2\\sigma^2}$, với tung độ trung tâm $0.3989/\\sigma$ (tr. 58). So với $e^{-\\pi x^2}$ thì $\\sigma=(2\\pi)^{-1/2}$ = {{g_sd}}.||"
                 "In statistics the Gaussian is the \"normal (error) distribution with zero mean\", normalised so the area and standard deviation are 1. For standard deviation $\\sigma$ the probability ordinate is $\\frac{1}{\\sigma\\sqrt{2\\pi}}e^{-x^2/2\\sigma^2}$ with central ordinate $0.3989/\\sigma$ (p. 58). Compared with $e^{-\\pi x^2}$ we have $\\sigma=(2\\pi)^{-1/2}$ = {{g_sd}}.⟧</p>"
                 + F("⟦Tung độ xác suất||Probability ordinate⟧", r"\frac{1}{\sigma\sqrt{2\pi}}\,e^{-x^2/2\sigma^2}")),
                ("⟦Tích phân sai số erf, erfc và tích phân xác suất||The error integral erf, erfc and the probability integral⟧",
                 "<p>⟦Tích phân sai số $\\text{erf}\\,x=\\frac{2}{\\sqrt\\pi}\\int_0^xe^{-t^2}dt$ và phần bù $\\text{erfc}\\,x=1-\\text{erf}\\,x$; tích phân xác suất $a(x)$ được tra bảng rộng rãi. Với Gauss của sách, $\\int_0^xe^{-\\pi t^2}dt=\\tfrac12\\text{erf}(\\sqrt\\pi\\,x)$ (tr. 58 đến 59). Tại $x=1$: tích phân số và công thức cho {{g_int1}}.||"
                 "The error integral $\\text{erf}\\,x=\\frac{2}{\\sqrt\\pi}\\int_0^xe^{-t^2}dt$ with complement $\\text{erfc}\\,x=1-\\text{erf}\\,x$; the probability integral $a(x)$ is widely tabulated. For the book's Gaussian, $\\int_0^xe^{-\\pi t^2}dt=\\tfrac12\\text{erf}(\\sqrt\\pi\\,x)$ (pp. 58 to 59). At $x=1$: numerical integration and the formula give {{g_int1}}.⟧</p>"
                 + F("⟦Liên hệ với erf||Relation to erf⟧", r"\int_0^{x}e^{-\pi t^2}\,dt=\tfrac12\,\operatorname{erf}\!\left(\sqrt{\pi}\,x\right)")),
                ("⟦Các thông số phân tán của $e^{-\\pi x^2}$||Dispersion parameters of $e^{-\\pi x^2}$⟧",
                 "<p>⟦Sách nêu năm thông số (tr. 59); notebook tính lại mỗi thông số bằng hai cách (công thức đóng và tích phân số hoặc tìm nghiệm):||The book lists five parameters (p. 59); the notebook recomputes each by two methods (closed form and numerical integration or root finding):⟧</p>"
                 + TBL(["⟦Thông số||Parameter⟧", "⟦Giá trị||Value⟧", "⟦Theo $\\sigma$||In units of $\\sigma$⟧"],
                       [["⟦sai số xác suất (nửa khoảng tứ phân vị)||probable error (semi-interquartile range)⟧", "{{pe}}", "0.6745"], ["⟦sai số tuyệt đối trung bình||mean absolute error⟧", "{{mad}}", "0.7979"],
                        ["⟦độ lệch chuẩn||standard deviation⟧", "{{g_sd}}", "1"], ["⟦độ rộng tại nửa đỉnh||width to half-peak⟧", "{{fwhm}}", "2.355"], ["⟦độ rộng tương đương||equivalent width⟧", "{{eqw}}", "2.5066"]])),
                ("⟦Bao nhiêu phần trăm nằm trong mỗi thông số?||What percentage lies within each parameter?⟧",
                 "<p>⟦Sai số xác suất đặc trưng cho 50 phần trăm giữa của một tập đo: \"chiều cao trung bình của sinh viên là 165 ± 10 cm\" nghĩa là một nửa số sinh viên nằm trong 155 đến 175 cm, trừ khi nêu thước đo khác (tr. 59). Với chuẩn, phần trăm nằm trong một độ lệch chuẩn là {{cov_sd}}, trong sai số tuyệt đối trung bình {{cov_mad}}, trong nửa độ rộng nửa đỉnh {{cov_half}}, trong nửa độ rộng tương đương {{cov_eq}}.||"
                 "The probable error characterises the middle 50 percent of a set of measurements: \"the students have an average height of 165 ± 10 cm\" means half of the students are in 155 to 175 cm unless another measure of spread is specified (p. 59). For a normal distribution the percentage within one standard deviation is {{cov_sd}}, within the mean absolute error {{cov_mad}}, within the semi-width to half-peak {{cov_half}}, within the semi-equivalent width {{cov_eq}}.⟧</p>"),
                ("⟦Hai chiều và phân phối Rayleigh||Two dimensions and the Rayleigh distribution⟧",
                 "<p>⟦Gauss hai chiều $e^{-\\pi(x^2+y^2)}$ vẫn tự biến đổi, có tung độ trung tâm và thể tích bằng 1. Với đối xứng tròn, xác suất tìm thấy khoảng cách trong $r$ đến $r+dr$ là $2\\pi r\\,dr$ nhân tung độ, nên $R(r)=\\frac{r}{\\sigma^2}e^{-r^2/2\\sigma^2}$. Đó là phân phối Rayleigh (tr. 59 đến 60).||"
                 "The two-dimensional Gaussian $e^{-\\pi(x^2+y^2)}$ is still self-transforming, with unit central ordinate and unit volume. With circular symmetry the probability of finding the radial distance between $r$ and $r+dr$ is $2\\pi r\\,dr$ times the ordinate, so $R(r)=\\frac{r}{\\sigma^2}e^{-r^2/2\\sigma^2}$. This is Rayleigh's distribution (pp. 59 to 60).⟧</p>"
                 + F("⟦Phân phối Rayleigh||Rayleigh distribution⟧", r"R(r)=\frac{r}{\sigma^2}\,e^{-r^2/2\sigma^2},\qquad r\ge0")),
                ("⟦Bước đi của người say: nghịch lý đỉnh không ở gốc||The drunkard's walk: the paradox of the peak away from the origin⟧",
                 "<p>⟦Bài toán người say của Rayleigh: mỗi bước theo hướng tùy ý. Sau lâu, xác suất ở $(x,y)$ là Gauss hai chiều (đỉnh ở gốc) nhưng xác suất ở khoảng cách $r$ là Rayleigh (đỉnh không ở gốc). Hai điều nghe mâu thuẫn, và Bracewell mời bạn tự suy ngẫm (tr. 60). Mô phỏng 400 000 điểm: khoảng cách trung bình {{ray_mean_mc}} (lý thuyết {{ray_mean_th}}), đỉnh tại {{ray_mode_mc}}, và {{ray_p1_mc}} số điểm nằm trong $r<\\sigma$ (lý thuyết {{ray_p1_th}}).||"
                 "Rayleigh's drunkard's-walk problem: each step is in an arbitrary direction. After a long time the probability at $(x,y)$ is a two-dimensional Gaussian (peak at the origin) yet the probability at distance $r$ is Rayleigh (peak away from the origin). The two sound contradictory and Bracewell invites you to contemplate it (p. 60). A simulation of 400 000 points: mean distance {{ray_mean_mc}} (theory {{ray_mean_th}}), peak at {{ray_mode_mc}}, and {{ray_p1_mc}} of the points lie within $r<\\sigma$ (theory {{ray_p1_th}}).⟧</p>{{fig:rayleigh}}"),
                ("⟦Dãy Gauss cho biến đổi trong giới hạn||Gaussian sequences for transforms in the limit||⟧".replace("||⟧", "⟧"),
                 "<p>⟦Dãy $\\exp(-\\pi\\tau^2x^2)$ khi $\\tau\\to0$ dùng để nhân với hàm có tích phân không hội tụ; giới hạn là 1. Dãy $|\\tau|^{-1}\\exp(-\\pi x^2/\\tau^2)$ dùng để khôi phục hàm thường trong trường hợp xung bằng tích chập. Gauss hợp cho việc này vì mọi đạo hàm liên tục và nó tắt nhanh hơn mọi lũy thừa của $x$ (tr. 60). Số đo: $\\int\\cos x\\,|\\tau|^{-1}e^{-\\pi x^2/\\tau^2}dx=e^{-\\tau^2/4\\pi}$ bằng {{gs_1}} ($\\tau=1$), {{gs_05}} ($\\tau=0.5$), {{gs_01}} ($\\tau=0.1$), tiến về $\\cos0=1$.||"
                 "The sequence $\\exp(-\\pi\\tau^2x^2)$ as $\\tau\\to0$ multiplies functions whose integrals do not converge; the limit is 1. The sequence $|\\tau|^{-1}\\exp(-\\pi x^2/\\tau^2)$ recovers ordinary functions, in cases of impulsive behaviour, by convolution. The Gaussian suits this because all its derivatives are continuous and it dies away faster than any power of $x$ (p. 60). Measured: $\\int\\cos x\\,|\\tau|^{-1}e^{-\\pi x^2/\\tau^2}dx=e^{-\\tau^2/4\\pi}$ equals {{gs_1}} ($\\tau=1$), {{gs_05}} ($\\tau=0.5$), {{gs_01}} ($\\tau=0.1$), tending to $\\cos0=1$.⟧</p>"),
            ]),
        # ------------------------------------------------------------ PART 3
        dict(
            title="⟦Bậc thang Heaviside, hàm dốc và hàm dấu||Heaviside's step, the ramp and the sign function⟧",
            scr=("⟦Điện áp bật đột ngột hay lực bắt đầu tác dụng tại một thời điểm là những bước nhảy quen thuộc trong vật lý.||Voltages switched on suddenly and forces that begin to act at a definite time are familiar jumps in physics.⟧",
                 "⟦Muốn viết chúng gọn và biến chúng thành tích phân dễ, ta cần một hàm cơ bản cho bước nhảy.||To write them compactly and turn them into easy integrals we need one basic function for a jump.⟧",
                 "⟦$H(x)$, kéo theo hàm dốc $R(x)$, tích chập là tích phân, và hàm dấu $\\text{sgn}\\,x$.||$H(x)$, with the ramp $R(x)$, convolution as integration, and the sign function $\\text{sgn}\\,x$.⟧"),
            preview=["⟦$H$, hàm dốc và tích phân||$H$, the ramp and integration⟧", "⟦Giá trị $H(0)$ và hàm rỗng||The value $H(0)$ and null functions⟧", "⟦Hàm dấu||The sign function⟧"],
            slides=[
                ("⟦Bậc thang đơn vị $H(x)$||The unit step $H(x)$⟧",
                 "<p>⟦$H(x)$ bằng 0 khi $x<0$, 1 khi $x>0$ (và thường $\\tfrac12$ tại 0). Nó biểu diễn điện áp bật đột ngột hoặc lực bắt đầu tác dụng tại một thời điểm rồi không đổi (hình 4.8, tr. 61). Nhân một hàm với $H$ đưa nó về 0 ở phía âm và giữ nguyên ở phía dương.||"
                 "$H(x)$ is 0 for $x<0$, 1 for $x>0$ (and usually $\\tfrac12$ at 0). It represents voltages suddenly switched on or forces that begin to act at a definite time and are constant thereafter (Fig. 4.8, p. 61). Multiplying a function by $H$ reduces it to zero on the negative side and leaves it intact on the positive side.⟧</p>"
                 + F("⟦Bậc thang Heaviside||Heaviside unit step⟧", r"H(x)=\begin{cases}0,&x<0\\ \tfrac12,&x=0\\ 1,&x>0\end{cases}")),
                ("⟦Biểu diễn bật tắt||Switching notation⟧",
                 "<p>⟦Sóng hình sin bật tại $t=0$ là $\\sin t\\,H(t)$ (hình 4.10). Điện áp bằng 0 tới $t_0$ rồi nhảy lên giá trị $E$ là $EH(t-t_0)$ (hình 4.11). Mọi hàm có bước nhảy phân tích được thành một hàm liên tục cộng bậc thang dịch phù hợp (tr. 61 đến 62).||"
                 "A sinusoid switched on at $t=0$ is $\\sin t\\,H(t)$ (Fig. 4.10). A voltage zero until $t_0$ and then jumping to a steady $E$ is $EH(t-t_0)$ (Fig. 4.11). Any function with a jump decomposes into a continuous function plus a suitably displaced step (pp. 61 to 62).⟧</p>"),
                ("⟦$\\Pi$ chỉ gồm các bậc thang||$\\Pi$ is made of steps alone⟧",
                 "<p>⟦Xung chữ nhật có hai bước nhảy đơn vị, một dương và một âm; bỏ chúng đi thì không còn gì. Vì vậy $\\Pi(x)=H(x+\\tfrac12)-H(x-\\tfrac12)$ (hình 4.9, tr. 61). Notebook kiểm bằng số trên lưới: {{pi_step_ok}}, kể cả tại $x=\\pm\\tfrac12$ với $H(0)=\\tfrac12$.||"
                 "The rectangle has two unit discontinuities, one positive and one negative; remove them and nothing remains. Hence $\\Pi(x)=H(x+\\tfrac12)-H(x-\\tfrac12)$ (Fig. 4.9, p. 61). The notebook checks it numerically on a grid: {{pi_step_ok}}, even at $x=\\pm\\tfrac12$ with $H(0)=\\tfrac12$.⟧</p>"
                 + F("⟦$\\Pi$ qua $H$||$\\Pi$ through $H$⟧", r"\Pi(x)=H\!\left(x+\tfrac12\right)-H\!\left(x-\tfrac12\right)")),
                ("⟦Hàm dốc $R(x)=xH(x)$||The ramp $R(x)=xH(x)$⟧",
                 "<p>⟦$(F/m)R(t)$ là vận tốc của khối lượng $m$ chịu lực không đổi $FH(t)$, hoặc dòng điện trong cuộn cảm $m$ khi đặt hiệu điện thế $FH(t)$. $R$ là tích phân của $H$ và $H$ là đạo hàm của $R$ (hình 4.12, tr. 61 đến 62). Notebook: tích chập số $H*H$ tại $x=2$ cho {{ramp_2}}, đúng $R(2)$.||"
                 "$(F/m)R(t)$ is the velocity of a mass $m$ to which a steady force $FH(t)$ has been applied, or the current in a coil of inductance $m$ across which the potential difference is $FH(t)$. $R$ is the integral of $H$ and $H$ is the derivative of $R$ (Fig. 4.12, pp. 61 to 62). Notebook: the numerical convolution $H*H$ at $x=2$ gives {{ramp_2}}, exactly $R(2)$.⟧</p>"
                 + F("⟦Hàm dốc||The ramp⟧", r"R(x)=xH(x)=\int_{-\infty}^{x}H(x')\,dx'=H*H,\qquad R'(x)=H(x)")),
                ("⟦Tích chập với $H$ là tích phân||Convolution with $H$ is integration⟧",
                 "<p>⟦Vì $H(x-x')$ bằng 0 khi $x'>x$, các tích phân có cận thay đổi trở thành cận cố định: $\\int_{-\\infty}^xf(x')dx'=\\int f(x')H(x-x')dx'$. Do đó $H*f$ là tích phân của $f$ (hình 4.13, tr. 62 đến 63). Với $f=e^{-\\pi x^2}$ tại $x=0.5$: tích chập số với bậc thang cho {{hf_05}}, đúng $\\tfrac12[1+\\text{erf}(\\sqrt\\pi\\,x)]$ (lệch tối đa {{hf_dev}}).||"
                 "Because $H(x-x')$ is zero for $x'>x$, integrals with variable limits become constant-limit integrals: $\\int_{-\\infty}^xf(x')dx'=\\int f(x')H(x-x')dx'$. Hence $H*f$ is the integral of $f$ (Fig. 4.13, pp. 62 to 63). With $f=e^{-\\pi x^2}$ at $x=0.5$: numerical convolution with a step gives {{hf_05}}, exactly $\\tfrac12[1+\\text{erf}(\\sqrt\\pi\\,x)]$ (largest deviation {{hf_dev}}).⟧</p>"
                 + F("⟦Tích chập với bậc thang||Convolution with the step⟧", r"H*f(x)=\int_{-\infty}^{x}f(x')\,dx'")),
                ("⟦Giá trị $H(0)$ và điều nhất quán||The value $H(0)$ and consistency⟧",
                 "<p>⟦Thường không cần định nghĩa $H(0)$, nhưng để tương thích với lý thuyết hàm đơn trị nên gán $\\tfrac12$. Khi đó $R'(0+)=1$, $R'(0-)=0$, và đạo hàm đối xứng tại 0 bằng $\\tfrac12$; tích phân Fourier hội tụ tại điểm gián đoạn cũng cho giá trị giữa (tr. 63). Số đo: $[R(\\Delta)-R(-\\Delta)]/2\\Delta$ = {{r_prime0}}.||"
                 "It is usually unimportant to define $H(0)$, but for compatibility with the theory of single-valued functions it is desirable to assign $\\tfrac12$. Then $R'(0+)=1$, $R'(0-)=0$ and the symmetric derivative at 0 equals $\\tfrac12$; the Fourier integral, when it converges at a point of discontinuity, also gives the midvalue (p. 63). Measured: $[R(\\Delta)-R(-\\Delta)]/2\\Delta$ = {{r_prime0}}.⟧</p>"),
                ("⟦Chọn $H(0)=0$ và hàm rỗng||Choosing $H(0)=0$ and null functions⟧",
                 "<p>⟦Không bắt buộc lấy $H(0)=\\tfrac12$; đôi khi lấy 0, như hệ quả của cách nhìn $\\hat H(x)=\\lim_{\\tau\\to0}(1-e^{-x/\\tau})H(x)$ (hình 4.14). Khi đó $H=\\hat H+\\tfrac12\\delta^{\\circ}$ với $\\delta^{\\circ}$ là một hàm rỗng: bằng 0 mọi nơi trừ gốc, tích phân luôn bằng 0 (tr. 63 đến 64). Số đo: $\\int(H-\\hat H)\\,dx=\\tau$ = {{hhat_int}} khi $\\tau=0.01$, tiến về 0.||"
                 "There is no obligation to take $H(0)=\\tfrac12$; it is sometimes taken as zero, a natural consequence of the view $\\hat H(x)=\\lim_{\\tau\\to0}(1-e^{-x/\\tau})H(x)$ (Fig. 4.14). Then $H=\\hat H+\\tfrac12\\delta^{\\circ}$ with $\\delta^{\\circ}$ a null function: zero everywhere except the origin, with integral always zero (pp. 63 to 64). Measured: $\\int(H-\\hat H)\\,dx=\\tau$ = {{hhat_int}} for $\\tau=0.01$, tending to 0.⟧</p>"),
                ("⟦Xấp xỉ liên tục của $H$||Continuous approximations to $H$⟧",
                 "<p>⟦Sách liệt kê nhiều xấp xỉ trơn tiến về $H(x)$ khi $\\tau\\to0$, chẳng hạn $\\tfrac12+\\frac1\\pi\\arctan\\frac x\\tau$, tích phân của một đường Lorentz (tr. 64). Tại $x=0.1$: với $\\tau=0.1$ được {{arctan_1}}, với $\\tau=0.01$ được {{arctan_2}}, tiến về 1. Khác biệt giữa $H$ và mọi phiên bản có $H(0)\\ne\\tfrac12$ là một hàm rỗng, vô hình với phép đo vật lý có độ phân giải hữu hạn nên nói tới $H(0)$ là không cần thiết (tr. 64 đến 65).||"
                 "The book lists many smooth approximations tending to $H(x)$ as $\\tau\\to0$, for example $\\tfrac12+\\frac1\\pi\\arctan\\frac x\\tau$, the integral of a Lorentzian (p. 64). At $x=0.1$: with $\\tau=0.1$ we get {{arctan_1}}, with $\\tau=0.01$ we get {{arctan_2}}, approaching 1. The difference between $H$ and any version with $H(0)\\ne\\tfrac12$ is a null function, invisible to physical measurements of finite resolving power, so it is more graceful not to mention $H(0)$ (pp. 64 to 65).⟧</p>{{fig:step_approx}}"),
                ("⟦Hàm dấu $\\text{sgn}\\,x$||The sign function $\\text{sgn}\\,x$⟧",
                 "<p>⟦$\\text{sgn}\\,x$ bằng $+1$ hoặc $-1$ theo dấu của $x$, và $\\text{sgn}\\,x=2H(x)-1$ (bước nhảy 2). Khác $H$, nó là hàm lẻ, còn $H$ có cả phần chẵn ($\\tfrac12$) lẫn phần lẻ ($\\tfrac12\\text{sgn}\\,x$): notebook xác nhận {{h_parts_ok}}. Hơn nữa $\\lim\\int_{-a}^{a}\\text{sgn}\\,x\\,dx=0$ còn $\\int_{-a}^{a}H\\,dx=a$ không tồn tại khi $a\\to\\infty$ (tr. 65).||"
                 "$\\text{sgn}\\,x$ equals $+1$ or $-1$ according to the sign of $x$, and $\\text{sgn}\\,x=2H(x)-1$ (a jump of 2). Unlike $H$ it is an odd function, whereas $H$ has both an even part ($\\tfrac12$) and an odd part ($\\tfrac12\\text{sgn}\\,x$): the notebook confirms {{h_parts_ok}}. Moreover $\\lim\\int_{-a}^{a}\\text{sgn}\\,x\\,dx=0$ while $\\int_{-a}^{a}H\\,dx=a$ does not exist as $a\\to\\infty$ (p. 65).⟧</p>"
                 + F("⟦Hàm dấu||Sign function⟧", r"\operatorname{sgn}x=2H(x)-1,\qquad H(x)=\tfrac12+\tfrac12\operatorname{sgn}x")),
            ]),
        # ------------------------------------------------------------ PART 4
        dict(
            title="⟦Hàm sinc, sinc bình phương và các hàm hai chiều||The sinc function, sinc squared and two-dimensional analogues⟧",
            scr=("⟦Hàm $\\sin\\pi x/\\pi x$ xuất hiện trong lọc, nội suy, nhiễu xạ và ăng-ten.||The function $\\sin\\pi x/\\pi x$ appears in filtering, interpolation, diffraction and antennas.⟧",
                 "⟦Nếu không có ký hiệu riêng và chuẩn hóa thống nhất, ta cứ phải viết lại nó và mất dấu các hằng số.||Without a dedicated symbol and a common normalisation we keep rewriting it and losing track of constants.⟧",
                 "⟦Bracewell đặt tên $\\text{sinc}\\,x$ với tung độ trung tâm và diện tích bằng 1, và gắn nó với $\\Pi$ qua biến đổi Fourier.||Bracewell names it $\\text{sinc}\\,x$ with central ordinate and area 1 and ties it to $\\Pi$ through the Fourier transform.⟧"),
            preview=["⟦Tính chất và vai trò lọc thông thấp||Properties and the low-pass role⟧", "⟦Tích phân của sinc và sine integral||The integral of sinc and the sine integral⟧", "⟦$\\text{sinc}^2$, $\\text{jinc}$ và quy ước vẽ||$\\text{sinc}^2$, $\\text{jinc}$ and drawing conventions⟧"],
            slides=[
                ("⟦Định nghĩa và tính chất của $\\text{sinc}\\,x$||Definition and properties of $\\text{sinc}\\,x$⟧",
                 "<p>⟦$\\text{sinc}\\,x=\\sin\\pi x/\\pi x$ có $\\text{sinc}\\,0=1$, triệt tiêu tại mọi số nguyên khác 0, và tổng diện tích bằng 1. Từ \"sinc\" xuất hiện ở Woodward (1953) và được dùng rộng rãi; bảng giá trị ở tr. 508 (tr. 65 đến 66). Notebook: $\\text{sinc}(3)$ = {{sinc_zero}}; $\\int_0^{100}\\text{sinc}$ = {{sinc_int100}}, tiến về $\\tfrac12$ (nửa diện tích 1).||"
                 "$\\text{sinc}\\,x=\\sin\\pi x/\\pi x$ has $\\text{sinc}\\,0=1$, vanishes at every nonzero integer, and has total area 1. The word \"sinc\" appears in Woodward (1953) and has achieved some currency; a table is on p. 508 (pp. 65 to 66). Notebook: $\\text{sinc}(3)$ = {{sinc_zero}}; $\\int_0^{100}\\text{sinc}$ = {{sinc_int100}}, tending to $\\tfrac12$ (half of area 1).⟧</p>"
                 + F("⟦Hàm sinc||The sinc function||⟧".replace("||⟧", "⟧"), r"\operatorname{sinc}x=\frac{\sin\pi x}{\pi x},\quad \operatorname{sinc}0=1,\quad \operatorname{sinc}n=0\ (n\ne0),\quad \int_{-\infty}^{\infty}\operatorname{sinc}x\,dx=1")),
                ("⟦Sinc và $\\Pi$ là một cặp biến đổi||Sinc and $\\Pi$ are a transform pair⟧",
                 "<p>⟦Tính chất đặc biệt của sinc bắt nguồn từ đặc tính phổ: nó chứa mọi tần số tới một giới hạn và không có tần số nào vượt qua, với phổ phẳng tới tần số cắt. Theo cách chọn ký hiệu, $\\text{sinc}\\,x$ và $\\Pi(s)$ là một cặp biến đổi Fourier, nên tần số cắt của sinc là 0.5 chu kỳ trên đơn vị $x$ (tr. 66). Số đo: $\\int_{-1/2}^{1/2}e^{i2\\pi sx}ds$ tại $x=0.3$ là {{sinc_03}}, đúng $\\text{sinc}(0.3)$.||"
                 "The unique properties of sinc go back to its spectral character: it contains components of all frequencies up to a limit and none beyond, with a flat spectrum up to the cutoff. By the choice of notation, $\\text{sinc}\\,x$ and $\\Pi(s)$ are a Fourier transform pair, so the cutoff of sinc is 0.5 cycles per unit of $x$ (p. 66). Measured: $\\int_{-1/2}^{1/2}e^{i2\\pi sx}ds$ at $x=0.3$ is {{sinc_03}}, exactly $\\text{sinc}(0.3)$.⟧</p>"
                 + F("⟦Cặp biến đổi||Transform pair⟧", r"\Pi(x)\ \supset\ \operatorname{sinc}s,\qquad \operatorname{sinc}x\ \supset\ \Pi(s)")),
                ("⟦Sinc trong tích chập: lọc thông thấp lý tưởng và nội suy||Sinc in convolution: ideal low-pass filtering and interpolation⟧",
                 "<p>⟦Khi $\\text{sinc}$ tham gia tích chập, nó lọc thông thấp lý tưởng: bỏ mọi thành phần trên tần số cắt và giữ nguyên mọi thành phần dưới. Trong điều kiện đặc biệt (định lý lấy mẫu, chương 10) nó còn nội suy (tr. 66). Thử số: tín hiệu $\\cos2\\pi(0.2)t+\\cos2\\pi(0.8)t$ chập với sinc cắt cụt: độ lợi tại 0.2 là {{lp_gain_02}} và tại 0.8 là {{lp_gain_08}}; bộ lọc vuông góc qua FFT cho {{lp_gain_02f}} và {{lp_gain_08f}}.||"
                 "When sinc enters convolution it performs ideal low-pass filtering: it removes all components above its cutoff and leaves all below unaltered, and under special circumstances (the sampling theorem, chapter 10) it performs interpolation (p. 66). Test: the signal $\\cos2\\pi(0.2)t+\\cos2\\pi(0.8)t$ convolved with a truncated sinc: the gain at 0.2 is {{lp_gain_02}} and at 0.8 is {{lp_gain_08}}; a brick-wall filter through the FFT gives {{lp_gain_02f}} and {{lp_gain_08f}}.⟧</p>{{fig:sinc_lp}}"),
                ("⟦Tích phân của sinc: sine integral $\\text{Si}$||The integral of sinc: the sine integral $\\text{Si}$⟧",
                 "<p>⟦Với $\\text{Si}\\,x=\\int_0^x\\frac{\\sin u}{u}du$, ta có $\\int_0^x\\text{sinc}\\,u\\,du=\\text{Si}(\\pi x)/\\pi$, $\\text{sinc}\\,x=\\frac{d}{dx}\\frac{\\text{Si}(\\pi x)}{\\pi}$ và $H*\\text{sinc}=\\tfrac12+\\text{Si}(\\pi x)/\\pi$ (hình 4.16, tr. 66 đến 67). Đường tích phân vượt qua 1 trước khi trở về: cực đại là {{gibbs_max}} tại $x=1$, đây là tràn quá kiểu Gibbs.||"
                 "With $\\text{Si}\\,x=\\int_0^x\\frac{\\sin u}{u}du$ we have $\\int_0^x\\text{sinc}\\,u\\,du=\\text{Si}(\\pi x)/\\pi$, $\\text{sinc}\\,x=\\frac{d}{dx}\\frac{\\text{Si}(\\pi x)}{\\pi}$ and $H*\\text{sinc}=\\tfrac12+\\text{Si}(\\pi x)/\\pi$ (Fig. 4.16, pp. 66 to 67). The integral curve overshoots 1 before returning: the maximum is {{gibbs_max}} at $x=1$, a Gibbs-type overshoot.⟧</p>"
                 + F("⟦Sinc và sine integral||Sinc and the sine integral||⟧".replace("||⟧", "⟧"), r"H*\operatorname{sinc}(x)=\int_{-\infty}^{x}\operatorname{sinc}u\,du=\frac12+\frac{\operatorname{Si}(\pi x)}{\pi}")),
                ("⟦Sinc bình phương||Sinc squared⟧",
                 "<p>⟦$\\text{sinc}^2x$ biểu diễn giản đồ bức xạ công suất của ăng-ten kích thích đều, hoặc cường độ ánh sáng trong nhiễu xạ Fraunhofer qua một khe. Có phổ cắt vì bình phương không tạo tần số cao hơn tổng tần số của mọi cặp thành phần. Biến đổi của nó là $\\Lambda(s)$, tần số cắt 1 chu kỳ trên đơn vị (hình 4.17, tr. 66 đến 68). Số đo: $\\text{sinc}^2(0.5)$ = {{sinc2_05}} bằng cả $\\int\\Lambda(s)e^{i2\\pi s/2}ds$ lẫn công thức; diện tích {{sinc2_area}}.||"
                 "$\\text{sinc}^2x$ represents the power radiation pattern of a uniformly excited antenna, or the intensity of light in the Fraunhofer diffraction pattern of a slit. It has a cutoff spectrum since squaring cannot generate frequencies higher than the sum-frequency of any pair of constituents. Its transform is $\\Lambda(s)$, with cutoff one cycle per unit (Fig. 4.17, pp. 66 to 68). Measured: $\\text{sinc}^2(0.5)$ = {{sinc2_05}} by both $\\int\\Lambda(s)e^{i2\\pi s/2}ds$ and the formula; area {{sinc2_area}}.⟧</p>"
                 + F("⟦Sinc bình phương||Sinc squared||⟧".replace("||⟧", "⟧"), r"\operatorname{sinc}^2x\ \supset\ \Lambda(s),\qquad \operatorname{sinc}^2 0=1,\quad \int\operatorname{sinc}^2x\,dx=1")),
                ("⟦Hàm tương tự hai chiều: $\\text{jinc}$||The two-dimensional analogue: $\\text{jinc}$⟧",
                 "<p>⟦Trong hai chiều, hàm tương tự là $J_1(\\pi r)/2r$, có thể tích 1, giá trị trung tâm $\\pi/4$ và biến đổi hai chiều là xung tròn. Một tổng quát khác với tính chất lọc và nội suy tương tự là $\\text{sinc}\\,x\\,\\text{sinc}\\,y$, có biến đổi $\\Pi(u)\\Pi(v)$ (tr. 68). Số đo: giá trị trung tâm {{jinc_center}} và điểm không đầu tiên tại $r$ = {{jinc_zero}}, bán kính của đĩa Airy trong quang học.||"
                 "In two dimensions the analogous function is $J_1(\\pi r)/2r$, which has unit volume, a central value $\\pi/4$ and a two-dimensional transform equal to a circular pulse. Another generalisation with analogous filtering and interpolating properties is $\\text{sinc}\\,x\\,\\text{sinc}\\,y$, with transform $\\Pi(u)\\Pi(v)$ (p. 68). Measured: the central value {{jinc_center}} and the first zero at $r$ = {{jinc_zero}}, the radius of the Airy disc in optics.⟧</p>"),
                ("⟦Quy ước vẽ đồ thị||Graphical conventions⟧",
                 "<p>⟦Để rõ ràng, các định lý về biến đổi được minh họa bằng ví dụ thực khi có thể, và đánh dấu các điểm mà hoành độ và tung độ bằng 1. Đại lượng thuần ảo luôn vẽ bằng nét đứt, nên đại lượng phức được biểu diễn rõ bằng phần thực và phần ảo (hình 4.18); cũng có thể vẽ môđun và pha (hình 4.19), vẽ ba chiều (hình 4.20) hoặc vẽ giá trị $F(s)$ trên mặt phẳng phức (hình 4.21) (tr. 68 đến 69).||"
                 "For clarity, theorems on Fourier transforms are illustrated by real examples where possible, marking the points where the abscissa and ordinate equal unity. Purely imaginary quantities are always drawn dashed, so complex quantities are shown unambiguously by real and imaginary parts (Fig. 4.18); one may also plot modulus and phase (Fig. 4.19), draw in three dimensions (Fig. 4.20) or plot the values of $F(s)$ on the complex plane (Fig. 4.21) (pp. 68 to 69).⟧</p>"),
                ("⟦Bảng 4.1: các ký hiệu đặc biệt||Table 4.1: special symbols⟧",
                 "<p>⟦Bracewell tổng hợp các ký hiệu (tr. 70):||Bracewell collects the symbols (p. 70):⟧</p>"
                 + TBL(["⟦Hàm||Function⟧", "⟦Ký hiệu||Notation⟧"],
                       [["⟦xung chữ nhật||rectangle⟧", "$\\Pi(x)$"], ["⟦tam giác||triangle⟧", "$\\Lambda(x)$"], ["⟦bậc thang Heaviside||Heaviside unit step⟧", "$H(x)$"], ["⟦dấu||sign (signum)⟧", "$\\text{sgn}\\,x$"],
                        ["⟦ký hiệu xung (chương 5)||impulse symbol (chapter 5)⟧", "$\\delta(x)$"], ["⟦ký hiệu lấy mẫu (chương 5)||sampling symbol (chapter 5)⟧", "$\\text{III}(x)=\\sum\\delta(x-n)$"],
                        ["⟦cặp xung chẵn, lẻ||even, odd impulse pair⟧", "$\\text{II}(x)$, $\\text{I}(x)$"], ["⟦lọc, nội suy||filtering, interpolating⟧", "$\\text{sinc}\\,x$"], ["jinc", "$J_1(\\pi x)/2x$"],
                        ["⟦tích chập, tích chập nối tiếp, tương quan||convolution, serial product, correlation⟧", "$*$, $\\{f\\}*\\{g\\}$, $\\star$"]])),
            ]),
        # ------------------------------------------------------------ PART 5
        dict(
            title="⟦Dùng bộ ký hiệu: dựng hàm, cửa sổ và ứng dụng||Using the notation: building functions, windows and applications⟧",
            scr=("⟦Có ký hiệu rồi, ta muốn dựng các hàm thực dụng và dự đoán biến đổi của chúng.||With the notation in hand we want to build practical functions and predict their transforms.⟧",
                 "⟦Một hàm hay bị viết từng khúc, và các cửa sổ khác nhau cho phổ khác nhau (rò phổ ở module 1).||A function often gets written piecewise, and different windows give different spectra (leakage in module 1).⟧",
                 "⟦Gộp $\\Pi$, $\\Lambda$, $H$ dựng hàm ban đầu, so cửa sổ qua thùy phụ, và xem khe quét là tích chập với $\\Pi$.||Combine $\\Pi$, $\\Lambda$, $H$ to build the opening function, compare windows through sidelobes, and see a scanning slit as convolution with $\\Pi$.⟧"),
            preview=["⟦Viết lại hàm mở đầu và bảng cặp biến đổi||Rewriting the opening function and a table of transform pairs⟧", "⟦Ba cửa sổ và thùy phụ||Three windows and their sidelobes⟧", "⟦Khe quét và trung bình trượt||A scanning slit and running means⟧"],
            slides=[
                ("⟦Viết lại hàm mở đầu||Rewriting the opening function⟧",
                 "<p>⟦Hàm $f(x)$ ở đầu chương (0, rồi $x$ trên $[0,1]$, rồi 1) là $R(x)-R(x-1)$, cũng là $x\\,\\Pi(x-\\tfrac12)+H(x-1)$. Ba cách viết đều trùng khớp trên lưới ({{ramp_ok}}); tại $x=0.4$ bằng {{ramp_04}}.||"
                 "The function $f(x)$ from the start of the chapter (0, then $x$ on $[0,1]$, then 1) equals $R(x)-R(x-1)$, and also $x\\,\\Pi(x-\\tfrac12)+H(x-1)$. All three writings coincide on a grid ({{ramp_ok}}); at $x=0.4$ it equals {{ramp_04}}.⟧</p>"
                 + F("⟦Bậc thang có dốc||Ramp-step function⟧", r"f(x)=R(x)-R(x-1)=x\,\Pi\!\left(x-\tfrac12\right)+H(x-1)")),
                ("⟦Bảng cặp biến đổi cho các hàm vừa học||Transform pairs for the functions just learned⟧",
                 "<p>⟦Sách sẽ tra cứu các cặp này ở chương 22; ở đây ta kiểm bằng số tại $s=0.3$ (tích phân số so với công thức; {{pairs_ok}} trên 5 cặp đúng):||The book tabulates these pairs in chapter 22; here we check them numerically at $s=0.3$ (numerical integral versus formula; {{pairs_ok}} of 5 pairs hold):⟧</p>"
                 + TBL(["$f(x)$", "$F(s)$", "F(0.3)"],
                       [["$\\Pi(x)$", "$\\text{sinc}\\,s$", "{{p_pi_03}}"], ["$\\Lambda(x)$", "$\\text{sinc}^2s$", "{{p_tri_03}}"], ["$e^{-\\pi x^2}$", "$e^{-\\pi s^2}$", "{{p_g_03}}"],
                        ["$e^{-|x|}$", "$2/(1+4\\pi^2s^2)$", "{{p_exp_03}}"], ["$e^{-x}H(x)$", "$1/(1+i2\\pi s)$", "|F| = {{p_caus_03}}"]])),
                ("⟦Ba cửa sổ: chữ nhật, tam giác, Gauss||Three windows: rectangle, triangle, Gaussian⟧",
                 "<p>⟦Cắt tín hiệu bằng một cửa sổ nhân phổ với biến đổi của cửa sổ. Biến đổi của $\\Pi$ là $\\text{sinc}\\,s$, của $\\Lambda$ là $\\text{sinc}^2s$, của Gauss là Gauss. Thùy phụ đầu của $\\text{sinc}$ có độ lớn {{sl_rect}} ({{sl_rect_db}} dB), thùy phụ đầu của $\\text{sinc}^2$ chỉ {{sl_tri}} ({{sl_tri_db}} dB), còn Gauss không có thùy phụ. Đây là lý do rò phổ ở module 1 nặng với cửa sổ chữ nhật.||"
                 "Cutting a signal with a window multiplies the spectrum by the window's transform's convolution. The transform of $\\Pi$ is $\\text{sinc}\\,s$, of $\\Lambda$ is $\\text{sinc}^2s$, of a Gaussian a Gaussian. The first sidelobe of $\\text{sinc}$ has magnitude {{sl_rect}} ({{sl_rect_db}} dB), that of $\\text{sinc}^2$ only {{sl_tri}} ({{sl_tri_db}} dB), and the Gaussian has none. That is why leakage in module 1 is heavy with the rectangular window.⟧</p>{{fig:windows}}"),
                ("⟦Đánh đổi: thùy phụ và bề rộng thùy chính||The trade-off: sidelobes versus main-lobe width⟧",
                 "<p>⟦Cửa sổ tam giác hạ thùy phụ nhưng thùy chính rộng gấp đôi (điểm không tại $|s|=1$ so với 0.5 của chữ nhật khi cùng bề rộng chân $b=1$; tam giác đáy 2 cho điểm không tại 1). Không có cửa sổ nào cùng lúc có thùy phụ thấp và thùy chính hẹp; đây là biểu hiện của quan hệ bất định (chương 8).||"
                 "The triangular window lowers the sidelobes but widens the main lobe (a null at $|s|=1$ versus 0.5 for the rectangle at the same base $b=1$; a triangle of base 2 has its null at 1). No window has both low sidelobes and a narrow main lobe; this is a manifestation of the uncertainty relation (chapter 8).⟧</p>"),
                ("⟦Khe quét là tích chập với $\\Pi$||A scanning slit is convolution with $\\Pi$⟧",
                 "<p>⟦Rãnh âm thanh quang học trên phim cũ được quét bằng khe rộng $w$, và việc quét đưa vào tích chập với xung chữ nhật rộng $w$ (bài tập 23 chương 3, tr. 53). Với rãnh hình sin chu kỳ $p=1$: khe $w=0.25$ giữ {{slit_025}}, $w=0.5$ giữ {{slit_05}}, $w=1$ giữ {{slit_1}} (tiếng bị triệt tiêu hoàn toàn). Độ lợi là $\\text{sinc}(wf_0)$.||"
                 "The optical sound track on old motion-picture film is scanned by a slit of width $w$, and the scanning introduces convolution with a rectangle of width $w$ (chapter 3 problem 23, p. 53). For a sinusoidal track of period $p=1$: a slit $w=0.25$ keeps {{slit_025}}, $w=0.5$ keeps {{slit_05}}, $w=1$ keeps {{slit_1}} (the tone is wiped out completely). The gain is $\\text{sinc}(wf_0)$.⟧</p>"
                 + F("⟦Độ lợi của khe||Slit gain⟧", r"\text{gain}=\left|\operatorname{sinc}(w f_0)\right|")),
                ("⟦Trung bình trượt $L$ điểm và sinc||An $L$-point running mean and sinc⟧",
                 "<p>⟦Trung bình trượt là tích chập với $\\Pi$ nên đáp ứng tần số là sinc, chính xác hơn là nhân Dirichlet cho dãy rời rạc. Với $L=8$ tại $f=0.05$ chu kỳ trên mẫu: giá trị chính xác {{ma_exact}} (đo bằng <code>freqz</code> và bằng công thức) và xấp xỉ sinc {{ma_sinc}}. Xấp xỉ tốt khi $L$ lớn và $f$ nhỏ.||"
                 "A running mean is convolution with $\\Pi$, so its frequency response is sinc, more precisely the Dirichlet kernel for a discrete sequence. For $L=8$ at $f=0.05$ cycles per sample: the exact value is {{ma_exact}} (measured with <code>freqz</code> and by the formula) and the sinc approximation {{ma_sinc}}. The approximation is good for large $L$ and small $f$.⟧</p>"
                 + F("⟦Nhân Dirichlet và sinc||Dirichlet kernel and sinc⟧", r"\left|\frac{\sin(\pi Lf)}{L\sin(\pi f)}\right|\ \approx\ \left|\operatorname{sinc}(Lf)\right|")),
                ("⟦Mẹo dùng bộ ký hiệu||Tips for using the notation⟧",
                 UL(["⟦Đặt $H(0)=\\tfrac12$ hoặc không nêu; đừng nhấn mạnh giá trị tại bước nhảy khi vẽ (tr. 57, 63).||Set $H(0)=\\tfrac12$ or do not mention it; do not emphasise the value at a jump when drawing (pp. 57, 63).⟧",
                     "⟦Dùng $H$ để đưa cận tích phân thay đổi về cận cố định (tr. 62).||Use $H$ to turn variable integration limits into constant ones (p. 62).⟧",
                     "⟦Chọn $e^{-\\pi x^2}$ khi cần tự biến đổi; đổi về thống kê bằng $\\sigma=(2\\pi)^{-1/2}$ (tr. 58).||Choose $e^{-\\pi x^2}$ when self-transformation is wanted; convert to the statistical form with $\\sigma=(2\\pi)^{-1/2}$ (p. 58).⟧",
                     "⟦Vẽ đại lượng ảo bằng nét đứt (tr. 68).||Draw imaginary quantities dashed (p. 68).⟧"])),
                ("⟦Liên hệ chéo với Barkat||Cross-reference to Barkat⟧",
                 "<p>⟦Gauss và Rayleigh của module này chính là các phân phối ở Barkat mục 2.3.2 (Normal) và 2.3.6 (Rayleigh, Rice, Maxwell). Hàm bậc thang và xung được Barkat dùng ở mục 1.3.1 để viết phân phối tích lũy và mật độ của biến ngẫu nhiên rời rạc: $F_X(x)=\\sum_kP_k\\,H(x-x_k)$. Module 11 dùng cả hai.||"
                 "The Gaussian and Rayleigh of this module are the distributions of Barkat sections 2.3.2 (Normal) and 2.3.6 (Rayleigh, Rice, Maxwell). Barkat uses the step and the impulse in section 1.3.1 to write the cumulative distribution and density of a discrete random variable: $F_X(x)=\\sum_kP_k\\,H(x-x_k)$. Module 11 uses both.⟧</p>"
                 + F("⟦Phân phối tích lũy của biến rời rạc||Cumulative distribution of a discrete variable⟧", r"F_X(x)=\sum_kP_k\,H(x-x_k),\qquad f_X(x)=\sum_kP_k\,\delta(x-x_k)")),
                ("⟦Tự kiểm tra||Self-check⟧",
                 UL(["⟦Viết $\\Lambda(x)$ bằng $\\Pi$ và viết $\\Pi(x)$ bằng $H$.||Write $\\Lambda(x)$ using $\\Pi$ and $\\Pi(x)$ using $H$.⟧",
                     "⟦Sinc triệt tiêu ở đâu và tần số cắt của nó là bao nhiêu?||Where does sinc vanish and what is its cutoff?⟧",
                     "⟦Vì sao đỉnh của Rayleigh không nằm ở gốc dù Gauss hai chiều có đỉnh ở gốc?||Why does the Rayleigh peak lie away from the origin although the 2D Gaussian peaks there?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: $\\Pi*\\Pi$ và $H(x+\\tfrac12)-H(x-\\tfrac12)$; số nguyên khác 0 và 0.5; vì diện tích vòng $2\\pi r\\,dr$ tăng theo $r$.||Hints: $\\Pi*\\Pi$ and $H(x+\\tfrac12)-H(x-\\tfrac12)$; nonzero integers and 0.5; because the ring area $2\\pi r\\,dr$ grows with $r$.⟧</p>"),
            ]),
    ],
    takeaways=[
        "⟦$\\Pi$ là cổng, $\\Lambda=\\Pi*\\Pi$ là tam giác, và tổ hợp $H$, $R$ dựng mọi hàm đa giác và bật tắt.||$\\Pi$ is a gate, $\\Lambda=\\Pi*\\Pi$ is the triangle, and combinations of $H$ and $R$ build every polygonal and switching function.⟧",
        "⟦Gauss $e^{-\\pi x^2}$ có tung độ trung tâm và diện tích bằng 1 và tự biến đổi; $\\sigma=(2\\pi)^{-1/2}$.||The Gaussian $e^{-\\pi x^2}$ has central ordinate and area 1 and is self-transforming; $\\sigma=(2\\pi)^{-1/2}$.⟧",
        "⟦Tích chập với $H$ là tích phân; $H(0)$ hầu như không cần nêu; $\\text{sgn}\\,x=2H-1$ là hàm lẻ.||Convolution with $H$ is integration; $H(0)$ hardly needs stating; $\\text{sgn}\\,x=2H-1$ is odd.⟧",
        "⟦$\\text{sinc}\\,x\\supset\\Pi(s)$: điểm không tại số nguyên, tần số cắt 0.5, lọc thông thấp lý tưởng; $\\text{sinc}^2\\supset\\Lambda$ với tần số cắt 1.||$\\text{sinc}\\,x\\supset\\Pi(s)$: zeros at integers, cutoff 0.5, ideal low-pass; $\\text{sinc}^2\\supset\\Lambda$ with cutoff 1.⟧",
        "⟦Cửa sổ tam giác hạ thùy phụ so với chữ nhật, đánh đổi bằng thùy chính rộng hơn.||The triangular window lowers sidelobes compared with the rectangle, at the cost of a wider main lobe.⟧",
    ],
    history="<p>⟦Chương mở đầu bằng nhận xét lịch sử: Fourier quan tâm tới hàm cho bằng đồ thị, và theo E. W. Hobson ông là người đầu tiên hiểu rằng một hàm có thể gồm các phần rời nhau cho tùy ý (tr. 55).||"
            "The chapter opens with a historical remark: Fourier was concerned with functions given graphically, and according to E. W. Hobson he was the first to grasp that a function may consist of detached portions given arbitrarily (p. 55).⟧</p>"
            "<p>⟦Từ \"sinc\" xuất hiện ở Woodward (1953) và đã được dùng rộng rãi (tr. 66). Tên \"thừa số gián đoạn Dirichlet\" cho $\\Pi$ gắn với lý thuyết hội tụ chuỗi Fourier (tr. 57). Bài toán \"bước đi của người say\" gắn với Rayleigh (tr. 60), và hàm bậc thang mang tên Heaviside (tr. 61).||"
            "The word \"sinc\" appears in Woodward (1953) and has achieved some currency (p. 66). The name \"Dirichlet's discontinuous factor\" for $\\Pi$ belongs to the theory of convergence of Fourier series (p. 57). The \"drunkard's walk\" problem is attached to Rayleigh (p. 60), and the step function bears Heaviside's name (p. 61).⟧</p>",
    case="<p>⟦<b>Khe quét làm mất tiếng.</b> Trên phim cũ, âm thanh nằm ở rãnh quang học và được đọc bằng khe rộng $w$; việc đọc là tích chập với $\\Pi$ rộng $w$. Một âm thuần ứng với chu kỳ rãnh $p=1$: khe $w=0.25$ giữ {{slit_025}} biên độ, $w=0.5$ giữ {{slit_05}}, và khe $w=1$ (bằng đúng một chu kỳ) xóa sạch âm ({{slit_1}}). Bản chất là độ lợi $\\text{sinc}(wf_0)$ với điểm không tại $wf_0=1$.||"
          "<b>A slit that wipes out a tone.</b> On old film the sound sits in an optical track and is read through a slit of width $w$; reading is convolution with a $\\Pi$ of width $w$. A pure tone of track period $p=1$: a slit $w=0.25$ keeps {{slit_025}} of the amplitude, $w=0.5$ keeps {{slit_05}}, and a slit $w=1$ (exactly one period) erases the tone ({{slit_1}}). The essence is the gain $\\text{sinc}(wf_0)$ with a zero at $wf_0=1$.⟧</p>"
         "<p>⟦Cùng cơ chế giải thích vì sao trung bình trượt có điểm không (module 3) và vì sao cửa sổ chữ nhật rò phổ (module 1): mọi lần cắt bằng $\\Pi$ đều nhân phổ với sinc.||The same mechanism explains why running means have zeros (module 3) and why the rectangular window leaks (module 1): every cut by $\\Pi$ multiplies the spectrum by sinc.⟧</p>",
    practice=[
        "⟦Mở notebook và chạy cell cài đặt.||Open the notebook and run the setup cell.⟧",
        "⟦Bài 1: dựng bậc thang có dốc, hàm đa giác và các bảng cặp biến đổi bằng $\\Pi,\\Lambda,H$; thử một hàm đa giác khác của bạn.||Task 1: build the ramp-step, a polygonal function and the transform-pair table with $\\Pi,\\Lambda,H$; try another polygonal function of your own.⟧",
        "⟦Bài 2: tự tính các thông số phân tán của một Gauss có $\\sigma=2$ và kiểm bằng mô phỏng.||Task 2: compute the dispersion parameters of a Gaussian with $\\sigma=2$ yourself and check by simulation.⟧",
        "⟦Bài 3: thay lưới của mô phỏng Rayleigh bằng 3 chiều (phân phối Maxwell) và dự đoán đỉnh.||Task 3: extend the Rayleigh simulation to 3 dimensions (the Maxwell distribution) and predict the peak.⟧",
        "⟦Bài 4: lọc tín hiệu hai tần số bằng sinc cắt cụt ở nhiều độ dài, xem độ lợi hội tụ ra sao.||Task 4: filter a two-tone signal with a truncated sinc of several lengths and see how the gain converges.⟧",
        "⟦Bài 5: so ba cửa sổ trên một tín hiệu có hai vạch gần nhau và vạch yếu; cửa sổ nào tách được?||Task 5: compare three windows on a signal with two close lines and a weak one; which window separates them?⟧",
    ],
    pitfalls=[
        "<b>⟦\"$\\Pi(\\pm\\tfrac12)$ phải được quy định để tích phân đúng.\"||\"$\\Pi(\\pm\\tfrac12)$ must be specified for integrals to be right.\"⟧</b><p>⟦Không: một điểm không đổi tích phân (lệch {{edge_diff}} giữa các quy ước). Bracewell hầu như không nêu (tr. 57).||No: a single point does not change an integral (deviation {{edge_diff}} between conventions). Bracewell almost never states it (p. 57).⟧</p>",
        "<b>⟦\"Gauss trong thống kê và trong giáo trình này là một.\"||\"The Gaussian in statistics and in this book are the same.\"⟧</b><p>⟦Khác chuẩn hóa: thống kê dùng $\\sigma=1$ và diện tích 1; giáo trình dùng $e^{-\\pi x^2}$, có $\\sigma$ = {{g_sd}} và tung độ trung tâm 1 (tr. 58).||They differ in normalisation: statistics uses $\\sigma=1$ and area 1; the book uses $e^{-\\pi x^2}$, with $\\sigma$ = {{g_sd}} and central ordinate 1 (p. 58).⟧</p>",
        "<b>⟦\"Khoảng cách của người say nhiều khả năng nhất là 0 vì Gauss có đỉnh ở gốc.\"||\"The most likely distance of the drunkard is 0 because the Gaussian peaks at the origin.\"⟧</b><p>⟦Mật độ theo $(x,y)$ có đỉnh ở gốc, còn mật độ theo khoảng cách nhân thêm $2\\pi r$ nên đỉnh tại $r=\\sigma$: mô phỏng cho {{ray_mode_mc}} (tr. 60).||The density in $(x,y)$ peaks at the origin, but the density in distance carries the extra factor $2\\pi r$ so it peaks at $r=\\sigma$: the simulation gives {{ray_mode_mc}} (p. 60).⟧</p>",
        "<b>⟦\"Sinc là bộ lọc lý tưởng nên dùng ngay được.\"||\"Sinc is the ideal filter, so use it as is.\"⟧</b><p>⟦Sinc kéo dài vô hạn và không nhân quả, phải cắt cụt; khi cắt độ lợi tại 0.2 chỉ còn {{lp_gain_02}} thay vì 1, và tích phân của nó vượt tới {{gibbs_max}} (tràn quá).||Sinc is infinite and non-causal and must be truncated; when truncated the gain at 0.2 is {{lp_gain_02}} instead of 1, and its integral overshoots to {{gibbs_max}}.⟧</p>",
    ],
    refs=[
        "⟦R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chương 4 (tr. 55 đến 70) và chương 3, bài tập 23 (tr. 53).||R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chapter 4 (pp. 55 to 70) and chapter 3, problem 23 (p. 53).⟧",
        "⟦M. Barkat, <i>Signal Detection and Estimation</i>, 2nd ed., Artech House, 2005, mục 1.3.1, 2.3.2 và 2.3.6, chỉ dẫn tới ở phần liên hệ chéo.||M. Barkat, <i>Signal Detection and Estimation</i>, 2nd ed., Artech House, 2005, sections 1.3.1, 2.3.2 and 2.3.6, cited only in the cross-reference.⟧",
    ],
    quiz=[
        dict(q="⟦Xung chữ nhật $h\\,\\Pi[(x-c)/b]$ với $h=3$, $b=2$, $c=1$ có diện tích bằng bao nhiêu?||What is the area of the rectangle $h\\,\\Pi[(x-c)/b]$ with $h=3$, $b=2$, $c=1$?⟧",
             opts=["{{rect_area}}", "3", "9", "12"], explain="⟦Diện tích $hb$ = {{rect_area}}, không phụ thuộc tâm $c$.||The area $hb$ = {{rect_area}}, independent of the centre $c$.⟧"),
        dict(q="⟦$\\int\\Pi(x)\\cos^2\\pi x\\,dx$ bằng bao nhiêu?||What does $\\int\\Pi(x)\\cos^2\\pi x\\,dx$ equal?⟧",
             opts=["{{gate_energy}}", "1", "0.6366", "0.25"], explain="⟦$\\int_{-1/2}^{1/2}\\cos^2\\pi x\\,dx$ = {{gate_energy}}.||$\\int_{-1/2}^{1/2}\\cos^2\\pi x\\,dx$ = {{gate_energy}}.⟧"),
        dict(q="⟦Hàm đa giác qua $(0,0),(1,2),(2,1),(3,3),(4,0)$ có giá trị nào tại $x=2.5$?||What value does the polygonal function through $(0,0),(1,2),(2,1),(3,3),(4,0)$ take at $x=2.5$?⟧",
             opts=["{{poly_25}}", "1.5", "3", "2.5"], explain="⟦Trung điểm của 1 và 3 là {{poly_25}}; tổng $\\sum y_k\\Lambda(x-k)$ trùng nội suy tuyến tính.||The midpoint of 1 and 3 is {{poly_25}}; the sum $\\sum y_k\\Lambda(x-k)$ equals linear interpolation.⟧"),
        dict(q="⟦Độ lệch chuẩn $\\sigma$ của Gauss $e^{-\\pi x^2}$ (dạng của Bracewell) bằng bao nhiêu?||What is the standard deviation $\\sigma$ of the Gaussian $e^{-\\pi x^2}$ (Bracewell's form)?⟧",
             opts=["{{g_sd}}", "1", "0.3183", "0.5642"], explain="⟦$\\sigma=(2\\pi)^{-1/2}$ = {{g_sd}}; giá trị trung bình của $x^2$ là {{g_var}}.||$\\sigma=(2\\pi)^{-1/2}$ = {{g_sd}}; the mean of $x^2$ is {{g_var}}.⟧"),
        dict(q="⟦$\\int_0^1e^{-\\pi t^2}dt$ bằng bao nhiêu?||What does $\\int_0^1e^{-\\pi t^2}dt$ equal?⟧",
             opts=["{{g_int1}}", "0.5", "0.4599", "0.9876"], explain="⟦$\\tfrac12\\text{erf}(\\sqrt\\pi)$ = {{g_int1}}.||$\\tfrac12\\text{erf}(\\sqrt\\pi)$ = {{g_int1}}.⟧"),
        dict(q="⟦Sai số xác suất (nửa khoảng tứ phân vị) của $e^{-\\pi x^2}$ bằng bao nhiêu?||What is the probable error (semi-interquartile range) of $e^{-\\pi x^2}$?⟧",
             opts=["{{pe}}", "0.3183", "0.3989", "0.4697"], explain="⟦$0.6745\\sigma$ = {{pe}}; tích phân số và tìm nghiệm cho cùng giá trị.||$0.6745\\sigma$ = {{pe}}; numerical integration and root finding give the same value.⟧"),
        dict(q="⟦Độ rộng tại nửa đỉnh của $e^{-\\pi x^2}$ bằng bao nhiêu?||What is the width to half-peak of $e^{-\\pi x^2}$?⟧",
             opts=["{{fwhm}}", "1", "0.4697", "1.1774"], explain="⟦$2\\sqrt{\\ln2/\\pi}$ = {{fwhm}}; độ rộng tương đương là {{eqw}}.||$2\\sqrt{\\ln2/\\pi}$ = {{fwhm}}; the equivalent width is {{eqw}}.⟧"),
        dict(q="⟦Với phân phối chuẩn, bao nhiêu phần trăm nằm trong một độ lệch chuẩn?||For a normal distribution, what percentage lies within one standard deviation?⟧",
             opts=["{{cov_sd}}", "50", "57.51", "95.45"], explain="⟦Bằng $\\text{erf}(1/\\sqrt2)$ = {{cov_sd}} phần trăm; trong sai số tuyệt đối trung bình là {{cov_mad}}.||Equal to $\\text{erf}(1/\\sqrt2)$ = {{cov_sd}} percent; within the mean absolute error it is {{cov_mad}}.⟧"),
        dict(q="⟦Khoảng cách trung bình tới gốc của Gauss hai chiều $\\sigma=1$ bằng bao nhiêu?||What is the mean distance to the origin of a two-dimensional Gaussian with $\\sigma=1$?⟧",
             opts=["{{ray_mean_th}}", "1", "0.7979", "1.4142"], explain="⟦Trung bình Rayleigh là $\\sigma\\sqrt{\\pi/2}$ = {{ray_mean_th}}; mô phỏng cho {{ray_mean_mc}}.||The Rayleigh mean is $\\sigma\\sqrt{\\pi/2}$ = {{ray_mean_th}}; the simulation gives {{ray_mean_mc}}.⟧"),
        dict(q="⟦Xác suất điểm Gauss hai chiều $\\sigma=1$ nằm trong $r<\\sigma$ bằng bao nhiêu?||What is the probability that a two-dimensional Gaussian ($\\sigma=1$) point lies within $r<\\sigma$?⟧",
             opts=["{{ray_p1_th}}", "0.6827", "0.5", "0.6065"], explain="⟦$1-e^{-1/2}$ = {{ray_p1_th}}; mô phỏng {{ray_p1_mc}}. Khác 68.27 phần trăm của Gauss một chiều.||$1-e^{-1/2}$ = {{ray_p1_th}}; simulation {{ray_p1_mc}}. Different from the 68.27 percent of the one-dimensional Gaussian.⟧"),
        dict(q="⟦$\\int\\cos x\\,|\\tau|^{-1}e^{-\\pi x^2/\\tau^2}dx$ với $\\tau=0.5$ bằng bao nhiêu?||What is $\\int\\cos x\\,|\\tau|^{-1}e^{-\\pi x^2/\\tau^2}dx$ for $\\tau=0.5$?⟧",
             opts=["{{gs_05}}", "0.9235", "0.9992", "0.8521"], explain="⟦$e^{-\\tau^2/4\\pi}$ = {{gs_05}}, tiến về $\\cos0=1$ khi $\\tau\\to0$.||$e^{-\\tau^2/4\\pi}$ = {{gs_05}}, tending to $\\cos0=1$ as $\\tau\\to0$.⟧"),
        dict(q="⟦Tích chập số của $H$ với $e^{-\\pi x^2}$ tại $x=0.5$ bằng bao nhiêu?||What is the numerical convolution of $H$ with $e^{-\\pi x^2}$ at $x=0.5$?⟧",
             opts=["{{hf_05}}", "0.5", "0.7887", "0.9545"], explain="⟦Bằng $\\tfrac12[1+\\text{erf}(\\sqrt\\pi\\cdot0.5)]$ = {{hf_05}}: tích chập với $H$ là tích phân.||Equal to $\\tfrac12[1+\\text{erf}(\\sqrt\\pi\\cdot0.5)]$ = {{hf_05}}: convolution with $H$ is integration.⟧"),
        dict(q="⟦Đạo hàm đối xứng của hàm dốc $R$ tại 0 (với $H(0)=\\tfrac12$) bằng bao nhiêu?||What is the symmetric derivative of the ramp $R$ at 0 (with $H(0)=\\tfrac12$)?⟧",
             opts=["{{r_prime0}}", "1", "0", "0.25"], explain="⟦$[R(\\Delta)-R(-\\Delta)]/2\\Delta=\\tfrac12$ = {{r_prime0}}, đúng giá trị giữa.||$[R(\\Delta)-R(-\\Delta)]/2\\Delta=\\tfrac12$ = {{r_prime0}}, the midvalue.⟧"),
        dict(q="⟦Xấp xỉ $\\tfrac12+\\frac1\\pi\\arctan(x/\\tau)$ tại $x=0.1$ với $\\tau=0.01$ bằng bao nhiêu?||What is the approximation $\\tfrac12+\\frac1\\pi\\arctan(x/\\tau)$ at $x=0.1$ with $\\tau=0.01$?⟧",
             opts=["{{arctan_2}}", "0.75", "0.9995", "0.8524"], explain="⟦$\\tfrac12+\\arctan(10)/\\pi$ = {{arctan_2}}; với $\\tau=0.1$ là {{arctan_1}}.||$\\tfrac12+\\arctan(10)/\\pi$ = {{arctan_2}}; with $\\tau=0.1$ it is {{arctan_1}}.⟧"),
        dict(q="⟦$H*\\text{sinc}$ đạt cực đại (tràn quá) bằng bao nhiêu?||What maximum (overshoot) does $H*\\text{sinc}$ reach?⟧",
             opts=["{{gibbs_max}}", "1", "1.1789", "1.0179"], explain="⟦$\\tfrac12+\\text{Si}(\\pi)/\\pi$ = {{gibbs_max}} tại $x=1$.||$\\tfrac12+\\text{Si}(\\pi)/\\pi$ = {{gibbs_max}} at $x=1$.⟧"),
        dict(q="⟦$\\text{sinc}(0.3)$ bằng bao nhiêu?||What is $\\text{sinc}(0.3)$?⟧",
             opts=["{{sinc_03}}", "0.8090", "0.9549", "0.7568"], explain="⟦$\\sin(0.3\\pi)/(0.3\\pi)$ = {{sinc_03}}; cũng bằng $\\int_{-1/2}^{1/2}e^{i2\\pi s(0.3)}ds$.||$\\sin(0.3\\pi)/(0.3\\pi)$ = {{sinc_03}}; also equal to $\\int_{-1/2}^{1/2}e^{i2\\pi s(0.3)}ds$.⟧"),
        dict(q="⟦Sau khi lọc bằng sinc cắt cụt, độ lợi tại tần số 0.8 (trên tần số cắt 0.5) gần bằng bao nhiêu?||After filtering with a truncated sinc, what is the gain at frequency 0.8 (above the 0.5 cutoff), approximately?⟧",
             opts=["{{lp_gain_08}}", "1", "0.5", "0.0212"], explain="⟦Sinc lý tưởng bỏ hoàn toàn 0.8; bản cắt cụt còn {{lp_gain_08}}, và giữ {{lp_gain_02}} tại 0.2.||An ideal sinc removes 0.8 entirely; the truncated version leaves {{lp_gain_08}}, and keeps {{lp_gain_02}} at 0.2.⟧"),
        dict(q="⟦Điểm không đầu tiên của $J_1(\\pi r)/2r$ nằm ở $r$ bằng bao nhiêu?||At which $r$ is the first zero of $J_1(\\pi r)/2r$?⟧",
             opts=["{{jinc_zero}}", "1", "0.5", "1.4303"], explain="⟦$3.8317/\\pi$ = {{jinc_zero}} (đĩa Airy); giá trị trung tâm là $\\pi/4$ = {{jinc_center}}.||$3.8317/\\pi$ = {{jinc_zero}} (the Airy disc); the central value is $\\pi/4$ = {{jinc_center}}.⟧"),
        dict(q="⟦Thùy phụ đầu của biến đổi cửa sổ chữ nhật thấp hơn đỉnh bao nhiêu dB?||How many dB below the peak is the first sidelobe of the rectangular window's transform?⟧",
             opts=["{{sl_rect_db}}", "-6.02", "-26.52", "-3.01"], explain="⟦$|\\text{sinc}|$ cực đại ngoài thùy chính là {{sl_rect}}, tức {{sl_rect_db}} dB.||The largest $|\\text{sinc}|$ outside the main lobe is {{sl_rect}}, i.e. {{sl_rect_db}} dB.⟧"),
        dict(q="⟦Thùy phụ đầu của cửa sổ tam giác (biến đổi $\\text{sinc}^2$) thấp hơn đỉnh bao nhiêu dB?||How many dB below the peak is the first sidelobe of the triangular window ($\\text{sinc}^2$ transform)?⟧",
             opts=["{{sl_tri_db}}", "-13.26", "-6.63", "-39.78"], explain="⟦Bình phương thùy phụ của sinc: {{sl_tri}}, tức {{sl_tri_db}} dB, gấp đôi số dB của cửa sổ chữ nhật.||The square of the sinc sidelobe: {{sl_tri}}, i.e. {{sl_tri_db}} dB, twice the dB of the rectangular window.⟧"),
        dict(q="⟦Rãnh hình sin chu kỳ 1 được quét bằng khe rộng 0.5. Biên độ còn lại bao nhiêu?||A sinusoidal track of period 1 is scanned by a slit of width 0.5. What amplitude remains?⟧",
             opts=["{{slit_05}}", "0.5", "0.9003", "0.3183"], explain="⟦Độ lợi $\\text{sinc}(0.5)$ = {{slit_05}}; đo bằng tích chập số trùng công thức.||The gain $\\text{sinc}(0.5)$ = {{slit_05}}; measured by numerical convolution it matches the formula.⟧"),
        dict(q="⟦Cũng rãnh đó nhưng khe rộng bằng đúng một chu kỳ ($w=1$): biên độ còn lại bao nhiêu?||The same track with a slit exactly one period wide ($w=1$): what amplitude remains?⟧",
             opts=["{{slit_1}}", "0.6366", "0.5", "0.3679"], explain="⟦$\\text{sinc}(1)=0$: khe rộng một chu kỳ xóa sạch âm.||$\\text{sinc}(1)=0$: a slit one period wide wipes the tone out.⟧"),
        dict(q="⟦Trung bình trượt 8 điểm tại 0.05 chu kỳ trên mẫu có độ lớn chính xác bao nhiêu?||What is the exact magnitude of an 8-point running mean at 0.05 cycles per sample?⟧",
             opts=["{{ma_exact}}", "{{ma_sinc}}", "0.6366", "0.8090"], explain="⟦Nhân Dirichlet cho {{ma_exact}}, còn xấp xỉ sinc {{ma_sinc}}.||The Dirichlet kernel gives {{ma_exact}}, the sinc approximation {{ma_sinc}}.⟧"),
        dict(q="⟦Biến đổi của $e^{-|x|}$ tại $s=0.3$ bằng bao nhiêu?||What is the transform of $e^{-|x|}$ at $s=0.3$?⟧",
             opts=["{{p_exp_03}}", "0.7537", "0.8584", "0.2170"], explain="⟦$2/(1+4\\pi^2s^2)$ = {{p_exp_03}}, tích phân số trùng.||$2/(1+4\\pi^2s^2)$ = {{p_exp_03}}, numerical integration agrees.⟧"),
        dict(q="⟦$\\text{sinc}^2(0.5)$ bằng bao nhiêu?||What is $\\text{sinc}^2(0.5)$?⟧",
             opts=["{{sinc2_05}}", "0.6366", "0.2026", "0.5"], explain="⟦$(2/\\pi)^2$ = {{sinc2_05}}, đúng $\\int\\Lambda(s)e^{i2\\pi s/2}ds$.||$(2/\\pi)^2$ = {{sinc2_05}}, exactly $\\int\\Lambda(s)e^{i2\\pi s/2}ds$.⟧"),
        dict(q="⟦Vì sao có thể viết $\\Pi(x)=H(x+\\tfrac12)-H(x-\\tfrac12)$?||Why can we write $\\Pi(x)=H(x+\\tfrac12)-H(x-\\tfrac12)$?⟧",
             opts=["⟦Nó chỉ có hai bước nhảy đơn vị, một dương và một âm||It has only two unit discontinuities, one positive and one negative⟧",
                   "⟦Vì $H$ là đạo hàm của $\\Pi$ nên hiệu hai $H$ dịch trở lại được $\\Pi$ qua tích phân||Because $H$ is the derivative of $\\Pi$, so the difference of two shifted $H$ returns $\\Pi$ through integration⟧",
                   "⟦Vì $\\Pi$ là tích chập của hai bậc thang cùng bề rộng đặt đối xứng quanh gốc||Because $\\Pi$ is the convolution of two steps of equal width placed symmetrically about the origin⟧",
                   "⟦Vì $H(x)$ chẵn nên hiệu hai $H$ dịch đối xứng luôn là hàm chẵn có giá trị 1||Because $H(x)$ is even, so the difference of two symmetrically shifted $H$ is always an even function of value 1⟧"],
             explain="⟦Bracewell, tr. 61: bỏ hai bước nhảy đi thì không còn gì nên $\\Pi$ biểu diễn được hoàn toàn bằng bậc thang.||Bracewell, p. 61: remove the two jumps and nothing remains, so $\\Pi$ is expressible entirely in terms of step functions.⟧"),
        dict(q="⟦Tích chập với $H$ làm gì?||What does convolution with $H$ do?⟧",
             opts=["⟦Lấy tích phân từ $-\\infty$ tới $x$||Integrates from $-\\infty$ to $x$⟧",
                   "⟦Lấy đạo hàm theo $x$ vì $H$ là hàm bậc thang có đạo hàm bằng xung||Differentiates with respect to $x$, since $H$ is a step whose derivative is an impulse⟧",
                   "⟦Đảo chiều hàm rồi dịch nó tới điểm $x=0$ trước khi cộng dồn giá trị||Reverses the function and shifts it to the point $x=0$ before accumulating values⟧",
                   "⟦Chuẩn hóa hàm sao cho diện tích toàn phần luôn bằng 1 dù hàm ban đầu ra sao||Normalises the function so its total area is always 1 whatever the original function is⟧"],
             explain="⟦Bracewell, tr. 62 đến 63: $H*f=\\int_{-\\infty}^xf(x')dx'$ khi các tích phân tồn tại.||Bracewell, pp. 62 to 63: $H*f=\\int_{-\\infty}^xf(x')dx'$ provided the integrals exist.⟧"),
        dict(q="⟦Vì sao Bracewell thấy tốt hơn là không nêu $H(0)$ trong ứng dụng vật lý?||Why does Bracewell find it more graceful not to mention $H(0)$ in physical applications?⟧",
             opts=["⟦Sự khác biệt là hàm rỗng, vô hình với phép đo có độ phân giải hữu hạn||The difference is a null function, invisible to measurements of finite resolving power⟧",
                   "⟦Vì $H(0)$ luôn bằng 0 với mọi hàm bậc thang đo được trong phòng thí nghiệm||Because $H(0)$ is always 0 for every step function measured in the laboratory⟧",
                   "⟦Vì giá trị $H(0)$ làm tích phân Fourier của bậc thang phân kỳ ở mọi tần số||Because the value $H(0)$ makes the Fourier integral of the step diverge at every frequency⟧",
                   "⟦Vì tính $H(0)$ đòi hỏi biết trước đạo hàm của $R$ tại gốc, thường không có||Because evaluating $H(0)$ requires knowing the derivative of $R$ at the origin, which is usually unavailable⟧"],
             explain="⟦Bracewell, tr. 64 đến 65: trung bình có trọng số trên khoảng khác không không bị ảnh hưởng bởi hàm rỗng.||Bracewell, pp. 64 to 65: weighted means over nonzero intervals are unaffected by null functions.⟧"),
        dict(q="⟦Hàm dấu và hàm bậc thang khác nhau ở chỗ nào về tính chẵn lẻ?||How do the sign function and the step function differ in parity?⟧",
             opts=["⟦$\\text{sgn}\\,x$ thuần lẻ, còn $H$ có cả phần chẵn lẫn lẻ||$\\text{sgn}\\,x$ is purely odd, whereas $H$ has both even and odd parts⟧",
                   "⟦$\\text{sgn}\\,x$ thuần chẵn vì chỉ nhận giá trị $\\pm1$, còn $H$ thuần lẻ||$\\text{sgn}\\,x$ is purely even since it takes only the values $\\pm1$, whereas $H$ is purely odd⟧",
                   "⟦Cả hai đều thuần lẻ, chỉ khác nhau hệ số 2 ở bước nhảy||Both are purely odd, differing only by the factor 2 in the jump⟧",
                   "⟦Cả hai đều vừa chẵn vừa lẻ tùy vào việc chọn gốc tọa độ||Both are even and odd at once depending on the choice of origin⟧"],
             explain="⟦Bracewell, tr. 65: $\\text{sgn}\\,x$ là hàm lẻ, còn $H$ có phần chẵn $\\tfrac12$ và phần lẻ $\\tfrac12\\text{sgn}\\,x$; notebook xác nhận {{h_parts_ok}}.||Bracewell, p. 65: $\\text{sgn}\\,x$ is odd, while $H$ has even part $\\tfrac12$ and odd part $\\tfrac12\\text{sgn}\\,x$; the notebook confirms {{h_parts_ok}}.⟧"),
        dict(q="⟦Tần số cắt của $\\text{sinc}\\,x$ (theo chu kỳ trên đơn vị $x$) là bao nhiêu?||What is the cutoff frequency of $\\text{sinc}\\,x$ (in cycles per unit of $x$)?⟧",
             opts=["0.5", "1 ⟦vì $\\text{sinc}$ triệt tiêu tại mọi số nguyên khác 0||since $\\text{sinc}$ vanishes at every nonzero integer⟧",
                   "$\\pi$ ⟦vì đối số của sinc là $\\pi x$||since the argument of sinc is $\\pi x$⟧",
                   "$1/2\\pi$ ⟦vì hằng số $2\\pi$ đứng trong số mũ của biến đổi||since the constant $2\\pi$ sits in the exponent of the transform⟧"],
             explain="⟦Bracewell, tr. 66: $\\text{sinc}\\,x$ và $\\Pi(s)$ là một cặp nên tần số cắt là 0.5 chu kỳ trên đơn vị của $x$.||Bracewell, p. 66: $\\text{sinc}\\,x$ and $\\Pi(s)$ are a pair so the cutoff is 0.5 cycles per unit of $x$.⟧"),
        dict(q="⟦Biến đổi Fourier của $\\text{sinc}^2x$ là gì?||What is the Fourier transform of $\\text{sinc}^2x$?⟧",
             opts=["$\\Lambda(s)$", "$\\Pi(s)$ ⟦vì bình phương không đổi dạng của phổ chữ nhật||since squaring does not change the shape of a rectangular spectrum⟧",
                   "$\\text{sinc}\\,s$ ⟦vì sinc tự biến đổi giống Gauss||since sinc is self-transforming like the Gaussian⟧",
                   "$H(s)$ ⟦vì tích chập hai xung chữ nhật cho bậc thang||since the convolution of two rectangles gives a step⟧"],
             explain="⟦Bracewell, tr. 67: biến đổi của $\\text{sinc}^2x$ là $\\Lambda(s)$, tần số cắt một chu kỳ trên đơn vị của $x$.||Bracewell, p. 67: the transform of $\\text{sinc}^2x$ is $\\Lambda(s)$, with cutoff one cycle per unit of $x$.⟧"),
        dict(q="⟦Vì sao Bracewell chọn $e^{-\\pi x^2}$ làm chuẩn cho hàm Gauss?||Why does Bracewell choose $e^{-\\pi x^2}$ as the standard Gaussian?⟧",
             opts=["⟦Tung độ trung tâm và diện tích đều bằng 1||Its central ordinate and area are both 1⟧",
                   "⟦Vì độ lệch chuẩn của nó đúng bằng 1 nên trùng phân phối chuẩn trong thống kê||Because its standard deviation is exactly 1, matching the normal distribution in statistics⟧",
                   "⟦Vì hằng số $\\pi$ làm mọi tích phân của nó là các số nguyên nên dễ tính tay||Because the constant $\\pi$ makes all its integrals integers, easy to compute by hand⟧",
                   "⟦Vì nó là hàm duy nhất có biến đổi Fourier bằng đúng chính nó||Because it is the only function whose Fourier transform equals itself exactly⟧"],
             explain="⟦Bracewell, tr. 58: cả tung độ trung tâm và diện tích bằng 1, và biến đổi Gauss cũng Gauss chuẩn hóa như vậy. (Không phải hàm tự biến đổi duy nhất: còn $\\text{sech}(\\pi x)$ và $\\text{III}$.)||Bracewell, p. 58: central ordinate and area both 1, and the Gaussian's transform is normalised the same way. (It is not the only self-transforming function: $\\text{sech}(\\pi x)$ and $\\text{III}$ also are.)⟧"),
        dict(q="⟦Vì sao phân phối Rayleigh có đỉnh không ở gốc dù Gauss hai chiều có đỉnh ở gốc?||Why does the Rayleigh distribution peak away from the origin although the 2D Gaussian peaks at the origin?⟧",
             opts=["⟦Vì diện tích vành $2\\pi r\\,dr$ tăng theo $r$||Because the ring area $2\\pi r\\,dr$ grows with $r$⟧",
                   "⟦Vì người say luôn bị đẩy ra xa gốc bởi một lực hướng tâm ngược chiều ở mỗi bước||Because the drunkard is always pushed away from the origin by an opposing radial force at every step⟧",
                   "⟦Vì Rayleigh là phân phối của bình phương khoảng cách nên đỉnh dịch theo bình phương||Because Rayleigh is the distribution of the squared distance so the peak shifts quadratically⟧",
                   "⟦Vì hai phân phối áp dụng cho hai biến khác nhau nên không thể so sánh trực tiếp||Because the two distributions apply to different variables so they cannot be compared directly at all⟧"],
             explain="⟦Bracewell, tr. 60: $R(r)dr$ bằng $2\\pi r\\,dr$ nhân tung độ; mô phỏng cho đỉnh tại {{ray_mode_mc}}.||Bracewell, p. 60: $R(r)dr$ is $2\\pi r\\,dr$ times the ordinate; the simulation puts the peak at {{ray_mode_mc}}.⟧"),
        dict(q="⟦Khe quét rộng bằng đúng một chu kỳ của một âm thuần làm gì?||What does a scanning slit exactly one period wide do to a pure tone?⟧",
             opts=["⟦Xóa hoàn toàn âm đó, vì $\\text{sinc}(1)=0$||Wipes it out entirely, since $\\text{sinc}(1)=0$⟧",
                   "⟦Giảm biên độ đi một nửa và giữ nguyên tần số cùng pha ban đầu của âm||Halves the amplitude and keeps the frequency and initial phase of the tone⟧",
                   "⟦Nhân đôi tần số của âm vì khe quét lấy mẫu mỗi nửa chu kỳ một lần||Doubles the frequency of the tone because the slit samples once every half period⟧",
                   "⟦Không ảnh hưởng gì vì khe chỉ làm nhòe biên chứ không đổi biên độ chính||Has no effect because the slit only blurs edges without changing the main amplitude⟧"],
             explain="⟦Độ lợi $\\text{sinc}(wf_0)$; với $w=1$ số đo là {{slit_1}}.||The gain is $\\text{sinc}(wf_0)$; for $w=1$ the measurement is {{slit_1}}.⟧"),
    ],
    nb=[
        ("md", """## 1. ⟦Xung chữ nhật, tam giác và hàm đa giác||The rectangle, the triangle and polygonal functions⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Hàm cổng có hoạt động như ta nói, tam giác có đúng là tự tích chập của xung chữ nhật, và hàm đa giác có viết được bằng tổng các tam giác dịch không? Ta so tích phân số với công thức và nội suy tuyến tính với tổng tam giác.||Does the gate behave as claimed, is the triangle really the self-convolution of the rectangle, and can a polygonal function be written as a sum of shifted triangles? We compare numerical integrals with formulas and linear interpolation with the sum of triangles.⟧"""),
        ("code", r'''from scipy import integrate, special, optimize
trap = getattr(np, "trapezoid", None) or np.trapz

# ⟦Năng lượng của đoạn Π(x)cos(πx)||Energy of the segment Π(x)cos(πx)⟧
ge = integrate.quad(lambda x: np.cos(np.pi*x)**2, -0.5, 0.5)[0]
assert abs(ge - 0.5) < 1e-12
report("gate_energy", ge, ".3f")

# ⟦Xung dịch h·Π((x−c)/b): diện tích h·b||Displaced rectangle h·Π((x−c)/b): area h·b⟧
h_, b_, c_ = 3.0, 2.0, 1.0
ra = integrate.quad(lambda x: h_*(1.0 if abs((x - c_)/b_) < 0.5 else 0.0), c_ - b_, c_ + b_, points=[c_ - b_/2, c_ + b_/2])[0]
assert abs(ra - h_*b_) < 1e-9
report("rect_area", ra, ".2f")

# ⟦Giá trị tại chỗ nhảy không đổi tích phân (lưới mịn, ba quy ước)||The value at the jump does not change the integral (fine grid, three conventions)⟧
dxr = 1e-4; xr = np.arange(-1, 1 + dxr/2, dxr); ar = []
for edge in (0.0, 0.5, 1.0):
    pv = np.where(np.abs(xr) < 0.5 - 1e-12, 1.0, np.where(np.abs(np.abs(xr) - 0.5) < 1e-12, edge, 0.0))
    ar.append(trap(pv, xr))
edge_diff = max(ar) - min(ar)
assert edge_diff < 2e-4
report("edge_diff", edge_diff, ".1e")

# ⟦Λ = Π * Π trên lưới mịn||Λ = Π * Π on a fine grid⟧
dxt = 0.001
cellp = np.ones(1000)
tri = np.convolve(cellp, cellp)*dxt
xt = (np.arange(len(tri)) - (len(tri) - 1)/2)*dxt
tri_dev = np.max(np.abs(tri - np.clip(1 - np.abs(xt), 0, None)))
assert tri_dev < 2e-3 and abs(trap(tri, xt) - 1) < 1e-3
report("tri_dev", tri_dev, ".1e"); report("tri_area", trap(tri, xt), ".2f")

# ⟦Hàm đa giác = tổng y_k Λ(x − k)||Polygonal function = sum of y_k Λ(x − k)⟧
knots, ys_ = np.arange(5), np.array([0, 2, 1, 3, 0.0])
Lam = lambda x: np.clip(1 - np.abs(x), 0, None)
xp = np.linspace(0, 4, 4001)
poly = sum(yk*Lam(xp - k) for k, yk in zip(knots, ys_))
poly_err = np.max(np.abs(poly - np.interp(xp, knots, ys_)))
assert poly_err < 1e-12
report("poly_err", poly_err, ".1e"); report("poly_25", np.interp(2.5, knots, ys_), ".2f")'''),
        ("code", r'''plt.figure(figsize=(7, 3.3))
plt.plot(xp, poly, "k", label=("⟦tổng y_k Λ(x−k)||sum of y_k Λ(x−k)⟧"))
for k, yk in zip(knots, ys_):
    plt.plot(xp, yk*Lam(xp - k), lw=0.7, alpha=0.6)
plt.plot(knots, ys_, "ro"); plt.xlabel("x"); plt.legend(); plt.tight_layout(); plt.show()''', dict(fig="poly", cap="⟦Hình 1. Hàm đa giác qua năm điểm (đen) là tổng của các tam giác Λ dịch và nhân với tung độ tại điểm nút (đường mảnh).||Figure 1. The polygonal function through five points (black) is the sum of shifted triangles Λ scaled by the ordinate at each knot (thin lines).⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Năng lượng của đoạn $\\Pi\\cos\\pi x$ là {{gate_energy}}; xung cao 3 đáy 2 có diện tích {{rect_area}}. Ba quy ước cho giá trị tại chỗ nhảy chỉ lệch {{edge_diff}} về diện tích. Tích chập số $\\Pi*\\Pi$ lệch tam giác tối đa {{tri_dev}} và diện tích {{tri_area}}. Hàm đa giác bằng tổng tam giác (lệch {{poly_err}} so với nội suy) và bằng {{poly_25}} tại 2.5.||The energy of the segment $\\Pi\\cos\\pi x$ is {{gate_energy}}; the rectangle of height 3 and base 2 has area {{rect_area}}. The three conventions for the value at the jump differ by only {{edge_diff}} in area. The numerical convolution $\\Pi*\\Pi$ deviates from the triangle by at most {{tri_dev}} with area {{tri_area}}. The polygonal function equals the sum of triangles (deviation {{poly_err}} from interpolation) and is {{poly_25}} at 2.5.⟧"""),
        ("md", """## 2. ⟦Gauss, erf, các thông số phân tán và Rayleigh||The Gaussian, erf, dispersion parameters and Rayleigh⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Các thông số phân tán của $e^{-\\pi x^2}$ (sai số xác suất, sai số tuyệt đối, độ rộng nửa đỉnh, độ rộng tương đương) và phần trăm bao phủ có đúng bảng của sách không, và người say đi lang thang cách gốc bao xa? Mỗi số tính bằng hai cách; Rayleigh kiểm bằng mô phỏng Monte Carlo.||Are the dispersion parameters of $e^{-\\pi x^2}$ (probable error, mean absolute error, half-peak width, equivalent width) and the coverage percentages as in the book's table, and how far does the drunkard wander from the origin? Each number is computed two ways; Rayleigh is checked by Monte Carlo simulation.⟧"""),
        ("code", r'''g = lambda x: np.exp(-np.pi*x**2)
area = integrate.quad(g, -np.inf, np.inf)[0]
var = integrate.quad(lambda x: x**2*g(x), -np.inf, np.inf)[0]
sd = np.sqrt(var)
assert abs(area - 1) < 1e-9 and abs(var - 1/(2*np.pi)) < 1e-9
report("g_area", area, ".2f"); report("g_var", var, ".4f"); report("g_sd", sd, ".4f")

gint1 = integrate.quad(g, 0, 1)[0]
assert abs(gint1 - 0.5*special.erf(np.sqrt(np.pi))) < 1e-12
report("g_int1", gint1, ".4f")

# ⟦Sai số xác suất: ∫_{−p}^{p} g = 1/2. Cách A: tìm nghiệm số; cách B: 0.6745σ||Probable error: ∫_{−p}^{p} g = 1/2. Method A: numerical root; method B: 0.6745σ⟧
pe = optimize.brentq(lambda p: integrate.quad(g, -p, p)[0] - 0.5, 0.05, 1)
assert abs(pe - 0.674489750*sd) < 1e-8
mad = 2*integrate.quad(lambda x: x*g(x), 0, np.inf)[0]
assert abs(mad - 1/np.pi) < 1e-9
fwhm = 2*optimize.brentq(lambda x: g(x) - 0.5, 0, 2)
assert abs(fwhm - 2*np.sqrt(np.log(2)/np.pi)) < 1e-9
eqw = area/g(0)
report("pe", pe, ".4f"); report("mad", mad, ".4f"); report("fwhm", fwhm, ".4f"); report("eqw", eqw, ".2f")

def cover(w): return integrate.quad(g, -w, w)[0]*100         # ⟦phần trăm nằm trong ±w||percentage within ±w⟧
for key, w, ex in (("cov_sd", sd, special.erf(1/np.sqrt(2))), ("cov_mad", mad, special.erf(mad/sd/np.sqrt(2))),
                   ("cov_half", fwhm/2, special.erf(fwhm/2/sd/np.sqrt(2))), ("cov_eq", 0.5, special.erf(0.5/sd/np.sqrt(2)))):
    assert abs(cover(w) - 100*ex) < 1e-8
    report(key, cover(w), ".2f")

# ⟦Rayleigh: mô phỏng 400 000 điểm Gauss hai chiều σ = 1||Rayleigh: simulate 400 000 two-dimensional Gaussian points with σ = 1⟧
rg = np.random.default_rng(2026)
pts = rg.standard_normal((400000, 2)); rr = np.hypot(pts[:, 0], pts[:, 1])
hist, edges = np.histogram(rr, bins=np.arange(0, 5, 0.05), density=True)
mode = 0.5*(edges[np.argmax(hist)] + edges[np.argmax(hist) + 1])
assert abs(rr.mean() - np.sqrt(np.pi/2)) < 0.01 and abs(mode - 1.0) < 0.1 and abs((rr < 1).mean() - (1 - np.exp(-0.5))) < 0.005
report("ray_mean_mc", rr.mean(), ".3f"); report("ray_mean_th", np.sqrt(np.pi/2), ".4f")
report("ray_mode_mc", mode, ".2f"); report("ray_p1_mc", (rr < 1).mean(), ".3f"); report("ray_p1_th", 1 - np.exp(-0.5), ".4f")

# ⟦Dãy Gauss: ∫ cos x · (1/τ) exp(−π x²/τ²) dx = exp(−τ²/4π)||Gaussian sequence: ∫ cos x · (1/τ) exp(−π x²/τ²) dx = exp(−τ²/4π)⟧
for tau, tag in ((1.0, "gs_1"), (0.5, "gs_05"), (0.1, "gs_01")):
    v_ = integrate.quad(lambda x: np.cos(x)*np.exp(-np.pi*x**2/tau**2)/tau, -12*tau, 12*tau, limit=400)[0]
    assert abs(v_ - np.exp(-tau**2/(4*np.pi))) < 1e-9
    report(tag, v_, ".4f")'''),
        ("code", r'''xs = np.linspace(0, 4, 400)
plt.figure(figsize=(7, 3.3))
plt.hist(rr, bins=np.arange(0, 5, 0.1), density=True, alpha=0.5, label=("⟦mô phỏng||simulation⟧"))
plt.plot(xs, xs*np.exp(-xs**2/2), "r", label=("⟦Rayleigh r·e^{−r²/2}||Rayleigh r·e^{−r²/2}⟧"))
plt.plot(xs, np.exp(-xs**2/2)/np.sqrt(2*np.pi), "k--", label=("⟦Gauss một chiều||1D Gaussian⟧"))
plt.xlabel("r"); plt.legend(); plt.tight_layout(); plt.show()''', dict(fig="rayleigh", cap="⟦Hình 2. Khoảng cách tới gốc của 400 000 điểm Gauss hai chiều: histogram khớp phân phối Rayleigh (đỏ), có đỉnh tại r = σ chứ không ở gốc, khác Gauss một chiều (nét đứt).||Figure 2. Distance from the origin of 400 000 two-dimensional Gaussian points: the histogram matches the Rayleigh distribution (red), peaking at r = σ rather than at the origin, unlike the one-dimensional Gaussian (dashed).⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦$e^{-\\pi x^2}$ có diện tích {{g_area}} và $\\sigma$ = {{g_sd}}. Sai số xác suất {{pe}}, sai số tuyệt đối {{mad}}, độ rộng nửa đỉnh {{fwhm}} và độ rộng tương đương {{eqw}}, đều khớp bảng của sách. Phần trăm bao phủ: {{cov_sd}}, {{cov_mad}}, {{cov_half}}, {{cov_eq}}. Mô phỏng Rayleigh cho trung bình {{ray_mean_mc}} (lý thuyết {{ray_mean_th}}), đỉnh {{ray_mode_mc}}, và {{ray_p1_mc}} trong $r<\\sigma$ (lý thuyết {{ray_p1_th}}). Dãy Gauss cho {{gs_1}}, {{gs_05}}, {{gs_01}} tiến về 1.||$e^{-\\pi x^2}$ has area {{g_area}} and $\\sigma$ = {{g_sd}}. The probable error {{pe}}, mean absolute error {{mad}}, half-peak width {{fwhm}} and equivalent width {{eqw}} all match the book's table. Coverage percentages: {{cov_sd}}, {{cov_mad}}, {{cov_half}}, {{cov_eq}}. The Rayleigh simulation gives mean {{ray_mean_mc}} (theory {{ray_mean_th}}), peak {{ray_mode_mc}}, and {{ray_p1_mc}} within $r<\\sigma$ (theory {{ray_p1_th}}). The Gaussian sequence gives {{gs_1}}, {{gs_05}}, {{gs_01}} tending to 1.⟧"""),
        ("md", """## 3. ⟦Bậc thang, dốc, tích chập với $H$ và hàm dấu||The step, the ramp, convolution with $H$ and the sign function⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦$\\Pi$ có đúng bằng hiệu hai bậc thang, $H*H$ có là hàm dốc, tích chập với $H$ có là tích phân, giá trị $H(0)$ có quan trọng, và $H$ tách chẵn lẻ ra sao? Mỗi điều kiểm bằng hai cách.||Is $\\Pi$ really the difference of two steps, is $H*H$ the ramp, is convolution with $H$ integration, does $H(0)$ matter, and how does $H$ split into even and odd parts? Each is checked two ways.⟧"""),
        ("code", r'''Hs = lambda x, h0=0.5: np.where(x > 1e-12, 1.0, np.where(np.abs(x) <= 1e-12, h0, 0.0))
xg = np.linspace(-2, 2, 4001)
Pi_g = np.where(np.abs(xg) < 0.5 - 1e-12, 1.0, np.where(np.abs(np.abs(xg) - 0.5) < 1e-12, 0.5, 0.0))
assert np.allclose(Pi_g, Hs(xg + 0.5) - Hs(xg - 0.5))
report("pi_step_ok", "yes", "s")

# ⟦Hàm dốc: H*H trên lưới||The ramp: H*H on a grid⟧
dxs = 0.002; xs_ = np.arange(0, 10, dxs)
HH = np.convolve(np.ones_like(xs_), np.ones_like(xs_))[:len(xs_)]*dxs
assert abs(HH[int(2/dxs)] - 2.0) < 5e-3
report("ramp_2", HH[int(2/dxs)], ".2f")

# ⟦Tích chập với H là tích phân: H*f với f = exp(−πx²)||Convolution with H is integration: H*f with f = exp(−πx²)⟧
xf = np.arange(-6, 6, 0.002)
Hf = np.convolve(np.where(xf >= 0, 1.0, 0.0), np.exp(-np.pi*xf**2))*0.002
xh = np.arange(len(Hf))*0.002 + 2*xf[0]
sel = (xh > -3) & (xh < 3)
exact = 0.5*(1 + special.erf(np.sqrt(np.pi)*xh))
hf_dev = np.max(np.abs(Hf[sel] - exact[sel]))
assert hf_dev < 4e-3
report("hf_05", np.interp(0.5, xh, Hf), ".4f"); report("hf_dev", hf_dev, ".4f")

# ⟦R'(0) đối xứng||The symmetric derivative of R at 0⟧
R = lambda x: x*Hs(np.asarray(x, float))
Dl = 1e-6
rp = (R(Dl) - R(-Dl))/(2*Dl)
assert abs(rp - 0.5) < 1e-9
report("r_prime0", float(rp), ".2f")

# ⟦Ĥ(x) = (1 − e^{−x/τ})H(x): tích phân của H − Ĥ bằng τ||Ĥ(x) = (1 − e^{−x/τ})H(x): the integral of H − Ĥ equals τ⟧
tau = 0.01
hh = integrate.quad(lambda x: np.exp(-x/tau), 0, np.inf)[0]
assert abs(hh - tau) < 1e-12
report("hhat_int", hh, ".2f")

# ⟦Xấp xỉ arctan: công thức so với tích phân Lorentz||Arctan approximation: formula versus the Lorentzian integral⟧
def atan_H(x, t): return 0.5 + np.arctan(x/t)/np.pi
def lor_H(x, t): return 0.5 + integrate.quad(lambda u: (t/np.pi)/(u**2 + t**2), 0, x)[0]
for t in (0.1, 0.01):
    assert abs(atan_H(0.1, t) - lor_H(0.1, t)) < 1e-9
report("arctan_1", atan_H(0.1, 0.1), ".4f"); report("arctan_2", atan_H(0.1, 0.01), ".4f")

# ⟦Hàm dấu và tách chẵn lẻ của H||The sign function and the even-odd split of H⟧
sg = np.sign(xg)
assert np.allclose(sg, 2*Hs(xg) - 1)
ev, od = 0.5*(Hs(xg) + Hs(-xg)), 0.5*(Hs(xg) - Hs(-xg))
assert np.allclose(ev, 0.5) and np.allclose(od, 0.5*sg)
report("h_parts_ok", "yes", "s")

# ⟦Hàm bậc thang có dốc: R(x) − R(x−1) = xΠ(x−1/2) + H(x−1)||The ramp-step: R(x) − R(x−1) = xΠ(x−1/2) + H(x−1)⟧
xq = np.linspace(-1, 3, 4001)
Piq = lambda x: np.where(np.abs(x) < 0.5 - 1e-12, 1.0, np.where(np.abs(np.abs(x) - 0.5) < 1e-12, 0.5, 0.0))
w1 = R(xq) - R(xq - 1); w2 = xq*Piq(xq - 0.5) + Hs(xq - 1)
w3 = np.where(xq < 0, 0, np.where(xq <= 1, xq, 1.0))
assert np.allclose(w1, w3) and np.allclose(w2[np.abs(xq - 1) > 1e-9], w3[np.abs(xq - 1) > 1e-9])
report("ramp_ok", "yes", "s"); report("ramp_04", float(R(0.4) - R(-0.6)), ".2f")'''),
        ("code", r'''xa = np.linspace(-0.5, 0.5, 1001)
plt.figure(figsize=(7, 3.3))
plt.plot(xa, Hs(xa), "k", label="H(x)")
for t, c in ((0.1, "tab:orange"), (0.03, "tab:blue"), (0.01, "tab:red")):
    plt.plot(xa, atan_H(xa, t), color=c, lw=1, label=f"τ = {t}")
plt.xlabel("x"); plt.legend(); plt.tight_layout(); plt.show()''', dict(fig="step_approx", cap="⟦Hình 3. Xấp xỉ liên tục ½ + arctan(x/τ)/π của bậc thang H(x): khi τ giảm, đường cong dựng đứng lên tại gốc và tiến về H.||Figure 3. The continuous approximation ½ + arctan(x/τ)/π of the step H(x): as τ decreases the curve steepens at the origin and approaches H.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦$\\Pi=H(x+\\tfrac12)-H(x-\\tfrac12)$ đúng trên lưới ({{pi_step_ok}}). $H*H$ tại 2 cho {{ramp_2}}, đúng $R(2)$. Tích chập $H*e^{-\\pi x^2}$ tại 0.5 là {{hf_05}} (lệch {{hf_dev}} so với $\\tfrac12[1+\\text{erf}]$). Đạo hàm đối xứng của $R$ tại 0 là {{r_prime0}}. Tích phân của $H-\\hat H$ là {{hhat_int}} khi $\\tau=0.01$, tiến về 0. Xấp xỉ arctan tại 0.1: {{arctan_1}} ($\\tau=0.1$), {{arctan_2}} ($\\tau=0.01$). $\\text{sgn}=2H-1$ và tách chẵn lẻ của $H$ đúng ({{h_parts_ok}}); hàm dốc-bậc thang viết ba cách trùng khớp ({{ramp_ok}}), bằng {{ramp_04}} tại 0.4.||$\\Pi=H(x+\\tfrac12)-H(x-\\tfrac12)$ holds on the grid ({{pi_step_ok}}). $H*H$ at 2 gives {{ramp_2}}, exactly $R(2)$. The convolution $H*e^{-\\pi x^2}$ at 0.5 is {{hf_05}} (deviation {{hf_dev}} from $\\tfrac12[1+\\text{erf}]$). The symmetric derivative of $R$ at 0 is {{r_prime0}}. The integral of $H-\\hat H$ is {{hhat_int}} for $\\tau=0.01$, tending to 0. The arctan approximation at 0.1: {{arctan_1}} ($\\tau=0.1$), {{arctan_2}} ($\\tau=0.01$). $\\text{sgn}=2H-1$ and the even-odd split of $H$ hold ({{h_parts_ok}}); the ramp-step written three ways coincides ({{ramp_ok}}) and equals {{ramp_04}} at 0.4.⟧"""),
        ("md", """## 4. ⟦Sinc, sinc bình phương và jinc||Sinc, sinc squared and jinc⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Sinc có các tính chất nêu (điểm không, diện tích, tần số cắt), có lọc thông thấp thật không khi cắt cụt, tích phân của nó tràn quá bao nhiêu, và jinc có điểm không đầu ở đâu? Ta so tích phân số với công thức Si, và tích chập không gian với bộ lọc vuông góc qua FFT.||Does sinc have the stated properties (zeros, area, cutoff), does it truly low-pass filter when truncated, by how much does its integral overshoot, and where is the first zero of jinc? We compare numerical integrals with the Si formula, and spatial convolution with a brick-wall filter through the FFT.⟧"""),
        ("code", r'''report("sinc_zero", abs(np.sinc(3)), ".2f")
sinc_int = integrate.quad(np.sinc, 0, 100, limit=2000)[0]
assert abs(sinc_int - special.sici(np.pi*100)[0]/np.pi) < 1e-6
report("sinc_int100", sinc_int, ".4f")

# ⟦Cặp biến đổi: ∫_{−1/2}^{1/2} e^{i2πsx} ds = sinc x||Transform pair: ∫_{−1/2}^{1/2} e^{i2πsx} ds = sinc x⟧
sx = integrate.quad(lambda s: np.cos(2*np.pi*s*0.3), -0.5, 0.5)[0]
assert abs(sx - np.sinc(0.3)) < 1e-12
report("sinc_03", sx, ".4f")

# ⟦Lọc thông thấp: hai âm 0.2 và 0.8; sinc cắt cụt (cách A) so với bộ lọc vuông góc qua FFT (cách B)||Low-pass: two tones 0.2 and 0.8; truncated sinc (method A) versus a brick-wall FFT filter (method B)⟧
dt = 0.05; T = np.arange(0, 400, dt)
sig = np.cos(2*np.pi*0.2*T) + np.cos(2*np.pi*0.8*T)
kt = np.arange(-100, 100 + dt/2, dt); kern = np.sinc(kt)*dt
ya = np.convolve(sig, kern, "same")
Sg = np.fft.rfft(sig); fq = np.fft.rfftfreq(len(T), dt); Sg[fq > 0.5] = 0
yb = np.fft.irfft(Sg, len(T))
mid = (T > 120) & (T < 280)
def gain(y, f0):
    A = np.column_stack([np.cos(2*np.pi*f0*T[mid]), np.sin(2*np.pi*f0*T[mid])])
    co = np.linalg.lstsq(A, y[mid], rcond=None)[0]; return np.hypot(*co)
ga02, ga08, gb02, gb08 = gain(ya, 0.2), gain(ya, 0.8), gain(yb, 0.2), gain(yb, 0.8)
assert abs(ga02 - 1) < 0.02 and ga08 < 0.03 and abs(gb02 - 1) < 1e-6 and gb08 < 2e-3
report("lp_gain_02", ga02, ".3f"); report("lp_gain_08", ga08, ".3f")
report("lp_gain_02f", gb02, ".3f"); report("lp_gain_08f", gb08, ".3f")

# ⟦H * sinc = ½ + Si(πx)/π và độ tràn quá||H * sinc = ½ + Si(πx)/π and its overshoot⟧
xx = np.linspace(-6, 6, 120001)
cum = 0.5 + np.concatenate([[0], np.cumsum((np.sinc(xx[1:]) + np.sinc(xx[:-1]))/2*np.diff(xx))])
cum -= cum[np.argmin(np.abs(xx))] - 0.5                                        # ⟦đặt giá trị tại 0 bằng ½||set the value at 0 to ½⟧
si_form = 0.5 + special.sici(np.pi*xx)[0]/np.pi
assert np.max(np.abs(cum - si_form)) < 1e-5
gmax = 0.5 + special.sici(np.pi)[0]/np.pi
assert abs(cum.max() - gmax) < 1e-5
d_num = (special.sici(np.pi*0.7001)[0] - special.sici(np.pi*0.6999)[0])/np.pi/0.0002
assert abs(d_num - np.sinc(0.7)) < 1e-6
report("gibbs_max", gmax, ".4f")

# ⟦sinc²: biến đổi Λ và diện tích||sinc²: its transform Λ and its area⟧
s2 = integrate.quad(lambda s: max(1 - abs(s), 0)*np.cos(2*np.pi*s*0.5), -1, 1, points=[0])[0]
assert abs(s2 - np.sinc(0.5)**2) < 1e-10
a2 = integrate.quad(lambda x: np.sinc(x)**2, -2000, 2000, limit=8000)[0]
assert abs(a2 - 1) < 1e-3
report("sinc2_05", s2, ".4f"); report("sinc2_area", a2, ".2f")

# ⟦jinc: J1(πr)/(2r)||jinc: J1(πr)/(2r)⟧
jinc = lambda r: special.j1(np.pi*r)/(2*r)
assert abs(jinc(1e-8) - np.pi/4) < 1e-9
z1 = special.jn_zeros(1, 1)[0]/np.pi
assert abs(jinc(z1)) < 1e-12
report("jinc_center", jinc(1e-8), ".4f"); report("jinc_zero", z1, ".4f")'''),
        ("code", r'''plt.figure(figsize=(8, 3.3))
plt.plot(T[mid][:400], sig[mid][:400], color="lightgray", label=("⟦tín hiệu hai âm||two-tone signal⟧"))
plt.plot(T[mid][:400], ya[mid][:400], "tab:red", label=("⟦sau lọc bằng sinc cắt cụt||after truncated-sinc filter⟧"))
plt.plot(T[mid][:400], np.cos(2*np.pi*0.2*T[mid][:400]), "k--", lw=0.8, label=("⟦âm 0.2 thuần||pure 0.2 tone⟧"))
plt.xlabel("t"); plt.legend(loc="upper right", fontsize=8); plt.tight_layout(); plt.show()''', dict(fig="sinc_lp", cap="⟦Hình 4. Tích chập với sinc cắt cụt giữ âm 0.2 (đỏ trùng nét đứt) và loại âm 0.8 (thành phần nhanh biến mất khỏi tín hiệu xám).||Figure 4. Convolution with a truncated sinc keeps the 0.2 tone (red on top of the dashed line) and removes the 0.8 tone (the fast component vanishes from the gray signal).⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦$\\text{sinc}(3)$ = {{sinc_zero}}, $\\int_0^{100}\\text{sinc}$ = {{sinc_int100}} (tiến về ½), và $\\int_{-1/2}^{1/2}e^{i2\\pi s(0.3)}ds$ = {{sinc_03}}. Lọc bằng sinc cắt cụt giữ {{lp_gain_02}} tại 0.2 và còn {{lp_gain_08}} tại 0.8; bộ lọc vuông góc qua FFT cho {{lp_gain_02f}} và {{lp_gain_08f}}. $H*\\text{sinc}$ đạt cực đại {{gibbs_max}}. $\\text{sinc}^2(0.5)$ = {{sinc2_05}}, diện tích {{sinc2_area}}. Jinc có giá trị trung tâm {{jinc_center}} và điểm không đầu tại {{jinc_zero}}.||$\\text{sinc}(3)$ = {{sinc_zero}}, $\\int_0^{100}\\text{sinc}$ = {{sinc_int100}} (tending to ½), and $\\int_{-1/2}^{1/2}e^{i2\\pi s(0.3)}ds$ = {{sinc_03}}. The truncated-sinc filter keeps {{lp_gain_02}} at 0.2 and leaves {{lp_gain_08}} at 0.8; the brick-wall filter through the FFT gives {{lp_gain_02f}} and {{lp_gain_08f}}. $H*\\text{sinc}$ reaches a maximum {{gibbs_max}}. $\\text{sinc}^2(0.5)$ = {{sinc2_05}}, area {{sinc2_area}}. Jinc has central value {{jinc_center}} and first zero at {{jinc_zero}}.⟧"""),
        ("md", """## 5. ⟦Cặp biến đổi, cửa sổ, khe quét và trung bình trượt||Transform pairs, windows, the scanning slit and running means⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Các cặp biến đổi của các hàm vừa học có đúng, ba cửa sổ khác nhau cho thùy phụ ra sao, khe quét làm suy giảm âm thế nào, và nhân Dirichlet khác sinc bao nhiêu? Ta so tích phân số với công thức, tìm cực đại bằng quét lưới và bằng nghiệm $\\tan\\pi s=\\pi s$, và tích chập số với công thức sinc.||Are the transform pairs of the functions just learned correct, what sidelobes do three windows give, how does a scanning slit attenuate a tone, and how far is the Dirichlet kernel from sinc? We compare numerical integrals with formulas, find maxima by grid scan and by the root of $\\tan\\pi s=\\pi s$, and numerical convolution with the sinc formula.⟧"""),
        ("code", r'''def ft_support(f, a, b, s, pts=None):
    re = integrate.quad(lambda x: f(x)*np.cos(2*np.pi*x*s), a, b, points=pts, limit=400)[0]
    im = integrate.quad(lambda x: -f(x)*np.sin(2*np.pi*x*s), a, b, points=pts, limit=400)[0]
    return re + 1j*im
s3 = 0.3
pairs = [("p_pi_03", ft_support(lambda x: 1.0, -0.5, 0.5, s3), np.sinc(s3)),
         ("p_tri_03", ft_support(lambda x: 1 - abs(x), -1, 1, s3, [0]), np.sinc(s3)**2),
         ("p_g_03", ft_support(g, -10, 10, s3), np.exp(-np.pi*s3**2)),
         ("p_exp_03", ft_support(lambda x: np.exp(-abs(x)), -40, 40, s3, [0]), 2/(1 + 4*np.pi**2*s3**2))]
for key, num_, ex_ in pairs:
    assert abs(num_ - ex_) < 1e-8
    report(key, num_.real, ".4f")
cz = ft_support(lambda x: np.exp(-x), 0, 40, s3)
assert abs(cz - 1/(1 + 2j*np.pi*s3)) < 1e-8
report("p_caus_03", abs(cz), ".4f"); report("pairs_ok", 5, "d")

# ⟦Thùy phụ đầu: cách A quét lưới; cách B nghiệm của tan(πs) = πs||First sidelobe: method A grid scan; method B root of tan(πs) = πs⟧
ss = np.arange(1, 3, 1e-5)
peak_scan = np.max(np.abs(np.sinc(ss)))
s_root = optimize.brentq(lambda s: np.tan(np.pi*s) - np.pi*s, 1.3, 1.5)
peak_root = abs(np.sinc(s_root))
assert abs(peak_scan - peak_root) < 1e-8
report("sl_rect", peak_root, ".4f"); report("sl_rect_db", 20*np.log10(peak_root), ".2f")
report("sl_tri", peak_root**2, ".4f"); report("sl_tri_db", 20*np.log10(peak_root**2), ".2f")

# ⟦Khe quét: tích chập số so với sinc(w f0)||Scanning slit: numerical convolution versus sinc(w f0)⟧
dxk = 0.001; xt = np.arange(0, 20, dxk); track = np.cos(2*np.pi*1.0*xt)
for w, key in ((0.25, "slit_025"), (0.5, "slit_05"), (1.0, "slit_1")):
    ker = np.ones(int(round(w/dxk)))/int(round(w/dxk))
    out = np.convolve(track, ker, "valid")
    xo = xt[:len(out)]
    A = np.column_stack([np.cos(2*np.pi*xo), np.sin(2*np.pi*xo)])
    co = np.linalg.lstsq(A, out, rcond=None)[0]
    amp = np.hypot(*co)
    assert abs(amp - abs(np.sinc(w*1.0))) < 5e-3
    report(key, abs(np.sinc(w)), ".4f")

# ⟦Trung bình trượt 8 điểm: freqz so với công thức, và xấp xỉ sinc||8-point running mean: freqz versus formula, and the sinc approximation⟧
from scipy import signal
fE = 0.05
_, Hm = signal.freqz(np.ones(8)/8, worN=[2*np.pi*fE])
exact_ma = abs(np.sin(np.pi*8*fE)/(8*np.sin(np.pi*fE)))
assert abs(abs(Hm[0]) - exact_ma) < 1e-12
report("ma_exact", exact_ma, ".4f"); report("ma_sinc", abs(np.sinc(8*fE)), ".4f")'''),
        ("code", r'''sf = np.linspace(0, 4, 2000)
plt.figure(figsize=(7.5, 3.3))
plt.plot(sf, 20*np.log10(np.abs(np.sinc(sf)) + 1e-12), label=("⟦chữ nhật (sinc)||rectangle (sinc)⟧"))
plt.plot(sf, 20*np.log10(np.sinc(sf)**2 + 1e-12), label=("⟦tam giác (sinc²)||triangle (sinc²)⟧"))
plt.plot(sf, 20*np.log10(np.exp(-np.pi*(sf/1.0)**2) + 1e-12), label=("⟦Gauss||Gaussian⟧"))
plt.ylim(-80, 3); plt.xlabel("s"); plt.ylabel("dB"); plt.legend(); plt.tight_layout(); plt.show()''', dict(fig="windows", cap="⟦Hình 5. Biến đổi của ba cửa sổ theo dB: chữ nhật (sinc) có thùy phụ đầu cao nhất, tam giác (sinc²) thấp hơn gấp đôi số dB, Gauss suy giảm đều không có thùy phụ.||Figure 5. The transforms of three windows in dB: the rectangle (sinc) has the highest first sidelobe, the triangle (sinc²) has twice as many dB below, the Gaussian decays smoothly with no sidelobes.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Tại $s=0.3$: $\\Pi$ cho {{p_pi_03}}, $\\Lambda$ cho {{p_tri_03}}, Gauss {{p_g_03}}, $e^{-|x|}$ cho {{p_exp_03}}, $|F|$ của $e^{-x}H$ là {{p_caus_03}}: {{pairs_ok}} trên 5 cặp đúng. Thùy phụ đầu: sinc {{sl_rect}} ({{sl_rect_db}} dB) bằng cả quét lưới lẫn nghiệm $\\tan\\pi s=\\pi s$; sinc$^2$ {{sl_tri}} ({{sl_tri_db}} dB). Khe quét giữ {{slit_025}}, {{slit_05}}, {{slit_1}} biên độ khi rộng 0.25, 0.5, 1 chu kỳ. Trung bình 8 điểm tại 0.05: chính xác {{ma_exact}}, sinc {{ma_sinc}}.||At $s=0.3$: $\\Pi$ gives {{p_pi_03}}, $\\Lambda$ gives {{p_tri_03}}, the Gaussian {{p_g_03}}, $e^{-|x|}$ gives {{p_exp_03}}, and $|F|$ of $e^{-x}H$ is {{p_caus_03}}: {{pairs_ok}} of 5 pairs hold. First sidelobes: sinc {{sl_rect}} ({{sl_rect_db}} dB) by both the grid scan and the root of $\\tan\\pi s=\\pi s$; sinc$^2$ {{sl_tri}} ({{sl_tri_db}} dB). The slit keeps {{slit_025}}, {{slit_05}}, {{slit_1}} of the amplitude for widths 0.25, 0.5, 1 period. The 8-point mean at 0.05: exact {{ma_exact}}, sinc {{ma_sinc}}.⟧"""),
    ],
)
