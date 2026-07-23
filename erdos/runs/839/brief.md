# Problem Brief: Erdős Problem #839

## 1. Precise statement

Let
\[
A=\{a_1<a_2<a_3<\cdots\}\subseteq \mathbb Z_{>0}
\]
be an infinite strictly increasing sequence of positive integers.

Call \(A\) **consecutive-sum-avoiding** if, for every \(i\ge 1\), there are no indices \(r,s\) satisfying
\[
1\le r\le s<i
\]
such that
\[
a_i=\sum_{j=r}^{s}a_j.
\tag{CSA}
\]
Allowing \(r=s\) is harmless, since then \(a_i=a_r\), impossible when \(r<i\). Thus the same class results if “sum” is required to contain at least two terms.

The standard reading of “consecutive \(a_j\) for \(j<i\)” is an arbitrary consecutive block
\[
a_r+a_{r+1}+\cdots+a_s
\quad\text{with }s<i,
\]
not merely a suffix \(a_r+\cdots+a_{i-1}\). The suffix-only interpretation would be a substantially weaker and apparently different problem.

Define
\[
A_{<}(x)=\#\{n:a_n<x\}
\]
and
\[
H_A(x)=\sum_{a_n<x}\frac1{a_n},
\qquad x>1.
\]

The problem asks whether every consecutive-sum-avoiding sequence satisfies:

### Conjecture P1
\[
\boxed{\limsup_{n\to\infty}\frac{a_n}{n}=\infty.}
\]

It asks further whether the stronger assertion holds:

### Conjecture P2
\[
\boxed{\lim_{x\to\infty}\frac{H_A(x)}{\log x}=0.}
\]

Because the displayed quantity is nonnegative, P2 is equivalently
\[
\limsup_{x\to\infty}\frac{H_A(x)}{\log x}=0.
\]

### Prefix-sum formulation

Let
\[
S_0=0,\qquad S_m=\sum_{j=1}^m a_j.
\]
Then
\[
a_r+\cdots+a_s=S_s-S_{r-1}.
\]
Thus (CSA) is equivalent to
\[
S_i-S_{i-1}\notin
\{S_s-S_t:0\le t<s\le i-1\}
\qquad(i\ge1).
\tag{PS}
\]
In words: the new gap \(S_i-S_{i-1}\) is never a positive difference of two earlier prefix sums.

### Density reformulation of P1

Let
\[
A_{\le}(x)=\#\{n:a_n\le x\}.
\]
The lower and upper asymptotic densities are
\[
\underline d(A)=\liminf_{x\to\infty}\frac{A_{\le}(x)}x,
\qquad
\overline d(A)=\limsup_{x\to\infty}\frac{A_{\le}(x)}x.
\]
For any increasing sequence,
\[
\underline d(A)
=
\frac{1}{\displaystyle \limsup_{n\to\infty}a_n/n},
\tag{1}
\]
with the convention \(1/\infty=0\), and similarly
\[
\overline d(A)
=
\frac{1}{\displaystyle \liminf_{n\to\infty}a_n/n}.
\tag{2}
\]
Consequently P1 is exactly the assertion
\[
\boxed{\underline d(A)=0}
\]
for every admissible \(A\).

### Logarithmic-density formulation of P2

Partial summation gives, up to an immaterial endpoint error,
\[
\sum_{a_n\le x}\frac1{a_n}
=
\frac{A_{\le}(x)}x+
\int_1^x\frac{A_{\le}(t)}{t^2}\,dt.
\tag{3}
\]
Thus P2 says that every admissible set has logarithmic density zero.

If \(\underline d(A)=d>0\), then (3) implies
\[
\liminf_{x\to\infty}\frac{H_A(x)}{\log x}\ge d.
\]
Therefore
\[
\text{P2}\implies\text{P1}.
\]
The converse is false for general subsets of the integers: lower density zero does not force logarithmic density zero.

---

## 2. What counts as a solution

The two assertions should be distinguished.

### A complete proof of P1 must establish

For every infinite strictly increasing sequence of positive integers satisfying (CSA),
\[
\limsup_{n\to\infty}\frac{a_n}{n}=\infty.
\]
Equivalently, for every constant \(C>0\), there are arbitrarily large \(n\) with
\[
a_n>Cn.
\]
Equivalently, every admissible \(A\) has lower asymptotic density zero.

A useful finite compactness equivalent is:

> For every \(C<\infty\), there is an \(N(C)\) such that no admissible finite sequence
> \[
> a_1<\cdots<a_{N(C)}
> \]
> can satisfy \(a_i\le Ci\) for every \(i\le N(C)\).

Indeed, if arbitrarily long such finite sequences existed for one fixed \(C\), the finitely branching tree of legal prefixes would have an infinite branch by König’s infinity lemma.

A proof of P1 alone answers the first question but does not settle P2.

### A complete proof of P2 must establish

For every admissible infinite sequence and every \(\varepsilon>0\), there is \(X_\varepsilon\) such that
\[
\sum_{a_n<x}\frac1{a_n}\le \varepsilon\log x
\]
for every real \(x\ge X_\varepsilon\).

This automatically proves P1.

### A complete disproof of P1 must provide

An infinite strictly increasing sequence \(A=\{a_n\}\subseteq\mathbb Z_{>0}\) such that:

1. for all \(i\) and all \(1\le r\le s<i\),
   \[
   a_i\ne \sum_{j=r}^s a_j;
   \]
2. there is a finite constant \(C\) such that
   \[
   a_n\le Cn
   \]
   for all sufficiently large \(n\), or equivalently
   \[
   \limsup_{n\to\infty}\frac{a_n}{n}<\infty.
   \]

Such a construction would have positive lower density and would also disprove P2.

If the sequence is defined recursively or algorithmically, the proof must show that the construction never stalls, remains increasing, satisfies (CSA) for every index, and has the required uniform linear-growth bound. A long finite computation is not enough.

### A complete disproof of P2 must provide

An admissible infinite sequence and constants \(\varepsilon>0\) and \(x_m\to\infty\) such that
\[
\sum_{a_n<x_m}\frac1{a_n}\ge \varepsilon\log x_m
\]
for every \(m\).

Equivalently,
\[
\limsup_{x\to\infty}\frac{H_A(x)}{\log x}>0.
\]
This counterexample need not have positive lower density; it could still satisfy P1.

---

## 3. What does not count

The following do not resolve either conjecture unless strengthened appropriately.

1. **Positive upper density.**  
   Constructing an admissible set with
   \[
   \overline d(A)>0
   \]
   only proves \(\liminf a_n/n<\infty\). It does not contradict P1, which concerns lower density or \(\limsup a_n/n\).

2. **Arbitrarily dense finite blocks.**  
   An infinite sequence can contain intervals on which its local density is large while having lower density and logarithmic density zero.

3. **Arbitrarily long finite examples with varying density constants.**  
   To disprove P1 via compactness, one fixed \(C\) must work for admissible prefixes of every length.

4. **A construction with \(H_A(x)\gg\log\log x\).**  
   Since
   \[
   \frac{\log\log x}{\log x}\to0,
   \]
   this remains consistent with P2.

5. **Showing only**
   \[
   H_A(x)\le c\log x
   \]
   for some universal \(0<c<1\). P2 requires \(o(\log x)\).

6. **Bounds along an uncontrolled sparse subsequence of \(x\).**  
   P2 requires the full limit. Checking all dyadic points \(x=2^m\) would suffice by monotonicity, but checking an arbitrarily sparse sequence need not.

7. **Ruling out bounded gaps.**  
   A positive-lower-density set may still have unbounded individual gaps, so this would be weaker than P1.

8. **Results only for special subclasses**, such as periodic sets, automatic sequences, bounded-gap sets, or sequences satisfying an additional regularity hypothesis.

9. **Conditional proofs**, probabilistic heuristics, or numerical evidence without a proof of the required universal or infinite statement.

10. **Ordinary sum-free arguments.**  
    The condition is neither simply \(x+y\ne z\) within \(A\) nor avoidance of all finite sums. The summands must form a block consecutive in the enumeration of \(A\).

---

## 4. Known results and context

### Results stated in the database commentary

1. Erdős observed that admissible sequences can satisfy
   \[
   \liminf_{n\to\infty}\frac{a_n}{n}<\infty.
   \]
   Equivalently, admissible sets can have positive upper asymptotic density.

2. There are admissible sequences for which
   \[
   \sum_{a_n<x}\frac1{a_n}\gg\log\log x.
   \]
   This shows that no universal boundedness result for the reciprocal sum is possible. It remains compatible with P2.

3. Erdős knew that upper density \(1/2\) was possible and conjectured that upper density probably could not exceed \(1/2\).

4. Freud [Fr93] disproved that auxiliary density conjecture by constructing an admissible sequence with upper density
   \[
   \frac{19}{36}> \frac12.
   \]
   This does not settle P1: positive upper density corresponds to finite \(\liminf a_n/n\), whereas P1 asks whether \(\limsup a_n/n\) must be infinite.

5. The database points to Problems [359] and [867] as related, but no additional content from those entries is part of the supplied statement.

### Elementary admissible examples

The geometric sequence
\[
a_n=2^{n-1}
\]
is admissible. Indeed, a block of at least two consecutive powers of \(2\) has sum
\[
2^{r-1}+\cdots+2^{s-1}
=
2^{r-1}\bigl(2^{s-r+1}-1\bigr),
\]
whose odd factor is at least \(3\), so it is not a power of \(2\). Here \(a_n/n\to\infty\), and the reciprocal sum converges.

More generally, any superincreasing sequence satisfying
\[
a_i>\sum_{j<i}a_j
\]
is automatically admissible. Such examples are much too sparse to address the problem.

### Relevant general tools

- **Abel/partial summation** gives the relation between \(H_A(x)\) and the counting function in (3).
- **König’s infinity lemma** yields the finite-obstruction formulation of P1 for each fixed linear bound \(C\).
- Standard additive-combinatorial density theorems do not apply directly. In particular, results about \(x+y=z\), arithmetic progressions, or unrestricted finite sums do not preserve the crucial “consecutive in the enumeration” requirement.

### Settled versus open aspects

- The conjectured upper-density ceiling \(1/2\) is settled negatively by Freud’s \(19/36\) construction.
- The existence of positive upper density and reciprocal sums of order at least \(\log\log x\) is known.
- Both P1 and P2 remain open according to the database.

---

## 5. Traps and edge cases

### 5.1 Upper density versus lower density

This is the central conceptual trap. Freud’s construction gives
\[
\overline d(A)>0,
\]
not necessarily \(\underline d(A)>0\). A sequence can have very dense blocks separated by enormous gaps. Such a sequence has finite \(\liminf a_n/n\) but may still have
\[
\limsup a_n/n=\infty.
\]

### 5.2 Consecutive means consecutive indices

The forbidden block is
\[
a_r,a_{r+1},\ldots,a_s,
\]
not a block of consecutive integers, and not an arbitrary subset of earlier terms.

### 5.3 The block need not end at \(i-1\)

One must test every \(r\le s<i\), not just sums
\[
a_r+\cdots+a_{i-1}.
\]

### 5.4 Singletons cause no issue

If blocks of length one are permitted, the equation \(a_i=a_r\) is impossible for \(r<i\). Thus the length-one convention does not change the problem.

### 5.5 Strict versus non-strict cutoff

The problem uses \(a_n<x\). Replacing it by \(a_n\le x\) changes the sum by at most one term and has no effect on the limit, but exact computational implementations should fix one convention.

### 5.6 Naive counting of block sums

Among \(a_1,\dots,a_n\) there are \(\Theta(n^2)\) consecutive blocks, but:

- many block sums can coincide;
- most can be far larger than plausible next terms;
- having many forbidden values does not imply they cover a useful interval;
- one needs an intersection with the actual future values \(a_i\).

A bare pigeonhole count is therefore insufficient.

### 5.7 Modular avoidance is not automatically exact avoidance

Showing that target terms and most block sums occupy different residues is useful only if every possible block length and every carry pattern is controlled. A congruence modulo a fixed \(q\) cannot by itself rule out equality in all cases.

### 5.8 Dense finite blocks do not concatenate cheaply

Separating finite admissible blocks by choosing each new block above the sum of all previous terms can guarantee avoidance, but introduces huge gaps. This naturally produces positive upper density at selected scales, not positive lower density.

### 5.9 Translation is not an invariance

Scaling all terms by a positive integer preserves admissibility. Translation generally does not:
\[
(a_r+c)+\cdots+(a_s+c)
=
(a_r+\cdots+a_s)+(s-r+1)c.
\]

### 5.10 Short-block avoidance is insufficient

For example, taking all odd integers avoids equality with sums of two terms, because such sums are even. But sums of three consecutive odd terms are odd, and in fact
\[
1+3+5=9.
\]
All block lengths must be handled.

### 5.11 Small cases

The first genuinely nontrivial obstruction can occur at \(i=3\):
\[
a_3=a_1+a_2.
\]
Any implementation should detect this immediately.

---

## 6. Verification hooks

### 6.1 Direct admissibility checker

For a finite sequence \(a_1<\cdots<a_N\), compute
\[
S_0=0,\qquad S_i=S_{i-1}+a_i.
\]
Before appending \(v=a_i\), form or maintain
\[
F_{i-1}=\{S_s-S_t:0\le t<s\le i-1\}.
\]
The append is legal exactly when
\[
v\notin F_{i-1}.
\]

After appending \(v\), add the \(i\) new differences
\[
S_i-S_t,\qquad 0\le t<i,
\]
to the forbidden-value hash table. This gives \(O(N^2)\) time and \(O(N^2)\) worst-case memory, with much less memory possible if only candidate values below a prescribed cap matter.

### 6.2 Fixed-\(C\) backtracking search

For a proposed linear bound \(C\), recursively enumerate
\[
a_{m-1}<a_m\le \lfloor Cm\rfloor
\]
subject to \(a_m\notin F_{m-1}\).

Record:

- maximum attainable depth;
- number of surviving prefixes at each depth;
- the distribution of legal next values;
- whether all legal prefixes eventually become blocked.

If the tree is proved finite, its maximal depth gives a finite certificate for that \(C\). If it survives to large depth, inspect whether common structural patterns occur.

### 6.3 CP-SAT or SMT formulation

For fixed \(N,C\), use integer variables \(a_1,\dots,a_N\) with
\[
1\le a_1<a_2<\cdots<a_N,\qquad a_i\le \lfloor Ci\rfloor,
\]
and impose, for every \(1\le r\le s<i\le N\),
\[
a_i\ne \sum_{j=r}^s a_j.
\]
The constraints are linear disequalities and are directly supported by SMT or CP-SAT systems. Unsatisfiability certificates for increasing \(N\) may reveal inductive invariants, though an isolated finite unsatisfiability result proves only that particular \(N,C\).

### 6.4 Extremal optimization

For each \(N\), minimize one of:
\[
\max_{1\le i\le N}\frac{a_i}{i},
\qquad
a_N,
\qquad
\max_i(a_i-a_{i-1}),
\]
over admissible prefixes. Growth of the first quantity is especially relevant to P1.

Also maximize:
\[
\frac{\#(A\cap[1,X])}{X}
\quad\text{or}\quad
\sum_{a_i<X}\frac1{a_i}
\]
for finite admissible sets, while tracking whether optimizers have a recursive or block structure.

### 6.5 Difference-histogram diagnostics

For each prefix compute
\[
r_m(t)=\#\{(u,v):0\le u<v\le m,\ S_v-S_u=t\}.
\]
Legal future terms must avoid the support of \(r_{i-1}\). Plot:

- coverage of intervals \([1,K]\);
- maximal uncovered gaps;
- multiplicities \(r_m(t)\);
- which block lengths produce values near the next-term scale \(O(m)\).

This directly tests proposed interval-coverage lemmas.

### 6.6 Dyadic logarithmic-density checks

For \(I_k=[2^k,2^{k+1})\), let
\[
d_k=\frac{|A\cap I_k|}{2^k}.
\]
Then
\[
\frac12\sum_{k<M}d_k
\;\lesssim\;
H_A(2^M)
\;\lesssim\;
\sum_{k<M}d_k+O(1).
\]
Thus P2 is closely related to showing that the Cesàro average of the dyadic densities \(d_k\) tends to zero. Computations should record both \(d_k\) and all cross-scale forbidden sums.

### 6.7 Automated verification of structured constructions

For a proposed periodic, substitutional, or base-\(q\) construction:

1. build a finite automaton for allowed term digits;
2. build a carry automaton for sums of consecutive terms;
3. search for an accepting state representing
   \[
   a_i=a_r+\cdots+a_s;
   \]
4. separately compute the density or logarithmic density from the substitution matrix.

Finite-state verification is rigorous only after proving that the automaton represents every possible block length and every carry.

---

## 7. Attack routes

## Route 1: Finite obstruction under a fixed linear bound

### Core mechanism

Assume \(a_i\le Ci\). Try to prove that the earlier consecutive-block sums eventually cover every possible legal next value.

### Key lemma needed

For each fixed \(C\), there should exist \(N(C)\) such that every admissible prefix
\[
a_1<\cdots<a_m,\qquad a_i\le Ci,
\]
with \(m\ge N(C)\), satisfies
\[
\{a_m+1,\ldots,\lfloor C(m+1)\rfloor\}
\subseteq
\left\{\sum_{j=r}^s a_j:1\le r\le s\le m\right\}.
\]
A weaker lemma that merely guarantees no legal extension under the bound would suffice.

### Why it might work

Under \(a_i=O(i)\), the prefix sum is \(S_m=O(m^2)\), and there are \(\Theta(m^2)\) consecutive blocks. Sums near the next-term scale \(O(m)\) arise from many combinations of starts and moderate block lengths. Monotonicity of \(a_i\) may force overlap and interval filling.

### Most likely failure point

The \(\Theta(m^2)\) block sums may be highly collisional or concentrated in arithmetically sparse sets. Moreover, only a short interval of candidate values near \(a_m\) matters.

### Quick blockage test

For small rational \(C\), run complete fixed-\(C\) searches and calculate the proportion of the candidate interval covered by earlier block sums. If long survivors systematically preserve residue classes or large uncovered intervals, a pure interval-coverage lemma is likely false and must incorporate structural alternatives.

---

## Route 2: Prefix-sum difference energy and additive combinatorics

### Core mechanism

Use
\[
a_i=S_i-S_{i-1}
\]
and the requirement that this new gap avoid every earlier difference \(S_s-S_t\).

Define the violation count
\[
V_N=
\sum_{i=1}^N
\#\{(t,s):0\le t<s<i,\ S_s-S_t=a_i\}.
\]
Admissibility says \(V_N=0\). Seek a lower bound \(V_N>0\) under a density hypothesis.

### Key lemma needed

A suitable theorem of the following kind:

> If the increasing gaps \(a_i\) have positive lower density as integers—or sufficiently large logarithmic mass—then the difference set of earlier prefix sums must contain one of the later gaps with the required chronological order.

Fourier analysis could express difference multiplicities through exponential sums over \(\{S_j\}\), while additive-energy or sumset estimates could force overlap with \(\{a_i\}\).

### Why it might work

The prefix sums form a strictly convex sequence because their gaps \(a_i\) are strictly increasing. Difference sets of convex sequences are typically large, and positive-density gap sets should be difficult to keep disjoint from all earlier differences.

### Most likely failure point

“Large difference set” does not imply that it intersects the particular set of future gaps. Convex-set results often establish cardinality, not interval coverage or the chronology \(s<i\). Fourier energy can also concentrate on differences much larger than \(a_i\).

### Quick blockage test

For computationally extremal prefixes, compare:

- the support of the difference representation function;
- the actual gap set \(\{a_i\}\);
- random sets of the same size.

If extremizers exhibit unusually low intersection despite very large difference support, a cardinality-only argument is blocked.

---

## Route 3: Direct logarithmic-density and multiscale recurrence

### Core mechanism

Attack P2 directly. Positive normalized reciprocal mass means that \(A\) occupies a positive proportion of scales on average:
\[
H_A(2^M)\asymp \sum_{k<M}\frac{|A\cap[2^k,2^{k+1})|}{2^k}.
\]
Try to prove that repeated density on many comparable scales forces a forbidden consecutive sum.

### Key lemma needed

A multiscale recurrence statement such as:

> If the average dyadic density of \(A\) is at least \(\delta>0\) across sufficiently many scales, then there exist \(r\le s<i\) with
> \[
> a_i=a_r+\cdots+a_s.
> \]

The proof may require a density-increment, entropy-decrement, or correspondence-principle argument that retains information about consecutive ranks.

### Why it might work

P2 permits very sparse individual scales but forbids positive average occupancy over logarithmically many scales. Consecutive block sums naturally move between scales, so repeated scale occupancy may force exact recurrence.

### Most likely failure point

Known positive-upper-density constructions probably exploit dense blocks separated by scale jumps. Such block organization may maintain significant reciprocal mass while frustrating any local fixed-scale argument. Exact equality is much harder than approximate scale matching.

### Quick blockage test

Optimize finite sequences for maximal
\[
\sum_{a_i<X}\frac1{a_i}
\]
and inspect the dyadic density profile. If optimizers repeatedly use a small family of block templates at separated scales, the required lemma must explicitly analyze cross-scale sums rather than relying on average density alone.

---

## Route 4: Modular and \(p\)-adic descent

### Core mechanism

Track prefix sums and terms modulo several moduli. If
\[
S_s-S_t\equiv a_i\pmod M
\]
and both quantities lie in an interval of length \(<M\), then congruence forces equality. The goal is to use dense residue recurrence and a sufficiently large product of moduli.

### Key lemma needed

One needs simultaneous residue recurrence with size control:

> Under \(a_i=O(i)\), for some \(i\) there exist \(t<s<i\) such that
> \[
> S_s-S_t\equiv a_i\pmod M,
> \]
> while
> \[
> |S_s-S_t-a_i|<M,
> \]
> for a modulus \(M\) large enough to force equality.

A \(p\)-adic variant could classify possible valuations of block sums and show that avoidance forces progressively thinner residue classes, contradicting positive density.

### Why it might work

The prefix sums have many collisions modulo small moduli. Since terms are linearly bounded under a hypothetical counterexample to P1, moderately growing moduli may convert modular coincidences into exact identities.

### Most likely failure point

Choosing \(M\) large enough to force equality destroys the residue pigeonhole advantage. Simultaneously matching the correct target \(a_i\), keeping the difference in range, and enforcing chronology may be impossible with elementary CRT arguments.

### Quick blockage test

For long finite extremizers, compute prefix-sum residue occupancy modulo products of small prime powers. Test whether every candidate \(a_i\) has a prior difference congruent to it modulo these products and whether the corresponding differences are close enough in magnitude. Persistent modular avoidance indicates that a descent theorem would need strong new structure.

---

## Route 5: Online bounded-density construction — disproof attempt

### Core mechanism

Construct \(a_{m+1}\) greedily or with bounded backtracking from the set of integers not represented by earlier consecutive blocks. Prove that a legal choice always exists below a linear cap.

### Key lemma needed

For some fixed \(C\),
\[
\bigl(a_m,\ C(m+1)\bigr]\not\subseteq F_m
\]
for every legal prefix produced by the algorithm, where
\[
F_m=\left\{\sum_{j=r}^s a_j:1\le r\le s\le m\right\}.
\]
Even stronger would be a bounded-gap statement
\[
a_{m+1}\le a_m+K.
\]

### Why it might work

Although there are quadratically many intervals, only a small fraction may land near the next-term range. A carefully designed choice rule might keep those forbidden sums clustered while reserving one or more residue classes for future terms.

### Most likely failure point

Earlier block sums may eventually cover every short interval above \(a_m\). Naive greedy choices can create many new sums exactly in the range where future choices are needed. A bounded-gap invariant may be far stronger than positive lower density.

### Quick blockage test

Run greedy, randomized greedy, and full backtracking searches for fixed \(C\). Measure whether failure is local and unavoidable or caused by poor early choices. If all branches terminate at comparable depth for modest \(C\), the online approach is likely blocked unless a nonlocal invariant is found.

A successful route would disprove both P1 and P2.

---

## Route 6: Self-similar or base-\(q\) construction — disproof attempt

### Core mechanism

Build \(A\) from repeated finite templates using base-\(q\) digits, substitutions, or blocks near scales \(q^m\). Arrange that leading digits of every consecutive block sum are incompatible with the digit language of later terms.

### Key lemma needed

A finite-state avoidance theorem:

> For every pair of indices \(r\le s<i\), the carry-normalized base-\(q\) expansion of
> \[
> a_r+\cdots+a_s
> \]
> does not belong to the language defining the later terms \(a_i\).

The same construction must have either positive lower density, to disprove P1, or positive logarithmic density, to disprove P2.

### Why it might work

Exact additive avoidance often admits digit constructions. A substitution system can encode infinitely many constraints through finitely many states, and its density can be calculated from a transition or substitution matrix.

### Most likely failure point

Consecutive blocks can cross template and scale boundaries, producing long carry chains. Making blocks sufficiently separated to simplify carries usually destroys lower density and may also force logarithmic density zero.

### Quick blockage test

For a proposed digit language, construct the complete carry automaton for all block lengths and boundary states. If a forbidden equality appears at low depth, discard the template. If the automaton appears safe, compute the Perron–Frobenius growth rate of accepted terms to determine whether the resulting set has enough density.

---

## 8. Verdict on difficulty

This is a genuinely difficult open density problem. Its main difficulty is that it combines:

- exact additive equality;
- a chronology restriction;
- sums of intervals consecutive in the enumeration rather than arbitrary subsets;
- a distinction between upper, lower, and logarithmic density;
- constructions that can be very dense on selected scales but extremely sparse between them.

P1 is equivalent to saying that no admissible set has positive lower asymptotic density. P2 is stronger, asserting zero logarithmic density. Freud’s \(19/36\) construction shows that admissible sets can be denser on selected scales than Erdős expected, so any proof must control oscillatory block constructions rather than merely bound upper density.

No equivalence to a famous named conjecture is known from the supplied context, and the problem is not an immediate consequence of standard sum-free, Szemerédi-type, or finite-sums theorems. The exact “consecutive in rank” condition puts it outside the usual formulations of those theories.

A plausible first milestone is the fixed-\(C\) finite-obstruction program: determine computationally whether admissible sequences with \(a_i\le Ci\) appear to have uniformly bounded length for small \(C\), and extract structural reasons for termination. A disproof would likely require a highly structured self-similar or automaton-based construction, not a random or naive greedy set.