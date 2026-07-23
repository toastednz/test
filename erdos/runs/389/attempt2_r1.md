STATUS: BLOCKED

## Result

Route 1 yields a sharp structural reduction but not a complete solution. For \(N=2X\), let
\[
L_M(X)=\operatorname{lcm}_{0\le r\le M}\binom Nr.
\]
I prove that
\[
L_M(X)=\binom NM\,Q_M(N),
\qquad Q_M(N)\mid M!,
\]
where \(Q_M(N)\) is periodic in \(N\) modulo \(M!\). Thus the universal-boundary condition differs from the single condition \(R_M(X)\in\mathbb Z\) only by a bounded correction supported on primes \(p\le M\). I also prove an arbitrary-surplus sealing lemma: every prime \(p\le M\) can be forced, by a fixed CRT congruence, to contribute enough surplus to absorb this correction. Consequently Route 1 reduces to finding, in one explicit arithmetic progression, an \(X\) for which no moving prime \(p>M\) is deficient. This remaining statement retains the full endpoint-factorization obstruction and is presently unproved. As a finite structural confirmation, \(X=8178\) is proved directly to be a universal boundary for every \(0\le m\le8\); using the exact \(m=10\) computation supplied in the brief, \(X=45153\) is universal for every \(0\le m\le10\).

## Complete Argument

### 1. The truncated-row correction is supported only on small primes

Put
\[
N=2X,\qquad C_r=\binom Nr,\qquad C_*=\binom NX.
\]
For \(M<X\), define
\[
L_M(X)=\operatorname{lcm}_{0\le r\le M}C_r.
\]

Since \(C_M\) is one of the entries in the lcm, there is an integer \(Q_M(N)\) such that
\[
L_M(X)=C_MQ_M(N).
\]

For \(0\le r<M\),
\[
\frac{C_r}{C_M}
=
\frac{M!/r!}{(N-r)(N-r-1)\cdots(N-M+1)}.
\]
Therefore, for every prime \(p\),
\[
v_p(C_r)-v_p(C_M)
=
v_p\!\left(\frac{M!}{r!}\right)
-\sum_{i=r}^{M-1}v_p(N-i).
\]
It follows that
\[
\boxed{
v_p(Q_M(N))
=
\max\left(
0,\ 
\max_{0\le r<M}
\left[
v_p\!\left(\frac{M!}{r!}\right)
-\sum_{i=r}^{M-1}v_p(N-i)
\right]
\right).
}
\tag{1}
\]

In particular,
\[
0\le v_p(Q_M(N))\le v_p(M!),
\]
and hence
\[
\boxed{Q_M(N)\mid M!.}
\tag{2}
\]

For \(p>M\), the numerator \(M!/r!\) has no factor \(p\), so (1) gives
\[
v_p(C_r)\le v_p(C_M)\qquad(0\le r\le M).
\]
Thus
\[
\boxed{
p>M\Longrightarrow
v_p(L_M(X))=v_p\binom NM.
}
\tag{3}
\]

This is the decisive Route 1 simplification: all moving primes \(p>M\) are already controlled by the single last denominator \(\binom NM\). Universal divisibility introduces no additional moving-prime conditions.

---

### 2. Periodicity of the correction

Let \(e_p=v_p(M!)\). Formula (1) only needs the values
\[
\min(v_p(N-i),e_p),\qquad 0\le i<M.
\]
Indeed, the positive term \(v_p(M!/r!)\) is at most \(e_p\), so any denominator valuation above \(e_p\) can be truncated to \(e_p\) without changing the positive part.

These truncated valuations are determined by \(N-i\bmod p^{e_p}\). Hence \(Q_M(N)\) is periodic modulo
\[
\prod_{p\le M}p^{e_p}=M!.
\]
Thus
\[
\boxed{Q_M(N+M!)=Q_M(N).}
\tag{4}
\]

The universal-boundary condition now has the exact form
\[
L_M(X)\mid C_*
\iff
v_p(C_*)-v_p(C_M)\ge v_p(Q_M(2X))
\quad\text{for every }p.
\]
Since
\[
v_p(C_*)-v_p(C_M)=D_p(M,X),
\]
we obtain:

\[
\boxed{
X\text{ is universal through }M
\iff
D_p(M,X)\ge v_p(Q_M(2X))
\quad\text{for every prime }p.
}
\tag{5}
\]

For \(p>M\), the right side is zero by (2). Hence the only distinction between a solution for \(m=M\) and a universal solution through \(M\) is a bounded small-prime surplus.

---

### 3. Arbitrary-surplus sealing lemma

The ordinary sealing lemma can be strengthened substantially.

**Lemma.**  
Fix \(M\ge1\), a prime \(p\), and integers \(\alpha,s\ge1\) with
\[
p^\alpha>M.
\]
Let \(k=X-M>0\). If
\[
\boxed{
k\equiv-p^\alpha\pmod{p^{\alpha+s}},
}
\tag{6}
\]
then
\[
\boxed{D_p(M,X)\ge s.}
\tag{7}
\]

**Proof.**

Write
\[
E_{p^a}(M,X)
=
\left\lfloor
\frac{2(X\bmod p^a)-(M\bmod p^a)}{p^a}
\right\rfloor.
\]

Because (6) implies \(p^\alpha\mid k\), for \(a\le\alpha\),
\[
X\equiv M\pmod{p^a},
\]
and consequently
\[
E_{p^a}(M,X)=0.
\]

Now let \(a=\alpha+b\) with \(1\le b\le s\). Reducing (6) modulo \(p^{\alpha+b}\) gives
\[
k\bmod p^{\alpha+b}=p^{\alpha+b}-p^\alpha.
\]
Since \(M<p^\alpha\),
\[
X\bmod p^{\alpha+b}
=
p^{\alpha+b}-p^\alpha+M.
\]
Writing \(q=p^{\alpha+b}\), we get
\[
2(X\bmod q)-M=2q-2p^\alpha+M.
\]
This is at least \(q\), because
\[
q-2p^\alpha+M
=
p^\alpha(p^b-2)+M\ge0.
\]
It is strictly below \(2q\), since \(M<p^\alpha\). Therefore
\[
E_q(M,X)=1
\qquad(\alpha<a\le\alpha+s).
\]

These \(s\) levels all occur below \(Y=2X-M\). Indeed, every positive solution of (6) has
\[
k\ge p^{\alpha+s}-p^\alpha,
\]
and therefore
\[
Y=M+2k
\ge M+2p^{\alpha+s}-2p^\alpha
\ge p^{\alpha+s}.
\]

Finally, for \(a>\alpha+s\), the residue \(k\bmod p^a\) is a multiple of \(p^\alpha\), between \(0\) and \(p^a-p^\alpha\). Since \(M<p^\alpha\), addition of \(M\) does not wrap modulo \(p^a\), and
\[
X\bmod p^a\ge M.
\]
Thus
\[
2(X\bmod p^a)-M\ge0,
\]
so no later level is negative.

There are therefore \(s\) explicit positive levels and no negative level, proving \(D_p(M,X)\ge s\). ∎

---

### 4. Simultaneous absorption of the entire truncated-lcm correction

For every prime \(p\le M\), put
\[
e_p=v_p(M!)
\]
and choose \(\alpha_p\) such that
\[
p^{\alpha_p}>M.
\]
Impose on \(k=X-M\) the simultaneous congruences
\[
\boxed{
k\equiv-p^{\alpha_p}
\pmod{p^{\alpha_p+e_p}}
\qquad(p\le M).
}
\tag{8}
\]
The moduli are pairwise coprime, so the Chinese remainder theorem gives an infinite arithmetic progression of positive \(k\).

The surplus lemma gives
\[
D_p(M,X)\ge e_p=v_p(M!)\ge v_p(Q_M(2X))
\qquad(p\le M).
\]
Combining this with (5) proves:

**Proposition.**  
Every \(X=M+k\) satisfying (8) is universal through \(M\), provided that
\[
\boxed{
D_p(M,X)\ge0\qquad\text{for every prime }p>M.
}
\tag{9}
\]

Thus Route 1 has reduced the proposed universal-boundary theorem to the following precise moving-prime problem:

> For each \(M\), prove that the explicit CRT progression (8) contains at least one \(X\) satisfying (9).

This is where the route blocks. Condition (9) still involves all large prime divisors of
\[
X,\ X-1,\ldots,X-\left\lceil\frac M2\right\rceil+1
\]
and all their prime-power compensation chains. The fixed progression controls the small primes perfectly but does not control fresh endpoint cofactors.

---

### 5. A fully verified universal boundary through \(M=8\)

I now give a finite exact certificate showing that \(X=8178\) works simultaneously for every \(0\le r\le8\).

Set
\[
N=2X=16356.
\]
The last truncated-row entry factors as
\[
\begin{aligned}
\binom{16356}{8}
={}&2^2 3^2 5^2\cdot
13\cdot17\cdot23\cdot29\cdot37\cdot47\\
&{}\cdot73\cdot79\cdot83\cdot109\cdot197
\cdot3271\cdot16349.
\end{aligned}
\tag{10}
\]
This follows from
\[
\begin{array}{rcl}
16356&=&2^2\cdot3\cdot29\cdot47,\\
16355&=&5\cdot3271,\\
16354&=&2\cdot13\cdot17\cdot37,\\
16353&=&3^2\cdot23\cdot79,\\
16352&=&2^5\cdot7\cdot73,\\
16351&=&83\cdot197,\\
16350&=&2\cdot3\cdot5^2\cdot109,\\
16349&=&16349,
\end{array}
\]
followed by division by
\[
8!=2^7 3^2 5\cdot7.
\]
The displayed factors are prime; for \(3271\) and \(16349\), trial division by primes up to their respective square roots \(<58\) and \(<128\) suffices.

For \(a_r(p)=v_p\binom{16356}{r}\), the sequences for \(1\le r\le8\) are

\[
\begin{array}{c|c|c|c}
p & (a_1,\ldots,a_8)&\max_{r\le8}a_r&a_8\\ \hline
2&(2,1,2,0,5,4,5,2)&5&2\\
3&(1,1,0,2,2,1,2,2)&2&2\\
5&(0,1,1,1,0,0,2,2)&2&2\\
7&(0,0,0,0,1,1,0,0)&1&0.
\end{array}
\tag{11}
\]

Meanwhile, the central valuations are
\[
v_2\binom{16356}{8178}=10,
\quad
v_3\binom{16356}{8178}=5,
\quad
v_5\binom{16356}{8178}=3,
\quad
v_7\binom{16356}{8178}=2.
\tag{12}
\]
For \(p=2\), this follows from
\[
8178=2^{12}+2^{11}+2^{10}+2^9+2^8+2^7+2^6+2^5+2^4+2,
\]
which has ten binary ones.

For the other small primes, the positive central-carry levels are

\[
\begin{array}{c|c}
p& p^a\text{ with }8178\bmod p^a\ge p^a/2\\ \hline
3&9,27,81,243,2187\\
5&5,3125,15625\\
7&49,343.
\end{array}
\]

For every prime \(p>8\) appearing in (10), one positive carry level is exhibited below:

\[
\begin{array}{c|c|c}
p&q=p^a&8178\bmod q\\ \hline
13&2197&1587\\
17&4913&3265\\
23&23&13\\
29&841&609\\
37&1369&1333\\
47&2209&1551\\
73&5329&2849\\
79&79&41\\
83&83&44\\
109&11881&8178\\
197&197&101\\
3271&3271&1636\\
16349&16349&8178.
\end{array}
\tag{13}
\]
Every residue in the third column is at least half of the corresponding modulus. Hence each prime factor of \(\binom{16356}{8}\) occurs to at most its exponent in the central binomial coefficient. Thus
\[
\binom{16356}{8}\mid\binom{16356}{8178}.
\]

For \(p>8\), equation (3) shows that
\[
v_p\binom{16356}{r}\le v_p\binom{16356}{8}
\qquad(0\le r\le8).
\]
For \(p=2,3,5,7\), the maxima in (11) are bounded by the central valuations in (12). Therefore
\[
\boxed{
\binom{16356}{r}\mid\binom{16356}{8178}
\qquad(0\le r\le8).
}
\]
Equivalently,
\[
\boxed{L_8(8178)\mid\binom{16356}{8178}.}
\]

In fact, from (11),
\[
Q_8(16356)=2^3\cdot7=56.
\]

---

### 6. The supplied \(X=45153\) candidate is universal through \(M=10\)

The brief supplies the exact fact
\[
\binom{90306}{10}\mid\binom{90306}{45153}.
\]
For the four primes at most \(10\), the truncated-row valuations are:

\[
\begin{array}{c|c|c}
p&(v_p\binom{90306}{r})_{r=1}^{10}&
v_p\binom{90306}{45153}\\ \hline
2&(1,0,6,4,5,4,6,3,4,3)&6\\
3&(2,2,1,2,2,1,2,2,0,2)&5\\
5&(0,1,1,1,0,0,2,2,2,1)&3\\
7&(0,0,0,0,0,0,0,0,0,0)&3.
\end{array}
\]
Thus the central valuation dominates the maximum truncated-row valuation at every \(p\le10\). For \(p>10\), equation (3) shows that the \(r=10\) valuation dominates every earlier entry. Therefore
\[
\boxed{
\binom{90306}{r}\mid\binom{90306}{45153}
\qquad(0\le r\le10).
}
\]
Here
\[
Q_{10}(90306)=2^3\cdot5=40.
\]

So the repeated boundary at \(X=45153\) is not merely shared by \(m=9,10\): it works for every \(m\le10\).

## Self-Audit

1. **The \(M=10\) conclusion uses the exact finite computation supplied in the brief.**  
   I have independently reduced universality to the displayed four small-prime rows, but I did not print a full factorization certificate for \(\binom{90306}{10}\mid\binom{90306}{45153}\). I believe it holds because it is explicitly part of the supplied minimal-value data and is independently checkable by the code below. The \(M=8\) certificate is self-contained and does not rely on this input.

2. **The finite \(M=8\) certificate contains substantial hand arithmetic.**  
   A mistaken factor or residue would affect only that finite illustration, not the general lemmas. The factorization, row-valuation sequences, and carry residues are all independently reproducible by the two valuation implementations below.

3. **The reduction to the CRT progression does not establish that the progression contains a success.**  
   This is not being treated as a proof. The surplus lemma controls all \(p\le M\), but the remaining \(p>M\) condition is of comparable difficulty to the original moving-prime problem. This is precisely why the route is marked BLOCKED.

## Computations To Verify

```python
from math import isqrt, factorial

def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for d in range(2, isqrt(n) + 1):
        if sieve[d]:
            sieve[d*d:n+1:d] = b"\x00" * (((n - d*d) // d) + 1)
    return [p for p in range(2, n + 1) if sieve[p]]

def vp_fact(n, p):
    ans = 0
    while n:
        n //= p
        ans += n
    return ans

def vp_binom(n, r, p):
    return vp_fact(n, p) - vp_fact(r, p) - vp_fact(n-r, p)

def central_vp(X, p):
    return vp_binom(2*X, X, p)

def D_legendre(m, X, p):
    Y = 2*X - m
    return vp_fact(Y, p) + vp_fact(m, p) - 2*vp_fact(X, p)

def D_residue(m, X, p):
    Y = 2*X - m
    q = p
    ans = 0
    while q <= Y:
        ans += (2*(X % q) - (m % q)) // q
        q *= p
    return ans

def candidate(m, X):
    assert X > m
    Y = 2*X - m
    for p in primes_upto(Y):
        d1 = D_legendre(m, X, p)
        d2 = D_residue(m, X, p)
        assert d1 == d2
        if d1 < 0:
            return False, p
    return True, None

def universal(M, X):
    """Checks C(2X,r) | C(2X,X) for every 0 <= r <= M."""
    assert X > M
    N = 2*X
    for p in primes_upto(N):
        central = central_vp(X, p)
        rowmax = max(vp_binom(N, r, p) for r in range(M + 1))
        if central < rowmax:
            return False, p, central, rowmax
    return True, None, None, None

def correction_Q(M, X):
    """Returns Q with lcm_{r<=M} C(2X,r) = C(2X,M)*Q."""
    N = 2*X
    Q = 1
    for p in primes_upto(M):
        base = vp_binom(N, M, p)
        excess = max(vp_binom(N, r, p) - base for r in range(M + 1))
        Q *= p ** max(0, excess)
    return Q

# Main finite checks.
assert universal(8, 8178)[0]
assert correction_Q(8, 8178) == 56

assert candidate(10, 45153)[0]
assert universal(10, 45153)[0]
assert correction_Q(10, 45153) == 40

# Earlier observed universal boundaries.
assert universal(2, 6)[0]
assert universal(4, 210)[0]
assert universal(5, 2480)[0]

# Verify Q_M(N) | M! and periodicity modulo M!.
for M in range(1, 20):
    period = factorial(M)
    for X in range(M + 1, M + 200):
        q = correction_Q(M, X)
        assert period % q == 0
        assert correction_Q(M, X + period) == q
```

Surplus-sealing test:

```python
def vp_integer(n, p):
    e = 0
    while n % p == 0 and n:
        n //= p
        e += 1
    return e

def crt_pair(a, m, b, n):
    # m,n coprime
    t = ((b - a) * pow(m, -1, n)) % n
    x = a + m*t
    return x % (m*n), m*n

def surplus_progression(M):
    """
    Constructs k modulo a CRT modulus so that
    D_p(M, M+k) >= v_p(M!) for every p <= M.
    """
    a, mod = 0, 1
    for p in primes_upto(M):
        s = vp_fact(M, p)
        alpha = 1
        while p**alpha <= M:
            alpha += 1
        newmod = p**(alpha + s)
        residue = (-p**alpha) % newmod
        a, mod = crt_pair(a, mod, residue, newmod)
    if a == 0:
        a += mod
    return a, mod

for M in range(2, 20):
    k0, mod = surplus_progression(M)
    for t in range(5):
        k = k0 + t*mod
        X = M + k
        for p in primes_upto(M):
            assert D_legendre(M, X, p) >= vp_fact(M, p)
```

A direct search for universal boundaries:

```python
def least_universal(M, bound):
    for X in range(M + 1, bound + 1):
        if universal(M, X)[0]:
            return X
    return None

for M in range(1, 11):
    print(M, least_universal(M, 50000))
```

## Route Diagnosis

The truncated-binomial-lcm viewpoint works better than expected algebraically:

- all extra universal-boundary requirements are supported on \(p\le M\);
- the correction \(Q_M(2X)\) divides \(M!\) and is periodic modulo \(M!\);
- arbitrary small-prime surplus can be sealed by explicit CRT congruences;
- the repeated observed boundaries really can be universal for long initial segments.

The route nevertheless remains blocked at the moving primes. After imposing the surplus progression, one must still prove the existence of a representative for which every \(p>M\) satisfies \(D_p(M,X)\ge0\). These are exactly the primes arising from uncontrolled endpoint cofactors and their higher-power compensation chains. Existing CRT, smoothness, and prime-gap tools do not prove that even one representative succeeds; every fixed progression also contains infinitely many failures.

A fresh attempt should therefore not spend further effort on the small-prime lcm correction—it is now completely controlled. The missing theorem should target large primes in the explicit surplus progression, perhaps by exploiting that odd offsets \(2X-i\) are automatically central-carry levels when \(i\) is odd, while the genuinely dangerous levels are localized to the even offsets \(2X-2j=2(X-j)\). Without a new global theorem preventing these exact endpoint deficits from covering the entire progression, Route 1 cannot close the problem.