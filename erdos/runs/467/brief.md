# Problem Brief: Erdős Problem #467

## 1. Precise statement

### 1.1 Formal reading

Let
\[
\mathcal P(x):=\{p:\ p\text{ is prime and }p\le x\}.
\]
The most literal standard analytic-number-theory reading is:

> There exists \(X_0>0\) such that, for every real \(x\ge X_0\), there exist:
> - for each \(p\in\mathcal P(x)\), a residue class
>   \[
>   a_p\in \mathbb Z/p\mathbb Z,
>   \]
> - a partition
>   \[
>   \mathcal P(x)=A\sqcup B,\qquad A\ne\varnothing,\quad B\ne\varnothing,
>   \]
> such that for every positive integer \(n<x\), there are primes \(p\in A\) and \(q\in B\), possibly depending on \(n\), for which
> \[
> n\equiv a_p\pmod p
> \quad\text{and}\quad
> n\equiv a_q\pmod q.
> \]

Equivalently, the selected residue classes belonging to \(A\) cover every positive integer below \(x\), and the selected classes belonging to \(B\) independently cover every positive integer below \(x\).

The primes \(p\) and \(q\) are automatically distinct because \(A\cap B=\varnothing\).

All choices may depend on \(x\).

### 1.2 Necessary interpretation of “\(n<x\)”

Here \(n\) must mean a positive integer. If it meant every integer \(n<x\), including arbitrarily negative integers, the statement would be false: given finitely many selected residue classes, the Chinese remainder theorem can produce infinitely many integers avoiding all of them.

If \(n\) is allowed to include \(0\), the interval length changes by one; this is not logically identical at the exact endpoint.

### 1.3 Real-\(x\) versus integer-\(x\) formulations

For real \(x\), let
\[
L(x):=\#\{n\in\mathbb Z_{>0}:n<x\}=\lceil x\rceil-1.
\]
The literal problem asks for two covers of an interval of \(L(x)\) consecutive integers using primes at most \(x\).

The all-real formulation is equivalent, up to the threshold, to the following cleaner integer statement:

> For every sufficiently large integer \(m\), partition the primes \(p\le m\) into two nonempty sets and choose one residue class modulo each prime so that both colors cover
> \[
> [m]:=\{1,2,\dots,m\}.
> \]

Indeed, apply the real statement at \(x=m+\tfrac12\). Conversely, a cover of \([m]\) by primes at most \(m\) handles every \(x\) with \(\lfloor x\rfloor=m\).

If the original source intended \(x\) to range only over integers, then the required interval is instead
\[
\{1,\dots,x-1\}.
\]
This produces a genuine off-by-one difference in the exact Jacobsthal reformulation below. The database explicitly warns that the original presentation in [ErGr80] omitted crucial quantifiers. The all-real formulation above is the strongest natural literal reading; the integer-only alternative should be tracked separately.

### 1.4 Exact CRT/Jacobsthal reformulation

For an integer \(M>1\), define the Jacobsthal function
\[
j(M):=\min\bigl\{\ell\ge1:\text{ every }\ell\text{ consecutive integers contain an integer coprime to }M\bigr\}.
\]
Equivalently, if
\[
R(M):=\max\left\{r\ge0:\exists t\in\mathbb Z\ \forall 1\le n\le r,\ \gcd(t+n,M)>1\right\},
\]
then
\[
j(M)=R(M)+1.
\]

For a finite set of primes \(S\), put
\[
P_S:=\prod_{p\in S}p.
\]
A choice of classes \(a_p\pmod p\) for \(p\in S\) covers \(\{1,\dots,L\}\) if and only if
\[
R(P_S)\ge L,
\]
or equivalently
\[
j(P_S)\ge L+1.
\]

Proof: by the Chinese remainder theorem there is a \(t\) satisfying
\[
t\equiv -a_p\pmod p\qquad(p\in S).
\]
Then
\[
n\equiv a_p\pmod p
\iff p\mid t+n.
\]
Thus the classes cover \(1,\dots,L\) exactly when every \(t+n\) has a prime divisor in \(S\).

Let
\[
Q_m:=\prod_{p\le m}p.
\]
Under the all-real interpretation, the problem is exactly:

> Prove that for every sufficiently large integer \(m\), there is a factorization
> \[
> Q_m=uv,\qquad u>1,\quad v>1,\quad \gcd(u,v)=1,
> \]
> such that
> \[
> j(u)\ge m+1
> \quad\text{and}\quad
> j(v)\ge m+1.
> \]

Here \(u\) and \(v\) are products of complementary sets of primes at most \(m\).

Under the integer-only interpretation, the target is instead
\[
j(u)\ge m,\qquad j(v)\ge m.
\]

This factorization formulation is likely the cleanest one for research.

---

## 2. What counts as a solution

### 2.1 Complete proof

A complete proof must establish a threshold \(X_0\), effective or ineffective, such that the required data exist for every \(x\ge X_0\). It is not enough to obtain an unbounded sequence of successful \(x\).

A proof may proceed in any of the following equivalent ways:

1. Directly construct the partition \(A\sqcup B\) and classes \(a_p\).
2. Construct disjoint prime sets \(A,B\) and shifts \(t_A,t_B\) satisfying
   \[
   \forall n<x,\quad
   \gcd\left(t_A+n,\prod_{p\in A}p\right)>1
   \]
   and
   \[
   \gcd\left(t_B+n,\prod_{q\in B}q\right)>1.
   \]
3. Prove the Jacobsthal factorization statement for every sufficiently large \(m\).

It is enough initially to construct two disjoint subfamilies of primes giving the two covers. Any unused primes can then be distributed arbitrarily between the two sides: adjoining prime factors to \(u\) or \(v\) cannot decrease \(R\) or \(j\), and their classes can be chosen compatibly with the existing shift.

The two shifts \(t_A,t_B\) need not be equal.

### 2.2 Complete disproof

Because the assertion is “for all sufficiently large \(x\),” one isolated bad value of \(x\) does not disprove it.

A complete disproof must establish arbitrarily large bad parameters. Under the all-real/integer-\(m\) reformulation, this means proving that there are infinitely many, or at least an unbounded sequence of, integers \(m\) such that for every factorization
\[
Q_m=uv,\qquad \gcd(u,v)=1,\quad u,v>1,
\]
one has
\[
\min\{j(u),j(v)\}\le m.
\]

Equivalently, for every partition of the primes up to \(m\), at least one color cannot cover an interval of \(m\) consecutive integers.

A computationally explicit bad \(m\) must come with a verifiable exhaustive certificate that no assignment of colors and residues works. Such a finite certificate establishes only failure at that \(m\), not failure of the eventual assertion. A disproof needs a proof producing bad \(m\) without bound.

---

## 3. What does not count

The following do not resolve the problem:

- Covering all but \(o(x)\), \(O(x/\log x)\), or even one integer below \(x\).
- Proving that every \(n<x\) is covered by at least two selected classes without proving that the primes can be globally 2-colored so that each \(n\) sees both colors.
- Giving two covers that use overlapping prime sets.
- Allowing two different residue classes modulo the same prime, one for each cover.
- Using primes up to \(Cx\), \(x^{1+\varepsilon}\), or another larger bound without a valid reduction to primes at most \(x\).
- Covering an interval of length \((1-\varepsilon)x\) for fixed \(\varepsilon>0\).
- Proving the assertion only for infinitely many \(x\), rather than every sufficiently large \(x\).
- A probabilistic heuristic saying that a successful assignment should exist.
- A conditional proof depending on an unproved conjecture, unless the condition itself is discharged.
- Showing only that the union \(A\cup B\) gives a cover.
- Showing that a specially prescribed partition fails; the conjecture allows the partition to be chosen adaptively.
- Establishing large \(j(Q_m)\) for the full primorial without splitting its prime factors into two successful products.
- A finite list of successful computations, regardless of size.

Under the all-real reading, a proof only for the integer interval \(\{1,\dots,m-1\}\) also leaves an exact endpoint gap unless an argument handles the additional point.

---

## 4. Known results and context

### 4.1 Database information

The database lists the problem as open and supplies no substantive previous theorem. Its commentary explicitly warns that the formulation in [ErGr80] is missing important quantifiers and that the database statement is an interpretation of the intended problem.

Accordingly, the positive-integer quantifier, the dependence of all choices on \(x\), and the real-versus-integer convention should be stated in any claimed solution.

### 4.2 Chinese remainder theorem

The CRT reformulation above is exact and central. Within one color, arbitrary selected classes modulo distinct primes always arise from a single shift \(t\) modulo the product of those primes.

Thus the problem is not merely analogous to a Jacobsthal problem; it is precisely a two-factor Jacobsthal problem for the primorial.

### 4.3 Jacobsthal function

General Jacobsthal estimates are relevant. A standard theorem of Iwaniec gives, in terms of the number \(\omega(M)\) of distinct prime factors,
\[
j(M)\ll \omega(M)^2(\log \omega(M))^2.
\]
For a factor containing about half the primes up to \(m\), this upper bound is roughly of order \(m^2\), far too large to obstruct the desired lower bound \(j(M)>m\). Thus known general upper bounds do not settle the problem.

### 4.4 Covering congruences and large prime gaps

The Erdős–Rankin method and later work on large prime gaps construct long intervals covered by residue classes modulo primes. In modern forms, these methods can use primes up to a parameter \(z\) to cover intervals substantially longer than \(z\).

This settles much stronger one-family covering questions. It does not automatically solve the present problem, because the crucial small and medium primes must be divided into two disjoint reservoirs, each of which must support its own complete covering.

The modern large-gap work of Ford, Green, Konyagin, Maynard and Tao is relevant as a source of highly optimized sieve-and-cleanup constructions, but no standard theorem from that theory immediately supplies two disjoint covers.

### 4.5 Mertens estimates and the density barrier

Mertens' theorems for primes give
\[
\sum_{p\le m}\frac1p=\log\log m+O(1),
\qquad
\prod_{p\le m}\left(1-\frac1p\right)\asymp \frac1{\log m}.
\]

If the primes are split into two portions with about half the reciprocal-prime mass, a naive random-sieve model predicts survivor density around
\[
(\log m)^{-1/2}
\]
for each side, leaving about
\[
\frac{m}{\sqrt{\log m}}
\]
uncovered points. This is substantially larger than the roughly \(m/\log m\) primes available in a terminal large-prime interval for singleton cleanup. This is only a heuristic, not an impossibility theorem, but it explains why simply splitting a standard one-cover construction is difficult.

### 4.6 A basic capacity condition

For an interval of length \(m\), one residue class modulo \(p\) contains at most
\[
\left\lceil\frac mp\right\rceil
\]
points. Therefore any prime set \(S\) capable of covering \([m]\) must satisfy
\[
\sum_{p\in S}\left\lceil\frac mp\right\rceil\ge m.
\]

Consequently a necessary condition for a two-cover partition is
\[
\sum_{p\le m}\left\lceil\frac mp\right\rceil\ge 2m.
\]
This is much too weak asymptotically, but useful in finite searches and in checking proposed structural lemmas.

---

## 5. Traps and edge cases

1. **The two covering primes depend on \(n\).** There is no fixed pair \(p,q\).

2. **The two shifts are independent.** The CRT gives one shift \(t_A\) for \(A\) and another shift \(t_B\) for \(B\). Requiring \(t_A=t_B\) is a much stronger problem.

3. **Double coverage is not enough.** If every \(n\) lies in at least two selected classes, it does not follow that the prime vertices can be 2-colored so every incidence set is bichromatic. For example, size-two incidence sets can encode an odd cycle.

4. **Small-prime overlap is usually severe.** Arguments that sum the densities \(1/p\) without controlling overlap do not establish a cover.

5. **Random expected coverage is insufficient.** The events for different \(n\) are strongly dependent, especially through small primes.

6. **A large prime need not be a strict singleton.** If \(m/2<p<m\), a residue modulo \(p\) can contain two points of \([m]\), but only a pair differing by exactly \(p\). For \(p=m\), it contains at most one point. Cleanup arguments must use the exact geometry.

7. **All primes must formally be assigned.** However, once two disjoint successful subfamilies are found, unused primes can safely be added to either side.

8. **Boundary convention matters.** Real \(x\), integer \(x\), \(n<x\), and \(n\le x\) differ by one point. That point is logically significant in a complete proof.

9. **A single failed \(m\) is not a counterexample to eventual truth.**

10. **Do not confuse ordinary composite intervals with the required intervals.** Every integer in the shifted block must have a prime divisor from the designated color set, hence at most \(m\), not merely be composite.

11. **The product \(P_S\) is enormous but periodicity is exact.** Claims about \(j(P_S)\) must quantify over shifts modulo \(P_S\), even when direct period enumeration is impossible.

12. **Average multiplicity is small.** The total number of incidences in any choice of one class per prime is at most
    \[
    \sum_{p\le m}\left\lceil\frac mp\right\rceil
    =m\log\log m+O(m).
    \]
    Thus the average point is covered only \(O(\log\log m)\) times. Any route demanding \(C\log m\) coverage at every point is impossible.

---

## 6. Verification hooks

### 6.1 Direct witness checker

For a fixed integer \(m\), a proposed witness consists of:

- the list of all primes \(p\le m\);
- a color \(c_p\in\{A,B\}\) for each \(p\);
- a residue \(a_p\in\{0,\dots,p-1\}\).

Verification:

```text
for n = 1,...,m:
    hitA = false
    hitB = false
    for p <= m prime:
        if n mod p == a_p:
            if c_p == A: hitA = true
            if c_p == B: hitB = true
    reject unless hitA and hitB
accept
```

This is polynomial in the witness size.

### 6.2 SAT encoding

Introduce Boolean variables
\[
y_{p,c,r},\qquad
p\le m,\quad c\in\{A,B\},\quad 0\le r<p,
\]
meaning that \(p\) is assigned color \(c\) and residue \(r\).

For each prime \(p\), impose exactly one of the \(2p\) variables \(y_{p,c,r}\).

For each \(n\in[m]\), impose the two coverage clauses
\[
\bigvee_{p\le m} y_{p,A,n\bmod p},
\qquad
\bigvee_{p\le m} y_{p,B,n\bmod p}.
\]

For \(m\ge1\), these clauses force both colors to be nonempty. An UNSAT result should be accompanied by a DRAT/LRAT or comparable independently checkable proof certificate.

### 6.3 Bitset search

Represent each residue class
\[
\{n\in[m]:n\equiv r\pmod p\}
\]
as an \(m\)-bit mask. Backtracking then selects one colored mask per prime while tracking the uncovered masks for \(A\) and \(B\). Useful branching rules include:

- branch first on primes with the largest possible new coverage;
- branch on an uncovered \(n\) with the fewest available covering options;
- prune by the capacity bound
  \[
  \sum_{\text{remaining }p}\max_r |C_{p,r}\cap U|\ge |U|.
  \]

### 6.4 Jacobsthal checker for a fixed partition

For small \(m\), construct the wheel of residues coprime to
\[
P_S=\prod_{p\in S}p
\]
incrementally and compute the largest cyclic gap between reduced residues. This yields \(j(P_S)\). Full period enumeration becomes infeasible quickly, so the direct SAT formulation is preferable for larger finite tests.

### 6.5 Diagnostics to record

For successful or near-successful assignments, record:

- uncovered-set sizes after each prime scale;
- coverage multiplicity of every \(n\);
- number of points covered by each prime;
- distribution of differences between leftover points;
- whether the final 2-coloring is the obstruction, as opposed to obtaining two incidences per point;
- \(j(P_A)\), \(j(P_B)\), and their minimum for small cases.

These data can distinguish sieve failure from coloring failure.

---

## 7. Attack routes

### Route 1: Two-reservoir Erdős–Rankin construction

**Core mechanism.** Adapt a long-prime-gap covering construction so that every relevant prime range is divided into two disjoint reservoirs, each supporting a full cover.

**Needed lemma.** A robust covering lemma of the following kind:

> If every prescribed prime scale contains a set of primes of positive relative density, then residue classes from those primes can cover an interval of length at least \(m\).

One would partition each scale into two comparable reservoirs and run the lemma independently.

**Why it might work.** Existing large-gap constructions cover intervals longer than the largest available prime and already combine sieving, probabilistic selection, and a matching-style cleanup.

**Likely failure point.** Standard constructions exploit nearly all small primes. Halving their reciprocal mass leaves approximately \(m/\sqrt{\log m}\) random-model survivors, too many for a terminal singleton cleanup.

**Quick test.** Implement a standard greedy or randomized Erdős–Rankin-style sieve using alternating primes in every dyadic interval. Plot the residual count before the final prime range and compare it with the number and pairing capacity of unused large primes.

---

### Route 2: Build a 2-colorable incidence hypergraph directly

For selected classes define
\[
H_n:=\{p\le m:n\equiv a_p\pmod p\}.
\]
The desired partition is exactly a property-B coloring of the hypergraph \(\{H_n:n\in[m]\}\): every edge must meet both colors.

**Needed lemma.** Construct residues so that the incidence hypergraph has a guaranteed proper 2-coloring, perhaps through bounded dependency, a special interval structure, or a discrepancy theorem.

**Why it might work.** This attacks the simultaneous problem rather than building two covers separately. Carefully designed incidence sets might have much better colorability than arbitrary hypergraphs.

**Likely failure point.** Small primes create vertices of very high degree, while the average edge size is only \(O(\log\log m)\). Naive union bounds or Lovász local lemma conditions are unlikely to hold.

**Quick test.** Search computationally for residues maximizing minimum edge size, then separately test 2-colorability. Determine whether failures come from uncovered points, singleton edges, or genuinely non-2-colorable incidence patterns.

---

### Route 3: Two-stage sieve plus disjoint cleanup matchings

**Core mechanism.** Give each color private small and medium primes to reduce its uncovered set, then use disjoint large-prime reservoirs to cover the remaining points.

**Needed lemma.** For each color \(i\), choose one residue per private small/medium prime so that the leftover set \(U_i\) is small enough and structured enough to be covered by its reserved large primes. A sufficient form would be
\[
|U_i|\le \#\{\text{reserved large primes for color }i\},
\]
though exploiting pairs at distance \(p\) could weaken this requirement.

**Why it might work.** Large primes can always cover arbitrary singleton leftovers and can sometimes cover pairs. This reduces the terminal stage to a Hall-type matching or packing problem.

**Likely failure point.** With only half the small-prime mass, known random-sieve estimates leave too many points. The essential challenge is a highly nonrandom choice of residues that beats the density heuristic.

**Quick test.** Run exact greedy optimization on the first several prime ranges and solve the terminal cleanup as a bipartite matching/ILP. Measure the ratio of residual points to available cleanup primes.

---

### Route 4: Recursive extension of Jacobsthal factorizations

**Core mechanism.** Inductively maintain a factorization of \(Q_m\) into two products with long non-coprime runs, and absorb new primes while extending both runs.

**Needed lemma.** An extension theorem such as:

> Given two covered intervals of length \(m\) using disjoint primes up to \(m\), the primes in \((m,m']\) can be distributed and assigned so that both intervals extend to length \(m'\), while compatible representatives of the old CRT shifts are chosen.

**Why it might work.** A shift modulo an old product can be replaced by any congruent representative, and CRT then permits independent control modulo newly added primes. This gives more freedom than a literal fixed-interval induction suggests.

**Likely failure point.** New primes larger than \(m\) hit only one or a few points in the extended interval. A doubling step creates a tail much longer than the number of new primes.

**Quick test.** Starting from exact small solutions, formulate the extension from \(m\) to \(m+\Delta\) as SAT while freezing the old prime residues modulo their products but allowing new CRT representatives. Determine the largest feasible \(\Delta\).

---

### Route 5: Random primorial factorization and extreme Jacobsthal gaps

**Core mechanism.** Color each prime independently red or blue and study the largest gaps between integers coprime to the two complementary random products.

**Needed lemma.** With positive probability,
\[
j(P_{\mathrm{red}})>m
\quad\text{and}\quad
j(P_{\mathrm{blue}})>m.
\]
A weaker sufficient theorem could impose balanced prime counts in each scale and then prove that every such sufficiently pseudorandom factor has a long Jacobsthal gap.

**Why it might work.** The periods \(P_{\mathrm{red}}\) and \(P_{\mathrm{blue}}\) are exponentially enormous. Even if a fixed block is unlikely to be fully covered, there are vast numbers of candidate shifts, so extreme-value effects may create long covered blocks.

**Likely failure point.** Candidate blocks are strongly dependent, and sieve lower bounds may force reduced residues to be too regularly distributed. Proving extreme gaps at the required scale may be as difficult as the original problem.

**Quick test.** For small \(m\), sample balanced random partitions, compute exact Jacobsthal values by wheel methods, and compare \(\min(j(P_A),j(P_B))\) with \(m\). Check whether the ratio trends upward, downward, or remains near one.

---

### Route 6: Disproof through a two-factor Jacobsthal upper bound

**Core mechanism.** Prove that the prime factors of a primorial cannot be divided so that both factors have Jacobsthal gaps longer than \(m\).

**Needed lemma.** For infinitely many \(m\),
\[
Q_m=uv,\quad \gcd(u,v)=1
\quad\Longrightarrow\quad
\min\{j(u),j(v)\}\le m.
\]
Potential tools include lower-bound sieves, larger-sieve inequalities, weighted interval arguments, or a dual certificate showing that one color must leave a coprime point in every block of length \(m\).

**Why it might work.** Splitting reciprocal-prime mass in half appears to leave each side with a survivor set much denser than the full primorial survivor set. There may be a genuine resource obstruction hidden by the flexibility of residue choices.

**Likely failure point.** Long prime-gap constructions show that independence heuristics can be defeated dramatically by optimized residue choices. Existing lower-bound sieve methods are often weakest precisely near the critical range needed here.

**Quick test.** For increasing small \(m\), maximize
\[
\min\{j(P_A),j(P_B)\}
\]
over all partitions. Also solve LP relaxations of the two-cover SAT instance and extract dual weights. Persistent normalized upper bounds or recurring dual obstructions would support this route.

---

## 8. Verdict on difficulty

This is a high-difficulty open problem. Its exact CRT reformulation asks for a factorization of every sufficiently large primorial into two complementary squarefree factors, each having a Jacobsthal gap longer than the prime cutoff. That is a rigid simultaneous strengthening of classical covering-congruence and large-prime-gap constructions.

The one-family covering technology is very strong, but the need to split the prime resource into two disjoint complete covers introduces a genuine critical-density problem. Naive random splitting appears quantitatively inadequate, while known general Jacobsthal upper bounds are far too weak to disprove the assertion.

No standard equivalence to a famous conjecture such as the Riemann hypothesis, Elliott–Halberstam, or a named prime-gap conjecture is known. Nevertheless, any successful proof will likely require either:

- a robust new two-channel version of Erdős–Rankin covering,
- a strong structural theorem for Jacobsthal gaps of complementary primorial factors, or
- an unexpectedly effective combinatorial hypergraph construction.

The source ambiguity must be resolved explicitly in any final claim. The all-real formulation corresponds to interval length \(m\); the integer-only reading corresponds to length \(m-1\). A rigorous research program should test both, but target the stronger all-real/Jacobsthal condition
\[
\min\{j(u),j(v)\}\ge m+1.
\]