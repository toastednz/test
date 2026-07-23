# Round 2 Problem Brief: Erdős Problem #196

**Status:** Open  
**Reference point:** Davis–Entringer–Graham–Simmons (1977), abbreviated DEGS  
**Subject:** Monotone arithmetic progressions in permutations of \(\mathbb N\)

---

## 1. Precise statement

Let
\[
\mathbb N=\{1,2,3,\dots\}.
\]
A permutation of \(\mathbb N\) is a bijection
\[
x:\mathbb N\to\mathbb N,\qquad i\mapsto x_i.
\]
Let
\[
p=x^{-1},
\]
so \(p(n)\) is the unique position at which the value \(n\) occurs.

A four-term arithmetic progression is an ordered tuple
\[
(a,a+d,a+2d,a+3d)
\]
with \(a,d\in\mathbb N\), hence \(d>0\).

The problem asks whether every permutation \(x\) has some \(a,d\in\mathbb N\) such that either
\[
p(a)<p(a+d)<p(a+2d)<p(a+3d)
\tag{INC}
\]
or
\[
p(a)>p(a+d)>p(a+2d)>p(a+3d).
\tag{DEC}
\]

Equivalently, in the sequence \(x_1,x_2,\dots\), the four increasing values
\[
a,a+d,a+2d,a+3d
\]
must appear either in increasing positional order or in decreasing positional order.

### Order-theoretic formulation

Define a strict total order \(\prec\) on the values by
\[
u\prec v \iff p(u)<p(v).
\]
Then the question is whether every total order \(\prec\) on \(\mathbb N\) of order type \(\omega\) contains \(a,d\ge 1\) for which
\[
a\prec a+d\prec a+2d\prec a+3d
\]
or
\[
a+3d\prec a+2d\prec a+d\prec a.
\]

Here “order type \(\omega\)” is essential: it means every element has only finitely many \(\prec\)-predecessors. Conversely, every total order on \(\mathbb N\) in which each element has finitely many predecessors is induced by a permutation.

### Comparison-coloring formulation

For \(u<v\), define
\[
c(u,v)=
\begin{cases}
+,&p(u)<p(v),\\
-,&p(u)>p(v).
\end{cases}
\]
This coloring must be transitive because it comes from a total order. A four-term progression is monotone exactly when its three adjacent comparisons are all \(+\) or all \(-\):
\[
c(a,a+d)=c(a+d,a+2d)=c(a+2d,a+3d).
\]

The order-type-\(\omega\) condition is equivalent to the eventual-forward property
\[
\forall u\in\mathbb N\ \exists V(u)\ \forall v\ge V(u):
\quad c(u,v)=+.
\tag{EF}
\]
Indeed, only finitely many values can occur before a fixed \(u\).

### Ambiguities in the database wording

1. Some conventions include \(0\) in \(\mathbb N\). This only translates the problem and makes no substantive difference.
2. “\(x_i,x_j,x_k,x_l\) are an arithmetic progression” is read in the standard ordered sense: the listed terms have a common nonzero difference. The intended problem is not merely that the four values form an arithmetic-progression set in some scrambled order.
3. The two index directions in the original wording correspond precisely to (INC) and (DEC).

---

## 2. What counts as a solution

### A complete affirmative solution

A proof must start with an **arbitrary** bijection \(p:\mathbb N\to\mathbb N\) and prove the existence of \(a,d\ge1\) satisfying either (INC) or (DEC).

It is enough to prove the stronger assertion that every permutation has an increasing positional four-term progression, namely (INC). Likewise, a proof that every permutation has a decreasing one would suffice.

Any auxiliary reduction must retain the order-type-\(\omega\) property. If the argument passes to a limiting total order, it must justify that the limit still has finite predecessor sets, or otherwise recover a progression in the original permutation.

### A complete negative solution

A disproof must establish the existence of a bijection
\[
p:\mathbb N\to\mathbb N
\]
such that for every \(a,d\ge1\),
\[
\neg\bigl(p(a)<p(a+d)<p(a+2d)<p(a+3d)\bigr)
\]
and
\[
\neg\bigl(p(a)>p(a+d)>p(a+2d)>p(a+3d)\bigr).
\]

Equivalently, for every \(a,d\), the sign sequence
\[
\operatorname{sgn}(p(a+d)-p(a)),\quad
\operatorname{sgn}(p(a+2d)-p(a+d)),\quad
\operatorname{sgn}(p(a+3d)-p(a+2d))
\]
must contain both signs.

A nonconstructive existence proof would logically suffice. For an explicit construction, one must verify:

1. **Totality:** \(p(n)\) is defined for every \(n\).
2. **Injectivity:** \(p(m)\ne p(n)\) for \(m\ne n\).
3. **Surjectivity:** every position is used; equivalently, the resulting sequence lists every natural number exactly once.
4. **Universal avoidance:** both monotone orientations are excluded for every \(a,d\ge1\).

If the construction is first presented as a total order, it is not enough to prove transitivity and avoidance. One must also prove that every element has finitely many predecessors.

A finite-state or automatic construction may use a finite automaton emptiness certificate to verify universal avoidance, but the automaton argument itself must be turned into a rigorous proof.

---

## 3. What does not count

The following do not resolve the problem.

1. **The DEGS three-term theorem.** Every permutation has a monotone three-term arithmetic progression, but a three-term progression need not extend to four terms.

2. **The DEGS five-term counterexample.** A permutation avoiding monotone five-term progressions may still contain monotone four-term progressions.

3. **Avoiding only one orientation.** A counterexample must avoid both increasing and decreasing positional orders.

4. **Finite avoiders.** There are avoiding linear orders on every finite interval \([N]\), even orders avoiding monotone three-term progressions. Thus no theorem of the form “every order on \([N]\), for sufficiently large \(N\), contains the desired progression” can be true without additional rank or coherence hypotheses.

5. **An arbitrary infinite total order.** The least-significant-bit order below avoids monotone three-term progressions but is not of order type \(\omega\), hence is not a permutation order.

6. **Quantile control.** Showing that the rank of each fixed value is \(o(N)\) inside \([N]\) is weaker than showing that its rank is bounded. A genuine permutation requires
   \[
   \sup_{N\ge n}\operatorname{rank}_{[N]}(n)<\infty
   \]
   for every fixed \(n\).

7. **Extremum counts alone.** Quadratically many local maxima and minima are compatible with known finite avoiders and do not force a monotone four-term progression.

8. **Uniform or pseudorandom cases only.** A proof that small \(U^3\)-norm, random arrival layers, or genericity forces a progression handles only the unstructured case.

9. **Balanced or nested arrival partitions alone.** Coherent nested quartile partitions can avoid the relevant ordered-rainbow pattern at every selected \(4\)-adic scale.

10. **Conditional structural statements.** A proof conditional on a new inverse theorem, compatibility theorem, or density-increment assertion is not a solution until that assertion is proved.

11. **Ramsey extraction without additive control.** An infinite comparison-homogeneous set may be arbitrarily sparse and need not contain any arithmetic progression.

12. **Finite computation without a uniform certificate.** SAT solutions or exclusions up to a large bound are evidence only. Unconstrained finite avoidance instances are satisfiable for every \(N\).

---

## 4. Known results and context

### 4.1 Published length results

DEGS proved:

- Every permutation of \(\mathbb N\) contains a monotone three-term arithmetic progression.
- There exists a permutation of \(\mathbb N\) containing no monotone five-term arithmetic progression.

Consequently:

- Length \(3\) is settled affirmatively.
- Every length \(k\ge5\) is settled negatively, since a monotone \(k\)-term progression contains a monotone five-term subprogression consisting of five consecutive terms.
- Length \(4\) is the unique unresolved boundary case.

No implication from a famous conjecture such as Szemerédi’s theorem, van der Waerden’s theorem, or Green–Tao is known. Those theorems concern color classes or dense sets, whereas the present problem concerns the relative order of an injective rank function.

---

### 4.2 The dyadic proof mechanism for three terms

A useful reconstruction of the DEGS mechanism is the following.

For every permutation \(p\), every \(r,d\ge1\), there are infinitely many \(j\ge0\) such that
\[
p(r)<p(r+2^jd)<p(r+2^{j+1}d).
\tag{D3}
\]

Indeed, all but finitely many values \(r+2^jd\) occur after \(r\). The infinite sequence
\[
p(r+2^jd)
\]
cannot be eventually strictly decreasing, since it consists of positive integers. Hence it has infinitely many adjacent ascents after the finite exceptional initial part.

For \(s=2^jd\), (D3) gives
\[
p(r)<p(r+s)<p(r+2s),
\]
an increasing positional three-term progression.

In a hypothetical four-term avoider, for all but finitely many such \(j\), the fourth term must cap this triple:
\[
p(r)<p(r+3s)<p(r+2s).
\tag{CAP}
\]
Otherwise
\[
r,r+s,r+2s,r+3s
\]
would be increasing in position.

The cap gives no fixed relation between \(p(r+s)\) and \(p(r+3s)\), and does not by itself produce a descending chain of positions.

---

### 4.3 Order type \(\omega\) and finite-restriction ranks

For a total order \(\prec\) on \(\mathbb N\), let
\[
r_N(v)=1+\#\{u\le N:u\prec v\}
\]
for \(N\ge v\). Then the following are equivalent:

1. \(\prec\) is induced by a permutation of \(\mathbb N\).
2. Every element has finitely many predecessors.
3. For every fixed \(v\),
   \[
   \sup_{N\ge v}r_N(v)<\infty.
   \]
4. The comparison coloring is eventually forward as in (EF).

This is the precise extra condition absent from compactness arguments based only on finite orders.

---

### 4.4 The least-significant-bit order

Write \(\varepsilon_t(n)\in\{0,1\}\) for the \(t\)-th binary digit of \(n\). For \(u\ne v\), let
\[
t=\nu_2(|u-v|),
\]
the least binary position at which \(u\) and \(v\) differ. Define
\[
u\prec_{\mathrm{LSB}} v
\quad\Longleftrightarrow\quad
\varepsilon_t(u)<\varepsilon_t(v).
\]

This is lexicographic order read from the least significant bit upward.

For every three-term progression
\[
a,\ a+d,\ a+2d,
\]
the midpoint \(a+d\) is an extremum in this order relative to the endpoints. If \(t=\nu_2(d)\), then the two endpoints have the same \(t\)-th bit while the midpoint has the opposite bit, and all lower bits agree. Thus the midpoint lies either before both endpoints or after both endpoints.

Therefore:

- \(\prec_{\mathrm{LSB}}\) contains no monotone three-term arithmetic progression.
- Every finite restriction of it avoids monotone three-term, hence four-term, progressions.
- It is not of order type \(\omega\); some elements have infinitely many predecessors.

This is the decisive obstruction to all arguments using only an induced order on one finite value interval.

---

### 4.5 Pathwise extrema

Fix \(a,d\ge1\) and consider
\[
a,a+d,\dots,a+(L-1)d.
\]
Let
\[
\sigma_t=\operatorname{sgn}\bigl(p(a+(t+1)d)-p(a+td)\bigr),
\qquad 0\le t<L-1.
\]

In a four-term avoider, \(\sigma\) has no run of three identical signs. A sign change corresponds to a strict local extremum of the position sequence.

The sharp consecutive-window consequences are:

- At least
  \[
  H(L)=\left\lfloor\frac{L-2}{2}\right\rfloor
  \]
  local extrema in total.
- At least
  \[
  G(L)=\left\lfloor\frac{L-2}{4}\right\rfloor
  \]
  local maxima and at least \(G(L)\) local minima.

These are exact for the sign-word condition. Additional nonconsecutive arithmetic-progression constraints may impose more structure.

---

### 4.6 Extremum incidence counting

For a finite induced order on \([N]\), let
\[
Q_N=\#\{(a,d):a+3d\le N\}
=\sum_{d\le (N-1)/3}(N-3d).
\]

For each four-term progression, count an incidence at its second term if that term is a local maximum or minimum relative to the first and third terms, and similarly at its third term relative to the second and fourth terms. Let \(I_N\) be the total incidence count.

Every nonmonotone sequence of four distinct ranks has at least one and at most two internal local extrema. Hence in a four-term avoider,
\[
Q_N\le I_N\le 2Q_N.
\tag{EI}
\]

Define
\[
M_N^{\max}
=
\#\{(c,d):1\le c-d<c+d\le N,\ 
p(c)>\max(p(c-d),p(c+d))\},
\]
and define \(M_N^{\min}\) analogously. The previous work established
\[
M_N^{\max}\ge \frac{N^2}{40}-O(N),
\qquad
M_N^{\min}\ge \frac{N^2}{40}-O(N).
\]

These counts are with multiplicity over centered three-term progressions, not counts of distinct centers.

If \(r_N(c)\) is the induced rank of \(c\) in \([N]\), elementary rank-capacity bounds include
\[
\#\{d:c\text{ is a local maximum at step }d\}
\le \left\lfloor\frac{r_N(c)-1}{2}\right\rfloor,
\]
and
\[
\#\{d:c\text{ is a local minimum at step }d\}
\le \left\lfloor\frac{N-r_N(c)}{2}\right\rfloor.
\]
Multiplicity-weighted analogues were also established.

These inequalities do not close: the LSB order makes every possible midpoint extremal and attains \(I_N=2Q_N\). Moreover, quantities such as
\[
\sum_{n\le N}p(n)
\]
have no useful universal upper bound for permutations.

---

### 4.7 Arrival layers and \(U^3\)

For a finite value interval, partition values according to position thresholds
\[
t_1<t_2<t_3.
\]
This creates four ordered arrival bands.

If a four-term progression has ranks
\[
r_0<r_1<r_2<r_3,
\]
then the number of threshold triples separating its four terms into consecutive arrival bands is exactly
\[
(r_1-r_0)(r_2-r_1)(r_3-r_2).
\]
Thus summing ordered-rainbow progressions over all nested threshold triples counts increasing positional four-term progressions with this exact gap weight. The decreasing case is analogous.

A generalized von Neumann argument for four-term progressions shows that sufficiently \(U^3\)-uniform, balanced arrival layers force an ordered-rainbow four-term progression. Therefore every finite avoiding order has a nontrivial \(U^3\)-structured component in at least one relevant layer.

This does not settle the structured case:

- Arbitrary balanced ordered-rainbow assertions fail, for example through block order \(1,3,2,4\).
- Balance, nesting, and fairness across all \(4\)-adic scales still do not suffice; there are genuine permutations whose selected nested quartile colorings avoid the desired rainbow pattern at every such scale.
- Standard \(U^3\) inverse theory produces scale-dependent quadratic structure but does not make these structures compatible across all arrival thresholds or retain bounded predecessor information.

---

### 4.8 Comparison coloring and eventual clauses

In a four-term avoider, eventual forwardness gives a strong endpoint clause.

For every fixed \(b\), all sufficiently large \(d\) satisfy
\[
p(b)<p(b+d).
\]
Hence avoidance of the increasing progression
\[
b,b+d,b+2d,b+3d
\]
forces
\[
p(b+d)>p(b+2d)
\quad\text{or}\quad
p(b+2d)>p(b+3d)
\tag{EC}
\]
for all sufficiently large \(d\).

The unresolved issue is to exploit these clauses simultaneously over their highly overlapping affine configurations. Each single-anchor subsystem can be satisfied by an order of type \(\omega\); previous work constructed such an order satisfying all avoidance constraints involving a designated globally first element.

Ramsey theory does not solve the overlap problem: it can extract comparison-homogeneous sets only at the cost of arbitrary additive sparsity. Fixed finite template gadgets do not prevent this sparsification.

---

### 4.9 Affine suffix records

For \(n,q\ge1\), consider the affine ray
\[
R(n,q)=\{n+kq:k\ge0\}.
\]
A coefficient \(k\) is a suffix record if
\[
p(n+kq)<p(n+\ell q)
\qquad\text{for every }\ell>k.
\]

Every affine ray has infinitely many suffix records: every tail of the sequence of positions has a least element.

The following are established:

1. **Three-record criterion.**  
   If the suffix-record coefficient set contains
   \[
   m,\ m+r,\ m+2r,
   \]
   then
   \[
   n+mq,\ n+(m+r)q,\ n+(m+2r)q,\ n+(m+3r)q
   \]
   form an increasing positional four-term progression.

2. **Two-record rigidity in an avoider.**  
   If \(m\) and \(m+r\) are suffix records but the order avoids monotone four-term progressions, then the associated four terms have the exact positional order
   \[
   0\prec 1\prec 3\prec 2,
   \]
   meaning
   \[
   p(n+mq)
   <
   p(n+(m+r)q)
   <
   p(n+(m+3r)q)
   <
   p(n+(m+2r)q).
   \]

3. **Cofinitely many good steps at a fixed anchor.**  
   For every fixed \(n\), \(n\) is a suffix record of \(R(n,q)\) for all but finitely many \(q\).

   More explicitly, let
   \[
   P^+(n)=\{m>n:p(m)<p(n)\}.
   \]
   This is finite. Define
   \[
   B(n)=\bigcup_{m\in P^+(n)}\{q:q\mid(m-n)\}.
   \tag{BAD}
   \]
   Then \(n\) is a suffix record of \(R(n,q)\) exactly when \(q\notin B(n)\).

4. **No density from a single ray.**  
   The global suffix-record set can be an arbitrarily prescribed infinite set. In particular, it can be extremely sparse and three-term-AP-free.

Thus Szemerédi-type density arguments cannot be applied to a single record set.

---

### 4.10 Constructive obstructions already identified

Several natural counterexample constructions have been eliminated.

- Pure coordinatewise digit permutations, including position-dependent digit maps, contain explicit carry-generated increasing four-term progressions.
- A simple append-only repair of the LSB order fails. Once an omitted target \(n\) would complete a monotone progression with three already scheduled terms, appending \(n\) later remains permanently unsafe.
- Nested balanced \(4\)-adic layer schedules can pass all selected rainbow tests while still failing globally due to carries.
- Any successful construction must therefore use genuinely prefix-dependent or state-dependent scheduling and must reserve endangered values before permanent obstructions form.

---

## 5. Traps and edge cases

1. **The common difference must be positive.**  
   The case \(d=0\) is excluded, and all values are distinct.

2. **Positions need not be consecutive.**  
   The indices \(p(a),p(a+d),p(a+2d),p(a+3d)\) can be arbitrarily far apart.

3. **A monotone subsequence is not enough.**  
   Erdős–Szekeres may find four monotone ranks along a long arithmetic progression, but the selected coefficient indices need not themselves form a four-term arithmetic progression.

4. **Reversing an infinite permutation is not legitimate.**  
   Finite orders have a reversal symmetry; an order of type \(\omega\) generally does not. A proof for increasing progressions cannot automatically be reversed to obtain one for decreasing progressions—although proving either orientation universally is sufficient.

5. **Compactness loses order type.**  
   A coherent sequence of finite avoiders can converge to a total order such as the LSB order with infinitely many predecessors per element.

6. **Small quantile is not bounded rank.**  
   Even \(r_N(v)/N\to0\) permits \(r_N(v)\to\infty\).

7. **Records are suffix minima of positions.**  
   They are not minima of the numerical values on the ray.

8. **Three record coefficients must themselves be in arithmetic progression.**  
   Three arbitrary records do not automatically yield a four-term progression.

9. **Arrival-layer rainbows must respect layer order.**  
   An arbitrary use of all four colors does not correspond to a monotone positional progression.

10. **Cyclic \(U^3\) computations can create wraparound progressions.**  
    Use a sufficiently large cyclic embedding or explicitly remove wraparound and \(d=0\).

11. **The eventual clause is anchor-dependent.**  
    In (EC), the threshold for “sufficiently large \(d\)” may depend arbitrarily on \(b\).

12. **Finite bad-step sets do not alone imply a simultaneous good step.**  
    Abstract finite sets \(B(n)\) can cover every triple
    \[
    B(n)\cup B(n+q)\cup B(n+2q)
    \]
    without contradiction. The sets in (BAD) have extra divisor and predecessor coherence that must be used.

13. **A total order avoiding the pattern is not a counterexample unless it is well-founded in the forward direction.**

14. **Random continuous priorities usually give the wrong order type.**  
    An exchangeable random order typically gives each element infinitely many predecessors.

15. **Do not infer an upper bound on position moments from bijectivity.**  
    Small values may be delayed arbitrarily far.

---

## 6. Verification hooks

### 6.1 Finite avoidance SAT/CP-SAT model

For \(N\), use integer variables
\[
r_v\in\{1,\dots,N\},\qquad v\in[N],
\]
with an `AllDifferent` constraint.

For every \(a,d\) with \(a+3d\le N\), impose
\[
\neg(r_a<r_{a+d}<r_{a+2d}<r_{a+3d})
\]
and
\[
\neg(r_a>r_{a+d}>r_{a+2d}>r_{a+3d}).
\]

Unconstrained instances should remain satisfiable for every tested \(N\). Use the LSB order as a regression witness.

Record:

- the ranks of the first \(K\) values;
- local-extremum counts;
- inversion counts;
- arrival-band \(U^3\)-norms;
- suffix-record sets on many affine rays.

---

### 6.2 LSB comparator regression test

For \(u\ne v\):

1. Compute
   \[
   t=\nu_2(|u-v|).
   \]
2. Compare the \(t\)-th bits of \(u\) and \(v\).
3. Sort \([N]\) by this comparator.
4. Verify that every centered three-term progression has an extremal midpoint.
5. Check that induced ranks of fixed values grow without bound where expected.

Any purported finite forcing theorem contradicted by these tests has omitted the order-type-\(\omega\) condition.

---

### 6.3 Extremum incidence checks

For each finite rank assignment:

1. Compute
   \[
   Q_N=\sum_{d\le(N-1)/3}(N-3d).
   \]
2. For each four-term progression, count internal extrema to obtain \(I_N\).
3. Verify \(Q_N\le I_N\le2Q_N\) in avoiders.
4. Compute \(M_N^{\max}\) and \(M_N^{\min}\).
5. Compare centerwise counts against
   \[
   \lfloor(r_N(c)-1)/2\rfloor,\qquad
   \lfloor(N-r_N(c))/2\rfloor.
   \]

---

### 6.4 Exact bad-step computation

Given a sufficiently long permutation prefix and an arrived value \(n\), its predecessor set is already final:
\[
P^+(n)=\{m>n:p(m)<p(n)\}.
\]
No future arrival can enter it.

Compute
\[
B(n)=\bigcup_{m\in P^+(n)}\operatorname{Div}(m-n).
\]

Search for \(n,q\) satisfying
\[
q\notin B(n)\cup B(n+q)\cup B(n+2q).
\tag{SG}
\]
If all three anchors have arrived, (SG) is exactly verifiable from the finite prefix and certifies
\[
p(n)<p(n+q)<p(n+2q)<p(n+3q).
\]

Also log which predecessor difference certifies each bad membership. This produces the divisor-certificate hypergraph needed in New Route A.

---

### 6.5 Rank-escape optimization

For fixed \(K,N\), define
\[
R_K(N)=
\min_{\prec}
\max_{1\le s\le K} r_N(s),
\]
where the minimum is over four-term-avoiding orders on \([N]\).

Compute \(R_K(N)\) exactly or with certified lower bounds. Also test weighted variants such as
\[
\min_{\prec}\sum_{s\le K}w_s r_N(s).
\]

Unbounded growth of \(R_K(N)\) for one fixed \(K\) would prove the original problem affirmatively.

---

### 6.6 Directed inversion graph

For a finite prefix define
\[
u\to v
\quad\Longleftrightarrow\quad
u<v\ \text{ and }\ p(v)<p(u).
\]

Check:

- outdegrees;
- transitive closure on increasing triples;
- longest directed paths;
- coverage of clauses
  \[
  b+d\to b+2d
  \quad\text{or}\quad
  b+2d\to b+3d.
  \]

Search for finite graphs satisfying these clauses under prescribed degree bounds. Extract minimal unsatisfiable affine clause collections rather than arbitrary finite-order obstructions.

---

### 6.7 Arrival-layer and \(U^3\) checks

For finite \([M]\), choose thresholds \(t_1<t_2<t_3\), form four arrival bands, and count ordered-rainbow four-term progressions.

For balanced indicator functions \(f_i\), compute normalized \(U^3\)-norms using an embedding into \(\mathbb Z/P\mathbb Z\) with \(P\) sufficiently larger than \(M\). Remove \(d=0\) and wraparound solutions.

The goal is diagnostic: identify persistent structured components and test whether their quadratic phases are coherent across nested thresholds.

---

### 6.8 Finite-state construction tests

For a proposed base-\(b\) transducer \(F\):

1. Certify that \(F:\mathbb N\to\mathbb N\) is bijective.
2. Build a product automaton reading the digits of \(a\) and \(d\).
3. Track carries for
   \[
   a,\ a+d,\ a+2d,\ a+3d.
   \]
4. Track transducer states and output comparisons.
5. Accept if
   \[
   F(a)<F(a+d)<F(a+2d)<F(a+3d)
   \]
   or the reverse.
6. Test automaton emptiness.

All known coordinatewise digit constructions must be rejected by a carry-generated witness.

---

## 7. Four new Round-2 attack routes

These routes are designed to address the precise failures of Round 1 rather than repeat finite counting, generic \(U^3\), direct dyadic iteration, or unstructured Ramsey extraction.

---

### New Route A: Divisor-certificate mass transport on affine records

#### Core mechanism

Use the exact description
\[
B(n)=
\bigcup_{m>n,\ p(m)<p(n)}
\operatorname{Div}(m-n).
\]
A step \(q\) is bad at \(n\) only because some larger value
\[
m=n+kq
\]
occurs before \(n\).

If
\[
q\notin B(n)\cup B(n+q)\cup B(n+2q),
\]
then \(n,n+q,n+2q\) are successive suffix records on the \(q\)-ray, yielding an increasing four-term progression.

#### Key lemma needed

A sufficient theorem is:

> **Simultaneous good-step lemma.**  
> For every permutation \(p\), there exist \(n,q\ge1\) such that
> \[
> q\notin B(n)\cup B(n+q)\cup B(n+2q).
> \]

This is stronger than the original problem, so it may fail even if the original problem is true.

A more flexible target would allow three record coefficients in arithmetic progression rather than requiring three consecutive coefficients.

#### Why it might work

Each \(B(n)\) is generated by divisors of finitely many predecessor differences. This is much more rigid than an arbitrary finite subset of \(\mathbb N\).

Charge a bad pair \((n,q)\) to a canonical witness
\[
m=n+kq,\qquad p(m)<p(n),
\]
for example the witness of smallest position or smallest \(k\). One inversion \((n,m)\) can certify only divisors of \(m-n\). Divisor-normalized weights such as
\[
\frac{1}{\tau(m-n)}
\]
may prevent a single inversion from absorbing excessive mass.

The intended multiscale argument should truncate simultaneously by:

- value window \(n\le N\);
- step range \(q\le Q\);
- arrival cutoff \(p(n)\le T\);
- witness rank or witness distance.

Canonical witnesses generate rank-descending forests, potentially allowing a bounded-injury or branching contradiction that raw inversion counts miss.

#### Most likely failure point

Abstract finiteness of the \(B(n)\) is insufficient. For example, one can mark every third point on each \(q\)-ray so that every block
\[
n,n+q,n+2q
\]
contains a marked point while each vertex receives only finitely many marks. Therefore the proof must use the fact that marks arise from actual predecessor witnesses in one common well-order.

A second danger is that an inversion with a highly composite difference can certify many bad steps, and the total number of inversions below a value cutoff has no useful global upper bound without a time cutoff.

#### Quick blocking test

For SAT-generated avoiders and long constructive prefixes:

1. Compute all exact \(B(n)\) for arrived \(n\).
2. Search for simultaneous good steps.
3. If none, assign every covered \((n,q)\) a canonical witness.
4. Measure witness multiplicities by \(\tau(m-n)\), rank drop, and value scale.
5. Test whether divisor-normalized charge remains bounded per inversion.

If a small family exhibits arbitrarily large normalized congestion or a coherent abstract covering compatible with actual predecessor ranks, this route is likely blocked.

---

### New Route B: Rank escape and structural classification of finite avoiders

#### Core mechanism

Finite avoiders exist for all \(N\), but an avoiding permutation would require bounded ranks for every fixed value across all restrictions. Attack exactly that distinction.

For fixed \(K\), recall
\[
R_K(N)=
\min_{\prec}
\max_{1\le s\le K}r_N(s),
\]
where the minimum is over avoiding orders on \([N]\).

#### Key lemma needed

A particularly clean sufficient statement is:

> **Fixed-anchor rank-escape lemma.**  
> There exists a fixed \(K\) such that
> \[
> R_K(N)\longrightarrow\infty
> \qquad(N\to\infty).
> \]

Indeed, if \(p\) were an avoiding permutation, then
\[
r_N(s)\le p(s)
\]
for every \(s\le K\), so
\[
R_K(N)\le \max_{s\le K}p(s),
\]
contradicting divergence.

Even a very slow unbounded lower bound would suffice; linear escape is unnecessary.

#### Why it might work

The LSB order suggests that finite avoiders may require persistent low-bit hierarchical separation, and such separation pushes some fixed small values to unbounded induced rank. The previous \(U^3\) result also says that every finite avoider has substantial structure. A stability or container theorem might classify avoiders into a bounded number of hierarchical types, then show that every such type delays at least one value from a fixed finite anchor set.

Possible tools include:

- hypergraph containers on adjacent-comparison variables;
- entropy decrement across dyadic or \(4\)-adic scales;
- permutation-pattern stability;
- flag-algebra discovery followed by an exact proof;
- recursive classification of near-saturators of the extremum incidence bound.

Unlike the failed generic \(U^3\) route, this route seeks a **global classification tied to actual ranks of fixed values**, not merely a structured phase at each scale.

#### Most likely failure point

Finite avoiders may be able to keep any prescribed finite set of values near the front while moving the non-\(\omega\) defect to larger and larger labels. The explicit one-anchor construction from Round 1 warns that \(K=1\) may be far too weak.

It is also possible that no fixed \(K\) has rank escape even though no coherent family of all these finite orders forms an avoiding permutation. Then one would need a more complicated finite deadline vector rather than a single fixed-anchor statistic.

#### Quick blocking test

Compute \(R_K(N)\) for \(K=1,2,\dots\) and increasing \(N\).

- If \(R_K(N)\) appears bounded, inspect whether the same prefix order on \([K]\) can be maintained.
- If it grows, extract SAT unsatisfiable cores and determine whether they involve a stable finite collection of affine configurations.
- Compare optimized orders with the LSB hierarchy and with \(U^3\)-structured layers.

A persistent construction with \(r_N(s)=s\) for all \(s\le K\) and arbitrarily large \(N\), for every tested \(K\), would strongly disfavor the simplest rank-escape lemma.

---

### New Route C: A well-founded affine descent-graph theorem

#### Core mechanism

From a hypothetical permutation define the forward inversion graph
\[
G_p=\{(u,v):u<v,\ p(v)<p(u)\}.
\]
Write \(u\to v\) for \((u,v)\in G_p\).

This graph has three crucial properties:

1. Every edge goes numerically forward: \(u<v\).
2. Every vertex has finite outdegree:
   \[
   \deg^+(u)\le p(u)-1.
   \]
3. It is transitively closed along increasing numerical chains:
   \[
   u<v<w,\quad u\to v,\quad v\to w
   \ \Longrightarrow\ 
   u\to w.
   \tag{TC}
   \]

In a four-term avoider, the eventual clause becomes
\[
b+d\to b+2d
\quad\text{or}\quad
b+2d\to b+3d
\tag{GC}
\]
for every fixed \(b\) and all sufficiently large \(d\).

Thus the original order problem implies the existence of a locally finite, transitively closed forward graph satisfying a dense family of overlapping affine edge-cover clauses.

#### Key lemma needed

> **Affine descent-graph impossibility theorem.**  
> No directed graph on \(\mathbb N\) can simultaneously satisfy:
> - all edges point from smaller to larger integers;
> - every vertex has finite outdegree;
> - the graph satisfies (TC);
> - for every \(b\), clause (GC) holds for all sufficiently large \(d\).

This theorem would immediately prove the Erdős problem affirmatively.

#### Why it might work

This formulation discards most of the total order and isolates precisely the simultaneous overlap that blocked the comparison-coloring route.

Because of transitive closure, any directed path
\[
u_0\to u_1\to\cdots\to u_k
\]
makes every later \(u_j\) an out-neighbor of \(u_0\). Thus finite outdegree bounds the depth below each vertex. One may define a finite height
\[
h(u)=\max\{\text{length of a directed path starting at }u\}.
\]
Every edge strictly decreases \(h\).

Clause (GC) therefore forces, for every \(b\) and all large \(d\),
\[
h(b+d)>h(b+2d)
\quad\text{or}\quad
h(b+2d)>h(b+3d).
\]
The problem becomes an additive theorem about a pointwise finite height function together with a sparse transitive edge relation. This may be accessible through minimal-height arguments, affine Ramsey theory with bounded branching, or a rank-reduction induction.

#### Most likely failure point

The graph theorem may be false without additional properties inherited from a full permutation. A carefully designed well-founded graph might cover all affine clauses while distributing edges among sources so that every outdegree remains finite.

Also, replacing actual edges by height inequalities loses information: \(h(v)<h(u)\) does not imply \(u\to v\).

#### Quick blocking test

Use SAT to search on \([N]\) for graphs satisfying:

- forward edges only;
- transitive closure;
- fixed outdegree bounds \(\Delta_u\);
- all clauses (GC) in a large interior range.

Minimize the maximum path height. If scalable examples appear, inspect whether they can be extended to an infinite locally finite graph. If small unsatisfiable cores repeatedly involve overlapping affine rays rather than boundary effects, they may suggest the missing theorem.

This route should not revert to arbitrary pair-coloring Ramsey theory; the finite-outdegree and transitive-closure conditions are the entire point.

---

### New Route D: Disproof via invertible finite-state ranking transducers

#### Core mechanism

Search for an explicit bijection
\[
F:\mathbb N\to\mathbb N
\]
and set
\[
p(n)=F(n).
\]
Then the desired counterexample condition becomes
\[
F(a),F(a+d),F(a+2d),F(a+3d)
\]
never strictly increasing and never strictly decreasing.

Previous digitwise maps fail because they do not react to carry states. Replace them by a genuinely stateful, prefix-dependent, invertible transducer over base \(b\).

A promising restricted class is:

- canonical base-\(b\) words;
- a finite-state synchronous Mealy transducer;
- state-dependent digit permutations;
- a certified invertibility condition;
- preservation of canonical length classes or another mechanism guaranteeing a bijection of \(\mathbb N\).

Because \(F\) itself is a bijection, order type \(\omega\) is automatic.

#### Key lemma needed

For disproof, one needs to find a transducer \(F\) for which the finite automaton recognizing monotone four-term progressions has empty language.

For an affirmative no-go theorem about this construction class, one would instead prove:

> Every invertible finite-state base-\(b\) ranking transducer admits \(a,d\ge1\) for which the four outputs are monotone.

The primary aim of this route is disproof, but a no-go theorem would sharply narrow the construction space.

#### Why it might work

The LSB order supplies a nearly perfect local scaffold: it makes every three-term midpoint extremal. Its sole fatal defect is non-\(\omega\) order type. A stateful transducer may preserve the LSB comparison rule on most carry states while introducing a proper global rank that schedules every value after finitely many predecessors.

Unlike append-only repair, the transducer can reserve future values through its state and alter comparisons before dangerous triples become permanently fixed.

Universal verification is finite-state:

- base-\(b\) addition has finitely many carry states;
- \(a+td\) for \(t=0,1,2,3\) can be processed in parallel;
- transducer states are finite;
- output comparison can be tracked by the last most-significant differing digit;
- existence of a monotone AP reduces to automaton nonemptiness.

#### Most likely failure point

Finite-state well-orders may be too rigid. Pumping could force repeated carry states and thereby produce an explicit monotone four-term progression in every such system. Length-preserving bijections are especially vulnerable because large-scale numerical order remains visible.

There are also technical traps involving leading zeros, canonical representations, and whether a locally invertible Mealy machine induces a genuine bijection on canonical finite words.

#### Quick blocking test

Enumerate invertible base-\(2\) and base-\(4\) transducers with small state sets.

For each candidate:

1. certify bijectivity;
2. build the four-copy carry product automaton;
3. search for increasing or decreasing outputs;
4. record the shortest witness and its carry-state cycle.

The known coordinatewise digit maps must fail immediately and serve as mandatory regression tests. If every small automaton fails through the same pumpable cycle, attempt to prove a general pumping theorem. If a candidate survives, independently verify it with exhaustive bounded testing and a formal automaton-emptiness certificate.

---

## 8. Verdict on difficulty

This is a genuinely difficult, long-standing boundary problem. DEGS settled lengths \(3\) and \(5\) in opposite directions in 1977, leaving exactly length \(4\). The obstruction is not merely quantitative:

- every finite interval admits an order avoiding even monotone three-term progressions;
- compactness produces the wrong type of infinite order;
- the crucial permutation condition is the noncompact requirement that every fixed value have finitely many predecessors;
- local extremum counts can be saturated by the LSB order;
- generic additive-combinatorial methods only handle the \(U^3\)-uniform case;
- single-ray record sets may be arbitrarily sparse;
- direct dyadic iteration does not align scales;
- simple hierarchical constructions are destroyed by carries.

No equivalence to a famous open conjecture is known, and there is no reason to claim that solving it would settle Szemerédi, Green–Tao, or a standard inverse-theorem conjecture. Nevertheless, the missing ingredient appears to require a new principle coupling additive structure with well-founded order or bounded predecessor sets.

The most focused affirmative targets are now:

1. a divisor-coherent simultaneous record theorem;
2. a fixed-anchor rank-escape theorem for finite avoiders;
3. an impossibility theorem for locally finite transitive affine descent graphs.

The most concrete disproof program is:

4. a stateful invertible finite-state repair of the LSB hierarchy, verified by exhaustive carry automata.

A successful Round 2 should prioritize exact finite tests of these proposed key lemmas before investing in broad generalizations.