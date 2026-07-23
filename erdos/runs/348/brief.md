# Problem Brief: Erdős Problem #348 — Deletion-Robust Complete Sequences

## 1. Precise statement

### 1.1 Sequences and subset sums

Let  
\[
A=(a_i)_{i\ge 1},\qquad 1\le a_1\le a_2\le \cdots,
\]
be an infinite nondecreasing sequence of positive integers. Repetitions are allowed and are treated as distinct indexed occurrences. Thus, for example, the two initial \(1\)'s in the Fibonacci sequence are two different removable elements.

For an index set \(I\subseteq \mathbb N\), write
\[
A\setminus I=(a_i)_{i\in \mathbb N\setminus I}.
\]
Its finite restricted subset-sum set is
\[
\Sigma(A\setminus I)
=
\left\{
\sum_{i\in F}a_i:
F\subseteq \mathbb N\setminus I\text{ finite}
\right\}.
\]
Each indexed term may be used at most once. The empty sum \(0\) is allowed.

### 1.2 Weak completeness: the intended open problem

The standard weak or asymptotic notion of completeness is:

> \(A\) is **complete** if there exists \(N_0\in\mathbb N\) such that
> \[
> [N_0,\infty)\cap\mathbb Z\subseteq \Sigma(A).
> \]
> Equivalently, only finitely many nonnegative integers fail to be representable as sums of distinct indexed terms of \(A\).

For an integer \(r\ge 0\), define:

- \(A\) is **\(r\)-deletion robust** if
  \[
  \forall I\subseteq\mathbb N,\quad |I|=r
  \implies A\setminus I\text{ is complete}.
  \]

- \(A\) is **universally \(r\)-deletion fragile** if
  \[
  \forall J\subseteq\mathbb N,\quad |J|=r
  \implies A\setminus J\text{ is not complete}.
  \]
  In expanded form,
  \[
  \forall J,\ |J|=r,\ \forall N_0,\ \exists x\ge N_0
  \quad x\notin\Sigma(A\setminus J).
  \]

The problem, under the most literal reading of “after removing any \(n\) elements,” is:

> **Classify all integer pairs \(0\le m<n\) for which there exists an infinite nondecreasing sequence \(A\) of positive integers that is \(m\)-deletion robust and universally \(n\)-deletion fragile.**

### 1.3 Quantifier ambiguity

The phrase “\(A\) is not complete after removing any \(n\) elements” can also be read existentially:

\[
\exists J\subseteq\mathbb N,\quad |J|=n,\qquad A\setminus J\text{ is not complete}.
\]

This is the natural “fault-tolerance threshold” reading: every deletion of \(m\) terms is harmless, but some deletion of \(n\) terms is fatal. It is strictly weaker than universal \(n\)-fragility.

The brief will use the **universal reading**, because that is the literal force of “any \(n\) elements.” Any proposed solution should nevertheless state explicitly whether it proves the universal or only the existential version. If consultation of the original Erdős–Graham formulation shows that the existential reading was intended, the quantifier must be changed throughout.

### 1.4 Strong completeness

The stronger notion mentioned in the database is:

\[
\Sigma(A)=\mathbb N_0.
\]

For positive nondecreasing sequences this is equivalent, by the standard interval-covering or Brown criterion, to
\[
a_1=1,\qquad
a_k\le 1+\sum_{i<k}a_i\quad(k\ge2).
\]

The strong version is not the intended open problem: van Doorn’s theorem settles the range \(2\le m<n\) negatively.

### 1.5 Immediate monotonicity

Because adding available summands cannot destroy representations:

1. If \(A\) is \(m\)-deletion robust, then it is \(r\)-deletion robust for every \(0\le r\le m\).

   Indeed, extend an \(r\)-element deletion set to one of size \(m\); the smaller-deletion sequence contains a complete subsequence.

2. If \(A\) is universally \(n\)-deletion fragile, then it is universally \(s\)-deletion fragile for every \(s\ge n\).

   Every \(s\)-deletion sequence is a subsequence of some \(n\)-deletion sequence.

Thus a construction for \((m,n)\) automatically gives constructions for every
\[
0\le m'\le m,\qquad n'\ge n,\qquad m'<n'.
\]

For the existential interpretation, a fatal \(n\)-set can similarly be enlarged, so existential \(n\)-fragility implies existential \(s\)-fragility for \(s\ge n\).

---

## 2. What counts as a solution

### 2.1 A full solution of the classification problem

A complete solution must give a set
\[
\mathcal P\subseteq\{(m,n)\in\mathbb Z^2:0\le m<n\}
\]
and prove both directions:

1. **Existence:** For every \((m,n)\in\mathcal P\), construct a sequence \(A_{m,n}\) and prove:
   \[
   \forall I,\ |I|=m,\quad A_{m,n}\setminus I\text{ is weakly complete},
   \]
   and
   \[
   \forall J,\ |J|=n,\quad A_{m,n}\setminus J\text{ is weakly incomplete}.
   \]

2. **Nonexistence:** For every \((m,n)\notin\mathcal P\), prove that no infinite nondecreasing positive-integer sequence has those two properties.

A result settling only \((2,3)\) would resolve the first explicitly open case, but not necessarily the whole classification.

### 2.2 What an existence construction must verify

For every \(m\)-element deletion set \(I\), one must produce or prove the existence of a threshold \(N(I)\) such that
\[
x\ge N(I)\implies x\in\Sigma(A\setminus I).
\]
The threshold may depend on \(I\); no uniform threshold is required unless separately proved.

For every \(n\)-element deletion set \(J\), one must prove there are infinitely many omitted integers:
\[
\forall X\ \exists x\ge X,\qquad x\notin\Sigma(A\setminus J).
\]
Exhibiting a single missing integer is insufficient for weak incompleteness.

The proof must cover deletion of arbitrary indexed occurrences, including arbitrarily large indices and, when values repeat, each possible choice of occurrence.

### 2.3 What an explicit counterexample to a proposed nonexistence theorem must contain

For example, an explicit counterexample to the natural conjecture “no pair with \(m\ge2\) is possible” would be a sequence for some \(2\le m<n\), ideally \(m=2,n=3\), together with rigorous proofs of both universal deletion statements above.

The sequence should be given by a formula, recurrence, effective algorithm, or other mathematically unambiguous specification. Numerical checks on long prefixes are not sufficient verification.

### 2.4 What a nonexistence proof for \((2,3)\) must show

It must prove:

> For every weakly complete sequence \(A\) that remains weakly complete after deletion of every two indexed terms, there exists at least one three-element index set \(J\) for which \(A\setminus J\) is still weakly complete.

This is the exact negation of universal \(3\)-fragility. Under the existential interpretation, the required conclusion would be much stronger: every sequence robust under all two-deletions must remain complete after every three-deletion.

---

## 3. What does not count

None of the following resolves the weak problem.

1. **Strong completeness only.**  
   Showing that a deletion leaves one integer unrepresentable proves failure of strong completeness, not weak completeness.

2. **A finite number of missing integers.**  
   Weak incompleteness requires infinitely many missing integers.

3. **Checking only bounded deletions.**  
   Verifying deletion sets contained in \(\{1,\dots,L\}\) does not cover deletion of arbitrarily late terms.

4. **Checking only consecutive or equal-valued deletions.**  
   The quantifier ranges over every set of indexed occurrences.

5. **Showing that some \(n\)-deletion is fatal under the universal reading.**  
   This proves only the existential variant.

6. **Showing that “most” \(m\)-deletions preserve completeness.**  
   Every \(m\)-element deletion must do so.

7. **Positive density or density \(1\) of subset sums.**  
   Even a density-one subset of \(\mathbb N\) can have infinitely many exceptions.

8. **Unbounded representation counts on average.**  
   Robustness concerns avoidance of prescribed deleted terms, not merely the total number of representations.

9. **Conditional results**, unless the condition is also proved.

10. **Asymptotic improvements**, such as proving that the number of exceptions below \(X\) is \(o(X)\).

11. **Finite computation alone.**  
    Long-prefix searches can falsify candidate lemmas or discover patterns, but cannot establish eventual completeness or infinitely many gaps without a general argument.

12. **Unrestricted coin representations.**  
    Each occurrence may be used at most once; arguments based on arbitrary nonnegative multiplicities address a different problem.

---

## 4. Known results and context

### 4.1 Powers of two

Let
\[
A=(1,2,4,8,\dots).
\]
Every nonnegative integer has a unique binary representation, so \(A\) is strongly complete.

If \(2^j\) is deleted, precisely those integers whose binary expansion requires the \(j\)-th bit become unavailable. Infinitely many integers are then missing. Hence \(A\) realizes \((m,n)=(0,1)\), in both the strong and weak senses.

By monotonicity, the same sequence realizes
\[
(m,n)=(0,n)\qquad\text{for every }n\ge1
\]
under the universal interpretation.

### 4.2 Fibonacci sequence

Let
\[
F_1=F_2=1,\qquad F_{k+2}=F_{k+1}+F_k,
\]
and take
\[
A=(F_1,F_2,F_3,\dots)=(1,1,2,3,5,8,\dots).
\]

The database states that this sequence realizes \((1,2)\). In particular:

- deleting any one indexed Fibonacci term leaves a complete sequence;
- deleting any two indexed Fibonacci terms leaves a weakly incomplete sequence.

The one-deletion strong completeness can be checked from Brown’s criterion. If \(F_j\) has been deleted, then at the next surviving Fibonacci term the deficit is exactly compensated by the recurrence, and all later Brown inequalities continue to hold.

The two-deletion weak incompleteness is stronger than merely observing a failed Brown inequality. Its proof uses persistent gap propagation in the Fibonacci numeration system and is related to Zeckendorf-type representation structure.

By monotonicity, Fibonacci therefore gives all pairs
\[
(m,n)=(1,n)\qquad(n\ge2),
\]
as well as pairs with \(m=0,n\ge2\), already covered by powers of two.

Thus, under the database interpretation, every pair with \(m\le1\) is known to be possible.

### 4.3 The first open case

The database explicitly identifies
\[
(m,n)=(2,3)
\]
as open for weak completeness.

No weakly complete sequence is known that survives every two-term deletion but becomes weakly incomplete after every three-term deletion, and no impossibility theorem is known.

This is the first unresolved point beyond the powers-of-two and Fibonacci phenomena.

### 4.4 van Doorn’s theorem for strong completeness

Van Doorn proved that under strong completeness there is no such sequence for
\[
2\le m<n.
\]

Combining this with powers of two, Fibonacci, and monotonicity gives a complete classification of the strong version:

\[
\boxed{\text{Strong version is possible exactly when }m\in\{0,1\}.}
\]

Therefore any positive construction for \((2,3)\) must exploit the allowance of finitely many exceptional integers in an essential way. It cannot remain strongly complete after every two-deletion.

### 4.5 Brown’s criterion

For a nondecreasing positive sequence \(b_1\le b_2\le\cdots\),
\[
\Sigma((b_i))=\mathbb N_0
\]
if and only if
\[
b_1=1,\qquad b_k\le 1+\sum_{i<k}b_i\quad(k\ge2).
\]

This is extremely useful for strong completeness and for constructing finite intervals of subset sums, but a failure of the inequality proves only that some finite gap exists. It does not by itself prove weak incompleteness.

### 4.6 Relation to additive-basis theory

Weakly complete sequences are restricted additive bases in which each indexed term is available at most once. Classical results about asymptotic bases with unrestricted repeated use do not transfer automatically.

Deletion fragility is closely related to “essential elements” or finite essential subsets of additive bases, but the restricted-sum setting is materially different. Any import from ordinary additive-basis theory must be re-proved for distinct indexed summands.

---

## 5. Traps and edge cases

### 5.1 Weak versus strong completeness

This is the central trap. A single missing integer, or even any fixed finite set of missing integers, is compatible with weak completeness.

For an \(n\)-deletion sequence to be weakly incomplete, one needs an unbounded sequence of missing integers.

### 5.2 Indexed occurrences versus values

For
\[
A=(1,1,2,3,\dots),
\]
the two \(1\)'s are distinct elements. Deleting the first \(1\), the second \(1\), or both are different indexed operations even if some resulting multisets coincide.

All deletion sets should be subsets of the index set \(\mathbb N\).

### 5.3 The scope of “any”

Under the universal reading,
\[
\forall J,\ |J|=n,\quad A\setminus J\text{ is incomplete}.
\]
A proof for one specially chosen \(J\) does not suffice.

Because the wording is genuinely ambiguous under negation, every paper or computational report must state the quantifier explicitly.

### 5.4 Thresholds are deletion-dependent

From
\[
\forall I,\ |I|=m,\quad A\setminus I\text{ is complete}
\]
one obtains
\[
\forall I\ \exists N(I)\ \forall x\ge N(I):x\in\Sigma(A\setminus I).
\]
One may not interchange the first two quantifiers without proof. There need not be a single threshold working for every \(m\)-deletion.

This blocks many naïve compactness and representation-multiplicity arguments.

### 5.5 Finite modifications are not harmless

Weak completeness in this restricted setting is not automatically invariant under finite deletion or finite addition. Powers of two are the basic counterexample: removing one term creates infinitely many gaps.

Likewise, a finite set of exceptional “residue correctors” can turn a highly structured tail into a complete sequence. One must track finite prefixes carefully.

### 5.6 Repeated bounded terms

The definition does not force \(a_i\to\infty\).

- Infinitely many copies of \(1\) make the sequence strongly complete after every finite deletion, so such a sequence can never be finitely deletion-fragile.
- Infinite repetitions of other values may produce modular phenomena.

A nonexistence proof must either handle bounded sequences or prove quickly that universal finite-deletion fragility forces \(a_i\to\infty\).

### 5.7 Modular obstructions are sufficient but not necessary

A congruence class omitted by all subset sums is a useful certificate of incompleteness. However, weak incompleteness need not arise from a fixed modulus. Persistent gaps can move between residue classes and scales, as in numeration systems.

Conversely, a gcd calculation alone is generally insufficient because finitely many exceptional terms can supply missing residue classes.

### 5.8 Failure of Brown’s inequality is local

If
\[
b_k>1+\sum_{i<k}b_i,
\]
then some integers below \(b_k\) are missing. Later terms cannot fill gaps below \(b_k\), but this yields only finitely many omissions unless a mechanism produces analogous gaps at infinitely many later scales.

### 5.9 Ordering and deletion

After deletion, the remaining sequence is automatically nondecreasing, but index formulas must account for skipped positions. Off-by-one mistakes are especially common in Fibonacci prefix-sum identities:
\[
\sum_{i=1}^{k}F_i=F_{k+2}-1.
\]

### 5.10 Monotonicity works only in the stated directions

- Robustness descends from \(m\) to smaller deletion counts.
- Universal fragility ascends from \(n\) to larger deletion counts.

Robustness at \(m\) says nothing automatic about \(m+1\), and fragility at \(n\) says nothing automatic about \(n-1\).

### 5.11 Representation multiplicity is not enough

If an integer has three representations, deleting two terms may still destroy all three if the representations share a small transversal. The relevant statistic is the minimum size of a set of indexed terms meeting every representation, not the raw number of representations.

---

## 6. Verification hooks

These computations cannot by themselves solve the problem, but they can test candidate constructions and lemmas.

### 6.1 Prefix subset-sum bitsets

For a finite prefix \(a_1,\dots,a_L\), compute
\[
P_L(x)=1\iff x\in\Sigma(a_1,\dots,a_L)
\]
using a bitset:
```text
reachable = bitset with bit 0 set
for a in terms:
    reachable |= reachable << a
```

For a deletion set \(D\subseteq\{1,\dots,L\}\), omit the corresponding updates.

This permits exact testing of:

- longest represented intervals;
- first missing integer;
- number and distribution of gaps;
- effects of all \(m\)- and \(n\)-deletions in a finite window.

### 6.2 Finite interval propagation certificate

Suppose a finite prefix of a remaining sequence has subset sums containing a full interval
\[
[L,U].
\]
If the next term \(b\) satisfies
\[
b\le U-L+1,
\]
then using or not using \(b\) gives
\[
[L,U]\cup[L+b,U+b]=[L,U+b].
\]

Thus, if one can verify a finite interval and then prove inductively that every later term is no larger than the current interval length, eventual completeness follows.

This gives a code-friendly positive certificate:

1. Find a full interval in a prefix bitset.
2. Propagate its right endpoint through the remaining terms.
3. Prove symbolically that propagation never fails beyond the tested range.

For deletion robustness, this must be done uniformly in the structural type of every allowed deletion set.

### 6.3 Brown-criterion checks

For strong completeness after a deletion \(D\), scan the remaining ordered terms and verify:
\[
b_1=1,\qquad b_k\le1+\sum_{i<k}b_i.
\]

This is useful for checking Fibonacci claims and for confirming that any proposed \(m\ge2\) construction necessarily leaves the strong regime somewhere.

### 6.4 Representation hypergraphs and transversal numbers

For each target \(x\), enumerate all representations
\[
\mathcal R_x=\{F\subseteq\{1,\dots,L\}:\sum_{i\in F}a_i=x\}.
\]
Treat \(\mathcal R_x\) as a hypergraph on the indices. Compute its transversal number
\[
\tau(x)=\min\{|D|:D\cap F\ne\varnothing\text{ for every }F\in\mathcal R_x\}.
\]

Interpretation:

- \(\tau(x)>m\) means no \(m\)-deletion can destroy all prefix representations of \(x\).
- \(\tau(x)\le n\) identifies a candidate fatal deletion for \(x\).

Track whether the same deletion set kills infinitely many targets or whether fatal sets drift with \(x\).

### 6.5 Gap propagation in recurrence sequences

For a recurrence candidate such as
\[
a_{k+r}=c_1a_{k+r-1}+\cdots+c_ra_k,
\]
compute subset-sum supports after deletion patterns and record normalized gaps relative to \(a_k\).

Search for a finite-state description in which a gap state at scale \(k\) forces a gap state at scale \(k+1\). A proved recurrent state or cycle can certify infinitely many missing integers.

The first candidates to test are generalized Fibonacci, tribonacci, and mixed-radix redundant systems.

### 6.6 SAT/MILP search for finite models

Search for finite nondecreasing sequences satisfying surrogate constraints:

- for every two-deletion pattern in a bounded prefix, a long terminal interval is representable;
- for every three-deletion pattern, at least one large test target is unrepresentable;
- prescribed growth constraints intended to make interval or gap propagation inductive.

This can identify plausible recurrences or show that a proposed local template is impossible. It cannot establish universal asymptotic claims without an accompanying theorem.

### 6.7 Modular-state searches

For a candidate deletion pattern, compute subset-sum residues modulo \(q\) by finite-state DP. Search over small moduli for a residue class permanently forbidden by the recurrence or block structure.

A finite-prefix residue omission alone is not a proof; one needs a symbolic invariant showing the omission persists through all later terms.

---

## 7. Attack routes

### Route 1: Convert weak completeness into a deletion-stable interval theorem

**Core idea.**  
Weak completeness should manifest as the eventual creation of long consecutive intervals of subset sums. Try to show that completeness after every two-deletion forces enough overlapping intervals that at least one three-deletion also remains complete.

**Key lemma needed.**  
A useful form would be:

> If every two-deletion \(A\setminus I\) is complete, then there exists a three-element set \(J\) and a finite prefix of \(A\setminus J\) whose subset sums contain an interval long enough to propagate through the entire tail.

A stronger uniform version might extract a finite set of interval certificates that cover all sufficiently late two-deletion configurations.

**Why it might work.**  
There are only three two-element subsets of a fixed triple \(J\). Their completeness might force overlapping representation intervals whose redundancy survives deletion of all three terms. Positivity and monotonicity make interval propagation particularly rigid once a sufficiently long interval exists.

**Likely failure point.**  
The completeness thresholds can depend arbitrarily on the deleted pair. There is no immediate uniformity over infinitely many deletion sets, and interval witnesses for different pairs may occur at unrelated scales.

**Quick obstruction test.**  
For random or recurrence-generated complete sequences, compute the earliest propagating interval after each two-deletion among the first \(L\) indices. If these witness scales grow wildly and no triple shares compatible certificates, the needed uniform lemma is likely false in that form.

---

### Route 2: Representation hypergraphs and finite transversals

**Core idea.**  
For each integer \(x\), regard its representations as a hypergraph \(\mathcal R_x\) on the term indices. A deletion set destroys \(x\) exactly when it is a transversal of \(\mathcal R_x\).

Two-deletion robustness says that for every fixed pair \(I\), all sufficiently large \(x\) have a representation disjoint from \(I\). Universal three-deletion fragility says that for every triple \(J\), infinitely many \(x\) have all representations meeting \(J\).

**Key lemma needed.**  
A compactness or sunflower-type theorem showing that these two patterns cannot coexist, for example:

> If every pair fails to be a transversal of \(\mathcal R_x\) for all sufficiently large \(x\), with the threshold depending on the pair, then some triple also eventually fails to be a transversal.

Alternatively, exploit special structural restrictions on representation hypergraphs arising from positive subset sums.

**Why it might work.**  
The problem is fundamentally about hitting all representations with a small set of terms. Hypergraph language isolates the exact combinatorial obstruction and may permit Helly-type, sunflower, or fractional-transversal arguments.

**Likely failure point.**  
Arbitrary hypergraphs can certainly exhibit complicated pair/triple behavior. The argument must use arithmetic structure, and the order of quantifiers prevents simply asserting that \(\tau(x)\ge3\) for every sufficiently large \(x\).

**Quick obstruction test.**  
Compute \(\tau(x)\), minimal transversals, and their supports for finite candidate sequences. Determine whether three-element transversals recur for infinitely many simulated scales while no fixed pair does. If this behavior already occurs robustly in natural recurrences, a general abstract hypergraph theorem will be insufficient.

---

### Route 3: Generalized numeration systems — a route toward disproof

**Core idea.**  
Search for a weak construction for \((2,3)\) based on a recurrence more redundant than Fibonacci. The intended analogy is:

- powers of two: zero-deletion robustness, one-deletion fragility;
- Fibonacci: one-deletion robustness, two-deletion fragility;
- a higher-order recurrence might give two-deletion robustness, three-deletion fragility.

Candidates include tribonacci-type sequences, recurrences with repeated initial terms, and controlled perturbations of linear recurrences.

**Key lemma needed.**  
For a candidate \(A\), prove both:

1. after any two deletions, a sufficiently long interval of subset sums appears and propagates forever;
2. after any three deletions, a recurrent forbidden state or canonical-representation obstruction produces infinitely many gaps.

**Why it might work.**  
Fibonacci deletion behavior comes from exact carry propagation. Higher-order numeration systems provide more local redundancy while potentially retaining global criticality.

**Likely failure point.**  
Simple higher-order recurrences may be too redundant: after three deletions they may still be weakly complete. Alternatively, they may fail two-deletion robustness for specially positioned deletions. Van Doorn’s theorem guarantees that no candidate can satisfy the corresponding strong conditions, so finite initial gaps are unavoidable and must somehow be harmless after two deletions but recurrent after three.

**Quick obstruction test.**  
For each candidate recurrence, enumerate all deletion patterns among the first \(L\) positions and compute gaps up to several multiples of the largest term. Classify patterns by relative spacings and look for:

- two-deletion gaps that stop propagating;
- three-deletion gaps that recur at increasing scales.

If a single two-deletion pattern shows stable recurrent gaps, discard the candidate.

---

### Route 4: Mixed-radix blocks with controlled carry propagation — another disproof route

**Core idea.**  
Build \(A\) in blocks corresponding to digit positions. Each digit should have enough redundant terms to tolerate two deletions, while any three deletions should disrupt carries at infinitely many later scales.

A naïve block construction fails because a finite deletion affects only finitely many blocks. The construction therefore needs global coupling: deleting a term in one block must alter carry possibilities at all later blocks.

**Key lemma needed.**  
A coding theorem producing a restricted digit system with:

- two-erasure correction for every finite pair of term erasures;
- three-erasure failure yielding an infinite family of forbidden integers;
- monotone positive place values and finite-use terms.

**Why it might work.**  
The problem resembles an erasure-correcting code embedded into a numeration system. Weak completeness allows finitely many low-level decoding failures, which is exactly the flexibility unavailable in van Doorn’s strong setting.

**Likely failure point.**  
Ordinary block independence makes finite deletions asymptotically irrelevant. Global coupling may restore fragility but also cause a two-deletion error to propagate indefinitely, violating robustness.

**Quick obstruction test.**  
Implement the proposed carry automaton. For each state induced by deleting up to three terms, determine whether the automaton eventually reaches a “full digit coverage” state or enters a recurrent deficient cycle. The desired state diagram has all two-deletion states absorbing into completeness and every three-deletion state entering a deficient cycle.

---

### Route 5: Lift weak completeness to strong completeness and invoke van Doorn

**Core idea.**  
Try to prove that an alleged weak \((2,3)\) example can be normalized, shifted, or finitely augmented to produce a strong example with the same deletion behavior, contradicting van Doorn.

**Key lemma needed.**  
Something close to:

> If \(A\) is complete after every two-deletion and incomplete after every three-deletion, then there is a finite modification \(A'\) that is strongly complete after every two-deletion while remaining incomplete after every three-deletion.

A weaker version could extract a strongly complete tail subsystem preserving the deletion pattern.

**Why it might work.**  
Weak completeness differs from strong completeness only by finitely many exceptions for each fixed deletion. If two-deletion robustness forces enough uniformity over those exceptions, they might be repaired simultaneously by finitely many added terms.

**Likely failure point.**  
The exceptional sets and thresholds may depend on the deleted pair, with no finite uniform bound. Adding repair terms can also destroy three-deletion fragility by introducing new representations. Finite modifications are not neutral in this problem.

**Quick obstruction test.**  
On candidate families, measure the maximum missing value after pair deletions among indices up to \(L\). If this maximum appears to grow without bound as the deleted indices grow, no straightforward finite repair theorem can hold.

---

### Route 6: Generating functions and support rigidity

**Core idea.**  
Encode subset sums formally by
\[
G_A(z)=\prod_{i\ge1}(1+z^{a_i}).
\]
The coefficient of \(z^x\) counts representations of \(x\). Deleting \(D\) replaces \(G_A\) by
\[
G_{A\setminus D}(z)
=
\frac{G_A(z)}{\prod_{i\in D}(1+z^{a_i})}
\]
as a formal product.

Completeness concerns eventual positivity of coefficients; fragility concerns infinitely many zero coefficients.

**Key lemma needed.**  
A support-rigidity theorem: if division by every product of two factors leaves eventually positive coefficients, then division by at least one product of three factors also leaves eventually positive coefficients—or, conversely, an explicit product construction violating this.

**Why it might work.**  
Deletion becomes an algebraic operation, and recurrence-based sequences often yield functional equations for \(G_A\). Roots of unity, automata, or Mahler-type functional equations may detect recurrent coefficient zeros.

**Likely failure point.**  
Coefficient support of infinite products is much harder than analytic nonvanishing. Cancellations are absent because coefficients are nonnegative, but eventual positivity remains a subtle combinatorial property. Generic complex-analytic information may be too coarse.

**Quick obstruction test.**  
Compute truncated products after all small deletion patterns and search for periodic or automatic zero sets. If gaps align with a fixed modulus or a finite automaton, generating-function methods become promising; if gap patterns are irregular, this route is less likely to close the problem.

---

## 8. Verdict on difficulty

The strong version is completely settled: van Doorn’s theorem rules out every \(2\le m<n\), while powers of two and Fibonacci supply all cases with \(m=0\) or \(1\).

The weak version is genuinely open already at \((2,3)\). The difficulty is not obtaining many representations, but reconciling two opposing universal properties:

- every prescribed pair of terms must eventually be avoidable in representations of all large integers;
- every prescribed triple must nevertheless hit all representations of infinitely many integers.

The dependence of completeness thresholds on the deleted set is the main logical obstruction to compactness and uniformity arguments. On the constructive side, finite deletions normally affect only finite local data, whereas the desired three-deletion failure must recur at arbitrarily large scales. Fibonacci achieves exactly such propagation for one-versus-two deletions, but no higher-order analogue is known.

There is no known equivalence to a famous conjecture such as the Riemann Hypothesis or a standard major additive-number-theory conjecture. Nonetheless, the first open case appears structurally difficult and may require a new theory of essential finite sets for restricted additive bases, or a novel numeration-system construction. The zero-dollar prize should not be interpreted as evidence that the problem is easy.