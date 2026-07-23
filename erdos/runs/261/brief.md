# Problem Brief: Erdős Problem #261

## 1. Precise statement

Let  
\[
\mathbb N=\{1,2,3,\dots\},\qquad w(r):=\frac r{2^r}\quad(r\in\mathbb N).
\]

For \(n\in\mathbb N\), define the property
\[
\mathcal F(n):
\quad
\exists\, t\in\mathbb Z,\ t\ge 2,\ \exists\,a_1,\dots,a_t\in\mathbb N
\]
such that

1. \(a_i\neq a_j\) whenever \(i\neq j\), and
2. 
   \[
   w(n)=\sum_{i=1}^t w(a_i).
   \]

Equivalently, \(\mathcal F(n)\) says that the singleton subsum \(w(n)\) has another representation as a finite subsum of the sequence
\[
\left(\frac r{2^r}\right)_{r\ge1},
\]
using at least two distinct indices.

The problem has three parts.

### Q1. Infinitely many \(n\)

Is
\[
\bigl|\{n\in\mathbb N:\mathcal F(n)\}\bigr|=\infty?
\]

This part is already settled affirmatively.

### Q2. Every \(n\)

Is
\[
\forall n\in\mathbb N,\quad \mathcal F(n)?
\]

This remains open according to the database, although it has been checked for \(n\le 10000\).

### Q3. Continuum many representations of a rational number

The standard intended interpretation is the following. For \(x\in\mathbb R\), define
\[
\mathcal R(x):=
\left\{
A\subseteq\mathbb N:
A\text{ is infinite and }
x=\sum_{a\in A}\frac a{2^a}
\right\}.
\]
The sum converges absolutely because
\[
\sum_{a=1}^{\infty}\frac a{2^a}=2.
\]

Equivalently, each \(A\in\mathcal R(x)\) may be encoded by its unique strictly increasing enumeration
\[
1\le a_1<a_2<a_3<\cdots
\]
satisfying
\[
x=\sum_{k=1}^{\infty}\frac{a_k}{2^{a_k}}.
\]

The question is whether
\[
\exists x\in\mathbb Q\quad
|\mathcal R(x)|\ge 2^{\aleph_0}.
\]
Since there are only \(2^{\aleph_0}\) subsets of \(\mathbb N\), “at least \(2^{\aleph_0}\)” is equivalent to “exactly \(2^{\aleph_0}\).”

### Important ambiguity in Q3

The phrase “solutions \((a_k)\)” must be interpreted as strictly increasing sequences, or equivalently as subsets of \(\mathbb N\). Otherwise the question is trivial:

- If arbitrary orderings count as different solutions, then a single infinite representation has continuum many permutations.
- For example,
  \[
  2=\sum_{n=1}^{\infty}\frac n{2^n},
  \]
  and the set \(\mathbb N\) has continuum many enumerations.

Thus counting ordered permutations cannot be the intended reading. Distinctness is also naturally inherited from the finite part of the problem.

It makes no material difference whether one allows finite subsets in the definition of the fiber: there are only countably many finite subsets of \(\mathbb N\), so a fiber has continuum cardinality with finite subsets allowed if and only if it has continuum many infinite representations.

---

## 2. Immediate structural reductions

### 2.1 Localization of the indices

The weights satisfy
\[
w(1)=w(2)=\frac12,
\]
and \(w(r)\) is strictly decreasing for \(r\ge2\).

Consequently:

- If \(n\ge3\), any representation witnessing \(\mathcal F(n)\) must have
  \[
  a_i>n\qquad\text{for every }i.
  \]
  Indeed, \(a_i<n\) would give \(w(a_i)>w(n)\), while \(a_i=n\) would already exhaust the target and leave no room for other positive terms.
- For \(n=2\), neither \(a=1\) nor \(a=2\) can occur in a representation with at least two terms, so again all \(a_i>2\).
- For \(n=1\), neither \(a=1\) nor \(a=2\) can occur, so all \(a_i\ge3\).

Since \(w(1)=w(2)\), the cases \(n=1\) and \(n=2\) are equivalent. In fact,
\[
\frac12=\frac3{2^3}+\frac6{2^6}+\frac8{2^8},
\]
so both are valid:
\[
\frac38+\frac6{64}+\frac8{256}
=\frac{12+3+1}{32}
=\frac12.
\]

Thus Q2 can be viewed, for \(n\ge2\), as asking whether \(w(n)\) is always a finite subsum of the strict tail \(\{w(k):k>n\}\).

### 2.2 Tail sums

For \(r\ge1\),
\[
\sum_{k=r}^{\infty}\frac{k}{2^k}
=\frac{r+1}{2^{r-1}}.
\]
Hence
\[
\sum_{k=n+1}^{\infty}\frac{k}{2^k}
=\frac{n+2}{2^n}> \frac n{2^n}.
\]

Moreover,
\[
\frac{k}{2^k}
<
\sum_{j=k+1}^{\infty}\frac j{2^j}
=\frac{k+2}{2^k}
\]
for every \(k\).

The standard interval-filling lemma for subsums therefore implies that the achievement set of every sufficiently late tail is a full interval. In particular, for every \(n\), \(w(n)\) has some representation as a subsum of later weights. That representation may be infinite. Thus the genuine issue in Q2 is finite termination, not existence of an arbitrary subset representation.

### 2.3 Integer form of a finite identity

Suppose
\[
\frac n{2^n}=\sum_{a\in A}\frac a{2^a}
\]
and \(M=\max A\). Since all relevant exponents satisfy \(M\ge n\), multiplying by \(2^M\) gives the exactly checkable integer identity
\[
n\,2^{M-n}=\sum_{a\in A}a\,2^{M-a}.
\]

For any nontrivial representation localized beyond \(n\), one has \(M>n\). Reducing the integer identity modulo \(2\) shows:

> **Parity condition:** the largest exponent \(M\) must be even.

Indeed, every term with \(a<M\) is even after multiplication by \(2^M\), and the left side is even, so the last term \(M\) must be even. Higher powers of \(2\) give further nested congruence restrictions involving the largest few selected indices.

---

## 3. What counts as a solution

Because the database entry contains multiple questions, each should be treated separately.

### 3.1 Q1

A proof of Q1 must exhibit or prove the existence of infinitely many distinct \(n\in\mathbb N\) satisfying \(\mathcal F(n)\).

This has already been done by the Borwein–Loring identity described below.

### 3.2 Q2: affirmative resolution

A complete affirmative solution must prove
\[
\forall n\in\mathbb N,\quad
\exists A_n\subset\mathbb N
\]
such that

- \(A_n\) is finite,
- \(|A_n|\ge2\),
- all members of \(A_n\) are distinct, and
- 
  \[
  \frac n{2^n}=\sum_{a\in A_n}\frac a{2^a}.
  \]

No uniform bound on \(|A_n|\) or \(\max A_n\) is required, unless used by the proof.

For \(n\ge2\), one may equivalently prove the existence of such an \(A_n\subset\{n+1,n+2,\dots\}\).

### 3.3 Q2: disproof

A complete disproof must produce some explicit \(n_0\in\mathbb N\) and prove
\[
\forall\text{ finite }A\subset\mathbb N,\quad
|A|\ge2
\implies
\sum_{a\in A}\frac a{2^a}\neq\frac{n_0}{2^{n_0}}.
\]

Merely searching up to some maximum exponent \(M\) is insufficient unless accompanied by a proved bound showing that every possible representation would have \(\max A\le M\).

A computer-assisted disproof would be acceptable if it supplies both:

1. a rigorous reduction to a finite search, for example a theorem bounding the largest exponent or a finite-state invariant excluding all larger exponents; and
2. a reproducible exact certificate for that finite search.

### 3.4 Q3: affirmative resolution

A complete affirmative solution must give a rational number \(x=p/q\) and prove that there are continuum many distinct subsets \(A\subseteq\mathbb N\) satisfying
\[
x=\sum_{a\in A}\frac a{2^a}.
\]

It is enough to construct an injection
\[
\{0,1\}^{\mathbb N}\hookrightarrow\mathcal R(x),
\]
or to construct a perfect binary tree of extendible partial representations.

There is also a useful descriptive-set-theoretic criterion. Define
\[
\Phi:\{0,1\}^{\mathbb N}\to[0,2],\qquad
\Phi(\varepsilon)=\sum_{n=1}^{\infty}\varepsilon_n\frac n{2^n}.
\]
This map is continuous, so every fiber \(\Phi^{-1}(x)\) is closed in Cantor space. By the Cantor–Bendixson/perfect set theorem, every uncountable closed subset of Cantor space has cardinality \(2^{\aleph_0}\). Therefore it is enough to prove that some rational fiber is uncountable.

### 3.5 Q3: disproof

A complete negative solution must prove
\[
\forall x\in\mathbb Q,\quad
|\mathcal R(x)|<2^{\aleph_0}.
\]

Under the standard set interpretation and the perfect set theorem, this is equivalent to proving that every rational fiber is countable. Exhibiting one rational with a unique or finite number of representations does not disprove the existential statement.

---

## 4. What does not count

### For Q2

The following do not resolve the all-\(n\) question:

- proving the property for infinitely many \(n\);
- proving it for all \(n\le N\), no matter how large \(N\) is;
- proving it for a positive-density or density-one set of \(n\);
- improving the Borwein–Loring family asymptotically;
- showing that every \(w(n)\) has an infinite tail representation;
- producing numerical approximations to the desired equality;
- proving the statement conditional on an unresolved conjecture;
- a bounded search with no a priori bound on the largest exponent.

### For Q3

The following are insufficient:

- finding a rational \(x\) with two, finitely many, or merely countably infinitely many representations;
- finding an irrational \(x\) with continuum many representations;
- counting different permutations of the same set of indices;
- allowing repetitions when the intended problem requires distinct indices;
- constructing continuum many representations whose sums depend on the binary choice;
- producing infinitely many independent equal-sum gadgets whose common total has not been proved rational;
- approximate equality rather than exact equality;
- probabilistic or entropy heuristics without a proof that a single rational fiber is uncountable.

---

## 5. Known results and context

### 5.1 Q1 is settled

For every positive integer \(m\), put
\[
n_m=2^{m+1}-m-2.
\]
Then
\[
\frac{n_m}{2^{n_m}}
=
\sum_{n_m<k\le n_m+m}\frac{k}{2^k}.
\]

Indeed,
\[
\sum_{j=1}^m\frac{n+j}{2^{n+j}}
=
\frac1{2^n}
\left(
n\sum_{j=1}^m2^{-j}
+
\sum_{j=1}^m j2^{-j}
\right),
\]
and
\[
\sum_{j=1}^m2^{-j}=1-2^{-m},
\qquad
\sum_{j=1}^m j2^{-j}=2-\frac{m+2}{2^m}.
\]
Thus
\[
\sum_{j=1}^m\frac{n+j}{2^{n+j}}
=
\frac1{2^n}
\left(
n+2-\frac{n+m+2}{2^m}
\right).
\]
For \(n=2^{m+1}-m-2\), one has \(n+m+2=2^{m+1}\), so the bracket equals \(n\).

To satisfy the requirement \(t\ge2\), take \(m\ge2\). The values \(n_m\) are strictly increasing, so this supplies infinitely many valid \(n\).

According to the database commentary:

- Erdős reported that Cusick had a simple proof of infinitude.
- Borwein and Loring [BoLo90] later gave the displayed construction.
- Thus the first question is not open.

### 5.2 Computation through \(10000\)

Tengely, Ulas, and Zygadlo [TUZ20] verified that
\[
\mathcal F(n)\quad\text{holds for every }n\le10000.
\]

This is substantial evidence for Q2 but does not settle it.

### 5.3 Achievement-set context

The sequence \(w(n)=n/2^n\) is positive, summable, and satisfies
\[
w(n)\le\sum_{k>n}w(k).
\]
The standard subsum interval theorem, often associated with Kakeya’s theory of achievement sets, gives
\[
\left\{
\sum_{n\in A}\frac n{2^n}:A\subseteq\mathbb N
\right\}
=[0,2].
\]

More strongly, every tail has an interval as its achievement set. Thus every target \(w(n)\) is representable by some subset of later indices. This does not force the representing subset to be finite.

### 5.4 The weakened “two representations” question

Under the standard subset interpretation, a rational number with two infinite representations is elementary:
\[
\sum_{n\in\mathbb N\setminus\{1\}}\frac n{2^n}
=
2-\frac12
=
\frac32,
\]
and likewise
\[
\sum_{n\in\mathbb N\setminus\{2\}}\frac n{2^n}
=
\frac32.
\]
These are distinct infinite subsets because \(w(1)=w(2)=1/2\).

Thus the two-representation weakening mentioned in the commentary is settled under the standard reading. The continuum-cardinality demand is the difficult part.

### 5.5 Closed fibers

The representation map \(\Phi\) above is continuous. Therefore rational fibers are compact closed subsets of Cantor space. Every such fiber is either countable or contains a perfect subset and hence has cardinality continuum. This reduces Q3 to the qualitative distinction “countable versus uncountable.”

No equivalence to a famous conjecture is currently apparent from the supplied context.

---

## 6. Traps and edge cases

1. **The Borwein–Loring parameter \(m=1\) does not satisfy \(t\ge2\).**  
   It gives a one-term identity. Use \(m\ge2\).

2. **The cases \(n=1\) and \(n=2\) have the same target.**  
   Since \(w(1)=w(2)=1/2\), arguments assuming strict monotonicity from \(n=1\) are invalid.

3. **A representation cannot use the target index itself.**  
   If \(a_i=n\), positivity of the other summands makes equality impossible.

4. **For \(n\ge3\), no smaller index can occur.**  
   Any term \(w(a)\) with \(a<n\) already exceeds \(w(n)\).

5. **Finite versus infinite representation is the central distinction.**  
   Compactness or interval-filling arguments usually give an infinite subset, not a finite one.

6. **A search cutoff is not a nonexistence proof.**  
   A valid representation could have an extremely large maximum exponent.

7. **The maximum selected exponent is necessarily even.**  
   Candidate-generation algorithms should enforce this. Conversely, evenness is only necessary, not sufficient.

8. **Binary-expansion intuition is dangerous.**  
   The “digit” at position \(n\) has value \(n/2^n\), not \(1/2^n\). Standard uniqueness or termination facts for dyadic expansions do not transfer directly.

9. **Greedy algorithms need not terminate.**  
   A greedy process may produce a valid infinite expansion of the dyadic rational \(n/2^n\) without yielding a finite representation.

10. **Do not count permutations in Q3.**  
    Doing so makes the problem trivial.

11. **Continuum many domain points do not force a continuum fiber.**  
    Both the domain of all subsets and the range interval have cardinality continuum; cardinal pigeonhole arguments give nothing.

12. **Independent switches must preserve one fixed rational total.**  
    It is not enough that each switch is an equal-sum identity if the sum over all gadgets is not proved rational.

13. **Finite representations form only a countable family.**  
    Hence any continuum fiber automatically contains continuum many genuinely infinite representations.

---

## 7. Verification hooks

### 7.1 Exact checker for a proposed finite representation

Input: \(n\) and a finite list \(A=\{a_1,\dots,a_t\}\).

Checks:

1. \(n\ge1\), \(t\ge2\);
2. all \(a_i\ge1\);
3. all \(a_i\) are distinct;
4. set \(M=\max(\{n\}\cup A)\) and verify the integer equality
   \[
   n\,2^{M-n}=\sum_{a\in A}a\,2^{M-a}.
   \]

This avoids all floating-point error.

### 7.2 Residual-state recurrence for Q2

For \(n\ge2\), only indices \(j>n\) need be considered. Let \(\varepsilon_j\in\{0,1\}\) indicate whether \(j\) is selected, and define
\[
r_j
=
2^j\left(
\frac n{2^n}
-
\sum_{n<k\le j}\varepsilon_k\frac k{2^k}
\right).
\]
Then
\[
r_n=n,
\qquad
r_j=2r_{j-1}-j\varepsilon_j.
\]

A finite representation exists exactly when some admissible path reaches
\[
r_M=0
\]
for some \(M\), after which all later \(\varepsilon_j\) are zero.

Any path that can be completed using indices \(>j\) must satisfy
\[
0\le r_j\le j+2,
\]
because the remaining tail, scaled by \(2^j\), has total \(j+2\).

This gives a narrow exact state graph with only \(O(j)\) potentially viable states at level \(j\).

For \(n=1\), use its equivalence with \(n=2\).

### 7.3 Finite-horizon capacity pruning

If the maximum allowed exponent is \(L\), then after level \(j<L\) the remaining scaled capacity is
\[
\sum_{k=j+1}^{L}\frac{k}{2^{k-j}}
=
j+2-\frac{L+2}{2^{L-j}}.
\]
A state exceeding this value cannot reach zero by level \(L\).

This gives an exact dynamic program for finding all representations with \(\max A\le L\).

### 7.4 Backward search

Starting from \(r_M=0\), reverse transitions satisfy
\[
r_{j-1}=\frac{r_j+j\varepsilon_j}{2},
\qquad \varepsilon_j\in\{0,1\},
\]
subject to integrality and
\[
0\le r_{j-1}\le j+1.
\]

Backward reachability is useful for discovering congruence invariants and for cataloguing all starting states that terminate by a given exponent.

### 7.5 Rational-fiber recurrence for Q3

Let \(x=p/q\) in lowest terms and let \(\varepsilon_j\in\{0,1\}\). Define
\[
R_j
=
q\,2^j\left(
x-\sum_{k=1}^{j}\varepsilon_k\frac k{2^k}
\right).
\]
Then
\[
R_0=p,\qquad
R_j=2R_{j-1}-qj\varepsilon_j.
\]

A full infinite path represents \(x\) if it satisfies
\[
0\le R_j\le q(j+2)
\]
for all \(j\). Indeed,
\[
x-\sum_{k=1}^{j}\varepsilon_k\frac k{2^k}
=
\frac{R_j}{q2^j}\longrightarrow0.
\]

For the especially natural candidate \(x=1\),
\[
R_0=1,\qquad
R_j=2R_{j-1}-j\varepsilon_j,\qquad
0\le R_j\le j+2.
\]

A program can enumerate viable prefixes, count branching prefixes, search for recurrent state corridors, and attempt to certify a perfect binary subtree.

### 7.6 Equal-sum gadget search

For disjoint finite sets \(P,Q\subseteq\{1,\dots,M\}\), check
\[
\sum_{p\in P}\frac p{2^p}
=
\sum_{q\in Q}\frac q{2^q}
\]
by testing
\[
\sum_{p\in P}p\,2^{M-p}
=
\sum_{q\in Q}q\,2^{M-q}.
\]

Cataloguing small gadgets may reveal rewrite rules or independent branching structures.

---

## 8. Attack routes

### Route 1: Residual-state dynamics and a universal termination theorem

**Core mechanism.**  
Use
\[
r_j=2r_{j-1}-j\varepsilon_j,\qquad 0\le r_j\le j+2,
\]
starting from \(r_n=n\). Q2 becomes a controlled reachability problem: can one choose \(\varepsilon_j\in\{0,1\}\) so that the path reaches zero?

**Key lemma needed.**  
A theorem of the form:

> For every \(n\ge2\), the state \((n,n)\) has a finite path to \(0\) within the admissible strip \(0\le r_j\le j+2\).

A stronger and more useful version would give a bounded-time descent or a finite collection of “funnels” leading to zero.

**Why it might work.**  
The admissible state space is only linear in \(j\), and the two transitions are very rigid. The verification through \(10000\) suggests that there may be a simple global control rule hidden in this dynamics.

**Likely failure point.**  
The system is nonautonomous: the subtraction term is \(j\), so no fixed finite-state quotient obviously captures all behavior. Locally sensible choices may trap the residual in an infinite nonterminating corridor.

**Quick blockage test.**  
For large ranges of \(n\), compute shortest terminating paths, maximum residuals, and normalized profiles \(r_j/j\). Check whether all successful paths pass through a small family of states such as \(r_j\in\{0,1,2,j/2,\dots\}\). If no reusable funnels emerge and minimal termination times grow irregularly, a simple control theorem is unlikely.

---

### Route 2: Finite rewrite identities and inductive covering

**Core mechanism.**  
Interpret an identity
\[
\sum_{p\in P}w(p)=\sum_{q\in Q}w(q)
\]
as a legal replacement rule. The Borwein–Loring identity replaces a singleton \(w(n_m)\) by a consecutive later block.

Seek a finite or parametrized family of replacement templates that covers every \(n\), possibly after a bounded number of transformations.

**Key lemma needed.**  
A covering theorem such as:

> Every sufficiently large \(n\) belongs to the domain of one of finitely many parametrized identities, and every exceptional output can be reduced to a smaller already solved case.

Alternatively, prove that a semigroup of rewrite templates acts transitively enough on all large indices.

**Why it might work.**  
The successful known family is exact and highly structured. Other finite intervals or sparse blocks may yield identities covering complementary residue classes.

**Likely failure point.**  
The weights are not translation invariant:
\[
w(k+s)=2^{-s}\frac{k+s}{2^k},
\]
so shifting an identity introduces an extra \(s/2^k\) contribution. Identities that look pattern-based at small scales may not extend uniformly.

**Quick blockage test.**  
Enumerate all small equal-sum identities, normalize them by largest exponent, and test whether their leading indices cover stable congruence classes or affine families. If the catalog has no repeatable templates beyond isolated coincidences and the known consecutive-block family, this route is probably blocked.

---

### Route 3: Strengthen the tail interval theorem to finite termination at dyadic targets

**Core mechanism.**  
The tail achievement set is an interval, so \(w(n)\) always has a later-index representation. Try to exploit the special dyadic rational target \(n/2^n\) to force one such expansion to terminate.

**Key lemma needed.**  
A finite-termination theorem tailored to this sequence, for example:

> Every dyadic rational in a specified subinterval of a tail achievement set has a finite subsum representation.

A weaker lemma only for the special targets \(n/2^n\) would suffice.

**Why it might work.**  
All residuals in the recurrence are integers after suitable scaling. Unlike a general real target, a dyadic target may be forced into a zero state by congruence control.

**Likely failure point.**  
For many redundant numeral systems, rational numbers can have only nonterminating expansions under particular digit constraints. Interval coverage by itself supplies no termination mechanism.

**Quick blockage test.**  
Implement several natural greedy and balanced-residual policies. Record whether they terminate for \(n\le10000\), and whether failures are eventually periodic or approach stable normalized residuals. Stable nonterminating behavior would show that a naive greedy strengthening is false, even if some other path terminates.

---

### Route 4: \(2\)-adic congruence descent aimed at a counterexample to Q2

**Core mechanism.**  
Assume a finite representation with largest exponent \(M\):
\[
n\,2^{M-n}=\sum_{a\in A}a\,2^{M-a}.
\]
Read this identity modulo \(2,4,8,\dots\), beginning at the largest selected exponents. This yields a forced backward parity process closely related to the reverse residual recurrence.

**Key lemma needed for disproof.**  
Find an \(n_0\) and an invariant showing that every admissible backward path from a terminal zero state avoids the starting state \(r_{n_0}=n_0\). Equivalently, derive incompatible congruence requirements for every possible even maximum \(M\).

**Why it might work.**  
The final exponent is already forced to be even, and each additional binary digit constrains whether \(M-1,M-2,\dots\) can be present. The coefficient \(a\) carries nontrivial \(2\)-adic information.

**Likely failure point.**  
The maximum \(M\) is unrestricted. Congruence obstructions valid for a fixed modulus may be evaded by taking \(M\) much larger or by changing the sparse pattern of selected exponents.

**Quick blockage test.**  
Search beyond \(10000\) using backward reachability and classify reachable starts modulo \(2^k\) for increasing \(k\). If every residue class repeatedly becomes reachable as the horizon grows, a finite congruence obstruction is unlikely. Any candidate counterexample must also survive searches with very large maximum exponent.

---

### Route 5: Perfect branching in a rational residual automaton

**Core mechanism.**  
Attack Q3 directly using the recurrence
\[
R_j=2R_{j-1}-qj\varepsilon_j.
\]
For a candidate such as \(x=1\), search for a recurrent admissible corridor in which every viable prefix eventually has two incompatible viable extensions.

**Key lemma needed.**  
Construct a perfect binary subtree \(T\subseteq\{0,1\}^{<\mathbb N}\) such that every branch satisfies
\[
0\le R_j\le q(j+2)
\]
for all \(j\). It is enough that every node of \(T\) has two later descendants that return to a common controlled region.

**Why it might work.**  
The two one-step options overlap when the state lies near half the current index. For \(x=1\), both choices are locally admissible near
\[
R_{j-1}\approx \frac j2.
\]
Repeated returns to this branching zone could create a Cantor set of representations.

**Likely failure point.**  
Large finite branching does not imply uncountably many infinite branches. Branches may merge, terminate, or eventually become forced, leaving only countably many full paths.

**Quick blockage test.**  
Compute finite-horizon viable trees with backward pruning, not merely forward reachability. Measure the number of prefixes having two extendible descendants at increasing separated levels. Search for explicit block return maps
\[
(j,R)\longmapsto(j+\ell,R')
\]
that offer two different digit blocks but land in the same or comparable corridor.

---

### Route 6: Infinitely many disjoint equal-sum gadgets plus rational completion

**Core mechanism.**  
Use disjoint pairs of finite sets \(P_i,Q_i\) satisfying
\[
\sum_{p\in P_i}w(p)=\sum_{q\in Q_i}w(q).
\]
Choosing \(P_i\) or \(Q_i\) independently gives continuum many subsets with the same total, provided all gadgets are disjoint and the overall common sum is rational after adding a fixed completion set.

The Borwein–Loring identities already give infinitely many candidate gadgets:
\[
P_m=\{n_m\},\qquad
Q_m=\{n_m+1,\dots,n_m+m\}.
\]

**Key lemma needed.**  
Choose disjoint gadgets and a fixed set \(C\), disjoint from all gadget coordinates, such that
\[
x=
\sum_{c\in C}w(c)
+
\sum_{i=1}^{\infty}\sum_{p\in P_i}w(p)
\]
is rational. Then every binary choice \(P_i\) versus \(Q_i\) gives the same rational \(x\).

A useful sufficient result would be an interval theorem for the achievement set remaining after deleting the gadget coordinates, allowing exact completion to a prescribed rational.

**Why it might work.**  
This route builds continuum cardinality explicitly and avoids delicate counting of automaton paths. The known identities already provide infinitely many independent local switches.

**Likely failure point.**  
The common gadget total
\[
\sum_i\sum_{p\in P_i}w(p)
\]
need not be rational. Also, deleting all gadget coordinates may destroy the interval property needed to construct a rational completion.

**Quick blockage test.**  
Choose increasingly sparse \(m_i\), compute rigorous upper and lower bounds for the deleted tail mass, and verify whether the undeleted sequence still satisfies a tail-dominance condition. Search for a rational \(x\) lying in the resulting completion interval. Failure of tail dominance for every natural gadget selection would seriously obstruct this route.

---

## 9. Verdict on difficulty

- **Q1 is completely settled.** The Borwein–Loring family gives infinitely many examples.
- **Q2 is genuinely open but computationally well supported.** Verification through \(10000\) is strong evidence, yet the unrestricted largest exponent makes both proof and disproof difficult. The most promising formulation is the narrow residual-state reachability problem.
- **Q3 is a distinct cardinality problem.** The key requirement is not merely multiple representations but an uncountable closed rational fiber. Perfect branching in the residual automaton or infinitely many independent equal-sum gadgets are the most concrete mechanisms.
- The statement that every \(n\) has some possibly infinite tail representation is elementary and does not solve Q2.
- No equivalence to a famous conjecture is known from the supplied context, and none should be asserted. The main difficulty appears to be a specialized interaction of dyadic arithmetic, constrained subset sums, and nonautonomous carry dynamics rather than an already recognized major conjecture.
- The database’s `OPEN` status should be understood as referring to Q2 and Q3, not to the already-settled infinitude question.