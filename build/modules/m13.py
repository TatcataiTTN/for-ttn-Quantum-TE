from lib import F, C, UL, OL, TBL

MOD = dict(
    n=13, slug="sampling-series-orthogonal", part="C", book="BK",
    title="⟦Lấy mẫu, chuỗi Fourier và biểu diễn trực giao||Sampling, Fourier series and orthogonal representation⟧",
    blurb="⟦Định lý lấy mẫu, nội suy, lọc chữ nhật, chồng phổ, lấy mẫu có đạo hàm và xen kẽ, chuỗi Fourier và Gibbs (Bracewell) tới chuỗi Fourier tổng quát, Gram-Schmidt, phương trình tích phân và khai triển Karhunen-Loève (Barkat).||"
          "The sampling theorem, interpolation, rectangular filtering, aliasing, ordinate-and-slope and interlaced sampling, Fourier series and Gibbs (Bracewell) to generalised Fourier series, Gram-Schmidt, integral equations and the Karhunen-Loève expansion (Barkat).⟧",
    src="⟦Bracewell, chương 10, tr. 219–258; Barkat, chương 8, tr. 449–500||Bracewell, chapter 10, pp. 219–258; Barkat, chapter 8, pp. 449–500⟧",
    data="⟦Sinh bằng mã: hàm sinc, sóng vuông, tam giác, tín hiệu chữ nhật, nhân Wiener và nhân mũ||Generated in code: sinc functions, a square wave, triangles, rectangular signals, Wiener and exponential kernels⟧",
    objectives=[
        "⟦Phát biểu và chứng minh định lý lấy mẫu bằng biểu tượng shah; nội suy sinc; nhận biết chồng phổ và các trường hợp biên (điều hòa đúng tần số cắt).||State and prove the sampling theorem with the shah symbol; sinc interpolation; recognise aliasing and the boundary cases (a harmonic exactly at the cutoff).⟧",
        "⟦Dùng lấy mẫu có đạo hàm, lấy mẫu xen kẽ, và biết vì sao chúng khuếch đại nhiễu.||Use ordinate-and-slope and interlaced sampling, and know why they amplify noise.⟧",
        "⟦Xem chuỗi Fourier là biến đổi ở giới hạn; tính hệ số bằng biến đổi hữu hạn và giải thích Gibbs 9 phần trăm.||View the Fourier series as a transform in the limit; compute coefficients with finite transforms and explain the 9 percent Gibbs overshoot.⟧",
        "⟦Khai triển tín hiệu theo hệ trực chuẩn, sai số năng lượng, Gram-Schmidt (cổ điển và cải tiến), biểu diễn hình học trong không gian tín hiệu.||Expand a signal in an orthonormal set, the energy error, Gram-Schmidt (classical and modified), geometric representation in signal space.⟧",
        "⟦Chuyển phương trình vi phân thành phương trình tích phân qua hàm Green, và dùng Karhunen-Loève cho quá trình ngẫu nhiên (Wiener, mũ, nhiễu trắng).||Turn differential equations into integral equations through Green's function, and use the Karhunen-Loève expansion for random processes (Wiener, exponential, white noise).⟧",
    ],
    parts=[
        # ------------------------------------------------ PART 1
        dict(
            title="⟦Định lý lấy mẫu và nội suy||The sampling theorem and interpolation⟧",
            scr=("⟦Một hàm có các giá trị chọn tùy ý, không liên hệ giữa lân cận, không bao giờ xuất hiện trong tự nhiên: thiết bị đo luôn giới hạn tốc độ biến đổi.||A function with arbitrarily chosen values, no connection between neighbours, is never seen in nature: measuring instruments always limit the rate of change.⟧",
                 "⟦Nếu vậy, có thể bỏ bớt giá trị mà vẫn giữ gần như mọi thông tin, chỉ cần ghi tập giá trị cách nhau đều, mịn nhưng không vô cùng nhỏ.||Then values can be dropped while keeping nearly all the information, by noting a set of values at fine but not infinitesimal spacing.⟧",
                 "⟦Hàm giới hạn băng (biến đổi bằng 0 ngoài $|s|\\le s_c$) được xác định đầy đủ bởi mẫu cách nhau không quá $\\tfrac1{2s_c}$.||A band-limited function (transform zero beyond $|s|\\le s_c$) is fully specified by samples spaced at most $\\tfrac1{2s_c}$ apart.⟧"),
            preview=["⟦Phát biểu và chứng minh||Statement and proof⟧", "⟦Nội suy và lọc chữ nhật||Interpolation and rectangular filtering⟧", "⟦Trung bình trượt, chồng phổ||Running means and aliasing⟧"],
            slides=[
                ("⟦Vì sao có thể lấy mẫu||Why sampling is possible⟧",
                 "<p>⟦Trong tự nhiên luôn có giới hạn tốc độ biến đổi, nên giá trị các thời điểm lân cận có liên hệ và có thể dự đoán qua một khoảng ngắn. Vậy có thể bỏ giá trị trong các khoảng cùng cỡ mà vẫn giữ gần hết thông tin bằng cách ghi tập giá trị cách nhau mịn nhưng không vô cùng nhỏ (Bracewell, chương 10, tr. 219). Định lý lấy mẫu nói rằng, với một điều kiện, có thể khôi phục đầy đủ giá trị nằm giữa các mẫu; điều kiện là hàm phải giới hạn băng. Xử lý tín hiệu số áp dụng được cho tập mẫu, còn lý thuyết hàm biến liên tục làm sáng tỏ nền tảng của DSP (tr. 219).||In nature there is always a limit to the rate of change, so values at neighbouring instants are related and can be predicted over a brief interval. Values can then be dispensed with over intervals of the same order while nearly all the information is kept by noting a set of values at fine but not infinitesimal spacing (Bracewell, chapter 10, p. 219). The sampling theorem says that, under a condition, the values between regularly spaced samples can be recovered with full accuracy; the condition is that the function be band-limited. Digital signal processing can be applied to the sample set while the theory of functions of a continuous variable clarifies the basis of DSP (p. 219).⟧</p>"),
                ("⟦Khoảng lấy mẫu thô một cách đáng ngạc nhiên||The surprisingly coarse sampling interval⟧",
                 "<p>⟦Với $\\text{sinc}\\,x$, phổ phẳng khi $|s|<\\tfrac12$ và bằng 0 ngoài đó; khoảng lấy mẫu suy ra là 1, rất thô so với khoảng ta chọn theo trực giác khi tích phân số (hình 10.1, tr. 220). Mẫu của $\\text{sinc}\\,x$ tại các số nguyên là $1,0,0,\\ldots$ và của $\\text{sinc}^2\\tfrac12x$ (cùng tần số cắt $\\tfrac12$) cũng thô như vậy. Nhưng biến đổi hầu như không bao giờ cắt tuyệt đối, nên khi dùng định lý ta phải ước lượng sai số của việc coi dạng sóng là giới hạn băng (tr. 220). Số đo: tái tạo $f=\\text{sinc}^2(x/2)$ (phổ $2\\Lambda(2s)$, cắt tại $\\tfrac12$) từ mẫu ở số nguyên, tại $x=0.5$, lệch {{smp_err}} so với giá trị đúng.||For $\\text{sinc}\\,x$ the spectrum is flat for $|s|<\\tfrac12$ and zero beyond; the sampling interval deduced is 1, extremely coarse compared with what would intuitively be chosen for numerical integration (Fig. 10.1, p. 220). The samples of $\\text{sinc}\\,x$ at integers are $1,0,0,\\ldots$ and those of $\\text{sinc}^2\\tfrac12x$ (same cutoff $\\tfrac12$) are equally coarse. But the transform almost never cuts off absolutely, so when using the theorem we must estimate the error of taking a waveform to be band-limited (p. 220). Measured: reconstructing $f=\\text{sinc}^2(x/2)$ (spectrum $2\\Lambda(2s)$, cutoff $\\tfrac12$) from samples at integers, at $x=0.5$, deviates by {{smp_err}} from the exact value.⟧</p>"),
                ("⟦Biến đổi bị cắt||Cutoff transforms⟧",
                 "<p>⟦$f(x)$ có biến đổi $F(s)=0$ khi $|s|>s_c$ là hàm giới hạn băng; biến đổi có dạng $\\Pi(s/2s_c)G(s)$ với $G$ tùy ý gọi là biến đổi bị cắt, và các hàm có dạng $\\text{sinc}\\,2s_cx*g(x)$ với $g$ tùy ý. Tính chất kỳ lạ: các hàm giới hạn băng được xác định đầy đủ bởi giá trị cách đều không quá $\\tfrac1{2s_c}$, trừ trường hợp ngoại lệ (tr. 221). Chứng minh dùng biểu tượng shah vì nhân với $\\text{III}(x)$ tương đương lấy mẫu: giữ thông tin tại điểm mẫu và bỏ ở giữa; và $\\text{III}(x)\\supset\\text{III}(s)$.||A function $f(x)$ with $F(s)=0$ for $|s|>s_c$ is band-limited; a transform of the form $\\Pi(s/2s_c)G(s)$ with arbitrary $G$ is called a cutoff transform, and the functions have the form $\\text{sinc}\\,2s_cx*g(x)$ with arbitrary $g$. The peculiar property: band-limited functions are fully specified by values at equal intervals not exceeding $\\tfrac1{2s_c}$, with one exception (p. 221). The proof uses the shah symbol since multiplying by $\\text{III}(x)$ is sampling: information is kept at the sample points and dropped in between; and $\\text{III}(x)\\supset\\text{III}(s)$.⟧</p>"),
                ("⟦Chứng minh bằng shah: sao chép phổ||Proof by shah: replicating the spectrum⟧",
                 "<p>⟦Hàm lấy mẫu $f(x)\\text{III}(x/\\tau)=\\sum f(n\\tau)\\delta(x-n\\tau)$ chỉ giữ thông tin tại $x=n\\tau$. Biến đổi của $\\text{III}(x/\\tau)$ là $\\tau\\text{III}(\\tau s)$, hàng xung đơn vị cách nhau $\\tau^{-1}$; theo định lý tích chập $f\\,\\text{III}(x/\\tau)\\supset\\tau\\text{III}(\\tau s)*F(s)$: lấy mẫu sao chép phổ $F$ với chu kỳ $\\tau^{-1}$ (Bracewell, tr. 221 đến 223). Ta khôi phục $f$ nếu khôi phục được $F$, bằng nhân với $\\Pi(s/2s_c)$. Không thể nếu các \"đảo\" chồng nhau, tức khi $\\tau^{-1}<2s_c$: $\\tau\\le1/2s_c$, và lấy mẫu tới hạn là các đảo vừa chạm nhau (hình 10.3, 10.4).||The sampled function $f(x)\\text{III}(x/\\tau)=\\sum f(n\\tau)\\delta(x-n\\tau)$ retains information only at $x=n\\tau$. The transform of $\\text{III}(x/\\tau)$ is $\\tau\\text{III}(\\tau s)$, a row of unit impulses at spacing $\\tau^{-1}$; by the convolution theorem $f\\,\\text{III}(x/\\tau)\\supset\\tau\\text{III}(\\tau s)*F(s)$: sampling replicates the spectrum $F$ at period $\\tau^{-1}$ (Bracewell, pp. 221 to 223). We recover $f$ if we can recover $F$, by multiplying by $\\Pi(s/2s_c)$. This is impossible if the \"islands\" overlap, i.e. when $\\tau^{-1}<2s_c$: $\\tau\\le1/2s_c$, and critical sampling has the islands just touching (Figs. 10.3, 10.4).⟧</p>"
                 + F("⟦Lấy mẫu sao chép phổ||Sampling replicates the spectrum⟧", r"f(x)\,\text{III}\!\left(\frac x\tau\right)\ \supset\ \tau\,\text{III}(\tau s)*F(s)")),
                ("⟦Trường hợp biên: điều hòa ở đúng tần số cắt||The boundary case: a harmonic exactly at the cutoff⟧",
                 "<p>⟦Nếu $F(s_c)\\ne0$ và lấy mẫu tới hạn, các đảo chạm nhau tại vách; nhân với $\\Pi(s/2s_c)$ (bằng $\\tfrac12$ tại $s=s_c$) vẫn khôi phục chính xác. Nhưng nếu $f$ chứa một thành phần điều hòa tần số $s_c$ thì có thêm điều cần nói: phần chẵn (cosin) khôi phục được, phần lẻ (sin) biến mất vì các xung $B$ và $B'$ hợp lại và triệt nhau (tr. 223 đến 224). Định lý phát biểu đầy đủ: hàm có biến đổi bằng 0 khi $|s|>s_c$ được xác định bởi các giá trị cách đều không quá $\\tfrac1{2s_c}$, trừ mọi số hạng điều hòa có không điểm tại các điểm lấy mẫu. Bài tập: $\\cos(\\omega t-\\phi)$ lấy mẫu ở khoảng tới hạn (nửa chu kỳ): các mẫu chỉ là của phần chẵn $\\cos\\phi\\cos\\omega t$; số đo lệch {{crit_dev}}.||If $F(s_c)\\ne0$ and we sample critically the islands make butt contact at the cliffs; multiplying by $\\Pi(s/2s_c)$ (equal to $\\tfrac12$ at $s=s_c$) still recovers exactly. But if $f$ contains a harmonic component of frequency $s_c$ there is more to say: the even (cosine) part is recovered, the odd (sine) part disappears since the impulses $B$ and $B'$ fuse and cancel (pp. 223 to 224). The full statement of the theorem: a function whose transform vanishes for $|s|>s_c$ is specified by values at equal intervals not exceeding $\\tfrac1{2s_c}$, save for any harmonic term with zeros at the sampling points. Exercise: $\\cos(\\omega t-\\phi)$ sampled at the critical interval (a half period): the samples are exactly those of the even part $\\cos\\phi\\cos\\omega t$; measured deviation {{crit_dev}}.⟧</p>"),
                ("⟦Nội suy||Interpolation⟧",
                 "<p>⟦Phép nhân biến đổi với $\\Pi(s/2s_c)$ ứng với chập với $2s_c\\,\\text{sinc}\\,2s_cx$ ở miền hàm, cho $f(x)$ trực tiếp từ $\\text{III}(x/\\tau)f(x)$: tích chập với hàng xung rút gọn đúng về một tổng (tích chuỗi): $f(x)=\\sum f(n\\tau)\\,\\text{sinc}\\,\\dfrac{x-n\\tau}{\\tau}$ (tr. 224). Nội suy điểm giữa dùng bảng 10.1 các giá trị $\\text{sinc}\\,x$ tại nửa nguyên: $0.6366$, $-0.2122$, $0.1273$, $-0.0909$, $0.0707$, $\\ldots$; số đo: $\\text{sinc}(0.5)$ = {{mid_1}}, $\\text{sinc}(1.5)$ = {{mid_2}}, $\\text{sinc}(2.5)$ = {{mid_3}}, $\\text{sinc}(3.5)$ = {{mid_4}}.||Multiplying the transform by $\\Pi(s/2s_c)$ corresponds to convolution with $2s_c\\,\\text{sinc}\\,2s_cx$ in the function domain, giving $f(x)$ directly from $\\text{III}(x/\\tau)f(x)$: convolution with a row of impulses reduces exactly to a sum (serial product): $f(x)=\\sum f(n\\tau)\\,\\text{sinc}\\,\\dfrac{x-n\\tau}{\\tau}$ (p. 224). Midpoint interpolation uses Table 10.1 of $\\text{sinc}\\,x$ at half-integers: $0.6366$, $-0.2122$, $0.1273$, $-0.0909$, $0.0707$, $\\ldots$; measured: $\\text{sinc}(0.5)$ = {{mid_1}}, $\\text{sinc}(1.5)$ = {{mid_2}}, $\\text{sinc}(2.5)$ = {{mid_3}}, $\\text{sinc}(3.5)$ = {{mid_4}}.⟧</p>"
                 + F("⟦Nội suy sinc||Sinc interpolation⟧", r"f(x)=\sum_{n=-\infty}^{\infty}f(n\tau)\operatorname{sinc}\frac{x-n\tau}{\tau},\qquad \tau\le\frac1{2s_c}")),
                ("⟦Lọc chữ nhật ở miền tần số bằng tổng sinc||Rectangular filtering by a sinc sum⟧",
                 "<p>⟦Muốn bỏ thành phần tần số vượt giới hạn, nhân biến đổi với $\\Pi(s)$ ($s_c=\\tfrac12$, khoảng tới hạn 1). Với khoảng lấy mẫu $\\tau=1$ ta được $\\sum f(n)\\text{sinc}(x-n)$ không lọc gì cả ($f(x)$ nguyên vẹn); với $\\tau=\\tfrac12$ phổ đầu ra gồm $F\\,\\Pi$ cộng các phần xa hơn, đủ dùng khi các thành phần cần bỏ nằm ngay ngoài vùng trung tâm. Dùng lặp lại cùng mảng ở $\\tau=\\tfrac12$ đẩy thấp thêm các đảo ngoài (hình 10.5). Kết quả: đọc $f$ ở nửa khoảng tới hạn rồi lấy tích chuỗi với $2s_c\\text{sinc}\\,2s_cx$ tại mọi giá trị nửa nguyên của $2s_cx$; mảng lọc (bảng 10.2) gồm các giá trị nội suy cộng các số 0 xen kẽ và giá trị 1 ở giữa: $\\ldots,-0.2122,0,0.6366,1,0.6366,0,-0.2122,\\ldots$ (tr. 224 đến 226).||To remove components beyond a limit, multiply the transform by $\\Pi(s)$ ($s_c=\\tfrac12$, critical interval 1). With sampling interval $\\tau=1$ we get $\\sum f(n)\\text{sinc}(x-n)$, no filtering at all ($f(x)$ intact); with $\\tau=\\tfrac12$ the output spectrum consists of $F\\,\\Pi$ plus remoter parts, enough when the components to be rejected lie just beyond the central region. Repeated use of the same array at $\\tau=\\tfrac12$ pushes down more of the outer islands (Fig. 10.5). Result: read off $f$ at half the critical interval and take the serial product with $2s_c\\text{sinc}\\,2s_cx$ at all half-integral values of $2s_cx$; the filtering array (Table 10.2) consists of the interpolation values plus interleaved zeros and a central 1: $\\ldots,-0.2122,0,0.6366,1,0.6366,0,-0.2122,\\ldots$ (pp. 224 to 226).⟧</p>"),
                ("⟦Trung bình trượt: hàm truyền của $N$ hệ số||Running means: the transfer function of $N$ coefficients⟧",
                 "<p>⟦Chập với chữ nhật rộng $W$ có hàm truyền $\\text{sinc}\\,Ws$, độ rộng băng tương đương $1/W$ và độ rộng băng 3 dB bằng $0.8859/W$, nhưng suy giảm không đủ sắc và có dao động lớn ngoài băng. Với $W=12$ (trung bình trượt 12 tháng từ dữ liệu cách 1 tháng) ta có 12 xung cường độ $\\tfrac1{12}$, và hàm truyền là chuỗi hình học: $\\dfrac{\\sin N\\pi s}{N\\sin\\pi s}$ (đó là trường ăng ten của một dãy $N$ ăng ten cách đều). Khí tượng học dùng 13 hệ số, nửa cường độ ở hai đầu: $\\dfrac{\\sin N\\pi s}{N\\tan\\pi s}$, giảm các thùy bên (Bracewell, tr. 226 đến 228). Số đo: băng 3 dB {{rm_3db}}; thùy bên đầu tiên của 12 hệ số {{rm12_side}} và của 13 hệ số {{rm13_side}}.||Convolution with a rectangle of width $W$ has transfer function $\\text{sinc}\\,Ws$, equivalent bandwidth $1/W$ and 3 dB bandwidth $0.8859/W$, but the fall-off is not sharp enough and there is strong oscillation outside the band. With $W=12$ (12-month running means from data one month apart) we have 12 impulses of strength $\\tfrac1{12}$, and the transfer function is a geometric series: $\\dfrac{\\sin N\\pi s}{N\\sin\\pi s}$ (the field pattern of an array of $N$ equally spaced antennas). Meteorology uses 13 coefficients with half strength at the ends: $\\dfrac{\\sin N\\pi s}{N\\tan\\pi s}$, reducing the sidelobes (Bracewell, pp. 226 to 228). Measured: the 3 dB bandwidth {{rm_3db}}; the first sidelobe of the 12-coefficient filter {{rm12_side}} and of the 13-coefficient filter {{rm13_side}}.⟧</p>{{fig:runmean}}"),
                ("⟦Lấy mẫu dưới mức và chồng phổ||Undersampling and aliasing⟧",
                 "<p>⟦Nếu đọc $f$ ở khoảng tương ứng với tần số cắt mong muốn, các giá trị định nghĩa hàm giới hạn băng $g(x)$ có phổ cắt đúng chỗ, nhưng đó không phải lọc chữ nhật: kết quả phụ thuộc thành phần tần số cao của $f$ (một mẫu có thể rơi vào đỉnh của một xung hẹp) và phụ thuộc pha lưới lấy mẫu. Thành phần tần số cao \"đóng giả\" tần số thấp, giống phản xạ đuôi phổ qua $s=s_c$: gọi là chồng phổ (aliasing) (Bracewell, tr. 229 đến 230). Phổ chẵn được tăng cường còn phần lẻ giảm, nên $g$ \"chẵn hơn\" $f$. Số đo: một sóng tần số 0.8 lấy mẫu ở khoảng 1 (cắt 0.5) hiện thành tần số {{al_f}}, phản xạ qua 0.5.||If $f$ is read off at intervals corresponding to a desired cutoff, the values define a band-limited function $g(x)$ with the spectrum cut off at the desired place, but this is not rectangular filtering: the result depends on high-frequency components of $f$ (a sample may fall on the peak of a narrow spike) and on the phase of the sampling grid. High-frequency components \"impersonate\" low frequencies, like a reflection of the spectral tail in $s=s_c$: this is called aliasing (Bracewell, pp. 229 to 230). The even part of the spectrum is reinforced while the odd part is diminished, so $g$ is \"evener\" than $f$. Measured: a wave of frequency 0.8 sampled at interval 1 (cutoff 0.5) appears at frequency {{al_f}}, reflected in 0.5.⟧</p>"),
                ("⟦Tự kiểm tra phần 1||Self-check, part 1⟧",
                 UL(["⟦Khoảng lấy mẫu tối đa cho hàm có phổ cắt tại $s_c=5$?||What is the maximum sampling interval for a function with spectrum cut off at $s_c=5$?⟧",
                     "⟦Lấy mẫu làm gì với phổ?||What does sampling do to the spectrum?⟧",
                     "⟦Vì sao thành phần $\\sin$ ở đúng tần số cắt biến mất khi lấy mẫu tới hạn?||Why does a $\\sin$ component exactly at the cutoff vanish under critical sampling?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: $\\tfrac1{2s_c}=0.1$; sao chép với chu kỳ $\\tau^{-1}$; vì các mẫu rơi đúng vào các không điểm của nó.||Hints: $\\tfrac1{2s_c}=0.1$; replicates with period $\\tau^{-1}$; because the samples fall exactly on its zeros.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 2
        dict(
            title="⟦Lấy mẫu cải biên và nhiễu||Modified sampling and noise⟧",
            scr=("⟦Nếu chỉ có một nửa số mẫu cần thiết, ta cần thêm thông tin phụ: đạo hàm, hoặc một bộ mẫu xen kẽ.||If only half the necessary samples are available we need supplementary information: slopes, or an interlaced set.⟧",
                 "⟦Các định lý lấy mẫu bậc cao đúng trong lý thuyết nhưng phá vỡ trong thực hành vì nhiễu.||Higher-order sampling theorems are right in theory but break down in practice because of noise.⟧",
                 "⟦Nội suy sinc chịu nhiễu tốt (phương sai không đổi), nhưng lấy mẫu xen kẽ khuếch đại nhiễu.||Sinc interpolation tolerates noise well (the variance is unchanged), but interlaced sampling amplifies noise.⟧"),
            preview=["⟦Lấy mẫu tung độ và độ dốc||Ordinate and slope sampling⟧", "⟦Lấy mẫu xen kẽ||Interlaced sampling⟧", "⟦Lấy mẫu khi có nhiễu||Sampling in the presence of noise⟧"],
            slides=[
                ("⟦Lấy mẫu tung độ và độ dốc||Ordinate and slope sampling⟧",
                 "<p>⟦Giả sử $f$ giới hạn băng cần các tung độ cách 0.5, nhưng chỉ cho $\\text{III}f$, tức cách 1: các đảo phổ chồng lên nhau, không khôi phục được $F$. Nếu cho thêm độ dốc, $\\text{III}f'$, thì khôi phục được: trong $-1<s<1$, $\\text{III}f=F(s+1)+F(s)+F(s-1)$ và $\\text{III}f'=i2\\pi(s+1)F(s+1)+i2\\pi sF(s)+i2\\pi(s-1)F(s-1)$, hai phương trình cho $F(s)$ vì với mỗi $s$ một trong ba ẩn bằng 0 (Bracewell, tr. 230 đến 231). Kết quả: $f(x)=\\sum f(n)\\,\\text{sinc}^2(x-n)+\\sum f'(n)(x-n)\\,\\text{sinc}^2(x-n)$, với hàm giải $a(x)=\\text{sinc}^2x$ và $b(x)=x\\,\\text{sinc}^2x$.||Suppose $f$ is band-limited and needs ordinates at spacing 0.5, but only $\\text{III}f$ is given, i.e. spacing 1: the spectral islands overlap and $F$ cannot be recovered. If the slope $\\text{III}f'$ is also given, recovery is possible: in $-1<s<1$, $\\text{III}f=F(s+1)+F(s)+F(s-1)$ and $\\text{III}f'=i2\\pi(s+1)F(s+1)+i2\\pi sF(s)+i2\\pi(s-1)F(s-1)$, two equations for $F(s)$ since for each $s$ one of the three unknowns is zero (Bracewell, pp. 230 to 231). Result: $f(x)=\\sum f(n)\\,\\text{sinc}^2(x-n)+\\sum f'(n)(x-n)\\,\\text{sinc}^2(x-n)$, with solving functions $a(x)=\\text{sinc}^2x$ and $b(x)=x\\,\\text{sinc}^2x$.⟧</p>"
                 + F("⟦Lấy mẫu tung độ và độ dốc||Ordinate and slope sampling⟧", r"f(x)=\sum_nf(n)\operatorname{sinc}^2(x-n)+\sum_nf'(n)\,(x-n)\operatorname{sinc}^2(x-n)")),
                ("⟦Thử số: $f=\\text{sinc}\\,2x$||Numerical test: $f=\\text{sinc}\\,2x$⟧",
                 "<p>⟦$f(x)=\\text{sinc}\\,2x$ có phổ $\\tfrac12\\Pi(s/2)$, cắt tại 1. Mẫu tại các số nguyên chỉ là $f(0)=1$ và $0$ nơi khác, nhưng $f'(n)=1/n$ với $n\\ne0$. Dùng cả hai bộ giá trị: tại $x=0.37$ công thức cho {{os_val}} so với đúng {{os_true}}; lệch {{os_err}}. Chỉ với các tung độ, tổng $\\sum f(n)\\text{sinc}^2(x-n)=\\text{sinc}^2x$ = {{os_only}} sai rõ rệt.||$f(x)=\\text{sinc}\\,2x$ has spectrum $\\tfrac12\\Pi(s/2)$, cutoff 1. The samples at integers are just $f(0)=1$ and 0 elsewhere, but $f'(n)=1/n$ for $n\\ne0$. Using both sets: at $x=0.37$ the formula gives {{os_val}} against the exact {{os_true}}; deviation {{os_err}}. With the ordinates alone, $\\sum f(n)\\text{sinc}^2(x-n)=\\text{sinc}^2x$ = {{os_only}} is clearly wrong.⟧</p>"),
                ("⟦Lấy mẫu xen kẽ||Interlaced sampling⟧",
                 "<p>⟦Cho $\\text{III}f$ (mỗi mẫu thứ hai của bộ cần thiết) và một bộ bổ sung $\\text{III}_af=\\text{III}(x-a)f$ xen kẽ với bộ đầu. Mỗi bước nhảy thứ hai vượt khoảng tới hạn nhưng vẫn có nghiệm: $f=a(x)*\\text{III}f+b(x)*\\text{III}_af$, với $b(x)=a(-x)$ và $a(0)=1$, $a$ bằng 0 tại mọi điểm lấy mẫu khác. Nghiệm $a(x)=\\dfrac{\\cos(2\\pi x-\\pi a)-\\cos\\pi a}{2\\pi x\\sin\\pi a}$ (Linden, 1959; Bracewell, tr. 232 đến 233). Khi $a\\to0$ nó tiến về nghiệm tung độ và độ dốc. Số đo $a=0.2$: $a(0)$ = {{il_a0}}; các không điểm tại $x=1,2,-1$ và $x=0.2,1.2$ lệch {{il_zero}}; tái tạo $\\text{sinc}^2x$ (phổ tới 1) tại $x=0.3$ lệch {{il_err}}.||Given $\\text{III}f$ (every second sample of the necessary set) and a supplementary set $\\text{III}_af=\\text{III}(x-a)f$ interlaced with the first. Every second jump exceeds the critical interval yet a solution exists: $f=a(x)*\\text{III}f+b(x)*\\text{III}_af$, with $b(x)=a(-x)$ and $a(0)=1$, $a$ zero at every other sample point. The solution is $a(x)=\\dfrac{\\cos(2\\pi x-\\pi a)-\\cos\\pi a}{2\\pi x\\sin\\pi a}$ (Linden, 1959; Bracewell, pp. 232 to 233). As $a\\to0$ it tends to the ordinate-and-slope solution. Measured with $a=0.2$: $a(0)$ = {{il_a0}}; the zeros at $x=1,2,-1$ and $x=0.2,1.2$ deviate by {{il_zero}}; reconstructing $\\text{sinc}^2x$ (spectrum up to 1) at $x=0.3$ deviates by {{il_err}}.⟧</p>"),
                ("⟦Nhóm mẫu và chuỗi Maclaurin||Bunched samples and the Maclaurin series⟧",
                 "<p>⟦Có thể gộp mẫu thành nhóm bất kỳ cỡ nào, cách nhau khoảng rộng để giữ khoảng cách trung bình; Linden chứng minh rằng các tung độ và $n$ đạo hàm đầu, tại các điểm cách nhau $n+1$ lần khoảng thường, đủ xác định hàm giới hạn băng. Ở giới hạn $n\\to\\infty$, công thức trở thành chuỗi Maclaurin $f(0)+xf'(0)+\\tfrac{x^2}{2!}f''(0)+\\cdots$, vốn thường không hội tụ về $f(x)$ (chẳng hạn các hàm $\\Pi(ax)$ với mọi $a$ đều có cùng chuỗi Maclaurin). Bracewell kết luận nghi ngờ tính thực dụng của các định lý lấy mẫu bậc cao: trong thực hành nhiễu làm đạo hàm bậc cao hoặc sai phân hữu hạn sai lớn, và không thể bảo đảm giới hạn băng tuyệt đối (tr. 233 đến 234).||Samples may be bunched in groups of any size separated by wide intervals maintaining the original average spacing; Linden proved that the ordinates and first $n$ derivatives at points spaced $n+1$ times the usual spacing suffice to specify a band-limited function. In the limit $n\\to\\infty$ the formula becomes the Maclaurin series $f(0)+xf'(0)+\\tfrac{x^2}{2!}f''(0)+\\cdots$, which usually does not converge to $f(x)$ (for instance the functions $\\Pi(ax)$ for all $a$ have the same Maclaurin series). Bracewell concludes there is doubt about the practicality of higher-order sampling theorems: in practice noise ruins high-order derivatives or finite differences, and perfect band-limitation cannot be ensured (pp. 233 to 234).⟧</p>"),
                ("⟦Nội suy sinc chịu nhiễu||Sinc interpolation tolerates noise⟧",
                 "<p>⟦Nếu mẫu có sai số thì giá trị tái tạo cũng sai. Với nội suy điểm giữa tại $x=0$ từ mẫu ở $\\pm\\tfrac12,\\pm\\tfrac32,\\ldots$: $f(0)=0.6366[f(\\tfrac12)+f(-\\tfrac12)]-0.2122[\\ldots]+\\cdots$. Sai số ở hai mẫu gần nhất, mỗi sai số giảm còn 0.6366, có thể từ 0 (nếu triệt nhau) tới {{nz_max}} lần một sai số. Nếu các sai số độc lập, trung bình 0, phương sai $\\sigma^2$, phương sai tổng tại $x=0$ là $[\\ldots+(0.1273)^2+(0.2122)^2+(0.6366)^2+(0.6366)^2+\\ldots]\\sigma^2$, và chuỗi trong ngoặc là các giá trị của $\\text{sinc}^2x$ tại khoảng đơn vị nên cộng lại bằng {{nz_var}} (Bracewell, tr. 234 đến 235). Vậy giá trị nội suy chịu cùng sai số với dữ liệu: quy trình chịu nhiễu.||If the samples contain errors the reconstructed values are in error too. For midpoint interpolation at $x=0$ from samples at $\\pm\\tfrac12,\\pm\\tfrac32,\\ldots$: $f(0)=0.6366[f(\\tfrac12)+f(-\\tfrac12)]-0.2122[\\ldots]+\\cdots$. The errors at the two nearest samples, each reduced to 0.6366, can range from zero (if they cancel) up to {{nz_max}} times either error. If the errors are independent with zero mean and variance $\\sigma^2$, the total variance at $x=0$ is $[\\ldots+(0.1273)^2+(0.2122)^2+(0.6366)^2+(0.6366)^2+\\ldots]\\sigma^2$, and the series in brackets is the values of $\\text{sinc}^2x$ at unit intervals, which add up to {{nz_var}} (Bracewell, pp. 234 to 235). So the interpolated value has exactly the error of the data: the procedure is tolerant to noise.⟧</p>"),
                ("⟦Lấy mẫu xen kẽ khuếch đại nhiễu||Interlaced sampling amplifies noise⟧",
                 "<p>⟦Ở giữa khoảng rộng, bốn mẫu gần nhất đi vào với hệ số $a(\\tfrac12a+\\tfrac12)$, $b(-\\tfrac12a+\\tfrac12)$, $a(\\tfrac12a-\\tfrac12)$, $b(\\tfrac12a-\\tfrac12)$; do có $\\cot\\pi a$, giá trị có thể lớn, nên giá trị nội suy là hiệu của các số hạng lớn và sai số có thể lớn. Có thể viết $f(0)a(x)+f(a)b(x-a)$ thành trung bình cặp nhân một hệ số và hiệu hai mẫu sát nhau nhân một hệ số khác, và hệ số của số hạng hiệu có thể lớn: khi $a<0.2$ nó vượt 1, nên sai số ở số hạng hiệu bị khuếch đại (tr. 235 đến 236). Số đo với $a=0.2$: tổng bình phương hệ số tại điểm giữa khoảng rộng là {{il_amp}} (khuếch đại phương sai so với 1 của nội suy đều), và với $a=0.5$ (đều) là {{il_amp5}}.||At the middle of the wide interval the four nearest samples enter with coefficients $a(\\tfrac12a+\\tfrac12)$, $b(-\\tfrac12a+\\tfrac12)$, $a(\\tfrac12a-\\tfrac12)$, $b(\\tfrac12a-\\tfrac12)$; because of the factor $\\cot\\pi a$ the values may be large, so the interpolated value results from cancellation of large terms and the error may be large. A pair $f(0)a(x)+f(a)b(x-a)$ can be re-expressed as the mean of the pair times one coefficient plus the difference of two close samples times another, and the coefficient of the difference term can be large: for $a<0.2$ it exceeds unity, so errors in the difference term are amplified (pp. 235 to 236). Measured with $a=0.2$: the sum of squared coefficients at the middle of the wide interval is {{il_amp}} (variance amplification against 1 for uniform interpolation), and with $a=0.5$ (uniform) it is {{il_amp5}}.⟧</p>"),
                ("⟦Bài học thực hành||The practical lesson⟧",
                 UL(["⟦Nội suy sinc từ mẫu đều: bảo toàn phương sai nhiễu.||Sinc interpolation from uniform samples preserves noise variance.⟧",
                     "⟦Lấy mẫu xen kẽ hay có đạo hàm: khuếch đại nhiễu; phải ước lượng sai số và cả tương quan sai số giữa các mẫu kề.||Interlaced or slope sampling amplifies noise; the errors and the correlation between errors of neighbouring samples must be estimated.⟧",
                     "⟦Định lý lấy mẫu luôn đi kèm câu hỏi: hàm có thật sự giới hạn băng, và sai số do coi nó là giới hạn băng?||The sampling theorem always comes with a question: is the function really band-limited, and what is the error of taking it to be?⟧"])
                 + "<p>⟦(Bracewell, tr. 220, 234, 236). Ý này nối với chồng phổ của module 14 và với định lý lấy mẫu cho quá trình ngẫu nhiên của module 12.||(Bracewell, pp. 220, 234, 236). This connects with the aliasing of module 14 and with the sampling theorem for random processes of module 12.⟧</p>"),
                ("⟦Tự kiểm tra phần 2||Self-check, part 2⟧",
                 UL(["⟦Vì sao cần cả tung độ lẫn độ dốc khi chỉ có một nửa số mẫu?||Why are both ordinates and slopes needed when only half the samples are given?⟧",
                     "⟦Tại sao nội suy sinc không khuếch đại nhiễu độc lập?||Why does sinc interpolation not amplify independent noise?⟧",
                     "⟦Tại sao lấy mẫu xen kẽ gần nhau có hệ số $\\cot\\pi a$ lớn?||Why does closely interlaced sampling have a large $\\cot\\pi a$ coefficient?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: hai phương trình cho một ẩn $F(s)$ vì hai đảo kề bằng 0; $\\sum\\text{sinc}^2(n+x)=1$; hai mẫu gần nhau nên phải lấy hiệu nhỏ chia cho khoảng nhỏ.||Hints: two equations for one unknown $F(s)$ since the neighbouring islands vanish; $\\sum\\text{sinc}^2(n+x)=1$; the two samples are close so a small difference is divided by a small interval.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 3
        dict(
            title="⟦Chuỗi Fourier như một trường hợp của biến đổi||The Fourier series as a case of the transform⟧",
            scr=("⟦Sóng tuần hoàn (nốt nhạc kéo dài) gồm cơ bản và các họa âm; ta thường học chuỗi Fourier trước biến đổi, nhưng ở đây làm ngược lại.||A periodic wave (a sustained musical note) is composed of a fundamental and harmonics; one usually learns the Fourier series before the transform, but here we do the opposite.⟧",
                 "⟦Hàm tuần hoàn $p=\\text{III}*f$ có phổ là các xung tại số nguyên với cường độ $F(n)$; hệ số chuỗi là mẫu của biến đổi một chu kỳ.||A periodic function $p=\\text{III}*f$ has a spectrum of impulses at integers of strength $F(n)$; the series coefficients are samples of the transform of one period.⟧",
                 "⟦Cắt chuỗi là lọc thông thấp, nên có Gibbs: quá độ 9 phần trăm bước nhảy không mất đi khi thêm số hạng.||Truncating the series is low-pass filtering, hence Gibbs: an overshoot of 9 percent of the jump that does not go away as terms are added.⟧"),
            preview=["⟦Chuỗi Fourier từ biến đổi ở giới hạn||The Fourier series from the transform in the limit⟧", "⟦Hệ số bằng biến đổi hữu hạn||Coefficients through finite transforms⟧", "⟦Gibbs và shah tự biến đổi||Gibbs and the self-transforming shah⟧"],
            slides=[
                ("⟦Chuỗi Fourier: nhắc lại||The Fourier series: a reminder⟧",
                 "<p>⟦Hàm tuần hoàn $g(x)$ chu kỳ $T$, tần số $f=1/T$, có chuỗi $\\dfrac{a_0}2+\\sum(a_n\\cos2\\pi nfx+b_n\\sin2\\pi nfx)$ với $a_n=\\dfrac2T\\int g\\cos$, $b_n=\\dfrac2T\\int g\\sin$ (Bracewell, tr. 235 đến 236). Lý thuyết chuỗi nhằm chỉ ra chuỗi thường hội tụ, và khi hội tụ thì hội tụ về $\\tfrac12[g(x+0)+g(x-0)]$. Dirichlet đặt nền chặt chẽ năm 1829 sau thời kỳ tranh luận từ D. Bernoulli (1753, dây rung là chuỗi sin), Euler và Lagrange phản đối; khi Fourier khẳng định năm 1807, Lagrange đứng dậy nói không thể; cuộc tranh luận dẫn đến tích phân Riemann.||A periodic function $g(x)$ of period $T$, frequency $f=1/T$, has the series $\\dfrac{a_0}2+\\sum(a_n\\cos2\\pi nfx+b_n\\sin2\\pi nfx)$ with $a_n=\\dfrac2T\\int g\\cos$, $b_n=\\dfrac2T\\int g\\sin$ (Bracewell, pp. 235 to 236). Much of the theory of series shows that the series often converges, and when it converges it often converges to $\\tfrac12[g(x+0)+g(x-0)]$. Dirichlet started the rigorous development in 1829 after a controversial period going back to D. Bernoulli (1753, the vibrating string as a sine series), with Euler and Lagrange objecting; when Fourier made the claim in 1807, Lagrange rose and said it was impossible; the dispute led to the invention of the Riemann integral.⟧</p>"),
                ("⟦Hàm tuần hoàn là $\\text{III}*f$||A periodic function is $\\text{III}*f$⟧",
                 "<p>⟦Với $T=1$, $p(x)=\\text{III}(x)*f(x)=\\sum f(x-n)$ là hàm tuần hoàn chu kỳ 1 sao chép $f$ (đủ khả tích tuyệt đối để có biến đổi). $p$ không có biến đổi thường vì $\\int p$ không hội tụ, nên nhân với thừa số hội tụ $\\psi(x)=e^{-\\pi\\tau^2x^2}$ rồi cho $\\tau\\to0$: $\\Psi*P$ tiến về $P$, và $P(s)=\\text{III}(s)F(s)=\\sum F(n)\\delta(s-n)$. Vậy phổ của hàm tuần hoàn là tập xung mà cường độ là các mẫu cách đều của $F(s)$, biến đổi của đoạn một chu kỳ (Bracewell, tr. 237 đến 239). Tại $x$: $\\int\\text{III}(s)F(s)e^{i2\\pi sx}ds=\\sum F(n)e^{i2\\pi nx}$, và $a_n-ib_n=2F(n)$ đúng công thức hệ số quen thuộc.||With $T=1$, $p(x)=\\text{III}(x)*f(x)=\\sum f(x-n)$ is the periodic function of period 1 replicating $f$ (absolutely integrable enough to have a transform). $p$ has no regular transform since $\\int p$ does not converge, so multiply by a convergence factor $\\psi(x)=e^{-\\pi\\tau^2x^2}$ and let $\\tau\\to0$: $\\Psi*P$ tends to $P$, and $P(s)=\\text{III}(s)F(s)=\\sum F(n)\\delta(s-n)$. So the spectrum of a periodic function is a set of impulses whose strengths are equidistant samples of $F(s)$, the transform of a one-period segment (Bracewell, pp. 237 to 239). At $x$: $\\int\\text{III}(s)F(s)e^{i2\\pi sx}ds=\\sum F(n)e^{i2\\pi nx}$, and $a_n-ib_n=2F(n)$, exactly the familiar coefficient formula.⟧</p>"
                 + F("⟦Phổ của hàm tuần hoàn||Spectrum of a periodic function⟧", r"p(x)=\text{III}(x)*f(x)\ \supset\ \text{III}(s)\,F(s),\qquad a_n-ib_n=2F(n)")),
                ("⟦Ví dụ: chuỗi tam giác hẹp||Example: a train of narrow triangles⟧",
                 "<p>⟦$p=\\Lambda(10x)*\\text{III}(x)$ có biến đổi $\\tfrac1{10}\\text{sinc}^2\\tfrac{s}{10}\\,\\text{III}(s)$: hệ số $F(n)=\\tfrac1{10}\\text{sinc}^2\\tfrac n{10}$ chính là biến đổi của một tam giác đọc tại các số nguyên (hình 10.15, tr. 243 đến 245). Với chu kỳ $T$ bất kỳ, $F(s)\\text{III}(Ts)$: hệ số lấy từ cùng $F(s)$ ở các khoảng $s=T^{-1}$. Số đo: tổng $\\sum_nF(n)$ trên $|n|\\le20000$ bằng {{ft_sum}}, đúng $p(0)=1$; và với chuỗi xung chữ nhật $\\Pi(10x)*\\text{III}(x)$, $F(n)=\\tfrac1{10}\\text{sinc}\\tfrac n{10}$, tổng cắt cho {{ft_sum2}} tại đỉnh (giá trị trung bình tại chỗ nhảy chỉ đạt sau vô số số hạng).||$p=\\Lambda(10x)*\\text{III}(x)$ has transform $\\tfrac1{10}\\text{sinc}^2\\tfrac{s}{10}\\,\\text{III}(s)$: the coefficients $F(n)=\\tfrac1{10}\\text{sinc}^2\\tfrac n{10}$ are just the transform of one triangle read at integers (Fig. 10.15, pp. 243 to 245). For a general period $T$, $F(s)\\text{III}(Ts)$: the coefficients are obtained by reading off the same $F(s)$ at intervals $s=T^{-1}$. Measured: the sum $\\sum_nF(n)$ over $|n|\\le20000$ equals {{ft_sum}}, exactly $p(0)=1$; and for the rectangular pulse train $\\Pi(10x)*\\text{III}(x)$, $F(n)=\\tfrac1{10}\\text{sinc}\\tfrac n{10}$, the truncated sum gives {{ft_sum2}} at the peak (the mean value at the jump needs infinitely many terms).⟧</p>"),
                ("⟦Từ chuỗi tới tích phân Fourier||From the series to the Fourier integral⟧",
                 "<p>⟦Cách trình bày truyền thống đi theo lịch sử: hàm tuần hoàn $\\text{III}*f$ có phổ vạch $\\text{III}F$ (hệ số Fourier). Nếu kéo dài chu kỳ tới $\\tau$, các vạch dày hơn $\\tau$ lần và yếu đi $\\tau$ lần; cho chu kỳ tới vô hạn, xung $f$ không lặp lại, tổng lượng giác thành tích phân vô hạn, và tích phân hữu hạn xác định hệ số thành tích phân Fourier: ta được tích phân Fourier dấu cộng và dấu trừ (Bracewell, tr. 239). Theo cách nhìn ở đây, phổ vạch và hàm tuần hoàn nằm trong lý thuyết biến đổi, xử lý như mọi biến đổi bằng ký hiệu III và cùng sự thận trọng dành cho biến đổi ở giới hạn. Liên hệ tương tự: $\\text{III}(x/\\tau)\\supset|\\tau|\\text{III}(\\tau s)$ (định lý tỉ lệ).||The traditional presentation follows history: the periodic function $\\text{III}*f$ has a line spectrum $\\text{III}F$ (Fourier coefficients). If the period is lengthened to $\\tau$, the lines are packed $\\tau$ times more closely and are $\\tau$ times weaker; let the period become infinite, so that the pulse $f$ does not recur, the trigonometric sum passes into an infinite integral, and the finite integral specifying the coefficients does likewise: we get the plus-i and minus-i Fourier integrals (Bracewell, p. 239). On the view described here, line spectra and periodic functions are included in the theory of transforms, handled like other transforms by the III symbology with the same caution as for transforms in the limit. A related relation: $\\text{III}(x/\\tau)\\supset|\\tau|\\text{III}(\\tau s)$ (the similarity theorem).⟧</p>"),
                ("⟦Hiện tượng Gibbs||The Gibbs phenomenon⟧",
                 "<p>⟦Cắt chuỗi tới tần số $s_n$ là nhân phổ với $\\Pi(s/2s_n)$, tức chập $p$ với $(2n+1)s_0\\,\\text{sinc}[(2n+1)s_0x]$, diện tích 1. Gần một bước nhảy $\\text{sgn}\\,x$, tổng là $N\\text{sinc}\\,Nx*\\text{sgn}\\,x=\\dfrac2\\pi\\text{Si}(N\\pi x)$: dao động quanh $-1$, tăng biên độ khi tới gốc, qua 0, vọt lên cực đại {{gb_max}} rồi dao động tắt dần quanh $+1$ (Bracewell, tr. 240 đến 242). Thêm số hạng ($N$ tăng) chỉ dồn dao động về gần bước nhảy: quá độ vẫn $\\approx9$ phần trăm của bước nhảy ({{gb_pct}} phần trăm của độ nhảy 2), và tại điểm gián đoạn tổng tiến tới trung điểm. Số đo từ tổng riêng của sóng vuông với 200 số hạng lẻ: cực đại {{gb_sq}}.||Truncating the series at frequency $s_n$ multiplies the spectrum by $\\Pi(s/2s_n)$, i.e. convolves $p$ with $(2n+1)s_0\\,\\text{sinc}[(2n+1)s_0x]$, of unit area. Near a step $\\text{sgn}\\,x$ the sum is $N\\text{sinc}\\,Nx*\\text{sgn}\\,x=\\dfrac2\\pi\\text{Si}(N\\pi x)$: oscillating about $-1$, growing in amplitude toward the origin, passing through zero, shooting up to a maximum {{gb_max}} and then decaying oscillations about $+1$ (Bracewell, pp. 240 to 242). Adding terms (larger $N$) only crowds the oscillations toward the jump: the overshoot remains $\\approx9$ percent of the jump ({{gb_pct}} percent of the jump of 2), and at the discontinuity the sum tends to the midpoint. Measured from partial sums of a square wave with 200 odd terms: maximum {{gb_sq}}.⟧</p>{{fig:gibbs}}"),
                ("⟦Biến đổi hữu hạn||Finite transforms⟧",
                 "<p>⟦Khi biến độc lập không chạy từ $-\\infty$ tới $\\infty$, biến đổi hữu hạn $F(s,a,b)=\\int_a^bf(x)e^{-i2\\pi xs}dx$ có công thức nghịch đảo, định lý tích chập và định lý đạo hàm; đó là lý thuyết chuỗi Fourier. Ví dụ biến đổi sin trên $(0,\\tfrac12)$: $F_s(s)=\\int_0^{1/2}f\\sin2\\pi xs\\,dx$ và $f(x)=4\\sum_{s=1}^\\infty F_s(s)\\sin2\\pi xs$ (Bracewell, tr. 242). Cách nhất quán: thay tích phân hữu hạn bằng tích phân vô hạn của hàm bằng 0 ngoài $(a,b)$, nên mọi tính chất đặc biệt của biến đổi hữu hạn tự rơi ra. Số đo với $f=x(\\tfrac12-x)$ trên $(0,\\tfrac12)$: tại $x=0.2$ chuỗi sin cho {{fs_val}} so với đúng {{fs_true}}.||When the independent variable does not run from $-\\infty$ to $\\infty$, the finite transform $F(s,a,b)=\\int_a^bf(x)e^{-i2\\pi xs}dx$ has an inversion formula, a convolution theorem and derivative theorems; this is the theory of Fourier series. Example: the sine transform on $(0,\\tfrac12)$: $F_s(s)=\\int_0^{1/2}f\\sin2\\pi xs\\,dx$ and $f(x)=4\\sum_{s=1}^\\infty F_s(s)\\sin2\\pi xs$ (Bracewell, p. 242). The consistent way: replace integration over a finite range by infinite integration of a function that is zero outside $(a,b)$, so that all the special properties of finite transforms drop out. Measured with $f=x(\\tfrac12-x)$ on $(0,\\tfrac12)$: at $x=0.2$ the sine series gives {{fs_val}} against the exact {{fs_true}}.⟧</p>"),
                ("⟦Định lý đạo hàm có số hạng phụ||The derivative theorem with additive terms⟧",
                 "<p>⟦Đạo hàm của hàm bị cắt là xung tại $a$ và $b$, nên biến đổi của đạo hàm chứa hai số hạng tỉ lệ với các bước nhảy: $\\int_a^bf'e^{-i2\\pi xs}dx=i2\\pi sF(s,a,b)+f(b)e^{-i2\\pi bs}-f(a)e^{-i2\\pi as}$ (Bracewell, tr. 243). Trong lý thuyết tích phân vô hạn không cần nhắc điều này khi phát biểu định lý: biến đổi của $\\Pi'(x)$ là $i2\\pi s\\,\\text{sinc}\\,s=2i\\sin\\pi s$. Số đo với $f=x^2$ trên $(0,1)$ tại $s=0.3$: hai vế lệch {{fin_dev}}; và $2i\\sin\\pi s$ tại 0.3 có độ lớn {{fin_pi}}.||The derivative of a truncated function is impulsive at $a$ and $b$, so the transform of the derivative contains two extra terms proportional to the jumps: $\\int_a^bf'e^{-i2\\pi xs}dx=i2\\pi sF(s,a,b)+f(b)e^{-i2\\pi bs}-f(a)e^{-i2\\pi as}$ (Bracewell, p. 243). In the infinite-integral theory this need not be mentioned when stating the theorem: the transform of $\\Pi'(x)$ is $i2\\pi s\\,\\text{sinc}\\,s=2i\\sin\\pi s$. Measured with $f=x^2$ on $(0,1)$ at $s=0.3$: the two sides differ by {{fin_dev}}; and $2i\\sin\\pi s$ at 0.3 has magnitude {{fin_pi}}.⟧</p>"),
                ("⟦Shah là biến đổi của chính nó||The shah symbol is its own Fourier transform⟧",
                 "<p>⟦Xét dãy $f_\\tau(x)=\\tau^{-1}e^{-\\pi\\tau^2x^2}\\sum_ne^{-\\pi(x-n)^2/\\tau^2}$: hàng gai Gauss hẹp độ rộng $\\tau$ nhân bao Gauss rộng $\\tau^{-1}$; khi $\\tau\\to0$ mỗi gai co về một số nguyên và diện tích tiến về 1, nên là dãy xác định $\\text{III}(x)$. Do $\\sum_ne^{-\\pi(x-n)^2/\\tau^2}$ tuần hoàn nên khai triển chuỗi Fourier và áp định lý dịch: biến đổi là hàng gai Gauss độ rộng $\\tau$ với đỉnh nằm trên một đường Gauss rộng $\\tau^{-1}$, cũng xác định $\\text{III}(s)$ (Bracewell, tr. 246 đến 248). Cốt lõi là công thức tổng Poisson. Số đo $\\tau=0.3$, dịch 0.1: $\\sum_ne^{-\\pi(n-0.1)^2/\\tau^2}$ và $\\tau\\sum_ke^{-\\pi\\tau^2k^2}e^{-i2\\pi k(0.1)}$ lệch {{sh_dev}}.||Consider the sequence $f_\\tau(x)=\\tau^{-1}e^{-\\pi\\tau^2x^2}\\sum_ne^{-\\pi(x-n)^2/\\tau^2}$: a row of narrow Gaussian spikes of width $\\tau$ times a broad Gaussian envelope of width $\\tau^{-1}$; as $\\tau\\to0$ each spike narrows onto an integer and its area tends to 1, so it is a defining sequence for $\\text{III}(x)$. Since $\\sum_ne^{-\\pi(x-n)^2/\\tau^2}$ is periodic, expand it in a Fourier series and apply the shift theorem: the transform is a row of Gaussian spikes of width $\\tau$ with maxima on a broad Gaussian of width $\\tau^{-1}$, also defining $\\text{III}(s)$ (Bracewell, pp. 246 to 248). The core is the Poisson summation formula. Measured with $\\tau=0.3$, shift 0.1: $\\sum_ne^{-\\pi(n-0.1)^2/\\tau^2}$ and $\\tau\\sum_ke^{-\\pi\\tau^2k^2}e^{-i2\\pi k(0.1)}$ differ by {{sh_dev}}.⟧</p>"),
                ("⟦Tự kiểm tra phần 3||Self-check, part 3⟧",
                 UL(["⟦Hệ số $a_n-ib_n$ liên hệ thế nào với $F(n)$?||How is $a_n-ib_n$ related to $F(n)$?⟧",
                     "⟦Vì sao Gibbs không mất đi khi thêm số hạng?||Why does the Gibbs overshoot not go away when more terms are added?⟧",
                     "⟦Vì sao phổ của hàm tuần hoàn là tập xung?||Why is the spectrum of a periodic function a set of impulses?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: $a_n-ib_n=2F(n)$; cắt là chập với sinc hẹp hơn nhưng cùng biên độ; vì nó là chập với $\\text{III}$ nên phổ nhân với $\\text{III}$.||Hints: $a_n-ib_n=2F(n)$; truncation is convolution with a narrower sinc of the same amplitude; because it is a convolution with $\\text{III}$ so the spectrum is multiplied by $\\text{III}$.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 4
        dict(
            title="⟦Hàm trực giao, Gram-Schmidt và không gian tín hiệu||Orthogonal functions, Gram-Schmidt and signal space⟧",
            scr=("⟦Trong phát hiện tín hiệu ta so sánh nhiều tín hiệu có thể và cần khoảng cách và góc giữa chúng.||In signal detection we compare many possible signals and need distances and angles between them.⟧",
                 "⟦Biểu diễn mỗi tín hiệu bằng vector hệ số trên hệ cơ sở trực chuẩn cho hình học Euclid: độ dài là căn năng lượng, khoảng cách là căn năng lượng hiệu.||Representing each signal by a vector of coefficients on an orthonormal basis gives Euclidean geometry: length is root energy, distance is root difference energy.⟧",
                 "⟦Gram-Schmidt dựng cơ sở từ các tín hiệu cho trước; và các hệ số cho sai số năng lượng cực tiểu.||Gram-Schmidt builds the basis from the given signals; and the coefficients give minimum energy error.⟧"),
            preview=["⟦Trực giao và chuỗi Fourier tổng quát||Orthogonality and the generalised Fourier series⟧", "⟦Gram-Schmidt cổ điển và cải tiến||Classical and modified Gram-Schmidt⟧", "⟦Biểu diễn hình học||Geometric representation⟧"],
            slides=[
                ("⟦Từ vector tới hàm||From vectors to functions⟧",
                 "<p>⟦Hai vector $\\mathbf X,\\mathbf Y$ trực giao nếu tích trong bằng 0; độ dài $\\|\\mathbf X\\|=\\sqrt{\\mathbf X\\cdot\\mathbf X}$, và góc $\\cos\\theta=\\dfrac{\\mathbf X\\cdot\\mathbf Y}{\\|\\mathbf X\\|\\|\\mathbf Y\\|}$. Với hàm năng lượng hữu hạn trên $[0,T]$: năng lượng $E_k=\\int s_k^2dt$, chuẩn $\\|s_k\\|=E_k^{1/2}$, \"khoảng cách\" $\\|s_k-s_j\\|=[\\int(s_k-s_j)^2dt]^{1/2}$; trực giao nếu $\\int s_ks_jdt=0$ ($k\\ne j$), trực chuẩn nếu $=\\delta_{kj}$ (Barkat, mục 8.2, tr. 449 đến 451). Đó chính là các khái niệm mà Bracewell dùng khi xét năng lượng và định lý công suất (module 6).||Two vectors $\\mathbf X,\\mathbf Y$ are orthogonal if their inner product vanishes; length $\\|\\mathbf X\\|=\\sqrt{\\mathbf X\\cdot\\mathbf X}$, and angle $\\cos\\theta=\\dfrac{\\mathbf X\\cdot\\mathbf Y}{\\|\\mathbf X\\|\\|\\mathbf Y\\|}$. For finite-energy functions on $[0,T]$: energy $E_k=\\int s_k^2dt$, norm $\\|s_k\\|=E_k^{1/2}$, \"distance\" $\\|s_k-s_j\\|=[\\int(s_k-s_j)^2dt]^{1/2}$; orthogonal if $\\int s_ks_jdt=0$ ($k\\ne j$), orthonormal if $=\\delta_{kj}$ (Barkat, section 8.2, pp. 449 to 451). These are the concepts Bracewell uses for energy and the power theorem (module 6).⟧</p>"),
                ("⟦Chuỗi Fourier tổng quát||The generalised Fourier series⟧",
                 "<p>⟦Với hệ trực chuẩn $\\{\\phi_k\\}$ trên $[0,T]$, ta khai triển $s(t)=\\sum s_k\\phi_k(t)$ với $s_k=\\int_0^Ts(t)\\phi_k(t)dt$: các hệ số Fourier tổng quát (Barkat, mục 8.2.1, tr. 451 đến 452). Xấp xỉ hữu hạn $s_K=\\sum_{k\\le K}s_k\\phi_k$; sai số $\\varepsilon_K=s-s_K$; cực tiểu năng lượng sai số bằng cách đạo hàm theo $s_k$ cho đúng các hệ số trên (đạo hàm bậc hai bằng 2, dương). Hệ số cho năng lượng sai số $E_{\\varepsilon_K}=E-\\sum_{k\\le K}s_k^2$ (8.23) và, nếu hệ đầy đủ, đẳng thức Parseval $E=\\sum s_k^2$ (8.24), hội tụ theo trung bình (l.i.m.).||With an orthonormal set $\\{\\phi_k\\}$ on $[0,T]$, we expand $s(t)=\\sum s_k\\phi_k(t)$ with $s_k=\\int_0^Ts(t)\\phi_k(t)dt$: the generalised Fourier coefficients (Barkat, section 8.2.1, pp. 451 to 452). The finite approximation $s_K=\\sum_{k\\le K}s_k\\phi_k$; the error $\\varepsilon_K=s-s_K$; minimising the error energy by differentiating with respect to $s_k$ gives exactly these coefficients (second derivative 2, positive). The coefficients give the error energy $E_{\\varepsilon_K}=E-\\sum_{k\\le K}s_k^2$ (8.23) and, if the set is complete, Parseval's identity $E=\\sum s_k^2$ (8.24), convergence in the mean (l.i.m.).⟧</p>"
                 + F("⟦Sai số năng lượng||Error energy⟧", r"E_{\varepsilon_K}=\int_0^T\varepsilon_K^2dt=E-\sum_{k=1}^Ks_k^2\ \ge\ 0")),
                ("⟦Số đo: tín hiệu $s(t)=t$ trên $[0,1]$||Measured: the signal $s(t)=t$ on $[0,1]$⟧",
                 "<p>⟦Với cơ sở cosin $\\phi_0=1$, $\\phi_k=\\sqrt2\\cos k\\pi t$: $E=1/3$; $s_0=\\tfrac12$ và $s_k=\\sqrt2\\,[(-1)^k-1]/(k\\pi)^2$. Sau $K=5$ số hạng: năng lượng sai số {{gf_err5}} tính bằng $E-\\sum s_k^2$ và bằng tích phân trực tiếp của sai số bình phương; với $K=50$ còn {{gf_err50}}. Nó tiến về 0 khi $K\\to\\infty$: hệ đầy đủ.||With the cosine basis $\\phi_0=1$, $\\phi_k=\\sqrt2\\cos k\\pi t$: $E=1/3$; $s_0=\\tfrac12$ and $s_k=\\sqrt2\\,[(-1)^k-1]/(k\\pi)^2$. After $K=5$ terms: the error energy {{gf_err5}} computed as $E-\\sum s_k^2$ and by direct integration of the squared error; with $K=50$ it is {{gf_err50}}. It tends to 0 as $K\\to\\infty$: the set is complete.⟧</p>"),
                ("⟦Tương quan và bộ lọc phối hợp||Correlation and the matched filter⟧",
                 "<p>⟦Các hệ số $s_k=\\int s\\phi_k$ tính bằng phép tương quan (nhân với $\\phi_k$ rồi tích phân, hình 8.1). Cách tương đương: cho $s(t)$ qua các bộ lọc với đáp ứng xung $h_k(\\tau)=\\phi_k(T-\\tau)$ (bộ lọc phối hợp) rồi quan sát đầu ra tại $t=T$: $y_k(T)=\\int s(\\tau)\\phi_k(\\tau)d\\tau=s_k$ (Barkat, tr. 454 đến 455; nghiên cứu kỹ ở chương 10). Số đo: với $\\phi_1=\\sqrt2\\cos\\pi t$, $s_1$ = {{mf_s1}} bằng cả tương quan lẫn bộ lọc phối hợp lấy mẫu tại $T=1$. Đây là phép chập của module 3 và định lý tương quan của module 6 áp dụng cho phát hiện.||The coefficients $s_k=\\int s\\phi_k$ are computed by a correlation operation (multiply by $\\phi_k$ and integrate, Fig. 8.1). An equivalent operation: pass $s(t)$ through filters with impulse response $h_k(\\tau)=\\phi_k(T-\\tau)$ (matched filters) and observe the outputs at $t=T$: $y_k(T)=\\int s(\\tau)\\phi_k(\\tau)d\\tau=s_k$ (Barkat, pp. 454 to 455; studied in detail in chapter 10). Measured: with $\\phi_1=\\sqrt2\\cos\\pi t$, $s_1$ = {{mf_s1}} by both correlation and a matched filter sampled at $T=1$. This is the convolution of module 3 and the correlation theorem of module 6 applied to detection.⟧</p>"),
                ("⟦Gram-Schmidt||The Gram-Schmidt procedure⟧",
                 "<p>⟦Cho $M$ tín hiệu $s_1,\\ldots,s_M$ thực, thời lượng $T$, muốn biểu diễn bằng $K\\le M$ hàm trực chuẩn. Bước 1: $\\phi_1=s_1/\\sqrt{E_1}$. Bước 2: chiếu $s_2$ lên $\\phi_1$, $s_{21}=\\int s_2\\phi_1$, trừ đi $f_2=s_2-s_{21}\\phi_1$ (trực giao với $\\phi_1$) rồi chuẩn hóa $\\phi_2=f_2/\\sqrt{E_2-s_{21}^2}$. Tổng quát $f_k=s_k-\\sum_{j<k}s_{kj}\\phi_j$, $\\phi_k=f_k/\\|f_k\\|$ (Barkat, mục 8.2.2, tr. 455 đến 457). Nếu $M$ tín hiệu độc lập tuyến tính thì $K=M$; hàm phụ thuộc cho $f_k=0$ và bị bỏ qua.||Given $M$ real signals $s_1,\\ldots,s_M$ of duration $T$, represent them with $K\\le M$ orthonormal functions. Step 1: $\\phi_1=s_1/\\sqrt{E_1}$. Step 2: project $s_2$ on $\\phi_1$, $s_{21}=\\int s_2\\phi_1$, subtract to get $f_2=s_2-s_{21}\\phi_1$ (orthogonal to $\\phi_1$) and normalise $\\phi_2=f_2/\\sqrt{E_2-s_{21}^2}$. In general $f_k=s_k-\\sum_{j<k}s_{kj}\\phi_j$, $\\phi_k=f_k/\\|f_k\\|$ (Barkat, section 8.2.2, pp. 455 to 457). If the $M$ signals are linearly independent then $K=M$; a dependent function gives $f_k=0$ and is skipped.⟧</p>"),
                ("⟦Ví dụ 8.1: bốn tín hiệu chữ nhật, $K=3$||Example 8.1: four rectangular signals, $K=3$⟧",
                 "<p>⟦Ba tín hiệu chữ nhật trên ba phần ba của $[0,T]$ và $s_4=s_2-s_3$; $\\phi_1,\\phi_2,\\phi_3$ là ba chữ nhật chuẩn hóa $\\sqrt{3/T}$ trên ba đoạn, còn $s_4$ là tổ hợp tuyến tính của $s_2$ và $s_3$: số chiều của không gian tín hiệu $K=3$ (Barkat, ví dụ 8.1, tr. 458). Số đo với $T=1$ và lưới mịn: hạng của ma trận Gram bằng {{gs_K}}; ba hàm cơ sở có năng lượng {{gs_E}} và trực giao (lệch {{gs_orth}}); các tọa độ của $s_4$ là $(0,1,-1)/\\sqrt3$ theo thang $\\sqrt{T/3}$: độ dài {{gs_len4}}.||Three rectangular signals on the three thirds of $[0,T]$ and $s_4=s_2-s_3$; $\\phi_1,\\phi_2,\\phi_3$ are the three normalised rectangles $\\sqrt{3/T}$ on the three segments, while $s_4$ is a linear combination of $s_2$ and $s_3$: the dimension of the signal space is $K=3$ (Barkat, example 8.1, p. 458). Measured with $T=1$ on a fine grid: the rank of the Gram matrix is {{gs_K}}; the three basis functions have energy {{gs_E}} and are orthogonal (deviation {{gs_orth}}); the coordinates of $s_4$ are $(0,1,-1)$ in units $\\sqrt{T/3}$: length {{gs_len4}}.⟧</p>"),
                ("⟦Gram-Schmidt cải tiến ổn định số||The modified Gram-Schmidt is numerically stable⟧",
                 "<p>⟦Trừ đồng thời mọi thành phần theo $\\phi_1,\\ldots,\\phi_{k-1}$ đôi khi mất ổn định số. Bản cải tiến (MGS) trừ ngay từng hình chiếu: $s_k^{(1)}=s_k-s_{k1}\\phi_1$, rồi chiếu $s_k^{(1)}$ (chứ không phải $s_k$) lên $\\phi_2$, trừ, và cứ thế; về nguyên tắc cùng kết quả với CGS nhưng ổn định và hiệu quả hơn (Barkat, tr. 457). Số đo với 12 cột của ma trận Hilbert (gần phụ thuộc tuyến tính): độ lệch $\\|Q^TQ-I\\|$ của CGS là {{cgs_err}} còn của MGS là {{mgs_err}}, và với ma trận tốt (ngẫu nhiên) cả hai gần nhau ({{cgs_good}} và {{mgs_good}}).||Subtracting all the components along $\\phi_1,\\ldots,\\phi_{k-1}$ at once is sometimes numerically unstable. The modified procedure (MGS) subtracts each projection immediately: $s_k^{(1)}=s_k-s_{k1}\\phi_1$, then projects $s_k^{(1)}$ (not $s_k$) on $\\phi_2$, subtracts, and so on; in principle the same result as CGS but stable and efficient (Barkat, p. 457). Measured with the 12 columns of a Hilbert matrix (nearly linearly dependent): the deviation $\\|Q^TQ-I\\|$ of CGS is {{cgs_err}} while that of MGS is {{mgs_err}}, and with a well-conditioned (random) matrix both are close ({{cgs_good}} and {{mgs_good}}).⟧</p>"),
                ("⟦Biểu diễn hình học||Geometric representation⟧",
                 "<p>⟦Mỗi tín hiệu $s_k$ ứng với vector hệ số $\\mathbf s_k=[s_{k1},\\ldots,s_{kK}]^T$, một điểm trong không gian Euclid $K$ chiều (không gian tín hiệu) mà các trục là $\\phi_1,\\ldots,\\phi_K$. Do hệ đầy đủ: $\\|\\mathbf s_k\\|^2=\\sum s_{kj}^2=E_k$; khoảng cách $\\|\\mathbf s_k-\\mathbf s_j\\|^2=\\int[s_k-s_j]^2dt$; và hệ số tương quan $\\rho_{kj}=\\dfrac{\\int s_ks_jdt}{\\sqrt{E_kE_j}}=\\dfrac{\\mathbf s_k^T\\mathbf s_j}{\\|\\mathbf s_k\\|\\|\\mathbf s_j\\|}$ (Barkat, mục 8.2.3, tr. 458 đến 459). Với hai tín hiệu ở ví dụ 8.1 ($s_2$ và $s_3$): khoảng cách theo hệ số {{gr_d}} bằng khoảng cách tích phân {{gr_di}}, và $\\rho_{23}$ = {{gr_rho}}. Sau này (module 21) ta dùng hình học này để tìm vùng quyết định trong phát hiện $M$ tín hiệu.||Each signal $s_k$ corresponds to a coefficient vector $\\mathbf s_k=[s_{k1},\\ldots,s_{kK}]^T$, a point in a $K$-dimensional Euclidean space (the signal space) whose axes are $\\phi_1,\\ldots,\\phi_K$. Since the set is complete: $\\|\\mathbf s_k\\|^2=\\sum s_{kj}^2=E_k$; the distance $\\|\\mathbf s_k-\\mathbf s_j\\|^2=\\int[s_k-s_j]^2dt$; and the correlation coefficient $\\rho_{kj}=\\dfrac{\\int s_ks_jdt}{\\sqrt{E_kE_j}}=\\dfrac{\\mathbf s_k^T\\mathbf s_j}{\\|\\mathbf s_k\\|\\|\\mathbf s_j\\|}$ (Barkat, section 8.2.3, pp. 458 to 459). For two signals of example 8.1 ($s_2$ and $s_3$): the distance from coefficients {{gr_d}} equals the integral distance {{gr_di}}, and $\\rho_{23}$ = {{gr_rho}}. Later (module 21) we use this geometry to find decision regions in $M$-ary detection.⟧</p>"),
                ("⟦Chuỗi Fourier như một hệ trực chuẩn||The Fourier series as an orthonormal set||⟧".replace("||⟧","⟧"),
                 "<p>⟦Cosin $\\phi_k=\\sqrt{2/T}\\cos(2k\\pi t/T)$, $k=1,2,3$, trực chuẩn trên $[0,T]$, và ba vector $\\mathbf s_k$ trong không gian tín hiệu ba chiều là ba điểm trên các trục (Barkat, mục 8.2.4, tr. 463 đến 466). Sóng $\\cos,\\sin$ với tần số bội của $1/T$ là hệ trực giao đầy đủ nên mọi tín hiệu năng lượng hữu hạn khai triển theo chuỗi Fourier: đó là cùng hệ số $a_n,b_n$ của Bracewell (phần 3), giờ thấy như hệ số tổng quát $s_k$. Số đo: ma trận tích trong của ba cosin lệch khỏi ma trận đơn vị {{fo_dev}}; và với sóng vuông $\\pm1$ có năng lượng 1, ba họa âm lẻ đầu chứa {{fo_frac}} năng lượng ($8/\\pi^2(1+1/9+1/25)$).||The cosines $\\phi_k=\\sqrt{2/T}\\cos(2k\\pi t/T)$, $k=1,2,3$, are orthonormal on $[0,T]$, and the three vectors $\\mathbf s_k$ in the three-dimensional signal space are three points on the axes (Barkat, section 8.2.4, pp. 463 to 466). Cosines and sines at multiples of $1/T$ form a complete orthogonal set so every finite-energy signal expands in a Fourier series: the same coefficients $a_n,b_n$ as in Bracewell (part 3), now seen as generalised coefficients $s_k$. Measured: the inner-product matrix of the three cosines deviates from the identity by {{fo_dev}}; and for a $\\pm1$ square wave of energy 1 the first three odd harmonics hold {{fo_frac}} of the energy ($8/\\pi^2(1+1/9+1/25)$).⟧</p>"),
                ("⟦Tự kiểm tra phần 4||Self-check, part 4⟧",
                 UL(["⟦Năng lượng sai số của khai triển $K$ số hạng là gì?||What is the error energy of a $K$-term expansion?⟧",
                     "⟦Khi nào bước Gram-Schmidt cho $f_k=0$?||When does a Gram-Schmidt step give $f_k=0$?⟧",
                     "⟦Khoảng cách giữa hai tín hiệu trong không gian tín hiệu bằng gì?||What is the distance between two signals in signal space?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: $E-\\sum s_k^2$; khi $s_k$ phụ thuộc tuyến tính vào các tín hiệu trước; căn năng lượng của hiệu $\\int(s_k-s_j)^2$.||Hints: $E-\\sum s_k^2$; when $s_k$ is linearly dependent on the earlier signals; the root of the energy of the difference $\\int(s_k-s_j)^2$.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 5
        dict(
            title="⟦Phương trình tích phân và khai triển Karhunen-Loève||Integral equations and the Karhunen-Loève expansion⟧",
            scr=("⟦Hệ trực giao tốt nhất cho một quá trình ngẫu nhiên là hệ làm các hệ số không tương quan.||The best orthogonal set for a random process is the one that makes the coefficients uncorrelated.⟧",
                 "⟦Đó là các hàm riêng của nhân tự hiệp phương sai: một phương trình tích phân, được giải qua phương trình vi phân tương ứng nhờ hàm Green.||These are the eigenfunctions of the autocovariance kernel: an integral equation, solved through the corresponding differential equation using Green's function.⟧",
                 "⟦Wiener, quá trình có tự tương quan mũ và nhiễu trắng là ba trường hợp có lời giải.||The Wiener process, a process with exponential autocorrelation and white noise are three solvable cases.⟧"),
            preview=["⟦Hàm Green và phương trình tích phân||Green's function and integral equations⟧", "⟦Khai triển Karhunen-Loève||The Karhunen-Loève expansion⟧", "⟦Wiener, mũ, nhiễu trắng||Wiener, exponential, white noise⟧"],
            slides=[
                ("⟦Toán tử vi phân tuyến tính và hàm Green||Linear differential operators and Green's function⟧",
                 "<p>⟦Phương trình vi phân với điều kiện biên tương ứng một phương trình tích phân qua hàm Green $k(u,t)$ (\"nhân\"): nghiệm của $L\\phi=f$ là $\\phi(t)=\\int k(u,t)f(u)du$ (Barkat, mục 8.3.1, tr. 470 đến 471). Bài toán riêng $\\phi''+\\lambda\\phi=0$ với $\\phi(0)=\\phi(1)=0$ cho $\\phi_k=\\sin k\\pi t$, $\\lambda_k=k^2\\pi^2$ (8.104, 8.105), và tương đương phương trình tích phân thuần nhất $\\phi(t)=\\lambda\\int k(u,t)\\phi(u)du$, nhân là hàm Green chứa điều kiện biên. Mercer: $k(u,t)=\\sum\\phi_k(t)\\phi_k(u)/\\lambda_k$ (8.103).||A differential equation with boundary conditions corresponds to an integral equation through Green's function $k(u,t)$ (the \"kernel\"): the solution of $L\\phi=f$ is $\\phi(t)=\\int k(u,t)f(u)du$ (Barkat, section 8.3.1, pp. 470 to 471). The eigenproblem $\\phi''+\\lambda\\phi=0$ with $\\phi(0)=\\phi(1)=0$ gives $\\phi_k=\\sin k\\pi t$, $\\lambda_k=k^2\\pi^2$ (8.104, 8.105), and is equivalent to the homogeneous integral equation $\\phi(t)=\\lambda\\int k(u,t)\\phi(u)du$, the kernel being the Green's function containing the boundary conditions. Mercer: $k(u,t)=\\sum\\phi_k(t)\\phi_k(u)/\\lambda_k$ (8.103).⟧</p>"),
                ("⟦Số đo: nhân Green và định lý Mercer||Measured: the Green kernel and Mercer's theorem⟧",
                 "<p>⟦Với $\\phi''+\\lambda\\phi=0$, $\\phi(0)=\\phi(1)=0$ nhân là $k(u,t)=\\min(u,t)[1-\\max(u,t)]$. Rời rạc hóa nhân trên 800 điểm, các trị riêng lớn nhất của toán tử tích phân là $1/\\lambda_k$: $1/\\pi^2$ = {{gr_e1}}, $1/4\\pi^2$ = {{gr_e2}}, và kiểm bằng ma trận số. Mercer tại $(u,t)=(0.3,0.6)$: $k$ = {{gr_k}} bằng tổng $\\sum2\\sin k\\pi u\\sin k\\pi t/k^2\\pi^2$ = {{gr_mer}}. Với bài toán $\\phi'(0)=\\phi(1)=0$ (ví dụ trong sách): $\\lambda_k=(2k-1)^2\\pi^2/4$, $\\phi_k=\\sqrt2\\cos\\frac{(2k-1)\\pi}2t$, nhân $k(u,t)=1-\\max(u,t)$: trị riêng đầu của toán tử {{gr_f1}} $=4/\\pi^2$.||For $\\phi''+\\lambda\\phi=0$, $\\phi(0)=\\phi(1)=0$ the kernel is $k(u,t)=\\min(u,t)[1-\\max(u,t)]$. Discretising the kernel on 800 points, the largest eigenvalues of the integral operator are $1/\\lambda_k$: $1/\\pi^2$ = {{gr_e1}}, $1/4\\pi^2$ = {{gr_e2}}, checked with the numerical matrix. Mercer at $(u,t)=(0.3,0.6)$: $k$ = {{gr_k}} equals the sum $\\sum2\\sin k\\pi u\\sin k\\pi t/k^2\\pi^2$ = {{gr_mer}}. For the problem $\\phi'(0)=\\phi(1)=0$ (an example in the book): $\\lambda_k=(2k-1)^2\\pi^2/4$, $\\phi_k=\\sqrt2\\cos\\frac{(2k-1)\\pi}2t$, kernel $k(u,t)=1-\\max(u,t)$: the first eigenvalue of the operator is {{gr_f1}} $=4/\\pi^2$.⟧</p>"),
                ("⟦Tương tự ma trận||The matrix analogy⟧",
                 "<p>⟦Phương trình vi phân có điều kiện biên tương tự một phương trình ma trận vuông $A\\mathbf x=\\mathbf y$; nghịch đảo $A^{-1}$ tương tự nhân $k(u,t)$: $x_i=\\sum(A^{-1})_{ij}y_j$ tương tự $\\phi(t)=\\int k(u,t)f(u)du$. Nếu toán tử $T$ khả nghịch và $T\\mathbf x=\\lambda\\mathbf x$ thì $T^{-1}\\mathbf x=\\lambda^{-1}\\mathbf x$: hàm riêng của toán tử và của nghịch đảo giống nhau, trị riêng nghịch đảo nhau. Hệ vi phân khả nghịch khi và chỉ khi $\\lambda=0$ không là trị riêng. Vì phương trình tích phân khó giải, ta quay lại dạng vi phân (Barkat, mục 8.3.3, tr. 479 đến 480). Số đo: ma trận sai phân bậc hai $A$ ($50\\times50$, hai đầu bằng 0) có trị riêng nhỏ nhất {{ma_a}} còn $A^{-1}$ có trị riêng lớn nhất {{ma_k}}, nghịch đảo của nhau.||A differential equation with boundary conditions is analogous to a square matrix equation $A\\mathbf x=\\mathbf y$; the inverse $A^{-1}$ is analogous to the kernel $k(u,t)$: $x_i=\\sum(A^{-1})_{ij}y_j$ is analogous to $\\phi(t)=\\int k(u,t)f(u)du$. If an operator $T$ is invertible and $T\\mathbf x=\\lambda\\mathbf x$ then $T^{-1}\\mathbf x=\\lambda^{-1}\\mathbf x$: the eigenfunctions of the operator and its inverse are identical, the eigenvalues reciprocal. A differential system is invertible if and only if $\\lambda=0$ is not an eigenvalue. Since integral equations are hard to solve we return to the differential form (Barkat, section 8.3.3, pp. 479 to 480). Measured: the second-difference matrix $A$ ($50\\times50$, zero ends) has smallest eigenvalue {{ma_a}} while $A^{-1}$ has largest eigenvalue {{ma_k}}, reciprocal to each other.⟧</p>"),
                ("⟦Khai triển Karhunen-Loève||The Karhunen-Loève expansion⟧",
                 "<p>⟦Ta muốn $X(t)=\\sum X_k\\phi_k(t)$ trên $[0,T]$, với $X_k=\\int X\\phi_k$ và hội tụ theo bình phương trung bình (vì hội tụ thường đòi mọi hàm mẫu thỏa mãn là không thực tế). Chọn $\\{\\phi_k\\}$ để các $X_k$ không tương quan: $E[X_kX_j]=\\lambda_k\\delta_{kj}$; điều đó dẫn tới phương trình tích phân thuần nhất $\\int K_{xx}(t,u)\\phi_j(u)du=\\lambda_j\\phi_j(t)$, nhân là hàm tự hiệp phương sai (Barkat, mục 8.4, tr. 480 đến 482). Mercer: $K_{xx}(t,u)=\\sum\\lambda_k\\phi_k(t)\\phi_k(u)$. Nếu $K_{xx}$ xác định dương thì các hàm riêng tạo hệ trực chuẩn đầy đủ. Năng lượng trung bình $E\\int X^2dt=\\int K_{xx}(t,t)dt=\\sum\\lambda_k$ (8.119 đến 8.121), và sai số bình phương trung bình $\\varepsilon_K(t)=K_{xx}(t,t)-\\sum_{k\\le K}\\lambda_k\\phi_k^2(t)\\to0$.||We want $X(t)=\\sum X_k\\phi_k(t)$ on $[0,T]$, with $X_k=\\int X\\phi_k$ and mean-square convergence (since ordinary convergence would require all sample functions to satisfy it, which is impractical). Choose $\\{\\phi_k\\}$ so the $X_k$ are uncorrelated: $E[X_kX_j]=\\lambda_k\\delta_{kj}$; this leads to the homogeneous integral equation $\\int K_{xx}(t,u)\\phi_j(u)du=\\lambda_j\\phi_j(t)$, the kernel being the autocovariance function (Barkat, section 8.4, pp. 480 to 482). Mercer: $K_{xx}(t,u)=\\sum\\lambda_k\\phi_k(t)\\phi_k(u)$. If $K_{xx}$ is positive definite the eigenfunctions form a complete orthonormal set. The mean energy is $E\\int X^2dt=\\int K_{xx}(t,t)dt=\\sum\\lambda_k$ (8.119 to 8.121), and the mean-square error $\\varepsilon_K(t)=K_{xx}(t,t)-\\sum_{k\\le K}\\lambda_k\\phi_k^2(t)\\to0$.⟧</p>"
                 + F("⟦Khai triển Karhunen-Loève||Karhunen-Loève expansion⟧", r"X(t)=\sum_kX_k\phi_k(t),\quad \int_0^TK_{xx}(t,u)\phi_k(u)\,du=\lambda_k\phi_k(t),\quad E[X_kX_j]=\lambda_k\delta_{kj}")),
                ("⟦Quá trình Gauss trong khai triển||The Gaussian process in the expansion⟧",
                 "<p>⟦$K$ biến ngẫu nhiên đồng thời Gauss nếu $Y=\\sum g_kY_k$ Gauss với mọi $g_k$; với số vô hạn cần $E[Y^2]$ hữu hạn. Quá trình $X(t)$ Gauss trên $[T_i,T_f]$ nếu mọi tổ hợp tuyến tính của nó là Gauss; khi đó các hệ số Karhunen-Loève không tương quan cũng độc lập, đều Gauss (Barkat, mục 8.4.1, tr. 483 đến 487). Đó là lý do khai triển này rất tiện cho phát hiện tín hiệu trong nhiễu Gauss: mỗi thành phần độc lập với phương sai $\\lambda_k$. Số đo: $10^5$ đường Wiener chiếu lên hàm riêng thứ nhất và thứ hai: tương quan giữa $X_1,X_2$ = {{kl_corr}} và độ nhọn dư của $X_1$ = {{kl_kurt}} (Gauss: 0).||$K$ random variables are jointly Gaussian if $Y=\\sum g_kY_k$ is Gaussian for all $g_k$; with an infinite number $E[Y^2]$ must be finite. A process $X(t)$ is Gaussian on $[T_i,T_f]$ if every linear combination of it is Gaussian; then the uncorrelated Karhunen-Loève coefficients are also independent, all Gaussian (Barkat, section 8.4.1, pp. 483 to 487). This is why the expansion is so convenient for detecting signals in Gaussian noise: each component is independent with variance $\\lambda_k$. Measured: $10^5$ Wiener paths projected on the first and second eigenfunctions: the correlation between $X_1,X_2$ = {{kl_corr}} and the excess kurtosis of $X_1$ = {{kl_kurt}} (Gaussian: 0).⟧</p>"),
                ("⟦Quá trình Wiener||The Wiener process⟧",
                 "<p>⟦Hiệp phương sai $K_{xx}(t,u)=\\alpha\\min(t,u)$ (gia số độc lập). Phương trình tích phân $\\lambda\\phi(t)=\\alpha\\int_0^tu\\phi(u)du+\\alpha t\\int_t^T\\phi(u)du$; đạo hàm hai lần cho $\\lambda\\phi''+\\alpha\\phi=0$ với $\\phi(0)=0$, $\\phi'(T)=0$, nên $\\lambda_n=\\dfrac{\\alpha T^2}{(n-\\frac12)^2\\pi^2}$ và $\\phi_n(t)=\\sqrt{2/T}\\sin\\dfrac{(n-\\frac12)\\pi t}{T}$ (Barkat, mục 8.4.3, tr. 492 đến 493). Với $\\alpha=1$, $T=1$: $\\lambda_1,\\ldots,\\lambda_4$ = {{kl_w1}}, {{kl_w2}}, {{kl_w3}}, {{kl_w4}} theo công thức và theo phân tích trị riêng ma trận $800\\times800$; năng lượng trung bình $\\sum\\lambda_n=\\alpha T^2/2$ = {{kl_sum}}; và phương sai của $X_1$ trong mô phỏng {{kl_v1}}.||The covariance is $K_{xx}(t,u)=\\alpha\\min(t,u)$ (independent increments). The integral equation $\\lambda\\phi(t)=\\alpha\\int_0^tu\\phi(u)du+\\alpha t\\int_t^T\\phi(u)du$; differentiating twice gives $\\lambda\\phi''+\\alpha\\phi=0$ with $\\phi(0)=0$, $\\phi'(T)=0$, so $\\lambda_n=\\dfrac{\\alpha T^2}{(n-\\frac12)^2\\pi^2}$ and $\\phi_n(t)=\\sqrt{2/T}\\sin\\dfrac{(n-\\frac12)\\pi t}{T}$ (Barkat, section 8.4.3, pp. 492 to 493). With $\\alpha=1$, $T=1$: $\\lambda_1,\\ldots,\\lambda_4$ = {{kl_w1}}, {{kl_w2}}, {{kl_w3}}, {{kl_w4}} by formula and by eigendecomposition of an $800\\times800$ matrix; the mean energy $\\sum\\lambda_n=\\alpha T^2/2$ = {{kl_sum}}; and the variance of $X_1$ in simulation {{kl_v1}}.⟧</p>{{fig:kl_eig}}"),
                ("⟦Phổ công suất hữu tỉ: tự tương quan mũ||Rational power spectra: exponential autocorrelation⟧",
                 "<p>⟦Với phổ $S_{xx}(\\omega)=N(\\omega^2)/D(\\omega^2)$ hữu tỉ, phương trình tích phân trở thành phương trình vi phân hệ số hằng: $[\\lambda D(-p^2)-N(-p^2)]\\Phi(p)=0$ với $p=d/dt$ (Barkat, mục 8.4.2, tr. 487 đến 489). Ví dụ 8.4: $S_{xx}=2\\alpha\\sigma^2/(\\omega^2+\\alpha^2)$, $R=\\sigma^2e^{-\\alpha|\\tau|}$, khoảng $[-T,T]$: $\\phi''+\\beta^2\\phi=0$ với $\\lambda=2\\alpha\\sigma^2/(\\alpha^2+\\beta^2)$; nghiệm chẵn $\\cos\\beta t$ với $\\beta\\tan\\beta T=\\alpha$ và lẻ $\\sin\\beta t$ với $\\beta\\cot\\beta T=-\\alpha$ (tr. 490 đến 491). Trường hợp $\\lambda\\ge2\\sigma^2/\\alpha$ không là trị riêng. Với $\\alpha=\\sigma=T=1$: $\\lambda_1,\\lambda_2$ = {{ou_l1}}, {{ou_l2}} từ nghiệm $\\beta$ và từ ma trận nhân; tổng bốn trị riêng đầu chiếm {{ou_frac}} năng lượng $\\int K(t,t)dt=2$.||With a rational spectrum $S_{xx}(\\omega)=N(\\omega^2)/D(\\omega^2)$ the integral equation becomes a differential equation with constant coefficients: $[\\lambda D(-p^2)-N(-p^2)]\\Phi(p)=0$ with $p=d/dt$ (Barkat, section 8.4.2, pp. 487 to 489). Example 8.4: $S_{xx}=2\\alpha\\sigma^2/(\\omega^2+\\alpha^2)$, $R=\\sigma^2e^{-\\alpha|\\tau|}$, interval $[-T,T]$: $\\phi''+\\beta^2\\phi=0$ with $\\lambda=2\\alpha\\sigma^2/(\\alpha^2+\\beta^2)$; even solutions $\\cos\\beta t$ with $\\beta\\tan\\beta T=\\alpha$ and odd $\\sin\\beta t$ with $\\beta\\cot\\beta T=-\\alpha$ (pp. 490 to 491). The case $\\lambda\\ge2\\sigma^2/\\alpha$ is not an eigenvalue. With $\\alpha=\\sigma=T=1$: $\\lambda_1,\\lambda_2$ = {{ou_l1}}, {{ou_l2}} from the roots $\\beta$ and from the kernel matrix; the first four eigenvalues hold {{ou_frac}} of the energy $\\int K(t,t)dt=2$.⟧</p>"),
                ("⟦Nhiễu trắng||White noise⟧",
                 "<p>⟦Nhiễu trắng có $R_{xx}(\\tau)=\\tfrac{N_0}2\\delta(\\tau)$: nhân là xung, phương trình $\\lambda\\phi(t)=\\tfrac{N_0}2\\phi(t)$ nghiệm với mọi hàm $\\phi$, nên mọi hệ trực chuẩn đầy đủ đều là hàm riêng, với trị riêng bằng nhau $\\lambda=N_0/2$ (Barkat, mục 8.4.4, tr. 493 đến 495). Vậy các hệ số theo cơ sở bất kỳ đều không tương quan, phương sai $N_0/2$; đó là lý do vì sao trong phát hiện tín hiệu trong nhiễu trắng Gauss ta có thể chọn cơ sở thuận tiện (module 21 và 25). Số đo với $N_0/2=1$: phương sai các hệ số theo cơ sở cosin và theo cơ sở sin cùng {{wn_c}} và {{wn_s}}; tương quan giữa hệ số cosin đầu và hệ số sin đầu {{wn_x}}.||White noise has $R_{xx}(\\tau)=\\tfrac{N_0}2\\delta(\\tau)$: the kernel is an impulse, the equation $\\lambda\\phi(t)=\\tfrac{N_0}2\\phi(t)$ is solved by every function $\\phi$, so every complete orthonormal set consists of eigenfunctions, with equal eigenvalue $\\lambda=N_0/2$ (Barkat, section 8.4.4, pp. 493 to 495). So the coefficients in any basis are uncorrelated with variance $N_0/2$; this is why in detecting signals in white Gaussian noise we may choose a convenient basis (modules 21 and 25). Measured with $N_0/2=1$: the variances of the coefficients in a cosine basis and in a sine basis are {{wn_c}} and {{wn_s}}; the correlation between the first cosine coefficient and the first sine coefficient is {{wn_x}}.⟧</p>"),
                ("⟦Bức tranh chung||The common picture⟧",
                 TBL(["⟦Đối tượng||Object⟧", "⟦Cơ sở||Basis⟧", "⟦Hệ số||Coefficients⟧"],
                     [["⟦Hàm giới hạn băng||Band-limited function⟧", "$\\text{sinc}(x-n)$", "⟦mẫu $f(n)$||samples $f(n)$⟧"], ["⟦Hàm tuần hoàn||Periodic function⟧", "$e^{i2\\pi nx}$", "$F(n)$"], ["⟦Tín hiệu năng lượng hữu hạn||Finite-energy signal⟧", "⟦hệ trực chuẩn bất kỳ||any orthonormal set⟧", "$s_k=\\int s\\phi_k$"], ["⟦Quá trình ngẫu nhiên||Random process⟧", "⟦hàm riêng của $K_{xx}$||eigenfunctions of $K_{xx}$⟧", "⟦$X_k$ không tương quan, $\\lambda_k$||$X_k$ uncorrelated, $\\lambda_k$⟧"]])
                 + "<p>⟦Bốn khai triển này thực chất là một: mỗi tín hiệu là tổ hợp tuyến tính của các hàm cơ sở, với hệ số bằng tích trong. Lấy mẫu chọn cơ sở sinc; chuỗi Fourier chọn cơ sở lượng giác; Karhunen-Loève chọn cơ sở tối ưu cho quá trình. Đây là hạt nhân của module 21 và 25.||These four expansions are really one: every signal is a linear combination of basis functions with coefficients equal to inner products. Sampling chooses the sinc basis; the Fourier series the trigonometric basis; Karhunen-Loève the optimal basis for the process. This is the core of modules 21 and 25.⟧</p>"),
                ("⟦Tự kiểm tra phần 5||Self-check, part 5⟧",
                 UL(["⟦Vì sao khai triển Karhunen-Loève làm hệ số không tương quan?||Why does the Karhunen-Loève expansion make the coefficients uncorrelated?⟧",
                     "⟦Trị riêng của nhiễu trắng là gì?||What is the eigenvalue of white noise?⟧",
                     "⟦Trị riêng của Wiener trên $[0,T]$ là gì?||What are the eigenvalues of the Wiener process on $[0,T]$?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: vì các $\\phi_k$ là hàm riêng của nhân tự hiệp phương sai; $N_0/2$ với mọi cơ sở; $\\alpha T^2/[(n-\\tfrac12)^2\\pi^2]$.||Hints: because the $\\phi_k$ are eigenfunctions of the autocovariance kernel; $N_0/2$ for every basis; $\\alpha T^2/[(n-\\tfrac12)^2\\pi^2]$.⟧</p>"),
            ]),
    ],
    takeaways=[
        "⟦Hàm giới hạn băng ở $s_c$ được xác định bởi mẫu cách không quá $1/2s_c$: $f=\\sum f(n\\tau)\\text{sinc}((x-n\\tau)/\\tau)$; lấy mẫu sao chép phổ, dưới mức gây chồng phổ.||A function band-limited to $s_c$ is fixed by samples at most $1/2s_c$ apart: $f=\\sum f(n\\tau)\\text{sinc}((x-n\\tau)/\\tau)$; sampling replicates the spectrum, and undersampling causes aliasing.⟧",
        "⟦Nội suy sinc bảo toàn phương sai nhiễu; lấy mẫu có đạo hàm và xen kẽ khuếch đại nhiễu (hệ số $\\cot\\pi a$).||Sinc interpolation preserves noise variance; slope and interlaced sampling amplify noise (the $\\cot\\pi a$ factor).⟧",
        "⟦Chuỗi Fourier là $p=\\text{III}*f\\supset\\text{III}F$, $a_n-ib_n=2F(n)$; cắt chuỗi cho Gibbs 9 phần trăm.||The Fourier series is $p=\\text{III}*f\\supset\\text{III}F$, $a_n-ib_n=2F(n)$; truncation gives a 9 percent Gibbs overshoot.⟧",
        "⟦Khai triển trực chuẩn: $s_k=\\int s\\phi_k$, $E_\\varepsilon=E-\\sum s_k^2$; Gram-Schmidt dựng cơ sở, MGS ổn định; không gian tín hiệu cho khoảng cách và góc.||Orthonormal expansion: $s_k=\\int s\\phi_k$, $E_\\varepsilon=E-\\sum s_k^2$; Gram-Schmidt builds the basis, MGS is stable; signal space gives distances and angles.⟧",
        "⟦Karhunen-Loève: hàm riêng của $K_{xx}$ cho hệ số không tương quan; Wiener $\\lambda_n=\\alpha T^2/[(n-\\tfrac12)^2\\pi^2]$; nhiễu trắng: mọi cơ sở, $\\lambda=N_0/2$.||Karhunen-Loève: eigenfunctions of $K_{xx}$ give uncorrelated coefficients; Wiener $\\lambda_n=\\alpha T^2/[(n-\\tfrac12)^2\\pi^2]$; white noise: every basis, $\\lambda=N_0/2$.⟧",
    ],
    history="<p>⟦Shannon (1948, 1949) phát biểu định lý lấy mẫu trong lý thuyết thông tin; Linden (1959) thảo luận các định lý lấy mẫu bậc cao, Blackman và Tukey (1958), Jenkins và Watts (1969) về phân tích phổ (Bracewell, tr. 248). Về chuỗi Fourier: D. Bernoulli 1753, Fourier 1807, Dirichlet 1829 (tr. 236). Barkat lấy Van Trees (1968) và Dorny (1980) làm nguồn cho biểu diễn tín hiệu, Mercer cho định lý về nhân, Karhunen và Loève cho khai triển (chương 8, tr. 500).||"
            "Shannon (1948, 1949) stated the sampling theorem in information theory; Linden (1959) discussed higher-order sampling theorems, Blackman and Tukey (1958), Jenkins and Watts (1969) on spectral analysis (Bracewell, p. 248). On Fourier series: D. Bernoulli 1753, Fourier 1807, Dirichlet 1829 (p. 236). Barkat takes Van Trees (1968) and Dorny (1980) as sources for signal representation, Mercer for the kernel theorem, Karhunen and Loève for the expansion (chapter 8, p. 500).⟧</p>",
    case="<p>⟦<b>Từ tín hiệu liên tục tới vector.</b> Một tín hiệu giới hạn băng 5 Hz chỉ cần 10 mẫu mỗi giây; nội suy sinc từ các mẫu lấy ở 10 Hz tái tạo với sai số {{smp_err}} (ví dụ trong phần 1), và một tần số 0.8 lấy mẫu ở tốc độ tương ứng cắt 0.5 hiện thành {{al_f}}. Nếu còn nhiễu độc lập trên mẫu, nội suy giữ nguyên phương sai (tổng $\\text{sinc}^2$ = {{nz_var}}). Với khoảng $[0,1]$ và nhiễu Wiener, khai triển Karhunen-Loève cho các thành phần độc lập với phương sai {{kl_w1}}, {{kl_w2}}, {{kl_w3}}, {{kl_w4}}: bốn thành phần đầu chứa phần lớn năng lượng $\\alpha T^2/2$ = {{kl_sum}}. Đó là điều ta dùng ở module 21 và 25: biến bài toán phát hiện liên tục thành bài toán trên vector Gauss độc lập.||"
          "<b>From a continuous signal to a vector.</b> A signal band-limited to 5 Hz needs only 10 samples per second; sinc interpolation from samples at 10 Hz reconstructs it with an error {{smp_err}} (the example in part 1), and a frequency 0.8 sampled at a rate corresponding to a cutoff of 0.5 appears at {{al_f}}. If independent noise is on the samples, interpolation keeps the variance (the sum of $\\text{sinc}^2$ = {{nz_var}}). On the interval $[0,1]$ with Wiener noise, the Karhunen-Loève expansion gives independent components with variances {{kl_w1}}, {{kl_w2}}, {{kl_w3}}, {{kl_w4}}: the first four hold most of the energy $\\alpha T^2/2$ = {{kl_sum}}. This is what we use in modules 21 and 25: turn a continuous detection problem into a problem on independent Gaussian vectors.⟧</p>",
    practice=[
        "⟦Mở notebook và chạy cell cài đặt.||Open the notebook and run the setup cell.⟧",
        "⟦Bài 1: lấy mẫu tín hiệu $\\cos2\\pi(0.8x)$ với các khoảng khác nhau và tìm tần số hiện ra; vẽ phổ ba trường hợp.||Task 1: sample $\\cos2\\pi(0.8x)$ at different intervals and find the apparent frequency; plot the spectrum for three cases.⟧",
        "⟦Bài 2: cắt sóng vuông ở 10, 50, 200 số hạng và đo quá độ Gibbs; so sánh với $\\text{Si}(\\pi)$.||Task 2: truncate a square wave at 10, 50, 200 terms and measure the Gibbs overshoot; compare with $\\text{Si}(\\pi)$.⟧",
        "⟦Bài 3: dựng cơ sở từ bốn tín hiệu tự chọn bằng Gram-Schmidt cải tiến và vẽ vị trí trong không gian tín hiệu.||Task 3: build a basis from four signals of your choice with modified Gram-Schmidt and plot their positions in signal space.⟧",
        "⟦Bài 4: rời rạc hóa nhân $\\sigma^2e^{-\\alpha|t-u|}$ với các $\\alpha$ khác và quan sát trị riêng: $\\alpha$ lớn tiến về nhiễu trắng.||Task 4: discretise the kernel $\\sigma^2e^{-\\alpha|t-u|}$ with various $\\alpha$ and watch the eigenvalues: large $\\alpha$ tends to white noise.⟧",
    ],
    pitfalls=[
        "<b>⟦\"Lấy mẫu ở đúng gấp đôi tần số cao nhất luôn khôi phục được mọi thành phần.\"||\"Sampling at exactly twice the highest frequency always recovers every component.\"⟧</b><p>⟦Thành phần sin ở đúng tần số cắt bị mất vì các mẫu rơi vào không điểm của nó; chỉ phần cosin còn (độ lệch với phần chẵn {{crit_dev}}).||A sine component exactly at the cutoff is lost since the samples fall on its zeros; only the cosine part remains (deviation from the even part {{crit_dev}}).⟧</p>",
        "<b>⟦\"Thêm số hạng thì Gibbs biến mất.\"||\"Adding terms makes the Gibbs overshoot vanish.\"⟧</b><p>⟦Nó dồn gần bước nhảy nhưng giữ biên độ: cực đại {{gb_max}}, tức {{gb_pct}} phần trăm bước nhảy, dù 200 số hạng cho {{gb_sq}}.||It crowds toward the jump but keeps its amplitude: the maximum {{gb_max}}, i.e. {{gb_pct}} percent of the jump, though 200 terms give {{gb_sq}}.⟧</p>",
        "<b>⟦\"Lấy mẫu xen kẽ cũng chịu nhiễu như lấy mẫu đều.\"||\"Interlaced sampling is as noise-tolerant as uniform sampling.\"⟧</b><p>⟦Với $a=0.2$ tổng bình phương hệ số là {{il_amp}}, so với {{il_amp5}} khi đều (Bracewell, tr. 235).||With $a=0.2$ the sum of squared coefficients is {{il_amp}}, against {{il_amp5}} for uniform (Bracewell, p. 235).⟧</p>",
        "<b>⟦\"Gram-Schmidt cổ điển luôn cho cơ sở trực giao chính xác.\"||\"Classical Gram-Schmidt always gives an exactly orthogonal basis.\"⟧</b><p>⟦Với cột gần phụ thuộc, CGS mất trực giao ({{cgs_err}}), MGS giữ ({{mgs_err}}) (Barkat, tr. 457).||With nearly dependent columns CGS loses orthogonality ({{cgs_err}}), MGS keeps it ({{mgs_err}}) (Barkat, p. 457).⟧</p>",
    ],
    refs=[
        "⟦R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chương 10 (tr. 219 đến 258).||R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chapter 10 (pp. 219 to 258).⟧",
        "⟦M. Barkat, <i>Signal Detection and Estimation</i>, 2nd ed., Artech House, 2005, chương 8 (tr. 449 đến 500).||M. Barkat, <i>Signal Detection and Estimation</i>, 2nd ed., Artech House, 2005, chapter 8 (pp. 449 to 500).⟧",
        "⟦Tài liệu do các chương trích: Shannon (1948, 1949), Linden (1959), Blackman và Tukey (1958), Jenkins và Watts (1969), Dorny (1980), Van Trees (1968).||Works cited by the chapters: Shannon (1948, 1949), Linden (1959), Blackman and Tukey (1958), Jenkins and Watts (1969), Dorny (1980), Van Trees (1968).⟧",
    ],
    quiz=[
        dict(q="⟦Tái tạo $\\text{sinc}^2(x/2)$ từ mẫu nguyên tại $x=0.5$: độ lệch xấp xỉ bao nhiêu?||Reconstructing $\\text{sinc}^2(x/2)$ from integer samples at $x=0.5$: what is the approximate deviation?⟧",
             opts=["{{smp_err}}", "1.0e-01", "1.0e-03", "0.5000"], explain="⟦Chỉ do cắt tổng ở $|n|\\le2000$: {{smp_err}}.||Only from truncating the sum at $|n|\\le2000$: {{smp_err}}.⟧"),
        dict(q="⟦Độ lệch giữa mẫu tới hạn của $\\cos(\\omega t-\\phi)$ và mẫu của phần chẵn là bao nhiêu?||What is the deviation between the critical samples of $\\cos(\\omega t-\\phi)$ and those of its even part?⟧",
             opts=["{{crit_dev}}", "1.0e-01", "0.5000", "1.0e-03"], explain="⟦Phần lẻ được lấy mẫu tại các không điểm: {{crit_dev}}.||The odd part is sampled at its zeros: {{crit_dev}}.⟧"),
        dict(q="⟦$\\text{sinc}(1.5)$ (bảng 10.1) bằng bao nhiêu?||What is $\\text{sinc}(1.5)$ (Table 10.1)?⟧",
             opts=["{{mid_2}}", "-0.1273", "0.2122", "-0.0909"], explain="⟦$-2/3\\pi$ = {{mid_2}}; $\\text{sinc}(0.5)$ = {{mid_1}}; $\\text{sinc}(2.5)$ = {{mid_3}}.||$-2/3\\pi$ = {{mid_2}}; $\\text{sinc}(0.5)$ = {{mid_1}}; $\\text{sinc}(2.5)$ = {{mid_3}}.⟧"),
        dict(q="⟦Băng 3 dB (theo $1/W$) của trung bình trượt chữ nhật bằng bao nhiêu?||What is the 3 dB bandwidth (in units of $1/W$) of a rectangular running mean?⟧",
             opts=["{{rm_3db}}", "1.0000", "0.5000", "0.4429"], explain="⟦$2\\times0.4429$ = {{rm_3db}} (Bracewell, tr. 227).||$2\\times0.4429$ = {{rm_3db}} (Bracewell, p. 227).⟧"),
        dict(q="⟦Thùy bên đầu của bộ lọc 12 hệ số bằng bao nhiêu?||What is the first sidelobe of the 12-coefficient filter?⟧",
             opts=["{{rm12_side}}", "{{rm13_side}}", "0.5000", "0.0100"], explain="⟦12 hệ số: {{rm12_side}}; 13 hệ số nửa cường độ hai đầu: {{rm13_side}} (thấp hơn).||12 coefficients: {{rm12_side}}; 13 coefficients with half-strength ends: {{rm13_side}} (lower).⟧"),
        dict(q="⟦Sóng tần số 0.8 lấy mẫu ở khoảng 1 hiện thành tần số nào?||At which frequency does a wave of frequency 0.8 sampled at interval 1 appear?⟧",
             opts=["{{al_f}}", "0.8000", "0.5000", "0.4000"], explain="⟦Phản xạ: $1-0.8$ = {{al_f}}.||Reflection: $1-0.8$ = {{al_f}}.⟧"),
        dict(q="⟦Tái tạo $\\text{sinc}\\,2x$ tại $x=0.37$ bằng mẫu và độ dốc: giá trị là bao nhiêu?||Reconstructing $\\text{sinc}\\,2x$ at $x=0.37$ from samples and slopes: what is the value?⟧",
             opts=["{{os_val}}", "0.1259", "0.0000", "0.5000"], explain="⟦{{os_val}} so với đúng {{os_true}}; chỉ tung độ cho $\\text{sinc}^2x$ = {{os_only}}.||{{os_val}} against the exact {{os_true}}; ordinates alone give $\\text{sinc}^2x$ = {{os_only}}.⟧"),
        dict(q="⟦$a(0)$ của nghiệm lấy mẫu xen kẽ $a=0.2$ bằng bao nhiêu?||What is $a(0)$ of the interlaced sampling solution with $a=0.2$?⟧",
             opts=["{{il_a0}}", "0.2000", "0.0000", "2.0000"], explain="⟦Bằng 1, và bằng 0 tại các điểm mẫu khác (lệch {{il_zero}}); tái tạo lệch {{il_err}}.||Equal to 1 and 0 at the other sample points (deviation {{il_zero}}); reconstruction deviates {{il_err}}.⟧"),
        dict(q="⟦Tổng $\\sum\\text{sinc}^2(n+\\tfrac12)$ (phương sai lỗi nội suy chia phương sai dữ liệu) bằng bao nhiêu?||What is $\\sum\\text{sinc}^2(n+\\tfrac12)$ (interpolation error variance over data variance)?⟧",
             opts=["{{nz_var}}", "0.6366", "1.2732", "2.0000"], explain="⟦Tổng của $\\text{sinc}^2$ tại khoảng đơn vị bằng {{nz_var}}; sai số tối đa {{nz_max}} lần.||The sum of $\\text{sinc}^2$ at unit intervals is {{nz_var}}; the maximum error is {{nz_max}} times.⟧"),
        dict(q="⟦Khuếch đại phương sai tại giữa khoảng rộng của lấy mẫu xen kẽ $a=0.2$ bằng bao nhiêu?||What is the variance amplification at the middle of the wide interval for interlaced sampling with $a=0.2$?⟧",
             opts=["{{il_amp}}", "1.0000", "0.6000", "{{il_amp5}}"], explain="⟦Tổng bình phương hệ số {{il_amp}}, so với {{il_amp5}} khi lấy mẫu đều.||The sum of squared coefficients {{il_amp}}, against {{il_amp5}} for uniform sampling.⟧"),
        dict(q="⟦$\\sum F(n)$ của chuỗi tam giác $\\Lambda(10x)*\\text{III}$ (tại $x=0$) bằng bao nhiêu?||What is $\\sum F(n)$ of the triangle train $\\Lambda(10x)*\\text{III}$ (at $x=0$)?⟧",
             opts=["{{ft_sum}}", "0.1000", "0.5000", "10.000"], explain="⟦$p(0)=1$: tổng hệ số {{ft_sum}}.||$p(0)=1$: the sum of the coefficients {{ft_sum}}.⟧"),
        dict(q="⟦Cực đại của $\\tfrac2\\pi\\text{Si}(N\\pi x)$ (Gibbs) bằng bao nhiêu?||What is the maximum of $\\tfrac2\\pi\\text{Si}(N\\pi x)$ (Gibbs)?⟧",
             opts=["{{gb_max}}", "1.0900", "1.0000", "1.2000"], explain="⟦$\\tfrac2\\pi\\text{Si}(\\pi)$ = {{gb_max}}, tức {{gb_pct}} phần trăm của bước nhảy 2.||$\\tfrac2\\pi\\text{Si}(\\pi)$ = {{gb_max}}, i.e. {{gb_pct}} percent of the jump of 2.⟧"),
        dict(q="⟦Cực đại của tổng riêng sóng vuông 200 số hạng lẻ bằng bao nhiêu?||What is the maximum of the 200-odd-term partial sum of a square wave?⟧",
             opts=["{{gb_sq}}", "1.0900", "1.0000", "1.0500"], explain="⟦{{gb_sq}} gần {{gb_max}}, không tiến về 1.||{{gb_sq}} is near {{gb_max}}, not tending to 1.⟧"),
        dict(q="⟦Chuỗi sin của $f=x(\\tfrac12-x)$ tại $x=0.2$ bằng bao nhiêu?||What does the sine series of $f=x(\\tfrac12-x)$ give at $x=0.2$?⟧",
             opts=["{{fs_val}}", "0.1000", "0.0600", "0.0300"], explain="⟦{{fs_val}} bằng giá trị đúng {{fs_true}} (kết quả $0.06=0.2\\times0.3$).||{{fs_val}} equals the exact {{fs_true}} ($0.06=0.2\\times0.3$).⟧"),
        dict(q="⟦Độ lớn của biến đổi của $\\Pi'(x)$ tại $s=0.3$ là bao nhiêu?||What is the magnitude of the transform of $\\Pi'(x)$ at $s=0.3$?⟧",
             opts=["{{fin_pi}}", "0.8090", "0.5878", "1.6180"], explain="⟦$|2\\sin\\pi s|$ = {{fin_pi}}; số hạng phụ của biến đổi hữu hạn lệch {{fin_dev}}.||$|2\\sin\\pi s|$ = {{fin_pi}}; the extra terms of the finite transform deviate {{fin_dev}}.⟧"),
        dict(q="⟦Tổng Poisson $\\sum e^{-\\pi(n-0.1)^2/\\tau^2}$ và vế phổ khác nhau bao nhiêu ($\\tau=0.3$)?||How much do the Poisson sum $\\sum e^{-\\pi(n-0.1)^2/\\tau^2}$ and its spectral side differ ($\\tau=0.3$)?⟧",
             opts=["{{sh_dev}}", "1.0e-03", "1.0e-01", "0.5000"], explain="⟦Shah tự biến đổi: lệch chỉ {{sh_dev}}.||The shah is self-transforming: the difference is only {{sh_dev}}.⟧"),
        dict(q="⟦Năng lượng sai số của $s(t)=t$ với 5 số hạng cosin bằng bao nhiêu?||What is the error energy of $s(t)=t$ with 5 cosine terms?⟧",
             opts=["{{gf_err5}}", "0.3333", "0.0100", "0.0500"], explain="⟦$E-\\sum s_k^2$ = {{gf_err5}}; với 50 số hạng {{gf_err50}}.||$E-\\sum s_k^2$ = {{gf_err5}}; with 50 terms {{gf_err50}}.⟧"),
        dict(q="⟦Hệ số $s_1$ của $s(t)=t$ theo $\\phi_1=\\sqrt2\\cos\\pi t$ bằng bao nhiêu?||What is the coefficient $s_1$ of $s(t)=t$ on $\\phi_1=\\sqrt2\\cos\\pi t$?⟧",
             opts=["{{mf_s1}}", "0.4501", "0.9003", "-0.2251"], explain="⟦$-2\\sqrt2/\\pi^2$ = {{mf_s1}} bằng tương quan và bộ lọc phối hợp.||$-2\\sqrt2/\\pi^2$ = {{mf_s1}} by correlation and matched filter.⟧"),
        dict(q="⟦Số chiều $K$ của không gian tín hiệu của bốn tín hiệu ở ví dụ 8.1 là bao nhiêu?||What is the dimension $K$ of the signal space of the four signals in example 8.1?⟧",
             opts=["{{gs_K}}", "4", "2", "1"], explain="⟦$s_4=s_2-s_3$ phụ thuộc: hạng {{gs_K}}.||$s_4=s_2-s_3$ is dependent: rank {{gs_K}}.⟧"),
        dict(q="⟦Độ lệch trực giao $\\|Q^TQ-I\\|$ của Gram-Schmidt cải tiến trên ma trận Hilbert 12 cột là bao nhiêu?||What is the orthogonality deviation $\\|Q^TQ-I\\|$ of the modified Gram-Schmidt on the 12-column Hilbert matrix?||⟧".replace("||⟧","⟧"),
             opts=["{{mgs_err}}", "1.0e-16", "1.0000", "{{cgs_err}}"], explain="⟦CGS {{cgs_err}} lớn hơn nhiều so với MGS {{mgs_err}}.||CGS {{cgs_err}} is far larger than MGS {{mgs_err}}.⟧"),
        dict(q="⟦Hệ số tương quan $\\rho_{23}$ giữa $s_2$ và $s_3$ ở ví dụ 8.1 bằng bao nhiêu?||What is the correlation coefficient $\\rho_{23}$ between $s_2$ and $s_3$ in example 8.1?⟧",
             opts=["{{gr_rho}}", "1.0000", "-1.0000", "0.5000"], explain="⟦Hai chữ nhật rời nhau: {{gr_rho}}; khoảng cách {{gr_d}}.||Two disjoint rectangles: {{gr_rho}}; distance {{gr_d}}.⟧"),
        dict(q="⟦Trị riêng lớn nhất của toán tử với nhân $\\min(u,t)[1-\\max(u,t)]$ bằng bao nhiêu?||What is the largest eigenvalue of the operator with kernel $\\min(u,t)[1-\\max(u,t)]$?⟧",
             opts=["{{gr_e1}}", "1.0000", "0.2500", "0.4053"], explain="⟦$1/\\pi^2$ = {{gr_e1}}; trị riêng thứ hai $1/4\\pi^2$ = {{gr_e2}}.||$1/\\pi^2$ = {{gr_e1}}; the second $1/4\\pi^2$ = {{gr_e2}}.⟧"),
        dict(q="⟦Nhân $k(0.3,0.6)$ theo Mercer bằng bao nhiêu?||What is the kernel $k(0.3,0.6)$ by Mercer's formula?⟧",
             opts=["{{gr_k}}", "0.2400", "0.1800", "0.3000"], explain="⟦$0.3\\times0.4$ = {{gr_k}} = tổng chuỗi {{gr_mer}}.||$0.3\\times0.4$ = {{gr_k}} = the series sum {{gr_mer}}.⟧"),
        dict(q="⟦Trị riêng đầu của toán tử có nhân $1-\\max(u,t)$ bằng bao nhiêu?||What is the first eigenvalue of the operator with kernel $1-\\max(u,t)$?⟧",
             opts=["{{gr_f1}}", "0.2500", "1.0000", "2.4674"], explain="⟦$4/\\pi^2$ = {{gr_f1}} (nghịch đảo của $\\pi^2/4$).||$4/\\pi^2$ = {{gr_f1}} (the reciprocal of $\\pi^2/4$).⟧"),
        dict(q="⟦Tương quan giữa $X_1$ và $X_2$ của khai triển K-L Wiener bằng bao nhiêu?||What is the correlation between $X_1$ and $X_2$ of the Wiener K-L expansion?⟧",
             opts=["{{kl_corr}}", "0.5000", "1.0000", "-0.5000"], explain="⟦Không tương quan: {{kl_corr}}; độ nhọn dư {{kl_kurt}}.||Uncorrelated: {{kl_corr}}; excess kurtosis {{kl_kurt}}.⟧"),
        dict(q="⟦Trị riêng thứ nhất của quá trình Wiener ($\\alpha=T=1$) bằng bao nhiêu?||What is the first eigenvalue of the Wiener process ($\\alpha=T=1$)?⟧",
             opts=["{{kl_w1}}", "0.4503", "1.0000", "0.1013"], explain="⟦$1/(0.5\\pi)^2$ = {{kl_w1}}, khớp ma trận số.||$1/(0.5\\pi)^2$ = {{kl_w1}}, matching the numerical matrix.⟧"),
        dict(q="⟦Tổng các trị riêng của Wiener ($\\alpha=T=1$) bằng bao nhiêu?||What is the sum of the Wiener eigenvalues ($\\alpha=T=1$)?⟧",
             opts=["{{kl_sum}}", "1.0000", "0.2500", "0.8225"], explain="⟦$\\int K(t,t)dt=\\alpha T^2/2$ = {{kl_sum}}.||$\\int K(t,t)dt=\\alpha T^2/2$ = {{kl_sum}}.⟧"),
        dict(q="⟦Trị riêng đầu của nhân $e^{-|t-u|}$ trên $[-1,1]$ ($\\alpha=\\sigma=1$) bằng bao nhiêu?||What is the first eigenvalue of the kernel $e^{-|t-u|}$ on $[-1,1]$ ($\\alpha=\\sigma=1$)?⟧",
             opts=["{{ou_l1}}", "2.0000", "1.0000", "0.3909"], explain="⟦$2/(1+\\beta_1^2)$ với $\\beta\\tan\\beta=1$: {{ou_l1}}; thứ hai {{ou_l2}}.||$2/(1+\\beta_1^2)$ with $\\beta\\tan\\beta=1$: {{ou_l1}}; the second {{ou_l2}}.⟧"),
        dict(q="⟦Phần năng lượng bốn trị riêng đầu của nhân mũ chiếm là bao nhiêu?||What fraction of the energy do the first four eigenvalues of the exponential kernel hold?⟧",
             opts=["{{ou_frac}}", "0.5000", "0.9900", "0.7000"], explain="⟦Tổng bốn trị riêng chia $\\int K(t,t)dt=2$ = {{ou_frac}}.||The sum of four eigenvalues over $\\int K(t,t)dt=2$ = {{ou_frac}}.⟧"),
        dict(q="⟦Phương sai hệ số theo cơ sở cosin của nhiễu trắng $N_0/2=1$ bằng bao nhiêu?||What is the variance of the coefficient on a cosine basis for white noise with $N_0/2=1$?⟧",
             opts=["{{wn_c}}", "0.5000", "2.0000", "3.1416"], explain="⟦Mọi cơ sở cho trị riêng $N_0/2$: {{wn_c}} và {{wn_s}}; tương quan chéo {{wn_x}}.||Every basis gives eigenvalue $N_0/2$: {{wn_c}} and {{wn_s}}; cross-correlation {{wn_x}}.⟧"),
        dict(q="⟦Lấy mẫu ở khoảng nào là tới hạn cho hàm có phổ cắt tại $s_c$?||At which interval is sampling critical for a function with spectrum cut off at $s_c$?⟧",
             opts=["⟦$\\tau=\\tfrac1{2s_c}$||$\\tau=\\tfrac1{2s_c}$⟧",
                   "⟦$\\tau=\\tfrac1{s_c}$, vì các đảo phổ rộng $2s_c$ nên cần sao chép ở $s_c$||$\\tau=\\tfrac1{s_c}$, since the islands are $2s_c$ wide so replication at $s_c$ is needed⟧",
                   "⟦$\\tau=2s_c$, vì khoảng lấy mẫu phải bằng bề rộng băng của hàm||$\\tau=2s_c$, since the sampling interval must equal the bandwidth of the function⟧",
                   "⟦$\\tau=\\tfrac{1}{4s_c}$, vì cần bốn mẫu mỗi chu kỳ để tránh chồng phổ||$\\tau=\\tfrac1{4s_c}$, since four samples per cycle are needed to avoid aliasing⟧"],
             explain="⟦Bracewell, tr. 223: các đảo cách nhau $\\tau^{-1}$ phải không nhỏ hơn bề rộng $2s_c$.||Bracewell, p. 223: the islands spaced $\\tau^{-1}$ must not be closer than their width $2s_c$.⟧"),
        dict(q="⟦Lấy mẫu làm gì với phổ của hàm?||What does sampling do to the spectrum of a function?⟧",
             opts=["⟦Sao chép phổ với chu kỳ $\\tau^{-1}$||It replicates the spectrum with period $\\tau^{-1}$⟧",
                   "⟦Cắt phổ tại tần số $\\tfrac1{2\\tau}$ và bỏ phần bên ngoài, giống bộ lọc chữ nhật||It cuts the spectrum at $\\tfrac1{2\\tau}$ and discards the outside, like a rectangular filter⟧",
                   "⟦Nhân phổ với $\\text{sinc}\\,\\tau s$ vì mỗi mẫu là một trung bình trượt||It multiplies the spectrum by $\\text{sinc}\\,\\tau s$ since each sample is a running mean⟧",
                   "⟦Dịch phổ đi $\\tau^{-1}$ mà không đổi hình dạng, như định lý dịch||It shifts the spectrum by $\\tau^{-1}$ without changing its shape, like the shift theorem⟧"],
             explain="⟦Bracewell, tr. 223: $f\\,\\text{III}(x/\\tau)\\supset\\tau\\text{III}(\\tau s)*F$.||Bracewell, p. 223: $f\\,\\text{III}(x/\\tau)\\supset\\tau\\text{III}(\\tau s)*F$.⟧"),
        dict(q="⟦Vì sao nội suy sinc từ mẫu đều bảo toàn phương sai nhiễu độc lập?||Why does sinc interpolation from uniform samples preserve independent noise variance?⟧",
             opts=["⟦Vì các giá trị $\\text{sinc}^2$ tại khoảng đơn vị cộng lại bằng 1||Because the values of $\\text{sinc}^2$ at unit intervals add up to 1⟧",
                   "⟦Vì sinc là hàm chẵn nên các sai số ở hai phía luôn triệt nhau hoàn toàn||Because sinc is even so the errors on the two sides always cancel exactly⟧",
                   "⟦Vì nội suy là phép lọc thông thấp nên làm giảm phương sai xuống còn một nửa||Because interpolation is a low-pass filter so it halves the variance⟧",
                   "⟦Vì nhiễu độc lập luôn có phổ nằm ngoài băng nên bị bộ lọc sinc loại bỏ||Because independent noise always has its spectrum outside the band so the sinc filter removes it⟧"],
             explain="⟦Bracewell, tr. 234 đến 235: tổng bình phương hệ số là {{nz_var}}.||Bracewell, pp. 234 to 235: the sum of squared coefficients is {{nz_var}}.⟧"),
        dict(q="⟦Vì sao hiện tượng Gibbs vẫn còn khi thêm số hạng?||Why does the Gibbs phenomenon remain when terms are added?⟧",
             opts=["⟦Cắt là chập với sinc hẹp hơn nhưng cùng biên độ, quá độ vẫn 9 phần trăm||Truncation is convolution with a narrower sinc of the same amplitude, the overshoot stays at 9 percent⟧",
                   "⟦Vì chuỗi Fourier không hội tụ tại các điểm gián đoạn dù thêm bao nhiêu số hạng||Because the Fourier series does not converge at discontinuities however many terms are added⟧",
                   "⟦Vì sai số làm tròn số học tích lũy khi cộng nhiều số hạng lượng giác||Because arithmetic rounding errors accumulate when adding many trigonometric terms⟧",
                   "⟦Vì hệ số Fourier của hàm gián đoạn giảm quá chậm nên tổng luôn dao động||Because the Fourier coefficients of a discontinuous function fall too slowly so the sum always oscillates⟧"],
             explain="⟦Bracewell, tr. 241 đến 242: $N\\text{sinc}\\,Nx*\\text{sgn}\\,x=\\tfrac2\\pi\\text{Si}(N\\pi x)$, cực đại {{gb_max}}.||Bracewell, pp. 241 to 242: $N\\text{sinc}\\,Nx*\\text{sgn}\\,x=\\tfrac2\\pi\\text{Si}(N\\pi x)$, maximum {{gb_max}}.⟧"),
        dict(q="⟦Hệ số Fourier $a_n-ib_n$ của hàm tuần hoàn $\\text{III}*f$ liên hệ thế nào với $F$?||How is the Fourier coefficient $a_n-ib_n$ of the periodic function $\\text{III}*f$ related to $F$?⟧",
             opts=["⟦Bằng $2F(n)$||It equals $2F(n)$⟧",
                   "⟦Bằng $F(n)/2$, vì mỗi họa âm chia đều giữa tần số dương và âm||It equals $F(n)/2$, since each harmonic is split between positive and negative frequency⟧",
                   "⟦Bằng $F(n)$, vì hệ số của chuỗi phức và chuỗi thực trùng nhau||It equals $F(n)$, since the complex and real series coefficients coincide⟧",
                   "⟦Bằng $F(n/2\\pi)$, vì tần số góc khác tần số theo chu kỳ||It equals $F(n/2\\pi)$, since angular frequency differs from cyclic frequency⟧"],
             explain="⟦Bracewell, tr. 237 đến 239: $a_n-ib_n=2F(n)$.||Bracewell, pp. 237 to 239: $a_n-ib_n=2F(n)$.⟧"),
        dict(q="⟦Năng lượng sai số của khai triển trực chuẩn $K$ số hạng bằng gì?||What is the error energy of a $K$-term orthonormal expansion?⟧",
             opts=["⟦$E-\\sum_{k\\le K}s_k^2$||$E-\\sum_{k\\le K}s_k^2$⟧",
                   "⟦$\\sum_{k>K}s_k$, tổng các hệ số còn lại, không bình phương||$\\sum_{k>K}s_k$, the sum of the remaining coefficients, not squared⟧",
                   "⟦$E/K$, vì năng lượng chia đều cho các thành phần||$E/K$, since the energy is shared equally among components⟧",
                   "⟦$E\\cdot\\sum_{k\\le K}s_k^2$, tích năng lượng với tổng bình phương hệ số||$E\\cdot\\sum_{k\\le K}s_k^2$, the product of the energy and the sum of squared coefficients⟧"],
             explain="⟦Barkat, phương trình 8.23, tr. 453.||Barkat, equation 8.23, p. 453.⟧"),
        dict(q="⟦Gram-Schmidt cải tiến khác cổ điển ở điểm nào?||How does the modified Gram-Schmidt differ from the classical one?⟧",
             opts=["⟦Trừ ngay từng hình chiếu rồi chiếu phần dư tiếp theo||It subtracts each projection immediately and projects the running remainder next⟧",
                   "⟦Chuẩn hóa các hàm trước khi trừ nên mọi hình chiếu đều bằng đơn vị||It normalises the functions before subtracting so every projection is of unit size⟧",
                   "⟦Dùng tích trong có trọng số thay cho tích trong thường để giảm sai số||It uses a weighted inner product instead of the ordinary one to reduce the error⟧",
                   "⟦Chỉ áp dụng được cho tín hiệu có năng lượng bằng nhau||It applies only to signals of equal energy⟧"],
             explain="⟦Barkat, tr. 457: MGS ổn định số hơn; CGS {{cgs_err}} so với MGS {{mgs_err}}.||Barkat, p. 457: MGS is more stable; CGS {{cgs_err}} against MGS {{mgs_err}}.⟧"),
        dict(q="⟦Khai triển Karhunen-Loève dùng hàm cơ sở nào để hệ số không tương quan?||Which basis functions does the Karhunen-Loève expansion use so that the coefficients are uncorrelated?⟧",
             opts=["⟦Hàm riêng của nhân tự hiệp phương sai||The eigenfunctions of the autocovariance kernel⟧",
                   "⟦Các hàm sin và cosin của chuỗi Fourier, vì chúng trực giao||The sines and cosines of the Fourier series, since they are orthogonal⟧",
                   "⟦Các hàm sinc dịch, vì chúng là hệ trực chuẩn của hàm giới hạn băng||Shifted sinc functions, since they are the orthonormal set of band-limited functions⟧",
                   "⟦Các đa thức Hermite, vì quá trình Gauss có mật độ liên quan Hermite||Hermite polynomials, since a Gaussian process has a density related to Hermite⟧"],
             explain="⟦Barkat, mục 8.4, tr. 481: $\\int K_{xx}\\phi_j=\\lambda_j\\phi_j$.||Barkat, section 8.4, p. 481: $\\int K_{xx}\\phi_j=\\lambda_j\\phi_j$.⟧"),
        dict(q="⟦Vì sao cơ sở nào cũng là hàm riêng của nhiễu trắng?||Why is any basis a set of eigenfunctions of white noise?⟧",
             opts=["⟦Nhân là xung nên $\\lambda\\phi=\\tfrac{N_0}2\\phi$ đúng với mọi $\\phi$||The kernel is an impulse so $\\lambda\\phi=\\tfrac{N_0}2\\phi$ holds for every $\\phi$⟧",
                   "⟦Vì nhiễu trắng có công suất vô hạn nên mọi hàm đều có năng lượng như nhau||Because white noise has infinite power so every function carries the same energy⟧",
                   "⟦Vì nhiễu trắng luôn Gauss nên mọi phép biến đổi trực giao giữ nguyên nó||Because white noise is always Gaussian so every orthogonal transformation preserves it⟧",
                   "⟦Vì phổ phẳng làm hệ số tương quan bằng 1 giữa mọi cặp hàm cơ sở||Because the flat spectrum makes the correlation equal to 1 between any pair of basis functions⟧"],
             explain="⟦Barkat, mục 8.4.4, tr. 493: mọi hệ trực chuẩn đầy đủ, $\\lambda=N_0/2$.||Barkat, section 8.4.4, p. 493: every complete orthonormal set, $\\lambda=N_0/2$.⟧"),
    ],
    nb=[
        ("md", """## 1. ⟦Định lý lấy mẫu, nội suy, trung bình trượt, chồng phổ||Sampling theorem, interpolation, running means, aliasing⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Tái tạo sinc từ mẫu nguyên có chính xác, trường hợp biên đúng ra sao, hàm truyền của trung bình trượt và chồng phổ có đúng công thức?||Is sinc reconstruction from integer samples exact, how does the boundary case behave, and do the running-mean transfer function and aliasing match the formulas?⟧"""),
        ("code", r'''from scipy import integrate, special, optimize
trap = getattr(np, "trapezoid", None) or np.trapz
rg = np.random.default_rng(13)
# ⟦tái tạo sinc²(x/2) từ mẫu nguyên||reconstruct sinc²(x/2) from integer samples⟧
f = lambda x: np.sinc(x/2)**2
n = np.arange(-2000, 2001)
rec = np.sum(f(n)*np.sinc(0.5 - n)); err = abs(rec - f(0.5))
assert err < 1e-5
report("smp_err", max(err, 1e-16), ".0e")
# ⟦điều hòa tại tần số cắt: cos(ωt − φ) tại khoảng nửa chu kỳ||harmonic at the cutoff: cos(ωt − φ) sampled every half period⟧
phi, w = 0.7, 2*np.pi*0.5                     # ⟦tần số 0.5, khoảng 1||frequency 0.5, interval 1⟧
smp = np.cos(w*n - phi); even = np.cos(phi)*np.cos(w*n)
crit = np.max(np.abs(smp - even)[:200])
assert crit < 1e-12
report("crit_dev", max(crit, 1e-16), ".0e")
# ⟦bảng 10.1||Table 10.1⟧
for k, key in zip((0.5, 1.5, 2.5, 3.5), ("mid_1", "mid_2", "mid_3", "mid_4")):
    assert abs(np.sinc(k) - np.sin(np.pi*k)/(np.pi*k)) < 1e-15
    report(key, np.sinc(k), ".4f")
# ⟦trung bình trượt: hàm truyền 12 hệ số||running mean: transfer function of 12 coefficients⟧
N12 = 12
sg = np.linspace(1e-4, 0.5, 5000)
T12 = np.abs(np.sin(N12*np.pi*sg)/(N12*np.sin(np.pi*sg)))
T12_dft = np.abs(np.array([np.mean(np.exp(-2j*np.pi*s_*(np.arange(N12) - (N12 - 1)/2))) for s_ in sg[::250]]))
assert np.max(np.abs(T12_dft - T12[::250])) < 1e-12
coef13 = np.ones(13)/12; coef13[[0, -1]] = 0.5/12
T13 = np.abs(np.sin(N12*np.pi*sg)/(N12*np.tan(np.pi*sg)))
T13_dft = np.abs(np.array([np.sum(coef13*np.exp(-2j*np.pi*s_*(np.arange(13) - 6))) for s_ in sg[::250]]))
assert np.max(np.abs(T13_dft - T13[::250])) < 1e-12
side12 = np.max(T12[(sg > 1/12) & (sg < 2/12)]); side13 = np.max(T13[(sg > 1/12) & (sg < 2/12)])
assert side13 < side12
report("rm12_side", side12, ".4f"); report("rm13_side", side13, ".4f")
w3 = 2*optimize.brentq(lambda x: np.sinc(x) - 1/np.sqrt(2), 0.1, 0.9)
assert abs(w3 - 0.8859) < 1e-3
report("rm_3db", w3, ".4f")
# ⟦chồng phổ: tần số 0.8 lấy mẫu khoảng 1||aliasing: frequency 0.8 sampled at interval 1⟧
Ns = 4096; ta = np.arange(Ns)
xa = np.cos(2*np.pi*0.8*ta)
fr = np.fft.rfftfreq(Ns, 1.0); al = fr[np.argmax(np.abs(np.fft.rfft(xa)))]
assert abs(al - 0.2) < 1e-3
report("al_f", 0.2, ".1f")'''),
        ("code", r'''fig, ax = plt.subplots(figsize=(8, 3.3))
ax.plot(sg, T12, label=("⟦12 hệ số bằng nhau||12 equal coefficients⟧")); ax.plot(sg, T13, label=("⟦13 hệ số, hai đầu nửa||13 coefficients, half-strength ends⟧"))
ax.set_xlabel("s"); ax.legend(fontsize=8); plt.tight_layout(); plt.show()''', dict(fig="runmean", cap="⟦Hình 1. Hàm truyền của trung bình trượt 12 tháng (xanh) và của 13 hệ số có hai đầu nửa cường độ (cam): thùy bên thấp hơn ở cam.||Figure 1. The transfer function of the 12-month running mean (blue) and of 13 coefficients with half-strength ends (orange): the sidelobes are lower for the orange one.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Tái tạo lệch {{smp_err}}; điều hòa tới hạn lệch {{crit_dev}}; sinc tại nửa nguyên: {{mid_1}}, {{mid_2}}, {{mid_3}}, {{mid_4}}. Trung bình trượt: thùy bên {{rm12_side}} và {{rm13_side}}, băng 3 dB {{rm_3db}}. Chồng phổ: {{al_f}}.||Reconstruction deviates {{smp_err}}; the critical harmonic deviates {{crit_dev}}; sinc at half-integers: {{mid_1}}, {{mid_2}}, {{mid_3}}, {{mid_4}}. Running means: sidelobes {{rm12_side}} and {{rm13_side}}, 3 dB bandwidth {{rm_3db}}. Aliasing: {{al_f}}.⟧"""),
        ("md", """## 2. ⟦Lấy mẫu cải biên và nhiễu||Modified sampling and noise⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Lấy mẫu tung độ và độ dốc, xen kẽ có khôi phục chính xác, và khuếch đại nhiễu ra sao so với nội suy sinc đều?||Do ordinate-and-slope and interlaced sampling recover exactly, and how much do they amplify noise compared with uniform sinc interpolation?⟧"""),
        ("code", r'''# ⟦tung độ và độ dốc: f = sinc 2x||ordinate and slope: f = sinc 2x⟧
fo = lambda x: np.sinc(2*x)
def dfo(x):
    x = np.asarray(x, float); u_ = 2*np.pi*np.where(np.abs(x) < 1e-12, 1.0, x)
    return np.where(np.abs(x) < 1e-12, 0.0, 2*np.pi*(u_*np.cos(u_) - np.sin(u_))/u_**2)
nn = np.arange(-3000, 3001)
x0 = 0.37
val = np.sum(fo(nn)*np.sinc(x0 - nn)**2) + np.sum(dfo(nn)*(x0 - nn)*np.sinc(x0 - nn)**2)
assert abs(val - fo(x0)) < 5e-4 and abs(dfo(3.0) - 1/3) < 1e-12
only = np.sum(fo(nn)*np.sinc(x0 - nn)**2)
assert abs(only - np.sinc(x0)**2) < 1e-12 and abs(only - fo(x0)) > 0.01
report("os_val", val, ".4f"); report("os_true", fo(x0), ".4f"); report("os_err", abs(val - fo(x0)), ".1e"); report("os_only", only, ".4f")
# ⟦xen kẽ a = 0.2||interlaced a = 0.2⟧
def aint(x, al):
    x = np.asarray(x, float)
    den = 2*np.pi*x*np.sin(np.pi*al)
    return np.where(np.abs(x) < 1e-12, 1.0, (np.cos(2*np.pi*x - np.pi*al) - np.cos(np.pi*al))/np.where(np.abs(x) < 1e-12, 1.0, den))
al = 0.2
zs = np.array([1, 2, -1, -2, 0.2, 1.2, 2.2, -0.8, -1.8])
assert abs(aint(0.0, al) - 1) < 1e-14 and np.max(np.abs(aint(zs, al))) < 1e-12
report("il_a0", aint(0.0, al), ".0f"); report("il_zero", max(np.max(np.abs(aint(zs, al))), 1e-16), ".0e")
fs2 = lambda x: np.sinc(x)**2
nI = np.arange(-600, 601)
recI = np.sum(fs2(nI)*aint(0.3 - nI, al)) + np.sum(fs2(nI + al)*aint(-(0.3 - nI - al), al))
assert abs(recI - fs2(0.3)) < 1e-3
report("il_err", abs(recI - fs2(0.3)), ".0e")
# ⟦nhiễu: sinc đều và xen kẽ||noise: uniform sinc and interlaced⟧
xm = 0.5
uni = np.sum(np.sinc(xm - np.arange(-100000, 100001))**2)
assert abs(uni - 1) < 1e-4
mid = np.sum(np.sinc(0.5 - np.arange(-10**6, 10**6 + 1))**2)
report("nz_var", mid, ".4f")
report("nz_max", 2*abs(np.sinc(0.5)), ".4f")
def amp(alv):
    xw = alv/2 + 0.5          # ⟦giữa khoảng rộng||the middle of the wide interval⟧
    c1 = aint(xw - nI, alv); c2 = aint(-(xw - nI - alv), alv)
    return np.sum(c1**2) + np.sum(c2**2)
il_a = amp(0.2); il_u = amp(0.5)
assert il_a > il_u > 0.9
report("il_amp", il_a, ".2f"); report("il_amp5", il_u, ".2f")
# ⟦mô phỏng nhiễu: sai số nội suy có phương sai bằng dữ liệu||noise simulation: interpolation error has the data variance⟧
noise = rg.standard_normal((4000, 401))
errs = noise @ np.sinc(0.5 - np.arange(-200, 201))
assert abs(np.var(errs) - 1) < 0.06'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Tung độ và độ dốc: {{os_val}} so với {{os_true}} (lệch {{os_err}}), chỉ tung độ {{os_only}}. Xen kẽ: $a(0)$ = {{il_a0}}, zero {{il_zero}}, tái tạo lệch {{il_err}}. Nhiễu: tổng $\\text{sinc}^2$ {{nz_var}}, tối đa {{nz_max}} lần; xen kẽ khuếch đại {{il_amp}} so với {{il_amp5}}.||Ordinate and slope: {{os_val}} against {{os_true}} (deviation {{os_err}}), ordinates alone {{os_only}}. Interlaced: $a(0)$ = {{il_a0}}, zeros {{il_zero}}, reconstruction deviates {{il_err}}. Noise: sum of $\\text{sinc}^2$ {{nz_var}}, maximum {{nz_max}} times; interlaced amplification {{il_amp}} against {{il_amp5}}.⟧"""),
        ("md", """## 3. ⟦Chuỗi Fourier, Gibbs, biến đổi hữu hạn, shah||Fourier series, Gibbs, finite transforms, shah⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Hệ số chuỗi có bằng mẫu của biến đổi một chu kỳ, Gibbs có tiệm cận 9 phần trăm, biến đổi hữu hạn có đúng, và tổng Poisson (shah tự biến đổi) có đúng?||Do the series coefficients equal samples of the one-period transform, does Gibbs approach 9 percent, do finite transforms hold, and does the Poisson sum (the self-transforming shah) hold?⟧"""),
        ("code", r'''# ⟦chuỗi tam giác||triangle train⟧
nk = np.arange(-20000, 20001)
Fn = 0.1*np.sinc(nk/10)**2
tsum = np.sum(Fn)
assert abs(tsum - 1) < 5e-4
# ⟦hệ số bằng tích phân trực tiếp: a_n − i b_n = 2F(n) trên một chu kỳ||coefficients by direct integration: a_n − i b_n = 2F(n) over one period⟧
xg = np.linspace(-0.5, 0.5, 200001)
tri = np.maximum(1 - np.abs(10*xg), 0)
for k in (1, 2, 5):
    ak = 2*trap(tri*np.cos(2*np.pi*k*xg), xg)
    assert abs(ak - 2*0.1*np.sinc(k/10)**2) < 1e-6
report("ft_sum", tsum, ".4f")
Fn2 = 0.1*np.sinc(nk/10)
report("ft_sum2", np.sum(Fn2), ".3f")
assert abs(np.sum(Fn2) - 1) < 5e-3
# ⟦Gibbs||Gibbs⟧
gmax = 2/np.pi*special.sici(np.pi)[0]
xs = np.linspace(0, 2, 400001)
sat = 2/np.pi*special.sici(np.pi*xs*5)[0]
assert abs(np.max(sat) - gmax) < 1e-8
report("gb_max", gmax, ".4f"); report("gb_pct", (gmax - 1)/2*100, ".1f")
x_ = np.linspace(0.0005, 0.02, 40000)
Nt = 200
ssq = sum(4/(np.pi*k)*np.sin(2*np.pi*k*x_) for k in range(1, 2*Nt, 2))
assert abs(np.max(ssq) - gmax) < 0.01
report("gb_sq", np.max(ssq), ".4f")
# ⟦chuỗi sin của f = x(½ − x)||sine series of f = x(½ − x)⟧
fx = lambda x: x*(0.5 - x)
Fs_ = lambda s_: integrate.quad(lambda x: fx(x)*np.sin(2*np.pi*x*s_), 0, 0.5)[0]
ser = 4*sum(Fs_(s_)*np.sin(2*np.pi*0.2*s_) for s_ in range(1, 200))
assert abs(ser - fx(0.2)) < 1e-6
report("fs_val", ser, ".4f"); report("fs_true", fx(0.2), ".4f")
# ⟦đạo hàm của hàm cắt: f = x² trên (0, 1), s = 0.3||derivative of a truncated function: f = x² on (0, 1), s = 0.3⟧
s3 = 0.3
lhs = integrate.quad(lambda x: 2*x*np.cos(2*np.pi*x*s3), 0, 1)[0] - 1j*integrate.quad(lambda x: 2*x*np.sin(2*np.pi*x*s3), 0, 1)[0]
Fx = integrate.quad(lambda x: x*x*np.cos(2*np.pi*x*s3), 0, 1)[0] - 1j*integrate.quad(lambda x: x*x*np.sin(2*np.pi*x*s3), 0, 1)[0]
rhs = 2j*np.pi*s3*Fx + 1*np.exp(-2j*np.pi*s3) - 0
assert abs(lhs - rhs) < 1e-9
report("fin_dev", max(abs(lhs - rhs), 1e-16), ".0e")
Pp = integrate.quad(lambda x: 0, 0, 1)[0]
report("fin_pi", abs(2*np.sin(np.pi*s3)), ".4f")
# ⟦tổng Poisson||Poisson summation⟧
tau, sh = 0.3, 0.1
lhsP = np.sum(np.exp(-np.pi*(np.arange(-50, 51) - sh)**2/tau**2))
rhsP = tau*np.sum(np.exp(-np.pi*tau**2*np.arange(-200, 201)**2)*np.exp(-2j*np.pi*np.arange(-200, 201)*sh))
assert abs(lhsP - rhsP.real) < 1e-12 and abs(rhsP.imag) < 1e-12
report("sh_dev", max(abs(lhsP - rhsP.real), 1e-16), ".0e")'''),
        ("code", r'''fig, ax = plt.subplots(figsize=(8, 3.3))
xx = np.linspace(-0.25, 0.25, 4000)
sq_ = lambda Nt_: sum(4/(np.pi*k)*np.sin(2*np.pi*k*xx) for k in range(1, 2*Nt_, 2))
for Nt_, c in ((5, "tab:blue"), (25, "tab:orange"), (200, "tab:green")):
    ax.plot(xx, sq_(Nt_), color=c, lw=0.9, label=f"{Nt_} ⟦số hạng lẻ||odd terms⟧")
ax.axhline(gmax, color="k", ls=":", lw=0.8); ax.set_xlim(-0.05, 0.25); ax.legend(fontsize=8); ax.set_xlabel("x"); plt.tight_layout(); plt.show()''', dict(fig="gibbs", cap="⟦Hình 2. Tổng riêng của sóng vuông: khi thêm số hạng, dao động dồn vào gần bước nhảy nhưng quá độ (đường chấm, 1.179) không giảm.||Figure 2. Partial sums of a square wave: as terms are added the oscillations crowd toward the jump but the overshoot (dotted line, 1.179) does not decrease.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Chuỗi tam giác: {{ft_sum}}; chữ nhật {{ft_sum2}}. Gibbs: {{gb_max}} ({{gb_pct}} phần trăm), tổng riêng {{gb_sq}}. Chuỗi sin: {{fs_val}} so với {{fs_true}}. Biến đổi hữu hạn lệch {{fin_dev}}, $|2\\sin\\pi s|$ = {{fin_pi}}. Tổng Poisson lệch {{sh_dev}}.||Triangle train: {{ft_sum}}; rectangle {{ft_sum2}}. Gibbs: {{gb_max}} ({{gb_pct}} percent), partial sum {{gb_sq}}. Sine series: {{fs_val}} against {{fs_true}}. The finite transform deviates {{fin_dev}}, $|2\\sin\\pi s|$ = {{fin_pi}}. The Poisson sum deviates {{sh_dev}}.⟧"""),
        ("md", """## 4. ⟦Khai triển trực chuẩn, Gram-Schmidt, không gian tín hiệu||Orthonormal expansion, Gram-Schmidt, signal space⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Năng lượng sai số $E-\\sum s_k^2$, tương quan bằng bộ lọc phối hợp, Gram-Schmidt trên các tín hiệu chữ nhật, ổn định của MGS, và hình học trong không gian tín hiệu có đúng?||Do the error energy $E-\\sum s_k^2$, correlation by matched filter, Gram-Schmidt on rectangular signals, the stability of MGS and the geometry of signal space hold?⟧"""),
        ("code", r'''# ⟦s(t) = t, cơ sở cosin||s(t) = t, cosine basis⟧
tg = np.linspace(0, 1, 400001)
st = tg
E = trap(st**2, tg)
def coef(k):
    ph_ = np.ones_like(tg) if k == 0 else np.sqrt(2)*np.cos(k*np.pi*tg)
    return trap(st*ph_, tg)
sk = np.array([coef(k) for k in range(0, 51)])
def err_int(K):
    approx = sum(sk[k]*(np.ones_like(tg) if k == 0 else np.sqrt(2)*np.cos(k*np.pi*tg)) for k in range(K + 1))
    return trap((st - approx)**2, tg)
e5 = E - np.sum(sk[:6]**2); e5i = err_int(5)
e50 = E - np.sum(sk**2)
assert abs(e5 - e5i) < 1e-7 and abs(e50 - err_int(50)) < 1e-7
assert abs(sk[1] - np.sqrt(2)*((-1) - 1)/np.pi**2) < 1e-8
report("gf_err5", e5, ".4f"); report("gf_err50", e50, ".5f")
# ⟦bộ lọc phối hợp||matched filter⟧
phi1 = np.sqrt(2)*np.cos(np.pi*tg)
s1_corr = trap(st*phi1, tg)
Tm = 1.0; dtm = tg[1] - tg[0]
h_mf = phi1[::-1]                                    # ⟦φ(T − τ)||φ(T − τ)⟧
y_T = np.convolve(st, h_mf)[len(tg) - 1]*dtm
assert abs(s1_corr - y_T) < 1e-4 and abs(s1_corr + 2*np.sqrt(2)/np.pi**2) < 1e-8
report("mf_s1", s1_corr, ".4f")
# ⟦Gram-Schmidt: bốn tín hiệu chữ nhật||Gram-Schmidt: four rectangular signals⟧
Ng = 3000; tt = (np.arange(Ng) + 0.5)/Ng; dtg = 1/Ng
s_a = ((tt >= 0) & (tt < 1/3)).astype(float); s_b = ((tt >= 1/3) & (tt < 2/3)).astype(float); s_c = ((tt >= 2/3) & (tt < 1)).astype(float)
S = np.vstack([s_a, s_b, s_c, s_b - s_c])
Gm = S @ S.T*dtg
rank = np.linalg.matrix_rank(Gm, tol=1e-8)
assert rank == 3
def gram_schmidt(S, modified):
    Q = []
    for s in S:
        f = s.copy()
        for q in Q:
            f = f - (f @ q*dtg if modified else s @ q*dtg)*q
        nrm = np.sqrt(f @ f*dtg)
        if nrm > 1e-9: Q.append(f/nrm)
    return np.array(Q)
Qg = gram_schmidt(S, True)
assert len(Qg) == 3
Ecoef = np.array([[np.sum(Qg[j]*Qg[i])*dtg for i in range(3)] for j in range(3)])
assert np.max(np.abs(Ecoef - np.eye(3))) < 1e-9
coords4 = (S[3] @ Qg.T)*dtg
assert np.allclose(coords4/np.sqrt(1/3), [0, 1, -1], atol=1e-9)
report("gs_K", rank, "d"); report("gs_E", np.sum(Qg[0]**2)*dtg, ".0f"); report("gs_orth", max(np.max(np.abs(Ecoef - np.eye(3))), 1e-16), ".0e")
report("gs_len4", np.linalg.norm(coords4)/np.sqrt(1/3), ".4f")
# ⟦hình học||geometry⟧
c2 = (S[1] @ Qg.T)*dtg; c3 = (S[2] @ Qg.T)*dtg
d_c = np.linalg.norm(c2 - c3); d_i = np.sqrt(np.sum((S[1] - S[2])**2)*dtg)
rho = (c2 @ c3)/(np.linalg.norm(c2)*np.linalg.norm(c3))
assert abs(d_c - d_i) < 1e-9 and abs(rho) < 1e-12
report("gr_d", d_c, ".4f"); report("gr_di", d_i, ".4f"); report("gr_rho", abs(rho), ".0f")
# ⟦CGS và MGS trên ma trận Hilbert||CGS and MGS on the Hilbert matrix⟧
def gs_matrix(A, modified):
    m, n = A.shape; Q = np.zeros((m, n));
    for j in range(n):
        v = A[:, j].copy()
        for i in range(j):
            v -= (Q[:, i] @ (v if modified else A[:, j]))*Q[:, i]
        Q[:, j] = v/np.linalg.norm(v)
    return Q
from scipy.linalg import hilbert
H = hilbert(12)
cg = np.linalg.norm(gs_matrix(H, False).T @ gs_matrix(H, False) - np.eye(12))
mg = np.linalg.norm(gs_matrix(H, True).T @ gs_matrix(H, True) - np.eye(12))
Rm = rg.standard_normal((30, 12))
cgg = np.linalg.norm(gs_matrix(Rm, False).T @ gs_matrix(Rm, False) - np.eye(12)); mgg = np.linalg.norm(gs_matrix(Rm, True).T @ gs_matrix(Rm, True) - np.eye(12))
assert cg > 1e-3*1 and mg < cg/10
report("cgs_err", cg, ".1e"); report("mgs_err", mg, ".1e"); report("cgs_good", cgg, ".1e"); report("mgs_good", mgg, ".1e")
# ⟦Fourier: cosin trực chuẩn||Fourier: orthonormal cosines⟧
Tq = 1.0
ph = [np.sqrt(2/Tq)*np.cos(2*k*np.pi*tg/Tq) for k in (1, 2, 3)]
Gc = np.array([[trap(a*b, tg) for b in ph] for a in ph])
assert np.max(np.abs(Gc - np.eye(3))) < 1e-8
report("fo_dev", max(np.max(np.abs(Gc - np.eye(3))), 1e-16), ".0e")
frac = 8/np.pi**2*(1 + 1/9 + 1/25)
sqw = np.where(tg < 0.5, 1.0, -1.0)
sqc = [trap(sqw*np.sqrt(2)*np.sin(2*np.pi*k*tg), tg) for k in (1, 3, 5)]
assert abs(sum(c**2 for c in sqc) - frac) < 1e-4
report("fo_frac", frac, ".4f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Sai số năng lượng: {{gf_err5}} (5 số hạng) và {{gf_err50}} (50); $s_1$ = {{mf_s1}}. Gram-Schmidt: $K$ = {{gs_K}}, năng lượng cơ sở {{gs_E}}, trực giao {{gs_orth}}, độ dài $s_4$ {{gs_len4}}. Hình học: khoảng cách {{gr_d}} và {{gr_di}}, $\\rho$ = {{gr_rho}}. CGS/MGS: {{cgs_err}} và {{mgs_err}}, ma trận tốt {{cgs_good}} và {{mgs_good}}. Fourier: {{fo_dev}}, {{fo_frac}}.||Error energy: {{gf_err5}} (5 terms) and {{gf_err50}} (50); $s_1$ = {{mf_s1}}. Gram-Schmidt: $K$ = {{gs_K}}, basis energy {{gs_E}}, orthogonality {{gs_orth}}, length of $s_4$ {{gs_len4}}. Geometry: distances {{gr_d}} and {{gr_di}}, $\\rho$ = {{gr_rho}}. CGS/MGS: {{cgs_err}} and {{mgs_err}}, well-conditioned {{cgs_good}} and {{mgs_good}}. Fourier: {{fo_dev}}, {{fo_frac}}.⟧"""),
        ("md", """## 5. ⟦Phương trình tích phân và Karhunen-Loève||Integral equations and Karhunen-Loève⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Trị riêng của nhân Green, Mercer, Wiener, nhân mũ và nhiễu trắng có đúng công thức của Barkat, tính bằng phân tích trị riêng ma trận, bằng nghiệm phương trình siêu việt và bằng mô phỏng?||Do the eigenvalues of Green's kernels, Mercer, the Wiener, exponential and white-noise cases match Barkat's formulas, computed by matrix eigendecomposition, by transcendental-equation roots and by simulation?⟧"""),
        ("code", r'''# ⟦nhân Green min(u,t)(1 − max(u,t))||Green's kernel min(u,t)(1 − max(u,t))⟧
M = 800; tm = (np.arange(M) + 0.5)/M
Kg = np.minimum.outer(tm, tm)*(1 - np.maximum.outer(tm, tm))/M
eg = np.sort(np.linalg.eigvalsh(Kg))[::-1]
assert abs(eg[0] - 1/np.pi**2) < 1e-5 and abs(eg[1] - 1/(4*np.pi**2)) < 1e-5
report("gr_e1", eg[0], ".4f"); report("gr_e2", eg[1], ".4f")
u, t = 0.3, 0.6
kk = min(u, t)*(1 - max(u, t))
mer = sum(2*np.sin(k*np.pi*u)*np.sin(k*np.pi*t)/(k*np.pi)**2 for k in range(1, 20000))
assert abs(kk - 0.12) < 1e-15 and abs(mer - kk) < 1e-7
report("gr_k", kk, ".2f"); report("gr_mer", mer, ".4f")
Kf = (1 - np.maximum.outer(tm, tm))/M
ef = np.sort(np.linalg.eigvalsh((Kf + Kf.T)/2))[::-1]
assert abs(ef[0] - 4/np.pi**2) < 1e-4
report("gr_f1", ef[0], ".4f")
# ⟦tương tự ma trận||matrix analogy⟧
Nm = 50
A = 2*np.eye(Nm) - np.eye(Nm, k=1) - np.eye(Nm, k=-1)
wa = np.linalg.eigvalsh(A); wk = np.linalg.eigvalsh(np.linalg.inv(A))
assert abs(wa.min()*wk.max() - 1) < 1e-9
report("ma_a", wa.min(), ".5f"); report("ma_k", wk.max(), ".2f")
# ⟦Wiener α = 1, T = 1||Wiener α = 1, T = 1⟧
Kw = np.minimum.outer(tm, tm)/M
ew, vw = np.linalg.eigh(Kw); order = np.argsort(ew)[::-1]; ew = ew[order]; vw = vw[:, order]
lam_n = lambda n: 1/((n - 0.5)**2*np.pi**2)
for n_ in range(1, 5):
    assert abs(ew[n_ - 1] - lam_n(n_)) < 2e-5
    report(f"kl_w{n_}", lam_n(n_), ".4f")
tot = sum(lam_n(n_) for n_ in range(1, 200000))
assert abs(tot - 0.5) < 1e-5 and abs(np.trace(Kw) - 0.5*(1 + 1/M)/1*0.5*2*0.5 + 0) >= 0
report("kl_sum", 0.5, ".1f")
# ⟦mô phỏng đường Wiener chiếu lên hàm riêng||simulate Wiener paths projected on eigenfunctions⟧
Npath, Nt = 100000, 400; dtw = 1/Nt
Wp = np.cumsum(rg.normal(0, np.sqrt(dtw), (Npath, Nt)), axis=1)
tw = (np.arange(Nt) + 1)*dtw
phi_n = lambda n_: np.sqrt(2)*np.sin((n_ - 0.5)*np.pi*tw)
X1 = Wp @ phi_n(1)*dtw; X2 = Wp @ phi_n(2)*dtw
assert abs(np.var(X1) - lam_n(1)) < 0.01 and abs(np.corrcoef(X1, X2)[0, 1]) < 0.01
kurt = np.mean(X1**4)/np.var(X1)**2 - 3
assert abs(kurt) < 0.1
report("kl_v1", np.var(X1), ".3f"); report("kl_corr", 0.0, ".0f"); report("kl_kurt", 0.0, ".0f")
# ⟦nhân mũ trên [−1, 1], α = σ = 1||exponential kernel on [−1, 1], α = σ = 1⟧
Mo = 800; to = -1 + (np.arange(Mo) + 0.5)*2/Mo
Ko = np.exp(-np.abs(np.subtract.outer(to, to)))*2/Mo
eo = np.sort(np.linalg.eigvalsh(Ko))[::-1]
b1 = optimize.brentq(lambda b: b*np.tan(b) - 1, 1e-6, np.pi/2 - 1e-6)
b2 = optimize.brentq(lambda b: b/np.tan(b) + 1, np.pi/2 + 1e-6, np.pi - 1e-6)
b3 = optimize.brentq(lambda b: b*np.tan(b) - 1, np.pi + 1e-6, 3*np.pi/2 - 1e-6)
b4 = optimize.brentq(lambda b: b/np.tan(b) + 1, 3*np.pi/2 + 1e-6, 2*np.pi - 1e-6)
lam_o = [2/(1 + b**2) for b in (b1, b2, b3, b4)]
assert np.max(np.abs(np.array(lam_o) - eo[:4])) < 2e-4
report("ou_l1", lam_o[0], ".4f"); report("ou_l2", lam_o[1], ".4f")
report("ou_frac", sum(lam_o)/2, ".3f")
# ⟦nhiễu trắng: hai cơ sở||white noise: two bases⟧
Nw = 2000000; nfr = 200
wn = rg.standard_normal((Nw//nfr, nfr))
cos_b = np.sqrt(2/nfr)*np.cos(2*np.pi*(np.arange(nfr) + 0.5)/nfr)
sin_b = np.sqrt(2/nfr)*np.sin(2*np.pi*(np.arange(nfr) + 0.5)/nfr)
c1 = wn @ cos_b; s1_ = wn @ sin_b
assert abs(np.var(c1) - 1) < 0.02 and abs(np.var(s1_) - 1) < 0.02 and abs(np.corrcoef(c1, s1_)[0, 1]) < 0.02
report("wn_c", np.var(c1), ".1f"); report("wn_s", np.var(s1_), ".1f"); report("wn_x", 0.0, ".0f")'''),
        ("code", r'''fig, ax = plt.subplots(figsize=(7.2, 3.3))
nrange = np.arange(1, 13)
ax.semilogy(nrange, ew[:12], "o", label=("⟦ma trận||matrix⟧")); ax.semilogy(nrange, [lam_n(n_) for n_ in nrange], "-", label=r"αT²/[(n−½)²π²]")
ax.set_xlabel("n"); ax.set_ylabel("λₙ"); ax.legend(fontsize=8); plt.tight_layout(); plt.show()''', dict(fig="kl_eig", cap="⟦Hình 3. Trị riêng của nhân Wiener min(t,u): phân tích trị riêng ma trận (chấm) trùng công thức αT²/[(n−½)²π²] (đường), giảm như 1/n².||Figure 3. Eigenvalues of the Wiener kernel min(t,u): matrix eigendecomposition (dots) matches αT²/[(n−½)²π²] (line), decaying like 1/n².⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Nhân Green: {{gr_e1}}, {{gr_e2}}; Mercer {{gr_k}} và {{gr_mer}}; nhân $1-\\max$: {{gr_f1}}. Ma trận: {{ma_a}} và {{ma_k}}. Wiener: {{kl_w1}}, {{kl_w2}}, {{kl_w3}}, {{kl_w4}}; tổng {{kl_sum}}; phương sai $X_1$ {{kl_v1}}; tương quan {{kl_corr}}; độ nhọn dư {{kl_kurt}}. Nhân mũ: {{ou_l1}}, {{ou_l2}}, bốn đầu chiếm {{ou_frac}}. Nhiễu trắng: {{wn_c}}, {{wn_s}}, {{wn_x}}.||Green's kernel: {{gr_e1}}, {{gr_e2}}; Mercer {{gr_k}} and {{gr_mer}}; the $1-\\max$ kernel: {{gr_f1}}. Matrix: {{ma_a}} and {{ma_k}}. Wiener: {{kl_w1}}, {{kl_w2}}, {{kl_w3}}, {{kl_w4}}; sum {{kl_sum}}; variance of $X_1$ {{kl_v1}}; correlation {{kl_corr}}; excess kurtosis {{kl_kurt}}. Exponential kernel: {{ou_l1}}, {{ou_l2}}, the first four hold {{ou_frac}}. White noise: {{wn_c}}, {{wn_s}}, {{wn_x}}.⟧"""),
    ],
)


# ---------------------------------------------------------------- extra slides
_EXTRA = {
0: [
 ("⟦Đối ngẫu: lấy mẫu phổ||Duality: sampling the spectrum⟧",
  "<p>⟦Định lý lấy mẫu áp dụng đối xứng ở miền còn lại: nếu $f(x)=0$ ngoài $|x|\\le x_c$ (hàm có độ dài hữu hạn) thì $F(s)$ được xác định bởi các mẫu cách nhau $\\tfrac1{2x_c}$: $F(s)=\\sum F\\!\\left(\\tfrac n{2x_c}\\right)\\text{sinc}(2x_cs-n)$. Đó chính là tính chất mà chuỗi Fourier dùng: hệ số là mẫu của biến đổi một chu kỳ (phần 3). Nói gọn, độ rộng hữu hạn ở một miền cho phép lấy mẫu ở miền kia.||The sampling theorem applies symmetrically in the other domain: if $f(x)=0$ outside $|x|\\le x_c$ (a function of finite duration) then $F(s)$ is determined by samples spaced $\\tfrac1{2x_c}$ apart: $F(s)=\\sum F\\!\\left(\\tfrac n{2x_c}\\right)\\text{sinc}(2x_cs-n)$. This is exactly the property the Fourier series uses: the coefficients are samples of the transform of one period (part 3). In short, finite width in one domain permits sampling in the other.⟧</p>"
  + F("⟦Lấy mẫu phổ||Sampling the spectrum⟧", r"F(s)=\sum_nF\!\left(\frac n{2x_c}\right)\operatorname{sinc}(2x_cs-n)")),
 ("⟦Đếm số bậc tự do||Counting degrees of freedom⟧",
  "<p>⟦Một tín hiệu giới hạn băng $|s|\\le s_c$ quan sát trong thời gian $T$ cần $2s_cT$ mẫu tự do. Với $s_c=5$ và $T=3$: $2\\times5\\times3=30$ giá trị. Đây là số thành phần của vector biểu diễn, và là cầu nối tới phần 4: một tín hiệu như vậy nằm trong không gian tín hiệu 30 chiều, và mỗi mẫu độc lập là một tọa độ trên cơ sở sinc. Nó cũng là lý do lấy mẫu nhanh hơn mức tới hạn không thêm thông tin, chỉ thêm dư thừa cho lọc (Bracewell, tr. 224 đến 226).||A signal band-limited to $|s|\\le s_c$ observed for a time $T$ needs $2s_cT$ free samples. With $s_c=5$ and $T=3$: $2\\times5\\times3=30$ values. This is the number of components of the representing vector and a bridge to part 4: such a signal lives in a 30-dimensional signal space, and each independent sample is a coordinate on the sinc basis. It is also why sampling faster than critical adds no information, only redundancy useful for filtering (Bracewell, pp. 224 to 226).⟧</p>"),
 ("⟦Ví dụ tay: nội suy điểm giữa||A hand example: midpoint interpolation⟧",
  "<p>⟦Cho mẫu $f(-1)=0.2$, $f(0)=1$, $f(1)=0.4$, $f(2)=0$ và coi các mẫu khác bằng 0, giá trị tại $x=0.5$ theo nội suy sinc: hai mẫu gần nhất mỗi mẫu nhân {{mid_1}}, mẫu kế nhân {{mid_2}}. Ta có $f(0.5)\\approx0.6366(1+0.4)-0.2122(0.2+0)=0.8913-0.0424=0.8488$. Các hệ số trên là hàng của bảng 10.1; bậc lớn hơn thêm các hệ số {{mid_3}}, {{mid_4}} với dấu xen kẽ và giảm chậm như $1/n$, nên phải dùng nhiều mẫu để đạt độ chính xác cao (Bracewell, tr. 224).||Given samples $f(-1)=0.2$, $f(0)=1$, $f(1)=0.4$, $f(2)=0$ and all others zero, the value at $x=0.5$ by sinc interpolation: the two nearest samples are each multiplied by {{mid_1}}, the next by {{mid_2}}. We get $f(0.5)\\approx0.6366(1+0.4)-0.2122(0.2+0)=0.8913-0.0424=0.8488$. The coefficients are the row of Table 10.1; higher orders add the coefficients {{mid_3}}, {{mid_4}} with alternating signs decaying slowly like $1/n$, so many samples are needed for high accuracy (Bracewell, p. 224).⟧</p>"),
 ("⟦Hướng dẫn thực hành chọn khoảng lấy mẫu||A practical guide to choosing the interval⟧",
  UL(["⟦Xác định $s_c$ từ phổ đo được, có chừa lề: đảo phổ không được chạm nhau, nếu không xảy ra chồng phổ (tần số 0.8 thành {{al_f}}).||Determine $s_c$ from the measured spectrum with a margin: the islands must not touch, otherwise aliasing occurs (frequency 0.8 becomes {{al_f}}).⟧",
      "⟦Lọc trước khi lấy mẫu để bỏ phần đuôi phổ; sau khi lấy mẫu không thể tách phần chồng.||Filter before sampling to remove the spectral tail; after sampling the overlap cannot be separated.⟧",
      "⟦Nếu phải lọc chữ nhật tốt, lấy mẫu ở nửa khoảng tới hạn rồi dùng mảng lọc của bảng 10.2.||If a good rectangular filter is needed, sample at half the critical interval and use the filtering array of Table 10.2.⟧",
      "⟦Kiểm tra sai số do coi tín hiệu là giới hạn băng, như sai số {{smp_err}} trong ví dụ đầu.||Check the error of taking the signal as band-limited, like the error {{smp_err}} in the first example.⟧"])),
],
1: [
 ("⟦So sánh ba cách lấy mẫu||Comparing three sampling schemes⟧",
  TBL(["⟦Cách||Scheme⟧", "⟦Dữ liệu cần||Data needed⟧", "⟦Chịu nhiễu||Noise behaviour⟧"],
      [["⟦Đều, khoảng tới hạn||Uniform, critical⟧", "$f(n)$", "⟦giữ phương sai ({{nz_var}})||keeps the variance ({{nz_var}})⟧"],
       ["⟦Tung độ và độ dốc||Ordinate and slope⟧", "$f(n),f'(n)$", "⟦độ dốc cần đo chính xác||the slope must be measured accurately⟧"],
       ["⟦Xen kẽ||Interlaced⟧", "$f(n),f(n+a)$", "⟦khuếch đại ({{il_amp}})||amplifies ({{il_amp}})⟧"]])
  + "<p>⟦Cả ba đều tái tạo chính xác hàm giới hạn băng; sự khác nhau nằm ở độ nhạy với sai số dữ liệu.||All three reconstruct a band-limited function exactly; the difference lies in the sensitivity to data errors.⟧</p>"),
 ("⟦Vì sao $a\\to0$ dẫn tới độ dốc||Why $a\\to0$ leads to the slope⟧",
  "<p>⟦Khi $a\\to0$, hai mẫu $f(n)$ và $f(n+a)$ gần nhau; hiệu chia cho $a$ tiến về $f'(n)$, nên lấy mẫu xen kẽ tiến tới tung độ và độ dốc. Nhưng nhân $a(x)$ có $\\sin\\pi a$ dưới mẫu số: hệ số phóng đại khoảng $1/\\pi a$, khiến sai số hai mẫu sát nhau bị nhân lên. Đây là cơ chế của khuếch đại nhiễu: $a=0.2$ cho {{il_amp}}, còn $a=0.5$ chỉ {{il_amp5}} (Bracewell, tr. 232 đến 236).||As $a\\to0$ the two samples $f(n)$ and $f(n+a)$ come together; the difference divided by $a$ tends to $f'(n)$, so interlaced sampling tends to ordinate-and-slope sampling. But the kernel $a(x)$ has $\\sin\\pi a$ in the denominator: an amplification of about $1/\\pi a$, which magnifies errors of the two close samples. This is the mechanism of noise amplification: $a=0.2$ gives {{il_amp}} while $a=0.5$ gives only {{il_amp5}} (Bracewell, pp. 232 to 236).⟧</p>"),
 ("⟦Ví dụ tay: lấy mẫu độc lập với sai số||A hand example: independent sample errors⟧",
  "<p>⟦Giả sử mỗi mẫu có sai số độc lập độ lệch chuẩn 0.01. Với nội suy sinc đều, độ lệch chuẩn của giá trị nội suy cũng 0.01 (hệ số 1). Với xen kẽ $a=0.2$, phương sai nhân {{il_amp}} nên độ lệch chuẩn nhân căn bậc hai của số đó, lớn hơn rõ. Khi thiết bị đo có độ chính xác thấp, chọn lấy mẫu đều dày hơn thay vì xen kẽ (Bracewell, tr. 235 đến 236).||Suppose each sample has an independent error of standard deviation 0.01. With uniform sinc interpolation the standard deviation of the interpolated value is also 0.01 (a factor of 1). With interlaced $a=0.2$ the variance is multiplied by {{il_amp}} so the standard deviation by its square root, clearly larger. When the instrument is inaccurate, choose denser uniform sampling instead of interlacing (Bracewell, pp. 235 to 236).⟧</p>"),
],
2: [
 ("⟦Dạng thực và tính chẵn lẻ||Real form and parity⟧",
  "<p>⟦Từ $a_n-ib_n=2F(n)$: nếu $f$ chẵn thì $F(n)$ thực và $b_n=0$, chuỗi chỉ gồm cosin; nếu $f$ lẻ thì $F$ ảo thuần và chuỗi chỉ gồm sin. Sóng vuông $\\pm1$ là hàm lẻ, chỉ có các sin họa âm lẻ với hệ số $4/(\\pi k)$, đó là cơ sở của phép tính Gibbs ở trên. Với chuỗi tam giác chẵn thì mọi hệ số sin bằng 0 và các hệ số cosin $2F(n)$ không âm, tổng {{ft_sum}} tại gốc (Bracewell, tr. 237 đến 245).||From $a_n-ib_n=2F(n)$: if $f$ is even then $F(n)$ is real and $b_n=0$, the series contains cosines only; if $f$ is odd then $F$ is purely imaginary and the series contains sines only. The $\\pm1$ square wave is odd, having only odd-harmonic sines with coefficients $4/(\\pi k)$, the basis of the Gibbs computation above. For the even triangle train all sine coefficients vanish and the cosine coefficients $2F(n)$ are nonnegative, summing to {{ft_sum}} at the origin (Bracewell, pp. 237 to 245).⟧</p>"),
 ("⟦Điểm gián đoạn và trung điểm||Discontinuities and the midpoint⟧",
  "<p>⟦Tại điểm gián đoạn nhảy, chuỗi hội tụ về trung bình $\\tfrac12[g(x+0)+g(x-0)]$ (Dirichlet), nên sóng vuông $\\pm1$ có tổng bằng 0 tại bước nhảy. Chuỗi xung chữ nhật cho tổng {{ft_sum2}} tại đỉnh, không phải 1 chính xác vì cắt ở 20000 số hạng, còn tại mép nó đến giá trị một nửa. Chú ý: hội tụ điểm này không đều: dao động Gibbs cho thấy sai số lớn nhất không nhỏ dần (Bracewell, tr. 236, 240 đến 242).||At a jump discontinuity the series converges to the mean $\\tfrac12[g(x+0)+g(x-0)]$ (Dirichlet), so the $\\pm1$ square wave sums to 0 at the step. The rectangular pulse train sums to {{ft_sum2}} at the peak, not exactly 1 due to truncation at 20000 terms, while at the edge it reaches half the value. Note that this pointwise convergence is not uniform: the Gibbs oscillation shows that the maximum error does not decrease (Bracewell, pp. 236, 240 to 242).⟧</p>"),
 ("⟦Chuỗi xung: shah là tổng các mũ phức||The impulse train: shah as a sum of complex exponentials⟧",
  "<p>⟦Phổ của $\\text{III}(x)$ là $\\text{III}(s)$: xung tại mọi số nguyên có cường độ 1, nên mọi họa âm có biên độ bằng nhau và $\\text{III}(x)=\\sum_ne^{i2\\pi nx}$. Chuỗi Fourier của chuỗi xung không hội tụ theo nghĩa thông thường mà chỉ theo nghĩa hàm suy rộng; đó là lý do định nghĩa bằng dãy xác định (hàng gai Gauss) ở slide trước, với tổng Poisson kiểm được bằng số, lệch {{sh_dev}} (Bracewell, tr. 246 đến 248).||The spectrum of $\\text{III}(x)$ is $\\text{III}(s)$: unit impulses at every integer, so every harmonic has equal amplitude and $\\text{III}(x)=\\sum_ne^{i2\\pi nx}$. The Fourier series of the impulse train does not converge in the ordinary sense but only in the sense of generalised functions; that is why it is defined through a defining sequence (a row of Gaussian spikes) in the previous slide, with the Poisson sum checked numerically to deviation {{sh_dev}} (Bracewell, pp. 246 to 248).⟧</p>"),
],
3: [
 ("⟦Hệ đầy đủ và đẳng thức Parseval bằng số||Completeness and Parseval, numerically⟧",
  "<p>⟦Hệ trực chuẩn gọi là đầy đủ nếu năng lượng sai số tiến về 0 khi $K\\to\\infty$, tức là đẳng thức Parseval $E=\\sum s_k^2$. Với $s(t)=t$ và cơ sở cosin: sau 5 số hạng năng lượng sai số {{gf_err5}}, sau 50 còn {{gf_err50}}, giảm như $1/K^3$ vì hệ số giảm như $1/k^2$. Nếu bỏ mất một hàm cơ sở cần thiết, sai số không tiến về 0. Hệ cosin nửa chu kỳ đầy đủ cho hàm trên $[0,1]$ mặc dù không có sin (Barkat, tr. 452 đến 454).||An orthonormal set is called complete if the error energy tends to 0 as $K\\to\\infty$, i.e. Parseval's identity $E=\\sum s_k^2$. With $s(t)=t$ and the cosine basis: after 5 terms the error energy is {{gf_err5}}, after 50 it is {{gf_err50}}, decaying like $1/K^3$ because the coefficients fall like $1/k^2$. If a necessary basis function is omitted the error does not tend to 0. The half-period cosine set is complete for functions on $[0,1]$ even without sines (Barkat, pp. 452 to 454).⟧</p>"),
 ("⟦Khoảng cách, năng lượng và tương quan||Distance, energy and correlation⟧",
  "<p>⟦Từ định nghĩa: $\\|s_k-s_j\\|^2=E_k+E_j-2\\sqrt{E_kE_j}\\rho_{kj}$, trong đó $\\rho_{kj}$ là hệ số tương quan. Với $s_2,s_3$ ở ví dụ 8.1 (năng lượng bằng nhau $E$, $\\rho=$ {{gr_rho}}): khoảng cách bằng $\\sqrt{2E}$ = {{gr_d}} với $E=1/3$. Khi $\\rho=1$ khoảng cách 0; khi $\\rho=-1$ khoảng cách cực đại $\\sqrt E_k+\\sqrt E_j$. Trong phát hiện, ta chọn các tín hiệu có khoảng cách lớn để dễ phân biệt (module 21).||From the definitions: $\\|s_k-s_j\\|^2=E_k+E_j-2\\sqrt{E_kE_j}\\rho_{kj}$, where $\\rho_{kj}$ is the correlation coefficient. For $s_2,s_3$ of example 8.1 (equal energy $E$, $\\rho=$ {{gr_rho}}): the distance is $\\sqrt{2E}$ = {{gr_d}} with $E=1/3$. When $\\rho=1$ the distance is 0; when $\\rho=-1$ the distance is the maximum $\\sqrt E_k+\\sqrt E_j$. In detection we choose signals with large distance to make them easy to tell apart (module 21).⟧</p>"),
 ("⟦Các hệ trực chuẩn quen thuộc||Familiar orthonormal sets⟧",
  TBL(["⟦Hệ||Set⟧", "⟦Hàm||Functions⟧", "⟦Ghi chú||Note⟧"],
      [["⟦Cosin||Cosine⟧", "$\\sqrt2\\cos k\\pi t$", "⟦trên $[0,1]$, {{gf_err50}} sau 50 số hạng||on $[0,1]$, {{gf_err50}} after 50 terms⟧"],
       ["⟦Lượng giác||Trigonometric⟧", "$\\sqrt{2/T}\\cos(2k\\pi t/T)$", "⟦lệch đơn vị {{fo_dev}}||identity deviation {{fo_dev}}⟧"],
       ["⟦Sinc||Sinc⟧", "$\\text{sinc}(x-n)$", "⟦hàm giới hạn băng||band-limited functions⟧"],
       ["⟦Chữ nhật||Rectangular⟧", "$\\sqrt{3/T}$⟦ trên đoạn||on a segment⟧", "⟦Gram-Schmidt, $K$ = {{gs_K}}||Gram-Schmidt, $K$ = {{gs_K}}⟧"]])),
],
4: [
 ("⟦Tỉ lệ năng lượng của các thành phần đầu||The energy fraction of the first components⟧",
  "<p>⟦Trị riêng $\\lambda_k$ cho biết mỗi thành phần chứa bao nhiêu năng lượng trung bình. Với Wiener $\\alpha=T=1$: $\\lambda_1$ = {{kl_w1}} trên tổng {{kl_sum}}, tức thành phần đầu chứa khoảng 81 phần trăm ($8/\\pi^2$); hai thành phần đầu chứa {{kl_w1}}+{{kl_w2}} trên {{kl_sum}}. Với nhân mũ, bốn trị riêng đầu chiếm {{ou_frac}}. Vì các trị riêng giảm nhanh, khai triển cắt ngắn đủ để xấp xỉ quá trình (Barkat, tr. 481 đến 495).||The eigenvalue $\\lambda_k$ tells how much mean energy each component holds. For Wiener with $\\alpha=T=1$: $\\lambda_1$ = {{kl_w1}} out of the total {{kl_sum}}, i.e. the first component holds about 81 percent ($8/\\pi^2$); the first two hold {{kl_w1}}+{{kl_w2}} out of {{kl_sum}}. For the exponential kernel the first four eigenvalues hold {{ou_frac}}. Because the eigenvalues fall quickly a truncated expansion approximates the process well (Barkat, pp. 481 to 495).⟧</p>"),
 ("⟦Quy trình giải Karhunen-Loève cho phổ hữu tỉ||Solving Karhunen-Loève for a rational spectrum⟧",
  OL(["⟦Viết $S_{xx}(\\omega)=N(\\omega^2)/D(\\omega^2)$ và chuyển thành toán tử $[\\lambda D(-p^2)-N(-p^2)]\\Phi(p)=0$.||Write $S_{xx}(\\omega)=N(\\omega^2)/D(\\omega^2)$ and turn it into the operator $[\\lambda D(-p^2)-N(-p^2)]\\Phi(p)=0$.⟧",
      "⟦Tìm nghiệm tổng quát của phương trình vi phân hệ số hằng, ứng với các gốc của phương trình đặc trưng.||Find the general solution of the constant-coefficient differential equation from the roots of the characteristic equation.⟧",
      "⟦Thay vào phương trình tích phân để tìm điều kiện biên; chia bài toán thành nghiệm chẵn và lẻ trên khoảng đối xứng.||Substitute into the integral equation to obtain the boundary conditions; split into even and odd solutions on a symmetric interval.⟧",
      "⟦Giải phương trình siêu việt cho $\\beta$ ($\\beta\\tan\\beta T=\\alpha$ hoặc $\\beta\\cot\\beta T=-\\alpha$), rồi $\\lambda=2\\alpha\\sigma^2/(\\alpha^2+\\beta^2)$.||Solve the transcendental equation for $\\beta$ ($\\beta\\tan\\beta T=\\alpha$ or $\\beta\\cot\\beta T=-\\alpha$), then $\\lambda=2\\alpha\\sigma^2/(\\alpha^2+\\beta^2)$.⟧",
      "⟦Kiểm tra các giá trị $\\lambda$ còn lại không là trị riêng và chuẩn hóa hàm riêng. Kết quả: $\\lambda_1$ = {{ou_l1}}, $\\lambda_2$ = {{ou_l2}}.||Check that the remaining values of $\\lambda$ are not eigenvalues and normalise the eigenfunctions. Result: $\\lambda_1$ = {{ou_l1}}, $\\lambda_2$ = {{ou_l2}}.⟧"])),
 ("⟦Vì sao Karhunen-Loève là cơ sở tốt nhất||Why Karhunen-Loève is the best basis⟧",
  "<p>⟦Sai số bình phương trung bình khi cắt tại $K$ số hạng là $\\sum_{k>K}\\lambda_k$ theo cơ sở K-L; trong mọi cơ sở trực chuẩn khác, sai số cắt bình phương trung bình không nhỏ hơn giá trị đó (tính chất tối ưu chuẩn của khai triển, không phải điều Barkat chứng minh riêng). Đối với Wiener, cắt sau một thành phần còn lại {{kl_sum}}−{{kl_w1}} năng lượng trung bình. Ý nghĩa: dùng ít hệ số nhất cho cùng độ chính xác, và các hệ số độc lập khi quá trình Gauss.||The mean-square truncation error at $K$ terms is $\\sum_{k>K}\\lambda_k$ in the K-L basis; in any other orthonormal basis the mean-square truncation error is no smaller (the standard optimality property of the expansion, not something Barkat proves separately). For the Wiener process, truncating after one component leaves {{kl_sum}}−{{kl_w1}} of the mean energy. Meaning: the fewest coefficients for a given accuracy, and independent coefficients when the process is Gaussian.⟧</p>"),
],
}
for _i, _sl in _EXTRA.items():
    MOD["parts"][_i]["slides"][-1:-1] = _sl
