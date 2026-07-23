# Problem Brief: Erdős Problem #614

## 1. Precise statement

### Standard formulation

All graphs are finite, simple, undirected graphs. Let \(n,k\in \mathbb Z_{\ge 0}\). Define \(f(n,k)\) to be the minimum number of edges in an \(n\)-vertex graph \(G\) such that

\[
\forall S\subseteq V(G),\quad |S|=k+2
\implies
\Delta(G[S])\ge k,
\]

where:

- \(G[S]\) is the subgraph induced by \(S\);
- \(d_{G[S]}(v)\) is the number of neighbors of \(v\) inside \(S\);
- \(\Delta(G[S])=\max_{v\in S}d_{G[S]}(v)\).

Equivalently, every \((k+2)\)-element set \(S\) contains a vertex adjacent in \(G\) to at least \(k\) of the other \(k+1\) vertices of \(S\). Thus the witnessing vertex may have at most one nonneighbor inside \(S\).

The problem asks for an exact determination of \(f(n,k)\), presumably for all admissible \(n,k\).

### Domain and vacuous cases

- If \(n<k+2\), there are no subsets of size \(k+2\), so the condition is vacuous and
  \[
  f(n,k)=0.
  \]
- If \(k=0\), the condition is automatic because every graph has maximum degree at least \(0\), so
  \[
  f(n,0)=0.
  \]
- The nontrivial range is therefore
  \[
  k\ge 1,\qquad n\ge k+2.
  \]

### Complementary extremal formulation

Let \(H=\overline G\). If \(|S|=k+2\), then for each \(v\in S\),

\[
d_{H[S]}(v)=(k+1)-d_{G[S]}(v).
\]

Therefore

\[
\Delta(G[S])\ge k
\iff
\delta(H[S])\le 1.
\]

Put \(m=k+2\), and let

\[
\mathcal F_m
=
\{F:\ |V(F)|=m,\ \delta(F)\ge 2\}.
\]

Here \(\mathcal F_m\) is a finite family of ordinary, not necessarily induced, forbidden subgraphs. Define

\[
\operatorname{ex}(n,\mathcal F_m)
=
\max\{e(H): |V(H)|=n,\ H\text{ contains no member of }\mathcal F_m
\text{ as a subgraph}\}.
\]

Then

\[
\boxed{
f(n,k)=\binom n2-\operatorname{ex}(n,\mathcal F_{k+2}).
}
\]

Although the original statement refers to induced subgraphs, the complementary avoidance problem is monotone and can be stated using ordinary subgraphs: if \(H[S]\) has minimum degree at least \(2\), then \(H[S]\) itself is a member of \(\mathcal F_m\); conversely, extra edges cannot reduce minimum degree.

### Ambiguity in “determine”

The standard reading of “determine \(f(n,k)\)” is an exact formula or exact extremal characterization for all \(n,k\). An alternative reading is asymptotic determination for fixed \(k\) as \(n\to\infty\). That weaker reading is unlikely to be the intended open problem, because for every fixed \(k\ge2\) the leading quadratic term is already easy:

\[
f(n,k)=\left(\frac12+o(1)\right)n^2.
\]

The genuinely difficult content lies in the error term, exact values, and extremal constructions.

---

## 2. What counts as a solution

### Complete exact solution

A complete solution under the standard interpretation must give, for every \(n,k\), an explicit value of \(f(n,k)\), together with:

1. **Construction/upper bound:** an \(n\)-vertex graph \(G\) with exactly the claimed number of edges satisfying
   \[
   \Delta(G[S])\ge k
   \quad\text{for every }|S|=k+2.
   \]

2. **Optimality/lower bound:** a proof that every \(n\)-vertex graph satisfying the condition has at least that many edges.

Equivalently, in the complement it must determine \(\operatorname{ex}(n,\mathcal F_{k+2})\), construct an extremal \(\mathcal F_{k+2}\)-free graph, and prove no denser one exists.

An exact classification of all extremal graphs is stronger than necessary unless “determine” is interpreted as requiring structural characterization, but it would be highly valuable.

### Complete asymptotic solution

If the intended target is asymptotic, a complete answer must specify the regime. For example, for each fixed \(k\),

\[
f(n,k)=\binom n2-c_k n^\alpha+o(n^\alpha)
\]

would require proving both a construction and a matching universal bound with the same exponent and, if claimed, the same leading constant.

Merely showing \(f(n,k)\sim n^2/2\) for fixed \(k\ge2\) is already known from elementary extremal estimates and almost certainly does not resolve the database problem.

### What a disproof or counterexample means here

The database statement is a request, not a yes/no conjecture, so there is no standalone proposition to “disprove.” A counterexample is relevant only to a proposed formula or structural conjecture.

If a candidate formula claims \(f(n,k)=a\), then:

- To prove the claimed value is **too large**, it suffices to give an \(n\)-vertex graph with at most \(a-1\) edges satisfying the property.
- To prove it is **too small**, one needs a universal lower-bound proof showing that no graph with \(a\) edges can satisfy the property. A single graph cannot establish this direction.
- In the complement, a graph \(H\) with more than \(\binom n2-a\) edges and no \(m\)-vertex subgraph of minimum degree at least \(2\) disproves the corresponding upper bound on \(\operatorname{ex}(n,\mathcal F_m)\).

An explicit counterexample should be given by an adjacency list, adjacency matrix, algebraic construction, or other unambiguous description. Verification must check every \((k+2)\)-set, or supply a structural certificate such as girth greater than \(k+2\).

---

## 3. What does not count

The following do not solve the problem under its standard exact interpretation:

1. Solving only finitely many small values of \(n\) or \(k\).
2. Solving only \(k=1\), \(k=2\), or another fixed parameter.
3. Giving only the complementary identity
   \[
   f(n,k)=\binom n2-\operatorname{ex}(n,\mathcal F_{k+2});
   \]
   this is a useful reformulation, not a determination.
4. Proving only
   \[
   f(n,k)=\left(\frac12+o(1)\right)n^2
   \quad (k\ge2\text{ fixed}).
   \]
5. Giving an upper construction without a matching lower bound.
6. Giving a lower bound from degree counting, \(K_{2,k}\)-avoidance, or cycle avoidance without matching it.
7. Conditional formulas depending on unresolved extremal problems, finite-geometry conjectures, or unproved stability assertions.
8. Heuristics from random graphs or numerical optimization.
9. A formula valid only when \(n\) belongs to a prime-power sequence, unless the problem is explicitly restricted to that sequence.
10. Showing that high-girth complements work, without proving they are extremal.
11. Treating only connected forbidden graphs: \(\mathcal F_m\) includes disconnected graphs, such as disjoint unions of cycles whose total number of vertices is \(m\).

---

## 4. Known results and context

The supplied database commentary contains no mathematical result beyond a cross-reference to a graph problem collection. The following consequences and related theorems are nevertheless immediate or standard.

### 4.1 Exact boundary cases

If \(n<k+2\), then

\[
f(n,k)=0.
\]

If \(n=k+2\), the condition is imposed only on the whole graph. A vertex of degree at least \(k\) forces at least \(k\) edges, and a \(K_{1,k}\) together with one isolated vertex attains this. Hence

\[
\boxed{f(k+2,k)=k.}
\]

### 4.2 The case \(k=1\) is settled

Here every set of three vertices must span at least one edge, so \(G\) has no independent set of size three:

\[
\alpha(G)\le2.
\]

Equivalently, \(\overline G\) is triangle-free. By Mantel’s theorem,

\[
\operatorname{ex}(n,K_3)=\left\lfloor\frac{n^2}{4}\right\rfloor.
\]

Therefore

\[
\boxed{
f(n,1)=\binom n2-\left\lfloor\frac{n^2}{4}\right\rfloor.
}
\]

An extremal \(G\) is the disjoint union of two cliques whose orders differ by at most one.

### 4.3 The case \(k=2\) is exactly the \(C_4\) extremal problem

For \(k=2\), \(m=4\). Every graph on four vertices with minimum degree at least \(2\) contains a \(4\)-cycle. Conversely, the four vertices of any \(C_4\), with or without additional diagonals, induce a graph of minimum degree at least \(2\). Thus

\[
\mathcal F_4\text{-free}
\iff
C_4\text{-free}.
\]

Consequently,

\[
\boxed{
f(n,2)=\binom n2-\operatorname{ex}(n,C_4).
}
\]

This is crucial: determining \(f(n,k)\) exactly for all \(n,k\) would determine \(\operatorname{ex}(n,C_4)\) exactly for every \(n\), a famous and still unresolved extremal problem.

The standard codegree count gives Reiman’s bound

\[
\operatorname{ex}(n,C_4)
\le
\frac n4\left(1+\sqrt{4n-3}\right).
\]

Indeed, in a \(C_4\)-free graph every pair of vertices has at most one common neighbor, so

\[
\sum_v \binom{d(v)}2\le \binom n2.
\]

Finite-projective-plane polarity constructions give \(C_4\)-free graphs with

\[
\operatorname{ex}(n,C_4)
=
\left(\frac12+o(1)\right)n^{3/2}
\]

along suitable sequences, and hence for general \(n\) up to constant-order adjustment. Thus

\[
f(n,2)
=
\binom n2-\left(\frac12+o(1)\right)n^{3/2}.
\]

The exact value for arbitrary \(n\) is not known.

### 4.4 General forbidden subgraphs

For \(k\ge2\), the complete bipartite graph \(K_{2,k}\) has \(k+2\) vertices and minimum degree at least \(2\), so

\[
K_{2,k}\in\mathcal F_{k+2}.
\]

Therefore

\[
\operatorname{ex}(n,\mathcal F_{k+2})
\le
\operatorname{ex}(n,K_{2,k})
=
O_k(n^{3/2})
\]

by the Kővári–Sós–Turán theorem. More precisely, the usual codegree argument gives a leading upper bound of order

\[
\frac{\sqrt{k-1}}2 n^{3/2}+O_k(n).
\]

Hence, for every fixed \(k\ge2\),

\[
\boxed{
f(n,k)=\binom n2-O_k(n^{3/2})
=\left(\frac12+o(1)\right)n^2.
}
\]

This settles only the leading quadratic term.

Also, \(C_{k+2}\in\mathcal F_{k+2}\), so

\[
\operatorname{ex}(n,\mathcal F_{k+2})
\le
\operatorname{ex}(n,C_{k+2}).
\]

When \(k+2=2r\) is even, the Bondy–Simonovits even-cycle theorem gives

\[
\operatorname{ex}(n,\mathcal F_{2r})
=
O_r\!\left(n^{1+1/r}\right).
\]

This is stronger than the generic \(O_k(n^{3/2})\) estimate when \(r>2\).

### 4.5 High-girth lower constructions in the complement

If \(H\) has girth greater than \(m=k+2\), then \(H\) is \(\mathcal F_m\)-free. Indeed, every finite graph of minimum degree at least \(2\) contains a cycle, and an \(m\)-vertex graph contains a cycle of length at most \(m\).

Thus any graph of girth greater than \(k+2\) gives

\[
f(n,k)\le \binom n2-e(H).
\]

At the most elementary level, any forest works, giving

\[
\operatorname{ex}(n,\mathcal F_{k+2})\ge n-1
\]

and therefore

\[
f(n,k)\le \binom n2-(n-1).
\]

Random alteration gives, for fixed \(m\),

\[
\operatorname{ex}(n,\mathcal F_m)
\ge
c_m n^{1+1/(m-1)}
\]

for some \(c_m>0\), by constructing graphs with no cycle of length at most \(m\).

These high-girth constructions are sufficient but need not be extremal.

### 4.6 Some second-order growth rates

Let

\[
M_m(n)=\operatorname{ex}(n,\mathcal F_m).
\]

Then:

- \(M_3(n)=\lfloor n^2/4\rfloor\).
- \(M_4(n)=\operatorname{ex}(n,C_4)=\Theta(n^{3/2})\).
- \(M_5(n)=\Theta(n^{3/2})\): the upper bound follows from \(K_{2,3}\in\mathcal F_5\), while incidence graphs of projective planes have girth \(6\) and \(\Theta(n^{3/2})\) edges.
- \(M_6(n)=\Theta(n^{4/3})\): the upper bound follows from the Bondy–Simonovits bound for \(C_6\); incidence graphs of generalized quadrangles provide girth \(8\) constructions with \(\Theta(n^{4/3})\) edges along standard parameter sequences, extendable to arbitrary \(n\) up to constants.

These determine the exponent of the correction term for several small \(k\), but not exact values or generally the leading constant.

### 4.7 A basic certificate-counting inequality

For \(v\in V(G)\) with \(d(v)=d_v\), the number of \((k+2)\)-sets certified by \(v\)—meaning that \(v\) has at least \(k\) neighbors inside the set—is

\[
\binom{d_v}{k+1}
+
(n-1-d_v)\binom{d_v}{k}.
\]

Since every \((k+2)\)-set must be certified by at least one vertex,

\[
\boxed{
\sum_{v\in V(G)}
\left[
\binom{d_v}{k+1}
+
(n-1-d_v)\binom{d_v}{k}
\right]
\ge
\binom n{k+2}.
}
\]

This is a valid necessary condition, but overlap between certificates is substantial, so it is unlikely by itself to be exact.

---

## 5. Traps and edge cases

1. **Maximum degree, not average degree.**  
   Each \((k+2)\)-set needs one high-degree witness. No lower bound on the other vertices’ degrees is imposed.

2. **The witness depends on the set.**  
   There need not be a globally high-degree vertex certifying all subsets.

3. **Exactly \(k+2\) vertices.**  
   The quantified sets have exactly this size. The property implies that every larger set has maximum degree at least \(k\), but it does not impose the stronger threshold \(|S|-2\) on larger sets.

4. **Complement off-by-one.**  
   On a \((k+2)\)-set,
   \[
   d_{\overline G[S]}(v)=k+1-d_{G[S]}(v),
   \]
   so “degree at least \(k\)” becomes “complementary degree at most \(1\),” not at most \(0\).

5. **The complementary forbidden problem is ordinary, not induced.**  
   A copy of an \(m\)-vertex minimum-degree-two graph already violates the condition even if additional edges are present.

6. **Short cycles do not automatically violate the condition.**  
   A cycle on fewer than \(m\) vertices cannot simply be padded with arbitrary vertices: the added vertices may have degree \(0\) or \(1\). By contrast, a \(C_m\) always violates the condition.

7. **Disconnected forbidden graphs matter.**  
   For example, if \(m\) is the sum of two cycle lengths, the disjoint union of those cycles belongs to \(\mathcal F_m\).

8. **High girth is sufficient, not necessary.**  
   An \(\mathcal F_m\)-free graph may contain cycles of length at most \(m-1\), provided they cannot be extended or combined into an \(m\)-vertex subgraph of minimum degree \(2\).

9. **The \(k=1\) case behaves qualitatively differently.**  
   The complement may have quadratic density. For every fixed \(k\ge2\), it has only \(O_k(n^{3/2})\) edges.

10. **Do not assume extremal complements are bipartite.**  
    \(C_4\)-free polarity graphs may contain triangles, and deleting all odd-cycle edges can lose relevant extremal information.

11. **Do not confuse “contains a cycle” with “has minimum degree two.”**  
    A graph can contain a cycle and also have leaves. The entire selected \(m\)-vertex subgraph must have minimum degree at least \(2\).

12. **Growing \(k\) versus fixed \(k\).**  
    Constants hidden in \(O_k(\cdot)\) are not uniform when \(k\) grows with \(n\). Any asymptotic theorem must state its parameter regime.

---

## 6. Verification hooks

### 6.1 Direct exhaustive checker

For a candidate graph \(G\):

1. Enumerate all subsets \(S\subseteq V(G)\) of size \(k+2\).
2. Compute \(d_{G[S]}(v)\) for each \(v\in S\).
3. Reject if
   \[
   \max_{v\in S}d_{G[S]}(v)<k.
   \]

The complementary version is often faster:

1. Form \(H=\overline G\).
2. Reject if some \((k+2)\)-set \(S\) satisfies
   \[
   d_{H[S]}(v)\ge2\quad\text{for every }v\in S.
   \]

Bitset intersection makes this practical for moderate \(n\).

### 6.2 SAT/ILP encoding

Use binary variables \(x_{ij}\) for edges of \(H\). For every \(m\)-set \(S\) and every \(v\in S\), introduce a binary selector \(y_{S,v}\), intended to mean that \(v\) witnesses degree at most \(1\) in \(H[S]\).

Impose

\[
\sum_{v\in S} y_{S,v}\ge1
\]

and, for each \(v\in S\),

\[
\sum_{u\in S\setminus\{v\}}x_{uv}
\le
1+(m-2)(1-y_{S,v}).
\]

Maximize \(\sum_{i<j}x_{ij}\). An optimizer gives \(M_m(n)\), and hence \(f(n,k)\). To prove an upper bound \(M_m(n)<E\), ask whether the constraints together with \(\sum x_{ij}\ge E\) are satisfiable and produce a checkable UNSAT certificate.

### 6.3 Specialized \(k=2\) test

A graph \(H\) is \(C_4\)-free exactly when no pair of vertices has two distinct common neighbors. Thus check

\[
|N_H(u)\cap N_H(v)|\le1
\quad\text{for every }u\ne v.
\]

This detects \(C_4\)'s even when the four vertices have diagonal edges.

### 6.4 Girth certificate

To certify a sufficient construction, run breadth-first search from every vertex to detect cycles of length at most \(k+2\). If none exist, the complement is automatically \(\mathcal F_{k+2}\)-free.

This check is only sufficient: failure of the girth test does not imply failure of the desired property.

### 6.5 Unlabeled graph enumeration

For small \(n\):

1. Generate unlabeled graphs with `nauty`, `Traces`, or equivalent canonical augmentation.
2. Filter by the \(\mathcal F_m\)-free condition.
3. Record maximum edge count and all extremal isomorphism types.
4. Compare degree sequences, girth, block structure, automorphism groups, and codegree distributions.

This can expose incorrect structural conjectures quickly.

### 6.6 Internal consistency checks

Any implementation should reproduce:

\[
f(n,1)=\binom n2-\left\lfloor\frac{n^2}{4}\right\rfloor,
\]

\[
f(k+2,k)=k,
\]

and, for \(k=2\),

\[
f(n,2)=\binom n2-\operatorname{ex}(n,C_4).
\]

In particular, \(f(4,2)=2\), since \(\operatorname{ex}(4,C_4)=4\).

---

## 7. Attack routes

### Route 1: Structural theory of the complementary \(2\)-core

**Core mechanism.**  
Study extremal \(\mathcal F_m\)-free graphs \(H\) through their blocks, cycles, and \(2\)-cores. A violating set is exactly an \(m\)-vertex subgraph with nonempty full \(2\)-core.

**Needed key lemma.**  
A useful result would classify, or sharply constrain, how cyclic blocks in an \(\mathcal F_m\)-free graph can intersect. For example, one might seek a decomposition theorem saying that every dense \(\mathcal F_m\)-free graph consists of a controlled high-girth core plus bounded-size cyclic attachments.

**Why it might work.**  
The forbidden condition is explicitly a minimum-degree-two condition, so the \(2\)-core is the natural invariant. It also handles disconnected forbidden graphs, unlike an approach focused only on single cycles.

**Likely failure point.**  
High-girth graphs can have large, highly nontrivial \(2\)-cores. There may be no simple block or cactus description once \(n\) is large.

**Quick obstruction test.**  
Apply any proposed decomposition to incidence graphs of projective planes, generalized quadrangles, and \(C_4\)-free polarity graphs. If it forces bounded block size or bounded average degree, it is false.

---

### Route 2: Codegree, spectral, and even-cycle inequalities

**Core mechanism.**  
Exploit that \(K_{2,k}\in\mathcal F_{k+2}\), and that \(C_{k+2}\in\mathcal F_{k+2}\). Use codegree moments, adjacency-matrix traces, nonbacktracking walks, and spectral inequalities.

**Needed key lemma.**  
A substantial advance would show that if an \(n\)-vertex graph has edge count above a proposed threshold, then its codegree/cycle structure necessarily assembles into exactly \(m\) vertices of minimum degree at least \(2\), not merely a \(K_{2,k}\) or one cycle of the wrong length.

**Why it might work.**  
This recovers the sharp mechanism for \(k=2\), where common-neighbor counting is exactly the \(C_4\) argument, and links even \(m\) to Bondy–Simonovits-type methods.

**Likely failure point.**  
Codegree bounds detect \(K_{2,k}\) but may miss sparse forbidden configurations such as long cycles or disconnected unions of cycles. Different members of \(\mathcal F_m\) may dominate in different ranges.

**Quick obstruction test.**  
Compute codegree distributions in known high-girth constructions. If the proposed inequality predicts a forbidden \(m\)-vertex subgraph in a graph of girth greater than \(m\), the averaging step is too coarse.

---

### Route 3: Induction via low-degree vertices and hereditary deletion

**Core mechanism.**  
The class of \(\mathcal F_m\)-free graphs is hereditary under vertex deletion. If one can bound the minimum degree of every such graph, then

\[
M_m(n)\le M_m(n-1)+\delta_{\max}(n,m),
\]

where \(\delta_{\max}(n,m)\) is a universal upper bound on the minimum degree.

**Needed key lemma.**  
Prove a sharp statement of the form:

> Every \(\mathcal F_m\)-free \(n\)-vertex graph has a vertex of degree at most \(D_m(n)\),

with equality cases classified tightly enough that summing the recurrence gives the exact or sharp asymptotic extremal number.

**Why it might work.**  
Many extremal graph proofs reduce to finding a low-degree vertex and inducting. The forbidden family is finite and the property survives deletion.

**Likely failure point.**  
Known high-girth regular graphs show that \(D_m(n)\) can grow polynomially with \(n\). A degree bound alone may give the correct exponent but not the constant or exact structure.

**Quick obstruction test.**  
Compare the proposed \(D_m(n)\) with the degrees in polarity graphs and generalized-polygon incidence graphs. Any bound below those examples is immediately impossible.

---

### Route 4: Original-graph certificate covering and nonlinear optimization

**Core mechanism.**  
View each vertex \(v\) as covering the \((k+2)\)-sets in which it has at least \(k\) neighbors. Use the exact covering count

\[
C_v=
\binom{d_v}{k+1}
+
(n-1-d_v)\binom{d_v}{k}.
\]

Then combine

\[
\sum_v C_v\ge\binom n{k+2}
\]

with overlap estimates, degree-sum constraints, and possibly higher-order neighborhood intersections.

**Needed key lemma.**  
One needs a sharp lower bound on unavoidable overlap between the families of sets certified by different vertices. Without such a lemma, the basic covering inequality permits unrealistic degree distributions.

**Why it might work.**  
This attacks \(f(n,k)\) directly rather than through a large forbidden family and may reveal degree-sequence rigidity in extremal graphs.

**Likely failure point.**  
Certificate sets overlap heavily and in construction-dependent ways. Degree data alone cannot distinguish many graphs with radically different local configurations.

**Quick obstruction test.**  
Optimize the degree-only relaxation numerically and compare it with exact SAT values for small \(n\). A persistent large gap shows that codegree or neighborhood-geometry information is essential.

---

### Route 5: Algebraic and high-girth constructions — disproof-oriented

**Core mechanism.**  
Construct dense complements \(H\) using finite geometries, generalized polygons, lifts, random regular graphs, or algebraic incidence relations. Prove \(H\) is \(\mathcal F_m\)-free, most simply by proving girth greater than \(m\).

**Needed key lemma.**  
For a proposed construction with many short cycles, one needs a direct theorem that no selection of exactly \(m\) vertices has minimum degree at least \(2\). Girth alone may be too restrictive to reach the optimum.

**Why it might work.**  
This is the main route for disproving overly large proposed values of \(f(n,k)\): every extra edge in \(H\) removes an edge from \(G\). Finite geometries are already extremal or near-extremal for \(k=2,3,4\).

**Likely failure point.**  
High-girth constructions may be far from extremal because \(\mathcal F_m\)-free graphs are allowed to contain many short cycles. Also, available generalized polygons exist only for restricted girths and parameter sequences.

**Quick obstruction test.**  
For each construction, exhaustively check the condition for small field orders. Compare its edge count with SAT optima. If denser small examples contain short cycles but remain \(\mathcal F_m\)-free, pure girth is not the right extremal mechanism.

---

### Route 6: Computer-assisted conjecture generation and stability

**Core mechanism.**  
Compute \(M_m(n)\) and extremal graphs for small \(m,n\), identify recurring algebraic or decomposition patterns, and then formulate a stability theorem.

**Needed key lemma.**  
A successful generalization needs a theorem saying that every near-extremal \(\mathcal F_m\)-free graph is close, in edit distance or local structure, to one of a small family of constructions.

**Why it might work.**  
The forbidden family is finite for each \(m\), so exact SAT/ILP computations are feasible for small instances. Extremal graph problems often exhibit detectable regularity, degree concentration, or design-like codegrees.

**Likely failure point.**  
Small-\(n\) extremizers may be exceptional, while large extremizers arise only from finite geometries at much larger orders. Exact \(C_4\) extremal data already show irregular dependence on \(n\).

**Quick obstruction test.**  
Run independent computations under vertex-transitive, bipartite, and unrestricted assumptions. If the unrestricted optimum repeatedly exceeds all structured families, avoid prematurely conjecturing symmetry.

---

## 8. Verdict on difficulty

**Extremely difficult in its exact all-parameter form.**

The decisive obstruction is

\[
\boxed{
f(n,2)=\binom n2-\operatorname{ex}(n,C_4).
}
\]

Thus a full exact solution of Erdős Problem #614 would in particular determine the exact Turán number of the \(4\)-cycle for every \(n\). That is a famous longstanding problem in extremal graph theory. This connection should be treated as a major warning: an elementary closed formula for all \(n,k\) is not presently realistic unless it also produces a breakthrough on \(\operatorname{ex}(n,C_4)\).

Parts already settled include:

- all vacuous cases;
- \(n=k+2\);
- the complete case \(k=1\);
- the reduction of \(k=2\) to \(C_4\)-extremal theory;
- the leading asymptotic \(f(n,k)\sim n^2/2\) for each fixed \(k\ge2\);
- the order of the complementary correction for some small \(k\), including \(k=2,3,4\).

The most plausible meaningful research targets short of the full exact problem are:

1. determine \(M_m(n)\) asymptotically, including its exponent and leading constant, for fixed \(m\);
2. solve specific small \(k\) beyond the known reductions;
3. prove structural or stability theorems for extremal \(\mathcal F_m\)-free graphs;
4. obtain exact values on infinite algebraic parameter sequences;
5. classify finite extremizers computationally and derive rigorous recurrences.

Any claimed complete solution must explicitly confront the \(k=2\)/\(C_4\) barrier rather than bypassing it with a weaker asymptotic interpretation.