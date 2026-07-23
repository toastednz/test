STATUS: SOLVED-DISPROOF

## Result

Under standard non-induced subgraph containment, the assertion is false: \(\mathcal F=\{P_3,2K_2\}\) has \(\operatorname{ex}(n;\mathcal F)=1\) for \(n\ge2\), while both singleton extremal numbers grow linearly. Pursuing Route 2 yields a complete classification: for a finite family of edge-containing graphs, \(\operatorname{ex}(n;\mathcal F)=O(1)\) exactly when \(\mathcal F\) contains a graph whose nonisolated part is a star and another whose nonisolated part is a matching. In fact, the joint extremal number then eventually stabilizes; otherwise it is at least \(\lfloor n/2\rfloor\). Among bounded families, the original assertion holds exactly in the trivial case where some member has one edge; every other bounded family is a counterexample. I also prove two further reductions for the repaired unbounded problem: a forest member controls every unbounded family containing it, while an all-cyclic family has a polynomially superlinear joint extremal number, and disconnected forbidden graphs admit an additive \(O_{\mathcal F}(n)\) component-packing reduction.

## Complete Argument

Throughout, \(\mathcal F\) is finite and nonempty, and every \(H\in\mathcal F\) has at least one edge.

### 1. Removing isolated vertices

For a graph \(H\), let \(H^+\) be obtained by deleting all isolated vertices.

**Lemma 1.** If \(X\) has \(n\ge v(H)\) vertices, then
\[
H\subseteq X\quad\Longleftrightarrow\quad H^+\subseteq X.
\]

**Proof.** The forward implication is immediate. Conversely, suppose a copy of \(H^+\) uses \(v(H^+)\) vertices of \(X\). If \(H\) has \(q=v(H)-v(H^+)\) isolated vertices, then
\[
n-v(H^+)\ge q.
\]
Map those isolated vertices injectively to any \(q\) unused vertices of \(X\). Since containment is not induced, no nonedge conditions need to be checked. ∎

Consequently, if
\[
N=\max_{H\in\mathcal F}v(H),
\]
then for every \(n\ge N\),
\[
\operatorname{ex}(n;\mathcal F)=\operatorname{ex}(n;\mathcal F^+),
\qquad
\mathcal F^+=\{H^+:H\in\mathcal F\}.
\]

### 2. Which graphs can occur in stars and matchings?

Call \(H\) **star-supported** if all its edges have a common endpoint. Equivalently,
\[
H^+\cong K_{1,a}
\]
for some \(a\ge1\).

Call \(H\) **matching-supported** if \(\Delta(H^+)\le1\). Equivalently,
\[
H^+\cong bK_2
\]
for some \(b\ge1\).

**Lemma 2.**

1. A graph \(H\) embeds into some star if and only if it is star-supported.
2. A graph \(H\) embeds into some matching if and only if it is matching-supported.

**Proof.**

For the first assertion, suppose \(H\) embeds into \(K_{1,m}\), whose center is \(c\). Every target edge contains \(c\). Since the embedding is injective and \(H\) has an edge, exactly one vertex \(w\in V(H)\) maps to \(c\), and every edge of \(H\) must contain \(w\). Thus \(H\) is star-supported.

Conversely, if all edges of \(H\) contain one vertex \(w\), map \(w\) to the center of a sufficiently large star, map the other nonisolated vertices to distinct leaves, and map all isolated vertices to unused leaves.

For the second assertion, if \(H\) embeds into a matching, no vertex of \(H\) can have degree at least two, because the image of such a vertex would be incident with two distinct target edges. Thus \(H^+\) is a matching.

Conversely, if \(H^+\cong bK_2\), map its \(b\) edges to \(b\) distinct matching edges and map the isolated vertices to unused vertices of a sufficiently large matching. ∎

### 3. Complete classification of bounded joint extremal numbers

**Theorem 3.** The following are equivalent:

1. \(\operatorname{ex}(n;\mathcal F)=O_{\mathcal F}(1)\).
2. The family \(\mathcal F\) contains both:
   - a star-supported member \(H_s\), and
   - a matching-supported member \(H_m\).
3. \(\operatorname{ex}(n;\mathcal F)\) is eventually constant.

Moreover, if
\[
H_s^+\cong K_{1,a},
\qquad
H_m^+\cong bK_2,
\]
then for all sufficiently large \(n\),
\[
\operatorname{ex}(n;\mathcal F)
\le 2(a-1)(b-1).
\]
If condition 2 fails, then for every \(n\),
\[
\operatorname{ex}(n;\mathcal F)\ge \left\lfloor\frac n2\right\rfloor.
\]

**Proof.**

#### Necessity

Suppose there are \(C,n_0\) such that
\[
\operatorname{ex}(n;\mathcal F)\le C
\qquad(n\ge n_0).
\]

Choose \(m>C\) with \(m+1\ge n_0\). The star \(K_{1,m}\) has \(m>C\) edges, so it cannot be \(\mathcal F\)-free. Hence some \(H_s\in\mathcal F\) embeds into this star. By Lemma 2, \(H_s\) is star-supported.

Likewise choose \(m>C\) with \(2m\ge n_0\). The matching \(mK_2\) has \(m>C\) edges, so some \(H_m\in\mathcal F\) embeds into it. By Lemma 2, \(H_m\) is matching-supported.

#### Sufficiency

Suppose
\[
H_s^+\cong K_{1,a},
\qquad
H_m^+\cong bK_2.
\]
Let \(X\) be an \(n\)-vertex \(\mathcal F\)-free graph with
\[
n\ge \max\{v(H_s),v(H_m)\}.
\]

By Lemma 1, \(X\) contains neither \(K_{1,a}\) nor \(bK_2\). Therefore
\[
\Delta(X)\le a-1,
\qquad
\nu(X)\le b-1.
\]

Let \(M\) be a maximal matching of \(X\), and let \(S\) be the set of endpoints of its edges. Then
\[
|S|=2|M|\le2(b-1).
\]
The set \(S\) is a vertex cover: otherwise an edge with both endpoints outside \(S\) could be added to \(M\), contradicting maximality. Hence
\[
e(X)\le\sum_{v\in S}d(v)
\le |S|\Delta(X)
\le2(b-1)(a-1).
\]

This proves boundedness.

#### The linear alternative

If \(\mathcal F\) contains no star-supported member, then by Lemma 2 no member of \(\mathcal F\) embeds into \(K_{1,n-1}\). Thus
\[
\operatorname{ex}(n;\mathcal F)\ge n-1.
\]

If \(\mathcal F\) contains no matching-supported member, then the \(n\)-vertex matching with \(\lfloor n/2\rfloor\) edges is \(\mathcal F\)-free. Thus
\[
\operatorname{ex}(n;\mathcal F)\ge\left\lfloor\frac n2\right\rfloor.
\]

If condition 2 fails, at least one of these alternatives applies, proving the claimed lower bound.

#### Eventual stabilization

Assume condition 2 and let
\[
B=2(a-1)(b-1).
\]
Every finite \(\mathcal F^+\)-free graph has at most \(B\) edges by the preceding degree-matching argument.

Define
\[
c_{\mathcal F}
=
\max\{e(X):X\text{ is a finite }\mathcal F^+\text{-free graph}\}.
\]
This maximum exists because the possible edge counts lie in the finite set
\(\{0,1,\dots,B\}\).

Choose a graph attaining \(c_{\mathcal F}\) and remove its isolated vertices. Its resulting core has at most \(2c_{\mathcal F}\le2B\) vertices. For any sufficiently large \(n\), pad this core with isolated vertices. The resulting graph remains \(\mathcal F^+\)-free, and hence, by Lemma 1, is \(\mathcal F\)-free. Therefore
\[
\operatorname{ex}(n;\mathcal F)=c_{\mathcal F}
\]
for all sufficiently large \(n\). This proves eventual constancy. The converse is immediate. ∎

Thus a finite family never has an unbounded but sublinear joint extremal number: it is either eventually constant or at least linear.

### 4. Exactly which bounded families violate the original assertion?

**Corollary 4.** Suppose \(\operatorname{ex}(n;\mathcal F)=O(1)\).

- If some \(H\in\mathcal F\) has exactly one edge, then \(H\) controls \(\mathcal F\).
- If every member of \(\mathcal F\) has at least two edges, then no member controls \(\mathcal F\).

**Proof.**

If \(H\) consists of one edge and \(q\) isolated vertices, then for every \(n\ge q+2\), every \(n\)-vertex graph containing an edge contains \(H\): use that edge and any \(q\) other vertices. Hence
\[
\operatorname{ex}(n;H)=0.
\]
Since \(H\in\mathcal F\), also
\[
\operatorname{ex}(n;\mathcal F)=0
\]
for those \(n\). Thus \(H\) controls the family.

Now suppose every \(H\in\mathcal F\) has at least two edges. For each such \(H\), either:

1. \(H\) has two adjacent edges, in which case every matching avoids \(H\), so
   \[
   \operatorname{ex}(n;H)\ge\left\lfloor\frac n2\right\rfloor;
   \]
2. or all edges of \(H\) are pairwise disjoint, in which case every star avoids \(H\), so
   \[
   \operatorname{ex}(n;H)\ge n-1.
   \]

Thus in every case
\[
\operatorname{ex}(n;H)\ge\left\lfloor\frac n2\right\rfloor.
\]
The joint extremal number is bounded above, and it is at least one for \(n\ge2\), because a one-edge graph avoids every member of \(\mathcal F\). Hence
\[
\frac{\operatorname{ex}(n;H)}
     {\operatorname{ex}(n;\mathcal F)}
\longrightarrow\infty
\]
for every \(H\in\mathcal F\). ∎

This completely identifies the bounded obstruction to the original assertion.

### 5. Explicit disproof

Take
\[
\mathcal F=\{P_3,2K_2\}.
\]

A graph is \(P_3\)-free if and only if it has maximum degree at most one: two edges incident with one vertex form a non-induced \(P_3\). Hence every \(P_3\)-free graph is a matching together with isolated vertices. If it is also \(2K_2\)-free, it has at most one edge. Conversely, a one-edge graph avoids both forbidden graphs. Therefore
\[
\operatorname{ex}(n;\{P_3,2K_2\})=1
\qquad(n\ge2).
\]

The same characterization gives
\[
\operatorname{ex}(n;P_3)=\left\lfloor\frac n2\right\rfloor.
\]

For \(2K_2\), being free means every two edges intersect. If all edges share one vertex, there are at most \(n-1\) edges. Otherwise choose two edges \(ab,ac\), and then an edge not containing \(a\). It must intersect both \(ab\) and \(ac\), so it is \(bc\). Any edge intersecting all three of \(ab,ac,bc\) must itself be one of these three edges. Thus the graph is contained in a triangle and has at most three edges. Therefore
\[
\operatorname{ex}(n;2K_2)=\max\{n-1,3\}=n-1
\qquad(n\ge4),
\]
with equality furnished by a star.

Consequently, for \(n\ge4\),
\[
\frac{\operatorname{ex}(n;P_3)}
     {\operatorname{ex}(n;\mathcal F)}
=
\left\lfloor\frac n2\right\rfloor\to\infty,
\]
and
\[
\frac{\operatorname{ex}(n;2K_2)}
     {\operatorname{ex}(n;\mathcal F)}
=n-1\to\infty.
\]
No member of \(\mathcal F\) controls the family, disproving the universal assertion.

### 6. Consequences for the repaired unbounded problem

The classification gives a useful positive case.

**Proposition 5.** If \(\operatorname{ex}(n;\mathcal F)\) is unbounded and some \(H\in\mathcal F\) is a forest, then
\[
\operatorname{ex}(n;\mathcal F)=\Theta_{\mathcal F}(n)
\]
and \(H\) controls \(\mathcal F\).

**Proof.** By Theorem 3,
\[
\operatorname{ex}(n;\mathcal F)\ge\left\lfloor\frac n2\right\rfloor.
\]

Let \(h=v(H)\). Any graph with more than \((h-2)n\) edges has a nonempty subgraph of minimum degree at least \(h-1\): repeatedly delete vertices of degree at most \(h-2\); if every vertex were deleted, at most \((h-2)n\) edges would have been removed.

Every graph of minimum degree at least \(h-1\) contains every \(h\)-vertex forest. To see this, order the vertices of each tree component starting with a root and with each nonroot appearing after its parent. Map roots to arbitrary unused vertices. When mapping a nonroot, its parent has at least \(h-1\) neighbors and at most \(h-2\) of them have already been used, so an unused neighbor is available.

Thus
\[
\operatorname{ex}(n;H)\le(h-2)n.
\]
Combining this with the linear lower bound for the joint extremal number proves the result. ∎

There is also a growth gap in the remaining case.

**Proposition 6.** If every \(H\in\mathcal F\) contains a cycle and
\[
L=\max_{H\in\mathcal F}v(H),
\]
then for some \(c_L>0\),
\[
\operatorname{ex}(n;\mathcal F)\ge c_Ln^{1+1/L}
\]
for all sufficiently large \(n\).

**Proof.** Take \(G\sim G(n,p)\) with
\[
p=n^{-1+1/L}.
\]
Then
\[
\mathbb E e(G)=\binom n2p=\Theta(n^{1+1/L}).
\]
For \(3\le k\le L\), the expected number of \(k\)-cycles is at most
\[
\frac{n^kp^k}{2k}
=\frac{n^{k/L}}{2k}.
\]
Thus the expected total number \(Z\) of cycles of lengths at most \(L\) is \(O_L(n)\). For sufficiently large \(n\),
\[
\mathbb E(e(G)-Z)\ge c_Ln^{1+1/L}.
\]
Choose a realization satisfying this inequality and delete one edge from every remaining cycle of length at most \(L\). At most \(Z\) edges are deleted. The resulting graph has girth greater than \(L\), at least \(c_Ln^{1+1/L}\) edges, and contains no member of \(\mathcal F\), since every such member contains a cycle of length at most \(L\). ∎

Hence the repaired problem splits into:

- bounded families, now completely classified;
- unbounded families containing a forest, where the assertion is true;
- families all of whose members contain cycles, where the joint extremal number is already polynomially superlinear.

### 7. Additive component-packing reduction

For each \(H\in\mathcal F\), let
\[
H^+=C_{H,1}\sqcup\cdots\sqcup C_{H,k_H}
\]
be its decomposition into nonisolated connected components. For a choice function
\[
\sigma(H)\in\{1,\dots,k_H\},
\]
put
\[
\mathcal C_\sigma
=
\{C_{H,\sigma(H)}:H\in\mathcal F\}.
\]

**Proposition 7.** Let
\[
s=\sum_{H\in\mathcal F}v(H^+).
\]
For all sufficiently large \(n\),
\[
\max_\sigma\operatorname{ex}(n;\mathcal C_\sigma)
\le
\operatorname{ex}(n;\mathcal F)
\le
\max_\sigma\operatorname{ex}(n;\mathcal C_\sigma)+sn.
\]

**Proof.** If a graph avoids one selected component of each \(H\), then it avoids every \(H^+\), and therefore, for sufficiently large \(n\), every \(H\). This proves the lower bound.

For the upper bound, let \(X\) be \(\mathcal F\)-free. For each fixed \(H\), greedily seek mutually vertex-disjoint copies of
\[
C_{H,1},C_{H,2},\dots,C_{H,k_H}
\]
in that order. The procedure must fail at some component, since otherwise their disjoint union would give a copy of \(H^+\). Let \(S_H\) be the vertices used before the failure, and let \(C_{H,\sigma(H)}\) be the component at which it fails. Then
\[
X-S_H
\]
is \(C_{H,\sigma(H)}\)-free.

Let
\[
S=\bigcup_{H\in\mathcal F}S_H.
\]
Then \(|S|\le s\), and \(X-S\) is \(\mathcal C_\sigma\)-free. Every selected component has an edge, so padding with isolated vertices preserves avoidance. Therefore
\[
e(X-S)\le\operatorname{ex}(n;\mathcal C_\sigma).
\]
At most \(|S|n\le sn\) edges are incident with \(S\), giving
\[
e(X)\le\operatorname{ex}(n;\mathcal C_\sigma)+sn.
\]
Maximizing over \(\sigma\) proves the result. ∎

For an all-cyclic family, Proposition 6 makes the additive \(O_{\mathcal F}(n)\) term negligible:
\[
\operatorname{ex}(n;\mathcal F)
=
\left(1+o(1)\right)
\max_\sigma\operatorname{ex}(n;\mathcal C_\sigma).
\]
This does not by itself select an original member \(H\in\mathcal F\), so it does not solve the repaired conjecture.

## Self-Audit

1. **The classification assumes every forbidden graph has an edge.** If edgeless forbidden graphs are admitted, the admissible class can be empty and \(\operatorname{ex}\) becomes convention-dependent. This is not a gap under the problem’s stated standard convention, which excludes that case.

2. **Deleting isolated vertices is valid only after the host has enough vertices.** I used it only for \(n\ge\max_{H\in\mathcal F}v(H)\). Lemma 1 explicitly supplies the necessary unused vertices, so no small-\(n\) assertion is being smuggled into an asymptotic conclusion.

3. **The component-packing reduction gives only an additive \(O(n)\) comparison and does not identify a controlling original member.** The displayed inequalities themselves are fully proved, but using them to solve the repaired problem would require a new selection argument. I therefore do not claim that this reduction settles the unbounded cyclic case.

## Computations To Verify

The minimal counterexample can be checked exhaustively as follows.

```python
from itertools import combinations

def all_edge_sets(n):
    pairs = list(combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        yield {pairs[i] for i in range(len(pairs)) if (mask >> i) & 1}

def p3_free(n, E):
    deg = [0] * n
    for u, v in E:
        deg[u] += 1
        deg[v] += 1
    return max(deg, default=0) <= 1

def twoK2_free(E):
    return not any(set(e).isdisjoint(f) for e, f in combinations(E, 2))

for n in range(1, 8):
    ex_joint = ex_p3 = ex_2k2 = 0
    for E in all_edge_sets(n):
        m = len(E)
        pfree = p3_free(n, E)
        mfree = twoK2_free(E)
        if pfree:
            ex_p3 = max(ex_p3, m)
        if mfree:
            ex_2k2 = max(ex_2k2, m)
        if pfree and mfree:
            ex_joint = max(ex_joint, m)
    print(n, ex_joint, ex_p3, ex_2k2)
```

Expected output:

```text
1 0 0 0
2 1 1 1
3 1 1 3
4 1 2 3
5 1 2 4
6 1 3 5
7 1 3 6
```

The structural lemmas, including isolated vertices, can be tested by brute-force non-induced embeddings.

```python
from itertools import combinations, permutations

def contains(H, X):
    # H=(h, edge_set), X=(n, edge_set)
    h, HE = H
    n, XE = X
    if h > n:
        return False
    XE = {tuple(sorted(e)) for e in XE}
    for image in permutations(range(n), h):
        if all(tuple(sorted((image[u], image[v]))) in XE for u, v in HE):
            return True
    return False

def Hplus(H):
    h, E = H
    used = sorted({v for e in E for v in e})
    relabel = {v: i for i, v in enumerate(used)}
    return (
        len(used),
        {tuple(sorted((relabel[u], relabel[v]))) for u, v in E}
    )

def star_supported(H):
    _, E = H
    common = set(next(iter(E)))
    for e in E:
        common &= set(e)
    return bool(common)

def matching_supported(H):
    h, E = H
    deg = [0] * h
    for u, v in E:
        deg[u] += 1
        deg[v] += 1
    return max(deg, default=0) <= 1

# Test Lemma 2 for every labeled graph on at most five vertices.
for h in range(2, 6):
    for E in all_edge_sets(h):
        if not E:
            continue
        H = (h, E)
        star = (h, {(0, i) for i in range(1, h)})
        matching = (h, {(2*i, 2*i+1) for i in range(h // 2)})
        assert star_supported(H) == contains(H, star)
        assert matching_supported(H) == contains(H, matching)

# Test isolated-vertex removal for h <= 4 and hosts up to five vertices.
for h in range(2, 5):
    for HE in all_edge_sets(h):
        if not HE:
            continue
        H = (h, HE)
        Hp = Hplus(H)
        for n in range(h, 6):
            for XE in all_edge_sets(n):
                X = (n, XE)
                assert contains(H, X) == contains(Hp, X)
```

For the component-packing inequality, a finite check can use:

```python
# Pseudocode:
for each small family F:
    replace every H by Hplus(H)
    compute all connected components of every H
    for each choice sigma of one component from every H:
        compute exact_ex(n, C_sigma)
    M = max_sigma exact_ex(n, C_sigma)
    E = exact_ex(n, F)
    s = sum(number_of_vertices(Hplus(H)) for H in F)
    assert M <= E <= M + s*n
```

## Route Diagnosis

**Proved ledger:** isolated vertices are asymptotically removable; star and matching embeddings are exactly characterized; all bounded joint extremal numbers are classified; bounded extremal numbers eventually stabilize; failure of the bounded criterion gives a uniform linear lower bound; bounded families without a one-edge member are precisely the bounded counterexamples; unbounded families with a forest member satisfy the repaired assertion; all-cyclic families have polynomially superlinear joint extremal number; and disconnected forbidden graphs reduce to connected-component choice families up to an additive \(O_{\mathcal F}(n)\).

**Blocked ledger:** the natural repaired conjecture remains unresolved for finite families in which every member contains a cycle, especially cyclic bipartite families. Route 2 cannot compare their singleton sparse Turán numbers with the simultaneous extremal number. Proposition 7 also does not bridge this gap: controlling one selected component need not control the largest component, and hence need not control the original disconnected graph.

**Dead ends:** bounded-obstruction removal alone cannot imply a constant-retention theorem; an \(O(n)\) deletion argument is useful only after the superlinear reduction and still does not choose a fixed original member. A fresh attempt should focus on all-cyclic bipartite families, either through balanced supersaturation/copy-hypergraph retention or by constructing an unbounded counterexample with incompatible sparse extremal geometries. For the literal problem, however, no block remains: it is completely disproved.