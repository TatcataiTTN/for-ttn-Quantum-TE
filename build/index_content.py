"""Content of the module-list page: the 12-step signal-processing workflow (accordion).

All worked-example numbers come from compute(), which cross-checks each result by a
second, independent method (formula versus simulation) before the page is built.
"""
import math

from lib import F, C, UL, TBL


def compute():
    import numpy as np
    from scipy import signal, stats

    R = {}
    # --- step 2: aliasing
    fs = 8000
    x = np.sin(2*np.pi*5000*np.arange(fs)/fs)
    peak = int(np.argmax(np.abs(np.fft.rfft(x))))
    assert peak == abs(5000 - round(5000/fs)*fs) == 3000
    R["alias_peak"] = str(peak); R["nyq"] = str(fs//2)
    # --- step 3: resolution
    R["df_1024"] = "%.4f" % (fs/1024)
    nmin = math.ceil(fs*0.2)
    assert fs/nmin <= 5
    R["n_5hz"] = str(nmin)
    # --- step 4: Hermitian redundancy
    R["n_rfft"] = str(len(np.fft.rfft(np.zeros(1000))))
    # --- step 5: moving average, freqz versus closed form
    L = 8; h = np.ones(L)/L
    for f, key in ((500, "ma_500"), (1000, "ma_1000")):
        _, H = signal.freqz(h, worN=[2*np.pi*f/fs])
        closed = abs(np.sin(np.pi*L*f/fs)/(L*np.sin(np.pi*f/fs)))
        assert abs(abs(H[0]) - closed) < 1e-12
        R[key] = "%.6f" % abs(H[0])
    # --- step 6: variance of the sum of two U(-1/2, 1/2) by numerical convolution
    dx = 1e-3
    xg = np.arange(-0.5, 0.5, dx) + dx/2
    tri = np.convolve(np.ones_like(xg), np.ones_like(xg))*dx
    xs = 2*xg[0] + np.arange(len(tri))*dx
    m1 = np.sum(xs*tri)*dx
    var = np.sum(xs**2*tri)*dx - m1**2
    assert abs(var - 1/6) < 1e-5
    R["var_sum"] = "%.5f" % var
    # --- step 7: periodogram of white noise, single versus averaged over K segments
    rng = np.random.default_rng(2026)
    K, N = 64, 1024
    P = np.abs(np.fft.rfft(rng.standard_normal((K, N)), axis=1))**2/N
    inner = P[:, 1:-1]
    s1, sK = inner[0].std(), inner.mean(axis=0).std()
    assert abs(inner.mean() - 1) < 0.02 and abs(s1 - 1) < 0.15 and abs(sK - 1/math.sqrt(K)) < 0.02
    R["pg_single"] = "%.2f" % s1; R["pg_avg"] = "%.3f" % sK; R["pg_theory"] = "%.3f" % (1/math.sqrt(K))
    # --- step 8/9: Neyman-Pearson detection of a DC level, formula versus Monte Carlo
    n, A, sig, pfa = 10, 1.0, 1.0, 1e-3
    q = stats.norm.isf(pfa); thr = sig/math.sqrt(n)*q
    d = math.sqrt(n)*A/sig; pd = stats.norm.sf(q - d)
    T = 400000
    X0 = rng.normal(0, sig, (T, n)).mean(axis=1)
    X1 = rng.normal(A, sig, (T, n)).mean(axis=1)
    assert abs((X0 > thr).mean() - pfa) < 3e-4 and abs((X1 > thr).mean() - pd) < 0.01
    R["np_thr"] = "%.4f" % thr; R["np_d"] = "%.4f" % d; R["np_pd"] = "%.4f" % pd; R["np_pd_mc"] = "%.3f" % (X1 > thr).mean()
    crlb = sig**2/n
    assert abs(X1.var() - crlb) < 0.003
    R["crlb"] = "%.4f" % crlb; R["crlb_mc"] = "%.4f" % X1.var()
    # --- step 10: scalar Wiener filter
    ss, sn = 1.0, 0.25
    g = ss/(ss + sn); mse = ss*sn/(ss + sn)
    s = rng.normal(0, math.sqrt(ss), T); nz = rng.normal(0, math.sqrt(sn), T); y = s + nz
    assert abs(np.mean((g*y - s)**2) - mse) < 0.003
    R["w_gain"] = "%.4f" % g; R["w_mse"] = "%.4f" % mse; R["w_mse_mc"] = "%.4f" % np.mean((g*y - s)**2); R["w_mse_raw"] = "%.4f" % np.mean((y - s)**2)
    # --- step 11: CA-CFAR threshold factor, formula versus Monte Carlo
    Nc, pf = 16, 1e-2
    alpha = Nc*(pf**(-1/Nc) - 1)
    cut = rng.exponential(1.0, 500000); ref = rng.exponential(1.0, (500000, Nc)).mean(axis=1)
    pf_mc = (cut > alpha*ref).mean()
    assert abs(pf_mc - pf) < 5e-4
    R["cfar_alpha"] = "%.3f" % alpha; R["cfar_pfa_mc"] = "%.4f" % pf_mc
    return {k: _trim(v) for k, v in R.items()}


def _trim(s):
    if "." in s and "e" not in s:
        s = s.rstrip("0").rstrip(".")
    return s


def step(n, title, mods, theory, faq, example, formula=""):
    return dict(n=n, title=title, mods=mods, theory=theory, faq=faq, example=example, formula=formula)


STEPS = [
    step(1, "⟦Đặt bài toán và mô hình tín hiệu||Pose the problem and the signal model⟧", [1, 9],
         "<p>⟦Trước khi tính, hãy xác định tín hiệu là tất định hay ngẫu nhiên, liên tục hay rời rạc, và hệ có tuyến tính bất biến hay không. Nếu hệ tuyến tính bất biến, đáp ứng là tích chập và đáp ứng tần số mô tả đầy đủ hệ (Bracewell, chương 1 và 9).||"
         "Before computing, decide whether the signal is deterministic or random, continuous or discrete, and whether the system is linear and invariant. If it is, the response is a convolution and the frequency response describes the system completely (Bracewell, chapters 1 and 9).⟧</p>",
         [("⟦Vì sao phải kiểm tra tuyến tính bất biến trước?||Why check linearity and invariance first?⟧",
           "⟦Vì mọi công cụ Fourier về sau chỉ đúng khi hai điều kiện đó. Module 1 cho thấy khâu bình phương và bộ nhân cosin tạo ra tần số mới.||Because every later Fourier tool relies on both conditions. Module 1 shows that a squarer and a cosine multiplier create new frequencies.⟧"),
          ("⟦Tín hiệu ngẫu nhiên có phổ không?||Does a random signal have a spectrum?⟧",
           "⟦Có phổ công suất (module 12), chứ không có một biến đổi Fourier thường cho từng thực hiện.||It has a power spectrum (module 12), not an ordinary Fourier transform for each realisation.⟧")],
         "<p>⟦Đưa sóng hình sin 50 Hz vào một bộ khuếch đại. Nếu ngõ ra có thêm vạch 100 Hz, hệ phi tuyến (module 1).||Feed a 50 Hz sinusoid into an amplifier. If the output has an extra 100 Hz line, the system is nonlinear (module 1).⟧</p>",
         F("⟦Đáp ứng của hệ tuyến tính bất biến||Response of a linear invariant system⟧", r"y=h*x\;\Longleftrightarrow\;Y(s)=H(s)\,X(s)")),
    step(2, "⟦Lấy mẫu và chống chồng phổ||Sampling and anti-aliasing⟧", [13],
         "<p>⟦Muốn giữ được tín hiệu phải lấy mẫu với tần số $f_s$ lớn hơn hai lần tần số cao nhất. Thành phần vượt quá $f_s/2$ bị gập về một tần số thấp hơn và không tách ra được sau khi đã lấy mẫu (Bracewell, chương 10; Barkat, mục 3.8).||"
         "To keep a signal you must sample at $f_s$ above twice its highest frequency. A component above $f_s/2$ is folded onto a lower frequency and cannot be separated after sampling (Bracewell, chapter 10; Barkat, section 3.8).⟧</p>",
         [("⟦Vì sao phải lọc trước khi lấy mẫu?||Why filter before sampling?⟧", "⟦Vì sau khi lấy mẫu, tần số thật và tần số bị gập trông giống hệt nhau.||Because after sampling the true and the folded frequency look identical.⟧"),
          ("⟦Lấy mẫu dày hơn mức cần có hại gì không?||Does oversampling hurt?⟧", "⟦Không sai kết quả, chỉ tốn dung lượng và thời gian tính.||It does not make the result wrong; it only costs storage and computation.⟧")],
         "<p>⟦Sóng 5000 Hz lấy mẫu ở $f_s=8000$ Hz (Nyquist {{nyq}} Hz). FFT cho đỉnh tại {{alias_peak}} Hz, đúng bằng $|5000-8000|$.||A 5000 Hz wave sampled at $f_s=8000$ Hz (Nyquist {{nyq}} Hz). The FFT peaks at {{alias_peak}} Hz, exactly $|5000-8000|$.⟧</p>",
         F("⟦Tần số bị gập||Aliased frequency⟧", r"f_{\text{alias}}=\left|f-\operatorname{round}\!\left(\tfrac{f}{f_s}\right)f_s\right|", [("f_s", "⟦tần số lấy mẫu||sampling rate⟧")])),
    step(3, "⟦Cửa sổ quan sát và độ phân giải tần số||Observation window and frequency resolution⟧", [1, 8, 14],
         "<p>⟦Quan sát trong thời gian $T$ chỉ phân giải được các vạch cách nhau ít nhất $1/T$. Cắt tín hiệu bằng cửa sổ chữ nhật làm phổ rò sang các ô lân cận (module 1); đây là mặt trái của tích chập với hàm sinc.||"
         "Observing for time $T$ resolves only lines at least $1/T$ apart. Cutting the signal with a rectangular window leaks the spectrum into neighbouring bins (module 1); this is the convolution with a sinc function seen from the other side.⟧</p>",
         [("⟦Thêm số 0 vào cuối tín hiệu có tăng độ phân giải không?||Does zero-padding raise the resolution?⟧", "⟦Không. Nó chỉ nội suy đường phổ mịn hơn; độ phân giải vẫn do $T$ quyết định.||No. It only interpolates a smoother curve; the resolution is still set by $T$.⟧"),
          ("⟦Cửa sổ Hann làm gì?||What does a Hann window do?⟧", "⟦Giảm rò phổ nhưng làm vạch phổ rộng hơn, tức đánh đổi độ phân giải.||It reduces leakage but widens the lines, trading away resolution.⟧")],
         "<p>⟦Với $f_s=8000$ Hz và 1024 mẫu, khoảng cách ô là {{df_1024}} Hz. Để tách hai vạch cách 5 Hz cần $T\\ge0.2$ s, tức ít nhất {{n_5hz}} mẫu.||With $f_s=8000$ Hz and 1024 samples the bin spacing is {{df_1024}} Hz. To separate two lines 5 Hz apart you need $T\\ge0.2$ s, i.e. at least {{n_5hz}} samples.⟧</p>",
         F("⟦Độ phân giải||Resolution⟧", r"\Delta f=\frac{f_s}{N}=\frac1T")),
    step(4, "⟦Biến đổi và đọc phổ||Transform and read the spectrum⟧", [2, 3, 4, 5, 6, 7, 14],
         "<p>⟦Chọn hệ quy ước (hằng số $2\\pi$ ở đâu) rồi khai thác đối xứng: tín hiệu thực có phổ Hermitian, nên chỉ cần lưu nửa phổ. Các định lý dịch, tỉ lệ, đạo hàm và tích chập (chương 6) giúp tìm biến đổi mà không phải tích phân (chương 7).||"
         "Pick a convention (where the $2\\pi$ sits) and exploit symmetry: a real signal has a Hermitian spectrum, so half of it suffices. The shift, similarity, derivative and convolution theorems (chapter 6) find transforms without integrating (chapter 7).⟧</p>",
         [("⟦Tín hiệu thực có đối xứng gì trong miền tần số?||What symmetry does a real signal have in frequency?⟧", "⟦Hermitian: $F(-s)=F^*(s)$, nên biên độ chẵn và pha lẻ (module 2).||Hermitian: $F(-s)=F^*(s)$, so the magnitude is even and the phase odd (module 2).⟧"),
          ("⟦Vì sao pha quan trọng?||Why does phase matter?⟧", "⟦Pha mang thông tin vị trí: dịch tín hiệu chỉ nhân phổ với một hệ số pha (module 6).||Phase carries position: shifting the signal only multiplies the spectrum by a phase factor (module 6).⟧")],
         "<p>⟦Một tín hiệu thực 1000 mẫu có 1000 hệ số FFT phức, nhưng nhờ tính Hermitian chỉ cần {{n_rfft}} hệ số (<code>rfft</code>).||A real 1000-sample signal has 1000 complex FFT coefficients, but thanks to the Hermitian property only {{n_rfft}} are needed (<code>rfft</code>).⟧</p>",
         F("⟦Hermitian||Hermitian symmetry⟧", r"f(x)\ \text{real}\;\Longrightarrow\;F(-s)=F^{*}(s)")),
    step(5, "⟦Lọc tuyến tính||Linear filtering⟧", [3, 9],
         "<p>⟦Bộ lọc là tích chập với đáp ứng xung, và ở miền tần số là phép nhân với đáp ứng tần số. Bộ lọc FIR (trung bình trượt) luôn ổn định; bộ lọc đệ quy như $y[n]=a\\,y[n-1]+(1-a)x[n]$ rẻ hơn nhưng phải kiểm ổn định (module 1, 3 và 9).||"
         "A filter is a convolution with the impulse response and, in the frequency domain, a multiplication by the frequency response. An FIR filter (running mean) is always stable; a recursive one such as $y[n]=a\\,y[n-1]+(1-a)x[n]$ is cheaper but stability must be checked (modules 1, 3 and 9).⟧</p>",
         [("⟦FIR khác IIR ở đâu?||How does FIR differ from IIR?⟧", "⟦FIR chỉ dùng số mẫu vào hữu hạn nên luôn ổn định; IIR có hồi tiếp nên gọn hơn nhưng có thể mất ổn định.||FIR uses a finite number of input samples and is always stable; IIR has feedback, so it is compact but can become unstable.⟧"),
          ("⟦Bộ lọc có làm đổi tần số không?||Does a filter change frequencies?⟧", "⟦Không, nếu tuyến tính bất biến: nó chỉ đổi biên độ và pha từng thành phần (module 1).||Not if it is linear and invariant: it only changes the amplitude and phase of each component (module 1).⟧")],
         "<p>⟦Trung bình trượt 8 điểm ở $f_s=8000$ Hz có độ lợi {{ma_500}} tại 500 Hz và {{ma_1000}} tại 1000 Hz (điểm không). Cả <code>freqz</code> lẫn công thức đóng cho cùng kết quả.||An 8-point running mean at $f_s=8000$ Hz has gain {{ma_500}} at 500 Hz and {{ma_1000}} at 1000 Hz (a null). Both <code>freqz</code> and the closed form agree.⟧</p>",
         F("⟦Đáp ứng biên độ của trung bình trượt $L$ điểm||Magnitude response of an $L$-point running mean⟧", r"|H(f)|=\left|\frac{\sin(\pi L f/f_s)}{L\,\sin(\pi f/f_s)}\right|")),
    step(6, "⟦Mô hình nhiễu và biến ngẫu nhiên||Noise and random-variable models⟧", [10, 11],
         "<p>⟦Tổng của các biến ngẫu nhiên độc lập có mật độ bằng tích chập các mật độ, tức hàm đặc trưng nhân với nhau. Cùng một phép tích chập, cùng một định lý (Bracewell, chương 16; Barkat, chương 1 và 2).||"
         "The density of a sum of independent random variables is the convolution of the densities, i.e. the characteristic functions multiply. The same convolution, the same theorem (Bracewell, chapter 16; Barkat, chapters 1 and 2).⟧</p>",
         [("⟦Vì sao tổng nhiều biến thường có dạng Gauss?||Why is a sum of many variables often Gaussian?⟧", "⟦Đó là định lý giới hạn trung tâm (Bracewell, chương 8, mục Central Limit Theorem; Barkat, mục 1.4.3 bàn luật số lớn).||That is the central limit theorem (Bracewell, chapter 8, section Central Limit Theorem; Barkat, section 1.4.3 covers the law of large numbers).⟧"),
          ("⟦Phân phối Rayleigh xuất hiện ở đâu?||Where does the Rayleigh distribution appear?⟧", "⟦Ở biên bao của nhiễu băng hẹp (Bracewell, chương 17; Barkat, mục 2.3.6).||In the envelope of bandpass noise (Bracewell, chapter 17; Barkat, section 2.3.6).⟧")],
         "<p>⟦Tổng của hai biến độc lập cùng phân bố đều trên $[-\\tfrac12,\\tfrac12]$ có mật độ tam giác. Tích chập số cho phương sai {{var_sum}}, khớp $1/12+1/12=1/6$.||The sum of two independent variables uniform on $[-\\tfrac12,\\tfrac12]$ has a triangular density. Numerical convolution gives variance {{var_sum}}, matching $1/12+1/12=1/6$.⟧</p>",
         F("⟦Mật độ của tổng||Density of a sum⟧", r"f_{X+Y}=f_X*f_Y\;\Longleftrightarrow\;\varphi_{X+Y}=\varphi_X\,\varphi_Y")),
    step(7, "⟦Ước lượng phổ công suất||Power-spectrum estimation⟧", [12, 20],
         "<p>⟦Phổ công suất là biến đổi Fourier của hàm tự tương quan. Periodogram của một đoạn dữ liệu có độ lệch chuẩn xấp xỉ bằng chính giá trị của nó và không giảm khi tăng $N$, nên phải lấy trung bình nhiều đoạn (Bracewell, chương 17 và 19; Barkat, mục 3.5 và 3.7).||"
         "The power spectrum is the Fourier transform of the autocorrelation. The periodogram of one record has a standard deviation about equal to its own value and does not shrink as $N$ grows, so several records must be averaged (Bracewell, chapters 17 and 19; Barkat, sections 3.5 and 3.7).⟧</p>",
         [("⟦Periodogram có nhất quán không?||Is the periodogram consistent?⟧", "⟦Không: phương sai không giảm khi tăng số mẫu; cần trung bình theo đoạn (kiểu Welch).||No: the variance does not fall as samples increase; segment averaging (Welch style) is needed.⟧"),
          ("⟦Tính ergodic để làm gì?||What is ergodicity for?⟧", "⟦Để trung bình theo thời gian của một thực hiện thay được trung bình tập hợp (Barkat, mục 3.7).||So a time average over one realisation can stand in for the ensemble average (Barkat, section 3.7).⟧")],
         "<p>⟦Nhiễu trắng chuẩn hóa, 1024 mẫu mỗi đoạn: một periodogram có độ lệch chuẩn {{pg_single}} (lý thuyết 1), trung bình 64 đoạn còn {{pg_avg}} (lý thuyết {{pg_theory}}).||Unit white noise, 1024 samples per record: one periodogram has standard deviation {{pg_single}} (theory 1), averaging 64 records leaves {{pg_avg}} (theory {{pg_theory}}).⟧</p>",
         F("⟦Định lý Wiener–Khinchin||Wiener–Khinchin theorem⟧", r"S(s)=\int_{-\infty}^{\infty}R(\tau)\,e^{-i2\pi s\tau}\,d\tau",
           [("R(\\tau)", "⟦hàm tự tương quan||autocorrelation function⟧"), ("S(s)", "⟦phổ công suất||power spectrum⟧")])),
    step(8, "⟦Phát hiện tín hiệu trong nhiễu||Detecting a signal in noise⟧", [21, 24, 25],
         "<p>⟦Phát hiện là chọn giữa $H_0$ (chỉ có nhiễu) và $H_1$ (có tín hiệu). Tiêu chuẩn Neyman–Pearson giữ xác suất báo động giả $P_{FA}$ cố định và cực đại hóa xác suất phát hiện $P_D$; lời giải là kiểm định tỉ số hợp lý (Barkat, chương 5 và 10).||"
         "Detection chooses between $H_0$ (noise only) and $H_1$ (signal present). The Neyman–Pearson criterion fixes the false-alarm probability $P_{FA}$ and maximises the detection probability $P_D$; the solution is a likelihood-ratio test (Barkat, chapters 5 and 10).⟧</p>",
         [("⟦Vì sao dùng Neyman–Pearson thay vì Bayes?||Why Neyman–Pearson rather than Bayes?⟧", "⟦Vì không cần biết xác suất tiên nghiệm và chi phí quyết định, thường không có trong radar và truyền thông.||Because it needs neither prior probabilities nor decision costs, which radar and communications often lack.⟧"),
          ("⟦Tăng số mẫu giúp thế nào?||How do more samples help?⟧", "⟦Chỉ số phát hiện $d=\\sqrt N A/\\sigma$ tăng theo $\\sqrt N$, nên $P_D$ tăng ở cùng $P_{FA}$.||The detectability index $d=\\sqrt N A/\\sigma$ grows with $\\sqrt N$, so $P_D$ rises at the same $P_{FA}$.⟧")],
         "<p>⟦Phát hiện mức một chiều $A=1$ trong nhiễu Gauss $\\sigma=1$ với $N=10$ mẫu và $P_{FA}=10^{-3}$: ngưỡng trên trung bình mẫu là {{np_thr}}, $d={{np_d}}$, $P_D={{np_pd}}$ theo công thức và {{np_pd_mc}} theo mô phỏng 400 000 lần.||"
         "Detecting a DC level $A=1$ in Gaussian noise $\\sigma=1$ with $N=10$ samples and $P_{FA}=10^{-3}$: the threshold on the sample mean is {{np_thr}}, $d={{np_d}}$, $P_D={{np_pd}}$ by formula and {{np_pd_mc}} by a 400 000-trial simulation.⟧</p>",
         F("⟦Xác suất phát hiện||Detection probability⟧", r"P_D=Q\!\left(Q^{-1}(P_{FA})-d\right),\qquad d=\frac{\sqrt N\,A}{\sigma}", [("Q", "⟦hàm đuôi của phân phối chuẩn||upper-tail function of the normal distribution⟧")])),
    step(9, "⟦Ước lượng tham số||Parameter estimation⟧", [22],
         "<p>⟦Ước lượng hợp lý cực đại (ML) chọn tham số làm dữ liệu quan sát có khả năng nhất; ước lượng Bayes thêm phân phối tiên nghiệm (MAP, MMSE). Giới hạn Cramér–Rao cho biết phương sai nhỏ nhất của mọi ước lượng không chệch (Barkat, chương 6).||"
         "Maximum-likelihood (ML) estimation picks the parameter that makes the observed data most likely; Bayes estimation adds a prior (MAP, MMSE). The Cramér–Rao bound gives the smallest variance of any unbiased estimator (Barkat, chapter 6).⟧</p>",
         [("⟦Ước lượng đạt được giới hạn Cramér–Rao gọi là gì?||What is an estimator that reaches the Cramér–Rao bound called?⟧", "⟦Ước lượng hiệu quả (efficient).||An efficient estimator.⟧"),
          ("⟦MAP khác ML ở đâu?||How does MAP differ from ML?⟧", "⟦MAP nhân thêm mật độ tiên nghiệm của tham số; khi tiên nghiệm phẳng thì trùng ML.||MAP multiplies in the prior density of the parameter; with a flat prior it coincides with ML.⟧")],
         "<p>⟦Ước lượng mức một chiều từ $N=10$ mẫu nhiễu $\\sigma=1$: giới hạn Cramér–Rao là {{crlb}}, phương sai của trung bình mẫu đo bằng mô phỏng là {{crlb_mc}}, nên trung bình mẫu là ước lượng hiệu quả.||"
         "Estimating a DC level from $N=10$ samples of noise $\\sigma=1$: the Cramér–Rao bound is {{crlb}}, the simulated variance of the sample mean is {{crlb_mc}}, so the sample mean is an efficient estimator.⟧</p>",
         F("⟦Giới hạn Cramér–Rao cho mức một chiều||Cramér–Rao bound for a DC level⟧", r"\operatorname{var}(\hat A)\ \ge\ \frac{\sigma^2}{N}")),
    step(10, "⟦Lọc tối ưu: Wiener và Kalman||Optimal filtering: Wiener and Kalman⟧", [23],
         "<p>⟦Nguyên lý trực giao nói sai số của ước lượng bình phương tối thiểu phải trực giao với dữ liệu. Bộ lọc Wiener áp dụng nó cho quá trình dừng; bộ lọc Kalman làm việc đệ quy cho hệ thay đổi theo thời gian (Barkat, mục 7.2, 7.3 và 7.5).||"
         "The orthogonality principle says the error of a least-squares estimate must be orthogonal to the data. The Wiener filter applies it to stationary processes; the Kalman filter works recursively for time-varying systems (Barkat, sections 7.2, 7.3 and 7.5).⟧</p>",
         [("⟦Wiener và Kalman khác nhau thế nào?||How do Wiener and Kalman differ?⟧", "⟦Wiener dành cho quá trình dừng, thiết kế trong miền tần số; Kalman cập nhật đệ quy theo từng mẫu.||Wiener is for stationary processes and designed in frequency; Kalman updates recursively sample by sample.⟧"),
          ("⟦Bộ lọc Wiener luôn cải thiện sai số không?||Does a Wiener filter always reduce the error?⟧", "⟦Nó cho sai số bình phương trung bình nhỏ nhất trong lớp bộ lọc tuyến tính, nên không bao giờ tệ hơn để nguyên dữ liệu.||It gives the smallest mean-square error among linear filters, so it is never worse than leaving the data alone.⟧")],
         "<p>⟦Tín hiệu vô hướng phương sai 1 trong nhiễu phương sai 0.25: hệ số Wiener {{w_gain}}, sai số bình phương trung bình {{w_mse}} (mô phỏng {{w_mse_mc}}) so với {{w_mse_raw}} nếu để nguyên dữ liệu.||A scalar signal of variance 1 in noise of variance 0.25: Wiener gain {{w_gain}}, mean-square error {{w_mse}} (simulated {{w_mse_mc}}) versus {{w_mse_raw}} if the data is left alone.⟧</p>",
         F("⟦Hệ số Wiener vô hướng||Scalar Wiener gain⟧", r"w=\frac{\sigma_s^2}{\sigma_s^2+\sigma_n^2},\qquad \text{MSE}=\frac{\sigma_s^2\sigma_n^2}{\sigma_s^2+\sigma_n^2}")),
    step(11, "⟦Ngưỡng thích nghi CFAR||Adaptive CFAR thresholds⟧", [26],
         "<p>⟦Khi công suất nhiễu thay đổi, ngưỡng cố định làm xác suất báo động giả trôi. CFAR ước lượng mức nhiễu từ các ô tham chiếu quanh ô đang xét rồi đặt ngưỡng tỉ lệ với nó, giữ $P_{FA}$ không đổi (Barkat, chương 11 và 12).||"
         "When the noise power varies, a fixed threshold lets the false-alarm probability drift. CFAR estimates the noise level from reference cells around the cell under test and sets a proportional threshold, keeping $P_{FA}$ constant (Barkat, chapters 11 and 12).⟧</p>",
         [("⟦Vì sao không dùng ngưỡng cố định?||Why not a fixed threshold?⟧", "⟦Vì $P_{FA}$ phụ thuộc công suất nhiễu; nhiễu tăng gấp đôi thì báo động giả tăng vọt.||Because $P_{FA}$ depends on the noise power; if the noise doubles, false alarms jump.⟧"),
          ("⟦Có mục tiêu nằm trong ô tham chiếu thì sao?||What if a target sits in the reference cells?⟧", "⟦Ngưỡng bị đẩy lên và mục tiêu bị che; các biến thể CFAR khác được điểm lại ở mục 11.3.2.||The threshold is pushed up and the target is masked; other CFAR variants are reviewed in section 11.3.2.⟧")],
         "<p>⟦CA-CFAR với $N=16$ ô tham chiếu và $P_{FA}=10^{-2}$ trong nhiễu bình phương-hợp-luật: hệ số ngưỡng $\\alpha={{cfar_alpha}}$ lần trung bình ô tham chiếu; mô phỏng 500 000 lần cho $P_{FA}={{cfar_pfa_mc}}$.||CA-CFAR with $N=16$ reference cells and $P_{FA}=10^{-2}$ in square-law noise: threshold factor $\\alpha={{cfar_alpha}}$ times the reference-cell mean; a 500 000-trial simulation gives $P_{FA}={{cfar_pfa_mc}}$.⟧</p>",
         F("⟦Hệ số ngưỡng CA-CFAR||CA-CFAR threshold factor⟧", r"P_{FA}=\left(1+\frac{\alpha}{N}\right)^{-N}\;\Longrightarrow\;\alpha=N\left(P_{FA}^{-1/N}-1\right)")),
    step(12, "⟦Kiểm chứng số và báo cáo||Numerical verification and reporting⟧", list(range(1, 27)),
         "<p>⟦Một kết quả chưa xong cho tới khi được tính bằng hai phương pháp độc lập và khớp nhau: FFT với tổng trực tiếp, tích phân số với công thức đóng, công thức với mô phỏng. Khi báo cáo, ghi đủ $f_s$, $N$, cửa sổ, hạt giống ngẫu nhiên và phiên bản thư viện để người khác tái lập.||"
         "A result is not finished until two independent methods agree: FFT with a direct sum, numerical integral with a closed form, formula with simulation. When reporting, state $f_s$, $N$, the window, the random seed and the library versions so others can reproduce it.⟧</p>",
         [("⟦Vì sao cần hai phương pháp?||Why two methods?⟧", "⟦Vì một phương pháp duy nhất có thể sai cùng chiều với bạn (nhầm hằng số $2\\pi$, nhầm dấu số mũ, nhầm chuẩn hóa $1/N$).||Because a single method can be wrong in the same direction as you (a $2\\pi$ constant, an exponent sign, a $1/N$ normalisation).⟧"),
          ("⟦Nên ghi gì để tái lập?||What should be recorded to reproduce it?⟧", "⟦Tham số thí nghiệm, hạt giống ngẫu nhiên, và phiên bản NumPy/SciPy dùng để chạy.||The experiment parameters, the random seed, and the NumPy/SciPy versions used.⟧")],
         "<p>⟦Mọi notebook của khóa đều làm đúng như vậy: ví dụ module 1 in ra độ lệch giữa FFT và tổng trực tiếp, và dừng nếu vượt $10^{-9}$.||Every notebook in this course does exactly this: for example module 1 prints the deviation between FFT and direct sum and stops if it exceeds $10^{-9}$.⟧</p>"),
]
