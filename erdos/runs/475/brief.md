# Problem Brief: Erdős Problem #475 — Valid Orderings in \(\mathbb F_p\)

## 1. PRECISE STATEMENT

Let \(p\) be a prime and let
\[
\mathbb F_p=\mathbb Z/p\mathbb Z
\]
be the additive group of the field with \(p\) elements. Let
\[
A\subseteq \mathbb F_p\setminus\{0\},\qquad t:=|A|.
\]

The problem asks whether the following assertion holds:

> For every prime \(p\) and every subset \(A\subseteq\mathbb F_p\setminus\{0\}\), there exists a bijection
> \[
> a:\{1,\dots,t\}\to A,\qquad m\mapsto a_m,
> \]
> such that the partial sums
> \[
> S_m:=\sum_{k=1}^m a_k\in\mathbb F_p,\qquad 1\le m\le t,
> \]
> are pairwise distinct.

Formally, the required condition is
\[
\forall\,1\le i<j\le t,\qquad S_i\ne S_j.
\]
Equivalently,
\[
\forall\,1\le i<j\le t,\qquad
\sum_{k=i+1}^{j}a_k\ne 0.
\]
Thus every nonempty consecutive block that begins at position \(2\) or later must have nonzero sum.

Such a permutation \((a_1,\dots,a_t)\) is called a **valid ordering** or, in related literature, a **simple ordering**.

### The empty set

If \(A=\varnothing\), then \(t=0\), the unique empty ordering satisfies the condition vacuously. One may instead formulate the conjecture only for \(t\ge1\); this makes no substantive difference.

### Crucial interpretation: \(S_0\) is not included

The empty partial sum
\[
S_0:=0
\]
is **not** among the sums required to be distinct. In particular, one or more partial sums may equal \(0\), provided no two of \(S_1,\dots,S_t\) coincide.

This is forced by the commentary: when \(A=\mathbb F_p\setminus\{0\}\),
\[
\sum_{a\in A}a=0,
\]
so \(S_t=0=S_0\). Graham’s positive result for \(t=p-1\) would be impossible under an interpretation that included \(S_0\).

Accordingly, neither of the following stronger statements is intended:

1. \(S_0,S_1,\dots,S_t\) are all distinct;
2. every \(S_m\) is nonzero.

Both fail whenever \(\sum_{a\in A}a=0\).

### Boolean-lattice reformulation

For \(U\subseteq A\), define its color
\[
c(U):=\sum_{a\in U}a\in\mathbb F_p.
\]
An ordering \(a_1,\dots,a_t\) defines a maximal chain
\[
\varnothing=U_0\subset U_1\subset\cdots\subset U_t=A,
\qquad U_m=\{a_1,\dots,a_m\}.
\]
The ordering is valid exactly when
\[
c(U_1),c(U_2),\dots,c(U_t)
\]
are pairwise distinct. Thus the problem asks for a rainbow maximal chain in the Boolean lattice \(2^A\), where subsets are colored by their sum modulo \(p\), with the color of \(\varnothing\) exempted.

---

## 2. WHAT COUNTS AS A SOLUTION

### A complete proof

A complete affirmative solution must prove
\[
\forall p\text{ prime}\ \forall A\subseteq\mathbb F_p\setminus\{0\}\ 
\exists\text{ a valid ordering of }A.
\]

Given the current commentary, this can be accomplished in either of two ways:

1. **Uniform theoretical proof:** prove the assertion directly for all primes and all subset sizes; or
2. **Asymptotic theorem plus finite verification:**  
   - extract an explicit, effective threshold \(P_0\) such that existing results prove the assertion for every prime \(p\ge P_0\);
   - verify rigorously every prime \(p<P_0\) and every relevant \(A\subseteq\mathbb F_p^\times\).

For a computer-assisted finite verification to count as a rigorous proof, it must establish that:

- every relevant prime has been enumerated;
- every subset has been covered, possibly modulo a proved symmetry reduction;
- for every subset orbit, an ordering has been produced and checked;
- all arithmetic is exact modulo \(p\);
- the source, proof certificates, or output data are independently checkable.

Because known theorems already settle \(t\le12\) and \(p-3\le t\le p-1\), only
\[
13\le t\le p-4
\]
needs checking in the unresolved finite range.

### A complete disproof

A disproof must provide:

- a specific prime \(p\);
- a specific subset
  \[
  A\subseteq\mathbb F_p\setminus\{0\};
  \]
- a proof that no bijection \(a_1,\dots,a_t\) from \(\{1,\dots,t\}\) onto \(A\) has pairwise distinct partial sums.

Equivalently, it must prove
\[
\forall (a_1,\dots,a_t)\text{ permutations of }A,\ 
\exists\,1\le i<j\le t
\]
such that
\[
\sum_{k=i+1}^{j}a_k=0.
\]

Merely listing a candidate set is not enough. Nonexistence can be verified through:

- a theoretical covering or obstruction argument;
- exhaustive enumeration of all \(t!\) orderings, with auditable code;
- a SAT/constraint encoding accompanied by a formally checkable UNSAT certificate such as LRAT;
- a complete dynamic-programming certificate covering every possible search state.

By the known results, any counterexample must satisfy
\[
13\le |A|\le p-4,
\]
hence necessarily \(p\ge17\). By the “all sufficiently large primes” theorem, any counterexample must also occur below some finite threshold.

---

## 3. WHAT DOES NOT COUNT

None of the following resolves the universal problem unless it covers every remaining case:

1. **Another sufficiently-large-\(p\) theorem.**  
   The problem is already known for all sufficiently large primes. Improving the unspecified threshold is not a complete solution unless it reaches all primes or is paired with exhaustive finite verification.

2. **Results for only part of the size range.**  
   For example, proving the assertion for
   \[
   t\le p^{0.99},\qquad t\ge p^{0.01},
   \]
   or \(t\) in a new density interval does not resolve uncovered sizes.

3. **Fixed-\(t\) results.**  
   Extending \(t\le12\) to \(t\le100\) is useful but incomplete.

4. **Almost-all statements.**  
   Proving that almost every subset \(A\), or almost every ordering of a typical \(A\), is valid does not handle adversarial sets.

5. **Conditional results.**  
   A proof conditional on GRH, a sumset conjecture, an unproved form of Alspach’s conjecture, or an unverified computational assumption is not unconditional resolution.

6. **Heuristics or randomized experiments.**  
   Finding valid orderings for all tested sets, or showing that a random permutation succeeds with high probability in experiments, is not a proof for all sets.

7. **A greedy algorithm without a completion theorem.**  
   It is easy to continue greedily through roughly half the positions, but a greedy process can become trapped near the end.

8. **Proving the wrong stronger condition.**  
   Requiring \(S_0,S_1,\dots,S_t\) all distinct is impossible for zero-sum sets such as \(A=\mathbb F_p^\times\). Failure of that stronger problem says nothing about the stated one.

9. **An explicit set for which one search algorithm fails.**  
   Failure of a particular greedy, local-search, or randomized algorithm does not show that no valid ordering exists.

---

## 4. KNOWN RESULTS AND CONTEXT

### General context: Alspach’s conjecture

This is a prime cyclic instance of a conjecture commonly attributed to Alspach: every subset of the nonidentity elements of a finite abelian group should admit a simple or valid ordering. The general abelian-group conjecture is broader and remains difficult.

### Exact size ranges

The commentary records the following results.

1. **Full nonzero set:** Graham proved the result when
   \[
   t=p-1,
   \qquad A=\mathbb F_p\setminus\{0\}.
   \]

2. **Small absolute size:** Costa and Pellegrini, together with earlier work cited by them, proved the result for
   \[
   t\le12.
   \]

3. **Codimension at most three:** Hicks, Ollis, and Schmitt, together with earlier work, proved it for
   \[
   p-3\le t\le p-1.
   \]

Therefore an unresolved counterexample must lie in
\[
13\le t\le p-4.
\]

### Asymptotic results covering all sizes

The commentary states that four types of results together prove the conjecture for every sufficiently large prime.

#### Small \(A\)

Kravitz proved the assertion for
\[
t\le \frac{\log p}{\log\log p}.
\]
This was also independently observed earlier by Will Sawin.

Bedert and Kravitz extended the range to
\[
t\le \exp\!\big(c(\log p)^{1/4}\big)
\]
for some absolute \(c>0\).

Costa and Della Fiore further extended it to
\[
t\le \exp\!\big(c(\log p)^{1/3}\big)
\]
for some \(c>0\).

#### Medium \(A\)

Pham and Sauermann proved that for every fixed \(0<\alpha<1\), the assertion holds when
\[
1\ll_\alpha t\le p^{1-\alpha}.
\]
Here \(1\ll_\alpha t\) means \(t\ge C(\alpha)\) for a constant depending on \(\alpha\).

#### Large \(A\)

Bedert, Bucić, Kravitz, Montgomery, and Müyesser proved the assertion in a range
\[
p^{1-c}\le t\le (1-o(1))p
\]
for some small absolute \(c>0\).

#### Very large \(A\)

Müyesser and Pokrovskiy proved it for
\[
t\ge(1-o(1))p.
\]

By choosing the parameters so that these ranges overlap, and taking \(p\) sufficiently large, they cover every \(1\le t\le p-1\).

### What is already settled

The problem is completely settled for:

- every \(A\) with \(|A|\le12\);
- every \(A\) with \(|A|\ge p-3\);
- every \(A\) for all sufficiently large primes \(p\).

Thus the remaining universal question is finite in principle.

### Meaning of the database status “DECIDABLE”

The status should not be read as “already proved true.” It indicates that the asymptotic theorem reduces the original universal assertion to finitely many primes, so a finite exact computation can in principle determine whether the answer is yes or no.

This requires an effective threshold. The asymptotic proofs are finitary and should in principle yield one, but extracting a usable numerical value may be a substantial task. A threshold that is merely existential or astronomically large makes practical computation difficult even though logical decidability remains.

### A useful probabilistic criterion

For \(0\le\ell\le t\), let
\[
N_\ell(A):=
\#\left\{B\subseteq A:|B|=\ell,\ \sum_{b\in B}b=0\right\}.
\]
Choose a uniformly random permutation of \(A\). A fixed internal interval of length \(\ell\) has a uniformly random \(\ell\)-element underlying set, so its probability of having sum zero is
\[
\frac{N_\ell(A)}{\binom t\ell}.
\]
There are \(t-\ell\) intervals of length \(\ell\) beginning at position \(2\) or later. Hence the expected number of forbidden zero-sum intervals is
\[
E(A)=
\sum_{\ell=1}^{t-1}
(t-\ell)\frac{N_\ell(A)}{\binom t\ell}.
\]
Therefore
\[
E(A)<1
\]
is a rigorous sufficient condition for \(A\) to have a valid ordering. Conversely, every counterexample must satisfy \(E(A)\ge1\). The converse is only a necessary condition, not a sufficient one.

---

## 5. TRAPS AND EDGE CASES

### 5.1 Zero partial sums are allowed

The condition is not \(S_m\ne0\). A valid ordering may have one partial sum equal to \(0\). It cannot have two such partial sums.

In particular, if \(\sum_{a\in A}a=0\), then \(S_t=0\), and validity only requires
\[
S_m\ne0\qquad(1\le m<t).
\]

### 5.2 The first position is exceptional

The equivalent interval condition only prohibits zero-sum consecutive blocks beginning at position \(2\) or later. A zero-sum prefix
\[
a_1+\cdots+a_j=0
\]
does not by itself violate validity, because that compares \(S_j\) to the excluded value \(S_0\).

This asymmetry means that many circular or reversal arguments are invalid.

### 5.3 Reversal need not preserve validity

For the reversed sequence,
\[
T_m=S_t-S_{t-m}.
\]
Distinctness of \(T_1,\dots,T_t\) involves \(S_0,\dots,S_{t-1}\), whereas the original condition involves \(S_1,\dots,S_t\). Thus reversal may fail when a proper prefix has sum zero.

Likewise, cyclic rotations need not preserve validity.

### 5.4 Scaling is a symmetry; translation is not

For every \(\lambda\in\mathbb F_p^\times\),
\[
A\text{ has a valid ordering}
\iff
\lambda A:=\{\lambda a:a\in A\}\text{ has one}.
\]
All partial sums are simply multiplied by \(\lambda\).

By contrast, replacing every \(a\) by \(a+c\) changes the \(m\)-th partial sum by \(mc\), so translation is not a valid symmetry. It may also introduce \(0\).

For prime fields, the additive-group automorphisms are exactly the nonzero scalings.

### 5.5 Complementation is not an automatic symmetry

Even though
\[
\sum_{x\in\mathbb F_p^\times}x=0,
\]
there is no immediate equivalence between the ordering problem for \(A\) and for \(\mathbb F_p^\times\setminus A\). Complementation must not be used as a search reduction without a proof.

### 5.6 The property is not obviously monotone

A valid ordering of \(A\) does not automatically induce a valid ordering of a subset after deleting entries: deletion shifts later partial sums and can create collisions. Likewise, adding one element to a valid set need not preserve a given ordering.

### 5.7 Greedy continuation stalls near the midpoint

After \(m\) elements have been chosen, let \(s\) be the current sum and let \(V\) be the set of the \(m\) partial sums already seen. A remaining \(a\) is immediately forbidden only when
\[
s+a\in V.
\]
There are at most \(m\) such values of \(a\). Thus if
\[
t-m>m,
\]
at least one legal next step exists.

This only guarantees progress while fewer than about half the elements have been used. It does not give a completion argument.

### 5.8 Small and degenerate cases

- \(A=\varnothing\): vacuous.
- \(t=1\): always valid.
- \(t=2\): always valid, since \(S_2-S_1=a_2\ne0\).
- \(p=2\): only \(A=\varnothing\) or \(A=\{1\}\), both trivial.
- Existing results settle all \(t\le12\), so hand checking these cases does not advance the unresolved range.

### 5.9 Union-bound direction

The criterion \(E(A)<1\) proves existence. The condition \(E(A)\ge1\) does not prove nonexistence; it only means that the simplest first-moment argument fails.

### 5.10 Asymptotic notation must be made effective

A statement such as \(t\ge(1-o(1))p\) is not itself a finite algorithm unless the \(o(1)\) term and the threshold are extracted. Stitching asymptotic ranges must be done with explicit parameter dependencies if the goal is certified finite reduction.

---

## 6. VERIFICATION HOOKS

### 6.1 Checking a proposed ordering

Given \(p\), \(A\), and a claimed ordering \(a_1,\dots,a_t\):

1. verify that every \(a_i\) is a nonzero residue;
2. verify that the \(a_i\) are distinct and their set equals \(A\);
3. initialize an empty Boolean array or hash set \(V\);
4. compute
   \[
   s\leftarrow s+a_i\pmod p
   \]
   successively;
5. reject if \(s\in V\), otherwise insert \(s\).

This takes \(O(t)\) modular operations with a residue bitset, or \(O(t\log t)\) with a balanced set.

Do **not** initialize \(V\) with \(0\).

### 6.2 Exact backtracking search

Maintain:

- \(U\subseteq A\), the used elements;
- \(V\subseteq\mathbb F_p\), the partial sums already seen;
- the current sum
  \[
  s=\sum_{a\in U}a,
  \]
  which is determined by \(U\).

A transition adding \(a\in A\setminus U\) is legal exactly when
\[
s+a\notin V.
\]
The next state is
\[
\bigl(U\cup\{a\},\,V\cup\{s+a\}\bigr).
\]

Pseudocode:

```text
Search(U, V):
    if U = A:
        return success
    s := sum(U) mod p
    for a in A \ U:
        z := s + a mod p
        if z not in V:
            if Search(U ∪ {a}, V ∪ {z}) succeeds:
                return success
    return failure
```

Memoization can use the exact state \((U,V)\). The set \(U\) alone is insufficient because different chains reaching the same \(U\) may have different previously seen partial sums.

### 6.3 SAT or CSP encoding

For a fixed candidate \(A\), encode:

- \(x_{i,a}\): element \(a\) occupies position \(i\);
- exactly-one constraints for positions and elements;
- \(y_{i,r}\): the \(i\)-th partial sum equals \(r\in\mathbb F_p\);
- modular recurrence constraints;
- all-different constraints among \(y_{1},\dots,y_t\).

SAT means a valid ordering exists. UNSAT proves that \(A\) is a counterexample, provided the encoding is proved correct and a checkable UNSAT certificate is supplied.

### 6.4 Exhaustive subset enumeration

For each relevant \(p\), enumerate only
\[
13\le |A|\le p-4.
\]
Reduce under the proved symmetry
\[
A\sim\lambda A,\qquad \lambda\in\mathbb F_p^\times.
\]
A canonical representative can be the lexicographically smallest residue bitmask among all \(\lambda A\).

Do not quotient by translation, reversal, or complementation without additional proof.

### 6.5 Zero-sum subset profile

Compute \(N_\ell(A)\) by dynamic programming:
\[
D[\ell][r]
=
\#\{B\subseteq A:|B|=\ell,\ \sum B=r\}.
\]
Initialize \(D[0][0]=1\), and update once for each \(a\in A\). Then
\[
N_\ell(A)=D[\ell][0].
\]

Use the exact rational value
\[
E(A)=\sum_{\ell=1}^{t-1}
(t-\ell)\frac{N_\ell(A)}{\binom t\ell}.
\]
If \(E(A)<1\), the set is certified positive without permutation search. Candidate counterexamples must have \(E(A)\ge1\).

### 6.6 Polynomial identity check

Define
\[
P(x_1,\dots,x_t)
=
\prod_{1\le i<j\le t}
\left(x_{i+1}+\cdots+x_j\right).
\]
For a permutation \((a_1,\dots,a_t)\) of \(A\),
\[
P(a_1,\dots,a_t)\ne0
\]
if and only if the ordering is valid.

To force the \(x_i\) to be distinct, define
\[
\Delta(x_1,\dots,x_t)=
\prod_{1\le r<s\le t}(x_s-x_r),
\qquad
Q=\Delta P.
\]
On \(A^t\), \(Q\ne0\) exactly at valid permutations.

Let
\[
f_A(X)=\prod_{a\in A}(X-a).
\]
Reduce \(Q\) modulo
\[
f_A(x_1),\dots,f_A(x_t)
\]
to the unique polynomial with degree \(<t\) in each variable. Multivariate interpolation gives:
\[
A\text{ has a valid ordering}
\iff
Q\bmod(f_A(x_1),\dots,f_A(x_t))\ne0.
\]
This is practical only for small \(t\), but it is an exact regression test for algebraic conjectures.

---

## 7. ATTACK ROUTES

### Route 1: Extract an effective threshold and perform certified finite verification

**Core mechanism.** Use the four asymptotic results to derive an explicit \(P_0\), then exhaustively solve every remaining prime and subset orbit.

**Key lemma needed.** An explicit range-stitching theorem of the form:
\[
p\ge P_0\implies
\text{every }A\subseteq\mathbb F_p^\times\text{ has a valid ordering},
\]
with every constant and threshold computable.

**Why it might work.** This is the most direct route justified by the database status. The mathematical problem is already known to have only finitely many possible exceptions.

**Likely failure point.** Constants hidden in \(c\), \(o(1)\), and \(1\ll_\alpha t\) may produce an astronomically large \(P_0\). Exhausting \(2^{p-1}\) subsets is infeasible unless the threshold is quite small or stronger reductions are found.

**Quick blockage test.**

1. Extract numerical constants from each cited proof.
2. Optimize \(\alpha\) to overlap the medium and large ranges.
3. Compute the resulting \(P_0\).
4. Benchmark exact search for all orbit representatives at the largest feasible \(p\).

If \(P_0\) exceeds even a few dozen without major additional structure, naive enumeration is blocked.

---

### Route 2: Rainbow-chain and insertion/exchange theory

**Core mechanism.** Work in the Boolean lattice colored by subset sum. Build a maximal chain with no repeated nonempty color, using insertion, deletion, and augmenting-path exchanges.

**Key lemma needed.** A robust extension statement, for example:

> Every valid chain through a sufficiently large subset can be modified locally so that some new element can be inserted while preserving all colors; or every minimal nonextendible chain admits an exchange that strictly increases an appropriate potential.

A stronger endpoint-flexibility lemma, giving many possible first elements or many possible terminal chains, would be especially useful.

**Why it might work.** The problem is exactly a rainbow maximal-chain problem with highly structured colors:
\[
c(U\cup\{a\})=c(U)+a.
\]
The distinct nonzero increments may prevent the arbitrary obstructions possible in general colorings of the Boolean lattice.

**Likely failure point.** A particular valid ordering of \(A\setminus\{x\}\) may have every insertion slot blocked. Local extendibility is much stronger than global existence, and exchange operations can create distant partial-sum collisions.

**Quick blockage test.** Exhaustively enumerate small sets and valid orderings, and ask:

- Does every valid ordering extend after adding every missing \(x\)?
- If not, does each enlarged set have some deletable \(x\) and some valid ordering of \(A\setminus\{x\}\) that extends?
- Are there minimal nonextendible chain states with no one- or two-element exchange?

Small counterexamples to the proposed extension lemma should be found quickly.

---

### Route 3: Polynomial method and Combinatorial Nullstellensatz

**Core mechanism.** Prove that
\[
Q=\Delta P
\]
does not vanish identically on \(A^t\), or identify a universally nonzero coefficient in its interpolation remainder.

**Key lemma needed.** A statement such as:
\[
Q\bmod(f_A(x_1),\dots,f_A(x_t))\ne0
\]
for every \(A\subseteq\mathbb F_p^\times\), possibly established by a distinguished monomial coefficient, determinant, or alternating-sum formula.

**Why it might work.** The validity condition is represented exactly by a product of linear forms, while the Vandermonde factor enforces that the tuple is a permutation. The problem is therefore an exact finite-field nonvanishing question.

**Likely failure point.**

- The total degree is large.
- Standard Combinatorial Nullstellensatz degree criteria may not fit the grid size.
- Characteristic-\(p\) cancellation may annihilate natural coefficients.
- The first variable is exceptional: \(P\) itself does not depend on \(x_1\), reflecting the exclusion of \(S_0\).

**Quick blockage test.** For small \(t\) and many primes:

1. compute the reduced interpolation polynomial;
2. inspect coefficients that remain nonzero across all \(A\);
3. test proposed determinant or coefficient formulas symbolically;
4. look for characteristic-dependent cancellations.

If every plausible universal coefficient vanishes for some positive instance, a simple one-coefficient Nullstellensatz proof is blocked.

---

### Route 4: Random permutations, switchings, and local lemma methods

**Core mechanism.** Choose a random permutation and control the bad events
\[
B_{r,s}:=\left\{\sum_{k=r}^{s}a_k=0\right\},
\qquad 2\le r\le s\le t.
\]

**Key lemma needed.** A uniform anti-concentration or switching estimate strong enough to show that the bad events do not cover all permutations, even for highly structured \(A\). A useful form would bound zero-sum subset counts \(N_\ell(A)\), or establish lopsided negative dependence between interval events.

**Why it might work.** The exact first-moment expression
\[
E(A)=\sum_{\ell=1}^{t-1}
(t-\ell)\frac{N_\ell(A)}{\binom t\ell}
\]
already settles every set with \(E(A)<1\). Local resampling or switching may handle cases where the expectation exceeds \(1\) but the bad events overlap heavily.

**Likely failure point.** Arbitrary \(A\) may contain many zero-sum subsets, especially many pairs \(\{x,-x\}\). The probability of an interval sum being zero is not uniformly \(1/p\), and interval events have extensive dependence.

**Quick blockage test.**

- Compute \(E(A)\) over all small subset orbits.
- Identify sets maximizing \(E(A)\).
- Compare \(E(A)\) with the actual fraction of valid permutations.
- Test whether a lopsided local lemma criterion holds using exact event dependencies.

If known positive sets have very large \(E(A)\) and near-total bad-event coverage, basic probabilistic methods need substantial structural input.

---

### Route 5: Additive-structural dichotomy plus absorption

**Core mechanism.** Split sets into pseudorandom and additively structured classes. Use probabilistic ordering in the pseudorandom case and explicit block construction with absorbers in the structured case.

**Key lemma needed.** A dichotomy of the following kind:

- either zero-sum subsets of every relevant size are sufficiently sparse for a random/switching argument;
- or \(A\) has enough additive structure to partition most elements into blocks with controlled nonzero sums, while a small absorber can incorporate the leftover elements without creating repeated partial sums.

**Why it might work.** The successful small, medium, large, and very large results already use different mechanisms in different density regimes. A unified quantitative dichotomy might eliminate the remaining threshold and produce a proof valid for all primes.

**Likely failure point.** High counts of zero-sum subsets are not governed solely by ordinary doubling or additive energy. Dense modular wraparound and configurations containing many opposite pairs may be structured in incompatible ways. Absorbing elements changes many subsequent partial sums simultaneously.

**Quick blockage test.**

1. For computationally hard small sets, calculate:
   - additive energy;
   - doubling size \(|A+A|\);
   - zero-sum subset profile \(N_\ell(A)\);
   - number and fraction of valid orderings.
2. Check whether hard instances cluster into recognizable structural classes.
3. Attempt an absorber of constant size and test all possible boundary sums.

If hard sets exhibit no stable structural signature, a simple Freiman-type dichotomy is unlikely to suffice.

---

### Route 6: Targeted disproof via zero-sum interval coverings

**Core mechanism.** Search for a finite exceptional set \(A\) whose proper zero-sum subsets force a forbidden interval in every permutation.

Let
\[
\mathcal Z(A)=
\left\{B\subsetneq A:
B\ne\varnothing,\ \sum_{b\in B}b=0\right\}.
\]
A counterexample is exactly a set for which every permutation has some \(B\in\mathcal Z(A)\) occupying consecutive positions that do not begin at position \(1\).

**Key lemma needed.** Construct or certify a family \(\mathcal Z(A)\) that covers every permutation in this sense. Promising candidates include sets with:

- many opposite pairs \(\{x,-x\}\);
- unions of multiplicative cosets;
- highly symmetric intervals around \(0\);
- exceptional zero-sum subset-size distributions.

**Why it might work.** Since all sufficiently large primes are settled, any counterexample must be an isolated finite phenomenon. That makes targeted SAT mining and symmetry-heavy small-prime searches more appropriate than seeking an infinite construction.

A necessary screening condition is
\[
\sum_{\ell=1}^{t-1}
(t-\ell)\frac{N_\ell(A)}{\binom t\ell}\ge1.
\]

**Likely failure point.** Many zero-sum subsets do not necessarily force one to appear contiguously away from the first position. Graham’s theorem for \(A=\mathbb F_p^\times\) demonstrates that maximal additive richness is compatible with a valid ordering.

**Quick blockage test.**

1. Restrict to primes above \(17\) and sizes \(13\le t\le p-4\).
2. Rank subset orbits by \(E(A)\), number of opposite pairs, and zero-sum subset counts.
3. Run proof-producing SAT on the highest-ranked candidates.
4. If UNSAT is found, independently verify the LRAT certificate.
5. If every high-density candidate is easily satisfiable, the zero-sum-covering heuristic is weak.

---

## 8. VERDICT ON DIFFICULTY

Historically, this is a significant special case of Alspach’s valid-ordering conjecture for finite abelian groups. A uniform conceptual proof would still be substantial.

However, according to the supplied commentary, the asymptotic existence problem is already settled: every sufficiently large prime works for every subset size. Consequently:

- the universal statement has only finitely many possible exceptions;
- any counterexample must satisfy
  \[
  13\le |A|\le p-4
  \]
  and lie below an effective finite threshold;
- the problem is in principle decidable by exact computation.

The central practical issue is therefore not a famous unresolved conjectural barrier such as GRH or the full Alspach conjecture. It is the extraction of effective constants and the feasibility of the resulting finite verification. If the available threshold is enormous, a direct computation may remain hopeless without a new uniform argument or much stronger finite-range reductions.

**Difficulty assessment:**

- **Conceptual all-prime proof:** hard and research-level.
- **Logical decidability:** already supplied by the sufficiently-large-prime theorem, assuming effective extraction.
- **Practical finite resolution:** potentially difficult because the threshold and search space may be enormous.
- **Disproof prospects:** finite and therefore testable, but constrained by all known results; any counterexample would be a small exceptional configuration rather than an infinite family.

The highest-priority first step is to extract the best explicit threshold from the cited papers. That calculation determines whether the problem should be attacked primarily as a proof-producing computation or as a search for a new uniform structural argument.