STATUS: BLOCKED

## Result

I did not resolve Erdős Problem #567. I established several rigorous Route 2 reductions and identified the precise obstruction to a naive edge-charged induction. A vertex-extension inequality \(R(G,H)\le R(G,H-v)+C_Gd_H(v)\) would immediately solve the problem, but extending one already chosen blue copy is impossible even with an arbitrarily large reserve. I proved a weaker neighborhood-descent recurrence involving \(R(G-x,H)\), a sharp pendant-vertex extension bound governed by an auxiliary extremal parameter, and linearity for all forest targets. For the three graphs, the pendant parameter is asymptotic to \(h,h,\) and \(2h\), respectively, rather than \(O(1)\); thus a purely local one-copy extension argument incurs vertex-scale rather than edge-scale cost. Continuing Route 2 requires a genuinely global switching or relocation theorem, whose clique specialization already contains the unresolved quadratic off-diagonal Ramsey problem.

## Complete Argument

### 1. Why the desired vertex recurrence would solve the problem

Fix a graph \(G\). Suppose there were a constant \(C_G\) such that, for every graph \(H\) and every nonisolated \(v\in V(H)\),
\[
R(G,H)\le R(G,H-v)+C_Gd_H(v).
\tag{1}
\]

This would imply Ramsey size linearity.

Indeed, start with a no-isolate graph \(H\) having \(m\) edges. Repeatedly delete a vertex of positive current degree until the remaining graph is edgeless, say on \(k\) vertices. If the deleted vertices have current degrees \(d_1,\dots,d_s\), then
\[
\sum_{i=1}^s d_i=m,
\]
because every edge is charged exactly when its first endpoint is deleted. Also
\[
k\le v(H)\le 2m.
\]
Iterating (1) gives
\[
R(G,H)\le R(G,E_k)+C_Gm,
\]
where \(E_k\) is the edgeless graph on \(k\) vertices. Since every set of \(k\) vertices is a copy of \(E_k\),
\[
R(G,E_k)=k.
\]
Consequently,
\[
R(G,H)\le (C_G+2)m.
\tag{2}
\]

Thus (1) is a sufficient Route 2 lemma. It is, however, unproved and substantially stronger than the original statement.

Two elementary auxiliary inequalities are useful:

* If \(H^+=H\sqcup K_1\), then
  \[
  R(G,H^+)\le R(G,H)+1.
  \tag{3}
  \]
  After finding a blue \(H\), use any unused vertex for the isolated vertex.

* For disjoint targets,
  \[
  R(G,H_1\sqcup H_2)\le R(G,H_1)+R(G,H_2).
  \tag{4}
  \]
  Partition the ambient vertex set into parts of these two sizes. If the red graph is \(G\)-free, the two induced complements contain disjoint copies of \(H_1\) and \(H_2\).

In particular, disconnected targets cause no additional difficulty once all connected components can be handled linearly.

---

### 2. A fixed blue copy cannot generally be extended

The strongest naive form of Route 2 is false.

Let \(H\) be any graph, let \(v\in V(H)\) have positive degree, and put \(H'=H-v\). Fix a blue copy \(\phi(H')\) on a vertex set \(C\), and let \(y\in N_H(v)\). Add an arbitrarily large reserve \(X\). Define the red graph to have exactly the edges
\[
\phi(y)x,\qquad x\in X,
\]
and no others.

The red graph is a star. It contains none of \(Q_3,K_{3,3},H_5\): each of these graphs has minimum degree at least two and contains a cycle, whereas every subgraph of a star is acyclic and has at most one vertex of degree greater than one.

All edges inside \(C\) are blue, so \(\phi\) is a blue embedding of \(H'\). But no \(x\in X\) can be the image of \(v\), because \(\phi(y)x\) is red. Since \(C\) is already fully occupied, this particular copy cannot be extended, regardless of \(|X|\).

Therefore, no statement of the following kind can hold:

> Every blue copy of \(H-v\) in a \(G\)-free red graph extends whenever \(Cd_H(v)\) additional vertices are available.

Any successful induction must be allowed to replace or globally rearrange the already embedded copy.

For \(H_5\), there is a stronger genuine Ramsey obstruction. Let \(H'\) be any connected graph on \(h\) vertices, distinguish \(y\in V(H')\), and let \(H\) be obtained by attaching a leaf to \(y\). Colour \(K_{2h}\) so that the red graph is \(K_{h,h}\). This red graph is bipartite and hence \(H_5\)-free. Its blue complement is
\[
K_h\sqcup K_h.
\]
The graph \(H\) is connected and has \(h+1\) vertices, so it cannot occur in the blue graph. Thus
\[
R(H_5,H)>2h.
\tag{5}
\]
This does not disprove linearity, because \(e(H)\ge h\), but it shows that a whole \(h\)-vertex blue component may have to be discarded and relocated.

---

### 3. A rigorous neighborhood-descent recurrence

There is a valid, but quantitatively inadequate, vertex-extension recurrence.

#### Lemma 1

Let \(G,H\) be graphs, let \(x\in V(G)\), and put \(J=G-x\). Let \(v\in V(H)\) have degree \(d\ge1\), and put \(H'=H-v\). Then
\[
R(G,H)
\le
R(G,H')+d\bigl(R(J,H)-1\bigr)+1.
\tag{6}
\]

#### Proof

Set
\[
r=R(G,H'),\qquad q=R(J,H),
\]
and consider a red-blue colouring on
\[
N=r+d(q-1)+1
\]
vertices with no red \(G\). Partition the vertices into sets
\[
A\sqcup B,\qquad |A|=r,\quad |B|=d(q-1)+1.
\]

The colouring induced on \(A\) contains a blue copy \(\phi(H')\). Let
\[
N_H(v)=\{u_1,\dots,u_d\},
\qquad z_i=\phi(u_i).
\]

If some \(b\in B\) is blue-adjacent to every \(z_i\), then extending \(\phi\) by \(\phi(v)=b\) produces a blue copy of \(H\). Suppose this does not happen. For every \(b\in B\), choose an index \(i(b)\) such that \(bz_{i(b)}\) is red. This partitions \(B\) into \(d\) classes, so one class \(B_i\) has size at least \(q\).

Every vertex of \(B_i\) is a red neighbour of \(z_i\). The red graph induced by \(B_i\) cannot contain \(J=G-x\): if it did, adding \(z_i\) as the image of \(x\) would give a red copy of \(G\). Extra red edges from \(z_i\) to vertices corresponding to non-neighbours of \(x\) do not matter because copies are not induced.

Since \(|B_i|\ge R(J,H)\) and \(F[B_i]\) is red-\(J\)-free, \(B_i\) contains a blue copy of \(H\). This proves (6). ∎

For the three fixed graphs, \(J\) can be chosen as follows:

\[
\begin{array}{c|c}
G & J=G-x\\ \hline
K_{3,3} & K_{2,3}\\
Q_3 & Q_3-x\\
H_5 & C_4.
\end{array}
\tag{7}
\]

For \(H_5\), use the representation with edges
\[
cd,ca,da,cb,db,ax,bx.
\]
Deleting \(c\) leaves the four-cycle
\[
d-a-x-b-d.
\]

The recurrence (6) is too expensive. Even if \(J\) were already known to be Ramsey size linear, it would only give
\[
R(G,H)\le R(G,H-v)+O\bigl(d_H(v)e(H)\bigr),
\]
not an \(O(d_H(v))\) increment. For a star, either deleting the centre or deleting leaves repeatedly leads to a quadratic bound through this recurrence. Thus descent to a red neighbourhood, by itself, does not close the induction.

---

### 4. A sharp pendant-vertex analysis

The degree-one case can be analyzed more precisely.

Let \(H'\) be a graph on \(h\) vertices with a distinguished vertex \(y\), and let \(H\) be obtained from \(H'\) by adding a new leaf adjacent to \(y\).

Define
\[
p_G(h)=
\max\left\{
n:\begin{array}{l}
\text{there exists a \(G\)-free graph \(F\) on \(n\) vertices}\\
\text{such that }\Delta(\overline F)\le h-1
\end{array}
\right\}.
\tag{8}
\]
This maximum is finite. Indeed, if \(g=v(G)\) and \(n>(g-1)h\), then any graph of maximum degree at most \(h-1\) has an independent set of size at least
\[
\left\lceil \frac nh\right\rceil\ge g.
\]
That independent set in \(\overline F\) is a red \(K_g\), which contains \(G\). Hence
\[
p_G(h)\le (g-1)h.
\tag{9}
\]

#### Lemma 2

With \(H,H'\) as above,
\[
R(G,H)\le R(G,H')+p_G(h).
\tag{10}
\]

#### Proof

Let
\[
r=R(G,H')
\]
and suppose that \(F\) is a \(G\)-free red graph on \(N\ge r\) vertices whose blue complement contains no \(H\).

Let \(Y\) be the set of vertices that can occur as the image of \(y\) in some blue embedding of \(H'\).

First,
\[
|V(F)\setminus Y|\le r-1.
\tag{11}
\]
Otherwise, an \(r\)-vertex subset of \(V(F)\setminus Y\) would contain a blue copy of \(H'\), and the image of \(y\) in that copy would belong to \(Y\), a contradiction.

Second, every \(z\in Y\) has blue degree at most \(h-1\). Choose a blue embedding of \(H'\) with \(y\) mapped to \(z\), on a set \(C\) of size \(h\). If \(z\) had a blue neighbour outside \(C\), that neighbour could serve as the added leaf, giving a blue \(H\). Therefore all blue neighbours of \(z\) lie in \(C\setminus\{z\}\).

It follows that the red graph \(F[Y]\) is \(G\)-free and
\[
\Delta(\overline{F[Y]})\le h-1.
\]
Thus
\[
|Y|\le p_G(h).
\]
Together with (11),
\[
N\le r-1+p_G(h).
\]
Consequently no avoiding colouring exists on \(r+p_G(h)\) vertices, proving (10). ∎

This lemma is global in the sense that it considers every possible image of the root, not just one fixed embedding. Nevertheless, \(p_G(h)\) is linear in \(h\) for all three graphs.

#### Extremal bound on \(p_G(h)\)

If \(F\) witnesses \(p_G(h)\) on \(n\) vertices, then every red degree is at least
\[
n-1-(h-1)=n-h.
\]
Hence
\[
\frac{n(n-h)}2\le e(F)\le \operatorname{ex}(n,G).
\tag{12}
\]

For \(K_{3,3}\), the Kővári–Sós–Turán theorem gives
\[
\operatorname{ex}(n,K_{3,3})\le A n^{5/3}
\]
for an absolute constant \(A\). From (12),
\[
n-h\le 2A n^{2/3}.
\tag{13}
\]
For sufficiently large \(h\), (13) first implies \(n<2h\): otherwise
\[
\frac n2\le 2A n^{2/3},
\]
which bounds \(n\) by an absolute constant. Substituting \(n<2h\) into (13) gives
\[
p_{K_{3,3}}(h)\le h+2A(2h)^{2/3}
=h+O(h^{2/3}).
\tag{14}
\]
Conversely, red \(K_{2,h}\) is \(K_{3,3}\)-free, and its blue complement is \(K_2\sqcup K_h\), of maximum degree \(h-1\). Thus
\[
p_{K_{3,3}}(h)\ge h+2
\tag{15}
\]
for \(h\ge2\). Therefore
\[
p_{K_{3,3}}(h)=h+O(h^{2/3}).
\tag{16}
\]

For \(Q_3\), Erdős–Stone gives
\[
\operatorname{ex}(n,Q_3)=o(n^2).
\]
If \(n>(1+\varepsilon)h\), then
\[
n-h>\frac{\varepsilon}{1+\varepsilon}n,
\]
so (12) would imply \(e(F)\ge c_\varepsilon n^2\), contradicting \(\operatorname{ex}(n,Q_3)=o(n^2)\) for sufficiently large \(n\). Hence
\[
p_{Q_3}(h)\le (1+o(1))h.
\tag{17}
\]
On the other hand, red \(K_{3,h}\) is \(Q_3\)-free: a connected bipartite copy of \(Q_3\) would have to send its two four-vertex bipartition classes into the two host parts, one of which has only three vertices. Its blue complement is \(K_3\sqcup K_h\). Thus
\[
p_{Q_3}(h)\ge h+3
\tag{18}
\]
for \(h\ge3\), and consequently
\[
p_{Q_3}(h)=(1+o(1))h.
\tag{19}
\]

For \(H_5\), Simonovits’s theorem gives, for sufficiently large \(n\),
\[
\operatorname{ex}(n,H_5)=\left\lfloor\frac{n^2}{4}\right\rfloor.
\]
If \(n>2h\), then
\[
\frac{n(n-h)}2>\frac{n^2}{4},
\]
contradicting (12). Hence
\[
p_{H_5}(h)\le 2h
\tag{20}
\]
for sufficiently large \(h\). Equality is attained by red \(K_{h,h}\), whose complement is \(K_h\sqcup K_h\) and which is \(H_5\)-free because it is bipartite. Therefore
\[
p_{H_5}(h)=2h
\tag{21}
\]
for all sufficiently large \(h\).

These estimates show that Lemma 2 necessarily pays \(\Theta(h)\), not \(O(1)\), for adding one leaf. Applying it one leaf at a time can therefore cost \(\Theta(m^2)\) on sparse connected targets.

---

### 5. A complete positive result for forest targets

Route 2 does succeed for forests, although this is far short of the problem.

Let \(g=v(G)\), and let \(T\) be a tree on \(n\) vertices. I claim
\[
R(G,T)\le (g-1)(n-1)+1.
\tag{22}
\]

Consider the blue graph \(B\) on
\[
N=(g-1)(n-1)+1
\]
vertices. If \(B\) contains no \(T\), then every subgraph of \(B\) has a vertex of degree at most \(n-2\). Indeed, every graph of minimum degree at least \(n-1\) contains every \(n\)-vertex tree: delete a leaf from the tree, embed the remaining tree inductively, and then map the deleted leaf to an unused neighbour of its parent. At most \(n-2\) other vertices have already been used, while the parent has at least \(n-1\) neighbours.

Thus a \(T\)-free graph is \((n-2)\)-degenerate and hence \((n-1)\)-colourable. One colour class has size at least
\[
\left\lceil\frac{N}{n-1}\right\rceil=g.
\]
That class is independent in blue and therefore is a red \(K_g\), which contains \(G\). This proves (22).

Now let \(H\) be a forest with no isolated vertices, with tree components \(T_1,\dots,T_c\), where \(T_i\) has \(n_i\) vertices. By (4) and (22),
\[
\begin{aligned}
R(G,H)
&\le \sum_{i=1}^c R(G,T_i)\\
&\le \sum_{i=1}^c\bigl((g-1)(n_i-1)+1\bigr)\\
&=(g-1)e(H)+c.
\end{aligned}
\]
Each component has at least one edge, so \(c\le e(H)\). Therefore
\[
R(G,H)\le g\,e(H).
\tag{23}
\]

In particular, forest targets satisfy the desired linear estimate with constants \(8,6,5\) for \(Q_3,K_{3,3},H_5\), respectively.

---

### 6. Why Route 2 remains blocked

The proven facts leave the following gap.

A fixed partial embedding cannot be extended locally: the red-star construction defeats any amount of reserve. Considering every possible rooted embedding gives Lemma 2, but its cost is \(\Theta(v(H))\) even for adding one leaf. Descending into a red neighbourhood gives Lemma 1, but costs \(d_H(v)R(G-x,H)\), which is generally at least \(d_H(v)v(H)\).

What is needed is a global switching theorem of approximately the following strength:

> Among the many blue copies of \(H-v\) forced throughout a \(G\)-free graph, one can either choose an extendable copy or combine several obstructed copies to produce a red \(G\), at a total reserve cost \(O_G(d_H(v))\).

No such theorem was proved here. Its clique specialization is already formidable: applying (1) to
\[
H=K_t,\qquad d_H(v)=t-1,
\]
and summing would yield
\[
R(G,K_t)=O_G(t^2).
\]
For \(G=K_{3,3}\), this is precisely the difficult off-diagonal benchmark identified in the problem brief. Thus the missing switching lemma contains an unresolved statement of comparable strength to the original problem.

## Self-Audit

1. **The estimates for \(p_G(h)\) use external extremal theorems.**  
   I used Kővári–Sós–Turán, Erdős–Stone, and the eventual exact Simonovits theorem for \(H_5\), rather than reproving them. These are standard results explicitly supplied in the brief. The deductions from them, particularly (12)–(21), are elementary and include the treatment of finite exceptional orders.

2. **The neighborhood-descent proof relies critically on non-induced copies.**  
   When a red copy of \(G-x\) lies inside a red neighbourhood, the added vertex may have extra red edges corresponding to nonedges incident with \(x\). This would fail for induced copies. Here copies are ordinary subgraphs, so extra edges are harmless and Lemma 1 is valid.

3. **The diagnosis does not prove that every possible edge-charged induction must fail.**  
   The counterexamples only refute fixed-copy extension and show that two natural global summaries incur linear-in-\(v(H)\) cost. A more sophisticated switching or absorption argument might still establish (1) or a block analogue. I nevertheless regard the current route as blocked because the missing lemma already implies the open quadratic \(K_{3,3}\)-versus-clique estimate, and none of the proved local information approaches that strength.

## Computations To Verify

The following brute-force code can verify small Ramsey numbers, the auxiliary parameter \(p_G(h)\), and proposed extension inequalities. It is practical only for small orders.

```python
from itertools import combinations, permutations

def norm_edge(a, b):
    return (a, b) if a < b else (b, a)

def all_edges(n):
    return list(combinations(range(n), 2))

def edge_set_from_mask(n, mask):
    E = all_edges(n)
    return {
        E[i] for i in range(len(E))
        if (mask >> i) & 1
    }

def complement_edges(n, E):
    return set(all_edges(n)) - set(E)

def has_copy(host_n, host_edges, pattern_n, pattern_edges):
    """Non-induced subgraph containment."""
    host_edges = set(host_edges)
    pattern_edges = set(pattern_edges)
    if host_n < pattern_n:
        return False

    for image in permutations(range(host_n), pattern_n):
        ok = True
        for a, b in pattern_edges:
            if norm_edge(image[a], image[b]) not in host_edges:
                ok = False
                break
        if ok:
            return True
    return False

def K33():
    E = {(a, b) for a in range(3) for b in range(3, 6)}
    return 6, E

def H5():
    # Cycle 0-1-2-3-4-0, chords 0-2 and 1-4.
    E = {
        norm_edge(0, 1), norm_edge(1, 2),
        norm_edge(2, 3), norm_edge(3, 4),
        norm_edge(4, 0), norm_edge(0, 2),
        norm_edge(1, 4)
    }
    return 5, E

def Q3():
    E = set()
    for x in range(8):
        for bit in (1, 2, 4):
            y = x ^ bit
            E.add(norm_edge(x, y))
    return 8, E

def exact_ramsey(G, H, max_N):
    g, GE = G
    h, HE = H

    for N in range(1, max_N + 1):
        M = len(all_edges(N))
        avoiding_exists = False

        for mask in range(1 << M):
            red = edge_set_from_mask(N, mask)
            blue = complement_edges(N, red)

            if (not has_copy(N, red, g, GE)
                    and not has_copy(N, blue, h, HE)):
                avoiding_exists = True
                break

        if not avoiding_exists:
            return N

    return None

def max_blue_degree(n, red):
    blue = complement_edges(n, red)
    deg = [0] * n
    for a, b in blue:
        deg[a] += 1
        deg[b] += 1
    return max(deg, default=0)

def p_exists(G, h, n):
    """Whether an n-vertex witness for p_G(h) exists."""
    g, GE = G
    M = len(all_edges(n))

    for mask in range(1 << M):
        red = edge_set_from_mask(n, mask)
        if has_copy(n, red, g, GE):
            continue
        if max_blue_degree(n, red) <= h - 1:
            return True
    return False

def exact_p_up_to(G, h, max_n):
    ans = 0
    for n in range(1, max_n + 1):
        if p_exists(G, h, n):
            ans = n
    return ans
```

Concrete checks:

1. For small \(h\), test whether
   ```python
   exact_p_up_to(H5(), h, 2*h + 1) == 2*h
   ```
   and similarly compare \(p_{K_{3,3}}(h)\) with \(h+2\), and \(p_{Q_3}(h)\) with \(h+3\).

2. Enumerate small no-isolate targets \(H\), compute \(R(G,H)\) and \(R(G,H-v)\), and record
   \[
   \frac{R(G,H)-R(G,H-v)}{d_H(v)}.
   \]
   Growth in this ratio would refute the strongest vertex-recurrence conjecture; bounded small values would only be supporting evidence.

3. A SAT test for the actual switching problem should impose:

   ```text
   variables x_ab = 1 iff ab is red

   clauses:
     - forbid every red copy of G;
     - force a specified copy of H-v to be blue;
     - for every reserve vertex z, require at least one red edge
       from z to the images of N_H(v);
     - optionally forbid every blue copy of H globally.
   ```

   The third condition is the clause
   \[
   \bigvee_{u\in N_H(v)} x_{\phi(u),z}.
   \]
   Without the final global condition, the red-star construction always gives examples. With it, the SAT instance searches for genuine failures of relocation rather than merely failures of a fixed embedding.

4. Hybrid targets should be prioritized: a clique on \(t\) vertices with a large star or many pendant trees attached to one clique vertex. These simultaneously test the high-chromatic, high-degree, and leaf-extension bottlenecks.

## Route Diagnosis

**Proved ledger**

- An additive recurrence \(R(G,H)\le R(G,H-v)+C_Gd_H(v)\) would imply \(R(G,H)=O_G(e(H))\).
- Isolated vertices cost at most one each, and Ramsey numbers are subadditive over target components.
- A prescribed blue copy of \(H-v\) can be unextendable despite an arbitrarily large reserve, even when the red graph is a star.
- The neighborhood-descent recurrence (6) is valid.
- The global pendant-root bound (10) is valid.
- The corresponding parameters satisfy
  \[
  p_{K_{3,3}}(h)=h+O(h^{2/3}),\quad
  p_{Q_3}(h)=(1+o(1))h,\quad
  p_{H_5}(h)=2h
  \]
  in the stated asymptotic sense.
- All forest targets satisfy \(R(G,H)\le v(G)e(H)\).

**Plausible but unproved**

- A global switching or absorption lemma might select an extendable copy among all copies of \(H-v\) at cost \(O_G(d_H(v))\).
- For \(H_5\), stability around the red complete-bipartite configuration may make such switching possible, but concentration of exceptional red edges remains uncontrolled.
- A block-deletion inequality may be more realistic than one-vertex deletion, especially if pendant forests and a chromatic core are processed together.

**Dead ends**

- Extending an arbitrary fixed copy: refuted by the red-star construction.
- Turning a union of red neighbourhoods into a common-neighbour certificate for \(G\): the star construction shows that the obstruction may be a disjoint union of red stars, with no useful intersections.
- Descending into one red neighbourhood: rigorous but costs \(dR(G-x,H)\), which is too large.
- Tracking all possible root images: rigorous but costs \(\Theta(v(H))\) per leaf, and this scale is sharp for the auxiliary information used.

A fresh Route 2 attempt must therefore incorporate global relocation of the embedded target, not merely larger reservoirs. For \(K_{3,3}\) and \(Q_3\), it should first be tested on clique targets because any successful induction must recover a quadratic off-diagonal bound. For \(H_5\), the most promising modification is a Route 2/Route 4 hybrid: use stability to identify large blue clique-like regions, then prove a switching lemma that moves the critical nonbipartite core and all attached trees simultaneously.