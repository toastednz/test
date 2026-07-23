# Erdős Problem #660: Distinct distances among vertices of a convex polyhedron

## 1. Precise statement

Let \(P\subset \mathbb R^{3}\) be a bounded, three-dimensional convex polytope, and let

\[
V(P)=\{x_1,\dots,x_n\}
\]

be its complete vertex set. Thus:

- the \(x_i\) are pairwise distinct;
- \(P=\operatorname{conv}\{x_1,\dots,x_n\}\);
- \(\dim P=3\);
- every \(x_i\) is an extreme point of \(P\).

Define the set of distinct positive pairwise Euclidean distances

\[
\Delta(P)
 =\left\{\|x_i-x_j\|_2:1\le i<j\le n\right\}
\]

and let

\[
D(P)=|\Delta(P)|.
\]

Define the extremal function

\[
m_3(n)=\min\{D(P):P\subset\mathbb R^3
\text{ is a three-dimensional convex polytope with }n\text{ vertices}\}.
\]

The standard formal reading of the problem is:

> Is it true that
> \[
> m_3(n)\ge \left(\frac12-o(1)\right)n
> \qquad (n\to\infty)?
> \]

Equivalently:

\[
\forall \varepsilon>0\;\exists N_\varepsilon\;\forall n\ge N_\varepsilon
\;\forall P,\qquad
D(P)\ge (1-\varepsilon)\frac n2.
\]

Equivalently again,

\[
\liminf_{n\to\infty}\frac{2m_3(n)}n\ge 1.
\]

The \(o(1)\) must be uniform over all \(n\)-vertex convex polytopes, not chosen separately for each configuration.

### Conventions and alternative readings

1. **“Convex polyhedron”** is most naturally read here as a bounded convex polytope. If unbounded polyhedra were allowed, that would enlarge the class and should be stated separately.
2. Some authors allow lower-dimensional convex polytopes lying in \(\mathbb R^3\). Under that reading, coplanar configurations must also be included. The coplanar case is already covered by Altman’s planar theorem and does not appear to be the intended difficulty.
3. “The vertices” normally means that the listed points are exactly the vertex set, not merely points chosen from a larger polyhedron. For the distance question, the essential condition is that every listed point be extreme in their convex hull.
4. The square brackets in the database display do not appear to denote a floor function. Even if they did, this would not affect the asymptotic formulation.

---

## 2. Sharpness of the constant \(1/2\)

The constant \(1/2\) cannot be asymptotically improved.

Let \(m=n-1\), let

\[
v_j=\left(R\cos\frac{2\pi j}{m},R\sin\frac{2\pi j}{m},0\right),
\qquad 0\le j<m,
\]

be the vertices of a regular \(m\)-gon, and let \(a=(0,0,h)\) be an apex. The convex hull is a three-dimensional pyramid.

The base distances are

\[
2R\sin\frac{\pi k}{m},
\qquad 1\le k\le \left\lfloor\frac m2\right\rfloor,
\]

and these values are strictly increasing in \(k\). Choose some \(k_0\) for which the corresponding chord \(L\) is larger than \(R\), for example \(k_0=\lfloor m/2\rfloor\), and set

\[
h=\sqrt{L^2-R^2}.
\]

Then every apex-to-base distance equals \(L\), already one of the base distances. Consequently,

\[
D(P)=\left\lfloor\frac m2\right\rfloor
=\left\lfloor\frac{n-1}{2}\right\rfloor.
\]

Thus

\[
m_3(n)\le \left\lfloor\frac{n-1}{2}\right\rfloor,
\]

so an affirmative answer would determine the asymptotic extremal value:

\[
m_3(n)=\left(\frac12+o(1)\right)n.
\]

This construction is also a warning that distances incident to an apex need not contribute any new distance values.

---

## 3. What counts as a solution

### A complete proof

A complete affirmative solution must produce a function \(\eta(n)\to 0\) such that every three-dimensional convex \(n\)-vertex polytope \(P\) satisfies

\[
D(P)\ge \frac n2(1-\eta(n)).
\]

Any of the following stronger statements would suffice:

\[
D(P)\ge \frac n2-O(1),
\]

or

\[
D(P)\ge \frac n2-o(n),
\]

or an exact lower bound with only finitely many exceptional \(n\).

The proof must cover:

- nonsimplicial and nonsimple polytopes;
- configurations with extensive symmetry;
- configurations with many equal distances;
- arbitrarily flat but still three-dimensional polytopes;
- all sufficiently large \(n\), uniformly over the geometry of \(P\).

If lower-dimensional polytopes are included in the interpretation, the proof should explicitly invoke or reprove the planar case.

### A complete disproof

The logical negation is:

\[
\exists \varepsilon_0>0\quad
\text{for infinitely many }n,\quad
\exists P_n\quad
D(P_n)<(1-\varepsilon_0)\frac n2.
\]

Thus a disproof requires an infinite family of convex three-dimensional polytopes with

\[
\liminf_{n\to\infty}\frac{D(P_n)}n<\frac12.
\]

An explicit counterexample family must provide:

1. coordinates, or an unambiguous geometric construction, for all members of the family;
2. a proof that all listed points are distinct;
3. a proof that all listed points are vertices of a three-dimensional convex hull;
4. an exact or rigorous upper bound for the number of distinct distances;
5. a fixed positive gap below \(n/2\) along an infinite sequence of \(n\).

For algebraic or trigonometric coordinates, equalities of distances must be verified exactly, preferably using squared distances.

A finite polytope with \(D(P)<n/2\) does **not** disprove the problem.

---

## 4. What does not count

The following do not resolve the problem.

### Insufficient lower bounds

- \(D(P)\gg n\) with an unspecified or fixed constant smaller than \(1/2\);
- \(D(P)\ge cn\) for one fixed \(c<1/2\);
- \(D(P)\ge n^\alpha\) with \(\alpha<1\);
- \(D(P)\ge n/\log n\);
- \(D(P)\ge (1/2-\varepsilon)n\) for one fixed \(\varepsilon>0\);
- a bound valid only for infinitely many \(n\);
- a bound valid only for generic, random, simplicial, simple, cospherical, or centrally symmetric polytopes.

A result of the form

\[
D(P)\ge \frac n2-f(n)
\]

does resolve the problem only if \(f(n)=o(n)\).

### Insufficient counterexamples

- one polytope, or finitely many polytopes, with fewer than \(n/2\) distances;
- a family with \(D(P_n)=n/2-O(1)\);
- a family with \(D(P_n)/(n/2)\to 1\);
- a family that is coplanar if the construction is claimed to refute the full-dimensional formulation but is not made three-dimensional;
- numerical evidence for distance coincidences without exact verification;
- configurations containing nonvertex points.

### Other nonresolutions

- conditional results depending on an unproved rigidity, incidence, or classification conjecture;
- heuristics suggesting regular pyramids are extremal;
- improvements for the planar problem alone;
- counting equal-distance pairs without converting the estimate to a sufficiently strong bound on distinct values.

---

## 5. Known results and context

### 5.1 The planar theorem of Altman

The database commentary states that Altman proved the corresponding planar result for the vertices of a convex polygon.

The sharp planar formulation must account for parity: a regular \(n\)-gon has exactly

\[
\left\lfloor\frac n2\right\rfloor
\]

distinct distances. Thus the standard sharp statement is that the vertices of a convex \(n\)-gon determine at least \(\lfloor n/2\rfloor\) distinct distances, or an equivalent parity-adjusted formulation. The phrase “at least \(n/2\)” in informal summaries cannot literally be correct for odd \(n\).

Altman’s proof fundamentally uses the cyclic order of the vertices of a convex polygon. No analogous global cyclic order exists on the boundary of a three-dimensional polytope.

### 5.2 Erdős’s reported linear bound

According to the database, Erdős wrote in [Er75f] that Altman had proved

\[
D(P)\gg n
\]

for convex polyhedra in \(\mathbb R^3\), but supplied no reference. Unless a proof is located and checked, this should be treated as an unverified historical assertion, not as an established theorem.

Even a valid bound \(D(P)\ge cn\) with \(c<1/2\) would not settle Problem #660.

### 5.3 Elementary few-distance bounds

Suppose an arbitrary \(n\)-point set in \(\mathbb R^3\) determines \(s\) distances \(\delta_1,\dots,\delta_s\). For each point \(x_i\), define

\[
p_i(x)=\prod_{r=1}^{s}
\bigl(\|x-x_i\|^2-\delta_r^2\bigr).
\]

Then \(p_i(x_j)=0\) for \(j\ne i\), while \(p_i(x_i)\ne0\). Hence the \(p_i\) are linearly independent. Since they have degree at most \(2s\),

\[
n\le \binom{2s+3}{3}.
\]

This gives only

\[
s=\Omega(n^{1/3}),
\]

and does not use convexity. It illustrates how far standard polynomial interpolation is from the desired linear estimate.

There are stronger general distinct-distance and few-distance results in the literature, but known general-purpose bounds remain far below the required \((1/2-o(1))n\) threshold.

### 5.4 Cospherical configurations and the Delsarte–Goethals–Seidel bound

Every finite set of distinct points on a sphere is in convex position: the tangent plane to the sphere at any point strictly separates that point from all the other points.

Thus the problem already contains the spherical few-distance problem on \(S^2\) as a substantial special case.

For an \(s\)-distance set on \(S^2\), the Delsarte–Goethals–Seidel absolute bound gives

\[
n\le
\binom{s+2}{2}+\binom{s+1}{2}
=(s+1)^2.
\]

Therefore the general harmonic-polynomial method yields only

\[
s\ge \sqrt n-1,
\]

again far short of \(n/2\). An affirmative solution would require much more than the standard absolute bound.

### 5.5 Squared Euclidean distance matrices

For points in \(\mathbb R^3\), the squared distance matrix

\[
Q_{ij}=\|x_i-x_j\|^2
\]

has rank at most \(5\), since

\[
Q_{ij}
=\|x_i\|^2+\|x_j\|^2-2x_i\cdot x_j.
\]

Equivalently, after double centering,

\[
B=-\frac12JQJ,\qquad
J=I-\frac1n\mathbf 1\mathbf 1^{\mathsf T},
\]

is positive semidefinite of rank at most \(3\). These are important algebraic constraints, but low rank alone has not yielded a linear lower bound for the number of distinct entries.

### 5.6 Diameter graphs

The Vázsonyi conjecture, proved by Grünbaum, Heppes, and Straszewicz, states that an \(n\)-point set in \(\mathbb R^3\) has at most \(2n-2\) diameter pairs.

This controls how many pairs can realize the largest distance, but does not directly force many different distances. All diameter pairs, by definition, realize the same value.

### 5.7 Polyhedral graph structure

By Steinitz’s theorem, the graphs of three-dimensional convex polytopes are exactly the finite planar \(3\)-connected graphs. In particular, the \(1\)-skeleton has at most \(3n-6\) edges and contains vertices of bounded degree.

This gives useful combinatorial induction possibilities, but counting graph edges is not the same as counting all pairwise distance values.

### 5.8 Small highly symmetric examples

Exact lower bounds near \(n/2\) cannot hold for every \(n\):

- a regular tetrahedron has \(n=4\) and one distance;
- a regular octahedron has \(n=6\) and two distances;
- a regular icosahedron has \(n=12\) and three distances.

These finite examples are compatible with an asymptotic statement but show that any proof must permit substantial bounded-size exceptions.

### Status

The planar analogue is settled. The asymptotic upper bound \(m_3(n)\le n/2+O(1)\) is elementary via regular pyramids. The required matching lower bound in three dimensions remains open.

---

## 6. Traps and edge cases

### 6.1 Exact versus asymptotic bounds

Finite counterexamples below \(n/2\) are irrelevant. Even an infinite family with

\[
D(P_n)=\frac{n}{2}-100
\]

supports rather than refutes the conjectured asymptotic.

### 6.2 Parity

A regular \(n\)-gon has \(\lfloor n/2\rfloor\) distances, not \(\lceil n/2\rceil\). Any use of the planar theorem must retain the correct floor and parity conventions.

### 6.3 Vertex condition

Convex position means every \(x_i\) is extreme. Points lying in the relative interiors of edges, facets, or the whole convex hull do not count as vertices.

A convenient exact certificate that \(x_i\) is a vertex is a vector \(u_i\) such that

\[
u_i\cdot x_i>u_i\cdot x_j
\qquad\text{for all }j\ne i.
\]

### 6.4 Full dimension

The hull must have affine dimension \(3\) under the standard reading. A nearly flat polytope is allowed; a genuinely coplanar polygon is not.

### 6.5 Projection is unsafe

Orthogonal, radial, or generic projection may preserve convexity properties but does not preserve Euclidean distances. A planar distinct-distance theorem cannot simply be applied to a projection.

Only Euclidean similarities preserve the distance-equality pattern. General affine transformations do not.

### 6.6 Face-by-face arguments do not add automatically

Applying Altman’s theorem separately to polygonal faces yields sets of distances, but the same numerical distance may recur on many faces. One obtains the maximum of the facewise bounds, not their sum, unless overlap is controlled.

Moreover, a simplicial polytope has only triangular faces, so no individual face gives a large planar polygon.

### 6.7 No guaranteed large planar subset

The vertex set of a three-dimensional polytope need not contain a planar or projected convex subset of linear size suitable for Altman’s theorem.

### 6.8 Equal-distance spheres can contain many vertices

For a fixed vertex \(x\) and a radius \(r\), the sphere \(S(x,r)\) can contain many other vertices. There is no constant upper bound on the number of vertices at one prescribed distance from \(x\).

### 6.9 Generic perturbation works in the wrong direction

A generic perturbation usually destroys equalities and increases the number of distinct distances. It cannot be used to infer a lower bound for highly symmetric or degenerate configurations, which are precisely the likely extremizers.

### 6.10 Edge lengths are only a subset of all distances

A polytope may have few edge lengths but many diagonal lengths, or conversely. An argument involving only the \(1\)-skeleton must explicitly connect edge-length diversity to diversity among all vertex pairs.

### 6.11 Diameter-pair bounds do not count diameter values

The theorem “at most \(2n-2\) diameter pairs” concerns the multiplicity of one value. It does not imply that repeated removal of diameter pairs produces many new values. Regular polygons and pyramids immediately expose this problem.

### 6.12 Numerical clustering is unreliable

Near-equalities of floating-point distances are not exact equalities. Since counterexamples require engineered coincidences, all decisive computations should use squared distances and exact arithmetic, minimal polynomials, or certified interval separation.

---

## 7. Verification hooks

### 7.1 Exact distance counter

For a proposed coordinate set:

1. compute all
   \[
   q_{ij}=\|x_i-x_j\|^2;
   \]
2. reduce each value in an exact algebraic number representation;
3. sort or hash the canonical representations;
4. count distinct values.

For rational coordinates, all \(q_{ij}\) are rational. For coordinates in a fixed number field, use a fixed field basis and exact coefficient vectors.

### 7.2 Convexity and vertex certification

For each \(i\), solve the strict separation problem

\[
u_i\cdot(x_i-x_j)>0
\qquad(j\ne i).
\]

After normalization, this can be turned into the linear program

\[
u_i\cdot(x_i-x_j)\ge1
\qquad(j\ne i)
\]

when feasible up to scaling. Alternatively, compute the convex hull and verify that every input index appears as a hull vertex.

For exact certification, record rational separating vectors whenever the coordinates are rational.

If all points lie on the same sphere, convexity is automatic: the tangent plane at each point is a strict supporting plane.

### 7.3 Dimension check

Choose four points and verify that

\[
\det(x_{i_2}-x_{i_1},x_{i_3}-x_{i_1},x_{i_4}-x_{i_1})\ne0.
\]

### 7.4 Euclidean distance matrix feasibility

For an abstract proposed distance pattern, build a squared distance matrix \(Q\) and check:

- \(Q=Q^{\mathsf T}\);
- \(Q_{ii}=0\);
- \(Q_{ij}>0\) for \(i\ne j\);
- \(B=-\frac12JQJ\succeq0\);
- \(\operatorname{rank}B=3\).

Coordinates can then be recovered from a rank-three factorization of \(B\). The recovered points must still pass the extreme-point test.

### 7.5 Symmetric cyclic-orbit search

A useful exact family is

\[
x_{a,k}=
\left(
r_a\cos\frac{2\pi(k+\theta_a)}m,\,
r_a\sin\frac{2\pi(k+\theta_a)}m,\,
z_a
\right),
\]

where \(1\le a\le q\) and \(0\le k<m\). The squared distance between two such points is

\[
r_a^2+r_b^2+(z_a-z_b)^2
-2r_ar_b
\cos\frac{2\pi(k-\ell+\theta_a-\theta_b)}m.
\]

If \(r_a^2+z_a^2=1\), all points lie on \(S^2\) and hence are vertices. Symbolic search can try to force overlaps between the distance spectra associated with different orbit pairs \((a,b)\).

A disproof through this route must achieve fewer than \((1/2-\delta)qm\) total values for some fixed \(\delta>0\).

### 7.6 Small-case database

Compute exact distance counts for:

- regular pyramids;
- prisms and antiprisms;
- bipyramids;
- Platonic and Archimedean solids;
- cyclic polytopes on the moment curve;
- stacked polytopes;
- geodesic subdivisions of the icosahedron;
- unions of latitude orbits on \(S^2\).

Record both the full distance spectrum and multiplicities. This will test proposed structural lemmas against the most symmetric obstructions.

### 7.7 Semialgebraic search for few-distance configurations

For small \(n,s\), introduce distance values \(\lambda_1,\dots,\lambda_s\) and a coloring of the pairs by these values. Impose the Euclidean distance matrix constraints and solve using:

- semidefinite relaxations;
- nonlinear algebraic solving;
- Gröbner bases for promising patterns;
- exact reconstruction from high-precision solutions.

Enumerating \(3\)-connected planar graphs with software such as `plantri` can additionally constrain the intended convex hull graph, though the distance conditions involve the complete graph.

---

## 8. Attack routes

### Route 1: Extend Altman’s cyclic-order mechanism through support geometry

**Core idea.** Replace the cyclic order of a convex polygon by an order derived from rotating support planes, the Gaussian map, or a generic family of directions on \(S^2\).

**Key lemma needed.** Construct a collection \(\mathcal C\) of at least \(n-o(n)\) vertex pairs, selected by support-geometric rules, such that every numerical distance occurs on at most two pairs of \(\mathcal C\). Then

\[
D(P)\ge \frac{|\mathcal C|}{2}
\ge \frac n2-o(n).
\]

A weaker weighted version, with total charge at least \(n-o(n)\) and charge at most \(2\) per distance value, would also suffice.

**Why it might work.** In the plane, convexity and cyclic order force monotonicity and noncrossing relations among chords. The normal fan of a three-dimensional polytope gives a cell decomposition of \(S^2\) that may support a higher-dimensional analogue.

**Likely failure point.** There is no canonical total order on a polyhedral sphere. A distance value can recur in many widely separated regions of the normal fan, and local noncrossing arguments need not control global coincidences.

**Quick test.** Implement any proposed certificate-selection rule on regular pyramids, prisms, the octahedron, and the icosahedron. Verify whether it really selects \(n-o(n)\) pairs and whether a single distance label can appear more than twice.

---

### Route 2: Vertex deletion and low-degree induction

**Core idea.** Use planarity of the \(1\)-skeleton to repeatedly delete vertices of degree at most \(5\), comparing the distance set before and after deletion.

A recurrence resembling

\[
m_3(n)\ge m_3(n-2)+1
\]

up to \(o(n)\) exceptional steps would yield the desired bound.

**Key lemma needed.** In every sufficiently large convex polytope, one can remove one or two carefully chosen vertices while retaining a three-dimensional convex hull, and either:

- at least one distance value disappears, or
- the absence of a disappearing value forces a rigid local configuration that can occur only \(o(n)\) times.

**Why it might work.** Every remaining vertex stays extreme after another vertex is deleted, and the polyhedral graph has low-degree vertices. This provides a natural induction parameter.

**Likely failure point.** All distances incident to a removed vertex may already occur elsewhere. The regular-pyramid construction deliberately makes every apex distance an old base distance. Local graph degree gives little control over global diagonal lengths.

**Quick test.** For each small symmetric polytope, compute for every vertex \(v\) the decrement

\[
D(P)-D(P-v).
\]

Search for large examples in which this decrement is zero for almost every removable vertex. Such examples would block a naive deletion recurrence.

---

### Route 3: Distance-matrix rank, polynomial interpolation, and stress rigidity

**Core idea.** Combine the rank-\(5\) structure of squared distance matrices with the fact that every point is exposed. Try to prove that a low-rank Euclidean distance matrix whose underlying points are all extreme cannot use substantially fewer than \(n/2\) distinct nonzero entries.

**Key lemma needed.** A structural theorem of the following kind:

> If a symmetric Euclidean distance matrix \(Q\) has embedding dimension \(3\), all embedded points are extreme, and \(Q\) has \(s\) distinct positive entries, then
> \[
> n\le 2s+o(s).
> \]

A more promising non-tautological version would produce an interpolation or stress space of effective dimension at most \(2s+o(s)\), in which \(n\) independent vertex-evaluation objects live.

**Why it might work.** Few distinct distances impose a strong edge-coloring or association-scheme structure on a matrix of fixed rank. Extremality adds strict separating inequalities absent from arbitrary low-rank matrices.

**Likely failure point.** Convexity consists primarily of inequalities, while rank and polynomial methods exploit identities. The standard polynomial spaces have dimension quadratic or cubic in \(s\), not linear.

**Quick test.** For known few-distance polytopes, compute:

- the adjacency matrices of each distance class;
- the algebra they generate;
- eigenvalue multiplicities;
- affine stress spaces;
- ranks of candidate interpolation families.

If regular pyramids already force dimension substantially above \(2s+O(1)\), the proposed algebraic space is the wrong one.

---

### Route 4: Spherical harmonic bounds plus stability and reduction

**Core idea.** First solve the problem for cospherical vertex sets, where distances correspond to inner products and harmonic analysis is available. Then seek a reduction from general convex polytopes to one or a controlled number of spherical layers.

**Key lemma needed.** At minimum, a strengthened spherical few-distance theorem:

\[
X\subset S^2,\quad |X|=n,\quad
|\{\|x-y\|:x\ne y\in X\}|=s
\quad\Longrightarrow\quad
n\le 2s+o(s).
\]

For the full problem one would additionally need a reduction showing that an extremal or near-extremal convex polytope can be transformed into a spherical configuration without increasing the number of distances by a linear amount.

**Why it might work.** Every spherical point is exposed, so this is already a broad subclass. The only finite rotation groups in dimension three with unbounded orbit size are essentially cyclic or dihedral families, and their natural distance counts are approximately half their cardinality. This suggests that large highly symmetric configurations may be forced toward polygonal or pyramidal behavior.

**Likely failure point.** The Delsarte–Goethals–Seidel bound is only \(n\le(s+1)^2\), and no general radial projection preserves distance equalities. Solving the spherical case would still leave the nonspherical case.

**Quick test.** Search cyclic and dihedral multi-orbit configurations on \(S^2\) symbolically. Determine whether two or more latitude orbits can produce extensive overlap among their cosine spectra. Any family with \(D/n<1/2-\delta\) would disprove the original problem directly.

---

### Route 5: Farthest-neighbor and diameter-layer decompositions

**Core idea.** Organize vertices by successive farthest-neighbor relations or diameter graphs, using supporting planes perpendicular to extremal chords.

**Key lemma needed.** A multiscale statement asserting that, although one diameter value may cover many vertices, secondary and tertiary farthest-distance layers collectively produce at least one new value for every two vertices, apart from \(o(n)\) vertices.

**Why it might work.** Diameter pairs have strong support geometry, and diameter graphs in \(\mathbb R^3\) are highly constrained by the \(2n-2\) theorem.

**Likely failure point.** Repeated diameter removal can select the same distance many times. A regular polygon has many diametrically opposite pairs but only one diameter value; the remaining distance values arise from lower scales. The Vázsonyi theorem is an upper bound on multiplicity and is not close to the required charging theorem.

**Quick test.** Run the proposed peeling scheme on regular pyramids with even and odd base size. If the proof only records diameters, it will fail immediately. A viable version must provably extract the entire hierarchy of base chord lengths.

---

### Route 6: Direct disproof through symmetric multi-orbit constructions

**Core idea.** Construct an infinite family in convex position, preferably on \(S^2\), formed from several large cyclic or dihedral orbits whose internal and cross-distance spectra overlap heavily.

**Key lemma needed.** Find fixed parameters \(q\) and \(\delta>0\), and configurations with \(n=qm\), such that the union of all spectra

\[
A_{ab}-B_{ab}\cos\frac{2\pi(k+\theta_{ab})}{m}
\]

contains at most

\[
\left(\frac q2-\delta\right)m
\]

distinct values.

**Why it might work.** Prisms, antiprisms, bipyramids, and unions of latitude circles already have distance spectra described by a small number of cosine families. Carefully tuning heights, radii, and angular offsets may force nontrivial identifications between those families.

**Likely failure point.** A nonzero vertical separation usually translates one cosine spectrum relative to another, producing almost disjoint sets of values. Finite cosine sets have very little translation invariance. Classification of finite rotation groups also limits sources of large symmetry in three dimensions.

**Quick test.** For \(q=2,3,4\) and moderate \(m\), perform exact symbolic searches over rational or low-degree algebraic values of \(r_a,z_a,\theta_a\). Measure the overlap of the spectra before attempting convex-hull optimization. Any observed advantage must persist linearly in \(m\), not merely save \(O(1)\) values.

---

## 9. Verdict on difficulty

This is a genuinely difficult asymptotic extremal geometry problem. The target constant is sharp, but the standard tools for distinct distances, few-distance sets, incidence geometry, polynomial interpolation, and spherical harmonics fall far short of it. The three-dimensional boundary has neither the cyclic order that drives the planar theorem nor enough global combinatorial rigidity for an immediate induction.

The problem is not presently known to be equivalent to a single famous named conjecture. However, it contains a strong asymptotic classification problem for spherical few-distance sets on \(S^2\), where the standard Delsarte–Goethals–Seidel bound is only quadratic rather than the required asymptotically linear bound. That subproblem alone appears substantial.

The most plausible affirmative route would need a new convex-geometric charging principle or a strong stability theorem showing that configurations with unusually few distances are asymptotically polygonal, pyramidal, cyclic, or dihedral. The most plausible disproof route is an exact multi-orbit spherical construction with extensive spectral overlap. Neither mechanism is currently available.

The unreferenced historical claim \(D(P)\gg n\), even if recoverable, would represent meaningful progress but would not by itself settle the sharp asymptotic constant in Problem #660.