STATUS: BLOCKED

## Result

Route 3 cannot succeed through any fixed-modulus forbidden residue for the unresolved coprime pairs \((5,2),(9,2),(5,3)\). In fact, I prove the opposite: every arithmetic progression containing integers coprime to \(pq\) contains infinitely many \((p,q)\)-representable integers. The proof gives explicit antichains modulo an arbitrary modulus, using a top boundary term, a bottom boundary encoding, and an arbitrarily long central antidiagonal whose terms are all \(1\) modulo the part of the modulus coprime to \(pq\). I also prove an exact boundary-peeling recurrence and a scaling equivalence. These clarify what a genuine higher-layer descent would have to control, but I do not obtain the required infinitude or density results.

## Complete Argument

### 1. Primitive-power orbits needed below

We use the following standard lifting fact.

**Lemma 1.** Let \(\ell\) be an odd prime. Suppose \(g\) has order \(\ell-1\) modulo \(\ell\), and
\[
v_\ell(g^{\ell-1}-1)=1.
\]
Then \(g\) is a primitive root modulo \(\ell^a\) for every \(a\ge1\).

**Proof.** Write
\[
g^{\ell-1}=1+c\ell,\qquad \ell\nmid c.
\]
For every \(j\ge0\), the binomial theorem gives
\[
(1+c\ell)^{\ell^j}\equiv 1+c\ell^{j+1}\pmod{\ell^{j+2}},
\]
so
\[
v_\ell\!\left(g^{(\ell-1)\ell^j}-1\right)=j+1.
\]
Hence \(g^{(\ell-1)\ell^{a-2}}\not\equiv1\pmod{\ell^a}\), while Euler’s theorem gives
\[
g^{(\ell-1)\ell^{a-1}}\equiv1\pmod{\ell^a}.
\]
The order modulo \(\ell^a\) is therefore exactly
\[
(\ell-1)\ell^{a-1}=\varphi(\ell^a).
\]
\(\square\)

The required instances are:

\[
\begin{array}{c|c|c}
g&\ell&g^{\ell-1}-1\\ \hline
2&5&2^4-1=15\\
2&3&2^2-1=3\\
3&5&3^4-1=80\\
5&3&5^2-1=24.
\end{array}
\]

Thus:

- \(2\) generates \((\mathbb Z/5^a\mathbb Z)^\times\);
- \(2\) generates \((\mathbb Z/3^a\mathbb Z)^\times\);
- \(3\) generates \((\mathbb Z/5^a\mathbb Z)^\times\);
- \(5\) generates \((\mathbb Z/3^a\mathbb Z)^\times\).

These hold for all \(a\ge1\).

---

### 2. Modular saturation theorem

Call a residue class \(r\bmod M\) **\((p,q)\)-admissible** if it contains at least one integer coprime to \(pq\).

**Theorem 2.** Let
\[
(p,q)\in\{(5,2),(9,2),(5,3)\}.
\]
For every \(M\ge1\), every \((p,q)\)-admissible residue class \(r\bmod M\) contains infinitely many integers in \(\mathcal R_{p,q}\) which are coprime to \(pq\).

Consequently, for these three pairs there is no fixed modulus \(M\) and admissible residue \(r\bmod M\) such that every integer in that progression is non-representable.

#### Reduction of the modulus

Let \(P,Q\) be the underlying primes:
\[
(P,Q)=
\begin{cases}
(5,2),&(p,q)=(5,2),\\
(3,2),&(p,q)=(9,2),\\
(5,3),&(p,q)=(5,3).
\end{cases}
\]

Replace \(M\) by
\[
D=\operatorname{lcm}(M,PQ).
\]
Since \(r\bmod M\) is admissible, there is a lift \(R\bmod D\) such that
\[
R\equiv r\pmod M,\qquad \gcd(R,PQ)=1.
\]

Write
\[
D=A B m,
\]
where

- \(A=P^a\) with \(a\ge1\);
- \(B=Q^b\) with \(b\ge1\);
- \(\gcd(m,pq)=1\).

It suffices to construct infinitely many antichain sums congruent to \(R\pmod D\).

For a unit \(u\bmod c\), write \(\operatorname{ord}_c(u)\) for its multiplicative order, with the convention \(\operatorname{ord}_1(u)=1\).

---

### 3. The cases \((5,2)\) and \((9,2)\)

Here \(q=2\), while \(p=P^e\), with
\[
(P,e)=(5,1)\quad\text{or}\quad(3,2).
\]

Set
\[
x_A=R\bmod A,\qquad x_B=R\bmod B,\qquad x_m=R\bmod m.
\]
Both \(x_A\) and \(x_B\) are units.

#### Top boundary term

By Lemma 1, \(2\) generates the units modulo \(A\). Choose \(\lambda_0\ge0\) such that
\[
2^{\lambda_0}\equiv x_A\pmod A.
\]
All exponents
\[
L\equiv\lambda_0
\pmod{\operatorname{lcm}(\operatorname{ord}_A(2),\operatorname{ord}_m(2))}
\]
give the same residue both modulo \(A\) and modulo \(m\). Such \(L\) may be chosen arbitrarily large.

The point \((0,L)\) contributes \(2^L\).

#### Bottom boundary encoding modulo \(2^b\)

Write the ordinary binary expansion
\[
x_B=\sum_{j\in J}2^j,\qquad J\subseteq\{0,\dots,b-1\}.
\]
Because \(x_B\) is odd, \(0\in J\).

Let
\[
h=\operatorname{lcm}\bigl(\operatorname{ord}_{2^b}(p),
                           \operatorname{ord}_m(p)\bigr).
\]
For every positive multiple \(K\) of \(h\),
\[
p^K\equiv1\pmod{2^b},
\qquad
p^K\equiv1\pmod m.
\]

List
\[
J=\{j_1>j_2>\cdots>j_s=0\}.
\]
Choose positive multiples
\[
K_1<K_2<\cdots<K_s
\]
of \(h\), all as large as desired. The terms
\[
p^{K_i}2^{j_i}
\]
then contribute
\[
\sum_{i=1}^s2^{j_i}=x_B\pmod{2^b}.
\]
Modulo \(m\), their total is the fixed residue
\[
c_{\mathrm{low}}:=\sum_{j\in J}2^j\pmod m.
\]

If the \(K_i\) are sufficiently large, all these terms vanish modulo \(A\).

#### Central antidiagonal

Let
\[
u=\operatorname{ord}_m(p),\qquad v=\operatorname{ord}_m(2).
\]
Choose integers \(C,D_0\) sufficiently large that
\[
p^{u(C+1)}\equiv0\pmod A,
\qquad
2^{v(D_0+1)}\equiv0\pmod{2^b}.
\]

For an integer \(t\ge0\), define the central points
\[
(k_i,\ell_i)
=
\bigl(u(C+i),\,v(D_0+t+1-i)\bigr),
\qquad 1\le i\le t.
\]
Their first coordinates strictly increase and their second coordinates strictly decrease. Each central term satisfies
\[
p^{k_i}2^{\ell_i}\equiv0\pmod A,\qquad
p^{k_i}2^{\ell_i}\equiv0\pmod{2^b},
\]
and
\[
p^{k_i}2^{\ell_i}\equiv1\pmod m.
\]
Thus the central block contributes exactly \(t\pmod m\).

The top term has the fixed residue
\[
c_{\mathrm{top}}:=2^{\lambda_0}\pmod m.
\]
Choose
\[
t\equiv x_m-c_{\mathrm{top}}-c_{\mathrm{low}}\pmod m.
\]
There are arbitrarily large such \(t\), namely \(t=t_0+jm\).

For each such \(t\):

1. choose \(L\) in the specified exponent class, with
   \[
   L>\max_i\ell_i,\qquad L\ge b;
   \]
2. choose the \(K_i\) so large that
   \[
   K_1>\max_i k_i
   \]
   and all low terms vanish modulo \(A\).

The complete sequence of exponent pairs is
\[
(0,L),\ 
(k_1,\ell_1),\dots,(k_t,\ell_t),\
(K_1,j_1),\dots,(K_s,j_s).
\]
Its first coordinates strictly increase and its second coordinates strictly decrease because
\[
L>\ell_1>\cdots>\ell_t\ge b>j_1>\cdots>j_s=0.
\]
It is therefore an antichain.

Modulo \(A\), only the top term survives, giving \(x_A\). Modulo \(2^b\), only the low block survives, giving \(x_B\). Modulo \(m\), the total is
\[
c_{\mathrm{top}}+t+c_{\mathrm{low}}\equiv x_m.
\]
Hence the sum is congruent to \(R\pmod D\).

As \(t\to\infty\), the largest central \(\ell\)-coordinate tends to infinity, forcing \(L\to\infty\). Therefore the resulting sums are unbounded and hence give infinitely many distinct represented integers in the prescribed class.

---

### 4. The case \((5,3)\)

Now
\[
A=5^a,\qquad B=3^b.
\]
By Lemma 1, \(3\) generates the units modulo \(A\), while \(5\) generates the units modulo \(B\).

Choose \(\lambda_0,\kappa_0\ge0\) satisfying
\[
3^{\lambda_0}\equiv R\pmod A,
\qquad
5^{\kappa_0}\equiv R\pmod B.
\]
The actual exponents \(L,K\) may be increased arbitrarily while preserving their residues modulo both the relevant prime-power modulus and \(m\), by taking
\[
L\equiv\lambda_0
\pmod{\operatorname{lcm}(\operatorname{ord}_A(3),
                           \operatorname{ord}_m(3))}
\]
and
\[
K\equiv\kappa_0
\pmod{\operatorname{lcm}(\operatorname{ord}_B(5),
                           \operatorname{ord}_m(5))}.
\]

The two boundary terms are
\[
3^L\quad\text{at }(0,L),
\qquad
5^K\quad\text{at }(K,0).
\]

Let
\[
u=\operatorname{ord}_m(5),\qquad v=\operatorname{ord}_m(3).
\]
For an arbitrary \(t\ge0\), choose central points
\[
(k_i,\ell_i)
=
\bigl(u(C+i),\,v(D_0+t+1-i)\bigr),
\qquad 1\le i\le t,
\]
where \(C,D_0\) are large enough that every central term vanishes modulo both \(5^a\) and \(3^b\).

Each central term is \(1\pmod m\). Thus choose
\[
t\equiv
R-3^{\lambda_0}-5^{\kappa_0}
\pmod m.
\]
Again there are arbitrarily large such \(t\).

After fixing \(t\), choose \(L\) and \(K\) in their allowed exponent classes so large that
\[
L>\max_i\ell_i,\qquad K>\max_i k_i,
\]
and also \(L\ge b,\ K\ge a\).

Then
\[
(0,L),\ (k_1,\ell_1),\dots,(k_t,\ell_t),\ (K,0)
\]
is an antichain. Modulo \(5^a\), only \(3^L\) survives; modulo \(3^b\), only \(5^K\) survives; and modulo \(m\), the central block adjusts the total to the desired residue.

These sums are unbounded as \(t\to\infty\), proving Theorem 2 in the final case. \(\square\)

---

### 5. Consequence for Route 3

**Corollary 3.** For each of
\[
(5,2),(9,2),(5,3),
\]
no fixed-modulus condition on the final sum can produce a nonempty arithmetic progression of integers coprime to \(pq\) that contains only non-representable integers.

This is stronger than merely saying that low powers \(p^a q^b\) have no missing reduced residues: arbitrary extra prime factors in the modulus do not help.

It does not exclude a size-sensitive obstruction in which the modulus grows with the integer under consideration.

---

### 6. Exact boundary peeling

The following gives the precise form of a possible boundary-layer descent.

For \(K,L\ge1\), let \(\mathcal R^{K,L}_{p,q}\) consist of \(0\), together with sums represented by antichains contained in
\[
\{0,\dots,K-2\}\times\{0,\dots,L-2\}.
\]
If \(K=1\) or \(L=1\), this box is empty and the only allowed value is \(0\).

**Lemma 4 (boundary peeling).** Let \(n>1\) and \(\gcd(n,pq)=1\). Then \(n\in\mathcal R_{p,q}\) if and only if there exist \(K,L\ge1\) such that
\[
m:=\frac{n-q^L-p^K}{pq}
\]
is a nonnegative integer belonging to \(\mathcal R^{K,L}_{p,q}\).

**Proof.** Suppose \(n\) has an antichain representation. Since \(n\not\equiv0\pmod p\), exactly one selected point has first coordinate \(0\), say \((0,L)\). Similarly, exactly one selected point has second coordinate \(0\), say \((K,0)\).

These points are distinct because otherwise the representation contains \((0,0)\), and the antichain would have to be the singleton \(\{(0,0)\}\), giving \(n=1\). Thus \(K,L\ge1\).

Every other point \((k,\ell)\) has \(k,\ell\ge1\). Incomparability with \((0,L)\) forces \(\ell<L\), while incomparability with \((K,0)\) forces \(k<K\). Therefore
\[
1\le k\le K-1,\qquad 1\le\ell\le L-1.
\]
After deleting the two boundary points and replacing every remaining \((k,\ell)\) by \((k-1,\ell-1)\), one obtains an antichain in
\[
\{0,\dots,K-2\}\times\{0,\dots,L-2\},
\]
whose sum is \(m\).

Conversely, take an antichain representing such an \(m\), shift all its points by \((1,1)\), and adjoin \((0,L)\) and \((K,0)\). The box restrictions ensure incomparability with both new endpoints. The resulting sum is
\[
q^L+p^K+pq\,m=n.
\]
\(\square\)

This recurrence is exact, but the possible endpoint exponents \(K,L\) are not uniquely determined. Controlling all alternatives is the unresolved difficulty.

---

### 7. Scaling equivalence

**Lemma 5.** For every coprime \(p,q\) and every positive integer \(n\),

\[
p\mid n\quad\Longrightarrow\quad
\bigl(n\in\mathcal R_{p,q}\iff n/p\in\mathcal R_{p,q}\bigr),
\]
and similarly
\[
q\mid n\quad\Longrightarrow\quad
\bigl(n\in\mathcal R_{p,q}\iff n/q\in\mathcal R_{p,q}\bigr).
\]

**Proof.** Scaling an antichain by \(p\) shifts every first coordinate by \(1\), proving the reverse implication.

For the forward implication, suppose \(p\mid n\) and \(n\) has an antichain representation. There is at most one term in row \(k=0\). If such a term existed, it would be \(q^\ell\), and reduction modulo \(p\) would give
\[
n\equiv q^\ell\not\equiv0\pmod p,
\]
contradicting \(p\mid n\). Thus every selected point has \(k\ge1\). Shifting all first coordinates down by \(1\) gives a representation of \(n/p\). The proof for \(q\) is symmetric. \(\square\)

This explains why Erdős–Lewin’s unrestricted infinitude cannot automatically yield coprime infinitude: a finite set of coprime non-representable “cores” can generate infinitely many non-representables by multiplication by \(p\) and \(q\).

## Self-Audit

1. **The synchronization of three modulus components is the most delicate part.**  
   The construction must preserve the \(A\)- and \(B\)-residues while changing the residue modulo \(m\). This is justified because endpoint exponents are shifted by least common multiples of the relevant multiplicative orders, low exponents are multiples of both orders, and every central term is simultaneously \(0\pmod{AB}\) and \(1\pmod m\).

2. **The \((9,2)\) case uses powers of \(9\), not a prime-base valuation.**  
   I explicitly use the underlying prime-power identity \(9^k=3^{2k}\): sufficiently large \(k\) makes the term vanish modulo any \(3^a\). The unit orbit needed on the other boundary is generated by \(2\) modulo \(3^a\), which was proved separately.

3. **The obstruction result applies only to fixed moduli.**  
   It does not rule out a sequence of moduli increasing with \(n\), where the least represented integer in a residue class is much larger than the modulus. I do not claim otherwise. The theorem genuinely proves only that every fixed admissible progression contains infinitely many representables.

## Computations To Verify

The following constructs the modular certificates from Theorem 2.

```python
from math import gcd, lcm

def order_mod(a, m):
    if m == 1:
        return 1
    assert gcd(a, m) == 1
    x = 1
    for h in range(1, m + 1):
        x = (x * a) % m
        if x == 1:
            return h
    raise AssertionError("order not found")

def discrete_log_generator(g, x, m):
    """Assumes x lies in <g> modulo m."""
    h = order_mod(g, m)
    y = 1 % m
    for e in range(h):
        if y == x % m:
            return e
        y = (y * g) % m
    raise AssertionError("target not in power orbit")

def prime_power_part(n, prime):
    part = 1
    while n % prime == 0:
        part *= prime
        n //= prime
    return part, n

def vanishing_exponent(base, modulus):
    """Used only when every prime of modulus divides base."""
    k, x = 0, 1
    while x % modulus != 0:
        k += 1
        x *= base
    return k

def raise_in_class(e, period, strict_lower_bound):
    while e <= strict_lower_bound:
        e += period
    return e

def modular_certificate(pair, M, r, index=0):
    """
    Returns (N, exponent_pairs), where:
      N == r mod M,
      gcd(N,p*q) == 1,
      exponent_pairs form an antichain.
    Increasing index gives unbounded certificates.
    """
    p, q = pair
    assert pair in {(5, 2), (9, 2), (5, 3)}
    assert M >= 1 and index >= 0

    if pair == (5, 2):
        P, Q = 5, 2
    elif pair == (9, 2):
        P, Q = 3, 2
    else:
        P, Q = 5, 3

    D = lcm(M, P * Q)

    # Choose a lift of r modulo D that is coprime to pq.
    start = r % M
    candidates = [
        x for x in range(start, D, M)
        if gcd(x, p * q) == 1
    ]
    assert candidates, "the progression is not (p,q)-admissible"
    R = candidates[0]

    A, rem = prime_power_part(D, P)
    B, m = prime_power_part(rem, Q)
    assert A * B * m == D
    assert gcd(m, p * q) == 1

    xA, xB, xm = R % A, R % B, R % m
    kthr = vanishing_exponent(p, A)
    lthr = vanishing_exponent(q, B)

    # Top exponent class.
    eL = discrete_log_generator(q, xA, A)
    periodL = lcm(order_mod(q, A), order_mod(q, m))
    top_mod_m = pow(q, eL, m)

    if pair in {(5, 2), (9, 2)}:
        # Binary expansion of the required odd residue modulo 2^b.
        b = B.bit_length() - 1
        bits = [j for j in range(b - 1, -1, -1)
                if (xB >> j) & 1]
        assert bits and bits[-1] == 0

        low_step = lcm(order_mod(p, B), order_mod(p, m))
        low_mod_m = sum(pow(q, j, m) for j in bits) % m
        t0 = (xm - top_mod_m - low_mod_m) % m

        # t central terms; t is fixed modulo m.
        t = t0 + index * m
        u, v = order_mod(p, m), order_mod(q, m)
        C = (kthr + u - 1) // u
        E = (lthr + v - 1) // v

        central = [
            (u * (C + i + 1), v * (E + t - i))
            for i in range(t)
        ]
        kmax = max((k for k, ell in central), default=0)
        lmax = max((ell for k, ell in central), default=0)

        L = raise_in_class(eL, periodL, max(lmax, lthr - 1))

        lower_bound = max(kmax, kthr - 1)
        H = lower_bound // low_step
        low = [
            ((H + i + 1) * low_step, j)
            for i, j in enumerate(bits)
        ]
        pairs = [(0, L)] + central + low

    else:
        # Pair (5,3): one bottom pure power realizes xB.
        eK = discrete_log_generator(p, xB, B)
        periodK = lcm(order_mod(p, B), order_mod(p, m))
        bottom_mod_m = pow(p, eK, m)
        t0 = (xm - top_mod_m - bottom_mod_m) % m
        t = t0 + index * m

        u, v = order_mod(p, m), order_mod(q, m)
        C = (kthr + u - 1) // u
        E = (lthr + v - 1) // v
        central = [
            (u * (C + i + 1), v * (E + t - i))
            for i in range(t)
        ]
        kmax = max((k for k, ell in central), default=0)
        lmax = max((ell for k, ell in central), default=0)

        L = raise_in_class(eL, periodL, max(lmax, lthr - 1))
        K = raise_in_class(eK, periodK, max(kmax, kthr - 1))
        pairs = [(0, L)] + central + [(K, 0)]

    pairs = sorted(pairs)
    assert all(pairs[i][0] < pairs[i + 1][0]
               for i in range(len(pairs) - 1))
    assert all(pairs[i][1] > pairs[i + 1][1]
               for i in range(len(pairs) - 1))

    N = sum((p ** k) * (q ** ell) for k, ell in pairs)
    assert N % D == R % D
    assert N % M == r % M
    assert gcd(N, p * q) == 1
    return N, pairs
```

Suggested exhaustive regression:

```python
for pair in [(5,2), (9,2), (5,3)]:
    p, q = pair
    for M in range(1, 100):
        for r in range(M):
            # Test whether the progression has a coprime lift.
            admissible = any(
                gcd(r + j*M, p*q) == 1
                for j in range(p*q + 1)
            )
            if admissible:
                N0, A0 = modular_certificate(pair, M, r, 0)
                N1, A1 = modular_certificate(pair, M, r, 1)
                assert N0 % M == r and N1 % M == r
                assert gcd(N0, p*q) == gcd(N1, p*q) == 1
```

For exact enumeration up to \(X\):

```python
def represented_up_to(p, q, X):
    K = 0
    while p ** (K + 1) <= X:
        K += 1
    L = 0
    while q ** (L + 1) <= X:
        L += 1

    represented = set()

    def dfs(k, ell_bound, total):
        if total > 0:
            represented.add(total)
        if k > K:
            return

        # Skip row k.
        dfs(k + 1, ell_bound, total)

        # Choose one point in row k.
        for ell in range(ell_bound):
            term = (p ** k) * (q ** ell)
            if total + term <= X:
                dfs(k + 1, ell, total + term)

    dfs(0, L + 1, 0)
    return represented
```

This can verify the peeling recurrence for all coprime \(n\le X\) by testing every feasible pair \(K,L\).

## Route Diagnosis

**Proved lemmas**

1. The four primitive-root assertions required for the critical pairs.
2. Every admissible arithmetic progression contains infinitely many coprime representable integers for \((5,2),(9,2),(5,3)\).
3. The exact boundary-peeling recurrence
   \[
   n=q^L+p^K+pq\,m
   \]
   with a necessary and sufficient bounding-box condition on the representation of \(m\).
4. Exact invariance of representability under division by \(p\) or \(q\) when the corresponding base divides \(n\).

**Dead ends**

- A missing reduced residue modulo \(p^a\), \(q^b\), or \(p^a q^b\): impossible for the three unresolved coprime pairs.
- Adding unrelated prime factors to the modulus: also impossible, because the central antidiagonal adjusts the residue modulo the coprime part.
- Deducing coprime infinitude directly from Erdős–Lewin unrestricted infinitude: blocked by the scaling equivalence.

**Precise block**

A successful boundary-layer descent must be size-sensitive. Although every finite residue condition is attainable, the constructed representation may be enormously larger than the modulus. One would need to prove that selected residue classes have no representation below a controlled size, or that all endpoint choices in Lemma 4 force an impossible chain of exponent bounds. I have no such estimate, and obtaining one appears comparable in strength to controlling the original weighted antichain count.

**Best next direction**

Study the least representable integer
\[
g_{p,q}(M,r)
=
\min\{n\in\mathcal R_{p,q}:n\equiv r\pmod M\}
\]
for growing \(M\), particularly \(M=p^a q^b\). The modular construction above shows \(g_{p,q}(M,r)<\infty\), but often with huge certificates. A superlinear lower bound for carefully chosen \(r=r(M)\), combined with a small positive representative of that residue, could yield infinitely many coprime non-representables. This would require quantitative boundary-layer or carry-compression arguments rather than another fixed finite automaton.