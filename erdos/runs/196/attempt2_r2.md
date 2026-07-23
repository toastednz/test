STATUS: BLOCKED

## Result

I did not resolve Erdős Problem #196. I proved that Route 2’s proposed fixed-anchor rank-escape lemma is maximally false:
\[
R_K(N)=K\qquad\text{for every }1\le K\le N.
\]
More strongly, for every fixed \(K\) there is a total order on \(\mathbb N\) avoiding all monotone four-term arithmetic progressions in which \(1,\dots,K\) occupy the first \(K\) places. The construction splices the LSB order on \([K]\) to the reverse LSB order on its complement. It is not a permutation order: every value greater than \(K\) has infinitely many predecessors. I also give an exact compactness reformulation using a full infinite vector of rank bounds. That reformulation shows precisely what remains: one must rule out every globally compatible deadline vector, which is equivalent in strength to the original problem.

## Complete Argument

### 1. Two properties of the LSB order

Write \(\triangleleft\) for the least-significant-bit order. Thus, for distinct \(u,v\), if \(t\) is the least binary position at which they differ, then
\[
u\triangleleft v
\quad\Longleftrightarrow\quad
\varepsilon_t(u)<\varepsilon_t(v).
\]

This is a total order because it is lexicographic order on binary digit sequences read from the least significant digit upward.

#### Lemma 1: Midpoint extremality

For every \(x,d\ge1\), the middle term \(x+d\) is an extremum relative to \(x\) and \(x+2d\) in the LSB order. Consequently, neither the LSB order nor its reverse contains a monotone three-term arithmetic progression.

**Proof.**

Let \(t=\nu_2(d)\). Modulo \(2^{t+1}\),
\[
d\equiv 2^t.
\]
The binary digits below position \(t\) of
\[
x,\quad x+d,\quad x+2d
\]
are therefore equal. Their \(t\)-th digits have the form
\[
b,\quad 1-b,\quad b.
\]
Thus the first LSB comparison between the midpoint and either endpoint occurs at position \(t\), and both endpoints lie on the same side of the midpoint. Hence the midpoint is either before both endpoints or after both endpoints. Reversing the order merely interchanges “before” and “after.” ∎

#### Lemma 2: Opposite-pair periodicity

For every \(a,d\ge1\),
\[
a\triangleleft a+d
\quad\Longleftrightarrow\quad
a+2d\triangleleft a+3d.
\tag{1}
\]

**Proof.**

Again let \(t=\nu_2(d)\). The digits below \(t\) agree among all four terms, while their \(t\)-th digits alternate:
\[
b,\quad 1-b,\quad b,\quad 1-b.
\]
Therefore the first comparison of \(a\) with \(a+d\) is identical to the first comparison of \(a+2d\) with \(a+3d\). ∎

---

### 2. A spliced avoiding order with an arbitrarily long finite initial segment

Fix \(K\ge1\). Define a total order \(\prec_K\) on \(\mathbb N\) as follows:

1. Every element of \([K]\) precedes every element greater than \(K\).
2. On \([K]\), use the LSB order:
   \[
   u\prec_K v\iff u\triangleleft v.
   \]
3. On \(\{K+1,K+2,\dots\}\), use the reverse LSB order:
   \[
   u\prec_K v\iff v\triangleleft u.
   \]

This is the ordinal sum of a finite LSB-ordered block and a reverse-LSB-ordered tail, hence is a strict total order.

#### Theorem 3: The spliced order avoids every monotone four-term progression

For every \(a,d\ge1\), the progression
\[
z_i=a+id,\qquad 0\le i\le3,
\]
is neither increasing nor decreasing under \(\prec_K\).

**Proof.**

Because \(z_0<z_1<z_2<z_3\) numerically and \([K]\) is a numerical initial interval, there is some \(j\in\{0,1,2,3,4\}\) such that precisely
\[
z_0,\dots,z_{j-1}
\]
belong to \([K]\).

We consider the five cases.

**Case \(j=0\).** All four terms lie in the reverse-LSB tail. A monotone four-term progression would make its first three terms monotone, contradicting Lemma 1.

**Case \(j=4\).** All four terms lie in the LSB block. Again, a monotone four-term progression would contain a monotone first triple, contradicting Lemma 1.

**Case \(j=1\).** We have
\[
z_0\prec_K z_1
\]
because \(z_0\) is in the first block and \(z_1\) is in the tail. Thus the four terms cannot be decreasing. If they were increasing, then
\[
z_1\prec_K z_2\prec_K z_3,
\]
which would be a monotone three-term progression in the reverse-LSB tail, contradicting Lemma 1.

**Case \(j=3\).** Again the block boundary gives
\[
z_2\prec_K z_3,
\]
so the progression cannot be decreasing. If it were increasing, then
\[
z_0\prec_K z_1\prec_K z_2
\]
would be a monotone three-term progression in the LSB block, contradicting Lemma 1.

**Case \(j=2\).** The block boundary gives
\[
z_1\prec_K z_2,
\]
so decreasing order is impossible. Suppose the progression were increasing. Then, inside the first block,
\[
z_0\triangleleft z_1.
\]
By Lemma 2,
\[
z_2\triangleleft z_3.
\]
But the tail uses the reverse LSB order, so the last relation implies
\[
z_3\prec_K z_2,
\]
contradicting the required increasing order \(z_2\prec_K z_3\).

All cases are excluded. ∎

---

### 3. Exact evaluation of the rank-escape statistic

Recall
\[
R_K(N)=
\min_{\prec}\max_{1\le s\le K} r_N(s),
\]
where the minimum is over four-term-avoiding orders on \([N]\).

#### Corollary 4

For every \(1\le K\le N\),
\[
R_K(N)=K.
\]

**Proof.**

In any order on \([N]\), the \(K\) values \(1,\dots,K\) have \(K\) distinct positive ranks. Hence
\[
\max_{1\le s\le K}r_N(s)\ge K.
\]

Conversely, restrict \(\prec_K\) from Theorem 3 to \([N]\). It remains avoiding. Every member of \([K]\) precedes every value greater than \(K\), so the ranks of \(1,\dots,K\) are exactly \(1,\dots,K\) in some order. Therefore
\[
\max_{1\le s\le K}r_N(s)=K.
\]
The lower and upper bounds coincide. ∎

Thus the proposed fixed-anchor rank-escape assertion
\[
R_K(N)\longrightarrow\infty
\]
fails for every fixed \(K\), and in the strongest possible way.

The same construction blocks every fixed-anchor weighted variant. For fixed nonnegative weights \(w_1,\dots,w_K\),
\[
\min_{\prec}\sum_{s=1}^K w_s r_N(s)
\le K\sum_{s=1}^K w_s,
\]
uniformly in \(N\).

---

### 4. Why this is not a counterexample permutation

The first \(K\) elements have finite predecessor sets under \(\prec_K\). Every \(n>K\), however, has infinitely many predecessors.

Indeed, choose any \(t\) larger than the binary length of \(n\), and put
\[
m_t=n+2^t.
\]
The first binary position at which \(n\) and \(m_t\) differ is \(t\), where \(n\) has digit \(0\) and \(m_t\) has digit \(1\). Thus
\[
n\triangleleft m_t.
\]
Since both are in the reverse-LSB tail,
\[
m_t\prec_K n.
\]
There are infinitely many such \(t\), so \(n\) has infinitely many predecessors.

Consequently \(\prec_K\) is not of order type \(\omega\). It is therefore not a disproof of the original problem. It shows instead that the non-\(\omega\) defect of an avoiding order can be pushed past any prescribed finite initial set.

---

### 5. The exact rank-box formulation

Although fixed-anchor rank escape fails, one can formulate the remaining rank problem exactly.

#### Proposition 5: Rank-box compactness criterion

There exists an avoiding permutation of \(\mathbb N\) if and only if there is a sequence of positive integers
\[
C=(C_1,C_2,\dots)
\]
such that, for every \(N\), there is a four-term-avoiding order on \([N]\) satisfying
\[
r_N(n)\le C_n
\qquad(1\le n\le N).
\tag{2}
\]

**Proof.**

Suppose first that \(p\) is an avoiding permutation. Set
\[
C_n=p(n).
\]
In the induced order on \([N]\), only some of the values that precede \(n\) in the full permutation remain present. Therefore
\[
r_N(n)\le p(n)=C_n.
\]
Thus (2) holds for every \(N\).

Conversely, suppose a sequence \(C\) satisfying the stated condition exists. Form a rooted tree whose level-\(N\) vertices are the avoiding orders on \([N]\) satisfying (2). Join an order on \([N+1]\) to its restriction to \([N]\).

Restriction preserves avoidance, and
\[
r_N(n)\le r_{N+1}(n),
\]
so the restriction still satisfies its rank bounds. The tree is therefore prefix-closed. It has a vertex at every level by assumption and is finitely branching because there are only finitely many orders on every \([N]\). By König’s infinity lemma it has an infinite branch.

The nested orders on this branch define a total order \(\prec\) on \(\mathbb N\). Every four-term progression occurs in some finite level, so \(\prec\) avoids every monotone four-term progression.

For a fixed \(n\), it has at most \(C_n-1\) predecessors. Otherwise choose \(C_n\) distinct predecessors of \(n\), and then choose \(N\) containing all of them and \(n\). This would give
\[
r_N(n)\ge C_n+1,
\]
contrary to (2).

It remains to verify that a total order in which every element has finitely many predecessors is induced by a permutation. Define
\[
q(n)=1+\#\{m:m\prec n\}.
\]
If \(u\prec v\), every predecessor of \(u\), as well as \(u\) itself, precedes \(v\). Hence
\[
q(u)<q(v),
\]
so \(q\) is injective.

The range of \(q\) is downward closed: if \(q(n)=r\), the \(r-1\) predecessors of \(n\), listed in increasing order, have ranks \(1,\dots,r-1\). Since \(q\) is an injection from an infinite set into \(\mathbb N\), its range is infinite. An infinite downward-closed subset of \(\mathbb N\) is all of \(\mathbb N\). Thus \(q\) is a bijection and is the required position function.

Therefore the limiting order gives an avoiding permutation. ∎

Accordingly, an affirmative solution is equivalent to proving:

> For every sequence \(C_1,C_2,\dots\), some finite level \(N\) admits no avoiding order satisfying all the bounds \(r_N(n)\le C_n\).

Unlike fixed-anchor rank escape, this statement involves infinitely many mutually compatible deadlines. Proposition 5 shows that proving it is equivalent to solving the original problem, not an independent reduction of lesser strength.

### Ledger

**Proved**

1. LSB midpoint extremality and opposite-pair periodicity.
2. The LSB/reverse-LSB splice \(\prec_K\) avoids every monotone four-term progression.
3. \(R_K(N)=K\) for all \(K\le N\).
4. Every tail element of \(\prec_K\) has infinitely many predecessors.
5. The full rank-box compactness criterion, Proposition 5.

**Plausible but unproved**

1. A genuinely nonlocal classification theorem might show that no single infinite deadline vector \(C\) supports finite avoiders at all levels.
2. Finite avoiders satisfying increasingly many deadlines may be forced to change their LSB-like hierarchy incompatibly from one scale to the next.

No proof of either statement was obtained.

**Dead ends**

1. Fixed-anchor rank escape is false for every \(K\).
2. Fixed finite weighted rank objectives cannot diverge.
3. Taking \(K\to\infty\) in the spliced orders does not produce a permutation order: for every fixed pair, the limiting comparison is the ordinary LSB comparison, recovering the known non-\(\omega\) order.

## Self-Audit

1. **The splice proof hinges on the \(j=2\) boundary case.** This is the point most susceptible to a hidden orientation error. It holds because the two standard-LSB comparisons at positions \(0,1\) and \(2,3\) are identical, while the second pair is deliberately ordered by reverse LSB.

2. **The constructed orders are not permutation orders.** This sharply limits the result’s relevance to the original problem. I explicitly verified the defect: every tail element \(n\) has the infinitely many predecessors \(n+2^t\) for sufficiently large \(t\).

3. **Proposition 5 does not advance the final compactness obstruction.** It is an exact reformulation, and therefore comparable in strength to the original problem. I believe the equivalence itself is sound because both directions are explicit, with the converse supplied by a finitely branching tree and a direct proof of finite predecessor sets.

## Computations To Verify

The following Python verifies the splice construction, Lemmas 1–2, and the exact value \(R_K(N)=K\) for small cases by exhaustive enumeration.

```python
from functools import cmp_to_key
from itertools import permutations

def cmp_lsb(u, v):
    """-1 if u is before v in standard LSB order, +1 if after."""
    if u == v:
        return 0
    z = u ^ v
    low = z & -z                 # lowest differing binary position
    bu = 1 if (u & low) else 0
    bv = 1 if (v & low) else 0
    return -1 if bu < bv else 1

def cmp_splice(u, v, K):
    """LSB on [K], reverse LSB above K, first block before second."""
    if u == v:
        return 0
    au = (u <= K)
    av = (v <= K)
    if au != av:
        return -1 if au else 1
    c = cmp_lsb(u, v)
    return c if au else -c

def positions_from_cmp(N, cmp):
    seq = sorted(range(1, N + 1), key=cmp_to_key(cmp))
    p = {v: i + 1 for i, v in enumerate(seq)}
    return seq, p

def is_four_AP_avoider(p, N):
    for d in range(1, (N - 1) // 3 + 1):
        for a in range(1, N - 3*d + 1):
            r = [p[a + i*d] for i in range(4)]
            inc = all(r[i] < r[i+1] for i in range(3))
            dec = all(r[i] > r[i+1] for i in range(3))
            if inc or dec:
                return False, (a, d, r)
    return True, None

# Lemma 1: every LSB three-term AP has opposite adjacent signs.
for a in range(1, 200):
    for d in range(1, 100):
        c1 = cmp_lsb(a, a + d)
        c2 = cmp_lsb(a + d, a + 2*d)
        assert c1 == -c2

# Lemma 2: first and third adjacent comparisons agree in standard LSB.
for a in range(1, 200):
    for d in range(1, 100):
        assert cmp_lsb(a, a + d) == cmp_lsb(a + 2*d, a + 3*d)

# Verify the splice for many finite restrictions.
for N in range(1, 50):
    for K in range(1, N + 1):
        cmp = lambda u, v, K=K: cmp_splice(u, v, K)
        seq, p = positions_from_cmp(N, cmp)
        ok, witness = is_four_AP_avoider(p, N)
        assert ok, (N, K, witness)

        # The first K positions are exactly the values 1,...,K.
        assert set(seq[:K]) == set(range(1, K + 1))
        assert max(p[s] for s in range(1, K + 1)) == K

# Verify infinitely many explicit predecessor witnesses symbolically
# for a finite sample of large t.
for K in range(1, 20):
    for n in range(K + 1, K + 20):
        for t in range(n.bit_length() + 1, n.bit_length() + 10):
            m = n + (1 << t)
            assert cmp_splice(m, n, K) == -1

# Exhaustively compute R_K(N) for small N.
def brute_R_values(N):
    best = [None] + [N + 1] * N

    for seq in permutations(range(1, N + 1)):
        p = {v: i + 1 for i, v in enumerate(seq)}
        ok, _ = is_four_AP_avoider(p, N)
        if not ok:
            continue

        current_max = 0
        for K in range(1, N + 1):
            current_max = max(current_max, p[K])
            best[K] = min(best[K], current_max)

    return best

for N in range(1, 9):
    best = brute_R_values(N)
    for K in range(1, N + 1):
        assert best[K] == K, (N, K, best[K])
```

A useful next computation is no longer to optimize \(R_K(N)\), whose value is now exact, but to choose candidate deadline vectors \(C_n\) and solve the bounded-rank finite instances
\[
r_N(n)\le C_n\qquad(n\le N).
\]
Certified infeasibility for one particular \(C\) is only evidence; an affirmative proof must handle every \(C\).

## Route Diagnosis

Route 2’s clean proposed mechanism—fixed-anchor rank escape—fails completely. Finite avoiders can keep any prescribed initial interval \([K]\) in the first \(K\) ranks for arbitrarily large \(N\), indeed inside one global avoiding total order. Thus neither extremum counts, LSB stability, containers, nor weighted rank objectives can prove escape using only finitely many fixed anchors.

What remains potentially viable is a cross-scale compatibility theorem: finite orders may meet every finite collection of bounded-rank requirements separately while being unable to meet one fixed infinite collection coherently. Proposition 5 shows that this is exactly the missing issue. No such theorem was proved here, and reducing to it without additional structure would merely restate the original problem.

A fresh attempt along Route 2 should therefore abandon \(R_K(N)\) and study the transition maps between bounded-rank avoiders at successive levels. In particular, it should search for a monotone invariant that accumulates injury whenever a new value is inserted before an old one, and whose total injury cannot remain finite for every value. Any invariant depending only on the ranks of a fixed finite anchor set is ruled out by the spliced construction above.