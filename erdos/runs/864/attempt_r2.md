STATUS: BLOCKED

## Result

I did not resolve the conjectured \(2/\sqrt3\) constant. I proved the uniform improvement
\[
F(N)\le \sqrt{2N}+O(N^{1/4}),
\]
derived an exact description and count of all doubled differences, and obtained the precise Erdős–Turán sliding-window inequality governing them. For fully reflected sets, the problem reduces to packing the distinct labels
\[
x_j-x_i\quad(i<j),\qquad x_i+x_j\quad(i\le j),
\]
which must all be distinct. The desired bound would follow from a sharp diameter theorem for these “signed Sidon” configurations, but the standard weighted-difference method does not prove it: on the Erdős–Freud construction the doubled small differences asymptotically saturate the available triangular weight. Thus the naive Route 2 estimate is definitively blocked, while more sophisticated position-sensitive or arithmetic use of the doubled differences remains possible.

## Complete Argument

### 1. A self-contained Sidon interval estimate

Call \(B\subseteq[M]\) genuine Sidon. For \(d>0\), put
\[
m_B(d)=|\{x:x,x+d\in B\}|.
\]
Then
\[
m_B(d)\le 1.
\]
Indeed, if both \(x,x+d\) and \(y,y+d\) are distinct occurrences, then
\[
x+(y+d)=(x+d)+y.
\]
The two unordered pairs are distinct, contradicting the Sidon property.

Let \(b=|B|\), fix an integer \(L\ge1\), and for
\[
u=1-L,\ldots,M-1
\]
write
\[
B_u=|B\cap[u+1,u+L]|.
\]
Each element of \(B\) belongs to exactly \(L\) of these windows, hence
\[
\sum_u B_u=Lb.
\]
A pair at distance \(d<L\) belongs to exactly \(L-d\) windows, so
\[
\sum_u\binom{B_u}{2}
 =\sum_{d=1}^{L-1}(L-d)m_B(d)
 \le \sum_{d=1}^{L-1}(L-d)
 =\frac{L(L-1)}2.
\]
There are \(M+L-1\) windows. Cauchy–Schwarz gives
\[
\sum_u\binom{B_u}{2}
=\frac12\left(\sum_uB_u^2-Lb\right)
\ge
\frac{L^2b^2}{2(M+L-1)}-\frac{Lb}{2}.
\]
Consequently
\[
\frac{L^2b^2}{M+L-1}-Lb\le L(L-1),
\]
or
\[
b^2\le \frac{(M+L-1)(L+b-1)}L. \tag{1}
\]

The distinct positive differences also give
\[
\binom b2\le M-1,
\]
so \(b=O(\sqrt M)\). Taking \(L=\lceil M^{3/4}\rceil\) in (1) now yields
\[
b^2\le M+O(M^{3/4}),
\]
and therefore
\[
|B|\le \sqrt M+O(M^{1/4}). \tag{2}
\]

The same estimate holds for a Sidon set contained in any interval of \(M\) consecutive integers, by translation.

---

### 2. A uniform \(\sqrt2\) upper bound for the original problem

Let \(A\subseteq[N]\) be admissible.

If no sum is repeated, then \(A\) is genuine Sidon and (2) gives
\[
|A|\le \sqrt N+O(N^{1/4}).
\]

Otherwise, let \(s\) be the unique repeated sum, and put
\[
p=\left\lfloor\frac s2\right\rfloor.
\]
Define
\[
A_-:=A\cap[1,p],\qquad A_+:=A\cap[p+1,N].
\]

Both \(A_-\) and \(A_+\) are genuine Sidon sets.

For \(A_+\), every pair sum is strictly greater than \(s\), so any collision would give a second repeated sum.

For \(A_-\), every pair sum is at most \(2p\le s\). A collision can therefore only occur at \(s\). If \(s\) is odd, no pair from \(A_-\) has sum \(s\). If \(s=2p\), the only pair from \(A_-\) with sum \(s\) is the diagonal pair \((p,p)\). Thus \(A_-\) also has no repeated sum.

Applying (2) in intervals of lengths \(p\) and \(N-p\),
\[
|A|
\le \sqrt p+\sqrt{N-p}+O(N^{1/4}).
\]
By Cauchy–Schwarz,
\[
\sqrt p+\sqrt{N-p}\le\sqrt{2N}.
\]
Hence uniformly over all admissible \(A\),
\[
\boxed{|A|\le\sqrt{2N}+O(N^{1/4}).} \tag{3}
\]

This improves the elementary constant \(2\), but does not reach \(2/\sqrt3\).

---

### 3. Exact structure of doubled differences

Continue to assume that \(s\) is the exceptional sum. Let
\[
C=A\cap(s-A)
\]
be the exceptional core, and put
\[
\delta=
\begin{cases}
1,&s\text{ even and }s/2\in A,\\
0,&\text{otherwise}.
\end{cases}
\]
If \(t=r_A(s)\), then
\[
|C|=2t-\delta.
\]

Let
\[
D:=\{d\ge1:m_A(d)=2\}.
\]

#### Lemma 1: Reflection characterization

If \(m_A(d)=2\), the two occurrences of \(d\) are reflections of one another about \(s/2\).

**Proof.**
Write the two occurrences as
\[
\{x,x+d\},\qquad \{y,y+d\},\qquad x\ne y.
\]
Then
\[
(x+d)+y=x+(y+d).
\]
The two unordered representations are distinct, so their common sum must be \(s\). Thus
\[
x+y+d=s,
\]
and hence
\[
y=s-x-d,\qquad y+d=s-x.
\]
Therefore
\[
\{y,y+d\}=\{s-(x+d),s-x\}.
\]
All four endpoints belong to \(C\). ∎

Conversely, if \(\{a,b\}\subset C\) is not fixed by reflection, its reflected pair is a second occurrence of the same positive difference. If \(a+b=s\), the pair is fixed and its difference occurs only once: a second occurrence would, by the preceding proof, have the same lower endpoint.

Thus reflection acts on the unordered distinct pairs from \(C\). Its fixed pairs are exactly the \(t-\delta\) non-diagonal representations of \(s\). Every other orbit has size two and gives one doubled difference. Different orbits cannot give the same difference, since that would make its multiplicity at least four. Therefore
\[
\boxed{
|D|
=\frac{\binom{2t-\delta}{2}-(t-\delta)}2.
} \tag{4}
\]
Explicitly,
\[
|D|=
\begin{cases}
t(t-1),&\delta=0,\\
(t-1)^2,&\delta=1.
\end{cases} \tag{5}
\]

In particular, every difference involving an unpaired element of \(A\setminus C\) occurs only once.

---

### 4. The exact sliding-window inequality

For any admissible \(A\), let \(k=|A|\). For \(L\ge1\) and
\[
u=1-L,\ldots,N-1,
\]
put
\[
A_u=|A\cap[u+1,u+L]|.
\]
Exactly as above,
\[
\sum_u A_u=Lk
\]
and
\[
\sum_u\binom{A_u}{2}
=\sum_{d=1}^{L-1}(L-d)m_A(d). \tag{6}
\]

By the doubled-difference characterization,
\[
m_A(d)\le 1+\mathbf 1_D(d).
\]
Define
\[
W_D(L):=\sum_{\substack{d\in D\\d<L}}(L-d).
\]
Then (6) gives
\[
\sum_u\binom{A_u}{2}
\le \frac{L(L-1)}2+W_D(L). \tag{7}
\]
On the other hand, Cauchy–Schwarz over the \(N+L-1\) windows gives
\[
\sum_u\binom{A_u}{2}
\ge
\frac{L^2k^2}{2(N+L-1)}-\frac{Lk}{2}. \tag{8}
\]
Combining (7) and (8),
\[
\boxed{
\frac{L^2k^2}{2(N+L-1)}-\frac{Lk}{2}
\le
\frac{L(L-1)}2+W_D(L).
} \tag{9}
\]

This is the precise global Route 2 inequality.

If one took \(L=o(N)\) with \(L\gg k\), then obtaining the conjectured bound directly from (9) would require approximately
\[
W_D(L)\le \left(\frac16+o(1)\right)L^2. \tag{10}
\]
The next subsection shows that (10) is false even on the conjecturally extremal construction.

---

### 5. Why the naive doubled-difference estimate fails sharply

Let \(N=3M\), let \(B\subseteq[M]\) be Sidon with
\[
|B|=(1+o(1))\sqrt M,
\]
and take
\[
A=B\cup(N-B).
\]
Every positive difference occurring inside \(B\) occurs a second time inside \(N-B\), so it belongs to \(D\).

Let \(L=M^{3/4}\). Applying the lower half of the sliding-window argument to \(B\),
\[
\sum_{d<L}(L-d)m_B(d)
\ge
\frac{L^2|B|^2}{2(M+L-1)}-\frac{L|B|}{2}
=\left(\frac12-o(1)\right)L^2.
\]
Therefore
\[
W_D(L)\ge \left(\frac12-o(1)\right)L^2.
\]
Since \(D\) consists of distinct positive integers,
\[
W_D(L)\le \sum_{d=1}^{L-1}(L-d)
=\left(\frac12+o(1)\right)L^2.
\]
Thus
\[
\boxed{
W_D(L)=\left(\frac12+o(1)\right)L^2
}
\tag{11}
\]
on the Erdős–Freud construction.

Consequently, no proof based on inserting a universal upper bound for \(W_D(L)\) into the global Cauchy estimate (9) can reach the desired constant. Any successful sliding-window argument must exploit the spatial distribution of \(A_u\), not merely the total triangular weight of the doubled differences.

---

### 6. Fully reflected sets and the signed-Sidon reduction

Suppose, for simplicity, that there is no central element and the entire set is paired:
\[
A=C.
\]
Write the complementary pairs as
\[
\left\{\frac s2-x_i,\frac s2+x_i\right\},
\qquad
0<x_1<\cdots<x_q.
\]
All \(x_i\) lie in the same integer or half-integer lattice.

The nonzero offsets from the exceptional sum \(s\) are exactly
\[
x_j-x_i\quad(i<j)
\]
from cross pairs, and
\[
x_i+x_j\quad(i\le j)
\]
from same-side pairs. Therefore admissibility is equivalent to the \(q^2\) positive integers
\[
\mathcal O(X):=
\{x_j-x_i:i<j\}
\cup
\{x_i+x_j:i\le j\} \tag{12}
\]
being pairwise distinct.

In particular:

* \(X=\{x_1,\ldots,x_q\}\) is Sidon;
* its positive differences are disjoint from all its unordered sums;
* the doubled differences are
  \[
  \{x_j-x_i:i<j\}\cup\{x_i+x_j:i<j\}.
  \]

Since \(A\subseteq[N]\),
\[
2x_q\le N-1. \tag{13}
\]
Thus the conjectured bound for fully reflected sets would follow from
\[
x_q\ge\left(\frac32-o(1)\right)q^2. \tag{14}
\]
Indeed, (13) and (14) would give
\[
N\ge (3-o(1))q^2,
\]
and since \(|A|=2q\),
\[
|A|\le\left(\frac2{\sqrt3}+o(1)\right)\sqrt N.
\]

However, (14) is itself an unproved sharp signed-Sidon diameter statement. It is already a substantial special case of the original problem, and it does not address unpaired elements.

---

### 7. What the weighted method does prove for the signed core

Let
\[
w=x_q-x_1.
\]
For an integer \(L\ge1\), define
\[
D_L=\sum_{i<j}(L-(x_j-x_i))_+
\]
and
\[
S_L=\sum_{i\le j}(L-(x_i+x_j))_+.
\]
Since all labels in (12) are distinct,
\[
D_L+S_L\le\sum_{n=1}^{L-1}(L-n)=\frac{L(L-1)}2. \tag{15}
\]

Translating \(X\) by \(-x_1\) and applying the sliding-window Cauchy estimate in an interval of span \(w\) gives
\[
D_L\ge
\frac{L^2q^2}{2(w+L)}-\frac{Lq}{2}. \tag{16}
\]
Consequently,
\[
\boxed{
S_L\le
\frac{L(L-1)}2
-\frac{L^2q^2}{2(w+L)}
+\frac{Lq}{2}.
} \tag{17}
\]

For example, if
\[
Q(y)=|\{i:x_i\le y\}|,
\]
then every unordered pair from \(X\cap[0,L/4]\) has sum at most \(L/2\), and so contributes at least \(L/2\) to \(S_L\). Combining this with (17) gives
\[
\boxed{
Q(L/4)\bigl(Q(L/4)+1\bigr)
\le
2(L-1)-\frac{2Lq^2}{w+L}+2q.
} \tag{18}
\]
This rigorously shows that when \(w\) is close to the minimal Sidon width, the signed-Sidon condition restricts how many elements may lie close to the center. It does not, however, force the central gap \(x_1\) to be of order \(q^2/2\).

Taking only \(D_L\le L(L-1)/2\) in (16) gives
\[
w\ge \frac{Lq^2}{L+q-1}-L.
\]
Choosing \(L=\lceil q^{3/2}\rceil\) yields
\[
\boxed{
w\ge q^2-O(q^{3/2}).
} \tag{19}
\]
Thus the desired (14) would follow if one could prove
\[
x_1\ge \frac12w-o(q^2). \tag{20}
\]
But (20) is not a consequence of mere disjointness by interval separation: sums and differences can interlace. For example,
\[
X=\{1,4,10\}
\]
has
\[
\{x_j-x_i\}=\{3,6,9\}
\]
and
\[
\{x_i+x_j:i\le j\}=\{2,5,8,11,14,20\},
\]
which are disjoint but highly interlaced.

A rigorous special case is available: if
\[
2x_1>x_q-x_1,
\]
so that all sums are larger than all differences, then (19) gives
\[
x_q=x_1+w>\frac32w
\ge \frac32q^2-O(q^{3/2}).
\]
Hence fully reflected, range-separated sets satisfy the conjectured asymptotic bound. This covers the geometry of the Erdős–Freud construction but not arbitrary admissible sets.

## Self-Audit

1. **The \(\sqrt2\) bound is far from the requested constant.**  
   It is nevertheless rigorous: both halves relative to \(s/2\) are genuine Sidon sets, including the even-\(s\) diagonal case, and the needed Sidon estimate was rederived from the sliding-window identity.

2. **The reflection-orbit count has delicate diagonal and central-element cases.**  
   I believe it is correct because fixed two-element orbits are exactly the \(t-\delta\) non-diagonal representations of \(s\), while pairs involving the center form nonfixed two-element orbits. This gives \(t(t-1)\) doubled differences without a center and \((t-1)^2\) with one.

3. **The Route 2 blockage is not a theorem that every possible weighted argument must fail.**  
   What is proved is narrower: the global Cauchy inequality plus any universal small upper bound on \(W_D(L)\) cannot be sharp, because the Erdős–Freud construction has \(W_D(L)\sim L^2/2\). A position-sensitive, multi-window, or arithmetic correlation argument could still succeed.

## Computations To Verify

```python
from collections import Counter
from itertools import combinations
from math import comb
from fractions import Fraction

def pair_sum_counts(A):
    A = sorted(A)
    c = Counter()
    for i, a in enumerate(A):
        for b in A[i:]:
            c[a + b] += 1
    return c

def difference_data(A):
    A = sorted(A)
    occ = {}
    for i, a in enumerate(A):
        for b in A[i+1:]:
            d = b - a
            occ.setdefault(d, []).append((a, b))
    return occ

def is_admissible(A):
    c = pair_sum_counts(A)
    repeated = [s for s, v in c.items() if v >= 2]
    return len(repeated) <= 1

def is_genuine_sidon(A):
    return max(pair_sum_counts(A).values(), default=0) <= 1

def verify_core_and_differences(A):
    csum = pair_sum_counts(A)
    repeated = [s for s, v in csum.items() if v >= 2]
    assert len(repeated) <= 1
    if not repeated:
        return

    s = repeated[0]
    t = csum[s]
    Aset = set(A)
    C = {a for a in A if s - a in A}
    delta = int(s % 2 == 0 and s // 2 in Aset)

    assert len(C) == 2 * t - delta

    occ = difference_data(A)
    assert max(map(len, occ.values()), default=0) <= 2
    D = {d for d, pairs in occ.items() if len(pairs) == 2}

    expected = (comb(len(C), 2) - (t - delta)) // 2
    assert len(D) == expected

    for d in D:
        (x, xd), (y, yd) = occ[d]
        assert xd == x + d and yd == y + d
        reflected = {s - xd, s - x}
        assert reflected == {y, yd}
        assert {x, xd, y, yd} <= C

def verify_sliding_identity(A, N):
    occ = difference_data(A)
    m = Counter({d: len(v) for d, v in occ.items()})
    for L in range(1, N + 3):
        lhs = 0
        for u in range(1 - L, N):
            au = sum(u < a <= u + L for a in A)
            lhs += comb(au, 2)
        rhs = sum((L - d) * m[d] for d in range(1, L))
        assert lhs == rhs

def verify_half_partition(A, N):
    csum = pair_sum_counts(A)
    repeated = [s for s, v in csum.items() if v >= 2]
    assert len(repeated) <= 1
    if not repeated:
        assert is_genuine_sidon(A)
        return
    s = repeated[0]
    p = s // 2
    low = [a for a in A if a <= p]
    high = [a for a in A if a > p]
    assert is_genuine_sidon(low)
    assert is_genuine_sidon(high)

def exhaustive_verify(Nmax=16):
    for N in range(1, Nmax + 1):
        best = 0
        examples = []
        for mask in range(1 << N):
            A = [i + 1 for i in range(N) if (mask >> i) & 1]
            if not is_admissible(A):
                continue
            verify_core_and_differences(A)
            verify_sliding_identity(A, N)
            verify_half_partition(A, N)
            if len(A) > best:
                best = len(A)
                examples = [A]
            elif len(A) == best:
                examples.append(A)
        print(N, best, examples[:3])

def signed_offsets(X):
    X = sorted(X)
    vals = []
    for i in range(len(X)):
        for j in range(i + 1, len(X)):
            vals.append(X[j] - X[i])
    for i in range(len(X)):
        for j in range(i, len(X)):
            vals.append(X[i] + X[j])
    return vals

def signed_sidon(X):
    vals = signed_offsets(X)
    return len(vals) == len(set(vals)) == len(X) ** 2

def minimal_signed_diameter(q, Hmax):
    # Returns the first signed-Sidon set of size q with minimum maximum
    # coordinate, if one is found.
    for H in range(1, Hmax + 1):
        for prefix in combinations(range(1, H), q - 1):
            X = prefix + (H,)
            if signed_sidon(X):
                return X
    return None

def verify_signed_weighted_inequality(X, L):
    assert signed_sidon(X)
    X = sorted(X)
    q = len(X)
    w = X[-1] - X[0]

    D = [X[j] - X[i]
         for i in range(q) for j in range(i + 1, q)]
    S = [X[i] + X[j]
         for i in range(q) for j in range(i, q)]

    assert not (set(D) & set(S))
    assert len(D) == len(set(D))
    assert len(S) == len(set(S))

    DW = sum(max(0, L - d) for d in D)
    SW = sum(max(0, L - s) for s in S)
    capacity = L * (L - 1) // 2
    assert DW + SW <= capacity

    lower_D = Fraction(L * L * q * q, 2 * (w + L)) - Fraction(L * q, 2)
    assert Fraction(DW) >= lower_D

def duplicate_weight(A, L):
    occ = difference_data(A)
    return sum(L - d for d, pairs in occ.items()
               if len(pairs) == 2 and d < L)

# Basic finite signed-core examples.
assert signed_sidon([1, 2])
assert signed_sidon([1, 4, 10])

# Suggested searches:
# for q in range(1, 8):
#     X = minimal_signed_diameter(q, Hmax=200)
#     print(q, X, None if X is None else X[-1] / (q*q))
#
# Test whether minimum x_q/q^2 appears to move toward 3/2 or below it.
```

Particularly useful computations would be:

1. Compute the minimum \(x_q\) for signed-Sidon sets through at least \(q=8\) or \(9\), using SAT/CP-SAT rather than the simple enumeration above.
2. For exact maximizers of \(F(N)\), record the exceptional-core proportion and whether the core itself violates any proposed central-gap inequality.
3. Evaluate several position-dependent window systems on the Erdős–Freud construction, since the translation-invariant triangular weight is provably too weak.

## Route Diagnosis

**Proved ledger.**

- Genuine Sidon sets in an interval of length \(M\) have size \(\sqrt M+O(M^{1/4})\), via the sliding-window argument.
- Every admissible set satisfies
  \[
  |A|\le\sqrt{2N}+O(N^{1/4}).
  \]
- Doubled differences are exactly nonfixed reflection orbits of pairs in the exceptional core.
- Their exact number is \(t(t-1)\) without a central loop and \((t-1)^2\) with one.
- The master weighted inequality is (9).
- Fully reflected sets reduce exactly to the signed-Sidon packing condition (12).
- The conjectured bound holds for fully reflected sets whose sum and difference label ranges are separated.

**Plausible but unproved.**

- The signed-Sidon diameter estimate
  \[
  x_q\ge\left(\frac32-o(1)\right)q^2.
  \]
  This is already a sharp, difficult special case and may itself be false.
- A two-sided packing inequality of the informal form
  \[
  N\ge |A_-|^2+|A_+|^2+|A_-||A_+|-o(|A|^2),
  \]
  which would be sharp on the Erdős–Freud construction. No proof was found.

**Dead ends.**

- A universal estimate \(W_D(L)\le(1/6+o(1))L^2\) is false; the lower construction has \(W_D(L)\sim L^2/2\).
- Assuming that sums and differences occupy separated ranges is false: \(\{1,4,10\}\) gives an immediate interlacing example.
- Sliding-window Cauchy estimates using only total doubled-difference weight lose too much on the two-block construction.

A fresh Route 2 attempt should use position-sensitive windows that distinguish the two reflected occurrences of each doubled difference, or prove a genuinely arithmetic theorem saying that a near-maximal Sidon difference set cannot avoid a translated Sidon sum set without a shift of about \(q^2\). Since one-dimensional density relaxations allow much more efficient interlacing, purely marginal counting is unlikely to suffice. In parallel, computational searches for signed-Sidon sets with \(x_q<(3/2-\varepsilon)q^2\) are the fastest way to test whether the fully reflected special case—and hence the conjectured constant—is credible.