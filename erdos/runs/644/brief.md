# Problem brief: Erdős Problem #644

## 1. Precise statement

### 1.1 Hypergraph formulation

Let \(k\ge 1\) and \(r\ge 3\) be integers. A **\(k\)-uniform hypergraph** is a pair
\[
\mathcal H=(V,E),
\]
where \(V\) is an arbitrary ground set and every edge \(A\in E\) is a \(k\)-element subset of \(V\).

For a subfamily \(\mathcal F\subseteq E\), its **transversal number** or **covering number** is
\[
\tau(\mathcal F)
 =\min\bigl\{|T|:T\subseteq V,\ T\cap A\ne\varnothing
 \text{ for every }A\in\mathcal F\bigr\}.
\]
Thus a “pair \(\{x,y\}\) which intersects all of the \(A_j\)” means a set of at most two vertices meeting every selected edge. Allowing one-element transversals is standard; whether \(x\) and \(y\) must be distinct is immaterial after adjoining unused vertices.

Call \(\mathcal H\) **\(r\)-locally 2-coverable** if
\[
\tau(\mathcal F)\le 2
\qquad\text{for every }\mathcal F\subseteq E
\text{ with }1\le |\mathcal F|\le r.
\tag{\(P_r\)}
\]
Equivalently, for every \(s\le r\) and every \(A_1,\dots,A_s\in E\), there are vertices \(x,y\in V\) such that
\[
A_i\cap\{x,y\}\ne\varnothing
\qquad (1\le i\le s).
\]

Define
\[
f(k,r)=
\max\bigl\{\tau(\mathcal H):
\mathcal H\text{ is a \(k\)-uniform hypergraph satisfying }(P_r)\bigr\}.
\tag{1}
\]
The maximum is finite: property \((P_r)\), with \(r\ge3\), forbids three pairwise disjoint edges. Hence a maximal matching has at most two edges, and the union of such a matching is a transversal of size at most \(2k\). Therefore
\[
f(k,r)\le 2k.
\tag{2}
\]

This is the cleanest convention for research purposes.

### 1.2 Relation to the database wording

The database says only that “for every collection of \(r\)” edges there is a two-point transversal. If the family contains at least \(r\) distinct members, this exact-\(r\) condition implies the corresponding condition for every smaller subfamily: extend a smaller subfamily to \(r\) edges. Thus it agrees with \((P_r)\) in the intended nondegenerate setting.

Possible alternative conventions are:

1. **Exactly \(r\) distinct edges only.** Families with fewer than \(r\) edges then satisfy the hypothesis vacuously. This can change \(f(k,r)\) by a bounded \(O_r(1)\) amount but not the stated linear asymptotics.
2. **Indexed families with repetitions.** One must distinguish distinct indices from distinct sets. Repetitions do not affect the global transversal number, but they can be used to pad a smaller subfamily to \(r\) indices.
3. **Simple families with at least \(r\) edges.** This avoids both repetitions and vacuous small families.

The asymptotic questions as \(k\to\infty\), with \(r\) fixed, are intended to be insensitive to these minor conventions. Any proposed exact small-\(k\) argument should nevertheless state its convention explicitly.

### 1.3 The two questions

The first question asks whether
\[
\lim_{k\to\infty}\frac{f(k,7)}{k}=\frac34.
\tag{Q1}
\]
Equivalently, for every \(\varepsilon>0\), there is \(K(\varepsilon)\) such that for all integers \(k\ge K(\varepsilon)\),
\[
\left(\frac34-\varepsilon\right)k
\le f(k,7)\le
\left(\frac34+\varepsilon\right)k.
\]

The second question asks whether, for every fixed integer \(r\ge3\), there exists a constant \(c_r>0\) such that
\[
\lim_{k\to\infty}\frac{f(k,r)}{k}=c_r.
\tag{Q2}
\]
The \(o(1)\) and the rate of convergence may depend on the fixed value of \(r\).

The standard interpretation is that \(c_r\) is positive. If \(c_r=0\) were allowed, the notation \((1+o(1))c_rk\) would be inappropriate; the correct statement would simply be \(f(k,r)=o(k)\).

---

## 2. What counts as a solution

### 2.1 Complete proof of the \(r=7\) assertion

A complete proof of (Q1) must establish both:

1. **Universal upper bound**
   \[
   \tau(\mathcal H)\le \left(\frac34+o(1)\right)k
   \]
   for every \(k\)-uniform, \(7\)-locally 2-coverable hypergraph \(\mathcal H\), uniformly over all ground sets and all family sizes.

2. **Matching lower bound**
   \[
   f(k,7)\ge \left(\frac34-o(1)\right)k.
   \]
   This requires admissible examples \(\mathcal H_k\) for all sufficiently large \(k\), or an interpolation argument covering all sufficiently large \(k\), with
   \[
   \tau(\mathcal H_k)\ge \left(\frac34-o(1)\right)k.
   \]

A construction only for a sparse subsequence of \(k\) proves a corresponding lower bound on the limsup, not necessarily the required liminf. There is no obvious monotonicity or padding principle in \(k\), so this distinction matters.

### 2.2 Complete disproof of the \(r=7\) assertion

To disprove (Q1), one must prove the formal negation
\[
\exists\varepsilon>0\quad
\text{for infinitely many }k,\quad
\left|\frac{f(k,7)}k-\frac34\right|\ge\varepsilon.
\]

This could be done in either direction:

- **High-side disproof:** construct, for infinitely many \(k\), \(7\)-locally 2-coverable \(k\)-uniform hypergraphs satisfying
  \[
  \tau(\mathcal H_k)\ge\left(\frac34+\varepsilon\right)k.
  \]
- **Low-side disproof:** prove a universal upper bound
  \[
  f(k,7)\le\left(\frac34-\varepsilon\right)k
  \]
  for infinitely many \(k\), preferably all sufficiently large \(k\).

For an explicit finite counterexample \(\mathcal H=(V,E)\) at a particular \(k\), verification requires:

1. every edge has exactly \(k\) vertices;
2. every subfamily of at most seven edges has a transversal of size at most two;
3. every vertex set of size at most the claimed lower threshold fails to hit all edges.

One isolated finite counterexample does not disprove an asymptotic limit unless it belongs to an infinite construction with a fixed linear gap.

### 2.3 Complete proof of the general limit assertion

A proof of (Q2) must establish, with quantifiers in this order,
\[
\forall r\ge3\ \exists c_r>0\
\forall\varepsilon>0\ \exists K(r,\varepsilon)\
\forall k\ge K(r,\varepsilon):
\quad
\left|\frac{f(k,r)}k-c_r\right|<\varepsilon.
\]

It is not necessary to give a closed formula for \(c_r\), provided existence and positivity are rigorously proved.

### 2.4 Complete disproof of the general limit assertion

A disproof must produce one fixed \(r\ge3\) for which no positive limiting constant exists. Since \(0\le f(k,r)/k\le2\), this means proving either:

- \(\liminf f(k,r)/k<\limsup f(k,r)/k\); or
- under the positive-\(c_r\) interpretation, \(f(k,r)/k\to0\).

Showing that \(c_r\) differs from a guessed value does not disprove (Q2).

---

## 3. What does not count

The following would not resolve the stated problems:

- proving only
  \[
  f(k,7)\le \left(\frac34+o(1)\right)k
  \]
  without a matching lower bound;
- constructing examples with transversal number \((3/4-o(1))k\) without proving the universal upper bound;
- obtaining the lower construction only for a subsequence, absent a valid interpolation argument;
- proving merely \(f(k,7)=\Theta(k)\), \(f(k,7)\le k\), or any other linear bound with the wrong constant;
- proving the assertion only for intersecting, linear, regular, symmetric, geometric, or bounded-ground-set hypergraphs;
- proving a fractional-transversal bound without controlling the integral transversal number;
- proving the result conditionally on an unproved conjecture;
- numerical evidence for finitely many \(k\);
- probabilistic or optimization heuristics without exact verification;
- proving the limit exists for \(r=7\) without identifying it as \(3/4\): this advances (Q2) but not (Q1);
- proving (Q1) alone: it settles only the \(r=7\) instance of (Q2), not every fixed \(r\);
- showing only that \(f(k,r)/k\) has convergent subsequences, which follows automatically from boundedness.

---

## 4. Known results and context

### 4.1 Results reported by the database

Erdős, Fon-Der-Flaass, Kostochka, and Tuza [EFKT92] proved the following exact values, under the conventions of their paper:
\[
f(k,3)=2k,
\]
\[
f(k,4)=\left\lfloor\frac{3k}{2}\right\rfloor,
\]
\[
f(k,5)=\left\lfloor\frac{5k}{4}\right\rfloor,
\]
and
\[
f(k,6)=k.
\]

Consequently, the general limit question is already settled for \(3\le r\le6\), with
\[
c_3=2,\qquad
c_4=\frac32,\qquad
c_5=\frac54,\qquad
c_6=1.
\]

The first unresolved case is \(r=7\), for which the proposed value is
\[
c_7=\frac34.
\]

### 4.2 Monotonicity in \(r\)

Under the at-most-\(r\) formulation,
\[
f(k,r+1)\le f(k,r).
\tag{3}
\]
Indeed, every \((r+1)\)-locally 2-coverable family is also \(r\)-locally 2-coverable.

Thus the known \(r=6\) result gives
\[
f(k,7)\le f(k,6)=k,
\tag{4}
\]
and more generally
\[
f(k,r)\le k\qquad(r\ge6),
\tag{5}
\]
subject to the exact-value convention and range in [EFKT92].

The conjectured \(r=7\) result therefore asks for a substantial improvement from the known coefficient \(1\) to \(3/4\), together with a sharp construction.

### 4.3 Matching-number bound

If \(\mathcal H\) satisfies \((P_r)\) for any \(r\ge3\), then its matching number satisfies
\[
\nu(\mathcal H)\le2.
\]
A maximal matching therefore has one or two edges, and its union is a transversal. This proves the general bound \(f(k,r)\le2k\).

This elementary argument is sharp when \(r=3\), according to the reported value \(f(k,3)=2k\), but it loses substantial information for larger \(r\).

### 4.4 Finite reduction

Although the database uses a sequence \(A_1,A_2,\dots\), upper-bound questions can be reduced to finite hypergraphs.

For fixed \(m\), if every finite subfamily of \(\mathcal H\) has a transversal of size at most \(m\), then \(\mathcal H\) itself has such a transversal. One proof uses compactness of \(\{0,1\}^V\): the conditions “hit edge \(A\)” are clopen because \(A\) is finite, and the condition “select at most \(m\) vertices” is closed.

Thus, if \(\tau(\mathcal H)>m\), some finite subfamily already has transversal number \(>m\). Finite computation can therefore detect genuine lower-bound examples, although a bound on the size of a minimal witness would still be needed for exhaustive universal proofs.

### 4.5 Dual formulation

For each vertex \(v\in V\), define the dual block
\[
D_v=\{A\in E:v\in A\}\subseteq E.
\]
Every edge-index \(A\in E\) lies in exactly \(k\) dual blocks \(D_v\), counting distinct vertices \(v\in A\).

The local hypothesis becomes:

> Every set of at most \(r\) edge-indices is contained in the union of two dual blocks \(D_x\cup D_y\).

The conclusion seeks a cover of all edge-indices by at most \(f(k,r)\) dual blocks. This is an abstract local-to-global covering problem with the additional regularity that every point of the dual system belongs to exactly \(k\) blocks.

### 4.6 Small-\(k\) convention warning

Under the robust \((P_r)\) definition, the two singleton edges \(\{\{a\},\{b\}\}\) have transversal number \(2\) and are locally 2-coverable for every \(r\). Hence \(f(1,r)\ge2\) under that convention. This is incompatible with taking formulas such as \(f(1,6)=1\) literally.

Therefore the exact formulas quoted by the database must be read with the precise small-family or small-\(k\) conventions of [EFKT92]. This does not affect either asymptotic question, but it must not be ignored in computer checks.

---

## 5. Traps and edge cases

1. **The pair depends on the selected edges.**  
   There is no fixed global pair. Inferring a common pair from the local condition is exactly the sort of invalid Helly-type leap the problem resists.

2. **“The pair intersects every edge” does not mean both vertices lie in every edge.**  
   For each selected edge \(A_i\), it is enough that \(x\in A_i\) or \(y\in A_i\).

3. **Pairwise intersection is not the hypothesis.**  
   A selected family may contain two disjoint edges; one witness point can lie in each.

4. **Exactly \(r\) versus at most \(r\).**  
   The equivalence requires enough distinct members to extend smaller subfamilies. Small or repeated families need separate treatment.

5. **No automatic monotonicity in \(k\).**  
   Padding every edge by common vertices introduces a global common point, while padding by private vertices need not increase the transversal number. Lower constructions on a subsequence cannot be interpolated without proof.

6. **A maximal matching gives only \(2k\).**  
   The fact that the union of two disjoint edges is a transversal does not imply it contains a nearly optimal transversal.

7. **Witnesses may lie outside a chosen matching core.**  
   If \(B,C\) are disjoint edges and \(U=B\cup C\), every edge meets \(U\), but a two-point witness for seven edges may use vertices outside \(U\). Passing to traces \(A\cap U\) need not preserve local 2-coverability.

8. **Fractional and integral transversals differ.**  
   A strong bound on \(\tau^*(\mathcal H)\) does not resolve the problem unless the relevant integrality gap is controlled to \(o(k)\).

9. **Minimum versus inclusion-minimal transversals.**  
   If \(T\) is inclusion-minimal, every \(x\in T\) has a private edge \(E_x\) with \(E_x\cap T=\{x\}\). This assertion is false for an arbitrary transversal.

10. **One finite example cannot refute an asymptotic limit.**

11. **Ground-set size is unrestricted.**  
    A proof cannot assume \(|V|=O(k)\) without a reduction. For a finite family one may replace \(V\) by the union of its edges, but that union may be large.

12. **Floors are irrelevant asymptotically but critical in exact checks.**

13. **Restricted classes may be misleading.**  
    Symmetric or linear examples can miss extremal configurations whose vertices have highly nonuniform incidence patterns.

---

## 6. Verification hooks

### 6.1 Checking the local condition directly

For a finite family \(E=\{A_1,\dots,A_m\}\), enumerate every subfamily
\[
\mathcal F=\{A_{i_1},\dots,A_{i_s}\},
\qquad 3\le s\le r.
\]
It has a two-point transversal if and only if there exist \(x,y\) in
\[
A_{i_1}\cup\cdots\cup A_{i_s}
\]
such that
\[
A_{i_j}\cap\{x,y\}\ne\varnothing
\qquad(1\le j\le s).
\]
This can be tested in \(O((sk)^2s)\) time per subfamily by enumerating pairs.

An equivalent test is: there exists a vertex \(x\) such that the intersection of all selected edges not containing \(x\) is nonempty. If every selected edge contains \(x\), then \(x\) alone is a transversal.

A machine-checkable certificate of admissibility can list one witness pair for every subfamily of size at most \(r\).

### 6.2 Computing the transversal number

For fixed \(\mathcal H=(V,E)\), solve the integer program
\[
\min \sum_{v\in V}x_v
\]
subject to
\[
\sum_{v\in A}x_v\ge1\qquad(A\in E),
\]
\[
x_v\in\{0,1\}\qquad(v\in V).
\]

To certify \(\tau(\mathcal H)>t\), it is enough to verify:
\[
\forall T\subseteq V,\quad |T|=t,\quad
\exists A\in E\text{ with }A\cap T=\varnothing.
\tag{6}
\]
For small \(n=|V|\), this can be checked exhaustively. A certificate may give, for every \(t\)-set \(T\), one edge disjoint from \(T\).

### 6.3 Searching over all \(k\)-sets on a fixed ground set

Fix \(V=[n]\). Introduce a binary variable \(z_A\) for each \(A\in\binom{V}{k}\), with \(z_A=1\) meaning that \(A\) belongs to the family.

For every bad subfamily \(\{A_1,\dots,A_s\}\), \(3\le s\le r\), having no two-point transversal, impose
\[
z_{A_1}+\cdots+z_{A_s}\le s-1.
\tag{7}
\]

To force transversal number at least \(t+1\), impose, for every \(T\in\binom{V}{t}\),
\[
\sum_{\substack{A\in\binom{V}{k}\\A\cap T=\varnothing}}z_A\ge1.
\tag{8}
\]

Feasibility of (7)–(8) produces an exact lower-bound example on \(n\) vertices.

### 6.4 Incidence-mask testing

For a selected \(s\)-tuple of edges, associate to each vertex \(v\) its incidence mask
\[
M_v=\{i\in[s]:v\in A_i\}.
\]
The tuple is two-point coverable exactly when
\[
M_x\cup M_y=[s]
\]
for some two masks realized by vertices. This representation is convenient for canonicalization and isomorphism reduction.

### 6.5 Testing structural conjectures

For each generated admissible hypergraph, record:

- \(\tau(\mathcal H)\) and fractional \(\tau^*(\mathcal H)\);
- matching number;
- minimum and maximum vertex degrees;
- the traces on the union of a maximal matching;
- private-edge incidence patterns relative to each minimum transversal;
- whether the family is intersecting or has two disjoint edges.

This can quickly refute proposed structural lemmas that are stronger than the actual conjecture.

### 6.6 Limits of computation

Searching all families on \(n\) vertices proves only a bounded-\(n\) result. It becomes a universal proof only after establishing a kernel theorem bounding the ground-set size or the number of edges of a minimal counterexample in terms of \(k,r,\tau\).

---

## 7. Attack routes

### Route 1: Minimum transversals and private-edge incidence

**Core mechanism.**  
Let \(T\) be a minimum transversal, \(|T|=t\). For every \(x\in T\), choose a private edge
\[
E_x\cap T=\{x\}.
\]
Apply the seven-edge local condition to collections of private edges.

**Key lemma needed.**  
A plausible target is a charging or set-pairs inequality of the form
\[
4|T|\le 3k+o(k)
\]
for every \(7\)-locally 2-coverable \(k\)-uniform family of private edges. This would give the desired upper bound.

One may seek to derive it using Bollobás-type set-pairs inequalities, skew set-pair inequalities, or a classification of how external vertices can simultaneously cover many private edges.

**Why it might work.**  
Private edges encode every indispensable point of a minimum transversal. Seven distinct private edges cannot be covered by two points of \(T\), since each meets \(T\) in a different singleton. Thus the local witnesses must create strong common-incidence patterns outside \(T\).

**Likely failure point.**  
A small collection of high-degree external vertices may cover many private edges in highly nonuniform ways, and the witness pair can change completely between seven-tuples. Standard set-pairs inequalities may be too coarse to recover the coefficient \(3/4\).

**Quick blocking test.**  
Use ILP/SAT to search, for small \(k\), for incidence systems consisting only of private edges with
\[
|T|>\left\lceil\frac{3k}{4}\right\rceil
\]
that nevertheless satisfy the seven-edge condition. Record the external incidence masks to test candidate charging rules.

---

### Route 2: Reduction to the union of a maximal matching

**Core mechanism.**  
Choose a maximal matching. If it consists of two disjoint edges \(B,C\), let
\[
U=B\cup C,\qquad |U|=2k.
\]
Every edge meets \(U\), so the trace family
\[
\{A\cap U:A\in E\}
\]
has a transversal in a \(2k\)-element ground set.

If the matching has size one, one \(k\)-edge already hits all edges, giving \(\tau\le k\); the seven-local condition must then be used to improve \(k\) to roughly \(3k/4\).

**Key lemma needed.**  
A kernel or compression theorem that preserves enough two-point witness information while replacing all external vertices by \(O(k)\) incidence types, followed by an extremal theorem giving a transversal of size at most \((3/4+o(1))k\).

**Why it might work.**  
The matching-number bound supplies a natural finite core of size at most \(2k\). The desired transversal is only a fixed proportion of this core, suggesting an extremal trace theorem or a compression argument.

**Likely failure point.**  
The trace family itself need not be seven-locally 2-coverable: a witness pair for seven original edges may use external vertices. Naively deleting the external part destroys the essential hypothesis.

**Quick blocking test.**  
Generate small admissible examples and explicitly compare:
\[
\tau(\mathcal H),\qquad
\tau(\{A\cap U\}),\qquad
\text{and local 2-coverability of the trace family}.
\]
Any proposed trace-preserving reduction should first survive these examples.

---

### Route 3: Fractional transversals plus asymptotically lossless rounding

**Core mechanism.**  
Study the fractional transversal LP
\[
\tau^*(\mathcal H)=
\min\left\{\sum_{v}w_v:
w_v\ge0,\ 
\sum_{v\in A}w_v\ge1\ \forall A\in E\right\}
\]
and its dual fractional matching.

**Key lemma needed.**  
Two separate assertions are required:

1. a local-to-global fractional estimate
   \[
   \tau^*(\mathcal H)\le\left(\frac34+o(1)\right)k;
   \]
2. an integrality statement specific to seven-local 2-coverability,
   \[
   \tau(\mathcal H)\le\tau^*(\mathcal H)+o(k).
   \]

**Why it might work.**  
The condition that every seven edges are covered by two vertices is a strong constraint on feasible fractional matchings. Averaging over seven-edge samples may force concentration around a few vertices, and concentration could support efficient deterministic rounding.

**Likely failure point.**  
For arbitrary hypergraphs, set-cover integrality gaps are large. Even matching number at most two does not by itself guarantee an additive \(o(k)\) gap. The local property must be used in an essential way in both LP steps.

**Quick blocking test.**  
Compute \(\tau\) and \(\tau^*\) for all small admissible examples found by SAT. If examples already exhibit a linear integrality gap, this route cannot yield the sharp constant without substantial additional structure.

---

### Route 4: Dual local-cover theorem

**Core mechanism.**  
Work with the dual blocks
\[
D_v=\{A:v\in A\}.
\]
Every edge-index belongs to exactly \(k\) dual blocks, every seven edge-indices lie in the union of two blocks, and the objective is to cover all indices with few blocks.

**Key lemma needed.**  
A theorem of the following general shape:

> In a set system in which every point lies in exactly \(k\) blocks and every seven points are covered by two blocks, the whole point set is covered by at most \((3/4+o(1))k\) blocks.

Potential tools include shifting, extremal incidence-matrix arguments, fractional Helly methods, Ramsey-type canonicalization, or entropy inequalities.

**Why it might work.**  
The local hypothesis becomes a direct covering condition on seven points, while \(k\)-uniformity becomes exact point-regularity in the dual. This may expose the constants \(2,3/2,5/4,1,3/4\) more transparently than the primal language.

**Likely failure point.**  
The dual system has no a priori bound on VC dimension, block size, or number of blocks. General local-cover theorems may be false without using exact point-regularity very sharply.

**Quick blocking test.**  
Search directly over binary incidence matrices with column sum \(k\), impose that every seven columns are covered by two rows, and maximize the minimum number of rows covering all columns. This avoids committing to a primal geometric intuition.

---

### Route 5: Approximate subadditivity and existence of \(c_r\)

**Core mechanism.**  
Attack the second question independently by seeking a Fekete-type argument. An estimate such as
\[
f(k+\ell,r)\le f(k,r)+f(\ell,r)+o(k+\ell)
\tag{9}
\]
with uniform error would imply existence of a normalized limit under suitable hypotheses. A complementary scaling or interpolation lemma would establish positivity and control all \(k\).

**Key lemma needed.**  
A decomposition theorem partitioning every \((k+\ell)\)-edge into \(k\)- and \(\ell\)-parts in a way that transfers the local two-point-cover condition to one or both induced systems, up to a controlled error.

Alternatively, one could seek an asymptotic finite-template theorem showing that extremal examples are approximated by weighted incidence structures whose optimum scales linearly.

**Why it might work.**  
The exact formulas for \(3\le r\le6\) are consistent with linear behavior plus bounded rounding errors. If a bounded-defect subadditivity principle exists, the general existence of \(c_r\) may follow without determining it.

**Likely failure point.**  
There is no evident natural product, sum, or blow-up operation:

- splitting each edge need not preserve local coverability in either part;
- disjoint unions can require more than two local witnesses;
- cloning vertices increases edge size without proportionally increasing the transversal number.

This lack of scaling is likely the central difficulty in (Q2).

**Quick blocking test.**  
Compute exact small values where feasible and test candidate inequalities such as
\[
f(k+\ell,r)\le f(k,r)+f(\ell,r)+C_r.
\]
Separately test proposed hypergraph products on known extremal examples for \(r=3,\dots,6\); a valid general mechanism should reproduce their linear scaling.

---

### Route 6: Disproof by symmetric or algebraic constructions

**Core mechanism.**  
Search for an infinite family of highly structured hypergraphs—cyclic, design-based, finite-geometric, or algebraic—with
\[
\tau(\mathcal H_k)\ge\left(\frac34+\delta\right)k
\]
while every seven edges are covered by two vertices.

A practical starting point is a cyclic family on \(\mathbb Z_n\), with edges obtained as translates of one or several \(k\)-subsets.

**Key lemma needed.**  
A parametric construction for infinitely many \(k\), together with proofs of:

1. seven-local 2-coverability;
2. the required linear lower bound on the transversal number.

For the general-limit question, one would need substantially more: constructions and upper bounds producing distinct liminf and limsup values for one fixed \(r\).

**Why it might work.**  
The conjectured constant may be inferred from a restricted class of known constructions rather than from a universal theorem. A new design with a larger covering ratio would immediately refute the \(3/4\) prediction on the high side.

**Likely failure point.**  
The local condition is extremely restrictive. Random or generic design families are likely to contain seven edges whose incidence masks cannot be covered by two vertices. Symmetry can also lower the transversal number unexpectedly.

**Quick blocking test.**  
Run SAT/ILP searches for \(k\le 8\) or \(10\), imposing cyclic symmetry when desired, and maximize \(\tau/k\). Any candidate should be checked by exhaustive seven-subfamily enumeration and exact transversal ILP. Inspect whether the best examples stabilize into a recognizable parametric pattern.

---

## 8. Verdict on difficulty

This is a serious long-standing extremal set-system problem originating in work from 1992. The exact transition
\[
2,\ \frac32,\ \frac54,\ 1,\ \boxed{\frac34?}
\]
for \(r=3,4,5,6,7\) suggests sharp and delicate structure rather than a routine averaging argument.

The \(r=7\) problem has two difficult and logically independent components:

- proving a universal improvement from the known coefficient \(1\) to \(3/4\);
- constructing matching examples with transversal number asymptotic to \(3k/4\).

The general existence-of-limits question is potentially harder still. Standard subadditivity and blow-up mechanisms do not obviously apply because neither edge size nor transversal number behaves well under natural hypergraph products.

No equivalence to a famous conjecture is supplied by the database, and none should be asserted without evidence. Nevertheless, the age of the problem, the exact low-\(r\) results, and the failure of obvious scaling operations indicate high difficulty. A realistic research program should first reconstruct the mechanisms behind the EFKT92 proofs for \(r=4,5,6\), identify which structural lemma changes at \(r=7\), and use exact computation primarily to test candidate structural statements rather than to infer the asymptotic answer directly.