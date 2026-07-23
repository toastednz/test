# Problem Brief: Erdős Problem #411

## 1. Precise statement

Let \(\phi:\mathbb Z_{\ge 1}\to\mathbb Z_{\ge 1}\) be Euler’s totient function, with the standard convention \(\phi(1)=1\). Define
\[
F(m):=m+\phi(m).
\]
For \(j\ge 0\), let \(F^j\) denote the \(j\)-fold iterate of \(F\), with \(F^0\) the identity. The database notation is
\[
g_1(n)=F(n),\qquad g_k(n)=F^k(n)\quad (k\ge 1).
\]

The problem asks for a classification of all pairs
\[
(n,r)\in \mathbb Z_{\ge 1}\times \mathbb Z_{\ge 1}
\]
such that there exists an integer \(K\ge 1\) for which
\[
F^{k+r}(n)=2F^k(n)\qquad\text{for every }k\ge K. \tag{P}
\]
Equivalently, in the original notation,
\[
g_{k+r}(n)=2g_k(n)\qquad\text{for all sufficiently large }k.
\]

It is often convenient to set
\[
a_0=n,\qquad a_{j+1}=F(a_j)=a_j+\phi(a_j).
\]
Then the condition is
\[
a_{k+r}=2a_k\qquad(k\ge K). \tag{1}
\]

### Standard interpretation and indexing caveat

The natural domain is positive integers \(n,r\). The function is not defined at \(n=0\) under the standard convention.

Because the database defines \(g_1=F\), “for all sufficiently large \(k\)” formally begins at some \(K\ge1\). Introducing \(F^0\) is only a notational convenience. It does not alter the eventual condition.

### Elementary reduction to a finite equality

The following facts are fundamental.

1. \(F(m)>m\) for every \(m\ge1\), so every orbit is strictly increasing.
2. If \(m\) is even and \(m\ge4\), then \(\phi(m)\) is even, hence \(F(m)\) is even.
3. If \(m\) is even, then
   \[
   F(2m)=2m+\phi(2m)=2m+2\phi(m)=2F(m), \tag{2}
   \]
   provided \(m\) is even. The parity condition is essential.
4. Consequently, if \(x\ge4\) is even and
   \[
   F^r(x)=2x, \tag{3}
   \]
   then
   \[
   F^{k+r}(x)=2F^k(x)\qquad\text{for every }k\ge0. \tag{4}
   \]

Thus, for \(n\ge4\) even, condition (P) is equivalent to the existence of some \(K\ge0\) such that
\[
F^r(F^K(n))=2F^K(n). \tag{5}
\]
In words: the orbit of \(n\) must eventually hit an even “seed” \(x\) satisfying \(F^r(x)=2x\).

This distinction matters: classifying direct seeds \(x\) is not automatically the same as classifying all \(n\) whose orbits eventually reach such seeds.

### Immediate exclusions

- If \(n>1\) is odd, then \(\phi(n)\) is even, so \(F(n)\) remains odd. Therefore an odd orbit cannot satisfy \(a_{k+r}=2a_k\).
- \(1\mapsto2\mapsto3\), after which the orbit remains odd.
- \(2\mapsto3\), after which the orbit remains odd.

Hence every solution must have
\[
n\text{ even and }n\ge4. \tag{6}
\]

Also, \(r=1\) is impossible. Indeed \(F(x)=2x\) would imply \(\phi(x)=x\), which occurs only at \(x=1\), and no orbit is eventually constantly at \(1\). Therefore
\[
r\ge2. \tag{7}
\]

### The conjectural complete answer

Cambie’s conjectural classification, rewritten without using \(p\) for the composite number \(35\), is:

> Condition (P) holds if and only if
> \[
> r=2
> \]
> and
> \[
> n=2^\ell q,\qquad \ell\ge1,\qquad
> q\in\{2,3,5,7,35,47\}. \tag{C}
> \]

The case \(q=2\) encodes the pure powers of \(2\) beginning with \(4\). Note that \(q\) is not always prime.

For all the numbers in (C), the stronger direct relation
\[
F^2(n)=2n
\]
holds, so the required equality is valid from the beginning, not merely eventually.

---

## 2. What counts as a solution

Because the original problem is a classification question rather than a yes/no proposition, a complete solution must give and prove an exhaustive classification.

### A complete proof of Cambie’s proposed classification must establish

1. **Sufficiency.** For every
   \[
   n=2^\ell q,\quad \ell\ge1,\quad
   q\in\{2,3,5,7,35,47\},
   \]
   prove
   \[
   F^{k+2}(n)=2F^k(n)
   \]
   for all sufficiently large \(k\), preferably for all \(k\ge0\).

2. **Exclusion of all other lags.** Prove that no \(r\ne2\) can occur.

3. **Exclusion of all other direct seeds.** Prove that if an even \(x\ge4\) satisfies
   \[
   F^r(x)=2x,
   \]
   then \(r=2\) and \(x\) belongs to the listed family.

4. **Exclusion of transient predecessors.** Prove that if the orbit of \(n\) eventually reaches a valid seed, then \(n\) itself is in the listed family. It is not enough to classify only the eventual seed \(F^K(n)\).

The sufficiency part is elementary. The base calculations are
\[
\begin{array}{c|c|c}
x&F(x)&F^2(x)\\ \hline
4&6&8\\
6&8&12\\
10&14&20\\
14&20&28\\
70&94&140\\
94&140&188.
\end{array}
\]
Thus \(F^2(x)=2x\) for
\[
x\in\{4,6,10,14,70,94\}.
\]
The identity \(F(2m)=2F(m)\) for even \(m\) then supplies all allowed powers of \(2\).

### What would refute Cambie’s proposed answer

A finite counterexample to (C) consists of integers \(n,r,K\) such that

- \(n\ge1\), \(r\ge1\), \(K\ge0\);
- either \(r\ne2\), or \(n\) is not of the form in (C);
- with \(x=F^K(n)\), one has \(x\ge4\) even and
  \[
  F^r(x)=2x.
  \]

Because of the propagation identity, this finite equality certifies
\[
F^{k+r}(n)=2F^k(n)\qquad(k\ge K).
\]

For a completely checkable certificate, provide the exact values
\[
n,F(n),\ldots,F^{K+r}(n)
\]
and factorizations of all arguments at which \(\phi\) is evaluated. The factorizations verify each totient using
\[
\phi\left(\prod_i p_i^{e_i}\right)
 =\prod_i p_i^{e_i-1}(p_i-1).
\]

Such a counterexample would disprove Cambie’s classification, but it would not by itself completely solve the original “for which \(n,r\)” problem. A full resolution after such a discovery would still require the correct exhaustive replacement classification.

---

## 3. What does not count as a solution

None of the following resolves the problem.

1. Proving the classification only for \(r=2\), without excluding \(r\ge3\).
2. Proving that only the listed numbers satisfy \(F^2(n)=2n\), while not treating orbits that enter such a seed later.
3. Classifying \(n\) only up to a numerical bound.
4. Showing that counterexamples, if any, must exceed a large bound such as \(10^{10}\).
5. Showing that the set of exceptions has density zero or is finite without identifying it.
6. Obtaining upper or lower bounds on \(r\) that do not force the complete answer.
7. Giving an algorithm that searches each individual orbit but has no global termination proof.
8. Conditional results depending on unproved conjectures about primes, inverse totients, shifted primes, or values of \(\phi\).
9. Heuristics based on treating \(\phi(m)/m\) as random or independent along the orbit.
10. Finding further identities of the form
    \[
    F^{k+s}(n)=cF^k(n)
    \]
    with \(c\ne2\). Such identities are relevant context but are not answers to this problem.
11. Reducing the problem to another unresolved Diophantine equation without solving that equation.
12. Producing one new solution outside Cambie’s list. This is a major result and refutes the conjectured answer, but does not itself classify all pairs.

---

## 4. Known results and context

### 4.1 The \(r=2\) equation

For a direct seed \(x\),
\[
F^2(x)=2x
\]
is equivalent to
\[
\phi(x)+\phi(x+\phi(x))=x. \tag{8}
\]
Indeed,
\[
F^2(x)
=x+\phi(x)+\phi(x+\phi(x)).
\]

For the original eventual problem with \(r=2\), equation (8) applies to the eventual seed \(x=F^K(n)\). An additional backward-orbit argument is needed to conclude a classification of the original starting value \(n\).

### 4.2 Steinerberger’s restriction

According to the database commentary, Steinerberger has shown that if (8) holds, then the odd part of \(x\), meaning
\[
\operatorname{odd}(x)=\frac{x}{2^{v_2(x)}},
\]
is either in
\[
\{1,3,5,7,35,47\},
\]
or belongs to an exceptional parametrized configuration involving
\[
8m+7,\qquad 6m+5,
\]
where
\[
8m+7\ge10^{10}\text{ is prime}
\]
and
\[
\phi(6m+5)=4m+4. \tag{9}
\]

The punctuation of the database summary is slightly ambiguous about whether both \(8m+7\) and \(6m+5\) can occur as odd parts under the joint conditions, or whether they represent two linked branches. Any use of this theorem should consult the precise statement in [St25].

The possible infinitude of such \(m\) is connected to the equation
\[
\phi(u)=\frac23(u+1). \tag{10}
\]
This places the remaining \(r=2\) analysis in the difficult territory of shifted and inverse totient equations.

### 4.3 Cambie’s reduction

The commentary states that Cambie reduces the problem to determining which integers \(r,t\ge1\) and primes
\[
p\equiv7\pmod8
\]
satisfy an equation printed as
\[
g_k(2p^t)=4p^t.
\]
The variable \(k\) is unbound in that sentence. The intended reading is almost certainly
\[
F^r(2p^t)=4p^t, \tag{11}
\]
that is, \(2p^t\) is a direct seed for lag \(r\).

Cambie conjectures that the only such cases are
\[
t=1,\qquad p\in\{7,47\},
\]
with the corresponding lag \(r=2\).

### 4.4 The database’s “known solutions” wording

The commentary says that the known solutions to
\[
g_{k+2}(n)=2g_k(n)
\]
are \(n=10\) and \(n=94\). Taken literally as an exhaustive statement about integer starting values, this cannot be correct: for example,
\[
4\mapsto6\mapsto8,\qquad 6\mapsto8\mapsto12,
\]
and hence \(n=4,6\) also satisfy the relation, as do all numbers in the conjectured families.

The sentence should therefore be read as historical shorthand for particular nontrivial representatives, or under an unstated equivalence convention involving doubling and orbit shifts. It should not be used as a formal exhaustive theorem.

### 4.5 Other exact scaling phenomena

The database records:

- Selfridge and Weintraub found examples satisfying
  \[
  F^{k+9}(n)=9F^k(n).
  \]
- Weintraub found
  \[
  F^{k+25}(3114)=729F^k(3114)\qquad(k\ge6).
  \]
- Cambie observed
  \[
  F^{k+4}(738)=3F^k(738),
  \]
  \[
  F^{k+4}(148646)=4F^k(148646),
  \]
  and
  \[
  F^{k+4}(4325798)=4F^k(4325798)
  \]
  for all \(k\ge1\).

These show that exact multiplicative self-similarity is not unique to multiplier \(2\), and that longer lags genuinely occur for other multipliers. They do not directly answer Problem #411.

### 4.6 Useful elementary identities

For \(m\ge1\),
\[
\phi(2m)=
\begin{cases}
\phi(m),&m\text{ odd},\\
2\phi(m),&m\text{ even}.
\end{cases} \tag{12}
\]
Thus
\[
F(2m)=
\begin{cases}
2m+\phi(m),&m\text{ odd},\\
2F(m),&m\text{ even}.
\end{cases} \tag{13}
\]

Also, if
\[
x_i=F^i(x),
\]
then
\[
F^r(x)=2x
\quad\Longleftrightarrow\quad
\sum_{i=0}^{r-1}\phi(x_i)=x. \tag{14}
\]
Equivalently,
\[
\prod_{i=0}^{r-1}
\left(1+\frac{\phi(x_i)}{x_i}\right)=2. \tag{15}
\]

Equation (14) is the additive form; equation (15) is the multiplicative density form.

---

## 5. Traps and edge cases

### 5.1 Parity exceptions at \(1\) and \(2\)

The familiar statement “\(\phi(n)\) is even” holds only for \(n>2\). In particular,
\[
F(1)=2,\qquad F(2)=3.
\]
Arguments asserting that every even orbit remains even must explicitly assume the current value is at least \(4\).

### 5.2 Incorrect unrestricted doubling identity

It is false that \(F(2m)=2F(m)\) for every \(m\). It holds when \(m\) is even. For odd \(m\),
\[
F(2m)=2m+\phi(m),\qquad
2F(m)=2m+2\phi(m).
\]

This is especially important when dividing a solution by powers of \(2\). The reduction works cleanly while the halved orbit remains even, but breaks at the odd core.

### 5.3 Direct versus eventual solutions

The implication
\[
F^r(n)=2n\Longrightarrow \text{eventual relation}
\]
is straightforward for even \(n\ge4\).

The converse is only
\[
\text{eventual relation}\Longrightarrow
F^r(F^K(n))=2F^K(n)
\]
for some \(K\). One may not replace \(F^K(n)\) by \(n\) without proving a backward-propagation theorem.

### 5.4 \(F\) is increasing along each orbit, but not monotone as a function

Since \(\phi(m)>0\),
\[
F(m)>m,
\]
so every individual orbit is strictly increasing.

However, \(m\mapsto m+\phi(m)\) is not globally monotone in \(m\), and injectivity must not be assumed. Therefore an equality
\[
F(a)=F(b)
\]
does not automatically imply \(a=b\). This is a central obstacle to propagating an eventual relation backward.

### 5.5 Lag uniqueness

For a fixed seed \(x\), the values \(F^j(x)\) are strictly increasing. Therefore there is at most one \(r\) satisfying
\[
F^r(x)=2x.
\]
Any computation reporting two different lags for the same seed contains an error.

### 5.6 The symbol \(p\) in the conjecture

The set
\[
\{2,3,5,7,35,47\}
\]
contains \(35\), so its elements should not uniformly be called primes. Use \(q\), “core,” or “odd factor.”

### 5.7 Pure powers of two

The odd part of a pure power of \(2\) is \(1\), whereas Cambie’s parameterization writes these as
\[
2^\ell\cdot 2.
\]
These are the same family after shifting the exponent. Do not inadvertently omit the odd-part-\(1\) branch.

### 5.8 Off-by-one in the iterates

The database uses \(g_1=F\), not \(g_0=\mathrm{id}\). Verify every claimed identity under the chosen indexing. In \(F\)-notation, a direct seed satisfies
\[
F^r(n)=2n;
\]
in database notation this corresponds to an identity involving \(g_r(n)\), not \(g_{r+1}(n)\).

### 5.9 Numerical evidence cannot exclude late entry

Even if no \(n\le N\) is itself a direct seed, some \(n\le N\) might conceivably enter a seed only after many iterations. A bounded search in starting values and orbit length does not prove a global classification.

### 5.10 Average-order heuristics are unreliable

The totient ratio
\[
\frac{\phi(m)}m=\prod_{p\mid m}\left(1-\frac1p\right)
\]
depends sharply on the prime support of \(m\). The numbers \(F^j(n)\) are additively linked, not probabilistically independent. Replacing totient ratios by average values cannot prove an exact equality.

### 5.11 The exceptional Steinerberger alternatives may overlap

The forms \(8m+7\), \(6m+5\), and the finite odd-core set may have overlaps for small \(m\), while the stated lower bound \(8m+7\ge10^{10}\) is intended to remove already checked ranges. Exact quantifiers from the source should be preserved.

---

## 6. Verification hooks

### 6.1 Exhaustive direct-seed search

For each even \(x\) in a chosen range, compute
\[
y_0=x,\qquad y_{j+1}=y_j+\phi(y_j).
\]
Because \(y_j\) is strictly increasing, continue only until \(y_j\ge2x\):

```text
y := x
for r := 1,2,...:
    y := y + phi(y)
    if y == 2*x:
        record (x,r)
        break
    if y > 2*x:
        break
```

This finds every \(r\) for that \(x\); there can be at most one.

For a dense bounded search, precompute \(\phi(m)\) by a totient sieve up to the largest orbit value required. For larger sparse values, factor each orbit element.

### 6.2 Primitive-core normalization

If \(x=2u\) with \(u\ge4\) even, then
\[
F^j(x)=2F^j(u)\qquad(j\ge0).
\]
Hence
\[
F^r(x)=2x
\quad\Longleftrightarrow\quad
F^r(u)=2u.
\]

Computational searches should therefore normalize direct seeds by repeatedly halving while the result remains even and at least \(4\). The primitive representatives are generally \(x\equiv2\pmod4\), together with the special pure-power representative \(x=4\).

### 6.3 Check the conjectured base cases

A unit test should verify exactly:
\[
\begin{aligned}
4&\to6\to8,\\
6&\to8\to12,\\
10&\to14\to20,\\
14&\to20\to28,\\
70&\to94\to140,\\
94&\to140\to188.
\end{aligned}
\]

It should then verify, for several powers of \(2\), that doubling each entire orbit segment preserves the relation.

### 6.4 Totient valuation logging

For every orbit element \(x_i\), record:

- \(v_2(x_i)\);
- the full factorization of \(x_i\);
- \(v_2(\phi(x_i))\);
- \(\phi(x_i)/x_i\);
- \(v_2(x_i+\phi(x_i))\).

The standard formula is
\[
v_2(\phi(n))
=
\max(v_2(n)-1,0)
+\sum_{\substack{p^a\parallel n\\p\text{ odd}}}v_2(p-1). \tag{16}
\]
This can expose impossible valuation patterns for a hypothetical block ending at \(2x\).

### 6.5 Backward-preimage search

For a target \(z\), search for all \(y<z\) satisfying
\[
y+\phi(y)=z. \tag{17}
\]
A simple bounded implementation sieves \(\phi(y)\) for \(y<z\). Apply this to the known solution rays to test whether there are predecessors not already in Cambie’s families.

Because \(F(y)>y\), every preimage lies below \(z\), so this is a finite computation for each fixed target.

### 6.6 Search for Steinerberger exceptional parameters

For \(m\) in a computational range:

1. test whether \(8m+7\) is prime;
2. factor \(6m+5\);
3. compute \(\phi(6m+5)\);
4. test
   \[
   \phi(6m+5)=4m+4.
   \]

Any hit should then be substituted into the exact \(r=2\) seed equation, because the commentary provides a necessary structural condition and should not be assumed to give sufficiency without checking the precise theorem.

### 6.7 Independent certificate format

For any proposed new seed \(x\), publish:

- \(r\);
- all values \(x_i=F^i(x)\), \(0\le i\le r\);
- prime factorizations of \(x_0,\ldots,x_{r-1}\);
- the computed totients;
- the final equality \(x_r=2x_0\).

For large prime factors, attach deterministic primality certificates or proofs rather than probable-prime declarations.

---

## 7. Attack routes

### Route 1: Primitive-core reduction under powers of two

**Core mechanism.** Use
\[
F(2m)=2F(m)
\]
throughout even orbits to reduce every direct seed to a primitive core, usually \(x\equiv2\pmod4\), plus the pure-power base \(4\).

**Key lemma needed.** A classification of primitive solutions to
\[
F^r(x)=2x
\]
showing that every primitive solution has
\[
r=2,\qquad x\in\{4,6,10,14,70,94\}.
\]

**Why it might work.** The conjectured infinite families are entirely generated by powers-of-two scaling. Removing this symmetry reduces the problem to odd-core arithmetic and aligns with Steinerberger’s odd-part theorem.

**Likely failure point.** The identity breaks at the transition from \(2q\) to the odd number \(q\). The primitive core still carries unrestricted odd prime factorizations, so the reduction may leave an inverse-totient problem of essentially unchanged difficulty.

**Quick obstruction test.** Enumerate all primitive even \(x\le B\), iterate only until crossing \(2x\), and tabulate all seeds by \(r\), odd core, and residue classes modulo \(2^j\). If numerous unexplained primitive patterns survive, this route alone is insufficient.

---

### Route 2: A \(2\)-adic transition theorem forcing \(r=2\)

**Core mechanism.** Analyze the sequence
\[
x_{i+1}=x_i+\phi(x_i)
\]
through \(v_2(x_i)\) and \(v_2(\phi(x_i))\). The endpoint condition
\[
x_r=2x_0
\]
increases the \(2\)-adic valuation by exactly one.

**Key lemma needed.** A rigidity theorem showing that an even orbit segment whose endpoint is exactly twice its start cannot have length \(r\ge3\), except possibly for a sharply specified exceptional prime-factor pattern.

**Why it might work.** Formula (16) translates odd prime congruence information into \(2\)-adic constraints. Repeated exact cancellation in
\[
x_i+\phi(x_i)
\]
may be too rigid to support a long block ending at \(2x_0\).

**Likely failure point.** Knowing \(v_2(x_i)\) and \(v_2(\phi(x_i))\) does not always determine
\[
v_2(x_i+\phi(x_i))
\]
when the two valuations agree; arbitrarily deep cancellation can depend on odd residues.

**Quick obstruction test.** Build a finite-state search of admissible valuation and residue patterns modulo \(2^M\), using factorization constraints on \(v_2(\phi(x_i))\). If admissible cycles or long blocks remain for every tested \(M\), purely \(2\)-adic information is unlikely to force \(r=2\).

---

### Route 3: Totient-density and prime-divisor propagation

**Core mechanism.** Use
\[
2=\frac{x_r}{x_0}
=\prod_{i=0}^{r-1}
\left(1+\frac{\phi(x_i)}{x_i}\right)
\]
together with
\[
\frac{\phi(x_i)}{x_i}
=\prod_{p\mid x_i}\left(1-\frac1p\right).
\]

**Key lemma needed.** A theorem controlling how the prime supports of
\[
x_i,\qquad x_i+\phi(x_i)
\]
can evolve under the exact product constraint, strong enough to show either \(r=2\) or a finite list of exceptional support patterns.

**Why it might work.** Long lags require many small multiplicative increments whose product is exactly \(2\). This should force the \(x_i\) to have many small prime divisors, but the additive update may then impose incompatible congruences on the next iterate.

**Likely failure point.** Prime divisors of \(x+\phi(x)\) are not directly controlled by those of \(x\). The additive step can introduce large new primes, defeating standard multiplicative closure arguments.

**Quick obstruction test.** Factor extensive orbit data and compare prime-support transitions for near misses and exact seeds. If new large primes appear with no stable restrictions, a direct density argument will need substantial additive-combinatorial input.

---

### Route 4: Backward-orbit and collision rigidity

**Core mechanism.** First classify direct seeds, then solve the inverse equations
\[
y+\phi(y)=z
\]
for targets \(z\) on the valid solution rays.

**Key lemma needed.** A restricted preimage theorem asserting that every preimage of a listed solution-ray value either lies on the same listed ray or cannot itself lead to an eventual doubling relation.

A stronger possible lemma is:
\[
F(u)=F(v),\quad v=2w,\quad\text{under suitable orbit constraints}
\Longrightarrow u=v.
\]

**Why it might work.** The difference between the direct-seed problem and the original eventual problem is exactly the existence of extra preimages. The known rays appear arithmetically sparse, so their full backward trees may be rigid.

**Likely failure point.** The inverse problem
\[
y+\phi(y)=z
\]
is itself difficult, and \(F\) is not known to be globally injective. Sporadic collisions could create transient starting values not captured by a direct-seed classification.

**Quick obstruction test.** Compute complete preimage trees to substantial depth for the targets on the six base rays. One unexpected off-family preimage that later enters a ray would immediately refute the simplest backward-rigidity claim.

---

### Route 5: Complete the \(r=2\) shifted-totient analysis

**Core mechanism.** Reduce to primitive \(x=2q\) and analyze
\[
\phi(x)+\phi(x+\phi(x))=x
\]
by factoring \(q\), splitting according to the parity of \(q+\phi(q)/2\), and exploiting Steinerberger’s restriction.

**Key lemma needed.** Eliminate or completely classify the exceptional parameters satisfying
\[
8m+7\ \text{prime},\qquad
\phi(6m+5)=4m+4.
\]
Ideally prove that they generate no new seeds beyond odd cores
\[
1,3,5,7,35,47.
\]

**Why it might work.** This is the most developed part of the problem. A near-classification is already available, and the remaining alternatives have a very explicit shifted-totient form.

**Likely failure point.** Equations prescribing exact totient values are notoriously rigid but difficult. The related equation
\[
\phi(u)=\frac23(u+1)
\]
may have an unknown infinite family. Eliminating all large exceptional parameters could require genuinely new inverse-totient technology.

**Quick obstruction test.** Implement the exceptional-parameter search and inspect the factorization patterns forced by
\[
\phi(6m+5)=4m+4.
\]
If the equation admits many large computational candidates or reduces to flexible prime constellations, an elementary elimination is unlikely.

---

### Route 6: Counterexample construction and targeted disproof search

**Core mechanism.** Search deliberately for either:

- a primitive seed with \(r\ge3\), or
- a new \(r=2\) odd core arising from Steinerberger’s exceptional branch, or
- an off-family predecessor entering a known seed orbit.

One can also attempt to engineer a block
\[
x_{i+1}=x_i+\phi(x_i),\qquad x_r=2x_0,
\]
by prescribing factorizations that give desired totient ratios.

**Key lemma needed.** For a constructive approach, a realization theorem producing integers with specified prime support and compatible additive transitions. For a computational approach, an efficient way to search large primitive cores without factoring every intermediate integer from scratch.

**Why it might work.** Exact scaling with longer lags occurs for multipliers \(3,4,9,729\), so long exact self-similar blocks are not intrinsically impossible. The assertion that multiplier \(2\) uniquely forces \(r=2\) may conceal a rare large counterexample.

**Likely failure point.** Prescribing \(\phi(x)\) and simultaneously controlling the factorization of \(x+\phi(x)\) is an inverse-totient problem coupled to an additive prime-value problem. Naive construction is severely overdetermined.

**Quick obstruction test.** Search all primitive even \(x\) in a large range, with exact iteration until the orbit exceeds \(2x\). Separately search the exceptional \(m\)-conditions and backward preimages of known rays. Any hit gives a finite, independently certifiable refutation of Cambie’s classification.

---

## 8. Verdict on difficulty

This is a genuinely difficult open classification problem. Its elementary formulation hides several hard components:

1. exact iteration of a highly nonuniform multiplicative function under an additive update;
2. inverse-totient equations;
3. shifted totient values;
4. prime constraints such as \(8m+7\) being prime;
5. possible noninjectivity and backward-orbit collisions;
6. the need to exclude every lag \(r\ge3\), not merely settle \(r=2\).

The \(r=2\) case is already linked to the unresolved equation
\[
\phi(u)=\frac23(u+1),
\]
or to closely related questions about whether such equations have infinitely many solutions. Therefore a complete proof of Cambie’s finite classification may require a substantial advance in inverse-totient theory.

It would be too strong, based only on the supplied commentary, to claim a formal equivalence with a single famous named conjecture. Nevertheless, the problem is loudly entangled with a recognized hard class of totient equations, and the remaining exceptional branch should not be treated as a routine finite cleanup.

The most realistic division of labor is:

1. formalize and verify the power-of-two and eventual-seed reductions;
2. attack \(r\ne2\) using \(2\)-adic and prime-support rigidity;
3. independently complete the \(r=2\) exceptional analysis;
4. prove a backward-preimage theorem;
5. maintain an aggressive exact search for a large counterexample throughout.

A full solution would be a significant result in the arithmetic dynamics of Euler’s totient function.