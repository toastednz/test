STATUS: BLOCKED

## Result

I did not construct a transcendental entire witness. I proved, however, a uniform zero-forcing lemma for a highly symmetric exponential spectrum: for every compact disc and every \(\varepsilon>0\), there is a finite exponential sum supported on one frequency circle such that the zero set of **every derivative** is \(\varepsilon\)-dense in that compact disc, with explicit Rouché contours and margins. This resolves the main finite-scale geometric concern in Route 2: equal-modulus frequencies arranged in many directions can make their Stokes network arbitrarily fine, uniformly over all derivative orders. I also proved a finite spectral interpolation lemma on any prescribed frequency circle. The remaining obstruction is an infinite gluing theorem: combining increasingly fine spectral rings into one normally convergent entire series without losing zeros at transitions between dominant rings. A naive one-ring-at-a-time Rouché strategy fails at adjacent transitions for a precise local reason described below.

## Complete Argument

### 1. Uniform zero forcing by one circular spectrum

For an integer \(M\geq4\), let

\[
\omega=e^{2\pi i/M}
\]

and define

\[
F_{M,r}(w)=\sum_{j=0}^{M-1}\omega^{jr}e^{\omega^j w},
\qquad 0\leq r<M.
\]

For \(R>0\), define the finite exponential sum

\[
P_{M,R}(z)=\sum_{j=0}^{M-1}e^{R\omega^jz}.
\]

Then

\[
P_{M,R}^{(n)}(z)
=
R^n F_{M,r}(Rz),
\qquad r\equiv n\pmod M.
\tag{1}
\]

Thus the normalized derivatives cycle through the \(M\) functions \(F_{M,r}\).

#### Theorem 1: explicit covering-radius bound

Fix

\[
\rho=\frac1{100},
\]

and put

\[
L_M=\frac{\pi}{\sin(\pi/M)}
\]

and

\[
T_M=
\frac{M^2}{16}
\left(
2\log M+\log\frac{2}{\rho}+2\rho
\right).
\]

For every \(K,R>0\), every \(n\geq0\), and every \(z_0\) with \(|z_0|\leq K\), the derivative \(P_{M,R}^{(n)}\) has a simple zero \(z_*\) satisfying

\[
|z_*-z_0|
\leq
\frac{\pi K}{M}
+
\frac{T_M+L_M+\rho}{R}.
\tag{2}
\]

More precisely, there is a circle of radius \(\rho/R\), contained in the right-hand side of (2), on which \(P_{M,R}^{(n)}\) is bounded away from zero and inside which it has exactly one zero.

Consequently, given \(K,\varepsilon>0\), if \(M,R\) are chosen so that

\[
\frac{\pi K}{M}<\frac{\varepsilon}{2},
\qquad
\frac{T_M+L_M+\rho}{R}<\frac{\varepsilon}{2},
\tag{3}
\]

then the zero set of every derivative \(P_{M,R}^{(n)}\) is \(\varepsilon\)-dense in \(\{|z|\leq K\}\).

#### Proof

Fix a residue \(r\in\{0,\ldots,M-1\}\). For each \(j\), let

\[
\beta_j=\frac{(2j+1)\pi}{M}
\]

and consider the ray

\[
\mathcal R_j=\{t e^{-i\beta_j}:t\geq0\}.
\]

On this ray, the \(j\)-th and \((j+1)\)-st exponentials have equal modulus. Indeed, for \(w=t e^{-i\beta_j}\),

\[
\operatorname{Re}(\omega^j w)
=
\operatorname{Re}(\omega^{j+1}w)
=
t\cos\frac{\pi}{M}.
\tag{4}
\]

Every other frequency has angular separation at least \(3\pi/M\) from the ray’s maximizing direction, and hence

\[
\operatorname{Re}(\omega^k w)
\leq
t\cos\frac{3\pi}{M},
\qquad k\notin\{j,j+1\}.
\tag{5}
\]

Consider the two-term sum

\[
H_{j,r}(w)
=
\omega^{jr}e^{\omega^jw}
+
\omega^{(j+1)r}e^{\omega^{j+1}w}.
\]

Since

\[
(\omega^{j+1}-\omega^j)t e^{-i\beta_j}
=
2it\sin\frac{\pi}{M},
\]

the zeros of \(H_{j,r}\) on \(\mathcal R_j\) are given by

\[
2t\sin\frac{\pi}{M}+\frac{2\pi r}{M}
\equiv \pi\pmod{2\pi}.
\tag{6}
\]

Their radial spacing is exactly

\[
L_M=\frac{\pi}{\sin(\pi/M)}.
\tag{7}
\]

In particular, for every \(A\geq0\), there is such a zero

\[
w_*=t_*e^{-i\beta_j}
\]

with

\[
A\leq t_*\leq A+L_M.
\tag{8}
\]

We now prove that when \(t_*\geq T_M\), a zero of the full sum \(F_{M,r}\) lies within \(\rho\) of \(w_*\).

Write

\[
F_{M,r}=H_{j,r}+G_{j,r},
\]

where \(G_{j,r}\) is the sum of the remaining \(M-2\) terms. On

\[
|w-w_*|=\rho,
\]

put

\[
u=(\omega^{j+1}-\omega^j)(w-w_*).
\]

At \(w_*\), the ratio of the second term of \(H_{j,r}\) to the first is \(-1\). Therefore

\[
|H_{j,r}(w)|
=
e^{\operatorname{Re}(\omega^jw)}|1-e^u|.
\]

Now

\[
|u|
=
2\rho\sin\frac{\pi}{M}
\leq 2\rho<\frac12.
\]

For \(|u|\leq1/2\),

\[
|e^u-1|\geq \frac{|u|}{2}.
\]

Also,

\[
\operatorname{Re}(\omega^jw)
\geq
t_*\cos\frac{\pi}{M}-\rho.
\]

Hence

\[
|H_{j,r}(w)|
\geq
\rho\sin\frac{\pi}{M}
\exp\left(
t_*\cos\frac{\pi}{M}-\rho
\right).
\tag{9}
\]

For every term in \(G_{j,r}\), (5) and \(|w-w_*|=\rho\) give

\[
|e^{\omega^kw}|
\leq
\exp\left(
t_*\cos\frac{3\pi}{M}+\rho
\right).
\]

Thus

\[
|G_{j,r}(w)|
\leq
M\exp\left(
t_*\cos\frac{3\pi}{M}+\rho
\right).
\tag{10}
\]

Let

\[
d_M=
\cos\frac{\pi}{M}-\cos\frac{3\pi}{M}
=
2\sin\frac{2\pi}{M}\sin\frac{\pi}{M}.
\]

For \(M\geq4\), using \(\sin x\geq 2x/\pi\) on \(0\leq x\leq\pi/2\),

\[
\sin\frac{\pi}{M}\geq\frac2M,
\qquad
\sin\frac{2\pi}{M}\geq\frac4M,
\]

and therefore

\[
d_M\geq\frac{16}{M^2}.
\tag{11}
\]

Combining (9) and (10),

\[
\frac{|G_{j,r}(w)|}{|H_{j,r}(w)|}
\leq
\frac{M}{\rho\sin(\pi/M)}
e^{-t_*d_M+2\rho}
\leq
\frac{M^2}{2\rho}
e^{-16t_*/M^2+2\rho}.
\tag{12}
\]

If \(t_*\geq T_M\), the right-hand side is at most \(1/4\). Therefore

\[
|G_{j,r}(w)|<|H_{j,r}(w)|
\]

on \(|w-w_*|=\rho\).

The zeros of \(H_{j,r}\) have mutual distance \(L_M>2\rho\), so \(H_{j,r}\) has exactly one, necessarily simple, zero in \(|w-w_*|<\rho\). Rouché’s theorem shows that \(F_{M,r}\) also has exactly one zero there. In addition, (9) and (12) give the explicit boundary margin

\[
|F_{M,r}(w)|
\geq
\frac12
\rho\sin\frac{\pi}{M}
\exp\left(
t_*\cos\frac{\pi}{M}-\rho
\right).
\tag{13}
\]

It remains to prove the covering estimate. Given \(w_0\in\mathbb C\), choose the nearest ray \(\mathcal R_j\). The angular distance is at most \(\pi/M\), so the distance from \(w_0\) to the point \(|w_0|e^{-i\beta_j}\) is at most

\[
\frac{\pi|w_0|}{M}.
\tag{14}
\]

By (8), there is a two-term zero on that ray with radial coordinate \(t_*\geq T_M\) and

\[
\left|t_*-|w_0|\right|
\leq T_M+L_M.
\tag{15}
\]

The full function \(F_{M,r}\) has a zero within \(\rho\) of that two-term zero. Hence

\[
\operatorname{dist}\bigl(w_0,Z(F_{M,r})\bigr)
\leq
\frac{\pi|w_0|}{M}+T_M+L_M+\rho.
\tag{16}
\]

Apply this with \(w_0=Rz_0\), divide by \(R\), and use (1). This proves (2). The zero is simple because its Rouché disc contains exactly one zero counted with multiplicity. ∎

---

### 2. Stable version of the ring lemma

The preceding proof gives more than mere zero existence.

Let \(\Gamma\) be the circle in the \(z\)-plane corresponding to

\[
|w-w_*|=\rho.
\]

Thus \(\Gamma\) has radius \(\rho/R\). On \(\Gamma\), (13) and (1) imply

\[
|P_{M,R}^{(n)}(z)|
\geq
\frac12 R^n
\rho\sin\frac{\pi}{M}
\exp\left(
t_*\cos\frac{\pi}{M}-\rho
\right).
\tag{17}
\]

Therefore, if an entire perturbation \(E\) satisfies on \(\Gamma\)

\[
|E(z)|
<
\frac12 R^n
\rho\sin\frac{\pi}{M}
\exp\left(
t_*\cos\frac{\pi}{M}-\rho
\right),
\tag{18}
\]

then \(P_{M,R}^{(n)}+E\) has exactly one zero inside \(\Gamma\).

Thus the ring construction supplies the robust contours needed in an eventual infinite construction.

---

### 3. Finite interpolation on one frequency circle

The following establishes substantial finite-dimensional flexibility for Route 2.

#### Lemma 2

Let

\[
(q_1,\zeta_1),\ldots,(q_m,\zeta_m)
\]

be distinct pairs with \(q_i\in\mathbb N_0\) and \(\zeta_i\in\mathbb C\). Given \(R>0\) and arbitrary values \(v_1,\ldots,v_m\in\mathbb C\), there is an exponential polynomial

\[
E(z)=\sum_{k=1}^m c_ke^{\lambda_kz},
\qquad |\lambda_k|=R,
\]

such that

\[
E^{(q_i)}(\zeta_i)=v_i
\qquad(1\leq i\leq m).
\tag{19}
\]

#### Proof

For each \(i\), define the entire function of the spectral parameter

\[
\phi_i(\lambda)=\lambda^{q_i}e^{\zeta_i\lambda}.
\]

These functions are linearly independent.

Indeed, suppose

\[
\sum_{i=1}^m a_i\lambda^{q_i}e^{\zeta_i\lambda}\equiv0.
\]

Group terms with the same \(\zeta\):

\[
\sum_{\zeta}p_\zeta(\lambda)e^{\zeta\lambda}\equiv0,
\]

where the \(p_\zeta\) are polynomials. Fix \(\zeta_0\) with \(p_{\zeta_0}\neq0\), and apply

\[
\prod_{\zeta\neq\zeta_0}
\left(\frac{d}{d\lambda}-\zeta\right)^{\deg p_\zeta+1}.
\]

This annihilates every term except the \(\zeta_0\)-term. On that term it produces

\[
e^{\zeta_0\lambda}Q(\lambda),
\]

where \(Q\neq0\): for \(a\neq0\), the operator \(D+a\) is injective on polynomials, as is every positive power of it. This is a contradiction. Hence the \(\phi_i\) are independent.

Consider the vectors

\[
V(\lambda)=\bigl(\phi_1(\lambda),\ldots,\phi_m(\lambda)\bigr)
\in\mathbb C^m,
\qquad |\lambda|=R.
\]

Their span is all of \(\mathbb C^m\). Otherwise there would be a nonzero linear functional annihilating \(V(\lambda)\) for every \(\lambda\) on the circle. The corresponding nonzero linear combination of the \(\phi_i\) would vanish on a circle and hence, by the identity theorem, identically.

Thus one may choose \(\lambda_1,\ldots,\lambda_m\), all on \(|\lambda|=R\), such that the matrix

\[
A_{ik}=\lambda_k^{q_i}e^{\lambda_k\zeta_i}
\]

is invertible. Solving

\[
Ac=v
\]

gives coefficients \(c_k\) satisfying (19). ∎

#### Corollary 3

Given finitely many distinct target points \(\zeta_i\) and derivative orders \(n_i\), one can choose a finite exponential polynomial supported on any prescribed frequency circle such that

\[
E^{(n_i)}(\zeta_i)=0,
\qquad
E^{(n_i+1)}(\zeta_i)=1.
\]

Thus every prescribed zero is simple.

To apply Lemma 2, choose all \(\zeta_i\) distinct, so that the pairs

\[
(n_i,\zeta_i),\qquad (n_i+1,\zeta_i)
\]

are pairwise distinct.

This proves that finite sets of zero constraints are not algebraically overdetermined in the circular-spectrum model. What is missing is quantitative control of the resulting coefficients as the number of constraints tends to infinity.

---

### 4. Why the obvious infinite gluing argument breaks

Theorem 1 suggests choosing increasingly fine rings

\[
P_s=P_{M_s,R_s}
\]

and trying to form

\[
f(z)=\sum_{s\geq1}a_sP_s(z),
\tag{20}
\]

with

\[
\sum_s |a_s|M_se^{R_sK}<\infty
\qquad\text{for every }K>0.
\tag{21}
\]

Each \(P_s\) individually has every derivative zero-dense at the spatial resolution associated with \((M_s,R_s)\). One would like derivative order \(n\) to be controlled by a single ring whose scalar size is approximately

\[
|a_s|R_s^n.
\]

The logarithms are affine functions of \(n\),

\[
\log|a_s|+n\log R_s,
\]

so by choosing lacunary \(R_s\), one can arrange sharp changes of scalar dominance between consecutive derivative orders.

The missing point is that scalar dominance at a point does not give Rouché dominance on a contour. A high-frequency term can be small at the contour’s center and exponentially larger on its boundary.

The following local calculation identifies the difficulty. Suppose \(G\) has a simple zero at \(0\), with \(G'(0)=g\neq0\), and one tries to preserve that zero against

\[
H(z)=Ae^{\Lambda z}
\]

on \(|z|=\delta\). A sufficient Rouché condition is of the form

\[
|A|e^{|\Lambda|\delta}
<
c|g|\delta
\tag{22}
\]

for some fixed local constant \(c>0\). But then

\[
|H'(0)|
=
|\Lambda A|
<
c|g|\,
(|\Lambda|\delta)e^{-|\Lambda|\delta}
\leq
\frac{c}{e}|g|.
\tag{23}
\]

Thus a high-frequency component that is small enough by this argument to preserve a simple zero of the previous derivative cannot simultaneously become arbitrarily dominant after one differentiation. Shrinking the contour does not remove the obstruction because

\[
x e^{-x}\leq \frac1e.
\]

This does not prove that a transition sum is zero-free. It proves only that the straightforward strategy

> preserve the old ring’s zeros at order \(n\), then let the new ring dominate at order \(n+1\)

cannot be justified by separate one-ring Rouché estimates.

A successful completion of Route 2 therefore requires a genuine **transition theorem** showing that a sum of two or several comparable spectral rings itself has a fine zero set. I have not proved such a theorem.

---

### 5. Exact point at which the full construction is blocked

The proved results reduce the intended problem to a substantially more structured but still unproved gluing assertion.

A sufficient statement would be:

> There exist \(M_s,R_s,a_s\), with \(M_s,R_s\to\infty\) and satisfying (21), such that for every compact disc \(K\) and every \(\varepsilon>0\), all sufficiently high derivatives of the series (20) have \(\varepsilon\)-dense zero sets in \(K\).

An even more useful local lemma would say that sums of two rings,

\[
A\,F_{M,r}(Rz)+B\,F_{N,q}(Sz),
\qquad S\gg R,
\tag{24}
\]

have a zero-covering radius controlled by something like

\[
C\left(
\frac{K}{M}
+\frac{M^2\log M}{R}
+\frac{K}{N}
+\frac{N^2\log N+|\log|A/B||}{S}
\right),
\tag{25}
\]

uniformly in the phase residues \(r,q\). Such a theorem would allow one to bridge scalar crossovers rather than trying to preserve one ring’s pre-existing zeros.

I do not currently have a proof of (25), and asserting it merely from tropical pictures would be unjustified.

## Self-Audit

1. **The decisive missing step is infinite gluing.**  
   Theorem 1 only gives finite-scale approximants; it does not yield one function with successively finer zero meshes. I have not implicitly assumed such a gluing theorem, which is why the status is BLOCKED rather than solved.

2. **The two-term dominance estimate is the most delicate proved step.**  
   In particular, all nonadjacent terms must remain smaller on an entire contour, not just on the central Stokes ray. The \(\rho\)-perturbation was included explicitly in (9)–(12), and the bound \(d_M\geq16/M^2\) gives a uniform factor \(1/4\), so Rouché applies strictly.

3. **The interpolation lemma has no usable coefficient bound.**  
   Its existence proof may produce extremely ill-conditioned matrices and enormous coefficients. The lemma is nevertheless correct as a finite statement because linear independence implies that evaluation vectors on the circle span the whole finite-dimensional target space. It cannot yet support an infinite convergence argument.

## Computations To Verify

The first computation checks the explicit Rouché contours for Theorem 1.

```python
import numpy as np
import cmath
import math

rho = 0.01

def omega(M):
    return cmath.exp(2j * math.pi / M)

def F(M, r, w):
    om = omega(M)
    return sum((om**(j*r)) * cmath.exp((om**j) * w)
               for j in range(M))

def H_pair(M, r, j, w):
    om = omega(M)
    return ((om**(j*r)) * cmath.exp((om**j) * w)
            + (om**((j+1)*r)) * cmath.exp((om**(j+1)) * w))

def constants(M):
    L = math.pi / math.sin(math.pi / M)
    T = (M*M/16.0) * (
        2*math.log(M) + math.log(2/rho) + 2*rho
    )
    return T, L

def next_pair_zero_radius(M, r, A):
    """
    Finds t >= A satisfying
    2 t sin(pi/M) + 2 pi r/M == pi mod 2 pi.
    """
    s = math.sin(math.pi / M)
    alpha = math.pi - 2*math.pi*r/M
    ell = math.ceil((2*s*A - alpha) / (2*math.pi))
    t = (alpha + 2*math.pi*ell) / (2*s)
    while t < A:
        ell += 1
        t = (alpha + 2*math.pi*ell) / (2*s)
    return t

def winding_number(values):
    args = np.unwrap(np.angle(np.array(values, dtype=complex)))
    return int(round((args[-1] - args[0]) / (2*math.pi)))

def verify_contour(M, r, j, samples=20000):
    T, L = constants(M)
    t = next_pair_zero_radius(M, r, T)
    beta = (2*j + 1) * math.pi / M
    wstar = t * cmath.exp(-1j * beta)

    vals_F = []
    max_ratio = 0.0

    for k in range(samples + 1):
        theta = 2*math.pi*k/samples
        w = wstar + rho*cmath.exp(1j*theta)
        h = H_pair(M, r, j, w)
        g = F(M, r, w) - h
        max_ratio = max(max_ratio, abs(g)/abs(h))
        vals_F.append(F(M, r, w))

    return {
        "M": M,
        "r": r,
        "j": j,
        "t": t,
        "T": T,
        "max_remainder_ratio": max_ratio,
        "winding_F": winding_number(vals_F),
    }

for M in [4, 6, 8, 12, 16]:
    for r in range(M):
        result = verify_contour(M, r, 0, samples=4000)
        assert result["max_remainder_ratio"] < 1.0
        assert result["winding_F"] == 1
    print("verified numerically for M =", M)
```

For larger \(M\), direct exponentials may overflow. A stable implementation should subtract

\[
\max_j \operatorname{Re}(\omega^jw)
\]

from all exponents before summation.

The interpolation lemma can be tested as follows.

```python
import numpy as np
import cmath
import math
from scipy.linalg import qr

def spectral_interpolant(pairs, values, R, number_candidates=500):
    """
    pairs = [(q_i, zeta_i)]
    Find frequencies on |lambda|=R and coefficients c_k so that
    sum c_k lambda_k^{q_i} exp(lambda_k*zeta_i) = values[i].
    """
    m = len(pairs)
    thetas = np.linspace(0, 2*math.pi, number_candidates, endpoint=False)
    lambdas = R * np.exp(1j*thetas)

    Awide = np.empty((m, number_candidates), dtype=complex)
    for i, (q, zeta) in enumerate(pairs):
        Awide[i, :] = (lambdas**q) * np.exp(lambdas*zeta)

    # Choose m well-conditioned columns by pivoted QR.
    _, _, piv = qr(Awide, pivoting=True, mode='economic')
    idx = piv[:m]
    selected = lambdas[idx]
    A = Awide[:, idx]

    coeffs = np.linalg.solve(A, np.asarray(values, dtype=complex))
    residual = np.linalg.norm(A @ coeffs - values)

    return selected, coeffs, np.linalg.cond(A), residual

# Example: prescribe three simple zeros.
targets = [
    (5, 0.2 + 0.1j),
    (8, -0.3 + 0.25j),
    (11, 0.1 - 0.4j),
]

pairs = []
values = []
for n, zeta in targets:
    pairs.append((n, zeta))
    values.append(0.0)
    pairs.append((n+1, zeta))
    values.append(1.0)

lam, c, cond, residual = spectral_interpolant(
    pairs, values, R=10.0, number_candidates=1000
)

print("condition number:", cond)
print("residual:", residual)
```

The unresolved transition problem should be tested by certified winding numbers for two-ring sums:

```python
def ring(M, R, residue, z):
    om = cmath.exp(2j*math.pi/M)
    return sum((om**(j*residue)) * cmath.exp(R*(om**j)*z)
               for j in range(M))

def two_ring(A, M, R, r, B, N, S, q, z):
    return A*ring(M, R, r, z) + B*ring(N, S, q, z)

def winding_on_circle(func, center, radius, samples=20000):
    vals = []
    for k in range(samples + 1):
        theta = 2*math.pi*k/samples
        z = center + radius*cmath.exp(1j*theta)
        vals.append(func(z))
    if min(abs(v) for v in vals) < 1e-10:
        return None  # refine or use ball arithmetic
    return winding_number(vals)

# Sweep log|B/A| through a crossover range and test a grid of discs.
# For a rigorous check, replace floating point by Arb/Acb ball arithmetic.
```

The most important empirical question is whether two-ring sums retain zeros in every small disc throughout the full amplitude crossover, not merely when one ring dominates.

## Route Diagnosis

**Proved ledger**

1. A circular root-of-unity spectrum gives an explicit zero-covering radius, uniformly for every derivative order.
2. The zeros are simple and come with explicit Rouché contours and lower bounds.
3. Arbitrary finite derivative-value constraints can be interpolated by frequencies lying on any prescribed circle.
4. The Stokes geometry is not inherently too one-dimensional: although the tie set is a collection of radial rays, taking \(M\to\infty\) makes it dense on every fixed compact, while \(R\to\infty\) makes zeros dense along those rays.

**Plausible but unproved**

1. A transition-stable zero theorem for sums of two or several spectral rings.
2. A normally convergent choice of ring amplitudes for which every derivative order lies either in a one-ring regime or a controlled transition regime.
3. Quantitative versions of the finite interpolation lemma with coefficient bounds strong enough for infinite gluing.

**Dead ends**

1. **Fixed finite directional complexity:** with \(M\) fixed, the angular cell width is approximately \(K/M\), so arbitrarily small discs far from the origin can be missed.
2. **Separate Rouché dominance across adjacent derivative orders:** the inequality \(x e^{-x}\leq1/e\) obstructs preserving a coarse-ring zero at order \(n\) while making a much higher-frequency ring dominant at order \(n+1\).
3. **Pure finite interpolation without estimates:** exact solvability alone gives no normal convergence or protection of earlier zeros.

**Best next step**

The strongest continuation of Route 2 is to prove a two-ring transition lemma for (24), using the tropical upper envelope of all participating exponentials rather than treating one ring as a perturbation of the other. Nested root sets, for example \(M_s\mid M_{s+1}\), may preserve enough common angular geometry to make this tractable. If that fails, the finite interpolation lemma should be combined with a Route 1-style exact-correction construction, but only after deriving explicit coefficient-norm bounds.