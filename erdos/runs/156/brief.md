# Problem Brief: Erdős Problem #156 — Small Maximal Sidon Sets

## 1. Precise statement

For a positive integer \(N\), write
\[
[N]:=\{1,2,\dots,N\}.
\]

A set \(A\subseteq [N]\) is a **Sidon set** (or \(B_2\)-set) if every equation
\[
a+b=c+d,\qquad a,b,c,d\in A,
\]
is trivial in the sense that
\[
\{a,b\}=\{c,d\}
\]
as multisets. Equivalently, all sums
\[
a+b,\qquad a,b\in A,\quad a\le b,
\]
are pairwise distinct. For subsets of the integers, this is also equivalent to all positive differences \(a-b\), with \(a,b\in A\) and \(a>b\), being distinct.

A Sidon set \(A\subseteq[N]\) is **maximal in \([N]\)** if it is inclusion-maximal among Sidon subsets of \([N]\); that is,
\[
\forall x\in[N]\setminus A,\qquad A\cup\{x\}\ \text{is not Sidon}.
\]
This is not the same as having maximum possible cardinality.

Define the minimum maximal-Sidon-set size
\[
\sigma(N):=
\min\bigl\{|A|:A\subseteq[N],\ A\text{ is Sidon and maximal in }[N]\bigr\}.
\]

The standard formal reading of the problem is:

> Do there exist absolute constants \(C>0\) and \(N_0\in\mathbb N\) such that for every integer \(N\ge N_0\), there is a maximal Sidon set \(A_N\subseteq[N]\) satisfying
> \[
> |A_N|\le C N^{1/3}?
> \]
> Equivalently, is
> \[
> \sigma(N)=O(N^{1/3})?
> \]

Because \(N\) is not quantified explicitly in the informal database statement, one could read it as asking only for arbitrarily large \(N\). That weaker interpretation would ask for
\[
\sigma(N)\ll N^{1/3}
\]
along an infinite sequence of \(N\). The standard asymptotic interpretation, consistent with the quoted upper bound of Ruzsa, is the uniform “for every sufficiently large \(N\)” formulation above.

### Exact maximality criterion

For \(A\subseteq\mathbb Z\), define
\[
A+A-A:=\{b+c-a:a,b,c\in A\}
\]
and
\[
\operatorname{Mid}(A):=
\{x\in\mathbb Z:2x=b+c\text{ for some }b,c\in A\}.
\]

If \(A\) is Sidon and \(x\notin A\), then \(A\cup\{x\}\) fails to be Sidon if and only if at least one of the following holds:

1. There are \(a,b,c\in A\) such that
   \[
   x+a=b+c,
   \]
   equivalently \(x\in A+A-A\).

2. There are \(b,c\in A\) such that
   \[
   2x=b+c,
   \]
   equivalently \(x\in\operatorname{Mid}(A)\).

Indeed, any new nontrivial equal-sum relation must involve \(x\); after cancellation, it has exactly one of these two forms. Consequently,
\[
A\text{ is maximal in }[N]
\quad\Longleftrightarrow\quad
[N]\subseteq (A+A-A)\cup\operatorname{Mid}(A).
\]
The inclusion also covers points of \(A\), since \(a=a+a-a\).

### Convention warning

Some authors use “weak Sidon set” to mean that only sums of two distinct elements must be different. Under that convention, relations \(2x=b+c\) do not necessarily obstruct adding \(x\), and the exact problem changes. The ordinary \(B_2\) convention above—allowing repeated summands—is the standard reading here.

---

## 2. What counts as a solution

### Complete affirmative solution

A complete proof must establish absolute constants \(C,N_0\) such that for every \(N\ge N_0\) one can produce, either explicitly or nonconstructively, a set \(A_N\subseteq[N]\) satisfying all three conditions:

1. **Sidon property:**
   \[
   a+b=c+d,\quad a,b,c,d\in A_N
   \implies
   \{a,b\}=\{c,d\}.
   \]

2. **Maximality in the entire interval:**
   \[
   \forall x\in[N]\setminus A_N,\quad
   A_N\cup\{x\}\text{ is not Sidon}.
   \]
   Equivalently,
   \[
   [N]\subseteq(A_N+A_N-A_N)\cup\operatorname{Mid}(A_N).
   \]

3. **Uniform cardinality bound:**
   \[
   |A_N|\le C N^{1/3},
   \]
   where \(C\) is independent of \(N\).

A construction only for certain convenient values of \(N\), such as prime powers, resolves the standard formulation only if accompanied by a rigorous transfer argument covering every sufficiently large \(N\) without losing more than a constant factor.

For an explicit proposed set \(A\), verification consists of checking:

- \(A\subseteq[N]\);
- all unordered pair sums \(a+b\), \(a\le b\), are distinct;
- every \(x\in[N]\setminus A\) has a witness \(x+a=b+c\) or \(2x=b+c\) with \(a,b,c\in A\).

### Complete disproof

The negation of \(\sigma(N)=O(N^{1/3})\) is
\[
\forall C>0\ \forall N_0\ \exists N\ge N_0
\quad
\sigma(N)>C N^{1/3}.
\]
Equivalently,
\[
\limsup_{N\to\infty}\frac{\sigma(N)}{N^{1/3}}=\infty.
\]

Thus a disproof must prove an unbounded-factor lower bound along an infinite sequence of \(N\). For example, it would suffice to prove
\[
\sigma(N_j)\ge N_j^{1/3}f(N_j)
\]
for some \(N_j\to\infty\) and some \(f(N_j)\to\infty\).

There is no single finite \(N\) that can disprove a big-\(O\) statement with an unspecified constant: any finite exception can be absorbed into the constant or threshold. A computational counterexample to a proposed construction may refute that construction, but not the problem itself.

For a finite \(N\), a certificate that \(\sigma(N)>k\) must establish that every Sidon \(A\subseteq[N]\) with \(|A|\le k\) is nonmaximal. Such finite certificates can support a general lower-bound argument but cannot alone resolve the asymptotic problem.

---

## 3. What does not count

The following do not resolve the standard problem:

1. **A small Sidon set that is not maximal.**  
   It must block every omitted point.

2. **An upper bound retaining an unbounded factor**, such as
   \[
   |A|\ll N^{1/3}(\log N)^\varepsilon
   \]
   for any fixed \(\varepsilon>0\), including the known
   \[
   |A|\ll (N\log N)^{1/3}.
   \]

3. **A construction only for infinitely many \(N\)** unless one adopts the weaker interpretation or supplies a transfer to all sufficiently large \(N\).

4. **A construction for \(N\) in a restricted range**, for prime powers only, or under an unproved number-theoretic hypothesis.

5. **An expected-size or high-probability heuristic** without a proof that the final set is simultaneously Sidon, maximal, and of the required size.

6. **A maximal extension argument without size control.**  
   Every Sidon set in a finite interval can be greedily extended to a maximal one, but the extension may add far too many elements.

7. **A bound on maximum Sidon sets.**  
   Maximum Sidon sets in \([N]\) have order \(N^{1/2}\); this is a different extremal quantity.

8. **Coverage of almost all of \([N]\).**  
   Even \(o(N)\) uncovered points are fatal unless they can be repaired while preserving the \(O(N^{1/3})\) size and the Sidon property.

9. **A cyclic-group maximal Sidon set without an interval transfer.**  
   A modular relation
   \[
   x+a\equiv b+c\pmod M
   \]
   need not yield the integer equality required in \([N]\).

10. **A conditional disproof**, or evidence that \(\sigma(N)/N^{1/3}\) grows in computed ranges, without an infinite lower-bound theorem.

---

## 4. Known results and context

The question is attributed to Erdős, Sárközy, and Sós [ESS94].

### Elementary lower bound

Let \(A\subseteq[N]\) be a maximal Sidon set and put \(k=|A|\). Since \(A\) is Sidon,
\[
|A+A|=\binom{k+1}{2}=\frac{k(k+1)}2.
\]
Using the maximality criterion,
\[
[N]\subseteq(A+A-A)\cup\operatorname{Mid}(A).
\]
Now
\[
|A+A-A|
\le |A|\cdot|A+A|
=\frac{k^2(k+1)}2,
\]
and
\[
|\operatorname{Mid}(A)|
\le |A+A|
=\frac{k(k+1)}2.
\]
Therefore
\[
N\le \frac{k^2(k+1)}2+\frac{k(k+1)}2
=\frac{k(k+1)^2}{2}.
\]
In particular,
\[
k\ge (2N)^{1/3}-O(1).
\]
Thus
\[
\sigma(N)=\Omega(N^{1/3}).
\]

This is the natural counting barrier. A positive solution would therefore determine the correct order of magnitude:
\[
\sigma(N)=\Theta(N^{1/3}).
\]

The database says that the lower bound is easy for the greedy construction. In fact, the coverage count above applies to every maximal Sidon set, including every output of a greedy maximal-extension procedure.

### Ruzsa’s upper bound

According to the database commentary, Ruzsa [Ru98b] proved
\[
\sigma(N)\ll (N\log N)^{1/3}.
\]
Thus the current stated gap is
\[
N^{1/3}\ll \sigma(N)\ll N^{1/3}(\log N)^{1/3}.
\]
The problem is precisely whether the logarithmic factor can be removed.

The appearance of \((\log N)^{1/3}\) is consistent with a coupon-collector or union-bound phenomenon: a set of size \(k\) has on the order of \(k^3\) potential witnesses \(b+c-a\), so \(k^3\asymp N\log N\) is the random scale at which one can hope to cover all \(N\) points by essentially independent random witnesses. Achieving \(k^3\asymp N\) requires a much more efficient, highly organized covering.

The database also refers to Problem #340. Its exact relevance is not included in the supplied material and should be checked directly before claiming a new implication or equivalence.

### Classical maximum-size results

Let
\[
F_2(N)=\max\{|A|:A\subseteq[N]\text{ is Sidon}\}.
\]
Classical work of Erdős–Turán gives
\[
F_2(N)\le \sqrt N+O(N^{1/4}),
\]
while finite-field constructions of Singer and Bose–Chowla give matching order \(\sqrt N\), and asymptotically sharp constructions along suitable parameter sequences.

These results concern maximum Sidon sets, not minimum maximal Sidon sets. They do show that the Sidon constraint itself permits sets much larger than \(N^{1/3}\); the difficulty here is to obtain complete domination with only \(O(N^{1/3})\) elements.

### Hypergraph/saturation interpretation

One may view \([N]\) as the vertex set of an additive-conflict hypergraph whose forbidden configurations are nontrivial equal-sum relations. A Sidon set is an independent set, and a maximal Sidon set is a maximal independent set, equivalently an independent dominating set in the associated conflict system. The problem asks for the order of the corresponding saturation number.

---

## 5. Traps and edge cases

### 5.1 Maximal versus maximum

“Maximal” means no element can be added. It does not mean largest cardinality. A maximum Sidon set is automatically maximal but has size about \(N^{1/2}\), far above the target.

### 5.2 Repeated summands cannot be omitted

When testing whether \(x\) can be added, the obstruction
\[
2x=b+c
\]
is essential. Checking only representations \(x+a=b+c\) misses the case in which the new repeated sum \(x+x\) collides with an old sum.

### 5.3 Coverage by formal triples is not enough unless the values lie in \([N]\)

The set \(A+A-A\) may contain many values outside \([N]\). Counting all triples \(b+c-a\) does not prove efficient coverage of the interval.

### 5.4 Multiplicity and symmetry waste

The ordered triples \((a,b,c)\) and \((a,c,b)\) give the same value \(b+c-a\). Further collisions may be extensive. The raw count \(k^3\) therefore overstates the number of possible covered points; the more natural first bound is \(k|A+A|\sim k^3/2\).

### 5.5 Almost maximal is not maximal

A set blocking \(99.999\%\) of the interval is not a solution. Repairing the remaining points one at a time can cost much more than \(N^{1/3}\) or destroy the Sidon property.

### 5.6 Uncovered points cannot generally be added simultaneously

If \(U\) is the set of points not blocked by \(A\), each \(x\in U\) may individually be admissible, while two elements of \(U\) may conflict with one another. Thus \(A\cup U\) need not be Sidon.

### 5.7 Restriction and padding are unsafe

If \(A\) is maximal in \([M]\), then \(A\cap[N]\) need not be maximal in \([N]\). Conversely, a maximal set in \([N]\) need not remain maximal after enlarging the interval. Therefore constructions on a subsequence of ambient sizes do not automatically interpolate.

### 5.8 Modular wrap-around

A Sidon set in \(\mathbb Z/M\mathbb Z\) represented by integers is still Sidon in the integers if modular Sidonicity is strong enough, because an integer equality implies a modular equality. Maximality does not transfer so easily: a modular witness may have
\[
b+c-a=x\pm M
\]
rather than \(b+c-a=x\).

### 5.9 Cartesian products usually fail

The Cartesian product of two Sidon sets need not be Sidon in a product group. The pairings of the two coordinates can be swapped inconsistently, producing equal sums not arising from the same unordered pair.

### 5.10 Affine operations

Translation preserves the Sidon property, and translation of both the set and ambient interval preserves maximality. Dilation preserves Sidonicity but generally creates unblocked residue classes and does not preserve maximality in a full interval.

### 5.11 Very small cases

Small values are dominated by boundary effects and should not guide asymptotic constants. Useful unit tests include
\[
\sigma(1)=1,\qquad \sigma(2)=2,\qquad
\sigma(3)=2,\qquad \sigma(4)=2.
\]
For \(N=4\), the set \(\{2,3\}\) is maximal: adding \(1\) gives \(1+3=2+2\), while adding \(4\) gives \(2+4=3+3\).

---

## 6. Verification hooks

### 6.1 Exact checker for a proposed set

Given \(N\) and \(A=\{a_1,\dots,a_k\}\):

1. Check \(1\le a_i\le N\) and distinctness.
2. Initialize a hash table for unordered pair sums.
3. For every \(1\le i\le j\le k\), compute
   \[
   s=a_i+a_j.
   \]
   Reject if \(s\) has already arisen from a different unordered pair.
4. Initialize a Boolean array `blocked[1..N]`.
5. For each unordered pair \(b\le c\) in \(A\), with \(s=b+c\):
   - for every \(a\in A\), set `blocked[s-a]=true` when \(1\le s-a\le N\);
   - if \(s\) is even, set `blocked[s/2]=true` when \(1\le s/2\le N\).
6. Accept maximality exactly when every \(x\in[N]\) is marked.

This runs in \(O(k^3+N)\) elementary operations. At the conjectural scale \(k=O(N^{1/3})\), this is \(O(N)\) up to hashing and constants.

### 6.2 Exact computation of \(\sigma(N)\)

A backtracking search can enumerate Sidon sets by inserting points in increasing order and maintaining occupied differences or pair sums. At each leaf, apply the exact maximality checker. Symmetries such as reflection
\[
A\mapsto N+1-A
\]
can reduce the search.

For fixed \(k\), a SAT or constraint-programming formulation can ask whether a maximal Sidon \(k\)-set exists.

- Boolean variable \(y_i\) records \(i\in A\).
- Auxiliary variable \(p_{ij}\) records \(y_i\land y_j\), for \(i\le j\).
- For each sum \(s\), impose
  \[
  \sum_{i+j=s,\ i\le j} p_{ij}\le 1.
  \]
- For each \(x\), require either \(y_x=1\) or at least one selected witness \(x+a=b+c\) or \(2x=b+c\).

Proof-producing SAT solvers can provide independently checkable unsatisfiability certificates for statements such as \(\sigma(N)>k\).

### 6.3 Coverage diagnostics

For a candidate \(A\), record:

- \(|(A+A-A)\cap[N]|\);
- \(|\operatorname{Mid}(A)\cap[N]|\);
- their intersection;
- the multiplicity
  \[
  r_A(x)=\#\{(a,\{b,c\}):x+a=b+c\};
  \]
- the number and location of uncovered points;
- the proportion of formal witnesses lying outside \([N]\);
- the longest consecutive interval covered by the blocker set.

These statistics distinguish failure from boundary waste, duplicate representations, or genuine holes.

### 6.4 Search for efficient Golomb rulers

Since a Sidon set in the integers is a Golomb ruler, for each \(k\) one can optimize
\[
L(A):=\max\{L:[L]\subseteq(A+A-A)\cup\operatorname{Mid}(A)\}
\]
after allowing translation and reflection. The central empirical question is whether the best \(L(A)\) grows like \(c k^3\) with \(c>0\).

### 6.5 Finite-group experiments

For a candidate Sidon set \(B\) in a finite abelian group \(G\), compute exactly whether
\[
G=(B+B-B)\cup\{x:2x\in B+B\}.
\]
Also compute fiber multiplicities of the map
\[
(a,\{b,c\})\longmapsto b+c-a.
\]
Candidates should then be lifted to integer representatives and retested using exact integer equalities, not congruences.

### 6.6 Product-gadget checks

Before relying on a proposed composition theorem, exhaustively test small pairs of gadgets. Verify:

- whether the composed set remains Sidon;
- whether coordinate-swapping creates collisions;
- whether carries create extra equal sums;
- whether every product point has a witness with compatible digit pairings.

---

## 7. Attack routes

### Route 1: Direct construction of covering Golomb rulers

**Core idea.**  
Use the equivalence between Sidon sets and Golomb rulers. Seek \(k\)-element rulers \(A\) for which the blocker set
\[
(A+A-A)\cup\operatorname{Mid}(A)
\]
covers an interval of length \(\Theta(k^3)\).

**Key lemma needed.**  
There are constants \(c,C>0\) and, for every sufficiently large \(k\), Sidon sets
\[
A_k\subseteq[Ck^3]
\]
with
\[
[c k^3]\subseteq(A_k+A_k-A_k)\cup\operatorname{Mid}(A_k).
\]
A second interpolation lemma would then be needed to treat every \(N\).

**Why it might work.**  
The elementary counting bound allows \(\Theta(k^3)\) blocked points. A near-optimal ruler whose translates of \(A-A\) overlap little could conceivably realize a positive proportion of this capacity:
\[
A+A-A=A+(A-A).
\]

**Likely failure point.**  
Differences may be unique while the translates \(a+(A-A)\) overlap heavily or lie outside the target interval. Boundary losses and unavoidable additive identities may prevent contiguous coverage.

**Quick test.**  
For \(k\le 15\) or \(20\), use SAT/CP/local search to maximize the longest covered interval and plot
\[
\frac{L(A)}{k^3}.
\]
A rapid decay toward zero would obstruct this direct form; stabilization at a positive constant would be strong evidence.

---

### Route 2: Finite-field or finite-group algebraic saturation

**Core idea.**  
Construct a Sidon set \(B\) of size \(k\) in a finite abelian group \(G\) of order \(\Theta(k^3)\) such that
\[
G=(B+B-B)\cup\{x:2x\in B+B\}.
\]
Then transfer the construction to an interval by a Freiman embedding, controlled lifting, or a bounded collection of compatible lifts.

Possible candidates include algebraic curves or moment-type parametrizations over finite fields, with constants chosen to respect the upper bound \(|B+B-B|\lesssim k^3/2\).

**Key lemma needed.**  
An explicit family \((G_q,B_q)\) with
\[
|B_q|=\Theta(q),\qquad |G_q|=\Theta(q^3),
\]
where \(B_q\) is Sidon and saturates \(G_q\), together with an interval-lifting theorem preserving both Sidonicity and domination at constant-factor cost.

**Why it might work.**  
Algebraic parametrizations can make equal-sum equations rigid, while polynomial maps in three parameters naturally have \(\Theta(q^3)\) possible outputs. Finite groups remove boundary losses.

**Likely failure point.**  
The triple map may omit a positive proportion of the group or have large fibers. Even perfect modular coverage may be caused by wrap-around and fail completely after lifting to integers.

**Quick test.**  
For small odd prime powers \(q\), enumerate proposed algebraic sets and compute the exact image of \(B+B-B\). Then inspect whether each modular witness can be assigned an integer lift with zero wrap, or whether a bounded number of lifts suffices.

---

### Route 3: Semirandom packing-covering or nibble construction

**Core idea.**  
Treat selection of \(A\) as a simultaneous packing and covering problem:

- packing constraint: no two unordered selected pairs have the same sum;
- covering constraint: every \(x\) must lie in a selected witness \(b+c-a\) or be a selected midpoint.

Use a Rödl-nibble-style process, random greedy process, or local resampling scheme designed to cover points efficiently rather than independently.

**Key lemma needed.**  
A semirandom process that, with \(k=O(N^{1/3})\), produces a Sidon set whose uncovered set can be eliminated by adding only \(O(k)\) further elements, while maintaining Sidonicity.

**Why it might work.**  
The lower-bound count shows that constant average witness multiplicity is enough in principle. Nibble methods often convert fractional or approximate designs into near-exact coverings with bounded waste.

**Likely failure point.**  
A naive random \(k\)-set with \(k\asymp N^{1/3}\) gives only constant expected witness count per point, leaving a positive proportion uncovered. Standard union bounds restore the known logarithm. The completion stage may introduce many cross-sum collisions.

**Quick test.**  
Simulate random greedy Sidon processes up to \(k=cN^{1/3}\), measuring uncovered density and witness-degree distribution. If the uncovered set remains linearly large for all moderate \(c\), any successful method must use substantially more structured choices than random greedy selection.

---

### Route 4: Multiscale or digitwise composition

**Core idea.**  
Build large saturating Sidon sets from smaller gadgets using mixed-radix representations. If a gadget of size \(m\) controls an interval of length \(\Theta(m^3)\), a valid multiplicative composition could produce size \(m_1m_2\) in ambient length
\[
\Theta(m_1^3m_2^3)=\Theta((m_1m_2)^3).
\]

**Key lemma needed.**  
A composition operation \(A_1\star A_2\) satisfying:

1. \(|A_1\star A_2|=|A_1||A_2|\);
2. Sidonicity is preserved;
3. maximality or blocker coverage is preserved digitwise;
4. carries and coordinate-pairing ambiguities are excluded;
5. arbitrary \(N\) can be reached with only constant-factor loss.

**Why it might work.**  
The exponent \(3\) is exactly compatible with multiplicative scaling. A finite library of small saturating templates could potentially be iterated to cover all scales.

**Likely failure point.**  
Plain Cartesian products are not Sidon because sum-pairings in separate coordinates can disagree. Carries can also turn formally different digit equations into the same integer sum.

**Quick test.**  
Implement every proposed composition on the smallest nontrivial gadgets and exhaustively check equal sums and maximality. Any theorem that fails at two-digit scale should be rejected immediately.

---

### Route 5: Extract a small dominating subset from a dense algebraic Sidon set

**Core idea.**  
Begin with a classical dense Sidon set \(B\subseteq[N]\) of size \(\Theta(N^{1/2})\). Since every subset of \(B\) is automatically Sidon, seek a subset \(A\subseteq B\) of size \(O(N^{1/3})\) such that every \(x\in[N]\setminus A\) has a witness using only elements of \(A\).

For each \(x\), form a hypergraph of triples
\[
\mathcal W_x=\{(a,b,c)\in B^3:x+a=b+c\}.
\]
The problem becomes selecting a small vertex subset \(A\subseteq B\) containing at least one whole witness from every \(\mathcal W_x\), including witnesses that block omitted points of \(B\).

**Key lemma needed.**  
For a suitably pseudorandom dense Sidon set \(B\), the family \(\{\mathcal W_x\}\) admits a common induced covering set \(A\) of size \(O(N^{1/3})\).

**Why it might work.**  
Classical finite-field Sidon sets have highly controlled representation theory. The Sidon condition is inherited automatically, isolating the difficulty to a structured covering problem.

**Likely failure point.**  
Randomly selecting \(N^{1/3}\) elements from \(B\) again gives only constant expected selected witnesses for a typical \(x\), so logarithmic oversampling may reappear. Some \(x\) may have very few witnesses even in \(B\).

**Quick test.**  
For Singer or Bose–Chowla-type sets at small prime powers, compute all witness hypergraphs and solve the induced covering problem by ILP. Compare the optimum with \(N^{1/3}\) and inspect which \(x\) force large selections.

---

### Route 6: Disproof via unavoidable overlap or holes

**Core idea.**  
Prove that no Sidon set can use its nominal \(O(k^3)\) blockers efficiently enough to cover an interval of length \(\Theta(k^3)\). This would require an unbounded loss, not merely a worse constant.

**Key lemma needed.**  
A theorem of the form
\[
\bigl|((A+A-A)\cup\operatorname{Mid}(A))\cap[N]\bigr|
\le \frac{k^3}{f(k)}
\]
for all Sidon \(A\subseteq[N]\), where \(f(k)\to\infty\), or an interval-hole theorem implying the same consequence for maximal sets.

Then maximality would force
\[
N\le \frac{k^3}{f(k)}
\]
and hence
\[
k\ge N^{1/3}f(k)^{1/3},
\]
disproving the conjectured \(O(N^{1/3})\) bound.

**Why it might work.**  
The potential blockers satisfy many algebraic dependencies, and a large fraction can be lost to symmetry, repeated values, or the boundary of \([N]\). The known logarithmic upper bound leaves open the possibility that some unbounded inefficiency is intrinsic.

**Likely failure point.**  
An unbounded loss is a very strong assertion. Random-looking Golomb rulers may have \(\Theta(k^3)\) distinct triple values, and finite-group constructions could defeat any general small-image theorem. Constant-factor overlap alone does not disprove the problem.

**Quick test.**  
Compute, for optimized small Sidon sets,
\[
\max_A\frac{|((A+A-A)\cup\operatorname{Mid}(A))\cap[N]|}{k^3}
\]
and the maximum consecutively covered interval. If these ratios stabilize away from zero, a universal \(o(k^3)\) image bound is implausible; a disproof would then need a subtler “holes despite large image” theorem.

---

## 8. Verdict on difficulty

This is a sharp additive-combinatorial saturation problem. The elementary lower bound and Ruzsa’s upper bound differ only by a factor of \((\log N)^{1/3}\), but removing such a factor is exactly the regime where random covering arguments cease to work: at \(k\asymp N^{1/3}\), only \(O(N)\) nominal witnesses are available to cover \(N\) points, so nearly all witnesses must be useful and duplication must be tightly controlled.

The problem has been open since at least the 1994 Erdős–Sárközy–Sós reference. It is not, as far as the supplied context and standard literature indicate, known to be equivalent to a famous conjecture such as the prime tuples conjecture or a standard finite-geometry conjecture. Nor is it settled by the classical theory of maximum Sidon sets.

The most important strategic fact is:

\[
\boxed{\text{The exponent }1/3\text{ is forced by counting; the entire problem is efficient exact coverage.}}
\]

A successful affirmative proof will likely need a design-like or algebraic mechanism replacing the coupon-collector behavior behind the logarithm. A disproof would require a genuinely new structural theorem showing an unbounded inefficiency in the blocker set of every Sidon set. Both directions appear difficult; the affirmative direction is presently more consistent with the raw counting heuristic, while the known logarithmic gap gives no decisive evidence either way.