# Problem brief: Erdős Problem #734

## 1. Precise statement

Let
\[
[n]=\{1,2,\dots,n\}.
\]

A **pairwise balanced block design** (PBD) on \([n]\) is a finite indexed family
\[
\mathcal A=(A_1,\dots,A_m),\qquad A_i\subseteq[n],
\]
such that:

1. every block has at least two points,
   \[
   |A_i|\ge 2;
   \]
2. every unordered pair of distinct points lies in exactly one block:
   \[
   \forall\,\{x,y\}\in\binom{[n]}2,\qquad
   \left|\{i\in[m]:\{x,y\}\subseteq A_i\}\right|=1.
   \]

Equivalently, the complete graph \(K_n\) is decomposed into edge-disjoint complete subgraphs \(K_{|A_i|}\), one on each vertex set \(A_i\).

The design is **nontrivial** in the standard sense that it does not consist of the single block \([n]\). Equivalently, under the convention \(|A_i|\ge2\), every block is proper:
\[
2\le |A_i|\le n-1.
\]
Indeed, if one block equals \([n]\), the pair condition forbids every other block of size at least \(2\).

For each integer \(t\), define the block-size multiplicity
\[
b_t(\mathcal A)=\left|\{i\in[m]:|A_i|=t\}\right|.
\]
Under the above convention, \(b_t=0\) unless \(2\le t\le n-1\).

### Formal problem

Prove that there exist absolute constants \(C>0\) and \(N\in\mathbb N\) such that, for every integer \(n\ge N\), there is a nontrivial PBD \(\mathcal A\) on \([n]\) satisfying
\[
\max_{2\le t\le n-1} b_t(\mathcal A)\le C\sqrt n.
\]

The implied \(O(\sqrt n)\)-constant must be uniform in both \(n\) and \(t\).

### Ambiguities and standard conventions

- “Find” is read as “prove existence”; an explicit deterministic construction would be stronger but is not required.
- Some definitions permit blocks of size \(0\) or \(1\). Such blocks cover no pair and can simply be omitted. They should not be counted as meaningful blocks.
- A literal reading allowing the \(O\)-constant to depend on \(t\) would be much weaker and is almost certainly not intended. The database commentary about the matching \(\Omega(\sqrt n)\) obstruction indicates the uniform reading above.
- The final sentence of the supplied commentary contains a typographical error: it should say that for some \(t\) there are \(\gg\sqrt n\) many **indices \(i\)** with \(|A_i|=t\), not “many \(t\).”

---

## 2. What counts as a solution

### Complete proof

A complete affirmative solution must establish all of the following:

1. There are fixed constants \(C,N\), independent of \(n\).
2. For every integer \(n\ge N\), not merely for a subsequence or congruence class, a nontrivial PBD on exactly \(n\) points exists.
3. Every pair of points occurs in exactly one block.
4. No block is the whole point set.
5. For every block size \(t\),
   \[
   b_t\le C\sqrt n.
   \]

A probabilistic proof is acceptable if it rigorously proves positive probability of all required properties simultaneously. A recursive proof must control the constant uniformly through all recursive levels and all rounding cases.

A finite claimed design can be verified by checking
\[
\sum_{i=1}^m \binom{|A_i|}{2}=\binom n2
\]
and, more importantly, checking directly that each pair occurs exactly once. The numerical identity alone is not sufficient.

### Complete disproof

Define
\[
f(n)=\min_{\mathcal A}\max_t b_t(\mathcal A),
\]
where the minimum ranges over all nontrivial PBDs on \([n]\). This set is nonempty for \(n\ge3\), since the family of all \(2\)-element subsets is a nontrivial PBD.

The conjectured statement is equivalent to
\[
f(n)=O(\sqrt n).
\]

Its logical negation is
\[
\forall C>0\;\forall N\;\exists n\ge N
\quad\text{such that}\quad
f(n)>C\sqrt n.
\]
Equivalently,
\[
\limsup_{n\to\infty}\frac{f(n)}{\sqrt n}=\infty.
\]

Thus a disproof must produce an unbounded sequence \(n_j\) and prove that **every** nontrivial PBD on \(n_j\) points has
\[
\max_t b_t\ge g_j\sqrt{n_j},
\qquad g_j\to\infty.
\]

Exhibiting a poorly behaved design does not disprove the problem. Nor does one exceptional value of \(n\), since the assertion concerns all sufficiently large \(n\).

---

## 3. What does not count

The following would not resolve the problem:

- A construction only when \(n\) is a prime power, a square, or lies in selected congruence classes.
- A construction for infinitely many \(n\), even a density-one set of \(n\), without handling every sufficiently large integer.
- A bound such as
  \[
  b_t=O(n^{1/2}\log n),\qquad
  O(n^{1/2+\varepsilon}),\quad\text{or}\quad o(n).
  \]
- A bound on the average of the \(b_t\), rather than on their maximum.
- A construction with one exceptional block size occurring \(\Theta(n)\) times.
- An approximate decomposition covering all but \(o(n^2)\) pairs.
- A packing in which each pair occurs at most once but some pairs remain uncovered.
- A \(\lambda\)-design in which every pair occurs \(\lambda>1\) times.
- A fractional clique decomposition.
- A conditional argument relying on unproved existence of projective planes or other designs for all relevant orders.
- A histogram \((b_t)\) satisfying the pair-count equation without an actual realization by blocks.
- Merely proving the already-known lower bound
  \[
  \max_t b_t=\Omega(\sqrt n).
  \]
- A construction whose hidden constant depends on \(n\) or on the varying size \(t\).

---

## 4. Known results and context

### 4.1 Basic identities

For every PBD,
\[
\sum_{t=2}^{n-1} b_t\binom t2=\binom n2,
\tag{1}
\]
because each block accounts for all pairs inside it, and every pair is accounted for exactly once.

For each point \(x\), let
\[
r_x=\left|\{i:x\in A_i\}\right|.
\]
Then
\[
\sum_{i:x\in A_i}(|A_i|-1)=n-1.
\tag{2}
\]
This follows because the blocks through \(x\) partition the other \(n-1\) points according to which block contains the pair \(\{x,y\}\).

Two distinct blocks intersect in at most one point:
\[
i\ne j\implies |A_i\cap A_j|\le1.
\tag{3}
\]

### 4.2 De Bruijn–Erdős theorem

The de Bruijn–Erdős theorem for finite linear spaces states that a nontrivial PBD on \(n\) points has at least \(n\) blocks:
\[
m\ge n.
\tag{4}
\]

In incidence-matrix language, if \(N\) is the \(n\times m\) point-block incidence matrix, then
\[
NN^{\mathsf T}=J+\operatorname{diag}(r_x-1),
\]
because distinct points occur together in exactly one block. In a nontrivial PBD, every \(r_x\ge2\), so this matrix is positive definite and has rank \(n\); hence \(m\ge n\).

The equality case is also classified: if \(m=n\), the design is either

- a projective plane, in which all \(n\) blocks have the same size; or
- a near-pencil, with one block of size \(n-1\) and \(n-1\) blocks of size \(2\).

Neither equality case satisfies the desired \(O(\sqrt n)\) multiplicity bound for large \(n\). Thus a successful construction must have \(m>n\).

### 4.3 The unavoidable \(\Omega(\sqrt n)\) lower bound

Let
\[
M=\max_t b_t.
\]
Order the block sizes as
\[
k_1\le k_2\le\cdots\le k_m.
\]
Because each integer size can occur at most \(M\) times,
\[
k_j\ge 2+\left\lfloor\frac{j-1}{M}\right\rfloor.
\]
Using \(m\ge n\) and the pair identity,
\[
\binom n2
=\sum_{j=1}^m\binom{k_j}{2}
\ge
\sum_{j=1}^n
\binom{2+\lfloor(j-1)/M\rfloor}{2}.
\tag{5}
\]

If \(L=\lfloor n/M\rfloor\), the right side is at least
\[
M\sum_{r=0}^{L-1}\binom{r+2}{2}
=
M\binom{L+2}{3}.
\]
Asymptotically this is
\[
\frac{n^3}{6M^2}(1+o(1)).
\]
Comparison with \(\binom n2\sim n^2/2\) gives
\[
M\ge \left(\frac1{\sqrt3}-o(1)\right)\sqrt n.
\tag{6}
\]

Thus the exponent \(1/2\) in the problem is optimal. The problem asks for a construction matching the unavoidable order of magnitude.

The database commentary compresses this argument: de Bruijn–Erdős supplies \(m\ge n\), but equation (1) is also needed to derive the \(\Omega(\sqrt n)\) repetition.

### 4.4 Wilson’s PBD existence theorem

Wilson’s existence theorem says, roughly, that for a fixed set \(K\) of allowed block sizes, the natural divisibility conditions are eventually sufficient for a PBD with block sizes in \(K\). If
\[
\alpha(K)=\gcd\{k-1:k\in K\},\qquad
\beta(K)=\gcd\{k(k-1):k\in K\},
\]
the necessary conditions are
\[
\alpha(K)\mid n-1,\qquad
\beta(K)\mid n(n-1),
\]
and for fixed \(K\) these are sufficient for all sufficiently large \(n\).

This does not solve the present problem. If \(K\) is fixed and \(m\ge n\), some size occurs at least \(n/|K|\) times. Any solution needs \(\Omega(\sqrt n)\) distinct block sizes, so the allowed sizes must grow with \(n\), outside the direct fixed-\(K\) regime.

Wilson’s fundamental construction and group-divisible designs remain potentially relevant as recursive tools.

### 4.5 Why standard finite geometries do not work

A projective plane of order \(q\) has
\[
n=q^2+q+1
\]
points and the same number of lines, all of size \(q+1\). Hence one size occurs \(n\) times.

An affine plane of order \(q\) has \(q^2\) points and \(q(q+1)\) lines, all of size \(q\). Again the multiplicity is \(\Theta(n)\).

Even restricting a projective plane to a dense subset of its points is obstructed by exact moment identities. Let \(S\) be a subset of \(s\) points in a projective plane of order \(q\), let \(v=q^2+q+1\), and let
\[
h_t=\left|\{L:|L\cap S|=t\}\right|.
\]
Then
\[
\sum_t h_t=v,\qquad
\sum_t t h_t=s(q+1),\qquad
\sum_t \binom t2h_t=\binom s2.
\tag{7}
\]
If \(T=|L\cap S|\) for a uniformly random line, then
\[
\operatorname{Var}(T)
=
q\frac{s}{v}\left(1-\frac{s}{v}\right).
\tag{8}
\]
For \(s=\alpha v\), with \(\alpha\) bounded away from \(0\) and \(1\), almost all line intersections lie in an interval of width \(O(\sqrt q)\). Since there are \(\Theta(q^2)\) lines, some intersection size occurs \(\Omega(q^{3/2})\) times. But \(\sqrt s=\Theta(q)\). Therefore simple dense restriction of a projective plane cannot solve the problem.

---

## 5. Traps and edge cases

1. **The one-block design is forbidden.**  
   The family \(\{[n]\}\) would otherwise satisfy the multiplicity condition trivially.

2. **Singletons are irrelevant but dangerous in counting arguments.**  
   They cover no pair and can be added arbitrarily. Work only with blocks of size at least \(2\).

3. **Repeated blocks of size at least \(2\) are impossible.**  
   Repeating such a block would cover each of its pairs more than once.

4. **The \(O(\sqrt n)\) constant is uniform.**  
   Constants depending on \(t\) or \(n\) do not establish the intended statement.

5. **The pair-count identity is necessary, not sufficient.**  
   A sequence \((b_t)\) satisfying
   \[
   \sum_t b_t\binom t2=\binom n2
   \]
   need not be geometrically realizable by pairwise-intersecting-at-most-once blocks.

6. **Disjoint union does not work.**  
   Taking PBDs on disjoint point sets leaves every cross-pair uncovered.

7. **Deleting points preserves pair uniqueness but can cause severe concentration.**  
   Restricting all old blocks to a point subset and discarding intersections of size below \(2\) gives a PBD, but finite-plane restrictions have the variance obstruction above.

8. **Refining blocks is exact but can create massive repetition.**  
   Replacing a block \(B\) by a PBD on \(B\) preserves the global pair condition, but repeating the same ingredient on many parent blocks usually creates far too many blocks of the same sizes.

9. **A large block severely constrains all other blocks.**  
   If \(B,C\) are distinct blocks, then
   \[
   |B|+|C|\le n+1.
   \]
   Also, if \(x\notin B\), then for every \(y\in B\) the block containing \(\{x,y\}\) is distinct, so exactly \(|B|\) blocks through \(x\) meet \(B\).

10. **The all-edge design is not useful.**  
    Taking every \(2\)-set as a block gives \(b_2=\binom n2\).

11. **The endpoint \(m=n\) is already classified and fails.**  
    Any approach that accidentally produces exactly \(n\) blocks can only give a projective plane or near-pencil.

12. **“All large \(n\)” requires robust rounding.**  
    Constructions based on \(n=q^2\), \(q^2+q+1\), or factorization \(n=ab\) need a method for arbitrary nearby integers without creating a repeated cleanup size.

13. **Full cyclic symmetry is fatal for prime \(n\).**  
    On \(\mathbb Z_p\), every proper nonempty block has a translation orbit of length \(p\). Thus any translation-invariant design contains \(p\) blocks of one size, too many for \(O(\sqrt p)\).

---

## 6. Verification hooks

### 6.1 Direct certificate checker

Given \(n\) and blocks represented as bitsets:

1. Check \(2\le |A_i|\le n-1\).
2. Initialize an \(n\times n\) upper-triangular pair counter.
3. For each block \(A_i\), increment the counter for every pair in \(\binom{A_i}{2}\).
4. Verify every pair counter equals \(1\).
5. Compute the histogram \(b_t\) and its maximum.

The work is
\[
O\!\left(\sum_i |A_i|^2+n^2\right).
\]

### 6.2 Histogram feasibility ILP

For fixed \(n\) and proposed cap \(M\), search for integers \(b_t\ge0\) satisfying
\[
b_t\le M,
\]
\[
\sum_{t=2}^{n-1}\binom t2b_t=\binom n2,
\]
\[
\sum_{t=2}^{n-1}b_t\ge n.
\]

Infeasibility proves that cap \(M\) is impossible. Feasibility only supplies a candidate histogram, not a design.

### 6.3 Local-incidence strengthening

Introduce integers
\[
a_{x,t}=\#\{\text{blocks of size }t\text{ containing }x\}.
\]
Necessary conditions include
\[
\sum_t (t-1)a_{x,t}=n-1
\quad\text{for every }x,
\]
and
\[
\sum_x a_{x,t}=t\,b_t.
\]
These constraints can eliminate many numerically feasible histograms before full exact-cover search.

### 6.4 Exact-cover/SAT formulation for small \(n\)

For every proper subset \(S\subset[n]\) with \(|S|\ge2\), introduce a binary variable \(x_S\). Impose
\[
\sum_{S\supseteq\{u,v\}}x_S=1
\quad\text{for every pair }\{u,v\},
\]
and
\[
\sum_{|S|=t}x_S\le M
\quad\text{for every }t.
\]
Minimize \(M\).

This has exponentially many variables, but is practical for small \(n\) using symmetry breaking, column generation, or CP-SAT. It directly computes \(f(n)\) for accessible orders.

### 6.5 Random-greedy diagnostics

For a proposed list of block sizes \(k_1,\dots,k_m\), repeatedly choose a random \(k_i\)-set whose internal pairs are still uncovered. Track:

- uncovered degree at each vertex;
- pair codegrees in the residual graph;
- the pointwise deficit in equation (2);
- whether the residual graph admits a plausible absorber.

A systematic late-stage failure indicates that the chosen size profile is incompatible with exact completion, even if the global pair equation holds.

### 6.6 Finite-geometry moment checks

For any construction obtained by restricting a projective plane, compute the histogram \(h_t\) and verify all three identities in (7). Equation (8) gives an immediate quantitative concentration test and can rule out whole families of candidate subsets without constructing the resulting blocks explicitly.

---

## 7. Attack routes

### Route 1: Prescribed large-clique decomposition via nibble and absorption

**Core idea.**  
Choose a list
\[
k_1,\dots,k_m
\]
with all or most \(k_i\) of order \(\sqrt n\), with every integer used at most \(C\sqrt n\) times, and with
\[
\sum_i\binom{k_i}{2}=\binom n2.
\]
Then seek an exact decomposition
\[
K_n=K_{k_1}\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}K_{k_m}.
\]

A plausible profile uses \(\Theta(n)\) blocks, \(\Theta(\sqrt n)\) different sizes, and \(\Theta(\sqrt n)\) copies of each size.

**Key lemma needed.**  
An exact decomposition theorem for \(K_n\) into a prescribed multiset of cliques of orders \(\Theta(\sqrt n)\), under appropriate global and local feasibility conditions.

**Why it might work.**  
The target scale is numerically natural: \(\Theta(n)\) blocks, each covering \(\Theta(n)\) pairs, account for \(\Theta(n^2)\) pairs. Random-greedy packing could cover almost all pairs, followed by a tailored absorber.

**Likely failure point.**  
Existing exact decomposition machinery is strongest for fixed clique order. Here the clique orders grow like \(\sqrt n\), precisely where codegrees and absorption structures become difficult. A numerically valid list may also fail pointwise degree partition conditions.

**Quick blockage test.**

1. Solve the histogram and local-incidence ILPs for moderate \(n\).
2. Run random greedy packing for the resulting size lists.
3. Measure whether residual degrees remain pseudorandom or develop large structured deficits.
4. Attempt completion with a bounded library of clique trades.

---

### Route 2: Exact-one-agreement codes and mixed orthogonal arrays

**Core idea.**  
Construct maps
\[
f_j:[n]\to\Sigma_j,\qquad j=1,\dots,r,
\]
such that any two distinct points \(x,y\) agree in exactly one coordinate:
\[
\left|\{j:f_j(x)=f_j(y)\}\right|=1.
\]
For each \(j\) and symbol \(a\), take the non-singleton fiber
\[
\{x:f_j(x)=a\}
\]
as a block. These fibers form a resolvable PBD.

Affine planes arise from a highly uniform version of this construction. The objective is to use mixed alphabets or nonlinear coordinate maps whose fiber sizes are widely dispersed.

**Key lemma needed.**  
For every sufficiently large \(n\), construct an exact-one-agreement code whose fiber-size histogram satisfies
\[
\max_t\#\{(j,a):|f_j^{-1}(a)|=t\}=O(\sqrt n).
\]

**Why it might work.**  
The pair condition is encoded globally and exactly. Mixed-level orthogonal arrays, quasigroups, finite-field maps, and code concatenation provide substantial algebraic structure.

**Likely failure point.**  
Near-extremal exact-one-agreement codes may be rigid and force approximately uniform fiber sizes, reproducing the projective- or affine-plane concentration. Deleting codewords preserves exact-one agreement but, as the moment calculation shows, dense deletion from a projective plane remains too concentrated.

**Quick blockage test.**

- Use SAT to search for small exact-one-agreement arrays with optimized fiber histogram.
- Compare the resulting profiles with affine-plane restrictions.
- Compute second moments of fiber sizes; if an identity forces variance \(O(\sqrt n)\) around one mean size, the route is blocked in that subclass.

---

### Route 3: Recursive block refinement and Wilson’s fundamental construction

**Core idea.**  
Start with a master PBD or group-divisible design. Assign weights to master points, replace each master block by a suitable ingredient GDD, and fill the groups recursively. Alternatively, replace selected blocks \(B\) by nontrivial PBDs on \(B\).

This gives exact pair coverage automatically if all ingredients are valid.

**Key lemma needed.**  
A **frequency-dispersing composition lemma**: ingredients can be chosen so that their block-size count vectors do not align, and the aggregate multiplicity at every final size remains \(O(\sqrt n)\), uniformly over recursive depth and rounding.

**Why it might work.**  
Wilson-type constructions are specifically designed to handle arbitrary sufficiently large orders and congruence corrections. Different ingredients could deliberately shift their block-size spectra so repeated parent blocks do not create repeated child sizes.

**Likely failure point.**  
Standard ingredients use a small fixed set of block sizes. If the same ingredient is inserted into \(\Theta(n)\) parent blocks, one child size immediately appears \(\Theta(n)\) times. Cleanup groups can likewise create a dominant size, often size \(2\).

**Quick blockage test.**

- Represent every ingredient by its block-size count vector.
- Simulate the recursive convolution of these vectors.
- Formulate the choice of ingredients as an ILP minimizing the largest final coordinate.
- If every available ingredient library forces one coordinate to grow linearly, substantially new GDD ingredients are required.

---

### Route 4: Difference families and partial group symmetry

**Core idea.**  
Use a group \(G\) of order \(n\), choose base blocks, and develop them under selected translations. Pair coverage then becomes a difference-covering condition. Subgroups or large stabilizers could reduce orbit lengths to \(O(\sqrt n)\).

**Key lemma needed.**  
For every large \(n\), construct a difference family in which:

- every nonzero difference is represented exactly once in the appropriate sense;
- every developed block orbit has length \(O(\sqrt n)\);
- the total number of blocks of any one cardinality is \(O(\sqrt n)\).

**Why it might work.**  
Difference methods turn pair coverage into explicit algebraic equations and often produce exact designs rather than approximate packings. If \(n\) has a factor near \(\sqrt n\), subgroup orbits have the desired scale.

**Likely failure point.**  
Prime orders are a fundamental obstruction to full translation symmetry. For \(G=\mathbb Z_p\), every proper nonempty block has orbit length \(p\), already too large. Thus a successful group-based method must either break symmetry, use only local group actions, or include a separate construction for prime-like orders.

**Quick blockage test.**

- Prove orbit-size lower bounds for the proposed symmetry group.
- For composite \(n\), run exact-cover searches on group differences.
- Check whether every candidate necessarily includes a full orbit longer than \(C\sqrt n\).
- Test first on \(n=q^2\), then on semiprimes with highly unequal factors, and finally on primes.

---

### Route 5: Disproof through stability and forced concentration

**Core idea.**  
Try to prove that finite linear-space constraints force much more repetition than the histogram lower bound detects. The equality case \(m=n\) is completely rigid; perhaps designs with \(m=O(n)\) are quantitatively close to projective planes or near-pencils and therefore still have a highly repeated size.

Use:

- the incidence identity
  \[
  NN^{\mathsf T}=J+\operatorname{diag}(r_x-1);
  \]
- local equations (2);
- intersection constraints;
- inequalities linking block sizes and point replications;
- possible stability versions of de Bruijn–Erdős.

**Key lemma needed.**  
For an unbounded sequence \(n_j\), every nontrivial PBD on \(n_j\) points must satisfy
\[
\max_t b_t\ge g_j\sqrt{n_j}
\]
with \(g_j\to\infty\).

A merely improved constant in front of \(\sqrt n\) would not disprove the problem.

**Why it might work.**  
The desired designs would be finite linear spaces with an unusually flat line-size spectrum. Known extremal linear spaces are highly regular or near-pencil-like, both of which have extreme concentration.

**Likely failure point.**  
The de Bruijn–Erdős equality classification may have no sufficiently strong stability extension. Highly irregular designs with \(m\) moderately larger than \(n\) may evade all rank and convexity arguments. Global histogram inequalities alone already permit the target scale.

**Quick blockage test.**

- Compute \(f(n)\) exactly for the largest feasible small \(n\).
- Compare primes, prime powers, and composite orders.
- Optimize over the histogram and local-incidence relaxations.
- Use semidefinite constraints derived from incidence matrices.
- If the relaxed optimum remains \(O(\sqrt n)\) with no arithmetic dependence, a disproof will require genuinely geometric, not merely numerical, constraints.

---

## 8. Verdict on difficulty

This is a sharp, exact existence problem. The exponent \(1/2\) is forced by elementary counting together with the de Bruijn–Erdős theorem, so there is no asymptotic slack: a solution must attain the information-theoretically optimal order.

The principal difficulties are:

- exact coverage of every pair;
- block orders growing with \(n\), outside the easiest fixed-parameter design-existence theorems;
- the need for \(\Theta(\sqrt n)\) distinct block sizes;
- uniform control for every sufficiently large integer \(n\);
- severe concentration in all standard finite-geometric constructions;
- multiplicity blowup under naive recursion or symmetry.

The problem is not known to be equivalent to a famous conjecture such as the projective-plane existence problem, and no such equivalence should be asserted. Nevertheless, it appears substantially harder than Erdős’s remark that it “probably will not be very difficult” suggests. Standard projective planes, affine planes, fixed-\(K\) PBD existence, cyclic difference families, and naive block refinement all fail for identifiable structural reasons.

A credible solution will likely require either:

1. a new exact clique-decomposition theorem for a carefully chosen, growing multiset of clique orders; or
2. a novel recursive/algebraic construction specifically designed to flatten the entire block-size spectrum.

The supplied database status is open, and the order of magnitude sought is already known to be best possible.