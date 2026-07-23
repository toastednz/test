STATUS: BLOCKED

## Result

Route 2 yields an exact \(2\)-adic transition theorem. After separating the power of \(2\), every direct solution corresponds to a periodic orbit of an explicit map on odd integers with total \(2\)-adic weight \(1\). Such a cycle is either \(1\leftrightarrow3\), or has exactly one valuation jump, occurring at a prime power \(p^t\) with \(p\equiv7\pmod8\); all other steps form a strictly increasing chain under \(u\mapsto u+\phi(u)/2\). This recovers Cambie’s prime-power reduction and proves that period-two solutions with \(t\ge2\) are impossible. However, the remaining increasing-chain problem is an inverse/shifted-totient problem not resolved by \(2\)-adic information. More importantly, the proposed eventual classification is false: every \(n=2^a11\), \(a\ge1\), is an omitted eventual solution with \(r=2\); for example \(22\to32\to48\to64\). I do not obtain an exhaustive replacement classification.

## Complete Argument

### 1. The exact odd-core transition

For an even integer \(x\ge4\), write
\[
x=2^a u,\qquad a=v_2(x)\ge1,\qquad u\ \text{odd}.
\]

Define a map \(H\) and an integer weight \(c\) on odd positive integers as follows.

For \(u=1\), set
\[
H(1)=3,\qquad c(1)=-1.
\]

For odd \(u>1\), define
\[
J(u):=u+\frac{\phi(u)}2,
\]
which is an integer because \(\phi(u)\) is even, and put
\[
c(u):=v_2(J(u)),\qquad H(u):=\frac{J(u)}{2^{c(u)}}.
\]

Thus \(H(u)\) is the odd part of \(J(u)\).

#### Lemma 1: Odd-core recurrence

If \(x=2^a u\ge4\) is even, then
\[
F(x)=
\begin{cases}
2^{a-1}H(1),&u=1,\\[2mm]
2^{a+c(u)}H(u),&u>1.
\end{cases}
\]

Equivalently, the odd part evolves by \(u\mapsto H(u)\), while \(v_2(x)\) changes by \(c(u)\).

#### Proof

If \(u=1\), then
\[
F(2^a)=2^a+\phi(2^a)
      =2^a+2^{a-1}
      =3\cdot2^{a-1}.
\]

If \(u>1\), multiplicativity gives
\[
\phi(2^a u)=2^{a-1}\phi(u),
\]
so
\[
F(2^a u)
=2^a u+2^{a-1}\phi(u)
=2^a\left(u+\frac{\phi(u)}2\right)
=2^{a+c(u)}H(u).
\]
∎

There is no danger from the exceptional transition \(2\mapsto3\): an orbit beginning at an even \(x\ge4\) remains even and strictly larger than \(2\). Thus whenever its odd core is \(1\), its \(2\)-adic exponent is at least \(2\).

---

### 2. Classification of the possible valuation changes

For odd \(u>1\), write
\[
u=\prod_{j=1}^s p_j^{e_j}.
\]
Then
\[
v_2(\phi(u))=\sum_{j=1}^s v_2(p_j-1).
\]

#### Lemma 2: Valuation transition dichotomy

For odd \(u>1\):

1. If \(u\) is not a prime power \(p^t\) with \(p\equiv3\pmod4\), then
   \[
   c(u)=0,\qquad H(u)=u+\frac{\phi(u)}2>u.
   \]

2. If \(u=p^t\) with \(p\equiv3\pmod4\), then
   \[
   J(u)=p^{t-1}\frac{3p-1}{2},
   \]
   and
   \[
   c(u)=v_2(3p-1)-1\ge1.
   \]

3. In the second case,
   \[
   c(u)=1\quad\Longleftrightarrow\quad p\equiv7\pmod8.
   \]

#### Proof

The number \(J(u)=u+\phi(u)/2\) is even exactly when \(\phi(u)/2\) is odd, because \(u\) is odd. Hence \(c(u)>0\) exactly when
\[
v_2(\phi(u))=1.
\]

Since every \(v_2(p_j-1)\ge1\), their sum is \(1\) exactly when there is one distinct prime divisor \(p\) and \(v_2(p-1)=1\). Thus
\[
u=p^t,\qquad p\equiv3\pmod4.
\]

For such \(u\),
\[
J(u)
=p^t+\frac{p^{t-1}(p-1)}2
=p^{t-1}\frac{3p-1}{2}.
\]

Now \(p\equiv3\) or \(7\pmod8\). If \(p\equiv7\pmod8\), then
\[
3p-1\equiv20\equiv4\pmod8,
\]
so \(v_2(3p-1)=2\) and \(c(u)=1\). If \(p\equiv3\pmod8\), then \(3p-1\) is divisible by \(8\), so \(c(u)\ge2\). ∎

Thus, apart from pure powers of \(2\), \(v_2\) never decreases. It remains constant at ordinary odd cores and jumps upward at prime powers \(p^t\) with \(p\equiv3\pmod4\).

---

### 3. Direct seeds are weight-one cycles

Suppose
\[
F^r(x)=2x
\]
for an even \(x\ge4\). Write
\[
F^i(x)=2^{a_i}u_i
\]
with \(u_i\) odd. Lemma 1 gives
\[
u_{i+1}=H(u_i),\qquad a_{i+1}=a_i+c(u_i).
\]

The endpoint equality implies
\[
u_r=u_0,\qquad a_r=a_0+1.
\]
Therefore
\[
H^r(u_0)=u_0,\qquad
\sum_{i=0}^{r-1}c(u_i)=1. \tag{18}
\]

Let \(d\) be the minimal period of \(u_0\) under \(H\), and let
\[
C=\sum_{i=0}^{d-1}c(H^i(u_0)).
\]
Since \(d\mid r\), equation (18) gives
\[
\frac rd\,C=1.
\]
Both factors are integers and \(r/d>0\). Consequently
\[
r=d,\qquad C=1. \tag{19}
\]

This proves:

#### Theorem 3: Exact cycle criterion

An even \(x\ge4\) satisfies \(F^r(x)=2x\) if and only if its odd core lies on an \(H\)-cycle of minimal period \(r\) whose total weight is \(1\), with the harmless restriction that odd core \(1\) must carry \(2\)-adic exponent at least \(2\).

In particular, the lag is the minimal period of the odd-core cycle.

The same theorem gives an exact eventual criterion. An even starting value \(n\ge4\) satisfies the eventual relation with lag \(r\) if and only if the \(H\)-orbit of its odd part eventually enters a weight-one cycle of minimal period \(r\).

Indeed, the forward implication follows by applying the direct criterion to \(F^K(n)\). Conversely, if an orbit reaches such a cycle, the corresponding even orbit point \(x\) satisfies \(F^r(x)=2x\). The identity
\[
F(2m)=2F(m)\qquad(m\ \text{even})
\]
then propagates the equality forever.

This criterion is exact but is a dynamical reduction, not an explicit arithmetic classification.

---

### 4. Structure of every weight-one cycle

#### The cycle containing \(1\)

Direct calculation gives
\[
H(1)=3,\quad c(1)=-1,
\]
and
\[
J(3)=3+\frac{\phi(3)}2=4,
\quad H(3)=1,\quad c(3)=2.
\]
Hence
\[
1\longleftrightarrow3
\]
is a cycle of total weight
\[
-1+2=1.
\]

Any cycle containing \(1\) is this cycle, because the forward orbit of \(1\) closes after these two steps.

It generates the direct seeds whose odd core is \(1\) or \(3\), namely pure powers of \(2\) at least \(4\) and the numbers \(3\cdot2^a\), \(a\ge1\).

#### Cycles not containing \(1\)

On such a cycle every weight is nonnegative. Since the total weight is \(1\), exactly one node has weight \(1\), and every other node has weight \(0\).

By Lemma 2, the unique positive-weight node is
\[
P=p^t,\qquad p\equiv7\pmod8,
\]
and its successor is
\[
M=H(P)
  =p^{t-1}\frac{3p-1}{4}. \tag{20}
\]

All remaining transitions have weight \(0\), so they are given by
\[
u\longmapsto J(u)=u+\frac{\phi(u)}2,
\]
and are strictly increasing.

Consequently every non-\(\{1,3\}\) weight-one cycle has the form
\[
P\longmapsto m_0\longmapsto m_1\longmapsto
\cdots\longmapsto m_{r-2}\longmapsto P, \tag{21}
\]
where
\[
P=p^t,\qquad p\equiv7\pmod8,
\]
\[
m_0=p^{t-1}\frac{3p-1}{4},
\]
and
\[
m_{j+1}=m_j+\frac{\phi(m_j)}2
\]
at every subsequent step, with
\[
m_0<m_1<\cdots<m_{r-2}<P. \tag{22}
\]

Conversely, any chain satisfying (20)–(22) produces a weight-one cycle and hence direct seeds with lag \(r\).

Telescoping the chain gives the necessary exact identity
\[
\sum_{j=0}^{r-2}\phi(m_j)
=2(P-M)
=p^{t-1}\frac{p+1}{2}. \tag{23}
\]

This is the precise point at which the purely \(2\)-adic argument stops: all intermediate steps have unchanged \(2\)-adic valuation.

---

### 5. Complete analysis of period two up to one shifted-totient equation

Suppose the nontrivial cycle has period \(2\). Put
\[
A=\frac{3p-1}{4},
\qquad M=p^{t-1}A.
\]
Then period two requires
\[
J(M)=p^t. \tag{24}
\]

Since \(\gcd(A,p)=1\), if \(t\ge2\), then
\[
\phi(M)=p^{t-2}(p-1)\phi(A).
\]
Substituting into (24) gives
\[
p^{t-1}A+\frac{p^{t-2}(p-1)\phi(A)}2=p^t.
\]
After division by \(p^{t-2}\) and multiplication by \(2\),
\[
2pA+(p-1)\phi(A)=2p^2.
\]
Using \(A=(3p-1)/4\),
\[
(p-1)\phi(A)=\frac{p(p+1)}2,
\]
so
\[
\phi(A)=\frac{p(p+1)}{2(p-1)}. \tag{25}
\]

Write \(p=2h+1\). Integrality of the right side requires
\[
2h\mid (2h+1)(h+1).
\]
Because \(\gcd(2h,2h+1)=1\), this requires
\[
2h\mid h+1,
\]
which is impossible for \(h>1\). Here \(p\equiv7\pmod8\), so \(p\ge7\) and \(h\ge3\).

Therefore:

#### Proposition 4

A nontrivial period-two cycle necessarily has \(t=1\).

For \(t=1\), equation (24) becomes
\[
A+\frac{\phi(A)}2=p,
\]
or
\[
\phi(A)=\frac{p+1}{2}. \tag{26}
\]
Writing
\[
p=8m+7,\qquad A=6m+5,
\]
this becomes exactly
\[
\phi(6m+5)=4m+4. \tag{27}
\]

The known solutions are
\[
p=7,\quad A=5,
\]
and
\[
p=47,\quad A=35,
\]
giving the cycles
\[
5\longleftrightarrow7,\qquad
35\longleftrightarrow47.
\]

Thus Route 2 completely rules out \(t\ge2\) for \(r=2\), but the \(t=1\) classification is precisely the difficult shifted-totient equation from the brief.

---

### 6. A further restriction on the last neutral step

The last node \(m=m_{r-2}\) in (21) satisfies
\[
m+\frac{\phi(m)}2=p^t. \tag{28}
\]

Let \(R=\operatorname{rad}(m)\), the product of the distinct primes dividing \(m\). Since
\[
\phi(m)=\frac{m}{R}\phi(R),
\]
equation (28) factors as
\[
\frac{m}{R}\left(R+\frac{\phi(R)}2\right)=p^t. \tag{29}
\]

Both factors are positive integers. Therefore each is a power of \(p\):
\[
\frac{m}{R}=p^\alpha,\qquad
R+\frac{\phi(R)}2=p^{t-\alpha} \tag{30}
\]
for some \(0\le\alpha\le t\).

In particular, every prime \(q\ne p\) occurs in \(m\) to exponent exactly \(1\). Thus the penultimate node is squarefree away from \(p\).

If \(p^s\parallel m\) with \(s\ge1\), writing \(m=p^s v\) and reducing the doubled version of (28) modulo \(p\) also gives
\[
p\mid\phi(v).
\]
Since \(\gcd(v,p)=1\), some prime divisor \(q\mid v\) must satisfy
\[
q\equiv1\pmod p.
\]
As \(p,q\) are odd, this forces
\[
q\ge2p+1.
\]

These restrictions are substantial, but equation (30) remains another inverse/shifted-totient problem and does not exclude long chains.

---

### 7. Cambie’s proposed eventual classification is false

The backward-orbit issue is not merely technical. There are elementary off-list predecessors of known direct seeds.

For every \(a\ge1\), let
\[
n=2^a\cdot11.
\]
Then
\[
\phi(n)=2^{a-1}\phi(11)=10\cdot2^{a-1}=5\cdot2^a,
\]
so
\[
F(n)=16\cdot2^a=2^{a+4}. \tag{31}
\]

Every power of \(2\) at least \(4\) is a direct period-two seed. Indeed, for \(s\ge2\),
\[
F(2^s)=3\cdot2^{s-1},
\]
and
\[
\phi(3\cdot2^{s-1})=2^{s-1},
\]
hence
\[
F^2(2^s)=4\cdot2^{s-1}=2^{s+1}=2\cdot2^s.
\]

Therefore every \(2^a11\) satisfies
\[
F^{k+2}(2^a11)=2F^k(2^a11)\qquad(k\ge1).
\]
Its odd part is \(11\), which is not in
\[
\{1,3,5,7,35,47\}.
\]
Thus none of these starting values belongs to the proposed list.

The smallest explicit certificate in this family is
\[
22\longmapsto32\longmapsto48\longmapsto64.
\]
The totients are verified by
\[
22=2\cdot11,\qquad \phi(22)=10,
\]
\[
32=2^5,\qquad \phi(32)=16,
\]
\[
48=2^4\cdot3,\qquad \phi(48)=2^3(3-1)=16.
\]
Thus
\[
F^3(22)=64=2F(22),
\]
and propagation gives
\[
F^{k+2}(22)=2F^k(22)\qquad(k\ge1).
\]

This rigorously refutes the conjectural classification under the stated eventual interpretation, but it does not classify all eventual starting values.

## Self-Audit

1. **Special handling of odd core \(1\).**  
   The recurrence has weight \(-1\) at \(u=1\), unlike all other cores. A hidden visit to \(2\) would invalidate continued even-orbit reasoning. It cannot occur here: an even orbit beginning at \(n\ge4\) is strictly increasing and remains even, so a pure-power orbit point always has exponent at least \(2\).

2. **The passage from \(F^r(x)=2x\) to minimal \(H\)-period \(r\).**  
   This depends on the cocycle sum being integral and repeating over the minimal odd-core period. Both are exact: if the minimal period is \(d\mid r\), the total exponent change is \((r/d)C=1\), forcing \(r/d=C=1\).

3. **Propagation of the \(22\) counterexample to all later indices.**  
   The identity \(F(2m)=2F(m)\) requires \(m\) to be even. Every iterate of \(32\) is even and at least \(4\), so the identity applies at every propagation step. The certificate therefore proves the full eventual relation, not only one isolated equality.

## Computations To Verify

```python
from math import isqrt

def phi(n):
    result = n
    m = n
    p = 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            result -= result // p
        p += 1 if p == 2 else 2
    if m > 1:
        result -= result // m
    return result

def F(n):
    return n + phi(n)

def odd_part(n):
    while n % 2 == 0:
        n //= 2
    return n

def odd_step(u):
    """Returns H(u), c(u)."""
    if u == 1:
        return 3, -1
    z = u + phi(u) // 2
    c = 0
    while z % 2 == 0:
        z //= 2
        c += 1
    return z, c

# Exact counterexample certificate
assert F(22) == 32
assert F(32) == 48
assert F(48) == 64
assert F(F(32)) == 64 == 2 * 32

# Infinite omitted family
for a in range(1, 30):
    n = (2**a) * 11
    x = F(n)
    assert x == 2**(a + 4)
    assert F(F(x)) == 2 * x

# Exhaustive direct-seed search up to B
def direct_seeds(B):
    hits = []
    for x in range(4, B + 1, 2):
        y = x
        r = 0
        while y < 2 * x:
            y = F(y)
            r += 1
            if y == 2 * x:
                hits.append((x, r))
                break
    return hits

# Verify the odd-core cycle/cocycle theorem on all bounded hits
def verify_hits(B):
    for x, r in direct_seeds(B):
        u = odd_part(x)
        total = 0
        v = u
        for _ in range(r):
            v, c = odd_step(v)
            total += c
        assert v == u
        assert total == 1

# Search prime-power reset chains
def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True

def reset_chains(P_bound):
    hits = []
    for p in range(7, P_bound + 1, 8):
        if not is_prime(p):
            continue
        P = p
        t = 1
        while P <= P_bound:
            m = (p**(t - 1)) * (3*p - 1) // 4
            u = m
            period = 1  # edge P -> m

            while u < P:
                v, c = odd_step(u)
                if c != 0:
                    break
                u = v
                period += 1

            if u == P:
                hits.append((p, t, period))
            t += 1
            P *= p
    return hits

# Search the period-two exceptional equation
def exceptional_parameters(M):
    hits = []
    for m in range(M + 1):
        p = 8*m + 7
        u = 6*m + 5
        if is_prime(p) and phi(u) == 4*m + 4:
            hits.append((m, p, u))
    return hits

# Complete one-step preimages of a target z
def preimages(z):
    return [y for y in range(1, z) if F(y) == z]

assert 22 in preimages(32)

# A genuine long zero-weight stretch, showing that local
# 2-adic constancy does not force period two.
neutral_run = [37, 55, 75, 95, 131]
for a, b in zip(neutral_run, neutral_run[1:]):
    v, c = odd_step(a)
    assert c == 0 and v == b
```

Recommended runs:

1. `verify_hits(10**6)` to test the cycle/cocycle theorem against every bounded direct seed.
2. `reset_chains(10**8)` to search for direct seeds with \(r\ge3\).
3. `exceptional_parameters(10**7)` to search the period-two shifted-totient branch.
4. Build complete preimage trees of \(2^a\), \(3\cdot2^a\), \(5\cdot2^a\), \(7\cdot2^a\), \(35\cdot2^a\), and \(47\cdot2^a\); this will enumerate many further transient solutions omitted from the proposed list.

## Route Diagnosis

### Proved ledger

- Exact odd-core map \(H\) and integer valuation cocycle \(c\).
- Direct seeds are precisely weight-one periodic \(H\)-orbits.
- The lag equals the minimal odd-core period.
- Every weight-one cycle is either \(1\leftrightarrow3\), or has one reset at \(p^t\), \(p\equiv7\pmod8\), followed by a strictly increasing neutral chain.
- The prime-power reduction \(F^r(2p^t)=4p^t\) follows exactly.
- Period two with \(t\ge2\) is impossible.
- Period two with \(t=1\) reduces to
  \[
  \phi(6m+5)=4m+4,\qquad 8m+7\ \text{prime}.
  \]
- The last neutral predecessor of \(p^t\) is squarefree away from \(p\).
- Cambie’s stated eventual classification is false; \(2^a11\) gives an infinite omitted family.

### Plausible but unproved

- That the only nontrivial weight-one cycles are \(5\leftrightarrow7\) and \(35\leftrightarrow47\).
- That there are no longer reset chains with \(r\ge3\).
- Any manageable explicit classification of all backward basins of the known cycles.

### Dead ends

1. **Purely \(2\)-adic forcing of \(r=2\).**  
   The valuation data force a unique reset but place no bound on the number of neutral steps. Actual stretches such as
   \[
   37\to55\to75\to95\to131
   \]
   show that several consecutive zero-weight transitions occur naturally.

2. **Uniform lower bounds for \(\phi(u)/u\).**  
   Such bounds are too weak to force one neutral step: the ratio can be arbitrarily small as the prime support grows.

3. **Simple backward rigidity.**  
   It is explicitly false. The collision
   \[
   F(22)=32
   \]
   puts an off-family value directly onto a known solution ray, and scaling gives infinitely many such predecessors.

### Precise block

Route 2 reduces every hypothetical \(r\ge3\) seed to the existence of an increasing chain
\[
p^{t-1}\frac{3p-1}{4}
\ \xrightarrow{\,u\mapsto u+\phi(u)/2\,}\
\cdots
\ \xrightarrow{}\ p^t,
\qquad p\equiv7\pmod8.
\]
All steps in the interior have identical \(2\)-adic valuation, so no further \(2\)-adic information distinguishes a one-step return from a long return. The terminal equation already contains an inverse/shifted-totient problem of comparable difficulty.

Moreover, even a complete direct-cycle classification would not solve the stated eventual problem: one must classify the full backward basins, and the proposed backward rigidity is refuted by \(22\).

A fresh attempt should therefore abandon the original conjectural target, retain the odd-core/cocycle reduction, and pursue two separate problems:

1. classify all weight-one \(H\)-cycles, probably through prime-support propagation in the neutral chain;
2. classify their complete backward basins under \(H\), normalized by powers of \(2\).

Aggressive searches for longer reset chains and off-cycle predecessors are warranted before formulating any replacement finite classification.