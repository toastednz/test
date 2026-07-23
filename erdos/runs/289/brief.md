# Problem brief: Erdős Problem #289

## 1. Precise statement

Let  
\[
\mathbb N=\{1,2,3,\dots\}.
\]
For integers \(1\le a\le b\), define the finite integer interval
\[
[a,b]_{\mathbb N}:=\{a,a+1,\dots,b\},
\]
with cardinality \(b-a+1\). Write
\[
H_0:=0,\qquad H_m:=\sum_{n=1}^m\frac1n,
\]
so that the reciprocal sum of an interval is
\[
w(a,b):=\sum_{n=a}^b\frac1n=H_b-H_{a-1}.
\]

For \(k\ge1\), let \(P(k)\) be the following assertion:

> There exist integers
> \[
> 1\le a_1\le b_1<a_2\le b_2<\cdots<a_k\le b_k
> \]
> such that
> \[
> b_i-a_i+1\ge2\qquad(1\le i\le k),
> \]
> \[
> a_{i+1}\ge b_i+2\qquad(1\le i<k),
> \]
> and
> \[
> \sum_{i=1}^k\sum_{n=a_i}^{b_i}\frac1n=1.
> \]

The separation condition \(a_{i+1}\ge b_i+2\) says that the intervals are disjoint and that at least one integer is omitted between successive intervals. Equivalently, the selected denominator set
\[
S:=\bigcup_{i=1}^k[a_i,b_i]_{\mathbb N}
\]
has exactly \(k\) maximal runs of consecutive integers, every run having length at least \(2\).

The problem asks whether
\[
\boxed{\exists K\in\mathbb N\ \forall k\ge K,\quad P(k).}
\]

The labels of the intervals are immaterial; they may always be reordered by increasing left endpoint. Pairwise disjointness already implies that the intervals are distinct, so “distinct” is formally redundant under the standard reading.

Any solution automatically has \(a_1\ge2\): if \(1\in S\), then the interval containing \(1\) has length at least \(2\), and its contribution is at least \(1+1/2>1\).

### Possible ambiguity

The standard reading of “not overlapping or adjacent” is pairwise nonoverlap with at least one omitted integer between intervals, as formalized above. If “adjacent” were interpreted differently, the problem would change substantially. In particular, merely disjoint intervals could always be merged when adjacent, changing the number of intervals. The formulation above is the natural interpretation indicated by the database commentary.

The published Erdős–Graham version reportedly omitted these separation and distinctness conditions. The database problem should therefore be treated as a strengthened, presumably intended version, not automatically as the literal statement in the original source.

---

## 2. What counts as a solution

### Complete proof

A complete affirmative solution must prove the existence of a fixed integer \(K\) such that, for every integer \(k\ge K\), a finite collection of exactly \(k\) intervals satisfying all the conditions exists.

A proof may be:

- **Explicitly constructive:** give formulas or an algorithm producing the endpoints for every \(k\ge K\), together with proofs that all endpoints are integers, all intervals have length at least \(2\), the gaps are nonempty, and the reciprocal sum is exactly \(1\).
- **Recursive:** give finitely many seed representations and rigorously valid transformations that generate every sufficiently large interval count.
- **Nonconstructive:** prove existence for every \(k\ge K\) without giving efficient endpoints, provided exact finiteness and exact equality are established.

If using count-increasing gadgets, it is not enough to produce arbitrarily many values of \(k\). One must prove that the attainable increments generate all sufficiently large integers, for example by producing reusable increments \(d_1,\dots,d_r\) with
\[
\gcd(d_1,\dots,d_r)=1
\]
and proving the required compatibility and seed conditions.

No determination of the least possible \(K\) is required.

### Complete disproof

The logical negation is
\[
\forall K\in\mathbb N\ \exists k\ge K\quad \neg P(k).
\]
Thus a disproof must establish that there are arbitrarily large values of \(k\) for which no valid representation exists.

Sufficient forms of disproof include:

- an explicit unbounded sequence \(k_1<k_2<\cdots\) such that \(P(k_j)\) fails for every \(j\);
- an infinite arithmetic progression or other unbounded class of forbidden \(k\);
- a theorem giving an absolute upper bound on the possible number of intervals;
- a structural invariant implying that infinitely many interval counts are impossible.

A single exceptional value of \(k\), even a very large one, does **not** disprove an eventual statement.

To verify a proposed construction for a particular \(k\), one must check:

1. \(a_i,b_i\in\mathbb N\);
2. \(a_i<b_i\), equivalently \(|I_i|\ge2\);
3. after ordering, \(a_{i+1}\ge b_i+2\);
4. exact equality
   \[
   \sum_i(H_{b_i}-H_{a_i-1})=1.
   \]

For exact verification, let
\[
L=\operatorname{lcm}\{n:n\in S\}.
\]
Then the equality is equivalent to the integer identity
\[
\sum_{n\in S}\frac{L}{n}=L.
\]

To verify a claimed nonexistence result for a particular \(k\), a bounded computer search is insufficient unless accompanied by a proved bound on all possible endpoints. There is no evident a priori upper bound on \(\max S\) in terms of \(k\).

---

## 3. What does not count

The following do not resolve the problem:

- representations for only finitely many \(k\);
- representations for arbitrarily large \(k\) but not all sufficiently large \(k\);
- representations for all \(k\) in one progression, unless the complement is proved finite;
- a representation of a target other than \(1\), such as the supplied representation of \(2\);
- approximate identities
  \[
  \left|\sum_{n\in S}\frac1n-1\right|<\varepsilon;
  \]
- infinite series whose sum is \(1\); every interval collection must be finite;
- constructions allowing singleton intervals;
- constructions allowing repeated, overlapping, or adjacent intervals;
- ordinary Egyptian-fraction expansions with isolated denominators;
- results restricted to \(k\le K_0\), or searches with all endpoints bounded by \(N\), without a global endpoint bound;
- conditional results depending on an unproved conjecture;
- heuristic density, random-subset, or floating-point evidence;
- proving the assertion only after replacing the target \(1\) by another rational;
- decomposing a long interval into adjacent smaller intervals and counting them separately: adjacent intervals are forbidden and in any case form one maximal run;
- a gadget that can be applied only once, unless its attainable counts and all later compatibility conditions cover every sufficiently large \(k\).

A theorem for the stronger special case in which every interval has length exactly \(2\) would solve the problem if it covered every sufficiently large \(k\). Partial results in that special case do not.

---

## 4. Known results and context

### 4.1 Origin and unrestricted variant

According to the database commentary, Erdős and Graham posed the question in [ErGr80] without explicitly requiring the intervals to be distinct, nonoverlapping, and nonadjacent. A comment by Kovac gives an easy argument for the version without those restrictions. The current database problem should therefore be understood as the natural strengthened form.

The unrestricted problem does not capture the central difficulty here: under the present conditions every denominator has coefficient either \(0\) or \(1\), and the support must consist of separated runs of length at least \(2\).

### 4.2 The Hickerson–Montgomery example

The supplied example is
\[
2=\sum_{i=1}^5\sum_{n\in I_i}\frac1n
\]
with
\[
I_1=[2,7],\quad I_2=[9,10],\quad I_3=[17,18],\quad
I_4=[34,35],\quad I_5=[84,85].
\]
These intervals meet all the geometric restrictions. Their block sums are
\[
\frac{223}{140},\quad \frac{19}{90},\quad \frac{35}{306},
\quad\frac{69}{1190},\quad\frac{169}{7140}.
\]
With common denominator \(21420\), the corresponding numerators are
\[
34119,\ 4522,\ 2450,\ 1242,\ 507,
\]
whose sum is
\[
42840=2\cdot21420.
\]

This is evidence that exact integer harmonic sums can arise from several separated blocks. It gives no direct representation of \(1\). In particular, doubling all denominators does not simply halve an interval sum, because the doubled denominators are no longer consecutive.

### 4.3 Kürschák’s theorem and the case \(k=1\)

A classical theorem of Kürschák states that a nontrivial sum of reciprocals of consecutive positive integers is not an integer. In particular,
\[
\sum_{n=a}^b\frac1n\notin\mathbb Z
\qquad\text{when }a<b.
\]
Thus \(P(1)\) is false.

The standard proof uses \(2\)-adic valuation. In any finite interval of at least two consecutive integers, there is a unique integer having maximal \(2\)-adic valuation. After multiplying the reciprocal sum by the least common multiple of the denominators, the term coming from that integer is odd and every other term is even. Hence the resulting numerator is odd, whereas an integral value would require divisibility by the full power of \(2\) in the least common multiple.

This settles only \(k=1\); it has no bearing on the eventual quantifier.

### 4.4 Ordinary Egyptian fractions

The Sylvester greedy algorithm and related splitting identities show that every positive rational has a finite Egyptian-fraction expansion into distinct unit fractions. For example,
\[
\frac1n=\frac1{n+1}+\frac1{n(n+1)}
\]
increases the number of terms by one.

These results are relevant as a source of exact rational identities, but they do not impose the consecutive-run condition. Isolated denominators, even if distinct, do not form admissible intervals of length at least \(2\).

### 4.5 Elementary local congruence condition

Let \(S\) be any finite denominator set satisfying
\[
\sum_{n\in S}\frac1n=m\in\mathbb Z,
\]
and let \(p\) be a prime dividing some member of \(S\). Put
\[
e=\max_{n\in S}v_p(n).
\]
For the denominators with \(v_p(n)=e\), write \(n=p^e u_n\), where \(p\nmid u_n\). Multiplication by \(L=\operatorname{lcm}(S)\) and reduction modulo \(p\) gives the necessary condition
\[
\sum_{\substack{n\in S\\v_p(n)=e}}u_n^{-1}\equiv0\pmod p.
\]
For \(p=2\), every \(u_n\) is odd, so this reduces to:

> The number of selected denominators having maximal \(2\)-adic valuation must be even.

This generalizes the obstruction behind Kürschák’s theorem. It is useful for pruning and possibly for disproof, but it is not presently strong enough to settle the problem.

### 4.6 What is actually settled

From the supplied information and the elementary facts above:

- \(k=1\) is impossible.
- Five separated admissible intervals can have reciprocal sum \(2\).
- The target-\(1\), eventual-\(k\) problem remains open.
- No equivalence with a standard famous conjecture is known from the supplied context.

---

## 5. Traps and edge cases

1. **The quantifier is eventual, not infinite.**  
   Producing infinitely many attainable values of \(k\) does not prove cofinite attainability.

2. **A finite counterexample does not disprove the statement.**  
   One needs arbitrarily large forbidden \(k\).

3. **Intervals are maximal runs.**  
   If \([a,b]\) and \([b+1,c]\) are both selected, they are adjacent and must be regarded as the single interval \([a,c]\), so they cannot contribute two to \(k\).

4. **There must be an omitted integer between successive intervals.**  
   The exact condition is
   \[
   a_{i+1}\ge b_i+2,
   \]
   not merely \(a_{i+1}>b_i\).

5. **Long intervals cannot be reduced to dimers without loss.**  
   Splitting a long run into shorter consecutive runs creates forbidden adjacency; inserting gaps changes the sum.

6. **The interval count is not the unit-fraction term count.**  
   The number of reciprocal terms is
   \[
   |S|=\sum_i(b_i-a_i+1)\ge2k,
   \]
   and may be much larger than \(2k\).

7. **The denominator \(1\) cannot occur.**  
   Any admissible interval containing \(1\) contributes more than \(1\).

8. **No scaling symmetry is available.**  
   Replacing every denominator \(n\) by \(qn\) destroys consecutiveness. Thus an identity for target \(2\) cannot simply be scaled to one for target \(1\).

9. **Harmonic divergence is not exact representability.**  
   The divergence of \(\sum1/n\) and the smallness of distant blocks can give approximation, but not exact equality by finitely many blocks.

10. **Real-analytic arguments miss arithmetic obstructions.**  
    The sums lie in highly structured rational lattices. Continuity or density alone cannot force exact equality.

11. **Floating-point verification is unsafe.**  
    Exact rational arithmetic or an integer identity after clearing denominators is mandatory.

12. **Bounded search cannot certify global nonexistence.**  
    A representation for fixed \(k\) could use extremely large denominators.

13. **Prime-valuation arguments must account for cancellation among several maximal terms.**  
    The unique-maximal-term proof works for one interval, but several separated intervals can contain several maximal-valuation denominators whose residues cancel.

14. **Reusing an identity may violate separation.**  
    A replacement gadget valid in isolation may overlap an existing interval or become adjacent to one after iteration.

15. **“Distinct” cannot be implemented by repeated copies with multiplicity.**  
    The restricted sum has coefficient \(1\) on each selected denominator.

---

## 6. Verification hooks

### 6.1 Exact verification of a proposed construction

Given endpoints \((a_i,b_i)\):

1. sort by \(a_i\);
2. check \(a_i<b_i\);
3. check \(a_{i+1}\ge b_i+2\);
4. form
   \[
   S=\bigcup_i\{a_i,\dots,b_i\};
   \]
5. compute \(L=\operatorname{lcm}(S)\);
6. verify
   \[
   \sum_{n\in S}L/n=L.
   \]

A language with arbitrary-precision integers is sufficient. Python’s `fractions.Fraction` is also adequate for moderate endpoints.

### 6.2 Exact bounded search as a binary integer program

Fix an endpoint bound \(N\). Introduce binary variables
\[
x_n=\mathbf 1_{\{n\in S\}},\qquad 1\le n\le N,
\]
with boundary values \(x_0=x_{N+1}=0\).

To forbid runs of length \(1\), impose
\[
x_n\le x_{n-1}+x_{n+1}\qquad(1\le n\le N).
\]

Introduce binary run-start variables \(y_n\), constrained by
\[
y_n\ge x_n-x_{n-1},\qquad
y_n\le x_n,\qquad
y_n\le1-x_{n-1}.
\]
Then
\[
\sum_{n=1}^N y_n=k
\]
forces exactly \(k\) maximal selected runs. Set \(x_1=0\).

Let
\[
L_N=\operatorname{lcm}(1,2,\dots,N).
\]
The exact target equation is
\[
\sum_{n=2}^N x_n\frac{L_N}{n}=L_N.
\]

This is an exact pseudo-Boolean or integer-linear formulation, although the coefficients are very large. Modular reductions can be added before attempting the full equality.

### 6.3 Modular pruning

For every prime \(p\le N\), determine the maximal \(p\)-adic valuation among selected denominators. Conditional constraints can enforce
\[
\sum_{v_p(n)=e}(n/p^e)^{-1}\equiv0\pmod p.
\]
At minimum, for \(p=2\), require an even number of selected denominators at maximal \(2\)-adic valuation.

Higher congruences modulo \(p^r\) can be obtained by retaining more terms after clearing denominators.

### 6.4 Meet-in-the-middle search over blocks

Precompute every admissible block
\[
B=[a,b],\qquad 2\le a<b\le N,
\]
with exact weight
\[
w(B)=H_b-H_{a-1}.
\]
Store weights as reduced numerator-denominator pairs or as integers over \(L_N\).

Build a compatibility graph in which two blocks are adjacent when they are separated by at least one omitted integer. Then search for compatible \(k\)-tuples with weight \(1\), using:

- meet-in-the-middle hashing of partial sums;
- branch-and-bound using positivity;
- modular fingerprints before exact comparison;
- canonical ordering by left endpoint.

### 6.5 Search for replacement gadgets

Enumerate identities of the form
\[
w(A,B)=\sum_{j=1}^r w(C_j,D_j),
\]
where
\[
B+2\le C_1\le D_1<C_2\le\cdots\le D_r
\]
and all right-side intervals have nonempty gaps. Hash sums of compatible pairs or triples of blocks to find exact identities.

The most valuable gadgets are parameterized families or gadgets that leave a “marked” block of the same type, allowing iteration.

### 6.6 Restricted dimer search

The length-\(2\) block beginning at \(n\) has weight
\[
d(n)=\frac1n+\frac1{n+1}
=\frac{2n+1}{n(n+1)}.
\]
A dimer-only solution requires
\[
\sum_{i=1}^k d(n_i)=1,\qquad n_{i+1}\ge n_i+3.
\]
This is a clean testbed for algebraic identities and modular obstructions. Failure in the dimer-only model does not imply failure of the original problem.

### 6.7 Sanity checks for claimed invariants

Every proposed necessary congruence for integer-valued separated block sums should first be tested on the Hickerson–Montgomery target-\(2\) example. Since the target is an integer, most least-common-multiple congruences apply equally to target \(1\) and target \(2\). Any invariant excluding that example is incorrectly formulated.

---

## 7. Attack routes

### Route 1: Reusable exact replacement gadgets

**Core mechanism.**  
Begin with one or finitely many seed representations and replace selected blocks by several later, separated blocks of exactly the same total weight. If replacement increases the interval count in controllable increments, numerical-semigroup arguments could cover every sufficiently large \(k\).

**Key lemma needed.**  
Construct one or more identities
\[
w(A,B)=\sum_{j=1}^r w(C_j,D_j)
\]
with all new blocks strictly to the right and mutually separated, together with enough location freedom to avoid any finite forbidden set. Ideally the replacement preserves a marked block to which the gadget can be applied again.

If reusable gadgets have count increments \(d_1,\dots,d_t\) with
\[
\gcd(d_1,\dots,d_t)=1,
\]
and suitable seeds cover the finitely many residue classes, then all sufficiently large counts follow.

**Why it might work.**  
Ordinary Egyptian fractions have abundant exact splitting identities. Harmonic tails are divergent, so there is ample real mass far to the right; the problem is to make that mass exact and run-structured.

**Most likely failure point.**  
Consecutive harmonic blocks do not enjoy a useful dilation symmetry. A sporadic identity may not move to arbitrary locations, and iteration may create overlaps or adjacency. Positivity also prevents easy telescoping by cancellation.

**Quick blockage test.**  
Perform exact meet-in-the-middle searches for one-block-to-two-block and one-block-to-three-block identities with the new blocks entirely to the right. Check whether discovered identities occur in parameterized families or are isolated accidents.

---

### Route 2: Global common-denominator subset-sum construction

**Core mechanism.**  
Fix a large \(N\), let \(L_N=\operatorname{lcm}(1,\dots,N)\), and seek a run-structured subset \(S\subseteq[2,N]\) satisfying the integer partition
\[
\sum_{n\in S}\frac{L_N}{n}=L_N.
\]
This converts the problem into a constrained subset-sum problem with highly structured divisor weights.

**Key lemma needed.**  
Prove that for every sufficiently large \(k\), some \(N=N(k)\) admits a subset \(S\subseteq[2,N]\) with exactly \(k\) runs, every run of length at least \(2\), and total weight \(L_N\).

A useful intermediate theorem would show that a large collection of separated candidate blocks has subset sums containing a long interval of multiples of some controlled modulus.

**Why it might work.**  
The weights \(L_N/n\) have extensive divisibility structure, and the total available harmonic mass is much larger than \(1\). Additive-combinatorial methods, zero-sum theorems, or carefully chosen divisor-rich windows may create exact coverage.

**Most likely failure point.**  
Modular coverage does not imply equality to exactly \(L_N\), and the weights vary greatly in size. The run constraints create substantial dependence between variables. The growing least common multiple prevents a straightforward limiting argument.

**Quick blockage test.**  
Solve the exact ILP for increasing \(N\) and \(k\), recording the smallest \(N\) found. Test whether attainable scaled sums fill intervals or remain arithmetically sparse. Examine coverage modulo small primes before enforcing exact equality.

---

### Route 3: Blockification of ordinary Egyptian fractions

**Core mechanism.**  
Start from an exact Egyptian-fraction expansion of \(1\), then replace each isolated unit fraction by a collection of admissible harmonic blocks placed far apart.

**Key lemma needed.**  
A strong blockification theorem such as:

> For every sufficiently suitable denominator \(q\), every finite forbidden set \(F\), and every sufficiently large admissible block count \(r\), the unit fraction \(1/q\) is a sum of \(r\) pairwise separated intervals of length at least \(2\), all lying beyond \(F\).

A weaker version for a specially chosen infinite family of \(q\) could suffice if an Egyptian expansion of \(1\) can be arranged using only that family.

**Why it might work.**  
Egyptian-fraction identities already provide exactness and flexible term counts. Denominators can often be pushed arbitrarily far out by repeated splitting, potentially creating room for local blockification.

**Most likely failure point.**  
There is no obvious way to “thicken” a singleton denominator into consecutive pairs while preserving the exact value. Scaling an identity does not preserve consecutive intervals. The desired blockification lemma may be essentially as hard as the original problem.

**Quick blockage test.**  
For small \(q\), run bounded exact searches for
\[
\frac1q=\sum_j w(a_j,b_j),
\]
with all \(a_j\) above a specified threshold. Look for formulas in \(q\), not merely isolated examples. In particular, test whether dimer-only blockifications exist for a structured family of \(q\).

---

### Route 4: Analytic reservoir plus exact arithmetic completion

**Core mechanism.**  
Use many remote, very small blocks as a flexible reservoir. First choose most of the \(k\) blocks so that their sum lies just below \(1\); then represent the small rational residual using a bounded correction library in a later denominator range.

**Key lemma needed.**  
An exact completion theorem of the form:

> For rationals \(r\) in a specified interval and denominator lattice, every such \(r\) can be represented by at most \(C\) separated harmonic blocks in a controlled later range, with the number of correction blocks selectable from a fixed finite set.

Alternatively, prove that scaled sums of compatible blocks in a slab contain every lattice point in a nontrivial interval.

**Why it might work.**  
Far-out block weights tend to zero, while the total harmonic mass of a sufficiently long slab can be prescribed on a logarithmic scale. This creates strong approximation flexibility and may allow a local central-limit or additive-basis phenomenon after clearing denominators.

**Most likely failure point.**  
Approximation and density naturally produce infinite subsums or small error, not exact finite equality. The denominator of the residual may acquire new prime powers that the later correction blocks cannot match.

**Quick blockage test.**  
For consecutive slabs \([M,cM]\), compute exact scaled subset sums of a sparse compatible block family. Measure whether they cover intervals of lattice values or have persistent congruence holes. Track residual denominators and prime-power obstructions explicitly.

---

### Route 5: \(p\)-adic obstruction and disproof

**Core mechanism.**  
Generalize Kürschák’s unique-maximal-valuation argument from one interval to a union of separated intervals. Attempt to prove that, for infinitely many \(k\), some prime necessarily yields a noncancellable maximal-valuation contribution.

**Key lemma needed.**  
A structural statement such as:

> For every union of \(k\) separated runs of length at least \(2\), with \(k\) in some unbounded class, there exists a prime \(p\) for which
> \[
> \sum_{\substack{n\in S\\v_p(n)=e}}
> (n/p^e)^{-1}\not\equiv0\pmod p,
> \qquad e=\max_{n\in S}v_p(n).
> \]

Any such lemma for an unbounded family of \(k\) would disprove the conjecture.

**Why it might work.**  
For a single interval, the \(2\)-adic argument is decisive. Separated runs may force isolated large prime powers or primes occurring in only one strategically located denominator. The gaps could conceivably strengthen rather than weaken valuation rigidity.

**Most likely failure point.**  
Endpoints are completely free. Different intervals can be arranged so that maximal-valuation denominators occur in cancelling pairs or larger zero-sum configurations. The interval count \(k\) alone may impose too little information on these residues.

**Quick blockage test.**  
Ignore the exact sum initially and search for run-structured sets satisfying all maximal-valuation congruences for primes up to a bound. If every large \(k\) quickly admits many such patterns, a purely first-order \(p\)-adic obstruction is unlikely to suffice. Also test every proposed invariant against the known target-\(2\) example.

---

## 8. Verdict on difficulty

This is a difficult exact additive–Diophantine problem. The unrestricted Egyptian-fraction background is comparatively easy; nearly all of the difficulty comes from simultaneously requiring:

- coefficients \(0\) or \(1\);
- support consisting of exactly \(k\) separated consecutive runs;
- every run having length at least \(2\);
- exact equality to \(1\);
- and coverage of every sufficiently large \(k\), not merely infinitely many counts.

The problem appears to require either a highly nontrivial exact identity mechanism or a new structural obstruction. Approximation methods alone are unlikely to settle it.

No known equivalence to a famous conjecture such as the Riemann hypothesis, abc, or Erdős–Straus is indicated by the supplied material, and none should be asserted. Nevertheless, the problem has reportedly remained open since the Erdős–Graham 1980 context. The main realistic targets for automated research are:

1. discover and prove reusable block-splitting identities;
2. find a direct common-denominator construction with count control;
3. establish a strong blockification lemma for unit fractions; or
4. uncover a genuinely global \(p\)-adic obstruction producing infinitely many forbidden \(k\).

A bounded search may be highly valuable for discovering identities and falsifying proposed invariants, but without a parameterized theorem or endpoint bound it cannot by itself resolve the problem.