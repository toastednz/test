STATUS: BLOCKED

## Result

Route 4 yields a rigorous local structure theorem but not a disproof of Question 2. For every nonmonomial entire \(f\), the maximum points admit, away from a locally finite set of logarithmic radii, finitely many nondegenerate real-analytic branches. Along any interval supporting \(k\) persistent maximum branches, all branches take the same value of \(zf'/f\), and \(\log M_f(e^t)\) is real analytic and strictly convex. If two such branches have constant angular separation, then \(f\) has the predicted rotational covariance. However, constant separation cannot be deduced: the polynomial \(1+az-z^2\) has two persistent equal global-max branches with varying separation and no nontrivial rotational covariance. A small positive rigidity result is proved for real cubics: three persistent maxima on an open radius interval force a binomial \(a_0+a_3z^3\). The unresolved obstruction is to control arbitrarily many moving, equimodular inverse branches of \(zf'/f\); the real-analytic argument alone provides no global bound on their number.

## Complete Argument

### 1. Real-analytic stratification of the maximum set

Put

\[
t=\log r,\qquad
H(t,\theta)=\left|f\!\left(e^{t+i\theta}\right)\right|^2,
\]

and define

\[
\mathcal A
=
\left\{
(t,\theta):
H(t,\theta)=\max_{\phi\in\mathbb R/2\pi\mathbb Z}H(t,\phi)
\right\}.
\]

The function \(H\) is real analytic on
\(\mathbb R\times\mathbb S^1\). Since \(f\) is nonmonomial, every fiber

\[
\mathcal A_t=\{\theta:(t,\theta)\in\mathcal A\}
\]

is finite.

We use the following standard consequence of real subanalytic cell decomposition.

> **Subanalytic finite-fiber fact.**  
> Let \(X\) be a compact subanalytic subset of a real-analytic surface, and let \(\pi:X\to [a,b]\) be analytic with finite fibers. Then \([a,b]\) has a finite partition into points and open intervals such that, over each open interval, \(X\) is a finite disjoint union of real-analytic graphs.

To apply it, restrict to a compact cylinder \(J\times\mathbb S^1\). The set

\[
\{(t,\theta,\phi):H(t,\phi)>H(t,\theta)\}
\]

is relatively semianalytic, and its projection in \((t,\theta)\) is subanalytic because the \(\phi\)-variable ranges over a compact set. Its complement is \(\mathcal A\), so \(\mathcal A\cap(J\times\mathbb S^1)\) is subanalytic. Its fibers are finite, and the quoted fact applies.

Thus, after removing finitely many radii from every compact \(t\)-interval, the maximum points are represented by finitely many real-analytic branches

\[
\theta=\theta_j(t).
\]

We next show that persistent angular degeneracy is impossible.

---

### 2. Degenerate global maxima occur only at locally finitely many radii

At a maximum point \(f(e^{t+i\theta})\neq0\). Locally put

\[
P(w)=f(e^w),\qquad w=t+i\theta,
\]

and define

\[
G(w)=\frac{P'(w)}{P(w)}
=
\frac{e^w f'(e^w)}{f(e^w)}.
\]

Locally we may write

\[
u(t,\theta)=\log |P(t+i\theta)|.
\]

If a prime denotes differentiation with respect to \(w\), the Cauchy–Riemann equations give

\[
u_\theta=-\operatorname{Im}G,
\qquad
u_{\theta\theta}=-\operatorname{Re}G'.
\]

Suppose there were an open \(t\)-interval and a differentiable branch
\(w(t)=t+i\theta(t)\) consisting entirely of degenerate angular maxima. Then

\[
u_\theta(t,\theta(t))=0,
\qquad
u_{\theta\theta}(t,\theta(t))=0.
\]

Hence along the branch

\[
G(w(t))\in\mathbb R,
\qquad
\operatorname{Re}G'(w(t))=0.
\]

Write \(G'(w(t))=ib(t)\), with \(b(t)\in\mathbb R\). Differentiating
\(\operatorname{Im}G(w(t))=0\) gives

\[
0
=
\operatorname{Im}\left(G'(w(t))(1+i\theta'(t))\right)
=
\operatorname{Im}\left(ib(t)-b(t)\theta'(t)\right)
=
b(t).
\]

Thus \(G'(w(t))=0\) throughout the branch. By the identity theorem,
\(G'\equiv0\) locally, so \(G\equiv\lambda\) for some constant \(\lambda\). Therefore

\[
\frac{zf'(z)}{f(z)}=\lambda
\]

on an open set. The entire function \(zf'(z)-\lambda f(z)\) consequently vanishes identically. If

\[
f(z)=\sum_{n\ge0}a_nz^n,
\]

then

\[
(n-\lambda)a_n=0
\]

for every \(n\). Since \(f\neq0\), exactly one Taylor coefficient can be nonzero, and \(f\) is a monomial, contrary to hypothesis.

The set of degenerate maximum points is subanalytic. If its projection to a compact \(t\)-interval were infinite, that projection, being a subanalytic subset of \(\mathbb R\), would contain an interval. Cell decomposition would then supply exactly the forbidden degenerate branch. Therefore:

> **Lemma 1.**  
> For a nonmonomial entire function, the radii at which at least one global maximum is angularly degenerate form a locally finite subset of \((0,\infty)\).

Combining this with the preceding stratification gives:

> **Lemma 2.**  
> There is a locally finite set \(E\subset\mathbb R\) such that on every component \(I\) of \(\mathbb R\setminus E\):
> 1. \(\nu_f(e^t)\) is constant, say equal to \(k\);
> 2. the maximum points are \(k\) disjoint real-analytic branches
>    \[
>    w_j(t)=t+i\theta_j(t);
>    \]
> 3. all these maxima are nondegenerate:
>    \[
>    \partial_{\theta\theta}\log|f(e^{t+i\theta_j(t)})|<0.
>    \]

Thus \(\nu_f(e^t)\) is locally piecewise constant. This does not imply that its values remain bounded as \(t\to\infty\): the exceptional set may be infinite and tend to infinity.

---

### 3. Differential identities along persistent maximum branches

Fix one of the intervals \(I\) from Lemma 2. Let

\[
m(t)=\log M_f(e^t).
\]

Every maximum branch satisfies

\[
u(t,\theta_j(t))=m(t).
\]

At a maximum, \(u_\theta=0\), so

\[
m'(t)
=
u_t(t,\theta_j(t))
=
\operatorname{Re}G(w_j(t)).
\]

But \(u_\theta=-\operatorname{Im}G=0\), hence

\[
\boxed{G(w_j(t))=m'(t)}
\]

for every \(j\). In the original \(z\)-coordinate,

\[
\boxed{
\frac{z_j(t)f'(z_j(t))}{f(z_j(t))}
=
m'(t),
\qquad
z_j(t)=e^{t+i\theta_j(t)}.
}
\]

Thus all persistent global maximum points on the same circle are not merely angular critical points: they are distinct points at which \(zf'/f\) takes exactly the same real value.

Let

\[
A_j(t)=G'(w_j(t))=a_j(t)+ib_j(t).
\]

Since

\[
u_{\theta\theta}=-\operatorname{Re}G',
\]

nondegeneracy of the maximum gives

\[
a_j(t)>0.
\]

Differentiating \(\operatorname{Im}G(w_j(t))=0\) gives

\[
0
=
\operatorname{Im}\left(A_j(t)(1+i\theta_j'(t))\right)
=
b_j(t)+a_j(t)\theta_j'(t),
\]

and therefore

\[
\boxed{
\theta_j'(t)=-\frac{b_j(t)}{a_j(t)}.
}
\]

Finally,

\[
\begin{aligned}
m''(t)
&=
\operatorname{Re}\left(A_j(t)(1+i\theta_j'(t))\right)\\
&=
a_j(t)-b_j(t)\theta_j'(t)\\
&=
a_j(t)+\frac{b_j(t)^2}{a_j(t)}\\
&=
\boxed{\frac{|A_j(t)|^2}{\operatorname{Re}A_j(t)}>0}.
\end{aligned}
\]

We have proved:

> **Lemma 3.**  
> On every regular maximum interval, \(\log M_f(e^t)\) is real analytic and strictly convex. If there are \(k\) maximum branches, then \(G=zf'/f\) takes the same real value \(m'(t)\) at all \(k\) points.

Because \(m''>0\), one can use

\[
s=m'(t)
\]

as a local parameter. If \(w_j=w_j(s)\), then

\[
G(w_j(s))=s,
\qquad
\operatorname{Re}w_j(s)=t(s),
\]

and

\[
\boxed{
\frac{dw_j}{ds}
=
\frac{1}{G'(w_j(s))}.
}
\]

Consequently, persistent multiplicity \(k\) is equivalent locally to the existence of \(k\) inverse branches of \(G\) over a real \(s\)-interval whose real parts coincide, together with the global-maximum condition.

This is the central reduction obtained from Route 4.

---

### 4. Constant angular separation does force rotational covariance

The expected rigidity conclusion is valid under one additional hypothesis.

> **Lemma 4.**  
> Suppose two distinct persistent maximum branches satisfy
> \[
> \theta_i(t)-\theta_j(t)=\alpha
> \]
> on a nonempty open interval, with \(\alpha\) constant modulo \(2\pi\). Then, with \(\omega=e^{i\alpha}\),
> \[
> f(\omega z)=c f(z)
> \]
> for some constant \(c\) with \(|c|=1\).

**Proof.** Choose continuous lifts so that

\[
w_i(t)=w_j(t)+i\alpha.
\]

Lemma 3 gives

\[
G(w_j(t)+i\alpha)=G(w_j(t)).
\]

The meromorphic function

\[
Q(w)=G(w+i\alpha)-G(w)
\]

therefore vanishes on a curve with an accumulation point away from its poles. By the identity theorem for meromorphic functions,

\[
G(w+i\alpha)=G(w)
\]

identically. In the \(z\)-plane this is

\[
\frac{\omega z f'(\omega z)}{f(\omega z)}
=
\frac{z f'(z)}{f(z)}.
\]

On an open set avoiding the zeros of \(f(z)f(\omega z)\),

\[
\frac{d}{dz}
\log\frac{f(\omega z)}{f(z)}
=
0.
\]

Hence \(f(\omega z)=cf(z)\) on that open set, and therefore everywhere by analytic continuation. Along the two maximum branches, the two sides have equal modulus, so \(|c|=1\). ∎

If \(f\) has at least two Taylor exponents \(m\neq n\), comparison of coefficients gives

\[
\omega^m=\omega^n=c,
\]

and hence

\[
\omega^{n-m}=1.
\]

Thus every nontrivial constant branch separation is a rational multiple of \(2\pi\) and comes from a genuine finite rotational covariance.

There is also a standard normalization. If \(n_0\) is the least Taylor exponent and

\[
q=\gcd\{n-n_0:a_n\neq0\},
\]

then

\[
f(z)=z^{n_0}h(z^q)
\]

for an entire \(h\), and

\[
\nu_f(r)=q\,\nu_h(r^q).
\]

Therefore a hypothetical affirmative example can be reduced to one with \(q=1\), i.e. no nontrivial rotational covariance. For such a normalized function, Lemma 4 says that no two distinct persistent maximum branches can have constant angular separation.

---

### 5. The naive branch-rigidity statement is false

Two persistent equal maxima need not come from rotation.

Let \(a\in\mathbb R\setminus\{0\}\) and

\[
f_a(z)=1+az-z^2.
\]

Writing \(x=\cos\theta\), direct expansion gives

\[
\begin{aligned}
|f_a(re^{i\theta})|^2
&=
1+a^2r^2+r^4
+2ar(1-r^2)x
-2r^2(2x^2-1)\\
&=
C(r)+2ar(1-r^2)x-4r^2x^2,
\end{aligned}
\]

where \(C(r)=1+a^2r^2+r^4+2r^2\). As a function of \(x\in[-1,1]\), this is a strictly concave quadratic with vertex

\[
x_*(r)=\frac{a(1-r^2)}{4r}.
\]

Whenever

\[
|a(1-r^2)|<4r,
\]

the vertex lies in \((-1,1)\), and the global maxima occur exactly at

\[
\theta_\pm(r)=\pm\arccos x_*(r).
\]

Thus

\[
\nu_{f_a}(r)=2
\]

throughout an open interval containing \(r=1\). These are nondegenerate persistent global maxima and have exactly equal values because of conjugation symmetry.

On the other hand, if

\[
f_a(\omega z)=c f_a(z),
\]

comparison of the constant coefficient gives \(c=1\), while comparison of the nonzero linear coefficient gives \(\omega=1\). Hence \(f_a\) has no nontrivial rotational covariance.

Moreover \(x_*(r)\) is nonconstant, so the angular separation between the two maximum branches varies with \(r\). This is exactly the mechanism not covered by Lemma 4.

Therefore the proposed principle

> persistent equal maximum branches imply rotation

is already false for two branches.

---

### 6. A finite-stage rigidity theorem for real cubics

There is nevertheless some evidence that higher persistent multiplicity may be more rigid.

> **Proposition.**  
> Let
> \[
> p(z)=a_0+a_1z+a_2z^2+a_3z^3,
> \qquad a_j\in\mathbb R,\quad a_0a_3\neq0.
> \]
> If
> \[
> \nu_p(r)\ge3
> \]
> for every \(r\) in a nonempty open interval, then
> \[
> a_1=a_2=0.
> \]
> Thus \(p(z)=a_0+a_3z^3\), and the persistent multiplicity is explained by cubic rotational symmetry.

**Proof.** Since the coefficients are real,

\[
|p(re^{i\theta})|^2=h_r(\cos\theta)
\]

for a real cubic polynomial \(h_r\). A single interior maximum \(x\in(-1,1)\) produces two angular maxima \(\pm\arccos x\), while each endpoint \(x=\pm1\) produces one.

A nonconstant cubic cannot have two distinct interior local maxima: its derivative is quadratic, and at its two distinct critical points the second derivatives have opposite signs. Therefore, if there are at least three angular maxima, there must be both an endpoint global maximum and an interior global maximum.

By the finite analytic decomposition from Section 1, after shrinking the radius interval, one fixed endpoint and one interior maximum persist. Replacing \(p(z)\) by \(p(-z)\) if necessary, assume the endpoint is \(x=1\).

Write

\[
h_r(x)=C(r)+h_1(r)x+h_2(r)x^2+h_3(r)x^3.
\]

A direct expansion using \(\cos2\theta=2x^2-1\) and
\(\cos3\theta=4x^3-3x\) gives

\[
\begin{aligned}
h_3(r)&=8a_0a_3r^3,\\
h_2(r)&=4(a_0a_2r^2+a_1a_3r^4),\\
h_1(r)&=
2a_0a_1r
+(2a_1a_2-6a_0a_3)r^3
+2a_2a_3r^5.
\end{aligned}
\]

Let \(X(r)\in(-1,1)\) be the interior maximum and let \(M(r)\) be the common maximum value. The cubic

\[
M(r)-h_r(x)
\]

vanishes at \(x=1\), and it has a double zero at \(x=X(r)\). Consequently

\[
M(r)-h_r(x)=K(r)(1-x)(x-X(r))^2.
\]

Comparison of the leading coefficient gives

\[
K(r)=h_3(r).
\]

Comparison of the \(x^2\) and \(x\) coefficients gives

\[
h_2=-h_3(1+2X),
\qquad
h_1=h_3(X^2+2X).
\]

Put

\[
Y=1+2X=-\frac{h_2}{h_3}.
\]

Since

\[
X^2+2X=\frac{Y^2+2Y-3}{4},
\]

we obtain the Laurent identity

\[
\frac{h_1}{h_3}
=
\frac{Y^2+2Y-3}{4}.
\]

Now

\[
Y
=
-\frac{a_2}{2a_3}r^{-1}
-\frac{a_1}{2a_0}r.
\]

The left-hand side \(h_1/h_3\) contains only the powers

\[
r^{-2},\quad r^0,\quad r^2.
\]

On the right-hand side, the term \(2Y/4\) contributes

\[
-\frac{a_2}{4a_3}r^{-1}
-\frac{a_1}{4a_0}r,
\]

while \(Y^2\) contains only \(r^{-2},r^0,r^2\). Since the identity holds on an open interval, its Laurent coefficients must agree. The coefficients of \(r^{-1}\) and \(r\) therefore vanish:

\[
a_2=0,\qquad a_1=0.
\]

This proves the proposition. ∎

This result is confined to real cubics. No corresponding theorem for arbitrary degree or arbitrary complex coefficients has been established here.

---

### 7. Exact point at which Route 4 stops

Suppose a hypothetical \(f\) satisfies

\[
\nu_f(r)\longrightarrow\infty.
\]

After removing the locally finite exceptional set, every sufficiently late regular interval contains arbitrarily many analytic branches \(w_j(t)\) satisfying

\[
G(w_j(t))=m'(t)\in\mathbb R,
\]

\[
\operatorname{Re}w_j(t)=t,
\]

\[
\operatorname{Re}G'(w_j(t))>0,
\]

and

\[
\operatorname{Re}\log f(e^{w_j(t)})=m(t).
\]

After reparametrization by \(s=m'(t)\), these become arbitrarily large families of inverse branches

\[
G(w_j(s))=s
\]

with the same real part.

For two inverse branches, equality of real parts on a real interval does not force their difference to be constant: a holomorphic function may be purely imaginary but nonconstant on a real interval. The example \(1+az-z^2\) realizes precisely this phenomenon through conjugate moving branches.

Thus the missing theorem would have to say something substantially stronger, for example:

> For an aperiodic logarithmic derivative \(G=zf'/f\), the number of inverse branches over a real interval that have the same real part and satisfy the maximum orientation condition \(\operatorname{Re}G'>0\) is bounded along arbitrarily large radii.

No such theorem has been proved here, and it is of comparable difficulty to the original negative assertion. Local real-analytic stratification does not prevent new branches from appearing at larger and larger radii, nor does it force any angular gap to become constant.

## Self-Audit

1. **Use of subanalytic cell decomposition.**  
   I invoked a standard but substantial theorem rather than reproving real subanalytic stratification from first principles. The hypotheses are satisfied: the maximum set is obtained by a proper projection over the compact angular variable, its fibers are finite, and the ambient space is real analytic. These are exactly the conditions under which finite graph decomposition applies.

2. **Passage from persistent degeneracy to a monomial.**  
   This uses a local nonvanishing neighborhood and the identity theorem for \(G'\). Maximum points cannot be zeros because \(M_f(r)>0\). Hence the logarithmic derivative is analytic near a short branch segment, and the calculation \(G'=0\) is valid. The final identity \(zf'=\lambda f\) is an entire identity, so the Taylor-coefficient argument is conclusive.

3. **The cubic rigidity result is very narrow.**  
   It depends on real coefficients and degree three; it provides no justification for extrapolating to transcendental entire functions. Within that scope, the argument is exact: the maximum configuration forces a cubic factorization, and comparison of the odd Laurent powers immediately forces \(a_1=a_2=0\).

## Computations To Verify

### 1. Symbolically verify the quadratic counterexample

```python
import sympy as sp

a, r, x = sp.symbols('a r x', nonzero=True, real=True)

H = (
    1 + a**2*r**2 + r**4
    + 2*a*r*(1-r**2)*x
    - 2*r**2*(2*x**2 - 1)
)

xstar = sp.simplify(a*(1-r**2)/(4*r))
Hstar = sp.simplify(H.subs(x, xstar))

print("dH/dx =", sp.factor(sp.diff(H, x)))
print("x* =", xstar)
print("H-H(x*) =", sp.factor(H - Hstar))

assert sp.simplify(sp.diff(H, x).subs(x, xstar)) == 0
assert sp.simplify(H - Hstar + 4*r**2*(x-xstar)**2) == 0
```

The final output should show

```text
H-H(x*) = -4*r**2*(x-x*)**2.
```

Thus, whenever `abs(xstar) < 1`, there are exactly two angular maxima.

### 2. Verify the cubic Laurent obstruction

```python
import sympy as sp

a0, a1, a2, a3, r = sp.symbols(
    'a0 a1 a2 a3 r', nonzero=True, real=True
)

h3 = 8*a0*a3*r**3
h2 = 4*(a0*a2*r**2 + a1*a3*r**4)
h1 = (
    2*a0*a1*r
    + (2*a1*a2 - 6*a0*a3)*r**3
    + 2*a2*a3*r**5
)

Y = sp.expand(-h2/h3)
obstruction = sp.expand(h1/h3 - (Y**2 + 2*Y - 3)/4)

print("Y =", Y)
print("Laurent obstruction =", sp.collect(obstruction, r))
print("coefficient of r^(-1):", sp.simplify(obstruction.coeff(r, -1)))
print("coefficient of r:", sp.simplify(obstruction.coeff(r, 1)))

assert sp.simplify(obstruction.coeff(r, -1) - a2/(4*a3)) == 0
assert sp.simplify(obstruction.coeff(r, 1) - a1/(4*a0)) == 0
```

Persistent endpoint/interior equality requires `obstruction == 0`, so the displayed coefficients force `a2 = a1 = 0`.

### 3. Numerically verify the common logarithmic-derivative value

```python
import cmath
import math

def branch_data(a, r):
    xs = a*(1-r*r)/(4*r)
    if abs(xs) >= 1:
        return None

    th = math.acos(xs)
    out = []

    for theta in (th, -th):
        z = r*cmath.exp(1j*theta)
        f = 1 + a*z - z*z
        fp = a - 2*z
        G = z*fp/f
        out.append((theta, abs(f), G))

    return out

for r in (0.8, 1.0, 1.2):
    vals = branch_data(1.0, r)
    print("r =", r)
    for theta, modulus, G in vals:
        print("  theta =", theta, "|f| =", modulus, "G =", G)
```

At each radius in the valid interval, both branches should have equal modulus and numerically equal real values of \(G=zf'/f\), with negligible imaginary part.

### 4. Search for complex-cubic counterexamples to higher rigidity

For rational complex coefficients, the following symbolic elimination can test whether an endpoint and another critical point have equal value persistently:

```python
# Pseudocode / SymPy outline

x, r = symbols('x r', real=True)
# Build H(r,theta) as a trigonometric polynomial.
# Substitute cos(theta)=x only when coefficients have reflection symmetry.
h = C(r) + h1(r)*x + h2(r)*x**2 + h3(r)*x**3

critical = diff(h, x)
equal_endpoint = h - h.subs(x, 1)

R = resultant(critical, equal_endpoint, x)
R = factor(R)

# Persistent equality on a radius interval requires R to vanish
# identically as a polynomial/Laurent polynomial in r.
# Remove factors corresponding to the trivial root x=1 and solve
# all remaining coefficient equations in the polynomial coefficients.
```

For genuinely complex coefficients one should instead use \(X=\cos\theta\), \(Y=\sin\theta\), \(X^2+Y^2=1\), impose the angular critical equation and equal-value equations for three candidate points, and eliminate the angular variables with Gröbner bases or cylindrical algebraic decomposition.

## Route Diagnosis

The real-analytic route successfully converts persistent global maxima into a finite family of nondegenerate analytic branches and then into equimodular inverse branches of \(G=zf'/f\). It also proves genuine rotational covariance when an angular gap is constant, and the real-cubic calculation gives limited evidence for high-multiplicity rigidity.

The route is blocked because angular gaps may vary. The quadratic example proves that equal persistent critical values can be maintained by an anti-holomorphic reflection mechanism without rotational covariance. Local stratification gives no bound on how many such moving branches can arise at increasingly large radii, and bifurcation radii may tend to infinity while remaining locally finite.

A fresh Route 4 attempt should focus on classifying families of inverse branches of \(zf'/f\) satisfying

\[
G(w_j(s))=s,\qquad
\operatorname{Re}w_j(s)=T(s),\qquad
\operatorname{Re}G'(w_j(s))>0.
\]

The immediate finite test is to classify persistent triples for complex cubics and quartics. If arbitrarily large nonsymmetric persistent families already occur for polynomials on one radius interval, the hoped-for local rigidity theorem is false. If low-degree classification consistently forces rotation or reflection, the next target should be a theorem showing that more than two equimodular inverse branches force a finite holomorphic or antiholomorphic symmetry. Without such a theorem, Route 4 does not reach a universal bound on \(\liminf\nu_f(r)\).