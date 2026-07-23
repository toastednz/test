STATUS: BLOCKED

## Result

The ordered-growth route does not presently yield a solution. I proved a translation-uniform logarithmic sparsity theorem, characterized finite coverings by superincreasing sets up to a factor \(4\), and constructed an infinite set \(A\) which is itself dissociated but cannot be covered by finitely many superincreasing sets. I also identified the precise obstruction to gluing dissociated pieces from widely separated magnitude blocks: element-size separation is insufficient because a high block may have signed sums as small as \(1\). Thus the strongest version of Route 3—forcing boundedly many highest-term-dominating colors—is false even under the optimal proportionality constant \(\delta=1\). What remains would require control of the entire signed-sum spectrum inside each scale block, and proportional dissociation gives no evident such control.

## Complete Argument

### 1. A translation-uniform local sparsity theorem

We first strengthen the usual estimate for \(A\cap[1,N]\).

**Lemma 1.**  
Suppose \(A\subseteq\mathbb N\) satisfies
\[
\alpha_{\mathrm{dis}}(B)\ge \delta |B|
\]
for every finite \(B\subseteq A\), where \(0<\delta\le 1\). If \(I\) is any interval of \(L\ge1\) consecutive integers, then
\[
|A\cap I|
\le
\frac{8}{\delta}\log_2(2L).
\]
More generally, the same bound holds for every finite \(B\subseteq A\) contained in an interval of length \(L\).

**Proof.**  
Let \(B\subseteq A\cap I\), put \(m=|B|\), and suppose \(m>0\). Choose a dissociated set \(D\subseteq B\) with
\[
d:=|D|\ge\delta m.
\]
Write
\[
I=\{u+1,u+2,\ldots,u+L\}
\]
and let \(r=\lfloor d/2\rfloor\).

Because \(D\) is dissociated, all sums of \(r\)-element subsets of \(D\) are distinct. Every such sum lies between \(r(u+1)\) and \(r(u+L)\). Hence
\[
\binom dr\le r(L-1)+1\le dL+1\le(d+1)L.
\]
The central binomial coefficient is the largest binomial coefficient of order \(d\), so
\[
\binom d{\lfloor d/2\rfloor}\ge \frac{2^d}{d+1}.
\]
Consequently,
\[
2^d\le(d+1)^2L. \tag{1}
\]

Set \(s=\log_2(2L)\), so \(s\ge1\) and \(L=2^{s-1}\). We claim that (1) implies \(d\le8s\). Indeed, the function
\[
h(x)=\frac{2^x}{(x+1)^2}
\]
is increasing for \(x\ge2\). Moreover,
\[
\frac{2^{8s}}{(8s+1)^2L}
=
\frac{2^{7s+1}}{(8s+1)^2}>1
\]
for \(s\ge1\): it holds at \(s=1\), where the two sides are \(256\) and \(81\), and the ratio is increasing because
\[
7\log 2-\frac{16}{8s+1}>0.
\]
Thus \(d>8s\) would imply \(2^d>(d+1)^2L\), contradicting (1). Therefore
\[
\delta m\le d\le8\log_2(2L),
\]
which proves the lemma. \(\square\)

In particular, if
\[
a_1<a_2<\cdots
\]
enumerates \(A\), then any \(m\) consecutive elements satisfy
\[
a_{j+m-1}-a_j+1
\ge
2^{\delta m/8-1}. \tag{2}
\]
Thus proportional dissociation forces exponential spreading in every translated interval, not merely on average from the origin.

For a finite \(F\subseteq A\cap[1,N]\), Lemma 1 gives
\[
|F|\le \frac{8}{\delta}\log_2(2N). \tag{3}
\]
Combining this with iterative extraction gives only a nonuniform estimate. If \(0<\delta<1\), repeatedly removing a dissociated subset occupying at least a \(\delta\)-fraction leaves at most
\[
(1-\delta)^t|F|
\]
elements after \(t\) rounds. Therefore
\[
\chi_{\mathrm{dis}}(F)
\le
1+\left\lfloor
\frac{\log |F|}{-\log(1-\delta)}
\right\rfloor
=
O_\delta(\log\log N).
\]
This still depends on \(N\), so it does not solve the problem.

---

### 2. Exact relation between dyadic occupancy and superincreasing coverings

Call \(S\subseteq\mathbb N\) **superincreasing** if, for every \(x\in S\),
\[
x>\sum_{\substack{y\in S\\y<x}}y.
\]
Every superincreasing set is dissociated: in a nonzero signed relation, the largest participating element has magnitude greater than the sum of all smaller participating elements.

For \(E\subseteq\mathbb N\), define its maximal dyadic occupancy
\[
M(E)=
\sup_{j\ge0}
\left|E\cap[2^j,2^{j+1})\right|.
\]

**Lemma 2.**  
If \(E\) can be covered by \(k\) superincreasing sets, then
\[
M(E)\le2k.
\]
Conversely, if \(M(E)=M<\infty\), then \(E\) can be partitioned into at most \(2M\) superincreasing sets.

**Proof.**

For the first assertion, a superincreasing set contains at most two elements of a single dyadic interval. Indeed, if
\[
2^j\le x<y<z<2^{j+1},
\]
then
\[
x+y\ge2^{j+1}>z,
\]
contradicting the superincreasing condition at \(z\). Thus \(k\) superincreasing sets cover at most \(2k\) elements of each dyadic interval.

For the converse, list the elements in each dyadic block increasingly:
\[
E\cap[2^j,2^{j+1})
=
\{x_{j,1}<\cdots<x_{j,m_j}\},
\qquad m_j\le M.
\]
Color \(x_{j,r}\) by the pair
\[
(r,j\bmod 2).
\]
There are at most \(2M\) colors.

Fix one color. It contains at most one element from each dyadic block, and occupied block indices differ by at least \(2\). If \(x\) is its element in block \(j\), then the sum of all preceding same-colored elements is less than
\[
\sum_{t\ge1}2^{j-2t+1}
=
\frac{2^{j+1}}3
<
2^j
\le x.
\]
Hence every color class is superincreasing. \(\square\)

Thus, up to constant factors, finite superincreasing colorability is exactly bounded dyadic occupancy.

Lemma 1 only gives
\[
\left|A\cap[2^j,2^{j+1})\right|
=
O_\delta(j),
\]
rather than a uniform bound. The next construction shows that this cannot be improved, even when \(A\) is itself dissociated.

---

### 3. Dissociated clusters that require arbitrarily many superincreasing colors

For \(d\ge1\), define
\[
D_d=\{2^d+2^r:0\le r<d\}.
\]

**Lemma 3.**  
The set \(D_d\) is dissociated.

**Proof.**  
Suppose
\[
\sum_{r=0}^{d-1}\varepsilon_r(2^d+2^r)=0,
\qquad \varepsilon_r\in\{-1,0,1\}.
\]
Put
\[
t=\sum_{r=0}^{d-1}\varepsilon_r,
\qquad
R=\sum_{r=0}^{d-1}\varepsilon_r2^r.
\]
Then
\[
2^dt+R=0,
\]
while
\[
|R|\le\sum_{r=0}^{d-1}2^r=2^d-1.
\]
Therefore \(t=0\) and \(R=0\). But the powers
\[
1,2,\ldots,2^{d-1}
\]
are dissociated: in a nonzero signed sum, the largest participating power exceeds the sum of all smaller powers. Hence every \(\varepsilon_r=0\). \(\square\)

All \(d\) elements of \(D_d\) lie in the single dyadic interval
\[
[2^d,2^{d+1}).
\]
Lemma 2 therefore shows that at least \(\lceil d/2\rceil\) superincreasing sets are needed to cover \(D_d\). Conversely, partitioning \(D_d\) into pairs and possibly one singleton gives a superincreasing partition, since every one- or two-element subset of positive distinct integers is superincreasing. Consequently,
\[
\chi_{\mathrm{superinc}}(D_d)=\left\lceil\frac d2\right\rceil,
\]
whereas
\[
\rho(D_d)=1,
\qquad
\chi_{\mathrm{dis}}(D_d)=1.
\]

There is therefore no bound on the number of superincreasing colors in terms of the hereditary dissociation ratio—not even when that ratio is \(1\).

This can be upgraded to one infinite example.

**Proposition 4.**  
There exists an infinite dissociated set \(A\subseteq\mathbb N\) which cannot be covered by finitely many superincreasing sets.

**Proof.**  
Choose powers of two \(Q_d=2^{q_d}\) recursively. Having chosen \(Q_1,\ldots,Q_{d-1}\), let
\[
S_{d-1}
=
\sum_{i<d}\sum_{x\in Q_iD_i}x.
\]
Choose \(Q_d\) so large that
\[
Q_d>S_{d-1}
\]
and so that the dyadic intervals containing the blocks \(Q_dD_d\) are distinct. This is possible because arbitrarily large powers of two are available. Set
\[
A=\bigcup_{d\ge1}Q_dD_d.
\]

Consider a nonzero finite signed relation in \(A\), and let \(d\) be the largest block index on which a coefficient is nonzero. The contribution from that block is
\[
Q_d\sum_{x\in D_d}\varepsilon_xx.
\]
Since \(D_d\) is dissociated, the inner sum is a nonzero integer, so the absolute value of this contribution is at least \(Q_d\). The total absolute contribution of all lower blocks is at most \(S_{d-1}<Q_d\), a contradiction. Thus \(A\) is dissociated.

Because \(Q_d\) is a power of two, all elements of \(Q_dD_d\) lie in one dyadic interval:
\[
Q_dD_d
\subseteq
[2^{q_d+d},2^{q_d+d+1}).
\]
That interval contains \(d\) elements of \(A\). A superincreasing set contains at most two of them. Hence a union of \(k\) superincreasing sets contains at most \(2k\) of them, which is impossible when \(d>2k\).

Thus \(A\) is dissociated, and in particular proportionately dissociated with \(\delta=1\), but has no finite superincreasing cover. \(\square\)

This is not a counterexample to the original problem: \(A\) itself is one dissociated color. It disproves the intended strengthening of the ordered-growth route.

The same construction also excludes any fixed lacunarity requirement. For every fixed \(q>1\), a \(q\)-lacunary set has only \(O_q(1)\) elements in an interval \([N,\tfrac32N]\), whereas \(D_d\) has \(d\) such elements.

---

### 4. Why widely separated dissociated blocks do not automatically glue

For a finite dissociated set \(E\), define its signed gap by
\[
\gamma(E)
=
\min_{\varepsilon\in\{-1,0,1\}^E\setminus\{0\}}
\left|
\sum_{x\in E}\varepsilon_xx
\right|.
\]
Since \(E\) is dissociated and integral, \(\gamma(E)\) is a positive integer.

**Lemma 5.**  
Let \(E_1,E_2,\ldots\) be finite dissociated sets. If
\[
\gamma(E_j)>
\sum_{i<j}\sum_{x\in E_i}x
\qquad\text{for every }j,
\tag{4}
\]
then \(\bigcup_jE_j\) is dissociated.

**Proof.**  
In a nonzero finite signed relation, choose the largest block index \(j\) carrying a nonzero coefficient. Its block contribution has absolute value at least \(\gamma(E_j)\). The absolute value of the contribution of all lower blocks is at most the right side of (4), so cancellation is impossible. \(\square\)

For a dilation,
\[
\gamma(QE)=Q\gamma(E)\ge Q.
\]
This is exactly why scale-separated dilated gadgets glue successfully.

In contrast, merely placing a block high in the ordering does not control its signed gap. For every \(M\ge2\), the blocks
\[
E_1=\{1\},
\qquad
E_2=\{M,M+1\}
\]
are individually dissociated and satisfy
\[
\min E_2=M>\sum_{x\in E_1}x=1.
\]
Nevertheless,
\[
1+M=M+1,
\]
so their union is not dissociated. Here
\[
\gamma(E_2)=1
\]
regardless of how large \(M\) is.

Thus the following seemingly natural block lemma is false:

> “If every scale block is dissociated and each new block lies far beyond the preceding blocks in magnitude, then their union is dissociated.”

The missing quantity is the least nonzero signed sum inside the high block, not the size of its elements. Balanced cancellation among comparable large elements can produce arbitrarily small residues.

The sets \(D_d\) exhibit the same phenomenon at maximal strength:
\[
\rho(D_d)=1
\quad\text{but}\quad
\gamma(D_d)=1,
\]
because
\[
(2^d+2)-(2^d+1)=1.
\]
Consequently, proportional dissociation cannot by itself give a useful lower bound on signed gaps.

---

### 5. Pure metric sparsity cannot encode the missing arithmetic information

Dilation preserves the complete signed-relation hypergraph.

**Lemma 6.**  
For every finite \(F\subseteq\mathbb N\) and integer \(Q\ge1\),
\[
\rho(QF)=\rho(F),
\qquad
\chi_{\mathrm{dis}}(QF)=\chi_{\mathrm{dis}}(F).
\]

**Proof.**  
For every coefficient vector \(\varepsilon\),
\[
\sum_{f\in F}\varepsilon_f(Qf)
=
Q\sum_{f\in F}\varepsilon_ff.
\]
Thus a subset of \(QF\) is dissociated exactly when the corresponding subset of \(F\) is dissociated. All independence and coloring parameters are therefore unchanged. \(\square\)

On the other hand, dilation can make an arbitrary finite integer set look extremely sparse in every translated interval. If \(|F|=n\) and \(Q\ge2^n\), then every interval \(I\) of length \(L\) satisfies
\[
|QF\cap I|\le\log_2(2L).
\]
Indeed, an interval containing two points of \(QF\) has length at least \(Q+1\), and hence
\[
\log_2(2L)\ge\log_2Q\ge n;
\]
an interval containing at most one point satisfies the estimate trivially.

Therefore no argument based only on local occupancy, diameter, absolute gaps, or comparable order statistics can distinguish a hard finite relation system from a sparse dilation of it. A successful ordered proof must retain exact arithmetic information about signed sums.

## Self-Audit

1. **The local sparsity constant \(8/\delta\) is crude.**  
   It relies on a deliberately loose estimate for the central binomial coefficient and an elementary monotonicity calculation. The constant is not claimed to be optimal, but every inequality needed for the stated bound is explicit.

2. **The infinite example only refutes superincreasing or fixed-lacunarity decompositions, not all possible ordered-growth arguments.**  
   This is the principal limitation. The example is itself dissociated, so it cannot disprove the Erdős statement. It nevertheless rigorously shows that replacing dissociation by highest-element domination loses an unbounded factor even at \(\delta=1\).

3. **The conclusion that Route 3 is blocked is a diagnosis, not an impossibility theorem for every order-based proof.**  
   A more sophisticated affine or digital decomposition might exploit balanced signed sums recursively. I regard the current route as blocked because the required new lemma would need to control signed-sum spectra or congruences inside arbitrary dense scale clusters, and neither the local sparsity theorem nor proportional extraction supplies such control.

## Computations To Verify

```python
from itertools import combinations, product
from fractions import Fraction
from collections import defaultdict
import math

def is_dissociated(xs):
    """Exact subset-sum test."""
    sums = {0}
    for x in xs:
        shifted = {s + x for s in sums}
        if sums & shifted:
            return False
        sums |= shifted
    return True

def signed_gap(xs):
    """Returns 0 if dependent; otherwise the least nonzero signed sum."""
    best = None
    for eps in product((-1, 0, 1), repeat=len(xs)):
        if all(e == 0 for e in eps):
            continue
        value = sum(e*x for e, x in zip(eps, xs))
        if value == 0:
            return 0
        best = abs(value) if best is None else min(best, abs(value))
    return best

def alpha_dis(xs):
    xs = list(xs)
    for r in range(len(xs), -1, -1):
        for sub in combinations(xs, r):
            if is_dissociated(sub):
                return r

def rho(xs):
    xs = list(xs)
    ans = Fraction(1, 1)
    for r in range(1, len(xs) + 1):
        for B in combinations(xs, r):
            ans = min(ans, Fraction(alpha_dis(B), r))
    return ans

def is_superincreasing(xs):
    total = 0
    for x in sorted(xs):
        if x <= total:
            return False
        total += x
    return True

def k_colorable(xs, k, predicate):
    """Exact backtracking for small sets."""
    order = sorted(xs, reverse=True)
    classes = [[] for _ in range(k)]

    def rec(i):
        if i == len(order):
            return True
        x = order[i]
        seen_states = set()
        for c in range(k):
            state = tuple(sorted(classes[c]))
            if state in seen_states:
                continue
            seen_states.add(state)

            candidate = classes[c] + [x]
            if predicate(candidate):
                classes[c].append(x)
                if rec(i + 1):
                    return True
                classes[c].pop()

            if not classes[c]:
                break  # Empty colors are symmetric.
        return False

    return rec(0)

def chromatic_number(xs, predicate):
    for k in range(1, len(xs) + 1):
        if k_colorable(xs, k, predicate):
            return k
    raise AssertionError

def D(d):
    return [2**d + 2**r for r in range(d)]

# Verify the finite cluster claims.
for d in range(1, 9):
    F = D(d)
    assert is_dissociated(F)
    assert rho(F) == 1
    assert signed_gap(F) == 1 if d >= 2 else signed_gap(F) > 0
    sigma = chromatic_number(F, is_superincreasing)
    assert sigma == (d + 1) // 2

# Verify failure of naive block gluing.
for M in [10, 100, 10**6]:
    assert is_dissociated([1])
    assert is_dissociated([M, M + 1])
    assert not is_dissociated([1, M, M + 1])
    assert signed_gap([M, M + 1]) == 1

def make_scale_separated_blocks(t):
    blocks = []
    total_lower = 0
    last_dyadic_index = -1

    for d in range(1, t + 1):
        Q = 1
        while (Q <= total_lower or
               (Q.bit_length() - 1) + d <= last_dyadic_index):
            Q *= 2

        block = [Q*x for x in D(d)]
        j = (Q.bit_length() - 1) + d
        assert all(2**j <= x < 2**(j + 1) for x in block)

        blocks.append(block)
        total_lower += sum(block)
        last_dyadic_index = j

    return blocks

# Finite-prefix sanity checks for Proposition 4.
blocks = make_scale_separated_blocks(5)
prefix = []
for block in blocks:
    prefix.extend(block)
    assert is_dissociated(prefix)

def dyadic_superincreasing_coloring(xs):
    blocks = defaultdict(list)
    for x in xs:
        j = x.bit_length() - 1
        blocks[j].append(x)

    colors = defaultdict(list)
    for j, vals in blocks.items():
        for rank, x in enumerate(sorted(vals)):
            colors[(rank, j % 2)].append(x)

    assert all(is_superincreasing(C) for C in colors.values())
    return colors

# Verify Lemma 2's constructive coloring on sample sets.
for F in [
    list(range(1, 30, 3)),
    D(8),
    [1, 4, 6, 20, 22, 80, 200]
]:
    colors = dyadic_superincreasing_coloring(F)
    M = max(
        sum(2**j <= x < 2**(j + 1) for x in F)
        for j in range(max(F).bit_length())
    )
    assert len(colors) <= 2*M

def verify_local_bound(F, delta):
    """
    It suffices to check intervals whose endpoints are elements of F:
    enlarging an interval only increases the right-hand side.
    """
    F = sorted(F)
    for i in range(len(F)):
        for j in range(i, len(F)):
            m = j - i + 1
            L = F[j] - F[i] + 1
            assert m <= (8/delta) * math.log2(2*L) + 1e-12

for d in range(1, 12):
    verify_local_bound(D(d), 1.0)
```

A more exploratory computation should track, for candidate ordered block decompositions, both dissociation and the signed gap
\[
\gamma(E)=\min_{\varepsilon\ne0}\left|\sum\varepsilon_xx\right|.
\]
The decisive question for this route is whether uniformly positive hereditary dissociation ratio ever forces a bounded coloring whose blockwise signed gaps dominate all lower-scale contributions. The examples above suggest searching directly for finite \(F\) with large \(\rho(F)\) but very small signed gaps in every large dissociated subset.

## Route Diagnosis

**Proved ledger.**

1. Proportional dissociation implies the translation-uniform interval bound
   \[
   |A\cap I|\le \frac8\delta\log_2(2|I|).
   \]
2. Finite superincreasing cover number is within constant factors of maximal dyadic occupancy.
3. The sets
   \[
   D_d=\{2^d+2^r:0\le r<d\}
   \]
   have \(\rho(D_d)=1\) and dissociation chromatic number \(1\), but require exactly \(\lceil d/2\rceil\) superincreasing colors.
4. There is one infinite dissociated set with unbounded dyadic occupancy and no finite superincreasing cover.
5. Block gluing is controlled by the least nonzero signed sum, not by the magnitude of block elements.
6. Dilation preserves the complete dissociation hypergraph while making absolute metric sparsity arbitrarily strong.

**Dead ends.**

- Bounded decomposition into superincreasing or fixed-lacunary sequences is false even for dissociated sets.
- Coloring each scale block dissociatively and then reusing colors across distant blocks is invalid: \(\{1\}\) and \(\{M,M+1\}\) are the minimal counterexample.
- Local logarithmic sparsity alone has no coloring content because it can be manufactured by dilation without changing any signed relation.

**Plausible but unproved.**

A recursive affine or digital decomposition might separate unbalanced relations, whose large common offset dominates, from balanced relations, which descend to relations among local offsets. However, no bounded-depth or bounded-color consequence of proportional dissociation is known here. Establishing one would amount to a new structural theorem controlling signed-sum spectra, rather than a consequence of ordered growth alone.

**Final diagnosis.**

Route 3 succeeds only under stronger assumptions such as uniformly bounded dyadic occupancy or explicit divisibility-separated blocks. Under the actual hypothesis, dense dissociated clusters and arbitrarily small internal signed residues defeat both mechanisms. A fresh attempt should either:

- develop a genuinely arithmetic multiscale invariant controlling balanced signed sums and congruence residues; or
- leave Route 3 and pursue finite high-chromatic gadgets, where the central task is to preserve a common hereditary dissociation ratio while controlling unintended long relations.

At present the route is blocked precisely at converting qualitative nonvanishing of signed sums into quantitative or compatible multiscale separation.