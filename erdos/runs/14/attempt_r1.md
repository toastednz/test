STATUS: BLOCKED

## Result

I did not resolve Q1 or Q2. Pursuing the finite Sidon-stability route yields three rigorous uniform results. First, if \(E_A(N)=o(N)\), then the total excess multiplicity satisfies
\[
\Delta_A(N)\ge \left(\frac{\sqrt2-1}{\sqrt2}-o(1)\right)\sqrt N.
\]
Consequently, if \(R_A(N)=\max_{n\le N}r_A(n)\), then
\[
E_A(N)\max(1,R_A(N))\gg \sqrt N.
\]
Thus Q1 holds for sets with \(R_A(N)=N^{o(1)}\). Second, a multiscale refinement gives the unconditional uniform lower bound
\[
E_A(N)\gg \frac{\log N}{\log\log N}.
\]
The route is blocked at the support-concentration step: the required \(\sqrt N\)-scale collision mass can be carried by very few sums, each of which is a large reflection matching. Standard Sidon stability does not rule this out.

## Complete Argument

### 1. Normalization at the least element

Let
\[
K=E_A(N).
\]
If \(K=N\), all the lower bounds below are immediate, so suppose \(K<N\). Then some \(n\le N\) has a representation, and \(A\) is nonempty. Let
\[
a=\min A.
\]
Since no integer below \(2a\) is representable,
\[
2a-1\le K.
\]
Put
\[
L=N-2a,\qquad B=A-a\subseteq\mathbb Z_{\ge0},\qquad
C=B\setminus\{0\}.
\]
For \(0\le t\le L\),
\[
r_B(t)=r_A(2a+t).
\]
Here \(r_B\) is interpreted using unordered pairs from the nonnegative set \(B\).

For \(t\ge1\),
\[
r_B(t)=1_C(t)+r_C(t),
\]
where \(r_C(t)\) counts unordered representations using two positive elements of \(C\). Define
\[
S=\{1\le t\le L:r_B(t)\ne1\}.
\]
Then
\[
|S|\le K.
\]

For every \(t\notin S\), exactly one of the following holds:

1. \(t\in C\) and \(r_C(t)=0\);
2. \(t\notin C\) and \(r_C(t)=1\).

Thus, away from \(S\), the interval is partitioned between elements of \(C\) and uniquely represented positive pair sums of \(C\).

---

### 2. A quantitative Sidon bound

We need a self-contained version of the classical upper bound.

**Lemma 1.** If \(D\subseteq[1,h]\) is Sidon, then
\[
|D|\le \sqrt h+2h^{1/4}+2.
\]

**Proof.**
Write
\[
D=\{d_1<\cdots<d_q\}.
\]
Let
\[
p=\lfloor h^{1/4}\rfloor.
\]
If \(q\le p\), the result is immediate. Otherwise consider all differences
\[
d_{i+j}-d_i,\qquad 1\le j\le p,\quad 1\le i\le q-j.
\]
They are distinct. Indeed, equality of two positive differences gives
\[
d_{i+j}+d_u=d_{u+v}+d_i,
\]
and the Sidon property forces the two ordered difference pairs to coincide.

Their number is
\[
M=pq-\frac{p(p+1)}2.
\]
For fixed \(j\),
\[
\sum_{i=1}^{q-j}(d_{i+j}-d_i)
=
\sum_{i=q-j+1}^{q}d_i-\sum_{i=1}^{j}d_i
\le jh.
\]
Therefore the sum of all \(M\) distinct positive differences is at most
\[
\frac{p(p+1)}2h.
\]
It is at least \(M(M+1)/2\), so
\[
M^2\le hp(p+1).
\]
Consequently,
\[
q\le \frac{p+1}{2}+\sqrt{\frac{h(p+1)}p}.
\]
For \(h\ge16\), \(p\ge h^{1/4}/2\), and hence the right side is at most
\[
\sqrt h+2h^{1/4}+2.
\]
The remaining finite values of \(h\) are immediate. ∎

---

### 3. Extracting a Sidon subset by paying excess multiplicity

Fix an integer \(h\) with
\[
2h\le L,
\]
and set
\[
C_h=C\cap[1,h],\qquad k=|C_h|.
\]
For \(s\le2h\), write
\[
m_h(s)=r_{C_h}(s).
\]
Define
\[
T_h=
\sum_{s\in S\cap[2,2h]}(m_h(s)-1)_+.
\]

**Lemma 2.** There is a Sidon subset \(D_h\subseteq C_h\) satisfying
\[
|D_h|\ge k-T_h.
\]

**Proof.**
If \(s\notin S\), then \(r_B(s)=1\), and therefore
\[
m_h(s)\le r_C(s)\le1.
\]

For a fixed \(s\in S\), the unordered pairs from \(C_h\) summing to \(s\) are pairwise vertex-disjoint: two different pairs sharing a summand would necessarily have the same other summand. Choose one pair to retain and, from every other pair, delete one of its vertices. This costs at most \(m_h(s)-1\) vertices.

Perform this operation for every \(s\in S\cap[2,2h]\). Deletions made for different sums may overlap, so at most \(T_h\) vertices are deleted in total. The remaining set has at most one unordered representation of every sum and is therefore Sidon. ∎

---

### 4. A collision-mass lower bound

At least \(h-K\) integers \(t\in[1,h]\) lie outside \(S\). Each such \(t\) is either an element of \(C_h\) or a pair sum of elements of \(C_h\). Hence
\[
h-K\le k+\frac{k(k+1)}2
=\frac{k^2+3k}{2}.
\tag{1}
\]

Take
\[
h_0=10^8.
\]

**Lemma 3.** If
\[
h\ge h_0,\qquad K\le \frac h8,\qquad 2h\le L,
\]
then
\[
T_h\ge \frac1{10}\sqrt h.
\]

**Proof.**
If \(k\le \frac65\sqrt h\), then
\[
\frac{k^2+3k}{2}
\le \frac{18}{25}h+\frac95\sqrt h.
\]
For \(h\ge h_0\), this is strictly less than \(7h/8\), whereas
\[
h-K\ge\frac{7h}{8},
\]
contradicting (1). Thus
\[
k>\frac65\sqrt h.
\]

By Lemma 1, every Sidon subset of \([1,h]\) has size at most
\[
\sqrt h+2h^{1/4}+2\le\frac{11}{10}\sqrt h
\]
for \(h\ge h_0\). Lemma 2 therefore gives
\[
k-T_h\le\frac{11}{10}\sqrt h.
\]
Since \(k>\frac65\sqrt h\),
\[
T_h>\frac1{10}\sqrt h.
\]
∎

---

### 5. Consequences for total excess and maximum multiplicity

Recall
\[
\Delta_A(N)=\sum_{\substack{n\le N\\r_A(n)\ge2}}(r_A(n)-1)
\]
and put
\[
R_A(N)=\max_{n\le N}r_A(n).
\]

For \(s\le2h\), the integer corresponding to \(s\) is \(2a+s\le N\). Moreover,
\[
m_h(s)\le r_A(2a+s).
\]
Thus
\[
T_h\le \Delta_A(N)
\tag{2}
\]
and also
\[
T_h\le K\,(R_A(N)-1).
\tag{3}
\]

Suppose \(K=o(N)\). Since \(2a-1\le K\),
\[
L=N-o(N).
\]
Take
\[
h=\left\lfloor\frac L2\right\rfloor
=\left(\frac12+o(1)\right)N.
\]
From (1),
\[
k\ge(\sqrt2-o(1))\sqrt h.
\]
Lemma 1 and Lemma 2 then give
\[
T_h\ge(\sqrt2-1-o(1))\sqrt h.
\]
Using \(h=(1/2+o(1))N\), we obtain
\[
\boxed{
\Delta_A(N)\ge
\left(\frac{\sqrt2-1}{\sqrt2}-o(1)\right)\sqrt N
}
\tag{4}
\]
and
\[
\boxed{
E_A(N)(R_A(N)-1)\ge
\left(\frac{\sqrt2-1}{\sqrt2}-o(1)\right)\sqrt N.
}
\tag{5}
\]

A coarse pointwise version is useful.

**Corollary 4.** There are absolute constants \(c>0\) and \(N_0\) such that, for every \(A\) and every \(N\ge N_0\),
\[
E_A(N)\max\{1,R_A(N)\}\ge c\sqrt N.
\tag{6}
\]

**Proof.**
If \(K\ge N/100\), the result is immediate. Otherwise
\[
L\ge N-K-1
\]
and
\[
h=\lfloor L/2\rfloor\ge0.49N
\]
for sufficiently large \(N\). Also \(K<h/8\), so Lemma 3 gives
\[
T_h\ge\frac1{10}\sqrt h\gg\sqrt N.
\]
Now use (3). ∎

In particular, if a fixed set \(A\) satisfies
\[
R_A(N)=N^{o(1)},
\]
then
\[
E_A(N)=N^{1/2-o(1)}.
\]
Thus Q1 is proved for this restricted class of sets.

---

### 6. Bounding the capacity of an old exceptional sum

To get a support bound, rather than merely a collision-mass bound, we need to know how much mass one exceptional sum can carry.

**Lemma 5.** Suppose \(2s\le L\), and put
\[
q_s=|C\cap[1,s]|.
\]
Then
\[
q_s\le K+2\sqrt s.
\tag{7}
\]
Consequently, a fixed sum \(s\) has at most
\[
\frac K2+\sqrt s+1
\tag{8}
\]
representations by positive elements of \(C\).

**Proof.**
All \(q_s(q_s+1)/2\) unordered pairs from \(C\cap[1,s]\) have sums at most \(2s\). At a sum outside \(S\), there is at most one such pair. At a sum in \(S\), there are at most \(\lceil q_s/2\rceil\), because representations of one fixed sum are pairwise vertex-disjoint. Hence
\[
\frac{q_s(q_s+1)}2
\le 2s+K\left\lceil\frac{q_s}{2}\right\rceil
\le 2s+\frac K2(q_s+1).
\]
Therefore
\[
(q_s-K)(q_s+1)\le4s.
\]
If \(q_s>K+2\sqrt s\), both factors on the left would exceed \(2\sqrt s\), a contradiction. This proves (7). The fixed-sum matching bound then gives
\[
r_C(s)\le\left\lceil\frac{q_s}{2}\right\rceil
\le\frac K2+\sqrt s+1.
\]
∎

---

### 7. A uniform logarithmic support bound

We now combine the collision-mass lower bound at many scales with Lemma 5.

Let
\[
h_*=\max\{h_0,1600K^4\},
\qquad
Q=6400K^2.
\]

**Lemma 6.** If
\[
h\ge h_*,\qquad 2h\le L,
\]
then \(S\) contains an element in
\[
\left(\frac{h}{1600K^2},\,2h\right].
\tag{9}
\]

**Proof.**
Set
\[
u=\frac{h}{1600K^2}.
\]
Suppose, to the contrary, that every exceptional sum at most \(2h\) is at most \(u\).

Lemma 3 gives
\[
T_h\ge\frac1{10}\sqrt h.
\tag{10}
\]
Every exceptional \(s\le u\) contributes at most, by Lemma 5,
\[
\frac K2+\sqrt u+1.
\]
Since there are at most \(K\) such sums,
\[
T_h
\le K\left(\frac K2+\sqrt u+1\right)
=\frac{K^2}{2}+K+\frac{\sqrt h}{40}.
\]
Because \(h\ge1600K^4\),
\[
\sqrt h\ge40K^2.
\]
For \(K\ge1\),
\[
\frac{K^2}{2}+K\le\frac{3K^2}{2}
\le\frac{3}{80}\sqrt h.
\]
Hence
\[
T_h\le\left(\frac{3}{80}+\frac{2}{80}\right)\sqrt h
=\frac1{16}\sqrt h,
\]
contradicting (10). ∎

Now let
\[
h_j=h_*Q^j,\qquad j=0,1,\dots,K.
\]
The intervals supplied by Lemma 6 are pairwise disjoint, because
\[
\frac{h_{j+1}}{1600K^2}
=4h_j>2h_j.
\]
If \(2h_K\le L\), Lemma 6 would produce \(K+1\) distinct elements of \(S\), contradicting \(|S|\le K\). Therefore
\[
L<2h_*Q^K.
\]
Since \(2a\le K+1\),
\[
N=L+2a
<
K+1+
2\max\{h_0,1600K^4\}(6400K^2)^K.
\tag{11}
\]
Taking logarithms gives an absolute constant \(C\) such that
\[
\log N\le C(K+1)\log(K+2).
\]
Inverting this inequality yields the following.

**Theorem 7.** There are absolute constants \(c>0\) and \(N_0\) such that, uniformly for every \(A\subseteq\mathbb N\),
\[
\boxed{
E_A(N)\ge c\frac{\log N}{\log\log N}
}
\qquad(N\ge N_0).
\tag{12}
\]

The same bound applies to the finite extremal function:
\[
D(N)\gg\frac{\log N}{\log\log N}.
\]

This is far short of \(N^{1/2-o(1)}\).

---

### 8. Compactness interpretation of \(D(N)\)

For completeness, there is a useful equivalence explaining why even qualitative growth of \(D(N)\) is structurally meaningful.

**Proposition 8.** The following are equivalent:

1. \(D(N)\) is bounded along an unbounded sequence of \(N\);
2. there exists \(A\subseteq\mathbb N\) for which \(r_A(n)=1\) for all but finitely many \(n\).

**Proof.**
The implication \(2\Rightarrow1\) follows by taking \(A\cap[1,N]\).

Conversely, suppose \(D(N_j)\le K\) with \(N_j\to\infty\). Choose \(X_j\subseteq[1,N_j]\) realizing this bound and regard each \(X_j\) as an infinite zero-one sequence. By a diagonal subsequence argument, assume membership of every fixed integer eventually stabilizes. Let \(A\) be the pointwise limit.

For every fixed \(M\), all representation counts \(r_{X_j}(n)\), \(n\le M\), eventually agree with \(r_A(n)\), since they depend only on membership below \(M\). Therefore
\[
E_A(M)\le K.
\]
Letting \(M\to\infty\), \(A\) has at most \(K\) exceptional integers. ∎

Theorem 7 therefore rules out an eventually unique representation basis, but gives no polynomial rate.

## Self-Audit

1. **Sidon extraction from exceptional fibers.**  
   The delicate point is that deleting one vertex from each representation beyond the first must eliminate all collisions. This holds because representations of a fixed sum are vertex-disjoint; deletions for different sums can only overlap and reduce the total cost.

2. **The multiscale reservoir argument.**  
   The main possible source of an indexing error is the use of Lemma 5 for old sums. It is valid because the chosen cutoff \(u\le h\) and \(2h\le L\), hence \(2s\le L\) for every \(s\le u\). The windows are disjoint by the explicit factor \(Q=6400K^2\).

3. **Passage from shifted collision mass to the original \(\Delta_A(N)\).**  
   Every shifted sum \(s\le2h\) corresponds to \(2a+s\le N\), and every \(C_h\)-representation is also an \(A\)-representation. Hence \((m_h(s)-1)_+\le(r_A(2a+s)-1)_+\). No later or larger elements can invalidate this inequality.

The central missing support estimate is not being asserted: nothing proved here prevents one exceptional sum from carrying \(\Theta(\sqrt N)\) representations.

## Computations To Verify

```python
from itertools import combinations
from math import sqrt, log

def representation_counts(A, N):
    """Exact unordered representation counts."""
    A = sorted(a for a in set(A) if a <= N - 1)
    r = [0] * (N + 1)
    for i, a in enumerate(A):
        for b in A[i:]:
            s = a + b
            if s > N:
                break
            r[s] += 1
    return r

def exceptional_data(A, N):
    r = representation_counts(A, N)
    bad = [n for n in range(1, N + 1) if r[n] != 1]
    missing = [n for n in bad if r[n] == 0]
    multiple = [n for n in bad if r[n] >= 2]
    Delta = sum(max(0, r[n] - 1) for n in range(1, N + 1))
    R = max(r[1:], default=0)
    return {
        "E": len(bad),
        "bad": bad,
        "missing": missing,
        "multiple": multiple,
        "Delta": Delta,
        "R": R,
        "r": r,
    }

def exhaustive_D(N):
    """Exact brute force; practical only for small N."""
    best = N + 1
    witnesses = []
    # Membership of N is irrelevant for sums <= N.
    for mask in range(1 << (N - 1)):
        X = {i + 1 for i in range(N - 1) if (mask >> i) & 1}
        E = exceptional_data(X, N)["E"]
        if E < best:
            best = E
            witnesses = [X]
        elif E == best:
            witnesses.append(X)
    return best, witnesses

def normalized_reps(B, L):
    """B is a subset of {0,...,L} containing 0."""
    B = sorted(set(B))
    r = [0] * (L + 1)
    for i, a in enumerate(B):
        for b in B[i:]:
            s = a + b
            if s > L:
                break
            r[s] += 1
    return r

# A long prefix with only one shifted exception:
B = {0, 1, 3, 5, 6, 13, 15}
rB = normalized_reps(B, 15)
assert [t for t in range(16) if rB[t] != 1] == [6]

# Translating by 1 gives two original exceptions through N=17:
# n=1 is missing and n=8 corresponds to shifted sum 6.
A = {b + 1 for b in B}
assert exceptional_data(A, 17)["bad"] == [1, 8]

def find_normalized_prefix(L, K):
    """
    Find B subset {0,...,L}, 0 in B, with at most K exceptional
    representation counts among t=1,...,L.
    """
    x = [0] * (L + 1)
    x[0] = 1

    def dfs(t, defects):
        if defects > K:
            return None
        if t == L + 1:
            return {i for i, bit in enumerate(x) if bit}

        for bit in (0, 1):
            x[t] = bit
            rt = sum(x[i] * x[t - i] for i in range(t // 2 + 1))
            ans = dfs(t + 1, defects + (rt != 1))
            if ans is not None:
                return ans
        x[t] = 0
        return None

    return dfs(1, 0)

def scale_diagnostics(B, L, h):
    """
    Compute k and T_h from the proof for a normalized B containing 0.
    """
    rB = normalized_reps(B, L)
    S = {t for t in range(1, L + 1) if rB[t] != 1}
    C = set(B) - {0}
    Ch = sorted(c for c in C if c <= h)
    m = [0] * (2 * h + 1)

    for i, a in enumerate(Ch):
        for b in Ch[i:]:
            if a + b <= 2 * h:
                m[a + b] += 1

    T = sum(max(0, m[s] - 1)
            for s in S if 2 <= s <= 2 * h)

    return {
        "K": len(S),
        "k": len(Ch),
        "T": T,
        "coverage_rhs": len(Ch) + len(Ch) * (len(Ch) + 1) // 2,
        "coverage_lhs": h - len(S),
    }

# Directly verify the numerical constants used in Lemma 3.
h0 = 10**8
assert 0.72 * h0 + 1.8 * sqrt(h0) < 0.875 * h0
assert sqrt(h0) + 2 * h0**0.25 + 2 <= 1.1 * sqrt(h0)
```

Useful finite searches would record, for each optimizer:

```python
for N in range(2, 23):
    D, W = exhaustive_D(N)
    X = W[0]
    data = exceptional_data(X, N)
    print(N, D, D / sqrt(N), data["R"], data["Delta"], sorted(X))
```

The key diagnostic is whether small-support optimizers have \(R_A(N)\) growing rapidly enough to saturate
\[
E_A(N)R_A(N)\gg\sqrt N.
\]

## Route Diagnosis

**What worked.**

- Normalizing at the least element turns unique representation into an almost-partition
  \[
  [1,h]\approx C\ \dot\cup\ (C+C).
  \]
- Deleting one vertex for every excess representation produces a genuine Sidon subset.
- The leading constants \(\sqrt2\) from coverage and \(1\) from the Sidon bound force \(\Theta(\sqrt N)\) total collision mass.
- Bounding the capacity of collision reservoirs at earlier scales and using disjoint scale windows yields
  \[
  D(N)\gg\frac{\log N}{\log\log N}.
  \]

**Precise block.**

The Sidon deletion argument controls
\[
\sum_{n\le N}(r_A(n)-1)_+,
\]
not the number of sums supporting this excess. A fixed sum is a reflection matching and can contain \(\Theta(\sqrt N)\) pair representations. Thus all the collision mass required by Sidon stability may be concentrated on very few exceptional sums. The product bound
\[
E_A(N)R_A(N)\gg\sqrt N
\]
is essentially sharp for this method unless one proves a new restriction on high-multiplicity reflection fibers.

**Plausible but unproved next lemma.**

A useful breakthrough would be a rigidity theorem saying that if one or a few exceptional sums support large reflection matchings, then the near-complete covering condition forces many additional exceptional sums. Compositions of the associated reflections become translations, so simultaneous large fibers should impose approximate periodicity; no quantitative theorem strong enough to yield \(N^{1/2-o(1)}\) has been established here.

**Dead ends.**

- Raw pair and difference counting fails because collisions may concentrate on a matching at one sum.
- Extracting an independent set from the union of \(K\) reflection matchings loses a factor comparable to \(K\), far too much near the critical Sidon constant.
- A bounded-gap recurrence for exceptional coefficients is false as a naive statement: the normalized set
  \[
  \{0,1,3,5,6,13,15\}
  \]
  has exactly one exception through \(15\).
- Moment or energy bounds reproduce the \(\sqrt N\) collision-mass obstruction but do not control its support.

A fresh Route 1 attempt should classify simultaneous high-multiplicity reflection fibers and combine that classification with interval coverage. Without such a concentration-breaking theorem, the finite Sidon-stability route remains blocked well below the target exponent.