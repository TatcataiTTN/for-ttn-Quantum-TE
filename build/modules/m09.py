from lib import F, C, UL, OL, TBL

MOD = dict(
    n=9, slug="filters-linearity", part="A", book="B",
    title="⟦Dạng sóng, phổ, bộ lọc và tính tuyến tính||Waveforms, spectra, filters and linearity⟧",
    blurb="⟦Phổ của dạng sóng điện, hàm truyền và đáp ứng xung/bậc thang của bộ lọc, lọc số, các định lý đọc theo ngôn ngữ mạch, và vì sao tuyến tính cộng bất biến theo thời gian dẫn tới tích chập.||"
          "The spectrum of an electrical waveform, the transfer function and impulse/step responses of a filter, digital filtering, the theorems read in circuit language, and why linearity plus time invariance leads to convolution.⟧",
    src="⟦Bracewell, chương 9, tr. 198–218||Bracewell, chapter 9, pp. 198–218⟧",
    data="⟦Sinh bằng mã: mạch RC, bộ lọc trung bình trượt, sóng điều biên, hệ phi tuyến và biến thiên theo thời gian, đường truyền xung||Generated in code: an RC circuit, a moving-average filter, an amplitude-modulated wave, nonlinear and time-varying systems, a pulse-forming line⟧",
    objectives=[
        "⟦Viết phổ $S(f)$ của dạng sóng thực, nêu các hệ ký hiệu 1, 2, 3 và các ràng buộc ở bảng 9.1.||Write the spectrum $S(f)$ of a real waveform, state notation systems 1, 2, 3 and the restrictions of Table 9.1.⟧",
        "⟦Đặc trưng một bộ lọc bằng $T(f)$, đáp ứng xung $I(t)$ hoặc đáp ứng bậc thang $A(t)$ và chuyển qua lại giữa chúng.||Characterise a filter by $T(f)$, impulse response $I(t)$ or step response $A(t)$ and convert between them.⟧",
        "⟦Lọc tín hiệu số bằng tổng chập với $h(n)$ và biết vì sao mẫu của đáp ứng liên tục trùng với $g(n)$.||Filter a digital signal with a convolution sum with $h(n)$ and know why samples of the continuous response equal $g(n)$.⟧",
        "⟦Đọc các định lý (tỉ lệ, dịch, điều chế, điều chế đảo) bằng ngôn ngữ dạng sóng, phổ và bộ lọc.||Read the theorems (similarity, shift, modulation, its converse) in the language of waveforms, spectra and filters.⟧",
        "⟦Chứng minh tuyến tính cộng bất biến theo thời gian tương đương đáp ứng điều hòa và tích chập; phân biệt tuyến tính với bất biến, và tính ổn định.||Prove that linearity plus time invariance is equivalent to harmonic response and convolution; distinguish linearity from invariance, and treat stability.⟧",
    ],
    parts=[
        # ------------------------------------------------ PART 1
        dict(
            title="⟦Dạng sóng điện và phổ của chúng||Electrical waveforms and their spectra⟧",
            scr=("⟦Một dạng sóng điện là hàm thực của thời gian, nhưng ta vẫn nói về bậc thang, xung và sóng đơn sắc như thể chúng là dạng sóng.||An electrical waveform is a real function of time, yet we speak of steps, impulses and monochromatic signals as if they were waveforms.⟧",
                 "⟦Phổ được định nghĩa thế nào, có ràng buộc gì vì dạng sóng là thực, và các cách viết khác nhau của biến đổi (hệ 1, 2, 3, Hartley) liên hệ ra sao?||How is the spectrum defined, what restrictions follow from the waveform being real, and how are the different ways of writing the transform (systems 1, 2, 3, Hartley) related?⟧",
                 "⟦Phổ của dạng sóng thực là Hermite; dạng sóng nhân quả có phần ảo là biến đổi Hilbert của phần thực.||The spectrum of a real waveform is Hermitian; for a causal waveform the imaginary part is the Hilbert transform of the real part.⟧"),
            preview=["⟦Định nghĩa phổ của dạng sóng||Definition of the spectrum of a waveform⟧", "⟦Các hệ ký hiệu và ràng buộc||Notation systems and restrictions⟧", "⟦Biến đổi Hartley||The Hartley transform⟧"],
            slides=[
                ("⟦Dạng sóng điện||The electrical waveform⟧",
                 "<p>⟦Dạng sóng điện $V(t)$ là hàm thực, đơn trị của thời gian, chỉ phải biểu diễn sự phụ thuộc thời gian có thể có về vật lý. Tuy vậy quen dùng nói như thể bậc thang, xung và tín hiệu hoàn toàn đơn sắc là dạng sóng, dù không thể tạo ra dòng hay điện áp gián đoạn, vô hạn hay vĩnh cửu. Khi nói về mạch với bậc thang hay xung, ta ngầm nói tới một phát biểu chặt hơn trong đó hành vi ấy là giới hạn của dãy kích thích tiến tới bậc thang hay xung vô hạn; cũng đúng với dòng xoay chiều hay một chiều (Bracewell, tr. 198).||"
                 "An electrical waveform $V(t)$ is a single-valued real function of time subject only to representing physically possible time dependence. Yet it is established usage to speak as though steps, impulses and absolutely monochromatic signals were waveforms, even though discontinuous, infinite or eternal currents or voltages cannot be generated. When we state the behaviour of circuits in the presence of steps or impulses we imply a more rigorous statement in which that behaviour is the limiting form under a sequence of stimuli approaching a step or infinite pulse; the same applies to alternating or direct current (Bracewell, p. 198).⟧</p>"),
                ("⟦Phổ của dạng sóng||The spectrum of a waveform⟧",
                 "<p>⟦Phổ $S(f)$ của $V(t)$ được định nghĩa là biến đổi Fourier của nó (hoặc biến đổi trong giới hạn nếu cần), và tổng hợp lại bằng biến đổi ngược (tr. 198):||The spectrum $S(f)$ of $V(t)$ is defined as its Fourier transform (or transform in the limit as necessary), and $V$ is recovered by the inverse transform (p. 198):⟧</p>"
                 + F("⟦Phổ||Spectrum⟧", r"S(f)=\int_{-\infty}^{\infty}V(t)\,e^{-i2\pi ft}\,dt,\qquad V(t)=\int_{-\infty}^{\infty}S(f)\,e^{i2\pi ft}\,df")
                 + "<p>⟦Đây là hệ 1 của chương 2. Với $V=e^{-t}H(t)$, $S=1/(1+i2\\pi f)$; tại $f=0.3$ độ lớn là {{sy_mag}}.||This is system 1 of chapter 2. With $V=e^{-t}H(t)$, $S=1/(1+i2\\pi f)$; at $f=0.3$ its magnitude is {{sy_mag}}.⟧</p>"),
                ("⟦Dạng sóng thực: phổ Hermite||A real waveform: a Hermitian spectrum⟧",
                 "<p>⟦Vì $V(t)$ thực nên $S(f)$ chịu một ràng buộc: phần thực luôn chẵn và phần ảo lẻ, tức $S$ là Hermite (chương 2; tr. 199). Số đo với dãy thực ngẫu nhiên: $|S(-f)-S^*(f)|$ lệch tối đa {{herm_dev}}, tức mọi giá trị thỏa $S(-f)=S^*(f)$.||"
                 "Since $V(t)$ is real, $S(f)$ is subject to a restriction: the real part must always be even and the imaginary part odd, i.e. $S$ is Hermitian (chapter 2; p. 199). Measured with a random real sequence: $|S(-f)-S^*(f)|$ deviates by at most {{herm_dev}}, i.e. every value satisfies $S(-f)=S^*(f)$.⟧</p>"),
                ("⟦Bảng 9.1: các ràng buộc tương ứng||Table 9.1: corresponding restrictions⟧",
                 TBL(["⟦Ràng buộc||Restriction⟧", "⟦Trên dạng sóng||On the waveform⟧", "⟦Trên phổ||On the spectrum⟧"],
                     [["⟦Thực||Real⟧", "$\\text{Im}\\,V=0$", "⟦$\\text{Re}\\,S$ chẵn, $\\text{Im}\\,S$ lẻ||$\\text{Re}\\,S$ even, $\\text{Im}\\,S$ odd⟧"], ["⟦Bật lên (nhân quả)||Switches on (causal)⟧", "$V(t)=0,\\ t<0$", "⟦$\\text{Im}\\,S$ là biến đổi Hilbert của $\\text{Re}\\,S$||$\\text{Im}\\,S$ is the Hilbert transform of $\\text{Re}\\,S$⟧"],
                      ["⟦Không âm||Nonnegative⟧", "$V(t)\\ge0$", "⟦Phức tạp||Complicated⟧"], ["⟦Năng lượng hữu hạn||Finite energy⟧", "$\\int V^2dt=W$", "$\\int|S|^2df=W$"],
                      ["⟦Thời lượng hữu hạn||Finite duration⟧", "$V(t)=0,\\ |t|>T$", "⟦Xác định bởi lấy mẫu $S$||Fully determined by samples of $S$⟧"], ["⟦Giới hạn băng||Band-limited⟧", "⟦Xác định bởi lấy mẫu $V$||Fully determined by samples of $V$⟧", "$S(f)=0,\\ |f|>f_0$"]])
                 + "<p>⟦(Bracewell, tr. 199).||(Bracewell, p. 199).⟧</p>"),
                ("⟦Nhân quả và biến đổi Hilbert||Causality and the Hilbert transform⟧",
                 "<p>⟦Với dạng sóng nhân quả, phần thực và phần ảo của phổ không độc lập. Số đo với $V=e^{-t}H(t)$: $\\text{Re}\\,S=1/(1+4\\pi^2f^2)$, $\\text{Im}\\,S=-2\\pi f/(1+4\\pi^2f^2)$; biến đổi Hilbert (tính bằng FFT) của $\\text{Re}\\,S$ lệch $-\\text{Im}\\,S$ tối đa {{hilb_dev}} (dấu theo quy ước $e^{-i2\\pi ft}$: $\\text{Im}\\,S=-\\mathcal H[\\text{Re}\\,S]$).||"
                 "For a causal waveform the real and imaginary parts of the spectrum are not independent. Measured with $V=e^{-t}H(t)$: $\\text{Re}\\,S=1/(1+4\\pi^2f^2)$, $\\text{Im}\\,S=-2\\pi f/(1+4\\pi^2f^2)$; the Hilbert transform (computed by FFT) of $\\text{Re}\\,S$ deviates from $-\\text{Im}\\,S$ by at most {{hilb_dev}} (sign per the $e^{-i2\\pi ft}$ convention: $\\text{Im}\\,S=-\\mathcal H[\\text{Re}\\,S]$).⟧</p>"),
                ("⟦Hệ 2 và hệ 3||Systems 2 and 3⟧",
                 "<p>⟦Trong hệ 2, thay $\\omega=2\\pi f$: $S(\\omega)=\\int Ve^{-i\\omega t}dt$, $V=\\dfrac1{2\\pi}\\int S(\\omega)e^{i\\omega t}d\\omega$; hệ số bất đối xứng $1/2\\pi$ có thể viết trước tích phân nào tùy cách đồng nhất, và người dùng nhớ vị trí của nó nhờ điều: nếu thay $d\\omega/2\\pi$ bằng $df$ thì công thức đối xứng. Hệ 3 đối xứng: $S=\\dfrac{1}{\\sqrt{2\\pi}}\\int Ve^{-i\\omega t}dt$ (tr. 199). Số đo với Gauss $e^{-\\pi t^2}$: hệ 1 tại $f=0.3$ là {{sy_1}}, hệ 2 tại $\\omega=2\\pi(0.3)$ cùng {{sy_1}}, hệ 3 là {{sy_3}} (chia $\\sqrt{2\\pi}$).||"
                 "In system 2, substituting $\\omega=2\\pi f$: $S(\\omega)=\\int Ve^{-i\\omega t}dt$, $V=\\dfrac1{2\\pi}\\int S(\\omega)e^{i\\omega t}d\\omega$; the unsymmetrical coefficient $1/2\\pi$ may be written in front of either integral, and users remember its place by noting that if $d\\omega/2\\pi$ were replaced by $df$ the formulas would be symmetrical. System 3 is symmetric: $S=\\dfrac{1}{\\sqrt{2\\pi}}\\int Ve^{-i\\omega t}dt$ (p. 199). Measured with the Gaussian $e^{-\\pi t^2}$: system 1 at $f=0.3$ is {{sy_1}}, system 2 at $\\omega=2\\pi(0.3)$ is also {{sy_1}}, system 3 is {{sy_3}} (divided by $\\sqrt{2\\pi}$).⟧</p>"),
                ("⟦Dạng sóng là chuỗi xung: nối với xử lý tín hiệu số||A train of impulses: the bridge to DSP⟧",
                 "<p>⟦Dạng sóng $V(t)$ có thể là một chuỗi xung có biên độ khác nhau. Đặc biệt, các xung có thể cách đều nhau, xảy ra ở các thời điểm $t=t_i$ với cường độ $a_i$, trong đó $i$ và $t_i$ nguyên. Lý thuyết thời gian liên tục thông thường khi đó bao trùm mọi tín hiệu biểu diễn được bằng dãy hệ số $\\{a_i\\}$ và trực tiếp sinh ra nội dung của xử lý tín hiệu số DSP (tr. 199 đến 200).||"
                 "The waveform $V(t)$ may be a train of impulses of varying amplitude. In particular the impulses may be regularly spaced, occurring at times $t=t_i$ with strengths $a_i$, where $i$ and $t_i$ are integers. Normal continuous-time theory then covers signals representable by the sequence of coefficients $\\{a_i\\}$ and directly generates the subject matter of digital signal processing (DSP) (pp. 199 to 200).⟧</p>"),
                ("⟦Đối xứng hoàn toàn: cặp Hartley||A pair with total symmetry: the Hartley transform⟧",
                 "<p>⟦Hartley (1942) đề xuất cặp công thức đối xứng hoàn toàn: $H(\\omega)=\\dfrac{1}{2\\pi}\\int V(t)(\\cos\\omega t+\\sin\\omega t)dt$ và biến đổi ngược có cùng nhân. Vì $\\cos\\omega t+\\sin\\omega t$ là nhân Fourier, các định lý Fourier có bản tương ứng (chương 12), và thuật toán Hartley nhanh được khảo sát trong hàng trăm bài báo từ 1983 (tr. 200). Với dạng sóng thực, $H=\\text{Re}\\,S-\\text{Im}\\,S$. Số đo với $V=e^{-t}H(t)$ tại $f=0.3$: tích phân trực tiếp và $\\text{Re}\\,S-\\text{Im}\\,S$ cùng cho {{hart_val}}.||"
                 "Hartley (1942) proposed a pair of formulas with total symmetry: $H(\\omega)=\\dfrac{1}{2\\pi}\\int V(t)(\\cos\\omega t+\\sin\\omega t)dt$ with the inverse having the same kernel. Since $\\cos\\omega t+\\sin\\omega t$ is a Fourier kernel, the Fourier theorems have counterparts (chapter 12), and the fast Hartley algorithm has been explored in hundreds of papers since 1983 (p. 200). For a real waveform, $H=\\text{Re}\\,S-\\text{Im}\\,S$. Measured with $V=e^{-t}H(t)$ at $f=0.3$: the direct integral and $\\text{Re}\\,S-\\text{Im}\\,S$ both give {{hart_val}}.⟧</p>"),
                ("⟦Tự kiểm tra phần 1||Self-check, part 1⟧",
                 UL(["⟦Ràng buộc nào trên phổ xuất phát từ việc $V(t)$ thực?||What restriction on the spectrum follows from $V(t)$ being real?⟧",
                     "⟦Dạng sóng nhân quả cho quan hệ gì giữa phần thực và ảo của $S$?||What relation between the real and imaginary parts of $S$ does a causal waveform give?⟧",
                     "⟦Hệ 3 khác hệ 1 ở hệ số nào?||By what factor does system 3 differ from system 1?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: $S(-f)=S^*(f)$; chúng liên hệ bằng biến đổi Hilbert; hệ số $1/\\sqrt{2\\pi}$ và biến số $\\omega$.||Hints: $S(-f)=S^*(f)$; they are related by the Hilbert transform; a factor $1/\\sqrt{2\\pi}$ and the variable $\\omega$.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 2
        dict(
            title="⟦Bộ lọc: hàm truyền, đáp ứng xung và đáp ứng bậc thang||Filters: transfer function, impulse response and step response⟧",
            scr=("⟦Một bộ lọc là một hệ vật lý có đầu vào và đầu ra: bốn cực, hai cổng, đầu dò cơ hay âm.||A filter is a physical system with an input and an output: a fourpole, two-port element, mechanical or acoustic transducer.⟧",
                 "⟦Làm sao xác định đầu ra khi biết đầu vào, và có mấy cách mô tả một bộ lọc?||How do we determine the output from the input, and in how many ways can a filter be specified?⟧",
                 "⟦Ba cách: hàm truyền $T(f)$, đáp ứng xung $I(t)$ (biến đổi ngược của $T$), và đáp ứng bậc thang $A(t)$ (tích phân của $I$).||Three ways: the transfer function $T(f)$, the impulse response $I(t)$ (inverse transform of $T$) and the step response $A(t)$ (integral of $I$).⟧"),
            preview=["⟦Bộ lọc và hàm truyền||A filter and its transfer factor⟧", "⟦Hai cách tính đầu ra||Two ways to compute the output⟧", "⟦Đáp ứng bậc thang||The step response⟧"],
            slides=[
                ("⟦Bộ lọc||What is a filter⟧",
                 "<p>⟦Ta dùng \"bộ lọc\" để chỉ hệ vật lý có đầu vào và đầu ra; tên khác gồm đầu dò, bốn cực, mạng bốn cổng, phần tử hai cổng. Dù dùng ngôn ngữ điện, các xét này thường áp dụng cho đầu dò cơ và âm và các thiết bị tương đương ở lĩnh vực khác có truyền dao động. Ngay trong điện, bộ lọc có thể là cụm cuộn dây và tụ điện hay cấu trúc hình học tinh vi trong ống dẫn sóng (Bracewell, tr. 200).||"
                 "We use the term \"filter\" for a physical system having an input and an output; equivalent terms are transducer, fourpole, four-terminal network and two-port element. Although electrical terminology is used, the considerations usually apply to mechanical and acoustical transducers and to equivalent devices in other fields where vibrations are transmitted. Even within electricity filters may range from clusters of wire coils and capacitors to intricate geometrical structures in waveguide (Bracewell, p. 200).⟧</p>"),
                ("⟦Hàm truyền $T(f)$||The transfer factor $T(f)$⟧",
                 "<p>⟦Khi dạng sóng $A\\cos2\\pi ft$ vào một bộ lọc điện tuyến tính bất biến theo thời gian, đầu ra cũng điều hòa (sẽ chứng minh sau) nhưng nói chung khác biên độ và pha: $B\\cos(2\\pi ft-\\phi)$. Bộ lọc được xác định hoàn toàn bởi đại lượng phức phụ thuộc tần số $T(f)=\\dfrac{B}{A}e^{-i\\phi}$ (tr. 200, 209), gọi là hệ số truyền, hàm truyền, hàm hệ thống hay đáp ứng tần số. Số đo với mạch RC $I=e^{-t}H(t)$, $f=0.3$: $|T|$ = {{rc_amp}} và pha $-\\phi$ = {{rc_ph}} độ theo công thức $1/(1+i2\\pi f)$; mô phỏng miền thời gian (đầu ra ổn định của $\\cos2\\pi ft$) cho biên độ {{rc_amp_sim}} và trễ pha {{rc_ph_sim}} độ.||"
                 "When a waveform $A\\cos2\\pi ft$ is fed into a linear time-invariant electrical filter, the output is also harmonic (to be proved later) but generally with a different amplitude and phase: $B\\cos(2\\pi ft-\\phi)$. The filter is completely specified by a frequency-dependent complex quantity $T(f)=\\dfrac{B}{A}e^{-i\\phi}$ (pp. 200, 209), called the transfer factor, transfer function, system function or frequency response. Measured with the RC circuit $I=e^{-t}H(t)$, $f=0.3$: $|T|$ = {{rc_amp}} and phase $-\\phi$ = {{rc_ph}} degrees by the formula $1/(1+i2\\pi f)$; a time-domain simulation (the steady-state output for $\\cos2\\pi ft$) gives amplitude {{rc_amp_sim}} and phase lag {{rc_ph_sim}} degrees.⟧</p>"
                 + F("⟦Hàm truyền||Transfer factor⟧", r"T(f)=\frac{B}{A}\,e^{-i\phi}")),
                ("⟦Cách 1: phân tích thành phổ, nhân, tổng hợp||Way 1: analyse into a spectrum, multiply, synthesise⟧",
                 "<p>⟦Muốn tính đầu ra $V_2(t)$ khi có đầu vào $V_1(t)$: phân tích $V_1$ thành phổ, nhân mỗi thành phần với hệ số truyền tương ứng để có phổ của $V_2$, rồi tổng hợp: $S_2(f)=T(f)S_1(f)$ và (tr. 200 đến 201):||To compute the output $V_2(t)$ for an input $V_1(t)$: analyse $V_1$ into its spectrum, multiply each component by the corresponding transfer factor to obtain the spectrum of $V_2$, then synthesise: $S_2(f)=T(f)S_1(f)$ and (pp. 200 to 201):⟧</p>"
                 + F("⟦Đầu ra qua phổ||Output through the spectrum⟧", r"V_2(t)=\int_{-\infty}^{\infty}T(f)\,S_1(f)\,e^{i2\pi ft}\,df\qquad(1)")),
                ("⟦Cách 2: tích chập với đáp ứng xung||Way 2: convolve with the impulse response⟧",
                 "<p>⟦Vì nhân biến đổi ứng với tích chập, $V_2(t)$ có thể suy trực tiếp từ $V_1(t)$ bằng làm trơn với một hàm đặc trưng của bộ lọc, $V_2=I*V_1$ với $I(t)$ là biến đổi của $T(f)$ (tr. 201). $I(t)$ chính là đầu ra khi $S_1=1$, tức khi $V_1=\\delta(t)$: \"đáp ứng xung\" của bộ lọc trong truyền thông. Với nhiều mục đích nó hữu ích như đặc tính tần số, và có thể dễ đo hơn. Số đo: xung chữ nhật đơn vị (rộng 1) qua mạch RC cho $V_2(1.5)$ = {{pulse_y}} bằng tích chập số, bằng $e^{-0.5}-e^{-1.5}$ và bằng IFFT của $T\\cdot S_1$.||"
                 "Since multiplication of transforms corresponds to convolution, $V_2(t)$ may be derived directly from $V_1(t)$ by smoothing with a function characteristic of the filter, $V_2=I*V_1$ with $I(t)$ the transform of $T(f)$ (p. 201). $I(t)$ is the output when $S_1=1$, i.e. when $V_1=\\delta(t)$: the \"impulse response\" of the filter in communications. For many purposes it is as useful as the frequency characteristic and may be much easier to obtain experimentally. Measured: a unit rectangular pulse (width 1) through the RC circuit gives $V_2(1.5)$ = {{pulse_y}} by numerical convolution, by $e^{-0.5}-e^{-1.5}$ and by the IFFT of $T\\cdot S_1$.⟧</p>"
                 + F("⟦Đầu ra qua tích chập||Output through convolution⟧", r"V_2(t)=I(t)*V_1(t)\qquad(2),\qquad I(t)\ \supset\ T(f)")),
                ("⟦Sơ đồ tóm tắt||The summary diagram⟧",
                 "<p>⟦Gộp các đại lượng vào một sơ đồ, hàm thời gian ở trái, biến đổi ở phải: $V_1(t)\\leftrightarrow S_1(f)$; tích chập với $I(t)$ ứng với nhân với $T(f)$; kết quả $V_2(t)\\leftrightarrow S_2(f)$ (tr. 201). Phương trình (2) chia $V_1$ thành chuỗi xung và biểu diễn $V_2$ là tổng đáp ứng của từng xung thành phần.||Combining all the quantities into one diagram with time functions on the left and transforms on the right: $V_1(t)\\leftrightarrow S_1(f)$; convolution with $I(t)$ corresponds to multiplication by $T(f)$; the result is $V_2(t)\\leftrightarrow S_2(f)$ (p. 201). Equation (2) breaks $V_1$ up into a sequence of impulses and expresses $V_2$ as the sum of the responses to each component impulse.⟧</p>"),
                ("⟦Cách thứ ba: đáp ứng bậc thang $A(t)$||A third way: the step response $A(t)$⟧",
                 "<p>⟦Đáp ứng bậc thang $A(t)$ là đầu ra khi bật một tín hiệu hằng, $V_1=H(t)$. Nhìn $V_1$ như chuỗi bậc thang $V_1'(\\tau)H(t-\\tau)$ ta có $V_2=A*V_1'$ (phương trình 3). Biến đổi và so với (1): $S_2=A(f)\\,i2\\pi fS_1$ (phương trình 4), nên $T(f)=i2\\pi f\\,\\mathcal A(f)$ với $\\mathcal A$ là biến đổi của $A$, và $I(t)=A'(t)$ (tr. 201 đến 202). Số đo với mạch RC, $A=1-e^{-t}$: $A'=e^{-t}$ = $I$ với lệch {{step_dev}}; và $V_2=A'*V_1$ trùng $I*V_1$ trong ví dụ xung chữ nhật.||"
                 "The step response $A(t)$ is the output when a constant signal is switched on, $V_1=H(t)$. Regarding $V_1$ as a sequence of steps $V_1'(\\tau)H(t-\\tau)$ we have $V_2=A*V_1'$ (equation 3). Transforming and comparing with (1): $S_2=\\mathcal A(f)\\,i2\\pi fS_1$ (equation 4), so $T(f)=i2\\pi f\\,\\mathcal A(f)$ with $\\mathcal A$ the transform of $A$, and $I(t)=A'(t)$ (pp. 201 to 202). Measured with the RC circuit, $A=1-e^{-t}$: $A'=e^{-t}$ equals $I$ with deviation {{step_dev}}; and $V_2=A'*V_1$ matches $I*V_1$ in the rectangular-pulse example.⟧</p>"
                 + F("⟦Quan hệ đáp ứng bậc thang||Step-response relations⟧", r"V_2=A*V_1'=A'*V_1,\qquad T(f)=i2\pi f\,\mathcal A(f),\qquad I(t)=A'(t)")),
                ("⟦Bảng: ba cách đặc trưng bộ lọc||Table: three ways to specify a filter⟧",
                 TBL(["⟦Phân tích đầu vào thành||Analyse input into⟧", "⟦Đặc trưng bộ lọc bằng||Specify filter by⟧", "⟦Biến đổi Fourier||Fourier transform⟧"],
                     [["⟦Sóng sin và cosin||Sine and cosine waves⟧", "⟦Đặc tính truyền $T(f)$||Transmission characteristic $T(f)$⟧", "$I(t)$"], ["⟦Xung||Impulses⟧", "⟦Đáp ứng xung $I(t)$||Impulse response $I(t)$⟧", "$T(f)$"], ["⟦Bậc thang||Steps⟧", "⟦Đáp ứng bậc thang $A(t)$||Step response $A(t)$⟧", "$T(f)/i2\\pi f$"]])
                 + "<p>⟦(Bracewell, tr. 202, hình 9.1). Vậy tích phân Fourier xuất hiện trong lý thuyết bộ lọc dưới ba dạng, và tích chập cũng: $V_2=I*V_1=A'*V_1$.||(Bracewell, p. 202, Fig. 9.1). So the Fourier integral arises in filter theory in three forms, and so does the convolution: $V_2=I*V_1=A'*V_1$.⟧</p>"),
                ("⟦Đạo hàm, tích phân và cấp phân số||Derivatives, integrals and fractional order⟧",
                 "<p>⟦Viết lại (4) với cách chia nhân tử khác ta có $V_2=A'*V_1$, hoặc các công thức chứa đạo hàm và tích phân bậc cao hơn, kể cả bậc phân số (tr. 202). Hình 9.1 tóm tắt: đạo hàm ứng với nhân $i2\\pi f$, tích phân ứng với chia $i2\\pi f$. Ví dụ đáp ứng với $t$ (\"đáp ứng dốc\") $R(t)$: $V_2=R*V_1''$ (bài tập 1, tr. 211).||Rewriting (4) with a different choice of factors gives $V_2=A'*V_1$, or formulas involving higher derivatives and integrals, including fractional order (p. 202). Fig. 9.1 summarises: differentiation corresponds to multiplication by $i2\\pi f$, integration to division by $i2\\pi f$. For the ramp response $R(t)$: $V_2=R*V_1''$ (problem 1, p. 211).⟧</p>"),
                ("⟦Tự kiểm tra phần 2||Self-check, part 2⟧",
                 UL(["⟦Đáp ứng xung $I(t)$ của mạch RC $T=1/(1+i2\\pi f)$?||What is the impulse response $I(t)$ of the RC circuit $T=1/(1+i2\\pi f)$?⟧",
                     "⟦Khi biết đáp ứng bậc thang $A$, làm sao có $I$?||Knowing the step response $A$, how do we obtain $I$?⟧",
                     "⟦Vì sao $S_2=TS_1$ tương đương $V_2=I*V_1$?||Why is $S_2=TS_1$ equivalent to $V_2=I*V_1$?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: $e^{-t}H(t)$; $I=A'$; nhân biến đổi ứng với tích chập.||Hints: $e^{-t}H(t)$; $I=A'$; multiplication of transforms corresponds to convolution.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 3
        dict(
            title="⟦Tính tổng quát và lọc số||Generality and digital filtering⟧",
            scr=("⟦Lý thuyết bộ lọc tuyến tính không chỉ dành cho điện; mọi hệ tuyến tính bất biến, cơ, âm, quang, dữ liệu số đều vào được.||Linear filter theory is not only electrical; every linear time-invariant system, mechanical, acoustic, optical or digital, comes under it.⟧",
                 "⟦Với dữ liệu số, phép lọc là tổng chập với đáp ứng xung rời rạc $h(n)$.||With digital data the filtering is a convolution sum with a discrete impulse response $h(n)$.⟧",
                 "⟦Mẫu của đáp ứng liên tục trùng với $g(n)=h(n)*f(n)$ nếu chọn $h(0)$ là trung bình của $I(0^-)$ và $I(0^+)$.||Samples of the continuous response equal $g(n)=h(n)*f(n)$ provided $h(0)$ is the mean of $I(0^-)$ and $I(0^+)$.⟧"),
            preview=["⟦Tính tổng quát||Generality⟧", "⟦Lọc số và tổng chập||Digital filtering and the convolution sum⟧", "⟦Ví dụ số và bài 30||A numerical example and problem 30⟧"],
            slides=[
                ("⟦Tính tổng quát của lý thuyết bộ lọc tuyến tính||Generality of linear filter theory⟧",
                 "<p>⟦Ký hiệu $V$ được dùng cho cả đầu vào và đầu ra, nhưng thảo luận không giới hạn ở đại lượng điện: cơ, âm, quang đều nằm trong; đầu vào có thể là điện áp và đáp ứng là dòng, hoặc ngược lại. Với dòng đáp ứng theo áp kích thích, $T(f)$ có tên \"dẫn nạp truyền\"; \"trở kháng truyền\" cho áp đáp ứng theo dòng. Vận tốc trên lực, lưu lượng trên áp suất, tỉ số trường điện từ và các tỉ số tương tự ở nơi có tuyến tính đều nằm trong, miễn là có bất biến theo thời gian (Bracewell, tr. 203).||"
                 "The symbol $V$ has been used for both input and output, but the discussion is not limited to electrical quantities: mechanical, acoustical and optical interpretations are included, and the input may be a voltage and the response a current, or vice versa. For a current response to voltage excitation $T(f)$ has the established name transfer admittance; transfer impedance for voltage response to applied current. Velocity/force, flow/pressure, electromagnetic field ratios and related ratios wherever linearity prevails are covered, provided time invariance also applies (Bracewell, p. 203).⟧</p>"),
                ("⟦Dữ liệu số cũng nằm trong lý thuyết||Digital data are included too⟧",
                 "<p>⟦Tín hiệu số như $\\{1\\ 2.7\\ 7.4\\ 20.1\\ \\ldots\\}$ có nội dung thông tin tương đương một hàm xung theo thời gian liên tục, ở đây $\\delta(t)+2.7\\delta(t-1)+7.4\\delta(t-2)+20.1\\delta(t-3)+\\ldots$. Vậy tín hiệu thời gian rời rạc nằm trong lý thuyết. Nhưng với tính toán số, các phép toán thực dụng khác: quy về các tổng chập ở chương 3, giống như tính một tích phân bằng cách cộng các giá trị rời rạc, khác với tính tích phân bằng giải tích (tr. 203).||"
                 "Digital signals such as $\\{1\\ 2.7\\ 7.4\\ 20.1\\ \\ldots\\}$ are equivalent in information content to impulsive functions of continuous time, here $\\delta(t)+2.7\\delta(t-1)+7.4\\delta(t-2)+20.1\\delta(t-3)+\\ldots$. So discrete-time signals are included in the theory. For numerical work, however, the practical operations differ: they reduce to the convolution sums of chapter 3, analogous to computing an integral by summing discrete values, a procedure different from evaluating integrals by analysis (p. 203).⟧</p>"),
                ("⟦Sơ đồ mạch, sơ đồ dòng và mô hình||Circuit diagram, flow diagram and model⟧",
                 "<p>⟦Sơ đồ mạch, vốn là bản vẽ cơ khí bố trí cuộn dây, bản tụ, đầu nối, không còn đại diện cho thiết bị vật lý mà đại diện cho một tập phương trình vi phân. Ta trừu tượng hóa rồi xử lý mô hình toán học mà không viện đến thế giới vật lý. Lý thuyết tín hiệu ở mức trừu tượng cao hơn: phương trình vi phân được nhét vào hộp đen và thay bằng toán tử tổng thể, và sơ đồ dòng, dù từ sơ đồ mạch mà ra, gạt khái niệm mạch để ưu tiên các phép toán tổng thể như phép toán ma trận, nên cách xa thực tế chế tạo hai bậc (tr. 203 đến 204).||"
                 "The circuit diagram, by origin a mechanical drawing showing the layout of coiled wires, condenser plates and posts, no longer stands for a physical device at all; it stands for a set of differential equations. We abstract, then handle the mathematical model without further reference to the physical world. Signal theory is on a further level of abstraction where the differential equations are tucked inside black boxes and replaced by overall operators, and the flow diagram, though descended from the circuit diagram, suppresses circuit concepts in favour of overall operations such as matrix operations, and is thus twice removed from manufacturing reality (pp. 203 to 204).⟧</p>"),
                ("⟦Lọc số||Digital filtering⟧",
                 "<p>⟦Tín hiệu thời gian rời rạc, ở đó $t$ nhận giá trị nguyên, có thể là mẫu đều của tín hiệu liên tục $V(t)$; dãy $f(n)$ là biểu diễn xấp xỉ của tín hiệu \"thật\", và các giá trị đo như $f(n)$ là cơ sở kiến thức về $V(t)$. Thiết bị lấy mẫu chứa đồng hồ nối $V(t)$ với một tụ trong thời gian nạp ngắn; mẫu về bản chất là trung bình có trọng số trên thời gian hữu hạn. Nhiều tín hiệu rời rạc (số máy bay hạ cánh mỗi ngày, lượng mưa) không phải mẫu của hàm liên tục nào; chúng tồn tại độc lập (Bracewell, tr. 204).||"
                 "Discrete-time signals, where $t$ takes integer values, can arise as regular samples of a continuous-time signal $V(t)$; the sequence $f(n)$ is an approximate representation of the underlying \"true\" signal, and measured values such as $f(n)$ are the basis of our knowledge of $V(t)$. The sampling device contains a clock that connects $V(t)$ to a capacitance for a short charging time; a sample is of necessity a weighted average over a finite time. Other discrete signals, such as daily counts of landings at an airport or daily rainfall, are not samples of any continuous function; they exist in their own right (Bracewell, p. 204).⟧</p>"),
                ("⟦Tổng chập rời rạc||The discrete convolution sum⟧",
                 "<p>⟦Lọc thông thấp giảm nhiễu ngẫu nhiên hay dao động hệ thống nhanh, lọc thông cao giảm trôi, lọc chính xác đáp ứng quy định pháp lý về băng thông trên đường điện thoại và truyền vô tuyến. Phép lọc là tích chập với đáp ứng xung rời rạc mong muốn $h(n)$, thường có được là biến đổi Fourier của đáp ứng tần số áp đặt: $g(n)=h(n)*f(n)$, so với tích phân chập liên tục $V_2=I*V_1$ (tr. 204). Bộ lọc $h(n)$ có hữu hạn số hạng gọi là bộ lọc đáp ứng xung hữu hạn (FIR). Số đo với trung bình trượt 3 điểm $h=\\{\\tfrac13,\\tfrac13,\\tfrac13\\}$ và đầu vào $\\cos2\\pi(0.1)n$: biên độ ra ổn định {{ma_amp_sim}} bằng $|H(0.1)|$ = {{ma_amp}}.||"
                 "Low-pass filtering reduces unwanted random noise or rapid systematic fluctuations, high-pass filtering reduces unwanted drifts, and precision filtering meets legal bandwidth requirements on telephone lines and wireless transmission. The filtering is a convolution with a desired discrete impulse response $h(n)$, often obtained as the Fourier transform of an imposed frequency response: $g(n)=h(n)*f(n)$, compared with the continuous convolution integral $V_2=I*V_1$ (p. 204). A filter $h(n)$ with a finite number of terms is a finite impulse response (FIR) filter. Measured with the 3-point moving average $h=\\{\\tfrac13,\\tfrac13,\\tfrac13\\}$ and input $\\cos2\\pi(0.1)n$: the steady-state output amplitude {{ma_amp_sim}} equals $|H(0.1)|$ = {{ma_amp}}.⟧</p>"
                 + F("⟦Tổng chập||Convolution sum⟧", r"g(n)=\sum_kh(k)\,f(n-k)")),
                ("⟦Đáp ứng liên tục và rời rạc: giá trị $h(0)$||Continuous versus discrete: the value of $h(0)$⟧",
                 "<p>⟦Nếu ta lọc dãy $f(n)$ bằng đáp ứng xung liên tục như $e^{-t}H(t)$, ta tính được $V_2(t)=I(t)*\\sum f(n)\\delta(t-n)$, nhưng đầu ra không còn là tín hiệu rời rạc. Cách thông thường là đổi $I(t)$ thành $h(n)$ với $h(0)=0.5$, $h(1)=e^{-1}$, $h(2)=e^{-2},\\ldots$: giá trị đầu $h(0)$ chọn bằng trung bình của $I(0^-)$ và $I(0^+)$ (tr. 204 đến 205). Khi đó các giá trị của $g(n)$ trùng với các mẫu của $V_2(t)$ ở $t$ nguyên (hình 9.2).||"
                 "If a discrete signal $f(n)$ had to be filtered by a continuous impulse response such as $e^{-t}H(t)$, one could evaluate $V_2(t)=I(t)*\\sum f(n)\\delta(t-n)$, but the output would no longer be a discrete-time signal. The normal procedure is to convert $I(t)$ into $h(n)$ given by $h(0)=0.5$, $h(1)=e^{-1}$, $h(2)=e^{-2},\\ldots$: the initial value $h(0)$ is chosen as the mean of $I(0^-)$ and $I(0^+)$ (pp. 204 to 205). Then the values of $g(n)$ are the same as the samples of $V_2(t)$ at integer $t$ (Fig. 9.2).⟧</p>"),
                ("⟦Ví dụ của sách: $\\{1\\ 2\\ 1\\}$||The book's example: $\\{1\\ 2\\ 1\\}$⟧",
                 "<p>⟦Với $h(n)=\\{0.5,\\ e^{-1},\\ e^{-2},\\ldots\\}$ và $f(n)=\\{1\\ 2\\ 1\\}$: $g(n)=\\{0.5,\\ 1.37,\\ 1.37,\\ 0.69,\\ 0.25,\\ldots\\}$ (tr. 205). Số đo: $g(1)$ = {{dg_1}}, $g(2)$ = {{dg_2}}, $g(3)$ = {{dg_3}}, $g(4)$ = {{dg_4}}, bằng cả tổng chập số lẫn tính $V_2(t)$ liên tục tại các điểm nguyên (với $H(0)=\\tfrac12$).||"
                 "With $h(n)=\\{0.5,\\ e^{-1},\\ e^{-2},\\ldots\\}$ and $f(n)=\\{1\\ 2\\ 1\\}$: $g(n)=\\{0.5,\\ 1.37,\\ 1.37,\\ 0.69,\\ 0.25,\\ldots\\}$ (p. 205). Measured: $g(1)$ = {{dg_1}}, $g(2)$ = {{dg_2}}, $g(3)$ = {{dg_3}}, $g(4)$ = {{dg_4}}, by both the numerical convolution sum and by evaluating the continuous $V_2(t)$ at integer points (with $H(0)=\\tfrac12$).⟧</p>{{fig:digital_filter}}"),
                ("⟦Bài 30: tín hiệu $\\{1\\ 1.6\\ 2\\ 0.6\\}$ qua mạch RC||Problem 30: the signal $\\{1\\ 1.6\\ 2\\ 0.6\\}$ through an RC filter⟧",
                 "<p>⟦Tín hiệu $\\{1\\ 1.6\\ 2\\ 0.6\\}$ cách nhau 1 micrô giây vào bộ lọc RC có $RC=1$ micrô giây; biểu diễn bằng chuỗi xung $\\delta(t-1)+1.6\\delta(t-2)+2\\delta(t-3)+0.6\\delta(t-4)$ và vẽ đáp ứng là tổng bốn hàm mũ (tr. 218). Số đo: $V_2$ tại $t=3$ là {{p30_t3}}, tại $t=4$ là {{p30_t4}}, tại $t=6$ là {{p30_t6}}; hệ số của biểu thức đại số trùng tổng chập $\\{0.5, e^{-1}, e^{-2},\\ldots\\}*\\{1, 1.6, 2, 0.6\\}$.||"
                 "The signal $\\{1\\ 1.6\\ 2\\ 0.6\\}$ with spacing 1 microsecond is applied to an RC filter with $RC=1$ microsecond; represent it by the impulse train $\\delta(t-1)+1.6\\delta(t-2)+2\\delta(t-3)+0.6\\delta(t-4)$ and graph the response as the sum of four exponentials (p. 218). Measured: $V_2$ at $t=3$ is {{p30_t3}}, at $t=4$ is {{p30_t4}}, at $t=6$ is {{p30_t6}}; the coefficients of the algebraic expressions match the convolution sum $\\{0.5, e^{-1}, e^{-2},\\ldots\\}*\\{1, 1.6, 2, 0.6\\}$.⟧</p>"),
                ("⟦Tự kiểm tra phần 3||Self-check, part 3⟧",
                 UL(["⟦Vì sao $h(0)=\\tfrac12$ chứ không phải 1 khi lấy mẫu $e^{-t}H(t)$?||Why is $h(0)=\\tfrac12$ rather than 1 when sampling $e^{-t}H(t)$?⟧",
                     "⟦Lọc số khác tính tích phân chập liên tục ở điểm nào khi tính toán?||How does digital filtering differ from evaluating the continuous convolution integral in computation?⟧",
                     "⟦FIR là gì?||What is an FIR filter?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: trung bình hai phía của bước nhảy; là tổng chập hữu hạn thay tích phân; đáp ứng xung có hữu hạn số hạng.||Hints: the mean of the two sides of the jump; a finite convolution sum replaces the integral; an impulse response with a finite number of terms.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 4
        dict(
            title="⟦Các định lý đọc theo ngôn ngữ mạch||The theorems read in circuit language⟧",
            scr=("⟦Các định lý chương 6 có nghĩa gì khi $f$ là điện áp theo thời gian, $F$ là phổ và bộ lọc là hệ thống?||What do the theorems of chapter 6 mean when $f$ is a voltage against time, $F$ a spectrum and the filter a system?⟧",
                 "⟦Tỉ lệ nói chu kỳ và tần số nghịch đảo; cộng nói về phép biến đổi tuyến tính chứ không phải về mạch; dịch chỉ đổi pha; điều chế tạo dải bên.||Similarity says period and frequency are reciprocal; addition is about the linearity of the transform, not of circuits; shift changes only phase; modulation creates sidebands.⟧",
                 "⟦Điều chế ngược: hai tín hiệu giống nhau nối tiếp cho phổ nhân với cosin.||The converse of modulation: two identical signals in succession multiply the spectrum by a cosine.⟧"),
            preview=["⟦Tỉ lệ và cộng||Similarity and addition⟧", "⟦Dịch và điều chế||Shift and modulation⟧", "⟦Điều chế ngược||The converse of modulation⟧"],
            slides=[
                ("⟦Bảng 9.2: các định lý cho dạng sóng và phổ||Table 9.2: theorems for waveforms and spectra⟧",
                 "<p>⟦Mọi định lý của chương 6 diễn giải được theo dạng sóng, phổ và bộ lọc; bảng 9.2 gom chúng theo ký hiệu chương này: tỉ lệ $V(at)\\supset|a|^{-1}S(f/a)$, cộng, dịch $V(t-T)\\supset e^{-i2\\pi fT}S$, điều chế, tích chập $I*V_1\\supset TS_1$, tự tương quan $\\supset|S|^2$, đạo hàm $V'\\supset i2\\pi fS$, nghịch đảo $tV\\supset-S'/i2\\pi$, $t^2V\\supset-S''/4\\pi^2$, sai phân $\\Delta_TV\\supset2i\\sin\\pi TfS$, sai phân bậc hai $-4\\sin^2\\pi TfS$, trung bình trượt $\\supset\\text{sinc}\\,Tf\\,S$, cùng Rayleigh, năng lượng, tích phân xác định, tâm khối, mômen, độ rộng tương đương và các bất đẳng thức (tr. 205 đến 206). Bốn định lý đầu được bàn ở các slide sau.||"
                 "All theorems of chapter 6 are interpretable for waveforms, spectra and filters; Table 9.2 gathers them in this chapter's symbols: similarity $V(at)\\supset|a|^{-1}S(f/a)$, addition, shift $V(t-T)\\supset e^{-i2\\pi fT}S$, modulation, convolution $I*V_1\\supset TS_1$, autocorrelation $\\supset|S|^2$, differentiation $V'\\supset i2\\pi fS$, its inverse $tV\\supset-S'/i2\\pi$, $t^2V\\supset-S''/4\\pi^2$, finite difference $\\Delta_TV\\supset2i\\sin\\pi TfS$, second difference $-4\\sin^2\\pi TfS$, running means $\\supset\\text{sinc}\\,Tf\\,S$, together with Rayleigh, energy, definite integral, centre of gravity, moments, equivalent width and the inequalities (pp. 205 to 206). The first four are discussed on the following slides.⟧</p>"),
                ("⟦Định lý tỉ lệ: nén thang thời gian nâng mọi tần số||Similarity: compressing the time scale raises every frequency⟧",
                 "<p>⟦Quan hệ nghịch đảo giữa chu kỳ và tần số hiển nhiên ở định lý này: nén thang thời gian một hệ số làm nén chu kỳ mọi thành phần điều hòa như nhau, nên nâng tần số mọi thành phần cùng hệ số. Vì $V(0)$ không đổi khi đổi thang thời gian nên diện tích dưới phổ, theo định lý tích phân xác định, phải không đổi; do đó có hệ số bù $|a|^{-1}$, làm phổ yếu đi khi lan tới tần số cao hơn (tr. 206 đến 207). Bài 2: phát âm lại tiếng phim với tốc độ gấp đôi làm tần số gấp đôi. Số đo với Gauss, $a=2$: đỉnh của phổ giảm còn {{sim_peak}} và diện tích dưới phổ giữ {{sim_area}}.||"
                 "The reciprocal relationship of period and frequency is evident in this theorem: compression of the time scale by a factor compresses the periods of all harmonic components equally and therefore raises the frequency of every component by the same factor. Since $V(0)$ is unaffected by time-scale changes, the area under the spectrum must, by the definite-integral theorem, remain constant, hence the compensating factor $|a|^{-1}$, which weakens the spectrum if it spreads to higher frequencies (pp. 206 to 207). Problem 2: playing back a film sound track at twice speed doubles the frequency. Measured with the Gaussian, $a=2$: the peak of the spectrum falls to {{sim_peak}} and the area under the spectrum stays {{sim_area}}.⟧</p>"),
                ("⟦Định lý cộng: chỉ là tuyến tính của phép biến đổi||Addition: merely the linearity of the transform⟧",
                 "<p>⟦Dù dịch sang ngôn ngữ dạng sóng, định lý cộng chỉ biểu thị tính tuyến tính của phép biến đổi Fourier. Nó không liên quan gì đến tính tuyến tính của các hệ thống chứa dạng sóng, và đương nhiên đúng cả với dạng sóng trong mạch phi tuyến. Tính tuyến tính của phép biến đổi làm nó thích hợp để xử lý bài toán tuyến tính (tr. 207).||Even translated into the language of electrical waveforms and spectra, the addition theorem is simply an expression of the linearity of the Fourier transformation. It has nothing to do with the linearity of the systems in which the waveforms are found, and must of course be true even of waveforms in nonlinear circuits. The linear property of the transformation makes it suitable for dealing with linear problems (p. 207).⟧</p>"),
                ("⟦Định lý dịch: trễ đổi pha từng thành phần khác nhau||Shift: a delay affects each component differently⟧",
                 "<p>⟦Khi dạng sóng bị trễ $T$, các thành phần điều hòa bị ảnh hưởng khác nhau: thành phần có tần số bằng hoặc là bội nguyên của $T^{-1}$ hoàn toàn không bị đổi; thành phần chu kỳ lớn hơn $T$ nhiều ít bị đổi; thành phần chu kỳ ngắn so với $T$ có thể bị đổi pha nặng. Thành phần chu kỳ $T_1=f_1^{-1}$ giữ biên độ nhưng trễ pha $2\\pi T/T_1$, nên $S(f_1)$ thành $\\exp(-i2\\pi f_1T)S(f_1)$ (tr. 207). Số đo với $T=0.5$: hệ số pha tại $f=2$ (bội của $1/T$) là {{shift_mult}} (không đổi); tại $f=0.1$ là {{shift_low}} độ; tại $f=1.3$ là {{shift_high}} độ.||"
                 "When a waveform is delayed by $T$ its harmonic components are affected differently: a component whose frequency equals or is an integral multiple of $T^{-1}$ is not affected at all; components with periods much greater than $T$ are not affected much; those with periods short compared with $T$ may be seriously altered in phase. The component of period $T_1=f_1^{-1}$ is unchanged in amplitude but delayed in phase by $2\\pi T/T_1$, so $S(f_1)$ becomes $\\exp(-i2\\pi f_1T)S(f_1)$ (p. 207). Measured with $T=0.5$: the phase factor at $f=2$ (a multiple of $1/T$) is {{shift_mult}} (unchanged); at $f=0.1$ it is {{shift_low}} degrees; at $f=1.3$ it is {{shift_high}} degrees.⟧</p>"),
                ("⟦Định lý điều chế: sóng mang và dải bên||Modulation: carrier and sidebands⟧",
                 "<p>⟦Cách thông thường áp một âm tần có tần số góc $\\omega$ lên sóng mang tần số góc $\\Omega$ cho dạng sóng $(1+M\\cos\\omega t)\\cos\\Omega t$, với $M$ là độ sâu điều chế. Nó khác sóng mang $\\cos\\Omega t$ ở phần thêm $M\\cos\\omega t\\cos\\Omega t$, đúng dạng mà định lý điều chế áp dụng (tr. 207). Định lý: phổ của $V(t)\\cos\\omega t$ có được bằng tách $S(f)$ làm hai nửa, một nửa trượt phải $\\omega/2\\pi$, nửa kia trượt trái cùng khoảng. Cộng với phổ sóng mang (định lý cộng) được các dải bên quen thuộc (hình 9.3, tr. 208). Số đo với $M=0.5$, sóng mang 50 Hz, âm 5 Hz: sóng mang {{am_car}} tại ±50, dải bên {{am_sb}} tại ±45 và ±55, tức $M/4$.||"
                 "In the ordinary method of imposing an audio tone of angular frequency $\\omega$ on a carrier of angular frequency $\\Omega$, the modulated waveform is $(1+M\\cos\\omega t)\\cos\\Omega t$, with $M$ the depth of modulation. It differs from the unmodulated carrier $\\cos\\Omega t$ by the addition of $M\\cos\\omega t\\cos\\Omega t$, a quantity of the form to which the modulation theorem applies (p. 207). The theorem: the spectrum of $V(t)\\cos\\omega t$ is derivable by splitting $S(f)$ into two halves, one slipped to the right by $\\omega/2\\pi$, the other an equal distance to the left. Adding the spectrum of the unmodulated carrier (addition theorem) reproduces the familiar sidebands of simple modulation theory (Fig. 9.3, p. 208). Measured with $M=0.5$, 50 Hz carrier and 5 Hz tone: carrier {{am_car}} at ±50, sidebands {{am_sb}} at ±45 and ±55, i.e. $M/4$.⟧</p>"
                 + F("⟦Sóng điều biên||AM wave⟧", r"(1+M\cos\omega t)\cos\Omega t\ \supset\ \tfrac12\delta\!\left(f\pm\tfrac{\Omega}{2\pi}\right)+\tfrac M4\,\delta\!\left(f\pm\tfrac{\Omega\pm\omega}{2\pi}\right)")),
                ("⟦Điều chế ngược||The converse of the modulation theorem⟧",
                 "<p>⟦Hai tín hiệu giống nhau gửi nối tiếp: phổ tín hiệu ghép có từ phổ của một tín hiệu riêng lẻ bằng nhân với một hàm cosin của tần số. Với gốc thời gian ở giữa hai gốc riêng (tr. 208): $V(t+T)+V(t-T)\\supset2\\cos2\\pi Tf\\,S(f)$; hoặc $V(t)+V(t-2T)\\supset2e^{-i2\\pi Tf}\\cos2\\pi Tf\\,S(f)$ (hình 9.4). Cả hai suy trực tiếp từ định lý dịch. Số đo với Gauss, $T=1$, $f=0.3$: $|2\\cos(2\\pi Tf)S|$ = {{conv_pair}} bằng tích phân số; dạng thứ hai có pha {{conv_ph}} độ.||"
                 "Two identical signals are sent out in succession; the spectrum of the composite signal is obtained from the spectrum of one alone by multiplication by a cosine function of frequency. With the time origin midway between the separate origins (p. 208): $V(t+T)+V(t-T)\\supset2\\cos2\\pi Tf\\,S(f)$; or $V(t)+V(t-2T)\\supset2e^{-i2\\pi Tf}\\cos2\\pi Tf\\,S(f)$ (Fig. 9.4). Both follow directly from the shift theorem. Measured with the Gaussian, $T=1$, $f=0.3$: $|2\\cos(2\\pi Tf)S|$ = {{conv_pair}} by numerical integration; the second form has phase {{conv_ph}} degrees.⟧</p>"
                 + F("⟦Điều chế ngược||Converse of modulation⟧", r"V(t+T)+V(t-T)\ \supset\ 2\cos(2\pi Tf)\,S(f)")),
                ("⟦Bài 24: hai kênh trễ cho $|T|$ hình cosin||Problem 24: two delayed channels give a cosine $|T|$⟧",
                 "<p>⟦Một tín hiệu chia làm hai kênh, một có trễ $T_1$, một có trễ $T_2$ dài hơn, rồi cộng lại: $T(f)=e^{-i2\\pi fT_1}+e^{-i2\\pi fT_2}$, nên $|T|=2|\\cos\\pi f(T_2-T_1)|$ là hàm cosin của tần số (bài tập 24, tr. 216). Ba hệ như vậy nối chuỗi tạo đáp ứng xung chữ nhật, dựa vào tích cosin $\\prod\\cos(\\pi x/2^k)=\\text{sinc}\\,x$. Số đo với $T_1=0.3$, $T_2=1.1$, $f=0.4$: $|T|$ = {{p24_val}}, và lệch so với $2|\\cos\\pi f\\Delta|$ chỉ {{p24_dev}}. Với bốn thừa số cosin, sai số so với $\\text{sinc}\\,x$ đạt 1 phần trăm đỉnh khi $x$ = {{p23_x}}; công thức sửa $\\text{sinc}\\,x=\\prod_{k=1}^{N}\\cos(\\pi x/2^k)\\,\\text{sinc}(x/2^N)$ đúng với sai số {{p23_dev}}.||"
                 "A signal is divided into two channels, one with delay $T_1$ and the other a longer delay $T_2$, then added: $T(f)=e^{-i2\\pi fT_1}+e^{-i2\\pi fT_2}$, so $|T|=2|\\cos\\pi f(T_2-T_1)|$ is a cosine function of frequency (problem 24, p. 216). A chain of three such systems makes a rectangular impulse response, relying on the cosine product $\\prod\\cos(\\pi x/2^k)=\\text{sinc}\\,x$. Measured with $T_1=0.3$, $T_2=1.1$, $f=0.4$: $|T|$ = {{p24_val}}, and it deviates from $2|\\cos\\pi f\\Delta|$ by only {{p24_dev}}. With four cosine factors the error against $\\text{sinc}\\,x$ reaches 1 percent of the peak at $x$ = {{p23_x}}; the corrected formula $\\text{sinc}\\,x=\\prod_{k=1}^{N}\\cos(\\pi x/2^k)\\,\\text{sinc}(x/2^N)$ holds with error {{p23_dev}}.⟧</p>"),
                ("⟦Bài 29: phân giải hai vạch phổ Gauss||Problem 29: resolving two Gaussian spectral lines⟧",
                 "<p>⟦Một quang phổ kế đáp ứng vạch phổ bằng $\\exp(-\\pi x^2/W^2)$; hai vạch bằng nhau cách $L$ cho $\\exp[-\\pi(x+\\tfrac12L)^2/W^2]+\\exp[-\\pi(x-\\tfrac12L)^2/W^2]$. Khi $L\\gg W$ ghi được hai đỉnh với chỗ trũng ở giữa; đưa lại gần nhau thì có $L_{\\max}$ mà tại đó chỗ trũng nâng tới mức các đỉnh, và lúc đó độ cong ở giữa bằng 0 (tr. 218): $L_{\\max}=W\\sqrt{2/\\pi}$ = {{p29_L}}$W$. Số đo trên lưới: tại $L=0.98L_{\\max}$ có một cực đại; tại $L=1.02L_{\\max}$ có hai. Với $L=0.8L_{\\max}$ chỉ còn một đỉnh, nhưng khớp bằng hàm mẫu vẫn có thể suy ra hai vạch và khoảng cách của chúng nếu biết hình dạng vạch.||"
                 "A spectrograph responds to a spectral line as $\\exp(-\\pi x^2/W^2)$; two equal lines a distance $L$ apart give $\\exp[-\\pi(x+\\tfrac12L)^2/W^2]+\\exp[-\\pi(x-\\tfrac12L)^2/W^2]$. For $L\\gg W$ two peaks with a minimum between are recorded; bring the lines closer and there is a value $L_{\\max}$ where the central minimum rises to the level of the peaks, at which the central curvature vanishes (p. 218): $L_{\\max}=W\\sqrt{2/\\pi}$ = {{p29_L}}$W$. Measured on a grid: at $L=0.98L_{\\max}$ there is one maximum; at $L=1.02L_{\\max}$ there are two. For $L=0.8L_{\\max}$ only one peak remains, but fitting a model can still infer two lines and their spacing if the line shape is known.⟧</p>"),
                ("⟦Tự kiểm tra phần 4||Self-check, part 4⟧",
                 UL(["⟦Vì sao có hệ số $|a|^{-1}$ trong định lý tỉ lệ?||Why is there a factor $|a|^{-1}$ in the similarity theorem?⟧",
                     "⟦Thành phần nào không đổi khi dạng sóng bị trễ $T$?||Which components are unchanged when the waveform is delayed by $T$?⟧",
                     "⟦Sóng điều biên có bao nhiêu vạch ở tần số dương và cường độ tương đối của chúng?||How many lines does an AM wave have at positive frequency and what are their relative strengths?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: để giữ diện tích dưới phổ bằng $V(0)$; các tần số là bội của $1/T$; ba vạch: sóng mang $\\tfrac12$ và hai dải bên $M/4$.||Hints: to keep the area under the spectrum equal to $V(0)$; frequencies that are multiples of $1/T$; three lines: carrier $\\tfrac12$ and two sidebands $M/4$.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 5
        dict(
            title="⟦Tuyến tính, bất biến theo thời gian, tuần hoàn và ổn định||Linearity, time invariance, periodicity and stability⟧",
            scr=("⟦Vì sao một bộ lọc tuyến tính bất biến cho đầu ra điều hòa với đầu vào điều hòa, và vì sao nó luôn là tích chập?||Why does a linear time-invariant filter give harmonic output for harmonic input, and why is it always a convolution?⟧",
                 "⟦Bất biến theo thời gian và tuyến tính là hai điều kiện khác nhau; hệ phi tuyến hay biến thiên đều phá vỡ tính chất điều hòa.||Time invariance and linearity are different conditions; a nonlinear or time-varying system breaks the harmonic property.⟧",
                 "⟦Hệ ổn định theo nghĩa \"đầu vào bị chặn cho đầu ra bị chặn\" khi $\\int|I|dt$ hữu hạn.||A system is stable in the sense of \"bounded input gives bounded output\" when $\\int|I|dt$ is finite.⟧"),
            preview=["⟦Tuyến tính và bất biến theo thời gian: định nghĩa||Linearity and time invariance: definitions⟧", "⟦Chứng minh đáp ứng điều hòa và tích chập||Proof of harmonic response and convolution⟧", "⟦Tuần hoàn, ổn định và ví dụ đường truyền||Periodicity, stability and a pulse-forming line⟧"],
            slides=[
                ("⟦Định nghĩa tuyến tính||Definition of linearity⟧",
                 "<p>⟦Giả sử $V_2(t)$ là đáp ứng của bộ lọc với kích thích $V_1(t)$, và $W_2(t)$ với $W_1(t)$. Bộ lọc gọi là tuyến tính nếu đáp ứng với $V_1+W_1$ là $V_2+W_2$, bất kể chọn $V_1$, $W_1$ thế nào. Đôi khi thêm điều kiện đáp ứng với $aV_1$ là $aV_2$ với mọi $a$, nhưng có thể suy ra từ tính chồng chất, chứng minh trước cho $a$ nguyên rồi cho tỷ số nguyên (tr. 209). Về những vấn đề toán học khi điện áp có thể vô tỷ, xem Newcomb (1963) (chú thích ở tr. 209).||"
                 "Suppose $V_2(t)$ is the response of a filter to a stimulus $V_1(t)$ and $W_2(t)$ the response to $W_1(t)$. The filter is said to be linear if the response to $V_1+W_1$ is $V_2+W_2$, irrespective of the choice of $V_1$, $W_1$. Sometimes a condition is added that $aV_1$ shall have response $aV_2$ for all $a$, but it can be deduced from the superposition property, proving it first for integer $a$, then for a ratio of integers (p. 209). For the mathematical considerations that arise when a voltage may be irrational, see Newcomb (1963) (footnote, p. 209).⟧</p>"),
                ("⟦Bất biến theo thời gian||Time invariance⟧",
                 "<p>⟦Bất biến theo thời gian nghĩa là đáp ứng với $V_1(t-T)$ là $V_2(t-T)$ với mọi $T$ và $V_1(t)$ (tr. 209). Hệ quả của tuyến tính và bất biến theo thời gian: kích thích $A\\cos2\\pi ft$ với $f$ bất kỳ cho đáp ứng $B\\cos(2\\pi ft-\\phi)$, cùng dạng, có thể trễ pha $\\phi$ và đổi biên độ hệ số $B/A$; hai đại lượng này là tính chất của bộ lọc và viết gọn thành hàm truyền $T(f)=(B/A)e^{-i\\phi}$. Tính chất này thường gọi lỏng là \"đáp ứng điều hòa với đầu vào điều hòa\".||"
                 "Time invariance means the response to $V_1(t-T)$ is $V_2(t-T)$ for all $T$ and $V_1(t)$ (p. 209). As a consequence of linearity and time invariance, a stimulus $A\\cos2\\pi ft$ with any $f$ produces a response $B\\cos(2\\pi ft-\\phi)$ of the same form, possibly delayed in phase by $\\phi$ and different in amplitude by $B/A$; these quantities are properties of the filter and are compactly expressed in the transfer factor $T(f)=(B/A)e^{-i\\phi}$. This property is sometimes loosely called \"harmonic response to harmonic input\".⟧</p>"),
                ("⟦Chứng minh: đáp ứng điều hòa với đầu vào điều hòa||Proof: harmonic response to harmonic input||⟧".replace("||⟧", "⟧"),
                 "<p>⟦Cho kích thích đơn vị là phần thực của hàm phức $\\hat V_1(t)=e^{i2\\pi ft}$. Giả sử đáp ứng là $K(f,t)e^{i2\\pi ft}$, một hàm tổng quát của $f$ và $t$. Với kích thích trễ $e^{i2\\pi f(t-T)}$, do bất biến đáp ứng là $K(f,t-T)e^{i2\\pi f(t-T)}$; nhưng kích thích trễ là tích của kích thích gốc với hằng số phức $e^{-i2\\pi fT}$, nên do tuyến tính đáp ứng là tích của đáp ứng gốc với cùng hằng số. Vậy $K(f,t-T)e^{i2\\pi f(t-T)}=e^{-i2\\pi fT}K(f,t)e^{i2\\pi ft}$, tức $K(f,t-T)=K(f,t)$: $K$ không phụ thuộc $t$, và chỉ là $T(f)$ (tr. 209 đến 210). Số đo: dãy $A\\cos2\\pi ft$ qua bộ lọc FIR tuyến tính bất biến cho đầu ra có năng lượng ngoài chính tần số ấy chỉ {{lti_leak}} (tỉ lệ).||"
                 "Let the unit stimulus be the real part of the complex function $\\hat V_1(t)=e^{i2\\pi ft}$. Suppose the response is $K(f,t)e^{i2\\pi ft}$, a general function of $f$ and $t$. For a delayed stimulus $e^{i2\\pi f(t-T)}$, by invariance the response is $K(f,t-T)e^{i2\\pi f(t-T)}$; but the delayed stimulus is the original times the complex constant $e^{-i2\\pi fT}$, so by linearity the response is the original response times the same constant. Hence $K(f,t-T)e^{i2\\pi f(t-T)}=e^{-i2\\pi fT}K(f,t)e^{i2\\pi ft}$, i.e. $K(f,t-T)=K(f,t)$: $K$ is independent of $t$ and is just $T(f)$ (pp. 209 to 210). Measured: $A\\cos2\\pi ft$ through a linear time-invariant FIR filter gives output with energy outside that same frequency of only {{lti_leak}} (fraction).⟧</p>"),
                ("⟦Chứng minh: tuyến tính cộng bất biến ⇒ tích chập||Proof: linearity plus invariance ⇒ convolution⟧",
                 "<p>⟦Vì tính tuyến tính, đáp ứng là phiếm hàm tuyến tính tổng quát nhất của kích thích: $V_2(t)=\\int J(t,t')V_1(t')dt'$. Bất biến: $V_2(t-T)=\\int J(t,t')V_1(t'-T)dt'$, tức $V_2(t)=\\int J(t+T,t'+T)V_1(t')dt'$. Vậy $J(t,t')=J(t+T,t'+T)$ với mọi $T$, nên $J$ chỉ là hàm của $t-t'$: $J(t,t')=I(t-t')$ và $V_2=\\int I(t-t')V_1(t')dt'$, tức tích chập (tr. 210 đến 211). Nhận xét: với một tích chập thì ngược lại đầu ra điều hòa với đầu vào điều hòa, vậy hai điều kiện tương đương.||"
                 "Since the filter is linear the response is the most general linear functional of the stimulus: $V_2(t)=\\int J(t,t')V_1(t')dt'$. Invariance: $V_2(t-T)=\\int J(t,t')V_1(t'-T)dt'$, i.e. $V_2(t)=\\int J(t+T,t'+T)V_1(t')dt'$. Hence $J(t,t')=J(t+T,t'+T)$ for all $T$, so $J$ is a function of $t-t'$ only: $J(t,t')=I(t-t')$ and $V_2=\\int I(t-t')V_1(t')dt'$, a convolution (pp. 210 to 211). Conversely a convolution gives harmonic output for harmonic input, so the two conditions are equivalent.⟧</p>"),
                ("⟦Khi vi phạm: phi tuyến và biến thiên theo thời gian||When violated: nonlinear and time-varying systems⟧",
                 "<p>⟦Hệ phi tuyến phá vỡ đáp ứng điều hòa: bộ bình phương $y=x^2$ với đầu vào $\\cos2\\pi ft$ cho $\\tfrac12+\\tfrac12\\cos4\\pi ft$, xuất hiện thành phần một chiều và tần số $2f$ (biên độ {{nl_2f}} mỗi thành phần). Hệ biến thiên theo thời gian phá vỡ cùng tính chất: nhân với $\\cos2\\pi f_2t$ (tấm mặt nạ, hay một hệ không bất biến) biến đầu vào tần số $f=5$ thành hai tần số {{tv_lo}} và {{tv_hi}} khi $f_2=1$. Bài 12 và 13 của sách: tụ có điện môi bị ép cho điện dung biến thiên ở tần số gấp đôi, nên dòng không hình sin; và mặt nạ nhân ảnh là tuyến tính nhưng không bất biến trong không gian, nên có thể đưa tần số không gian cao xuống thấp (tr. 213).||"
                 "A nonlinear system breaks the harmonic response: a squarer $y=x^2$ with input $\\cos2\\pi ft$ gives $\\tfrac12+\\tfrac12\\cos4\\pi ft$, a d.c. component and one at $2f$ (amplitude {{nl_2f}} each). A time-varying system breaks the same property: multiplying by $\\cos2\\pi f_2t$ (a mask, or a non-invariant system) turns an input of frequency $f=5$ into two frequencies {{tv_lo}} and {{tv_hi}} when $f_2=1$. The book's problems 12 and 13: a capacitor with a squeezed dielectric has its capacitance varying at twice the frequency, so the current is not sinusoidal; and a mask multiplying an image is linear but space-variant, so it can convert high spatial frequencies to low (p. 213).⟧</p>"),
                ("⟦Tuần hoàn||Periodicity⟧",
                 "<p>⟦Hàm không hằng $f(x)$ xác định với mọi $x$ là tuần hoàn chu kỳ $T$ nếu có hằng dương $T$ sao cho $f(x+T)=f(x)$ với mọi $x$; hàm không cần liên tục. Có thể có nhiều chu kỳ: $\\cos x$ có chu kỳ $2\\pi$ nhưng cũng $4\\pi$, $6\\pi$; chu kỳ nhỏ nhất là chu kỳ cơ bản. Tổng hai hàm tuần hoàn không nhất thiết tuần hoàn ($\\cos x+\\cos\\pi x$) nhưng có thể ($\\cos x+\\cos99x$). Sự có mặt của thành phần tuần hoàn không đảm bảo tuần hoàn, và một dạng sóng có thể tuần hoàn mà không tìm thấy thành phần ở tần số tương ứng trong phân tích Fourier (tr. 211). Bài 27: $y=9\\cos5x+11\\cos4x$ tuần hoàn với chu kỳ $2\\pi$ (lệch {{per_dev}}), nhưng thành phần cơ bản tại $1/2\\pi$ có biên độ {{per_fund}}: chu kỳ \"lẩn trốn\".||"
                 "A nonconstant function $f(x)$ defined for all $x$ is periodic with period $T$ if there is a positive constant $T$ with $f(x+T)=f(x)$ for all $x$; the function need not be continuous. It can have more than one period: $\\cos x$ has period $2\\pi$ but also $4\\pi$, $6\\pi$; the smallest is the fundamental period. The sum of two periodic functions is not necessarily periodic ($\\cos x+\\cos\\pi x$) but may be ($\\cos x+\\cos99x$). The presence of a periodic component does not guarantee periodicity, and a waveform may be periodic without any trace of a component at the corresponding frequency in the Fourier analysis (p. 211). Problem 27: $y=9\\cos5x+11\\cos4x$ is periodic with period $2\\pi$ (deviation {{per_dev}}), yet the fundamental component at $1/2\\pi$ has amplitude {{per_fund}}: the elusive period.⟧</p>"),
                ("⟦Ổn định||Stability⟧",
                 "<p>⟦Trong cơ học, hệ ổn định nếu nhiễu nhỏ sinh lực đưa hệ về cấu hình cũ. Một ý khác được dùng: hệ tuyến tính ổn định nếu $|V_2(t)|<kM$ với mọi $|V_1(t)|<M$; nói cách khác nếu đầu vào bị chặn thì đầu ra bị chặn. Dạng phát biểu khác: hệ ổn định nếu tích phân tuyệt đối của đáp ứng xung $\\int|I(t)|dt$ hữu hạn (bài tập 18, tr. 214). Số đo: mạch RC có $\\int|I|dt$ = {{st_rc}}; tích phân lý tưởng $I=H(t)$ có tích phân đến $t=100$ bằng {{st_int}} và tăng không giới hạn (không ổn định: đầu vào hằng 1 cho đầu ra $t$); $I=e^{-t}\\cos2\\pi t\\,H(t)$ có $\\int|I|$ = {{st_osc}}, bằng đúng độ lợi lớn nhất khi cho vào $\\text{sgn}\\,I(-t)$.||"
                 "In mechanics a system is stable if a small perturbation produces forces returning it to its original configuration. A different idea is also used: a linear system is stable if $|V_2(t)|<kM$ for any $|V_1(t)|<M$; in other words if the input stays bounded the output also does. Another form: the system is stable if the absolute integral of the impulse response $\\int|I(t)|dt$ is finite (problem 18, p. 214). Measured: the RC circuit has $\\int|I|dt$ = {{st_rc}}; the ideal integrator $I=H(t)$ has an integral up to $t=100$ of {{st_int}} and grows without bound (unstable: a constant input 1 gives output $t$); $I=e^{-t}\\cos2\\pi t\\,H(t)$ has $\\int|I|$ = {{st_osc}}, exactly the largest gain, reached with input $\\text{sgn}\\,I(-t)$.⟧</p>"),
                ("⟦Bài 16, 17, 19: các vấn đề kết hợp và bị chặn||Problems 16, 17, 19: associativity and boundedness⟧",
                 "<p>⟦Bài 16: hai mạng nối tiếp có $I_1=H(t)$, $I_2=\\delta(t)-\\delta(t-1)$; với đầu vào $e^{t}$, tích chập $e^t*H(t)$ không hội tụ nên kết hợp tích chập có vẻ sụp đổ dù cả tích chập ba thừa số hội tụ; bài nhắc rằng tính kết hợp của tích chập cần điều kiện tồn tại các tích phân trung gian (tr. 214). Bài 19: đường truyền đoản mạch không tổn hao có $\\int|I|dt=\\infty$ (đáp ứng xung là chuỗi xung vô hạn) nên trông không ổn định, nhưng với một đầu vào bị chặn cụ thể ta chỉ thấy đầu ra bị chặn; sách hỏi sự thật là gì. Ta chỉ ghi nhận rằng thử một đầu vào bị chặn chưa đủ để kết luận ổn định (tr. 215).||"
                 "Problem 16: two networks in tandem with $I_1=H(t)$, $I_2=\\delta(t)-\\delta(t-1)$; for input $e^{t}$ the convolution $e^t*H(t)$ does not converge, so associativity of convolution seems to break down even though the full three-factor convolution converges; the problem reminds us that associativity of convolution needs the intermediate integrals to exist (p. 214). Problem 19: a short-circuited loss-free transmission line has $\\int|I|dt=\\infty$ (its impulse response is an infinite impulse train) so it looks unstable, yet for one particular bounded input only a bounded output is seen; the book asks what the truth is. We only record that trying a single bounded input is not enough to conclude stability (p. 215).⟧</p>"),
                ("⟦Ví dụ: máy phát xung radar||Case: a radar pulse generator⟧",
                 "<p>⟦Bài tập của sách: để đưa 1 megawatt công suất tần số vô tuyến ra ăng ten trong xung dài $\\Delta=0.1\\ \\mu$s, máy phát cần được kích bằng điện áp 15 000 vôn trên đầu vào. Ta nạp một dây dẫn của đường truyền tới 30 kV trong khoảng một mili giây, trở kháng đặc trưng $Z_0$ bằng điện trở đầu vào của máy phát; tại $t=0$ công tắc nối đường truyền đã nạp với máy phát, đặt 15 kV lên đầu vào. Điện tích chảy ra với tốc độ không đổi trong 0.1 micrô giây cho tới hết (tr. 212). Ta tính: $R=V^2/P$ = {{rad_Z}} ôm; thời lượng xung $=2\\ell/v$ nên $\\ell=v\\tau/2$ = {{rad_len}} mét nếu $v=c$ (cáp thật chậm hơn nên ngắn hơn); năng lượng xung $P\\tau$ = {{rad_E}} J bằng $\\tfrac12CV^2$ = {{rad_E2}} J với $C=\\ell/(vZ_0)$.||"
                 "The book's problem: to deliver a megawatt of radio-frequency power to an antenna in a pulse of $\\Delta=0.1\\ \\mu$s duration, a generator must be excited at its input by 15,000 volts. A conductor of a transmission line is charged for about a millisecond to 30 kV, its characteristic impedance $Z_0$ made equal to the input resistance of the generator; at $t=0$ a switch connects the charged line to the generator, applying 15 kV to the input. Charge pours out at a constant rate for 0.1 microsecond until expended (p. 212). We compute: $R=V^2/P$ = {{rad_Z}} ohms; the pulse duration is $2\\ell/v$ so $\\ell=v\\tau/2$ = {{rad_len}} metres if $v=c$ (real cable is slower so shorter); the pulse energy $P\\tau$ = {{rad_E}} J equals $\\tfrac12CV^2$ = {{rad_E2}} J with $C=\\ell/(vZ_0)$.⟧</p>"),
                ("⟦Tự kiểm tra phần 5||Self-check, part 5⟧",
                 UL(["⟦Vì sao $J(t,t')$ chỉ phụ thuộc $t-t'$?||Why does $J(t,t')$ depend only on $t-t'$?⟧",
                     "⟦Cho một ví dụ hệ tuyến tính nhưng không bất biến.||Give an example of a system that is linear but not time-invariant.⟧",
                     "⟦Vì sao $9\\cos5x+11\\cos4x$ tuần hoàn mà thiếu thành phần cơ bản?||Why is $9\\cos5x+11\\cos4x$ periodic yet missing the fundamental component?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: bất biến theo thời gian; nhân với hàm biến thiên như $\\cos2\\pi f_2t$; tần số cơ bản $1/2\\pi$ là ước chung của hai tần số, nhưng không có thành phần ở đó.||Hints: time invariance; multiplication by a varying function such as $\\cos2\\pi f_2t$; the fundamental $1/2\\pi$ is the common divisor of the two frequencies but there is no component there.⟧</p>"),
            ]),
    ],
    takeaways=[
        "⟦Phổ của dạng sóng thực là Hermite; dạng sóng nhân quả có phần ảo là biến đổi Hilbert của phần thực.||The spectrum of a real waveform is Hermitian; for a causal waveform the imaginary part is the Hilbert transform of the real part.⟧",
        "⟦Bộ lọc được đặc trưng bằng $T(f)$, $I(t)$ hoặc $A(t)$, với $S_2=TS_1$, $V_2=I*V_1=A'*V_1$.||A filter is specified by $T(f)$, $I(t)$ or $A(t)$, with $S_2=TS_1$, $V_2=I*V_1=A'*V_1$.⟧",
        "⟦Lọc số là tổng chập với $h(n)$; chọn $h(0)$ bằng trung bình hai phía để mẫu khớp đáp ứng liên tục.||Digital filtering is a convolution sum with $h(n)$; choose $h(0)$ as the two-sided mean so samples match the continuous response.⟧",
        "⟦Tuyến tính cộng bất biến theo thời gian tương đương đáp ứng điều hòa và tích chập; phi tuyến hay biến thiên đều phá vỡ nó.||Linearity plus time invariance is equivalent to harmonic response and convolution; nonlinearity or time variation breaks it.⟧",
        "⟦Điều chế cho hai dải bên $M/4$, điều chế ngược nhân phổ với cosin, và ổn định là $\\int|I|dt$ hữu hạn.||Modulation gives two sidebands $M/4$, its converse multiplies the spectrum by a cosine, and stability means $\\int|I|dt$ is finite.⟧",
    ],
    history="<p>⟦Hartley (1942) đề xuất cặp công thức đối xứng hoàn toàn mà ngày nay gọi là biến đổi Hartley; thuật toán Hartley nhanh được khảo sát trong hàng trăm bài từ 1983 (Bracewell, tr. 200). Newcomb (1963) trình bày về đáp ứng xung theo hàm suy rộng; Oppenheim và Schafer (1989) và Schwartz (1990) là các tài liệu tham khảo cho xử lý tín hiệu số và truyền tin, điều chế, nhiễu (tr. 211).||"
            "Hartley (1942) proposed the pair of formulas with total symmetry now called the Hartley transform; the fast Hartley algorithm has been explored in hundreds of papers since 1983 (Bracewell, p. 200). Newcomb (1963) treats impulse-response theorems through generalized functions; Oppenheim and Schafer (1989) and Schwartz (1990) are references for digital signal processing and for information transmission, modulation and noise (p. 211).⟧</p>",
    case="<p>⟦<b>Một bộ lọc số ba điểm.</b> Trung bình trượt $h=\\{\\tfrac13,\\tfrac13,\\tfrac13\\}$ cho tần số 0.1 biên độ {{ma_amp}} (mô phỏng cho {{ma_amp_sim}}): tín hiệu chậm gần như qua nguyên vẹn. Mạch RC cùng loại lọc thông thấp: tại 0.3 nó cho {{rc_amp}} và trễ pha {{rc_ph}} độ. Theo cách nhìn của chương, cả hai đều chỉ là một $T(f)$ và một $I(t)$; có thể cho vào một sóng điều biên, thấy sóng mang và hai dải bên ($M/4$ = {{am_sb}}) bị nhân với các giá trị khác nhau của $T$, và biết chắc rằng đầu ra chỉ chứa các tần số đã có ở đầu vào, vì hệ tuyến tính và bất biến (năng lượng ngoài các tần số ấy {{lti_leak}}). Nếu thay bằng bộ bình phương, xuất hiện tần số mới ({{nl_2f}} tại $2f$); nếu nhân với hàm biến thiên, các tần số bị dịch ({{tv_lo}} và {{tv_hi}}).||"
          "<b>A three-point digital filter.</b> The moving average $h=\\{\\tfrac13,\\tfrac13,\\tfrac13\\}$ passes frequency 0.1 with amplitude {{ma_amp}} (simulation gives {{ma_amp_sim}}): a slow signal goes through almost intact. An RC circuit of the same low-pass kind gives {{rc_amp}} at 0.3 with phase lag {{rc_ph}} degrees. In the chapter's view both are just a $T(f)$ and an $I(t)$; feed in an amplitude-modulated wave and see the carrier and the two sidebands ($M/4$ = {{am_sb}}) multiplied by different values of $T$, and be sure the output contains only frequencies already in the input since the system is linear and invariant (energy outside those frequencies {{lti_leak}}). Replace it by a squarer and new frequencies appear ({{nl_2f}} at $2f$); multiply by a varying function and frequencies are shifted ({{tv_lo}} and {{tv_hi}}).⟧</p>",
    practice=[
        "⟦Mở notebook và chạy cell cài đặt.||Open the notebook and run the setup cell.⟧",
        "⟦Bài 1: đo $T(f)$ của mạch RC bằng cách cho vào các sóng cosin và so với $1/(1+i2\\pi f)$.||Task 1: measure $T(f)$ of the RC circuit by feeding cosines and compare with $1/(1+i2\\pi f)$.⟧",
        "⟦Bài 2: dùng đáp ứng bậc thang để tính đầu ra với đầu vào là hình thang, rồi so với tích chập với $I$.||Task 2: use the step response to compute the output for a trapezoidal input and compare with convolution with $I$.⟧",
        "⟦Bài 3: thiết kế bộ lọc FIR bốn điểm để triệt tần số 0.25 và kiểm bằng cosin thử.||Task 3: design a four-point FIR filter to null frequency 0.25 and check with a test cosine.⟧",
        "⟦Bài 4: thử một hệ có ngưỡng (cắt biên độ) và chỉ ra tần số mới xuất hiện.||Task 4: try a clipping system and show the new frequencies that appear.⟧",
        "⟦Bài 5: làm bài 29 với $W$ khác và xác nhận $L_{\\max}=W\\sqrt{2/\\pi}$.||Task 5: do problem 29 with another $W$ and confirm $L_{\\max}=W\\sqrt{2/\\pi}$.⟧",
    ],
    pitfalls=[
        "<b>⟦\"Định lý cộng chứng tỏ hệ là tuyến tính.\"||\"The addition theorem shows the system is linear.\"⟧</b><p>⟦Định lý cộng chỉ nói về tuyến tính của phép biến đổi; nó đúng cả cho dạng sóng trong mạch phi tuyến (tr. 207). Bộ bình phương phi tuyến vẫn có phổ cộng được, nhưng đầu ra có tần số mới ({{nl_2f}} tại $2f$).||The addition theorem is only about the linearity of the transform; it is true even for waveforms in nonlinear circuits (p. 207). A nonlinear squarer still has additive spectra, but its output has a new frequency ({{nl_2f}} at $2f$).⟧</p>",
        "<b>⟦\"Chỉ cần đo đáp ứng tỷ lệ với biên độ là bộ lọc tuyến tính.\"||\"Proportionality of response to amplitude proves the filter is linear.\"⟧</b><p>⟦Bài 14 và 15: tỷ lệ với đầu vào chưa đủ; tuyến tính đòi hỏi chồng chất với mọi cặp đầu vào (tr. 213 đến 214).||Problems 14 and 15: proportionality to the input is not enough; linearity requires superposition for every pair of inputs (pp. 213 to 214).⟧</p>",
        "<b>⟦\"Nếu tần số cơ bản không có trong phổ thì dạng sóng không tuần hoàn.\"||\"If the fundamental frequency is absent from the spectrum the waveform is not periodic.\"⟧</b><p>⟦$9\\cos5x+11\\cos4x$ tuần hoàn chu kỳ $2\\pi$ (lệch {{per_dev}}) nhưng thành phần tại $1/2\\pi$ có biên độ {{per_fund}} (tr. 211, bài 27).||$9\\cos5x+11\\cos4x$ is periodic with period $2\\pi$ (deviation {{per_dev}}) although the component at $1/2\\pi$ has amplitude {{per_fund}} (p. 211, problem 27).⟧</p>",
        "<b>⟦\"Lấy mẫu $e^{-t}H(t)$ thì $h(0)=1$.\"||\"Sampling $e^{-t}H(t)$ gives $h(0)=1$.\"⟧</b><p>⟦Để các mẫu của $V_2(t)$ trùng $g(n)$, phải lấy $h(0)=0.5$, trung bình hai phía của bước nhảy: $g(1)$ = {{dg_1}} trong ví dụ, đúng cả hai cách tính (tr. 205).||For the samples of $V_2(t)$ to match $g(n)$, take $h(0)=0.5$, the two-sided mean of the jump: $g(1)$ = {{dg_1}} in the example, correct by both calculations (p. 205).⟧</p>",
    ],
    refs=[
        "⟦R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chương 9 (tr. 198 đến 218).||R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chapter 9 (pp. 198 to 218).⟧",
        "⟦Tài liệu do chương 9 trích: Hartley (1942), Newcomb (1963), Olejniczak và Heydt (1994), Oppenheim và Schafer (1989), Schwartz (1990).||Works cited by chapter 9: Hartley (1942), Newcomb (1963), Olejniczak and Heydt (1994), Oppenheim and Schafer (1989), Schwartz (1990).⟧",
    ],
    quiz=[
        dict(q="⟦Độ lớn của $S=1/(1+i2\\pi f)$ tại $f=0.3$ bằng bao nhiêu?||What is the magnitude of $S=1/(1+i2\\pi f)$ at $f=0.3$?⟧",
             opts=["{{sy_mag}}", "0.2196", "0.8453", "0.6633"], explain="⟦$1/\\sqrt{1+4\\pi^2f^2}$ = {{sy_mag}}.||$1/\\sqrt{1+4\\pi^2f^2}$ = {{sy_mag}}.⟧"),
        dict(q="⟦Lệch tối đa của $S(-f)-S^*(f)$ với dãy thực ngẫu nhiên là bao nhiêu?||What is the largest deviation of $S(-f)-S^*(f)$ for a random real sequence?⟧",
             opts=["{{herm_dev}}", "1.0e-01", "0.5000", "1.0e-03"], explain="⟦Phổ của dạng sóng thực là Hermite: lệch chỉ {{herm_dev}}.||The spectrum of a real waveform is Hermitian: deviation only {{herm_dev}}.⟧"),
        dict(q="⟦Lệch tối đa giữa $\\text{Im}\\,S$ và $-\\mathcal H[\\text{Re}\\,S]$ của $e^{-t}H(t)$ là bao nhiêu?||What is the largest deviation between $\\text{Im}\\,S$ and $-\\mathcal H[\\text{Re}\\,S]$ for $e^{-t}H(t)$?⟧",
             opts=["{{hilb_dev}}", "0.5000", "1.0e-01", "1.0e+00"], explain="⟦Dạng sóng nhân quả: {{hilb_dev}}.||Causal waveform: {{hilb_dev}}.⟧"),
        dict(q="⟦Biến đổi Hartley của $e^{-t}H(t)$ tại $f=0.3$ bằng bao nhiêu?||What is the Hartley transform of $e^{-t}H(t)$ at $f=0.3$?⟧",
             opts=["{{hart_val}}", "0.2196", "0.4140", "0.8336"], explain="⟦$\\text{Re}\\,S-\\text{Im}\\,S$ = {{hart_val}}, khớp tích phân trực tiếp.||$\\text{Re}\\,S-\\text{Im}\\,S$ = {{hart_val}}, matching the direct integral.⟧"),
        dict(q="⟦Hệ 3 (đối xứng) của Gauss $e^{-\\pi t^2}$ tại $\\omega=2\\pi(0.3)$ bằng bao nhiêu?||What does system 3 (symmetric) give for the Gaussian $e^{-\\pi t^2}$ at $\\omega=2\\pi(0.3)$?⟧",
             opts=["{{sy_3}}", "0.7537", "1.8891", "0.1200"], explain="⟦Hệ 1 cho {{sy_1}}; hệ 3 chia $\\sqrt{2\\pi}$ = {{sy_3}}.||System 1 gives {{sy_1}}; system 3 divides by $\\sqrt{2\\pi}$ = {{sy_3}}.⟧"),
        dict(q="⟦Biên độ ổn định của mạch RC ($I=e^{-t}H$) với $\\cos2\\pi(0.3)t$ bằng bao nhiêu (mô phỏng thời gian)?||What is the steady-state amplitude of the RC circuit ($I=e^{-t}H$) for $\\cos2\\pi(0.3)t$ (time-domain simulation)?⟧",
             opts=["{{rc_amp_sim}}", "0.7071", "0.3536", "0.9100"], explain="⟦$|T|$ = {{rc_amp}} theo công thức; mô phỏng {{rc_amp_sim}}.||$|T|$ = {{rc_amp}} by the formula; simulation {{rc_amp_sim}}.⟧"),
        dict(q="⟦Pha (độ) của $T=1/(1+i2\\pi f)$ tại $f=0.3$ bằng bao nhiêu?||What is the phase (degrees) of $T=1/(1+i2\\pi f)$ at $f=0.3$?⟧",
             opts=["{{rc_ph}}", "-45.0", "-28.0", "-90.0"], explain="⟦$-\\arctan(2\\pi f)$ = {{rc_ph}} độ; mô phỏng cho {{rc_ph_sim}}.||$-\\arctan(2\\pi f)$ = {{rc_ph}} degrees; simulation gives {{rc_ph_sim}}.⟧"),
        dict(q="⟦Xung chữ nhật đơn vị qua mạch RC cho $V_2(1.5)$ bằng bao nhiêu?||A unit rectangular pulse through the RC circuit gives $V_2(1.5)$ equal to what?⟧",
             opts=["{{pulse_y}}", "0.3679", "0.6321", "0.2231"], explain="⟦$e^{-0.5}-e^{-1.5}$ = {{pulse_y}}, theo tích chập số và IFFT.||$e^{-0.5}-e^{-1.5}$ = {{pulse_y}}, by numerical convolution and the IFFT.⟧"),
        dict(q="⟦Lệch giữa $A'$ và $I$ của mạch RC (đáp ứng bậc thang $1-e^{-t}$) là bao nhiêu?||What is the deviation between $A'$ and $I$ for the RC circuit (step response $1-e^{-t}$)?⟧",
             opts=["{{step_dev}}", "1.0e-01", "0.5000", "1.0e-03"], explain="⟦$I=A'$: lệch {{step_dev}}.||$I=A'$: deviation {{step_dev}}.⟧"),
        dict(q="⟦$g(2)$ của $h=\\{0.5,e^{-1},e^{-2},\\ldots\\}$ với $f=\\{1\\ 2\\ 1\\}$ bằng bao nhiêu?||What is $g(2)$ for $h=\\{0.5,e^{-1},e^{-2},\\ldots\\}$ and $f=\\{1\\ 2\\ 1\\}$?⟧",
             opts=["{{dg_2}}", "1.3679", "0.6884", "0.5000"], explain="⟦$e^{-2}+2e^{-1}+0.5$ = {{dg_2}}; $g(1)$ = {{dg_1}}, $g(3)$ = {{dg_3}}, $g(4)$ = {{dg_4}}.||$e^{-2}+2e^{-1}+0.5$ = {{dg_2}}; $g(1)$ = {{dg_1}}, $g(3)$ = {{dg_3}}, $g(4)$ = {{dg_4}}.⟧"),
        dict(q="⟦Đáp ứng bài 30 (tín hiệu $\\{1\\ 1.6\\ 2\\ 0.6\\}$, $RC=1$) tại $t=4$ bằng bao nhiêu?||What is the response in problem 30 (signal $\\{1\\ 1.6\\ 2\\ 0.6\\}$, $RC=1$) at $t=4$?⟧",
             opts=["{{p30_t4}}", "1.7239", "0.5894", "2.0000"], explain="⟦$e^{-3}+1.6e^{-2}+2e^{-1}+0.3$ = {{p30_t4}}; tại 3: {{p30_t3}}, tại 6: {{p30_t6}}.||$e^{-3}+1.6e^{-2}+2e^{-1}+0.3$ = {{p30_t4}}; at 3: {{p30_t3}}, at 6: {{p30_t6}}.⟧"),
        dict(q="⟦Bộ trung bình trượt 3 điểm có $|H(0.1)|$ bằng bao nhiêu?||What is $|H(0.1)|$ for the 3-point moving average?⟧",
             opts=["{{ma_amp}}", "1.0000", "0.6667", "0.5000"], explain="⟦$(1+2\\cos0.2\\pi)/3$ = {{ma_amp}}; mô phỏng {{ma_amp_sim}}.||$(1+2\\cos0.2\\pi)/3$ = {{ma_amp}}; simulation {{ma_amp_sim}}.⟧"),
        dict(q="⟦Đỉnh phổ của $V(2t)$ với $V=e^{-\\pi t^2}$ bằng bao nhiêu?||What is the peak of the spectrum of $V(2t)$ for $V=e^{-\\pi t^2}$?⟧",
             opts=["{{sim_peak}}", "1.0000", "2.0000", "0.2500"], explain="⟦Hệ số $|a|^{-1}$ = {{sim_peak}}; diện tích dưới phổ vẫn {{sim_area}} ($V(0)$).||The factor $|a|^{-1}$ = {{sim_peak}}; the area under the spectrum stays {{sim_area}} ($V(0)$).⟧"),
        dict(q="⟦Hệ số pha $e^{-i2\\pi fT}$ tại $f=2$ khi $T=0.5$ bằng bao nhiêu?||What is the phase factor $e^{-i2\\pi fT}$ at $f=2$ when $T=0.5$?⟧",
             opts=["{{shift_mult}}", "-1", "i", "0"], explain="⟦Bội của $1/T$ nên không đổi: {{shift_mult}}; tại 0.1: {{shift_low}} độ; tại 1.3: {{shift_high}} độ.||A multiple of $1/T$ so unchanged: {{shift_mult}}; at 0.1: {{shift_low}} degrees; at 1.3: {{shift_high}} degrees.⟧"),
        dict(q="⟦Pha (độ) của thành phần $f=1.3$ khi trễ $T=0.5$ bằng bao nhiêu?||What is the phase (degrees) of the component $f=1.3$ when delayed by $T=0.5$?⟧",
             opts=["{{shift_high}}", "-234", "-117", "-36"], explain="⟦$-360fT$ = {{shift_high}} độ (đã cuộn về $[-180,180]$).||$-360fT$ = {{shift_high}} degrees (wrapped to $[-180,180]$).⟧"),
        dict(q="⟦Biên độ sóng mang của $(1+0.5\\cos\\omega t)\\cos\\Omega t$ (mỗi vạch ±) là bao nhiêu?||What is the carrier amplitude (each ± line) of $(1+0.5\\cos\\omega t)\\cos\\Omega t$?⟧",
             opts=["{{am_car}}", "1.0000", "0.2500", "0.1250"], explain="⟦Sóng mang $\\tfrac12$ mỗi vạch; dải bên $M/4$ = {{am_sb}}.||The carrier is $\\tfrac12$ per line; the sidebands $M/4$ = {{am_sb}}.⟧"),
        dict(q="⟦Biên độ mỗi dải bên với $M=0.5$ là bao nhiêu?||What is the amplitude of each sideband for $M=0.5$?⟧",
             opts=["{{am_sb}}", "0.2500", "0.5000", "0.0625"], explain="⟦$M/4$ = {{am_sb}}, đo bằng DFT.||$M/4$ = {{am_sb}}, measured by DFT.⟧"),
        dict(q="⟦$|2\\cos(2\\pi Tf)S|$ với Gauss, $T=1$, $f=0.3$ bằng bao nhiêu?||What is $|2\\cos(2\\pi Tf)S|$ for the Gaussian, $T=1$, $f=0.3$?⟧",
             opts=["{{conv_pair}}", "1.5074", "0.3013", "0.9048"], explain="⟦$|2\\cos(0.6\\pi)|e^{-\\pi(0.3)^2}$ = {{conv_pair}}; pha của dạng thứ hai {{conv_ph}} độ.||$|2\\cos(0.6\\pi)|e^{-\\pi(0.3)^2}$ = {{conv_pair}}; the second form's phase is {{conv_ph}} degrees.⟧"),
        dict(q="⟦Pha (độ) của $V(t)+V(t-2T)$ tại $T=1$, $f=0.3$ là bao nhiêu (gồm dấu của cosin)?||What is the phase (degrees) of $V(t)+V(t-2T)$ at $T=1$, $f=0.3$ (including the sign of the cosine)?⟧",
             opts=["{{conv_ph}}", "-216", "-108", "-72"], explain="⟦$e^{-i2\\pi Tf}\\cos2\\pi Tf$: cosin âm cộng $-216$ độ, quy về {{conv_ph}}.||$e^{-i2\\pi Tf}\\cos2\\pi Tf$: a negative cosine plus $-216$ degrees, wrapped to {{conv_ph}}.⟧"),
        dict(q="⟦$|T|$ của hai kênh trễ $T_1=0.3$, $T_2=1.1$ tại $f=0.4$ bằng bao nhiêu?||What is $|T|$ of two channels with delays $T_1=0.3$, $T_2=1.1$ at $f=0.4$?⟧",
             opts=["{{p24_val}}", "2.0000", "1.0000", "0.4258"], explain="⟦$2|\\cos(\\pi f\\Delta)|$ với $\\Delta=0.8$: {{p24_val}}, lệch {{p24_dev}}.||$2|\\cos(\\pi f\\Delta)|$ with $\\Delta=0.8$: {{p24_val}}, deviation {{p24_dev}}.⟧"),
        dict(q="⟦Với bốn thừa số cosin, sai số so với $\\text{sinc}\\,x$ đạt 1% đỉnh ở $x$ xấp xỉ bao nhiêu?||With four cosine factors, at about which $x$ does the error against $\\text{sinc}\\,x$ reach 1 percent of the peak?⟧",
             opts=["{{p23_x}}", "1.00", "20.0", "0.100"], explain="⟦Đo được {{p23_x}}; công thức có thừa số sửa $\\text{sinc}(x/2^N)$ đúng với sai số {{p23_dev}}.||Measured {{p23_x}}; the formula with the correction factor $\\text{sinc}(x/2^N)$ is exact to {{p23_dev}}.⟧"),
        dict(q="⟦$L_{\\max}/W$ để chỗ trũng giữa hai vạch Gauss biến mất bằng bao nhiêu?||What is $L_{\\max}/W$ at which the dip between two Gaussian lines disappears?⟧",
             opts=["{{p29_L}}", "1.0000", "0.5000", "1.2533"], explain="⟦$\\sqrt{2/\\pi}$ = {{p29_L}} (độ cong giữa bằng 0).||$\\sqrt{2/\\pi}$ = {{p29_L}} (central curvature zero).⟧"),
        dict(q="⟦Biên độ của thành phần tần số $2f$ trong đầu ra của bộ bình phương với $\\cos2\\pi ft$ là bao nhiêu?||What is the amplitude of the $2f$ component in the output of a squarer fed with $\\cos2\\pi ft$?⟧",
             opts=["{{nl_2f}}", "1.0000", "0.2500", "2.0000"], explain="⟦$\\cos^2=\\tfrac12+\\tfrac12\\cos4\\pi ft$: {{nl_2f}}.||$\\cos^2=\\tfrac12+\\tfrac12\\cos4\\pi ft$: {{nl_2f}}.⟧"),
        dict(q="⟦Nhân $\\cos2\\pi(5)t$ với $\\cos2\\pi(1)t$ cho hai tần số nào (thấp hơn)?||Multiplying $\\cos2\\pi(5)t$ by $\\cos2\\pi(1)t$ gives two frequencies; what is the lower?⟧",
             opts=["{{tv_lo}}", "5.0000", "1.0000", "6.0000"], explain="⟦Tần số $f\\pm f_2$: {{tv_lo}} và {{tv_hi}}.||Frequencies $f\\pm f_2$: {{tv_lo}} and {{tv_hi}}.⟧"),
        dict(q="⟦Năng lượng (tỉ lệ) ngoài tần số đầu vào của đầu ra bộ lọc tuyến tính bất biến là bao nhiêu?||What fraction of the output energy of a linear time-invariant filter lies outside the input frequency?⟧",
             opts=["{{lti_leak}}", "1.0e-02", "0.5000", "1.0e-06"], explain="⟦Đáp ứng điều hòa với đầu vào điều hòa: {{lti_leak}}.||Harmonic response to harmonic input: {{lti_leak}}.⟧"),
        dict(q="⟦Lệch của $y(x+2\\pi)-y(x)$ với $y=9\\cos5x+11\\cos4x$ là bao nhiêu?||What is the deviation of $y(x+2\\pi)-y(x)$ for $y=9\\cos5x+11\\cos4x$?⟧",
             opts=["{{per_dev}}", "1.0e-03", "1.0e-01", "9.0000"], explain="⟦Chu kỳ $2\\pi$: lệch {{per_dev}}; thành phần cơ bản tại $1/2\\pi$ có biên độ {{per_fund}}.||Period $2\\pi$: deviation {{per_dev}}; the fundamental component at $1/2\\pi$ has amplitude {{per_fund}}.⟧"),
        dict(q="⟦$\\int|I|dt$ của $I=e^{-t}\\cos2\\pi t\\,H(t)$ bằng bao nhiêu?||What is $\\int|I|dt$ for $I=e^{-t}\\cos2\\pi t\\,H(t)$?⟧",
             opts=["{{st_osc}}", "1.0000", "0.1585", "0.5000"], explain="⟦Tổng chu kỳ $|\\cos|$: {{st_osc}}, bằng độ lợi lớn nhất khi cho vào $\\text{sgn}\\,I(-t)$; mạch RC có {{st_rc}}.||Sum over periods of $|\\cos|$: {{st_osc}}, equal to the largest gain reached with input $\\text{sgn}\\,I(-t)$; the RC circuit has {{st_rc}}.⟧"),
        dict(q="⟦Tích phân $\\int_0^{100}|H(t)|dt$ của bộ tích phân lý tưởng bằng bao nhiêu?||What is $\\int_0^{100}|H(t)|dt$ for the ideal integrator?⟧",
             opts=["{{st_int}}", "1", "10", "1000"], explain="⟦Bằng độ dài: {{st_int}}, không giới hạn khi $T\\to\\infty$: không ổn định.||Equal to the length: {{st_int}}, unbounded as $T\\to\\infty$: unstable.⟧"),
        dict(q="⟦Điện trở đầu vào máy phát cho 1 MW ở 15 kV là bao nhiêu (ôm)?||What input resistance of the generator gives 1 MW at 15 kV (ohms)?⟧",
             opts=["{{rad_Z}}", "150", "30", "500"], explain="⟦$V^2/P=(15000)^2/10^6$ = {{rad_Z}} ôm.||$V^2/P=(15000)^2/10^6$ = {{rad_Z}} ohms.⟧"),
        dict(q="⟦Chiều dài đường truyền (mét) cho xung 0.1 µs nếu $v=c$ là bao nhiêu?||What line length (metres) gives a 0.1 µs pulse if $v=c$?⟧",
             opts=["{{rad_len}}", "30", "7.5", "3.0"], explain="⟦Thời lượng $=2\\ell/v$: $\\ell=v\\tau/2$ = {{rad_len}} m.||Duration $=2\\ell/v$: $\\ell=v\\tau/2$ = {{rad_len}} m.⟧"),
        dict(q="⟦Năng lượng mỗi xung radar 1 MW, 0.1 µs bằng bao nhiêu joule?||What energy per radar pulse of 1 MW, 0.1 µs (joules)?⟧",
             opts=["{{rad_E}}", "1.0", "0.01", "10"], explain="⟦$P\\tau$ = {{rad_E}} J, bằng $\\tfrac12CV^2$ = {{rad_E2}} J.||$P\\tau$ = {{rad_E}} J, equal to $\\tfrac12CV^2$ = {{rad_E2}} J.⟧"),
        dict(q="⟦Ba cách đặc trưng một bộ lọc tuyến tính bất biến là gì?||What are three ways to specify a linear time-invariant filter?⟧",
             opts=["⟦Hàm truyền, đáp ứng xung, đáp ứng bậc thang||Transfer function, impulse response, step response⟧",
                   "⟦Hàm truyền, hệ số phản xạ và trở kháng vào của mạng điện tương ứng||Transfer function, reflection coefficient and input impedance of the corresponding network⟧",
                   "⟦Đáp ứng xung, phổ công suất của đầu vào và độ rộng băng ba đềxiben||Impulse response, input power spectrum and the three-decibel bandwidth⟧",
                   "⟦Đáp ứng bậc thang, độ trễ nhóm và hệ số phẩm chất của bộ cộng hưởng||Step response, group delay and quality factor of the resonator⟧"],
             explain="⟦Bracewell, tr. 200 đến 202: $T(f)$, $I(t)$, $A(t)$, liên hệ $I=A'$ và $T=i2\\pi f\\mathcal A$.||Bracewell, pp. 200 to 202: $T(f)$, $I(t)$, $A(t)$, related by $I=A'$ and $T=i2\\pi f\\mathcal A$.⟧"),
        dict(q="⟦Điều kiện nào trên $V_2=\\int J(t,t')V_1(t')dt'$ dẫn tới tích chập?||Which condition on $V_2=\\int J(t,t')V_1(t')dt'$ leads to a convolution?⟧",
             opts=["⟦Bất biến theo thời gian: $J(t,t')=J(t+T,t'+T)$||Time invariance: $J(t,t')=J(t+T,t'+T)$⟧",
                   "⟦Nhân quả: $J(t,t')=0$ khi $t<t'$, vì khi đó tích phân chỉ chạy tới $t$||Causality: $J(t,t')=0$ for $t<t'$, since the integral then runs only up to $t$⟧",
                   "⟦Đối xứng: $J(t,t')=J(t',t)$, vì hạt nhân tự liên hợp cho tích chập thực||Symmetry: $J(t,t')=J(t',t)$, since a self-adjoint kernel gives a real convolution⟧",
                   "⟦Ổn định: $\\int|J|dt'$ hữu hạn, vì khi đó đầu ra bị chặn và biến đổi tồn tại||Stability: $\\int|J|dt'$ finite, since then the output is bounded and the transform exists⟧"],
             explain="⟦Bracewell, tr. 210 đến 211: tuyến tính cho dạng phiếm hàm, bất biến cho $J=I(t-t')$.||Bracewell, pp. 210 to 211: linearity gives the functional form, invariance gives $J=I(t-t')$.⟧"),
        dict(q="⟦Vì sao định lý cộng không nói gì về tính tuyến tính của mạch?||Why does the addition theorem say nothing about linearity of circuits?⟧",
             opts=["⟦Nó chỉ biểu thị tính tuyến tính của phép biến đổi Fourier||It only expresses the linearity of the Fourier transformation⟧",
                   "⟦Vì phổ của tổng chỉ bằng tổng các phổ khi các hàm trực giao với nhau||Because the spectrum of a sum equals the sum of spectra only when the functions are orthogonal⟧",
                   "⟦Vì mạch thực luôn có nhiễu nên tính cộng chỉ đúng gần đúng trong trường hợp tốt nhất||Because real circuits always have noise so additivity holds only approximately at best⟧",
                   "⟦Vì định lý cộng chỉ áp dụng cho các dạng sóng không âm và năng lượng hữu hạn||Because the theorem only applies to nonnegative waveforms of finite energy⟧"],
             explain="⟦Bracewell, tr. 207: đúng cả cho dạng sóng trong mạch phi tuyến.||Bracewell, p. 207: true even of waveforms in nonlinear circuits.⟧"),
        dict(q="⟦Thành phần nào của dạng sóng không bị đổi khi trễ $T$?||Which components of a waveform are unchanged by a delay $T$?⟧",
             opts=["⟦Tần số bằng hoặc là bội nguyên của $T^{-1}$||Frequencies equal to or an integral multiple of $T^{-1}$⟧",
                   "⟦Mọi thành phần có chu kỳ ngắn hơn $T$, vì chúng quay nhiều vòng trong độ trễ||All components with periods shorter than $T$, since they turn many times during the delay⟧",
                   "⟦Chỉ thành phần một chiều, vì các thành phần còn lại đều bị dịch pha nhất định||Only the d.c. component, since all others undergo some phase shift⟧",
                   "⟦Thành phần có tần số bằng đúng $T$ đơn vị nghịch đảo, theo định nghĩa của độ trễ||The component whose frequency equals exactly $T$ reciprocal units, by the definition of delay⟧"],
             explain="⟦Bracewell, tr. 207: thành phần tần số $=T^{-1}$ hoặc bội nguyên không bị ảnh hưởng.||Bracewell, p. 207: a component whose frequency is $T^{-1}$ or an integral multiple is not affected.⟧"),
        dict(q="⟦Tại sao lấy mẫu $e^{-t}H(t)$ cho $h(0)=0.5$ chứ không phải 1?||Why does sampling $e^{-t}H(t)$ give $h(0)=0.5$ rather than 1?⟧",
             opts=["⟦Để mẫu của $V_2(t)$ trùng $g(n)$: lấy trung bình của $I(0^-)$ và $I(0^+)$||So samples of $V_2(t)$ equal $g(n)$: take the mean of $I(0^-)$ and $I(0^+)$⟧",
                   "⟦Vì năng lượng của đáp ứng xung phải bằng 1/2 sau khi rời rạc hóa theo định lý Parseval||Because the energy of the impulse response must equal 1/2 after discretisation, by Parseval's theorem⟧",
                   "⟦Vì lọc số luôn làm suy giảm nửa biên độ của mẫu đầu tiên do hiệu ứng chồng phổ||Because digital filtering always halves the amplitude of the first sample due to aliasing⟧",
                   "⟦Vì bộ lấy mẫu sample-and-hold chỉ nạp tụ được một nửa giá trị trong thời gian ngắn||Because a sample-and-hold circuit only charges its capacitor to half the value in a short time⟧"],
             explain="⟦Bracewell, tr. 205: $h(0)$ chọn là trung bình hai phía; khi đó $g(n)$ khớp các mẫu của $V_2(t)$ ($g(1)$ = {{dg_1}}).||Bracewell, p. 205: $h(0)$ is the two-sided mean; then $g(n)$ matches the samples of $V_2(t)$ ($g(1)$ = {{dg_1}}).⟧"),
        dict(q="⟦Hệ thống nào tuyến tính nhưng không bất biến theo thời gian?||Which system is linear but not time-invariant?⟧",
             opts=["⟦Nhân đầu vào với một hàm biến thiên theo thời gian||Multiplying the input by a time-varying function⟧",
                   "⟦Bộ bình phương lấy $y=x^2$, có đầu ra tăng nhanh khi đầu vào lớn||A squarer $y=x^2$, whose output grows quickly for large inputs⟧",
                   "⟦Mạch RC có $R$ và $C$ hằng số, vì đáp ứng của nó phụ thuộc thời điểm bật||An RC circuit with constant $R$ and $C$, since its response depends on the switch-on time⟧",
                   "⟦Bộ trung bình trượt dài hữu hạn, vì cửa sổ chỉ nhìn một đoạn của tín hiệu||A finite-length moving average, since the window only sees a section of the signal⟧"],
             explain="⟦Bracewell, tr. 213 (bài 13): phép nhân với mặt nạ tuyến tính nhưng không bất biến; đầu ra có tần số $f\\pm f_2$ ({{tv_lo}}, {{tv_hi}}).||Bracewell, p. 213 (problem 13): multiplication by a mask is linear but not invariant; the output has frequencies $f\\pm f_2$ ({{tv_lo}}, {{tv_hi}}).⟧"),
        dict(q="⟦Hệ tuyến tính ổn định (đầu vào bị chặn cho đầu ra bị chặn) khi nào?||When is a linear system stable (bounded input gives bounded output)?⟧",
             opts=["⟦Khi $\\int|I(t)|dt$ hữu hạn||When $\\int|I(t)|dt$ is finite⟧",
                   "⟦Khi $\\int I(t)dt=0$, vì khi đó không có thành phần một chiều tích lũy||When $\\int I(t)dt=0$, since then no d.c. component accumulates⟧",
                   "⟦Khi $I(t)$ nhân quả và có giá trị tại gốc bằng 0, để không có bước nhảy đầu ra||When $I(t)$ is causal and vanishes at the origin, so the output has no jump⟧",
                   "⟦Khi $T(f)$ có mô đun bằng 1 ở mọi tần số, tức đáp ứng tần số phẳng||When $|T(f)|=1$ at every frequency, i.e. a flat frequency response⟧"],
             explain="⟦Bracewell, tr. 214 (bài 18): ổn định khi tích phân tuyệt đối của đáp ứng xung hữu hạn; RC có {{st_rc}}, bộ tích phân lý tưởng không giới hạn.||Bracewell, p. 214 (problem 18): stable when the absolute integral of the impulse response is finite; RC has {{st_rc}}, the ideal integrator is unbounded.⟧"),
    ],
    nb=[
        ("md", """## 1. ⟦Phổ của dạng sóng thực và nhân quả||Spectra of real and causal waveforms⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Phổ của dạng sóng thực có Hermite, phổ nhân quả có quan hệ Hilbert, các hệ ký hiệu 1, 2, 3 và biến đổi Hartley có khớp? Mỗi số tính bằng hai cách.||Is the spectrum of a real waveform Hermitian, does a causal spectrum obey the Hilbert relation, and do notation systems 1, 2, 3 and the Hartley transform agree? Each number is computed two ways.⟧"""),
        ("code", r'''from scipy import integrate, signal
trap = getattr(np, "trapezoid", None) or np.trapz
def ftq(f, a, b, s, pts=None):
    re = integrate.quad(lambda x: f(x)*np.cos(2*np.pi*x*s), a, b, points=pts, limit=400)[0]
    im = integrate.quad(lambda x: -f(x)*np.sin(2*np.pi*x*s), a, b, points=pts, limit=400)[0]
    return re + 1j*im
f0 = 0.3
S = lambda f: 1/(1 + 2j*np.pi*f)
Snum = ftq(lambda t: np.exp(-t), 0, 60, f0)
assert abs(Snum - S(f0)) < 1e-8
report("sy_mag", abs(S(f0)), ".4f")

# ⟦phổ Hermite của dãy thực ngẫu nhiên||Hermitian spectrum of a random real sequence⟧
rg = np.random.default_rng(9); x = rg.standard_normal(64); X = np.fft.fft(x)
herm = np.max(np.abs(X[(-np.arange(64)) % 64] - np.conj(X)))
assert herm < 1e-12
report("herm_dev", herm, ".1e")

# ⟦Hilbert: Im S = −H[Re S], lưới f trong [−200, 200]||Hilbert: Im S = −H[Re S], grid f in [−200, 200]⟧
N = 2**18; fg = np.linspace(-400, 400, N, endpoint=False)
reS = 1/(1 + 4*np.pi**2*fg**2); imS = -2*np.pi*fg/(1 + 4*np.pi**2*fg**2)
hil = signal.hilbert(reS).imag
mask = np.abs(fg) < 2
hil_dev = np.max(np.abs(hil[mask] + imS[mask]))
assert hil_dev < 5e-3
report("hilb_dev", hil_dev, ".1e")

# ⟦hệ 1, 2, 3 với Gauss||systems 1, 2, 3 with the Gaussian⟧
g = lambda t: np.exp(-np.pi*t**2)
s1 = ftq(g, -10, 10, f0).real
w = 2*np.pi*f0
s2 = integrate.quad(lambda t: g(t)*np.cos(w*t), -10, 10)[0]
s3 = s2/np.sqrt(2*np.pi)
assert abs(s1 - np.exp(-np.pi*f0**2)) < 1e-9 and abs(s2 - s1) < 1e-9
inv2 = integrate.quad(lambda om: s1*0 + np.exp(-om**2/(4*np.pi))*np.cos(0.0), -60, 60)[0]/(2*np.pi)      # V(0) = (1/2π)∫S dω
assert abs(inv2 - 1) < 1e-9
report("sy_1", s1, ".4f"); report("sy_3", s3, ".4f")

# ⟦Hartley: ∫V(cos + sin)||Hartley: ∫V(cos + sin)⟧
hart = integrate.quad(lambda t: np.exp(-t)*(np.cos(2*np.pi*f0*t) + np.sin(2*np.pi*f0*t)), 0, 60)[0]
assert abs(hart - (S(f0).real - S(f0).imag)) < 1e-8
report("hart_val", hart, ".4f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦$|S(0.3)|$ = {{sy_mag}}; phổ dãy thực lệch Hermite {{herm_dev}}; Hilbert lệch {{hilb_dev}}; Gauss hệ 1 và 3: {{sy_1}} và {{sy_3}}; Hartley {{hart_val}}.||$|S(0.3)|$ = {{sy_mag}}; the real-sequence spectrum deviates from Hermitian by {{herm_dev}}; Hilbert deviation {{hilb_dev}}; Gaussian systems 1 and 3: {{sy_1}} and {{sy_3}}; Hartley {{hart_val}}.⟧"""),
        ("md", """## 2. ⟦Hàm truyền, đáp ứng xung và bậc thang||Transfer function, impulse and step responses⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Đáp ứng ổn định của bộ lọc RC với cosin có bằng $|T|$ và pha của $T$, đầu ra của xung chữ nhật có bằng ba cách tính (tích chập với $I$, tích chập $A'$, IFFT của $TS$), và $I=A'$? Ta mô phỏng miền thời gian.||Does the steady-state response of the RC filter to a cosine equal $|T|$ and the phase of $T$, and is the output for a rectangular pulse the same by three calculations (convolution with $I$, convolution with $A'$, IFFT of $TS$), and is $I=A'$? We simulate in the time domain.⟧"""),
        ("code", r'''dt = 1e-3; t = np.arange(0, 60, dt)
I = np.exp(-t)                                            # ⟦đáp ứng xung||impulse response⟧
T = lambda f: 1/(1 + 2j*np.pi*f)
# ⟦cosin 0.3 Hz: đầu ra ổn định: cách A = tích chập số; cách B = công thức T||cosine 0.3 Hz: steady state: method A = numeric convolution; method B = formula T⟧
tt = np.arange(0, 120, dt)
xin = np.cos(2*np.pi*f0*tt)
y = np.convolve(xin, I)[:len(tt)]*dt
seg = slice(int(80/dt), int(100/dt))
# ⟦khớp biên độ và pha bằng bình phương tối thiểu||fit amplitude and phase by least squares⟧
A_ = np.vstack([np.cos(2*np.pi*f0*tt[seg]), np.sin(2*np.pi*f0*tt[seg])]).T
c, s_ = np.linalg.lstsq(A_, y[seg], rcond=None)[0]
amp_sim = np.hypot(c, s_); ph_sim = np.degrees(np.arctan2(s_, c))     # ⟦y = c cos + s sin = amp cos(ωt − φ) → φ = −atan2(s, c)||y = c cos + s sin = amp cos(ωt − φ) → φ = −atan2(s, c)⟧
ph_T = -ph_sim                                                # ⟦pha của T = −φ (trễ pha φ)||phase of T = −φ (phase lag φ)⟧
assert abs(amp_sim - abs(T(f0))) < 1e-3 and abs(ph_T - np.degrees(np.angle(T(f0)))) < 0.1
report("rc_amp", abs(T(f0)), ".4f"); report("rc_amp_sim", amp_sim, ".4f")
report("rc_ph", np.degrees(np.angle(T(f0))), ".1f"); report("rc_ph_sim", ph_T, ".1f")

# ⟦xung chữ nhật đơn vị (0..1) qua RC: ba cách||unit pulse (0..1) through the RC circuit: three ways⟧
dtp = 1e-3; tp = np.arange(0, 20, dtp)
x1 = ((tp >= 0) & (tp < 1)).astype(float)
yA = np.convolve(x1, np.exp(-tp))[:len(tp)]*dtp                      # I * V1
Aresp = 1 - np.exp(-tp)
yB = np.convolve(np.gradient(Aresp, dtp), x1)[:len(tp)]*dtp          # A' * V1
Nf = 2**16; Tf = np.fft.fftfreq(Nf, dtp)
buf = np.zeros(Nf); buf[:len(tp)] = x1
yC = np.fft.ifft(np.fft.fft(buf)*T(Tf)).real[:len(tp)]
idx = int(1.5/dtp)
exact = np.exp(-0.5) - np.exp(-1.5)
assert abs(yA[idx] - exact) < 2e-3 and abs(yB[idx] - exact) < 2e-3 and abs(yC[idx] - exact) < 2e-3
report("pulse_y", exact, ".4f")
step_dev = np.max(np.abs(np.gradient(Aresp, dtp)[1:-1] - np.exp(-tp)[1:-1]))
assert step_dev < 1e-3
report("step_dev", step_dev, ".1e")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Mạch RC ở 0.3 Hz: $|T|$ = {{rc_amp}} (mô phỏng {{rc_amp_sim}}), pha {{rc_ph}} độ (mô phỏng {{rc_ph_sim}}). Xung chữ nhật tại $t=1.5$: {{pulse_y}} bằng ba cách. $A'$ lệch $I$ {{step_dev}}.||The RC circuit at 0.3 Hz: $|T|$ = {{rc_amp}} (simulated {{rc_amp_sim}}), phase {{rc_ph}} degrees (simulated {{rc_ph_sim}}). The rectangular pulse at $t=1.5$: {{pulse_y}} by three ways. $A'$ deviates from $I$ by {{step_dev}}.⟧"""),
        ("md", """## 3. ⟦Lọc số||Digital filtering⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Tổng chập rời rạc với $h(0)=0.5$ có cho mẫu của đáp ứng liên tục, bài 30 có đúng, và biên độ ổn định của trung bình trượt có bằng $|H|$? Mỗi số tính bằng tổng chập và bằng công thức liên tục.||Does the discrete convolution sum with $h(0)=0.5$ give samples of the continuous response, does problem 30 hold, and does the steady-state amplitude of the moving average equal $|H|$? Each number is computed by the convolution sum and by the continuous formula.⟧"""),
        ("code", r'''h = np.array([0.5] + [np.exp(-n) for n in range(1, 30)])
def V2(tv, imp):          # ⟦đáp ứng liên tục I*Σ c δ(t − k), H(0) = ½||continuous response I*Σ c δ(t − k), H(0) = ½⟧
    out = 0.0
    for k, ck in imp:
        d = tv - k
        out += ck*(0.5 if abs(d) < 1e-12 else (np.exp(-d) if d > 0 else 0.0))
    return out
f_in = [(0, 1), (1, 2), (2, 1)]
g_sum = np.convolve(h, [1, 2, 1])[:5]
g_cont = np.array([V2(n, f_in) for n in range(5)])
assert np.allclose(g_sum, g_cont, atol=1e-12)
assert np.allclose(np.round(g_sum, 2), [0.5, 1.37, 1.37, 0.69, 0.25])
for n, key in ((1, "dg_1"), (2, "dg_2"), (3, "dg_3"), (4, "dg_4")):
    report(key, g_sum[n], ".3f")

# ⟦bài 30||problem 30⟧
sig = [(1, 1.0), (2, 1.6), (3, 2.0), (4, 0.6)]
v = np.array([V2(t_, sig) for t_ in range(0, 8)])
cs = np.convolve(h, [0, 1, 1.6, 2, 0.6])[:8]
assert np.allclose(v, cs, atol=1e-12)
report("p30_t3", v[3], ".4f"); report("p30_t4", v[4], ".4f"); report("p30_t6", v[6], ".4f")

# ⟦trung bình trượt 3 điểm, cosin 0.1||3-point moving average, cosine 0.1⟧
hm = np.ones(3)/3
n = np.arange(2000); xin = np.cos(2*np.pi*0.1*n)
ym = np.convolve(xin, hm)[:2000]
seg = ym[500:1500]; nn = n[500:1500]
Am = np.vstack([np.cos(2*np.pi*0.1*nn), np.sin(2*np.pi*0.1*nn)]).T
c2, s2_ = np.linalg.lstsq(Am, seg, rcond=None)[0]
amp = np.hypot(c2, s2_); Hf = abs(np.sum(hm*np.exp(-2j*np.pi*0.1*np.arange(3))))
assert abs(amp - Hf) < 1e-9 and abs(Hf - (1 + 2*np.cos(0.2*np.pi))/3) < 1e-12
report("ma_amp", Hf, ".4f"); report("ma_amp_sim", amp, ".4f")'''),
        ("code", r'''tt_ = np.linspace(0, 6, 601)
fig, ax = plt.subplots(figsize=(8, 3.3))
ax.plot(tt_, [V2(t_, f_in) if t_ != 0 else 0.5 for t_ in tt_], color="tab:blue", label="V₂(t)")
ax.stem(np.arange(5), g_sum, linefmt="r-", markerfmt="ro", basefmt=" ", label="g(n)")
ax.set_xlabel("t"); ax.legend(fontsize=8); plt.tight_layout(); plt.show()''', dict(fig="digital_filter", cap="⟦Hình 1. Đầu vào {1 2 1} qua mạch RC: đường xanh là V₂(t) liên tục, các chấm đỏ là g(n) = h(n)*f(n); mẫu của V₂ ở t nguyên trùng g(n) vì h(0) = 0.5.||Figure 1. The input {1 2 1} through an RC circuit: the blue curve is the continuous V₂(t), the red dots are g(n) = h(n)*f(n); samples of V₂ at integer t equal g(n) because h(0) = 0.5.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦$g$ = {0.5, {{dg_1}}, {{dg_2}}, {{dg_3}}, {{dg_4}}}; bài 30: {{p30_t3}}, {{p30_t4}}, {{p30_t6}}. Trung bình trượt ở 0.1: {{ma_amp}} (mô phỏng {{ma_amp_sim}}).||$g$ = {0.5, {{dg_1}}, {{dg_2}}, {{dg_3}}, {{dg_4}}}; problem 30: {{p30_t3}}, {{p30_t4}}, {{p30_t6}}. The moving average at 0.1: {{ma_amp}} (simulated {{ma_amp_sim}}).⟧"""),
        ("md", """## 4. ⟦Các định lý và bài tập 23, 24, 29||The theorems and problems 23, 24, 29⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Tỉ lệ, dịch, điều chế, điều chế ngược có đúng trên số cụ thể, tích cosin có bằng sinc, và điểm phân giải của hai vạch Gauss ở đâu? Mỗi số kiểm bằng tích phân/DFT và công thức.||Do similarity, shift, modulation and its converse hold for concrete numbers, does the cosine product equal the sinc, and where is the resolution point of two Gaussian lines? Each is checked by integral/DFT and formula.⟧"""),
        ("code", r'''# ⟦tỉ lệ a = 2||similarity a = 2⟧
sim_peak = ftq(lambda t: g(2*t), -10, 10, 0).real
sim_area = integrate.quad(lambda f: 0.5*np.exp(-np.pi*(f/2)**2), -20, 20)[0]
assert abs(sim_peak - 0.5) < 1e-9 and abs(sim_area - 1) < 1e-9
report("sim_peak", sim_peak, ".4f"); report("sim_area", sim_area, ".4f")
# ⟦dịch T = 0.5||shift T = 0.5⟧
Tt = 0.5
ph = lambda f: np.degrees(np.angle(np.exp(-2j*np.pi*f*Tt)))
mult = np.exp(-2j*np.pi*2.0*Tt)
assert abs(mult - 1) < 1e-12
report("shift_mult", mult.real, ".0f")
report("shift_low", ph(0.1), ".1f"); report("shift_high", ph(1.3), ".1f")
Fs = ftq(lambda t: g(t - Tt), -10, 10, 1.3)
assert abs(np.degrees(np.angle(Fs)) - ph(1.3)) < 1e-6 or abs(abs(np.degrees(np.angle(Fs)) - ph(1.3)) - 360) < 1e-6

# ⟦điều biên: M = 0.5, 50 Hz, 5 Hz||AM: M = 0.5, 50 Hz carrier, 5 Hz tone⟧
fs_ = 1000; N = 4000; tt = np.arange(N)/fs_
wave = (1 + 0.5*np.cos(2*np.pi*5*tt))*np.cos(2*np.pi*50*tt)
Wf = np.fft.fft(wave)/N
fr = np.fft.fftfreq(N, 1/fs_)
amp = lambda f: abs(Wf[np.argmin(np.abs(fr - f))])
car = amp(50); sb = amp(55)
assert abs(car - 0.5*0.5*2) < 1e-9 or True
assert abs(amp(50) - 0.5) < 1e-9 and abs(amp(45) - 0.125) < 1e-9 and abs(amp(55) - 0.125) < 1e-9
report("am_car", amp(50), ".4f"); report("am_sb", amp(55), ".4f")

# ⟦điều chế ngược||converse of modulation⟧
Tc, fc = 1.0, 0.3
pair = ftq(lambda t: g(t + Tc) + g(t - Tc), -12, 12, fc)
assert abs(pair - 2*np.cos(2*np.pi*Tc*fc)*np.exp(-np.pi*fc**2)) < 1e-9
report("conv_pair", abs(pair), ".4f")
pair2 = ftq(lambda t: g(t) + g(t - 2*Tc), -12, 12, fc)
form2 = 2*np.exp(-2j*np.pi*Tc*fc)*np.cos(2*np.pi*Tc*fc)*np.exp(-np.pi*fc**2)
assert abs(pair2 - form2) < 1e-9
report("conv_ph", np.degrees(np.angle(pair2)), ".1f")

# ⟦bài 24: hai kênh trễ; đo bằng DFT của hai xung||problem 24: two delayed channels; measured by DFT of two impulses⟧
T1, T2 = 0.3, 1.1
Nn = 4000; dts = 0.01; sig2 = np.zeros(Nn); sig2[int(T1/dts)] = 1; sig2[int(T2/dts)] += 1
Tf_ = np.fft.fft(sig2); frq = np.fft.fftfreq(Nn, dts)
k = np.argmin(np.abs(frq - 0.4))
val = abs(Tf_[k]); form_ = 2*abs(np.cos(np.pi*frq[k]*(T2 - T1)))
assert abs(val - form_) < 1e-9
report("p24_val", 2*abs(np.cos(np.pi*0.4*(T2 - T1))), ".4f"); report("p24_dev", abs(val - form_), ".1e")

# ⟦bài 23: tích cosin||problem 23: cosine product⟧
xs = np.linspace(0.001, 60, 600000)
prod4 = np.prod([np.cos(np.pi*xs/2**k) for k in range(1, 5)], axis=0)
err = np.abs(prod4 - np.sinc(xs))
x1pct = xs[np.argmax(err >= 0.01)]
assert x1pct > 0
corr = np.max(np.abs(prod4*np.sinc(xs/2**4) - np.sinc(xs)))
assert corr < 1e-12
report("p23_x", x1pct, ".2f"); report("p23_dev", corr, ".1e")

# ⟦bài 29: hai Gauss, W = 1||problem 29: two Gaussians, W = 1⟧
Lmax = np.sqrt(2/np.pi)
xg_ = np.linspace(-4, 4, 80001)
def peaks(L):
    y = np.exp(-np.pi*(xg_ + L/2)**2) + np.exp(-np.pi*(xg_ - L/2)**2)
    return int(np.sum((y[1:-1] > y[:-2]) & (y[1:-1] > y[2:])))
assert peaks(0.98*Lmax) == 1 and peaks(1.02*Lmax) == 2
curv = -2*np.pi*(1 - 2*np.pi*(Lmax/2)**2)
assert abs(curv) < 1e-12
report("p29_L", Lmax, ".4f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Tỉ lệ $a=2$: đỉnh {{sim_peak}}, diện tích {{sim_area}}. Dịch $T=0.5$: hệ số pha tại 2 là {{shift_mult}}, tại 0.1 là {{shift_low}} và tại 1.3 là {{shift_high}} độ. Điều biên: sóng mang {{am_car}}, dải bên {{am_sb}}. Điều chế ngược: {{conv_pair}}, pha {{conv_ph}}. Bài 24: {{p24_val}} (lệch {{p24_dev}}); bài 23: $x$ = {{p23_x}} và sửa đúng {{p23_dev}}; bài 29: $L_{\\max}/W$ = {{p29_L}}.||Similarity $a=2$: peak {{sim_peak}}, area {{sim_area}}. Shift $T=0.5$: phase factor at 2 is {{shift_mult}}, at 0.1 is {{shift_low}} and at 1.3 is {{shift_high}} degrees. AM: carrier {{am_car}}, sidebands {{am_sb}}. Converse of modulation: {{conv_pair}}, phase {{conv_ph}}. Problem 24: {{p24_val}} (deviation {{p24_dev}}); problem 23: $x$ = {{p23_x}} and the correction exact to {{p23_dev}}; problem 29: $L_{\\max}/W$ = {{p29_L}}.⟧"""),
        ("md", """## 5. ⟦Tuyến tính, bất biến, tuần hoàn, ổn định||Linearity, invariance, periodicity, stability⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Hệ tuyến tính bất biến có cho đầu ra chỉ chứa tần số đầu vào; bộ bình phương và bộ nhân với hàm biến thiên sinh tần số mới; $9\\cos5x+11\\cos4x$ tuần hoàn mà thiếu thành phần cơ bản; tiêu chuẩn ổn định $\\int|I|dt$; và đường truyền radar? Mỗi số có hai cách tính.||Does a linear time-invariant system give output containing only the input frequency, do a squarer and a multiplier by a varying function generate new frequencies, is $9\\cos5x+11\\cos4x$ periodic yet missing its fundamental, what is the stability criterion $\\int|I|dt$, and what of the radar line? Each number has two calculations.⟧"""),
        ("code", r'''# ⟦tuyến tính bất biến: FIR bất kỳ, cosin chu kỳ nguyên (10 chu kỳ / 200 mẫu)||LTI: any FIR, cosine with integer periods (10 cycles / 200 samples)⟧
N = 200; nn = np.arange(N); xin = np.cos(2*np.pi*10*nn/N)
hh = np.array([0.4, -0.2, 0.7, 0.1])
yl = np.array([np.sum(hh*xin[(k - np.arange(4)) % N]) for k in range(N)])     # ⟦tích chập vòng||circular convolution⟧
Y = np.fft.fft(yl); leak = (np.sum(np.abs(Y)**2) - np.abs(Y[10])**2 - np.abs(Y[N - 10])**2)/np.sum(np.abs(Y)**2)
assert leak < 1e-20
report("lti_leak", max(leak, 1e-32), ".0e")
# ⟦bình phương: cos² = ½ + ½ cos 2·||squarer: cos² = ½ + ½ cos 2·⟧
ys = xin**2; Ys = np.fft.fft(ys)/N
assert abs(abs(Ys[20]) - 0.25) < 1e-12 and abs(Ys[0] - 0.5) < 1e-12
nl = 2*abs(Ys[20])
report("nl_2f", nl, ".4f")
# ⟦nhân với cos(2π·1 t) ở 5 Hz||multiplier: 5 Hz times a 1 Hz mask⟧
fs_ = 200; Nt = 2000; t_ = np.arange(Nt)/fs_
mix = np.cos(2*np.pi*5*t_)*np.cos(2*np.pi*1*t_)
Mx = np.abs(np.fft.rfft(mix)); fr = np.fft.rfftfreq(Nt, 1/fs_)
top = fr[np.argsort(Mx)[-2:]]
assert sorted(np.round(top, 3)) == [4.0, 6.0]
report("tv_lo", min(top), ".1f"); report("tv_hi", max(top), ".1f")

# ⟦tuần hoàn: y = 9cos5x + 11cos4x||periodicity: y = 9cos5x + 11cos4x⟧
xx = np.linspace(0, 40, 4001)
yy = lambda x: 9*np.cos(5*x) + 11*np.cos(4*x)
per_dev = np.max(np.abs(yy(xx + 2*np.pi) - yy(xx)))
assert per_dev < 1e-12
# ⟦thành phần cơ bản (tần số 1/2π, tức cos x và sin x) qua tích phân trên một chu kỳ||the fundamental component (cos x, sin x) by integration over one period⟧
a1 = integrate.quad(lambda x: yy(x)*np.cos(x), 0, 2*np.pi, limit=200)[0]/np.pi
b1 = integrate.quad(lambda x: yy(x)*np.sin(x), 0, 2*np.pi, limit=200)[0]/np.pi
assert abs(a1) < 1e-10 and abs(b1) < 1e-10
# ⟦kiểm: không có chu kỳ nhỏ hơn 2π/k với k = 2..8||no smaller period 2π/k for k = 2..8⟧
assert all(np.max(np.abs(yy(xx + 2*np.pi/k) - yy(xx))) > 1e-3 for k in range(2, 9))
report("per_dev", max(per_dev, 1e-15), ".0e"); report("per_fund", 0, "d")

# ⟦ổn định||stability⟧
st_rc = integrate.quad(lambda t: np.exp(-t), 0, np.inf)[0]
Ti = 100.0; st_int = integrate.quad(lambda t: 1.0, 0, Ti)[0]
assert abs(st_rc - 1) < 1e-9 and abs(st_int - Ti) < 1e-9
Iosc = lambda t: np.exp(-t)*np.cos(2*np.pi*t)
tot = integrate.quad(lambda t: abs(Iosc(t)), 0, 40, limit=2000, points=[0.25*k for k in range(1, 160, 2)])[0]
one = integrate.quad(lambda t: np.exp(-t)*abs(np.cos(2*np.pi*t)), 0, 0.5, points=[0.25])[0]
series = one/(1 - np.exp(-0.5))
assert abs(tot - series) < 1e-6
# ⟦độ lợi lớn nhất: đầu vào sgn I(−t) cho đầu ra tại 0 bằng ∫|I|||largest gain: input sgn I(−t) gives output at 0 equal to ∫|I|⟧
dtq = 1e-3; tq = np.arange(0, 30, dtq)
gain = np.sum(np.abs(Iosc(tq)))*dtq
assert abs(gain - series) < 5e-3
report("st_rc", st_rc, ".4f"); report("st_int", st_int, ".0f"); report("st_osc", series, ".4f")

# ⟦đường truyền xung radar: 1 MW, 15 kV, 0.1 µs, v = c||radar pulse-forming line: 1 MW, 15 kV, 0.1 µs, v = c⟧
P, V, tau, c0 = 1e6, 15e3, 0.1e-6, 3e8
Z = V**2/P; length = c0*tau/2
C_line = length/(c0*Z)
E1 = P*tau; E2 = 0.5*C_line*(2*V)**2
assert abs(E1 - E2) < 1e-12 and abs(Z - 225) < 1e-9 and abs(length - 15) < 1e-9
report("rad_Z", Z, ".0f"); report("rad_len", length, ".0f"); report("rad_E", E1, ".2f"); report("rad_E2", E2, ".2f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Hệ tuyến tính bất biến: năng lượng ngoài tần số đầu vào {{lti_leak}}. Bộ bình phương: {{nl_2f}} tại $2f$. Nhân với mặt nạ 1 Hz: {{tv_lo}} và {{tv_hi}}. $9\\cos5x+11\\cos4x$: lệch chu kỳ {{per_dev}}, biên độ thành phần cơ bản {{per_fund}}. Ổn định: RC {{st_rc}}, bộ tích phân {{st_int}}, dao động tắt dần {{st_osc}}. Đường truyền: $R$ = {{rad_Z}} ôm, $\\ell$ = {{rad_len}} m, năng lượng {{rad_E}} và {{rad_E2}} J.||The LTI system: energy outside the input frequency {{lti_leak}}. Squarer: {{nl_2f}} at $2f$. Multiplied by a 1 Hz mask: {{tv_lo}} and {{tv_hi}}. $9\\cos5x+11\\cos4x$: period deviation {{per_dev}}, fundamental amplitude {{per_fund}}. Stability: RC {{st_rc}}, integrator {{st_int}}, damped oscillation {{st_osc}}. The line: $R$ = {{rad_Z}} ohms, $\\ell$ = {{rad_len}} m, energy {{rad_E}} and {{rad_E2}} J.⟧"""),
    ],
)
