STATUS: BLOCKED

## Result

I obtained a rigorous Abel/Fourier formulation valid for every integer-valued \(f\in\mathbb Q[x]\): after normalizing \(0\in A\cap C_f\), an exact tiling defines a representation height \(H(n)=|a(n)|+|c(n)|\), and the absolutely convergent Fourier series satisfy
\[
F_A(t,\theta)F_{C_f}(t,\theta)
=\sum_{n\in\mathbb Z}t^{H(n)}e(n\theta).
\]
As \(t\uparrow1\), this product converges distributionally to \(\delta_0\). I also prove the sharp packing estimate
\[
\sup_I |A\cap I|=O_f(|I|^{1-1/d}),
\]
which places \(1_A\) and \(1_{C_f}\) exactly at the critical Sobolev regularity compatible with a delta product. For cubes, the Abel transform has the expected Weyl cancellation at irrational frequencies and explicit cubic Gauss-sum limits at rationals. The route nevertheless remains blocked: the right side is governed by the completely uncontrolled height \(H(n)\), so distributional convergence cannot be divided into separate spectral identities for \(A\) and \(C_f\). Even an additional equidistribution theorem for \(H\)-balls would currently yield only residue equidistribution of \(A\), not a contradiction.

## Complete Argument

### 1. Normalization and injectivity

Assume for the purposes of deriving consequences that
\[
\mathbb Z=A\oplus C,\qquad C=f(\mathbb Z),
\]
where \(f\in\mathbb Q[x]\) is integer-valued and has degree \(d\ge2\).

Let \(0=a_0+c_0\) be the unique representation of \(0\). Replacing
\[
A\quad\text{by}\quad A-a_0,\qquad
C\quad\text{by}\quad C-c_0
\]
preserves the direct-sum identity because \(a_0+c_0=0\), and makes
\[
0\in A\cap C.
\]
The translated \(C\) is still the value set of the integer-valued polynomial \(f-c_0\). Thus we may assume \(0\in A\cap C\).

The addition map
\[
A\times C\longrightarrow \mathbb Z,\qquad (a,c)\longmapsto a+c
\]
is a bijection. In particular, it is injective on every subset of \(A\times C\).

For each \(n\in\mathbb Z\), denote its unique representation by
\[
n=a(n)+c(n),\qquad a(n)\in A,\ c(n)\in C,
\]
and define the representation height
\[
H(n):=|a(n)|+|c(n)|.
\]
The triangle inequality gives
\[
H(n)\ge |n|.
\]

---

### 2. Polynomial value-set growth

Let
\[
N_C(R):=|C\cap[-R,R]|.
\]

#### Lemma 2.1
There are constants \(c_f,C_f>0\) and \(R_0\) such that
\[
c_fR^{1/d}\le N_C(R)\le C_fR^{1/d}
\qquad(R\ge R_0).
\]

#### Proof

Write the leading coefficient of \(f\) as \(\alpha\ne0\). There are constants \(K_0,u,v>0\) such that for \(|k|\ge K_0\),
\[
u|k|^d\le |f(k)|\le v|k|^d.
\]

If \(|f(k)|\le R\), then either \(|k|<K_0\) or
\[
|k|\le (R/u)^{1/d}.
\]
Thus the number of parameters producing values in \([-R,R]\) is \(O_f(R^{1/d})\), and hence so is the number of distinct values.

For the lower bound, \(f'\) has constant nonzero sign on a sufficiently large positive ray, so \(f\) is strictly monotone on the integers \(k\ge K_1\). For a sufficiently small fixed \(\eta>0\), all integers
\[
K_1\le k\le \eta R^{1/d}
\]
satisfy \(|f(k)|\le R\) when \(R\) is large. Their values are distinct, giving \(\gg_f R^{1/d}\) elements of \(C\cap[-R,R]\). ∎

This proof uses only that \(f\) is a rational polynomial taking integer values; it does not require \(f\in\mathbb Z[x]\).

---

### 3. A sharp uniform packing bound for a hypothetical complement

Set
\[
\beta:=\frac1d,\qquad \alpha:=1-\frac1d.
\]

#### Lemma 3.1
For every integer interval \(I\) containing \(L\ge1\) points,
\[
|A\cap I|=O_f(L^\alpha),
\]
uniformly in the location of \(I\).

#### Proof

For sufficiently large \(L\), take
\[
C_L:=C\cap[-L,L].
\]
By Lemma 2.1,
\[
|C_L|\ge c_fL^\beta.
\]

The addition map is injective on
\[
(A\cap I)\times C_L.
\]
Consequently,
\[
|A\cap I|\,|C_L|
=|(A\cap I)+C_L|.
\]
The latter sumset is contained in the interval obtained by enlarging \(I\) by \(L\) at each endpoint, which contains at most \(3L+O(1)\) integers. Hence
\[
|A\cap I|\,c_fL^\beta\le 3L+O(1),
\]
and therefore
\[
|A\cap I|=O_f(L^{1-\beta})=O_f(L^\alpha).
\]
Small \(L\) are absorbed into the implied constant. ∎

This is stronger than merely proving that \(A\) has upper Banach density zero.

A finite \(A\) is impossible: finitely many translates of \(C\) contain only \(O_f(N^{1/d})\) points in \([-N,N]\), whereas coverage requires \(2N+1\). Thus both \(A\) and \(C\) are infinite.

---

### 4. An exact Abel/Fourier identity

Write
\[
e(\theta):=e^{2\pi i\theta}.
\]
For \(0<t<1\), define
\[
F_A(t,\theta):=\sum_{a\in A}t^{|a|}e(a\theta),
\qquad
F_C(t,\theta):=\sum_{c\in C}t^{|c|}e(c\theta).
\]
Both series converge absolutely and uniformly in \(\theta\).

#### Proposition 4.1
For every \(0<t<1\),
\[
F_A(t,\theta)F_C(t,\theta)
=
Q_t(\theta),
\]
where
\[
Q_t(\theta):=\sum_{n\in\mathbb Z}t^{H(n)}e(n\theta).
\]

#### Proof

Absolute convergence permits multiplication:
\[
F_A(t,\theta)F_C(t,\theta)
=
\sum_{a\in A}\sum_{c\in C}
t^{|a|+|c|}e((a+c)\theta).
\]
For each \(n\), there is exactly one pair \((a(n),c(n))\) with \(a(n)+c(n)=n\). Therefore the coefficient of \(e(n\theta)\) is exactly
\[
t^{|a(n)|+|c(n)|}=t^{H(n)}.
\]
This proves the identity. ∎

There is also an analytic Laurent-series version. For
\[
t<|z|<t^{-1},
\]
the series
\[
F_X(t,z):=\sum_{x\in X}t^{|x|}z^x
\]
converges absolutely for \(X=A,C\), and
\[
F_A(t,z)F_C(t,z)
=
\sum_{n\in\mathbb Z}t^{H(n)}z^n.
\]
Thus the regularization is not merely formal.

---

### 5. Distributional limit

Let \(\delta_0\) denote the unit point mass at \(0\) on the circle \(\mathbb T=\mathbb R/\mathbb Z\).

#### Proposition 5.1
As \(t\uparrow1\),
\[
Q_t\longrightarrow\delta_0
\]
in the space of distributions \(\mathcal D'(\mathbb T)\).

#### Proof

Let \(\varphi\in C^\infty(\mathbb T)\). Since its Fourier coefficients are absolutely summable,
\[
\langle Q_t,\varphi\rangle
=
\sum_{n\in\mathbb Z}t^{H(n)}\widehat\varphi(-n).
\]
For every fixed \(n\),
\[
t^{H(n)}\longrightarrow1,
\]
and \(0\le t^{H(n)}\le1\). Dominated convergence therefore gives
\[
\lim_{t\uparrow1}\langle Q_t,\varphi\rangle
=
\sum_{n\in\mathbb Z}\widehat\varphi(-n)
=
\varphi(0)
=
\langle\delta_0,\varphi\rangle.
\]
∎

Hence the legitimate Fourier statement is
\[
F_A(t,\cdot)F_C(t,\cdot)\longrightarrow\delta_0
\quad\text{in }\mathcal D'(\mathbb T).
\]

It is not legitimate to replace this by a pointwise or ordinary distributional product
\[
\widehat{1_A}\,\widehat{1_C}=\delta_0,
\]
because the product of the two limiting distributions is not defined a priori.

---

### 6. Abel growth and the critical exponent

At frequency \(0\),
\[
F_A(t,0)F_C(t,0)=\sum_n t^{H(n)}.
\]
Since \(H(n)\ge|n|\),
\[
F_A(t,0)F_C(t,0)
\le
\sum_{n\in\mathbb Z}t^{|n|}
=
\frac{1+t}{1-t}.
\]

Lemma 2.1 gives, as \(t\uparrow1\),
\[
F_C(t,0)\asymp_f (1-t)^{-1/d}.
\]
For example, the lower bound comes from values \(|c|\le(1-t)^{-1}\), while the upper bound follows by splitting \(C\) into dyadic shells and applying \(N_C(R)=O_f(R^{1/d})\).

Therefore
\[
F_A(t,0)=O_f\!\left((1-t)^{-(1-1/d)}\right).
\]

This is the Abel analogue of Lemma 3.1.

Now define periodic distributions
\[
T_A(\theta)=\sum_{a\in A}e(a\theta),
\qquad
T_C(\theta)=\sum_{c\in C}e(c\theta).
\]
The counting estimates imply
\[
T_A\in H^{-s}(\mathbb T)
\quad\text{for every }s>\frac{d-1}{2d},
\]
and
\[
T_C\in H^{-s}(\mathbb T)
\quad\text{for every }s>\frac1{2d}.
\]
Indeed, dyadic summation gives
\[
\sum_{a\in A}(1+a^2)^{-s}<\infty
\]
when \(2s>(d-1)/d\), and similarly for \(C\).

For \(C\), the endpoint fails:
\[
T_C\notin H^{-1/(2d)}.
\]
To see this, choose a large fixed \(\Lambda\). Lemma 2.1 implies that every sufficiently large annulus
\[
R/\Lambda<|c|\le R
\]
contains \(\gg_f R^{1/d}\) values after choosing \(\Lambda\) so that the lower count at \(R\) dominates the upper count at \(R/\Lambda\). Its contribution to the endpoint Sobolev norm is then bounded below by a positive constant, and summing over disjoint geometric annuli diverges.

On the other hand,
\[
\delta_0\in H^{-s}(\mathbb T)
\quad\Longleftrightarrow\quad s>\frac12.
\]
The two threshold exponents add exactly to \(1/2\):
\[
\frac{d-1}{2d}+\frac1{2d}=\frac12.
\]

Thus the hypothetical factorization lies precisely on the critical Sobolev line compatible with producing a delta distribution. Standard multiplication theorems for distributions give no contradiction here; in particular both factors have negative regularity.

---

### 7. What Weyl cancellation says for cubes

Now specialize to
\[
C=\{k^3:k\in\mathbb Z\}.
\]
The parametrization is injective, so define
\[
G_\varepsilon(\theta)
:=
\sum_{k\in\mathbb Z}
e^{-\varepsilon|k|^3}e(\theta k^3).
\]
This is \(F_C(e^{-\varepsilon},\theta)\).

At zero,
\[
G_\varepsilon(0)
=
2\Gamma(4/3)\varepsilon^{-1/3}+O(1).
\]
This follows from integral comparison with
\[
\int_0^\infty e^{-\varepsilon x^3}\,dx
=
\Gamma(4/3)\varepsilon^{-1/3}.
\]

#### Irrational frequencies

For fixed irrational \(\theta\), Weyl's theorem gives
\[
S_\theta(K):=\sum_{1\le k\le K}e(\theta k^3)=o(K).
\]
Abel summation with the decreasing weight
\[
w_\varepsilon(k)=e^{-\varepsilon k^3}
\]
then gives
\[
\sum_{k\ge1}w_\varepsilon(k)e(\theta k^3)
=o(\varepsilon^{-1/3}).
\]

Indeed, for every \(\eta>0\), choose \(K_0\) so that
\[
|S_\theta(K)|\le\eta K\qquad(K\ge K_0).
\]
The initial segment contributes \(O_\theta(K_0)\), while the tail is bounded by
\[
\eta\sum_{k\ge K_0}k\bigl(w_\varepsilon(k)-w_\varepsilon(k+1)\bigr)
\le
\eta\sum_{k\ge1}w_\varepsilon(k)
=O(\eta\varepsilon^{-1/3}).
\]
The negative-\(k\) tail is handled identically. Hence
\[
\frac{G_\varepsilon(\theta)}{G_\varepsilon(0)}
\longrightarrow0
\qquad(\theta\notin\mathbb Q).
\]

#### Rational frequencies

Let \(\theta=j/q\). The sequence
\[
p(k)=e(jk^3/q)
\]
is \(q\)-periodic, with mean
\[
\mu_{q,j}
:=
\frac1q\sum_{r=0}^{q-1}e(jr^3/q).
\]
The partial sums of \(p(k)-\mu_{q,j}\) are \(O(q)\). Abel summation therefore yields
\[
G_\varepsilon(j/q)
=
\mu_{q,j}G_\varepsilon(0)+O(q),
\]
and consequently
\[
\frac{G_\varepsilon(j/q)}{G_\varepsilon(0)}
\longrightarrow \mu_{q,j}.
\]

Thus the normalized cube transform vanishes at irrational frequencies and has cubic Gauss-sum limits at rational frequencies.

---

### 8. Why this does not separate the two Fourier factors

Define normalized functions
\[
\Phi_{A,\varepsilon}(\theta)
=
\frac{F_A(e^{-\varepsilon},\theta)}
     {F_A(e^{-\varepsilon},0)},
\]
\[
\Phi_{C,\varepsilon}(\theta)
=
\frac{F_C(e^{-\varepsilon},\theta)}
     {F_C(e^{-\varepsilon},0)},
\]
and
\[
\Phi_{H,\varepsilon}(\theta)
=
\frac{\sum_n e^{-\varepsilon H(n)}e(n\theta)}
     {\sum_n e^{-\varepsilon H(n)}}.
\]
The exact identity becomes
\[
\Phi_{A,\varepsilon}(\theta)\,
\Phi_{C,\varepsilon}(\theta)
=
\Phi_{H,\varepsilon}(\theta).
\]

Each function is the characteristic function of a probability measure:

- \(A\) is weighted by \(e^{-\varepsilon|a|}\);
- \(C\) is weighted by \(e^{-\varepsilon|c|}\);
- the representation integers are weighted by \(e^{-\varepsilon H(n)}\).

The last measure is the pushforward under addition of the product of the first two measures. Thus this normalized identity is exact but tautological.

For a modulus \(q\), put
\[
B_{r,q}(t):=
\sum_{\substack{n\in\mathbb Z\\n\equiv r\pmod q}}t^{H(n)}.
\]
Then
\[
Q_t(j/q)
=
\sum_{r=0}^{q-1}B_{r,q}(t)e(jr/q).
\]
Every \(B_{r,q}(t)\) tends to infinity as \(t\uparrow1\), because each residue class contains infinitely many fixed integers whose individual weights tend to \(1\). However, nothing proved above controls their relative rates of divergence.

A useful but presently unproved statement would be
\[
\frac{B_{r,q}(t)}
     {\sum_{s=0}^{q-1}B_{s,q}(t)}
\longrightarrow\frac1q
\qquad(t\uparrow1).
\tag{\(*\)}
\]
This is exactly a Følner/equidistribution assertion for the representation-height exhaustion.

If \((*)\) held, then
\[
\Phi_{H,\varepsilon}(j/q)\longrightarrow0
\qquad(j\not\equiv0\pmod q).
\]
For cubes, whenever \(\mu_{q,j}\ne0\), one would then get
\[
\Phi_{A,\varepsilon}(j/q)\longrightarrow0.
\]
This would say that the Abel-weighted points of \(A\) are equidistributed modulo certain moduli.

That conclusion is not a contradiction. Sparse aperiodic sets can be equidistributed modulo every fixed modulus. Thus Route 3 presently requires two additional inputs:

1. a theorem controlling \(H(n)\), strong enough to prove \((*)\) or a stronger local Fourier limit; and
2. a theorem converting the resulting spectral restrictions on \(A\) into an exact nonzero common difference with \(C-C\), or into periodicity.

Neither follows from the current hypotheses.

The obstruction is exactly the possible nonlocality:
\[
H(n)=|a(n)|+|c(n)|
\]
may be arbitrarily larger than \(|n|\), and there is no bound on
\[
H(n+q)-H(n)
\]
or on the jumps of \(a(n)\) and \(c(n)\).

Distributional convergence
\[
Q_t\to\delta_0
\]
does not repair this. Evaluation at a single rational frequency is not continuous in the distribution topology, so \(Q_t\to\delta_0\) gives no pointwise control of \(Q_t(j/q)\).

---

### 9. A digital model showing that the critical Fourier picture is consistent

This example is not a polynomial value set, so it does not solve the problem. It demonstrates that the packing exponents and delta-product identity alone cannot yield an impossibility theorem.

Every integer has a unique balanced ternary expansion
\[
n=\sum_{j\ge0}\varepsilon_j3^j,
\qquad
\varepsilon_j\in\{-1,0,1\},
\]
with finitely many nonzero digits.

Existence follows by choosing \(\varepsilon_0\equiv n\pmod3\) in \(\{-1,0,1\}\) and iterating with \((n-\varepsilon_0)/3\). Uniqueness follows because in a nontrivial relation
\[
\sum_j\delta_j3^j=0,\qquad \delta_j\in\{-2,-1,0,1,2\},
\]
the coefficient at the least nonzero position is not divisible by \(3\), whereas all higher terms are.

Fix \(d\ge2\), and partition the digit positions into
\[
J_C=\{j:j\equiv0\pmod d\},
\qquad
J_A=\mathbb N_0\setminus J_C.
\]
Set
\[
C_{\rm dig}
=
\left\{
\sum_{j\in J_C}\varepsilon_j3^j:
\varepsilon_j\in\{-1,0,1\},\text{ finitely supported}
\right\},
\]
and define \(A_{\rm dig}\) analogously using \(J_A\).

Partitioning the unique balanced ternary digits gives
\[
\mathbb Z=A_{\rm dig}\oplus C_{\rm dig}.
\]
Moreover,
\[
|C_{\rm dig}\cap[-R,R]|\asymp R^{1/d},
\qquad
|A_{\rm dig}\cap[-R,R]|\asymp R^{1-1/d}.
\]
The reason is that a balanced ternary integer with highest nonzero digit at position \(m\) has absolute value between \((3^m+1)/2\) and \((3^{m+1}-1)/2\), while the numbers of allowed positions up to \(m\) are \(m/d+O(1)\) and \((1-1/d)m+O(1)\).

Both sets are infinite and aperiodic. Thus exact aperiodic tilings with precisely the same complementary growth exponents do exist in the digital category. Polynomial-specific information must do more than establish Weyl cancellation and critical Sobolev size.

## Self-Audit

1. **The Fourier product is only a regularized identity, not a product of limiting distributions.**  
   This distinction is essential and is the main reason the route is blocked. The identity itself is secure because, for every \(t<1\), both series converge absolutely and every Fourier coefficient receives exactly one contribution by uniqueness.

2. **The polynomial counting lower bound must count distinct values rather than parameters.**  
   I used only a sufficiently large positive ray on which \(f\) is strictly monotone. Thus all selected values are distinct, including for even polynomials or polynomials with global symmetries.

3. **The claim that Route 3 cannot presently finish is a diagnosis, not an impossibility theorem about all conceivable Fourier methods.**  
   A stronger microlocal or analytic argument might exploit the full two-variable Laurent identity. I believe the stated block is genuine for the standard Abel/Følner approach because its unknown factor is explicitly the height distribution \(t^{H(n)}\), and even hypothetical residue equidistribution supplies no contradiction by itself.

## Computations To Verify

```python
import cmath
import itertools
import math
from collections import defaultdict

TWOPI = 2.0 * math.pi

def e(x):
    return cmath.exp(1j * TWOPI * x)

# ------------------------------------------------------------
# 1. Cube Abel sums and rational Gauss-sum limits
# ------------------------------------------------------------

def cube_abel(eps, theta, tol=1e-14):
    # Choose K so exp(-eps*K^3) is tiny.
    K = max(1, math.ceil((abs(math.log(tol)) / eps) ** (1/3)))
    return sum(
        math.exp(-eps * abs(k)**3) * e(theta * k**3)
        for k in range(-K, K + 1)
    )

def cubic_gauss_mean(q, j):
    return sum(e(j * (r**3) / q) for r in range(q)) / q

def test_cube_limits():
    for q in range(2, 16):
        for j in range(1, q):
            if math.gcd(j, q) != 1:
                continue
            mu = cubic_gauss_mean(q, j)
            print("q,j,mu =", q, j, mu)
            for eps in [0.1, 0.03, 0.01, 0.003]:
                ratio = cube_abel(eps, j/q) / cube_abel(eps, 0.0)
                print("  eps, ratio =", eps, ratio)

    # Irrational probes: normalized values should tend toward zero.
    theta = math.sqrt(2) - 1
    for eps in [0.1, 0.03, 0.01, 0.003, 0.001]:
        ratio = cube_abel(eps, theta) / cube_abel(eps, 0.0)
        print("irrational", eps, ratio, abs(ratio))


# ------------------------------------------------------------
# 2. Exact finite balanced-ternary digital factorization
# ------------------------------------------------------------

def digit_set(positions):
    S = {0}
    for j in positions:
        p = 3**j
        S = {x + digit*p for x in S for digit in (-1, 0, 1)}
    return S

def balanced_factors(M, d):
    c_positions = [j for j in range(M + 1) if j % d == 0]
    a_positions = [j for j in range(M + 1) if j % d != 0]
    return digit_set(a_positions), digit_set(c_positions)

def check_balanced_factorization(M=8, d=3):
    A, C = balanced_factors(M, d)
    reps = {}
    for a in A:
        for c in C:
            n = a + c
            assert n not in reps, ("collision", n, reps[n], (a, c))
            reps[n] = (a, c)

    radius = (3**(M + 1) - 1) // 2
    assert set(reps) == set(range(-radius, radius + 1))
    print("sizes:", len(A), len(C), len(reps), "radius:", radius)

    # Verify the weighted Laurent/Fourier identity numerically.
    t = 0.83
    theta = math.sqrt(5) - 2
    lhs = (
        sum(t**abs(a) * e(theta*a) for a in A)
        * sum(t**abs(c) * e(theta*c) for c in C)
    )
    rhs = sum(
        t**(abs(a) + abs(c)) * e(theta*n)
        for n, (a, c) in reps.items()
    )
    print("Abel identity error:", abs(lhs - rhs))


# ------------------------------------------------------------
# 3. Generic exact Abel identity for any finite direct sum
# ------------------------------------------------------------

def check_finite_abel_identity(A, C, t, theta):
    reps = {}
    for a in A:
        for c in C:
            n = a + c
            if n in reps:
                return False, ("collision", n, reps[n], (a, c))
            reps[n] = (a, c)

    lhs = (
        sum(t**abs(a) * e(theta*a) for a in A)
        * sum(t**abs(c) * e(theta*c) for c in C)
    )
    rhs = sum(
        t**(abs(a) + abs(c)) * e(theta*n)
        for n, (a, c) in reps.items()
    )
    return abs(lhs - rhs) < 1e-10, abs(lhs - rhs)


# ------------------------------------------------------------
# 4. Bounded CP-SAT probe for cube complements
#
# pip install ortools
# This is only a finite model. Unsatisfiability is not a global
# obstruction because a global representation may use |a| > M.
# ------------------------------------------------------------

def bounded_cube_model(N, M):
    from ortools.sat.python import cp_model

    model = cp_model.CpModel()
    centers = list(range(-M, M + 1))
    x = {a: model.NewBoolVar(f"x_{a}") for a in centers}

    # Cubes sufficient for representing |n| <= N using |a| <= M.
    V = N + M
    Kcov = math.ceil(V ** (1/3)) + 2
    cubes_cov = {k**3 for k in range(-Kcov, Kcov + 1)}

    for n in range(-N, N + 1):
        cand = [x[a] for a in centers if n - a in cubes_cov]
        if not cand:
            return None
        model.Add(sum(cand) == 1)

    # Complete cube-difference set for differences of bounded centers.
    # Kdiff = 2M+2 is much larger than necessary but safely complete.
    Kdiff = 2*M + 2
    cube_vals = [k**3 for k in range(-Kdiff, Kdiff + 1)]
    D = {
        u - v
        for u in cube_vals
        for v in cube_vals
        if 0 < abs(u - v) <= 2*M
    }

    for i, a in enumerate(centers):
        for b in centers[i+1:]:
            if b - a in D or a - b in D:
                model.Add(x[a] + x[b] <= 1)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 120
    status = solver.Solve(model)

    if status not in (solver.OPTIMAL, solver.FEASIBLE):
        return None

    A = {a for a in centers if solver.Value(x[a])}
    selector = {}
    for n in range(-N, N + 1):
        pairs = [(a, n-a) for a in A if n-a in cubes_cov]
        assert len(pairs) == 1
        selector[n] = pairs[0]

    return A, selector

def height_residue_profile(selector, eps, q):
    B = [0.0] * q
    for n, (a, c) in selector.items():
        H = abs(a) + abs(c)
        B[n % q] += math.exp(-eps * H)
    total = sum(B)
    return [b / total for b in B]


# Suggested nested experiment:
#
# previous_A = None
# for N, M in [(20,100), (40,400), (80,1600)]:
#     result = bounded_cube_model(N, M)
#     if result is None:
#         print("no bounded model", N, M)
#         break
#     A, selector = result
#     print(N, M, len(A))
#     for q in [2,3,7,9,13]:
#         print(q, height_residue_profile(selector, 1/M, q))
#
# To test genuine compatibility, add constraints fixing x_a to their
# previous values on the old center interval before solving the next stage.
```

The most informative numerical quantities are:

1. the normalized rational values of the cube Abel sum versus \(\mu_{q,j}\);
2. the residue profiles of \(e^{-\varepsilon H(n)}\);
3. growth of
   \[
   \max_{|n|\le N}H(n)/N
   \]
   in compatible bounded models;
4. whether nested solutions survive when all previous center decisions are fixed.

## Route Diagnosis

The route succeeded in producing a fully legitimate Fourier framework: absolute Abel regularization gives an exact analytic identity, and the product converges distributionally to \(\delta_0\). Polynomial growth also yields sharp complementary exponents for \(A\) and \(C_f\). What fails is spectral separation. The regularized product is not a standard approximate identity; its coefficients are \(t^{H(n)}\), and exact tiling gives no useful control of \(H(n)\). Weyl cancellation at irrational frequencies is automatically compatible with the product equation, while rational major arcs only relate unknown height-residue distributions to Abel residue distributions of \(A\). Even proving height equidistribution would not yet force a collision.

A fresh Fourier attempt should therefore target the induced shift on representation pairs,
\[
(a(n),c(n))\longmapsto(a(n+1),c(n+1)),
\]
and prove that the proper length \(H(n)=|a(n)|+|c(n)|\) generates a Følner exhaustion with quantitative distortion bounds. It would then still need a new theorem showing that the resulting major-arc restrictions are incompatible with avoiding \(C_f-C_f\). Without such a selector-height theorem, Route 3 reduces to an unproved nonlocality statement of comparable difficulty and is blocked.