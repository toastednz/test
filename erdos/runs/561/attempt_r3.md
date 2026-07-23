STATUS: BLOCKED

## Result

Route 3 yields an exact Boolean/blocker reformulation and two rigorous lower-bound mechanisms, but not the conjectured general bound. I prove that arrowing is equivalent to cross-intersection of the two blocker families, derive the universal bound
\[
|E(H)|\ge N+M-1+\max\{\delta(F_1,F_2),\delta(F_2,F_1)\},
\]
where \(N=|E(F_1)|\), \(M=|E(F_2)|\), and \(\delta\) is an explicitly computable maximum-common-subgraph deficiency. I also give a complete Boolean-threshold characterization for hosts that are disjoint unions of stars, recovering exactly the antidiagonal sum \(L\) in that class. The route blocks because generic Boolean-cube or blocker inequalities see only \(N+M-1\), while obtaining the remaining antidiagonal terms requires a new graph-specific inequality coupling several residual copy families simultaneously. Even the elementary settled case \(2K_{1,2}\) versus \(2K_{1,2}\) exposes this gap: the blocker bound gives only \(7\), whereas \(L=9\).

## Complete Argument

### 1. Boolean-cube and blocker reformulation

Let \(H\) be a fixed host graph with edge set \(E\). Let

\[
\mathcal A=\{E(A):A\subseteq H,\ A\cong F_1\},
\qquad
\mathcal B=\{E(B):B\subseteq H,\ B\cong F_2\}.
\]

A transversal of a family \(\mathcal C\subseteq 2^E\) is a set meeting every member of \(\mathcal C\). Let \(\operatorname{Tr}(\mathcal C)\) denote all its transversals and \(b(\mathcal C)\) its inclusion-minimal transversals.

#### Proposition 1: Exact blocker duality

The following are equivalent.

1. \(H\to(F_1,F_2)\).
2. There are no disjoint sets
   \[
   R\in\operatorname{Tr}(\mathcal B),
   \qquad
   D\in\operatorname{Tr}(\mathcal A).
   \]
3. Every transversal \(R\) of \(\mathcal B\) contains a member of \(\mathcal A\).
4. The blocker families \(b(\mathcal A)\) and \(b(\mathcal B)\) are cross-intersecting:
   \[
   X\cap Y\ne\varnothing
   \quad
   \text{for all }X\in b(\mathcal A),\ Y\in b(\mathcal B).
   \]

#### Proof

A coloring with red edge set \(R\) and blue edge set \(D=E\setminus R\) contains no red \(F_1\) exactly when \(D\) meets every copy of \(F_1\), i.e. \(D\in\operatorname{Tr}(\mathcal A)\). It contains no blue \(F_2\) exactly when \(R\in\operatorname{Tr}(\mathcal B)\).

Thus an avoiding coloring produces disjoint transversals \(R,D\).

Conversely, suppose \(R_0\in\operatorname{Tr}(\mathcal B)\) and \(D_0\in\operatorname{Tr}(\mathcal A)\) are disjoint. Color every edge of \(D_0\) blue and every other edge red. The red edge set \(E\setminus D_0\) contains \(R_0\), so it remains a transversal of \(\mathcal B\); hence there is no blue \(F_2\). The blue set \(D_0\) meets every copy of \(F_1\), so there is no red \(F_1\). This proves the equivalence of 1 and 2.

If \(R\in\operatorname{Tr}(\mathcal B)\) contains no member of \(\mathcal A\), color \(R\) red and its complement blue. Then there is neither a red \(F_1\) nor a blue \(F_2\). Conversely, an avoiding coloring has precisely such a red set. This proves the equivalence with 3.

Every transversal of a finite hypergraph contains an inclusion-minimal transversal. Hence disjoint transversals exist if and only if disjoint inclusion-minimal transversals exist, proving the equivalence with 4. ∎

This is the exact Route 3 formulation: the desired lower bound says that the blocker families of graph-realizable star-forest copy hypergraphs cannot be cross-intersecting on fewer than \(L\) ground elements.

---

### 2. The cardinality-only Boolean bound

Write
\[
N=\sum_{i=1}^s n_i,
\qquad
M=\sum_{j=1}^t m_j.
\]

#### Proposition 2

Every arrowing host satisfies
\[
|E(H)|\ge N+M-1.
\]

#### Proof

Suppose \(q=|E(H)|\le N+M-2\). Choose an integer \(r\) satisfying
\[
q-(M-1)\le r\le N-1
\]
and \(0\le r\le q\). Such an \(r\) exists because \(q\le N+M-2\).

Color exactly \(r\) edges red and the other \(q-r\) edges blue. There are fewer than \(N\) red edges, so the red graph cannot contain \(F_1\), which has \(N\) edges. There are fewer than \(M\) blue edges, so the blue graph cannot contain \(F_2\). Therefore \(H\) does not arrow \((F_1,F_2)\). ∎

No argument using only the uniformities \(N\) and \(M\) can generally improve this. Indeed, on a ground set of \(N+M-1\) elements, let \(\mathcal A\) be all \(N\)-subsets and \(\mathcal B\) all \(M\)-subsets. Every set \(R\) either has \(|R|\ge N\), or its complement has at least \(M\) elements. Thus these abstract hypergraphs cover the Boolean cube with only \(N+M-1\) elements.

For example, for
\[
F_1=F_2=2K_{1,2}
\]
one has \(N=M=4\), while
\[
L=3(2+2-1)=9.
\]
The abstract complete-uniform construction covers the cube on \(7\) elements. Therefore a proof of \(L=9\) must use graph-realizability and cannot follow from clause sizes, monotonicity, LYM alone, or generic blocker duality.

---

### 3. A minimum-transversal exchange lemma

For two graphs \(Q,X\), define
\[
\rho(Q,X)
=
\max\{|E(J)|:J\text{ is isomorphic to an edge-subgraph of both }Q\text{ and }X\}.
\]

Thus \(\rho(Q,X)\) is the maximum number of edges of \(Q\) that can simultaneously be realized inside \(X\). In particular,
\[
Q\subseteq X\quad\Longleftrightarrow\quad \rho(Q,X)=|E(Q)|.
\]

Define
\[
\delta(P,Q)
=
\max_{\substack{X\subseteq P\\X\text{ an edge-subgraph}\\Q\nsubseteq X}}
\bigl(|E(X)|-\rho(Q,X)\bigr).
\]
The empty subgraph is allowed, so \(\delta(P,Q)\ge0\).

#### Proposition 3: Residual-hypergraph exchange

Let \(T\) be a minimum-cardinality transversal of \(\mathcal B\), and put \(O=E(H)\setminus T\). Suppose \(A\subseteq H[T]\) is a copy of \(F_1\). Let \(X\) be an edge-subgraph of \(A\) containing no copy of \(F_2\). Then
\[
|O|
\ge
|E(X)|+M-\rho(F_2,X)-1.
\]

#### Proof

Define a hypergraph on ground set \(O\) by
\[
\mathcal C_X
=
\left\{
E(B)\setminus T:
B\cong F_2,\ 
\varnothing\ne E(B)\cap T\subseteq E(X)
\right\}.
\]

First, every member of \(\mathcal C_X\) is nonempty. Otherwise some copy \(B\cong F_2\) would satisfy
\[
E(B)\subseteq E(X),
\]
contrary to the assumption that \(X\) is \(F_2\)-free.

We claim
\[
\tau(\mathcal C_X)\ge |E(X)|,
\]
where \(\tau\) denotes transversal number. Suppose instead that \(Y\subseteq O\) meets every member of \(\mathcal C_X\) and
\[
|Y|<|E(X)|.
\]
Set
\[
T'=(T\setminus E(X))\cup Y.
\]
Then \(|T'|<|T|\). We show that \(T'\) still meets every copy \(B\) of \(F_2\).

If \(E(B)\cap(T\setminus E(X))\ne\varnothing\), this is immediate. Otherwise, because \(T\) is a transversal,
\[
\varnothing\ne E(B)\cap T\subseteq E(X).
\]
Consequently \(E(B)\setminus T\in\mathcal C_X\), and this residual set meets \(Y\). Hence \(B\) also meets \(T'\). This contradicts the minimum cardinality of \(T\).

Now take any \(C=E(B)\setminus T\in\mathcal C_X\). The graph formed by \(E(B)\cap T\) is an edge-subgraph of both \(F_2\) and \(X\). Therefore
\[
|E(B)\cap T|\le \rho(F_2,X),
\]
and hence
\[
|C|
=
M-|E(B)\cap T|
\ge M-\rho(F_2,X).
\]
Put
\[
d=M-\rho(F_2,X)\ge1.
\]

For any hypergraph on a \(u\)-element ground set whose members all have size at least \(d\), its transversal number is at most \(u-d+1\): choose any \(d-1\) ground elements and take their complement; every hyperedge meets that complement. Applying this to \(\mathcal C_X\) gives
\[
|E(X)|
\le\tau(\mathcal C_X)
\le |O|-d+1.
\]
Rearranging proves
\[
|O|\ge |E(X)|+M-\rho(F_2,X)-1.
\]
∎

#### Theorem 4: Refined Boolean lower bound

If \(H\to(F_1,F_2)\), then
\[
\boxed{
|E(H)|
\ge
N+M-1+
\max\{\delta(F_1,F_2),\delta(F_2,F_1)\}.
}
\]

#### Proof

Let \(T\) be a minimum transversal of the \(F_2\)-copy family. By Proposition 1, \(H[T]\) contains a copy \(A\cong F_1\); in particular, \(|T|\ge N\).

For every \(F_2\)-free edge-subgraph \(X\subseteq A\), Proposition 3 yields
\[
|E(H)|
=
|T|+|O|
\ge
N+|E(X)|+M-\rho(F_2,X)-1.
\]
Maximizing over \(X\) gives
\[
|E(H)|\ge N+M-1+\delta(F_1,F_2).
\]
If \(\delta(F_1,F_2)=0\), the same conclusion is just Proposition 2.

Swapping the roles of the colors gives
\[
|E(H)|\ge N+M-1+\delta(F_2,F_1).
\]
Taking the larger bound proves the theorem. ∎

---

### 4. Computing the deficiency for star forests

Suppose
\[
P=\bigsqcup_{i=1}^s K_{1,p_i},
\qquad
Q=\bigsqcup_{j=1}^t K_{1,q_j}.
\]
An edge-subgraph \(X\subseteq P\) has component capacities
\[
0\le x_i\le p_i.
\]
After sorting these capacities as
\[
x_1^\downarrow\ge\cdots\ge x_s^\downarrow,
\]
one has
\[
\boxed{
\rho(Q,X)
=
\sum_{r=1}^{\min(s,t)}
\min(x_r^\downarrow,q_r).
}
\]

Indeed, each nonempty component of a common subgraph must pair one component of \(Q\) with one component of \(X\). Two different target components cannot use the same host-star component because target components are vertex-disjoint, whereas every two host-star edges meet at the host center. Pairing capacities and demands in decreasing order maximizes the sum of the minima. This follows, for example, by counting independently at every edge level \(a\ge1\): the number of paired edges available at level \(a\) is maximized by pairing the components with capacity at least \(a\) to those with demand at least \(a\).

Consequently, \(\delta(P,Q)\) is an explicit finite integer optimization over
\[
\prod_{i=1}^s\{0,1,\ldots,p_i\}.
\]

As a small exact example, take
\[
F_1=2K_2,\qquad F_2=K_{1,2}.
\]
Here \(N=M=2\). Taking \(X=F_1\), one has \(\rho(F_2,X)=1\): two adjacent edges cannot embed in a two-edge matching. Thus
\[
\delta(F_1,F_2)\ge2-1=1,
\]
and Theorem 4 gives
\[
|E(H)|\ge2+2-1+1=4.
\]
The antidiagonal formula also gives \(L=4\), so this instance follows.

The limitation is already visible for
\[
F_1=F_2=2K_{1,2}.
\]
Every \(F_2\)-free edge-subgraph \(X\subseteq F_1\) is itself a subgraph of \(F_2\), so
\[
\rho(F_2,X)=|E(X)|
\]
and \(\delta(F_1,F_2)=0\). Theorem 4 yields only \(7\), while \(L=9\).

---

### 5. Exact Boolean threshold theorem for star-forest hosts

Although insufficient for arbitrary hosts, the antidiagonal formula has a complete blocker-style explanation when the host itself is a disjoint union of stars.

Let
\[
D=\bigsqcup_{h=1}^u K_{1,d_h},
\qquad
d_1\ge d_2\ge\cdots\ge d_u\ge1.
\]
For \(1\le i\le s\), \(1\le j\le t\), define
\[
c_{ij}
=
\#\{h:d_h\ge n_i+m_j-1\}.
\]

#### Proposition 5

One has
\[
D\to(F_1,F_2)
\quad\Longleftrightarrow\quad
c_{ij}\ge i+j-1
\quad\text{for every }i,j.
\]

#### Proof

Consider a coloring of the \(h\)-th host star. Let \(r_h\) and \(b_h=d_h-r_h\) denote its red and blue degrees.

A red copy of \(F_1\) exists precisely when, after sorting the \(r_h\),
\[
r_i^\downarrow\ge n_i
\quad\text{for every }1\le i\le s.
\]
This is because one target component must be assigned to one host-star component. Distinct target components cannot be placed in one host star, as all nonempty edge sets in a host star meet at its center. The statement remains valid for \(K_{1,1}\), since two edges in one host star are not vertex-disjoint.

Thus, if there is no red \(F_1\), there is some \(i\) such that at most \(i-1\) host stars satisfy \(r_h\ge n_i\). Similarly, if there is no blue \(F_2\), there is some \(j\) such that at most \(j-1\) host stars satisfy \(b_h\ge m_j\).

Every host star counted by \(c_{ij}\) satisfies
\[
d_h\ge n_i+m_j-1.
\]
It therefore cannot simultaneously have
\[
r_h\le n_i-1,\qquad b_h\le m_j-1.
\]
Hence it is either red-large, \(r_h\ge n_i\), or blue-large, \(b_h\ge m_j\).

If \(c_{ij}\ge i+j-1\) for every \(i,j\), an avoiding coloring would give indices \(i,j\) for which at most \(i-1\) stars are red-large and at most \(j-1\) are blue-large. But then
\[
c_{ij}\le(i-1)+(j-1)=i+j-2,
\]
a contradiction. Thus \(D\) arrows.

Conversely, suppose
\[
c_{ij}\le i+j-2
\]
for some \(i,j\). Partition the \(c_{ij}\) large host stars into two classes \(S_R,S_B\) with
\[
|S_R|\le i-1,\qquad |S_B|\le j-1.
\]
For \(h\in S_R\), color at most \(m_j-1\) edges blue and the rest red. For \(h\in S_B\), color at most \(n_i-1\) edges red and the rest blue.

For every remaining host star,
\[
d_h\le n_i+m_j-2,
\]
so its edges can be split with
\[
r_h\le n_i-1,\qquad b_h\le m_j-1.
\]
The resulting coloring has at most \(i-1\) host components with red degree at least \(n_i\), and at most \(j-1\) with blue degree at least \(m_j\). Hence it contains neither \(F_1\) nor \(F_2\). ∎

#### Corollary 6

If a disjoint union of stars arrows \((F_1,F_2)\), then it has at least \(L\) edges.

#### Proof

Fix \(k\in\{2,\ldots,s+t\}\) and an admissible pair \(i+j=k\). Proposition 5 gives
\[
c_{ij}\ge k-1.
\]
Therefore
\[
d_{k-1}\ge n_i+m_j-1.
\]
Taking the maximum over all \(i+j=k\),
\[
d_{k-1}\ge l_k.
\]
Hence
\[
|E(D)|
=
\sum_{h=1}^u d_h
\ge
\sum_{h=1}^{s+t-1}d_h
\ge
\sum_{k=2}^{s+t}l_k
=L.
\]
The canonical host
\[
H^\star=\bigsqcup_{k=2}^{s+t}K_{1,l_k}
\]
meets these inequalities with equality and therefore arrows. ∎

This rigorously explains why the antidiagonal maximum arises: the \((k-1)\)-st largest independent star resource must cross every threshold \(n_i+m_j-1\) with \(i+j=k\).

---

### 6. Counterexamples to tempting blocker lemmas

#### Inclusion-minimal transversals are insufficient

Let
\[
F_1=2K_2,\qquad F_2=K_{1,2},
\]
and let \(H=P_4\), with consecutive edges \(e_1,e_2,e_3\).

The set
\[
T=\{e_1,e_3\}
\]
is an inclusion-minimal transversal of all \(P_3\) copies: the copies have edge sets \(\{e_1,e_2\}\) and \(\{e_2,e_3\}\). Moreover, \(T\) contains \(2K_2\). Nevertheless,
\[
|E(H)|=3<L=4.
\]
Thus the proposed lemma

> “an inclusion-minimal \(F_2\)-transversal containing \(F_1\) forces at least \(L\) edges”

is false. The minimum transversal \(\{e_2\}\) avoids \(F_1\), which is exactly the avoiding red set.

#### Private witnesses may overlap completely

For \(F_2=K_{1,2}\), let \(H=K_3\) and let \(T\) consist of two triangle edges. Then \(T\) is a minimum \(F_2\)-transversal. Removing either edge of \(T\) exposes a private \(P_3\), but both private witnesses use the same outside edge. Thus private-witness edge counts cannot simply be added.

These examples forced the use of the residual-hypergraph transversal number in Proposition 3. That refinement is valid, but the \(2K_{1,2}\) example shows it is still too weak.

---

## Self-Audit

1. **The residual-hypergraph bound is the most delicate proved step.**  
   The possible concern is that \(E(B)\cap T\) may be a disconnected or partially oriented subgraph of \(F_2\). The definition of \(\rho(F_2,X)\) deliberately allows arbitrary edge-subgraphs, so every such intersection is covered. The replacement set \((T\setminus X)\cup Y\) is checked against every \(F_2\)-copy, not merely private witnesses.

2. **The star-host characterization relies on “one target component per host component.”**  
   This remains valid when a target component is \(K_{1,1}\): two distinct edges of one host star meet at the center, whereas different components of the target forest must be vertex-disjoint. Thus no two nonempty target components can share a host-star component.

3. **Nothing proved here extends the antidiagonal counting argument to arbitrary hosts.**  
   This is not a hidden completeness claim: it is the decisive gap. A connected host may support several vertex-disjoint stars and may let residual witness families overlap. The explicit gap \(7<9\) for \(2K_{1,2}\) versus itself confirms that the proved blocker inequality does not already contain the desired theorem.

## Computations To Verify

```python
from itertools import product, combinations

def conjectured_L(n, m):
    s, t = len(n), len(m)
    ell = []
    for k in range(2, s + t + 1):
        vals = [
            n[i-1] + m[j-1] - 1
            for i in range(1, s+1)
            for j in range(1, t+1)
            if i + j == k
        ]
        assert vals
        ell.append(max(vals))
    assert all(ell[i] >= ell[i+1] for i in range(len(ell)-1))
    return sum(ell), ell

def rho_star_forest(x, m):
    """
    Maximum number of common edges between
    X = disjoint stars with capacities x
    and Q = disjoint stars with demands m.
    """
    xs = sorted((a for a in x if a > 0), reverse=True)
    ms = sorted(m, reverse=True)
    return sum(min(a, b) for a, b in zip(xs, ms))

def delta_star_forest(p, q):
    """
    delta(P,Q), where P and Q are star forests
    represented by their component sizes.
    """
    Qedges = sum(q)
    best = 0
    witness = None
    for x in product(*[range(a + 1) for a in p]):
        rho = rho_star_forest(x, q)
        if rho < Qedges:              # Q is not contained in X
            value = sum(x) - rho
            if value > best:
                best, witness = value, x
    return best, witness

def blocker_lower_bound(n, m):
    N, M = sum(n), sum(m)
    d12, x12 = delta_star_forest(n, m)
    d21, x21 = delta_star_forest(m, n)
    return N + M - 1 + max(d12, d21), (d12, x12), (d21, x21)

def contains_profile(capacities, demands):
    c = sorted(capacities, reverse=True)
    d = sorted(demands, reverse=True)
    return len(c) >= len(d) and all(c[i] >= d[i] for i in range(len(d)))

def star_host_criterion(d, n, m):
    for i, ni in enumerate(n, start=1):
        for j, mj in enumerate(m, start=1):
            count = sum(x >= ni + mj - 1 for x in d)
            if count < i + j - 1:
                return False
    return True

def brute_star_host_arrow(d, n, m):
    """
    Exhaust all color-count vectors on a disjoint union of stars.
    """
    for red in product(*[range(x + 1) for x in d]):
        blue = [d[h] - red[h] for h in range(len(d))]
        if not contains_profile(red, n) and not contains_profile(blue, m):
            return False, red
    return True, None

# Exhaustively compare Proposition 5 with direct color-count enumeration.
for u in range(1, 6):
    for d in product(range(1, 7), repeat=u):
        d = sorted(d, reverse=True)
        for s in range(1, 4):
            for t in range(1, 4):
                for n in product(range(1, 4), repeat=s):
                    if list(n) != sorted(n, reverse=True):
                        continue
                    for m in product(range(1, 4), repeat=t):
                        if list(m) != sorted(m, reverse=True):
                            continue
                        criterion = star_host_criterion(d, n, m)
                        brute, witness = brute_star_host_arrow(d, n, m)
                        assert criterion == brute, (d, n, m, witness)

# Key examples.
assert conjectured_L([2, 2], [2, 2]) == (9, [3, 3, 3])
assert blocker_lower_bound([2, 2], [2, 2])[0] == 7

assert conjectured_L([1, 1], [2])[0] == 4
assert blocker_lower_bound([1, 1], [2])[0] == 4
```

For an exact SAT test of a fixed host:

```python
from itertools import combinations
from pysat.solvers import Solver

def star_candidates(G, q, edge_id):
    """
    Return (vertex_set, edge_set) candidates for K_{1,q}.
    G is a networkx.Graph.
    """
    out = set()

    if q == 1:
        for u, v in G.edges():
            e = edge_id[tuple(sorted((u, v)))]
            out.add((frozenset((u, v)), frozenset((e,))))
        return list(out)

    for center in G.nodes():
        nbrs = list(G.neighbors(center))
        for leaves in combinations(nbrs, q):
            vertices = frozenset((center,) + leaves)
            edges = frozenset(
                edge_id[tuple(sorted((center, leaf)))]
                for leaf in leaves
            )
            out.add((vertices, edges))
    return list(out)

def forest_copy_edge_sets(G, demands):
    """
    Enumerate edge sets of complete, vertex-disjoint star-forest copies.
    """
    edge_id = {
        tuple(sorted(e)): i + 1
        for i, e in enumerate(G.edges())
    }
    candidate_lists = [
        star_candidates(G, q, edge_id)
        for q in demands
    ]

    copies = set()

    def dfs(k, used_vertices, used_edges):
        if k == len(demands):
            copies.add(frozenset(used_edges))
            return
        for vertices, edges in candidate_lists[k]:
            if used_vertices.isdisjoint(vertices):
                dfs(k + 1,
                    used_vertices | vertices,
                    used_edges | edges)

    dfs(0, frozenset(), frozenset())
    return copies

def is_arrow(G, red_demands, blue_demands):
    A = forest_copy_edge_sets(G, red_demands)
    B = forest_copy_edge_sets(G, blue_demands)

    if not A or not B:
        return False, None

    with Solver(name="cadical153") as solver:
        # At least one edge of every F1 copy is blue.
        for copy in A:
            solver.add_clause([-e for e in copy])

        # At least one edge of every F2 copy is red.
        for copy in B:
            solver.add_clause([e for e in copy])

        sat = solver.solve()
        if sat:
            return False, solver.get_model()
        return True, None
```

For the seed \((3,2)\) versus \((3,2)\), it suffices to search all no-isolate graphs with exactly \(11\) edges: any smaller arrowing graph can be augmented by disjoint edges and remains arrowing. Using `nauty`/`geng`, enumerate

```text
for v = 1,...,22:
    geng -d1 v 11:11
```

convert each graph6 output to `networkx`, discard graphs not containing the target uncolored, and call

```python
is_arrow(G, [3, 2], [3, 2])
```

An UNSAT candidate should then be rerun with proof logging and an independently checked DRAT/LRAT certificate.

## Route Diagnosis

**Proved ledger**

- Exact Boolean/blocker equivalences for arrowing.
- The universal \(N+M-1\) lower bound.
- The minimum-transversal residual exchange lemma.
- The computable deficiency lower bound
  \[
  N+M-1+\max\{\delta(F_1,F_2),\delta(F_2,F_1)\}.
  \]
- An exact criterion for disjoint unions of stars, yielding the full antidiagonal sum \(L\) in that host class.
- Counterexamples to naive summation of private witnesses and to use of arbitrary inclusion-minimal blockers.

**Plausible but unproved**

A successful Route 3 theorem would have to say roughly:

> If the blocker families of two graph-realizable star-forest copy hypergraphs are cross-intersecting, then their ground set has at least \(L\) elements.

As stated, this is essentially the original problem in blocker language. A useful noncircular version would need a multi-residual inequality coupling the exchange hypergraphs \(\mathcal C_X\) belonging to several vertex-disjoint red star components. Proposition 3 controls each such residual family separately, but their transversals and witnesses may overlap heavily.

**Dead ends**

- Clause lengths, LYM, generic monotone-cube covering, and generic blocker inequalities cannot exceed \(N+M-1\); complete uniform hypergraphs give a sharp abstract obstruction.
- Inclusion-minimal blocker witnesses cannot be summed; \(P_4\) and \(K_3\) give explicit failures.
- A single minimum-transversal exchange inequality is too weak even for \(2K_{1,2}\) versus itself, where it gives \(7\) instead of \(9\).

**Recommended fresh direction**

The most promising continuation is a hybrid of Routes 2 and 3: study the several residual copy hypergraphs generated by deleting different unions of red star components, and seek a graph-specific cross-transversal or set-pair inequality that charges overlapping residual witnesses according to their vertex-disjoint star-packing capacity. Computationally, minimal UNSAT cores and all minimum blockers for the \(L=9\) equal \(2K_{1,2}\) case and the \(L=12\) \((3,2)\) seed should be extracted first. They should reveal whether the missing antidiagonal charge is laminar, matching-based, or genuinely resolution-theoretic.