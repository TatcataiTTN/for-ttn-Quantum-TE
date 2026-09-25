from lib import F, C, UL, OL, TBL


def P(s):
    return "<p>" + s + "</p>"


def Q(q, ans, d1, d2, d3, ex):
    return dict(q=q, opts=[ans, d1, d2, d3], explain=ex)


MOD = dict(
    n=16, slug="relatives-of-ft", part="C", book="B",
    title="⟦Họ hàng của biến đổi Fourier: nhiều chiều, Hankel, Mellin, z, Abel, Radon, Hilbert, phân số||Relatives of the Fourier transform: multidimensional, Hankel, Mellin, z, Abel, Radon, Hilbert, fractional⟧",
    blurb="⟦Biến đổi Fourier hai và ba chiều, Hankel khi có đối xứng tròn, hạt nhân Fourier, Mellin và z, Abel và Radon (chụp cắt lớp), Hilbert (tín hiệu giải tích, nhân quả) và Fourier phân số (Bracewell, chương 13).||"
          "The Fourier transform in two and three dimensions, Hankel under circular symmetry, Fourier kernels, Mellin and z, Abel and Radon (tomography), Hilbert (analytic signal, causality) and the fractional Fourier transform (Bracewell, chapter 13).⟧",
    src="⟦Bracewell, chương 13, tr. 330–374||Bracewell, chapter 13, pp. 330–374⟧",
    data="⟦Sinh bằng mã: Gauss hai chiều, hình cầu, hàm Bessel, hàm mũ, tín hiệu điều biên và điều tần, và bộ chiếu Radon||Generated in code: 2D Gaussians, a ball, Bessel functions, exponentials, AM and FM signals and Radon projections⟧",
    objectives=[
        "⟦Áp dụng các định lý Fourier hai chiều (xoay, cắt, affine, mômen) và biến đổi ba chiều đối xứng cầu.||Apply the two-dimensional Fourier theorems (rotation, shear, affine, moments) and the spherically symmetric three-dimensional transform.⟧",
        "⟦Dùng biến đổi Hankel bậc 0 và $n$ chiều khi có đối xứng tròn, và hiểu hạt nhân Fourier theo nghĩa rộng qua định lý Hankel.||Use the zero-order and $n$-dimensional Hankel transforms under circular symmetry, and understand Fourier kernels in the broad sense through Hankel's theorem.⟧",
        "⟦Chuyển giữa Laplace, Mellin và z, và dùng tích chuỗi để nhân và chia đa thức z.||Move between Laplace, Mellin and z, and use the serial product to multiply and divide z polynomials.⟧",
        "⟦Tính biến đổi Abel số, dùng vòng Abel-Fourier-Hankel, định lý lát chiếu và chiếu ngược có sửa đổi trong chụp cắt lớp.||Compute the Abel transform numerically and use the Abel-Fourier-Hankel ring, the projection-slice theorem and modified back-projection in tomography.⟧",
        "⟦Xây dựng tín hiệu giải tích bằng biến đổi Hilbert, tìm đường bao và tần số tức thời, dùng nhân quả (cặp Hilbert), và biết biến đổi Fourier phân số.||Build the analytic signal with the Hilbert transform, find the envelope and instantaneous frequency, use causality (Hilbert pairs) and know the fractional Fourier transform.⟧",
    ],
    parts=[
        # ---------------------------------------------------------- PART 1
        dict(
            title="⟦Fourier hai và ba chiều||Two- and three-dimensional Fourier transforms⟧",
            scr=("⟦Ăng ten, thấu kính, cách tử, màn hình và tinh thể đều là hệ hai hay ba chiều; công thức một chiều tổng quát hóa dễ dàng.||Antennas, lenses, gratings, screens and crystals are two- or three-dimensional systems; the one-dimensional formulas generalise readily.⟧",
                 "⟦Nhiều định lý giữ nguyên; thêm các định lý chỉ có ở nhiều chiều: xoay, cắt, affine.||Many theorems carry over; some exist only in several dimensions: rotation, shear, affine.⟧",
                 "⟦Nhiều bài toán có đối xứng, khi đó biến đổi hai và ba chiều thu về biến đổi một chiều.||Many problems have symmetry, whereupon the two- and three-dimensional transforms reduce to one-dimensional ones.⟧"),
            preview=["⟦Biến đổi 2D và tích, chập||The 2D transform, products and convolution⟧", "⟦Xoay, cắt, affine, mômen||Rotation, shear, affine, moments⟧", "⟦Biến đổi 3D||The 3D transform⟧"],
            slides=[
                ("⟦Các họ hàng gần và xa||Close and distant relatives⟧",
                 P(r"⟦Nhiều biến đổi tuyến tính thông dụng liên quan trực tiếp với Fourier hoặc Laplace. Gần nhất là tổng quát hóa lên hai chiều hoặc hơn, và biến đổi Hankel bậc 0 và cao hơn khi có đối xứng. Biến đổi Mellin được soi sáng nhờ biến đổi Laplace và là công cụ xây dựng lý thuyết hạt nhân Fourier. Biến đổi Hilbert trở nên gọn khi xét bằng Fourier, và có mối quan hệ mật thiết: Abel, Fourier và Hankel áp dụng liên tiếp tái tạo hàm ban đầu. Biến đổi Radon là tổng quát hóa của Abel khi bỏ đối xứng tròn, và vòng Abel-Fourier-Hankel tổng quát thành định lý lát chiếu, công cụ suy nghĩ cho tái tạo từ hình chiếu (Bracewell, tr. 329 đến 330).||Many linear transforms in common use have a direct connection with either the Fourier or the Laplace transform. The closest is the generalisation to two or more dimensions, and the Hankel transforms of zero and higher order under symmetry. The Mellin transform is illuminated by the Laplace transform and is the tool by which the theory of Fourier kernels is built. The Hilbert transform simplifies when studied by Fourier, and there is an intimate relationship whereby the Abel, Fourier and Hankel transformations applied in succession regenerate the original function. The Radon transform is a generalisation of the Abel transform when circular symmetry is dropped, and the Abel-Fourier-Hankel cycle generalises to the projection-slice theorem, a thinking tool for reconstruction from projections (Bracewell, pp. 329 to 330).⟧")),
                ("⟦Biến đổi Fourier hai chiều||The two-dimensional Fourier transform⟧",
                 P(r"⟦$F(u,v)=\iint f(x,y)e^{-i2\pi(ux+vy)}dx\,dy$ và nghịch đảo $f=\iint F\,e^{i2\pi(ux+vy)}du\,dv$. Màng căng, ăng ten và dãy ăng ten, thấu kính, cách tử nhiễu xạ, hình ảnh trên màn hình đều là hệ hai chiều. Một hàm tách được $f(x)g(y)$ có biến đổi $F(u)G(v)$; ví dụ Gauss $e^{-\pi(x^2+y^2)}$ tự biến đổi thành $e^{-\pi(u^2+v^2)}$. Số đo bằng tổng trên lưới bước 0.04: tại $(u,v)=(0.5,0.3)$ ta có {{g2_num}}, và công thức {{g2_cf}} lệch {{g2_dev}}. Tích chập hai chiều là $f**g=\iint f(x',y')g(x-x',y-y')dx'dy'$ (một hàm xoay nửa vòng quanh gốc, dịch, nhân, tích phân) (tr. 330 đến 331).||$F(u,v)=\iint f(x,y)e^{-i2\pi(ux+vy)}dx\,dy$ and the inverse $f=\iint F\,e^{i2\pi(ux+vy)}du\,dv$. Stretched membranes, antennas and arrays of antennas, lenses, diffraction gratings and pictures on television screens are two-dimensional systems. A separable function $f(x)g(y)$ has transform $F(u)G(v)$; for example the Gaussian $e^{-\pi(x^2+y^2)}$ transforms into $e^{-\pi(u^2+v^2)}$. Measured by a sum on a grid of step 0.04: at $(u,v)=(0.5,0.3)$ we get {{g2_num}}, and the formula {{g2_cf}} deviates by {{g2_dev}}. The two-dimensional convolution is $f**g=\iint f(x',y')g(x-x',y-y')dx'dy'$ (one function rotated half a turn about the origin, displaced, multiplied and integrated) (pp. 330 to 331).⟧")),
                ("⟦Tích và chập: cách biểu diễn một hàm||Product and convolution: two ways to express a function⟧",
                 P(r"⟦Hình chữ nhật hai chiều $\Pi(x,y)$ (bằng 1 khi $|x|,|y|<\tfrac12$) có hai cách biểu diễn: $\Pi(x,y)=\Pi(x)\Pi(y)$ (tích) và $=[\Pi(x)\delta(y)]*[\Pi(y)\delta(x)]$ (chập của hai thanh vuông góc) (hình 13.2, tr. 331). Điều này giúp nhận ra một hàm là chập, và cho biến đổi $\mathrm{sinc}\,u\,\mathrm{sinc}\,v$. Số đo rời rạc: chập hai chiều của hàng $a$ (5 phần tử) và cột $b$ (4 phần tử) bằng tích ngoài $b\,a^T$, độ lệch {{pc_dev}}, có tổng phần tử bằng $\sum a\sum b$ = {{pc_sum}}.||The two-dimensional rectangle $\Pi(x,y)$ (equal to 1 when $|x|,|y|<\tfrac12$) has two representations: $\Pi(x,y)=\Pi(x)\Pi(y)$ (a product) and $=[\Pi(x)\delta(y)]*[\Pi(y)\delta(x)]$ (a convolution of two perpendicular bars) (Fig. 13.2, p. 331). This helps recognise a function as a convolution and gives the transform $\mathrm{sinc}\,u\,\mathrm{sinc}\,v$. Discrete measurement: the two-dimensional convolution of a row $a$ (5 elements) and a column $b$ (4 elements) equals the outer product $b\,a^T$, deviation {{pc_dev}}, with total sum $\sum a\sum b$ = {{pc_sum}}.⟧")),
                ("⟦Bảng định lý hai chiều||Table of two-dimensional theorems⟧",
                 TBL(["⟦Định lý||Theorem⟧", "$f(x,y)$", "$F(u,v)$"],
                     [["⟦Đồng dạng||Similarity⟧", "$f(ax,by)$", "$\\tfrac1{|ab|}F(\\tfrac ua,\\tfrac vb)$"],
                      ["⟦Dịch||Shift⟧", "$f(x-a,y-b)$", "$e^{-i2\\pi(au+bv)}F$"],
                      ["⟦Chập||Convolution⟧", "$f**g$", "$F\\,G$"],
                      ["⟦Tự tương quan||Autocorrelation⟧", "$f\\star f^*$", "$|F|^2$"],
                      ["⟦Rayleigh||Rayleigh⟧", "$\\iint|f|^2$", "$\\iint|F|^2$"],
                      ["⟦Vi phân||Differentiation⟧", "$\\partial f/\\partial x$", "$i2\\pi uF$"],
                      ["⟦Laplace||Laplacian⟧", "$\\nabla^2f$", "$-4\\pi^2(u^2+v^2)F$"]])
                 + P(r"⟦Các định lý một chiều tổng quát hóa dễ dàng (bảng 13.1, tr. 332 đến 333). Tích phân xác định $\iint f=F(0,0)$; mômen bậc nhất cho trọng tâm $\bar x=-F_u(0,0)/(i2\pi F(0,0))$; mômen bậc hai $\iint x^2f=-F_{uu}(0,0)/4\pi^2$ và $\iint(x^2+y^2)f=-[F_{uu}+F_{vv}](0,0)/4\pi^2$. Với Gauss $e^{-\pi r^2}$: $F(0,0)$ = {{mo_F0}} và $\iint r^2f$ = {{mo_r2}}, bằng cả hai cách (tính trực tiếp và từ đạo hàm của $F$).||The one-dimensional theorems generalise readily (Table 13.1, pp. 332 to 333). The definite integral $\iint f=F(0,0)$; the first moment gives the centre of gravity $\bar x=-F_u(0,0)/(i2\pi F(0,0))$; the second moment $\iint x^2f=-F_{uu}(0,0)/4\pi^2$ and $\iint(x^2+y^2)f=-[F_{uu}+F_{vv}](0,0)/4\pi^2$. For the Gaussian $e^{-\pi r^2}$: $F(0,0)$ = {{mo_F0}} and $\iint r^2f$ = {{mo_r2}}, both ways (direct and from the derivatives of $F$).⟧")),
                ("⟦Định lý xoay và định lý cắt||The rotation and shear theorems⟧",
                 P(r"⟦Xoay: nếu $f$ xoay góc $\theta$ trên mặt phẳng $(x,y)$ thì biến đổi xoay cùng góc, cùng chiều trên mặt phẳng $(u,v)$: $f(x\cos\theta-y\sin\theta,\ x\sin\theta+y\cos\theta)\supset F(u\cos\theta-v\sin\theta,\ u\sin\theta+v\cos\theta)$. Cắt (shear): $f(x+by,y)\supset F(u,v-bu)$: hàm bị cắt thì biến đổi bị cắt cùng mức theo hướng vuông góc (tr. 332 đến 333). Số đo với $f=e^{-\pi(4x^2+y^2/4)}$ xoay $\theta=0.6$ tại $(u,v)=(0.3,0.2)$: hai vế lệch {{rot_dev}}; với Gauss tròn cắt $b=0.5$ tại $(0.4,0.3)$: lệch {{shr_dev}}.||Rotation: if $f$ is rotated through an angle $\theta$ on the $(x,y)$-plane then its transform is rotated through the same angle in the same sense on the $(u,v)$-plane: $f(x\cos\theta-y\sin\theta,\ x\sin\theta+y\cos\theta)\supset F(u\cos\theta-v\sin\theta,\ u\sin\theta+v\cos\theta)$. Shear: $f(x+by,y)\supset F(u,v-bu)$: if the function is sheared its transform is sheared to the same degree in the perpendicular direction (pp. 332 to 333). Measured with $f=e^{-\pi(4x^2+y^2/4)}$ rotated by $\theta=0.6$ at $(u,v)=(0.3,0.2)$: the two sides deviate by {{rot_dev}}; with a circular Gaussian sheared by $b=0.5$ at $(0.4,0.3)$: deviation {{shr_dev}}.⟧")),
                ("⟦Định lý affine||The affine theorem⟧",
                 P(r"⟦Hàm chịu biến đổi affine của mặt phẳng, $f(ax+by+c,\ dx+ey+f)$, có biến đổi $|ae-bd|^{-1}\exp\{i2\pi(ae-bd)^{-1}[(ec-bf)u+(af-cd)v]\}\,F\!\left[\tfrac{eu-dv}{ae-bd},\ \tfrac{-bu+av}{ae-bd}\right]$ (Bracewell và cộng sự, 1993; tr. 333). Nó chứa mọi định lý xoay, cắt, đồng dạng và dịch như trường hợp riêng. Số đo với Gauss không đẳng hướng ($a,b,c,d,e,f=1.2,0.3,0.4,-0.2,0.9,-0.3$) tại $(u,v)=(0.35,-0.2)$: công thức với dấu $+$ trong mũ lệch {{aff_dev}}, còn đổi dấu thành $-$ lệch {{aff_wrong}}: dấu là quan trọng.||A function subjected to an affine transformation of the plane, $f(ax+by+c,\ dx+ey+f)$, has the transform $|ae-bd|^{-1}\exp\{i2\pi(ae-bd)^{-1}[(ec-bf)u+(af-cd)v]\}\,F\!\left[\tfrac{eu-dv}{ae-bd},\ \tfrac{-bu+av}{ae-bd}\right]$ (Bracewell et al., 1993; p. 333). It contains the rotation, shear, similarity and shift theorems as special cases. Measured with an anisotropic Gaussian ($a,b,c,d,e,f=1.2,0.3,0.4,-0.2,0.9,-0.3$) at $(u,v)=(0.35,-0.2)$: the formula with a $+$ sign in the exponent deviates by {{aff_dev}}, while flipping it to $-$ deviates by {{aff_wrong}}: the sign matters.⟧")),
                ("⟦Biến đổi Fourier ba chiều||The three-dimensional Fourier transform||⟧".replace("||⟧", "⟧"),
                 P(r"⟦Ví dụ kinh điển: nhiễu xạ tia X bởi tinh thể: $F(u,v,w)=\iiint f\,e^{-i2\pi(ux+vy+wz)}dx\,dy\,dz$. Ký hiệu vectơ $\mathbf x,\mathbf s$ gọn cho $n$ chiều. Với đối xứng cầu $f=k(r)$: $K(s)=4\pi\int_0^\infty k(r)\,\mathrm{sinc}(2sr)\,r^2dr$, cũng đối ngược. Bảng 13.4: khối cầu $\Pi(r/2)$ (bán kính 1) có biến đổi $\dfrac{\sin2\pi s-2\pi s\cos2\pi s}{2\pi^2s^3}$; giá trị tại 0 là thể tích {{ball_s0}} ($4\pi/3$), tại $s=1$ là {{ball_s1}} ($-1/\pi$), khớp tích phân số {{ball_num}}. Gauss ba chiều $e^{-\pi r^2}$ tự biến đổi, ví dụ tại $s=0.5$: {{g3_s}}. Các cặp tách được $f(x)g(y)h(z)\supset F(u)G(v)H(w)$ sinh thêm nhiều cặp (tr. 340 đến 343).||The classical example: X-ray diffraction by crystals: $F(u,v,w)=\iiint f\,e^{-i2\pi(ux+vy+wz)}dx\,dy\,dz$. Vector notation $\mathbf x,\mathbf s$ is convenient in $n$ dimensions. With spherical symmetry $f=k(r)$: $K(s)=4\pi\int_0^\infty k(r)\,\mathrm{sinc}(2sr)\,r^2dr$, also reciprocal. Table 13.4: the ball $\Pi(r/2)$ (radius 1) has transform $\dfrac{\sin2\pi s-2\pi s\cos2\pi s}{2\pi^2s^3}$; its value at 0 is the volume {{ball_s0}} ($4\pi/3$), at $s=1$ it is {{ball_s1}} ($-1/\pi$), matching the numerical integral {{ball_num}}. The three-dimensional Gaussian $e^{-\pi r^2}$ is self-transforming, for example at $s=0.5$: {{g3_s}}. The separable pairs $f(x)g(y)h(z)\supset F(u)G(v)H(w)$ generate many more pairs (pp. 340 to 343).⟧")),
                ("⟦Các đối xứng trụ và cầu||Cylindrical and spherical symmetry⟧",
                 P(r"⟦Đối xứng tròn quanh trục $z$ ($f$ không phụ thuộc góc): $H(s,w)=2\pi\iint h(r,z)J_0(2\pi sr)e^{-i2\pi wz}r\,dr\,dz$ (Hankel theo $r$, Fourier theo $z$). Đối xứng trụ ($f$ chỉ phụ thuộc $r$): $F(u,v,w)=K(s)\delta(w)$ với $K(s)=2\pi\int k(r)J_0(2\pi sr)r\,dr$: một đường trụ vô hạn có biến đổi là một tấm trong không gian tần số. Bảng 13.4: thanh $2\Pi(x,y)$ có biến đổi $\mathrm{sinc}\,u\,\mathrm{sinc}\,v\,\delta(w)$; tấm $\Pi(x)$ có biến đổi $\mathrm{sinc}\,u\,\delta(v)\delta(w)$; lập phương $\Pi(x,y,z)$ có $\mathrm{sinc}\,u\,\mathrm{sinc}\,v\,\mathrm{sinc}\,w$. Số đo: giá trị lập phương đơn vị tại $(0.5,0.25,0.25)$ bằng tích ba sinc {{cube_val}} (theo hai cách: tích và tổng số đo).||Circular symmetry about the $z$-axis ($f$ independent of angle): $H(s,w)=2\pi\iint h(r,z)J_0(2\pi sr)e^{-i2\pi wz}r\,dr\,dz$ (Hankel in $r$, Fourier in $z$). Cylindrical symmetry ($f$ depending only on $r$): $F(u,v,w)=K(s)\delta(w)$ with $K(s)=2\pi\int k(r)J_0(2\pi sr)r\,dr$: an infinite cylinder has as transform a sheet in frequency space. Table 13.4: the bar $2\Pi(x,y)$ has transform $\mathrm{sinc}\,u\,\mathrm{sinc}\,v\,\delta(w)$; the slab $\Pi(x)$ has $\mathrm{sinc}\,u\,\delta(v)\delta(w)$; the cube $\Pi(x,y,z)$ has $\mathrm{sinc}\,u\,\mathrm{sinc}\,v\,\mathrm{sinc}\,w$. Measured: the unit cube at $(0.5,0.25,0.25)$ equals the product of three sincs {{cube_val}} (two ways: product and a summed measure).⟧")),
                ("⟦Tự kiểm tra phần 1||Self-check, part 1⟧",
                 UL([r"⟦Định lý xoay hai chiều nói gì?||What does the two-dimensional rotation theorem say?⟧",
                     r"⟦Vì sao dấu trong mũ của định lý affine quan trọng?||Why does the sign in the exponent of the affine theorem matter?⟧",
                     r"⟦Biến đổi của khối cầu bán kính 1 tại 0 bằng bao nhiêu?||What is the transform of the unit-radius ball at 0?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: biến đổi xoay cùng góc, cùng chiều; nó quyết định pha tuyến tính do dịch; thể tích $4\\pi/3$.||Hints: the transform rotates through the same angle in the same sense; it sets the linear phase due to shift; the volume $4\\pi/3$.⟧</p>"),
            ]),
        # ---------------------------------------------------------- PART 2
        dict(
            title="⟦Hankel và hạt nhân Fourier||Hankel and Fourier kernels⟧",
            scr=("⟦Khi $f(x,y)=f(r)$, biến đổi 2D cũng đối xứng tròn và thu về biến đổi Hankel một chiều với hạt nhân Bessel $J_0$.||When $f(x,y)=f(r)$ the 2D transform is also circularly symmetric and reduces to a one-dimensional Hankel transform with the Bessel kernel $J_0$.⟧",
                 "⟦Biến đổi Hankel đối ngược chặt chẽ; nó là một \"hạt nhân Fourier\" theo nghĩa rộng cùng với cos, sin và cas.||The Hankel transform is strictly reciprocal; it is a \"Fourier kernel\" in the broad sense together with cos, sin and cas.⟧",
                 "⟦Định lý Hankel cho cả họ hạt nhân $J_\\nu$; $\\nu=\\pm\\tfrac12$ cho lại cos và sin.||Hankel's theorem gives a whole family of kernels $J_\\nu$; $\\nu=\\pm\\tfrac12$ recovers cos and sin.⟧"),
            preview=["⟦Định nghĩa và bảng cặp||Definition and pairs⟧", "⟦Định lý Hankel, hạt nhân Fourier||Hankel's theorem and Fourier kernels⟧", "⟦Hankel $n$ chiều||The $n$-dimensional Hankel transform⟧"],
            slides=[
                ("⟦Đối xứng tròn dẫn tới Hankel||Circular symmetry leads to Hankel⟧",
                 P(r"⟦Hệ quang học thường gồm các thành phần đối xứng tròn, và sóng lan tỏa hai chiều từ nguồn có đối xứng tự nhiên. Khi $f(x,y)=f(r)$, $r^2=x^2+y^2$, thì $F(u,v)=F(q)$, $q^2=u^2+v^2$. Đổi sang tọa độ cực và tích phân theo góc (dùng $J_0(z)=\tfrac1{2\pi}\int_0^{2\pi}e^{iz\cos\phi}d\phi$): $F(q)=2\pi\int_0^\infty f(r)J_0(2\pi qr)\,r\,dr$ và nghịch đảo $f(r)=2\pi\int_0^\infty F(q)J_0(2\pi qr)\,q\,dq$ (Bracewell, tr. 335 đến 336). Gọi $F(q)$ là biến đổi Hankel bậc 0 của $f$: đối ngược chặt chẽ, như khi hạt nhân là cos và sin. Thừa số $2\pi$ trong ngoặc là do đo $q$ bằng chu kỳ nguyên trên mỗi đơn vị của $r$, thừa số $2\pi$ trước tích phân từ phần tử diện tích $2\pi r\,dr$.||Optical systems are often built from circularly symmetrical components, and waves spreading in two dimensions from a source exhibit symmetry naturally. When $f(x,y)=f(r)$, $r^2=x^2+y^2$, then $F(u,v)=F(q)$, $q^2=u^2+v^2$. Change to polar coordinates and integrate over the angle (using $J_0(z)=\tfrac1{2\pi}\int_0^{2\pi}e^{iz\cos\phi}d\phi$): $F(q)=2\pi\int_0^\infty f(r)J_0(2\pi qr)\,r\,dr$ and the inverse $f(r)=2\pi\int_0^\infty F(q)J_0(2\pi qr)\,q\,dq$ (Bracewell, pp. 335 to 336). Call $F(q)$ the Hankel transform of zero order of $f$: strictly reciprocal, as with the cos and sin kernels. The $2\pi$ in parentheses comes from measuring $q$ in whole cycles per unit of $r$, the $2\pi$ before the integral from the area element $2\pi r\,dr$.⟧")
                 + F("⟦Hankel bậc 0||Zero-order Hankel⟧", r"F(q)=2\pi\int_0^\infty f(r)J_0(2\pi qr)\,r\,dr,\qquad f(r)=2\pi\int_0^\infty F(q)J_0(2\pi qr)\,q\,dq")),
                ("⟦Các cặp Hankel: đĩa, mũ, Gauss||Hankel pairs: disk, exponential, Gaussian⟧",
                 P(r"⟦Bảng 13.2 (tr. 338): đĩa $\Pi(r/2a)\supset a\,J_1(2\pi aq)/q$ (còn gọi là jinc); mũ $e^{-ar}\supset2\pi a\,(a^2+4\pi^2q^2)^{-3/2}$; Gauss $e^{-\pi r^2}\supset e^{-\pi q^2}$; vòng xung $\delta(r-a)\supset2\pi aJ_0(2\pi aq)$; $1/r\supset1/q$. Số đo $a=1.5$ tại $q=0.4$: đĩa tích phân số {{hk_num}} khớp công thức {{hk_cf}} (jinc); mũ $a=1.3$: tích phân {{hk_e_num}} khớp {{hk_e_cf}}; Gauss tại $q=0.5$: {{hk_g}}. Áp dụng hai lần cho mũ trả lại $f(0.5)$ = {{hk_rec_f}} với độ lệch {{hk_rec_dev}}: đối ngược.||Table 13.2 (p. 338): the disk $\Pi(r/2a)\supset a\,J_1(2\pi aq)/q$ (also called jinc); the exponential $e^{-ar}\supset2\pi a\,(a^2+4\pi^2q^2)^{-3/2}$; the Gaussian $e^{-\pi r^2}\supset e^{-\pi q^2}$; the ring impulse $\delta(r-a)\supset2\pi aJ_0(2\pi aq)$; $1/r\supset1/q$. Measured for $a=1.5$ at $q=0.4$: the disk by numerical integration {{hk_num}} matches the formula {{hk_cf}} (jinc); the exponential with $a=1.3$: integral {{hk_e_num}} matches {{hk_e_cf}}; the Gaussian at $q=0.5$: {{hk_g}}. Applying it twice to the exponential returns $f(0.5)$ = {{hk_rec_f}} with deviation {{hk_rec_dev}}: reciprocity.⟧")),
                ("⟦Các định lý Hankel||Theorems for the Hankel transform⟧",
                 P(r"⟦Bảng 13.3 (tr. 339): đồng dạng $f(ar)\supset a^{-2}F(q/a)$; cộng; chập hai chiều tròn $\supset F(q)G(q)$; Rayleigh $\int|f|^2r\,dr=\int|F|^2q\,dq$; tích phân xác định $2\pi\int f\,r\,dr=F(0)$; mômen bậc hai $2\pi\int r^2f\,r\,dr=-F''(0)/2\pi$ (tr. 339 in $F''(0)/2\pi$ với dấu tùy quy ước); độ rộng tương đương $=F(0)/f(0)$ hay $f(0)/F(0)$. Dịch gốc phá đối xứng tròn nên không có định lý dịch. Với Gauss $e^{-\pi r^2}$: $2\pi\int f\,r\,dr$ = {{hd_int}}, và Rayleigh cho {{hd_ray_l}} và {{hd_ray_r}}.||Table 13.3 (p. 339): similarity $f(ar)\supset a^{-2}F(q/a)$; addition; circular two-dimensional convolution $\supset F(q)G(q)$; Rayleigh $\int|f|^2r\,dr=\int|F|^2q\,dq$; definite integral $2\pi\int f\,r\,dr=F(0)$; second moment $2\pi\int r^2f\,r\,dr=-F''(0)/2\pi$ (up to the sign convention of the table); equivalent width $=F(0)/f(0)$ or $f(0)/F(0)$. A shift of origin destroys circular symmetry so there is no shift theorem. For the Gaussian $e^{-\pi r^2}$: $2\pi\int f\,r\,dr$ = {{hd_int}}, and Rayleigh gives {{hd_ray_l}} and {{hd_ray_r}}.⟧")),
                ("⟦Tính số biến đổi Hankel||Numerical evaluation of the Hankel transform⟧",
                 P(r"⟦Bracewell: khá đơn giản nếu có hàm Bessel $J_0$. Cách khác: lấy biến đổi Abel $f_A(x)$ với $x\ge0$, làm thành hàm chẵn độ dài gấp đôi bằng cách cho giá trị tại $x<0$, rồi gọi FFT; vòng Abel-Fourier-Hankel sẽ nói sau (tr. 337). Số đo cho Gauss $e^{-\pi r^2}$: tích phân $J_0$ trực tiếp tại $q=0.5$ cho {{nh_direct}}, đường Abel rồi FFT (lưới bước 0.01) cho {{nh_abel}}, và công thức $e^{-\pi q^2}$ cho {{nh_cf}}: khớp ba cách.||Bracewell: quite straightforward if the Bessel function $J_0$ is available. Alternative: take the Abel transform $f_A(x)$ for $x\ge0$, make it an even function of double length by supplying values for negative $x$, and call an FFT; the Abel-Fourier-Hankel ring is explained later (p. 337). Measured for the Gaussian $e^{-\pi r^2}$: the direct $J_0$ integral at $q=0.5$ gives {{nh_direct}}, the Abel path followed by a Fourier sum (grid step 0.01) gives {{nh_abel}}, and the formula $e^{-\pi q^2}$ gives {{nh_cf}}: three ways agree.⟧")),
                ("⟦Hạt nhân Fourier theo nghĩa rộng||Fourier kernels in the broad sense⟧",
                 P(r"⟦Hai hàm $f,g$ liên hệ qua $g(x)=\int f(s)k(s,x)ds$ với nghịch đảo $f(x)=\int g(s)k(s,x)ds$ (cùng hạt nhân) gọi $k$ là hạt nhân Fourier theo nghĩa rộng: $2\cos2\pi ax$, $2\sin2\pi ax$, $\mathrm{cas}\,2\pi ax$ và $J_0$. Định lý Hankel: $g(x)=\int_0^\infty f(s)(xs)^{1/2}J_\nu(xs)\,ds$ hay $G(s)=\int g(x)(xs)^{1/2}J_\nu(xs)\,dx$, và $g(x)=\int G(s)(xs)^{1/2}J_\nu(xs)\,ds$. Tách $s^{1/2}$, $x^{1/2}$: $F(s)=\int_0^\infty x\,f(x)J_\nu(xs)\,dx$ và $f(x)=\int s\,F(s)J_\nu(xs)\,ds$ (bậc $\nu$ tổng quát; $\nu=0$ ở trên) (tr. 339 đến 340). Với $\nu=\pm\tfrac12$: $J_{1/2}(z)=(2/\pi z)^{1/2}\sin z$ và $J_{-1/2}(z)=(2/\pi z)^{1/2}\cos z$, nên cosin và sin nằm trong định lý Hankel; số đo tại $z=2.3$: hai đẳng thức lệch {{jv_dev}}.||Two functions $f,g$ related by $g(x)=\int f(s)k(s,x)ds$ with inverse $f(x)=\int g(s)k(s,x)ds$ (the same kernel) make $k$ a Fourier kernel in the broad sense: $2\cos2\pi ax$, $2\sin2\pi ax$, $\mathrm{cas}\,2\pi ax$ and $J_0$. Hankel's theorem: $g(x)=\int_0^\infty f(s)(xs)^{1/2}J_\nu(xs)\,ds$, or $G(s)=\int g(x)(xs)^{1/2}J_\nu(xs)\,dx$, and $g(x)=\int G(s)(xs)^{1/2}J_\nu(xs)\,ds$. Splitting off $s^{1/2}$, $x^{1/2}$: $F(s)=\int_0^\infty x\,f(x)J_\nu(xs)\,dx$ and $f(x)=\int s\,F(s)J_\nu(xs)\,ds$ (general order $\nu$; $\nu=0$ above) (pp. 339 to 340). With $\nu=\pm\tfrac12$: $J_{1/2}(z)=(2/\pi z)^{1/2}\sin z$ and $J_{-1/2}(z)=(2/\pi z)^{1/2}\cos z$, so the cosine and sine are included in Hankel's theorem; measured at $z=2.3$: the two identities deviate by {{jv_dev}}.⟧")),
                ("⟦Hankel $n$ chiều||The $n$-dimensional Hankel transform⟧",
                 P(r"⟦Khi có đối xứng cầu trong $n$ chiều, biến đổi một chiều còn lại là $F(q)=2\pi q^{1-n/2}\int_0^\infty f(r)J_{n/2-1}(2\pi qr)\,r^{n/2}dr$ (tr. 343). Với $n=1,2,3$ ta lấy lại Fourier, Hankel và trường hợp đối xứng cầu đã nêu (nhớ $J_{1/2}$ và $J_{-1/2}$ là sin và cos). Số đo cho Gauss $e^{-\pi r^2}$ tại $q=0.5$: cả $n=1,2,3$ cho cùng {{nd_val}} ($e^{-\pi q^2}$), độ lệch lớn nhất {{nd_dev}}. Đó là lý do Gauss là điểm cố định của biến đổi Fourier ở mọi số chiều.||With spherical symmetry in $n$ dimensions the resulting one-dimensional transform is $F(q)=2\pi q^{1-n/2}\int_0^\infty f(r)J_{n/2-1}(2\pi qr)\,r^{n/2}dr$ (p. 343). With $n=1,2,3$ we recover the Fourier and Hankel transforms and the case of spherical symmetry stated before (recalling $J_{1/2}$ and $J_{-1/2}$ are sine and cosine). Measured for the Gaussian $e^{-\pi r^2}$ at $q=0.5$: $n=1,2,3$ all give the same {{nd_val}} ($e^{-\pi q^2}$), maximum deviation {{nd_dev}}. This is why the Gaussian is the fixed point of the Fourier transform in every number of dimensions.⟧")),
                ("⟦Hình 13.4: các cặp Hankel trực quan||Fig. 13.4: Hankel pairs pictured||⟧".replace("||⟧", "⟧"),
                 UL([r"⟦Vòng xung $\delta(r-a)$ biến thành $2\pi aJ_0(2\pi aq)$: vòng sóng đồng tâm mở rộng (nhiễu xạ qua khe tròn).||A ring impulse $\delta(r-a)$ becomes $2\pi aJ_0(2\pi aq)$: a set of concentric wave rings (diffraction from a circular slit).⟧",
                     r"⟦Đĩa (khẩu độ tròn) $\Pi(r/2a)$ biến thành jinc: vòng Airy, không điểm tại nghiệm của $J_1$; số đo nghiệm đầu tiên $2\pi aq\approx$ {{airy_z}} (giá trị $3.8317$).||A disk (circular aperture) $\Pi(r/2a)$ becomes the jinc: the Airy rings, with zeros at the roots of $J_1$; the first zero at $2\pi aq\approx$ {{airy_z}} (the value $3.8317$).⟧",
                     r"⟦Gauss tự biến đổi và không có vòng phụ, ưu thế cho chùm ánh sáng; $1/r$ tự biến đổi thành $1/q$.||The Gaussian transforms into itself with no side rings, an advantage for light beams; $1/r$ transforms into $1/q$.⟧"])),
                ("⟦Tự kiểm tra phần 2||Self-check, part 2⟧",
                 UL([r"⟦Vì sao Hankel bậc 0 đối ngược chặt chẽ?||Why is the zero-order Hankel transform strictly reciprocal?⟧",
                     r"⟦Biến đổi Hankel của đĩa bán kính $a$ là gì?||What is the Hankel transform of a disk of radius $a$?⟧",
                     r"⟦Định lý Hankel cho hạt nhân nào với $\nu=\tfrac12$?||Which kernel does Hankel's theorem give for $\nu=\tfrac12$?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: vì nó suy ra từ Fourier hai chiều đối xứng; $aJ_1(2\\pi aq)/q$; sin, vì $J_{1/2}\\propto\\sin z/\\sqrt z$.||Hints: because it derives from the symmetric 2D Fourier transform; $aJ_1(2\\pi aq)/q$; the sine, since $J_{1/2}\\propto\\sin z/\\sqrt z$.⟧</p>"),
            ]),
        # ---------------------------------------------------------- PART 3
        dict(
            title="⟦Mellin và z: hai họ hàng của Laplace||Mellin and z: two relatives of Laplace⟧",
            scr=("⟦Biến đổi Mellin $F_M(s)=\\int_0^\\infty f(x)x^{s-1}dx$ tương đương Laplace sau khi đặt $x=e^{-t}$.||The Mellin transform $F_M(s)=\\int_0^\\infty f(x)x^{s-1}dx$ is equivalent to Laplace after putting $x=e^{-t}$.⟧",
                 "⟦Biến đổi z của dãy mẫu là đa thức $F(z)=\\sum f(n)z^{-n}$; tích chuỗi của dãy là tích đa thức.||The z transform of a sample sequence is the polynomial $F(z)=\\sum f(n)z^{-n}$; the serial product of sequences is the product of polynomials.⟧",
                 "⟦Mellin là mômen của $f$: $F_M(s)$ là mômen bậc $s-1$; z là phiên bản rời rạc của Laplace, với $z=e^{p}$.||Mellin is a moment: $F_M(s)$ is the $(s-1)$th moment of $f$; z is the discrete version of Laplace with $z=e^{p}$.⟧"),
            preview=["⟦Mellin và Laplace||Mellin and Laplace⟧", "⟦Mômen, hạt nhân Fourier||Moments and Fourier kernels⟧", "⟦Biến đổi z và tích chuỗi||The z transform and the serial product⟧"],
            slides=[
                ("⟦Biến đổi Mellin||The Mellin transform⟧",
                 P(r"⟦Với $s$ phức: $F_M(s)=\int_0^\infty f(x)x^{s-1}dx$ (Bracewell, tr. 343). Đặt $x=e^{-t}$: $dx=-e^{-t}dt$, $x^{s-1}=e^{-(s-1)t}$ nên $F_M(s)=\int_{-\infty}^\infty f(e^{-t})e^{-st}dt$: Laplace của hàm $f(e^{-t})$; vẽ lại hàm thời gian theo $e^{-t}$ nén toàn bộ thời gian dương vào khoảng từ 1 đến 0 (hình 13.5). Nghịch đảo $f(x)=\tfrac1{2\pi i}\int F_M(s)x^{-s}ds$. Số đo: với $f=e^{-x}$ ta có $F_M(s)=\Gamma(s)$; tại $s=2.5$ ta có {{ml_gam}} bằng cả tích phân trực tiếp và tích phân Laplace $\int\exp(-e^{-t})e^{-st}dt$ (độ lệch {{ml_dev}}).||For complex $s$: $F_M(s)=\int_0^\infty f(x)x^{s-1}dx$ (Bracewell, p. 343). Put $x=e^{-t}$: $dx=-e^{-t}dt$, $x^{s-1}=e^{-(s-1)t}$ so $F_M(s)=\int_{-\infty}^\infty f(e^{-t})e^{-st}dt$: the Laplace transform of $f(e^{-t})$; replotting a function of time as a function of $e^{-t}$ compresses all positive time into the range from 1 to 0 (Fig. 13.5). The inverse is $f(x)=\tfrac1{2\pi i}\int F_M(s)x^{-s}ds$. Measured: for $f=e^{-x}$ we have $F_M(s)=\Gamma(s)$; at $s=2.5$ this is {{ml_gam}} by both the direct integral and the Laplace integral $\int\exp(-e^{-t})e^{-st}dt$ (deviation {{ml_dev}}).⟧")),
                ("⟦Bảng cặp Mellin||A table of Mellin pairs⟧",
                 TBL(["$f(x)$", "$F_M(s)$", "⟦Miền||Region⟧"],
                     [["$e^{-ax}$", "$a^{-s}\\Gamma(s)$", "$\\mathrm{Re}\\,s>0$"],
                      ["$\\sin x$", "$\\Gamma(s)\\sin\\tfrac12\\pi s$", "$-1<\\mathrm{Re}\\,s<1$"],
                      ["$\\cos x$", "$\\Gamma(s)\\cos\\tfrac12\\pi s$", "$0<\\mathrm{Re}\\,s<1$"],
                      ["$\\dfrac1{1+x}$", "$\\pi\\,\\mathrm{cosec}\\,\\pi s$", "$0<\\mathrm{Re}\\,s<1$"],
                      ["$H(a-x)$", "$a^s/s$", "$\\mathrm{Re}\\,s>0$"]])
                 + P(r"⟦(Bảng 13.5, tr. 345.) Số đo: $\sin x$ tại $s=0.5$ cho {{ml_sin}} ($\Gamma(\tfrac12)\sin\tfrac\pi4$) qua tích phân dao động; $\tfrac1{1+x}$ tại $s=0.3$ cho {{ml_rat}} ($\pi/\sin0.3\pi$); và xung chữ nhật $H(1-x)$ tại $s=2$ cho {{ml_h2}}.||(Table 13.5, p. 345.) Measured: $\sin x$ at $s=0.5$ gives {{ml_sin}} ($\Gamma(\tfrac12)\sin\tfrac\pi4$) through an oscillatory integral; $\tfrac1{1+x}$ at $s=0.3$ gives {{ml_rat}} ($\pi/\sin0.3\pi$); and the box $H(1-x)$ at $s=2$ gives {{ml_h2}}.⟧")),
                ("⟦Mellin là mômen||Mellin as a moment⟧",
                 P(r"⟦$F_M(s)$ là mômen bậc $(s-1)$ của $f$. Diện tích $F_M(1)$; mômen bậc nhất $F_M(2)$; mômen bậc hai $F_M(3)$; hoành độ trọng tâm $\bar x=F_M(2)/F_M(1)$; bán kính quán tính $[F_M(3)/F_M(1)]^{1/2}$; mômen bậc hai quanh trọng tâm $F_M(3)/F_M(1)-[F_M(2)/F_M(1)]^2$ (Bracewell, tr. 344, dạng chuẩn hóa). Ví dụ $f=\Pi(x-\tfrac12)$ (bằng 1 trên $(0,1)$): $F_M(s)=1/s$; trọng tâm {{mm_c}}, bán kính quán tính {{mm_rg}}, phương sai {{mm_v}} ($1/12$). Định lý đồng dạng $f(ax)\supset a^{-s}F_M(s)$: với $e^{-x}$, $a=2$, $s=2.5$ ta có {{mm_sc}}.||$F_M(s)$ is the $(s-1)$th moment of $f$. Area $F_M(1)$; first moment $F_M(2)$; second moment $F_M(3)$; abscissa of centroid $\bar x=F_M(2)/F_M(1)$; radius of gyration $[F_M(3)/F_M(1)]^{1/2}$; second moment about the centroid $F_M(3)/F_M(1)-[F_M(2)/F_M(1)]^2$ (Bracewell, p. 344, normalised form). Example $f=\Pi(x-\tfrac12)$ (equal to 1 on $(0,1)$): $F_M(s)=1/s$; centroid {{mm_c}}, radius of gyration {{mm_rg}}, variance {{mm_v}} ($1/12$). The similarity theorem $f(ax)\supset a^{-s}F_M(s)$: with $e^{-x}$, $a=2$, $s=2.5$ we get {{mm_sc}}.⟧")),
                ("⟦Mellin và điều kiện hạt nhân Fourier||Mellin and the Fourier-kernel condition⟧",
                 P(r"⟦Từ $g(x)=\int f(s)k(xs)ds$ và $f(x)=\int g(s)h(xs)ds$, lấy Mellin cả hai vế cho $K_M(s)H_M(1-s)=1$, tức nghiệm giải cho phương trình tích phân hạt nhân $k(ax)$. Khi $h=k$ đó là điều kiện để $k(ax)$ là hạt nhân Fourier: $K_M(s)K_M(1-s)=1$ (Bracewell, tr. 346 đến 347). Kiểm tra với $k(x)=2\cos2\pi x$: $K_M(s)=2(2\pi)^{-s}\Gamma(s)\cos\tfrac12\pi s$; tại $s=0.3$: $K_M(0.3)$ = {{fk_k}} (tích phân số {{fk_num}}), và tích $K_M(0.3)K_M(0.7)$ = {{fk_prod}}. Đây là chứng minh rằng hạt nhân cosin đối ngược, qua Mellin.||From $g(x)=\int f(s)k(xs)ds$ and $f(x)=\int g(s)h(xs)ds$, taking the Mellin transform of both gives $K_M(s)H_M(1-s)=1$, i.e. the solving kernel for integral equations with kernel $k(ax)$. When $h=k$ this is the condition for $k(ax)$ to be a Fourier kernel: $K_M(s)K_M(1-s)=1$ (Bracewell, pp. 346 to 347). Check with $k(x)=2\cos2\pi x$: $K_M(s)=2(2\pi)^{-s}\Gamma(s)\cos\tfrac12\pi s$; at $s=0.3$: $K_M(0.3)$ = {{fk_k}} (numerical integral {{fk_num}}), and the product $K_M(0.3)K_M(0.7)$ = {{fk_prod}}. This proves through Mellin that the cosine kernel is reciprocal.⟧")),
                ("⟦Biến đổi z: đa thức mẫu||The z transform: a polynomial of samples⟧",
                 P(r"⟦Tín hiệu mà giá trị mẫu cách đều là toàn bộ thông tin (điều chế xung, hệ điều khiển lấy mẫu). Với khoảng bằng 1 và $f(t)$ biết tại $t=0,1,\ldots,n$, đa thức $F(z)=f(0)+f(1)z^{-1}+f(2)z^{-2}+\cdots+f(n)z^{-n}$ là biến đổi z (tr. 347). Chuỗi xung $g(t)=\sum f(n)\delta(t-n)$ đầy đủ tương đương tập mẫu. Liên hệ với Laplace: $F_L(p)=\sum f(n)e^{-np}$, nên với $z=e^{p}$ đó chính là biến đổi z; tại $p=0.7$ số đo cho {{z_lap}} bằng $F(e^{0.7})$ (độ lệch {{z_lap_dev}}). Trên vòng đơn vị $z=e^{i2\pi k/N}$ ta có DFT (module 14): $F(z_k)$ lệch {{z_dft}} so với FFT.||A signal whose sample values at equispaced times constitute the full information (pulse modulation, sampled-data control systems). With interval 1 and $f(t)$ known at $t=0,1,\ldots,n$, the polynomial $F(z)=f(0)+f(1)z^{-1}+f(2)z^{-2}+\cdots+f(n)z^{-n}$ is the z transform (p. 347). The impulse string $g(t)=\sum f(n)\delta(t-n)$ is fully equivalent to the sample set. The relation with Laplace: $F_L(p)=\sum f(n)e^{-np}$, so with $z=e^{p}$ it is exactly the z transform; at $p=0.7$ the measurement gives {{z_lap}} equal to $F(e^{0.7})$ (deviation {{z_lap_dev}}). On the unit circle $z=e^{i2\pi k/N}$ we get the DFT (module 14): $F(z_k)$ deviates by {{z_dft}} from the FFT.⟧")),
                ("⟦Tích chuỗi là tích đa thức||The serial product is a polynomial product||⟧".replace("||⟧", "⟧"),
                 P(r"⟦Hệ có đáp ứng xung $\{h(0)\,h(1)\,\ldots\}$ nhận vào tín hiệu $\{f(0)\,f(1)\,\ldots\}$ cho ra tích chuỗi, có biến đổi z bằng tích $F(z)H(z)$. Ví dụ: tín hiệu $\{2\,1\}$ và đáp ứng $\{8\,4\,2\,1\}$: $(2+z^{-1})(8+4z^{-1}+2z^{-2}+z^{-3})=16+16z^{-1}+8z^{-2}+4z^{-3}+z^{-4}$, nên đầu ra $\{16\,16\,8\,4\,1\}$ ({{z_o1}} phần tử đầu, {{z_o5}} phần tử cuối) (tr. 348). Ngược lại chia biến đổi z đầu ra cho đầu vào cho đáp ứng: phép chia đa thức trả lại $\{8\,4\,2\,1\}$ (phần dư {{z_rem}}). Thừa số hóa đa thức cho thuận tiện lý thuyết, đó là lý do dùng z.||A system with impulse response $\{h(0)\,h(1)\,\ldots\}$ receiving the signal $\{f(0)\,f(1)\,\ldots\}$ gives the serial product, whose z transform is the product $F(z)H(z)$. Example: the signal $\{2\,1\}$ and the response $\{8\,4\,2\,1\}$: $(2+z^{-1})(8+4z^{-1}+2z^{-2}+z^{-3})=16+16z^{-1}+8z^{-2}+4z^{-3}+z^{-4}$, so the output is $\{16\,16\,8\,4\,1\}$ ({{z_o1}} the first element, {{z_o5}} the last) (p. 348). Conversely dividing the output z transform by the input gives the response: polynomial division returns $\{8\,4\,2\,1\}$ (remainder {{z_rem}}). Factoring polynomials gives theoretical convenience, which is why z is used.⟧")),
                ("⟦Bảng z và định lý||z tables and theorems⟧",
                 P(r"⟦Bảng 13.7 cho các dãy có công thức (tr. 350): $\{1,1,1,\ldots\}\to\dfrac1{1-z^{-1}}$; $\{n\}\to\dfrac{z^{-1}}{(1-z^{-1})^2}$; $\{n^2\}\to\dfrac{z^{-1}(1+z^{-1})}{(1-z^{-1})^3}$; $\{a^n\}\to\dfrac1{1-az^{-1}}$; $\{\cos\alpha n\}\to\dfrac{1-z^{-1}\cos\alpha}{1-2z^{-1}\cos\alpha+z^{-2}}$. Số đo tại $z=2$ (tổng chuỗi 300 số hạng): $\sum n z^{-n}$ = {{z_n1}}, $\sum n^2z^{-n}$ = {{z_n2}}, $\sum\cos(0.7n)z^{-n}$ = {{z_cos}} khớp công thức. Định lý (bảng 13.8): $f(n-1)\supset z^{-1}F$; $nf(n)\supset-zF'(z)$ (số đo lệch {{z_dev}}); $f_1*f_2\supset F_1F_2$. Bảng z và định lý Mellin gần như giống hệt vì Mellin và z ngược đều dẫn từ Laplace.||Table 13.7 for sequences with formulas (p. 350): $\{1,1,1,\ldots\}\to\dfrac1{1-z^{-1}}$; $\{n\}\to\dfrac{z^{-1}}{(1-z^{-1})^2}$; $\{n^2\}\to\dfrac{z^{-1}(1+z^{-1})}{(1-z^{-1})^3}$; $\{a^n\}\to\dfrac1{1-az^{-1}}$; $\{\cos\alpha n\}\to\dfrac{1-z^{-1}\cos\alpha}{1-2z^{-1}\cos\alpha+z^{-2}}$. Measured at $z=2$ (a 300-term series sum): $\sum n z^{-n}$ = {{z_n1}}, $\sum n^2z^{-n}$ = {{z_n2}}, $\sum\cos(0.7n)z^{-n}$ = {{z_cos}} matching the formulas. Theorems (Table 13.8): $f(n-1)\supset z^{-1}F$; $nf(n)\supset-zF'(z)$ (measured deviation {{z_dev}}); $f_1*f_2\supset F_1F_2$. The z table and the Mellin theorems are nearly identical because Mellin and inverse z both derive from Laplace.⟧")),
                ("⟦Tự kiểm tra phần 3||Self-check, part 3⟧",
                 UL([r"⟦Biến đổi Mellin của $e^{-x}$ tại $s=2.5$ là gì?||What is the Mellin transform of $e^{-x}$ at $s=2.5$?⟧",
                     r"⟦Biến đổi z của $\{2\,1\}*\{8\,4\,2\,1\}$ là gì?||What is the z transform of $\{2\,1\}*\{8\,4\,2\,1\}$?⟧",
                     r"⟦Điều kiện hạt nhân Fourier theo Mellin là gì?||What is the Fourier-kernel condition in Mellin terms?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: $\\Gamma(2.5)=1.3293$; đa thức $16+16z^{-1}+8z^{-2}+4z^{-3}+z^{-4}$; $K_M(s)K_M(1-s)=1$.||Hints: $\\Gamma(2.5)=1.3293$; the polynomial $16+16z^{-1}+8z^{-2}+4z^{-3}+z^{-4}$; $K_M(s)K_M(1-s)=1$.⟧</p>"),
            ]),
        # ---------------------------------------------------------- PART 4
        dict(
            title="⟦Abel, Radon và chụp cắt lớp||Abel, Radon and tomography⟧",
            scr=("⟦Phân bố tròn chiếu xuống một chiều cho biến đổi Abel: $f_A(x)=2\\int_x^\\infty f(r)r\\,dr/\\sqrt{r^2-x^2}$.||A circularly symmetric distribution projected in one dimension gives the Abel transform: $f_A(x)=2\\int_x^\\infty f(r)r\\,dr/\\sqrt{r^2-x^2}$.⟧",
                 "⟦Abel, rồi Fourier, rồi Hankel đưa về hàm ban đầu; tổng quát hóa thành định lý lát chiếu.||Abel, then Fourier, then Hankel returns the original function; this generalises to the projection-slice theorem.⟧",
                 "⟦Chụp cắt lớp: lọc mỗi hình chiếu bằng phép chập rồi chiếu ngược.||Tomography: filter each projection by a convolution, then back-project.⟧"),
            preview=["⟦Biến đổi Abel và cách tính số||The Abel transform and its numerics⟧", "⟦Vòng Abel-Fourier-Hankel||The Abel-Fourier-Hankel ring⟧", "⟦Radon và chiếu ngược||Radon and back-projection⟧"],
            slides=[
                ("⟦Biến đổi Abel||The Abel transform⟧",
                 P(r"⟦Khi có phân bố tròn chiếu xuống một chiều (đáp ứng của camera truyền hình quét qua một vạch hẹp, hay của vi quang kế quét qua phân bố mật độ tròn trên kính ảnh) ta gặp biến đổi Abel: $f_A(x)=2\int_x^\infty\dfrac{f(r)\,r\,dr}{(r^2-x^2)^{1/2}}$ (Bracewell, tr. 351). Nó cũng gắn với đạo hàm cấp phân số (dẫn nhiệt trong chất rắn, truyền tín hiệu trên cáp). Bằng cách đặt $\xi=x^2$, $\rho=r^2$, được biến đổi Abel sửa đổi $F_A=K*F$ với $K(\xi)=\xi^{-1/2}$ khi $\xi<0$ (dạng chập), nên lấy Fourier: $F=(1/\pi)\,\ldots$; nghiệm là $f(r)=-\dfrac1\pi\int_r^\infty\dfrac{f_A'(x)\,dx}{(x^2-r^2)^{1/2}}$ (tr. 352 đến 353). Kiểm tra: $f_A(0)=2\int_0^\infty f\,dr$ và $\int f_A\,dx=2\pi\int f\,r\,dr$.||When a circularly symmetric distribution is projected in one dimension (the response of a television camera scanning across a narrow line, or of a microdensitometer whose slit scans over a circular density distribution on a photographic plate) one meets the Abel transform: $f_A(x)=2\int_x^\infty\dfrac{f(r)\,r\,dr}{(r^2-x^2)^{1/2}}$ (Bracewell, p. 351). It is also tied to fractional-order derivatives (heat conduction in solids, signal transmission through cables). Putting $\xi=x^2$, $\rho=r^2$ gives the modified Abel transform $F_A=K*F$ with $K(\xi)=\xi^{-1/2}$ for $\xi<0$ (a convolution form), so Fourier transforming; the solution is $f(r)=-\dfrac1\pi\int_r^\infty\dfrac{f_A'(x)\,dx}{(x^2-r^2)^{1/2}}$ (pp. 352 to 353). Checks: $f_A(0)=2\int_0^\infty f\,dr$ and $\int f_A\,dx=2\pi\int f\,r\,dr$.⟧")),
                ("⟦Các cặp Abel: đĩa, bán ellip, tam giác||Abel pairs: disk, semi-ellipse, triangle⟧",
                 P(r"⟦Bảng 13.9 (tr. 354): đĩa $\Pi(r/2a)\to2(a^2-x^2)^{1/2}\Pi(x/2a)$ (bán ellip); Gauss $e^{-r^2/2\sigma^2}\to(2\pi)^{1/2}\sigma\,e^{-x^2/2\sigma^2}$; hình nón $a\Lambda(r/a)$ $\to$ hàm có $\cosh^{-1}$; vòng xung $\delta(r-a)\to2a(a^2-x^2)^{-1/2}\Pi(x/2a)$; $\mathrm{sinc}$-loại. Số đo: đĩa $a=1$ tại $x=0.6$ cho $f_A$ = {{ab_disk}} ($2\sqrt{1-0.36}$); Gauss $e^{-\pi r^2}$ tại $x=0.5$ cho {{ab_gauss}} ($e^{-\pi x^2}$, tự biến đổi); tại 0: $f_A(0)=2\int f\,dr$ cho $f=1-r$ (trên $r<1$) là {{ab_0}}, và $\int f_A\,dx$ = {{ab_area}} ($2\pi/6=\pi/3$).||Table 13.9 (p. 354): the disk $\Pi(r/2a)\to2(a^2-x^2)^{1/2}\Pi(x/2a)$ (a semi-ellipse); Gaussian $e^{-r^2/2\sigma^2}\to(2\pi)^{1/2}\sigma\,e^{-x^2/2\sigma^2}$; the cone $a\Lambda(r/a)$ $\to$ a function with $\cosh^{-1}$; the ring impulse $\delta(r-a)\to2a(a^2-x^2)^{-1/2}\Pi(x/2a)$. Measured: the disk with $a=1$ at $x=0.6$ gives $f_A$ = {{ab_disk}} ($2\sqrt{1-0.36}$); the Gaussian $e^{-\pi r^2}$ at $x=0.5$ gives {{ab_gauss}} ($e^{-\pi x^2}$, self-transforming); at 0: $f_A(0)=2\int f\,dr$ for $f=1-r$ (on $r<1$) is {{ab_0}}, and $\int f_A\,dx$ = {{ab_area}} ($2\pi/6=\pi/3$).⟧")),
                ("⟦Cách tính số biến đổi Abel bằng bảng hệ số||Numerical Abel transform by a table of coefficients⟧",
                 P(r"⟦Sau khi đổi biến, tính tổng các tích $K(\rho)F(\xi-\rho)$ tại các bước rời rạc. Giá trị của $K$ không đổi khi bước nhỏ đi, trừ thừa số chuẩn hóa, nên lập được bảng vạn năng (bảng 13.10): hệ số cho khoảng $[n,n+1]$ là $c_n=\int_n^{n+1}\rho^{-1/2}d\rho=2(\sqrt{n+1}-\sqrt n)$: $c_0$ = 2, $c_1$ = {{ab_k1}}, $c_2$ = {{ab_k2}}, $c_3$ = {{ab_k3}}. Ví dụ của sách $F(p)=(10-p)^{1/2}$ có $F_A(\xi)=\tfrac\pi2(10-\xi)$: tại $\xi=5$ tổng $\sum c_nF(5+n+\tfrac12)$ cho {{ab_alg}} (sách 7.78) so với đúng {{ab_exact}} (tr. 353 đến 355). Bài toán ngược tính từ dưới lên với cùng bảng.||After the change of variable, sum products $K(\rho)F(\xi-\rho)$ at discrete steps. The values of $K$ turn out to be the same however fine the interval, save for a normalising factor, so a universal table (Table 13.10) can be set up: the coefficient for the interval $[n,n+1]$ is $c_n=\int_n^{n+1}\rho^{-1/2}d\rho=2(\sqrt{n+1}-\sqrt n)$: $c_0$ = 2, $c_1$ = {{ab_k1}}, $c_2$ = {{ab_k2}}, $c_3$ = {{ab_k3}}. The book's example $F(p)=(10-p)^{1/2}$ has $F_A(\xi)=\tfrac\pi2(10-\xi)$: at $\xi=5$ the sum $\sum c_nF(5+n+\tfrac12)$ gives {{ab_alg}} (book 7.78) against the exact {{ab_exact}} (pp. 353 to 355). The inverse problem is computed from the bottom up with the same table.⟧")),
                ("⟦Chương trình tính $f(r)=1-r$||The program for $f(r)=1-r$⟧",
                 P(r"⟦Cách thay thế tránh kỳ dị khi $r\to x$: định nghĩa hàm $f(r)$ nội suy giữa các mẫu, rồi tích phân $f_A(x)=2\int_0^\infty f(\sqrt{x^2+t^2})\,dt$ (đổi $r^2=x^2+t^2$), khỏi phải xử lý căn ở mẫu số. Với $f=1-r$ trên $[0,1]$, sách in các giá trị $f_A(x)$ tại $x=0,0.1,\ldots,0.9$: $1,\ .9651,\ .8881,\ .7853,\ .6658,\ .5368,\ .4045,\ .2753,\ .1564,\ .0575$ (sai số tuyệt đối trung bình nhỏ); tính lại ở đây: $f_A(0.1)$ = {{ab_x1}}, $f_A(0.5)$ = {{ab_x5}}, $f_A(0.9)$ = {{ab_x9}}, khớp giá trị in trong 0.001 (tr. 356).||An alternative avoiding the singularity as $r\to x$: define the function $f(r)$ interpolated between samples, then integrate $f_A(x)=2\int_0^\infty f(\sqrt{x^2+t^2})\,dt$ (with $r^2=x^2+t^2$), avoiding the root in the denominator. For $f=1-r$ on $[0,1]$ the book prints the values $f_A(x)$ at $x=0,0.1,\ldots,0.9$: $1,\ .9651,\ .8881,\ .7853,\ .6658,\ .5368,\ .4045,\ .2753,\ .1564,\ .0575$ (small mean absolute error); recomputed here: $f_A(0.1)$ = {{ab_x1}}, $f_A(0.5)$ = {{ab_x5}}, $f_A(0.9)$ = {{ab_x9}}, agreeing with the printed values within 0.001 (p. 356).⟧")),
                ("⟦Vòng Abel-Fourier-Hankel||The Abel-Fourier-Hankel ring||⟧".replace("||⟧", "⟧"),
                 P(r"⟦Bắt đầu từ hàm chẵn $f(r)$: biến đổi Abel, rồi Fourier một chiều, rồi Hankel: ta trở về hàm ban đầu (Bracewell, 1956). Ví dụ $f(r)=\delta(r-a)$: Abel cho $2a/\sqrt{a^2-x^2}\,\Pi(x/2a)$, Fourier của nó là $2\pi aJ_0(2\pi as)$, và bảng 13.2 cho Hankel của $J_0$ là $\delta(r-a)$ (tr. 357). Số đo với Gauss $e^{-\pi r^2}$ tại $r=0.6$: giá trị đúng {{arh_val}}, tính đủ ba bước bằng số (Abel tích phân, Fourier tổng, Hankel tổng) cho lại giá trị với độ lệch {{arh_dev}}. Nghĩa là Hankel = Fourier $\circ$ Abel (bài 16 của chương).||Start with an even function $f(r)$: take the Abel transform, then the one-dimensional Fourier transform, then the Hankel transform: we return to the original function (Bracewell, 1956). Example $f(r)=\delta(r-a)$: Abel gives $2a/\sqrt{a^2-x^2}\,\Pi(x/2a)$, its Fourier transform is $2\pi aJ_0(2\pi as)$, and Table 13.2 gives the Hankel transform of $J_0$ as $\delta(r-a)$ (p. 357). Measured with the Gaussian $e^{-\pi r^2}$ at $r=0.6$: the exact value {{arh_val}}, and carrying out all three steps numerically (Abel integral, Fourier sum, Hankel sum) reproduces it with deviation {{arh_dev}}. This means Hankel = Fourier $\circ$ Abel (problem 16 of the chapter).⟧")),
                ("⟦Biến đổi Radon và định lý lát chiếu||The Radon transform and the projection-slice theorem⟧",
                 P(r"⟦Với mật độ không đối xứng $f(x,y)$ quét theo hướng $\theta$: $g_\theta(R)=\iint f(x,y)\,\delta(R-x\cos\theta-y\sin\theta)\,dx\,dy$ là tích phân dọc đường $x\cos\theta+y\sin\theta=R$ (khe ở khoảng cách $R$ từ gốc). Kỹ thuật này làm cách mạng chẩn đoán y học (CAT, NMR) và thiên văn vô tuyến. Định lý lát chiếu: lát cắt của $F(u,v)$ dọc góc $\theta$ bằng Fourier một chiều của hình chiếu $g_\theta(R)$ (Bracewell, 1956; tr. 356 đến 358). Số đo với Gauss ellip $f=e^{-\pi(x^2/4+y^2/0.25)}$ ($a=2$, $b=0.5$) tại $\theta=0.6$: hình chiếu $g_\theta(0.3)$ tích phân số {{rd_num}} khớp công thức {{rd_cf}}; và Fourier một chiều của hình chiếu tại $q=0.4$ bằng lát cắt $F(q\cos\theta,q\sin\theta)$: lệch {{ps_dev}}.||With an unsymmetrical density $f(x,y)$ scanned in direction $\theta$: $g_\theta(R)=\iint f(x,y)\,\delta(R-x\cos\theta-y\sin\theta)\,dx\,dy$ is the integral along the line $x\cos\theta+y\sin\theta=R$ (the slit at distance $R$ from the origin). This technique revolutionised medical diagnosis (CAT, NMR) and radio astronomy. The projection-slice theorem: the slice of $F(u,v)$ at angle $\theta$ equals the one-dimensional Fourier transform of the projection $g_\theta(R)$ (Bracewell, 1956; pp. 356 to 358). Measured with the elliptical Gaussian $f=e^{-\pi(x^2/4+y^2/0.25)}$ ($a=2$, $b=0.5$) at $\theta=0.6$: the projection $g_\theta(0.3)$ by numerical integration {{rd_num}} matches the formula {{rd_cf}}; and the one-dimensional Fourier transform of the projection at $q=0.4$ equals the slice $F(q\cos\theta,q\sin\theta)$: deviation {{ps_dev}}.⟧")),
                ("⟦Tái tạo bằng chiếu ngược có sửa đổi||Reconstruction by modified back-projection⟧",
                 P(r"⟦Các hình chiếu cho $F(u,v)$ trên các nan hoa $\theta=\mathrm{const}$; mật độ điểm tỉ lệ nghịch với bán kính, nên nhân với $|q|$ để hiệu chỉnh: hệ số $\Pi(q/2M)-\Lambda(q/M)=|q|/M$ khi $|q|<M$. Nhân ở miền $q$ tương ứng phép chập dữ liệu $g_0(R)=g(R)*(2M\,\mathrm{sinc}\,2MR-M\,\mathrm{sinc}^2MR)$. Quy trình: (a) sửa mỗi hình chiếu bằng chập, (b) chiếu ngược (rải hình chiếu đã sửa đều theo hướng vuông góc với trục $R$) và (c) cộng dồn trên mặt phẳng $(x,y)$: chiếu ngược có sửa đổi (Bracewell và Riddle, 1967; tr. 358). Số đo: biến đổi Fourier của nhân tại $q=2$ bằng $|q|/M$ = {{kf_2}} (với $M=6$), tại $q=8>M$ bằng {{kf_8}}; tái tạo hai Gauss từ 180 hướng: tại tâm {{fb_c}} (đúng 1), sai lệch lớn nhất trên bốn điểm {{fb_dev}}.||The projections give $F(u,v)$ on spokes $\theta=\mathrm{const}$; the density of points is inversely proportional to radius, so multiply by $|q|$ to correct: the factor $\Pi(q/2M)-\Lambda(q/M)=|q|/M$ for $|q|<M$. Multiplication in the $q$ domain corresponds to a convolution of the data $g_0(R)=g(R)*(2M\,\mathrm{sinc}\,2MR-M\,\mathrm{sinc}^2MR)$. The procedure: (a) modify each scan by convolution, (b) back-project (spread the modified scan uniformly over the plane perpendicular to the $R$-axis) and (c) accumulate over the $(x,y)$ plane: modified back-projection (Bracewell and Riddle, 1967; p. 358). Measured: the Fourier transform of the kernel at $q=2$ equals $|q|/M$ = {{kf_2}} (with $M=6$), at $q=8>M$ it is {{kf_8}}; reconstructing two Gaussians from 180 directions: at the centre {{fb_c}} (exact 1), maximum error over four points {{fb_dev}}.⟧")),
                ("⟦Ví dụ: hai Gauss và các hình chiếu||Example: two Gaussians and their projections||⟧".replace("||⟧", "⟧"),
                 UL([r"⟦Vật thể: một Gauss trung tâm (bề rộng 0.5, biên độ 1) và một Gauss nhỏ hơn (bề rộng 0.3, biên độ 0.6) tại $(0.7,-0.5)$; hình chiếu của mỗi Gauss là Gauss theo $R$, tâm dịch $R_c=x_c\cos\theta+y_c\sin\theta$.||The object: a central Gaussian (width 0.5, amplitude 1) and a smaller one (width 0.3, amplitude 0.6) at $(0.7,-0.5)$; the projection of each Gaussian is a Gaussian in $R$ with centre shifted to $R_c=x_c\cos\theta+y_c\sin\theta$.⟧",
                     r"⟦Không lọc thì chiếu ngược cho ảnh mờ (trọng số $1/|q|$); lọc bằng nhân chập cho ảnh sắc: giá trị tại tâm {{fb_c}}.||Without filtering back-projection gives a blurred image (weight $1/|q|$); filtering with the convolution kernel gives a sharp image: the value at the centre {{fb_c}}.⟧",
                     r"⟦Sai số còn lại đến từ băng thông hữu hạn $M$ và nội suy tuyến tính, không phải từ số hướng: 90, 180 và 360 hướng cho cùng kết quả đến 3 chữ số.||The remaining error comes from the finite bandwidth $M$ and linear interpolation, not from the number of directions: 90, 180 and 360 directions agree to three digits.⟧"])),
                ("⟦Tự kiểm tra phần 4||Self-check, part 4⟧",
                 UL([r"⟦Biến đổi Abel của đĩa bán kính 1 tại $x=0.6$ là bao nhiêu?||What is the Abel transform of a unit-radius disk at $x=0.6$?⟧",
                     r"⟦Vòng Abel-Fourier-Hankel nói gì?||What does the Abel-Fourier-Hankel ring say?⟧",
                     r"⟦Vì sao chiếu ngược cần bộ lọc dốc $|q|$?||Why does back-projection need the ramp filter $|q|$?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: $2\\sqrt{1-0.36}=1.6$; Abel, rồi Fourier, rồi Hankel trả lại hàm ban đầu; vì mật độ điểm trên nan hoa tỉ lệ $1/|q|$.||Hints: $2\\sqrt{1-0.36}=1.6$; Abel, then Fourier, then Hankel returns the original function; because the density of points on spokes goes as $1/|q|$.⟧</p>"),
            ]),
        # ---------------------------------------------------------- PART 5
        dict(
            title="⟦Hilbert và Fourier phân số||Hilbert and fractional Fourier⟧",
            scr=("⟦Biến đổi Hilbert là bộ lọc dời pha $\\pm\\tfrac\\pi2$ mà giữ nguyên biên độ; áp dụng hai lần cho $-f$.||The Hilbert transform is a filter that shifts phase by $\\pm\\tfrac\\pi2$ while leaving amplitudes unchanged; applied twice it gives $-f$.⟧",
                 "⟦Tín hiệu giải tích $f-iF_{\\mathrm{Hi}}$ chỉ có tần số dương, cho đường bao và tần số tức thời; nhân quả cho cặp Hilbert (Kramers-Kronig).||The analytic signal $f-iF_{\\mathrm{Hi}}$ has only positive frequencies and gives the envelope and instantaneous frequency; causality gives Hilbert pairs (Kramers-Kronig).⟧",
                 "⟦Fourier phân số có bậc $a$ tùy ý, cộng tính, với hàm Hermite-Gauss là hàm riêng.||The fractional Fourier transform has arbitrary order $a$, is additive, with Hermite-Gauss functions as eigenfunctions.⟧"),
            preview=["⟦Hilbert và tín hiệu giải tích||Hilbert and the analytic signal⟧", "⟦Nhân quả và tính số||Causality and computing⟧", "⟦Fourier phân số||The fractional Fourier transform⟧"],
            slides=[
                ("⟦Biến đổi Hilbert||The Hilbert transform⟧",
                 P(r"⟦Định nghĩa $F_{\mathrm{Hi}}(x)=\tfrac1\pi\,\mathrm{P.V.}\!\int\dfrac{f(x')\,dx'}{x'-x}=\left(-\dfrac1{\pi x}\right)*f(x)$, kỳ dị tại $x=x'$ lấy giá trị chính Cauchy. Biến đổi Fourier của $-1/(\pi x)$ là $i\,\mathrm{sgn}\,s$ ($+i$ cho $s>0$, $-i$ cho $s<0$): biến đổi Hilbert là bộ lọc lạ, giữ biên độ các thành phần phổ nhưng dời pha $\pi/2$ theo dấu của $s$. Áp dụng hai lần đảo pha mọi thành phần nên $f=-F_{\mathrm{Hi}}*(1/\pi x)$... tức $HH f=-f$. Mọi cosin thành $-$sin và mọi sin thành cosin; hàm chẵn thành hàm lẻ (Bracewell, tr. 359 đến 361). Số đo trên tín hiệu tuần hoàn: Hilbert của $\cos$ lệch $-\sin$ bởi {{hb_cos}}, và áp dụng hai lần lệch $-f$ bởi {{hb_two}}. Hilbert của $\Pi(x)$ là $\tfrac1\pi\ln|(x-\tfrac12)/(x+\tfrac12)|$: tại $x=1$ là {{hr_1}}, tại $x=0.2$ (điểm trong vùng kỳ dị) là {{hr_02}}, cả hai bằng tích phân giá trị chính số.||Definition $F_{\mathrm{Hi}}(x)=\tfrac1\pi\,\mathrm{P.V.}\!\int\dfrac{f(x')\,dx'}{x'-x}=\left(-\dfrac1{\pi x}\right)*f(x)$, the divergence at $x=x'$ taken as the Cauchy principal value. The Fourier transform of $-1/(\pi x)$ is $i\,\mathrm{sgn}\,s$ ($+i$ for $s>0$, $-i$ for $s<0$): Hilbert transformation is a curious kind of filtering, leaving the amplitudes of spectral components unchanged but shifting their phases by $\pi/2$ according to the sign of $s$. Applying it twice reverses the phase of every component so $HHf=-f$. All cosines become $-$sines and all sines become cosines; even functions become odd (Bracewell, pp. 359 to 361). Measured on a periodic signal: the Hilbert transform of $\cos$ differs from $-\sin$ by {{hb_cos}}, and applying it twice differs from $-f$ by {{hb_two}}. The Hilbert transform of $\Pi(x)$ is $\tfrac1\pi\ln|(x-\tfrac12)/(x+\tfrac12)|$: at $x=1$ it is {{hr_1}}, at $x=0.2$ (a point inside the singular range) it is {{hr_02}}, both matching numerical principal-value integrals.⟧")
                 + F("⟦Biến đổi Hilbert||The Hilbert transform⟧", r"F_{\mathrm{Hi}}=\Big(-\frac1{\pi x}\Big)*f\ \ \supset\ \ i\,\operatorname{sgn}s\;F(s)")),
                ("⟦Tín hiệu giải tích||The analytic signal⟧",
                 P(r"⟦Với $f(t)$ thực, liên kết hàm phức $f(t)-iF_{\mathrm{Hi}}(t)$ mà phần thực là $f$: tín hiệu giải tích; $F_{\mathrm{Hi}}$ là hàm cầu phương. Ví dụ hàm cầu phương của $\cos t$ là $-\sin t$ và tín hiệu giải tích là $e^{it}$: nó liên hệ với $f$ như $e^{it}$ với $\cos t$. Nó không chứa thành phần tần số âm: có được bằng cách triệt tần số âm và nhân đôi: $2H(f)F(f)$. Số đo với tín hiệu ngẫu nhiên dải hẹp: tính $f-iF_{\mathrm{Hi}}$ (bộ lọc $i\,\mathrm{sgn}\,s$) khớp hàm $\mathrm{scipy.signal.hilbert}$ với độ lệch {{an_dev}}, và phổ của nó trên tần số âm nhỏ hơn {{an_neg}} (Bracewell, tr. 361 đến 363).||For a real $f(t)$, associate the complex function $f(t)-iF_{\mathrm{Hi}}(t)$ whose real part is $f$: the analytic signal; $F_{\mathrm{Hi}}$ is the quadrature function. Example: the quadrature function of $\cos t$ is $-\sin t$ and the analytic signal is $e^{it}$: it bears to $f$ the same relation as $e^{it}$ to $\cos t$. It contains no negative-frequency components: it is obtained by suppressing negative frequencies and doubling: $2H(f)F(f)$. Measured with a random narrow-band signal: computing $f-iF_{\mathrm{Hi}}$ (filter $i\,\mathrm{sgn}\,s$) matches $\mathrm{scipy.signal.hilbert}$ with deviation {{an_dev}}, and its spectrum at negative frequencies is below {{an_neg}} (Bracewell, pp. 361 to 363).⟧")),
                ("⟦Đường bao và tần số tức thời||Envelope and instantaneous frequency⟧",
                 P(r"⟦Nếu gán được tần số góc trung bình $\omega$, tín hiệu giải tích viết $V(t)e^{i\omega t}$; $V(t)$ là phasor biến thiên theo thời gian; $|V(t)|$ là biên độ tức thời, hay đường bao, và tốc độ đổi pha là tần số tức thời (Bracewell, tr. 362 đến 363). Bracewell cảnh báo: $\omega$ và $V(t)$ nói chung không xác định duy nhất, nên thuật ngữ đường bao có thể gây bất ngờ. Số đo: điều biên $(1+0.5\cos3t)\cos50t$ có đường bao $1+0.5\cos3t$ với độ lệch {{env_dev}}; điều tần $\cos(50t+2\sin3t)$ có tần số tức thời cực đại lệch tần mang $\beta\Omega=6$: {{fm_dev}}.||If a mean angular frequency $\omega$ can be assigned, the analytic signal is written $V(t)e^{i\omega t}$; $V(t)$ is a time-varying phasor; $|V(t)|$ is the instantaneous amplitude, or envelope, and the time rate of change of phase is the instantaneous frequency (Bracewell, pp. 362 to 363). Bracewell warns: $\omega$ and $V(t)$ are in general not uniquely defined, so when you see the term envelope be prepared for surprises. Measured: the AM signal $(1+0.5\cos3t)\cos50t$ has envelope $1+0.5\cos3t$ with deviation {{env_dev}}; the FM signal $\cos(50t+2\sin3t)$ has maximum instantaneous frequency deviation $\beta\Omega=6$ from the carrier: {{fm_dev}}.⟧")),
                ("⟦Nhân quả và cặp Hilbert||Causality and Hilbert pairs⟧",
                 P(r"⟦Đáp ứng xung $I(t)$ của hệ vật lý bằng 0 khi $t<0$: nhân quả (\"khả thi vật lý\" là thuật ngữ không tốt vì hệ có thể khó xây vì lý do khác). Tách $I=E+O$ chẵn và lẻ với $O=\mathrm{sgn}\,t\,E$ nên $I=(1+\mathrm{sgn}\,t)E$, và biến đổi $T(f)=G(f)+iB(f)$ với $B=F_{\mathrm{Hi}}[G]$: phần thực và ảo của hàm truyền nhân quả là cặp Hilbert; $B(f)=\tfrac{2f}\pi\int_0^\infty\dfrac{G(u)\,du}{u^2-f^2}$ (giá trị chính) và $G(f)=\ldots$ (Kramers-Kronig, tr. 363 đến 364). Ví dụ $I(t)=e^{-t}H(t)$: $T=\dfrac1{1+i2\pi f}$, $G=\dfrac1{1+4\pi^2f^2}$, $B=\dfrac{-2\pi f}{1+4\pi^2f^2}$. Tại $f=0.3$: $B$ = {{kk_b}} từ công thức và {{kk_num}} từ giá trị chính số, lệch {{kk_dev}}.||The impulse response $I(t)$ of a physical system is zero for $t<0$: causal (\"physical realisability\" is a bad term since a system may be impossible to build for other reasons). Split $I=E+O$ into even and odd with $O=\mathrm{sgn}\,t\,E$ so $I=(1+\mathrm{sgn}\,t)E$, and the transform $T(f)=G(f)+iB(f)$ with $B=F_{\mathrm{Hi}}[G]$: the real and imaginary parts of a causal transfer function are a Hilbert pair; $B(f)=\tfrac{2f}\pi\int_0^\infty\dfrac{G(u)\,du}{u^2-f^2}$ (principal value) and $G(f)=\ldots$ (Kramers-Kronig, pp. 363 to 364). Example $I(t)=e^{-t}H(t)$: $T=\dfrac1{1+i2\pi f}$, $G=\dfrac1{1+4\pi^2f^2}$, $B=\dfrac{-2\pi f}{1+4\pi^2f^2}$. At $f=0.3$: $B$ = {{kk_b}} from the formula and {{kk_num}} from a numerical principal-value integral, deviation {{kk_dev}}.⟧")),
                ("⟦Tính biến đổi Hilbert bằng máy||Computing the Hilbert transform||⟧".replace("||⟧", "⟧"),
                 P(r"⟦Có vẻ đơn giản: rời rạc hóa, lấy DFT, nhân $i\,\mathrm{sgn}\,s$, nghịch đảo. Còn đơn giản hơn: chập với các hệ số của $-1/\pi x$ tại số nguyên. Với bán khoảng $N=5$ khoảng lấy mẫu, 11 hệ số là $\{.064\ .080\ .106\ .159\ .318\ 0\ -.318\ -.159\ -.106\ -.080\ -.064\}$ ({{dh_a}} tại $\pm5$, {{dh_b}} tại $\pm1$). Mối lo là các hệ số bị bỏ có tổng vô hạn, hy vọng hai vô cực triệt nhau; và khoảng lấy mẫu phải nhỏ để không chồng phổ. Đáp ứng tần số của 11 hệ số có pha đúng $\pm\pi/2$ nhưng biên độ không phải 1: chỉ một dải hẹp gần $s=${{dh_s}} có biên độ xấp xỉ 1 (cực đại {{dh_peak}}), tại $s=0.1$ là {{dh_a10}}, tại $0.25$ là {{dh_a25}}, tại $0.4$ là {{dh_a40}} (tr. 364 đến 366). Cách Fourier cũng hỏng tương tự do chồng phổ.||It seems simple: discretise, take the DFT, multiply by $i\,\mathrm{sgn}\,s$, invert. Simpler still: convolve with coefficients of $-1/\pi x$ at integers. With a semispan of $N=5$ sample spacings, the 11 coefficients are $\{.064\ .080\ .106\ .159\ .318\ 0\ -.318\ -.159\ -.106\ -.080\ -.064\}$ ({{dh_a}} at $\pm5$, {{dh_b}} at $\pm1$). The concern is that the discarded coefficients have an infinite sum, hoping the two infinities cancel; and the sampling interval must be small against aliasing. The frequency response of the 11 coefficients has the right phase $\pm\pi/2$ but the amplitude is not 1: only a narrow band near $s=${{dh_s}} has amplitude near 1 (maximum {{dh_peak}}), at $s=0.1$ it is {{dh_a10}}, at $0.25$ it is {{dh_a25}}, at $0.4$ it is {{dh_a40}} (pp. 364 to 366). The Fourier way fails similarly due to aliasing.⟧")),
                ("⟦Hilbert bằng biến đổi Hartley||The Hilbert transform with the Hartley transform⟧",
                 P(r"⟦Với dữ liệu $f(\tau)$, $\tau=0,\ldots,N-1$: lấy DHT $H(\nu)$, đổi chỗ $N/2-1$ cặp giá trị, với một phần tử của mỗi cặp đổi dấu: $\{H(0),H(1),\ldots,H(7)\}\to\{H(0),-H(7),-H(6),-H(5),H(4),H(3),H(2),H(1)\}$ (với $N=8$); rồi lấy DHT ngược để có biến đổi Hilbert (Pei và Jaw, 1989; Bracewell, tr. 366 đến 367). Số đo: với tín hiệu trung bình 0, không có thành phần Nyquist, cách hoán vị DHT trùng cách bộ lọc $i\,\mathrm{sgn}\,s$ của FFT với độ lệch {{hh_dev}}; nếu đổi dấu tổng thể thì lệch {{hh_wrong}}, nên phải theo đúng dấu. (Các thành phần dc và Nyquist mà cả hai cách xử lý khác nhau nên bị loại khỏi phép thử.)||For data $f(\tau)$, $\tau=0,\ldots,N-1$: take the DHT $H(\nu)$, swap $N/2-1$ pairs of values, with one element of each pair changing sign: $\{H(0),H(1),\ldots,H(7)\}\to\{H(0),-H(7),-H(6),-H(5),H(4),H(3),H(2),H(1)\}$ (for $N=8$); then take the inverse DHT to get the Hilbert transform (Pei and Jaw, 1989; Bracewell, pp. 366 to 367). Measured: for a zero-mean signal with no Nyquist component, the DHT swap agrees with the FFT $i\,\mathrm{sgn}\,s$ filter to deviation {{hh_dev}}; with an overall sign flip the deviation is {{hh_wrong}}, so the signs must be followed exactly. (The dc and Nyquist components, treated differently by the two methods, are excluded from the test.)⟧")),
                ("⟦Biến đổi Fourier phân số: định nghĩa||The fractional Fourier transform: definition⟧",
                 P(r"⟦Áp dụng $\mathcal F$ hai lần cho $f(-x)$, bốn lần quay lại $f(x)$: nếu $\mathcal F^a$ với $a$ nguyên có tính nhất quán, cộng tính, giao hoán, tuyến tính, liệu có $\mathcal F^{1/2}$ mà áp dụng hai lần cho $\mathcal F$? Với hai chiều, $\mathcal F^2$ là phép quay $\pi$ và $\mathcal F^4$ quay $2\pi$. Vật lý: trường ở mặt phẳng trung gian giữa mặt phẳng vào và mặt phẳng biến đổi (nhiễu xạ Fraunhofer), hay trong sợi quang có chiết suất phân bậc bình phương $n=n_0(1-r^2/h^2)$ mà biến đổi bậc $a$ nằm ở khoảng cách $aL$ với $L=\pi h/2\sqrt{2n_0}$ (Bracewell, tr. 367 đến 369). Định nghĩa (Namias, 1980), với $\phi=\tfrac12\pi a$: $\mathcal F^af(\xi)=\sqrt{1-i\cot\phi}\,e^{i\pi\xi^2\cot\phi}\int f(t)\,e^{i\pi t^2\cot\phi}e^{-i2\pi\xi t/\sin\phi}dt$ (dạng chuẩn hóa theo đơn vị Fourier quen); tại $a=1$ ($\phi=\pi/2$) nó là Fourier: số đo với Gauss lệch {{fr_ft}}.||Applying $\mathcal F$ twice gives $f(-x)$, four times returns $f(x)$: if $\mathcal F^a$ with integer $a$ has consistency, additivity, commutativity and linearity, can $\mathcal F^{1/2}$ exist that applied twice gives $\mathcal F$? In two dimensions $\mathcal F^2$ is a rotation by $\pi$ and $\mathcal F^4$ by $2\pi$. Physics: the field in an intermediate plane between the input plane and the transform plane (Fraunhofer diffraction), or in an optical fibre with quadratically graded index $n=n_0(1-r^2/h^2)$ where the transform of order $a$ appears at distance $aL$ with $L=\pi h/2\sqrt{2n_0}$ (Bracewell, pp. 367 to 369). The definition (Namias, 1980), with $\phi=\tfrac12\pi a$: $\mathcal F^af(\xi)=\sqrt{1-i\cot\phi}\,e^{i\pi\xi^2\cot\phi}\int f(t)\,e^{i\pi t^2\cot\phi}e^{-i2\pi\xi t/\sin\phi}dt$ (normalised to the familiar Fourier units); at $a=1$ ($\phi=\pi/2$) it is the Fourier transform: measured with a Gaussian the deviation is {{fr_ft}}.⟧")),
                ("⟦Cộng tính và hàm riêng Hermite-Gauss||Additivity and Hermite-Gauss eigenfunctions⟧",
                 P(r"⟦Bracewell: các hàm trực giao $H_n(\sqrt{2\pi}t)e^{-\pi t^2}$ ($H_n$ Hermite) là hàm riêng của biến đổi Fourier phân số: $\mathcal F^ah_n=e^{-in\phi}h_n$, $\phi=\tfrac12\pi a$; và đáng chú ý là các hàm sóng của dao động tử điều hòa lượng tử cũng là những hàm này, cũng là các mode của sợi quang chiết suất phân bậc và của hốc laser (tr. 370). Số đo $a=0.7$ (rời rạc hóa 700 điểm): độ lệch lớn nhất với $n=0,1,2,3$ là {{fr_eig}}; cộng tính $\mathcal F^{0.4}\mathcal F^{0.5}=\mathcal F^{0.9}$ lệch {{fr_add}}; pha của $n=1$ với $a=0.5$ bằng $-\pi/4$ = {{fr_ph}}. Ứng dụng: phương trình Schrödinger (Namias), quang học sợi, xử lý thông tin quang, xoay phân bố Wigner (phân tích thời gian-tần số, module 20) và Fourier Hartley phân số thực (Mendlovic, 1995).||Bracewell: the orthogonal functions $H_n(\sqrt{2\pi}t)e^{-\pi t^2}$ ($H_n$ Hermite) are eigenfunctions of the fractional Fourier transform: $\mathcal F^ah_n=e^{-in\phi}h_n$, $\phi=\tfrac12\pi a$; and strikingly the quantum harmonic-oscillator wave functions are these same functions, also the modes of a graded-index fibre and of a laser cavity (p. 370). Measured for $a=0.7$ (discretised on 700 points): the largest deviation over $n=0,1,2,3$ is {{fr_eig}}; the additivity $\mathcal F^{0.4}\mathcal F^{0.5}=\mathcal F^{0.9}$ deviates by {{fr_add}}; the phase of $n=1$ at $a=0.5$ equals $-\pi/4$ = {{fr_ph}}. Applications: the Schrödinger equation (Namias), fibre optics, optical information processing, rotation of the Wigner distribution (time-frequency analysis, module 20) and the real fractional Hartley transform (Mendlovic, 1995).⟧")),
                ("⟦Tự kiểm tra phần 5||Self-check, part 5⟧",
                 UL([r"⟦Áp dụng biến đổi Hilbert hai lần cho gì?||What does applying the Hilbert transform twice give?⟧",
                     r"⟦Tín hiệu giải tích của $\cos t$ là gì?||What is the analytic signal of $\cos t$?⟧",
                     r"⟦Vì sao phần thực và ảo của hàm truyền nhân quả là cặp Hilbert?||Why are the real and imaginary parts of a causal transfer function a Hilbert pair?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: $-f$; $e^{it}$; vì $I=(1+\\mathrm{sgn}\\,t)E$ nên phổ là $G$ cộng Hilbert của $G$.||Hints: $-f$; $e^{it}$; because $I=(1+\\mathrm{sgn}\\,t)E$ so the spectrum is $G$ plus the Hilbert transform of $G$.⟧</p>"),
            ]),
    ],
    takeaways=[
        "⟦Fourier hai chiều: xoay và cắt giữ cấu trúc; định lý affine chứa mọi trường hợp; ba chiều đối xứng cầu $K(s)=4\\pi\\int k\\,\\mathrm{sinc}(2sr)r^2dr$.||Two-dimensional Fourier: rotation and shear keep the structure; the affine theorem contains all cases; three dimensions with spherical symmetry $K(s)=4\\pi\\int k\\,\\mathrm{sinc}(2sr)r^2dr$.⟧",
        "⟦Hankel $F(q)=2\\pi\\int f J_0(2\\pi qr)r\\,dr$ đối ngược; đĩa $\\to aJ_1(2\\pi aq)/q$; định lý Hankel cho $J_\\nu$, $\\nu=\\pm\\tfrac12$ là cos và sin.||Hankel $F(q)=2\\pi\\int f J_0(2\\pi qr)r\\,dr$ is reciprocal; the disk $\\to aJ_1(2\\pi aq)/q$; Hankel's theorem gives $J_\\nu$, with $\\nu=\\pm\\tfrac12$ the cos and sin.⟧",
        "⟦Mellin $=$ Laplace sau $x=e^{-t}$, là mômen $s-1$; z là đa thức mẫu, tích chuỗi $=$ tích đa thức, $z=e^{p}$ nối Laplace.||Mellin $=$ Laplace after $x=e^{-t}$, a moment of order $s-1$; z is the polynomial of samples, the serial product $=$ the polynomial product, $z=e^{p}$ links Laplace.⟧",
        "⟦Abel $\\to$ Fourier $\\to$ Hankel trả lại hàm; định lý lát chiếu; chiếu ngược có sửa đổi lọc bằng $|q|$ rồi chiếu ngược.||Abel $\\to$ Fourier $\\to$ Hankel returns the function; the projection-slice theorem; modified back-projection filters by $|q|$ then back-projects.⟧",
        "⟦Hilbert dời pha $\\pm\\tfrac\\pi2$, $HH=-1$, tạo tín hiệu giải tích, đường bao, cặp nhân quả; Fourier phân số cộng tính, hàm riêng Hermite-Gauss với trị riêng $e^{-in\\phi}$.||Hilbert shifts phase by $\\pm\\tfrac\\pi2$, $HH=-1$, builds the analytic signal, the envelope, causal pairs; the fractional Fourier transform is additive with Hermite-Gauss eigenfunctions and eigenvalues $e^{-in\\phi}$.⟧",
    ],
    history="<p>⟦Hankel (biến đổi Bessel), Mellin (dùng cho lý thuyết hàm và hạt nhân Fourier), Abel (bài toán đường cong 1826) và Radon (1917) là các biến đổi cổ điển; Bracewell (1956) chứng minh vòng Abel-Fourier-Hankel và định lý lát chiếu; Bracewell và Riddle (1967) nêu chiếu ngược có sửa đổi trong thiên văn vô tuyến; Namias (1980) đưa Fourier phân số; Hilbert gắn với nhân quả và Kramers-Kronig (Bracewell, tr. 329 đến 374).||Hankel (Bessel transform), Mellin (used for function theory and Fourier kernels), Abel (the curve problem of 1826) and Radon (1917) are classical transforms; Bracewell (1956) proved the Abel-Fourier-Hankel ring and the projection-slice theorem; Bracewell and Riddle (1967) gave modified back-projection in radio astronomy; Namias (1980) introduced the fractional Fourier transform; Hilbert is tied to causality and Kramers-Kronig (Bracewell, pp. 329 to 374).⟧</p>",
    case="<p>⟦<b>Từ hình chiếu tới ảnh.</b> Một hình chụp cắt lớp gồm các hình chiếu $g_\\theta(R)$ của mật độ; mỗi hình chiếu là biến đổi Radon, và theo định lý lát chiếu, Fourier một chiều của nó là một lát của $F(u,v)$. Lọc dốc $|q|/M$ rồi chiếu ngược cho lại vật thể: tại tâm của hai Gauss, {{fb_c}} so với đúng 1, từ 180 hướng. Với vật đối xứng tròn, chuỗi Abel-Fourier-Hankel biến đường cong quét thành ảnh: Gauss $e^{-\\pi r^2}$ tại $r=0.6$ lấy lại {{arh_val}} với độ lệch {{arh_dev}}. Nếu tín hiệu quét là dao động điều biên, Hilbert cho đường bao: $1+0.5\\cos3t$ với độ lệch {{env_dev}}. Và nếu hệ nhân quả như $e^{-t}H(t)$, phần ảo $B(0.3)$ = {{kk_b}} suy ra từ phần thực qua giá trị chính Kramers-Kronig, khớp {{kk_num}}.||"
          "<b>From projections to an image.</b> A tomographic scan consists of projections $g_\\theta(R)$ of the density; each projection is a Radon transform, and by the projection-slice theorem its one-dimensional Fourier transform is a slice of $F(u,v)$. Ramp-filtering by $|q|/M$ then back-projecting returns the object: at the centre of the two Gaussians, {{fb_c}} against the exact 1, from 180 directions. For a circularly symmetric object the Abel-Fourier-Hankel chain turns the scan curve into the image: the Gaussian $e^{-\\pi r^2}$ at $r=0.6$ recovers {{arh_val}} with deviation {{arh_dev}}. If the scanned signal is an amplitude-modulated oscillation, Hilbert gives the envelope: $1+0.5\\cos3t$ with deviation {{env_dev}}. And if the system is causal like $e^{-t}H(t)$, the imaginary part $B(0.3)$ = {{kk_b}} follows from the real part through the Kramers-Kronig principal value, matching {{kk_num}}.⟧</p>",
    practice=[
        "⟦Mở notebook và chạy cell cài đặt.||Open the notebook and run the setup cell.⟧",
        "⟦Bài 1: kiểm tra định lý xoay và affine cho một Gauss ellip khác; đổi dấu trong mũ của định lý affine và xem sai số.||Task 1: check the rotation and affine theorems for another elliptical Gaussian; flip the sign in the exponent of the affine theorem and watch the error.⟧",
        "⟦Bài 2: tính Hankel bậc 0 của $e^{-ar}$ và đĩa bằng cầu phương, so với bảng 13.2, rồi tự đảo lại.||Task 2: compute the zero-order Hankel transform of $e^{-ar}$ and the disk by quadrature, compare with Table 13.2, then invert it yourself.⟧",
        "⟦Bài 3: dựng ảnh cắt lớp của hai Gauss với 30, 90, 180 hướng và vẽ sai số theo số hướng và theo $M$.||Task 3: build a tomographic image of two Gaussians with 30, 90, 180 directions and plot the error against the number of directions and against $M$.⟧",
        "⟦Bài 4: tính tín hiệu giải tích của một tín hiệu FM, vẽ đường bao và tần số tức thời, so với $\\beta\\Omega$.||Task 4: compute the analytic signal of an FM signal, plot the envelope and instantaneous frequency and compare with $\\beta\\Omega$.⟧",
    ],
    pitfalls=[
        "<b>⟦\"Dấu trong mũ của định lý affine không quan trọng.\"||\"The sign in the exponent of the affine theorem does not matter.\"⟧</b><p>⟦Đúng dấu $+$ lệch {{aff_dev}}; đổi dấu lệch {{aff_wrong}}.||The correct $+$ sign deviates {{aff_dev}}; the flipped sign deviates {{aff_wrong}}.⟧</p>",
        "<b>⟦\"Bộ lọc Hilbert 11 hệ số cho biên độ bằng 1 trên mọi tần số.\"||\"The 11-coefficient Hilbert filter has unit amplitude at every frequency.\"⟧</b><p>⟦Chỉ gần $s=${{dh_s}} (cực đại {{dh_peak}}); tại 0.4 còn {{dh_a40}} và tại 0.1 là {{dh_a10}}.||Only near $s=${{dh_s}} (maximum {{dh_peak}}); at 0.4 it is {{dh_a40}} and at 0.1 it is {{dh_a10}}.⟧</p>",
        "<b>⟦\"Chiếu ngược không lọc là đủ để tái tạo ảnh.\"||\"Unfiltered back-projection is enough to reconstruct the image.\"⟧</b><p>⟦Mật độ điểm trên nan hoa tỉ lệ $1/|q|$; phải nhân $|q|$, tức chập với nhân sửa đổi (kernel tại $q=2$ = {{kf_2}}).||The density of points on spokes goes as $1/|q|$; multiply by $|q|$, i.e. convolve with the modified kernel (the kernel at $q=2$ equals {{kf_2}}).⟧</p>",
        "<b>⟦\"Đường bao của tín hiệu luôn xác định duy nhất.\"||\"The envelope of a signal is always uniquely defined.\"⟧</b><p>⟦Bracewell cảnh báo phụ thuộc $\\omega$; chỉ với dải hẹp không chồng phổ mới có $1+0.5\\cos3t$ đúng (độ lệch {{env_dev}}).||Bracewell warns of the dependence on $\\omega$; only for a narrow band without overlap does $1+0.5\\cos3t$ come out right (deviation {{env_dev}}).⟧</p>",
    ],
    refs=[
        "⟦R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chương 13 (tr. 330 đến 374).||R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chapter 13 (pp. 330 to 374).⟧",
        "⟦Tài liệu do chương trích: Erdélyi et al. (1954), Deans (1983), Bracewell và Riddle (1967), Namias (1980), Mendlovic và Ozaktas (1993), Pei và Jaw (1989).||Works cited by the chapter: Erdélyi et al. (1954), Deans (1983), Bracewell and Riddle (1967), Namias (1980), Mendlovic and Ozaktas (1993), Pei and Jaw (1989).⟧",
    ],
    quiz=[
        Q("⟦FT hai chiều của $e^{-\\pi(x^2+y^2)}$ tại $(0.5,0.3)$ bằng bao nhiêu?||What is the 2D FT of $e^{-\\pi(x^2+y^2)}$ at $(0.5,0.3)$?⟧", "{{g2_cf}}", "0.7000", "0.1170", "0.5000", "⟦$e^{-\\pi(0.34)}$; số đo {{g2_num}}.||$e^{-\\pi(0.34)}$; measured {{g2_num}}.⟧"),
        Q("⟦Tổng các phần tử của chập hàng (5 phần tử) và cột (4 phần tử) là bao nhiêu?||What is the sum of elements of the convolution of a row (5 elements) and a column (4 elements)?⟧", "{{pc_sum}}", "20", "9", "45", "⟦$\\sum a\\cdot\\sum b$.||$\\sum a\\cdot\\sum b$.⟧"),
        Q("⟦Mômen bậc hai $\\iint r^2e^{-\\pi r^2}$ bằng bao nhiêu?||What is the second moment $\\iint r^2e^{-\\pi r^2}$?⟧", "{{mo_r2}}", "1.0000", "0.5000", "3.1416", "⟦$1/\\pi$.||$1/\\pi$.⟧"),
        Q("⟦Định lý xoay hai chiều: sai lệch số của hai vế xấp xỉ bao nhiêu?||Two-dimensional rotation theorem: what is the numerical deviation of the two sides?⟧", "{{rot_dev}}", "1.0e-01", "1.0e-03", "0.5000", "⟦Chỉ do rời rạc hóa lưới.||Only grid discretisation.⟧"),
        Q("⟦Định lý affine với dấu $-$ trong mũ lệch bao nhiêu?||By how much does the affine theorem deviate with a $-$ sign in the exponent?⟧", "{{aff_wrong}}", "1.0e-16", "1.0e-06", "0.0000", "⟦Dấu $+$ lệch {{aff_dev}}.||The $+$ sign deviates {{aff_dev}}.⟧"),
        Q("⟦Biến đổi 3D của khối cầu bán kính 1 tại $s=0$ bằng bao nhiêu?||What is the 3D transform of the unit-radius ball at $s=0$?⟧", "{{ball_s0}}", "3.1416", "1.0472", "12.566", "⟦$4\\pi/3$.||$4\\pi/3$.⟧"),
        Q("⟦Cùng khối cầu tại $s=1$ bằng bao nhiêu?||The same ball at $s=1$?⟧", "{{ball_s1}}", "0.3183", "-0.1592", "1.0000", "⟦$-1/\\pi$; tích phân số {{ball_num}}.||$-1/\\pi$; numerical integral {{ball_num}}.⟧"),
        Q("⟦Gauss 3D $e^{-\\pi r^2}$ tại $s=0.5$ bằng bao nhiêu?||What is the 3D Gaussian $e^{-\\pi r^2}$ at $s=0.5$?⟧", "{{g3_s}}", "0.7854", "0.2000", "0.3679", "⟦Tự biến đổi: $e^{-\\pi/4}$.||Self-transforming: $e^{-\\pi/4}$.⟧"),
        Q("⟦Giá trị của lập phương đơn vị 3D tại $(0.5,0.25,0.25)$ bằng bao nhiêu?||What is the 3D unit cube's transform at $(0.5,0.25,0.25)$?⟧", "{{cube_val}}", "0.5000", "0.1200", "0.9000", "⟦Tích ba $\\mathrm{sinc}$.||The product of three sincs.⟧"),
        Q("⟦Hankel của đĩa bán kính 1.5 tại $q=0.4$ bằng bao nhiêu?||What is the Hankel transform of a disk of radius 1.5 at $q=0.4$?⟧", "{{hk_cf}}", "1.5000", "0.9000", "2.2000", "⟦$aJ_1(2\\pi aq)/q$; số đo {{hk_num}}.||$aJ_1(2\\pi aq)/q$; measured {{hk_num}}.⟧"),
        Q("⟦Hankel của $e^{-1.3r}$ tại $q=0.4$ bằng bao nhiêu?||What is the Hankel transform of $e^{-1.3r}$ at $q=0.4$?⟧", "{{hk_e_cf}}", "0.4000", "1.0000", "0.1500", "⟦$2\\pi a(a^2+4\\pi^2q^2)^{-3/2}$.||$2\\pi a(a^2+4\\pi^2q^2)^{-3/2}$.⟧"),
        Q("⟦Áp dụng Hankel hai lần cho $e^{-1.3r}$ lệch $f(0.5)$ bao nhiêu?||By how much does applying Hankel twice to $e^{-1.3r}$ deviate from $f(0.5)$?⟧", "{{hk_rec_dev}}", "1.0e-02", "1.0e-06", "0.5000", "⟦Đối ngược; $f(0.5)$ = {{hk_rec_f}}.||Reciprocity; $f(0.5)$ = {{hk_rec_f}}.⟧"),
        Q("⟦Nghiệm đầu của $J_1$ (jinc) là bao nhiêu?||What is the first zero of $J_1$ (the jinc)?⟧", "{{airy_z}}", "2.4048", "5.1356", "3.1416", "⟦Vòng Airy đầu.||The first Airy ring.⟧"),
        Q("⟦Hankel $n=1,2,3$ của Gauss cho cùng giá trị nào tại $q=0.5$?||At $q=0.5$, which common value do the $n=1,2,3$ Hankel transforms of the Gaussian give?⟧", "{{nd_val}}", "0.2000", "0.7854", "0.6000", "⟦$e^{-\\pi q^2}$.||$e^{-\\pi q^2}$.⟧"),
        Q("⟦$\\Gamma(2.5)$ (Mellin của $e^{-x}$ tại $s=2.5$) bằng bao nhiêu?||What is $\\Gamma(2.5)$ (Mellin transform of $e^{-x}$ at $s=2.5$)?⟧", "{{ml_gam}}", "1.5000", "2.5000", "0.8862", "⟦Cả tích phân trực tiếp và Laplace.||Both the direct and Laplace integrals.⟧"),
        Q("⟦Mellin của $\\sin x$ tại $s=0.5$ bằng bao nhiêu?||What is the Mellin transform of $\\sin x$ at $s=0.5$?⟧", "{{ml_sin}}", "1.7725", "0.8862", "0.7071", "⟦$\\Gamma(\\tfrac12)\\sin\\tfrac\\pi4$.||$\\Gamma(\\tfrac12)\\sin\\tfrac\\pi4$.⟧"),
        Q("⟦Mellin của $1/(1+x)$ tại $s=0.3$ bằng bao nhiêu?||What is the Mellin transform of $1/(1+x)$ at $s=0.3$?⟧", "{{ml_rat}}", "1.5708", "2.2000", "5.1000", "⟦$\\pi/\\sin0.3\\pi$.||$\\pi/\\sin0.3\\pi$.⟧"),
        Q("⟦Phương sai quanh trọng tâm của $\\Pi(x-\\tfrac12)$ (từ Mellin) bằng bao nhiêu?||What is the variance about the centroid of $\\Pi(x-\\tfrac12)$ (from Mellin)?⟧", "{{mm_v}}", "0.2500", "0.3333", "0.1667", "⟦$1/12$.||$1/12$.⟧"),
        Q("⟦$K_M(0.3)K_M(0.7)$ cho hạt nhân $2\\cos2\\pi x$ bằng bao nhiêu?||What is $K_M(0.3)K_M(0.7)$ for the kernel $2\\cos2\\pi x$?⟧", "{{fk_prod}}", "2", "0.5", "4", "⟦Điều kiện hạt nhân Fourier.||The Fourier-kernel condition.⟧"),
        Q("⟦Phần tử cuối của đầu ra $\\{2\\,1\\}*\\{8\\,4\\,2\\,1\\}$ là bao nhiêu?||What is the last element of the output $\\{2\\,1\\}*\\{8\\,4\\,2\\,1\\}$?⟧", "{{z_o5}}", "4", "8", "2", "⟦$\\{16\\,16\\,8\\,4\\,1\\}$.||$\\{16\\,16\\,8\\,4\\,1\\}$.⟧"),
        Q("⟦$\\sum nz^{-n}$ tại $z=2$ bằng bao nhiêu?||What is $\\sum nz^{-n}$ at $z=2$?⟧", "{{z_n1}}", "1", "4", "0.5", "⟦$z^{-1}/(1-z^{-1})^2$.||$z^{-1}/(1-z^{-1})^2$.⟧"),
        Q("⟦$\\sum n^2z^{-n}$ tại $z=2$ bằng bao nhiêu?||What is $\\sum n^2z^{-n}$ at $z=2$?⟧", "{{z_n2}}", "4", "8", "3", "⟦$z^{-1}(1+z^{-1})/(1-z^{-1})^3=6$.||$z^{-1}(1+z^{-1})/(1-z^{-1})^3=6$.⟧"),
        Q("⟦Hệ số $c_1$ của bảng Abel $2(\\sqrt2-1)$ bằng bao nhiêu?||What is the Abel-table coefficient $c_1=2(\\sqrt2-1)$?⟧", "{{ab_k1}}", "1.4142", "0.4142", "1.2000", "⟦Bảng 13.10: 0.828.||Table 13.10: 0.828.⟧"),
        Q("⟦Biến đổi Abel của đĩa bán kính 1 tại $x=0.6$ bằng bao nhiêu?||What is the Abel transform of a unit disk at $x=0.6$?⟧", "{{ab_disk}}", "0.8000", "1.2000", "2.0000", "⟦$2\\sqrt{1-0.36}$.||$2\\sqrt{1-0.36}$.⟧"),
        Q("⟦$\\int f_A\\,dx$ cho $f=1-r$ ($r<1$) bằng bao nhiêu?||What is $\\int f_A\\,dx$ for $f=1-r$ ($r<1$)?⟧", "{{ab_area}}", "0.5000", "3.1416", "2.0944", "⟦$2\\pi\\int f\\,r\\,dr=\\pi/3$.||$2\\pi\\int f\\,r\\,dr=\\pi/3$.⟧"),
        Q("⟦Thuật toán bảng cho $F_A(5)$ của $(10-p)^{1/2}$ cho giá trị nào (đúng 7.854)?||The table algorithm for $F_A(5)$ of $(10-p)^{1/2}$ gives what value (exact 7.854)?⟧", "{{ab_alg}}", "8.5400", "7.1000", "7.5000", "⟦Sách 7.78.||The book gives 7.78.⟧"),
        Q("⟦$f_A(0.5)$ cho $f=1-r$ bằng bao nhiêu (sách .5368)?||What is $f_A(0.5)$ for $f=1-r$ (book .5368)?⟧", "{{ab_x5}}", "0.5000", "0.4500", "0.6100", "⟦Khớp trong 0.001.||Agreeing within 0.001.⟧"),
        Q("⟦Độ lệch sau ba bước Abel, Fourier, Hankel cho Gauss là bao nhiêu?||What is the deviation after the three steps Abel, Fourier, Hankel for the Gaussian?⟧", "{{arh_dev}}", "1.0e-02", "0.1000", "1.0e-12", "⟦Trả lại $f(0.6)$ = {{arh_val}}.||Returns $f(0.6)$ = {{arh_val}}.⟧"),
        Q("⟦Hình chiếu $g_\\theta(0.3)$ của Gauss ellip ($a=2$, $b=0.5$, $\\theta=0.6$) bằng bao nhiêu?||What is the projection $g_\\theta(0.3)$ of the elliptical Gaussian ($a=2$, $b=0.5$, $\\theta=0.6$)?||⟧".replace("||⟧", "⟧"), "{{rd_cf}}", "0.6000", "1.0000", "0.2500", "⟦Số đo {{rd_num}}.||Measured {{rd_num}}.⟧"),
        Q("⟦Biến đổi Fourier của nhân sửa đổi (M=6) tại $q=2$ bằng bao nhiêu?||What is the Fourier transform of the modified kernel ($M=6$) at $q=2$?⟧", "{{kf_2}}", "0.5000", "1.0000", "0.1667", "⟦$|q|/M=2/6$.||$|q|/M=2/6$.⟧"),
        Q("⟦Tái tạo cắt lớp tại tâm của hai Gauss (đúng 1) cho bao nhiêu?||What does the tomographic reconstruction give at the centre of the two Gaussians (exact 1)?⟧", "{{fb_c}}", "0.9000", "1.1000", "0.5000", "⟦Sai số phụ thuộc $M$, không phụ thuộc số hướng.||The error depends on $M$, not on the number of directions.⟧"),
        Q("⟦Hilbert của $\\Pi(x)$ tại $x=1$ bằng bao nhiêu?||What is the Hilbert transform of $\\Pi(x)$ at $x=1$?⟧", "{{hr_1}}", "0.3497", "-0.5000", "-0.1749", "⟦$\\tfrac1\\pi\\ln|0.5/1.5|$.||$\\tfrac1\\pi\\ln|0.5/1.5|$.⟧"),
        Q("⟦Hilbert của $\\Pi(x)$ tại $x=0.2$ (giá trị chính) bằng bao nhiêu?||What is the Hilbert transform of $\\Pi(x)$ at $x=0.2$ (principal value)?⟧", "{{hr_02}}", "0.2697", "-0.6000", "-0.1349", "⟦$\\tfrac1\\pi\\ln(0.3/0.7)$.||$\\tfrac1\\pi\\ln(0.3/0.7)$.⟧"),
        Q("⟦Tần số tức thời cực đại lệch tần mang của $\\cos(50t+2\\sin3t)$ bằng bao nhiêu?||What is the maximum instantaneous-frequency deviation from the carrier of $\\cos(50t+2\\sin3t)$?⟧", "{{fm_dev}}", "2.000", "3.000", "12.00", "⟦$\\beta\\Omega=2\\times3$.||$\\beta\\Omega=2\\times3$.⟧"),
        Q("⟦Phần ảo $B(0.3)$ của $1/(1+i2\\pi f)$ (cặp Hilbert của $G$) bằng bao nhiêu?||What is the imaginary part $B(0.3)$ of $1/(1+i2\\pi f)$ (the Hilbert pair of $G$)?⟧", "{{kk_b}}", "0.4140", "-0.2070", "-0.8280", "⟦Giá trị chính số: {{kk_num}}.||Numerical principal value: {{kk_num}}.⟧"),
        Q("⟦Hệ số chập của bộ lọc Hilbert 11 phần tử tại $\\pm1$ là bao nhiêu?||What is the coefficient of the 11-element Hilbert filter at $\\pm1$?⟧", "{{dh_b}}", "0.5000", "0.1590", "0.6370", "⟦$1/\\pi$.||$1/\\pi$.⟧"),
        Q("⟦Cực đại biên độ của bộ lọc Hilbert 11 hệ số là bao nhiêu?||What is the maximum amplitude of the 11-coefficient Hilbert filter?⟧", "{{dh_peak}}", "0.5500", "1.5000", "0.7000", "⟦Tại $s\\approx${{dh_s}}.||At $s\\approx${{dh_s}}.⟧"),
        Q("⟦Biên độ của bộ lọc đó tại $s=0.4$ bằng bao nhiêu?||What is the amplitude of that filter at $s=0.4$?⟧", "{{dh_a40}}", "0.9700", "0.5500", "0.5000", "⟦Chỉ một dải hẹp gần 1.||Only a narrow band is near 1.⟧"),
        Q("⟦Độ lệch của phép hoán vị DHT so với bộ lọc FFT $i\\,\\mathrm{sgn}\\,s$ là bao nhiêu?||What is the deviation of the DHT swap from the FFT $i\\,\\mathrm{sgn}\\,s$ filter?⟧", "{{hh_dev}}", "1.0e-03", "0.5000", "1.0e-01", "⟦Với dc và Nyquist bằng 0.||With dc and Nyquist equal to zero.⟧"),
        Q("⟦Pha của hàm riêng $n=1$ dưới biến đổi Fourier phân số $a=0.5$ bằng bao nhiêu?||What is the phase of the $n=1$ eigenfunction under the fractional Fourier transform with $a=0.5$?⟧", "{{fr_ph}}", "-1.5708", "0.7854", "-0.3927", "⟦$-n\\phi=-\\pi/4$.||$-n\\phi=-\\pi/4$.⟧"),
        Q("⟦Độ lệch cộng tính $\\mathcal F^{0.4}\\mathcal F^{0.5}$ so với $\\mathcal F^{0.9}$ xấp xỉ bao nhiêu?||What is the additivity deviation of $\\mathcal F^{0.4}\\mathcal F^{0.5}$ against $\\mathcal F^{0.9}$?⟧", "{{fr_add}}", "1.0e-02", "0.1000", "1.0e-06", "⟦Rời rạc hóa 700 điểm.||A 700-point discretisation.⟧"),
        Q("⟦Biến đổi Fourier hai chiều của hàm bị xoay thì thế nào?||What happens to the 2D transform of a rotated function?⟧", "⟦Xoay cùng góc, cùng chiều||It rotates through the same angle in the same sense⟧", "⟦Xoay ngược chiều với góc bằng một nửa góc ban đầu, do chuẩn hóa||It rotates in the opposite sense through half the original angle, due to normalisation⟧", "⟦Giữ nguyên vì biên độ Fourier không đổi dưới phép xoay||It stays unchanged since the Fourier amplitude is invariant under rotation⟧", "⟦Xoay $90^\\circ$ bất kể góc ban đầu||It rotates through $90^\\circ$ regardless of the original angle⟧", "⟦Bracewell, tr. 332.||Bracewell, p. 332.⟧"),
        Q("⟦Vì sao Hankel bậc 0 đối ngược chặt chẽ?||Why is the zero-order Hankel transform strictly reciprocal?⟧", "⟦Nó suy từ Fourier 2D đối xứng tròn||It follows from the symmetric 2D FT⟧", "⟦Vì $J_0$ thực nên biến đổi luôn tự nghịch đảo với mọi hàm||Because $J_0$ is real so the transform is always self-inverse for every function⟧", "⟦Vì $J_0$ trực giao với chính nó trên nửa đường thẳng dương||Because $J_0$ is orthogonal to itself on the positive half line⟧", "⟦Vì thừa số $2\\pi$ triệt tiêu ở biến đổi ngược||Because the factor $2\\pi$ cancels in the inverse transform⟧", "⟦Bracewell, tr. 336.||Bracewell, p. 336.⟧"),
        Q("⟦Biến đổi Mellin liên hệ với Laplace bằng phép đổi biến nào?||Which change of variable relates the Mellin transform to Laplace?⟧", "⟦$x=e^{-t}$||$x=e^{-t}$⟧", "⟦$x=\\ln t$, đưa tích phân về khoảng hữu hạn||$x=\\ln t$, taking the integral to a finite range⟧", "⟦$x=t^2$, vì Mellin là Laplace của bình phương||$x=t^2$, since Mellin is the Laplace transform of the square⟧", "⟦$x=1/t$, đảo trục thời gian||$x=1/t$, reversing the time axis⟧", "⟦Bracewell, tr. 343.||Bracewell, p. 343.⟧"),
        Q("⟦Tích chuỗi hai dãy tương ứng với gì ở biến đổi z?||What does the serial product of two sequences correspond to in the z transform?⟧", "⟦Tích hai đa thức $F(z)H(z)$||The product of the two polynomials $F(z)H(z)$⟧", "⟦Tổng hai đa thức vì chập tương ứng phép cộng||The sum of the two polynomials since convolution corresponds to addition⟧", "⟦Chập hai đa thức như hai dãy hệ số||The convolution of the two polynomials as two coefficient sequences⟧", "⟦Đạo hàm của tích hai đa thức theo $z$||The derivative of the product of the polynomials with respect to $z$⟧", "⟦Bracewell, tr. 348.||Bracewell, p. 348.⟧"),
        Q("⟦Vì sao chiếu ngược cần hệ số $|q|$?||Why does back-projection need the factor $|q|$?⟧", "⟦Mật độ điểm trên các nan hoa tỉ lệ nghịch với bán kính||The density of points on the spokes is inversely proportional to radius⟧", "⟦Vì hình chiếu bị làm mờ bởi đường kính hữu hạn của khe||Because the projection is blurred by the finite width of the slit⟧", "⟦Vì định lý lát chiếu chỉ đúng cho tần số dương||Because the projection-slice theorem holds only for positive frequencies⟧", "⟦Vì Radon là tích phân đường nên nhân đôi năng lượng||Because Radon is a line integral so it doubles the energy⟧", "⟦Bracewell, tr. 358.||Bracewell, p. 358.⟧"),
        Q("⟦Tín hiệu giải tích có tính chất phổ nào?||What spectral property does the analytic signal have?⟧", "⟦Không có tần số âm||No negative frequencies⟧", "⟦Không có thành phần tần số dương, chỉ có phần âm||It has no positive-frequency components, only the negative part⟧", "⟦Có phổ chẵn thực với mọi tín hiệu thực||It has a real even spectrum for every real signal⟧", "⟦Có phổ phẳng bằng 1 trên mọi tần số||It has a flat spectrum equal to 1 at all frequencies⟧", "⟦Bracewell, tr. 362.||Bracewell, p. 362.⟧"),
    ],
    nb=[
        ("md", """## 1. ⟦Fourier hai và ba chiều||Two- and three-dimensional Fourier transforms⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Các định lý hai chiều (xoay, cắt, affine, mômen) và biến đổi khối cầu 3D có đúng số, tính bằng tổng trên lưới và bằng công thức?||Do the two-dimensional theorems (rotation, shear, affine, moments) and the 3D ball transform hold numerically, computed by sums on a grid and by formulas?⟧"""),
        ("code", r'''from scipy import integrate, special, signal
trap = getattr(np, "trapezoid", None) or np.trapz
rg = np.random.default_rng(16)
h_ = np.arange(-8, 8, 0.04); X, Y = np.meshgrid(h_, h_, indexing="ij"); dxy = 0.04
def FT2(fun, u, v): return np.sum(fun(X, Y)*np.exp(-2j*np.pi*(u*X + v*Y)))*dxy*dxy
gg = lambda x, y: np.exp(-np.pi*(x**2 + y**2))
u0, v0 = 0.5, 0.3
num = FT2(gg, u0, v0); cf = np.exp(-np.pi*(u0**2 + v0**2))
assert abs(num - cf) < 1e-10
report("g2_num", num.real, ".4f"); report("g2_cf", cf, ".4f"); report("g2_dev", max(abs(num - cf), 1e-16), ".0e")
# ⟦tích và chập||product and convolution⟧
a = np.array([1, 2, 3, 2, 1.]); b = np.array([1, 3, 3, 1.])
cv = signal.convolve2d(a[None, :], b[:, None]); assert np.allclose(cv, np.outer(b, a))
report("pc_dev", max(np.max(np.abs(cv - np.outer(b, a))), 1e-16), ".0e"); report("pc_sum", cv.sum(), ".0f")
# ⟦mômen||moments⟧
mo_num = np.sum((X**2 + Y**2)*gg(X, Y))*dxy*dxy
Fuu = -2*np.pi; mo_der = -(Fuu + Fuu)/(4*np.pi**2)
assert abs(mo_num - 1/np.pi) < 1e-9 and abs(mo_der - 1/np.pi) < 1e-12 and abs(np.sum(gg(X, Y))*dxy*dxy - 1) < 1e-10
report("mo_F0", 1.0, ".0f"); report("mo_r2", 1/np.pi, ".4f")
# ⟦xoay||rotation⟧
f0 = lambda x, y: np.exp(-np.pi*(4*x**2 + y**2/4)); F0f = lambda u, v: np.exp(-np.pi*(u**2/4 + 4*v**2))
th = 0.6; fr_ = lambda x, y: f0(x*np.cos(th) - y*np.sin(th), x*np.sin(th) + y*np.cos(th))
u1, v1 = 0.3, 0.2
lhs = FT2(fr_, u1, v1); rhs = F0f(u1*np.cos(th) - v1*np.sin(th), u1*np.sin(th) + v1*np.cos(th))
assert abs(lhs - rhs) < 1e-9; report("rot_dev", max(abs(lhs - rhs), 1e-16), ".0e")
# ⟦cắt||shear⟧
bs = 0.5; fsh = lambda x, y: gg(x + bs*y, y); u2, v2 = 0.4, 0.3
lhs = FT2(fsh, u2, v2); rhs = np.exp(-np.pi*(u2**2 + (v2 - bs*u2)**2))
assert abs(lhs - rhs) < 1e-9; report("shr_dev", max(abs(lhs - rhs), 1e-16), ".0e")
# ⟦affine||affine⟧
Fa = lambda x, y: np.exp(-np.pi*(x**2 + 2*y**2 + 0.5*x*y))
ap, bp, cp, dp, ep, fp = 1.2, 0.3, 0.4, -0.2, 0.9, -0.3
faf = lambda x, y: Fa(ap*x + bp*y + cp, dp*x + ep*y + fp)
u3, v3 = 0.35, -0.2; det = ap*ep - bp*dp
arg = ((ep*u3 - dp*v3)/det, (-bp*u3 + ap*v3)/det)
lhs = FT2(faf, u3, v3)
right = abs(det)**-1*np.exp(1j*2*np.pi/det*((ep*cp - bp*fp)*u3 + (ap*fp - cp*dp)*v3))*FT2(Fa, *arg)
wrong = abs(det)**-1*np.exp(-1j*2*np.pi/det*((ep*cp - bp*fp)*u3 + (ap*fp - cp*dp)*v3))*FT2(Fa, *arg)
assert abs(lhs - right) < 1e-9 and abs(lhs - wrong) > 0.1
report("aff_dev", max(abs(lhs - right), 1e-16), ".0e"); report("aff_wrong", abs(lhs - wrong), ".2f")
# ⟦3D: khối cầu||3D: the ball⟧
ball = lambda s_: (np.sin(2*np.pi*s_) - 2*np.pi*s_*np.cos(2*np.pi*s_))/(2*np.pi**2*s_**3)
sv = 1.0
bnum = 4*np.pi*integrate.quad(lambda r: np.sinc(2*sv*r)*r*r, 0, 1)[0]
assert abs(bnum - ball(sv)) < 1e-12 and abs(ball(1.0) + 1/np.pi) < 1e-12
vol0 = 4*np.pi*integrate.quad(lambda r: r*r, 0, 1)[0]; assert abs(vol0 - 4*np.pi/3) < 1e-12
report("ball_s0", vol0, ".4f"); report("ball_s1", ball(1.0), ".4f"); report("ball_num", bnum, ".4f")
sg = 0.5; g3 = 4*np.pi*integrate.quad(lambda r: np.exp(-np.pi*r*r)*np.sinc(2*sg*r)*r*r, 0, 12)[0]
assert abs(g3 - np.exp(-np.pi*sg**2)) < 1e-10; report("g3_s", g3, ".4f")
cube = np.sinc(0.5)*np.sinc(0.25)*np.sinc(0.25)
xs_ = np.linspace(-0.5, 0.5, 4001); cu = trap(np.cos(2*np.pi*0.5*xs_), xs_)*trap(np.cos(2*np.pi*0.25*xs_), xs_)**2
assert abs(cu - cube) < 1e-6; report("cube_val", cube, ".4f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Gauss 2D {{g2_num}} và {{g2_cf}}; chập {{pc_sum}}; mômen {{mo_r2}}; xoay {{rot_dev}}; cắt {{shr_dev}}; affine {{aff_dev}} và sai dấu {{aff_wrong}}; khối cầu {{ball_s0}}, {{ball_s1}}; Gauss 3D {{g3_s}}; lập phương {{cube_val}}.||2D Gaussian {{g2_num}} and {{g2_cf}}; convolution {{pc_sum}}; moment {{mo_r2}}; rotation {{rot_dev}}; shear {{shr_dev}}; affine {{aff_dev}} and wrong sign {{aff_wrong}}; ball {{ball_s0}}, {{ball_s1}}; 3D Gaussian {{g3_s}}; cube {{cube_val}}.⟧"""),
        ("md", """## 2. ⟦Hankel và hạt nhân Fourier||Hankel and Fourier kernels⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Các cặp Hankel (đĩa, mũ, Gauss) có khớp bảng, biến đổi có đối ngược, $J_{\\pm1/2}$ có cho cos và sin, và Hankel $n$ chiều có cho cùng Gauss?||Do the Hankel pairs (disk, exponential, Gaussian) match the table, is the transform reciprocal, do $J_{\\pm1/2}$ give cos and sin, and does the $n$-dimensional Hankel transform give the same Gaussian?⟧"""),
        ("code", r'''J0 = special.j0; J1 = special.j1
hank = lambda fun, q, upper=np.inf: 2*np.pi*integrate.quad(lambda r: fun(r)*J0(2*np.pi*q*r)*r, 0, upper, limit=400)[0]
a_d, q_ = 1.5, 0.4
disk_num = hank(lambda r: 1.0, q_, a_d); disk_cf = a_d*J1(2*np.pi*a_d*q_)/q_
assert abs(disk_num - disk_cf) < 1e-10; report("hk_num", disk_num, ".4f"); report("hk_cf", disk_cf, ".4f")
ae = 1.3; e_num = hank(lambda r: np.exp(-ae*r), q_, 60); e_cf = 2*np.pi*ae*(ae**2 + 4*np.pi**2*q_**2)**-1.5
assert abs(e_num - e_cf) < 1e-9; report("hk_e_num", e_num, ".4f"); report("hk_e_cf", e_cf, ".4f")
gq = hank(lambda r: np.exp(-np.pi*r*r), 0.5, 12); assert abs(gq - np.exp(-np.pi*0.25)) < 1e-10; report("hk_g", gq, ".4f")
# ⟦đối ngược: áp dụng hai lần cho e^{-ar}||reciprocity: apply twice to e^{-ar}⟧
Fq = lambda q: 2*np.pi*ae*(ae**2 + 4*np.pi**2*q**2)**-1.5
back = 2*np.pi*integrate.quad(lambda q: Fq(q)*J0(2*np.pi*q*0.5)*q, 0, 400, limit=2000)[0]
tail = 2*np.pi*(2*np.pi*ae)*(2*np.pi)**-3*(1/400)  # ⟦đuôi ~ 1/q² của tích phân nhân J0 ≈ dao động, bỏ qua||the tail is oscillatory and negligible⟧
assert abs(back - np.exp(-ae*0.5)) < 5e-4
report("hk_rec_f", np.exp(-ae*0.5), ".4f"); report("hk_rec_dev", max(abs(back - np.exp(-ae*0.5)), 1e-16), ".0e")
# ⟦định lý||theorems⟧
hd_int = 2*np.pi*integrate.quad(lambda r: np.exp(-np.pi*r*r)*r, 0, 12)[0]; assert abs(hd_int - 1) < 1e-10
rl = 2*np.pi*integrate.quad(lambda r: np.exp(-2*np.pi*r*r)*r, 0, 12)[0]; rr = 2*np.pi*integrate.quad(lambda q: np.exp(-2*np.pi*q*q)*q, 0, 12)[0]
assert abs(rl - rr) < 1e-12; report("hd_int", hd_int, ".0f"); report("hd_ray_l", rl, ".4f"); report("hd_ray_r", rr, ".4f")
# ⟦Abel rồi Fourier: Hankel = Fourier ∘ Abel||Abel then Fourier: Hankel = Fourier ∘ Abel⟧
xg = np.arange(0, 6.0001, 0.02)
A_num = np.array([2*integrate.quad(lambda t: np.exp(-np.pi*(x_**2 + t**2)), 0, 8)[0] for x_ in xg])
assert np.max(np.abs(A_num - np.exp(-np.pi*xg**2))) < 1e-9
sgg = np.arange(0, 6.0001, 0.02)
Fs_ = np.array([2*trap(A_num*np.cos(2*np.pi*s_*xg), xg) for s_ in sgg])
q_half = 0.5; nh_abel = 2*np.pi*trap(Fs_*J0(2*np.pi*sgg*0.0 + 0)*0, sgg) if False else 0
Fh_q = np.interp(q_half, sgg, Fs_)
nh_direct = hank(lambda r: np.exp(-np.pi*r*r), 0.5, 12)
assert abs(Fh_q - np.exp(-np.pi*0.25)) < 1e-4 and abs(nh_direct - np.exp(-np.pi*0.25)) < 1e-10
report("nh_direct", nh_direct, ".4f"); report("nh_abel", Fh_q, ".4f"); report("nh_cf", np.exp(-np.pi*0.25), ".4f")
# ⟦J_{±1/2}||J_{±1/2}⟧
z = 2.3; jm = special.jv(-0.5, z) - np.sqrt(2/(np.pi*z))*np.cos(z); jp = special.jv(0.5, z) - np.sqrt(2/(np.pi*z))*np.sin(z)
assert abs(jm) < 1e-13 and abs(jp) < 1e-13; report("jv_dev", max(abs(jm), abs(jp), 1e-16), ".0e")
# ⟦Hankel n chiều||n-dimensional Hankel⟧
def hn(n, q):
    return 2*np.pi*q**(1 - n/2)*integrate.quad(lambda r: np.exp(-np.pi*r*r)*special.jv(n/2 - 1, 2*np.pi*q*r)*r**(n/2), 0, 12)[0]
vals = [hn(n, 0.5) for n in (1, 2, 3)]
assert max(abs(v_ - np.exp(-np.pi*0.25)) for v_ in vals) < 1e-9
report("nd_val", vals[0], ".4f"); report("nd_dev", max(max(abs(v_ - np.exp(-np.pi*0.25)) for v_ in vals), 1e-16), ".0e")
zj = special.jn_zeros(1, 1)[0]; assert abs(zj - 3.8317) < 1e-4; report("airy_z", zj, ".4f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Đĩa {{hk_num}} và {{hk_cf}}; mũ {{hk_e_num}} và {{hk_e_cf}}; Gauss {{hk_g}}; đối ngược {{hk_rec_f}} lệch {{hk_rec_dev}}; Rayleigh {{hd_ray_l}}, {{hd_ray_r}}; Hankel {{nh_direct}}, {{nh_abel}}; $J_{1/2}$ {{jv_dev}}; $n$ chiều {{nd_val}}, {{nd_dev}}; nghiệm jinc {{airy_z}}.||Disk {{hk_num}} and {{hk_cf}}; exponential {{hk_e_num}} and {{hk_e_cf}}; Gaussian {{hk_g}}; reciprocity {{hk_rec_f}} deviating {{hk_rec_dev}}; Rayleigh {{hd_ray_l}}, {{hd_ray_r}}; Hankel {{nh_direct}}, {{nh_abel}}; $J_{1/2}$ {{jv_dev}}; $n$ dimensions {{nd_val}}, {{nd_dev}}; jinc zero {{airy_z}}.⟧"""),
        ("md", """## 3. ⟦Mellin và z||Mellin and z⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Các cặp Mellin (mũ, sin, phân thức), điều kiện hạt nhân Fourier, và các cặp, định lý của biến đổi z có đúng số?||Do the Mellin pairs (exponential, sine, rational), the Fourier-kernel condition, and the z pairs and theorems hold numerically?⟧"""),
        ("code", r'''G = special.gamma
s_ = 2.5
ml_direct = integrate.quad(lambda x: np.exp(-x)*x**(s_ - 1), 0, np.inf)[0]
ml_lap = integrate.quad(lambda t: np.exp(-np.exp(-t))*np.exp(-s_*t), -30, 40, limit=400)[0]
assert abs(ml_direct - G(s_)) < 1e-9 and abs(ml_lap - G(s_)) < 1e-8
report("ml_gam", G(s_), ".4f"); report("ml_dev", max(abs(ml_lap - ml_direct), 1e-16), ".0e")
def mellin_sin(s):
    a = integrate.quad(lambda x: np.sin(x), 0, 1, weight="alg", wvar=(s - 1, 0))[0]
    b = integrate.quad(lambda x: x**(s - 1), 1, np.inf, weight="sin", wvar=1)[0]
    return a + b
assert abs(mellin_sin(0.5) - G(0.5)*np.sin(np.pi/4)) < 1e-8; report("ml_sin", mellin_sin(0.5), ".4f")
rat = integrate.quad(lambda x: x**(0.3 - 1)/(1 + x), 0, np.inf)[0]; assert abs(rat - np.pi/np.sin(0.3*np.pi)) < 1e-6
report("ml_rat", np.pi/np.sin(0.3*np.pi), ".4f")
h2 = integrate.quad(lambda x: x**(2 - 1), 0, 1)[0]; assert abs(h2 - 0.5) < 1e-12; report("ml_h2", h2, ".1f")
# ⟦mômen||moments⟧
FM = lambda s: integrate.quad(lambda x: x**(s - 1), 0, 1)[0]
assert abs(FM(1) - 1) < 1e-12 and abs(FM(2) - 0.5) < 1e-12 and abs(FM(3) - 1/3) < 1e-12
cx = FM(2)/FM(1); rgy = np.sqrt(FM(3)/FM(1)); var = FM(3)/FM(1) - cx**2
assert abs(var - 1/12) < 1e-12
report("mm_c", cx, ".1f"); report("mm_rg", rgy, ".4f"); report("mm_v", var, ".4f")
sc = integrate.quad(lambda x: np.exp(-2*x)*x**1.5, 0, np.inf)[0]; assert abs(sc - 2**-2.5*G(2.5)) < 1e-9
report("mm_sc", sc, ".4f")
# ⟦hạt nhân Fourier||Fourier kernel⟧
def KM(s):
    a = integrate.quad(lambda x: np.cos(2*np.pi*x), 0, 1, weight="alg", wvar=(s - 1, 0))[0]
    b = integrate.quad(lambda x: x**(s - 1), 1, np.inf, weight="cos", wvar=2*np.pi)[0]
    return 2*(a + b)
Kcf = lambda s: 2*(2*np.pi)**(-s)*G(s)*np.cos(np.pi*s/2)
assert abs(KM(0.3) - Kcf(0.3)) < 1e-8 and abs(Kcf(0.3)*Kcf(0.7) - 1) < 1e-12 and abs(KM(0.3)*KM(0.7) - 1) < 1e-7
report("fk_k", Kcf(0.3), ".4f"); report("fk_num", KM(0.3), ".4f"); report("fk_prod", Kcf(0.3)*Kcf(0.7), ".4f")
# ⟦biến đổi z||the z transform⟧
fz = np.array([3, 1, 4, 1, 5, 9, 2, 6.]); zf = lambda zz: np.sum(fz*zz**(-np.arange(len(fz))))
p_ = 0.7; lap = np.sum(fz*np.exp(-np.arange(8)*p_)); assert abs(lap - zf(np.exp(p_))) < 1e-12
report("z_lap", lap, ".4f"); report("z_lap_dev", max(abs(lap - zf(np.exp(p_))), 1e-16), ".0e")
Nz = len(fz); zk = np.exp(2j*np.pi*np.arange(Nz)/Nz); Fz = np.array([zf(z_) for z_ in zk])
assert np.allclose(Fz, np.fft.fft(fz)); report("z_dft", max(np.max(np.abs(Fz - np.fft.fft(fz))), 1e-16), ".0e")
out = np.convolve([2, 1], [8, 4, 2, 1]); assert list(out) == [16, 16, 8, 4, 1]
qd, rd = np.polydiv(out.astype(float), np.array([2., 1.])); assert np.allclose(qd, [8, 4, 2, 1]) and np.allclose(rd, 0)
report("z_o1", out[0], "d"); report("z_o5", out[-1], "d"); report("z_rem", np.max(np.abs(rd)) + 0.0, ".0f")
n_ = np.arange(300); zz = 2.0
S1 = np.sum(n_*zz**-n_); S2 = np.sum(n_**2*zz**-n_.astype(float)); al = 0.7; Sc = np.sum(np.cos(al*n_)*zz**-n_.astype(float))
zi = 1/zz
assert abs(S1 - zi/(1 - zi)**2) < 1e-10 and abs(S2 - zi*(1 + zi)/(1 - zi)**3) < 1e-10
assert abs(Sc - (1 - zi*np.cos(al))/(1 - 2*zi*np.cos(al) + zi**2)) < 1e-10
report("z_n1", S1, ".0f"); report("z_n2", S2, ".0f"); report("z_cos", Sc, ".4f")
Fpoly = lambda z_: np.sum(fz*z_**(-np.arange(8)))
zt = 1.7; hh = 1e-6
der = (Fpoly(zt + hh) - Fpoly(zt - hh))/(2*hh)
nf = np.sum(np.arange(8)*fz*zt**(-np.arange(8)))
assert abs(nf - (-zt*der)) < 1e-6; report("z_dev", max(abs(nf + zt*der), 1e-16), ".0e")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦$\\Gamma(2.5)$ = {{ml_gam}}; $\\sin$ {{ml_sin}}; $1/(1+x)$ {{ml_rat}}; trọng tâm {{mm_c}}, phương sai {{mm_v}}; hạt nhân Fourier {{fk_k}}, tích {{fk_prod}}; z: {{z_lap}}, {{z_dft}}; đầu ra {{z_o1}}…{{z_o5}}; chuỗi {{z_n1}}, {{z_n2}}, {{z_cos}}.||$\\Gamma(2.5)$ = {{ml_gam}}; $\\sin$ {{ml_sin}}; $1/(1+x)$ {{ml_rat}}; centroid {{mm_c}}, variance {{mm_v}}; Fourier kernel {{fk_k}}, product {{fk_prod}}; z: {{z_lap}}, {{z_dft}}; output {{z_o1}}…{{z_o5}}; series {{z_n1}}, {{z_n2}}, {{z_cos}}.⟧"""),
        ("md", """## 4. ⟦Abel, Radon, chiếu ngược||Abel, Radon, back-projection⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Biến đổi Abel số có khớp bảng của sách, định lý lát chiếu có đúng, và chiếu ngược có sửa đổi có tái tạo được mật độ từ các hình chiếu không?||Does the numerical Abel transform match the book's table, does the projection-slice theorem hold, and does modified back-projection reconstruct the density from projections?⟧"""),
        ("code", r'''fA = lambda fun, x, upper=np.inf: 2*integrate.quad(lambda t: fun(np.sqrt(x*x + t*t)), 0, upper, limit=200)[0]
disk = lambda r: 1.0 if r < 1 else 0.0
adisk = 2*integrate.quad(lambda t: 1.0, 0, np.sqrt(1 - 0.36))[0]; assert abs(adisk - 1.6) < 1e-12
report("ab_disk", adisk, ".1f")
report("ab_gauss", fA(lambda r: np.exp(-np.pi*r*r), 0.5, 10), ".4f")
assert abs(fA(lambda r: np.exp(-np.pi*r*r), 0.5, 10) - np.exp(-np.pi*0.25)) < 1e-10
f1r = lambda r: max(1 - r, 0.0)
def fA1(x):
    if x >= 1: return 0.0
    return 2*integrate.quad(lambda t: 1 - np.sqrt(x*x + t*t), 0, np.sqrt(1 - x*x))[0]
book = [1, .9651, .8881, .7853, .6658, .5368, .4045, .2753, .1564, .0575]
vals = [fA1(x/10) for x in range(10)]
assert max(abs(v_ - b_) for v_, b_ in zip(vals, book)) < 1.5e-3
report("ab_x1", vals[1], ".4f"); report("ab_x5", vals[5], ".4f"); report("ab_x9", vals[9], ".4f"); report("ab_0", vals[0], ".0f")
area = integrate.quad(fA1, -1, 1, points=[0])[0]; assert abs(area - np.pi/3) < 1e-8; report("ab_area", area, ".4f")
# ⟦bảng hệ số||table of coefficients⟧
cn = lambda n: 2*(np.sqrt(n + 1) - np.sqrt(n))
assert abs(cn(0) - 2) < 1e-12; report("ab_k1", cn(1), ".3f"); report("ab_k2", cn(2), ".3f"); report("ab_k3", cn(3), ".3f")
alg = sum(cn(n)*np.sqrt(10 - (5 + n + 0.5)) for n in range(5)); exact = np.pi/2*(10 - 5)
assert abs(alg - 7.78) < 0.02 and abs(exact - 7.854) < 1e-3
ex_num = integrate.quad(lambda r: np.sqrt(10 - r)/np.sqrt(r - 5), 5, 10)[0]; assert abs(ex_num - exact) < 1e-6
report("ab_alg", alg, ".2f"); report("ab_exact", exact, ".3f")
# ⟦vòng Abel-Fourier-Hankel||Abel-Fourier-Hankel ring⟧
xg = np.arange(0, 6.0001, 0.02)
A_num = np.array([fA(lambda r: np.exp(-np.pi*r*r), x_, 8) for x_ in xg])
sgg = np.arange(0, 6.0001, 0.02)
Fs_ = np.array([2*trap(A_num*np.cos(2*np.pi*s_*xg), xg) for s_ in sgg])
r0 = 0.6; back = 2*np.pi*integrate.simpson(Fs_*special.j0(2*np.pi*sgg*r0)*sgg, x=sgg)
assert abs(back - np.exp(-np.pi*r0**2)) < 1e-6
report("arh_val", np.exp(-np.pi*r0**2), ".4f"); report("arh_dev", max(abs(back - np.exp(-np.pi*r0**2)), 1e-16), ".0e")
# ⟦Radon và định lý lát chiếu||Radon and the projection-slice theorem⟧
aa, bb = 2.0, 0.5; ell = lambda x, y: np.exp(-np.pi*(x**2/aa**2 + y**2/bb**2))
th = 0.6; kap = aa**2*np.cos(th)**2 + bb**2*np.sin(th)**2
proj_cf = lambda R: aa*bb/np.sqrt(kap)*np.exp(-np.pi*R**2/kap)
proj_num = lambda R: integrate.quad(lambda t: ell(R*np.cos(th) - t*np.sin(th), R*np.sin(th) + t*np.cos(th)), -30, 30, limit=200)[0]
assert abs(proj_num(0.3) - proj_cf(0.3)) < 1e-9; report("rd_num", proj_num(0.3), ".4f"); report("rd_cf", proj_cf(0.3), ".4f")
Rg = np.linspace(-12, 12, 4801); gR = np.array([proj_cf(R) for R in Rg]); q0 = 0.4
one_d = trap(gR*np.exp(-2j*np.pi*q0*Rg), Rg); slice_ = aa*bb*np.exp(-np.pi*q0**2*kap)
assert abs(one_d - slice_) < 1e-9; report("ps_dev", max(abs(one_d - slice_), 1e-16), ".0e")
# ⟦nhân sửa đổi||the modified kernel⟧
M = 6.0; Rk = np.arange(-600, 600, 0.02)
kern = 2*M*np.sinc(2*M*Rk) - M*np.sinc(M*Rk)**2
for q, want in ((2.0, 2.0/M), (8.0, 0.0)):
    got = trap(kern*np.cos(2*np.pi*q*Rk), Rk); assert abs(got - want) < 2e-3
report("kf_2", trap(kern*np.cos(2*np.pi*2.0*Rk), Rk), ".3f"); report("kf_8", round(trap(kern*np.cos(2*np.pi*8.0*Rk), Rk), 3) + 0.0, ".0f")
# ⟦chiếu ngược có sửa đổi||modified back-projection⟧
dR = 1/(4*M); Rgrid = np.arange(-8, 8, dR); nR = len(Rgrid)
def proj_two(theta, R):
    out_ = 0
    for A_, w_, cx_, cy_ in ((1.0, 0.5, 0.0, 0.0), (0.6, 0.3, 0.7, -0.5)):
        cn_ = cx_*np.cos(theta) + cy_*np.sin(theta)
        out_ = out_ + A_*w_*np.exp(-np.pi*(R - cn_)**2/w_**2)
    return out_
qf = np.fft.fftfreq(nR, dR); ramp = np.where(np.abs(qf) < M, np.abs(qf)/M, 0)
f_true = lambda x, y: np.exp(-np.pi*(x**2 + y**2)/0.25) + 0.6*np.exp(-np.pi*((x - 0.7)**2 + (y + 0.5)**2)/0.09)
pts = [(0, 0), (0.7, -0.5), (0.3, 0.2), (-0.5, 0.4)]
def recon(nth):
    thetas = np.linspace(0, np.pi, nth, endpoint=False)
    mods = [np.real(np.fft.ifft(np.fft.fft(proj_two(t_, Rgrid))*ramp)) for t_ in thetas]
    return [M*sum(np.interp(x_*np.cos(t_) + y_*np.sin(t_), Rgrid, g0) for t_, g0 in zip(thetas, mods))*np.pi/nth for (x_, y_) in pts]
r180 = recon(180); r90 = recon(90)
errs = [abs(r - f_true(x_, y_)) for r, (x_, y_) in zip(r180, pts)]
assert max(errs) < 0.02 and abs(r180[0] - 1) < 0.01 and max(abs(np.array(r180) - np.array(r90))) < 1e-3
report("fb_c", r180[0], ".4f"); report("fb_dev", max(errs), ".3f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Abel: đĩa {{ab_disk}}, Gauss {{ab_gauss}}; $f=1-r$: {{ab_x1}}, {{ab_x5}}, {{ab_x9}}, diện tích {{ab_area}}; hệ số {{ab_k1}}, {{ab_k2}}, {{ab_k3}}; thuật toán {{ab_alg}} so với {{ab_exact}}; vòng {{arh_val}} lệch {{arh_dev}}; Radon {{rd_num}}, {{rd_cf}}, lát cắt {{ps_dev}}; nhân {{kf_2}}, {{kf_8}}; tái tạo {{fb_c}}, sai {{fb_dev}}.||Abel: disk {{ab_disk}}, Gaussian {{ab_gauss}}; $f=1-r$: {{ab_x1}}, {{ab_x5}}, {{ab_x9}}, area {{ab_area}}; coefficients {{ab_k1}}, {{ab_k2}}, {{ab_k3}}; algorithm {{ab_alg}} against {{ab_exact}}; ring {{arh_val}} deviating {{arh_dev}}; Radon {{rd_num}}, {{rd_cf}}, slice {{ps_dev}}; kernel {{kf_2}}, {{kf_8}}; reconstruction {{fb_c}}, error {{fb_dev}}.⟧"""),
        ("md", """## 5. ⟦Hilbert và Fourier phân số||Hilbert and fractional Fourier⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Hilbert dời pha $\\pm\\pi/2$ có đúng, tín hiệu giải tích có khớp thư viện, đường bao và tần số tức thời có đúng, cặp nhân quả có đúng, và biến đổi Fourier phân số có cộng tính và hàm riêng Hermite-Gauss không?||Does Hilbert shift phase by $\\pm\\pi/2$, does the analytic signal match the library, are the envelope and instantaneous frequency right, does the causal pair hold, and is the fractional Fourier transform additive with Hermite-Gauss eigenfunctions?⟧"""),
        ("code", r'''# ⟦Hilbert bằng FFT (bộ lọc i sgn s)||Hilbert by FFT (the i sgn s filter)⟧
def hilb(x):
    Xf = np.fft.fft(x); sgf = np.sign(np.fft.fftfreq(len(x))); return np.real(np.fft.ifft(Xf*1j*sgf))
Np = 1024; tp = np.arange(Np)/Np
c5 = np.cos(2*np.pi*5*tp); s5 = np.sin(2*np.pi*5*tp)
assert np.max(np.abs(hilb(c5) + s5)) < 1e-12 and np.max(np.abs(hilb(s5) - c5)) < 1e-12
report("hb_cos", max(np.max(np.abs(hilb(c5) + s5)), 1e-16), ".0e")
xr = rg.standard_normal(Np); Xr = np.fft.fft(xr); Xr[0] = 0; Xr[Np//2] = 0; xr = np.real(np.fft.ifft(Xr))
assert np.max(np.abs(hilb(hilb(xr)) + xr)) < 1e-12; report("hb_two", max(np.max(np.abs(hilb(hilb(xr)) + xr)), 1e-16), ".0e")
# ⟦Hilbert của Π(x)||Hilbert of Π(x)⟧
def hilb_rect(x0):
    if abs(abs(x0) - 0.5) < 1e-12: return np.nan
    if abs(x0) > 0.5: return (1/np.pi)*integrate.quad(lambda xp: 1/(xp - x0), -0.5, 0.5)[0]
    return (1/np.pi)*integrate.quad(lambda xp: 1.0, -0.5, 0.5, weight="cauchy", wvar=x0)[0]
cf = lambda x0: (1/np.pi)*np.log(abs((x0 - 0.5)/(x0 + 0.5)))
assert abs(hilb_rect(1.0) - cf(1.0)) < 1e-10 and abs(hilb_rect(0.2) - cf(0.2)) < 1e-10
report("hr_1", cf(1.0), ".4f"); report("hr_02", cf(0.2), ".4f")
# ⟦tín hiệu giải tích||analytic signal⟧
b_ = signal.firwin(101, [0.10, 0.20], pass_zero=False); nb = signal.lfilter(b_, 1, rg.standard_normal(4096))[200:200 + 2048]
an_scipy = signal.hilbert(nb); an_ours = nb - 1j*hilb(nb)
assert np.max(np.abs(an_scipy - an_ours)) < 1e-10
Fan = np.fft.fft(an_ours); neg = np.max(np.abs(Fan[len(nb)//2 + 1:]))/np.max(np.abs(Fan))
assert neg < 1e-10
report("an_dev", max(np.max(np.abs(an_scipy - an_ours)), 1e-16), ".0e"); report("an_neg", max(neg, 1e-16), ".0e")
# ⟦đường bao, tần số tức thời||envelope, instantaneous frequency⟧
Ns = 4096; ts = np.arange(Ns)*2*np.pi/Ns*4   # ⟦4 chu kỳ của Ω = 3? dùng tần số nguyên||using integer frequencies⟧
tt = np.arange(Ns)/Ns*2*np.pi
am = (1 + 0.5*np.cos(3*tt))*np.cos(50*tt); env = np.abs(signal.hilbert(am))
assert np.max(np.abs(env - (1 + 0.5*np.cos(3*tt)))) < 1e-9
report("env_dev", max(np.max(np.abs(env - (1 + 0.5*np.cos(3*tt)))), 1e-16), ".0e")
fm = np.cos(50*tt + 2*np.sin(3*tt)); ph = np.unwrap(np.angle(signal.hilbert(fm)))
inst = np.gradient(ph, tt); dev = np.max(inst[50:-50]) - 50
assert abs(dev - 6) < 0.05; report("fm_dev", dev, ".3f")
# ⟦Kramers-Kronig||Kramers-Kronig⟧
Gk = lambda u: 1/(1 + 4*np.pi**2*u**2); f0 = 0.3
pv1 = integrate.quad(lambda u: Gk(u), f0 - 1, f0 + 1, weight="cauchy", wvar=f0)[0]
rest = integrate.quad(lambda u: Gk(u)/(u - f0), f0 + 1, np.inf)[0] + integrate.quad(lambda u: Gk(u)/(u - f0), -np.inf, f0 - 1)[0]
Bnum = (pv1 + rest)/np.pi; Bcf = -2*np.pi*f0/(1 + 4*np.pi**2*f0**2)
assert abs(Bnum - Bcf) < 1e-9
report("kk_b", Bcf, ".4f"); report("kk_num", Bnum, ".4f"); report("kk_dev", max(abs(Bnum - Bcf), 1e-16), ".0e")
# ⟦Hilbert rời rạc: 11 hệ số||discrete Hilbert: 11 coefficients⟧
nn = np.arange(-5, 6); hx = np.where(nn == 0, 0, -1/(np.pi*np.where(nn == 0, 1, nn)))
assert np.allclose(np.abs(hx[[0, 1, 2, 3, 4]]), [.064, .080, .106, .159, .318], atol=6e-4)
report("dh_a", abs(hx[0]), ".3f"); report("dh_b", abs(hx[4]), ".3f")
sv = np.linspace(0.01, 0.49, 49); Hs_ = np.array([np.sum(hx*np.exp(-2j*np.pi*s_*nn)) for s_ in sv])
assert np.all(np.abs(np.angle(Hs_) - np.pi/2) < 1e-9)
amp = np.abs(Hs_); ip = int(np.argmax(amp))
report("dh_s", sv[ip], ".2f"); report("dh_peak", amp[ip], ".3f"); report("dh_a10", amp[9], ".3f"); report("dh_a25", amp[24], ".3f"); report("dh_a40", amp[39], ".3f")
# ⟦Hilbert bằng DHT||Hilbert by the DHT⟧
def dht(f):
    f = np.asarray(f, float); N = len(f); t = np.arange(N)
    return np.array([np.sum(f*(np.cos(2*np.pi*v*t/N) + np.sin(2*np.pi*v*t/N))) for v in range(N)])/N
def idht(H):
    N = len(H); v = np.arange(N); return np.array([np.sum(H*(np.cos(2*np.pi*v*t/N) + np.sin(2*np.pi*v*t/N))) for t in range(N)])
f8 = rg.standard_normal(8); F8 = np.fft.fft(f8); F8[0] = 0; F8[4] = 0; f8 = np.real(np.fft.ifft(F8))
H8 = dht(f8); Hsw = np.array([H8[0], -H8[7], -H8[6], -H8[5], H8[4], H8[3], H8[2], H8[1]])
hd = idht(Hsw); ref = hilb(f8)
assert np.max(np.abs(hd - ref)) < 1e-12 and np.max(np.abs(hd + ref)) > 0.1
report("hh_dev", max(np.max(np.abs(hd - ref)), 1e-16), ".0e"); report("hh_wrong", np.max(np.abs(hd + ref)), ".2f")
# ⟦Fourier phân số||fractional Fourier⟧
tg = np.arange(-7, 7.0001, 0.02); dtg = 0.02
def frft_mat(alpha):
    cot = 1/np.tan(alpha); sn = np.sin(alpha)
    return np.sqrt(1 - 1j*cot)*np.exp(1j*np.pi*cot*(tg[:, None]**2 + tg[None, :]**2))*np.exp(-2j*np.pi*tg[:, None]*tg[None, :]/sn)*dtg
herm = lambda n: special.eval_hermite(n, np.sqrt(2*np.pi)*tg)*np.exp(-np.pi*tg**2)
al7 = 0.7; K7 = frft_mat(al7)
eig = max(np.max(np.abs(K7 @ herm(n) - np.exp(-1j*n*al7)*herm(n))) for n in range(4))
assert eig < 1e-10; report("fr_eig", max(eig, 1e-16), ".0e")
gtest = np.exp(-np.pi*(tg - 0.6)**2)*(1 + 0.3*tg)
addd = np.max(np.abs(frft_mat(0.4) @ (frft_mat(0.5) @ gtest) - frft_mat(0.9) @ gtest)); assert addd < 1e-9
report("fr_add", max(addd, 1e-16), ".0e")
Kf = frft_mat(np.pi/2 - 1e-12); gsh = np.exp(-np.pi*(tg - 0.6)**2)
ft_true = np.exp(-np.pi*tg**2)*np.exp(-1j*np.pi*0.6*2*tg)*0 + np.sum(gsh[None, :]*np.exp(-2j*np.pi*tg[:, None]*tg[None, :]), axis=1)*dtg
assert np.max(np.abs(Kf @ gsh - ft_true)) < 1e-9; report("fr_ft", max(np.max(np.abs(Kf @ gsh - ft_true)), 1e-16), ".0e")
K5 = frft_mat(0.5*np.pi/2); out5 = K5 @ herm(1); ph5 = np.angle(np.sum(out5*herm(1))/np.sum(herm(1)**2))
assert abs(ph5 + np.pi/4) < 1e-6; report("fr_ph", ph5, ".4f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Hilbert: {{hb_cos}}, {{hb_two}}; $\\Pi$: {{hr_1}}, {{hr_02}}; giải tích {{an_dev}}, {{an_neg}}; đường bao {{env_dev}}; FM {{fm_dev}}; Kramers-Kronig {{kk_b}}, {{kk_num}}; 11 hệ số: {{dh_b}}, cực đại {{dh_peak}} tại {{dh_s}}; DHT {{hh_dev}}; phân số: {{fr_eig}}, {{fr_add}}, {{fr_ft}}, pha {{fr_ph}}.||Hilbert: {{hb_cos}}, {{hb_two}}; $\\Pi$: {{hr_1}}, {{hr_02}}; analytic {{an_dev}}, {{an_neg}}; envelope {{env_dev}}; FM {{fm_dev}}; Kramers-Kronig {{kk_b}}, {{kk_num}}; 11 coefficients: {{dh_b}}, maximum {{dh_peak}} at {{dh_s}}; DHT {{hh_dev}}; fractional: {{fr_eig}}, {{fr_add}}, {{fr_ft}}, phase {{fr_ph}}.⟧"""),
    ],
)
