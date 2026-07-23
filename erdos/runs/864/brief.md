# Problem brief: Erdős Problem #864

## 1. Precise statement

For a positive integer \(N\), write
\[
[N]:=\{1,2,\dots,N\}.
\]
For \(A\subseteq[N]\) and \(n\in\mathbb Z\), define the unordered representation function
\[
r_A(n):=\bigl|\{(a,b)\in A^2:a\le b,\ a+b=n\}\bigr|.
\]
Thus diagonal representations \(n=2a\) are allowed and counted once.

Call \(A\) **admissible** if
\[
\bigl|\{n\in\mathbb Z:r_A(n)\ge 2\}\bigr|\le 1.
\]
Since \(A\subseteq[N]\), only \(2\le n\le 2N\) can have \(r_A(n)>0\).

Define the extremal function
\[
F(N):=\max\{|A|:A\subseteq[N]\text{ is admissible}\}.
\]

The principal conjecture is
\[
F(N)\le \left(\frac{2}{\sqrt3}+o(1)\right)\sqrt N,
\]
equivalently,
\[
\limsup_{N\to\infty}\frac{F(N)}{\sqrt N}\le \frac{2}{\sqrt3}.
\]
In fully quantified form: for every \(\varepsilon>0\), there is \(N_0(\varepsilon)\) such that for every \(N\ge N_0(\varepsilon)\) and every admissible \(A\subseteq[N]\),
\[
|A|\le \left(\frac{2}{\sqrt3}+\varepsilon\right)\sqrt N.
\]

The known construction gives the reverse asymptotic inequality, so the conjecture is equivalent to
\[
F(N)=\left(\frac{2}{\sqrt3}+o(1)\right)\sqrt N.
\]

### Terminological caution

A **genuine Sidon set** \(B\) here means a set satisfying
\[
r_B(n)\le 1\qquad\text{for every }n,
\]
including sums with equal summands. This is stronger than some conventions for “weak Sidon set.”

The database wording is not meaningfully ambiguous because it explicitly requires \(a\le b\). Without that condition, ordered pairs \((a,b)\) and \((b,a)\) would create artificial multiplicities.

---

## 2. What counts as a solution

### Complete proof of the conjectured estimate

It is enough to prove that for every admissible \(A\subseteq[N]\),
\[
|A|\le \left(\frac{2}{\sqrt3}+o(1)\right)\sqrt N,
\]
where the \(o(1)\) is uniform over all admissible \(A\).

Combined with the Erdős–Freud construction below, this establishes
\[
F(N)=\left(\frac{2}{\sqrt3}+o(1)\right)\sqrt N.
\]

A stronger explicit estimate such as
\[
|A|\le \frac{2}{\sqrt3}\sqrt N+O(N^\theta)
\qquad (\theta<1/2)
\]
would also solve the problem.

### Complete disproof of the proposed upper bound

To disprove the asymptotic upper bound, one must establish
\[
\limsup_{N\to\infty}\frac{F(N)}{\sqrt N}>\frac{2}{\sqrt3}.
\]
Concretely, it suffices to produce:

- a constant \(\varepsilon>0\);
- an unbounded sequence \(N_j\to\infty\);
- sets \(A_j\subseteq[N_j]\);

such that
\[
\left|\{n:r_{A_j}(n)\ge2\}\right|\le1
\]
and
\[
|A_j|\ge\left(\frac{2}{\sqrt3}+\varepsilon\right)\sqrt{N_j}
\]
for every \(j\).

For an explicit construction, admissibility can be verified by computing all \(\binom{|A_j|+1}{2}\) unordered pair sums and checking that at most one integer occurs more than once.

A single large finite example does **not** disprove an asymptotic statement. Nor does a family satisfying
\[
|A_j|=\frac{2}{\sqrt3}\sqrt{N_j}+o(\sqrt{N_j})
\]
even if it is always slightly larger than \(\frac{2}{\sqrt3}\sqrt{N_j}\).

### A complete estimate different from the conjecture

If the conjectured constant is false, a full resolution of the broader request “estimate the maximal possible size” would require identifying the correct leading asymptotic, or at least determining the relevant limsup and liminf. Merely disproving the displayed inequality would answer the “in particular” question but not necessarily determine \(F(N)\).

---

## 3. What does not count

The following do not by themselves resolve the problem:

1. **The known lower bound**
   \[
   F(N)\ge\left(\frac{2}{\sqrt3}-o(1)\right)\sqrt N.
   \]

2. **A weaker upper constant**, for example
   \[
   F(N)\le (2+o(1))\sqrt N.
   \]

3. An upper bound proved only when:
   - the exceptional sum equals \(N\);
   - \(A\) is symmetric under \(a\mapsto s-a\);
   - all elements participate in representations of the exceptional sum;
   - the exceptional representation count lies in only part of its possible range.

4. Bounds valid for only a density-one sequence of \(N\), unless they can be extended uniformly to all sufficiently large \(N\).

5. Conditional results depending on an unproved Sidon-set, inverse-additive, or pseudorandomness conjecture.

6. Numerical verification for finitely many \(N\), regardless of range.

7. Heuristic random-set calculations, continuous relaxations, or optimization of a model that does not encode every pair-sum collision.

8. A proof that the total number of repeated **representations** is small. The hypothesis concerns the number of distinct sums having multiplicity at least two, and the single exceptional sum may have multiplicity of order \(|A|\).

9. An improvement only in a lower-order term while retaining a leading constant larger than \(2/\sqrt3\).

---

## 4. Known results and context

### 4.1 Erdős–Freud lower construction

Let
\[
M=\left\lfloor\frac N3\right\rfloor
\]
and let \(B\subseteq[M]\) be a genuine Sidon set of size
\[
|B|=(1+o(1))\sqrt M.
\]
Define
\[
A:=B\cup (N-B),\qquad N-B:=\{N-b:b\in B\}.
\]
The two parts are disjoint for large \(N\), and
\[
|A|=2|B|=(1+o(1))\frac{2}{\sqrt3}\sqrt N.
\]

To check admissibility, divide pair sums into three types.

- **Low-low sums:**
  \[
  b+b',\qquad b,b'\in B.
  \]
  These are unique because \(B\) is Sidon, and they lie at most \(2N/3\).

- **High-high sums:**
  \[
  (N-b)+(N-b')=2N-(b+b').
  \]
  These are also unique and lie at least \(4N/3\).

- **Cross sums:**
  \[
  b+(N-b')=N+(b-b').
  \]
  If \(b\ne b'\), uniqueness follows from uniqueness of nonzero differences in a Sidon set. If \(b=b'\), every such pair has sum \(N\).

The three ranges do not overlap. Thus the only repeated sum is
\[
s=N,
\]
which has exactly \(|B|\) representations. Therefore
\[
F(N)\ge(1+o(1))\frac{2}{\sqrt3}\sqrt N.
\]

The existence of Sidon sets \(B\subseteq[M]\) of size \((1+o(1))\sqrt M\) follows from classical finite-field constructions, such as the Singer and Bose–Chowla constructions, together with standard truncation arguments.

### 4.2 Classical Sidon bounds

Let \(S(N)\) be the largest size of a genuine Sidon subset of \([N]\). Classical results of Erdős–Turán, together with finite-field lower constructions, give
\[
S(N)=(1+o(1))\sqrt N,
\]
with upper bounds of the form
\[
S(N)\le \sqrt N+O(N^{1/4}).
\]

Hence the case with no repeated sum is already far below the conjectured extremal constant.

### 4.3 Elementary global upper bound

Let \(k=|A|\). There are
\[
\binom{k+1}{2}
\]
unordered pair instances. If \(s\) is the exceptional sum and
\[
t=r_A(s),
\]
then all other sums occur at most once. A fixed-sum representation graph is a matching, possibly with one loop at \(s/2\), so
\[
t\le \left\lceil\frac k2\right\rceil.
\]
Since there are \(2N-1\) possible sums,
\[
\binom{k+1}{2}\le 2N-2+\left\lceil\frac k2\right\rceil.
\]
Consequently,
\[
F(N)\le 2\sqrt N+O(1).
\]

Thus the presently immediate asymptotic range is
\[
\frac{2}{\sqrt3}\le
\liminf_{N\to\infty}\frac{F(N)}{\sqrt N}
\le
\limsup_{N\to\infty}\frac{F(N)}{\sqrt N}
\le 2.
\]

### 4.4 Sidon extraction from the exceptional matching

Suppose an exceptional sum \(s\) exists, with \(t=r_A(s)\ge2\). The \(t\) representations of \(s\) are pairwise vertex-disjoint except that one may be the diagonal representation \((s/2,s/2)\).

Delete one element from each of \(t-1\) of these representations. The resulting set \(B\subseteq A\) has at most one representation of \(s\), and all other sums were already unique. Hence \(B\) is Sidon and
\[
|A|-t+1\le S(N).
\]
Therefore
\[
|A|\le S(N)+t-1.
\]

In particular, the conjectured bound already follows in the range
\[
t\le\left(\frac{2}{\sqrt3}-1+o(1)\right)\sqrt N.
\]
Any counterexample to the conjectured upper bound must therefore have a substantial exceptional matching.

### 4.5 Difference multiplicities

For \(d\in\{1,\dots,N-1\}\), define
\[
m_A(d):=\bigl|\{x:x,x+d\in A\}\bigr|.
\]
Then every admissible set satisfies
\[
m_A(d)\le2.
\]

Indeed, if \(x\ne y\) both represent the same difference \(d\), then
\[
(x+d)+y=(y+d)+x.
\]
These are distinct unordered pair representations, so their common sum must be the exceptional sum \(s\). If a third base \(z\) existed, then
\[
x+y+d=s=x+z+d,
\]
forcing \(y=z\).

Moreover, every duplicated difference is generated entirely by elements participating in representations of \(s\). This is a useful rigidity property, though the crude count
\[
\binom{k}{2}=\sum_{d=1}^{N-1}m_A(d)\le2(N-1)
\]
again gives only \(k\le2\sqrt N+O(1)\).

### 4.6 The exceptional core

If \(s\) is exceptional, define
\[
C_s:=A\cap(s-A)=\{a\in A:s-a\in A\}.
\]
If \(t=r_A(s)\), then
\[
|C_s|=2t-\delta,
\]
where
\[
\delta=
\begin{cases}
1,&s\text{ even and }s/2\in A,\\
0,&\text{otherwise}.
\end{cases}
\]
The complement \(A\setminus C_s\) consists of elements not paired under reflection about \(s/2\). The lower construction has essentially all elements in \(C_s\), but this need not hold for an arbitrary admissible set.

### 4.7 Analogous difference problem

The database commentary reports that Erdős and Freud proved the analogous extremal quantity for representations of the form
\[
n=a-b
\]
is asymptotic to \(\sqrt N\), under their corresponding representation convention. That result does not directly settle the sum problem because fixed-sum representations form a reflection matching and interact differently with the interval boundary.

The database also states that Problem #864 is a weaker form of Problem #840. Without the precise statement of #840, no stronger formal implication should be asserted here.

---

## 5. Traps and edge cases

1. **“At most one” includes zero.**  
   A genuine Sidon set is admissible.

2. **The exceptional sum has unbounded multiplicity.**  
   It may have up to \(\lceil |A|/2\rceil\) representations. Treating it as merely one extra collision loses the main phenomenon.

3. **Diagonal representations count.**  
   If \(2a=n\), then \((a,a)\) is a valid representation. Collisions such as
   \[
   a+c=2b
   \]
   are forbidden unless that value is the unique exceptional sum.

4. **Fixed-sum representations form a matching, not a clique.**  
   An element \(a\) can occur in only the pair \(\{a,s-a\}\), with a possible loop at \(s/2\).

5. **A set need not be symmetric about the exceptional sum.**  
   The core \(C_s\) may be a proper subset of \(A\). Assuming \(A=s-A\) proves only a special case.

6. **Repeated differences are possible.**  
   Admissibility does not imply that \(A\) is Sidon in the difference sense. Every positive difference may occur twice, and the lower construction has many duplicated differences.

7. **But a positive difference cannot occur three times.**  
   This structural fact should be used rather than assuming all differences are distinct.

8. **Sum counting alone is too weak.**  
   If \(t=r_A(s)\), then
   \[
   |A+A|=\binom{|A|+1}{2}-(t-1).
   \]
   Comparing this only with \(2N-1\) yields the constant \(2\), not \(2/\sqrt3\).

9. **Modular reduction creates new collisions.**  
   Distinct integer sums may become equal modulo \(q\). One cannot simply map \(A\) into a cyclic group and declare it Sidon there.

10. **Reflection conventions matter.**  
    The interval reflection \(a\mapsto N+1-a\) sends an exceptional sum \(s\) to \(2N+2-s\). The lower construction instead uses \(b\mapsto N-b\), centered at the exceptional sum \(N\).

11. **Deleting one element is generally insufficient.**  
    To eliminate an exceptional sum with \(t\) representations while retaining one, one must generally delete \(t-1\) elements.

12. **Small endpoint sums cannot be highly exceptional.**  
    For sums near \(2\) or \(2N\), there are very few possible pairs. Arguments that optimize over \(s\) should include these boundary restrictions rather than treating all \(s\) identically.

13. **Asymptotic quantifiers must be uniform.**  
    An \(o(1)\) that depends on the chosen set \(A\) does not establish the extremal bound.

14. **Terminology may conceal diagonal exceptions.**  
    Results about weak Sidon sets, \(B_2[g]\)-sets, or sets with bounded additive energy must be checked against the exact unordered-with-diagonal representation function used here.

---

## 6. Verification hooks

### 6.1 Direct admissibility checker

Given \(A\subseteq[N]\):

1. Initialize integer counters \(c[2],\dots,c[2N]\) to zero.
2. For every \(a,b\in A\) with \(a\le b\), increment \(c[a+b]\).
3. Form
   \[
   E=\{n:c[n]\ge2\}.
   \]
4. Accept exactly when \(|E|\le1\).

This takes \(O(|A|^2+N)\) time.

The checker should also output:

- the exceptional sum \(s\), if any;
- its multiplicity \(t=c[s]\);
- the paired core \(C_s\);
- all difference multiplicities \(m_A(d)\).

These statistics are useful for testing structural conjectures.

### 6.2 Exact backtracking

For moderate \(N\), build \(A\) incrementally. Maintain:

- all current pair-sum counts;
- either no repeated sum yet or a designated exceptional sum \(s\).

When adding \(x\), update the sums \(x+a\) for existing \(a\in A\), together with \(2x\). Reject if some sum \(n\ne s\) reaches multiplicity two, or if two different sums become repeated.

Reflection
\[
A\mapsto\{N+1-a:a\in A\}
\]
can be used for symmetry reduction.

### 6.3 Exact ILP formulation

Use binary variables \(x_i\) indicating \(i\in A\), and binary variables \(y_{ij}\) for \(1\le i\le j\le N\), with
\[
y_{ij}=x_i x_j
\]
enforced by standard linearization:
\[
y_{ij}\le x_i,\qquad y_{ij}\le x_j,\qquad
y_{ij}\ge x_i+x_j-1.
\]
For \(i=j\), these constraints force \(y_{ii}=x_i\).

Introduce binary variables \(z_n\) for \(2\le n\le2N\), with
\[
\sum_{n=2}^{2N}z_n\le1,
\]
and constraints
\[
\sum_{\substack{1\le i\le j\le N\\i+j=n}}y_{ij}
\le 1+N z_n.
\]
Maximize
\[
\sum_{i=1}^N x_i.
\]
This computes \(F(N)\) exactly, subject to solver certification.

### 6.4 Fixed-exception SAT formulation

Fix a candidate exceptional sum \(s\). For every \(n\ne s\) and every two distinct unordered pairs
\[
\{a,b\},\{c,d\}\subseteq[N],\qquad a+b=c+d=n,
\]
forbid simultaneous inclusion of all elements in the two pairs. This gives a finite hypergraph independent-set formulation. Enumerating \(s\) and also the no-exception case gives the exact optimum.

### 6.5 Construction verification

For a proposed Sidon seed \(B\subseteq[\lfloor N/3\rfloor]\):

- hash all unordered sums \(b+b'\) and verify uniqueness;
- form \(A=B\cup(N-B)\);
- verify that all repeated pair sums equal \(N\);
- confirm that \(r_A(N)=|B|\).

This catches diagonal and boundary mistakes.

### 6.6 Useful experimental observables

For exact or heuristic maximizers, record:

\[
\frac{|A|}{\sqrt N},\qquad
\frac{s}{N},\qquad
\frac{t}{|A|},\qquad
\frac{|C_s|}{|A|},
\]
as well as:

- the distribution of \(A\) below and above \(s/2\);
- the set of duplicated differences;
- the number of occupied sums in low, central, and high ranges;
- whether maximizers resemble \(B\cup(s-B)\);
- the minimum number of distinct repeated sums among all \(k\)-element subsets.

Finite data cannot prove the asymptotic result, but it can rapidly refute proposed structural lemmas.

---

## 7. Attack routes

### Route 1: Exceptional-core decomposition and stability

**Core mechanism.**  
Write
\[
A=C_s\sqcup U,
\]
where \(C_s=A\cap(s-A)\) is the reflected core and \(U\) consists of unpaired elements. Parameterize the core by complementary pairs
\[
\{x_i,s-x_i\},\qquad 1\le i\le t,
\]
with a possible central singleton \(s/2\).

**Key lemma needed.**  
A quantitative packing or stability theorem of the following kind:

> If \(A\subseteq[N]\) has all repeated sums concentrated at \(s\), then the interactions among complementary pairs and unpaired elements force
> \[
> |A|^2\le \frac43N+o(N).
> \]

A more refined version could give a lower bound
\[
N\ge \Phi(t,|U|)-o(|A|^2)
\]
whose minimum over feasible \(t,|U|\) is \(3|A|^2/4\).

**Why it might work.**  
Every duplicated positive difference is generated inside \(C_s\), while every interaction involving \(U\) must be collision-free. The lower construction is completely reflected and highly structured, suggesting a stability phenomenon.

**Most likely failure point.**  
Sidon extraction only forces
\[
t\gtrsim |A|-\sqrt N,
\]
which does not imply that almost all elements are paired. A substantial unpaired part may coexist with the core, and controlling all three types
\[
C_s+C_s,\qquad C_s+U,\qquad U+U
\]
may be difficult.

**Quick blockage test.**  
For exact maximizers at small \(N\), plot \(|C_s|/|A|\) and test every proposed inequality in the variables \(t,|U|,s\). Any lemma forcing near-total symmetry should be checked for immediate finite counterexamples.

---

### Route 2: Weighted differences and an Erdős–Turán sliding-window argument

**Core mechanism.**  
Adapt the classical Erdős–Turán proof of the Sidon upper bound. For an interval length \(L\), let
\[
A_u:=|A\cap[u+1,u+L]|.
\]
Sums of \(\binom{A_u}{2}\) over shifts \(u\) can be rewritten as weighted sums of difference multiplicities:
\[
\sum_u\binom{A_u}{2}
=
\sum_{d<L}(L-d)m_A(d)
\]
up to explicitly controlled boundary terms.

Here \(m_A(d)\le2\), and every \(d\) with \(m_A(d)=2\) satisfies a rigid reflection relation involving \(s\).

**Key lemma needed.**  
A sharp upper bound on
\[
\sum_{d<L}(L-d)m_A(d)
\]
that exploits not only \(m_A(d)\le2\), but also the fact that all doubled differences arise from complementary pairs about the same center \(s/2\). After combining with the Cauchy lower bound on the sliding-window counts and optimizing \(L\), the desired output must be
\[
|A|^2\le\frac43N+o(N).
\]

**Why it might work.**  
The sharp Sidon constant comes from weighted local difference counts, not from the crude inequality \(\binom{k}{2}\le N\). The present problem also has strong difference rigidity, so a modified weighted argument is natural.

**Most likely failure point.**  
Replacing \(m_A(d)\le1\) by \(m_A(d)\le2\) immediately loses the needed constant. The doubled differences in the lower construction are numerous and organized, so the argument must exploit their exact geometry rather than merely count them.

**Quick blockage test.**  
Evaluate every candidate weighted inequality on the Erdős–Freud construction. It must allow
\[
|A|\sim\frac{2}{\sqrt3}\sqrt N
\]
and should be close to equality there. If it yields a stronger constant, some boundary or duplicated-difference contribution has been omitted.

---

### Route 3: Fourier or generating-polynomial inequalities

**Core mechanism.**  
Let
\[
P(z)=\sum_{a\in A}z^a.
\]
The coefficient of \(z^n\) in \(P(z)^2\) is the ordered representation count
\[
R_A(n)=|\{(a,b)\in A^2:a+b=n\}|.
\]
For \(n\ne s\),
\[
R_A(n)\le2,
\]
with value \(1\) possible for a diagonal representation. Only the coefficient at \(s\) can be large.

Parseval gives
\[
\int_0^1\left|P(e^{2\pi i\theta})\right|^4\,d\theta
=
\sum_n R_A(n)^2.
\]

**Key lemma needed.**  
A weighted fourth-moment, large-sieve, or positive-kernel inequality showing that a polynomial supported in \([N]\) cannot have all convolution coefficients bounded by \(2\) except for one spike unless
\[
P(1)=|A|\le\left(\frac{2}{\sqrt3}+o(1)\right)\sqrt N.
\]
The location \(s\) and diagonal parity terms must be included explicitly.

**Why it might work.**  
The hypothesis is exactly a statement about the coefficient profile of \(P^2\): almost every coefficient is tiny, with one exceptional coefficient. Positive trigonometric kernels can exploit both support length and concentration in a way raw pair counting cannot.

**Most likely failure point.**  
The unweighted fourth moment mainly measures total additive energy. A single coefficient of size \(2t\) contributes \(4t^2\), potentially absorbing all nontrivial energy and leaving only the weak constant \(2\). Spatial information about coefficient locations is essential.

**Quick blockage test.**  
Reduce the proposed moment inequalities to an optimization in \(k,t,s\) and compare with exact coefficient profiles from small extremizers and the reflected Sidon construction. If the optimized constant remains \(2\), the chosen moments do not use enough localization.

---

### Route 4: Hypergraph supersaturation for repeated sum values

**Core mechanism.**  
Fix \(N\). For each equality
\[
a+b=c+d
\]
between distinct unordered pairs, regard the support \(\{a,b,c,d\}\), with the appropriate diagonal convention, as a forbidden hyperedge labeled by the common sum. An admissible set may contain many hyperedges, but all must carry one label \(s\).

**Key lemma needed.**  
A labeled supersaturation theorem:

> For every \(\varepsilon>0\), every
> \[
> A\subseteq[N],\qquad
> |A|\ge\left(\frac{2}{\sqrt3}+\varepsilon\right)\sqrt N,
> \]
> contains additive quadruples with at least two distinct common-sum labels.

Equivalently, every set above the conjectured threshold has at least two distinct integers \(n\) with \(r_A(n)\ge2\).

**Why it might work.**  
This directly matches the statement and avoids first classifying the exceptional matching. Techniques from extremal hypergraph theory, dependent random choice, or entropy may quantify not just the number of additive quadruples but the number of labels supporting them.

**Most likely failure point.**  
Standard additive-energy supersaturation only forces many quadruples. It does not prevent those quadruples from all lying over a single sum, which is exactly the allowed configuration.

**Quick blockage test.**  
For small \(N\), compute
\[
g_N(k):=\min_{\substack{A\subseteq[N]\\|A|=k}}
\left|\{n:r_A(n)\ge2\}\right|.
\]
Compare the transition \(g_N(k)=1\to g_N(k)\ge2\) with \((2/\sqrt3)\sqrt N\). Also test any proposed supersaturation inequality against sets with one very high-multiplicity sum.

---

### Route 5: Modular projection and cyclic Sidon bounds

**Core mechanism.**  
Project \(A\) into one or several cyclic groups \(\mathbb Z/q\mathbb Z\), possibly after a translation or restriction to selected subintervals. Apply sharp bounds for Sidon sets in finite groups to large collision-free pieces, then combine the information from several moduli or interval blocks.

**Key lemma needed.**  
A projection/partition theorem guaranteeing that one can choose \(q\), shifts, and a large subset \(A'\subseteq A\) such that all modular pair-sum collisions in \(A'\) either come from the integer exceptional sum \(s\) or are few enough to remove cheaply. The retained size and modulus must optimize to the constant \(2/\sqrt3\).

**Why it might work.**  
Finite-group Sidon bounds are sharp and algebraically robust. The factor \(3\) in the lower construction—one low block, one central cross-sum band, and one high block—suggests that a three-region or multi-modulus argument may recover the constant.

**Most likely failure point.**  
Reduction modulo \(q\) identifies sums differing by \(q\), producing many wraparound collisions unrelated to \(s\). Removing all such collisions may destroy too large a fraction of \(A\).

**Quick blockage test.**  
Project exact lower constructions modulo candidate values of \(q\). Measure the minimum deletions needed to obtain a modular Sidon set. If even the conjecturally extremal construction loses too much, that modulus or partition cannot produce a sharp proof.

---

### Route 6: Disproof through multi-block or finite-geometric constructions

**Core mechanism.**  
Attempt to improve the two-block construction
\[
B\cup(N-B)
\]
using three or more blocks, affine copies of Sidon sets, perfect difference sets, or finite-field templates. Separate macro-scale block centers from micro-scale Sidon labels.

A general model is
\[
A=\bigcup_{i=1}^m (L_i+\lambda_i B_i),
\]
with block locations \(L_i\) chosen so that:

- internal and cross-block sums occupy disjoint ranges or residue classes;
- every collision that remains has the same total sum \(s\);
- the total number of selected elements exceeds \((2/\sqrt3+\varepsilon)\sqrt N\).

**Key lemma needed.**  
An explicit family of block templates and label sets for which equality
\[
a+b=c+d
\]
between distinct unordered pairs implies
\[
a+b=c+d=s.
\]
The block-span efficiency must beat the reflected two-block ratio.

**Why it might work.**  
The known lower construction may not be globally optimal; it is only the simplest way to concentrate all collisions at one sum. Finite-geometric difference families can sometimes coordinate many pair types with fewer occupied integer positions.

**Most likely failure point.**  
With three or more blocks, macro-level parallelograms tend to create repeated sums at several block-center values. Avoiding all but one such value may force the macro template itself to be Sidon, eliminating any gain.

**Quick blockage test.**  
Use SAT or MILP to optimize small macro templates with symbolic collision labels. Then substitute small Sidon or Golomb-ruler microsets and verify all pair sums. Search specifically for scalable templates whose density ratio beats \(2/\sqrt3\), rather than isolated finite examples.

---

## 8. Verdict on difficulty

This is a genuinely difficult sharp-constant problem. Elementary counting gives only
\[
F(N)\le(2+o(1))\sqrt N,
\]
while the conjecture asks for
\[
F(N)\le\left(\frac{2}{\sqrt3}+o(1)\right)\sqrt N.
\]
The missing improvement is substantial and cannot come from counting the number of pair sums alone. A successful proof must exploit the fact that **all** nontrivial collisions occur at one common sum, including the rigid reflection structure this imposes on duplicated differences.

The problem lies at the intersection of sharp Sidon-set estimates, additive-energy concentration, and interval geometry. The main obstruction is that the exceptional sum may support \(\Theta(|A|)\) representations, so standard “almost Sidon” arguments lose too much.

The database identifies this as a weaker form of Problem #840, suggesting that a solution of the stronger problem may settle it. No equivalence to a famous broad conjecture is evident from the supplied information, and none should be claimed. Nonetheless, the exact leading constant and the absence of any apparent soft route make this a high-difficulty research problem rather than a routine refinement of the classical Sidon bound.