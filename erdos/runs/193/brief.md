# Problem Brief: Erdős Problem #193

## 1. Precise statement

Let \(S\subseteq \mathbb Z^3\) be finite. An **\(S\)-walk** is a sequence
\[
(a_n)_{n\ge 1},\qquad a_n\in \mathbb Z^3,
\]
such that
\[
a_{n+1}-a_n\in S\qquad\text{for every }n\ge 1.
\]

The standard reading of the database statement is that the image
\[
A=\{a_n:n\ge 1\}
\]
is infinite. Equivalently, one may restrict to walks whose vertices \(a_n\) are pairwise distinct; see the discussion below on loop erasure.

The problem asks whether the following universal assertion is true:

> For every finite \(S\subseteq\mathbb Z^3\) and every infinite \(S\)-walk \((a_n)_{n\ge1}\) with infinite image, there exist indices
> \[
> 1\le i<j<k
> \]
> such that \(a_i,a_j,a_k\) are three distinct collinear points.

Collinearity means that the three points lie on one affine line in \(\mathbb R^3\). Algebraically,
\[
(a_j-a_i)\times(a_k-a_i)=0.
\]
Equivalently, there are \(x\in\mathbb Z^3\), a primitive nonzero vector \(v\in\mathbb Z^3\), and three distinct integers \(r,s,t\) such that
\[
a_i=x+rv,\qquad a_j=x+sv,\qquad a_k=x+tv.
\]

### Equivalent formulations

1. **Bounded-step formulation.**  
   Since bounded subsets of \(\mathbb Z^3\) are finite, the problem is equivalent to asking whether every injective sequence \((a_n)\subseteq\mathbb Z^3\) satisfying
   \[
   \sup_n \|a_{n+1}-a_n\|<\infty
   \]
   contains three collinear points.

2. **Adjacent block-sum formulation.**  
   Write
   \[
   s_n=a_{n+1}-a_n\in S.
   \]
   For \(i<j<k\), put
   \[
   U=\sum_{n=i}^{j-1}s_n=a_j-a_i,\qquad
   V=\sum_{n=j}^{k-1}s_n=a_k-a_j.
   \]
   Then \(a_i,a_j,a_k\) are collinear exactly when
   \[
   U\times V=0.
   \]
   Thus the question asks whether every infinite word over a finite vector alphabet \(S\subseteq\mathbb Z^3\), with distinct prefix sums, has two adjacent nonempty factors whose vector sums are parallel.

3. **Coarsely connected set formulation.**  
   A disproof is equivalent to the existence of an \(R<\infty\) and an infinite set \(X\subseteq\mathbb Z^3\) such that:
   - no affine line contains three points of \(X\);
   - the graph on \(X\) joining \(x,y\) whenever \(\|x-y\|_\infty\le R\) is connected.

   Indeed, every infinite connected locally finite graph contains a one-way infinite simple path by König’s infinity lemma.

### Ambiguity about repeated vertices

If “infinite walk” were interpreted as an infinite sequence possibly having finite image, the assertion would be ill-posed relative to the wording \(A\subseteq\mathbb Z^3\): infinitely repeated visits do not create three distinct points of the set \(A\). The natural condition is therefore that \(A\) itself is infinite.

Allowing repeated vertices but requiring infinite image does not materially change the problem. The directed graph formed by the observed transitions has finite out-degree and infinitely many reachable vertices. By applying König’s infinity lemma to its tree of finite simple directed paths, one obtains an injective \(S\)-walk whose vertices are contained in the original image.

---

## 2. What counts as a solution

### A complete proof

A complete affirmative solution must establish:

\[
\forall\, S\subseteq\mathbb Z^3\text{ finite},\quad
\forall\, (a_n)_{n\ge1}\text{ infinite-image \(S\)-walk},
\]
there exist \(i<j<k\) such that
\[
(a_j-a_i)\times(a_k-a_i)=0.
\]

The bound on \(i,j,k\), if one is produced, may depend on \(S\). No uniform bound over all finite \(S\) is required.

It is enough to prove the stronger statement that every such walk contains a nontrivial three-term arithmetic progression
\[
a_i+a_k=2a_j,
\]
but this is stronger than the actual problem: general collinear triples need not be equally spaced.

For a fixed \(S\), the following finite extremal statement is equivalent to the desired conclusion for that \(S\):

> There exists \(N(S)\) such that every injective \(S\)-walk of \(N(S)\) vertices contains three collinear points.

The equivalence follows from König’s infinity lemma applied to the finitely branching tree of all finite triple-free \(S\)-walks starting at \(0\).

### A complete disproof

A complete disproof must produce, or rigorously prove the existence of:

- one fixed finite set \(S\subseteq\mathbb Z^3\);
- an infinite sequence \((a_n)_{n\ge1}\subseteq\mathbb Z^3\);

such that:

1. \(a_{n+1}-a_n\in S\) for every \(n\);
2. the image \(\{a_n:n\ge1\}\) is infinite, preferably with the \(a_n\) pairwise distinct;
3. for every \(i<j<k\),
   \[
   (a_j-a_i)\times(a_k-a_i)\ne 0.
   \]

An explicit counterexample may be given by a formula, substitution system, finite automaton, recursive construction, or algorithm, but all three properties above must be proved for every \(n\) and every triple of indices.

A nonconstructive disproof is also logically valid. In particular, for one fixed \(S\), a rigorous proof that triple-free \(S\)-walks of arbitrary finite length exist would imply an infinite counterexample by compactness/König’s lemma.

For a computer-assisted disproof, the infinite nature of the construction needs a finite, checkable certificate: for example, a verified recursive invariant, a substitution theorem, or a finite-state mechanism whose iteration is proved to preserve injectivity and noncollinearity.

---

## 3. What does not count

The following do not resolve the problem:

1. **The planar case only.**  
   The \(\mathbb Z^2\) case is known, but the open case is genuinely rank three.

2. **A result for special step sets.**  
   Proving the assertion only for symmetric \(S\), small \(|S|\), steps of bounded coordinate size, monotone walks, or particular generating sets does not prove the universal statement.

3. **A bounded number greater than two.**  
   Constructing a walk with at most \(C\) points on every line, for some \(C\ge3\), does not give a counterexample. A counterexample requires \(C=2\).

4. **Avoiding only three-term arithmetic progressions.**  
   A walk with no solutions to
   \[
   a_i+a_k=2a_j
   \]
   may still have unequally spaced collinear triples.

5. **Long finite examples with changing step sets.**  
   Triple-free walks of arbitrary length with \(S=S_N\) depending on the length do not imply an infinite counterexample. The same fixed finite \(S\) is required. By contrast, arbitrary lengths for one fixed \(S\) would suffice by König’s lemma.

6. **Finite computational searches alone.**  
   A triple-free path of length \(10^6\), for example, gives evidence but no resolution. Exhausting all paths up to a particular length proves only a finite bound for that particular \(S\).

7. **Density or asymptotic statements alone.**  
   Showing that every positive-density set contains a collinear triple does not solve the problem because a bounded-step path can have zero density.

8. **Projected collinearity.**  
   Three points whose projections to \(\mathbb Z^2\) are collinear need not themselves be collinear in \(\mathbb Z^3\).

9. **Conditional or heuristic results.**  
   A proof assuming an unproved conjecture, a probabilistic heuristic without an existence theorem, or numerical evidence does not settle the problem unconditionally.

---

## 4. Known results and context

### 4.1 Gerver–Ramsey result in dimension two

According to the database commentary, Gerver and Ramsey conjectured the statement and proved the affirmative answer in \(\mathbb Z^2\):

> Every infinite bounded-step walk in \(\mathbb Z^2\) contains three collinear points.

Consequently, the present problem is already settled whenever the subgroup generated by the steps has rank at most two. More precisely, if
\[
H=\langle S\rangle_{\mathbb Z}\le \mathbb Z^3
\]
has rank at most \(2\), then the walk lies in the affine coset \(a_1+H\), which can be identified linearly with a lattice in \(\mathbb R^2\), and the Gerver–Ramsey theorem applies.

Thus any counterexample must use genuinely three-dimensional motion: the subgroup generated by the steps actually used must have rank \(3\).

### 4.2 Bounded collinearity in dimension three

The commentary says that Gerver and Ramsey showed in \(\mathbb Z^3\) that “the largest number of collinear points can be bounded.” Since straight-line walks have infinitely many collinear points, the only viable interpretation is existential:

> There exists an infinite bounded-step walk \(A\subseteq\mathbb Z^3\) and a finite constant \(C\) such that
> \[
> |A\cap L|\le C
> \]
> for every affine line \(L\subseteq\mathbb R^3\).

The database excerpt gives no value of \(C\), so none should be assumed. This result refutes the stronger assertion that every such walk must have arbitrarily many collinear points. The open problem is precisely whether the bound can be reduced all the way to \(2\).

### 4.3 Small step alphabets

There is a useful connection with abelian repetitions in words.

If the step word contains adjacent blocks \(U,V\) having the same multiplicity of every step symbol, then their vector sums are equal:
\[
\sum U=\sum V.
\]
For an injective walk this common sum is nonzero, and the three boundary points form a three-term arithmetic progression.

A classical theorem in combinatorics on words says that no infinite word over an alphabet of at most three letters can avoid abelian squares, while infinite abelian-square-free words exist on four letters; Keränen’s construction shows that four letters suffice and is optimal. Therefore:

> The problem has an affirmative answer whenever the walk uses at most three distinct step vectors.

This does not settle the problem because a potential counterexample may use four or more steps. Moreover, abelian-square-freeness only avoids one sufficient mechanism for collinearity; parallel block sums can occur without equal Parikh vectors.

### 4.4 Eventually periodic walks

If the step word is eventually periodic with period block \(P\), let \(d\) be the vector sum of \(P\). Injectivity forces \(d\ne0\). The endpoints of two consecutive copies of \(P\) then give
\[
x,\quad x+d,\quad x+2d,
\]
so every eventually periodic injective walk contains three collinear points. Thus any counterexample must be genuinely aperiodic.

### 4.5 Density theorems

By density versions of Szemerédi’s theorem, including the multidimensional Szemerédi theorem, any subset of \(\mathbb Z^3\) of positive upper Banach density contains a nontrivial three-term arithmetic progression. Hence a counterexample must have upper Banach density zero.

This is only a necessary condition. A one-dimensional bounded-step path in three-dimensional space may naturally have density zero.

### 4.6 Graph-theoretic compactness

For each fixed \(S\), either:

- triple-free \(S\)-walks have a finite maximum length; or
- an infinite triple-free \(S\)-walk exists.

There is no intermediate possibility. This makes fixed-\(S\) exhaustive computation conceptually meaningful, although the resulting bounds may be enormous and the original problem quantifies over every finite \(S\).

---

## 5. Traps and edge cases

1. **The three points must be distinct.**  
   Repeated indices or repeated vertices do not constitute three points of the set.

2. **The zero step.**  
   The set \(S\) may contain \(0\), but an injective walk never uses it. If revisits are allowed, zero steps do not by themselves prove the existence of three distinct collinear points.

3. **Unequal spacing.**  
   Collinearity is not equivalent to
   \[
   a_i+a_k=2a_j.
   \]
   For example, \(x,x+v,x+3v\) are collinear but not a three-term arithmetic progression in that order.

4. **Index order versus geometric order.**  
   If \(i<j<k\), the point \(a_j\) need not lie geometrically between \(a_i\) and \(a_k\). In block-sum language, the adjacent sums \(U,V\) may be negative scalar multiples, except that \(U+V=0\) would violate injectivity.

5. **Projection does not preserve the converse.**  
   Actual collinearity implies collinearity under every linear projection, but a collinear projected triple may lift to a noncollinear triple.

6. **Congruence collinearity is not exact collinearity.**  
   A cross product that vanishes modulo \(p\) need not vanish over \(\mathbb Z\). Modular calculations can filter candidates but cannot establish exact collinearity without a size bound or exact arithmetic.

7. **Pigeonholing a repeated step is insufficient.**  
   Since \(S\) is finite, some step occurs infinitely often, but the starting points of those occurrences need not lie on one line.

8. **Planar slices need not contain an infinite subwalk.**  
   A walk can pass through every fixed plane or slab only finitely many times while drifting in a third direction.

9. **Deleting repetitions naively can destroy the step condition.**  
   Taking an arbitrary injective subsequence may create unbounded jumps. The correct reduction uses a simple ray in the finite-out-degree transition graph.

10. **Algebraic no-three sets may fail the connectivity requirement.**  
    For example,
    \[
    Q=\{(x,y,x^2+y^2):x,y\in\mathbb Z\}
    \]
    contains no three collinear points: a real line intersects the positive-definite paraboloid in at most two points. But this alone is not a counterexample. One must also find an infinite bounded-step path in \(Q\), and fixed-radius adjacency on such a rapidly curved surface appears highly restrictive.

11. **Greedy extension has a global obstruction.**  
    When adding a new point, it must avoid every line determined by every pair of earlier points. Although only finitely many next steps are available, the number of old forbidden lines grows quadratically.

12. **Varying \(S\) invalidates compactness.**  
    Arbitrarily long examples only yield an infinite branch when all examples belong to the same finitely branching tree, hence use the same fixed step set.

---

## 6. Verification hooks

### 6.1 Exact incremental collinearity test

Suppose \(a_1,\dots,a_n\) are already known to contain no collinear triple, and a candidate \(q=a_n+s\) is proposed.

It suffices to test whether two previous points lie on the same line through \(q\). For each \(i\le n\):

1. Compute \(d_i=a_i-q\).
2. Let
   \[
   g_i=\gcd(|d_{i,1}|,|d_{i,2}|,|d_{i,3}|).
   \]
3. Replace \(d_i\) by the primitive vector \(d_i/g_i\).
4. Identify \(v\) and \(-v\) by choosing the sign for which the first nonzero coordinate is positive.

The candidate \(q\) creates a collinear triple exactly when the same canonical primitive direction occurs for two different earlier vertices. This gives an \(O(n)\) hash-table test per extension.

Also reject \(q\) if it is already among the previous vertices.

### 6.2 Depth-first search for a fixed \(S\)

Normalize \(a_1=0\). Recursively try
\[
a_{n+1}=a_n+s,\qquad s\in S,
\]
rejecting repeated vertices and collinear triples.

For a fixed \(S\):

- finding paths to large depths gives lower bounds on the extremal length;
- exhaustive failure at depth \(N\) proves that every \(S\)-walk of \(N\) vertices has a collinear triple;
- rigorously proving paths at every depth implies an infinite counterexample by König’s lemma.

Symmetries available for normalization include translation and invertible affine lattice transformations \(x\mapsto Ux+b\) with \(U\in\mathrm{GL}_3(\mathbb Z)\).

### 6.3 SAT/SMT formulation

For a target length \(N\), introduce step variables
\[
s_i\in S,\qquad
a_1=0,\qquad
a_{i+1}=a_i+s_i.
\]
Impose:

- \(a_i\ne a_j\) for \(i\ne j\);
- for every \(i<j<k\), at least one coordinate of
  \[
  (a_j-a_i)\times(a_k-a_i)
  \]
  is nonzero.

SMT over integers can encode this directly. A SAT implementation can use finite-domain position variables or precomputed transition tables.

### 6.4 Modular acceleration with exact certification

For finite paths, modular cross products can rapidly reject noncollinearity candidates. If all coordinates of steps are bounded by \(M\), then for a path of length \(N\), each coordinate of a difference is at most \(NM\) in absolute value, and each cross-product coordinate is at most approximately
\[
2N^2M^2.
\]
If an integer cross-product coordinate vanishes modulo primes whose product exceeds twice the relevant absolute bound, then it must vanish over \(\mathbb Z\). Direct arbitrary-precision arithmetic is simpler for final certification.

### 6.5 Testing algebraic-surface constructions

For a candidate set such as
\[
Q_f=\{(x,y,f(x,y)):x,y\in\mathbb Z\},
\]
and a radius \(R\):

1. enumerate points with \(|x|,|y|\le B\);
2. join pairs at \(\ell_\infty\)-distance at most \(R\);
3. compute connected components and their growth as \(B\) increases;
4. search for paths reaching the boundary.

This can quickly expose whether all apparent components remain bounded.

### 6.6 Testing word or substitution constructions

Given a morphic or automatic step word:

1. generate long prefixes;
2. compute all prefix sums;
3. test injectivity;
4. use the primitive-direction hash test to locate the first collinear triple;
5. classify the offending triple by the two adjacent factor sums \(U,V\).

The locations of first failures may reveal a finite family of cross-block configurations that a recursive proof would need to exclude.

### 6.7 Projection experiments

Choose several primitive vectors \(v_r\in\mathbb Z^3\) and integer linear maps
\[
\pi_r:\mathbb Z^3\to\mathbb Z^2,\qquad \ker \pi_r=\mathbb Z v_r.
\]
For finite candidate walks, record all triples collinear under each \(\pi_r\), then test whether any triple is collinear under enough independent projections to force actual collinearity. This measures whether a synchronization approach is plausible.

---

## 7. Attack routes

### Route 1: Additive combinatorics on the step word

**Core mechanism.**  
Translate geometry into adjacent block sums. For \(i<j<k\),
\[
U=a_j-a_i,\qquad V=a_k-a_j,
\]
and the triple is collinear exactly when \(U\times V=0\).

**Key lemma needed.**  
A sufficiently strong target would be:

> Every infinite word over a finite vector alphabet \(S\subseteq\mathbb Z^3\), whose prefix sums are distinct, contains two adjacent nonempty factors with nonzero parallel sums.

The special case \(U=V\) is an additive square and already yields a three-term arithmetic progression.

**Why it might work.**  
The step alphabet is finite, while block sums lie in a rank-three abelian group. Repetition theorems, factorization methods, semigroup arguments, or unavoidable-pattern results may force adjacent factors with dependent sums. The known \(|S|\le3\) result via abelian squares gives a genuine foothold.

**Most likely failure point.**  
Infinite abelian-square-free words exist over four letters, so equality of adjacent Parikh vectors cannot be forced in general. Moreover, a four-letter vector alphabet in rank three may be chosen so that simple combinatorial repetitions do not translate cleanly into equal vector sums.

**Quick blockage test.**  
For candidate rank-three step sets with four to eight vectors, search for very long words whose prefix sums are distinct and for which no adjacent factor sums are parallel. Compare maximal lengths with analogous abelian-square-free words. If standard abelian-square-free morphisms fail almost immediately through unequal but parallel sums, that is evidence the geometric condition is substantially stronger and potentially exploitable.

---

### Route 2: Synchronizing planar projection theorems

**Core mechanism.**  
Project the walk along several independent integer directions to rank-two lattices and apply the Gerver–Ramsey planar theorem.

For a primitive \(v\in\mathbb Z^3\), choose
\[
\pi_v:\mathbb Z^3\to\mathbb Z^2,\qquad \ker\pi_v=\mathbb Zv.
\]
If the projected image is finite, some fiber contains infinitely many original points, already giving infinitely many points on a line parallel to \(v\). If the projected image is infinite, the planar theorem gives a triple whose projection is collinear.

For \(u=a_j-a_i\) and \(w=a_k-a_i\), projected collinearity is equivalent to one scalar constraint of the form
\[
v\cdot(u\times w)=0.
\]

**Key lemma needed.**  
One must force the same triple \((i,j,k)\) to be projection-collinear for three linearly independent kernel vectors \(v\). Then \(u\times w\) is orthogonal to three independent vectors and hence is zero.

**Why it might work.**  
Every projection supplies many planar collinear triples, not merely one. A quantitative strengthening of the planar theorem, combined with Ramsey or hypergraph intersection arguments, might force overlap among the families of triples arising from different projections.

**Most likely failure point.**  
The planar theorem may guarantee only sparse and completely different triples for different projections. There is no immediate reason that the three triple-hypergraphs must intersect.

**Quick blockage test.**  
For long computed triple-free walks, enumerate the triples collinear under several projections. Measure their number, distribution by scale, and intersections. If each projection produces only a few highly projection-specific triples with empty pairwise intersections, naive synchronization is blocked.

---

### Route 3: Fixed-\(S\) finite extremal theory and renormalization

**Core mechanism.**  
For each fixed \(S\), use compactness to reduce the problem to proving a finite upper bound \(N(S)\). Seek an induction based on slabs, convex hulls, repeated local configurations, or coarse changes of direction.

**Key lemma needed.**  
A representative target is:

> Every sufficiently long injective \(S\)-walk either contains a collinear triple or has a long subwalk lying in a bounded-width neighborhood of a rank-two affine lattice, with bounded effective steps.

The latter case could then be reduced to a quantitative form of the planar theorem.

**Why it might work.**  
A fixed step set gives finite local complexity. Long walks must repeatedly exhibit related local displacement patterns. The full problem permits \(N(S)\) to depend arbitrarily badly on \(S\), so even a very ineffective structural induction would suffice.

**Most likely failure point.**  
A rank-three walk can drift through successive slabs while visiting each slab only briefly. Recurrent local step patterns do not imply recurrent absolute geometry, and the no-three condition is global rather than local.

**Quick blockage test.**  
Exhaustively study small generating sets such as subsets of
\[
\{-1,0,1\}^3\setminus\{0\}.
\]
Record whether extremal paths become approximately planar, helical, or directionally drifting. If very long paths repeatedly escape every bounded-width plane, a planar-renormalization lemma needs substantial strengthening.

---

### Route 4: Lift a planar walk by a bounded-increment height function — disproof route

**Core mechanism.**  
Choose a bounded-step planar walk \(b_n\in\mathbb Z^2\) and heights \(z_n\in\mathbb Z\) with
\[
z_{n+1}-z_n
\]
drawn from a fixed finite set. Set
\[
a_n=(b_n,z_n)\in\mathbb Z^3.
\]
Any collinear triple upstairs must project to a collinear triple among the \(b_n\), so only planar collinear triples need to be destroyed by the heights.

If
\[
b_i=b_0+t_i v,\quad b_j=b_0+t_jv,\quad b_k=b_0+t_kv
\]
for distinct integer parameters \(t_i,t_j,t_k\), then the lifted points are collinear exactly when
\[
(t_k-t_i)(z_j-z_i)=(t_j-t_i)(z_k-z_i).
\]

**Key lemma needed.**  
Construct a planar bounded-step walk and a bounded-increment integer height sequence avoiding all such affine constraints simultaneously.

Possible tools include the Lovász local lemma, entropy compression, symbolic dynamics, or a recursive assignment exploiting sparsity of planar collinear triples in a specially designed base walk.

**Why it might work.**  
The third coordinate provides a degree of freedom for breaking each planar collinearity. If the base path can be arranged so that each index participates in relatively few dangerous triples at each scale, a local or hierarchical avoidance argument may succeed.

**Most likely failure point.**  
The planar theorem guarantees that dangerous triples cannot be eliminated in the base. An index may belong to infinitely many constraints, and bounded height increments strongly correlate distant heights. Local-lemma dependencies are likely nonlocal and unbounded.

**Quick blockage test.**  
Fix a structured planar path and solve finite height-assignment instances with increments in \([-M,M]\). Determine whether maximal feasible length grows rapidly with \(M\), stabilizes, or fails at a small scale. Extract minimal unsatisfiable collections of collinearity constraints.

---

### Route 5: Infinite bounded-step path on a line-free quadric — disproof route

**Core mechanism.**  
Place the walk on a set that automatically contains no three collinear points. The basic example is the elliptic paraboloid
\[
Q=\{(x,y,x^2+y^2):x,y\in\mathbb Z\}.
\]
No real affine line meets this surface in three distinct points: substituting a line into \(z=x^2+y^2\) gives a quadratic with positive leading coefficient unless the horizontal direction is zero, in which case the line meets the graph at most once.

**Key lemma needed.**  
Find a line-free quadratic surface, or a suitable affine image or variant, whose integer points contain an infinite connected component under some fixed-radius adjacency relation.

**Why it might work.**  
The no-three property would be automatic and exact, leaving only a Diophantine connectivity problem.

**Most likely failure point.**  
For the standard paraboloid, a step
\[
(u,v,w)
\]
from \((x,y,x^2+y^2)\) is possible only if
\[
w=2ux+2vy+u^2+v^2.
\]
For a fixed finite step set, this confines the starting points of each step type to an affine line in the \((x,y)\)-plane. A finite union of such rigid loci may have only finite components. Positive-definite curvature appears fundamentally hostile to bounded-step escape.

**Quick blockage test.**  
For several quadratic forms \(q(x,y)\), build the fixed-radius adjacency graph on
\[
\{(x,y,q(x,y)):|x|,|y|\le B\}
\]
and test whether component diameters grow with \(B\). Symbolically classify the affine loci supporting each allowed displacement and see whether their incidence graph can support unbounded motion.

---

### Route 6: Self-similar or morphic counterexample with a finite step alphabet — disproof route

**Core mechanism.**  
Construct the step word by a substitution on at least four symbols, inspired by abelian-square-free words, and choose corresponding vectors in \(\mathbb Z^3\). Prove noncollinearity by induction over substitution scales.

**Key lemma needed.**  
A substitution and vector assignment must satisfy a scale-separation property such as:

> For any two adjacent factors with parallel vector sums, both factors lie inside a common lower-level substitution block.

Induction would then reduce every potential collinear triple to finitely many base cases.

**Why it might work.**  
The threshold of four letters for infinite abelian-square-free words matches the first step-alphabet size not already covered by the easy additive-square argument. Hierarchical words can provide strong control over repetitions and factor sums while retaining a fixed finite step set.

**Most likely failure point.**  
Four step vectors in \(\mathbb Z^3\) necessarily satisfy integer linear relations. These can create equal or parallel sums even when the corresponding words have different Parikh vectors. In addition, ordinary substitution scale separation controls symbolic boundaries, not geometric directions of vector sums.

**Quick blockage test.**  
Take known abelian-square-free substitutions, assign small rank-three integer vectors to their letters, and search vector assignments by SAT/SMT. Generate several substitution levels and classify all parallel adjacent factor sums. If every assignment produces low-level unavoidable failures, the substitution needs additional geometric structure rather than mere abelian-square avoidance.

---

## 8. Verdict on difficulty

This is a genuinely difficult, long-standing open problem dating to the Gerver–Ramsey work cited as [GeRa79]. The unresolved case is sharply concentrated:

- the walk must be genuinely rank three;
- it must use at least four distinct step vectors;
- it must be aperiodic;
- its image must have zero upper Banach density;
- known constructions can already keep the number of points on every line uniformly bounded, so no argument can rely on forcing arbitrarily large collinear subsets.

The problem sits at an intersection of discrete geometry, combinatorics on words, additive combinatorics, and infinite graph theory. Its main difficulty is that bounded-step connectivity is only a one-dimensional global condition: it gives neither density nor recurrence in any fixed region, while the prohibition of collinear triples is a global condition involving all pairs of previous vertices.

No standard equivalence with a famous conjecture such as the Erdős–Turán conjecture, the cap-set problem, or a major density conjecture is presently evident from the stated context. It should nevertheless be treated as a high-difficulty foundational problem. The Gerver–Ramsey bounded-collinearity construction is particularly important: any successful affirmative proof must isolate a specifically three-point obstruction, rather than proving that bounded-step walks necessarily create rich or arbitrarily large linear structure.