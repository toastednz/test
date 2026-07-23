# Problem brief: Erdős Problem #361

## 1. Precise statement

For integers \(N,n\ge 1\), write
\[
[N]:=\{1,2,\dots,N\}.
\]
For a finite set \(S\) of integers, let
\[
\sigma(S):=\sum_{s\in S}s,
\]
with \(\sigma(\varnothing)=0\).

Define
\[
M(N,n):=\max\left\{|A|:\ A\subseteq [N]\ \text{and}\ 
\sigma(S)\ne n\ \text{for every }S\subseteq A\right\}.
\]
Thus elements may be used at most once: this is a **distinct-element subset-sum** problem, not an unrestricted sum problem.

For fixed real \(c>0\), set
\[
N_c(n):=\lfloor cn\rfloor,\qquad M_c(n):=M(N_c(n),n).
\]

The problem asks for the size of \(M_c(n)\) for large \(n\), and asks whether its dependence on \(n\) is arithmetically irregular.

### Standard interpretation

The most standard reading is:

- \(c>0\) is fixed independently of \(n\);
- \(n\to\infty\) through all positive integers;
- one seeks either an exact formula for \(M_c(n)\), or at minimum a sharp asymptotic formula, including any dependence on the arithmetic structure of \(n\).

The phrase “Does this depend on \(n\) in an irregular way?” is not itself formal. Natural formalizations include:

1. Does the limit
   \[
   \lim_{n\to\infty}\frac{M_c(n)}n
   \]
   exist for each fixed \(c\)?
2. If it does not, what are the liminf, limsup, or set of limit points?
3. Is the main term controlled by arithmetic data such as divisibility of \(n\), its least nondivisor, or congruence classes?
4. Is there an eventual exact or quasi-polynomial formula?

These questions should not be conflated: an irregular exact error term may coexist with a regular leading constant.

### Alternative readings

The wording “let \(c>0\) and \(n\) be some large integer” could also allow \(c=c(n)\), but that is substantially different. Unless stated otherwise, \(c\) should be treated as fixed.

Because \(n>0\), it does not matter whether “subset” includes the empty subset. It does matter that repetitions are forbidden.

---

## 2. Immediate reductions and elementary facts

These should be built into any attempted solution.

### 2.1 Elements larger than \(n\) are free

All elements are positive, so no element \(a>n\) can occur in a subset summing to \(n\). Hence
\[
M(N,n)=(N-n)_+ + M(\min(N,n),n),
\]
where \(x_+=\max(x,0)\).

In particular, the substantive range is \(N<n\), equivalently \(0<c<1\). The range \(c\ge 1\) is elementary and already settled.

### 2.2 Exact solution for \(N\ge n-1\)

One has
\[
M(n,n)=M(n-1,n)=\left\lfloor\frac n2\right\rfloor.
\]

Indeed:

- \(n\) itself cannot belong to \(A\);
- for every pair \(\{a,n-a\}\) with \(1\le a<n/2\), at most one member may belong to \(A\);
- these pairs are disjoint.

This gives the upper bound \(\lfloor n/2\rfloor\). Equality is attained by
\[
A=
\begin{cases}
\{(n+1)/2,\dots,n-1\},&n\text{ odd},\\[2mm]
\{n/2,n/2+1,\dots,n-1\},&n\text{ even}.
\end{cases}
\]
Any two distinct elements of these sets have sum greater than \(n\), while no singleton has sum \(n\).

Consequently, for \(N\ge n\),
\[
\boxed{M(N,n)=N-\left\lceil\frac n2\right\rceil.}
\]
Thus for every fixed \(c\ge1\),
\[
\boxed{M_c(n)=\lfloor cn\rfloor-\left\lceil\frac n2\right\rceil.}
\]

The open content is therefore concentrated in \(0<c<1\).

### 2.3 Pair upper bound

Let \(P(N,n)\) be the number of unordered distinct pairs contained in \([N]\) whose sum is \(n\). These pairs are disjoint, and
\[
P(N,n)=
\max\left(
0,\,
\left\lceil\frac n2\right\rceil-\max(1,n-N)
\right).
\]
Therefore
\[
M(N,n)\le N-P(N,n)-\mathbf 1_{N\ge n}.
\]

For \(N<n\), this simplifies to
\[
M(N,n)\le N-P(N,n).
\]
This bound uses only two-element representations and may be far from sharp because representations of \(n\) with three or more distinct summands impose additional constraints.

### 2.4 Basic constructions

Several lower bounds should always be included in comparisons.

#### Divisibility construction

If \(d\ge2\) and \(d\nmid n\), then
\[
A=d\mathbb Z\cap[N]
\]
is admissible. Hence
\[
M(N,n)\ge \left\lfloor\frac Nd\right\rfloor.
\]

Writing
\[
q(n):=\min\{d\ge2:d\nmid n\},
\]
this gives
\[
M(N,n)\ge \left\lfloor\frac{N}{q(n)}\right\rfloor.
\]
For odd \(n\), taking all even numbers gives \(\lfloor N/2\rfloor\).

This is an important possible source of arithmetic irregularity, but variation in this lower bound alone does not prove variation in the true optimum.

#### One-cardinality-window construction

For any integer \(k\ge1\), define
\[
I_k(N,n):=
\left\{a\in[N]:\frac{n}{k+1}<a<\frac nk\right\}.
\]
No subset of \(I_k(N,n)\) sums to \(n\): a subset of at most \(k\) elements has sum \(<n\), while a subset of at least \(k+1\) elements has sum \(>n\). Thus
\[
M(N,n)\ge |I_k(N,n)|,
\]
where
\[
|I_k(N,n)|
=
\max\left(
0,\,
\min\left(N,\left\lceil\frac nk\right\rceil-1\right)
-\left\lfloor\frac{n}{k+1}\right\rfloor
\right).
\]

For every fixed \(0<c<1\), choose \(k\) with
\[
\frac1{k+1}<c\le\frac1k.
\]
Then this construction has positive density:
\[
M_c(n)\ge
\left(c-\frac1{k+1}\right)n+O(1).
\]
Therefore, for every fixed \(c>0\),
\[
M_c(n)=\Theta_c(n).
\]
Merely proving linear order of magnitude does not resolve the problem.

#### Small-total-sum construction

If \(r\le N\) and
\[
\frac{r(r+1)}2<n,
\]
then \([r]\) is admissible. This gives a general \(\asymp\sqrt n\) lower bound, but it is inferior to the linear constructions when \(c>0\) is fixed.

---

## 3. What counts as a solution

The database question is interrogative rather than a single yes/no conjecture. A full solution should provide one of the following, with matching upper and lower bounds.

### Exact resolution

An exact solution would determine \(M(N,n)\), or equivalently \(M_c(n)\), for every fixed \(c>0\) and all sufficiently large \(n\), including floor effects and any arithmetic parameters.

It must contain:

1. an explicit construction \(A\subseteq[\lfloor cn\rfloor]\) of the claimed cardinality;
2. a proof that no subset of \(A\) sums to \(n\);
3. a universal upper bound proving that every larger \(A\) contains a subset summing to \(n\).

### Sharp asymptotic resolution

If “size” is interpreted asymptotically, a satisfactory result should determine
\[
M_c(n)=F(c,n)n+o(n)
\]
or preferably
\[
M_c(n)=F(c,n)n+O_c(1),
\]
where any arithmetic dependence of \(F(c,n)\) is explicitly characterized.

If the leading term is regular, this means proving the existence and value of
\[
\lim_{n\to\infty}\frac{M_c(n)}n.
\]
If it is irregular, a complete answer should at least determine the liminf, limsup, or limit points and identify the arithmetic mechanism causing them.

### What a disproof or counterexample must establish

There is no single asserted conjecture here to disprove. For a proposed formula \(G(N,n)\):

- To disprove an upper bound \(M(N,n)\le G(N,n)\), one must give an explicit \(A\subseteq[N]\) with
  \[
  |A|>G(N,n)
  \]
  and verify by exact subset-sum computation or proof that \(n\notin\Sigma(A)\).
- To disprove a lower bound or claimed exact value, one must certify
  \[
  M(N,n)<G(N,n).
  \]
  Failure to find a construction is not enough; a rigorous upper-bound certificate is required.
- To disprove convergence of \(M_c(n)/n\), one needs two infinite sequences \(n_j,m_j\to\infty\) and a fixed \(\delta>0\) such that proven bounds imply
  \[
  \limsup_j\frac{M_c(n_j)}{n_j}
  \ge
  \liminf_j\frac{M_c(m_j)}{m_j}+\delta.
  \]
  Different lower bounds on two subsequences do not suffice unless matching upper bounds separate the actual optima.

For a finite counterexample involving \(c\), it is cleaner to report \((N,n)\), since \(M_c(n)\) depends on \(c\) only through \(N=\lfloor cn\rfloor\).

---

## 4. What does not count as a solution

The following are meaningful partial results but do not settle the problem:

- solving only \(c\ge1\), which is elementary as above;
- proving only \(M_c(n)=\Theta_c(n)\);
- proving bounds with different positive linear constants;
- treating only prime \(n\), odd \(n\), squarefree \(n\), or a density-one set of integers;
- finding a good modular construction without proving it optimal;
- proving that \(M_c(n)/n\) has different available lower bounds on different subsequences;
- computational verification for finitely many \(n\);
- conditional results depending on unproved inverse-additive or number-theoretic conjectures;
- heuristic random-set thresholds;
- results about unrestricted sums, sums allowing repetition, or sums modulo \(n\);
- proving that a nonempty subset sum is \(0\pmod n\), since that sum may be \(2n,3n,\dots\), not \(n\);
- asymptotic improvements of lower or upper bounds that do not meet;
- a structural theorem with an unclassified exceptional family large enough to contain extremizers.

---

## 5. Known results and context

The supplied database commentary consists only of the word “Previous” and contains no mathematical result to summarize. No claimed prior bound should be inferred from it.

The following established tools are directly relevant.

### 5.1 Distinct partitions and hypergraph transversals

Let
\[
\mathcal P_{N,n}:=
\left\{S\subseteq[N]:\sigma(S)=n\right\}.
\]
Then \(A\) is admissible exactly when it is an independent set in the hypergraph
\[
\mathcal H_{N,n}=([N],\mathcal P_{N,n}).
\]
Equivalently, \(C=[N]\setminus A\) must be a transversal meeting every partition of \(n\) into distinct parts at most \(N\). Thus
\[
M(N,n)=N-\tau(\mathcal H_{N,n}),
\]
where \(\tau\) denotes transversal number.

This reformulation is exact and useful for integer programming, covering arguments, and stability analysis.

### 5.2 Generating-function formulation

For \(A\subseteq[N]\), define
\[
P_A(x):=\prod_{a\in A}(1+x^a).
\]
Then
\[
[x^n]P_A(x)
\]
is exactly the number of subsets of \(A\) summing to \(n\). Hence \(A\) is admissible precisely when
\[
[x^n]P_A(x)=0.
\]

### 5.3 Complete-sequence lemma

If
\[
1=a_1<a_2<\cdots<a_t
\]
and
\[
a_i\le 1+\sum_{j<i}a_j
\quad\text{for every }i\ge2,
\]
then every integer between \(0\) and \(\sum_i a_i\) is a subset sum of \(\{a_1,\dots,a_t\}\).

More generally, variants with an initial interval of represented sums allow one to extend coverage greedily. A promising upper-bound argument may try to extract such a complete core from a dense \(A\).

### 5.4 Restricted sumsets

For a set \(A\) in a finite abelian group, write
\[
h^{\wedge}A
=
\{a_1+\cdots+a_h:\ a_1,\dots,a_h\in A
\text{ distinct}\}.
\]

For \(A\subseteq\mathbb Z/p\mathbb Z\) with \(p\) prime, the Dias da Silva–Hamidoune theorem gives
\[
|h^{\wedge}A|
\ge
\min\{p,\ h|A|-h^2+1\}.
\]

Applied when \(n=p\) is prime and \(N<n\), if
\[
h|A|-h^2+1\ge n
\quad\text{and}\quad
hN<2n,
\]
then \(h^{\wedge}A\) contains \(0\pmod n\), and the corresponding positive integer sum is less than \(2n\); it must therefore equal \(n\). Consequently, an admissible \(A\) must satisfy
\[
|A|<\frac{n+h^2-1}{h}
\]
for every \(h\) satisfying \(hN<2n\).

This illustrates the potential of restricted-sumset methods on prime subsequences. Composite \(n\) introduces subgroup stabilizers, precisely where divisibility constructions can survive.

### 5.5 Inverse additive theory

Freiman-type inverse theorems, Kneser’s theorem, critical-number results for cyclic groups, and structural results on subset sums of dense sets are relevant. Their typical conclusion is that failure of subset-sum coverage forces concentration in a progression or proper subgroup. However, the present problem asks for one exact integer \(n\), not coverage of a whole interval or group, so existing results do not automatically solve it.

### Settled portion

The range \(c\ge1\) is completely settled:
\[
M_c(n)=\lfloor cn\rfloor-\left\lceil\frac n2\right\rceil.
\]
No comparable general formula is supplied for \(0<c<1\).

---

## 6. Traps and edge cases

1. **No repetition.**  
   The representation \(n=(n/2)+(n/2)\) is illegal because \(A\) is a set and a subset cannot use \(n/2\) twice.

2. **Exact equality, not exceeding \(n\).**  
   A subset with sum greater than \(n\) causes no problem.

3. **Integer equality, not congruence.**  
   A zero-sum modulo \(n\) may have sum \(kn\) for \(k\ge2\).

4. **The element \(n\).**  
   If \(N\ge n\), then \(n\notin A\) because \(\{n\}\) is forbidden.

5. **Elements greater than \(n\).**  
   These are always harmless and should always be included in an extremal set.

6. **A large total sum proves nothing by itself.**  
   The implication
   \[
   \sum_{a\in A}a\ge n\Longrightarrow n\in\Sigma(A)
   \]
   is false.

7. **A gcd condition is only one-sided.**  
   If \(\gcd(A)\nmid n\), then \(A\) is admissible. But \(\gcd(A)\mid n\) does not imply that \(n\) is represented.

8. **Pair bounds may not be sharp.**  
   Selecting at most one element from every pair \(\{a,n-a\}\) does not prevent three- or higher-term representations.

9. **Floor effects.**  
   Endpoints in the interval construction must be strict. If \(a=n/k\), then \(k\) copies would sum to \(n\), but copies are unavailable; nevertheless endpoint inclusion can create other representations, so it cannot be added without a separate argument.

10. **Fixed \(c\) versus varying \(c\).**  
    For fixed \(c>0\), \(N\) is linear in \(n\), even if \(c\) is very small. Arguments valid only when \(N=O(\sqrt n)\) do not address this regime.

11. **Irregular constructions do not prove irregular optima.**  
    The quantity \(q(n)\) varies arithmetically, but another regular construction may dominate it for all \(n\).

12. **Prime-modulus theorems do not extend automatically to composite \(n\).**  
    Kneser stabilizers and proper subgroups are genuine obstructions.

---

## 7. Verification hooks

### 7.1 Verify a proposed set

For \(A=\{a_1,\dots,a_t\}\), maintain an \((n+1)\)-bit bitset \(R\):

```text
R = 1                 # only bit 0 set
for a in A:
    R = R OR ((R << a) masked to bits 0,...,n)
valid iff bit n of R is 0
```

This is exact and runs in roughly \(O(|A|n/w)\) machine-word operations.

### 7.2 Exact optimization by integer programming

Introduce binary variables \(x_a\in\{0,1\}\) for \(a\in[N]\). For every distinct-part partition \(S\in\mathcal P_{N,n}\), impose
\[
\sum_{a\in S}x_a\le |S|-1.
\]
Maximize
\[
\sum_{a=1}^N x_a.
\]

The partitions can be enumerated recursively in increasing order, pruning once the partial sum exceeds \(n\). For rigorous upper bounds, preserve an ILP proof log or convert to SAT and retain an unsatisfiability certificate.

### 7.3 Complementary hitting-set formulation

Use variables \(y_a=1-x_a\) and constraints
\[
\sum_{a\in S}y_a\ge1
\qquad(S\in\mathcal P_{N,n}).
\]
Minimize \(\sum_a y_a\). This may be computationally better because pair constraints can be inserted immediately.

### 7.4 Restricted \(h\)-sum checks

For each \(h\), compute
\[
R_h=\left\{\sum_{a\in S}a:\ S\subseteq A,\ |S|=h,\ \sum_{a\in S}a\le n\right\}
\]
using layered bitsets. This identifies which subset cardinalities first force \(n\) and can test restricted-sumset conjectures.

### 7.5 Template classification

For computed extremizers, record:

- \(\gcd(A)\);
- residue-class densities modulo \(d\le D\);
- maximal interval components;
- the smallest represented and omitted sums;
- the distribution of representation sizes of \(n\);
- distance from divisibility templates \(d\mathbb Z\cap[N]\);
- distance from intervals \(I_k(N,n)\).

This can reveal whether optimizers are modular, interval-based, or genuinely mixed.

### 7.6 Search ranges

A useful initial grid is:

- \(20\le n\le200\);
- every \(1\le N<n\), not only selected \(c\);
- primes, odd composites, highly divisible integers, prime powers, and \(n=\operatorname{lcm}(1,\dots,r)\).

Tabulate
\[
\frac{M(N,n)}n,\qquad \frac{M(N,n)}N,
\]
along with the pair bound and all basic constructions.

---

## 8. Attack routes

### Route 1: Inverse theorem for dense sets with a missing target

**Core mechanism.**  
Prove that if \(A\subseteq[cn]\) has positive density and \(n\notin\Sigma(A)\), then \(A\) must be close to one of a small list of structured obstructions: a proper sublattice \(d\mathbb Z\), a short interval separating subset cardinalities, or a bounded union of such objects.

**Key needed lemma.**  
A stability theorem of the form:

> If \(|A|\ge\delta n\) and \(n\notin\Sigma(A)\), then after deleting \(o(n)\) elements, \(A\) lies in a progression or periodic set whose subset sums have a provable obstruction at \(n\).

**Why it might work.**  
Dense sets usually have very rich subset sums. Persistent failure at one central-scale target should require arithmetic or geometric structure.

**Likely failure point.**  
Most inverse theorems require omission of a long interval or failure of global expansion. Omitting a single integer may be too weak to force structure.

**Quick obstruction test.**  
Compute exact extremizers and check whether each is \(o(n)\)-close to a bounded-modulus periodic set or one of the intervals \(I_k\). If extremizers show many unrelated local patterns, a simple classification theorem is unlikely.

---

### Route 2: Restricted sumsets modulo \(n\), followed by lifting

**Core mechanism.**  
Choose a subset cardinality \(h\). Prove that \(h^{\wedge}A\) covers \(0\pmod n\), while ensuring every positive \(h\)-term sum is less than \(2n\). The resulting sum must equal \(n\).

**Key needed lemma.**  
A sharp composite-modulus analogue of the Dias da Silva–Hamidoune bound, with a classification of stabilizer cases:
\[
|h^{\wedge}A|\ \text{large unless }A\text{ is concentrated in cosets of a proper subgroup}.
\]

**Why it might work.**  
It directly respects distinct summands and can turn a density condition into coverage by sums of a fixed number of terms. Subgroup exceptions align with divisibility constructions.

**Likely failure point.**  
For composite \(n\), subgroup stabilizers can be large. Also, if \(hN\ge2n\), residue \(0\) may lift to \(2n\) or more.

**Quick obstruction test.**  
For candidate densities, find integers \(h\) satisfying both
\[
hN<2n
\quad\text{and}\quad
h|A|-h^2+1\ge n
\]
in the prime case. If no such \(h\) exists even at the conjectured threshold, this route cannot by itself prove the desired bound.

---

### Route 3: Extract a complete subset-sum core

**Core mechanism.**  
Order the elements of \(A\), extract a small subset whose subset sums contain an interval, and then add further elements to expand that interval until it contains \(n\).

**Key needed lemma.**  
A robust completeness result such as:

> Every sufficiently large \(A\subseteq[cn]\), unless concentrated in a proper lattice or high interval, contains \(B\subseteq A\) whose subset sums contain an interval \([L,U]\) of length \(\gg n\).

One then needs \(L\le n\le U\).

**Why it might work.**  
The elementary complete-sequence lemma is extremely effective once a short initial interval of sums is available. Dense sets may supply enough small increments to bridge all gaps.

**Likely failure point.**  
An admissible set may deliberately omit small elements, have nontrivial gcd, or produce a long interval of sums located entirely below or above \(n\).

**Quick obstruction test.**  
For computed extremizers, calculate the longest interval contained in \(\Sigma(A)\cap[0,n]\). If the represented sums remain highly fragmented even for large extremizers, a direct completeness argument is blocked.

---

### Route 4: Hypergraph transversal and stability

**Core mechanism.**  
Treat distinct-part partitions of \(n\) with parts at most \(N\) as hyperedges. Prove a lower bound on the size of every transversal and classify near-minimal transversals.

**Key needed lemma.**  
A sharp covering theorem for \(\mathcal H_{N,n}\), possibly using:

- many low-overlap representations of \(n\);
- fractional transversal bounds;
- entropy or container arguments;
- a stability theorem showing that small transversals are periodic or interval-like.

**Why it might work.**  
This formulation addresses the exact target \(n\), rather than replacing it by modular or interval coverage. Pair constraints are simply the first layer of the hypergraph.

**Likely failure point.**  
The hypergraph is highly nonuniform: it contains edges of sizes \(1,2,\dots,\Theta(\sqrt n)\), and vertices near \(n\) occur in far fewer edges than small vertices. Fractional and integral covering numbers may differ substantially.

**Quick obstruction test.**  
Compute the LP relaxation and exact ILP optimum for small instances. A growing integrality gap would show that purely fractional covering arguments are insufficient.

---

### Route 5: Generating functions and analytic positivity

**Core mechanism.**  
Use
\[
P_A(x)=\prod_{a\in A}(1+x^a)
\]
and prove that \([x^n]P_A(x)>0\) once \(|A|\) exceeds a structural threshold.

**Key needed lemma.**  
A uniform lower bound on \([x^n]P_A(x)\) for dense \(A\), except when \(A\) has an explicit root-of-unity or support obstruction.

**Why it might work.**  
For pseudorandom dense \(A\), local central-limit or saddle-point methods should predict many representations of \(n\). Major arcs may isolate precisely the modular obstructions.

**Likely failure point.**  
The theorem must be uniform over adversarial sets \(A\). The coefficient is exactly zero for divisibility constructions, and near-periodic sets can make minor-arc estimates ineffective.

**Quick obstruction test.**  
Compare exact coefficients \([x^n]P_A(x)\) for random dense sets and computed extremizers. If extremizers have clear Fourier concentration at low-order roots of unity, an analytic-plus-inverse approach is plausible.

---

### Route 6: Constructive disproof and arithmetic irregularity

**Core mechanism.**  
Search for new periodic, layered, or mixed constructions that outperform both the divisibility and single-interval constructions along selected arithmetic subsequences of \(n\).

Possible templates include:

- unions of residue classes modulo \(d\);
- several disjoint intervals whose possible subset cardinalities leave a gap at \(n\);
- recursive or mixed-radix constructions;
- a periodic core plus a high interval.

**Key needed lemma.**  
A simple invariant—congruence, subset cardinality, quotient-remainder decomposition, or automaton state—that certifies no subset sum is exactly \(n\).

**Why it might work.**  
The problem explicitly suggests irregular dependence on \(n\). Composite moduli may permit structures more efficient than a single subgroup.

**Likely failure point.**  
With linearly many elements, repeated residue classes usually make all residues attainable. Mixed layers may interact to create \(n\) even when each layer is individually safe.

**Quick obstruction test.**  
Enumerate periodic templates of small modulus and verify them by bitset DP for many multiples and nonmultiples of the modulus. Require a stable linear improvement, not an isolated small-\(n\) anomaly.

---

## 9. Verdict on difficulty

The range \(c\ge1\) is elementary and completely solved. The substantive problem is the phase diagram for
\[
0<c<1.
\]

A mere order-of-magnitude answer is also elementary: \(M_c(n)=\Theta_c(n)\). The difficult task is obtaining the sharp linear constant, determining whether it depends on arithmetic properties of \(n\), and classifying extremal sets.

This appears to be a genuine inverse-additive and restricted-subset-sum problem. The all-\(n\) version is likely substantially harder than prime-modulus variants because proper subgroups and divisibility obstructions are intrinsic, not technical nuisances.

No equivalence to a famous conjecture such as the Riemann hypothesis, Goldbach’s conjecture, or a standard major open conjecture is evident from the statement or supplied commentary. However, a complete exact formula for all \(0<c<1\) and all large \(n\) may require a strong new structural theorem for dense sets with one missing subset sum. A first-order asymptotic phase diagram is a more plausible initial target, but remains a serious open research problem.