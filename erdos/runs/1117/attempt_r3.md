STATUS: BLOCKED

## Result

Route 3 does not currently yield a solution of Question 2. I proved several rigorous obstructions to the standard lacunary/Newton-polygon strategy. First, any construction based on simultaneous phase alignment has a fixed number of maxima equal to the gcd of the exponent differences. Second, arbitrarily small symmetry-breaking monomials can reduce a \(q\)-peak binomial to a unique maximum on every circle. Third, if \(q\) fixed equally spaced angular locations remain global maxima throughout any open radius interval, then the entire function has exact global \(q\)-fold rotational covariance; hence one nonmonomial entire function cannot realize fixed-spoke templates of unbounded orders on successive annuli. A perturbation theorem quantifies how the first nondominant exponent splits the \(q\) binomial peaks. The unresolved possibility is that many equal maxima move irregularly with the radius. Persistent moving branches satisfy strong equal-value constraints for \(zf'/f\), but these constraints do not presently force rotational symmetry, and an explicit polynomial example shows that even two persistent moving maxima need not come from rotation.

## Complete Argument

### 1. Phase-alignment constructions have fixed multiplicity

Let

\[
f(z)=\sum_{n\ge 0}a_nz^n
\]

be entire and nonmonomial, and let

\[
E=\{n\ge0:a_n\ne0\}.
\]

Define

\[
d=\gcd\{n-m:n,m\in E\}.
\]

Since \(E\) contains at least two elements, \(d\) is a finite positive integer.

#### Lemma 1

Suppose that for some \(r>0\) and \(\theta_0\), all nonzero terms

\[
a_nr^ne^{in\theta_0},\qquad n\in E,
\]

have the same argument. Then

\[
\nu_f(r)=d.
\]

In particular, if the same phase-alignment condition is available for every \(r\), then \(\nu_f(r)=d\) for every \(r>0\).

#### Proof

Absolute convergence gives

\[
|f(re^{i\theta})|
\le \sum_{n\in E}|a_n|r^n.
\]

At \(\theta=\theta_0\), all terms point in the same direction, so equality holds. Thus

\[
M_f(r)=\sum_{n\in E}|a_n|r^n.
\]

Equality in the triangle inequality for an absolutely convergent sum holds only when all nonzero summands have the same argument. Indeed, if \(S=\sum x_n\) and \(|S|=\sum|x_n|\), multiply by \(\overline S/|S|\). Then

\[
\sum_n\left(|x_n|-\operatorname{Re}\left(\frac{\overline S}{|S|}x_n\right)\right)=0,
\]

and every summand is nonnegative, so each is zero.

Consequently, another angle \(\theta\) is a maximum angle exactly when

\[
e^{i(n-m)(\theta-\theta_0)}=1
\qquad\text{for all }n,m\in E.
\]

By the definition of \(d\), this is equivalent to

\[
d(\theta-\theta_0)\in2\pi\mathbb Z.
\]

There are exactly \(d\) such angles modulo \(2\pi\). ∎

#### Corollary 1

If all nonzero coefficients \(a_n\) are nonnegative real numbers, then

\[
\nu_f(r)=d
\qquad\text{for every }r>0.
\]

Thus no positive-coefficient lacunary series can answer Question 2.

More generally, this applies whenever the coefficient phases can be made simultaneous by one angular rotation and one scalar multiplication.

---

### 2. Norm dominance cannot preserve exact peak equality

A dominant binomial may have \(q\) equal maxima, but an arbitrarily small term can destroy all but one.

#### Proposition 2

For every integer \(q\ge2\) and every \(\varepsilon>0\), the polynomial

\[
f_\varepsilon(z)=1+\varepsilon z+z^q
\]

has exactly one maximum-modulus point on every circle \(|z|=r\), \(r>0\).

#### Proof

All three coefficients are positive. The exponent support is \(\{0,1,q\}\), whose difference gcd is \(1\). Lemma 1 therefore gives

\[
\nu_{f_\varepsilon}(r)=1
\]

for every \(r>0\). Explicitly, the unique maximum point is \(z=r\). ∎

On any fixed compact annulus \(a\le |z|\le b\),

\[
|\varepsilon z|\le \varepsilon b,
\]

so the perturbation can be made arbitrarily small uniformly while changing the number of maxima from \(q\) for \(1+z^q\) to \(1\).

Therefore no phase-locking lemma of the form

> “If a \(q\)-peak block dominates the remaining terms sufficiently strongly in norm, then the full function retains \(q\) equal global maxima”

can be true without additional exact identities.

---

### 3. Fixed persistent maximum rays force global covariance

The preceding counterexample suggests that exact equality must come from an identity. The following makes this precise for fixed angular locations.

Write

\[
G(z)=\frac{zf'(z)}{f(z)}
\]

where \(f(z)\ne0\).

#### Lemma 3: fixed-ray covariance

Let \(I\subset(0,\infty)\) be a nonempty open interval, and let \(\theta,\phi\) be fixed angles. Suppose that for every \(r\in I\),

1. \(re^{i\theta}\) and \(re^{i\phi}\) are angular critical points of \(|f|\), and
2. their moduli are equal:
   \[
   |f(re^{i\theta})|=|f(re^{i\phi})|.
   \]

Then there is a constant \(c\), \(|c|=1\), such that

\[
f(e^{i\phi}z)=c\,f(e^{i\theta}z)
\qquad\text{for all }z\in\mathbb C.
\]

Equivalently,

\[
f(e^{i(\phi-\theta)}w)=c\,f(w)
\qquad\text{for all }w\in\mathbb C.
\]

#### Proof

Neither value can vanish on \(I\). If, for example, \(f(re^{i\theta})=0\), then the common value would be zero. If these points are global maxima this immediately forces \(f\equiv0\); under the present critical-point hypotheses, we may simply restrict to a component of \(I\) avoiding isolated zeros. The resulting identity then extends to all of \(I\), and hence globally, by analytic continuation.

For \(z=re^{i\theta}\),

\[
\frac{\partial}{\partial\theta}\log|f(re^{i\theta})|
=-\operatorname{Im}G(re^{i\theta}).
\]

Thus angular criticality gives

\[
\operatorname{Im}G(re^{i\theta})=0.
\]

On the other hand,

\[
\frac{d}{dr}\arg f(re^{i\theta})
=
\operatorname{Im}\left(e^{i\theta}\frac{f'(re^{i\theta})}{f(re^{i\theta})}\right)
=
\frac1r\operatorname{Im}G(re^{i\theta})
=0.
\]

Hence \(f(re^{i\theta})\) has constant argument as \(r\) varies in \(I\). There is an \(\alpha\in\mathbb R\) such that

\[
A(z):=e^{-i\alpha}f(e^{i\theta}z)
\]

is real-valued for real \(z\in I\). By the identity theorem applied to

\[
A(z)-\overline{A(\overline z)},
\]

the entire function \(A\) has real Taylor coefficients.

Likewise there is a \(\beta\) such that

\[
B(z):=e^{-i\beta}f(e^{i\phi}z)
\]

has real Taylor coefficients. The equal-modulus hypothesis gives, for \(r\in I\),

\[
A(r)^2=B(r)^2.
\]

Thus the entire function \(A^2-B^2\) vanishes on an interval, so

\[
(A-B)(A+B)\equiv0.
\]

The ring of entire functions is an integral domain; consequently either \(A\equiv B\) or \(A\equiv-B\). Therefore

\[
f(e^{i\phi}z)=\pm e^{i(\beta-\alpha)}f(e^{i\theta}z),
\]

which is the claimed identity. ∎

#### Corollary 3: fixed \(q\)-spoke templates are global symmetries

Suppose that for every \(r\) in an open interval \(I\), all the fixed points

\[
re^{i(\theta_0+2\pi j/q)},\qquad j=0,\dots,q-1,
\]

are global maximum-modulus points. Then

\[
f(e^{2\pi i/q}z)=c f(z)
\]

for some \(|c|=1\). Consequently, all nonzero Taylor coefficients of \(f\) have exponents in one residue class modulo \(q\), and

\[
f(z)=z^m g(z^q)
\]

for some entire \(g\).

#### Proof

Global maxima are angular critical points. Apply Lemma 3 to the first two fixed rays. Expanding

\[
\sum_n a_ne^{2\pi in/q}z^n
=
c\sum_n a_nz^n
\]

shows that

\[
e^{2\pi in/q}=c
\]

for every \(n\in E\). Thus all exponents in \(E\) are congruent modulo \(q\). ∎

#### Corollary 4: unbounded fixed-spoke orders are impossible

A nonmonomial entire function cannot possess fixed equally spaced maximum spokes of orders \(q_k\to\infty\) on successive open radius intervals.

#### Proof

Choose two distinct exponents \(m,n\in E\). Corollary 3 would imply

\[
q_k\mid n-m
\]

for every \(k\). This is impossible once \(q_k>|n-m|\). ∎

This directly rules out the most natural lacunary construction in which a dominant binomial supplies \(q_k\) fixed phase-alignment directions and all other terms are expected to preserve those directions exactly.

---

### 4. First-order splitting of a dominant binomial

The next result identifies the peak-splitting effect of the first symmetry-breaking term.

#### Lemma 5: perturbative splitting

Let \(A,C>0\), \(D\ne0\), \(q\ge2\), and \(s\in\mathbb Z\). Define

\[
F_\varepsilon(\theta)
=
A+Ce^{iq\theta}+\varepsilon De^{is\theta},
\qquad \varepsilon\ge0.
\]

Let

\[
d=\gcd(q,s),
\]

with \(\gcd(q,0)=q\). For all sufficiently small \(\varepsilon>0\), every global maximum of \(|F_\varepsilon|\) lies near one of the unperturbed points

\[
\theta_j=\frac{2\pi j}{q},
\qquad j=0,\dots,q-1.
\]

Moreover, if \(s\not\equiv0\pmod q\), then

\[
\nu_{F_\varepsilon}\le 2d
\]

for sufficiently small \(\varepsilon\). For generic phases of \(D\),

\[
\nu_{F_\varepsilon}=d.
\]

#### Proof

Set

\[
H_\varepsilon(\theta)=|F_\varepsilon(\theta)|^2.
\]

At \(\varepsilon=0\),

\[
H_0(\theta)=A^2+C^2+2AC\cos(q\theta).
\]

Its global maxima are exactly the \(q\) points \(\theta_j\), and they are nondegenerate since

\[
H_0''(\theta_j)=-2ACq^2<0.
\]

Choose pairwise disjoint neighborhoods \(U_j\) of these points so that \(H_0''<0\) throughout each \(U_j\), and so that \(H_0\) has a strict gap below its maximum outside their union. For sufficiently small \(\varepsilon\), the strict gap persists, every global maximum lies in some \(U_j\), and the implicit function theorem gives a unique local maximum

\[
\theta_j(\varepsilon)\in U_j.
\]

Let

\[
V_j(\varepsilon)=H_\varepsilon(\theta_j(\varepsilon)).
\]

Because \(\partial_\theta H_0(\theta_j)=0\),

\[
V_j'(0)
=
\left.\partial_\varepsilon H_\varepsilon(\theta_j)\right|_{\varepsilon=0}
=
2(A+C)\operatorname{Re}\left(De^{2\pi isj/q}\right).
\]

Define

\[
L_j=\operatorname{Re}\left(De^{2\pi isj/q}\right).
\]

If \(L_j\) is strictly less than \(\max_kL_k\), then

\[
V_j(\varepsilon)
<
\max_kV_k(\varepsilon)
\]

for all sufficiently small positive \(\varepsilon\). Thus only indices maximizing \(L_j\) can give global maxima.

The points \(e^{2\pi isj/q}\) run through the vertices of a regular polygon of order \(q/d\), each repeated \(d\) times. A nonzero real linear functional on the vertices of a regular polygon is maximized at at most two vertices. Therefore at most \(2d\) indices maximize \(L_j\). Except when the direction determined by \(D\) is normal to an edge of that polygon, exactly one polygon vertex maximizes the functional, giving exactly \(d\) indices.

Finally, all frequencies \(0,q,s\) are divisible by \(d\), so the profile has exact period \(2\pi/d\). Hence in the generic case the \(d\) surviving maxima have exactly equal heights, establishing \(\nu=d\). ∎

The same conclusion remains valid with an additional remainder \(R_\varepsilon(\theta)\) satisfying

\[
\|R_\varepsilon\|_{C^2}=o(\varepsilon):
\]

the maxima stay in the same neighborhoods, their locations move by \(O(\varepsilon)\), and their peak values have the same first-order expansion.

This is precisely the behavior expected in a strongly hierarchical lacunary series: after selecting a dominant binomial, the first term whose exponent is not congruent modulo the binomial gap selects only one or two residue classes of the nominal peaks. The threshold, however, depends on \(q,s,A,C,D\); this does not by itself prove a theorem for all lacunary series.

---

### 5. What persistent moving maxima imply

The fixed-ray theorem does not apply if the maximum points move with \(r\). There is nevertheless a useful exact constraint.

#### Lemma 6: equal logarithmic-derivative values

Let

\[
z_j(r)=re^{i\theta_j(r)},\qquad j=1,\dots,N,
\]

be \(C^1\) branches on an interval \(I\). Suppose that each \(z_j(r)\) is an angular critical point and that

\[
|f(z_1(r))|=\cdots=|f(z_N(r))|>0
\]

throughout \(I\). Then

\[
\frac{z_1(r)f'(z_1(r))}{f(z_1(r))}
=
\cdots=
\frac{z_N(r)f'(z_N(r))}{f(z_N(r))}
\in\mathbb R.
\]

#### Proof

Angular criticality gives

\[
G(z_j(r))=\frac{z_j(r)f'(z_j(r))}{f(z_j(r))}\in\mathbb R.
\]

Also,

\[
\frac{z_j'(r)}{z_j(r)}
=
\frac1r+i\theta_j'(r).
\]

Therefore

\[
\frac{d}{dr}\log|f(z_j(r))|
=
\operatorname{Re}\left(
\frac{f'(z_j(r))}{f(z_j(r))}z_j'(r)
\right)
=
\operatorname{Re}\left(
G(z_j(r))\left(\frac1r+i\theta_j'(r)\right)
\right)
=
\frac{G(z_j(r))}{r}.
\]

The logarithmic moduli are equal throughout \(I\), so their derivatives are equal. Hence all values \(G(z_j(r))\) coincide. ∎

Thus \(N\) persistent equal maximum branches give \(N\) points on the same circle at which the meromorphic function \(zf'/f\) takes the same real value. No known theorem bounds such configurations uniformly for arbitrary entire \(f\).

---

### 6. Moving persistent maxima need not come from rotation

A tempting extension of Lemma 3 would assert that any persistent equal maxima force rotational covariance. That statement is false.

#### Proposition 7

For

\[
p(z)=1+z-z^2,
\]

there are exactly two global maximum-modulus points on every circle with

\[
\sqrt5-2<r<\sqrt5+2,
\]

and their angles move nontrivially with \(r\). The polynomial has no nontrivial rotational covariance.

#### Proof

Writing \(x=\cos\theta\),

\[
\begin{aligned}
|p(re^{i\theta})|^2
&=1+r^2+r^4+2r(1-r^2)\cos\theta-2r^2\cos2\theta\\
&=1+3r^2+r^4+2r(1-r^2)x-4r^2x^2.
\end{aligned}
\]

As a function of \(x\in[-1,1]\), this is a strictly concave quadratic with vertex

\[
x_*(r)=\frac{1-r^2}{4r}.
\]

The condition \(|x_*(r)|<1\) is exactly

\[
\sqrt5-2<r<\sqrt5+2.
\]

On this interval there are exactly two angles modulo \(2\pi\) satisfying

\[
\cos\theta=x_*(r),
\]

and they are the two global maxima. Since \(x_*(r)\) is nonconstant, the angles move with \(r\).

If \(p(\omega z)=cp(z)\), comparison of the constant coefficients gives \(c=1\), and comparison of the linear coefficients then gives \(\omega=1\). Thus there is no nontrivial rotational covariance. ∎

This example identifies the precise block: persistent moving equal branches can be maintained by reflection-type identities without fixed rays, and Lemma 3 cannot be extended naively.

---

### 7. Conditional local reduction to persistent branches

Suppose that at some radius \(r_0\), every angular critical point is nondegenerate. Then, after shrinking to an interval \(J\ni r_0\), all critical points can be enumerated by finitely many real-analytic branches

\[
\theta_1(r),\dots,\theta_L(r).
\]

If \(\nu_f(r)\ge N\) for every \(r\in J\), then on some nonempty open subinterval \(J'\subset J\), a fixed collection of \(N\) branches has equal global maximum value throughout \(J'\).

Indeed, for every \(N\)-element subset \(A\subset\{1,\dots,L\}\), let \(E_A\) be the set of radii where all branches in \(A\) have equal value and that value is at least every other critical value. The sets \(E_A\) are closed and finitely many of them cover \(J\). By the Baire category theorem, one \(E_A\) has nonempty interior.

Therefore, at regular radii, switching between different maxima cannot completely avoid persistent equal-value branches. The unresolved issue is classification or control of these moving branches.

## Self-Audit

1. **The fixed-spoke obstruction assumes angles independent of \(r\).**  
   This is the largest limitation. It rigorously kills binomial phase-locking at the original peak directions, but it does not cover irregularly moving maxima. Proposition 7 shows that this distinction is essential, not merely technical.

2. **The perturbative splitting lemma is a fixed-\(q\) asymptotic statement.**  
   Its smallness threshold can deteriorate rapidly as \(q\), \(s\), and the curvature \(ACq^2\) vary. I have not used it to claim a uniform theorem for an infinite lacunary series. The stated finite-dimensional result follows from a strict gap, the implicit function theorem, and explicit first-order peak-height calculations.

3. **The branch reduction is conditional on a regular interval.**  
   Persistent degeneracies or bifurcation radii require real-analytic stratification beyond the elementary argument given here. Where nondegeneracy holds, the finite analytic enumeration and Baire argument are standard and complete; I do not claim that this automatically covers every large radius.

## Computations To Verify

The following code numerically isolates angular critical points of a polynomial using the Fourier representation. Floating-point equality is not a proof, but it is useful for searching for counterexamples and transition failures.

```python
import numpy as np
from math import gcd, pi

def fourier_coeffs(a, r):
    """
    a[n] is the coefficient of z^n.
    Returns c[k] for H(theta)=|p(r exp(i theta))|^2
    = sum_{k=-d}^d c[k] exp(i k theta).
    """
    a = np.asarray(a, dtype=complex)
    d = len(a) - 1
    c = {}
    for k in range(d + 1):
        c[k] = sum(
            a[n+k] * np.conjugate(a[n]) * r**(2*n+k)
            for n in range(d-k+1)
        )
    for k in range(1, d+1):
        c[-k] = np.conjugate(c[k])
    return c

def critical_angles(a, r, unit_tol=1e-7, merge_tol=1e-7):
    """
    H'(theta)=i sum k*c[k]*w^k, w=e^{i theta}.
    Multiply by w^d and solve the resulting polynomial.
    """
    d = len(a) - 1
    c = fourier_coeffs(a, r)

    # Ascending coefficients for w^0,...,w^(2d)
    P = np.zeros(2*d + 1, dtype=complex)
    for k in range(-d, d+1):
        P[k+d] += 1j * k * c[k]

    # Remove numerically zero leading coefficients.
    while len(P) > 1 and abs(P[-1]) < 1e-14:
        P = P[:-1]

    roots = np.polynomial.polynomial.polyroots(P)
    angles = sorted(
        (np.angle(w) % (2*pi))
        for w in roots
        if abs(abs(w)-1) < unit_tol
    )

    merged = []
    for t in angles:
        if not merged or abs(t-merged[-1]) > merge_tol:
            merged.append(t)
    if len(merged) > 1 and abs((merged[0] + 2*pi) - merged[-1]) < merge_tol:
        merged[0] = 0.0
        merged.pop()
    return merged

def count_global_maxima(a, r, value_tol=1e-8):
    angles = critical_angles(a, r)
    vals = []
    for t in angles:
        z = r*np.exp(1j*t)
        p = sum(an*z**n for n, an in enumerate(a))
        vals.append(abs(p))
    M = max(vals)
    maxima = [t for t, v in zip(angles, vals)
              if M-v <= value_tol*max(1.0, M)]
    return maxima, M
```

Baseline splitting test:

```python
for q in [3, 5, 10, 25]:
    eps = 1e-12
    # 1 + eps*z + z^q
    a = [0.0]*(q+1)
    a[0], a[1], a[q] = 1.0, eps, 1.0
    for r in [0.5, 1.0, 2.0]:
        maxima, M = count_global_maxima(a, r, value_tol=1e-10)
        print(q, r, len(maxima), maxima)
# Exact theorem predicts one maximum, at theta=0, for every r.
```

First-order splitting prediction:

```python
def first_order_survivors(q, s, D):
    L = np.array([
        np.real(D*np.exp(2j*np.pi*s*j/q))
        for j in range(q)
    ])
    mx = np.max(L)
    J = [j for j, x in enumerate(L) if abs(x-mx) < 1e-12]
    return gcd(q, abs(s)), J, L

for q, s, D in [
    (12, 1, 1+0.3j),
    (12, 4, 1+0.3j),
    (12, 4, np.exp(1j*np.pi/4)),
]:
    d, J, L = first_order_survivors(q, s, D)
    print("q,s,d =", q, s, d, "predicted candidates =", J)
# Generic prediction: len(J)=d; exceptional edge-normal phase: <=2d.
```

Exact symbolic verification of Proposition 7:

```python
import sympy as sp

r, x = sp.symbols('r x', positive=True, real=True)
H = 1 + 3*r**2 + r**4 + 2*r*(1-r**2)*x - 4*r**2*x**2
xstar = sp.solve(sp.diff(H, x), x)[0]
print(sp.simplify(xstar))             # (1-r**2)/(4*r)
print(sp.solve_univariate_inequality(abs(xstar) < 1, r))
# Expected: sqrt(5)-2 < r < sqrt(5)+2.
```

For a proposed lacunary construction, transition radii should be generated and checked as follows:

```python
def transition_radius(ai, ni, aj, nj):
    # Solve |ai| r^ni = |aj| r^nj.
    assert nj != ni and ai != 0 and aj != 0
    return (abs(ai)/abs(aj))**(1.0/(nj-ni))

# Given exponents n[k] and coefficients a[k]:
# 1. Generate all consecutive Newton-polygon transition radii.
# 2. Test r = R*exp(t) for a fine mesh of small positive and negative t.
# 3. Record both local critical points and equal global peak counts.
# 4. At suspicious points, replace numpy root finding by Arb or
#    exact algebraic root isolation.
```

A symbolic elimination search for moving equal maxima in trinomials should solve, for distinct \(x=e^{i\theta}\) and \(y=e^{i\phi}\),

\[
\partial_\theta H(r,\theta)=0,\qquad
\partial_\phi H(r,\phi)=0,\qquad
H(r,\theta)=H(r,\phi),
\]

together with \(|x|=|y|=1\), and test whether the resulting component projects onto an open interval of \(r\). This is the most direct finite-model test of whether persistent moving ties can occur without obvious reflection or rotation.

## Route Diagnosis

### Proved ledger

- Phase-alignment maxima are exactly controlled by the fixed gcd of the exponent support.
- Positive-coefficient and phase-compatible lacunary series have bounded, constant \(\nu_f(r)\).
- Arbitrarily small norm perturbations can reduce \(q\) exact binomial peaks to one.
- Fixed persistent equal-critical rays force a global holomorphic covariance identity.
- Fixed equally spaced \(q\)-spoke templates force support in one congruence class modulo \(q\).
- A nonmonomial entire function cannot support fixed-spoke templates of unbounded orders on different annuli.
- The first noncongruent perturbing exponent generically reduces \(q\) nominal peaks to \(\gcd(q,s)\), and at worst \(2\gcd(q,s)\) at first order.
- Persistent moving equal maxima force equal real values of \(zf'/f\).
- Two persistent moving global maxima need not imply rotational symmetry.

### Plausible but unproved

- In a sufficiently hierarchical superlacunary series, iterative splitting by the first, second, and later symmetry-breaking terms should often reduce the global maxima to a number controlled by the gcd of the full support. Making this uniform through infinitely many exponentially small levels is unproved.
- Persistent large numbers of moving equal maxima may force a finite group of holomorphic or antiholomorphic symmetries, even though two branches do not. No theorem of the necessary strength is known here.
- Generic lacunary coefficients likely produce only one global maximum, or a conjugate pair under real-coefficient symmetry, on many large circles. Genericity cannot disprove the existential problem.

### Dead ends

- **Dominant-binomial norm estimates:** killed by \(1+\varepsilon z+z^q\).
- **Positive coefficients or simultaneous phase alignment:** multiplicity is the fixed support gcd.
- **Preserving the original \(q\) spokes by exact cancellation:** persistence on an interval forces global \(q\)-covariance, incompatible with unbounded \(q\) for a nonmonomial.
- **Naive persistent-branch rigidity:** false already for \(1+z-z^2\).

### Precise block

A viable Route 3 construction must avoid both perturbative stability and fixed rotational templates. It must arrange, throughout every sufficiently large radius interval, many **moving, generally irregular** branches \(z_j(r)\) satisfying simultaneously

\[
|f(z_i(r))|=|f(z_j(r))|=M_f(r)
\]

and

\[
\frac{z_i(r)f'(z_i(r))}{f(z_i(r))}
=
\frac{z_j(r)f'(z_j(r))}{f(z_j(r))}
\in\mathbb R.
\]

Lacunary dominance gives no mechanism for these exact identities. Producing or excluding such moving branches is essentially a rigidity/interpolation problem of comparable strength to the original open question.

A fresh attempt should therefore combine Routes 3, 4, and 6: first classify persistent equal-max branches for three- and four-term lacunary sums using resultants; then determine whether configurations with three or more branches are always explained by rotational or reflection symmetries. If that finite classification fails, the counterexamples may reveal a genuinely non-symmetric equality mechanism suitable for an affirmative construction.