STATUS: BLOCKED

## Result

Route 2 yields several rigorous necessary conditions. In any perfect-power configuration, the rightmost interval \([a,B]\) must satisfy \(a>|[a,B]|\). If the product is a \(q\)-th power and \(L\) is the maximum block length, then every prime \(p>L\) occurring in the product must occur to exponent at least \(\lceil q/r\rceil\) in some single selected integer. Consequently, all selected integers are \(\max\{L,B^{1/\lceil q/r\rceil}\}\)-smooth. Combining this with Sylvester’s theorem gives an explicit endpoint lower bound, notably \(B\ge (l+1)^{\lceil q/r\rceil}\) when the rightmost block has maximal length \(l\). However, arbitrary gaps permit \(B\) to be arbitrarily large. Moreover, exact CRT constructions show that any fixed finite set of prime valuations can be neutralized modulo \(q\), and that arbitrarily long translated intervals can have every term divisible by a prescribed large prime power. Thus elementary large-prime density and finite-sieve approaches do not close the problem. The square case \(q=2\), already containing the square-binomial obstruction, remains completely untouched by the concentration estimate.

## Complete Argument

Let
\[
U=\bigcup_{i=1}^r I_i,\qquad
I_i=[a_i,b_i],\qquad
\ell_i=b_i-a_i+1,
\]
and let
\[
P=\prod_{m\in U}m,\qquad
B=\max U,\qquad
L=\max_i\ell_i.
\]

The following statements are unconditional.

### 1. The rightmost block must start beyond its own length

**Lemma 1.**  
Suppose \(P\) is a perfect power. After ordering the intervals from left to right, write the rightmost interval as
\[
I_r=[a,B],\qquad \ell=B-a+1.
\]
Then
\[
a>\ell.
\]

**Proof.**  
Assume instead that \(a\le\ell\). Since \(\ell=B-a+1\), this gives
\[
2a\le B+1.
\]
Hence \(I_r\) contains every integer from \(\lceil B/2\rceil\) to \(B\).

Because a nontrivial perfect power has \(B\ge2\), Bertrand’s postulate supplies a prime \(p\) satisfying
\[
\frac B2<p\le B.
\]
Thus \(p\in I_r\). Since every selected integer is at most \(B\) and \(2p>B\), the only selected multiple of \(p\) is \(p\) itself. Also \(p^2>B\). Therefore
\[
v_p(P)=1,
\]
contradicting that \(P\) is a perfect power. Hence \(a>\ell\). ∎

This is a useful structural fact: every putative counterexample has a genuinely far-right last block, so the classical Sylvester theorem applies to that block.

---

### 2. Concentration of large-prime valuations

**Lemma 2.**  
Suppose \(P\) is a \(q\)-th power for an integer \(q\ge2\). If \(p>L\) and \(p\mid P\), then some selected integer \(m\in U\) satisfies
\[
p^{\,\lceil q/r\rceil}\mid m.
\]

**Proof.**  
Because \(p>L\ge\ell_i\), each interval contains at most one multiple of \(p\). Thus at most \(r\) selected integers are divisible by \(p\). List them as
\[
m_1,\dots,m_t,\qquad 1\le t\le r,
\]
and put \(e_j=v_p(m_j)\ge1\). Since \(P\) is a \(q\)-th power,
\[
e_1+\cdots+e_t=v_p(P)
\]
is a positive multiple of \(q\), and hence is at least \(q\). Therefore
\[
\max_j e_j\ge \left\lceil\frac qt\right\rceil
\ge \left\lceil\frac qr\right\rceil.
\]
The corresponding \(m_j\) is divisible by \(p^{\lceil q/r\rceil}\). ∎

This gives the following smoothness restriction.

**Corollary 3.**  
Put
\[
s=\left\lceil\frac qr\right\rceil.
\]
If \(P\) is a \(q\)-th power, then every prime factor of every selected integer is at most
\[
\max\{L,B^{1/s}\}.
\]

**Proof.**  
Let \(p>L\) divide a selected integer. By Lemma 2, some selected integer is divisible by \(p^s\). Since all selected integers are at most \(B\),
\[
p^s\le B,
\]
so \(p\le B^{1/s}\). Primes not exceeding \(L\) already satisfy the asserted bound. ∎

In particular, when \(q>r\), one has \(s\ge2\). Thus every prime exceeding \(L\) must be supported somewhere by a square or higher power of that same prime.

A useful contrapositive is:

> If \(q>r\) and some selected integer has a prime factor
> \[
> p>\max\{L,B^{1/\lceil q/r\rceil}\},
> \]
> then \(P\) is not a \(q\)-th power.

The difficulty is that no such prime factor is known to exist uniformly in arbitrary translated intervals.

---

### 3. A length-sensitive refinement

The preceding argument can be applied to a prime which is larger than one particular block length, without requiring it to exceed all block lengths.

**Lemma 4.**  
Let \(I_h=[a_h,b_h]\) have length \(\ell=\ell_h\), and suppose \(a_h>\ell\). Define
\[
C_h=\sum_{i=1}^r
\left\lceil\frac{\ell_i}{\ell+1}\right\rceil.
\]
If \(P\) is a \(q\)-th power, then
\[
B\ge(\ell+1)^{\lceil q/C_h\rceil}.
\]

**Proof.**  
The classical Sylvester theorem says that a product of \(\ell\) consecutive integers, all greater than \(\ell\), has a prime divisor exceeding \(\ell\). Thus there is a prime \(p>\ell\) dividing the product over \(I_h\).

An interval of length \(\ell_i\) contains at most
\[
\left\lceil\frac{\ell_i}{p}\right\rceil
\le
\left\lceil\frac{\ell_i}{\ell+1}\right\rceil
\]
multiples of \(p\). Hence the total number \(t\) of selected multiples of \(p\) satisfies
\[
t\le C_h.
\]

As in Lemma 2, the positive integer \(v_p(P)\) is at least \(q\). Consequently, one of these \(t\) selected multiples has \(p\)-adic valuation at least
\[
\left\lceil\frac qt\right\rceil
\ge
\left\lceil\frac q{C_h}\right\rceil.
\]
Some selected integer is therefore divisible by
\[
p^{\lceil q/C_h\rceil}.
\]
Since it is at most \(B\) and \(p\ge\ell+1\),
\[
B\ge p^{\lceil q/C_h\rceil}
\ge(\ell+1)^{\lceil q/C_h\rceil}.
\]
∎

By Lemma 1, this applies in every putative counterexample to the rightmost interval.

If the rightmost interval also has maximal length \(\ell=L\), then every summand defining \(C_h\) equals \(1\), so \(C_h=r\). Therefore:

**Corollary 5.**  
If the rightmost block has maximal length \(L\) and \(P\) is a \(q\)-th power, then
\[
B\ge (L+1)^{\lceil q/r\rceil}.
\]
Equivalently,
\[
q\le
r\left\lfloor\frac{\log B}{\log(L+1)}\right\rfloor.
\]

In particular, if \(q>r\), then necessarily
\[
B\ge(L+1)^2.
\]

This excludes high perfect-power exponents when the endpoint is polynomially controlled by the block length, but the original problem imposes no such endpoint bound.

---

### 4. Exact finite-prime valuation steering

The following shows why a sieve based on any predetermined finite set of primes cannot be uniform in the endpoints.

**Lemma 6.**  
Fix a length \(\ell\ge1\), an integer \(q\ge2\), a finite set of primes \(S\), and prescribed residues
\[
c_p\in\mathbb Z/q\mathbb Z\qquad(p\in S).
\]
There are arbitrarily large positive integers \(a\) such that
\[
v_p\!\left(\prod_{j=0}^{\ell-1}(a+j)\right)
\equiv c_p\pmod q
\]
for every \(p\in S\).

**Proof.**  
For each \(p\in S\), put
\[
C_p=v_p((\ell-1)!).
\]
Choose \(E_p\) sufficiently large that
\[
E_p>\max_{1\le j<\ell}v_p(j)
\]
and
\[
E_p+C_p\equiv c_p\pmod q.
\]
Such \(E_p\) exist because one may increase \(E_p\) by multiples of \(q\).

Impose
\[
a\equiv p^{E_p}\pmod {p^{E_p+1}}
\qquad(p\in S).
\]
These moduli are pairwise coprime, so the Chinese remainder theorem gives a common residue class for \(a\), containing arbitrarily large positive integers.

For such an \(a\),
\[
v_p(a)=E_p.
\]
For \(1\le j<\ell\), one has \(v_p(j)<E_p=v_p(a)\). The elementary \(p\)-adic identity
\[
v_p(x+y)=\min\{v_p(x),v_p(y)\}
\quad\text{when }v_p(x)\ne v_p(y)
\]
therefore gives
\[
v_p(a+j)=v_p(j).
\]
Hence
\[
v_p\!\left(\prod_{j=0}^{\ell-1}(a+j)\right)
=E_p+\sum_{j=1}^{\ell-1}v_p(j)
=E_p+C_p
\equiv c_p\pmod q.
\]
∎

**Corollary 7.**  
For any fixed lengths \(\ell_1,\dots,\ell_r\), any finite set \(S\) of primes, and any \(q\ge2\), there are arbitrarily far-right pairwise disjoint intervals of those lengths such that
\[
v_p(P)\equiv0\pmod q
\qquad(p\in S).
\]

**Proof.**  
Apply Lemma 6 to each block with every target residue equal to \(0\). Each resulting CRT residue class contains arbitrarily large representatives, so the starts can be chosen successively to ensure disjointness. ∎

More strongly, after some blocks have already been chosen, Lemma 6 can make a new block cancel all their valuations modulo \(q\) on any finite set of primes. The new block generally introduces new prime divisors, so this does not construct a perfect power; it proves that a finite-prime sieve necessarily leaves an uncontrolled tail.

---

### 5. Arbitrarily long runs covered by large prime powers

A second obstacle is that high prime powers are not uniformly sparse in translated intervals once boundary errors are allowed.

**Lemma 8.**  
For every \(\ell\ge1\) and \(s\ge2\), there are arbitrarily large \(a\) and distinct primes
\[
p_0,\dots,p_{\ell-1}>\ell
\]
such that
\[
v_{p_j}(a+j)=s
\qquad(0\le j<\ell).
\]
Moreover, \(p_j\) divides no other member of the interval
\[
[a,a+\ell-1].
\]

**Proof.**  
Choose distinct primes \(p_j>\ell\), and impose
\[
a+j\equiv p_j^s\pmod {p_j^{s+1}},
\]
or equivalently
\[
a\equiv p_j^s-j\pmod {p_j^{s+1}},
\qquad 0\le j<\ell.
\]
The moduli are pairwise coprime, so CRT gives arbitrarily large solutions \(a\). The congruence gives
\[
v_{p_j}(a+j)=s.
\]

If \(k\ne j\), then
\[
a+k\equiv k-j\pmod {p_j}.
\]
Since \(0<|k-j|<\ell<p_j\), this is nonzero modulo \(p_j\). Thus \(p_j\nmid a+k\). ∎

Therefore one cannot prove the needed unmatched-prime statement merely by arguing that multiples of \(p^s\) have small natural density. The usual estimate
\[
\#\{n\in[a,a+\ell-1]:p^s\mid n\}
\le\frac{\ell}{p^s}+1
\]
has a boundary term \(1\) for each prime, and CRT can realize those boundary terms simultaneously.

This lemma does **not** satisfy the full concentration condition from Lemma 2: the terms may have additional, unprescribed large prime factors. Controlling all such cofactors simultaneously is exactly the unresolved point.

---

### 6. Counterexamples to stronger large-prime assertions

Several tempting strengthenings of Route 2 are already false.

1. A product of consecutive integers need not have a prime of valuation \(1\):
   \[
   8\cdot9=2^3\,3^2.
   \]

2. Sylvester’s prime need not occur to valuation \(1\). For the length-two interval \([8,9]\), the only prime exceeding the length is \(3\), and it occurs to valuation \(2\).

3. In
   \[
   48\cdot49\cdot50=2^5\cdot3\cdot5^2\cdot7^2,
   \]
   every prime exceeding the interval length \(3\) occurs to an even exponent. The obstruction to squareness is instead the small-prime valuation \(v_3=1\), which is exactly canceled by the factor \(3!\) in the known two-block square example.

4. One cannot insist on primes among the selected integers: the interval
   \[
   [N!+2,N!+N]
   \]
   is an arbitrarily long interval containing only composite integers.

These checks rule out several naive forms of a bounded-component Sylvester principle.

## Self-Audit

1. **The endpoint bound uses the classical Sylvester theorem as an external input.** I have not reproved Sylvester’s theorem here. I believe the step is sound because the theorem is unconditional and its hypothesis is checked exactly: Lemma 1 gives \(a_h>\ell_h\), so all \(\ell_h\) terms are greater than \(\ell_h\).

2. **The smoothness/concentration lemma only controls primes larger than all block lengths.** It says nothing useful for \(q\le r\), where \(\lceil q/r\rceil=1\), and it does not itself force a forbidden prime for \(q>r\). I believe the stated lemma is nevertheless exact because it is only a pigeonhole argument over the at most one multiple of \(p\) in each block.

3. **The CRT constructions neutralize only finitely many prescribed primes and do not produce a perfect power.** Unprescribed prime factors of the constructed interval remain uncontrolled. I have not used the constructions as counterexamples to the original problem; only as rigorous obstructions to finite-prime and naive density arguments. Their asserted valuation properties follow directly from the displayed congruences.

## Computations To Verify

```python
from math import gcd, comb, isqrt
from itertools import combinations

def vp(n, p):
    e = 0
    while n % p == 0 and n:
        n //= p
        e += 1
    return e

def factor_trial(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def config_exponents(intervals):
    exps = {}
    selected = []
    for a, b in intervals:
        for n in range(a, b + 1):
            selected.append(n)
            for p, e in factor_trial(n).items():
                exps[p] = exps.get(p, 0) + e
    return exps, selected

def perfect_degree(intervals):
    exps, selected = config_exponents(intervals)
    if not exps:  # product 1
        return 0
    d = 0
    for e in exps.values():
        d = gcd(d, e)
    return d

def pairwise_disjoint(intervals):
    for (a, b), (c, d) in combinations(intervals, 2):
        if not (b < c or d < a):
            return False
    return True

def prime_divisors(n):
    return list(factor_trial(n))

# Verify Lemmas 1, 2 and the endpoint consequence in a bounded box.
def verify_bounded(Bmax=40, r=2):
    all_intervals = [
        (a, b) for a in range(1, Bmax + 1)
        for b in range(a, Bmax + 1)
    ]
    for intervals in combinations(all_intervals, r):
        if not pairwise_disjoint(intervals):
            continue
        d = perfect_degree(intervals)
        if d < 2:
            continue

        exps, selected = config_exponents(intervals)
        intervals = sorted(intervals)
        a, B = intervals[-1]
        ell = B - a + 1

        # Lemma 1
        assert a > ell, (intervals, d)

        lengths = [b - a + 1 for a, b in intervals]
        L = max(lengths)

        for q in prime_divisors(d):
            s = (q + r - 1) // r

            # Lemma 2
            for p in exps:
                if p > L:
                    assert any(n % (p ** s) == 0 for n in selected)

            # Lemma 4, applied to the rightmost block.
            C = sum((li + ell) // (ell + 1) for li in lengths)
            sh = (q + C - 1) // C
            assert B >= (ell + 1) ** sh, (intervals, q, C)

# Generalized CRT.
def crt(congruences):
    # congruences is a list of (residue, modulus), with coprime moduli
    x, M = 0, 1
    for a, m in congruences:
        t = ((a - x) * pow(M, -1, m)) % m
        x = (x + M * t) % (M * m)
        M *= m
    return x, M

def interval_vp(a, ell, p):
    return sum(vp(a + j, p) for j in range(ell))

# Construct Lemma 6.
def steered_start(ell, q, targets, lower_bound=0):
    # targets is {prime: residue mod q}
    congruences = []
    chosen_E = {}

    for p, target in targets.items():
        C = sum(vp(j, p) for j in range(1, ell))
        max_j = max((vp(j, p) for j in range(1, ell)), default=-1)
        E = max(1, max_j + 1)
        while (E + C - target) % q:
            E += 1
        chosen_E[p] = E
        congruences.append((p ** E, p ** (E + 1)))

    a, M = crt(congruences)
    if a <= lower_bound:
        a += ((lower_bound - a) // M + 1) * M

    for p, target in targets.items():
        assert interval_vp(a, ell, p) % q == target % q
    return a, chosen_E

# Example:
# a, E = steered_start(ell=20, q=5,
#                      targets={2: 0, 3: 1, 5: 4, 7: 2},
#                      lower_bound=10**6)

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n

# Construct Lemma 8.
def prime_power_covered_run(ell, s, lower_bound=0):
    primes = []
    p = ell
    for _ in range(ell):
        p = next_prime(p)
        primes.append(p)

    congruences = []
    for j, p in enumerate(primes):
        modulus = p ** (s + 1)
        residue = (p ** s - j) % modulus
        congruences.append((residue, modulus))

    a, M = crt(congruences)
    if a <= lower_bound:
        a += ((lower_bound - a) // M + 1) * M

    for j, p in enumerate(primes):
        assert vp(a + j, p) == s
        for k in range(ell):
            if k != j:
                assert (a + k) % p != 0
    return a, primes

# Search square binomial coefficients.
def square_binomial_search(L, N):
    ans = []
    for ell in range(2, L + 1):
        for n in range(2 * ell, N + 1):
            z = comb(n, ell)
            y = isqrt(z)
            if y * y == z:
                ans.append((n, ell, y))
    return ans

assert comb(9, 2) == 6**2
assert comb(50, 3) == 140**2
```

## Route Diagnosis

**Proved ledger.**

- The rightmost interval in any perfect-power configuration begins beyond its own length.
- For \(p>L\), a \(q\)-th-power configuration forces \(p^{\lceil q/r\rceil}\) into one selected integer.
- This yields a global smoothness restriction and explicit endpoint lower bounds.
- Any finite set of valuation congruences can be prescribed exactly by CRT.
- Arbitrarily long intervals can be covered term-by-term by distinct large prime powers.

**Plausible but unproved.**

- For fixed \(r\) and \(q>r\), sufficiently long unions might force a prime \(p>L\) which is not supported to order \(\lceil q/r\rceil\) anywhere else. This would settle the high-exponent range, but no known argument survives the CRT constructions and arbitrary endpoint growth.
- A substantially stronger all-primes theorem might exploit relations among the unprescribed cofactors rather than the density of prime powers. This presently appears comparable in difficulty to powerful-value problems for products of consecutive integers.

**Dead ends.**

- “There is always a prime of valuation \(1\)” is false already for \(8\cdot9\).
- A predetermined finite-prime sieve is defeated exactly by Lemma 6.
- A density count for large prime powers is defeated by Lemma 8.
- Prime-in-short-interval arguments cannot be uniform because arbitrarily long translated intervals may contain no primes.
- Sylvester alone only supplies \(p>\ell\), while arbitrary gaps allow the endpoint to be much larger than every power of \(\ell\).

The decisive block is \(q\le r\), especially \(r=q=2\): the concentration exponent becomes \(1\) and gives no information. The special configuration
\[
[1,\ell],\quad[n-\ell+1,n]
\]
shows that resolving this range affirmatively would in particular bound the lower index of square binomial coefficients. No Route 2 argument developed here approaches that uniform Diophantine obstruction. A fresh attempt should either find a genuinely global, all-primes extension of the Erdős–Selfridge allocation mechanism, or attack squarefree-kernel collisions directly; finite sieving and local large-prime density are insufficient.