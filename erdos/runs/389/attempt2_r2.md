STATUS: BLOCKED

## Result

Route 2 yields a rigorous and useful local theory but not a complete construction. For every prime \(p>m\), all negative \(p\)-power contributions come from exactly one endpoint \(X-j\), and their number is precisely \(v_p(X-j)\). I prove an exact cofactor-digit formula for every possible compensating positive level, as well as a generalized self-compensation criterion allowing repeated prime factors. When the small primes are sealed by imposing \(p^A\mid X-m\), the proposed factorization construction becomes a simultaneous system of “relative weak primary pseudoperfect” congruences for the shifted numbers \(1+(X-m)/a\), with \(a\) ranging over the upper half of \(\{1,\dots,m\}\). This reduction is exact and exposes the block: no unconditional method is known here for producing even one such synchronized system, and ordinary CRT cannot prescribe it because its congruences depend on the unknown prime divisors of the final numbers. Moreover, the rigid one-step congruence is not exhibited by the known solution \(m=3,X=210\), where some primes compensate only at the \(p^3\)-level.

## Complete Argument

### 1. Exact localization and counting of all negative levels

Assume throughout this section that \(m\ge1\), put

\[
H=\left\lceil\frac m2\right\rceil,\qquad Y=2X-m,
\]

and let \(p>m\) be prime.

For \(q=p^a\), the residue formula simplifies to

\[
E_q(m,X)=
\left\lfloor\frac{2(X\bmod q)-m}{q}\right\rfloor,
\]

because \(m\bmod q=m\).

#### Lemma 1: Endpoint localization is exact

For every \(a\ge1\),

\[
E_{p^a}(m,X)=-1
\]

if and only if

\[
p^a\mid X-j
\]

for some unique \(j\in\{0,\dots,H-1\}\).

If such a \(j\) exists for \(a=1\), and

\[
t=v_p(X-j),
\]

then

\[
E_{p^a}(m,X)=-1\quad\Longleftrightarrow\quad 1\le a\le t.
\]

In particular, there are exactly \(t\) negative levels in the entire \(p\)-chain.

#### Proof

Write \(r=X\bmod p^a\). Since \(0\le r<p^a\) and \(m<p^a\),

\[
E_{p^a}=-1
\iff 2r-m<0
\iff r<\frac m2
\iff 0\le r<H.
\]

Thus \(r=j\) for a unique \(j\in\{0,\dots,H-1\}\), which is equivalent to \(p^a\mid X-j\).

If \(E_p=-1\), let \(j=X\bmod p\), so \(0\le j<H<p\). At any later negative level \(p^a\), the corresponding endpoint index must reduce to \(j\) modulo \(p\). Since all possible indices lie in \([0,H-1]\subset[0,p-1]\), it is the same integer \(j\). Therefore

\[
E_{p^a}=-1\iff p^a\mid X-j,
\]

and these are exactly the levels \(1\le a\le v_p(X-j)\). ∎

A useful consequence is that if \(p>m\) divides none of

\[
X,\ X-1,\ldots,X-H+1,
\]

then \(D_p(m,X)\ge0\): its chain contains no negative terms.

---

### 2. Exact cofactor-digit formula

Suppose \(p>m\) divides the endpoint

\[
N=X-j,\qquad 0\le j<H.
\]

Write

\[
N=p^t u,\qquad t=v_p(N),\qquad p\nmid u.
\]

By Lemma 1, the first \(t\) levels contribute \(-1\).

For \(s\ge1\), consider the level \(p^{t+s}\). Since \(j<p\le p^t\),

\[
X=N+j
\equiv p^t(u\bmod p^s)+j
\pmod {p^{t+s}},
\]

and the displayed quantity is already in \([0,p^{t+s}-1]\). Therefore:

#### Lemma 2: Exact compensation criterion

For every \(s\ge1\),

\[
E_{p^{t+s}}(m,X)=1
\]

if and only if

\[
\boxed{
u\bmod p^s
\ge
\left\lceil
\frac{p^{t+s}+m-2j}{2p^t}
\right\rceil.
}
\]

Consequently,

\[
\boxed{
D_p(m,X)
=
-t+
\#\left\{
s\ge1:
p^{t+s}\le Y,\ 
u\bmod p^s
\ge
\left\lceil
\frac{p^{t+s}+m-2j}{2p^t}
\right\rceil
\right\}.
}
\]

#### Proof

For \(r=j+p^t(u\bmod p^s)\), Lemma 1 shows that no level beyond \(t\) is negative. Hence it is positive precisely when

\[
2r-m\ge p^{t+s}.
\]

Substituting the value of \(r\) and solving for the integral residue \(u\bmod p^s\) gives the claimed inequality. Combining this with the \(t\) initial negative levels proves the formula for \(D_p\). ∎

This formula is a complete local description for every moving prime \(p>m\). It shows that compensation is an upper-half condition on suitable truncations of the endpoint cofactor in base \(p\).

---

### 3. One-step self-compensation

The condition suggested in Route 2 is the extreme choice

\[
t=1,\qquad \frac Np\equiv-1\pmod p.
\]

#### Proposition 3: Rigid one-step sealing

Let \(p>m+2\), let \(0\le j<H\), and suppose

\[
v_p(X-j)=1,\qquad \frac{X-j}{p}\equiv-1\pmod p.
\]

Then

\[
D_p(m,X)\ge0.
\]

#### Proof

Put \(N=X-j=pu\). The congruence says \(u\bmod p=p-1\), so

\[
X\bmod p^2=p(p-1)+j=p^2-p+j.
\]

The \(p\)-level contributes \(-1\). At level \(p^2\),

\[
2(X\bmod p^2)-m-p^2
=
p^2-2p+2j-m.
\]

Since \(p\ge m+3\),

\[
p^2-2p+2j-m
\ge p^2-2p-m
\ge (m+3)^2-2(m+3)-m
=m^2+3m+3>0.
\]

Thus \(E_{p^2}=1\). By Lemma 1, exact divisibility \(v_p(N)=1\) precludes any later negative level. Hence

\[
D_p\ge -1+1=0.
\]

∎

The congruence \(-1\pmod p\) is stronger than necessary. Lemma 2 shows that it is enough to have

\[
\frac Np\bmod p
\ge
\left\lceil\frac{p^2+m-2j}{2p}\right\rceil,
\]

which is roughly an upper-half residue condition.

---

### 4. Repeated prime factors can also self-compensate

The exact-once requirement can be removed by replacing it with a prime-power congruence.

#### Proposition 4: Generalized prime-power self-compensation

Let \(p>m+2\), let \(0\le j<H\), and write

\[
X-j=p^t u,\qquad p\nmid u.
\]

If

\[
u\equiv-1\pmod {p^t},
\]

equivalently,

\[
\boxed{p^{2t}\mid X-j+p^t,}
\]

then

\[
D_p(m,X)\ge0.
\]

#### Proof

The first \(t\) levels contribute \(-1\) by Lemma 1.

For each \(1\le s\le t\),

\[
u\bmod p^s=p^s-1.
\]

At level \(p^{t+s}\), the residue of \(X\) is therefore

\[
r=p^t(p^s-1)+j=p^{t+s}-p^t+j.
\]

Then

\[
2r-m-p^{t+s}
=
p^{t+s}-2p^t+2j-m
=
p^t(p^s-2)+2j-m.
\]

Since \(s\ge1\),

\[
p^s-2\ge p-2>m,
\]

and hence the displayed quantity is positive. Thus each of

\[
p^{t+1},p^{t+2},\ldots,p^{2t}
\]

contributes \(+1\). These \(t\) positive contributions cancel the \(t\) negative contributions, and all remaining levels are nonnegative by Lemma 1. ∎

This is the natural repeated-prime version of Route 2.

---

### 5. A rigorous sufficient construction theorem

Let \(P\ge m+2\). For every prime \(p\le P\), choose \(A_p\) such that

\[
p^{A_p}>m,
\]

and put

\[
M=\prod_{p\le P}p^{A_p}.
\]

#### Proposition 5

Suppose \(K\) is a positive multiple of \(M\), put

\[
X=m+K,
\]

and assume that for every \(0\le j<H\) and every prime \(p>P\) dividing \(X-j\), with

\[
t=v_p(X-j),
\]

one has

\[
\frac{X-j}{p^t}\equiv-1\pmod {p^t}.
\]

Then \(R_m(X)\) is an integer.

The exact-once version of Route 2 is obtained by requiring additionally that all these exponents satisfy \(t=1\).

#### Proof

For \(p\le P\), we have \(p^{A_p}\mid X-m\) and \(p^{A_p}>m\). The sealing lemma therefore gives

\[
D_p(m,X)\ge0.
\]

For \(p>P\), either \(p\) divides none of the endpoints, in which case Lemma 1 gives \(D_p\ge0\), or \(p\) divides a unique endpoint and Proposition 4 gives \(D_p\ge0\).

Thus \(D_p(m,X)\ge0\) for every prime \(p\), proving integrality. ∎

This theorem completes the local part of Route 2. The unresolved issue is the existence of \(K\) satisfying its factorization hypotheses.

---

### 6. Exact reformulation after sealing the small primes

The sealing strategy makes the unresolved global condition especially rigid.

Let

\[
a=m-j,
\]

so \(a\) ranges through

\[
\mathcal A_m=\{m-H+1,\ldots,m\}.
\]

Since \(X=m+K\),

\[
X-j=K+a.
\]

Because \(K\) is divisible by \(p^{A_p}\) with \(p^{A_p}>m\), every \(a\le m\) divides \(K\). Define

\[
Q_a=1+\frac Ka,
\]

so that

\[
K+a=aQ_a.
\]

Moreover, for every \(p\le P\),

\[
v_p(K+a)=v_p(a).
\]

Indeed, \(v_p(K)>v_p(a)\), and the valuation of a sum with unequal valuations is the smaller one. Therefore

\[
\gcd(Q_a,\prod_{p\le P}p)=1.
\]

Thus every prime factor of \(Q_a\) exceeds \(P\).

Under the exact-once version of Route 2, \(Q_a\) is squarefree and the required congruence is

\[
a\frac{Q_a}{p}\equiv-1\pmod p
\qquad(p\mid Q_a).
\]

#### Lemma 6: Relative weak-primary-pseudoperfect identity

Let \(Q>1\) be squarefree and coprime to \(a\). Then

\[
a\frac Qp\equiv-1\pmod p
\qquad\text{for every }p\mid Q
\]

if and only if

\[
\boxed{
\frac1Q+a\sum_{p\mid Q}\frac1p\in\mathbb Z.
}
\]

#### Proof

Set

\[
C=1+a\sum_{p\mid Q}\frac Qp.
\]

Modulo a fixed \(p\mid Q\), all terms \(Q/q\) with \(q\ne p\) vanish, leaving

\[
C\equiv1+a\frac Qp\pmod p.
\]

Thus the family of congruences is equivalent to \(p\mid C\) for every \(p\mid Q\). Since \(Q\) is squarefree, this is equivalent to \(Q\mid C\). Finally,

\[
\frac CQ=\frac1Q+a\sum_{p\mid Q}\frac1p.
\]

∎

Consequently, the sealed exact-once construction asks for a single \(K\) such that, simultaneously for every \(a\in\mathcal A_m\),

\[
\boxed{
Q_a=1+\frac Ka
\text{ is \(P\)-rough and squarefree, and }
\frac1{Q_a}
+a\sum_{p\mid Q_a}\frac1p\in\mathbb Z.
}
\]

These \(Q_a\) must also be pairwise coprime.

#### Lemma 7: Pairwise coprimality

If \(a,b\in\mathcal A_m\) are distinct, then

\[
\gcd(Q_a,Q_b)=1.
\]

#### Proof

If a prime \(p\) divided both, then \(p>P\) and

\[
p\mid aQ_a=K+a,\qquad p\mid bQ_b=K+b.
\]

Hence \(p\mid a-b\). But

\[
0<|a-b|<m<P<p,
\]

which is impossible. ∎

This synchronization requirement is much stronger than constructing the numbers \(Q_a\) independently.

---

### 7. A size obstruction to a limiting-CRT construction

Let

\[
r_a=\omega(Q_a).
\]

The integer in Lemma 6 is positive, so it is at least \(1\). Hence

\[
a\sum_{p\mid Q_a}\frac1p
\ge1-\frac1{Q_a}.
\]

Because every \(p\mid Q_a\) exceeds \(P\),

\[
\sum_{p\mid Q_a}\frac1p<\frac{r_a}{P}.
\]

Also \(Q_a>P\), so \(1-1/Q_a>1-1/P\). It follows that

\[
\boxed{
r_a>\frac{P-1}{a}.
}
\]

In particular,

\[
r_a\ge \left\lfloor\frac{P-1}{a}\right\rfloor+1
\]

and, since every prime divisor exceeds \(P\),

\[
Q_a>P^{r_a}.
\]

Thus increasing \(P\) in an attempt to seal more primes forces every shifted factor \(Q_a\) to acquire an increasing number of previously unknown large prime divisors. This is a rigorous form of the circularity obstructing sequential CRT.

---

### 8. Generalized reciprocal identity for prime-power components

The repeated-factor condition of Proposition 4 has a similar exact reformulation.

Write

\[
Q=\prod_{i=1}^r q_i,\qquad q_i=p_i^{t_i},
\]

where the \(p_i\) are distinct. Then

\[
a\frac Q{q_i}\equiv-1\pmod {q_i}
\quad(1\le i\le r)
\]

if and only if

\[
\boxed{
\frac1Q+a\sum_{i=1}^r\frac1{q_i}\in\mathbb Z.
}
\]

The proof is identical to that of Lemma 6, using the pairwise coprimality of the prime powers \(q_i\).

Thus allowing repeated prime factors does not remove the self-referential global condition; it replaces reciprocal primes by reciprocal prime powers.

---

### 9. The limited Euclid-type extension mechanism

There is one exact way to enlarge an individual relative solution.

Suppose

\[
F_a(Q)=\frac1Q+a\sum_{p\mid Q}\frac1p
\]

is an integer and

\[
q=aQ+1
\]

is a new prime. Then

\[
F_a(Qq)
=
F_a(Q)+\frac{aQ+1-q}{Qq}
=
F_a(Q).
\]

Hence \(Qq\) is another relative weak-primary-pseudoperfect solution.

For the prime-power version, the same argument works if \(q=aQ+1\) is a prime power and is treated as one prime-power component.

This gives the familiar recursion

\[
N=aQ\longmapsto N(N+1)
\]

when \(N+1\) is a prime or an admissible prime power. It does not solve the present problem for two reasons:

1. the required primality or prime-power condition is itself uncontrolled;
2. different \(a\)'s must satisfy
   \[
   a(Q_a-1)=K
   \]
   with the same \(K\), so independent Euclid recursions do not synchronize.

---

### 10. The rigid congruence is not the pattern of known solutions

For the known solution

\[
m=3,\qquad X=210,\qquad Y=417,
\]

the endpoints are \(210\) and \(209\).

For \(p=5\mid210\),

\[
\frac{210}{5}=42\equiv2\pmod5,
\]

not \(-1\pmod5\). Its ledger is instead

\[
E_5=-1,\qquad E_{25}=0,\qquad E_{125}=1.
\]

For \(p=7\mid210\),

\[
\frac{210}{7}=30\equiv2\pmod7,
\]

again not \(-1\pmod7\), and

\[
E_7=-1,\qquad E_{49}=0,\qquad E_{343}=1.
\]

By contrast, the primes dividing \(209\) compensate at their squares:

\[
\begin{aligned}
p=11:&\quad E_{11}=-1,\quad E_{121}=1,\\
p=19:&\quad E_{19}=-1,\quad E_{361}=1.
\end{aligned}
\]

Thus the exact \(-1\) condition is a sufficient certificate, not an empirically supported necessary pattern. Any viable continuation of Route 2 should allow bounded-depth upper-half digit matching from Lemma 2.

---

### 11. Precise point where the route is blocked

Proposition 5 would solve the problem if, for every \(m\), one could produce a \(K\) satisfying its simultaneous endpoint factorization conditions. After small-prime sealing, the exact-once version requires

\[
Q_a=1+\frac Ka,\qquad a\in\mathcal A_m,
\]

to be pairwise coprime, \(P\)-rough, squarefree relative weak-primary-pseudoperfect numbers, all tied to the same \(K\).

No argument developed here proves the existence of such a \(K\), even for a fixed pair of distinct values of \(a\). CRT cannot impose the required congruences in advance because they quantify over the unknown prime divisors of \(Q_a\). The Euclid recursion constructs at most one \(Q_a\) at a time and introduces uncontrolled prime or prime-power conditions. Broadening to the exact digit criterion in Lemma 2 removes the reciprocal identity but turns the problem into a simultaneous shifted factorization-and-digit problem of essentially the original strength.

Accordingly, Route 2 is **blocked**, not solved.

## Self-Audit

1. **The construction obstruction is not an impossibility theorem.**  
   I have not proved that simultaneous relative weak-primary-pseudoperfect shifts do not exist. I only proved that the stated sealing implementation is exactly equivalent to producing them. This is why the status is BLOCKED rather than SOLVED-DISPROOF.

2. **The threshold \(p>m+2\) is deliberately nonoptimal.**  
   Some smaller primes also satisfy Propositions 3 and 4, but the uniform inequality used in the proof is clean and sufficient. The conclusions stated under this threshold follow directly from the displayed inequalities.

3. **The reciprocal reduction applies only after full small-prime sealing.**  
   For an arbitrary successful \(X\), its endpoint small-prime parts need not equal \(a=m-j\); for example \(X=210\) does not arise from the sealed setup. The reduction is nevertheless exact for the proposed Route-2 construction because \(p^{A_p}\mid K\) with \(p^{A_p}>m\) forces both \(a\mid K\) and \(v_p(K+a)=v_p(a)\).

## Computations To Verify

```python
from fractions import Fraction
from sympy import primerange, factorint

def E_level(m, X, q):
    # Python // is floor division, including for negative numerators.
    return (2 * (X % q) - (m % q)) // q

def prime_ledger(m, X, p):
    Y = 2 * X - m
    out = []
    q = p
    while q <= Y:
        out.append((q, E_level(m, X, q)))
        q *= p
    return out

def is_solution(m, X):
    Y = 2 * X - m
    for p in primerange(2, Y + 1):
        if sum(e for q, e in prime_ledger(m, X, p)) < 0:
            return False
    return True

# Mandatory known example.
assert is_solution(3, 210)
assert prime_ledger(3, 210, 5) == [(5, -1), (25, 0), (125, 1)]
assert prime_ledger(3, 210, 7) == [(7, -1), (49, 0), (343, 1)]
assert prime_ledger(3, 210, 11) == [(11, -1), (121, 1)]
assert prime_ledger(3, 210, 19) == [(19, -1), (361, 1)]

def check_endpoint_digit_formula(m, X, p):
    """
    Verifies Lemmas 1 and 2 for one p > m.
    """
    assert p > m
    H = (m + 1) // 2
    Y = 2 * X - m

    endpoints = [j for j in range(H) if (X - j) % p == 0]

    if not endpoints:
        assert all(e >= 0 for q, e in prime_ledger(m, X, p))
        return True

    assert len(endpoints) == 1
    j = endpoints[0]
    N = X - j

    t = 0
    z = N
    while z % p == 0:
        z //= p
        t += 1
    u = z

    ledger = dict(prime_ledger(m, X, p))

    for a in range(1, t + 1):
        assert ledger[p**a] == -1

    s = 1
    while p**(t + s) <= Y:
        q = p**(t + s)
        threshold_num = q + m - 2*j
        threshold = (threshold_num + 2*p**t - 1) // (2*p**t)
        predicted = 1 if (u % p**s) >= threshold else 0
        assert ledger[q] == predicted
        s += 1

    return True

def sealing_modulus(m, P):
    """
    M = product p^A over p <= P, where p^A > m.
    """
    M = 1
    for p in primerange(2, P + 1):
        q = p
        while q <= m:
            q *= p
        M *= q
    return M

def strict_route2_condition(m, P, K):
    """
    Exact-once/-1 version of Proposition 5.
    """
    M = sealing_modulus(m, P)
    if K <= 0 or K % M:
        return False

    X = m + K
    H = (m + 1) // 2

    for j in range(H):
        N = X - j
        for p, e in factorint(N).items():
            if p > P:
                if e != 1:
                    return False
                if (N // p) % p != p - 1:
                    return False
    return True

def generalized_route2_condition(m, P, K):
    """
    Prime-power version of Proposition 5.
    """
    M = sealing_modulus(m, P)
    if K <= 0 or K % M:
        return False

    X = m + K
    H = (m + 1) // 2

    for j in range(H):
        N = X - j
        for p, t in factorint(N).items():
            if p > P:
                q = p**t
                if ((N // q) + 1) % q:
                    return False
    return True

def relative_identity(a, Q):
    fac = factorint(Q)
    if any(e != 1 for e in fac.values()):
        return None
    value = Fraction(1, Q)
    for p in fac:
        value += Fraction(a, p)
    return value

def search_route2(m, P, multiplier_bound, generalized=False):
    """
    Searches K = c*M for a sufficient Route-2 certificate.
    A found value is a rigorous solution after is_solution confirms it.
    Failure to find one proves nothing.
    """
    M = sealing_modulus(m, P)
    test = generalized_route2_condition if generalized else strict_route2_condition

    for c in range(1, multiplier_bound + 1):
        K = c * M
        if test(m, P, K):
            X = m + K
            assert is_solution(m, X)
            return K, X
    return None

# Verify pairwise-coprime Q_a and the reciprocal identities
# whenever a strict certificate is found.
def audit_strict_certificate(m, P, K):
    assert strict_route2_condition(m, P, K)
    H = (m + 1) // 2
    A = range(m - H + 1, m + 1)

    Qs = {}
    for a in A:
        assert K % a == 0
        Q = 1 + K // a
        Qs[a] = Q
        val = relative_identity(a, Q)
        assert val is not None and val.denominator == 1
        assert all(p > P for p in factorint(Q))

    items = list(Qs.items())
    from math import gcd
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            assert gcd(items[i][1], items[j][1]) == 1

    return Qs
```

Recommended finite experiments:

1. Run `search_route2(m, m+2, B)` for \(m=1,\dots,10\), both in strict and generalized mode.
2. For every known successful \((m,X)\), run `check_endpoint_digit_formula` on every prime divisor of the endpoint block.
3. Record, for each endpoint prime, the least \(s\) at which Lemma 2 supplies compensation. This tests whether a fixed bounded depth might replace the rigid one-step condition.
4. Search directly for simultaneous relative identities
   \[
   Q_a=1+K/a
   \]
   before checking full integrality, to determine empirically how sparse the Route-2 sufficient certificates are.

## Route Diagnosis

**Proved ledger**

- Negative \(p\)-power levels for \(p>m\) are exactly the first \(v_p(X-j)\) powers attached to one endpoint.
- The complete cofactor-digit formula in Lemma 2.
- One-step \(-1\pmod p\) self-compensation.
- Repeated-prime self-compensation via
  \[
  p^{2t}\mid X-j+p^t.
  \]
- A complete sufficient construction theorem combining small-prime sealing with endpoint self-compensation.
- Exact reduction of the sealed construction to simultaneous relative weak-primary-pseudoperfect identities.
- Pairwise coprimality of the resulting shifted factors.
- A quantitative lower bound on how many uncontrolled large prime factors each shifted factor must have.
- The Euclid-type extension mechanism and its synchronization failure.

**Plausible but unproved**

- A bounded-depth version of Lemma 2 may be flexible enough to occur simultaneously on all endpoints.
- There may be multiplicative closure operations more general than \(Q\mapsto Q(aQ+1)\) that synchronize several values of \(a\).
- Generalized prime-power components may be substantially more constructible than the strict squarefree version.

**Dead or presently blocked**

- The exact \(-1\pmod p\) condition is too rigid to describe known solutions such as \(X=210\).
- Sequential CRT remains circular because every increase in the sealing threshold creates many new, unknown endpoint prime divisors.
- Independent Euclid recursions do not preserve the common parameter \(K\).
- The broadened exact-digit problem appears to require a new theorem on simultaneous shifted factorization and \(p\)-adic digit conditions.

A fresh Route-2 attempt should focus on bounded-depth compensation trees from Lemma 2 rather than exact \(-1\) congruences. The most concrete target is to find a multiplicative operation on endpoint values that preserves all existing prime-chain balances while adjoining new prime factors with certified upper-half cofactor digits. Without such a closure operation, Route 2 collapses into the global shifted-correlation obstruction already identified in the brief.