from lib import F, C, UL, OL, TBL

MOD = dict(
    n=10, slug="probability-cf", part="B", book="BK",
    title="⟦Xác suất, biến ngẫu nhiên và hàm đặc trưng||Probability, random variables and the characteristic function⟧",
    blurb="⟦Từ tập hợp và xác suất, biến ngẫu nhiên và mômen (Barkat) tới phân bố của tổng là tích chập, hàm đặc trưng là biến đổi Fourier của mật độ, phân bố mũ, Poisson và giới hạn trung tâm (Bracewell).||"
          "From sets and probability, random variables and moments (Barkat) to the distribution of a sum as a convolution, the characteristic function as the Fourier transform of a density, the exponential and Poisson distributions and the central limit (Bracewell).⟧",
    src="⟦Bracewell, chương 16, tr. 427–445; Barkat, chương 1, tr. 1–73||Bracewell, chapter 16, pp. 427–445; Barkat, chapter 1, pp. 1–73⟧",
    data="⟦Sinh bằng mã: xúc xắc, bình chọn bình đựng bóng, điện trở, chai tiền, phân bố mũ, Poisson, bảng xác suất đồng thời||Generated in code: dice, urns, resistors, a barrel of banknotes, exponential and Poisson variables, joint probability tables⟧",
    objectives=[
        "⟦Dùng tập hợp, phép đếm, xác suất có điều kiện và quy tắc Bayes để tính xác suất của biến cố.||Use sets, counting, conditional probability and Bayes' rule to compute the probability of events.⟧",
        "⟦Mô tả biến ngẫu nhiên rời rạc, liên tục, hỗn hợp bằng CDF và PDF (có xung), rồi tính kỳ vọng, phương sai, mômen.||Describe discrete, continuous and mixed random variables by CDF and PDF (with impulses) and compute expectation, variance and moments.⟧",
        "⟦Thấy rằng mật độ của tổng hai biến độc lập là tích chập, và suy ra trung bình, phương sai cộng; xử lý cả tích, thương, max, min và hàm một biến.||See that the density of the sum of two independent variables is a convolution, deduce that means and variances add, and handle products, quotients, max, min and functions of one variable.⟧",
        "⟦Dùng hàm đặc trưng (biến đổi Fourier của mật độ) để lấy mômen, cộng các biến độc lập, và giải thích giới hạn trung tâm; dùng Tchebycheff, Chernoff, luật số lớn.||Use the characteristic function (the Fourier transform of the density) to obtain moments, add independent variables and explain the central limit; use Chebyshev, Chernoff and the law of large numbers.⟧",
        "⟦Nhận ra phân bố mũ cắt cụt, gamma (Pearson III) và Poisson từ tích chập, và làm việc với biến ngẫu nhiên hai chiều, tương quan, độc lập với không tương quan.||Recognise the truncated exponential, gamma (Pearson III) and Poisson distributions from convolutions, and work with two-dimensional random variables, correlation, and independence versus uncorrelatedness.⟧",
    ],
    parts=[
        # ------------------------------------------------ PART 1
        dict(
            title="⟦Tập hợp và xác suất||Sets and probability⟧",
            scr=("⟦Muốn nói về ngẫu nhiên phải có một ngôn ngữ chính xác cho biến cố và cách đếm chúng.||To speak of randomness we need an exact language for events and a way to count them.⟧",
                 "⟦Tập hợp cho ngôn ngữ; đếm cho xác suất cổ điển; xác suất có điều kiện và Bayes cho cách cập nhật khi biết thêm thông tin.||Sets provide the language; counting gives classical probability; conditional probability and Bayes' rule show how to update when more information arrives.⟧",
                 "⟦Xác suất là hàm không âm, chuẩn hóa, cộng được trên biến cố loại trừ; mọi công thức sau đó suy ra từ ba tiên đề này.||Probability is a nonnegative, normalised function additive over mutually exclusive events; all later formulas follow from these three axioms.⟧"),
            preview=["⟦Tập hợp, biểu đồ Venn và các luật||Sets, Venn diagrams and laws⟧", "⟦Tiên đề xác suất và phép đếm||Axioms of probability and counting⟧", "⟦Xác suất có điều kiện, độc lập và quy tắc Bayes||Conditional probability, independence and Bayes' rule⟧"],
            slides=[
                ("⟦Vì sao học xác suất trước khi phát hiện tín hiệu||Why probability comes before signal detection⟧",
                 "<p>⟦Sách Barkat được thiết kế cho việc học phát hiện tín hiệu thống kê và ước lượng tham số; những khái niệm ấy đòi hỏi hiểu biết vững về xác suất, biến ngẫu nhiên và quá trình ngẫu nhiên. Chương 1 bắt đầu từ lý thuyết tập hợp vì đó là khái niệm nền của xác suất (Barkat, mục 1.1, tr. 1). Bracewell tới cùng chủ đề từ phía khác: vô số ứng dụng của biến đổi Fourier trong thống kê đều xuất phát từ một quan hệ tích chập (chương 16, tr. 427).||"
                 "Barkat's book is designed for the study of statistical signal detection and parameter estimation; these concepts require a good knowledge of probability, random variables and stochastic processes. Chapter 1 starts from set theory since it provides the most fundamental concepts of probability (Barkat, section 1.1, p. 1). Bracewell arrives at the same subject from the other side: countless applications of Fourier transforms in statistics trace to one convolution relation (chapter 16, p. 427).⟧</p>"),
                ("⟦Tập hợp: các định nghĩa||Sets: the basic definitions⟧",
                 "<p>⟦Tập hợp là bộ sưu tập các đối tượng, gọi là phần tử; ký hiệu $a\\in A$. Có thể mô tả bằng liệt kê, bằng lời, hoặc bằng dạng $A=\\{a\\mid a\\text{ nguyên},1\\le a\\le6\\}$. Tập đếm được nếu các phần tử có thể tương ứng 1-1 với $1,2,3,\\ldots$. Tập vũ trụ $U$ gồm mọi phần tử đang xét, tập rỗng $\\emptyset$ không chứa gì. $B\\subseteq A$ nếu mọi phần tử của $B$ thuộc $A$; hai tập không có phần tử chung là rời nhau hay loại trừ nhau (Barkat, mục 1.2.1, tr. 1 đến 3). Nếu $U$ có $n$ phần tử thì có $2^n$ tập con: với con xúc xắc, $2^6=$ {{sub_n}}.||"
                 "A set is a collection of objects called elements; we write $a\\in A$. It can be described by listing, in words, or as $A=\\{a\\mid a\\text{ integer},1\\le a\\le6\\}$. A set is countable if its elements can be put in one-to-one correspondence with $1,2,3,\\ldots$. The universal set $U$ contains all elements under consideration, the empty set $\\emptyset$ none. $B\\subseteq A$ if every element of $B$ is in $A$; two sets with no common element are disjoint or mutually exclusive (Barkat, section 1.2.1, pp. 1 to 3). If $U$ has $n$ elements there are $2^n$ subsets: for a die, $2^6=$ {{sub_n}}.⟧</p>"),
                ("⟦Phép toán và các luật||Operations and laws⟧",
                 TBL(["⟦Phép toán||Operation⟧", "⟦Ký hiệu||Notation⟧", "⟦Ý nghĩa||Meaning⟧"],
                     [["⟦Hợp||Union⟧", "$A\\cup B$", "⟦thuộc $A$ hoặc $B$ hoặc cả hai||in $A$ or $B$ or both⟧"], ["⟦Giao||Intersection⟧", "$A\\cap B$", "⟦thuộc cả $A$ và $B$||in both $A$ and $B$⟧"], ["⟦Hiệu||Difference⟧", "$A-B$", "⟦thuộc $A$ không thuộc $B$||in $A$ not in $B$⟧"],
                      ["⟦Phần bù||Complement⟧", "$\\bar A$", "⟦thuộc $U$ không thuộc $A$||in $U$ not in $A$⟧"], ["⟦Tích Descartes||Cartesian product⟧", "$A\\times B$", "⟦các cặp có thứ tự $(a,b)$||ordered pairs $(a,b)$⟧"]])
                 + "<p>⟦Luật: giao hoán, kết hợp, phân phối; $A\\cup\\bar A=U$, $A\\cap\\bar A=\\emptyset$; và De Morgan $\\overline{A\\cup B}=\\bar A\\cap\\bar B$ (Barkat, tr. 3 đến 6).||Laws: commutative, associative, distributive; $A\\cup\\bar A=U$, $A\\cap\\bar A=\\emptyset$; and De Morgan $\\overline{A\\cup B}=\\bar A\\cap\\bar B$ (Barkat, pp. 3 to 6).⟧</p>"),
                ("⟦Không gian mẫu và biến cố||Sample space and events⟧",
                 "<p>⟦Lý thuyết xác suất ra đời làm mô hình cho trò chơi may rủi như gieo xúc xắc, quay roulette, chia bài; sau đó mô hình cho thí nghiệm vật lý. Tập mọi kết cục phân biệt có thể có gọi là không gian mẫu $S$; biến cố là một kết cục hoặc tổ hợp kết cục, tức một tập con của $S$ (Barkat, mục 1.2.3, tr. 6). Với hai xúc xắc, $|S|=36$; $A=\\{$tổng bằng 7$\\}$ có 6 phần tử, $B=\\{$một chẵn một lẻ$\\}$ có 18: $P(A)$ = {{d_pa}}, $P(B)$ = {{d_pb}}, $P(A\\cap B)$ = {{d_pab}} (vì $A\\subset B$), $P(\\bar A)$ = {{d_pna}} (tr. 7 đến 8).||"
                 "Probability theory was developed to model games of chance such as rolling a die, spinning a roulette wheel or dealing cards; later it modelled physical experiments. The set of all distinct possible outcomes is the sample space $S$; an event is an outcome or combination of outcomes, i.e. a subset of $S$ (Barkat, section 1.2.3, p. 6). With two dice $|S|=36$; $A=\\{$sum is 7$\\}$ has 6 elements, $B=\\{$one even one odd$\\}$ has 18: $P(A)$ = {{d_pa}}, $P(B)$ = {{d_pb}}, $P(A\\cap B)$ = {{d_pab}} (since $A\\subset B$), $P(\\bar A)$ = {{d_pna}} (pp. 7 to 8).⟧</p>"),
                ("⟦Ba định nghĩa xác suất||Three definitions of probability⟧",
                 UL(["⟦Cổ điển: $N$ kết cục loại trừ, đồng khả năng; $P(A)=N_A/N$.||Classical: $N$ mutually exclusive equally likely outcomes; $P(A)=N_A/N$.⟧",
                     "⟦Tần suất tương đối: $P(A)=\\lim_{n\\to\\infty}n_A/n$; không cần đồng khả năng, nhưng thực tế $n$ hữu hạn.||Relative frequency: $P(A)=\\lim_{n\\to\\infty}n_A/n$; no need for equal likelihood, but in practice $n$ is finite.⟧",
                     "⟦Chủ quan: mức độ tin vào một kết cục (De Finetti).||Subjective: the degree of confidence in an outcome (De Finetti).⟧"])
                 + "<p>⟦Barkat nêu ba định nghĩa (tr. 6 đến 7). Số đo: gieo hai xúc xắc 200 000 lần, tần suất tổng bằng 7 là {{d_freq}}, gần $1/6$ = {{d_pa}}.||Barkat states three definitions (pp. 6 to 7). Measured: throwing two dice 200,000 times, the frequency of a sum of 7 is {{d_freq}}, near $1/6$ = {{d_pa}}.⟧</p>"),
                ("⟦Định nghĩa hình thức và các tính chất||The formal definition and properties⟧",
                 "<p>⟦Hàm xác suất $P(\\cdot)$ gán cho biến cố $A$ một số thực sao cho: (1) $P(A)\\ge0$; (2) $P(S)=1$; (3) với các biến cố loại trừ nhau đếm được, $P(A_1\\cup\\cdots\\cup A_n)=\\sum P(A_i)$ (tr. 7). Từ đó: $0\\le P(A)\\le1$, $P(\\emptyset)=0$, $P(\\bar A)=1-P(A)$ và $P(A\\cup B)=P(A)+P(B)-P(A\\cap B)$ (tr. 12 đến 13). Kiểm tra bằng đếm: với hai xúc xắc, $P(A\\cup B)$ = {{d_pun}} $=\\tfrac12+\\tfrac16-\\tfrac16$.||"
                 "A probability function $P(\\cdot)$ assigns to an event $A$ a real number such that: (1) $P(A)\\ge0$; (2) $P(S)=1$; (3) for countable mutually exclusive events, $P(A_1\\cup\\cdots\\cup A_n)=\\sum P(A_i)$ (p. 7). From these: $0\\le P(A)\\le1$, $P(\\emptyset)=0$, $P(\\bar A)=1-P(A)$ and $P(A\\cup B)=P(A)+P(B)-P(A\\cap B)$ (pp. 12 to 13). Check by counting: with two dice $P(A\\cup B)$ = {{d_pun}} $=\\tfrac12+\\tfrac16-\\tfrac16$.⟧</p>"),
                ("⟦Phép đếm: quy tắc nhân, hoán vị, tổ hợp||Counting: the product rule, permutations, combinations⟧",
                 "<p>⟦Nếu việc gồm các bước với $n_1,n_2,\\ldots,n_k$ cách, tổng số cách là $n_1n_2\\cdots n_k$: từ có 5 chữ cái có thể lặp là $26^5$ = {{cnt_rep}}; không lặp là $26\\cdot25\\cdot24\\cdot23\\cdot22$ = {{cnt_perm}} (Barkat, mục 1.2.4, tr. 8). Hoán vị $r$ vật trong $n$ chỗ: ${}_nP_r=n!/(n-r)!$; tổ hợp (không quan tâm thứ tự): $\\binom nr=n!/[(n-r)!r!]$; hoán vị có vật giống nhau dùng hệ số đa thức $n!/(n_1!\\cdots n_k!)$ (tr. 8 đến 9). Số đo: $\\binom{14}{6}$ = {{cnt_c146}}.||"
                 "If a task consists of steps with $n_1,n_2,\\ldots,n_k$ ways, the total is $n_1n_2\\cdots n_k$: a 5-letter word with repeats is $26^5$ = {{cnt_rep}}; without repeats $26\\cdot25\\cdot24\\cdot23\\cdot22$ = {{cnt_perm}} (Barkat, section 1.2.4, p. 8). Permutations of $r$ objects in $n$ slots: ${}_nP_r=n!/(n-r)!$; combinations (order irrelevant): $\\binom nr=n!/[(n-r)!r!]$; permutations with repeated objects use the multinomial coefficient $n!/(n_1!\\cdots n_k!)$ (pp. 8 to 9). Measured: $\\binom{14}{6}$ = {{cnt_c146}}.⟧</p>"
                 + F("⟦Tổ hợp||Combinations⟧", r"\binom nr=\frac{n!}{(n-r)!\,r!}=\binom n{n-r},\qquad \binom nr=\binom{n-1}{r-1}+\binom{n-1}{r}")),
                ("⟦Ví dụ: cây xác suất và lấy mẫu không hoàn lại||Examples: a tree diagram and sampling without replacement⟧",
                 "<p>⟦Bình A có 5 bóng đỏ 2 trắng, bình B có 3 đỏ 2 trắng; chọn ngẫu nhiên một bình rồi rút hai bóng liên tiếp không hoàn lại. $P(2\\text{ trắng})=\\tfrac12\\cdot\\tfrac27\\cdot\\tfrac16+\\tfrac12\\cdot\\tfrac25\\cdot\\tfrac14$ = {{urn_tree}} (Barkat, ví dụ 1.3, tr. 9 đến 10), bằng cả phân số chính xác lẫn mô phỏng. Ví dụ 1.4: bình 5 đỏ, 3 lục, 4 xanh, 2 trắng, rút 6 bóng: xác suất có 2 đỏ, 1 lục, 2 xanh, 1 trắng là $\\binom52\\binom31\\binom42\\binom21/\\binom{14}6$ = {{urn_multi}} theo đếm chính xác và mô phỏng. (Bản in của sách ghi 0.080; đếm trực tiếp cho 360/3003, ta dùng giá trị tính được.)||"
                 "Urn A has 5 red and 2 white balls, urn B has 3 red and 2 white; choose an urn at random then draw two balls in succession without replacement. $P(2\\text{ white})=\\tfrac12\\cdot\\tfrac27\\cdot\\tfrac16+\\tfrac12\\cdot\\tfrac25\\cdot\\tfrac14$ = {{urn_tree}} (Barkat, example 1.3, pp. 9 to 10), by exact fractions and by simulation. Example 1.4: an urn with 5 red, 3 green, 4 blue, 2 white balls, draw 6: the probability of 2 red, 1 green, 2 blue, 1 white is $\\binom52\\binom31\\binom42\\binom21/\\binom{14}6$ = {{urn_multi}} by exact counting and simulation. (The book's printed value is 0.080; direct counting gives 360/3003, so we use the computed value.)⟧</p>"),
                ("⟦Xác suất có điều kiện và độc lập||Conditional probability and independence⟧",
                 "<p>⟦$P(A\\mid B)=P(A\\cap B)/P(B)$; nếu $B$ không ảnh hưởng $A$ thì độc lập: $P(A\\cap B)=P(A)P(B)$ (Barkat, tr. 13). Với ba biến cố phải thỏa cả tính độc lập từng cặp và $P(A_1\\cap A_2\\cap A_3)=P(A_1)P(A_2)P(A_3)$ (tr. 13). Ví dụ 1.7: hộp 7 trắng, 3 đỏ, 6 lục; rút lần lượt đỏ, trắng, lục: có hoàn lại thì các biến cố độc lập, $\\tfrac3{16}\\cdot\\tfrac7{16}\\cdot\\tfrac68$ = {{rw_repl}}; không hoàn lại thì $\\tfrac3{16}\\cdot\\tfrac7{15}\\cdot\\tfrac6{14}$ = {{rw_norepl}} (tr. 14 đến 15).||"
                 "$P(A\\mid B)=P(A\\cap B)/P(B)$; if $B$ has no effect on $A$ they are independent: $P(A\\cap B)=P(A)P(B)$ (Barkat, p. 13). For three events both pairwise independence and $P(A_1\\cap A_2\\cap A_3)=P(A_1)P(A_2)P(A_3)$ must hold (p. 13). Example 1.7: a box with 7 white, 3 red, 6 green balls; draw red, white, green in order: with replacement the events are independent, $\\tfrac3{16}\\cdot\\tfrac7{16}\\cdot\\tfrac68$ = {{rw_repl}}; without replacement $\\tfrac3{16}\\cdot\\tfrac7{15}\\cdot\\tfrac6{14}$ = {{rw_norepl}} (pp. 14 to 15).⟧</p>"
                 + F("⟦Xác suất có điều kiện||Conditional probability⟧", r"P(A\mid B)=\frac{P(A\cap B)}{P(B)},\qquad P(A_1\cap A_2\cap A_3)=P(A_1)P(A_2\mid A_1)P(A_3\mid A_1\cap A_2)")),
                ("⟦Quy tắc Bayes và xác suất toàn phần||Bayes' rule and total probability⟧",
                 "<p>⟦Nếu $A_1,\\ldots,A_n$ loại trừ nhau và hợp lại là $S$ thì với mọi biến cố $A$: $P(A)=\\sum P(A\\mid A_i)P(A_i)$ (xác suất toàn phần) và $P(A_k\\mid A)=P(A_k)P(A\\mid A_k)/P(A)$ (Bayes) (Barkat, tr. 13 đến 14). Ví dụ 1.6: nguồn phát 0 với xác suất 0.6, 1 với 0.4, kênh làm sai một ký hiệu với xác suất 0.2: $P(\\text{nhận }0)=0.8\\cdot0.6+0.2\\cdot0.4$ = {{ch_r0}}; và $P(\\text{gửi }0\\mid\\text{nhận }0)$ = {{ch_post}} (tr. 14). Ví dụ 1.8 (ba bình, tổng 32 bóng): $P(\\text{trắng})$ = {{urn_pw}} và $P(\\text{bình B}\\mid\\text{trắng})$ = {{urn_pb}} (tr. 15 đến 17).||"
                 "If $A_1,\\ldots,A_n$ are mutually exclusive and their union is $S$ then for every event $A$: $P(A)=\\sum P(A\\mid A_i)P(A_i)$ (total probability) and $P(A_k\\mid A)=P(A_k)P(A\\mid A_k)/P(A)$ (Bayes) (Barkat, pp. 13 to 14). Example 1.6: a source sends 0 with probability 0.6 and 1 with 0.4, the channel garbles a symbol with probability 0.2: $P(\\text{receive }0)=0.8\\cdot0.6+0.2\\cdot0.4$ = {{ch_r0}}; and $P(\\text{sent }0\\mid\\text{received }0)$ = {{ch_post}} (p. 14). Example 1.8 (three urns, 32 balls): $P(\\text{white})$ = {{urn_pw}} and $P(\\text{urn B}\\mid\\text{white})$ = {{urn_pb}} (pp. 15 to 17).⟧</p>"
                 + F("⟦Bayes||Bayes⟧", r"P(A_k\mid A)=\frac{P(A_k)\,P(A\mid A_k)}{\sum_iP(A\mid A_i)P(A_i)}")),
                ("⟦Bác bỏ ngộ nhận: độc lập khác loại trừ nhau||Debunking: independent is not mutually exclusive⟧",
                 "<p>⟦Hai biến cố có xác suất dương và loại trừ nhau thì không độc lập, vì $P(A\\cap B)=0\\ne P(A)P(B)$. Số đo: $A=\\{$tổng 7$\\}$ và $B=\\{$xúc xắc thứ nhất là 1$\\}$ là hai biến cố có giao khác rỗng và $P(A\\cap B)$ = {{ind_ab}} bằng $P(A)P(B)$ = {{ind_ab}}: độc lập dù không loại trừ nhau; còn $C=\\{$tổng 2$\\}$ và $D=\\{$tổng 12$\\}$ loại trừ nhau, $P(C\\cap D)$ = {{ind_cd}} nhưng $P(C)P(D)$ = {{ind_cd_prod}}: không độc lập.||"
                 "Two events with positive probability that are mutually exclusive are not independent, since $P(A\\cap B)=0\\ne P(A)P(B)$. Measured: $A=\\{$sum 7$\\}$ and $B=\\{$first die is 1$\\}$ overlap and $P(A\\cap B)$ = {{ind_ab}} equals $P(A)P(B)$ = {{ind_ab}}: independent though not exclusive; while $C=\\{$sum 2$\\}$ and $D=\\{$sum 12$\\}$ are exclusive, $P(C\\cap D)$ = {{ind_cd}} but $P(C)P(D)$ = {{ind_cd_prod}}: not independent.⟧</p>"),
                ("⟦Tự kiểm tra phần 1||Self-check, part 1⟧",
                 UL(["⟦Vì sao $P(A\\cap B)=P(A)P(B)$ chỉ khi độc lập?||Why does $P(A\\cap B)=P(A)P(B)$ hold only under independence?⟧",
                     "⟦Bao nhiêu tập con của tập có 6 phần tử?||How many subsets does a 6-element set have?⟧",
                     "⟦Vì sao rút không hoàn lại làm mất tính độc lập?||Why does drawing without replacement destroy independence?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: nó là định nghĩa của độc lập; 64; không gian mẫu đổi sau mỗi lần rút.||Hints: it is the definition of independence; 64; the sample space changes after each draw.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 2
        dict(
            title="⟦Biến ngẫu nhiên và mômen||Random variables and moments⟧",
            scr=("⟦Biến ngẫu nhiên là hàm ánh xạ kết cục lên trục thực; ta mô tả nó bằng hàm phân bố và hàm mật độ.||A random variable is a function mapping outcomes to the real axis; we describe it with distribution and density functions.⟧",
                 "⟦Dùng hàm bậc thang và xung ta gộp được biến rời rạc, liên tục, hỗn hợp làm một, rồi tính kỳ vọng, phương sai và mômen.||With step and impulse functions we unify discrete, continuous and mixed variables, then compute expectation, variance and moments.⟧",
                 "⟦Đây là chỗ xung $\\delta$ của Bracewell (chương 5) trở thành mật độ của biến rời rạc.||This is where Bracewell's impulse $\\delta$ (chapter 5) becomes the density of a discrete variable.⟧"),
            preview=["⟦Biến rời rạc, liên tục, hỗn hợp||Discrete, continuous and mixed variables⟧", "⟦Kỳ vọng, phương sai, mômen||Expectation, variance and moments⟧", "⟦Tần số phân bố và ký hiệu $P(x)\\,dx$||Frequency distributions and the notation $P(x)\\,dx$⟧"],
            slides=[
                ("⟦Biến ngẫu nhiên: một hàm||A random variable: a function⟧",
                 "<p>⟦Biến ngẫu nhiên là hàm thực ánh xạ các phần tử của không gian mẫu $S$ lên các điểm trên trục thực. Nó chẳng ngẫu nhiên cũng chẳng phải biến, mà là một hàm, nên tên hơi dễ gây hiểu lầm. Ký hiệu $X,Y,Z$ cho biến, $x,y,z$ cho giá trị cụ thể (Barkat, mục 1.3, tr. 17). Bracewell dùng thuật ngữ tần suất phân bố: xác suất để đại lượng nhận giá trị giữa $x$ và $x+dx$ là $P(x)\\,dx$, không thứ nguyên; nếu $dx$ có thứ nguyên thì $P(x)$ có thứ nguyên nghịch đảo (chương 16, tr. 427).||"
                 "A random variable is a real function mapping the elements of the sample space $S$ to points of the real axis. It is neither random nor a variable but a function, so the name is a little misleading. Capital letters $X,Y,Z$ denote variables and lowercase $x,y,z$ particular values (Barkat, section 1.3, p. 17). Bracewell uses the term frequency distribution: the probability that a quantity takes values between $x$ and $x+dx$ is $P(x)\\,dx$, dimensionless; if $dx$ has dimensions then $P(x)$ has the reciprocal dimensions (chapter 16, p. 427).⟧</p>"),
                ("⟦Hàm bậc thang và xung: công cụ chung||Step and impulse functions: a common tool⟧",
                 "<p>⟦Bậc thang đơn vị $u(x)$ bằng 1 khi $x\\ge0$ và 0 khi $x<0$. Xung đơn vị $\\delta(x)$ là giới hạn của xung chữ nhật diện tích 1 khi độ rộng tiến về 0; tích phân của xung là bậc thang, đạo hàm của bậc thang là xung, và $\\int A\\delta(x-x_0)f(x)dx=Af(x_0)$ (Barkat, mục 1.3.1, tr. 17 đến 18). Đó chính là tính chất sàng lọc trong Bracewell (module 5). Với kỳ vọng ta sẽ dùng $\\delta$ để viết mật độ của biến rời rạc.||"
                 "The unit step $u(x)$ equals 1 for $x\\ge0$ and 0 for $x<0$. The unit impulse $\\delta(x)$ is the limit of a rectangular pulse of unit area as its width goes to 0; the integral of the impulse is the step, the derivative of the step is the impulse, and $\\int A\\delta(x-x_0)f(x)dx=Af(x_0)$ (Barkat, section 1.3.1, pp. 17 to 18). This is the sifting property of Bracewell (module 5). We will use $\\delta$ to write the density of a discrete variable.⟧</p>"),
                ("⟦Biến rời rạc: xác suất và CDF||Discrete variables: probabilities and the CDF⟧",
                 "<p>⟦Biến rời rạc chỉ nhận một tập hữu hạn hoặc đếm được các giá trị $x_i$ với $P(x_i)\\ge0$ và $\\sum P(x_i)=1$. Hàm phân bố tích lũy $F_X(x)=P(X\\le x)$, và mật độ là $f_X(x)=\\sum P(x_i)\\delta(x-x_i)$ (Barkat, mục 1.3.2, tr. 18 đến 19). Ví dụ 1.9: $X$ là tổng hai xúc xắc: $P(4\\le X\\le6)$ = {{dice_46}} và $P(X\\ge5)$ = {{dice_ge5}} (tr. 19 đến 20). Mật độ là $\\frac1{36}[\\delta(x-2)+2\\delta(x-3)+\\cdots+\\delta(x-12)]$: đó là tích chập của hai mật độ đồng đều, điều sẽ trở lại ở phần 3.||"
                 "A discrete variable takes only a finite or countable set of values $x_i$ with $P(x_i)\\ge0$ and $\\sum P(x_i)=1$. The cumulative distribution function is $F_X(x)=P(X\\le x)$, and the density is $f_X(x)=\\sum P(x_i)\\delta(x-x_i)$ (Barkat, section 1.3.2, pp. 18 to 19). Example 1.9: $X$ is the sum of two dice: $P(4\\le X\\le6)$ = {{dice_46}} and $P(X\\ge5)$ = {{dice_ge5}} (pp. 19 to 20). The density is $\\frac1{36}[\\delta(x-2)+2\\delta(x-3)+\\cdots+\\delta(x-12)]$: the convolution of two uniform densities, which returns in part 3.⟧</p>"),
                ("⟦Biến liên tục: mật độ||Continuous variables: the density⟧",
                 "<p>⟦Biến liên tục có $F_X(x)=\\int_{-\\infty}^xf_X(u)du$ với $f_X\\ge0$ và $\\int f_X=1$; ngược lại $f_X=dF_X/dx$ (Barkat, mục 1.3.3, tr. 20 đến 22). Ví dụ 1.10: $f_X=cx$ trên $0<x<3$: $c=2/9$ = {{pdf_c}}; $P(1<X<2)$ = {{pdf_p12}}; và $F_X(x)=x^2/9$ trên $[0,3]$, tại $x=2$ bằng {{pdf_F2}}. Mỗi số tính bằng tích phân số và bằng công thức.||"
                 "A continuous variable has $F_X(x)=\\int_{-\\infty}^xf_X(u)du$ with $f_X\\ge0$ and $\\int f_X=1$; conversely $f_X=dF_X/dx$ (Barkat, section 1.3.3, pp. 20 to 22). Example 1.10: $f_X=cx$ on $0<x<3$: $c=2/9$ = {{pdf_c}}; $P(1<X<2)$ = {{pdf_p12}}; and $F_X(x)=x^2/9$ on $[0,3]$, equal to {{pdf_F2}} at $x=2$. Each number is computed by numerical integration and by formula.⟧</p>"),
                ("⟦Biến hỗn hợp: bộ chỉnh lưu nửa sóng||Mixed variables: the half-wave rectifier⟧",
                 "<p>⟦Biến hỗn hợp có mật độ vừa chứa xung (xác suất tại các điểm rời rạc) vừa có phần liên tục. Ví dụ: đầu vào $X$ có mật độ đối xứng qua bộ chỉnh lưu nửa sóng lý tưởng $Y=X$ khi $X>0$, $Y=0$ khi $X\\le0$: $P(Y=0)=\\tfrac12$ (xung cường độ $\\tfrac12$ tại 0) và phần liên tục với diện tích $\\tfrac12$ bằng mật độ của $X$ khi $y>0$ (Barkat, mục 1.3.4, tr. 22 đến 23). Số đo với $X$ chuẩn: $P(Y=0)$ = {{rect_p0}}, $E[Y]$ = {{rect_e}} và $\\text{var}\\,Y$ = {{rect_var}}, theo tích phân và theo mô phỏng.||"
                 "A mixed variable has a density with both impulses (probabilities at discrete points) and a continuous part. Example: an input $X$ with a symmetric density through an ideal half-wave rectifier $Y=X$ for $X>0$, $Y=0$ for $X\\le0$: $P(Y=0)=\\tfrac12$ (an impulse of strength $\\tfrac12$ at 0) and a continuous part of area $\\tfrac12$ equal to the density of $X$ for $y>0$ (Barkat, section 1.3.4, pp. 22 to 23). Measured with a normal $X$: $P(Y=0)$ = {{rect_p0}}, $E[Y]$ = {{rect_e}} and $\\text{var}\\,Y$ = {{rect_var}}, by integration and by simulation.⟧</p>"),
                ("⟦Kỳ vọng||Expectation⟧",
                 "<p>⟦Kỳ vọng (giá trị trung bình) của biến rời rạc là $E[X]=\\sum xP(x)$; của biến liên tục $E[X]=\\int xf_X(x)dx$. Với hàm $g(X)$: $E[g(X)]=\\int g(x)f_X(x)dx$ (định lý quan trọng dùng suốt sách), và $E[cX]=cE[X]$ (Barkat, mục 1.4.1, tr. 23 đến 25). Ví dụ 1.11: một con xúc xắc: $E[X]$ = {{die_e}}. Ví dụ 1.12: mật độ chẵn (bằng $1/4$ trên $|x|<1$ và $1/8$ trên $1<|x|<3$): $E[X]$ = {{ex12_e}}.||"
                 "The expectation (mean) of a discrete variable is $E[X]=\\sum xP(x)$; of a continuous one $E[X]=\\int xf_X(x)dx$. For a function $g(X)$: $E[g(X)]=\\int g(x)f_X(x)dx$ (an important theorem used throughout the book), and $E[cX]=cE[X]$ (Barkat, section 1.4.1, pp. 23 to 25). Example 1.11: one die: $E[X]$ = {{die_e}}. Example 1.12: an even density ($1/4$ on $|x|<1$ and $1/8$ on $1<|x|<3$): $E[X]$ = {{ex12_e}}.⟧</p>"),
                ("⟦Mômen, bình phương trung bình và phương sai||Moments, mean-square and variance⟧",
                 "<p>⟦$E[X^n]$ là mômen bậc $n$ quanh gốc; $E[X^2]$ là giá trị bình phương trung bình. Phương sai $\\sigma_x^2=E[(X-E[X])^2]=E[X^2]-(E[X])^2$ và $\\sigma_x$ là độ lệch chuẩn (Barkat, tr. 25 đến 26). Ví dụ 1.13: với mật độ của ví dụ 1.12, $E[X^2]=\\sigma_x^2$ = {{ex12_var}} $=7/3$. Đây đúng là các đại lượng mà Bracewell gọi là mômen, tâm khối và phương sai của một hàm (module 8): mật độ xác suất chỉ là một hàm có diện tích 1. Số đo: hai xúc xắc có $E$ = {{dice_e}} và phương sai {{dice_var}} $=35/6$.||"
                 "$E[X^n]$ is the $n$th moment about the origin; $E[X^2]$ is the mean-square value. The variance is $\\sigma_x^2=E[(X-E[X])^2]=E[X^2]-(E[X])^2$ and $\\sigma_x$ is the standard deviation (Barkat, pp. 25 to 26). Example 1.13: for the density of example 1.12, $E[X^2]=\\sigma_x^2$ = {{ex12_var}} $=7/3$. These are exactly what Bracewell calls the moment, centroid and variance of a function (module 8): a probability density is simply a function of area 1. Measured: two dice have $E$ = {{dice_e}} and variance {{dice_var}} $=35/6$.⟧</p>"
                 + F("⟦Phương sai||Variance⟧", r"\sigma_x^2=E\big[(X-m_x)^2\big]=E[X^2]-m_x^2")),
                ("⟦Tự kiểm tra phần 2||Self-check, part 2⟧",
                 UL(["⟦Mật độ của biến rời rạc viết thế nào bằng xung?||How do we write the density of a discrete variable with impulses?⟧",
                     "⟦Biến hỗn hợp khác biến liên tục ở điểm nào trên mật độ?||How does a mixed variable differ from a continuous one in its density?⟧",
                     "⟦$\\text{var}\\,X$ bằng gì theo $E[X^2]$ và $E[X]$?||What is $\\text{var}\\,X$ in terms of $E[X^2]$ and $E[X]$?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: $\\sum P(x_i)\\delta(x-x_i)$; có xung; $E[X^2]-(E[X])^2$.||Hints: $\\sum P(x_i)\\delta(x-x_i)$; it contains impulses; $E[X^2]-(E[X])^2$.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 3
        dict(
            title="⟦Phân bố của tổng, tích, max, min: tích chập||Distribution of a sum, product, max and min: convolution⟧",
            scr=("⟦Chế tạo mạch cần điện trở 150 ôm bằng cách nối tiếp một điện trở 100 ôm và một điện trở 50 ôm, mỗi cái sai số 10 phần trăm.||A circuit needs a 150-ohm resistance made by joining in series a 100-ohm and a 50-ohm resistor, each with a 10 percent tolerance.⟧",
                 "⟦Tổng hợp có dung sai bao nhiêu và phân bố thế nào?||What tolerance and distribution does the composite have?⟧",
                 "⟦Phân bố của tổng hai đại lượng độc lập là tích chập của hai phân bố; đây là quan hệ tích chập cơ bản của Bracewell chương 16.||The distribution of the sum of two independent quantities is the convolution of their distributions; this is Bracewell's basic convolution relation of chapter 16.⟧"),
            preview=["⟦Điện trở nối tiếp và chai tiền||Series resistors and a barrel of money⟧", "⟦Hệ quả: trung bình và phương sai cộng||Consequence: means and variances add⟧", "⟦Tích, thương, max, min và hàm một biến||Products, quotients, max, min and functions of one variable⟧"],
            slides=[
                ("⟦Bài toán điện trở||The resistor problem⟧",
                 "<p>⟦Mua nhiều điện trở 100 ôm với dung sai 10 phần trăm thì giá trị dao động từ 90 đến 110, gần như đều: mật độ $P_1(R)=\\frac1{20}\\Pi\\!\\left(\\frac{R-100}{20}\\right)$. Tương tự điện trở 50 ôm: $P_2(R)=\\frac1{10}\\Pi\\!\\left(\\frac{R-50}{10}\\right)$. Cần biết dung sai của tổ hợp nối tiếp, tức phân bố $P(R)$ giữa 135 và 165 ôm (Bracewell, tr. 429 đến 430).||"
                 "Buying many 100-ohm resistors with a 10 percent tolerance gives values from 90 to 110, roughly uniform: density $P_1(R)=\\frac1{20}\\Pi\\!\\left(\\frac{R-100}{20}\\right)$. Similarly for 50-ohm resistors: $P_2(R)=\\frac1{10}\\Pi\\!\\left(\\frac{R-50}{10}\\right)$. We need the tolerance of the series combination, i.e. the distribution $P(R)$ between 135 and 165 ohms (Bracewell, pp. 429 to 430).⟧</p>"),
                ("⟦Lập luận dẫn tới tích chập||The argument leading to convolution⟧",
                 "<p>⟦Gọi điện trở chọn từ kho 100 ôm là $R'$; muốn tổng bằng $R$ thì điện trở từ kho 50 ôm phải là $R-R'$. Tần suất tổng $R$ là tích tần suất của $R'$ ở thành phần thứ nhất và $R-R'$ ở thành phần thứ hai, lấy tích phân trên mọi khả năng của $R'$: $P(R)=\\int P_1(R')P_2(R-R')dR'$, tức $P=P_1*P_2$ (Bracewell, tr. 430). Ta có thể để cận vô hạn vì $P_1$ bằng 0 ngoài $[90,110]$. Đây là quan hệ tích chập cơ bản giữa phân bố của tổng và phân bố các thành phần.||"
                 "Let the resistor from the 100-ohm stock be $R'$; for the total to be $R$ the resistor from the 50-ohm stock must be $R-R'$. The frequency of a total $R$ is the product of the frequencies of $R'$ in the first component and $R-R'$ in the second, integrated over the possibilities of $R'$: $P(R)=\\int P_1(R')P_2(R-R')dR'$, i.e. $P=P_1*P_2$ (Bracewell, p. 430). We may use infinite limits since $P_1$ is zero outside $[90,110]$. This is the basic convolution relation between the distribution of a sum and the distributions of its components.⟧</p>"
                 + F("⟦Tổng độc lập||Independent sum⟧", r"P(x)=\int_{-\infty}^{\infty}P_1(x')\,P_2(x-x')\,dx'=P_1*P_2")),
                ("⟦Kết quả: hình thang||The result: a trapezoid⟧",
                 "<p>⟦Tích chập cho phân bố hình thang (hình 16.1) từ 135 đến 165 ôm, với đỉnh phẳng có độ cao {{res_flat}} trong khoảng 145 đến 155, giống hệt việc quét một dải rộng 20 đơn vị bằng khe rộng 10 đơn vị (cả ba pha kéo dài 10 đơn vị), hay xung chữ nhật 20 vào bộ lọc có đáp ứng xung chữ nhật 10 (tr. 430). Số đo: tại $R=140$, mật độ {{res_140}}; giá trị trung bình {{res_mean}} ôm. Cả tích chập số trên lưới và công thức từng khúc cho cùng kết quả.||"
                 "The convolution gives a trapezoidal distribution (Fig. 16.1) from 135 to 165 ohms, with a flat top of height {{res_flat}} between 145 and 155, exactly what scanning a uniform stripe 20 units wide with a slit 10 units wide would give (the three phases last 10 units each), or a rectangular pulse of 20 into a filter with a rectangular impulse response of 10 (p. 430). Measured: at $R=140$ the density is {{res_140}}; the mean is {{res_mean}} ohms. A numerical convolution on a grid and the piecewise formula give the same result.⟧</p>{{fig:sum_conv}}"),
                ("⟦Kiểm tra bằng các định lý tích chập||Checks with the convolution theorems⟧",
                 "<p>⟦Trọng tâm cộng nhau: trung bình của tổ hợp bằng tổng các trung bình. Diện tích nhân nhau: hai phân bố diện tích 1 cho diện tích 1. Phương sai cộng nhau: $\\sigma^2=20^2/12+10^2/12$ = {{res_var}}, độ lệch chuẩn {{res_sd}} ôm, tức {{res_pct}} phần trăm của 150 so với {{comp_pct}} phần trăm của mỗi thành phần. Dung sai (theo độ lệch chuẩn) được cải thiện, nhưng khoảng giữa hai cực trị vẫn là 10 phần trăm (tr. 430 đến 431). Nếu có thêm nhiều phần tử nối tiếp hay phân bố tròn hơn, dạng Gauss theo giới hạn trung tâm tiến gần hơn.||"
                 "Centroids add: the mean of the combination equals the sum of the means. Areas multiply: two distributions of area 1 give area 1. Variances add: $\\sigma^2=20^2/12+10^2/12$ = {{res_var}}, standard deviation {{res_sd}} ohms, i.e. {{res_pct}} percent of 150 against {{comp_pct}} percent for each component. The tolerance (by standard deviation) is improved, but the spread between extremes is still 10 percent (pp. 430 to 431). With more elements in series or rounder distributions the Gaussian result of the central-limit theorem would be approached more closely.⟧</p>"),
                ("⟦Ví dụ thứ hai: chai tiền||Second example: a barrel of money⟧",
                 "<p>⟦Một chai đầy tiền, một nửa là tờ 1 đô, còn lại là tờ 5, 10 và vài tờ 20. Xác suất xuất hiện tờ $n$ đô tỉ lệ với dãy $\\{10,6,3,1\\}$ tại $\\{1,5,10,20\\}$ (tổng 20), tức $P_1(x)=\\tfrac{10}{20}\\delta(x-1)+\\tfrac6{20}\\delta(x-5)+\\tfrac3{20}\\delta(x-10)+\\tfrac1{20}\\delta(x-20)$. Rút hai tờ và cộng: phân bố của tổng là tích chuỗi (tích chập rời rạc) của dãy với chính nó, $\\{p\\}=\\{p_1\\}*\\{p_2\\}$ (Bracewell, tr. 431 đến 433). Kết quả: $\\tfrac1{400}[100\\delta(x-2)+120\\delta(x-6)+36\\delta(x-10)+60\\delta(x-11)+36\\delta(x-15)+9\\delta(x-20)+20\\delta(x-21)+12\\delta(x-25)+6\\delta(x-30)+\\delta(x-40)]$.||"
                 "A barrel full of money, half dollar bills, the rest fives, tens and a few twenties. The frequency of $n$-dollar bills is proportional to the sequence $\\{10,6,3,1\\}$ at $\\{1,5,10,20\\}$ (sum 20), i.e. $P_1(x)=\\tfrac{10}{20}\\delta(x-1)+\\tfrac6{20}\\delta(x-5)+\\tfrac3{20}\\delta(x-10)+\\tfrac1{20}\\delta(x-20)$. Draw two bills and add: the distribution of the total is the serial product (discrete convolution) of the sequence with itself, $\\{p\\}=\\{p_1\\}*\\{p_2\\}$ (Bracewell, pp. 431 to 433). Result: $\\tfrac1{400}[100\\delta(x-2)+120\\delta(x-6)+36\\delta(x-10)+60\\delta(x-11)+36\\delta(x-15)+9\\delta(x-20)+20\\delta(x-21)+12\\delta(x-25)+6\\delta(x-30)+\\delta(x-40)]$.⟧</p>"),
                ("⟦Số đo cho chai tiền||Numbers for the barrel⟧",
                 "<p>⟦Tổng hai lần rút bằng 6 đô có xác suất $120/400$ = {{bar_p6}}; bằng 11 đô có xác suất {{bar_p11}}; tổng các xác suất bằng {{bar_sum}} (kiểm tra số học của sách). Trung bình một lần rút {{bar_m1}}, hai lần {{bar_mean2}}; phương sai một lần {{bar_var1}}, hai lần {{bar_var2}}: đúng cộng nhau. Kiểm cả bằng liệt kê 16 cặp có thứ tự và bằng tích chập chính xác dạng phân số.||"
                 "The probability that two draws total 6 dollars is $120/400$ = {{bar_p6}}; total 11 dollars {{bar_p11}}; the probabilities add to {{bar_sum}} (the book's numerical check). The mean of one draw is {{bar_m1}}, of two {{bar_mean2}}; the variance of one draw {{bar_var1}}, of two {{bar_var2}}: they indeed add. Checked both by enumerating the 16 ordered pairs and by exact fractional convolution.⟧</p>"),
                ("⟦Cảnh báo: có độc lập không?||A warning: are the draws independent?⟧",
                 "<p>⟦Quan hệ tích chập giả định hai đại lượng không ảnh hưởng nhau. Nếu chai được đổ đầy bằng cách ném từng nắm mỗi loại tiền và không khuấy kỹ thì kết quả có thể khác; hoặc nếu chỉ có một tờ 20 đô trong chai thì rút được nó sẽ ảnh hưởng mạnh lần rút sau. Trước khi áp dụng tích chập phải luôn xét xem hai lần rút có độc lập hay không, tức quy tắc tích có áp dụng được không (Bracewell, tr. 433). Số đo: chỉ có một tờ 20 trong chai 20 tờ (ví dụ), thì P(tổng 40) khi rút hai không hoàn lại là {{bar_dep}}, không phải $1/400$.||"
                 "The convolution relation assumes the two quantities do not influence each other. If the barrel had been filled by throwing in great wads of each denomination and not thoroughly stirred the results could differ; or if there were only one twenty-dollar bill, drawing it would radically influence the second draw. Before applying convolution always consider whether the two draws are independent, i.e. whether the product rule applies (Bracewell, p. 433). Measured: with a single twenty in a barrel of 20 bills (an example), the probability of a total of 40 when drawing two without replacement is {{bar_dep}}, not $1/400$.⟧</p>"),
                ("⟦Hệ quả: trung bình và phương sai cộng nhau||Consequences: means and variances add⟧",
                 "<p>⟦Hoành độ trọng tâm cộng nhau dưới tích chập, vậy $m=m_1+m_2$: trung bình của tổng hai biến ngẫu nhiên là tổng hai trung bình. Phương sai cũng cộng: $\\sigma^2=\\sigma_1^2+\\sigma_2^2$ (Bracewell, tr. 434). Với ba đại lượng $P=P_1*P_2*P_3$ nhờ tính kết hợp, và mở rộng cho mọi số đại lượng. Barkat viết các kết quả cùng nghĩa cho biến ngẫu nhiên: $E[X+Y]=E[X]+E[Y]$ (luôn đúng), $\\text{var}[X+Y]=\\text{var}X+\\text{var}Y$ (khi không tương quan) (mục 1.5.2, tr. 41 đến 43).||"
                 "The abscissas of centroids add under convolution, so $m=m_1+m_2$: the mean of the sum of two random variables is the sum of the means. Variances also add: $\\sigma^2=\\sigma_1^2+\\sigma_2^2$ (Bracewell, p. 434). For three quantities $P=P_1*P_2*P_3$ by associativity, and it extends to any number. Barkat writes the same results for random variables: $E[X+Y]=E[X]+E[Y]$ (always true), $\\text{var}[X+Y]=\\text{var}X+\\text{var}Y$ (when uncorrelated) (section 1.5.2, pp. 41 to 43).⟧</p>"
                 + F("⟦Cộng dưới tích chập||Adding under convolution⟧", r"m=m_1+m_2,\qquad \sigma^2=\sigma_1^2+\sigma_2^2\qquad(P=P_1*P_2)")),
                ("⟦Tổng đồng đều: hình thang tổng quát||Sum of uniforms: the general trapezoid⟧",
                 "<p>⟦Barkat, ví dụ 1.20: $X$ đều trên $[0,a]$, $Y$ đều trên $[0,b]$, $a<b$; mật độ của $Z=X+Y$ là tích chập, tính bằng đồ thị: $z/(ab)$ khi $0\\le z<a$; $1/b$ khi $a\\le z<b$; $(a+b-z)/(ab)$ khi $b\\le z<a+b$ (mục 1.6.2, tr. 52 đến 54). Với $a=1$, $b=2$: $f_Z(0.5)$ = {{uu_05}}; $f_Z(1.5)$ = {{uu_15}} (đỉnh phẳng); $f_Z(2.5)$ = {{uu_25}}. Đó chính là hình thang của Bracewell, cả hai cách viết đều là một phép tích chập.||"
                 "Barkat, example 1.20: $X$ uniform on $[0,a]$, $Y$ uniform on $[0,b]$, $a<b$; the density of $Z=X+Y$ is the convolution, computed graphically: $z/(ab)$ for $0\\le z<a$; $1/b$ for $a\\le z<b$; $(a+b-z)/(ab)$ for $b\\le z<a+b$ (section 1.6.2, pp. 52 to 54). With $a=1$, $b=2$: $f_Z(0.5)$ = {{uu_05}}; $f_Z(1.5)$ = {{uu_15}} (the flat top); $f_Z(2.5)$ = {{uu_25}}. This is exactly Bracewell's trapezoid; both are one convolution.⟧</p>"),
                ("⟦Tích, thương, cực đại, cực tiểu||Product, quotient, maximum, minimum⟧",
                 "<p>⟦Với $X,Y$ độc lập: $U=XY$ có $f_U(u)=\\int\\frac1{|x|}f_X(x)f_Y(u/x)dx$; $V=X/Y$ có $f_V(v)=\\int|y|f_X(vy)f_Y(y)dy$; $M=\\max(X,Y)$ có $F_M=F_XF_Y$ nên $f_M=F_Xf_Y+f_XF_Y$; $N=\\min(X,Y)$ có $f_N=f_X(1-F_Y)+f_Y(1-F_X)$ (Barkat, tr. 55 đến 58). Với $X,Y$ đồng đều $(0,1)$: $f_U(u)=-\\ln u$, $f_U(0.2)$ = {{prod_f}}, $E[U]$ = {{prod_e}}; $E[M]$ = {{mx_e}} và $E[N]$ = {{mn_e}}, mỗi số theo tích phân và mô phỏng.||"
                 "For independent $X,Y$: $U=XY$ has $f_U(u)=\\int\\frac1{|x|}f_X(x)f_Y(u/x)dx$; $V=X/Y$ has $f_V(v)=\\int|y|f_X(vy)f_Y(y)dy$; $M=\\max(X,Y)$ has $F_M=F_XF_Y$ so $f_M=F_Xf_Y+f_XF_Y$; $N=\\min(X,Y)$ has $f_N=f_X(1-F_Y)+f_Y(1-F_X)$ (Barkat, pp. 55 to 58). For $X,Y$ uniform on $(0,1)$: $f_U(u)=-\\ln u$, $f_U(0.2)$ = {{prod_f}}, $E[U]$ = {{prod_e}}; $E[M]$ = {{mx_e}} and $E[N]$ = {{mn_e}}, each by integration and simulation.⟧</p>"),
                ("⟦Hàm một biến: định lý cơ bản||A function of one variable: the fundamental theorem⟧",
                 "<p>⟦Nếu $Y=g(X)$ đơn điệu khả vi thì $f_Y(y)=f_X[g^{-1}(y)]\\,|d g^{-1}/dy|$; nếu có nhiều nghiệm $x_i$ thì $f_Y(y)=\\sum f_X(x_i)/|g'(x_i)|$; và cho $Y=aX+b$, $f_Y=\\frac1{|a|}f_X\\!\\left(\\frac{y-b}a\\right)$ (Barkat, mục 1.6.1, tr. 49 đến 51). Ví dụ 1.19: $Y=aX^2$ có hai nghiệm $\\pm\\sqrt{y/a}$: $f_Y=\\frac1{2\\sqrt{ay}}[f_X(\\sqrt{y/a})+f_X(-\\sqrt{y/a})]$. Số đo với $X$ chuẩn, $a=2$: $E[Y]$ = {{ft_e}}, và $P(Y\\le1)$ = {{ft_p}} từ mật độ của $Y$ và từ hàm sai số.||"
                 "If $Y=g(X)$ is monotone and differentiable then $f_Y(y)=f_X[g^{-1}(y)]\\,|dg^{-1}/dy|$; with several roots $x_i$, $f_Y(y)=\\sum f_X(x_i)/|g'(x_i)|$; and for $Y=aX+b$, $f_Y=\\frac1{|a|}f_X\\!\\left(\\frac{y-b}a\\right)$ (Barkat, section 1.6.1, pp. 49 to 51). Example 1.19: $Y=aX^2$ has two roots $\\pm\\sqrt{y/a}$: $f_Y=\\frac1{2\\sqrt{ay}}[f_X(\\sqrt{y/a})+f_X(-\\sqrt{y/a})]$. Measured with a normal $X$, $a=2$: $E[Y]$ = {{ft_e}}, and $P(Y\\le1)$ = {{ft_p}} from the density of $Y$ and from the error function.⟧</p>"),
                ("⟦Tự kiểm tra phần 3||Self-check, part 3⟧",
                 UL(["⟦Vì sao phân bố của tổng hai biến độc lập là tích chập?||Why is the distribution of the sum of two independent variables a convolution?⟧",
                     "⟦Trung bình và phương sai của tổ hợp nối tiếp $100\\Omega+50\\Omega$?||The mean and variance of the series combination $100\\Omega+50\\Omega$?⟧",
                     "⟦Khi nào không được áp dụng tích chập cho hai lần rút?||When must convolution not be applied to two draws?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: tích tần suất $P_1(x')P_2(x-x')$ tích phân theo $x'$; 150 và 41.67; khi các lần rút phụ thuộc nhau.||Hints: the product $P_1(x')P_2(x-x')$ integrated over $x'$; 150 and 41.67; when the draws depend on each other.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 4
        dict(
            title="⟦Hàm đặc trưng, giới hạn trung tâm và các cận||The characteristic function, the central limit and bounds⟧",
            scr=("⟦Tích chập khó tính, nhưng biến đổi Fourier biến tích chập thành phép nhân.||Convolution is hard to compute, but the Fourier transform turns convolution into multiplication.⟧",
                 "⟦Hàm đặc trưng là biến đổi Fourier (dấu cộng) của mật độ; nhân các hàm đặc trưng cho phân bố của tổng, và đạo hàm tại 0 cho mômen.||The characteristic function is the (plus-sign) Fourier transform of the density; multiplying characteristic functions gives the distribution of a sum, and derivatives at 0 give moments.⟧",
                 "⟦Từ đó giải thích giới hạn trung tâm và cho phép chứng minh luật số lớn, cận Tchebycheff và Chernoff.||From it we explain the central limit and can prove the law of large numbers, and the Chebyshev and Chernoff bounds.⟧"),
            preview=["⟦Định nghĩa và tính chất||Definition and properties⟧", "⟦Lấy mômen, tổng độc lập, giới hạn trung tâm||Moments, independent sums and the central limit⟧", "⟦Tchebycheff, Chernoff, luật số lớn||Chebyshev, Chernoff and the law of large numbers⟧"],
            slides=[
                ("⟦Định nghĩa hàm đặc trưng||Definition of the characteristic function⟧",
                 "<p>⟦Bracewell: hàm đặc trưng gắn với phân bố tần suất $P(x)$ là $\\phi(t)=\\int P(x)e^{ixt}dx$, tức biến đổi Fourier dấu cộng của phân bố (chương 16, tr. 435). Barkat: $\\Phi_x(\\omega)=E[e^{j\\omega X}]=\\int f_X(x)e^{j\\omega x}dx$, biến đổi Fourier của mật độ, và nghịch đảo $f_X(x)=\\frac1{2\\pi}\\int e^{-j\\omega x}\\Phi_x(\\omega)d\\omega$ (mục 1.4.2, tr. 27 đến 28) [dấu của số mũ trong bản in nghịch đảo phụ thuộc quy ước]. Hai định nghĩa là một; liên hệ với biến đổi Fourier quen thuộc của Bracewell: $\\phi(t)=F(-t/2\\pi)$ với $F(s)=\\int P(x)e^{-i2\\pi xs}dx$.||"
                 "Bracewell: the characteristic function associated with a frequency distribution $P(x)$ is $\\phi(t)=\\int P(x)e^{ixt}dx$, the plus-sign Fourier transform of the distribution (chapter 16, p. 435). Barkat: $\\Phi_x(\\omega)=E[e^{j\\omega X}]=\\int f_X(x)e^{j\\omega x}dx$, the Fourier transform of the density, with inverse $f_X(x)=\\frac1{2\\pi}\\int e^{-j\\omega x}\\Phi_x(\\omega)d\\omega$ (section 1.4.2, pp. 27 to 28) [the sign of the exponent in the printed inverse depends on convention]. The two definitions are one; relation to Bracewell's usual transform: $\\phi(t)=F(-t/2\\pi)$ with $F(s)=\\int P(x)e^{-i2\\pi xs}dx$.⟧</p>"
                 + F("⟦Hàm đặc trưng||Characteristic function⟧", r"\phi(t)=E\!\left[e^{itX}\right]=\int_{-\infty}^{\infty}P(x)\,e^{ixt}\,dx")),
                ("⟦Ví dụ: phân bố Laplace||Example: the Laplace distribution⟧",
                 "<p>⟦Với $P(x)=\\tfrac12e^{-|x|}$: $\\phi(t)=\\dfrac1{1+t^2}$. Số đo tại $t=0.5$: tích phân số {{cf_lap}}, đúng $1/(1+0.25)$; theo liên hệ Bracewell tại $t=0.7$: $F(-0.7/2\\pi)$ = {{cf_rel}} bằng $\\phi(0.7)$ = $1/(1+0.49)$. (Ví dụ 1.14 của Barkat, theo lớp chữ của bản PDF, dùng $e^{-|x|/2}$ với kết quả $4/(1+4\\omega^2)$; mật độ này có tích phân 4 chứ không phải 1, nên ở đây ta dùng $\\tfrac12e^{-|x|}$ đã chuẩn hóa.)||"
                 "With $P(x)=\\tfrac12e^{-|x|}$: $\\phi(t)=\\dfrac1{1+t^2}$. Measured at $t=0.5$: numerical integral {{cf_lap}}, exactly $1/(1+0.25)$; through the Bracewell relation at $t=0.7$: $F(-0.7/2\\pi)$ = {{cf_rel}}, equal to $\\phi(0.7)$ = $1/(1+0.49)$. (Barkat's example 1.14, as read from the PDF text layer, uses $e^{-|x|/2}$ with result $4/(1+4\\omega^2)$; that function integrates to 4, not 1, so here we use the normalised $\\tfrac12e^{-|x|}$.)⟧</p>"),
                ("⟦Tính chất của hàm đặc trưng||Properties of the characteristic function⟧",
                 UL(["⟦$\\phi(0)=1$, vì $\\int P(x)dx=1$.||$\\phi(0)=1$, since $\\int P(x)dx=1$.⟧",
                     "⟦$\\phi(-t)=\\phi^*(t)$ (Hermite) vì $P$ thực: phần thực chẵn, phần ảo lẻ.||$\\phi(-t)=\\phi^*(t)$ (Hermitian) since $P$ is real: the real part even, the imaginary part odd.⟧",
                     "⟦$|\\phi(t)|\\le1$.||$|\\phi(t)|\\le1$.⟧",
                     "⟦Nếu $P(x)=0$ với $x<0$ thì phần thực và phần ảo của $\\phi$ là một cặp Hilbert; nếu $P$ bằng 0 trên nửa đường thẳng khác thì dùng định lý dịch (Bracewell, tr. 435).||If $P(x)=0$ for $x<0$ the real and imaginary parts of $\\phi$ form a Hilbert pair; if $P$ is zero over some other semi-infinite range, use the shift theorem (Bracewell, p. 435).⟧"])
                 + "<p>⟦Số đo với phân bố mũ $P=e^{-x}H(x)$, $\\phi=1/(1-it)$: $\\phi(0)$ = {{cf_0}}, $\\max|\\phi|$ trên lưới = {{cf_max}}, và lệch Hermite {{cf_herm}}. Barkat thêm: hàm đặc trưng luôn tồn tại còn hàm sinh mômen thì không chắc (tr. 28).||Measured with the exponential distribution $P=e^{-x}H(x)$, $\\phi=1/(1-it)$: $\\phi(0)$ = {{cf_0}}, $\\max|\\phi|$ on a grid = {{cf_max}}, and Hermitian deviation {{cf_herm}}. Barkat adds: the characteristic function always exists whereas the moment generating function may not (p. 28).⟧</p>"),
                ("⟦Hàm sinh mômen và lấy mômen||The moment generating function and taking moments⟧",
                 "<p>⟦Hàm sinh mômen $M_x(t)=E[e^{tX}]$ khai triển chuỗi McLaurin cho $M_x(t)=1+tE[X]+\\frac{t^2}{2!}E[X^2]+\\cdots$, nên $M_x^{(n)}(0)=E[X^n]$. Đặt $t=j\\omega$ được hàm đặc trưng, với $E[X^n]=(-j)^n\\,d^n\\Phi/d\\omega^n|_{\\omega=0}$ (Barkat, tr. 26 đến 28). Bracewell (module 8) đã có cùng kết quả: mômen bậc $n$ bằng $(-2\\pi i)^{-n}F^{(n)}(0)$. Số đo với Laplace: $E[X^2]$ = {{cf_m2}} và $E[X^4]$ = {{cf_m4}}, cả từ tích phân trực tiếp lẫn từ đạo hàm của $\\phi=1/(1+t^2)$ (tích phân đường quanh 0).||"
                 "The moment generating function $M_x(t)=E[e^{tX}]$ expands in the McLaurin series $M_x(t)=1+tE[X]+\\frac{t^2}{2!}E[X^2]+\\cdots$, so $M_x^{(n)}(0)=E[X^n]$. Setting $t=j\\omega$ gives the characteristic function, with $E[X^n]=(-j)^n\\,d^n\\Phi/d\\omega^n|_{\\omega=0}$ (Barkat, pp. 26 to 28). Bracewell (module 8) has the same result: the $n$th moment equals $(-2\\pi i)^{-n}F^{(n)}(0)$. Measured with the Laplace distribution: $E[X^2]$ = {{cf_m2}} and $E[X^4]$ = {{cf_m4}}, both from direct integration and from derivatives of $\\phi=1/(1+t^2)$ (a contour integral around 0).⟧</p>"),
                ("⟦Tổng độc lập: nhân các hàm đặc trưng||Independent sums: multiply the characteristic functions⟧",
                 "<p>⟦Biến đổi $P=P_1*P_2$ ta có $\\phi(t)=\\phi_1(t)\\phi_2(t)$: nhân đơn giản các hàm đặc trưng cho hàm đặc trưng của phân bố tổng (Bracewell, tr. 435; Barkat, phương trình 1.135, tr. 45). Đó chính là định lý tích chập. Số đo: tổng hai biến Laplace độc lập có hàm đặc trưng $1/(1+t^2)^2$; mật độ tại 0 là $\\frac1{2\\pi}\\int(1+t^2)^{-2}dt$ = {{cf_sum0}} và bằng $\\int P(u)P(-u)du$ từ tích chập trực tiếp.||"
                 "Transforming $P=P_1*P_2$ gives $\\phi(t)=\\phi_1(t)\\phi_2(t)$: simple multiplication of the characteristic functions gives the characteristic function of the distribution of a sum (Bracewell, p. 435; Barkat, equation 1.135, p. 45). That is just the convolution theorem. Measured: the sum of two independent Laplace variables has characteristic function $1/(1+t^2)^2$; its density at 0 is $\\frac1{2\\pi}\\int(1+t^2)^{-2}dt$ = {{cf_sum0}} and equals $\\int P(u)P(-u)du$ from the direct convolution.⟧</p>"
                 + F("⟦Tổng||Sum⟧", r"P=P_1*P_2\ \Longleftrightarrow\ \phi(t)=\phi_1(t)\,\phi_2(t)")),
                ("⟦Giới hạn trung tâm nhìn qua hàm đặc trưng||The central limit through the characteristic function⟧",
                 "<p>⟦Nếu nhiều đại lượng ngẫu nhiên được cộng thì phân bố của tổng tiến tới Gauss, với trung bình bằng tổng các trung bình và phương sai bằng tổng các phương sai; khi đủ nhiều thành phần, hai tham số ấy đủ xác định Gauss (Bracewell, tr. 434 đến 435). Nhìn qua $\\phi^n$: gần $t=0$, $\\phi\\approx1-\\sigma^2t^2/2$ nên $\\phi^n\\approx e^{-n\\sigma^2t^2/2}$, là Gauss, đúng như module 8. Số đo: tổng 12 biến đồng đều trên $(-\\tfrac12,\\tfrac12)$ (phương sai 1) có mật độ tại 0 bằng {{clt_f0}} tính từ tích chập 12 lần và từ $\\frac1{2\\pi}\\int\\phi^{12}$, so với Gauss chuẩn {{clt_g0}}.||"
                 "If several random quantities are added, the distribution of the sum approaches a Gaussian, the mean being the sum of the means and the variance the sum of the variances; with enough components these two parameters fix the Gaussian (Bracewell, pp. 434 to 435). Through $\\phi^n$: near $t=0$, $\\phi\\approx1-\\sigma^2t^2/2$ so $\\phi^n\\approx e^{-n\\sigma^2t^2/2}$, a Gaussian, exactly as in module 8. Measured: the sum of 12 variables uniform on $(-\\tfrac12,\\tfrac12)$ (variance 1) has density at 0 equal to {{clt_f0}} by 12-fold convolution and by $\\frac1{2\\pi}\\int\\phi^{12}$, against the standard Gaussian {{clt_g0}}.⟧</p>"),
                ("⟦Tchebycheff||The Chebyshev inequality⟧",
                 "<p>⟦Khi phân bố chưa biết đầy đủ nhưng biết trung bình $m_x$ và phương sai $\\sigma_x^2$, ta cần cận trên cho xác suất. Tchebycheff: $P(|X-m_x|\\ge\\varepsilon)\\le\\sigma_x^2/\\varepsilon^2$; với $\\varepsilon=k\\sigma_x$ thì $\\le1/k^2$ (Barkat, mục 1.4.3, tr. 29). Với phân bố mũ đơn vị ($m=1$, $\\sigma^2=1$): $P(|X-1|\\ge2)=P(X\\ge3)$ = {{true_3}} và cận Tchebycheff {{cheb_3}}; $P(|X-1|\\ge9)$ = {{true_10}} với cận {{cheb_10}}.||"
                 "When the distribution is not completely specified but the mean $m_x$ and variance $\\sigma_x^2$ are known we want an upper bound on probabilities. Chebyshev: $P(|X-m_x|\\ge\\varepsilon)\\le\\sigma_x^2/\\varepsilon^2$; with $\\varepsilon=k\\sigma_x$ it is $\\le1/k^2$ (Barkat, section 1.4.3, p. 29). For the unit exponential ($m=1$, $\\sigma^2=1$): $P(|X-1|\\ge2)=P(X\\ge3)$ = {{true_3}} and the Chebyshev bound {{cheb_3}}; $P(|X-1|\\ge9)$ = {{true_10}} with bound {{cheb_10}}.⟧</p>"
                 + F("⟦Tchebycheff||Chebyshev⟧", r"P\big(|X-m_x|\ge\varepsilon\big)\le\frac{\sigma_x^2}{\varepsilon^2}")),
                ("⟦Chernoff||The Chernoff bound⟧",
                 "<p>⟦Chernoff chỉ dùng một phía. Với $Y=1$ khi $X\\ge\\varepsilon$ và mọi $t>0$: $Ye^{t\\varepsilon}\\le e^{tX}$, nên $P(X\\ge\\varepsilon)\\le e^{-t\\varepsilon}E[e^{tX}]$ (Barkat, tr. 29 đến 30). Cần biết thêm về phân bố để tính $E[e^{tX}]$, và chọn $t$ để cận nhỏ nhất. Với phân bố mũ đơn vị $E[e^{tX}]=1/(1-t)$, $t=1-1/\\varepsilon$ tối ưu: cận cho $P(X\\ge3)$ là {{chern_3}} (lỏng hơn Tchebycheff {{cheb_3}} vì Tchebycheff hai phía cho cận $\\tfrac14$ nhưng đại lượng này chỉ nằm một phía), và cho $P(X\\ge10)$ là {{chern_10}} (chặt hơn nhiều so với {{cheb_10}}, và gần giá trị thật {{true_10}}). Chernoff không phải lúc nào cũng chặt hơn; nó thắng khi đuôi xa.||"
                 "Chernoff uses only one side. With $Y=1$ for $X\\ge\\varepsilon$ and any $t>0$: $Ye^{t\\varepsilon}\\le e^{tX}$, so $P(X\\ge\\varepsilon)\\le e^{-t\\varepsilon}E[e^{tX}]$ (Barkat, pp. 29 to 30). More knowledge of the distribution is needed to evaluate $E[e^{tX}]$, and $t$ is chosen to minimise the bound. For the unit exponential $E[e^{tX}]=1/(1-t)$, the optimum is $t=1-1/\\varepsilon$: the bound for $P(X\\ge3)$ is {{chern_3}} (looser than Chebyshev's {{cheb_3}}, since the two-sided Chebyshev gives $\\tfrac14$ while this quantity lies on one side only), and for $P(X\\ge10)$ it is {{chern_10}} (much tighter than {{cheb_10}} and close to the true {{true_10}}). Chernoff is not always tighter; it wins at far tails.⟧</p>{{fig:bounds}}"),
                ("⟦Luật số lớn||The law of large numbers⟧",
                 "<p>⟦Cho $X_1,\\ldots,X_n$ độc lập cùng trung bình $m_x$, phương sai $\\sigma_x^2$; $S_n=\\sum X_i$. Luật yếu: $\\lim_{n\\to\\infty}P(|S_n/n-m_x|\\ge\\varepsilon)=0$, chứng minh bằng Tchebycheff với $\\text{var}(S_n/n)=\\sigma_x^2/n$; luật mạnh: xác suất $\\lim S_n/n=m_x$ bằng 1 (Barkat, tr. 30 đến 31). Số đo: 1000 phép thử Bernoulli, $p=0.3$, $\\varepsilon=0.05$: xác suất chính xác $P(|S_n/n-0.3|\\ge0.05)$ = {{lln_exact}} còn cận Tchebycheff $pq/(n\\varepsilon^2)$ = {{lln_bound}}: đúng nhưng rất lỏng.||"
                 "Let $X_1,\\ldots,X_n$ be independent with common mean $m_x$ and variance $\\sigma_x^2$; $S_n=\\sum X_i$. The weak law: $\\lim_{n\\to\\infty}P(|S_n/n-m_x|\\ge\\varepsilon)=0$, proved with Chebyshev using $\\text{var}(S_n/n)=\\sigma_x^2/n$; the strong law: the probability that $\\lim S_n/n=m_x$ is one (Barkat, pp. 30 to 31). Measured: 1000 Bernoulli trials, $p=0.3$, $\\varepsilon=0.05$: the exact probability $P(|S_n/n-0.3|\\ge0.05)$ = {{lln_exact}} while the Chebyshev bound $pq/(n\\varepsilon^2)$ = {{lln_bound}}: correct but very loose.⟧</p>"),
                ("⟦Nghịch lý điện trở chính xác||The precision-resistor fallacy⟧",
                 "<p>⟦Bài tập 3 của Bracewell: để làm điện trở chuẩn 1 megôm, lấy 10 000 điện trở 100 ôm sai số 1 phần trăm nối tiếp. Lập luận: trung bình $nR$, phương sai $n\\sigma^2$, độ lệch chuẩn $\\sqrt n\\sigma$, nên độ lệch tương đối $\\sigma/(R\\sqrt n)\\sim10^{-4}$. Sai lầm nằm ở giả định độc lập: điện trở cùng lô có sai lệch chung (cùng nhiệt độ, cùng lô sản xuất, cùng hệ số nhiệt). Số đo với sai số đồng đều $\\pm1$ phần trăm độc lập: độ lệch tương đối {{bo_ind}}; nếu thêm độ lệch chung của lô đều $\\pm0.5$ phần trăm thì {{bo_corr}}, không cải thiện được ngoài mức ấy (tr. 443). Đây là minh họa của chúng tôi cho một cách giải thích khả dĩ.||"
                 "Bracewell's problem 3: to make a 1-megohm standard resistor, connect 10,000 ordinary 100-ohm 1-percent resistors in series. The argument: mean $nR$, variance $n\\sigma^2$, standard deviation $\\sqrt n\\sigma$, so the relative deviation $\\sigma/(R\\sqrt n)\\sim10^{-4}$. The fallacy is the assumption of independence: resistors from one batch share a common offset (same temperature, same production lot, same temperature coefficient). Measured with independent uniform $\\pm1$ percent errors: relative deviation {{bo_ind}}; adding a common batch offset uniform $\\pm0.5$ percent gives {{bo_corr}}, with no improvement beyond that level (p. 443). This is our illustration of one plausible explanation.⟧</p>"),
                ("⟦Tự kiểm tra phần 4||Self-check, part 4⟧",
                 UL(["⟦Hàm đặc trưng của tổng hai biến độc lập là gì?||What is the characteristic function of the sum of two independent variables?⟧",
                     "⟦Làm sao lấy $E[X^2]$ từ $\\phi(t)$?||How do we get $E[X^2]$ from $\\phi(t)$?⟧",
                     "⟦Tchebycheff cần biết gì về phân bố?||What does Chebyshev need to know about the distribution?⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: tích $\\phi_1\\phi_2$; $-\\phi''(0)$; chỉ cần trung bình và phương sai.||Hints: the product $\\phi_1\\phi_2$; $-\\phi''(0)$; only the mean and variance.⟧</p>"),
            ]),
        # ------------------------------------------------ PART 5
        dict(
            title="⟦Phân bố mũ, gamma, Poisson và biến ngẫu nhiên hai chiều||The exponential, gamma and Poisson distributions and two-dimensional variables⟧",
            scr=("⟦Các biến cố hoàn toàn ngẫu nhiên, như phân rã phóng xạ hay cuộc gọi điện thoại, cách nhau những khoảng có phân bố nào?||What distribution do the intervals between completely random events, such as radioactive decays or telephone calls, follow?⟧",
                 "⟦Cộng các khoảng đó cho gamma rồi Poisson và Gauss; và nhiều đại lượng thì phải xét chung: mật độ đồng thời, biên, điều kiện, tương quan.||Adding them gives gamma, then Poisson and Gaussian; and several quantities must be treated jointly: joint density, marginals, conditionals, correlation.⟧",
                 "⟦Độc lập kéo theo không tương quan, nhưng ngược lại không đúng.||Independence implies uncorrelatedness, but not conversely.⟧"),
            preview=["⟦Phân bố mũ cắt cụt||The truncated exponential distribution⟧", "⟦Gamma, Poisson và tiến về Gauss||Gamma, Poisson and the approach to Gaussian⟧", "⟦Hai chiều: đồng thời, biên, điều kiện, tương quan||Two dimensions: joint, marginal, conditional, correlation⟧"],
            slides=[
                ("⟦Biến cố ngẫu nhiên hoàn toàn||Completely random events⟧",
                 "<p>⟦Ví dụ tốt nhất về biến cố hoàn toàn ngẫu nhiên là sự phân rã phóng xạ tự phát của hạt nhân; cuộc gọi điện thoại và sự bức xạ electron từ catốt cũng có thể trong điều kiện nhất định. Quan sát cho thấy nguyên tử không bền phân rã ở mọi thời điểm có khả năng như nhau, nên số phân rã mỗi giây tỉ lệ với số nguyên tử chưa phân rã. Khoảng cách giữa hai biến cố kề nhau ngắn hơn trung bình thì thường hơn: khoảng càng ngắn càng thường, tới tận khoảng 0, liên quan tới câu ngạn ngữ \"tai họa đến từng cặp\" (Bracewell, tr. 436).||"
                 "The best example of a completely random event is the spontaneous radioactive disintegration of an atomic nucleus; telephone calls or electron emission from a cathode may serve under certain conditions. Observation shows an unstable atom is as likely to disintegrate at one moment as at any other, so the number of disintegrations per second is proportional to the number of unstable atoms present. Intervals shorter than average between one event and the next are more frequent: the shorter the interval the more frequent, right down to zero, connected with the folk saying that misfortunes occur in pairs (Bracewell, p. 436).⟧</p>"),
                ("⟦Phân bố mũ cắt cụt: suy ra||The truncated exponential: derivation⟧",
                 "<p>⟦Khoảng trung bình giữa các biến cố là $X$ nên tốc độ trung bình là $X^{-1}$ trên đơn vị. Xác suất xảy ra trong khoảng ngắn $\\Delta x$ là $X^{-1}\\Delta x$; không xảy ra là $1-X^{-1}\\Delta x$. Sau một biến cố, tần suất để $N=x/\\Delta x$ khoảng liên tiếp không có biến cố rồi khoảng kế có biến cố là $P(x)\\Delta x=(1-X^{-1}\\Delta x)^NX^{-1}\\Delta x$; khi $\\Delta x\\to0$, $P(x)=X^{-1}e^{-x/X}H(x)$ (Bracewell, tr. 437). Với $X=2$, $x=3$, $N=10^7$: biểu thức giới hạn cho {{ex_pdf}}, đúng $e^{-1.5}/2$.||"
                 "The mean interval between events is $X$ so the average rate is $X^{-1}$ per unit. The probability of an occurrence in a brief space $\\Delta x$ is $X^{-1}\\Delta x$; of nonoccurrence $1-X^{-1}\\Delta x$. After one event, the frequency of failing to occur in each of $N=x/\\Delta x$ successive spaces then occurring in the next is $P(x)\\Delta x=(1-X^{-1}\\Delta x)^NX^{-1}\\Delta x$; as $\\Delta x\\to0$, $P(x)=X^{-1}e^{-x/X}H(x)$ (Bracewell, p. 437). With $X=2$, $x=3$, $N=10^7$: the limiting expression gives {{ex_pdf}}, exactly $e^{-1.5}/2$.⟧</p>"
                 + F("⟦Phân bố mũ cắt cụt||Truncated exponential⟧", r"P(x)=\frac1X\,e^{-x/X}H(x),\qquad m=X,\quad \sigma^2=X^2")),
                ("⟦Thử số: trung bình và phương sai||Numerical test: mean and variance⟧",
                 "<p>⟦Trung bình $m=X$ và phương sai $\\sigma^2=X^2$ (Bracewell, tr. 436). Mô phỏng $10^6$ khoảng với $X=2$: trung bình {{ex_mean}}, phương sai {{ex_var}} (đúng $4$); và tích phân số của $xP(x)$ và $x^2P(x)$ cho cùng số. Dạng này còn xuất hiện ở kích thước sự kiện: nếu kích thước tỉ lệ với khoảng thời gian trôi qua và sự kiện xảy ra ở thời điểm ngẫu nhiên đều thì kích thước theo đúng phân bố mũ cắt cụt, thí dụ động đất nhỏ và trận mưa nhỏ nhiều hơn lớn (tr. 437 đến 438).||"
                 "The mean is $m=X$ and the variance $\\sigma^2=X^2$ (Bracewell, p. 436). A simulation of $10^6$ intervals with $X=2$: mean {{ex_mean}}, variance {{ex_var}} (exactly $4$); and numerical integrals of $xP(x)$ and $x^2P(x)$ give the same numbers. The same form appears for event sizes: if the size is proportional to the elapsed interval and the event is as likely at one moment as another, sizes follow the truncated exponential law, e.g. small earthquakes and small showers are more frequent than large (pp. 437 to 438).⟧</p>"),
                ("⟦Cộng các khoảng: gamma (Pearson III)||Adding intervals: the gamma (Pearson III) distribution⟧",
                 "<p>⟦Với $E(x)=e^{-x}H(x)$ (trung bình một đơn vị), tổng hai giá trị: $E*E=xE(x)$, giống đáp ứng xung của thiết bị tắt dần tới hạn; đỉnh không còn ở 0 mà ở 1 (Bracewell, tr. 438 đến 439). Quy nạp: $[E(x)]^{*n}=\\dfrac{x^{n-1}}{(n-1)!}e^{-x}H(x)$, phân bố Pearson loại III, cũng là phân bố gamma. Số đo: $E*E$ tại $x=2$ bằng {{gam2}} và $[E]^{*5}$ tại $x=4$ bằng {{gam5}}, theo tích chập trên lưới và theo công thức; trung bình và phương sai của $[E]^{*n}$ đều bằng $n$ (ở đây $n=5$: {{gam_mean}} và {{gam_var}}).||"
                 "With $E(x)=e^{-x}H(x)$ (mean of one unit), the sum of two values: $E*E=xE(x)$, like the impulse response of a critically damped instrument; the mode is no longer at 0 but at 1 (Bracewell, pp. 438 to 439). By induction: $[E(x)]^{*n}=\\dfrac{x^{n-1}}{(n-1)!}e^{-x}H(x)$, the Pearson type III distribution, also the gamma distribution. Measured: $E*E$ at $x=2$ is {{gam2}} and $[E]^{*5}$ at $x=4$ is {{gam5}}, by grid convolution and by the formula; the mean and variance of $[E]^{*n}$ both equal $n$ (here $n=5$: {{gam_mean}} and {{gam_var}}).⟧</p>"
                 + F("⟦Pearson III||Pearson III⟧", r"[E(x)]^{*n}=\frac{x^{n-1}}{(n-1)!}\,e^{-x}H(x)")),
                ("⟦Từ gamma tới Gauss||From gamma to Gaussian⟧",
                 "<p>⟦Theo giới hạn trung tâm, với $n$ lớn ta gần Gauss. Trung bình và phương sai đều là $n$ (hệ quả của cộng dưới tích chập); độ lệch chuẩn quanh trung bình là $n^{-1/2}$ lần trung bình, nên khi biểu diễn theo $\\xi=x/n$ ta được Gauss ngày càng hẹp (hình 16.7). Dùng công thức Stirling $n!\\approx(2\\pi n)^{1/2}n^ne^{-n}$, vế trái rút về Gauss tâm $\\xi=1-1/n$ (Bracewell, tr. 440 đến 442). Số đo với $n=100$: mật độ gamma tại giá trị trung bình chia mật độ Gauss cùng trung bình và phương sai bằng {{st_ratio}}.||"
                 "By the central-limit theorem, for large $n$ we approach a Gaussian. The mean and variance are both $n$ (a consequence of adding under convolution); the standard deviation about the mean is $n^{-1/2}$ times the mean, so expressed in $\\xi=x/n$ we get an ever narrower Gaussian (Fig. 16.7). Using Stirling's formula $n!\\approx(2\\pi n)^{1/2}n^ne^{-n}$, the left-hand side reduces to a Gaussian centred on $\\xi=1-1/n$ (Bracewell, pp. 440 to 442). Measured with $n=100$: the gamma density at its mean divided by the Gaussian density of the same mean and variance is {{st_ratio}}.⟧</p>{{fig:gamma_clt}}"),
                ("⟦Poisson từ các khoảng ngẫu nhiên||Poisson from random intervals⟧",
                 "<p>⟦Nếu các biến cố xảy ra ngẫu nhiên như hình 16.5 với khoảng trung bình 1, xác suất để có đúng $n$ biến cố trong khoảng $x$ là tích phân của xác suất biến cố thứ $n$ tới ở $x'$ và biến cố kế tiếp tới sau $x-x'$: $\\int[E(x')]^{*n}E(x-x')dx'=[E]^{*(n+1)}\\text{-like}=\\dfrac{x^n}{n!}e^{-x}$, tức phân bố Poisson (Bracewell, tr. 442). Số đo: $n=2$, $x=3$: {{po_pmf}} theo tích phân, theo công thức và theo hàm khối Poisson; bài tập 5: sự kiện 0.1 lần mỗi micrô giây, đúng hai lần trong 1 micrô giây: {{p5_val}}. Bài tập 14: các số hạng cộng lại bằng {{po_sum}}, và khi $x$ nguyên có hai số hạng bằng nhau ($x=4$: $P(3)=P(4)$ = {{po_eq}}).||"
                 "If events occur at random as in Fig. 16.5 with average interval unity, the probability that precisely $n$ events occur in the interval $x$ is the integral of the probability that the $n$th event arrives at $x'$ and the next arrives after a further $x-x'$: $\\int[E(x')]^{*n}E(x-x')dx'=\\dfrac{x^n}{n!}e^{-x}$, the Poisson distribution (Bracewell, p. 442). Measured: $n=2$, $x=3$: {{po_pmf}} by the integral, by the formula and by the Poisson mass function; problem 5: an event 0.1 times per microsecond, exactly two in 1 microsecond: {{p5_val}}. Problem 14: the terms sum to {{po_sum}}, and when $x$ is an integer two terms are equal ($x=4$: $P(3)=P(4)$ = {{po_eq}}).⟧</p>"),
                ("⟦Poisson cộng nhau; nhị thức||Poisson adds; the binomial⟧",
                 "<p>⟦Hàm đặc trưng của Poisson $(x^n/n!)e^{-x}$ là $\\exp\\{x[e^{it}-1]\\}$, nên hai biến Poisson độc lập có trung bình $x_1,x_2$ cho tổng Poisson trung bình $x_1+x_2$ (bài tập 13, tr. 444). Bernoulli: kết cục 1 với xác suất $p$, 0 với $q=1-p$, $\\{q\\ p\\}$; tổng $n$ phép thử là $\\{q\\ p\\}^{*n}$, phân bố nhị thức có hàm đặc trưng $[q+pe^{it}]^n$ (bài tập 12). Số đo: tích chập của Poisson trung bình 2 và 3 tại 5 bằng {{po_add}}, cũng là $P(5)$ của Poisson trung bình 5; nhị thức $n=20$, $p=\\tfrac12$ tại 10: {{bin_10}}, so với Gauss $1/\\sqrt{2\\pi npq}$ = {{bin_g}}.||"
                 "The characteristic function of the Poisson $(x^n/n!)e^{-x}$ is $\\exp\\{x[e^{it}-1]\\}$, so two independent Poisson variables with means $x_1,x_2$ give a Poisson sum with mean $x_1+x_2$ (problem 13, p. 444). Bernoulli: outcome 1 with probability $p$, 0 with $q=1-p$, $\\{q\\ p\\}$; the sum of $n$ trials is $\\{q\\ p\\}^{*n}$, the binomial distribution, with characteristic function $[q+pe^{it}]^n$ (problem 12). Measured: the convolution of Poisson means 2 and 3 at 5 gives {{po_add}}, also $P(5)$ of the Poisson with mean 5; the binomial $n=20$, $p=\\tfrac12$ at 10: {{bin_10}}, against the Gaussian $1/\\sqrt{2\\pi npq}$ = {{bin_g}}.⟧</p>"),
                ("⟦Biến ngẫu nhiên hai chiều||Two-dimensional random variables⟧",
                 "<p>⟦Ta thường quan tâm quan hệ giữa hai biến. Mật độ đồng thời $f_{XY}(x,y)\\ge0$ với $\\iint f_{XY}=1$; $P(x_1<X<x_2,y_1<Y<y_2)=\\iint f_{XY}$; phân bố đồng thời $F_{XY}=P(X\\le x,Y\\le y)$ và $f_{XY}=\\partial^2F_{XY}/\\partial x\\partial y$. Mật độ biên $f_X(x)=\\int f_{XY}dy$, $f_Y(y)=\\int f_{XY}dx$; điều kiện $f_X(x\\mid y)=f_{XY}(x,y)/f_Y(y)$; độc lập khi $f_{XY}=f_Xf_Y$ (Barkat, mục 1.5, tr. 31 đến 36). Ví dụ 1.15: $f_{XY}=x^2+xy/3$ trên $[0,1]\\times[0,2]$: tích phân toàn miền {{j_int}}; $P(X>\\tfrac12)$ = {{j_px}}; $P(Y<X)$ = {{j_pyx}}; $P(Y<\\tfrac12\\mid X<\\tfrac12)$ = {{j_cond}} (tr. 38 đến 40).||"
                 "We are often interested in the relationship between two variables. The joint density $f_{XY}(x,y)\\ge0$ with $\\iint f_{XY}=1$; $P(x_1<X<x_2,y_1<Y<y_2)=\\iint f_{XY}$; the joint distribution $F_{XY}=P(X\\le x,Y\\le y)$ and $f_{XY}=\\partial^2F_{XY}/\\partial x\\partial y$. The marginals are $f_X(x)=\\int f_{XY}dy$, $f_Y(y)=\\int f_{XY}dx$; the conditional $f_X(x\\mid y)=f_{XY}(x,y)/f_Y(y)$; independence when $f_{XY}=f_Xf_Y$ (Barkat, section 1.5, pp. 31 to 36). Example 1.15: $f_{XY}=x^2+xy/3$ on $[0,1]\\times[0,2]$: total integral {{j_int}}; $P(X>\\tfrac12)$ = {{j_px}}; $P(Y<X)$ = {{j_pyx}}; $P(Y<\\tfrac12\\mid X<\\tfrac12)$ = {{j_cond}} (pp. 38 to 40).⟧</p>"),
                ("⟦Rời rạc hai chiều và kiểm tra độc lập||Discrete two-dimensional variables and an independence test⟧",
                 "<p>⟦Với biến rời rạc, mật độ đồng thời là $\\sum P(x_i,y_j)\\delta(x-x_i)\\delta(y-y_j)$, xung hai chiều có thể tích 1; mật độ biên cộng theo chiều kia (Barkat, tr. 36 đến 38). Ví dụ 1.16: bảng $P(1,0)=\\tfrac14$, $P(2,0)=\\tfrac14$, $P(1,1)=0$, $P(2,1)=\\tfrac18$, $P(1,2)=\\tfrac14$, $P(2,2)=\\tfrac18$. Độc lập cần $P(x_i,y_j)=P(x_i)P(y_j)$ với mọi cặp; chỉ cần một phản ví dụ: $P(X=1,Y=2)$ = {{j_dep}} nhưng $P(X=1)P(Y=2)$ = {{j_ind}}, nên $X$ và $Y$ không độc lập (tr. 40 đến 41).||"
                 "For discrete variables the joint density is $\\sum P(x_i,y_j)\\delta(x-x_i)\\delta(y-y_j)$, two-dimensional impulses of volume 1; marginals sum over the other index (Barkat, pp. 36 to 38). Example 1.16: the table $P(1,0)=\\tfrac14$, $P(2,0)=\\tfrac14$, $P(1,1)=0$, $P(2,1)=\\tfrac18$, $P(1,2)=\\tfrac14$, $P(2,2)=\\tfrac18$. Independence needs $P(x_i,y_j)=P(x_i)P(y_j)$ for all pairs; a single counterexample suffices: $P(X=1,Y=2)$ = {{j_dep}} but $P(X=1)P(Y=2)$ = {{j_ind}}, so $X$ and $Y$ are not independent (pp. 40 to 41).⟧</p>"),
                ("⟦Kỳ vọng có điều kiện và tương quan||Conditional expectation and correlation⟧",
                 "<p>⟦$E[X\\mid y]=\\int xf_{X|Y}(x\\mid y)dx$ và $E\\{E[X\\mid Y]\\}=E[X]$ (Barkat, tr. 44). Ví dụ 1.17: $f_{XY}=kxy$ trên $x\\le y$, $0\\le y\\le1$: $k$ = {{c17_k}}; $f_Y=4y^3$; $E[X\\mid Y=y]=2y/3$ = {{c17_e}} tại $y=0.6$; và $E\\{E[X\\mid Y]\\}=E[X]$ = {{c17_ex}} theo cả hai cách. Tương quan $R_{xy}=E[XY]$, hiệp phương sai $C_{xy}=E[(X-m_x)(Y-m_y)]$, hệ số tương quan $\\rho_{xy}=C_{xy}/(\\sigma_x\\sigma_y)$ với $-1\\le\\rho\\le1$ (mục 1.5.2, tr. 41 đến 43). Độc lập kéo theo không tương quan nhưng ngược lại không đúng.||"
                 "$E[X\\mid y]=\\int xf_{X|Y}(x\\mid y)dx$ and $E\\{E[X\\mid Y]\\}=E[X]$ (Barkat, p. 44). Example 1.17: $f_{XY}=kxy$ on $x\\le y$, $0\\le y\\le1$: $k$ = {{c17_k}}; $f_Y=4y^3$; $E[X\\mid Y=y]=2y/3$ = {{c17_e}} at $y=0.6$; and $E\\{E[X\\mid Y]\\}=E[X]$ = {{c17_ex}} by both ways. The correlation is $R_{xy}=E[XY]$, the covariance $C_{xy}=E[(X-m_x)(Y-m_y)]$, the correlation coefficient $\\rho_{xy}=C_{xy}/(\\sigma_x\\sigma_y)$ with $-1\\le\\rho\\le1$ (section 1.5.2, pp. 41 to 43). Independence implies uncorrelatedness but not conversely.⟧</p>"),
                ("⟦Không tương quan nhưng phụ thuộc: nửa đĩa||Uncorrelated yet dependent: the half-disc⟧",
                 "<p>⟦Ví dụ 1.18: $f_{XY}=2/\\pi$ trên nửa đĩa đơn vị $x^2+y^2\\le1$, $y\\ge0$. $E[XY]=0$, $E[X]=0$, $E[Y]=4/3\\pi$ = {{hd_ey}}, nên $\\rho_{xy}=0$: không tương quan (Barkat, tr. 47 đến 48). Nhưng $X$ và $Y$ phụ thuộc: $P(X>0.7,Y>0.8)$ = {{hd_pj}} trong khi $P(X>0.7)P(Y>0.8)$ = {{hd_pp}}. Hàm đặc trưng chung $\\Phi_{xy}(\\omega_1,\\omega_2)=E[e^{j(\\omega_1X+\\omega_2Y)}]$ là biến đổi Fourier hai chiều của mật độ đồng thời (tr. 44 đến 46) và mở rộng ý tưởng của phần 4 cho nhiều biến.||"
                 "Example 1.18: $f_{XY}=2/\\pi$ on the unit half-disc $x^2+y^2\\le1$, $y\\ge0$. $E[XY]=0$, $E[X]=0$, $E[Y]=4/3\\pi$ = {{hd_ey}}, so $\\rho_{xy}=0$: uncorrelated (Barkat, pp. 47 to 48). But $X$ and $Y$ are dependent: $P(X>0.7,Y>0.8)$ = {{hd_pj}} while $P(X>0.7)P(Y>0.8)$ = {{hd_pp}}. The joint characteristic function $\\Phi_{xy}(\\omega_1,\\omega_2)=E[e^{j(\\omega_1X+\\omega_2Y)}]$ is the two-dimensional Fourier transform of the joint density (pp. 44 to 46) and extends the ideas of part 4 to several variables.⟧</p>"),
                ("⟦Tự kiểm tra phần 5||Self-check, part 5⟧",
                 UL(["⟦Vì sao khoảng giữa các biến cố ngẫu nhiên có phân bố mũ?||Why do intervals between random events have an exponential distribution?⟧",
                     "⟦$[E]^{*n}$ có trung bình và phương sai bao nhiêu?||What are the mean and variance of $[E]^{*n}$?⟧",
                     "⟦Cho ví dụ hai biến không tương quan nhưng phụ thuộc.||Give an example of two variables that are uncorrelated but dependent.⟧"])
                 + "<p class='lang-note'>⟦Gợi ý: xác suất xảy ra trong mỗi khoảng ngắn như nhau; cả hai bằng $n$; nửa đĩa đơn vị đều.||Hints: the same probability of occurrence in each short interval; both equal $n$; the uniform unit half-disc.⟧</p>"),
            ]),
    ],
    takeaways=[
        "⟦Xác suất là hàm không âm, chuẩn hóa, cộng được trên biến cố loại trừ; đếm, xác suất có điều kiện và Bayes suy ra từ đó.||Probability is a nonnegative normalised function additive over exclusive events; counting, conditional probability and Bayes follow from it.⟧",
        "⟦Biến ngẫu nhiên có mật độ (kể cả xung); trung bình, phương sai, mômen là kỳ vọng của $x$, $(x-m)^2$, $x^n$.||A random variable has a density (impulses included); mean, variance and moments are expectations of $x$, $(x-m)^2$, $x^n$.⟧",
        "⟦Phân bố của tổng độc lập là tích chập; trung bình và phương sai cộng; tích, max, min có công thức riêng.||The distribution of an independent sum is a convolution; means and variances add; products, max and min have their own formulas.⟧",
        "⟦Hàm đặc trưng là biến đổi Fourier của mật độ: nhân cho tổng, đạo hàm cho mômen, và giải thích giới hạn trung tâm.||The characteristic function is the Fourier transform of the density: products give sums, derivatives give moments, and it explains the central limit.⟧",
        "⟦Khoảng giữa các biến cố ngẫu nhiên là mũ; cộng chúng cho gamma, đếm cho Poisson; độc lập kéo theo không tương quan, không ngược lại.||Intervals between random events are exponential; adding them gives gamma, counting gives Poisson; independence implies uncorrelatedness, not conversely.⟧",
    ],
    history="<p>⟦Bracewell nhắc các nguồn: Gardner (1986/88), Gray (1987), Leon-Garcia (1989), Papoulis (1965/68) và Parzen (1960/62), và các phân bố như phân bố chuẩn (sai số), Rayleigh, Poisson (chương 16, tr. 427, 442). Phân bố Pearson loại III xuất hiện như tự tích chập của mũ cắt cụt (tr. 439). Barkat trích De Finetti về xác suất chủ quan (mục 1.2.3, tr. 6 đến 7), Chernoff và Tchebycheff cho các cận (tr. 29).||"
            "Bracewell points to sources: Gardner (1986/88), Gray (1987), Leon-Garcia (1989), Papoulis (1965/68) and Parzen (1960/62), and to distributions such as the normal (of errors), Rayleigh and Poisson (chapter 16, pp. 427, 442). The Pearson type III distribution appears as the self-convolution of the truncated exponential (p. 439). Barkat cites De Finetti on subjective probability (section 1.2.3, pp. 6 to 7), and Chernoff and Chebyshev for the bounds (p. 29).⟧</p>",
    case="<p>⟦<b>Tổ hợp hai điện trở nối tiếp và đường truyền tin.</b> Điện trở 100 và 50 ôm với dung sai đều 10 phần trăm cho tổ hợp trung bình {{res_mean}} ôm, độ lệch chuẩn {{res_sd}} ôm ({{res_pct}} phần trăm) so với {{comp_pct}} phần trăm ở mỗi thành phần, phân bố hình thang; ta biết vậy mà không cần tích phân, vì tích chập cộng trung bình và phương sai. Kênh nhị phân 0.6/0.4 làm sai 0.2 cho $P(\\text{nhận }0)$ = {{ch_r0}} và $P(\\text{gửi }0\\mid\\text{nhận }0)$ = {{ch_post}}: nhận được 0 thì 85.7 phần trăm khả năng đúng là 0 đã gửi; đây là bài toán quyết định ở module 21. Chuẩn bị cho các module sau: tổng nhiều nhiễu độc lập gần Gauss (giới hạn trung tâm), và khoảng giữa biến cố ngẫu nhiên là mũ.||"
          "<b>Two resistors in series and a communication link.</b> A 100-ohm and a 50-ohm resistor with uniform 10 percent tolerances give a combination with mean {{res_mean}} ohms, standard deviation {{res_sd}} ohms ({{res_pct}} percent) against {{comp_pct}} percent for each component, and a trapezoidal distribution; we know this without integrating, since convolution adds means and variances. A binary channel 0.6/0.4 with garbling 0.2 gives $P(\\text{receive }0)$ = {{ch_r0}} and $P(\\text{sent }0\\mid\\text{received }0)$ = {{ch_post}}: on receiving a 0 it is 85.7 percent likely that a 0 was sent; this is the decision problem of module 21. A preview of later modules: sums of many independent noises are nearly Gaussian (central limit), and intervals between random events are exponential.⟧</p>",
    practice=[
        "⟦Mở notebook và chạy cell cài đặt.||Open the notebook and run the setup cell.⟧",
        "⟦Bài 1: tính phân bố tổng của ba xúc xắc bằng tích chập (bài tập 6 của Bracewell) và so với đếm trực tiếp.||Task 1: compute the distribution of the total of three dice by convolution (Bracewell's problem 6) and compare with direct counting.⟧",
        "⟦Bài 2: tìm mật độ của $1/R$ khi $R$ đều trên $[90,110]$ bằng định lý cơ bản (bài tập 16) và giải thích vì sao không còn bằng phẳng.||Task 2: find the density of $1/R$ for $R$ uniform on $[90,110]$ with the fundamental theorem (problem 16) and explain why it is no longer flat.⟧",
        "⟦Bài 3: kiểm hàm đặc trưng của nhị thức $[q+pe^{it}]^n$ bằng biến đổi Fourier rời rạc của $\\{q\\ p\\}^{*n}$.||Task 3: check the binomial characteristic function $[q+pe^{it}]^n$ by the discrete Fourier transform of $\\{q\\ p\\}^{*n}$.⟧",
        "⟦Bài 4: mô phỏng số cuộc gọi trong khoảng dài và xác nhận trung bình bằng phương sai (đặc trưng của Poisson).||Task 4: simulate the number of calls in an interval and confirm mean equals variance (a Poisson signature).⟧",
    ],
    pitfalls=[
        "<b>⟦\"Hai biến cố loại trừ nhau thì độc lập.\"||\"Two mutually exclusive events are independent.\"⟧</b><p>⟦Ngược lại: nếu cả hai có xác suất dương thì loại trừ ngăn độc lập; $P(C\\cap D)$ = {{ind_cd}} còn $P(C)P(D)$ = {{ind_cd_prod}} với tổng 2 và tổng 12.||It is the opposite: if both have positive probability, exclusion prevents independence; $P(C\\cap D)$ = {{ind_cd}} while $P(C)P(D)$ = {{ind_cd_prod}} for sum 2 and sum 12.⟧</p>",
        "<b>⟦\"Không tương quan nghĩa là độc lập.\"||\"Uncorrelated means independent.\"⟧</b><p>⟦Nửa đĩa có $\\rho=0$ nhưng phụ thuộc: $P(X>0.7,Y>0.8)$ = {{hd_pj}} khác tích {{hd_pp}} (Barkat, ví dụ 1.18).||The half-disc has $\\rho=0$ but is dependent: $P(X>0.7,Y>0.8)$ = {{hd_pj}} differs from the product {{hd_pp}} (Barkat, example 1.18).⟧</p>",
        "<b>⟦\"Nhiều điện trở cho sai số giảm như $1/\\sqrt n$.\"||\"Many resistors reduce the error like $1/\\sqrt n$.\"⟧</b><p>⟦Chỉ khi sai số độc lập. Khi có độ lệch chung của lô, độ lệch tương đối dừng ở {{bo_corr}} thay vì {{bo_ind}} (Bracewell, bài tập 3).||Only when errors are independent. With a common batch offset the relative deviation stops at {{bo_corr}} instead of {{bo_ind}} (Bracewell, problem 3).⟧</p>",
        "<b>⟦\"Cận Chernoff luôn chặt hơn Tchebycheff.\"||\"The Chernoff bound is always tighter than Chebyshev's.\"⟧</b><p>⟦Với mũ đơn vị, $P(X\\ge3)$: Chernoff {{chern_3}} lỏng hơn Tchebycheff {{cheb_3}}; nhưng ở $P(X\\ge10)$: {{chern_10}} chặt hơn {{cheb_10}}.||For the unit exponential, $P(X\\ge3)$: Chernoff {{chern_3}} is looser than Chebyshev {{cheb_3}}; but at $P(X\\ge10)$: {{chern_10}} is tighter than {{cheb_10}}.⟧</p>",
    ],
    refs=[
        "⟦R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chương 16 (tr. 427 đến 445).||R. N. Bracewell, <i>The Fourier Transform and Its Applications</i>, 3rd ed., McGraw-Hill, 2000, chapter 16 (pp. 427 to 445).⟧",
        "⟦M. Barkat, <i>Signal Detection and Estimation</i>, 2nd ed., Artech House, 2005, chương 1 (tr. 1 đến 73).||M. Barkat, <i>Signal Detection and Estimation</i>, 2nd ed., Artech House, 2005, chapter 1 (pp. 1 to 73).⟧",
        "⟦Tài liệu do các chương trích: Gardner (1988), Gray (1987), Leon-Garcia (1989), Papoulis (1968), Parzen (1960); De Finetti [1] (Barkat).||Works cited by the chapters: Gardner (1988), Gray (1987), Leon-Garcia (1989), Papoulis (1968), Parzen (1960); De Finetti [1] (Barkat).⟧",
    ],
    quiz=[
        dict(q="⟦$P(\\text{tổng}=7)$ khi gieo hai xúc xắc bằng bao nhiêu?||What is $P(\\text{sum}=7)$ when two dice are thrown?⟧",
             opts=["{{d_pa}}", "0.1250", "0.2222", "0.0833"], explain="⟦6 trên 36 = {{d_pa}}; $P(B)$ = {{d_pb}}, $P(\\bar A)$ = {{d_pna}}.||6 in 36 = {{d_pa}}; $P(B)$ = {{d_pb}}, $P(\\bar A)$ = {{d_pna}}.⟧"),
        dict(q="⟦Số từ 5 chữ cái không lặp (26 chữ cái) là bao nhiêu?||How many 5-letter words without repeated letters (26 letters)?⟧",
             opts=["{{cnt_perm}}", "11881376", "65780", "7893660"], explain="⟦$26\\cdot25\\cdot24\\cdot23\\cdot22$ = {{cnt_perm}}; có lặp {{cnt_rep}}.||$26\\cdot25\\cdot24\\cdot23\\cdot22$ = {{cnt_perm}}; with repeats {{cnt_rep}}.⟧"),
        dict(q="⟦$\\binom{14}{6}$ bằng bao nhiêu?||What is $\\binom{14}{6}$?⟧",
             opts=["{{cnt_c146}}", "2002", "8008", "1001"], explain="⟦$14!/(8!6!)$ = {{cnt_c146}}.||$14!/(8!6!)$ = {{cnt_c146}}.⟧"),
        dict(q="⟦Xác suất rút hai bóng trắng ở ví dụ 1.3 (hai bình) bằng bao nhiêu?||What is the probability of two white balls in example 1.3 (two urns)?⟧",
             opts=["{{urn_tree}}", "0.0500", "0.0238", "0.1000"], explain="⟦$\\tfrac1{42}+\\tfrac1{20}$ = {{urn_tree}}, bằng phân số chính xác và mô phỏng.||$\\tfrac1{42}+\\tfrac1{20}$ = {{urn_tree}}, by exact fractions and simulation.⟧"),
        dict(q="⟦Xác suất chọn 2 đỏ, 1 lục, 2 xanh, 1 trắng từ 14 bóng (5, 3, 4, 2) bằng bao nhiêu?||What is the probability of 2 red, 1 green, 2 blue, 1 white from 14 balls (5, 3, 4, 2)?⟧",
             opts=["{{urn_multi}}", "0.0800", "0.2000", "0.0300"], explain="⟦$360/3003$ = {{urn_multi}}; số 0.080 in trong sách không khớp đếm trực tiếp.||$360/3003$ = {{urn_multi}}; the 0.080 printed in the book does not match direct counting.⟧"),
        dict(q="⟦Rút đỏ, trắng, lục có hoàn lại từ hộp 7 trắng, 3 đỏ, 6 lục bằng bao nhiêu?||What is red, white, green with replacement from a box of 7 white, 3 red, 6 green?⟧",
             opts=["{{rw_repl}}", "0.0375", "0.0500", "0.0208"], explain="⟦$\\tfrac3{16}\\cdot\\tfrac7{16}\\cdot\\tfrac68$ = {{rw_repl}}; không hoàn lại {{rw_norepl}}.||$\\tfrac3{16}\\cdot\\tfrac7{16}\\cdot\\tfrac68$ = {{rw_repl}}; without replacement {{rw_norepl}}.⟧"),
        dict(q="⟦Xác suất nhận được 0 trong ví dụ 1.6 (0.6/0.4, sai 0.2) bằng bao nhiêu?||What is the probability of receiving a 0 in example 1.6 (0.6/0.4, garbling 0.2)?⟧",
             opts=["{{ch_r0}}", "0.6000", "0.4800", "0.8000"], explain="⟦$0.8\\cdot0.6+0.2\\cdot0.4$ = {{ch_r0}}.||$0.8\\cdot0.6+0.2\\cdot0.4$ = {{ch_r0}}.⟧"),
        dict(q="⟦$P(\\text{gửi }0\\mid\\text{nhận }0)$ ở cùng ví dụ bằng bao nhiêu?||What is $P(\\text{sent }0\\mid\\text{received }0)$ in the same example?⟧",
             opts=["{{ch_post}}", "0.8000", "0.6000", "0.9231"], explain="⟦Bayes: $0.48/0.56$ = {{ch_post}}.||Bayes: $0.48/0.56$ = {{ch_post}}.⟧"),
        dict(q="⟦$P(\\text{bình B}\\mid\\text{bóng trắng})$ ở ví dụ 1.8 bằng bao nhiêu?||What is $P(\\text{urn B}\\mid\\text{white})$ in example 1.8?⟧",
             opts=["{{urn_pb}}", "0.4000", "0.3333", "0.2217"], explain="⟦$P(\\text{trắng})$ = {{urn_pw}}; $0.1333/0.2217$ = {{urn_pb}}.||$P(\\text{white})$ = {{urn_pw}}; $0.1333/0.2217$ = {{urn_pb}}.⟧"),
        dict(q="⟦$P(4\\le X\\le6)$ với $X$ là tổng hai xúc xắc bằng bao nhiêu?||What is $P(4\\le X\\le6)$ for $X$ the sum of two dice?⟧",
             opts=["{{dice_46}}", "0.2500", "0.5000", "0.4167"], explain="⟦$(3+4+5)/36$ = {{dice_46}}; $P(X\\ge5)$ = {{dice_ge5}}.||$(3+4+5)/36$ = {{dice_46}}; $P(X\\ge5)$ = {{dice_ge5}}.⟧"),
        dict(q="⟦Hằng số $c$ của $f_X=cx$ trên $0<x<3$ bằng bao nhiêu?||What is the constant $c$ of $f_X=cx$ on $0<x<3$?⟧",
             opts=["{{pdf_c}}", "0.3333", "0.1111", "0.5000"], explain="⟦$\\int_0^3cx\\,dx=1$: $c=2/9$ = {{pdf_c}}; $P(1<X<2)$ = {{pdf_p12}}.||$\\int_0^3cx\\,dx=1$: $c=2/9$ = {{pdf_c}}; $P(1<X<2)$ = {{pdf_p12}}.⟧"),
        dict(q="⟦$E[Y]$ của đầu ra bộ chỉnh lưu nửa sóng với $X$ chuẩn bằng bao nhiêu?||What is $E[Y]$ for the half-wave rectifier output with a normal $X$?⟧",
             opts=["{{rect_e}}", "0.5000", "0.3183", "0.7979"], explain="⟦$1/\\sqrt{2\\pi}$ = {{rect_e}}; $P(Y=0)$ = {{rect_p0}}; phương sai {{rect_var}}.||$1/\\sqrt{2\\pi}$ = {{rect_e}}; $P(Y=0)$ = {{rect_p0}}; variance {{rect_var}}.⟧"),
        dict(q="⟦Phương sai của tổng hai xúc xắc bằng bao nhiêu?||What is the variance of the sum of two dice?⟧",
             opts=["{{dice_var}}", "2.9167", "35.000", "7.0000"], explain="⟦Cộng phương sai: $2\\times35/12=35/6$ = {{dice_var}}; trung bình {{dice_e}}.||Variances add: $2\\times35/12=35/6$ = {{dice_var}}; the mean is {{dice_e}}.⟧"),
        dict(q="⟦$E[X^2]$ của mật độ ví dụ 1.12 (1/4 trên $|x|<1$, 1/8 trên $1<|x|<3$) bằng bao nhiêu?||What is $E[X^2]$ of the density in example 1.12 (1/4 on $|x|<1$, 1/8 on $1<|x|<3$)?⟧",
             opts=["{{ex12_var}}", "1.1667", "3.5000", "0.0000"], explain="⟦$7/3$ = {{ex12_var}}; trung bình {{ex12_e}}.||$7/3$ = {{ex12_var}}; the mean is {{ex12_e}}.⟧"),
        dict(q="⟦Mật độ của tổ hợp $100\\Omega+50\\Omega$ (dung sai đều 10%) ở $R=140$ bằng bao nhiêu?||What is the density of the combination $100\\Omega+50\\Omega$ (uniform 10% tolerances) at $R=140$?⟧",
             opts=["{{res_140}}", "0.0500", "0.0100", "0.2500"], explain="⟦Sườn tăng $(R-135)/200$ = {{res_140}}; đỉnh phẳng {{res_flat}} trong 145 đến 155.||The rising slope $(R-135)/200$ = {{res_140}}; the flat top {{res_flat}} between 145 and 155.⟧"),
        dict(q="⟦Độ lệch chuẩn của tổ hợp $100\\Omega+50\\Omega$ bằng bao nhiêu ôm?||What is the standard deviation of the $100\\Omega+50\\Omega$ combination (ohms)?⟧",
             opts=["{{res_sd}}", "5.7735", "10.000", "7.0711"], explain="⟦$\\sqrt{20^2/12+10^2/12}$ = {{res_sd}}, tức {{res_pct}} phần trăm của 150.||$\\sqrt{20^2/12+10^2/12}$ = {{res_sd}}, i.e. {{res_pct}} percent of 150.⟧"),
        dict(q="⟦Xác suất tổng hai lần rút chai tiền bằng 6 đô là bao nhiêu?||What is the probability that two draws from the barrel total 6 dollars?⟧",
             opts=["{{bar_p6}}", "0.2500", "0.1500", "0.6000"], explain="⟦$120/400$ = {{bar_p6}}; tổng 11: {{bar_p11}}.||$120/400$ = {{bar_p6}}; total 11: {{bar_p11}}.⟧"),
        dict(q="⟦Phương sai của tổng hai lần rút chai tiền bằng bao nhiêu?||What is the variance of the total of two draws from the barrel?⟧",
             opts=["{{bar_var2}}", "22.750", "9.0000", "43.000"], explain="⟦Hai lần một lần: $2\\times22.75$ = {{bar_var2}}; trung bình {{bar_mean2}}.||Twice the one-draw value: $2\\times22.75$ = {{bar_var2}}; the mean is {{bar_mean2}}.⟧"),
        dict(q="⟦$f_Z(0.5)$ khi $Z=X+Y$, $X\\sim U[0,1]$, $Y\\sim U[0,2]$ bằng bao nhiêu?||What is $f_Z(0.5)$ for $Z=X+Y$, $X\\sim U[0,1]$, $Y\\sim U[0,2]$?⟧",
             opts=["{{uu_05}}", "0.5000", "0.1250", "1.0000"], explain="⟦$z/(ab)=0.5/2$ = {{uu_05}}; đỉnh phẳng {{uu_15}}; $f_Z(2.5)$ = {{uu_25}}.||$z/(ab)=0.5/2$ = {{uu_05}}; the flat top {{uu_15}}; $f_Z(2.5)$ = {{uu_25}}.⟧"),
        dict(q="⟦$f_U(0.2)$ của tích hai biến đều $(0,1)$ độc lập bằng bao nhiêu?||What is $f_U(0.2)$ for the product of two independent uniform $(0,1)$ variables?⟧",
             opts=["{{prod_f}}", "0.8000", "0.2000", "1.0000"], explain="⟦$-\\ln0.2$ = {{prod_f}}; $E[U]$ = {{prod_e}}.||$-\\ln0.2$ = {{prod_f}}; $E[U]$ = {{prod_e}}.⟧"),
        dict(q="⟦$E[\\max(X,Y)]$ cho hai biến đều $(0,1)$ độc lập bằng bao nhiêu?||What is $E[\\max(X,Y)]$ for two independent uniform $(0,1)$ variables?⟧",
             opts=["{{mx_e}}", "0.5000", "0.7500", "0.3333"], explain="⟦$f_M=2m$: $E$ = {{mx_e}}; $E[\\min]$ = {{mn_e}}.||$f_M=2m$: $E$ = {{mx_e}}; $E[\\min]$ = {{mn_e}}.⟧"),
        dict(q="⟦$P(Y\\le1)$ với $Y=2X^2$, $X$ chuẩn bằng bao nhiêu?||What is $P(Y\\le1)$ for $Y=2X^2$, $X$ standard normal?⟧",
             opts=["{{ft_p}}", "0.6827", "0.3829", "0.7605"], explain="⟦$P(|X|\\le1/\\sqrt2)=\\text{erf}(0.5)$ = {{ft_p}}; $E[Y]$ = {{ft_e}}.||$P(|X|\\le1/\\sqrt2)=\\text{erf}(0.5)$ = {{ft_p}}; $E[Y]$ = {{ft_e}}.⟧"),
        dict(q="⟦Hàm đặc trưng của $\\tfrac12e^{-|x|}$ tại $t=0.5$ bằng bao nhiêu?||What is the characteristic function of $\\tfrac12e^{-|x|}$ at $t=0.5$?⟧",
             opts=["{{cf_lap}}", "0.6667", "0.5000", "0.9000"], explain="⟦$1/(1+t^2)$ = {{cf_lap}}; $\\phi(0.7)$ = {{cf_rel}}.||$1/(1+t^2)$ = {{cf_lap}}; $\\phi(0.7)$ = {{cf_rel}}.⟧"),
        dict(q="⟦$E[X^4]$ của phân bố Laplace $\\tfrac12e^{-|x|}$ bằng bao nhiêu?||What is $E[X^4]$ for the Laplace distribution $\\tfrac12e^{-|x|}$?⟧",
             opts=["{{cf_m4}}", "12", "2", "120"], explain="⟦$4!$ = {{cf_m4}}; $E[X^2]$ = {{cf_m2}}.||$4!$ = {{cf_m4}}; $E[X^2]$ = {{cf_m2}}.⟧"),
        dict(q="⟦Mật độ tại 0 của tổng hai biến Laplace độc lập bằng bao nhiêu?||What is the density at 0 of the sum of two independent Laplace variables?⟧",
             opts=["{{cf_sum0}}", "0.5000", "0.1250", "1.0000"], explain="⟦$\\frac1{2\\pi}\\int(1+t^2)^{-2}dt$ = {{cf_sum0}}.||$\\frac1{2\\pi}\\int(1+t^2)^{-2}dt$ = {{cf_sum0}}.⟧"),
        dict(q="⟦Mật độ tại 0 của tổng 12 biến đều $(-\\tfrac12,\\tfrac12)$ bằng bao nhiêu?||What is the density at 0 of the sum of 12 uniform $(-\\tfrac12,\\tfrac12)$ variables?⟧",
             opts=["{{clt_f0}}", "0.3000", "0.5000", "0.3183"], explain="⟦Gần Gauss chuẩn {{clt_g0}}: {{clt_f0}} (giới hạn trung tâm).||Close to the standard Gaussian {{clt_g0}}: {{clt_f0}} (central limit).⟧"),
        dict(q="⟦Cận Tchebycheff cho $P(|X-1|\\ge2)$ với mũ đơn vị bằng bao nhiêu?||What is the Chebyshev bound for $P(|X-1|\\ge2)$ with the unit exponential?⟧",
             opts=["{{cheb_3}}", "0.0498", "0.5000", "0.4060"], explain="⟦$\\sigma^2/\\varepsilon^2=1/4$ = {{cheb_3}}; giá trị thật {{true_3}}.||$\\sigma^2/\\varepsilon^2=1/4$ = {{cheb_3}}; the true value {{true_3}}.⟧"),
        dict(q="⟦Cận Chernoff cho $P(X\\ge10)$ với mũ đơn vị bằng bao nhiêu?||What is the Chernoff bound for $P(X\\ge10)$ with the unit exponential?⟧",
             opts=["{{chern_10}}", "0.0123", "0.0001", "0.0500"], explain="⟦$t=0.9$: $e^{-9}/0.1$ = {{chern_10}}; Tchebycheff {{cheb_10}}; thật {{true_10}}.||$t=0.9$: $e^{-9}/0.1$ = {{chern_10}}; Chebyshev {{cheb_10}}; true {{true_10}}.⟧"),
        dict(q="⟦Xác suất chính xác $P(|S_n/n-0.3|\\ge0.05)$ với $n=1000$, $p=0.3$ bằng bao nhiêu?||What is the exact probability $P(|S_n/n-0.3|\\ge0.05)$ for $n=1000$, $p=0.3$?⟧",
             opts=["{{lln_exact}}", "0.0840", "0.0500", "0.0100"], explain="⟦{{lln_exact}}, còn cận Tchebycheff {{lln_bound}}.||{{lln_exact}}, while the Chebyshev bound is {{lln_bound}}.⟧"),
        dict(q="⟦Độ lệch tương đối của 10 000 điện trở 1% độc lập nối tiếp bằng bao nhiêu?||What is the relative deviation of 10,000 independent 1% resistors in series?⟧",
             opts=["{{bo_ind}}", "1.0e-04", "5.8e-03", "1.0e-02"], explain="⟦$0.577\\%/100$ = {{bo_ind}}; có độ lệch chung: {{bo_corr}}.||$0.577\\%/100$ = {{bo_ind}}; with a common offset: {{bo_corr}}.⟧"),
        dict(q="⟦Mật độ mũ với $X=2$ tại $x=3$ (từ giới hạn $(1-\\Delta x/X)^N$) bằng bao nhiêu?||What is the exponential density with $X=2$ at $x=3$ (from the limit $(1-\\Delta x/X)^N$)?⟧",
             opts=["{{ex_pdf}}", "0.2231", "0.1500", "0.0743"], explain="⟦$e^{-1.5}/2$ = {{ex_pdf}}.||$e^{-1.5}/2$ = {{ex_pdf}}.⟧"),
        dict(q="⟦Phương sai của khoảng giữa các biến cố khi khoảng trung bình $X=2$ bằng bao nhiêu?||What is the variance of the interval between events when the mean interval is $X=2$?⟧",
             opts=["{{ex_var}}", "2.0000", "1.0000", "8.0000"], explain="⟦$\\sigma^2=X^2$ = {{ex_var}}; trung bình mô phỏng {{ex_mean}}.||$\\sigma^2=X^2$ = {{ex_var}}; the simulated mean {{ex_mean}}.⟧"),
        dict(q="⟦$E*E$ tại $x=2$ ($E=e^{-x}H$) bằng bao nhiêu?||What is $E*E$ at $x=2$ ($E=e^{-x}H$)?⟧",
             opts=["{{gam2}}", "0.1353", "0.5413", "0.3033"], explain="⟦$xe^{-x}=2e^{-2}$ = {{gam2}}.||$xe^{-x}=2e^{-2}$ = {{gam2}}.⟧"),
        dict(q="⟦$[E]^{*5}$ tại $x=4$ bằng bao nhiêu?||What is $[E]^{*5}$ at $x=4$?⟧",
             opts=["{{gam5}}", "0.1465", "0.2500", "0.0733"], explain="⟦$4^4e^{-4}/4!$ = {{gam5}}; trung bình và phương sai {{gam_mean}}.||$4^4e^{-4}/4!$ = {{gam5}}; mean and variance {{gam_mean}}.⟧"),
        dict(q="⟦Xác suất có đúng 2 biến cố trong khoảng $x=3$ (khoảng trung bình 1) bằng bao nhiêu?||What is the probability of exactly 2 events in an interval $x=3$ (mean interval 1)?⟧",
             opts=["{{po_pmf}}", "0.1494", "0.2707", "0.3000"], explain="⟦$3^2e^{-3}/2$ = {{po_pmf}}.||$3^2e^{-3}/2$ = {{po_pmf}}.⟧"),
        dict(q="⟦Xác suất đúng hai biến cố trong 1 µs khi tốc độ 0.1 mỗi µs bằng bao nhiêu?||What is the probability of exactly two events in 1 µs at a rate of 0.1 per µs?⟧",
             opts=["{{p5_val}}", "0.0100", "0.0905", "0.0005"], explain="⟦$e^{-0.1}(0.1)^2/2$ = {{p5_val}}.||$e^{-0.1}(0.1)^2/2$ = {{p5_val}}.⟧"),
        dict(q="⟦Tích chập của Poisson trung bình 2 và 3 tại 5 bằng bao nhiêu?||What is the convolution of Poisson means 2 and 3 at 5?⟧",
             opts=["{{po_add}}", "0.2240", "0.0842", "0.1494"], explain="⟦Bằng $P(5)$ của Poisson trung bình 5: {{po_add}}.||Equal to $P(5)$ of the Poisson with mean 5: {{po_add}}.⟧"),
        dict(q="⟦Với ví dụ 1.15, $P(Y<X)$ bằng bao nhiêu?||In example 1.15, what is $P(Y<X)$?⟧",
             opts=["{{j_pyx}}", "0.8333", "0.1563", "0.5000"], explain="⟦$7/24$ = {{j_pyx}}; $P(X>\\tfrac12)$ = {{j_px}}; điều kiện {{j_cond}}.||$7/24$ = {{j_pyx}}; $P(X>\\tfrac12)$ = {{j_px}}; the conditional {{j_cond}}.⟧"),
        dict(q="⟦$E[X\\mid Y=0.6]$ của ví dụ 1.17 bằng bao nhiêu?||What is $E[X\\mid Y=0.6]$ in example 1.17?⟧",
             opts=["{{c17_e}}", "0.3000", "0.6000", "0.5333"], explain="⟦$2y/3$ = {{c17_e}}; $E[X]$ = {{c17_ex}}; $k$ = {{c17_k}}.||$2y/3$ = {{c17_e}}; $E[X]$ = {{c17_ex}}; $k$ = {{c17_k}}.⟧"),
        dict(q="⟦$E[Y]$ trên nửa đĩa đơn vị đều bằng bao nhiêu?||What is $E[Y]$ on the uniform unit half-disc?⟧",
             opts=["{{hd_ey}}", "0.5000", "0.6366", "0.3183"], explain="⟦$4/3\\pi$ = {{hd_ey}}; $\\rho=0$ nhưng phụ thuộc: {{hd_pj}} so với {{hd_pp}}.||$4/3\\pi$ = {{hd_ey}}; $\\rho=0$ but dependent: {{hd_pj}} against {{hd_pp}}.⟧"),
        dict(q="⟦Phân bố của tổng hai biến độc lập là gì?||What is the distribution of the sum of two independent variables?⟧",
             opts=["⟦Tích chập của hai mật độ||The convolution of the two densities⟧",
                   "⟦Tích của hai mật độ, vì độc lập cho xác suất nhân nhau||The product of the two densities, since independence makes probabilities multiply⟧",
                   "⟦Tổng của hai mật độ chia hai, vì tổng phải chuẩn hóa về diện tích 1||The sum of the two densities divided by two, since the sum must be normalised to area 1⟧",
                   "⟦Mật độ đồng thời lấy tại đường thẳng $x+y=z$ mà không tích phân||The joint density evaluated on the line $x+y=z$ without integrating⟧"],
             explain="⟦Bracewell, tr. 430; Barkat, phương trình 1.148: $P=P_1*P_2$.||Bracewell, p. 430; Barkat, equation 1.148: $P=P_1*P_2$.⟧"),
        dict(q="⟦Hàm đặc trưng của tổng hai biến độc lập bằng gì?||What is the characteristic function of the sum of two independent variables?⟧",
             opts=["⟦Tích các hàm đặc trưng||The product of the characteristic functions⟧",
                   "⟦Tổng các hàm đặc trưng, vì kỳ vọng của tổng là tổng các kỳ vọng||The sum of the characteristic functions, since the expectation of a sum is the sum of expectations⟧",
                   "⟦Tích chập các hàm đặc trưng, vì phép biến đổi giữ nguyên tích chập||The convolution of the characteristic functions, since the transform preserves convolution⟧",
                   "⟦Hàm đặc trưng lớn hơn trong hai hàm, vì chi phối phần đuôi của tổng||The larger of the two characteristic functions, since it dominates the tail of the sum⟧"],
             explain="⟦Bracewell, tr. 435; Barkat, 1.135: $\\phi=\\phi_1\\phi_2$.||Bracewell, p. 435; Barkat, 1.135: $\\phi=\\phi_1\\phi_2$.⟧"),
        dict(q="⟦Khi nào không được dùng tích chập cho tổng hai lần rút?||When must convolution not be used for the sum of two draws?⟧",
             opts=["⟦Khi hai lần rút phụ thuộc nhau||When the two draws depend on each other⟧",
                   "⟦Khi hai mật độ có diện tích khác nhau, vì tích chập nhân các diện tích với nhau||When the two densities have different areas, since convolution multiplies the areas⟧",
                   "⟦Khi các giá trị rời rạc, vì tích chập chỉ định nghĩa cho hàm liên tục||When the values are discrete, since convolution is only defined for continuous functions⟧",
                   "⟦Khi phương sai của một trong hai lần rút vô hạn hoặc không xác định||When the variance of one of the draws is infinite or undefined⟧"],
             explain="⟦Bracewell, tr. 433: cần xét độc lập trước; một tờ 20 đô trong chai làm hai lần rút phụ thuộc (P(40) = {{bar_dep}}).||Bracewell, p. 433: independence must be considered first; a single twenty in the barrel makes the draws dependent (P(40) = {{bar_dep}}).⟧"),
        dict(q="⟦Vì sao Tchebycheff cần ít thông tin hơn Chernoff?||Why does Chebyshev need less information than Chernoff?⟧",
             opts=["⟦Chỉ cần trung bình và phương sai||It needs only the mean and variance⟧",
                   "⟦Vì Tchebycheff áp dụng cho một phía còn Chernoff cần cả hai phía của mật độ||Because Chebyshev applies to one side while Chernoff needs both sides of the density⟧",
                   "⟦Vì Tchebycheff dùng hàm sinh mômen còn Chernoff chỉ dùng hàm đặc trưng||Because Chebyshev uses the moment generating function while Chernoff uses only the characteristic function⟧",
                   "⟦Vì Chernoff chỉ đúng khi phân bố đối xứng quanh trung bình||Because Chernoff holds only when the distribution is symmetric about the mean⟧"],
             explain="⟦Barkat, tr. 29 đến 30: Chernoff cần $E[e^{tX}]$, tức biết thêm về phân bố; Tchebycheff hai phía, Chernoff một phía.||Barkat, pp. 29 to 30: Chernoff needs $E[e^{tX}]$, i.e. more knowledge of the distribution; Chebyshev is two-sided, Chernoff one-sided.⟧"),
        dict(q="⟦Quan hệ giữa độc lập và không tương quan là gì?||What is the relation between independence and uncorrelatedness?⟧",
             opts=["⟦Độc lập kéo theo không tương quan, không ngược lại||Independence implies uncorrelatedness, not conversely⟧",
                   "⟦Hai điều kiện tương đương nhau với mọi biến ngẫu nhiên có phương sai hữu hạn||The two conditions are equivalent for all random variables with finite variance⟧",
                   "⟦Không tương quan kéo theo độc lập, nhưng độc lập không kéo theo không tương quan||Uncorrelatedness implies independence, but independence does not imply uncorrelatedness⟧",
                   "⟦Không có quan hệ nào giữa hai điều kiện, vì một cái nói về mômen, cái kia về phân bố||No relation between the two, since one concerns moments and the other distributions⟧"],
             explain="⟦Barkat, tr. 43: độc lập thì không tương quan, ngược lại không đúng (nửa đĩa: $\\rho=0$ nhưng phụ thuộc).||Barkat, p. 43: independent variables are uncorrelated, the converse is false (half-disc: $\\rho=0$ but dependent).⟧"),
    ],
    nb=[
        ("md", """## 1. ⟦Tập hợp, đếm và Bayes||Sets, counting and Bayes⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Các xác suất trong ví dụ của Barkat (xúc xắc, bình bóng, kênh nhị phân) có đúng khi tính bằng phân số chính xác và bằng mô phỏng độc lập?||Are the probabilities in Barkat's examples (dice, urns, binary channel) correct when computed with exact fractions and by independent simulation?⟧"""),
        ("code", r'''from fractions import Fraction as Fr
from itertools import product, permutations
from math import comb, factorial, perm
from scipy import integrate, special, stats, optimize
trap = getattr(np, "trapezoid", None) or np.trapz
rg = np.random.default_rng(10)
S = list(product(range(1, 7), repeat=2))
A = [s for s in S if sum(s) == 7]; B = [s for s in S if (s[0] + s[1]) % 2 == 1]
pa = Fr(len(A), 36); pb = Fr(len(B), 36); pab = Fr(len([s for s in A if s in B]), 36)
assert pa == Fr(1, 6) and pb == Fr(1, 2) and pab == pa
pmf2 = np.convolve(np.ones(6)/6, np.ones(6)/6)                     # ⟦hai xúc xắc: tích chập||two dice: convolution⟧
assert abs(pmf2[5] - 1/6) < 1e-15 and abs(pmf2.sum() - 1) < 1e-15
report("d_pa", float(pa), ".4f"); report("d_pb", float(pb), ".4f"); report("d_pab", float(pab), ".4f"); report("d_pna", float(1 - pa), ".4f")
report("d_pun", float(pa + pb - pab), ".4f"); report("sub_n", 2**6, "d")
d1 = rg.integers(1, 7, 200000); d2 = rg.integers(1, 7, 200000)
freq = np.mean(d1 + d2 == 7)
assert abs(freq - 1/6) < 0.004
report("d_freq", freq, ".3f")

# ⟦đếm||counting⟧
assert 26**5 == 11881376 and perm(26, 5) == 26*25*24*23*22 == 7893600
assert comb(14, 6) == factorial(14)//(factorial(8)*factorial(6)) == 3003
report("cnt_rep", 26**5, "d"); report("cnt_perm", perm(26, 5), "d"); report("cnt_c146", comb(14, 6), "d")

# ⟦cây, ví dụ 1.3||tree, example 1.3⟧
p2w = Fr(1, 2)*(Fr(2, 7)*Fr(1, 6)) + Fr(1, 2)*(Fr(2, 5)*Fr(1, 4))
N = 400000
which = rg.integers(0, 2, N)
def two_white(u):
    balls = [1, 1, 0, 0, 0, 0, 0] if u == 0 else [1, 1, 0, 0, 0]
    return None
cnt = 0
for u, nb_w, nb_tot in ((0, 2, 7), (1, 2, 5)):
    n_u = int(np.sum(which == u))
    arr = np.array([1]*nb_w + [0]*(nb_tot - nb_w))
    draws = np.argsort(rg.random((n_u, nb_tot)), axis=1)[:, :2]
    cnt += int(np.sum(arr[draws].sum(axis=1) == 2))
assert abs(cnt/N - float(p2w)) < 0.003
report("urn_tree", float(p2w), ".4f")
# ⟦ví dụ 1.4||example 1.4⟧
multi = Fr(comb(5, 2)*comb(3, 1)*comb(4, 2)*comb(2, 1), comb(14, 6))
lab = np.array([0]*5 + [1]*3 + [2]*4 + [3]*2)
Nm = 200000
sel = np.argsort(rg.random((Nm, 14)), axis=1)[:, :6]
counts = np.stack([(lab[sel] == c).sum(axis=1) for c in range(4)], axis=1)
mc = np.mean((counts == [2, 1, 2, 1]).all(axis=1))
assert abs(mc - float(multi)) < 0.003 and multi == Fr(360, 3003)
report("urn_multi", float(multi), ".4f")

# ⟦ví dụ 1.7: hai cách: công thức và liệt kê||example 1.7: formula and enumeration⟧
colors = ["W"]*7 + ["R"]*3 + ["G"]*6
rep = sum(1 for t in product(range(16), repeat=3) if (colors[t[0]], colors[t[1]], colors[t[2]]) == ("R", "W", "G"))
norep = sum(1 for t in permutations(range(16), 3) if (colors[t[0]], colors[t[1]], colors[t[2]]) == ("R", "W", "G"))
assert Fr(rep, 16**3) == Fr(3, 16)*Fr(7, 16)*Fr(6, 16) and Fr(norep, 16*15*14) == Fr(3, 16)*Fr(7, 15)*Fr(6, 14)
report("rw_repl", rep/16**3, ".4f"); report("rw_norepl", norep/(16*15*14), ".4f")

# ⟦kênh nhị phân, ví dụ 1.6||binary channel, example 1.6⟧
p0, p1_, gar = Fr(6, 10), Fr(4, 10), Fr(2, 10)
pr0 = (1 - gar)*p0 + gar*p1_
post = (1 - gar)*p0/pr0
sent = rg.random(500000) < 0.6                                  # ⟦gửi 0 với 0.6||send 0 with 0.6⟧
recv0 = np.where(rg.random(500000) < 0.2, ~sent, sent)
assert abs(np.mean(recv0) - float(pr0)) < 0.004 and abs(np.mean(sent[recv0]) - float(post)) < 0.004
report("ch_r0", float(pr0), ".4f"); report("ch_post", float(post), ".4f")
# ⟦ba bình||three urns⟧
tab = {"A": (5, 6, 2), "B": (3, 3, 4), "C": (6, 2, 1)}
pw = sum(Fr(1, 3)*Fr(v[2], sum(v)) for v in tab.values())
pB = Fr(1, 3)*Fr(4, 10)/pw
urn = rg.integers(0, 3, 400000); names = ["A", "B", "C"]
pw_mc = np.mean([0]*0 or [1]) if False else None
wprob = np.array([Fr(tab[n][2], sum(tab[n])) for n in names], dtype=float)
white = rg.random(400000) < wprob[urn]
assert abs(np.mean(white) - float(pw)) < 0.003 and abs(np.mean(urn[white] == 1) - float(pB)) < 0.005
report("urn_pw", float(pw), ".4f"); report("urn_pb", float(pB), ".4f")

# ⟦độc lập vs loại trừ||independent vs exclusive⟧
Aa = [s for s in S if sum(s) == 7]; Bb = [s for s in S if s[0] == 1]; Cc = [s for s in S if sum(s) == 2]; Dd = [s for s in S if sum(s) == 12]
pAB = Fr(len([s for s in Aa if s in Bb]), 36)
assert pAB == Fr(len(Aa), 36)*Fr(len(Bb), 36)
assert Fr(len([s for s in Cc if s in Dd]), 36) == 0 and Fr(len(Cc), 36)*Fr(len(Dd), 36) == Fr(1, 1296)
report("ind_ab", float(pAB), ".4f"); report("ind_cd", 0.0, ".4f"); report("ind_cd_prod", 1/1296, ".5f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Hai xúc xắc: $P(A)$ = {{d_pa}}, $P(B)$ = {{d_pb}}, $P(A\\cup B)$ = {{d_pun}}; tần suất {{d_freq}}. Đếm: {{cnt_rep}}, {{cnt_perm}}, $\\binom{14}6$ = {{cnt_c146}}. Bình: {{urn_tree}}, {{urn_multi}}, {{rw_repl}} và {{rw_norepl}}. Kênh: {{ch_r0}} và {{ch_post}}; ba bình {{urn_pw}} và {{urn_pb}}. Độc lập: {{ind_ab}}; loại trừ: {{ind_cd}} và {{ind_cd_prod}}.||Two dice: $P(A)$ = {{d_pa}}, $P(B)$ = {{d_pb}}, $P(A\\cup B)$ = {{d_pun}}; frequency {{d_freq}}. Counting: {{cnt_rep}}, {{cnt_perm}}, $\\binom{14}6$ = {{cnt_c146}}. Urns: {{urn_tree}}, {{urn_multi}}, {{rw_repl}} and {{rw_norepl}}. Channel: {{ch_r0}} and {{ch_post}}; three urns {{urn_pw}} and {{urn_pb}}. Independence: {{ind_ab}}; exclusive: {{ind_cd}} and {{ind_cd_prod}}.⟧"""),
        ("md", """## 2. ⟦Biến ngẫu nhiên và mômen||Random variables and moments⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Xác suất, kỳ vọng, phương sai của biến rời rạc, liên tục và hỗn hợp có khớp giữa tích phân, phân số chính xác và mô phỏng?||Do probabilities, expectations and variances of discrete, continuous and mixed variables agree between integration, exact fractions and simulation?⟧"""),
        ("code", r'''# ⟦hai xúc xắc||two dice⟧
xv = np.arange(2, 13)
assert abs(pmf2[2:5].sum() - 1/3) < 1e-15 and abs(pmf2[3:].sum() - 5/6) < 1e-15     # ⟦P(4≤X≤6) = indices 2..4; P(X≥5) = indices 3..||P(4≤X≤6) = indices 2..4; P(X≥5) = indices 3..⟧
dice_ge5 = 1 - pmf2[:3].sum()
assert abs(dice_ge5 - 5/6) < 1e-15
mean2 = np.sum(xv*pmf2); var2 = np.sum(xv**2*pmf2) - mean2**2
assert abs(mean2 - 7) < 1e-12 and abs(var2 - 35/6) < 1e-12
assert abs(var2 - 2*(35/12)) < 1e-12
report("dice_46", pmf2[2:5].sum(), ".4f"); report("dice_ge5", 5/6, ".4f"); report("dice_e", mean2, ".4f"); report("dice_var", var2, ".4f")
report("die_e", np.mean(np.arange(1, 7)), ".1f")

# ⟦ví dụ 1.10||example 1.10⟧
cc = 1/integrate.quad(lambda x: x, 0, 3)[0]
assert abs(cc - 2/9) < 1e-12
p12 = integrate.quad(lambda x: cc*x, 1, 2)[0]
assert abs(p12 - 1/3) < 1e-12 and abs(integrate.quad(lambda x: cc*x, 0, 2)[0] - 4/9) < 1e-12
report("pdf_c", cc, ".4f"); report("pdf_p12", p12, ".4f"); report("pdf_F2", 4/9, ".4f")

# ⟦ví dụ 1.12, 1.13||examples 1.12, 1.13⟧
f12 = lambda x: 0.25 if abs(x) < 1 else (0.125 if abs(x) < 3 else 0.0)
tot = integrate.quad(f12, -3, 3, points=[-1, 1])[0]
E12 = integrate.quad(lambda x: x*f12(x), -3, 3, points=[-1, 1])[0]
V12 = integrate.quad(lambda x: x*x*f12(x), -3, 3, points=[-1, 1])[0]
assert abs(tot - 1) < 1e-12 and abs(E12) < 1e-12 and abs(V12 - 7/3) < 1e-10
# ⟦mô phỏng: chọn miền theo xác suất||simulation: choose a region by probability⟧
u = rg.random(400000)
xs = np.where(u < 0.5, rg.uniform(-1, 1, 400000), np.where(rg.random(400000) < 0.5, rg.uniform(1, 3, 400000), rg.uniform(-3, -1, 400000)))
assert abs(np.mean(xs**2) - 7/3) < 0.02
report("ex12_e", 0.0, ".4f"); report("ex12_var", V12, ".4f")

# ⟦chỉnh lưu nửa sóng, X chuẩn||half-wave rectifier, X standard normal⟧
phi = lambda x: np.exp(-x*x/2)/np.sqrt(2*np.pi)
EY = integrate.quad(lambda x: x*phi(x), 0, np.inf)[0]; EY2 = integrate.quad(lambda x: x*x*phi(x), 0, np.inf)[0]
Xn = rg.standard_normal(1000000); Yr = np.maximum(Xn, 0)
assert abs(EY - 1/np.sqrt(2*np.pi)) < 1e-10 and abs(np.mean(Yr) - EY) < 3e-3 and abs(np.var(Yr) - (0.5 - 1/(2*np.pi))) < 3e-3
assert abs(np.mean(Yr == 0) - 0.5) < 2e-3
report("rect_p0", 0.5, ".4f"); report("rect_e", EY, ".4f"); report("rect_var", EY2 - EY**2, ".4f")'''),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Hai xúc xắc: $P(4\\le X\\le6)$ = {{dice_46}}, $P(X\\ge5)$ = {{dice_ge5}}, trung bình {{dice_e}}, phương sai {{dice_var}}; một xúc xắc {{die_e}}. $c$ = {{pdf_c}}, $P(1<X<2)$ = {{pdf_p12}}, $F(2)$ = {{pdf_F2}}. Ví dụ 1.12: $E$ = {{ex12_e}}, $E[X^2]$ = {{ex12_var}}. Chỉnh lưu: $P(Y=0)$ = {{rect_p0}}, $E[Y]$ = {{rect_e}}, phương sai {{rect_var}}.||Two dice: $P(4\\le X\\le6)$ = {{dice_46}}, $P(X\\ge5)$ = {{dice_ge5}}, mean {{dice_e}}, variance {{dice_var}}; one die {{die_e}}. $c$ = {{pdf_c}}, $P(1<X<2)$ = {{pdf_p12}}, $F(2)$ = {{pdf_F2}}. Example 1.12: $E$ = {{ex12_e}}, $E[X^2]$ = {{ex12_var}}. Rectifier: $P(Y=0)$ = {{rect_p0}}, $E[Y]$ = {{rect_e}}, variance {{rect_var}}.⟧"""),
        ("md", """## 3. ⟦Phân bố của tổng, tích, max, min||Distribution of sum, product, max, min⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Tích chập có cho hình thang điện trở, chai tiền, tổng đồng đều đúng như công thức, và trung bình, phương sai có cộng nhau? Tích, max, min và hàm một biến khớp mô phỏng?||Does convolution give the resistor trapezoid, the barrel of money and the sum of uniforms exactly as the formulas say, and do means and variances add? Do the product, max, min and one-variable transforms match simulation?⟧"""),
        ("code", r'''# ⟦điện trở: lưới mịn||resistors: a fine grid⟧
dr = 0.005
R1 = np.arange(90, 110 + dr/2, dr); R2 = np.arange(45, 55 + dr/2, dr)
P1 = np.ones(len(R1))/20; P2 = np.ones(len(R2))/10
conv = np.convolve(P1, P2)*dr
Rt = R1[0] + R2[0] + np.arange(len(conv))*dr
def analytic(R):
    return np.where((R < 135) | (R > 165), 0.0, np.where(R < 145, (R - 135)/200, np.where(R <= 155, 0.05, (165 - R)/200)))
idx = lambda v: int(round((v - Rt[0])/dr))
assert abs(conv[idx(140)] - analytic(140.0)) < 2e-4 and abs(conv[idx(150)] - 0.05) < 2e-4
area = trap(conv, Rt); mean = trap(Rt*conv, Rt)/area; var = trap((Rt - mean)**2*conv, Rt)/area
assert abs(area - 1) < 1e-3 and abs(mean - 150) < 1e-3 and abs(var - (400/12 + 100/12)) < 5e-2
Rs = rg.uniform(90, 110, 500000) + rg.uniform(45, 55, 500000)
assert abs(np.mean(Rs) - 150) < 0.05 and abs(np.var(Rs) - var) < 0.5
sd = np.sqrt(400/12 + 100/12)
report("res_flat", 0.05, ".2f"); report("res_140", float(analytic(140.0)), ".3f"); report("res_mean", 150, "d")
report("res_var", 500/12, ".3f"); report("res_sd", sd, ".3f"); report("res_pct", 100*sd/150, ".2f"); report("comp_pct", 100*(20/np.sqrt(12))/100, ".2f")
assert abs(100*(10/np.sqrt(12))/50 - 100*(20/np.sqrt(12))/100) < 1e-12

# ⟦chai tiền: Fraction chính xác||the barrel: exact Fractions⟧
p1 = {1: Fr(10, 20), 5: Fr(6, 20), 10: Fr(3, 20), 20: Fr(1, 20)}
p2 = {}
for a, pa_ in p1.items():
    for b, pb_ in p1.items():
        p2[a + b] = p2.get(a + b, 0) + pa_*pb_
book = {2: 100, 6: 120, 10: 36, 11: 60, 15: 36, 20: 9, 21: 20, 25: 12, 30: 6, 40: 1}
assert all(p2[k] == Fr(v, 400) for k, v in book.items()) and set(p2) == set(book)
assert sum(p2.values()) == 1
m1 = sum(k*v for k, v in p1.items()); v1 = sum(k*k*v for k, v in p1.items()) - m1**2
m2 = sum(k*v for k, v in p2.items()); v2 = sum(k*k*v for k, v in p2.items()) - m2**2
assert m2 == 2*m1 and v2 == 2*v1
report("bar_p6", float(p2[6]), ".2f"); report("bar_p11", float(p2[11]), ".2f"); report("bar_sum", float(sum(p2.values())), ".1f")
report("bar_m1", float(m1), ".2f"); report("bar_mean2", float(m2), ".1f"); report("bar_var1", float(v1), ".2f"); report("bar_var2", float(v2), ".1f")
# ⟦phụ thuộc: chỉ một tờ 20 trong 20 tờ (10 tờ 1, 6 tờ 5, 3 tờ 10, 1 tờ 20), không hoàn lại||dependence: a single twenty among 20 bills (10 ones, 6 fives, 3 tens, 1 twenty), without replacement⟧
bills = [1]*10 + [5]*6 + [10]*3 + [20]
ways = sum(1 for i, j in permutations(range(20), 2) if bills[i] + bills[j] == 40)
assert ways == 0
report("bar_dep", 0, "d")

# ⟦tổng đồng đều a = 1, b = 2||sum of uniforms a = 1, b = 2⟧
a_, b_ = 1.0, 2.0; dz = 0.001
fx = np.ones(int(a_/dz))/a_; fy = np.ones(int(b_/dz))/b_
fz = np.convolve(fx, fy)*dz
z = (np.arange(len(fz)) + 1)*dz
val = lambda zz: fz[int(round(zz/dz)) - 1]
form = lambda zz: zz/(a_*b_) if zz < a_ else (1/b_ if zz < b_ else (a_ + b_ - zz)/(a_*b_))
for zz in (0.5, 1.5, 2.5):
    assert abs(val(zz) - form(zz)) < 2e-3
report("uu_05", form(0.5), ".4f"); report("uu_15", form(1.5), ".4f"); report("uu_25", form(2.5), ".4f")

# ⟦tích, max, min của hai biến đều (0,1)||product, max, min of two uniform (0,1)||⟧
fU = lambda u: integrate.quad(lambda x: 1.0/x, u, 1)[0]
assert abs(fU(0.2) - (-np.log(0.2))) < 1e-9
EU = integrate.quad(lambda u: u*(-np.log(u)), 0, 1)[0]
Xu, Yu = rg.random(1000000), rg.random(1000000)
assert abs(EU - 0.25) < 1e-9 and abs(np.mean(Xu*Yu) - 0.25) < 1e-3
EM = integrate.quad(lambda m: m*2*m, 0, 1)[0]; EN = integrate.quad(lambda n: n*2*(1 - n), 0, 1)[0]
assert abs(EM - 2/3) < 1e-9 and abs(EN - 1/3) < 1e-9 and abs(np.mean(np.maximum(Xu, Yu)) - 2/3) < 1e-3 and abs(np.mean(np.minimum(Xu, Yu)) - 1/3) < 1e-3
report("prod_f", -np.log(0.2), ".4f"); report("prod_e", EU, ".2f"); report("mx_e", EM, ".4f"); report("mn_e", EN, ".4f")

# ⟦hàm một biến Y = aX², a = 2||function of one variable Y = aX², a = 2⟧
a2 = 2.0
fY = lambda y: (phi(np.sqrt(y/a2)) + phi(-np.sqrt(y/a2)))/(2*np.sqrt(a2*y))
tot = integrate.quad(fY, 0, np.inf)[0]
Ey = integrate.quad(lambda y: y*fY(y), 0, np.inf)[0]
pY = integrate.quad(fY, 0, 1)[0]
assert abs(tot - 1) < 1e-6 and abs(Ey - 2) < 1e-5 and abs(pY - special.erf(0.5)) < 1e-6
assert abs(np.mean(a2*Xn**2 <= 1) - special.erf(0.5)) < 2e-3
report("ft_e", Ey, ".4f"); report("ft_p", pY, ".4f")'''),
        ("code", r'''fig, ax = plt.subplots(1, 2, figsize=(10, 3.3))
ax[0].plot(Rt, conv, label=("⟦tích chập số||numerical convolution⟧")); ax[0].plot(Rt, analytic(Rt), "--", lw=1, label=("⟦công thức||formula⟧"))
ax[0].set_xlabel("R (Ω)"); ax[0].legend(fontsize=8)
ks_ = sorted(p2); ax[1].stem(ks_, [float(p2[k]) for k in ks_], basefmt=" "); ax[1].set_xlabel(("⟦tổng hai lần rút ($)||total of two draws ($)⟧"))
plt.tight_layout(); plt.show()''', dict(fig="sum_conv", cap="⟦Hình 1. Tích chập hai phân bố đều cho hình thang cho điện trở nối tiếp (trái, số và công thức trùng nhau), và tích chập rời rạc cho chai tiền (phải).||Figure 1. Convolving two uniform distributions gives the trapezoid for series resistors (left, numerical and formula coincide), and a discrete convolution gives the barrel of money (right).⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Điện trở: trung bình {{res_mean}}, độ lệch chuẩn {{res_sd}} ({{res_pct}} phần trăm so với {{comp_pct}}), mật độ tại 140 là {{res_140}}. Chai tiền: {{bar_p6}}, {{bar_p11}}, tổng {{bar_sum}}, trung bình {{bar_mean2}}, phương sai {{bar_var2}}; phụ thuộc: {{bar_dep}}. Tổng đều: {{uu_05}}, {{uu_15}}, {{uu_25}}. Tích $f_U(0.2)$ = {{prod_f}}, $E[U]$ = {{prod_e}}; $E[M]$ = {{mx_e}}, $E[N]$ = {{mn_e}}; $Y=2X^2$: $E$ = {{ft_e}}, $P(Y\\le1)$ = {{ft_p}}.||Resistors: mean {{res_mean}}, standard deviation {{res_sd}} ({{res_pct}} percent against {{comp_pct}}), density at 140 is {{res_140}}. Barrel: {{bar_p6}}, {{bar_p11}}, sum {{bar_sum}}, mean {{bar_mean2}}, variance {{bar_var2}}; dependence: {{bar_dep}}. Sum of uniforms: {{uu_05}}, {{uu_15}}, {{uu_25}}. Product $f_U(0.2)$ = {{prod_f}}, $E[U]$ = {{prod_e}}; $E[M]$ = {{mx_e}}, $E[N]$ = {{mn_e}}; $Y=2X^2$: $E$ = {{ft_e}}, $P(Y\\le1)$ = {{ft_p}}.⟧"""),
        ("md", """## 4. ⟦Hàm đặc trưng, giới hạn trung tâm, các cận||Characteristic function, central limit, bounds⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Hàm đặc trưng có cho mômen và tổng độc lập đúng, mật độ tổng 12 biến đều có gần Gauss, và Tchebycheff, Chernoff, luật số lớn cho cận ra sao so với giá trị thật?||Does the characteristic function give moments and independent sums correctly, is the density of the sum of 12 uniform variables close to Gaussian, and how do Chebyshev, Chernoff and the law of large numbers bound the true values?⟧"""),
        ("code", r'''# ⟦Laplace: φ(t) = 1/(1+t²)||Laplace: φ(t) = 1/(1+t²)⟧
lap = lambda x: 0.5*np.exp(-abs(x))
phi_num = integrate.quad(lambda x: lap(x)*np.cos(0.5*x), -80, 80, points=[0], limit=800)[0]
assert abs(phi_num - 1/(1 + 0.25)) < 1e-8
report("cf_lap", phi_num, ".4f")
# ⟦liên hệ Bracewell φ(t) = F(−t/2π), F(s) = ∫P e^{−i2πxs}||Bracewell relation φ(t) = F(−t/2π)⟧
t7 = 0.7; s7 = -t7/(2*np.pi)
F7 = integrate.quad(lambda x: lap(x)*np.cos(2*np.pi*x*s7), -80, 80, points=[0], limit=800)[0]
assert abs(F7 - 1/(1 + t7**2)) < 1e-8
report("cf_rel", F7, ".4f")
# ⟦mômen từ đạo hàm (tích phân đường qua FFT)||moments from derivatives (a contour integral by FFT)⟧
def derivs(fun, nmax, r=0.3, N=128):
    th = 2*np.pi*np.arange(N)/N
    coef = np.fft.fft(fun(r*np.exp(1j*th)))/N
    return [coef[n]*factorial(n)/r**n for n in range(nmax + 1)]
dv = derivs(lambda t: 1/(1 + t**2), 4)
m2_cf = (-(1j)**2*dv[2]).real*(-1)**0        # E[X^n] = (−i)^n φ^(n)(0)
m2_cf = ((-1j)**2*dv[2]).real; m4_cf = ((-1j)**4*dv[4]).real
m2_q = integrate.quad(lambda x: x**2*lap(x), -80, 80, points=[0], limit=800)[0]
m4_q = integrate.quad(lambda x: x**4*lap(x), -120, 120, points=[0], limit=800)[0]
assert abs(m2_cf - 2) < 1e-8 and abs(m4_cf - 24) < 1e-6 and abs(m2_q - 2) < 1e-6 and abs(m4_q - 24) < 1e-4
report("cf_m2", m2_cf, ".0f"); report("cf_m4", m4_cf, ".0f")
# ⟦tổng hai Laplace: f(0)||sum of two Laplace: f(0)⟧
f0_a = integrate.quad(lambda t: (1/(1 + t*t))**2, -np.inf, np.inf)[0]/(2*np.pi)
f0_b = integrate.quad(lambda u: lap(u)*lap(-u), -60, 60, points=[0], limit=400)[0]
assert abs(f0_a - 0.25) < 1e-9 and abs(f0_b - 0.25) < 1e-9
report("cf_sum0", f0_a, ".2f")
# ⟦tính chất: mũ đơn vị||properties: unit exponential⟧
tg = np.linspace(-50, 50, 200001)
ph_e = 1/(1 - 1j*tg)
herm = np.max(np.abs(ph_e[::-1] - np.conj(ph_e)))
assert abs(1/(1 - 0j) - 1) < 1e-15 and np.max(np.abs(ph_e)) <= 1 + 1e-12 and herm < 1e-12
report("cf_0", 1.0, ".0f"); report("cf_max", np.max(np.abs(ph_e)), ".0f"); report("cf_herm", max(herm, 1e-16), ".0e")

# ⟦giới hạn trung tâm: 12 biến đều (−½, ½), phương sai 1||central limit: 12 uniform (−½, ½), variance 1⟧
du = 0.005; base = np.ones(int(1/du))/1.0
cur = base.copy()
for _ in range(11): cur = np.convolve(cur, base)*du
xx = (np.arange(len(cur)) - (len(cur) - 1)/2)*du
f0_grid = cur[len(cur)//2]
f0_cf = integrate.quad(lambda t: np.sinc(t/(2*np.pi))**12, -60, 60, limit=800)[0]/(2*np.pi)
assert abs(f0_grid - f0_cf) < 2e-3 and abs(f0_cf - 1/np.sqrt(2*np.pi)) < 1e-2
report("clt_f0", f0_cf, ".4f"); report("clt_g0", 1/np.sqrt(2*np.pi), ".4f")

# ⟦Tchebycheff và Chernoff cho mũ đơn vị||Chebyshev and Chernoff for the unit exponential⟧
true_ = lambda e: np.exp(-e)
cheb = lambda e: 1/(e - 1)**2           # ⟦P(X ≥ e) ⊂ P(|X−1| ≥ e−1)||P(X ≥ e) ⊂ P(|X−1| ≥ e−1)⟧
def chern(e):
    r = optimize.minimize_scalar(lambda t: np.exp(-t*e)/(1 - t), bounds=(1e-6, 1 - 1e-6), method="bounded", options={"xatol": 1e-12})
    return r.fun
assert abs(chern(3) - 3*np.exp(-2)) < 1e-6 and abs(chern(10) - np.exp(-9)/0.1) < 1e-6
assert true_(3) < cheb(3) < chern(3) and true_(10) < chern(10) < cheb(10)
report("true_3", true_(3), ".4f"); report("cheb_3", cheb(3), ".4f"); report("chern_3", chern(3), ".4f")
report("true_10", true_(10), ".1e"); report("cheb_10", cheb(10), ".4f"); report("chern_10", chern(10), ".4f")

# ⟦luật số lớn: n = 1000, p = 0.3||law of large numbers: n = 1000, p = 0.3⟧
n_, p_ = 1000, 0.3
k = np.arange(n_ + 1); pm = stats.binom.pmf(k, n_, p_)
ex = pm[np.abs(k/n_ - p_) >= 0.05 - 1e-12].sum()
ex2 = stats.binom.cdf(250, n_, p_) + stats.binom.sf(349, n_, p_)
bound = p_*(1 - p_)/(n_*0.05**2)
assert abs(ex - ex2) < 1e-12 and ex < bound
report("lln_exact", ex, ".4f"); report("lln_bound", bound, ".4f")

# ⟦điện trở chính xác||the precision resistor⟧
n = 10000; trials = 400
sigma = 0.01/np.sqrt(3)
ind_sd = sigma/np.sqrt(n)
sums_ind = (1 + rg.uniform(-0.01, 0.01, (trials, n))).mean(axis=1)
com = rg.uniform(-0.005, 0.005, trials)
sums_corr = (1 + com[:, None] + rg.uniform(-0.01, 0.01, (trials, n))).mean(axis=1)
corr_sd = np.sqrt((0.005/np.sqrt(3))**2 + ind_sd**2)
assert abs(np.std(sums_ind)/ind_sd - 1) < 0.15 and abs(np.std(sums_corr)/corr_sd - 1) < 0.15
report("bo_ind", ind_sd, ".1e"); report("bo_corr", corr_sd, ".1e")'''),
        ("code", r'''es = np.linspace(2, 12, 200)
fig, ax = plt.subplots(figsize=(8, 3.4))
ax.semilogy(es, [true_(e) for e in es], "k", label=("⟦thật||true⟧"))
ax.semilogy(es, [cheb(e) for e in es], "tab:blue", label=("⟦Tchebycheff||Chebyshev⟧"))
ax.semilogy(es, [chern(e) for e in es], "tab:red", label="Chernoff")
ax.set_xlabel("ε"); ax.set_ylabel("P(X ≥ ε)"); ax.legend(fontsize=8); plt.tight_layout(); plt.show()''', dict(fig="bounds", cap="⟦Hình 2. Cận trên của P(X ≥ ε) cho phân bố mũ đơn vị: Tchebycheff (xanh) giảm như 1/ε², còn Chernoff (đỏ) giảm như mũ và đuổi theo giá trị thật (đen); ở ε nhỏ (khoảng 3) Chernoff lỏng hơn.||Figure 2. Upper bounds on P(X ≥ ε) for the unit exponential: Chebyshev (blue) falls like 1/ε² while Chernoff (red) falls exponentially and tracks the true value (black); at small ε (about 3) Chernoff is looser.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Laplace: $\\phi(0.5)$ = {{cf_lap}}, $\\phi(0.7)$ theo Bracewell {{cf_rel}}, $E[X^2]$ = {{cf_m2}}, $E[X^4]$ = {{cf_m4}}, mật độ tổng tại 0 {{cf_sum0}}. Mũ đơn vị: $\\phi(0)$ = {{cf_0}}, $\\max|\\phi|$ = {{cf_max}}, lệch Hermite {{cf_herm}}. Tổng 12 biến đều: {{clt_f0}} so với {{clt_g0}}. Cận: $P(X\\ge3)$ thật {{true_3}}, Tchebycheff {{cheb_3}}, Chernoff {{chern_3}}; $P(X\\ge10)$ thật {{true_10}}, {{cheb_10}}, {{chern_10}}. Luật số lớn: chính xác {{lln_exact}}, cận {{lln_bound}}. Điện trở chính xác: {{bo_ind}} và {{bo_corr}}.||Laplace: $\\phi(0.5)$ = {{cf_lap}}, $\\phi(0.7)$ by Bracewell {{cf_rel}}, $E[X^2]$ = {{cf_m2}}, $E[X^4]$ = {{cf_m4}}, sum density at 0 {{cf_sum0}}. Unit exponential: $\\phi(0)$ = {{cf_0}}, $\\max|\\phi|$ = {{cf_max}}, Hermitian deviation {{cf_herm}}. Sum of 12 uniforms: {{clt_f0}} against {{clt_g0}}. Bounds: $P(X\\ge3)$ true {{true_3}}, Chebyshev {{cheb_3}}, Chernoff {{chern_3}}; $P(X\\ge10)$ true {{true_10}}, {{cheb_10}}, {{chern_10}}. Law of large numbers: exact {{lln_exact}}, bound {{lln_bound}}. Precision resistor: {{bo_ind}} and {{bo_corr}}.⟧"""),
        ("md", """## 5. ⟦Mũ, gamma, Poisson và hai chiều||Exponential, gamma, Poisson and two dimensions⟧
🎯 **⟦Phương pháp này trả lời câu hỏi gì?||What question does this method answer?⟧** ⟦Khoảng giữa các biến cố ngẫu nhiên có phân bố mũ, tự tích chập cho gamma, đếm cho Poisson, Poisson cộng, nhị thức gần Gauss? Và các ví dụ hai chiều (1.15 đến 1.18) đúng ra sao?||Do intervals between random events follow an exponential distribution, does self-convolution give gamma, counting Poisson, do Poissons add, is the binomial close to Gaussian? And how do the two-dimensional examples (1.15 to 1.18) come out?⟧"""),
        ("code", r'''# ⟦giới hạn (1 − Δx/X)^N / X||the limit (1 − Δx/X)^N / X⟧
Xm, x0 = 2.0, 3.0
Nlim = 10**7
lim_val = (1 - (x0/Nlim)/Xm)**Nlim/Xm
assert abs(lim_val - np.exp(-x0/Xm)/Xm) < 1e-6
report("ex_pdf", lim_val, ".4f")
# ⟦mô phỏng: khoảng giữa các biến cố của quá trình Poisson với tốc độ 1/X||simulation: intervals of a Poisson process of rate 1/X⟧
arr = np.cumsum(rg.exponential(Xm, 1000000)); iv = np.diff(arr)
qm = integrate.quad(lambda x: x*np.exp(-x/Xm)/Xm, 0, np.inf)[0]; qv = integrate.quad(lambda x: x*x*np.exp(-x/Xm)/Xm, 0, np.inf)[0] - qm**2
assert abs(np.mean(iv) - qm) < 0.01 and abs(np.var(iv) - qv) < 0.05 and abs(qm - 2) < 1e-9 and abs(qv - 4) < 1e-9
report("ex_mean", np.mean(iv), ".2f"); report("ex_var", np.var(iv), ".1f")

# ⟦gamma: E*E, [E]^{*5}||gamma: E*E, [E]^{*5}⟧
from scipy.signal import fftconvolve
dxg = 0.002; xg = np.arange(0, 40, dxg); E1 = np.exp(-xg)
cur = E1.copy(); conv_pows = {1: E1.copy()}
for n_ in range(2, 6):
    cur = fftconvolve(cur, E1)[:len(xg)]*dxg
    conv_pows[n_] = cur.copy()
g2 = conv_pows[2][int(round(2/dxg))]; g5 = conv_pows[5][int(round(4/dxg))]
assert abs(g2 - 2*np.exp(-2)) < 2e-3 and abs(g5 - 4**4*np.exp(-4)/24) < 2e-3
assert abs(g5 - stats.gamma.pdf(4, a=5)) < 2e-3
ar5 = trap(conv_pows[5], xg); mean5 = trap(xg*conv_pows[5], xg)/ar5; var5 = trap(xg**2*conv_pows[5], xg)/ar5 - mean5**2
assert abs(mean5 - 5) < 5e-2 and abs(var5 - 5) < 0.1
report("gam2", 2*np.exp(-2), ".4f"); report("gam5", 4**4*np.exp(-4)/24, ".4f"); report("gam_mean", 5, "d"); report("gam_var", 5, "d")
# ⟦Stirling, n = 100||Stirling, n = 100⟧
nS = 100
gam = stats.gamma.pdf(nS, a=nS); gauss = 1/np.sqrt(2*np.pi*nS)
gam_log = np.exp((nS - 1)*np.log(nS) - nS - special.gammaln(nS))
assert abs(gam - gam_log) < 1e-12
report("st_ratio", gam/gauss, ".4f")

# ⟦Poisson từ khoảng||Poisson from intervals⟧
xn, nn = 3.0, 2
po_int = integrate.quad(lambda xp: xp**(nn - 1)/factorial(nn - 1)*np.exp(-xp)*np.exp(-(xn - xp)), 0, xn)[0]
po_form = xn**nn/factorial(nn)*np.exp(-xn)
assert abs(po_int - po_form) < 1e-10 and abs(po_int - stats.poisson.pmf(nn, xn)) < 1e-12
cnts = np.searchsorted(arr, 3.0*Xm*0 + 0)*0        # ⟦(giữ chỗ)||(placeholder)⟧
tr = np.cumsum(rg.exponential(1.0, (200000, 12)), axis=1)
mc = np.mean((tr < 3.0).sum(axis=1) == 2)
assert abs(mc - po_form) < 3e-3
report("po_pmf", po_form, ".4f")
p5 = stats.poisson.pmf(2, 0.1); assert abs(p5 - np.exp(-0.1)*0.01/2) < 1e-15
report("p5_val", p5, ".4f")
ks5 = np.arange(0, 60)
po_sum = stats.poisson.pmf(ks5, 4).sum(); assert abs(po_sum - 1) < 1e-12 and abs(stats.poisson.pmf(3, 4) - stats.poisson.pmf(4, 4)) < 1e-15
report("po_sum", po_sum, ".0f"); report("po_eq", stats.poisson.pmf(4, 4), ".4f")
pa2 = stats.poisson.pmf(np.arange(0, 40), 2); pb3 = stats.poisson.pmf(np.arange(0, 40), 3)
conv_po = np.convolve(pa2, pb3)[5]
assert abs(conv_po - stats.poisson.pmf(5, 5)) < 1e-12
report("po_add", conv_po, ".4f")
bn = np.array([1.0]);
for _ in range(20): bn = np.convolve(bn, [0.5, 0.5])
assert abs(bn[10] - comb(20, 10)/2**20) < 1e-15
report("bin_10", bn[10], ".4f"); report("bin_g", 1/np.sqrt(2*np.pi*20*0.25), ".4f")

# ⟦hai chiều: ví dụ 1.15||two dimensions: example 1.15⟧
fxy = lambda y, x: x*x + x*y/3
J = integrate.dblquad(fxy, 0, 1, 0, 2)[0]
PX = integrate.quad(lambda x: integrate.quad(lambda y: fxy(y, x), 0, 2)[0], 0.5, 1)[0]
PYX = integrate.dblquad(fxy, 0, 1, 0, lambda x: x)[0]
PC = integrate.dblquad(fxy, 0, 0.5, 0, 0.5)[0]/integrate.dblquad(fxy, 0, 0.5, 0, 2)[0]
assert abs(J - 1) < 1e-9 and abs(PX - 5/6) < 1e-9 and abs(PYX - 7/24) < 1e-9 and abs(PC - 5/32) < 1e-9
xs_ = rg.random(2000000); ys_ = rg.random(2000000)*2                       # ⟦mô phỏng loại bỏ: mật độ ≤ 1 + 2/3||rejection sampling: density ≤ 1 + 2/3⟧
acc = rg.random(2000000)*(5/3) < xs_**2 + xs_*ys_/3
X_, Y_ = xs_[acc], ys_[acc]
assert abs(np.mean(X_ > 0.5) - 5/6) < 4e-3 and abs(np.mean(Y_ < X_) - 7/24) < 4e-3
report("j_int", J, ".1f"); report("j_px", PX, ".4f"); report("j_pyx", PYX, ".4f"); report("j_cond", PC, ".4f")
# ⟦bảng ví dụ 1.16||table of example 1.16⟧
tabl = {(1, 0): Fr(1, 4), (2, 0): Fr(1, 4), (1, 1): Fr(0), (2, 1): Fr(1, 8), (1, 2): Fr(1, 4), (2, 2): Fr(1, 8)}
assert sum(tabl.values()) == 1
PX1 = sum(v for (x, y), v in tabl.items() if x == 1); PY2 = sum(v for (x, y), v in tabl.items() if y == 2)
assert PX1 == Fr(1, 2) and PY2 == Fr(3, 8) and tabl[(1, 2)] != PX1*PY2
report("j_dep", float(tabl[(1, 2)]), ".2f"); report("j_ind", float(PX1*PY2), ".4f")
# ⟦ví dụ 1.17||example 1.17⟧
kk = 1/integrate.dblquad(lambda x, y: y*x, 0, 1, 0, lambda y: y)[0]
assert abs(kk - 8) < 1e-9
fYc = lambda y: 4*y**3
Exy = lambda y: integrate.quad(lambda x: x*8*x*y/fYc(y), 0, y)[0]
assert abs(Exy(0.6) - 0.4) < 1e-9
EX_tower = integrate.quad(lambda y: Exy(y)*fYc(y), 0, 1)[0]
EX_dir = integrate.dblquad(lambda x, y: x*8*x*y, 0, 1, 0, lambda y: y)[0]
assert abs(EX_tower - 8/15) < 1e-9 and abs(EX_dir - 8/15) < 1e-9
report("c17_k", kk, ".0f"); report("c17_e", Exy(0.6), ".2f"); report("c17_ex", EX_dir, ".4f")
# ⟦nửa đĩa||the half-disc⟧
hd = lambda y, x: 2/np.pi
EYh = integrate.dblquad(lambda x, y: y*2/np.pi, 0, 1, lambda y: -np.sqrt(1 - y*y), lambda y: np.sqrt(1 - y*y))[0]
EXYh = integrate.dblquad(lambda x, y: x*y*2/np.pi, 0, 1, lambda y: -np.sqrt(1 - y*y), lambda y: np.sqrt(1 - y*y))[0]
assert abs(EYh - 4/(3*np.pi)) < 1e-9 and abs(EXYh) < 1e-9
pj = integrate.dblquad(lambda y, x: 2/np.pi, 0.7, 1, 0.8, lambda x: np.sqrt(max(1 - x*x, 0)))[0] if False else 0.0
# ⟦P(X > 0.7, Y > 0.8) = 0 vì 0.7² + 0.8² = 1.13 > 1||P(X > 0.7, Y > 0.8) = 0 since 0.7² + 0.8² = 1.13 > 1⟧
assert 0.7**2 + 0.8**2 > 1
px7 = integrate.dblquad(lambda y, x: 2/np.pi, 0.7, 1, 0, lambda x: np.sqrt(1 - x*x))[0]
py8 = integrate.dblquad(lambda x, y: 2/np.pi, 0.8, 1, lambda y: -np.sqrt(1 - y*y), lambda y: np.sqrt(1 - y*y))[0]
assert px7*py8 > 0
ang = rg.random(2000000)*np.pi; rad = np.sqrt(rg.random(2000000))
Xh, Yh = rad*np.cos(ang), rad*np.sin(ang)
assert abs(np.mean((Xh > 0.7) & (Yh > 0.8))) < 1e-9 and abs(np.mean(Yh) - EYh) < 2e-3 and abs(np.corrcoef(Xh, Yh)[0, 1]) < 3e-3
report("hd_ey", EYh, ".4f"); report("hd_pj", 0.0, ".4f"); report("hd_pp", px7*py8, ".4f")'''),
        ("code", r'''fig, ax = plt.subplots(figsize=(8, 3.4))
for n_, c in ((1, "tab:blue"), (2, "tab:orange"), (5, "tab:green")):
    ax.plot(xg, conv_pows[n_], color=c, label=f"[E]^{{*{n_}}}")
ax.set_xlim(0, 15); ax.set_xlabel("x"); ax.legend(fontsize=8); plt.tight_layout(); plt.show()''', dict(fig="gamma_clt", cap="⟦Hình 3. Tự tích chập của phân bố mũ cắt cụt E: E (xanh), E*E (cam), [E]*5 (xanh lá) dịch sang phải, hạ thấp và tròn dần về dạng Gauss.||Figure 3. Self-convolutions of the truncated exponential E: E (blue), E*E (orange), [E]*5 (green) shift right, flatten and round toward a Gaussian.⟧")),
        ("md", """#### 📤 ⟦Đầu ra thật||Real output⟧
⟦Mũ $X=2$: mật độ giới hạn tại 3 là {{ex_pdf}}, trung bình {{ex_mean}}, phương sai {{ex_var}}. Gamma: {{gam2}} và {{gam5}}, trung bình và phương sai {{gam_mean}}; Stirling tại 100 cho tỉ số {{st_ratio}}. Poisson: {{po_pmf}}, {{p5_val}}, tổng {{po_sum}}, $P(3)=P(4)$ = {{po_eq}}, cộng {{po_add}}; nhị thức {{bin_10}} so với {{bin_g}}. Ví dụ 1.15: {{j_int}}, {{j_px}}, {{j_pyx}}, {{j_cond}}. Ví dụ 1.16: {{j_dep}} và {{j_ind}}. Ví dụ 1.17: $k$ = {{c17_k}}, {{c17_e}}, {{c17_ex}}. Nửa đĩa: $E[Y]$ = {{hd_ey}}; {{hd_pj}} so với {{hd_pp}}.||Exponential $X=2$: the limiting density at 3 is {{ex_pdf}}, mean {{ex_mean}}, variance {{ex_var}}. Gamma: {{gam2}} and {{gam5}}, mean and variance {{gam_mean}}; Stirling at 100 gives ratio {{st_ratio}}. Poisson: {{po_pmf}}, {{p5_val}}, sum {{po_sum}}, $P(3)=P(4)$ = {{po_eq}}, adds to {{po_add}}; binomial {{bin_10}} against {{bin_g}}. Example 1.15: {{j_int}}, {{j_px}}, {{j_pyx}}, {{j_cond}}. Example 1.16: {{j_dep}} and {{j_ind}}. Example 1.17: $k$ = {{c17_k}}, {{c17_e}}, {{c17_ex}}. Half-disc: $E[Y]$ = {{hd_ey}}; {{hd_pj}} against {{hd_pp}}.⟧"""),
    ],
)
