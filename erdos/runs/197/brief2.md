# Round-2 Problem Brief: Erdős Problem #197

## 1. Precise statement

### 1.1 Conventions

Take
\[
\mathbb N=\{1,2,3,\dots\},\qquad \mathbb N_0=\{0,1,2,\dots\}.
\]
Using \(\mathbb N_0\) instead is equivalent by the translation \(n\mapsto n+1\), which preserves 3-term arithmetic progressions.

A **permutation of an infinite set** \(A\subseteq\mathbb N\) means a bijection
\[
\pi:\mathbb N_0\to A.
\]
Thus the induced order on \(A\) must have order type \(\omega\); arbitrary countable linear orders are not allowed.

A triple of distinct integers is a **3-term arithmetic progression** if it has the form
\[
(a,a+d,a+2d),\qquad a\in\mathbb N,\ d\in\mathbb N.
\]

A permutation \(\pi\) **avoids monotone 3-term arithmetic progressions** if there are no indices
\[
i<j<k
\]
such that
\[
\pi(i)+\pi(k)=2\pi(j).
\]
Because the entries are distinct, this equation says exactly that
\[
(\pi(i),\pi(j),\pi(k))
\]
is either an increasing or a decreasing 3-term arithmetic progression.

Equivalently, if \(\triangleleft\) denotes the temporal order induced by \(\pi\), then for every numerical progression
\[
a<a+d<a+2d
\]
contained in the set, its midpoint \(a+d\) must occur either before both endpoints or after both endpoints:
\[
a+d\triangleleft a,\ a+d\triangleleft a+2d,
\]
or
\[
a\triangleleft a+d,\ a+2d\triangleleft a+d.
\]

### 1.2 Formal problem

Determine whether there exist disjoint sets \(A_0,A_1\subseteq\mathbb N\) and bijections
\[
\pi_c:\mathbb N_0\to A_c,\qquad c\in\{0,1\},
\]
such that

1. \(A_0\cup A_1=\mathbb N\);
2. for each \(c\in\{0,1\}\), there are no \(i<j<k\) satisfying
   \[
   \pi_c(i)+\pi_c(k)=2\pi_c(j).
   \]

Allowing one part to be finite does not change the question: the other part would be cofinite, and no cofinite subset of \(\mathbb N\) has an avoiding \(\omega\)-enumeration; see §4.2.

### 1.3 Ambiguities to avoid

The standard reading forbids both increasing and decreasing progressions in the permutation. Two alternative readings are not intended:

* If only increasing temporal progressions were forbidden, decreasing progressions would remain legal, and the infinite problem would be different because an \(\omega\)-order cannot simply be reversed.
* If “avoid a 3-AP” meant that the underlying set contained no 3-AP at all, the answer would be negative for every finite number of parts by van der Waerden’s theorem. That interpretation is also inconsistent with the known positive three-set result.

---

## 2. What counts as a solution

### 2.1 Complete affirmative solution

A complete affirmative solution must provide, explicitly or existentially with a rigorous proof:

1. a coloring
   \[
   \chi:\mathbb N\to\{0,1\},
   \]
   with \(A_c=\chi^{-1}(c)\);
2. for each \(c\), an actual \(\omega\)-enumeration
   \[
   \pi_c:\mathbb N_0\to A_c;
   \]
3. a proof that each \(\pi_c\) is bijective, hence in particular:
   * no integer is repeated;
   * every integer of color \(c\) is eventually listed;
4. a proof that for every \(c\), every \(i<j<k\) satisfies
   \[
   \pi_c(i)+\pi_c(k)\ne 2\pi_c(j).
   \]

A recursive or priority construction must prove **fairness/coverage**, not merely that it can append infinitely many safe values.

For the ternary-shell ansatz in §5, it would suffice to prove that every finite shell instance \(\mathcal F_k\) is satisfiable, because the resulting finite shell permutations concatenate to genuine \(\omega\)-enumerations.

### 2.2 Complete negative solution

A complete disproof must establish
\[
\forall \chi:\mathbb N\to\{0,1\},\ 
\forall \pi_0,\pi_1
\]
enumerating the two color classes, at least one \(\pi_c\) contains indices \(i<j<k\) with
\[
\pi_c(i)+\pi_c(k)=2\pi_c(j).
\]

Since the original assertion is existential, exhibiting a particular partition that fails is not a counterexample. Likewise:

* an unsatisfiable ternary or dyadic shell disproves only that shell construction;
* a dead finite prefix disproves only a universal extension principle;
* failure of a proposed digital order disproves only that digital ansatz.

A computational disproof must be accompanied by a rigorous finite reduction covering **all** possible two-color \(\omega\)-orders. Any unsatisfiability claim should ideally be supported by a checkable proof certificate such as DRAT/LRAT, or by a short independently verifiable combinatorial certificate.

---

## 3. What does not count

None of the following resolves the problem:

1. Valid constructions only for \([1,N]\), no matter how large \(N\) is. Every finite set has a one-color avoiding permutation.
2. Arbitrary linear orders on the two color classes unless each induced order has type \(\omega\). Ordinary compactness often produces orders with infinite descending chains or elements with infinitely many predecessors.
3. Infinite injective avoiding sequences that omit infinitely many integers.
4. Proofs that arbitrarily large safe append moves exist. Safe moves need not give coverage.
5. A construction with three colors. That variant is already settled affirmatively.
6. A proof for a density-one subset, a cofinite modification, or all sufficiently large integers unless the omitted integers are rigorously integrated.
7. Conditional results depending on an unproved shell lemma, bounded-rank conjecture, SAT pattern, or famous conjecture.
8. Satisfiability of finitely many shell instances without a theorem reducing all shells to those cases.
9. An unsatisfiable shell instance presented as a disproof of the original problem.
10. Avoidance only of increasing progressions while allowing decreasing ones.
11. Heuristic evidence from random permutations, asymptotic counts of constraints, or solver runtimes.
12. A finite-coloring result in which each class merely avoids infinite arithmetic progressions. Finite 3-APs still impose ordering constraints.

---

## 4. Known results and context

## 4.1 Every finite set has an avoiding permutation

**Finite parity lemma.** Every finite set \(S\subseteq\mathbb Z\) admits a permutation avoiding monotone 3-term arithmetic progressions.

A standard proof recursively separates the odd and even elements. If the common difference \(d\) of a 3-AP is odd, its endpoints have one parity and its midpoint the other, so placing parity classes contiguously puts the midpoint before both endpoints or after both. If \(d\) is even, all three terms have the same parity and the assertion reduces, after dividing by \(2\), to a smaller finite instance.

This proves that all finite initial-segment versions are trivially satisfiable, even with one color. The obstruction is entirely the requirement of a covering order of type \(\omega\).

## 4.2 One color, and every cofinite set, are impossible

**Theorem.** No cofinite \(S\subseteq\mathbb N\) has an avoiding \(\omega\)-enumeration.

Proof sketch: let \(x\) be the first listed element. Choose \(d\) large enough that
\[
x+2^m d\in S\qquad\text{for every }m\ge 0.
\]
For every \(m\), the progression
\[
x,\quad x+2^m d,\quad x+2^{m+1}d
\]
has \(x\) first. To avoid it, the largest term must occur before the midpoint:
\[
\operatorname{pos}(x+2^{m+1}d)
<
\operatorname{pos}(x+2^m d).
\]
This gives an infinite strictly decreasing sequence of nonnegative positions, impossible.

Consequences:

* \(\mathbb N\) itself has no avoiding permutation.
* Any affirmative two-color solution must have both parts infinite.
* More generally, neither color class may contain an infinite affine copy
  \[
  \{a+dn:n\in\mathbb N_0\}
  \]
  of \(\mathbb N_0\), since restricting an \(\omega\)-order to that subset would give a forbidden one-color enumeration.

This immediately kills valuation colorings such as \(v_2(n)\bmod 2\): the odd numbers alone form the affine copy \(2n+1\).

## 4.3 Three colors are sufficient

The three-color variant is settled affirmatively.

An explicit scale-separated construction is as follows. Let
\[
q=\frac32,\qquad a_k=\left\lceil q^k\right\rceil,
\]
and define finite consecutive blocks
\[
B_k=[a_k,a_{k+1}-1]\cap\mathbb N.
\]
Color \(B_k\) by \(k\bmod 3\). For each color, enumerate its blocks in increasing \(k\), using the finite parity lemma inside each block.

If \(k\ge 3\), the previous block of the same color ends at \(a_{k-2}-1\). The inequalities
\[
a_k>2(a_{k-2}-1)
\]
and
\[
(a_{k+1}-1)+(a_{k-2}-1)<2a_k
\]
follow from
\[
q^2=\frac94>2,\qquad q+q^{-2}=\frac{35}{18}<2.
\]
They exclude both possible kinds of cross-block 3-AP:

* two smaller terms in old blocks and the largest in \(B_k\);
* the smallest term in an old block and the midpoint and largest term in \(B_k\).

Thus every monochromatic 3-AP lies in a single finite block and is handled internally.

Hence the minimum number of colors is known to be either \(2\) or \(3\).

## 4.4 Exact block-concatenation criterion

Suppose one color class is divided into finite value intervals
\[
B_0<B_1<B_2<\cdots
\]
and the block permutations are concatenated in this order. Let \(x<y<z\) be a numerical 3-AP.

* If \(x,y,z\) lie in three distinct blocks, then their temporal order is automatically \(x,y,z\), so the construction fails.
* If \(x,y\in B_r\) and \(z\in B_s\) with \(r<s\), then the internal order must put
  \[
  y\triangleleft x.
  \]
* If \(x\in B_r\) and \(y,z\in B_s\) with \(r<s\), then the internal order must put
  \[
  z\triangleleft y.
  \]
* If all three lie in one block, the block permutation must handle them internally.

These conditions are necessary and sufficient.

A previous round also proved that for any decomposition of \(\mathbb N\) into consecutive nonempty finite intervals colored alternately with two colors, some monochromatic 3-AP necessarily crosses block boundaries. Thus a two-state interval construction cannot simply arrange that every monochromatic progression is internal. Cross-block precedence constraints must be solved.

## 4.5 Digital constructions: what has been ruled out

Several natural digital constructions are now known to fail.

1. **Full dyadic-cylinder contiguity.** Least-significant-bit or parity-recursive orders avoid 3-APs locally, but their infinite limits generally have descending chains. Preserving full dyadic cylinder contiguity is incompatible with making every color restriction an \(\omega\)-order under any finite coloring.

2. **Valuation coloring.** Coloring by \(v_2(n)\bmod 2\) fails because a color contains an affine copy of all nonnegative integers.

3. **Naive parity recursion in shells.** Alternating dyadic shells remain a viable ansatz, but the natural parity-recursive candidate already violates the exact shell constraints on \([16,31]\). This does not prove that the shell instance is unsatisfiable; it proves only that the obvious parity induction cannot establish it.

4. A stronger dyadic “boundary lemma” was verified through shell size \(8\), but no proof or finite-state recursion is known. It should not be treated as established for general shells.

## 4.6 Append-only and priority constructions: exact obstructions

For a finite avoiding sequence
\[
P=(p_0,\dots,p_{m-1}),
\]
define its append-forbidden set
\[
F(P)=\{2p_j-p_i:0\le i<j<m\}\cap\mathbb N.
\]
A new unused value \(x\) can be appended to \(P\) if and only if
\[
x\notin F(P).
\]
These forbidden sets are monotone: appending more elements can only enlarge them.

For two frozen prefixes \(P_0,P_1\), an unused value in
\[
F(P_0)\cap F(P_1)
\]
can never be appended to either side. Thus absence of such a collision is necessary for a covering continuation, but it is not sufficient.

The explicit prefixes
\[
P_0=(5,20),\qquad P_1=(2,6,7,11)
\]
are disjoint, avoiding, and collision-free, yet have no covering append-only continuation. Their initial forbidden sets are
\[
F(P_0)=\{35\},
\]
and
\[
F(P_1)=\{8,10,12,15,16,20\}.
\]
Moreover, an affine copy of this dead gadget can be appended safely after any finite collision-free state. Therefore:

* there is no universal extension theorem from every locally safe state;
* collision-freeness is not an adequate invariant;
* no uniformly bounded terminal-repair or bounded-injury lemma can work;
* appending arbitrarily large safe reservoir elements does not solve coverage;
* insertion can fail even for a new numerical maximum.

Frozen prefixes also impose directed precedence edges on future same-color elements. A directed cycle in this forced-precedence graph is an absolute obstruction. Any future priority construction must preserve a much stronger global well-foundedness invariant.

## 4.7 Exact bounded-predecessor compactness criterion

For a finite valid coloring and ordering of \([1,N]\), let
\[
\operatorname{pred}_N(n)
\]
be the number of same-color elements preceding \(n\).

The original problem is equivalent to the existence of a function
\[
b:\mathbb N\to\mathbb N_0
\]
such that for every \(N\) there is a valid two-colored ordering of \([1,N]\) satisfying
\[
\operatorname{pred}_N(n)\le b(n)\qquad(1\le n\le N).
\]

* An infinite solution gives such a \(b\) by taking the actual rank of each integer in its color sequence.
* Conversely, coordinatewise bounded predecessor counts allow a diagonal limit in which every element has finitely many predecessors, hence each infinite color order has type \(\omega\).

Ordinary compactness does not provide these bounds. The one-color finite instances are all satisfiable, although the infinite one-color problem is impossible. In compactness limits, ranks can escape to infinity. The canonical parity-recursive compactness order also contains descending chains in every finite induced coloring.

---

## 5. The exact ternary-shell finite family

This is the highest-priority concrete reduction from Round 1.

## 5.1 Fixed coloring and block order

For \(k\ge 0\), define the ternary shell
\[
I_k=\{n\in\mathbb N:3^k\le n\le 3^{k+1}-1\}.
\]
Thus, writing
\[
M=3^k,
\]
we have
\[
I_k=[M,3M-1],\qquad |I_k|=2M.
\]

Color all of \(I_k\) by
\[
k\bmod 2.
\]
For each color, concatenate its shells in increasing shell index. The only remaining freedom is the permutation chosen inside each \(I_k\).

Define the earlier same-colored set
\[
U_k=\bigcup_{\substack{0\le j\le k-2\\j\equiv k\pmod 2}} I_j.
\]
Equivalently,
\[
U_k=I_{k-2}\cup I_{k-4}\cup\cdots,
\]
with \(U_0=U_1=\varnothing\).

## 5.2 Why the shell problems are independent

Let
\[
a<b<c,\qquad a+c=2b
\]
be a monochromatic 3-AP, and suppose \(c\in I_k\) where \(k\) is maximal.

If \(b\) were in an earlier same-colored shell, then
\[
b\le 3^{k-1}-1,
\]
and hence
\[
c=2b-a<2\cdot 3^{k-1}<3^k,
\]
contradicting \(c\in I_k\).

Therefore \(b,c\in I_k\). There are only two cases:

1. \(a,b,c\in I_k\): this is an internal shell constraint.
2. \(a\in U_k\) and \(b,c\in I_k\): since \(a\) occurs before the entire shell \(I_k\), the order \(a,b,c\) is forbidden exactly when \(b\) occurs before \(c\). Therefore one must impose
   \[
   c\triangleleft b.
   \]

Crucially, this constraint depends only on the numerical set \(U_k\), not on the permutations of earlier shells. Hence the shell instances are independent.

## 5.3 Formal shell instance \(\mathcal F_k\)

Let
\[
X_k=I_k=[M,3M-1],\qquad M=3^k.
\]

The task is to find a bijection
\[
\sigma_k:\{0,1,\dots,2M-1\}\to X_k.
\]
Let
\[
p_k(v)=\sigma_k^{-1}(v)
\]
be the position of \(v\).

### Internal non-betweenness constraints

For every
\[
a\in[M,3M-1],\qquad d\in\mathbb N,
\]
such that
\[
a+2d\le 3M-1,
\]
set
\[
b=a+d,\qquad c=a+2d.
\]
Require
\[
\bigl(p_k(b)<p_k(a)\ \wedge\ p_k(b)<p_k(c)\bigr)
\]
or
\[
\bigl(p_k(a)<p_k(b)\ \wedge\ p_k(c)<p_k(b)\bigr).
\]
Equivalently,
\[
p_k(b)\notin
\bigl(\min\{p_k(a),p_k(c)\},
      \max\{p_k(a),p_k(c)\}\bigr).
\]

### Incoming precedence constraints

For every \(y,z\in X_k\) with \(y<z\), let
\[
x=2y-z.
\]
If
\[
x\in U_k,
\]
require
\[
p_k(z)<p_k(y).
\]

Equivalently, the fixed incoming edge set is
\[
E_k=\{(z,y)\in X_k^2:y<z,\ 2y-z\in U_k\},
\]
where \((z,y)\) denotes the required precedence \(z\triangleleft y\).

### Exact equivalence for this ansatz

The alternating ternary-shell construction gives a positive solution to the original problem if and only if \(\mathcal F_k\) is satisfiable for every \(k\ge0\).

This is an equivalence only for the fixed ternary-shell ansatz, not for the original problem as a whole.

## 5.4 Geometry and exact parameters

For \(k\ge2\),
\[
\max U_k=3^{k-1}-1=\frac M3-1.
\]
If \((z,y)\in E_k\), then
\[
y\le \left\lfloor\frac{3M-1+(M/3-1)}2\right\rfloor
=\frac{5M}{3}-1,
\]
and
\[
z=2y-x\ge 2M-\left(\frac M3-1\right)
=\frac{5M}{3}+1.
\]

Thus every fixed edge points from
\[
\left[\frac{5M}{3}+1,3M-1\right]
\]
to
\[
\left[M,\frac{5M}{3}-1\right].
\]
The central value \(5M/3\) is incident with no incoming edge. In particular, the fixed precedence graph \(E_k\) is itself acyclic; any unsatisfiability must come from interaction with internal 3-AP constraints.

The number of internal 3-APs is
\[
\sum_{d=1}^{M-1}(2M-2d)=M(M-1).
\]

Also,
\[
|U_k|=
\begin{cases}
(M-1)/4,& k\text{ even},\\[2mm]
(M-3)/4,& k\text{ odd}.
\end{cases}
\]

The exact number of incoming edges is
\[
|E_k|
=
\sum_{x\in U_k}
\left(
\left\lfloor\frac{M-1+x}{2}\right\rfloor+1
\right).
\]

### Initial instances

| \(k\) | \(M=3^k\) | Shell \(X_k\) | \(|X_k|\) | \(U_k\) | Internal 3-APs | Incoming edges |
|---:|---:|---|---:|---|---:|---:|
| 0 | 1 | \([1,2]\) | 2 | \(\varnothing\) | 0 | 0 |
| 1 | 3 | \([3,8]\) | 6 | \(\varnothing\) | 6 | 0 |
| 2 | 9 | \([9,26]\) | 18 | \([1,2]\) | 72 | 11 |
| 3 | 27 | \([27,80]\) | 54 | \([3,8]\) | 702 | 99 |
| 4 | 81 | \([81,242]\) | 162 | \([1,2]\cup[9,26]\) | 6,480 | 974 |
| 5 | 243 | \([243,728]\) | 486 | \([3,8]\cup[27,80]\) | 58,806 | 8,766 |
| 6 | 729 | \([729,2186]\) | 1,458 | \([1,2]\cup[9,26]\cup[81,242]\) | 530,712 | 79,625 |
| 7 | 2,187 | \([2187,6560]\) | 4,374 | \([3,8]\cup[27,80]\cup[243,728]\) | 4,780,782 | 716,625 |

The cases \(k=0,1\) are automatically satisfiable by the finite parity lemma. Explicit witnesses are
\[
(1,2)
\]
and, for \(I_1=[3,8]\),
\[
(3,7,5,6,4,8).
\]
No reduction of all higher \(k\) to finitely many base cases is currently known.

## 5.5 Solver-ready formulations

### CP formulation with positions

Create integer variables
\[
p_v\in\{0,\dots,2M-1\},\qquad v\in X_k,
\]
and impose `AllDifferent(p_v)`.

For each \((z,y)\in E_k\), impose
\[
p_z<p_y.
\]

For each internal progression \((a,b,c)\), impose
\[
(p_b<p_a\wedge p_b<p_c)
\ \vee\
(p_a<p_b\wedge p_c<p_b).
\]

A returned model can be verified independently by sorting the vertices by \(p_v\).

### Acyclic-orientation formulation

For each internal progression \((a,b,c)\), choose one of two states:

* midpoint first: add arcs \(b\to a\) and \(b\to c\);
* midpoint last: add arcs \(a\to b\) and \(c\to b\).

Also add all fixed arcs \(z\to y\) from \(E_k\). The shell is satisfiable if and only if the progression states can be chosen so that the resulting directed graph is acyclic. Any topological ordering is then a valid shell permutation.

This formulation is particularly useful for extracting minimal directed-cycle obstructions or for lazy SAT solving with cycle clauses.

---

## 6. Traps and edge cases

1. **Order type matters.** An AP-avoiding countable linear order with descending chains is not a permutation indexed by \(\mathbb N_0\).
2. **One cannot reverse an infinite permutation.** Reversal of a finite avoiding order is harmless; there is no analogous reversal of an \(\omega\)-enumeration.
3. **Finite compactness is insufficient.** Every finite one-color instance is satisfiable.
4. **Coverage is not automatic.** Infinite safe append sequences may starve some integers forever.
5. **Forbidden append sets only grow.** Adding auxiliary values cannot make a currently forbidden target appendable.
6. **Collision-freeness is only necessary.** The dead-prefix gadget is collision-free but nonextendible.
7. **Incoming shell edge direction is \(z\triangleleft y\), not \(y\triangleleft z\).** The old smallest term is already before the shell.
8. **Use only earlier same-colored shells.** In \(\mathcal F_k\), \(2y-z\) must lie in \(U_k\), not merely anywhere below \(M/3\).
9. **The shell endpoints are inclusive.** \(I_k=[3^k,3^{k+1}-1]\), of size \(2\cdot3^k\).
10. **For \(k=0,1\), \(U_k=\varnothing\).** Do not interpret negative-index shells.
11. **Acyclicity of \(E_k\) alone is irrelevant.** Internal AP constraints are disjunctive and can create cycles after orientation.
12. **AllDifferent can be omitted only in the acyclic-height model.** Tied heights are then merely a certificate of a DAG and must be refined by a topological sort.
13. **Finite shell satisfiability is not a finite proof of the infinite theorem.** Uniformity in \(k\) is essential.
14. **An unsatisfiable shell kills only the fixed shell coloring.**
15. **Positive density does not by itself settle orderability.** Van der Waerden and Szemerédi give finite progressions, while finite progression sets can be ordered safely.
16. **Affine copies are dangerous.** If a color contains a full infinite arithmetic progression, it is immediately nonorderable.
17. **The failure at the dyadic shell \([16,31]\)** concerns the natural parity-recursive candidate, not the existence of some other valid shell order.

---

## 7. Verification hooks

## 7.1 Exact ternary-shell generator

For shell \(k\):

```text
M = 3^k
X = {M, M+1, ..., 3M-1}

U = empty
for j = 0,...,k-2:
    if j ≡ k (mod 2):
        add {3^j,...,3^(j+1)-1} to U

InternalAPs = empty
for d = 1,...,M-1:
    for a = M,...,3M-1-2d:
        add (a, a+d, a+2d)

IncomingEdges = empty
for y in X:
    for z in {y+1,...,3M-1}:
        if 2y-z in U:
            add edge z -> y
```

Sanity checks:

* `len(X) = 2*M`;
* `len(InternalAPs) = M*(M-1)`;
* every incoming edge satisfies
  \[
  y\le 5M/3-1,\qquad z\ge 5M/3+1;
  \]
* the edge counts match the table in §5.4.

Run exact instances in the order
\[
k=2,3,4,5,6,
\]
then \(k=7\) if feasible. An unsatisfiable result should be converted to a checkable certificate.

## 7.2 Witness checker

Given a proposed shell permutation \(\sigma\):

1. verify that it contains every integer in \(X_k\) exactly once;
2. compute inverse positions \(p_v\);
3. verify \(p_z<p_y\) for every \((z,y)\in E_k\);
4. for every internal \((a,b,c)\), verify
   \[
   p_b<\min(p_a,p_c)
   \quad\text{or}\quad
   p_b>\max(p_a,p_c).
   \]

This checker should be completely independent of the solver.

## 7.3 Minimal obstruction extraction

In the orientation formulation:

1. select source/sink states for internal progressions;
2. detect a directed cycle;
3. add a clause forbidding that exact combination of progression states;
4. repeat.

If unsatisfiable, extract a minimal set of incoming edges and internal progressions forcing cyclicity. Record the numerical values and normalize them by translation/scaling where possible.

A small core at one shell would be more informative than a bare UNSAT result.

## 7.4 Dyadic comparison tests

For the dyadic shell
\[
D_k=[2^k,2^{k+1}-1],
\]
use the analogous earlier same-parity shell union and the same incoming-edge rule. Run exact CP-SAT for
\[
M=16,32,64.
\]
Distinguish carefully between:

* exact shell satisfiability;
* satisfiability under the stronger boundary state;
* satisfiability inside the parity-recursive subclass.

Only the last is known to fail at \(M=16\).

## 7.5 Append-prefix checks

For a finite prefix \(P\), compute
\[
F(P)=\{2p_j-p_i:i<j\}\cap\mathbb N.
\]
For the dead gadget verify
\[
F(5,20)=\{35\},
\]
and
\[
F(2,6,7,11)=\{8,10,12,15,16,20\}.
\]

A program exploring continuations must treat forbidden sets as permanent and must distinguish:

* extending safely for a fixed number of steps;
* covering a fixed target interval;
* obtaining a genuine covering continuation.

## 7.6 Bounded-rank optimization

For finite valid two-color orders on \([1,N]\), define
\[
R_m(N)=
\min
\max_{1\le n\le m}\operatorname{pred}_N(n).
\]
If for some fixed \(m\),
\[
R_m(N)\to\infty
\]
along a sequence of \(N\), then the original problem has a negative answer: any infinite solution would give a uniform finite bound on the predecessors of the fixed integers \(1,\dots,m\).

Compute \(R_m(N)\) for fixed
\[
m=1,2,4,8,16
\]
and increasing \(N\). Plateauing does not prove a positive answer, but sustained certified growth would identify a concrete disproof target.

---

## 8. Four new attack routes

## Route 1: Finite-state substitution for the ternary shells

### Core mechanism

Exploit the exact self-similarity under multiplication by \(3\). The shell
\[
I_{k+1}=[3M,9M-1]
\]
splits into the three residue classes
\[
\{3q+r:q\in I_k\},\qquad r=0,1,2,
\]
each an affine copy of \(I_k\). The incoming-edge geometry also has a scale-invariant cut at \(5M/3\).

Do not insist on one parity-recursive order. Instead, search for a finite library of boundary states and AP-safe shuffle templates that allow the three residue children to interleave.

### Required key lemma

There exists a finite set of states \(\mathcal S\) and a finite collection of substitution templates such that:

1. each state specifies exactly the boundary precedence information needed by a shell;
2. every shell in a state can be constructed from smaller-shell witnesses in states from \(\mathcal S\);
3. the construction handles all cross-residue internal 3-APs and all incoming edges;
4. the state transition closes on \(\mathcal S\);
5. finitely many explicitly listed base shells realize all initial states.

This would reduce the infinite theorem to finite checking.

### Why it might work

The obstruction to the naive parity induction was not shell unsatisfiability, but insufficient boundary-state flexibility. The fixed edges occupy only the normalized upper-to-lower region
\[
z>5M/3>y,
\]
and the scale is exactly ternary. A finite collection of low/middle/high shuffle types may capture all interactions.

### Most likely failure

Cross-residue APs may require boundary information of unbounded complexity, so that the number of necessary states grows with \(k\). A finite template library might fail even though every individual shell remains satisfiable.

### Quick blocking test

Solve \(k=2,\dots,6\), then:

1. project each witness to its residue word modulo \(3\);
2. record relative orders induced on the three affine children;
3. canonicalize boundary signatures at the cuts
   \[
   M,\quad 4M/3,\quad 5M/3,\quad 2M,\quad 7M/3,\quad 8M/3,\quad 3M;
   \]
4. test whether a fixed small library of signatures reproduces all larger witnesses.

If every witness requires a new signature, this route is likely blocked. If a stable library appears, formalize the substitution and list all base states explicitly.

---

## Route 2: Source/sink orientation and minimal-cycle descent

### Core mechanism

Use the exact acyclic-orientation reformulation. For each internal 3-AP \((a,b,c)\), choose either

* \(b\) before both endpoints, or
* \(b\) after both endpoints.

Together with incoming edges, this produces a directed graph. The shell is feasible exactly when the orientations can be chosen acyclically.

Study minimal unavoidable directed cycles rather than permutations.

### Required key lemma

For every \(k\), there is a choice of source/sink orientations for the internal APs of \(I_k\) such that the resulting graph with \(E_k\) is acyclic.

A particularly useful proof would show:

> Every minimal purported obstruction admits an arithmetic projection, reflection, or cycle-shortening operation producing a strictly smaller obstruction.

This would give an infinite descent.

### Why it might work

All fixed edges point strictly from the upper region to the lower region. Hence any directed cycle must return upward through selected internal-AP arcs. The arithmetic equalities defining those arcs may force a smaller normalized cycle under
\[
n\mapsto \left\lfloor n/3\right\rfloor
\]
or under reflection about an AP midpoint.

This attacks the exact combinatorial obstruction instead of trying to guess a total order.

### Most likely failure

General non-betweenness CSPs are highly nonlocal. Different APs can share vertices in ways that create unavoidable alternating cycles with no scale-reducing projection. A minimal obstruction may use all residue classes essentially.

### Quick blocking test

Implement lazy cycle-clause SAT for \(k=2,3,4,5\). For every generated cycle:

1. record which arcs are fixed and which depend on progression choices;
2. minimize the cycle/core;
3. classify values by residue modulo \(3\);
4. check whether the core projects to a valid smaller-shell core.

A small UNSAT core kills the ternary-shell route. Persistent SAT with cycle cores exhibiting a uniform reducible pattern strongly supports the descent lemma.

---

## Route 3: Compress the known three-color construction to two tracks

### Core mechanism

Start from the explicit three-color \(3/2\)-scale block construction rather than from alternating ternary shells. Keep one of the three classes as the first final color and try to merge the other two classes into a single avoiding \(\omega\)-order.

More flexibly, relabel the narrow blocks by two colors using a finite-state schedule and allow a nontrivial interleaving of the blocks within each final color.

### Required key lemma

A **two-track merge lemma** of the following form:

> The union of two adjacent classes in the \(3/2\)-scale three-color construction admits an avoiding \(\omega\)-enumeration, with each block acquiring only finitely many predecessor obligations from earlier blocks and with a uniform finite-state scheduling rule.

Alternatively, prove that a finite-state binary relabeling of the \(3/2\)-blocks makes both block-interaction CSPs uniformly solvable.

### Why it might work

The three-color construction already eliminates all same-class cross-block progressions. The third color acts as a scale buffer. Merging two tracks preserves substantial separation and may leave a block-interaction graph of bounded or finite-state complexity. This directly investigates the precise role of the third state rather than repeating the failed two-state interval isolation argument.

The growing omitted blocks also prevent either merged class from trivially containing an infinite arithmetic progression.

### Most likely failure

After merging, an old smallest term can interact with a midpoint and largest term in much later adjacent blocks. Thus block interactions may not actually have bounded range. The resulting union may reproduce the original long-memory precedence problem in a less transparent form.

### Quick blocking test

For the first \(K\) blocks, with \(K=12,18,24,30\):

1. build every monochromatic cross-block AP constraint after merging two of the three classes;
2. solve for internal block orders and an allowed block schedule;
3. impose tentative bounded-predecessor or finite-state scheduling restrictions;
4. monitor the ranks of the first few blocks as \(K\) grows.

Early forced cycles or systematic rank escape block the simple merge. Stable periodic scheduling signatures would justify a formal two-track merge theorem.

---

## Route 4: Disproof through fixed-anchor rank escape

### Core mechanism

Exploit the exact bounded-predecessor criterion. Ordinary rank escape may drift to larger and larger integers and therefore says nothing. A negative solution would follow if rank escape can be forced on a **fixed finite anchor set**.

Use dead-prefix gadgets, affine recurrence, and finite Ramsey/van der Waerden structure to try to force one of a fixed collection of small integers to acquire arbitrarily many predecessors.

### Required key lemma

Prove that there exists a fixed \(m\) such that
\[
R_m(N)\to\infty,
\]
where
\[
R_m(N)=
\min_{\text{valid two-color orders on }[1,N]}
\max_{1\le n\le m}\operatorname{pred}_N(n).
\]

A stronger combinatorial formulation would be:

> For every \(B\), sufficiently large finite valid instances force some \(n\in\{1,\dots,m\}\) to have more than \(B\) same-color predecessors.

This immediately contradicts an infinite solution.

### Why it might work

The dead-prefix gadget shows that local precedence cycles can be reproduced affinely at arbitrary scales. If sufficiently many affine gadgets can be made to feed obligations back toward a fixed set of anchors, the omega-order condition may force unbounded anchor ranks. This is precisely the strengthening missing from ordinary compactness arguments.

### Most likely failure

Rank escape may be intrinsically mobile: every fixed finite set may retain bounded rank while the burden moves to newly introduced integers. This is exactly the mechanism by which compactness can fail without yielding a fixed-coordinate contradiction. The affine dead gadget is installable by an adversary but need not be forced in an arbitrary solution.

### Quick blocking test

Use CP-SAT to compute or lower-bound \(R_m(N)\) for fixed small \(m\) and increasing \(N\). Extract dual or UNSAT certificates for bounds
\[
\operatorname{pred}_N(n)\le B\qquad(n\le m).
\]
If \(R_m(N)\) stabilizes for every tested fixed \(m\), abandon fixed-anchor disproof unless a new forcing theorem is found. If it grows, inspect the certificates for repeated affine dead-gadget structure and turn that pattern into a proof.

---

## 9. Recommended Round-2 execution order

1. **Generate and solve the exact ternary instances \(k=2,3,4,5,6\).**
2. If some instance is UNSAT, extract a minimal certified obstruction. This kills only the ternary ansatz but is the highest-value negative information.
3. If all are SAT, mine witnesses simultaneously for:
   * residue-mod-\(3\) substitution patterns;
   * low/middle/high boundary states;
   * source/sink orientation rules;
   * bounded numbers of canonical shell signatures.
4. In parallel, run the exact dyadic tests \(M=16,32,64\), carefully separating exact feasibility from the failed parity-recursive subclass.
5. Run fixed-anchor rank optimization only as a targeted disproof experiment, not as a replacement for the shell computation.
6. Do not return to universal append-only extension, collision-freeness, or ordinary compactness without a genuinely new global well-foundedness invariant.

---

## 10. Verdict on difficulty

This is a genuine open threshold problem. The one-color case is impossible, while three colors suffice by an elementary scale-separated construction; the entire difficulty is compressing three states to two while retaining two genuine \(\omega\)-orders.

No equivalence to a standard famous conjecture is currently known. Van der Waerden’s theorem, finite parity recursion, and compactness explain parts of the landscape but do not settle the order-type obstruction.

The most concrete present bottleneck is the fully explicit family \(\mathcal F_k\) of finite ternary-shell non-betweenness problems. It is computationally accessible for several nontrivial scales, and a finite-state substitution theorem would solve the original problem. Conversely, an unsatisfiable shell would decisively terminate the strongest current constructive ansatz, though not the original problem.

The problem should be regarded as difficult: several broad methods fail for structural, now-proved reasons rather than for lack of technical polishing. The next high-value progress is therefore either a certified shell obstruction or a genuinely uniform finite-state shell theorem.