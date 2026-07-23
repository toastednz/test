# Problem brief: Erdős Problem #1117

## 1. Precise statement

Let \(f:\mathbb C\to\mathbb C\) be a nonzero entire function. For \(r>0\), define its maximum modulus

\[
M_f(r):=\max_{|z|=r}|f(z)|
\]

and its set of maximum-modulus points on the circle of radius \(r\),

\[
S_f(r):=
\left\{
z\in\mathbb C:
|z|=r,\quad |f(z)|=M_f(r)
\right\}.
\]

Define

\[
\nu_f(r):=\#S_f(r),
\]

where distinct points are counted without multiplicity.

Here a **monomial** means a function

\[
f(z)=az^m
\]

with \(a\in\mathbb C\setminus\{0\}\) and \(m\in\mathbb Z_{\ge 0}\). Thus nonzero constants are monomials. The zero function must also be excluded: otherwise every point of every circle is a maximum point. Equivalently, the intended hypothesis is that the Taylor series of \(f\) has at least two nonzero coefficients.

For every nonzero, nonmonomial entire \(f\), \(\nu_f(r)\) is a finite positive integer for every \(r>0\). Indeed, \(\theta\mapsto |f(re^{i\theta})|^2\) is real analytic. If it had infinitely many maximum points, it would be constant in \(\theta\); an entire function having constant modulus on one centered circle must be a monomial.

All limits below are understood as \(r\to\infty\). More formally,

\[
\limsup_{r\to\infty}\nu_f(r)
=
\lim_{R\to\infty}\sup_{r\ge R}\nu_f(r),
\]

and similarly for \(\liminf\), with values in the extended real line.

The problem consists of two existence questions.

### Question 1: unbounded upper limit

Does there exist a nonzero, nonmonomial entire function \(f\) such that

\[
\limsup_{r\to\infty}\nu_f(r)=\infty?
\]

Equivalently:

\[
\forall N\in\mathbb N\ \forall R>0\ \exists r\ge R
\quad \nu_f(r)\ge N.
\]

This question has been answered **yes** by Herzog and Piranian.

### Question 2: divergent lower limit

Does there exist a nonzero, nonmonomial entire function \(f\) such that

\[
\liminf_{r\to\infty}\nu_f(r)=\infty?
\]

Because every \(\nu_f(r)\) is finite and integer-valued, this is equivalent to

\[
\nu_f(r)\longrightarrow\infty \qquad (r\to\infty),
\]

or, fully quantified,

\[
\forall N\in\mathbb N\ \exists R_N>0\ \forall r\ge R_N,
\quad \nu_f(r)\ge N.
\]

This second question remains open.

### Why \(\nu_f(r)\) is finite

Suppose \(S_f(r)\) were infinite. Then the real-analytic function

\[
H_r(\theta):=|f(re^{i\theta})|^2
\]

would attain its maximum at infinitely many points of the compact circle and hence would be constant. Thus \(|f|\) is constant on \(|z|=r\).

By the standard finite-Blaschke-product characterization, the restriction of \(f\) to \(|z|<r\), after normalization by its boundary modulus, is a finite Blaschke product. Since \(f\) extends to an entire function, all nonzero Blaschke factors would introduce poles at the reflected points \(r^2/\overline a\). Hence the only possible zero is at \(0\), and \(f(z)=az^m\). Therefore a nonmonomial entire function has only finitely many maximum points on each circle.

The standard asymptotic reading is forced here: interpreting \(\liminf\nu(r)\) as an infimum over all \(r>0\) would make the second displayed condition impossible, since \(\nu(r)\) is finite at every fixed radius.

---

## 2. What counts as a solution

## A. Complete solution of Question 1

Question 1 is already settled affirmatively. An independent complete proof would have to construct or otherwise prove the existence of a single entire, nonmonomial \(f\) for which

\[
\forall N\ \forall R\ \exists r\ge R:\ \nu_f(r)\ge N.
\]

It is not enough to obtain arbitrarily many maxima on one circle, or to construct a different function for each \(N\).

Since Herzog and Piranian already established this, a rigorous modern resolution may cite their theorem after confirming that their definition of maximum-modulus points and their limiting convention agree with the formulation above.

## B. Complete affirmative solution of Question 2

A complete affirmative solution must give one entire function \(f\) and prove all of the following:

1. **Entirety:** \(f\) is holomorphic on all of \(\mathbb C\).  
   For a series construction \(f(z)=\sum a_nz^n\), this means proving infinite radius of convergence, for example
   \[
   \limsup_{n\to\infty}|a_n|^{1/n}=0.
   \]

2. **Nondegeneracy:** \(f\not\equiv 0\) and \(f\) is not of the form \(az^m\).

3. **Exact global maximality:** for every \(N\), there is \(R_N\) such that for every real \(r\ge R_N\), there are at least \(N\) distinct points \(z_1,\dots,z_N\) on \(|z|=r\) satisfying
   \[
   |f(z_j)|=M_f(r).
   \]

4. **Uniformity over all large radii:** the proof must cover every \(r\ge R_N\), including transition radii between annuli or dominant terms. Exceptional radii are not allowed.

5. **Distinctness:** the \(N\) points must be geometrically distinct. A high-order or degenerate maximum at one point still contributes only \(1\) to \(\nu_f(r)\).

The construction may be explicit, inductive, or existential, but exact equality with the global maximum must be proved. Numerical plots or approximate equality are insufficient.

## C. Complete negative solution of Question 2

Question 2 is existential. Its negation is the universal assertion

\[
\forall f\ \bigl[
f\text{ entire, nonzero, nonmonomial}
\implies
\liminf_{r\to\infty}\nu_f(r)<\infty
\bigr].
\]

Equivalently, one must prove:

\[
\forall f\ \exists K_f\in\mathbb N\ \forall R>0\ \exists r\ge R
\quad \nu_f(r)\le K_f.
\]

The bound \(K_f\) may depend on \(f\). It cannot be uniform over all entire functions, since \(f(z)=1+z^q\) has \(\nu_f(r)=q\) for every \(r>0\).

A single example with bounded \(\nu_f\) is not a counterexample to Question 2: most simple functions already have bounded \(\nu_f\). To disprove the existential statement, one needs a theorem applying to every nonmonomial entire function.

---

## 3. What does not count

The following do not resolve the open second question.

1. **Unboundedness only along a sequence.**  
   Showing
   \[
   \nu_f(r_k)\to\infty
   \]
   for some \(r_k\to\infty\) establishes only the already-solved limsup statement.

2. **A different function for every lower bound.**  
   For example,
   \[
   f_N(z)=1+z^N
   \]
   satisfies \(\nu_{f_N}(r)=N\) for every \(r>0\). This does not produce one function whose number of maxima tends to infinity.

3. **A fixed finite rotational symmetry.**  
   If \(F(z)=g(z^q)\), then
   \[
   \nu_F(r)=q\,\nu_g(r^q),
   \]
   so \(F\) has at least \(q\) maximum points on every circle. A fixed \(q\), however large, does not imply divergence.

4. **Many local maxima.**  
   The problem counts points attaining the global value \(M_f(r)\), not local maxima of \(\theta\mapsto |f(re^{i\theta})|\).

5. **Near-maximal points.**  
   Points satisfying
   \[
   |f(z)|\ge (1-\varepsilon(r))M_f(r)
   \quad\text{or}\quad
   \log|f(z)|\ge \log M_f(r)-o(1)
   \]
   do not count unless exact equality is obtained.

6. **Results outside exceptional radii.**  
   A conclusion valid outside a set of finite logarithmic measure, density zero, or arbitrarily small measure still leaves open whether bad radii occur arbitrarily far out.

7. **Average lower bounds.**  
   Large averages of \(\nu_f(r)\), or many favorable radii in each interval, do not imply a divergent liminf.

8. **Restricted classes only.**  
   Proving impossibility for functions of finite order, lacunary series, canonical products, or another subclass does not disprove the existential problem unless all entire functions are covered.

9. **Conditional arguments.**  
   A result conditional on an unproved growth, zero-distribution, or regularity hypothesis does not settle the unrestricted question.

10. **Counting multiplicity.**  
    A degenerate maximum with high vanishing order of the angular derivative is still one maximum point.

11. **Numerical evidence.**  
    Numerical equality of peak heights cannot certify exact equality, especially when exponentially small perturbations can select a unique global maximum.

---

## 4. Known results and context

### 4.1 Database history

- The problem appears as Problem 2.16 in \([{\rm Ha74}]\), where it is attributed to Erdős.
- Herzog and Piranian \([{\rm HePi68}]\) answered the first question affirmatively:
  there is a nonmonomial entire function \(f\) with
  \[
  \limsup_{r\to\infty}\nu_f(r)=\infty.
  \]
- The second question remains open.
- Glücksam and Pardo-Simón \([{\rm GlPa24}]\) give what the database describes as an “approximate” affirmative answer.

The database excerpt does not state the precise theorem of Glücksam and Pardo-Simón. Therefore no exact quantitative formulation should be attributed to them without consulting the paper. In particular, “approximate” must not be silently upgraded to exact global maximality on every sufficiently large circle. The approximation could concern peak height, exceptional radii, or a related relaxation; its precise hypotheses and conclusion should be extracted directly from the source before being used.

### 4.2 Polynomial and finite-support cases are impossible

Let

\[
p(z)=\sum_{n=m}^{d}a_nz^n,\qquad a_m a_d\ne0,
\]

with at least two nonzero terms, and let \(s=d-m\). Then

\[
H_r(\theta)=|p(re^{i\theta})|^2
\]

is a nonconstant trigonometric polynomial of degree at most \(s\). Its derivative is a nonzero trigonometric polynomial of degree at most \(s\), so it has at most \(2s\) zeros on \([0,2\pi)\). Every global maximum is among those zeros. Hence

\[
\nu_p(r)\le 2(d-m)
\]

for every \(r>0\).

Consequently, any affirmative example for Question 2 must be transcendental entire.

### 4.3 Binomials provide arbitrary fixed lower bounds

If \(m<n\) and \(a,b\ne0\), then

\[
f(z)=az^m+bz^n
\]

has exactly \(n-m\) maximum points on every circle. Indeed, equality in

\[
|az^m+bz^n|
\le |a|r^m+|b|r^n
\]

holds exactly when the two terms have the same phase, which gives \(n-m\) equally spaced solutions.

Thus there is no universal finite bound on \(\nu_f(r)\) independent of \(f\). The open issue is whether one fixed transcendental entire function can realize successively larger exact ties on every sufficiently large circle.

### 4.4 Fixed rotational symmetries

If

\[
F(z)=z^m g(z^q),
\]

then multiplication by \(z^m\) does not change angular modulus and \(z\mapsto z^q\) is \(q\)-to-one on each circle. Therefore

\[
\nu_F(r)=q\,\nu_g(r^q).
\]

This gives a simple mechanism for a fixed number of repeated maxima, but not for symmetry order tending to infinity.

### 4.5 Single-circle behavior is highly flexible

Many maximum points on one circle need not arise from rotational symmetry. Given distinct angles \(\theta_1,\dots,\theta_N\), consider a nonnegative trigonometric polynomial such as

\[
Q(\theta)=\prod_{j=1}^N\bigl(1-\cos(\theta-\theta_j)\bigr)
\]

and choose \(C>\max Q\). Then

\[
H(\theta)=C-Q(\theta)>0
\]

has global maxima exactly at the prescribed angles. By the Fejér–Riesz theorem,

\[
H(\theta)=|P(e^{i\theta})|^2
\]

for some polynomial \(P\).

Thus high \(\nu_f(r)\) at one prescribed radius is not rigid. The difficulty is making the phenomenon persist coherently as \(r\) varies through an unbounded interval.

### 4.6 Relevant classical tools

The following are naturally relevant, though none alone settles the problem:

- maximum modulus principle;
- finite Blaschke-product characterization of analytic functions of constant boundary modulus;
- Fejér–Riesz factorization of nonnegative trigonometric polynomials;
- Hadamard three-circles and convexity of \(\log M_f(r)\);
- Wiman–Valiron theory and central-index analysis;
- canonical products and logarithmic potentials of zero sets;
- real-analytic stratification of critical and equal-value loci;
- Nevanlinna theory and the logarithmic derivative \(zf'(z)/f(z)\).

---

## 5. Traps and edge cases

### 5.1 The zero function and constants

The zero function has infinitely many maximum points on every circle and must be excluded. Nonzero constants must be treated as monomials \(az^0\); otherwise the parenthetical finiteness statement is false.

### 5.2 Angles \(0\) and \(2\pi\) represent the same point

When counting roots of angular equations, use \(\mathbb R/2\pi\mathbb Z\) or a half-open interval such as \([0,2\pi)\).

### 5.3 Maxima are counted without multiplicity

If \(H_r'(\theta)\) has a root of multiplicity \(100\), this still gives only one point unless there are distinct angular locations.

### 5.4 Critical points are not necessarily maxima

At a maximum point \(z=re^{i\theta}\),

\[
\frac{d}{d\theta}|f(re^{i\theta})|^2
=
-2\,\operatorname{Im}\!\left(zf'(z)\overline{f(z)}\right)=0.
\]

The converse is false: this equation also detects minima and other stationary points.

### 5.5 Local maxima are not global maxima

A high-frequency perturbation can create many local peaks while a tiny low-frequency term makes exactly one of them globally highest. This is perhaps the central technical trap.

For example, a dominant \(\cos(q\theta)\) term has \(q\) equal peaks, but adding \(\varepsilon\cos\theta\) typically splits their heights and leaves only one global maximum.

### 5.6 Exact equalities are unstable

If a model has \(q\) equal maxima because of symmetry, a generic arbitrarily small perturbation destroys their equality. Uniform approximation alone preserves strict inequalities and local extrema, but not equality of peak heights.

This is why approximation constructions naturally lead to “near maxima” rather than exact maximum points.

### 5.7 Dominance by a high-frequency term is insufficient

Even if one block of a lacunary series dominates all others in norm, a much smaller nonsymmetric term can determine which one of the nearly equal peaks is globally largest. Error estimates must preserve an exact identity, not merely be relatively small.

### 5.8 Transition radii are unavoidable

An annular construction may produce many maxima well inside each annulus but fail where one dominant block hands over to the next. Since Question 2 has an all-radii quantifier, infinitely many transition circles cannot be discarded.

### 5.9 Positive coefficients tend to give fixed symmetry

If all nonzero coefficients are positive real and the exponent support is \(E\subset\mathbb Z_{\ge0}\), then the triangle inequality is sharp when all phases \(e^{in\theta}\), \(n\in E\), align. The number of such angles is governed by the fixed gcd

\[
\gcd\{n-n_0:n\in E\},
\]

not by radius. Pure phase-alignment constructions therefore tend to yield only fixed-order symmetry.

### 5.10 No uniform negative bound is possible

Any negative theorem must allow the bound to depend on \(f\). The functions \(1+z^q\) have \(\nu(r)=q\) for every \(r\).

### 5.11 Polynomial truncations may misidentify exact ties

A truncation can locate candidate maxima and certify strict gaps away from them. It usually cannot prove that multiple candidate peaks of the full entire function have exactly equal height unless the tail respects a proved identity or symmetry.

---

## 6. Verification hooks

These checks are suitable for symbolic or certified computation.

### 6.1 Angular critical equation

For \(z=re^{i\theta}\), define

\[
H(r,\theta)=|f(re^{i\theta})|^2.
\]

Then

\[
\partial_\theta H(r,\theta)
=
-2\,\operatorname{Im}\!\left(
zf'(z)\overline{f(z)}
\right).
\]

A candidate maximum must satisfy

\[
\operatorname{Im}\!\left(
zf'(z)\overline{f(z)}
\right)=0.
\]

For polynomial truncations, this becomes a trigonometric-polynomial equation that can be solved by root isolation rather than floating-point sampling.

### 6.2 Fourier/autocorrelation representation

If

\[
f(z)=\sum_{n=0}^\infty a_nz^n,
\]

then

\[
H(r,\theta)
=
\sum_{k\in\mathbb Z}c_k(r)e^{ik\theta},
\]

where for \(k\ge0\),

\[
c_k(r)=
\sum_{n=0}^\infty
a_{n+k}\overline{a_n}\,r^{2n+k},
\qquad
c_{-k}(r)=\overline{c_k(r)}.
\]

This permits direct computation of the angular spectrum and detection of low-frequency perturbations that split nominally equal peaks.

### 6.3 Certified counting for polynomials

For a polynomial \(p\) with rational or algebraic coefficients and an algebraic radius \(r\):

1. form the trigonometric polynomial \(H_r(\theta)=|p(re^{i\theta})|^2\);
2. transform it using \(x=\cos\theta\), \(y=\sin\theta\), \(x^2+y^2=1\);
3. isolate all roots of \(\partial_\theta H_r\);
4. evaluate \(H_r\) at those roots with exact algebraic arithmetic or interval enclosures;
5. count the distinct roots attaining the largest value.

For a whole radius interval, the condition \(\nu_p(r)\ge N\) is semialgebraic and can in principle be attacked by cylindrical algebraic decomposition, although complexity grows quickly.

### 6.4 Tail certification for entire series

For \(P_L(z)=\sum_{n\le L}a_nz^n\), obtain a uniform bound

\[
T_L(r)\ge
\sup_{|z|=r}|f(z)-P_L(z)|
\]

from the coefficient tail. Then

\[
\bigl||f(z)|-|P_L(z)|\bigr|\le T_L(r).
\]

This can certify that no maximum occurs on arcs where \(P_L\) lies more than \(2T_L(r)\) below its candidate peak. It cannot by itself certify equality among different candidate peaks.

Derivative tail bounds can similarly certify the number of local extrema in specified arcs.

### 6.5 Baseline test cases

Any implementation should reproduce:

- \(f(z)=az^m\): every point is a maximum; excluded case.
- \(f(z)=1+z^q\): exactly \(q\) maxima for every \(r>0\).
- \(f(z)=z^m(1+z^q)\): exactly \(q\) maxima.
- \(f(z)=g(z^q)\): numerically and symbolically verify
  \[
  \nu_f(r)=q\nu_g(r^q).
  \]
- A perturbed model \(1+z^q+\varepsilon z\): test how a tiny low-frequency term splits the \(q\) equal peaks.

### 6.6 Annular-transition tests

For any proposed block construction:

1. identify the radii where two consecutive blocks have comparable size;
2. compute all global maxima over a dense mesh of those transition intervals;
3. use certified root isolation at suspicious radii;
4. track whether peak heights cross, split, or become unequal;
5. test whether the claimed lower bound survives throughout the entire transition interval.

Failures are most likely at these handover radii.

### 6.7 Symmetry verification

If exact equality is claimed from rotational symmetry, verify an identity of the form

\[
|f(e^{2\pi i/q}z)|=|f(z)|
\]

for all relevant \(z\), not merely numerically. For holomorphic functions, a stronger identity such as

\[
f(e^{2\pi i/q}z)=e^{i\alpha}f(z)
\]

can be checked coefficientwise.

A symmetry valid only approximately or only for a truncation does not certify exact maximum multiplicity for the full function.

---

## 7. Attack routes

## Route 1: Annular holomorphic patching with exact maximum templates

**Direction:** Affirmative.

Construct \(f\) inductively on expanding annuli. On the \(k\)-th annulus, approximate a holomorphic model whose modulus has at least \(N_k\to\infty\) equal global maxima on every centered circle. Use Runge-, Arakelian-, or chaplet-type approximation while keeping previous stages nearly unchanged.

### Key lemma needed

An **exact-max patching lemma**: given an existing entire approximation and an annulus, produce a correction such that, on every circle in that annulus,

- at least \(N\) designated branches attain exactly the same modulus;
- this common value is strictly larger than the modulus elsewhere;
- the property survives on overlap regions with adjacent annuli.

### Why it might work

Holomorphic approximation is powerful on separated annular or sectorial sets, and strict inequalities away from the prescribed peaks are robust. The approximate theorem of Glücksam and Pardo-Simón may provide useful architecture for such an exhaustion.

### Most likely failure

Exact equality of several peak heights is not open under approximation. A tiny correction can select one peak. Imposing equality along a continuum of radii may amount to imposing an analytic identity too rigid to localize to one annulus.

### Quick blocking test

Attempt the finite-stage problem with a polynomial correction: prescribe \(N\) moving angles \(\theta_j(r)\) and solve

\[
|p(re^{i\theta_1(r)})|
=\cdots=
|p(re^{i\theta_N(r)})|
\]

throughout an interval of \(r\), together with strict dominance elsewhere. Symbolic elimination can reveal whether the constraints force a global rotational symmetry or another rigid functional identity.

---

## Route 2: Canonical products with regular polygonal zero shells

**Direction:** Affirmative.

Arrange zeros in large regular polygons on successive radial shells. Factors such as

\[
1-\left(\frac zR\right)^q
\]

have exact \(q\)-fold angular structure. A canonical product with shell sizes \(q_k\to\infty\) might make the \(k\)-th shell control the angular maximum on a corresponding annulus.

### Key lemma needed

A shell-neutralization lemma showing that earlier and later factors contribute either:

- exactly radially on the active annulus, or
- an angular perturbation that preserves equality of at least \(q_k\) global peaks,

including during transitions between shells.

### Why it might work

The logarithm of the modulus of a canonical product is a sum of logarithmic potentials. Radially separated shells can dominate in different regions, and regular polygons yield explicitly computable Fourier modes.

### Most likely failure

A remote shell is only approximately radial, not exactly radial. Its tiny low-frequency angular component can split the equal peaks created by the active shell. Also, increasing exact rotational symmetries are arithmetically incompatible: the global symmetry order is controlled by a fixed gcd of all active exponents.

### Quick blocking test

For finite products

\[
P_K(z)=\prod_{j=1}^K
\left(1-\left(\frac z{R_j}\right)^{q_j}\right),
\]

compute the Fourier expansion of \(\log|P_K(re^{i\theta})|\) and certify \(\nu_{P_K}(r)\) across each transition interval. Check whether older shells produce a unique preferred peak even when their contribution is extremely small.

---

## Route 3: Lacunary series and Newton-polygon/central-index engineering

**Direction:** Affirmative.

Choose a lacunary series

\[
f(z)=\sum_k a_k z^{n_k}
\]

so that different high-frequency blocks dominate on consecutive radius ranges. Wiman–Valiron or Newton-polygon analysis can locate the dominant exponents and quantify tail errors.

### Key lemma needed

A phase-locking lemma guaranteeing that a dominant block with frequency gap \(q_k\) produces \(q_k\) **equal global** maxima despite all nondominant terms, uniformly over the whole dominance interval.

A successful version must be exact, not perturbative.

### Why it might work

Large exponent gaps naturally create many angular oscillations. Coefficients and phases can be tuned at transition radii, and lacunarity gives very strong control of all omitted terms.

### Most likely failure

Dominance in absolute size preserves local peaks but not equal peak heights. A term smaller by an arbitrarily large factor can still distinguish the peaks. If equality is forced by simultaneous phase alignment, the relevant number of alignments is usually controlled by a fixed gcd of the exponent support.

### Quick blocking test

Study models with three or four terms and widely separated exponents. Compute the global peak heights exactly or with certified intervals as the smallest term tends to zero. If generic arbitrarily small perturbations leave only one global maximum, then any successful construction needs a nonperturbative equality mechanism rather than mere lacunarity.

---

## Route 4: Real-analytic rigidity of persistent global-max branches

**Direction:** Disproof.

Study

\[
H(r,\theta)=|f(re^{i\theta})|^2
\]

as a real-analytic function on \((0,\infty)\times\mathbb S^1\). The global maxima form a subset of the critical locus

\[
\partial_\theta H(r,\theta)=0.
\]

If every sufficiently large circle has many global maxima, there must be many branches of the critical locus with identical value.

### Key lemma needed

A rigidity theorem of the following type:

> If a real-analytic function arising as \(|f(re^{i\theta})|^2\) has sufficiently many equal global-max branches throughout an interval of radii, then \(f\) has a nontrivial rotational covariance
> \[
> f(\omega z)=c\,f(z),\qquad |\omega|=|c|=1.
> \]

A strengthened iteration would need to show that unbounded lower multiplicity forces symmetries of unbounded order, hence forces \(f\) to be a monomial.

### Why it might work

Equality of several analytic critical values over a continuum is much more rigid than coincidence at isolated radii. The all-radii condition in the liminf problem is the main possible source of a negative theorem.

### Most likely failure

The relevant branches can be born, die, and exchange at bifurcation radii. The number of maxima may increase only at larger and larger scales, so no fixed compact annulus contains unbounded complexity. Equal-value branches need not arise from rotations.

### Quick blocking test

Classify polynomial or finite exponential-sum examples in which several global maxima persist over an open radius interval. Use resultants to eliminate \(r,\theta_i,\theta_j\) from the criticality and equal-value equations. Determine whether all persistent examples found are explained by coefficient symmetries.

---

## Route 5: Fourier/autocorrelation rigidity

**Direction:** Primarily disproof, with possible constructive implications.

Use the exact Fourier expansion

\[
|f(re^{i\theta})|^2
=
\sum_{k\in\mathbb Z}c_k(r)e^{ik\theta},
\qquad
c_k(r)=\sum_{n\ge0}a_{n+k}\overline{a_n}r^{2n+k}.
\]

Try to translate many equal global maxima into constraints on the low Fourier coefficients \(c_k(r)\). Since each \(c_k(r)\) is real analytic in \(r\), constraints valid for intervals of radii may force coefficient identities.

### Key lemma needed

A theorem connecting a large number of global maxima, uniformly over a radius interval, to vanishing or exact dependence of a substantial initial segment of the angular Fourier spectrum. One would then seek to deduce that the Taylor support of \(f\) lies in increasingly sparse congruence classes, ultimately forcing a monomial.

### Why it might work

The special radial dependence of \(c_k(r)\) couples the angular profiles at different radii. Arbitrary trigonometric polynomials can have many maxima, but not every one-parameter family of them comes from a single entire function.

### Most likely failure

Many maxima at one radius impose almost no useful low-frequency vanishing. They may be irregularly placed or clustered. Fejér–Riesz factorization explicitly shows that arbitrary finite maximum sets can occur on a single circle.

### Quick blocking test

Use

\[
H(\theta)=C-\prod_{j=1}^N(1-\cos(\theta-\theta_j))
\]

with arbitrary or clustered \(\theta_j\), and inspect its low Fourier coefficients. Any proposed lemma saying “many maxima imply low modes are small or zero” should first survive this family. The essential extra hypothesis must involve persistence in \(r\) and the autocorrelation form of the coefficients.

---

## Route 6: Logarithmic derivative, argument principle, and value distribution

**Direction:** Disproof or structural reduction.

At a maximum point \(z=re^{i\theta}\), \(f(z)\ne0\) and

\[
\operatorname{Im}\!\left(\frac{zf'(z)}{f(z)}\right)=0.
\]

Thus maximum points lie among intersections of the circle with the real-level locus of the meromorphic function

\[
G(z)=\frac{zf'(z)}{f(z)}.
\]

One can combine this with the requirement that all selected points have the same value of \(\log|f|\).

### Key lemma needed

A bound, valid on arbitrarily large radii, on the number of equal-height global maxima in terms of zeros, poles, or growth data of \(G\), strong enough to imply

\[
\exists K_f\ \forall R\ \exists r\ge R:\ \nu_f(r)\le K_f.
\]

Alternatively, prove that persistent large multiplicity forces an impossible concentration of real-axis crossings or logarithmic-derivative values.

### Why it might work

The argument principle and Nevanlinna theory can control average angular behavior of logarithmic derivatives. Maximum points impose both a differential condition and a global level condition, which may be significantly more restrictive than criticality alone.

### Most likely failure

Nevanlinna estimates are averaged and tolerate exceptional radii, while the problem is about exact global ties. Transcendental logarithmic derivatives can have arbitrarily complicated level sets, and many real crossings do not imply many global maxima.

### Quick blocking test

For canonical products and lacunary series, compute:

- the number of zeros of
  \[
  \operatorname{Im}(zf'(z)\overline{f(z)})
  \]
  on \(|z|=r\);
- the actual number \(\nu_f(r)\);
- the number of zeros and poles of \(zf'/f\) in nearby disks.

If critical-point counts are enormous while \(\nu_f(r)\) remains \(1\), then any viable argument must use equal-height information essentially.

---

## 8. Verdict on difficulty

The first question is **not open**: Herzog and Piranian answered it affirmatively.

The second question is a long-standing and genuinely difficult open problem, originating at least in the late 1960s/early 1970s. Its difficulty is not primarily producing many angular peaks; high-frequency blocks and fixed symmetries do that easily. The obstacle is producing **many exactly equal global peaks on every sufficiently large circle**, including infinitely many transition regions.

No established equivalence with a famous conjecture such as the Riemann hypothesis is known from the supplied context, and none should be asserted. Nevertheless, the problem appears structurally hard because:

- exact equality is unstable under perturbation;
- approximation methods naturally yield near-maxima, not exact maxima;
- symmetry gives only fixed multiplicity unless a new mechanism allows the effective symmetry order to grow with radius;
- a negative result would require a universal rigidity theorem for all entire functions;
- single-circle configurations are extremely flexible, so any rigidity must exploit the coupled dependence on radius.

The “approximate” result of Glücksam and Pardo-Simón is likely the closest modern guide, but its precise theorem must be checked carefully. The central research question is whether its relaxed conclusion can be upgraded to exact equality with no exceptional large radii, or whether the failure of such an upgrade can be converted into a universal obstruction.