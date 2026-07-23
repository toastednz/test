# ROUND 2 PROBLEM BRIEF: ERDŐS PROBLEM #203

## 1. PRECISE STATEMENT

Let \(\mathbb N_0=\{0,1,2,\ldots\}\). Determine whether the following existential assertion is true:

\[
\exists m\in \mathbb Z_{\ge 1}\quad \gcd(m,6)=1
\quad\text{such that}\quad
\forall (k,\ell)\in\mathbb N_0^2,\;
2^k3^\ell m+1\ \text{is not prime}.
\]

Since every number \(2^k3^\ell m+1\) is at least \(2\), “not prime” here means composite.

Equivalently, the desired \(m\) must satisfy

\[
\forall k,\ell\ge 0,\quad \exists d=d(k,\ell)
\quad\text{with}\quad
1<d<2^k3^\ell m+1,\qquad
d\mid 2^k3^\ell m+1.
\]

The divisor \(d\), and its prime factors, may depend on \((k,\ell)\).

### 1.1 Immediate boundary observations

Because \(\gcd(m,6)=1\), \(m\) is odd.

- If \(m=1\), then the term with \(k=\ell=0\) is \(2\), so \(m=1\) is not a solution.
- Hence every solution must have \(m>1\).
- For every odd \(m>1\) and every \(\ell\ge 0\),
  \[
  3^\ell m+1
  \]
  is an even integer greater than \(2\). Thus all terms with \(k=0\) are automatically composite.
- The substantive range is therefore \(k\ge 1\), though the formal statement includes \(k=0\).

Setting \(\ell=0\) shows that a solution must in particular be a Sierpiński number:

\[
2^k m+1\ \text{is composite for every }k\ge 0.
\]

More strongly, for every \(\ell\ge 0\), the odd integer \(3^\ell m\) must itself be a Sierpiński number.

### 1.2 Standard reading and alternatives

The database statement explicitly says \(k,\ell\ge 0\), so the standard reading is that the quantifiers are independent and include zero. A version with \(k,\ell\ge 1\) would be strictly weaker, though the \(k=0\) boundary is automatic once \(m>1\).

There is no ambiguity about the sign of \(m\): the condition \(m\ge 1\) excludes negative integers.

---

## 2. THE FINITE LATTICE-COVERING FORMALISM

This is the central constructive formalism, but an important logical qualification is required.

### 2.1 Prime divisibility cosets

Fix a prime \(p\ge 5\). Let

\[
H_p=\langle 2,3\rangle\le \mathbb F_p^\times.
\]

Define

\[
o_{2,p}=\operatorname{ord}_p(2),\qquad
o_{3,p}=\operatorname{ord}_p(3),
\]

and

\[
h_p=|H_p|
=\operatorname{lcm}(o_{2,p},o_{3,p}).
\]

The equality follows because \(\mathbb F_p^\times\) is cyclic.

Define the homomorphism

\[
\phi_p:\mathbb Z^2\longrightarrow H_p,\qquad
\phi_p(k,\ell)=2^k3^\ell\pmod p.
\]

Its kernel is the rank-two lattice

\[
L_p=\{(k,\ell)\in\mathbb Z^2:2^k3^\ell\equiv1\pmod p\},
\]

and

\[
[\mathbb Z^2:L_p]=h_p.
\]

For \(t\in H_p\), define the affine coset

\[
C(p,t)=\{(k,\ell)\in\mathbb Z^2:2^k3^\ell\equiv t\pmod p\}.
\]

This is one coset of \(L_p\), of natural density \(1/h_p\) in \(\mathbb Z^2\).

For fixed \(m\) with \(p\nmid m\),

\[
p\mid 2^k3^\ell m+1
\iff
2^k3^\ell\equiv -m^{-1}\pmod p.
\]

Thus \(p\) is useful only if \(-m^{-1}\in H_p\), and then it covers exactly the coset

\[
C\bigl(p,-m^{-1}\bigr).
\]

### 2.2 Linear-character representation

Choose a generator \(g_p\) of \(H_p\), and write

\[
2=g_p^{a_p},\qquad 3=g_p^{b_p}.
\]

Because \(g_p\) generates \(\langle2,3\rangle\),

\[
\gcd(a_p,b_p,h_p)=1.
\]

If \(t=g_p^{c_p}\), then

\[
C(p,t)=
\{(k,\ell)\in\mathbb Z^2:
a_pk+b_p\ell\equiv c_p\pmod{h_p}\}.
\]

Thus every prime gives one affine cyclic character constraint.

When \(h_p=q\) is prime and both \(2\) and \(3\) have order \(q\), this is literally an affine line in \(\mathbb F_q^2\). More generally, if \(q\mid h_p\), reduction of the character modulo \(q\) gives an affine-line shadow in \(\mathbb F_q^2\). Covering the shadows is necessary but not sufficient: the full congruence modulo \(h_p\) contains additional lifting conditions.

### 2.3 Finite-cover sufficiency

Suppose there are distinct primes \(p_1,\dots,p_s\ge5\) and targets \(t_i\in H_{p_i}\) such that

\[
\mathbb Z^2=\bigcup_{i=1}^s C(p_i,t_i).
\]

Choose \(m\) by the Chinese remainder theorem so that

\[
m\equiv -t_i^{-1}\pmod{p_i}\qquad(1\le i\le s)
\]

and, for example,

\[
m\equiv1\pmod6.
\]

Choose the representative \(m\) large enough that

\[
m>\max_i p_i.
\]

Then for every \(k,\ell\ge0\), some \(p_i\) divides \(2^k3^\ell m+1\), and

\[
2^k3^\ell m+1>p_i.
\]

Hence every term is composite. This gives a complete affirmative solution.

The target cosets are independently selectable across distinct primes because CRT imposes no compatibility between different moduli.

### 2.4 The finite-cover formulation is not known to be equivalent to the original problem

The statement in the initial research notes that the original problem is “equivalent” to finding a finite lattice cover requires correction.

What is true is:

> An \(m\) for which a fixed finite set of primes supplies a divisor of every term is equivalent to a finite cover by the corresponding affine lattices.

Indeed, if a finite set of primes divides all terms, then primes \(2\) and \(3\) can be discarded after restricting to \(k,\ell\ge1\), and periodicity extends the resulting cover from the positive quadrant to all of \(\mathbb Z^2\).

What is not established is:

> Every \(m\) whose terms are all composite must admit a finite set of covering primes.

An all-composite family could, in principle, use infinitely many different prime factors without any finite subcover. Compactness does not automatically produce a finite subcover: an infinite family of periodic sets can cover every integer point while failing to have a finite subcover.

Therefore:

- a finite lattice-cover certificate is a fully valid sufficient construction;
- ruling out finite covers does **not** by itself disprove the original problem.

---

## 3. WHAT COUNTS AS A COMPLETE SOLUTION

### 3.1 Complete affirmative solution

A complete proof of “yes” must exhibit a specific \(m\ge1\), \(\gcd(m,6)=1\), and rigorously prove

\[
\forall k,\ell\ge0,\quad 2^k3^\ell m+1\text{ is composite}.
\]

Acceptable proof formats include the following.

#### Format A: finite prime-cover certificate

Provide:

1. Distinct primes \(p_1,\dots,p_s\ge5\).
2. One target \(t_i\in H_{p_i}\) for each prime.
3. A proof that
   \[
   \mathbb Z^2=\bigcup_i C(p_i,t_i).
   \]
4. A CRT construction of \(m\) satisfying
   \[
   m\equiv-t_i^{-1}\pmod{p_i},\qquad m\equiv1\text{ or }5\pmod6.
   \]
5. A choice of representative with \(m>\max p_i\), or separate verification that every displayed divisor is proper.

For finite verification, let

\[
A=\operatorname{lcm}_i o_{2,p_i},\qquad
B=\operatorname{lcm}_i o_{3,p_i}.
\]

It is enough to verify coverage of every pair in

\[
\mathbb Z/A\mathbb Z\times\mathbb Z/B\mathbb Z.
\]

An exact verification using the smaller quotient

\[
\mathbb Z^2/\bigcap_i L_{p_i}
\]

is equally valid.

#### Format B: hybrid algebraic and congruence certificate

One may specify a periodic set \(S\subseteq\mathbb N_0^2\) on which compositeness follows from an algebraic factorization, and use prime cosets to cover the complement. The proof must establish:

- the algebraic factorization for every \((k,\ell)\in S\);
- properness of the factors, including all smallest cases;
- exact coverage of every \((k,\ell)\notin S\);
- compatibility between the required shape of \(m\) and all CRT residues.

#### Format C: non-covering direct proof

Any other rigorous construction is acceptable, even if infinitely many different prime factors are used, provided all exponent pairs are handled.

### 3.2 Complete negative solution

A complete proof of “no” must establish

\[
\forall m\ge1,\quad
\gcd(m,6)=1
\implies
\exists k,\ell\ge0
\quad\text{such that}\quad
2^k3^\ell m+1\text{ is prime}.
\]

No single explicit \(m\) can disprove the existential statement. Showing that one candidate \(m\) fails only eliminates that candidate.

A finite computation over \(m\le M\) is not a disproof unless accompanied by a theorem excluding all \(m>M\).

A proof that no finite affine-lattice cover exists would still be insufficient unless one also proves that every all-composite \(m\) must have such a finite cover.

---

## 4. WHAT DOES NOT COUNT

The following do not resolve the problem.

1. Finding an \(m\) for which all terms are composite only for
   \[
   0\le k,\ell\le X.
   \]

2. Verifying a candidate numerically for millions of pairs without a periodic or algebraic proof.

3. Showing that \(m\) is a Sierpiński number, i.e. treating only \(\ell=0\).

4. Treating only finitely many values of \(\ell\), or all \(\ell\) in a proper residue subset.

5. Covering a set of exponent pairs of density \(1-o(1)\), or density \(99.999\%\).

6. Obtaining nominal reciprocal mass
   \[
   \sum_i\frac1{h_{p_i}}>1.
   \]
   This is necessary but not sufficient because of forced overlaps and lifting obstructions.

7. Covering only a coarse projection such as \(\mathbb F_q^2\). A shadow line is generally larger than the full prime coset.

8. Ruling out one finite prime pool, all primes below a bound, all \(5040\)-compatible primes, or all smooth-index primes below \(2\cdot10^6\).

9. Proving that no finite covering certificate exists, without bridging the finite-cover gap described above.

10. Using the same prime for two different target cosets. A fixed \(m\) determines only one target \(-m^{-1}\pmod p\).

11. Producing CRT residues for \(m\) while also requiring \(m=x^r\), but failing to check that every residue is an \(r\)-th power.

12. Taking \(m=4x^4\). This violates \(\gcd(m,6)=1\).

13. A conditional result under GRH, \(abc\), Schinzel’s hypothesis, Bateman–Horn, or an unproved prime-distribution statement.

14. Heuristics suggesting that prime terms should occur infinitely often.

---

## 5. KNOWN RESULTS, REUSABLE LEMMAS, AND CONTEXT

## 5.1 Sierpiński context

A positive odd integer \(n\) such that \(n2^k+1\) is composite for every \(k\ge1\) is called a Sierpiński number. The classical example is \(78557\), with a finite covering using primes

\[
3,5,7,13,19,37,73.
\]

Any solution to the present problem must have every \(3^\ell m\) Sierpiński.

The classical covering for \(78557\) does not lift directly to the two-dimensional problem. Once \(\ell\ge1\), the prime \(3\) cannot divide \(2^k3^\ell m+1\). The total two-dimensional mass of the remaining covering primes is

\[
\frac14+\frac16+\frac1{12}+\frac1{18}
+\frac1{36}+\frac1{36}
=\frac{11}{18}<1.
\]

Thus arbitrary retargeting of those non-\(3\) primes cannot cover \(\mathbb Z^2\).

The database also mentions broader questions involving
\[
p_1^{k_1}\cdots p_r^{k_r}m+1
\]
for distinct fixed primes \(p_i\), and a variant involving products \(q_1\cdots q_r m+1\) with \(q_i\equiv1\pmod4\). The latter has the trivial choice \(m=1\) if at least one \(q_i\) is required, because the product is \(1\pmod4\) and its successor is an even integer greater than \(2\). Some missing side condition was probably intended.

## 5.2 Necessary mass condition

For a finite cover by prime cosets,

\[
1\le\sum_{p\in\mathcal P}\frac1{h_p}.
\]

This is only the union bound. Equality or slight excess is generally inadequate because intersections are forced.

For an algebraic set of density \(\delta\) together with prime cosets covering its complement, one necessarily has

\[
\sum_{p\in\mathcal P}\frac1{h_p}\ge1-\delta,
\]

again without accounting for overlaps or residue-shape restrictions.

## 5.3 Computed order data

The reliable computation gives

\[
\sum_{\substack{5\le p<10^5\\p\text{ prime}}}
\frac1{\operatorname{lcm}(\operatorname{ord}_p(2),\operatorname{ord}_p(3))}
=2.492\ldots
\]

Thus a simple total-density obstruction is unavailable.

Important contributors are:

\[
\begin{array}{c|c|c|c}
p&o_{2,p}&o_{3,p}&h_p\\ \hline
5&4&4&4\\
7&3&6&6\\
11&10&5&10\\
23&11&11&11\\
13&12&3&12\\
17&8&16&16\\
19&18&18&18\\
47&23&23&23\\
29&28&28&28\\
31&5&30&30\\
71&35&35&35\\
37&36&18&36\\
73&9&12&36\\
41&20&8&40\\
43&14&42&42\\
431&43&43&43\\
97&48&48&48\\
53&52&52&52\\
59&58&29&58\\
61&60&10&60\\
67&66&22&66\\
601&75&75&75\\
79&39&78&78\\
83&82&41&82\\
167&83&83&83\\
89&11&88&88\\
191&95&95&95\\
193&96&96&96\\
101&100&50&100\\
103&51&102&102
\end{array}
\]

Examples of exact prime-order line geometry include:

- \(p=23\): \(h_p=11\), and \(3\equiv2^8\pmod{23}\), so its cosets are
  \[
  k+8\ell\equiv c\pmod{11}.
  \]
- \(p=47\): exact lines modulo \(23\).
- \(p=431\): exact lines modulo \(43\).
- \(p=167\): exact lines modulo \(83\).

Primes such as \(89\) have a useful \(11\)-shadow but impose a full congruence modulo \(88\), not merely a line modulo \(11\).

## 5.4 The \(2\)-\(3\)-smooth-index pool is insufficient by itself

For primes \(p<2\cdot10^6\) such that both \(o_{2,p}\) and \(o_{3,p}\) are \(2\)-\(3\)-smooth, the computed pool consists of the following \(31\) primes, listed with \(h_p\):

\[
\begin{aligned}
&5(4),7(6),13(12),17(16),19(18),37(36),73(36),97(48),\\
&193(96),109(108),577(144),163(162),433(216),257(256),\\
&769(384),487(486),1153(576),1297(648),2593(648),3889(648),\\
&1459(1458),3457(1728),2917(2916),18433(4608),10369(5184),\\
&331777(5184),139969(5832),746497(23328),1990657(31104),\\
&466561(46656),1492993(746496).
\end{aligned}
\]

Their total mass is approximately

\[
0.7493<1.
\]

Therefore this bounded smooth-index pool cannot cover \(\mathbb Z^2\) by itself. This does not rule out further smooth-index primes above the search bound.

## 5.5 The \(q\)-cohort obstruction

A reusable lemma proved in the first-round work is the following.

> **Cohort lemma.**  
> Let a finite affine-lattice cover of \(\mathbb Z^2\) by the cyclic-character cosets arising from selected primes be inclusion-minimal. If a prime \(q\) divides \(h_p\) for one selected prime \(p\), then at least \(q\) selected indices \(h_{p'}\) are divisible by \(q\).

When exactly \(q\) selected cyclic-character cosets have index divisible by \(q\), their reductions to \(\mathbb F_q^2\) must form a parallel affine-line pencil.

Consequences:

- \(p=47\), with \(23\mid h_p\), cannot be inserted as an isolated patch. A minimal cover containing it requires at least \(23\) selected indices divisible by \(23\).
- \(p=431\) similarly forces a cohort of at least \(43\).
- \(p=167\) forces a cohort of at least \(83\).

This decisively kills the original idea of adding a few large-prime-factor line primes to repair a smooth residual.

For hybrid algebraic covers, the generalized coset-cover version must be reapplied with the algebraic cosets included. The parallel-line conclusion is specific to cyclic \(q\)-quotient shadows and cannot simply be copied to a subgroup such as \(q\mathbb Z^2\), whose quotient has rank two.

A practical necessary test is iterative cohort pruning: repeatedly delete every candidate whose index contains a prime \(q\) for which fewer than \(q\) surviving candidate sets have index divisible by \(q\). Any candidate pool killed by this process cannot contain an inclusion-minimal cover.

## 5.6 Exact overlap obstructions

The small primes \(5,7,11\) have incompatible parity characters:

- \(p=5\) has parity shadow of type \(k+\ell=c\);
- \(p=7\) has parity shadow of type \(\ell=c\);
- \(p=11\) has parity shadow of type \(k=c\).

Their intersections cannot all be avoided.

The first-round work proved:

- any chosen \(p=5\) and \(p=7\) cosets overlap in density \(1/24\);
- the combined forced loss among \(p=5,7,11\) is at least
  \[
  \frac{3}{40}.
  \]

Hence any pool containing all three must have total nominal mass at least

\[
1+\frac{3}{40}=\frac{43}{40}=1.075.
\]

This explains why \(5040\)-compatible pools of mass only \(1.02\)–\(1.03\) cannot work when they contain \(5,7,11\).

A particular \(22\)-prime coarse-pencil construction had total mass

\[
\frac{75883}{75600}\approx1.00374.
\]

The unavoidable \(p=5,p=7\) overlap already forces it below full coverage. Any enlargement retaining that pool must add at least

\[
\frac{25}{24}-\frac{75883}{75600}
=\frac{2867}{75600}
\approx0.037923
\]

of nominal mass merely to clear this first obstruction.

## 5.7 Capacity bounds

For \(A\ge1\), define the finite prime set

\[
\mathcal P_2(A)=
\{p\ge5:p\text{ prime and }o_{2,p}\mid A\}.
\]

It is finite because every such \(p\) divides \(2^A-1\). Define

\[
C_2(A)=\sum_{p\in\mathcal P_2(A)}\frac1{h_p}.
\]

Any prime-coset cover whose selected primes all have \(o_{2,p}\mid A\) must satisfy

\[
C_2(A)\ge1.
\]

Similarly define \(C_3(B)\) using primes with \(o_{3,p}\mid B\).

The proved computation

\[
C_2(60)=\frac{4529}{6600}<1
\]

shows that no choice of the second period \(B\) can produce a cover with \(k\)-period dividing \(60\).

These capacities should be checked before any exact set-cover search.

## 5.8 Correct algebraic factorization

The initial suggestion \(m=4x^4\) is invalid because \(m\) would be even.

The valid Sophie Germain construction is:

\[
m=x^4,\qquad \gcd(x,6)=1,\qquad x>1.
\]

If

\[
k\equiv2\pmod4,\qquad \ell\equiv0\pmod4,
\]

then

\[
b=2^{(k-2)/4}3^{\ell/4}x
\]

is an integer greater than \(1\), and

\[
2^k3^\ell m+1=4b^4+1
=(2b^2-2b+1)(2b^2+2b+1).
\]

Thus this algebraically covers one residue class of density \(1/16\).

If prime cosets are used as well, the residue demanded of \(m=x^4\) modulo every selected \(p\) must be a fourth power:

\[
-t_p^{-1}\in(\mathbb F_p^\times)^4.
\]

Equivalently, one must choose a root \(r_p\) with

\[
r_p^4\equiv-t_p^{-1}\pmod p
\]

and then apply CRT to the roots \(x\equiv r_p\pmod p\), not merely to \(m\).

## 5.9 Dead or presently blocked routes

The following specific approaches have already been diagnosed.

1. **A barely-supercritical \(5040\)-torus pool:** blocked by exact capacity and forced-overlap inequalities.

2. **Isolated use of \(23\)-, \(43\)-, or \(83\)-shadow line primes:** blocked by the cohort lemma.

3. **The bounded \(2\)-\(3\)-smooth-index pool:** total mass \(0.7493<1\).

4. **The classical \(78557\) Sierpiński covering:** after losing \(p=3\), total two-dimensional mass is only \(11/18\).

5. **Single equal-order families:** fewer than \(q\) available exact lines cannot cover \(\mathbb F_q^2\); exactly \(q\) lines would have to be parallel.

6. **Common-slope lifting with the currently highlighted primes:** the required discrete-log slopes are incompatible.

7. **Simultaneous use of Bang–Zsigmondy:** Zsigmondy supplies primitive divisors of one exponential difference, but does not supply common primitive divisors of \(2^A-1\) and \(3^B-1\), nor the necessary discrete-log slopes.

8. **The natural mixed pool highlighted in Round 1:** it fails a parity-projected covering inequality even after adjoining primes such as \(61\) and \(89\).

9. **Coarse projective pencils modulo \(5\) and \(7\):** valid at the shadow level, but their lifts waste too much mass and do not cover the full character quotient.

---

## 6. TRAPS AND EDGE CASES

1. **Finite cover versus original problem.** A finite cover proves “yes”; nonexistence of finite covers does not prove “no.”

2. **The \(k=0\) boundary.** It is automatically composite for \(m>1\), but this does not reduce a finite periodic covering problem: every residue class modulo a finite \(k\)-period has representatives with \(k\ge1\).

3. **The \(m=1\) case.** It fails because \(m+1=2\).

4. **Primes \(2\) and \(3\).** The lattice formalism requires \(p\ge5\). For \(k,\ell\ge1\), no term is divisible by \(2\) or \(3\).

5. **A prime can be used only once.** Different target cosets for the same prime are incompatible with a fixed \(m\).

6. **The target sign and inverse.** The correct congruence is
   \[
   m\equiv-t^{-1}\pmod p.
   \]

7. **Not every affine congruence is available.** The target must lie in \(H_p=\langle2,3\rangle\), and the linear coefficients are fixed by the discrete logs of \(2\) and \(3\).

8. **The index is \(h_p\), not \(o_{2,p}o_{3,p}\).**
   \[
   h_p=\operatorname{lcm}(o_{2,p},o_{3,p}).
   \]

9. **Rectangular periods versus actual quotient.** The finite rectangle uses
   \[
   A=\operatorname{lcm}o_{2,p},\quad B=\operatorname{lcm}o_{3,p},
   \]
   but the more economical quotient is determined by \(\bigcap L_p\).

10. **Shadows are not lifts.** A line modulo \(q\mid h_p\) is only the projection of the full coset.

11. **Nominal mass is not union density.** Pairwise and higher intersections can be forced by low-order projections.

12. **Cohort counting must be done after removing redundant sets.** Adding unused primes can make a raw pool pass the count while every minimal subcover still fails.

13. **Proper divisors.** If \(p\mid N\) but \(N=p\), primality has not been excluded. Choosing \(m>\max p\) avoids this globally.

14. **Sophie Germain at \(b=1\).** The factor \(2b^2-2b+1\) equals \(1\) at \(b=1\). Require \(x>1\).

15. **Power-shape compatibility.** If \(m=x^M\), every selected CRT residue must be an \(M\)-th power modulo the corresponding prime.

16. **Machine verification must use exact arithmetic.** Floating-point density or probabilistic primality checks are not proof.

17. **Large sample checking is only a sanity test.** Testing \(k,\ell\le10^4\) cannot replace finite-period verification.

---

## 7. VERIFICATION HOOKS

## 7.1 Prime-character enumeration

For every candidate prime \(p\):

1. Compute
   \[
   o_{2,p}=\operatorname{ord}_p(2),\quad
   o_{3,p}=\operatorname{ord}_p(3),\quad
   h_p=\operatorname{lcm}(o_{2,p},o_{3,p}).
   \]
2. Enumerate \(H_p=\langle2,3\rangle\) and confirm \(|H_p|=h_p\).
3. Choose a generator \(g_p\) of \(H_p\).
4. Compute \(a_p,b_p\) with
   \[
   2=g_p^{a_p},\quad3=g_p^{b_p}.
   \]
5. Verify \(\gcd(a_p,b_p,h_p)=1\).

All of this can be done in exact modular arithmetic with `sympy.n_order`, explicit subgroup enumeration, and discrete-log lookup tables.

## 7.2 Candidate-column generation

A candidate target can be stored as either:

- \(t_p\in H_p\);
- a shift \((k_p,\ell_p)\) with
  \[
  t_p=2^{k_p}3^{\ell_p}\pmod p;
  \]
- or a character intercept
  \[
  c_p\pmod{h_p}.
  \]

The verifier should cross-check all three representations when supplied.

For \(m=x^M\), retain only targets satisfying

\[
-t_p^{-1}\in(\mathbb F_p^\times)^M.
\]

This can be tested by enumerating \(M\)-th powers or by a cyclic-group criterion.

## 7.3 Exact torus verification

For a manageable pool, compute

\[
A=\operatorname{lcm}_p o_{2,p},\qquad
B=\operatorname{lcm}_p o_{3,p}.
\]

For every \((k,\ell)\in[0,A-1]\times[0,B-1]\), verify at least one condition

\[
2^k3^\ell\equiv t_p\pmod p,
\]

or membership in a certified algebraic class.

If \(AB\) is too large, compute the intersection lattice

\[
K=\bigcap_p L_p
\]

using Hermite or Smith normal form and verify on the finite group \(\mathbb Z^2/K\). A BDD, ZDD, or recursive CRT decomposition can represent unions without enumerating the full rectangle.

## 7.4 Exact intersection calculation

For a set of character constraints

\[
a_i k+b_i\ell\equiv c_i\pmod{h_i},
\]

use Smith normal form to determine:

- whether the intersection is empty;
- if nonempty, its index in \(\mathbb Z^2\);
- hence its exact density.

This supports rigorous pairwise- and higher-overlap inequalities.

## 7.5 Cohort audit

Factor every \(h_p\). For every prime \(q\) appearing in any index, count candidates with \(q\mid h_p\). Iteratively remove candidates violating the \(q\)-cohort threshold.

When exactly \(q\) selected cyclic-character sets have \(q\mid h_p\), explicitly compute their affine-line shadows in \(\mathbb F_q^2\) and verify that they form a parallel complete pencil.

## 7.6 Capacity checks

For proposed \(A\):

1. Factor \(2^A-1\).
2. List all prime divisors \(p\ge5\).
3. Retain those with \(o_{2,p}\mid A\).
4. Compute
   \[
   C_2(A)=\sum_p1/h_p.
   \]

Do the symmetric calculation for \(C_3(B)\).

These are cheap rejection tests relative to a full covering search.

## 7.7 Algebraic-mask verification

For \(m=x^4\), mark

\[
k\equiv2\pmod4,\qquad \ell\equiv0\pmod4.
\]

Check the identity symbolically and check the minimal case \(k=2,\ell=0\) with \(x>1\).

For more general perfect-power constructions below, verify each factorization symbolically and enumerate the union density exactly on the least common modulus.

## 7.8 CRT output verification

Given targets \(t_p\), compute \(m\) satisfying

\[
m\equiv-t_p^{-1}\pmod p,\qquad m\equiv1\pmod6.
\]

Then verify:

- \(\gcd(m,6)=1\);
- every modular congruence;
- \(m>\max p\).

For \(m=x^M\), CRT must instead be applied to selected roots \(x\equiv r_p\pmod p\).

## 7.9 Sanity testing

After an exact certificate is obtained, independently test all \(k,\ell\le10^4\):

- identify the certified divisor;
- verify exact divisibility;
- optionally run a primality test on the full term for small values.

This is useful for finding transcription errors but is not the proof.

---

## 8. FOUR NEW ATTACK ROUTES FOR ROUND 2

## Route 1: Multi-identity perfect-power core

### Core mechanism

The Sophie Germain class can be enlarged substantially by making \(m\) a high perfect power and using ordinary cyclotomic factorizations as well.

Let

\[
m=x^M,\qquad x>1,\qquad \gcd(x,6)=1.
\]

If \(q\) is an odd prime with

\[
q\mid M,\qquad q\mid k,\qquad q\mid\ell,
\]

then

\[
2^k3^\ell x^M
=
\left(2^{k/q}3^{\ell/q}x^{M/q}\right)^q.
\]

Hence

\[
2^k3^\ell m+1=Y^q+1
\]

with \(Y>1\), and therefore

\[
Y^q+1=(Y+1)(Y^{q-1}-Y^{q-2}+\cdots-Y+1)
\]

is composite.

If \(4\mid M\), the Sophie Germain class

\[
k\equiv2\pmod4,\qquad \ell\equiv0\pmod4
\]

is also available.

A particularly attractive trial is \(M=60\). Then the algebraic classes are

\[
E_3=\{3\mid k,\ 3\mid\ell\},
\]
\[
E_5=\{5\mid k,\ 5\mid\ell\},
\]
and
\[
S_4=\{k\equiv2\pmod4,\ \ell\equiv0\pmod4\}.
\]

Their union has exact density

\[
1-\left(1-\frac19\right)
\left(1-\frac1{25}\right)
\left(1-\frac1{16}\right)
=
1-\frac{8}{9}\frac{24}{25}\frac{15}{16}
=
\frac15.
\]

Thus \(20\%\) of the exponent plane is handled algebraically, leaving density \(4/5\) for prime cosets.

A less restrictive first trial is \(M=15\), which algebraically covers

\[
E_3\cup E_5
\]

of density

\[
\frac19+\frac1{25}-\frac1{225}
=\frac{11}{75}.
\]

### Key lemma needed

Find a finite family of primes and allowed targets satisfying

\[
-t_p^{-1}\in(\mathbb F_p^\times)^M
\]

whose cosets cover the complement of the algebraic mask.

For \(M=60\), the allowed target set for \(p\) is

\[
H_p\cap\bigl(-(\mathbb F_p^\times)^{60}\bigr).
\]

The exact covering problem must use only these targets.

### Why it might work

- The \(M=60\) algebraic core reduces the required prime coverage from \(1\) to \(0.8\).
- The bounded smooth-index pool already has nominal mass \(0.7493\).
- A comparatively small cohort-legal mixed pool could provide the remaining slack.
- The algebraic classes are structured and exact, not heuristic.

### Most likely failure point

The \(M\)-th-power restriction may remove most useful target intercepts, especially for primes with \(3\) or \(5\) dividing \(p-1\). Also, introducing \(E_3\) and \(E_5\) brings additional subgroup indices divisible by \(3\) and \(5\), so the generalized cohort obstruction must be checked for the hybrid cover.

### Quick blocking test

For \(M\in\{12,15,20,60\}\):

1. Enumerate all allowed targets for a large candidate pool.
2. Add the algebraic mask.
3. Run cohort pruning including the algebraic cosets.
4. Solve an LP relaxation with exact overlap constraints.
5. If the maximum possible covered mass is below \(1\), reject that \(M\) before SAT.

This route is a genuine extension of the one-class Sophie Germain idea, not merely a larger prime search.

---

## Route 2: Finite-state orbit of one-dimensional Sierpiński templates

### Core mechanism

Instead of treating the problem as one enormous two-dimensional cover, regard

\[
n_\ell=3^\ell m
\]

as an orbit under multiplication by \(3\), and seek a finite cycle of one-dimensional Sierpiński covering templates.

Fix a finite prime pool and let

\[
B=\operatorname{lcm}_p o_{3,p}.
\]

For a chosen target \(t_p\), define the induced \(k\)-class on row \(r\in\mathbb Z/B\mathbb Z\) by

\[
K_{p,t_p}(r)
=
\{k\in\mathbb Z:
2^k\equiv t_p3^{-r}\pmod p\}.
\]

This set is either empty or one residue class modulo \(o_{2,p}\).

The desired condition becomes:

\[
\forall r\in\mathbb Z/B\mathbb Z,\qquad
\mathbb Z=
\bigcup_p K_{p,t_p}(r).
\]

Thus every \(\ell\)-state must carry a valid one-dimensional covering of the \(k\)-axis, but the same prime may participate in several states only according to its actual discrete-log transition law.

This generalizes the failed attempt to use one fixed classical Sierpiński cover: instead of requiring one template to be invariant under multiplication by \(3\), permit a finite cycle of mutually compatible templates.

### Key lemma needed

Construct a period \(B\), distinct primes \(p\), and one target \(t_p\) per prime such that the induced one-dimensional residue systems cover \(\mathbb Z\) for every state \(r\pmod B\).

A stronger, easier sufficient lemma would produce a small library of exact one-dimensional covering systems and a transition rule under \(r\mapsto r+1\).

### Why it might work

- One-dimensional covering systems are much better understood and easier to search than arbitrary two-dimensional unions.
- It directly exploits the necessary fact that every \(3^\ell m\) must be Sierpiński.
- It does not require all useful primes to have a common two-dimensional slope.
- Rowwise capacity and overlap obstructions can reject bad pools early.
- A prime’s coverage on different rows is correlated in a highly structured way, making automata or transfer-matrix methods natural.

### Most likely failure point

The same prime cannot be independently retargeted in different \(\ell\)-states. The transition law may force a hard row to have total one-dimensional mass below \(1\), reproducing the two-dimensional obstruction in asymmetric form. The period \(B\) may also become too large.

### Quick blocking test

For each proposed pool and each possible target assignment, or LP relaxation thereof, compute the row capacities

\[
W_r=\sum_{\substack{p:\\K_{p,t_p}(r)\ne\varnothing}}
\frac1{o_{2,p}}.
\]

Every row must satisfy \(W_r\ge1\). Add exact one-dimensional overlap inequalities for the small moduli. More strongly, derive Hall-type inequalities for subsets of rows based on which primes can be active there.

If every target assignment violates a row-capacity inequality, discard the pool without constructing the full torus.

---

## Route 3: Cohort-saturated recursive tiling in group-algebra coordinates

### Core mechanism

A generic SAT search over the full rectangle is too large and ignores the proved cohort structure. Instead, build a proof-producing recursive cover along a chain of finite abelian quotients.

For a selected candidate pool, let

\[
K=\bigcap_p L_p,\qquad G=\mathbb Z^2/K.
\]

Factor the relevant character indices into prime powers and choose a chain

\[
G_0\leftarrow G_1\leftarrow\cdots\leftarrow G_s=G
\]

where each step introduces one \(q\)-primary layer.

At every layer:

1. project candidate prime cosets to the current quotient;
2. group them into complete \(q\)-cohorts;
3. search for exact or near-exact “gadgets” whose union covers a parent residual cell or partitions it into smaller residual cells;
4. pass only the symbolic residual to the next layer.

The output should be a decision diagram or group-algebra identity proving

\[
\mathbf 1_G\le\sum_{p}\mathbf 1_{C(p,t_p)}
\]

pointwise, with each prime appearing at most once.

This is not a prime-first greedy search. The basic objects are cohort-legal lift gadgets.

### Key lemma needed

For each prime factor \(q\) introduced in the quotient chain, construct enough **lift-compatible \(q\)-gadgets**: collections of distinct prime cosets whose \(q\)-shadows form complete pencils and whose higher-order constraints either partition the relevant parent cell or leave a residual representable at deeper layers.

The key advance over the failed projective-shadow attempts must be exact control of the lift, not merely coverage modulo \(q\).

### Why it might work

- It builds the cohort lemma into the search architecture rather than checking it afterward.
- It avoids introducing \(p=47\), \(431\), etc. unless a full \(23\)- or \(43\)-cohort gadget has already been found.
- It can use exact symbolic unions and SNF coordinates instead of a gigantic \(A\times B\) bitset.
- It provides a compact, independently verifiable proof certificate.
- The total mass \(2.492\) below \(10^5\) suggests that a substantially slack, cohort-closed pool may exist even though the small hand-picked pools fail.

### Most likely failure point

A prime’s full character often constrains several quotient layers simultaneously. Consequently, a perfect shadow pencil may fragment badly on lifting. Distinct primes with the necessary matching lower-level restrictions may simply not exist in adequate numbers.

### Quick blocking test

For each \(q\in\{5,7,11,13,\ldots\}\):

1. enumerate all candidates with \(q\mid h_p\);
2. record their full character signatures, not just slopes modulo \(q\);
3. construct a compatibility hypergraph whose hyperedges are lift-compatible \(q\)-pencils;
4. check whether the residual cells requiring \(q\)-repair admit a matching by these hyperedges.

If no full pencil survives at the first nontrivial lift, that \(q\)-branch is blocked before global search.

This should be combined with LP duals and exact low-prime overlap cuts, but its core mechanism is recursive group tiling rather than generic SAT.

---

## Route 4: Genuine disproof route via a quantitative local-to-global principle

### Core mechanism

A negative answer requires prime production, not merely a covering obstruction. The only remotely plausible negative program has two separate gates:

1. Prove that no finite allowed affine-lattice cover exists.
2. Prove a quantitative local-to-global theorem saying that absence of a finite local obstruction forces at least one prime value
   \[
   2^k3^\ell m+1.
   \]

A possible form of the required theorem is:

> If, for a fixed \(m\), no finite family of prime-divisibility cosets covers \(\mathbb N_0^2\), then there exists \((k,\ell)\) for which \(2^k3^\ell m+1\) is prime.

A quantitative approach would seek \((k,\ell)\) in a controlled box that avoids every prime divisor up to

\[
\sqrt{2^k3^\ell m+1}.
\]

If such a pair exists, the corresponding number must be prime.

The rank-two heuristic is mildly supportive: the expected number of primes among pairs \(k,\ell\le R\), absent local obstructions, grows roughly linearly with \(R\), since

\[
\sum_{k,\ell\le R}\frac1{\log(2^k3^\ell m)}
\]

is of order \(R\). But this is only heuristic.

### Key lemma needed

Either:

- a rank-two sieve theorem overcoming the parity problem and producing a prime value; or
- a finite-obstruction theorem proving that every all-composite orbit necessarily has a finite prime cover, followed by a universal no-cover theorem.

Both statements are far beyond anything currently established in the notes.

### Why it might work

The extra exponent \(\ell\) provides substantially more freedom than the ordinary Sierpiński sequence. If all local congruence obstructions could be avoided in a sufficiently small exponent box, primality would follow.

The cohort cascade may also conceivably force any finite cover to introduce indefinitely many large prime factors in its indices, contradicting finiteness.

### Most likely failure point

This route encounters the classical sieve parity barrier in an unusually sparse exponential sequence. Avoiding all small prime divisors does not currently give a sufficiently small pair \((k,\ell)\), and there is no known reason that an all-composite sequence must have a finite covering set. Moreover, the large available mass and the algebraic constructions make an affirmative finite certificate more plausible.

### Quick blocking test

- Continue exact finite-cover searches on large cohort-closed pools. Discovery of a cover immediately kills the negative route and solves the problem affirmatively.
- For small \(m\), compute in boxes \(k,\ell\le R\) the maximal least prime factor of the terms and compare it with the square-root threshold. If the avoidance radius grows far too slowly, the quantitative sieve strategy is empirically blocked.
- Test whether cohort pruning stabilizes on large prime pools. If large cohort-closed cores survive with ample mass, a universal no-cover theorem is unlikely.

This route should receive substantially less computational priority than the three constructive routes.

---

## 9. VERDICT ON DIFFICULTY

The problem remains fully open. No explicit \(m\), no finite covering certificate, and no negative theorem are currently known from the supplied work.

A positive solution could be elementary once an exact finite certificate is found: the proof would reduce to modular arithmetic, a finite covering check, CRT, and possibly polynomial factorizations. The hard part is the combinatorial design.

The main structural facts are now clear:

- nominal mass is abundant globally;
- barely-supercritical smooth-period pools are rigorously impossible;
- large line primes cannot be used singly because of the cohort law;
- coarse projective pencils do not automatically lift;
- common-slope and classical Sierpiński lifts are insufficient;
- a successful construction likely needs substantial slack and exact multilevel organization.

The most promising new direction is the multi-perfect-power algebraic core, especially \(m=x^{15}\) or \(m=x^{60}\), combined with a target-compatible, cohort-saturated exact cover.

A negative solution would be much harder. It would require a universal prime-production result for a sparse rank-two exponential family or an unknown theorem reducing all-composite behavior to finite local obstructions. This is well beyond standard sieve methods and should be treated as a high-risk route.

There is no known equivalence to a single famous conjecture such as GRH or \(abc\). Nevertheless, a genuine “no” proof would require machinery at least comparable in difficulty to major unresolved prime-value problems. Current evidence leans toward **yes via an explicit hybrid covering certificate**, but that remains only a research judgment, not a theorem.