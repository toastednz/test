STATUS: SOLVED-PROOF

## Result

The intended transcendental version has an affirmative solution. A probabilistic construction works: let \((\xi_m)_{m\ge0}\) be independent standard complex Gaussian variables and set
\[
f(z)=\sum_{m=0}^{\infty}\xi_m\frac{z^m}{(m!)^{1/4}}.
\]
Almost surely this is transcendental entire. For every disc \(D\), the expected number of zeros of \(f^{(n)}\) in a fixed smaller subdisc of \(D\), measured by a smooth nonnegative test function, grows at least like \(n^{3/4}\), while the variance of that smooth zero statistic is bounded independently of \(n\). Consequently, the probability that \(f^{(n)}\) has no zero in \(D\) is \(O_D(n^{-3/2})\). Borel–Cantelli, followed by a countable-basis argument, gives almost surely that every disc is met by every sufficiently high derivative.

## Complete Argument

### 1. The random entire function

Let \(\xi_0,\xi_1,\ldots\) be independent standard complex Gaussian random variables, each with density
\[
\frac1\pi e^{-|z|^2}\,dA(z).
\]
Fix
\[
\alpha=\frac34
\]
and define
\[
f(z)=\sum_{m=0}^{\infty}\xi_m(m!)^\alpha\frac{z^m}{m!}
=\sum_{m=0}^{\infty}\xi_m\frac{z^m}{(m!)^{1/4}}.
\tag{1}
\]

Almost surely, \(f\) is entire. Indeed,
\[
\Pr\bigl(|\xi_m|>e^m\bigr)=e^{-e^{2m}},
\]
and these probabilities are summable. Thus, by Borel–Cantelli, almost surely \(|\xi_m|\le e^m\) for all sufficiently large \(m\). Hence
\[
\left|\frac{\xi_m}{(m!)^{1/4}}\right|^{1/m}
\le
\frac{e}{(m!)^{1/(4m)}}\longrightarrow 0.
\]
The series therefore has infinite radius of convergence.

Also, \(\Pr(\xi_m=0)=0\) for every \(m\). Almost surely all coefficients in (1) are nonzero, so \(f\) is not a polynomial.

Termwise differentiation gives
\[
f^{(n)}(z)
=
\sum_{r=0}^{\infty}
\xi_{n+r}\frac{((n+r)!)^\alpha}{r!}z^r.
\tag{2}
\]

We will prove that almost every realization of (1) has the required property.

---

### 2. A uniform variance bound for smooth zero statistics

We first record a general Gaussian analytic-function lemma.

#### Lemma 1

Let \(G\) be a nondegenerate complex Gaussian analytic function on a neighborhood of the support of a real-valued function \(\phi\in C_c^\infty(\mathbb C)\). Let
\[
X_\phi(G)=\sum_{G(z)=0}\phi(z),
\]
where zeros are counted with multiplicity. If
\[
K(z,w)=\mathbb E[G(z)\overline{G(w)}],
\]
then
\[
\mathbb E X_\phi(G)
=
\frac1{4\pi}\int_{\mathbb C}\phi(z)\Delta\log K(z,z)\,dA(z),
\tag{3}
\]
and
\[
\operatorname{Var}X_\phi(G)
\le
\frac1{96}
\left(\int_{\mathbb C}|\Delta\phi(z)|\,dA(z)\right)^2.
\tag{4}
\]

#### Proof

The distributional identity
\[
\frac1{2\pi}\Delta\log|G|
=
\sum_{G(z)=0}\delta_z
\]
gives
\[
X_\phi(G)
=
\frac1{2\pi}\int_{\mathbb C}\Delta\phi(z)\log|G(z)|\,dA(z).
\tag{5}
\]

For each fixed \(z\),
\[
\frac{G(z)}{\sqrt{K(z,z)}}
\]
is a standard complex Gaussian. Thus
\[
\mathbb E\log|G(z)|
=
\frac12\log K(z,z)+c_0,
\]
where \(c_0=\mathbb E\log|\xi_0|\). Since \(\int\Delta\phi\,dA=0\), taking expectations in (5) gives (3).

Let
\[
Y(z)=
\log|G(z)|-\frac12\log K(z,z)-c_0.
\]
Every \(Y(z)\) has the same variance as \(\log|\xi_0|\). Since \(|\xi_0|^2\) is exponentially distributed,
\[
\operatorname{Var}(\log|\xi_0|)
=
\frac14\operatorname{Var}\bigl(\log|\xi_0|^2\bigr)
=
\frac{\pi^2}{24}.
\tag{6}
\]
For example, this follows by differentiating
\[
\mathbb E\bigl[|\xi_0|^{2s}\bigr]=\Gamma(1+s)
\]
twice at \(s=0\).

By Cauchy–Schwarz,
\[
|\operatorname{Cov}(Y(z),Y(w))|
\le \frac{\pi^2}{24}.
\]
Subtracting the expectation from (5), applying Fubini and then this covariance bound, we obtain
\[
\begin{aligned}
\operatorname{Var}X_\phi(G)
&=
\frac1{4\pi^2}
\iint
\Delta\phi(z)\Delta\phi(w)
\operatorname{Cov}(Y(z),Y(w))
\,dA(z)dA(w)\\
&\le
\frac1{4\pi^2}\frac{\pi^2}{24}
\left(\int|\Delta\phi|\,dA\right)^2,
\end{aligned}
\]
which is (4). All integrals are legitimate because the centered logarithm of a standard complex Gaussian has a finite second moment. ∎

---

### 3. Covariance kernel of \(f^{(n)}\)

From (2), the covariance kernel of \(f^{(n)}\) is
\[
K_n(z,w)
=
\sum_{r=0}^{\infty}
\frac{((n+r)!)^{2\alpha}}{(r!)^2}(z\overline w)^r.
\]
Factoring out \((n!)^{2\alpha}\), define
\[
S_n(t)
=
\sum_{r=0}^{\infty}
\frac{\left((n+r)!/n!\right)^{2\alpha}}{(r!)^2}t^r,
\qquad t\ge0.
\tag{7}
\]
Then
\[
K_n(z,z)=(n!)^{2\alpha}S_n(|z|^2).
\tag{8}
\]

For \(t>0\), introduce a probability distribution on \(\mathbb N\cup\{0\}\):
\[
p_{n,t}(r)
=
\frac{1}{S_n(t)}
\frac{\left((n+r)!/n!\right)^{2\alpha}}{(r!)^2}t^r.
\tag{9}
\]
Let \(R_{n,t}\) be a random variable with this distribution.

A direct differentiation gives
\[
t\frac{S_n'(t)}{S_n(t)}=\mathbb E R_{n,t}
\]
and hence
\[
\frac{d}{dt}\left(t\frac{S_n'(t)}{S_n(t)}\right)
=
\frac{\operatorname{Var}(R_{n,t})}{t}.
\tag{10}
\]
For a radial function \(F(|z|^2)\),
\[
\Delta F(|z|^2)
=
4\frac{d}{dt}\bigl(tF'(t)\bigr)\Big|_{t=|z|^2}.
\]
Consequently,
\[
\frac1{4\pi}\Delta\log K_n(z,z)
=
\frac{\operatorname{Var}(R_{n,|z|^2})}{\pi |z|^2},
\qquad z\ne0.
\tag{11}
\]

It remains to lower-bound this variance.

---

### 4. The coefficient-index distribution has variance of order \(n^\alpha\)

#### Lemma 2

Let \(0<\alpha<1\), and let \(0<t_0<t_1<\infty\). There are constants \(c>0\) and \(N\), depending only on \(\alpha,t_0,t_1\), such that
\[
\operatorname{Var}(R_{n,t})\ge c n^\alpha
\tag{12}
\]
for every \(n\ge N\) and every \(t\in[t_0,t_1]\).

#### Proof

Write the unnormalized weights in (9) as
\[
w_r=
\frac{\left((n+r)!/n!\right)^{2\alpha}}{(r!)^2}t^r.
\]
Their consecutive ratios are
\[
q_r:=\frac{w_{r+1}}{w_r}
=
t\frac{(n+r+1)^{2\alpha}}{(r+1)^2}.
\tag{13}
\]

These ratios are strictly decreasing. Indeed,
\[
\frac{q_{r+1}}{q_r}
=
\left(1+\frac1{n+r+1}\right)^{2\alpha}
\left(1+\frac1{r+1}\right)^{-2}<1,
\]
because
\[
\left(1+\frac1{n+r+1}\right)^\alpha
<
1+\frac1{r+1}.
\]

Let \(m\) be the mode index characterized by
\[
q_{m-1}\ge1\ge q_m.
\tag{14}
\]
Uniformly for \(t\in[t_0,t_1]\),
\[
c_0n^\alpha\le m\le C_0n^\alpha
\tag{15}
\]
for suitable positive constants \(c_0,C_0\). To see this, if
\[
r+1\le \frac{\sqrt{t_0}}2 n^\alpha,
\]
then \(q_r\ge4\) for all sufficiently large \(n\). On the other hand, since \(n^\alpha=o(n)\), for
\[
r+1\ge 2^{\alpha+1}\sqrt{t_1}\,n^\alpha
\]
we have \(n+r+1\le2n\) for large \(n\), and then \(q_r\le1/4\).

Set
\[
d_r=\log q_r-\log q_{r+1}.
\]
From (13),
\[
d_r
=
2\log\left(1+\frac1{r+1}\right)
-
2\alpha\log\left(1+\frac1{n+r+1}\right).
\tag{16}
\]
Because \(m\asymp n^\alpha=o(n)\), there are constants \(c_1,C_1>0\) such that, uniformly for
\[
\frac m2\le r\le2m,
\]
one has
\[
\frac{c_1}{m}\le d_r\le\frac{C_1}{m}.
\tag{17}
\]
Indeed, use
\[
\frac{x}{1+x}\le\log(1+x)\le x
\]
in (16); the term of size \(1/n\) is \(o(1/m)\).

By (14) and (17),
\[
|\log q_{m-1}|+|\log q_m|\le \frac{C_2}{m}.
\tag{18}
\]
Summing (17) away from the mode and then summing the resulting bounds for \(\log q_r\) yields constants \(c_2,C_2,C_3>0\) such that, whenever \(|k|\le m/2\),
\[
C_3^{-1}e^{-C_2k^2/m}
\le
\frac{w_{m+k}}{w_m}
\le
C_3e^{-c_2k^2/m}.
\tag{19}
\]

For completeness, on the right this follows from
\[
\log\frac{w_{m+k}}{w_m}
=
\sum_{j=0}^{k-1}\log q_{m+j},
\]
while
\[
-\frac{C(j+1)}m
\le \log q_{m+j}\le-\frac{cj-C}m.
\]
The left side is identical after writing
\[
\log\frac{w_{m-k}}{w_m}
=
-\sum_{j=1}^{k}\log q_{m-j}.
\]

Moreover, at distance \(m/4\) from the mode, (17) shows that \(q_r\) differs from \(1\) by a fixed multiplicative factor. Since the \(q_r\) are decreasing, the remaining tails are bounded by geometric series. Thus (19) implies
\[
\sum_{r\ge0}w_r\le C_4\sqrt m\,w_m.
\tag{20}
\]

Now consider the two intervals
\[
I_-=[m-2\sqrt m,m-\sqrt m],
\qquad
I_+=[m+\sqrt m,m+2\sqrt m].
\]
For large \(m\), both lie in \([m/2,2m]\). The lower bound in (19) and the upper bound (20) show that
\[
\Pr(R_{n,t}\in I_-)\ge c_3,
\qquad
\Pr(R_{n,t}\in I_+)\ge c_3
\tag{21}
\]
for a fixed \(c_3>0\).

Let \(R'\) be an independent copy of \(R_{n,t}\). Since the two intervals in (21) are separated by at least \(2\sqrt m\),
\[
\begin{aligned}
\operatorname{Var}(R_{n,t})
&=\frac12\mathbb E(R_{n,t}-R')^2\\
&\ge c_4m.
\end{aligned}
\]
Together with \(m\ge c_0n^\alpha\), this proves (12). ∎

For our chosen \(\alpha=3/4\), equations (11) and (12) imply the following: for every compact annulus
\[
0<a\le |z|\le b<\infty,
\]
there are \(c_{a,b}>0\) and \(N_{a,b}\) such that
\[
\frac1{4\pi}\Delta\log K_n(z,z)
\ge c_{a,b}n^{3/4}
\tag{22}
\]
throughout that annulus whenever \(n\ge N_{a,b}\).

---

### 5. Summable hole probabilities

Let \(D\) be any nonempty open disc. Choose a nonnegative, nonzero function
\[
\phi\in C_c^\infty(D)
\]
whose support avoids the origin. This is always possible, even when \(0\in D\), by choosing a smaller disc centered at a nonzero point of \(D\).

Let
\[
X_{n,\phi}
=
\sum_{f^{(n)}(z)=0}\phi(z).
\]
By Lemma 1 and (22), there is a constant \(c_\phi>0\) such that
\[
\mathbb E X_{n,\phi}\ge c_\phi n^{3/4}
\tag{23}
\]
for all sufficiently large \(n\).

Lemma 1 also gives a constant \(C_\phi\), independent of \(n\), such that
\[
\operatorname{Var}X_{n,\phi}\le C_\phi.
\tag{24}
\]

Because \(\phi\ge0\), if \(X_{n,\phi}=0\), then
\[
|X_{n,\phi}-\mathbb EX_{n,\phi}|
\ge \mathbb EX_{n,\phi}.
\]
Chebyshev's inequality, (23), and (24) therefore give
\[
\Pr(X_{n,\phi}=0)
\le
\frac{C_\phi}{c_\phi^2n^{3/2}}.
\tag{25}
\]
In particular,
\[
\sum_{n=1}^{\infty}\Pr(X_{n,\phi}=0)<\infty.
\tag{26}
\]

If \(f^{(n)}\) has no zero in \(D\), then \(X_{n,\phi}=0\). Hence
\[
\sum_{n=1}^{\infty}
\Pr\bigl(Z_n(f)\cap D=\varnothing\bigr)<\infty.
\tag{27}
\]

The first Borel–Cantelli lemma, which requires no independence between derivative orders, now shows that almost surely only finitely many \(n\) satisfy
\[
Z_n(f)\cap D=\varnothing.
\tag{28}
\]

---

### 6. Simultaneous conclusion for every disc

Let \(\{D_j:j\ge1\}\) be the countable rational basis of discs. Applying (28) to every \(D_j\), and intersecting the resulting probability-one events, we obtain a probability-one event on which
\[
\forall j\ \exists N_j\ \forall n\ge N_j,\qquad
Z_n(f)\cap D_j\ne\varnothing.
\tag{29}
\]

Intersect this event with the probability-one event on which \(f\) is entire and transcendental. Choose any realization in the intersection.

Every nonempty open disc contains a rational basis disc \(D_j\), so (29) implies
\[
\forall D\ne\varnothing\text{ open disc}\quad
\exists N_D\quad
\forall n\ge N_D,\quad
Z_n(f)\cap D\ne\varnothing.
\]
This is exactly \((P'')\), and hence is equivalent to the original “every increasing sequence” property.

Thus a transcendental entire function satisfying Erdős Problem #906 exists. ∎

## Self-Audit

1. **The main quantitative input is Lemma 2.**  
   Its weakest part is the passage from the ratio bounds to the two-sided Gaussian estimate (19). The proof supplies the needed mechanism explicitly: \(\log q_r\) changes by \(\asymp1/m\) per step near the mode, so summing once gives \(\log q_{m+j}\asymp-j/m\), and summing again gives \(\log(w_{m+k}/w_m)\asymp-k^2/m\). Monotonicity of \(q_r\) controls the remaining tails.

2. **Poincaré–Lelong is applied to the singular function \(\log|G|\).**  
   This is legitimate distributionally. The expectation and variance manipulations are justified because the centered logarithm at every point has uniformly bounded second moment. If desired, one can first replace \(\log|G|\) by \(\frac12\log(|G|^2+\varepsilon)\), perform all integrations, and pass to the limit in \(L^2_{\mathrm{loc}}\).

3. **The witness is nonexplicit.**  
   The proof only shows that almost every Gaussian realization works. This is nevertheless a valid existence proof. No independence among the events for different \(n\) is used: the first Borel–Cantelli lemma follows solely from the summable marginal bounds (25).

## Computations To Verify

The coefficient-index variance and expected zero-density lower bound can be checked directly.

```python
import math
import numpy as np

alpha = 0.75

def index_distribution_stats(n, t, alpha=alpha):
    # Mode is approximately sqrt(t) * n**alpha.
    mode_guess = max(1, int(math.sqrt(t) * n**alpha))
    R = int(5 * mode_guess + 20 * math.sqrt(mode_guess) + 100)

    logw = np.empty(R + 1)
    logw[0] = 0.0

    for r in range(R):
        # w_{r+1}/w_r = t*(n+r+1)^(2 alpha)/(r+1)^2
        logq = (
            math.log(t)
            + 2 * alpha * math.log(n + r + 1)
            - 2 * math.log(r + 1)
        )
        logw[r + 1] = logw[r] + logq

    logw -= np.max(logw)
    p = np.exp(logw)
    p /= np.sum(p)

    r = np.arange(R + 1, dtype=float)
    mean = np.sum(r * p)
    var = np.sum((r - mean)**2 * p)
    mode = int(np.argmax(p))
    density = var / (math.pi * t)

    # Tail warning: the last weights should be negligible.
    tail_indicator = p[-1]

    return {
        "mode": mode,
        "mode_scaled": mode / n**alpha,
        "mean": mean,
        "variance": var,
        "variance_scaled": var / n**alpha,
        "expected_zero_density": density,
        "tail_probability_at_cutoff": tail_indicator,
    }

for t in [0.25, 1.0, 4.0]:
    for n in [100, 300, 1000, 3000, 10000]:
        print(t, n, index_distribution_stats(n, t))
```

The expected output should show that both the mode and variance, divided by \(n^{3/4}\), remain bounded above and away from zero.

A finite Monte Carlo test of the hole probabilities can be run as follows. This is exploratory rather than certified, because it truncates the derivative series.

```python
import numpy as np
import math

def sample_complex_gaussian(size):
    return (
        np.random.normal(size=size)
        + 1j * np.random.normal(size=size)
    ) / math.sqrt(2)

def derivative_truncation_coeffs(xi, n, R, alpha=0.75):
    # Ascending coefficients of f^(n):
    # xi[n+r] * ((n+r)!)^alpha / r!
    logs = np.array([
        alpha * math.lgamma(n + r + 1) - math.lgamma(r + 1)
        for r in range(R + 1)
    ])
    scale = np.max(logs)
    coeff = np.array([
        xi[n+r] * math.exp(logs[r] - scale)
        for r in range(R + 1)
    ])
    return coeff

def has_root_in_disc(coeff_ascending, center, radius):
    # numpy.roots expects descending coefficients.
    roots = np.roots(coeff_ascending[::-1])
    return np.any(np.abs(roots - center) < radius)

def estimate_hole_probability(n, center, radius,
                              trials=1000, alpha=0.75):
    # Effective degree on a bounded set is of order n^alpha.
    R = int(6 * (abs(center) + radius + 1) * n**alpha + 50)
    holes = 0

    for _ in range(trials):
        xi = sample_complex_gaussian(n + R + 1)
        coeff = derivative_truncation_coeffs(xi, n, R, alpha)

        if not has_root_in_disc(coeff, center, radius):
            holes += 1

    return holes / trials

for n in [30, 60, 120, 240]:
    p = estimate_hole_probability(
        n=n,
        center=1.0 + 0.5j,
        radius=0.25,
        trials=500
    )
    print(n, p, "scaled:", p * n**1.5)
```

For certified finite verification, one should replace `numpy.roots` by ball-arithmetic root isolation and bound the omitted tail on the boundary using the exact coefficient ratio
\[
\frac{w_{r+1}}{w_r}
=
t\frac{(n+r+1)^{3/2}}{(r+1)^2}.
\]

## Route Diagnosis

The direct coefficient-block route has a genuine transition problem. A useful finite packet is
\[
Q(z)=\prod_{j=1}^s(z-w_j)^M.
\]
Then \(Q^{(k)}(w_j)=0\) for every \(j\le s\) and \(0\le k<M\). Thus an \(N\)-fold antiderivative of \(Q\) controls \(M\) consecutive derivatives. However, its degree is \(N+sM\). If the next disjoint block starts after that degree, approximately \((s-1)M\) derivative orders remain uncontrolled; if the next block starts immediately after the controlled interval, the coefficient blocks overlap heavily. Exact finite differential interpolation removes the algebraic obstruction, but no satisfactory quantitative extension lemma emerged that simultaneously preserves old zeros, handles adjacent derivative orders, and maintains summable compact-uniform perturbations. Cauchy estimates show why a naive “tiny old derivative but arbitrarily large next derivative” argument cannot work across a fixed protected contour.

The probabilistic construction bypasses this block-transition issue entirely. Its essential successful features are:

- coefficient growth \((m!)^{3/4}\) in exponential-generating coordinates remains subfactorial, so \(f\) is entire;
- the effective number of competing terms in \(f^{(n)}\) on any compact set away from \(0\) is \(\asymp n^{3/4}\);
- smooth zero statistics have uniformly bounded variance;
- the resulting \(O(n^{-3/2})\) hole estimate is summable.

Ledger:

- **Proved:** the Gaussian zero-statistic variance bound; the coefficient-index variance lower bound; summable hole probabilities; almost-sure eventual zero-hitting in every rational disc.
- **Plausible but unnecessary:** a sufficiently quantitative exact-interpolation block lemma may still yield a deterministic explicit construction.
- **Dead end:** disjoint multiplicity blocks without overlap, because their degree overhead leaves uncontrolled derivative orders.