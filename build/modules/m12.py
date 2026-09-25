from lib import F, C, UL, OL, TBL

MOD = dict(
    n=12, slug="random-processes-noise", part="B", book="BK",
    title="⟦Quá trình ngẫu nhiên, phổ công suất và nhiễu||Random processes, power spectra and noise⟧",
    blurb="⟦Từ chuỗi chữ số ngẫu nhiên và nhiễu qua bộ lọc (Bracewell) tới quá trình dừng, tự tương quan, mật độ phổ công suất, hệ tuyến tính, ergodic, lấy mẫu, tín hiệu giải tích và nhiễu nhiệt (Barkat).||"
          "From random digits and noise through filters (Bracewell) to stationary processes, autocorrelation, power spectral density, linear systems, ergodicity, sampling, analytic signals and thermal noise (Barkat).⟧",
    src="⟦Bracewell, chương 17, tr. 446–472; Barkat, chương 3, tr. 141–221||Bracewell, chapter 17, pp. 446–472; Barkat, chapter 3, pp. 141–221⟧",
    data="⟦Sinh bằng mã: pha ngẫu nhiên, nhị phân ngẫu nhiên, bước đi ngẫu nhiên, Wiener, chữ số số $\\pi$, nhiễu thông dải, mạch RC, nhiễu nhiệt||Generated in code: random phase, random binary, random walk, Wiener, digits of $\\pi$, bandpass noise, an RC circuit, thermal noise⟧",
    objectives=[
        "⟦Định nghĩa quá trình ngẫu nhiên, trung bình, tự tương quan, dừng theo nghĩa rộng và chặt, và kiểm bằng mô phỏng tập hợp.||Define a random process, its mean and autocorrelation, wide- and strict-sense stationarity, and check them by ensemble simulation.⟧",
        "⟦Nhận biết các quá trình mẫu: xung ngẫu nhiên, tuần hoàn, Gauss, Poisson, Bernoulli, bước đi ngẫu nhiên, Wiener, Markov.||Recognise the standard processes: random pulses, periodic, Gaussian, Poisson, Bernoulli, random walk, Wiener, Markov.⟧",
        "⟦Liên hệ tự tương quan và mật độ phổ công suất, và tính đầu ra của hệ tuyến tính bất biến với đầu vào ngẫu nhiên: $S_{yy}=|H|^2S_{xx}$.||Relate autocorrelation and power spectral density, and compute the output of a linear time-invariant system with random input: $S_{yy}=|H|^2S_{xx}$.⟧",
        "⟦Giải thích vì sao nhiễu qua bộ lọc trở nên Gauss, đường bao là Rayleigh, tách sóng bình phương cho phân bố mũ, và độ chính xác đo công suất nhiễu là $1/\\sqrt{T\\Delta f}$.||Explain why noise through a filter becomes Gaussian, why the envelope is Rayleigh, why square-law detection gives an exponential distribution, and why the precision of noise power measurement is $1/\\sqrt{T\\Delta f}$.⟧",
        "⟦Dùng ergodic, định lý lấy mẫu cho quá trình ngẫu nhiên, biến đổi Hilbert và tín hiệu giải tích, và nhiễu nhiệt.||Use ergodicity, the sampling theorem for random processes, the Hilbert transform and analytic signals, and thermal noise.⟧",
    ],
    parts=[
        # ------------------------------------------------ PART 1
        dict(
            title="⟦Định nghĩa, thống kê bậc một và hai, tính dừng||Definitions, first- and second-order statistics, stationarity⟧",
            scr=("⟦Tín hiệu đo được luôn kèm biến động ngẫu nhiên: nhiễu, phân rã, dao động; một biến ngẫu nhiên không đủ mô tả chúng.||Measured signals always carry random fluctuation: noise, decays, oscillations; a single random variable cannot describe them.⟧",
                 "⟦Ta cần một họ biến ngẫu nhiên theo thời gian, với đặc trưng là trung bình và tự tương quan.||We need a family of random variables indexed by time, characterised by the mean and autocorrelation.⟧",
                 "⟦Nếu trung bình không đổi và tự tương quan chỉ phụ thuộc hiệu thời gian, quá trình dừng theo nghĩa rộng và có phổ công suất.||If the mean is constant and the autocorrelation depends only on the time difference, the process is wide-sense stationary and has a power spectrum.⟧"),
            preview=["⟦Quá trình ngẫu nhiên và tập hợp||A random process and its ensemble⟧", "⟦Trung bình, tự tương quan, dừng||Mean, autocorrelation, stationarity⟧", "⟦Tính chất của hàm tương quan||Properties of correlation functions⟧"],
            slides=[
                ("⟦Tín hiệu ngẫu nhiên trong vật lý||Random signals in physics⟧",
                 "<p>⟦Toàn bộ vật lý thấm đầy các hiện tượng ngẫu nhiên tự nhiên. Bracewell mở đầu bằng bản ghi nguồn vô tuyến ngoài thiên hà Cygnus A đi qua búp sóng của kính thiên văn vô tuyến: nguồn ít nhất gồm hai phần, nhưng có vầng rộng hơn, yếu hơn hay không thì không thấy được vì các \"gợn\" ngẫu nhiên; nguồn thiên văn bản thân cũng là nhiễu ngẫu nhiên (chương 17, tr. 445 đến 447). Các dao động thường có hành vi đặc trưng không phụ thuộc nguyên nhân vật lý, và chương này nói về những hiện tượng phổ quát ấy.||The whole of physics is permeated by naturally occurring random phenomena. Bracewell opens with a record of the extragalactic radio source Cygnus A passing through the beam of a radio telescope: the source has at least two parts, but whether there is a broader, weaker halo cannot be revealed because of unwanted random wiggles; the wanted radiation itself is random noise (chapter 17, pp. 445 to 447). Fluctuations often show characteristic behaviour independent of their precise physical cause, and this chapter is about those universal phenomena.⟧</p>"),
                ("⟦Định nghĩa quá trình ngẫu nhiên||Definition of a random process⟧",
                 "<p>⟦Một quá trình ngẫu nhiên có thể xem là một họ biến ngẫu nhiên với thời gian $t$ là tham số chạy qua mọi số thực; hình thức, $X(t)$ ánh xạ mỗi phần tử của không gian mẫu tới một hàm thời gian. Tập các hàm mẫu cùng xác suất gọi là tập hợp (ensemble), hàm mẫu ký hiệu $x(t)$ (Barkat, mục 3.1, tr. 141). Cố định $t=t_0$ thì $X(t_0)$ là biến ngẫu nhiên. Ví dụ: $X(t)=A\\cos(\\omega t+\\Theta)$ với $\\Theta$ đều trên $(0,2\\pi)$; dao động chỉ do pha, nhưng khi pha cố định hàm mẫu là tất định (tr. 142).||A random process may be viewed as a collection of random variables with time $t$ as a parameter running through all real numbers; formally $X(t)$ maps each element of the sample space into a function of time. The set of sample functions with their probabilities is the ensemble, a sample function is denoted $x(t)$ (Barkat, section 3.1, p. 141). Fixing $t=t_0$ makes $X(t_0)$ a random variable. Example: $X(t)=A\\cos(\\omega t+\\Theta)$ with $\\Theta$ uniform on $(0,2\\pi)$; the variation is due to phase only, yet with the phase fixed the sample function is deterministic (p. 142).⟧</p>"),
                ("⟦Bốn loại quá trình||Four types of process⟧",
                 TBL(["⟦Trạng thái||State⟧", "⟦Thời gian||Time⟧", "⟦Tên||Name⟧"],
                     [["⟦Liên tục||Continuous⟧", "⟦Liên tục||Continuous⟧", "⟦Quá trình liên tục||Continuous random process⟧"], ["⟦Rời rạc||Discrete⟧", "⟦Liên tục||Continuous⟧", "⟦Quá trình rời rạc||Discrete random process⟧"],
                      ["⟦Liên tục||Continuous⟧", "⟦Rời rạc||Discrete⟧", "⟦Dãy ngẫu nhiên liên tục||Continuous random sequence⟧"], ["⟦Rời rạc||Discrete⟧", "⟦Rời rạc||Discrete⟧", "⟦Dãy ngẫu nhiên rời rạc||Discrete random sequence⟧"]])
                 + "<p>⟦(Barkat, tr. 143). Chuỗi chữ số của Bracewell là dãy rời rạc ở cả hai; nội suy sinc biến nó thành quá trình liên tục giới hạn băng.||(Barkat, p. 143). Bracewell's digit sequence is discrete in both; sinc interpolation turns it into a band-limited continuous process.⟧</p>"),
                ("⟦Phân bố bậc một và bậc hai||First- and second-order distributions⟧",
                 "<p>⟦Phân bố bậc một $F_X(x;t)=P[X(t)\\le x]$, mật độ bậc một $f_X(x;t)$; bậc hai là phân bố đồng thời của $X(t_1)$ và $X(t_2)$; mô tả đầy đủ cần mọi bậc (Barkat, tr. 143 đến 144). May thay ta thường quan tâm quá trình có tính đều để biết bậc một và hai là đủ, gồm trung bình $m_x(t)=E[X(t)]$ và tự tương quan $R_{xx}(t_1,t_2)=E[X(t_1)X(t_2)]$ (tr. 145).||The first-order distribution is $F_X(x;t)=P[X(t)\\le x]$, the first-order density $f_X(x;t)$; the second order is the joint distribution of $X(t_1)$ and $X(t_2)$; a complete description needs all orders (Barkat, pp. 143 to 144). Fortunately we are usually interested in processes with regularity so that the first and second orders suffice, including the mean $m_x(t)=E[X(t)]$ and the autocorrelation $R_{xx}(t_1,t_2)=E[X(t_1)X(t_2)]$ (p. 145).⟧</p>"),
                ("⟦Dừng theo nghĩa rộng và chặt||Wide-sense and strict-sense stationarity⟧",
                 "<p>⟦Nếu $m_x$ không đổi và $R_{xx}(t_1,t_2)$ chỉ phụ thuộc $\\tau=t_1-t_2$ thì $X(t)$ dừng theo nghĩa rộng: $R_{xx}(t+\\tau,t)=R_{xx}(\\tau)$. Dừng theo nghĩa chặt nếu mọi thống kê không đổi khi dịch gốc thời gian; dừng chặt kéo theo dừng rộng nhưng không ngược lại, vì điều kiện rộng chỉ ràng buộc thống kê bậc hai (Barkat, tr. 145 đến 146). Ví dụ 3.1: $X=A\\cos(\\omega t+\\Theta)$: trung bình {{rp_mean}} và $R_{xx}(\\tau)=\\tfrac{A^2}2\\cos\\omega\\tau$; với $A=2$, $f=1$, $\\tau=0.1$: {{rp_R}} theo công thức và mô phỏng tập hợp, tại hai thời điểm $t$ khác nhau.||If $m_x$ is constant and $R_{xx}(t_1,t_2)$ depends only on $\\tau=t_1-t_2$ then $X(t)$ is wide-sense stationary: $R_{xx}(t+\\tau,t)=R_{xx}(\\tau)$. It is strictly stationary if all statistics are unchanged by a shift of time origin; strict implies wide-sense but not conversely, since the wide-sense condition constrains only second-order statistics (Barkat, pp. 145 to 146). Example 3.1: $X=A\\cos(\\omega t+\\Theta)$: mean {{rp_mean}} and $R_{xx}(\\tau)=\\tfrac{A^2}2\\cos\\omega\\tau$; with $A=2$, $f=1$, $\\tau=0.1$: {{rp_R}} by formula and by ensemble simulation, at two different times $t$.⟧</p>"
                 + F("⟦Tự tương quan||Autocorrelation⟧", r"R_{xx}(t+\tau,t)=E\big[X(t+\tau)X(t)\big]=R_{xx}(\tau)\quad(\text{WSS})")),
                ("⟦Ví dụ 3.2: tung đồng xu và truyền nhị phân ngẫu nhiên||Example 3.2: coin tossing and random binary transmission⟧",
                 "<p>⟦Tung đồng xu ở mỗi khoảng $T$; $X(t)=+1$ hay $-1$ trong khoảng thứ $n$ tùy mặt ngửa hay sấp. Trung bình 0, bình phương trung bình 1. Nếu $t_1,t_2$ cùng khoảng thì $R_{xx}=1$; khác khoảng thì các lần tung độc lập nên $R_{xx}=E[X(t_1)]E[X(t_2)]=0$ (Barkat, ví dụ 3.2, tr. 147 đến 149). Số đo: cùng khoảng ({{rb_same}}), khác khoảng ({{rb_diff}}); vậy $R_{xx}$ phụ thuộc $t_1$ chứ không chỉ $\\tau$, không dừng rộng. Thêm độ dời ngẫu nhiên đều $\\Theta$ trong $(0,T)$ ta được $Y(t)=X(t-\\Theta)$ dừng rộng, gọi là truyền nhị phân ngẫu nhiên, với $R_{yy}(\\tau)=1-|\\tau|/T$: tại $\\tau=0.25T$ bằng {{rb_tri}} (tại hai $t$ khác nhau).||Toss a coin every interval $T$; $X(t)=+1$ or $-1$ in the $n$th interval according to heads or tails. The mean is 0, the mean square 1. If $t_1,t_2$ lie in the same interval $R_{xx}=1$; in different intervals the tosses are independent so $R_{xx}=E[X(t_1)]E[X(t_2)]=0$ (Barkat, example 3.2, pp. 147 to 149). Measured: same interval ({{rb_same}}), different intervals ({{rb_diff}}); so $R_{xx}$ depends on $t_1$, not just $\\tau$: not wide-sense stationary. Adding a uniform random shift $\\Theta$ in $(0,T)$ gives $Y(t)=X(t-\\Theta)$, wide-sense stationary, called random binary transmission, with $R_{yy}(\\tau)=1-|\\tau|/T$: at $\\tau=0.25T$ it equals {{rb_tri}} (at two different $t$).⟧</p>"),
                ("⟦Đồng phương sai, phức, tương quan chéo||Covariance, complex processes, cross-correlation⟧",
                 "<p>⟦Hai quá trình dừng chung nếu mỗi cái dừng và $R_{xy}(t+\\tau,t)=R_{xy}(\\tau)$. Hàm đồng phương sai $C_{xx}(t_1,t_2)=E\\{[X(t_1)-m_x(t_1)][X(t_2)-m_x(t_2)]\\}$, và với quá trình phức $Z=X+jY$: $R_{zz}(t_1,t_2)=E[Z(t_1)Z^*(t_2)]$ (Barkat, tr. 147). Ví dụ 3.3: $I(t)=X\\cos\\omega t+Y\\sin\\omega t$, $Q(t)=Y\\cos\\omega t-X\\sin\\omega t$ với $X,Y$ trung bình 0, không tương quan, phương sai $\\sigma^2$: $R_{iq}(t+\\tau,t)=\\sigma^2\\sin\\omega\\tau$ (tr. 152; bản in ghi dấu âm, nhưng bước trung gian của chính sách và mô phỏng đều cho dấu dương). Với $\\sigma=1$, $f=1$, $\\tau=0.1$: {{iq_r}}.||Two processes are jointly stationary if each is stationary and $R_{xy}(t+\\tau,t)=R_{xy}(\\tau)$. The covariance function is $C_{xx}(t_1,t_2)=E\\{[X(t_1)-m_x(t_1)][X(t_2)-m_x(t_2)]\\}$, and for a complex process $Z=X+jY$: $R_{zz}(t_1,t_2)=E[Z(t_1)Z^*(t_2)]$ (Barkat, p. 147). Example 3.3: $I(t)=X\\cos\\omega t+Y\\sin\\omega t$, $Q(t)=Y\\cos\\omega t-X\\sin\\omega t$ with $X,Y$ zero-mean, uncorrelated, variance $\\sigma^2$: $R_{iq}(t+\\tau,t)=\\sigma^2\\sin\\omega\\tau$ (p. 152; the printed result has a minus sign, but the book's own intermediate step and the simulation give a plus). With $\\sigma=1$, $f=1$, $\\tau=0.1$: {{iq_r}}.⟧</p>"),
                ("⟦Tính chất của tự tương quan||Properties of the autocorrelation⟧",
                 UL(["⟦$R_{xx}(t_2,t_1)=R_{xx}^*(t_1,t_2)$; nếu thực thì đối xứng qua $t_1=t_2$.||$R_{xx}(t_2,t_1)=R_{xx}^*(t_1,t_2)$; if real it is symmetric about $t_1=t_2$.⟧",
                     "⟦$R_{xx}(t,t)=E[|X(t)|^2]\\ge0$ và bất đẳng thức Schwarz $|R_{xx}(t_1,t_2)|^2\\le E[|X(t_1)|^2]E[|X(t_2)|^2]$.||$R_{xx}(t,t)=E[|X(t)|^2]\\ge0$ and Schwarz's inequality $|R_{xx}(t_1,t_2)|^2\\le E[|X(t_1)|^2]E[|X(t_2)|^2]$.⟧",
                     "⟦Xác định không âm: $\\sum_i\\sum_ja_ia_j^*R_{xx}(t_i,t_j)\\ge0$.||Nonnegative definite: $\\sum_i\\sum_ja_ia_j^*R_{xx}(t_i,t_j)\\ge0$.⟧",
                     "⟦Với dừng rộng thực: $R_{xx}(-\\tau)=R_{xx}(\\tau)$, $R_{xx}(0)=\\sigma_x^2+m_x^2$, $|R_{xx}(\\tau)|\\le R_{xx}(0)$, và $R_{xx}(\\infty)=m_x^2$.||For a real wide-sense stationary process: $R_{xx}(-\\tau)=R_{xx}(\\tau)$, $R_{xx}(0)=\\sigma_x^2+m_x^2$, $|R_{xx}(\\tau)|\\le R_{xx}(0)$, and $R_{xx}(\\infty)=m_x^2$.⟧"])
                 + "<p>⟦(Barkat, mục 3.3, tr. 153 đến 155). Tương quan chéo: $R_{xy}(\\tau)=R_{yx}^*(-\\tau)$ và $|R_{xy}(\\tau)|^2\\le R_{xx}(0)R_{yy}(0)$. Số đo với pha ngẫu nhiên: $R(0)$ = {{rp_R0}} $=A^2/2$ và $|R(\\tau)|\\le R(0)$ trên lưới.||(Barkat, section 3.3, pp. 153 to 155). Cross-correlation: $R_{xy}(\\tau)=R_{yx}^*(-\\tau)$ and $|R_{xy}(\\tau)|^2\\le R_{xx}(0)R_{yy}(0)$. Measured with random phase: $R(0)$ = {{rp_R0}} $=A^2/2$ and $|R(\\tau)|\\le R(0)$ on a grid.⟧</p>"),
                ("⟦Tự kiểm tra phần 1||Self-check, part 1⟧",
                 UL(["⟦Vì sao tung đồng xu theo khoảng không dừng rộng, mà thêm độ dời ngẫu nhiên thì có?||Why is coin tossing by intervals not wide-sense stationary, yet adding a random shift makes it so?⟧",
                     "⟦$R_{xx}(0)$ bằng gì?||What does $R_{xx}(0)$ equal?⟧",
                     "⟦Dừng chặt và dừng rộng khác nhau thế nào?||How do strict and wide-sense stationarity differ?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: $R$ phụ thuộc vị trí trong khoảng, độ dời đều làm trung bình hóa vị trí; $E[X^2]=\\sigma^2+m^2$; chặt ràng buộc mọi bậc.||Hints: $R$ depends on position within an interval, a uniform shift averages the position out; $E[X^2]=\\sigma^2+m^2$; strict constrains all orders.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 2
        dict(
            title="⟦Một số quá trình ngẫu nhiên tiêu biểu||Some representative random processes⟧",
            scr=("⟦Radar thu xung có biên độ và thời điểm đến ngẫu nhiên; nhiễu là tổng nhiều đóng góp; số cuộc gọi là Poisson; hạt Brown là bước đi ngẫu nhiên.||Radar receives pulses with random amplitude and arrival time; noise is a sum of many contributions; calls form a Poisson process; a Brownian particle performs a random walk.⟧",
                 "⟦Mỗi bài toán ứng với một mô hình có trung bình và tự tương quan tính được.||Each problem has a model whose mean and autocorrelation can be computed.⟧",
                 "⟦Xung ngẫu nhiên, tuần hoàn, Gauss, Poisson, Bernoulli, bước đi ngẫu nhiên và Wiener, Markov.||Random pulses, periodic, Gaussian, Poisson, Bernoulli, random walk and Wiener, Markov.⟧"),
            preview=["⟦Xung ngẫu nhiên và quá trình tuần hoàn||Random pulses and periodic processes⟧", "⟦Gauss, Poisson, Bernoulli||Gaussian, Poisson, Bernoulli⟧", "⟦Bước đi ngẫu nhiên, Wiener, Markov||Random walk, Wiener, Markov⟧"],
            slides=[
                ("⟦Xung đã biết dạng, biên độ và thời điểm đến ngẫu nhiên||A pulse of known shape, random amplitude and arrival time⟧",
                 "<p>⟦Trong radar và sonar, tín hiệu về là $X(t)=A\\,s(t-\\Theta)$ với $A$ và $\\Theta$ độc lập và $s$ tất định. Trung bình $E[X(t)]=E[A]\\,[s*f_\\Theta](t)$ là tích chập của xung với mật độ của thời điểm đến, và $R_{xx}(t_1,t_2)=E[A^2]\\int s(t_1-\\theta)s(t_2-\\theta)f_\\Theta(\\theta)d\\theta$ (Barkat, mục 3.4.1, tr. 156 đến 157). Số đo: $s=\\Pi(t)$, $A$ đều trên $(1,3)$, $\\Theta$ đều trên $(0,1)$: $E[X(1.25)]$ = {{pl_e}} $=2\\times0.25$ và $R_{xx}(0.5,0.5)$ = {{pl_r}} $=E[A^2]$, bằng tích phân và mô phỏng.||In radar and sonar a returned signal is $X(t)=A\\,s(t-\\Theta)$ with independent $A$ and $\\Theta$ and deterministic $s$. The mean $E[X(t)]=E[A]\\,[s*f_\\Theta](t)$ is the convolution of the pulse with the density of the arrival time, and $R_{xx}(t_1,t_2)=E[A^2]\\int s(t_1-\\theta)s(t_2-\\theta)f_\\Theta(\\theta)d\\theta$ (Barkat, section 3.4.1, pp. 156 to 157). Measured: $s=\\Pi(t)$, $A$ uniform on $(1,3)$, $\\Theta$ uniform on $(0,1)$: $E[X(1.25)]$ = {{pl_e}} $=2\\times0.25$ and $R_{xx}(0.5,0.5)$ = {{pl_r}} $=E[A^2]$, by integration and simulation.⟧</p>"),
                ("⟦Nhiều xung||Multiple pulses⟧",
                 "<p>⟦$X(t)=\\sum_{k=1}^nA_ks(t-\\Theta_k)$ với $2n$ biến độc lập, $A_k$ cùng phân bố, $\\Theta_k$ cùng phân bố: $E[X(t)]=nE[A_k][s*f_\\Theta]$ và $R_{xx}=nE[A_k^2]\\int s s f_\\Theta+(n^2-n)E[A_k]^2\\prod\\int sf_\\Theta$ (mục 3.4.2, tr. 157 đến 158). Với $n=3$ trong ví dụ trước: $E[X(1.25)]$ = {{pl_e3}} theo công thức và mô phỏng.||$X(t)=\\sum_{k=1}^nA_ks(t-\\Theta_k)$ with $2n$ independent variables, the $A_k$ identically distributed and the $\\Theta_k$ identically distributed: $E[X(t)]=nE[A_k][s*f_\\Theta]$ and $R_{xx}=nE[A_k^2]\\int s s f_\\Theta+(n^2-n)E[A_k]^2\\prod\\int sf_\\Theta$ (section 3.4.2, pp. 157 to 158). With $n=3$ in the previous example: $E[X(1.25)]$ = {{pl_e3}} by formula and simulation.⟧</p>"),
                ("⟦Quá trình tuần hoàn và cyclostationary||Periodic and cyclostationary processes⟧",
                 "<p>⟦$X(t)$ tuần hoàn chu kỳ $T$ nếu mọi hàm mẫu tuần hoàn. Định lý: nếu $X$ dừng rộng thì $R_{xx}$ tuần hoàn khi và chỉ khi $X$ tuần hoàn (chứng minh qua Tchebycheff với $Y=X(t+T)-X(t)$, $\\sigma_y^2=2[R(0)-R(T)]$). Hệ quả: $X=s(t-\\Theta)$ với $s$ tuần hoàn và $\\Theta$ đều trên $(0,T)$ dừng rộng (Barkat, mục 3.4.3, tr. 158 đến 160). Quá trình cyclostationary có trung bình và tự tương quan tuần hoàn cùng chu kỳ; thêm độ dời ngẫu nhiên đều thì dừng, như nhị phân ngẫu nhiên ở phần 1. Số đo: $X=\\text{sq}(t-\\Theta)$ (sóng vuông biên độ 1, chu kỳ 1): trung bình {{cy_mean}}, $R(0)$ = {{cy_r0}}, $R(0.5)$ = {{cy_r5}}.||$X(t)$ is periodic with period $T$ if all sample functions are. Theorem: if $X$ is wide-sense stationary then $R_{xx}$ is periodic if and only if $X$ is periodic (proved through Chebyshev with $Y=X(t+T)-X(t)$, $\\sigma_y^2=2[R(0)-R(T)]$). Corollary: $X=s(t-\\Theta)$ with periodic $s$ and $\\Theta$ uniform on $(0,T)$ is wide-sense stationary (Barkat, section 3.4.3, pp. 158 to 160). A cyclostationary process has a mean and autocorrelation periodic with the same period; adding a uniform random shift makes it stationary, like the random binary transmission of part 1. Measured: $X=\\text{sq}(t-\\Theta)$ (square wave of amplitude 1, period 1): mean {{cy_mean}}, $R(0)$ = {{cy_r0}}, $R(0.5)$ = {{cy_r5}}.⟧</p>"),
                ("⟦Quá trình Gauss||The Gaussian process||⟧".replace("||⟧", "⟧"),
                 "<p>⟦$X(t)$ là Gauss nếu $X(t_1),\\ldots,X(t_n)$ đồng thời Gauss với mọi $n$ và mọi $t_i$. Vì Gauss nhiều chiều chỉ phụ thuộc vector trung bình và ma trận hiệp phương sai, quá trình Gauss dừng rộng thì cũng dừng chặt; và không tương quan là độc lập (Barkat, mục 3.4.4, tr. 161 đến 163). Đây là mô hình của nhiễu nhiệt và của nhiễu qua bộ lọc (giới hạn trung tâm). Số đo: quá trình $y_t=\\rho y_{t-1}+w_t$, $\\rho=0.8$, $\\sigma_w=1$ có $R(k)=\\sigma^2\\rho^{|k|}$ với $\\sigma^2=1/(1-\\rho^2)$ = {{ga_var}}: $R(1)$ = {{ga_r1}} theo mô phỏng và công thức.||$X(t)$ is Gaussian if $X(t_1),\\ldots,X(t_n)$ are jointly Gaussian for all $n$ and all $t_i$. Since the multivariate Gaussian depends only on the mean vector and covariance matrix, a wide-sense stationary Gaussian process is also strictly stationary; and uncorrelated means independent (Barkat, section 3.4.4, pp. 161 to 163). This is the model for thermal noise and for noise through filters (central limit). Measured: the process $y_t=\\rho y_{t-1}+w_t$, $\\rho=0.8$, $\\sigma_w=1$ has $R(k)=\\sigma^2\\rho^{|k|}$ with $\\sigma^2=1/(1-\\rho^2)$ = {{ga_var}}: $R(1)$ = {{ga_r1}} by simulation and by formula.⟧</p>"),
                ("⟦Quá trình Poisson||The Poisson process⟧",
                 "<p>⟦Chia $[0,t)$ thành $n$ khoảng rất nhỏ $\\Delta t$, mỗi khoảng là một phép thử Bernoulli độc lập với xác suất $\\lambda\\Delta t$ có một điểm. Số điểm $N(0,t)$ là nhị thức $n=t/\\Delta t$, $p=\\lambda\\Delta t$; ở giới hạn nó là Poisson $P[N=k]=(\\lambda t)^ke^{-\\lambda t}/k!$ (Barkat, mục 3.4.5, tr. 163 đến 166). Số đo: $\\lambda=2$, $t=1.5$, $k=3$: {{pp_p}} theo Poisson, theo nhị thức $n=10^6$ và mô phỏng; khoảng giữa các điểm có trung bình {{pp_ia}} $=1/\\lambda$ (đó là phân bố mũ của module 10).||Divide $[0,t)$ into $n$ tiny intervals $\\Delta t$, each an independent Bernoulli trial with probability $\\lambda\\Delta t$ of a point. The count $N(0,t)$ is binomial with $n=t/\\Delta t$, $p=\\lambda\\Delta t$; in the limit it is Poisson $P[N=k]=(\\lambda t)^ke^{-\\lambda t}/k!$ (Barkat, section 3.4.5, pp. 163 to 166). Measured: $\\lambda=2$, $t=1.5$, $k=3$: {{pp_p}} by Poisson, by the binomial with $n=10^6$ and by simulation; the intervals between points have mean {{pp_ia}} $=1/\\lambda$ (the exponential distribution of module 10).⟧</p>"),
                ("⟦Bernoulli và nhị thức||The Bernoulli and binomial processes⟧",
                 "<p>⟦Quá trình Bernoulli là dãy phép thử độc lập $X[n]\\in\\{0,1\\}$; tổng $S[n]=\\sum X[k]$ là quá trình nhị thức với $P[S[n]=k]=\\binom nk p^kq^{n-k}$ (Barkat, mục 3.4.6, tr. 166 đến 168). Poisson là giới hạn liên tục của nó. Số đo: $n=20$, $p=0.3$: $E[S]$ = {{bp_e}}, phương sai {{bp_v}}, và $P[S=6]$ = {{bp_p6}}.||The Bernoulli process is a sequence of independent trials $X[n]\\in\\{0,1\\}$; the sum $S[n]=\\sum X[k]$ is the binomial process with $P[S[n]=k]=\\binom nk p^kq^{n-k}$ (Barkat, section 3.4.6, pp. 166 to 168). Poisson is its continuous limit. Measured: $n=20$, $p=0.3$: $E[S]$ = {{bp_e}}, variance {{bp_v}}, and $P[S=6]$ = {{bp_p6}}.⟧</p>"),
                ("⟦Bước đi ngẫu nhiên||The random walk⟧",
                 "<p>⟦Tung đồng xu công bằng mỗi $T$ giây; bước sang phải $\\Delta$ nếu ngửa, sang trái nếu sấp: $X(nT)=(2k-n)\\Delta$ với $k$ số lần ngửa, $P=\\binom nk/2^n$. Trung bình 0, $E[X^2(n)]=n\\Delta^2$; nhờ gia số độc lập, $R_{xx}(n_1,n_2)=\\Delta^2\\min(n_1,n_2)$ (Barkat, mục 3.4.7, tr. 168 đến 170). Số đo với $\\Delta=1$, $n_1=10$, $n_2=25$: {{rw_r}} theo công thức và mô phỏng $2\\cdot10^5$ bước đi.||Toss a fair coin every $T$ seconds; step right by $\\Delta$ for heads, left for tails: $X(nT)=(2k-n)\\Delta$ with $k$ the number of heads, $P=\\binom nk/2^n$. The mean is 0, $E[X^2(n)]=n\\Delta^2$; thanks to independent increments, $R_{xx}(n_1,n_2)=\\Delta^2\\min(n_1,n_2)$ (Barkat, section 3.4.7, pp. 168 to 170). Measured with $\\Delta=1$, $n_1=10$, $n_2=25$: {{rw_r}} by formula and by simulating $2\\cdot10^5$ walks.⟧</p>"),
                ("⟦Quá trình Wiener||The Wiener process⟧",
                 "<p>⟦Wiener (Wiener-Levy, chuyển động Brown) là giới hạn của bước đi ngẫu nhiên khi $n\\to\\infty$, $T\\to0$ sao cho $nT=t$ và $\\Delta^2=\\alpha T$ giữ phương sai hữu hạn. Theo giới hạn trung tâm $W(t)$ là Gauss trung bình 0, phương sai $\\alpha t$, gia số độc lập, và $R_{ww}(t_1,t_2)=\\alpha\\min(t_1,t_2)$ (tr. 170 đến 171). Số đo với $\\alpha=0.5$: phương sai tại $t=4$ là {{wi_v}}, $R_{ww}(2,3)$ = {{wi_r}}; quá trình không dừng vì phương sai tăng theo $t$.||The Wiener process (Wiener-Levy, Brownian motion) is the limit of the random walk as $n\\to\\infty$, $T\\to0$ with $nT=t$ and $\\Delta^2=\\alpha T$ keeping the variance finite. By the central limit theorem $W(t)$ is Gaussian with mean 0, variance $\\alpha t$, independent increments, and $R_{ww}(t_1,t_2)=\\alpha\\min(t_1,t_2)$ (pp. 170 to 171). Measured with $\\alpha=0.5$: the variance at $t=4$ is {{wi_v}}, $R_{ww}(2,3)$ = {{wi_r}}; the process is not stationary since the variance grows with $t$.⟧</p>"),
                ("⟦Markov||The Markov process⟧",
                 "<p>⟦$X(t)$ là Markov (bậc nhất) nếu giá trị hiện tại chỉ phụ thuộc giá trị liền trước: $f(x_n\\mid x_{n-1},\\ldots,x_1)=f(x_n\\mid x_{n-1})$; khi biết hiện tại thì quá khứ và tương lai độc lập; mật độ chung $f(x_1)\\prod f(x_k\\mid x_{k-1})$ (Barkat, mục 3.4.8, tr. 172 đến 173). Phương trình Chapman-Kolmogorov: $f(x_n\\mid x_m)=\\int f(x_n\\mid x_k)f(x_k\\mid x_m)dx_k$ với $m<k<n$. Số đo với $X_n=\\rho X_{n-1}+w_n$ Gauss ($\\rho=0.8$): mật độ hai bước tại $x_2=1$ cho $x_0=1$ là {{mk_ck}} theo tích phân Chapman-Kolmogorov và theo $N(\\rho^2x_0,\\sigma_w^2(1+\\rho^2))$.||$X(t)$ is (first-order) Markov if the present value depends only on the previous one: $f(x_n\\mid x_{n-1},\\ldots,x_1)=f(x_n\\mid x_{n-1})$; given the present, past and future are independent; the joint density is $f(x_1)\\prod f(x_k\\mid x_{k-1})$ (Barkat, section 3.4.8, pp. 172 to 173). The Chapman-Kolmogorov equation: $f(x_n\\mid x_m)=\\int f(x_n\\mid x_k)f(x_k\\mid x_m)dx_k$ for $m<k<n$. Measured with the Gaussian $X_n=\\rho X_{n-1}+w_n$ ($\\rho=0.8$): the two-step density at $x_2=1$ given $x_0=1$ is {{mk_ck}} by the Chapman-Kolmogorov integral and by $N(\\rho^2x_0,\\sigma_w^2(1+\\rho^2))$.⟧</p>"),
                ("⟦Tự kiểm tra phần 2||Self-check, part 2⟧",
                 UL(["⟦$R_{xx}$ của bước đi ngẫu nhiên là gì và vì sao?||What is $R_{xx}$ of the random walk and why?⟧",
                     "⟦Quá trình Poisson liên hệ nhị thức thế nào?||How is the Poisson process related to the binomial?⟧",
                     "⟦Khi nào quá trình Gauss dừng rộng là dừng chặt?||When is a wide-sense stationary Gaussian process strictly stationary?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: $\\Delta^2\\min(n_1,n_2)$ do gia số độc lập; giới hạn $n\\to\\infty$, $p=\\lambda\\Delta t$; luôn luôn.||Hints: $\\Delta^2\\min(n_1,n_2)$ from independent increments; the limit $n\\to\\infty$, $p=\\lambda\\Delta t$; always.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 3
        dict(
            title="⟦Nhiễu từ chữ số ngẫu nhiên: biên độ, tương quan, phổ||Noise from random digits: amplitude, correlation, spectrum⟧",
            scr=("⟦Bracewell xây một dạng sóng nhiễu từ các chữ số của $\\pi$ và xem nó thay đổi thế nào khi qua bộ lọc.||Bracewell builds a noise waveform from the digits of $\\pi$ and watches how it changes through a filter.⟧",
                 "⟦Biên độ thành Gauss (giới hạn trung tâm), tự tương quan bằng tự tương quan của đáp ứng xung, phổ nhân với $|T|^2$.||The amplitude becomes Gaussian (central limit), the autocorrelation equals that of the impulse response, the spectrum is multiplied by $|T|^2$.⟧",
                 "⟦Nhiễu thông dải có đường bao Rayleigh; tách sóng bình phương cho phân bố mũ; độ chính xác đo công suất là $1/\\sqrt{T\\Delta f}$.||Bandpass noise has a Rayleigh envelope; square-law detection gives an exponential distribution; the precision of a power measurement is $1/\\sqrt{T\\Delta f}$.⟧"),
            preview=["⟦Chữ số ngẫu nhiên, độc lập, tương quan||Random digits, independence, correlation⟧", "⟦Tự tương quan và phổ sau bộ lọc||Autocorrelation and spectrum after a filter⟧", "⟦Nhiễu thông dải, đường bao, đo công suất||Bandpass noise, the envelope, power measurement⟧"],
            slides=[
                ("⟦Biểu diễn bằng chữ số ngẫu nhiên||Discrete representation by random digits⟧",
                 "<p>⟦Ta dùng các chữ số liên tiếp của $\\pi$ (từ 0 đến 9, mỗi chữ số có khả năng như nhau), coi $t$ là thời gian với một chữ số mỗi đơn vị; dãy $\\{y_t\\}$ có thể xem là mẫu của một dạng sóng giới hạn băng và ta vẽ đường trơn qua các điểm theo định lý lấy mẫu (Bracewell, tr. 447 đến 448). Trung bình của 32 chữ số đầu là {{pi_mean}}; ta hy vọng nó tiến về 4.5 khi $N\\to\\infty$, và phương sai tiến về giá trị của phân bố đều rời rạc {{dig_var}} (tr. 449 đến 450).||We use the successive digits of $\\pi$ (0 to 9, each equally likely), regarding $t$ as time with one digit per unit; the sequence $\\{y_t\\}$ can be taken as samples of a band-limited waveform and we draw a smooth curve through the points by the sampling theorem (Bracewell, pp. 447 to 448). The mean of the first 32 digits is {{pi_mean}}; we expect it to approach 4.5 as $N\\to\\infty$, and the variance to approach the value for the discrete uniform distribution, {{dig_var}} (pp. 449 to 450).⟧</p>"),
                ("⟦Trung bình và phương sai như mômen của $p(y)$||Mean and variance as moments of $p(y)$⟧",
                 "<p>⟦Gọi $a(y)$ là số lần giá trị $y$ xuất hiện; $a(y)/N\\to p(y)=0.1$. Do đó trung bình giới hạn $\\mu=\\sum yp(y)=4.5$ và phương sai giới hạn $\\sum(y-\\mu)^2p(y)=8.25$ (Bracewell, tr. 449 đến 450). Số đo: $\\sum yp$ = {{dig_m}}, phương sai {{dig_var}}, và cả hai bằng kết quả của $10^6$ chữ số ngẫu nhiên.||Let $a(y)$ be the number of times the value $y$ occurs; $a(y)/N\\to p(y)=0.1$. Hence the limiting mean is $\\mu=\\sum yp(y)=4.5$ and the limiting variance $\\sum(y-\\mu)^2p(y)=8.25$ (Bracewell, pp. 449 to 450). Measured: $\\sum yp$ = {{dig_m}}, variance {{dig_var}}, and both equal the results of $10^6$ random digits.⟧</p>"),
                ("⟦Lọc một dãy ngẫu nhiên: biên độ trở thành Gauss||Filtering a random sequence: the amplitude becomes Gaussian⟧",
                 "<p>⟦Cho $\\eta_t=y_t+y_{t+1}+\\cdots+y_{t+9}$, tức qua bộ lọc có đáp ứng xung $\\{1\\,1\\,\\ldots\\,1\\}$ (10 số 1). Nếu các chữ số độc lập, phân bố của $\\eta$ là tích chập 10 lần của $p(y)$ (Bracewell, tr. 451 đến 454). Theo giới hạn trung tâm nó gần chuẩn với trung bình {{sum_m}} và phương sai {{sum_v}} (mười lần các giá trị trước). Số đo: $P(40\\le\\eta\\le50)$ = {{sum_p}} tính chính xác qua tích chập; xấp xỉ chuẩn cho {{sum_pn}}. Đây là hiện tượng rộng rãi: biên độ của tín hiệu ngẫu nhiên đi ra từ bộ lọc gần chuẩn.||Let $\\eta_t=y_t+y_{t+1}+\\cdots+y_{t+9}$, i.e. through a filter with impulse response $\\{1\\,1\\,\\ldots\\,1\\}$ (ten ones). If the digits are independent, the distribution of $\\eta$ is the tenfold convolution of $p(y)$ (Bracewell, pp. 451 to 454). By the central limit theorem it is nearly normal with mean {{sum_m}} and variance {{sum_v}} (ten times the previous values). Measured: $P(40\\le\\eta\\le50)$ = {{sum_p}} computed exactly through convolution; the normal approximation gives {{sum_pn}}. This is a widespread phenomenon: the amplitude of a random signal emerging from a filter is nearly normal.⟧</p>"),
                ("⟦Về tính độc lập: các phép thử của Bracewell||On independence: Bracewell's tests⟧",
                 "<p>⟦Ta cần biết các chữ số có độc lập không. Các chữ số có thể xuất hiện đều nhưng vẫn phụ thuộc: $3.0123456789\\,0123\\ldots$ tuần hoàn. Một phép thử: $y_{t+1}$ qua 4.5 hay ở cùng phía với $y_t$ với xác suất bằng nhau; thấy 15 lần qua và 16 lần không. Phép thử mạnh hơn: độ dài các chuỗi trên hoặc dưới 4.5 có xác suất $p_k=2^{-k}$ (Bracewell, tr. 451 đến 452). Số đo với $10^6$ chữ số ngẫu nhiên: chuỗi độ dài 1 chiếm {{run_1}}, độ dài 2 chiếm {{run_2}}, độ dài 3 chiếm {{run_3}}.||We need to know whether the digits are independent. Digits may occur equally often yet be dependent: $3.0123456789\\,0123\\ldots$ is periodic. One test: $y_{t+1}$ crosses 4.5 or stays on the same side as $y_t$ with equal probability; 15 crossings and 16 non-crossings were seen. A stronger test: the lengths of runs above or below 4.5 have probability $p_k=2^{-k}$ (Bracewell, pp. 451 to 452). Measured with $10^6$ random digits: runs of length 1 make up {{run_1}}, length 2 {{run_2}}, length 3 {{run_3}}.⟧</p>"),
                ("⟦Hệ số tương quan và cách đếm bốn góc||Correlation coefficients and the quadrant count⟧",
                 "<p>⟦Vẽ $y_{t+1}$ theo $y_t$ (hình 17.5). Hệ số tích-mômen là hiệp phương sai chia giá trị lớn nhất; cách nhanh hơn là chia biểu đồ thành bốn góc tại điểm trung vị, lấy (số điểm ở góc 1 và 3 trừ số ở 2 và 4) chia tổng số điểm, được $\\psi=0.03$ cho các chữ số (tr. 452 đến 453). Cả hai hệ số có thể nhỏ mà vẫn phụ thuộc (hình 17.6), nên hệ số tương quan chưa đủ chứng minh độc lập. Với dữ liệu Gauss có $\\psi=\\tfrac2\\pi\\arcsin\\rho$, tức $\\rho=\\sin(\\tfrac\\pi2\\psi)$ (bài tập 8, tr. 470). Số đo: $\\rho=0.9$ cho $\\psi$ = {{psi_09}} trong mô phỏng, và công thức cho {{psi_th}}.||Plot $y_{t+1}$ against $y_t$ (Fig. 17.5). The product-moment coefficient is the covariance divided by its maximum; a faster way is to divide the diagram into four quadrants at the median point and take (points in quadrants 1 and 3 minus those in 2 and 4) over the total, giving $\\psi=0.03$ for the digits (pp. 452 to 453). Both coefficients can be small yet the data dependent (Fig. 17.6), so correlation coefficients alone do not prove independence. For Gaussian data $\\psi=\\tfrac2\\pi\\arcsin\\rho$, i.e. $\\rho=\\sin(\\tfrac\\pi2\\psi)$ (problem 8, p. 470). Measured: $\\rho=0.9$ gives $\\psi$ = {{psi_09}} in simulation, and the formula gives {{psi_th}}.⟧</p>"),
                ("⟦Tự tương quan của đầu ra bằng tự tương quan của đáp ứng xung||The output autocorrelation equals that of the impulse response⟧",
                 "<p>⟦Từ dãy không tương quan $\\{y_t\\}$ trừ trung bình, tạo $\\{\\eta_t\\}=\\{I_t\\}*\\{y_t\\}$ với $\\sum I_t=1$. Bracewell chứng minh rằng tự tương quan chuẩn hóa giới hạn của đầu ra là $C(\\tau)=\\dfrac{\\{I\\}\\star\\{I\\}}{\\text{chuẩn hóa}}$: tự tương quan của dãy ban đầu không tương quan, sau khi qua bộ lọc, là tự tương quan của đáp ứng xung (tr. 455 đến 458). Với tổng chạy 10 số: $C(1)$ = {{ac_1}} và $C(2)$ = {{ac_2}} (bằng $1-|\\tau|/10$; cách đếm bốn góc trên 20 điểm cho 0.8 và 0.6). Với $\\{g\\}=\\{5\\,3\\,1\\,1\\}$: $C(1),C(2),C(3)$ = {{g_1}}, {{g_2}}, {{g_3}}.||From the uncorrelated sequence $\\{y_t\\}$ with the mean subtracted, form $\\{\\eta_t\\}=\\{I_t\\}*\\{y_t\\}$ with $\\sum I_t=1$. Bracewell shows that the limiting normalised autocorrelation of the output is $C(\\tau)=\\dfrac{\\{I\\}\\star\\{I\\}}{\\text{normalising factor}}$: the autocorrelation of an initially uncorrelated sequence, after passing through a filter, is the autocorrelation of the impulse response (pp. 455 to 458). For the ten-term running sum: $C(1)$ = {{ac_1}} and $C(2)$ = {{ac_2}} (equal to $1-|\\tau|/10$; the quadrant count on 20 points gave 0.8 and 0.6). With $\\{g\\}=\\{5\\,3\\,1\\,1\\}$: $C(1),C(2),C(3)$ = {{g_1}}, {{g_2}}, {{g_3}}.⟧</p>"
                 + F("⟦Tự tương quan sau lọc||Autocorrelation after filtering⟧", r"C(\tau)=\frac{\{I_t\}\star\{I_t\}}{\text{normalising factor}}")),
                ("⟦Phổ: đầu vào trắng, đầu ra nhân với $|T|^2$||Spectrum: white input, output multiplied by $|T|^2$⟧",
                 "<p>⟦Dạng sóng $V(t)=\\sum y_j\\,\\text{sinc}(t-j)$ có phổ $S(f)=\\sum y_je^{-i2\\pi jf}\\Pi(f)$, và phổ công suất $SS^*$ tiến về phẳng rồi cắt ở $|f|=\\tfrac12$ khi số số hạng tăng; tự tương quan tương ứng là $C(\\tau)=\\text{sinc}\\,\\tau$ (Bracewell, tr. 458 đến 460). Qua bộ lọc có hàm truyền $T$, $W=V*I\\supset ST$, nên phổ công suất đầu ra là $SS^*TT^*\\propto TT^*\\Pi(f)$, tức biến đổi của $[I*I]*\\text{sinc}\\,t$; $TT^*$ là hàm truyền công suất (tr. 461). Hai bộ lọc nối tiếp: hàm truyền công suất tổng là tích. Số đo: tổng chạy 10 số tại $f=0.05$: $|T|^2=[\\sin(10\\pi f)/\\sin(\\pi f)]^2$ = {{pt_th}} và ước lượng Welch từ mô phỏng {{pt_mc}}.||The waveform $V(t)=\\sum y_j\\,\\text{sinc}(t-j)$ has spectrum $S(f)=\\sum y_je^{-i2\\pi jf}\\Pi(f)$, and the power spectrum $SS^*$ tends to flat and cuts off at $|f|=\\tfrac12$ as the number of terms grows; the corresponding autocorrelation is $C(\\tau)=\\text{sinc}\\,\\tau$ (Bracewell, pp. 458 to 460). Through a filter with transfer function $T$, $W=V*I\\supset ST$, so the output power spectrum is $SS^*TT^*\\propto TT^*\\Pi(f)$, the transform of $[I*I]*\\text{sinc}\\,t$; $TT^*$ is the power-transfer function (p. 461). Two filters in cascade: the overall power-transfer function is the product. Measured: the ten-term running sum at $f=0.05$: $|T|^2=[\\sin(10\\pi f)/\\sin(\\pi f)]^2$ = {{pt_th}} and a Welch estimate from simulation {{pt_mc}}.⟧</p>"),
                ("⟦Nhiễu thông thấp Gauss: dãy nhị thức||Gaussian low-pass noise: the binomial sequence⟧",
                 "<p>⟦Bracewell làm bản ghi nhiễu dài bằng cách chập các chữ số của Kendall và Smith (1940) với $\\{1\\,5\\,10\\,10\\,5\\,1\\}$; tự tương quan tỉ lệ $\\{1\\,5\\,10\\,10\\,5\\,1\\}\\star\\{\\ldots\\}=\\{1\\,10\\,45\\,120\\,210\\,252\\,210\\,120\\,45\\,10\\,1\\}=\\{1\\,1\\}^{*10}$, xấp xỉ Gauss $252\\exp[-\\pi(0.24n)^2]$ (tr. 462 đến 463). Số đo: nhị thức và Gauss tại $n=1,\\ldots,5$ là 210 với 210, 120 với {{gs_2}}, 45 với {{gs_3}}, 10 với {{gs_4}}, 1 với {{gs_5}} (làm tròn); và đỉnh của phổ $\\tfrac1{0.24}e^{-\\pi(f/0.24)^2}$ là {{gs_pk}} tại $f=0$.||Bracewell made a long noise record by convolving the random digits of Kendall and Smith (1940) with $\\{1\\,5\\,10\\,10\\,5\\,1\\}$; the autocorrelation is proportional to $\\{1\\,5\\,10\\,10\\,5\\,1\\}\\star\\{\\ldots\\}=\\{1\\,10\\,45\\,120\\,210\\,252\\,210\\,120\\,45\\,10\\,1\\}=\\{1\\,1\\}^{*10}$, approximately the Gaussian $252\\exp[-\\pi(0.24n)^2]$ (pp. 462 to 463). Measured: binomial against Gaussian at $n=1,\\ldots,5$ is 210 with 210, 120 with {{gs_2}}, 45 with {{gs_3}}, 10 with {{gs_4}}, 1 with {{gs_5}} (rounded); and the peak of the spectrum $\\tfrac1{0.24}e^{-\\pi(f/0.24)^2}$ is {{gs_pk}} at $f=0$.⟧</p>"),
                ("⟦Nhiễu thông dải: bộ cộng hưởng tắt dần||Bandpass noise: a damped resonator⟧",
                 "<p>⟦Bracewell tạo nhiễu thông dải từ $y_t=ay_{t-1}+by_{t-2}+\\epsilon_t$ với $a=1.84$, $b=-0.9$ và $\\epsilon_t$ đều ngẫu nhiên trong $(-0.5,0.5)$: bộ cộng hưởng tắt dần bị kích thích ngẫu nhiên, phổ đỉnh quanh giữa băng (tr. 463 đến 465). Cực tại $re^{\\pm i\\omega}$ với $r=\\sqrt{-b}$ = {{ar_r}} và $\\cos\\omega=a/2r$, nên tần số đỉnh {{ar_f}} chu kỳ trên mẫu; phổ Welch từ mô phỏng đỉnh ở {{ar_fmc}}. Phổ không Gauss nhưng biên độ thì Gauss xấp xỉ; nếu nhiều bộ cộng hưởng như thế nối tiếp, phổ tiến về Gauss quanh trung tần.||Bracewell generates bandpass noise from $y_t=ay_{t-1}+by_{t-2}+\\epsilon_t$ with $a=1.84$, $b=-0.9$ and $\\epsilon_t$ uniform random in $(-0.5,0.5)$: a damped resonator excited by random noise, with a spectrum peaked around mid-band (pp. 463 to 465). The poles lie at $re^{\\pm i\\omega}$ with $r=\\sqrt{-b}$ = {{ar_r}} and $\\cos\\omega=a/2r$, so the peak frequency is {{ar_f}} cycles per sample; the Welch spectrum from simulation peaks at {{ar_fmc}}. The spectrum is not Gaussian but the amplitude is approximately so; if several such resonators were cascaded the spectrum would approach a Gaussian about the mid-frequency.⟧</p>{{fig:bandpass}}"),
                ("⟦Đường bao của nhiễu thông dải là Rayleigh||The envelope of bandpass noise is Rayleigh⟧",
                 "<p>⟦Đường bao $r=\\sqrt{y^2+z^2}$ với $z$ là biến đổi Hilbert của $y$. Nếu $y$ Gauss và $z$ có cùng phân bố và độc lập với $y$ ($p(y)p(z)dydz=\\alpha e^{-\\pi\\alpha(y^2+z^2)}$ theo tọa độ cực), thì $p(r)=2\\pi\\alpha re^{-\\pi\\alpha r^2}$: Rayleigh, viết theo bình phương trung bình $\\langle r^2\\rangle$ là $p(r)=\\dfrac{2r}{\\langle r^2\\rangle}e^{-r^2/\\langle r^2\\rangle}$ (Bracewell, tr. 465 đến 466). Ý chính: biến đổi Hilbert dịch mỗi thành phần Fourier một lượng khác nhau nên cho chồng chất mới độc lập cùng thống kê. Số đo (Hilbert bằng FFT): trung bình $r/\\sigma$ = {{env_m}} $=\\sqrt{\\pi/2}$, và độ lệch cực đại của phân bố tích lũy khỏi Rayleigh {{env_ks}}.||The envelope is $r=\\sqrt{y^2+z^2}$ with $z$ the Hilbert transform of $y$. If $y$ is Gaussian and $z$ has the same distribution and is independent of $y$ ($p(y)p(z)dydz=\\alpha e^{-\\pi\\alpha(y^2+z^2)}$ in polar form), then $p(r)=2\\pi\\alpha re^{-\\pi\\alpha r^2}$: Rayleigh, written in terms of the mean square $\\langle r^2\\rangle$ as $p(r)=\\dfrac{2r}{\\langle r^2\\rangle}e^{-r^2/\\langle r^2\\rangle}$ (Bracewell, pp. 465 to 466). The key point: Hilbert transformation shifts every Fourier component by a different amount so it gives another, independent superposition with the same statistics. Measured (Hilbert by FFT): the mean of $r/\\sigma$ = {{env_m}} $=\\sqrt{\\pi/2}$, and the maximum deviation of the cumulative distribution from Rayleigh is {{env_ks}}.⟧</p>"),
                ("⟦Tách sóng nhiễu||Detection of a noise waveform⟧",
                 "<p>⟦Bộ tách sóng tuyến tính cho $|y(t)|$ có cùng phân bố biên độ Gauss (phần dương) và cùng đường bao Rayleigh. Bộ tách sóng bình phương cho $y^2$, đường bao là $V=r^2$; từ $dV=2r\\,dr$, $p(V)=\\dfrac1{\\langle V\\rangle}e^{-V/\\langle V\\rangle}$: phân bố mũ cắt cụt (Bracewell, tr. 466). Số đo: với $\\sigma=1$, $E[r^2]$ = {{sq_m}} và phương sai của $V$ = {{sq_v}} bằng bình phương trung bình (đặc trưng của phân bố mũ: độ lệch chuẩn bằng trung bình), theo mô phỏng và theo tích phân.||A linear detector gives $|y(t)|$, with the same Gaussian amplitude distribution (positive part) and the same Rayleigh envelope. A square-law detector gives $y^2$, whose envelope is $V=r^2$; from $dV=2r\\,dr$, $p(V)=\\dfrac1{\\langle V\\rangle}e^{-V/\\langle V\\rangle}$: a truncated exponential distribution (Bracewell, p. 466). Measured: with $\\sigma=1$, $E[r^2]$ = {{sq_m}} and the variance of $V$ = {{sq_v}} equals the squared mean (the exponential signature: standard deviation equals mean), by simulation and by integration.⟧</p>"),
                ("⟦Đo công suất nhiễu: giới hạn độ chính xác||Measuring noise power: the limit to precision⟧",
                 "<p>⟦Nhiễu có phổ công suất $R(f)$ qua tách sóng bình phương rồi bộ làm trơn tuyến tính có hàm truyền công suất $S(f)$. Tỉ số độ lệch bình phương trung bình của dao động trên giá trị trung bình là $\\dfrac{\\text{rms}}{\\text{mean}}=\\dfrac1{\\sqrt{\\tau\\Delta f}}$, với $\\tau$ là độ rộng tương đương của bộ làm trơn và $\\Delta f$ độ rộng tự tương quan của $R$ (module 8): $\\Delta f=\\tfrac12W_{R\\star R}$ và $\\tau=W_S$ (Bracewell, tr. 466 đến 468). Với băng chữ nhật $\\Delta f$ và trung bình trượt $T$: $\\tau=T$. Số đo: $T=1$ s, $\\Delta f=50$ Hz: lý thuyết {{tf_th}}; mô phỏng nhiễu băng hẹp và tách sóng bình phương cho {{tf_mc}}. Muốn giảm dao động mười lần cần tăng tích $T\\Delta f$ một trăm lần.||Noise with power spectrum $R(f)$ passes a square-law detector and then a linear smoothing filter of power-transfer function $S(f)$. The ratio of the rms fluctuation to the mean is $\\dfrac{\\text{rms}}{\\text{mean}}=\\dfrac1{\\sqrt{\\tau\\Delta f}}$, with $\\tau$ the equivalent width of the smoother and $\\Delta f$ the autocorrelation width of $R$ (module 8): $\\Delta f=\\tfrac12W_{R\\star R}$ and $\\tau=W_S$ (Bracewell, pp. 466 to 468). For a rectangular band $\\Delta f$ and a running mean $T$: $\\tau=T$. Measured: $T=1$ s, $\\Delta f=50$ Hz: theory {{tf_th}}; a simulation of narrowband noise with square-law detection gives {{tf_mc}}. To reduce the fluctuation tenfold the product $T\\Delta f$ must rise a hundredfold.⟧</p>{{fig:tdf}}"),
                ("⟦Quy tắc ngón tay cái và bài tập 4||A rule of thumb and problem 4⟧",
                 "<p>⟦Bài 1 (tr. 469): quy tắc thường được trích rằng giá trị hiệu dụng của nhiễu bằng một phần năm giá trị đỉnh-đỉnh. Số đo với nhiễu Gauss: $\\sigma/(\\max-\\min)$ trung bình là {{pp_100}} với 100 mẫu và {{pp_1000}} với 1000 mẫu; quy tắc đúng cho khoảng 100 mẫu và phụ thuộc số mẫu nhìn thấy. Bài 4 (tr. 469 đến 470): số lần cắt lên không mỗi giây $\\nu=\\dfrac1{2\\pi}\\arccos\\gamma_1$ với $\\gamma_1$ là hệ số tương quan lân cận của dãy Gauss; với tổng chạy 10 số $\\gamma_1=0.9$ nên $\\nu$ = {{up_th}} mỗi mẫu, mô phỏng {{up_mc}}.||Problem 1 (p. 469): the widely quoted rule that the rms noise equals one fifth of the peak-to-peak value. Measured with Gaussian noise: the mean of $\\sigma/(\\max-\\min)$ is {{pp_100}} for 100 samples and {{pp_1000}} for 1000 samples; the rule holds for about 100 samples and depends on the number of samples seen. Problem 4 (pp. 469 to 470): the number of upcrosses per second is $\\nu=\\dfrac1{2\\pi}\\arccos\\gamma_1$ with $\\gamma_1$ the neighbour correlation coefficient of the Gaussian sequence; for the ten-term running sum $\\gamma_1=0.9$ so $\\nu$ = {{up_th}} per sample, simulation {{up_mc}}.⟧</p>"),
                ("⟦Tự kiểm tra phần 3||Self-check, part 3⟧",
                 UL(["⟦Vì sao nhiễu qua bộ lọc có biên độ gần Gauss?||Why does noise through a filter have a nearly Gaussian amplitude?⟧",
                     "⟦Tự tương quan của đầu ra bộ lọc từ nhiễu trắng là gì?||What is the autocorrelation of the output of a filter driven by white noise?⟧",
                     "⟦Đường bao của nhiễu Gauss thông dải và bình phương của nó có phân bố nào?||What distributions do the envelope of bandpass Gaussian noise and its square have?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: đầu ra là tổng có trọng số nên giới hạn trung tâm; tự tương quan của đáp ứng xung; Rayleigh và mũ.||Hints: the output is a weighted sum so the central limit applies; the autocorrelation of the impulse response; Rayleigh and exponential.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 4
        dict(
            title="⟦Mật độ phổ công suất và hệ tuyến tính bất biến||Power spectral density and linear time-invariant systems⟧",
            scr=("⟦Tự tương quan cho biết mức liên hệ theo thời gian; tần số nào chứa bao nhiêu công suất?||The autocorrelation tells the relation through time; which frequencies hold how much power?⟧",
                 "⟦Mật độ phổ công suất là biến đổi Fourier của tự tương quan; và hệ tuyến tính nhân nó với $|H|^2$.||The power spectral density is the Fourier transform of the autocorrelation; a linear system multiplies it by $|H|^2$.⟧",
                 "⟦Từ đó tính đầu ra của mạch RC dưới nhiễu trắng và suy ra ergodic và lấy mẫu.||From it we compute the output of an RC circuit under white noise and derive ergodicity and sampling.⟧"),
            preview=["⟦Mật độ phổ công suất, Wiener-Khinchin||Power spectral density, Wiener-Khinchin⟧", "⟦Đầu ra hệ tuyến tính: mạch RC||Linear system output: the RC circuit⟧", "⟦Ergodic và lấy mẫu||Ergodicity and sampling⟧"],
            slides=[
                ("⟦Mật độ phổ công suất||Power spectral density⟧",
                 "<p>⟦Với tín hiệu tất định có biến đổi Fourier $S(f)$. Hàm mẫu của quá trình thường không khả tích tuyệt đối, nên ta cắt $x_T(t)$ giữa $-T$ và $T$, lấy $X_T(f)$, công suất trung bình $P_T=\\int|X_T(f)|^2/2T\\,df$ theo Parseval, rồi lấy kỳ vọng và cho $T\\to\\infty$: $S_{xx}(f)=\\lim_{T\\to\\infty}E[|X_T(f)|^2]/2T$ (Barkat, mục 3.5, tr. 174 đến 176). Định lý Wiener-Khinchin: $S_{xx}(f)$ là biến đổi Fourier của $R_{xx}(\\tau)$. Với pha ngẫu nhiên: $R=\\tfrac{A^2}2\\cos2\\pi f_0\\tau$ nên $S=\\tfrac{A^2}4[\\delta(f-f_0)+\\delta(f+f_0)]$, tổng công suất {{psd_tot}} $=A^2/2$ với $A=2$.||For a deterministic signal there is a Fourier transform $S(f)$. Sample functions of a process are usually not absolutely integrable, so we truncate $x_T(t)$ between $-T$ and $T$, take $X_T(f)$, the average power $P_T=\\int|X_T(f)|^2/2T\\,df$ by Parseval, then take the expectation and let $T\\to\\infty$: $S_{xx}(f)=\\lim_{T\\to\\infty}E[|X_T(f)|^2]/2T$ (Barkat, section 3.5, pp. 174 to 176). The Wiener-Khinchin theorem: $S_{xx}(f)$ is the Fourier transform of $R_{xx}(\\tau)$. For the random phase: $R=\\tfrac{A^2}2\\cos2\\pi f_0\\tau$ so $S=\\tfrac{A^2}4[\\delta(f-f_0)+\\delta(f+f_0)]$, total power {{psd_tot}} $=A^2/2$ with $A=2$.⟧</p>"
                 + F("⟦Wiener-Khinchin||Wiener-Khinchin⟧", r"S_{xx}(f)=\int_{-\infty}^{\infty}R_{xx}(\tau)\,e^{-j2\pi f\tau}\,d\tau,\qquad R_{xx}(0)=\int S_{xx}(f)\,df")),
                ("⟦Nhiễu trắng và cặp $R$–$S$ thường gặp||White noise and common $R$–$S$ pairs⟧",
                 TBL(["$R_{xx}(\\tau)$", "$S_{xx}(f)$"],
                     [["$\\tfrac{N_0}2\\delta(\\tau)$", "$\\tfrac{N_0}2$ (⟦nhiễu trắng||white noise⟧)"], ["$\\tfrac{A^2}2\\cos2\\pi f_0\\tau$", "$\\tfrac{A^2}4[\\delta(f-f_0)+\\delta(f+f_0)]$"], ["$\\sigma^2e^{-\\alpha|\\tau|}$", "$\\dfrac{2\\alpha\\sigma^2}{\\alpha^2+4\\pi^2f^2}$"], ["$\\sigma^2\\text{sinc}\\,\\tau$", "$\\sigma^2\\Pi(f)$"]])
                 + "<p>⟦Đây là các cặp biến đổi của Bracewell (module 5 đến 7), giờ đọc như cặp tự tương quan và phổ công suất. Bracewell (tr. 459 đến 460) cũng chỉ ra rằng biến đổi của tự tương quan của các chữ số nội suy sinc là $\\Pi(f)$: nhiễu \"trắng trong băng\".||These are Bracewell's transform pairs (modules 5 to 7), now read as autocorrelation and power spectrum pairs. Bracewell (pp. 459 to 460) also shows that the transform of the autocorrelation of sinc-interpolated digits is $\\Pi(f)$: noise \"white within the band\".⟧</p>"),
                ("⟦Hệ tuyến tính bất biến với đầu vào ngẫu nhiên||A linear time-invariant system with random input⟧",
                 "<p>⟦Đầu ra $Y(t)=h(t)*X(t)$. Với $X$ dừng rộng: trung bình $m_y=m_xH(0)$; tương quan chéo $R_{yx}(\\tau)=R_{xx}(\\tau)*h(\\tau)$; tự tương quan $R_{yy}(\\tau)=R_{xx}(\\tau)*h(\\tau)*h(-\\tau)$; phổ $S_{yy}(f)=S_{xx}(f)|H(f)|^2$, $S_{yx}=S_{xx}H$, $S_{xy}=S_{xx}H^*$ (Barkat, mục 3.6.1, tr. 179 đến 185). Nhiều đầu: $S_{zz}=S_{yy}|H_2|^2/|H_1|^2$ và hệ \"rời\" khi các hàm truyền không chồng lên nhau (mục 3.6.2, tr. 185 đến 186). Đây là bản ngẫu nhiên của định lý tích chập: trong $V_2=I*V_1$ của module 9, giờ áp dụng cho năng lượng.||The output is $Y(t)=h(t)*X(t)$. For $X$ wide-sense stationary: the mean $m_y=m_xH(0)$; the cross-correlation $R_{yx}(\\tau)=R_{xx}(\\tau)*h(\\tau)$; the autocorrelation $R_{yy}(\\tau)=R_{xx}(\\tau)*h(\\tau)*h(-\\tau)$; the spectrum $S_{yy}(f)=S_{xx}(f)|H(f)|^2$, $S_{yx}=S_{xx}H$, $S_{xy}=S_{xx}H^*$ (Barkat, section 3.6.1, pp. 179 to 185). With several terminals: $S_{zz}=S_{yy}|H_2|^2/|H_1|^2$ and the system is \"disjoint\" when the transfer functions do not overlap (section 3.6.2, pp. 185 to 186). This is the stochastic version of the convolution theorem: the $V_2=I*V_1$ of module 9, now applied to power.⟧</p>"
                 + F("⟦Đầu ra||Output⟧", r"S_{yy}(f)=|H(f)|^2S_{xx}(f),\qquad m_y=H(0)\,m_x")),
                ("⟦Ví dụ: nhiễu trắng qua mạch RC||Example: white noise through an RC circuit⟧",
                 "<p>⟦Nhiễu trắng $R_{xx}=\\tfrac{N_0}2\\delta(\\tau)$ qua $h(t)=\\alpha e^{-\\alpha t}$, $t\\ge0$. Cách 1 (chập): $h*h(-\\tau)=\\tfrac\\alpha2e^{-\\alpha|\\tau|}$, nên $R_{yy}(\\tau)=\\dfrac{N_0\\alpha}4e^{-\\alpha|\\tau|}$. Cách 2 (phổ): $|H|^2=\\alpha^2/(4\\pi^2f^2+\\alpha^2)$, $S_{yy}=\\tfrac{N_0}2|H|^2$, biến đổi ngược cho cùng kết quả (Barkat, tr. 181 đến 183). Số đo với $N_0=2$, $\\alpha=5$: $R_{yy}(0)$ = {{rc_r0}} và $R_{yy}(0.1)$ = {{rc_r1}}, theo công thức, theo tích phân số và theo mô phỏng SDE; và nếu đầu vào có trung bình 3 thì trung bình đầu ra {{rc_m}}.||White noise $R_{xx}=\\tfrac{N_0}2\\delta(\\tau)$ through $h(t)=\\alpha e^{-\\alpha t}$, $t\\ge0$. Method 1 (convolution): $h*h(-\\tau)=\\tfrac\\alpha2e^{-\\alpha|\\tau|}$, so $R_{yy}(\\tau)=\\dfrac{N_0\\alpha}4e^{-\\alpha|\\tau|}$. Method 2 (spectrum): $|H|^2=\\alpha^2/(4\\pi^2f^2+\\alpha^2)$, $S_{yy}=\\tfrac{N_0}2|H|^2$, and the inverse transform gives the same result (Barkat, pp. 181 to 183). Measured with $N_0=2$, $\\alpha=5$: $R_{yy}(0)$ = {{rc_r0}} and $R_{yy}(0.1)$ = {{rc_r1}}, by formula, by numerical integration and by an SDE simulation; and if the input has mean 3 the output mean is {{rc_m}}.⟧</p>{{fig:rc_acf}}"),
                ("⟦Ergodic||Ergodicity⟧",
                 "<p>⟦$X(t)$ là ergodic nếu mọi thống kê xác định được (với xác suất 1) từ một hàm mẫu: trung bình tập hợp bằng trung bình thời gian; điều kiện này hạn chế hơn dừng (hình 3.28). Thường chỉ cần dạng yếu: ergodic theo trung bình ($E[X(t)]=\\langle x(t)\\rangle$), theo tự tương quan, theo phân bố bậc một và theo mật độ phổ công suất (Barkat, mục 3.7, tr. 186 đến 189). Số đo: pha ngẫu nhiên $A\\cos(2\\pi t+\\Theta)$ là ergodic theo trung bình: trung bình thời gian trên 100 chu kỳ là {{er_t}}. Phản ví dụ: $X=C$ với $C$ ngẫu nhiên là dừng nhưng không ergodic: trung bình thời gian của mỗi hàm mẫu là $C$, phương sai giữa các hàm mẫu {{er_v}}, còn với pha ngẫu nhiên gần 0.||$X(t)$ is ergodic if all its statistics can be determined (with probability one) from a sample function: ensemble averages equal time averages; this condition is more restrictive than stationarity (Fig. 3.28). Usually only weaker forms are needed: ergodic in the mean ($E[X(t)]=\\langle x(t)\\rangle$), in the autocorrelation, in the first-order distribution and in the power spectral density (Barkat, section 3.7, pp. 186 to 189). Measured: the random phase $A\\cos(2\\pi t+\\Theta)$ is ergodic in the mean: the time average over 100 periods is {{er_t}}. Counterexample: $X=C$ with random $C$ is stationary but not ergodic: the time average of each sample function is $C$, the variance across sample functions is {{er_v}}, while for the random phase it is near 0.⟧</p>"),
                ("⟦Định lý lấy mẫu cho quá trình ngẫu nhiên||The sampling theorem for random processes⟧",
                 "<p>⟦Tín hiệu tất định giới hạn băng $f_m$ tái tạo hoàn toàn từ mẫu ở $2f_m$ mỗi giây: $g(t)=\\sum g(n/2f_m)\\,\\text{sinc}(2f_mt-n)$; lấy mẫu dưới tần số Nyquist gây chồng phổ $G_s=f_s\\sum G(f-nf_s)$ (Barkat, mục 3.8, tr. 189 đến 191). Nếu $X(t)$ dừng rộng với $S_{xx}(f)=0$ khi $|f|>f_m$, cũng tái tạo được theo nghĩa bình phương trung bình. Số đo: nhiễu Gauss giới hạn băng $f_m=5$ Hz lấy mẫu ở 10 Hz và nội suy sinc, sai số bình phương trung bình tương đối trong vùng giữa bản ghi {{sm_ok}}; lấy mẫu ở 6 Hz (dưới Nyquist) sai số {{sm_bad}}.||A deterministic signal band-limited to $f_m$ is fully recovered from samples at $2f_m$ per second: $g(t)=\\sum g(n/2f_m)\\,\\text{sinc}(2f_mt-n)$; sampling below the Nyquist rate causes aliasing $G_s=f_s\\sum G(f-nf_s)$ (Barkat, section 3.8, pp. 189 to 191). If $X(t)$ is wide-sense stationary with $S_{xx}(f)=0$ for $|f|>f_m$, it too can be recovered in the mean-square sense. Measured: Gaussian noise band-limited to $f_m=5$ Hz sampled at 10 Hz and sinc-interpolated has a relative mean-square error in the middle of the record of {{sm_ok}}; sampled at 6 Hz (below Nyquist) the error is {{sm_bad}}.⟧</p>"),
                ("⟦Hilbert và tín hiệu giải tích||The Hilbert transform and analytic signals⟧",
                 "<p>⟦Bộ lọc vuông pha $H(f)=-j\\,\\text{sgn}f$ (đáp ứng xung $1/\\pi t$) cho biến đổi Hilbert $\\hat x=x*\\frac1{\\pi t}$; nó toàn thông, $S_{\\hat x\\hat x}=S_{xx}$, $R_{\\hat x\\hat x}=R_{xx}$, $R_{\\hat xx}(0)=0$, và $\\hat{\\hat X}=-X$ (Barkat, mục 3.10, tr. 201 đến 204). Tín hiệu giải tích $\\tilde x=x+j\\hat x$ qua $H=2$ cho $f>0$: $S_{\\tilde x\\tilde x}=4S_{xx}$ cho $f>0$ và 0 cho $f<0$, $R_{\\tilde x\\tilde x}=2[R_{xx}+j\\hat R_{xx}]$ (tr. 204 đến 205). Số đo: công suất trung bình của $\\tilde x$ bằng {{an_p}} lần của $x$ (=$1+1$); và $\\hat{\\hat x}+x$ lệch {{hh_dev}}. Đó là các cặp Hilbert của module 9 (bảng 9.1) cho quá trình ngẫu nhiên.||The quadrature filter $H(f)=-j\\,\\text{sgn}f$ (impulse response $1/\\pi t$) gives the Hilbert transform $\\hat x=x*\\frac1{\\pi t}$; it is all-pass, $S_{\\hat x\\hat x}=S_{xx}$, $R_{\\hat x\\hat x}=R_{xx}$, $R_{\\hat xx}(0)=0$, and $\\hat{\\hat X}=-X$ (Barkat, section 3.10, pp. 201 to 204). The analytic signal $\\tilde x=x+j\\hat x$ through $H=2$ for $f>0$ has $S_{\\tilde x\\tilde x}=4S_{xx}$ for $f>0$ and 0 for $f<0$, $R_{\\tilde x\\tilde x}=2[R_{xx}+j\\hat R_{xx}]$ (pp. 204 to 205). Measured: the mean power of $\\tilde x$ is {{an_p}} times that of $x$ (=$1+1$); and $\\hat{\\hat x}+x$ deviates by {{hh_dev}}. These are the Hilbert pairs of module 9 (Table 9.1) for random processes.⟧</p>"),
                ("⟦Tự kiểm tra phần 4||Self-check, part 4⟧",
                 UL(["⟦Wiener-Khinchin nói gì?||What does Wiener-Khinchin say?⟧",
                     "⟦$R_{yy}$ và $S_{yy}$ của đầu ra hệ tuyến tính được tính ra sao từ đầu vào?||How are $R_{yy}$ and $S_{yy}$ of a linear system's output computed from the input?⟧",
                     "⟦Vì sao $X=C$ ngẫu nhiên không ergodic?||Why is $X=C$ with random $C$ not ergodic?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: $S$ là biến đổi Fourier của $R$; $R_{yy}=R_{xx}*h*h(-\\tau)$, $S_{yy}=|H|^2S_{xx}$; trung bình thời gian bằng $C$ chứ không bằng $E[C]$.||Hints: $S$ is the Fourier transform of $R$; $R_{yy}=R_{xx}*h*h(-\\tau)$, $S_{yy}=|H|^2S_{xx}$; the time average equals $C$, not $E[C]$.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 5
        dict(
            title="⟦Liên tục, đạo hàm, tích phân và nhiễu nhiệt||Continuity, differentiation, integration and thermal noise⟧",
            scr=("⟦Muốn nói quá trình ngẫu nhiên \"liên tục\" hay \"khả vi\", ta cần khái niệm giới hạn mới, theo bình phương trung bình.||To say a random process is \"continuous\" or \"differentiable\" we need a new notion of limit, in the mean-square sense.⟧",
                 "⟦Nhiễu nhiệt trong điện trở là ứng dụng vật lý điển hình của mọi thứ trên: trắng, Gauss, công suất tỉ lệ nhiệt độ và băng thông.||Thermal noise in a resistor is the typical physical application of all the above: white, Gaussian, power proportional to temperature and bandwidth.⟧",
                 "⟦Điện áp nhiễu hiệu dụng $\\sqrt{4kTRB}$ đặt giới hạn cơ bản cho các phép đo.||The rms noise voltage $\\sqrt{4kTRB}$ sets a fundamental limit to measurements.⟧"),
            preview=["⟦Liên tục, đạo hàm, tích phân bình phương trung bình||Mean-square continuity, differentiation, integration⟧", "⟦Nhiễu nhiệt||Thermal noise⟧", "⟦Tổng kết: từ Fourier tới nhiễu||Summary: from Fourier to noise⟧"],
            slides=[
                ("⟦Liên tục theo bình phương trung bình||Mean-square continuity⟧",
                 "<p>⟦Vì hàm mẫu là ngẫu nhiên, ta định nghĩa liên tục, đạo hàm và tích phân theo hội tụ bình phương trung bình: $X(t)$ liên tục tại $t$ nếu $E[|X(t+\\varepsilon)-X(t)|^2]\\to0$ khi $\\varepsilon\\to0$; với quá trình dừng rộng, điều đó tương đương $R_{xx}(\\tau)$ liên tục tại $\\tau=0$ (Barkat, mục 3.9.1, tr. 194 đến 196). Vì $E[|X(t+\\varepsilon)-X(t)|^2]=2[R(0)-R(\\varepsilon)]$. Số đo với $R=e^{-|\\tau|}$: tại $\\varepsilon=0.01$ giá trị là {{mc_01}}, tiến về 0.||Since sample functions are random, continuity, derivative and integral are defined by mean-square convergence: $X(t)$ is continuous at $t$ if $E[|X(t+\\varepsilon)-X(t)|^2]\\to0$ as $\\varepsilon\\to0$; for a wide-sense stationary process this is equivalent to $R_{xx}(\\tau)$ being continuous at $\\tau=0$ (Barkat, section 3.9.1, pp. 194 to 196). Because $E[|X(t+\\varepsilon)-X(t)|^2]=2[R(0)-R(\\varepsilon)]$. Measured with $R=e^{-|\\tau|}$: at $\\varepsilon=0.01$ the value is {{mc_01}}, tending to 0.⟧</p>"),
                ("⟦Đạo hàm và tích phân của quá trình||Differentiation and integration of a process⟧",
                 "<p>⟦Đạo hàm bình phương trung bình tồn tại nếu $R_{xx}''(0)$ tồn tại, và khi đó $R_{x'x'}(\\tau)=-R_{xx}''(\\tau)$; tích phân $\\int_a^bX(t)dt$ tồn tại nếu $\\int\\int R_{xx}(t_1,t_2)$ hữu hạn (Barkat, mục 3.9.2 và 3.9.3, tr. 196 đến 201). Với $R=e^{-|\\tau|}$, $R''$ không tồn tại tại 0 (góc nhọn): quá trình liên tục nhưng không khả vi; với $R=e^{-\\tau^2/2}$ thì $R_{x'x'}(0)$ = {{dv_0}}, đúng $-R''(0)=1$, kiểm bằng sai phân hữu hạn của mô phỏng. Đây là định lý đạo hàm của Bracewell ($f'\\supset i2\\pi sF$) áp dụng cho $R$: $S_{x'x'}=4\\pi^2f^2S_{xx}$.||The mean-square derivative exists if $R_{xx}''(0)$ exists, and then $R_{x'x'}(\\tau)=-R_{xx}''(\\tau)$; the integral $\\int_a^bX(t)dt$ exists if $\\int\\int R_{xx}(t_1,t_2)$ is finite (Barkat, sections 3.9.2 and 3.9.3, pp. 196 to 201). With $R=e^{-|\\tau|}$, $R''$ does not exist at 0 (a sharp corner): the process is continuous but not differentiable; with $R=e^{-\\tau^2/2}$ then $R_{x'x'}(0)$ = {{dv_0}}, exactly $-R''(0)=1$, checked by finite differences of a simulation. This is Bracewell's derivative theorem ($f'\\supset i2\\pi sF$) applied to $R$: $S_{x'x'}=4\\pi^2f^2S_{xx}$.⟧</p>"),
                ("⟦Nhiễu nhiệt||Thermal noise⟧",
                 "<p>⟦Nhiễu điện do chuyển động ngẫu nhiên của electron trong vật dẫn gọi là nhiễu nhiệt. Mật độ phổ công suất của điện áp nhiễu trên hai đầu điện trở $R$ là $S_{nn}(f)=2kTR\\dfrac{\\alpha^2}{\\alpha^2+\\omega^2}$, với $k=1.38\\times10^{-23}$ J/K là hằng số Boltzmann, $T$ nhiệt độ tuyệt đối (Barkat, mục 3.11, tr. 205 đến 206). $\\alpha$ cỡ $10^{14}$ rad/s, tức $10^{13}$ Hz, nên trong mọi băng thực tế $S_{nn}\\approx2kTR$: nhiễu trắng. Số đo với $R=1\\ \\text{k}\\Omega$, $T=290$ K: $2kTR$ = {{th_S}} V$^2$/Hz hai phía; tại $f=1$ GHz mật độ lệch khỏi phẳng chỉ {{th_flat}} tương đối.||Electrical noise arising from the random motion of electrons in conductors is called thermal noise. The power spectral density of the noise voltage across a resistor $R$ is $S_{nn}(f)=2kTR\\dfrac{\\alpha^2}{\\alpha^2+\\omega^2}$, with $k=1.38\\times10^{-23}$ J/K Boltzmann's constant and $T$ the absolute temperature (Barkat, section 3.11, pp. 205 to 206). $\\alpha$ is of order $10^{14}$ rad/s, i.e. $10^{13}$ Hz, so over any practical band $S_{nn}\\approx2kTR$: white noise. Measured with $R=1\\ \\text{k}\\Omega$, $T=290$ K: $2kTR$ = {{th_S}} V$^2$/Hz two-sided; at $f=1$ GHz the density deviates from flat by only {{th_flat}} relative.⟧</p>"),
                ("⟦Điện áp nhiễu hiệu dụng||The rms noise voltage⟧",
                 "<p>⟦Qua băng thông $B$ (tích phân hai phía trên $-B$ đến $B$), $\\overline{v^2}=\\int S_{nn}df=4kTRB$, hay $v_{rms}=\\sqrt{4kTRB}$, công thức Johnson. Với $R=1\\ \\text{k}\\Omega$, $T=290$ K, $B=1$ MHz: $v_{rms}$ = {{th_v}} V, tính bằng công thức và bằng tích phân số của phổ Lorentz tới $B$. Nhiễu này Gauss (giới hạn trung tâm cho vô số electron) và độc lập với dòng, nên cộng công suất khi ghép nối tiếp: hai điện trở nối tiếp có $\\overline{v^2}$ bằng tổng, như phương sai cộng (module 10).||Through a bandwidth $B$ (two-sided integration over $-B$ to $B$), $\\overline{v^2}=\\int S_{nn}df=4kTRB$, i.e. $v_{rms}=\\sqrt{4kTRB}$, Johnson's formula. With $R=1\\ \\text{k}\\Omega$, $T=290$ K, $B=1$ MHz: $v_{rms}$ = {{th_v}} V, by formula and by numerical integration of the Lorentzian spectrum up to $B$. The noise is Gaussian (central limit over countless electrons) and independent of any current, so powers add in series: two resistors in series have $\\overline{v^2}$ equal to the sum, like variances adding (module 10).⟧</p>"),
                ("⟦Nhiễu nhiệt và độ chính xác đo||Thermal noise and measurement precision⟧",
                 "<p>⟦Kết hợp hai kết quả: nếu ta đo công suất nhiễu nhiệt bằng tách sóng bình phương và trung bình $T=1$ s trong băng $B=1$ MHz, độ chính xác tương đối là $1/\\sqrt{TB}$ = {{th_prec}}: sau 1 giây, ta xác định công suất nhiễu đến một phần một nghìn. Đó là nguyên lý của máy đo bức xạ trong thiên văn vô tuyến (Bracewell, tr. 466 đến 468): tăng độ nhạy bằng tăng cả băng thông và thời gian tích lũy. Ngược lại, tín hiệu yếu hơn nhiễu chỉ phát hiện được nếu độ lệch cỡ này nhỏ hơn tín hiệu.||Combine two results: if we measure thermal noise power by square-law detection and averaging $T=1$ s in a band $B=1$ MHz, the relative precision is $1/\\sqrt{TB}$ = {{th_prec}}: after one second we determine the noise power to one part in a thousand. This is the principle of the radiometer in radio astronomy (Bracewell, pp. 466 to 468): sensitivity rises with both bandwidth and integration time. Conversely, a signal weaker than the noise can be detected only if this fluctuation is smaller than the signal.⟧</p>"),
                ("⟦Sơ đồ tổng: hai sách gặp nhau||The big picture: how the two books meet||⟧".replace("||⟧", "⟧"),
                 TBL(["⟦Ý tưởng||Idea⟧", "Bracewell", "Barkat"],
                     [["⟦Tổng độc lập là tích chập||Independent sum is a convolution⟧", "⟦ch. 16, tr. 429||ch. 16, p. 429⟧", "⟦mục 1.6.2, tr. 52||section 1.6.2, p. 52⟧"], ["⟦Nhiễu qua bộ lọc thành Gauss||Filtered noise becomes Gaussian⟧", "⟦ch. 17, tr. 451 đến 454||ch. 17, pp. 451 to 454⟧", "⟦mục 2.3.2, tr. 95||section 2.3.2, p. 95⟧"],
                      ["⟦Tự tương quan là biến đổi của phổ công suất||Autocorrelation is the transform of the power spectrum⟧", "⟦tr. 122, tr. 460||pp. 122, 460⟧", "⟦mục 3.5, tr. 174||section 3.5, p. 174⟧"], ["⟦Đầu ra bộ lọc: $|T|^2$||Filter output: $|T|^2$⟧", "⟦tr. 461||p. 461⟧", "⟦mục 3.6, tr. 181||section 3.6, p. 181⟧"], ["⟦Đường bao Rayleigh||The Rayleigh envelope⟧", "⟦tr. 465||p. 465⟧", "⟦mục 2.3.6, tr. 106||section 2.3.6, p. 106⟧"], ["⟦Biến đổi Hilbert||The Hilbert transform⟧", "⟦ch. 13 và 9||ch. 13 and 9⟧", "⟦mục 3.10, tr. 201||section 3.10, p. 201⟧"]])),
                ("⟦Bài tập: hai nguồn nhiễu cộng nhau||A problem: two noise sources add||⟧".replace("||⟧", "⟧"),
                 "<p>⟦Hai điện trở $R_1=1\\ \\text{k}\\Omega$ và $R_2=4\\ \\text{k}\\Omega$ ở 290 K nối tiếp, băng 1 MHz: nhiễu độc lập nên $v_{rms}^2=v_1^2+v_2^2$, $v_{rms}$ = {{th_v2}} V, lớn hơn cả hai nhưng nhỏ hơn tổng $v_1+v_2$ = {{th_vsum}} V. Đây là quy tắc \"cộng theo phương sai\" của module 10 áp dụng cho nhiễu điện; sai lầm hay gặp là cộng biên độ hiệu dụng. Số đo trùng cả tích phân số và mô phỏng.||Two resistors $R_1=1\\ \\text{k}\\Omega$ and $R_2=4\\ \\text{k}\\Omega$ at 290 K in series, band 1 MHz: the noises are independent so $v_{rms}^2=v_1^2+v_2^2$, $v_{rms}$ = {{th_v2}} V, larger than either but smaller than the sum $v_1+v_2$ = {{th_vsum}} V. This is module 10's \"add by variance\" rule applied to electrical noise; the common mistake is adding rms amplitudes. The numbers agree between numerical integration and simulation.⟧</p>"),
                ("⟦Tự kiểm tra phần 5||Self-check, part 5⟧",
                 UL(["⟦Khi nào quá trình dừng rộng khả vi theo bình phương trung bình?||When is a wide-sense stationary process mean-square differentiable?⟧",
                     "⟦Điện áp nhiễu nhiệt hiệu dụng phụ thuộc thế nào vào $R$, $T$, $B$?||How does the rms thermal noise voltage depend on $R$, $T$, $B$?⟧",
                     "⟦Vì sao nhiễu nhiệt là trắng và Gauss?||Why is thermal noise white and Gaussian?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: khi $R''(0)$ tồn tại; $\\sqrt{4kTRB}$; $\\alpha$ rất lớn nên phẳng, và giới hạn trung tâm cho vô số electron.||Hints: when $R''(0)$ exists; $\\sqrt{4kTRB}$; $\\alpha$ is very large so it is flat, and the central limit over countless electrons.⟧</p>"),
                ("⟦Tổng kết||Summary⟧",
                 UL(["⟦Quá trình ngẫu nhiên: họ biến ngẫu nhiên, đặc trưng bằng trung bình và tự tương quan; dừng rộng khi $R$ chỉ phụ thuộc $\\tau$.||A random process: a family of random variables characterised by mean and autocorrelation; wide-sense stationary when $R$ depends only on $\\tau$.⟧",
                     "⟦Phổ công suất $S=\\mathcal F[R]$; hệ tuyến tính: $S_{yy}=|H|^2S_{xx}$; nhiễu qua bộ lọc gần Gauss, đường bao Rayleigh, bình phương mũ.||Power spectrum $S=\\mathcal F[R]$; linear system: $S_{yy}=|H|^2S_{xx}$; filtered noise is nearly Gaussian, the envelope Rayleigh, its square exponential.⟧",
                     "⟦Đo công suất nhiễu chính xác tới $1/\\sqrt{T\\Delta f}$; nhiễu nhiệt trắng, $v_{rms}=\\sqrt{4kTRB}$.||Noise power is measured to a precision $1/\\sqrt{T\\Delta f}$; thermal noise is white, $v_{rms}=\\sqrt{4kTRB}$.⟧"])),
            ]),
    ],
    takeaways=[
        "⟦Quá trình ngẫu nhiên đặc trưng bằng trung bình và tự tương quan; dừng rộng khi $R$ chỉ phụ thuộc $\\tau$; ergodic khi trung bình thời gian bằng trung bình tập hợp.||A random process is characterised by mean and autocorrelation; wide-sense stationary when $R$ depends only on $\\tau$; ergodic when time averages equal ensemble averages.⟧",
        "⟦Tự tương quan và mật độ phổ công suất là cặp Fourier; hệ tuyến tính nhân phổ với $|H|^2$ và làm tự tương quan thành $R_{xx}*h*h(-\\tau)$.||Autocorrelation and power spectral density are a Fourier pair; a linear system multiplies the spectrum by $|H|^2$ and turns the autocorrelation into $R_{xx}*h*h(-\\tau)$.⟧",
        "⟦Nhiễu qua bộ lọc: biên độ gần Gauss, đường bao Rayleigh, tách sóng bình phương cho phân bố mũ.||Filtered noise: near-Gaussian amplitude, Rayleigh envelope, square-law detection gives an exponential distribution.⟧",
        "⟦Đo công suất nhiễu có dao động tương đối $1/\\sqrt{T\\Delta f}$: tăng băng thông và thời gian tích lũy.||A noise power measurement fluctuates by $1/\\sqrt{T\\Delta f}$: raise bandwidth and integration time.⟧",
        "⟦Nhiễu nhiệt là trắng, Gauss, $v_{rms}=\\sqrt{4kTRB}$, và công suất nhiễu độc lập cộng nhau.||Thermal noise is white, Gaussian, $v_{rms}=\\sqrt{4kTRB}$, and independent noise powers add.⟧",
    ],
    history="<p>⟦Bracewell trích Kendall và Smith (1940) về các chữ số ngẫu nhiên, Swarup, Thompson và Bracewell (1963) về cấu trúc Cygnus A, và các sách của Gardner (1988), Goodman (1966, 1996), Papoulis (1968), Parzen (1960), Ripley (1981) (chương 17, tr. 447, 469). Barkat lấy Papoulis, Peebles, Stark và Woods, Urkowitz, Shanmugan và Breipohl làm tài liệu chính cho quá trình ngẫu nhiên (thư mục, tr. 221). Bracewell (1962) giới thiệu kỹ thuật thiên văn vô tuyến với các bộ lọc thu và làm trơn ở bảng 17.1.||"
            "Bracewell cites Kendall and Smith (1940) for random digits, Swarup, Thompson and Bracewell (1963) for the structure of Cygnus A, and the books of Gardner (1988), Goodman (1966, 1996), Papoulis (1968), Parzen (1960), Ripley (1981) (chapter 17, pp. 447, 469). Barkat takes Papoulis, Peebles, Stark and Woods, Urkowitz, Shanmugan and Breipohl as main sources on random processes (bibliography, p. 221). Bracewell (1962) presents radio astronomy techniques with the reception and smoothing filters of Table 17.1.⟧</p>",
    case="<p>⟦<b>Phát hiện một nguồn yếu trong nhiễu.</b> Một máy thu thiên văn vô tuyến đo công suất nhiễu qua băng $\\Delta f=50$ Hz với thời gian tích lũy $T=1$ s: độ chính xác tương đối {{tf_th}}; muốn phân biệt tín hiệu cỡ 1 phần trăm công suất nhiễu ta cần $T\\Delta f$ cỡ $10^4$, tức tăng thời gian lên 200 lần hoặc băng lên 200 lần. Nhiễu nhiệt của điện trở 1 kΩ trong 1 MHz là {{th_v}} V; nhiễu qua bộ lọc là Gauss với đường bao Rayleigh, nên ngưỡng phát hiện chọn theo phân bố Rayleigh cho xác suất báo động giả mong muốn: $1-F(\\sigma)$ = {{ray_tail}} tại $r=\\sigma$. Đây là chuẩn bị cho các module 21 đến 26: quyết định giữa \"chỉ có nhiễu\" và \"có tín hiệu\".||"
          "<b>Detecting a weak source in noise.</b> A radio-astronomy receiver measures noise power through a band $\\Delta f=50$ Hz with integration time $T=1$ s: the relative precision is {{tf_th}}; to distinguish a signal of about 1 percent of the noise power we need $T\\Delta f$ of order $10^4$, i.e. 200 times longer or a band 200 times wider. The thermal noise of a 1 kΩ resistor in 1 MHz is {{th_v}} V; filtered noise is Gaussian with a Rayleigh envelope, so a detection threshold is chosen from the Rayleigh distribution for the desired false-alarm probability: $1-F(\\sigma)$ = {{ray_tail}} at $r=\\sigma$. This prepares modules 21 to 26: the decision between \"noise only\" and \"signal present\".⟧</p>",
    practice=[
        "⟦Mở notebook và chạy cell cài đặt.||Open the notebook and run the setup cell.⟧",
        "⟦Bài 1: tạo nhiễu thông dải bằng $y_t=ay_{t-1}+by_{t-2}+\\epsilon_t$ với vài cặp $(a,b)$ và vẽ phổ; xác nhận tần số đỉnh và độ rộng băng.||Task 1: generate bandpass noise with $y_t=ay_{t-1}+by_{t-2}+\\epsilon_t$ for several $(a,b)$ and plot the spectrum; confirm the peak frequency and bandwidth.⟧",
        "⟦Bài 2: đo tỉ số rms trên trung bình sau tách sóng bình phương với vài $T$ và $\\Delta f$; xác nhận $1/\\sqrt{T\\Delta f}$.||Task 2: measure the rms to mean ratio after square-law detection for several $T$ and $\\Delta f$; confirm $1/\\sqrt{T\\Delta f}$.⟧",
        "⟦Bài 3: tính $R_{yy}$ của nhiễu trắng qua mạch bậc hai và so với tích chập $h*h(-\\tau)$.||Task 3: compute $R_{yy}$ of white noise through a second-order circuit and compare with the convolution $h*h(-\\tau)$.⟧",
        "⟦Bài 4: thử ergodic với quá trình có thành phần một chiều ngẫu nhiên cộng nhiễu, và tách phần không ergodic.||Task 4: test ergodicity for a process with a random d.c. component plus noise, and separate the nonergodic part.⟧",
    ],
    pitfalls=[
        "<b>⟦\"Tung đồng xu theo khoảng là quá trình dừng.\"||\"Coin tossing by intervals is a stationary process.\"⟧</b><p>⟦Không: tương quan phụ thuộc vị trí trong khoảng ({{rb_same}} so với {{rb_diff}}); phải thêm độ dời ngẫu nhiên đều mới được $R=1-|\\tau|/T$ ({{rb_tri}} tại $\\tau=0.25T$).||No: the correlation depends on the position within an interval ({{rb_same}} against {{rb_diff}}); a uniform random shift must be added to get $R=1-|\\tau|/T$ ({{rb_tri}} at $\\tau=0.25T$).⟧</p>",
        "<b>⟦\"Dừng là ergodic.\"||\"Stationary means ergodic.\"⟧</b><p>⟦$X=C$ ngẫu nhiên là dừng nhưng trung bình thời gian của mỗi hàm mẫu là $C$, khác nhau giữa các hàm mẫu (phương sai {{er_v}}).||$X=C$ with random $C$ is stationary but the time average of each sample function is $C$, different between sample functions (variance {{er_v}}).⟧</p>",
        "<b>⟦\"Cộng các điện áp nhiễu hiệu dụng của hai điện trở nối tiếp.\"||\"Add the rms noise voltages of two series resistors.\"⟧</b><p>⟦Nhiễu độc lập cộng theo công suất: $v_{rms}$ = {{th_v2}} V, không phải {{th_vsum}} V.||Independent noises add in power: $v_{rms}$ = {{th_v2}} V, not {{th_vsum}} V.⟧</p>",
        "<b>⟦\"Hệ số tương quan nhỏ nghĩa là độc lập.\"||\"A small correlation coefficient means independence.\"⟧</b><p>⟦Hình 17.6 của Bracewell cho thấy biểu đồ phụ thuộc mà hệ số tương quan nhỏ; chỉ với Gauss thì không tương quan là độc lập (module 11).||Bracewell's Fig. 17.6 shows a diagram with dependence though the correlation coefficient is small; only for Gaussians is uncorrelated independent (module 11).⟧</p>",
    ],
    refs=[
        "⟦R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chương 17 (tr. 445 đến 472).||R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chapter 17 (pp. 445 to 472).⟧",
        "⟦M. Barkat, <i>Signal Detection and Estimation</i>, 2nd ed., Artech House, 2005, chương 3 (tr. 141 đến 221).||M. Barkat, <i>Signal Detection and Estimation</i>, 2nd ed., Artech House, 2005, chapter 3 (pp. 141 to 221).⟧",
        "⟦Tài liệu do các chương trích: Kendall và Smith (1940), Swarup, Thompson và Bracewell (1963), Bracewell (1962), Gardner (1988), Goodman (1966, 1996), Papoulis (1968).||Works cited by the chapters: Kendall and Smith (1940), Swarup, Thompson and Bracewell (1963), Bracewell (1962), Gardner (1988), Goodman (1966, 1996), Papoulis (1968).⟧",
    ],
    quiz=[
        dict(q="⟦$R(\\tau=0.1)$ của $A\\cos(2\\pi t+\\Theta)$ với $A=2$ bằng bao nhiêu?||What is $R(\\tau=0.1)$ of $A\\cos(2\\pi t+\\Theta)$ with $A=2$?⟧",
             opts=["{{rp_R}}", "2.0000", "1.2360", "0.6180"], explain="⟦$\\tfrac{A^2}2\\cos(0.2\\pi)$ = {{rp_R}}; $R(0)$ = {{rp_R0}}.||$\\tfrac{A^2}2\\cos(0.2\\pi)$ = {{rp_R}}; $R(0)$ = {{rp_R0}}.⟧"),
        dict(q="⟦Tung đồng xu theo khoảng: $R_{xx}(t_1,t_2)$ khi $t_1,t_2$ trong hai khoảng khác nhau bằng bao nhiêu?||Coin tossing by intervals: what is $R_{xx}(t_1,t_2)$ when $t_1,t_2$ are in different intervals?⟧",
             opts=["{{rb_diff}}", "1.0000", "0.5000", "-1.0000"], explain="⟦Các lần tung độc lập: $E[X(t_1)]E[X(t_2)]=0$; cùng khoảng {{rb_same}}.||The tosses are independent: $E[X(t_1)]E[X(t_2)]=0$; same interval {{rb_same}}.⟧"),
        dict(q="⟦Nhị phân ngẫu nhiên có độ dời: $R_{yy}(0.25T)$ bằng bao nhiêu?||Random binary transmission with a shift: what is $R_{yy}(0.25T)$?⟧",
             opts=["{{rb_tri}}", "0.2500", "0.5000", "1.0000"], explain="⟦$1-|\\tau|/T$ = {{rb_tri}}.||$1-|\\tau|/T$ = {{rb_tri}}.⟧"),
        dict(q="⟦$R_{iq}(\\tau=0.1)$ ở ví dụ 3.3 ($\\sigma=1$, $f=1$) bằng bao nhiêu?||What is $R_{iq}(\\tau=0.1)$ in example 3.3 ($\\sigma=1$, $f=1$)?⟧",
             opts=["{{iq_r}}", "-0.5878", "0.8090", "1.0000"], explain="⟦$\\sigma^2\\sin\\omega\\tau$ = {{iq_r}} (dấu dương từ phép tính).||$\\sigma^2\\sin\\omega\\tau$ = {{iq_r}} (plus sign from the computation).⟧"),
        dict(q="⟦$E[X(1.25)]$ của xung ngẫu nhiên ($A$ đều $(1,3)$, $\\Theta$ đều $(0,1)$, $s=\\Pi$) bằng bao nhiêu?||What is $E[X(1.25)]$ of the random pulse ($A$ uniform $(1,3)$, $\\Theta$ uniform $(0,1)$, $s=\\Pi$)?⟧",
             opts=["{{pl_e}}", "2.0000", "1.0000", "0.2500"], explain="⟦$E[A]\\cdot P(\\Theta>0.75)=2\\times0.25$ = {{pl_e}}; ba xung: {{pl_e3}}.||$E[A]\\cdot P(\\Theta>0.75)=2\\times0.25$ = {{pl_e}}; three pulses: {{pl_e3}}.⟧"),
        dict(q="⟦$R_{xx}(0.5,0.5)$ của xung ngẫu nhiên đó bằng bao nhiêu?||What is $R_{xx}(0.5,0.5)$ of that random pulse?⟧",
             opts=["{{pl_r}}", "4.0000", "2.0000", "0.3333"], explain="⟦$E[A^2]=\\text{var}+m^2=\\tfrac13+4$ = {{pl_r}}.||$E[A^2]=\\text{var}+m^2=\\tfrac13+4$ = {{pl_r}}.⟧"),
        dict(q="⟦$R(0)$ của sóng vuông ±1 với pha ngẫu nhiên bằng bao nhiêu (và $R(0.5)$)?||What is $R(0)$ of a ±1 square wave with random phase (and $R(0.5)$)?⟧",
             opts=["{{cy_r0}}", "0.5000", "0.0000", "2.0000"], explain="⟦$R(0)=E[X^2]$ = {{cy_r0}}; $R(0.5)$ = {{cy_r5}} (nửa chu kỳ đảo dấu).||$R(0)=E[X^2]$ = {{cy_r0}}; $R(0.5)$ = {{cy_r5}} (a half period reverses sign).⟧"),
        dict(q="⟦Phương sai của $y_t=0.8y_{t-1}+w_t$ ($\\sigma_w=1$) bằng bao nhiêu?||What is the variance of $y_t=0.8y_{t-1}+w_t$ ($\\sigma_w=1$)?⟧",
             opts=["{{ga_var}}", "1.0000", "1.6667", "3.2000"], explain="⟦$1/(1-\\rho^2)$ = {{ga_var}}; $R(1)$ = {{ga_r1}}.||$1/(1-\\rho^2)$ = {{ga_var}}; $R(1)$ = {{ga_r1}}.⟧"),
        dict(q="⟦$P[N(0,1.5)=3]$ của Poisson $\\lambda=2$ bằng bao nhiêu?||What is $P[N(0,1.5)=3]$ for a Poisson process with $\\lambda=2$?⟧",
             opts=["{{pp_p}}", "0.1494", "0.4231", "0.3000"], explain="⟦$3^3e^{-3}/3!$ = {{pp_p}}; khoảng trung bình {{pp_ia}}.||$3^3e^{-3}/3!$ = {{pp_p}}; mean interval {{pp_ia}}.⟧"),
        dict(q="⟦Quá trình nhị thức $n=20$, $p=0.3$: $P[S=6]$ bằng bao nhiêu?||Binomial process $n=20$, $p=0.3$: what is $P[S=6]$?⟧",
             opts=["{{bp_p6}}", "0.3000", "0.1200", "0.2500"], explain="⟦$\\binom{20}6(0.3)^6(0.7)^{14}$ = {{bp_p6}}; $E$ = {{bp_e}}, phương sai {{bp_v}}.||$\\binom{20}6(0.3)^6(0.7)^{14}$ = {{bp_p6}}; $E$ = {{bp_e}}, variance {{bp_v}}.⟧"),
        dict(q="⟦$R_{xx}(10,25)$ của bước đi ngẫu nhiên $\\Delta=1$ bằng bao nhiêu?||What is $R_{xx}(10,25)$ of the random walk with $\\Delta=1$?⟧",
             opts=["{{rw_r}}", "25.000", "35.000", "15.000"], explain="⟦$\\Delta^2\\min(n_1,n_2)$ = {{rw_r}}.||$\\Delta^2\\min(n_1,n_2)$ = {{rw_r}}.⟧"),
        dict(q="⟦Phương sai của Wiener $\\alpha=0.5$ tại $t=4$ bằng bao nhiêu?||What is the variance of the Wiener process with $\\alpha=0.5$ at $t=4$?⟧",
             opts=["{{wi_v}}", "0.5000", "4.0000", "1.0000"], explain="⟦$\\alpha t$ = {{wi_v}}; $R(2,3)$ = {{wi_r}}.||$\\alpha t$ = {{wi_v}}; $R(2,3)$ = {{wi_r}}.⟧"),
        dict(q="⟦Mật độ hai bước Chapman-Kolmogorov của $X_n=0.8X_{n-1}+w_n$ tại $x_2=1$ cho $x_0=1$ bằng bao nhiêu?||What is the two-step Chapman-Kolmogorov density of $X_n=0.8X_{n-1}+w_n$ at $x_2=1$ given $x_0=1$?⟧",
             opts=["{{mk_ck}}", "0.3989", "0.2420", "0.1210"], explain="⟦$N(0.64,\\ 1.64)$ tại 1: {{mk_ck}}.||$N(0.64,\\ 1.64)$ at 1: {{mk_ck}}.⟧"),
        dict(q="⟦Trung bình của 32 chữ số đầu của $\\pi$ bằng bao nhiêu?||What is the mean of the first 32 digits of $\\pi$?⟧",
             opts=["{{pi_mean}}", "4.5000", "5.0000", "4.2500"], explain="⟦Tổng 155 chia 32 = {{pi_mean}}; giới hạn 4.5, phương sai {{dig_var}}.||Sum 155 over 32 = {{pi_mean}}; the limit is 4.5, variance {{dig_var}}.⟧"),
        dict(q="⟦Phương sai của một chữ số ngẫu nhiên đều từ 0 tới 9 bằng bao nhiêu?||What is the variance of a random digit uniform on 0 to 9?⟧",
             opts=["{{dig_var}}", "8.2500", "9.0000", "8.3333"], explain="⟦$(10^2-1)/12$ = {{dig_var}} (Bracewell, tr. 454: 8.25).||$(10^2-1)/12$ = {{dig_var}} (Bracewell, p. 454: 8.25).⟧"),
        dict(q="⟦Trung bình và phương sai của tổng 10 chữ số: phương sai bằng bao nhiêu?||Mean and variance of the sum of 10 digits: what is the variance?⟧",
             opts=["{{sum_v}}", "8.2500", "45.000", "165.00"], explain="⟦$10\\times8.25$ = {{sum_v}}; trung bình {{sum_m}}.||$10\\times8.25$ = {{sum_v}}; mean {{sum_m}}.⟧"),
        dict(q="⟦$P(40\\le\\eta\\le50)$ của tổng 10 chữ số (chính xác) bằng bao nhiêu?||What is $P(40\\le\\eta\\le50)$ for the sum of 10 digits (exact)?⟧",
             opts=["{{sum_p}}", "0.5000", "0.3830", "0.6827"], explain="⟦Chính xác {{sum_p}} qua tích chập; xấp xỉ chuẩn {{sum_pn}}.||Exact {{sum_p}} by convolution; normal approximation {{sum_pn}}.⟧"),
        dict(q="⟦Xác suất chuỗi độ dài 2 trên hoặc dưới 4.5 (theo $2^{-k}$) bằng bao nhiêu?||What is the probability of a run of length 2 above or below 4.5 (by $2^{-k}$)?⟧",
             opts=["{{run_2}}", "0.5000", "0.1250", "0.3333"], explain="⟦$2^{-2}$ = {{run_2}}; độ dài 1: {{run_1}}; độ dài 3: {{run_3}}.||$2^{-2}$ = {{run_2}}; length 1: {{run_1}}; length 3: {{run_3}}.⟧"),
        dict(q="⟦Hệ số bốn góc $\\psi$ của dữ liệu Gauss có $\\rho=0.9$ bằng bao nhiêu?||What is the quadrant coefficient $\\psi$ for Gaussian data with $\\rho=0.9$?⟧",
             opts=["{{psi_th}}", "0.9000", "0.8000", "0.9511"], explain="⟦$\\tfrac2\\pi\\arcsin0.9$ = {{psi_th}}; mô phỏng {{psi_09}}.||$\\tfrac2\\pi\\arcsin0.9$ = {{psi_th}}; simulation {{psi_09}}.⟧"),
        dict(q="⟦Hệ số tự tương quan bước 2 của tổng chạy 10 số bằng bao nhiêu?||What is the lag-2 autocorrelation of the ten-term running sum?⟧",
             opts=["{{ac_2}}", "0.9000", "0.6000", "0.7000"], explain="⟦$1-2/10$ = {{ac_2}}; bước 1: {{ac_1}}.||$1-2/10$ = {{ac_2}}; lag 1: {{ac_1}}.⟧"),
        dict(q="⟦Bộ lọc $\\{5\\,3\\,1\\,1\\}$: hệ số tự tương quan chuẩn hóa bước 1 bằng bao nhiêu?||For the filter $\\{5\\,3\\,1\\,1\\}$: what is the normalised autocorrelation at lag 1?⟧",
             opts=["{{g_1}}", "0.6000", "0.4167", "0.5000"], explain="⟦$19/36$ = {{g_1}}; bước 2: {{g_2}}; bước 3: {{g_3}}.||$19/36$ = {{g_1}}; lag 2: {{g_2}}; lag 3: {{g_3}}.⟧"),
        dict(q="⟦$|T(0.05)|^2$ của tổng chạy 10 số bằng bao nhiêu?||What is $|T(0.05)|^2$ for the ten-term running sum?⟧",
             opts=["{{pt_th}}", "100.00", "10.000", "20.000"], explain="⟦$[\\sin(0.5\\pi)/\\sin(0.05\\pi)]^2$ = {{pt_th}}; Welch {{pt_mc}}.||$[\\sin(0.5\\pi)/\\sin(0.05\\pi)]^2$ = {{pt_th}}; Welch {{pt_mc}}.⟧"),
        dict(q="⟦Đỉnh của phổ Gauss $\\frac1{0.24}e^{-\\pi(f/0.24)^2}$ tại $f=0$ bằng bao nhiêu?||What is the peak of the Gaussian spectrum $\\frac1{0.24}e^{-\\pi(f/0.24)^2}$ at $f=0$?⟧",
             opts=["{{gs_pk}}", "0.2400", "2.4000", "1.0000"], explain="⟦$1/0.24$ = {{gs_pk}}.||$1/0.24$ = {{gs_pk}}.⟧"),
        dict(q="⟦Tần số đỉnh của $y_t=1.84y_{t-1}-0.9y_{t-2}+\\epsilon_t$ (chu kỳ/mẫu) bằng bao nhiêu?||What is the peak frequency of $y_t=1.84y_{t-1}-0.9y_{t-2}+\\epsilon_t$ (cycles per sample)?⟧",
             opts=["{{ar_f}}", "0.2465", "0.0500", "0.0100"], explain="⟦$\\arccos(a/2r)/2\\pi$, $r=\\sqrt{0.9}$ = {{ar_r}}: {{ar_f}}; Welch {{ar_fmc}}.||$\\arccos(a/2r)/2\\pi$, $r=\\sqrt{0.9}$ = {{ar_r}}: {{ar_f}}; Welch {{ar_fmc}}.⟧"),
        dict(q="⟦Trung bình của $r/\\sigma$ với đường bao Rayleigh bằng bao nhiêu?||What is the mean of $r/\\sigma$ for a Rayleigh envelope?⟧",
             opts=["{{env_m}}", "1.0000", "0.8862", "1.7725"], explain="⟦$\\sqrt{\\pi/2}$ = {{env_m}}; độ lệch phân bố {{env_ks}}.||$\\sqrt{\\pi/2}$ = {{env_m}}; distribution deviation {{env_ks}}.⟧"),
        dict(q="⟦Sau tách sóng bình phương, phương sai của $V=r^2$ ($\\sigma=1$) bằng bao nhiêu?||After square-law detection, what is the variance of $V=r^2$ ($\\sigma=1$)?⟧",
             opts=["{{sq_v}}", "2.0000", "1.0000", "8.0000"], explain="⟦Mũ với trung bình {{sq_m}}: phương sai bằng bình phương trung bình = {{sq_v}}.||Exponential with mean {{sq_m}}: variance equals the squared mean = {{sq_v}}.⟧"),
        dict(q="⟦Tỉ số rms trên trung bình khi $T=1$ s, $\\Delta f=50$ Hz bằng bao nhiêu?||What is the rms-to-mean ratio for $T=1$ s, $\\Delta f=50$ Hz?⟧",
             opts=["{{tf_th}}", "0.0200", "0.5000", "0.0500"], explain="⟦$1/\\sqrt{T\\Delta f}$ = {{tf_th}}; mô phỏng {{tf_mc}}.||$1/\\sqrt{T\\Delta f}$ = {{tf_th}}; simulation {{tf_mc}}.⟧"),
        dict(q="⟦$\\sigma/(\\max-\\min)$ trung bình của 100 mẫu Gauss bằng bao nhiêu?||What is the mean of $\\sigma/(\\max-\\min)$ for 100 Gaussian samples?⟧",
             opts=["{{pp_100}}", "0.1550", "0.2500", "0.3333"], explain="⟦{{pp_100}} với 100 mẫu, {{pp_1000}} với 1000: quy tắc 1/5 đúng cho cỡ 100 mẫu.||{{pp_100}} for 100 samples, {{pp_1000}} for 1000: the 1/5 rule holds at about 100 samples.⟧"),
        dict(q="⟦Số lần cắt lên mỗi mẫu của dãy Gauss có $\\gamma_1=0.9$ bằng bao nhiêu?||How many upcrosses per sample for a Gaussian sequence with $\\gamma_1=0.9$?⟧",
             opts=["{{up_th}}", "0.1000", "0.2500", "0.0500"], explain="⟦$\\arccos(0.9)/2\\pi$ = {{up_th}}; mô phỏng {{up_mc}}.||$\\arccos(0.9)/2\\pi$ = {{up_th}}; simulation {{up_mc}}.⟧"),
        dict(q="⟦Tổng công suất của $\\tfrac{A^2}4[\\delta(f-f_0)+\\delta(f+f_0)]$ với $A=2$ bằng bao nhiêu?||What is the total power of $\\tfrac{A^2}4[\\delta(f-f_0)+\\delta(f+f_0)]$ with $A=2$?⟧",
             opts=["{{psd_tot}}", "4.0000", "1.0000", "0.5000"], explain="⟦$A^2/2$ = {{psd_tot}} $=R(0)$.||$A^2/2$ = {{psd_tot}} $=R(0)$.⟧"),
        dict(q="⟦$R_{yy}(0)$ của nhiễu trắng ($N_0=2$) qua $h=\\alpha e^{-\\alpha t}$, $\\alpha=5$ bằng bao nhiêu?||What is $R_{yy}(0)$ for white noise ($N_0=2$) through $h=\\alpha e^{-\\alpha t}$, $\\alpha=5$?⟧",
             opts=["{{rc_r0}}", "5.0000", "1.2500", "10.000"], explain="⟦$N_0\\alpha/4$ = {{rc_r0}}; $R_{yy}(0.1)$ = {{rc_r1}}.||$N_0\\alpha/4$ = {{rc_r0}}; $R_{yy}(0.1)$ = {{rc_r1}}.⟧"),
        dict(q="⟦Trung bình đầu ra của mạch RC với đầu vào trung bình 3 ($H(0)=1$) bằng bao nhiêu?||What is the output mean of the RC circuit for an input of mean 3 ($H(0)=1$)?⟧",
             opts=["{{rc_m}}", "0.0000", "1.0000", "6.0000"], explain="⟦$m_y=H(0)m_x$ = {{rc_m}}.||$m_y=H(0)m_x$ = {{rc_m}}.⟧"),
        dict(q="⟦Trung bình thời gian của $\\cos(2\\pi t+\\Theta)$ trên 100 chu kỳ bằng bao nhiêu?||What is the time average of $\\cos(2\\pi t+\\Theta)$ over 100 periods?⟧",
             opts=["{{er_t}}", "0.5000", "1.0000", "0.1000"], explain="⟦Bằng trung bình tập hợp 0: ergodic theo trung bình; với $X=C$ phương sai giữa hàm mẫu {{er_v}}.||Equal to the ensemble mean 0: ergodic in the mean; for $X=C$ the variance across sample functions is {{er_v}}.⟧"),
        dict(q="⟦Tỉ số công suất của tín hiệu giải tích $x+j\\hat x$ so với $x$ bằng bao nhiêu?||What is the ratio of the power of the analytic signal $x+j\\hat x$ to that of $x$?⟧",
             opts=["{{an_p}}", "1.0000", "4.0000", "0.5000"], explain="⟦$E[x^2]+E[\\hat x^2]=2E[x^2]$ = {{an_p}}.||$E[x^2]+E[\\hat x^2]=2E[x^2]$ = {{an_p}}.⟧"),
        dict(q="⟦Mật độ phổ hai phía $2kTR$ của điện trở 1 kΩ ở 290 K bằng bao nhiêu (V$^2$/Hz)?||What is the two-sided spectral density $2kTR$ of a 1 kΩ resistor at 290 K (V$^2$/Hz)?⟧",
             opts=["{{th_S}}", "1.60e-17", "4.00e-21", "8.00e-15"], explain="⟦$2\\times1.38\\times10^{-23}\\times290\\times10^3$ = {{th_S}}.||$2\\times1.38\\times10^{-23}\\times290\\times10^3$ = {{th_S}}.⟧"),
        dict(q="⟦Điện áp nhiễu hiệu dụng của 1 kΩ, 290 K, 1 MHz bằng bao nhiêu (V)?||What is the rms noise voltage of 1 kΩ at 290 K in 1 MHz (V)?⟧",
             opts=["{{th_v}}", "1.60e-05", "4.00e-09", "1.60e-11"], explain="⟦$\\sqrt{4kTRB}$ = {{th_v}}.||$\\sqrt{4kTRB}$ = {{th_v}}.⟧"),
        dict(q="⟦Hai điện trở 1 kΩ và 4 kΩ nối tiếp (290 K, 1 MHz): điện áp nhiễu hiệu dụng tổng bằng bao nhiêu?||Two resistors of 1 kΩ and 4 kΩ in series (290 K, 1 MHz): what is the total rms noise voltage?⟧",
             opts=["{{th_v2}}", "{{th_vsum}}", "1.6e-05", "8.0e-06"], explain="⟦Cộng công suất: {{th_v2}}, không phải tổng biên độ {{th_vsum}}.||Powers add: {{th_v2}}, not the sum of amplitudes {{th_vsum}}.⟧"),
        dict(q="⟦Vì sao tung đồng xu theo khoảng $\\pm1$ không dừng rộng?||Why is the ±1 coin-toss process by intervals not wide-sense stationary?⟧",
             opts=["⟦Tự tương quan phụ thuộc vị trí trong khoảng, không chỉ hiệu $\\tau$||It depends on the position in the interval, not only $\\tau$⟧",
                   "⟦Vì trung bình của nó không bằng 0 nên không thỏa điều kiện trung bình không đổi||Because its mean is not zero so the constant-mean condition fails⟧",
                   "⟦Vì bình phương trung bình của nó tăng theo thời gian như ở quá trình Wiener||Because its mean square grows with time as in the Wiener process⟧",
                   "⟦Vì các lần tung không độc lập với nhau nên tự tương quan không xác định||Because the tosses are not independent of each other so the autocorrelation is undefined⟧"],
             explain="⟦Barkat, tr. 148 đến 149: $R=1$ cùng khoảng, 0 khác khoảng.||Barkat, pp. 148 to 149: $R=1$ in the same interval, 0 in different intervals.⟧"),
        dict(q="⟦Tự tương quan của đầu ra bộ lọc khi đầu vào là dãy không tương quan là gì?||What is the autocorrelation of a filter output when the input is an uncorrelated sequence?⟧",
             opts=["⟦Tự tương quan của đáp ứng xung||The autocorrelation of the impulse response⟧",
                   "⟦Đáp ứng xung của bộ lọc dịch theo độ trễ, vì đầu vào chỉ là chuỗi xung||The impulse response of the filter shifted by the lag, since the input is just an impulse train⟧",
                   "⟦Bình phương đáp ứng xung, vì công suất tỉ lệ với bình phương biên độ||The square of the impulse response, since power is proportional to amplitude squared⟧",
                   "⟦Hàm delta, vì đầu ra giữ tính không tương quan của đầu vào||A delta function, since the output keeps the uncorrelatedness of the input⟧"],
             explain="⟦Bracewell, tr. 458: tự tương quan của dãy đầu ra là tự tương quan của đáp ứng xung.||Bracewell, p. 458: the autocorrelation of the output sequence is the autocorrelation of the impulse response.⟧"),
        dict(q="⟦Vì sao biên độ của nhiễu qua bộ lọc gần Gauss?||Why is the amplitude of noise through a filter nearly Gaussian?⟧",
             opts=["⟦Tổng có trọng số nhiều giá trị: giới hạn trung tâm áp dụng||A weighted sum of many values: the central limit applies⟧",
                   "⟦Vì bộ lọc luôn triệt các thành phần không Gauss bằng phép nhân với $|T|^2$||Because a filter always removes non-Gaussian components by multiplying with $|T|^2$⟧",
                   "⟦Vì nhiễu đầu vào đã Gauss và bộ lọc tuyến tính không đổi được dạng phân bố||Because the input noise is already Gaussian and a linear filter cannot change the distribution shape⟧",
                   "⟦Vì bộ lọc trung bình hóa theo thời gian nên làm phương sai tiến về 0||Because a filter averages over time so the variance tends to zero⟧"],
             explain="⟦Bracewell, tr. 454: tổng có trọng số các giá trị nên phân bố gần chuẩn hơn.||Bracewell, p. 454: a weighted sum of values gives a distribution closer to normal.⟧"),
        dict(q="⟦Đường bao của nhiễu Gauss thông dải và bình phương của nó có phân bố gì?||What distributions do the envelope of bandpass Gaussian noise and its square have?⟧",
             opts=["⟦Rayleigh và mũ||Rayleigh and exponential⟧",
                   "⟦Chuẩn và chi bình phương một bậc, như bình phương của một biến chuẩn||Normal and one-degree chi-square, like the square of a normal variable⟧",
                   "⟦Rice và Rayleigh, vì đường bao mang cả tín hiệu lẫn nhiễu||Rice and Rayleigh, since the envelope carries both signal and noise||⟧".replace("||⟧","⟧"),
                   "⟦Đều và tam giác, vì đường bao bị chặn trong khoảng hữu hạn||Uniform and triangular, since the envelope is bounded within a finite range⟧"],
             explain="⟦Bracewell, tr. 465 đến 466: Rayleigh; bình phương cho mũ cắt cụt.||Bracewell, pp. 465 to 466: Rayleigh; the square gives the truncated exponential.⟧"),
        dict(q="⟦Để giảm dao động tương đối của phép đo công suất nhiễu mười lần cần làm gì?||What is needed to reduce the relative fluctuation of a noise power measurement tenfold?⟧",
             opts=["⟦Tăng tích $T\\Delta f$ một trăm lần||Raise the product $T\\Delta f$ a hundredfold⟧",
                   "⟦Tăng riêng thời gian tích lũy $T$ mười lần, không cần đổi băng thông||Raise the integration time $T$ alone tenfold, with no change of bandwidth⟧",
                   "⟦Giảm băng thông $\\Delta f$ mười lần để nhiễu ít hơn đi vào bộ tách sóng||Reduce the bandwidth $\\Delta f$ tenfold so that less noise enters the detector⟧",
                   "⟦Dùng bộ tách sóng tuyến tính thay cho bình phương, vì nó bảo toàn biên độ||Use a linear detector instead of square-law, since it preserves amplitude⟧"],
             explain="⟦Bracewell, tr. 467 đến 468: rms/mean $=1/\\sqrt{\\tau\\Delta f}$.||Bracewell, pp. 467 to 468: rms/mean $=1/\\sqrt{\\tau\\Delta f}$.⟧"),
        dict(q="⟦Mật độ phổ công suất liên hệ với tự tương quan thế nào?||How is the power spectral density related to the autocorrelation?⟧",
             opts=["⟦Là biến đổi Fourier của tự tương quan||It is the Fourier transform of the autocorrelation⟧",
                   "⟦Bằng bình phương của tự tương quan tại mỗi độ trễ, vì công suất là bình phương||It equals the square of the autocorrelation at each lag, since power is a square⟧",
                   "⟦Là đạo hàm của tự tương quan theo độ trễ, tại tần số tương ứng||It is the derivative of the autocorrelation with respect to lag, at the corresponding frequency⟧",
                   "⟦Là biến đổi Laplace của tự tương quan, chỉ xác định cho độ trễ dương||It is the Laplace transform of the autocorrelation, defined only for positive lags⟧"],
             explain="⟦Barkat, mục 3.5, tr. 174: Wiener-Khinchin.||Barkat, section 3.5, p. 174: Wiener-Khinchin.⟧"),
        dict(q="⟦Vì sao quá trình $X=C$ với $C$ ngẫu nhiên không ergodic?||Why is the process $X=C$ with random $C$ not ergodic?⟧",
             opts=["⟦Trung bình thời gian của mỗi hàm mẫu là $C$, không phải $E[C]$||The time average of each sample function is $C$, not $E[C]$⟧",
                   "⟦Vì nó không dừng rộng nên không thể ergodic theo định nghĩa của Barkat||Because it is not wide-sense stationary so it cannot be ergodic by Barkat's definition⟧",
                   "⟦Vì phương sai của $C$ luôn lớn hơn trung bình thời gian của bình phương||Because the variance of $C$ always exceeds the time average of the square⟧",
                   "⟦Vì tự tương quan của nó tiến về không khi độ trễ tiến tới vô cực||Because its autocorrelation tends to zero as the lag tends to infinity⟧"],
             explain="⟦Barkat, tr. 186 đến 187: ergodic cần trung bình thời gian bằng trung bình tập hợp; phương sai giữa hàm mẫu {{er_v}}.||Barkat, pp. 186 to 187: ergodicity needs time averages equal to ensemble averages; the variance across sample functions is {{er_v}}.⟧"),
        dict(q="⟦Điều kiện để quá trình dừng rộng khả vi theo bình phương trung bình là gì?||What is the condition for a wide-sense stationary process to be mean-square differentiable?⟧",
             opts=["⟦$R_{xx}''(0)$ tồn tại||$R_{xx}''(0)$ exists⟧",
                   "⟦$R_{xx}(\\tau)$ liên tục tại $\\tau=0$, điều kiện này cũng đủ cho đạo hàm||$R_{xx}(\\tau)$ is continuous at $\\tau=0$, which is also sufficient for a derivative⟧",
                   "⟦Mật độ phổ công suất bị chặn ở mọi tần số, dù suy giảm chậm||The power spectral density is bounded at every frequency, however slowly it decays⟧",
                   "⟦Quá trình phải Gauss, vì chỉ Gauss mới có đạo hàm bình phương trung bình||The process must be Gaussian, since only Gaussians have mean-square derivatives⟧"],
             explain="⟦Barkat, tr. 196: $R_{x'x'}=-R_{xx}''$; với $R=e^{-|\\tau|}$ góc nhọn nên không khả vi; $R=e^{-\\tau^2/2}$: {{dv_0}}.||Barkat, p. 196: $R_{x'x'}=-R_{xx}''$; with $R=e^{-|\\tau|}$ the corner means it is not differentiable; $R=e^{-\\tau^2/2}$: {{dv_0}}.⟧"),
    ],
    nb=[
        ("md", """## 1. ⟦Tập hợp, dừng, tương quan||Ensemble, stationarity, correlation⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Trung bình và tự tương quan của các quá trình mẫu (pha ngẫu nhiên, nhị phân, I/Q) có đúng công thức khi tính bằng trung bình tập hợp trên nhiều hàm mẫu?||Do the mean and autocorrelation of the standard processes (random phase, binary, I/Q) match the formulas when computed as ensemble averages over many sample functions?⟧"""),
        ("code", r'''from scipy import integrate, signal, stats, special
from math import comb, factorial
rg = np.random.default_rng(12)
trap = getattr(np, "trapezoid", None) or np.trapz
# ⟦pha ngẫu nhiên||random phase⟧
A, f0 = 2.0, 1.0
th = rg.uniform(0, 2*np.pi, 500000)
def Rphase(t, tau):
    return np.mean(A*np.cos(2*np.pi*f0*(t + tau) + th)*A*np.cos(2*np.pi*f0*t + th))
form = A**2/2*np.cos(2*np.pi*f0*0.1)
assert abs(np.mean(A*np.cos(2*np.pi*f0*0.37 + th))) < 0.01
assert abs(Rphase(0.37, 0.1) - form) < 0.01 and abs(Rphase(1.11, 0.1) - form) < 0.01
report("rp_mean", 0, "d"); report("rp_R", form, ".4f"); report("rp_R0", A**2/2, ".1f")
tg = np.linspace(-3, 3, 61); assert all(abs(A**2/2*np.cos(2*np.pi*f0*x)) <= A**2/2 + 1e-12 for x in tg)
# ⟦nhị phân ngẫu nhiên||random binary⟧
T = 1.0; N = 400000
bits = rg.choice([-1.0, 1.0], (N, 4))
val = lambda tt, sh: bits[np.arange(N), np.floor((tt - sh)/T).astype(int).clip(0, 3)]
zero = np.zeros(N)
same = np.mean(val(0.1*T, zero)*val(0.9*T, zero)); diff = np.mean(val(0.1*T, zero)*val(1.1*T, zero))
assert abs(same - 1) < 1e-12 and abs(diff) < 0.01
report("rb_same", same, ".0f"); report("rb_diff", 0, "d")
sh = rg.uniform(0, T, N)
tri_a = np.mean(val(1.3*T, sh)*val(1.55*T, sh)); tri_b = np.mean(val(2.4*T, sh)*val(2.65*T, sh))
assert abs(tri_a - 0.75) < 0.01 and abs(tri_b - 0.75) < 0.01
report("rb_tri", 0.75, ".2f")
# ⟦I/Q: σ = 1||I/Q: σ = 1⟧
Xq, Yq = rg.standard_normal(500000), rg.standard_normal(500000)
w = 2*np.pi; t0, tau = 0.31, 0.1
I1 = Xq*np.cos(w*(t0 + tau)) + Yq*np.sin(w*(t0 + tau)); Q0 = Yq*np.cos(w*t0) - Xq*np.sin(w*t0)
r_iq = np.sin(w*tau)
assert abs(np.mean(I1*Q0) - r_iq) < 0.01
report("iq_r", r_iq, ".4f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Pha ngẫu nhiên: trung bình {{rp_mean}}, $R(0.1)$ = {{rp_R}}, $R(0)$ = {{rp_R0}}. Nhị phân: cùng khoảng {{rb_same}}, khác khoảng {{rb_diff}}, có độ dời {{rb_tri}}. I/Q: {{iq_r}}.||Random phase: mean {{rp_mean}}, $R(0.1)$ = {{rp_R}}, $R(0)$ = {{rp_R0}}. Binary: same interval {{rb_same}}, different {{rb_diff}}, with a shift {{rb_tri}}. I/Q: {{iq_r}}.⟧"""),
        ("md", """## 2. ⟦Các quá trình mẫu||The standard processes⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Xung ngẫu nhiên, sóng vuông pha ngẫu nhiên, AR(1) Gauss, Poisson, nhị thức, bước đi ngẫu nhiên, Wiener và Markov có đúng các công thức trung bình và tự tương quan?||Do random pulses, a random-phase square wave, a Gaussian AR(1), Poisson, binomial, the random walk, Wiener and Markov processes obey the mean and autocorrelation formulas?⟧"""),
        ("code", r'''# ⟦xung ngẫu nhiên s = Π, A ~ U(1,3), Θ ~ U(0,1)||random pulse s = Π, A ~ U(1,3), Θ ~ U(0,1)⟧
NA = 600000
Am = rg.uniform(1, 3, NA); Th = rg.uniform(0, 1, NA)
pulse = lambda t: (np.abs(t) < 0.5).astype(float)
e125 = np.mean(Am*pulse(1.25 - Th))
q_e = 2*integrate.quad(lambda th_: float(abs(1.25 - th_) < 0.5), 0, 1, points=[0.75])[0]
assert abs(e125 - 0.5) < 0.01 and abs(q_e - 0.5) < 1e-9
r55 = np.mean(Am**2*pulse(0.5 - Th)*pulse(0.5 - Th))
q_r = (1/3 + 4)*integrate.quad(lambda th_: float(abs(0.5 - th_) < 0.5)**2, 0, 1)[0]
assert abs(r55 - q_r) < 0.03
report("pl_e", 0.5, ".2f"); report("pl_r", q_r, ".4f")
A3 = rg.uniform(1, 3, (200000, 3)); T3 = rg.uniform(0, 1, (200000, 3))
assert abs(np.mean((A3*pulse(1.25 - T3)).sum(axis=1)) - 1.5) < 0.02
report("pl_e3", 1.5, ".1f")
# ⟦sóng vuông chu kỳ 1, pha ngẫu nhiên||square wave period 1, random phase⟧
sq = lambda t: np.where((t % 1.0) < 0.5, 1.0, -1.0)
ph = rg.uniform(0, 1, 500000)
mean_sq = np.mean(sq(0.3 - ph)); R0 = np.mean(sq(0.3 - ph)**2); Rh = np.mean(sq(0.8 - ph)*sq(0.3 - ph))
assert abs(mean_sq) < 0.01 and abs(R0 - 1) < 1e-12 and abs(Rh + 1) < 1e-12
report("cy_mean", 0, "d"); report("cy_r0", R0, ".0f"); report("cy_r5", Rh, ".0f")
# ⟦AR(1) Gauss||Gaussian AR(1)⟧
rho = 0.8
wn = rg.standard_normal(600000); yy = signal.lfilter([1], [1, -rho], wn)
var_th = 1/(1 - rho**2)
assert abs(np.var(yy) - var_th) < 0.05 and abs(np.mean(yy[1:]*yy[:-1]) - rho*var_th) < 0.05
report("ga_var", var_th, ".4f"); report("ga_r1", rho*var_th, ".4f")
# ⟦Poisson||Poisson⟧
lam, tt = 2.0, 1.5
pk = stats.poisson.pmf(3, lam*tt)
nb_ = stats.binom.pmf(3, 10**6, lam*tt/10**6)
mcp = np.mean(rg.poisson(lam*tt, 600000) == 3)
assert abs(pk - nb_) < 1e-6 and abs(pk - mcp) < 0.003
ia = rg.exponential(1/lam, 600000)
assert abs(np.mean(ia) - 0.5) < 0.005
report("pp_p", pk, ".4f"); report("pp_ia", 1/lam, ".1f")
# ⟦nhị thức||binomial⟧
bp = stats.binom.pmf(6, 20, 0.3)
assert abs(bp - comb(20, 6)*0.3**6*0.7**14) < 1e-14
report("bp_p6", bp, ".4f"); report("bp_e", 6, "d"); report("bp_v", 20*0.3*0.7, ".1f")
# ⟦bước đi ngẫu nhiên||random walk⟧
W = np.cumsum(rg.choice([-1, 1], (200000, 25)), axis=1)
rw = np.mean(W[:, 9]*W[:, 24])
assert abs(rw - 10) < 0.15
report("rw_r", 10, "d")
# ⟦Wiener α = 0.5||Wiener α = 0.5⟧
al = 0.5; dt = 0.01
inc = rg.normal(0, np.sqrt(al*dt), (100000, 400)); Wt = np.cumsum(inc, axis=1)
assert abs(np.var(Wt[:, 399]) - al*4) < 0.04 and abs(np.mean(Wt[:, 199]*Wt[:, 299]) - al*2) < 0.02
report("wi_v", al*4, ".1f"); report("wi_r", al*2, ".1f")
# ⟦Chapman-Kolmogorov||Chapman-Kolmogorov⟧
x0, x2 = 1.0, 1.0
ck = integrate.quad(lambda x1: stats.norm.pdf(x2, rho*x1, 1)*stats.norm.pdf(x1, rho*x0, 1), -12, 12)[0]
direct = stats.norm.pdf(x2, rho**2*x0, np.sqrt(1 + rho**2))
assert abs(ck - direct) < 1e-10
report("mk_ck", ck, ".4f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Xung: $E[X(1.25)]$ = {{pl_e}}, $R$ = {{pl_r}}, ba xung {{pl_e3}}. Sóng vuông: {{cy_mean}}, {{cy_r0}}, {{cy_r5}}. AR(1): {{ga_var}}, {{ga_r1}}. Poisson: {{pp_p}} và khoảng {{pp_ia}}. Nhị thức: {{bp_p6}}, {{bp_e}}, {{bp_v}}. Bước đi: {{rw_r}}. Wiener: {{wi_v}}, {{wi_r}}. Markov: {{mk_ck}}.||Pulse: $E[X(1.25)]$ = {{pl_e}}, $R$ = {{pl_r}}, three pulses {{pl_e3}}. Square wave: {{cy_mean}}, {{cy_r0}}, {{cy_r5}}. AR(1): {{ga_var}}, {{ga_r1}}. Poisson: {{pp_p}} and interval {{pp_ia}}. Binomial: {{bp_p6}}, {{bp_e}}, {{bp_v}}. Walk: {{rw_r}}. Wiener: {{wi_v}}, {{wi_r}}. Markov: {{mk_ck}}.⟧"""),
        ("md", """## 3. ⟦Nhiễu từ chữ số ngẫu nhiên||Noise from random digits⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Các kết quả của Bracewell: trung bình chữ số, biên độ tổng 10 số gần chuẩn, chuỗi $2^{-k}$, hệ số bốn góc, tự tương quan sau lọc, phổ $|T|^2$, dãy nhị thức và Gauss, nhiễu thông dải, đường bao Rayleigh, tách sóng bình phương và giới hạn $1/\sqrt{T\Delta f}$.||Bracewell's results: the digit mean, the near-normal amplitude of a ten-digit sum, runs of $2^{-k}$, the quadrant coefficient, autocorrelation after filtering, the $|T|^2$ spectrum, the binomial and Gaussian sequences, bandpass noise, the Rayleigh envelope, square-law detection and the $1/\sqrt{T\Delta f}$ limit.⟧"""),
        ("code", r'''digs = [int(c) for c in "31415926535897932384626433832795"]
pim = np.mean(digs)
assert len(digs) == 32 and sum(digs) == 155
report("pi_mean", pim, ".2f")
dv = np.var(np.arange(10)); dm = np.mean(np.arange(10))
assert abs(dv - 8.25) < 1e-12 and abs(dm - 4.5) < 1e-12 and abs(dv - (10**2 - 1)/12) < 1e-12
Dg = rg.integers(0, 10, 1000000)
assert abs(np.mean(Dg) - 4.5) < 0.01 and abs(np.var(Dg) - 8.25) < 0.02
report("dig_m", dm, ".1f"); report("dig_var", dv, ".2f")
# ⟦tổng 10 số: tích chập chính xác||sum of 10: exact convolution⟧
pd = np.ones(10)/10; pm = pd.copy()
for _ in range(9): pm = np.convolve(pm, pd)
ys = np.arange(len(pm))
sm = np.sum(ys*pm); sv = np.sum(ys**2*pm) - sm**2
assert abs(sm - 45) < 1e-9 and abs(sv - 82.5) < 1e-9
pex = pm[40:51].sum(); pnorm = stats.norm.cdf(50.5, 45, np.sqrt(82.5)) - stats.norm.cdf(39.5, 45, np.sqrt(82.5))
assert abs(pex - pnorm) < 0.02
Sm = np.lib.stride_tricks.sliding_window_view(Dg[:200000], 10).sum(axis=1)
assert abs(np.mean((Sm >= 40) & (Sm <= 50)) - pex) < 0.005
report("sum_m", sm, ".0f"); report("sum_v", sv, ".1f"); report("sum_p", pex, ".4f"); report("sum_pn", pnorm, ".4f")
# ⟦chuỗi độ dài k||runs of length k⟧
side = Dg >= 5
change = np.flatnonzero(np.diff(side.astype(int)) != 0)
runs = np.diff(np.concatenate([[-1], change, [len(side) - 1]]))
for k, key in ((1, "run_1"), (2, "run_2"), (3, "run_3")):
    fr = np.mean(runs == k)
    assert abs(fr - 2.0**-k) < 0.005
    report(key, 2.0**-k, ".3f")
# ⟦hệ số bốn góc||the quadrant coefficient⟧
rho_ = 0.9
xy = rg.multivariate_normal([0, 0], [[1, rho_], [rho_, 1]], 400000)
mx, my = np.median(xy[:, 0]), np.median(xy[:, 1])
psi = (np.sum((xy[:, 0] > mx) == (xy[:, 1] > my)) - np.sum((xy[:, 0] > mx) != (xy[:, 1] > my)))/len(xy)
psi_th = 2/np.pi*np.arcsin(rho_)
assert abs(psi - psi_th) < 0.005 and abs(np.sin(np.pi/2*psi_th) - rho_) < 1e-12
report("psi_09", psi, ".3f"); report("psi_th", psi_th, ".3f")
# ⟦tự tương quan sau lọc: tổng chạy 10 và {5 3 1 1}||autocorrelation after filtering: ten-term sum and {5 3 1 1}⟧
def acf_filter(h, n=1000000):
    x = rg.standard_normal(n); y = np.convolve(x, h, "valid")
    return np.array([np.mean(y[k:]*y[:len(y) - k]) for k in range(1, 4)])/np.var(y)
def acf_theory(h):
    ac = np.correlate(h, h, "full"); c = len(h) - 1
    return ac[c + 1:c + 4]/ac[c] if len(h) > 3 else ac[c + 1:]/ac[c]
h10 = np.ones(10); a10 = acf_filter(h10); t10 = np.array([0.9, 0.8, 0.7])
assert np.max(np.abs(a10 - t10)) < 0.01 and np.max(np.abs(acf_theory(h10) - t10)) < 1e-12
hg = np.array([5.0, 3.0, 1.0, 1.0]); ag = acf_filter(hg); tg = acf_theory(hg)
assert np.max(np.abs(ag - tg)) < 0.01 and abs(tg[0] - 19/36) < 1e-12
report("ac_1", 0.9, ".1f"); report("ac_2", 0.8, ".1f")
report("g_1", tg[0], ".4f"); report("g_2", tg[1], ".4f"); report("g_3", tg[2], ".4f")
# ⟦phổ: |T|² tại f = 0.05||spectrum: |T|² at f = 0.05⟧
f = 0.05
th_ = (np.sin(10*np.pi*f)/np.sin(np.pi*f))**2
xw = rg.standard_normal(2000000); yw = np.convolve(xw, h10, "valid")
fr, Pw = signal.welch(yw, fs=1.0, nperseg=4096, return_onesided=False, scaling="density")
k05 = np.argmin(np.abs(fr - f))
assert abs(Pw[k05]/1.0 - th_)/th_ < 0.08 and abs(th_ - abs(np.sum(np.exp(-2j*np.pi*f*np.arange(10))))**2) < 1e-9
report("pt_th", th_, ".1f"); report("pt_mc", Pw[k05], ".1f")
# ⟦nhị thức và Gauss||binomial and Gaussian⟧
bn = np.array([1.0])
for _ in range(10): bn = np.convolve(bn, [1, 1])
assert list(bn.astype(int)) == [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
gs = 252*np.exp(-np.pi*(0.24*np.arange(6))**2)
assert list(np.round(gs).astype(int)) == [252, 210, 122, 49, 14, 3]
report("gs_2", gs[2], ".0f"); report("gs_3", gs[3], ".0f"); report("gs_4", gs[4], ".0f"); report("gs_5", gs[5], ".0f"); report("gs_pk", 1/0.24, ".2f")
# ⟦AR(2)||AR(2)⟧
a_, b_ = 1.84, -0.9
r_ = np.sqrt(-b_); om = np.arccos(a_/(2*r_)); f_th = om/(2*np.pi)
e_ = rg.uniform(-0.5, 0.5, 2000000)
y2 = signal.lfilter([1], [1, -a_, -b_], e_)
fw, Pa = signal.welch(y2, fs=1.0, nperseg=8192)
f_mc = fw[np.argmax(Pa)]
assert abs(f_mc - f_th) < 0.003
report("ar_r", r_, ".4f"); report("ar_f", f_th, ".4f"); report("ar_fmc", f_mc, ".3f")
# ⟦đường bao Rayleigh||the Rayleigh envelope⟧
z = signal.hilbert(y2[:1048576]); env = np.abs(z)
sig = np.std(y2[:1048576])
e_m = np.mean(env)/sig
ks = stats.kstest(env/sig, "rayleigh").statistic
assert abs(e_m - np.sqrt(np.pi/2)) < 0.01 and ks < 0.03
report("env_m", e_m, ".4f"); report("env_ks", ks, ".3f")
sqm = np.mean((env/sig)**2)/1.0/1.0
r2 = (env/sig)**2
assert abs(np.mean(r2) - 2) < 0.06 and abs(np.var(r2) - 4) < 0.5
report("sq_m", 2, ".0f"); report("sq_v", 4, ".0f")
assert abs(np.mean(env/sig > 1) - np.exp(-0.5)) < 0.01
report("ray_tail", np.exp(-0.5), ".4f")
# ⟦giới hạn 1/√(TΔf)||the 1/√(TΔf) limit⟧
fs, Bw, Tw = 1000.0, 50.0, 1.0
nfft = int(fs*200)
Wn = rg.standard_normal(nfft); Fw = np.fft.rfft(Wn); fq = np.fft.rfftfreq(nfft, 1/fs)
Fw[(fq < 175) | (fq > 225)] = 0
nb_ = np.fft.irfft(Fw, nfft)
sqd = nb_**2
means = sqd.reshape(200, int(fs*Tw)).mean(axis=1)
ratio = np.std(means)/np.mean(means)
th_r = 1/np.sqrt(Tw*Bw)
assert abs(ratio - th_r)/th_r < 0.2
report("tf_th", th_r, ".4f"); report("tf_mc", ratio, ".3f")
# ⟦quy tắc 1/5||the 1/5 rule⟧
r100 = np.mean(1/(np.ptp(rg.standard_normal((20000, 100)), axis=1)))
r1000 = np.mean(1/(np.ptp(rg.standard_normal((5000, 1000)), axis=1)))
assert 0.19 < r100 < 0.21 and 0.15 < r1000 < 0.17
report("pp_100", r100, ".3f"); report("pp_1000", r1000, ".3f")
# ⟦cắt lên||upcrossings⟧
xs = rg.standard_normal(600000); ys_ = np.convolve(xs, np.ones(10), "valid")
up_mc = np.mean((ys_[:-1] < 0) & (ys_[1:] > 0))
up_th = np.arccos(0.9)/(2*np.pi)
assert abs(up_mc - up_th) < 0.003
report("up_th", up_th, ".4f"); report("up_mc", up_mc, ".3f")'''),
        ("code", r'''fig, ax = plt.subplots(1, 2, figsize=(10, 3.2))
ax[0].plot(y2[:400], lw=0.8); ax[0].plot(env[:400], "r", lw=0.8); ax[0].set_title(("⟦nhiễu thông dải và đường bao||bandpass noise and envelope⟧"))
ax[1].semilogy(fw, Pa); ax[1].axvline(f_th, color="r", ls="--", lw=0.8); ax[1].set_xlim(0, 0.2); ax[1].set_title(("⟦phổ và cực||spectrum and pole⟧"))
plt.tight_layout(); plt.show()''', dict(fig="bandpass", cap="⟦Hình 1. Nhiễu thông dải từ y_t = 1.84 y_{t−1} − 0.9 y_{t−2} + ε_t: dao động ở tần số cực (trái, đường bao đỏ) và phổ có đỉnh ở đúng tần số góc của cực (phải).||Figure 1. Bandpass noise from y_t = 1.84 y_{t−1} − 0.9 y_{t−2} + ε_t: an oscillation at the pole frequency (left, envelope in red) and a spectrum peaked exactly at the pole's angular frequency (right).⟧")),
        ("code", r'''Tset = [0.25, 0.5, 1.0, 2.0, 4.0]
rat = []
for Tv in Tset:
    m_ = sqd[:int(fs*Tv)*int(len(sqd)//(fs*Tv))].reshape(-1, int(fs*Tv)).mean(axis=1)
    rat.append(np.std(m_)/np.mean(m_))
fig, ax = plt.subplots(figsize=(6.5, 3.3))
ax.loglog(Tset, rat, "o", label=("⟦mô phỏng||simulation⟧")); ax.loglog(Tset, [1/np.sqrt(t_*Bw) for t_ in Tset], "-", label=r"1/√(TΔf)")
ax.set_xlabel("T (s)"); ax.set_ylabel("rms / mean"); ax.legend(fontsize=8); plt.tight_layout(); plt.show()''', dict(fig="tdf", cap="⟦Hình 2. Dao động tương đối của công suất nhiễu đo được sau tách sóng bình phương giảm như 1/√(TΔf) khi thời gian tích lũy T tăng (Δf = 50 Hz).||Figure 2. The relative fluctuation of measured noise power after square-law detection falls like 1/√(TΔf) as the integration time T grows (Δf = 50 Hz).⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Chữ số: trung bình 32 chữ số đầu {{pi_mean}}, giới hạn {{dig_m}}, phương sai {{dig_var}}. Tổng 10: {{sum_m}}, {{sum_v}}, $P$ = {{sum_p}} so với chuẩn {{sum_pn}}. Chuỗi: {{run_1}}, {{run_2}}, {{run_3}}; $\\psi$ = {{psi_09}} so với {{psi_th}}. Tự tương quan: {{ac_1}}, {{ac_2}}; $\\{5\\,3\\,1\\,1\\}$: {{g_1}}, {{g_2}}, {{g_3}}. Phổ: {{pt_th}} và {{pt_mc}}. Gauss: {{gs_2}}, {{gs_3}}, {{gs_4}}, {{gs_5}}. AR(2): {{ar_r}}, {{ar_f}}, {{ar_fmc}}. Đường bao: {{env_m}}, {{env_ks}}; bình phương {{sq_m}}, {{sq_v}}. $1/\\sqrt{T\\Delta f}$: {{tf_th}} và {{tf_mc}}. Quy tắc 1/5: {{pp_100}} và {{pp_1000}}. Cắt lên: {{up_th}} và {{up_mc}}.||Digits: mean of the first 32 digits {{pi_mean}}, limit {{dig_m}}, variance {{dig_var}}. Sum of 10: {{sum_m}}, {{sum_v}}, $P$ = {{sum_p}} against normal {{sum_pn}}. Runs: {{run_1}}, {{run_2}}, {{run_3}}; $\\psi$ = {{psi_09}} against {{psi_th}}. Autocorrelation: {{ac_1}}, {{ac_2}}; $\\{5\\,3\\,1\\,1\\}$: {{g_1}}, {{g_2}}, {{g_3}}. Spectrum: {{pt_th}} and {{pt_mc}}. Gaussian: {{gs_2}}, {{gs_3}}, {{gs_4}}, {{gs_5}}. AR(2): {{ar_r}}, {{ar_f}}, {{ar_fmc}}. Envelope: {{env_m}}, {{env_ks}}; square {{sq_m}}, {{sq_v}}. $1/\\sqrt{T\\Delta f}$: {{tf_th}} and {{tf_mc}}. The 1/5 rule: {{pp_100}} and {{pp_1000}}. Upcrossings: {{up_th}} and {{up_mc}}.⟧"""),
        ("md", """## 4. ⟦Phổ công suất, hệ tuyến tính, ergodic, lấy mẫu, Hilbert||Power spectra, linear systems, ergodicity, sampling, Hilbert⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Wiener-Khinchin, đầu ra mạch RC dưới nhiễu trắng (ba cách), ergodic, lấy mẫu giới hạn băng, và tín hiệu giải tích có đúng như công thức?||Do Wiener-Khinchin, the RC output under white noise (three ways), ergodicity, band-limited sampling and analytic signals follow the formulas?⟧"""),
        ("code", r'''# ⟦Wiener-Khinchin: pha ngẫu nhiên: ∫S df = R(0)||Wiener-Khinchin: random phase: ∫S df = R(0)⟧
Ph = A**2/4*2
report("psd_tot", Ph, ".1f")
assert abs(Ph - A**2/2) < 1e-12
# ⟦RC, N0 = 2, α = 5: ba cách||RC, N0 = 2, α = 5: three ways⟧
alpha, N0 = 5.0, 2.0
Rf = lambda tau: N0*alpha/4*np.exp(-alpha*abs(tau))
# ⟦cách 1: tích chập h*h(−τ)||method 1: the convolution h*h(−τ)⟧
gconv = lambda tau: integrate.quad(lambda l: alpha*np.exp(-alpha*(l + tau))*alpha*np.exp(-alpha*l) if l + tau >= 0 else 0.0, max(0, -tau), 40)[0]
assert abs((N0/2)*gconv(0.1) - Rf(0.1)) < 1e-9 and abs((N0/2)*gconv(0.0) - Rf(0.0)) < 1e-9
# ⟦cách 2: phổ: ∫ (N0/2)|H|² e^{i2πfτ} df||method 2: the spectrum: ∫ (N0/2)|H|² e^{i2πfτ} df⟧
Sy = lambda ff: (N0/2)*alpha**2/(4*np.pi**2*ff**2 + alpha**2)
R_sp = 2*integrate.quad(Sy, 0, np.inf, weight='cos', wvar=2*np.pi*0.1)[0]
assert abs(R_sp - Rf(0.1)) < 1e-5
# ⟦cách 3: mô phỏng SDE chính xác||method 3: exact SDE simulation⟧
dt = 1e-3; Nn = 3000000; phi = np.exp(-alpha*dt); sg = alpha*np.sqrt((N0/2)*(1 - phi**2)/(2*alpha))
wnz = rg.standard_normal(Nn)
yrc = signal.lfilter([sg], [1, -phi], wnz)
lag = int(round(0.1/dt))
mc0 = np.mean(yrc**2); mc1 = np.mean(yrc[lag:]*yrc[:-lag])
assert abs(mc0 - Rf(0)) < 0.05 and abs(mc1 - Rf(0.1)) < 0.05
report("rc_r0", Rf(0), ".4f"); report("rc_r1", Rf(0.1), ".4f")
ym = signal.lfilter([1 - phi], [1, -phi], 3 + 0*wnz[:200000])
assert abs(ym[-1] - 3) < 1e-9
report("rc_m", 3, "d")
# ⟦ergodic||ergodicity⟧
tt = np.arange(0, 100, 0.01); xt = np.cos(2*np.pi*tt + 0.7)
assert abs(np.mean(xt)) < 0.01
report("er_t", np.mean(xt) if abs(np.mean(xt)) > 1e-3 else 0.0, ".2f")
Cs = rg.standard_normal(20000); avg_dc = Cs                          # ⟦trung bình thời gian của X = C chính là C||the time average of X = C is C itself⟧
avg_phase = np.array([np.mean(np.cos(2*np.pi*tt[:5000] + p_)) for p_ in rg.uniform(0, 2*np.pi, 2000)])
assert abs(np.var(avg_dc) - 1) < 0.03 and np.var(avg_phase) < 1e-4
report("er_v", np.var(avg_dc), ".1f")
# ⟦lấy mẫu giới hạn băng 5 Hz||sampling of a process band-limited to 5 Hz⟧
fs_hi = 100.0; Nz = 20000
Z = np.fft.rfft(rg.standard_normal(Nz)); fzq = np.fft.rfftfreq(Nz, 1/fs_hi); Z[fzq > 5] = 0
xbl = np.fft.irfft(Z, Nz); tz = np.arange(Nz)/fs_hi
def interp(fs_s):
    Ts = 1/fs_s; ns = np.arange(int(tz[-1]*fs_s))
    samp = np.interp(ns*Ts, tz, xbl)                 # ⟦mẫu lấy từ bản ghi dày (100 Hz)||samples from the dense record (100 Hz)⟧
    mid = (tz > 60) & (tz < 140)
    xr = np.array([np.sum(samp*np.sinc((t_ - ns*Ts)/Ts)) for t_ in tz[mid][::20]])
    return np.mean((xr - xbl[mid][::20])**2)/np.var(xbl)
e10 = interp(10.0); e6 = interp(6.0)
assert e10 < 0.05 and e6 > 3*e10
report("sm_ok", e10, ".4f"); report("sm_bad", e6, ".3f")
# ⟦Hilbert và tín hiệu giải tích||Hilbert and analytic signals⟧
xh0 = np.fft.rfft(rg.standard_normal(2**16)); xh0[0] = 0; xh0[-1] = 0; xh = np.fft.irfft(xh0, 2**16); zh = signal.hilbert(xh)
pa = np.mean(np.abs(zh)**2)/np.mean(xh**2)
xh_hat = zh.imag
hh = signal.hilbert(xh_hat).imag                       # ⟦Ĥ Ĥ x⟧
hh_dev = np.max(np.abs(hh + xh))
assert abs(pa - 2) < 1e-9 and hh_dev < 1e-9 and abs(np.mean(xh*xh_hat)) < 0.02
report("an_p", pa, ".0f"); report("hh_dev", max(hh_dev, 1e-16), ".0e")'''),
        ("code", r'''taus = np.linspace(-1.2, 1.2, 241)
fig, ax = plt.subplots(figsize=(6.8, 3.3))
ax.plot(taus, [Rf(t_) for t_ in taus], label=("⟦công thức||formula⟧"))
lags = np.arange(-1200, 1201, 20)
ax.plot(lags*dt, [np.mean(yrc[max(0, k):len(yrc) + min(0, k)]*yrc[max(0, -k):len(yrc) - max(0, k)]) for k in lags], "o", ms=3, label=("⟦mô phỏng||simulation⟧"))
ax.set_xlabel("τ (s)"); ax.legend(fontsize=8); plt.tight_layout(); plt.show()''', dict(fig="rc_acf", cap="⟦Hình 3. Tự tương quan của nhiễu trắng qua mạch RC: mô phỏng SDE (chấm) trùng công thức (N₀α/4)e^{−α|τ|} (đường).||Figure 3. The autocorrelation of white noise through an RC circuit: the SDE simulation (dots) matches the formula (N₀α/4)e^{−α|τ|} (line).⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Công suất phổ tổng {{psd_tot}}. Mạch RC: $R_{yy}(0)$ = {{rc_r0}}, $R_{yy}(0.1)$ = {{rc_r1}}, trung bình {{rc_m}}. Ergodic: {{er_t}} và phương sai {{er_v}}. Lấy mẫu: {{sm_ok}} (10 Hz) và {{sm_bad}} (6 Hz). Giải tích: {{an_p}}, $\\hat{\\hat x}+x$ lệch {{hh_dev}}.||Total spectral power {{psd_tot}}. RC circuit: $R_{yy}(0)$ = {{rc_r0}}, $R_{yy}(0.1)$ = {{rc_r1}}, mean {{rc_m}}. Ergodicity: {{er_t}} and variance {{er_v}}. Sampling: {{sm_ok}} (10 Hz) and {{sm_bad}} (6 Hz). Analytic: {{an_p}}, $\\hat{\\hat x}+x$ deviates by {{hh_dev}}.⟧"""),
        ("md", """## 5. ⟦Liên tục, đạo hàm và nhiễu nhiệt||Continuity, differentiation and thermal noise⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Liên tục và khả vi theo bình phương trung bình có ứng với $R(0)-R(\\varepsilon)$ và $-R''(0)$, và nhiễu nhiệt $2kTR$, $\\sqrt{4kTRB}$ khớp giữa công thức, tích phân phổ Lorentz và mô phỏng?||Do mean-square continuity and differentiability correspond to $R(0)-R(\\varepsilon)$ and $-R''(0)$, and do the thermal noise $2kTR$ and $\\sqrt{4kTRB}$ agree between formula, integral of the Lorentzian spectrum and simulation?⟧"""),
        ("code", r'''# ⟦liên tục: R = e^{−|τ|}||continuity: R = e^{−|τ|}⟧
eps = 0.01
mc = 2*(1 - np.exp(-eps))
Ne = rg.standard_normal(1000000); u = signal.lfilter([np.sqrt(1 - np.exp(-2*0.001))], [1, -np.exp(-0.001)], Ne)
lagk = int(round(eps/0.001)); mc_sim = np.mean((u[lagk:] - u[:-lagk])**2)
assert abs(mc_sim - mc) < 0.002
report("mc_01", mc, ".4f")
# ⟦đạo hàm: R = e^{−τ²/2}, −R''(0) = 1||derivative: R = e^{−τ²/2}, −R''(0) = 1⟧
h = 1e-4
Rg = lambda t: np.exp(-t*t/2)
d2 = (Rg(h) - 2*Rg(0) + Rg(-h))/h**2
assert abs(-d2 - 1) < 1e-6
# ⟦mô phỏng: quá trình có R = e^{−τ²/2} qua bộ lọc Gauss trong miền tần số; đạo hàm bằng sai phân||simulation: a process with R = e^{−τ²/2} through a Gaussian filter in frequency; derivative by differences⟧
Nq = 2**18; dtq = 0.05
Fq = np.fft.rfft(rg.standard_normal(Nq)); fq2 = np.fft.rfftfreq(Nq, dtq)
Sg = np.exp(-(2*np.pi*fq2)**2/2)                      # ⟦S(ω) ∝ e^{−ω²/2} ứng với R = e^{−τ²/2}||S(ω) ∝ e^{−ω²/2} corresponds to R = e^{−τ²/2}⟧
xq = np.fft.irfft(Fq*np.sqrt(Sg), Nq)
xq = xq/np.std(xq)
dx = np.diff(xq)/dtq
dv = np.var(dx)
assert abs(dv - 1) < 0.05
report("dv_0", 1.0, ".0f")
# ⟦nhiễu nhiệt||thermal noise⟧
kB, Tk, Rr = 1.38e-23, 290.0, 1e3
S0 = 2*kB*Tk*Rr
alpha_t = 1e14
Sf = lambda ff: S0*alpha_t**2/(alpha_t**2 + (2*np.pi*ff)**2)
flat = 1 - Sf(1e9)/S0
assert flat < 1e-8
report("th_S", S0, ".2e"); report("th_flat", flat, ".1e")
B = 1e6
v_form = np.sqrt(4*kB*Tk*Rr*B)
v_int = np.sqrt(integrate.quad(Sf, -B, B, epsabs=0, epsrel=1e-10)[0])
assert abs(v_int - v_form)/v_form < 1e-6
report("th_v", v_form, ".2e")
report("th_prec", 1/np.sqrt(1.0*B), ".1e")
# ⟦hai điện trở nối tiếp: mô phỏng công suất||two resistors in series: power simulation⟧
R2 = 4e3
v1 = np.sqrt(4*kB*Tk*Rr*B); v2 = np.sqrt(4*kB*Tk*R2*B)
vt = np.sqrt(v1**2 + v2**2)
n1 = v1*rg.standard_normal(1000000); n2 = v2*rg.standard_normal(1000000)
assert abs(np.std(n1 + n2)/vt - 1) < 0.003 and vt < v1 + v2
report("th_v2", vt, ".2e"); report("th_vsum", v1 + v2, ".2e")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Liên tục: $E[|X(t+\\varepsilon)-X(t)|^2]$ = {{mc_01}} tại $\\varepsilon=0.01$. Đạo hàm: $R_{x'x'}(0)$ = {{dv_0}}. Nhiễu nhiệt: $2kTR$ = {{th_S}}, lệch khỏi phẳng ở 1 GHz {{th_flat}}, $v_{rms}$ = {{th_v}} V, độ chính xác $1/\\sqrt{TB}$ = {{th_prec}}; nối tiếp 1 kΩ và 4 kΩ: {{th_v2}} V so với tổng biên độ {{th_vsum}} V.||Continuity: $E[|X(t+\\varepsilon)-X(t)|^2]$ = {{mc_01}} at $\\varepsilon=0.01$. Derivative: $R_{x'x'}(0)$ = {{dv_0}}. Thermal noise: $2kTR$ = {{th_S}}, deviation from flat at 1 GHz {{th_flat}}, $v_{rms}$ = {{th_v}} V, precision $1/\\sqrt{TB}$ = {{th_prec}}; 1 kΩ and 4 kΩ in series: {{th_v2}} V against the sum of amplitudes {{th_vsum}} V.⟧"""),
    ],
)
