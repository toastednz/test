# Problem brief: Erdős Problem #774

## 1. Precise statement

### 1.1 Dissociated sets

Take \(\mathbb N=\{1,2,3,\dots\}\). A set \(D\subseteq \mathbb N\) is **dissociated** if for every pair of finite subsets \(X,Y\subseteq D\),
\[
\sum_{x\in X}x=\sum_{y\in Y}y
\quad\Longrightarrow\quad
X=Y.
\]
The empty sum is \(0\).

After cancelling \(X\cap Y\), this is equivalent to:

> There is no nonzero finitely supported function
> \[
> \varepsilon:D\to\{-1,0,1\}
> \]
> such that
> \[
> \sum_{d\in D}\varepsilon(d)d=0.
> \]

Thus “dissociated” here means independence against \(\{-1,0,1\}\)-relations, not linear independence over \(\mathbb Q\), and not uniqueness of sums allowing repeated summands.

For a finite set \(B\subseteq\mathbb N\), define its dissociation number by
\[
\alpha_{\mathrm{dis}}(B)
=
\max\{|D|:D\subseteq B\text{ is dissociated}\}.
\]

### 1.2 Proportionately dissociated sets

An infinite set \(A\subseteq\mathbb N\) is **proportionately dissociated** if
\[
\exists\,\delta>0\quad
\forall\,B\subseteq A\text{ finite}\quad
\exists\,D\subseteq B
\]
such that
\[
D\text{ is dissociated}
\qquad\text{and}\qquad
|D|\ge \delta |B|.
\]
Equivalently,
\[
\inf_{\varnothing\ne B\subseteq A,\ B\text{ finite}}
\frac{\alpha_{\mathrm{dis}}(B)}{|B|}>0.
\]

The notation \(\gg |B|\) is understood in the standard way: the implied positive constant is independent of \(B\), but may depend on \(A\). Necessarily \(0<\delta\le 1\).

If one uses the convention \(0\in\mathbb N\), the hypothesis automatically excludes \(0\in A\), since \(\{0\}\) contains no nonempty dissociated subset.

### 1.3 The question

Is the following statement true?

> For every infinite proportionately dissociated set \(A\subseteq\mathbb N\), there is an integer \(k\ge 1\) and dissociated sets
> \[
> A_1,\dots,A_k\subseteq A
> \]
> such that
> \[
> A=A_1\cup\cdots\cup A_k?
> \]

The \(A_i\) need not initially be disjoint. Since subsets of dissociated sets are dissociated, a finite cover is equivalent to a finite partition: assign each element of \(A\) to one covering set containing it.

### 1.4 Hypergraph formulation

For \(A\subseteq\mathbb N\), let \(\mathcal H(A)\) be the hypergraph with vertex set \(A\), whose hyperedges are the finite sets \(S\subseteq A\) supporting a nontrivial signed relation
\[
\sum_{s\in S}\varepsilon_s s=0,
\qquad \varepsilon_s\in\{-1,1\}.
\]
It suffices to retain only inclusion-minimal such supports, called **circuits**.

Then:

- a subset of \(A\) is dissociated exactly when it is independent in \(\mathcal H(A)\);
- \(A\) is proportionately dissociated exactly when every finite induced subhypergraph has an independent set occupying at least a fixed positive proportion of its vertices;
- \(A\) is a finite union of dissociated sets exactly when \(\mathcal H(A)\) has finite chromatic number.

Define
\[
\chi_{\mathrm{dis}}(B)
=
\min\{k:B\text{ can be partitioned into }k\text{ dissociated sets}\}.
\]

The problem asks whether the hereditary lower bound
\[
\alpha_{\mathrm{dis}}(B)\ge \delta|B|
\]
forces finite dissociation chromatic number.

---

## 2. What counts as a solution

### 2.1 Complete positive solution

A complete proof must show:

\[
\forall A\subseteq\mathbb N\text{ infinite},\quad
\left[
\exists\delta>0\
\forall B\subseteq A\text{ finite},\
\alpha_{\mathrm{dis}}(B)\ge\delta|B|
\right]
\]
implies
\[
\exists k<\infty\quad \chi_{\mathrm{dis}}(A)\le k.
\]

The number \(k\) may initially be allowed to depend on \(A\). However, the problem is in fact equivalent to the following uniform finite statement:

> **Uniform finite formulation.** For every \(\delta>0\), there exists \(k=k(\delta)\) such that every finite \(F\subseteq\mathbb N\) satisfying
> \[
> \alpha_{\mathrm{dis}}(B)\ge\delta |B|
> \quad\text{for all }B\subseteq F
> \]
> satisfies
> \[
> \chi_{\mathrm{dis}}(F)\le k.
> \]

Once the uniform finite result is proved, the infinite coloring follows by compactness: if every finite subset of \(A\) admits a valid \(k\)-coloring, then the closed finite constraints in the compact space \([k]^A\) have a simultaneous solution.

Conversely, failure of a uniform \(k(\delta)\) can be assembled into an infinite counterexample by the scale-separation construction described below. Thus a positive proof must, perhaps implicitly, establish a bound depending only on the proportionality constant.

### 2.2 Complete negative solution

A complete disproof must construct, probabilistically or explicitly, an infinite \(A\subseteq\mathbb N\) and a fixed \(\delta>0\) such that:

1. for every finite \(B\subseteq A\),
   \[
   \alpha_{\mathrm{dis}}(B)\ge\delta|B|;
   \]
2. for every \(k\ge1\), \(A\) cannot be partitioned into \(k\) dissociated sets.

Condition 2 can be verified by proving that for every \(k\) there is a finite \(F_k\subseteq A\) with
\[
\chi_{\mathrm{dis}}(F_k)>k.
\]
Equivalently, every \(k\)-coloring of \(F_k\) must contain a monochromatic nontrivial \(\{-1,0,1\}\)-relation.

A particularly useful sufficient route to a counterexample is to construct finite sets \(F_i\subseteq\mathbb N\) with one fixed \(\delta>0\) such that
\[
\alpha_{\mathrm{dis}}(B)\ge\delta|B|
\quad\text{for every }B\subseteq F_i,
\]
while
\[
\chi_{\mathrm{dis}}(F_i)\longrightarrow\infty.
\]

These gadgets can be joined without introducing cross-gadget relations. Choose integers \(Q_i\) recursively and set
\[
A_i=Q_iF_i
\]
so that
\[
Q_i>\sum_{j<i}\sum_{a\in A_j}a.
\]
Then put
\[
A=\bigcup_{i\ge1}A_i.
\]

Any signed relation in \(A\) can be examined in its highest-index block. A nonzero signed sum from \(A_i\) has absolute value at least \(Q_i\), while the contribution of all lower blocks has absolute value less than \(Q_i\). Consequently, a union of dissociated subsets, one from each block, remains dissociated. Hence \(A\) inherits the same proportionality constant, while
\[
\chi_{\mathrm{dis}}(A)\ge\sup_i\chi_{\mathrm{dis}}(F_i)=\infty.
\]

Thus a uniform family of finite gadgets is already a complete route to disproof.

---

## 3. What does not count

The following would not settle the problem.

1. **Logarithmically many colors.** Repeatedly remove a dissociated subset of size at least \(\delta\) times the current remainder. This gives
   \[
   \chi_{\mathrm{dis}}(B)=O_\delta(\log |B|)
   \]
   for finite \(B\), not a bound independent of \(|B|\).

2. **A bound only for bounded sets.** Proving the result for \(A\subseteq[1,N]\), with the number of colors depending on \(N\), is insufficient.

3. **A bound only for special families**, such as lacunary sequences, sets with bounded occupancy in dyadic intervals, random sets of a particular model, or sets satisfying a stronger growth condition.

4. **Checking only short relations.** Avoiding equations such as
   \[
   x+y=z,\qquad x+y=z+w
   \]
   does not ensure dissociation. Relations can have arbitrarily large support.

5. **Additive-combinatorial Sidon decompositions.** The analogous problem for \(B_2\)-sets is distinct. Standard additive Sidon conditions involve equations with repeated summands, whereas the present definition only allows coefficients in \(\{-1,0,1\}\).

6. **Asymptotic density estimates.** Showing \(A\cap[1,N]\) is small, or improving its upper bound, does not provide a finite coloring.

7. **Conditional results** depending on an unproved conjecture do not resolve the unconditional problem.

8. **A candidate counterexample verified only on initial segments.** A disproof needs one fixed \(\delta>0\) for all finite subsets and unbounded chromatic number, with rigorous proofs of both properties.

9. **A probabilistic construction without controlling unintended relations.** In an integer realization, long accidental signed relations may dramatically reduce the hereditary dissociation ratio.

---

## 4. Known results and context

### 4.1 Pisier’s characterization

In harmonic analysis, a set \(A\subseteq\mathbb Z\) is a **Sidon set** if there exists \(C<\infty\) such that for every finitely supported \(f:A\to\mathbb C\),
\[
\sum_{n\in A}|f(n)|
\le
C\sup_{\theta\in[0,1]}
\left|
\sum_{n\in A}f(n)e^{2\pi in\theta}
\right|.
\]
Equivalently, for each such \(f\), some \(\theta\) attains the corresponding lower bound up to the constant \(C\).

Pisier proved that, for subsets of \(\mathbb Z\), this harmonic-analytic Sidon property is equivalent to proportional dissociation: every finite subset contains a dissociated, often called **quasi-independent**, subset of proportional cardinality.

Therefore Erdős Problem #774 is exactly the classical structural question:

> Is every harmonic-analytic Sidon subset of \(\mathbb Z\) a finite union of quasi-independent sets?

This is substantially stronger than merely being a Sidon set.

### 4.2 The easy converse

If
\[
A=A_1\cup\cdots\cup A_k
\]
with each \(A_i\) dissociated, then every finite \(B\subseteq A\) has
\[
|B\cap A_i|\ge |B|/k
\]
for some \(i\), after using a disjoint refinement of the cover. Thus \(B\cap A_i\) is dissociated and has proportional size. This is the converse noted by Pisier.

The open direction is whether proportional dissociation forces such a finite decomposition.

### 4.3 History

The question appears in a paper of Alon and Erdős from 1985, who wrote that sufficiency seemed unlikely. The broader harmonic-analytic context goes back at least to Pisier’s 1983 work.

The analogous question obtained by replacing “dissociated” with “Sidon” in the additive-combinatorial \(B_2\) sense was resolved negatively by Nešetřil, Rödl, and Sales in 2024. That result is important evidence for a negative answer here, but it does not directly transfer because the forbidden relation systems are different.

### 4.4 Elementary sparsity consequence

If \(D\subseteq[1,N]\) is dissociated and \(|D|=d\), its \(2^d\) subset sums are distinct integers lying in \([0,dN]\). Hence
\[
2^d\le dN+1.
\]
If \(A\) is proportionately dissociated with constant \(\delta\), apply this to a dissociated subset of
\[
B=A\cap[1,N].
\]
One obtains
\[
|A\cap[1,N]|=O_\delta(\log N).
\]

This severe sparsity is necessary but does not imply finite decomposability.

### 4.5 Easy positive examples

If \(a_1<a_2<\cdots\) satisfies the superincreasing condition
\[
a_j>\sum_{i<j}a_i
\]
for every \(j\), then \(\{a_j\}\) is dissociated. Powers of two are the standard example.

More generally, sufficiently lacunary sequences can be partitioned into finitely many superincreasing subsequences. Thus the problem concerns Sidon sets whose sparseness is not organized into a bounded number of simple growth chains.

---

## 5. Traps and edge cases

### 5.1 Repeated summands are not allowed

The equation
\[
2a=b+c
\]
does not by itself violate dissociation, because it uses coefficient \(2\). For example,
\[
\{2,3,4\}
\]
is dissociated: its subset sums are
\[
0,2,3,4,5,6,7,9,
\]
all distinct, even though
\[
2+4=3+3.
\]

This is a major distinction from standard additive \(B_2\)-sets.

### 5.2 Checking pair sums is insufficient

A set may have no nontrivial relation of support at most four and still possess a longer relation. A proof must exclude all finite \(\{-1,0,1\}\)-relations.

### 5.3 Rational linear algebra is irrelevant

All integers lie in a one-dimensional vector space over \(\mathbb Q\), so ordinary linear independence cannot model dissociation. The bounded coefficient set \(\{-1,0,1\}\) is essential.

### 5.4 Greedy extraction loses a logarithm

From proportional dissociation one can color a finite \(n\)-element set with \(O_\delta(\log n)\) colors by repeatedly removing large dissociated subsets. The remainder never becomes empty after a bounded number of proportional removals uniformly in \(n\). This is the most immediate false proof.

### 5.5 Maximal versus maximum

A maximal dissociated subset need not be maximum or have the guaranteed proportional size. Pisier’s criterion supplies existence of a large subset, not largeness of every greedily constructed maximal subset.

### 5.6 Modular arguments

Dissociation modulo a prime \(p\) implies integer dissociation, but the converse need not hold because distinct integer sums can coincide modulo \(p\). For a fixed finite set, choosing
\[
p>2\sum_{a\in F}a
\]
avoids wraparound and makes signed zero-relations modulo \(p\) equivalent to integer zero-relations.

### 5.7 Overlapping covers

A finite cover by dissociated sets may always be refined to a partition. No extra strength is gained by allowing overlaps.

### 5.8 Small cases can be deceptive

For
\[
F=\{1,2,3\},
\]
the only essential obstruction is
\[
1+2=3.
\]
Every proper subset is dissociated, so
\[
\min_{\varnothing\ne B\subseteq F}
\frac{\alpha_{\mathrm{dis}}(B)}{|B|}
=\frac23,
\qquad
\chi_{\mathrm{dis}}(F)=2.
\]
High chromatic behavior requires a coherent collection of many relations, not merely individual dependencies.

---

## 6. Verification hooks

### 6.1 Testing dissociation exactly

For a finite set
\[
D=\{d_1,\dots,d_r\},
\]
compute all \(2^r\) subset sums. Then \(D\) is dissociated exactly when all sums are distinct.

Equivalently, enumerate
\[
\varepsilon\in\{-1,0,1\}^r\setminus\{0\}
\]
and test whether
\[
\sum_i\varepsilon_i d_i=0.
\]
To remove sign duplication, require the first nonzero coefficient to be \(+1\).

### 6.2 Computing the hereditary ratio

For finite \(F\), define
\[
\rho(F)=
\min_{\varnothing\ne B\subseteq F}
\frac{\alpha_{\mathrm{dis}}(B)}{|B|}.
\]

A brute-force exact computation is:

1. enumerate every \(B\subseteq F\);
2. enumerate every \(D\subseteq B\);
3. test whether \(D\) is dissociated;
4. record the maximum \(|D|\);
5. minimize the resulting ratio.

This is exponential at several levels, but is practical for small \(F\). Memoizing dissociation status and processing subsets by cardinality significantly reduces the cost.

### 6.3 Circuit hypergraph generation

Enumerate all signed relations
\[
\sum_{i=1}^n\varepsilon_i f_i=0,
\qquad \varepsilon_i\in\{-1,0,1\}.
\]
Record the support
\[
S=\{f_i:\varepsilon_i\ne0\}.
\]
Delete every support properly containing another dependent support. The remaining supports are the circuits.

### 6.4 Computing \(\chi_{\mathrm{dis}}(F)\)

For a proposed number \(k\) of colors, use Boolean variables
\[
x_{v,c}\in\{0,1\},
\qquad v\in F,\ c\in[k].
\]
Impose
\[
\sum_{c=1}^k x_{v,c}=1
\]
for each \(v\). For every circuit \(S\) and color \(c\), impose
\[
\sum_{v\in S}x_{v,c}\le |S|-1.
\]
Feasibility is exactly \(k\)-colorability into dissociated classes. SAT, MILP, or exact-cover solvers can be used.

### 6.5 Gadget search target

The decisive computational target is not merely a set with large \(\chi_{\mathrm{dis}}\). It is a sequence \(F_i\) for which both
\[
\rho(F_i)\ge\delta
\]
for one common \(\delta>0\), and
\[
\chi_{\mathrm{dis}}(F_i)\to\infty.
\]

Track the Pareto frontier of
\[
\bigl(\rho(F),\chi_{\mathrm{dis}}(F),|F|,\max F\bigr).
\]

### 6.6 Testing scale separation

Given gadgets \(F_1,\dots,F_t\), choose \(Q_i\) recursively and verify mechanically that
\[
Q_i>\sum_{j<i}\sum_{a\in Q_jF_j}a.
\]
Then enumerate signed relations in the finite union and confirm that every relation decomposes blockwise. This is a useful sanity check before formalizing the general scale-separation lemma.

---

## 7. Attack routes

### Route 1: Arithmetic circuit hypergraph coloring

**Core idea.** Study the hypergraph of minimal \(\{-1,0,1\}\)-relations and prove that this special class of hypergraphs is \(\chi\)-bounded by its hereditary independence ratio.

**Key lemma needed.** A structural theorem of the form:
\[
\alpha_{\mathrm{dis}}(B)\ge\delta|B|
\ \forall B\subseteq F
\quad\Longrightarrow\quad
\chi_{\mathrm{dis}}(F)\le k(\delta).
\]
To avoid merely restating the problem, the lemma should arise from a specific feature such as circuit elimination, a bounded-degeneracy reduction, or control of a subfamily of “essential” circuits whose proper coloring automatically eliminates all relations.

**Why it might work.** Signed relations among integers obey arithmetic identities unavailable in arbitrary hypergraphs. Minimal relations may have enough elimination structure to force a bounded coloring theorem.

**Likely failure point.** Dissociation circuits do not satisfy the matroid circuit axioms, and their sizes are unbounded. Circuit elimination can create coefficients outside \(\{-1,0,1\}\), destroying the required structure.

**Quick test.** Enumerate circuits of small sets and test whether two intersecting circuits admit another circuit in their union minus one common vertex. Frequent failure would block a matroid-style elimination proof.

---

### Route 2: Harmonic analysis and Riesz-product decomposition

**Core idea.** Use Pisier’s Sidon characterization, interpolation measures, and Riesz products to strengthen “every finite subset contains one large quasi-independent subset” into a bounded decomposition.

**Key lemma needed.** A bounded-support decomposition theorem: a Sidon set with constant \(C\) should admit a cover by at most \(k(C)\) quasi-independent sets, or an analytic certificate that can be rounded into such a cover.

**Why it might work.** Dissociated sets are precisely those for which classical Riesz-product arguments are strongest. The Sidon inequality provides uniform control for all coefficient choices, not only cardinality estimates.

**Likely failure point.** Pisier’s criterion produces a large quasi-independent subset separately for each finite set. It does not produce compatible subsets, a bounded family of selectors, or a global coloring. Independent random selectors generally give only logarithmically many sets to cover an \(n\)-point set.

**Quick test.** For small finite \(F\), compare numerical or certified finite Sidon constants with \(\chi_{\mathrm{dis}}(F)\). Search for families with bounded Sidon constant but growing dissociation chromatic number. Such families would strongly disfavor this route and point toward disproof.

---

### Route 3: Ordered growth and block decomposition

**Core idea.** Exploit the natural order on \(\mathbb N\). Split \(A\) into multiplicative or dyadic blocks and color so that, within each color, the largest term in any proposed relation dominates all lower terms.

**Key lemma needed.** A proportionately dissociated set must admit a bounded coloring in which each color has sufficiently sparse occupancy across scales, ideally making each color superincreasing or satisfying a weaker highest-term domination property.

**Why it might work.** Positive integers have no cancellation without comparable large terms. The counting bound
\[
|A\cap[1,N]|=O_\delta(\log N)
\]
shows exponential average growth.

**Likely failure point.** Logarithmic global counting does not imply uniformly bounded occupancy in intervals such as \([N,2N]\). A Sidon set may have large clusters at rare scales, preventing a bounded decomposition into lacunary sequences.

**Quick test.** Search finite sets with large \(\rho(F)\) but with large minimum number of superincreasing subsequences needed to cover \(F\). If this number grows while \(\rho(F)\) stays bounded below, the strongest version of this route is blocked.

---

### Route 4: Matroid approximation and partition theorems

**Core idea.** Treat
\[
r(B)=\alpha_{\mathrm{dis}}(B)
\]
as a rank-like function. If dissociated sets were the independent sets of a matroid, the condition
\[
|B|\le k\,r(B)
\]
for all \(B\) would lead to a partition into \(k\) independent sets via matroid partition theory.

**Key lemma needed.** Either:

- prove an approximate exchange property for dissociated subsets;
- sandwich \(r\) between matroid ranks with bounded loss;
- or represent dissociation as the intersection of boundedly many matroidal independence systems.

**Why it might work.** The hypothesis is precisely the type of hereditary rank inequality appearing in matroid arboricity and partition theorems.

**Likely failure point.** Dissociated sets do not satisfy the matroid exchange axiom. Replacing one element can activate a long signed relation, and there may be no single-element repair.

**Quick test.** Exhaustively search for small \(X,Y\subseteq F\) with \(X,Y\) dissociated, \(|X|<|Y|\), but
\[
X\cup\{y\}
\]
non-dissociated for every \(y\in Y\setminus X\). Measure how badly exchange can fail as \(|F|\) grows.

---

### Route 5: Probabilistic coloring and the local lemma

**Core idea.** Randomly color the elements with \(k\) colors. For each circuit \(S\), the bad event is that \(S\) is monochromatic, with probability
\[
k^{1-|S|}.
\]
Use the Lovász local lemma, cluster expansion, or entropy compression.

**Key lemma needed.** Derive from proportional dissociation a strong enough bound on the number and overlap pattern of circuits through each vertex, especially short circuits, to make a nonuniform local-lemma criterion converge.

**Why it might work.** Large circuits are individually unlikely to be monochromatic. Only a controlled family of short or highly overlapping circuits should be dangerous.

**Likely failure point.** Proportional independence does not obviously bound circuit degrees. A vertex may lie in enormously many relations even when every induced set has a large dissociated subset.

**Quick test.** For computationally generated high-\(\rho\) sets, count circuits by size and vertex degree. Insert the data into asymmetric or cluster-expansion local-lemma inequalities. If these fail badly even at moderate sizes, a direct random coloring is unlikely to work.

---

### Route 6: Disproof by finite gadgets and arithmetic realization

**Core idea.** Construct finite integer sets with uniformly positive hereditary dissociation ratio but unbounded dissociation chromatic number, then join them by scale separation.

**Key lemma needed.** An arithmetic realization theorem or direct construction producing \(F_i\subseteq\mathbb N\) such that
\[
\rho(F_i)\ge\delta>0
\quad\text{and}\quad
\chi_{\mathrm{dis}}(F_i)\to\infty.
\]
A promising source is the Nešetřil–Rödl–Sales construction for the analogous additive Sidon problem, modified so that all unintended longer \(\{-1,0,1\}\)-relations remain controlled.

**Why it might work.** The analogous additive-combinatorial question is false. General hypergraphs can have a positive hereditary independence ratio without bounded chromatic number, and scale separation makes it possible to combine finite arithmetic gadgets cleanly.

**Likely failure point.** Encoding a desired family of short relations among integers usually creates many unintended long relations. Those extra dependencies may make \(\rho(F_i)\to0\), invalidating the construction. Moreover, arbitrary hypergraphs are unlikely to be realizable as minimal signed-relation hypergraphs in rank one.

**Quick test.** Start from small high-chromatic hypergraphs and formulate integer realization as a SAT/SMT problem:
\[
\sum_{v\in X}a_v=\sum_{v\in Y}a_v
\]
for desired edges, together with inequalities forbidding undesired signed relations up to a chosen support size. Compute the resulting \(\rho(F)\) exactly. Failure even for small gadgets would identify the realization obstruction; successful examples would be highly significant.

---

## 8. Verdict on difficulty

This is a long-standing open structural problem about harmonic-analytic Sidon sets, dating to the early 1980s. By Pisier’s theorem, it is exactly the question whether every Sidon subset of \(\mathbb Z\) is a finite union of quasi-independent sets.

No equivalence to a conjecture such as the Riemann hypothesis is known, but the problem is itself a recognized major open question in the structure theory of Sidon sets. The negative solution of the analogous additive-combinatorial problem in 2024 is substantial evidence that a counterexample may exist, in line with Alon and Erdős’s original skepticism. However, dissociation involves all \(\{-1,0,1\}\)-relations, so controlling unintended long relations is a serious additional obstacle.

The most decisive research target is the uniform finite formulation:

\[
\boxed{
\text{Does }\rho(F)\ge\delta\text{ force }
\chi_{\mathrm{dis}}(F)\le k(\delta)?
}
\]

A positive answer requires a genuinely new bounded-coloring mechanism beyond iterative extraction. A negative answer requires finite arithmetic gadgets with uniformly positive hereditary dissociation ratio and unbounded dissociation chromatic number. Either direction appears difficult and structurally deep.