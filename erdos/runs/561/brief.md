# Problem Brief: Erdős Problem #561 — Asymmetric Size Ramsey Numbers of Star Forests

## 1. Precise statement

### 1.1 Graph-theoretic conventions

All graphs are finite, undirected, and simple unless explicitly stated otherwise.

For an integer \(q\ge 1\), let \(K_{1,q}\) denote the star with one center, \(q\) leaves, \(q+1\) vertices, and \(q\) edges.

Let \(s,t\ge 1\), and let
\[
n_1\ge n_2\ge \cdots \ge n_s\ge 1,\qquad
m_1\ge m_2\ge \cdots \ge m_t\ge 1
\]
be integers. Define the star forests
\[
F_1=\bigsqcup_{i=1}^{s}K_{1,n_i},
\qquad
F_2=\bigsqcup_{j=1}^{t}K_{1,m_j},
\]
where \(\bigsqcup\) denotes vertex-disjoint union. Thus different star components have disjoint centers and disjoint leaf sets.

A copy of a graph means a not-necessarily-induced subgraph isomorphic to that graph. Extra edges among the chosen vertices do not matter.

### 1.2 Asymmetric size Ramsey number

For graphs \(G_1,G_2\), write
\[
H\longrightarrow (G_1,G_2)
\]
if every map
\[
c:E(H)\to\{\mathrm{red},\mathrm{blue}\}
\]
has either:

- a red subgraph isomorphic to \(G_1\), or
- a blue subgraph isomorphic to \(G_2\).

The asymmetric size Ramsey number is
\[
\widehat R(G_1,G_2)
=
\min\left\{
|E(H)|:\ H\text{ is a finite simple graph and }H\to(G_1,G_2)
\right\}.
\]
The usual one-argument notation satisfies
\[
\widehat R(G)=\widehat R(G,G).
\]

The database statement first defines the symmetric notation and then writes \(\widehat R(F_1,F_2)\); the standard and intended interpretation is the asymmetric definition above.

### 1.3 The proposed formula

For each integer \(k\) with \(2\le k\le s+t\), define
\[
I_k=
\left\{
(i,j)\in\mathbb Z^2:
1\le i\le s,\ 1\le j\le t,\ i+j=k
\right\}.
\]
Every \(I_k\) in this range is nonempty. Set
\[
l_k
=
\max_{(i,j)\in I_k}
\bigl(n_i+m_j-1\bigr),
\]
and
\[
L=L(n_1,\ldots,n_s;m_1,\ldots,m_t)
=
\sum_{k=2}^{s+t}l_k.
\]

The problem asks for a proof that, for every choice of the above parameters,
\[
\boxed{\widehat R(F_1,F_2)=L.}
\]

The quantities \(l_k\) are nonincreasing:
\[
l_2\ge l_3\ge\cdots\ge l_{s+t}.
\]
Indeed, any admissible pair on the \((k+1)\)-st antidiagonal can be shifted one step toward a valid pair on the \(k\)-th antidiagonal, increasing one of the indices backward and therefore not decreasing the relevant \(n_i\) or \(m_j\).

The problem excludes \(s=0\) or \(t=0\). Allowing an empty forest would require separate conventions and would trivialize one side of the arrow relation.

---

## 2. What counts as a solution

### 2.1 The upper bound is already elementary

A complete treatment should record the following universal construction:
\[
H^\star=\bigsqcup_{k=2}^{s+t}K_{1,l_k}.
\]
It has exactly \(L\) edges.

To prove
\[
H^\star\to(F_1,F_2),
\]
initialize \(i=j=1\). At the stage corresponding to the component
\[
K_{1,l_{i+j}},
\]
let \(r\) be its number of red edges and \(b=l_{i+j}-r\) its number of blue edges.

- If \(r\ge n_i\), select a red \(K_{1,n_i}\) and replace \(i\) by \(i+1\).
- Otherwise \(r\le n_i-1\), and
  \[
  b
  \ge l_{i+j}-(n_i-1)
  \ge (n_i+m_j-1)-(n_i-1)
  =m_j.
  \]
  Select a blue \(K_{1,m_j}\) and replace \(j\) by \(j+1\).

At each step \(i+j\) increases by one, so a new component of \(H^\star\) is used. After at most \(s+t-1\) steps, either \(i=s+1\), producing all \(s\) red star components of \(F_1\), or \(j=t+1\), producing all \(t\) blue star components of \(F_2\). Because the components of \(H^\star\) are vertex-disjoint, the selected stars are also vertex-disjoint.

Therefore
\[
\widehat R(F_1,F_2)\le L
\]
for all parameters.

### 2.2 What a complete proof must establish

Since the upper bound is unconditional, the unresolved content is exactly the lower bound:

> For every choice of \(s,t,n_1,\ldots,n_s,m_1,\ldots,m_t\) as above, and every finite simple graph \(H\) satisfying
> \[
> |E(H)|\le L-1,
> \]
> there exists a red-blue coloring of \(E(H)\) such that the red graph contains no copy of \(F_1\) and the blue graph contains no copy of \(F_2\).

Equivalently, one must prove
\[
H\nrightarrow(F_1,F_2)
\qquad\text{whenever }|E(H)|<L.
\]

The proof may be constructive, probabilistic, extremal, inductive, or otherwise nonconstructive, but it must apply to every finite simple host graph \(H\), not merely to star forests, connected graphs, or graphs of a prescribed degree pattern.

### 2.3 What a complete disproof must establish

Because the upper bound \(L\) is already proved, the claimed equality can fail only downward.

A disproof must provide:

1. integers \(s,t\ge1\);
2. nonincreasing positive integer sequences
   \[
   n_1\ge\cdots\ge n_s\ge1,\qquad
   m_1\ge\cdots\ge m_t\ge1;
   \]
3. the resulting number
   \[
   L=\sum_{k=2}^{s+t}l_k;
   \]
4. a finite simple graph \(H\) with
   \[
   |E(H)|\le L-1;
   \]
5. a proof that
   \[
   H\to(F_1,F_2).
   \]

The last item requires verification over every red-blue coloring of \(E(H)\). For a small graph this may be done by exhaustive enumeration, SAT with a checkable unsatisfiability certificate, or a human structural argument. Merely observing that many tested colorings are Ramsey is not enough.

---

## 3. What does not count as a solution

None of the following resolves the problem:

1. **Proving only the upper bound.**  
   The disjoint-star construction above already gives \(\widehat R(F_1,F_2)\le L\).

2. **Restricting the host graph.**  
   Proving the lower bound only when \(H\) is a forest, star forest, connected graph, bipartite graph, bounded-degree graph, or disjoint union of prescribed pieces does not suffice.

3. **Proving that \(H^\star\) is optimal only among disjoint unions of stars.**  
   A smaller arbitrary host might share vertices or use dense subgraphs more efficiently.

4. **Partial parameter ranges.**  
   Additional parity cases, bounded \(s,t\), equal component sizes, or inequalities among the \(n_i,m_j\) are useful progress but not a full solution.

5. **Asymptotic estimates.**  
   Bounds such as
   \[
   \widehat R(F_1,F_2)=L+o(L),\qquad
   \widehat R(F_1,F_2)\ge cL,
   \]
   or \(L-O(s+t)\) do not establish the exact formula.

6. **Conditional results.**  
   A proof assuming another unproved conjecture is not a resolution unless that conjecture is also proved.

7. **Forcing the individual components without proving disjointness.**  
   Showing that the red graph contains each \(K_{1,n_i}\) somewhere does not show that it contains their vertex-disjoint union.

8. **Mixing colors among components.**  
   A copy of \(F_1\) must have every edge red, and a copy of \(F_2\) must have every edge blue. It is irrelevant that one can find some red components and some blue components whose union has the same uncolored shape.

9. **Degree-only criteria.**  
   A red vertex of degree at least \(n_1\) gives one red star, not necessarily a red copy of the entire star forest.

10. **Ordinary Ramsey or vertex-Ramsey arguments.**  
    The quantity being minimized is the number of edges of an edge-colored host graph.

---

## 4. Known results and context

### 4.1 General upper and elementary lower bounds

As proved above,
\[
\widehat R(F_1,F_2)\le L
\]
in complete generality.

Also, all-red and all-blue colorings imply that every Ramsey host \(H\) must contain both \(F_1\) and \(F_2\) as uncolored subgraphs. Hence
\[
|E(H)|\ge |E(F_1)|=\sum_{i=1}^s n_i
\]
and
\[
|E(H)|\ge |E(F_2)|=\sum_{j=1}^t m_j.
\]
Thus the elementary lower bound is
\[
\widehat R(F_1,F_2)
\ge
\max\left\{
\sum_{i=1}^s n_i,\,
\sum_{j=1}^t m_j
\right\}.
\]
This is generally much weaker than the conjectured value \(L\).

### 4.2 Settled parameter regimes

According to the database commentary:

- **Burr, Erdős, Faudree, Rousseau, and Schelp (1978)** proved the formula when all red component sizes are equal and all blue component sizes are equal:
  \[
  n_1=\cdots=n_s=n,\qquad
  m_1=\cdots=m_t=m.
  \]
  In this case
  \[
  l_k=n+m-1
  \]
  for every \(k\), so
  \[
  \widehat R(sK_{1,n},tK_{1,m})
  =(s+t-1)(n+m-1).
  \]

- **Győri and Schelp (2002)** proved the formula under the sufficient condition
  \[
  \binom{l_k}{2}>
  \sum_{i=k}^{s+t}l_i
  \qquad
  \text{for every }2\le k\le s+t.
  \]
  The strict inequality is part of the hypothesis.

- **Davoodi, Javadi, Kamranian, and Raeisi (2025)** proved further cases, including:
  - \(s=1\);
  - \(s=2\) and \(n_1=n_2\);
  - all \(n_i\) and all \(m_j\) odd;
  - all \(n_i\) equal to the same odd integer and \(m_1\) odd.

By color symmetry, the corresponding statements obtained by exchanging
\[
(F_1,s,n_i)\longleftrightarrow(F_2,t,m_j)
\]
are also settled. Thus, for example, the \(s=1\) result also gives the \(t=1\) case after swapping colors.

### 4.3 Relevant structural theorem: Hall’s theorem

If distinct candidate centers \(c_1,\ldots,c_r\) are fixed and one seeks vertex-disjoint stars with respective leaf demands \(a_1,\ldots,a_r\), the leaf-selection problem becomes a bipartite \(b\)-matching problem. Hall’s marriage theorem, in its replicated-vertex or capacitated form, gives the condition
\[
\left|
\bigcup_{i\in I}
\left(N(c_i)\setminus\{c_1,\ldots,c_r\}\right)
\right|
\ge
\sum_{i\in I}a_i
\]
for every \(I\subseteq\{1,\ldots,r\}\).

This is useful once centers have been selected. The difficult part is that the centers are not fixed in advance and must themselves be disjoint from all selected leaves.

### 4.4 Status of the central difficulty

The exact upper construction is simple and completely understood. The open problem is a universal, exact lower bound against arbitrary host graphs. Such a host may exploit shared neighborhoods, dense cores, or overlapping potential star centers in ways unavailable to the disjoint-star construction.

---

## 5. Traps and edge cases

### 5.1 Disjoint union is essential

The notation
\[
F_1=\bigcup_iK_{1,n_i}
\]
must mean vertex-disjoint union. Otherwise the sequence \((n_i)\) would not determine a unique graph.

A red copy of \(F_1\) requires \(s\) pairwise vertex-disjoint red stars. Their centers must be distinct, their leaves must be distinct, and no center may serve as a leaf of another selected component.

### 5.2 Copies are not induced

Extra edges between vertices of a selected copy do not invalidate it. Those extra edges may have either color. Only the image of each edge of the target forest must have the required color.

### 5.3 The case \(K_{1,1}\)

The graph \(K_{1,1}\) is a single edge. Its “center” is not intrinsically distinguished. Any algorithm that fixes oriented centers must avoid double-counting or accidentally excluding valid embeddings.

If all \(n_i=1\), then \(F_1\) is a matching of size \(s\), not a collection of edges allowed to share endpoints.

### 5.4 One high-degree vertex supports only one component

A vertex with many red incident edges can produce a large red star, but all stars centered there intersect. It cannot by itself supply multiple components of \(F_1\).

Conversely, in an arbitrary graph, neighbors of a high-degree vertex may also act as centers using other edges. Thus one cannot simply partition the graph by high-degree vertices.

### 5.5 The \(-1\) is exact

The threshold
\[
n_i+m_j-1
\]
comes from the fact that avoiding both a red \(K_{1,n_i}\) and a blue \(K_{1,m_j}\) at a common center would require
\[
r\le n_i-1,\qquad b\le m_j-1,
\]
and hence
\[
r+b\le n_i+m_j-2.
\]
Replacing \(-1\) by \(0\) or \(-2\) changes the statement.

### 5.6 Correct antidiagonal range

The sum contains exactly \(s+t-1\) terms:
\[
k=2,3,\ldots,s+t.
\]
For fixed \(k\), the maximum is only over pairs satisfying all three conditions
\[
1\le i\le s,\quad 1\le j\le t,\quad i+j=k.
\]

In particular,
\[
l_2=n_1+m_1-1,\qquad
l_{s+t}=n_s+m_t-1.
\]

### 5.7 Sorted component sizes

The components themselves are unlabeled, but sorting their sizes is important for the antidiagonal formula. In an embedding, the largest demands should generally be matched first against the largest available capacities.

### 5.8 Edge count, not vertex count

The host may have arbitrarily many isolated vertices, but they are irrelevant and can be deleted. A graph with \(q\) edges and no isolated vertices has at most \(2q\) vertices, which is important for finite searches.

### 5.9 Strict lower-bound threshold

To prove equality it is necessary to color every graph with
\[
|E(H)|\le L-1.
\]
Showing colorability only for \(|E(H)|\le L-2\) leaves open the possibility that the true value is \(L-1\).

### 5.10 Ramsey-minimal hosts need not be connected

The known upper construction is itself disconnected. Therefore one must not assume without proof that an edge-minimal Ramsey host is connected.

### 5.11 Individual embeddings versus a forest embedding

Clauses or counting arguments that block every red \(K_{1,n_i}\) separately are too strong and may destroy valid avoiding colorings. To avoid \(F_1\), it is enough to prevent a vertex-disjoint collection of all its components.

---

## 6. Verification hooks

### 6.1 Computing the conjectured value

For given sequences, compute
```text
for k = 2,...,s+t:
    l[k] = max(n[i] + m[j] - 1 over valid i,j with i+j=k)
L = sum(l[k])
```
As consistency checks:

- verify that every maximum is over a nonempty set;
- verify
  \[
  l_2\ge l_3\ge\cdots\ge l_{s+t};
  \]
- verify color symmetry by swapping the two sequences and obtaining the same \(L\).

### 6.2 Checking the upper construction

For
\[
H^\star=\bigsqcup_{k=2}^{s+t}K_{1,l_k},
\]
it is unnecessary to enumerate all \(2^L\) edge colorings. Up to automorphisms of each star component, only the red counts
\[
r_k\in\{0,1,\ldots,l_k\}
\]
matter. One can enumerate the
\[
\prod_{k=2}^{s+t}(l_k+1)
\]
count vectors and run the greedy lattice-path argument.

This is a useful implementation check for indexing and off-by-one errors.

### 6.3 Detecting a monochromatic prescribed star forest

Given a colored graph \(G\) and demands \(a_1,\ldots,a_r\), one direct exact algorithm is:

1. For each \(q=a_i\), enumerate all monochromatic copies of \(K_{1,q}\):
   - choose a center \(v\);
   - choose \(q\) same-colored neighbors of \(v\).
2. Treat each candidate star as the set of its \(q+1\) vertices.
3. Solve an exact packing problem selecting one candidate for each demand, with all selected vertex sets pairwise disjoint.

Repeated demands can be handled with multiplicities rather than labels. For \(q=1\), canonicalize the edge to avoid counting both orientations unless oriented centers are explicitly intended.

### 6.4 SAT encoding of avoiding colorings

For a fixed host \(H\), introduce one Boolean variable \(x_e\) per edge, with
\[
x_e=\text{true}\iff e\text{ is red}.
\]

Enumerate all injective embeddings \(\phi:F_1\hookrightarrow H\). For each such embedding add
\[
\bigvee_{f\in E(F_1)}\neg x_{\phi(f)}.
\]
This clause says that the embedded copy is not entirely red.

Enumerate all embeddings \(\psi:F_2\hookrightarrow H\). For each add
\[
\bigvee_{f\in E(F_2)}x_{\psi(f)}.
\]
This clause says that the embedded copy is not entirely blue.

The resulting formula is satisfiable exactly when \(H\) admits an avoiding coloring. Therefore:

- SAT gives an explicit avoiding coloring;
- UNSAT proves \(H\to(F_1,F_2)\);
- a DRAT/LRAT or similar independently checkable certificate can make a computational counterexample rigorous.

The embeddings must be embeddings of the entire disconnected forest, not merely its individual components.

### 6.5 Exhaustive search for fixed parameters

For a fixed \(L\), any relevant host with fewer than \(L\) edges can be assumed to have no isolated vertices, hence at most \(2(L-1)\) vertices. In principle:

1. generate all unlabeled simple graphs with at most \(L-1\) edges and no isolated vertices, using tools such as `nauty`/`Traces`;
2. discard graphs not containing both \(F_1\) and \(F_2\) uncolored;
3. run the SAT test above;
4. search for an UNSAT instance.

This is finite for each parameter tuple, although usually expensive.

### 6.6 A small uncovered search seed

A natural parameter set not covered by the regimes listed in the commentary is
\[
(n_1,n_2)=(3,2),\qquad
(m_1,m_2)=(3,2).
\]
Here
\[
l_2=5,\qquad l_3=4,\qquad l_4=3,
\]
so
\[
L=12.
\]
The upper host is
\[
K_{1,5}\sqcup K_{1,4}\sqcup K_{1,3}.
\]

The Győri–Schelp inequalities fail:
\[
\binom52=10\not>12,\qquad
\binom42=6\not>7,\qquad
\binom32=3\not>3.
\]
A direct search asks whether any graph with at most \(11\) edges arrows
\[
(K_{1,3}\sqcup K_{1,2},\,K_{1,3}\sqcup K_{1,2}).
\]

---

## 7. Attack routes

## Route A: Induction through Ramsey-minimal host structure

### Core idea

Assume a smallest counterexample \(H\) with
\[
|E(H)|<L,\qquad H\to(F_1,F_2),
\]
and derive a reducible vertex, edge, or cut. Delete the reducible structure, color the smaller graph by induction, and extend the coloring.

The antidiagonal formula suggests an induction state indexed by \((i,j)\): paying \(n_i+m_j-1\) edges corresponds to forcing one step either toward the next red component or toward the next blue component.

### Needed key lemma

A quantitative extension lemma of the following kind:

> Every graph below the edge threshold has a local structure whose incident edges can be colored so that, relative to an avoiding coloring of the remainder, it does not complete both the next red star demand \(n_i\) and the next blue star demand \(m_j\).

Ideally the edge cost of a nonreducible structure would be at least \(l_{i+j}\), and iteration would sum these costs.

### Why it might work

Exact size-Ramsey lower bounds are often proved by analyzing edge-minimal Ramsey graphs. The formula itself is a dynamic-programming or lattice-path sum, making a two-parameter induction natural.

### Most likely failure point

Whether a newly colored edge completes a star-forest copy depends globally on vertex-disjoint packings. A local extension may create a large star whose center or leaves interact with several previously selected components. Minimum degree alone is unlikely to control this.

### Quick blockage test

For small parameter tuples, enumerate edge-minimal arrowing graphs at the known threshold \(L\), and test proposed reducibility conditions:

- low degree;
- a vertex whose deletion decreases the relevant packing profile predictably;
- a bridge or sparse cut;
- an edge contained in few potential forest embeddings.

If known threshold examples already violate the proposed local lemma, redesign it before attempting a general induction.

---

## Route B: Star-packing min-max theorem plus edge-color allocation

### Core idea

Develop an exact obstruction theory for containing a prescribed star forest. With centers fixed, Hall’s theorem solves the leaf assignment. The aim would be to optimize simultaneously over the choice of centers and turn noncontainment of \(F_1\) or \(F_2\) into a finite family of deficiency inequalities.

Then color the edges so that the red graph satisfies a deficiency certificate for \(F_1\) and the blue graph satisfies one for \(F_2\).

### Needed key lemma

A min-max characterization such as:

> A graph contains \(\bigsqcup_i K_{1,n_i}\) if and only if every object in some explicitly described family of vertex-set or neighborhood inequalities has nonnegative deficiency.

The characterization must be integral and must allow the centers to vary.

A second required lemma would partition the edges into red and blue so that at least one red deficiency and one blue deficiency are maintained whenever the total edge count is below \(L\).

### Why it might work

Stars reduce to capacitated matching once centers are known. The problem is therefore close to \(b\)-matching, flow, and Hall-type theory, all of which have strong integral duality. An exact dual certificate could explain the exact antidiagonal maximum.

### Most likely failure point

The center-selection problem is nonconvex: a chosen center cannot simultaneously be used as a leaf. The family of feasible star packings is not obviously a matroid, and natural linear relaxations may have integrality gaps.

### Quick blockage test

Formulate the prescribed star-packing problem as an integer program and compare it with candidate LP relaxations on all small graphs. Search immediately for:

- fractional packings larger than integral packings;
- dual inequalities that fail to characterize \(K_{1,1}\)-heavy instances;
- examples where optimal centers must be changed globally.

A small integrality-gap example would rule out a naive LP-duality approach.

---

## Route C: Hypergraph/Boolean-cube duality

### Core idea

For a fixed host \(H\), let \(\mathcal A\) be the family of edge sets of copies of \(F_1\), and let \(\mathcal B\) be the family of edge sets of copies of \(F_2\).

An avoiding coloring is a set \(R\subseteq E(H)\) such that
\[
A\nsubseteq R\quad\text{for every }A\in\mathcal A,
\]
and
\[
B\nsubseteq E(H)\setminus R\quad\text{for every }B\in\mathcal B.
\]

Thus \(H\to(F_1,F_2)\) means that two monotone families cover the entire Boolean cube \(2^{E(H)}\). Seek an inequality proving that such a cover is impossible when \(|E(H)|<L\).

### Needed key lemma

A graph-realizable set-pair inequality of the form:

> If the red-copy and blue-copy hypergraphs cover every edge subset, then the ground-set size is at least
> \[
> \sum_{k=2}^{s+t}\max_{i+j=k}(n_i+m_j-1).
> \]

Potential tools include blocker duality, Bollobás-type set-pair inequalities, LYM inequalities, or monotone Boolean-function certificates.

### Why it might work

The lower-bound assertion is exactly a statement about the existence of a Boolean assignment avoiding two monotone families. The max-over-antidiagonals structure resembles an extremal set-system convolution.

### Most likely failure point

Generic hypergraphs can cover a Boolean cube much more efficiently than graph-embedding hypergraphs. Any successful inequality must exploit the special intersection structure of star-forest copies, not merely their cardinalities.

### Quick blockage test

For small known Ramsey hosts, construct the SAT formula and extract minimal unsatisfiable cores. Check whether the cores admit:

- a layered antidiagonal structure;
- a set-pair witness;
- a short resolution proof whose width or clause structure sums to \(L\).

If minimal cores are irregular and substantially smaller than any proposed layered certificate, a simple Boolean-cube inequality is unlikely to suffice.

---

## Route D: Componentwise Pareto-state dynamic programming

### Core idea

Analyze each connected component \(C\) of an arbitrary host by the set of red/blue star-forest capacities achievable under its colorings. Combine components by a convolution analogous to a knapsack or lattice-path dynamic program.

One wants to show that a connected component with \(q\) edges cannot advance the red-blue forcing state more efficiently than spending those \(q\) edges among the canonical star components \(K_{1,l_k}\).

### Needed key lemma

An extremality statement such as:

> For purposes of forcing prescribed disjoint red and blue stars, every connected \(q\)-edge graph has a coloring whose red/blue packing state is no worse than the state achievable in an appropriate \(q\)-edge star or collection of stars.

Equivalently, the disjoint-star upper host would have to be shown edge-optimal under a suitable state-space ordering.

### Why it might work

The target graphs are disconnected, so connected components of the host naturally contribute independent collections of target components. The conjectured formula is itself a sum of local thresholds.

### Most likely failure point

A connected graph can contain several disjoint stars and may use shared edges or neighborhoods to force multiple state transitions more efficiently than a single star. The relevant state must record more than the largest available red and blue degrees.

### Quick blockage test

For every connected graph with, say, at most \(8\) or \(10\) edges, compute its full Pareto frontier:
\[
(\text{largest red star-forest profile},\,
 \text{largest blue star-forest profile})
\]
over all colorings. Compare this frontier with that of stars and disjoint unions of stars of the same edge count. Any strict efficiency gain identifies exactly what extra state a proof must control.

---

## Route E: Probabilistic or entropy-based coloring

### Core idea

Color each edge independently, perhaps with edge-dependent probabilities, and show that with positive probability there is neither a red \(F_1\) nor a blue \(F_2\). More sophisticated variants could use the Lovász local lemma, entropy compression, cluster expansion, or randomized greedy recoloring.

### Needed key lemma

A universal bound on the weighted number and dependency structure of star-forest embeddings in an \(m\)-edge graph, strong enough to imply positive probability whenever
\[
m<L.
\]

Since exactness is required, the lemma must recover the integer threshold rather than merely a constant-factor or asymptotic bound.

### Why it might work

Every fixed graph with fewer than \(L\) is conjectured to have at least one avoiding coloring. Probabilistic methods can prove existence without having to identify that coloring explicitly. Stars have simple local event structure around centers.

### Most likely failure point

The number of possible embeddings may be enormous, and events overlap heavily. Red and blue bad events compete, while an exact threshold usually lies beyond ordinary union-bound or symmetric-local-lemma estimates.

### Quick blockage test

For small difficult parameter tuples and candidate dense hosts:

1. optimize a global red probability \(p\);
2. optimize edge-dependent probabilities;
3. test asymmetric local-lemma or cluster-expansion criteria.

If these criteria already fail badly on graphs known to be colorable below \(L\), then a standard product-measure argument is too weak and would require substantial correlation or recoloring machinery.

---

## Route F: Computational disproof search

### Core idea

Search for a host graph with fewer than \(L\) edges that is more efficient than the canonical disjoint-star host. Dense or highly overlapping structures are the most plausible source of a counterexample.

### Needed key lemma or output

This route needs an explicit tuple and graph \(H\) for which the avoiding-coloring SAT instance is unsatisfiable. The final result must include a verifiable exhaustive argument or proof certificate.

### Why it might work

Size-Ramsey phenomena sometimes admit connected or dense hosts that beat naive disjoint constructions. The existence of numerous special-case proofs, rather than a known general lower-bound mechanism, leaves open the possibility that mixed-size and mixed-parity instances behave differently.

### Most likely failure point

The conjecture may be true, in which case every graph below \(L\) has an avoiding coloring. Exhaustive graph generation and embedding enumeration also grow extremely quickly.

### Quick search plan

Prioritize parameter tuples satisfying all of the following:

- \(s,t\ge2\);
- neither list is constant in a way covered by known results;
- not all component sizes are odd;
- the Győri–Schelp inequalities fail;
- \(L\) is small enough for enumeration.

The tuple
\[
(3,2)\quad\text{versus}\quad(3,2)
\]
with \(L=12\) is an immediate test case. Search all no-isolate graphs with at most \(11\) edges, first filtering by the necessary condition that they contain both target forests uncolored.

If a candidate is found, minimize it under edge and vertex deletion and produce an independently checkable UNSAT certificate.

---

## 8. Verdict on difficulty

This is a difficult exact extremal problem. The upper bound is short and transparent; essentially all of the difficulty lies in proving that no arbitrary graph with fewer edges can exploit overlap more efficiently.

The problem has been open since at least the 1978 work cited in the database and has required multiple later papers to settle substantial but restricted regimes, including work as recent as 2025. That strongly suggests that a successful proof will need a genuinely new lower-bound mechanism for asymmetric size Ramsey numbers of disconnected forests, rather than a routine refinement of the upper construction.

There is no basis in the supplied context for claiming equivalence to a famous conjecture such as the Erdős–Hajnal conjecture or a standard open matching theorem. However, the desired statement is stronger than any argument that only controls degrees or individual stars: it requires exact two-color control of vertex-disjoint star packings in every host graph.

The most promising conceptual directions are:

1. an exact min-max theorem for prescribed star-forest packing;
2. a structural induction for Ramsey-minimal hosts that mirrors the antidiagonal formula;
3. a Boolean/hypergraph duality inequality tailored to graph-realizable copy families.

A computational search in the smallest uncovered mixed-size cases should be run early. It can either uncover a genuine counterexample or reveal the structural patterns that any general lower-bound proof must explain.