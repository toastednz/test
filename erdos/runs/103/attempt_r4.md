STATUS: BLOCKED

## Result

Route 4 does not currently yield a solution. I proved several rigorous structural statements that sharply constrain any active-graph exchange argument. Most importantly: if an optimal configuration has a vertex of combined contact/diameter degree at most \(2\), then it lies in a continuum of incongruent optimal configurations, so \(h(n)=\infty\). Every optimum also supports a nonzero signed equilibrium stress. On the discrete-exchange side, compatible replacement flips force plateaus in \(D_n\); in particular, for \(n\ge7\), an elementary equilateral-triangle ear flip forces \(D_{n+1}=D_n\). Moreover, the simplest same-active-graph two-anchor reflection necessarily has active degree \(2\), hence gives continuous rather than genuinely discrete multiplicity. Finally, arbitrarily large unit triangular-lattice frameworks satisfy all standard contact/diameter graph sparsity restrictions while admitting no noncongruent realization preserving their contact lengths. Thus planarity, degree bounds, and diameter-graph sparsity alone cannot force exchanges. The route is blocked at the genuinely optimal-specific assertion that every large order has an optimum containing many compatible discrete switches—or even one low-active-degree vertex.

## Complete Argument

### 1. Active constraints

Let \(X=\{x_1,\dots,x_n\}\in\mathcal M_n\), put \(D=D_n\), and assume \(n\ge4\), so \(D>1\).

Write
\[
C(X)=\{ij:\|x_i-x_j\|=1\},
\qquad
B(X)=\{ij:\|x_i-x_j\|=D\}.
\]
The combined active graph is
\[
A(X)=(X,C(X)\cup B(X)).
\]

For a fixed vertex \(p\in X\) and an active neighbor \(q\), define the signed feasible normal
\[
g_{pq}=
\begin{cases}
p-q,& pq\in C(X),\\
q-p,& pq\in B(X).
\end{cases}
\]
If only \(p\) is moved with velocity \(v\), then the derivative of the relevant slack is
\[
2g_{pq}\cdot v.
\]
Thus \(g_{pq}\cdot v>0\) means that the active inequality becomes strict to first order.

---

### 2. A low-active-degree vertex forces \(h(n)=\infty\)

#### Theorem 2.1

Let \(n\ge4\). If some \(X\in\mathcal M_n\) has a vertex of degree at most \(2\) in \(A(X)\), then
\[
h(n)=\infty.
\]
Indeed, \(X\) belongs to a one-parameter family of pairwise incongruent optimal configurations.

#### Proof

Fix a vertex \(p\), keeping \(Y=X\setminus\{p\}\) fixed. Every inactive distance from \(p\) has a positive margin from both \(1\) and \(D\). Hence it suffices to construct an arbitrarily small nonconstant path \(p(t)\) satisfying the inequalities incident to the at most two active neighbors.

##### Degree \(0\)

All constraints involving \(p\) are strict. Therefore a sufficiently small open ball around \(p\) is feasible. Choose a line segment \(p(t)=p+tv\) on which one distance to \(Y\) varies strictly monotonically.

##### Degree \(1\)

If \(pq\) is a contact edge, move \(p\) slightly away from \(q\). If \(pq\) is a diameter edge, move \(p\) slightly toward \(q\). The active inequality becomes strict, while all inactive inequalities remain valid for sufficiently small motion.

##### Degree \(2\): non-antiparallel signed normals

Let the two signed normals be \(g_1,g_2\). If they are not negative multiples of one another, there exists \(v\) such that
\[
g_1\cdot v>0,\qquad g_2\cdot v>0.
\]
For example, after normalizing,
\[
v=\frac{g_1}{\|g_1\|}+\frac{g_2}{\|g_2\|}
\]
works unless the normalized vectors are opposite. Then \(p(t)=p+tv\) makes both active inequalities strict for all sufficiently small \(t>0\).

##### Degree \(2\): antiparallel signed normals

There are three possible types.

1. **Two contact edges.**  
   Their neighbors must be \(p-u\) and \(p+u\), where \(\|u\|=1\). If \(w\perp u\) is a unit vector, put
   \[
   p(t)=p+tw.
   \]
   Both formerly unit distances become
   \[
   \sqrt{1+t^2}>1.
   \]

2. **Two diameter edges.**  
   This case is impossible. Antiparallel signed normals would place the two neighbors at \(p-Du\) and \(p+Du\), whose mutual distance is \(2D>D\).

3. **One contact and one diameter edge.**  
   After a rigid motion, take
   \[
   p=0,\qquad q=u,\qquad r=Du,
   \]
   where \(q\) is the contact neighbor, \(r\) the diameter neighbor, and \(u\) is a unit vector. Choose \(w\perp u\) and
   \[
   \frac1{2D}<a<\frac12.
   \]
   Set
   \[
   p(t)=a t^2u+tw.
   \]
   Then
   \[
   \|p(t)-q\|^2
   =1+(1-2a)t^2+a^2t^4>1
   \]
   for small nonzero \(t\), while
   \[
   \|p(t)-r\|^2
   =D^2+(1-2aD)t^2+a^2t^4<D^2
   \]
   for sufficiently small nonzero \(t\).

Thus in every case there is a nonconstant feasible path \(X(t)=Y\cup\{p(t)\}\) with diameter at most \(D\). Since \(D=D_n\), every \(X(t)\) must actually have diameter exactly \(D_n\), and hence is optimal.

The path can be chosen so that at least one labeled pairwise distance varies strictly monotonically. Therefore its labeled squared-distance matrices are all distinct. One unordered congruence class has at most \(n!\) labeled squared-distance matrices, one for each relabeling. Consequently a continuum of parameter values produces a continuum of unordered congruence classes. Hence \(h(n)=\infty\). ∎

#### Corollary 2.2

If \(h(n)<\infty\) and \(n\ge4\), then every vertex of every optimal configuration has combined active degree at least \(3\).

This is substantially stronger than a rigidity count: degree \(2\) is impossible even in the exceptional antiparallel cases where first-order linear analysis alone is inconclusive.

---

### 3. Further local necessary conditions for finite \(h(n)\)

#### Proposition 3.1

Suppose \(X\in\mathcal M_n\), and at a vertex \(p\) there is a vector \(v\) such that
\[
g_{pq}\cdot v>0
\]
for every active edge \(pq\) incident to \(p\). Then \(h(n)=\infty\).

#### Proof

Move only \(p\) along \(p+tv\). Every incident active constraint becomes strict to first order, and all inactive constraints remain valid for sufficiently small \(t>0\). The proof of Theorem 2.1 then applies. ∎

By Gordan’s theorem of alternatives, if \(h(n)<\infty\), then at every vertex \(p\) there are nonnegative coefficients, not all zero, satisfying the local balance
\[
\sum_{pq\in C(X)}\alpha_{pq}(p-q)
+
\sum_{pq\in B(X)}\beta_{pq}(q-p)=0.
\]
This condition is only necessary; antiparallel degree-two normals satisfy such a balance but still permit a second-order flex, as Theorem 2.1 shows.

#### Proposition 3.2

If \(h(n)<\infty\), every vertex of every optimal configuration is incident to at least one contact edge.

#### Proof

Suppose \(p\) has only diameter-active neighbors \(q_1,\dots,q_s\). Since
\[
\|q_i-q_j\|\le D
\]
and both \(q_i,q_j\) lie on the circle of radius \(D\) around \(p\), the angle \(\theta_{ij}\) between \(q_i-p\) and \(q_j-p\) satisfies
\[
2D\sin\frac{\theta_{ij}}2\le D,
\]
so \(\theta_{ij}\le\pi/3\). Thus all diameter-neighbor directions lie in an arc of angular length at most \(\pi/3\). There is a vector \(v\) pointing into the middle of this arc such that
\[
(q_i-p)\cdot v>0
\]
for every \(i\). Moving \(p\) in direction \(v\) strictly decreases all incident diameter distances. Proposition 3.1 gives \(h(n)=\infty\), a contradiction. ∎

Hence, if \(h(n)<\infty\), the contact graph has minimum degree at least \(1\), and in particular at least \(n/2\) contact edges. This remains far below the planar upper bound \(3n-6\).

---

### 4. Every optimum supports a signed equilibrium stress

#### Theorem 4.1

For every \(X\in\mathcal M_n\), \(n\ge4\), there are coefficients
\[
\lambda_{ij}\ge0\quad(ij\in C(X)),\qquad
\mu_{ij}\ge0\quad(ij\in B(X)),
\]
not all zero, such that at every vertex \(x_i\),
\[
\sum_{ij\in C(X)}\lambda_{ij}(x_i-x_j)
-
\sum_{ij\in B(X)}\mu_{ij}(x_i-x_j)=0.
\]
Moreover,
\[
\sum_{ij\in C(X)}\lambda_{ij}
=
D^2\sum_{ij\in B(X)}\mu_{ij},
\]
so both contact and diameter coefficients occur nontrivially.

#### Proof

For a contact edge \(ij\), use the row vector corresponding to the derivative of
\[
\|x_i-x_j\|^2-1.
\]
For a diameter edge, use the row vector corresponding to the derivative of
\[
D^2-\|x_i-x_j\|^2.
\]

There cannot be a velocity vector making all these derivatives strictly positive. If there were, a sufficiently small perturbation would make every contact distance strictly larger than \(1\) and every diameter distance strictly smaller than \(D\); the finitely many inactive constraints would remain strict. The resulting \(n\)-point set would have all mutual distances at least \(1\) and diameter strictly smaller than \(D_n\), a contradiction.

Gordan’s theorem of alternatives therefore gives a nonzero nonnegative linear dependence among the active constraint gradients. Collecting the terms at each vertex gives the stated equilibrium equations.

Now dot the equilibrium equation at \(x_i\) with \(x_i\), sum over all vertices, and combine the two contributions from each edge. This gives
\[
0=
\sum_{ij\in C(X)}\lambda_{ij}\|x_i-x_j\|^2
-
\sum_{ij\in B(X)}\mu_{ij}\|x_i-x_j\|^2.
\]
Since contact lengths are \(1\) and diameter lengths are \(D\),
\[
\sum_{ij\in C(X)}\lambda_{ij}
=
D^2\sum_{ij\in B(X)}\mu_{ij}.
\]
As the entire stress is nonzero, neither side can vanish. ∎

This is the strongest general optimality consequence I obtained from the active graph. It does not imply a flippable circuit: the stress can be degenerate, supported on a small subgraph, or coexist with a globally rigid active framework.

---

### 5. A rigorous switching lemma

The following isolates exactly what an exchange construction would need.

#### Theorem 5.1: switching cube

Let \(D=D_n\). Suppose there are a common core \(C\) and pairs of modules
\[
A_i^0,A_i^1,\qquad 1\le i\le r,
\]
such that for every bit vector \(\varepsilon\in\{0,1\}^r\),
\[
X_\varepsilon
=
C\cup\bigcup_{i=1}^r A_i^{\varepsilon_i}
\]
has exactly \(n\) points, mutual distances at least \(1\), and diameter at most \(D\). Then every \(X_\varepsilon\) is optimal.

Assume additionally that:

1. the \(2^r\) resulting point sets are distinct;
2. every isometry between two \(X_\varepsilon\) sends \(C\) onto \(C\);
3. \(C\) contains three noncollinear points.

If
\[
\Gamma=\{T:T(C)=C\},
\]
then the number of incongruent configurations among the \(X_\varepsilon\) is at least
\[
\frac{2^r}{|\Gamma|}
\ge \frac{2^r}{2|C|}.
\]

#### Proof

Every \(X_\varepsilon\) is feasible with diameter at most \(D_n\). By the definition of \(D_n\), its diameter is therefore exactly \(D_n\), so it is optimal.

If \(X_\varepsilon\) and \(X_\delta\) are congruent, the assumed recognizability of \(C\) implies that the congruence lies in \(\Gamma\). For fixed \(\varepsilon\), each \(T\in\Gamma\) produces at most one set \(X_\delta=T(X_\varepsilon)\). Thus one congruence class contains at most \(|\Gamma|\) members of the switching family.

Finally, a finite group preserving \(C\) fixes its centroid and is conjugate to a finite subgroup of \(O(2)\), hence is cyclic or dihedral. If its rotation subgroup has order \(s\), the orbit of any noncentral point of \(C\) has \(s\) elements, so \(s\le |C|\). Therefore \(|\Gamma|\le2|C|\). ∎

This reduces Route 4 to finding such switching systems in an optimum for every sufficiently large \(n\), with enough switches and sufficient intrinsic marking. No theorem presently forces even one such switch.

---

### 6. Compatible switches force capacity plateaus

Discrete replacement flips often have a hidden consequence: the old and new sites can coexist.

#### Proposition 6.1

Let
\[
X=C\cup\{p_1,\dots,p_r\}\in\mathcal M_n,
\qquad D=D_n.
\]
Suppose there are alternative points \(p_1',\dots,p_r'\) such that the union
\[
U=C\cup\{p_1,p_1',\dots,p_r,p_r'\}
\]
has \(n+r\) distinct points, all mutual distances at least \(1\), and diameter at most \(D\). Then
\[
D_n=D_{n+1}=\cdots=D_{n+r}.
\]

#### Proof

The union \(U\) is a feasible \((n+r)\)-point configuration of diameter at most \(D_n\), so
\[
D_{n+r}\le D_n.
\]
Monotonicity gives \(D_n\le D_{n+r}\), hence equality. Every intermediate value is trapped between them. ∎

Thus a large family of mutually compatible local switches would imply a wide capacity plateau. This connects the naive form of Route 4 directly to Route 3.

---

### 7. Equilateral ear flips force a plateau

#### Proposition 7.1

Let \(n\ge7\), \(X\in\mathcal M_n\), and suppose \(p,a,b\in X\) form a unit equilateral triangle. Let \(p'\) be the reflection of \(p\) across the line \(ab\). Assume \(p'\notin X\setminus\{p\}\) and
\[
X'=(X\setminus\{p\})\cup\{p'\}
\]
is feasible with diameter at most \(D_n\). Then \(X'\) is optimal and
\[
D_{n+1}=D_n.
\]

#### Proof

First, \(D_n>\sqrt3\) for \(n\ge7\). Indeed, if \(D\le\sqrt3\), Oler’s inequality and the isodiametric bounds from the brief give
\[
n\le
\frac{\pi}{2\sqrt3}D^2+\frac\pi2D+1
\le \pi\sqrt3+1<7.
\]

The reflected equilateral vertices satisfy
\[
\|p-p'\|=\sqrt3<D_n.
\]
The old point \(p\) is compatible with every point of \(X\setminus\{p\}\), and by assumption so is \(p'\). Hence
\[
(X\setminus\{p\})\cup\{p,p'\}
\]
is a feasible \((n+1)\)-point set of diameter at most \(D_n\). Proposition 6.1 gives \(D_{n+1}=D_n\). The replacement \(X'\) is feasible at diameter \(D_n\), hence optimal. ∎

Therefore the most obvious contact-triangle flip cannot be used independently of the plateau problem: for all sufficiently large orders, its existence certifies a plateau.

---

### 8. A same-active-graph two-contact reflection is never a genuinely discrete switch

#### Proposition 8.1

Let \(X\) be feasible with diameter \(D>1\). Suppose \(p\in X\) has two distinct contact neighbors \(a,b\), and let \(p'\ne p\) be the reflection of \(p\) across the line \(ab\). Assume:

1. replacing \(p\) by \(p'\) is feasible;
2. every active edge incident to \(p\) is preserved with the same type:
   \[
   \|p-q\|=1\Longrightarrow\|p'-q\|=1,
   \]
   \[
   \|p-q\|=D\Longrightarrow\|p'-q\|=D.
   \]

Then \(a,b\) are the only active neighbors of \(p\).

Consequently, if \(X\) is optimal, then \(h(n)=\infty\).

#### Proof

Choose coordinates so the reflection axis is the \(x\)-axis and
\[
p=(0,h),\qquad p'=(0,-h),\qquad h>0.
\]
Since \(a,b\) lie on the axis and are each at distance \(1\) from \(p\), they are
\[
a=(-s,0),\qquad b=(s,0),
\qquad s=\sqrt{1-h^2}.
\]
Their mutual separation is \(2s\ge1\), so \(s\ge1/2\).

If an active edge \(pq\) is preserved with the same length after reflection, then
\[
\|p-q\|=\|p'-q\|,
\]
so \(q\) lies on the reflection axis.

If the common length is \(1\), the only axis points at distance \(1\) from \(p\) are \(a\) and \(b\).

Suppose the common length is \(D\). Then
\[
q=(t,0),\qquad t=\pm\sqrt{D^2-h^2}.
\]
Take \(t>0\); the other case is symmetric. The distance from \(q\) to \(a=(-s,0)\) is \(t+s\). Since \(D-s>0\),
\[
t>D-s
\]
is equivalent after squaring to
\[
D^2-h^2>(D-s)^2,
\]
or
\[
2Ds>h^2+s^2=1.
\]
This holds because \(D>1\) and \(s\ge1/2\). Hence
\[
\|q-a\|=t+s>D,
\]
contradicting feasibility. Thus there is no diameter-active neighbor preserved by the reflection.

Therefore \(p\) has exactly the two active neighbors \(a,b\). If \(X\) is optimal, Theorem 2.1 gives \(h(n)=\infty\). ∎

So the simplest two-anchor active-graph flip has only two outcomes superficially: in fact the original realization is already continuously movable. A genuinely discrete switch must involve more vertices, must change the incident active graph, or must use alternatives that are mutually incompatible.

---

### 9. The standard graph bounds do not force any exchange

There are arbitrarily large feasible frameworks satisfying all the usual graph restrictions but having no noncongruent realization preserving their contact lengths.

Let
\[
e_1=(1,0),\qquad e_2=\left(\frac12,\frac{\sqrt3}{2}\right),
\]
and define
\[
H_k=
\left\{
ae_1+be_2:
a,b\in\mathbb Z,\ 
\max(|a|,|b|,|a+b|)\le k
\right\}.
\]
Then
\[
|H_k|=1+3k(k+1),\qquad \operatorname{diam}(H_k)=2k.
\]
Its unit-contact graph is the standard triangulation of a regular hexagonal lattice patch.

#### Proposition 9.1

Any realization of the abstract contact graph of \(H_k\) in which every contact edge has length \(1\) and all vertices remain distinct is congruent to the standard realization.

#### Proof

The elementary triangles of the lattice patch form a triangulated disk, and their dual adjacency graph is connected.

Fix one elementary triangle. Its three unit edge lengths determine it up to congruence and reflection. Consider an adjacent elementary triangle sharing an edge. Given the two endpoints of a unit edge, there are exactly two points at unit distance from both endpoints. One is the already realized third vertex of the first triangle. The third vertex of the adjacent abstract triangle is a distinct vertex, so it cannot occupy that same point. It is therefore forced to occupy the other equilateral position.

Proceed along a spanning tree of the connected dual graph. Every elementary triangle, and hence every vertex of \(H_k\), is forced. The resulting realization is the standard one, up to the initial Euclidean isometry and reflection. ∎

Thus these arbitrarily large frameworks:

- have planar contact graphs;
- have contact degree at most \(6\);
- have diameter graphs with at most \(n\) edges;
- contain long boundaries;
- admit no noncongruent realization preserving all active contact lengths.

They are not optimal for large \(k\): their diameter is \(2k\), whereas the known asymptotic gives
\[
D_{|H_k|}
=
\sqrt{\frac{6\sqrt3}{\pi}}\,k+O(1),
\]
and \(\sqrt{6\sqrt3/\pi}<2\). Their role is therefore not to disprove the Erdős statement, but to show that planarity, bounded contact degree, sparse diameter graph, and large size cannot alone imply a flippable circuit. Any successful exchange theorem must use exact global optimality in a substantially stronger way.

---

### 10. Exact point of blockage

The established results leave the following alternatives for a successful proof.

1. **Continuous route:** Prove that for every sufficiently large \(n\), some optimal configuration has a vertex of active degree at most \(2\), or more generally a vertex admitting a strict local feasible direction. Theorem 2.1 or Proposition 3.1 would then give
   \[
   h(n)=\infty.
   \]
   No counting argument from the known edge bounds forces such a vertex.

2. **Discrete route:** Prove that every sufficiently large order has an optimum containing many multi-vertex switches whose alternatives:
   - remain feasible against the full configuration;
   - preserve diameter \(D_n\);
   - are sufficiently marked to survive quotienting by congruence;
   - are not merely compatible alternative sites producing an unproved wide plateau;
   - and are not the two-contact reflection of Proposition 8.1.

This required assertion is currently of comparable difficulty to the original problem. The global signed stress from Theorem 4.1 does not force such switches, and the rigid examples in Proposition 9.1 show why the standard graph-theoretic bounds cannot do so.

## Self-Audit

1. **The low-degree theorem is only conditional on finding such a vertex in a certified global optimum.**  
   Nothing proved here forces low active degree for all large \(n\). The theorem itself is reliable because every possible degree-\(\le2\) signed-normal configuration was treated explicitly, including the first-order-degenerate antiparallel cases.

2. **The equilibrium stress is too weak to produce exchange circuits.**  
   Its support may be small or degenerate, and a stressed framework may be globally rigid. The stress identity itself is rigorous: it follows directly from Gordan’s alternative, and the contact/diameter mass relation follows by an exact dot-product calculation.

3. **The rigid triangular patches are not optimal configurations.**  
   They only refute a purely combinatorial exchange principle based on the currently known graph bounds; they do not refute an optimality-specific exchange theorem. Their rigidity statement is nevertheless secure because adjacent equilateral triangles are forced successively across the connected dual graph.

## Computations To Verify

The following code checks the exact combinatorics and numerical rigidity rank of the hexagonal patches.

```python
import itertools
import numpy as np

def H(k):
    return [(a, b)
            for a in range(-k, k + 1)
            for b in range(-k, k + 1)
            if max(abs(a), abs(b), abs(a + b)) <= k]

def qdist(u, v):
    # Squared Euclidean distance for basis vectors at 60 degrees.
    a = u[0] - v[0]
    b = u[1] - v[1]
    return a*a + a*b + b*b

def lattice_xy(u):
    a, b = u
    return np.array([a + 0.5*b, np.sqrt(3)*b/2.0])

def patch_data(k):
    V = H(k)
    n = len(V)
    contacts = []
    diameter_edges = []
    diam2 = max(qdist(u, v) for u, v in itertools.combinations(V, 2))

    for i, j in itertools.combinations(range(n), 2):
        q = qdist(V[i], V[j])
        if q == 1:
            contacts.append((i, j))
        if q == diam2:
            diameter_edges.append((i, j))

    R = np.zeros((len(contacts), 2*n))
    P = np.array([lattice_xy(v) for v in V])
    for row, (i, j) in enumerate(contacts):
        d = P[i] - P[j]
        R[row, 2*i:2*i+2] = d
        R[row, 2*j:2*j+2] = -d

    rank = np.linalg.matrix_rank(R, tol=1e-9)

    return {
        "n": n,
        "expected_n": 1 + 3*k*(k+1),
        "diam2": diam2,
        "expected_diam2": 4*k*k,
        "contacts": len(contacts),
        "diameter_edges": len(diameter_edges),
        "rigidity_rank": rank,
        "expected_rigidity_rank": 2*n - 3,
    }

for k in range(1, 8):
    print(k, patch_data(k))
```

A numerical active-graph and reflection scanner for candidate optimizers:

```python
import numpy as np
from itertools import combinations

def reflect_across_line(p, a, b):
    u = b - a
    u = u / np.linalg.norm(u)
    projection = a + u * np.dot(p - a, u)
    return 2*projection - p

def active_graph(P, tol=1e-8):
    P = np.asarray(P, dtype=float)
    n = len(P)
    d = np.zeros((n, n))
    for i, j in combinations(range(n), 2):
        d[i, j] = d[j, i] = np.linalg.norm(P[i] - P[j])
    D = d.max()

    contacts = []
    diameters = []
    for i, j in combinations(range(n), 2):
        if abs(d[i, j] - 1.0) <= tol:
            contacts.append((i, j))
        if abs(d[i, j] - D) <= tol:
            diameters.append((i, j))

    degree = [0]*n
    for i, j in contacts + diameters:
        degree[i] += 1
        degree[j] += 1

    return D, contacts, diameters, degree

def scan_contact_reflections(P, tol=1e-8):
    P = np.asarray(P, dtype=float)
    n = len(P)
    D, contacts, diameters, degree = active_graph(P, tol)
    contact_neighbors = [[] for _ in range(n)]
    for i, j in contacts:
        contact_neighbors[i].append(j)
        contact_neighbors[j].append(i)

    reports = []
    for i in range(n):
        for a_idx, b_idx in combinations(contact_neighbors[i], 2):
            p, a, b = P[i], P[a_idx], P[b_idx]
            p2 = reflect_across_line(p, a, b)
            if np.linalg.norm(p2 - p) <= tol:
                continue

            others = [j for j in range(n) if j != i]
            distances = np.array([np.linalg.norm(p2 - P[j]) for j in others])
            replacement_feasible = (
                distances.min() >= 1.0 - tol and
                distances.max() <= D + tol
            )

            if replacement_feasible:
                old_new = np.linalg.norm(p - p2)
                reports.append({
                    "moving_vertex": i,
                    "anchors": (a_idx, b_idx),
                    "anchor_distance": np.linalg.norm(a - b),
                    "old_new_distance": old_new,
                    "active_degree": degree[i],
                    "union_feasible": 1.0 - tol <= old_new <= D + tol,
                })
    return reports
```

The antiparallel contact/diameter path from Theorem 2.1 can be checked directly:

```python
def verify_mixed_path(D, a, ts):
    assert D > 1
    assert 1/(2*D) < a < 1/2
    q = np.array([1.0, 0.0])   # contact center
    r = np.array([D, 0.0])     # diameter center

    for t in ts:
        p = np.array([a*t*t, t])
        contact2 = np.dot(p-q, p-q)
        diameter2 = np.dot(p-r, p-r)
        assert contact2 > 1.0
        assert diameter2 < D*D

verify_mixed_path(D=3.0, a=0.3, ts=[1e-4, 1e-3, 1e-2, 5e-2])
```

Given a numerical candidate, the signed stress can be sought by linear programming:

```python
import numpy as np
from scipy.optimize import linprog

def find_nonnegative_stress(P, tol=1e-8):
    P = np.asarray(P, dtype=float)
    n = len(P)
    D, C, B, degree = active_graph(P, tol)

    edges = [(i, j, +1) for i, j in C] + [(i, j, -1) for i, j in B]
    A = np.zeros((len(edges), 2*n))

    for row, (i, j, sign) in enumerate(edges):
        d = P[i] - P[j]
        # Contact row: +(xi-xj); diameter row: -(xi-xj).
        A[row, 2*i:2*i+2] = sign*d
        A[row, 2*j:2*j+2] = -sign*d

    # Seek w >= 0, A^T w = 0, sum(w)=1.
    Aeq = np.vstack([A.T, np.ones((1, len(edges)))])
    beq = np.zeros(2*n + 1)
    beq[-1] = 1.0

    result = linprog(
        c=np.zeros(len(edges)),
        A_eq=Aeq,
        b_eq=beq,
        bounds=[(0, None)]*len(edges),
        method="highs"
    )
    if not result.success:
        return None

    w = result.x
    contact_mass = w[:len(C)].sum()
    diameter_mass = w[len(C):].sum()
    virial_error = contact_mass - D*D*diameter_mass
    return w, virial_error
```

For any prospective exact switch, the decisive finite checks are:

1. solve both realizations exactly from their active equations;
2. verify every inactive squared distance lies in \([1,D_n^2]\);
3. test whether the union of old and alternative sites is feasible, which would certify a plateau;
4. compare complete squared-distance matrices under all graph isomorphism candidates;
5. separately certify \(D=D_n\) by quantifier elimination or exhaustive interval infeasibility below \(D\).

## Route Diagnosis

The productive part of Route 4 was identifying what simple exchanges actually imply. Low-degree active circuits produce continuous moduli, not isolated binary choices. Equilateral ear flips produce capacity plateaus. Same-active two-contact reflections again reduce to continuous mobility. The universal graph constraints do not force any exchange because large triangulated unit frameworks can be completely realization-rigid.

The precise block is the absence of an optimality-specific boundary theorem. A fresh attempt should target one of two statements:

- for every sufficiently large \(n\), some optimum has a vertex or bounded subframework with a certified finite flex at fixed diameter; or
- every sufficiently large \(n\) has an optimum containing many mutually incompatible, active-graph-changing multi-vertex switches with an intrinsically recognizable core.

The first would switch effectively to Route 2 and, by Theorem 2.1, could prove the much stronger conclusion \(h(n)=\infty\). The second remains the genuine discrete Route 4, but simple reflection gadgets are now ruled out or diverted into the plateau problem.