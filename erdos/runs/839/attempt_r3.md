STATUS: BLOCKED

## Result

I did not resolve P1 or P2. I proved three rigorous partial results relevant to Route 3: (i) every admissible sequence satisfies the universal bound \(\limsup H_A(x)/\log x\le 2/3\); (ii) failure of P2 forces quadratically many weighted consecutive-sum incidences, namely \(W_A(X)\gg_\eta(\log X)^2\) along a subsequence, where \(W_A\) counts representations with multiplicity; and (iii) these incidences must have harmonic-average multiplicity \(\gg_\eta\log X\), because all represented values lie outside \(A\). This identifies the exact obstruction to the multiscale packing argument. I also give arbitrarily large admissible finite—and hence extendible infinite—examples in which one integer has \(R+1\) consecutive-block representations of every length in an interval \([2R,3R]\). Thus any bounded-overlap or bounded-multiplicity lemma, even within one dyadic source scale and one length octave, is false.

## Complete Argument

### 1. Global disjointness formulation

For \(k\ge2\), define the sliding \(k\)-term sums
\[
b_{r,k}=a_r+a_{r+1}+\cdots+a_{r+k-1},
\qquad
B_k=\{b_{r,k}:r\ge1\}.
\]

Because all \(a_j\) are positive,
\[
b_{r,k}>a_{r+k-1}.
\]
Consequently, if \(b_{r,k}\in A\), it must equal some later term \(a_i\) with \(i>r+k-1\), contradicting (CSA). Hence
\[
A\cap B_k=\varnothing \qquad(k\ge2).
\tag{4}
\]

Moreover,
\[
b_{r+1,k}-b_{r,k}=a_{r+k}-a_r>0,
\]
so every \(B_k\) is itself strictly increasing. Thus its elements are distinct.

This shows that (CSA) can equivalently be read globally as saying that \(A\) is disjoint from all sums of consecutive blocks of length at least two.

---

### 2. A universal logarithmic-density bound of \(2/3\)

Let
\[
H_{B_k}(X)=\sum_{\substack{b\in B_k\\b<X}}\frac1b.
\]

If \(j\ge k\) and \(a_j<X/k\), then the \(k\)-term block ending at \(j\) satisfies
\[
b_{j-k+1,k}\le k a_j<X
\]
and therefore
\[
\frac1{b_{j-k+1,k}}\ge \frac1{k a_j}.
\]
It follows that
\[
H_{B_k}(X)
\ge
\frac1k
\sum_{\substack{j\ge k\\a_j<X/k}}\frac1{a_j}.
\tag{5}
\]

For fixed \(k\), omission of the first \(k-1\) terms contributes only \(O_k(1)\), so
\[
H_{B_k}(X)
\ge \frac1k H_A(X/k)-O_k(1).
\tag{6}
\]

Also,
\[
H_A(X)-H_A(X/k)
\le
\sum_{X/k\le n<X}\frac1n
\le \log k+O(1).
\tag{7}
\]
Hence
\[
H_{B_k}(X)\ge \frac1k H_A(X)-O_k(1).
\tag{8}
\]

By (4), \(A\) and \(B_k\) are disjoint subsets of the positive integers, so
\[
H_A(X)+H_{B_k}(X)
\le
\sum_{1\le n<X}\frac1n
=
\log X+O(1).
\]
Combining this with (8),
\[
\left(1+\frac1k\right)H_A(X)
\le \log X+O_k(1).
\]
Therefore
\[
\limsup_{X\to\infty}\frac{H_A(X)}{\log X}
\le \frac{k}{k+1}.
\tag{9}
\]

The strongest member of this family is \(k=2\), giving
\[
\boxed{
\limsup_{X\to\infty}\frac{H_A(X)}{\log X}\le\frac23.
}
\tag{10}
\]

This is far short of P2, which requires the left side to be zero.

---

### 3. Positive reciprocal density forces many dense dyadic scales

Let
\[
I_t=[2^t,2^{t+1}),\qquad
m_t=|A\cap I_t|,\qquad
d_t=\frac{m_t}{2^t},
\]
and let
\[
h_t=\sum_{a\in A\cap I_t}\frac1a.
\]

Every \(a\in I_t\) satisfies
\[
2^{-t-1}<\frac1a\le 2^{-t},
\]
so
\[
\frac{d_t}{2}\le h_t\le d_t.
\tag{11}
\]

Moreover,
\[
H_A(2^M)=\sum_{t=0}^{M-1}h_t.
\tag{12}
\]
Thus P2 is equivalent to
\[
\frac1M\sum_{t<M}h_t\longrightarrow0.
\tag{13}
\]

Suppose instead that for some \(\eta>0\) and arbitrarily large \(M\),
\[
H_A(2^M)\ge \eta M\log2.
\tag{14}
\]
Then, by \(h_t\le d_t\),
\[
\sum_{t<M}d_t\ge \eta M\log2.
\tag{15}
\]

Put \(c=\eta\log2\) and \(\theta=c/2\). Since \(0\le d_t\le1\), if
\[
D_M=\{t<M:d_t\ge\theta\},
\]
then
\[
cM
\le
\sum_{t<M}d_t
\le
|D_M|+(M-|D_M|)\theta.
\]
Therefore
\[
|D_M|
\ge
\frac{c-\theta}{1-\theta}M
\ge \frac c2 M.
\tag{16}
\]

Hence failure of P2 cannot be caused by only \(o(M)\) exceptional dense scales: along suitable dyadic cutoffs, a positive proportion of all preceding scales have density bounded below by a positive constant.

---

### 4. Local length-octave incidence

Fix a dyadic source scale \(t\). The elements of \(A\cap I_t\) form a consecutive segment of the enumeration of \(A\); write them as
\[
c_1<c_2<\cdots<c_m,
\qquad m=m_t.
\]

Let \(L=2^q\ge2\), and suppose
\[
L\le \frac m4.
\tag{17}
\]
Consider all consecutive blocks among \(c_1,\dots,c_m\) whose lengths \(\ell\) satisfy
\[
L\le\ell<2L.
\]

For each such \(\ell\), there are \(m-\ell+1\ge m/2\) blocks. Since there are \(L\) choices of \(\ell\), the number of block occurrences is at least
\[
\frac{mL}{2}.
\tag{18}
\]

Each such sum is less than
\[
2L\cdot 2^{t+1}=2^{t+q+2}.
\tag{19}
\]
Thus the total reciprocal weight of these block occurrences, counted with multiplicity, is at least
\[
\frac{mL}{2}\,2^{-(t+q+2)}
=
\frac{m}{8\cdot2^t}
=
\frac{d_t}{8}.
\tag{20}
\]

Every represented integer is outside \(A\), by admissibility. The important qualification is that (20) counts representations with multiplicity.

If additionally
\[
t+q+2\le M,
\tag{21}
\]
all these sums are below \(2^M\).

Combining (16), (20), and (21) shows the multiscale mechanism explicitly. For every dense source scale \(t\in D_M\), one obtains a contribution at least \(\theta/8\) for every integer \(q\ge1\) satisfying
\[
2^q\le m_t/4,\qquad t+q+2\le M.
\tag{22}
\]
Since \(m_t\ge\theta2^t\), the number \(Q_t\) of such \(q\)'s satisfies
\[
Q_t\ge \max\{0,\min(t,M-t)-C_\eta\}
\tag{23}
\]
for a constant \(C_\eta\).

For completeness, if \(D\subseteq\{0,\dots,M-1\}\) has cardinality \(L\), then
\[
\sum_{t\in D}\min(t+1,M-t)\ge \frac{L^2}{4}.
\tag{24}
\]
Indeed, the multiset of the \(L\) smallest possible distances from the two endpoints is bounded below termwise by
\[
1,1,2,2,3,3,\ldots,
\]
whose first \(L\) terms have sum at least \(L^2/4\).

Using (16), (23), and (24),
\[
\sum_{t\in D_M}Q_t\gg_\eta M^2.
\tag{25}
\]
Therefore the block occurrences furnished by the dyadic construction have total reciprocal weight
\[
\gg_\eta M^2.
\tag{26}
\]

The obstruction is that these \(\gg_\eta M^2\) weighted occurrences need not represent \(\gg_\eta M^2\) weighted distinct integers.

---

### 5. A global quadratic-incidence theorem

Define the representation function
\[
R_A(x)
=
\#\left\{
(r,s):1\le r<s,\ 
a_r+\cdots+a_s=x
\right\}
\]
and the weighted incidence count
\[
W_A(X)
=
\sum_{x<X}\frac{R_A(x)}x
=
\sum_{\substack{r<s\\a_r+\cdots+a_s<X}}
\frac1{a_r+\cdots+a_s}.
\tag{27}
\]

The following gives a cleaner version of (26).

#### Proposition

Let \(0<\eta\le1\). If
\[
H_A(X)\ge\eta\log X
\tag{28}
\]
for a sufficiently large \(X\), then
\[
\boxed{
W_A(X)\ge \frac{\eta^2}{32}(\log X)^2.
}
\tag{29}
\]

#### Proof

Put
\[
K=\left\lfloor X^{\eta/8}\right\rfloor.
\]
For \(2\le k\le K\), consider every \(k\)-term block ending at an index \(j\ge k\) for which \(a_j<X/k\). As in (5),
\[
W_A(X)
\ge
\sum_{k=2}^{K}\frac1k
\sum_{\substack{j\ge k\\a_j<X/k}}\frac1{a_j}.
\tag{30}
\]

Now
\[
H_A(X/k)
\ge H_A(X)-\log k-O(1),
\tag{31}
\]
while, since \(a_j\ge j\),
\[
\sum_{j<k}\frac1{a_j}
\le
\sum_{j<k}\frac1j
\le \log k+O(1).
\tag{32}
\]
Consequently,
\[
\sum_{\substack{j\ge k\\a_j<X/k}}\frac1{a_j}
\ge
H_A(X)-2\log k-O(1).
\tag{33}
\]

For \(k\le K\),
\[
2\log k\le \frac{\eta}{4}\log X.
\]
Using (28), for all sufficiently large \(X\), the right side of (33) is at least
\[
\frac{\eta}{2}\log X.
\tag{34}
\]
Also, for sufficiently large \(X\),
\[
\sum_{k=2}^{K}\frac1k
\ge \frac{\eta}{16}\log X.
\tag{35}
\]
Substituting (34) and (35) into (30) proves (29). ∎

For comparison, \(W_A(X)\) is always at most of quadratic logarithmic order, without any admissibility assumption. Indeed, strict increase gives \(a_j\ge j\). A block of length \(k\) starting at \(r\) has sum at least \(kr\). If its sum is below \(X\), then \(r<X/k\), and necessarily \(k<\sqrt{2X}\). Hence
\[
W_A(X)
\le
\sum_{2\le k<\sqrt{2X}}
\frac1k\sum_{r<X/k}\frac1r
\ll (\log X)^2.
\tag{36}
\]

Thus failure of P2 forces \(W_A(X)\) to have the largest possible logarithmic order.

---

### 6. Consequence of admissibility: average multiplicity must be logarithmic

For an admissible \(A\),
\[
R_A(x)>0\quad\Longrightarrow\quad x\notin A.
\]
Therefore
\[
W_A(X)
=
\sum_{\substack{x<X\\x\notin A}}\frac{R_A(x)}x.
\tag{37}
\]

On the other hand,
\[
\sum_{\substack{x<X\\x\notin A}}\frac1x
\le \log X+O(1).
\tag{38}
\]

Combining (29), (37), and (38), if \(H_A(X)\ge\eta\log X\), then the harmonic-measure average of \(R_A(x)\) over \(x<X\), \(x\notin A\), is at least
\[
\frac{\eta^2}{64}\log X
\tag{39}
\]
for sufficiently large \(X\). In particular, some \(x<X\) has
\[
R_A(x)\ge \frac{\eta^2}{64}\log X.
\tag{40}
\]

Thus any counterexample to P2 must create logarithmic or larger representation multiplicity on average, not merely at isolated exceptional values.

A sufficient statement for P2 would be
\[
W_A(X)=o((\log X)^2)
\tag{41}
\]
for every admissible \(A\). The proposition would immediately contradict (41) whenever \(H_A(X)\ge\eta\log X\) along an unbounded sequence. I have not proved (41).

---

### 7. Geometry of collisions

Suppose one integer \(x\) has two representations
\[
x=a_r+\cdots+a_s=a_{r'}+\cdots+a_{s'},
\qquad r<r'.
\tag{42}
\]

Necessarily \(s<s'\): if \(s\ge s'\), the second interval is properly contained in the first, contradicting positivity.

Put
\[
p=r'-r,\qquad q=s'-s.
\]
Using prefix sums, (42) gives
\[
a_r+\cdots+a_{r'-1}
=
a_{s+1}+\cdots+a_{s'}.
\tag{43}
\]
If \(p\le q\), pair the \(p\) terms on the left with the first \(p\) terms on the right. Every right-hand term has a strictly larger index than its paired left-hand term, so the right side is strictly larger. Hence
\[
p>q.
\tag{44}
\]

It follows that the second representation is shorter:
\[
(s-r+1)-(s'-r'+1)=p-q>0.
\tag{45}
\]

Under admissibility, \(q\ne1\). Indeed, if \(q=1\), then (43) reads
\[
a_r+\cdots+a_{r'-1}=a_{s+1}.
\]
If \(r'-1\ge s+1\), the left side contains \(a_{s+1}\) and at least one additional positive term, which is impossible. Otherwise all terms on the left precede \(a_{s+1}\), and the equality violates (CSA). Therefore
\[
q\ge2,\qquad p\ge3.
\tag{46}
\]

So equal-sum representations form chains that move to the right and strictly decrease in length, with the extremal allowed transition being “remove three earlier terms and add two later terms.”

Unfortunately, such chains can be arbitrarily long.

---

### 8. Arbitrarily large collision chains inside one dyadic scale

Fix \(R\ge1\). Choose a power of two \(N\) with
\[
N\ge20R.
\]
Define a finite sequence of length \(5R\).

For \(1\le i\le3R\), set
\[
a_i=N+i.
\tag{47}
\]
For \(0\le j<R\), let
\[
T_j=a_{3j+1}+a_{3j+2}+a_{3j+3}
=3N+9j+6,
\tag{48}
\]
and define
\[
a_{3R+2j+1}=\left\lfloor\frac{T_j-1}{2}\right\rfloor,
\qquad
a_{3R+2j+2}=T_j-a_{3R+2j+1}.
\tag{49}
\]

Within each pair in (49), the second value is strictly larger than the first. Since \(T_{j+1}=T_j+9\), the first value of pair \(j+1\) exceeds the second value of pair \(j\) by at least three. Also,
\[
a_{3R}<N+3R<\frac32N\le a_{3R+1},
\]
using \(N\ge20R\). Finally, the largest term is less than
\[
\frac32N+\frac92R+1<2N.
\]
Thus the whole sequence is strictly increasing and lies in
\[
[N,2N).
\tag{50}
\]

Every sum of at least two terms exceeds \(2N\), while every term is less than \(2N\). Therefore this finite sequence is admissible.

For \(0\le j\le R\), consider the interval
\[
I_j=[\,3j+1,\ 3R+2j\,].
\]
Its length is
\[
|I_j|=3R-j.
\tag{51}
\]
Passing from \(I_j\) to \(I_{j+1}\) removes the triple
\[
a_{3j+1}+a_{3j+2}+a_{3j+3}=T_j
\]
and adds the pair
\[
a_{3R+2j+1}+a_{3R+2j+2}=T_j.
\]
Hence all \(R+1\) intervals \(I_0,\dots,I_R\) have the same sum.

Their lengths are precisely
\[
3R,3R-1,\dots,2R.
\tag{52}
\]
Thus one integer has at least \(R+1\) consecutive-block representations, one at every length in a full length octave up to constant factors.

The finite prefix can be extended to an infinite admissible sequence: after the last constructed term, recursively choose
\[
a_{m+1}>a_1+\cdots+a_m.
\]
Each new term is then larger than every earlier block sum, so no new violation is introduced.

This construction rules out all of the following possible Route 3 lemmas:

- a uniform bound on \(R_A(x)\);
- a uniform bound on the number of representations with lengths in \([L,2L]\);
- a uniform bounded-overlap assertion for block sums coming from one dyadic source scale;
- any argument that simply divides weighted incidence by \(O(1)\) congestion.

---

### 9. Ledger

**Proved lemmas**

1. \(A\cap B_k=\varnothing\) for every \(k\ge2\).
2. \(\limsup H_A(X)/\log X\le2/3\).
3. Failure of P2 forces a positive proportion of dense dyadic scales.
4. Every dense source scale creates a fixed positive amount of weighted block-sum incidence in each available length octave.
5. If \(H_A(X)\ge\eta\log X\), then \(W_A(X)\ge \eta^2(\log X)^2/32\).
6. For admissible \(A\), this forces harmonic-average representation multiplicity \(\gg_\eta\log X\).
7. Equal-sum representations move rightward and become shorter; under CSA, consecutive transitions satisfy \(p\ge3\), \(q\ge2\).
8. Arbitrarily long collision chains occur even inside one dyadic source scale.

**Plausible but unproved**

- The near-extremal incidence bound
  \[
  W_A(X)=o((\log X)^2)
  \]
  for admissible sequences. This would prove P2, but it is currently unsupported.
- An inverse theorem saying that \(W_A(X)\gg(\log X)^2\) forces many length-one differences to recur as longer prefix-sum differences, contradicting CSA.
- An entropy bound showing that logarithmic multiplicity cannot occur for a positive harmonic proportion of represented values.

**Dead ends**

- Treating the sets \(B_k\) as essentially disjoint: they can overlap heavily.
- Bounded representation multiplicity, even within one source scale and one length octave: explicitly false by the construction above.
- Using only one block length per length octave: its total forbidden harmonic mass is only \(O(H_A)\), not \(H_A\log X\).
- A scale-limit or correspondence argument based only on approximate normalized sums: it loses the exact integer equality central to the problem.

## Self-Audit

1. **The quadratic incidence argument counts representations, not distinct forbidden integers.** This is the central limitation, not a hidden proof step. The count is nevertheless correct because \(W_A(X)\) was explicitly defined with multiplicity, and every selected block contributes separately.

2. **The dyadic dense-scale argument is stated along dyadic cutoffs.** This loses no information about failure of P2: if the normalized reciprocal sum is positive along arbitrary \(X\), passing to the next dyadic point changes \(\log X\) by a \(1+o(1)\) factor and only increases \(H_A\).

3. **The missing congestion or inverse theorem may itself be comparable in difficulty to P2.** I do not claim that \(W_A(X)=o((\log X)^2)\) has been established, or even that it is the optimal formulation. The explicit collision construction shows why elementary bounded-overlap proofs cannot establish it; this is the reason for the BLOCKED status.

## Computations To Verify

```python
from collections import Counter
from math import log

def is_csa(a):
    """Exact finite CSA checker."""
    assert all(a[i] < a[i+1] for i in range(len(a)-1))
    forbidden = set()
    for i, v in enumerate(a):
        if v in forbidden:
            return False
        # Add all blocks ending at i for future terms.
        total = 0
        for r in range(i, -1, -1):
            total += a[r]
            forbidden.add(total)
    return True


def representation_statistics(a, X):
    """
    R[x] counts consecutive blocks of length >=2 with sum x<X.
    It suffices that a contains every term below X.
    """
    R = Counter()
    n = len(a)
    for r in range(n):
        total = a[r]
        for s in range(r + 1, n):
            total += a[s]
            if total >= X:
                break
            R[total] += 1

    H = sum(1.0 / v for v in a if v < X)
    W = sum(mult / x for x, mult in R.items())
    hole_mass = sum(1.0 / x for x in R)
    weighted_average_multiplicity = W / hole_mass if hole_mass else 0.0
    return H, W, weighted_average_multiplicity, R


def collision_construction(R):
    """
    Produces the admissible 5R-term construction from the proof.
    N is chosen to be a power of two, so all terms lie in one
    dyadic interval [N,2N).
    """
    N = 1
    while N < 20 * R:
        N *= 2

    a = [N + i for i in range(1, 3 * R + 1)]

    for j in range(R):
        T = 3 * N + 9 * j + 6
        u = (T - 1) // 2
        v = T - u
        a.extend([u, v])

    assert len(a) == 5 * R
    assert all(a[i] < a[i+1] for i in range(len(a)-1))
    assert min(a) >= N and max(a) < 2 * N
    assert is_csa(a)

    interval_sums = []
    interval_lengths = []
    for j in range(R + 1):
        left = 3 * j                    # zero-based index of 3j+1
        right = 3 * R + 2 * j - 1      # zero-based index of 3R+2j
        interval_sums.append(sum(a[left:right + 1]))
        interval_lengths.append(right - left + 1)

    assert len(set(interval_sums)) == 1
    assert interval_lengths == list(range(3 * R, 2 * R - 1, -1))
    return N, a, interval_sums[0]


# Verify the collision construction over a substantial finite range.
for R in range(1, 1000):
    N, a, common_sum = collision_construction(R)
    _, _, _, reps = representation_statistics(a, common_sum + 1)
    assert reps[common_sum] >= R + 1


def dyadic_profile(a, M):
    """Returns m_t, d_t, h_t for t=0,...,M-1."""
    out = []
    for t in range(M):
        lo, hi = 2**t, 2**(t+1)
        vals = [v for v in a if lo <= v < hi]
        m = len(vals)
        d = m / lo
        h = sum(1.0 / v for v in vals)
        assert d / 2 <= h + 1e-15
        assert h <= d + 1e-15
        out.append((m, d, h))
    return out


def localized_collisions(a, M):
    """
    Records all localized representations used in the dyadic
    length-octave argument. provenance[x] contains
    (source_scale, q, local_start, length).
    """
    provenance = Counter()

    for t in range(M):
        lo, hi = 2**t, 2**(t+1)
        inds = [i for i, v in enumerate(a) if lo <= v < hi]
        if not inds:
            continue

        # Elements in a value interval must be consecutive in rank.
        assert inds == list(range(inds[0], inds[-1] + 1))
        vals = a[inds[0]:inds[-1] + 1]
        m = len(vals)

        q = 1
        while 2**q <= m // 4 and t + q + 2 <= M:
            L = 2**q
            for ell in range(L, 2 * L):
                total = sum(vals[:ell])
                if total < 2**M:
                    provenance[total] += 1
                for r in range(1, m - ell + 1):
                    total += vals[r + ell - 1] - vals[r - 1]
                    if total < 2**M:
                        provenance[total] += 1
            q += 1

    return provenance


def fixed_C_search(C, target_depth):
    """
    Complete backtracking search for a prefix satisfying a_i <= C*i.
    Returns one survivor of target_depth, or None.
    """
    def dfs(a, forbidden):
        m = len(a)
        if m == target_depth:
            return a[:]

        cap = int(C * (m + 1))
        first = a[-1] + 1 if a else 1

        for v in range(first, cap + 1):
            if v in forbidden:
                continue

            new_a = a + [v]
            new_forbidden = forbidden.copy()
            total = 0
            for u in reversed(new_a):
                total += u
                new_forbidden.add(total)

            ans = dfs(new_a, new_forbidden)
            if ans is not None:
                return ans
        return None

    return dfs([], set())


# Suggested experiments:
#
# 1. For C in [1.1, 1.2, ..., 10], increase target_depth until search fails.
# 2. For every survivor, set X near C*depth and record:
#       H/log(X), W/log(X)^2,
#       max_x R[x], and harmonic-average multiplicity.
# 3. Use localized_collisions to determine whether large W is caused by:
#       (a) many source scales representing the same x,
#       (b) many lengths in one octave representing the same x, or
#       (c) both.
# 4. Search specifically for prefixes maximizing W/log(X)^2 subject to CSA.
```

The decisive computational diagnostic is whether prefixes with unusually large \(H_A(X)/\log X\) also drive \(W_A(X)/(\log X)^2\) toward a positive constant and, if so, whether the resulting collision chains exhibit a reusable finite-state or substitutional pattern.

## Route Diagnosis

Route 3 successfully converts positive logarithmic density into a strong multiscale recurrence requirement: a counterexample must generate the maximal possible order \((\log X)^2\) of weighted consecutive-sum incidences while concentrating them onto only \(O(\log X)\) harmonic mass of forbidden integers. What blocks the route is congestion. Equal-sum intervals can form arbitrarily long chains even when all constituent terms lie in a single dyadic interval, and CSA only forces each chain transition to replace at least three earlier terms by at least two later terms. A fresh attempt should therefore not seek bounded multiplicity. The most promising next step is an inverse theorem for near-maximal \(W_A(X)\): prove that sustaining harmonic-average multiplicity \(\gg\log X\) across many source scales forces some adjacent prefix-sum difference \(a_i\) to recur as a longer difference. This would merge Route 3 with Route 2’s convex-difference energy viewpoint and directly exploit the one representation type that CSA forbids—length one.