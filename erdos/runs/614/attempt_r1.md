STATUS: BLOCKED
## Result

Route 1 yields an exact reduction to the global \(2\)-core, a structural description of all edge-minimal forbidden certificates, explicit reduced forbidden families for \(m\le 6\), and a new exact near-boundary value:
\[
f(k+3,k)=
\begin{cases}
2,&k=1,\\
4,&k=2,\\
2k+1,&k\ge3.
\end{cases}
\]
For \(k\ge3\), the extremal complements on \(k+3\) vertices are classified below. However, the full problem is blocked decisively: when \(k=2\), Route 1 becomes the exact \(C_4\)-extremal problem. Moreover, dense \(C_4\)-free and high-girth graphs can have their entire vertex set as one large, complicated \(2\)-core, so no bounded-block or cactus decomposition can hold.

## Complete Argument

Let
\[
m=k+2,\qquad
M_m(n)=\operatorname{ex}(n,\mathcal F_m),
\]
where \(\mathcal F_m\) is the family of \(m\)-vertex graphs of minimum degree at least \(2\). Thus
\[
f(n,k)=\binom n2-M_{k+2}(n).
\]

Throughout the nontrivial structural discussion, \(m\ge3\).

### 1. Exact reduction to the \(2\)-core

Let \(C(H)\) denote the \(2\)-core of a graph \(H\), obtained by repeatedly deleting vertices of current degree at most \(1\).

#### Lemma 1
A graph \(H\) contains an \(m\)-vertex subgraph of minimum degree at least \(2\) if and only if \(H[C(H)]\) does.

#### Proof

The reverse implication is immediate because \(H[C(H)]\subseteq H\).

For the forward implication, suppose \(S\subseteq V(H)\), \(|S|=m\), and
\[
\delta(H[S])\ge2.
\]
During the iterative deletion process defining \(C(H)\), no vertex of \(S\) can be the first deleted vertex belonging to \(S\): before any vertex of \(S\) has been deleted, every vertex of \(S\) still has at least its two neighbors in \(S\). Therefore all vertices of \(S\) survive the entire process, so \(S\subseteq C(H)\). ∎

This gives an exact extremal decomposition. Define
\[
M_m^{\mathrm{core}}(r)
=
\max\bigl\{
e(Q): |V(Q)|=r,\ \delta(Q)\ge2,\ Q\text{ is }\mathcal F_m\text{-free}
\bigr\},
\]
with the maximum interpreted as \(-\infty\) if no such graph exists.

#### Proposition 2
For \(n\ge1\),
\[
\boxed{
M_m(n)=
\max\left\{
n-1,\ 
\max_{3\le r\le n}
\left(M_m^{\mathrm{core}}(r)+n-r\right)
\right\}.
}
\]

#### Proof

Let \(H\) be \(\mathcal F_m\)-free and let \(r=|C(H)|\).

If \(r=0\), then \(H\) is a forest: any cycle would survive the deletion process. Hence \(e(H)\le n-1\).

Suppose \(r>0\). During the deletion process, each of the \(n-r\) deleted vertices has current degree at most \(1\). Charge every edge outside \(H[C(H)]\) to the endpoint deleted first. Each deleted vertex receives at most one charge, so
\[
e(H)-e(H[C(H)])\le n-r.
\]
By Lemma 1, \(H[C(H)]\) is also \(\mathcal F_m\)-free. Therefore
\[
e(H)\le M_m^{\mathrm{core}}(r)+n-r.
\]

Conversely, a tree gives \(n-1\) edges. Given any admissible core \(Q\) on \(r\) vertices, attach each of the remaining \(n-r\) vertices as a leaf to a fixed vertex of \(Q\). The resulting graph has
\[
e(Q)+n-r
\]
edges, has \(2\)-core exactly \(Q\), and is \(\mathcal F_m\)-free by Lemma 1. ∎

Thus acyclic attachments are completely understood: each contributes at most one edge. The unsolved content is entirely in the possible large \(2\)-cores.

A useful elementary construction follows. Take \(K_{m-1}\) and attach every remaining vertex as a leaf. Hence
\[
M_m(n)\ge \binom{m-1}{2}+n-m+1
= n+\frac{(m-1)(m-4)}2.
\]

### 2. Edge-minimal forbidden certificates

The family \(\mathcal F_m\) can be replaced by a much smaller structural family.

Let \(\mathcal T_m\) consist of the \(m\)-vertex graphs \(T\) such that

1. \(\delta(T)\ge2\), and
2. every edge of \(T\) has at least one endpoint of degree exactly \(2\).

#### Lemma 3
A graph is \(\mathcal F_m\)-free if and only if it contains no member of \(\mathcal T_m\) as a subgraph.

#### Proof

Every member of \(\mathcal T_m\) belongs to \(\mathcal F_m\).

Conversely, suppose \(H\) contains an \(m\)-vertex subgraph \(F\) with \(\delta(F)\ge2\). Delete edges from \(F\), while preserving minimum degree at least \(2\), until this is no longer possible. Let the resulting spanning subgraph be \(T\).

If \(xy\in E(T)\) and both \(d_T(x),d_T(y)\ge3\), then deleting \(xy\) would leave every degree at least \(2\), contrary to minimality. Thus every edge has an endpoint of degree exactly \(2\), and \(T\in\mathcal T_m\). ∎

The connected members of \(\mathcal T_m\) admit a kernel description.

#### Lemma 4
Let \(T\in\mathcal T_m\), and let
\[
B=\{v:d_T(v)\ge3\},\qquad D=V(T)\setminus B.
\]
Then:

1. \(B\) is independent;
2. every vertex of \(D\) has degree exactly \(2\);
3. every connected component of \(T\) is either a cycle, or is obtained from a connected multigraph of minimum degree at least \(3\) by subdividing every edge at least once;
4. loops in the multigraph kernel are subdivided at least twice;
5. if \(b=|B|\), then
   \[
   \boxed{b\le\left\lfloor\frac{2m}{5}\right\rfloor.}
   \]

#### Proof

Every vertex has degree at least \(2\). By the definition of \(\mathcal T_m\), no edge can have both endpoints in \(B\), proving that \(B\) is independent. Hence all remaining vertices have degree exactly \(2\).

Consider a connected component \(J\). If \(B\cap V(J)=\varnothing\), then \(J\) is a connected \(2\)-regular graph, hence a cycle.

Otherwise, consider the components of \(J[D]\). Each has maximum degree at most \(2\). Such a component cannot be a cycle, because all of its vertices would already have degree \(2\) inside that cycle, so it would have no edge to \(B\), contradicting the connectedness of \(J\). Therefore every component of \(J[D]\) is a path, possibly a single vertex.

Suppress each such path to one edge joining its endpoint vertices in \(B\). The resulting object is a connected multigraph. Its degrees equal the degrees of the corresponding vertices in \(B\), hence are at least \(3\). Since \(B\) is independent, every kernel edge has at least one subdivision vertex. A loop cannot have only one subdivision vertex in a simple graph, because that would require two copies of the same edge between the branch vertex and the subdivision vertex. Thus a loop has at least two subdivision vertices.

Finally, writing \(d=|D|=m-b\), every edge incident to \(B\) joins \(B\) to \(D\). Therefore
\[
3b\le \sum_{v\in B}d_T(v)=e_T(B,D)\le 2d=2(m-b).
\]
Hence \(5b\le2m\). ∎

Thus every minimal \(m\)-vertex obstruction has at least \(3m/5\) vertices of degree exactly \(2\). It is a union of cycles and subdivisions of bounded-order multigraph kernels, rather than an arbitrary minimum-degree-two graph.

### 3. Explicit reduced forbidden families for \(m\le6\)

Write \(C_a\vee C_b\) for two cycles sharing exactly one vertex, and let \(\Theta_{2,2,3}\) be the graph consisting of three internally disjoint paths of lengths \(2,2,3\) between the same two endpoints.

#### Proposition 5
The following ordinary forbidden-subgraph descriptions hold:
\[
\begin{aligned}
\mathcal F_3\text{-free}
&\iff C_3\text{-free},\\
\mathcal F_4\text{-free}
&\iff C_4\text{-free},\\
\mathcal F_5\text{-free}
&\iff \{C_5,K_{2,3},C_3\vee C_3\}\text{-free},\\
\mathcal F_6\text{-free}
&\iff
\{C_6,\ C_3\mathbin{\dot\cup}C_3,\ C_3\vee C_4,\ K_{2,4},\
\Theta_{2,2,3}\}\text{-free}.
\end{aligned}
\]

#### Proof

By Lemma 3, it suffices to classify the members of \(\mathcal T_m\).

If there are no branch vertices, every component is a cycle. Partitions of \(m\) into cycle orders at least \(3\) give:

- \(C_3\) for \(m=3\);
- \(C_4\) for \(m=4\);
- \(C_5\) for \(m=5\);
- \(C_6\) and \(C_3\dot\cup C_3\) for \(m=6\).

A connected component containing exactly one branch vertex has a one-vertex multigraph kernel. Its kernel edges are loops. Since a loop contributes \(2\) to the kernel degree and needs at least two subdivision vertices, at least two loops are required, using at least five vertices in total. Therefore no such obstruction occurs for \(m\le4\).

For \(m=5\), exactly two minimally subdivided loops are possible, giving \(C_3\vee C_3\).

For \(m=6\), two loops use five subdivision vertices, distributed as \(2+3\), giving \(C_3\vee C_4\). A branch component on five vertices together with one additional component is impossible, since every additional minimum-degree-two component has at least three vertices.

Now suppose there are two branch vertices. For \(m=5\), there are three degree-two vertices. The two branch vertices must have degree at least \(3\). The only possibility is three parallel kernel edges, each subdivided once, yielding \(K_{2,3}\).

For \(m=6\), there are four degree-two vertices. The two branch vertices must lie in the same component. If the kernel contained a loop at one branch vertex, then either the other branch vertex would require at least three connecting kernel edges, using at least \(2+3=5\) subdivision vertices, or it too would need a loop, again using at least five. Thus there are no loops.

There must therefore be either:

- four parallel kernel edges, each subdivided once, giving \(K_{2,4}\); or
- three parallel kernel edges, with subdivision counts \(1,1,2\), giving \(\Theta_{2,2,3}\).

Lemma 4 gives at most two branch vertices when \(m\le6\), so the list is complete. ∎

In particular,
\[
\boxed{
M_5(n)=\operatorname{ex}\bigl(n,\{C_5,K_{2,3},C_3\vee C_3\}\bigr).
}
\]

### 4. Extension and intersection restrictions on cyclic cores

#### Lemma 6
Let \(H\) be \(\mathcal F_m\)-free.

1. If \(A_1,\dots,A_s\) each span a subgraph of minimum degree at least \(2\), then
   \[
   \left|\bigcup_i A_i\right|\ne m.
   \]
2. If \(|A|=m-1\) and \(\delta(H[A])\ge2\), then every \(x\notin A\) has at most one neighbor in \(A\).

#### Proof

For the first assertion, every vertex in \(\bigcup_i A_i\) belongs to at least one \(A_i\) and retains at least two neighbors from that \(A_i\) inside the union. If the union had order \(m\), it would violate \(\mathcal F_m\)-freeness.

For the second assertion, if \(x\) had two neighbors in \(A\), then every vertex of \(A\cup\{x\}\) would have at least two neighbors in that set, which has order \(m\). ∎

Consequently, if an \(\mathcal F_m\)-free graph \(H\) contains such an \((m-1)\)-vertex set \(A\), then
\[
e(H)\le
\binom{m-1}{2}
+(n-m+1)
+M_m(n-m+1).
\]

For \(m=5\), every \(C_4\) is therefore “sealed”: every outside vertex has at most one neighbor on its four vertices. Hence any \(\mathcal F_5\)-free graph containing a \(C_4\) satisfies
\[
e(H)\le M_5(n-4)+n+2.
\]
This is rigorous but too weak, by itself, to determine \(M_5(n)\).

### 5. Exact determination on \(n=m+1\) vertices

We now determine \(M_m(m+1)\).

#### Theorem 7
For \(m\ge3\),
\[
\boxed{
M_m(m+1)=
\begin{cases}
4,&m=3,\\
6,&m=4,\\
\binom{m-1}{2}+2,&m\ge5.
\end{cases}
}
\]

For \(m\ge5\), all extremal graphs are of one of the following two types:

1. a clique \(K_{m-1}\) together with two nonadjacent pendant vertices, each attached to an arbitrary clique vertex; or
2. a clique \(K_{m-1}\) with a pendant path of length \(2\) attached to a clique vertex.

#### Proof

Put \(N=m+1\). An \(N\)-vertex graph \(H\) is \(\mathcal F_m\)-free precisely when
\[
\delta(H-x)\le1\qquad\text{for every }x\in V(H),
\]
because the \(m\)-sets are exactly the sets \(V(H)\setminus\{x\}\).

Let
\[
A=\{v:d_H(v)\le1\},\quad
B=\{v:d_H(v)=2\},\quad
C=\{v:d_H(v)\ge3\}.
\]

##### Case 1: \(|A|\ge2\)

Choose distinct \(a,b\in A\). All edges not contained in \(H-\{a,b\}\) number at most
\[
d(a)+d(b)\le2.
\]
Therefore
\[
e(H)\le \binom{N-2}{2}+2.
\]

##### Case 2: \(|A|=1\)

Let \(A=\{a\}\). Since \(\delta(H-a)\le1\), there is \(u\ne a\) such that
\[
d_{H-a}(u)\le1.
\]
No vertex other than \(a\) has degree at most \(1\) in \(H\), so necessarily
\[
d_H(u)=2,\qquad au\in E(H).
\]
Moreover, \(a\) cannot be isolated, so \(d_H(a)=1\).

The number of edges incident to at least one of \(a,u\) is
\[
d(a)+d(u)-1=2.
\]
Thus again
\[
e(H)\le \binom{N-2}{2}+2.
\]

##### Case 3: \(A=\varnothing\)

Here \(\delta(H)\ge2\). For every \(x\), a vertex witnessing \(\delta(H-x)\le1\) must be a degree-two neighbor of \(x\). Hence every vertex has a neighbor in \(B\). In particular, every vertex of \(B\) has a neighbor in \(B\).

Let
\[
t=|B|,\qquad r=|C|=N-t,\qquad
q=e(H[B]),\qquad p=e_H(B,C).
\]
Because \(H[B]\) has no isolated vertex,
\[
q\ge\left\lceil\frac t2\right\rceil.
\]
Every vertex of \(C\) has a neighbor in \(B\), so \(p\ge r\). On the other hand, summing degrees over \(B\) gives
\[
2t=2q+p.
\]
Thus \(p\le t\), and consequently \(r\le t\).

If \(r=0\), then every vertex has degree exactly \(2\), so \(e(H)=N\).

If \(r\ge1\), then \(1\le r\le N/2\), and
\[
\begin{aligned}
e(H)
&=e(H[C])+q+p\\
&=e(H[C])+2t-q\\
&\le \binom r2+\left\lfloor\frac{3t}{2}\right\rfloor\\
&\le \binom r2+\frac32(N-r)\\
&=\frac{r^2-4r+3N}{2}.
\end{aligned}
\]
The last expression is convex in \(r\), so on \(1\le r\le N/2\) its maximum is attained at an endpoint. The two endpoint bounds are
\[
\frac{3N-3}{2}
\quad\text{and}\quad
\frac{N^2}{8}+\frac N2.
\]
For every \(N\ge6\), both are at most
\[
\binom{N-2}{2}+2=\frac{N^2-5N+10}{2}.
\]
Indeed, the respective differences are
\[
\frac{N^2-8N+13}{2}\ge0
\]
and
\[
\frac{3N^2-24N+40}{8}\ge0,
\]
with both expressions increasing from positive values at \(N=6\). Also
\[
N\le\binom{N-2}{2}+2
\]
for \(N\ge6\).

Thus, for \(N\ge6\),
\[
e(H)\le\binom{N-2}{2}+2.
\]
Equality is attained by a \(K_{N-2}\) with either two pendant vertices or one attached pendant path of length two. Every \(N-1\) vertex set contains a vertex of degree at most \(1\), so these graphs are admissible.

The equality classification follows from Cases 1 and 2. In Case 1, equality forces \(H-\{a,b\}\) to be complete, \(a,b\) to be nonadjacent, and both to have degree \(1\). In Case 2, equality forces \(H-\{a,u\}\) to be complete, while \(a-u-w\) is a pendant path for some clique vertex \(w\). Case 3 is strictly below the bound for \(N\ge6\).

For \(N=5\), the preceding argument gives \(e(H)\le6\). Equality is attained by two triangles sharing one central vertex: deleting the center leaves two disjoint edges, while deleting any other vertex leaves its paired vertex of degree \(1\).

For \(N=4\), the argument gives \(e(H)\le4\), attained by \(C_4\). ∎

Returning to the original parameters \(m=k+2\) gives:

#### Corollary 8
For \(k\ge1\),
\[
\boxed{
f(k+3,k)=
\begin{cases}
2,&k=1,\\
4,&k=2,\\
2k+1,&k\ge3.
\end{cases}
}
\]

#### Proof

Use
\[
f(k+3,k)=\binom{k+3}{2}-M_{k+2}(k+3).
\]
For \(k\ge3\),
\[
\binom{k+3}{2}
-\left(\binom{k+1}{2}+2\right)
=2k+1.
\]
The two exceptional values follow from \(M_3(4)=4\) and \(M_4(5)=6\). ∎

### 6. Why Route 1 cannot presently finish the problem

For \(m=4\), Proposition 5 gives exactly
\[
M_4(n)=\operatorname{ex}(n,C_4).
\]
Thus a complete determination of \(f(n,k)\) would in particular determine \(\operatorname{ex}(n,C_4)\) for every \(n\).

The \(2\)-core reduction does not weaken this obstruction. A \(C_4\)-free graph can have minimum degree much larger than \(2\), so its entire vertex set is its \(2\)-core. Dense polarity and high-girth constructions provide large cyclic cores with no cactus or bounded-block decomposition. Hence Proposition 2 reduces the problem to the extremal density of precisely the kind of large core that remains unresolved.

## Self-Audit

1. **The small-\(m\) template classification is the point most vulnerable to an omitted topology.**  
   I believe it is complete because Lemma 4 reduces the enumeration to at most two branch vertices for \(m\le6\), after which all loop and parallel-edge kernels are explicitly exhausted. The finite verification code below independently checks the list.

2. **The \(n=m+1\) upper bound relies on a global degree partition that could easily suffer an off-by-one error.**  
   The crucial implication is exact: if \(\delta(H-x)\le1\) and \(\delta(H)\ge2\), its witness must be a degree-two neighbor of \(x\). The three cases \(|A|\ge2\), \(|A|=1\), and \(A=\varnothing\) are exhaustive, and the endpoint inequalities are displayed explicitly.

3. **The \(2\)-core formula is exact but does not control the hard part.**  
   Its proof is solid—the witness survives every degree-\(\le1\) deletion, and at most one removed edge is charged to each deleted vertex—but it leaves \(M_m^{\mathrm{core}}(r)\) unresolved. In particular, it does not constitute an exact solution of the original problem.

## Computations To Verify

The following Python exhaustively verifies:

- \(M_m(m+1)\) for \(3\le m\le6\);
- the reduced template lists for \(m=5,6\);
- survival of every forbidden witness inside the \(2\)-core;
- the extremal classification for \(N=m+1\), \(m=5,6\).

```python
from itertools import combinations, permutations
from math import comb

def pairs(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]

def adjacency_masks(mask, n):
    adj = [0] * n
    for i, (u, v) in enumerate(pairs(n)):
        if (mask >> i) & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    return adj

def has_witness(mask, n, m, allowed=None):
    """True iff some m-set in allowed has induced minimum degree >= 2."""
    adj = adjacency_masks(mask, n)
    if allowed is None:
        allowed = list(range(n))
    else:
        allowed = list(allowed)
    if len(allowed) < m:
        return False

    for S in combinations(allowed, m):
        sbits = sum(1 << v for v in S)
        if all((adj[v] & sbits).bit_count() >= 2 for v in S):
            return True
    return False

def two_core(mask, n):
    adj = adjacency_masks(mask, n)
    alive = (1 << n) - 1

    while True:
        low = [
            v for v in range(n)
            if ((alive >> v) & 1)
            and (adj[v] & alive).bit_count() <= 1
        ]
        if not low:
            break
        for v in low:
            alive &= ~(1 << v)

    return [v for v in range(n) if (alive >> v) & 1]

def exact_M(n, m):
    E = len(pairs(n))
    best = -1
    extremals = []
    for mask in range(1 << E):
        if not has_witness(mask, n, m):
            e = mask.bit_count()
            if e > best:
                best = e
                extremals = [mask]
            elif e == best:
                extremals.append(mask)
    return best, extremals

# Verify Theorem 7 through m=6.
expected = {
    3: 4,
    4: 6,
    5: comb(4, 2) + 2,  # 8
    6: comb(5, 2) + 2,  # 12
}
for m, target in expected.items():
    value, _ = exact_M(m + 1, m)
    assert value == target, (m, value, target)

def cycle_edges(vertices):
    return [
        (vertices[i], vertices[(i + 1) % len(vertices)])
        for i in range(len(vertices))
    ]

templates = {
    5: [
        cycle_edges([0, 1, 2, 3, 4]),  # C5
        [(u, v) for u in [0, 1] for v in [2, 3, 4]],  # K2,3
        # Two triangles sharing vertex 0
        [(0, 1), (1, 2), (2, 0),
         (0, 3), (3, 4), (4, 0)],
    ],
    6: [
        cycle_edges([0, 1, 2, 3, 4, 5]),  # C6
        # Two disjoint triangles
        [(0, 1), (1, 2), (2, 0),
         (3, 4), (4, 5), (5, 3)],
        # C3 and C4 sharing vertex 0
        [(0, 1), (1, 2), (2, 0),
         (0, 3), (3, 4), (4, 5), (5, 0)],
        # K2,4
        [(u, v) for u in [0, 1] for v in [2, 3, 4, 5]],
        # Theta with path lengths 2,2,3 between 0 and 1
        [(0, 2), (2, 1),
         (0, 3), (3, 1),
         (0, 4), (4, 5), (5, 1)],
    ],
}

def all_relabelled_masks(n, edge_lists):
    P = pairs(n)
    idx = {e: i for i, e in enumerate(P)}
    result = set()
    for edges in edge_lists:
        for p in permutations(range(n)):
            mask = 0
            for u, v in edges:
                a, b = sorted((p[u], p[v]))
                mask |= 1 << idx[(a, b)]
            result.add(mask)
    return result

# Verify that minimum degree >= 2 is equivalent to containing
# one listed spanning template, for m=5 and m=6.
for m in [5, 6]:
    relabelled = all_relabelled_masks(m, templates[m])
    for mask in range(1 << len(pairs(m))):
        adj = adjacency_masks(mask, m)
        md2 = all(adj[v].bit_count() >= 2 for v in range(m))
        contains_template = any((mask & T) == T for T in relabelled)
        assert md2 == contains_template, (m, mask)

# Verify Lemma 1 exhaustively for small orders.
for n in range(3, 7):
    for m in range(3, n + 1):
        for mask in range(1 << len(pairs(n))):
            core = two_core(mask, n)
            assert has_witness(mask, n, m) == \
                   has_witness(mask, n, m, core)

def is_clique(adj, vertices):
    V = set(vertices)
    return all(
        v in adj_set
        for i, u in enumerate(vertices)
        for v in vertices[i + 1:]
        for adj_set in [{x for x in range(len(adj))
                         if (adj[u] >> x) & 1}]
    )

def near_boundary_extremal_type(mask, n):
    adj = adjacency_masks(mask, n)
    deg = [a.bit_count() for a in adj]
    low = [v for v in range(n) if deg[v] <= 1]

    # Type 1: clique plus two pendant vertices.
    if len(low) == 2:
        a, b = low
        R = [v for v in range(n) if v not in {a, b}]
        if (deg[a] == deg[b] == 1
            and not ((adj[a] >> b) & 1)
            and is_clique(adj, R)):
            return 1

    # Type 2: clique plus attached path of length two.
    if len(low) == 1:
        a = low[0]
        if deg[a] == 1:
            u = (adj[a] & -adj[a]).bit_length() - 1
            R = [v for v in range(n) if v not in {a, u}]
            if deg[u] == 2 and is_clique(adj, R):
                return 2

    return None

# Verify the equality classification for m=5,6.
for m in [5, 6]:
    n = m + 1
    best, extremals = exact_M(n, m)
    assert best == comb(n - 2, 2) + 2
    assert all(near_boundary_extremal_type(H, n) in {1, 2}
               for H in extremals)
```

## Route Diagnosis

### Proved ledger

- A forbidden \(m\)-set always survives into the global \(2\)-core.
- All edges outside the \(2\)-core contribute at most one edge per outside vertex.
- \(M_m(n)\) has the exact core-excess formula in Proposition 2.
- Every forbidden graph contains a spanning edge-minimal certificate whose every edge touches a degree-two vertex.
- Such certificates are cycles or subdivisions of minimum-degree-three multigraph kernels, with at most \(2m/5\) branch vertices.
- The reduced forbidden families for \(m=3,4,5,6\) are explicitly classified.
- Cyclic sets of total union order exactly \(m\) are prohibited, and every \((m-1)\)-vertex core is sealed from outside vertices by cross-degree at most one.
- \(M_m(m+1)\), hence \(f(k+3,k)\), is determined exactly, including extremal complements for \(k\ge3\).

### Plausible but unproved

- For \(m=5\), the combination of \(K_{2,3}\)-freeness, bowtie-freeness, \(C_5\)-freeness, and the sealing of every \(C_4\) may yield a useful stability theorem separating a nearly \(C_4\)-free regime from a bounded-core-attachment regime.
- Minimal-kernel enumeration may permit systematic exact results for \(n=m+s\) with fixed \(s\), but no proof for general \(s\) was obtained.

### Dead ends

- **Bounded cyclic blocks or cactus structure:** false. High-girth regular graphs can be large, highly connected \(2\)-cores while remaining \(\mathcal F_m\)-free.
- **Deleting acyclic attachments and inducting on the core:** exact but insufficient; for \(m=4\), the remaining core problem is exactly \(\operatorname{ex}(n,C_4)\).
- **Ear-decomposition prefix counting:** an ear union is indeed a minimum-degree-two subgraph, but long initial cycles and large high-girth blocks can skip the target order \(m\), so this gives no universal decomposition theorem.
- **The conditional recurrence obtained from an \((m-1)\)-vertex core:** rigorous but too weak asymptotically.

### Precise block

A complete solution must determine
\[
M_4(n)=\operatorname{ex}(n,C_4)
\]
for every \(n\). This remains open and is of comparable strength to the original problem. Route 1 does not bypass it because extremal or near-extremal \(C_4\)-free graphs may themselves be large \(2\)-cores with no low-degree or bounded-block decomposition.

A fresh Route 1 attempt should focus on a restricted target, particularly \(m=5\), using
\[
\mathcal F_5\equiv\{C_5,K_{2,3},C_3\vee C_3\}
\]
and the sealing property of \(C_4\)'s. For the full all-parameter problem, however, an independent breakthrough on exact \(C_4\) extremal theory is unavoidable.