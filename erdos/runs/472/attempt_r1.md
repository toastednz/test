STATUS: BLOCKED

## Result

Route 1 yields rigorous conditional growth control but does not establish nontermination. In the additive variables \(a_n=q_n-1\), I prove that if the selected indices are eventually bounded away from \(n\), then \(\log q_n=o(n)\); if \(j_n\le n^\beta\) eventually, then \(q_n\le n^{1/(1-\beta)}(\log n)^{O(1)}\); and if \(j_n=n^{o(1)}\), then \(q_n=n^{1+o(1)}\). However, slow growth alone cannot force extension: for every \(m\ge2\), the seed consisting of the first \(m\) primes congruent to \(2\bmod 3\) is immediately terminal, despite having \(q_m\sim2m\log m\). I also prove that no infinite trajectory can use only finitely many selected indices, and that consecutive self-selections are necessarily finite. The missing step remains a lower bound for primes in the adaptive translate set \(\{q_n+q_i-1\}\), a subset-sensitive prime-pair assertion beyond present sieve methods.

## Complete Argument

### 1. Additive formulation

Put
\[
a_i=q_i-1.
\]
All \(a_i\) are positive integers, and whenever the process extends,
\[
a_{n+1}=a_n+a_{j_n}.
\]
Since \(j_n\le n\) and \(a_i\) is increasing,
\[
a_n<a_{n+1}\le 2a_n.
\]
Thus
\[
\limsup_{n\to\infty}\frac{\log a_n}{n}\le \log 2
\]
for every infinite trajectory.

The following results apply to any positive increasing sequence satisfying this additive recurrence; primality is used only to ensure that a selected index exists.

---

### 2. An early-index growth theorem

#### Proposition 1

Suppose an infinite trajectory satisfies
\[
j_n\le \alpha n
\]
for all sufficiently large \(n\), where \(0<\alpha<1\). Then
\[
\log a_n=o(n).
\]

#### Proof

Let
\[
L=\limsup_{n\to\infty}\frac{\log a_n}{n}.
\]
The doubling bound gives \(0\le L\le\log2\).

Choose \(\lambda\) with
\[
1<\lambda<\frac1\alpha.
\]
For a sufficiently large integer \(m\), put
\[
N=\left\lceil\frac m\lambda\right\rceil.
\]
For every \(k\) with \(N\le k<m\),
\[
j_k\le\alpha k<\alpha m\le\alpha\lambda N<N
\]
once rounding errors are absorbed by taking \(m\) sufficiently large. Therefore \(a_{j_k}\le a_N\), and
\[
a_m
 =a_N+\sum_{k=N}^{m-1}a_{j_k}
 \le a_N+(m-N)a_N
 \le m a_N.
\]
For every \(\varepsilon>0\), the definition of \(L\) gives
\[
\log a_N\le (L+\varepsilon)N
\]
for all sufficiently large \(N\). Hence
\[
\frac{\log a_m}{m}
 \le \frac{\log m}{m}+\frac{N}{m}(L+\varepsilon).
\]
Taking the limsup as \(m\to\infty\),
\[
L\le \frac{L+\varepsilon}{\lambda}.
\]
Letting \(\varepsilon\to0\) gives \(L\le L/\lambda\). Since \(\lambda>1\), this forces \(L=0\). ∎

Thus any positive exponential growth rate would force
\[
\limsup_{n\to\infty}\frac{j_n}{n}=1.
\]

---

### 3. Polynomial growth from polynomially early indices

#### Proposition 2

Let \(0\le\beta<1\). If
\[
j_n\le n^\beta
\]
for all sufficiently large \(n\), then
\[
\log a_n\le \frac{\log n}{1-\beta}+O(\log\log n),
\]
and consequently
\[
a_n\le n^{1/(1-\beta)}(\log n)^{O(1)}.
\]

#### Proof

The case \(\beta=0\) is immediate: eventually \(j_n=1\), so \(a_n\) grows linearly. Assume \(0<\beta<1\).

Choose \(N\) such that \(j_k\le k^\beta\) for all \(k\ge N\). For \(t\ge N\),
\[
a_t=a_N+\sum_{k=N}^{t-1}a_{j_k}
 \le a_N+t\,a_{\lceil t^\beta\rceil}.
\]
Since \(a_{\lceil t^\beta\rceil}\ge a_1>0\), there is a constant \(C\), independent of \(t\), such that
\[
a_t\le Ct\,a_{\lceil t^\beta\rceil}. \tag{1}
\]

Starting with \(t_0=n\), define
\[
t_{r+1}=\lceil t_r^\beta\rceil
\]
until \(t_R\) falls below a sufficiently large fixed threshold \(T\). Iterating (1) gives
\[
a_n\le C^R\left(\prod_{r=0}^{R-1}t_r\right)
       \max_{u<T}a_u. \tag{2}
\]

For \(t_r\ge T\), choose \(T\) large enough that
\[
t_{r+1}\le 2t_r^\beta.
\]
Writing \(u_r=\log t_r\), we have
\[
u_{r+1}\le\beta u_r+\log2.
\]
It follows by induction that
\[
u_r\le \beta^r u_0+\frac{\log2}{1-\beta}.
\]
Moreover, while \(t_r\ge T\), one may choose a fixed \(\gamma\in(\beta,1)\) and enlarge \(T\) so that \(u_{r+1}\le\gamma u_r\). Hence
\[
R=O(\log\log n).
\]
Also,
\[
\sum_{r=0}^{R-1}u_r
 \le \frac{u_0}{1-\beta}+O(R)
 =\frac{\log n}{1-\beta}+O(\log\log n).
\]
Taking logarithms in (2) proves the result. ∎

#### Corollary 3

If
\[
j_n=n^{o(1)},
\]
then
\[
a_n=n^{1+o(1)}
\qquad\text{and hence}\qquad
q_n=n^{1+o(1)}.
\]

#### Proof

For every fixed \(\beta>0\), eventually \(j_n\le n^\beta\). Proposition 2 therefore gives
\[
\limsup_{n\to\infty}\frac{\log a_n}{\log n}\le\frac1{1-\beta}.
\]
Letting \(\beta\to0\) gives an upper bound of \(1\). Conversely,
\[
a_n=a_m+\sum_{k=m}^{n-1}a_{j_k}
 \ge a_m+(n-m)a_1,
\]
so
\[
\liminf_{n\to\infty}\frac{\log a_n}{\log n}\ge1.
\]
Thus the ratio tends to \(1\). ∎

In particular, the empirical-looking bound \(j_n=O(\log n)\) would imply \(q_n=n^{1+o(1)}\).

Because \(q_1,\dots,q_n\) are \(n\) distinct increasing primes, the prime number theorem also gives
\[
q_n\ge (1+o(1))n\log n.
\]
Thus under \(j_n=n^{o(1)}\), one would have
\[
n\log n\ll q_n\le n^{1+o(1)}.
\]

---

### 4. What a bound \(j_n=O(\log q_n)\) would imply

The form suggested in Route 1 is \(j_n\ll\log q_n\). There is a sharp limitation to what the additive recurrence alone can deduce from this.

#### Proposition 4

Suppose for some fixed \(C>0\),
\[
j_n\le C\log a_n
\]
eventually. Put
\[
L=\limsup_{n\to\infty}\frac{\log a_n}{n}.
\]
Then either
\[
L=0
\]
or
\[
L\ge\frac1C.
\]
In particular, if \(C<1/\log2\), then \(L=0\).

#### Proof

If \(0<L<1/C\), choose \(\varepsilon>0\) such that
\[
C(L+\varepsilon)<1.
\]
For all sufficiently large \(n\),
\[
\log a_n\le(L+\varepsilon)n,
\]
so
\[
j_n\le C(L+\varepsilon)n=\alpha n
\]
with \(\alpha<1\). Proposition 1 then gives \(L=0\), a contradiction.

Finally, \(L\le\log2\). If \(C<1/\log2\), then the alternative \(L\ge1/C\) is impossible. ∎

This dichotomy cannot be improved using only the abstract additive recurrence: the model sequence \(a_n=2^n\), \(j_n=n\), satisfies
\[
j_n=\frac{\log a_n}{\log2}.
\]
Primality would have to supply the additional input excluding such behavior.

---

### 5. Slow growth and many candidates do not force a prime

The central obstruction to bootstrapping the preceding estimates is elementary and severe.

#### Proposition 5: dense terminal seeds

For every \(m\ge2\), there is an immediately terminal seed of length \(m\). More precisely, let
\[
q_1<\cdots<q_m
\]
be the first \(m\) primes congruent to \(2\bmod3\). Then the process terminates at \(q_m\).

Moreover, by the prime number theorem in arithmetic progressions,
\[
q_m\sim2m\log m.
\]

#### Proof

Since \(m\ge2\), the current prime \(p=q_m\) is at least \(5\). For every \(i\le m\),
\[
p+q_i-1\equiv2+2-1\equiv0\pmod3.
\]
Also,
\[
p+q_i-1\ge5+2-1=6>3.
\]
Therefore every candidate is a composite multiple of \(3\), including the self-candidate \(2p-1\). Hence the state is terminal.

There are infinitely many primes congruent to \(2\bmod3\); this also follows from the usual Euclidean argument. The quantitative asymptotic is the standard consequence
\[
\pi(x;3,2)\sim\frac{x}{2\log x}
\]
of the prime number theorem in arithmetic progressions, inverted at the \(m\)-th such prime. ∎

Since the smallest possible \(m\)-th prime is asymptotic to \(m\log m\), these terminal seeds have essentially minimal possible growth, up to a factor \(2\). Therefore no assertion of the form

> “if \(q_n\) is subexponential/polynomial/\(n^{1+o(1)}\) and there are \(n\) candidates, one candidate must be prime”

can be true without substantial residue-distribution hypotheses.

There is an even more flexible obstruction.

#### Proposition 6: any fixed reservoir can be killed

Let \(d_1,\dots,d_k\) be fixed positive integers. There exist arbitrarily large primes \(p\) such that
\[
p+d_i
\]
is composite for every \(i\), and \(2p-1\) is composite.

Consequently, given any fixed list of earlier seed primes \(r_1,\dots,r_k\), one can append an arbitrarily large prime \(p\) so that the resulting seed is terminal.

#### Proof

Choose distinct odd primes
\[
\ell_0,\ell_1,\dots,\ell_k
\]
such that \(\ell_i\nmid d_i\) for \(i\ge1\). Impose the congruences
\[
p\equiv 2^{-1}\pmod{\ell_0},
\qquad
p\equiv-d_i\pmod{\ell_i}\quad(1\le i\le k).
\]
By the Chinese remainder theorem, these define a residue class \(b\bmod M\), where
\[
M=\prod_{i=0}^k\ell_i.
\]
Every prescribed residue is nonzero modulo its corresponding prime, so \(\gcd(b,M)=1\). Dirichlet’s theorem therefore gives infinitely many primes
\[
p\equiv b\pmod M.
\]
Choose one larger than every \(\ell_i\) and every \(d_i\). Then
\[
\ell_i\mid p+d_i,\qquad p+d_i>\ell_i,
\]
so each \(p+d_i\) is composite. Likewise,
\[
\ell_0\mid2p-1,\qquad 2p-1>\ell_0,
\]
so the self-candidate is composite.

For earlier primes \(r_i\), take \(d_i=r_i-1\). ∎

This proposition does not show that a generated trajectory can be forced into such a state. It shows that cardinality and the mere presence of a fixed reservoir cannot provide a uniform extension theorem.

---

### 6. An infinite trajectory cannot use a finite reservoir

#### Proposition 7

If a trajectory is infinite, then the selected indices \(j_n\) are unbounded. Equivalently, infinitely many distinct earlier terms must eventually be used as selected increments.

#### Proof

Suppose instead that \(j_n\le K\) eventually. Put
\[
A=a_K=q_K-1.
\]
Then eventually
\[
q_{n+1}-q_n=a_{j_n}\le A. \tag{3}
\]

There are arbitrarily long intervals containing no primes. Explicitly, choose an integer \(L>A+1\). Then
\[
L!+2,L!+3,\dots,L!+A+1
\]
are all composite. Choose \(L\) so large that this interval lies beyond the stage from which (3) holds.

An infinite increasing sequence of primes must eventually cross this interval. If \(q_n\) is the last trajectory term at most \(L!+1\), then the next term must satisfy
\[
q_{n+1}\ge L!+A+2,
\]
and consequently
\[
q_{n+1}-q_n\ge A+1,
\]
contradicting (3). ∎

Thus Route 4 cannot work with a genuinely finite reservoir that alone supplies all future increments; any successful engineered seed would have to replenish it with unboundedly many new usable indices.

---

### 7. Consecutive self-selection cannot persist

The self-candidate \(2q_n-1\) can occasionally be selected, but it cannot support an infinite trajectory by itself.

#### Proposition 8

Let \(p=q_n\) be an odd prime. If consecutive self-selections start at \(p\), their number is strictly less than
\[
\operatorname{ord}_p(2),
\]
the multiplicative order of \(2\bmod p\).

#### Proof

After \(t\) consecutive self-transitions,
\[
q_{n+t}-1=2^t(p-1),
\]
so
\[
q_{n+t}=1+2^t(p-1). \tag{4}
\]
Let \(d=\operatorname{ord}_p(2)\). Then \(2^d\equiv1\bmod p\), and (4) gives
\[
q_{n+d}\equiv1+(p-1)\equiv0\pmod p.
\]
Since \(q_{n+d}>p\), this number is composite. Hence \(d\) consecutive self-transitions are impossible. ∎

The bound \(d\le p-1\) is far too large to yield useful global growth control, so this does not exclude long exponential bursts.

---

### 8. Precise point at which Route 1 blocks

The growth lemmas are conditional on \(j_n\) existing. At a proposed next stage, one must first prove that at least one of
\[
a_n+a_i+1=q_n+q_i-1
\]
is prime. Bounds on earlier selected indices control the size of \(q_n\), but they do not themselves prove this prime-existence statement.

Even if all primes \(r\le p\) were available, the required assertion would be
\[
\exists r\le p:\quad r\in\mathbb P,\qquad r+p-1\in\mathbb P.
\]
This is a prime-pair problem with the growing prescribed difference \(p-1\). In the actual recurrence, \(r\) must additionally lie in a sparse adaptive subset of the primes. A lower-bound sieve for this correlation encounters the parity obstruction, while Proposition 5 shows that growth and candidate count alone are insufficient.

No invariant was found for the \((2)\) or \((3,5)\) trajectory that both:

1. is preserved under the deterministic smallest-candidate choice, and
2. is strong enough to force a prime candidate at the next stage.

Thus the remaining assertion is of essentially the same strength as nontermination for the chosen seed, and Route 1 is blocked.

## Self-Audit

1. **The polynomial-growth conclusions are entirely conditional.**  
   I have not proved \(j_n\le n^\beta\), \(j_n=O(\log n)\), or even \(j_n\le\alpha n\) for the \((3,5)\) trajectory. The deductions from these assumptions are rigorous, but they do not cross a terminal stage.

2. **The asymptotic \(q_m\sim2m\log m\) for the terminal family invokes the prime number theorem in arithmetic progressions.**  
   This is a standard unconditional theorem. More importantly, the existence and terminality of the family are elementary and do not depend on that asymptotic.

3. **“Parity obstruction” is a diagnosis of available methods, not a theorem that no clever lower bound can exist.**  
   The concrete mathematical evidence is stronger than a heuristic: Proposition 5 rules out every extension criterion based only on slow growth and candidate count, while the remaining required statement is explicitly a growing-shift prime-pair lower bound on an adaptive subset.

## Computations To Verify

```python
from math import log
from itertools import combinations
from sympy import isprime, primerange, factorint
from sympy.ntheory import n_order

def simulate(seed, generated_steps):
    Q = list(seed)
    assert Q == sorted(set(Q))
    assert all(isprime(q) for q in Q)

    records = []
    for _ in range(generated_steps):
        p = Q[-1]
        candidates = [p + r - 1 for r in Q]
        prime_indices = [i for i, N in enumerate(candidates) if isprime(N)]

        if not prime_indices:
            return Q, records, {
                "terminal": True,
                "current": p,
                "candidate_factors": [factorint(N) for N in candidates],
            }

        j = prime_indices[0]
        # Factors certifying minimality for moderate-sized computations.
        earlier_factors = [factorint(candidates[i]) for i in range(j)]

        records.append({
            "n": len(Q),
            "current": p,
            "selected_index_1_based": j + 1,
            "selected_prime": Q[j],
            "next": candidates[j],
            "number_prime_candidates": len(prime_indices),
            "earlier_candidate_factors": earlier_factors,
            "j_over_log_p": (j + 1) / log(p),
            "log_p_over_n": log(p) / len(Q),
        })
        Q.append(candidates[j])

    return Q, records, {"terminal": False}

# Route-1 trajectory statistics.
Q, records, status = simulate([3, 5], 10000)
for rec in records[:50]:
    print(rec["n"], rec["current"],
          rec["selected_index_1_based"],
          rec["next"],
          rec["j_over_log_p"],
          rec["log_p_over_n"])
print(status)

# Verify the congruence-terminal family.
def primes_2_mod_3(count):
    ans = []
    x = 2
    while len(ans) < count:
        if isprime(x) and x % 3 == 2:
            ans.append(x)
        x += 1
    return ans

Qmod3 = primes_2_mod_3(1000)
for m in range(2, len(Qmod3) + 1):
    seed = Qmod3[:m]
    p = seed[-1]
    for r in seed:
        N = p + r - 1
        assert N % 3 == 0
        assert N > 3
        assert not isprime(N)
print("All tested 2 mod 3 seeds are terminal.")

# Verify the consecutive-self bound for small starting primes.
for p in list(primerange(3, 10000)):
    d = n_order(2, p)
    transitions = 0
    q = p
    while isprime(2*q - 1):
        q = 2*q - 1
        transitions += 1
        if transitions > d:
            raise AssertionError((p, d, transitions))
    assert transitions < d
print("Self-run order bound verified in tested range.")

# Exhaustive bounded seed search.
def bounded_seed_search(B, max_m, steps):
    primes = list(primerange(2, B + 1))
    output = []
    for m in range(1, max_m + 1):
        for seed in combinations(primes, m):
            Q, records, state = simulate(seed, steps)
            output.append({
                "seed": seed,
                "generated": len(Q) - m,
                "terminal": state["terminal"],
                "last": Q[-1],
                "max_selected_index":
                    max((r["selected_index_1_based"] for r in records),
                        default=None),
            })
    return output

# Example:
# results = bounded_seed_search(B=50, max_m=4, steps=1000)
# print(sorted(results, key=lambda x: x["generated"], reverse=True)[:20])

# Sieve-survivor statistics for a state.
def candidate_sieve_stats(Q, z):
    p = Q[-1]
    small_primes = list(primerange(2, z + 1))
    data = []
    for i, r in enumerate(Q):
        N = p + r - 1
        divisor = next((ell for ell in small_primes
                        if N != ell and N % ell == 0), None)
        data.append((i + 1, r, N, divisor, isprime(N)))
    return data

# Example on the last computed state:
# stats = candidate_sieve_stats(Q, int(Q[-1]**0.25))
# survivors = [row for row in stats if row[3] is None]
# print(len(stats), len(survivors),
#       sum(row[4] for row in stats))
```

## Route Diagnosis

**Proved ledger**

- Eventual \(j_n\le\alpha n\), \(\alpha<1\), implies \(\log q_n=o(n)\).
- Eventual \(j_n\le n^\beta\) implies \(q_n\le n^{1/(1-\beta)}(\log n)^{O(1)}\).
- \(j_n=n^{o(1)}\) implies \(q_n=n^{1+o(1)}\).
- A bound \(j_n\le C\log q_n\) gives a zero-or-large exponential-growth dichotomy.
- There are immediately terminal seeds of every length \(m\ge2\), with largest term asymptotic to \(2m\log m\).
- Any fixed finite set of increments can be simultaneously defeated at arbitrarily large prime current terms.
- An infinite trajectory must use unboundedly many selected indices.
- Consecutive self-selection is always finite.

**Plausible but unproved**

- For the \((3,5)\) trajectory, \(j_n\) may be polylogarithmic or \(n^{o(1)}\).
- Its terms may be sufficiently equidistributed modulo small primes to leave the expected number of sieve survivors.
- The number of actual prime candidates may follow a Hardy–Littlewood-type main term.

**Dead ends**

- Slow growth or near-maximal candidate count alone: refuted by the \(2\bmod3\) terminal family.
- A permanently fixed reservoir: impossible by arbitrarily long prime gaps.
- Repeated self-candidates: impossible indefinitely and still gives no controlled alternative.
- Ordinary lower-bound sieving: blocked by the need to distinguish primes from numbers with an even number of prime factors.

A fresh Route 1 attempt needs a genuinely dynamical invariant for a particular seed—most likely quantitative residue distribution plus additional structure overcoming the parity problem. Without such an invariant, the required “abundance of candidates” lemma is essentially the original problem restated.