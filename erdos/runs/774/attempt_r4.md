STATUS: BLOCKED

## Result

Route 4 does not currently yield a solution. I proved three rigorous obstructions to the proposed matroidal strategy, all already occurring for finite sets with hereditary dissociation ratio at least \(1/2\): the dissociation rank is not submodular; proportional dissociation does not imply any bounded approximate exchange or \(p\)-system property; and the dissociation independence system cannot be represented as the intersection of \(q=q(\delta)\) matroids. The last two failures are quantitative and unbounded. However, the constructed sets are themselves unions of two dissociated sets, so they are not counterexamples to Erdős Problem #774. The remaining possible matroid route—constructing a single inner matroid whose rank approximates dissociation rank uniformly—would immediately solve the original problem by matroid partition, but I found no way to construct such a matroid or to rule it out. Thus the route is blocked at a statement of essentially comparable strength to the original problem.

## Complete Argument

### 1. What a successful matroid approximation would imply

Write
\[
r_{\mathrm{dis}}(B)=\alpha_{\mathrm{dis}}(B).
\]

Two precise matroidal mechanisms would suffice.

#### Lemma 1.1: An inner rank-approximating matroid would solve the problem

Suppose that for every finite \(F\subseteq\mathbb N\) satisfying
\[
r_{\mathrm{dis}}(B)\ge \delta |B|
\qquad(B\subseteq F),
\]
there is a matroid \(M\) on \(F\), with rank function \(r_M\), such that:

1. every \(M\)-independent set is dissociated;
2. for some \(c=c(\delta)>0\),
   \[
   r_M(B)\ge c\,r_{\mathrm{dis}}(B)
   \qquad(B\subseteq F).
   \]

Then
\[
\chi_{\mathrm{dis}}(F)\le \left\lceil\frac1{c\delta}\right\rceil.
\]

**Proof.**
Set \(k=\lceil 1/(c\delta)\rceil\). For every \(B\subseteq F\),
\[
k r_M(B)\ge k c\,r_{\mathrm{dis}}(B)
\ge k c\delta |B|\ge |B|.
\]
By the matroid partition theorem, \(F\) can be partitioned into \(k\) \(M\)-independent sets. Each is dissociated by assumption. ∎

Thus finding such a matroid is already enough for a complete positive solution.

#### Lemma 1.2: A bounded intersection of matroids would solve the problem

Suppose that on every such \(F\), there are matroids \(M_1,\dots,M_q\), where \(q=q(\delta)\), satisfying
\[
\mathcal I_{\mathrm{dis}}(F)
=
\bigcap_{j=1}^q \mathcal I(M_j).
\]
Then
\[
\chi_{\mathrm{dis}}(F)
\le
\left\lceil\frac1\delta\right\rceil^q.
\]

**Proof.**
Every dissociated subset of \(B\) is independent in every \(M_j\). Hence
\[
r_{M_j}(B)\ge r_{\mathrm{dis}}(B)\ge\delta |B|.
\]
Let \(k=\lceil1/\delta\rceil\). The matroid partition theorem gives, for each \(j\), a partition of \(F\) into \(k\) sets independent in \(M_j\).

Assign to each \(v\in F\) the \(q\)-tuple of its colors in these \(q\) partitions. Each common color class is independent in every \(M_j\), hence dissociated. There are at most \(k^q\) color tuples. ∎

The construction below disproves the possibility that \(q\) can depend only on \(\delta\), even for \(\delta=1/2\).

---

### 2. Dissociation rank is not submodular

Let
\[
F_0=\{1,2,3,4,9\},
\]
and put
\[
B=\{1,2,3,9\},\qquad
C=\{1,3,4,9\}.
\]

Then
\[
r_{\mathrm{dis}}(B)=3.
\]
Indeed, \(1+2=3\), so \(B\) is dependent, while \(\{1,3,9\}\) is dissociated.

Similarly,
\[
r_{\mathrm{dis}}(C)=3,
\]
because \(1+3=4\), while again \(\{1,3,9\}\) is dissociated.

Furthermore,
\[
B\cap C=\{1,3,9\},
\]
which is dissociated, so
\[
r_{\mathrm{dis}}(B\cap C)=3.
\]

Finally,
\[
B\cup C=F_0.
\]
The set \(F_0\) is dependent, while
\[
\{1,2,4,9\}
\]
is superincreasing and therefore dissociated. Hence
\[
r_{\mathrm{dis}}(B\cup C)=4.
\]

Consequently,
\[
r_{\mathrm{dis}}(B)+r_{\mathrm{dis}}(C)
=6
<
7
=
r_{\mathrm{dis}}(B\cap C)+r_{\mathrm{dis}}(B\cup C).
\]
Thus \(r_{\mathrm{dis}}\) is not submodular.

This failure occurs under a fixed proportionality hypothesis: \(F_0\) is the union of the two dissociated sets
\[
\{1,3,9\}
\quad\text{and}\quad
\{2,4\},
\]
so every \(S\subseteq F_0\) has a dissociated subset of size at least \(|S|/2\).

The additive submodularity defect can be made arbitrarily large. Take scale-separated copies \(Q_iF_0\), choosing
\[
Q_i>\sum_{j<i}\sum_{a\in Q_jF_0}a.
\]
Relations then decompose blockwise: in a highest nonzero block, a nonzero signed contribution has absolute value at least \(Q_i\), whereas all lower blocks together contribute less than \(Q_i\). Therefore dissociation rank is additive across the blocks. Taking unions of the corresponding copies of \(B\) and \(C\) produces
\[
r(B_t)+r(C_t)=6t,\qquad
r(B_t\cap C_t)+r(B_t\cup C_t)=7t.
\]
Hence no submodularity inequality with a universally bounded additive error can hold, even when the hereditary ratio is at least \(1/2\).

---

### 3. A no-carry lemma

The following elementary encoding will be used repeatedly.

#### Lemma 3.1

Let \(M,L\) be positive integers with \(L\le M-1\). If
\[
\sum_{i=0}^{m-1} c_iM^i=0,
\qquad c_i\in\mathbb Z,\quad |c_i|\le L,
\]
then every \(c_i=0\).

**Proof.**
Suppose not, and let \(r\) be the largest index with \(c_r\ne0\). Then
\[
|c_r|M^r
=
\left|\sum_{i<r}c_iM^i\right|
\le
L\sum_{i<r}M^i
=
L\frac{M^r-1}{M-1}
\le M^r-1.
\]
But \(|c_r|M^r\ge M^r\), a contradiction. ∎

Thus evaluation at a sufficiently large base preserves all bounded-coefficient vector relations exactly.

---

### 4. Large dissociated families of sign vectors

We need a family of many sign vectors that is itself dissociated.

#### Lemma 4.1

For all sufficiently large \(d\), there exist
\[
t\ge \frac1{20}d\log d
\]
vectors
\[
\sigma^{(1)},\dots,\sigma^{(t)}\in\{-1,1\}^{d+1},
\]
all having final coordinate \(1\), such that
\[
\sum_{j=1}^t\lambda_j\sigma^{(j)}=0,
\qquad \lambda_j\in\{-1,0,1\},
\]
implies that every \(\lambda_j=0\).

Here and below \(\log\) denotes the natural logarithm.

**Proof.**
Let
\[
t=\left\lfloor \frac1{10}d\log d\right\rfloor.
\]
Choose independent random vectors
\[
v^{(1)},\dots,v^{(t)}\in\{-1,1\}^d
\]
uniformly, and set
\[
\sigma^{(j)}=(v^{(j)},1).
\]

Suppose
\[
\sum_j\lambda_j\sigma^{(j)}=0.
\]
Looking at the final coordinate gives
\[
\sum_j\lambda_j=0.
\]
Thus the number of coefficients \(+1\) equals the number of coefficients \(-1\); call this number \(s\). The relation has the form
\[
\sum_{j\in P}v^{(j)}
=
\sum_{j\in N}v^{(j)}
\]
for disjoint \(P,N\) with \(|P|=|N|=s\).

For fixed \(P,N\), in one coordinate the difference is a sum of \(2s\) independent Rademacher variables. Its probability of being zero is
\[
p_s=\frac{\binom{2s}{s}}{4^s}.
\]
The coordinates are independent, so the probability of vector equality is \(p_s^d\).

The number of choices of \(P,N\) is at most
\[
\binom{t}{2s}\binom{2s}{s}
\le
\left(\frac{et}{s}\right)^{2s}.
\]
Also,
\[
p_1=\frac12,
\qquad
p_s\le s^{-1/2}\quad(s\ge2).
\]
Therefore the probability of any nonzero relation is at most
\[
t^2 2^{-d}
+
\sum_{s=2}^{\lfloor t/2\rfloor}
\left(\frac{et}{s}\right)^{2s}s^{-d/2}.
\]

We divide the sum into ranges.

For
\[
2\le s\le \frac{d}{(\log d)^2},
\]
we have, for large \(d\),
\[
2s\log\left(\frac{et}{s}\right)
\le 4s\log d
\le\frac{4d}{\log d},
\]
whereas
\[
\frac d2\log s\ge \frac d2\log2.
\]
Thus every term in this range is exponentially small in \(d\).

For
\[
\frac{d}{(\log d)^2}<s<d,
\]
we have
\[
\frac{et}{s}\le e(\log d)^3,
\]
and hence
\[
2s\log\left(\frac{et}{s}\right)
\le 8d\log\log d
\]
for large \(d\), while
\[
\frac d2\log s
\ge
\frac d2\bigl(\log d-2\log\log d\bigr).
\]
Thus these terms are at most \(\exp(-\tfrac14d\log d)\) for sufficiently large \(d\).

Finally, for \(s\ge d\), the total number of coefficient vectors is at most \(3^t\), and each corresponding relation has probability at most \(d^{-d/2}\). This range contributes at most
\[
3^t d^{-d/2}
=
\exp\left(t\log3-\frac d2\log d\right)
=o(1),
\]
because \(t\le \frac1{10}d\log d\).

The total failure probability therefore tends to zero. Hence a desired family exists. For sufficiently large \(d\),
\[
t\ge \frac1{20}d\log d.
\]
∎

---

### 5. Arithmetic sets with fixed hereditary ratio and arbitrarily bad exchange

Fix a sign-vector family from Lemma 4.1. Let
\[
m=d+1,\qquad M=t+2,
\]
and define
\[
x_i=M^i,\qquad 0\le i\le d,
\]
and
\[
X=\{x_0,\dots,x_d\}.
\]
For each \(j\), define
\[
y_j=\sum_{i=0}^d \sigma_i^{(j)}M^i,
\qquad
Y=\{y_1,\dots,y_t\}.
\]
Since every \(\sigma_d^{(j)}=1\),
\[
y_j
\ge
M^d-\sum_{i<d}M^i>0.
\]
Thus \(X\cup Y\subseteq\mathbb N\).

#### Proposition 5.1

The sets \(X\) and \(Y\) are disjoint dissociated sets.

**Proof.**

The powers \(X\) are dissociated by Lemma 3.1.

Suppose
\[
\sum_{j=1}^t\lambda_jy_j=0,
\qquad \lambda_j\in\{-1,0,1\}.
\]
Expanding in base \(M\) gives
\[
\sum_{i=0}^d
\left(\sum_{j=1}^t\lambda_j\sigma_i^{(j)}\right)M^i=0.
\]
Each coefficient has absolute value at most \(t<M-1\). Lemma 3.1 therefore gives
\[
\sum_j\lambda_j\sigma^{(j)}=0.
\]
The sign vectors are dissociated, so every \(\lambda_j=0\). Hence \(Y\) is dissociated.

Distinct sign vectors give distinct \(y_j\), again by Lemma 3.1. Likewise, if \(y_j=x_r\), then
\[
\sum_i\sigma_i^{(j)}M^i-M^r=0
\]
would, by Lemma 3.1, imply that \(\sigma^{(j)}\) is a standard basis vector. This is impossible because every coordinate of \(\sigma^{(j)}\) is nonzero and \(m\ge2\). Thus \(X\cap Y=\varnothing\). ∎

Let
\[
F=X\cup Y.
\]

#### Proposition 5.2

For every \(B\subseteq F\),
\[
r_{\mathrm{dis}}(B)\ge \frac12|B|.
\]

**Proof.**
Both \(B\cap X\) and \(B\cap Y\) are dissociated. One of them has size at least \(|B|/2\). ∎

Thus \(\rho(F)\ge1/2\), uniformly as \(d\to\infty\).

On the other hand, for each \(j\),
\[
y_j-\sum_{i=0}^d\sigma_i^{(j)}x_i=0
\]
is a nontrivial signed relation. Therefore \(X\cup\{y_j\}\) is not dissociated.

#### Proposition 5.3: Unbounded failure of approximate exchange

The set \(X\) is a maximal dissociated subset of \(F\), while \(Y\) is dissociated and
\[
\frac{|Y|}{|X|}
\ge c\log |X|
\]
for an absolute \(c>0\).

**Proof.**
The set \(X\) is dissociated. Adding any \(y_j\) creates the displayed relation, so \(X\) is maximal in \(F\).

Also,
\[
|X|=d+1,\qquad
|Y|=t\ge\frac1{20}d\log d.
\]
The asserted ratio follows. ∎

Consequently, for every fixed \(p\), there are dissociated \(X,Y\subseteq F\) with
\[
|Y|>p|X|
\]
such that
\[
X\cup\{y\}
\]
is dependent for every \(y\in Y\).

This rules out any bounded approximate exchange statement of the form
\[
|Y|>p(\delta)|X|
\Longrightarrow
\exists y\in Y\setminus X:\ X\cup\{y\}\text{ dissociated},
\]
even at \(\delta=1/2\).

It also rules out a bounded \(p\)-system property. Indeed, \(X\) is a maximal independent set of \(F\), while \(Y\) can be extended to a maximal independent set of size at least \(t\). Thus the ratio of sizes of maximal independent sets can be at least
\[
\frac{t}{d+1}\to\infty.
\]

Notice that this does not give a counterexample to the original problem:
\[
F=X\sqcup Y
\]
is already partitioned into two dissociated sets.

---

### 6. No bounded intersection-of-matroids representation

The same construction gives a stronger obstruction.

#### Proposition 6.1

For each \(j\), the set
\[
C_j=X\cup\{y_j\}
\]
is an inclusion-minimal dependent set.

**Proof.**
It is dependent by the defining relation.

Consider any relation supported in \(C_j\):
\[
\lambda y_j+\sum_{i=0}^d\nu_i x_i=0,
\qquad
\lambda,\nu_i\in\{-1,0,1\}.
\]
After base-\(M\) expansion, every coefficient has absolute value at most \(2\). Lemma 3.1 gives
\[
\lambda\sigma_i^{(j)}+\nu_i=0
\qquad(0\le i\le d).
\]
If \(\lambda=0\), then every \(\nu_i=0\). If \(\lambda\ne0\), then
\[
\nu_i=-\lambda\sigma_i^{(j)}\ne0
\]
for every \(i\). Thus every nontrivial relation uses all of \(C_j\). Hence every proper subset is dissociated. ∎

#### Proposition 6.2

If \(j\ne k\), then
\[
U_{jk}=(X\setminus\{x_d\})\cup\{y_j,y_k\}
\]
is dissociated.

**Proof.**
Suppose
\[
\lambda y_j+\mu y_k+\sum_{i=0}^{d-1}\nu_i x_i=0,
\qquad
\lambda,\mu,\nu_i\in\{-1,0,1\}.
\]
Base-\(M\) coefficients have absolute value at most \(3\), so Lemma 3.1 applies. In the top coordinate, where both sign vectors have coordinate \(1\), it gives
\[
\lambda+\mu=0.
\]

If \(\lambda=\mu=0\), all \(\nu_i=0\).

Otherwise, \(\mu=-\lambda\). Since \(\sigma^{(j)}\ne\sigma^{(k)}\) and their top coordinates agree, they differ at some coordinate \(r<d\). At this coordinate, the base coefficient is
\[
\lambda\bigl(\sigma_r^{(j)}-\sigma_r^{(k)}\bigr)+\nu_r.
\]
The first term is \(2\) or \(-2\), which cannot be cancelled by \(\nu_r\in\{-1,0,1\}\). This is a contradiction. ∎

#### Theorem 6.3

Suppose matroids \(M_1,\dots,M_q\) on \(F\) satisfy
\[
\mathcal I_{\mathrm{dis}}(F)
=
\bigcap_{\ell=1}^q\mathcal I(M_\ell).
\]
Then
\[
q\ge t\ge c\,d\log d.
\]

In particular, no bound \(q=q(\delta)\) is possible, even for \(\delta=1/2\).

**Proof.**
For every \(j\), the dependent set \(C_j\) is not in the intersection, so it is dependent in at least one matroid \(M_{\ell(j)}\).

Every proper subset of \(C_j\) is dissociated, hence is independent in every \(M_\ell\). Thus \(C_j\) is a circuit of \(M_{\ell(j)}\).

Suppose \(C_j\) and \(C_k\), with \(j\ne k\), were circuits of the same matroid \(M_\ell\). Both contain \(x_d\). By the matroid circuit-elimination axiom, there would be a circuit \(C'\) of \(M_\ell\) satisfying
\[
C'\subseteq (C_j\cup C_k)\setminus\{x_d\}
=
U_{jk}.
\]
But \(U_{jk}\) is dissociated by Proposition 6.2, hence independent in every \(M_\ell\). This is impossible.

Therefore distinct \(C_j\) must be assigned to distinct matroids, and \(q\ge t\). ∎

This directly kills the “intersection of boundedly many matroids” branch of Route 4 under the full proportionality hypothesis.

---

### 7. Ledger

#### Proved

1. A uniform inner matroid rank minorant would imply a positive solution by matroid partition.
2. A representation as the intersection of \(q(\delta)\) matroids would imply a positive solution.
3. Dissociation rank is not submodular, even when \(\rho(F)\ge1/2\).
4. The additive submodularity defect is unbounded under scale-separated products.
5. There are finite \(F\subseteq\mathbb N\) with \(\rho(F)\ge1/2\) containing dissociated \(X,Y\) with \(|Y|/|X|\to\infty\), while no element of \(Y\) augments \(X\).
6. Hence no bounded exchange factor or bounded \(p\)-system property follows from proportional dissociation.
7. For the same \(F\), any exact representation of dissociation as the intersection of matroids requires an unbounded number of matroids.
8. These examples nevertheless satisfy \(\chi_{\mathrm{dis}}(F)=2\).

#### Plausible but unproved

1. There might exist a subtler inner matroid \(M_F\) with
   \[
   r_{M_F}(B)\ge c(\delta)r_{\mathrm{dis}}(B)
   \]
   for every \(B\subseteq F\). Proving this would solve the problem, but none of the standard exchange or circuit constructions produces it.
2. A weaker polymatroidal approximation might exist, but no rounding theorem from such an approximation to dissociated color classes has been established.
3. The sign-vector/base-\(M\) framework may be useful for constructing finite high-chromatic gadgets, but the present examples are only two-colorable.

#### Dead ends

1. Treating \(r_{\mathrm{dis}}\) itself as a matroid or polymatroid rank: it is not submodular.
2. Deriving bounded approximate exchange from the hereditary ratio: quantitatively false at \(\delta=1/2\).
3. Representing dissociation as the intersection of \(q(\delta)\) matroids: quantitatively false at \(\delta=1/2\).
4. Using maximal dissociated sets as proxies for maximum ones: their size ratio can tend to zero like \(1/\log |F|\), even under \(\rho(F)\ge1/2\).

## Self-Audit

1. **The probabilistic sign-vector lemma is the least elementary part.** Its conclusion is only existential and the threshold “sufficiently large” is not optimized. I believe it is sound because every possible relation is classified by equal-size positive and negative supports, its exact probability is \(\bigl(\binom{2s}{s}/4^s\bigr)^d\), and the union bound is treated in ranges covering all \(s\).

2. **The no-carry encoding depends critically on choosing \(M\) large enough.** An overlooked carry would invalidate the arithmetic construction. Here every relation used has coordinate coefficients bounded by \(t\), \(3\), or \(2\), while \(M=t+2\); Lemma 3.1 therefore applies in every occurrence.

3. **The route obstruction does not rule out all conceivable matroid approximations.** In particular, it does not disprove the existence of one inner matroid with a uniform rank minorant. I believe the stated negative conclusions nevertheless hold because they concern precisely defined mechanisms—submodularity, bounded exchange, \(p\)-systems, and exact bounded matroid intersections—and explicit counterexamples were proved for each. No claim that the original problem is solved is being made.

## Computations To Verify

The following Python performs exact small-case checks.

```python
from itertools import combinations
from fractions import Fraction
import random

def is_dissociated(vals):
    """Exact test using subset-sum uniqueness."""
    vals = list(vals)
    sums = {0}
    for a in vals:
        shifted = {s + a for s in sums}
        if sums & shifted:
            return False
        sums |= shifted
    return True

def alpha_dis(vals):
    vals = list(vals)
    n = len(vals)
    for r in range(n, -1, -1):
        for I in combinations(range(n), r):
            if is_dissociated([vals[i] for i in I]):
                return r
    return 0

def rho(vals):
    vals = list(vals)
    n = len(vals)
    ans = Fraction(1, 1)
    for mask in range(1, 1 << n):
        B = [vals[i] for i in range(n) if (mask >> i) & 1]
        ans = min(ans, Fraction(alpha_dis(B), len(B)))
    return ans

# Submodularity counterexample.
F0 = {1, 2, 3, 4, 9}
B = {1, 2, 3, 9}
C = {1, 3, 4, 9}

assert alpha_dis(B) == 3
assert alpha_dis(C) == 3
assert alpha_dis(B & C) == 3
assert alpha_dis(B | C) == 4
assert alpha_dis(B) + alpha_dis(C) < \
       alpha_dis(B & C) + alpha_dis(B | C)

print("rho(F0) =", rho(sorted(F0)))


def explicit_sign_vectors(m):
    """
    m linearly independent sign vectors, all with top coordinate +1.
    This smaller deterministic family already verifies the
    circuit-elimination obstruction for q >= m.
    """
    sigmas = [tuple([1] * m)]
    for j in range(m - 1):
        v = [1] * m
        v[j] = -1
        sigmas.append(tuple(v))
    return sigmas

def vector_dissociated(vectors):
    """Subset-sum uniqueness for integer vectors."""
    vectors = list(vectors)
    if not vectors:
        return True
    dim = len(vectors[0])
    zero = (0,) * dim
    sums = {zero}
    for v in vectors:
        shifted = {
            tuple(s[i] + v[i] for i in range(dim))
            for s in sums
        }
        if sums & shifted:
            return False
        sums |= shifted
    return True

def integer_construction(sigmas):
    t = len(sigmas)
    m = len(sigmas[0])
    M = t + 2
    X = [M ** i for i in range(m)]
    Y = [
        sum(v[i] * M ** i for i in range(m))
        for v in sigmas
    ]
    assert min(Y) > 0
    return M, X, Y

# Verify the deterministic small construction.
m = 4
sigmas = explicit_sign_vectors(m)
assert vector_dissociated(sigmas)

M, X, Y = integer_construction(sigmas)
assert is_dissociated(X)
assert is_dissociated(Y)
assert set(X).isdisjoint(Y)

# Each C_j is a circuit: dependent, but every one-element deletion
# is dissociated. By heredity, this checks every proper subset.
for y in Y:
    Cj = X + [y]
    assert not is_dissociated(Cj)
    for z in Cj:
        D = list(Cj)
        D.remove(z)
        assert is_dissociated(D)

# Pairwise circuit-elimination obstruction after removing top x.
for y1, y2 in combinations(Y, 2):
    U = X[:-1] + [y1, y2]
    assert is_dissociated(U)

# Exact hereditary ratio is feasible only for small m.
F = X + Y
if len(F) <= 12:
    print("rho(construction) =", rho(F))
assert all(is_dissociated(part) for part in (X, Y))


def random_sign_family(d, t, attempts=10000):
    """
    Search for t dissociated vectors (v,1), v in {+-1}^d.
    Exact subset-sum checking is exponential in t.
    """
    for _ in range(attempts):
        sigmas = [
            tuple(random.choice((-1, 1)) for _ in range(d)) + (1,)
            for _ in range(t)
        ]
        if vector_dissociated(sigmas):
            return sigmas
    return None

# Example exploratory search:
# sigmas = random_sign_family(d=8, t=10)
# if sigmas:
#     M, X, Y = integer_construction(sigmas)
#     assert is_dissociated(X)
#     assert is_dissociated(Y)
#     assert all(not is_dissociated(X + [y]) for y in Y)
#     for y1, y2 in combinations(Y, 2):
#         assert is_dissociated(X[:-1] + [y1, y2])
#     print(len(X), len(Y), rho(X + Y) if len(X + Y) <= 14 else "too large")
```

A more ambitious computation should search directly for finite vector or integer sets on the Pareto frontier
\[
\bigl(\rho(F),\chi_{\mathrm{dis}}(F)\bigr),
\]
while separately measuring:

1. the ratio between largest and smallest maximal dissociated sets;
2. minimum matroid-intersection dimension, using circuit-elimination incompatibility constraints;
3. whether high-\(\chi_{\mathrm{dis}}\) examples survive exact no-carry encoding.

## Route Diagnosis

The direct matroid analogy works only formally. The hypothesis
\[
|B|\le \delta^{-1}r_{\mathrm{dis}}(B)
\]
looks exactly like the matroid arboricity inequality, but the structural ingredients behind matroid partition are absent:

- \(r_{\mathrm{dis}}\) is not submodular;
- maximal independent sets can be logarithmically smaller than maximum ones;
- exchange can fail even when the larger independent set is arbitrarily larger;
- the independence system has unbounded exact matroid-intersection dimension at fixed hereditary ratio.

The one remaining matroid possibility is a specially chosen inner matroid with a bounded rank loss. Lemma 1.1 shows that this would immediately settle the original problem, but the counterexamples eliminate the standard ways of constructing it from maximal sets, exchange chains, circuits, or bounded intersections. At present this reduces Route 4 to a new statement of comparable strength to Erdős #774, so the route is blocked.

A fresh attempt should probably move to finite high-chromatic gadgets rather than continue trying to recover matroid exchange. The no-carry sign-vector construction is potentially useful there: finite bounded-coefficient vector relations can be transferred exactly to integer relations by evaluation at a sufficiently large base, avoiding accidental carries. The missing ingredient is a family of vector gadgets with one fixed hereditary dissociation ratio and unbounded dissociation chromatic number. The constructions above deliberately fail at that point because \(F=X\sqcup Y\) is always two-colorable.