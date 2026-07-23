# Problem brief: Erdős Problem #1110

## 1. Precise statement

Let \(p>q\ge 2\) be integers satisfying \(\gcd(p,q)=1\). Exponents are understood to be nonnegative integers:
\[
\mathbb N_0=\{0,1,2,\dots\}.
\]

Define the multiplicative grid
\[
S_{p,q}:=\{p^kq^\ell:(k,\ell)\in\mathbb N_0^2\}.
\]

A positive integer \(n\) is **\((p,q)\)-representable** if there is a finite nonempty set
\[
A=\{(k_1,\ell_1),\dots,(k_r,\ell_r)\}\subseteq \mathbb N_0^2
\]
such that

1. 
   \[
   n=\sum_{i=1}^r p^{k_i}q^{\ell_i},
   \]
2. the corresponding summands are pairwise incomparable under divisibility: for all \(i\ne j\),
   \[
   p^{k_i}q^{\ell_i}\nmid p^{k_j}q^{\ell_j}.
   \]

Because \(\gcd(p,q)=1\),
\[
p^kq^\ell\mid p^{k'}q^{\ell'}
\quad\Longleftrightarrow\quad
k\le k'\ \text{and}\ \ell\le \ell'.
\]
Thus \(A\) must be an antichain in the product poset
\[
(\mathbb N_0^2,\le_{\mathrm{prod}}),
\qquad
(k,\ell)\le_{\mathrm{prod}}(k',\ell')
\iff k\le k'\text{ and }\ell\le\ell'.
\]

Equivalently, after ordering the exponent pairs by increasing first coordinate,
\[
k_1<k_2<\cdots<k_r,
\]
the second coordinates must satisfy
\[
\ell_1>\ell_2>\cdots>\ell_r.
\]
In particular, no two summands can have the same \(p\)-exponent or the same \(q\)-exponent.

Write
\[
\mathcal R_{p,q}
 :=
 \left\{
 \sum_{(k,\ell)\in A}p^kq^\ell:
 A\subseteq\mathbb N_0^2
 \text{ is a finite nonempty antichain}
 \right\}
\]
and
\[
\mathcal N_{p,q}:=\mathbb N\setminus\mathcal R_{p,q}.
\]

The counting functions are
\[
R_{p,q}(X):=\#\bigl(\mathcal R_{p,q}\cap[1,X]\bigr),
\qquad
N_{p,q}(X):=\#\bigl(\mathcal N_{p,q}\cap[1,X]\bigr).
\]

The natural density of the non-representable integers, if it exists, is
\[
d(\mathcal N_{p,q})
 :=
 \lim_{X\to\infty}\frac{N_{p,q}(X)}{\lfloor X\rfloor}.
\]
Since \(R_{p,q}(X)+N_{p,q}(X)=\lfloor X\rfloor\), the assertion
\[
d(\mathcal N_{p,q})=1
\]
is equivalent to
\[
R_{p,q}(X)=o(X).
\]

The standard reading of “coprime non-representable numbers” is
\[
\mathcal N_{p,q}^{*}
 :=
 \{n\in\mathcal N_{p,q}:\gcd(n,pq)=1\}.
\]
The second question is whether
\[
\#\mathcal N_{p,q}^{*}=\infty
\]
for every admissible pair other than \(\{p,q\}=\{2,3\}\).

### Formal version of the database problem

For every pair of coprime integers \(p>q\ge2\) with \((p,q)\ne(3,2)\):

1. determine the density, or at least the correct density behavior, of \(\mathcal N_{p,q}\);
2. determine whether \(\mathcal N_{p,q}^{*}\) is infinite.

The density question is phrased exploratorily rather than as a single yes/no conjecture. The strongest natural conjectural answer suggested by the known results is
\[
R_{p,q}(X)=o(X)
\quad\text{for every }(p,q)\ne(3,2),
\]
hence \(d(\mathcal N_{p,q})=1\), but the database statement itself does not explicitly assert this conjecture.

### Interpretive conventions and alternatives

- Exponents must be allowed to be zero. This is the standard reading and is required by the quoted \((2,3)\) induction. If \(k,\ell\ge1\) were required instead, this would be a materially different problem.
- The sum is finite. Repetition is automatically forbidden, because two equal summands divide one another.
- The integer \(1=p^0q^0\) is an allowed summand. Since \(1\) divides every other positive integer, it can occur only in the singleton representation \(1=1\).
- “Coprime non-representable” is taken to mean coprime to \(pq\), not that different non-representable integers are pairwise coprime.
- Density means ordinary natural density among all positive integers, not relative density inside the reduced residue classes modulo \(pq\). If natural density fails to exist, upper and lower densities should be distinguished.

---

## 2. What counts as a solution

Because the original entry contains an open-ended density question and a yes/no infinitude question, a full resolution should address both.

### 2.1 Complete positive resolution of the density-one conjecture

A proof of the strongest expected density statement must show that for every coprime pair \(p>q\ge2\), \((p,q)\ne(3,2)\),
\[
R_{p,q}(X)=o(X).
\]
Equivalently, for every \(\varepsilon>0\), there is \(X_0=X_0(p,q,\varepsilon)\) such that
\[
R_{p,q}(X)\le \varepsilon X
\qquad(X\ge X_0).
\]

It is not enough merely to count antichains in a fixed exponent box unless the resulting estimate rigorously implies this \(o(X)\) bound.

If the actual density is not always \(1\), a complete answer must instead classify every pair and prove, for each pair, either:

- existence and value of
  \[
  \lim_{X\to\infty}N_{p,q}(X)/X,
  \]
  or
- nonexistence of the limit, with rigorous information on the distinct liminf and limsup.

Given the known results, the unresolved density work is concentrated in five pairs:
\[
(p,q)\in\{(5,2),(7,2),(9,2),(4,3),(5,3)\}.
\]
Settling all five would complete the currently missing density classification.

### 2.2 Complete positive resolution of the coprime infinitude question

A proof must establish, for every admissible nonexceptional pair,
\[
\forall B\ge1\ \exists n>B:
\quad
\gcd(n,pq)=1
\quad\text{and}\quad
n\notin\mathcal R_{p,q}.
\]

The known results reduce this question to the three pairs
\[
(p,q)\in\{(5,2),(9,2),(5,3)\}.
\]

A proof of density one for any of these pairs would automatically settle its coprime infinitude question. Indeed, the integers coprime to \(pq\) have positive density, while \(R_{p,q}(X)=o(X)\); therefore almost all integers coprime to \(pq\) would be non-representable.

### 2.3 What a disproof must establish

There is no single formal density conjecture in the wording, but a disproof of the natural universal density-one assertion requires an admissible pair \((p,q)\ne(3,2)\) and a rigorous demonstration that
\[
R_{p,q}(X)\ne o(X).
\]
For example, it would suffice to prove
\[
R_{p,q}(X)\ge cX
\]
for some \(c>0\) and infinitely many \(X\). A stronger disproof would prove positive lower density of representable numbers.

A disproof of universal coprime infinitude requires an admissible pair \((p,q)\ne(3,2)\) for which
\[
\mathcal N_{p,q}^{*}
\]
is finite. Concretely, one could provide:

1. a threshold \(N_0\);
2. a constructive proof that every \(n>N_0\) with \(\gcd(n,pq)=1\) has an antichain representation;
3. an exhaustive finite computation below \(N_0\).

A single representable integer, or even a very long interval of representable coprime integers, does not disprove infinitude.

### 2.4 Verification of an explicit individual claim

For a fixed \(n\), a claimed representation is verified by checking:

- every exponent is in \(\mathbb N_0\);
- the summands total \(n\);
- after sorting by increasing \(k\), the \(\ell\)'s strictly decrease.

A claimed individual non-representable integer can be verified by finite exhaustive search, because every summand is positive and at most \(n\), so only exponent pairs satisfying
\[
p^kq^\ell\le n
\]
need be considered. Such a computation proves only that particular \(n\) is non-representable.

---

## 3. What does not count

The following do not resolve the full problem.

1. **Only unrestricted infinitude.** Erdős–Lewin already proved that there are infinitely many non-representable integers for every nonexceptional pair. This does not imply infinitely many are coprime to \(pq\).

2. **Only the already settled parameter ranges.** Reproving density one for \(q>3\), \(q=3,p>6\), or \(q=2,p>10\) does not settle the five remaining density pairs.

3. **A power saving weaker than needed in the wrong direction.** A bound such as
   \[
   R_{p,q}(X)\ll X^{1+\varepsilon}
   \quad\text{or}\quad
   R_{p,q}(X)\le C X
   \]
   says nothing about density zero. One needs \(o(X)\), or a quantitatively stronger estimate such as \(O(X^{1-\delta})\).

4. **Counting representations rather than represented integers without a usable bound.** If \(r_{p,q}(n)\) counts representations, then
   \[
   R_{p,q}(X)\le\sum_{n\le X}r_{p,q}(n),
   \]
   but a representation count larger than \(X\) gives no density conclusion because many antichains may have the same sum.

5. **Arbitrarily large non-representable integers without coprimality.** These are already known to exist.

6. **A finite list of coprime non-representable integers.** No finite computation proves infinitude.

7. **A fixed-modulus heuristic.** Observing missing residues for truncated exponent ranges is not enough. The obstruction must hold for antichains with arbitrarily large exponents.

8. **Conditional results.** A theorem conditional on an unproved conjecture does not solve the database problem unless that conjecture is also proved.

9. **Numerical density trends.** Computations suggesting \(R_{p,q}(X)/X\to0\) do not establish a density.

10. **Removing the antichain condition.** Results on sums of arbitrary distinct \(p^kq^\ell\), or arbitrary sums with repetition, concern a different problem.

11. **Changing the exponent convention.** Results with \(k,\ell\ge1\) do not apply to the standard problem.

---

## 4. Known results and context

### 4.1 The exceptional pair \((p,q)=(3,2)\)

For \(\{p,q\}=\{2,3\}\), every positive integer is representable. The standard induction proves the stronger statement that every even \(n\) has a representation all of whose summands are even.

- If \(n=2m\), represent \(m\) inductively and multiply every summand by \(2\).
- If \(n\) is odd, choose \(3^j\le n<3^{j+1}\) maximal. Then \(n-3^j\) is even. Represent \(n-3^j\) with even summands and add \(3^j\).

The compatibility of the new summand is important. Every old term has a factor \(2\), so it cannot divide \(3^j\). Also every old term is less than
\[
n-3^j<2\cdot3^j;
\]
hence no old term can be divisible by \(3^j\), since an even multiple of \(3^j\) is at least \(2\cdot3^j\).

Thus
\[
\mathcal N_{3,2}=\varnothing.
\]

### 4.2 Erdős–Lewin

Erdős and Lewin [ErLe96] proved:
\[
\mathcal N_{p,q}\text{ is finite}
\quad\Longleftrightarrow\quad
\{p,q\}=\{2,3\}.
\]
Since the exceptional pair actually represents every positive integer, it follows that for every other coprime pair \(p>q\ge2\),
\[
\#\mathcal N_{p,q}=\infty.
\]

This settles unrestricted infinitude, but neither density nor coprime infinitude.

### 4.3 Yu–Chen density theorem

Yu and Chen [YuCh22] proved
\[
R_{p,q}(X)=o(X),
\]
and hence
\[
d(\mathcal N_{p,q})=1,
\]
in each of the following ranges:

- \(q>3\);
- \(q=3\) and \(p>6\);
- \(q=2\) and \(p>10\).

Consequently, the only unresolved density pairs are
\[
(5,2),\ (7,2),\ (9,2),\ (4,3),\ (5,3).
\]

### 4.4 Yu–Chen coprime infinitude theorem

Yu and Chen also proved that \(\mathcal N_{p,q}^{*}\) is infinite when:

- \(q>3\);
- \(q=3\) and \(p\ne5\);
- \(q=2\) and \(p\notin\{3,5,9\}\).

After excluding the exceptional pair \((3,2)\), the unresolved coprime cases are exactly
\[
(5,2),\quad(9,2),\quad(5,3).
\]

The present status can therefore be summarized as follows.

| Pair or range | Density of non-representables | Infinitely many coprime non-representables |
|---|---:|---:|
| \((3,2)\) | \(0\); in fact none | No |
| \(q>3\) | \(1\) | Yes |
| \(q=3,\ p>6\) | \(1\) | Yes |
| \((4,3)\) | Open | Yes |
| \((5,3)\) | Open | Open |
| \(q=2,\ p>10\) | \(1\) | Yes |
| \((7,2)\) | Open | Yes |
| \((5,2),(9,2)\) | Open | Open |

### 4.5 A useful elementary boundary congruence

Suppose \(n\in\mathcal R_{p,q}\) and \(\gcd(n,p)=1\). In any antichain there is at most one point with \(k=0\), because two such points would be comparable. All summands with \(k\ge1\) are divisible by \(p\). Since \(n\not\equiv0\pmod p\), there must be exactly one \(k=0\) summand. Therefore
\[
n\equiv q^\ell\pmod p
\]
for some \(\ell\ge0\).

Similarly, if \(\gcd(n,q)=1\), then
\[
n\equiv p^k\pmod q
\]
for some \(k\ge0\).

Hence every representable \(n\) coprime to \(pq\) satisfies
\[
n\bmod p\in\langle q\bmod p\rangle\subseteq (\mathbb Z/p\mathbb Z)^\times
\]
and
\[
n\bmod q\in\langle p\bmod q\rangle\subseteq (\mathbb Z/q\mathbb Z)^\times.
\]

If either cyclic subgroup is proper, a missing reduced residue class, combined with the Chinese remainder theorem, gives an infinite arithmetic progression of coprime non-representable integers.

This elementary obstruction explains, for example:

- \((7,2)\): powers of \(2\) modulo \(7\) are only \(1,2,4\);
- \((4,3)\): powers of \(4\) modulo \(3\) are only \(1\).

It fails at the first level for the three unresolved coprime pairs:

- \(\langle2\rangle=(\mathbb Z/5\mathbb Z)^\times\);
- \(\langle2\rangle=(\mathbb Z/9\mathbb Z)^\times\);
- \(\langle3\rangle=(\mathbb Z/5\mathbb Z)^\times\) and \(\langle5\rangle=(\mathbb Z/3\mathbb Z)^\times\).

Thus any congruence proof for these pairs must use higher-power moduli, several boundary layers, or a more global compatibility condition.

### 4.6 Elementary antichain counting baseline

If \(n\le X\), every summand satisfies
\[
k\le K:=\lfloor\log_pX\rfloor,
\qquad
\ell\le L:=\lfloor\log_qX\rfloor.
\]
The number of antichains in the full rectangle
\[
\{0,\dots,K\}\times\{0,\dots,L\}
\]
is
\[
\sum_{r=0}^{\min(K+1,L+1)}
 \binom{K+1}{r}\binom{L+1}{r}
 =
 \binom{K+L+2}{K+1}.
\]
This gives a simple upper bound for the number of representations, but it is generally too crude for the remaining small-base pairs. It ignores the much stronger constraint
\[
\sum_{(k,\ell)\in A}p^kq^\ell\le X.
\]

### 4.7 The auxiliary large-summand problem

Erdős and Lewin also asked, for the exceptional pair \(\{2,3\}\), how large one can force every summand in a representation of \(n\) to be. Under the standard extremal interpretation of the function \(f(n)\), Yu–Chen proved
\[
\frac{n}{(\log n)^{\log_2 3}}\ll f(n)\ll \frac n{\log n},
\]
and Yang–Zhao [YaZh25] improved the lower bound to
\[
f(n)\gg \frac n{\log n}.
\]
As noted by van Doorn, a result of Blecksmith, McCallum, and Selfridge [BMS98] already implies the asymptotic
\[
f(n)\sim \frac{\log2\,\log3}{2}\frac n{\log n}.
\]

This auxiliary question is therefore essentially settled and should not be confused with the unresolved density and coprime questions.

The database also points to Problem [123] for three bases, [845] for further questions concerning \(\{2,3\}\), and [246] for the analogous topic without the antichain condition.

---

## 5. Traps and edge cases

1. **The bases need not be prime.** In particular, \(p=4\) and \(p=9\) occur among the critical cases. Arguments using prime valuations, primitive roots, or fields must be adapted to composite moduli.

2. **Exponent zero matters.** The boundary terms \(q^\ell\) with \(k=0\) and \(p^k\) with \(\ell=0\) are central to both induction and congruence arguments.

3. **The summand \(1\).** It is legal, but it cannot coexist with any other summand.

4. **Pairwise distinct is weaker than antichain.** Distinct terms such as \(1\) and \(p\), or \(q\) and \(pq\), are not allowed together.

5. **After sorting by \(k\), the \(\ell\)'s must decrease strictly.** Weak decrease is insufficient: equal \(\ell\)'s also give divisibility.

6. **Scaling is safe; adjoining a term is not automatically safe.** Multiplying every term by \(p\) or \(q\) preserves incomparability. Adding a pure power requires checking both divisibility directions against every existing term.

7. **Every term is at most \(n\).** This makes individual non-representability decidable by finite search. It does not make infinitude or density a finite problem.

8. **Unrestricted infinitude does not imply coprime infinitude.** It is logically possible that all but finitely many non-representables are divisible by \(p\) or \(q\).

9. **Density one would imply coprime infinitude.** Thus if density one is proved in one of the three fully unresolved pairs, its coprime question is automatically solved.

10. **A modular obstruction must cover all exponents.** Searching powers only up to a cutoff is not valid unless periodicity or nilpotence modulo the chosen modulus is incorporated rigorously.

11. **Modulo \(p\) and modulo \(q\), only the boundary layer survives; modulo \(p^a\) several layers survive.** For composite bases this means powers of the integer \(p\), not ordinary \(p\)-adic valuation levels associated with a prime.

12. **Representation multiplicity can be large.** A large number of admissible antichains does not imply a large set of represented integers, and a large represented set cannot be inferred without controlling collisions.

13. **Positive upper density is not positive lower density.** To disprove density one, a positive limsup for representables suffices; to prove a positive natural density, substantially more is required.

14. **The order \(p>q\) is only a normalization.** The mathematical property is symmetric in the two bases after swapping coordinates, but parameter tables must respect the database convention.

---

## 6. Verification hooks

### 6.1 Exact enumeration up to \(X\)

For fixed \(p,q,X\), form all exponent pairs satisfying
\[
p^kq^\ell\le X.
\]
Enumerate antichains by scanning \(k\) in increasing order and maintaining an upper bound on the next \(\ell\).

A recursive state can be
\[
(k,L_{\max},s),
\]
where:

- all future chosen exponents must have first coordinate at least \(k\);
- a chosen \(\ell\) must satisfy \(\ell<L_{\max}\);
- \(s\) is the current sum.

At row \(k\), either skip the row or choose one \(\ell<L_{\max}\) with
\[
s+p^kq^\ell\le X,
\]
then recurse with \(L_{\max}=\ell\).

Mark every positive sum reached. This exactly computes \(\mathcal R_{p,q}\cap[1,X]\).

The critical pairs to test are
\[
(5,2),(7,2),(9,2),(4,3),(5,3).
\]

Record:

- \(R_{p,q}(X)\);
- \(R_{p,q}(X)/X\);
- the number of non-representables;
- the number with \(\gcd(n,pq)=1\);
- maximal gaps and residue-class distributions;
- representation multiplicities.

### 6.2 Exact transfer recurrence

Let \(F_{k,L}(z)\) be the generating polynomial for antichains using rows \(k,k+1,\dots\), with all selected second coordinates \(<L\), truncated at degree \(X\). Then
\[
F_{k,L}(z)
=
F_{k+1,L}(z)
+
\sum_{\substack{0\le\ell<L\\p^kq^\ell\le X}}
z^{p^kq^\ell}F_{k+1,\ell}(z),
\]
again truncating degrees above \(X\).

- Coefficients count representations.
- Boolean coefficients compute the represented set.
- Integer coefficients allow computation of the collision energy
  \[
  \sum_{n\le X}r_{p,q}(n)^2.
  \]

### 6.3 Boundary congruence checks

Compute the finite cyclic sets
\[
H_p=\{q^\ell\bmod p:\ell\ge0\},
\qquad
H_q=\{p^k\bmod q:k\ge0\}.
\]
If either omits a unit residue, use CRT to produce an explicit infinite arithmetic progression of coprime non-representables.

For the unresolved coprime cases, verify that the first-level test indeed has no missing units before attempting higher moduli.

### 6.4 Higher-layer modular automata

For a modulus such as \(p^aq^b\), enumerate the possible contributions of the low-\(k\) and low-\(\ell\) boundary layers. Large \(k\) or \(\ell\) contributions eventually vanish in the corresponding prime-power component, while exponents in coprime components become periodic.

Any claimed forbidden residue must be accompanied by a proof that the automaton has stabilized and accounts for arbitrary exponent sizes and arbitrary antichain lengths.

### 6.5 Induction-certificate search

For a possible eventual-representability theorem, search for finitely many states encoding:

- \(n\) modulo a chosen modulus;
- a scaling operation by \(p\) or \(q\);
- the largest or smallest allowed exponent in the existing representation;
- which pure boundary term may be adjoined safely.

A successful computer search should output a finite transition table whose correctness can then be verified symbolically. Merely checking all \(n\le X\) is not an induction proof.

### 6.6 Regression checks

Any implementation should verify:

- every \(n\) up to the test bound is represented for \((3,2)\);
- representations containing \(1\) are singleton;
- sorting every output by increasing \(k\) yields strictly decreasing \(\ell\);
- the modular boundary condition holds for every enumerated representable \(n\) coprime to \(pq\);
- independent DFS and generating-polynomial implementations agree for small \(X\).

---

## 7. Attack routes

### Route 1: Weighted antichain entropy

**Core mechanism.** Count admissible antichains satisfying the actual weight constraint
\[
\sum_{(k,\ell)\in A}p^kq^\ell\le X,
\]
rather than merely placing \(A\) in a logarithmic rectangle.

**Key lemma needed.** For each unresolved density pair,
\[
\#\left\{A:
A\text{ a finite antichain},\
\sum_{(k,\ell)\in A}p^kq^\ell\le X
\right\}
=o(X).
\]

This immediately implies \(R_{p,q}(X)=o(X)\).

**Why it might work.** The full-rectangle antichain count grossly overcounts paths containing several very expensive northeast points. A variational or entropy calculation incorporating exponential weights may lower the growth exponent below \(1\), especially because the five unresolved cases lie near the threshold of crude counting methods.

**Most likely failure.** For small bases, the number of valid antichains may genuinely grow faster than \(X\), even though their distinct sums remain sparse. Then representation counting alone cannot prove density zero.

**Quick test.** Use exact dynamic programming to count admissible antichains, not just distinct sums, for geometrically increasing \(X\). Estimate
\[
\alpha(X)=\frac{\log A_{p,q}(X)}{\log X}.
\]
If \(\alpha(X)\) appears bounded below by \(1\), the direct first-moment route is probably blocked.

---

### Route 2: Canonicalization and carry compression

**Core mechanism.** Exploit arithmetic identities among the weights to map every antichain sum to a canonical digit profile with far fewer possibilities than there are antichains.

**Key lemma needed.** Construct a canonical encoding \(C(A)\) such that:

1. \(\sum_{A}p^kq^\ell\) is determined by \(C(A)\);
2. the number of possible codes for sums at most \(X\) is \(o(X)\).

One possible framework is a normalization of mixed \(p\)- and \(q\)-adic carries combined with the monotone boundary path of the antichain.

**Why it might work.** Small bases create many exact or near-exact carry relations. These may cause the huge collision multiplicities that defeat raw antichain counting. A canonical normal form could count distinct sums directly.

**Most likely failure.** Carrying can destroy the antichain structure, and different carry orders may not lead to a unique normal form. The set of canonical digit profiles may still have linear complexity.

**Quick test.** Enumerate all representations for moderate \(X\), compare the antichain count with the number of distinct sums, and measure collision multiplicities. If
\[
\frac{\#\{\text{antichains of weight}\le X\}}{R_{p,q}(X)}
\]
grows rapidly for the unresolved pairs, a compression argument is promising. If collisions remain modest, it is not.

---

### Route 3: Higher congruence and boundary-layer descent

**Core mechanism.** Extend the elementary conditions modulo \(p\) and \(q\) to moduli \(p^a\), \(q^b\), or mixed moduli.

For instance, modulo \(p^a\), only rows
\[
k=0,1,\dots,a-1
\]
can contribute nontrivially in the base-\(p\) sense. Since each row contains at most one selected point and the selected \(\ell\)'s decrease, the possible residues have strong ordering constraints.

**Key lemma needed.** For one of the unresolved coprime pairs, find a modulus \(M\) and a reduced residue \(r\bmod M\) such that no antichain sum is congruent to \(r\pmod M\).

Then every integer in that residue class is non-representable, yielding infinitely many coprime examples and in fact positive lower density of non-representables.

A weaker alternative is an infinite descent showing that any representation of numbers in a prescribed sequence of unit residue classes would force impossible exponent inequalities.

**Why it might work.** The first boundary layer is completely understood. Higher layers remain sparse and ordered, even when powers of one base generate all units modulo the other base.

**Most likely failure.** For \((5,2),(9,2),(5,3)\), higher layers may fill every residue modulo every fixed modulus. A fixed congruence obstruction need not exist even if infinitely many non-representables exist.

**Quick test.** Build exact residue automata modulo
\[
p^a,\quad q^b,\quad p^aq^b
\]
for small \(a,b\), with rigorous exponent periodicity. Search for stable missing reduced residues. If all units are filled quickly for increasing \(a,b\), fixed-modulus obstruction is likely blocked.

---

### Route 4: Recursive representability and finite-state induction — disproof route

**Core mechanism.** Generalize the \((2,3)\) induction. Divide by \(p\) or \(q\) when possible; otherwise subtract a carefully chosen pure power so that the remainder is divisible by one base and the new summand is incomparable with the scaled representation.

**Key lemma needed.** For one of
\[
(5,2),\ (9,2),\ (5,3),
\]
construct finitely many inductive representation classes such that every sufficiently large \(n\) coprime to \(pq\) belongs to one class and each class reduces to a smaller integer while preserving an exponent-bound invariant.

If successful, this could prove that only finitely many coprime non-representables exist, thereby disproving the universal coprime-infinitude conjecture.

A weaker coverage lemma proving that a positive proportion of integers are representable would already disprove universal density one.

**Why it might work.** Exactly in the unresolved coprime cases, the first-level unit power orbits are complete. This is the local condition needed to choose a boundary power matching the desired residue.

**Most likely failure.** Matching the residue is easy; guaranteeing incomparability is hard. The chosen pure power may divide or be divisible by a term in the recursively constructed representation. Erdős–Lewin’s unrestricted infinitude also rules out eventual representability of all integers.

**Quick test.** For large computational ranges, examine whether every sufficiently large reduced residue class appears represented and whether the largest coprime non-representable observed value stabilizes or continues to grow. Attempt automatic synthesis of induction states with explicit exponent ceilings.

---

### Route 5: Additive energy and collision control — density disproof route

**Core mechanism.** Let
\[
r_{p,q}(n)
\]
be the number of antichain representations of \(n\). Then
\[
\sum_{n\le X}r_{p,q}(n)
\]
counts admissible antichains of weight at most \(X\), while
\[
E(X):=\sum_{n\le X}r_{p,q}(n)^2
\]
counts pairs of antichains with equal sum. Cauchy–Schwarz gives
\[
R_{p,q}(X)
\ge
\frac{\left(\sum_{n\le X}r_{p,q}(n)\right)^2}{E(X)}.
\]

**Key lemma needed.** For one unresolved pair, prove an energy bound strong enough to imply
\[
R_{p,q}(X)\ge cX
\]
for infinitely many \(X\), or even for all large \(X\).

Equal-sum collisions lead to equations of the form
\[
\sum_i p^{k_i}q^{\ell_i}
=
\sum_j p^{a_j}q^{b_j},
\]
with both sides supported on antichains. Rigidity results for \(S\)-unit equations may help control nondegenerate solutions, although uniformity in the number of terms is a major issue.

**Why it might work.** In the unresolved small-base cases, the raw number of antichains may be sufficiently large to force substantial interval coverage if collisions are not too concentrated.

**Most likely failure.** There may be enormous structured collision families caused by carrying identities. Classical \(S\)-unit theorems usually control equations with a fixed number of terms, whereas antichain size grows with \(X\).

**Quick test.** Compute
\[
A(X)=\sum_{n\le X}r(n),\qquad
E(X)=\sum_{n\le X}r(n)^2,\qquad
A(X)^2/E(X),
\]
and compare the last quantity with the actual \(R(X)\). If the Cauchy–Schwarz lower bound is already of order \(X\), the energy route is credible. If it is tiny because of extreme multiplicities, it is blocked without a strong structural collision classification.

---

## 8. Verdict on difficulty

This is a genuine open problem, but the current results isolate it to a small set of low-base cases rather than an unrestricted two-parameter family.

The remaining tasks are:

- density for
  \[
  (5,2),(7,2),(9,2),(4,3),(5,3);
  \]
- coprime infinitude for
  \[
  (5,2),(9,2),(5,3).
  \]

The small bases are likely exceptional precisely because ordinary entropy estimates and first-level congruence obstructions are too weak there. The problem combines:

- weighted antichain enumeration in \(\mathbb N_0^2\);
- lacunary additive structure;
- mixed-base carrying;
- congruence restrictions from boundary layers;
- potentially difficult equal-sum equations among \(S\)-units.

No equivalence to a famous conjecture such as GRH, \(abc\), or the Subspace Theorem is currently indicated by the supplied context, and one should not claim such an equivalence without proof. Nevertheless, some possible approaches may require uniform \(S\)-unit or additive-energy estimates substantially beyond standard fixed-term results.

A global proof that all five remaining pairs satisfy
\[
R_{p,q}(X)=o(X)
\]
would be the cleanest resolution: it would settle the entire density question and automatically settle the three remaining coprime-infinitude cases. Conversely, the most plausible disproof avenue is a finite-state recursive construction showing eventual representability in the reduced residue classes for one of \((5,2),(9,2),(5,3)\), or an additive-energy argument proving positive density of representable integers for one of the five unresolved pairs.