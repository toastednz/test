# Research Brief: Erdős Problem #477

## 1. Precise statement

### 1.1 Primary formulation

Let \(f\in \mathbb Q[x]\) be an **integer-valued polynomial**, meaning
\[
f(n)\in \mathbb Z\qquad\text{for every }n\in\mathbb Z,
\]
and suppose
\[
\deg f\ge 2.
\]
Define its value set
\[
C_f:=f(\mathbb Z)=\{f(k):k\in\mathbb Z\}\subseteq\mathbb Z.
\]

The problem asks whether there exist such an \(f\) and a set \(A\subseteq\mathbb Z\) for which
\[
\forall n\in\mathbb Z,\quad \exists!\,(a,c)\in A\times C_f
\quad\text{such that}\quad n=a+c.
\]

Equivalently, does there exist \(f\) of degree at least \(2\) such that
\[
\mathbb Z=A\oplus C_f,
\]
where \(\oplus\) denotes a direct sum of subsets: every integer has exactly one representation as a sum of one element from each summand?

### 1.2 Coefficient convention

The notation “a polynomial \(f:\mathbb Z\to\mathbb Z\)” naturally allows integer-valued polynomials in \(\mathbb Q[x]\), such as
\[
f(x)=\binom{x}{2}=\frac{x(x-1)}2.
\]
Some sources may instead intend the narrower condition \(f\in\mathbb Z[x]\). A final solution should explicitly state which convention it handles.

- A negative proof for all integer-valued \(f\in\mathbb Q[x]\) settles both readings.
- An affirmative example with \(f\in\mathbb Z[x]\) also settles both readings.
- An affirmative example requiring nonintegral rational coefficients settles the literal integer-valued reading, but may not settle an intended \(\mathbb Z[x]\) version.

An integer-valued polynomial can be represented uniquely as
\[
f(x)=\sum_{j=0}^d u_j\binom{x}{j},\qquad u_j\in\mathbb Z.
\]

### 1.3 Uniqueness is by values, not by parameters

The pair being counted is
\[
(a,c)\in A\times C_f,
\]
not \((a,k)\in A\times\mathbb Z\). Thus, if \(f(k)=f(\ell)\) with \(k\ne \ell\), these do **not** constitute two representations. Multiplicities in the parametrization \(k\mapsto f(k)\) are discarded.

### 1.4 Difference-set formulation

For subsets \(X,Y\subseteq\mathbb Z\), write
\[
X-Y:=\{x-y:x\in X,\ y\in Y\}.
\]

Then
\[
\mathbb Z=A\oplus C_f
\]
is equivalent to the conjunction
\[
A+C_f=\mathbb Z
\]
and
\[
(A-A)\cap(C_f-C_f)=\{0\}.
\]

Indeed, a collision
\[
a+c=a'+c'
\]
is equivalent to
\[
a-a'=c'-c.
\]
A nonzero common difference therefore produces two distinct representations, and conversely.

---

## 2. What counts as a solution

The formal problem is existential.

### 2.1 Complete affirmative solution

A complete affirmative solution must provide:

1. A specific polynomial \(f\) with \(\deg f\ge 2\).
2. A proof that \(f(\mathbb Z)\subseteq\mathbb Z\).
3. A precisely defined set \(A\subseteq\mathbb Z\).
4. A proof of coverage:
   \[
   A+f(\mathbb Z)=\mathbb Z.
   \]
5. A proof of uniqueness:
   \[
   (A-A)\cap(f(\mathbb Z)-f(\mathbb Z))=\{0\}.
   \]

An algorithmic or recursive definition of \(A\) is acceptable only if it is proved to be well-defined and the coverage and uniqueness assertions are proved for every integer. Arbitrarily extensive finite computation does not replace the global proof.

Such an example is also a counterexample to the Erdős–Graham expectation that the answer should be negative.

### 2.2 Complete negative solution

A complete negative solution must prove
\[
\forall f\quad
\Bigl[
f(\mathbb Z)\subseteq\mathbb Z,\ \deg f\ge2
\implies
\forall A\subseteq\mathbb Z,\ 
\mathbb Z\ne A\oplus f(\mathbb Z)
\Bigr].
\]

For every admissible \(f\) and every \(A\), it must show either:

- **failure of coverage:** some \(n\in\mathbb Z\) is not in \(A+f(\mathbb Z)\); or
- **failure of uniqueness:** there exist distinct pairs
  \[
  (a,c)\ne(a',c')\in A\times f(\mathbb Z)
  \]
  with
  \[
  a+c=a'+c'.
  \]

In difference language, once coverage is assumed, it is enough to exhibit a nonzero element of
\[
(A-A)\cap(f(\mathbb Z)-f(\mathbb Z)).
\]

Because the statement is existential, there is no finite “counterexample” disproving existence. Disproof requires a universal impossibility theorem.

---

## 3. What does not count

None of the following settles the problem:

1. **The degree-\(2\) case alone.** This case is already settled negatively.
2. Impossibility for only even degrees, only odd degrees, monomials, or any other proper subclass.
3. Impossibility for polynomials satisfying
   \[
   f(\mathbb Z)-f(\mathbb Z)\supseteq q\mathbb Z
   \]
   unless this is proved for every polynomial of degree at least \(2\).
4. Results assuming \(A\) has positive density, is syndetic, periodic, measurable in some extra structure, finitely generated, automatic, or eventually periodic.
5. Proving that representations are unique for “almost all” integers or that every sufficiently large integer has a representation.
6. Obtaining boundedly many representations instead of exactly one.
7. Replacing \(\mathbb Z\) by \(\mathbb N\), a finite cyclic group, or a residue ring.
8. Treating \(f(\mathbb N)\) instead of \(f(\mathbb Z)\).
9. Counting parameters \(k\) rather than distinct values \(f(k)\).
10. Heuristic density comparisons such as
    \[
    |A\cap[-N,N]|\approx N^{1-1/d}
    \]
    without a rigorous localization theorem controlling which polynomial values represent integers in that interval.
11. A conditional result depending on a major unresolved conjecture.
12. A finite search that finds no tiling in a bounded window. Representations of integers in the window may use very large \(a\) and \(f(k)\) of opposite signs.

---

## 4. Known results and context

### 4.1 The general subgroup-difference obstruction

Let \(C\subseteq\mathbb Z\) be infinite. Suppose
\[
C-C\supseteq q\mathbb Z
\]
for some \(q\ge1\). Then \(C\) cannot be a direct summand of \(\mathbb Z\) with an infinite complementary set \(A\).

Indeed, any infinite \(A\) contains distinct \(a,a'\) congruent modulo \(q\). Hence
\[
0\ne a-a'\in q\mathbb Z\subseteq C-C,
\]
contradicting
\[
(A-A)\cap(C-C)=\{0\}.
\]

This is the mechanism in the database commentary.

### 4.2 Any possible complement \(A\) must be infinite

For a polynomial of degree \(d\ge2\), its value set is uniformly sparse:
\[
\sup_{x\in\mathbb Z}
\bigl|f(\mathbb Z)\cap[x,x+N]\bigr|
=O_f(N^{1/d}+1).
\]
In particular, \(f(\mathbb Z)\) has upper Banach density zero. A finite union of translates of it cannot cover \(\mathbb Z\). Therefore \(A\) cannot be finite.

### 4.3 Degree \(2\) is completely settled negatively

Let
\[
f(x)=\alpha x^2+\beta x+\gamma
\]
be integer-valued on \(\mathbb Z\), with \(\alpha\ne0\).

If \(\beta\ne0\), then
\[
f(k)-f(-k)=2\beta k.
\]
Because \(f(1)-f(-1)=2\beta\in\mathbb Z\), the nonzero integer
\[
q=|2\beta|
\]
satisfies
\[
q\mathbb Z\subseteq f(\mathbb Z)-f(\mathbb Z).
\]

If \(\beta=0\), then
\[
f(k+1)-f(k-1)=4\alpha k.
\]
Here \(4\alpha\in\mathbb Z\), so
\[
|4\alpha|\mathbb Z\subseteq f(\mathbb Z)-f(\mathbb Z).
\]

Thus the subgroup-difference obstruction applies to every integer-valued quadratic. In particular, **no quadratic polynomial works**.

For \(f\in\mathbb Z[x]\), this is exactly the argument recorded in the database commentary.

### 4.4 A higher-degree class also ruled out

Suppose
\[
f(x)=g((x-k)^2)+c_1x+c_0,
\]
where \(g\in\mathbb Z[x]\), \(k,c_0,c_1\in\mathbb Z\), and \(c_1\ne0\). Then
\[
f(k+t)-f(k-t)=2c_1t.
\]
Therefore
\[
2c_1\mathbb Z\subseteq f(\mathbb Z)-f(\mathbb Z),
\]
and no exact complement exists.

This rules out many even-degree polynomials whose nonlinear part is symmetric about an integral center and whose antisymmetric part is nonzero linear.

### 4.5 The cubic test case is genuinely different

For
\[
f(x)=x^3,
\]
the difference set
\[
D_3=\{k^3-\ell^3:k,\ell\in\mathbb Z\}
\]
does not contain \(q\mathbb Z\) for any \(q\ge1\). A quantitative reason is
\[
|D_3\cap[-X,X]|=O(X^{2/3}).
\]

To see the corresponding pair bound, write \(k-\ell=h\ne0\):
\[
k^3-\ell^3
=h(k^2+k\ell+\ell^2).
\]
For fixed \(h\), the quadratic factor grows like \(\ell^2+h^2\), giving
\[
O\!\left(\sqrt{\frac X{|h|}}+1\right)
\]
possible \(\ell\), while \(|h|=O(X^{1/3})\). Summation yields \(O(X^{2/3})\).

Thus the quadratic argument cannot simply be reused for cubes. Note also that
\[
1^3-(-1)^3=2;
\]
the fact that some small integers are cube differences says nothing about containing a complete subgroup \(q\mathbb Z\).

### 4.6 A hypothetical complement has upper Banach density zero

If \(A+C=\mathbb Z\) uniquely and \(C\) is infinite, then the translates
\[
A+c,\qquad c\in C,
\]
are pairwise disjoint.

Choose distinct \(c_1,\dots,c_m\in C\). For any interval \(I\) of length \(N\),
\[
\sum_{i=1}^m |(A+c_i)\cap I|\le N.
\]
After comparing the shifted intervals \(I-c_i\) with a fixed one and allowing an \(O_{c_1,\dots,c_m}(1)\) boundary error,
\[
m|A\cap I|\le N+O(1).
\]
Hence
\[
d^*(A)\le \frac1m.
\]
Since \(m\) is arbitrary,
\[
d^*(A)=0.
\]

This is crucial: positive-density recurrence theorems cannot be applied directly to \(A\).

### 4.7 Relation to polynomial recurrence

The Furstenberg–Sárközy theorem and its polynomial extensions imply that a positive-density set contains differences of the form \(P(n)\) for suitable integer polynomials \(P\) with \(P(0)=0\). In the present setting,
\[
P(n)=f(n)-f(0)
\]
is contained in \(f(\mathbb Z)-f(\mathbb Z)\), after a harmless input dilation if \(f\) is merely integer-valued.

This would immediately contradict uniqueness if \(A\) had positive upper density. But the preceding argument shows that any hypothetical \(A\) must have upper Banach density zero, so the standard polynomial recurrence machinery is below the required threshold.

### 4.8 Periodic complements are impossible

If \(A\) has a nonzero period \(p\), then
\[
p\mathbb Z\subseteq A-A.
\]
Since \(f(\mathbb Z)\) is infinite, two distinct values of \(f\) are congruent modulo \(p\), so
\[
(f(\mathbb Z)-f(\mathbb Z))\cap p\mathbb Z
\]
contains a nonzero element. This contradicts uniqueness.

Therefore any affirmative construction must be genuinely aperiodic.

This also explains why finite-tile periodicity theorems, such as Newman’s theorem for finite tiles of \(\mathbb Z\), do not directly solve the problem: here the polynomial tile is infinite, and a periodic complement is already impossible.

### 4.9 Linear polynomials behave differently

The degree restriction is essential. If
\[
f(k)=mk+r,\qquad m\ne0,
\]
then
\[
f(\mathbb Z)=r+m\mathbb Z,
\]
and a complete set of residues modulo \(|m|\), shifted appropriately, gives an exact complement. The obstruction begins only at degree \(2\).

---

## 5. Traps and edge cases

1. **Do not count two parameters giving the same value twice.**  
   For example, \(k^2=(-k)^2\), but this is one element of \(C_f\).

2. **The intersection criterion is \(\{0\}\), not the empty set.**  
   Both difference sets always contain \(0\).

3. **A congruence is not an equality.**  
   Showing
   \[
   a-a'\equiv f(k)-f(\ell)\pmod q
   \]
   does not produce a collision. Exact equality in \(\mathbb Z\) is required.

4. **The subgroup argument requires an entire subgroup.**  
   Finding many multiples of \(q\) in \(C_f-C_f\) is insufficient unless every difference forced by pigeonhole is covered or another argument closes the gap.

5. **No unjustified localization.**  
   If \(n=a+f(k)\) lies in a small interval, \(a\) and \(f(k)\) need not be small. They may be very large with opposite signs.

6. **Even and odd degree have different geometry.**
   - An even-degree value set is bounded on one side.
   - An odd-degree value set is unbounded in both directions.
   
   Arguments based on well-ordering or one-sided formal series may apply only to the former.

7. **Integer-valued versus integer-coefficient polynomials.**  
   Divisibility identities valid coefficientwise for \(\mathbb Z[x]\) need rechecking for \(\mathbb Q[x]\). Passing to an input arithmetic progression often clears denominators.

8. **Constant and input shifts do not change the essence.**
   - Replacing \(f(x)\) by \(f(x+t)\), \(t\in\mathbb Z\), does not change its value set.
   - Replacing \(f\) by \(f+s\) only translates \(C_f\), which can be absorbed by translating \(A\).
   - Negating both summands changes \(f\) to \(-f\).

9. **A candidate complement cannot be periodic.**  
   Searches restricted to periodic \(A\) cannot find a solution.

10. **Positive-density arguments are structurally blocked.**  
    Any valid \(A\) has upper Banach density zero.

11. **Finite cyclic tilings are not automatically necessary.**  
    Reducing an infinite tiling modulo \(m\) can merge infinitely many values and representations. Failure or success modulo \(m\) is only decisive if accompanied by a rigorous lifting or projection lemma.

12. **The tag “Sidon sets” should not be overread.**  
    Neither \(A\) nor \(C_f\) must individually be Sidon. The condition is the cross-difference restriction
    \[
    (A-A)\cap(C_f-C_f)=\{0\}.
    \]

---

## 6. Verification hooks

### 6.1 Symbolic difference-slice computation

For a proposed \(f\), compute
\[
G_h(x):=f(x+h)-f(x).
\]
This is a degree-\((d-1)\) polynomial in \(x\). Search symbolically for substitutions \(x=u(t)\), \(h=v(t)\) that make \(G_h(x)\) linear in \(t\) or cover an arithmetic progression.

For symmetric polynomials, test
\[
f(k+t)-f(k-t).
\]

A computer algebra system can certify identities showing
\[
q\mathbb Z\subseteq f(\mathbb Z)-f(\mathbb Z).
\]

### 6.2 Enumerating the polynomial difference set

For bounds \(K,X\), compute
\[
D_{K,X}:=
\{f(k)-f(\ell):|k|,|\ell|\le K,\ |f(k)-f(\ell)|\le X\}.
\]

Record:

- \(|D_{K,X}|\);
- the largest gap in \(D_{K,X}\cap[0,X]\);
- residue classes occupied modulo \(m\);
- the contribution from each slice \(k-\ell=h\);
- representation multiplicities.

Increase \(K\) until a proven growth bound guarantees completeness in \([-X,X]\).

### 6.3 Difference graph for candidate pieces of \(A\)

For a finite interval \(V=[-M,M]\), form a graph with vertex set \(V\), joining \(a\ne a'\) if
\[
a-a'\in D_X
\]
for a sufficiently complete finite portion \(D_X\subseteq C_f-C_f\).

Every finite portion of a valid \(A\) must be an independent set in this graph. Compute independence numbers and compare them with any rigorous lower bound on the number of centers required for local coverage.

### 6.4 Bounded exact-cover ILP/SAT model

Choose bounds \(N,M,K\). Introduce Boolean variables
\[
x_a\in\{0,1\},\qquad |a|\le M,
\]
and impose
\[
\sum_{\substack{c\in f([-K,K])\\ |n-c|\le M}} x_{n-c}=1,
\qquad |n|\le N.
\]

This tests whether the target interval can be tiled using only the bounded set of centers and polynomial values.

Interpretation must be careful:

- A solution is only a finite model.
- Unsatisfiability does not rule out a global tiling unless all representations of \([-N,N]\) are rigorously known to satisfy the chosen bounds.

Use nested boxes and retain only solutions compatible under restriction to detect whether a stable inverse system might exist.

### 6.5 Finite cyclic probes

For \(m\ge2\), compute
\[
C_m:=\{f(k)\bmod m:k\in\mathbb Z\}\subseteq\mathbb Z/m\mathbb Z
\]
and search for
\[
A_m\oplus C_m=\mathbb Z/m\mathbb Z.
\]

Check the necessary cardinality condition
\[
|A_m||C_m|=m
\]
for a direct factorization in the finite group.

These experiments can identify promising digital or \(p\)-adic structures, but are not by themselves consequences of or obstructions to a global nonperiodic tiling.

### 6.6 Direct verification of a proposed constructive \(A\)

For a computable \(A\):

1. Enumerate distinct values \(c=f(k)\), deduplicating collisions.
2. Hash sums \(a+c\) in increasing boxes.
3. Detect duplicate sums and record the corresponding nonzero common difference.
4. Record uncovered integers.
5. Track the maximum sizes of \(|a|\) and \(|c|\) used to cover a target interval.

The fifth statistic is especially important: uncontrolled growth signals that finite-window evidence may not stabilize.

---

## 7. Attack routes

### Route 1: Quantitative difference forcing from exact-cover growth  
**Goal:** Negative solution.

**Core mechanism.** Combine the number of centers needed for coverage with upper bounds for sets avoiding polynomial differences.

A finite subset \(B\subseteq A\) must satisfy
\[
(B-B)\cap(C_f-C_f)=\{0\}.
\]
If coverage could be localized at scale \(X\), the sparsity
\[
|C_f\cap I|=O(X^{1/d})
\]
would suggest that roughly \(X^{1-1/d}\) centers are needed to cover an interval of length \(X\). One would then seek an extremal theorem showing that every subset of an interval of that size has a nonzero difference in \(C_f-C_f\).

**Key lemma needed.** A rigorous localization theorem of the form:

> In every exact tiling \(\mathbb Z=A\oplus C_f\), there are arbitrarily large intervals \(I\) for which many representations \(n=a+c\), \(n\in I\), use \(a\) and \(c\) lying in controlled intervals of polynomial size.

Together with this, one needs a strong quantitative polynomial-difference theorem at density approximately \(X^{-1/d}\), far below positive density.

**Why it might work.** Exact coverage imposes a quantitative burden even though \(A\) has density zero. The union of the difference slices
\[
f(k+h)-f(k)
\]
may be substantially more forcing than any one polynomial sequence.

**Most likely failure point.** Representations may be violently nonlocal: a bounded interval could be covered by centers and polynomial values of arbitrarily large opposite magnitude. Existing Sárközy-type bounds are also likely too weak at the required sparse scale.

**Quick blockage test.** For \(f(x)=x^3\), compute the maximum independent set in the truncated cube-difference graph on \([1,N]\), and compare it with \(N^{2/3}\). If independent sets substantially larger than the expected coverage scale persist, pure extremal difference forcing is unlikely to suffice.

---

### Route 2: One-sided order and generating functions for even degree  
**Goal:** Negative solution, initially for all even-degree polynomials.

After an output translation and possibly negation, an even-degree value set can be arranged as
\[
C_f\subseteq\mathbb N_0,\qquad 0\in C_f,
\]
with \(C_f\) infinite.

The tiling equation becomes
\[
\sum_{c\in C_f}1_A(n-c)=1
\qquad(n\in\mathbb Z).
\]

**Key lemma needed.** Prove a structural theorem such as:

> If an infinite set \(C\subseteq\mathbb N_0\) with growing gaps tiles all of \(\mathbb Z\) uniquely, then its translation set is periodic, or \(C\) is finite, or the tiling induces an impossible well-founded recurrence.

Any periodicity conclusion would contradict the known impossibility of periodic \(A\).

**Why it might work.** The tile is one-sided and locally finite. Equations for successive \(n\) resemble a renewal recurrence, and polynomial gaps eventually grow regularly. This is stronger structure than is available for odd-degree images.

**Most likely failure point.** Although \(C_f\) is bounded below, \(A\) is unbounded below. Formal power-series multiplication is not automatically legitimate, and there is no least element of \(A\) from which to start an induction. Infinite one-sided exact complements can exhibit digital behavior.

**Quick blockage test.** Run exact-cover searches for \(C=\{k^4:k\in\mathbb Z\}\) on increasingly long intervals, allowing a large negative range for centers. Check whether solutions force stable periodic patterns or instead keep introducing new distant centers.

---

### Route 3: Fourier or distributional obstruction  
**Goal:** Negative solution.

The formal convolution identity is
\[
1_A*1_{C_f}=1.
\]
Polynomial exponential sums have strong cancellation away from rational frequencies, while exact tilings often impose rigid spectral relations.

**Key lemma needed.** A legitimate Fourier framework for two infinite zero-density sets, for example an Abel-weighted or Følner-averaged identity whose boundary error remains controlled despite nonlocal representations. One would want a conclusion resembling
\[
\widehat{1_A}(\theta)\,\widehat{1_{C_f}}(\theta)=0
\]
away from frequency \(0\), with enough spectral support information to force periodicity or contradiction.

**Why it might work.** Weyl bounds give precise information about
\[
\sum_{|k|\le K}e(\theta f(k)).
\]
Finite translational tilings are heavily constrained by zeros of mask polynomials; an infinite analogue may retain enough rigidity.

**Most likely failure point.** Neither indicator is summable, both have upper Banach density zero, and ordinary Fourier transforms are distributions. Weighting destroys exact convolution because representations may use terms far outside the weighted window.

**Quick blockage test.** For finite exact-cover models, compute weighted Fourier products
\[
\left(\sum_a x_a e^{-\varepsilon|a|}e(\theta a)\right)
\left(\sum_k e^{-\varepsilon|f(k)|}e(\theta f(k))\right)
\]
and measure whether residuals concentrate at rational frequencies as boxes expand. Lack of stabilization would indicate that boundary nonlocality is fatal.

---

### Route 4: \(p\)-adic/digital rigidity and finite quotients  
**Goal:** Negative solution, or structural reduction.

Exact factorizations of integers often arise from mixed-radix digit decompositions. A polynomial value set has highly constrained behavior modulo \(p^r\), governed by \(p\)-adic valuations of
\[
f(k)-f(\ell).
\]

**Key lemma needed.** Show that a global exact tiling by \(C_f\) induces a compatible family of finite or \(p\)-adic factorizations, or an odometer-like structure. Then prove that no polynomial value set of degree at least \(2\) can occupy the required digit positions.

A particularly useful statement would be:

> Every exact complement of a polynomial value set has a nontrivial period modulo some \(p^r\), or yields a clopen factorization of \(\mathbb Z_p\).

Any actual period of \(A\) is impossible.

**Why it might work.** Polynomial images modulo prime powers are algebraically rigid, and differences have controlled valuations through Taylor expansion:
\[
f(k+p^r t)-f(k)
=p^r t f'(k)+\cdots.
\]

**Most likely failure point.** A global nonperiodic tiling need not project to a direct factorization modulo \(p^r\); reduction merges infinitely many translates and values. The required compactness or finite-local-complexity theorem may be false.

**Quick blockage test.** For \(f(x)=x^3\), enumerate \(C_{p^r}\), its difference set, and all direct factorizations of \(\mathbb Z/p^r\mathbb Z\) for small \(p,r\). Determine whether compatible factorizations survive as \(r\) increases. If no consistent digital pattern exists, this supports the route but is not yet a proof.

---

### Route 5: Representation-selector cocycle and polynomial gap rigidity  
**Goal:** Negative solution.

Assuming a tiling, define the unique selector
\[
c(n)\in C_f,\qquad a(n):=n-c(n)\in A.
\]
Then
\[
a(n+1)-a(n)=1-\bigl(c(n+1)-c(n)\bigr).
\]
More generally,
\[
a(n+t)-a(n)
=t-\bigl(c(n+t)-c(n)\bigr).
\]

Because every difference of two \(a(n)\)'s must avoid \(C_f-C_f\), the selector is subject to a large system of forbidden transition identities.

**Key lemma needed.** Prove that polynomial gap growth forces the selector \(c(n)\) to have repeated or slowly varying transition patterns, and that one such recurrence yields
\[
a(n+t)-a(n)\in C_f-C_f\setminus\{0\}.
\]

A possible target is a finite-pattern recurrence theorem for the normalized increments of \(c(n)\).

**Why it might work.** Coverage supplies a canonical global function, rather than merely a sparse set \(A\). Comparing neighboring or congruent integers may expose rigidity invisible in density arguments.

**Most likely failure point.** The selector can jump between extremely distant polynomial values. There is no a priori bound on
\[
|c(n+1)-c(n)|
\]
or any finite alphabet of transition types, so symbolic recurrence may not apply.

**Quick blockage test.** Extract selector sequences from bounded SAT solutions. Measure the number of distinct transition patterns
\[
(c(n+1)-c(n),\ldots,c(n+L)-c(n+L-1))
\]
after normalization by polynomial indices. Explosive pattern growth would indicate that no finite-state argument is available without a new regularity lemma.

---

### Route 6: Constructive exact complement for \(f(x)=x^3\)  
**Goal:** Affirmative solution; this would refute the Erdős–Graham expectation.

The cube-difference set is sparse, so it may be possible to build \(A\) recursively while maintaining
\[
(A-A)\cap(D_3\setminus\{0\})=\varnothing
\]
and gradually covering all integers by translates \(a+C_3\), where
\[
C_3=\{k^3:k\in\mathbb Z\}.
\]

**Key lemma needed.** A finite-extension theorem:

> Every finite partial family of pairwise disjoint translates of \(C_3\), satisfying suitable boundary conditions, can be extended so as to cover one more prescribed integer without destroying the possibility of completing the tiling.

Alternatively, prove that a nested sequence of finite exact-cover instances has a compatible infinite branch and that the resulting branch covers every integer.

**Why it might work.** The sparseness
\[
|D_3\cap[-X,X]|=O(X^{2/3})
\]
leaves many possible differences outside \(D_3\), so large cube-difference-free sets exist locally. Cubes are also unbounded in both directions, allowing a new center to target an uncovered integer using a very large positive or negative cube.

**Most likely failure point.** Adding one center adds the entire translate \(a+C_3\), not a single point. It may create collisions arbitrarily far away. Local compactness is difficult because each coverage equation involves infinitely many possible centers and cube values. Greedy coverage may irreversibly block a distant integer.

**Quick blockage test.** Build nested exact-cover models with strict compatibility on a central interval and rapidly expanding margins. Require each stage to extend the preceding assignment rather than merely finding a new unrelated solution. Persistent compatible branches would be meaningful evidence; repeated unavoidable dead ends would suggest a hidden global obstruction.

---

## 8. Verdict on difficulty

The degree-\(2\) case is settled, as are all polynomials whose difference set contains a nonzero subgroup \(q\mathbb Z\). These results do **not** approach the full existential question unless one can prove that every polynomial difference set has an equally strong unavoidable structure—which is false for the simplest cubic example in the literal subgroup sense.

The first natural unresolved model is
\[
C=\{k^3:k\in\mathbb Z\}.
\]
It evades the elementary congruence-pigeonhole argument because its difference set is sparse. At the same time, any exact complement must be:

- infinite;
- aperiodic;
- of upper Banach density zero;
- disjoint from all its translates by nonzero cube differences;
- nevertheless sufficient, together with the cubes, to cover every integer exactly once.

This combination places the problem outside standard positive-density polynomial recurrence and outside standard finite-tile periodicity theory.

There is no known equivalence here to a famous conjecture such as the polynomial Szemerédi theorem, and that theorem does not directly help because the hypothetical complement has zero upper Banach density. The main difficulty is instead an infinite, nonperiodic translational-tiling problem with severe nonlocality.

A complete negative solution likely requires a new rigidity theorem for exact complements of sparse polynomial sequences. A complete affirmative solution likely requires a genuinely nonperiodic recursive or \(p\)-adic construction with unusually strong global collision control. Either direction appears substantially harder than the settled quadratic case.