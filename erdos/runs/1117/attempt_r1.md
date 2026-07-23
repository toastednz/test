STATUS: BLOCKED

## Result

The standard form of Route 1—patching annular models with \(q_k\)-fold equal maxima, where \(q_k\to\infty\)—is rigorously obstructed. I prove that if two equal stationary maximum branches remain related by a fixed rotation throughout any open radius interval, then the entire function has that rotational covariance globally. Consequently, if an annular template supplies a rotating or fixed regular \(q\)-gon of maxima on every circle of an annulus, the final entire function must have global \(q\)-fold covariance; such orders cannot be unbounded unless the function is a monomial. I also prove that arbitrarily accurate Runge approximation cannot preserve maximum multiplicity: \(1+z^q\) has \(q\) maxima on every circle, while the arbitrarily small perturbation \(1+\delta z+z^q\) has exactly one. However, persistent equal maxima do not always force symmetry: \(z^2+bz-1\) has two moving equal maxima on an open interval without nontrivial rotational covariance. Thus Route 1 is blocked precisely at the need for an exact patching mechanism using irregular, moving maximum branches; ordinary approximation, regular-polygon templates, and freezing values along arcs cannot provide it.

## Complete Argument

### 1. Rotated maximum branches force global rotational covariance

The following is the main obstruction.

**Lemma 1 (rotated-branch rigidity).**  
Let \(f\) be a nonzero entire function, let \(\omega\in\mathbb C\) satisfy \(|\omega|=1\), and let \(I\subset(0,\infty)\) be a nonempty open interval. Suppose that \(\theta:I\to\mathbb R\) is \(C^1\), and put
\[
z(r)=re^{i\theta(r)}.
\]
Assume that for every \(r\in I\),

1. \(f(z(r))\ne0\) and \(f(\omega z(r))\ne0\);
2. the two points are angular stationary points of \(|f|\):
   \[
   \frac{\partial}{\partial\phi}\log|f(re^{i\phi})|
   \bigg|_{\phi=\theta(r)}=0,
   \]
   \[
   \frac{\partial}{\partial\phi}\log|f(re^{i\phi})|
   \bigg|_{\phi=\theta(r)+\arg\omega}=0;
   \]
3. they have equal modulus:
   \[
   |f(\omega z(r))|=|f(z(r))|.
   \]

Then there is a constant \(c\), with \(|c|=1\), such that
\[
f(\omega z)=c f(z)\qquad\text{for all }z\in\mathbb C.
\]

**Proof.**  
Near every point of the curve \(z(r)\), define
\[
Q(z)=\frac{f(\omega z)}{f(z)}.
\]
This is holomorphic and nonzero there. Set
\[
v(r,\phi)
=
\log|Q(re^{i\phi})|
=
\log|f(\omega re^{i\phi})|-\log|f(re^{i\phi})|.
\]
The equal-modulus hypothesis gives
\[
v(r,\theta(r))=0.
\]
The two angular stationarity hypotheses give
\[
v_\phi(r,\theta(r))=0.
\]
Differentiating \(v(r,\theta(r))=0\) with respect to \(r\) yields
\[
v_r(r,\theta(r))+\theta'(r)v_\phi(r,\theta(r))=0,
\]
hence
\[
v_r(r,\theta(r))=0.
\]

For \(z=re^{i\phi}\), put
\[
A(z)=z\frac{Q'(z)}{Q(z)}.
\]
The Cauchy–Riemann equations, or direct differentiation, give
\[
r v_r=\operatorname{Re}A,
\qquad
v_\phi=\operatorname{Re}(iA)=-\operatorname{Im}A.
\]
Thus at every \(z(r)\),
\[
\operatorname{Re}A(z(r))=\operatorname{Im}A(z(r))=0,
\]
so \(Q'(z(r))=0\).

Equivalently,
\[
W(z(r))=0,
\]
where
\[
W(z)
=
\omega f'(\omega z)f(z)-f(\omega z)f'(z).
\]
The function \(W\) is entire. Since the curve \(z(I)\) has an accumulation point in \(\mathbb C\), the identity theorem gives \(W\equiv0\).

Choose one point \(z_0\) with \(f(z_0)\ne0\). On a neighborhood of \(z_0\),
\[
\left(\frac{f(\omega z)}{f(z)}\right)'=0,
\]
so \(f(\omega z)=c f(z)\) there for some constant \(c\). The entire function
\[
f(\omega z)-c f(z)
\]
therefore vanishes identically. The original equal-modulus condition gives \(|c|=1\). ∎

At a global maximum point of a nonzero entire function, \(f\) cannot vanish: otherwise the maximum modulus on that circle would be zero and \(f\) would vanish on the whole circle, hence identically. Global maxima are angular stationary points. Therefore Lemma 1 applies directly to maximum branches.

---

### 2. Regular polygonal annular templates cannot be localized

**Corollary 2.**  
Let \(\omega=e^{2\pi i/q}\), where \(q\ge2\). Suppose there are an open interval \(I\) and a \(C^1\) function \(\theta:I\to\mathbb R\) such that
\[
re^{i\theta(r)}\omega^j\in S_f(r)
\qquad
(j=0,\dots,q-1,\ r\in I).
\]
Then
\[
f(\omega z)=c f(z)
\]
for some \(|c|=1\). Consequently, the Taylor support of \(f\) lies in one residue class modulo \(q\):
\[
f(z)=z^m G(z^q)
\]
for some \(m\in\{0,\dots,q-1\}\) and an entire \(G\).

**Proof.**  
Apply Lemma 1 to the branches \(z(r)\) and \(\omega z(r)\). If
\[
f(z)=\sum_{n=0}^\infty a_nz^n,
\]
then
\[
\sum_n a_n\omega^n z^n
=
c\sum_n a_nz^n.
\]
Thus
\[
a_n\ne0\implies \omega^n=c.
\]
All indices in the support are therefore congruent modulo \(q\). ∎

This includes both fixed and rotating regular polygons: the common orientation \(\theta(r)\) may vary arbitrarily, provided it is \(C^1\).

**Corollary 3 (unbounded regular-polygon orders force a monomial).**  
Suppose one entire function \(f\) admits, on open radius intervals \(I_k\), regular \(q_k\)-gons of maximum points as in Corollary 2, where \(q_k\to\infty\). Then \(f\) is a monomial.

**Proof.**  
If \(a_m,a_n\ne0\), Corollary 2 implies
\[
q_k\mid(n-m)
\]
for every \(k\). If \(m\ne n\), this is impossible once \(q_k>|n-m|\). Hence the Taylor series has at most one nonzero coefficient. ∎

Therefore the most natural Route 1 templates—such as \(1+z^{q_k}\), regular polygonal zero shells, or any annular model whose designated maxima form a regular \(q_k\)-gon—cannot be installed exactly on successive annuli with \(q_k\to\infty\).

---

### 3. Exact modulus symmetry on one annulus is already global

There is an even simpler obstruction if a patching construction attempts to make the whole angular modulus profile symmetric.

**Lemma 4 (annular modulus symmetry is global).**  
Let
\[
A=\{z:r_0<|z|<r_1\}
\]
and let \(f\) be holomorphic on a connected rotation-invariant domain containing \(A\). If
\[
|f(\omega z)|=|f(z)|\qquad(z\in A),
\]
then
\[
f(\omega z)=c f(z)
\]
on the whole connected domain, for some \(|c|=1\).

**Proof.**  
The modulus identity shows that \(f(z)=0\) if and only if \(f(\omega z)=0\). Their vanishing orders also agree: comparing the local leading terms in the modulus identity forces the orders to be equal. Hence
\[
Q(z)=\frac{f(\omega z)}{f(z)}
\]
extends holomorphically and without zeros across the zeros of \(f\) in \(A\). It satisfies \(|Q|=1\) throughout \(A\). By the open mapping theorem, \(Q\) is constant on \(A\). The identity theorem extends
\[
f(\omega z)=c f(z)
\]
to the connected domain. ∎

Thus one cannot impose an exact \(q\)-fold modulus identity merely on an annulus and hope that it remains localized there.

---

### 4. Multiplicative corrections preserving polygonal maxima inherit the symmetry

A common patching idea is to multiply an existing function by a correction close to \(1\).

**Corollary 5.**  
Suppose \(f\) has equal stationary branches \(z(r)\) and \(\omega z(r)\) as in Lemma 1. Let \(h\) be entire, and suppose that \(fh\) has the same two branches as equal stationary nonzero points. Then
\[
h(\omega z)=c h(z)
\]
for some \(|c|=1\).

**Proof.**  
Since both \(f\) and \(fh\) have equal moduli at the two branches,
\[
|h(\omega z(r))|=|h(z(r))|.
\]
Since both \(f\) and \(fh\) are angular stationary there,
\[
\partial_\phi\log|h(re^{i\phi})|=0
\]
at both branches. Lemma 1 applied to \(h\) gives the result. ∎

Therefore a multiplicative correction cannot preserve a regular \(q\)-gon of designated maxima while breaking or localizing the corresponding symmetry.

---

### 5. Uniform approximation does not preserve exact maximum multiplicity

**Lemma 6 (arbitrarily small perturbations collapse all ties).**  
For every integer \(q\ge2\),
\[
F_0(z)=1+z^q
\]
has exactly \(q\) maximum-modulus points on every circle. For every \(\delta>0\),
\[
F_\delta(z)=1+\delta z+z^q
\]
has exactly one maximum-modulus point on every circle.

Moreover, \(F_\delta\to F_0\) uniformly on every compact set as \(\delta\downarrow0\).

**Proof.**  
For \(|z|=r\),
\[
|1+z^q|\le1+r^q.
\]
Equality holds exactly when \(z^q=r^q\), equivalently
\[
z=re^{2\pi ij/q},\qquad j=0,\dots,q-1.
\]
Thus \(\nu_{F_0}(r)=q\).

For \(F_\delta\),
\[
|1+\delta z+z^q|
\le 1+\delta r+r^q.
\]
Equality in the triangle inequality requires the three nonzero summands to have the same argument. Since the first summand is the positive number \(1\), this requires
\[
e^{i\theta}=1.
\]
That condition also implies \(e^{iq\theta}=1\). Hence equality occurs only at \(z=r\), and
\[
\nu_{F_\delta}(r)=1.
\]

Finally, on a compact set \(K\),
\[
\sup_{z\in K}|F_\delta(z)-F_0(z)|
\le \delta\sup_{z\in K}|z|\longrightarrow0.
\]
∎

This rules out any proof that invokes Runge, Arakelian, or chaplet approximation and then claims that sufficiently accurate approximation preserves equal peak heights. Such approximation can preserve separated peak neighborhoods and local maxima, but not equality of their global values.

---

### 6. Freezing complex values on a maximum arc also fails

Suppose an inductive construction attempts to protect previous maxima by requiring every later additive correction \(h\) to vanish at those points.

If a maximum branch \(z(r)\) is continuous and nonconstant on an open interval and
\[
h(z(r))=0\qquad(r\in I),
\]
then \(h\equiv0\) by the identity theorem. Thus no nontrivial holomorphic correction can preserve even one continuum of previous complex values exactly.

Preserving only moduli is less rigid, but Corollary 5 shows that preserving polygonal maximum branches multiplicatively forces global covariance.

---

### 7. Persistent equal maxima need not come from rotations

The preceding rigidity cannot be extended to arbitrary moving maximum branches.

**Lemma 7 (a nonsymmetric persistent pair).**  
Let \(b>0\) and
\[
p_b(z)=z^2+bz-1.
\]
For every \(r>0\) satisfying
\[
\left|\frac{b(r^2-1)}{4r}\right|<1,
\]
the function \(p_b\) has exactly two maximum-modulus points on \(|z|=r\), at
\[
\theta=\pm\arccos\!\left(\frac{b(r^2-1)}{4r}\right).
\]
The polynomial has no nontrivial rotational covariance.

**Proof.**  
Write \(z=re^{i\theta}\) and \(x=\cos\theta\). Direct expansion gives
\[
\begin{aligned}
|p_b(re^{i\theta})|^2
={}&r^4+b^2r^2+1
   +2br(r^2-1)\cos\theta
   -2r^2\cos2\theta\\
={}&r^4+b^2r^2+1+2r^2
   -4r^2x^2+2br(r^2-1)x.
\end{aligned}
\]
As a function of \(x\in[-1,1]\), this is a strictly concave quadratic whose unique maximizing value is
\[
x_0=\frac{b(r^2-1)}{4r}.
\]
If \(|x_0|<1\), exactly two angles in \([0,2\pi)\) have cosine \(x_0\), namely
\[
\theta=\pm\arccos x_0.
\]
They are therefore exactly the two global maximum points.

The Taylor support of \(p_b\) is \(\{0,1,2\}\). If
\[
p_b(\omega z)=c\,p_b(z),
\]
comparison of the constant and linear coefficients gives \(c=1\) and \(\omega=1\). Hence there is no nontrivial rotational covariance. ∎

The two branches are related by complex conjugation, and their angular separation varies with \(r\). This is a concrete counterexample to any proposed lemma asserting that persistent multiple maxima automatically imply rotational symmetry.

---

### 8. A structural identity for arbitrary smooth maximum branches

Although arbitrary moving branches need not give a rotation, they satisfy a strong logarithmic-derivative condition.

**Lemma 8.**  
Let \(I\) be an interval and suppose
\[
z_j(r)=re^{i\theta_j(r)},\qquad j=1,\dots,N,
\]
are \(C^1\) branches of global maximum points of a nonzero entire function \(f\). Then
\[
\frac{z_j(r)f'(z_j(r))}{f(z_j(r))}
=
r\frac{d}{dr}\log M_f(r)
\]
for every \(j\). In particular, all these logarithmic-derivative values are the same real number.

**Proof.**  
At an angular maximum,
\[
\operatorname{Im}\!\left(\frac{z_jf'(z_j)}{f(z_j)}\right)=0.
\]
Set
\[
G(z)=\frac{zf'(z)}{f(z)}.
\]
Since
\[
z_j'(r)=z_j(r)\left(\frac1r+i\theta_j'(r)\right),
\]
we have
\[
\frac{d}{dr}\log|f(z_j(r))|
=
\operatorname{Re}\left(
\frac{f'(z_j)}{f(z_j)}z_j'
\right)
=
\operatorname{Re}\left(
G(z_j)\left(\frac1r+i\theta_j'\right)
\right).
\]
Because \(G(z_j)\) is real, this equals \(G(z_j)/r\). But
\[
|f(z_j(r))|=M_f(r),
\]
so
\[
G(z_j(r))=r\frac{d}{dr}\log M_f(r),
\]
independently of \(j\). ∎

Thus any successful irregular patch must arrange, on every active circle, many points of equal modulus that are also distinct preimages of one common real value of \(zf'/f\). Ordinary uniform approximation does not enforce either exact condition.

---

### 9. Ledger

#### Proved

1. Equal stationary branches related by a fixed rotation on an interval force global rotational covariance.
2. A regular \(q\)-gon of maxima on an annulus forces the Taylor support into one residue class modulo \(q\).
3. Unbounded regular-polygon orders force a monomial.
4. Exact modulus symmetry on one open annulus extends globally.
5. Multiplicative corrections preserving regular polygonal maxima inherit the same covariance.
6. Arbitrarily small perturbations can reduce \(q\) exact maxima to one on every circle.
7. Persistent moving equal maxima can occur without rotational symmetry.
8. Smooth equal maximum branches share the same value of \(zf'/f\).

#### Plausible but unproved

1. There may be a stronger rigidity theorem for \(N\ge3\) irregular moving maximum branches, but Lemma 7 shows that no such theorem can merely say “persistent ties imply symmetry.”
2. An exact interpolation theorem for real parts or moduli along several moving curves might conceivably repair Route 1, but standard Runge/Arakelian approximation does not provide it.
3. The common-value condition in Lemma 8 may be strong enough, together with global maximality, to give a negative theorem; no argument was found that controls the births, deaths, and exchanges of branches.

#### Dead ends

1. **Successive regular-polygon templates:** ruled out by Corollary 3.
2. **Exact annular modulus symmetrization:** ruled out by Lemma 4.
3. **Preserving old maxima by vanishing corrections:** the identity theorem forces the correction to be zero.
4. **Preserving old polygonal maxima multiplicatively:** the correction must have global covariance.
5. **Relying on arbitrarily accurate approximation:** ruled out by Lemma 6.
6. **Claiming all persistent ties arise from symmetry:** refuted by Lemma 7.

## Self-Audit

1. **The rigidity theorem assumes \(C^1\) maximum branches.**  
   A hypothetical solution could exploit degenerate maxima and repeated branch bifurcations so that no useful regular-polygon branch persists smoothly. The theorem nevertheless holds exactly under its stated assumptions by differentiating the equal-modulus identity and applying the identity theorem. In particular, it covers the strict, smoothly designated peak branches normally required by annular patching.

2. **The obstruction only rules out maxima related by a fixed rotation.**  
   It does not control irregular moving configurations; Lemma 7 explicitly shows why such a limitation is necessary. Thus the argument is not a disproof of Question 2. The claimed blockage is still valid for the proposed regular-polygon and symmetric-template implementations of Route 1.

3. **Failure of approximation does not prove failure of an exact nonlinear interpolation scheme.**  
   Lemma 6 shows that approximation alone is logically insufficient, not that no carefully tuned correction exists. I regard the route as blocked because the missing exact interpolation lemma must simultaneously enforce equal values, stationarity, global dominance, preservation of all previous annuli, and transition control; none of the standard approximation theorems supplies these closed, continuum-sized constraints.

## Computations To Verify

The following symbolic check verifies Lemma 7.

```python
import sympy as sp

r, b, th = sp.symbols('r b th', positive=True, real=True)
z = r * sp.exp(sp.I * th)
p = z**2 + b*z - 1

H = sp.expand_complex(p * sp.conjugate(p))
H_expected = (
    r**4 + b**2*r**2 + 1
    + 2*b*r*(r**2 - 1)*sp.cos(th)
    - 2*r**2*sp.cos(2*th)
)

print(sp.simplify(sp.trigsimp(H - H_expected)))  # should print 0

x = sp.symbols('x', real=True)
Hx = (
    r**4 + b**2*r**2 + 1 + 2*r**2
    - 4*r**2*x**2 + 2*b*r*(r**2 - 1)*x
)
x0 = sp.solve(sp.diff(Hx, x), x)[0]
print(sp.simplify(x0))                 # b*(r**2 - 1)/(4*r)
print(sp.diff(Hx, x, 2))              # -8*r**2 < 0
```

This numerically counts stationary global maxima of a polynomial on a circle. It can test candidate irregular templates, though floating-point ties must later be certified symbolically.

```python
import numpy as np
from math import pi

def poly_value(a, z):
    # a[n] is coefficient of z^n
    return sum(a[n] * z**n for n in range(len(a)))

def stationary_angles(a, r, tol_circle=1e-7, tol_angle=1e-7):
    """
    Roots the Laurent polynomial for d/dtheta |p(re^{i theta})|^2.
    Numerical only.
    """
    d = len(a) - 1
    # After multiplying by w^d and omitting the harmless factor i:
    # P(w) = sum_{n,m} (n-m) a_n conjugate(a_m)
    #        r^(n+m) w^(n-m+d)
    P = np.zeros(2*d + 1, dtype=complex)  # ascending powers
    for n, an in enumerate(a):
        for m, am in enumerate(a):
            P[n - m + d] += (
                (n - m) * an * np.conjugate(am) * r**(n + m)
            )

    while len(P) > 1 and abs(P[-1]) < 1e-14:
        P = P[:-1]

    roots = np.roots(P[::-1])
    angles = []
    for w in roots:
        if abs(abs(w) - 1) < tol_circle:
            w = w / abs(w)
            t = np.angle(w) % (2*pi)
            if all(abs(np.angle(np.exp(1j*(t-s)))) > tol_angle
                   for s in angles):
                angles.append(t)
    return sorted(angles)

def numerical_nu(a, r, tol_height=1e-7):
    angles = stationary_angles(a, r)
    vals = np.array([
        abs(poly_value(a, r*np.exp(1j*t))) for t in angles
    ])
    if len(vals) == 0:
        return 0, [], []
    vmax = vals.max()
    winners = [
        t for t, v in zip(angles, vals)
        if abs(v - vmax) <= tol_height * max(1.0, vmax)
    ]
    return len(winners), winners, vals

# 1 + z^q versus 1 + delta*z + z^q
for q in [3, 5, 8]:
    a0 = [1] + [0]*(q-1) + [1]
    ad = [1, 1e-4] + [0]*(q-2) + [1]
    for r in [0.5, 1.0, 2.0]:
        print("q,r =", q, r,
              "baseline:", numerical_nu(a0, r)[0],
              "perturbed:", numerical_nu(ad, r)[0])

# z^2 + b*z - 1 on the interval |b(r^2-1)/(4r)| < 1
b = 1.0
a = [-1, b, 1]
for r in np.linspace(0.4, 2.0, 9):
    x0 = b*(r*r - 1)/(4*r)
    if abs(x0) < 1:
        print("moving pair", r, x0, numerical_nu(a, r)[0])
```

The following search probes the main unresolved finite-stage question: whether a real polynomial with support gcd \(1\) can have at least four persistent maxima, corresponding to at least two distinct maximizing values of \(x=\cos\theta\), over a substantial radius interval.

```python
import itertools
import numpy as np
from math import gcd
from functools import reduce

def support_gcd(a):
    E = [n for n, c in enumerate(a) if abs(c) > 1e-14]
    if len(E) <= 1:
        return 0
    base = E[0]
    return reduce(gcd, [n-base for n in E[1:]])

radii = np.linspace(0.7, 1.3, 13)
values = [-2, -1, 0, 1, 2]

for degree in range(3, 7):
    for coeffs in itertools.product(values, repeat=degree+1):
        if coeffs[-1] == 0 or sum(c != 0 for c in coeffs) < 2:
            continue
        if support_gcd(coeffs) != 1:
            continue

        counts = [numerical_nu(coeffs, r, tol_height=1e-6)[0]
                  for r in radii]
        if min(counts) >= 4:
            print("candidate:", coeffs, counts)
            # Any output is only a candidate. It must next be checked
            # by exact resultant/CAD calculations.
```

For any candidate \(p\) with real coefficients, an exact follow-up is:

1. Express
   \[
   H(r,x)=|p(re^{i\theta})|^2,\qquad x=\cos\theta,
   \]
   as a polynomial in \(r,x\).
2. Form
   \[
   H_x(r,x)=0,\qquad H_x(r,y)=0,\qquad H(r,x)-H(r,y)=0.
   \]
3. Eliminate \(x,y\) by resultants.
4. Check whether a positive-dimensional component projects onto an open \(r\)-interval.
5. Prove with Sturm sequences or cylindrical algebraic decomposition that both \(x,y\in(-1,1)\) are global, not merely local, maximizers throughout that interval.

This computation would test whether irregular persistent multi-peak templates exist even at a finite polynomial stage.

## Route Diagnosis

Route 1 succeeds only at producing approximate or locally separated peaks. It fails at the exact-equality step. Regular \(q\)-fold templates cannot be patched annulus by annulus because even one open annulus of rotationally related maximum branches forces global covariance; unbounded covariance orders force a monomial. Uniform holomorphic approximation cannot repair this because exact ties are destroyed by arbitrarily small perturbations. Literal interpolation or freezing of complex values along old maximum arcs is prohibited by the identity theorem.

The remaining possibility is substantially different: construct annular templates with many **irregular, moving** maximum branches, no pair of which remains related by a fixed rotation, and devise corrections that solve the continuum of equal-value and stationarity equations exactly while preserving all earlier annuli. Lemma 8 shows that this requires many points on each circle satisfying
\[
\frac{zf'(z)}{f(z)}=L(r)\in\mathbb R
\]
and having exactly equal modulus. No available Runge-, Arakelian-, or chaplet-type theorem enforces these nonlinear identities.

A fresh attempt should therefore abandon regular polygons and investigate the real-analytic equal-critical-value locus of \(zf'/f\). The most useful immediate finite problem is to classify polynomials having at least three or four persistent irregular global maxima on an open radius interval without rotational covariance. If no such examples exist, a rigidity theorem along Routes 4 or 6 may be possible. If they do exist, their algebraic mechanism may supply the missing exact annular template for a renewed Route 1 construction.