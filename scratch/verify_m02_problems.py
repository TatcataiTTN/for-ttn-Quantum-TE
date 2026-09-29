import numpy as np
from scipy import integrate

# P2: |F(s)|^2 even for real f
rng = np.random.default_rng(0)
xg = np.linspace(-30, 30, 20000)
f = np.exp(-0.3*xg**2) + 0.4*np.sin(2*xg)*np.exp(-0.1*xg**2)  # real, neither even nor odd
def Fnum(s):
    re = np.trapezoid(f*np.cos(2*np.pi*xg*s), xg)
    im = np.trapezoid(-f*np.sin(2*np.pi*xg*s), xg)
    return re+1j*im
for s in (0.3, 0.7, 1.3):
    a, b = abs(Fnum(s))**2, abs(Fnum(-s))**2
    print("P2", s, a, b, abs(a-b))

# P4: periodic function violates absolute integrability -> integral grows unboundedly
for Nper in (10, 100, 1000):
    L = Nper*2*np.pi
    xs = np.linspace(0, L, 200000)
    I = np.trapezoid(np.abs(np.cos(xs)), xs)
    print("P4", Nper, I, I/Nper)  # should approach 4 per period (int_0^2pi |cos| = 4)

# P5: cos(x) integral of |f| over symmetric growing domain diverges; exp(-a|x|)cos(x) converges
for a in (0.1, 0.5, 1.0):
    val = integrate.quad(lambda x: np.exp(-a*abs(x))*abs(np.cos(x)), -200, 200, limit=500)[0]
    bound = 2/a
    print("P5", a, val, bound, val <= bound)

# P6: odd/even parts of H(x)
H = lambda x: np.where(x>0,1.0,np.where(x<0,0.0,0.5))
xt = np.array([-3,-1,-0.001,0.001,1,3])
e = (H(xt)+H(-xt))/2
o = (H(xt)-H(-xt))/2
print("P6 H even part", e)   # expect 0.5 everywhere
print("P6 H odd part", o)    # expect 0.5*sgn(x)

Ecx = lambda x: np.exp(x)
ee = (Ecx(xt)+Ecx(-xt))/2  # cosh
oo = (Ecx(xt)-Ecx(-xt))/2  # sinh
print("P6 e^x even=cosh?", np.allclose(ee, np.cosh(xt)))
print("P6 e^x odd=sinh?", np.allclose(oo, np.sinh(xt)))

caus = lambda x: np.exp(-x)*(x>0)
ec = (caus(xt)+caus(-xt))/2
oc = (caus(xt)-caus(-xt))/2
print("P6 causal even", ec, "expect 0.5*e^-|x|", 0.5*np.exp(-np.abs(xt)))
print("P6 causal odd", oc, "expect 0.5*sgn(x)*e^-|x|", 0.5*np.sign(xt)*np.exp(-np.abs(xt)))

# P8: even(f*g) = even(f)*even(g) + odd(f)*odd(g)
rng = np.random.default_rng(1)
xg2 = np.linspace(-5,5,4001)
f1 = np.sin(1.3*xg2) + 0.5*np.cos(0.7*xg2) + 0.2*xg2
g1 = np.exp(-0.2*xg2**2)*xg2 + np.cos(2*xg2)
def parts(fun, x):
    return (fun(x)+fun(-x))/2, (fun(x)-fun(-x))/2
def interp(vals, x):
    return np.interp(x, xg2, vals)
ef = (f1 + f1[::-1])/2; of = (f1 - f1[::-1])/2
eg = (g1 + g1[::-1])/2; og = (g1 - g1[::-1])/2
prod = f1*g1
eprod = (prod + prod[::-1])/2
rhs = ef*eg + of*og
print("P8 max err", np.max(np.abs(eprod-rhs)))

# P11: odd part of log|x| -- is it constant? log|x| is EVEN (log|x|=log|-x|), so its odd part is 0 (a constant, namely 0)
xt2 = np.array([1,2,5,10,0.5])
lg = np.log(np.abs(xt2))
oddlg = (lg - np.log(np.abs(-xt2)))/2
print("P11 odd part of log|x| (should be 0)", oddlg)

# P12: composition parity rules
odd_fn = lambda x: np.sin(x) + x**3
even_fn = lambda x: np.cos(x) + x**2
xt3 = np.linspace(-4,4,101)
def is_odd(vals):
    return np.allclose(vals, -vals[::-1], atol=1e-9)
def is_even(vals):
    return np.allclose(vals, vals[::-1], atol=1e-9)
oo_ = odd_fn(odd_fn(xt3)); print("P12 odd(odd) is odd:", is_odd(oo_))
oe_ = odd_fn(even_fn(xt3)); print("P12 odd(even) is even:", is_even(oe_))
eo_ = even_fn(odd_fn(xt3)); print("P12 even(odd) is even:", is_even(eo_))
ee_ = even_fn(even_fn(xt3)); print("P12 even(even) is even:", is_even(ee_))

# P13: FT of real odd function is imaginary and odd
fodd = lambda x: x*np.exp(-x**2)
def Fo(s):
    xg3 = np.linspace(-15,15,30000)
    re = np.trapezoid(fodd(xg3)*np.cos(2*np.pi*xg3*s), xg3)
    im = np.trapezoid(-fodd(xg3)*np.sin(2*np.pi*xg3*s), xg3)
    return re+1j*im
for s in (0.2,0.6,1.0):
    Fp, Fm = Fo(s), Fo(-s)
    print("P13", s, "Re~0:", abs(Fp.real), "imag odd err:", abs(Fp.imag+Fm.imag))

# P16: sum of squared integrals of odd+even parts invariant under shift
def energy_split(fun, a, xg4):
    fx = fun(xg4-a)
    e = (fx+fx[::-1])/2; o=(fx-fx[::-1])/2
    return np.trapezoid(e**2,xg4), np.trapezoid(o**2,xg4)
xg4 = np.linspace(-20,20,40001)
base = lambda x: np.exp(-x**2)
for a in (0,0.5,1.5,3.0):
    Ie, Io = energy_split(base, a, xg4)
    print("P16 shift", a, "sum", Ie+Io)
