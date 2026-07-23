STATUS: BLOCKED

## Result

A complete determination is blocked already at \(k=2\), since it is exactly equivalent to determining \(\operatorname{ex}(n,C_4)\) for every \(n\). Pursuing Route 2 nevertheless gives several rigorous advances. For every \(m\ge4\), codegree counting yields
\[
M_m(n):=\operatorname{ex}(n,\mathcal F_m)
\le
\frac n4\left(1+\sqrt{1+4(m-3)(n-1)}\right).
\]
For \(m=5\) (\(k=3\)), I prove a sharp asymptotic result within the bipartite class:
\[
\max_{\substack{H\text{ bipartite}\\H\ \mathcal F_5\text{-free}}}e(H)
=
\left(\frac12+o(1)\right)n^{3/2}.
\]
The lower bound comes from an explicit finite-field quotient construction and its bipartite double cover. Consequently,
\[
\left(\frac12-o(1)\right)n^{3/2}
\le M_5(n)\le
\left(\frac{\sqrt2}{2}+o(1)\right)n^{3/2}.
\]
I also prove that every \(\mathcal F_5\)-free graph has at most \(n\) triangles. Finally, the algebraic bipartite examples contain \(\Theta(n^2)\) copies of \(C_4\), and deleting all \(C_4\)'s requires \(\Omega(n^{3/2})\) edges. Thus a proposed reduction of dense \(\mathcal F_5\)-free graphs to high-girth graphs by negligible edge deletion is rigorously false.

## Complete Argument

### 1. The unavoidable \(C_4\) obstruction

Let
\[
M_m(n)=\operatorname{ex}(n,\mathcal F_m).
\]
Then
\[
f(n,k)=\binom n2-M_{k+2}(n).
\]

For \(m=4\), a graph on four vertices with minimum degree at least \(2\) contains a \(C_4\). Indeed, it contains a cycle. If this cycle has length four, there is nothing to prove. If it is a triangle \(abc\), the fourth vertex \(x\) has at least two neighbors in the triangle, say \(a,b\), and then
\[
x-a-c-b-x
\]
is a \(4\)-cycle. Conversely, the four vertices of any \(C_4\), even with extra edges present, span a graph of minimum degree at least \(2\). Hence
\[
M_4(n)=\operatorname{ex}(n,C_4)
\]
and therefore
\[
f(n,2)=\binom n2-\operatorname{ex}(n,C_4).
\]

Thus an exact all-\((n,k)\) solution necessarily includes an exact all-\(n\) solution to the \(C_4\) Turán problem. The arguments below do not overcome that obstruction.

---

### 2. General codegree and spectral inequalities

#### Lemma 2.1: Codegree cap

Let \(m\ge4\), and let \(H\) be \(\mathcal F_m\)-free. Then every two distinct vertices have at most \(m-3\) common neighbors.

#### Proof

If \(u,v\) had \(m-2\) distinct common neighbors \(x_1,\dots,x_{m-2}\), the graph on
\[
\{u,v,x_1,\dots,x_{m-2}\}
\]
would contain \(K_{2,m-2}\). Every \(x_i\) has degree \(2\) in this subgraph, while \(u,v\) each have degree \(m-2\ge2\). This is an \(m\)-vertex subgraph of minimum degree at least \(2\), a contradiction. ∎

Put \(a=m-3\). Counting length-two paths by their middle vertices gives
\[
\sum_{v}\binom{d(v)}2
=
\sum_{\{x,y\}}|N(x)\cap N(y)|
\le
a\binom n2.
\]
By Cauchy–Schwarz,
\[
\sum_v d(v)^2\ge \frac{(2e(H))^2}{n},
\]
so
\[
\sum_v\binom{d(v)}2
=
\frac12\sum_vd(v)^2-e(H)
\ge
\frac{2e(H)^2}{n}-e(H).
\]
Consequently
\[
\frac{2e(H)^2}{n}-e(H)
\le
\frac{a n(n-1)}2.
\]
Solving the resulting quadratic inequality gives:

#### Theorem 2.2: General codegree upper bound

For every \(m\ge4\),
\[
\boxed{
M_m(n)\le
\frac n4\left(1+\sqrt{1+4(m-3)(n-1)}\right).
}
\]

Equivalently, for \(k\ge2\),
\[
\boxed{
f(n,k)\ge
\binom n2-
\frac n4\left(1+\sqrt{1+4(k-1)(n-1)}\right).
}
\]

For \(k=2\), this is exactly the standard Reiman codegree bound for \(C_4\)-free graphs.

There is also a direct spectral consequence. Let \(A\) be the adjacency matrix of \(H\), and let \(c(u,v)\) denote codegree. For every \(v\),
\[
(A^2\mathbf1)_v
=
d(v)+\sum_{u\ne v}c(u,v)
\le d(v)+a(n-1)
\le(a+1)(n-1).
\]
Since \(A^2\) is nonnegative,
\[
\rho(A)^2=\rho(A^2)\le(a+1)(n-1),
\]
and the Rayleigh quotient of \(\mathbf1\) gives \(2e(H)/n\le\rho(A)\). Hence
\[
e(H)\le\frac n2\sqrt{(m-2)(n-1)}.
\]
This spectral estimate is weaker than Theorem 2.2, illustrating that the second adjacency moment alone does not assemble the required \(m\)-vertex configuration.

---

### 3. Local assembly restrictions

The codegree cap detects only \(K_{2,m-2}\). The following restrictions use other members of \(\mathcal F_m\).

#### Lemma 3.1: Two-neighbor extension

Suppose \(H\) is \(\mathcal F_m\)-free and \(Q\subseteq H\) is a subgraph on \(\ell<m\) vertices with \(\delta(Q)\ge2\). Then there are at most \(m-\ell-1\) vertices outside \(Q\) having at least two neighbors in \(V(Q)\).

#### Proof

If there were \(m-\ell\) such vertices, choose a set \(X\) of exactly \(m-\ell\) of them. Retain the edges of \(Q\) and, for each \(x\in X\), any two edges from \(x\) into \(Q\). In the resulting graph on \(V(Q)\cup X\), every vertex of \(Q\) still has degree at least \(2\), and every vertex of \(X\) has degree at least \(2\). This contradicts \(\mathcal F_m\)-freeness. ∎

In particular, if \(C\) is a cycle of length \(\ell<m\), then at most \(m-\ell-1\) outside vertices have at least two neighbors on \(C\).

#### Lemma 3.2: Neighborhood shadow

If \(H\) is \(\mathcal F_m\)-free, then for every vertex \(v\), the graph \(H[N(v)]\) contains no \((m-1)\)-vertex subgraph of minimum degree at least \(1\).

#### Proof

If \(X\subseteq N(v)\), \(|X|=m-1\), and \(H[X]\) has minimum degree at least \(1\), then in \(H[X\cup\{v\}]\), every vertex of \(X\) has its neighbor inside \(X\) and also the neighbor \(v\), while \(v\) has degree \(m-1\). Thus the \(m\)-vertex graph has minimum degree at least \(2\), a contradiction. ∎

---

### 4. Special consequences for \(m=5\)

#### Proposition 4.1: At most \(n\) triangles

Every \(\mathcal F_5\)-free \(n\)-vertex graph contains at most \(n\) triangles.

#### Proof

Fix \(v\), and put \(L=H[N(v)]\). By Lemma 3.2, \(L\) contains no four-vertex subgraph without isolated vertices.

If \(L\) had two distinct connected components each containing an edge, the four endpoints of one edge from each component would span a four-vertex graph with no isolated vertex. Thus \(L\) has at most one nontrivial component.

If that component had at least four vertices, take a spanning tree and repeatedly delete leaves until four vertices remain. Those four vertices span a connected subgraph and hence have no isolated vertices, again a contradiction.

Therefore the only nontrivial component of \(L\), if present, has at most three vertices. It follows that
\[
e(H[N(v)])\le3.
\]
Each triangle of \(H\) contributes one edge to \(H[N(v)]\) for each of its three vertices. If \(T(H)\) denotes the number of triangles, then
\[
3T(H)=\sum_v e(H[N(v)])\le3n.
\]
Hence \(T(H)\le n\). ∎

The estimate is sharp: a disjoint union of copies of \(K_4\) is \(\mathcal F_5\)-free and has exactly one triangle per vertex.

It follows in particular that every \(\mathcal F_5\)-free graph can be made triangle-free by deleting at most \(n\) edges.

---

### 5. The bipartite \(m=5\) problem is asymptotically solved

#### Lemma 5.1

A bipartite graph is \(\mathcal F_5\)-free if and only if it is \(K_{2,3}\)-free.

#### Proof

One direction is immediate because \(K_{2,3}\) has five vertices and minimum degree \(2\).

Conversely, suppose a bipartite graph contains a five-vertex subgraph \(F\) with \(\delta(F)\ge2\). Both bipartition classes of \(F\) have size at least \(2\), so their sizes are \(2\) and \(3\). Every vertex in the class of size \(3\) has degree at most \(2\), and hence exactly \(2\). Thus all three are adjacent to both vertices in the other class, producing a \(K_{2,3}\). ∎

Let \(Z_5(n)\) denote the maximum number of edges in a bipartite, \(\mathcal F_5\)-free \(n\)-vertex graph.

#### Proposition 5.2: Bipartite upper bound

\[
Z_5(n)\le \frac12n^{3/2}+n.
\]

#### Proof

Let the bipartition have orders \(x,y\), and let the graph have \(e\) edges. Since it is \(K_{2,3}\)-free, every two vertices in the same part have at most two common neighbors.

Counting wedges centered in the \(y\)-part,
\[
\sum_{w\in Y}\binom{d(w)}2\le2\binom x2.
\]
Cauchy–Schwarz gives
\[
\sum_{w\in Y}\binom{d(w)}2
\ge
\frac{e^2}{2y}-\frac e2,
\]
and hence
\[
\frac{e^2}{y}-e\le2x(x-1)\le2x^2.
\]
Therefore
\[
e^2\le ey+2x^2y,
\]
which implies
\[
e\le y+\sqrt2\,x\sqrt y.
\]
Interchanging the two parts similarly gives
\[
e\le x+\sqrt2\,y\sqrt x.
\]
Consequently
\[
e\le n+\sqrt2\min\{x\sqrt y,y\sqrt x\}.
\]
If \(x\le y\), the minimum is \(x\sqrt y=x\sqrt{n-x}\), which is increasing for \(x\le n/2\). Its maximum is therefore attained at \(x=y=n/2\), where it equals
\[
\frac{n^{3/2}}{2\sqrt2}.
\]
Thus
\[
e\le n+\frac12n^{3/2}.
\]
∎

---

### 6. An algebraic construction attaining the bipartite constant

The following quotient construction also shows that the codegree inequalities can be nearly saturated without producing the desired forbidden configuration.

#### Lemma 6.1: Finite-field codegree construction

Let \(q\) be a prime power, and let \(T\le\mathbb F_q^\times\) be a multiplicative subgroup of order \(t\). On
\[
X=(\mathbb F_q^2\setminus\{0\})/T,
\]
where vectors are identified under multiplication by elements of \(T\), define distinct classes \([a],[b]\) to be adjacent when
\[
a\cdot b\in T.
\]
After loops are discarded, the resulting simple graph \(J(q,t)\) has
\[
|X|=\frac{q^2-1}{t},
\qquad
d(v)\in\{q-1,q\},
\]
and every two distinct vertices have at most \(t\) common neighbors. In particular, it is \(K_{2,t+1}\)-free.

#### Proof

The definition is independent of representatives because replacing \(a,b\) by \(h_1a,h_2b\), with \(h_1,h_2\in T\), multiplies \(a\cdot b\) by \(h_1h_2\in T\).

For fixed nonzero \(a\), the set
\[
\{b:a\cdot b\in T\}
\]
is the disjoint union of \(t\) affine lines, each containing \(q\) vectors. It therefore has \(tq\) vectors, or \(q\) quotient classes. The class \([a]\) itself may be among them, accounting for a loop; after loops are removed, the degree is \(q\) or \(q-1\).

Now consider distinct classes \([a],[b]\). If \(a,b\) are linearly independent, then for each \((h_1,h_2)\in T^2\), the system
\[
a\cdot x=h_1,\qquad b\cdot x=h_2
\]
has a unique solution. The \(t^2\) solutions split into quotient orbits of size \(t\) under simultaneous multiplication by elements of \(T\), giving exactly \(t\) common classes before loops are removed.

If \(b=\lambda a\), distinctness of the quotient classes means \(\lambda\notin T\). Were \(x\) a common neighbor, then both \(a\cdot x\) and \(\lambda a\cdot x\) would lie in \(T\), forcing \(\lambda\in T\), a contradiction. Thus dependent distinct classes have no common neighbor. Removing loops cannot increase codegrees. ∎

Take \(t=2\), \(q\) odd, and \(T=\{1,-1\}\). Then
\[
N_0=|V(J(q,2))|=\frac{q^2-1}{2},
\qquad
e(J(q,2))\ge\frac{N_0(q-1)}2.
\]

Form the bipartite double cover \(B_q\): take left and right copies of \(V(J)\), and replace every edge \(uv\) of \(J\) with the two bipartite edges
\[
u_Lv_R,\qquad v_Lu_R.
\]
Then
\[
|V(B_q)|=2N_0=q^2-1
\]
and
\[
e(B_q)=2e(J(q,2))
\ge N_0(q-1)
=
\frac{(q^2-1)(q-1)}2.
\]
Pairs in either side of \(B_q\) have the same codegrees as the corresponding pairs in \(J(q,2)\), so \(B_q\) is \(K_{2,3}\)-free. By Lemma 5.1, it is \(\mathcal F_5\)-free.

Thus, when \(N=q^2-1\),
\[
M_5(N)\ge\frac{N(q-1)}2
=
\left(\frac12-o(1)\right)N^{3/2}.
\]
For arbitrary large \(n\), choose an odd prime \(q=(1-o(1))\sqrt n\) with \(q^2-1\le n\), using the prime number theorem, and add isolated vertices. Therefore
\[
M_5(n)\ge\left(\frac12-o(1)\right)n^{3/2}.
\]

Together with Theorem 2.2,
\[
\boxed{
\left(\frac12-o(1)\right)n^{3/2}
\le M_5(n)
\le
\left(\frac{\sqrt2}{2}+o(1)\right)n^{3/2}.
}
\]
Moreover, Proposition 5.2 and the construction prove
\[
\boxed{
Z_5(n)=\left(\frac12+o(1)\right)n^{3/2}.
}
\]

In terms of the original problem,
\[
\binom n2-\left(\frac{\sqrt2}{2}+o(1)\right)n^{3/2}
\le f(n,3)
\le
\binom n2-\left(\frac12-o(1)\right)n^{3/2}.
\]

---

### 7. Dense \(C_4\)'s are compatible with \(\mathcal F_5\)-freeness

The construction above disproves a tempting structural route: one cannot generally delete \(o(n^{3/2})\) edges from a dense \(\mathcal F_5\)-free graph to make it \(C_4\)-free.

Consider first the loop-allowed relation underlying \(J(q,2)\). Every linearly independent pair of quotient classes has exactly two common classes.

There are \(N_0=(q^2-1)/2\) quotient classes. Each one-dimensional subspace of \(\mathbb F_q^2\) contains \((q-1)/2\) quotient classes, so the number of linearly dependent unordered pairs is
\[
(q+1)\binom{(q-1)/2}{2}=O(q^3).
\]
Removing loops can lower the codegree of a pair only when one of its common classes equals an endpoint. There are at most \(N_0q=O(q^3)\) such endpoint-neighbor incidences. Hence all but \(O(q^3)\) of the \(\binom{N_0}{2}\) pairs have codegree exactly \(2\) in the simple graph \(J(q,2)\).

In the bipartite double cover, every pair of left vertices with two common right neighbors determines a unique \(C_4\). Therefore
\[
\#C_4(B_q)
\ge
\binom{N_0}{2}-O(q^3)
=
\Theta(q^4)
=
\Theta(|V(B_q)|^2).
\]

On the other hand, every edge of \(B_q\) belongs to at most \(q-1\) copies of \(C_4\). Indeed, fix an edge \(u_Lw_R\). For each other left neighbor \(v_L\) of \(w_R\), the pair \(u_L,v_L\) has at most two common neighbors, one of which is \(w_R\), leaving at most one choice for the fourth vertex. Since \(d(w_R)\le q\), the edge belongs to at most \(q-1\) four-cycles.

Thus any set of edges meeting every \(C_4\) has size at least
\[
\frac{\Theta(q^4)}{q-1}
=
\Theta(q^3)
=
\Theta(|V(B_q)|^{3/2}).
\]
Since \(e(B_q)=\Theta(|V(B_q)|^{3/2})\), a positive-order proportion of the edges may have to be removed to eliminate all \(C_4\)'s.

This is a concrete counterexample to any proposed lemma asserting that dense \(\mathcal F_5\)-free graphs are asymptotically high-girth after negligible edge deletion.

---

### 8. Ledger

**Proved lemmas and results**

1. \(M_4(n)=\operatorname{ex}(n,C_4)\).
2. The codegree cap \(c(u,v)\le m-3\).
3. The general bound
   \[
   M_m(n)\le\frac n4\left(1+\sqrt{1+4(m-3)(n-1)}\right).
   \]
4. The two-neighbor extension lemma.
5. The neighborhood-shadow lemma.
6. Every \(\mathcal F_5\)-free graph has at most \(n\) triangles.
7. Bipartite \(\mathcal F_5\)-free is equivalent to \(K_{2,3}\)-free.
8. The bipartite asymptotic
   \[
   Z_5(n)=\left(\frac12+o(1)\right)n^{3/2}.
   \]
9. The explicit algebraic lower construction for \(M_5(n)\).
10. The algebraic examples contain \(\Theta(n^2)\) copies of \(C_4\) and require \(\Omega(n^{3/2})\) edge deletions to become \(C_4\)-free.

**Plausible but unproved**

A natural conjecture suggested by the bipartite construction is
\[
M_5(n)=\left(\frac12+o(1)\right)n^{3/2}.
\]
A sufficient missing statement is:

> Every triangle-free, \(C_5\)-free, \(K_{2,3}\)-free graph has at most  
> \((\tfrac12+o(1))n^{3/2}\) edges.

The triangle bound reduces the general \(m=5\) problem to this statement up to \(O(n)\) deleted edges. I have not proved it, and no argument above rules out a nonbipartite construction with a larger constant.

**Dead ends**

1. Pure second-moment or spectral-radius estimates recover only the Kővári–Sós–Turán constant.
2. Reducing \(\mathcal F_5\)-free graphs to high-girth graphs by deleting \(o(n^{3/2})\) edges is false.
3. Codegree saturation does not by itself assemble a forbidden five-vertex subgraph: the bipartite algebraic examples have codegree \(2\) for almost all same-side pairs but remain \(\mathcal F_5\)-free.
4. Exact Route 2 optimization for \(m=4\) is exactly the unresolved exact \(C_4\) extremal problem.

## Self-Audit

1. **The arbitrary-\(n\) lower bound for \(Z_5(n)\) invokes the prime number theorem.**  
   This theorem was not reproved here. It is a standard rigorous result and is needed only to pass from the explicit sequence \(n=q^2-1\) to every sufficiently large \(n\). The infinite-sequence lower bound is independent of this invocation.

2. **Loop removal in the finite-field construction is delicate.**  
   The degree can fall by at most one because only the vertex’s own quotient class can be a loop. Codegrees cannot increase, and the \(C_4\)-count argument explicitly discards the \(O(q^3)\) endpoint incidences where loop removal can lower a codegree.

3. **The strongest desired \(m=5\) upper bound remains unproved.**  
   Nothing here establishes the conjectural constant \(1/2\) for unrestricted graphs; the rigorous upper constant remains \(\sqrt2/2\). This is a limitation, not a hidden inference: all statements using the \(1/2\) upper constant are explicitly restricted to bipartite graphs.

## Computations To Verify

```python
from itertools import combinations

def is_Fm_free(adj, m):
    """adj is a list of sets; tests whether no m-set has minimum degree >= 2."""
    n = len(adj)
    for S in combinations(range(n), m):
        Sset = set(S)
        if all(len(adj[v] & Sset) >= 2 for v in S):
            return False
    return True

def triangle_count(adj):
    n = len(adj)
    return sum(
        1 for a, b, c in combinations(range(n), 3)
        if b in adj[a] and c in adj[a] and c in adj[b]
    )

def codegree(adj, u, v):
    return len(adj[u] & adj[v])

def count_C4_bipartite(adj, left):
    """Each C4 has a unique pair of opposite left vertices."""
    ans = 0
    for u, v in combinations(left, 2):
        c = codegree(adj, u, v)
        ans += c * (c - 1) // 2
    return ans
```

Finite-field construction for odd prime \(q\):

```python
def canon_pm(v, q):
    """Canonical representative modulo multiplication by +/-1."""
    a, b = v
    w = ((-a) % q, (-b) % q)
    return min((a, b), w)

def furedi_t2_graph(q):
    """
    J(q,2) for an odd prime q.
    Classes are nonzero vectors modulo +/-1.
    """
    reps = sorted({
        canon_pm((a, b), q)
        for a in range(q)
        for b in range(q)
        if (a, b) != (0, 0)
    })
    N = len(reps)
    adj = [set() for _ in range(N)]

    for i, j in combinations(range(N), 2):
        a, b = reps[i]
        x, y = reps[j]
        dot = (a*x + b*y) % q
        if dot in (1, q-1):  # +/-1
            adj[i].add(j)
            adj[j].add(i)

    return adj, reps

def bipartite_double_cover(adjJ):
    s = len(adjJ)
    adjB = [set() for _ in range(2*s)]
    for u in range(s):
        for v in adjJ[u]:
            if u < v:
                # u_L -- v_R
                adjB[u].add(s+v)
                adjB[s+v].add(u)
                # v_L -- u_R
                adjB[v].add(s+u)
                adjB[s+u].add(v)
    return adjB

for q in [3, 5, 7]:
    J, reps = furedi_t2_graph(q)
    B = bipartite_double_cover(J)
    N = len(B)
    E = sum(map(len, B)) // 2

    assert N == q*q - 1
    assert E >= N*(q-1)//2

    # Same-side codegrees must be at most two.
    s = len(J)
    assert all(codegree(B, u, v) <= 2
               for u, v in combinations(range(s), 2))
    assert all(codegree(B, u, v) <= 2
               for u, v in combinations(range(s, 2*s), 2))

    # Direct five-set check; practical for q <= 7.
    assert is_Fm_free(B, 5)

    c4 = count_C4_bipartite(B, range(s))
    print(q, N, E, c4)
```

Exhaustive verification of the triangle lemma and small extremal values:

```python
def graph_from_mask(n, mask):
    pairs = list(combinations(range(n), 2))
    adj = [set() for _ in range(n)]
    for bit, (u, v) in enumerate(pairs):
        if (mask >> bit) & 1:
            adj[u].add(v)
            adj[v].add(u)
    return adj

def exhaustive_M(n, m):
    pairs = list(combinations(range(n), 2))
    best = -1
    best_masks = []
    max_triangles = 0

    for mask in range(1 << len(pairs)):
        e = mask.bit_count()
        if e < best:
            continue
        adj = graph_from_mask(n, mask)
        if is_Fm_free(adj, m):
            max_triangles = max(max_triangles, triangle_count(adj))
            if e > best:
                best = e
                best_masks = [mask]
            elif e == best:
                best_masks.append(mask)

    return best, best_masks, max_triangles

# Feasible through n=7 with straightforward optimization.
for n in range(5, 8):
    M5, masks, maxT = exhaustive_M(n, 5)
    assert maxT <= n
    print("n =", n, "M5 =", M5, "max triangles =", maxT)

# For m=4, compare against direct C4-free codegree test.
def is_C4_free(adj):
    n = len(adj)
    return all(codegree(adj, u, v) <= 1
               for u, v in combinations(range(n), 2))

for n in range(4, 8):
    for mask in range(1 << (n*(n-1)//2)):
        adj = graph_from_mask(n, mask)
        assert is_Fm_free(adj, 4) == is_C4_free(adj)
```

To verify that the algebraic examples are far from \(C_4\)-free, enumerate their \(C_4\)'s and solve the edge-hitting-set ILP:

```python
# Variables z_e in {0,1}, one for each edge.
# For every enumerated C4 C:
#     sum(z_e for e in E(C)) >= 1
# Minimize sum_e z_e.
#
# Compare the optimum with N**1.5.
# The proof predicts a positive-order ratio, not o(N**1.5).
```

## Route Diagnosis

Route 2 successfully gives universal codegree bounds, local assembly restrictions, a sharp bipartite \(m=5\) asymptotic, and explicit constructions showing that short cycles—especially \(C_4\)'s—can be abundant without producing the forbidden exact-order core. It does not solve the full problem because \(m=4\) is precisely the exact \(C_4\) Turán problem. Even after setting that barrier aside, codegree moments alone cannot distinguish the algebraic \(\mathcal F_5\)-free examples from configurations that do contain a forbidden set.

The most concrete next target is the sparse stability statement
\[
e(H)\le\left(\frac12+o(1)\right)n^{3/2}
\]
for triangle-free, \(C_5\)-free, \(K_{2,3}\)-free graphs. Proving it would determine the leading correction constant for \(k=3\); disproving it would require a genuinely nonbipartite construction beating the algebraic double covers. For the exact all-parameter problem, however, a fresh attempt must first confront—not bypass—the exact \(C_4\) extremal barrier.