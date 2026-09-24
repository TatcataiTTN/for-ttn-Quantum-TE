from lib import F, C, UL, OL, TBL

MOD = dict(
    n=6, slug="theorems", part="A", book="B",
    title="⟦Các định lý cơ bản của biến đổi Fourier||The basic theorems of the Fourier transform⟧",
    blurb="⟦Tỉ lệ, cộng, dịch, điều chế, tích chập, Rayleigh, công suất, tự tương quan, đạo hàm: mười định lý cho phép suy ra hầu hết biến đổi mà không phải tích phân.||"
          "Similarity, addition, shift, modulation, convolution, Rayleigh, power, autocorrelation and derivative: ten theorems that yield most transforms without integrating.⟧",
    src="⟦Bracewell, chương 6, tr. 105–135||Bracewell, chapter 6, pp. 105–135⟧",
    data="⟦Sinh bằng mã: Gauss, sinc, xung chữ nhật, sóng mang điều biên, mạch RC, dãy phức có đối xứng||Generated in code: Gaussians, sinc, rectangles, an amplitude-modulated carrier, an RC circuit, symmetric complex sequences⟧",
    objectives=[
        "⟦Nêu và dùng mười định lý ở bảng 6.1, kể cả điều kiện và dạng đối xứng của chúng.||State and use the ten theorems of Table 6.1, including their conditions and symmetric forms.⟧",
        "⟦Suy ra biến đổi mới từ sáu cặp chuẩn bằng định lý thay vì tích phân.||Derive new transforms from six standard pairs by theorem instead of integration.⟧",
        "⟦Diễn giải vật lý: dịch là pha tuyến tính, điều chế là hai bản sao nửa cường độ, tích chập là nhân phổ.||Interpret physically: shift is a linear phase, modulation gives two half-strength replicas, convolution multiplies spectra.⟧",
        "⟦Dùng Rayleigh, công suất và tự tương quan để nối năng lượng theo $x$ với năng lượng theo $s$.||Use Rayleigh, power and autocorrelation to connect energy in $x$ with energy in $s$.⟧",
        "⟦Dùng định lý đạo hàm, và biết định lý áp dụng cho hàm suy rộng ra sao.||Use the derivative theorem and know how the theorems extend to generalized functions.⟧",
    ],
    parts=[
        # ---------------------------------------------------------------- PART 1
        dict(
            title="⟦Sáu cặp chuẩn và tính tương hỗ||Six standard pairs and reciprocity⟧",
            scr=("⟦Muốn hiểu định lý, cần vài cặp biến đổi cụ thể để thấy định lý làm gì.||To understand the theorems we need a few concrete transform pairs to see what each does.⟧",
                 "⟦Các cặp này ở dạng \"quá dễ\" nên dễ bỏ qua chuyện hai chiều biến đổi thuận và ngược nói hai điều khác nhau.||These pairs look \"too easy\" so it is tempting to skip that the direct and inverse directions say different things.⟧",
                 "⟦Giữ sáu cặp làm kho tham chiếu, cộng ba cặp trong giới hạn từ Gauss.||Keep six pairs as a stock, plus three pairs in the limit obtained from the Gaussian.⟧"),
            preview=["⟦Sáu cặp tham chiếu||Six reference pairs⟧", "⟦Tương hỗ: hai câu nói khác nhau||Reciprocity: two different statements⟧", "⟦Các cặp trong giới hạn: $1$, $e^{i\\pi x}$, $\\cos\\pi x$||Pairs in the limit: $1$, $e^{i\\pi x}$, $\\cos\\pi x$⟧"],
            slides=[
                ("⟦Vì sao có \"bộ định lý\"||Why there is a \"set of theorems\"⟧",
                 "<p>⟦Một số ít định lý đóng vai trò nền tảng khi tư duy với biến đổi Fourier. Phần lớn quen thuộc dưới dạng này hay khác; ở đây ta gom chúng như các tính chất toán học đơn giản. Phần lớn cách suy ra rất đơn giản, và khả năng áp dụng cho hàm xung kiểm được bằng dãy xung chữ nhật; chứng minh chặt chẽ bằng đại số hàm suy rộng ở cuối chương (Bracewell, tr. 105).||"
                 "A small number of theorems play a basic role in thinking with Fourier transforms. Most are familiar in one form or another; here we collect them as simple mathematical properties. Most derivations are simple, and applicability to impulsive functions is verified with sequences of rectangular pulses; proofs through the algebra of generalized functions are gathered at the end of the chapter (Bracewell, p. 105).⟧</p>"),
                ("⟦Sáu cặp tham chiếu||Six reference pairs⟧",
                 "<p>⟦Ba cặp đầu là những cặp quen thuộc: Gauss tự biến đổi, sinc và xung chữ nhật, sinc$^2$ và tam giác (tr. 105 đến 106):||The first three are familiar: the self-transforming Gaussian, sinc and the rectangle, sinc$^2$ and the triangle (pp. 105 to 106):⟧</p>"
                 + F("⟦Ba cặp đầu||First three pairs⟧", r"e^{-\pi x^2}\supset e^{-\pi s^2},\qquad \operatorname{sinc}x\supset\Pi(s),\qquad \operatorname{sinc}^2x\supset\Lambda(s)")
                 + "<p>⟦Ba cặp còn lại là cặp trong giới hạn: $1\\supset\\delta(s)$, $\\cos\\pi x\\supset\\mu(s)$, $\\sin\\pi x\\supset i\\nu(s)$. Notebook kiểm ba cặp đầu tại $s=0.3$: {{p_g}}, {{p_sinc}}, {{p_sinc2}}.||The other three are pairs in the limit: $1\\supset\\delta(s)$, $\\cos\\pi x\\supset\\mu(s)$, $\\sin\\pi x\\supset i\\nu(s)$. The notebook checks the first three at $s=0.3$: {{p_g}}, {{p_sinc}}, {{p_sinc2}}.⟧</p>"),
                ("⟦Tương hỗ: hai câu nói khác nhau||Reciprocity: two different statements⟧",
                 "<p>⟦Hình 6.1 nói $\\Pi(s)$ là biến đổi của $\\text{sinc}\\,x$; ta có thể thêm hình đổi trái phải nói sinc $s$ là biến đổi của $\\Pi(x)$, hệ quả của tính tương hỗ, nhưng hai phát biểu có bản chất khác. Phát biểu thứ nhất nói tích phân của tích hai hàm khá bình thường bằng 1 khi $|s|<\\tfrac12$ và bằng 0 khi $|s|>\\tfrac12$, đổi đột ngột dù $s$ đổi rất ít (tr. 106).||"
                 "Fig. 6.1 says $\\Pi(s)$ is the transform of $\\text{sinc}\\,x$; a second figure with left and right interchanged could say sinc $s$ is the transform of $\\Pi(x)$, a consequence of reciprocity, but the two statements have different characters. The first says the integral of the product of rather ordinary functions equals 1 for $|s|<\\tfrac12$ and 0 for $|s|>\\tfrac12$, changing abruptly however little $s$ changes (p. 106).⟧</p>"
                 + F("⟦Hai chiều||Two directions⟧", r"\int_{-\infty}^{\infty}\operatorname{sinc}x\,e^{-i2\pi xs}\,dx=\Pi(s),\qquad \operatorname{sinc}s=\int_{-1/2}^{1/2}e^{-i2\pi xs}\,dx")),
                ("⟦Thử số: tích phân của sinc nhảy quanh $|s|=\\tfrac12$||Numerical test: the integral of sinc jumps around $|s|=\\tfrac12$⟧",
                 "<p>⟦Cắt tích phân ở $|x|\\le200$: tại $s=0.3$ được {{re_03}}, tại $s=0.7$ được {{re_07}}, và ngay tại $s=0.5$ được {{re_05}}, đúng trung bình của 1 và 0. Hai cách (tích phân dao động và công thức qua hàm $\\text{Si}$) cho cùng số.||"
                 "Cutting the integral at $|x|\\le200$: at $s=0.3$ we get {{re_03}}, at $s=0.7$ we get {{re_07}}, and right at $s=0.5$ we get {{re_05}}, the mean of 1 and 0. Two methods (the oscillatory integral and the formula through $\\text{Si}$) give the same numbers.⟧</p>"),
                ("⟦Cặp trong giới hạn: $1\\supset\\delta(s)$||A pair in the limit: $1\\supset\\delta(s)$⟧",
                 "<p>⟦Từ kết quả của Gauss và một phép thế biến đơn giản: $\\int e^{-\\pi a^2x^2}e^{-i2\\pi xs}dx=|a|^{-1}e^{-\\pi s^2/a^2}$. Khi $a\\to0$, vế phải là dãy xác định $\\delta(s)$, còn vế trái là biến đổi của thứ mà trong giới hạn là 1. Vậy 1 là biến đổi Fourier trong giới hạn của $\\delta(s)$ (tr. 106). Số đo: đỉnh tại $s=0$ là {{gs_10}} khi $a=0.1$ và {{gs_20}} khi $a=0.05$.||"
                 "From the Gaussian result and a simple substitution: $\\int e^{-\\pi a^2x^2}e^{-i2\\pi xs}dx=|a|^{-1}e^{-\\pi s^2/a^2}$. As $a\\to0$ the right side is a defining sequence for $\\delta(s)$ and the left side is the transform of what in the limit is unity. So 1 is the Fourier transform in the limit of $\\delta(s)$ (p. 106). Measured: the peak at $s=0$ is {{gs_10}} for $a=0.1$ and {{gs_20}} for $a=0.05$.⟧</p>"
                 + F("⟦Một và xung||One and the impulse⟧", r"1\ \supset\ \delta(s),\qquad \delta(x)\ \supset\ 1")),
                ("⟦Sóng phức và cosin: cặp xung||The complex wave and the cosine: impulse pairs⟧",
                 "<p>⟦Từ $\\int e^{-\\pi a^2x^2}e^{i\\pi x}e^{-i2\\pi xs}dx=|a|^{-1}e^{-\\pi(s-1/2)^2/a^2}$ ta được $e^{i\\pi x}\\supset\\delta(s-\\tfrac12)$. Tách phần thực và ảo, phần chẵn và lẻ: $\\cos\\pi x\\supset\\mu(s)$ và $i\\sin\\pi x\\supset-\\nu(s)$ (tr. 108). Số đo: với cửa sổ Gauss $a=0.05$, đỉnh của $\\cos\\pi x$ tại $s=0.5$ cao {{cos_peak}} và diện tích {{cos_area}}, đúng $\\tfrac12\\delta(s-\\tfrac12)$.||"
                 "From $\\int e^{-\\pi a^2x^2}e^{i\\pi x}e^{-i2\\pi xs}dx=|a|^{-1}e^{-\\pi(s-1/2)^2/a^2}$ we get $e^{i\\pi x}\\supset\\delta(s-\\tfrac12)$. Splitting into real and imaginary, even and odd parts: $\\cos\\pi x\\supset\\mu(s)$ and $i\\sin\\pi x\\supset-\\nu(s)$ (p. 108). Measured: with a Gaussian window $a=0.05$ the peak of $\\cos\\pi x$ at $s=0.5$ has height {{cos_peak}} and area {{cos_area}}, exactly $\\tfrac12\\delta(s-\\tfrac12)$.⟧</p>"),
                ("⟦Bảng tóm tắt các cặp||Summary of the pairs⟧",
                 TBL(["$f(x)$", "$F(s)$"],
                     [["$e^{-\\pi x^2}$", "$e^{-\\pi s^2}$"], ["$\\Pi(x)$", "$\\text{sinc}\\,s$"], ["$\\text{sinc}\\,x$", "$\\Pi(s)$"], ["$\\text{sinc}^2x$", "$\\Lambda(s)$"], ["$1$", "$\\delta(s)$"],
                      ["$\\cos\\pi x$", "$\\mu(s)=\\tfrac12\\delta(s+\\tfrac12)+\\tfrac12\\delta(s-\\tfrac12)$"], ["$\\sin\\pi x$", "$i\\nu(s)$"], ["$\\delta(x)$", "$1$"], ["$e^{i\\pi x}$", "$\\delta(s-\\tfrac12)$"]])),
                ("⟦Tính chất gồm trong bộ mẫu||Properties present in the sample set⟧",
                 "<p>⟦Các cặp được chọn có nhiều tính chất: gián đoạn, xung, giới hạn bề rộng, không âm và lẻ. Các ví dụ duy nhất phức hoặc không đối xứng là $e^{i\\pi x}\\supset\\delta(s-\\tfrac12)$ và $\\delta(x-\\tfrac12)\\supset e^{-i\\pi s}$ (tr. 108). Chúng cũng đều có diễn giải vật lý sẽ được nêu sau.||"
                 "The chosen pairs exhibit many properties: discontinuity, impulsiveness, limited extent, non-negativeness and oddness. The only complex or nonsymmetrical examples are $e^{i\\pi x}\\supset\\delta(s-\\tfrac12)$ and $\\delta(x-\\tfrac12)\\supset e^{-i\\pi s}$ (p. 108). All have physical interpretations brought out later.⟧</p>"),
                ("⟦Tự kiểm tra phần 1||Self-check, part 1⟧",
                 UL(["⟦Vì sao $\\int\\text{sinc}\\,x\\,e^{-i2\\pi xs}dx$ có giá trị {{re_05}} tại $s=0.5$?||Why does $\\int\\text{sinc}\\,x\\,e^{-i2\\pi xs}dx$ have value {{re_05}} at $s=0.5$?⟧",
                     "⟦Biến đổi trong giới hạn của $\\cos\\pi x$ là gì?||What is the transform in the limit of $\\cos\\pi x$?⟧",
                     "⟦Đỉnh của dãy Gauss $|a|^{-1}e^{-\\pi s^2/a^2}$ thay đổi ra sao khi $a\\to0$?||How does the peak of the Gaussian sequence $|a|^{-1}e^{-\\pi s^2/a^2}$ change as $a\\to0$?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: trung bình hai phía của bước nhảy; cặp xung chẵn $\\mu(s)$; cao lên như $1/a$ và hẹp lại, diện tích giữ 1.||Hints: the mean of the two sides of the jump; the even pair $\\mu(s)$; it grows like $1/a$ and narrows, keeping area 1.⟧</p>"),
            ]),
        # ---------------------------------------------------------------- PART 2
        dict(
            title="⟦Định lý tỉ lệ, cộng và dịch||The similarity, addition and shift theorems⟧",
            scr=("⟦Nén trục thời gian, cộng hai tín hiệu, hoặc trễ một tín hiệu là những phép biến đổi quen thuộc.||Compressing the time axis, adding two signals or delaying a signal are familiar operations.⟧",
                 "⟦Chúng làm gì với phổ, và có bảo toàn diện tích, năng lượng, biên độ không?||What do they do to the spectrum, and do they conserve area, energy, amplitude?⟧",
                 "⟦Tỉ lệ đổi ngược hai trục, cộng bảo toàn tuyến tính, và dịch chỉ đổi pha tuyến tính theo tần số.||Similarity inverts the two axes, addition preserves linearity, and shift only changes phase linearly with frequency.⟧"),
            preview=["⟦Tỉ lệ và bảo toàn diện tích, năng lượng||Similarity, and conservation of area and energy⟧", "⟦Cộng và tuyến tính||Addition and linearity⟧", "⟦Dịch: pha tuyến tính, độ trễ nhóm||Shift: linear phase and group delay⟧"],
            slides=[
                ("⟦Định lý tỉ lệ||The similarity theorem⟧",
                 "<p>⟦Nếu $f(x)$ có biến đổi $F(s)$ thì $f(ax)$ có biến đổi $|a|^{-1}F(s/a)$. Chứng minh bằng đổi biến $x'=ax$ (Bracewell, tr. 108). Dấu môđun bù cho việc đổi cận khi $a<0$.||"
                 "If $f(x)$ has transform $F(s)$ then $f(ax)$ has transform $|a|^{-1}F(s/a)$. Proof by the substitution $x'=ax$ (Bracewell, p. 108). The modulus counteracts the interchange of limits when $a<0$.⟧</p>"
                 + F("⟦Định lý tỉ lệ||Similarity theorem⟧", r"f(ax)\ \supset\ \frac{1}{|a|}\,F\!\left(\frac sa\right)")),
                ("⟦Nén trục này thì giãn trục kia, và diện tích giữ nguyên||Compress one axis and the other expands, with area conserved⟧",
                 "<p>⟦Nén thang thời gian tương ứng với giãn thang tần số. Nhưng khi một thành viên giãn ngang, thành viên kia không chỉ co ngang mà còn cao lên, sao cho diện tích bên dưới không đổi (hình 6.2, tr. 109). Số đo với Gauss $a=2$: $f(2x)$ có diện tích {{sim_area}}; biến đổi tại 0 cao {{sim_area}}; tại $s=0.3$ bằng {{sim_03}}, đúng $\\tfrac12e^{-\\pi(0.15)^2}$.||"
                 "Compressing the time scale corresponds to expanding the frequency scale. But as one member expands horizontally the other not only contracts horizontally but also grows vertically so as to keep constant the area beneath it (Fig. 6.2, p. 109). Measured with the Gaussian and $a=2$: $f(2x)$ has area {{sim_area}}; its transform is {{sim_area}} high at 0; at $s=0.3$ it equals {{sim_03}}, exactly $\\tfrac12e^{-\\pi(0.15)^2}$.⟧</p>{{fig:similarity}}"),
                ("⟦Cosinusoid giãn ra: xung dịch chỗ, không co lại||An expanded cosinusoid: the impulses shift, they do not shrink⟧",
                 "<p>⟦Trường hợp đặc biệt của hàm tuần hoàn và xung: giãn một cosinusoid chỉ dịch các xung của biến đổi. Đây không đơn thuần là nén thang $s$, vì khi đó cường độ xung phải giảm (hình 6.3, tr. 109 đến 110). Số đo với cửa sổ Gauss $a=0.05$: đỉnh của $\\cos2\\pi(2x)$ tại $s=2$ cao {{cos_h_2}} và của $\\cos2\\pi(4x)$ tại $s=4$ cũng cao {{cos_h_4}}.||"
                 "A special case with periodic functions and impulses: expanding a cosinusoid simply shifts the impulses of the transform. This is not simply a compression of the $s$ scale, for that would reduce the strength of the impulses (Fig. 6.3, pp. 109 to 110). Measured with a Gaussian window $a=0.05$: the peak of $\\cos2\\pi(2x)$ at $s=2$ is {{cos_h_2}} high and that of $\\cos2\\pi(4x)$ at $s=4$ is also {{cos_h_4}} high.⟧</p>"),
                ("⟦Dạng đối xứng của định lý tỉ lệ||The symmetric version of the similarity theorem⟧",
                 "<p>⟦Nếu $f(x)$ có biến đổi $F(s)$ thì $|a|^{1/2}f(ax)$ có biến đổi $|b|^{1/2}F(bs)$ với $b=a^{-1}$. Khi mỗi hàm giãn hoặc co, nó cũng thấp xuống hay cao lên để bù, sao cho tích phân của bình phương không đổi, như sẽ thấy từ định lý công suất (hình 6.4, tr. 110). Số đo: $\\int f^2$ = {{sym_energy}} và $\\int(|a|^{1/2}f(ax))^2$ cũng {{sym_energy}} với $a=2$.||"
                 "If $f(x)$ has transform $F(s)$ then $|a|^{1/2}f(ax)$ has transform $|b|^{1/2}F(bs)$ with $b=a^{-1}$. As each function expands or contracts it also shrinks or grows vertically to compensate, so the integral of its square is maintained constant, as the power theorem will show (Fig. 6.4, p. 110). Measured: $\\int f^2$ = {{sym_energy}} and $\\int(|a|^{1/2}f(ax))^2$ is also {{sym_energy}} for $a=2$.⟧</p>"
                 + F("⟦Dạng đối xứng||Symmetric form⟧", r"|a|^{1/2}f(ax)\ \supset\ |b|^{1/2}F(bs),\qquad b=a^{-1}")),
                ("⟦Định lý cộng||The addition theorem⟧",
                 "<p>⟦Nếu $f$ và $g$ có biến đổi $F$ và $G$ thì $f+g$ có biến đổi $F+G$. Định lý phản ánh sự phù hợp của biến đổi Fourier với bài toán tuyến tính. Hệ quả: $af$ có biến đổi $aF$ với $a$ là hằng số (tr. 110 đến 111). Số đo: biến đổi của $e^{-\\pi x^2}+2e^{-|x|}$ tại $s=0.3$ là {{add_03}}, đúng tổng các biến đổi.||"
                 "If $f$ and $g$ have transforms $F$ and $G$ then $f+g$ has transform $F+G$. The theorem reflects the suitability of the Fourier transform for linear problems. A corollary: $af$ has transform $aF$ for a constant $a$ (pp. 110 to 111). Measured: the transform of $e^{-\\pi x^2}+2e^{-|x|}$ at $s=0.3$ is {{add_03}}, exactly the sum of the transforms.⟧</p>"
                 + F("⟦Cộng||Addition⟧", r"f(x)+g(x)\ \supset\ F(s)+G(s)")),
                ("⟦Định lý dịch||The shift theorem⟧",
                 "<p>⟦Nếu $f(x)$ có biến đổi $F(s)$ thì $f(x-a)$ có biến đổi $e^{-i2\\pi as}F(s)$ (tr. 111). Dịch một hàm theo chiều dương một lượng $a$ không đổi biên độ của thành phần nào, nên thay đổi ở biến đổi chỉ là pha. Số đo với Gauss dịch $a=0.25$ tại $s=0.3$: độ lớn {{shift_mag}} (không đổi) và pha {{shift_ph}} độ, đúng $-2\\pi as$.||"
                 "If $f(x)$ has transform $F(s)$ then $f(x-a)$ has transform $e^{-i2\\pi as}F(s)$ (p. 111). Shifting a function by $a$ in the positive direction changes no Fourier component in amplitude, so the changes in the transform are confined to phase. Measured with the Gaussian shifted by $a=0.25$ at $s=0.3$: magnitude {{shift_mag}} (unchanged) and phase {{shift_ph}} degrees, exactly $-2\\pi as$.⟧</p>"
                 + F("⟦Dịch||Shift⟧", r"f(x-a)\ \supset\ e^{-i2\pi a s}\,F(s)")),
                ("⟦Vì sao pha tỉ lệ với $s$||Why the phase is proportional to $s$⟧",
                 "<p>⟦Mỗi thành phần bị trễ pha một lượng tỉ lệ với $s$: tần số càng cao, thay đổi góc pha càng lớn. Lý do là độ dời tuyệt đối $a$ chiếm phần lớn hơn của chu kỳ $s^{-1}$ khi tần số cao. Trễ pha bằng $a/s^{-1}$ chu kỳ, tức $2\\pi as$ radian; hằng số tỉ lệ $2\\pi a$ là tốc độ đổi pha theo tần số (tr. 111). Số đo: độ dốc của pha đã gỡ cuốn theo $s$ là {{group_slope}} rad trên đơn vị $s$, đúng $-2\\pi a$.||"
                 "Each component is delayed in phase by an amount proportional to $s$: the higher the frequency, the greater the change in phase angle. This is because the absolute shift $a$ occupies a greater fraction of the period $s^{-1}$ at higher frequency. The phase delay is $a/s^{-1}$ cycles or $2\\pi as$ radians; the constant $2\\pi a$ is the rate of change of phase with frequency (p. 111). Measured: the slope of the unwrapped phase against $s$ is {{group_slope}} rad per unit of $s$, exactly $-2\\pi a$.⟧</p>{{fig:shift_phase}}"),
                ("⟦Ví dụ vật lý: quay chùm sáng bằng lăng kính||A physical example: steering a beam with a prism⟧",
                 "<p>⟦Định lý dịch hiển nhiên trong một hiện thực vật lý cụ thể. Chiếu ánh sáng đơn sắc song song vuông góc lên một khẩu độ. Muốn quay chùm nhiễu xạ một góc nhỏ, ta đổi góc tới đúng góc đó. Nhưng đó chỉ là cách làm pha chiếu sáng đổi tuyến tính trên khẩu độ; cách khác là chèn lăng kính mỏng gây trễ tỉ lệ với bề dày lăng kính ở mỗi điểm (tr. 111 đến 112; chương 13 quay lại).||"
                 "The shift theorem is self-evident in a chosen physical embodiment. Consider parallel monochromatic light falling normally on an aperture. To shift the diffracted beam through a small angle, one changes the angle of incidence by that amount. But that is simply a way of making the phase of the illumination change linearly across the aperture; another way is to insert a thin prism that injects delays proportional to the prism thickness at each point (pp. 111 to 112; chapter 13 returns to it).⟧</p>"),
                ("⟦Xoắn ốc: dịch một phần tư làm biến đổi xoắn 90 độ trên mỗi đơn vị $s$||Twist: shifting by a quarter twists the transform 90 degrees per unit of $s$⟧",
                 "<p>⟦Cho hàm có biến đổi thực. Dịch nó $\\tfrac14$ đơn vị $x$ tương ứng với xoắn đều $\\pi/2$ trên mỗi đơn vị $s$; mặt phẳng chứa $F(s)$ bị biến dạng thành mặt xoắn ốc (hình 6.6, tr. 112 đến 113). Số đo: pha tại $s=1$ là {{twist_1}} độ, tại $s=2$ là {{twist_2}} độ (hoặc $+180$ sau khi cuộn vòng).||"
                 "Take a function whose transform is real. Shifting it by $\\tfrac14$ unit of $x$ corresponds to a uniform twist of $\\pi/2$ per unit of $s$; the plane containing $F(s)$ is deformed into a helicoid (Fig. 6.6, pp. 112 to 113). Measured: the phase at $s=1$ is {{twist_1}} degrees, at $s=2$ it is {{twist_2}} degrees (or $+180$ after wrapping).⟧</p>"),
                ("⟦Cosin trượt: từ thực sang ảo||A sliding cosine: from real to imaginary⟧",
                 "<p>⟦Dịch nhỏ một cosin giữ gần nguyên phần thực của biến đổi nhưng thêm phần ảo lẻ. Dịch tăng thì phần ảo tăng cho tới khi dịch $\\pi/2$ thì không còn phần thực; rồi phần thực trở lại với dấu ngược, và ở dịch $\\pi$ cả hai thành phần đảo pha hoàn toàn (hình 6.7, tr. 113). Hệ số DFT tại tần số của cosin: {{cos_re_01}} và {{cos_im_01}} (thực, ảo) khi lệch pha 0.1 rad; {{cos_re_90}} và {{cos_im_90}} khi lệch $\\pi/2$; {{cos_re_180}} và {{cos_im_180}} khi lệch $\\pi$.||"
                 "A small shift of a cosine leaves the real part of the transform almost intact but introduces an odd imaginary part. With further shift the imaginary part increases until at a shift of $\\pi/2$ there is no real part left; then the real part reappears with opposite sign until at a shift of $\\pi$ both components have undergone a full reversal (Fig. 6.7, p. 113). The DFT coefficient at the cosine's frequency: {{cos_re_01}} and {{cos_im_01}} (real, imaginary) for a phase shift of 0.1 rad; {{cos_re_90}} and {{cos_im_90}} for $\\pi/2$; {{cos_re_180}} and {{cos_im_180}} for $\\pi$.⟧</p>"),
                ("⟦Tự kiểm tra phần 2||Self-check, part 2⟧",
                 UL(["⟦Nếu $f(3x)$ hẹp lại 3 lần, biến đổi thay đổi ra sao về chiều rộng và chiều cao?||If $f(3x)$ is 3 times narrower, how does the transform change in width and height?⟧",
                     "⟦Dịch $f$ đi $a$ làm gì tới $|F|$ và tới pha?||What does shifting $f$ by $a$ do to $|F|$ and to the phase?⟧",
                     "⟦Vì sao bậc thang hay lăng kính đều làm chùm sáng quay?||Why do a tilt of the beam and a prism both steer the beam?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: rộng gấp 3, thấp còn 1/3; $|F|$ giữ nguyên, pha thêm $-2\\pi as$; vì cả hai đều làm pha đổi tuyến tính trên khẩu độ.||Hints: 3 times wider, 1/3 as high; $|F|$ unchanged, phase gets $-2\\pi as$; because both make the phase change linearly across the aperture.⟧</p>"),
            ]),
        # ---------------------------------------------------------------- PART 3
        dict(
            title="⟦Định lý điều chế và định lý tích chập||The modulation and convolution theorems⟧",
            scr=("⟦Điều chế biên độ là cách phát thanh và truyền hình mang tín hiệu trên sóng mang.||Amplitude modulation is how radio and television carry a signal on a carrier wave.⟧",
                 "⟦Phổ của tín hiệu điều chế trông thế nào, và làm sao dùng tích chập để tính nhanh phổ của tích?||What does the spectrum of a modulated signal look like, and how do we use convolution to find the spectrum of a product quickly?⟧",
                 "⟦Nhân với cosin nhân đôi phổ ra hai bản sao nửa cường độ; tích chập trở thành nhân phổ và ngược lại.||Multiplying by a cosine splits the spectrum into two half-strength replicas; convolution becomes multiplication of spectra and vice versa.⟧"),
            preview=["⟦Điều chế: hai bản sao nửa cường độ||Modulation: two half-strength replicas⟧", "⟦Tích chập là nhân phổ, và ba phép kiểm||Convolution is spectral multiplication and three checks⟧", "⟦Hai mươi dạng của định lý||The twenty forms of the theorem⟧"],
            slides=[
                ("⟦Định lý điều chế||The modulation theorem⟧",
                 "<p>⟦Nếu $f(x)$ có biến đổi $F(s)$ thì $f(x)\\cos\\omega x$ có biến đổi $\\tfrac12F(s-\\omega/2\\pi)+\\tfrac12F(s+\\omega/2\\pi)$ (Bracewell, tr. 113 đến 114). Chứng minh viết $\\cos\\omega x$ qua hai hàm mũ phức rồi áp dụng định lý dịch cho biến đổi.||"
                 "If $f(x)$ has transform $F(s)$ then $f(x)\\cos\\omega x$ has transform $\\tfrac12F(s-\\omega/2\\pi)+\\tfrac12F(s+\\omega/2\\pi)$ (Bracewell, pp. 113 to 114). The proof writes $\\cos\\omega x$ through two complex exponentials and applies the shift theorem to the transform.⟧</p>"
                 + F("⟦Điều chế||Modulation⟧", r"f(x)\cos\omega x\ \supset\ \tfrac12F\!\left(s-\tfrac{\omega}{2\pi}\right)+\tfrac12F\!\left(s+\tfrac{\omega}{2\pi}\right)")),
                ("⟦Là một trường hợp riêng của định lý tích chập||A special case of the convolution theorem⟧",
                 "<p>⟦Biến đổi mới là tích chập của $F(s)$ với $\\tfrac12\\delta(s+\\omega/2\\pi)+\\tfrac12\\delta(s-\\omega/2\\pi)$. Trong vô tuyến và truyền hình, sóng mang điều hòa được điều chế bằng một đường bao; phổ của đường bao tách thành hai phần mỗi phần nửa cường độ, dịch dọc trục $s$ một lượng $\\pm\\omega/2\\pi$ (hình 6.8, tr. 115). Số đo: với đường bao Gauss và sóng mang $f_0=3$, đỉnh tại $s=3$ cao {{mod_peak}}, đúng $\\tfrac12F(0)$.||"
                 "The new transform is the convolution of $F(s)$ with $\\tfrac12\\delta(s+\\omega/2\\pi)+\\tfrac12\\delta(s-\\omega/2\\pi)$. In radio and television a harmonic carrier is modulated by an envelope; the spectrum of the envelope separates into two parts, each of half the strength, shifted along the $s$ axis by $\\pm\\omega/2\\pi$ (Fig. 6.8, p. 115). Measured: with a Gaussian envelope and carrier $f_0=3$, the peak at $s=3$ is {{mod_peak}} high, exactly $\\tfrac12F(0)$.⟧</p>{{fig:modulation}}"),
                ("⟦Xung cao tần: phổ là hai sinc||A radio-frequency pulse: the spectrum is two sinc functions⟧",
                 "<p>⟦Xung $\\Pi(x/X)\\cos2\\pi fx$ có phổ $\\tfrac12X\\{\\text{sinc}[X(s+f)]+\\text{sinc}[X(s-f)]\\}$ (bài tập 8, tr. 131). Với $X=10$, $f=1$: tại $s=1$ phổ bằng {{pulse_peak}}; tại $s=1.05$ bằng {{pulse_off}}, bằng cả tích phân số và công thức.||"
                 "The pulse $\\Pi(x/X)\\cos2\\pi fx$ has spectrum $\\tfrac12X\\{\\text{sinc}[X(s+f)]+\\text{sinc}[X(s-f)]\\}$ (problem 8, p. 131). With $X=10$, $f=1$: at $s=1$ the spectrum equals {{pulse_peak}}; at $s=1.05$ it equals {{pulse_off}}, by both numerical integration and the formula.⟧</p>"
                 + F("⟦Phổ xung cao tần||Spectrum of an RF pulse⟧", r"\tfrac12X\left\{\operatorname{sinc}[X(s+f)]+\operatorname{sinc}[X(s-f)]\right\}")),
                ("⟦Xung điều biên: sóng mang và hai dải bên||An amplitude-modulated pulse: carrier and two sidebands⟧",
                 "<p>⟦Xung $\\Pi(x/X)(1+M\\cos2\\pi Fx)\\cos2\\pi fx$ có phổ gồm sóng mang $\\tfrac12X\\text{sinc}$ tại $\\pm f$ và bốn dải bên cường độ $\\tfrac14MX$ tại $\\pm f\\pm F$ (bài tập 9, tr. 132). Với $X=200$, $f=50$, $F=5$, $M=0.6$: sóng mang {{am_carrier}}, dải bên {{am_side}}, tỉ số {{am_ratio}} đúng $M/2$.||"
                 "The pulse $\\Pi(x/X)(1+M\\cos2\\pi Fx)\\cos2\\pi fx$ has a spectrum with a carrier $\\tfrac12X\\text{sinc}$ at $\\pm f$ and four sidebands of strength $\\tfrac14MX$ at $\\pm f\\pm F$ (problem 9, p. 132). With $X=200$, $f=50$, $F=5$, $M=0.6$: carrier {{am_carrier}}, sideband {{am_side}}, ratio {{am_ratio}}, exactly $M/2$.⟧</p>"),
                ("⟦Định lý tích chập||The convolution theorem⟧",
                 "<p>⟦Nếu $f$ có biến đổi $F$ và $g$ có biến đổi $G$ thì $f*g$ có biến đổi $FG$: tích chập hai hàm là nhân hai biến đổi (tr. 117). Chứng minh: đổi thứ tự lấy tích phân rồi dùng định lý dịch.||"
                 "If $f$ has transform $F$ and $g$ has transform $G$ then $f*g$ has transform $FG$: convolution of two functions means multiplication of their transforms (p. 117). Proof: interchange the order of integration and use the shift theorem.⟧</p>"
                 + F("⟦Tích chập||Convolution⟧", r"f*g\ \supset\ F\,G,\qquad f\,g\ \supset\ F*G")),
                ("⟦Tuyến tính cộng bất biến quyết định khi nào dùng được||Linearity plus invariance decides when it applies⟧",
                 "<p>⟦Một đoàn tàu chậm chạy qua cầu: tải tại $x$ là $f(x)$ và độ võng tại $x$ là $h(x)$. Vì các thanh không bị đẩy quá miền ứng suất tỉ lệ biến dạng, độ võng là tổ hợp tuyến tính có trọng số của tải. Nhưng khi tàu đi tiếp, dạng độ võng không đi theo nguyên vẹn, nên không viết được bằng tích chập. Tính tuyến tính cộng bất biến theo $x$ mới làm phân tích Fourier hữu ích; đó cũng là điều kiện cho sóng điều hòa vào cho sóng điều hòa ra cùng tần số (tr. 115).||"
                 "A train slowly crosses a bridge: the load at $x$ is $f(x)$ and the deflection at $x$ is $h(x)$. Since the members are not pushed beyond the regime where stress is proportional to strain, the deflection is a duly weighted linear combination of the load. But as the train moves on, the deflection pattern does not move with it unchanged, so it is not a convolution. Linearity combined with $x$-shift invariance is what makes Fourier analysis useful; it is also the condition for harmonic inputs to give harmonic outputs of unaltered frequency (p. 115).⟧</p>"),
                ("⟦Bốn cách phát biểu bằng lời||Four statements in words⟧",
                 OL(["⟦Biến đổi của một tích chập là tích các biến đổi.||The transform of a convolution is the product of the transforms.⟧",
                     "⟦Biến đổi của một tích là tích chập các biến đổi.||The transform of a product is the convolution of the transforms.⟧",
                     "⟦Tích chập của hai hàm là biến đổi của tích các biến đổi của chúng.||The convolution of two functions is the transform of the product of their transforms.⟧",
                     "⟦Tích của hai hàm là biến đổi của tích chập các biến đổi của chúng.||The product of two functions is the transform of the convolution of their transforms.⟧"]) + "<p>⟦Ký hiệu gạch ngang gọn: $\\overline{f*g}=\\bar f\\bar g$ và $\\overline{fg}=\\bar f*\\bar g$; cũng có $f*g*h\\supset FGH$ và $f*(gh)=(f*g)h$ dạng kết hợp (tr. 117).||With bar notation: $\\overline{f*g}=\\bar f\\bar g$ and $\\overline{fg}=\\bar f*\\bar g$; also $f*g*h\\supset FGH$ (p. 117).⟧</p>"),
                ("⟦Ba phép kiểm hay dùng||Three checks often used⟧",
                 UL(["⟦Diện tích dưới tích chập bằng tích các diện tích: $\\int(f*g)=\\int f\\int g$.||The area under a convolution equals the product of the areas: $\\int(f*g)=\\int f\\int g$.⟧",
                     "⟦Hoành độ các trọng tâm cộng lại: $\\langle x\\rangle_{f*g}=\\langle x\\rangle_f+\\langle x\\rangle_g$.||The abscissas of the centres of gravity add: $\\langle x\\rangle_{f*g}=\\langle x\\rangle_f+\\langle x\\rangle_g$.⟧",
                     "⟦Các mômen bậc hai cộng khi $\\langle x\\rangle_f$ hoặc $\\langle x\\rangle_g$ bằng 0, nghĩa là phương sai cộng (tr. 118).||The second moments add if $\\langle x\\rangle_f$ or $\\langle x\\rangle_g$ is 0, i.e. the variances add (p. 118).⟧"])
                 + "<p>⟦Số đo với $f=e^{-x}H(x)$ và $g=\\Pi$: diện tích {{ch_area}}, trọng tâm {{ch_mean}}, phương sai {{ch_var}} $=1+1/12$.||Measured with $f=e^{-x}H(x)$ and $g=\\Pi$: area {{ch_area}}, centre of gravity {{ch_mean}}, variance {{ch_var}} $=1+1/12$.⟧</p>"),
                ("⟦Hai mươi dạng của định lý||The twenty forms of the theorem⟧",
                 "<p>⟦Khi tính đến liên hợp phức và đảo dấu biến, có tới 20 dạng của định lý tích chập thường được cần. Bracewell liệt kê 10 dạng viết gọn (tr. 118 đến 119), như $f*g\\supset FG$, $f*g(-)\\supset FG(-)$, $f*g^*(-)\\supset FG^*$, $f^*(-)*g^*(-)\\supset F^*G^*$. Notebook kiểm {{forms_ok}} dạng đầu bằng DFT với dãy phức, so tổng trực tiếp với tích các DFT.||"
                 "Allowing for complex conjugates and sign reversals of the variables, there are 20 versions of the convolution theorem that are constantly needed. Bracewell lists 10 abbreviated forms (pp. 118 to 119), such as $f*g\\supset FG$, $f*g(-)\\supset FG(-)$, $f*g^*(-)\\supset FG^*$, $f^*(-)*g^*(-)\\supset F^*G^*$. The notebook checks {{forms_ok}} of these forms with the DFT on complex sequences, comparing the direct sum with the product of DFTs.⟧</p>"),
                ("⟦Định lý tích chập bằng số: hai cách||The convolution theorem numerically: two ways⟧",
                 "<p>⟦Với hai dãy phức độ dài 64, tích chập vòng tính bằng tổng trực tiếp và bằng $\\text{IFFT}(F\\cdot G)$ lệch nhau tối đa {{conv_th_diff}}. Đây là lý do FFT giúp tích chập nhanh (module 3 và 14).||"
                 "For two complex sequences of length 64, the circular convolution computed by the direct sum and by $\\text{IFFT}(F\\cdot G)$ differ by at most {{conv_th_diff}}. That is why the FFT speeds up convolution (modules 3 and 14).⟧</p>"),
                ("⟦Tự kiểm tra phần 3||Self-check, part 3⟧",
                 UL(["⟦Nhân với $\\cos2\\pi f_0x$ làm gì với phổ, và cường độ mỗi bản sao là bao nhiêu?||What does multiplying by $\\cos2\\pi f_0x$ do to the spectrum, and how strong is each replica?⟧",
                     "⟦Vì sao hình dạng độ võng cầu khi tàu chạy không phải một tích chập?||Why is the bridge deflection as the train moves not a convolution?⟧",
                     "⟦Phương sai của $f*g$ bằng bao nhiêu nếu phương sai của $f$ là 2 và của $g$ là 3 (diện tích 1)?||What is the variance of $f*g$ if $f$ has variance 2 and $g$ has variance 3 (unit areas)?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: hai bản sao nửa cường độ dịch $\\pm f_0$; vì thiếu bất biến theo $x$; 5.||Hints: two half-strength replicas shifted by $\\pm f_0$; because it lacks $x$-invariance; 5.⟧</p>"),
            ]),
        # ---------------------------------------------------------------- PART 4
        dict(
            title="⟦Rayleigh, công suất và tự tương quan||Rayleigh, power and autocorrelation⟧",
            scr=("⟦Năng lượng của một hệ có thể tính bằng tích phân theo tọa độ hoặc theo thành phần phổ.||The energy of a system can be computed by integrating over a coordinate or over spectral components.⟧",
                 "⟦Hai cách có cho cùng kết quả không, và với hai hàm khác nhau (điện áp và dòng) thì sao?||Do the two ways agree, and what about two different functions (voltage and current)?⟧",
                 "⟦Rayleigh cho bình phương một hàm, công suất cho tích hai hàm, và tự tương quan cho biến đổi của phổ năng lượng.||Rayleigh handles the square of one function, power handles the product of two, and autocorrelation handles the transform of the energy spectrum.⟧"),
            preview=["⟦Định lý Rayleigh||Rayleigh's theorem⟧", "⟦Định lý công suất||The power theorem⟧", "⟦Định lý tự tương quan||The autocorrelation theorem⟧"],
            slides=[
                ("⟦Định lý Rayleigh||Rayleigh's theorem⟧",
                 "<p>⟦Tích phân bình phương môđun của một hàm bằng tích phân bình phương môđun của phổ (Bracewell, tr. 119). Định lý tương ứng với định lý Parseval của chuỗi Fourier, được Rayleigh dùng lần đầu năm 1889 khi nghiên cứu bức xạ vật đen; mỗi tích phân biểu diễn năng lượng của hệ, một lấy theo mọi giá trị của tọa độ, một lấy theo mọi thành phần phổ (hình 6.9, tr. 119 đến 120).||"
                 "The integral of the squared modulus of a function equals the integral of the squared modulus of its spectrum (Bracewell, p. 119). It corresponds to Parseval's theorem for Fourier series and was first used by Rayleigh in 1889 in his study of black-body radiation; each integral represents the energy of a system, one taken over all values of a coordinate, the other over all spectral components (Fig. 6.9, pp. 119 to 120).⟧</p>"
                 + F("⟦Định lý Rayleigh||Rayleigh's theorem⟧", r"\int_{-\infty}^{\infty}|f(x)|^2\,dx=\int_{-\infty}^{\infty}|F(s)|^2\,ds")),
                ("⟦Điều kiện và tên gọi||Conditions and names⟧",
                 "<p>⟦Trong giới toán học, định lý còn gọi là định lý Plancherel (Titchmarsh, 1924), theo M. Plancherel, người năm 1910 nêu điều kiện để nó đúng: đúng khi cả hai tích phân tồn tại. Gần đây, Carleman chỉ ra nó đúng chỉ cần một trong hai tích phân tồn tại. Rayleigh đơn giản giả định các tích phân tồn tại (tr. 120).||"
                 "In mathematical circles the theorem is called Plancherel's theorem (Titchmarsh, 1924) after M. Plancherel, who in 1910 established conditions under which it is true: it holds if both integrals exist. More recently Carleman showed it is true if one of the integrals exists. Rayleigh simply assumed the integrals existed (p. 120).⟧</p>"),
                ("⟦Thử số: hai ví dụ||Numerical test: two examples⟧",
                 "<p>⟦Với Gauss $e^{-\\pi x^2}$: $\\int f^2$ = {{ray_gauss}} và $\\int|F|^2$ = {{ray_gauss}}. Với $e^{-x}H(x)$: $\\int|f|^2$ = {{ray_exp}} và $\\int|F|^2ds=\\int ds/(1+4\\pi^2s^2)$ = {{ray_exp}}. Cùng số theo hai cách tính độc lập.||"
                 "For the Gaussian $e^{-\\pi x^2}$: $\\int f^2$ = {{ray_gauss}} and $\\int|F|^2$ = {{ray_gauss}}. For $e^{-x}H(x)$: $\\int|f|^2$ = {{ray_exp}} and $\\int|F|^2ds=\\int ds/(1+4\\pi^2s^2)$ = {{ray_exp}}. The same numbers by two independent computations.⟧</p>"),
                ("⟦Định lý công suất||The power theorem⟧",
                 "<p>⟦Tổng quát hơn Rayleigh, cho tích hai hàm: $\\int f\\,g^*dx=\\int F\\,G^*ds$. Mỗi vế biểu diễn năng lượng hay công suất theo hai cách. Cách thứ nhất lấy công suất tức thời là tích một cặp biến liên hợp chính tắc (điện trường và từ trường, điện áp và dòng, lực và vận tốc) tích phân theo thời gian hoặc không gian. Cách thứ hai nhân các thành phần phổ rồi lấy tích phân trên toàn phổ (tr. 120).||"
                 "More general than Rayleigh's, for a product of two functions: $\\int f\\,g^*dx=\\int F\\,G^*ds$. Each side is energy or power computed two ways. In the first, instantaneous power is the product of a pair of canonically conjugate variables (electric and magnetic fields, voltage and current, force and velocity) integrated over time or space. In the second, the spectral components are multiplied and integrated over the whole spectrum (p. 120).⟧</p>"
                 + F("⟦Định lý công suất||Power theorem⟧", r"\int_{-\infty}^{\infty}f(x)\,g^*(x)\,dx=\int_{-\infty}^{\infty}F(s)\,G^*(s)\,ds")),
                ("⟦Thử số: hai Gauss dịch||Numerical test: two shifted Gaussians⟧",
                 "<p>⟦Với $f=e^{-\\pi(x+0.3)^2}$ và $g=e^{-\\pi(x-1)^2}$: $\\int fg\\,dx$ = {{pow_direct}} và $\\int FG^*ds$ = {{pow_fourier}}, trùng nhau. Đây là dạng hai hàm thực nên $F$ và $G$ phức.||"
                 "For $f=e^{-\\pi(x+0.3)^2}$ and $g=e^{-\\pi(x-1)^2}$: $\\int fg\\,dx$ = {{pow_direct}} and $\\int FG^*ds$ = {{pow_fourier}}, equal. Here $f$ and $g$ are real so $F$ and $G$ are complex.⟧</p>"),
                ("⟦Với $f$, $g$ thực: chỉ cần phần thực và phần ảo||For real $f$, $g$: real and imaginary parts suffice⟧",
                 "<p>⟦Nếu $f$ và $g$ thực thì $F$, $G$ là Hermitian: phần thực chẵn, phần ảo lẻ. Các số hạng lẻ không đóng góp vào tích phân vô hạn, nên $\\int fg\\,dx=\\int[\\text{Re}F\\,\\text{Re}G+\\text{Im}F\\,\\text{Im}G]ds$ (hình 6.11, tr. 121). Trong ví dụ trên, tích phân hai phần này là {{pow_re}} và {{pow_im}}, tổng {{pow_fourier}}.||"
                 "If $f$ and $g$ are real then $F$ and $G$ are Hermitian: real parts even, imaginary parts odd. The odd terms do not contribute to the infinite integral, so $\\int fg\\,dx=\\int[\\text{Re}F\\,\\text{Re}G+\\text{Im}F\\,\\text{Im}G]ds$ (Fig. 6.11, p. 121). In the example above the two parts integrate to {{pow_re}} and {{pow_im}}, summing to {{pow_fourier}}.⟧</p>"
                 + F("⟦Dạng thực||Real form⟧", r"\int fg\,dx=\int\left[\operatorname{Re}F\,\operatorname{Re}G+\operatorname{Im}F\,\operatorname{Im}G\right]ds,\qquad \int f(x)g(-x)\,dx=\int F(s)G(s)\,ds")),
                ("⟦Định lý tự tương quan||The autocorrelation theorem||⟧".replace("||⟧", "⟧"),
                 "<p>⟦Hàm tự tương quan $\\int f^*(u)f(u+x)du$ của $f$ có biến đổi $|F(s)|^2$. Trong truyền thông, đó là phát biểu: tự tương quan của một tín hiệu là biến đổi Fourier của phổ công suất của nó; hình 6.12 minh họa (tr. 122). Đặc điểm riêng so với tự chập: thông tin về pha của $F(s)$ hoàn toàn vắng mặt trong $|F|^2$, cũng như tự tương quan không chứa thông tin về pha các thành phần Fourier (module 3, tr. 45).||"
                 "The autocorrelation $\\int f^*(u)f(u+x)du$ of $f$ has transform $|F(s)|^2$. In communications this reads: the autocorrelation function of a signal is the Fourier transform of its power spectrum; Fig. 6.12 illustrates it (p. 122). The distinguishing feature against self-convolution: information about the phase of $F(s)$ is entirely missing from $|F|^2$, just as the autocorrelation contains no information about the phases of the Fourier components (module 3, p. 45).⟧</p>"
                 + F("⟦Tự tương quan||Autocorrelation⟧", r"f\star f\ \supset\ |F(s)|^2")),
                ("⟦Thử số: $\\Pi\\star\\Pi=\\Lambda$ và phổ $\\text{sinc}^2$||Numerical test: $\\Pi\\star\\Pi=\\Lambda$ and the $\\text{sinc}^2$ spectrum⟧",
                 "<p>⟦Tự tương quan của $\\Pi$ là $\\Lambda$, biến đổi tại $s=0.3$ là {{ac_pi_03}}, đúng $\\text{sinc}^2(0.3)=|{\\rm sinc}\\,0.3|^2$. Với Gauss, tự tương quan chuẩn hóa $e^{-\\pi x^2/2}$ có biến đổi $\\sqrt2e^{-2\\pi s^2}$ với tích phân {{ns_int}}: đó là phổ công suất chuẩn hóa tích phân bằng 1 (bài tập trong sách, tr. 122).||"
                 "The autocorrelation of $\\Pi$ is $\\Lambda$, with transform {{ac_pi_03}} at $s=0.3$, exactly $\\text{sinc}^2(0.3)=|\\text{sinc}\\,0.3|^2$. For the Gaussian, the normalised autocorrelation $e^{-\\pi x^2/2}$ has transform $\\sqrt2e^{-2\\pi s^2}$ with integral {{ns_int}}: the normalised power spectrum whose infinite integral is unity (the book's exercise, p. 122).⟧</p>"),
                ("⟦Giới hạn $C(x)$ và phổ công suất; định lý Wiener||The limit $C(x)$ and the power spectrum; Wiener's theorem⟧",
                 "<p>⟦Với tín hiệu chạy mãi, dãy tự tương quan chuẩn hóa $\\gamma_X(x)$ có thể tiến về giới hạn $C(x)$, và khi đó phổ công suất chuẩn hóa của đoạn dài $X$ tiến về dạng giới hạn: $C(x)\\supset|\\Phi_\\infty(s)|^2$. Định lý tương ứng cho tín hiệu không tắt còn được gọi là định lý Wiener (1949) (tr. 122 đến 123). Ví dụ $f=\\cos ax$ có $C=\\cos ax$ và phổ là cặp xung $\\tfrac12\\delta(s\\pm a/2\\pi)$. Số đo với đoạn 10 s của $\\cos2\\pi(5t)$: tỉ lệ công suất tại $+5$ Hz và $-5$ Hz là {{cos_frac}} mỗi bên.||"
                 "For signals that run on, the normalised autocorrelations $\\gamma_X(x)$ may tend to a limit $C(x)$, and then the normalised power spectrum of a segment of length $X$ tends to a limiting form: $C(x)\\supset|\\Phi_\\infty(s)|^2$. The corresponding theorem for signals that do not tend to zero is sometimes called Wiener's theorem (1949) (pp. 122 to 123). For example $f=\\cos ax$ has $C=\\cos ax$ and the spectrum is the impulse pair $\\tfrac12\\delta(s\\pm a/2\\pi)$. Measured over a 10 s segment of $\\cos2\\pi(5t)$: the fraction of power at $+5$ Hz and at $-5$ Hz is {{cos_frac}} on each side.⟧</p>"),
                ("⟦Tự kiểm tra phần 4||Self-check, part 4⟧",
                 UL(["⟦Rayleigh đúng cho $e^{-x}H(x)$: hai vế bằng bao nhiêu?||Rayleigh holds for $e^{-x}H(x)$: what do the two sides equal?⟧",
                     "⟦Vì sao định lý công suất cần liên hợp $g^*$?||Why does the power theorem need the conjugate $g^*$?⟧",
                     "⟦Tự tương quan có khôi phục được tín hiệu không?||Can the signal be recovered from its autocorrelation?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: ½; để hai vế cho năng lượng dương với hàm phức; không, vì mất pha.||Hints: ½; so both sides give positive energy for complex functions; no, because the phase is lost.⟧</p>"),
            ]),
        # ---------------------------------------------------------------- PART 5
        dict(
            title="⟦Định lý đạo hàm, hàm suy rộng và tổng kết||The derivative theorem, generalized functions and the summary⟧",
            scr=("⟦Đạo hàm là phép toán rất thường gặp: vận tốc từ vị trí, dòng từ điện tích.||Differentiation is very common: velocity from position, current from charge.⟧",
                 "⟦Trong miền tần số đạo hàm trông thế nào, và tính kỹ thuật thế nào khi hàm không có đạo hàm?||What does it look like in the frequency domain, and how do we handle functions without a derivative?⟧",
                 "⟦Đạo hàm là nhân với $i2\\pi s$; các định lý áp dụng cho hàm suy rộng, và gom lại thành bảng 6.1.||Differentiation is multiplication by $i2\\pi s$; the theorems extend to generalized functions and collect into Table 6.1.⟧"),
            preview=["⟦Định lý đạo hàm và đạo hàm của tích chập||The derivative theorem and the derivative of a convolution⟧", "⟦Biến đổi của hàm suy rộng, chứng minh||The transform of a generalized function and proofs⟧", "⟦Bảng 6.1 và các bài tập chọn||Table 6.1 and selected problems⟧"],
            slides=[
                ("⟦Định lý đạo hàm||The derivative theorem⟧",
                 "<p>⟦Nếu $f(x)$ có biến đổi $F(s)$ thì $f'(x)$ có biến đổi $i2\\pi sF(s)$ (Bracewell, tr. 124). Chứng minh: viết đạo hàm là giới hạn của thương sai phân rồi dùng định lý dịch và cộng. Số đo với $f=e^{-\\pi x^2}$: biến đổi của $f'$ tại $s=0.3$ có độ lớn {{der_03}}, đúng $2\\pi s\\,e^{-\\pi s^2}$.||"
                 "If $f(x)$ has transform $F(s)$ then $f'(x)$ has transform $i2\\pi sF(s)$ (Bracewell, p. 124). Proof: write the derivative as the limit of a difference quotient and use the shift and addition theorems. Measured with $f=e^{-\\pi x^2}$: the transform of $f'$ at $s=0.3$ has magnitude {{der_03}}, exactly $2\\pi s\\,e^{-\\pi s^2}$.⟧</p>"
                 + F("⟦Đạo hàm||Derivative⟧", r"f'(x)\ \supset\ i2\pi s\,F(s)")),
                ("⟦Đạo hàm tăng cường tần số cao||Differentiation enhances high frequencies⟧",
                 "<p>⟦Nhân với $i2\\pi s$ nghĩa là đạo hàm tăng cường thành phần tần số cao, làm yếu thành phần tần số thấp và triệt tiêu thành phần tần số 0 (hình 6.13 và 6.14, tr. 125). Áp dụng lặp lại nhân với $(i2\\pi s)^n$: cực đại của $|(2\\pi s)^ne^{-\\pi s^2}|$ nằm ở {{pk1}} ($n=1$), {{pk2}} ($n=2$), {{pk3}} ($n=3$), dịch dần lên tần số cao, đúng $\\sqrt{n/2\\pi}$.||"
                 "Multiplying by $i2\\pi s$ means differentiation enhances the higher frequencies, attenuates the lower frequencies and suppresses any zero-frequency component (Figs. 6.13 and 6.14, p. 125). Repeated application multiplies by $(i2\\pi s)^n$: the maximum of $|(2\\pi s)^ne^{-\\pi s^2}|$ lies at {{pk1}} ($n=1$), {{pk2}} ($n=2$), {{pk3}} ($n=3$), shifting up in frequency, exactly $\\sqrt{n/2\\pi}$.⟧</p>{{fig:derivative}}"),
                ("⟦Khi đạo hàm có gián đoạn vô hạn: xung vào cuộc||When the derivative has infinite discontinuities: impulses step in⟧",
                 "<p>⟦Thường phép nhân với $i2\\pi s$ làm tích phân của $|i2\\pi sF(s)|$ phân kỳ; tương ứng đạo hàm $f'(x)$ có gián đoạn vô hạn. Tình huống này được ký hiệu xung và các đạo hàm của nó thu nạp (tr. 125). Số đo với bậc thang tắt dần $e^{-\\varepsilon x}H(x)$: biến đổi của đạo hàm là $i2\\pi s/(\\varepsilon+i2\\pi s)$, lệch khỏi 1 (biến đổi của $\\delta$) chỉ {{step_dev}} khi $\\varepsilon=10^{-3}$ và $s=0.5$.||"
                 "It frequently happens that multiplication by $i2\\pi s$ makes the integral of $|i2\\pi sF(s)|$ diverge; correspondingly $f'(x)$ exhibits infinite discontinuities. Such situations are accommodated by the impulse symbol and its derivatives (p. 125). Measured with the decaying step $e^{-\\varepsilon x}H(x)$: the transform of the derivative is $i2\\pi s/(\\varepsilon+i2\\pi s)$, which differs from 1 (the transform of $\\delta$) by only {{step_dev}} for $\\varepsilon=10^{-3}$ and $s=0.5$.⟧</p>"),
                ("⟦Đạo hàm của một tích chập||The derivative of a convolution⟧",
                 "<p>⟦Từ định lý đạo hàm cùng định lý tích chập: nếu $h=f*g$ thì $h'=f'*g=f*g'$: đạo hàm của tích chập là tích chập của một hàm với đạo hàm của hàm kia (tr. 126). Có thể viết bằng xung: $h=\\delta*h$ nên $h'=\\delta'*h=(\\delta'*f)*g=f'*g$. Công thức chủ yếu có giá trị lý thuyết, như suy ra quan hệ bất định và công thức đáp ứng của bộ lọc từ đáp ứng xung và đáp ứng bậc thang.||"
                 "From the derivative theorem together with the convolution theorem: if $h=f*g$ then $h'=f'*g=f*g'$: the derivative of a convolution is the convolution of either function with the derivative of the other (p. 126). In impulse notation $h=\\delta*h$, so $h'=\\delta'*h=(\\delta'*f)*g=f'*g$. The formulas are mostly of theoretical value, such as deducing the uncertainty relation and the filter response from the impulse and step responses.⟧</p>"
                 + F("⟦Đạo hàm của tích chập||Derivative of a convolution⟧", r"(f*g)'=f'*g=f*g'")),
                ("⟦Thử số: đáp ứng qua đáp ứng bậc thang||Numerical test: the response through the step response⟧",
                 "<p>⟦Với mạch RC ($h=e^{-t}H(t)$, đáp ứng bậc thang $s(t)=1-e^{-t}$) và vào $x(t)=\\sin(2\\pi t)$ bật mượt, đáp ứng $y=x*h$ bằng $x'*s$: lệch tối đa {{ds_diff}}. Nghĩa là biết đáp ứng bậc thang là đủ để tính đáp ứng với mọi vào khả vi.||"
                 "For an RC circuit ($h=e^{-t}H(t)$, step response $s(t)=1-e^{-t}$) and a smoothly switched-on input $x(t)=\\sin(2\\pi t)$, the response $y=x*h$ equals $x'*s$: the largest deviation is {{ds_diff}}. Knowing the step response is enough to compute the response to any differentiable input.⟧</p>"),
                ("⟦Biến đổi của hàm suy rộng||The transform of a generalized function⟧",
                 "<p>⟦Cho $p(x)$ là hàm suy rộng xác định bởi dãy $p_\\tau$; biến đổi các phần tử của dãy thành $P_\\tau(s)$. Từ định lý năng lượng, dãy $P_\\tau$ chính quy nên xác định hàm suy rộng $P(s)$, biến đổi Fourier của $p$, với $\\int PF\\,ds=\\int p(x)f(-x)dx$ cho mọi hàm thử (tr. 127). Số đo với $p=\\delta(x-a)$, $a=0.5$: $\\int e^{-i2\\pi as}e^{-\\pi s^2}ds$ = {{gf_05}}, đúng $e^{-\\pi a^2}$.||"
                 "Let $p(x)$ be a generalized function defined by the sequence $p_\\tau$; transform the members to $P_\\tau(s)$. From the energy theorem the sequence $P_\\tau$ is regular so it defines a generalized function $P(s)$, the Fourier transform of $p$, with $\\int PF\\,ds=\\int p(x)f(-x)dx$ for every test function (p. 127). Measured with $p=\\delta(x-a)$, $a=0.5$: $\\int e^{-i2\\pi as}e^{-\\pi s^2}ds$ = {{gf_05}}, exactly $e^{-\\pi a^2}$.⟧</p>"
                 + F("⟦Định lý năng lượng cho hàm suy rộng||Energy theorem for generalized functions⟧", r"\int P(s)\,F(s)\,ds=\int p(x)\,f(-x)\,dx")),
                ("⟦Nhân với đa thức, và vì sao không có tích hai hàm suy rộng||Multiplying by polynomials, and why there is no product of two generalized functions⟧",
                 "<p>⟦Nếu $\\phi(x)$ có đạo hàm mọi cấp nhưng tăng không quá nhanh (như đa thức; không gồm $e^x$, $\\log x$) thì $\\phi p$ vẫn là hàm suy rộng. Nhưng không có gì được gọi là tích của hai hàm suy rộng: tích hai dãy xác định không nhất thiết chính quy (tr. 127 đến 128). Vì vậy $[\\delta(x)]^2$ không có nghĩa, và định lý công suất chỉ chứng minh được dạng $\\int PF\\,ds=\\int pf(-x)dx$ (tr. 129).||"
                 "If $\\phi(x)$ has derivatives of all orders but grows no faster than a power (a polynomial, but not $e^x$ or $\\log x$) then $\\phi p$ is still a generalized function. But nothing is introduced that could be called the product of two generalized functions: the product of two defining sequences is not necessarily regular (pp. 127 to 128). So $[\\delta(x)]^2$ has no meaning, and the best power theorem that can be proved is $\\int PF\\,ds=\\int pf(-x)dx$ (p. 129).⟧</p>"),
                ("⟦Chứng minh chặt: tỉ lệ cộng dịch và đạo hàm||Rigorous proofs: similarity with shift, and the derivative⟧",
                 "<p>⟦Các \"chứng minh\" ngắn trong chương hữu ích khi học định lý nhưng chưa phải chứng minh chặt (như Lighthill, 1958). Với hàm suy rộng, tỉ lệ và dịch được chứng minh cùng lúc: $p(ax+b)\\supset|a|^{-1}e^{i2\\pi bs/a}P(s/a)$. Định lý đạo hàm: biến đổi của $p_\\tau'$ là $i2\\pi sP_\\tau$ nên biến đổi của $p'$ là $i2\\pi sP$ (tr. 128 đến 129). Số đo với Gauss, $a=2$, $b=0.3$, $s=0.4$: độ lớn {{sb_mag}}, pha {{sb_ph}} độ, tính bằng tích phân số và công thức.||"
                 "The short \"derivations\" in the chapter are useful while learning but do not qualify as strict proofs (as in Lighthill, 1958). For generalized functions, similarity and shift are proved together: $p(ax+b)\\supset|a|^{-1}e^{i2\\pi bs/a}P(s/a)$. The derivative theorem: the transform of $p_\\tau'$ is $i2\\pi sP_\\tau$ so that of $p'$ is $i2\\pi sP$ (pp. 128 to 129). Measured with the Gaussian, $a=2$, $b=0.3$, $s=0.4$: magnitude {{sb_mag}}, phase {{sb_ph}} degrees, by numerical integration and the formula.⟧</p>"
                 + F("⟦Tỉ lệ cộng dịch||Similarity with shift⟧", r"p(ax+b)\ \supset\ \frac{1}{|a|}\,e^{i2\pi bs/a}\,P\!\left(\frac sa\right)")),
                ("⟦Hai chiều||Two dimensions⟧",
                 "<p>⟦Mọi định lý trên mở rộng dễ dàng sang hai chiều. Phép quay và cắt xiên, không có ở một chiều, gắn với các định lý cơ bản mới; đối xứng tròn đưa vào các trường hợp riêng quan trọng; và định lý afin cho hàm dạng $f(ax+by+c,\\,dx+ey+f)$ có nhiều ý nghĩa cho đồ họa (Bracewell và cộng sự 1993, Bracewell 1994) (tr. 129).||"
                 "All the above theorems generalise readily to two dimensions. Rotation and shear, which do not arise in one dimension, are associated with new basic theorems, circular symmetry introduces important special cases, and the affine theorem for functions of the form $f(ax+by+c,\\,dx+ey+f)$ has rich implications for graphics (Bracewell et al. 1993, Bracewell 1994) (p. 129).⟧</p>"),
                ("⟦Bảng 6.1: các định lý||Table 6.1: the theorems⟧",
                 TBL(["⟦Định lý||Theorem⟧", "$f(x)$", "$F(s)$"],
                     [["⟦Tỉ lệ||Similarity⟧", "$f(ax)$", "$|a|^{-1}F(s/a)$"], ["⟦Cộng||Addition⟧", "$f+g$", "$F+G$"], ["⟦Dịch||Shift⟧", "$f(x-a)$", "$e^{-i2\\pi as}F(s)$"],
                      ["⟦Điều chế||Modulation⟧", "$f\\cos\\omega x$", "$\\tfrac12F(s-\\tfrac\\omega{2\\pi})+\\tfrac12F(s+\\tfrac\\omega{2\\pi})$"], ["⟦Tích chập||Convolution⟧", "$f*g$", "$FG$"],
                      ["⟦Tự tương quan||Autocorrelation⟧", "$f\\star f$", "$|F|^2$"], ["⟦Đạo hàm||Derivative⟧", "$f'(x)$", "$i2\\pi sF(s)$"],
                      ["⟦Đạo hàm của tích chập||Derivative of convolution⟧", "$(f*g)'$", "$f'*g=f*g'$"], ["Rayleigh", "$\\int|f|^2dx$", "$\\int|F|^2ds$"], ["⟦Công suất||Power⟧", "$\\int fg^*dx$", "$\\int FG^*ds$"]])),
                ("⟦Bài tập chọn: hình thang, $\\text{sinc}^4$, $xe^{-\\pi x^2}$ và định lý tích phân||Selected problems: trapezoid, $\\text{sinc}^4$, $xe^{-\\pi x^2}$ and the integral theorem⟧",
                 "<p>⟦Bài 10 (tr. 132): hình thang $f=2\\Lambda(x/2)-\\Lambda(x)$ có $F=\\text{sinc}^2s\\,(1+2\\cos2\\pi s)$, tại $s=0.3$ bằng {{trap_03}}. Bài 17 (tr. 133): theo Rayleigh, $\\int\\text{sinc}^4x\\,dx=\\int\\Lambda^2=\\tfrac23$ = {{sinc4}}. Bài 21: biến đổi của $xe^{-\\pi x^2}$ là $-is\\,e^{-\\pi s^2}$, độ lớn {{xg_03}} tại 0.3. Bài 19 và 20: biến đổi của tích phân bất định $\\int_{-\\infty}^xf$ là $F(s)/(i2\\pi s)$ cộng $\\tfrac12F(0)\\delta(s)$ (số hạng bị lãng quên): số đo lệch {{int_thm_diff}} khi kiểm $\\text{FT}[H*f-H]=(F-1)/(i2\\pi s)$.||"
                 "Problem 10 (p. 132): the trapezoid $f=2\\Lambda(x/2)-\\Lambda(x)$ has $F=\\text{sinc}^2s\\,(1+2\\cos2\\pi s)$, equal to {{trap_03}} at $s=0.3$. Problem 17 (p. 133): by Rayleigh, $\\int\\text{sinc}^4x\\,dx=\\int\\Lambda^2=\\tfrac23$ = {{sinc4}}. Problem 21: the transform of $xe^{-\\pi x^2}$ is $-is\\,e^{-\\pi s^2}$, magnitude {{xg_03}} at 0.3. Problems 19 and 20: the transform of the indefinite integral $\\int_{-\\infty}^xf$ is $F(s)/(i2\\pi s)$ plus $\\tfrac12F(0)\\delta(s)$ (the forgotten term): measured deviation {{int_thm_diff}} when checking $\\text{FT}[H*f-H]=(F-1)/(i2\\pi s)$.⟧</p>"),
                ("⟦Tự kiểm tra phần 5||Self-check, part 5⟧",
                 UL(["⟦Biến đổi của $f''$ là gì?||What is the transform of $f''$?⟧",
                     "⟦Vì sao $h'=f'*g=f*g'$?||Why is $h'=f'*g=f*g'$?⟧",
                     "⟦Vì sao \"biến đổi của $\\int f$ là $F/i2\\pi s$\" chưa đủ?||Why is \"the transform of $\\int f$ is $F/i2\\pi s$\" not the whole story?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: $(i2\\pi s)^2F$; từ định lý đạo hàm và tích chập; thiếu số hạng $\\tfrac12F(0)\\delta(s)$ (thành phần một chiều).||Hints: $(i2\\pi s)^2F$; from the derivative and convolution theorems; the term $\\tfrac12F(0)\\delta(s)$ (the DC component) is missing.⟧</p>"),
            ]),
    ],
    takeaways=[
        "⟦Tỉ lệ đổi ngược hai trục và giữ diện tích; dịch chỉ nhân $e^{-i2\\pi as}$, giữ $|F|$.||Similarity inverts the two axes and conserves area; shift only multiplies by $e^{-i2\\pi as}$, keeping $|F|$.⟧",
        "⟦Điều chế cho hai bản sao nửa cường độ dịch $\\pm f_0$; tích chập là nhân phổ và ngược lại.||Modulation gives two half-strength replicas shifted $\\pm f_0$; convolution is multiplication of spectra and vice versa.⟧",
        "⟦Rayleigh và công suất nối năng lượng theo $x$ với theo $s$; tự tương quan $\\supset|F|^2$ và bỏ mất pha.||Rayleigh and power connect energy in $x$ with $s$; autocorrelation $\\supset|F|^2$ and loses phase.⟧",
        "⟦Đạo hàm là nhân $i2\\pi s$; đạo hàm của tích chập chuyển sang một thừa số.||Differentiation is multiplication by $i2\\pi s$; the derivative of a convolution moves onto one factor.⟧",
        "⟦Định lý mở rộng cho hàm suy rộng, nhưng không có tích hai hàm suy rộng.||The theorems extend to generalized functions, but there is no product of two generalized functions.⟧",
    ],
    history="<p>⟦Định lý Rayleigh được Rayleigh dùng lần đầu năm 1889 khi nghiên cứu bức xạ vật đen; nó tương ứng định lý Parseval của chuỗi Fourier. Trong giới toán học nó mang tên Plancherel, người năm 1910 nêu điều kiện đúng; Carleman sau đó chỉ ra chỉ cần một tích phân tồn tại (Bracewell, tr. 119 đến 120).||"
            "Rayleigh's theorem was first used by Rayleigh in 1889 in his study of black-body radiation; it corresponds to Parseval's theorem for Fourier series. Mathematicians call it Plancherel's theorem after Plancherel, who in 1910 established conditions for it; Carleman later showed one integral existing suffices (Bracewell, pp. 119 to 120).⟧</p>"
            "<p>⟦Định lý tự tương quan dạng cho tín hiệu không tắt còn gọi là định lý Wiener (1949) (tr. 122). Sách kể các nguồn: Titchmarsh (1924) cho Plancherel, Lighthill (1958) cho chứng minh chặt qua hàm suy rộng, Bell (1972) về quang phổ biến đổi Fourier, Bracewell và cộng sự (1993) và Bracewell (1994) về định lý afin hai chiều (tr. 130).||"
            "The autocorrelation theorem for signals that do not tend to zero is called Wiener's theorem (1949) (p. 122). The book's sources: Titchmarsh (1924) for Plancherel, Lighthill (1958) for rigorous proofs through generalized functions, Bell (1972) on Fourier transform spectroscopy, Bracewell et al. (1993) and Bracewell (1994) on the two-dimensional affine theorem (p. 130).⟧</p>",
    case="<p>⟦<b>Sóng mang và tin nhắn.</b> Một máy phát điều biên phát xung dài $X=200$ với sóng mang $f=50$ và tin điều biên $F=5$, chỉ số điều chế $M=0.6$. Nhờ định lý điều chế, phổ gồm sóng mang cao {{am_carrier}} và hai dải bên cao {{am_side}} mỗi phía (tỉ số {{am_ratio}} $=M/2$). Mọi thông tin của tin nhắn nằm trong hai dải bên; sóng mang chỉ là \"cần trục\". Bề rộng phổ cần thiết là $2F$ quanh sóng mang, không phụ thuộc $f$: cơ sở để chia kênh vô tuyến.||"
          "<b>Carrier and message.</b> An amplitude-modulated transmitter sends a long pulse $X=200$ with carrier $f=50$ and message $F=5$, modulation index $M=0.6$. By the modulation theorem the spectrum has a carrier of height {{am_carrier}} and two sidebands of height {{am_side}} on each side (ratio {{am_ratio}} $=M/2$). All the message information sits in the two sidebands; the carrier is just the \"crane\". The spectral width needed is $2F$ around the carrier, independent of $f$: the basis for dividing radio channels.⟧</p>"
         "<p>⟦Cùng logic giải thích vì sao một máy thu chỉ cần nhân với cosin sóng mang để đưa dải bên về gốc, rồi lọc thông thấp (giải điều chế).||The same logic explains why a receiver only needs to multiply by the carrier cosine to bring the sidebands back to baseband and then low-pass filter (demodulation).⟧</p>",
    practice=[
        "⟦Mở notebook và chạy cell cài đặt.||Open the notebook and run the setup cell.⟧",
        "⟦Bài 1: kiểm định lý tỉ lệ với $a=0.5$ và $a=-2$; xem dấu môđun quan trọng ra sao.||Task 1: check the similarity theorem with $a=0.5$ and $a=-2$; see why the modulus matters.⟧",
        "⟦Bài 2: dịch một xung chữ nhật và vẽ pha của biến đổi; đo độ dốc rồi suy ra độ dịch.||Task 2: shift a rectangle and plot the phase of its transform; measure the slope and infer the shift.⟧",
        "⟦Bài 3: đổi $M$, $F$, $f$ của xung điều biên và tự dự đoán vị trí, độ cao các dải bên trước khi tính.||Task 3: change $M$, $F$, $f$ of the AM pulse and predict the positions and heights of the sidebands before computing.⟧",
        "⟦Bài 4: kiểm định lý công suất với $f=\\text{sinc}\\,x$ và $g=\\text{sinc}\\,2x$.||Task 4: check the power theorem with $f=\\text{sinc}\\,x$ and $g=\\text{sinc}\\,2x$.⟧",
        "⟦Bài 5: dùng định lý đạo hàm để tìm biến đổi của $x^2e^{-\\pi x^2}$ rồi kiểm bằng số.||Task 5: use the derivative theorem to find the transform of $x^2e^{-\\pi x^2}$ and check numerically.⟧",
    ],
    pitfalls=[
        "<b>⟦\"Nén trục $x$ thì nén cả trục $s$.\"||\"Compressing the $x$ axis compresses the $s$ axis too.\"⟧</b><p>⟦Ngược lại: nén $x$ thì giãn $s$, và biến đổi cao lên $|a|^{-1}$ để giữ diện tích (Gauss $a=2$: đỉnh {{sim_area}}).||It is the opposite: compressing $x$ expands $s$, and the transform grows by $|a|^{-1}$ to keep the area (Gaussian $a=2$: peak {{sim_area}}).⟧</p>",
        "<b>⟦\"Giãn một cosinusoid thì các xung của phổ co lại về gốc và yếu đi.\"||\"Expanding a cosinusoid makes the spectral impulses shrink toward the origin and weaken.\"⟧</b><p>⟦Các xung chỉ dịch chỗ, cường độ giữ nguyên (đỉnh {{cos_h_2}} và {{cos_h_4}} ở hai tần số), vì tỉ lệ $s$ đơn thuần sẽ làm yếu xung (tr. 109 đến 110).||The impulses only move; their strength is unchanged (peaks {{cos_h_2}} and {{cos_h_4}} at the two frequencies), because a plain scaling of $s$ would weaken them (pp. 109 to 110).⟧</p>",
        "<b>⟦\"Dịch một hàm làm thay đổi phổ biên độ.\"||\"Shifting a function changes the amplitude spectrum.\"⟧</b><p>⟦Chỉ đổi pha: độ lớn giữ {{shift_mag}} còn pha thêm {{shift_ph}} độ tại $s=0.3$ (tr. 111).||Only the phase changes: the magnitude stays {{shift_mag}} while the phase gains {{shift_ph}} degrees at $s=0.3$ (p. 111).⟧</p>",
        "<b>⟦\"Biến đổi của tích phân bất định $\\int f$ chỉ là $F/i2\\pi s$.\"||\"The transform of the indefinite integral $\\int f$ is just $F/i2\\pi s$.\"⟧</b><p>⟦Thiếu $\\tfrac12F(0)\\delta(s)$ (thành phần một chiều). Lập luận \"đạo hàm của $\\int f$ là $f$\" chỉ xác định phần không phải một chiều (bài tập 19, tr. 133).||The term $\\tfrac12F(0)\\delta(s)$ (the DC component) is missing. The reasoning \"the derivative of $\\int f$ is $f$\" fixes only the non-DC part (problem 19, p. 133).⟧</p>",
    ],
    refs=[
        "⟦R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chương 6 (tr. 105 đến 135).||R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chapter 6 (pp. 105 to 135).⟧",
    ],
    quiz=[
        dict(q="⟦Biến đổi của Gauss $e^{-\\pi x^2}$ tại $s=0.3$ bằng bao nhiêu?||What is the transform of the Gaussian $e^{-\\pi x^2}$ at $s=0.3$?⟧",
             opts=["{{p_g}}", "0.6065", "0.8584", "0.3679"], explain="⟦Tự biến đổi: $e^{-\\pi(0.3)^2}$ = {{p_g}}.||Self-transforming: $e^{-\\pi(0.3)^2}$ = {{p_g}}.⟧"),
        dict(q="⟦Tích phân $\\int_{-200}^{200}\\text{sinc}\\,x\\,e^{-i2\\pi xs}dx$ tại $s=0.5$ gần bằng bao nhiêu?||What is $\\int_{-200}^{200}\\text{sinc}\\,x\\,e^{-i2\\pi xs}dx$ at $s=0.5$, approximately?⟧",
             opts=["{{re_05}}", "0.9999", "0.0001", "0.2500"], explain="⟦Đúng chỗ nhảy nên bằng trung bình 1 và 0: {{re_05}}; tại 0.3 là {{re_03}}, tại 0.7 là {{re_07}}.||Exactly at the jump so it equals the mean of 1 and 0: {{re_05}}; at 0.3 it is {{re_03}}, at 0.7 it is {{re_07}}.⟧"),
        dict(q="⟦Đỉnh tại $s=0$ của $|a|^{-1}e^{-\\pi s^2/a^2}$ với $a=0.05$ bằng bao nhiêu?||What is the peak at $s=0$ of $|a|^{-1}e^{-\\pi s^2/a^2}$ for $a=0.05$?⟧",
             opts=["{{gs_20}}", "{{gs_10}}", "0.05", "5"], explain="⟦Bằng $1/a$: {{gs_20}} khi $a=0.05$ và {{gs_10}} khi $a=0.1$.||It equals $1/a$: {{gs_20}} for $a=0.05$ and {{gs_10}} for $a=0.1$.⟧"),
        dict(q="⟦Diện tích đỉnh của $\\cos\\pi x$ (cửa sổ Gauss) tại $s=0.5$ là bao nhiêu?||What is the area of the peak of $\\cos\\pi x$ (Gaussian window) at $s=0.5$?⟧",
             opts=["{{cos_area}}", "1", "0.25", "2"], explain="⟦Cặp xung chẵn $\\mu$ có mỗi xung diện tích $\\tfrac12$: {{cos_area}}.||The even pair $\\mu$ has each impulse of area $\\tfrac12$: {{cos_area}}.⟧"),
        dict(q="⟦Với $f=e^{-\\pi x^2}$ và $a=2$, biến đổi của $f(ax)$ tại $s=0.3$ bằng bao nhiêu?||With $f=e^{-\\pi x^2}$ and $a=2$, what is the transform of $f(ax)$ at $s=0.3$?⟧",
             opts=["{{sim_03}}", "0.7537", "0.9317", "0.5"], explain="⟦$|a|^{-1}F(s/a)=\\tfrac12e^{-\\pi(0.15)^2}$ = {{sim_03}}.||$|a|^{-1}F(s/a)=\\tfrac12e^{-\\pi(0.15)^2}$ = {{sim_03}}.⟧"),
        dict(q="⟦Diện tích của $f(2x)$ với $f=e^{-\\pi x^2}$ bằng bao nhiêu?||What is the area of $f(2x)$ for $f=e^{-\\pi x^2}$?⟧",
             opts=["{{sim_area}}", "1", "2", "0.25"], explain="⟦Nén 2 lần làm diện tích giảm còn $1/|a|$ = {{sim_area}}, và biến đổi cũng cao {{sim_area}} tại 0.||Compression by 2 reduces the area to $1/|a|$ = {{sim_area}}, and the transform is also {{sim_area}} high at 0.⟧"),
        dict(q="⟦Đỉnh của phổ $\\cos2\\pi(4x)$ (cửa sổ Gauss $a=0.05$) tại $s=4$ cao bao nhiêu?||How high is the spectral peak of $\\cos2\\pi(4x)$ (Gaussian window $a=0.05$) at $s=4$?⟧",
             opts=["{{cos_h_4}}", "{{cos_h_2}}5", "2.5", "20"], explain="⟦Giãn cosinusoid chỉ dịch xung, không đổi cường độ: {{cos_h_2}} tại $s=2$ và {{cos_h_4}} tại $s=4$.||Expanding the cosinusoid only shifts the impulse, not its strength: {{cos_h_2}} at $s=2$ and {{cos_h_4}} at $s=4$.⟧"),
        dict(q="⟦$\\int(|a|^{1/2}f(ax))^2dx$ với $a=2$, $f=e^{-\\pi x^2}$ bằng bao nhiêu?||What is $\\int(|a|^{1/2}f(ax))^2dx$ for $a=2$, $f=e^{-\\pi x^2}$?⟧",
             opts=["{{sym_energy}}", "0.3536", "1.4142", "0.5"], explain="⟦Dạng đối xứng bảo toàn năng lượng: {{sym_energy}} $=\\int f^2$.||The symmetric form conserves energy: {{sym_energy}} $=\\int f^2$.⟧"),
        dict(q="⟦Biến đổi của $e^{-\\pi x^2}+2e^{-|x|}$ tại $s=0.3$ bằng bao nhiêu?||What is the transform of $e^{-\\pi x^2}+2e^{-|x|}$ at $s=0.3$?⟧",
             opts=["{{add_03}}", "1.2074", "0.7537", "0.8786"], explain="⟦$0.7537+2\\times0.4393$ = {{add_03}}: định lý cộng.||$0.7537+2\\times0.4393$ = {{add_03}}: the addition theorem.⟧"),
        dict(q="⟦Pha (độ) của biến đổi Gauss dịch $a=0.25$ tại $s=0.3$ bằng bao nhiêu?||What is the phase (degrees) of the transform of the Gaussian shifted by $a=0.25$ at $s=0.3$?⟧",
             opts=["{{shift_ph}}", "27", "-54", "-13.5"], explain="⟦$-2\\pi as$ = $-2\\pi(0.25)(0.3)$ rad = {{shift_ph}} độ; độ lớn giữ {{shift_mag}}.||$-2\\pi as$ = $-2\\pi(0.25)(0.3)$ rad = {{shift_ph}} degrees; the magnitude stays {{shift_mag}}.⟧"),
        dict(q="⟦Độ dốc của pha đã gỡ cuốn theo $s$ khi dịch $a=0.25$ bằng bao nhiêu (rad trên đơn vị $s$)?||What is the slope of the unwrapped phase against $s$ for a shift $a=0.25$ (rad per unit of $s$)?⟧",
             opts=["{{group_slope}}", "-0.25", "-6.2832", "1.5708"], explain="⟦Bằng $-2\\pi a$ = {{group_slope}}.||It equals $-2\\pi a$ = {{group_slope}}.⟧"),
        dict(q="⟦Dịch $\\tfrac14$ đơn vị làm pha của biến đổi thực tại $s=1$ bằng bao nhiêu độ?||Shifting by $\\tfrac14$ unit gives the phase of a real transform at $s=1$ equal to how many degrees?⟧",
             opts=["{{twist_1}}", "-45", "-180", "90"], explain="⟦Xoắn đều 90 độ trên mỗi đơn vị $s$: {{twist_1}} độ tại 1, {{twist_2}} độ tại 2.||A uniform twist of 90 degrees per unit of $s$: {{twist_1}} degrees at 1, {{twist_2}} degrees at 2.⟧"),
        dict(q="⟦Hệ số DFT của $\\cos(2\\pi f_0t-\\varphi)$ với $\\varphi=\\pi/2$ (chuẩn hóa) có phần thực và ảo là gì?||What are the real and imaginary parts of the (normalised) DFT coefficient of $\\cos(2\\pi f_0t-\\varphi)$ with $\\varphi=\\pi/2$?⟧",
             opts=["{{cos_re_90}}, {{cos_im_90}}", "1, 0", "0, 1", "-1, -1"], explain="⟦$e^{-i\\varphi}$ = $-i$: thực {{cos_re_90}}, ảo {{cos_im_90}}; tại $\\pi$ là {{cos_re_180}}, {{cos_im_180}}.||$e^{-i\\varphi}$ = $-i$: real {{cos_re_90}}, imaginary {{cos_im_90}}; at $\\pi$ it is {{cos_re_180}}, {{cos_im_180}}.⟧"),
        dict(q="⟦Đỉnh phổ của $f(x)\\cos2\\pi(3x)$ ($f$ Gauss) tại $s=3$ cao bao nhiêu?||How high is the spectral peak of $f(x)\\cos2\\pi(3x)$ ($f$ Gaussian) at $s=3$?⟧",
             opts=["{{mod_peak}}", "1", "0.25", "2"], explain="⟦$\\tfrac12F(0)$ = {{mod_peak}}: hai bản sao nửa cường độ.||$\\tfrac12F(0)$ = {{mod_peak}}: two half-strength replicas.⟧"),
        dict(q="⟦Phổ xung $\\Pi(x/10)\\cos2\\pi x$ tại $s=1$ bằng bao nhiêu?||What is the spectrum of the pulse $\\Pi(x/10)\\cos2\\pi x$ at $s=1$?⟧",
             opts=["{{pulse_peak}}", "10", "2.5", "3.2608"], explain="⟦$\\tfrac12X[1+\\text{sinc}(2Xf)]$ = {{pulse_peak}}; tại $s=1.05$ là {{pulse_off}}.||$\\tfrac12X[1+\\text{sinc}(2Xf)]$ = {{pulse_peak}}; at $s=1.05$ it is {{pulse_off}}.⟧"),
        dict(q="⟦Tỉ số dải bên trên sóng mang của xung điều biên với $M=0.6$ là bao nhiêu?||What is the sideband-to-carrier ratio of the AM pulse with $M=0.6$?⟧",
             opts=["{{am_ratio}}", "0.6", "0.15", "0.5"], explain="⟦$\\tfrac14MX/\\tfrac12X=M/2$ = {{am_ratio}}: sóng mang {{am_carrier}}, dải bên {{am_side}}.||$\\tfrac14MX/\\tfrac12X=M/2$ = {{am_ratio}}: carrier {{am_carrier}}, sideband {{am_side}}.⟧"),
        dict(q="⟦Phương sai của $e^{-x}H(x)*\\Pi$ bằng bao nhiêu?||What is the variance of $e^{-x}H(x)*\\Pi$?⟧",
             opts=["{{ch_var}}", "1.1667", "0.0833", "2"], explain="⟦Phương sai cộng: $1+1/12$ = {{ch_var}}; diện tích {{ch_area}}, trọng tâm {{ch_mean}}.||Variances add: $1+1/12$ = {{ch_var}}; area {{ch_area}}, centre of gravity {{ch_mean}}.⟧"),
        dict(q="⟦Bao nhiêu trong 9 dạng viết gọn của định lý tích chập được kiểm đúng bằng DFT?||How many of the 9 abbreviated forms of the convolution theorem are verified with the DFT?⟧",
             opts=["{{forms_ok}}", "5", "6", "10"], explain="⟦Cả {{forms_ok}} dạng đúng với dãy phức, so tổng trực tiếp với tích các DFT.||All {{forms_ok}} forms hold for complex sequences, comparing the direct sum with the product of DFTs.⟧"),
        dict(q="⟦$\\int|f|^2dx$ của $f=e^{-x}H(x)$ bằng bao nhiêu (và bằng $\\int|F|^2ds$)?||What is $\\int|f|^2dx$ of $f=e^{-x}H(x)$ (and equal to $\\int|F|^2ds$)?⟧",
             opts=["{{ray_exp}}", "1", "0.7071", "0.25"], explain="⟦$\\int e^{-2x}dx$ = {{ray_exp}}; vế phổ $\\int ds/(1+4\\pi^2s^2)$ cùng bằng {{ray_exp}}.||$\\int e^{-2x}dx$ = {{ray_exp}}; the spectral side $\\int ds/(1+4\\pi^2s^2)$ is also {{ray_exp}}.⟧"),
        dict(q="⟦$\\int f\\,g\\,dx$ với $f=e^{-\\pi(x+0.3)^2}$, $g=e^{-\\pi(x-1)^2}$ bằng bao nhiêu?||What is $\\int f\\,g\\,dx$ for $f=e^{-\\pi(x+0.3)^2}$, $g=e^{-\\pi(x-1)^2}$?⟧",
             opts=["{{pow_direct}}", "0.7071", "0.2079", "0.0351"], explain="⟦Định lý công suất: {{pow_direct}} bằng $\\int FG^*ds$ = {{pow_fourier}}.||The power theorem: {{pow_direct}} equals $\\int FG^*ds$ = {{pow_fourier}}.⟧"),
        dict(q="⟦Biến đổi của tự tương quan $\\Pi\\star\\Pi$ tại $s=0.3$ bằng bao nhiêu?||What is the transform of the autocorrelation $\\Pi\\star\\Pi$ at $s=0.3$?⟧",
             opts=["{{ac_pi_03}}", "0.8584", "0.5", "0.4053"], explain="⟦$|F|^2=\\text{sinc}^2(0.3)$ = {{ac_pi_03}}.||$|F|^2=\\text{sinc}^2(0.3)$ = {{ac_pi_03}}.⟧"),
        dict(q="⟦Với đoạn 10 s của $\\cos2\\pi(5t)$, tỉ lệ công suất tại $+5$ Hz là bao nhiêu?||For a 10 s segment of $\\cos2\\pi(5t)$, what fraction of the power lies at $+5$ Hz?⟧",
             opts=["{{cos_frac}}", "1", "0.25", "0.75"], explain="⟦Phổ công suất là $\\tfrac12\\delta(s\\pm5)$: mỗi bên {{cos_frac}}.||The power spectrum is $\\tfrac12\\delta(s\\pm5)$: {{cos_frac}} on each side.⟧"),
        dict(q="⟦Độ lớn biến đổi của $f'$ ($f=e^{-\\pi x^2}$) tại $s=0.3$ bằng bao nhiêu?||What is the magnitude of the transform of $f'$ ($f=e^{-\\pi x^2}$) at $s=0.3$?⟧",
             opts=["{{der_03}}", "0.7537", "1.8850", "0.4559"], explain="⟦$2\\pi s\\,e^{-\\pi s^2}$ = {{der_03}}.||$2\\pi s\\,e^{-\\pi s^2}$ = {{der_03}}.⟧"),
        dict(q="⟦Cực đại của $|(2\\pi s)^2e^{-\\pi s^2}|$ ($n=2$) nằm ở $s$ bằng bao nhiêu?||Where is the maximum of $|(2\\pi s)^2e^{-\\pi s^2}|$ ($n=2$)?⟧",
             opts=["{{pk2}}", "{{pk1}}", "{{pk3}}", "1"], explain="⟦$\\sqrt{n/2\\pi}$: {{pk1}}, {{pk2}}, {{pk3}} cho $n=1,2,3$.||$\\sqrt{n/2\\pi}$: {{pk1}}, {{pk2}}, {{pk3}} for $n=1,2,3$.⟧"),
        dict(q="⟦Lệch giữa biến đổi của đạo hàm bậc thang tắt dần và 1 ($\\varepsilon=10^{-3}$, $s=0.5$) là bao nhiêu?||What is the deviation between the transform of the derivative of the decaying step and 1 ($\\varepsilon=10^{-3}$, $s=0.5$)?⟧",
             opts=["{{step_dev}}", "1.0e-01", "0", "1.0e-06"], explain="⟦$\\varepsilon/|\\varepsilon+i2\\pi s|$ = {{step_dev}}, tiến về 0: đạo hàm của bậc thang là xung.||$\\varepsilon/|\\varepsilon+i2\\pi s|$ = {{step_dev}}, tending to 0: the derivative of the step is the impulse.⟧"),
        dict(q="⟦Lệch giữa $x*h$ và $x'*s$ (mạch RC, $s$ là đáp ứng bậc thang) bằng bao nhiêu?||What is the deviation between $x*h$ and $x'*s$ (RC circuit, $s$ the step response)?⟧",
             opts=["{{ds_diff}}", "1.0e-01", "1.0e-03", "0.5"], explain="⟦Đạo hàm của tích chập chuyển sang một thừa số: lệch chỉ {{ds_diff}}.||The derivative of a convolution moves onto one factor: the deviation is only {{ds_diff}}.⟧"),
        dict(q="⟦Biến đổi của hình thang $f=2\\Lambda(x/2)-\\Lambda(x)$ tại $s=0.3$ bằng bao nhiêu?||What is the transform of the trapezoid $f=2\\Lambda(x/2)-\\Lambda(x)$ at $s=0.3$?⟧",
             opts=["{{trap_03}}", "0.7368", "0.4053", "0.5236"], explain="⟦$\\text{sinc}^2s(1+2\\cos2\\pi s)$ = {{trap_03}}, tích phân số trùng.||$\\text{sinc}^2s(1+2\\cos2\\pi s)$ = {{trap_03}}, numerical integration agrees.⟧"),
        dict(q="⟦Theo Rayleigh, $\\int\\text{sinc}^4x\\,dx$ bằng bao nhiêu?||By Rayleigh, what is $\\int\\text{sinc}^4x\\,dx$?⟧",
             opts=["{{sinc4}}", "1", "0.5", "0.3333"], explain="⟦Bằng $\\int\\Lambda^2ds=\\tfrac23$ = {{sinc4}}.||It equals $\\int\\Lambda^2ds=\\tfrac23$ = {{sinc4}}.⟧"),
        dict(q="⟦Độ lớn biến đổi của $xe^{-\\pi x^2}$ tại $s=0.3$ bằng bao nhiêu?||What is the magnitude of the transform of $xe^{-\\pi x^2}$ at $s=0.3$?⟧",
             opts=["{{xg_03}}", "0.7537", "1.4207", "0.1130"], explain="⟦Định lý đạo hàm cho $-is\\,e^{-\\pi s^2}$: độ lớn {{xg_03}}.||The derivative theorem gives $-is\\,e^{-\\pi s^2}$: magnitude {{xg_03}}.⟧"),
        dict(q="⟦$\\int e^{-i2\\pi as}e^{-\\pi s^2}ds$ với $a=0.5$ bằng bao nhiêu?||What is $\\int e^{-i2\\pi as}e^{-\\pi s^2}ds$ for $a=0.5$?⟧",
             opts=["{{gf_05}}", "0.7071", "1", "0.2079"], explain="⟦Bằng $e^{-\\pi a^2}$ = {{gf_05}}: biến đổi của $\\delta(x-a)$ thử với $F$.||Equal to $e^{-\\pi a^2}$ = {{gf_05}}: the transform of $\\delta(x-a)$ tested against $F$.⟧"),
        dict(q="⟦Định lý tỉ lệ nói $f(ax)$ có biến đổi nào?||What transform does the similarity theorem give for $f(ax)$?⟧",
             opts=["$|a|^{-1}F(s/a)$", "$|a|\\,F(as)$ ⟦vì nén trục $x$ cũng nén trục $s$ và cao lên tương ứng||since compressing the $x$ axis also compresses the $s$ axis and raises it accordingly⟧",
                   "$F(s/a)$ ⟦vì đổi thang không đổi diện tích của biến đổi||since rescaling does not change the area of the transform⟧",
                   "$F(as)/|a|$ ⟦vì trục $s$ co lại cùng chiều với trục $x$||since the $s$ axis contracts in the same direction as the $x$ axis⟧"],
             explain="⟦Bracewell, tr. 108: $f(ax)\\supset|a|^{-1}F(s/a)$; nén một trục thì giãn trục kia.||Bracewell, p. 108: $f(ax)\\supset|a|^{-1}F(s/a)$; compressing one axis expands the other.⟧"),
        dict(q="⟦Định lý dịch nói gì về $f(x-a)$?||What does the shift theorem say about $f(x-a)$?⟧",
             opts=["⟦Nhân $F(s)$ với $e^{-i2\\pi as}$, chỉ đổi pha||Multiplies $F(s)$ by $e^{-i2\\pi as}$, changing only the phase⟧",
                   "⟦Dịch $F(s)$ đi $a$ đơn vị trên trục tần số mà không đổi pha||Shifts $F(s)$ by $a$ units along the frequency axis without changing the phase⟧",
                   "⟦Nhân $F(s)$ với $e^{-a s}$, làm suy giảm các thành phần tần số cao||Multiplies $F(s)$ by $e^{-as}$, attenuating the high-frequency components⟧",
                   "⟦Đổi biên độ tỉ lệ với $a$ nhưng giữ nguyên mọi pha của các thành phần||Changes the amplitudes in proportion to $a$ but leaves every phase of the components unchanged⟧"],
             explain="⟦Bracewell, tr. 111: $f(x-a)\\supset e^{-i2\\pi as}F(s)$; độ lớn giữ {{shift_mag}}.||Bracewell, p. 111: $f(x-a)\\supset e^{-i2\\pi as}F(s)$; the magnitude stays {{shift_mag}}.⟧"),
        dict(q="⟦Định lý điều chế nói $f(x)\\cos\\omega x$ có phổ nào?||What spectrum does the modulation theorem give for $f(x)\\cos\\omega x$?⟧",
             opts=["⟦Hai bản sao nửa cường độ của $F$ dịch $\\pm\\omega/2\\pi$||Two half-strength replicas of $F$ shifted by $\\pm\\omega/2\\pi$⟧",
                   "⟦Một bản sao $F$ duy nhất cường độ đầy đủ dịch tới $\\omega/2\\pi$ về phía tần số dương||A single full-strength copy of $F$ shifted to $\\omega/2\\pi$ on the positive-frequency side⟧",
                   "⟦Bản $F$ co lại $\\omega$ lần, vì nhân với cosin nén trục tần số||$F$ compressed by a factor $\\omega$, since multiplying by a cosine compresses the frequency axis⟧",
                   "⟦Tích của $F$ với $\\cos\\omega s$, cũng là một nhân trong miền tần số||The product of $F$ with $\\cos\\omega s$, also a multiplication in the frequency domain⟧"],
             explain="⟦Bracewell, tr. 113 đến 115: $\\tfrac12F(s-\\omega/2\\pi)+\\tfrac12F(s+\\omega/2\\pi)$; đỉnh {{mod_peak}} trong ví dụ Gauss.||Bracewell, pp. 113 to 115: $\\tfrac12F(s-\\omega/2\\pi)+\\tfrac12F(s+\\omega/2\\pi)$; peak {{mod_peak}} in the Gaussian example.⟧"),
        dict(q="⟦Vì sao độ võng cầu khi tàu chạy không thể viết bằng tích chập?||Why can the bridge deflection as the train moves not be written as a convolution?⟧",
             opts=["⟦Dạng độ võng không chuyển dịch nguyên vẹn theo tàu||The deflection pattern does not move on with the train unchanged⟧",
                   "⟦Vì cầu là hệ phi tuyến nên độ võng không tỉ lệ với tải dù ở ứng suất nhỏ||Because the bridge is a nonlinear system so the deflection is not proportional to the load even at small stress⟧",
                   "⟦Vì tải của tàu không khả tích tuyệt đối nên tích chập không tồn tại||Because the train's load is not absolutely integrable so the convolution does not exist⟧",
                   "⟦Vì tích chập chỉ dùng cho tín hiệu theo thời gian, không dùng được theo không gian||Because convolution applies only to signals in time, not in space⟧"],
             explain="⟦Bracewell, tr. 115: độ võng vẫn là phiếm hàm tuyến tính của tải, nhưng không bất biến khi dịch, nên không phải tích chập.||Bracewell, p. 115: the deflection is still a linear functional of the load but not shift-invariant, so it is not a convolution.⟧"),
        dict(q="⟦Ba phép kiểm hay dùng cho tích chập gồm những gì?||What are the three checks often used for convolution?⟧",
             opts=["⟦Diện tích nhân nhau, trọng tâm cộng, phương sai cộng||Areas multiply, centres of gravity add, variances add⟧",
                   "⟦Diện tích cộng nhau, trọng tâm nhân nhau, phương sai nhân nhau khi cả hai bằng nhau||Areas add, centres of gravity multiply, variances multiply when the two are equal⟧",
                   "⟦Diện tích bằng nhau, trọng tâm bằng 0, phương sai bằng 1 với mọi hàm chuẩn hóa||Areas are equal, centres of gravity are 0, variances are 1 for every normalised function⟧",
                   "⟦Chiều cao cộng, độ rộng nhân, diện tích giữ nguyên như hàm ban đầu||Heights add, widths multiply, area stays as in the original function⟧"],
             explain="⟦Bracewell, tr. 118: diện tích nhân, hoành độ trọng tâm cộng, mômen bậc hai (phương sai) cộng; đo được {{ch_area}}, {{ch_mean}}, {{ch_var}}.||Bracewell, p. 118: areas multiply, centres of gravity add, second moments (variances) add; measured {{ch_area}}, {{ch_mean}}, {{ch_var}}.⟧"),
        dict(q="⟦Định lý Rayleigh tương ứng với định lý nào của chuỗi Fourier?||Which theorem of Fourier series does Rayleigh's theorem correspond to?⟧",
             opts=["⟦Parseval||Parseval's⟧",
                   "⟦Dirichlet, vì cả hai nói về hội tụ tại điểm gián đoạn||Dirichlet's, because both concern convergence at a point of discontinuity⟧",
                   "⟦Fejér, vì cả hai dùng trung bình Cesàro của các tổng riêng||Fejér's, because both use Cesàro means of partial sums⟧",
                   "⟦Gibbs, vì cả hai mô tả độ tràn quá ở lân cận bước nhảy||Gibbs's, because both describe the overshoot near a jump⟧"],
             explain="⟦Bracewell, tr. 119: Rayleigh (1889) tương ứng định lý Parseval của chuỗi Fourier.||Bracewell, p. 119: Rayleigh (1889) corresponds to Parseval's theorem for Fourier series.⟧"),
        dict(q="⟦Tự tương quan của một hàm có biến đổi nào, và nó mất thông tin gì?||What transform does the autocorrelation of a function have, and what information does it lose?⟧",
             opts=["$|F(s)|^2$, ⟦mất pha||it loses the phase⟧",
                   "$F(s)^2$ ⟦đủ cả pha, vì bình phương phức giữ nguyên góc||with full phase, since squaring a complex number keeps the angle⟧",
                   "$|F(s)|$ ⟦mất giá trị tại tần số 0 nhưng giữ mọi pha||losing the value at zero frequency but keeping every phase⟧",
                   "$F(s)F(-s)$ ⟦mất phần thực nhưng giữ phần ảo của biến đổi||losing the real part but keeping the imaginary part of the transform⟧"],
             explain="⟦Bracewell, tr. 122: $f\\star f\\supset|F|^2$; thông tin về pha hoàn toàn vắng mặt.||Bracewell, p. 122: $f\\star f\\supset|F|^2$; information about the phase is entirely missing.⟧"),
        dict(q="⟦Định lý đạo hàm nói $f'$ có biến đổi nào, và điều đó làm gì với tần số?||What transform does the derivative theorem give for $f'$, and what does it do to frequencies?⟧",
             opts=["$i2\\pi sF(s)$, ⟦tăng cường tần số cao và triệt tiêu tần số 0||enhancing high frequencies and suppressing zero frequency⟧",
                   "$F(s)/i2\\pi s$ ⟦làm yếu tần số cao và tăng cường thành phần một chiều||attenuating high frequencies and enhancing the DC component⟧",
                   "$sF(s)$ ⟦làm phổ rộng ra và giữ nguyên pha của mọi thành phần||broadening the spectrum and leaving the phase of every component unchanged⟧",
                   "$F'(s)$ ⟦đạo hàm phổ, làm dịch các vạch phổ lên tần số cao hơn||the derivative of the spectrum, shifting spectral lines to higher frequency⟧"],
             explain="⟦Bracewell, tr. 124 đến 125: $f'\\supset i2\\pi sF$; cực đại của $(2\\pi s)^ne^{-\\pi s^2}$ dịch lên: {{pk1}}, {{pk2}}, {{pk3}}.||Bracewell, pp. 124 to 125: $f'\\supset i2\\pi sF$; the maximum of $(2\\pi s)^ne^{-\\pi s^2}$ moves up: {{pk1}}, {{pk2}}, {{pk3}}.⟧"),
        dict(q="⟦Đạo hàm của tích chập $(f*g)'$ bằng gì?||What does the derivative of a convolution $(f*g)'$ equal?⟧",
             opts=["$f'*g=f*g'$", "$f'*g'$ ⟦vì đạo hàm áp dụng cho cả hai thừa số như quy tắc tích||because differentiation applies to both factors like the product rule⟧",
                   "$f'\\,g+f\\,g'$ ⟦quy tắc Leibniz của phép nhân từng điểm||the Leibniz rule for pointwise multiplication⟧",
                   "$(f*g)*\\delta$ ⟦vì đạo hàm của tích chập là tích chập với xung||because the derivative of a convolution is the convolution with an impulse⟧"],
             explain="⟦Bracewell, tr. 126: đạo hàm của tích chập là tích chập của một hàm với đạo hàm của hàm kia; số đo {{ds_diff}}.||Bracewell, p. 126: the derivative of a convolution is the convolution of either with the derivative of the other; measured {{ds_diff}}.⟧"),
        dict(q="⟦Vì sao không định nghĩa tích của hai hàm suy rộng?||Why is no product of two generalized functions defined?⟧",
             opts=["⟦Tích hai dãy xác định không nhất thiết chính quy||The product of two defining sequences is not necessarily regular⟧",
                   "⟦Vì tích của hai xung luôn bằng 0 nên không có gì để định nghĩa||Because the product of two impulses is always zero so there is nothing to define⟧",
                   "⟦Vì biến đổi Fourier của tích hai hàm suy rộng phân kỳ ở mọi tần số||Because the Fourier transform of a product of two generalized functions diverges at every frequency⟧",
                   "⟦Vì hàm suy rộng chỉ có nghĩa khi đứng trong tích phân với đúng một hàm thử||Because a generalized function only has meaning inside an integral with exactly one test function⟧"],
             explain="⟦Bracewell, tr. 128: không có gì được gọi là tích của hai hàm suy rộng; ví dụ $[\\delta(x)]^2$ không có nghĩa.||Bracewell, p. 128: nothing could be called the product of two generalized functions; for example $[\\delta(x)]^2$ has no meaning.⟧"),
        dict(q="⟦Vì sao biến đổi của $\\int_{-\\infty}^xf$ không chỉ là $F(s)/(i2\\pi s)$?||Why is the transform of $\\int_{-\\infty}^xf$ not just $F(s)/(i2\\pi s)$?⟧",
             opts=["⟦Thiếu số hạng một chiều $\\tfrac12F(0)\\delta(s)$||The DC term $\\tfrac12F(0)\\delta(s)$ is missing⟧",
                   "⟦Vì phép chia cho $i2\\pi s$ chỉ đúng khi $F(0)=0$ và trong mọi trường hợp khác biến đổi không tồn tại||Because division by $i2\\pi s$ is only valid when $F(0)=0$ and otherwise the transform does not exist⟧",
                   "⟦Vì tích phân bất định luôn có hằng số tích phân bằng $F(0)$ làm biến đổi thêm một xung||Because an indefinite integral always carries an integration constant equal to $F(0)$, adding an impulse to the transform⟧",
                   "⟦Vì định lý đạo hàm chỉ áp dụng cho hàm có đạo hàm liên tục ở mọi điểm||Because the derivative theorem applies only to functions whose derivative is continuous at every point⟧"],
             explain="⟦Bài tập 19 và 20 (tr. 133): lập luận đạo hàm chỉ xác định phần không phải một chiều; số đo lệch {{int_thm_diff}} khi kiểm $H*f-H$.||Problems 19 and 20 (p. 133): the derivative argument fixes only the non-DC part; the measured deviation is {{int_thm_diff}} when checking $H*f-H$.⟧"),
    ],
    nb=[
        ("md", """## 1. ⟦Sáu cặp chuẩn và tương hỗ||Six standard pairs and reciprocity⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Ba cặp đầu có đúng, tích phân sinc thật sự nhảy quanh $|s|=\\tfrac12$, và các cặp trong giới hạn ($1$, $\\cos\\pi x$) hình thành ra sao từ Gauss? Ta so tích phân dao động với công thức qua hàm $\\text{Si}$, và tích phân số với công thức đóng.||Are the first three pairs correct, does the sinc integral really jump around $|s|=\\tfrac12$, and how do the pairs in the limit ($1$, $\\cos\\pi x$) arise from the Gaussian? We compare the oscillatory integral with the formula through $\\text{Si}$, and numerical integrals with closed forms.⟧"""),
        ("code", r'''from scipy import integrate, special, signal
trap = getattr(np, "trapezoid", None) or np.trapz

def ft_support(f, a, b, s, pts=None):
    re = integrate.quad(lambda x: f(x)*np.cos(2*np.pi*x*s), a, b, points=pts, limit=400)[0]
    im = integrate.quad(lambda x: -f(x)*np.sin(2*np.pi*x*s), a, b, points=pts, limit=400)[0]
    return re + 1j*im
g = lambda x: np.exp(-np.pi*x**2)
s3 = 0.3
pg = ft_support(g, -10, 10, s3).real
psinc = ft_support(lambda x: 1.0, -0.5, 0.5, s3).real                       # ⟦sinc s = ∫Π e^{−i2πxs}||sinc s = ∫Π e^{−i2πxs}⟧
psinc2 = ft_support(lambda x: 1 - abs(x), -1, 1, s3, [0]).real
assert abs(pg - np.exp(-np.pi*s3**2)) < 1e-8 and abs(psinc - np.sinc(s3)) < 1e-9 and abs(psinc2 - np.sinc(s3)**2) < 1e-9
report("p_g", pg, ".4f"); report("p_sinc", psinc, ".4f"); report("p_sinc2", psinc2, ".4f")

# ⟦∫_{−X}^{X} sinc x e^{−i2πxs} dx: cách A tích phân dao động; cách B công thức Si||∫_{−X}^{X} sinc x e^{−i2πxs} dx: method A oscillatory integral; method B the Si formula⟧
X = 200
def sinc_int(s):
    return 2*integrate.quad(np.sinc, 0, X, weight="cos", wvar=2*np.pi*s, limit=4000)[0]
def sinc_si(s):
    return (special.sici(np.pi*X*(1 + 2*s))[0] + special.sici(np.pi*X*(1 - 2*s))[0])/np.pi
for s, key in ((0.3, "re_03"), (0.7, "re_07"), (0.5, "re_05")):
    assert abs(sinc_int(s) - sinc_si(s)) < 1e-6
    report(key, sinc_si(s), ".4f")

# ⟦Dãy Gauss: đỉnh 1/a, và cửa sổ Gauss của cos(πx)||Gaussian sequence: peak 1/a, and the Gaussian-windowed cos(πx)⟧
for a_, key in ((0.1, "gs_10"), (0.05, "gs_20")):
    v = ft_support(lambda x: np.exp(-np.pi*a_**2*x**2), -60/a_*0.2, 60/a_*0.2, 0.0).real
    assert abs(v - 1/a_) < 1e-6
    report(key, v, ".0f")
aw = 0.05
Fc = lambda s: 0.5/aw*(np.exp(-np.pi*(s - 0.5)**2/aw**2) + np.exp(-np.pi*(s + 0.5)**2/aw**2))
peak_num = ft_support(lambda x: np.exp(-np.pi*aw**2*x**2)*np.cos(np.pi*x), -60, 60, 0.5, None).real
assert abs(peak_num - Fc(0.5)) < 1e-6
area_num = integrate.quad(Fc, 0, 1)[0]
assert abs(area_num - 0.5) < 1e-9
report("cos_peak", peak_num, ".2f"); report("cos_area", area_num, ".2f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Tại $s=0.3$: Gauss {{p_g}}, sinc {{p_sinc}}, sinc$^2$ {{p_sinc2}}. Tích phân của sinc cắt ở $|x|\\le200$ là {{re_03}} tại 0.3, {{re_07}} tại 0.7 và {{re_05}} tại 0.5, đúng trung bình. Đỉnh của dãy Gauss là {{gs_10}} và {{gs_20}} khi $a=0.1$ và $0.05$, tức $1/a$. Cửa sổ Gauss của $\\cos\\pi x$ cho đỉnh {{cos_peak}} và diện tích {{cos_area}}, tiến về $\\tfrac12\\delta(s-\\tfrac12)$.||At $s=0.3$: Gaussian {{p_g}}, sinc {{p_sinc}}, sinc$^2$ {{p_sinc2}}. The sinc integral cut at $|x|\\le200$ is {{re_03}} at 0.3, {{re_07}} at 0.7 and {{re_05}} at 0.5, exactly the mean. The Gaussian sequence's peak is {{gs_10}} and {{gs_20}} for $a=0.1$ and $0.05$, i.e. $1/a$. The Gaussian-windowed $\\cos\\pi x$ gives peak {{cos_peak}} and area {{cos_area}}, tending to $\\tfrac12\\delta(s-\\tfrac12)$.⟧"""),
        ("md", """## 2. ⟦Tỉ lệ, cộng và dịch||Similarity, addition and shift⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Định lý tỉ lệ giữ diện tích và năng lượng ra sao, cosinusoid giãn ra dịch xung thế nào, dịch có chỉ đổi pha tuyến tính, và cosin trượt đi từ thực sang ảo như thế nào? Mỗi điều được kiểm bằng tích phân số so với công thức, và bằng DFT.||How does the similarity theorem conserve area and energy, how does an expanded cosinusoid shift its impulses, does a shift only change the phase linearly, and how does a sliding cosine move from real to imaginary? Each is checked by numerical integration against the formula, and by the DFT.⟧"""),
        ("code", r'''# ⟦Tỉ lệ: f(ax), a = 2||Similarity: f(ax), a = 2⟧
a2 = 2.0
sim03 = ft_support(lambda x: g(a2*x), -10, 10, 0.3).real
assert abs(sim03 - 0.5*np.exp(-np.pi*(0.3/a2)**2)) < 1e-9
sim_area = integrate.quad(lambda x: g(a2*x), -10, 10)[0]
assert abs(sim_area - 0.5) < 1e-9
report("sim_03", sim03, ".4f"); report("sim_area", sim_area, ".2f")
en_f = integrate.quad(lambda x: g(x)**2, -10, 10)[0]
en_sym = integrate.quad(lambda x: (np.sqrt(a2)*g(a2*x))**2, -10, 10)[0]
assert abs(en_f - en_sym) < 1e-9 and abs(en_f - 1/np.sqrt(2)) < 1e-9
report("sym_energy", en_f, ".4f")

# ⟦Cosinusoid giãn ra: cửa sổ Gauss a = 0.05, tần số 2 và 4||Expanded cosinusoid: Gaussian window a = 0.05, frequencies 2 and 4⟧
for f0, key in ((2, "cos_h_2"), (4, "cos_h_4")):
    num_ = ft_support(lambda x: np.exp(-np.pi*aw**2*x**2)*np.cos(2*np.pi*f0*x), -60, 60, f0).real
    assert abs(num_ - 0.5/aw) < 1e-6
    report(key, num_, ".0f")

# ⟦Cộng: FT(g + 2e^{−|x|}) = G + 2E||Addition: FT(g + 2e^{−|x|}) = G + 2E⟧
e_abs = lambda x: np.exp(-abs(x))
add_num = ft_support(lambda x: g(x) + 2*e_abs(x), -40, 40, 0.3, [0]).real
add_sum = ft_support(g, -10, 10, 0.3).real + 2*ft_support(e_abs, -40, 40, 0.3, [0]).real
assert abs(add_num - add_sum) < 1e-8
report("add_03", add_num, ".4f")

# ⟦Dịch a = 0.25: độ lớn và pha||Shift a = 0.25: magnitude and phase⟧
a_sh = 0.25
Fsh = ft_support(lambda x: g(x - a_sh), -10, 10, 0.3)
assert abs(Fsh - np.exp(-2j*np.pi*a_sh*0.3)*np.exp(-np.pi*0.09)) < 1e-9
report("shift_mag", abs(Fsh), ".4f"); report("shift_ph", np.degrees(np.angle(Fsh)), ".1f")
ss = np.linspace(0, 1, 21)
Fs_ = np.array([ft_support(lambda x: g(x - a_sh), -10, 10, s) for s in ss])
slope = np.polyfit(ss, np.unwrap(np.angle(Fs_)), 1)[0]
assert abs(slope + 2*np.pi*a_sh) < 1e-8
report("group_slope", slope, ".4f")
Ft1 = ft_support(lambda x: g(x - 0.25), -10, 10, 1.0); Ft2 = ft_support(lambda x: g(x - 0.25), -10, 10, 2.0)
report("twist_1", np.degrees(np.angle(Ft1)), ".0f"); report("twist_2", np.degrees(np.angle(Ft2)), ".0f")

# ⟦Cosin trượt bằng DFT||A sliding cosine by DFT⟧
N = 1000; tq = np.arange(N)/N
for phi, tag in ((0.1, "01"), (np.pi/2, "90"), (np.pi, "180")):
    Xc = np.fft.fft(np.cos(2*np.pi*10*tq - phi))[10]/(N/2)
    assert abs(Xc - np.exp(-1j*phi)) < 1e-9
    report(f"cos_re_{tag}", abs(Xc.real) if abs(Xc.real) < 1e-9 else Xc.real, ".4f")
    report(f"cos_im_{tag}", abs(Xc.imag) if abs(Xc.imag) < 1e-9 else Xc.imag, ".4f")'''),
        ("code", r'''fig, ax = plt.subplots(1, 2, figsize=(10, 3.2))
xg_ = np.linspace(-3, 3, 600); sg = np.linspace(-3, 3, 600)
for a_, c in ((1, "tab:blue"), (2, "tab:orange"), (4, "tab:red")):
    ax[0].plot(xg_, g(a_*xg_), color=c, label=f"a = {a_}")
    ax[1].plot(sg, np.exp(-np.pi*(sg/a_)**2)/a_, color=c, label=f"a = {a_}")
ax[0].set_title("f(ax)"); ax[1].set_title("|a|⁻¹F(s/a)"); ax[0].legend(); ax[1].legend()
for a_ in ax: a_.set_xlabel("x / s")
plt.tight_layout(); plt.show()''', dict(fig="similarity", cap="⟦Hình 1. Định lý tỉ lệ với Gauss: khi a tăng, f(ax) hẹp lại (trái) còn biến đổi (phải) rộng ra và thấp xuống đúng 1/a, nên diện tích bên dưới giữ nguyên.||Figure 1. The similarity theorem with the Gaussian: as a increases f(ax) narrows (left) while the transform (right) widens and drops by exactly 1/a, so the area beneath is conserved.⟧")),
        ("code", r'''sq = np.linspace(0, 2, 401)
Fq = np.array([ft_support(lambda x: g(x - a_sh), -10, 10, s) for s in sq])
fig, ax = plt.subplots(1, 2, figsize=(9, 3.2))
ax[0].plot(sq, np.abs(Fq)); ax[0].set_title("|F(s)|")
ax[1].plot(sq, np.unwrap(np.angle(Fq))); ax[1].set_title(("⟦pha (rad)||phase (rad)⟧"))
for a_ in ax: a_.set_xlabel("s")
plt.tight_layout(); plt.show()''', dict(fig="shift_phase", cap="⟦Hình 2. Dịch Gauss đi 0.25: độ lớn |F| (trái) giữ nguyên hình Gauss, còn pha (phải) là đường thẳng dốc −2πa = −π/2 theo s.||Figure 2. Shifting the Gaussian by 0.25: the magnitude |F| (left) keeps its Gaussian shape, while the phase (right) is a straight line of slope −2πa = −π/2 in s.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Với $a=2$: diện tích {{sim_area}}, biến đổi tại 0.3 là {{sim_03}}, năng lượng đối xứng {{sym_energy}}. Đỉnh của cosinusoid giãn là {{cos_h_2}} và {{cos_h_4}} (không đổi). Cộng cho {{add_03}}. Dịch 0.25: độ lớn {{shift_mag}}, pha {{shift_ph}} độ, độ dốc pha {{group_slope}}, pha tại $s=1,2$ là {{twist_1}} và {{twist_2}} độ. Cosin trượt: (thực, ảo) = ({{cos_re_01}}, {{cos_im_01}}), ({{cos_re_90}}, {{cos_im_90}}), ({{cos_re_180}}, {{cos_im_180}}) khi lệch $0.1$, $\\pi/2$, $\\pi$.||With $a=2$: area {{sim_area}}, the transform at 0.3 is {{sim_03}}, symmetric energy {{sym_energy}}. The peaks of the expanded cosinusoid are {{cos_h_2}} and {{cos_h_4}} (unchanged). Addition gives {{add_03}}. Shift 0.25: magnitude {{shift_mag}}, phase {{shift_ph}} degrees, phase slope {{group_slope}}, phases at $s=1,2$ are {{twist_1}} and {{twist_2}} degrees. The sliding cosine: (real, imaginary) = ({{cos_re_01}}, {{cos_im_01}}), ({{cos_re_90}}, {{cos_im_90}}), ({{cos_re_180}}, {{cos_im_180}}) for shifts $0.1$, $\\pi/2$, $\\pi$.⟧"""),
        ("md", """## 3. ⟦Điều chế và tích chập||Modulation and convolution⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Phổ của một sóng điều biên có đúng hai bản sao nửa cường độ, xung cao tần có phổ hai sinc, các phép kiểm tích chập (diện tích, trọng tâm, phương sai) và chín dạng của định lý tích chập có đúng? Mỗi điều kiểm bằng hai cách.||Does the spectrum of an AM wave really have two half-strength replicas, does an RF pulse have a two-sinc spectrum, and do the convolution checks (area, centre of gravity, variance) and the nine forms of the theorem hold? Each is checked two ways.⟧"""),
        ("code", r'''# ⟦Điều chế: đường bao Gauss, sóng mang f0 = 3||Modulation: Gaussian envelope, carrier f0 = 3⟧
mod_peak = ft_support(lambda x: g(x)*np.cos(2*np.pi*3*x), -10, 10, 3.0).real
assert abs(mod_peak - 0.5*(1 + np.exp(-np.pi*36))) < 1e-8
report("mod_peak", mod_peak, ".2f")

# ⟦Xung cao tần Π(x/X)cos(2πfx), X = 10, f = 1||RF pulse Π(x/X)cos(2πfx), X = 10, f = 1⟧
Xp, fp = 10.0, 1.0
def pulse_ft(s): return ft_support(lambda x: np.cos(2*np.pi*fp*x), -Xp/2, Xp/2, s).real
pulse_formula = lambda s: 0.5*Xp*(np.sinc(Xp*(s + fp)) + np.sinc(Xp*(s - fp)))
for s in (1.0, 1.05):
    assert abs(pulse_ft(s) - pulse_formula(s)) < 1e-8
report("pulse_peak", pulse_formula(1.0), ".2f"); report("pulse_off", pulse_formula(1.05), ".4f")

# ⟦Xung điều biên: X = 200, f = 50, F = 5, M = 0.6||AM pulse: X = 200, f = 50, F = 5, M = 0.6⟧
Xa, fa, Fa, Ma = 200.0, 50.0, 5.0, 0.6
xa = np.arange(-Xa/2, Xa/2, 0.001)
env = (1 + Ma*np.cos(2*np.pi*Fa*xa))*np.cos(2*np.pi*fa*xa)
def am(s): return trap(env*np.cos(2*np.pi*xa*s), xa)
carrier, side = am(fa), am(fa + Fa)
assert abs(carrier - 0.5*Xa) < 0.5 and abs(side - 0.25*Ma*Xa) < 0.5
report("am_carrier", carrier, ".0f"); report("am_side", side, ".0f"); report("am_ratio", side/carrier, ".2f")

# ⟦Các phép kiểm: f = e^{−x}H(x) * Π trên lưới||Checks: f = e^{−x}H(x) * Π on a grid⟧
dxc = 0.002; xf = np.arange(0, 40, dxc)
conv = np.convolve(np.exp(-xf), np.ones(500))*dxc
xc = (np.arange(len(conv)) - 250)*dxc + dxc/2
area = trap(conv, xc); mean = trap(xc*conv, xc)/area; var = trap((xc - mean)**2*conv, xc)/area
assert abs(area - 1) < 5e-3 and abs(mean - 1) < 5e-3 and abs(var - (1 + 1/12)) < 5e-3
report("ch_area", area, ".2f"); report("ch_mean", mean, ".2f"); report("ch_var", var, ".4f")

# ⟦Chín dạng của định lý tích chập, DFT vòng, dãy phức độ dài 64||Nine forms of the convolution theorem, circular DFT, complex sequences of length 64⟧
rg = np.random.default_rng(6); Nn = 64; rv = (-np.arange(Nn)) % Nn
fz, gz = rg.standard_normal(Nn) + 1j*rg.standard_normal(Nn), rg.standard_normal(Nn) + 1j*rg.standard_normal(Nn)
def cconv(u, v): return np.array([np.sum(u*v[(k - np.arange(Nn)) % Nn]) for k in range(Nn)])
R = lambda z: z[rv]; Cj = np.conj
Fz, Gz = np.fft.fft(fz), np.fft.fft(gz)
forms = [(cconv(fz, gz), Fz*Gz), (cconv(fz, R(gz)), Fz*R(Gz)), (cconv(R(fz), R(gz)), R(Fz)*R(Gz)),
         (cconv(fz, Cj(R(gz))), Fz*Cj(Gz)), (cconv(fz, Cj(gz)), Fz*Cj(R(Gz))), (cconv(R(fz), Cj(R(gz))), R(Fz)*Cj(Gz)),
         (cconv(R(fz), Cj(gz)), R(Fz)*Cj(R(Gz))), (cconv(Cj(R(fz)), Cj(R(gz))), Cj(Fz)*Cj(Gz)), (cconv(Cj(R(fz)), Cj(gz)), Cj(Fz)*Cj(R(Gz)))]
ok = sum(bool(np.allclose(np.fft.fft(l_), r_)) for l_, r_ in forms)
assert ok == 9
report("forms_ok", ok, "d")
th = np.max(np.abs(np.fft.ifft(Fz*Gz) - cconv(fz, gz)))
assert th < 1e-9
report("conv_th_diff", th, ".1e")'''),
        ("code", r'''xm = np.linspace(-1.2, 1.2, 1200)
env_g = g(xm)
fig, ax = plt.subplots(1, 2, figsize=(10, 3.2))
ax[0].plot(xm, env_g, "k--", lw=0.8); ax[0].plot(xm, env_g*np.cos(2*np.pi*3*xm), color="tab:red")
ax[0].set_title(("⟦đường bao × sóng mang||envelope × carrier⟧")); ax[0].set_xlabel("x")
ss2 = np.linspace(-6, 6, 1200)
ax[1].plot(ss2, np.exp(-np.pi*ss2**2), "k--", lw=0.8, label=("⟦phổ đường bao||envelope spectrum⟧"))
ax[1].plot(ss2, 0.5*np.exp(-np.pi*(ss2 - 3)**2) + 0.5*np.exp(-np.pi*(ss2 + 3)**2), color="tab:red", label=("⟦phổ điều chế||modulated spectrum⟧"))
ax[1].legend(fontsize=8); ax[1].set_xlabel("s")
plt.tight_layout(); plt.show()''', dict(fig="modulation", cap="⟦Hình 3. Điều chế bằng cosin: phổ của đường bao Gauss (nét đứt) tách thành hai bản sao nửa cường độ ở ±3 (đỏ).||Figure 3. Modulation by a cosine: the spectrum of the Gaussian envelope (dashed) splits into two half-strength replicas at ±3 (red).⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Đỉnh phổ điều chế {{mod_peak}}. Xung cao tần: {{pulse_peak}} tại $s=1$ và {{pulse_off}} tại $s=1.05$. Xung điều biên: sóng mang {{am_carrier}}, dải bên {{am_side}}, tỉ số {{am_ratio}}. Tích chập $e^{-x}H*\\Pi$: diện tích {{ch_area}}, trọng tâm {{ch_mean}}, phương sai {{ch_var}}. {{forms_ok}} trên 9 dạng của định lý tích chập đúng, và tích chập vòng bằng IFFT của tích DFT (lệch {{conv_th_diff}}).||The modulated spectrum has peak {{mod_peak}}. The RF pulse: {{pulse_peak}} at $s=1$ and {{pulse_off}} at $s=1.05$. The AM pulse: carrier {{am_carrier}}, sideband {{am_side}}, ratio {{am_ratio}}. The convolution $e^{-x}H*\\Pi$: area {{ch_area}}, centre of gravity {{ch_mean}}, variance {{ch_var}}. {{forms_ok}} of the 9 forms of the convolution theorem hold, and the circular convolution equals the IFFT of the DFT product (deviation {{conv_th_diff}}).⟧"""),
        ("md", """## 4. ⟦Rayleigh, công suất và tự tương quan||Rayleigh, power and autocorrelation⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Năng lượng tính theo $x$ và theo $s$ có bằng nhau (Rayleigh), tích hai hàm khác nhau có bảo toàn (công suất), và tự tương quan có là biến đổi ngược của $|F|^2$? Tính mỗi số bằng tích phân theo hai miền.||Are energies computed in $x$ and in $s$ equal (Rayleigh), is the product of two different functions conserved (power), and is the autocorrelation the inverse transform of $|F|^2$? Each number is computed by integrating in the two domains.⟧"""),
        ("code", r'''# ⟦Rayleigh: Gauss và e^{−x}H(x)||Rayleigh: the Gaussian and e^{−x}H(x)⟧
Ex = integrate.quad(lambda x: g(x)**2, -10, 10)[0]; Es = integrate.quad(lambda s: np.exp(-2*np.pi*s**2), -10, 10)[0]
assert abs(Ex - Es) < 1e-9 and abs(Ex - 1/np.sqrt(2)) < 1e-9
report("ray_gauss", Ex, ".4f")
Ee = integrate.quad(lambda x: np.exp(-2*x), 0, np.inf)[0]; Ese = integrate.quad(lambda s: 1/(1 + 4*np.pi**2*s**2), -np.inf, np.inf)[0]
assert abs(Ee - 0.5) < 1e-9 and abs(Ese - 0.5) < 1e-7
report("ray_exp", Ee, ".2f")

# ⟦Công suất: f = e^{−π(x+0.3)²}, g = e^{−π(x−1)²}. F, G phức||Power: f = e^{−π(x+0.3)²}, g = e^{−π(x−1)²}. F, G complex⟧
f1 = lambda x: np.exp(-np.pi*(x + 0.3)**2); g1 = lambda x: np.exp(-np.pi*(x - 1)**2)
direct = integrate.quad(lambda x: f1(x)*g1(x), -10, 10)[0]
Ff = lambda s: np.exp(2j*np.pi*0.3*s)*np.exp(-np.pi*s**2); Gf = lambda s: np.exp(-2j*np.pi*1.0*s)*np.exp(-np.pi*s**2)
fourier_re = integrate.quad(lambda s: (Ff(s)*np.conj(Gf(s))).real, -10, 10)[0]
fourier_im = integrate.quad(lambda s: (Ff(s)*np.conj(Gf(s))).imag, -10, 10)[0]
pre = integrate.quad(lambda s: Ff(s).real*Gf(s).real, -10, 10)[0]; pim = integrate.quad(lambda s: Ff(s).imag*Gf(s).imag, -10, 10)[0]
assert abs(direct - fourier_re) < 1e-9 and abs(fourier_im) < 1e-9 and abs(pre + pim - direct) < 1e-9
alt = integrate.quad(lambda s: (Ff(s)*Gf(s)).real, -10, 10)[0]
alt_direct = integrate.quad(lambda x: f1(x)*g1(-x), -10, 10)[0]
assert abs(alt - alt_direct) < 1e-9
report("pow_direct", direct, ".4f"); report("pow_fourier", fourier_re, ".4f"); report("pow_re", pre, ".4f"); report("pow_im", pim, ".4f")

# ⟦Tự tương quan của Π là Λ; biến đổi tại s = 0.3 = |sinc|². Chuẩn hóa Gauss||Autocorrelation of Π is Λ; its transform at s = 0.3 = |sinc|². Gaussian normalisation⟧
ac_pi = ft_support(lambda x: max(1 - abs(x), 0), -1, 1, 0.3, [0]).real
assert abs(ac_pi - np.sinc(0.3)**2) < 1e-9
report("ac_pi_03", ac_pi, ".4f")
ns = integrate.quad(lambda s: np.sqrt(2)*np.exp(-2*np.pi*s**2), -10, 10)[0]
assert abs(ns - 1) < 1e-9 and abs(ft_support(lambda x: np.exp(-np.pi*x**2/2), -20, 20, 0.3).real - np.sqrt(2)*np.exp(-2*np.pi*0.09)) < 1e-9
report("ns_int", ns, ".2f")

# ⟦Phổ công suất chuẩn hóa của cos(2π·5t) trên 10 s||Normalised power spectrum of cos(2π·5t) over 10 s⟧
tt = np.arange(0, 10, 0.01); Xc = np.fft.fft(np.cos(2*np.pi*5*tt)); P = np.abs(Xc)**2/np.sum(np.abs(Xc)**2)
fr = np.fft.fftfreq(len(tt), 0.01)
frac = P[np.argmin(np.abs(fr - 5))]
assert abs(frac - 0.5) < 1e-9 and abs(P[np.argmin(np.abs(fr + 5))] - 0.5) < 1e-9
report("cos_frac", frac, ".2f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Rayleigh: $\\int f^2=\\int|F|^2$ = {{ray_gauss}} cho Gauss và {{ray_exp}} cho $e^{-x}H$. Công suất: $\\int fg$ = {{pow_direct}} = $\\int FG^*$ = {{pow_fourier}}, gồm phần thực-thực {{pow_re}} và ảo-ảo {{pow_im}}. Tự tương quan của $\\Pi$ có biến đổi {{ac_pi_03}} tại 0.3 (đúng $\\text{sinc}^2$), phổ công suất chuẩn hóa của Gauss có tích phân {{ns_int}}, và $\\cos2\\pi(5t)$ dồn {{cos_frac}} công suất vào mỗi vạch $\\pm5$ Hz.||Rayleigh: $\\int f^2=\\int|F|^2$ = {{ray_gauss}} for the Gaussian and {{ray_exp}} for $e^{-x}H$. Power: $\\int fg$ = {{pow_direct}} = $\\int FG^*$ = {{pow_fourier}}, made of the real-real part {{pow_re}} and the imaginary-imaginary part {{pow_im}}. The autocorrelation of $\\Pi$ has transform {{ac_pi_03}} at 0.3 (exactly $\\text{sinc}^2$), the Gaussian's normalised power spectrum integrates to {{ns_int}}, and $\\cos2\\pi(5t)$ puts {{cos_frac}} of the power in each $\\pm5$ Hz line.⟧"""),
        ("md", """## 5. ⟦Đạo hàm, hàm suy rộng và bài tập chọn||Derivative, generalized functions and selected problems⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Đạo hàm nhân phổ với $i2\\pi s$ và dịch cực đại lên thế nào, đạo hàm của bậc thang có tiến về xung, đạo hàm của tích chập chuyển sang một thừa số, và các bài tập 10, 17, 19, 21 có đúng? Ta so tích phân số với công thức, và tích chập đạo hàm với tích chập gốc.||How does differentiation multiply the spectrum by $i2\\pi s$ and move the maximum up, does the derivative of the step tend to the impulse, does the derivative of a convolution move onto one factor, and do problems 10, 17, 19 and 21 hold? We compare numerical integrals with formulas, and the derivative convolution with the original.⟧"""),
        ("code", r'''# ⟦Định lý đạo hàm: f' = −2πx e^{−πx²}||Derivative theorem: f' = −2πx e^{−πx²}⟧
fprime = lambda x: -2*np.pi*x*np.exp(-np.pi*x**2)
der = ft_support(fprime, -10, 10, 0.3)
assert abs(der - 2j*np.pi*0.3*np.exp(-np.pi*0.09)) < 1e-9
report("der_03", abs(der), ".4f")
sgrid = np.linspace(0.001, 3, 300001)
for n, key in ((1, "pk1"), (2, "pk2"), (3, "pk3")):
    peak_grid = sgrid[np.argmax((2*np.pi*sgrid)**n*np.exp(-np.pi*sgrid**2))]
    assert abs(peak_grid - np.sqrt(n/(2*np.pi))) < 1e-4
    report(key, np.sqrt(n/(2*np.pi)), ".4f")

# ⟦Bậc thang tắt dần: đạo hàm có biến đổi i2πs/(ε + i2πs) → 1||The decaying step: its derivative has transform i2πs/(ε + i2πs) → 1⟧
eps = 1e-3; s_ = 0.5
Fd = 1j*2*np.pi*s_/(eps + 2j*np.pi*s_)
dev = abs(Fd - 1)
assert abs(dev - eps/np.hypot(eps, 2*np.pi*s_)) < 1e-15
report("step_dev", dev, ".1e")

# ⟦Đạo hàm của tích chập: y = x*h so với x'*s (mạch RC)||Derivative of a convolution: y = x*h versus x'*s (RC circuit)⟧
dt = 1e-3; tt = np.arange(0, 12, dt)
xin = np.sin(2*np.pi*tt)*(1 - np.exp(-8*tt))                     # ⟦vào bật mượt, x(0) = 0||smoothly switched-on input, x(0) = 0⟧
h_rc = np.exp(-tt); s_rc = 1 - np.exp(-tt)
y1 = np.convolve(xin, h_rc)[:len(tt)]*dt
xdot = np.gradient(xin, dt)
y2 = np.convolve(xdot, s_rc)[:len(tt)]*dt
ds_diff = np.max(np.abs(y1 - y2)[:8000])
assert ds_diff < 5e-3
report("ds_diff", ds_diff, ".1e")

# ⟦Bài tập 10 (hình thang), 17 (sinc⁴), 21 (xe^{−πx²})||Problems 10 (trapezoid), 17 (sinc⁴), 21 (xe^{−πx²})⟧
tr = ft_support(lambda x: 2*max(1 - abs(x)/2, 0) - max(1 - abs(x), 0), -2, 2, 0.3, [-1, 0, 1]).real
assert abs(tr - np.sinc(0.3)**2*(1 + 2*np.cos(2*np.pi*0.3))) < 1e-9
report("trap_03", tr, ".4f")
s4 = integrate.quad(lambda x: np.sinc(x)**4, -300, 300, limit=4000)[0]
assert abs(s4 - 2/3) < 1e-4 and abs(integrate.quad(lambda s: max(1 - abs(s), 0)**2, -1, 1, points=[0])[0] - 2/3) < 1e-9
report("sinc4", 2/3, ".4f")
xg = ft_support(lambda x: x*np.exp(-np.pi*x**2), -10, 10, 0.3)
assert abs(xg + 1j*0.3*np.exp(-np.pi*0.09)) < 1e-9
report("xg_03", abs(xg), ".4f")

# ⟦Định lý tích phân: FT[H*f − H] = (F − 1)/(i2πs)||Integral theorem: FT[H*f − H] = (F − 1)/(i2πs)⟧
Hf = lambda x: 0.5*(1 + special.erf(np.sqrt(np.pi)*x))
lhs = ft_support(lambda x: Hf(x) - (1.0 if x > 0 else 0.0 if x < 0 else 0.5), -12, 12, 0.3, [0])
rhs = (np.exp(-np.pi*0.09) - 1)/(2j*np.pi*0.3)
assert abs(lhs - rhs) < 1e-6
report("int_thm_diff", abs(lhs - rhs), ".1e")

# ⟦Hàm suy rộng: ∫ e^{−i2πas} F(s) ds = e^{−πa²}; và p(ax+b) tỉ lệ cộng dịch||Generalized function: ∫ e^{−i2πas} F(s) ds = e^{−πa²}; and p(ax+b) similarity with shift⟧
gf = integrate.quad(lambda s: np.cos(2*np.pi*0.5*s)*np.exp(-np.pi*s**2), -10, 10)[0]
assert abs(gf - np.exp(-np.pi*0.25)) < 1e-9
report("gf_05", gf, ".4f")
a_, b_, s4_ = 2.0, 0.3, 0.4
sb = ft_support(lambda x: g(a_*x + b_), -10, 10, s4_)
sb_formula = np.exp(2j*np.pi*b_*s4_/a_)*np.exp(-np.pi*(s4_/a_)**2)/abs(a_)
assert abs(sb - sb_formula) < 1e-9
report("sb_mag", abs(sb), ".4f"); report("sb_ph", np.degrees(np.angle(sb)), ".1f")'''),
        ("code", r'''sg = np.linspace(0, 2.5, 500)
plt.figure(figsize=(7.5, 3.3))
for n, c in ((0, "gray"), (1, "tab:blue"), (2, "tab:orange"), (3, "tab:red")):
    plt.plot(sg, (2*np.pi*sg)**n*np.exp(-np.pi*sg**2), color=c, label=f"n = {n}")
plt.xlabel("s"); plt.ylabel("|(i2πs)ⁿ F(s)|"); plt.legend(); plt.tight_layout(); plt.show()''', dict(fig="derivative", cap="⟦Hình 4. Đạo hàm nhiều lần nhân phổ với (i2πs)ⁿ: tần số thấp bị làm yếu, cực đại dịch dần lên cao (n = 1, 2, 3), và tần số 0 bị triệt tiêu.||Figure 4. Repeated differentiation multiplies the spectrum by (i2πs)ⁿ: low frequencies are attenuated, the maximum moves up (n = 1, 2, 3), and zero frequency is suppressed.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Biến đổi của $f'$ tại 0.3 có độ lớn {{der_03}}; cực đại của $(2\\pi s)^ne^{-\\pi s^2}$ ở {{pk1}}, {{pk2}}, {{pk3}}. Bậc thang tắt dần lệch xung {{step_dev}}. Mạch RC: $x*h$ và $x'*s$ lệch {{ds_diff}}. Bài tập: hình thang {{trap_03}}, $\\int\\text{sinc}^4$ = {{sinc4}}, $xe^{-\\pi x^2}$ có độ lớn {{xg_03}}, định lý tích phân lệch {{int_thm_diff}}. Hàm suy rộng: {{gf_05}} và $p(2x+0.3)$ có độ lớn {{sb_mag}}, pha {{sb_ph}} độ.||The transform of $f'$ at 0.3 has magnitude {{der_03}}; the maximum of $(2\\pi s)^ne^{-\\pi s^2}$ lies at {{pk1}}, {{pk2}}, {{pk3}}. The decaying step deviates from the impulse by {{step_dev}}. RC circuit: $x*h$ and $x'*s$ differ by {{ds_diff}}. Problems: trapezoid {{trap_03}}, $\\int\\text{sinc}^4$ = {{sinc4}}, $xe^{-\\pi x^2}$ has magnitude {{xg_03}}, the integral theorem deviates by {{int_thm_diff}}. Generalized function: {{gf_05}} and $p(2x+0.3)$ has magnitude {{sb_mag}}, phase {{sb_ph}} degrees.⟧"""),
    ],
)
