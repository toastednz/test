# Problem Brief: Erdős Problem #203

## 1. PRECISE STATEMENT

Let  
\[
\mathbb N_0=\{0,1,2,\dots\}.
\]
Determine whether there exists an integer \(m\ge 1\) satisfying
\[
\gcd(m,6)=1
\]
such that
\[
2^k3^\ell m+1
\]
is composite for every ordered pair
\[
(k,\ell)\in\mathbb N_0^2.
\]

Equivalently, the question is whether
\[
\exists m\in\mathbb Z_{\ge1}\quad
\left[
\gcd(m,6)=1\ \wedge\
\forall k,\ell\in\mathbb N_0,\ 
2^k3^\ell m+1\notin\mathbb P
\right],
\]
where \(\mathbb P\) denotes the set of positive primes.

Because \(\gcd(m,6)=1\), \(m\) is odd. Thus:

- \(m=1\) fails, since \(2^03^0m+1=2\) is prime.
- For every possible solution \(m>1\), the entire axis \(k=0\) is automatic:
  \[
  3^\ell m+1
  \]
  is even and greater than \(2\), hence composite.
- Therefore the substantive requirement is
  \[
  2^k3^\ell m+1\ \text{composite for all }k\ge1,\ \ell\ge0.
  \]

The explicit bounds \(k,\ell\ge0\) leave little ambiguity. A reading with \(k,\ell\ge1\) would be a different and strictly weaker problem.

### The finite-covering formulation

For a prime \(p\ge5\), define
\[
\phi_p:\mathbb Z^2\longrightarrow \mathbb F_p^\times,\qquad
\phi_p(k,\ell)=2^k3^\ell \pmod p.
\]
Let
\[
H_p=\langle 2,3\rangle\le \mathbb F_p^\times
\]
and
\[
L_p=\ker\phi_p
=\{(u,v)\in\mathbb Z^2:2^u3^v\equiv1\pmod p\}.
\]

Since \(\mathbb F_p^\times\) is cyclic,
\[
[\mathbb Z^2:L_p]
=|H_p|
=\operatorname{lcm}\bigl(\operatorname{ord}_p(2),\operatorname{ord}_p(3)\bigr).
\]
Write this common quantity as \(h_p\).

For fixed \(m\not\equiv0\pmod p\),
\[
p\mid 2^k3^\ell m+1
\]
if and only if
\[
2^k3^\ell\equiv -m^{-1}\pmod p.
\]
If \(-m^{-1}\in H_p\), this set of exponent pairs is one coset of \(L_p\); otherwise it is empty.

Thus a strong sufficient condition for a positive answer is the existence of distinct primes \(p_1,\dots,p_r\ge5\) and targets \(t_i\in H_{p_i}\) such that
\[
\mathbb Z^2
=
\bigcup_{i=1}^r
\{(k,\ell):2^k3^\ell\equiv t_i\pmod {p_i}\}.
\]
The Chinese Remainder Theorem then gives \(m\) satisfying
\[
m\equiv -t_i^{-1}\pmod {p_i}\qquad(1\le i\le r)
\]
and, independently,
\[
m\equiv1\ \text{or }5\pmod6.
\]
Taking a sufficiently large positive representative ensures
\[
m>\max_i p_i,
\]
so divisibility by \(p_i\) proves genuine compositeness rather than allowing the value to equal \(p_i\).

### Important correction to the pipeline formulation

The original problem is **not known to be equivalent** to the existence of a finite prime-coset covering.

A finite covering is sufficient. Conversely, a hypothetical \(m\) for which every term is composite might use infinitely many different prime divisors, with no finite set covering all exponent pairs. There is no general compactness argument forcing a finite subcover of \(\mathbb N_0^2\).

What is true is:

> There exists an \(m\) whose sequence admits a finite set of covering primes if and only if there exists a finite coset covering of the above kind.

This is a stronger, finitely certifiable version of the original problem.

---

## 2. WHAT COUNTS AS A SOLUTION

### A complete affirmative solution

A complete proof of “YES” must exhibit or prove the existence of an \(m\ge1\) with \(\gcd(m,6)=1\) and establish, without an exponent cutoff, that
\[
2^k3^\ell m+1
\]
is composite for every \(k,\ell\ge0\).

The cleanest possible solution would be a finite covering certificate consisting of:

1. Distinct certified primes \(p_1,\dots,p_r\ge5\).
2. For each \(i\), a target
   \[
   t_i\in\langle2,3\rangle\pmod {p_i},
   \]
   preferably represented as
   \[
   t_i\equiv2^{a_i}3^{b_i}\pmod {p_i}.
   \]
3. A proof that for every \((k,\ell)\in\mathbb Z^2\), at least one \(i\) satisfies
   \[
   2^k3^\ell\equiv t_i\pmod {p_i}.
   \]
4. A CRT solution to
   \[
   m\equiv-t_i^{-1}\pmod {p_i},
   \qquad
   m\equiv1\text{ or }5\pmod6.
   \]
5. A choice of positive representative with \(m>\max_i p_i\).

Then every term has a proper divisor:
\[
p_i\mid 2^k3^\ell m+1,
\qquad
1<p_i<2^k3^\ell m+1.
\]

It is not necessary to print the decimal expansion of an enormous \(m\), provided its CRT residue class is explicit and effectively computable. Such a certificate would in fact yield infinitely many valid \(m\), namely all sufficiently large representatives in the same residue class modulo
\[
6\prod_i p_i.
\]

An affirmative proof not based on a finite covering would also count, but it must still handle all infinitely many exponent pairs rigorously.

### A complete negative solution

A complete proof of “NO” must establish
\[
\forall m\ge1,\quad
\gcd(m,6)=1
\Longrightarrow
\exists k,\ell\ge0
\quad
2^k3^\ell m+1\in\mathbb P.
\]

This is a universal statement over all admissible \(m\). It is not enough to refute individual candidates.

For any fixed proposed \(m\), a proven prime value
\[
2^k3^\ell m+1
\]
is a valid counterexample to that candidate. Its primality must be proved, for example by deterministic factorization methods for small values or by a verifiable ECPP/Pratt/Pocklington certificate for large values. But one failed \(m\), or any finite collection of failed \(m\), does not answer the original problem.

Likewise, proving that no finite coset covering exists would not by itself prove “NO,” unless one also proves that every everywhere-composite family must admit a finite covering.

---

## 3. WHAT DOES NOT COUNT

The following do **not** resolve the problem:

1. Finding an \(m\) for which no prime occurs in a finite box
   \[
   0\le k\le K,\qquad 0\le\ell\le L.
   \]

2. Finding an \(m\) for which all tested terms are composite, even for extremely large computational bounds.

3. Showing only that \(m\) is a Sierpiński number, i.e.
   \[
   2^km+1
   \]
   is composite for all \(k\). This addresses only the line \(\ell=0\).

4. Covering all but finitely many, density-zero many, or asymptotically negligible exponent pairs.

5. Obtaining total covering “mass” greater than \(1\) without constructing an actual covering.

6. Randomized searches that report no uncovered pair but do not provide an exhaustive, independently checkable certificate.

7. A conditional result assuming Artin-type conjectures, Bateman–Horn heuristics, generalized Schinzel hypotheses, or unproved distribution statements about primes in exponential sequences.

8. Proving that no finite cover exists. This only rules out the strongest standard construction, not the original possibility of infinitely many varying prime divisors.

9. Reusing one prime \(p\) for several different target cosets. For fixed \(m\), the residue
   \[
   -m^{-1}\pmod p
   \]
   is fixed, so one prime can cover only one coset of \(L_p\).

10. A divisibility certificate that fails to rule out equality with the divisor. If \(p\mid N\), one must also have \(N>p\) to infer compositeness.

---

## 4. KNOWN RESULTS AND CONTEXT

### 4.1 Relation to Sierpiński numbers

An odd positive integer \(s\) is a Sierpiński number if
\[
s2^k+1
\]
is composite for every \(k\ge1\). Setting \(\ell=0\) shows that every solution \(m\) to the present problem must be a Sierpiński number.

Indeed, more strongly, for every \(\ell\ge0\),
\[
3^\ell m
\]
must itself be a Sierpiński number, since
\[
2^k(3^\ell m)+1
\]
must be composite for all \(k\ge1\).

The least Sierpiński number is known computationally to be
\[
78557.
\]
Consequently, any solution here must satisfy
\[
m\ge78557.
\]
The fact that \(78557\) is Sierpiński does not imply it solves the two-parameter problem.

Classical Sierpiński-number constructions use a covering system for the exponent \(k\), followed by CRT conditions on the coefficient. The present problem asks for a two-dimensional analogue.

### 4.2 Generalizations in the database commentary

Erdős and Graham also ask about expressions
\[
p_1^{k_1}\cdots p_r^{k_r}m+1
\]
for fixed distinct primes \(p_i\), and about
\[
q_1\cdots q_rm+1
\]
where the \(q_i\) range over primes congruent to \(1\pmod4\).

For the latter formulation, if \(r\ge1\) and no additional condition is imposed, \(m=1\) is indeed trivial:
\[
q_1\cdots q_r+1
\]
is even and greater than \(2\). Thus the quoted question likely omitted a restriction, perhaps on \(m\) or on the allowed number of factors.

### 4.3 Structure of a prime coset

For \(p\ge5\), set
\[
o_2(p)=\operatorname{ord}_p(2),\qquad
o_3(p)=\operatorname{ord}_p(3),\qquad
h_p=\operatorname{lcm}(o_2(p),o_3(p)).
\]
A target \(t\in H_p\) covers a set of natural density
\[
\frac1{h_p}
\]
in \(\mathbb Z^2\).

Hence any finite coset covering must satisfy the necessary density inequality
\[
\sum_{p\in S}\frac1{h_p}\ge1.
\]
This condition is far from sufficient because the cosets can overlap heavily.

If
\[
o_2(p)=o_3(p)=q
\]
and \(3\equiv2^d\pmod p\), then the condition
\[
2^k3^\ell=t
\]
becomes an affine line
\[
k+d\ell\equiv c\pmod q.
\]
For example, modulo \(23\),
\[
\operatorname{ord}_{23}(2)=\operatorname{ord}_{23}(3)=11,
\qquad
3\equiv2^8\pmod{23},
\]
so each target is a line
\[
k+8\ell\equiv c\pmod{11}.
\]

Other useful equal-order examples from the supplied computation include:

\[
\begin{array}{c|c|c|c}
p&o_2(p)&o_3(p)&h_p\\ \hline
23&11&11&11\\
47&23&23&23\\
71&35&35&35\\
431&43&43&43\\
601&75&75&75\\
167&83&83&83
\end{array}
\]

Small heavy contributors include:

\[
\begin{array}{c|c|c|c}
p&o_2(p)&o_3(p)&h_p\\ \hline
5&4&4&4\\
7&3&6&6\\
11&10&5&10\\
13&12&3&12\\
17&8&16&16\\
19&18&18&18\\
29&28&28&28\\
31&5&30&30\\
37&36&18&36\\
73&9&12&36\\
41&20&8&40\\
43&14&42&42
\end{array}
\]

The supplied SymPy computation found
\[
\sum_{\substack{5\le p<10^5\\p\text{ prime}}}\frac1{h_p}\approx2.492.
\]
Thus there is no simple density obstruction to a finite covering.

However, much of this mass lives on incompatible large subtori. Restricting to primes whose coordinate periods divide a tractable common torus, such as one based on \(5040\), reportedly leaves only about \(1.02\)–\(1.03\) total mass. This explains why naïve randomized covering performs poorly.

A caution concerning \(p=89\): here
\[
o_2(89)=11,\qquad o_3(89)=88,\qquad h_{89}=88.
\]
It is not simply another affine line on \(\mathbb Z_{11}^2\); the \(\ell\)-coordinate retains period \(88\).

### 4.4 Relevant general tools

The most relevant established tools are:

- the Chinese Remainder Theorem;
- cyclicity of \(\mathbb F_p^\times\);
- multiplicative orders and discrete logarithms;
- finite covering congruences;
- Smith normal form for intersections and quotients of exponent lattices;
- Bang–Zsigmondy theory for producing primitive prime divisors of \(a^n-1\).

Bang–Zsigmondy can produce primes with specified order behavior for one base, but does not automatically produce primes simultaneously well aligned with both \(2\) and \(3\). That simultaneous-order issue is central here.

---

## 5. TRAPS AND EDGE CASES

### 5.1 The primes \(2\) and \(3\)

The group/lattice description applies only to \(p\ge5\).

- Since \(m\) is odd,
  \[
  2\mid 3^\ell m+1
  \]
  exactly along \(k=0\). For \(k\ge1\), the expression is odd.

- For \(\ell\ge1\),
  \[
  2^k3^\ell m+1\equiv1\pmod3,
  \]
  so \(3\) cannot divide an interior term.

- On \(\ell=0\),
  \[
  3\mid2^km+1
  \]
  for one parity of \(k\), depending on \(m\bmod3\).

The boundary help from \(2\) and \(3\) does not reduce the density requirement for a finite cover of the interior. If finitely many primes \(p\ge5\) cover all \(k,\ell\ge1\), periodicity implies that they cover every residue pair in the associated finite torus.

### 5.2 The term \(m+1\)

For every admissible \(m>1\),
\[
m+1
\]
is automatically even and greater than \(2\). It need not be covered by one of the selected odd primes. Requiring an odd covering prime for \((k,\ell)=(0,0)\) is unnecessarily strong.

### 5.3 Finite covering is not equivalent to the problem

The statement “every term is composite” gives an infinite cover by all possible prime divisors. It does not imply that finitely many of those primes suffice.

A profinite compactness argument does not repair this: natural exponent pairs are dense rather than compact, and an infinite open cover of the natural points need not have a finite subcover.

### 5.4 One prime gives one coset

For a fixed prime \(p\nmid m\), the target is fixed:
\[
2^k3^\ell\equiv-m^{-1}\pmod p.
\]
A proposed construction cannot assign several intercepts to the same prime.

### 5.5 The lattice is generally diagonal

It is incorrect to model the covered set merely by independent conditions
\[
k\bmod o_2(p),\qquad \ell\bmod o_3(p).
\]
The kernel can contain nontrivial diagonal relations
\[
2^u3^v\equiv1\pmod p.
\]
The rectangular periods are valid for exhaustive verification, but they do not describe the minimal lattice geometry.

### 5.6 Density is only necessary

Even
\[
\sum 1/h_p>1
\]
does not imply coverability. The cosets may overlap in a highly correlated way. Conversely, a restricted candidate pool with mass below \(1\) cannot furnish a finite cover, but this says nothing about primes outside that pool.

### 5.7 Period explosion

For selected primes \(S\), the safe rectangular periods are
\[
A=\operatorname{lcm}_{p\in S}o_2(p),\qquad
B=\operatorname{lcm}_{p\in S}o_3(p).
\]
The product \(AB\) can be enormous even for a modest set of primes. A search that silently replaces \(A\) or \(B\) by a smaller convenient modulus is invalid unless it proves that all selected predicates descend to that smaller quotient.

### 5.8 Divisibility versus compositeness

If a certificate only proves
\[
p\mid2^k3^\ell m+1,
\]
it must rule out equality. Taking \(m>\max p_i\) is the simplest uniform safeguard.

---

## 6. VERIFICATION HOOKS

### 6.1 Verification of a finite covering certificate

Given distinct primes \(p_i\) and targets \(t_i\):

1. Prove each \(p_i\) prime, preferably with deterministic certificates.
2. Compute
   \[
   a_i=o_2(p_i),\qquad b_i=o_3(p_i).
   \]
   To certify an order \(a_i\), check
   \[
   2^{a_i}\equiv1\pmod {p_i}
   \]
   and
   \[
   2^{a_i/q}\not\equiv1\pmod {p_i}
   \]
   for every prime \(q\mid a_i\). Do the same for \(3\).
3. Verify \(t_i\in H_{p_i}\), most easily by supplying
   \[
   t_i\equiv2^{u_i}3^{v_i}\pmod {p_i}.
   \]
4. Compute
   \[
   A=\operatorname{lcm}_i a_i,\qquad
   B=\operatorname{lcm}_i b_i.
   \]
5. Exhaustively verify that every
   \[
   (k,\ell)\in\{0,\dots,A-1\}\times\{0,\dots,B-1\}
   \]
   satisfies
   \[
   2^k3^\ell\equiv t_i\pmod {p_i}
   \]
   for at least one \(i\).

If \(AB\) is too large, replace direct enumeration by a symbolic partition, BDD, SAT proof, or quotient by
\[
L=\bigcap_iL_{p_i}.
\]
Any compressed verification must still provide a checkable proof that no uncovered class exists.

### 6.2 CRT verification

Let
\[
P=\prod_i p_i.
\]
Solve
\[
m\equiv-t_i^{-1}\pmod {p_i},
\qquad
m\equiv1\pmod6
\]
or \(m\equiv5\pmod6\).

Independently verify each residue. Then replace \(m\) by
\[
m+6Pn
\]
for a sufficiently large \(n\), ensuring
\[
m>\max_i p_i.
\]

### 6.3 Reproduction of the mass computation

For each prime \(5\le p<10^5\):

1. Factor \(p-1\).
2. Compute \(o_2(p)\) and \(o_3(p)\).
3. Set
   \[
   h_p=\operatorname{lcm}(o_2(p),o_3(p)).
   \]
4. Sum \(1/h_p\) exactly as a rational number and convert to decimal only at the end.

This reproduces or checks the reported value \(2.492\).

### 6.4 Candidate-\(m\) refutation

For a proposed \(m\), enumerate exponent pairs in increasing approximate value
\[
k\log2+\ell\log3.
\]
For each pair, compute
\[
N=2^k3^\ell m+1
\]
and run a primality prover. One proven prime immediately refutes that \(m\).

This is useful for rejecting candidates, but failure to find a prime is not positive evidence of the required strength.

### 6.5 Symbolic residual analysis

Represent each prime predicate as an affine coset of a lattice. Intersections of covered or uncovered regions can be handled using:

- Hermite or Smith normal form;
- CRT on finite abelian quotients;
- exact bitsets on moderate quotient groups;
- SAT variables \(x_{p,c}\), with at most one selected coset \(c\) for each \(p\).

For a proposed hierarchical cover, verify after every stage that the residual is exactly the claimed union of lattice cosets.

---

## 7. ATTACK ROUTES

### Route 1: Exact finite-cover search by SAT/CP-SAT

**Core mechanism.**  
Choose a finite candidate set of primes. For each \(p\), introduce variables selecting at most one of the \(h_p\) possible target cosets. Impose one covering constraint for every class in a common quotient of \(\mathbb Z^2\).

**Key lemma needed.**  
A tractable quotient or symbolic representation on which all candidate cosets can be enumerated exactly.

**Why it might work.**  
Any satisfying assignment immediately gives a complete CRT certificate. The reported mass \(2.492\) suggests that a sufficiently rich prime pool has enough nominal capacity.

**Likely failure point.**  
The common rectangular period \(A\times B\) becomes enormous, while restricting to a small smooth period leaves only barely more than unit mass. Standard random or greedy set cover will likely trap itself in a structured residual.

**Quick blockage test.**  
Run the LP relaxation and exact SAT search on nested candidate pools. Record:

- fractional optimum;
- minimum uncovered residue count;
- dual weights concentrating on hard residual classes.

If the LP itself cannot reach full coverage, that pool is conclusively inadequate.

---

### Route 2: Hierarchical or nested lattice covering

**Core mechanism.**  
First cover most of a coarse quotient using high-density primes such as
\[
5,7,11,13,17,19,29,31,37,41,43,61,73.
\]
Express the residual exactly as a union of cosets of a finer sublattice. Then use primes such as
\[
23,47,71,167,431,601
\]
whose diagonal line structures act efficiently on selected residual fibers.

**Key lemma needed.**  
At each stage, the residual must decompose into cosets aligned with the kernels of the next-stage primes, and the available primes must have enough distinct slopes/intercepts to cover those residual fibers.

**Why it might work.**  
This directly addresses the main computational obstruction: the useful mass lies on mutually incommensurate subtori and should not be forced into one flat global search.

**Likely failure point.**  
A residual that is simple on one quotient can fragment badly after lifting to another. Also, each prime supplies only one intercept.

**Quick blockage test.**  
After choosing the first-stage primes, compute the residual in Smith-normal-form coordinates and its intersection profile with every candidate line prime. If every remaining prime overlaps essentially the same residual portion, the hierarchy is blocked and the first-stage choices must be redesigned.

---

### Route 3: Product-grid construction from common cyclotomic divisors

**Core mechanism.**  
Choose periods \(A,B\) and seek many primes satisfying
\[
o_2(p)\mid A,\qquad o_3(p)\mid B.
\]
Such primes divide
\[
\gcd(2^A-1,\,3^B-1).
\]
Use their cosets to cover the finite grid
\[
\mathbb Z_A\times\mathbb Z_B.
\]

More refined versions prescribe exact cyclotomic factors and use primitive divisors to obtain controlled lattices.

**Key lemma needed.**  
A period pair \((A,B)\) for which the common divisors of \(2^A-1\) and \(3^B-1\) supply enough distinct primes with sufficiently varied lattice kernels.

**Why it might work.**  
It avoids period incompatibility by manufacturing all primes inside one designed torus.

**Likely failure point.**  
Bang–Zsigmondy gives primitive divisors of one sequence at a time; it does not ensure simultaneous compatibility with both bases. The relevant gcd may have too few distinct prime factors or may yield nearly identical kernels.

**Quick blockage test.**  
For moderate smooth \(A,B\), factor or partially factor
\[
\gcd(2^A-1,3^B-1),
\]
compute the induced lattices, and solve the resulting exact finite set-cover instance. A persistent shortage of distinct useful factors would strongly disfavor this route.

---

### Route 4: Lift one-dimensional Sierpiński coverings to affine-line covers

**Core mechanism.**  
Start from a covering system for exponents \(k\) in the ordinary Sierpiński problem. For primes where \(3\in\langle2\rangle\), multiplication by \(3^\ell\) shifts the covered \(k\)-class:
\[
2^k3^\ell\equiv2^{k+d\ell}.
\]
Thus one-dimensional congruence classes become affine lines in \((k,\ell)\).

Try to combine families of lines of different slopes so that their uncovered intersections are eliminated by other primes.

**Key lemma needed.**  
A collection of available primes whose induced affine lines covers the relevant finite affine planes or covers the residual left by the dense small-prime stage.

**Why it might work.**  
It imports the successful mechanism behind classical Sierpiński numbers while using \(\ell\) as a controlled translation parameter.

**Likely failure point.**  
A full \(q\times q\) affine plane requires substantial line mass. There are often only a few useful primes for a given \(q\), and existing Sierpiński coverings fix residues that may not interlock correctly in two dimensions.

**Quick blockage test.**  
For \(q=11,23,35,43,83\), explicitly compute all available slopes and solve the finite incidence problem on \(\mathbb F_q^2\), both alone and restricted to the residual from small primes. In particular, do not treat \(p=89\) as an ordinary line on \(\mathbb F_{11}^2\).

---

### Route 5: Probabilistic covering with alteration

**Core mechanism.**  
For each selected prime \(p\), choose a target coset randomly, possibly with a biased distribution adapted to a weighted residual. Analyze the uncovered set and then use a deterministic alteration phase to cover the remaining structured classes.

**Key lemma needed.**  
A probabilistic or entropy bound showing that some target choice leaves a residual small and structured enough to be finished by the remaining primes.

**Why it might work.**  
Coset choices for distinct primes are CRT-independent. Random choices cover a point with marginal probability \(1/h_p\), and weighted randomization may avoid the excessive overlaps seen in naïve greedy methods.

**Likely failure point.**  
With total mass \(2.492\), independent heuristics predict an uncovered proportion on the order of
\[
e^{-2.492}\approx0.083,
\]
far too large for direct completion. Correlations induced by common order factors can make the residual worse.

**Quick blockage test.**  
Run many randomized target selections and classify residual points by lattice signature. If the residual fraction remains near the independent prediction and no small family of signatures dominates, a simple alteration argument is unlikely to work.

---

### Route 6: Disproof through prime production or a structural obstruction

**Core mechanism.**  
Prove that for every admissible \(m\), some member of
\[
\{m2^k3^\ell+1:k,\ell\ge0\}
\]
is prime.

A possible two-stage strategy would be:

1. rule out every finite local covering obstruction;
2. prove that absence of such an obstruction forces a prime value.

**Key lemma needed.**  
An unconditional prime-value theorem for this two-parameter exponential family, or a valid local-to-global theorem saying that an everywhere-composite family must admit a finite prime cover.

**Why it might work.**  
Heuristically, there are about \(T^2\) exponent pairs with \(k,\ell\le T\), while the logarithms of the corresponding numbers are \(O(T)\), so random-prime heuristics predict many prime values unless a covering obstruction exists.

**Likely failure point.**  
No standard sieve theorem can prove prime values in a family this sparse and nonlinear. Moreover, the local-to-global finite-cover principle is unproved and is not generally justified by compactness.

**Quick blockage test.**  
Attempt to formulate the claimed local-to-global lemma in analogous one-dimensional composite sequences; search for known counterexamples or infinite-prime-divisor constructions. Separately, any explicit finite coset certificate immediately destroys the entire disproof route.

---

## 8. VERDICT ON DIFFICULTY

The problem remains genuinely open. It is stronger than the classical Sierpiński-number problem because a solution \(m\) would make every
\[
3^\ell m
\]
a Sierpiński number simultaneously.

There is no known equivalence to a famous named conjecture. However, the two possible directions have very different apparent difficulty:

- A **YES** answer may be attainable by a finite, computer-assisted covering certificate. Once such a certificate is found, verification is elementary and fully rigorous: multiplicative orders, finite coverage, CRT, and proper-divisor checks.
- A **NO** answer appears substantially harder. It would require prime production uniformly for every admissible \(m\), or a new theorem forcing finite local obstructions. Current sieve and exponential-sequence methods do not appear close to this.

The supplied computations strongly disfavor a simple density obstruction and suggest that total covering mass is available. They do not prove coverability, but they make an explicit hierarchical finite cover the most plausible route.

The central research task is therefore:

> Construct a finite family of distinct primes \(p\ge5\), one target coset per prime, whose affine exponent-lattice cosets cover \(\mathbb Z^2\), and output a fully checkable CRT certificate.

The main technical barrier is not lack of density, but organizing diagonal cosets across incompatible period structures without wasting too much mass through overlap.