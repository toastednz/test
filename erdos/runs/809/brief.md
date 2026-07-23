# Problem brief: Erdős Problem #809

## 1. Precise statement

All graphs below are finite, simple, and undirected.

For integers \(n,e\ge 0\) with \(e\le \binom n2\), and a fixed graph \(G\), let
\[
\mathcal H_{n,e}=\{H: |V(H)|=n,\ |E(H)|=e\}.
\]
For \(r\ge 1\), an \(r\)-edge-coloring of \(H\) is a map
\[
c:E(H)\to [r]=\{1,\dots,r\}.
\]
Surjectivity is immaterial: at a minimum, unused colors can be deleted.

A copy of \(G\) in \(H\) means a not-necessarily-induced subgraph isomorphic to \(G\), equivalently an injective map
\[
\varphi:V(G)\hookrightarrow V(H)
\]
such that \(\varphi(u)\varphi(v)\in E(H)\) whenever \(uv\in E(G)\). This copy is **rainbow** if
\[
uv\longmapsto c(\varphi(u)\varphi(v))
\]
is injective on \(E(G)\).

Define
\[
\chi_S(n,e,G)
=
\min\left\{
r:\ \exists H\in\mathcal H_{n,e}\ \exists c:E(H)\to[r]
\text{ such that every copy of }G\text{ in }H\text{ is rainbow}
\right\}.
\]
Thus the minimization is over both the host graph and its edge-coloring.

If an admissible host \(H\) is \(G\)-free, the condition is vacuous and \(\chi_S(n,e,G)=1\) under this convention. This issue is irrelevant asymptotically here because of the exact extremal theorem for odd cycles, but it matters for small \(n\).

Let
\[
t_2(n)=\left\lfloor \frac{n^2}{4}\right\rfloor.
\]
The problem asks whether, for every fixed integer \(k\ge 3\),
\[
\chi_S\bigl(n,t_2(n)+1,C_{2k+1}\bigr)\sim \frac{n^2}{8}
\qquad (n\to\infty).
\]
Formally, this means:

> For every fixed \(k\ge 3\) and every \(\varepsilon>0\), there is \(N=N(k,\varepsilon)\) such that for every \(n\ge N\),
> \[
> (1-\varepsilon)\frac{n^2}{8}
> \le
> \chi_S\bigl(n,t_2(n)+1,C_{2k+1}\bigr)
> \le
> (1+\varepsilon)\frac{n^2}{8}.
> \]

The quantification is pointwise in fixed \(k\); no uniformity in \(k\) is asserted.

### Current reduction of the open problem

Bucić, Chen, and Ma proved the assertion for every fixed \(k\ge 4\). Therefore the only unresolved case in the stated range is
\[
\boxed{\chi_S\bigl(n,t_2(n)+1,C_7\bigr)\sim \frac{n^2}{8}.}
\]

Moreover, an elementary construction gives the upper bound
\[
\chi_S\bigl(n,t_2(n)+1,C_7\bigr)\le \frac{n^2}{8}+O(n).
\]
Consequently, the substantive remaining task is the universal lower bound
\[
\boxed{\chi_S\bigl(n,t_2(n)+1,C_7\bigr)\ge \frac{n^2}{8}-o(n^2).}
\]

Since \(t_2(n)+1=n^2/4+O(1)\), this is equivalently
\[
\chi_S\bigl(n,t_2(n)+1,C_7\bigr)\ge \frac{e}{2}-o(n^2),
\qquad e=t_2(n)+1.
\]

### Useful reformulation by a conflict graph

For a host graph \(H\), define the \(C_7\)-conflict graph \(Q_7(H)\) by

- \(V(Q_7(H))=E(H)\);
- two distinct edges \(f,g\in E(H)\) are adjacent in \(Q_7(H)\) if some copy of \(C_7\) in \(H\) contains both \(f\) and \(g\).

Then an edge-coloring of \(H\) makes every \(C_7\) rainbow if and only if it is a proper vertex-coloring of \(Q_7(H)\). Hence
\[
\chi_S(n,e,C_7)=\min_{H\in\mathcal H_{n,e}}\chi(Q_7(H)).
\]

Equivalently, let \(I_7(H)=\overline{Q_7(H)}\). Each color class must be a clique in \(I_7(H)\), i.e. a set of edges no two of which occur together on a \(7\)-cycle.

---

## 2. What counts as a solution

### Complete affirmative solution

Given the known theorem for \(k\ge 4\), a complete affirmative resolution of the open part must prove:

> For every \(\varepsilon>0\), there exists \(N(\varepsilon)\) such that whenever \(n\ge N(\varepsilon)\), \(H\) is any \(n\)-vertex graph with exactly \(t_2(n)+1\) edges, and \(c\) is any edge-coloring of \(H\) under which every copy of \(C_7\) is rainbow, then \(c\) uses at least
> \[
> (1-\varepsilon)\frac{n^2}{8}
> \]
> distinct colors.

This is universal over all host graphs \(H\) with the exact edge count and all valid colorings. Proving the lower bound only for a selected or “natural” host graph does not suffice.

Together with the explicit upper construction below, this would establish
\[
\chi_S\bigl(n,t_2(n)+1,C_7\bigr)=\frac{n^2}{8}+o(n^2).
\]

A new proof of the upper bound is not essential if the elementary construction is cited and checked correctly.

### Complete disproof

Because there is already an upper bound \(n^2/8+O(n)\), a disproof must show that the quantity is bounded away below \(n^2/8\) along an infinite sequence. Concretely, it is enough to exhibit:

- a constant \(\delta>0\);
- infinitely many integers \(n_j\to\infty\);
- explicit graphs \(H_j\) with
  \[
  |V(H_j)|=n_j,\qquad |E(H_j)|=t_2(n_j)+1;
  \]
- explicit edge-colorings \(c_j\) using at most
  \[
  (1-\delta)\frac{n_j^2}{8}
  \]
  colors;

such that every \(C_7\) in \(H_j\) has seven pairwise distinct edge colors.

For verification, it is enough to prove that whenever two edges receive the same color, no simple \(7\)-cycle of \(H_j\) contains both.

A single finite example does not disprove an asymptotic statement. An infinite parametrized family, together with a rigorous proof of its edge count, color count, and rainbow property, is required.

---

## 3. What does not count

The following do not resolve the remaining problem:

1. **Another positive constant lower bound**
   \[
   \chi_S(n,t_2(n)+1,C_7)\ge c n^2
   \]
   with \(c<1/8\). This is already known qualitatively from Burr–Erdős–Graham–Sós.

2. **Only an upper bound**
   \[
   \chi_S(n,t_2(n)+1,C_7)\le \frac{n^2}{8}+o(n^2).
   \]
   An \(O(n)\)-error upper bound is elementary.

3. **A lower bound for one host graph.** Since \(\chi_S\) minimizes over hosts, the lower bound must cover every \(H\) with exactly \(t_2(n)+1\) edges.

4. **Results for \(k\ge 4\).** Those cases are already settled affirmatively. The open case is \(k=3\), namely \(C_7\).

5. **Results for \(C_3\) or \(C_5\).** These lie outside \(k\ge3\) and behave differently.

6. **An asymptotic lower bound with the wrong leading constant**, such as
   \[
   \left(\frac18-\delta\right)n^2.
   \]

7. **A result for edge counts \(t_2(n)+\omega(1)\)** or \((1/4+\delta)n^2\). The problem concerns the exact near-extremal count \(t_2(n)+1\). Standard supersaturation at positive density above \(1/4\) does not address this regime.

8. **A coloring in which every \(C_7\) uses many colors but not necessarily seven.** Every individual \(C_7\) must be fully rainbow.

9. **A coloring forcing the existence of one rainbow \(C_7\).** The requirement is that every \(C_7\) in the selected host be rainbow.

10. **Conditional, probabilistic, or heuristic conclusions** without removal of the condition or a deterministic existence proof.

11. **Computations for finitely many \(n\)** without an argument extending to an infinite sequence or all sufficiently large \(n\).

---

## 4. Known results and context

### Burr–Erdős–Graham–Sós

Burr, Erdős, Graham, and Sós proved that for every fixed \(k\),
\[
\chi_S\bigl(n,t_2(n)+1,C_{2k+1}\bigr)\gg_k n^2.
\]
Thus there is a constant \(c_k>0\) such that, for all sufficiently large \(n\),
\[
\chi_S\bigl(n,t_2(n)+1,C_{2k+1}\bigr)\ge c_k n^2.
\]
This establishes the correct order of magnitude but not the conjectured leading constant \(1/8\).

### Bucić–Chen–Ma

Bucić, Chen, and Ma proved
\[
\chi_S\bigl(n,t_2(n)+1,C_{2k+1}\bigr)\sim \frac{n^2}{8}
\]
for every fixed \(k\ge 4\). Thus all cycle lengths
\[
C_9,C_{11},C_{13},\dots
\]
are settled. Their proof should be treated as the primary source to audit for a possible \(C_7\) extension: one must identify exactly where length at least \(9\) is used.

### The exceptional shorter odd cycles

The shorter cycles behave very differently:

- For triangles,
  \[
  \chi_S\bigl(n,t_2(n)+1,C_3\bigr)=3
  \]
  in the relevant range. The standard host is a balanced complete bipartite graph plus one edge inside a part.

- Erdős and Simonovits proved, as reported in BEGS,
  \[
  \chi_S\bigl(n,t_2(n)+1,C_5\bigr)=\left\lfloor\frac n2\right\rfloor+3
  \]
  for all sufficiently large \(n\).

Thus the sequence of orders is:
\[
C_3:\Theta(1),\qquad C_5:\Theta(n),\qquad C_7:\Theta(n^2),
\]
with the precise quadratic constant for \(C_7\) still open.

### Exact odd-cycle extremal theorem

An odd cycle is a color-critical \(3\)-chromatic graph. By Simonovits’s exact theorem for color-critical graphs, for every fixed \(\ell\ge 2\),
\[
\operatorname{ex}(n,C_{2\ell+1})=t_2(n)
\]
for all sufficiently large \(n\).

Therefore every sufficiently large \(n\)-vertex graph with \(t_2(n)+1\) edges contains \(C_{2\ell+1}\). The rainbow condition is consequently nonvacuous asymptotically. This need not hold for small \(n\).

### Elementary upper construction

The upper bound \(n^2/8+O(n)\) can be obtained by a graph whose cycles are confined to one of two dense pieces.

#### Even \(n=2q\)

Take disjoint sets
\[
|A|=q-1,\qquad |B|=q+1.
\]
Put complete graphs on \(A\) and \(B\). Choose \(x\in A\), choose \(S\subseteq B\) with \(|S|=q\), and add all edges \(xs\), \(s\in S\). Then
\[
|E(H)|
=
\binom{q-1}{2}+\binom{q+1}{2}+q
=
q^2+1
=
t_2(n)+1.
\]

#### Odd \(n=2q+1\)

Take
\[
|A|=q,\qquad |B|=q+1.
\]
Put complete graphs on \(A\) and \(B\). Choose \(x\in A\) and join \(x\) to every vertex of \(B\). Then
\[
|E(H)|
=
\binom q2+\binom{q+1}{2}+(q+1)
=
q(q+1)+1
=
t_2(n)+1.
\]

In either case:

- color all edges of \(K_B\) distinctly;
- color all edges of \(K_A\) distinctly, reusing colors from \(K_B\) injectively;
- give all \(A\)-\(B\) edges fresh, pairwise distinct colors.

Any simple cycle is either contained in \(A\), contained in \(B\), or consists of \(x\), two cross edges, and a path inside \(B\). No cycle contains both an internal \(A\)-edge and an internal \(B\)-edge. Hence every cycle, in particular every \(C_7\), is rainbow.

The number of colors is
\[
\binom{q+1}{2}+O(q)=\frac{n^2}{8}+O(n).
\]

This explains the conjectured constant: two clique palettes of size approximately \(n^2/8\) can be reused because the corresponding edge sets never occur together on a cycle.

---

## 5. Traps and edge cases

1. **Minimum over host graphs.**  
   For an upper bound, one construction suffices. For a lower bound, every host with the prescribed edge count must be handled.

2. **Exact edge count.**  
   The host must have exactly \(t_2(n)+1\) edges. A construction with \(t_2(n)+O(n)\) or \((1/4+o(1))n^2\) edges is not automatically admissible.

3. **Small-\(n\) vacuity.**  
   If \(n<7\), no \(C_7\) exists. Even for some \(n\ge7\), \(t_2(n)+1\) need not force a \(C_7\). The conjecture is asymptotic.

4. **Non-induced cycles.**  
   A \(C_7\) may have chords in the host. The seven chosen cycle edges must be distinct in color; chord colors are irrelevant to that particular copy.

5. **Not merely a proper edge-coloring.**  
   Two disjoint or nonincident edges may be forced to have different colors if some \(C_7\) contains both.

6. **Pairwise formulation is exact.**  
   A coloring is valid precisely when no two same-colored edges lie on a common \(C_7\). This should be used instead of checking entire color sequences ad hoc.

7. **Stability at density \(1/4\) is delicate.**  
   The edge excess is only one. Ordinary removal or supersaturation estimates with \(o(n^2)\) losses may erase the only information distinguishing \(t_2(n)\) from \(t_2(n)+1\).

8. **The host need not resemble a balanced complete bipartite graph.**  
   For example, a dense clique plus isolated vertices can also have approximately \(n^2/4\) edges. A proof cannot assume Turán stability merely from the edge count.

9. **Counting cycles alone may be insufficient.**  
   There can be very few \(C_7\)'s at this exact threshold, and their overlap structure matters more than their number.

10. **Color classes can be large.**  
    It is false in general that every color appears at most twice. Edges in different cycle-separated blocks can safely reuse a color.

11. **Conflict-edge counts do not directly give chromatic number.**  
    Showing that \(Q_7(H)\) has many edges is not enough to conclude \(\chi(Q_7(H))\ge n^2/8-o(n^2)\).

12. **Clique number is also insufficient by itself.**  
    The desired lower bound concerns the chromatic number of \(Q_7(H)\), not just the largest family of pairwise co-cyclic host edges.

13. **Deleting edges is one-directional.**  
    If a colored graph is valid, deleting edges preserves validity. But a lower-bound argument cannot freely add or delete \(o(n^2)\) edges without controlling the coloring and the exact threshold.

14. **Parity and floors matter in constructions.**  
    The formulas for even and odd \(n\) differ by linear terms. They are negligible asymptotically but essential for an exact admissible host.

15. **Graphon limits lose the \(+1\).**  
    At graphon scale, the edge density is exactly \(1/2\) relative to \(\binom n2\), and the balanced bipartite graphon is \(C_7\)-free. A first-order graphon argument cannot see the one-edge excess.

16. **A finite low value does not refute the limit.**  
    Computational anomalies at \(n=7,8,\dots\) may be caused by failure of exact odd-cycle extremal behavior in the small range.

---

## 6. Verification hooks

### 6.1 Constructing the conflict graph

Given a host \(H\):

1. Create one vertex of \(Q_7(H)\) for each edge of \(H\).
2. Enumerate all simple \(7\)-cycles in \(H\).
3. For each such cycle, add all \(\binom72=21\) conflict edges between its seven host edges.

Then
\[
\chi(Q_7(H))
\]
is exactly the minimum number of colors making all \(C_7\)'s rainbow.

A direct cycle enumeration can use:

- all \(7\)-subsets of \(V(H)\), followed by Hamilton-cycle enumeration in the induced subgraph; or
- depth-first search for simple paths of length \(6\), closed by an edge.

Canonicalization is needed to avoid counting rotations and reversals repeatedly, though duplicates do not affect correctness.

### 6.2 Checking a proposed coloring

It is enough to iterate over every pair \(e,f\) with \(c(e)=c(f)\) and test whether a simple \(7\)-cycle contains both. If one does, the coloring is invalid.

For adjacent \(e=uv\), \(f=vw\), this reduces to finding a simple \(u\)-\(w\) path of length \(5\) avoiding \(v\).

For disjoint edges \(e=uv\), \(f=xy\), one may test the finitely many cyclic endpoint orders. The remaining five cycle edges split into two internally vertex-disjoint connecting paths between suitable endpoint pairs.

Because the target length is fixed, bounded-depth color-coding, subset dynamic programming, or explicit DFS is practical.

### 6.3 Computing \(\chi(Q_7(H))\)

For fixed \(H\), use:

- DSATUR or branch-and-bound;
- SAT encoding for \(r\)-colorability;
- an ILP with binary variables \(x_{f,i}\), constraints
  \[
  \sum_i x_{f,i}=1,
  \qquad
  x_{f,i}+x_{g,i}\le1
  \]
  whenever \(fg\in E(Q_7(H))\).

Binary search on \(r\) gives the exact chromatic number for modest instances.

### 6.4 Joint host/color search

For small \(n\), a SAT/SMT model can use:

- host variables \(h_{uv}\in\{0,1\}\);
- the exact constraint
  \[
  \sum_{u<v} h_{uv}=t_2(n)+1;
  \]
- color variables for present edges;
- for every ordered \(7\)-tuple of distinct vertices, an implication:
  if its seven cycle edges are present, their colors are pairwise distinct.

Strong symmetry breaking is essential:

- fix vertex degree order;
- fix the first-used color convention;
- quotient host graphs by isomorphism where possible.

### 6.5 Testing structural conjectures

For generated hosts, compute:

- blocks and cut vertices of \(H\);
- connected components of \(Q_7(H)\);
- maximal cliques of \(I_7(H)=\overline{Q_7(H)}\);
- whether maximal \(I_7(H)\)-cliques are stars, cuts, or unions of cycle-separated blocks;
- the degree distribution in \(Q_7(H)\);
- for each edge pair, the number of \(C_7\)'s containing it.

These data can test candidate classification lemmas before attempting a proof.

### 6.6 Checking the elementary upper construction

For both parity cases, code should verify symbolically or for sample \(q\):

- vertex count;
- edge count \(t_2(n)+1\);
- number of colors;
- every cross-block cycle is contained in \(B\cup\{x\}\);
- no repeated-color pair lies on a common cycle.

This provides a baseline construction against which automated searches should be compared.

---

## 7. Attack routes

### Route 1: Extend the Bucić–Chen–Ma argument to \(C_7\)

**Core mechanism.**  
Audit the proof for \(C_{2k+1}\), \(k\ge4\), and isolate every use of \(2k+1\ge9\). The likely obstruction is a rooted path-extension or connector lemma that requires more spare vertices than a \(7\)-cycle allows.

**Key lemma needed.**  
A \(C_7\)-specific replacement for the BCM linkage lemma: under the structural hypotheses forced by too few colors, two same-colored edges must admit internally disjoint connecting paths whose total length completes a simple \(7\)-cycle.

For adjacent marked edges, this means a length-\(5\) path between their free endpoints. For disjoint marked edges, it means two disjoint endpoint-connecting paths with total length \(5\).

**Why it might work.**  
All longer odd cycles are already settled, so the missing issue may be a finite family of short connector configurations. A careful classification could replace a general long-cycle argument with several \(C_7\)-specific lemmas.

**Most likely failure point.**  
The length condition may be genuinely sharp: configurations may support the longer detours used for \(C_9\) while forbidding every corresponding \(C_7\). Such configurations could be abundant enough to affect the leading constant.

**Quick obstruction test.**  
Generate dense hosts and list edge pairs that lie on a \(C_9\) but on no \(C_7\). Compare their local rooted neighborhoods with the exceptional configurations in the BCM proof. If these pairs occur with quadratic multiplicity in near-optimal constructions, a direct shortening is blocked.

---

### Route 2: Dense-block and fixed-length linkage decomposition

**Core mechanism.**  
Decompose \(H\) into regions in which most pairs of edges lie together on a \(C_7\), separated by cut vertices, sparse interfaces, or exceptional low-connectivity structures. Palette reuse is possible mainly between regions that no \(C_7\) can visit simultaneously, as in the two-clique upper construction.

Relevant classical tools include Menger-type linkage, block decomposition, and pancyclicity results such as Bondy’s theorem, although none directly gives the needed fixed-length, two-marked-edge statement.

**Key lemma needed.**  
A structural theorem of the following type:

> After discarding \(o(n^2)\) exceptional edges, \(E(H)\) can be partitioned into robust \(C_7\)-linkage blocks such that any two edges in the same block lie on a common \(C_7\), while the edge-count constraint forces the largest block-palette cost to be at least \(n^2/8-o(n^2)\).

A more flexible version may allow each block conflict graph to have chromatic number close to half its edge count.

**Why it might work.**  
The extremal upper construction is organized by cycle-separated blocks. A sharp lower bound may amount to proving that all other structures are at least as expensive in colors.

**Most likely failure point.**  
Fixed cycle length is much more rigid than unrestricted common-cycle membership. Dense graphs can contain many \(C_7\)'s without every relevant edge pair sharing one, and sparse interfaces may contribute quadratically many reusable pairs.

**Quick obstruction test.**  
For small and heuristic near-minimizing hosts, compare:

- ordinary blocks of \(H\);
- components of \(Q_7(H)\);
- maximal dense subgraphs;
- the chromatic contribution of each conflict component.

If \(Q_7(H)\) repeatedly cuts across ordinary block structure in complicated ways, a simple decomposition theorem is unlikely.

---

### Route 3: Classify large color classes and charge palette savings

**Core mechanism.**  
Let the color classes have sizes \(s_1,\dots,s_r\). Since
\[
e=\sum_i s_i,
\qquad
e-r=\sum_i(s_i-1),
\]
the desired lower bound \(r\ge e/2-o(n^2)\) is equivalent to
\[
\sum_i(s_i-1)\le \frac e2+o(n^2).
\]

Each color class is a clique in \(I_7(H)\): every pair of its edges avoids common membership in a \(C_7\). Classify such pairwise \(C_7\)-incompatible edge families and charge each unit of color saving to a limited structural resource.

**Key lemma needed.**  
A theorem asserting that every large set \(F\subseteq E(H)\) with no \(C_7\) containing two edges of \(F\) is structurally close to one of a short list, for example:

- edges isolated in different cycle blocks;
- edges concentrated on a cut interface;
- a star or near-star around a separator;
- edges in components that cannot be jointly traversed by a \(7\)-cycle.

The global edge budget must then imply that the total savings over all color classes are at most \(e/2+o(n^2)\).

**Why it might work.**  
The coloring condition is pairwise, so this route attacks exactly the correct object rather than merely counting cycles. It also naturally accommodates large color classes created by block separation.

**Most likely failure point.**  
Even if each color class is classifiable, different classes may overlap the same separators or exceptional structures, defeating a naive summation. A local bound on one class need not globalize.

**Quick obstruction test.**  
Enumerate maximal cliques of \(I_7(H)\) for candidate extremal hosts and cluster them by support pattern. Search for large incompatible families that are neither star-like nor separated by a small vertex cut.

---

### Route 4: Spectral or path-count inequalities with marked edges

**Core mechanism.**  
A \(C_7\) containing two specified edges can be expressed through short path counts:

- adjacent marked edges require a simple length-\(5\) path between their free endpoints;
- disjoint marked edges require two internally disjoint paths whose lengths sum to \(5\).

Use adjacency-matrix powers, nonbacktracking operators, or explicit simple-path kernels to show that too many same-color pairs force one of these marked-cycle configurations.

**Key lemma needed.**  
A weighted fixed-length supersaturation statement. One possible form is:

> If \(H\) has \(t_2(n)+1\) edges and its edges are partitioned into fewer than \(n^2/8-o(n^2)\) classes, then some class contains two edges with positive simple-\(C_7\) linkage count.

The estimate must remain effective at one edge above the Turán threshold and must handle highly irregular graphs.

**Why it might work.**  
Length \(7\) is small enough that every positional type of two marked edges can be written explicitly. Matrix inequalities may convert the edge density and color multiplicities into a forced positive linkage count.

**Most likely failure point.**  
Adjacency powers count walks, not simple paths. Backtracking and repeated vertices dominate in graphs with hubs or cut vertices—the exact structures used by the upper construction. Moreover, ordinary spectral estimates lose the \(+1\) threshold.

**Quick obstruction test.**  
Evaluate the proposed path kernels on:

- the elementary two-clique-plus-star construction;
- a clique plus isolated vertices;
- balanced bipartite graphs plus one internal edge;
- random graphs with the same edge count.

If the inequality predicts false positive \(C_7\)-linkage for repeated-color pairs in the upper construction, it is counting non-simple walks and needs substantial correction.

---

### Route 5: Color-aware symmetrization and finite-template reduction

**Core mechanism.**  
Attempt a Zykov-style compression or cloning procedure on a minimizing pair \((H,c)\), replacing vertices with twins and moving edges so that:

- the edge count remains \(t_2(n)+1\);
- no new nonrainbow \(C_7\) is created;
- the number of colors does not increase.

If successful, a minimizer could be reduced to a blow-up of a bounded template with a controlled color-reuse pattern.

**Key lemma needed.**  
A color-aware symmetrization lemma showing that one of two vertices can be cloned to the other, together with a recoloring of only \(o(n^2)\) edges, without increasing the leading-order color count or violating the rainbow-\(C_7\) condition.

The resulting templates would then be solved by a finite quadratic optimization.

**Why it might work.**  
The known upper construction is a very low-complexity template. Extremal graph problems near a sharp density threshold often admit such reductions.

**Most likely failure point.**  
Ordinary symmetrization preserves forbidden-subgraph conditions but not this coloring condition. Cloning a vertex can create new \(C_7\)'s containing two pre-existing same-colored edges, so monotonicity is absent.

**Quick obstruction test.**  
For small valid colored hosts, perform all local clone/delete-add operations and recompute \(Q_7(H)\). If almost every symmetrization increases \(\chi(Q_7(H))\) or invalidates the inherited coloring, a direct Zykov method is blocked.

---

### Route 6: Disproof via a new block or blow-up construction

**Core mechanism.**  
Search for an infinite family improving on the two-clique palette size by exploiting separators, short-cycle obstructions, or a finite blow-up template in which many edge families can reuse colors without any repeated-color pair appearing on a \(C_7\).

The goal is a construction with
\[
t_2(n)+1
\]
edges and at most
\[
\left(\frac18-\eta\right)n^2
\]
colors for some fixed \(\eta>0\).

**Key lemma or certificate needed.**  
A finite template \(T\), rational cluster sizes, and a symbolic coloring rule such that:

1. the blow-up has edge density \(1/2+o(1)\) relative to \(\binom n2\), adjustable to the exact edge count;
2. the number of color labels is \((1/8-\eta)n^2+o(n^2)\);
3. every two same-colored blown-up edges are excluded from every simple \(7\)-cycle by a type-level obstruction.

**Why it might work.**  
The fact that \(C_7\) remains exceptional after \(C_9,C_{11},\dots\) were solved suggests there may be genuinely short-cycle-specific templates. Cut vertices and star interfaces already allow substantial palette reuse.

**Most likely failure point.**  
Reaching \(t_2(n)+1\) edges tends to require enough dense coupling that a \(C_7\) can traverse two reused palettes. Type-level walks may also lift to simple \(7\)-cycles even when the quotient template appears harmless.

**Quick obstruction test.**  
Set up a finite-template SAT/ILP search:

- choose \(3\)–\(8\) vertex types;
- choose allowed complete/empty bipartite pairs and internal clique types;
- enumerate all type patterns of simple \(7\)-cycles, including repeated types represented by distinct blow-up vertices;
- optimize the quadratic edge density and quadratic color count subject to same-color incompatibility.

Any candidate must then be instantiated for moderate \(n\) and checked by the conflict-graph algorithm.

---

## 8. Verdict on difficulty

This is a serious research-level extremal coloring problem. The original infinite family is mostly solved, but the remaining \(C_7\) case is not a routine endpoint:

\[
\boxed{\text{The whole open problem is now the sharp lower bound for }C_7.}
\]

The elementary upper construction fixes the target constant, and BEGS gives only an unspecified positive quadratic lower bound. Thus the gap is not one of order of magnitude but of a sharp leading constant at the extremely delicate edge threshold \(t_2(n)+1\).

The principal difficulty is that:

- the host is optimized as well as the coloring;
- the surplus over the odd-cycle extremal number is only one edge;
- the condition depends on co-occurrence of pairs of edges in a fixed-length simple cycle;
- cut vertices and block structure permit extensive color reuse;
- methods that work for cycles of length at least \(9\) apparently do not directly cover \(C_7\).

No equivalence to a famous unresolved conjecture is presently evident. Nevertheless, the failure of the recent \(k\ge4\) theorem to include \(k=3\) should be taken as strong evidence that a genuinely new short-cycle argument—or a counterexample construction—may be required.