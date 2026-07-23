# Problem Brief: Erdős Problem #881

## 1. PRECISE STATEMENT

### 1.1 Standard conventions

Let  
\[
\mathbb N_0=\{0,1,2,\dots\}.
\]
Replacing \(\mathbb N_0\) by \(\mathbb N=\{1,2,\dots\}\) changes only finite initial issues and should not affect the asymptotic problem.

For \(A\subseteq\mathbb N_0\) and an integer \(h\ge 1\), define the \(h\)-fold sumset
\[
hA=\{a_1+\cdots+a_h:a_1,\dots,a_h\in A\}.
\]
Summands may be repeated.

The standard reading here should be **asymptotic additive basis**:

- \(A\) is an asymptotic basis of order at most \(h\) if \(hA\) is cofinite in \(\mathbb N_0\), i.e.
  \[
  \exists N_0\ \forall n\ge N_0,\quad n\in hA.
  \]
- Its exact order is
  \[
  \operatorname{ord}(A)=\min\{h\ge 1:hA\text{ is cofinite}\},
  \]
  with \(\operatorname{ord}(A)=\infty\) if no such \(h\) exists.

Thus “\(A\) is a basis of order \(k\)” most naturally means
\[
\operatorname{ord}(A)=k.
\]

If \(hA\) is cofinite and \(a\in A\), then
\[
a+hA\subseteq (h+1)A,
\]
so \((h+1)A\) is also cofinite. Hence being a basis of order at most \(h\) is monotone in \(h\).

### 1.2 Formal statement

For every integer \(k\ge 1\), suppose \(A\subseteq\mathbb N_0\) satisfies:

1. \(\operatorname{ord}(A)=k\); and
2. for every infinite set \(B\subseteq A\),
   \[
   \operatorname{ord}(A\setminus B)\ne k.
   \]

Because \(A\setminus B\subseteq A\), its order cannot be less than \(k\). Thus condition 2 is equivalently
\[
\forall B\subseteq A\ \bigl(B\text{ infinite}\implies
\forall N\ \exists n\ge N:\ n\notin k(A\setminus B)\bigr).
\]

The question is whether there must exist an infinite \(B\subseteq A\) such that
\[
\operatorname{ord}(A\setminus B)=k+1.
\]
Equivalently, does there exist an infinite \(B\subseteq A\) and a threshold \(N_1\) such that
\[
\forall n\ge N_1,\qquad n\in (k+1)(A\setminus B)?
\]

The premise already implies that \(A\setminus B\) is not a basis of order \(k\), so if \((k+1)(A\setminus B)\) is cofinite, then its exact order is automatically \(k+1\).

### 1.3 Terminological warning

The property called “minimal” in the database statement is specifically:

> no infinite subset can be deleted while preserving order \(k\).

This is weaker than the usual pointwise notion of a minimal basis,
\[
\forall a\in A,\quad A\setminus\{a\}\text{ is not a basis of order }k.
\]
Indeed, pointwise minimality implies the database property, but not conversely.

Some authors use “basis of order \(k\)” merely to mean that \(kA\) is cofinite, without requiring \(k\) to be least. Under that reading, the clean formal version is
\[
kA\text{ cofinite},\qquad
\forall B\subseteq A\text{ infinite},\ k(A\setminus B)\text{ not cofinite},
\]
and asks whether \((k+1)(A\setminus B)\) is cofinite for some infinite \(B\). The exact-order interpretation is the more standard one and makes the intended “increase from \(k\) to \(k+1\)” explicit.

A non-asymptotic interpretation requiring representation of every integer is unlikely to be intended: finite initial obstructions would dominate the deletion question.

---

## 2. WHAT COUNTS AS A SOLUTION

### 2.1 Complete affirmative solution

A complete proof must establish, for every relevant \(k\) and every \(A\) satisfying the premise, the existence of a **single infinite set**
\[
B\subseteq A
\]
and a **single finite threshold** \(N_1=N_1(A,B)\) such that
\[
\forall n\ge N_1,\quad
n=c_1+\cdots+c_{k+1}
\]
for some \(c_1,\dots,c_{k+1}\in A\setminus B\).

It is not enough to find a different deletion set \(B_n\) for each \(n\), or different sets for different finite intervals.

The proof must also verify that \(B\) is infinite. The premise then supplies
\[
k(A\setminus B)\text{ is not cofinite},
\]
so the surviving set has exact order \(k+1\).

A proof for every \(k\ge 2\), together with the elementary \(k=1\) argument below, would settle the problem completely.

### 2.2 Complete disproof

A disproof must produce some integer \(k\ge 1\) and some explicitly defined \(A\subseteq\mathbb N_0\) such that:

1. **Initial basis property**
   \[
   kA\text{ is cofinite},
   \]
   and, under the exact-order convention,
   \[
   hA\text{ is not cofinite for every }h<k.
   \]

2. **Infinite-deletion minimality**
   \[
   \forall B\subseteq A\text{ infinite},\quad
   k(A\setminus B)\text{ is not cofinite}.
   \]
   Equivalently, for every infinite \(B\subseteq A\), there are arbitrarily large integers having no \(k\)-term representation using only \(A\setminus B\).

3. **Failure of the desired conclusion**
   \[
   \forall B\subseteq A\text{ infinite},\quad
   (k+1)(A\setminus B)\text{ is not cofinite}.
   \]
   Equivalently,
   \[
   \forall B\subseteq A\text{ infinite}\ \forall N\
   \exists n\ge N:\quad n\notin (k+1)(A\setminus B).
   \]

For an explicit construction, finite computations may verify local gadgets or initial scales, but the three infinite assertions above require proofs. In particular, checking many deletion sets of bounded size is not sufficient to verify the universal quantifier over all infinite \(B\).

A useful sufficient certificate for conditions 2 or 3 would be a scheme assigning to every infinite \(B\) infinitely many “witness integers” \(n_j(B)\), together with a proof that every relevant representation of \(n_j(B)\) uses at least one element of \(B\).

---

## 3. WHAT DOES NOT COUNT

The following would not resolve the problem:

1. Finding arbitrarily large finite \(B\), rather than one infinite \(B\).
2. Showing that every finite initial segment of a proposed infinite deletion can be made safely.
3. Producing an infinite \(B\) for which \(A\setminus B\) remains a basis of some order
   \[
   H>k+1.
   \]
4. Proving that \((k+1)(A\setminus B)\) has density \(1\), contains arbitrarily long intervals, or misses only a zero-density set. Cofiniteness is required.
5. Showing that infinitely many, rather than all sufficiently large, integers are representable.
6. Proving the result only for bases with positive density, regular growth, bounded gaps, many representations, or another additional hypothesis.
7. A conditional proof using an unproved representation-function conjecture.
8. An asymptotic improvement such as a surviving basis of order \(O(k)\), \(2k\), or \(k+O(1)\).
9. A randomized construction for which each fixed integer is representable with high probability, unless it is also proved that with positive probability all sufficiently large integers are simultaneously represented and infinitely many elements are deleted.
10. A computational search over finite truncations without a rigorous passage to the infinite set.
11. Replacing “delete an infinite subset” by “delete one element.”
12. Proving the statement only for \(k=1\), which is elementary and does not settle the open range \(k\ge2\).

---

## 4. KNOWN RESULTS AND CONTEXT

### 4.1 Database commentary

The supplied database commentary contains only the word “Previous,” apparently a navigation artifact, and gives no substantive theorem, reference, or partial result. Thus there is no database-supplied progress to summarize beyond the status **OPEN**.

### 4.2 The case \(k=1\) is affirmative

This part is elementary.

If \(\operatorname{ord}(A)=1\), then \(A\) is cofinite. The minimality premise is automatic: deleting an infinite \(B\subseteq A\) leaves infinitely many integers absent, so \(A\setminus B\) is not a basis of order \(1\).

Choose \(M\) such that every integer at least \(M\) belongs to \(A\), and put
\[
B=\{2^j:2^j\ge M\}.
\]
Then \(B\subseteq A\) is infinite. Let
\[
C=A\setminus B.
\]

For sufficiently large \(n\), consider integers
\[
c\in [n/3,2n/3].
\]
Both \(c\) and \(n-c\) are at least \(M\). The forbidden values are those for which either \(c\) or \(n-c\) is a power of \(2\). There are only \(O(\log n)\) such values, while the interval has \(\asymp n\) integers. Hence some \(c\) satisfies
\[
c,n-c\in C,
\]
and therefore \(n\in 2C\). Thus \(C\) is a basis of order \(2\), but not of order \(1\).

Consequently, the genuinely open range is \(k\ge2\), unless the original source explicitly imposed \(k\ge2\).

### 4.3 Elementary structural observations

For \(C\subseteq A\), inclusion gives
\[
hC\subseteq hA.
\]
Therefore deleting elements can never decrease exact order.

The target can also be written as
\[
(k+1)C=C+kC
\]
being cofinite, where \(C=A\setminus B\). Thus the problem asks for a co-infinite subset \(C\subseteq A\) such that \(kC\) has infinitely many gaps but the extra translate-union \(C+kC\) fills all sufficiently large gaps.

### 4.4 Essential elements

An element \(a\) of an asymptotic basis \(A\) is called **essential** if
\[
A\setminus\{a\}
\]
is not an asymptotic basis of any finite order.

A classical theorem, usually associated with Erdős–Graham and later refinements on bounds, states:

> Every asymptotic basis has only finitely many essential elements.

A consequence is that one can repeatedly delete a nonessential element and retain some finite-order basis at every finite stage. This does not solve the problem:

- the orders may grow beyond \(k+1\);
- the thresholds may diverge;
- the intersection after infinitely many deletions may cease to be a basis of every finite order.

These three failures are central obstacles.

### 4.5 Kneser-type structure

Kneser’s theorem and its asymptotic variants are relevant whenever failure of basis behavior is caused by periodicity or a modular obstruction. For example, if a set is trapped in unsuitable residue classes modulo \(q\), then its \(h\)-fold sumset misses an entire residue class and hence cannot be cofinite.

However, not every nonbasis has a modular explanation. Very thin or irregular gap sets can avoid all fixed congruence obstructions. Kneser theory is therefore a structural tool, not an automatic solution.

### 4.6 Representation-function warning

Let
\[
r_h(n;A)=\#\{(a_1,\dots,a_h)\in A^h:a_1+\cdots+a_h=n\},
\]
with an ordered or unordered convention fixed as needed.

Any approach that assumes abundant or increasingly many representations should be treated cautiously. Already for order \(2\), the Erdős–Turán conjecture asserts that the representation function of an asymptotic basis of order \(2\) is unbounded. That conjecture remains open. Problem #881 is not known to be equivalent to Erdős–Turán, but a route requiring strong uniform multiplicity of representations may be attempting something at least as difficult as major open representation-function questions.

---

## 5. TRAPS AND EDGE CASES

1. **“Minimal” is not ordinary minimality.**  
   The hypothesis concerns deletion of infinite subsets only. It does not say that deleting a single element destroys order \(k\).

2. **Exact order versus order at most \(k\).**  
   State the convention. Under the exact-order reading, inclusion guarantees that a subset of \(A\) cannot have order below \(k\).

3. **Exactly \(h\) summands.**  
   The standard sumset \(hA\) uses exactly \(h\) summands, with repetition. “At most \(h\)” is not literally identical unless \(0\in A\), although asymptotic shifting arguments give monotonicity in \(h\).

4. **Repeated summands matter.**  
   A representation may use the same \(a\in A\) several times. Deleting \(a\) destroys the entire representation; in hypergraph language the edge is its support, which may have size less than \(h\).

5. **The threshold depends on \(B\).**  
   The desired \(N_1\) may depend on the selected infinite deletion set. No uniform threshold over all possible \(B\) is required.

6. **One \(B\), not a sequence of \(B_n\).**  
   Local choices for individual target integers do not combine automatically.

7. **Finite-stage preservation does not imply preservation in the limit.**  
   Even if every finite deletion \(B_j\) leaves a basis, the intersection
   \[
   A\setminus\bigcup_j B_j
   \]
   may have infinite order.

8. **Threshold drift.**  
   A nested sequence \(C_1\supseteq C_2\supseteq\cdots\), each a basis of order \(k+1\), may have thresholds tending to infinity, while the intersection is not a basis.

9. **Density-one is insufficient.**  
   A sumset can have density \(1\) and still miss infinitely many integers.

10. **Sparse deletion is not automatically harmless.**  
    A set \(B\) may be very sparse numerically but contain elements uniquely responsible for representations of infinitely many integers.

11. **Modular obstructions can be created by deleting finitely many elements.**  
    For example, finitely many exceptional residue representatives can be essential to breaking a gcd obstruction. Thus “finite changes do not matter asymptotically” is false for additive-basis status.

12. **The negation is universal.**  
    To disprove the statement one must defeat every infinite \(B\subseteq A\), not merely exhibit one bad deletion.

13. **\(B=A\) is allowed in the premise.**  
    It is harmless there, since the empty set is not a basis. In the conclusion \(B=A\) is impossible because the complement must be a basis.

14. **Compactness must enforce infinitely many deletions.**  
    A limit of finite masks can converge to the undeleted set \(A\) unless distinct deletions are explicitly forced at successive stages.

15. **Small \(k\).**  
    The case \(k=1\) is affirmative as above. Any proposed counterexample must therefore have \(k\ge2\).

---

## 6. VERIFICATION HOOKS

All computations should exploit nonnegativity: representations of \(n\) use only elements of \(A\cap[0,n]\).

### 6.1 Sumset bitsets

For a finite truncation \(C\cap[0,U]\), represent it by a Boolean bitset and compute
\[
hC\cap[0,U]
\]
using repeated Boolean convolution or bitset shifting.

For each \(h\), record:

- the missing integers in a window \([L,U]\);
- the longest final interval contained in \(hC\);
- empirical thresholds;
- the change under deletion of selected elements.

This is useful for testing examples but cannot prove cofiniteness without additional structure.

### 6.2 Representation hypergraphs

For fixed \(n,h,A\), form a hypergraph \(\mathcal H_h(n)\):

- vertices: \(A\cap[0,n]\);
- hyperedges: supports of \(h\)-term representations of \(n\).

Then:

- \(n\in h(A\setminus B)\) iff some edge of \(\mathcal H_h(n)\) is disjoint from \(B\);
- deleting \(B\) destroys every representation of \(n\) iff \(B\) is a transversal of \(\mathcal H_h(n)\).

Compute:

- the transversal number \(\tau_h(n)\);
- the maximum number \(\nu_h(n)\) of pairwise vertex-disjoint representations;
- elements occurring in every representation;
- representation-support frequency.

These statistics directly test proposed redundancy lemmas.

### 6.3 SAT or integer-programming formulation

Use variables \(x_a\in\{0,1\}\), where \(x_a=1\) means \(a\) is retained. For each target \(n\), impose
\[
\bigvee_{e\in\mathcal H_h(n)}\ \bigwedge_{a\in e}x_a.
\]
This requires at least one surviving representation.

Add constraints forcing deletions in successive bands:
\[
\sum_{a\in A\cap[I_j,I_{j+1})}(1-x_a)\ge1.
\]
This is a finite analogue of requiring infinitely many deletions.

One can search for masks retaining all \((k+1)\)-representations in a large window while forcing \(k\)-gaps.

### 6.4 Finite analogue of the minimality premise

For \(A_U=A\cap[0,U]\), ask whether there exists a deletion set \(B_U\) of prescribed size or with one deletion in each block such that every \(n\in[L,U]\) remains in \(k(A_U\setminus B_U)\).

If such large structured deletions repeatedly exist, they may suggest an affirmative construction. If no such deletion exists, extract minimal unsatisfiable cores to locate “private” representations or fragile elements.

This is only diagnostic: the true premise quantifies over infinite deletions and arbitrarily large witnesses.

### 6.5 Gap-correlation checks

For \(C=A\setminus B\), compute
\[
G_k(C)=\mathbb N_0\setminus kC.
\]
Since
\[
n\notin (k+1)C
\quad\Longleftrightarrow\quad
n-c\in G_k(C)\ \text{for every }c\in C,\ c\le n,
\]
test whether translates \(n-C\) are contained in the \(k\)-gap set.

Useful statistics include:

- density and run lengths of \(G_k(C)\);
- intersections \((n-C)\cap kC\);
- correlations between \(C\) and translates of \(G_k(C)\).

### 6.6 Modular gadget search

For small moduli \(q\), enumerate \(D\subseteq\mathbb Z/q\mathbb Z\) and compute
\[
hD=D+\cdots+D.
\]
Search for deletion-sensitive gadgets satisfying variants of:

- \(kD=\mathbb Z/q\mathbb Z\);
- after deleting designated elements, \(kD'\ne\mathbb Z/q\mathbb Z\);
- after designated deletions, also \((k+1)D'\ne\mathbb Z/q\mathbb Z\).

Such gadgets may support a block or mixed-radix counterexample. They are not by themselves sufficient because representations may cross blocks or use carries.

### 6.7 Mixed-radix and block-construction checks

For proposed digital constructions:

1. enumerate all carries at each radix boundary;
2. verify that every integer in a scale interval has a \(k\)-representation;
3. identify all representations of proposed witness integers;
4. ensure that representations using adjacent or distant blocks do not bypass the intended obstruction;
5. test the construction for several concatenated scales, not merely one local gadget.

---

## 7. ATTACK ROUTES

### Route 1: Probabilistic sparse deletion via representation redundancy

**Core mechanism.**  
Choose infinitely many elements of \(A\) for deletion with very small, nonuniform probabilities. Try to show that every sufficiently large \(n\) retains a \((k+1)\)-term representation.

**Key lemma needed.**  
A useful form would be:

> For all sufficiently large \(n\), the hypergraph of \((k+1)\)-representations of \(n\) contains sufficiently many suitably independent or pairwise disjoint edges, with quantitative growth strong enough to make the probability that all representations are hit summable in \(n\).

Then Borel–Cantelli, a local lemma, or an alteration argument could yield one infinite deletion set preserving all large \(n\).

**Why it might work.**  
The extra summand may introduce substantial flexibility: one can vary one summand \(a\in A\) and represent \(n-a\) by \(k\) elements. Extremely sparse deletion can be arranged to be infinite while having finite expected impact on each representation family.

**Likely failure point.**  
Minimality under infinite deletion does not obviously imply high representation multiplicity. A basis may have many integers with very few or highly overlapping representations. For \(k=2\), even proving weak general multiplicity statements can approach unresolved Erdős–Turán-type territory.

**Quick obstruction test.**  
Compute \(\nu_{k+1}(n)\), the maximum number of vertex-disjoint representations, for structured candidate bases. If \(\nu_{k+1}(n)\) remains bounded along an infinite sequence, the simplest independent-deletion argument is blocked.

---

### Route 2: Iterative deletion of nonessential elements with controlled order

**Core mechanism.**  
Use the theorem that every asymptotic basis has only finitely many essential elements. Delete one nonessential element at a time, producing
\[
A=C_0\supset C_1\supset C_2\supset\cdots,
\]
where each \(C_j\) remains an asymptotic basis of some finite order.

**Key lemma needed.**  
One needs a strong controlled-order and uniformity statement, for example:

> At every stage, there is a nonessential element whose deletion leaves a basis of order at most \(k+1\), and the choices can be made so that the limiting intersection has a uniform \((k+1)\)-basis threshold.

A weaker but still useful lemma would provide nested “safe deletion” choices together with a compactness invariant preventing threshold drift.

**Why it might work.**  
The premise guarantees that an infinite final deletion cannot preserve order \(k\). Therefore, if the limiting survivor remains a basis of order at most \(k+1\), it must have exact order \(k+1\).

**Likely failure point.**  
After a single deletion, the least order may jump above \(k+1\). Even if every finite stage has order \(k+1\), the thresholds can diverge and the intersection can fail to be a basis.

**Quick obstruction test.**  
For explicit bases, greedily delete each nonessential candidate and compute the least observed order and threshold in large windows. Rapid order growth or threshold drift indicates that a naive iterative scheme will not close.

---

### Route 3: Gap-set covering and additive-density methods

**Core mechanism.**  
Write \(C=A\setminus B\). The target is
\[
C+kC=(k+1)C
\]
cofinite even though \(kC\) is not cofinite. Let
\[
G=\mathbb N_0\setminus kC.
\]
Then a large \(n\) fails to lie in \((k+1)C\) exactly when
\[
n-C\subseteq G.
\]
Try to choose an infinite sparse deletion so that \(G\) remains too small or too unstructured to contain any full translate \(n-C\) for large \(n\).

**Key lemma needed.**  
A possible target is:

> There exists a co-infinite \(C\subseteq A\) such that \(kC\) has infinitely many gaps but, uniformly for all sufficiently large \(n\), some \(c\in C\) satisfies \(n-c\in kC\).

This might follow from density, syndeticity, additive energy, or a correlation estimate between \(C\) and the gap set of \(kC\).

**Why it might work.**  
The premise requires the deletion to create infinitely many \(k\)-gaps, but it does not require those gaps to be dense. The extra translate by all of \(C\) may fill a very sparse or poorly correlated gap set.

**Likely failure point.**  
Bases may have zero density, and deleting a numerically sparse set can create highly structured gaps. Density-one of \(kC\) alone would still not imply cofiniteness of \(C+kC\).

**Quick obstruction test.**  
For candidate deletions, compute \(G\) and search for large \(n\) satisfying \(n-C\subseteq G\) over long finite windows. Persistent aligned patterns suggest that density alone is insufficient.

---

### Route 4: Kneser theory and classification of deletion-created obstructions

**Core mechanism.**  
Analyze why \(k(A\setminus B)\) ceases to be cofinite. Attempt to show that a carefully chosen sparse deletion creates only a “one-level” obstruction that disappears after one more summand.

**Key lemma needed.**  
A strong structural statement would be:

> For some infinite sparse \(B\subseteq A\), every obstruction to \(k(A\setminus B)\) being cofinite is eventually periodic, and the surviving residue classes satisfy
> \[
> (k+1)(A\setminus B)\equiv \mathbb Z/q\mathbb Z
> \]
> modulo every relevant period \(q\).

Alternatively, prove that if every infinite deletion also destroys the \((k+1)\)-basis property, then a fixed modular obstruction already forces a contradiction with \(kA\) being cofinite.

**Why it might work.**  
Finite exceptional elements and residue-class obstructions are central in the theory of essential elements. The difference between \(k\) and \(k+1\) often has a transparent finite-group formulation.

**Likely failure point.**  
Failure of cofiniteness need not be periodic. Thin, scale-dependent gaps can evade any fixed modulus, especially in block constructions.

**Quick obstruction test.**  
For finite models, compute missing residues of \(kC\) and \((k+1)C\) modulo many small \(q\). If the observed gaps show no stable periodic signature as the truncation grows, a pure Kneser approach is unlikely to suffice.

---

### Route 5: Compactness, Baire category, or an infinite extension tree

**Core mechanism.**  
View subsets \(C\subseteq A\) as points of the Cantor space \(\{0,1\}^A\). For fixed \(n\), the condition
\[
n\in (k+1)C
\]
depends on only finitely many coordinates, because all summands are at most \(n\). Build a finitely branching tree of partial retention masks that:

- delete a new element at each scale;
- preserve representations of increasingly many integers;
- maintain an extension invariant.

Apply König’s lemma or a category argument to obtain an infinite branch.

**Key lemma needed.**  
An extension lemma of the form:

> Every admissible finite mask that has deleted \(j\) prescribed elements can be extended to delete a new element while preserving all \((k+1)\)-representations required up to the next scale and retaining the ability to continue indefinitely.

The invariant must control future integers, not just the current finite window.

**Why it might work.**  
Membership of a fixed \(n\) in \((k+1)C\) is a finite-coordinate condition, so this is naturally a compactness problem. Infinite deletion can be forced by requiring one new zero-coordinate in each designated band.

**Likely failure point.**  
Finite-window feasibility need not imply a globally extensible branch. A choice harmless below \(U\) can be indispensable for infinitely many larger integers. Also, the property “all sufficiently large integers are represented” is not a simple open condition.

**Quick obstruction test.**  
Implement the extension tree for increasing cutoffs. Measure whether partial masks that survive one scale have any children at the next. If all branches die after bounded depth unless deletions stop, the required extension lemma is false in that model.

---

### Route 6: Disproof by block or mixed-radix construction

**Core mechanism.**  
Construct a highly nonuniform basis in separated scales. At each scale, install a finite gadget whose representations are fragile. Arrange that every infinite deletion meets infinitely many active scales, producing infinitely many missing integers not only in the \(k\)-fold sumset but also in the \((k+1)\)-fold sumset.

**Key lemma needed.**  
One needs local gadgets and a concatenation theorem with the following properties:

1. the undeleted global set is a basis of exact order \(k\);
2. deletion of a designated element or class at a scale forces a \(k\)-term witness gap at that scale;
3. the same deletion forces a \((k+1)\)-term witness gap;
4. representations using other scales or carries cannot repair the witness;
5. every infinite \(B\subseteq A\) triggers infinitely many distinct scales.

A useful finite model may be a digit set in a large cyclic group or a carry-free interval gadget.

**Why it might work.**  
The universal quantifier over infinite \(B\) is naturally attacked by scale separation: every infinite set must affect infinitely many blocks or affect one block type infinitely often. Private witness intervals can convert this into infinitely many additive failures.

**Likely failure point.**  
Cross-block representations are extremely difficult to exclude. The extra \((k+1)\)-st summand may repair a local obstruction even when \(k\)-term representations are rigid. Moreover, local conditions such as \(kD\) covering all residues tend to make \((k+1)D\) more robust after deletion.

**Quick obstruction test.**  
Search exhaustively for small finite cyclic gadgets with the required deletion sensitivity. Then concatenate two or three scales and enumerate all cross-scale representations of the proposed witness integers. If bypass representations appear immediately, the gadget does not globalize.

---

## 8. VERDICT ON DIFFICULTY

The case \(k=1\) is elementary and affirmative. The open substance is \(k\ge2\).

For \(k\ge2\), the problem appears genuinely difficult because it simultaneously requires:

- an infinite deletion;
- preservation of a sharp order bound \(k+1\);
- a single uniform tail of represented integers;
- control over all interactions among infinitely many deletion choices;
- exploitation of a premise that gives only negative information about \(k\)-fold representations.

There is no supplied evidence that the problem is equivalent to a famous conjecture. In particular, no equivalence to the Erdős–Turán representation-function conjecture is known. However, any attack that assumes broad representation redundancy—especially for \(k=2\)—risks running directly into unresolved Erdős–Turán-type difficulties.

The most promising proof strategies are likely those that use either:

1. a controlled infinite-deletion/compactness lemma specifically exploiting the extra summand; or
2. a structural classification of how an infinite deletion can destroy order \(k\).

The most plausible disproof strategy is a rapidly separated block or digital construction, but the universal control of \((k+1)\)-representations across scales is a severe obstacle.

Overall assessment: **high difficulty, with a substantial gap between finite-stage intuition and the required infinite uniform conclusion.**