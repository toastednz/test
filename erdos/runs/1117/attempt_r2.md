STATUS: BLOCKED

## Result

I did not resolve Question 2. For canonical products built from centered regular polygonal zero shells, I proved several exact obstructions to the natural shell-dominance strategy: factorwise phase alignment yields only the fixed gcd of all shell orders; a fixed nonmonomial polynomial envelope times one \(q\)-fold shell has at most \(8D\) global maxima, independently of \(q\); a sufficiently remote old \(p\)-shell splits the \(q\) nominal peaks of a new shell down to at most \(2\gcd(p,q)\); and if the \(q\) antiphodal peak rays of an active shell remain maxima throughout a radius interval, then all remaining factors must have genuine global \(q\)-fold rotational covariance. I also constructed an entire regular-shell product for which every fixed low Fourier coefficient of \(\log |f(re^{i\theta})|\) vanishes on all sufficiently large circles. This is strong exact shell neutralization, but it does not imply multiple global maxima: even polynomials with arbitrarily long such spectral gaps can have exactly one maximum point on every circle. Thus Route 2 is blocked precisely at the passage from exact Fourier neutralization to exact equality of global peak heights.

## Complete Argument

### 1. Canonical products of regular polygonal shells

For \(q\ge1\), \(R>0\), and \(\psi\in\mathbb R\), write

\[
A_{q,R,\psi}(z)
=
1-e^{-iq\psi}\left(\frac zR\right)^q.
\]

Its zeros are the vertices

\[
R\exp\left(i\left(\psi+\frac{2\pi l}{q}\right)\right),
\qquad 0\le l<q,
\]

of a regular \(q\)-gon.

Consider

\[
F(z)=\prod_{j=1}^{\infty}A_{q_j,R_j,\psi_j}(z),
\]

where \(R_j\to\infty\) and

\[
\sum_j\left(\frac A{R_j}\right)^{q_j}<\infty
\qquad\text{for every }A>0.
\tag{1}
\]

On \(|z|\le A\),

\[
\left|e^{-iq_j\psi_j}\left(\frac z{R_j}\right)^{q_j}\right|
\le \left(\frac A{R_j}\right)^{q_j},
\]

so (1) gives locally uniform convergence of the product. Hence \(F\) is entire and \(F(0)=1\). If at least one shell is present, \(F\) has zeros and therefore is not the constant monomial \(1\).

For \(\rho>0\),

\[
\log|1-\rho e^{ix}|
=
\begin{cases}
-\displaystyle\sum_{m\ge1}\frac{\rho^m}{m}\cos(mx),
&0<\rho<1,\\[1.2ex]
\log\rho-\displaystyle\sum_{m\ge1}\frac{\rho^{-m}}m\cos(mx),
&\rho>1.
\end{cases}
\tag{2}
\]

The series is locally uniform away from \(\rho=1\) and the zeros of the factor. At \(\rho=1\), it holds in \(L^1\) in the angular variable.

Thus a shell contributes

\[
\log|A_{q,R,\psi}(re^{i\theta})|
=
C(r)-\sum_{k\ge1}\frac{t(r)^k}{k}
\cos\bigl(kq(\theta-\psi)\bigr),
\tag{3}
\]

where

\[
t(r)=\min\left\{\left(\frac rR\right)^q,
\left(\frac Rr\right)^q\right\}.
\]

If \(r\) lies between shell radii, the total logarithmic modulus has the exact expansion

\[
\begin{aligned}
\log|F(re^{i\theta})|
=C(r)-\sum_{n\ge1}\frac1n\operatorname{Re}\Bigg[
e^{in\theta}\Bigg(
&r^{-n}
\sum_{\substack{j:R_j<r\\q_j\mid n}}
q_jR_j^n e^{-in\psi_j}\\
+{}&r^n
\sum_{\substack{j:R_j>r\\q_j\mid n}}
q_jR_j^{-n}e^{-in\psi_j}
\Bigg)\Bigg].
\end{aligned}
\tag{4}
\]

This formula exhibits the central obstruction: an inner shell is only approximately radial. Its angular terms are negative Laurent modes \(r^{-n}e^{in\theta}\), and they remain exact, however small.

---

### 2. Factorwise maximization gives only a fixed gcd

For every shell,

\[
|A_{q,R,\psi}(re^{i\theta})|
\le 1+\left(\frac rR\right)^q,
\tag{5}
\]

with equality exactly when

\[
q(\theta-\psi)\equiv \pi\pmod{2\pi}.
\tag{6}
\]

For a convergent infinite product, the product of the upper bounds in (5) is finite at every fixed \(r\): there are only finitely many inner shells, while the outer contribution converges by (1).

Suppose the congruences

\[
q_j(\theta-\psi_j)\equiv\pi\pmod{2\pi}
\qquad(j\ge1)
\tag{7}
\]

have a common solution. Then the product of the factorwise upper bounds is attained, hence is \(M_F(r)\). Conversely, any point attaining that product must give equality in every individual factor inequality.

Let

\[
d=\gcd(q_1,q_2,\ldots).
\]

This infinite gcd is well defined because the gcds of the finite initial segments form a decreasing sequence of positive divisors of \(q_1\), hence eventually stabilize. If (7) is consistent and \(\theta_0\) is one solution, all solutions are

\[
\theta_0+\frac{2\pi l}{d},
\qquad 0\le l<d.
\]

Therefore:

**Lemma 1.** If the global maximum of a regular-shell product is proved by simultaneous factorwise maximization, then

\[
\nu_F(r)=d,
\]

where \(d\) is the fixed gcd of all shell orders.

Thus direct phase alignment can never produce a multiplicity tending to infinity.

---

### 3. A fixed polynomial envelope bounds the number of maxima independently of the new shell order

Let \(G(\theta)\) be a nonconstant nonnegative trigonometric polynomial of degree \(D\), and let

\[
A(\theta)=a-b\cos(q\theta),
\qquad
a=1+\rho^2,\quad b=2\rho,\quad \rho>0.
\]

Set

\[
H(\theta)=G(\theta)A(\theta).
\]

This includes

\[
G(\theta)=|P(re^{i\theta})|^2,
\qquad
A(\theta)=|1-\rho e^{iq\theta}|^2.
\]

Let \(C=\max H>0\). At any global maximum, \(G>0\) and

\[
C=G(a-b\cos q\theta),
\]

so

\[
\cos q\theta=\frac{aG-C}{bG}.
\tag{8}
\]

Also,

\[
0=H'
=G'A+Gbq\sin q\theta,
\]

which, using \(A=C/G\), gives

\[
\sin q\theta=-\frac{CG'}{bqG^2}.
\tag{9}
\]

Squaring (8) and (9), adding, and clearing denominators gives

\[
E_C(\theta):=
q^2G^2\bigl((aG-C)^2-b^2G^2\bigr)
+C^2(G')^2
=0
\tag{10}
\]

at every global maximum.

Now

\[
G^2\bigl((aG-C)^2-b^2G^2\bigr)
=
(a^2-b^2)G^4-2aCG^3+C^2G^2.
\tag{11}
\]

If \(\rho\ne1\), then

\[
a^2-b^2=(1-\rho^2)^2\ne0.
\]

If \(c_D\ne0\) is the top Fourier coefficient of \(G\), the coefficient of frequency \(4D\) in \(G^4\) is \(c_D^4\ne0\). Hence \(E_C\) is a nonzero trigonometric polynomial of degree \(4D\).

If \(\rho=1\), then \(a=b=2\), so the \(G^4\) term vanishes, but the leading term is

\[
-4q^2CG^3.
\]

Because \(C>0\), \(E_C\) is then a nonzero trigonometric polynomial of degree \(3D\).

A nonzero trigonometric polynomial of degree \(L\) has at most \(2L\) distinct zeros on \([0,2\pi)\). Therefore:

**Lemma 2.** For every \(q\ge1\) and every \(\rho>0\),

\[
\#\operatorname*{argmax}_{\theta}
G(\theta)|1-\rho e^{iq\theta}|^2
\le 8D.
\tag{12}
\]

In particular, if \(P\) is a fixed nonmonomial polynomial whose lowest and highest exponents differ by \(D\), multiplying it by a shell of arbitrarily high order \(q\) cannot produce more than \(8D\) maximum points on any circle.

The exceptional case is exactly when the envelope is a monomial in modulus, in which case the \(q\)-fold shell itself has \(q\) equal maxima.

---

### 4. Exact two-shell splitting

The preceding bound does not identify how many peaks survive. For a sufficiently remote old shell, this can be determined exactly.

Let \(p,q\ge1\), \(\rho>0\), and

\[
H_\varepsilon(\theta)
=
|1-\rho e^{iq\theta}|^2
|1-\varepsilon e^{-ip\theta}|^2,
\qquad \varepsilon>0.
\tag{13}
\]

Put

\[
d=\gcd(p,q),\qquad P=p/d,\qquad Q=q/d.
\]

At \(\varepsilon=0\), the global maxima are the \(q\) nondegenerate points

\[
\theta_l=\frac{(2l+1)\pi}{q},
\qquad 0\le l<q.
\tag{14}
\]

Indeed, the second angular derivative of the first factor at \(\theta_l\) is

\[
-2\rho q^2<0.
\]

Choose disjoint neighborhoods of the \(\theta_l\). By the implicit function theorem, for sufficiently small \(\varepsilon\), each neighborhood contains a unique critical point \(\theta_l(\varepsilon)\), which is a strict local maximum. Uniform convergence to the first factor shows that every global maximum lies in one of these neighborhoods.

Let

\[
V_l(\varepsilon)=H_\varepsilon(\theta_l(\varepsilon)).
\]

Because the derivative with respect to \(\theta\) vanishes at \(\varepsilon=0\),

\[
V_l'(0)
=
(1+\rho)^2
\left.\frac{\partial}{\partial\varepsilon}
|1-\varepsilon e^{-ip\theta_l}|^2
\right|_{\varepsilon=0}
=
-2(1+\rho)^2\cos(p\theta_l).
\tag{15}
\]

Consequently, for sufficiently small \(\varepsilon\), only those \(l\) minimizing \(\cos(p\theta_l)\) can give global maxima.

The \(Q\) distinct values of \(e^{ip\theta_l}\) are

\[
e^{i\pi P/Q}e^{2\pi iPl/Q}.
\tag{16}
\]

Since \(\gcd(P,Q)=1\), this is a regular \(Q\)-gon, each vertex repeated \(d\) times among the \(q\) indices.

- If \(Q=1\), there is one vertex and therefore \(d\) selected peaks.
- If \(P\) and \(Q\) are both odd, the set (16) contains \(-1\), uniquely among its \(Q\) distinct values, so there are \(d\) selected peaks.
- Otherwise \(Q\ge2\), and the minimum real part is attained at exactly two conjugate vertices, giving \(2d\) selected peaks.

These selected peak heights are exactly equal, not merely asymptotically equal. Indeed, \(H_\varepsilon\) has period \(2\pi/d\), which identifies the \(d\) copies of each selected vertex, and it is even in \(\theta\), which interchanges the two conjugate selected orbits when there are two.

Thus:

**Lemma 3.** For sufficiently small \(\varepsilon>0\),

\[
\nu_{H_\varepsilon}
=
\begin{cases}
d,&Q=1\text{ or }P,Q\text{ both odd},\\
2d,&\text{otherwise}.
\end{cases}
\tag{17}
\]

In particular,

\[
\nu_{H_\varepsilon}\le 2\gcd(p,q)\le 2p.
\tag{18}
\]

This applies directly to two radial shells

\[
\left(1-\left(\frac zR\right)^p\right)
\left(1-\left(\frac zS\right)^q\right)
\]

near the outer shell \(r\asymp S\), because

\[
\left|1-\left(\frac{re^{i\theta}}R\right)^p\right|
=
\left(\frac rR\right)^p
\left|1-\left(\frac Rr\right)^p e^{-ip\theta}\right|.
\]

Hence a remote old \(p\)-shell, although arbitrarily close to radial in relative size, generally reduces the \(q\) nominal peaks of the outer shell to at most \(2p\).

---

### 5. Persistent antiphodal maxima force genuine rotational symmetry

The previous splitting result concerns one circle or a compact range of active-shell parameters. The all-radii requirement gives a stronger rigidity statement.

**Lemma 4.** Let \(G\) be entire and zero-free on an annulus

\[
\mathcal A=\{a<|z|<b\}.
\]

Fix \(q\ge2\) and

\[
\theta_l=\theta_0+\frac{2\pi l}{q},
\qquad 0\le l<q.
\]

Suppose that for every \(r\in(a,b)\):

1. \(|G(re^{i\theta_l})|\) is independent of \(l\);
2. \(\partial_\theta\log|G(re^{i\theta})|=0\) at every \(\theta=\theta_l\).

Then there is a constant \(c\), \(|c|=1\), such that

\[
G(e^{2\pi i/q}z)=cG(z)
\qquad\text{for every }z\in\mathbb C.
\tag{19}
\]

**Proof.** Since \(G\) is zero-free on \(\mathcal A\),

\[
u(z)=\log|G(z)|
\]

is harmonic there and has a convergent harmonic Laurent expansion

\[
u(re^{i\theta})
=
A\log r+B+
\operatorname{Re}\sum_{n\ge1}
\left(
a_nr^ne^{in\theta}
+b_nr^{-n}e^{-in\theta}
\right).
\tag{20}
\]

The powers \(r^n\), \(r^{-n}\), \(1\), and \(\log r\) are linearly independent on an interval, and the Laurent expansion is unique. Thus the two hypotheses apply separately to every Fourier-Laurent mode.

For a positive mode, put

\[
X_l=a_ne^{in\theta_l}.
\]

The derivative condition says \(\operatorname{Im}X_l=0\), while equality of the values says \(\operatorname{Re}X_l\) is independent of \(l\). Hence all \(X_l\) are the same real number. But

\[
X_{l+1}=e^{2\pi in/q}X_l.
\]

If \(q\nmid n\), this is possible only if \(a_n=0\). The same argument gives \(b_n=0\) whenever \(q\nmid n\). Therefore only frequencies divisible by \(q\) occur in (20), and

\[
|G(e^{2\pi i/q}z)|=|G(z)|
\quad(z\in\mathcal A).
\]

The quotient

\[
h(z)=\frac{G(e^{2\pi i/q}z)}{G(z)}
\]

is holomorphic on \(\mathcal A\) and has constant modulus \(1\). By the open mapping theorem, \(h\) is a constant \(c\). Hence

\[
G(e^{2\pi i/q}z)=cG(z)
\]

on \(\mathcal A\), and the identity theorem extends this relation to all of \(\mathbb C\). ∎

Now let

\[
F(z)=A_{q,R,\psi}(z)G(z).
\]

The \(q\) factorwise maximum rays of the active shell are

\[
\theta_l=\psi+\frac{(2l+1)\pi}{q}.
\tag{21}
\]

At all these points, the active factor has the same modulus and zero angular derivative. If, throughout an open radius interval on which \(G\) is zero-free, all points (21) are global maximum points of \(F\), then equality of their \(F\)-moduli gives equality of their \(G\)-moduli, and stationarity of \(F\) gives stationarity of \(G\). Lemma 4 therefore forces (19).

If \(G\) has a nonzero zero \(\alpha\), relation (19) forces all

\[
\alpha,\ e^{2\pi i/q}\alpha,\ldots,e^{2\pi i(q-1)/q}\alpha
\]

to be zeros. These are \(q\) distinct points on \(|z|=|\alpha|\). Since an entire nonzero function has only finitely many zeros on a fixed compact circle, the possible values of \(q\) are bounded by the number of zeros of \(G\) on that circle.

Consequently, in a shell construction with a fixed earlier nonzero zero, the exact antiphodal maxima of successive active shells cannot persist on open radius intervals with orders \(q\to\infty\).

This rules out the most natural exact implementation of Route 2. It does not rule out maxima that move away from the shell’s antiphodal rays.

---

### 6. Exact neutralization of every fixed low logarithmic Fourier mode

Although exact radial neutralization is impossible, finite collections of moments can be canceled exactly.

For a regular \(n\)-gon at radius \(R\) and rotation \(\psi\), its zero power sum is

\[
\sum_{l=0}^{n-1}
\left(
Re^{i(\psi+2\pi l/n)}
\right)^m
=
\begin{cases}
nR^m e^{im\psi},&n\mid m,\\
0,&n\nmid m.
\end{cases}
\tag{22}
\]

I now construct two \(n\)-gons at each stage \(n\).

Suppose stages \(1,\ldots,n-1\) have been constructed, and let \(s_n\) be the \(n\)-th power sum of all existing zeros. Choose \(R_n\) arbitrarily large, with

\[
R_n>R_{n-1},\qquad
R_n\ge 2^n,\qquad
|s_n|\le 2nR_n^n.
\tag{23}
\]

Every complex number of modulus at most \(2\) is a sum of two unimodular complex numbers. Therefore choose \(u_{n,1},u_{n,2}\), \(|u_{n,h}|=1\), satisfying

\[
u_{n,1}+u_{n,2}
=
-\frac{s_n}{nR_n^n}.
\tag{24}
\]

Choose rotations \(\psi_{n,h}\) with

\[
e^{in\psi_{n,h}}=u_{n,h}.
\]

Add the two corresponding regular \(n\)-gons. Their combined \(n\)-th power sum is \(-s_n\), while by (22) they do not affect any lower power sum. Inductively, after stage \(n\),

\[
s_1=s_2=\cdots=s_n=0.
\tag{25}
\]

Future stages \(k>n\) do not change \(s_n\), because a regular \(k\)-gon has zero \(n\)-th power sum.

Define

\[
F(z)
=
\prod_{n=1}^{\infty}
\prod_{h=1}^2
\left[
1-e^{-in\psi_{n,h}}
\left(\frac z{R_n}\right)^n
\right].
\tag{26}
\]

Since \(R_n\ge2^n\),

\[
\sum_{n=1}^{\infty}2\left(\frac A{R_n}\right)^n<\infty
\]

for every fixed \(A\). Thus (26) converges locally uniformly and defines an entire function. It satisfies \(F(0)=1\) and has infinitely many zeros, so it is nonzero and nonmonomial.

Let

\[
u_r(\theta)=\log|F(re^{i\theta})|.
\]

At a zero on the circle, \(u_r\) has only a logarithmic singularity, so it is still in \(L^1\). Let \(\widehat u_r(m)\) denote its \(m\)-th Fourier coefficient.

Fix \(m\ge1\) and take \(r>R_m\). A shell of order \(n\) contributes to frequency \(m\) only if \(n\mid m\), hence only if \(n\le m\). All such shells lie inside \(|z|=r\). Formula (4) gives

\[
\widehat u_r(m)
=
-\frac{1}{2mr^m}
\overline{
\sum_{\alpha\text{ a zero of }F}\alpha^m
}.
\tag{27}
\]

Only stages \(n\mid m\) contribute to the sum, so it is finite and equals the stabilized power sum \(s_m=0\). Therefore

\[
\widehat u_r(m)=0
\qquad(r>R_m).
\tag{28}
\]

Hence:

**Lemma 5.** The entire regular-shell product (26) satisfies, for every \(K\),

\[
\widehat u_r(m)=0
\qquad
(1\le |m|\le K,\ r>R_K).
\tag{29}
\]

Thus the angular Fourier spectrum of \(\log|F|\) has an exact spectral gap tending to infinity on all sufficiently large circles.

---

### 7. Why the spectral-gap construction does not solve the problem

A spectral gap does not force even two global maximum points.

For any \(K\ge1\), consider

\[
P_K(z)=z^{K+2}+z+1.
\tag{30}
\]

If its zeros are \(\alpha_1,\ldots,\alpha_{K+2}\), Newton’s identities and the absence of the coefficients of

\[
z^{K+1},z^K,\ldots,z^2
\]

give

\[
\sum_j\alpha_j^m=0,
\qquad 1\le m\le K.
\tag{31}
\]

Consequently, outside all its zeros, the first \(K\) nonconstant Fourier coefficients of \(\log|P_K(re^{i\theta})|\) vanish.

Nevertheless,

\[
|P_K(re^{i\theta})|
\le r^{K+2}+r+1.
\tag{32}
\]

Equality requires the three summands to have the same phase. Since the constant term has phase \(0\), equality requires \(e^{i\theta}=1\). This also aligns the highest term. Therefore

\[
\nu_{P_K}(r)=1
\qquad\text{for every }r>0.
\tag{33}
\]

Thus arbitrarily long exact low-frequency gaps in \(\log|f|\), even within the logarithmic modulus of a polynomial, do not imply multiple global maxima.

Lemma 5 therefore achieves exact shell neutralization but stops strictly short of the required conclusion.

## Self-Audit

1. **The exact two-shell count is asymptotic rather than effective.**  
   I prove the existence of an \(\varepsilon_0(p,q,\rho)>0\), but do not provide a numerical formula. The conclusion nevertheless follows rigorously from nondegeneracy, the implicit function theorem, the first-order separation in (15), and exact rotational/reflection symmetries.

2. **The persistent-ray rigidity lemma has restrictive hypotheses.**  
   It requires the maxima to remain on the active shell’s fixed antiphodal rays and the remaining factor to be zero-free on the annulus. These hypotheses hold for the natural “active shell supplies the designated maxima” construction on a shell-free radial band, but not for moving or irregular maximum branches. I do not claim otherwise; under the stated hypotheses, Laurent-series uniqueness makes the proof complete.

3. **The moment-neutralized product controls \(\log|F|\), not \(|F|^2\) or peak equality.**  
   Exponentiating a high-frequency logarithmic profile can regenerate low Fourier modes in \(|F|^2\), and in any case Fourier gaps do not control global ties. The construction and cancellation identities themselves are exact, while the polynomial example (30)–(33) shows decisively why this does not settle \(\nu_F(r)\).

## Computations To Verify

The following code constructs the moment-neutralized shells, verifies the canceled power sums, and numerically counts critical maxima for finite truncations.

```python
import numpy as np
import cmath
import math

def two_unit_sum(t):
    """Return unit complex u1,u2 with u1+u2=t, assuming |t| <= 2."""
    a = abs(t)
    if a < 1e-30:
        return 1.0 + 0j, -1.0 + 0j
    eta = t / a
    alpha = math.acos(min(1.0, a / 2.0))
    return eta * cmath.exp(1j * alpha), eta * cmath.exp(-1j * alpha)

def neutralized_shells(K):
    """
    Construct two regular n-gons at each stage n <= K.
    Returns:
      shells = [(n,R,psi), ...]
      zeros  = all zeros in the finite product
    """
    shells = []
    zeros = []
    Rprev = 1.0

    for n in range(1, K + 1):
        s = sum(z**n for z in zeros)

        lower = (abs(s) / (2.0*n))**(1.0/n) if abs(s) > 0 else 0.0
        R = max(2.0 * Rprev, 2.0**n, 2.0 * lower + 1.0)

        t = -s / (n * R**n)
        assert abs(t) <= 2.0 + 1e-12

        u1, u2 = two_unit_sum(t)
        for u in (u1, u2):
            psi = cmath.phase(u) / n
            shells.append((n, R, psi))
            for ell in range(n):
                zeros.append(
                    R * cmath.exp(1j * (psi + 2*math.pi*ell/n))
                )

        # Verify all power sums through n.
        for m in range(1, n + 1):
            sm = sum(z**m for z in zeros)
            scale = max(1.0, sum(abs(z)**m for z in zeros))
            assert abs(sm) / scale < 1e-10

        Rprev = R

    return shells, zeros

def product_coefficients(shells):
    """Ascending coefficients of the finite shell product."""
    a = np.array([1.0 + 0j])
    for n, R, psi in shells:
        factor = np.zeros(n + 1, dtype=complex)
        factor[0] = 1.0
        factor[n] = -cmath.exp(-1j*n*psi) / R**n
        a = np.polynomial.polynomial.polymul(a, factor)
    return a

def critical_angles_on_circle(a, r, unit_tol=1e-6):
    """
    Find angular critical points of |p(re^{i theta})|^2
    through the autocorrelation Laurent polynomial.
    Exploratory floating-point routine, not a certificate.
    """
    a = np.asarray(a, dtype=complex)
    D = len(a) - 1
    b = a * (r ** np.arange(D + 1))

    c = {}
    for k in range(0, D + 1):
        c[k] = sum(b[j+k] * np.conj(b[j]) for j in range(D-k+1))
        if k > 0:
            c[-k] = np.conj(c[k])

    # x^D dH/dtheta = sum i*k*c_k*x^(k+D)
    Q = np.zeros(2*D + 1, dtype=complex)
    for k in range(-D, D + 1):
        Q[k + D] = 1j * k * c[k]

    roots = np.roots(Q[::-1])
    angles = []
    for x in roots:
        if abs(abs(x) - 1.0) < unit_tol:
            th = cmath.phase(x) % (2*math.pi)
            if all(abs(cmath.exp(1j*th) - cmath.exp(1j*t)) > 1e-5
                   for t in angles):
                angles.append(th)

    vals = []
    for th in angles:
        z = r * cmath.exp(1j*th)
        val = abs(np.polynomial.polynomial.polyval(z, a))**2
        vals.append(val)

    return angles, vals

def numerical_nu(a, r, reltol=1e-8):
    angles, vals = critical_angles_on_circle(a, r)
    vmax = max(vals)
    winners = [
        th for th, v in zip(angles, vals)
        if abs(v-vmax) <= reltol * max(1.0, vmax)
    ]
    return len(winners), winners, vmax
```

Test the exact two-shell prediction using the polynomial

\[
(z^p-\varepsilon)(1-\rho z^q)
\]

on the unit circle:

```python
def two_shell_coeffs(p, q, eps, rho):
    f1 = np.zeros(p + 1, dtype=complex)
    f1[0], f1[p] = -eps, 1.0

    f2 = np.zeros(q + 1, dtype=complex)
    f2[0], f2[q] = 1.0, -rho

    return np.polynomial.polynomial.polymul(f1, f2)

def predicted_two_shell_count(p, q):
    d = math.gcd(p, q)
    P, Q = p // d, q // d
    if Q == 1 or (P % 2 == 1 and Q % 2 == 1):
        return d
    return 2*d

for p in [1, 2, 3, 4]:
    for q in range(2, 13):
        a = two_shell_coeffs(p, q, eps=1e-5, rho=1.3)
        num, winners, vmax = numerical_nu(a, 1.0)
        print(p, q, "predicted", predicted_two_shell_count(p, q),
              "numerical", num)
```

For the moment-neutralized product, verify spectral cancellation and inspect transition radii:

```python
shells, zeros = neutralized_shells(7)
a = product_coefficients(shells)

# Exact structural check via power sums.
for m in range(1, 8):
    sm = sum(z**m for z in zeros)
    print("m =", m, "power sum =", sm)

# Inspect maxima just below, at, and above shell radii.
radii = sorted(set(R for n, R, psi in shells))
for R in radii:
    for factor in [0.8, 0.95, 1.0, 1.05, 1.2]:
        r = factor * R
        try:
            num, winners, vmax = numerical_nu(a, r)
            print("r =", r, "nu approximately =", num)
        except Exception as exc:
            print("ill-conditioned at r =", r, exc)
```

For a certified finite check with rational coefficients and rational \(r\), use exact algebraic elimination:

```text
Input polynomial p and radius r.

1. Put z = r(x+iy), with x^2+y^2=1.
2. Form H(x,y) = |p(z)|^2 exactly over Q[x,y].
3. Form the angular derivative
       D(x,y) = -y * dH/dx + x * dH/dy.
4. Solve the zero-dimensional real algebraic system
       x^2+y^2-1 = 0,
       D(x,y) = 0
   using resultants and real-root isolation.
5. Evaluate H as an algebraic number at every isolated solution.
6. Compare the algebraic values exactly and count the maximizers.
```

This should be run particularly for \(p=1\), where Lemma 3 predicts one surviving maximum for odd \(q\) and two for even \(q\), once \(\varepsilon\) is sufficiently small.

## Route Diagnosis

**Proved ledger.**

1. Exact logarithmic Fourier expansion (4) for regular polygonal shell products.
2. Simultaneous factorwise maximization produces exactly the fixed gcd of all shell orders.
3. A fixed degree-\(D\) nonmonomial polynomial envelope times one \(q\)-shell has at most \(8D\) global maxima, independently of \(q\).
4. A sufficiently weak old \(p\)-shell splits the \(q\) active peaks to exactly \(d\) or \(2d\), where \(d=\gcd(p,q)\).
5. Persistent maxima on the active shell’s fixed antiphodal rays force genuine \(q\)-fold rotational covariance of the remaining entire factor.
6. There exists an entire regular-shell product whose first \(K\) logarithmic angular Fourier coefficients vanish on every circle beyond a radius \(R_K\).

**Dead ends.**

- “Remote shells are almost radial” fails because arbitrarily small nonradial terms split exact peak ties.
- Exact phase alignment is confined to a fixed global gcd.
- Vanishing low Fourier modes does not imply multiple global maxima; \(z^{K+2}+z+1\) has the relevant exact moment gap but one maximum point on every circle.
- Keeping the active shell’s standard \(q\) peak rays throughout an annulus forces global symmetry and therefore cannot support \(q\to\infty\).

**Plausible but unproved.**

- In strongly separated generic shell products, the oldest surviving nonsymmetric Laurent mode should eventually reduce the global multiplicity to a bounded number.
- Persistent large equal-height branches that move with \(r\) may still force some rotational covariance, but the fixed-ray Laurent argument does not cover moving branches.
- Carefully correlated shell clusters might tune moving peak heights without full symmetry, but doing so over a continuum of radii appears to require infinitely many exact analytic identities.

**Precise block.**

Any successful continuation of Route 2 must use global maximum points that move away from the active shell’s antiphodal grid. It must prove exact equality among many such moving critical values throughout every active and transition interval. Neither shell dominance, Fourier neutralization, nor approximate radiality supplies this equality. Establishing it would require a new moving-branch phase-locking theorem; at present that is essentially the original open difficulty rather than a reduced problem.

A fresh attempt should either:

1. classify moving equal-critical-value branches for products of two or three polygonal shells and look for a non-symmetry mechanism that survives on an open radius interval; or
2. switch to the real-analytic rigidity route and try to prove that sufficiently many persistent moving branches force rotational covariance, which would support a negative answer.