# Round 2 Problem Brief: Erdős Problem #289

## 1. Precise statement

Let
\[
\mathbb N=\{1,2,3,\dots\}.
\]
For integers \(1\le a\le b\), write
\[
[a,b]_{\mathbb N}:=\{a,a+1,\dots,b\},
\qquad
w(a,b):=\sum_{n=a}^b \frac1n.
\]

A family of intervals \(I_1,\dots,I_k\) is **admissible** if, after relabeling them so that
\[
I_i=[a_i,b_i]_{\mathbb N},\qquad a_1<a_2<\cdots<a_k,
\]
the following hold:

1. **Minimum length**
   \[
   b_i-a_i+1\ge 2\qquad(1\le i\le k).
   \]
2. **Pairwise disjoint and nonadjacent**
   \[
   b_i+1<a_{i+1}\qquad(1\le i<k).
   \]
   Thus at least one integer is omitted between consecutive intervals.

The problem asks whether
\[
\boxed{
\exists K\in\mathbb N\ \forall k\in\mathbb N,\ k\ge K\
\exists\text{ an admissible family }I_1,\dots,I_k
\text{ such that }
\sum_{i=1}^k\sum_{n\in I_i}\frac1n=1.
}
\]

Equivalently, does there exist \(K\) such that for every \(k\ge K\) there is a finite set \(S\subset\{2,3,\dots\}\) satisfying

- \(S\) has exactly \(k\) maximal runs of consecutive integers;
- every maximal run has length at least \(2\);
- \(\sum_{n\in S}1/n=1\)?

The equivalence uses the fact that the admissible intervals must be precisely the maximal consecutive components of their union. No solution can contain \(1\), since an interval containing \(1\) has at least two terms and hence reciprocal sum \(>1\).

### Ambiguity in the historical formulation

Erdős and Graham apparently stated the question without explicitly requiring the intervals to be distinct, disjoint, and nonadjacent. The database adopts the natural strengthened interpretation above. Without these restrictions, the commentary reports that the problem is easy. This brief concerns only the strengthened database formulation.

The word “distinct” is formally redundant once pairwise disjointness is imposed.

---

## 2. What counts as a solution

### 2.1 Complete proof

A complete affirmative solution must prove the full eventual quantifier:
\[
\exists K\ \forall k\ge K\ \exists\text{ an exact admissible representation of }1.
\]

It is enough to give either:

- an explicit algorithm constructing the intervals from \(k\), with a proof that it works for every \(k\ge K\); or
- a nonconstructive existence proof valid for every sufficiently large \(k\).

For every constructed family, the proof must establish:

1. all endpoints are positive integers;
2. every interval has length at least \(2\);
3. after sorting, \(b_i+1<a_{i+1}\);
4. the number of maximal runs is exactly \(k\), after merging any accidentally adjacent pieces;
5. the reciprocal identity is exact over \(\mathbb Q\), not merely numerical.

A construction valid only for infinitely many \(k\), or only for \(k\) in one arithmetic progression, is insufficient unless the omitted values are subsequently covered.

### 2.2 Complete disproof

The negation is
\[
\forall K\in\mathbb N\ \exists k\ge K
\quad
\text{such that no admissible \(k\)-interval representation of \(1\) exists.}
\]

Thus a disproof must produce an unbounded set of bad values of \(k\). For example, it would suffice to prove that:

- no solution exists for every \(k\) in some infinite sequence \(k_j\to\infty\);
- every solution has at most \(C\) intervals;
- every solution has its number of intervals in a proper noncofinite set, such as one or more forbidden residue classes.

A single large \(k\) with no solution does **not** disprove the statement.

Because denominators are unbounded, a finite search up to \(N\) cannot certify that a given \(k\) is impossible unless accompanied by a theorem bounding the largest denominator of any hypothetical \(k\)-interval solution. A verifiable computational disproof would therefore need:

1. a rigorous bound \(N\le B(k)\) for the bad values under consideration;
2. an exhaustive exact search up to \(B(k)\); and
3. an unbounded family of such bad \(k\), or a general obstruction theorem.

---

## 3. What does not count

The following do not settle the problem:

- one representation with a very large number of intervals;
- representations for infinitely many but not all sufficiently large \(k\);
- an asymptotic estimate
  \[
  \sum_{i,n\in I_i}\frac1n=1+o(1);
  \]
- exact sums \(1\pm\varepsilon_k\) with \(\varepsilon_k\ne0\), however small;
- an exact infinite expansion of \(1\), since the required family is finite;
- representations of \(2\) or any other integer;
- allowing singleton intervals, overlaps, repetitions, or adjacent intervals counted separately;
- signed reciprocal identities, integer linear combinations, or identities using a denominator more than once;
- a gcd or lattice-generation argument using subtraction;
- equal-weight block configurations whose run counts differ, unless one side can actually be replaced inside a target-\(1\) representation;
- a conditional result depending on an unproved completion theorem;
- a fixed-\(k\) search with an arbitrary denominator cutoff;
- failure of a dimer-only construction: intervals of length \(>2\) remain available;
- solving the historically weaker unrestricted formulation.

---

## 4. Known results and context

### 4.1 Historical example representing \(2\)

Hickerson and Montgomery, in their solution of Hahn’s AMS Monthly problem E2689, found
\[
2=w(2,7)+w(9,10)+w(17,18)+w(34,35)+w(84,85).
\]

For convenience, define the dimer weight
\[
d(q):=\frac1q+\frac1{q+1}=w(q,q+1).
\]

Since
\[
\frac12+\frac13+\frac16=1,
\]
the example gives the exact defective target-\(1\) identity
\[
\boxed{
1=d(4)+\frac17+d(9)+d(17)+d(34)+d(84).
}
\]
The only illegal component is the singleton \(1/7\).

It also yields
\[
\boxed{
d(4)+d(9)+d(17)+d(34)+\frac1{85}
=d(2)+\frac1{84}.
}
\]
Equivalently,
\[
d(4)+d(9)+d(17)+d(34)
=d(2)+\frac1{84}-\frac1{85}
=\frac56+\frac1{7140}.
\]

Consequently,
\[
\boxed{
w(4,6)+w(9,10)+w(17,18)+w(34,35)
=1+\frac1{7140}.
}
\]
This is a valid four-interval near-solution.

### 4.2 A matching local gap slide

Let
\[
A=[82,84]\cup[86,87],
\qquad
B=[82,83]\cup[85,87].
\]
Both supports consist of two legal runs, and
\[
w(A)-w(B)=\frac1{84}-\frac1{85}=\frac1{7140}.
\]

Thus replacing \(A\) by \(B\) lowers a reciprocal sum by exactly the error in the four-block near-solution. The immediate argument nevertheless fails because the known near-solution does not contain \(A\). Appending \(A\) and then replacing it by \(B\) adds the positive weight \(w(B)\), rather than correcting the target.

### 4.3 Exact count-changing block gadget

The previous round proved
\[
\begin{aligned}
&w(4,10)+w(17,18)+w(34,35)+w(82,83)+w(85,87)\\
&\qquad=
w(2,3)+w(6,8)+w(82,84)+w(86,87).
\end{aligned}
\]
The left side has five admissible intervals and the right side four. Hence, when the right side occurs compatibly inside a representation, it can be replaced by the left side and the run count increases by one.

More generally, a padding lemma was proved:

> If two finite, disjoint Egyptian-fraction sets have equal reciprocal sums and their term counts differ by \(m\), then, beyond any prescribed cutoff, one can construct two admissible block configurations of equal weight whose interval counts differ by \(m\).

Applied to
\[
\frac1{2s}
=\sum_{j=1}^m\frac1{3^js}+\frac1{2\cdot3^m s},
\]
this gives arbitrarily remote equal-weight admissible configurations with any prescribed run-count difference \(m\).

This completely removes any simple global congruence obstruction on run-count differences between equal-weight configurations. It does **not** solve the problem, because an equal-weight identity is usable only when one side already appears in a target-\(1\) representation.

### 4.4 Finite-support counting and the exact lattice formulation

Let \(N\ge2\). The number of subsets \(S\subset[2,N]\) having exactly \(k\) maximal runs, all of length at least \(2\), is
\[
\boxed{\binom{N-k}{2k}},
\]
with the binomial coefficient understood as zero when \(N<3k\).

This follows by writing the \(k\) run lengths as \(2+\ell_i\), the \(k-1\) internal gaps as \(1+g_i\), and using two unrestricted outer gaps.

Let
\[
L_N:=\operatorname{lcm}(1,2,\dots,N).
\]
For \(S\subset[2,N]\),
\[
\sum_{n\in S}\frac1n=1
\quad\Longleftrightarrow\quad
\sum_{n\in S}\frac{L_N}{n}=L_N.
\]

The previous round proved:

- if a tail begins no later than \(N/2\), then the integers \(L_N/n\) over that tail have gcd \(1\);
- the additive group generated by all block weights
  \[
  \sum_{n=a}^b\frac{L_N}{n}
  \]
  in such a tail is also \(\mathbb Z\).

These are signed lattice statements only. They do not imply that \(L_N\) is a positive, zero-one sum of pairwise compatible block weights.

Moreover,
\[
\log L_N=\psi(N)\sim N
\]
by the prime number theorem, whereas the total number of supports is at most \(2^{N-1}\). Thus
\[
2^N=o(L_N).
\]
A generic claim that legal subset sums cover a fixed-width interval of the full \(L_N\)-lattice is therefore impossible by cardinality alone. Any successful additive argument must exploit the special target \(L_N\) or a denominator family with much smaller lcm complexity.

### 4.5 \(p\)-adic restrictions

A basic maximal-valuation lemma is reusable.

> **Maximal \(p\)-valuation lemma.**  
> If \(S\) is finite and \(\sum_{n\in S}1/n\) is an integer, then for every prime \(p\), the maximum of \(v_p(n)\) over \(n\in S\) cannot be attained at exactly one selected denominator.

Indeed, with \(D=\operatorname{lcm}\{n:n\in S\}\), reduce
\[
\sum_{n\in S}\frac Dn=D\sum_{n\in S}\frac1n
\]
modulo \(p\). Only terms whose denominator has maximal \(p\)-valuation survive on the left, while the right is divisible by \(p\).

The previous round pushed this to the quantitative statement that, if \(N=\max S\) and the reciprocal sum is an integer, then every selected \(n\) satisfies
\[
P^+(n)=O\!\left(\frac{N\log\log N}{\log N}\right),
\]
where \(P^+(n)\) denotes the largest prime factor of \(n\).

This is not close to a run-count bound. There are arbitrarily many separated smooth dimers, for example
\[
[a^2-1,a^2],
\]
because both endpoints have all prime factors at most \(a+1\), and such dimers can be separated by choosing distinct sufficiently spaced \(a\).

### 4.6 Exact under- and over-dimer identities

For every \(q\ge1\),
\[
\boxed{
\frac1q=d(2q)+\frac1{2q(2q+1)}.
}
\tag{U}
\]
Thus one can replace a singleton \(1/q\) by one legal dimer and a much smaller singleton residual.

The complementary over-identity is
\[
\boxed{
d(2q-1)=\frac1q+\frac1{2q(2q-1)}.
}
\tag{O}
\]
This is a positive two-singleton packet identity.

Iterating (U), with
\[
q_0=q,\qquad q_{j+1}=2q_j(2q_j+1),
\]
gives
\[
\frac1q=\sum_{j=0}^{m-1}d(2q_j)+\frac1{q_m}.
\]
The dimers are mutually nonadjacent. Letting \(m\to\infty\) yields an exact infinite separated-dimer expansion.

The previous round also proved:

- no unit fraction is the weight of a single dimer;
- in particular, the equation
  \[
  \frac1q=d(a)
  \]
  has no positive integer solutions;
- \(1/6\) is not a sum of two dimers, even if separation and distinctness are ignored;
- two local singleton-packet identities can be obtained from the under/over mechanism, but they do not assemble into a complete target-\(1\) expansion;
- a fixed scaled Egyptian template cannot be made exact at infinitely many scales merely by choosing, independently for each source term, its nearest under- or over-dimer replacement. For a fixed orientation pattern the discrepancy is a rational function of the scale, and the previous attempt proved it is not identically zero.

Thus independent local thickening is blocked; any successful use of these identities must couple several residuals.

### 4.7 The exact reservoir

Set
\[
Q_0=1,\qquad Q_{j+1}=2Q_j(2Q_j+1).
\]
The first values are
\[
Q_0=1,\qquad Q_1=6,\qquad Q_2=156,\qquad Q_3=97656.
\]

Iteration of (U) gives, for every \(m\ge1\),
\[
\boxed{
1=\sum_{j=0}^{m-1}d(2Q_j)+\frac1{Q_m}.
}
\]
Hence there are exactly \(m\) separated dimers of total weight
\[
1-\frac1{Q_m}.
\]

This is an exceptionally strong near-solution: the error is exact and decreases doubly exponentially.

A family of **caps**
\[
\frac1{Q_m}=\sum_{\ell=1}^c w(J_{m,\ell})
\]
with \(c\) independent of \(m\), valid for every sufficiently large \(m\), would solve the problem: the reservoir plus the cap would have \(m+c\) intervals.

Any positive cap for \(1/Q\) must use only denominators \(>Q\). If a selected denominator were \(n\le Q\), then its single term would already contribute at least \(1/Q\), and the rest of its interval would make the total too large. Thus a cap for \(Q_m\) would automatically lie beyond the reservoir.

The previous round proved significant restrictions on such caps, but no cap:

- generic full-lattice coverage with a bounded number of blocks is impossible;
- no fixed template whose interval endpoints are affine functions of \(Q_m\) can complete infinitely many residuals;
- the special nonlinear factorization
  \[
  Q_{m+1}=2Q_m(2Q_m+1)
  \]
  must be exploited if this route is to work.

### 4.8 Cap-specific \(p\)-adic condition

For a proposed identity
\[
\frac1Q=\sum_{n\in S}\frac1n,
\]
let
\[
D=\operatorname{lcm}(Q,\{n:n\in S\}).
\]
For a prime \(p\), put \(A=v_p(D)\) and \(e=v_p(Q)\). If \(A>e\), then reducing
\[
\sum_{n\in S}\frac Dn=\frac DQ
\]
modulo \(p\) forces cancellation among the selected denominators with maximal \(p\)-valuation. In particular, the maximal valuation cannot occur only once. When \(A=e\), the right side is a \(p\)-adic unit and a different leading congruence applies.

These constraints are useful search filters but have not yet forced impossibility or produced a cap.

---

## 5. Precisely blocked or dead routes from Round 1

### 5.1 Equal-weight count gadgets without a target seed

**What is proved:** run-count increments of \(1\), and indeed arbitrary integer increments, exist in exact admissible equal-weight identities arbitrarily far out.

**Precise obstruction:** if \(W(A)=W(B)>0\), one cannot append \(A\) and “subtract” \(B\). The identity is useful only when \(B\) already occurs as a compatible subconfiguration of a representation of \(1\). Common padding preserves equality but adds positive weight to both sides and creates the same unresolved completion problem.

A fresh route must therefore maintain the target \(1\) throughout, or produce an exact seed containing reusable low sides.

### 5.2 Generic lattice saturation

**What is proved:** the relevant integer weights generate the full lattice \(\mathbb Z\).

**Precise obstruction:** the proof uses subtraction, overlapping blocks, and incompatible choices. Positive legal supports are zero-one objects in a sparse conflict system. The cardinality estimate \(2^N=o(L_N)\) rules out broad coverage of a macroscopic interval in the full common-denominator lattice.

A successful additive route must target \(L_N\) specifically or lower the lcm complexity of the denominator universe.

### 5.3 Independent dimer thickening

**What is proved:** every unit fraction admits arbitrarily many separated dimers plus one smaller singleton residual.

**Precise obstruction:** the residual remains positive forever. For \(1/6\), one- and two-dimer closures are impossible. Independent under/over choices in a fixed scaled template cannot cancel identically at infinitely many scales.

Further iteration of (U) alone is dead. A new approach must couple branches or use a genuinely nonlinear finite closure.

### 5.4 Tiny residual plus generic completion

**What is proved:** \(m\) legal blocks can leave the exact residual \(1/Q_m\), with \(Q_m\) doubly exponential.

**Precise obstruction:** smallness in the real metric gives no exact arithmetic completion. Bounded full-lattice coverage and fixed affine templates have been ruled out. The cap problem remains essentially as hard as the original problem.

### 5.5 Naive matching of the \(1/7140\) error

The four-block near-solution and the gap slide have exactly matching errors. Nevertheless, the slide can correct the near-solution only if its high side \(A\) is already part of that same configuration. Appending \(A\) first adds a positive amount and does not solve the problem.

---

## 6. Traps and edge cases

1. **The intervals are maximal runs.**  
   Two adjacent constructed blocks must be merged and counted as one interval. Overlapping blocks may cause repeated reciprocal terms and are invalid unless the algebra explicitly accounts for multiplicity.

2. **A gap of one omitted integer is legal.**  
   If one interval ends at \(b\), the next may begin at \(b+2\), but not at \(b+1\).

3. **No denominator \(1\).**  
   Any legal interval containing \(1\) already has weight \(>1\).

4. **Exact arithmetic is mandatory.**  
   Errors such as \(1/Q_m\) can be astronomically small but remain fatal.

5. **Scaling destroys geometry.**  
   Replacing each \(n\) by \(tn\) scales reciprocal sums, but an interval becomes an arithmetic progression rather than an interval.

6. **Signed generation is not positive representation.**  
   A gcd of \(1\) says only that integer linear combinations exist.

7. **Equal-weight gadgets are replacements, not zero-cost additions.**

8. **Exterior compatibility matters.**  
   Even if both sides of a gadget are internally admissible, replacing one side can create adjacency with intervals outside the gadget.

9. **An infinite expansion is not a finite solution.**

10. **Dimer impossibility is not block impossibility.**  
    Longer intervals may succeed where dimers fail.

11. **The maximal-\(p\)-valuation lemma gives multiplicity, not automatic exclusion.**  
    A large prime factor may survive if another selected denominator supplies the required cancellation.

12. **Use \(N=\max S\) in largest-prime-factor statements.**  
    Artificially enlarging the ambient cutoff weakens the conclusion.

13. **A cap for one isolated \(Q_m\) gives only one new run count.**  
    To settle eventual existence via the reservoir, one needs caps for all sufficiently large \(m\), preferably with uniformly bounded run count.

14. **A finite bad \(k\) does not disprove an eventual assertion.**

15. **Search cutoffs require proof.**  
    Denominators can be arbitrarily large for fixed \(k\) unless a separate bound is established.

---

## 7. Verification hooks

All computations should use arbitrary-precision integers or reduced rational arithmetic.

### 7.1 Canonical interval checker

Given a list \((a_i,b_i)\):

1. sort by \(a_i\);
2. check \(b_i-a_i+1\ge2\);
3. check \(b_i+1<a_{i+1}\);
4. compute
   \[
   \sum_i\sum_{n=a_i}^{b_i}\frac1n
   \]
   as an exact fraction;
5. compare numerator and denominator.

This should first verify:

- the Hickerson–Montgomery identity;
- the defective \(1\)-identity;
- the \(1+1/7140\) near-solution;
- the gap-slide difference;
- the four-to-five gadget.

### 7.2 Brute verification of the support count

Enumerate all binary strings indexed by \(2,\dots,N\). Retain those whose runs of \(1\)'s all have length at least \(2\), and count by number of runs. Compare with
\[
\binom{N-k}{2k}.
\]

### 7.3 Exact dynamic programming for fixed \(N\)

Use weights
\[
c_n=L_N/n.
\]
A finite-state automaton can scan \(n=2,\dots,N\) with run states:

- \(0\): currently outside a run;
- \(1\): current run has length exactly \(1\);
- \(2\): current run has length at least \(2\).

Transitions:

- selecting \(n\): \(0\to1\), \(1\to2\), \(2\to2\);
- omitting \(n\): \(0\to0\), \(2\to0\), while \(1\to0\) is forbidden.

Increment the run count on \(0\to1\). At the end, accept only states \(0\) and \(2\), and test whether the integer sum is \(L_N\).

Sparse hashing, meet-in-the-middle, and modular prefilters are necessary well before large \(N\).

### 7.4 \(p\)-adic rejection filter

For every candidate support and each prime \(p\le N\):

1. compute \(a=\max_{n\in S}v_p(n)\);
2. if \(a>0\) is attained once, reject immediately;
3. optionally compute the full leading congruence
   \[
   \sum_{v_p(n)=a}\frac Dn\equiv0\pmod p.
   \]

For cap searches, use the modified right side \(D/Q\).

### 7.5 Exhaustive dimer-cap search

For fixed \(Q\) and fixed number \(c\), search
\[
\sum_{i=1}^c d(a_i)=\frac1Q,
\qquad
a_{i+1}\ge a_i+3
\]
for separated dimers.

Since \(d(a)\) is strictly decreasing, an ordered recursive search has finite branching: if \(r\) is the remaining target with \(s\) dimers left, then the next dimer must satisfy
\[
\frac r s\le d(a)<r.
\]
This bounds \(a\) at every step.

Priority targets are
\[
Q=6,\quad 156,\quad 97656,
\]
especially three- and four-dimer representations of \(1/6\).

### 7.6 The \(2^{14}\) Hickerson–Montgomery orientation test

The representation of \(2\) contains fourteen individual reciprocal terms. For each denominator \(n\), choose either
\[
d(2n)=\frac1n-\frac1{2n(2n+1)}
\]
or
\[
d(2n-1)=\frac1n+\frac1{2n(2n-1)}.
\]

Enumerate all \(2^{14}\) choices and test:

1. whether the signed errors cancel exactly;
2. whether the chosen dimer supports overlap;
3. after merging adjacent dimers, how many maximal legal runs remain.

This tests the smallest coupled under/over instance not covered by the fixed independent-template argument.

### 7.7 Forced gap-slide search

For
\[
A_t=[t-2,t]\cup[t+2,t+3],
\qquad
B_t=[t-2,t-1]\cup[t+1,t+3],
\]
one has
\[
w(A_t)-w(B_t)=\frac1t-\frac1{t+1}=\frac1{t(t+1)}.
\]

Search for a legal support containing \(A_t\) and having total
\[
1+\frac1{t(t+1)}.
\]
Replacing \(A_t\) by \(B_t\) would then give an exact solution. The first test is \(t=84\).

This forced-pattern search is materially different from simply appending the known slide.

### 7.8 Split-tree search

For \(x,t\ge1\) with \(t\mid x^2\),
\[
\boxed{
\frac1x=\frac1{x+t}+\frac1{x(x+t)/t}.
}
\]
Exclude \(t=x\), which gives duplicate denominators.

Starting from
\[
1=\frac12+\frac13+\frac16,
\]
perform bounded breadth-first or SMT search over exact refinements. Intermediate states may be multisets, but terminal states must be sets whose maximal runs all have length at least \(2\). Track run count and reject irreparable collisions.

### 7.9 Smooth-cluster entropy test

For square dimers
\[
C_a=[a^2-1,a^2],\qquad a\le A,
\]
all denominators divide \(L_{A+1}^2\), since
\[
a^2\mid L_{A+1}^2,\qquad
a^2-1=(a-1)(a+1)\mid L_{A+1}^2.
\]

Compute:

- the exact lcm of candidate denominators;
- the number of independent local configurations;
- reachable reciprocal residues modulo that lcm;
- the count spectrum.

The binary square-dimer reservoir has entropy only about \(A\log2\), while
\[
\log L_{A+1}^2\sim2A.
\]
Thus it is already too small for a bare pigeonhole argument. Any smooth-cluster route must find substantially more than two local states per unit of lcm complexity.

---

## 8. Four new Round-2 attack routes

## Route 1: Coupled Egyptian splitting dynamics

### Core mechanism

Maintain the exact target \(1\) at every step using the two-term refinement
\[
\frac1x=\frac1{x+t}+\frac1{x(x+t)/t},
\qquad t\mid x^2.
\]
Unlike the under-dimer iteration, this creates no residual error: it replaces one exact unit fraction by two exact unit fractions. The parameters \(t\) can be coordinated across several branches so that terminal denominators become consecutive.

Start from the exact expansion
\[
1=\frac12+\frac13+\frac16,
\]
where \([2,3]\) is already legal and only \(6\) is a singleton defect.

### Key lemma needed

A useful non-tautological form would be a **synchronized refinement macro**:

> There exist two or more marked unit fractions and exact finite split trees which replace them by legal runs together with a new marked set of the same form at larger denominators, with available run-count increments whose gcd is \(1\); moreover the marked set admits finite closures at arbitrarily large depths.

Such a macro would keep all defects inside an exact representation of \(1\), avoiding the seed-compatibility problem of equal-weight padding gadgets.

### Why it might work

- Exactness is preserved automatically.
- The variable divisor parameter \(t\mid x^2\) is much richer than the previously blocked nearest under/over replacement.
- Branches can be coupled: a denominator generated from one source can be made adjacent to a denominator generated from another.
- Every split increases term count, supplying a natural pump if terminal runs can be controlled.

### Most likely failure point

The equations forcing cross-branch adjacency,
\[
x+t+1=\frac{y(y+s)}s
\quad\text{or similar},
\]
may have too few compatible integer solutions. Duplicate leaves, overlapping supports, and unwanted merging may destroy run-count control. The rewriting graph may have no finite terminal state other than configurations containing singleton defects.

### Quick blocking test

Run the exact split-tree search from \(\{2,3,6\}\) with:

- \(t\mid x^2\);
- denominator bounds increasing through \(10^3,10^4,\dots\);
- canonicalization under permutation;
- scores for the number of singleton runs and marked defects.

If no state reduces the defect count below one despite millions of distinct coupled states, restrict to two-source Diophantine adjacency equations and solve them symbolically. Conversely, one terminal support should be mined for a repeatable local macro rather than treated merely as an isolated solution.

---

## Route 2: Grouped practical-number and divisor-coin constructions

### Core mechanism

Choose a specially engineered common denominator \(M\). For every candidate interval \(I\) whose elements divide \(M\), define the integer block coin
\[
A_I:=M\sum_{n\in I}\frac1n=\sum_{n\in I}\frac Mn.
\]
The target becomes an exact partition
\[
\sum_I A_I=M.
\]

Instead of invoking generic gcd saturation, arrange separated local windows with several admissible states and prove a cardinality-refined coin-coverage theorem. The conceptual model is the theory of practical numbers: the Stewart–Sierpiński theorem characterizes integers whose divisors represent every smaller integer as a subset sum. Here one needs a substantially stronger **grouped** version in which divisors are forced to occur in consecutive-denominator blocks.

### Key lemma needed

A grouped practical-number lemma of the following type:

> For arbitrarily large \(r\), there exist a common denominator \(M_r\), mutually separated local windows \(W_1,\dots,W_r\), and finitely many legal states in each window, such that the associated integer weights represent a specified target \(T_r\) with every cardinality in a long interval of consecutive values.

The target should be either \(M_r\), or a residual \(M_r(1-W(C))\) after a fixed legal core \(C\).

### Why it might work

- It targets one special integer rather than requiring broad lattice coverage.
- Local windows make compatibility automatic and make run counts additive.
- Divisor systems can have deterministic complete-sequence structure unavailable in generic \(L_N/n\) weights.
- Cardinality-refined subset-sum induction could directly produce every large \(k\).

### Most likely failure point

Natural grouped block weights are too coarse and fail the usual complete-sequence inequalities. Practical-number theorems allow arbitrary divisors, whereas this problem groups reciprocals according to consecutive denominators and enforces guard gaps. The \(p\)-adic restrictions may eliminate exactly the denominators needed for coverage.

### Quick blocking test

For moderate \(N\):

1. set \(M=L_N\) or a structured multiple;
2. enumerate all legal blocks in preassigned separated windows;
3. compute their integer weights;
4. perform exact DP by target and run count;
5. inspect whether the attainable count set at target \(M\) expands into intervals or remains sporadic.

Also test the complete-sequence criterion after sorting local-state weight differences. If large gaps persist at every scale, ordinary practical-number induction is blocked and a more specialized divisor architecture is required.

---

## Route 3: Low-lcm smooth reservoirs with \(p\)-adic Fourier mixing

### Core mechanism

The generic universe \([2,N]\) has too much lcm complexity:
\[
\log L_N\sim N>\log 2^N.
\]
Instead, build many separated local configurations using only smooth denominators dividing a much smaller common denominator \(M\). Seek enough local choice entropy to mix the integer reciprocal weight modulo \(M\).

If a legal support has common denominator \(M\), reciprocal sum in \((0,2)\), and
\[
\sum_{n\in S}\frac Mn\equiv0\pmod M,
\]
then its reciprocal sum is a positive integer below \(2\), hence exactly \(1\).

The reservoir
\[
1-\frac1{Q_m}
\]
can serve as the coarse core, while smooth clusters beyond \(Q_m\) attempt to fill the residual with a prescribed number of runs.

### Key lemma needed

A local-limit or Fourier-mixing statement:

> There exist separated smooth clusters \(C_1,\dots,C_r\), each with several local admissible states, such that the resulting weighted sums are sufficiently equidistributed modulo every prime-power factor of the common denominator \(M\), including in each desired run-count layer.

A strong enough version should give positive mass at the target residue for every count in a long interval.

### Why it might work

- It directly addresses the entropy obstruction by reducing \(\log M\), rather than ignoring it.
- The earlier smoothness theorem indicates that any genuine solution is already forced toward smooth denominators.
- Local clusters permit transfer-matrix or character-sum factorization.
- Exact equality follows from congruence plus a real interval bound, avoiding the need to hit a single huge integer directly.

### Most likely failure point

Smooth consecutive integers are arithmetically scarce. The local weights may be highly singular modulo prime powers, so large configuration entropy need not imply equidistribution. Pigeonhole arguments usually produce two equal residues, not the required zero residue or target count.

The simplest square-dimer family is already entropy-deficient:
\[
2^A< L_{A+1}^2
\]
on the exponential scale. The route therefore needs richer clusters with roughly eight or more effective local states per \(a\)-scale, not merely optional square dimers.

### Quick blocking test

Construct candidate clusters from explicit smooth pairs and short runs, factor their common denominator, and compute transfer matrices modulo successive prime powers. Measure:

- entropy per cluster;
- \(\log M\) per cluster;
- Fourier coefficients for nontrivial characters;
- surviving run counts after CRT combination.

If the entropy rate remains below lcm growth, or a fixed nontrivial character has correlation near \(1\), this route is blocked in that family.

---

## Route 4: Disproof via simultaneous prime-power forcing

### Core mechanism

Strengthen the maximal-\(p\)-valuation lemma into a global structural theory. For each prime power \(p^a\), the selected denominators attaining the maximal \(p\)-valuation satisfy an exact leading congruence. These congruences link distant intervals because adjacent integers are coprime.

Encode a hypothetical solution by a prime-power incidence hypergraph:

- vertices are selected denominators or runs;
- a hyperedge records all denominators attaining a maximal \(p\)-valuation;
- each hyperedge carries its mod-\(p\) cancellation equation.

The aim is to prove that target-\(1\) solutions have either boundedly many runs or an interval-count spectrum omitting infinitely many values.

### Key lemma needed

A genuinely decisive lemma would be one of:

1. a **bounded-core theorem**: every integer reciprocal support whose runs all have length at least \(2\) is contained below an absolute bound;
2. an infinite count obstruction, such as
   \[
   k\notin\mathcal R
   \]
   for an infinite set of \(k\);
3. a terminal-defect theorem showing that every sufficiently remote collection of legal runs contributes a nonzero \(p\)-adic residue that cannot be canceled by the bounded low-denominator core.

Any result only excluding the specific caps \(1/Q_m\) would not disprove the original problem.

### Why it might work

- Exact integer reciprocal sums obey far more simultaneous congruences than the first-order “maximum attained twice” condition.
- Runs force selection of adjacent coprime numbers, while \(p\)-adic cancellation generally requires additional distant multiples of their large prime factors.
- Repeating this forcing may create an expanding dependency graph incompatible with finite support.
- The persistent singleton residual in the reservoir may reflect a real terminal arithmetic obstruction rather than merely a failed construction.

### Most likely failure point

The constraints may have enough flexibility to propagate indefinitely. The explicit equal-weight gadgets with arbitrary run-count differences warn that no simple count invariant can hold for all rational weights. Smooth square dimers also show that first-order prime-factor restrictions alone permit arbitrarily many runs.

A disproof is therefore substantially less plausible than a constructive solution unless higher-order congruences produce a qualitatively new rigidity theorem.

### Quick blocking test

For increasing \(N\):

1. encode only the prime-power leading congruences and run constraints as SAT/SMT;
2. record feasible run counts, without yet enforcing the full reciprocal equation;
3. repeat for cap equations \(1/6\), \(1/156\), and \(1/97656\);
4. inspect the incidence hypergraphs of surviving assignments.

If all sufficiently large run counts already survive the complete family of local prime-power constraints, then this obstruction mechanism is too weak. If strong count gaps appear, attempt to prove them uniformly using primes in intervals
\[
\frac N{r+1}<p\le \frac Nr.
\]

---

## 9. Verdict on difficulty

This is a genuinely difficult exact-arithmetic existence problem. The previous round achieved unusually strong partial structure:

- arbitrary run-count differences in equal-weight legal gadgets;
- a valid four-block sum \(1+1/7140\) and a matching local correction;
- full signed lattice generation;
- substantial \(p\)-adic smoothness restrictions;
- an exact \(m\)-block reservoir with doubly exponentially small residual.

None addresses the central compatibility problem: converting exact positive mass into a finite legal representation of the fixed target \(1\).

The problem is not presently known to be equivalent to a famous conjecture such as the Erdős–Straus conjecture, nor is such an implication visible from the supplied literature. Nevertheless, it has remained open since the Erdős–Graham formulation, and the round-1 reductions show that generic analytic approximation, gcd arguments, and independent Egyptian-fraction splitting are inadequate.

The most promising immediate Round-2 program is:

1. exact coupled split-tree search from \(1/2+1/3+1/6\);
2. forced-pattern searches around the \(1/7140\) slide;
3. exact three- and four-dimer cap searches for \(1/6\) and \(1/156\);
4. only then, abstraction into a synchronized rewrite macro or a low-lcm grouped coin theorem.

A complete solution likely requires a new finite exact identity with a self-propagating structure, not merely a sharper approximation or a more general lattice statement.