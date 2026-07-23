STATUS: BLOCKED

## Result

I did not resolve the \(C_7\) case. I established a sharp reduction to one dense ordinary block, proved the exact marked-edge connector formulation needed for Route 1, and found a concrete obstruction showing why a \(C_9\)-linkage argument cannot simply be shortened to \(C_7\). Specifically, every \(n\)-vertex host with \(t_2(n)+1\) edges has a single block \(B\) with more than \((n^2-1)/8\) edges and \(e(B)>t_2(|B|)\), so this block itself contains a \(C_7\). However, 2-connectivity and density \(n^2/4-O(n)\) are not enough for useful \(C_7\)-linkage: a balanced complete bipartite graph with a length-5 ear is 2-connected, has only \(2n-O(1)\) fewer edges than the target, and admits a valid 7-coloring. It also contains quadratically many edge-disjoint pairs lying on a \(C_9\) but on no \(C_7\). Thus any successful extension of the Bucić–Chen–Ma mechanism must use the exact \(t_2(n)+1\) edge budget to rule out or charge these short-ear configurations; an asymptotic density or generic 2-connected linkage lemma cannot suffice.

## Complete Argument

### 1. Exact marked-edge connector formulation

These are the precise linkage statements that a \(C_7\)-specific BCM replacement must force.

#### Lemma 1

Let \(e_1=uv\) and \(e_2=vw\) be distinct adjacent edges of a graph \(H\). They lie together on a simple \(C_7\) if and only if \(H-v\) contains a simple \(u\)-\(w\) path of length \(5\).

#### Proof

If a \(C_7\) contains \(uv\) and \(vw\), deleting these two edges and the common vertex \(v\) from the cyclic ordering leaves a simple \(u\)-\(w\) path consisting of the other five cycle edges. Conversely, adjoining \(uv\) and \(vw\) to such a path gives a simple cycle of length \(5+2=7\). ∎

#### Lemma 2

Let \(e_1=uv\) and \(e_2=xy\) be disjoint edges. They lie together on a simple \(C_7\) if and only if one of the following holds:

- there are mutually internally vertex-disjoint paths \(P_{ux}\) and \(P_{vy}\), disjoint also from the other marked endpoints, whose lengths are positive and sum to \(5\); or
- there are such paths \(P_{uy}\) and \(P_{vx}\) whose lengths are positive and sum to \(5\).

#### Proof

Delete the two marked edges from a simple \(C_7\). The remaining graph has two path components and pairs the four marked endpoints in one of the two stated ways. The five remaining cycle edges are partitioned between the two paths. Conversely, the union of the two paths and the two marked edges is a connected 2-regular graph on seven edges; the vertex-disjointness assumptions ensure that it is a simple \(C_7\). ∎

Thus the missing Route 1 ingredient is genuinely a fixed-length rooted linkage theorem, not merely common-cycle membership.

---

### 2. A universal dense-block reduction

The following reduction appears useful independently of the BCM proof.

#### Lemma 3: Block accounting

Let \(H\) have \(n\) vertices, \(e\) edges, and \(c\) connected components, counting isolated vertices. Let \(\mathcal B\) be its blocks, with bridges regarded as \(K_2\)-blocks. Then
\[
\sum_{B\in\mathcal B} \bigl(|V(B)|-1\bigr)=n-c,
\qquad
\sum_{B\in\mathcal B}|E(B)|=e.
\]

#### Proof

The edge identity holds because every edge lies in exactly one block.

For a connected nontrivial component, its block-cut incidence graph is a tree. Starting with one block and adding leaf blocks, each added block contributes exactly \(|V(B)|-1\) new vertices because it meets the preceding union in its unique cut vertex. Hence
\[
\sum_B(|V(B)|-1)=|V(\text{component})|-1.
\]
An isolated vertex contributes zero to both sides. Summing over components proves the identity. ∎

#### Proposition 4: A target-sized block exists

For all sufficiently large \(n\), every \(n\)-vertex graph \(H\) with
\[
e(H)=t_2(n)+1
\]
contains a block \(B\), of order \(m=|V(B)|\), satisfying
\[
e(B)>\frac{n^2-1}{8}
\]
and
\[
e(B)>t_2(m).
\]
In particular, \(m\ge n/2-o(1)\), and \(B\) contains a \(C_7\).

#### Proof

Put
\[
w_B=|V(B)|-1,\qquad e_B=|E(B)|.
\]
By Lemma 3,
\[
\sum_Bw_B=n-c\le n-1,\qquad \sum_Be_B=e.
\]
Therefore some block \(B\) satisfies
\[
\frac{e_B}{w_B}\ge \frac{e}{n-1}=:\rho_0.
\]
Write \(\rho_B=e_B/w_B\). Since \(B\) is simple,
\[
e_B\le \binom{w_B+1}{2}=\frac{w_B(w_B+1)}2.
\]
Consequently
\[
\rho_B\le\frac{w_B+1}{2},
\qquad\text{so}\qquad
w_B\ge 2\rho_B-1.
\]
It follows that
\[
e_B=\rho_Bw_B
   \ge \rho_B(2\rho_B-1)
   \ge \rho_0(2\rho_0-1).
\]
Because
\[
t_2(n)\ge \frac{n^2-1}{4},
\]
we have
\[
\rho_0=\frac{t_2(n)+1}{n-1}>\frac{n+1}{4}.
\]
Hence
\[
e_B>
\frac{n+1}{4}\left(\frac{n+1}{2}-1\right)
=\frac{n^2-1}{8}.
\]

It remains to show \(e_B>t_2(m)\). Define
\[
\phi(s)=\frac{t_2(s)}{s-1},\qquad s\ge2.
\]
This function is nondecreasing. Indeed, for \(q\ge1\),
\[
\phi(2q)=\frac{q^2}{2q-1},
\qquad
\phi(2q+1)=\frac{q+1}{2},
\]
and
\[
\phi(2q+1)-\phi(2q)
=\frac{q-1}{2(2q-1)}\ge0,
\]
while
\[
\phi(2q+2)-\phi(2q+1)
=\frac{q+1}{2(2q+1)}>0.
\]
Thus
\[
\frac{e_B}{m-1}
\ge \rho_0
=\phi(n)+\frac1{n-1}
>\phi(n)\ge\phi(m).
\]
Therefore \(e_B>t_2(m)\).

Also \(e_B\le\binom m2<m^2/2\), so the previously established lower bound on \(e_B\) gives \(m\ge n/2-o(1)\). Thus \(m\to\infty\), and Simonovits’s exact theorem
\[
\operatorname{ex}(m,C_7)=t_2(m)
\]
applies. Since \(e_B>t_2(m)\), the block \(B\) contains a \(C_7\). ∎

This is a useful localization: the desired global lower bound would follow from the following block-level statement.

> **Unproved block linkage statement.** If \(G\) is a 2-connected graph on \(m\le n\) vertices satisfying
> \[
> \frac{e(G)}{m-1}\ge\frac{t_2(n)+1}{n-1},
> \]
> then every coloring in which all \(C_7\)'s are rainbow uses at least
> \[
> \frac{n^2}{8}-o(n^2)
> \]
> colors.

This statement remains unproved and is the present block.

---

### 3. A sharp obstruction to an asymptotic linkage lemma

The next construction shows that neither 2-connectivity nor edge count \(t_2(n)-O(n)\) is sufficient.

#### Proposition 5: The length-5 ear obstruction

Let \(A,B\) be disjoint sets with \(x,y\in A\), and let
\[
p_1,p_2,p_3,p_4
\]
be four further vertices. Start with \(K_{A,B}\) and add the path
\[
P=xp_1p_2p_3p_4y.
\]
Assume \(|A|,|B|\ge2\). Then:

1. the resulting graph \(J\) is 2-connected;
2. its \(C_7\)'s are exactly
   \[
   P\cup\{yb,bx\},\qquad b\in B;
   \]
3. \(\chi(Q_7(J))=7\);
4. if \(|A|+|B|=n-4\) and the bipartite core is balanced, then
   \[
   e(J)=t_2(n)-2n+9,
   \]
   only \(2n-8\) edges below \(t_2(n)+1\).

#### Proof

The complete bipartite core is 2-connected. Adding an ear between two distinct vertices of a 2-connected graph preserves 2-connectivity. This can also be checked directly: deleting an internal path vertex leaves the two remaining path segments attached to the connected core at \(x\) and \(y\); deleting a core vertex leaves the core connected and the surviving path attached to at least one endpoint.

Every internal vertex \(p_i\) has degree two. Therefore any cycle containing one edge of \(P\) must contain all of \(P\). A cycle avoiding \(P\) lies in the bipartite core and hence has even length. Thus every \(C_7\) consists of all five edges of \(P\) and an \(x\)-\(y\) path of length two in the core. Such paths are exactly \(xby\), \(b\in B\). This proves the asserted classification.

Color the five path edges with five distinct colors. Give every edge \(xb\), \(b\in B\), color 6, and every edge \(yb\), \(b\in B\), color 7. Give every remaining core edge color 1. Each \(C_7\) contains the five differently colored path edges and exactly one edge of colors 6 and 7, so it is rainbow. Thus \(\chi(Q_7(J))\le7\). Since \(J\) contains a \(C_7\), its seven edges form a \(K_7\) in the conflict graph, so \(\chi(Q_7(J))\ge7\).

Finally, if \(|A|+|B|=n-4\) and the core is balanced, then
\[
e(J)=t_2(n-4)+5.
\]
For both parities,
\[
t_2(n)-t_2(n-4)=2n-4.
\]
Hence
\[
e(J)=t_2(n)-(2n-4)+5=t_2(n)-2n+9.
\]
The difference from \(t_2(n)+1\) is \(2n-8\). ∎

This invalidates any proposed lemma of the form:

> Every 2-connected graph with \(n^2/4-o(n^2)\) edges and at least one \(C_7\) satisfies \(\chi(Q_7)=\Omega(n^2)\).

Indeed, the graphs above have \(n^2/4-O(n)\) edges but conflict chromatic number exactly 7.

---

### 4. Why direct shortening from \(C_9\) fails

The same ear graph supplies quadratically many explicit pairs that can be linked by a \(C_9\) but not by a \(C_7\).

#### Proposition 6

In the graph \(J\) of Proposition 5, let
\[
a\in A\setminus\{x,y\},\qquad b_1,b_2\in B,\quad b_1\ne b_2.
\]
Then the two adjacent core edges
\[
ab_1,\quad ab_2
\]
lie together on a \(C_9\), but on no \(C_7\).

Moreover, if \(|A|,|B|=\Theta(n)\), there are \(\Theta(n^2)\) pairwise edge-disjoint pairs with this property.

#### Proof

By Proposition 5, every core edge appearing on a \(C_7\) is incident with \(x\) or \(y\). Therefore neither \(ab_1\) nor \(ab_2\) appears on any \(C_7\).

On the other hand,
\[
x p_1p_2p_3p_4 y b_2 a b_1 x
\]
is a simple \(C_9\) containing both marked edges.

For each \(a\in A\setminus\{x,y\}\), partition all but at most one vertex of \(B\) into pairs \(\{b_{2i-1},b_{2i}\}\), and use the marked pair
\[
\{ab_{2i-1},ab_{2i}\}.
\]
No host edge occurs in two selected marked pairs. Their number is
\[
(|A|-2)\left\lfloor\frac{|B|}{2}\right\rfloor=\Theta(n^2).
\]
∎

Thus a BCM linkage assertion that obtains a length-7 detour after deleting two marked edges from a \(C_9\) cannot simply be shortened to the length-5 detour needed for \(C_7\). The failure occurs with quadratic multiplicity, not merely in finitely many local exceptions.

---

### 5. A positive \(C_7\)-specific model calculation

The obstruction is caused by the long ear consuming five of the seven cycle edges. In the standard near-bipartite model with one internal edge, \(C_7\)-linkage is instead very strong.

#### Proposition 7

Let \(H=K_{A,B}+xy\), where \(x,y\in A\), \(|A|\ge4\), and \(|B|\ge3\). Then
\[
F=E(A\setminus\{x,y\},B)
\]
is a clique in \(Q_7(H)\). Consequently, every valid coloring uses at least
\[
(|A|-2)|B|
\]
colors.

#### Proof

Take distinct edges \(a_1b_1,a_2b_2\in F\). Every desired cycle will consist of the internal edge \(xy\) and a simple length-6 \(y\)-\(x\) path in the complete bipartite graph.

There are three cases.

If \(a_1=a_2=a\), choose
\[
a'\in A\setminus\{x,y,a\},\qquad
b_3\in B\setminus\{b_1,b_2\}.
\]
Then
\[
x y b_1 a b_2 a' b_3 x
\]
is a \(C_7\) containing both edges.

If \(b_1=b_2=b\), choose distinct
\[
c_1,c_3\in B\setminus\{b\}.
\]
Then
\[
x y c_1 a_1 b a_2 c_3 x
\]
is a \(C_7\) containing both edges.

If \(a_1\ne a_2\) and \(b_1\ne b_2\), choose
\[
b_0\in B\setminus\{b_1,b_2\}.
\]
Then
\[
x y b_1 a_1 b_0 a_2 b_2 x
\]
is a \(C_7\) containing both edges.

Thus every two edges of \(F\) conflict, proving the result. ∎

In particular, for the balanced host \(K_{\lfloor n/2\rfloor,\lceil n/2\rceil}\) plus one internal edge, this already forces
\[
\frac{n^2}{4}-O(n)
\]
colors, much more than the conjectured lower bound. Therefore the difficult hosts must exploit separators or ear-like structures, not merely near-bipartiteness.

## Self-Audit

1. **The block calculation depends on the precise convention for blocks.**  
   Bridges must be included as \(K_2\)-blocks, and isolated vertices contribute no block. Under that standard convention, the identity \(\sum_B(|B|-1)=n-c\) follows directly from the block-cut tree, so I believe the calculation is sound.

2. **The assertion that the selected block contains a \(C_7\) uses Simonovits’s exact theorem.**  
   This is an external theorem supplied in the brief. The selected block has order at least \(n/2-o(n)\), so its order tends to infinity and the unspecified finite threshold in that theorem is eventually passed.

3. **The ear and complete-bipartite connector arguments depend on there being enough spare vertices.**  
   The assumptions \(|A|\ge4\) and \(|B|\ge3\) in Proposition 7 explicitly provide every spare vertex used in the three cases. In the ear construction, degree two of every internal ear vertex forces the whole ear into any cycle, so no unlisted \(C_7\) can occur. These points can also be exhaustively checked computationally.

The central \(C_7\) block-linkage assertion is not proved and is not being presented as a weakly justified step; it is the precise missing theorem.

## Computations To Verify

The following code enumerates non-induced simple cycles correctly: chords are allowed because only the selected cyclic edges are tested.

```python
import itertools
import networkx as nx

def edge(u, v):
    return tuple(sorted((u, v)))

def cycles_of_length(G, L):
    """Return simple L-cycles as frozensets of their L selected edges."""
    out = set()
    nodes = sorted(G.nodes())
    for S in itertools.combinations(nodes, L):
        root = min(S)
        rest = [v for v in S if v != root]
        for perm in itertools.permutations(rest):
            cyc = (root,) + perm
            # Quotient reversal; fixing root already quotients rotations.
            if cyc[1] > cyc[-1]:
                continue
            edges = [
                edge(cyc[i], cyc[(i + 1) % L])
                for i in range(L)
            ]
            if all(G.has_edge(*e) for e in edges):
                out.add(frozenset(edges))
    return out

def conflict_graph(G, L=7):
    Q = nx.Graph()
    host_edges = [edge(u, v) for u, v in G.edges()]
    Q.add_nodes_from(host_edges)
    for C in cycles_of_length(G, L):
        for e, f in itertools.combinations(C, 2):
            Q.add_edge(e, f)
    return Q
```

The ear construction and its 7-coloring:

```python
def ear_graph(a, b):
    assert a >= 2 and b >= 1
    A = list(range(a))
    B = list(range(a, a + b))
    p = list(range(a + b, a + b + 4))
    x, y = A[0], A[1]

    G = nx.Graph()
    G.add_nodes_from(A + B + p)
    G.add_edges_from((u, v) for u in A for v in B)

    path_vertices = [x] + p + [y]
    path_edges = [
        edge(path_vertices[i], path_vertices[i + 1])
        for i in range(5)
    ]
    G.add_edges_from(path_edges)

    colors = {}
    for i, e in enumerate(path_edges):
        colors[e] = i + 1

    for u, v in G.edges():
        e = edge(u, v)
        if e in colors:
            continue
        if x in e and (e[0] in B or e[1] in B):
            colors[e] = 6
        elif y in e and (e[0] in B or e[1] in B):
            colors[e] = 7
        else:
            colors[e] = 1

    return G, colors, A, B, x, y, p

G, colors, A, B, x, y, p = ear_graph(5, 5)
C7s = cycles_of_length(G, 7)

assert len(C7s) == len(B)
for C in C7s:
    assert len({colors[e] for e in C}) == 7

Q7 = conflict_graph(G, 7)
assert nx.graph_clique_number(Q7) >= 7
```

Verification of the \(C_9\)-but-not-\(C_7\) pairs:

```python
def conflict_pairs(G, L):
    pairs = set()
    for C in cycles_of_length(G, L):
        for e, f in itertools.combinations(sorted(C), 2):
            pairs.add(frozenset((e, f)))
    return pairs

G, colors, A, B, x, y, p = ear_graph(5, 5)
P7 = conflict_pairs(G, 7)
P9 = conflict_pairs(G, 9)

for a in A:
    if a in (x, y):
        continue
    for b1, b2 in itertools.combinations(B, 2):
        pair = frozenset((edge(a, b1), edge(a, b2)))
        assert pair not in P7
        assert pair in P9
```

Verification of Proposition 7:

```python
def complete_bip_plus_internal(a, b):
    A = list(range(a))
    B = list(range(a, a + b))
    x, y = A[0], A[1]

    G = nx.Graph()
    G.add_nodes_from(A + B)
    G.add_edges_from((u, v) for u in A for v in B)
    G.add_edge(x, y)
    return G, A, B, x, y

for a in range(4, 8):
    for b in range(3, 8):
        G, A, B, x, y = complete_bip_plus_internal(a, b)
        Q = conflict_graph(G, 7)
        F = [edge(u, v) for u in A if u not in (x, y) for v in B]
        assert all(Q.has_edge(e, f) for e, f in itertools.combinations(F, 2))
```

A useful finite-template search is to force the ear and ask whether it can be completed by exactly \(2n-8\) edges to an exact-threshold host while retaining significantly fewer than \(n^2/8\) colors. The following CP-SAT skeleton does this.

```python
from ortools.sat.python import cp_model

def can_complete_ear_with_k_colors(a, b, K, time_limit=600):
    base, _, _, _, _, _, _ = ear_graph(a, b)
    n = base.number_of_nodes()
    vertices = list(range(n))
    all_edges = [edge(u, v) for u in vertices for v in vertices if u < v]

    model = cp_model.CpModel()
    present = {e: model.NewBoolVar(f"h_{e[0]}_{e[1]}") for e in all_edges}
    color = {
        e: model.NewIntVar(0, K - 1, f"c_{e[0]}_{e[1]}")
        for e in all_edges
    }

    for e in base.edges():
        model.Add(present[edge(*e)] == 1)

    model.Add(sum(present.values()) == (n * n) // 4 + 1)

    # Enumerate every abstract 7-cycle in K_n.
    Kn = nx.complete_graph(n)
    for C in cycles_of_length(Kn, 7):
        literals = [present[e] for e in C]
        for e, f in itertools.combinations(C, 2):
            model.Add(color[e] != color[f]).OnlyEnforceIf(literals)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = 8
    result = solver.Solve(model)
    return result in (cp_model.OPTIMAL, cp_model.FEASIBLE)
```

The most informative runs would be:

- balanced cores on \(n-4\) vertices for \(11\le n\le15\);
- \(K\) near \(\lfloor n^2/8\rfloor\);
- then progressively smaller \(K\);
- extraction and structural analysis of every feasible completion.

## Route Diagnosis

### Proved ledger

- Exact adjacent and disjoint marked-edge formulations for membership in a \(C_7\).
- Every exact-threshold host contains one ordinary block with more than \((n^2-1)/8\) edges.
- That same block exceeds \(t_2(m)\) on its own vertex set and therefore contains a \(C_7\).
- A 2-connected graph with \(t_2(n)-2n+9\) edges can nevertheless have \(\chi(Q_7)=7\).
- There are quadratically many edge-disjoint pairs which lie on a \(C_9\) but on no \(C_7\).
- In \(K_{A,B}\) plus one internal edge, all cross edges avoiding the two internal-edge endpoints form a clique in \(Q_7\).

### Plausible but unproved

A sharp block/ear theorem is needed: a 2-connected block satisfying the exact density-ratio inequality from Proposition 4 should either have conflict chromatic number at least \(n^2/8-o(n^2)\), or admit a decomposition into short-cycle-separated dense pieces whose largest palette still has that size.

This cannot be weakened to \(e=t_2(n)-O(n)\): Proposition 5 is a counterexample.

### Dead ends

1. **Directly shorten a \(C_9\) connector to a \(C_7\) connector.**  
   Proposition 6 kills this with \(\Theta(n^2)\) edge-disjoint marked pairs.

2. **Use only 2-connectivity and density \(n^2/4-o(n^2)\).**  
   Proposition 5 has those properties but only needs seven colors.

3. **Use ordinary block decomposition alone.**  
   It locates a target-sized block, but fixed-length \(C_7\)-conflict can occupy only a tiny part of a dense 2-connected block unless the exact edge budget is exploited.

### Best next direction

The most promising continuation is a hybrid of Routes 1 and 2 based on an ear decomposition of the dense block from Proposition 4. A “long” attachment that localizes all \(C_7\)'s has a quantifiable vertex cost: the length-5 ear example loses exactly \(2n-O(1)\) edges relative to \(t_2(n)\). At the exact threshold, those missing edges must be restored elsewhere. One should prove that restoring them either:

- creates the length-5 marked connectors required by Lemmas 1 and 2 on a quadratic edge set; or
- creates another dense, cycle-separated region whose palette alone costs \(n^2/8-o(n^2)\).

Computationally, the immediate obstruction test is to complete the ear graph by exactly \(2n-8\) edges and optimize \(\chi(Q_7)\). If low-color completions repeatedly converge to a finite blow-up template, that would point toward a disproof. If all completions collapse toward the known two-dense-piece construction or a near-complete bipartite graph with a broadly linked internal edge, it would support the required sharp ear-accounting lemma.