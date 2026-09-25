from lib import F, C, UL, OL, TBL

MOD = dict(
    n=11, slug="distributions", part="B", book="K",
    title="⟦Các phân bố xác suất thường gặp||The distributions that arise in practice⟧",
    blurb="⟦Bernoulli, nhị thức, hình học, Pascal, siêu bội, Poisson, đều, chuẩn, mũ, gamma, beta, chi bình phương, Rayleigh, Rice, Maxwell, Nakagami, Student, Cauchy, Gauss nhiều chiều, Weibull, log-chuẩn và K.||"
          "Bernoulli, binomial, geometric, Pascal, hypergeometric, Poisson, uniform, normal, exponential, gamma, beta, chi-square, Rayleigh, Rice, Maxwell, Nakagami, Student, Cauchy, multivariate Gaussian, Weibull, log-normal and K.⟧",
    src="⟦Barkat, chương 2, tr. 75–139||Barkat, chapter 2, pp. 75–139⟧",
    data="⟦Sinh bằng mã: dãy thử Bernoulli, bình bóng, biến chuẩn, tích của Rayleigh và gamma (K)||Generated in code: Bernoulli trials, urns, normal variables, a Rayleigh-times-gamma product (K)⟧",
    objectives=[
        "⟦Nhận biết phân bố nào mô hình hóa tình huống nào: đếm thành công, thời gian chờ, tổng nhiều nhiễu, biên độ tín hiệu, suy hao đa đường.||Recognise which distribution models which situation: counting successes, waiting times, sums of many noises, signal amplitudes, multipath fading.⟧",
        "⟦Tính trung bình, phương sai, hàm đặc trưng của mỗi phân bố và kiểm bằng hai cách.||Compute the mean, variance and characteristic function of each distribution and check them two ways.⟧",
        "⟦Dùng hàm sai số và hàm $Q$ để tính xác suất chuẩn; dùng giới hạn trung tâm cho nhị thức và Poisson.||Use the error function and the $Q$ function for normal probabilities; use the central limit for binomial and Poisson.⟧",
        "⟦Dựng chuỗi liên hệ: Gauss → chi bình phương → Rayleigh, Rice, Maxwell; Rayleigh ≡ Weibull $b=2$; gamma × Rayleigh → K.||Build the chain of relations: Gaussian → chi-square → Rayleigh, Rice, Maxwell; Rayleigh ≡ Weibull $b=2$; gamma × Rayleigh → K.⟧",
        "⟦Làm việc với Gauss hai chiều: điều kiện, elip chuẩn, độc lập bằng không tương quan.||Work with the bivariate Gaussian: conditionals, the standard ellipse, independence from uncorrelatedness.⟧",
    ],
    parts=[
        # ---------------------------------------------------------------- PART 1
        dict(
            title="⟦Phân bố rời rạc||Discrete distributions⟧",
            scr=("⟦Đếm số thành công, số lần thử tới thành công đầu tiên, số bóng trắng rút ra, số biến cố trong một khoảng thời gian là những bài toán rất khác nhau.||Counting successes, trials to the first success, white balls drawn, or events in a time interval are quite different problems.⟧",
                 "⟦Mỗi bài toán ứng với một phân bố có tên và công thức trung bình, phương sai riêng.||Each problem has a named distribution with its own mean and variance.⟧",
                 "⟦Bernoulli sinh ra nhị thức, hình học, Pascal; siêu bội là lấy mẫu không hoàn lại; Poisson là giới hạn của nhị thức.||Bernoulli generates the binomial, geometric and Pascal; the hypergeometric is sampling without replacement; Poisson is the limit of the binomial.⟧"),
            preview=["⟦Bernoulli, nhị thức, đa thức||Bernoulli, binomial, multinomial⟧", "⟦Hình học, Pascal, siêu bội||Geometric, Pascal, hypergeometric⟧", "⟦Poisson và giới hạn của nhị thức||Poisson and the limit of the binomial⟧"],
            slides=[
                ("⟦Bản đồ chương||A map of the chapter⟧",
                 "<p>⟦Chương 1 định nghĩa xác suất, biến ngẫu nhiên và mômen; chương 2 nghiên cứu các phân bố hay gặp trong các ứng dụng như radar và truyền thông, ở dạng tổng quát, kèm vài chi tiết cho ứng dụng cụ thể (Barkat, mục 2.1, tr. 75). Mục 2.2 nói về phân bố rời rạc, mục 2.3 về liên tục, mục 2.4 về các phân bố đặc biệt: nhiều chiều, Weibull, log-chuẩn, K và hợp thành tổng quát.||Chapter 1 defined probability, random variables and moments; chapter 2 studies the distributions frequently encountered in applications such as radar and communications, in general form with some detail for particular applications (Barkat, section 2.1, p. 75). Section 2.2 covers discrete distributions, 2.3 continuous ones, and 2.4 special distributions: multivariate, Weibull, log-normal, K and the generalised compound.⟧</p>"),
                ("⟦Bernoulli và nhị thức||Bernoulli and binomial⟧",
                 "<p>⟦Phép thử Bernoulli có hai kết cục: thành công (1) với xác suất $p$, thất bại (0) với $q=1-p$. Xác suất đúng $k$ thành công trong $n$ phép thử độc lập là nhị thức $\\binom nk p^kq^{n-k}$; trung bình $np$, phương sai $npq$, hàm đặc trưng $(pe^{j\\omega}+q)^n$ (Barkat, mục 2.2.1, tr. 75 đến 77). Ví dụ 2.1: gieo xúc xắc 10 lần, được mặt 6 đúng hai lần: {{bi_ex21}}. Số đo: $E$ = {{bi_mean}} và phương sai {{bi_var}}.||A Bernoulli trial has two outcomes: success (1) with probability $p$, failure (0) with $q=1-p$. The probability of exactly $k$ successes in $n$ independent trials is the binomial $\\binom nk p^kq^{n-k}$; mean $np$, variance $npq$, characteristic function $(pe^{j\\omega}+q)^n$ (Barkat, section 2.2.1, pp. 75 to 77). Example 2.1: rolling a die 10 times, a six exactly twice: {{bi_ex21}}. Measured: $E$ = {{bi_mean}} and variance {{bi_var}}.⟧</p>"
                 + F("⟦Nhị thức||Binomial⟧", r"P(X=k)=\binom nk p^kq^{n-k},\quad E[X]=np,\quad \operatorname{var}X=npq")),
                ("⟦Ví dụ 2.2: quyết định theo đa số||Example 2.2: a majority decision⟧",
                 "<p>⟦Máy thu nhận ba ký hiệu và quyết định theo đa số; mỗi quyết định đúng với xác suất 0.8. Xác suất quyết định đúng là $P(D=2)+P(D=3)=3(0.8)^2(0.2)+(0.8)^3$ = {{bi_ex22}} (tr. 77 đến 78). Số đo bằng công thức nhị thức, bằng hàm khối và bằng mô phỏng cùng cho kết quả ấy. Đây là ví dụ đầu tiên cho thấy xử lý nhiều quan sát cải thiện độ tin cậy, ý tưởng cốt lõi của phát hiện tín hiệu.||The receiver takes three symbols and decides by majority; each decision is correct with probability 0.8. The probability of a correct decision is $P(D=2)+P(D=3)=3(0.8)^2(0.2)+(0.8)^3$ = {{bi_ex22}} (pp. 77 to 78). The binomial formula, the mass function and simulation agree. This is the first example of how processing several observations improves reliability, the core idea of signal detection.⟧</p>"),
                ("⟦Đa thức||The multinomial distribution⟧",
                 "<p>⟦Nếu mỗi phép thử có $k$ kết cục loại trừ với xác suất $P_1,\\ldots,P_k$ thì xác suất có $n_i$ lần kết cục $i$ là $\\dfrac{n!}{n_1!\\cdots n_k!}P_1^{n_1}\\cdots P_k^{n_k}$ (tr. 78). Các $X_i$ không độc lập vì $\\sum n_i=n$. Số đo: $n=10$, xác suất $(0.2,0.3,0.5)$, số lần $(2,3,5)$: {{mn_p}}.||If each trial has $k$ exclusive outcomes with probabilities $P_1,\\ldots,P_k$ the probability of $n_i$ occurrences of outcome $i$ is $\\dfrac{n!}{n_1!\\cdots n_k!}P_1^{n_1}\\cdots P_k^{n_k}$ (p. 78). The $X_i$ are not independent since $\\sum n_i=n$. Measured: $n=10$, probabilities $(0.2,0.3,0.5)$, counts $(2,3,5)$: {{mn_p}}.⟧</p>"),
                ("⟦Hình học và Pascal||Geometric and Pascal⟧",
                 "<p>⟦Nếu thử đến khi biến cố $A$ xuất hiện lần đầu ở phép thử thứ $k$: hình học $P(X=k)=q^{k-1}p$, $E[X]=1/p$, $\\operatorname{var}=q/p^2$, hàm sinh mômen $p/(1-qe^t)$ (Barkat, mục 2.2.2, tr. 78 đến 80). Dừng ở lần thứ $r$: Pascal (nhị thức âm) $P(X=k)=\\binom{k-1}{r-1}p^rq^{k-r}$ (tr. 80 đến 82), $E=r/p$, $\\operatorname{var}=rq/p^2$; $r=1$ cho hình học. Số đo: xúc xắc, mặt 6 đầu tiên ở lần thứ 3: {{ge_p3}}; $E$ = {{ge_mean}} và phương sai {{ge_var}}; Pascal $r=3$, $p=0.5$, $k=5$: {{pa_p}}.||If we repeat until an event $A$ first occurs at trial $k$: geometric $P(X=k)=q^{k-1}p$, $E[X]=1/p$, $\\operatorname{var}=q/p^2$, moment generating function $p/(1-qe^t)$ (Barkat, section 2.2.2, pp. 78 to 80). Stopping at the $r$th occurrence: Pascal (negative binomial) $P(X=k)=\\binom{k-1}{r-1}p^rq^{k-r}$ (pp. 80 to 82), $E=r/p$, $\\operatorname{var}=rq/p^2$; $r=1$ gives the geometric. Measured: die, first six at the third roll: {{ge_p3}}; $E$ = {{ge_mean}} and variance {{ge_var}}; Pascal $r=3$, $p=0.5$, $k=5$: {{pa_p}}.⟧</p>"),
                ("⟦Liên hệ nhị thức và Pascal||Binomial versus Pascal⟧",
                 "<p>⟦Nếu $X$ là nhị thức (số thành công trong $n$ thử) và $Y$ là Pascal (số thử để có $r$ thành công) thì $P(X\\ge r)=P(Y\\le n)$: có ít nhất $r$ thành công trong $n$ thử đầu khi và chỉ khi cần nhiều nhất $n$ thử để có $r$ thành công; tương tự $P(X<r)=P(Y>n)$ (tr. 82). Số đo với $n=10$, $r=3$, $p=0.3$: {{pa_rel}} bằng cả hai vế.||If $X$ is binomial (successes in $n$ trials) and $Y$ Pascal (trials to get $r$ successes) then $P(X\\ge r)=P(Y\\le n)$: at least $r$ successes in the first $n$ trials if and only if at most $n$ trials are needed for $r$ successes; likewise $P(X<r)=P(Y>n)$ (p. 82). Measured with $n=10$, $r=3$, $p=0.3$: {{pa_rel}} on both sides.⟧</p>"),
                ("⟦Siêu bội: lấy mẫu không hoàn lại||Hypergeometric: sampling without replacement⟧",
                 "<p>⟦Bình có $N$ bóng, $r$ trắng. Rút $n$ bóng có hoàn lại thì số bóng trắng là nhị thức. Không hoàn lại thì $P(X=k)=\\binom rk\\binom{N-r}{n-k}/\\binom Nn$, $k\\le\\min(n,r)$, trung bình $nr/N=np$ và phương sai $npq\\,\\dfrac{N-n}{N-1}$ (Barkat, mục 2.2.3, tr. 82 đến 84). Ví dụ 2.3: 5 trắng, 3 đen, 3 đỏ, được đúng 3 trắng sau 7 lần rút không hoàn lại: {{hy_p}} $=5/11$; phương sai {{hy_var}}. Khi $N\\to\\infty$ tiến về nhị thức: với $N=10000$, $r=3000$, $n=10$, $k=3$ lệch giữa hai phân bố chỉ {{hy_dev}}.||An urn has $N$ balls, $r$ white. Drawing $n$ with replacement gives a binomial count of whites. Without replacement, $P(X=k)=\\binom rk\\binom{N-r}{n-k}/\\binom Nn$, $k\\le\\min(n,r)$, mean $nr/N=np$ and variance $npq\\,\\dfrac{N-n}{N-1}$ (Barkat, section 2.2.3, pp. 82 to 84). Example 2.3: 5 white, 3 black, 3 red, exactly 3 whites after 7 draws without replacement: {{hy_p}} $=5/11$; variance {{hy_var}}. As $N\\to\\infty$ it tends to the binomial: with $N=10000$, $r=3000$, $n=10$, $k=3$ the two distributions differ by only {{hy_dev}}.⟧</p>"),
                ("⟦Poisson||The Poisson distribution⟧",
                 "<p>⟦Số biến cố trong khoảng thời gian $t$, khi các khoảng độc lập và xác suất không phụ thuộc chỗ bắt đầu: $P(X=k)=e^{-\\lambda}\\lambda^k/k!$ (Barkat, mục 2.2.4, tr. 85 đến 86). Ví dụ: lưu lượng điện thoại, hỏng thiết bị, phân rã phóng xạ. Trung bình và phương sai đều bằng $\\lambda$, $E[X^2]=\\lambda^2+\\lambda$, hàm đặc trưng $\\exp[\\lambda(e^{j\\omega}-1)]$. Số đo với $\\lambda=3$: $E[X^2]$ = {{po_ms}}. Ví dụ 2.4: tổng hai Poisson độc lập là Poisson với $\\lambda_1+\\lambda_2$; tại 5 với $\\lambda=2,3$ ta được {{po_add}} bằng $P(5)$ của Poisson tham số 5.||The number of events in a period $t$, when intervals are independent and the probability does not depend on the starting point: $P(X=k)=e^{-\\lambda}\\lambda^k/k!$ (Barkat, section 2.2.4, pp. 85 to 86). Examples: telephone traffic, equipment failures, radioactive decay. Mean and variance both equal $\\lambda$, $E[X^2]=\\lambda^2+\\lambda$, characteristic function $\\exp[\\lambda(e^{j\\omega}-1)]$. Measured with $\\lambda=3$: $E[X^2]$ = {{po_ms}}. Example 2.4: the sum of two independent Poissons is Poisson with $\\lambda_1+\\lambda_2$; at 5 with $\\lambda=2,3$ we get {{po_add}}, equal to $P(5)$ of the Poisson with parameter 5.⟧</p>"),
                ("⟦Poisson là giới hạn của nhị thức||Poisson as the limit of the binomial⟧",
                 "<p>⟦Khi $n\\to\\infty$, $p=\\lambda/n$ nhỏ: $\\binom nk p^k(1-p)^{n-k}\\to e^{-\\lambda}\\lambda^k/k!$, dùng $(1-\\lambda/n)^n\\to e^{-\\lambda}$ và $n(n-1)\\cdots(n-k+1)/n^k\\to1$ (tr. 87 đến 88). Siêu bội tiến về nhị thức rồi Poisson. Số đo: $n=1000$, $p=0.003$, $k=2$: nhị thức {{po_bin}}, Poisson $\\lambda=3$ {{po_pois}}; lệch {{po_dev}}.||When $n\\to\\infty$ with $p=\\lambda/n$ small: $\\binom nk p^k(1-p)^{n-k}\\to e^{-\\lambda}\\lambda^k/k!$, using $(1-\\lambda/n)^n\\to e^{-\\lambda}$ and $n(n-1)\\cdots(n-k+1)/n^k\\to1$ (pp. 87 to 88). The hypergeometric tends to the binomial and then to the Poisson. Measured: $n=1000$, $p=0.003$, $k=2$: binomial {{po_bin}}, Poisson $\\lambda=3$ {{po_pois}}; difference {{po_dev}}.⟧</p>"),
                ("⟦Tự kiểm tra phần 1||Self-check, part 1⟧",
                 UL(["⟦Khác nhau giữa nhị thức và Pascal?||What is the difference between binomial and Pascal?⟧",
                     "⟦Khi nào siêu bội gần nhị thức?||When is the hypergeometric close to the binomial?⟧",
                     "⟦Vì sao Poisson có trung bình bằng phương sai?||Why does the Poisson have mean equal to variance?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: nhị thức cố định $n$, Pascal cố định $r$; khi $N\\gg n$; vì là giới hạn $np$ và $npq$ với $q\\to1$.||Hints: the binomial fixes $n$, the Pascal fixes $r$; when $N\\gg n$; because it is the limit of $np$ and $npq$ with $q\\to1$.⟧</p>"),
            ]),
        # ---------------------------------------------------------------- PART 2
        dict(
            title="⟦Phân bố liên tục cơ bản: đều, chuẩn, mũ, gamma, beta||Basic continuous distributions: uniform, normal, exponential, gamma, beta⟧",
            scr=("⟦Phân bố chuẩn là quan trọng nhất, nhưng có nhiều ứng dụng mà nó không thích hợp.||The normal distribution is the most important, but many applications need others.⟧",
                 "⟦Ta cần công cụ tính xác suất chuẩn (hàm sai số, $Q$), và một số phân bố không âm cho thời gian chờ và độ lớn.||We need tools for normal probabilities (error function, $Q$) and some nonnegative distributions for waiting times and magnitudes.⟧",
                 "⟦Đều, chuẩn, mũ, Laplace, gamma, beta cùng công thức trung bình, phương sai và hàm đặc trưng.||Uniform, normal, exponential, Laplace, gamma and beta with their means, variances and characteristic functions.⟧"),
            preview=["⟦Đều và chuẩn: hàm sai số, $Q$||Uniform and normal: error function, $Q$⟧", "⟦Giới hạn trung tâm cho nhị thức và Poisson||The central limit for binomial and Poisson⟧", "⟦Mũ, Laplace, gamma, beta||Exponential, Laplace, gamma, beta⟧"],
            slides=[
                ("⟦Phân bố đều||The uniform distribution⟧",
                 "<p>⟦$f_X=\\frac1{b-a}$ trên $[a,b]$; $F_X=(x-a)/(b-a)$; trung bình $\\tfrac12(a+b)$, phương sai $\\tfrac1{12}(b-a)^2$, hàm đặc trưng $(e^{j\\omega b}-e^{j\\omega a})/[j\\omega(b-a)]$ (Barkat, mục 2.3.1, tr. 88 đến 89). Với $[2,8]$: phương sai {{un_var}}, kiểm bằng tích phân số. Hàm đặc trưng là một sinc dịch pha: dạng quen của Bracewell.||$f_X=\\frac1{b-a}$ on $[a,b]$; $F_X=(x-a)/(b-a)$; mean $\\tfrac12(a+b)$, variance $\\tfrac1{12}(b-a)^2$, characteristic function $(e^{j\\omega b}-e^{j\\omega a})/[j\\omega(b-a)]$ (Barkat, section 2.3.1, pp. 88 to 89). For $[2,8]$: variance {{un_var}}, checked by numerical integration. The characteristic function is a phase-shifted sinc: Bracewell's familiar form.⟧</p>"),
                ("⟦Phân bố chuẩn||The normal distribution⟧",
                 "<p>⟦$f_X=\\dfrac1{\\sqrt{2\\pi}\\sigma}\\exp\\!\\left[-\\dfrac{(x-m)^2}{2\\sigma^2}\\right]$; hàm đặc trưng $\\exp(jm\\omega-\\sigma^2\\omega^2/2)$; mômen bậc chẵn của biến trung bình 0 là $n!\\sigma^n/[(n/2)!2^{n/2}]$, bậc lẻ bằng 0 (Barkat, mục 2.3.2, tr. 89 đến 93). Chuẩn tắc $N(0,1)$: $E[X^4]$ = {{n_m4}} $=3$. Đỉnh của mật độ $1/(\\sqrt{2\\pi}\\sigma)$, và tại $m\\pm\\sigma$ mật độ còn $0.607$ lần đỉnh (hình 2.3).||$f_X=\\dfrac1{\\sqrt{2\\pi}\\sigma}\\exp\\!\\left[-\\dfrac{(x-m)^2}{2\\sigma^2}\\right]$; characteristic function $\\exp(jm\\omega-\\sigma^2\\omega^2/2)$; the even moments of a zero-mean variable are $n!\\sigma^n/[(n/2)!2^{n/2}]$, the odd ones vanish (Barkat, section 2.3.2, pp. 89 to 93). Standard $N(0,1)$: $E[X^4]$ = {{n_m4}} $=3$. The peak of the density is $1/(\\sqrt{2\\pi}\\sigma)$, and at $m\\pm\\sigma$ the density is $0.607$ of the peak (Fig. 2.3).⟧</p>"),
                ("⟦Hàm sai số và hàm $Q$||The error function and the $Q$ function⟧",
                 "<p>⟦$\\text{erf}(x)=\\frac2{\\sqrt\\pi}\\int_0^xe^{-u^2}du$; $F_X(x)=\\tfrac12+\\tfrac12\\text{erf}\\!\\left(\\frac{x-m}{\\sqrt2\\sigma}\\right)$; $Q(x)=\\frac1{\\sqrt{2\\pi}}\\int_x^\\infty e^{-u^2/2}du=\\tfrac12\\text{erfc}(x/\\sqrt2)$; $Q(0)=\\tfrac12$, $Q(-x)=1-Q(x)$, và $Q(x)\\approx\\frac1{x\\sqrt{2\\pi}}e^{-x^2/2}$ với $x>4$ (tr. 91 đến 92). Ví dụ 2.5: $Y\\sim N(3,4)$: $P(Y>4)$ = {{n_ex25}}; $P(2<Y<5)$ = {{n_ex25b}}. Tại $x=4$: $Q(4)$ = {{n_q4}} còn xấp xỉ cho {{n_q4a}}.||$\\text{erf}(x)=\\frac2{\\sqrt\\pi}\\int_0^xe^{-u^2}du$; $F_X(x)=\\tfrac12+\\tfrac12\\text{erf}\\!\\left(\\frac{x-m}{\\sqrt2\\sigma}\\right)$; $Q(x)=\\frac1{\\sqrt{2\\pi}}\\int_x^\\infty e^{-u^2/2}du=\\tfrac12\\text{erfc}(x/\\sqrt2)$; $Q(0)=\\tfrac12$, $Q(-x)=1-Q(x)$, and $Q(x)\\approx\\frac1{x\\sqrt{2\\pi}}e^{-x^2/2}$ for $x>4$ (pp. 91 to 92). Example 2.5: $Y\\sim N(3,4)$: $P(Y>4)$ = {{n_ex25}}; $P(2<Y<5)$ = {{n_ex25b}}. At $x=4$: $Q(4)$ = {{n_q4}} while the approximation gives {{n_q4a}}.⟧</p>"
                 + F("⟦Xác suất chuẩn||Normal probability⟧", r"P(a\le Y\le b)=\Phi\!\left(\frac{b-m}{\sigma}\right)-\Phi\!\left(\frac{a-m}{\sigma}\right),\qquad Q(x)=\tfrac12\operatorname{erfc}\!\left(\frac{x}{\sqrt2}\right)")),
                ("⟦Giới hạn trung tâm||The central limit theorem⟧",
                 "<p>⟦Với $X_1,X_2,\\ldots$ độc lập cùng phân bố, tổng $S_n$ có mật độ là tích chập $f_{X_1}*\\cdots*f_{X_n}$ tiến tới chuẩn với trung bình $\\sum m_k$ và phương sai $\\sum\\sigma_k^2$; chuẩn hóa $\\sum(X_k-m_k)/\\sigma$ tiến tới $N(0,1)$ (Barkat, tr. 95). Đúng cho mọi phân bố, ở đây xét nhị thức, $U=(X-np)/\\sqrt{npq}$, và Poisson, $(X-\\lambda)/\\sqrt\\lambda$ (tr. 95 đến 96). Đó là kết quả của Bracewell (module 8 và 10) với ngôn ngữ xác suất.||For i.i.d. $X_1,X_2,\\ldots$ the sum $S_n$ has density equal to the convolution $f_{X_1}*\\cdots*f_{X_n}$ tending to a normal with mean $\\sum m_k$ and variance $\\sum\\sigma_k^2$; the normalised $\\sum(X_k-m_k)/\\sigma$ tends to $N(0,1)$ (Barkat, p. 95). It holds for all distributions; here binomial, $U=(X-np)/\\sqrt{npq}$, and Poisson, $(X-\\lambda)/\\sqrt\\lambda$ (pp. 95 to 96). This is Bracewell's result (modules 8 and 10) in probability language.⟧</p>"),
                ("⟦Bài 2.11 và 2.12: giới hạn trung tâm thực hành||Problems 2.11 and 2.12: the central limit in practice⟧",
                 "<p>⟦Bài 2.11 (tr. 138): gieo hai xúc xắc 200 lần, thành công là tổng bằng 7 ($p=1/6$); xác suất thành công ít nhất 20 phần trăm số lần (từ 40): chính xác {{c211_ex}}, xấp xỉ chuẩn (có hiệu chỉnh liên tục) {{c211_n}}. Bài 2.12: tổng 100 biến Poisson $\\lambda=0.032$ là Poisson $\\lambda=3.2$; $P(S>5)$ chính xác {{c212_ex}}, xấp xỉ chuẩn (có hiệu chỉnh) {{c212_n}}: xấp xỉ khá với nhị thức nhưng kém hơn khi $\\lambda$ nhỏ.||Problem 2.11 (p. 138): throw two dice 200 times, success is a sum of 7 ($p=1/6$); the probability of success at least 20 percent of the time (from 40): exact {{c211_ex}}, normal approximation (with continuity correction) {{c211_n}}. Problem 2.12: the sum of 100 Poisson variables with $\\lambda=0.032$ is Poisson with $\\lambda=3.2$; $P(S>5)$ exact {{c212_ex}}, normal approximation (with correction) {{c212_n}}: fair for the binomial but worse when $\\lambda$ is small.⟧</p>"),
                ("⟦Mũ và Laplace||The exponential and Laplace distributions⟧",
                 "<p>⟦Mũ: $f_X=\\alpha e^{-\\alpha x}$, $x\\ge0$; trung bình $\\beta=1/\\alpha$, phương sai $\\beta^2$, hàm đặc trưng $(1-j\\beta\\omega)^{-1}$ (Barkat, mục 2.3.3, tr. 96 đến 97). Tính chất không nhớ (bài 2.7): $P(X\\ge x_1+x_2\\mid X>x_1)=P(X\\ge x_2)$: với $\\alpha=2$, $x_1=0.5$, $x_2=0.7$ cả hai vế bằng {{ex_mem}}. Laplace: $f_X=\\frac\\alpha2e^{-\\alpha|x|}$, hàm đặc trưng $e^{-jm\\omega}/(1+\\lambda^2\\omega^2)$, phương sai {{la_var}} khi $\\alpha=1$ (tr. 97 đến 98). Đây là các phân bố của module 10 (Bracewell).||Exponential: $f_X=\\alpha e^{-\\alpha x}$, $x\\ge0$; mean $\\beta=1/\\alpha$, variance $\\beta^2$, characteristic function $(1-j\\beta\\omega)^{-1}$ (Barkat, section 2.3.3, pp. 96 to 97). The memoryless property (problem 2.7): $P(X\\ge x_1+x_2\\mid X>x_1)=P(X\\ge x_2)$: with $\\alpha=2$, $x_1=0.5$, $x_2=0.7$ both sides equal {{ex_mem}}. Laplace: $f_X=\\frac\\alpha2e^{-\\alpha|x|}$, characteristic function $e^{-jm\\omega}/(1+\\lambda^2\\omega^2)$, variance {{la_var}} for $\\alpha=1$ (pp. 97 to 98). These are the distributions of module 10 (Bracewell).⟧</p>"),
                ("⟦Gamma||The gamma distribution⟧",
                 "<p>⟦Hàm gamma $\\Gamma(\\alpha)=\\int_0^\\infty x^{\\alpha-1}e^{-x}dx=(\\alpha-1)\\Gamma(\\alpha-1)$, $\\Gamma(n)=(n-1)!$, $\\Gamma(\\tfrac12)=\\sqrt\\pi$ = {{ga_half}}. Phân bố gamma $G(\\alpha,\\beta)$: $f_X=\\dfrac{x^{\\alpha-1}e^{-x/\\beta}}{\\Gamma(\\alpha)\\beta^\\alpha}$; trung bình $\\alpha\\beta$, phương sai $\\alpha\\beta^2$, hàm đặc trưng $(1-j\\beta\\omega)^{-\\alpha}$ (Barkat, mục 2.3.4, tr. 98 đến 100). Với $\\alpha=3$, $\\beta=2$: trung bình {{ga_mean}}, phương sai {{ga_var}}. Đó là Pearson III của Bracewell: tổng $\\alpha$ biến mũ.||The gamma function $\\Gamma(\\alpha)=\\int_0^\\infty x^{\\alpha-1}e^{-x}dx=(\\alpha-1)\\Gamma(\\alpha-1)$, $\\Gamma(n)=(n-1)!$, $\\Gamma(\\tfrac12)=\\sqrt\\pi$ = {{ga_half}}. The gamma distribution $G(\\alpha,\\beta)$: $f_X=\\dfrac{x^{\\alpha-1}e^{-x/\\beta}}{\\Gamma(\\alpha)\\beta^\\alpha}$; mean $\\alpha\\beta$, variance $\\alpha\\beta^2$, characteristic function $(1-j\\beta\\omega)^{-\\alpha}$ (Barkat, section 2.3.4, pp. 98 to 100). With $\\alpha=3$, $\\beta=2$: mean {{ga_mean}}, variance {{ga_var}}. This is Bracewell's Pearson III: the sum of $\\alpha$ exponential variables.⟧</p>"),
                ("⟦Beta||The beta distribution⟧",
                 "<p>⟦Hàm beta $B(\\alpha,\\beta)=\\int_0^1u^{\\alpha-1}(1-u)^{\\beta-1}du=\\Gamma(\\alpha)\\Gamma(\\beta)/\\Gamma(\\alpha+\\beta)$ (Barkat, tr. 100). Phân bố beta trên $(0,1)$: $f_X=x^{\\alpha-1}(1-x)^{\\beta-1}/B(\\alpha,\\beta)$, trung bình $\\alpha/(\\alpha+\\beta)$, phương sai $\\alpha\\beta/[(\\alpha+\\beta)^2(\\alpha+\\beta+1)]$ (tr. 100 đến 101). Với $\\alpha=2$, $\\beta=5$: trung bình {{be_mean}}, phương sai {{be_var}}, kiểm bằng tích phân và mô phỏng.||The beta function $B(\\alpha,\\beta)=\\int_0^1u^{\\alpha-1}(1-u)^{\\beta-1}du=\\Gamma(\\alpha)\\Gamma(\\beta)/\\Gamma(\\alpha+\\beta)$ (Barkat, p. 100). The beta distribution on $(0,1)$: $f_X=x^{\\alpha-1}(1-x)^{\\beta-1}/B(\\alpha,\\beta)$, mean $\\alpha/(\\alpha+\\beta)$, variance $\\alpha\\beta/[(\\alpha+\\beta)^2(\\alpha+\\beta+1)]$ (pp. 100 to 101). With $\\alpha=2$, $\\beta=5$: mean {{be_mean}}, variance {{be_var}}, checked by integration and simulation.⟧</p>"),
                ("⟦Tự kiểm tra phần 2||Self-check, part 2⟧",
                 UL(["⟦$Q(x)$ liên hệ thế nào với $\\text{erfc}$?||How is $Q(x)$ related to $\\text{erfc}$?⟧",
                     "⟦Vì sao phân bố mũ \"không nhớ\"?||Why is the exponential distribution \"memoryless\"?⟧",
                     "⟦Gamma $G(\\alpha,\\beta)$ có trung bình và phương sai bao nhiêu?||What are the mean and variance of $G(\\alpha,\\beta)$?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: $Q(x)=\\tfrac12\\text{erfc}(x/\\sqrt2)$; xác suất còn lại sau $x_1$ có cùng dạng; $\\alpha\\beta$ và $\\alpha\\beta^2$.||Hints: $Q(x)=\\tfrac12\\text{erfc}(x/\\sqrt2)$; the residual probability after $x_1$ has the same form; $\\alpha\\beta$ and $\\alpha\\beta^2$.⟧</p>"),
            ]),
        # ---------------------------------------------------------------- PART 3
        dict(
            title="⟦Từ Gauss tới chi bình phương, Rayleigh, Rice, Maxwell||From Gaussian to chi-square, Rayleigh, Rice and Maxwell⟧",
            scr=("⟦Trong radar và truyền thông, ta đo biên độ và công suất của tín hiệu cộng nhiễu, tức căn hoặc bình phương của các biến chuẩn.||In radar and communications we measure amplitude and power of signal plus noise, i.e. roots or squares of normal variables.⟧",
                 "⟦Các phân bố nào xuất hiện khi ta bình phương, cộng, rồi lấy căn các biến chuẩn?||Which distributions arise when we square, add and take roots of normal variables?⟧",
                 "⟦Chi bình phương cho công suất; Rayleigh cho biên độ khi không có tín hiệu; Rice khi có tín hiệu; Maxwell cho 3 chiều; Nakagami cho suy hao đa đường.||Chi-square gives power; Rayleigh gives amplitude without signal; Rice with signal; Maxwell in 3 dimensions; Nakagami for multipath fading.⟧"),
            preview=["⟦Chi bình phương và chi bình phương không tâm||Chi-square and noncentral chi-square⟧", "⟦Rayleigh, Rice, Maxwell||Rayleigh, Rice, Maxwell⟧", "⟦Nakagami, Student, F, Cauchy||Nakagami, Student, F, Cauchy⟧"],
            slides=[
                ("⟦Chi bình phương||The chi-square distribution⟧",
                 "<p>⟦Nếu $X_1,\\ldots,X_n$ chuẩn $N(0,\\sigma^2)$ độc lập thì $X=\\sum X_i^2$ là chi bình phương $n$ bậc tự do; nó là gamma với $\\alpha=n/2$, $\\beta=2\\sigma^2$ (Barkat, mục 2.3.5, tr. 101 đến 106). Với $\\sigma=1$: trung bình $n$, phương sai $2n$. Số đo $n=4$: trung bình {{chi_mean}} và phương sai {{chi_var}} theo mô phỏng và theo gamma $G(2,2)$.||If $X_1,\\ldots,X_n$ are independent $N(0,\\sigma^2)$ then $X=\\sum X_i^2$ is chi-square with $n$ degrees of freedom; it is a gamma with $\\alpha=n/2$, $\\beta=2\\sigma^2$ (Barkat, section 2.3.5, pp. 101 to 106). With $\\sigma=1$: mean $n$, variance $2n$. Measured for $n=4$: mean {{chi_mean}} and variance {{chi_var}} by simulation and by the gamma $G(2,2)$.⟧</p>"),
                ("⟦Chi bình phương không tâm||The noncentral chi-square⟧",
                 "<p>⟦Nếu $X_i$ có trung bình $m_i\\ne0$, $X=\\sum X_i^2$ là chi bình phương không tâm với tham số không tâm $\\lambda=\\sum m_i^2$; trung bình $n\\sigma^2+\\lambda$, phương sai $2n\\sigma^4+4\\sigma^2\\lambda$; hàm phân bố biểu diễn qua hàm $Q$ Marcum tổng quát, $F_X(x)=1-Q_m(\\sqrt\\lambda/\\sigma,\\sqrt x/\\sigma)$ với $m=n/2$ (tr. 102 đến 106). Số đo $n=3$, $\\sigma=1$, $\\lambda=5$: trung bình {{nc_mean}} và phương sai {{nc_var}}.||If the $X_i$ have means $m_i\\ne0$, $X=\\sum X_i^2$ is noncentral chi-square with noncentrality parameter $\\lambda=\\sum m_i^2$; mean $n\\sigma^2+\\lambda$, variance $2n\\sigma^4+4\\sigma^2\\lambda$; the distribution function is expressed by the generalised Marcum $Q$ function, $F_X(x)=1-Q_m(\\sqrt\\lambda/\\sigma,\\sqrt x/\\sigma)$ with $m=n/2$ (pp. 102 to 106). Measured for $n=3$, $\\sigma=1$, $\\lambda=5$: mean {{nc_mean}} and variance {{nc_var}}.⟧</p>"),
                ("⟦Rayleigh||The Rayleigh distribution⟧",
                 "<p>⟦Nếu $X_1,X_2$ độc lập $N(0,\\sigma^2)$ thì $X=X_1^2+X_2^2$ là chi bình phương 2 bậc và $Y=\\sqrt X$ là Rayleigh: $f_Y=\\frac y{\\sigma^2}e^{-y^2/2\\sigma^2}$, $F_Y=1-e^{-y^2/2\\sigma^2}$, trung bình $\\sigma\\sqrt{\\pi/2}$, phương sai $(2-\\pi/2)\\sigma^2$ (Barkat, mục 2.3.6, tr. 106 đến 108). Với $\\sigma=1$: trung bình {{ray_mean}}, phương sai {{ray_var}}, $F(\\sigma)$ = {{ray_F1}} (hình 2.9). Ví dụ: $Y=a+bX^2$ với $X$ Rayleigh có phương sai $4b^2\\sigma^4$; $b=2$, $\\sigma=1$: {{ray_vy}}.||If $X_1,X_2$ are independent $N(0,\\sigma^2)$ then $X=X_1^2+X_2^2$ is chi-square with 2 degrees and $Y=\\sqrt X$ is Rayleigh: $f_Y=\\frac y{\\sigma^2}e^{-y^2/2\\sigma^2}$, $F_Y=1-e^{-y^2/2\\sigma^2}$, mean $\\sigma\\sqrt{\\pi/2}$, variance $(2-\\pi/2)\\sigma^2$ (Barkat, section 2.3.6, pp. 106 to 108). With $\\sigma=1$: mean {{ray_mean}}, variance {{ray_var}}, $F(\\sigma)$ = {{ray_F1}} (Fig. 2.9). Example: $Y=a+bX^2$ with $X$ Rayleigh has variance $4b^2\\sigma^4$; $b=2$, $\\sigma=1$: {{ray_vy}}.⟧</p>"),
                ("⟦Suy ra Rayleigh bằng tọa độ cực||Deriving Rayleigh with polar coordinates⟧",
                 "<p>⟦$F_X(x)=P(X_1^2+X_2^2\\le x^2)=\\frac1{2\\pi\\sigma^2}\\int_0^{2\\pi}d\\theta\\int_0^xre^{-r^2/2\\sigma^2}dr=1-e^{-x^2/2\\sigma^2}$, đạo hàm cho $f_X=\\frac x{\\sigma^2}e^{-x^2/2\\sigma^2}$ (tr. 108 đến 110). Kết quả trùng với định lý cơ bản của chương 1. Số đo: $P(R\\le2)$ theo tích phân cực = {{ray_polar}} = $1-e^{-2}$ và mô phỏng.||$F_X(x)=P(X_1^2+X_2^2\\le x^2)=\\frac1{2\\pi\\sigma^2}\\int_0^{2\\pi}d\\theta\\int_0^xre^{-r^2/2\\sigma^2}dr=1-e^{-x^2/2\\sigma^2}$, whose derivative gives $f_X=\\frac x{\\sigma^2}e^{-x^2/2\\sigma^2}$ (pp. 108 to 110). It agrees with the fundamental theorem of chapter 1. Measured: $P(R\\le2)$ by the polar integral = {{ray_polar}} = $1-e^{-2}$ and by simulation.⟧</p>"),
                ("⟦Rice||The Rice distribution⟧",
                 "<p>⟦Nếu $X_1,X_2$ có trung bình $m_1,m_2$ (tín hiệu) và phương sai $\\sigma^2$ (nhiễu), $R=\\sqrt{X_1^2+X_2^2}$ là Rice: $f_R=\\frac r{\\sigma^2}e^{-(r^2+\\lambda)/2\\sigma^2}I_0(\\sqrt\\lambda r/\\sigma^2)$, $\\lambda=m_1^2+m_2^2$, $F_R=1-Q_1(\\sqrt\\lambda/\\sigma,r/\\sigma)$; $\\lambda=0$ cho Rayleigh (tr. 111 đến 113). Số đo với $m_1=m_2=1$, $\\sigma=1$: $F_R(2)$ = {{rice_F}} theo hàm Marcum (qua chi bình phương không tâm), theo tích phân mật độ Rice và theo mô phỏng; trung bình $R$ = {{rice_mean}}.||If $X_1,X_2$ have means $m_1,m_2$ (signal) and variance $\\sigma^2$ (noise), $R=\\sqrt{X_1^2+X_2^2}$ is Rice: $f_R=\\frac r{\\sigma^2}e^{-(r^2+\\lambda)/2\\sigma^2}I_0(\\sqrt\\lambda r/\\sigma^2)$, $\\lambda=m_1^2+m_2^2$, $F_R=1-Q_1(\\sqrt\\lambda/\\sigma,r/\\sigma)$; $\\lambda=0$ gives Rayleigh (pp. 111 to 113). Measured with $m_1=m_2=1$, $\\sigma=1$: $F_R(2)$ = {{rice_F}} by the Marcum function (through noncentral chi-square), by integrating the Rice density and by simulation; the mean of $R$ = {{rice_mean}}.⟧</p>"),
                ("⟦Maxwell||The Maxwell distribution⟧",
                 "<p>⟦Ba biến chuẩn $N(0,\\sigma^2)$: $Y=\\sqrt{X_1^2+X_2^2+X_3^2}$ là Maxwell, $f_Y=\\frac1{\\sigma^3}\\sqrt{\\tfrac2\\pi}\\,y^2e^{-y^2/2\\sigma^2}$, trung bình $2\\sigma\\sqrt{2/\\pi}$, phương sai $\\sigma^2(3-8/\\pi)$ (tr. 113 đến 114). Với $\\sigma=1$: trung bình {{mx_mean}}, phương sai {{mx_var}}. Tổng quát hóa cho $n$ biến có trung bình bất kỳ ta được chi bình phương không tâm, Rayleigh, Rice, Maxwell là các trường hợp riêng.||Three $N(0,\\sigma^2)$ variables: $Y=\\sqrt{X_1^2+X_2^2+X_3^2}$ is Maxwell, $f_Y=\\frac1{\\sigma^3}\\sqrt{\\tfrac2\\pi}\\,y^2e^{-y^2/2\\sigma^2}$, mean $2\\sigma\\sqrt{2/\\pi}$, variance $\\sigma^2(3-8/\\pi)$ (pp. 113 to 114). With $\\sigma=1$: mean {{mx_mean}}, variance {{mx_var}}. Generalising to $n$ variables with arbitrary means gives the noncentral chi-square, with Rayleigh, Rice and Maxwell as special cases.⟧</p>"),
                ("⟦Nakagami $m$||The Nakagami $m$-distribution⟧",
                 "<p>⟦Trong truyền thông, Nakagami mô tả thống kê tín hiệu qua kênh đa đường suy hao: $f_X=\\frac2{\\Gamma(m)}\\left(\\frac mv\\right)^mx^{2m-1}e^{-mx^2/v}$ với $v=E[X^2]$ và $m=v^2/E[(X^2-v)^2]\\ge\\tfrac12$ là \"hệ số suy hao\" (Barkat, mục 2.3.7, tr. 115); $m=1$ cho Rayleigh. Số đo: mô phỏng với $m=2$, $v=1$ cho {{nk_m}} khi ước lượng $m$ từ mômen, và $E[X^2]$ = {{nk_v}}; tích phân số của mật độ bằng {{nk_int}}.||In communications the Nakagami distribution describes the statistics of signals through multipath fading channels: $f_X=\\frac2{\\Gamma(m)}\\left(\\frac mv\\right)^mx^{2m-1}e^{-mx^2/v}$ with $v=E[X^2]$ and $m=v^2/E[(X^2-v)^2]\\ge\\tfrac12$ the \"fading figure\" (Barkat, section 2.3.7, p. 115); $m=1$ gives Rayleigh. Measured: a simulation with $m=2$, $v=1$ gives {{nk_m}} when $m$ is estimated from moments, and $E[X^2]$ = {{nk_v}}; the numerical integral of the density is {{nk_int}}.⟧</p>"),
                ("⟦Student $t$ và $F$||Student's $t$ and the $F$ distribution⟧",
                 "<p>⟦$T=X/\\sqrt{Y/n}$ với $X\\sim N(0,1)$, $Y\\sim\\chi^2_n$ độc lập là Student $t$ với $n$ bậc: $f_T=\\dfrac{\\Gamma(\\frac{n+1}2)}{\\sqrt{n\\pi}\\Gamma(n/2)}(1+t^2/n)^{-(n+1)/2}$; trung bình 0, phương sai $n/(n-2)$ khi $n>2$ (tr. 115 đến 117). $F=(Y_1/n_1)/(Y_2/n_2)$ là tỉ số hai chi bình phương chuẩn hóa, trung bình $n_2/(n_2-2)$ (tr. 117 đến 120). Số đo: $t$ với $n=5$: phương sai {{t_var}}; $F$ với $(4,10)$ bậc: trung bình {{f_mean}}; $t$ với $n=1$: $P(|T|<1)$ = {{t1_p}}, chính là Cauchy.||$T=X/\\sqrt{Y/n}$ with independent $X\\sim N(0,1)$, $Y\\sim\\chi^2_n$ is Student's $t$ with $n$ degrees: $f_T=\\dfrac{\\Gamma(\\frac{n+1}2)}{\\sqrt{n\\pi}\\Gamma(n/2)}(1+t^2/n)^{-(n+1)/2}$; mean 0, variance $n/(n-2)$ for $n>2$ (pp. 115 to 117). $F=(Y_1/n_1)/(Y_2/n_2)$ is the ratio of two normalised chi-squares, with mean $n_2/(n_2-2)$ (pp. 117 to 120). Measured: $t$ with $n=5$: variance {{t_var}}; $F$ with $(4,10)$ degrees: mean {{f_mean}}; $t$ with $n=1$: $P(|T|<1)$ = {{t1_p}}, which is the Cauchy.⟧</p>"),
                ("⟦Cauchy: không có trung bình||Cauchy: no mean⟧",
                 "<p>⟦$f_X=\\dfrac{\\beta}{\\pi[\\beta^2+(x-\\alpha)^2]}$, $C(\\alpha,\\beta)$: trung bình (giá trị chính) $\\alpha$ nhưng phương sai và mômen cao không tồn tại; hàm sinh mômen không tồn tại, hàm đặc trưng $e^{j\\alpha\\omega-\\beta|\\omega|}$; tổng các biến Cauchy là Cauchy với $\\alpha$ và $\\beta$ cộng lại (Barkat, mục 2.3.9, tr. 120 đến 121). Hệ quả: trung bình mẫu của $n$ biến Cauchy có cùng phân bố với một biến, không hội tụ, trái với luật số lớn. Số đo: $P(|\\bar X_n|<1)$ = {{cau_1}} với $n=1$ và {{cau_100}} với $n=100$; còn với chuẩn tắc, $n=100$ cho {{cau_n100}}. Tổng hai $C(0,1)$ là $C(0,2)$: $P(|X|<2)$ = {{cau_sum}}.||$f_X=\\dfrac{\\beta}{\\pi[\\beta^2+(x-\\alpha)^2]}$, $C(\\alpha,\\beta)$: the mean (principal value) is $\\alpha$ but the variance and higher moments do not exist; the moment generating function does not exist, the characteristic function is $e^{j\\alpha\\omega-\\beta|\\omega|}$; the sum of Cauchy variables is Cauchy with $\\alpha$ and $\\beta$ adding (Barkat, section 2.3.9, pp. 120 to 121). Consequence: the sample mean of $n$ Cauchy variables has the same distribution as one variable and does not converge, contrary to the law of large numbers. Measured: $P(|\\bar X_n|<1)$ = {{cau_1}} for $n=1$ and {{cau_100}} for $n=100$; for a standard normal $n=100$ gives {{cau_n100}}. The sum of two $C(0,1)$ is $C(0,2)$: $P(|X|<2)$ = {{cau_sum}}.⟧</p>"),
                ("⟦Tự kiểm tra phần 3||Self-check, part 3⟧",
                 UL(["⟦Khi nào biên độ là Rayleigh, khi nào là Rice?||When is the amplitude Rayleigh and when Rice?⟧",
                     "⟦Chi bình phương $n$ bậc là trường hợp riêng của gamma nào?||Chi-square with $n$ degrees is which special gamma?⟧",
                     "⟦Vì sao luật số lớn không áp dụng cho Cauchy?||Why does the law of large numbers not apply to the Cauchy?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: Rayleigh khi chỉ có nhiễu, Rice khi có tín hiệu; $\\alpha=n/2$, $\\beta=2\\sigma^2$; vì không có trung bình hữu hạn (kỳ vọng $|X|$ vô hạn).||Hints: Rayleigh with noise only, Rice with a signal; $\\alpha=n/2$, $\\beta=2\\sigma^2$; because there is no finite mean ($E|X|$ is infinite).⟧</p>"),
            ]),
        # ---------------------------------------------------------------- PART 4
        dict(
            title="⟦Gauss nhiều chiều và các phân bố đặc biệt||Multivariate Gaussian and special distributions⟧",
            scr=("⟦Tín hiệu và nhiễu nhiều cảm biến là vector ngẫu nhiên; radar biển và địa hình có thống kê không Gauss.||Multisensor signals and noise are random vectors; sea and terrain radar clutter has non-Gaussian statistics.⟧",
                 "⟦Cần mô hình chung cho vector Gauss và vài phân bố có đuôi nặng: Weibull, log-chuẩn, K.||We need a general model for Gaussian vectors and a few heavy-tailed distributions: Weibull, log-normal, K.⟧",
                 "⟦Gauss hai chiều xác định bởi trung bình, phương sai và $\\rho$; Weibull tổng quát hóa mũ và Rayleigh; K là tích của Rayleigh (speckle) và gamma (texture).||The bivariate Gaussian is determined by means, variances and $\\rho$; the Weibull generalises the exponential and Rayleigh; K is the product of Rayleigh (speckle) and gamma (texture).⟧"),
            preview=["⟦Gauss hai chiều và nhiều chiều||Bivariate and multivariate Gaussian⟧", "⟦Weibull và log-chuẩn||Weibull and log-normal⟧", "⟦Phân bố K và hợp thành tổng quát||The K distribution and the generalised compound⟧"],
            slides=[
                ("⟦Gauss hai chiều||The bivariate Gaussian⟧",
                 "<p>⟦$f_{X_1X_2}=\\dfrac1{2\\pi\\sigma_1\\sigma_2\\sqrt{1-\\rho^2}}\\exp\\!\\Big\\{-\\dfrac1{2(1-\\rho^2)}\\Big[\\dfrac{(x_1-m_1)^2}{\\sigma_1^2}+\\dfrac{(x_2-m_2)^2}{\\sigma_2^2}-2\\rho\\dfrac{(x_1-m_1)(x_2-m_2)}{\\sigma_1\\sigma_2}\\Big]\\Big\\}$ (Barkat, mục 2.4.1, tr. 121 đến 122). Các phân bố biên là chuẩn, và phân bố điều kiện $f(x_2\\mid x_1)$ cũng chuẩn với trung bình $m_2+\\rho\\frac{\\sigma_2}{\\sigma_1}(x_1-m_1)$ và phương sai $\\sigma_2^2(1-\\rho^2)$. Số đo: $m=(1,-1)$, $\\sigma=(1,2)$, $\\rho=0.6$, cho $x_1=2$: trung bình điều kiện {{bg_cm}}, phương sai điều kiện {{bg_cv}}, theo công thức và theo mô phỏng có điều kiện.||$f_{X_1X_2}=\\dfrac1{2\\pi\\sigma_1\\sigma_2\\sqrt{1-\\rho^2}}\\exp\\!\\Big\\{-\\dfrac1{2(1-\\rho^2)}\\Big[\\dfrac{(x_1-m_1)^2}{\\sigma_1^2}+\\dfrac{(x_2-m_2)^2}{\\sigma_2^2}-2\\rho\\dfrac{(x_1-m_1)(x_2-m_2)}{\\sigma_1\\sigma_2}\\Big]\\Big\\}$ (Barkat, section 2.4.1, pp. 121 to 122). The marginals are normal, and the conditional $f(x_2\\mid x_1)$ is also normal with mean $m_2+\\rho\\frac{\\sigma_2}{\\sigma_1}(x_1-m_1)$ and variance $\\sigma_2^2(1-\\rho^2)$. Measured: $m=(1,-1)$, $\\sigma=(1,2)$, $\\rho=0.6$, for $x_1=2$: conditional mean {{bg_cm}}, conditional variance {{bg_cv}}, by formula and by conditional simulation.⟧</p>"),
                ("⟦Hàm đặc trưng và dạng ma trận||The characteristic function and matrix form⟧",
                 "<p>⟦Với ma trận hiệp phương sai $C=\\begin{pmatrix}\\sigma_1^2&\\rho\\sigma_1\\sigma_2\\\\\\rho\\sigma_1\\sigma_2&\\sigma_2^2\\end{pmatrix}$, $|C|=\\sigma_1^2\\sigma_2^2(1-\\rho^2)$, mật độ là $\\dfrac1{2\\pi\\sqrt{|C|}}\\exp[-\\tfrac12(\\mathbf x-\\mathbf m)^TC^{-1}(\\mathbf x-\\mathbf m)]$ và hàm đặc trưng $\\exp(-\\tfrac12\\boldsymbol\\omega^TC\\boldsymbol\\omega+j\\mathbf m^T\\boldsymbol\\omega)$ (tr. 123 đến 124); dạng $n$ chiều là (2.236), (2.237) (tr. 127). Số đo với $C$ ở trên: $|C|$ = {{bg_det}}; mật độ tại tâm bằng {{bg_f0}} theo công thức vô hướng và theo công thức ma trận.||With the covariance matrix $C=\\begin{pmatrix}\\sigma_1^2&\\rho\\sigma_1\\sigma_2\\\\\\rho\\sigma_1\\sigma_2&\\sigma_2^2\\end{pmatrix}$, $|C|=\\sigma_1^2\\sigma_2^2(1-\\rho^2)$, the density is $\\dfrac1{2\\pi\\sqrt{|C|}}\\exp[-\\tfrac12(\\mathbf x-\\mathbf m)^TC^{-1}(\\mathbf x-\\mathbf m)]$ and the characteristic function $\\exp(-\\tfrac12\\boldsymbol\\omega^TC\\boldsymbol\\omega+j\\mathbf m^T\\boldsymbol\\omega)$ (pp. 123 to 124); the $n$-dimensional forms are (2.236), (2.237) (p. 127). Measured with the $C$ above: $|C|$ = {{bg_det}}; the density at the centre is {{bg_f0}} by the scalar formula and by the matrix formula.⟧</p>"),
                ("⟦Không tương quan là độc lập (chỉ với Gauss)||Uncorrelated means independent (for Gaussians only)⟧",
                 "<p>⟦Khi $\\rho=0$, mật độ chung phân tích thành tích các mật độ biên nên $X_1,X_2$ độc lập, và hàm đặc trưng chung bằng tích các hàm đặc trưng biên. Đây là đặc tính quan trọng của biến Gauss: không tương quan kéo theo độc lập; ma trận hiệp phương sai đường chéo là điều kiện cần và đủ (tr. 124, 127). Tương phản với module 10 (nửa đĩa: $\\rho=0$ nhưng phụ thuộc). Số đo: với $\\rho=0$ độ lệch tối đa giữa mật độ chung và tích các biên là {{bg_ind}}.||When $\\rho=0$ the joint density factors into the product of the marginals, so $X_1,X_2$ are independent, and the joint characteristic function equals the product of the marginals. This is an important characteristic of Gaussian variables: uncorrelated implies independent; a diagonal covariance matrix is necessary and sufficient (pp. 124, 127). Contrast module 10 (the half-disc: $\\rho=0$ yet dependent). Measured: with $\\rho=0$ the largest deviation between the joint density and the product of the marginals is {{bg_ind}}.⟧</p>"),
                ("⟦Elip chuẩn và phép quay||The standard ellipse and rotation⟧",
                 "<p>⟦Đặt biểu thức trong ngoặc của mũ bằng 1 được elip chuẩn tâm $(m_1,m_2)$ (hình 2.16). Xem $X_1,X_2$ là xoay góc $\\theta$ của hai biến độc lập $U,V$: $\\sigma_1^2=\\sigma_u^2\\cos^2\\theta+\\sigma_v^2\\sin^2\\theta$, $\\sigma_2^2=\\sigma_u^2\\sin^2\\theta+\\sigma_v^2\\cos^2\\theta$, $E[X_1X_2]=(\\sigma_u^2-\\sigma_v^2)\\sin\\theta\\cos\\theta$ và $\\theta=\\tfrac12\\arctan\\dfrac{2\\rho\\sigma_1\\sigma_2}{\\sigma_1^2-\\sigma_2^2}$ (tr. 124 đến 126). Với $\\sigma=(1,2)$, $\\rho=0.6$: $\\theta$ = {{bg_theta}} độ, $\\sigma_u^2$ = {{bg_su}}, $\\sigma_v^2$ = {{bg_sv}}, và đó chính là các trị riêng của $C$ (tính bằng phân tích trị riêng).||Setting the bracket in the exponent equal to 1 gives the standard ellipse centred at $(m_1,m_2)$ (Fig. 2.16). Regard $X_1,X_2$ as a rotation by angle $\\theta$ of independent $U,V$: $\\sigma_1^2=\\sigma_u^2\\cos^2\\theta+\\sigma_v^2\\sin^2\\theta$, $\\sigma_2^2=\\sigma_u^2\\sin^2\\theta+\\sigma_v^2\\cos^2\\theta$, $E[X_1X_2]=(\\sigma_u^2-\\sigma_v^2)\\sin\\theta\\cos\\theta$ and $\\theta=\\tfrac12\\arctan\\dfrac{2\\rho\\sigma_1\\sigma_2}{\\sigma_1^2-\\sigma_2^2}$ (pp. 124 to 126). With $\\sigma=(1,2)$, $\\rho=0.6$: $\\theta$ = {{bg_theta}} degrees, $\\sigma_u^2$ = {{bg_su}}, $\\sigma_v^2$ = {{bg_sv}}, and these are exactly the eigenvalues of $C$ (computed by eigendecomposition).⟧</p>{{fig:ellipse}}"),
                ("⟦Weibull||The Weibull distribution⟧",
                 "<p>⟦$f_X=abx^{b-1}e^{-ax^b}$, $x>0$, với $a$ là tham số tỉ lệ, $b$ tham số hình dạng; $F_X=1-e^{-ax^b}$; $E[X]=a^{-1/b}\\Gamma(1+1/b)$, $\\operatorname{var}=a^{-2/b}[\\Gamma(1+2/b)-\\Gamma^2(1+1/b)]$ (Barkat, mục 2.4.2, tr. 129 đến 131). $b=1$ cho mũ, $b=2$ cho Rayleigh với $a=1/2\\sigma^2$. Số đo: $b=2$, $a=\\tfrac12$: trung bình {{wb_rmean}} bằng Rayleigh $\\sigma\\sqrt{\\pi/2}$; $b=3$, $a=1$: trung bình {{wb_m3}}, phương sai {{wb_v3}}.||$f_X=abx^{b-1}e^{-ax^b}$, $x>0$, with $a$ the scale and $b$ the shape parameter; $F_X=1-e^{-ax^b}$; $E[X]=a^{-1/b}\\Gamma(1+1/b)$, $\\operatorname{var}=a^{-2/b}[\\Gamma(1+2/b)-\\Gamma^2(1+1/b)]$ (Barkat, section 2.4.2, pp. 129 to 131). $b=1$ gives the exponential, $b=2$ the Rayleigh with $a=1/2\\sigma^2$. Measured: $b=2$, $a=\\tfrac12$: mean {{wb_rmean}}, equal to the Rayleigh $\\sigma\\sqrt{\\pi/2}$; $b=3$, $a=1$: mean {{wb_m3}}, variance {{wb_v3}}.⟧</p>"),
                ("⟦Log-chuẩn||The log-normal distribution⟧",
                 "<p>⟦$\\ln X$ là chuẩn: $f_X=\\dfrac1{\\sqrt{2\\pi}\\sigma x}\\exp\\!\\left[-\\dfrac{\\ln^2(x/x_m)}{2\\sigma^2}\\right]$ với $x_m$ là trung vị (Barkat, mục 2.4.3, tr. 131 đến 132). Trung bình $x_me^{\\sigma^2/2}$, phương sai $x_m^2e^{\\sigma^2}(e^{\\sigma^2}-1)$, $E[X^k]=x_m^ke^{k^2\\sigma^2/2}$; tỉ số trung bình trên trung vị $\\rho=e^{\\sigma^2/2}$. Với $x_m=1$, $\\sigma=0.5$: trung bình {{ln_mean}}, phương sai {{ln_var}}.||$\\ln X$ is normal: $f_X=\\dfrac1{\\sqrt{2\\pi}\\sigma x}\\exp\\!\\left[-\\dfrac{\\ln^2(x/x_m)}{2\\sigma^2}\\right]$ with $x_m$ the median (Barkat, section 2.4.3, pp. 131 to 132). Mean $x_me^{\\sigma^2/2}$, variance $x_m^2e^{\\sigma^2}(e^{\\sigma^2}-1)$, $E[X^k]=x_m^ke^{k^2\\sigma^2/2}$; the mean-to-median ratio is $\\rho=e^{\\sigma^2/2}$. With $x_m=1$, $\\sigma=0.5$: mean {{ln_mean}}, variance {{ln_var}}.⟧</p>"),
                ("⟦Phân bố K: speckle nhân texture||The K distribution: speckle times texture⟧",
                 "<p>⟦Phân bố K sinh ra để mô hình nhiễu phản xạ biển của radar: $f_X=\\dfrac4{b\\Gamma(\\nu)}\\left(\\dfrac xb\\right)^\\nu K_{\\nu-1}\\!\\left(\\dfrac{2x}b\\right)$, $x\\ge0$, $K_\\nu$ là hàm Bessel biến dạng, $b$ tỉ lệ, $\\nu$ hình dạng (Barkat, mục 2.4.4, tr. 132 đến 135). Nó là kết quả của $X=ST$: $S$ speckle Rayleigh $f_S=2se^{-s^2}$ và $T$ texture với $f_T=\\frac2{b^\\nu\\Gamma(\\nu)}t^{2\\nu-1}e^{-t^2/b^2}$, tính từ $f_X=\\int f_{X|T}(x|t)f_T(t)dt$ với $f_{X|T}=\\frac{2x}{t^2}e^{-x^2/t^2}$. Với $b=1$, $\\nu=2$: $f_X(1)$ = {{k_f1}} bằng tích phân hợp thành và bằng công thức Bessel; $E[X^2]=\\nu b^2$ = {{k_e2}}, kiểm bằng mô phỏng.||The K distribution arose to model radar sea clutter: $f_X=\\dfrac4{b\\Gamma(\\nu)}\\left(\\dfrac xb\\right)^\\nu K_{\\nu-1}\\!\\left(\\dfrac{2x}b\\right)$, $x\\ge0$, $K_\\nu$ the modified Bessel function, $b$ the scale and $\\nu$ the shape parameter (Barkat, section 2.4.4, pp. 132 to 135). It results from $X=ST$: $S$ Rayleigh speckle $f_S=2se^{-s^2}$ and $T$ texture with $f_T=\\frac2{b^\\nu\\Gamma(\\nu)}t^{2\\nu-1}e^{-t^2/b^2}$, computed from $f_X=\\int f_{X|T}(x|t)f_T(t)dt$ with $f_{X|T}=\\frac{2x}{t^2}e^{-x^2/t^2}$. With $b=1$, $\\nu=2$: $f_X(1)$ = {{k_f1}} by the compound integral and by the Bessel formula; $E[X^2]=\\nu b^2$ = {{k_e2}}, checked by simulation.⟧</p>{{fig:kdist}}"),
                ("⟦Hợp thành tổng quát và ý nghĩa||The generalised compound and what it means⟧",
                 "<p>⟦Phân bố K là một ví dụ của phân bố hợp thành: một tham số của phân bố cơ sở (Rayleigh) lại ngẫu nhiên (gamma). Barkat trình bày hợp thành tổng quát cho các mô hình nhiễu radar không Gauss (mục 2.4.5, tr. 135 đến 136), có nguồn từ các công trình về thống kê nhiễu độ phân giải cao (Anastassopoulos và cộng sự, 1999). Ý nghĩa: khi biến đổi thang của nhiễu nền, như tán xạ biển, thay đổi chậm, ngưỡng phát hiện cố định sẽ sai; đó là lý do dùng ngưỡng thích nghi CFAR ở các module 25 và 26.||The K distribution is one example of a compound distribution: a parameter of the base distribution (Rayleigh) is itself random (gamma). Barkat presents a generalised compound for non-Gaussian radar clutter models (section 2.4.5, pp. 135 to 136), from work on high-resolution clutter statistics (Anastassopoulos et al., 1999). Meaning: when the scale of the background clutter, e.g. sea scatter, varies slowly, a fixed detection threshold is wrong; this is why adaptive CFAR thresholds are used in modules 25 and 26.⟧</p>"),
                ("⟦Tự kiểm tra phần 4||Self-check, part 4⟧",
                 UL(["⟦Phân bố điều kiện của Gauss hai chiều có gì đặc biệt?||What is special about the conditional distribution of a bivariate Gaussian?⟧",
                     "⟦Weibull $b=2$ trùng phân bố nào?||Which distribution does Weibull with $b=2$ coincide with?⟧",
                     "⟦K là tích của hai biến nào?||K is the product of which two variables?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: cũng chuẩn, trung bình tuyến tính theo $x_1$, phương sai $\\sigma_2^2(1-\\rho^2)$; Rayleigh; speckle Rayleigh và texture kiểu gamma.||Hints: also normal, mean linear in $x_1$, variance $\\sigma_2^2(1-\\rho^2)$; Rayleigh; Rayleigh speckle and gamma-type texture.⟧</p>"),
            ]),
    ],
    takeaways=[
        "⟦Bernoulli sinh nhị thức, hình học, Pascal; siêu bội là lấy mẫu không hoàn lại; Poisson là giới hạn nhị thức.||Bernoulli generates the binomial, geometric and Pascal; the hypergeometric is sampling without replacement; Poisson is the binomial limit.⟧",
        "⟦Chuẩn: $Q$, erf; giới hạn trung tâm cho nhị thức và Poisson; mũ không nhớ, gamma là tổng mũ, Laplace là mũ hai phía.||Normal: $Q$, erf; the central limit for binomial and Poisson; the exponential is memoryless, gamma is a sum of exponentials, Laplace is two-sided.⟧",
        "⟦Gauss → chi bình phương → Rayleigh (nhiễu), Rice (tín hiệu cộng nhiễu), Maxwell (3 chiều); Nakagami cho suy hao đa đường.||Gaussian → chi-square → Rayleigh (noise), Rice (signal plus noise), Maxwell (3D); Nakagami for multipath fading.⟧",
        "⟦Cauchy không có mômen nên luật số lớn không đúng; Gauss nhiều chiều: không tương quan là độc lập.||The Cauchy has no moments so the law of large numbers fails; multivariate Gaussian: uncorrelated is independent.⟧",
        "⟦Weibull tổng quát hóa mũ và Rayleigh; log-chuẩn và K mô hình nhiễu đuôi nặng, với K là speckle nhân texture.||The Weibull generalises the exponential and Rayleigh; log-normal and K model heavy-tailed clutter, K being speckle times texture.⟧",
    ],
    history="<p>⟦Chương 2 xây trên các tài liệu kinh điển: Abramowitz và Stegun cho hàm đặc biệt, Feller và Papoulis cho xác suất, Proakis cho truyền thông số, Jakeman và Pusey (1976) đề xuất phân bố K cho nhiễu biển, Ward và Watts (1985) về nhiễu biển radar, Sekine và Mao về nhiễu Weibull, Anastassopoulos và cộng sự (1999) về thống kê nhiễu độ phân giải cao (Barkat, tr. 139 và thư mục).||"
            "Chapter 2 builds on classical sources: Abramowitz and Stegun for special functions, Feller and Papoulis for probability, Proakis for digital communications, Jakeman and Pusey (1976) who proposed the K distribution for sea echo, Ward and Watts (1985) on radar sea clutter, Sekine and Mao on Weibull clutter, and Anastassopoulos et al. (1999) on high-resolution clutter statistics (Barkat, p. 139 and bibliography).⟧</p>",
    case="<p>⟦<b>Chọn mô hình cho biên độ nhiễu.</b> Nếu nhiễu nền chỉ là nhiệt (tổng nhiều đóng góp độc lập, giới hạn trung tâm), hai thành phần vuông pha là Gauss và biên độ là Rayleigh: xác suất biên độ vượt $\\sigma$ là $1-F(\\sigma)$ = {{ray_tail}}. Nếu có thêm tín hiệu cố định, biên độ là Rice, $F_R(2)$ = {{rice_F}} với ví dụ trên. Nếu hệ số phản xạ trung bình thay đổi chậm theo vùng (biển động), tích speckle nhân texture cho K, đuôi nặng hơn Rayleigh, và ngưỡng cho cùng xác suất báo động giả phải cao hơn nhiều: đây là lý do có phát hiện CFAR. Cauchy là trường hợp cực đoan, không có trung bình: {{cau_100}} cho mọi $n$.||"
          "<b>Choosing a model for clutter amplitude.</b> If the background is only thermal (a sum of many independent contributions, central limit), the two quadrature components are Gaussian and the amplitude is Rayleigh: the probability that the amplitude exceeds $\\sigma$ is $1-F(\\sigma)$ = {{ray_tail}}. With a fixed signal added, the amplitude is Rice, $F_R(2)$ = {{rice_F}} in the example above. If the mean reflectivity varies slowly across regions (rough sea), the product speckle times texture gives K, heavier-tailed than Rayleigh, and the threshold for the same false-alarm probability must be much higher: this is why CFAR detection exists. The Cauchy is the extreme case, with no mean: {{cau_100}} for every $n$.⟧</p>",
    practice=[
        "⟦Mở notebook và chạy cell cài đặt.||Open the notebook and run the setup cell.⟧",
        "⟦Bài 1: kiểm bằng mô phỏng $P(X\\ge r)=P(Y\\le n)$ cho nhị thức và Pascal với các $p$ khác nhau.||Task 1: check $P(X\\ge r)=P(Y\\le n)$ by simulation for binomial and Pascal with various $p$.⟧",
        "⟦Bài 2: đối với Rice, thay $\\lambda$ từ 0 tới 9 và quan sát mật độ chuyển từ Rayleigh sang gần Gauss (hình 2.12).||Task 2: for the Rice, vary $\\lambda$ from 0 to 9 and watch the density move from Rayleigh to nearly Gaussian (Fig. 2.12).⟧",
        "⟦Bài 3: tính xác suất vượt ngưỡng cố định của Rayleigh, Weibull $b=1.5$ và K ($\\nu=1$) cùng trung bình bình phương và so sánh đuôi.||Task 3: compute the probability of exceeding a fixed threshold for Rayleigh, Weibull $b=1.5$ and K ($\\nu=1$) with the same mean square and compare the tails.⟧",
        "⟦Bài 4: xác nhận $X=ST$ cho K bằng mô phỏng hai bước rồi so histogram với công thức Bessel.||Task 4: confirm $X=ST$ for K by a two-step simulation and compare the histogram with the Bessel formula.⟧",
    ],
    pitfalls=[
        "<b>⟦\"Trung bình mẫu luôn hội tụ.\"||\"The sample mean always converges.\"⟧</b><p>⟦Không với Cauchy: $P(|\\bar X_n|<1)$ = {{cau_1}} với $n=1$ và {{cau_100}} với $n=100$, còn chuẩn tắc cho {{cau_n100}} (Barkat, mục 2.3.9).||Not for the Cauchy: $P(|\\bar X_n|<1)$ = {{cau_1}} for $n=1$ and {{cau_100}} for $n=100$, while the standard normal gives {{cau_n100}} (Barkat, section 2.3.9).⟧</p>",
        "<b>⟦\"Không tương quan là độc lập.\"||\"Uncorrelated means independent.\"⟧</b><p>⟦Chỉ đúng cho Gauss chung; với $\\rho=0$ mật độ chung phân tích được (lệch {{bg_ind}}) nhưng điều này không đúng với phân bố tùy ý (module 10, nửa đĩa).||True only for jointly Gaussian variables; with $\\rho=0$ the joint density factors (deviation {{bg_ind}}) but this fails for arbitrary distributions (module 10, the half-disc).⟧</p>",
        "<b>⟦\"Xấp xỉ chuẩn luôn tốt cho Poisson.\"||\"The normal approximation is always good for the Poisson.\"⟧</b><p>⟦Tốt khi $\\lambda$ lớn; với $\\lambda=3.2$ xấp xỉ cho {{c212_n}} so với chính xác {{c212_ex}} (bài 2.12).||Good when $\\lambda$ is large; with $\\lambda=3.2$ it gives {{c212_n}} against the exact {{c212_ex}} (problem 2.12).⟧</p>",
        "<b>⟦\"Biên độ tín hiệu cộng nhiễu là Rayleigh.\"||\"The amplitude of signal plus noise is Rayleigh.\"⟧</b><p>⟦Rayleigh chỉ khi trung bình các thành phần bằng 0; có tín hiệu thì là Rice (trung bình {{rice_mean}} với $\\lambda=2$ so với Rayleigh {{ray_mean}}).||Rayleigh only when the component means are zero; with a signal it is Rice (mean {{rice_mean}} for $\\lambda=2$ against Rayleigh {{ray_mean}}).⟧</p>",
    ],
    refs=[
        "⟦M. Barkat, <i>Signal Detection and Estimation</i>, 2nd ed., Artech House, 2005, chương 2 (tr. 75 đến 139).||M. Barkat, <i>Signal Detection and Estimation</i>, 2nd ed., Artech House, 2005, chapter 2 (pp. 75 to 139).⟧",
        "⟦Tài liệu do chương 2 trích: Anastassopoulos et al. (1999), Abramowitz và Stegun, Feller, Papoulis, Proakis, Jakeman và Pusey (1976), Ward và Watts (1985).||Works cited by chapter 2: Anastassopoulos et al. (1999), Abramowitz and Stegun, Feller, Papoulis, Proakis, Jakeman and Pusey (1976), Ward and Watts (1985).⟧",
    ],
    quiz=[
        dict(q="⟦Xác suất được đúng hai mặt 6 khi gieo xúc xắc 10 lần bằng bao nhiêu?||What is the probability of exactly two sixes in 10 rolls of a die?⟧",
             opts=["{{bi_ex21}}", "0.2000", "0.1550", "0.3230"], explain="⟦$\\binom{10}2(1/6)^2(5/6)^8$ = {{bi_ex21}}.||$\\binom{10}2(1/6)^2(5/6)^8$ = {{bi_ex21}}.⟧"),
        dict(q="⟦Xác suất quyết định đúng theo đa số 2/3 với độ đúng mỗi quyết định 0.8 bằng bao nhiêu?||What is the probability of a correct majority-of-three decision with 0.8 accuracy per decision?⟧",
             opts=["{{bi_ex22}}", "0.8000", "0.5120", "0.9920"], explain="⟦$0.384+0.512$ = {{bi_ex22}}.||$0.384+0.512$ = {{bi_ex22}}.⟧"),
        dict(q="⟦Phương sai của nhị thức $n=10$, $p=1/6$ bằng bao nhiêu?||What is the variance of the binomial $n=10$, $p=1/6$?⟧",
             opts=["{{bi_var}}", "1.6667", "0.8333", "2.7778"], explain="⟦$npq$ = {{bi_var}}; trung bình {{bi_mean}}.||$npq$ = {{bi_var}}; the mean is {{bi_mean}}.⟧"),
        dict(q="⟦Xác suất đa thức $(2,3,5)$ với $n=10$ và xác suất $(0.2,0.3,0.5)$ bằng bao nhiêu?||What is the multinomial probability of counts $(2,3,5)$ with $n=10$ and probabilities $(0.2,0.3,0.5)$?⟧",
             opts=["{{mn_p}}", "0.1000", "0.0300", "0.2520"], explain="⟦$2520\\cdot0.2^2\\cdot0.3^3\\cdot0.5^5$ = {{mn_p}}.||$2520\\cdot0.2^2\\cdot0.3^3\\cdot0.5^5$ = {{mn_p}}.⟧"),
        dict(q="⟦Xác suất mặt 6 đầu tiên xuất hiện ở lần gieo thứ 3 bằng bao nhiêu?||What is the probability the first six appears on the third roll?⟧",
             opts=["{{ge_p3}}", "0.0046", "0.1667", "0.3472"], explain="⟦$(5/6)^2(1/6)$ = {{ge_p3}}; $E$ = {{ge_mean}}, phương sai {{ge_var}}.||$(5/6)^2(1/6)$ = {{ge_p3}}; $E$ = {{ge_mean}}, variance {{ge_var}}.⟧"),
        dict(q="⟦Phương sai của phân bố hình học với $p=1/6$ bằng bao nhiêu?||What is the variance of the geometric distribution with $p=1/6$?⟧",
             opts=["{{ge_var}}", "6.0000", "36.000", "5.0000"], explain="⟦$q/p^2$ = {{ge_var}}.||$q/p^2$ = {{ge_var}}.⟧"),
        dict(q="⟦Pascal $r=3$, $p=0.5$: $P(Y=5)$ bằng bao nhiêu?||Pascal $r=3$, $p=0.5$: what is $P(Y=5)$?⟧",
             opts=["{{pa_p}}", "0.3125", "0.1250", "0.0625"], explain="⟦$\\binom42/32$ = {{pa_p}}.||$\\binom42/32$ = {{pa_p}}.⟧"),
        dict(q="⟦$P(X\\ge3)=P(Y\\le10)$ với $p=0.3$ ($X$ nhị thức $n=10$) bằng bao nhiêu?||What is $P(X\\ge3)=P(Y\\le10)$ for $p=0.3$ ($X$ binomial $n=10$)?⟧",
             opts=["{{pa_rel}}", "0.3828", "0.8497", "0.2668"], explain="⟦Hai vế cùng bằng {{pa_rel}}.||Both sides equal {{pa_rel}}.⟧"),
        dict(q="⟦Ví dụ 2.3 (siêu bội, 11 bóng): xác suất đúng 3 bóng trắng sau 7 lần rút bằng bao nhiêu?||Example 2.3 (hypergeometric, 11 balls): what is the probability of exactly 3 whites in 7 draws?⟧",
             opts=["{{hy_p}}", "0.2963", "0.3000", "0.6364"], explain="⟦$\\binom53\\binom64/\\binom{11}7=5/11$ = {{hy_p}}; phương sai {{hy_var}}.||$\\binom53\\binom64/\\binom{11}7=5/11$ = {{hy_p}}; variance {{hy_var}}.⟧"),
        dict(q="⟦$E[X^2]$ của Poisson $\\lambda=3$ bằng bao nhiêu?||What is $E[X^2]$ for a Poisson with $\\lambda=3$?⟧",
             opts=["{{po_ms}}", "9.0000", "3.0000", "10.000"], explain="⟦$\\lambda^2+\\lambda$ = {{po_ms}}.||$\\lambda^2+\\lambda$ = {{po_ms}}.⟧"),
        dict(q="⟦Tổng Poisson $\\lambda=2$ và $\\lambda=3$ độc lập có $P(5)$ bằng bao nhiêu?||What is $P(5)$ for the sum of independent Poissons with $\\lambda=2$ and $\\lambda=3$?⟧",
             opts=["{{po_add}}", "0.2240", "0.0842", "0.1494"], explain="⟦Bằng Poisson $\\lambda=5$ tại 5: {{po_add}}.||Equal to the Poisson $\\lambda=5$ at 5: {{po_add}}.⟧"),
        dict(q="⟦Nhị thức $n=1000$, $p=0.003$ tại $k=2$ gần Poisson $\\lambda=3$ bằng bao nhiêu?||The binomial $n=1000$, $p=0.003$ at $k=2$ is close to the Poisson $\\lambda=3$ value; what is it?⟧",
             opts=["{{po_pois}}", "0.1494", "0.1000", "0.3000"], explain="⟦Nhị thức {{po_bin}}, Poisson {{po_pois}}, lệch {{po_dev}}.||Binomial {{po_bin}}, Poisson {{po_pois}}, difference {{po_dev}}.⟧"),
        dict(q="⟦Phương sai của phân bố đều trên $[2,8]$ bằng bao nhiêu?||What is the variance of the uniform distribution on $[2,8]$?⟧",
             opts=["{{un_var}}", "1.5000", "6.0000", "0.5000"], explain="⟦$(b-a)^2/12=36/12$ = {{un_var}}.||$(b-a)^2/12=36/12$ = {{un_var}}.⟧"),
        dict(q="⟦$P(Y>4)$ với $Y\\sim N(3,4)$ bằng bao nhiêu?||What is $P(Y>4)$ for $Y\\sim N(3,4)$?⟧",
             opts=["{{n_ex25}}", "0.6915", "0.1587", "0.5000"], explain="⟦$Q(1/2)$ = {{n_ex25}}.||$Q(1/2)$ = {{n_ex25}}.⟧"),
        dict(q="⟦$P(2<Y<5)$ với $Y\\sim N(3,4)$ bằng bao nhiêu?||What is $P(2<Y<5)$ for $Y\\sim N(3,4)$?⟧",
             opts=["{{n_ex25b}}", "0.5586", "0.3413", "0.8413"], explain="⟦$I(1)-I(-1/2)$ = {{n_ex25b}}.||$I(1)-I(-1/2)$ = {{n_ex25b}}.⟧"),
        dict(q="⟦$Q(4)$ bằng bao nhiêu?||What is $Q(4)$?⟧",
             opts=["{{n_q4}}", "3.4000e-05", "1.0000e-04", "6.3000e-05"], explain="⟦{{n_q4}}, còn xấp xỉ $e^{-x^2/2}/(x\\sqrt{2\\pi})$ cho {{n_q4a}}.||{{n_q4}}, while the approximation $e^{-x^2/2}/(x\\sqrt{2\\pi})$ gives {{n_q4a}}.⟧"),
        dict(q="⟦Bài 2.11: xác suất ít nhất 40 thành công trong 200 lần ($p=1/6$) bằng bao nhiêu (chính xác)?||Problem 2.11: what is the exact probability of at least 40 successes in 200 trials ($p=1/6$)?⟧",
             opts=["{{c211_ex}}", "0.1500", "0.0500", "0.2000"], explain="⟦Chính xác {{c211_ex}}, xấp xỉ chuẩn có hiệu chỉnh {{c211_n}}.||Exact {{c211_ex}}, normal approximation with correction {{c211_n}}.⟧"),
        dict(q="⟦Bài 2.12: $P(S>5)$ với $S$ Poisson $\\lambda=3.2$ bằng bao nhiêu (chính xác)?||Problem 2.12: what is $P(S>5)$ for a Poisson $S$ with $\\lambda=3.2$ (exact)?⟧",
             opts=["{{c212_ex}}", "0.2000", "0.0500", "0.5000"], explain="⟦Chính xác {{c212_ex}}, xấp xỉ chuẩn {{c212_n}}.||Exact {{c212_ex}}, normal approximation {{c212_n}}.⟧"),
        dict(q="⟦$P(X\\ge x_1+x_2\\mid X>x_1)$ với mũ $\\alpha=2$, $x_1=0.5$, $x_2=0.7$ bằng bao nhiêu?||What is $P(X\\ge x_1+x_2\\mid X>x_1)$ for the exponential with $\\alpha=2$, $x_1=0.5$, $x_2=0.7$?⟧",
             opts=["{{ex_mem}}", "0.1353", "0.3679", "0.4966"], explain="⟦$e^{-\\alpha x_2}=e^{-1.4}$ = {{ex_mem}}, không phụ thuộc $x_1$.||$e^{-\\alpha x_2}=e^{-1.4}$ = {{ex_mem}}, independent of $x_1$.⟧"),
        dict(q="⟦Phương sai của Laplace $\\frac12e^{-|x|}$ bằng bao nhiêu?||What is the variance of the Laplace $\\frac12e^{-|x|}$?⟧",
             opts=["{{la_var}}", "1.0000", "0.5000", "4.0000"], explain="⟦$2/\\alpha^2$ = {{la_var}}.||$2/\\alpha^2$ = {{la_var}}.⟧"),
        dict(q="⟦Trung bình và phương sai của gamma $G(3,2)$ là bao nhiêu (phương sai)?||What is the variance of the gamma $G(3,2)$?⟧",
             opts=["{{ga_var}}", "6.0000", "18.000", "9.0000"], explain="⟦$\\alpha\\beta^2$ = {{ga_var}}; trung bình {{ga_mean}}.||$\\alpha\\beta^2$ = {{ga_var}}; mean {{ga_mean}}.⟧"),
        dict(q="⟦Phương sai của beta $(2,5)$ bằng bao nhiêu?||What is the variance of the beta $(2,5)$?⟧",
             opts=["{{be_var}}", "0.2857", "0.0500", "0.1020"], explain="⟦$10/(49\\cdot8)$ = {{be_var}}; trung bình {{be_mean}}.||$10/(49\\cdot8)$ = {{be_var}}; mean {{be_mean}}.⟧"),
        dict(q="⟦Phương sai của chi bình phương 4 bậc bằng bao nhiêu?||What is the variance of a chi-square with 4 degrees of freedom?⟧",
             opts=["{{chi_var}}", "4.0000", "16.000", "2.0000"], explain="⟦$2n$ = {{chi_var}}; trung bình {{chi_mean}}.||$2n$ = {{chi_var}}; mean {{chi_mean}}.⟧"),
        dict(q="⟦Phương sai của chi bình phương không tâm ($n=3$, $\\sigma=1$, $\\lambda=5$) bằng bao nhiêu?||What is the variance of a noncentral chi-square ($n=3$, $\\sigma=1$, $\\lambda=5$)?⟧",
             opts=["{{nc_var}}", "6.0000", "8.0000", "16.000"], explain="⟦$2n\\sigma^4+4\\sigma^2\\lambda=6+20$ = {{nc_var}}; trung bình {{nc_mean}}.||$2n\\sigma^4+4\\sigma^2\\lambda=6+20$ = {{nc_var}}; mean {{nc_mean}}.⟧"),
        dict(q="⟦Trung bình của Rayleigh $\\sigma=1$ bằng bao nhiêu?||What is the mean of a Rayleigh with $\\sigma=1$?⟧",
             opts=["{{ray_mean}}", "1.0000", "0.8862", "1.7725"], explain="⟦$\\sqrt{\\pi/2}$ = {{ray_mean}}; phương sai {{ray_var}}.||$\\sqrt{\\pi/2}$ = {{ray_mean}}; variance {{ray_var}}.⟧"),
        dict(q="⟦$F_Y(\\sigma)$ của Rayleigh bằng bao nhiêu?||What is $F_Y(\\sigma)$ for the Rayleigh?⟧",
             opts=["{{ray_F1}}", "0.6321", "0.5000", "0.3679"], explain="⟦$1-e^{-1/2}$ = {{ray_F1}}, khớp hình 2.9.||$1-e^{-1/2}$ = {{ray_F1}}, matching Fig. 2.9.⟧"),
        dict(q="⟦Phương sai của $Y=a+bX^2$ ($b=2$, $X$ Rayleigh $\\sigma=1$) bằng bao nhiêu?||What is the variance of $Y=a+bX^2$ ($b=2$, $X$ Rayleigh $\\sigma=1$)?⟧",
             opts=["{{ray_vy}}", "8.0000", "4.0000", "32.000"], explain="⟦$4b^2\\sigma^4$ = {{ray_vy}}.||$4b^2\\sigma^4$ = {{ray_vy}}.⟧"),
        dict(q="⟦$F_R(2)$ của Rice với $m_1=m_2=1$, $\\sigma=1$ bằng bao nhiêu?||What is $F_R(2)$ of the Rice with $m_1=m_2=1$, $\\sigma=1$?⟧",
             opts=["{{rice_F}}", "0.8647", "0.6321", "0.3935"], explain="⟦$1-Q_1(\\sqrt2,2)$ = {{rice_F}}; trung bình {{rice_mean}}.||$1-Q_1(\\sqrt2,2)$ = {{rice_F}}; mean {{rice_mean}}.⟧"),
        dict(q="⟦Trung bình của Maxwell $\\sigma=1$ bằng bao nhiêu?||What is the mean of a Maxwell with $\\sigma=1$?⟧",
             opts=["{{mx_mean}}", "1.2533", "1.7725", "1.0000"], explain="⟦$2\\sqrt{2/\\pi}$ = {{mx_mean}}; phương sai {{mx_var}}.||$2\\sqrt{2/\\pi}$ = {{mx_mean}}; variance {{mx_var}}.⟧"),
        dict(q="⟦Phương sai của Student $t$ với 5 bậc bằng bao nhiêu?||What is the variance of Student's $t$ with 5 degrees of freedom?⟧",
             opts=["{{t_var}}", "1.0000", "5.0000", "1.2500"], explain="⟦$n/(n-2)$ = {{t_var}}.||$n/(n-2)$ = {{t_var}}.⟧"),
        dict(q="⟦Trung bình của phân bố $F$ với $(4,10)$ bậc bằng bao nhiêu?||What is the mean of an $F$ distribution with $(4,10)$ degrees?⟧",
             opts=["{{f_mean}}", "1.0000", "0.4000", "2.5000"], explain="⟦$n_2/(n_2-2)$ = {{f_mean}}.||$n_2/(n_2-2)$ = {{f_mean}}.⟧"),
        dict(q="⟦$P(|\\bar X_{100}|<1)$ của Cauchy chuẩn bằng bao nhiêu?||What is $P(|\\bar X_{100}|<1)$ for the standard Cauchy?⟧",
             opts=["{{cau_100}}", "0.9900", "0.9545", "0.7500"], explain="⟦Trung bình mẫu vẫn Cauchy chuẩn: {{cau_100}}; với chuẩn tắc {{cau_n100}}.||The sample mean is still standard Cauchy: {{cau_100}}; for a standard normal {{cau_n100}}.⟧"),
        dict(q="⟦Trung bình có điều kiện $E[X_2\\mid X_1=2]$ với $m=(1,-1)$, $\\sigma=(1,2)$, $\\rho=0.6$ bằng bao nhiêu?||What is $E[X_2\\mid X_1=2]$ for $m=(1,-1)$, $\\sigma=(1,2)$, $\\rho=0.6$?⟧",
             opts=["{{bg_cm}}", "1.2000", "-1.0000", "0.6000"], explain="⟦$-1+0.6\\cdot2\\cdot1$ = {{bg_cm}}; phương sai điều kiện {{bg_cv}}.||$-1+0.6\\cdot2\\cdot1$ = {{bg_cm}}; conditional variance {{bg_cv}}.⟧"),
        dict(q="⟦Phương sai điều kiện $\\text{var}[X_2\\mid X_1]$ với $\\sigma_2=2$, $\\rho=0.6$ bằng bao nhiêu?||What is the conditional variance $\\text{var}[X_2\\mid X_1]$ with $\\sigma_2=2$, $\\rho=0.6$?⟧",
             opts=["{{bg_cv}}", "4.0000", "1.4400", "2.0000"], explain="⟦$\\sigma_2^2(1-\\rho^2)=4\\cdot0.64$ = {{bg_cv}}.||$\\sigma_2^2(1-\\rho^2)=4\\cdot0.64$ = {{bg_cv}}.⟧"),
        dict(q="⟦Trị riêng lớn của ma trận hiệp phương sai $C$ ($\\sigma=(1,2)$, $\\rho=0.6$) bằng bao nhiêu?||What is the larger eigenvalue of the covariance matrix $C$ ($\\sigma=(1,2)$, $\\rho=0.6$)?⟧",
             opts=["{{bg_sv}}", "4.0000", "5.0000", "2.5000"], explain="⟦$2.5+\\sqrt{2.25+1.44}$ = {{bg_sv}}; nhỏ {{bg_su}}.||$2.5+\\sqrt{2.25+1.44}$ = {{bg_sv}}; the smaller {{bg_su}}.⟧"),
        dict(q="⟦Trung bình của Weibull $b=3$, $a=1$ bằng bao nhiêu?||What is the mean of the Weibull with $b=3$, $a=1$?⟧",
             opts=["{{wb_m3}}", "1.0000", "0.7500", "1.2533"], explain="⟦$\\Gamma(4/3)$ = {{wb_m3}}; phương sai {{wb_v3}}.||$\\Gamma(4/3)$ = {{wb_m3}}; variance {{wb_v3}}.⟧"),
        dict(q="⟦Trung bình của log-chuẩn $x_m=1$, $\\sigma=0.5$ bằng bao nhiêu?||What is the mean of the log-normal with $x_m=1$, $\\sigma=0.5$?⟧",
             opts=["{{ln_mean}}", "1.0000", "1.2840", "0.8825"], explain="⟦$e^{\\sigma^2/2}=e^{0.125}$ = {{ln_mean}}; phương sai {{ln_var}}.||$e^{\\sigma^2/2}=e^{0.125}$ = {{ln_mean}}; variance {{ln_var}}.⟧"),
        dict(q="⟦$f_X(1)$ của phân bố K với $b=1$, $\\nu=2$ bằng bao nhiêu?||What is $f_X(1)$ of the K distribution with $b=1$, $\\nu=2$?⟧",
             opts=["{{k_f1}}", "0.7358", "0.4000", "1.0000"], explain="⟦$4K_1(2)$ = {{k_f1}}, bằng tích phân hợp thành; $E[X^2]$ = {{k_e2}}.||$4K_1(2)$ = {{k_f1}}, equal to the compound integral; $E[X^2]$ = {{k_e2}}.⟧"),
        dict(q="⟦Phân bố nào là gamma với $\\alpha=n/2$, $\\beta=2\\sigma^2$?||Which distribution is a gamma with $\\alpha=n/2$, $\\beta=2\\sigma^2$?⟧",
             opts=["⟦Chi bình phương $n$ bậc||Chi-square with $n$ degrees⟧",
                   "⟦Rayleigh, vì nó là căn của tổng hai bình phương chuẩn||Rayleigh, since it is the root of a sum of two squared normals⟧",
                   "⟦Student $t$, vì nó là tỉ số của chuẩn và căn của chi bình phương||Student's $t$, since it is the ratio of a normal to the root of a chi-square⟧",
                   "⟦Nakagami với $m=1$, vì tham số $m$ đóng vai trò của $\\alpha$||Nakagami with $m=1$, since the parameter $m$ plays the role of $\\alpha$⟧"],
             explain="⟦Barkat, tr. 101 đến 106 (và tr. 113): chi bình phương là gamma đặc biệt.||Barkat, pp. 101 to 106 (and p. 113): chi-square is a special gamma.⟧"),
        dict(q="⟦Hai biến Gauss chung không tương quan thì sao?||What of two jointly Gaussian variables that are uncorrelated?⟧",
             opts=["⟦Chúng độc lập||They are independent⟧",
                   "⟦Chúng vẫn có thể phụ thuộc, như ví dụ nửa đĩa của chương 1||They can still be dependent, as in the half-disc example of chapter 1⟧",
                   "⟦Mật độ chung không còn là Gauss vì mất số hạng chéo||The joint density is no longer Gaussian since the cross term is lost⟧",
                   "⟦Phân bố điều kiện có phương sai bằng 0 do hai biến cùng hướng||The conditional distribution has zero variance since the two variables are aligned⟧"],
             explain="⟦Barkat, tr. 124: mật độ chung phân tích thành tích các mật độ biên; ma trận hiệp phương sai đường chéo là điều kiện cần và đủ.||Barkat, p. 124: the joint density factors into the marginals; a diagonal covariance matrix is necessary and sufficient.⟧"),
        dict(q="⟦Vì sao phân bố Cauchy vi phạm luật số lớn?||Why does the Cauchy distribution violate the law of large numbers?⟧",
             opts=["⟦Không có trung bình hữu hạn nên trung bình mẫu không co lại||It has no finite mean so the sample mean does not shrink⟧",
                   "⟦Vì phương sai của nó nhỏ hơn 1 nên tổng không hội tụ theo Tchebycheff||Because its variance is below 1 so the sum does not converge by Chebyshev⟧",
                   "⟦Vì các biến Cauchy luôn phụ thuộc lẫn nhau khi lấy từ cùng một mẫu||Because Cauchy variables drawn from the same sample are always dependent⟧",
                   "⟦Vì hàm đặc trưng $e^{-\\beta|\\omega|}$ không khả vi tại mọi tần số||Because the characteristic function $e^{-\\beta|\\omega|}$ is nondifferentiable at every frequency⟧"],
             explain="⟦Barkat, tr. 120: chỉ hàm đặc trưng không khả vi tại 0; tổng Cauchy là Cauchy, vậy trung bình mẫu không co lại ({{cau_1}} rồi {{cau_100}}).||Barkat, p. 120: the characteristic function is nondifferentiable at 0 only; a sum of Cauchy variables is Cauchy, so the sample mean does not shrink ({{cau_1}} then {{cau_100}}).⟧"),
        dict(q="⟦Weibull với $b=2$ là phân bố nào?||Which distribution is the Weibull with $b=2$?⟧",
             opts=["⟦Rayleigh, với $a=1/2\\sigma^2$||Rayleigh, with $a=1/2\\sigma^2$⟧",
                   "⟦Mũ, vì $b=2$ nhân đôi tham số của mật độ||Exponential, since $b=2$ doubles the density parameter⟧",
                   "⟦Chuẩn nửa, vì $e^{-ax^2}$ có dạng Gauss||Half-normal only, since $e^{-ax^2}$ is Gaussian in shape⟧",
                   "⟦Maxwell, vì $b=2$ ứng với hai chiều không gian||Maxwell, since $b=2$ corresponds to two spatial dimensions⟧"],
             explain="⟦Barkat, tr. 129 đến 130: $b=1$ mũ, $b=2$ Rayleigh; trung bình {{wb_rmean}}.||Barkat, pp. 129 to 130: $b=1$ exponential, $b=2$ Rayleigh; mean {{wb_rmean}}.⟧"),
        dict(q="⟦Phân bố K là tích của hai biến nào?||K is the product of which two variables?⟧",
             opts=["⟦Speckle Rayleigh và texture kiểu gamma||Rayleigh speckle and gamma-type texture⟧",
                   "⟦Hai biến Rayleigh độc lập với cùng tham số tỉ lệ||Two independent Rayleigh variables with the same scale⟧",
                   "⟦Một biến chuẩn và một biến log-chuẩn phản ánh nhiễu cộng||A normal and a log-normal variable reflecting additive noise⟧",
                   "⟦Một biến mũ và một biến Poisson mô tả số lần phản xạ||An exponential and a Poisson variable describing the number of reflections⟧"],
             explain="⟦Barkat, tr. 132 đến 135: $X=ST$.||Barkat, pp. 132 to 135: $X=ST$.⟧"),
        dict(q="⟦Khi nào biên độ của tín hiệu cộng nhiễu Gauss là Rice thay vì Rayleigh?||When is the amplitude of signal plus Gaussian noise Rice rather than Rayleigh?⟧",
             opts=["⟦Khi các thành phần vuông pha có trung bình khác 0||When the quadrature components have nonzero means⟧",
                   "⟦Khi nhiễu có phương sai lớn hơn năng lượng tín hiệu trong khung quan sát||When the noise variance exceeds the signal energy in the observation window⟧",
                   "⟦Khi hai thành phần vuông pha tương quan với nhau một cách đáng kể||When the two quadrature components are significantly correlated⟧",
                   "⟦Khi biên độ được đo qua bộ lọc thông dải thay vì trực tiếp||When the amplitude is measured through a bandpass filter instead of directly⟧"],
             explain="⟦Barkat, tr. 111 đến 113: $\\lambda=m_1^2+m_2^2\\ne0$; $\\lambda=0$ cho Rayleigh.||Barkat, pp. 111 to 113: $\\lambda=m_1^2+m_2^2\\ne0$; $\\lambda=0$ gives Rayleigh.⟧"),
    ],
    nb=[
        ("md", """## 1. ⟦Phân bố rời rạc||Discrete distributions⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Các công thức nhị thức, đa thức, hình học, Pascal, siêu bội, Poisson và giới hạn có khớp với hàm khối của thư viện và với mô phỏng?||Do the binomial, multinomial, geometric, Pascal, hypergeometric and Poisson formulas and limits agree with library mass functions and with simulation?⟧"""),
        ("code", r'''from math import comb, factorial, gamma as G, sqrt, pi, exp, log
from scipy import stats, special, integrate
rg = np.random.default_rng(11)
trap = getattr(np, "trapezoid", None) or np.trapz
# ⟦nhị thức||binomial⟧
p10 = comb(10, 2)*(1/6)**2*(5/6)**8
assert abs(p10 - stats.binom.pmf(2, 10, 1/6)) < 1e-14 and abs(np.mean(rg.binomial(10, 1/6, 400000) == 2) - p10) < 0.003
report("bi_ex21", p10, ".4f")
c2 = sum(comb(3, k)*0.8**k*0.2**(3 - k) for k in (2, 3))
assert abs(c2 - 0.896) < 1e-12 and abs(np.mean(rg.binomial(3, 0.8, 400000) >= 2) - c2) < 0.003
report("bi_ex22", c2, ".3f")
report("bi_mean", 10/6, ".4f"); report("bi_var", 10*(1/6)*(5/6), ".4f")
assert abs(stats.binom.var(10, 1/6) - 10*(1/6)*(5/6)) < 1e-14
# ⟦đa thức||multinomial⟧
mn = factorial(10)/(factorial(2)*factorial(3)*factorial(5))*0.2**2*0.3**3*0.5**5
assert abs(mn - stats.multinomial.pmf([2, 3, 5], 10, [0.2, 0.3, 0.5])) < 1e-14
report("mn_p", mn, ".4f")
# ⟦hình học, Pascal||geometric, Pascal⟧
pg = (5/6)**2*(1/6)
assert abs(pg - stats.geom.pmf(3, 1/6)) < 1e-14
kk = np.arange(1, 4000); gm = np.sum(kk*(5/6)**(kk - 1)/6); gv = np.sum(kk**2*(5/6)**(kk - 1)/6) - gm**2
assert abs(gm - 6) < 1e-9 and abs(gv - 30) < 1e-6
report("ge_p3", pg, ".4f"); report("ge_mean", gm, ".0f"); report("ge_var", gv, ".0f")
pp = comb(4, 2)*0.5**3*0.5**2
assert abs(pp - stats.nbinom.pmf(2, 3, 0.5)) < 1e-14          # ⟦nbinom: số thất bại x = k − r||nbinom: number of failures x = k − r⟧
report("pa_p", pp, ".4f")
n_, r_, p_ = 10, 3, 0.3
lhs = stats.binom.sf(r_ - 1, n_, p_); rhs = stats.nbinom.cdf(n_ - r_, r_, p_)
assert abs(lhs - rhs) < 1e-14
report("pa_rel", lhs, ".4f")
# ⟦siêu bội||hypergeometric⟧
hy = comb(5, 3)*comb(6, 4)/comb(11, 7)
assert abs(hy - stats.hypergeom.pmf(3, 11, 5, 7)) < 1e-14 and abs(hy - 5/11) < 1e-14
hv = 7*5*6*4/(121*10)
assert abs(stats.hypergeom.var(11, 5, 7) - hv) < 1e-12
report("hy_p", hy, ".4f"); report("hy_var", hv, ".4f")
hd = abs(stats.hypergeom.pmf(3, 10000, 3000, 10) - stats.binom.pmf(3, 10, 0.3))
assert hd < 1e-3
report("hy_dev", hd, ".1e")
# ⟦Poisson||Poisson⟧
lam = 3.0
ms = lam**2 + lam
kk = np.arange(0, 80); pm = stats.poisson.pmf(kk, lam)
assert abs(np.sum(kk**2*pm) - ms) < 1e-9
report("po_ms", ms, ".0f")
conv = np.convolve(stats.poisson.pmf(np.arange(0, 60), 2), stats.poisson.pmf(np.arange(0, 60), 3))[5]
assert abs(conv - stats.poisson.pmf(5, 5)) < 1e-12
report("po_add", conv, ".4f")
pb = stats.binom.pmf(2, 1000, 0.003); pw = stats.poisson.pmf(2, 3.0)
assert abs(pb - pw) < 5e-3 and abs(pb - comb(1000, 2)*0.003**2*0.997**998) < 1e-14
report("po_bin", pb, ".4f"); report("po_pois", pw, ".4f"); report("po_dev", abs(pb - pw), ".1e")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Nhị thức: {{bi_ex21}}, {{bi_ex22}}, trung bình {{bi_mean}}, phương sai {{bi_var}}; đa thức {{mn_p}}. Hình học: {{ge_p3}}, {{ge_mean}}, {{ge_var}}; Pascal {{pa_p}}, quan hệ {{pa_rel}}. Siêu bội: {{hy_p}}, {{hy_var}}, lệch tới nhị thức {{hy_dev}}. Poisson: {{po_ms}}, cộng {{po_add}}; nhị thức {{po_bin}} so với {{po_pois}} (lệch {{po_dev}}).||Binomial: {{bi_ex21}}, {{bi_ex22}}, mean {{bi_mean}}, variance {{bi_var}}; multinomial {{mn_p}}. Geometric: {{ge_p3}}, {{ge_mean}}, {{ge_var}}; Pascal {{pa_p}}, relation {{pa_rel}}. Hypergeometric: {{hy_p}}, {{hy_var}}, deviation from binomial {{hy_dev}}. Poisson: {{po_ms}}, sum {{po_add}}; binomial {{po_bin}} against {{po_pois}} (difference {{po_dev}}).⟧"""),
        ("md", """## 2. ⟦Đều, chuẩn, mũ, gamma, beta||Uniform, normal, exponential, gamma, beta⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Các ví dụ 2.5, bài 2.11, 2.12 và các công thức mômen cho đều, mũ, Laplace, gamma, beta có đúng, và xấp xỉ chuẩn tốt cỡ nào?||Are examples 2.5, problems 2.11, 2.12 and the moment formulas for uniform, exponential, Laplace, gamma and beta right, and how good is the normal approximation?⟧"""),
        ("code", r'''# ⟦đều||uniform⟧
a_, b_ = 2.0, 8.0
uv = integrate.quad(lambda x: (x - 5)**2/(b_ - a_), a_, b_)[0]
assert abs(uv - 3) < 1e-12
report("un_var", uv, ".0f")
# ⟦chuẩn||normal⟧
Qf = lambda x: 0.5*special.erfc(x/np.sqrt(2))
assert abs(Qf(0.5) - stats.norm.sf(0.5)) < 1e-15
p1 = Qf(0.5); p2 = stats.norm.cdf(1.0) - stats.norm.cdf(-0.5)
assert abs(p1 - stats.norm.sf(4, 3, 2)) < 1e-15 and abs(p2 - (stats.norm.cdf(5, 3, 2) - stats.norm.cdf(2, 3, 2))) < 1e-15
Ys = rg.normal(3, 2, 1000000)
assert abs(np.mean(Ys > 4) - p1) < 3e-3 and abs(np.mean((Ys > 2) & (Ys < 5)) - p2) < 3e-3
report("n_ex25", p1, ".4f"); report("n_ex25b", p2, ".4f")
q4 = Qf(4.0); q4a = np.exp(-8)/(4*np.sqrt(2*np.pi))
assert abs(q4 - stats.norm.sf(4)) < 1e-18 and 0.9 < q4a/q4 < 1.1
report("n_q4", q4, ".3e"); report("n_q4a", q4a, ".3e")
m4 = integrate.quad(lambda x: x**4*stats.norm.pdf(x), -12, 12)[0]
assert abs(m4 - 3) < 1e-8 and abs(factorial(4)/(factorial(2)*2**2) - 3) < 1e-14
report("n_m4", m4, ".0f")
# ⟦bài 2.11, 2.12||problems 2.11, 2.12⟧
ex211 = stats.binom.sf(39, 200, 1/6)
mu, sd = 200/6, np.sqrt(200*(1/6)*(5/6))
nap211 = stats.norm.sf((39.5 - mu)/sd)
mc211 = np.mean(rg.binomial(200, 1/6, 1000000) >= 40)
assert abs(ex211 - mc211) < 2e-3 and abs(ex211 - nap211) < 0.02
report("c211_ex", ex211, ".4f"); report("c211_n", nap211, ".4f")
ex212 = stats.poisson.sf(5, 3.2)
nap212 = stats.norm.sf((5.5 - 3.2)/np.sqrt(3.2))
mc212 = np.mean(rg.poisson(0.032, (200000, 100)).sum(axis=1) > 5)
assert abs(ex212 - mc212) < 3e-3 and abs(ex212 - nap212) < 0.03
report("c212_ex", ex212, ".4f"); report("c212_n", nap212, ".4f")
# ⟦mũ, không nhớ; Laplace||exponential, memoryless; Laplace⟧
al, x1, x2 = 2.0, 0.5, 0.7
lhs = np.exp(-al*(x1 + x2))/np.exp(-al*x1); rhs = np.exp(-al*x2)
assert abs(lhs - rhs) < 1e-15
Ex = rg.exponential(1/al, 2000000)
assert abs(np.mean(Ex[Ex > x1] >= x1 + x2) - rhs) < 3e-3
report("ex_mem", rhs, ".4f")
lv = integrate.quad(lambda x: x*x*0.5*np.exp(-abs(x)), -60, 60, points=[0])[0]
assert abs(lv - 2) < 1e-8
report("la_var", lv, ".0f")
# ⟦gamma, beta||gamma, beta⟧
gm = integrate.quad(lambda x: x*stats.gamma.pdf(x, 3, scale=2), 0, np.inf)[0]
gv = integrate.quad(lambda x: x*x*stats.gamma.pdf(x, 3, scale=2), 0, np.inf)[0] - gm**2
assert abs(gm - 6) < 1e-8 and abs(gv - 12) < 1e-6 and abs(G(0.5)**2 - pi) < 1e-12
report("ga_mean", gm, ".0f"); report("ga_var", gv, ".0f"); report("ga_half", G(0.5), ".4f")
Bf = G(2)*G(5)/G(7)
bm = integrate.quad(lambda x: x*x**1*(1 - x)**4/Bf, 0, 1)[0]; bv = integrate.quad(lambda x: x*x*x**1*(1 - x)**4/Bf, 0, 1)[0] - bm**2
Bs = rg.beta(2, 5, 1000000)
assert abs(Bf - special.beta(2, 5)) < 1e-14 and abs(bm - 2/7) < 1e-9 and abs(bv - 10/(49*8)) < 1e-9 and abs(np.var(Bs) - bv) < 2e-4
report("be_mean", bm, ".4f"); report("be_var", bv, ".4f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Đều: {{un_var}}. Chuẩn: {{n_ex25}}, {{n_ex25b}}, $Q(4)$ = {{n_q4}} (xấp xỉ {{n_q4a}}), $E[X^4]$ = {{n_m4}}. Bài 2.11: {{c211_ex}} và {{c211_n}}; bài 2.12: {{c212_ex}} và {{c212_n}}. Mũ: {{ex_mem}}; Laplace {{la_var}}; gamma {{ga_mean}}, {{ga_var}}, $\\Gamma(1/2)$ = {{ga_half}}; beta {{be_mean}}, {{be_var}}.||Uniform: {{un_var}}. Normal: {{n_ex25}}, {{n_ex25b}}, $Q(4)$ = {{n_q4}} (approximation {{n_q4a}}), $E[X^4]$ = {{n_m4}}. Problem 2.11: {{c211_ex}} and {{c211_n}}; problem 2.12: {{c212_ex}} and {{c212_n}}. Exponential: {{ex_mem}}; Laplace {{la_var}}; gamma {{ga_mean}}, {{ga_var}}, $\\Gamma(1/2)$ = {{ga_half}}; beta {{be_mean}}, {{be_var}}.⟧"""),
        ("md", """## 3. ⟦Chi bình phương, Rayleigh, Rice, Maxwell, Nakagami, Student, Cauchy||Chi-square, Rayleigh, Rice, Maxwell, Nakagami, Student, Cauchy⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Chuỗi biến đổi từ biến chuẩn có cho đúng các phân bố và tham số, kể cả hàm Marcum của Rice, Nakagami từ mômen, và tính bất thường của Cauchy? Mỗi số kiểm bằng mô phỏng và bằng tích phân hoặc công thức.||Does the chain of transformations of normal variables give the right distributions and parameters, including the Marcum function of the Rice, Nakagami from moments, and the pathology of the Cauchy? Each number is checked by simulation and by integration or formula.⟧"""),
        ("code", r'''# ⟦chi bình phương||chi-square⟧
Z = rg.standard_normal((1000000, 4))
X2 = (Z**2).sum(axis=1)
assert abs(np.mean(X2) - 4) < 0.02 and abs(np.var(X2) - 8) < 0.1 and abs(stats.gamma.var(2, scale=2) - 8) < 1e-12
report("chi_mean", stats.chi2.mean(4), ".0f"); report("chi_var", stats.chi2.var(4), ".0f")
# ⟦không tâm n = 3, σ = 1, λ = 5||noncentral n = 3, σ = 1, λ = 5⟧
mvec = np.array([np.sqrt(5), 0, 0])
Xn = ((rg.standard_normal((1000000, 3)) + mvec)**2).sum(axis=1)
assert abs(np.mean(Xn) - 8) < 0.03 and abs(np.var(Xn) - 26) < 0.4 and abs(stats.ncx2.mean(3, 5) - 8) < 1e-12 and abs(stats.ncx2.var(3, 5) - 26) < 1e-12
report("nc_mean", 8, ".0f"); report("nc_var", 26, ".0f")
# ⟦Rayleigh σ = 1||Rayleigh σ = 1⟧
Rr = np.sqrt((rg.standard_normal((1000000, 2))**2).sum(axis=1))
rmn = integrate.quad(lambda y: y*y*np.exp(-y*y/2), 0, np.inf)[0]; rvv = integrate.quad(lambda y: y**3*np.exp(-y*y/2), 0, np.inf)[0] - rmn**2
assert abs(rmn - np.sqrt(np.pi/2)) < 1e-9 and abs(rvv - (2 - np.pi/2)) < 1e-9 and abs(np.mean(Rr) - rmn) < 3e-3
report("ray_mean", rmn, ".4f"); report("ray_var", rvv, ".4f"); report("ray_F1", 1 - np.exp(-0.5), ".4f")
assert abs(np.mean(Rr <= 1) - (1 - np.exp(-0.5))) < 3e-3
vy = np.var(2*Rr**2)
assert abs(vy - 16) < 0.4 and abs(stats.expon.var(scale=2)*4 - 16) < 1e-12        # ⟦X² ~ mũ trung bình 2σ²||X² ~ exponential mean 2σ²⟧
report("ray_vy", 16, ".0f")
polar = integrate.dblquad(lambda r, th: r*np.exp(-r*r/2)/(2*np.pi), 0, 2*np.pi, 0, 2)[0]
assert abs(polar - (1 - np.exp(-2))) < 1e-9 and abs(np.mean(Rr <= 2) - polar) < 3e-3
report("ray_polar", polar, ".4f"); report("ray_tail", np.exp(-0.5), ".4f")
# ⟦Rice m1 = m2 = 1, σ = 1, λ = 2||Rice m1 = m2 = 1, σ = 1, λ = 2⟧
lam = 2.0
Rc = np.sqrt(((rg.standard_normal((1000000, 2)) + 1.0)**2).sum(axis=1))
f_rice = lambda r: r*np.exp(-(r - np.sqrt(lam))**2/2)*special.i0e(np.sqrt(lam)*r)
F_int = integrate.quad(f_rice, 0, 2)[0]
F_ncx = stats.ncx2.cdf(4.0, 2, lam)                       # ⟦P(R ≤ 2) = P(R² ≤ 4), R² ~ ncx2(2, λ)||P(R ≤ 2) = P(R² ≤ 4), R² ~ ncx2(2, λ)⟧
F_rice = stats.rice.cdf(2.0, np.sqrt(lam))
assert abs(F_int - F_ncx) < 1e-9 and abs(F_int - F_rice) < 1e-9 and abs(np.mean(Rc <= 2) - F_int) < 3e-3
Emean = integrate.quad(lambda r: r*f_rice(r), 0, 60)[0]
assert abs(Emean - np.mean(Rc)) < 5e-3
report("rice_F", F_int, ".4f"); report("rice_mean", Emean, ".4f")
# ⟦Maxwell σ = 1||Maxwell σ = 1⟧
Mx = np.sqrt((rg.standard_normal((1000000, 3))**2).sum(axis=1))
fm = lambda y: np.sqrt(2/np.pi)*y*y*np.exp(-y*y/2)
mm = integrate.quad(lambda y: y*fm(y), 0, np.inf)[0]; mv = integrate.quad(lambda y: y*y*fm(y), 0, np.inf)[0] - mm**2
assert abs(mm - 2*np.sqrt(2/np.pi)) < 1e-9 and abs(mv - (3 - 8/np.pi)) < 1e-9 and abs(np.mean(Mx) - mm) < 4e-3
report("mx_mean", mm, ".4f"); report("mx_var", mv, ".4f")
# ⟦Nakagami m = 2, v = 1: X² ~ gamma(m, v/m)||Nakagami m = 2, v = 1: X² ~ gamma(m, v/m)⟧
mN, vN = 2.0, 1.0
Xk = np.sqrt(rg.gamma(mN, vN/mN, 1000000))
v_hat = np.mean(Xk**2); m_hat = v_hat**2/np.var(Xk**2)
fN = lambda x: 2/G(mN)*(mN/vN)**mN*x**(2*mN - 1)*np.exp(-mN*x*x/vN)
assert abs(integrate.quad(fN, 0, np.inf)[0] - 1) < 1e-9 and abs(m_hat - 2) < 0.05 and abs(v_hat - 1) < 3e-3
assert abs(stats.nakagami.mean(mN, scale=np.sqrt(vN)) - np.mean(Xk)) < 3e-3
report("nk_m", m_hat, ".2f"); report("nk_v", v_hat, ".2f"); report("nk_int", integrate.quad(fN, 0, np.inf)[0], ".0f")
# ⟦Student, F, Cauchy||Student, F, Cauchy⟧
tS = rg.standard_normal(1000000)/np.sqrt(rg.chisquare(5, 1000000)/5)
assert abs(np.var(tS[np.abs(tS) < 200]) - 5/3) < 0.1 and abs(stats.t.var(5) - 5/3) < 1e-12
report("t_var", 5/3, ".4f")
Fs = (rg.chisquare(4, 1000000)/4)/(rg.chisquare(10, 1000000)/10)
assert abs(np.mean(Fs) - 1.25) < 0.02 and abs(stats.f.mean(4, 10) - 1.25) < 1e-12
report("f_mean", 1.25, ".2f")
t1 = stats.t.cdf(1, 1) - stats.t.cdf(-1, 1); assert abs(t1 - 0.5) < 1e-12 and abs(t1 - (stats.cauchy.cdf(1) - stats.cauchy.cdf(-1))) < 1e-12
report("t1_p", t1, ".2f")
def prob_mean(n):
    xs = rg.standard_cauchy((100000, n)).mean(axis=1); return np.mean(np.abs(xs) < 1)
assert abs(prob_mean(1) - 0.5) < 5e-3 and abs(prob_mean(100) - 0.5) < 5e-3
pn = np.mean(np.abs(rg.standard_normal((100000, 100)).mean(axis=1)) < 1)
assert pn > 0.999
report("cau_1", 0.5, ".2f"); report("cau_100", 0.5, ".2f"); report("cau_n100", stats.norm.cdf(10) - stats.norm.cdf(-10), ".0f")
csum = rg.standard_cauchy((1000000, 2)).sum(axis=1)
assert abs(np.mean(np.abs(csum) < 2) - 0.5) < 3e-3 and abs(stats.cauchy.cdf(2, scale=2) - stats.cauchy.cdf(-2, scale=2) - 0.5) < 1e-12
report("cau_sum", 0.5, ".2f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Chi bình phương: {{chi_mean}}, {{chi_var}}; không tâm {{nc_mean}}, {{nc_var}}. Rayleigh: {{ray_mean}}, {{ray_var}}, $F(\\sigma)$ = {{ray_F1}}, $Y=2X^2$: {{ray_vy}}, cực: {{ray_polar}}. Rice: $F_R(2)$ = {{rice_F}}, trung bình {{rice_mean}}. Maxwell: {{mx_mean}}, {{mx_var}}. Nakagami: $m$ = {{nk_m}}, $v$ = {{nk_v}}. $t_5$: {{t_var}}; $F$: {{f_mean}}; Cauchy: {{cau_1}} và {{cau_100}} so với chuẩn {{cau_n100}}.||Chi-square: {{chi_mean}}, {{chi_var}}; noncentral {{nc_mean}}, {{nc_var}}. Rayleigh: {{ray_mean}}, {{ray_var}}, $F(\\sigma)$ = {{ray_F1}}, $Y=2X^2$: {{ray_vy}}, polar: {{ray_polar}}. Rice: $F_R(2)$ = {{rice_F}}, mean {{rice_mean}}. Maxwell: {{mx_mean}}, {{mx_var}}. Nakagami: $m$ = {{nk_m}}, $v$ = {{nk_v}}. $t_5$: {{t_var}}; $F$: {{f_mean}}; Cauchy: {{cau_1}} and {{cau_100}} against normal {{cau_n100}}.⟧"""),
        ("md", """## 4. ⟦Gauss nhiều chiều, Weibull, log-chuẩn, K||Multivariate Gaussian, Weibull, log-normal, K⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Phân bố điều kiện, elip và trị riêng của Gauss hai chiều, các mômen của Weibull và log-chuẩn, và phân bố K từ tích speckle nhân texture có đúng công thức Bessel?||Are the conditional, ellipse and eigenvalues of the bivariate Gaussian, the moments of the Weibull and log-normal, and the K distribution from speckle times texture consistent with the Bessel formula?⟧"""),
        ("code", r'''# ⟦Gauss hai chiều||bivariate Gaussian⟧
m = np.array([1.0, -1.0]); s1, s2, rho = 1.0, 2.0, 0.6
Cm = np.array([[s1**2, rho*s1*s2], [rho*s1*s2, s2**2]])
cm = m[1] + rho*s2/s1*(2.0 - m[0]); cv = s2**2*(1 - rho**2)
XY = rg.multivariate_normal(m, Cm, 4000000)
sel = np.abs(XY[:, 0] - 2.0) < 0.02
assert abs(np.mean(XY[sel, 1]) - cm) < 0.03 and abs(np.var(XY[sel, 1]) - cv) < 0.08
report("bg_cm", cm, ".1f"); report("bg_cv", cv, ".2f")
det = np.linalg.det(Cm); assert abs(det - s1**2*s2**2*(1 - rho**2)) < 1e-12
f0_scalar = 1/(2*np.pi*s1*s2*np.sqrt(1 - rho**2)); f0_matrix = stats.multivariate_normal(m, Cm).pdf(m)
assert abs(f0_scalar - f0_matrix) < 1e-14
report("bg_det", det, ".2f"); report("bg_f0", f0_scalar, ".4f")
# ⟦không tương quan ⇒ độc lập||uncorrelated ⇒ independent⟧
C0 = np.diag([s1**2, s2**2]); g0 = stats.multivariate_normal(m, C0)
grid = np.random.default_rng(3).uniform(-4, 4, (2000, 2)) + m
ind_dev = np.max(np.abs(g0.pdf(grid) - stats.norm.pdf(grid[:, 0], m[0], s1)*stats.norm.pdf(grid[:, 1], m[1], s2)))
assert ind_dev < 1e-15
report("bg_ind", max(ind_dev, 1e-17), ".0e")
# ⟦elip: công thức 2.226–2.229 và trị riêng||ellipse: formulas 2.226–2.229 and eigenvalues⟧
th = 0.5*np.arctan(2*rho*s1*s2/(s1**2 - s2**2))
su2 = (s1**2*np.cos(th)**2 - s2**2*np.sin(th)**2)/(np.cos(th)**2 - np.sin(th)**2)
sv2 = (s2**2*np.cos(th)**2 - s1**2*np.sin(th)**2)/(np.cos(th)**2 - np.sin(th)**2)
w = np.sort(np.linalg.eigvalsh(Cm))
assert abs(su2 - w[0]) < 1e-12 and abs(sv2 - w[1]) < 1e-12
report("bg_theta", np.degrees(th), ".2f"); report("bg_su", su2, ".3f"); report("bg_sv", sv2, ".3f")
# ⟦Weibull||Weibull⟧
wr = integrate.quad(lambda x: x*2*0.5*x*np.exp(-0.5*x*x), 0, np.inf)[0]
assert abs(wr - stats.weibull_min.mean(2, scale=np.sqrt(2))) < 1e-9 and abs(wr - np.sqrt(np.pi/2)) < 1e-9
w3m = G(1 + 1/3); w3v = G(1 + 2/3) - G(1 + 1/3)**2
assert abs(w3m - stats.weibull_min.mean(3)) < 1e-12 and abs(w3v - stats.weibull_min.var(3)) < 1e-12
report("wb_rmean", wr, ".4f"); report("wb_m3", w3m, ".4f"); report("wb_v3", w3v, ".4f")
# ⟦log-chuẩn||log-normal⟧
sg = 0.5
lm = np.exp(sg**2/2); lv = np.exp(sg**2)*(np.exp(sg**2) - 1)
Ln = np.exp(rg.normal(0, sg, 2000000))
assert abs(lm - stats.lognorm.mean(sg)) < 1e-12 and abs(lv - stats.lognorm.var(sg)) < 1e-12 and abs(np.mean(Ln) - lm) < 3e-3 and abs(np.var(Ln) - lv) < 1e-2
report("ln_mean", lm, ".4f"); report("ln_var", lv, ".4f")
# ⟦K: b = 1, ν = 2||K: b = 1, ν = 2⟧
b_, nu = 1.0, 2.0
fT = lambda t: 2/(b_**nu*G(nu))*t**(2*nu - 1)*np.exp(-t*t/b_**2)
fXT = lambda x, t: 2*x/t**2*np.exp(-x*x/t**2)
compound = integrate.quad(lambda t: fXT(1.0, t)*fT(t), 0, np.inf)[0]
bessel = 4/(b_*G(nu))*(1.0/b_)**nu*special.kv(nu - 1, 2*1.0/b_)
assert abs(compound - bessel) < 1e-7
tot = integrate.quad(lambda x: 4/(b_*G(nu))*(x/b_)**nu*special.kv(nu - 1, 2*x/b_), 0, np.inf)[0]
assert abs(tot - 1) < 1e-7
T = np.sqrt(rg.gamma(nu, b_**2, 2000000)); Sx = np.sqrt(rg.exponential(1.0, 2000000))*T
assert abs(np.mean(Sx**2) - nu*b_**2) < 0.03 and abs(np.mean(T**2) - nu*b_**2) < 0.03
report("k_f1", bessel, ".4f"); report("k_e2", nu*b_**2, ".0f")'''),
        ("code", r'''th_ = np.linspace(0, 2*np.pi, 300)
fig, ax = plt.subplots(figsize=(4.6, 4.4))
ax.scatter(XY[:1500, 0], XY[:1500, 1], s=3, alpha=0.35)
L = np.linalg.cholesky(Cm)
el = (L @ np.vstack([np.cos(th_), np.sin(th_)])).T + m
ax.plot(el[:, 0], el[:, 1], "r", label=("⟦elip chuẩn||standard ellipse⟧"))
ax.set_aspect("equal"); ax.legend(fontsize=8); ax.set_xlabel("x₁"); ax.set_ylabel("x₂"); plt.tight_layout(); plt.show()''', dict(fig="ellipse", cap="⟦Hình 1. Gauss hai chiều với σ = (1, 2), ρ = 0.6: đám điểm mô phỏng và elip chuẩn (đỏ) có trục lớn theo trị riêng của ma trận hiệp phương sai.||Figure 1. The bivariate Gaussian with σ = (1, 2), ρ = 0.6: simulated points and the standard ellipse (red) whose axes follow the eigenvalues of the covariance matrix.⟧")),
        ("code", r'''xs_ = np.linspace(0.01, 4, 400)
fig, ax = plt.subplots(figsize=(7.5, 3.3))
ax.semilogy(xs_, 4/(b_*G(nu))*(xs_/b_)**nu*special.kv(nu - 1, 2*xs_/b_), label=("K (ν = 2)"))
ax.semilogy(xs_, 2*xs_*np.exp(-xs_**2)*1, label=("⟦Rayleigh (cùng E[X²]=1)||Rayleigh (same E[X²]=1)⟧"))
ax.set_ylim(1e-5, 2); ax.set_xlabel("x"); ax.legend(fontsize=8); plt.tight_layout(); plt.show()''', dict(fig="kdist", cap="⟦Hình 2. Mật độ K (ν = 2, b = 1) so với Rayleigh: đuôi K nặng hơn nhiều, nên ngưỡng phát hiện cho cùng xác suất báo động giả phải cao hơn.||Figure 2. The K density (ν = 2, b = 1) against a Rayleigh: the K tail is much heavier, so the detection threshold for the same false-alarm probability must be higher.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Gauss hai chiều: trung bình điều kiện {{bg_cm}}, phương sai {{bg_cv}}, $|C|$ = {{bg_det}}, $f(m)$ = {{bg_f0}}, độc lập khi $\\rho=0$ lệch {{bg_ind}}; $\\theta$ = {{bg_theta}} độ, $\\sigma_u^2$ = {{bg_su}}, $\\sigma_v^2$ = {{bg_sv}}. Weibull: {{wb_rmean}}, {{wb_m3}}, {{wb_v3}}. Log-chuẩn: {{ln_mean}}, {{ln_var}}. K: $f(1)$ = {{k_f1}}, $E[X^2]$ = {{k_e2}}.||Bivariate Gaussian: conditional mean {{bg_cm}}, variance {{bg_cv}}, $|C|$ = {{bg_det}}, $f(m)$ = {{bg_f0}}, independence at $\\rho=0$ deviates by {{bg_ind}}; $\\theta$ = {{bg_theta}} degrees, $\\sigma_u^2$ = {{bg_su}}, $\\sigma_v^2$ = {{bg_sv}}. Weibull: {{wb_rmean}}, {{wb_m3}}, {{wb_v3}}. Log-normal: {{ln_mean}}, {{ln_var}}. K: $f(1)$ = {{k_f1}}, $E[X^2]$ = {{k_e2}}.⟧"""),
    ],
)
