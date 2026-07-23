STATUS: BLOCKED

## Result

Route 2 reduces at the decisive scale to a parity-sensitive prime-pair correlation for which no unconditional lower-bound sieve is available. I proved an exact square-root sieve criterion and a von Mangoldt transference criterion, but neither can presently be verified for a trajectory. More sharply, I constructed terminal seeds whose earlier terms contain an arbitrarily large proportion of all primes below the terminal prime and are exactly equidistributed modulo any prescribed fixed modulus. By diagonalization, there are terminal states whose earlier-prime sets have relative density tending to \(1\) and are asymptotically equidistributed modulo every fixed modulus. Thus density and fixed-level equidistribution—even in extremely strong forms—cannot be the missing Route 2 lemma. Any successful transference theorem must control correlations at a scale growing with \(q_n\), essentially the correlation with the shifted primes themselves.

## Complete Argument

### 1. An exact square-root sieve formulation

Let the current term be an odd prime \(p=q_n\), and put
\[
h=p-1.
\]
For each earlier prime \(q_i\), the candidate is
\[
N_i=h+q_i=p+q_i-1.
\]

Define
\[
E=\{i\le n:q_i\nmid h\}.
\]
If \(i\notin E\), then \(q_i\mid h\), so
\[
q_i\mid h+q_i=N_i,
\]
and \(N_i>q_i\). Thus every candidate excluded from \(E\) is composite. In particular, \(q_i=2\) is always excluded because \(2\mid h\).

Set
\[
z=\left\lfloor\sqrt{2p-1}\right\rfloor
\]
and
\[
\mathcal L_h(z)=\{\ell\le z:\ell\text{ prime and }\ell\nmid h\},
\qquad
P_h(z)=\prod_{\ell\in\mathcal L_h(z)}\ell.
\]

#### Lemma 1: exact square-root sieve

The number of prime candidates at the state \(p\) is exactly
\[
S_h(z)=\#\{i\in E:\gcd(h+q_i,P_h(z))=1\}.
\]
Consequently, the recurrence extends if and only if \(S_h(z)>0\).

#### Proof

For \(i\in E\), we have \(q_i\ne2\), so \(q_i\ge3\), and hence
\[
p+2\le N_i=h+q_i\le 2p-1.
\]
Suppose \(N_i\) is composite. It has a prime divisor
\[
\ell\le\sqrt{N_i}\le\sqrt{2p-1},
\]
so \(\ell\le z\). If \(\ell\mid h\), then from \(\ell\mid h+q_i\) we get \(\ell\mid q_i\). Since \(q_i\) is prime, this forces \(q_i=\ell\), contradicting \(i\in E\). Therefore \(\ell\nmid h\), so \(\ell\in\mathcal L_h(z)\), and
\[
\gcd(N_i,P_h(z))>1.
\]

Conversely, if \(\gcd(N_i,P_h(z))>1\), then some prime \(\ell\le z\) divides \(N_i\). Since
\[
z<p<N_i
\]
for \(p\ge3\), this is a proper divisor, so \(N_i\) is composite.

Thus, among indices in \(E\), the candidates coprime to \(P_h(z)\) are exactly the prime candidates. All indices outside \(E\) were already shown to give composite candidates. ∎

This is an exact sieve reformulation, but it already shows the difficulty: primality requires sieving all the way to \(z\asymp p^{1/2}\).

---

### 2. Exact inclusion-exclusion and a conditional transference criterion

For squarefree \(d\mid P_h(z)\), define
\[
A(d)=\#\{i\in E:d\mid h+q_i\}.
\]
Since \(\gcd(d,h)=1\),
\[
d\mid h+q_i
\quad\Longleftrightarrow\quad
q_i\equiv-h\pmod d,
\]
where \(-h\) is a reduced residue class modulo \(d\).

Inclusion-exclusion gives the exact identity
\[
S_h(z)=\sum_{d\mid P_h(z)}\mu(d)A(d).
\]

If the earlier primes behaved uniformly among reduced residue classes, the expected value would be
\[
A(d)\approx \frac{|E|}{\varphi(d)}.
\]
Write
\[
A(d)=\frac{|E|}{\varphi(d)}+R(d).
\]
Then
\[
S_h(z)=|E|V_h(z)+
\sum_{d\mid P_h(z)}\mu(d)R(d),
\]
where
\[
V_h(z)
=\prod_{\substack{\ell\le z\\ \ell\nmid h}}
\left(1-\frac1{\ell-1}\right).
\]

Thus the following is rigorous.

#### Lemma 2: full-discrepancy sufficient condition

If
\[
\sum_{d\mid P_h(z)}|R(d)|<|E|V_h(z),
\]
then the recurrence extends from \(p\).

#### Proof

The exact identity implies
\[
S_h(z)
\ge |E|V_h(z)-\sum_{d\mid P_h(z)}|R(d)|>0.
\]
Lemma 1 then gives a prime candidate. ∎

The expected sieve factor can be evaluated. Let
\[
C_2=\prod_{\ell>2}
\left(1-\frac1{(\ell-1)^2}\right)
\]
be the twin-prime constant. Since
\[
1-\frac1{\ell-1}
=
\left(1-\frac1\ell\right)
\left(1-\frac1{(\ell-1)^2}\right),
\]
Mertens' theorem gives
\[
\prod_{3\le\ell\le z}
\left(1-\frac1{\ell-1}\right)
\sim \frac{2C_2e^{-\gamma}}{\log z}.
\]
Therefore
\[
V_h(z)
\sim
\frac{2C_2e^{-\gamma}}{\log z}
\prod_{\substack{3\le\ell\le z\\\ell\mid h}}
\frac{\ell-1}{\ell-2}.
\]

This is the expected singular-series enhancement. At \(z\asymp\sqrt p\), the heuristic main term is of order
\[
\frac{|E|}{\log p}.
\]

The obstruction is that Lemma 2 requires simultaneous control over all divisors of a product containing every relevant prime up to \(\sqrt p\). This is far stronger than ordinary fixed-modulus equidistribution.

A weaker but exact finite-order criterion is also available.

#### Lemma 3: Bonferroni lower bound

For every odd positive integer \(K\),
\[
S_h(z)\ge
\sum_{\substack{d\mid P_h(z)\\\omega(d)\le K}}
\mu(d)A(d).
\]
In particular, positivity of the right-hand side proves extension.

#### Proof

Fix a candidate \(N_i\) and let \(r_i\) be the number of primes in \(\mathcal L_h(z)\) dividing it. Its contribution to the truncated sum is
\[
\sum_{j=0}^{\min(K,r_i)}(-1)^j\binom{r_i}{j}.
\]
If \(r_i=0\), this equals \(1\). If \(1\le r_i\le K\), it equals \(0\). If \(r_i>K\), then
\[
\sum_{j=0}^{K}(-1)^j\binom{r_i}{j}
=(-1)^K\binom{r_i-1}{K}\le0
\]
because \(K\) is odd. Hence the contribution is always at most the indicator of \(r_i=0\). Summing over \(i\in E\) proves the claim. ∎

Already for \(K=1\), this is just the union bound
\[
S_h(z)\ge |E|-\sum_{\ell\in\mathcal L_h(z)}A(\ell).
\]
The expected sum of the individual forbidden-residue densities diverges like \(\log\log z\), so first-order information is insufficient.

---

### 3. A von Mangoldt transference target

Let
\[
X=2p-1
\]
and
\[
T(p)=\sum_{i\in E}\Lambda(h+q_i).
\]

#### Lemma 4: a sufficiently large \(\Lambda\)-correlation forces extension

If
\[
T(p)>
\left(
X^{1/2}+(\log_2 X)X^{1/3}
\right)\log X,
\]
then there is a prime candidate.

#### Proof

Assume there is no prime candidate. The von Mangoldt function is nonzero only when
\[
h+q_i=\ell^k
\]
for a prime \(\ell\) and \(k\ge2\).

The number of prime powers at most \(X\) with exponent at least \(2\) is at most
\[
\sum_{k=2}^{\lfloor\log_2 X\rfloor}X^{1/k}
\le
X^{1/2}+(\log_2 X)X^{1/3}.
\]
This overcounts numbers that are powers in more than one way, which is harmless. Each such number contributes at most \(\log X\) to the von Mangoldt sum. Since the candidate values are distinct, the claimed upper bound on \(T(p)\) follows under nonextension. Its violation therefore forces a prime candidate. ∎

Thus a lower bound
\[
T(p)\gg |E|
\]
would suffice whenever
\[
|E|\gg \sqrt p\,(\log p)^2.
\]
But proving such a lower bound is a pointwise correlation estimate between the adaptive earlier-prime set and the shifted von Mangoldt function. It is substantially stronger than congruence equidistribution and is essentially the desired prime-pair statement.

---

### 4. Density and fixed-modulus equidistribution do not suffice

The next construction is the main rigorous obstruction found during Route 2.

#### Theorem 5: arbitrarily dense, equidistributed terminal seeds

Let \(W\) be any fixed even positive integer, and let \(\varepsilon>0\). There exist infinitely many terminal seeds
\[
q_1<\cdots<q_{m-1}<q_m=p
\]
such that:

1. for every reduced residue class \(c\bmod W\), exactly the same number of the earlier terms \(q_1,\ldots,q_{m-1}\) lie in \(c\bmod W\);
2. every candidate \(p+q_i-1\), including the self-candidate \(2p-1\), is composite;
3. for all sufficiently large seeds in the construction,
   \[
   \frac{m-1}{\pi(p)}>1-\varepsilon.
   \]

Thus an arbitrarily large proportion of all primes below \(p\) can occur in an exactly fixed-modulus-equidistributed terminal seed.

#### Proof

Choose a finite set \(L\) of primes \(\ell\ge5\), none dividing \(W\), such that
\[
\eta=\prod_{\ell\in L}
\left(1-\frac1{\ell-1}\right)<\frac{\varepsilon}{2}.
\]
This is possible because
\[
\sum_{\ell\ \mathrm{prime}}\frac1{\ell-1}
\]
diverges, and hence the corresponding product tends to zero.

Put
\[
\delta=1-\eta>1-\frac{\varepsilon}{2}.
\]

Choose another prime \(k\) dividing neither \(W\) nor \(\prod_{\ell\in L}\ell\). By the Chinese remainder theorem, there is a reduced residue class \(a\bmod M\), where
\[
M=Wk\prod_{\ell\in L}\ell,
\]
specified by
\[
\begin{aligned}
p&\equiv1\pmod W,\\
p&\equiv-1\pmod\ell
\qquad(\ell\in L),\\
2p&\equiv1\pmod k.
\end{aligned}
\]
Each prescribed residue is nonzero modulo the corresponding prime factor, so \(\gcd(a,M)=1\). Dirichlet's theorem therefore supplies infinitely many primes \(p\equiv a\pmod M\).

For a reduced residue class \(c\bmod W\), define
\[
\mathcal B_c(x)=
\left\{
q\le x:
\begin{array}{l}
q\text{ prime},\\
q\equiv c\pmod W,\\
q\equiv2\pmod\ell
\text{ for at least one }\ell\in L
\end{array}
\right\}.
\]
By inclusion-exclusion and the prime number theorem in fixed arithmetic progressions,
\[
\#\mathcal B_c(x)
\sim
\frac{\delta}{\varphi(W)}\operatorname{Li}(x).
\]
Indeed, for a subset \(S\subseteq L\), simultaneous conditions
\[
q\equiv c\pmod W,\qquad
q\equiv2\pmod\ell\quad(\ell\in S)
\]
describe one reduced residue class modulo \(W\prod_{\ell\in S}\ell\), and inclusion-exclusion gives the factor
\[
1-\prod_{\ell\in L}\left(1-\frac1{\ell-1}\right)=\delta.
\]

For one of the primes \(p\equiv a\pmod M\), let
\[
t_p=\min_{\substack{c\bmod W\\(c,W)=1}}
\#\mathcal B_c(p-1).
\]
There are only finitely many reduced classes \(c\bmod W\), so
\[
t_p\sim
\frac{\delta}{\varphi(W)}\operatorname{Li}(p)
\]
as \(p\to\infty\) through these primes.

For each reduced class \(c\bmod W\), choose exactly \(t_p\) primes from \(\mathcal B_c(p-1)\). Sort all the selected primes increasingly and append \(p\). This gives a strictly increasing prime seed. By construction, exactly \(t_p\) earlier terms occur in each reduced class modulo \(W\).

If \(q\) is selected, then for some \(\ell\in L\),
\[
q\equiv2\pmod\ell.
\]
Since \(p\equiv-1\pmod\ell\),
\[
p+q-1\equiv -1+2-1\equiv0\pmod\ell.
\]
For sufficiently large \(p\), this candidate is larger than \(\ell\), so it is composite.

The self-candidate satisfies
\[
2p-1\equiv0\pmod k,
\]
and for sufficiently large \(p\) it is larger than \(k\), so it is composite as well. Hence the seed is terminal.

Finally,
\[
m-1=\varphi(W)t_p
\sim \delta\operatorname{Li}(p),
\]
while
\[
\pi(p)\sim\operatorname{Li}(p).
\]
Therefore
\[
\frac{m-1}{\pi(p)}\longrightarrow\delta
>1-\frac{\varepsilon}{2},
\]
and in particular the ratio is greater than \(1-\varepsilon\) for all sufficiently large choices of \(p\). ∎

A small instance of the same covering idea is the terminal seed
\[
(2,7,17,29),
\]
because
\[
29+2-1=30,\quad
29+7-1=35,\quad
29+17-1=45,\quad
2\cdot29-1=57.
\]

#### Corollary 6: density-one and all fixed-modulus equidistribution still do not suffice

There is a sequence of terminal seeds with terminal primes \(p_r\to\infty\) such that
\[
\frac{m_r-1}{\pi(p_r)}\longrightarrow1,
\]
and, for every fixed modulus \(d\), the earlier primes are eventually exactly equidistributed among the reduced residue classes modulo \(d\).

#### Proof

Apply Theorem 5 with
\[
W_r=2\operatorname{lcm}(1,2,\ldots,r)
\]
and \(\varepsilon=1/r\). Choose the terminal prime \(p_r\) sufficiently large that the density ratio exceeds \(1-1/r\).

For each fixed \(d\), once \(r\ge d\), we have \(d\mid W_r\). Equal occupation of all reduced residue classes modulo \(W_r\) implies equal occupation of all reduced residue classes modulo \(d\), because the reduction map
\[
(\mathbb Z/W_r\mathbb Z)^\times
\longrightarrow
(\mathbb Z/d\mathbb Z)^\times
\]
is surjective with equal-sized fibers. ∎

This directly refutes the plausible Route 2 lemma:

> “A set containing density \(1-o(1)\) of the primes below \(p\), and equidistributed modulo every fixed modulus, must contain a prime \(q\) with \(p+q-1\) prime.”

It is false even for legal starting states of this problem. The missing information is a correlation at moduli or sieve levels growing with \(p\).

---

### 5. Recurrence-specific modular structure

The recurrence does possess one exact local invariant, but it does not force primality.

#### Lemma 7: invariant common divisor

Let
\[
g=\gcd(q_1-1,\ldots,q_m-1).
\]
At every later stage for which the trajectory is defined,
\[
g\mid q_n-1,
\]
and the gcd of all available values \(q_i-1\) remains exactly \(g\).

#### Proof

Write \(a_i=q_i-1\). Every generated term satisfies
\[
a_{n+1}=a_n+a_{j_n}.
\]
If all currently available \(a_i\) are divisible by \(g\), then so is \(a_{n+1}\). Thus all later \(a_i\) are divisible by \(g\).

The original seed values remain present, and their gcd is \(g\). Appending further multiples of \(g\) cannot increase or decrease the gcd of the complete set, so it remains exactly \(g\). ∎

In particular, if all seed primes satisfy
\[
q_i\equiv1\pmod W,
\]
then every later term and every candidate satisfy
\[
q_n+q_i-1\equiv1\pmod W.
\]
Thus an engineered seed can permanently immunize every candidate against divisibility by the primes dividing a fixed \(W\). This is favorable local behavior, but \(W\) is fixed while the required sieve range grows like \(\sqrt{q_n}\).

It also shows that ordinary equidistribution is not a universal recurrence property: trajectories may be permanently concentrated in one reduced residue class.

---

### 6. A finite reservoir cannot support an infinite trajectory

A self-replenishing construction would have to use genuinely new increments indefinitely.

#### Lemma 8: infinitely many different indices must be selected

In any infinite trajectory, the set
\[
\{j_n:n\ge m\}
\]
of selected indices is infinite.

#### Proof

Suppose only finitely many indices are ever selected. Then there is a constant
\[
C=\max\{q_j-1:j\text{ is ever selected}\}
\]
such that
\[
q_{n+1}-q_n\le C
\]
at every generated step. Hence
\[
q_N\le q_m+C(N-m)=O(N).
\]

On the other hand, \(q_1,\ldots,q_N\) are \(N\) distinct primes not exceeding \(q_N\), so
\[
N\le\pi(q_N).
\]
The elementary estimate \(\pi(x)=o(x)\) now gives
\[
N\le o(q_N)=o(N),
\]
a contradiction.

For completeness, \(\pi(x)=o(x)\) follows as follows. Fix \(y\) and let
\[
M_y=\prod_{\ell\le y,\ \ell\text{ prime}}\ell.
\]
Every prime greater than \(y\) is coprime to \(M_y\), so
\[
\pi(x)\le \pi(y)+x\frac{\varphi(M_y)}{M_y}+M_y.
\]
After division by \(x\) and letting \(x\to\infty\),
\[
\limsup_{x\to\infty}\frac{\pi(x)}x
\le
\prod_{\ell\le y}\left(1-\frac1\ell\right).
\]
Moreover,
\[
\prod_{\ell\le y}\left(1-\frac1\ell\right)^{-1}
\ge \sum_{n\le y}\frac1n,
\]
because every \(n\le y\) has all prime factors at most \(y\). The harmonic sum diverges, so the product tends to zero as \(y\to\infty\). ∎

Thus Route 4-style constructions based on a fixed finite set of reservoir increments cannot work. Any successful reservoir must continually replenish itself with unboundedly many selected terms.

---

### 7. A rigorous form of the parity warning

Let \(\lambda(n)=(-1)^{\Omega(n)}\) be the Liouville function and define nonnegative weights
\[
w_+(n)=1+\lambda(n),\qquad
w_-(n)=1-\lambda(n).
\]
Then \(w_+\) vanishes on every prime, while \(w_-\) equals \(2\) on every prime.

For any fixed \(D\) and every \(d\le D\),
\[
\sum_{\substack{n\le x\\d\mid n}}w_\pm(n)
=
\frac{x}{d}+o(x).
\]
Indeed,
\[
\sum_{\substack{n\le x\\d\mid n}}\lambda(n)
=
\lambda(d)\sum_{m\le x/d}\lambda(m)
=o(x),
\]
using the classical prime-number-theorem consequence
\[
\sum_{m\le y}\lambda(m)=o(y).
\]

Thus the two nonnegative sequences have asymptotically identical divisibility statistics for every fixed finite collection of moduli, but one has no prime support. This is the basic parity phenomenon in a concrete form. It does not prove that every possible sieve strategy must fail, but it explains why fixed-level local data cannot establish the required prime lower bound.

---

### 8. Running ledger

**Proved lemmas**

1. Prime candidates are exactly the survivors of the sieve by primes up to \(\sqrt{2p-1}\).
2. Exact inclusion-exclusion and a full-discrepancy sufficient condition.
3. Odd-order Bonferroni lower bounds.
4. A sufficient von Mangoldt-correlation bound.
5. Terminal seeds can be arbitrarily dense among primes and exactly equidistributed modulo any prescribed fixed modulus.
6. A diagonal sequence of density-one, fixed-modulus-equidistributed terminal states exists.
7. The gcd of the increments \(q_i-1\) is invariant.
8. An infinite trajectory must use infinitely many distinct selected indices.

**Plausible but unproved**

1. For a favorable trajectory, one might have
   \[
   \sum_{i\le n}\Lambda(q_n+q_i-1)\gg n.
   \]
   This is exactly the kind of correlation currently unavailable.
2. The \((2)\) or \((3,5)\) trajectory may exhibit useful moving-level equidistribution. Fixed-level equidistribution would not suffice.
3. A specially engineered seed may have a self-replenishing structure using infinitely many new increments, but no invariant establishing this was found.

**Dead ends**

1. **Positive density among earlier primes:** Theorem 5 shows that even density arbitrarily close to \(1\) does not force extension.
2. **Equidistribution modulo fixed small primes:** Theorem 5 and Corollary 6 refute this as a sufficient condition.
3. **A fixed \(W\)-trick:** It removes finitely many prime divisors forever but cannot address factors up to \(\sqrt p\).
4. **A fixed finite reservoir:** Lemma 8 proves this cannot sustain an infinite trajectory.
5. **Ordinary lower-bound sieve:** At the square-root threshold it meets the parity problem; stopping below that threshold only produces rough or almost-prime candidates, not prime candidates.

## Self-Audit

1. **Theorem 5 uses the prime number theorem in fixed arithmetic progressions.**  
   I did not reprove that theorem. It is a standard unconditional result and is applied only for finitely many fixed moduli; no uniformity in a growing modulus is assumed. The CRT classes are explicitly reduced, so its hypotheses are satisfied.

2. **The terminal constructions do not rule out a recurrence-specific transference theorem for one favorable seed.**  
   They only prove that density and fixed-modulus equidistribution cannot be sufficient hypotheses. This limitation is explicit, and I do not claim the constructions disprove the original existential problem.

3. **The Liouville argument is a methodological parity obstruction, not a theorem that all conceivable sieve methods fail.**  
   It rigorously shows that fixed local divisibility data cannot distinguish prime support from even-parity support. The stronger claim that no enhanced recurrence-specific sieve can work is not made.

## Computations To Verify

The proofs above are theoretical, but the following code checks the exact sieve identities, trajectories, and finite terminal constructions.

```python
from math import gcd, isqrt, prod
from fractions import Fraction
from itertools import combinations
from sympy import isprime, factorint, primerange, totient, nextprime
from sympy.ntheory.modular import crt

def simulate(seed, generated_steps=100):
    Q = sorted(seed)
    assert len(Q) == len(set(Q))
    assert all(isprime(q) for q in Q)

    records = []
    for _ in range(generated_steps):
        p = Q[-1]
        selected = None

        for i, q in enumerate(Q):
            N = p + q - 1
            if isprime(N):
                selected = (i, q, N)
                break

        if selected is None:
            terminal = []
            for i, q in enumerate(Q):
                N = p + q - 1
                terminal.append((i, q, N, factorint(N)))
            return {
                "status": "terminal",
                "Q": Q,
                "records": records,
                "terminal_certificates": terminal,
            }

        i, q, N = selected
        earlier_composites = []
        for k in range(i):
            C = p + Q[k] - 1
            assert not isprime(C)
            earlier_composites.append((k, Q[k], C, factorint(C)))

        records.append({
            "p": p,
            "selected_index": i,
            "selected_q": q,
            "new_prime": N,
            "earlier_composites": earlier_composites,
        })
        Q.append(N)

    return {"status": "limit reached", "Q": Q, "records": records}
```

Exact verification of Lemmas 1–3:

```python
def exact_sieve_audit(Q, z_override=None, bonferroni_K=3):
    p = Q[-1]
    assert p >= 3 and p % 2 == 1
    h = p - 1
    X = 2 * p - 1
    z = isqrt(X) if z_override is None else z_override

    E = [q for q in Q if h % q != 0]
    L = [ell for ell in primerange(2, z + 1) if h % ell != 0]
    P = prod(L, start=1)

    survivors = [q for q in E if gcd(h + q, P) == 1]
    prime_candidates = [q for q in E if isprime(h + q)]

    if z == isqrt(X):
        assert survivors == prime_candidates

    # Exact inclusion-exclusion; feasible only when len(L) is modest.
    inclusion_sum = 0
    main_term = Fraction(0, 1)
    signed_error = Fraction(0, 1)

    for r in range(len(L) + 1):
        for subset in combinations(L, r):
            d = prod(subset, start=1)
            A_d = sum((h + q) % d == 0 for q in E)
            mu_d = -1 if r % 2 else 1

            inclusion_sum += mu_d * A_d

            expected = Fraction(len(E), int(totient(d)))
            main_term += mu_d * expected
            signed_error += mu_d * (Fraction(A_d, 1) - expected)

    assert inclusion_sum == len(survivors)
    assert Fraction(inclusion_sum, 1) == main_term + signed_error

    K = bonferroni_K
    assert K % 2 == 1
    bonferroni = 0
    for r in range(min(K, len(L)) + 1):
        for subset in combinations(L, r):
            d = prod(subset, start=1)
            A_d = sum((h + q) % d == 0 for q in E)
            bonferroni += (-1 if r % 2 else 1) * A_d

    assert bonferroni <= len(survivors)

    V = Fraction(1, 1)
    for ell in L:
        V *= Fraction(ell - 2, ell - 1)

    return {
        "p": p,
        "z": z,
        "eligible_count": len(E),
        "sieve_primes": L,
        "survivor_count": len(survivors),
        "prime_candidate_count": len(prime_candidates),
        "V": V,
        "expected_main_term": len(E) * V,
        "bonferroni_lower_bound": bonferroni,
    }
```

The small terminal example:

```python
Q = [2, 7, 17, 29]
out = simulate(Q, generated_steps=1)
assert out["status"] == "terminal"

assert [29 + q - 1 for q in Q] == [30, 35, 45, 57]
print(out["terminal_certificates"])
```

A brute-force version of the terminal-seed construction from Theorem 5:

```python
def primes_in_union_below(c, W, L, p):
    """
    Primes q < p with q == c mod W and q == 2 mod ell
    for at least one ell in L.
    """
    ans = set()

    for ell in L:
        a, modulus = crt([W, ell], [c, 2])
        a, modulus = int(a), int(modulus)

        q = a
        if q < 2:
            q += ((2 - q + modulus - 1) // modulus) * modulus

        while q < p:
            if isprime(q):
                ans.add(q)
            q += modulus

    return sorted(ans)


def construct_balanced_terminal_seed(W, eps=0.25, minimum_per_class=1):
    assert W % 2 == 0
    assert 0 < eps < 1

    # Choose covering primes L with product survival factor < eps/2.
    L = []
    survival = 1.0
    ell = 5

    while survival >= eps / 2:
        if gcd(ell, W) == 1:
            L.append(ell)
            survival *= (ell - 2) / (ell - 1)
        ell = int(nextprime(ell))

    # Prime k kills the self-candidate.
    k = int(nextprime(max(L)))
    while gcd(k, W) != 1 or k in L:
        k = int(nextprime(k))

    mods = [W] + L + [k]
    residues = [1] + [ell - 1 for ell in L] + [(k + 1) // 2]
    a, M = crt(mods, residues)
    a, M = int(a), int(M)

    reduced_classes = [c for c in range(W) if gcd(c, W) == 1]

    p = a
    if p < max(L + [k]) + 10:
        p += ((max(L + [k]) + 10 - p + M - 1) // M) * M

    while True:
        if isprime(p):
            pools = {
                c: primes_in_union_below(c, W, L, p)
                for c in reduced_classes
            }
            t = min(len(pool) for pool in pools.values())

            if t >= minimum_per_class:
                earlier = []
                for c in reduced_classes:
                    earlier.extend(pools[c][:t])
                earlier = sorted(earlier)
                Q = earlier + [p]

                # Exact balance modulo W.
                counts = {
                    c: sum(q % W == c for q in earlier)
                    for c in reduced_classes
                }
                assert len(set(counts.values())) == 1

                # Every earlier candidate is covered by L.
                for q in earlier:
                    N = p + q - 1
                    assert any(N % ell == 0 and N > ell for ell in L)

                # Self-candidate is covered by k.
                assert (2 * p - 1) % k == 0
                assert 2 * p - 1 > k

                return {
                    "seed": Q,
                    "terminal_prime": p,
                    "covering_primes": L,
                    "self_factor": k,
                    "count_per_W_class": t,
                    "density_ratio": len(earlier) /
                                     sum(isprime(r) for r in range(2, p + 1)),
                }

        p += M
```

The CRT modulus grows quickly, so this last brute-force search is only practical for small parameters. For proof-quality finite output, replace generic primality calls with ECPP or Pratt certificates and record explicit factors of every composite candidate.

## Route Diagnosis

The exact sieve worked cleanly: at a state \(p\), extension is precisely survival after sieving to \(\sqrt{2p-1}\), with expected main term approximately
\[
\frac{n}{\log p}
\prod_{\ell\mid p-1}\frac{\ell-1}{\ell-2}.
\]
What failed is the lower bound. Fixed-modulus density and equidistribution are decisively insufficient: terminal seeds can satisfy them with relative density tending to \(1\). Sieving only to \(p^\theta\) with \(\theta<1/2\) leaves composites and almost-primes; reaching the square-root threshold encounters the classical parity obstruction. Even for the unrestricted set of all primes \(q\le p\), proving for every relevant \(p\) that some \(p+q-1\) is prime is an unresolved growing-shift prime-pair problem.

A fresh Route 2 attempt therefore needs information qualitatively stronger than residue equidistribution: a direct lower bound for
\[
\sum_{i\le n}\Lambda(q_n+q_i-1),
\]
or an equivalent bilinear/correlation estimate exploiting special recurrence structure. No such structure was found. A seed-construction alternative must use infinitely many genuinely new increments, by Lemma 8; a fixed finite reservoir is impossible.