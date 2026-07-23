STATUS: BLOCKED

## Result

Route 3 yields an exact and useful reformulation: a transitive pair-coloring comes from a permutation of \(\mathbb N\) precisely when every vertex has only finitely many larger numerical labels colored backwards. This implies strong “eventual forwardness,” affine-ray minimum constraints, quadratic lower bounds on both comparison colors, and rigid rank-layer restrictions. However, the direct extension of the DEGS three-term minimum argument fails sharply: I construct an explicit order of type \(\omega\) satisfying all avoidance constraints involving the globally first element. Standard Ramsey extraction also loses all additive structure, and a finite-gadget lemma proves that this loss cannot be repaired by any fixed family of disjoint finite templates. Thus Route 3 is blocked at the need to exploit the simultaneous overlap of infinitely many translated affine-ray constraints.

## Complete Argument

### 1. Exact characterization of the order-type-\(\omega\) condition

Let \(c\) be a transitive coloring of pairs \(u<v\) by
\[
c(u,v)=
\begin{cases}
+,&u\prec v,\\
-,&v\prec u,
\end{cases}
\]
where \(\prec\) is the total order represented by \(c\).

#### Lemma 1: Finite-predecessor characterization

The order \(\prec\) is induced by a permutation of \(\mathbb N\) if and only if every element has finitely many \(\prec\)-predecessors.

Equivalently,
\[
\forall u\in\mathbb N,\qquad
\#\{v>u:c(u,v)=-\}<\infty.
\tag{1}
\]

Equivalently again, for every \(u\) there is \(N(u)\) such that
\[
v>N(u)\implies c(u,v)=+.
\tag{2}
\]

#### Proof

If \(\prec\) is induced by a permutation rank function \(p\), then \(u\) has exactly \(p(u)-1\) predecessors.

Conversely, suppose every principal predecessor set is finite. Define
\[
r(u)=1+\#\{v:v\prec u\}.
\]
If \(u\prec v\), every predecessor of \(u\), as well as \(u\) itself, is a predecessor of \(v\). Hence \(r(u)<r(v)\), so \(r\) is injective and order-preserving.

The finite predecessor set of an element with rank \(m\) is itself a finite total order of size \(m-1\); inductively its elements have ranks \(1,\dots,m-1\). Since the underlying set is infinite, the ranks are unbounded, and therefore every positive integer occurs. Thus \(r:\mathbb N\to\mathbb N\) is a bijection and \(\prec\) has order type \(\omega\).

For the equivalence with (1), the predecessors of \(u\) consist of at most \(u-1\) labels below \(u\), together with those \(v>u\) for which \(c(u,v)=-\). Thus the predecessor set is finite exactly when (1) holds. Since a finite subset of \(\mathbb N\) has a maximum, (1) is equivalent to (2). ∎

Thus Route 3 can be stated exactly as follows:

> Does every transitive pair-coloring satisfying eventual forwardness (2) have a four-term arithmetic progression whose three consecutive pairs have the same color?

This is an exact reformulation, not yet a simplification.

---

### 2. What ordinary Ramsey theory gives—and why it is insufficient

#### Lemma 2: Every infinite homogeneous set is forward

For every permutation order \(p\), infinite Ramsey theory gives an infinite set
\[
H=\{h_1<h_2<\cdots\}
\]
on which \(c\) is constant. Its color must be \(+\).

#### Proof

If its color were \(-\), then
\[
p(h_1)>p(h_2)>p(h_3)>\cdots,
\]
an infinite strictly decreasing sequence of positive integers, which is impossible. ∎

This does not provide an arithmetic progression. For example, for the identity permutation, the set
\[
\{1,2,4,8,16,\dots\}
\]
is homogeneous \(+\) and contains no nontrivial three-term arithmetic progression, hence no four-term one.

So the standard Ramsey extraction discards exactly the additive structure needed in the problem.

---

### 3. Affine restrictions and eventual endpoint constraints

Every infinite arithmetic ray inherits order type \(\omega\).

#### Lemma 3: Affine self-similarity

Fix \(r,q\ge1\), and consider
\[
R=\{r,r+q,r+2q,\dots\}.
\]
The restriction of \(\prec\) to \(R\) has order type \(\omega\). If \(p\) avoids monotone four-term progressions, then the rescaled order on the indices of \(R\) does also.

#### Proof

Each element has only finitely many predecessors globally and therefore only finitely many predecessors in \(R\). Lemma 1 applies. An arithmetic progression in the indices maps under \(n\mapsto r+nq\) to an arithmetic progression in \(\mathbb N\), so avoidance is inherited. ∎

Let \(b\) be the earliest element of \(R\), and suppose \(b=r+n_0q\). Then for every \(d\ge1\),
\[
p(b)<p(b+qd),p(b+2qd),p(b+3qd).
\]
Consequently, avoidance forces
\[
p(b+qd)>p(b+2qd)
\quad\text{or}\quad
p(b+2qd)>p(b+3qd).
\tag{3}
\]

There is also a pointwise eventual version using the full strength of finite predecessors.

#### Lemma 4: Every fixed label is eventually the first endpoint

For every fixed \(b\), there is \(D(b)\) such that for all \(d\ge D(b)\),
\[
p(b)<p(b+d),\quad p(b)<p(b+2d),\quad p(b)<p(b+3d).
\]
Hence a counterexample would have to satisfy
\[
p(b+d)>p(b+2d)
\quad\text{or}\quad
p(b+2d)>p(b+3d)
\tag{4}
\]
for every sufficiently large \(d\).

#### Proof

The predecessor set
\[
F_b=\{n:p(n)<p(b)\}
\]
is finite. Let \(M_b=\max(F_b\cup\{b\})\). If \(d>M_b\), then \(b+d,b+2d,b+3d>M_b\), so none belongs to \(F_b\). This proves the first assertion.

Because \(p(b)\) is then the smallest of the four ranks, the four ranks cannot be decreasing. They are increasing exactly when
\[
p(b+d)<p(b+2d)<p(b+3d).
\]
Negating this strict chain gives (4). ∎

The unresolved difficulty is compatibility of (4) as \(b\) ranges over every positive integer.

---

### 4. The global-minimum extension of the DEGS argument fails

The DEGS three-term proof follows immediately from a global minimum. If \(p(m)=1\) and there were no increasing three-term progression starting at \(m\), then
\[
p(m+d)>p(m+2d)
\]
for every \(d\). Replacing \(d\) successively by \(2d,4d,\dots\) produces an infinite descending sequence of ranks.

For four terms, one gets only the disjunction
\[
p(m+d)>p(m+2d)
\quad\text{or}\quad
p(m+2d)>p(m+3d),
\tag{5}
\]
and that disjunction can be satisfied in an order of type \(\omega\).

#### Proposition 5: An \(\omega\)-order satisfying every constraint through its first element

There is a permutation \(p\) with \(p(1)=1\) such that every four-term arithmetic progression containing \(1\) is nonmonotone.

#### Proof

On the positive offsets, impose the precedence relations
\[
3d\triangleleft 2d\qquad(d\ge1).
\tag{6}
\]
Along every relation (6), the \(2\)-adic valuation strictly increases:
\[
v_2(3d)=v_2(d)<v_2(2d)=v_2(d)+1.
\]
Thus there is no directed cycle.

Every \(n\) has only finitely many transitive predecessors. Indeed, if \(n\) is even, its unique immediate predecessor is
\[
\frac{3n}{2},
\]
and iterating gives
\[
\frac{3n}{2},\frac{3^2n}{2^2},\dots,
\frac{3^{v_2(n)}n}{2^{v_2(n)}}.
\]
The chain terminates after \(v_2(n)\) steps.

Construct a linear extension by repeatedly outputting the least unused positive integer whose immediate predecessor, if it has one, has already been output.

This procedure is fair. We prove by induction on \(v_2(n)\) that every \(n\) is eventually output. If \(n\) is odd, it is available from the beginning. While it remains unlisted, the algorithm can choose only available labels below \(n\); there are finitely many, so \(n\) is eventually chosen. If \(n\) is even, its predecessor \(3n/2\) has smaller \(2\)-adic valuation and is eventually output by induction. Thereafter \(n\) is permanently available and again can be delayed by only finitely many smaller labels.

Let \(q(n)\) be the position of offset \(n\) in this linear extension. Then
\[
q(3d)<q(2d)
\tag{7}
\]
for every \(d\).

Now define the permutation sequence by listing \(1\) first and then listing \(1+n\) in the offset order. Thus
\[
p(1)=1,\qquad p(1+n)=1+q(n).
\]
For every \(d\),
\[
p(1+3d)<p(1+2d),
\]
so
\[
p(1),p(1+d),p(1+2d),p(1+3d)
\]
cannot be increasing. It cannot be decreasing because its first rank is \(1\). Since every positive arithmetic progression containing \(1\) starts at \(1\), all such progressions are safe. ∎

This is not a counterexample to the original problem; progressions not containing \(1\) may be monotone. It rigorously shows that the global-minimum argument alone cannot settle length four.

---

### 5. Rank layers forced by the transitive order

For each \(n\), define
\[
I(n)=\max\left\{k:
n_1<\cdots<n_k=n,\ 
p(n_1)<\cdots<p(n_k)\right\},
\]
and
\[
D(n)=\max\left\{k:
n_1<\cdots<n_k=n,\ 
p(n_1)>\cdots>p(n_k)\right\}.
\]

These are the lengths of the longest increasing and decreasing subsequences ending at \(n\).

#### Lemma 6: Rank monotonicity

For \(u<v\):

1. if \(p(u)<p(v)\), then \(I(v)\ge I(u)+1\);
2. if \(p(u)>p(v)\), then \(D(v)\ge D(u)+1\).

Consequently:

- every level set \(\{n:I(n)=r\}\) is decreasing in \(p\);
- every level set \(\{n:D(n)=s\}\) is increasing in \(p\);
- every \(I\)-level is finite.

#### Proof

Append \(v\) to a longest relevant subsequence ending at \(u\), proving the first two statements.

If \(u<v\) and \(I(u)=I(v)\), then \(p(u)<p(v)\) is impossible, so \(p(u)>p(v)\). Thus an increasing numerical enumeration of an \(I\)-level gives a strictly decreasing sequence of positive ranks. Such a sequence is finite.

The \(D\)-level assertion is analogous: equality \(D(u)=D(v)\) excludes \(p(u)>p(v)\), hence forces \(p(u)<p(v)\). ∎

If \(p\) is a counterexample, every \(I\)-level and every \(D\)-level is four-AP-free: a four-AP in an \(I\)-level would be decreasing in \(p\), while one in a \(D\)-level would be increasing.

There is also a useful necessary condition on every four-AP.

#### Corollary 7

In a counterexample, for every four-term progression
\[
n_0<n_1<n_2<n_3,
\]
the sequence
\[
I(n_0),I(n_1),I(n_2),I(n_3)
\]
has an adjacent strict ascent, and the same is true of the \(D\)-sequence.

#### Proof

If \(I(n_{t+1})\le I(n_t)\) for all \(t\), Lemma 6 excludes \(p(n_t)<p(n_{t+1})\) on every edge. Hence all three comparisons are decreasing, a forbidden progression.

The argument for \(D\) is the same with the signs reversed. ∎

The tempting strengthening that one of the two rank sequences must be nonincreasing is false even in the smallest case. For
\[
p(1),p(2),p(3),p(4)=(2,1,4,3),
\]
one obtains
\[
I=(1,1,2,2),\qquad D=(1,2,1,2).
\]
Both have an ascent, while the only four-AP is nonmonotone.

---

### 6. Finite quantitative restrictions on any counterexample

Let \(r_4(N)\) denote the maximum size of a subset of \([N]\) containing no four-term arithmetic progression. Let \(\chi_4(N)\) be the chromatic number of the four-AP hypergraph on \([N]\).

Let
\[
L_N=\max_{n\le N}I(n),\qquad
M_N=\max_{n\le N}D(n).
\]
These are the longest increasing and decreasing subsequence lengths of
\[
p(1),\dots,p(N).
\]

#### Proposition 8

If \(p\) is a counterexample, then
\[
\max\left\{\chi_4(N),\frac{N}{r_4(N)}\right\}
\le L_N,M_N\le r_4(N).
\tag{8}
\]

#### Proof

Any increasing or decreasing subsequence has a four-AP-free label set: a four-AP within its labels would be monotone in \(p\). Thus
\[
L_N,M_N\le r_4(N).
\]

For \(u<v\), either \(I(v)>I(u)\) or \(D(v)>D(u)\), according to the sign of \(p(v)-p(u)\). Hence the pairs
\[
(I(n),D(n)),\qquad n\le N,
\]
are all distinct. There are at most \(L_NM_N\) such pairs, so
\[
N\le L_NM_N.
\]
Combining this with \(L_N,M_N\le r_4(N)\) gives
\[
L_N,M_N\ge \frac{N}{r_4(N)}.
\]

Finally, the \(I\)-levels partition \([N]\) into \(L_N\) four-AP-free sets, and the \(D\)-levels partition it into \(M_N\) four-AP-free sets. Therefore
\[
\chi_4(N)\le L_N,M_N.
\]
This proves (8). ∎

By Szemerédi’s theorem,
\[
r_4(N)=o(N),
\]
so both \(L_N\) and \(M_N\) must tend to infinity. In particular, every counterexample must have arbitrarily long decreasing subsequences, but every such monotone subsequence must have a four-AP-free label set.

Also, each global \(D\)-level has zero upper density: it is four-AP-free, so positive upper density would contradict Szemerédi. Every finite union of \(D\)-levels likewise has zero upper density.

---

### 7. A quadratic comparison-count obstruction

Let
\[
\mathcal A_N=\{(a,d):a+3d\le N\},
\]
and put
\[
A_N=|\mathcal A_N|
=\sum_{d=1}^{\lfloor(N-1)/3\rfloor}(N-3d)
=\frac{N^2}{6}+O(N).
\]

Let \(E_N^-\) be the set of pairs \(u<v\le N\) with \(p(u)>p(v)\), and \(E_N^+\) the set with \(p(u)<p(v)\).

#### Proposition 9

Every finite restriction of a counterexample satisfies
\[
|E_N^-|\ge \frac{A_N}{3},
\qquad
|E_N^+|\ge \frac{A_N}{3}.
\tag{9}
\]
In particular,
\[
|E_N^\pm|\ge \frac{N^2}{18}-O(N).
\]

#### Proof

Every four-AP needs at least one negative consecutive comparison to prevent it from being increasing.

A fixed pair \(u<v\) can occur as a consecutive pair in at most three four-APs, one in each possible slot. The corresponding possible starting points are uniquely determined:
\[
a=u,\qquad a=2u-v,\qquad a=3u-2v.
\]
Some may fail to be positive, but there are never more than three.

Counting incidences between four-APs and negative consecutive pairs gives
\[
A_N\le 3|E_N^-|.
\]
The positive-color bound follows identically because every four-AP needs a positive consecutive comparison to prevent it from being decreasing. ∎

Thus a counterexample would have a positive density of both inversions and noninversions inside every sufficiently large \([N]\), even though each fixed vertex has only finitely many forward inversions.

This is not contradictory. For example, ordering consecutive dyadic blocks in increasing block order but reversing each block gives an order of type \(\omega\) whose inversion density stays bounded away from zero. It has many monotone four-APs inside blocks, so it is not a counterexample, but it refutes any attempted lemma that order type \(\omega\) alone forces inversion density to vanish.

---

### 8. Exact limitation of finite-template Ramsey extraction

The finite-predecessor condition gives the following strong block extraction.

#### Lemma 10: Blockwise forward subsequence

Let \(G_1,G_2,\dots\) be pairwise disjoint, nonempty finite subsets of \(\mathbb N\). For every permutation order \(p\), there are
\[
j_1<j_2<\cdots
\]
such that every element of \(G_{j_r}\) precedes every element of \(G_{j_s}\) whenever \(r<s\).

#### Proof

Choose \(j_1\) arbitrarily. Suppose \(j_1,\dots,j_r\) have been chosen and let
\[
M=\max\{p(v):v\in G_{j_1}\cup\cdots\cup G_{j_r}\}.
\]
Only \(M\) labels have rank at most \(M\). Since the \(G_j\) are disjoint, only finitely many \(G_j\) intersect this set of labels. Choose \(j_{r+1}>j_r\) avoiding all of them. Then every element of \(G_{j_{r+1}}\) has rank greater than \(M\). ∎

However, no fixed family of finite disjoint gadgets can ensure a four-AP transversal after such an extraction.

#### Proposition 11: Finite-gadget obstruction

For every sequence of pairwise disjoint finite sets \(G_1,G_2,\dots\), there is an infinite \(H\subseteq\mathbb N\) such that no four-term arithmetic progression has its four terms in four distinct \(G_i\), \(i\in H\), in either increasing or decreasing index order.

#### Proof

For \(i<j<k<l\), color \(\{i,j,k,l\}\) red if there are \(a,d\ge1\) satisfying either
\[
a\in G_i,\quad a+d\in G_j,\quad
a+2d\in G_k,\quad a+3d\in G_l,
\tag{10}
\]
or the reverse assignment
\[
a+3d\in G_i,\quad a+2d\in G_j,\quad
a+d\in G_k,\quad a\in G_l.
\tag{11}
\]
Otherwise color it blue.

By the infinite Ramsey theorem, there is an infinite homogeneous set \(H\). It cannot be red-homogeneous. Indeed, fix its first two indices \(i<j\). In case (10), a choice
\[
u\in G_i,\qquad v\in G_j
\]
determines \(d=v-u\) and hence uniquely determines the last two terms. Because the \(G_n\) are disjoint, these last two terms determine at most one pair of indices \(k,l\). There are only finitely many choices of \(u,v\).

In case (11), the same argument applies with \(d=u-v\). Thus only finitely many pairs \(k,l\) can form a red quadruple with the fixed \(i,j\), contradicting red homogeneity of an infinite set. Therefore \(H\) is blue-homogeneous. ∎

Combining Propositions 10 and 11 shows that the order-type-\(\omega\) block extraction cannot, by itself, recover an arithmetic progression crossing four distinct finite templates. Progressions using multiple elements of one gadget are not covered, so this is a methodological obstruction rather than a disproof.

---

### 9. Ledger

**Proved**

1. A transitive pair-coloring comes from a permutation exactly when each row has only finitely many backward entries.
2. Every fixed label precedes all sufficiently large numerical labels.
3. Every affine restriction again has order type \(\omega\).
4. The earliest point of each affine ray imposes the disjunction (3).
5. There is an explicit \(\omega\)-order satisfying all four-AP constraints involving its first element.
6. The \(I,D\) rank-layer structure and bounds (8).
7. Quadratic lower bounds (9) for both comparison colors.
8. Finite disjoint templates always admit a blockwise forward subsequence, but also an infinite index set with no monotone four-AP transversal.

**Plausible but unproved**

- The simultaneous translated constraints (4), together with transitivity, may force an infinite descending inversion path or a monotone four-AP. No argument establishing this is known here.
- A useful intermediate theorem would have to exploit overlaps between minima of many affine rays; treating each ray separately is insufficient.

**Dead ends**

1. Infinite Ramsey gives an increasing homogeneous set, but it can be AP-free.
2. The global-minimum DEGS argument dies at the disjunction (5); Proposition 5 is an explicit countermodel to that proof strategy.
3. A rank claim asserting that every four-AP has \(I\) or \(D\) nonincreasing is already false for \(p=(2,1,4,3)\).
4. Quadratic inversion density does not contradict order type \(\omega\).
5. Fixed disjoint finite gadgets cannot preserve enough additive structure under Ramsey/block extraction.

## Self-Audit

1. **The fairness of the topological construction is the most delicate elementary point.**  
   The immediate predecessor of an even \(n\) can be larger than \(n\), so ordinary numerical induction would be invalid. The proof instead inducts on \(v_2(n)\), which strictly decreases on passing to the predecessor \(3n/2\). Once the predecessor is listed, least-available scheduling can delay \(n\) by only finitely many labels below it.

2. **The finite subsequence bounds use global ranks although only labels in \([N]\) are counted.**  
   This is valid because \(I(n)\) and \(D(n)\) only use earlier numerical labels, all of which also lie in \([N]\) when \(n\le N\). The injection \(n\mapsto(I(n),D(n))\) therefore applies directly to the finite sequence \(p(1),\dots,p(N)\).

3. **The finite-gadget obstruction has a deliberately limited scope.**  
   It excludes progressions using four distinct gadgets in monotone gadget order, but says nothing about progressions with two or more terms in one gadget or about overlapping/infinite templates. The proof of the stated scope is sound: fixing the first two gadget indices leaves only finitely many possible completions, which rules out an infinite red Ramsey clique.

## Computations To Verify

```python
from itertools import permutations

def violations(word):
    """
    word is a finite list of distinct positive integers in arrival order.
    Returns all monotone 4-APs wholly contained in word.
    """
    pos = {v: i for i, v in enumerate(word, start=1)}
    vals = set(word)
    M = max(word)
    bad = []

    for d in range(1, (M - 1) // 3 + 1):
        for a in range(1, M - 3*d + 1):
            ap = (a, a+d, a+2*d, a+3*d)
            if all(v in vals for v in ap):
                ranks = tuple(pos[v] for v in ap)
                inc = all(ranks[i] < ranks[i+1] for i in range(3))
                dec = all(ranks[i] > ranks[i+1] for i in range(3))
                if inc or dec:
                    bad.append((a, d, ranks))
    return bad


def topo_offsets(K):
    """
    First K offsets in the least-available topological order for
    the relations 3d before 2d.
    """
    used = set()
    out = []

    while len(out) < K:
        n = 1
        while True:
            if n not in used:
                available = (n % 2 == 1) or ((3*n)//2 in used)
                if available:
                    break
            n += 1
        used.add(n)
        out.append(n)

    return out


def verify_anchor_construction(K=1000):
    offsets = topo_offsets(K)
    q = {n: i for i, n in enumerate(offsets, start=1)}

    # Whenever 2d has appeared, its required predecessor 3d appeared earlier.
    for d in range(1, max(offsets) + 1):
        if 2*d in q:
            assert 3*d in q
            assert q[3*d] < q[2*d]

    word = [1] + [1+n for n in offsets]
    bad = violations(word)

    # No complete violating AP in this prefix may start at 1.
    assert all(a != 1 for a, d, ranks in bad)
    return word[:30], bad[:10]


def rank_layers_from_positions(p):
    """
    p is a 1-indexed list: p[n] is the rank of label n.
    """
    N = len(p) - 1
    I = [0] * (N + 1)
    D = [0] * (N + 1)

    for n in range(1, N + 1):
        I[n] = 1 + max(
            (I[u] for u in range(1, n) if p[u] < p[n]),
            default=0
        )
        D[n] = 1 + max(
            (D[u] for u in range(1, n) if p[u] > p[n]),
            default=0
        )

    for u in range(1, N + 1):
        for v in range(u + 1, N + 1):
            if p[u] < p[v]:
                assert I[v] >= I[u] + 1
            else:
                assert D[v] >= D[u] + 1

    pairs = {(I[n], D[n]) for n in range(1, N + 1)}
    assert len(pairs) == N
    assert N <= max(I) * max(D)
    return I[1:], D[1:]


def positions_of_full_word(word):
    N = len(word)
    assert set(word) == set(range(1, N+1))
    p = [0] * (N + 1)
    for rank, label in enumerate(word, start=1):
        p[label] = rank
    return p


def avoids_full_word(word):
    return len(violations(word)) == 0


def verify_small_rank_dead_end():
    word = [2, 1, 4, 3]
    assert avoids_full_word(word)
    p = positions_of_full_word(word)
    I, D = rank_layers_from_positions(p)
    assert I == [1, 1, 2, 2]
    assert D == [1, 2, 1, 2]

    # Neither sequence is nonincreasing on the sole 4-AP.
    assert not all(I[t] >= I[t+1] for t in range(3))
    assert not all(D[t] >= D[t+1] for t in range(3))


def comparison_counts(word):
    """
    For a full order of [N], count positive and negative pair colors
    and verify Proposition 9 if the order avoids.
    """
    N = len(word)
    p = positions_of_full_word(word)

    neg = 0
    pos = 0
    for u in range(1, N+1):
        for v in range(u+1, N+1):
            if p[u] > p[v]:
                neg += 1
            else:
                pos += 1

    A = sum(N - 3*d for d in range(1, (N-1)//3 + 1))

    if avoids_full_word(word):
        assert 3*neg >= A
        assert 3*pos >= A

    return A, pos, neg


def enumerate_small_avoiders(max_N=9):
    """
    Exhaustive only for small N. Prints the number of avoiding orders
    and checks the comparison-count bound.
    """
    for N in range(1, max_N + 1):
        count = 0
        for word in permutations(range(1, N+1)):
            if avoids_full_word(word):
                count += 1
                comparison_counts(word)
        print(N, count)


if __name__ == "__main__":
    print(verify_anchor_construction(1000))
    verify_small_rank_dead_end()
    # enumerate_small_avoiders(9)
```

Useful larger finite experiments should additionally record, for SAT-generated avoiders:

1. the forward inversion degree
   \[
   \deg^-(u)=|\{v>u:p(v)<p(u)\}|;
   \]
2. the \(I,D\) layer sizes;
3. the earliest point of each tested affine ray;
4. which side of disjunction (3) witnesses each anchored constraint;
5. whether repeated translated constraints generate long directed inversion paths.

## Route Diagnosis

The exact order-type-\(\omega\) contribution is now isolated: every row of the transitive coloring is eventually \(+\). This gives strong endpoint constraints, but each individual endpoint system is satisfiable by an \(\omega\)-order, as Proposition 5 demonstrates. Ramsey theory extracts forward homogeneous sets only by allowing arbitrary sparsity, and Proposition 11 shows that fixed finite templates cannot prevent this additive sparsification.

The block is therefore precise: one needs a theorem using the **simultaneous overlap** of the eventual clauses
\[
p(b+d)>p(b+2d)\quad\text{or}\quad p(b+2d)>p(b+3d)
\]
for every \(b\) and all sufficiently large \(d\), together with transitivity. Proving merely that no transitive eventually-forward coloring can satisfy the mixed-sign condition on every four-AP would simply restate the original problem.

A fresh attempt should concentrate on one of the following:

1. Analyze the joint \(I,D\) rank layers and seek an additive theorem stronger than the false “one rank sequence is nonincreasing” claim.
2. Search computationally for incompatible finite collections of **overlapping affine-ray minima**, rather than arbitrary finite orders.
3. Recover the DEGS three-term proof in a recursive affine-restriction form and determine whether minima of several intersecting rays force compatible orientations.
4. In SAT-generated avoiders, inspect whether the clauses (3) create a recurring well-founded orientation rule analogous to \(3d\prec2d\); a stable rule could suggest a counterexample construction, while certified failure of every finite-state rule could guide an affirmative proof.