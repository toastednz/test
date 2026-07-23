STATUS: BLOCKED

## Result

Route 4 gives an exact “burst-code” reformulation and several rigorous necessary conditions. Large primes provide sparse parity-check coordinates; in particular, a perfect-power configuration must place its final connected component entirely after the largest prime below its maximum endpoint, so any counterexample family must lie in increasingly long prime gaps and satisfy \(N/\min_i|I_i|\to\infty\). Conversely, any predetermined finite set of prime coordinates can be neutralized by arbitrarily long disjoint intervals, showing that a successful valuation-vector proof must use endpoint-dependent large primes. Most decisively, the \(r=2,q=2\) burst-zero-sum statement contains the unresolved problem of square binomial coefficients with unbounded lower index. I did not resolve that obstruction, so this route is blocked rather than solved.

## Complete Argument

### 1. The valuation-vector problem is a bounded-burst code problem

Fix a prime \(q\), and let
\[
\mathcal V_q=\bigoplus_p\mathbb F_q.
\]
For \(n\ge 0\), define the prefix vector
\[
C_q(n)=\bigl(v_p(n!)\bmod q\bigr)_p,
\qquad C_q(0)=0.
\]
For an interval \(I=[a,b]\),
\[
V_q(I)=\biggl(v_p\left(\prod_{m=a}^b m\right)\bmod q\biggr)_p.
\]

Since
\[
\prod_{m=a}^b m=\frac{b!}{(a-1)!},
\]
we have the exact identity
\[
V_q([a,b])=C_q(b)-C_q(a-1).
\]
Therefore, for disjoint intervals \(I_i=[a_i,b_i]\),
\[
\sum_{i=1}^rV_q(I_i)
 =\sum_{i=1}^r\bigl(C_q(b_i)-C_q(a_i-1)\bigr).
\]

By unique factorization,
\[
\prod_{i=1}^r\prod_{m\in I_i}m
\]
is a \(q\)-th power if and only if this vector is zero.

Equivalently, if
\[
x_n=\bigl(v_p(n)\bmod q\bigr)_p,
\]
then the selected set \(U=\bigcup_i I_i\) gives a codeword
\[
\sum_{n\in U}x_n=0
\]
whose support is a union of at most \(r\) intervals, or “bursts.” The Erdős–Selfridge theorem says that a nontrivial codeword cannot consist of one burst of length at least \(2\). Problem #930 asks whether, for each fixed \(r\), a codeword made from at most \(r\) bursts must have at least one short burst.

If two intervals are adjacent, their prefix terms cancel:
\[
C_q(b)-C_q(a-1)+C_q(c)-C_q(b)=C_q(c)-C_q(a-1).
\]
Thus adjacent intervals may be merged, and it is natural to work with the connected components of \(U\).

---

### 2. Finite-coordinate blindness

The first serious obstruction is that no fixed finite collection of prime coordinates can prove the theorem.

#### Lemma 2.1

Let \(S\) be a finite set of primes, \(L\ge1\), and \(q\) a prime. There exist \(q\) pairwise disjoint intervals \(I_0,\dots,I_{q-1}\), all of length \(L\), such that
\[
\sum_{t=0}^{q-1}V_q(I_t)
\]
vanishes on every coordinate \(p\in S\).

For \(q=2\), the two intervals have identical valuation vectors on \(S\).

#### Proof

For each \(p\in S\), choose \(J_p\) such that
\[
p^{J_p}>L.
\]
Let
\[
M=\prod_{p\in S}p^{J_p};
\]
if \(S=\varnothing\), take \(M=L+1\). In either case we may arrange \(M>L\). Define
\[
I_t=[tM+1,tM+L],\qquad 0\le t<q.
\]
These intervals are pairwise disjoint because \(M>L\).

Fix \(p\in S\) and \(1\le m\le L\). Write
\[
m=p^e u,\qquad p\nmid u.
\]
Since \(m<p^{J_p}\), we have \(e<J_p\). Since \(p^{J_p}\mid M\),
\[
tM+m
 =p^e\left(t\frac{M}{p^e}+u\right),
\]
and the expression in parentheses is congruent to \(u\not\equiv0\pmod p\). Hence
\[
v_p(tM+m)=e=v_p(m).
\]
Summing over \(m=1,\dots,L\),
\[
v_p\left(\prod_{n\in I_t}n\right)=v_p(L!)
\]
for every \(t\). Consequently,
\[
\sum_{t=0}^{q-1}v_p\left(\prod_{n\in I_t}n\right)
 =q\,v_p(L!)\equiv0\pmod q.
\]
This holds for every \(p\in S\). ∎

For \(q=2\), the intervals are
\[
[1,L],\qquad [M+1,M+L].
\]
Their product is
\[
(L!)^2\binom{M+L}{L},
\]
and the proof gives the stronger fact
\[
v_p\binom{M+L}{L}=0\qquad(p\in S).
\]

Thus, for any prescribed bound \(B(L)\), one can choose arbitrarily long intervals for which every prime \(p\le B(L)\) fails to detect nonsquareness. Any successful proof must use primes depending essentially on the actual endpoints, not merely on \(r\) and the lengths.

This lemma does not produce a perfect power: uncontrolled primes outside \(S\) may obstruct it. It proves only that finite-dimensional coding or small-prime arguments are intrinsically insufficient.

---

### 3. Sparse coordinates supplied by large primes

Let
\[
U=\bigcup_{i=1}^r I_i,\qquad
P=\prod_{n\in U}n,\qquad
N=\max U,\qquad
L=\max_i|I_i|.
\]

#### Lemma 3.1: sparse-prime checks

Let \(p\) be prime.

1. If \(p^2>N\), then
   \[
   v_p(P)=\#\{n\in U:p\mid n\}.
   \]

2. If additionally \(p>L\), then each interval contains at most one multiple of \(p\), and therefore
   \[
   v_p(P)=\#\{i:I_i\text{ contains a multiple of }p\}\le r.
   \]

3. Without assuming \(p^2>N\), if \(p>L\) and \(p\mid P\), then
   \[
   1\le v_p(P)\le r\lfloor\log_pN\rfloor.
   \]

#### Proof

If \(p^2>N\), no positive integer at most \(N\) is divisible by \(p^2\). Hence every selected multiple of \(p\) contributes exactly one to \(v_p(P)\), proving the first assertion.

If \(p>L\), an interval of length at most \(L\) cannot contain two different multiples of \(p\), proving the second.

For the third assertion, each interval contains at most one multiple \(m_i\) of \(p\). If it exists,
\[
v_p(m_i)\le\lfloor\log_pN\rfloor.
\]
Summing over at most \(r\) intervals gives the claimed bound. ∎

#### Corollary 3.2

If \(P\) is a \(q\)-th power and
\[
p>\max(\sqrt N,L),
\]
then the number of intervals containing a multiple of \(p\) is divisible by \(q\).

In particular:

- if \(q>r\), no selected integer is divisible by such a prime;
- if \(r<2q\), every such prime that occurs must occur in exactly \(q\) intervals;
- for \(q=2\), every such prime must occur in an even number of intervals.

This is the clearest coding-theoretic structure obtained from Route 4: primes above both \(\sqrt N\) and the maximum interval length give \(0\)-\(1\) parity-check rows of weight at most \(r\).

#### Corollary 3.3: exponent-smoothness hierarchy

Fix an integer \(t\ge2\). If \(P\) is a \(q\)-th power and
\[
q>r(t-1),
\]
then every prime divisor of \(P\) is at most
\[
\max(L,N^{1/t}).
\]

#### Proof

Suppose \(p\mid P\) and
\[
p>\max(L,N^{1/t}).
\]
By Lemma 3.1,
\[
0<v_p(P)\le r\lfloor\log_pN\rfloor.
\]
Since \(p^t>N\),
\[
\lfloor\log_pN\rfloor\le t-1.
\]
Thus
\[
0<v_p(P)\le r(t-1)<q,
\]
which is impossible because \(q\mid v_p(P)\). ∎

For \(t=2\), a \(q\)-th power with \(q>r\) forces every selected integer to be \(\max(L,\sqrt N)\)-smooth. This is a useful dichotomy, but no unconditional theorem rules out arbitrarily long intervals of this kind at arbitrary heights.

There is also a global form not involving \(L\): if
\[
p>\max(\sqrt N,N/q),
\]
then \(p^2>N\) and there are fewer than \(q\) multiples of \(p\) in \([1,N]\). Hence a \(q\)-th power configuration contains no multiple of \(p\).

---

### 4. The high-prime cell structure

For real \(x>\sqrt N\), define
\[
c_U(x)=\#\{k\ge1:kx\in U\}.
\]
This is well-defined with only finitely many contributing \(k\), since \(kx\le N\) implies \(k<\sqrt N\).

As a function of \(x\), \(c_U(x)\) is constant on each open component obtained after deleting the finitely many boundary points
\[
\frac{a_i}{k},\qquad \frac{b_i}{k}
\]
that lie above \(\sqrt N\).

If \(p>\sqrt N\) is prime, then Lemma 3.1 gives
\[
v_p(P)=c_U(p).
\]
Consequently, if \(P\) is a \(q\)-th power, every cell on which
\[
c_U(x)\not\equiv0\pmod q
\]
must be prime-free.

This identifies a possible Route 4 strategy: prove that one of the “bad” cells necessarily contains a prime. The problem is that the cells can be extremely short and depend arbitrarily on the endpoints. Present prime-distribution theorems do not give primes in every such endpoint-dependent cell.

---

### 5. A sharp restriction on the final component

Let \([A,N]\) be the final connected component of \(U\), after merging adjacent intervals. Let \(p^-(N)\) denote the largest prime at most \(N\).

#### Proposition 5.1

If \(P\) is a perfect power, then
\[
A>p^-(N)
\]
and hence
\[
N-A+1\le N-p^-(N).
\]

#### Proof

By Bertrand’s postulate,
\[
p^-(N)>\frac N2
\]
for every \(N\ge2\). If \(p^-(N)\in U\), it is the only positive multiple of \(p^-(N)\) not exceeding \(N\). Therefore
\[
v_{p^-(N)}(P)=1,
\]
which is incompatible with \(P\) being a perfect power.

If \(A\le p^-(N)\), then \(p^-(N)\in[A,N]\subseteq U\), a contradiction. Therefore \(A>p^-(N)\), and
\[
N-A+1\le N-p^-(N).
\]
∎

The prime number theorem implies
\[
N-p^-(N)=o(N).
\]
Indeed, for every fixed \(\varepsilon>0\),
\[
\pi(N)-\pi((1-\varepsilon)N)
 \sim \frac{\varepsilon N}{\log N}>0,
\]
so \(p^-(N)>(1-\varepsilon)N\) for sufficiently large \(N\).

Thus any hypothetical counterexample sequence with all interval lengths tending to infinity must satisfy
\[
\frac{\text{length of the final component}}{N}\longrightarrow0.
\]
Since the final component contains the top interval,
\[
\frac{\min_i|I_i|}{N}\longrightarrow0,
\qquad\text{equivalently}\qquad
\frac{N}{\min_i|I_i|}\longrightarrow\infty.
\]

This gives the following genuine restricted affirmative result.

#### Corollary 5.2

For every fixed \(C\ge1\), there exists \(K(C)\) such that no perfect-power configuration satisfies both
\[
\min_i|I_i|\ge K(C)
\quad\text{and}\quad
N\le C\min_i|I_i|.
\]

#### Proof

By the prime number theorem, for sufficiently large \(N\),
\[
N-p^-(N)<\frac NC.
\]
On the other hand, the final component has length at least \(\min_i|I_i|\), which under the displayed endpoint condition is at least \(N/C\). This contradicts Proposition 5.1. ∎

This does not approach the required endpoint-uniform threshold because prime gaps are unbounded.

---

### 6. Factorial gaps defeat a purely macroscopic large-prime argument

The obstruction above is genuine rather than merely technical.

#### Proposition 6.1

Let \(M\ge3\), \(2\le K\le M\), and
\[
N=M!+M.
\]
Then the interval
\[
J=[M!+K,M!+M]
\]
has length \(M-K+1\), and every prime divisor of every integer in \(J\) is at most \(N/K\).

#### Proof

For \(K\le j\le M\), since \(j\mid M!\),
\[
M!+j=j\left(\frac{M!}{j}+1\right).
\]
The first factor satisfies
\[
j\le M\le\frac NK,
\]
because \(N=M!+M\ge M^2\ge MK\).

The second factor satisfies
\[
\frac{M!}{j}+1
 \le\frac{M!}{K}+1
 \le\frac{M!}{K}+\frac MK
 =\frac NK.
\]
Every prime divisor of \(M!+j\) divides one of these two factors, so it is at most \(N/K\). ∎

Taking \(K=\lceil M/2\rceil\) gives a terminal interval of length tending to infinity whose elements have no prime factor larger than approximately \(2N/M=o(N)\).

This is not a perfect-power construction. It proves that one cannot hope to find a prime factor comparable to the endpoint in every long interval. A successful sparse-coordinate argument must work far below the macroscopic scale and must account for matching contributions from lower intervals.

---

### 7. Exact square-binomial obstruction

For
\[
I_1=[1,\ell],
\qquad
I_2=[n-\ell+1,n],
\qquad n\ge2\ell,
\]
we have
\[
\prod_{m\in I_1}m\prod_{m\in I_2}m
 =\ell!\frac{n!}{(n-\ell)!}
 =(\ell!)^2\binom n\ell.
\]
Therefore,
\[
V_2(I_1)+V_2(I_2)
 =V_2\left(\binom n\ell\right).
\]
Consequently,
\[
V_2(I_1)+V_2(I_2)=0
\quad\Longleftrightarrow\quad
\binom n\ell\text{ is a square}.
\]

Thus even the following special Route 4 claim is presently out of reach:

> There exists \(K\) such that no two disjoint intervals of equal length at least \(K\), one beginning at \(1\), have equal squarefree-kernel vectors.

It would imply
\[
\ell\ge K,\quad n\ge2\ell
\Longrightarrow \binom n\ell\text{ is not a square}.
\]
Conversely, square binomial coefficients with unbounded \(\ell\) would give an unbounded two-burst zero-sum and disprove Problem #930.

This is the precise comparable-strength obstruction blocking Route 4.

---

### 8. Counterexamples to stronger valuation-vector claims

A common strengthening would be to seek a prime of valuation exactly \(1\) whenever the product is not a perfect power. This is already false for unions of short intervals.

Take
\[
[1,2],\qquad[8,10],\qquad[24,25].
\]
Their products are
\[
2,\qquad 2^4 3^2 5,\qquad 2^3 3 5^2,
\]
so the total product is
\[
2^8 3^3 5^3.
\]
The gcd of the exponents is \(1\), so it is not a perfect power, but no prime has valuation \(1\).

This does not refute an eventual theorem for sufficiently long intervals, but it shows that “valuation one” is strictly stronger than the required conclusion and is not a formal consequence of disconnectedness.

The square example
\[
[1,3],\qquad[48,50]
\]
also exposes a flaw in the assertion that a prime larger than the interval length gives a \(0\)-\(1\) coordinate:
\[
\prod_{m=48}^{50}m=2^5\cdot3\cdot5^2\cdot7^2.
\]
Here \(7>3\), but the selected multiple is \(49=7^2\), so its valuation is \(2\). Indeed,
\[
(1\cdot2\cdot3)(48\cdot49\cdot50)
 =2^6 3^2 5^2 7^2=840^2.
\]
The hypothesis \(p^2>N\) in Lemma 3.1 is therefore essential.

---

### 9. Ledger

**Proved lemmas and reductions**

1. Exact prefix-vector and bounded-burst code reformulation.
2. Finite-coordinate blindness for arbitrarily long disjoint intervals.
3. Sparse high-prime incidence checks.
4. The exponent-smoothness hierarchy.
5. Piecewise-constant high-prime cell formulation.
6. The terminal prime-gap bound
   \[
   \text{final component length}\le N-p^-(N).
   \]
7. The restricted theorem when \(N/\min |I_i|\) is bounded.
8. Arbitrarily long factorial-gap intervals with no prime factor comparable to the endpoint.
9. Exact reduction of the two-burst square problem to square binomial coefficients.

**Plausible but unproved claims**

1. A bound on the prime exponent \(q\) depending only on \(r\).
2. A theorem forcing a high-prime cell with nonzero count modulo \(q\) to contain a prime.
3. Uniform boundedness of square binomial coefficients in the lower half of Pascal’s triangle.
4. An endpoint-uniform theorem excluding long terminal intervals whose large-prime coordinates can all be matched by at most \(r-1\) lower intervals.

None of these is used as if proved.

**Dead ends**

1. Predetermined finite sets of small primes: defeated by Lemma 2.1.
2. A universal valuation-one certificate: defeated by \(2^8 3^3 5^3\).
3. Treating \(p>|I_i|\) as a \(0\)-\(1\) coordinate: defeated by selected prime powers such as \(49\).
4. Macroscopic prime-factor arguments: defeated by factorial-gap intervals.
5. Generic finite-dimensional zero-sum or coding bounds: the ambient dimension grows with the endpoints, and exact structured collisions include the square-binomial family.

## Self-Audit

1. **The prime-gap corollary invokes the prime number theorem rather than proving it from scratch.** It is a standard unconditional theorem, and only its elementary consequence \(p^-(N)=N-o(N)\) is used. The sharper exact inequality in Proposition 5.1 needs only Bertrand’s postulate.

2. **The finite-coordinate construction gives only projected zero-sums, not actual perfect powers.** I have explicitly not claimed otherwise. Its relevance is diagnostic: it rigorously excludes proofs based on any endpoint-independent finite collection of primes.

3. **The conclusion that Route 4 is blocked relies on the unresolved square-binomial subproblem rather than a proof that no other valuation-vector idea can work.** The algebraic reduction itself is exact. A new argument could bypass square-binomial theory by proving the needed uniform statement directly, but the present analysis does not supply one.

## Computations To Verify

```python
from math import gcd, isqrt, comb, factorial
from functools import reduce

def factor_integer(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def valuation_vector(intervals):
    """intervals is a list of inclusive pairs (a,b)."""
    out = {}
    for a, b in intervals:
        for n in range(a, b + 1):
            for p, e in factor_integer(n).items():
                out[p] = out.get(p, 0) + e
    return {p: e for p, e in out.items() if e}

def power_gcd(intervals):
    vals = valuation_vector(intervals)
    return reduce(gcd, vals.values()) if vals else 0

def is_qth_power(intervals, q):
    return all(e % q == 0 for e in valuation_vector(intervals).values())

# The nonpower with no valuation-one coordinate.
vals = valuation_vector([(1, 2), (8, 10), (24, 25)])
assert vals == {2: 8, 3: 3, 5: 3}
assert reduce(gcd, vals.values()) == 1
assert all(e != 1 for e in vals.values())

# Known square examples.
assert power_gcd([(1, 2), (8, 9)]) >= 2
assert power_gcd([(1, 3), (48, 50)]) >= 2
```

Finite-coordinate blindness:

```python
def vp(n, p):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e

def finite_blindness_check(S, L, q):
    M = 1
    for p in S:
        z = p
        while z <= L:
            z *= p
        M *= z
    if not S:
        M = L + 1

    assert M > L

    for p in S:
        block_vals = []
        for t in range(q):
            block_vals.append(sum(vp(t*M + m, p)
                                  for m in range(1, L + 1)))
        assert len(set(block_vals)) == 1
        assert sum(block_vals) % q == 0

    # For q=2, the associated binomial coefficient avoids every p in S.
    if q == 2:
        n = M + L
        for p in S:
            assert vp(comb(n, L), p) == 0

finite_blindness_check([2, 3, 5, 7, 11], L=100, q=2)
finite_blindness_check([2, 3, 5], L=40, q=3)
```

Sparse high-prime conditions:

```python
def sieve(N):
    isprime = [True] * (N + 1)
    if N >= 0:
        isprime[0] = False
    if N >= 1:
        isprime[1] = False
    for p in range(2, isqrt(N) + 1):
        if isprime[p]:
            for m in range(p*p, N + 1, p):
                isprime[m] = False
    return [p for p in range(2, N + 1) if isprime[p]]

def selected_multiple_count(intervals, p):
    return sum(b // p - (a - 1) // p for a, b in intervals)

def verify_sparse_rows(intervals, q):
    N = max(b for a, b in intervals)
    if not is_qth_power(intervals, q):
        return
    for p in sieve(N):
        if p * p > N:
            assert selected_multiple_count(intervals, p) % q == 0

verify_sparse_rows([(1, 2), (8, 9)], 2)
verify_sparse_rows([(1, 3), (48, 50)], 2)
```

Square-binomial search:

```python
def square_binomial_search(Lmax, Nmax):
    hits = []
    for ell in range(2, Lmax + 1):
        for n in range(2 * ell, Nmax + 1):
            z = comb(n, ell)
            y = isqrt(z)
            if y * y == z:
                hits.append((n, ell, y))
    return hits

hits = square_binomial_search(20, 10000)
assert (9, 2, 6) in hits
assert (50, 3, 140) in hits
print(hits)
```

Squarefree-kernel collision search for fixed lengths:

```python
def spf_table(N):
    spf = list(range(N + 1))
    for p in range(2, isqrt(N) + 1):
        if spf[p] == p:
            for m in range(p*p, N + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf

def squareclass_prefix(N):
    spf = spf_table(N)
    primes = [p for p in range(2, N + 1) if spf[p] == p]
    bit = {p: i for i, p in enumerate(primes)}

    squareclass = [0] * (N + 1)
    for n in range(2, N + 1):
        x = n
        mask = 0
        while x > 1:
            p = spf[x]
            parity = 0
            while x % p == 0:
                x //= p
                parity ^= 1
            if parity:
                mask ^= 1 << bit[p]
        squareclass[n] = mask

    prefix = [0] * (N + 1)
    for n in range(1, N + 1):
        prefix[n] = prefix[n - 1] ^ squareclass[n]
    return prefix

def interval_squareclass(prefix, a, b):
    return prefix[b] ^ prefix[a - 1]

def collision_search(N, L):
    prefix = squareclass_prefix(N)
    earliest = {}
    hits = []
    for a in range(1, N - L + 2):
        b = a + L - 1
        mask = interval_squareclass(prefix, a, b)
        if mask in earliest:
            c, d = earliest[mask]
            if d < a:
                hits.append(((c, d), (a, b)))
        else:
            earliest[mask] = (a, b)
    return hits

assert ((1, 2), (8, 9)) in collision_search(100, 2)
assert ((1, 3), (48, 50)) in collision_search(100, 3)
```

Factorial-gap smoothness:

```python
def largest_prime_factor(n):
    return max(factor_integer(n))

def verify_factorial_block(M, K):
    N = factorial(M) + M
    for j in range(K, M + 1):
        n = factorial(M) + j
        assert largest_prime_factor(n) <= N // K

for M in range(3, 13):
    verify_factorial_block(M, (M + 1) // 2)
```

## Route Diagnosis

The valuation-vector formulation is exact and useful, but generic additive-combinatorial heuristics do not supply the required endpoint-uniform control. Large primes do yield sparse coordinates, and they force a hypothetical counterexample into long prime gaps with very thin intervals relative to the endpoints. That is substantial structural information, but prime gaps are unbounded, finite collections of small primes can be neutralized by congruent translations, and prime powers destroy naive \(0\)-\(1\) incidence arguments.

The precise block is already present for \(r=2,q=2\): proving that two sufficiently long disjoint interval vectors cannot coincide would settle uniform boundedness of square binomial coefficients in the lower half of Pascal’s triangle. No argument developed here resolves that comparable-strength problem.

A fresh attempt should concentrate on one of three points:

1. Prove an exponent bound \(q\le f(r)\), turning the problem into finitely many modular zero-sum questions.
2. Analyze the high-prime incidence hypergraph together with prime-power coordinates, seeking a row whose weight is not divisible by \(q\).
3. Switch toward Route 6 and search for an exact unbounded square-binomial or squarefree-kernel collision family; such a family would immediately disprove the problem for \(r=2\).