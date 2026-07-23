STATUS: BLOCKED

## Result

Route 4 succeeds completely in the near-extremal regime. I prove that every sufficiently large \(H_5\)-free graph with \((1/4-o(1))N^2\) red edges contains a red-independent set of size \((1/2-o(1))N\), hence its blue complement contains a clique of that size and therefore every \(m\)-edge target once \(N\) is a sufficiently large constant multiple of \(m\). This strengthens ordinary stability by controlling concentrated exceptional red edges. I also reduce the target problem, using the BGS theorem, to targets whose every connected component is nonbipartite, and show that any remaining counterexample must have uniformly small red edge-codegrees and \(o(N^3)\) red triangles, hence be edge-close to triangle-free. The route then blocks: neither stability nor the bipartite-target theorem gives the robust, rooted embedding needed for complements of such subextremal, almost-triangle-free red graphs.

## Complete Argument

Write \(J=H_5=K_4^*\), and let \(F\) be the red graph.

### 1. Bipartite connected components can be peeled off

We use the known BGS theorem:

> There is a constant \(C_{\mathrm{bip}}\) such that
> \[
> R(J,L)\le C_{\mathrm{bip}}e(L)
> \]
> for every bipartite graph \(L\) without isolated vertices.

Let \(\mathcal N\) be the class of no-isolate graphs every connected component of which is nonbipartite.

#### Lemma 1
The full Ramsey-size-linearity problem for \(J\) is equivalent to proving a linear bound only for targets in \(\mathcal N\).

#### Proof
One direction is immediate. Conversely, suppose there is \(C_{\mathcal N}\) such that
\[
R(J,L)\le C_{\mathcal N}e(L)\qquad(L\in\mathcal N).
\]

Given an arbitrary no-isolate target \(H\), let \(H_{\mathrm{bip}}\) be the union of its bipartite connected components and \(H_{\mathcal N}\) the union of its nonbipartite connected components. Put
\[
m_{\mathrm{bip}}=e(H_{\mathrm{bip}}),\qquad
m_{\mathcal N}=e(H_{\mathcal N}).
\]

After rounding the two constants upward to integers, partition an ambient complete graph into disjoint sets of orders
\[
C_{\mathrm{bip}}m_{\mathrm{bip}}
\quad\text{and}\quad
C_{\mathcal N}m_{\mathcal N},
\]
omitting an empty part when the corresponding target is empty.

If the whole red graph is \(J\)-free, so are the two induced red graphs. The first block contains a blue \(H_{\mathrm{bip}}\), and the second a blue \(H_{\mathcal N}\). These copies are vertex-disjoint, and no edges are required between distinct connected components. Their union is a blue copy of \(H\). Therefore
\[
R(J,H)\le
C_{\mathrm{bip}}m_{\mathrm{bip}}+
C_{\mathcal N}m_{\mathcal N}
\le
\max\{C_{\mathrm{bip}},C_{\mathcal N}\}e(H).
\]
∎

This is the one decomposition for which compatibility is automatic. Decomposing a connected target into bipartite edge-subgraphs would not have this property.

Every \(H\in\mathcal N\) satisfies the stronger vertex bound
\[
v(H)\le e(H).
\]
Indeed, every connected nonbipartite component contains a cycle, and hence has at least as many edges as vertices.

---

### 2. The exact local constraint imposed by \(H_5\)-freeness

For a red edge \(cd\), write
\[
A_{cd}=N_F(c)\cap N_F(d).
\]

#### Lemma 2: Common-neighborhood lemma
If \(F\) is \(J\)-free, then every vertex \(x\notin\{c,d\}\) has at most one red neighbor in \(A_{cd}\). In particular,
\[
\Delta(F[A_{cd}])\le 1
\]
and
\[
\alpha(F[A_{cd}])\ge \left\lceil\frac{|A_{cd}|}{2}\right\rceil.
\]

#### Proof
Suppose some \(x\notin\{c,d\}\) has two distinct red neighbors \(a,b\in A_{cd}\). The five vertices \(c,d,a,b,x\) are distinct and contain the red edges
\[
cd,\ ca,\ da,\ cb,\ db,\ ax,\ bx.
\]
These are precisely the seven required edges in the certificate description of \(H_5\). Extra red edges do not matter because copies are not induced. Thus \(F\) would contain \(J\), a contradiction.

The assertion about \(F[A_{cd}]\) follows by taking \(x\in A_{cd}\). A graph of maximum degree at most one is a disjoint union of isolated vertices and edges, so it has an independent set containing at least one vertex from every edge and every isolated vertex, of size at least \(\lceil |A_{cd}|/2\rceil\). ∎

This local lemma is the mechanism that upgrades ordinary stability below.

---

### 3. Concentrated perturbations of a complete bipartite graph

Let \(V(F)=X\sqcup Y\). Define
\[
q=e_{\overline F}(X,Y),
\]
the number of missing red cross-edges. For \(x\in X\), let
\[
\overline d_Y(x)=|\{y\in Y:xy\notin E(F)\}|,
\]
and define \(\overline d_X(y)\) analogously.

#### Lemma 3: Exceptional-vertex concentration
Let \(F\) be \(J\)-free, let \(t>0\), and define
\[
X_0=\{x\in X:\overline d_Y(x)\le t\},\qquad
Y_0=\{y\in Y:\overline d_X(y)\le t\}.
\]

If
\[
q<(|X|-2)(|Y|-2t-1),
\]
then \(F[X_0]\) has no edges. Similarly, if
\[
q<(|Y|-2)(|X|-2t-1),
\]
then \(F[Y_0]\) has no edges.

Moreover,
\[
|X_0|\ge |X|-\frac qt,\qquad
|Y_0|\ge |Y|-\frac qt.
\]

#### Proof
Suppose \(uv\in E(F[X_0])\). Set
\[
A=N_F(u)\cap N_F(v)\cap Y.
\]
Because \(u,v\in X_0\),
\[
|A|\ge |Y|-\overline d_Y(u)-\overline d_Y(v)\ge |Y|-2t.
\]

By Lemma 2, each \(x\in X\setminus\{u,v\}\) has at most one red neighbor in \(A\). Consequently, for each such \(x\), at least \(|A|-1\) pairs \(xy\), \(y\in A\), are missing red cross-edges. These pairs are distinct for different \(x\), so
\[
q\ge (|X|-2)(|A|-1)
   \ge (|X|-2)(|Y|-2t-1),
\]
contradicting the hypothesis. Thus \(F[X_0]\) is edgeless. The proof for \(Y_0\) is symmetric.

Finally,
\[
\sum_{x\in X}\overline d_Y(x)=q.
\]
Every vertex of \(X\setminus X_0\) contributes more than \(t\), so
\[
|X\setminus X_0|<q/t.
\]
The same argument applies to \(Y\). ∎

Thus a small number of missing cross-edges does not merely imply that there are few internal red edges: it implies that every internal red edge is incident to a vertex having large cross-deficiency.

---

### 4. Upgrading Simonovits stability to an almost-half blue clique

We use the standard stability theorem for \(J\), which has chromatic number three:

> For every \(\eta>0\), there are \(\delta_{\mathrm{stab}}>0\) and \(N_{\mathrm{stab}}\) such that every \(J\)-free graph \(F\) on \(N\ge N_{\mathrm{stab}}\) vertices with
> \[
> e(F)\ge \left(\frac14-\delta_{\mathrm{stab}}\right)N^2
> \]
> has a partition \(V(F)=X\sqcup Y\) satisfying
> \[
> e(F[X])+e(F[Y])\le \eta N^2.
> \]

#### Theorem 4: Robust near-extremal independence
For every \(\gamma>0\), there are \(\delta>0\) and \(N_0\) such that every \(J\)-free graph \(F\) on \(N\ge N_0\) vertices satisfying
\[
e(F)\ge \left(\frac14-\delta\right)N^2
\]
has
\[
\alpha(F)\ge \left(\frac12-\gamma\right)N.
\]

#### Proof
It is enough to consider \(0<\gamma<1/4\). Set
\[
\tau=\frac{\gamma}{8}.
\]
Choose
\[
0<\eta<\frac{\gamma^2}{256},
\]
apply stability with this \(\eta\), and then choose
\[
0<\delta\le
\min\left\{\delta_{\mathrm{stab}},\frac{\gamma^2}{256}\right\}.
\]
Put
\[
r=\eta+\delta<\frac{\gamma^2}{128}.
\]

Let \(X\sqcup Y\) be the stability partition, and write
\[
I=e(F[X])+e(F[Y]),\qquad
q=e_{\overline F}(X,Y).
\]
Since
\[
e_F(X,Y)=e(F)-I,
\]
we have
\[
|X||Y|\ge e_F(X,Y)
\ge \left(\frac14-r\right)N^2.
\]
Writing \(|X|=N/2+s\), we obtain
\[
\frac{N^2}{4}-s^2=|X||Y|
\ge \left(\frac14-r\right)N^2,
\]
and hence
\[
|s|\le \sqrt r\,N<\frac{\gamma N}{8}.
\]
Therefore
\[
|X|,|Y|\ge \left(\frac12-\frac{\gamma}{8}\right)N.
\]

Also,
\[
\begin{aligned}
q
 &=|X||Y|-e_F(X,Y)\\
 &=|X||Y|-e(F)+I\\
 &\le \frac{N^2}{4}
    -\left(\frac14-\delta\right)N^2
    +\eta N^2\\
 &\le rN^2.
\end{aligned}
\]

Apply Lemma 3 with \(t=\tau N\). For sufficiently large \(N\), both products
\[
(|X|-2)(|Y|-2\tau N-1),
\qquad
(|Y|-2)(|X|-2\tau N-1)
\]
are much larger than \(rN^2\). Explicitly, their limiting coefficient is at least
\[
\left(\frac12-\frac{\gamma}{8}\right)
\left(\frac12-\frac{3\gamma}{8}\right),
\]
which exceeds \(0.19\) for \(0<\gamma<1/4\), whereas
\[
r<\frac{\gamma^2}{128}\le \frac1{2048}.
\]
Thus Lemma 3 shows that \(X_0\) and \(Y_0\) are both red-independent.

Moreover,
\[
\frac{q}{\tau N}
\le \frac{r}{\tau}N
<\frac{\gamma}{16}N.
\]
Consequently,
\[
|X_0|
\ge |X|-\frac{q}{\tau N}
\ge \left(\frac12-\frac{3\gamma}{16}\right)N
> \left(\frac12-\gamma\right)N.
\]
Hence \(\alpha(F)\ge |X_0|>(1/2-\gamma)N\). ∎

#### Corollary 5: The dense red regime is harmless
There are fixed \(\delta>0\) and \(N_0\) such that, if \(H\) has \(m\) edges and no isolated vertices, \(N\ge 5m\), and \(F\) is a \(J\)-free graph on \(N\ge N_0\) vertices with
\[
e(F)\ge \left(\frac14-\delta\right)N^2,
\]
then \(\overline F\) contains \(H\).

#### Proof
Apply Theorem 4 with \(\gamma=1/10\). Then
\[
\alpha(F)\ge \frac{2N}{5}\ge 2m\ge v(H).
\]
An independent set of \(F\) of order \(v(H)\) is a blue clique and hence contains \(H\). ∎

For the reduced class \(\mathcal N\), the factor \(5\) can be replaced by \(3\), because \(v(H)\le m\):
\[
\alpha(F)\ge \frac{2N}{5}\ge \frac65m\ge v(H)
\qquad\text{when }N\ge3m.
\]

Thus ordinary stability, together with the exact \(H_5\) certificate, fully resolves the concentration problem in the near-extremal regime.

---

### 5. Every remaining obstruction has small red codegrees

#### Lemma 6
Let \(F\) be \(J\)-free, and suppose \(\overline F\) contains no copy of a graph \(H\) on \(h\) vertices. Then every red edge \(cd\) satisfies
\[
|N_F(c)\cap N_F(d)|\le 2h-2.
\]

#### Proof
If \(A=N_F(c)\cap N_F(d)\), Lemma 2 gives
\[
\alpha(F[A])\ge \left\lceil\frac{|A|}{2}\right\rceil.
\]
On the other hand, \(\alpha(F)\le h-1\): an independent set of \(h\) red vertices would be a blue \(K_h\), which contains \(H\). Hence
\[
\left\lceil\frac{|A|}{2}\right\rceil\le h-1,
\]
which implies \(|A|\le2h-2\). ∎

For an arbitrary \(m\)-edge no-isolate target,
\[
h\le2m,
\]
so every red edge has codegree at most \(4m-2\). For the reduced target class \(\mathcal N\), the stronger \(h\le m\) gives codegree at most \(2m-2\).

---

### 6. Every asymptotic obstruction is close to triangle-free

Let \(T(F)\) denote the number of red triangles. Since every triangle contributes once to the common-neighbor count of each of its three edges,
\[
3T(F)=
\sum_{cd\in E(F)}
|N_F(c)\cap N_F(d)|.
\]
By Lemma 6,
\[
T(F)\le \frac{(2h-2)e(F)}3.
\]

For all sufficiently large \(N\), Simonovits’s exact extremal theorem gives
\[
e(F)\le \frac{N^2}{4}.
\]
Thus, if \(N=Cm\), then for an arbitrary target,
\[
T(F)\le \frac{(4m-2)N^2}{12}
      <\frac{N^3}{3C}.
\]
For \(H\in\mathcal N\), this improves to
\[
T(F)<\frac{N^3}{6C}.
\]

The triangle-removal lemma now gives the following.

#### Corollary 7
For every \(\varepsilon>0\), there is \(C_\varepsilon\) such that if

- \(N\ge C_\varepsilon m\),
- \(F\) is \(J\)-free on \(N\) vertices, and
- \(\overline F\) omits an \(m\)-edge no-isolate graph \(H\),

then one can delete at most \(\varepsilon N^2\) red edges from \(F\) and obtain a triangle-free spanning graph.

#### Proof
Let \(\theta=\theta(\varepsilon)>0\) be supplied by the triangle-removal lemma. Choose
\[
C_\varepsilon\ge \frac1{3\theta}.
\]
The triangle estimate gives \(T(F)\le\theta N^3\), after harmless adjustment for the convention concerning labeled versus unlabeled triangles. Triangle removal then supplies the required set of at most \(\varepsilon N^2\) red edges. ∎

Consequently, any hypothetical disproof sequence with
\[
\frac{N_i}{e(H_i)}\longrightarrow\infty
\]
must satisfy all of the following:

1. its red density is bounded away from \(1/4\), by Corollary 5;
2. every red edge has codegree \(o(N_i)\), by Lemma 6;
3. it has \(o(N_i^3)\) red triangles;
4. it can be made triangle-free by deleting \(o(N_i^2)\) red edges.

These conditions are rigorous but do not yet force the required blue embedding.

---

### 7. Precise point of blockage

Let \(F_0\subseteq F\) be the triangle-free graph produced by Corollary 7. Then
\[
\overline{F_0}\supseteq \overline F.
\]
Even if one proves that \(\overline{F_0}\) contains \(H\), that copy may use edges which belong to \(F\setminus F_0\), so it need not occur in \(\overline F\).

The exceptional set \(F\setminus F_0\) can contain \(\varepsilon N^2\) edges, while \(H\) has only \(m=\Theta(N/C)\) edges. Thus a simple averaging or deletion argument cannot ensure that a copy of \(H\) avoids all exceptional red edges. One needs either:

- a resilience/multiplicity theorem giving many well-distributed blue embeddings in complements of triangle-free graphs; or
- a rooted version of the BGS bipartite-target theorem capable of attaching the bipartite parts of a nonbipartite component to a pre-embedded odd core.

Neither follows from the stated stability or BGS results, and proving either in sufficient generality appears comparable in strength to the remaining \(H_5\) problem.

## Self-Audit

1. **Theorem 4 imports Simonovits/Erdős–Simonovits stability rather than reproving it.**  
   This is the principal external input. It is explicitly part of the problem’s known context, and the proof above uses only its standard quantified form: near-extremal edge count yields a bipartition with \(o(N^2)\) internal edges.

2. **The local \(H_5\) certificate must preserve five distinct vertices.**  
   In Lemma 2, \(c,d\) are endpoints of an edge, \(a,b\) are distinct common neighbors, and \(x\notin\{c,d\}\) is adjacent to both \(a,b\). Since a loop is impossible, \(x\ne a,b\), and common neighbors \(a,b\) are distinct from \(c,d\). Hence all five vertices are distinct and the seven required edges are present.

3. **The triangle-removal reduction is not an embedding theorem.**  
   It is tempting, but invalid, to infer that an embedding into \(\overline{F_0}\) survives in \(\overline F\). I have not made that inference. The failure of this step is exactly why the status is BLOCKED rather than SOLVED.

## Computations To Verify

The following Python exhaustively verifies Lemmas 2 and 3 for all graphs on small orders.

```python
from itertools import combinations

def all_graphs(n):
    edges = list(combinations(range(n), 2))
    for mask in range(1 << len(edges)):
        adj = [0] * n
        for k, (u, v) in enumerate(edges):
            if (mask >> k) & 1:
                adj[u] |= 1 << v
                adj[v] |= 1 << u
        yield adj

def has_edge(adj, u, v):
    return ((adj[u] >> v) & 1) == 1

def contains_H5(adj):
    n = len(adj)
    for c, d in combinations(range(n), 2):
        if not has_edge(adj, c, d):
            continue
        A_mask = adj[c] & adj[d]
        A = [a for a in range(n) if (A_mask >> a) & 1]
        for a, b in combinations(A, 2):
            common = adj[a] & adj[b]
            common &= ~(1 << c)
            common &= ~(1 << d)
            common &= ~(1 << a)
            common &= ~(1 << b)
            if common:
                return True
    return False

def verify_common_neighborhood_lemma(adj):
    n = len(adj)
    assert not contains_H5(adj)
    for c, d in combinations(range(n), 2):
        if not has_edge(adj, c, d):
            continue
        A = adj[c] & adj[d]
        for x in range(n):
            if x in (c, d):
                continue
            assert (adj[x] & A).bit_count() <= 1

def verify_partition_lemma(adj):
    n = len(adj)
    vertices = set(range(n))

    for Xmask in range(1, (1 << n) - 1):
        X = [x for x in range(n) if (Xmask >> x) & 1]
        Y = list(vertices - set(X))

        q = sum(
            not has_edge(adj, x, y)
            for x in X for y in Y
        )

        for t in range(0, n + 1):
            X0 = [
                x for x in X
                if sum(not has_edge(adj, x, y) for y in Y) <= t
            ]
            Y0 = [
                y for y in Y
                if sum(not has_edge(adj, x, y) for x in X) <= t
            ]

            rhs_X = (len(X) - 2) * (len(Y) - 2*t - 1)
            if q < rhs_X:
                assert all(
                    not has_edge(adj, u, v)
                    for u, v in combinations(X0, 2)
                )

            rhs_Y = (len(Y) - 2) * (len(X) - 2*t - 1)
            if q < rhs_Y:
                assert all(
                    not has_edge(adj, u, v)
                    for u, v in combinations(Y0, 2)
                )

def run_exhaustive(n_max=7):
    for n in range(1, n_max + 1):
        checked = 0
        for adj in all_graphs(n):
            if contains_H5(adj):
                continue
            checked += 1
            verify_common_neighborhood_lemma(adj)
            verify_partition_lemma(adj)
        print("n =", n, "H5-free graphs checked =", checked)

# run_exhaustive(7)
```

To verify the codegree and triangle assertions against a small target \(H\):

```python
from itertools import permutations, combinations

def contains_target(host_adj, target_edges, h):
    n = len(host_adj)
    for image in permutations(range(n), h):
        if all(has_edge(host_adj, image[u], image[v])
               for u, v in target_edges):
            return True
    return False

def complement(adj):
    n = len(adj)
    out = [0] * n
    for u in range(n):
        for v in range(u + 1, n):
            if not has_edge(adj, u, v):
                out[u] |= 1 << v
                out[v] |= 1 << u
    return out

def triangle_count(adj):
    n = len(adj)
    return sum(
        has_edge(adj, a, b)
        and has_edge(adj, a, c)
        and has_edge(adj, b, c)
        for a, b, c in combinations(range(n), 3)
    )

def verify_obstruction_bounds(adj, target_edges, h):
    assert not contains_H5(adj)
    blue = complement(adj)

    if contains_target(blue, target_edges, h):
        return

    n = len(adj)
    codegree_sum = 0
    red_edges = 0

    for u, v in combinations(range(n), 2):
        if has_edge(adj, u, v):
            red_edges += 1
            codeg = (adj[u] & adj[v]).bit_count()
            assert codeg <= 2*h - 2
            codegree_sum += codeg

    T = triangle_count(adj)
    assert codegree_sum == 3*T
    assert 3*T <= (2*h - 2) * red_edges
```

A useful SAT/enumeration experiment for the unresolved regime is:

1. Enumerate or SAT-generate \(H_5\)-free red graphs \(F\) on \(N\) vertices.
2. Restrict to
   \[
   e(F)\le (1/4-\delta)N^2
   \]
   and maximum edge-codegree at most \(2m-2\).
3. Enumerate targets whose connected components are all nonbipartite and have \(m\) edges.
4. Test whether \(\overline F\) omits one.
5. Record the triangle-removal distance and whether the exceptional red edges admit a small vertex cover.

The last statistic directly tests whether the exceptional edges might satisfy a concentration theorem stronger than ordinary triangle removal.

## Route Diagnosis

### Proved ledger

- Bipartite connected components can be embedded in a separate block using BGS; it suffices to handle targets all of whose components are nonbipartite.
- Such reduced targets satisfy \(v(H)\le e(H)\).
- For every red edge \(cd\), its common red neighborhood induces maximum red degree at most one.
- Near a complete bipartite red structure, all internal red edges are incident to vertices with large cross-deficiency.
- Every near-extremal \(H_5\)-free red graph has a red-independent set of size \((1/2-o(1))N\).
- Therefore the entire near-extremal red regime gives the desired blue embedding.
- Any remaining obstruction has red edge-codegree \(O(m)\), \(O(N^3/C)\) red triangles when \(N=Cm\), and is edge-close to triangle-free for large \(C\).

### Plausible but unproved

- A resilience theorem for complements of triangle-free graphs may allow deletion of the exceptional red edges furnished by triangle removal.
- A rooted BGS theorem may allow an odd core to be embedded first and its bipartite remainder attached compatibly.
- The \(H_5\) local codegree restriction may force more structure on the triangle-removal exceptional edges than is visible from their total number alone.

### Dead ends

- **Stability at all densities:** impossible. Every triangle-free graph is \(H_5\)-free, including blow-ups of odd cycles and high-chromatic triangle-free graphs far from bipartite.
- **Decomposing a connected target into bipartite edge-subgraphs:** independent BGS embeddings need not use the same images for shared vertices and therefore do not compose.
- **Assuming triangle-removal edges concentrate on few vertices:** false in general. A disjoint union of red \(K_4\)'s is \(H_5\)-free, has triangles spread over all vertices, and requires vertex deletions in every component to become induced-triangle-free.
- **Using edge-closeness to triangle-free directly:** the new blue edges created by deleting red edges may be indispensable to every embedding found in the enlarged blue graph.

The most promising fresh attempt is a robust multiplicity theorem for blue embeddings against a triangle-free red graph, strong enough to avoid an exceptional red set constrained by Lemma 2. Without such a theorem, Route 4 is genuinely blocked in the uniformly subextremal regime.