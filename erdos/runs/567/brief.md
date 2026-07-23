# Problem brief: Erdős Problem #567

## 1. Precise statement

All graphs below are finite, simple, and undirected.

For graphs \(G\) and \(H\), the two-colour Ramsey number \(R(G,H)\) is the least integer \(N\) such that every red-blue colouring of the edges of \(K_N\) contains either

- a red copy of \(G\), or
- a blue copy of \(H\).

Copies are ordinary, not necessarily induced, subgraphs. Equivalently, if \(F\) is the graph of red edges, then \(R(G,H)\) is the least \(N\) such that every graph \(F\) on \(N\) vertices contains \(G\), or its complement \(\overline F\) contains \(H\).

The three possible fixed graphs \(G\) are:

1. **The three-dimensional cube \(Q_3\):**
   \[
   V(Q_3)=\{0,1\}^3,
   \]
   with two binary triples adjacent exactly when they differ in one coordinate. Thus
   \[
   |V(Q_3)|=8,\qquad |E(Q_3)|=12.
   \]
   It is bipartite and isomorphic to \(K_{4,4}\) minus a perfect matching.

2. **The complete bipartite graph \(K_{3,3}\):**
   it has a bipartition \(A\sqcup B\), with \(|A|=|B|=3\), and all nine edges between \(A\) and \(B\).

3. **The graph \(H_5\):**
   start with the cycle
   \[
   1\,2\,3\,4\,5\,1
   \]
   and add the vertex-disjoint chords \(13\) and \(25\). Thus
   \[
   E(H_5)=\{12,23,34,45,51,13,25\}.
   \]
   All choices of two vertex-disjoint chords of \(C_5\) give isomorphic graphs. This graph is also denoted \(K_4^*\): it is obtained from \(K_4\) by subdividing one edge once. It has five vertices, seven edges, degree sequence \((3,3,3,3,2)\), and chromatic number \(3\).

For a fixed choice of \(G\), the question is whether
\[
\exists C_G<\infty\ \ \forall H\quad
\left[
\bigl(\forall v\in V(H),\ \deg_H(v)\ge 1\bigr)
\Longrightarrow
R(G,H)\le C_G |E(H)|
\right].
\]

Writing \(m=|E(H)|\), this is the meaning of
\[
R(G,H)\ll m.
\]
The implicit constant may depend on the fixed graph \(G\), but not on \(H\), \(m\), \(|V(H)|\), \(\Delta(H)\), \(\chi(H)\), or any other parameter of \(H\).

The database entry is most naturally read as asking the question separately for each of
\[
G=Q_3,\qquad G=K_{3,3},\qquad G=H_5.
\]
If it is read as a single conjunction, one asks that all three statements hold. Since there are only three fixed graphs, separate constants can be replaced by their maximum.

The condition that \(H\) have no isolated vertices implies
\[
|V(H)|\le 2|E(H)|=2m.
\]
We should take \(H\) to be nonempty, so \(m\ge 1\); the empty graph is a vacuous edge case not intended by the problem.

---

## 2. What counts as a solution

### A complete positive solution

For a particular fixed \(G\in\{Q_3,K_{3,3},H_5\}\), a proof must establish a constant \(C_G\) such that for every finite simple graph \(H\) with no isolated vertices and \(m\) edges,
\[
R(G,H)\le C_Gm.
\]

Equivalently, it must prove:

> Every \(G\)-free graph \(F\) on at least \(C_Gm\) vertices has the property that \(\overline F\) contains every graph \(H\) with \(m\) edges and no isolated vertices.

An explicit numerical value of \(C_G\) is not required, provided the proof establishes that some finite constant depending only on \(G\) exists.

A theorem proved only for all sufficiently large \(m\) is enough, provided the bound is uniform over all admissible \(H\) with that many edges. There are only finitely many isomorphism classes of no-isolate graphs with \(m<m_0\), because such graphs have at most \(2m_0\) vertices, so finitely many exceptional cases can be absorbed into the constant.

To solve the database entry in full under the conjunctive reading, this must be proved for all three choices of \(G\).

### A complete negative solution

For a fixed \(G\), a disproof must show
\[
\sup_{\substack{H\text{ finite simple}\\ \delta(H)\ge1}}
\frac{R(G,H)}{|E(H)|}=\infty.
\]

A standard sufficient form is to construct sequences

- \(H_i\), each with no isolated vertices,
- \(m_i=|E(H_i)|\),
- integers \(N_i\), and
- red-blue colourings of \(K_{N_i}\),

such that the colouring contains neither a red \(G\) nor a blue \(H_i\), and
\[
\frac{N_i}{m_i}\longrightarrow\infty.
\]
The colouring then proves
\[
R(G,H_i)>N_i,
\]
hence \(R(G,H_i)/m_i\to\infty\).

For an “explicit counterexample family,” verification must establish for every member of the family that:

1. the red graph contains no subgraph isomorphic to \(G\);
2. the blue graph contains no subgraph isomorphic to \(H_i\);
3. \(H_i\) has no isolated vertices;
4. \(N_i/|E(H_i)|\) is unbounded.

One isolated finite example with a large ratio cannot disprove the statement, since the unspecified constant \(C_G\) could simply be larger.

A particularly important possible disproof uses clique targets. If there are \(G\)-free graphs \(F_N\) with
\[
\alpha(F_N)=o(\sqrt N),
\]
then, taking \(H_N=K_{\alpha(F_N)+1}\), the blue graph \(\overline{F_N}\) contains no \(H_N\), while
\[
|E(H_N)|=\Theta(\alpha(F_N)^2)=o(N).
\]
This would immediately disprove Ramsey size linearity for \(G\).

---

## 3. What does not count

The following do not resolve the problem:

- A bound of the form
  \[
  R(G,H)=O(m\log m),\qquad O(m^{1+\varepsilon}),
  \]
  or merely \(m^{1+o(1)}\).

- A linear bound only when \(H\) belongs to a restricted class, such as:
  - bipartite graphs,
  - connected graphs,
  - forests,
  - bounded-degree graphs,
  - bounded-degeneracy graphs,
  - bounded-chromatic-number graphs,
  - regular graphs,
  - complete graphs,
  - graphs with \(|V(H)|\ll m^\theta\).

- A result whose constant depends on \(H\), \(\Delta(H)\), \(\chi(H)\), or \(m\).

- A proof for one of the three possible fixed graphs presented as a solution for the other two. The three statements are logically separate.

- A conditional proof depending on an unresolved Ramsey, extremal, pseudorandomness, or embedding conjecture.

- Heuristic evidence, random simulations, or exact computations for finitely many target graphs.

- A statement about the **size-Ramsey number** \(\widehat R(G,H)\). Despite the terminology “Ramsey size linear,” this problem concerns the ordinary vertex Ramsey number \(R(G,H)\).

- A bound only for induced Ramsey numbers or only for induced copies. The copies here are non-induced.

- Proving merely that the red graph has few edges. Even \(e(F)=o(N^2)\) does not automatically make \(\overline F\) universal for every graph with \(O(N)\) edges.

---

## 4. Known results and context

### 4.1 Database results

The property under discussion is called **Ramsey size linearity** of the fixed graph \(G\).

The problem is a special case of Erdős Problem #566. Erdős specifically asked about
\[
G=K_{3,3}
\]
in [Er95].

Bradać, Gishboliner, and Sudakov [BGS23] proved:

1. Every subdivision of \(K_4\) on at least six vertices is Ramsey size linear.

2. For the exceptional five-vertex subdivision \(H_5=K_4^*\),
   \[
   R(H_5,H)=O(|E(H)|)
   \]
   whenever \(H\) is bipartite and has no isolated vertices.

Thus the \(H_5\) case is already settled for all bipartite target graphs \(H\). The remaining \(H_5\) problem concerns arbitrary targets, in particular nonbipartite targets.

The theorem about subdivisions on at least six vertices does not cover \(H_5\), which has only five vertices.

The corresponding assertion is false for \(K_4\). Taking \(H=K_n\), for which
\[
|E(H)|=\binom n2=\Theta(n^2),
\]
the lower bound
\[
R(K_4,K_n)\gg n^{3-o(1)}
\]
implies
\[
\frac{R(K_4,K_n)}{|E(K_n)|}\to\infty.
\]
Thus subdividing one edge of \(K_4\) may mark a genuine threshold.

### 4.2 Necessary off-diagonal Ramsey consequences

A positive answer for any fixed \(G\) implies
\[
R(G,K_t)=O_G(t^2),
\]
because \(|E(K_t)|=\binom t2\).

Equivalently, there must be a constant \(c_G>0\) such that every sufficiently large \(G\)-free graph \(F\) on \(N\) vertices satisfies
\[
\alpha(F)\ge c_G\sqrt N.
\]

This clique-target consequence is necessary but not sufficient: the full problem asks for every \(m\)-edge target, including highly irregular and disconnected graphs.

For \(G=K_{3,3}\), obtaining the required uniform result necessarily includes the difficult quadratic off-diagonal estimate
\[
R(K_{3,3},K_t)=O(t^2).
\]
Any proposed proof should be checked first against this benchmark.

### 4.3 Extremal information

The Kővári–Sós–Turán theorem gives
\[
\operatorname{ex}(N,K_{3,3})=O(N^{5/3}).
\]
Thus a red \(K_{3,3}\)-free graph is sparse compared with \(K_N\), but it can still have average degree of order \(N^{2/3}\). That is much too large for a naive greedy embedding into its complement.

Since \(Q_3\) is bipartite, the Erdős–Stone theorem gives
\[
\operatorname{ex}(N,Q_3)=o(N^2).
\]
Again, this density statement alone does not imply that the complement contains every graph with \(O(N)\) edges.

The graph \(H_5\) has chromatic number \(3\) and a colour-critical edge. In the \(K_4^*\) description, if \(ab\) is the subdivided edge and \(c,d\) are the other two original vertices, then deleting \(cd\) makes the graph bipartite. Simonovits’s theorem for colour-critical graphs therefore gives, for all sufficiently large \(N\),
\[
\operatorname{ex}(N,H_5)=e(T_2(N))=\left\lfloor\frac{N^2}{4}\right\rfloor.
\]
Moreover, stability theory says that near-extremal \(H_5\)-free graphs are structurally close to bipartite graphs. This is potentially important for the unresolved nonbipartite-target case.

### 4.4 Elementary target bounds

If \(H\) has \(m\) edges and no isolated vertices, then
\[
v(H)\le 2m.
\]

Also,
\[
\chi(H)\le \frac{1+\sqrt{1+8m}}2.
\]
Indeed, a \(k\)-chromatic graph contains a \(k\)-critical subgraph of minimum degree at least \(k-1\), and hence has at least \(k(k-1)/2\) edges.

These observations are useful for decomposition, but neither by itself gives the required Ramsey bound.

---

## 5. Traps and edge cases

1. **Non-induced copies.**  
   To embed \(H\) in the blue graph, only the edges of \(H\) must be blue. Nonedges of \(H\) may also be blue.

2. **The no-isolated-vertices hypothesis is essential.**  
   Isolated vertices contribute no edges but still require distinct vertices in a copy. Without the hypothesis, one could add arbitrarily many isolated vertices while keeping \(m\) fixed.

3. **Disconnected targets are included.**  
   It is not enough to embed every connected \(m\)-edge graph. Different components must be embedded simultaneously and vertex-disjointly.

4. **A single bad finite ratio is irrelevant.**  
   Disproof requires an unbounded family of ratios \(R(G,H)/e(H)\).

5. **Red/blue orientation.**  
   In the complement formulation, the red graph must be \(G\)-free and its complement must avoid \(H\). Swapping which graph is assigned to which colour can invalidate an argument, even though Ramsey numbers themselves are symmetric after swapping both graph labels.

6. **Subgraph monotonicity must be used in the correct direction.**  
   If \(G_1\subseteq G_2\), then
   \[
   R(G_1,H)\le R(G_2,H).
   \]
   A theorem for a smaller forbidden red graph does not automatically prove a theorem for a larger one.

7. **Subdivision is not a harmless monotone operation.**  
   The result for subdivisions of \(K_4\) on at least six vertices does not follow down to \(H_5\), and a limit or contraction argument does not preserve the relevant Ramsey property.

8. **\(H_5\) is not bipartite.**  
   It contains triangles. The BGS theorem concerns bipartite target graphs \(H\), not a bipartite fixed red graph.

9. **Extremal sparsity is insufficient.**  
   From \(e(F)=o(N^2)\), one cannot conclude that \(\overline F\) contains every \(m\)-edge graph with \(m=\Theta(N)\). The missing red edges can be concentrated around strategically chosen vertices or sets.

10. **A naive greedy embedding can pay too much.**  
    Embedding a vertex of \(H\) may require an intersection of many blue neighbourhoods. Paying a fixed positive fraction of the ambient set for each neighbour can lead to exponential or superlinear losses.

11. **Blow-ups can create the forbidden graph.**  
    A blow-up of a \(G\)-free base graph need not remain \(G\)-free, because a copy of \(G\) may arise from a non-injective homomorphism into the base graph.

12. **Exact local descriptions must preserve distinctness.**
    - A red \(K_{3,3}\) consists of three distinct vertices with at least three distinct common red neighbours.
    - A red \(Q_3\) is a red \(K_{4,4}\) minus a matching; the eight selected vertices must be distinct.
    - For \(H_5\), one useful description has vertices \(a,b,c,d,x\) and edges
      \[
      cd,ca,da,cb,db,ax,bx.
      \]
      Thus \(c,d\) form a red edge with two common red neighbours \(a,b\), and \(a,b\) have another common red neighbour \(x\), all five vertices distinct.

13. **Small-\(m\) exceptions are harmless only after uniformity is proved.**  
    One can absorb finitely many small targets into \(C_G\), but not an infinite target subclass excluded by the argument.

---

## 6. Verification hooks

### 6.1 SAT formulation for exact lower bounds

For fixed \(G,H,N\), introduce a Boolean variable \(x_{uv}\) for each edge \(uv\in E(K_N)\), with
\[
x_{uv}=1 \iff uv\text{ is red}.
\]

To forbid a red \(G\), for every injective map
\[
\phi:V(G)\hookrightarrow [N],
\]
add the clause
\[
\bigvee_{ab\in E(G)}\neg x_{\phi(a)\phi(b)}.
\]

To forbid a blue \(H\), for every injective map
\[
\psi:V(H)\hookrightarrow [N],
\]
add the clause
\[
\bigvee_{ab\in E(H)}x_{\psi(a)\psi(b)}.
\]

A satisfying assignment is a colouring of \(K_N\) with neither a red \(G\) nor a blue \(H\), and proves
\[
R(G,H)>N.
\]

Symmetry breaking can fix the colours of edges incident to one vertex or use canonical labelling under \(S_N\).

### 6.2 Enumeration of \(G\)-free red graphs

For small \(N\):

1. Enumerate unlabeled \(G\)-free graphs \(F\) on \(N\) vertices.
2. Form \(B=\overline F\).
3. Test whether \(B\) contains each no-isolate graph \(H\) with a prescribed edge count.
4. Record the smallest \(m\) for which some \(m\)-edge \(H\) is absent from \(B\).

This directly searches for complements that are not edge-universal.

### 6.3 Clique-target search

For every enumerated or constructed \(G\)-free graph \(F\), compute \(\alpha(F)\). Then the colouring with red graph \(F\) avoids a blue
\[
K_{\alpha(F)+1}.
\]
Record
\[
\frac{N}{\binom{\alpha(F)+1}{2}}.
\]
Growth of this quantity would be evidence toward a clique-based disproof. An actual disproof requires it to be unbounded.

### 6.4 Graph-specific certificate checks

Code direct routines for:

- \(K_{3,3}\): enumerate triples \(S\) and test whether
  \[
  \left|\bigcap_{v\in S}N_F(v)\right|\ge3.
  \]

- \(Q_3\): enumerate disjoint four-sets \(A,B\) and test whether the red bipartite graph between them contains \(K_{4,4}\) minus a perfect matching.

- \(H_5\): enumerate red edges \(cd\), pairs \(a,b\) of common red neighbours of \(c,d\), and a fifth vertex \(x\) red-adjacent to both \(a,b\).

These are faster than general subgraph isomorphism and useful when testing structural lemmas.

### 6.5 Testing proposed extension lemmas

Given a proposed one-vertex extension statement, use SAT to search for:

- a \(G\)-free red graph \(F\),
- a partial blue embedding of \(H-v\),
- no possible image for \(v\),

while keeping the ambient order below the claimed threshold. Such searches can quickly expose missing minimum-degree, reservoir, or distinctness hypotheses.

### 6.6 Perturbations of extremal \(H_5\)-free examples

Start from the complete bipartite red graph \(T_2(N)\), whose blue complement is two disjoint cliques. Add or delete selected red edges and test:

1. whether the resulting red graph remains \(H_5\)-free;
2. which nonbipartite target graphs disappear from the blue complement;
3. whether the obstruction survives when \(N/e(H)\) grows.

This tests stability-based conjectures and possible near-bipartite counterexamples.

---

## 7. Attack routes

### Route 1: Graph-specific local obstruction and dependent-random-choice embedding

**Core mechanism.**  
Translate failure of a blue embedding into large structured collections of red incidences, then use the specific local shape of \(G\) to force a red copy.

For \(K_{3,3}\), the decisive forbidden pattern is three vertices with three common red neighbours. For \(Q_3\), it is an almost-complete \(4\times4\) red bipartite pattern. For \(H_5\), it is a red edge with two common neighbours whose pair has another common neighbour.

**Key lemma needed.**  
A graph-specific embedding lemma of the following kind:

> If \(F\) is \(G\)-free on \(Cm\) vertices and a greedy or reservoir-based embedding of an \(m\)-edge graph \(H\) into \(\overline F\) fails, then the accumulated red obstruction sets contain the relevant local certificate for \(G\).

Ideally, the total cost should be charged to incidences or edges of \(H\), not to all pairs of vertices.

**Why it might work.**  
All three fixed graphs have compact codegree descriptions. Failed blue extensions naturally produce red neighbourhood coverings, and repeated failures may force large common red neighbourhoods.

**Most likely failure point.**  
A failed embedding generally says that a candidate set is covered by a union of red neighbourhoods. It need not produce a large intersection of red neighbourhoods. Converting union-cover information into the specific common-neighbour pattern may lose logarithmic or polynomial factors.

**Quick blockage test.**  
For small \(H\), generate maximal partial blue embeddings in \(G\)-free graphs and record all obstruction neighbourhoods. Use SAT to ask whether the proposed local implication can fail without creating \(G\). A counterexample on even \(10\)–\(20\) vertices may invalidate an overly strong lemma.

---

### Route 2: Edge-charged induction on the target graph

**Core mechanism.**  
Delete vertices or small subgraphs from \(H\), embed the remainder, and extend while charging the extra ambient vertices to the number of deleted incident edges.

**Key lemma needed.**  
A robust extension inequality resembling
\[
R(G,H)\le R(G,H-v)+C_G\,d_H(v),
\]
possibly with extra bookkeeping for vertices that become isolated, or a more flexible statement using a block of vertices \(S\):
\[
R(G,H)\le R(G,H-S)+C_G\,e_H(S,V(H)).
\]
Summing such costs over a deletion order would give \(O(m)\).

**Why it might work.**  
Every edge of \(H\) can be charged only once. This directly matches the desired parameter and naturally handles disconnected targets if components are processed carefully.

**Most likely failure point.**  
Extending a vertex of degree \(d\) requires a common blue neighbour of \(d\) already embedded vertices. The nonexistence of such a common neighbour may not force \(G\), and the cost can depend exponentially on \(d\) rather than linearly on \(d\). Deleting vertices also creates isolated vertices, so the induction class must be enlarged.

**Quick blockage test.**  
Test the proposed extension bound first on:
- stars,
- complete bipartite targets,
- cliques,
- one high-degree vertex attached to a dense core.

Search computationally for \(G\)-free red graphs in which a blue copy of \(H-v\) exists but every such copy is unextendable.

---

### Route 3: Critical-core decomposition and weighted multipartite embedding

**Core mechanism.**  
Exploit the fact that an \(m\)-edge target has chromatic number \(O(\sqrt m)\). Separate \(H\) into a chromatically critical core and lower-degree or low-degeneracy remainder. Embed the core using an off-diagonal Ramsey theorem, while retaining large blue reservoirs for the remainder.

**Key lemma needed.**  
A weighted multipartite or reservoir theorem:

> Given a proper colouring of an \(m\)-edge graph \(H\), every sufficiently large \(G\)-free red graph contains disjoint candidate sets for the colour classes and an embedding of the critical core such that all remaining required blue adjacency constraints can be met at total cost \(O(m)\).

This must exploit the actual edge set of \(H\), not require all cross-pairs between colour classes to be blue; the latter could cost \(\Theta(v(H)^2)\).

**Why it might work.**  
The high-chromatic part of \(H\) cannot be too large or too sparse: a \(k\)-critical graph has minimum degree at least \(k-1\) and at least \(\binom{k}{2}\) edges. The remainder should admit an edge-charged embedding.

**Most likely failure point.**  
Even when \(\chi(H)=O(\sqrt m)\), colour classes may be extremely unbalanced and the edge distribution between them highly irregular. Ordinary multipartite Ramsey results usually pay for complete cross-pairs, much more than the number of edges of \(H\).

**Quick blockage test.**  
Apply the proposed lemma to targets formed by combining:
- a clique of order \(\Theta(\sqrt m)\),
- a star with \(\Theta(m)\) leaves,
- many disjoint edges,
- sparse connections between these pieces.

These hybrid targets expose whether the reservoirs can handle simultaneously high chromatic number, high maximum degree, and near-spanning matching structure.

---

### Route 4: Stability and an upgrade from bipartite targets for \(H_5\)

**Core mechanism.**  
Use the colour-critical nature of \(H_5\). A dense \(H_5\)-free red graph should be close to bipartite; inside each side, the blue graph is correspondingly dense. Combine this with the BGS theorem for bipartite targets.

**Key lemma needed.**  
A dichotomy such as:

> For \(N=Cm\), every \(H_5\)-free red graph either has enough blue pseudorandomness to contain every \(m\)-edge \(H\), or admits a near-bipartition \(V=X\sqcup Y\) in which one can embed all nonbipartite components of \(H\) inside blue-dense pieces and use the BGS bipartite-target theorem for the remaining structure.

A composition lemma is essential: independently embedded bipartite pieces must be joined by the required blue edges.

**Why it might work.**  
Simonovits stability provides unusually strong global information for \(H_5\). In the extremal model \(T_2(N)\), the blue graph is the union of two cliques, and if \(C\) is large then either clique alone has room for all \(v(H)\le2m\) vertices. Thus the exact extremal configuration is benign; the challenge is controlling perturbations.

**Most likely failure point.**  
Stability controls the number of exceptional edges but not their concentration. A small exceptional red set can be concentrated around vertices crucial for embedding a high-degree or nonbipartite part of \(H\). Also, decomposing \(H\) into bipartite subgraphs does not by itself produce compatible embeddings.

**Quick blockage test.**  
Start with a red complete bipartite graph and add the largest possible \(H_5\)-free family of red edges inside one part. Determine computationally whether the blue graph can omit small nonbipartite graphs with unusually few edges relative to \(N\). Focus on triangles with many pendant edges, odd cycles with large attached stars, and disjoint unions of such components.

---

### Route 5: Disproof via low-independence \(G\)-free graphs or structured complements

**Core mechanism.**  
Construct \(G\)-free red graphs whose complements omit a target with substantially fewer than \(N\) edges.

The cleanest version uses clique targets: seek \(G\)-free graphs \(F_N\) with
\[
\alpha(F_N)=o(\sqrt N).
\]

A broader version seeks a graph \(H_N\not\subseteq\overline F_N\) with
\[
e(H_N)=o(N)
\]
even when \(\alpha(F_N)\) is too large for a clique target.

**Key lemma needed.**  
Either:

1. an explicit or probabilistic construction of \(G\)-free \(F_N\) with \(\alpha(F_N)=o(\sqrt N)\); or
2. a structural invariant of \(\overline F_N\), such as bounded clique number, chromatic restrictions, forbidden multipartite patterns, or deficient matching structure, that excludes an \(o(N)\)-edge no-isolate target.

**Why it might work.**  
This is precisely how \(K_4\) fails Ramsey size linearity. Highly pseudorandom forbidden-subgraph constructions and \(G\)-free processes are natural sources of small independent sets.

**Most likely failure point.**  
For these three graphs, the forbidden-red condition may itself force independent sets of order \(\Omega(\sqrt N)\), blocking clique targets. Moreover, since any no-isolate \(H\) has \(v(H)\le2e(H)\), omitting a target with \(o(N)\) edges means omitting a graph on \(o(N)\) vertices; a very dense blue graph may contain every such graph even if it misses some large spanning structures.

**Quick blockage test.**  
For each candidate family \(F_N\), compute or bound
\[
\frac{N}{\alpha(F_N)^2}.
\]
If this remains bounded, the clique route cannot disprove the problem. Then compute the minimum number of edges in a no-isolate graph absent from \(\overline F_N\). A disproof requires this minimum to be \(o(N)\).

---

## 8. Verdict on difficulty

This is a genuinely difficult open Ramsey problem, not a routine consequence of extremal graph theory.

The \(K_{3,3}\) case was explicitly singled out by Erdős and remains open. Any positive solution must, at minimum, deliver the strong off-diagonal consequence
\[
R(K_{3,3},K_t)=O(t^2),
\]
and then go substantially beyond clique targets to arbitrary irregular and disconnected graphs with \(m\) edges.

The \(Q_3\) case faces a similar gap: red \(Q_3\)-free graphs are asymptotically sparse, but converting that fact into universal blue embeddings on the sharp \(O(m)\) vertex scale requires much finer structure than Erdős–Stone theory provides.

The \(H_5\) case is the most sharply localized. It is already solved when the target is bipartite, and every longer subdivision of \(K_4\) is solved. The unresolved issue is exactly the exceptional five-vertex subdivision against arbitrary nonbipartite targets. Colour-critical stability makes this case potentially more approachable, but the contrast with \(K_4\)—which is decisively not Ramsey size linear—shows that small structural differences have major consequences.

No equivalence with a single famous named conjecture is given in the known commentary, but the problem contains major off-diagonal Ramsey estimates as necessary special cases. A complete solution will likely require a new universal embedding principle for complements of these specific forbidden-subgraph classes, or a new pseudorandom construction providing an unbounded counterexample family.