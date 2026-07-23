STATUS: BLOCKED

## Result

Route 3 can rigorously accomplish its finite objectives: one can force the endpoint interval to be composite, seal every prescribed finite set of primes against valuation deficits, and even arrange that the primes used in the composite covering are themselves valuation-balanced. The obstruction is genuinely circular. Every arithmetic progression produced by finitely many CRT conditions contains infinitely many failures caused by a new, arbitrarily large prime dividing \(x=m+k\). Moreover, any sufficiently large solution must make every integer in \((x-m/2,x]\) \(\sqrt{2x-m}\)-smooth, and this smoothness is still not sufficient. Thus the route reduces to uncontrolled simultaneous factorization and \(p\)-adic conditions on several linear forms; I do not obtain a proof or disproof of Erdős Problem #389.

## Complete Argument

Write
\[
x=m+k>m,\qquad
R_m(k)=\frac{(2x-m)!\,m!}{x!^2}.
\]
For an integer \(q\ge2\), define
\[
e_q(m,x):=
\left\lfloor\frac{2x-m}{q}\right\rfloor
+\left\lfloor\frac mq\right\rfloor
-2\left\lfloor\frac xq\right\rfloor.
\]
Then for every prime \(p\),
\[
D_p(m,x):=v_p(R_m(k))=\sum_{a\ge1}e_{p^a}(m,x).
\]

Throughout \(m\ge1\); the case \(m=0\) is already solved by central binomial coefficients. Put
\[
J_m:=\{j\in\mathbb Z:0\le j<m/2\}
=\{0,1,\ldots,\lceil m/2\rceil-1\}.
\]

### 1. Exact residue description of every valuation level

**Lemma 1.** Let
\[
r=x\bmod q,\qquad s=m\bmod q,
\]
with \(0\le r,s<q\). Then
\[
e_q(m,x)=\left\lfloor\frac{2r-s}{q}\right\rfloor\in\{-1,0,1\}.
\]
In particular,
\[
e_q=-1\iff 2r<s,
\qquad
e_q=1\iff 2r\ge q+s.
\]
If \(q>m\), then
\[
e_q=-1\iff x\bmod q\in J_m.
\]

**Proof.** Write \(x=bq+r\) and \(m=aq+s\). Then
\[
2x-m=(2b-a)q+(2r-s),
\]
so
\[
\begin{aligned}
e_q(m,x)
&=2b-a+\left\lfloor\frac{2r-s}{q}\right\rfloor+a-2b\\
&=\left\lfloor\frac{2r-s}{q}\right\rfloor.
\end{aligned}
\]
Since \(-q<2r-s<2q\), this belongs to \(\{-1,0,1\}\). If \(q>m\), then \(s=m\), and \(e_q=-1\) precisely when \(2r<m\), equivalently \(r\in J_m\). ∎

Thus every negative level \(p^a>m\) means that a multiple of \(p^a\) lies among
\[
x,\ x-1,\ldots,x-\lceil m/2\rceil+1.
\]

---

### 2. A prime can be sealed by one congruence

**Lemma 2.** Let \(p\) be prime and let \(p^A>m\). If
\[
p^A\mid k=x-m,
\]
then
\[
D_p(m,x)\ge0.
\]

**Proof.** For every \(a\le A\), one has \(p^a\mid k\), hence
\[
x\equiv m\pmod{p^a}.
\]
Substitution in Lemma 1 gives \(e_{p^a}=0\).

Suppose \(a>A\) and \(e_{p^a}=-1\). Since \(p^a>m\), Lemma 1 gives
\[
x\bmod p^a=j
\]
for some \(j\in J_m\). Reducing modulo \(p^A\) gives
\[
m\equiv x\equiv j\pmod{p^A}.
\]
Both \(m\) and \(j\) lie in \([0,p^A)\), so \(m=j\), impossible because \(j<m/2\). Consequently every term with \(a>A\) is nonnegative, proving \(D_p\ge0\). ∎

Define
\[
Q_m:=\prod_{p\le m}p^{A_p},
\qquad
A_p:=\min\{a:p^a>m\}.
\]

**Corollary 3.** If \(Q_m\mid k\), then \(D_p(m,x)\ge0\) for every prime \(p\le m\).

Also, \(Q_m\) is divisible by every integer \(1\le d\le m\), because its \(p\)-adic exponent is strictly larger than \(\lfloor\log_p m\rfloor\).

This is stronger than merely controlling finitely many low prime powers: one congruence seals all higher powers of the same prime as well.

---

### 3. The standard composite covering can be carried out cleanly

Take
\[
k=tQ_m,\qquad x=m+tQ_m,\qquad t\ge1.
\]
For \(j\in J_m\), put \(d_j=m-j\). Since \(1\le d_j\le m\), we have \(d_j\mid Q_m\), and hence
\[
x-j=(m-j)+tQ_m
=d_j\left(1+t\frac{Q_m}{d_j}\right).
\]

For \(m\ge2\), \(d_j\ge2\), and the second factor exceeds \(1\). Therefore all integers
\[
x,\ x-1,\ldots,x-\lceil m/2\rceil+1
\]
are composite. Simultaneously, Corollary 3 seals all primes \(p\le m\).

Thus Route 3’s initial two goals—composite endpoint covering and complete control of small primes—are unconditionally achievable.

They do not suffice. For example, when \(m=3\),
\[
Q_3=4\cdot9=36.
\]
Taking \(t=1\) gives \(x=39\), whose relevant endpoint integers are \(39\) and \(38\), both composite. All primes \(p\le3\) are sealed. Nevertheless,
\[
13\mid39,\qquad 13^2>2\cdot39-3,
\]
and hence \(D_{13}(3,39)=-1\). Likewise \(19\mid38\) gives \(D_{19}(3,39)=-1\).

---

### 4. Exact support of the remaining obstructions

**Lemma 4.** Let \(p>m\). If \(D_p(m,x)<0\), then
\[
p\mid\prod_{j\in J_m}(x-j).
\]

**Proof.** If the sum \(\sum_a e_{p^a}\) is negative, at least one summand is \(-1\). Since every \(p^a>m\), Lemma 1 gives
\[
x\bmod p^a=j
\]
for some \(j\in J_m\). Hence \(p\mid x-j\). ∎

Consequently, after imposing \(Q_m\mid k\), all possible bad primes divide the fixed-length endpoint product
\[
E_m(x):=\prod_{j\in J_m}(x-j).
\]
This is a substantial localization, but the factors of \(E_m(x)\) change with \(x\).

---

### 5. A necessary simultaneous smoothness condition

**Lemma 5.** Suppose \(p>m\), \(p^2>2x-m\), and
\[
p\mid x-j
\]
for some \(j\in J_m\). Then
\[
D_p(m,x)=-1.
\]

**Proof.** Since \(p>m>j\), the residue of \(x\) modulo \(p\) is \(j\). Lemma 1 gives \(e_p=-1\). For \(a\ge2\),
\[
p^a\ge p^2>2x-m,
\]
so all corresponding Legendre terms vanish. Thus \(D_p=e_p=-1\). ∎

Let \(P(N)\) denote the largest prime factor of \(N>1\).

**Corollary 6.** If
\[
x>\frac{m^2+m}{2}
\]
and \(R_m(x-m)\) is integral, then
\[
P(x-j)\le\sqrt{2x-m}
\qquad\text{for every }j\in J_m.
\]

**Proof.** The displayed bound on \(x\) gives
\[
\sqrt{2x-m}>m.
\]
If some \(x-j\) had a prime factor \(p>\sqrt{2x-m}\), then \(p>m\), \(p^2>2x-m\), and Lemma 5 would give a valuation deficit. ∎

For the simple CRT family \(x=m+tQ_m\), this means that all the linear forms
\[
1+t\frac{Q_m}{m-j},
\qquad j\in J_m,
\]
must simultaneously avoid prime factors larger than roughly a constant times their square root. Ordinary CRT composite coverings only provide the fixed factor \(m-j\); they give no control over this large cofactor.

Even the smoothness condition is not sufficient. For \(m=3,x=16\), the endpoint integers are \(16\) and \(15\), and
\[
P(16)=2,\qquad P(15)=5
<\sqrt{29}.
\]
Nevertheless,
\[
e_2=e_4=e_8=e_{16}=-1,
\]
so
\[
D_2(3,16)=-4.
\]
Thus higher prime-power multiplicities and carry structure remain essential.

---

### 6. Every individual covering prime can be balanced

The problem is not a local incompatibility.

**Lemma 7.** Let \(p>m\), \(p\ge3\), and \(j\in J_m\). If
\[
x\equiv j+p(p-1)\pmod{p^2},
\]
then
\[
D_p(m,x)\ge0.
\]

**Proof.** Modulo \(p\), \(x\equiv j\), so \(e_p=-1\).

Modulo \(p^2\), let \(r=j+p(p-1)\). Then
\[
2r-m-p^2=p^2-2p+2j-m.
\]
Since \(m\le p-1\) and \(p\ge3\),
\[
p^2-2p+2j-m
\ge p^2-3p+1\ge1.
\]
Thus \(2r\ge p^2+m\), and Lemma 1 gives \(e_{p^2}=1\).

For \(a\ge3\), a negative contribution would imply
\[
x\bmod p^a=j'
\]
for some \(j'\in J_m\). Reducing modulo \(p^2\) would give
\[
j+p(p-1)\equiv j'\pmod{p^2}.
\]
Both sides are representatives in \([0,p^2)\), but the left side is at least \(p(p-1)>m\), whereas \(j'<m/2\). This is impossible. Therefore all higher contributions are nonnegative, so
\[
D_p\ge -1+1=0.
\]
∎

The exceptional pair \(m=1,p=2\) can similarly be balanced by
\[
x\equiv6\pmod8,
\]
for which
\[
e_2=-1,\qquad e_4=0,\qquad e_8=1,
\]
and no higher negative contribution is possible.

Hence one may choose distinct primes \(p_j>\max(m,2)\) and impose
\[
x\equiv j+p_j(p_j-1)\pmod{p_j^2}
\qquad(j\in J_m),
\]
together with
\[
x\equiv m\pmod{Q_m}.
\]
CRT gives an arithmetic progression of \(x\) for which:

1. every \(p\le m\) is sealed;
2. every endpoint \(x-j\) is divisible by its assigned \(p_j\);
3. every assigned \(p_j\) has nonnegative total valuation.

Thus even a valuation-balanced composite covering is possible. The residual cofactors introduce new primes.

---

### 7. More generally, every finite \(p\)-adic condition can be repaired

**Lemma 8.** Fix \(m\ge1\), a prime \(p\), and any initial congruence
\[
x\equiv r_0\pmod{p^{A_0}}.
\]
There exist \(B\ge A_0\) and a residue \(R\bmod p^B\), extending the initial congruence, such that
\[
D_p(m,x)\ge0
\]
for every \(x\equiv R\pmod{p^B}\).

**Proof.** First extend the residue arbitrarily to a modulus \(q=p^A>m\), and let \(r\in[0,q)\) denote the resulting residue. Let
\[
S=\sum_{a=1}^{A}e_{p^a}(m,r).
\]

Extend from modulus \(q\) to \(pq\) by replacing \(r\) with
\[
r'=r+(p-1)q.
\]

If \(p\ge3\), then
\[
2r'-m-pq
=2r+(p-2)q-m>0
\]
because \(q>m\). Hence the newly added contribution is \(+1\).

If \(p=2\), then the new contribution is \(+1\) whenever \(2r\ge m\). If \(2r<m\), it is \(0\), but then
\[
r'=r+q>m,
\]
so all subsequent extensions of the same form contribute \(+1\).

Repeat this extension until the partial sum is nonnegative. After at most one preliminary zero contribution, each step adds \(1\), so the process terminates. At termination the residue \(R\) modulo \(p^B\) is not in \(J_m\).

For a higher power \(p^a\), \(a>B\), a negative contribution would imply
\[
x\bmod p^a=j\in J_m.
\]
Reduction modulo \(p^B\) would then give \(R\equiv j\pmod{p^B}\), impossible because \(R\notin J_m\). Therefore all contributions above \(p^B\) are nonnegative. The constructed partial sum is already nonnegative, proving the claim. ∎

By CRT, any finite collection of primes can therefore be made simultaneously safe. There is no finite local obstruction.

---

### 8. The decisive circular obstruction: every CRT progression contains infinitely many failures

**Theorem 9.** Fix \(m\ge1\). Every arithmetic progression of possible \(x\)-values contains infinitely many \(x\) for which \(R_m(x-m)\) is nonintegral.

**Proof.** Let the progression be
\[
x\equiv a\pmod N,
\]
where \(0\le a<N\). Put
\[
d=\gcd(a,N),\qquad a=db,\qquad N=dA.
\]
Then \(\gcd(A,b)=1\). If \(a=0\), then \(d=N,A=1,b=0\), which causes no difficulty.

Every member has the form
\[
x=a+Nt=d(b+At).
\]
By Dirichlet’s theorem on primes in arithmetic progressions, there are infinitely many \(t\) for which
\[
q=b+At
\]
is prime. For \(A=1\), this is simply the infinitude of primes. For all sufficiently large such \(q\),
\[
q>m,\qquad q^2>2dq-m=2x-m.
\]
Since \(q\mid x\), Lemma 5 with \(j=0\in J_m\) gives
\[
D_q(m,x)=-1.
\]
Thus infinitely many members of the progression fail. ∎

In particular, every arithmetic progression arising from finitely many repaired CRT conditions contains infinitely many new-prime failures. This does **not** prove that the progression contains no successful member; it proves that finite congruence control cannot make the uncontrolled primes automatically harmless.

For the elementary family \(x=m+tQ_m\), the same argument is especially explicit. Since \(m\mid Q_m\), write \(A=Q_m/m\). Whenever
\[
q=1+tA
\]
is a sufficiently large prime,
\[
x=m+tQ_m=mq,
\]
and \(q\) gives \(D_q=-1\). Dirichlet supplies infinitely many such \(t\).

---

### 9. Why this blocks Route 3

Finite-prime control is complete: Lemmas 2, 7, and 8 show that every finite set of local conditions can be repaired and combined by CRT. But after those conditions are imposed, the resulting arithmetic progression necessarily contains arbitrarily large representatives with a fresh obstructing prime. Adding that prime to the CRT modulus produces another progression, to which Theorem 9 applies again.

To finish affirmatively, one would need a noncongruential selection theorem guaranteeing a representative for which all prime divisors of the endpoint numbers are simultaneously:

1. at most \(\sqrt{2x-m}\);
2. arranged across their higher powers so that every negative \(e_{p^a}\) is canceled.

For the natural family \(x=m+tQ_m\), this already demands simultaneous square-root smoothness of
\[
1+t\frac{Q_m}{m-j},
\qquad j\in J_m,
\]
and smoothness alone is insufficient, as \(m=3,x=16\) demonstrates. I have no theorem establishing the required simultaneous factorization and digit behavior, nor a universal obstruction proving it impossible.

As a side observation, Route 2 cannot replace Route 3: for every \(m>0\) and \(x>m\),
\[
e_x(m,x)
=
\left\lfloor\frac{2x-m}{x}\right\rfloor
+\left\lfloor\frac mx\right\rfloor
-2
=1+0-2=-1.
\]
Thus the Gaussian-binomial strengthening fails for every possible \(k\) when \(m>0\).

## Self-Audit

1. **Theorem 9 uses Dirichlet’s theorem.** This is the only substantial external input. Its hypotheses are exactly verified by \(\gcd(A,b)=1\), and the conclusion needed is the standard unconditional infinitude of primes in the progression \(b\bmod A\).

2. **The local repair lemma is strong but only finite-prime control.** Its terminal-residue argument is exact: a higher negative level would reduce to an endpoint residue modulo the sealing power. It gives no control over new primes, and I have not used it as though it did.

3. **The route diagnosis is not an impossibility theorem for all CRT-inspired constructions.** Theorem 9 only says no fixed finite congruence class is eventually composed of solutions; an individual successful representative could still occur. Therefore the status is BLOCKED rather than SOLVED-DISPROOF.

## Computations To Verify

The following Python/SymPy code checks valuations, the sealing construction, the smoothness obstruction, and balanced CRT classes.

```python
from math import gcd, isqrt
from sympy import primerange, factorint, isprime, nextprime
from sympy.ntheory.modular import crt

def level(m, x, q):
    return (2*x - m)//q + m//q - 2*(x//q)

def vp_ratio(m, x, p):
    """v_p((2x-m)! m! / x!^2), where k=x-m."""
    total = 0
    q = p
    while q <= 2*x - m:
        total += level(m, x, q)
        q *= p
    return total

def all_valuations(m, x):
    return {
        p: vp_ratio(m, x, p)
        for p in primerange(2, 2*x - m + 1)
    }

def is_solution_x(m, x):
    assert x > m
    return all(v >= 0 for v in all_valuations(m, x).values())

def endpoint_indices(m):
    return range((m + 1)//2)  # 0 <= j < m/2

def Qm(m):
    Q = 1
    for p in primerange(2, m + 1):
        q = p
        while q <= m:
            q *= p
        Q *= q
    return Q

def endpoint_obstructions(m, x):
    """Large one-level obstruction primes."""
    out = []
    N = 2*x - m
    for j in endpoint_indices(m):
        y = x - j
        for p in factorint(y):
            if p > m and p*p > N:
                out.append((j, y, p))
    return out

def smoothness_condition(m, x):
    """Necessary for a solution when x > (m^2+m)/2."""
    bound2 = 2*x - m
    for j in endpoint_indices(m):
        y = x - j
        P = max(factorint(y))
        if P*P > bound2:
            return False
    return True

# Exact examples from the argument.
assert Qm(2) == 4
assert is_solution_x(2, 6)       # m=2, k=4

assert Qm(3) == 36
assert vp_ratio(3, 39, 13) == -1
assert vp_ratio(3, 39, 19) == -1

assert smoothness_condition(3, 16)
assert vp_ratio(3, 16, 2) == -4
assert not is_solution_x(3, 16)

def verify_sealing(max_m=30, multiplier_bound=30):
    for m in range(1, max_m + 1):
        for p in primerange(2, m + 1):
            q = p
            while q <= m:
                q *= p
            for t in range(1, multiplier_bound + 1):
                k = t*q
                x = m + k
                assert vp_ratio(m, x, p) >= 0

def balanced_residue(m, j, p):
    """
    For p>m, p>=3:
    x == j+p(p-1) mod p^2 seals p while p divides x-j.
    """
    assert p > m and p >= 3 and 0 <= 2*j < m
    r = j + p*(p-1)
    assert level(m, r, p) == -1
    assert level(m, r, p*p) == 1
    return r, p*p

def balanced_cover_class(m):
    """
    Construct one CRT class sealing all p<=m and assigning one
    balanced covering prime to each endpoint x-j.
    """
    mods, residues = [], []

    Q = Qm(m)
    if Q > 1:
        mods.append(Q)
        residues.append(m % Q)

    p = nextprime(max(m, 2))
    assigned = []
    for j in endpoint_indices(m):
        r, mod = balanced_residue(m, j, p)
        mods.append(mod)
        residues.append(r)
        assigned.append((j, p))
        p = nextprime(p)

    a, N = crt(mods, residues)
    return int(a), int(N), assigned

def test_balanced_cover(m, number_of_representatives=50):
    a, N, assigned = balanced_cover_class(m)

    # Move to a positive representative x>m.
    if a <= m:
        a += ((m - a)//N + 1)*N

    for t in range(number_of_representatives):
        x = a + t*N

        # Small primes are sealed.
        for p in primerange(2, m + 1):
            assert vp_ratio(m, x, p) >= 0

        # Assigned covering primes divide the endpoint and are safe.
        for j, p in assigned:
            assert (x - j) % p == 0
            assert vp_ratio(m, x, p) >= 0

        vals = all_valuations(m, x)
        bad = [(p, v) for p, v in vals.items() if v < 0]
        print("m,x =", m, x, "bad primes =", bad)

def local_repair(m, p, r0, A0=1):
    """
    Construct the residue class in Lemma 8.
    Initial condition: x == r0 mod p^A0.
    Returns (R, p^B, partial_sum).
    """
    q = p**A0
    r = r0 % q
    B = A0

    # Extend with zero higher digits until q>m.
    while q <= m:
        q *= p
        B += 1

    S = 0
    qa = p
    for _ in range(1, B + 1):
        S += level(m, r, qa)
        qa *= p

    # r in J_m exactly when 2*r < m, because q>m.
    while S < 0 or 2*r < m:
        old_q = q
        r += (p - 1)*old_q
        q *= p
        B += 1
        S += level(m, r, q)

    assert S >= 0
    assert 2*r >= m
    return r, q, S

def test_progression_failures_for_seed(m, t_bound=100000):
    """
    Search for the explicit Dirichlet-type bad subsequence
    x=m+t Q_m, q=1+t(Q_m/m) prime.
    This is a finite illustration, not a proof of infinitude.
    """
    Q = Qm(m)
    A = Q // m
    found = []
    for t in range(1, t_bound + 1):
        q = 1 + t*A
        if isprime(q) and q > 2*m:
            x = m + t*Q
            assert x == m*q
            assert q*q > 2*x - m
            assert vp_ratio(m, x, q) == -1
            found.append((t, x, q))
            if len(found) >= 20:
                break
    return found
```

Particularly useful experiments are:

1. Run `test_balanced_cover(m)` for \(3\le m\le20\) and classify the new bad primes.
2. Search the family \(x=m+tQ_m\) for values where all endpoint linear forms are square-root smooth, then test whether small-prime-power deficits remain.
3. Implement the iterative strategy “factor endpoints, repair every bad prime, recompute the least CRT representative” and record whether the number and size of fresh bad primes stabilizes or grows.

## Route Diagnosis

**Proved lemmas**

- Every level \(e_q\) is exactly \(-1,0,\) or \(1\), with negative high levels corresponding to endpoint residues.
- A congruence \(p^A\mid k\) with \(p^A>m\) seals the prime \(p\) at all powers.
- The entire endpoint interval can be made composite while all primes \(p\le m\) are sealed.
- Every remaining bad prime divides one of the endpoint integers.
- Every sufficiently large solution requires all endpoint integers to be \(\sqrt{2x-m}\)-smooth.
- Any prescribed finite collection of primes can be locally repaired and combined by CRT.
- Every fixed CRT progression nevertheless contains infinitely many failures from fresh large primes.
- The Gaussian-binomial strengthening is impossible for every \(m>0\), because \(e_x=-1\).

**Plausible but unproved**

- An iterative CRT repair process might terminate for every \(m\).
- There might exist representatives where all endpoint linear forms are simultaneously square-root smooth and have favorable higher \(p\)-adic digits.
- A sieve or algebraic construction might supply the required specially factored endpoint block.

**Dead ends**

- Merely forcing the endpoint interval to be composite: residual cofactors can contain primes \(>\sqrt{2x-m}\).
- Sealing any fixed finite set of primes and declaring larger primes harmless: Theorem 9 gives infinitely many counterexamples in every resulting progression.
- Replacing smoothness for the valuation conditions: \(m=3,x=16\) is smooth at every endpoint but has \(D_2=-4\).
- Gaussian/cyclotomic positivity: always fails at \(d=x\) for \(m>0\).

A fresh attempt should focus on a genuinely noncongruential construction of simultaneous balanced factorizations of the endpoint integers, or on an analytic sieve capable of handling both smoothness and the higher-power residue conditions. Finite CRT control by itself cannot close the argument.