# Problem brief: Erdős Problem #195

## 1. Precise statement

### 1.1 Standard interpretation

The standard interpretation is that a **permutation of \(\mathbb Z\)** is a one-sided enumeration
\[
\pi=(\pi(0),\pi(1),\pi(2),\ldots),
\]
where
\[
\pi:\mathbb N_0\to\mathbb Z
\]
is a bijection. For each \(z\in\mathbb Z\), define its position
\[
p_\pi(z):=\pi^{-1}(z)\in\mathbb N_0.
\]

For \(k\ge 2\), a nonconstant \(k\)-term arithmetic progression in \(\mathbb Z\) is a tuple
\[
x_i=a+(i-1)d,\qquad 1\le i\le k,
\]
with \(a\in\mathbb Z\) and \(d\in\mathbb Z_{>0}\). Thus
\[
x_1<x_2<\cdots<x_k.
\]

This progression is **monotone in \(\pi\)** if its terms occur in one of the two numerical orders:

- increasing:
  \[
  p_\pi(x_1)<p_\pi(x_2)<\cdots<p_\pi(x_k),
  \]
- or decreasing:
  \[
  p_\pi(x_1)>p_\pi(x_2)>\cdots>p_\pi(x_k).
  \]

Equivalently, the sequence \(\pi\) contains either
\[
a,a+d,\ldots,a+(k-1)d
\]
or its reversal as a subsequence.

Let \(P(k)\) be the assertion
\[
\forall \pi:\mathbb N_0\overset{\sim}{\longrightarrow}\mathbb Z\quad
\exists a\in\mathbb Z\ \exists d\in\mathbb Z_{>0}
\]
such that
\[
p_\pi(a)<p_\pi(a+d)<\cdots<p_\pi(a+(k-1)d)
\]
or
\[
p_\pi(a)>p_\pi(a+d)>\cdots>p_\pi(a+(k-1)d).
\]

The problem asks for
\[
K:=\max\{k\in\mathbb N:P(k)\}.
\]

The property is hereditary downward: a monotone \(k\)-term progression contains a monotone \(j\)-term progression for every \(j\le k\), by taking \(j\) consecutive terms. Thus the set of guaranteed lengths is an initial interval.

### 1.2 Presently known numerical range

Under this interpretation,
\[
\boxed{3\le K\le 4.}
\]

Hence the open question is exactly:

> Does every permutation of \(\mathbb Z\) contain a monotone four-term arithmetic progression?

Equivalently, is \(K=4\), or can one construct a permutation of \(\mathbb Z\) with no monotone four-term arithmetic progression, in which case \(K=3\)?

### 1.3 Ambiguities that must be controlled

There are two potentially material ambiguities.

1. **One-sided versus two-sided permutation.**  
   A formal set-theoretic “permutation of \(\mathbb Z\)” can mean a bijection \(\mathbb Z\to\mathbb Z\), viewed as a doubly infinite sequence. The standard reading used here is instead a one-sided listing \(\mathbb N_0\to\mathbb Z\), equivalently a linear order of order type \(\omega\) on \(\mathbb Z\). The distinction is important: the elementary lower-bound argument for \(K\ge3\) uses the existence of a first term and does not apply unchanged to a two-sided order.

2. **Both monotone orientations versus increasing only.**  
   “Monotone” normally includes both increasing and decreasing progressions. If the intended convention is only that \(x_1<\cdots<x_k\) occur in that order, the reverse-position clause should be deleted. Any use of Geneson’s or Adenwalla’s bounds must match their exact convention. The brief adopts the two-orientation interpretation.

A third interpretation—asking for an arithmetic progression of indices on which the permutation values are monotone—is not the natural reading of the displayed statement and is not adopted here.

---

## 2. What counts as a solution

Because the known bounds leave only \(K=3\) or \(K=4\), there are exactly two resolution types.

### 2.1 A complete proof that \(K=4\)

One must prove:

\[
\forall \pi:\mathbb N_0\overset{\sim}{\longrightarrow}\mathbb Z\quad
\exists a\in\mathbb Z,\ d\in\mathbb Z_{>0}
\]
such that either
\[
p_\pi(a)<p_\pi(a+d)<p_\pi(a+2d)<p_\pi(a+3d)
\]
or
\[
p_\pi(a)>p_\pi(a+d)>p_\pi(a+2d)>p_\pi(a+3d).
\]

Together with Adenwalla’s established construction avoiding monotone five-term progressions, this gives \(K=4\). A self-contained solution should either reproduce the relevant \(K\le4\) construction or cite it with conventions checked exactly.

A proof for a restricted class of permutations is insufficient. It must cover every bijection \(\mathbb N_0\to\mathbb Z\), with no growth, regularity, computability, symmetry, or density assumptions.

### 2.2 A complete proof that \(K=3\)

One must construct, either explicitly or by a rigorous existence proof, a bijection
\[
\pi:\mathbb N_0\to\mathbb Z
\]
such that for every \(a\in\mathbb Z\) and every \(d>0\), neither
\[
p_\pi(a)<p_\pi(a+d)<p_\pi(a+2d)<p_\pi(a+3d)
\]
nor
\[
p_\pi(a)>p_\pi(a+d)>p_\pi(a+2d)>p_\pi(a+3d)
\]
holds.

For an explicit recursive or algorithmic construction, the proof must separately establish:

1. **Totality:** the \(n\)-th output is defined for every \(n\).
2. **No repetition:** distinct stages output distinct integers.
3. **Surjectivity:** every integer is eventually output.
4. **Global avoidance:** every four-term AP fails both monotonicity orientations.

A finite-state, substitution, priority, or probabilistic construction is acceptable only if all four points are proved.

Since \(P(3)\) is known, such a construction would establish the exact answer \(K=3\).

### 2.3 Verification of an alleged counterexample

For a proposed formula or algorithm, it is not enough to inspect a large prefix. The global avoidance condition can be verified only through a theorem reducing every possible pair \((a,d)\) to finitely many structural cases, or through a rigorous inductive invariant that covers all future stages.

If the construction is nonconstructive, the existence argument must produce an order of type \(\omega\), not merely an arbitrary countable total order.

---

## 3. What does not count

The following do not resolve the problem.

1. **Reproving the known \(K\ge3\) bound.**
2. **Constructing a permutation avoiding six-term or five-term progressions.**  
   The latter is already known from Adenwalla and only proves \(K\le4\).
3. **Showing that every permutation has a monotone four-term AP under extra hypotheses**, such as bounded displacement, periodicity, computability, prescribed growth, positive density conditions, or symmetry.
4. **Proving the result only for permutations of a finite interval \([-N,N]\)** or for all \(N\) below a computational threshold.
5. **Producing arbitrarily large finite permutations avoiding monotone four-term APs.**  
   Such finite orders need not converge to an enumeration of \(\mathbb Z\).
6. **Producing an arbitrary countable total order avoiding four-term APs.**  
   A permutation in the intended sense must have order type \(\omega\): it has a least element, and every element has only finitely many predecessors.
7. **A construction that omits some integers, repeats integers, or lists only \(\mathbb N\).**
8. **Avoiding only increasing progressions** if “monotone” includes both orientations.
9. **Average-case or random-order heuristics.**  
   There is no canonical uniform random permutation of a countably infinite set, and almost-sure statements would not settle a universal question.
10. **Conditional results**, unless the invoked conjecture is also proved.
11. **Asymptotic reductions** such as showing that a long initial segment “usually” contains the desired pattern.
12. **Applications of Erdős–Szekeres producing an arbitrary monotone subsequence.**  
    The selected values must themselves form an arithmetic progression.
13. **Applications of van der Waerden to a coloring not shown to encode occurrence order consistently.**

---

## 4. Known results and context

### 4.1 Elementary lower bound \(K\ge3\)

Every one-sided permutation of \(\mathbb Z\) contains an increasing three-term arithmetic progression.

Let \(a=\pi(0)\), the first term, and suppose no increasing three-term AP occurs. For every \(d>0\), the progression
\[
a,\ a+d,\ a+2d
\]
cannot occur in increasing order. Since \(p_\pi(a)=0\), both other terms occur later, so necessarily
\[
p_\pi(a+2d)<p_\pi(a+d).
\]
Taking \(d=2^j\) gives
\[
p_\pi(a+2^{j+1})<p_\pi(a+2^j)
\qquad(j\ge0).
\]
Thus
\[
p_\pi(a+1)>p_\pi(a+2)>p_\pi(a+4)>\cdots
\]
would be an infinite strictly decreasing sequence of nonnegative integers, impossible. Therefore a monotone three-term AP exists.

Hence
\[
K\ge3.
\]

This proof depends essentially on a first position. It must not be silently transferred to a doubly infinite ordering.

### 4.2 Geneson’s upper bound

According to the database commentary, Geneson [Ge19] proved
\[
K\le5.
\]
In concrete terms, this means the existence of a permutation of \(\mathbb Z\) with no monotone six-term arithmetic progression.

The off-by-one is important: constructing an example avoiding length \(6\) proves that length \(6\) is not universally forced, hence \(K\le5\).

### 4.3 Adenwalla’s improvement

Adenwalla [Ad22] proved
\[
K\le4,
\]
that is, constructed a permutation with no monotone five-term arithmetic progression.

Combining this with the elementary lower bound gives
\[
\boxed{3\le K\le4}.
\]

Thus the previously known \(K\le5\) bound is superseded for the exact numerical problem, although its construction may still contain useful ideas.

### 4.4 Relevant general theorems

Several standard theorems are relevant as tools but do not directly settle the problem.

- **Erdős–Szekeres monotone subsequence theorem.**  
  Every sequence of \((r-1)(s-1)+1\) distinct real numbers contains an increasing subsequence of length \(r\) or a decreasing subsequence of length \(s\). Here it does not ensure that the selected values form an AP.

- **Van der Waerden’s theorem.**  
  Every finite coloring of \(\mathbb Z\) contains arbitrarily long monochromatic arithmetic progressions. A successful application would need a finite coloring derived from occurrence-order data such that a monochromatic configuration forces compatible position inequalities.

- **Ramsey’s theorem.**  
  Pair or tuple comparisons can be homogenized on infinite subsets, but an arbitrary infinite subset of \(\mathbb Z\) need not contain even a three-term AP.

- **Compactness and Kőnig-type arguments.**  
  Finite AP-avoiding orders may have a limiting total order. The main difficulty is that compactness typically does not preserve order type \(\omega\). The limit can have no least element, infinitely many predecessors below an element, or a dense/non-discrete order type.

The database also cross-references Problems #194 and #196. Their exact statements should be consulted before transferring results; the present commentary alone does not specify which variants they concern.

---

## 5. Traps and edge cases

### 5.1 Exclude zero common difference

The common difference must satisfy \(d>0\). Allowing \(d=0\) makes every repeated constant tuple an AP, but a permutation has no repetitions and this is not the intended notion.

### 5.2 “Monotone” concerns occurrence order

The progression values are
\[
a<a+d<\cdots<a+(k-1)d.
\]
They are monotone in the permutation only if their positions are monotone. Merely finding all of them somewhere in the permutation is vacuous, since the permutation contains every integer.

### 5.3 Both orientations must be checked

Avoiding
\[
a,a+d,a+2d,a+3d
\]
as a subsequence does not automatically avoid
\[
a+3d,a+2d,a+d,a.
\]
A counterexample must exclude both unless the source convention is explicitly one-sided.

### 5.4 Finite compactness is especially dangerous

There are often highly structured finite AP-avoiding orders obtained by residue-class recursion. Passing to a subsequential limit may yield a total order on \(\mathbb Z\), but not one realizable as
\[
\pi(0),\pi(1),\pi(2),\ldots.
\]

For an order \(\prec\) on \(\mathbb Z\) to arise from such a permutation, every element must have finitely many predecessors:
\[
\#\{y:y\prec x\}<\infty
\quad\text{for every }x.
\]

### 5.5 Infinite concatenation of infinite residue classes is invalid

A proposed order such as “list all odds, then all evens” is not a one-sided permutation: the first infinite block is never completed. Residue-class constructions must be interleaved through finite blocks or otherwise prove fairness.

### 5.6 Finite-prefix avoidance does not imply extendibility

A finite prefix can contain no forbidden AP but still be a dead end relative to a prescribed fairness requirement. Conversely, every finite set may admit a good order while no coherent sequence of such orders has order type \(\omega\).

### 5.7 Surjectivity is often the hidden failure

A greedy rule can continue forever while postponing one integer forever. Showing infinitely many distinct outputs is not enough; every positive and negative integer must eventually occur.

### 5.8 Reversing an \(\omega\)-order is not an \(\omega\)-order

Reversing the entire sequence would produce order type \(\omega^\ast\), not another one-sided enumeration. Symmetry arguments involving reversal must instead use a valid operation such as value negation
\[
\pi(n)\mapsto-\pi(n),
\]
and even then the orientation implications must be checked.

### 5.9 A longer AP contains consecutive shorter APs

A monotone \(m\)-term AP with \(m\ge4\) contains a monotone four-term AP in any four consecutive terms. Thus avoiding four-term APs automatically avoids every longer length. Nonconsecutive subsets need not retain the same common difference, so use consecutive terms when invoking this.

### 5.10 Growth estimates alone are unlikely to contradict enumeration

An enumeration can delay an integer arbitrarily long. A lower bound such as
\[
p_\pi(n)\ge f(|n|)
\]
for a very rapidly growing \(f\) is not by itself a contradiction. A proof must force either an actual infinite descent in \(\mathbb N_0\), infinitely many predecessors below one element, or permanent omission of an integer.

### 5.11 The first-term argument weakens at length four

For \(a=\pi(0)\), avoidance of the increasing four-term progression only says that
\[
p(a+d),p(a+2d),p(a+3d)
\]
are not in increasing order. Unlike the three-term case, this does not force a single inequality and therefore does not immediately yield a descending chain.

---

## 6. Verification hooks

### 6.1 Direct checker for a finite prefix

Given a finite list of distinct integers
\[
w=(w_0,\ldots,w_{m-1}),
\]
construct the position dictionary
\[
p_w(w_i)=i.
\]

For every \(a,d\) such that
\[
a,a+d,a+2d,a+3d
\]
all belong to the listed set, check whether
\[
p_w(a)<p_w(a+d)<p_w(a+2d)<p_w(a+3d)
\]
or the reverse chain holds.

This is a correct test for forbidden configurations already completed inside the prefix.

A practical enumeration avoids looping over all \((a,d)\): for every ordered pair of listed values \(u<v\), test whether \(v-u\) can serve as one, two, or three common-difference units and query the remaining terms in a hash table.

### 6.2 Incremental “forbidden next value” computation

Suppose a good prefix is being extended by appending a new value \(y\). Since \(y\) is last in occurrence order, it can complete a monotone four-term AP only as a numerical endpoint.

- If the prefix already contains
  \[
  a,\ a+d,\ a+2d
  \]
  in that occurrence order, then appending
  \[
  y=a+3d
  \]
  is forbidden.

- If the prefix already contains
  \[
  a+3d,\ a+2d,\ a+d
  \]
  in that occurrence order, then appending
  \[
  y=a
  \]
  is forbidden.

Thus a program can maintain a dynamic set of currently forbidden endpoint values. This is useful for testing greedy or priority constructions and detecting finite dead ends.

### 6.3 SAT/SMT encoding for finite sets

For a finite \(S\subset\mathbb Z\), introduce Boolean variables
\[
B_{u,v}\quad(u\ne v,\ u,v\in S),
\]
meaning “\(u\) precedes \(v\).” Impose:

- \(B_{u,v}\leftrightarrow\neg B_{v,u}\),
- transitivity,
- optionally a designated least element.

For every \(a,d\) with
\[
a,a+d,a+2d,a+3d\in S,
\]
forbid
\[
B_{a,a+d}\wedge B_{a+d,a+2d}\wedge B_{a+2d,a+3d}
\]
and its reverse.

This can search for finite forbidden-order patterns, forced inequalities, or minimal unsatisfiable cores. Finite satisfiability alone is not a counterexample.

### 6.4 Testing first-element forcing

Normalize the first term to \(0\) by translation. Search over finite sets such as

\[
\{0\}\cup\{id:1\le i\le M,\ d\in D\},
\]
or affine grids
\[
\{id+je:0\le i,j\le M\},
\]
with \(0\) constrained to be first. Enumerate all AP-avoiding orders or use SAT to extract implications of the form
\[
p(u)<p(v).
\]

The useful output is not merely unsatisfiability, but a small collection of local implications that can be iterated to force an infinite descent.

### 6.5 Candidate-construction stress tests

For a proposed recursive construction, compute:

1. the first \(10^m\) outputs for increasing \(m\);
2. the largest \(N\) such that every integer in \([-N,N]\) has appeared;
3. the minimum and maximum positions of \([-N,N]\);
4. all monotone four-term APs completed so far;
5. the number and structure of currently forbidden next values;
6. whether particular small integers are repeatedly postponed.

The coverage statistic is crucial for detecting a hidden failure of surjectivity.

### 6.6 Residue-pattern analysis

For a candidate based on \(2\)-adic or \(q\)-adic valuations, enumerate every possible residue pattern of a four-term AP modulo \(q^r\). For each pattern, record:

- the valuation of each term;
- which blocks contain the four terms;
- the induced block order;
- whether within-block recursion can still make all four positions monotone.

This finite table can reveal the exact cross-block configurations that invalidate a substitution construction.

---

## 7. Attack routes

### Route 1: Forced infinite descent from the first term

**Core mechanism.**  
Generalize the elementary proof for three terms. Let \(a=\pi(0)\). For each \(d>0\), avoidance of
\[
a,a+d,a+2d,a+3d
\]
places a restriction on the six possible orders of
\[
a+d,\ a+2d,\ a+3d.
\]
Use overlapping progressions at differences \(d,2d,3d,\ldots\) to force an infinite descending chain of positions.

**Key lemma needed.**  
A finite system of implications showing that every realizable assignment of order types to the triples
\[
(a+d,a+2d,a+3d),\quad
(a+2d,a+4d,a+6d),\quad\ldots
\]
eventually forces
\[
p(u_0)>p(u_1)>p(u_2)>\cdots
\]
for distinct integers \(u_i\).

**Why it might work.**  
The three-term lower bound already has exactly this structure. Length four merely replaces one forced inequality by a finite set of allowed order types. Overlaps among scaled APs may eliminate all but cyclic or descending behavior.

**Most likely failure point.**  
The extra order-type freedom may allow compatible switching between patterns, preventing a uniform descending chain.

**Quick blockage test.**  
Use SAT on multiplicatively closed finite sets such as
\[
\{a+2^i3^j:0\le i,j\le r\},
\]
with \(a\) first. If large instances admit highly periodic order-type assignments with no long forced descent, the simplest version of this route is likely blocked.

---

### Route 2: Finite-coloring and affine-grid Ramsey theory

**Core mechanism.**  
Color each positive difference \(d\) by the relative position order of
\[
a+d,\ a+2d,\ a+3d,
\]
possibly enriched by a bounded amount of comparison data. Apply van der Waerden, Ramsey, or a finite affine-grid theorem to find many related differences with identical color. Use overlap consistency to derive a forbidden monotone four-term AP.

**Key lemma needed.**  
A finite realizable coloring of differences such that a monochromatic arithmetic or multiplicative configuration forces a cycle of strict inequalities or directly forces a monotone four-term AP.

**Why it might work.**  
The obstruction is translation- and dilation-invariant in the values. Homogenizing the finite order types of several affine copies is a natural way to turn this invariance into rigid position inequalities.

**Most likely failure point.**  
Van der Waerden gives equal colors but not necessarily the exact shared vertices needed to compare the corresponding position inequalities. The coloring may also require unbounded contextual data.

**Quick blockage test.**  
Generate all realizable colorings on \(\{1,\ldots,N\}\) induced by finite AP-avoiding orders. Check whether large monochromatic configurations coexist with consistent position orders. If they do, the chosen coloring is too coarse.

---

### Route 3: Order-type obstruction—show that every avoiding order is not \(\omega\)

**Core mechanism.**  
Forget the numerical position labels and study total orders \(\prec\) on \(\mathbb Z\) with no monotone four-term AP. Characterize a structural feature forced by avoidance, then prove that every such order has either no least element or some element with infinitely many predecessors. Either conclusion rules out order type \(\omega\).

**Key lemma needed.**  
For every four-AP-avoiding total order \(\prec\) on \(\mathbb Z\), there exists \(x\in\mathbb Z\) such that
\[
\{y:y\prec x\}
\]
is infinite, or there is an infinite strictly descending \(\prec\)-chain below every proposed least element.

**Why it might work.**  
Compactness may well produce AP-avoiding total orders; the unresolved issue is precisely whether one can have the very rigid order type \(\omega\). An order-theoretic obstruction targets that distinction directly.

**Most likely failure point.**  
Four-term avoidance may be flexible enough to admit well-founded orders, and the known five-term-avoiding construction shows that closely related local constraints are compatible with order type \(\omega\).

**Quick blockage test.**  
Construct large finite orders with a designated least element and minimize the maximum number of predecessors forced below selected central elements. Stable bounded behavior would weaken this route; rapidly growing forced predecessor sets would support it.

---

### Route 4: Hierarchical residue-class or \(p\)-adic construction aimed at disproof

**Core mechanism.**  
Build an order recursively by residue classes or valuations, for example using \(v_2(n-c)\), with carefully chosen reversals between levels. The goal is that every four-term AP crosses levels in a pattern that prevents its positions from being monotone.

**Key lemma needed.**  
A finite substitution rule on residue classes such that:

1. every four-term AP has a first level where its terms split among blocks;
2. the induced block order is nonmonotone;
3. within-block recursion handles APs remaining in one block;
4. finite-block scheduling yields a genuine enumeration of all integers.

**Why it might work.**  
Parity and valuation recursions are effective for finite AP-avoidance problems, and the existing upper-bound constructions may have related multiscale structure. Four-term APs have constrained residue patterns modulo small powers of \(2\) or \(3\).

**Most likely failure point.**  
A naive “all of one residue class before another” recursion produces an order not of type \(\omega\). Fair interleaving can destroy the block-order protection. APs with common difference divisible by high powers of the modulus also survive deep into the recursion.

**Quick blockage test.**  
Enumerate all four-AP residue patterns modulo \(2^r\) or \(3^r\), then test candidate block orders by SAT. Reject any rule for which a cross-block AP can be monotone independently of the recursive within-block orders.

---

### Route 5: Priority or online construction aimed at disproof

**Core mechanism.**  
Construct the permutation from left to right. At each stage, append an unused integer that does not complete a monotone four-term AP, while assigning priorities to ensure every integer is eventually selected.

**Key lemma needed.**  
An extension/fairness lemma such as:

> For every finite good prefix and every finite target set \(T\) of unlisted integers, there is a bounded-length good extension that lists at least one designated high-priority member of \(T\).

A stronger version would show that among any sufficiently large interval there is always an admissible next value.

**Why it might work.**  
Appending a new term can only complete a forbidden progression as its numerical endpoint. Therefore the forbidden-next-value set has an explicit description in terms of previously ordered three-term APs.

**Most likely failure point.**  
The forbidden endpoint set may eventually cover every value in a neighborhood of the current highest-priority omitted integer, allowing it to be postponed forever. A greedy construction may be infinite and injective but non-surjective.

**Quick blockage test.**  
Implement several fairness schedules and compute the forbidden-next-value set after each stage. Search by SAT or backtracking for finite good prefixes from which a designated omitted integer cannot be appended within any extension of length \(L\), for increasing \(L\).

---

### Route 6: Computer-assisted extraction of a finite forcing calculus

**Core mechanism.**  
Use SAT/SMT to analyze finite affine configurations and extract minimal unsatisfiable cores or universally forced comparisons. Convert these computational observations into a small, human-checkable inference system whose iteration proves a monotone four-term AP must occur.

**Key lemma needed.**  
A finite list of certified implications of the form
\[
\text{specified order relations}+\text{no monotone 4-AP}
\Longrightarrow u\prec v,
\]
together with a scheme that iterates the implications indefinitely from the least element.

**Why it might work.**  
The local constraint is finite and purely order-theoretic. Automated reasoning is well suited to finding nonobvious overlapping AP configurations that force comparison cycles.

**Most likely failure point.**  
Every finite configuration may be satisfiable, with the obstruction—if any—depending essentially on an unbounded sequence of scales. Large SAT instances could then produce examples without revealing a finite forcing rule.

**Quick blockage test.**  
Search systematically for small affine sets with a designated least element whose AP-avoidance constraints force a long descending comparison chain. If chain length grows with the size of the affine grid and the certificates exhibit a stable recursive pattern, this route is promising.

---

## 8. Verdict on difficulty

The problem is sharply reduced but genuinely open:

\[
\boxed{K\in\{3,4\}.}
\]

The remaining task is not a routine application of van der Waerden, Erdős–Szekeres, or compactness. Its central difficulty is the interaction between:

- local forbidden order patterns on four-term APs;
- the global requirement that the order have type \(\omega\);
- the absence of any bound on how long an enumeration may postpone a given integer.

The known construction avoiding five-term progressions shows that very long monotone APs can be globally suppressed while retaining a valid enumeration. On the other hand, the elementary three-term proof suggests that the existence of a first element can force infinite descent through dilation. Length four is exactly where the simple forced-inequality argument ceases to work.

No equivalence to a famous major conjecture such as Szemerédi’s theorem, the polynomial van der Waerden theorem, or a standard Ramsey-theoretic open problem is known from the supplied context. It should therefore be treated as a focused but difficult infinite ordering problem, not as a disguised solved theorem and not presently as a known consequence of a famous conjecture.

The decisive target is:

\[
\boxed{\text{Either prove every order of type }\omega\text{ on }\mathbb Z
\text{ contains a monotone 4-AP, or construct one that does not.}}
\]