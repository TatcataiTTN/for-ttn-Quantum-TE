from lib import F, C, UL, OL, TBL

MOD = dict(
    n=5, slug="impulse", part="A", book="B",
    title="⟦Ký hiệu xung: $\\delta$, tính chất sàng, shah và hàm suy rộng||The impulse symbol: $\\delta$, sifting, shah and generalized functions⟧",
    blurb="⟦Xung là dãy xung ngắn diện tích 1 mà chi tiết dạng không quan trọng: tính chất sàng, chuỗi xung shah, đạo hàm của xung, hàm rỗng và cơ sở hàm suy rộng.||"
          "The impulse is a sequence of brief unit-area pulses whose detailed shape does not matter: sifting, the shah train, derivatives of the impulse, null functions and the basis of generalized functions.⟧",
    src="⟦Bracewell, chương 5, tr. 74–98||Bracewell, chapter 5, pp. 74–98⟧",
    data="⟦Sinh bằng mã: mạch RC với các xung khác dạng, dãy xung đủ dạng (chữ nhật, Gauss, tam giác, sinc, Lorentz), chuỗi shah và tổng Poisson||Generated in code: an RC circuit driven by pulses of different shapes, pulse sequences of many shapes (rectangle, Gaussian, triangle, sinc, Lorentzian), the shah train and Poisson sums⟧",
    objectives=[
        "⟦Giải thích $\\delta(x)$ như giới hạn của dãy xung diện tích 1, và vì sao dạng xung không quan trọng.||Explain $\\delta(x)$ as the limit of unit-area pulses and why the pulse shape does not matter.⟧",
        "⟦Dùng tính chất sàng, tỉ lệ $\\delta(ax)$, và cẩn thận với $x\\delta(x)$.||Use the sifting property, the scaling $\\delta(ax)$, and take care with $x\\delta(x)$.⟧",
        "⟦Dùng $\\text{III}(x)$ cho lấy mẫu và nhân bản, và cặp xung chẵn, lẻ cho sai phân.||Use $\\text{III}(x)$ for sampling and replication, and the even and odd pairs for finite differences.⟧",
        "⟦Tính với $\\delta'$, $\\delta''$, hàm rỗng và xung nhiều chiều.||Compute with $\\delta'$, $\\delta''$, null functions and multidimensional impulses.⟧",
        "⟦Hiểu hàm suy rộng là lớp các dãy chính quy, và đạo hàm định nghĩa bằng tích phân từng phần.||Understand a generalized function as a class of regular sequences, with derivatives defined by integration by parts.⟧",
    ],
    parts=[
        # ---------------------------------------------------------------- PART 1
        dict(
            title="⟦Từ xung vật lý tới ký hiệu $\\delta$||From the physical impulse to the symbol $\\delta$⟧",
            scr=("⟦Khối điểm, điện tích điểm, lực tập trung là các thực thể quen thuộc trong vật lý dù không tồn tại thật.||Point masses, point charges and concentrated forces are familiar in physics although they do not really exist.⟧",
                 "⟦Vì sao dùng thứ không tồn tại, và nói \"hàm bằng vô cùng tại gốc\" có nghĩa gì?||Why use something that does not exist, and what does \"a function infinite at the origin\" mean?⟧",
                 "⟦Coi xung là dấu hiệu tắt cho một xung ngắn, diện tích 1, mà chi tiết dạng không đo được.||Treat the impulse as shorthand for a brief unit-area pulse whose detailed shape cannot be measured.⟧"),
            preview=["⟦Xung là khái niệm về tích phân, không về dạng||The impulse is about the integral, not the shape⟧", "⟦Đáp ứng của mạch RC với các xung khác dạng||An RC circuit driven by pulses of different shapes⟧", "⟦Các dãy xác định $\\delta$ và bậc thang||Defining sequences of $\\delta$ and the step⟧"],
            slides=[
                ("⟦Xung: chỉ tích phân quan trọng||The impulse: only the integral matters⟧",
                 "<p>⟦Cần một ký hiệu cho xung mạnh, diện tích 1, ngắn tới mức thiết bị đo có độ phân giải cho trước không phân biệt được nó với xung ngắn hơn nữa. Cơ học gọi là \"xung lượng\". Thuộc tính quan trọng là tích phân của nó; chi tiết dạng không quan trọng (Bracewell, tr. 74).||"
                 "We need notation for intense unit-area pulses so brief that measuring equipment of a given resolving power cannot tell them from even briefer ones. Mechanics calls this an \"impulse\". The important attribute is its integral; the precise details of its form are unimportant (Bracewell, p. 74).⟧</p>"),
                ("⟦Lịch sử ký hiệu $\\delta(x)$||History of the symbol $\\delta(x)$⟧",
                 "<p>⟦Ý tưởng đã có hơn một thế kỷ trong giới toán: van der Pol và Bremmer (1955) dẫn các ví dụ từ Hermite, Cauchy, Poisson, Kirchhoff, Helmholtz, Kelvin và Heaviside. Ký hiệu $\\delta(x)$ do G. Kirchhoff dùng đầu tiên, rồi Dirac đưa vào cơ học lượng tử năm 1927 (tr. 74).||"
                 "The idea has been current for a century or more in mathematical circles: van der Pol and Bremmer (1955) cite examples from Hermite, Cauchy, Poisson, Kirchhoff, Helmholtz, Kelvin and Heaviside. The notation $\\delta(x)$ was first used by G. Kirchhoff and introduced into quantum mechanics by Dirac in 1927 (p. 74).⟧</p>"),
                ("⟦Những thứ không tồn tại nhưng hữu ích||Things that do not exist but are useful⟧",
                 "<p>⟦Khối điểm, điện tích điểm, nguồn điểm, lực tập trung, nguồn đường, điện tích mặt là các thực thể quen thuộc trong vật lý, dù không tồn tại. Giá trị khái niệm của chúng nằm ở chỗ đáp ứng xung (tác dụng gắn với xung) có thể không phân biệt được, với thiết bị đo cho trước, so với đáp ứng của một xung có thật (tr. 74).||"
                 "Point masses, point charges, point sources, concentrated forces, line sources and surface charges are familiar and accepted entities in physics, though they do not exist. Their conceptual value stems from the fact that the impulse response, the effect associated with the impulse, may be indistinguishable, given measuring equipment of specified resolving power, from the response due to a physically realisable pulse (p. 74).⟧</p>"),
                ("⟦Định nghĩa: không phải một hàm||Definition: not a function⟧",
                 "<p>⟦Ta muốn viết $\\delta(x)=0$ với $x\\ne0$ và $\\int\\delta=1$, nhưng ký hiệu xung không biểu diễn một hàm theo nghĩa giải tích. Dirac gọi nó là \"hàm không chính thức\" và tích phân ở trên chỉ có nghĩa khi nêu quy ước diễn giải. Ở đây nó nghĩa là giới hạn của $\\int\\tau^{-1}\\Pi(x/\\tau)dx$ khi $\\tau\\to0$ (tr. 74 đến 75).||"
                 "We wish to write $\\delta(x)=0$ for $x\\ne0$ and $\\int\\delta=1$, but the impulse symbol does not represent a function in the sense of analysis. Dirac called it an \"improper function\", and the integral above has no meaning until a convention of interpretation is declared. Here it means the limit of $\\int\\tau^{-1}\\Pi(x/\\tau)dx$ as $\\tau\\to0$ (pp. 74 to 75).⟧</p>"
                 + F("⟦Cách diễn giải||The interpretation⟧", r"\int_{-\infty}^{\infty}\delta(x)\,dx\ \equiv\ \lim_{\tau\to0}\int_{-\infty}^{\infty}\tau^{-1}\Pi\!\left(\frac{x}{\tau}\right)dx=1",
                     [(r"\tau^{-1}\Pi(x/\tau)", "⟦xung chữ nhật cao $\\tau^{-1}$, đáy $\\tau$, diện tích 1||rectangle of height $\\tau^{-1}$, base $\\tau$, unit area⟧")])),
                ("⟦Đáp ứng của mạch lọc RC: dạng xung dần không quan trọng||An RC low-pass circuit: the pulse shape gradually stops mattering⟧",
                 "<p>⟦Cho xung điện áp vào bộ lọc thông thấp, đáp ứng quá độ dần ổn định khi xung ngắn dần, và khi đó không phụ thuộc dạng xung vào, vì thành phần tần số cao phân biệt các xung gần như không gây đáp ứng (tr. 75). Với mạch RC có $h(t)=e^{-t}H(t)$, ba xung diện tích 1 (chữ nhật, tam giác, hai xung nhỏ) rộng $\\tau$: tại $t=1$ độ chênh giữa ba đáp ứng là {{spread_05}} khi $\\tau=0.5$, {{spread_01}} khi $\\tau=0.1$ và {{spread_001}} khi $\\tau=0.01$.||"
                 "Feed voltage pulses into a low-pass filter: the transient response settles to a definite form as the pulses shorten, independent of the input pulse shape, because the high-frequency components that distinguish the pulses produce negligible response (p. 75). For an RC circuit with $h(t)=e^{-t}H(t)$ and three unit-area pulses (rectangle, triangle, two small pulses) of width $\\tau$: at $t=1$ the spread among the three responses is {{spread_05}} for $\\tau=0.5$, {{spread_01}} for $\\tau=0.1$ and {{spread_001}} for $\\tau=0.01$.⟧</p>{{fig:rc_pulses}}"),
                ("⟦Mối liên hệ giữa $\\delta$ và bậc thang||The relation between $\\delta$ and the step⟧",
                 "<p>⟦Vì $\\int_{-\\infty}^x\\delta(x')dx'$ bằng 1 khi $x>0$ và 0 khi $x<0$, ta có $\\int_{-\\infty}^x\\delta=H(x)$. Để hiểu đúng, thay $\\delta$ bằng dãy $\\tau^{-1}\\Pi(x/\\tau)$: các tích phân là hàm dốc-bậc thang (hình 5.1), rồi cố định $x$ và cho $\\tau\\to0$ (tr. 75 đến 77). Tại $x=0.1$: $\\tau=0.5$ cho {{step_x01_t05}}, $\\tau=0.1$ cho {{step_x01_t01}}; tại $x=-0.1$: {{step_xm01_t05}} và {{step_xm01_t01}}.||"
                 "Since $\\int_{-\\infty}^x\\delta(x')dx'$ is 1 for $x>0$ and 0 for $x<0$, we have $\\int_{-\\infty}^x\\delta=H(x)$. To interpret it, replace $\\delta$ by the sequence $\\tau^{-1}\\Pi(x/\\tau)$: the integrals are ramp-step functions (Fig. 5.1); fix $x$ and let $\\tau\\to0$ (pp. 75 to 77). At $x=0.1$: $\\tau=0.5$ gives {{step_x01_t05}}, $\\tau=0.1$ gives {{step_x01_t01}}; at $x=-0.1$: {{step_xm01_t05}} and {{step_xm01_t01}}.⟧</p>"
                 + F("⟦Đạo hàm của bậc thang||Derivative of the step⟧", r"\int_{-\infty}^{x}\delta(x')\,dx'=H(x),\qquad \delta(x)=\frac{d}{dx}H(x)")),
                ("⟦\"Đạo hàm của bậc thang là xung\" nghĩa là gì||What \"the derivative of the step is the impulse\" means⟧",
                 "<p>⟦Bậc thang không có đạo hàm tại gốc, nên phát biểu này là dấu tắt cho: đạo hàm của một dãy hàm khả vi tiến về $H(x)$ là một dãy xác định phù hợp cho $\\delta(x)$. Các hàm dốc-bậc thang của hình 5.1 khả vi và tiến về $H$; bước nhảy luôn bằng 1 nên diện tích dưới mỗi đạo hàm bằng 1, đủ điều kiện làm dãy xung đơn vị (tr. 77).||"
                 "The step has no derivative at the origin, so the statement is shorthand for: the derivatives of a sequence of differentiable functions approaching $H(x)$ constitute a suitable defining sequence for $\\delta(x)$. The ramp-step functions of Fig. 5.1 are differentiable and approach $H$; since the step is always 1 the area under each derivative is 1, qualifying it as a unit-impulse sequence (p. 77).⟧</p>"),
                ("⟦Nhiều dãy khác nhau xác định cùng một $\\delta$||Many different sequences define the same $\\delta$⟧",
                 "<p>⟦Bracewell liệt kê các dãy tiến về 0 qua giá trị dương của $\\tau$ (tr. 77 đến 78): xung chữ nhật đặt lệch (cạnh trái tại gốc, hay dùng trong mạch điện có công tắc), Gauss (mọi đạo hàm đều tồn tại), tam giác (liên tục, bằng 0 ngoài $|x|<\\tau$), $\\tau^{-1}\\text{sinc}(x/\\tau)$ (không tắt dần nhưng vẫn dùng được), đường cộng hưởng $\\tau/[\\pi(x^2+\\tau^2)]$ (tắt chậm), và hàm trơn có giá compact. Bảng sau cho $\\int f\\,\\delta_\\tau\\,dx$ với $f=\\cos x+\\tfrac12\\sin2x$ (nên $f(0)=1$):||"
                 "Bracewell lists sequences as $\\tau$ approaches zero through positive values (pp. 77 to 78): a displaced rectangle (left edge at the origin, common in switched circuits), the Gaussian (derivatives of all orders exist), the triangle (continuous, zero outside $|x|<\\tau$), $\\tau^{-1}\\text{sinc}(x/\\tau)$ (does not die out yet serves), the resonance profile $\\tau/[\\pi(x^2+\\tau^2)]$ (decays slowly), and a smooth compactly supported bump. The table gives $\\int f\\,\\delta_\\tau\\,dx$ with $f=\\cos x+\\tfrac12\\sin2x$ (so $f(0)=1$):⟧</p>"
                 + TBL(["⟦Dạng xung||Pulse shape⟧", "$\\tau=0.1$", "$\\tau=0.01$"],
                       [["⟦chữ nhật đặt giữa||centred rectangle⟧", "{{sift_rc_01}}", "{{sift_rc_001}}"], ["⟦chữ nhật cạnh trái tại gốc||left-edge rectangle⟧", "{{sift_rl_01}}", "{{sift_rl_001}}"],
                        ["Gauss", "{{sift_g_01}}", "{{sift_g_001}}"], ["⟦tam giác||triangle⟧", "{{sift_t_01}}", "{{sift_t_001}}"], ["sinc", "{{sift_s_01}}", "{{sift_s_001}}"],
                        ["⟦Lorentz (cộng hưởng)||Lorentzian (resonance)⟧", "{{sift_l_01}}", "{{sift_l_001}}"]])
                 + "<p>⟦Mọi dạng đối xứng đều tiến về 1; dạng cạnh trái tiến về $f(0+)$ ở chỗ gián đoạn nên hơi khác khi $\\tau$ chưa nhỏ.||All symmetric shapes tend to 1; the left-edge shape tends to $f(0+)$ at a discontinuity so it differs a little until $\\tau$ is small.⟧</p>"),
                ("⟦Tự kiểm tra phần 1||Self-check, part 1⟧",
                 UL(["⟦Vì sao mạch RC không phân biệt được các xung vào rất ngắn có dạng khác nhau?||Why can an RC circuit not tell very brief input pulses of different shapes apart?⟧",
                     "⟦Vì sao \"đạo hàm của bậc thang là xung\" chỉ là dấu tắt?||Why is \"the derivative of the step is the impulse\" only shorthand?⟧",
                     "⟦Dãy nào trong bảng trên tiến về giá trị khác 1 khi $\\tau$ chưa nhỏ, và vì sao?||Which sequence in the table above differs from 1 while $\\tau$ is not small, and why?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: vì thành phần tần số cao gần như không gây đáp ứng; vì bậc thang không có đạo hàm tại gốc; dạng chữ nhật cạnh trái, vì nó sàng $f$ tại lân cận bên phải.||Hints: because high-frequency components produce almost no response; because the step has no derivative at the origin; the left-edge rectangle, because it sifts $f$ from just to the right.⟧</p>"),
            ]),
        # ---------------------------------------------------------------- PART 2
        dict(
            title="⟦Tính chất sàng, tỉ lệ và chuỗi shah||Sifting, scaling and the shah train⟧",
            scr=("⟦Muốn tính với $\\delta$ như với một hàm bình thường, ta cần các quy tắc chính xác.||To compute with $\\delta$ like an ordinary function we need exact rules.⟧",
                 "⟦Vài quy tắc trông hiển nhiên lại có bẫy: $\\delta(ax)$, $x\\delta(x)$, $\\text{III}(ax)$.||A few seemingly obvious rules have traps: $\\delta(ax)$, $x\\delta(x)$, $\\text{III}(ax)$.⟧",
                 "⟦Tính chất sàng là quy tắc trung tâm, và shah nhân rộng nó ra một chuỗi xung đều.||Sifting is the central rule and shah extends it to a regular train of impulses.⟧"),
            preview=["⟦Tính chất sàng và tích chập với $\\delta$||Sifting and convolution with $\\delta$⟧", "⟦Tỉ lệ $\\delta(ax)$ và $x\\delta(x)=0$ có điều kiện||Scaling $\\delta(ax)$ and the qualified $x\\delta(x)=0$⟧", "⟦Chuỗi xung shah: lấy mẫu và nhân bản||The shah train: sampling and replication⟧"],
            slides=[
                ("⟦Tính chất sàng||The sifting property⟧",
                 "<p>⟦Thay $\\delta$ bằng $\\tau^{-1}\\Pi(x/\\tau)$, nhân với $f$, lấy tích phân rồi cho $\\tau\\to0$: diện tích phía dưới xấp xỉ $\\tau^{-1}$ nhân phần bóng, vốn cao trung bình gần $f(0)$ và rộng $\\tau$, nên tiến về $f(0)$. Phép toán \"sàng\" ra một giá trị duy nhất của $f$. Dạng xung không quan trọng, chỉ tích phân có ý nghĩa (tr. 79).||"
                 "Replace $\\delta$ by $\\tau^{-1}\\Pi(x/\\tau)$, multiply by $f$, integrate and let $\\tau\\to0$: the area is about $\\tau^{-1}$ times the shaded part, whose average height is near $f(0)$ and width $\\tau$, so it tends to $f(0)$. The operation \"sifts\" out a single value of $f$. The pulse shape does not matter, only its integral counts (p. 79).⟧</p>"
                 + F("⟦Tính chất sàng||Sifting property⟧", r"\int_{-\infty}^{\infty}\delta(x)f(x)\,dx=f(0),\qquad \int_{-\infty}^{\infty}\delta(x-a)f(x)\,dx=f(a)")),
                ("⟦Tích chập với $\\delta$ không đổi gì||Convolution with $\\delta$ changes nothing⟧",
                 "<p>⟦Viết dưới dạng tích chập, $\\delta(x)*f(x)=f(x)*\\delta(x)=f(x)$. Nếu $f$ có bước nhảy tại $x=0$, tích phân sàng có giá trị giới hạn $\\tfrac12[f(0+)+f(0-)]$, nên tổng quát hơn ta viết $\\delta*f=\\tfrac12[f(x+)+f(x-)]$; khác $f$ chỉ bởi hàm rỗng (tr. 80). Số đo với $f=e^{-x}H(x)$: dãy đặt giữa cho {{jump_mid}}, dãy cạnh trái cho {{jump_left}} tại chỗ nhảy.||"
                 "Written as a convolution, $\\delta(x)*f(x)=f(x)*\\delta(x)=f(x)$. If $f$ has a jump at $x=0$ the sifting integral has limiting value $\\tfrac12[f(0+)+f(0-)]$, so more generally $\\delta*f=\\tfrac12[f(x+)+f(x-)]$; it differs from $f$ only by a null function (p. 80). Measured with $f=e^{-x}H(x)$: the centred sequence gives {{jump_mid}}, the left-edge sequence gives {{jump_left}} at the jump.⟧</p>"
                 + F("⟦Tích chập với xung||Convolution with the impulse⟧", r"\delta*f=f*\delta=\tfrac12\left[f(x^+)+f(x^-)\right]")),
                ("⟦Dãy cạnh trái sàng $f(x+)$||The left-edge sequence sifts $f(x+)$⟧",
                 "<p>⟦Dãy chữ nhật không đối xứng $\\tau^{-1}\\Pi[(x-\\tau/2)/\\tau]$ có tính chất sàng ra $f(x+)$. Tại điểm gián đoạn, dùng dãy này cho kết quả khác. Trong phân tích quá độ, nơi gián đoạn ở thời điểm đóng công tắc $t=0$ rất phổ biến, việc chọn dãy có vẻ cho đáp số khác, nhưng khác biệt chỉ tức thời (tr. 80).||"
                 "The asymmetric rectangular sequence $\\tau^{-1}\\Pi[(x-\\tau/2)/\\tau]$ sifts out $f(x+)$. At points of discontinuity this sequence gives a different result. In transient analysis, where discontinuities at the switching instant $t=0$ are particularly common, the choice of sequence can appear to give different answers, but the difference can only be instantaneous (p. 80).⟧</p>"),
                ("⟦Tỉ lệ: $\\delta(ax)=|a|^{-1}\\delta(x)$||Scaling: $\\delta(ax)=|a|^{-1}\\delta(x)$⟧",
                 "<p>⟦Nén thang $x$ đi $a$ lần làm diện tích của các xung vốn bằng 1 giảm đi, nên cường độ xung giảm $|a|$ lần. Dấu môđun bao hàm tính chất $\\delta(-x)=\\delta(x)$ (tr. 80). Số đo: $\\int f\\,\\tau^{-1}\\Pi(3x/\\tau)dx$ với $\\tau=0.01$ bằng {{scale_3}}, gần $f(0)/3$.||"
                 "Compressing the scale of $x$ by $a$ reduces the area of pulses that previously had unit area, so the strength of the impulse is reduced by $|a|$. The modulus allows for $\\delta(-x)=\\delta(x)$ (p. 80). Measured: $\\int f\\,\\tau^{-1}\\Pi(3x/\\tau)dx$ with $\\tau=0.01$ equals {{scale_3}}, close to $f(0)/3$.⟧</p>"
                 + F("⟦Tỉ lệ||Scaling⟧", r"\delta(ax)=\frac{1}{|a|}\,\delta(x),\qquad \delta(-x)=\delta(x)")),
                ("⟦Nhân với hàm liên tục: $f(x)\\delta(x)=f(0)\\delta(x)$||Multiplying by a continuous function: $f(x)\\delta(x)=f(0)\\delta(x)$⟧",
                 "<p>⟦Nếu $f$ liên tục tại 0 thì $f(x)\\delta(x)=f(0)\\delta(x)$ (tr. 81). Kiểm số: kiểm bằng hàm thử $g=e^{-x^2}$ và dãy Gauss $\\tau=0.01$, $\\int f\\delta_\\tau g\\,dx$ = {{fg_sift}}, đúng $f(0)g(0)=1$.||"
                 "If $f$ is continuous at 0 then $f(x)\\delta(x)=f(0)\\delta(x)$ (p. 81). Numerical check with the test function $g=e^{-x^2}$ and a Gaussian sequence $\\tau=0.01$: $\\int f\\delta_\\tau g\\,dx$ = {{fg_sift}}, exactly $f(0)g(0)=1$.⟧</p>"),
                ("⟦$x\\delta(x)=0$: đúng, nhưng có điều kiện||$x\\delta(x)=0$: true, but qualified⟧",
                 "<p>⟦Từ tính chất sàng với $f=x$, $\\int x\\delta(x)dx=0$, và người ta viết $x\\delta(x)=0$. Nhưng nhìn các hàm trước giới hạn, phương trình này che giấu một thành phần khác không gợi nhớ hiện tượng Gibbs: $\\lim_{\\tau\\to0}[x\\tau^{-1}\\Pi(x/\\tau)]=0$ với mọi $x$, nhưng cực đại của nó luôn là $\\tfrac12$ và cực tiểu $-\\tfrac12$ (tr. 81). Đo: cực đại {{xd_max}} với $\\tau=0.1$ lẫn $\\tau=0.001$.||"
                 "From sifting with $f=x$, $\\int x\\delta(x)dx=0$, and one writes $x\\delta(x)=0$. But contemplating the prelimit graphs, this equation conceals a nonvanishing component reminiscent of the Gibbs phenomenon: $\\lim_{\\tau\\to0}[x\\tau^{-1}\\Pi(x/\\tau)]=0$ for all $x$, yet its maximum is always $\\tfrac12$ and its minimum $-\\tfrac12$ (p. 81). Measured: maximum {{xd_max}} for both $\\tau=0.1$ and $\\tau=0.001$.⟧</p>"),
                ("⟦Chuỗi xung shah $\\text{III}(x)$||The shah impulse train $\\text{III}(x)$⟧",
                 "<p>⟦Chuỗi vô hạn các xung đơn vị cách nhau 1 (hình 5.4). Mọi dè dặt của $\\delta$ đều áp dụng, và nhiều hơn: vô số gián đoạn vô hạn và tích phân vô hạn không hội tụ, nên mọi điều kiện tồn tại biến đổi Fourier đều bị vi phạm; nhưng nó lại rất hữu ích và dễ thao tác (tr. 81 đến 82). Các tính chất hiển nhiên: tuần hoàn chu kỳ 1, chẵn, $\\text{III}(x-\\tfrac12)=\\text{III}(x+\\tfrac12)$.||"
                 "An infinite sequence of unit impulses spaced by 1 (Fig. 5.4). Every reservation about $\\delta$ applies, and more: infinitely many infinite discontinuities and a nonconvergent infinite integral, so all conditions for a Fourier transform are violated; yet it is extremely useful and easy to manipulate (pp. 81 to 82). Obvious properties: period 1, even, $\\text{III}(x-\\tfrac12)=\\text{III}(x+\\tfrac12)$.⟧</p>"
                 + F("⟦Shah||Shah⟧", r"\text{III}(x)=\sum_{n=-\infty}^{\infty}\delta(x-n),\qquad \text{III}(-x)=\text{III}(x),\qquad \text{III}(x+n)=\text{III}(x)")),
                ("⟦Lấy mẫu: nhân với shah||Sampling: multiplying by shah⟧",
                 "<p>⟦Nhân $f(x)$ với $\\text{III}(x)$ lấy mẫu $f$ ở các khoảng đơn vị: $\\text{III}(x)f(x)=\\sum f(n)\\delta(x-n)$. Thông tin trong các khoảng giữa các số nguyên bị mất, nhưng giá trị tại số nguyên được giữ. Shah dùng cho giản đồ bức xạ dàn ăng-ten, nhiễu xạ cách tử, quét raster trong tivi và radar, điều chế xung, lấy mẫu dữ liệu, chuỗi Fourier và bảng số (tr. 82). Tổng mẫu $\\sum_nf(n)$ với $f=e^{-\\pi x^2}$ là {{X_sum_1}}.||"
                 "Multiplying $f(x)$ by $\\text{III}(x)$ samples it at unit intervals: $\\text{III}(x)f(x)=\\sum f(n)\\delta(x-n)$. The information between the integers is lost but the values at integers are preserved. Shah serves antenna-array patterns, diffraction gratings, raster scanning in television and radar, pulse modulation, data sampling, Fourier series and tabular computing (p. 82). The sum of samples $\\sum_nf(n)$ for $f=e^{-\\pi x^2}$ is {{X_sum_1}}.⟧</p>"
                 + F("⟦Lấy mẫu||Sampling⟧", r"\text{III}(x)\,f(x)=\sum_{n=-\infty}^{\infty}f(n)\,\delta(x-n)")),
                ("⟦Nhân bản: tích chập với shah||Replication: convolving with shah⟧",
                 "<p>⟦$\\text{III}*f=\\sum f(x-n)$: hàm $f$ xuất hiện lặp lại (bản sao) ở các khoảng đơn vị về cả hai phía; nếu $f$ rộng hơn một đơn vị thì các bản sao chồng lấn (hình 5.6). Tính hai mặt (lấy mẫu và tuần hoàn) không phải ngẫu nhiên: $\\text{III}$ là biến đổi Fourier của chính nó (trong giới hạn), nên hữu ích gấp đôi (tr. 82 đến 83). Với $f=e^{-\\pi x^2}$, $(\\text{III}*f)(0.5)$ = {{rep_05}}, tính bằng tổng trực tiếp và bằng chuỗi Fourier $\\sum(-1)^ke^{-\\pi k^2}$ đều ra cùng số.||"
                 "$\\text{III}*f=\\sum f(x-n)$: $f$ appears in replica at unit intervals on both sides; if $f$ is more than one unit wide the replicas overlap (Fig. 5.6). This twofold character is no accident: $\\text{III}$ is its own Fourier transform (in the limit), making it twice as useful (pp. 82 to 83). For $f=e^{-\\pi x^2}$, $(\\text{III}*f)(0.5)$ = {{rep_05}}, computed both by the direct sum and by the Fourier series $\\sum(-1)^ke^{-\\pi k^2}$.⟧</p>"
                 + F("⟦Nhân bản||Replication⟧", r"\text{III}*f(x)=\sum_{n=-\infty}^{\infty}f(x-n)")),
                ("⟦Cái bẫy $\\text{III}(ax)$: cường độ xung||The $\\text{III}(ax)$ trap: impulse strength⟧",
                 "<p>⟦Nén shah theo $x$ hai lần thành $\\text{III}(2x)$ làm các xung sát gấp đôi, nhưng để nhất quán đại số, cường độ giảm cùng hệ số: $\\text{III}(ax)=|a|^{-1}\\sum\\delta(x-n/a)$. Nếu kéo giãn để khoảng cách là $X$ thì $\\text{III}(x/X)$ chưa có cường độ đơn vị: xung đơn vị cách nhau $X$ là $X^{-1}\\text{III}(x/X)$ (tr. 83). Số đo với $f=e^{-\\pi x^2}$ (diện tích 1): $\\sum f(nX)$ = {{X_sum_1}} ($X=1$) và {{X_sum_05}} ($X=0.5$, gấp đôi vì thiếu hệ số $X$), còn $X\\sum f(nX)$ = {{X_riem_05}} ($X=0.5$), đúng diện tích.||"
                 "Squeezing shah by 2 into $\\text{III}(2x)$ packs the impulses twice as closely, but for algebraic consistency their strength drops by the same factor: $\\text{III}(ax)=|a|^{-1}\\sum\\delta(x-n/a)$. If it is stretched so that the spacing is $X$ then $\\text{III}(x/X)$ does not have unit strength: unit impulses spaced $X$ are $X^{-1}\\text{III}(x/X)$ (p. 83). Measured with $f=e^{-\\pi x^2}$ (area 1): $\\sum f(nX)$ = {{X_sum_1}} ($X=1$) and {{X_sum_05}} ($X=0.5$, twice too large because the factor $X$ is missing), while $X\\sum f(nX)$ = {{X_riem_05}} ($X=0.5$), the area.⟧</p>"
                 + F("⟦Shah khoảng cách $X$||Shah with spacing $X$⟧", r"\text{III}(ax)=\frac1{|a|}\sum_n\delta\!\left(x-\frac na\right),\qquad \text{unit impulses spaced }X:\ X^{-1}\,\text{III}(x/X)")),
                ("⟦Đối ngẫu Poisson: shah tự biến đổi||Poisson duality: shah is self-transforming⟧",
                 "<p>⟦Vì $\\text{III}\\supset\\text{III}$, tổng các mẫu của $f$ bằng tổng các mẫu của $F$: $\\sum f(n)=\\sum F(k)$. Với $f=e^{-\\pi x^2/4}$ có $F=2e^{-4\\pi s^2}$: vế trái {{shah_lhs}} và vế phải {{shah_rhs}}, trùng tới sai số làm tròn. Đây là công thức tổng Poisson mà chương 10 sẽ dùng cho định lý lấy mẫu.||"
                 "Since $\\text{III}\\supset\\text{III}$, the sum of samples of $f$ equals the sum of samples of $F$: $\\sum f(n)=\\sum F(k)$. With $f=e^{-\\pi x^2/4}$ having $F=2e^{-4\\pi s^2}$: the left side is {{shah_lhs}} and the right side {{shah_rhs}}, equal to rounding error. This is the Poisson summation formula chapter 10 will use for the sampling theorem.⟧</p>"
                 + F("⟦Tổng Poisson||Poisson summation⟧", r"\sum_{n=-\infty}^{\infty}f(n)=\sum_{k=-\infty}^{\infty}F(k)")),
                ("⟦Tự kiểm tra phần 2||Self-check, part 2⟧",
                 UL(["⟦Vì sao $x\\delta(x)=0$ vẫn để lại một cực đại $\\tfrac12$ trước giới hạn?||Why does $x\\delta(x)=0$ still leave a maximum of $\\tfrac12$ before the limit?⟧",
                     "⟦Xung đơn vị cách nhau $X$ biểu diễn thế nào?||How are unit impulses spaced $X$ represented?⟧",
                     "⟦Vì sao $\\text{III}$ vừa lấy mẫu vừa nhân bản?||Why does $\\text{III}$ both sample and replicate?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: vì $x\\tau^{-1}\\Pi(x/\\tau)$ cao $\\tfrac12$ tại mép; $X^{-1}\\text{III}(x/X)$; vì nó tự biến đổi.||Hints: because $x\\tau^{-1}\\Pi(x/\\tau)$ reaches $\\tfrac12$ at the edge; $X^{-1}\\text{III}(x/X)$; because it is self-transforming.⟧</p>"),
            ]),
        # ---------------------------------------------------------------- PART 3
        dict(
            title="⟦Cặp xung chẵn, lẻ và đạo hàm của $\\delta$||Even and odd impulse pairs and derivatives of $\\delta$⟧",
            scr=("⟦Cosin và sin cần các cặp xung làm biến đổi, còn dipole và tứ cực cần đạo hàm của xung.||Cosine and sine need impulse pairs as transforms, and dipoles and quadrupoles need derivatives of the impulse.⟧",
                 "⟦Ta không thể bắt một hàm vọt lên vô cùng bên trái gốc và xuống âm vô cùng bên phải.||We cannot ask a function to go infinite just left of the origin and negatively infinite just right of it.⟧",
                 "⟦Dùng dãy đạo hàm của các xung trơn, và đọc tính chất sàng đạo hàm bằng tích phân từng phần.||Use derivatives of smooth pulse sequences and read derivative-sifting by integration by parts.⟧"),
            preview=["⟦Cặp xung chẵn và lẻ, sai phân||The even and odd pairs, finite differences⟧", "⟦$\\delta'$, $\\delta''$ và các tích phân đặc trưng||$\\delta'$, $\\delta''$ and their characteristic integrals⟧", "⟦Hàm rỗng||Null functions⟧"],
            slides=[
                ("⟦Cặp xung chẵn và cặp xung lẻ||The even and odd impulse pairs⟧",
                 "<p>⟦Bracewell định nghĩa (hình 5.7, ký hiệu riêng ở bảng 4.1; ở đây viết $\\mu$ và $\\nu$):||Bracewell defines (Fig. 5.7, special symbols in Table 4.1; written here as $\\mu$ and $\\nu$):⟧</p>"
                 + F("⟦Cặp chẵn và lẻ||Even and odd pairs⟧", r"\mu(x)=\tfrac12\delta\!\left(x+\tfrac12\right)+\tfrac12\delta\!\left(x-\tfrac12\right),\qquad \nu(x)=\tfrac12\delta\!\left(x+\tfrac12\right)-\tfrac12\delta\!\left(x-\tfrac12\right)")
                 + "<p>⟦Chúng quan trọng vì liên hệ biến đổi với cosin và sin: $\\mu(x)\\supset\\cos\\pi s$, $\\cos\\pi x\\supset\\mu(s)$, và $\\nu(x)\\supset i\\sin\\pi s$, $\\sin\\pi x\\supset i\\nu(s)$ (tr. 84). Notebook: biến đổi số của $\\mu$ tại $s=0.3$ là {{mu_ft}}, đúng $\\cos0.3\\pi$.||They matter because of their transform relation to cosine and sine: $\\mu(x)\\supset\\cos\\pi s$, $\\cos\\pi x\\supset\\mu(s)$, and $\\nu(x)\\supset i\\sin\\pi s$, $\\sin\\pi x\\supset i\\nu(s)$ (p. 84). Notebook: the numerical transform of $\\mu$ at $s=0.3$ is {{mu_ft}}, exactly $\\cos0.3\\pi$.⟧</p>"),
                ("⟦Cặp chẵn nhân đôi hàm||The even pair duplicates a function⟧",
                 "<p>⟦Tích chập với $\\mu$ cho $\\mu*f=\\tfrac12f(x+\\tfrac12)+\\tfrac12f(x-\\tfrac12)$, tức trung bình hai bản dịch (hình 5.8). Chuẩn hóa để diện tích bằng 1 có lợi thế; đôi khi người ta muốn hai xung đơn vị (tr. 84). Với $f=e^{-\\pi x^2}$ tại $x=0$: {{mu_conv}}.||"
                 "Convolving with $\\mu$ gives $\\mu*f=\\tfrac12f(x+\\tfrac12)+\\tfrac12f(x-\\tfrac12)$, the mean of two displaced copies (Fig. 5.8). Normalising to unit area has advantages; occasionally two unit impulses would be preferable (p. 84). With $f=e^{-\\pi x^2}$ at $x=0$: {{mu_conv}}.⟧</p>"),
                ("⟦Sai phân hữu hạn bằng cặp lẻ||Finite difference through the odd pair⟧",
                 "<p>⟦Định nghĩa sai phân hữu hạn $\\Delta f(x)=f(x+\\tfrac12)-f(x-\\tfrac12)$, ta có $\\Delta f=2\\nu*f$, tức toán tử $\\Delta=2\\nu*$ (tr. 84 đến 85). Kiểm số: với $f=\\sin x$, $\\Delta f(0)=2\\sin\\tfrac12$ = {{fd_0}}; với $f=e^{-\\pi x^2}$, biến đổi của $\\Delta f$ là $2i\\sin(\\pi s)F(s)$, độ lớn {{fd_ft}} tại $s=0.3$ bằng cả tích phân số lẫn công thức.||"
                 "Defining the finite difference $\\Delta f(x)=f(x+\\tfrac12)-f(x-\\tfrac12)$ we have $\\Delta f=2\\nu*f$, i.e. the operator $\\Delta=2\\nu*$ (pp. 84 to 85). Numerical check: for $f=\\sin x$, $\\Delta f(0)=2\\sin\\tfrac12$ = {{fd_0}}; for $f=e^{-\\pi x^2}$ the transform of $\\Delta f$ is $2i\\sin(\\pi s)F(s)$, of magnitude {{fd_ft}} at $s=0.3$ by both numerical integration and the formula.⟧</p>"
                 + F("⟦Sai phân||Finite difference⟧", r"\Delta f(x)=f\!\left(x+\tfrac12\right)-f\!\left(x-\tfrac12\right)=2\,\nu(x)*f(x)")),
                ("⟦Đạo hàm thứ nhất $\\delta'(x)$: dipole||The first derivative $\\delta'(x)$: the dipole⟧",
                 "<p>⟦$\\delta'(x)=\\frac{d}{dx}\\delta(x)$ gợi hình ảnh một lưỡng cực vô cùng nhỏ trong tĩnh điện, một hình ảnh quen thuộc và dễ dùng. Cách viết $\\delta'$ chuyển sự dễ dàng đó sang toán, nhưng ta không thể bắt một hàm vọt lên vô cùng ngay trái gốc, xuống âm vô cùng ngay phải, và bằng 0 ở mọi chỗ khác. Ta cũng muốn viết $\\delta'(0)=0$ (tr. 85).||"
                 "$\\delta'(x)=\\frac{d}{dx}\\delta(x)$ evokes an infinitesimal dipole in electrostatics, a familiar and easy picture. The notation $\\delta'$ carries that facility into mathematics, but we cannot ask a function to go positively infinite just left of the origin, negatively infinite just right, and zero everywhere else. We would also wish to write $\\delta'(0)=0$ (p. 85).⟧</p>"),
                ("⟦Diễn giải chặt chẽ: đạo hàm của dãy xung||Rigorous reading: derivatives of a pulse sequence⟧",
                 "<p>⟦Ta lui về dãy xung như với $\\delta$ và xét các đạo hàm của chúng (hình 5.9). Ví dụ $\\int\\delta'(x)dx=0$ là dấu tắt của $\\lim\\int[\\text{đạo hàm của xung}]dx=0$. Hình dạng xung chính xác không quan trọng, thậm chí xung chữ nhật cũng được, nhưng trong công việc sau, xung trơn có thể có lợi (tr. 85 đến 86). Tính chất sàng đạo hàm: $\\int\\delta'(x)f(x)dx=-f'(0)$; với dãy Gauss $\\tau=0.05$ và $f=\\cos x+\\tfrac12\\sin2x$ cho {{dprime_sift}}, trùng $-\\int\\delta_\\tau f'$ (lệch {{ibp_diff}}).||"
                 "We fall back on pulse sequences as for $\\delta$ and consider their derivatives (Fig. 5.9). For example $\\int\\delta'(x)dx=0$ is shorthand for $\\lim\\int[\\text{derivative of the pulse}]dx=0$. The exact pulse form is unimportant, even a rectangle will do, but in later work a smooth pulse may offer an advantage (pp. 85 to 86). Derivative sifting: $\\int\\delta'(x)f(x)dx=-f'(0)$; with the Gaussian sequence $\\tau=0.05$ and $f=\\cos x+\\tfrac12\\sin2x$ it gives {{dprime_sift}}, equal to $-\\int\\delta_\\tau f'$ (difference {{ibp_diff}}).⟧</p>"
                 + F("⟦Sàng đạo hàm||Derivative sifting⟧", r"\int_{-\infty}^{\infty}\delta'(x)\,f(x)\,dx=-f'(0)")),
                ("⟦Tính chất của $\\delta'$||Properties of $\\delta'$⟧",
                 "<p>⟦Các tính chất đi kèm (tr. 86): $\\int x\\delta'(x)dx=-1$, $\\int|\\delta'(x)|dx=\\infty$, $\\delta'(-x)=-\\delta'(x)$, $x\\delta'(x)=-\\delta(x)$, và $f(x)\\delta'(x)=f(0)\\delta'(x)-f'(0)\\delta(x)$. Số đo: $\\int x\\delta'_\\tau dx$ = {{x_dprime}}; $\\int|\\delta'_\\tau|dx$ = {{l1_01}} khi $\\tau=0.1$ và {{l1_001}} khi $\\tau=0.01$, tăng như $2/\\tau$: không có giới hạn hữu hạn.||"
                 "The accompanying properties (p. 86): $\\int x\\delta'(x)dx=-1$, $\\int|\\delta'(x)|dx=\\infty$, $\\delta'(-x)=-\\delta'(x)$, $x\\delta'(x)=-\\delta(x)$, and $f(x)\\delta'(x)=f(0)\\delta'(x)-f'(0)\\delta(x)$. Measured: $\\int x\\delta'_\\tau dx$ = {{x_dprime}}; $\\int|\\delta'_\\tau|dx$ = {{l1_01}} for $\\tau=0.1$ and {{l1_001}} for $\\tau=0.01$, growing like $2/\\tau$: no finite limit.⟧</p>"
                 + F("⟦Vài hệ thức||A few relations⟧", r"x\,\delta'(x)=-\delta(x),\qquad f(x)\,\delta'(x)=f(0)\,\delta'(x)-f'(0)\,\delta(x)")),
                ("⟦Đạo hàm bậc cao||Higher derivatives⟧",
                 "<p>⟦Với đạo hàm cấp cao (tr. 87): $\\int\\delta''(x)dx=0$, $\\int x^2\\delta''(x)dx=2$, $x^n\\delta^{(n)}(x)=(-1)^nn!\\,\\delta(x)$, và $\\int\\delta^{(n)}(x)f(x)dx=(-1)^nf^{(n)}(0)$. Số đo: $\\int x^2\\delta''_\\tau dx$ = {{x2_d2}}; với $f=\\cos x+\\tfrac12\\sin2x$, $\\int\\delta''f$ = {{d2_sift}}, đúng $f''(0)=-1$.||"
                 "For higher-order derivatives (p. 87): $\\int\\delta''(x)dx=0$, $\\int x^2\\delta''(x)dx=2$, $x^n\\delta^{(n)}(x)=(-1)^nn!\\,\\delta(x)$, and $\\int\\delta^{(n)}(x)f(x)dx=(-1)^nf^{(n)}(0)$. Measured: $\\int x^2\\delta''_\\tau dx$ = {{x2_d2}}; with $f=\\cos x+\\tfrac12\\sin2x$, $\\int\\delta''f$ = {{d2_sift}}, exactly $f''(0)=-1$.⟧</p>"
                 + F("⟦Sàng đạo hàm bậc $n$||$n$-th derivative sifting⟧", r"\int\delta^{(n)}(x)\,f(x)\,dx=(-1)^n f^{(n)}(0)")),
                ("⟦Hàm rỗng||Null functions⟧",
                 "<p>⟦Hàm rỗng nổi tiếng vì biến đổi Fourier bằng 0 mà bản thân không đồng nhất bằng 0. Định nghĩa: $f$ rỗng nếu $\\int_a^bf\\,dx=0$ với mọi $a,b$. Định lý Lerch: nếu hai hàm có cùng biến đổi thì hiệu của chúng là hàm rỗng. Ví dụ là $\\delta^{\\circ}(x)$, bằng 0 khi $x\\ne0$ và 1 khi $x=0$; nó mô tả dòng điện qua điện trở nối tiếp tụ điện từ một acquy khi điện dung tiến về 0 (tr. 87). Số đo: diện tích của một điểm cao 1 trên lưới bước $10^{-3}$ và $10^{-6}$ là {{null_1}} và {{null_2}}, tiến về 0.||"
                 "Null functions are known chiefly for having Fourier transforms that are zero while not themselves identically zero. By definition $f$ is null if $\\int_a^bf\\,dx=0$ for all $a,b$. Lerch's theorem: if two functions have the same transform then their difference is a null function. An example is $\\delta^{\\circ}(x)$, 0 for $x\\ne0$ and 1 at $x=0$; it describes the current taken by a series combination of a resistance and a capacitance from a battery, as the capacitance approaches zero (p. 87). Measured: the area of a single point of height 1 on a grid of step $10^{-3}$ and $10^{-6}$ is {{null_1}} and {{null_2}}, tending to 0.⟧</p>"
                 + F("⟦Bậc thang và hàm rỗng||Step and null function⟧", r"H(x)=\hat H(x)+\tfrac12\,\delta^{\circ}(x)")),
                ("⟦Tự kiểm tra phần 3||Self-check, part 3⟧",
                 UL(["⟦Tính $\\int\\delta'(x)\\cos x\\,dx$ và $\\int\\delta''(x)\\cos x\\,dx$.||Compute $\\int\\delta'(x)\\cos x\\,dx$ and $\\int\\delta''(x)\\cos x\\,dx$.⟧",
                     "⟦Vì sao $\\int|\\delta'|=\\infty$ dù $\\int\\delta'=0$?||Why is $\\int|\\delta'|=\\infty$ although $\\int\\delta'=0$?⟧",
                     "⟦Hàm rỗng có biến đổi Fourier là gì?||What is the Fourier transform of a null function?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: 0 và $-1$; vì hai nửa dương và âm đều dài vô hạn theo $1/\\tau$; bằng 0.||Hints: 0 and $-1$; because the positive and negative halves each grow like $1/\\tau$; zero.⟧</p>"),
            ]),
        # ---------------------------------------------------------------- PART 4
        dict(
            title="⟦Xung nhiều chiều||Multidimensional impulses⟧",
            scr=("⟦Vật lý cần khối lượng điểm trên mặt phẳng, điện tích điểm trong không gian, dàn ăng-ten hai chiều.||Physics needs point masses on a plane, point charges in space and two-dimensional antenna arrays.⟧",
                 "⟦Ký hiệu một chiều có mở rộng tự nhiên không, và giữ được tính tự biến đổi của shah không?||Does the one-dimensional notation extend naturally, and does shah keep its self-transforming property?⟧",
                 "⟦Có: tích của các xung một chiều, và các ký hiệu ghép như \"giường đinh\" $^2\\text{III}$.||Yes: products of one-dimensional impulses and compound symbols such as the \"bed of nails\" $^2\\text{III}$.⟧"),
            preview=["⟦$\\delta(x,y)$ và $\\delta(x,y,z)$||$\\delta(x,y)$ and $\\delta(x,y,z)$⟧", "⟦Giường đinh, hàng đinh và cách tử||The bed of nails, the row of spikes and the grating⟧", "⟦Đạo hàm của xung là dipole, tứ cực||Derivatives of impulses as dipoles and quadrupoles⟧"],
            slides=[
                ("⟦Xung hai chiều và ba chiều||Two- and three-dimensional impulses⟧",
                 "<p>⟦$^2\\delta(x,y)$ mô tả phân bố áp suất trên mặt phẳng khi đặt một lực tập trung đơn vị tại gốc; $^3\\delta(x,y,z)$ mô tả mật độ điện tích trong một thể tích chứa một điện tích đơn vị tại $(0,0,0)$. Tính chất được thiết lập bằng dãy như $\\tau^{-2}\\Pi(x/\\tau)\\Pi(y/\\tau)$ có thể tích 1 (tr. 89).||"
                 "$^2\\delta(x,y)$ describes the pressure distribution over the plane when a concentrated unit force is applied at the origin; $^3\\delta(x,y,z)$ describes the charge density in a volume containing a unit charge at $(0,0,0)$. Properties are established with sequences such as $\\tau^{-2}\\Pi(x/\\tau)\\Pi(y/\\tau)$ of unit volume (p. 89).⟧</p>"
                 + F("⟦Xung hai chiều||Two-dimensional impulse⟧", r"\iint{}^2\delta(x,y)\,dx\,dy=1,\qquad {}^2\delta(ax,by)=\frac{1}{|ab|}\,{}^2\delta(x,y),\qquad {}^2\delta(x,y)=\delta(x)\,\delta(y)")),
                ("⟦Dạng xuyên tâm và trụ||Radial and cylindrical forms⟧",
                 "<p>⟦Với $r^2=x^2+y^2$, $^2\\delta(x,y)=\\delta(r)/\\pi r$. Trong ba chiều, $^3\\delta(x,y,z)=\\delta(x)\\delta(y)\\delta(z)={}^2\\delta(x,y)\\delta(z)$, và trong toạ độ trụ và cầu có các dạng tương ứng (tr. 89 đến 90). Số đo: tích phân $2\\pi r\\,dr$ của $\\delta_\\tau(r)/\\pi r$ với dãy Gauss trên mặt phẳng ($\\tau=0.1$) bằng {{delta2_vol}}.||"
                 "With $r^2=x^2+y^2$, $^2\\delta(x,y)=\\delta(r)/\\pi r$. In three dimensions, $^3\\delta(x,y,z)=\\delta(x)\\delta(y)\\delta(z)={}^2\\delta(x,y)\\delta(z)$, with matching forms in cylindrical and spherical coordinates (pp. 89 to 90). Measured: the integral over the plane ($2\\pi r\\,dr$) of a two-dimensional Gaussian sequence ($\\tau=0.1$) equals {{delta2_vol}}.⟧</p>"),
                ("⟦Giường đinh $^2\\text{III}(x,y)$||The bed of nails $^2\\text{III}(x,y)$⟧",
                 "<p>⟦Để mô tả các dàn hai chiều, dùng ký hiệu giường đinh (hình 5.12). Nó tích được: $^2\\text{III}(x,y)=\\text{III}(x)\\text{III}(y)$, tuần hoàn kép, và $f(x,y)\\,{}^2\\text{III}=\\sum\\sum f(m,n)\\,{}^2\\delta(x-m,y-n)$: dữ liệu hai chiều tra bảng và hệ số của chuỗi Fourier kép (tr. 90 đến 91). Chập với nó cho bản sao hai chiều, như dàn ăng-ten giống hệt nhau. Số đo: $\\sum\\sum e^{-\\pi(m^2+n^2)}$ = {{nails_sum}} bằng bình phương của tổng một chiều {{X_sum_1}}.||"
                 "For two-dimensional arrays use the bed-of-nails symbol (Fig. 5.12). It factorises: $^2\\text{III}(x,y)=\\text{III}(x)\\text{III}(y)$, is doubly periodic, and $f(x,y)\\,{}^2\\text{III}=\\sum\\sum f(m,n)\\,{}^2\\delta(x-m,y-n)$: two-dimensionally sampled data and the coefficients of double Fourier series (pp. 90 to 91). Convolving with it gives two-dimensional replicas, as in an array of identical antennas. Measured: $\\sum\\sum e^{-\\pi(m^2+n^2)}$ = {{nails_sum}}, the square of the one-dimensional sum {{X_sum_1}}.⟧</p>"
                 + F("⟦Giường đinh||Bed of nails⟧", r"{}^2\text{III}(x,y)=\sum_{m}\sum_{n}{}^2\delta(x-m,\,y-n)=\text{III}(x)\,\text{III}(y)")),
                ("⟦Hàng đinh và cách tử||The row of spikes and the grating⟧",
                 "<p>⟦Hai phân bố hai chiều quan trọng không cần ký hiệu mới: hàng đinh $\\text{III}(x)\\delta(y)$ và cách tử $\\text{III}(x)$ (hình 5.14). Chúng tạo thành một cặp biến đổi Fourier hai chiều, tiện cho bàn về nhiễu xạ ánh sáng qua một hàng lỗ kim hay qua cách tử nhiễu xạ (tr. 91).||"
                 "Two other important two-dimensional distributions need no new symbols: the row of spikes $\\text{III}(x)\\delta(y)$ and the grating $\\text{III}(x)$ (Fig. 5.14). They form a two-dimensional Fourier transform pair, suitable for discussing the diffraction of light by a row of pinholes or by a diffraction grating (p. 91).⟧</p>"),
                ("⟦Đạo hàm của xung: dipole và tứ cực||Derivatives of impulses: dipoles and quadrupoles⟧",
                 "<p>⟦Diễn giải bằng đạo hàm của xung, nhiều dạng là phân bố điện tích quen thuộc. $\\delta'(x)$ trên mặt phẳng $(x,y)$ là phân bố mô men lưỡng cực đường nằm trên trục $y$; trong không gian ba chiều là phân bố mô men lưỡng cực mặt trên mặt phẳng $(y,z)$. Lưỡng cực đơn tại gốc, mô men đơn vị theo $x$, là $-\\delta'(x)\\delta(y)\\delta(z)$. Tứ cực đơn là $\\delta''(x)\\delta(y)\\delta(z)$ (tr. 91 đến 92).||"
                 "Interpreted with derivatives of impulses, many forms are familiar electric-charge distributions. $\\delta'(x)$ on the $(x,y)$-plane is a line distribution of dipole moment on the $y$-axis; in three dimensions a sheet of dipole moment on the $(y,z)$-plane. A simple dipole at the origin with unit moment along $x$ is $-\\delta'(x)\\delta(y)\\delta(z)$. A simple unit quadrupole is $\\delta''(x)\\delta(y)\\delta(z)$ (pp. 91 to 92).⟧</p>"
                 + F("⟦Dipole và tứ cực||Dipole and quadrupole⟧", r"\text{dipole}=-\delta'(x)\delta(y)\delta(z),\qquad \text{quadrupole}=\delta''(x)\delta(y)\delta(z)")),
                ("⟦Ứng dụng vào phương trình vật lý||Use in physical equations⟧",
                 "<p>⟦Bức xạ tứ diệp (cỏ ba lá) của một anten có giản đồ mô tả bởi $\\delta'(x)\\delta'(y)$ trên mặt phẳng $(x,y)$. Mọi biểu thức ký hiệu này có thể tin cậy đưa vào phương trình Maxwell, phương trình sóng, phương trình Poisson và các phương trình vi phân cơ bản khác (tr. 92).||"
                 "$\\delta'(x)\\delta'(y)$ represents an electromagnetic radiator with a quatrefoil (clover-leaf) radiation pattern in the $(x,y)$-plane. All these symbolic expressions may confidently be inserted into Maxwell's equations, the wave equation, Poisson's equation and other fundamental differential equations (p. 92).⟧</p>"),
                ("⟦Tự kiểm tra phần 4||Self-check, part 4⟧",
                 UL(["⟦Viết $^2\\delta(2x,3y)$ theo $^2\\delta(x,y)$.||Write $^2\\delta(2x,3y)$ in terms of $^2\\delta(x,y)$.⟧",
                     "⟦$^2\\text{III}(x,y)$ liên hệ thế nào với $\\text{III}(x)$ và $\\text{III}(y)$?||How is $^2\\text{III}(x,y)$ related to $\\text{III}(x)$ and $\\text{III}(y)$?⟧",
                     "⟦Xung nào biểu diễn một lưỡng cực đơn vị hướng theo $x$?||Which impulse represents a unit dipole along $x$?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: $\\tfrac16\\,{}^2\\delta(x,y)$; là tích; $-\\delta'(x)\\delta(y)\\delta(z)$.||Hints: $\\tfrac16\\,{}^2\\delta(x,y)$; the product; $-\\delta'(x)\\delta(y)\\delta(z)$.⟧</p>"),
            ]),
        # ---------------------------------------------------------------- PART 5
        dict(
            title="⟦Hàm suy rộng: cơ sở chặt chẽ||Generalized functions: the rigorous basis⟧",
            scr=("⟦Ký hiệu xung rất tiện, nhưng ta vẫn muốn nó có nền chặt chẽ.||The impulse symbol is convenient but we still want it on a rigorous footing.⟧",
                 "⟦Khó khăn: $\\delta$ không phải hàm, và ta còn muốn cộng chúng, lấy đạo hàm chúng.||The difficulty: $\\delta$ is not a function, and we also want to add them and differentiate them.⟧",
                 "⟦Định nghĩa hàm suy rộng như lớp các dãy chính quy của hàm trơn, và định nghĩa phép toán bằng tích phân từng phần.||Define a generalized function as a class of regular sequences of smooth functions, with operations defined by integration by parts.⟧"),
            preview=["⟦Vì sao cần: gián đoạn, dòng xoay chiều thuần túy, độ phân giải hữu hạn||Why: discontinuities, pure AC, finite resolution⟧", "⟦Hàm trơn tuyệt đối, dãy chính quy||Well-behaved functions and regular sequences⟧", "⟦Đại số và đạo hàm của hàm suy rộng||Algebra and derivatives of generalized functions⟧"],
            slides=[
                ("⟦Vì sao cần hàm suy rộng||Why we need generalized functions⟧",
                 "<p>⟦Ký hiệu xung và các tổ hợp như $\\text{III}$, $\\mu$ đem lại nhiều tiện lợi, trong đó có việc cho đạo hàm của hàm có gián đoạn đơn giản. Thông thường ta nói đạo hàm không tồn tại; ký hiệu xung cho phép chứa các gián đoạn đó (Bracewell, tr. 92). Dùng \"symbol\" để nhắc rằng đây không phải hàm.||"
                 "The impulse symbol and combinations such as $\\text{III}$ and $\\mu$ bring much convenience, one use being to provide derivatives for functions with simple discontinuities. Ordinarily we would say the derivative does not exist; the impulse symbol permits such discontinuities to be accommodated (Bracewell, p. 92). The word \"symbol\" reminds us these are not functions.⟧</p>"),
                ("⟦Dòng xoay chiều thuần túy: vô hạn xa xôi là tiện lợi||Pure alternating current: the infinitely remote past is convenient⟧",
                 "<p>⟦Dòng xoay chiều thuần túy là biến thiên điều hòa vĩnh cửu, không tạo được. Nhưng đáp ứng với biến thiên điều hòa trên một khoảng rồi bằng 0 bên ngoài có thể làm độc lập với thời điểm bật tới một độ chính xác cho trước, nếu chờ đủ lâu. Vì cách bật không quan trọng, ta đẩy nó vào quá khứ vô hạn xa (tr. 92 đến 93). Tương tự, xung không tạo được nhưng đáp ứng với các xung đủ ngắn có thể không phân biệt được, với độ phân giải hữu hạn.||"
                 "Pure alternating current means an eternal harmonic variation, which cannot be generated. But the response to a variation that is harmonic over an interval and zero outside can be made independent of the switching time to a given precision by waiting long enough. Since the details of switching are irrelevant they may be relegated to the infinitely remote past (pp. 92 to 93). Likewise impulses cannot be generated, but responses to sufficiently brief pulses can be made indistinguishable at finite resolution.⟧</p>"),
                ("⟦Độ phân giải hữu hạn là chìa khóa||Finite resolution is the key⟧",
                 "<p>⟦Độ chính xác đo bị giới hạn bởi độ phân giải thời gian và phổ của thiết bị. Chính đặc điểm này là chìa khóa cho việc diễn giải toán học: tích phân chứa $\\delta$ được hiểu là giới hạn của dãy tích phân trong đó $\\delta$ thay bằng xung chữ nhật diện tích 1. Giới hạn có thể tồn tại dù các xung chữ nhật cao lên vô hạn. Tình huống vật lý tương ứng là dãy kích thích ngày càng gọn cho đáp ứng ngày càng khó phân biệt, dù độ chính xác cao tới đâu (tr. 93).||"
                 "Precision of measurement is limited by the temporal and spectral resolution of the instrument. That feature is the key to the mathematical interpretation: integrals containing $\\delta$ are limits of a sequence of integrals in which $\\delta$ is replaced by unit-area rectangular pulses. The limit may exist even though the rectangular pulses grow without limit. The physical situation is a sequence of ever more compact stimuli producing responses that become indistinguishable however high the precision (p. 93).⟧</p>"),
                ("⟦Lịch sử của cách tiếp cận||History of the approach⟧",
                 "<p>⟦Một lý thuyết chặt chẽ được xây theo hướng này, trình bày trong sách của Lighthill (1958) và Friedman (1956). Lighthill ghi công Temple đã đơn giản hóa trình bày; Temple (1953) ghi công nhà toán học Ba Lan Mikusiński (1948) đưa ra cách trình bày bằng dãy. Hai tập của Schwartz (1950, 1951) về lý thuyết phân bố (distributions) thống nhất các kỹ thuật riêng lẻ. Ý tưởng về dãy đã lưu hành trong giới vật lý từ trước 1948, xuất phát từ G. S. Kirchhoff năm 1882 (tr. 93).||"
                 "A satisfactory mathematical formulation was evolved along these lines and is expounded in the books of Lighthill (1958) and Friedman (1956). Lighthill credits Temple with simplifying the presentation; Temple (1953) credits the Polish mathematician Mikusiński (1948) with introducing the presentation in terms of sequences. Schwartz's two volumes (1950, 1951) on the theory of distributions unify partial and special techniques. The idea of sequences was current in physical circles before 1948, going back to G. S. Kirchhoff in 1882 (p. 93).⟧</p>"),
                ("⟦Lớp $S$: các hàm trơn tuyệt đối||The class $S$: particularly well-behaved functions⟧",
                 "<p>⟦Lớp $S$ gồm các hàm có đạo hàm mọi cấp tại mọi điểm và, cùng mọi đạo hàm, tắt ít nhất nhanh như $|x|^{-N}$ khi $|x|\\to\\infty$, với $N$ lớn tùy ý. Đạo hàm và biến đổi Fourier của một hàm trong $S$ cũng thuộc $S$ (tr. 94). Độ tắt của biến đổi phản ánh độ trơn: biến đổi của Gauss tại $s=3$ là {{gauss_tail}}, còn của xung chữ nhật, $|\\text{sinc}(3.5)|$ = {{sinc_tail}}, tắt chỉ như $1/s$.||"
                 "The class $S$ consists of functions with derivatives of all orders at all points which, with all their derivatives, die off at least as rapidly as $|x|^{-N}$ as $|x|\\to\\infty$, however large $N$. The derivative and the Fourier transform of a function in $S$ are also in $S$ (p. 94). The decay of the transform reflects smoothness: the transform of a Gaussian at $s=3$ is {{gauss_tail}}, while for the rectangle $|\\text{sinc}(3.5)|$ = {{sinc_tail}}, decaying only like $1/s$.⟧</p>"),
                ("⟦Dãy chính quy||Regular sequences⟧",
                 "<p>⟦Trong các dãy hàm trơn tuyệt đối, ta chọn dãy $p_\\tau(x)$ có giới hạn khi nhân với mọi hàm trơn tuyệt đối $F(x)$ rồi lấy tích phân: gọi là dãy chính quy. Ví dụ dãy $\\tau^{-1}\\exp(-\\pi x^2/\\tau^2)$ là chính quy; hình 5.15 nêu một dãy không chính quy. Diện tích đơn vị không bắt buộc, chẳng hạn $(1+\\tau^{-1})\\exp(-x^2/\\tau^2)$ cũng chính quy (tr. 94 đến 95).||"
                 "Among sequences of particularly well-behaved functions we distinguish sequences $p_\\tau(x)$ which lead to limits when multiplied by any well-behaved $F(x)$ and integrated: regular sequences. The sequence $\\tau^{-1}\\exp(-\\pi x^2/\\tau^2)$ is regular; Fig. 5.15 shows a non-regular example. Unit area is not essential; for instance $(1+\\tau^{-1})\\exp(-x^2/\\tau^2)$ is also regular (pp. 94 to 95).⟧</p>"),
                ("⟦Hàm suy rộng là một lớp các dãy||A generalized function is a class of sequences⟧",
                 "<p>⟦Một hàm suy rộng $p(x)$ được xác định bởi một dãy chính quy. Vì giới hạn có thể như nhau với nhiều dãy, hàm suy rộng là lớp mọi dãy chính quy tương đương. Ký hiệu $p(x)$ đại diện cho một thực thể khác hàm thường: một lớp hàm và bản thân không phải hàm, nên khi viết ở nơi quen dùng hàm thường phải nêu rõ nghĩa (tr. 95). Dãy $\\tau^{-1}\\Pi(x/\\tau)$ và $\\tau^{-1}\\Lambda(x/\\tau)$ không nằm trong định nghĩa chặt vì không có đạo hàm mọi cấp, nhưng dùng được khi chỉ cần đạo hàm bậc thấp (tr. 95 đến 96).||"
                 "A generalized function $p(x)$ is defined by a regular sequence. Since the limit can be the same for more than one sequence, it is finally the class of all equivalent regular sequences. The symbol $p(x)$ stands for an entity different from an ordinary function: it stands for a class of functions and is itself not a function, so when written where ordinary functions are customary the meaning must be stated (p. 95). The sequences $\\tau^{-1}\\Pi(x/\\tau)$ and $\\tau^{-1}\\Lambda(x/\\tau)$ do not strictly define one since they lack derivatives of all orders, but they are usable where only low-order derivatives are needed (pp. 95 to 96).⟧</p>"),
                ("⟦Chứng minh $\\tau^{-1}e^{-\\pi x^2/\\tau^2}\\to\\delta$||Proof that $\\tau^{-1}e^{-\\pi x^2/\\tau^2}\\to\\delta$⟧",
                 "<p>⟦Dãy $e^{-\\pi\\tau^2x^2}$ xác định hàm suy rộng $I(x)=1$ vì $\\lim\\int e^{-\\pi\\tau^2x^2}F\\,dx=\\int F\\,dx$. Dãy $\\tau^{-1}e^{-\\pi x^2/\\tau^2}$ xác định $\\delta$: $\\bigl|\\int\\tau^{-1}e^{-\\pi x^2/\\tau^2}[F(x)-F(0)]dx\\bigr|\\le\\max|F'|\\int|x|\\tau^{-1}e^{-\\pi x^2/\\tau^2}dx=\\tau\\max|F'|/\\pi$, tiến về 0 (tr. 96). Số đo với $F=\\cos x$, $\\tau=0.1$: sai lệch thật {{dev_01}} nhỏ hơn cận {{bound_01}}.||"
                 "The sequence $e^{-\\pi\\tau^2x^2}$ defines the generalized function $I(x)=1$ since $\\lim\\int e^{-\\pi\\tau^2x^2}F\\,dx=\\int F\\,dx$. The sequence $\\tau^{-1}e^{-\\pi x^2/\\tau^2}$ defines $\\delta$: $\\bigl|\\int\\tau^{-1}e^{-\\pi x^2/\\tau^2}[F(x)-F(0)]dx\\bigr|\\le\\max|F'|\\int|x|\\tau^{-1}e^{-\\pi x^2/\\tau^2}dx=\\tau\\max|F'|/\\pi$, which tends to 0 (p. 96). Measured with $F=\\cos x$, $\\tau=0.1$: the actual deviation {{dev_01}} is below the bound {{bound_01}}.⟧</p>"
                 + F("⟦Cận sai số||Error bound⟧", r"\left|\int\tau^{-1}e^{-\pi x^2/\tau^2}F(x)\,dx-F(0)\right|\ \le\ \frac{\tau}{\pi}\max|F'|")),
                ("⟦Đại số: cộng và đạo hàm hàm suy rộng||Algebra: adding and differentiating generalized functions⟧",
                 "<p>⟦Tổng của hai dãy chính quy là dãy chính quy, và không phụ thuộc cách chọn dãy, nên $p+q$ có nghĩa (tr. 96 đến 97). Đạo hàm định nghĩa qua tích phân từng phần: $\\int p'F\\,dx=-\\int pF'\\,dx$, và tổng quát $\\int p^{(n)}F\\,dx=(-1)^n\\int pF^{(n)}dx$. Vì $F$ trơn tuyệt đối có đạo hàm mọi cấp nên hàm suy rộng có đạo hàm mọi cấp (tr. 97 đến 98).||"
                 "The sum of two regular sequences is regular and independent of the choice of sequences, so $p+q$ is meaningful (pp. 96 to 97). Derivatives are defined through integration by parts: $\\int p'F\\,dx=-\\int pF'\\,dx$, and in general $\\int p^{(n)}F\\,dx=(-1)^n\\int pF^{(n)}dx$. Since well-behaved $F$ has derivatives of every order, a generalized function has derivatives of every order (pp. 97 to 98).⟧</p>"
                 + F("⟦Đạo hàm hàm suy rộng||Derivative of a generalized function⟧", r"\int p'(x)\,F(x)\,dx=-\int p(x)\,F'(x)\,dx")),
                ("⟦Đạo hàm của hàm thường: $H'=\\delta$||Differentiating ordinary functions: $H'=\\delta$⟧",
                 "<p>⟦Một hàm thường tăng chậm cũng xem được như hàm suy rộng, nên $H(x)$ có đạo hàm: $\\int H'F\\,dx=-\\int H F'\\,dx=-\\int_0^\\infty F'dx=F(0)$, mà $\\int\\delta F\\,dx=F(0)$, nên $H'=\\delta$ (tr. 98). Số đo với $F=e^{-x^2}$: $-\\int_0^\\infty F'$ = {{hp_exact}}; với dãy đạo hàm của $\\tfrac12+\\arctan(x/\\tau)/\\pi$ (Lorentz), $\\tau=0.1$ cho {{hp_1}} và $\\tau=0.01$ cho {{hp_2}}: hội tụ về 1 nhưng chậm vì đuôi Lorentz.||"
                 "An ordinary function of slow growth can also be regarded as a generalized function, so $H(x)$ has a derivative: $\\int H'F\\,dx=-\\int H F'\\,dx=-\\int_0^\\infty F'dx=F(0)$, while $\\int\\delta F\\,dx=F(0)$, hence $H'=\\delta$ (p. 98). Measured with $F=e^{-x^2}$: $-\\int_0^\\infty F'$ = {{hp_exact}}; with the derivative sequence of $\\tfrac12+\\arctan(x/\\tau)/\\pi$ (a Lorentzian), $\\tau=0.1$ gives {{hp_1}} and $\\tau=0.01$ gives {{hp_2}}: converging to 1 but slowly because of the Lorentzian tails.⟧</p>"),
                ("⟦Liên hệ chéo với Barkat||Cross-reference to Barkat⟧",
                 "<p>⟦Barkat, mục 1.3.1 (Step and Impulse Functions) dùng đúng công cụ này cho biến ngẫu nhiên: hàm phân phối tích lũy của biến rời rạc là tổng các bậc thang $\\sum P_kH(x-x_k)$ và mật độ là tổng các xung $\\sum P_k\\delta(x-x_k)$; biến hỗn hợp có cả phần liên tục và phần xung (mục 1.3.4). Module 10 ghép hai sách ở điểm này.||"
                 "Barkat, section 1.3.1 (Step and Impulse Functions), uses exactly these tools for random variables: the cumulative distribution of a discrete variable is a sum of steps $\\sum P_kH(x-x_k)$ and its density a sum of impulses $\\sum P_k\\delta(x-x_k)$; mixed variables have both a continuous part and an impulsive part (section 1.3.4). Module 10 merges the two books here.⟧</p>"
                 + F("⟦Mật độ của biến rời rạc||Density of a discrete variable⟧", r"f_X(x)=\sum_kP_k\,\delta(x-x_k)")),
                ("⟦Tự kiểm tra phần 5||Self-check, part 5⟧",
                 UL(["⟦Hàm suy rộng khác hàm thường ở điểm nào?||How does a generalized function differ from an ordinary function?⟧",
                     "⟦Đạo hàm của hàm suy rộng được định nghĩa thế nào?||How is the derivative of a generalized function defined?⟧",
                     "⟦Vì sao $H'=\\delta$ dù $H$ không có đạo hàm tại 0?||Why is $H'=\\delta$ although $H$ has no derivative at 0?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: nó là một lớp dãy chính quy; bằng tích phân từng phần; vì đạo hàm được định nghĩa qua phép thử $-\\int HF'=F(0)$.||Hints: it is a class of regular sequences; by integration by parts; because the derivative is defined through the test $-\\int HF'=F(0)$.⟧</p>"),
            ]),
    ],
    takeaways=[
        "⟦$\\delta$ là dấu tắt cho dãy xung diện tích 1; dạng xung không quan trọng, chỉ tích phân có nghĩa.||$\\delta$ is shorthand for a sequence of unit-area pulses; the pulse shape does not matter, only the integral.⟧",
        "⟦Sàng: $\\int\\delta f=f(0)$; tỉ lệ: $\\delta(ax)=\\delta/|a|$; $x\\delta=0$ nhưng có cực đại $\\tfrac12$ trước giới hạn.||Sifting: $\\int\\delta f=f(0)$; scaling: $\\delta(ax)=\\delta/|a|$; $x\\delta=0$ but a maximum $\\tfrac12$ exists before the limit.⟧",
        "⟦Shah lấy mẫu khi nhân và nhân bản khi chập, và tự biến đổi; xung cách nhau $X$ là $X^{-1}\\text{III}(x/X)$.||Shah samples under multiplication, replicates under convolution and is self-transforming; unit impulses spaced $X$ are $X^{-1}\\text{III}(x/X)$.⟧",
        "⟦$\\delta'$ là dipole: $\\int\\delta'f=-f'(0)$; hàm rỗng có tích phân 0 và biến đổi 0.||$\\delta'$ is a dipole: $\\int\\delta'f=-f'(0)$; null functions have zero integral and zero transform.⟧",
        "⟦Hàm suy rộng là lớp các dãy chính quy; đạo hàm định nghĩa bằng tích phân từng phần, nên $H'=\\delta$.||A generalized function is a class of regular sequences; derivatives are defined by integration by parts, so $H'=\\delta$.⟧",
    ],
    history="<p>⟦Ký hiệu $\\delta(x)$ do G. Kirchhoff dùng lần đầu, được Dirac đưa vào cơ học lượng tử năm 1927, và ngày nay dùng rộng rãi. Các ví dụ lịch sử về ý tưởng xung có ở Hermite, Cauchy, Poisson, Kirchhoff, Helmholtz, Kelvin và Heaviside (van der Pol và Bremmer, 1955) (Bracewell, tr. 74).||"
            "The notation $\\delta(x)$ was first used by G. Kirchhoff, introduced into quantum mechanics by Dirac in 1927 and is now in general use. Historical examples of the impulse idea appear in Hermite, Cauchy, Poisson, Kirchhoff, Helmholtz, Kelvin and Heaviside (van der Pol and Bremmer, 1955) (Bracewell, p. 74).⟧</p>"
            "<p>⟦Từ \"hàm suy rộng\" do G. Temple đưa ra năm 1953; Dirac gọi $\\delta$ là \"hàm không chính thức\"; Bracewell dùng \"ký hiệu\" một cách hệ thống để đánh dấu các thực thể không phải hàm (tr. 74). Lý thuyết chặt chẽ có trong Lighthill (1958) và Friedman (1956), Schwartz (1950, 1951) về phân bố, và Mikusiński (1948) với cách trình bày qua dãy (tr. 93).||"
            "The term \"generalized function\" was introduced by G. Temple in 1953; Dirac called $\\delta$ an \"improper function\"; Bracewell uses \"symbol\" systematically to mark entities that are not functions (p. 74). The rigorous theory is in Lighthill (1958) and Friedman (1956), Schwartz (1950, 1951) on distributions, and Mikusiński (1948) with the presentation through sequences (p. 93).⟧</p>",
    case="<p>⟦<b>Đáp ứng xung của một mạch lọc.</b> Muốn đặc trưng một mạch RC, ta không cần một xung lý tưởng: chỉ cần một xung đủ ngắn. Với ba xung khác dạng (chữ nhật, tam giác, hai xung nhỏ) và diện tích 1, độ chênh giữa ba đáp ứng tại $t=1$ chỉ còn {{spread_05}} khi xung rộng 0.5, {{spread_01}} khi 0.1 và {{spread_001}} khi 0.01, tức đáp ứng tiến về một dạng duy nhất $h(t)=e^{-t}H(t)$. Kỹ sư đo đáp ứng xung bằng cách đưa xung ngắn hơn hằng số thời gian của mạch nhiều lần.||"
          "<b>Impulse response of a filter circuit.</b> To characterise an RC circuit we do not need an ideal impulse, only a sufficiently brief pulse. With three differently shaped unit-area pulses (rectangle, triangle, two small pulses) the spread between the three responses at $t=1$ falls to {{spread_05}} for width 0.5, {{spread_01}} for 0.1 and {{spread_001}} for 0.01, i.e. the responses approach a single form $h(t)=e^{-t}H(t)$. Engineers measure impulse responses by applying a pulse many times shorter than the circuit's time constant.⟧</p>"
         "<p>⟦Đây là lý do định nghĩa $\\delta$ bằng dãy là hợp lý: thiết bị có độ phân giải hữu hạn thì không phân biệt được một xung ngắn với $\\delta$.||This is why defining $\\delta$ through sequences is reasonable: an instrument with finite resolution cannot distinguish a brief pulse from $\\delta$.⟧</p>",
    practice=[
        "⟦Mở notebook và chạy cell cài đặt.||Open the notebook and run the setup cell.⟧",
        "⟦Bài 1: cho ba dạng xung khác vào mạch RC với hằng số $RC=2$ và đo độ chênh tại $t=3$ khi $\\tau$ giảm.||Task 1: feed three other pulse shapes into an RC circuit with $RC=2$ and measure the spread at $t=3$ as $\\tau$ decreases.⟧",
        "⟦Bài 2: thêm hai dạng xung của riêng bạn vào bảng sàng và kiểm chúng tiến về $f(0)$.||Task 2: add two pulse shapes of your own to the sifting table and check they tend to $f(0)$.⟧",
        "⟦Bài 3: thử $\\text{III}(x/X)$ với $X=0.25$ và $X=2$, kiểm $X\\sum f(nX)$ tiến về diện tích thế nào.||Task 3: try $\\text{III}(x/X)$ with $X=0.25$ and $X=2$ and see how $X\\sum f(nX)$ approaches the area.⟧",
        "⟦Bài 4: kiểm $\\int x^3\\delta'''$ và $\\int\\delta^{(4)}f$ bằng dãy Gauss.||Task 4: check $\\int x^3\\delta'''$ and $\\int\\delta^{(4)}f$ with a Gaussian sequence.⟧",
        "⟦Bài 5: tự chọn hàm thử $F$ và kiểm cận $\\tau\\max|F'|/\\pi$.||Task 5: pick a test function $F$ of your own and check the bound $\\tau\\max|F'|/\\pi$.⟧",
    ],
    pitfalls=[
        "<b>⟦\"$\\delta(x)$ là hàm bằng vô cùng tại 0.\"||\"$\\delta(x)$ is a function equal to infinity at 0.\"⟧</b><p>⟦Không phải hàm: nó là dấu tắt cho giới hạn của các tích phân. Giá trị \"vô cùng\" không có nghĩa; chỉ tích phân có nghĩa (tr. 74 đến 75).||It is not a function: it is shorthand for a limit of integrals. The \"infinite value\" is meaningless; only the integral has meaning (pp. 74 to 75).⟧</p>",
        "<b>⟦\"$\\delta(ax)=\\delta(x)$.\"||\"$\\delta(ax)=\\delta(x)$.\"⟧</b><p>Đúng là $\\delta(ax)=\\delta(x)/|a|$: ⟦với $a=3$, tích phân sàng bằng {{scale_3}} chứ không phải 1 (tr. 80).||the sifting integral for $a=3$ equals {{scale_3}}, not 1 (p. 80).⟧</p>",
        "<b>⟦\"$X$ khoảng cách giữa các xung thì $\\text{III}(x/X)$ có xung đơn vị.\"||\"With spacing $X$, $\\text{III}(x/X)$ has unit impulses.\"⟧</b><p>⟦Sai: cường độ là $X$; xung đơn vị cách nhau $X$ là $X^{-1}\\text{III}(x/X)$. Bỏ hệ số $X^{-1}$ làm tổng mẫu {{X_sum_05}} thay vì {{X_riem_05}} (tr. 83).||Wrong: the strength is $X$; unit impulses spaced $X$ are $X^{-1}\\text{III}(x/X)$. Dropping the factor $X^{-1}$ makes the sum of samples {{X_sum_05}} instead of {{X_riem_05}} (p. 83).⟧</p>",
        "<b>⟦\"$x\\delta(x)=0$ nên biến mất hoàn toàn.\"||\"$x\\delta(x)=0$ so it vanishes completely.\"⟧</b><p>⟦Tích phân của nó là 0, nhưng trước giới hạn nó đạt cực đại {{xd_max}} với mọi $\\tau$ (giống Gibbs); nếu đưa vào màn dao động ký ta sẽ thấy các xung nhọn (tr. 81).||Its integral is 0 but before the limit its maximum is {{xd_max}} for every $\\tau$ (Gibbs-like); fed to an oscilloscope one would see spikes (p. 81).⟧</p>",
    ],
    refs=[
        "⟦R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chương 5 (tr. 74 đến 98).||R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chapter 5 (pp. 74 to 98).⟧",
        "⟦M. Barkat, <i>Signal Detection and Estimation</i>, 2nd ed., Artech House, 2005, mục 1.3.1 và 1.3.4, chỉ dẫn tới ở phần liên hệ chéo.||M. Barkat, <i>Signal Detection and Estimation</i>, 2nd ed., Artech House, 2005, sections 1.3.1 and 1.3.4, cited only in the cross-reference.⟧",
    ],
    quiz=[
        dict(q="⟦Với ba xung diện tích 1 rộng $\\tau=0.01$ đưa vào mạch RC, độ chênh giữa ba đáp ứng tại $t=1$ là bao nhiêu?||With three unit-area pulses of width $\\tau=0.01$ fed into an RC circuit, what is the spread among the three responses at $t=1$?⟧",
             opts=["{{spread_001}}", "{{spread_05}}", "0.5", "0.0368"], explain="⟦Xung càng ngắn thì đáp ứng càng không phụ thuộc dạng: {{spread_05}} ($\\tau=0.5$), {{spread_01}} (0.1), {{spread_001}} (0.01).||The shorter the pulse the less the response depends on shape: {{spread_05}} ($\\tau=0.5$), {{spread_01}} (0.1), {{spread_001}} (0.01).⟧"),
        dict(q="⟦$\\int_{-\\infty}^{x}\\tau^{-1}\\Pi(x'/\\tau)dx'$ tại $x=0.1$ với $\\tau=0.5$ bằng bao nhiêu?||What is $\\int_{-\\infty}^{x}\\tau^{-1}\\Pi(x'/\\tau)dx'$ at $x=0.1$ with $\\tau=0.5$?⟧",
             opts=["{{step_x01_t05}}", "0.5", "0.6", "1"], explain="⟦Hàm dốc-bậc thang: $\\tfrac12+x/\\tau$ = {{step_x01_t05}}; với $\\tau=0.1$ đã bão hòa ở {{step_x01_t01}}.||The ramp-step: $\\tfrac12+x/\\tau$ = {{step_x01_t05}}; for $\\tau=0.1$ it has saturated at {{step_x01_t01}}.⟧"),
        dict(q="⟦Dãy chữ nhật cạnh trái ($\\tau=0.01$) sàng $\\int f\\delta_\\tau$ với $f=\\cos x+\\tfrac12\\sin2x$ cho giá trị gần nhất là bao nhiêu?||The left-edge rectangular sequence ($\\tau=0.01$) sifting $f=\\cos x+\\tfrac12\\sin2x$ gives approximately what?⟧",
             opts=["{{sift_rl_001}}", "{{sift_rl_01}}", "0.9", "1.5"], explain="⟦Tiến về $f(0+)=1$: {{sift_rl_01}} khi $\\tau=0.1$ và {{sift_rl_001}} khi $\\tau=0.01$.||Tends to $f(0+)=1$: {{sift_rl_01}} for $\\tau=0.1$ and {{sift_rl_001}} for $\\tau=0.01$.⟧"),
        dict(q="⟦Dãy Gauss ($\\tau=0.1$) sàng cùng $f$ cho bao nhiêu?||What does the Gaussian sequence ($\\tau=0.1$) give for the same $f$?⟧",
             opts=["{{sift_g_01}}", "1", "0.5", "1.0498"], explain="⟦$e^{-\\tau^2/4\\pi}$ = {{sift_g_01}}, tiến về 1.||$e^{-\\tau^2/4\\pi}$ = {{sift_g_01}}, tending to 1.⟧"),
        dict(q="⟦Với $f=e^{-x}H(x)$, dãy chữ nhật đặt giữa sàng ra giá trị nào tại chỗ nhảy?||With $f=e^{-x}H(x)$, what value does the centred rectangular sequence sift at the jump?⟧",
             opts=["{{jump_mid}}", "1", "0", "0.25"], explain="⟦Trung bình $\\tfrac12[f(0+)+f(0-)]$ = {{jump_mid}}; dãy cạnh trái cho {{jump_left}}.||The mean $\\tfrac12[f(0+)+f(0-)]$ = {{jump_mid}}; the left-edge sequence gives {{jump_left}}.⟧"),
        dict(q="⟦$\\int f(x)\\,\\tau^{-1}\\Pi(3x/\\tau)\\,dx$ với $\\tau=0.01$ và $f(0)=1$ gần bằng bao nhiêu?||What is $\\int f(x)\\,\\tau^{-1}\\Pi(3x/\\tau)\\,dx$ for $\\tau=0.01$ and $f(0)=1$, approximately?⟧",
             opts=["{{scale_3}}", "1", "3", "0.1111"], explain="⟦$\\delta(3x)=\\delta(x)/3$ nên kết quả {{scale_3}}.||$\\delta(3x)=\\delta(x)/3$ so the result is {{scale_3}}.⟧"),
        dict(q="⟦Cực đại của $x\\,\\tau^{-1}\\Pi(x/\\tau)$ khi $\\tau\\to0$ là bao nhiêu?||What is the maximum of $x\\,\\tau^{-1}\\Pi(x/\\tau)$ as $\\tau\\to0$?⟧",
             opts=["{{xd_max}}", "0", "1", "0.25"], explain="⟦Luôn bằng {{xd_max}} tại mép xung, dù giới hạn từng điểm bằng 0.||Always {{xd_max}} at the pulse edge although the pointwise limit is 0.⟧"),
        dict(q="⟦$\\int f\\delta_\\tau g\\,dx$ với $f=\\cos x+\\tfrac12\\sin2x$, $g=e^{-x^2}$ tiến về giá trị nào?||To which value does $\\int f\\delta_\\tau g\\,dx$ tend for $f=\\cos x+\\tfrac12\\sin2x$ and $g=e^{-x^2}$?⟧",
             opts=["{{fg_sift}}", "0.5", "0.3679", "2"], explain="⟦$f(x)\\delta(x)=f(0)\\delta(x)$ nên $f(0)g(0)$ = {{fg_sift}}.||$f(x)\\delta(x)=f(0)\\delta(x)$ so $f(0)g(0)$ = {{fg_sift}}.⟧"),
        dict(q="⟦Với $f=e^{-\\pi x^2}$, tổng mẫu $\\sum_nf(n)$ bằng bao nhiêu?||For $f=e^{-\\pi x^2}$, what is the sum of samples $\\sum_nf(n)$?⟧",
             opts=["{{X_sum_1}}", "1", "0.9135", "2"], explain="⟦$1+2\\sum_{n\\ge1}e^{-\\pi n^2}$ = {{X_sum_1}}.||$1+2\\sum_{n\\ge1}e^{-\\pi n^2}$ = {{X_sum_1}}.⟧"),
        dict(q="⟦$(\\text{III}*f)(0.5)$ với $f=e^{-\\pi x^2}$ bằng bao nhiêu?||What is $(\\text{III}*f)(0.5)$ for $f=e^{-\\pi x^2}$?⟧",
             opts=["{{rep_05}}", "1.0864", "0.4559", "0.5"], explain="⟦$\\sum e^{-\\pi(0.5-n)^2}$ = {{rep_05}}, cũng bằng $\\sum(-1)^ke^{-\\pi k^2}$.||$\\sum e^{-\\pi(0.5-n)^2}$ = {{rep_05}}, also equal to $\\sum(-1)^ke^{-\\pi k^2}$.⟧"),
        dict(q="⟦$X\\sum_nf(nX)$ với $f=e^{-\\pi x^2}$ và $X=0.5$ bằng bao nhiêu?||What is $X\\sum_nf(nX)$ for $f=e^{-\\pi x^2}$ and $X=0.5$?⟧",
             opts=["{{X_riem_05}}", "2", "0.5", "1.0864"], explain="⟦Xấp xỉ diện tích ({{X_riem_05}}); còn $\\sum f(nX)$ không nhân $X$ cho {{X_sum_05}}.||It approximates the area ({{X_riem_05}}); $\\sum f(nX)$ without the factor $X$ gives {{X_sum_05}}.⟧"),
        dict(q="⟦Vế trái $\\sum_ne^{-\\pi n^2/4}$ của công thức Poisson bằng bao nhiêu?||What is the left side $\\sum_ne^{-\\pi n^2/4}$ of the Poisson formula?⟧",
             opts=["{{shah_lhs}}", "1.0864", "3.000014", "1"], explain="⟦Bằng $2\\sum_ke^{-4\\pi k^2}$ = {{shah_rhs}}: shah tự biến đổi.||Equal to $2\\sum_ke^{-4\\pi k^2}$ = {{shah_rhs}}: shah is self-transforming.⟧"),
        dict(q="⟦Biến đổi của cặp xung chẵn $\\mu(x)$ tại $s=0.3$ bằng bao nhiêu?||What is the transform of the even pair $\\mu(x)$ at $s=0.3$?⟧",
             opts=["{{mu_ft}}", "0.8090", "0.9511", "0.3090"], explain="⟦$\\cos0.3\\pi$ = {{mu_ft}}.||$\\cos0.3\\pi$ = {{mu_ft}}.⟧"),
        dict(q="⟦$(\\mu*f)(0)$ với $f=e^{-\\pi x^2}$ bằng bao nhiêu?||What is $(\\mu*f)(0)$ for $f=e^{-\\pi x^2}$?⟧",
             opts=["{{mu_conv}}", "1", "0.9121", "0.2280"], explain="⟦$\\tfrac12f(\\tfrac12)+\\tfrac12f(-\\tfrac12)=e^{-\\pi/4}$ = {{mu_conv}}.||$\\tfrac12f(\\tfrac12)+\\tfrac12f(-\\tfrac12)=e^{-\\pi/4}$ = {{mu_conv}}.⟧"),
        dict(q="⟦Sai phân hữu hạn $\\Delta f(0)$ của $f=\\sin x$ bằng bao nhiêu?||What is the finite difference $\\Delta f(0)$ of $f=\\sin x$?⟧",
             opts=["{{fd_0}}", "0.4794", "1", "0.8776"], explain="⟦$f(\\tfrac12)-f(-\\tfrac12)=2\\sin\\tfrac12$ = {{fd_0}}.||$f(\\tfrac12)-f(-\\tfrac12)=2\\sin\\tfrac12$ = {{fd_0}}.⟧"),
        dict(q="⟦Độ lớn biến đổi của $\\Delta f$ ($f=e^{-\\pi x^2}$) tại $s=0.3$ bằng bao nhiêu?||What is the magnitude of the transform of $\\Delta f$ ($f=e^{-\\pi x^2}$) at $s=0.3$?⟧",
             opts=["{{fd_ft}}", "0.7537", "1.618", "0.6097"], explain="⟦$2\\sin(0.3\\pi)e^{-0.09\\pi}$ = {{fd_ft}}, bằng tích phân số.||$2\\sin(0.3\\pi)e^{-0.09\\pi}$ = {{fd_ft}}, equal to the numerical integral.⟧"),
        dict(q="⟦$\\int\\delta'(x)f(x)dx$ với $f=\\cos x+\\tfrac12\\sin2x$ bằng bao nhiêu?||What is $\\int\\delta'(x)f(x)dx$ for $f=\\cos x+\\tfrac12\\sin2x$?⟧",
             opts=["{{dprime_sift}}", "1", "0", "-1.9984"], explain="⟦$-f'(0)$, với $f'(0)=1$, nên {{dprime_sift}}.||$-f'(0)$ with $f'(0)=1$, so {{dprime_sift}}.⟧"),
        dict(q="⟦$\\int x\\,\\delta'(x)dx$ bằng bao nhiêu?||What is $\\int x\\,\\delta'(x)dx$?⟧",
             opts=["{{x_dprime}}", "1", "0", "-2"], explain="⟦Bằng $-\\frac{d}{dx}x$ = {{x_dprime}} (tr. 86).||Equal to $-\\frac{d}{dx}x$ = {{x_dprime}} (p. 86).⟧"),
        dict(q="⟦$\\int|\\delta'_\\tau(x)|dx$ (Gauss) với $\\tau=0.01$ bằng bao nhiêu?||What is $\\int|\\delta'_\\tau(x)|dx$ (Gaussian) for $\\tau=0.01$?⟧",
             opts=["{{l1_001}}", "20", "2", "2000"], explain="⟦Bằng $2/\\tau$: {{l1_01}} khi $\\tau=0.1$ và {{l1_001}} khi $\\tau=0.01$, không có giới hạn hữu hạn.||It equals $2/\\tau$: {{l1_01}} for $\\tau=0.1$ and {{l1_001}} for $\\tau=0.01$, no finite limit.⟧"),
        dict(q="⟦$\\int x^2\\delta''(x)dx$ bằng bao nhiêu?||What is $\\int x^2\\delta''(x)dx$?⟧",
             opts=["{{x2_d2}}", "0", "1", "-2"], explain="⟦Bằng $(-1)^2\\frac{d^2}{dx^2}x^2$ = {{x2_d2}} (tr. 87).||Equal to $(-1)^2\\frac{d^2}{dx^2}x^2$ = {{x2_d2}} (p. 87).⟧"),
        dict(q="⟦$\\int\\delta''(x)f(x)dx$ với $f=\\cos x+\\tfrac12\\sin2x$ bằng bao nhiêu?||What is $\\int\\delta''(x)f(x)dx$ for $f=\\cos x+\\tfrac12\\sin2x$?⟧",
             opts=["{{d2_sift}}", "1", "0", "-2"], explain="⟦$f''(0)$ = {{d2_sift}}.||$f''(0)$ = {{d2_sift}}.⟧"),
        dict(q="⟦Tích phân của $\\int_{-\\infty}^\\infty{}^2\\delta$ dạng Gauss ($\\tau=0.1$) trên mặt phẳng bằng bao nhiêu?||What is the plane integral of a Gaussian ${}^2\\delta$ sequence ($\\tau=0.1$)?⟧",
             opts=["{{delta2_vol}}", "0.5", "2", "1.5708"], explain="⟦Thể tích đơn vị: {{delta2_vol}}.||Unit volume: {{delta2_vol}}.⟧"),
        dict(q="⟦$\\sum_m\\sum_ne^{-\\pi(m^2+n^2)}$ bằng bao nhiêu?||What is $\\sum_m\\sum_ne^{-\\pi(m^2+n^2)}$?⟧",
             opts=["{{nails_sum}}", "1.0864", "2", "1"], explain="⟦Bằng $(\\sum e^{-\\pi n^2})^2$ = {{nails_sum}} vì giường đinh tích được.||Equal to $(\\sum e^{-\\pi n^2})^2$ = {{nails_sum}} because the bed of nails factorises.⟧"),
        dict(q="⟦Tại $s=3$, biến đổi của Gauss $e^{-\\pi x^2}$ có độ lớn bao nhiêu?||At $s=3$, what is the magnitude of the transform of the Gaussian $e^{-\\pi x^2}$?⟧",
             opts=["{{gauss_tail}}", "{{sinc_tail}}", "0.0121", "1.2e-05"], explain="⟦$e^{-9\\pi}$ = {{gauss_tail}}, tắt cực nhanh so với sinc ({{sinc_tail}} tại 3.5).||$e^{-9\\pi}$ = {{gauss_tail}}, decaying very fast compared with sinc ({{sinc_tail}} at 3.5).⟧"),
        dict(q="⟦Với $F=\\cos x$ và $\\tau=0.1$, độ lệch $\\bigl|\\int\\tau^{-1}e^{-\\pi x^2/\\tau^2}F-F(0)\\bigr|$ bằng bao nhiêu?||With $F=\\cos x$ and $\\tau=0.1$, what is the deviation $\\bigl|\\int\\tau^{-1}e^{-\\pi x^2/\\tau^2}F-F(0)\\bigr|$?⟧",
             opts=["{{dev_01}}", "{{bound_01}}", "1.0e-02", "0"], explain="⟦Sai lệch thật {{dev_01}} nhỏ hơn cận $\\tau\\max|F'|/\\pi$ = {{bound_01}}.||The actual deviation {{dev_01}} is below the bound $\\tau\\max|F'|/\\pi$ = {{bound_01}}.⟧"),
        dict(q="⟦$-\\int_0^\\infty F'(x)dx$ với $F=e^{-x^2}$ bằng bao nhiêu (kiểm $H'=\\delta$)?||What is $-\\int_0^\\infty F'(x)dx$ for $F=e^{-x^2}$ (checking $H'=\\delta$)?⟧",
             opts=["{{hp_exact}}", "0", "0.5", "2"], explain="⟦Bằng $F(0)$ = {{hp_exact}}.||Equal to $F(0)$ = {{hp_exact}}.⟧"),
        dict(q="⟦Với dãy Lorentz $\\tau=0.01$ cho $H'$, $\\int H'_\\tau F$ ($F=e^{-x^2}$) gần bằng bao nhiêu?||With the Lorentzian sequence $\\tau=0.01$ for $H'$, what is $\\int H'_\\tau F$ ($F=e^{-x^2}$), approximately?⟧",
             opts=["{{hp_2}}", "{{hp_1}}", "0.5", "1.0100"], explain="⟦Hội tụ chậm về $F(0)=1$: {{hp_1}} ($\\tau=0.1$), {{hp_2}} ($\\tau=0.01$).||Slowly convergent to $F(0)=1$: {{hp_1}} ($\\tau=0.1$), {{hp_2}} ($\\tau=0.01$).⟧"),
        dict(q="⟦Diện tích của một điểm cao 1 trên lưới bước $10^{-6}$ (hàm rỗng) bằng bao nhiêu?||What is the area of a single point of height 1 on a grid of step $10^{-6}$ (a null function)?⟧",
             opts=["{{null_2}}", "1", "0.001", "0.5"], explain="⟦Bằng bước lưới, tiến về 0: {{null_1}} với $10^{-3}$, {{null_2}} với $10^{-6}$.||Equal to the grid step, tending to 0: {{null_1}} for $10^{-3}$, {{null_2}} for $10^{-6}$.⟧"),
        dict(q="⟦Vì sao \"$\\delta(x)$ bằng vô cùng tại 0\" là cách nói sai?||Why is \"$\\delta(x)$ equals infinity at 0\" a misleading statement?⟧",
             opts=["⟦Vì $\\delta$ không phải hàm; chỉ tích phân của nó có nghĩa||Because $\\delta$ is not a function; only its integrals have meaning⟧",
                   "⟦Vì $\\delta$ thật ra hữu hạn, chỉ rất lớn, và bằng $\\tau^{-1}$ với $\\tau$ nhỏ nhất đo được||Because $\\delta$ is actually finite, only very large, equal to $\\tau^{-1}$ for the smallest $\\tau$ that can be measured⟧",
                   "⟦Vì $\\delta(0)$ bằng 0 theo quy ước của Dirac để giữ tính chẵn của xung||Because $\\delta(0)$ equals 0 by Dirac's convention to preserve the evenness of the impulse⟧",
                   "⟦Vì tích phân của $\\delta$ trên toàn trục bằng vô cùng chứ không bằng 1||Because the integral of $\\delta$ over the whole axis is infinite rather than 1⟧"],
             explain="⟦Bracewell, tr. 74 đến 75: ký hiệu xung không biểu diễn một hàm; tích phân chỉ có nghĩa khi nêu quy ước diễn giải qua dãy xung.||Bracewell, pp. 74 to 75: the impulse symbol does not represent a function; the integral has no meaning until a convention of interpretation through pulse sequences is declared.⟧"),
        dict(q="⟦\"Đạo hàm của bậc thang là xung\" nên hiểu thế nào?||How should \"the derivative of the step is the impulse\" be understood?⟧",
             opts=["⟦Đạo hàm của dãy hàm khả vi tiến về $H$ là một dãy xác định $\\delta$||The derivatives of a sequence of differentiable functions approaching $H$ form a defining sequence for $\\delta$⟧",
                   "⟦Đạo hàm của $H$ tại 0 tồn tại và bằng vô cùng theo nghĩa giải tích thông thường||The derivative of $H$ at 0 exists and equals infinity in the ordinary analytic sense⟧",
                   "⟦$H$ khả vi ở mọi điểm trừ gốc nên đạo hàm là 0 khắp nơi, và $\\delta$ chỉ thêm giá trị tại gốc||$H$ is differentiable everywhere except the origin so the derivative is 0 everywhere and $\\delta$ only adds the value at the origin⟧",
                   "⟦Đạo hàm là hàm chữ nhật có diện tích 1 và độ rộng đúng bằng 0||The derivative is a rectangular function of area 1 and width exactly 0⟧"],
             explain="⟦Bracewell, tr. 77: đó là dấu tắt; các hàm dốc-bậc thang khả vi tiến về $H$ và đạo hàm của chúng, diện tích 1, là dãy xung đơn vị.||Bracewell, p. 77: it is shorthand; the differentiable ramp-step functions tend to $H$ and their derivatives, of area 1, are unit-impulse sequences.⟧"),
        dict(q="⟦Vì sao đáp ứng của mạch thông thấp dần không phụ thuộc dạng xung vào khi xung ngắn dần?||Why does a low-pass circuit's response gradually stop depending on the input pulse shape as the pulse shortens?⟧",
             opts=["⟦Thành phần tần số cao phân biệt các xung gần như không gây đáp ứng||The high-frequency components that distinguish the pulses produce negligible response⟧",
                   "⟦Vì mạch thông thấp bù đủ năng lượng để san bằng mọi khác biệt của xung vào||Because a low-pass circuit stores enough energy to flatten every difference in the input pulse⟧",
                   "⟦Vì các xung ngắn hơn làm mạch chuyển sang chế độ tuyến tính mà xung dài không có||Because shorter pulses drive the circuit into a linear regime that longer pulses do not reach⟧",
                   "⟦Vì độ rộng xung nhỏ hơn hằng số thời gian làm hàm truyền đạt đổi theo dạng xung||Because a pulse width below the time constant changes the transfer function according to the pulse shape⟧"],
             explain="⟦Bracewell, tr. 75: đáp ứng chỉ còn phụ thuộc mạch, không phụ thuộc dạng xung, vì tần số cao bị loại; số đo: độ chênh {{spread_001}} khi $\\tau=0.01$.||Bracewell, p. 75: the response then depends only on the circuit because high frequencies are rejected; measured spread {{spread_001}} for $\\tau=0.01$.⟧"),
        dict(q="⟦Vì sao $\\text{III}$ vừa lấy mẫu vừa tạo tuần hoàn?||Why does $\\text{III}$ both sample and generate periodicity?⟧",
             opts=["⟦Vì nó là biến đổi Fourier của chính nó||Because it is its own Fourier transform⟧",
                   "⟦Vì các xung của nó cách đều nên mọi phép nhân hay chập với nó đều dịch hàm đi một chu kỳ||Because its impulses are equally spaced, so any multiplication or convolution with it shifts the function by one period⟧",
                   "⟦Vì $\\text{III}$ là tổng vô hạn các hàm chẵn nên vừa đối xứng vừa tuần hoàn||Because $\\text{III}$ is an infinite sum of even functions so it is both symmetric and periodic⟧",
                   "⟦Vì lấy mẫu và tuần hoàn là cùng một phép tính viết theo hai ký hiệu khác nhau||Because sampling and periodicity are the same calculation written in two different notations⟧"],
             explain="⟦Bracewell, tr. 83: tính hai mặt không ngẫu nhiên, liên quan tới việc $\\text{III}$ tự biến đổi (trong giới hạn); vế Poisson {{shah_lhs}} = {{shah_rhs}}.||Bracewell, p. 83: the twofold character is no accident but is connected with $\\text{III}$ being its own Fourier transform (in the limit); Poisson sides {{shah_lhs}} = {{shah_rhs}}.⟧"),
        dict(q="⟦Hàm rỗng là gì?||What is a null function?⟧",
             opts=["⟦Hàm có $\\int_a^bf\\,dx=0$ với mọi $a,b$, và biến đổi Fourier bằng 0||A function with $\\int_a^bf\\,dx=0$ for all $a,b$, whose Fourier transform is zero⟧",
                   "⟦Hàm đồng nhất bằng 0 ở mọi điểm, kể cả tại gốc tọa độ||A function identically zero at every point, including at the origin⟧",
                   "⟦Hàm có tích phân toàn trục bằng 0 nhưng có thể khác 0 trên các đoạn con||A function whose whole-axis integral is zero but which may be nonzero on subintervals⟧",
                   "⟦Hàm có đạo hàm bằng 0 ở mọi điểm liên tục của nó||A function whose derivative is zero at every point of continuity⟧"],
             explain="⟦Bracewell, tr. 87: $f$ rỗng nếu $\\int_a^bf=0$ với mọi $a,b$; hai hàm cùng biến đổi khác nhau bởi một hàm rỗng (Lerch).||Bracewell, p. 87: $f$ is null if $\\int_a^bf=0$ for all $a,b$; two functions with the same transform differ by a null function (Lerch).⟧"),
        dict(q="⟦Hàm suy rộng, theo Bracewell, thực chất là gì?||What is a generalized function, in essence, according to Bracewell?⟧",
             opts=["⟦Lớp các dãy chính quy của hàm trơn tuyệt đối tương đương nhau||The class of all equivalent regular sequences of particularly well-behaved functions⟧",
                   "⟦Một hàm thường nhận giá trị vô cùng tại một số điểm rời rạc cho trước||An ordinary function taking infinite values at a given set of discrete points⟧",
                   "⟦Một hàm có đạo hàm tại mọi điểm gián đoạn, đạt được nhờ đổi giá trị tại điểm đó||A function with a derivative at every discontinuity, obtained by changing its value there⟧",
                   "⟦Một chuỗi số thực hội tụ, đại diện cho giá trị giới hạn của một tích phân||A convergent sequence of real numbers representing the limit value of an integral⟧"],
             explain="⟦Bracewell, tr. 95: hàm suy rộng là lớp mọi dãy chính quy tương đương; bản thân không phải một hàm.||Bracewell, p. 95: a generalized function is the class of all equivalent regular sequences; it is itself not a function.⟧"),
        dict(q="⟦Đạo hàm của hàm suy rộng $p$ được định nghĩa thế nào?||How is the derivative of a generalized function $p$ defined?⟧",
             opts=["$\\int p'F\\,dx=-\\int pF'\\,dx$ ⟦bằng tích phân từng phần||by integration by parts⟧",
                   "$\\int p'F\\,dx=\\int pF'\\,dx$ ⟦vì đạo hàm chuyển nguyên vẹn sang hàm thử||because the derivative moves intact onto the test function⟧",
                   "$p'=\\lim\\frac{p(x+h)-p(x)}{h}$ ⟦tại mọi $x$ mà giới hạn tồn tại||at every $x$ where the limit exists⟧",
                   "$p'(x)=p(x)\\cdot\\delta(x)$ ⟦vì đạo hàm của hàm suy rộng luôn tập trung tại gốc||because the derivative of a generalized function is always concentrated at the origin⟧"],
             explain="⟦Bracewell, tr. 97: dùng tích phân từng phần; vì $F$ trơn tuyệt đối nên có đạo hàm mọi cấp.||Bracewell, p. 97: integration by parts; since $F$ is well-behaved it has derivatives of every order.⟧"),
        dict(q="⟦Vì sao $H'=\\delta$ đúng dù $H$ không có đạo hàm tại 0?||Why is $H'=\\delta$ valid although $H$ has no derivative at 0?⟧",
             opts=["⟦Vì $\\int H'F=-\\int HF'=F(0)$ với mọi hàm thử $F$||Because $\\int H'F=-\\int HF'=F(0)$ for every test function $F$⟧",
                   "⟦Vì $H$ liên tục tại 0 sau khi gán $H(0)=\\tfrac12$ nên đạo hàm tại 0 tồn tại và bằng vô cùng||Because $H$ becomes continuous at 0 after assigning $H(0)=\\tfrac12$, so the derivative exists there and is infinite⟧",
                   "⟦Vì đạo hàm trái và đạo hàm phải của $H$ tại 0 bằng nhau khi lấy giới hạn theo dãy chữ nhật||Because the left and right derivatives of $H$ at 0 agree when taken along a rectangular sequence⟧",
                   "⟦Vì $\\delta$ được định nghĩa là đạo hàm của $H$ nên khẳng định đúng theo định nghĩa||Because $\\delta$ is defined as the derivative of $H$, so the claim is true by definition⟧"],
             explain="⟦Bracewell, tr. 98: $\\int H'F\\,dx=-\\int_0^\\infty F'dx=F(0)$ và $\\int\\delta F=F(0)$; số đo {{hp_exact}}.||Bracewell, p. 98: $\\int H'F\\,dx=-\\int_0^\\infty F'dx=F(0)$ and $\\int\\delta F=F(0)$; measured {{hp_exact}}.⟧"),
        dict(q="⟦Đối với $\\text{III}(ax)$, biểu thức nào đúng?||For $\\text{III}(ax)$, which expression is correct?⟧",
             opts=["$|a|^{-1}\\sum\\delta(x-n/a)$", "$\\sum\\delta(x-n/a)$ ⟦vì nén thang không đổi cường độ mỗi xung||since compressing the scale does not change the strength of each impulse⟧",
                   "$|a|\\sum\\delta(x-n/a)$ ⟦vì nén thang làm xung mạnh hơn cùng hệ số||since compression makes the impulses stronger by the same factor⟧",
                   "$\\sum\\delta(x-na)$ ⟦vì $a$ nhân trực tiếp vào khoảng cách các xung||since $a$ multiplies the impulse spacing directly⟧"],
             explain="⟦Bracewell, tr. 83: nén thang làm cường độ giảm $|a|$ lần; đây là cái bẫy quen thuộc với sinh viên.||Bracewell, p. 83: compressing the scale reduces the strength by $|a|$; a known trap for students.⟧"),
    ],
    nb=[
        ("md", """## 1. ⟦Xung ngắn và đáp ứng mạch RC||Brief pulses and the RC circuit response⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Đáp ứng của mạch RC có thật sự thôi phụ thuộc dạng xung vào khi xung ngắn dần, và dãy tích phân của xung chữ nhật có tiến về bậc thang không? Ta tính tích chập số (cách A) và so với công thức giải tích của xung chữ nhật (cách B).||Does the RC circuit's response really stop depending on the pulse shape as the pulse shortens, and does the sequence of integrals of the rectangle tend to the step? We compute numerical convolutions (method A) and compare with the analytic formula for the rectangle (method B).⟧"""),
        ("code", r'''from scipy import integrate, special
trap = getattr(np, "trapezoid", None) or np.trapz

# ⟦Mạch RC với RC = 1: h(t) = e^{-t}H(t). Ba xung diện tích 1 rộng τ||RC circuit with RC = 1: h(t) = e^{-t}H(t). Three unit-area pulses of width τ⟧
dtc = 1e-4; tt = np.arange(0, 8, dtc)
h_rc = np.exp(-tt)
def pulses(tau):
    n = max(int(round(tau/dtc)), 4); p_rect = np.ones(n)/(n*dtc)
    x = (np.arange(n) + 0.5)/n; p_tri = (1 - np.abs(2*x - 1)); p_tri = p_tri/(np.sum(p_tri)*dtc)
    p_two = np.zeros(n); k = max(n//8, 1); p_two[:k] = 1; p_two[-k:] = 1; p_two = p_two/(np.sum(p_two)*dtc)
    return p_rect, p_tri, p_two
spreads = {}
for tau, tag in ((0.5, "05"), (0.1, "01"), (0.01, "001")):
    ys = []
    for p in pulses(tau):
        y = np.convolve(p, h_rc)[:len(tt)]*dtc
        ys.append(y[int(1/dtc)])
    spreads[tag] = max(ys) - min(ys)
    # ⟦cách B: xung chữ nhật có công thức đóng y(t) = (e^{τ} − 1)e^{-t}/τ||method B: the rectangle has a closed form y(t) = (e^{τ} − 1)e^{-t}/τ⟧
    assert abs(ys[0] - (np.exp(tau) - 1)*np.exp(-1)/tau) < 5e-4
    report(f"spread_{tag}", spreads[tag], ".4f")
assert spreads["001"] < spreads["01"] < spreads["05"]

# ⟦Tích phân của xung chữ nhật → bậc thang. Cách A: cộng dồn số; cách B: hàm dốc-bậc thang||Integral of the rectangle → the step. Method A: numerical cumulative sum; method B: the ramp-step function⟧
xs = np.linspace(-1, 1, 200001)
for tau, tag in ((0.5, "t05"), (0.1, "t01")):
    pulse = np.where(np.abs(xs) < tau/2, 1/tau, 0.0)
    cum = np.concatenate([[0], np.cumsum((pulse[1:] + pulse[:-1])/2*np.diff(xs))])
    ramp = np.clip(xs/tau + 0.5, 0, 1)
    assert np.max(np.abs(cum - ramp)) < 1e-4
    for xv, key in ((0.1, f"step_x01_{tag}"), (-0.1, f"step_xm01_{tag}")):
        report(key, np.interp(xv, xs, cum), ".4f")'''),
        ("code", r'''tau = 0.5
plt.figure(figsize=(8, 3.3))
for tau, c in ((0.5, "tab:orange"), (0.1, "tab:blue"), (0.01, "tab:red")):
    ys = [np.convolve(p, h_rc)[:len(tt)]*dtc for p in pulses(tau)]
    plt.plot(tt[:30000], ys[0][:30000], color=c, label=f"τ = {tau}")
plt.plot(tt[:30000], h_rc[:30000], "k--", lw=0.8, label="h(t)")
plt.xlabel("t"); plt.legend(); plt.tight_layout(); plt.show()''', dict(fig="rc_pulses", cap="⟦Hình 1. Đáp ứng của mạch RC với xung chữ nhật diện tích 1 rộng τ: khi τ giảm, đường cong (màu) áp sát đáp ứng xung h(t) = e^{−t} (nét đứt).||Figure 1. The RC circuit's response to a unit-area rectangular pulse of width τ: as τ decreases the curve (coloured) approaches the impulse response h(t) = e^{−t} (dashed).⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Độ chênh giữa ba đáp ứng (chữ nhật, tam giác, hai xung nhỏ) tại $t=1$ là {{spread_05}} với $\\tau=0.5$, {{spread_01}} với $\\tau=0.1$ và {{spread_001}} với $\\tau=0.01$, giảm đều: đáp ứng tiến về $h(t)$. Tích phân của xung chữ nhật tại $x=0.1$ cho {{step_x01_t05}} ($\\tau=0.5$) và {{step_x01_t01}} ($\\tau=0.1$), tại $x=-0.1$ cho {{step_xm01_t05}} và {{step_xm01_t01}}: tiến về bậc thang $H$.||The spread among the three responses (rectangle, triangle, two small pulses) at $t=1$ is {{spread_05}} for $\\tau=0.5$, {{spread_01}} for $\\tau=0.1$ and {{spread_001}} for $\\tau=0.01$, falling steadily: the response tends to $h(t)$. The integral of the rectangle at $x=0.1$ gives {{step_x01_t05}} ($\\tau=0.5$) and {{step_x01_t01}} ($\\tau=0.1$), and at $x=-0.1$ gives {{step_xm01_t05}} and {{step_xm01_t01}}: tending to the step $H$.⟧"""),
        ("md", """## 2. ⟦Tính chất sàng với nhiều dạng xung||Sifting with many pulse shapes⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Mọi dạng xung có tiến về $f(0)$ không, dạng nào lệch khi $\\tau$ chưa nhỏ, tỉ lệ $\\delta(ax)$, và cái bẫy $x\\delta(x)$? Mỗi dạng tính bằng tích phân số (cách A) và công thức đóng (cách B).||Do all pulse shapes tend to $f(0)$, which one is off while $\\tau$ is not small, what about the scaling $\\delta(ax)$ and the trap $x\\delta(x)$? Each shape is computed by numerical integration (method A) and a closed form (method B).⟧"""),
        ("code", r'''f = lambda x: np.cos(x) + 0.5*np.sin(2*x)                      # ⟦f(0) = 1, f'(0) = 1, f''(0) = −1||f(0) = 1, f'(0) = 1, f''(0) = −1⟧
def q(fun, a, b, pts=None): return integrate.quad(fun, a, b, points=pts, limit=800)[0]
def sift(tau):
    out = {}
    out["rc"] = (q(lambda x: f(x)/tau, -tau/2, tau/2), 2*np.sin(tau/2)/tau)
    out["rl"] = (q(lambda x: f(x)/tau, 0, tau), (np.sin(tau) + 0.25*(1 - np.cos(2*tau))*2/2)/tau)
    out["g"] = (q(lambda x: f(x)*np.exp(-np.pi*x**2/tau**2)/tau, -12*tau, 12*tau), np.exp(-tau**2/(4*np.pi)))
    out["t"] = (q(lambda x: f(x)*(1 - abs(x)/tau)/tau, -tau, tau, [0]), 2*(1 - np.cos(tau))/tau**2)
    xx = np.arange(-100, 100, 5e-4)
    out["s"] = (trap(f(xx)*np.sinc(xx/tau)/tau, xx), 1.0)
    out["l"] = (q(lambda x: np.cos(x)*(tau/np.pi)/(x**2 + tau**2), -np.inf, np.inf) if False else 2*integrate.quad(lambda x: (tau/np.pi)/(x**2 + tau**2), 0, np.inf, weight="cos", wvar=1)[0], np.exp(-tau))
    return out
for tau, tag in ((0.1, "01"), (0.01, "001")):
    for shape, (num_, ex_) in sift(tau).items():
        tol = 5e-3 if shape == "s" else 1e-8
        if shape == "rl": ex_ = (np.sin(tau) + 0.5*(1 - np.cos(2*tau))/2)/tau        # ⟦công thức đóng của cạnh trái||closed form of the left edge⟧
        assert abs(num_ - ex_) < tol, (shape, tau, num_, ex_)
        report(f"sift_{shape}_{tag}", num_, ".4f")

# ⟦Chỗ nhảy: f = e^{-x}H(x) với dãy đặt giữa và dãy cạnh trái||At a jump: f = e^{-x}H(x) with the centred and the left-edge sequences⟧
fj = lambda x: np.exp(-x)*(x > 0)
tj = 1e-4
jm = q(lambda x: fj(x)/tj, -tj/2, tj/2, [0]); jl = q(lambda x: fj(x)/tj, 0, tj)
assert abs(jm - 0.5) < 1e-3 and abs(jl - 1) < 1e-3
report("jump_mid", jm, ".2f"); report("jump_left", jl, ".2f")

# ⟦Tỉ lệ δ(3x)||Scaling δ(3x)⟧
tt3 = 0.01
sc = q(lambda x: f(x)/tt3, -tt3/6, tt3/6)
assert abs(sc - 1/3) < 1e-4
report("scale_3", sc, ".4f")

# ⟦x·δ(x): cực đại của x τ^{-1} Π(x/τ) vẫn là 1/2||x·δ(x): the maximum of x τ^{-1} Π(x/τ) stays 1/2⟧
for tau in (0.1, 0.001):
    xg = np.linspace(-tau, tau, 100001); v = np.where(np.abs(xg) < tau/2, xg/tau, 0.0)
    assert abs(v.max() - 0.5) < 1e-4 and abs(v.min() + 0.5) < 1e-4
report("xd_max", 0.5, ".2f")

# ⟦f(x)δ(x) = f(0)δ(x): kiểm với hàm thử g = e^{-x²}||f(x)δ(x) = f(0)δ(x): checked with the test function g = e^{-x²}⟧
fg = q(lambda x: f(x)*np.exp(-x**2)*np.exp(-np.pi*x**2/0.01**2)/0.01, -0.12, 0.12)
assert abs(fg - 1) < 1e-3
report("fg_sift", fg, ".4f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Bảng sàng ($\\tau=0.1$ / $\\tau=0.01$): chữ nhật giữa {{sift_rc_01}} / {{sift_rc_001}}, cạnh trái {{sift_rl_01}} / {{sift_rl_001}}, Gauss {{sift_g_01}} / {{sift_g_001}}, tam giác {{sift_t_01}} / {{sift_t_001}}, sinc {{sift_s_01}} / {{sift_s_001}}, Lorentz {{sift_l_01}} / {{sift_l_001}}: cả sáu tiến về $f(0)=1$, dạng cạnh trái chậm hơn vì nó sàng bên phải. Tại chỗ nhảy, dãy giữa cho {{jump_mid}} và dãy cạnh trái cho {{jump_left}}. $\\delta(3x)$ cho {{scale_3}}. Cực đại của $x\\tau^{-1}\\Pi$ là {{xd_max}} với mọi $\\tau$. Phép kiểm $f\\delta g$ cho {{fg_sift}}.||The sifting table ($\\tau=0.1$ / $\\tau=0.01$): centred rectangle {{sift_rc_01}} / {{sift_rc_001}}, left edge {{sift_rl_01}} / {{sift_rl_001}}, Gaussian {{sift_g_01}} / {{sift_g_001}}, triangle {{sift_t_01}} / {{sift_t_001}}, sinc {{sift_s_01}} / {{sift_s_001}}, Lorentzian {{sift_l_01}} / {{sift_l_001}}: all six tend to $f(0)=1$, the left-edge one more slowly because it sifts on the right. At the jump, the centred sequence gives {{jump_mid}} and the left-edge sequence gives {{jump_left}}. $\\delta(3x)$ gives {{scale_3}}. The maximum of $x\\tau^{-1}\\Pi$ is {{xd_max}} for every $\\tau$. The $f\\delta g$ check gives {{fg_sift}}.⟧"""),
        ("md", """## 3. ⟦Shah, tổng Poisson và giường đinh||Shah, Poisson summation and the bed of nails⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Lấy mẫu và nhân bản bằng shah cho số bao nhiêu, cái bẫy $X^{-1}\\text{III}(x/X)$ là gì, và shah có thật tự biến đổi (tổng Poisson $\\sum f(n)=\\sum F(k)$)? Ta tính bằng hai cách: tổng trực tiếp và chuỗi Fourier.||What numbers do sampling and replication by shah give, what is the $X^{-1}\\text{III}(x/X)$ trap, and is shah really self-transforming (Poisson summation $\\sum f(n)=\\sum F(k)$)? We compute two ways: the direct sum and the Fourier series.⟧"""),
        ("code", r'''N_ = np.arange(-40, 41)
g = lambda x: np.exp(-np.pi*x**2)
report("X_sum_1", np.sum(g(N_)), ".4f")
for X, tag in ((0.5, "05"),):
    n_ = np.arange(-200, 201)
    s_ = np.sum(g(n_*X))
    assert abs(X*s_ - 1) < 2e-5                      # ⟦sai số 2e^{−4π} theo Poisson||error 2e^{−4π} by Poisson⟧
    report(f"X_sum_{tag}", s_, ".4f"); report(f"X_riem_{tag}", X*s_, ".4f")

# ⟦Nhân bản (III*f)(0.5): tổng trực tiếp so với chuỗi Fourier Σ (−1)^k e^{−πk²}||Replication (III*f)(0.5): direct sum versus the Fourier series Σ (−1)^k e^{−πk²}⟧
rep_direct = np.sum(g(0.5 - N_))
rep_series = np.sum((-1.0)**N_*np.exp(-np.pi*N_**2))
assert abs(rep_direct - rep_series) < 1e-12
report("rep_05", rep_direct, ".4f")

# ⟦Tổng Poisson: f = e^{−πx²/4}, F = 2e^{−4πs²}||Poisson summation: f = e^{−πx²/4}, F = 2e^{−4πs²}⟧
lhs = np.sum(np.exp(-np.pi*N_**2/4)); rhs = np.sum(2*np.exp(-4*np.pi*N_**2))
assert abs(lhs - rhs) < 1e-12
report("shah_lhs", lhs, ".6f"); report("shah_rhs", rhs, ".6f")

# ⟦Giường đinh: Σ_m Σ_n e^{−π(m²+n²)} = (Σ e^{−πn²})²||Bed of nails: Σ_m Σ_n e^{−π(m²+n²)} = (Σ e^{−πn²})²⟧
mm, nn = np.meshgrid(N_[15:66], N_[15:66])
nails = np.sum(np.exp(-np.pi*(mm**2 + nn**2)))
assert abs(nails - np.sum(g(N_))**2) < 1e-12
report("nails_sum", nails, ".4f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦$\\sum f(n)$ với Gauss là {{X_sum_1}}; với khoảng cách 0.5 tổng không nhân $X$ là {{X_sum_05}} (gấp đôi), còn $X\\sum f(nX)$ = {{X_riem_05}} là diện tích. $(\\text{III}*f)(0.5)$ = {{rep_05}} bằng cả tổng trực tiếp và chuỗi Fourier. Tổng Poisson: {{shah_lhs}} = {{shah_rhs}}: shah tự biến đổi. Giường đinh: {{nails_sum}}, bằng bình phương của {{X_sum_1}}.||$\\sum f(n)$ for the Gaussian is {{X_sum_1}}; at spacing 0.5 the sum without the factor $X$ is {{X_sum_05}} (twice too large), while $X\\sum f(nX)$ = {{X_riem_05}} is the area. $(\\text{III}*f)(0.5)$ = {{rep_05}} by both the direct sum and the Fourier series. Poisson summation: {{shah_lhs}} = {{shah_rhs}}: shah is self-transforming. The bed of nails: {{nails_sum}}, the square of {{X_sum_1}}.⟧"""),
        ("md", """## 4. ⟦Cặp xung, đạo hàm của $\\delta$ và hàm rỗng||Impulse pairs, derivatives of $\\delta$ and null functions⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Cặp xung chẵn có biến đổi cosin, sai phân bằng $2\\nu*$, và các tích phân $\\int\\delta'f$, $\\int x\\delta'$, $\\int x^2\\delta''$, $\\int\\delta''f$ có bằng $-f'(0)$, $-1$, $2$, $f''(0)$? Ta dùng dãy Gauss và so sánh với tích phân từng phần.||Does the even pair have a cosine transform, is the difference $2\\nu*$, and do $\\int\\delta'f$, $\\int x\\delta'$, $\\int x^2\\delta''$, $\\int\\delta''f$ equal $-f'(0)$, $-1$, $2$, $f''(0)$? We use a Gaussian sequence and compare with integration by parts.⟧"""),
        ("code", r'''# ⟦Cặp xung chẵn: biến đổi là cos(πs); μ*f tại 0||Even pair: the transform is cos(πs); μ*f at 0⟧
s0 = 0.3
mu_ft = 0.5*np.exp(-2j*np.pi*s0*0.5) + 0.5*np.exp(-2j*np.pi*s0*(-0.5))
assert abs(mu_ft - np.cos(np.pi*s0)) < 1e-15
report("mu_ft", mu_ft.real, ".4f")
report("mu_conv", 0.5*g(0.5) + 0.5*g(-0.5), ".4f")
assert abs(0.5*g(0.5) + 0.5*g(-0.5) - np.exp(-np.pi/4)) < 1e-15

# ⟦Sai phân: Δf = f(x+½) − f(x−½) = 2ν*f. Kiểm bằng biến đổi Fourier||Difference: Δf = f(x+½) − f(x−½) = 2ν*f. Check via the Fourier transform⟧
report("fd_0", np.sin(0.5) - np.sin(-0.5), ".4f")
dfun = lambda x: g(x + 0.5) - g(x - 0.5)
fd_ft = integrate.quad(lambda x: dfun(x)*np.sin(2*np.pi*x*s0), -12, 12, limit=400)[0]        # ⟦phần ảo (dấu −)||imaginary part (sign −)⟧
assert abs(abs(fd_ft) - 2*np.sin(np.pi*s0)*np.exp(-np.pi*s0**2)) < 1e-9
report("fd_ft", abs(fd_ft), ".4f")

# ⟦δ' bằng dãy Gauss τ = 0.05: ∫δ'f = −f'(0); so với −∫δ f'||δ' by the Gaussian sequence τ = 0.05: ∫δ'f = −f'(0); versus −∫δ f'⟧
tau = 0.05
d0 = lambda x: np.exp(-np.pi*x**2/tau**2)/tau
d1 = lambda x: -2*np.pi*x/tau**2*d0(x)
d2 = lambda x: (-2*np.pi/tau**2 + (2*np.pi*x/tau**2)**2)*d0(x)
fp = lambda x: -np.sin(x) + np.cos(2*x); fpp = lambda x: -np.cos(x) - 2*np.sin(2*x)
L = 12*tau
i1 = q(lambda x: d1(x)*f(x), -L, L); i2 = -q(lambda x: d0(x)*fp(x), -L, L)
assert abs(i1 - i2) < 1e-9 and abs(i1 + 1) < 5e-3
report("dprime_sift", i1, ".4f"); report("ibp_diff", abs(i1 - i2), ".1e")
xd = q(lambda x: x*d1(x), -L, L); assert abs(xd + 1) < 1e-9
x2 = q(lambda x: x**2*d2(x), -L, L); assert abs(x2 - 2) < 1e-9
d2s = q(lambda x: d2(x)*f(x), -L, L); assert abs(d2s + 1) < 5e-3
report("x_dprime", xd, ".2f"); report("x2_d2", x2, ".2f"); report("d2_sift", d2s, ".3f")

# ⟦∫|δ'_τ| = 2/τ||∫|δ'_τ| = 2/τ⟧
for tau_, key in ((0.1, "l1_01"), (0.01, "l1_001")):
    d0_ = lambda x: np.exp(-np.pi*x**2/tau_**2)/tau_
    d1_ = lambda x: -2*np.pi*x/tau_**2*d0_(x)
    v = q(lambda x: abs(d1_(x)), -12*tau_, 12*tau_, [0])
    assert abs(v - 2/tau_) < 1e-6
    report(key, v, ".0f")

# ⟦Hàm rỗng: diện tích của một điểm cao 1||Null function: the area of a single point of height 1⟧
for dxn, key in ((1e-3, "null_1"), (1e-6, "null_2")):
    report(key, dxn*1.0, ".0e")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Cặp chẵn: biến đổi tại 0.3 là {{mu_ft}}, $\\mu*f(0)$ = {{mu_conv}}. Sai phân: $\\Delta\\sin(0)$ = {{fd_0}}, độ lớn biến đổi $\\Delta f$ tại 0.3 là {{fd_ft}}. Với dãy Gauss $\\tau=0.05$: $\\int\\delta'f$ = {{dprime_sift}} (bằng $-\\int\\delta f'$, lệch {{ibp_diff}}), $\\int x\\delta'$ = {{x_dprime}}, $\\int x^2\\delta''$ = {{x2_d2}}, $\\int\\delta''f$ = {{d2_sift}}. $\\int|\\delta'_\\tau|$ = {{l1_01}} và {{l1_001}}, tăng như $2/\\tau$. Hàm rỗng: diện tích {{null_1}} và {{null_2}}.||Even pair: the transform at 0.3 is {{mu_ft}}, $\\mu*f(0)$ = {{mu_conv}}. Difference: $\\Delta\\sin(0)$ = {{fd_0}}, the magnitude of the transform of $\\Delta f$ at 0.3 is {{fd_ft}}. With the Gaussian sequence $\\tau=0.05$: $\\int\\delta'f$ = {{dprime_sift}} (equal to $-\\int\\delta f'$, difference {{ibp_diff}}), $\\int x\\delta'$ = {{x_dprime}}, $\\int x^2\\delta''$ = {{x2_d2}}, $\\int\\delta''f$ = {{d2_sift}}. $\\int|\\delta'_\\tau|$ = {{l1_01}} and {{l1_001}}, growing like $2/\\tau$. Null function: areas {{null_1}} and {{null_2}}.⟧"""),
        ("md", """## 5. ⟦Xung hai chiều và hàm suy rộng||Two-dimensional impulses and generalized functions⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Dãy Gauss hai chiều có thể tích 1, biến đổi của Gauss tắt nhanh thế nào so với sinc, cận sai số của dãy chính quy có đúng, và $H'=\\delta$ qua dãy Lorentz ra sao? Mỗi điều kiểm bằng hai cách.||Does the two-dimensional Gaussian sequence have unit volume, how fast does the Gaussian's transform decay compared with sinc, is the regular-sequence error bound valid, and what does $H'=\\delta$ look like through a Lorentzian sequence? Each is checked two ways.⟧"""),
        ("code", r'''# ⟦Thể tích của dãy Gauss hai chiều τ = 0.1: 2π∫ r·(τ^{-2}e^{−πr²/τ²})dr||Volume of the 2D Gaussian sequence τ = 0.1: 2π∫ r·(τ^{-2}e^{−πr²/τ²})dr⟧
tau2 = 0.1
vol = 2*np.pi*integrate.quad(lambda r: r*np.exp(-np.pi*r**2/tau2**2)/tau2**2, 0, 10*tau2)[0]
assert abs(vol - 1) < 1e-9
report("delta2_vol", vol, ".2f")

# ⟦Độ tắt của biến đổi: Gauss so với sinc||Decay of the transform: Gaussian versus sinc⟧
report("gauss_tail", np.exp(-9*np.pi), ".1e"); report("sinc_tail", abs(np.sinc(3.5)), ".4f")
assert abs(integrate.quad(lambda x: np.exp(-np.pi*x**2)*np.cos(2*np.pi*3*x), -10, 10)[0] - np.exp(-9*np.pi)) < 1e-9

# ⟦Cận sai số của dãy chính quy, F = cos x, τ = 0.1||Error bound of a regular sequence, F = cos x, τ = 0.1⟧
tau = 0.1
dev = 1 - integrate.quad(lambda x: np.cos(x)*np.exp(-np.pi*x**2/tau**2)/tau, -12*tau, 12*tau)[0]
assert abs(dev - (1 - np.exp(-tau**2/(4*np.pi)))) < 1e-9 and dev < tau/np.pi
report("dev_01", dev, ".1e"); report("bound_01", tau/np.pi, ".1e")

# ⟦H' = δ: −∫_0^∞ F' = F(0), và dãy Lorentz (đạo hàm của ½ + arctan(x/τ)/π)||H' = δ: −∫_0^∞ F' = F(0), and the Lorentzian sequence (derivative of ½ + arctan(x/τ)/π)⟧
Fh = lambda x: np.exp(-x**2); Fhp = lambda x: -2*x*np.exp(-x**2)
hp_exact = -integrate.quad(Fhp, 0, np.inf)[0]
assert abs(hp_exact - 1) < 1e-9
report("hp_exact", hp_exact, ".2f")
for t_, key in ((0.1, "hp_1"), (0.01, "hp_2")):
    v = integrate.quad(lambda x: (t_/np.pi)/(x**2 + t_**2)*Fh(x), -np.inf, np.inf, limit=400)[0]
    assert abs(v - np.exp(t_**2)*special.erfc(t_)) < 1e-6
    report(key, v, ".4f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Dãy Gauss hai chiều có thể tích {{delta2_vol}}. Biến đổi của Gauss tại 3 chỉ {{gauss_tail}} so với {{sinc_tail}} của sinc tại 3.5: độ trơn của hàm quyết định độ tắt của biến đổi. Sai lệch thật của dãy chính quy là {{dev_01}}, dưới cận {{bound_01}}. $-\\int_0^\\infty F'$ = {{hp_exact}} = $F(0)$, và dãy Lorentz hội tụ chậm: {{hp_1}} ($\\tau=0.1$), {{hp_2}} ($\\tau=0.01$).||The two-dimensional Gaussian sequence has volume {{delta2_vol}}. The Gaussian's transform at 3 is only {{gauss_tail}} against {{sinc_tail}} for sinc at 3.5: smoothness of the function sets the decay of the transform. The actual deviation of the regular sequence is {{dev_01}}, below the bound {{bound_01}}. $-\\int_0^\\infty F'$ = {{hp_exact}} = $F(0)$, and the Lorentzian sequence converges slowly: {{hp_1}} ($\\tau=0.1$), {{hp_2}} ($\\tau=0.01$).⟧"""),
    ],
)
