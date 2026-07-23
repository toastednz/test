STATUS: BLOCKED

## Result

Route 2 yields a rigorous analytic consequence: a Sidon set with constant \(C\) is uniformly subgaussian, which gives hereditary bounds on the number and vertex-degrees of signed-relation circuits. However, these bounds are too weak and too aggregate to produce a bounded coloring. I isolate the precise missing step as a compatible-selector/rounding problem, naturally expressed through fractional dissociation coloring. I also construct a uniformly Sidon, two-colorable family having \(\Theta(n^2)\) four-circuits and unbounded circuit degree, showing that direct Riesz-product moment estimates combined with a standard local-lemma argument cannot suffice. No proof or counterexample to Erdős Problem #774 is obtained.

## Complete Argument

### 1. Sidon interpolation measures

Let \(F\subseteq\mathbb Z\) be finite and suppose it has Sidon constant at most \(C\), meaning
\[
\sum_{n\in F}|a_n|
\le C\left\|\sum_{n\in F}a_ne^{2\pi int}\right\|_{L^\infty(\mathbb T)}
\tag{1}
\]
for every coefficient family \((a_n)_{n\in F}\).

#### Lemma 1: interpolation formulation

For every \(z=(z_n)_{n\in F}\) with \(|z_n|\le1\), there is a complex Borel measure \(\mu_z\) on \(\mathbb T\) such that
\[
\|\mu_z\|\le C,\qquad
\int_{\mathbb T}e^{2\pi int}\,d\mu_z(t)=z_n
\quad(n\in F).
\tag{2}
\]

**Proof.**
On the subspace
\[
E_F=\left\{\sum_{n\in F}a_ne^{2\pi int}\right\}\subset C(\mathbb T),
\]
define
\[
L_z\left(\sum_{n\in F}a_ne^{2\pi int}\right)=\sum_{n\in F}a_nz_n.
\]
By (1),
\[
|L_z(f)|
\le \sum_{n\in F}|a_n|
\le C\|f\|_\infty.
\]
Hahn–Banach extends \(L_z\) to a functional on \(C(\mathbb T)\) of norm at most \(C\). The Riesz representation theorem supplies a measure \(\mu_z\) with total variation at most \(C\), and evaluating the extension on the characters gives (2). ∎

Conversely, (2) implies (1) by choosing \(z_n=\overline{a_n}/|a_n|\) when \(a_n\ne0\). Thus this interpolation statement captures exactly the basic harmonic-analytic Sidon information.

---

### 2. Uniform subgaussianity

For a trigonometric polynomial
\[
f(t)=\sum_{n\in F}a_ne^{2\pi int},
\]
and signs \(\varepsilon_n\in\{-1,1\}\), put
\[
f_\varepsilon(t)=\sum_{n\in F}\varepsilon_na_ne^{2\pi int}.
\]

Define
\[
(g\star\mu)(t)=\int_{\mathbb T}g(t+s)\,d\mu(s).
\]
If \(\mu_\varepsilon\) interpolates the signs \(\varepsilon_n\), then
\[
f_\varepsilon=f\star\mu_\varepsilon,
\qquad
f=f_\varepsilon\star\mu_\varepsilon,
\]
because \(\varepsilon_n^2=1\). Translation invariance and Minkowski’s inequality give
\[
\|g\star\mu\|_p\le\|\mu\|\|g\|_p.
\]
Consequently,
\[
\|f\|_p\le C\|f_\varepsilon\|_p
\tag{3}
\]
for every sign choice.

#### Lemma 2: subgaussian estimate

For every \(p\ge2\),
\[
\left\|\sum_{n\in F}a_ne^{2\pi int}\right\|_p
\le 4C\sqrt p\left(\sum_{n\in F}|a_n|^2\right)^{1/2}.
\tag{4}
\]

**Proof.**
For arbitrary complex numbers \(b_n\), let
\[
S=\sum_n\varepsilon_nb_n,\qquad \sigma^2=\sum_n|b_n|^2.
\]
The standard Rademacher estimate
\[
\bigl(\mathbb E_\varepsilon|S|^p\bigr)^{1/p}
\le4\sqrt p\,\sigma
\tag{5}
\]
follows, for example, from
\[
\mathbb E e^{u\operatorname{Re}S}
=\prod_n\cosh(u\operatorname{Re}b_n)
\le e^{u^2\sigma^2/2},
\]
the analogous estimate for \(\operatorname{Im}S\), and integration of the resulting Gaussian tail bound.

Raise (3) to the \(p\)-th power and average over all sign choices:
\[
\|f\|_p^p
\le C^p\mathbb E_\varepsilon\|f_\varepsilon\|_p^p.
\]
By Fubini and (5),
\[
\begin{aligned}
\mathbb E_\varepsilon\|f_\varepsilon\|_p^p
&=\int_{\mathbb T}
 \mathbb E_\varepsilon
 \left|\sum_{n\in F}\varepsilon_na_ne^{2\pi int}\right|^pdt\\
&\le
\left(4\sqrt p\left(\sum_{n\in F}|a_n|^2\right)^{1/2}\right)^p.
\end{aligned}
\]
Taking \(p\)-th roots proves (4). ∎

By Pisier’s characterization quoted in the brief, a proportionately dissociated set with proportionality constant \(\delta\) has a Sidon constant \(C=C(\delta)\). Hence (4) is uniform over all finite subsets of such a set.

---

### 3. Hereditary circuit-count bounds

Let \(B\subseteq F\), \(|B|=n\), and
\[
f_B(t)=\sum_{b\in B}e^{2\pi ibt}.
\]
For \(p,q\ge1\), let \(R_{p,q}(B)\) be the number of ordered solutions
\[
x_1+\cdots+x_p=y_1+\cdots+y_q,
\qquad x_i,y_j\in B,
\]
where repetitions are allowed. Fourier orthogonality gives
\[
R_{p,q}(B)
=\int_{\mathbb T}f_B(t)^p\overline{f_B(t)}^{\,q}\,dt.
\tag{6}
\]

Set \(s=p+q\). By (4),
\[
\begin{aligned}
R_{p,q}(B)
&\le\int_{\mathbb T}|f_B(t)|^sdt\\
&=\|f_B\|_s^s\\
&\le \left(4C\sqrt{s}\sqrt n\right)^s.
\end{aligned}
\tag{7}
\]

#### Proposition 3: number of circuits

Let \(N_s(B)\) be the number of inclusion-minimal signed-relation supports of cardinality \(s\). Then, for \(s\ge3\),
\[
N_s(B)
\le (s-1)(4C\sqrt s)^s n^{s/2}.
\tag{8}
\]

**Proof.**
Every circuit \(S\) of size \(s\) supports a relation
\[
\sum_{x\in X}x=\sum_{y\in Y}y
\]
with \(X\dot\cup Y=S\), \(|X|=p\), \(|Y|=s-p\), and \(1\le p\le s-1\). Choose one orientation and order the two sides canonically. Distinct circuit supports give distinct ordered solutions. Therefore
\[
N_s(B)\le\sum_{p=1}^{s-1}R_{p,s-p}(B).
\]
Apply (7). ∎

A corresponding vertex-degree estimate also follows.

#### Proposition 4: circuits through one vertex

For \(v\in B\), let \(N_s(B;v)\) be the number of \(s\)-circuits containing \(v\). Then
\[
N_s(B;v)
\le
2(s-1)\bigl(4C\sqrt{s-1}\bigr)^{s-1}n^{(s-1)/2}.
\tag{9}
\]

**Proof.**
Fix \(p+q=s\). The number of ordered solutions with \(x_1=v\) is
\[
\int_{\mathbb T}
 e^{2\pi ivt}f_B(t)^{p-1}\overline{f_B(t)}^{\,q}\,dt,
\]
whose absolute value is at most
\[
\int|f_B|^{s-1}
\le
\bigl(4C\sqrt{s-1}\sqrt n\bigr)^{s-1}.
\]
The same estimate applies when \(v\) is placed on the other side. Summing over \(p=1,\dots,s-1\), and again mapping each circuit to a canonical ordered solution, gives (9). ∎

These estimates control all relation lengths, not merely pair-sum or Schur relations.

---

### 4. The selector and fractional-coloring bottleneck

Let \(\mathcal I(F)\) denote the collection of all dissociated subsets of \(F\). Define the fractional dissociation chromatic number by
\[
\chi_{\mathrm{dis}}^*(F)
=
\min\left\{
\sum_{D\in\mathcal I(F)}\lambda_D:
\lambda_D\ge0,\
\sum_{\substack{D\in\mathcal I(F)\\v\in D}}\lambda_D\ge1
\quad(v\in F)
\right\}.
\tag{10}
\]

Its linear-programming dual is
\[
\chi_{\mathrm{dis}}^*(F)
=
\max\left\{
\sum_{v\in F}w_v:
w_v\ge0,\
\sum_{v\in D}w_v\le1
\quad(D\in\mathcal I(F))
\right\}.
\tag{11}
\]

#### Proposition 5: equivalent compatible-selector formulations

For \(\eta>0\), the following are equivalent:

1. \(\chi_{\mathrm{dis}}^*(F)\le1/\eta\);
2. there is a probability distribution on dissociated \(D\subseteq F\) such that
   \[
   \mathbb P(v\in D)\ge\eta
   \quad\text{for every }v\in F;
   \tag{12}
   \]
3. for every nonnegative weight family \(w=(w_v)\), there is a dissociated \(D\subseteq F\) satisfying
   \[
   \sum_{v\in D}w_v\ge\eta\sum_{v\in F}w_v.
   \tag{13}
   \]

**Proof.**

- If (10) has a solution of total mass at most \(1/\eta\), add mass to the empty set so the total is exactly \(1/\eta\), and normalize by multiplying the weights by \(\eta\). This gives (12).
- Given (12), averaging gives
  \[
  \mathbb E\sum_{v\in D}w_v
  =\sum_vw_v\mathbb P(v\in D)
  \ge\eta\sum_vw_v,
  \]
  so some \(D\) satisfies (13).
- Suppose (13) holds and \(w\) is feasible in (11). Since every dissociated \(D\) has \(w(D)\le1\), (13) implies
  \[
  \eta\sum_vw_v\le1.
  \]
  Taking the dual maximum gives \(\chi_{\mathrm{dis}}^*(F)\le1/\eta\). ∎

This identifies a natural analytic intermediate target:

> **Weighted Pisier selector problem.** Does Sidon constant \(C\) imply (13) with \(\eta=\eta(C)>0\)?

I did not prove this. The usual proportional extraction theorem only treats equal weights, and a dyadic reduction loses a logarithm. Indeed, if \(|F|=n\) and every \(B\subseteq F\) has a dissociated subset of size at least \(\delta|B|\), then elementary dyadic decomposition yields only
\[
\max_{D\text{ dissociated}}w(D)
\gg \frac{\delta}{\log(2n)}w(F).
\tag{14}
\]
To see this, discard vertices of weight below \(w(F)/(2n)\), losing at most half the total weight, and divide the remaining weights into at most \(\lceil\log_2(2n)\rceil\) dyadic classes. One class carries at least a reciprocal-logarithmic fraction of the total weight. A dissociated subset occupying a \(\delta\)-fraction of that class carries at least half the corresponding \(\delta\)-fraction of its weight.

Even a uniform fractional bound would not by itself solve the problem: one would still need a bounded integrality-gap theorem
\[
\chi_{\mathrm{dis}}(F)
\le g\bigl(\chi_{\mathrm{dis}}^*(F)\bigr)
\tag{15}
\]
for signed-relation hypergraphs. No such theorem is established here.

Independent sampling from a selector distribution also reproduces the logarithmic obstruction: after \(r\) samples, a fixed vertex is uncovered with probability at most \((1-\eta)^r\), and the union bound requires \(r\asymp_\eta\log n\) to cover all \(n\) vertices.

---

### 5. A sharp stress test for moment/LLL arguments

For \(m\ge2\), let
\[
u_i=3^i,\qquad v_i=3^m+3^i
\quad(0\le i<m),
\]
and set
\[
F_m=\{u_0,\dots,u_{m-1},v_0,\dots,v_{m-1}\}.
\]
Write \(P_i=\{u_i,v_i\}\).

#### Proposition 6: exact relation structure

The circuits of \(F_m\) are exactly
\[
P_i\cup P_j,\qquad 0\le i<j<m,
\tag{16}
\]
supporting
\[
u_i+v_j=v_i+u_j.
\tag{17}
\]

**Proof.**
Suppose
\[
\sum_{i=0}^{m-1}\alpha_i u_i+
\sum_{i=0}^{m-1}\beta_i v_i=0,
\qquad \alpha_i,\beta_i\in\{-1,0,1\}.
\]
With \(M=3^m\), this becomes
\[
M\sum_i\beta_i+\sum_i(\alpha_i+\beta_i)3^i=0.
\tag{18}
\]
Since \(\alpha_i+\beta_i\in\{-2,-1,0,1,2\}\),
\[
\left|\sum_i(\alpha_i+\beta_i)3^i\right|
\le2\sum_{i=0}^{m-1}3^i
=3^m-1<M.
\]
Therefore (18) forces
\[
\sum_i\beta_i=0,
\qquad
\sum_i(\alpha_i+\beta_i)3^i=0.
\]
If \(\gamma_i\in[-2,2]\cap\mathbb Z\) and
\(\sum_i\gamma_i3^i=0\), choose the largest \(r\) with
\(\gamma_r\ne0\). Then
\[
|\gamma_r|3^r\ge3^r
>
2\sum_{i<r}3^i=3^r-1,
\]
a contradiction. Hence \(\alpha_i=-\beta_i\) for every \(i\).

Thus every relation is specified by a nonzero vector
\(\beta\in\{-1,0,1\}^m\) with \(\sum_i\beta_i=0\), and each nonzero
\(\beta_i\) places both vertices of \(P_i\) in its support. Such a relation contains one with exactly one \(+1\) and one \(-1\). It is inclusion-minimal precisely in that case, yielding (16) and (17). ∎

#### Corollary 7: exact hereditary ratio and chromatic number

For \(m\ge2\),
\[
\rho(F_m)=\frac{m+1}{2m}>\frac12,
\qquad
\chi_{\mathrm{dis}}(F_m)=2.
\tag{19}
\]

**Proof.**
A subset is dissociated exactly when it contains at most one complete pair \(P_i\). If \(B\subseteq F_m\) contains \(r\) complete pairs and \(s\) additional singleton vertices, then
\[
\alpha_{\mathrm{dis}}(B)=
\begin{cases}
|B|,&r\le1,\\
r+s+1,&r\ge2.
\end{cases}
\]
For fixed \(r\ge2\), the ratio
\[
\frac{r+s+1}{2r+s}
\]
is minimized at \(s=0\), and \((r+1)/(2r)\) decreases with \(r\). The minimum is therefore attained at \(B=F_m\), giving the first assertion.

The two layers \(\{u_i\}\) and \(\{v_i\}\) are dissociated, so two colors suffice. Since \(F_m\) has a circuit when \(m\ge2\), one color does not suffice. ∎

There are
\[
\binom m2=\Theta(|F_m|^2)
\]
four-circuits, and every vertex belongs to \(m-1\) of them. Thus the exponent \(n^{s/2}\) in (8) is already sharp at \(s=4\), even among uniformly proportionately dissociated sets.

For a uniformly random \(k\)-coloring, the event that a fixed four-circuit is monochromatic has probability \(k^{-3}\). The dependency graph of the circuit events is the line graph of \(K_m\), of degree
\[
2(m-2).
\]
Hence the standard symmetric local-lemma condition
\[
e\,k^{-3}\bigl(2m-3\bigr)\le1
\]
fails for every fixed \(k\) and sufficiently large \(m\), even though the sets are explicitly two-colorable.

These examples can be placed, by scale separation, inside one infinite union of two dissociated sets. Therefore unbounded circuit degree occurs inside a single Sidon set with one fixed Sidon constant; it is not an artifact of allowing the constants to vary.

---

## Self-Audit

1. **Use of Pisier’s quantitative equivalence.** I rely on the quoted theorem to pass from proportionality constant \(\delta\) to a uniform Sidon constant \(C(\delta)\). This is external to the argument, but it is explicitly part of the problem brief. All analytic lemmas are also stated and proved conditionally on a given \(C\).

2. **The local-lemma obstruction is limited.** The family \(F_m\) proves only that aggregate circuit counts and the standard symmetric dependency criterion are inadequate. It does not rule out asymmetric LLL, entropy compression, or an argument exploiting the special rectangular organization of the circuits. I believe the stated limitation because the exact circuit hypergraph and dependency degree were proved, but I do not claim a general impossibility theorem.

3. **The selector bottleneck is a diagnosis, not a disproof of Route 2.** Proposition 5 rigorously identifies fractional coloring with weighted selectors, but I did not prove that harmonic analysis cannot supply more structured, jointly covering selectors. The block is genuine because neither \(C\Rightarrow\chi_{\mathrm{dis}}^*=O_C(1)\) nor bounded fractional-to-integral rounding was established.

## Computations To Verify

The following exact Python checks the stress-test family, computes all minimal circuit supports, the hereditary ratio, and the dissociation chromatic number for small cases.

```python
from itertools import product
from fractions import Fraction

def stress_family(m):
    U = [3**i for i in range(m)]
    M = 3**m
    V = [M + 3**i for i in range(m)]
    return U + V

def is_dissociated(vals, mask):
    sums = {0}
    for i, x in enumerate(vals):
        if (mask >> i) & 1:
            shifted = {s + x for s in sums}
            if sums & shifted:
                return False
            sums |= shifted
    return True

def all_dissociation_flags(vals):
    return [
        is_dissociated(vals, mask)
        for mask in range(1 << len(vals))
    ]

def hereditary_ratio(vals):
    n = len(vals)
    diss = all_dissociation_flags(vals)
    alpha = [0] * (1 << n)

    # Process by increasing cardinality.
    masks = sorted(range(1 << n), key=int.bit_count)
    for mask in masks:
        if diss[mask]:
            alpha[mask] = mask.bit_count()
        elif mask:
            alpha[mask] = max(
                alpha[mask ^ (1 << i)]
                for i in range(n) if (mask >> i) & 1
            )

    rho = min(
        Fraction(alpha[mask], mask.bit_count())
        for mask in range(1, 1 << n)
    )
    return rho, alpha

def minimal_circuit_masks(vals):
    n = len(vals)
    dependent_supports = set()

    for eps in product((-1, 0, 1), repeat=n):
        try:
            first = next(i for i, e in enumerate(eps) if e)
        except StopIteration:
            continue

        # Quotient out global sign reversal.
        if eps[first] != 1:
            continue

        if sum(e * x for e, x in zip(eps, vals)) == 0:
            mask = 0
            for i, e in enumerate(eps):
                if e:
                    mask |= 1 << i
            dependent_supports.add(mask)

    circuits = []
    for s in dependent_supports:
        if not any(t != s and (t & s) == t
                   for t in dependent_supports):
            circuits.append(s)
    return sorted(circuits)

def expected_stress_circuits(m):
    # Vertex order is U_0,...,U_{m-1},V_0,...,V_{m-1}.
    pairs = [(1 << i) | (1 << (m + i)) for i in range(m)]
    return sorted(
        pairs[i] | pairs[j]
        for i in range(m) for j in range(i + 1, m)
    )

def dissociation_chromatic_number(vals, circuits=None):
    n = len(vals)
    if circuits is None:
        circuits = minimal_circuit_masks(vals)

    for k in range(1, n + 1):
        for colors in product(range(k), repeat=n):
            # Remove color-permutation symmetry.
            if colors[0] != 0:
                continue

            valid = True
            for edge in circuits:
                vertices = [i for i in range(n) if (edge >> i) & 1]
                if len({colors[i] for i in vertices}) == 1:
                    valid = False
                    break
            if valid:
                return k
    raise RuntimeError("No coloring found")

for m in range(2, 7):
    F = stress_family(m)
    circuits = minimal_circuit_masks(F)
    expected = expected_stress_circuits(m)
    assert circuits == expected

    rho, _ = hereditary_ratio(F)
    assert rho == Fraction(m + 1, 2 * m)

    chi = dissociation_chromatic_number(F, circuits)
    assert chi == 2

    degree = []
    for v in range(2 * m):
        degree.append(sum((edge >> v) & 1 for edge in circuits))
    assert set(degree) == {m - 1}

    print(m, len(F), rho, chi, len(circuits), degree[0])
```

Expected output has
\[
|F_m|=2m,\quad
\rho(F_m)=\frac{m+1}{2m},\quad
\chi_{\mathrm{dis}}(F_m)=2,\quad
\#\text{circuits}=\binom m2.
\]

Moment counts can be checked exactly as follows:

```python
from collections import Counter

def ordered_sum_counts(vals, r):
    counts = Counter({0: 1})
    for _ in range(r):
        nxt = Counter()
        for s, c in counts.items():
            for x in vals:
                nxt[s + x] += c
        counts = nxt
    return counts

def R_pq(vals, p, q):
    cp = ordered_sum_counts(vals, p)
    cq = ordered_sum_counts(vals, q)
    return sum(cp[s] * cq[s] for s in cp.keys() & cq.keys())

for m in range(2, 8):
    F = stress_family(m)
    print(m, R_pq(F, 2, 2), "circuits =", m * (m - 1) // 2)
```

For computational investigation of the analytic bottleneck, enumerate all dissociated masks and solve the fractional-cover LP:

```python
import numpy as np
from scipy.optimize import linprog

def fractional_dissociation_chromatic(vals):
    n = len(vals)
    independent = [
        mask for mask in range(1 << n)
        if is_dissociated(vals, mask)
    ]

    # Variables lambda_D; minimize sum lambda_D.
    c = np.ones(len(independent))
    A = np.zeros((n, len(independent)))
    for v in range(n):
        for j, mask in enumerate(independent):
            if (mask >> v) & 1:
                A[v, j] = -1.0
    b = -np.ones(n)

    result = linprog(
        c, A_ub=A, b_ub=b,
        bounds=[(0, None)] * len(independent),
        method="highs"
    )
    assert result.success
    return result.fun
```

The decisive search is for finite integer sets with bounded hereditary ratio but either:

```text
(a) unbounded fractional dissociation chromatic number, or
(b) bounded fractional number but unbounded integral number.
```

Either phenomenon would directly identify where Riesz-product selector methods must fail.

## Route Diagnosis

**Proved:**

- Sidon interpolation measures imply the uniform subgaussian inequality (4).
- This gives hereditary circuit-count and circuit-degree bounds (8)–(9) for every relation length.
- Weighted dissociated selectors are exactly equivalent to bounded fractional dissociation coloring.
- The explicit family \(F_m\) has exact circuit hypergraph
  \[
  \{P_i\cup P_j:i<j\},
  \]
  hereditary ratio \((m+1)/(2m)\), chromatic number \(2\), \(\Theta(n^2)\) four-circuits, and unbounded circuit degree.

**Plausible but unproved:**

- A Sidon constant \(C\) may force a bounded fractional dissociation chromatic number.
- Additional arithmetic structure might permit bounded rounding from fractional covers, but no mechanism emerged.
- More sophisticated correlated Riesz-product selectors might contain information absent from arbitrary interpolation measures.

**Dead ends:**

- Independent repetition of large quasi-independent selectors loses \(\Theta(\log n)\) samples when covering all vertices.
- Dyadic reduction from unweighted to weighted extraction also loses \(\Theta(\log n)\).
- Moment bounds plus the standard circuit-event local lemma fail badly on the explicit two-colorable family \(F_m\).
- Aggregate bounds on the number of relations do not reveal the low-complexity organization needed for coloring.

**Precise block:** classical Sidon/Riesz-product machinery supplies one large quasi-independent subset or one interpolation measure for each prescribed sign pattern. It supplies neither a bounded family of compatible selectors covering all frequencies nor a bounded integrality-gap theorem. Producing either would be a substantial new structural result; producing both would solve the problem.

A fresh attempt should first test the weighted selector question computationally through \(\chi_{\mathrm{dis}}^*\). If bounded Sidon constant allows unbounded \(\chi_{\mathrm{dis}}^*\), that points directly toward Route 6 and a counterexample. If \(\chi_{\mathrm{dis}}^*\) remains bounded while \(\chi_{\mathrm{dis}}\) grows, the central issue is arithmetic fractional-to-integral rounding.