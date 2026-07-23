# Erdős Problem #885: Common factor-difference sets

## 1. Precise statement

For a positive integer \(n\), define
\[
D(n):=\{\,|a-b|:a,b\in \mathbb Z_{>0},\ ab=n\,\}\subseteq \mathbb Z_{\ge 0}.
\]

Since interchanging \(a\) and \(b\) does not change \(|a-b|\), one may equivalently restrict to factor pairs \(a\le b\):
\[
D(n)=\left\{\frac{n}{a}-a:a\mid n,\ 1\le a\le \sqrt n\right\}.
\]

The problem asks whether the following assertion holds:

> For every integer \(k\ge 1\), there exist pairwise distinct positive integers
> \[
> N_1<N_2<\cdots<N_k
> \]
> such that
> \[
> \left|\bigcap_{i=1}^{k}D(N_i)\right|\ge k.
> \]

Equivalently, for every \(k\ge1\), there should exist distinct nonnegative integers
\[
0\le d_1<d_2<\cdots<d_k
\]
and distinct positive integers \(N_1,\dots,N_k\) such that
\[
d_j\in D(N_i)\qquad(1\le i,j\le k).
\]

Thus the problem asks whether the bipartite incidence relation
\[
d\sim N\quad\Longleftrightarrow\quad d\in D(N)
\]
contains a copy of \(K_{k,k}\) for every \(k\).

### Exact square reformulation

For \(N\ge1\) and \(d\ge0\),
\[
d\in D(N)
\]
if and only if there exists \(m\ge1\) such that
\[
N=m(m+d).
\]
Equivalently,
\[
4N+d^2=(2m+d)^2.
\]
Hence
\[
d\in D(N)
\quad\Longleftrightarrow\quad
4N+d^2 \text{ is a perfect square}.
\]

Indeed, if \(x^2=4N+d^2\), then \(x>d\), and \(x\equiv d\pmod 2\) follows automatically from \(x^2\equiv d^2\pmod4\). Therefore
\[
a=\frac{x-d}{2},\qquad b=\frac{x+d}{2}
\]
are positive integers with \(ab=N\) and \(b-a=d\).

The problem is therefore equivalent to constructing, for every \(k\), integers
\[
N_1<\cdots<N_k,\qquad 0\le d_1<\cdots<d_k,
\]
and positive integers \(x_{ij}\) satisfying
\[
x_{ij}^2=4N_i+d_j^2\qquad(1\le i,j\le k).
\]

Writing \(t_i=4N_i\) and \(s_j=d_j^2\), this is a \(k\times k\) array of squares
\[
x_{ij}^2=t_i+s_j,
\]
where the \(t_i\) are distinct positive multiples of \(4\) and the \(s_j\) are distinct integer squares.

### Conventions and ambiguity

- The standard reading uses positive integral factor pairs \(a,b\). Allowing negative integral factors does not change \(D(n)\), since the negative pair \((-a,-b)\) gives the same absolute difference.
- Rational factors must not be allowed; that would define a different and generally infinite set.
- The value \(0\) is allowed: \(0\in D(n)\) exactly when \(n\) is a square.
- The intersection is over \(i=1,\dots,k\).

Define \(P(k)\) to be the assertion above. Then
\[
P(k+1)\Longrightarrow P(k),
\]
because one may retain any \(k\) rows and any \(k\) common differences. Consequently, proving \(P(k)\) for arbitrarily large \(k\)—even only for an unbounded subsequence of \(k\)—would prove the full conjecture.

---

## 2. What counts as a solution

### Complete affirmative solution

A complete proof must establish \(P(k)\) for every positive integer \(k\). It may do so in any of the following ways:

1. Give explicit formulas or an algorithm producing suitable \(N_i,d_j\) for every \(k\), with a proof that:
   - all \(N_i\) are positive and pairwise distinct;
   - all \(d_j\) are nonnegative and pairwise distinct;
   - every \(4N_i+d_j^2\) is an integer square.

2. Prove nonconstructively that such integers exist for every \(k\).

3. Construct solutions for an unbounded sequence \(k_1<k_2<\cdots\), since monotonicity then yields every smaller \(k\).

4. Construct rational data
   \[
   T_i>0,\quad E_j\ge0,\quad X_{ij}\in\mathbb Q,
   \qquad X_{ij}^2=T_i+E_j^2,
   \]
   with the \(T_i\) and \(E_j\) distinct, for arbitrarily large sizes. A common scaling converts this into an integral solution: choose \(L\) so that
   \[
   N_i=L^2T_i,\qquad d_j=2LE_j,\qquad x_{ij}=2LX_{ij}
   \]
   are integers. Then \(x_{ij}^2=4N_i+d_j^2\).

Any computer-assisted proof must include certified exact arithmetic and a rigorous proof of termination or of all asserted search bounds.

### Complete disproof

A complete disproof must exhibit an explicit integer \(k_0\ge1\) and prove
\[
\left|\bigcap_{i=1}^{k_0}D(N_i)\right|<k_0
\]
for every choice of pairwise distinct positive integers \(N_1,\dots,N_{k_0}\).

Equivalently, it must prove that no nondegenerate \(k_0\times k_0\) integer square grid
\[
x_{ij}^2=4N_i+d_j^2
\]
exists with distinct positive \(N_i\) and distinct nonnegative \(d_j\).

There is no ordinary “counterexample tuple” here: a tuple with too small an intersection merely fails to be a witness. A counterexample to the universal assertion is an explicit value \(k_0\) together with a global impossibility proof. A finite exhaustive computation would count only if accompanied by a theorem reducing all possible solutions to the finitely searched region.

---

## 3. What does not count

The following do not resolve the problem:

- Reproving only the cases \(k\le4\), or proving any other fixed finite range.
- Producing \(r\) integers with only \(o(r)\), \(cr\) for \(c<1\), or otherwise fewer than \(r\) common differences.
- Producing arbitrarily many common differences for a fixed number of \(N_i\); both sides of the biclique must become arbitrarily large.
- Showing that “most” choices of \(N_i\) or \(d_j\) fail.
- Dimension counts, probabilistic heuristics, numerical searches, or observed patterns without a proof.
- Conditional constructions depending on unproved conjectures.
- Proving existence only over \(\mathbb R\), over finite fields, or \(p\)-adically without an unconditional passage to rational or integral points.
- Finding rational points without checking positivity, distinctness, and the denominator-clearing step.
- A bounded search finding no \(k=5\) example.
- Invoking Faltings’ theorem merely to show that a fixed high-genus curve has finitely many rational points. The problem requires only finitely many points on each specially chosen curve, and the curve itself may vary.
- Using a construction with repeated \(N_i\) or repeated \(d_j\). Distinctness is essential.

By contrast, proving the assertion for infinitely many \(k\) does count, because an infinite subset of the positive integers is unbounded and \(P(k)\) is downward monotone.

---

## 4. Known results and context

According to the supplied database commentary:

- \(k=1\) is trivial, for example \(N_1=1\), with \(D(1)=\{0\}\).
- Erdős and Rosenfeld [ErRo97] proved \(P(2)\).
- Jiménez-Urroz [Ji99] proved \(P(3)\).
- Bremner [Br19] proved \(P(4)\), using elliptic-curve methods.
- The general assertion remains open.

A small explicit \(k=2\) example is
\[
N_1=25,\qquad N_2=81,
\]
because
\[
D(25)=\{0,24\},
\]
while \(0,24\in D(81)\), from \(81=9\cdot9=3\cdot27\). Thus
\[
\{0,24\}\subseteq D(25)\cap D(81).
\]

The supplied record does not state that every individual case \(k\ge5\) is unknown, only that the general assertion is open and that the listed progression reaches \(k=4\). A current research effort should check the post-2019 literature, especially work citing Bremner.

### Size of an individual factor-difference set

Let \(\tau(n)\) be the number of positive divisors of \(n\). Different unordered factor pairs give different differences: for fixed \(d\), the equation
\[
a(a+d)=n
\]
has at most one positive solution \(a\). Therefore
\[
|D(n)|=
\begin{cases}
\tau(n)/2,&n\text{ nonsquare},\\[2mm]
(\tau(n)+1)/2,&n\text{ square}.
\end{cases}
\]
Equivalently,
\[
|D(n)|=\left\lceil\frac{\tau(n)}2\right\rceil.
\]

Thus every row in a \(k\times k\) solution must satisfy
\[
\tau(N_i)\ge
\begin{cases}
2k,&N_i\text{ nonsquare},\\
2k-1,&N_i\text{ square}.
\end{cases}
\]
This is necessary but far from sufficient.

### Exact finiteness for two fixed differences

Fix \(0\le d_1<d_2\), and put
\[
C=d_2^2-d_1^2>0.
\]
If both \(d_1,d_2\in D(N)\), write
\[
x_r^2=4N+d_r^2\qquad(r=1,2).
\]
Then
\[
x_2^2-x_1^2=C,
\]
so
\[
(x_2-x_1)(x_2+x_1)=C.
\]

Hence all such \(N\) can be enumerated from factor pairs
\[
uv=C,\qquad u<v,\qquad u\equiv v\pmod2,
\]
by setting
\[
x_1=\frac{v-u}{2},\qquad x_2=\frac{v+u}{2},\qquad
N=\frac{x_1^2-d_1^2}{4},
\]
and retaining only positive integral \(N\) with \(x_1\equiv d_1\pmod2\).

In particular, any fixed pair of differences has only finitely many common \(N\). A \(k\)-row construction must therefore choose \(d_1,d_2\) so that \(d_2^2-d_1^2\) has at least \(k\) admissible factor pairs.

### Rational curves associated with fixed columns

For fixed \(d_1<\cdots<d_r\), take \(X=x_{i1}\). The other entries in a row satisfy
\[
Y_j^2=X^2+d_j^2-d_1^2,\qquad 2\le j\le r.
\]
Over \(\mathbb Q\), this defines a multiquadratic curve. When the branch points are distinct, its smooth projective model has genus
\[
g=1+2^{r-2}(r-3).
\]
Thus:

- \(r=2\): genus \(0\);
- \(r=3\): genus \(1\);
- \(r=4\): genus \(5\);
- the genus then grows rapidly.

This helps explain why elliptic curves appear in small cases and why naive extension becomes difficult. It does not imply impossibility for larger \(r\), because the shifts \(d_j\) are themselves free parameters and only finitely many rational points are required.

### Pythagorean specialization

If \(0\) is one common difference, then every \(N_i\) is a square, say
\[
N_i=r_i^2.
\]
If all other common differences are even, \(d_j=2e_j\), then
\[
4r_i^2+(2e_j)^2=(2h_{ij})^2
\]
is equivalent to
\[
r_i^2+e_j^2=h_{ij}^2.
\]

Thus a sufficient specialization is the existence of arbitrarily large complete bipartite subgraphs in the graph whose vertices are positive integers and where \(r\) is adjacent to \(e\) when \(r^2+e^2\) is a square.

### Relation to arithmetic progressions of squares

Fermat’s theorem that there are no four distinct integer squares in a nonconstant arithmetic progression blocks some tempting ansätze:

- Four \(N_i\) in arithmetic progression are impossible in any solution, because for each fixed \(d_j\), the values \(4N_i+d_j^2\) would be four distinct squares in arithmetic progression.
- Likewise, four values \(d_j^2\) cannot form a nonconstant arithmetic progression.

This is only an obstruction to particular structured constructions, not to the general problem.

---

## 5. Traps and edge cases

1. **The value \(d=0\).**  
   It is valid and occurs exactly for square \(N\). Excluding it changes the problem.

2. **Parity in the square reformulation.**  
   Checking only that \(4N+d^2\) is a square is sufficient; the parity needed to reconstruct the factors follows automatically. One must still have \(x>d\), which follows from \(N>0\).

3. **Factor-pair duplication.**  
   The pairs \((a,b)\) and \((b,a)\) give the same element. Enumerate only \(a\le\sqrt N\).

4. **No multiplicities.**  
   \(D(N)\) is a set, not a multiset. Fortunately, different unordered factor pairs cannot produce the same difference.

5. **Distinctness on both sides.**  
   Repeated \(N_i\) or repeated \(d_j\) do not count. The strict ordering of the \(N_i\) can be imposed after proving they are distinct.

6. **Parity classes of \(N\).**
   - If \(N\) is odd, every factor pair consists of odd numbers, so every \(d\in D(N)\) is even.
   - If \(N\equiv2\pmod4\), every \(d\in D(N)\) is odd.
   - If a common intersection contains both an odd and an even difference, then every \(N_i\) must be divisible by \(4\).

7. **Uniform scaling is valid but does not enlarge the grid.**  
   If \(d\in D(N)\), then
   \[
   qd\in D(q^2N)
   \]
   for every positive integer \(q\). Scaling produces new examples of the same size, not larger ones. Scaling different rows by unrelated factors generally destroys common differences.

8. **The equation \(x^2-y^2=C\) is not a Pell equation.**  
   For fixed integer \(C\), it factors as \((x-y)(x+y)=C\) and has only finitely many integer solutions. Pell-type intuition can be misleading here.

9. **High genus is not a disproof.**  
   Faltings gives finiteness for each fixed curve of genus \(>1\), not a uniform bound as the curve varies, and the problem asks for only \(k\) points.

10. **Dimension counts are heuristic.**  
    The variety
    \[
    x_{ij}^2=4N_i+d_j^2
    \]
    has many variables, but positive expected dimension does not imply rational points, let alone integral points satisfying inequalities and distinctness.

11. **Arithmetic-progression ansätze.**  
    Any construction placing four \(N_i\) in arithmetic progression is immediately impossible by Fermat’s four-squares theorem.

12. **Finite modular searches.**  
    Distinct integers may coincide modulo every fixed small prime. Imposing modular distinctness can incorrectly discard genuine integral candidates.

---

## 6. Verification hooks

### A. Direct candidate verifier

Given proposed lists \(N_1,\dots,N_k\) and \(d_1,\dots,d_k\):

1. Check \(N_i>0\) and pairwise distinct.
2. Check \(d_j\ge0\) and pairwise distinct.
3. For every \(i,j\), compute
   \[
   q_{ij}=4N_i+d_j^2.
   \]
4. Let \(x_{ij}=\lfloor\sqrt{q_{ij}}\rfloor\) using exact integer square root.
5. Accept exactly when \(x_{ij}^2=q_{ij}\) for all \(i,j\).

Optional factor witnesses are
\[
a_{ij}=\frac{x_{ij}-d_j}{2},\qquad
b_{ij}=\frac{x_{ij}+d_j}{2}.
\]

### B. Direct computation of \(D(n)\)

Enumerate divisors \(a\mid n\) with \(a\le\sqrt n\), and insert
\[
d=\frac na-a.
\]
This gives \(D(n)\) without duplication. Check
\[
|D(n)|=\left\lceil\frac{\tau(n)}2\right\rceil
\]
as a consistency test.

### C. Bounded biclique search

For a bound \(B\):

1. Compute \(D(n)\) for all \(1\le n\le B\).
2. Build the bipartite graph with left vertices \(n\) and right vertices \(d\).
3. Search for \(K_{k,k}\) using bitset intersections or frequent-itemset/biclique-mining algorithms.

This can find examples but cannot establish nonexistence without a global bound.

### D. Pair-first exact enumeration

For bounds \(d_1<d_2\le D_{\max}\):

1. Factor
   \[
   C=d_2^2-d_1^2.
   \]
2. Enumerate factor pairs \(uv=C\) with \(u<v\) and \(u\equiv v\pmod2\).
3. Form
   \[
   x_1=\frac{v-u}{2},\qquad N=\frac{x_1^2-d_1^2}{4}.
   \]
4. Retain positive integral \(N\) for which \(4N+d_r^2\) is square for \(r=1,2\).
5. For the resulting finite candidate pool, compute all \(D(N)\) and search for a subset of \(k\) rows with at least \(k\) common differences.

For fixed \(d_1,d_2\), this enumeration is complete.

### E. Pythagorean specialization search

Generate primitive and imprimitive Pythagorean triples
\[
r^2+e^2=h^2.
\]
Build a graph with an edge \(r\sim e\), and search for \(K_{k,k-1}\). Such a biclique yields
\[
N_i=r_i^2,\qquad d_1=0,\qquad d_j=2e_j.
\]

### F. Algebraic-geometry checks

For proposed rational column parameters \(d_1,\dots,d_r\):

1. Construct the curve
   \[
   Y_j^2=X^2+d_j^2-d_1^2.
   \]
2. Check smoothness and compute its genus.
3. Search for automorphisms and low-genus quotients.
4. Compute Jacobian decompositions, Mordell–Weil ranks of elliptic factors, and rational-point lifts using SageMath or Magma.
5. Verify every lifted point directly in the original equations; quotient points need not lift.

### G. Modular sieves

For candidate numerical parameters, reject a pair \((N,d)\) if
\[
4N+d^2
\]
is a nonsquare modulo some small prime. Bitmasks of quadratic residues make this fast. Such sieves are useful for search but not by themselves for global impossibility.

---

## 7. Attack routes

### Route 1: Parametric rational square grids and induction

**Core mechanism.** Work over \(\mathbb Q\) with
\[
X_{ij}^2=T_i+E_j^2,
\]
then clear denominators. Seek a recursive construction that extends a specially structured \(r\times r\) grid to an \((r+1)\times(r+1)\) grid.

**Key lemma needed.** A nondegenerate extension or amplification lemma, for example:

> For every \(r\), there is a positive-dimensional rational family of \(r\times r\) solutions containing a specialization that extends to size \(r+1\).

A weaker lemma constructing solutions for an unbounded sequence of sizes would suffice.

**Why it might work.** The full variety has expected dimension \(2r\), and the established small cases show substantial arithmetic flexibility. Rational constructions avoid divisibility restrictions, since denominators can be cleared at the end.

**Likely failure point.** Adding a new row and column imposes many simultaneous square conditions. Generic fibers quickly become high-genus curves or intersections of quadrics with few rational points. An extension may exist only on a thin exceptional locus that becomes empty.

**Quick test.** For \(r=5\), impose low-degree polynomial or rational-function ansätze on \(T_i,E_j,X_{ij}\). Compute the coefficient ideal, its dimension, and its saturated components. Test whether any component avoids the diagonals
\[
T_i=T_{i'},\qquad E_j=E_{j'}.
\]

---

### Route 2: Engineer many rows from one highly composite difference of squares

**Core mechanism.** Begin with two columns \(d_1<d_2\). Every common row is generated by a factor pair of
\[
C=d_2^2-d_1^2.
\]
Choose \(C\) with many admissible factor pairs, producing a large candidate set of \(N\), and then search for additional common differences across a selected subset.

**Key lemma needed.** Construct, for arbitrarily large \(k\), integers \(d_1<d_2\) and at least \(k\) admissible factor pairs of \(C\) whose associated \(N_i\) have at least \(k-2\) further common factor differences.

**Why it might work.** The first two columns are completely controlled by divisor theory. Highly composite numbers provide arbitrarily many candidate rows, turning the remaining problem into a finite structured incidence problem rather than an unbounded search over \(N\).

**Likely failure point.** For random candidate rows, further intersections of their \(D(N)\) are extremely sparse. A large divisor count for \(C\) alone may give no alignment beyond the initial two differences.

**Quick test.** Enumerate values
\[
C=d_2^2-d_1^2
\]
with unusually large \(\tau(C)\), generate all candidate rows exactly, and compute the maximum biclique contained in their factor-difference incidence matrix. Compare highly composite \(C\), squares \(C=d_2^2\), and products with prescribed parity patterns.

---

### Route 3: Force \(d=0\) and construct Pythagorean bicliques

**Core mechanism.** Set one common difference equal to \(0\), forcing
\[
N_i=r_i^2.
\]
Choose the other differences to be \(2e_j\). The problem reduces to
\[
r_i^2+e_j^2=h_{ij}^2.
\]

**Key lemma needed.** For every \(k\), there exist distinct positive integers \(r_1,\dots,r_k\) and distinct positive integers \(e_1,\dots,e_{k-1}\) such that every pair \((r_i,e_j)\) is the pair of legs of an integer right triangle.

Rational \(r_i,e_j\) are enough, since a common scaling makes them integral.

**Why it might work.** Pythagorean triples admit strong rational parametrizations and composition laws. The specialization automatically handles one column and all row distinctness via distinct square \(N_i\).

**Likely failure point.** Simultaneously requiring many prescribed pairs to be Pythagorean is closely analogous to difficult rational-box and simultaneous-conic problems. The complete bipartite condition may be much more rigid than the abundance of individual Pythagorean triples suggests.

**Quick test.** Generate a large graph of Pythagorean-leg compatibility, mine maximal bicliques, and inspect whether successful examples arise from common parametrized families. On the rational side, fix several \(r_i\) and compute the genus/rank of the curve parametrizing common \(e\).

---

### Route 4: Special high-genus curves with elliptic quotients

**Core mechanism.** Fix columns \(d_1,\dots,d_r\) and study
\[
Y_j^2=X^2+d_j^2-d_1^2.
\]
Search for special choices of the \(d_j\) for which this multiquadratic curve has exceptional automorphisms, decomposable Jacobian, or maps to elliptic curves of positive rank.

**Key lemma needed.** For arbitrarily large \(r\), choose distinct rational \(d_j\) so that the associated curve has at least \(r\) rational points yielding distinct positive values
\[
N=\frac{X^2-d_1^2}{4}.
\]

A particularly useful mechanism would be an elliptic quotient whose rational points lift through all remaining double covers along an infinite or sufficiently large explicit subset.

**Why it might work.** Bremner’s \(k=4\) result already indicates that elliptic-curve arithmetic can overcome the raw system of square conditions. Multiquadratic curves often have several natural involutions and correspondingly decomposable Jacobians.

**Likely failure point.** Positive rank on a quotient does not imply that infinitely many quotient points lift to the original curve. For \(r\ge4\), the full curve has high genus, and the simultaneous lifting conditions can be thin or finite.

**Quick test.** For structured choices such as geometric, reciprocal, or norm-generated \(d_j\), compute the automorphism group and Jacobian decomposition. For each elliptic quotient, perform descent and exact lifting tests. Abort a family quickly if every rational quotient point fails one fixed covering condition.

---

### Route 5: Split-norm composition and biclique amplification

**Core mechanism.** Use the identity
\[
(x^2-d^2)(y^2-e^2)
=(xy+de)^2-(xe+dy)^2.
\]
This is multiplication of norms in the split quadratic algebra \(\mathbb Q[\varepsilon]/(\varepsilon^2-1)\).

Since every edge has the form
\[
x_{ij}^2-d_j^2=4N_i,
\]
one can try to compose two existing arrays to produce a much larger one.

**Key lemma needed.** A composition law that takes configurations of sizes \(r\) and \(s\) to a configuration of size tending to infinity—ideally \(rs\)—while ensuring that the new “imaginary parts” depend only on the column index and the new norms depend only on the row index.

**Why it might work.** Norm identities are one of the few mechanisms that systematically preserve “square minus square” structure. An amplification law would immediately turn the known small configurations into unbounded ones.

**Likely failure point.** Under naive multiplication,
\[
d' = xe+dy
\]
depends on both the old row variable \(x\) and the old column variable \(d\), so column-independence is lost. Distinctness and positivity can also collapse.

**Quick test.** Symbolically compose two \(2\times2\) configurations. Determine whether any choice of signs, row scalings, or separable normalizations makes the resulting difference factor as a function of column indices alone. If the required separability forces all rows or columns equal, the naive norm route is blocked.

---

### Route 6: Disproof through rigidity or a maximal-size theorem

**Core mechanism.** Search for a structural theorem showing that sufficiently large additive square matrices
\[
x_{ij}^2=t_i+s_j,\qquad s_j=d_j^2,
\]
must be degenerate. Every \(2\times2\) subarray satisfies
\[
x_{ij}^2+x_{i'j'}^2=x_{ij'}^2+x_{i'j}^2,
\]
so the matrix of entrywise squares has additive rank at most \(2\).

**Key lemma needed.** For some explicit \(k_0\), prove that every rational or integral \(k_0\times k_0\) solution of these rectangle identities with square column offsets has either:
- repeated \(t_i\);
- repeated \(d_j\);
- a nonpositive \(t_i\); or
- a parity/integrality obstruction.

That would disprove \(P(k_0)\).

**Why it might work.** The genus grows rapidly with the number of columns, and classical rigidity such as the impossibility of four squares in arithmetic progression shows that square arrays can obey unexpectedly strong global restrictions.

**Likely failure point.** The shifts \(t_i,s_j\) vary with \(k\), divisor counts are unbounded, and high-genus finiteness for fixed parameters does not imply a uniform maximal grid size. The moduli spaces may contain exceptional positive-dimensional components for every \(k\).

**Quick test.** For \(k=5\), compute elimination ideals for the rational square-grid variety, saturated by all row and column difference products. Search for forced algebraic degeneracies or low-degree identities. Finite-field experiments can identify likely components, but modular nonexistence claims must allow that distinct integers may coincide modulo the chosen prime.

---

## 8. Verdict on difficulty

This is a genuinely difficult open Diophantine construction problem. The progression
\[
k=2,\quad k=3,\quad k=4
\]
culminating in an elliptic-curve argument is strong evidence that the first unresolved case is already arithmetically substantial. For fixed columns, the associated rational curve moves from genus \(0\) to genus \(1\) and then to genus \(5\), with exponentially growing genus thereafter. At the same time, the columns themselves are variable, so standard finiteness theorems do not settle the problem.

No equivalence to a single famous conjecture is presently evident from the supplied information. In particular:

- Faltings’ theorem does not resolve it.
- Fermat’s theorem on four squares in arithmetic progression only rules out narrow ansätze.
- A general local-to-global principle is unavailable.
- A positive-dimensional ambient variety does not guarantee rational solutions.

The most credible affirmative strategies are either an unexpected composition/amplification identity or a highly structured family of curves with controllable rational points. A disproof would require a new uniform rigidity theorem, substantially stronger than the usual fixed-curve finiteness results. The problem should be treated as high difficulty, with \(k=5\) as the essential experimental and theoretical test case.