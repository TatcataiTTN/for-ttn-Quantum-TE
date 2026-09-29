import numpy as np

def manual_conv(a, b):
    a=np.asarray(a,float); b=np.asarray(b,float); n=len(a)+len(b)-1
    out=np.zeros(n)
    for k in range(n):
        s=0.0
        for i in range(len(a)):
            j=k-i
            if 0<=j<len(b): s+=a[i]*b[j]
        out[k]=s
    return out

# 1(a)-(e),(j)-(q): discrete serial products, cross-check convolve vs manual
cases = {
 "a": ([6,9,17,20,10,1],[3,8,11]),
 "b": ([1,1,1,1,1],[1,1,1,1]),
 "j": ([1,1,0,0,1,0,1],[1,1,0,0,1,0,1]),
 "k": ([1,1,0,0,1,0,1],[1,0,1,0,0,1,1]),
 "n": ([1,3,1],[1,2,2]),
 "q": ([1,8,1],[1,2,2]),
}
ok_all = True
for k,(a,b) in cases.items():
    r1=np.convolve(a,b); r2=manual_conv(a,b)
    ok = np.allclose(r1,r2); ok_all &= ok
    print("1"+k, list(r1.astype(int)), ok)

# 1(i): triple self-convolution {11}*{11}*{11}
r1 = np.convolve(np.convolve([1,1],[1,1]),[1,1])
r2 = manual_conv(manual_conv([1,1],[1,1]),[1,1])
print("1i", list(r1.astype(int)), np.allclose(r1,r2))
print("1i vs Pascal row3 (1,3,3,1):", list(r1.astype(int))==[1,3,3,1])

# 1(o),(p): serial multiplication via convolution+carry == real multiplication
def mult_via_conv(A,B):
    c = np.convolve(A[::-1],B[::-1])[::-1][::-1]  # digits low->high after align
    # simpler: use convolve on digit arrays low-to-high then carry
    return None
def digits_low(n):
    return [int(d) for d in str(n)][::-1]
def mult_conv(n1,n2):
    a=digits_low(n1); b=digits_low(n2)
    c=np.convolve(a,b)
    carry=0; out=[]
    for v in c:
        v=int(v)+carry; out.append(v%10); carry=v//10
    while carry: out.append(carry%10); carry//=10
    return int("".join(str(d) for d in out[::-1]))
print("1o 131*122:", mult_conv(131,122), "==", 131*122, mult_conv(131,122)==131*122)
print("1p 10301*10202:", mult_conv(10301,10202), "==", 10301*10202, mult_conv(10301,10202)==10301*10202)

# Problem 3,4,5: commutative, associative, distributive (continuous, via discrete approx on random functions, 2 methods: direct conv vs FFT-based)
dx=0.01; xg=np.arange(-10,10,dx)
rng=np.random.default_rng(2)
f=np.exp(-0.3*xg**2)*np.cos(1.7*xg); g=np.exp(-0.2*(xg-0.5)**2); h=np.exp(-0.4*(xg+1)**2)*np.sin(xg)
def conv_direct(f,g,dx): return np.convolve(f,g,mode="same")*dx
def conv_fft(f,g,dx):
    n=len(f)+len(g)-1
    F=np.fft.fft(f,n); G=np.fft.fft(g,n)
    full=np.fft.ifft(F*G).real*dx
    start=(len(g)-1)//2
    return full[start:start+len(f)]
fg_d=conv_direct(f,g,dx); fg_f=conv_fft(f,g,dx)
print("P3 direct vs fft convolve max diff:", np.max(np.abs(fg_d-fg_f)))
gf_d=conv_direct(g,f,dx)
print("P3 commutative f*g vs g*f maxdiff:", np.max(np.abs(fg_d-gf_d)))

fg=conv_direct(f,g,dx); fg_h=conv_direct(fg,h,dx)
gh=conv_direct(g,h,dx); f_gh=conv_direct(f,gh,dx)
print("P4 associative (f*g)*h vs f*(g*h) maxdiff:", np.max(np.abs(fg_h-f_gh)))

f_gplush = conv_direct(f, g+h, dx)
fg_plus_fh = conv_direct(f,g,dx)+conv_direct(f,h,dx)
print("P5 distributive maxdiff:", np.max(np.abs(f_gplush-fg_plus_fh)))

# Problem 6: f=g*h; self-convolutions of f,g,h related same way (f*f = (g*g)*(h*h))  [also problem 7 says this directly]
ff = conv_direct(fg,fg,dx)
gg = conv_direct(g,g,dx); hh=conv_direct(h,h,dx)
gg_hh = conv_direct(gg,hh,dx)
print("P7 f*f vs (g*g)*(h*h) maxdiff:", np.max(np.abs(ff-gg_hh)))

# Problem 8: a(f*g) = (af)*g = f*(ag)
a=2.7
lhs=a*conv_direct(f,g,dx); m1=conv_direct(a*f,g,dx); m2=conv_direct(f,a*g,dx)
print("P8 maxdiff:", max(np.max(np.abs(lhs-m1)), np.max(np.abs(lhs-m2))))

# Problem 9: autocorrelation is hermitian C(-u)=C*(u); real f -> C even
def autocorr(f,dx):
    n=len(f)
    C = np.correlate(f,f,mode="full")*dx
    return C
Cr = autocorr(f,dx)
mid=len(Cr)//2
print("P9 real f -> autocorr even, maxdiff:", np.max(np.abs(Cr - Cr[::-1])))
# complex case: use analytic-signal-like complex f2 = f + i*g
f2 = f + 1j*g
C2 = np.correlate(f2, f2, mode="full")*dx  # note: numpy correlate conjugates second arg
Cm = np.correlate(f2.conj(), f2.conj(), mode="full")*dx
print("P9 hermitian C(-u)=C*(u) maxdiff:", np.max(np.abs(C2 - np.conj(C2[::-1]))))

# Problem 13 (Parseval central-value identity): ∫f(x)²dx = central value of f⋆f (autocorrelation at 0)
lhs13 = np.trapezoid(f**2, xg)
Cr2 = np.correlate(f,f,mode="full")*dx
rhs13 = Cr2[len(Cr2)//2]
print("P13:", lhs13, rhs13, abs(lhs13-rhs13))

# Problem 21: self-convolution of sinc(x+2)+sinc(x-2)
xg2 = np.arange(-30,30,0.01)
fsinc = np.sinc(xg2+2) + np.sinc(xg2-2)
conv21 = conv_direct(fsinc, fsinc, 0.01)
# expected: convolution of sum of two shifted sincs -> triangle-ish combos; check via FFT-domain: FT(sinc)=Pi, so FT(f)=2Pi(s)cos(4 pi s); FT(conv21)=FT(f)^2
import numpy.fft as fft
