STATUS: BLOCKED

## Result

Route 1 gives an exact primitive-core reduction, but it terminates at the unresolved Diophantine problem anticipated in the brief. I prove that every non-pure primitive direct seed belongs to an odd cycle modulo doubling determined by a prime \(P\equiv7\pmod 8\) and an exponent \(a\ge1\). More precisely, it is equivalent to an all-odd chain from \(P^{a-1}(3P-1)/4\) to \(P^a\) under \(u\mapsto u+\phi(u)/2\). For lag \(2\), this forces \(a=1\) and reduces exactly to \(\phi(A)=2(A+1)/3\), with \(P=(4A+1)/3\) prime. I additionally prove that such \(A\) is squarefree and that if it has at most three prime factors, then \(A\in\{5,35,1295\}\), with \(1295\) excluded because its associated \(P=1727\) is composite. However, the original eventual-start conjecture is already false: \(18\mapsto24\), and \(24\) is a direct lag-\(2\) seed, so \((18,2)\) satisfies the eventual relation although \(18\) is not in the proposed list. In fact this gives the infinite off-list family \(18\cdot2^j\), \(j\ge0\). A complete classification remains blocked both by the primitive-chain equation and by the backward preimage trees.

## Complete Argument

### 1. A normalized map that removes all powers-of-two symmetry

For \(y\ge2\), define
\[
T(y):=\frac{F(2y)}2
      =y+\frac{\phi(2y)}2.
\]
Since \(2y\ge4\), the quantity \(\phi(2y)\) is even. Explicitly,
\[
T(y)=
\begin{cases}
y+\dfrac{\phi(y)}2,&y\text{ odd},\\[2mm]
y+\phi(y)=F(y),&y\text{ even}.
\end{cases} \tag{18}
\]

For every \(y\ge2\),
\[
T(2y)=2T(y). \tag{19}
\]
Indeed,
\[
T(2y)=\frac{F(4y)}2
     =\frac{2F(2y)}2
     =F(2y)
     =2T(y),
\]
where \(F(4y)=2F(2y)\) is valid because \(2y\) is even.

Also, by induction,
\[
F^j(2y)=2T^j(y)\qquad(j\ge0). \tag{20}
\]
Consequently,
\[
F^r(2y)=4y
\quad\Longleftrightarrow\quad
T^r(y)=2y. \tag{21}
\]

If \(y=2^e q\), where \(q\ge3\) is odd, then repeated use of (19) gives
\[
T^j(y)=2^eT^j(q).
\]
Thus
\[
T^r(y)=2y
\quad\Longleftrightarrow\quad
T^r(q)=2q. \tag{22}
\]

Therefore every non-pure direct seed reduces uniquely to a primitive seed \(2q\) with \(q\ge3\) odd. Pure powers reduce to the representative \(4\).

---

### 2. Parity transitions of \(T\)

Let \(u>1\) be odd. Then
\[
T(u)=u+\frac{\phi(u)}2.
\]
Since \(u\) is odd, \(T(u)\) is even exactly when \(\phi(u)/2\) is odd, equivalently when
\[
v_2(\phi(u))=1. \tag{23}
\]

Writing
\[
u=\prod_{i=1}^s p_i^{a_i},
\]
we have
\[
v_2(\phi(u))=\sum_{i=1}^s v_2(p_i-1).
\]
Every summand is at least \(1\). Hence (23) holds if and only if \(s=1\) and
\[
p_1\equiv3\pmod4.
\]

Thus:

**Lemma 1.** For odd \(u>1\), \(T(u)\) is even if and only if
\[
u=P^a
\]
for some prime \(P\equiv3\pmod4\) and \(a\ge1\).

For such a prime power,
\[
T(P^a)
=P^a+\frac{P^{a-1}(P-1)}2
=P^{a-1}\frac{3P-1}{2}. \tag{24}
\]
Therefore
\[
v_2(T(P^a))=v_2(3P-1)-1.
\]
If \(P\equiv7\pmod8\), then \(3P-1\equiv4\pmod8\), so this valuation is exactly \(1\). If \(P\equiv3\pmod8\), then \(8\mid3P-1\), so the valuation is at least \(2\).

---

### 3. The pure-power exceptional cycle

The subset
\[
\mathcal E
=\{2^e:e\ge1\}\cup\{3\cdot2^e:e\ge0\}
\]
is invariant under \(T\). Indeed,
\[
T(2)=3,
\]
and for \(e\ge2\),
\[
T(2^e)=F(2^e)=3\cdot2^{e-1}.
\]
Also,
\[
T(3)=4,
\qquad
T(3\cdot2^e)=2^eT(3)=2^{e+2}.
\]

In particular,
\[
T^2(2)=4=2\cdot2,\qquad
T^2(3)=6=2\cdot3.
\]
Since all \(T\)-orbits are strictly increasing, lag \(2\) is the unique doubling lag for \(2\) and \(3\).

Under (20), these yield the primitive \(F\)-seeds
\[
4,\quad6.
\]

---

### 4. Exact primitive-chain reduction for all other direct seeds

**Theorem 2.** Let \(q\ge3\) be odd and suppose
\[
T^r(q)=2q. \tag{25}
\]
Then either:

1. \(q=3\) and \(r=2\); or
2. there are a prime \(P\equiv7\pmod8\), an exponent \(a\ge1\), and odd integers
   \[
   u_0<u_1<\cdots<u_{r-1}
   \]
   satisfying
   \[
   u_0=P^{a-1}\frac{3P-1}{4},\qquad
   u_{r-1}=P^a, \tag{26}
   \]
   and
   \[
   u_{i+1}=u_i+\frac{\phi(u_i)}2
   \qquad(0\le i\le r-2). \tag{27}
   \]

Moreover, \(q\) is one of the \(u_i\).

Conversely, any chain satisfying (26)–(27) gives
\[
T^r(u_i)=2u_i
\qquad(0\le i\le r-1). \tag{28}
\]

#### Proof

Set
\[
z_i=T^i(q).
\]
Then \(z_0=q\) is odd and \(z_r=2q\) has \(2\)-adic valuation \(1\). Let \(h\) be the first index for which \(z_h\) is even. By Lemma 1,
\[
z_{h-1}=P^a
\]
for some prime \(P\equiv3\pmod4\).

Suppose first that some \(z_i\) belongs to \(\mathcal E\). Since \(\mathcal E\) is \(T\)-invariant, \(z_r=2q\in\mathcal E\). As \(v_2(2q)=1\) and \(q\) is odd, this forces \(2q=6\), hence \(q=3\). Direct calculation gives \(r=2\).

Now assume \(q\ne3\). Then no \(z_i\) belongs to \(\mathcal E\).

If \(z=2^e w\), where \(e\ge1\) and \(w>1\) is odd, then by (19)
\[
T(z)=2^eT(w).
\]
Consequently,
\[
v_2(T(z))\ge e.
\]
Thus, after the first parity transition, the \(2\)-adic valuation cannot decrease. Since the final valuation is \(1\), the first even value \(z_h\) must already have valuation \(1\), and all \(z_i\), \(h\le i\le r\), have valuation \(1\).

It follows from (24) that \(P\equiv7\pmod8\), and
\[
z_h=T(P^a)
=2P^{a-1}\frac{3P-1}{4}.
\]
Put
\[
u_0=P^{a-1}\frac{3P-1}{4}.
\]
Then \(u_0\) is odd and \(z_h=2u_0\).

For \(i\ge h\), write
\[
z_i=2w_{i-h}
\]
with \(w_{i-h}\) odd. Since \(T(2w)=2T(w)\),
\[
w_{j+1}=T(w_j).
\]
At the endpoint,
\[
z_r=2q,
\]
so
\[
T^{r-h}(u_0)=q. \tag{29}
\]
On the other hand,
\[
T^{h-1}(q)=P^a. \tag{30}
\]
Concatenating (29) and (30) gives an all-odd chain of \(r\) terms
\[
u_0,\ T(u_0),\ldots,q,\ldots,P^a,
\]
with
\[
T^{r-1}(u_0)=P^a.
\]
This is precisely (26)–(27), and \(q\) is one of the chain terms.

Conversely, suppose such a chain exists. Equation (24) gives
\[
T(P^a)=2u_0.
\]
Hence
\[
T^r(u_0)=2u_0.
\]
For a general chain member \(u_i\), iteration from \(u_i\) first reaches \(P^a\), then \(2u_0\), and thereafter (19) gives twice the initial segment of the chain. Thus
\[
T^r(u_i)=2u_i.
\]
This proves the converse. ∎

This theorem gives a complete equivalence for direct seeds:

- the pure cycle gives \(4\) and \(6\), and all their doublings;
- every other primitive direct seed comes from a chain (26)–(27);
- every chain member \(u_i\) gives the primitive \(F\)-seed \(2u_i\), and all its doublings.

Equivalently, Route 1 reduces the direct-seed problem to
\[
T^{r-1}\left(P^{a-1}\frac{3P-1}{4}\right)=P^a, \tag{31}
\]
with every intermediate value odd and \(P\equiv7\pmod8\). This is the precise form of Cambie’s stated reduction.

---

### 5. Complete reduction for lag \(2\)

Suppose a non-pure chain has \(r=2\). Let
\[
A=\frac{3P-1}{4}.
\]
Then
\[
u_0=P^{a-1}A,\qquad u_1=P^a.
\]

#### Exclusion of \(a\ge2\)

Because \(P\nmid A\),
\[
\phi(P^{a-1}A)=P^{a-2}(P-1)\phi(A).
\]
The equality \(T(u_0)=P^a\) becomes
\[
\frac{P^{a-2}(P-1)\phi(A)}2
=P^a-P^{a-1}A
=P^{a-1}\frac{P+1}{4}.
\]
Therefore
\[
2(P-1)\phi(A)=P(P+1). \tag{32}
\]
The left side is divisible by \(P-1\), so \(P-1\mid P(P+1)\). But
\[
P(P+1)\equiv2\pmod{P-1}.
\]
Hence \(P-1\mid2\), impossible because \(P\equiv7\pmod8\) and thus \(P\ge7\).

Therefore
\[
a=1. \tag{33}
\]

#### The resulting shifted-totient equation

Now \(u_0=A\), and \(T(A)=P\) gives
\[
\phi(A)=\frac{P+1}{2}. \tag{34}
\]
Since
\[
P=\frac{4A+1}{3},
\]
equation (34) is equivalent to
\[
\boxed{\phi(A)=\frac{2(A+1)}3}, \tag{35}
\]
together with the requirement that
\[
\boxed{\frac{4A+1}{3}\text{ is prime and }\equiv7\pmod8.} \tag{36}
\]

For \(A=5\), the associated prime is \(P=7\). For \(A=35\), it is \(P=47\). These give the chains
\[
5\longmapsto7\longmapsto10=2\cdot5,
\]
and
\[
35\longmapsto47\longmapsto70=2\cdot35.
\]

Thus the six known primitive seeds are exactly
\[
4,\ 6,\ 10,\ 14,\ 70,\ 94.
\]

---

### 6. Additional arithmetic restrictions on the lag-\(2\) exception

Suppose \(A\) satisfies (35). Write
\[
A=\prod_{i=1}^s p_i^{e_i},
\qquad
D=\prod_{i=1}^s p_i^{e_i-1},
\qquad
R=\prod_{i=1}^s p_i,
\qquad
S=\prod_{i=1}^s(p_i-1).
\]
Then \(A=DR\) and \(\phi(A)=DS\). Equation
\[
3\phi(A)=2A+2
\]
becomes
\[
D(3S-2R)=2. \tag{37}
\]
Because \(A\) is odd, \(D\) is odd. Hence \(D\mid2\) implies \(D=1\).

Therefore:

**Lemma 3.** Every solution of (35) is squarefree.

The equation then becomes
\[
3\prod_{p\mid A}(p-1)-2\prod_{p\mid A}p=2. \tag{38}
\]

It is possible to classify solutions having at most three prime factors.

#### One prime factor

If \(A=p\), then
\[
3(p-1)-2p=2,
\]
so \(p=5\).

#### Two prime factors

If \(A=pq\), then
\[
3(p-1)(q-1)-2pq=2,
\]
equivalently
\[
(p-3)(q-3)=8.
\]
Since \(p-3\) and \(q-3\) are positive even integers, this gives
\[
\{p,q\}=\{5,7\}.
\]
Thus \(A=35\).

#### Three prime factors

Let \(A=pqr\) with \(p<q<r\). Solving (38) for \(r\) gives
\[
r=
\frac{3(p-1)(q-1)+2}
     {3(p-1)(q-1)-2pq}. \tag{39}
\]
The denominator must be positive.

If \(p\ge7\), then \(q\ge p+2\). A direct calculation shows that
\[
q\bigl(3(p-1)(q-1)-2pq\bigr)
-\bigl(3(p-1)(q-1)+2\bigr)>0
\]
for \(p\ge7\) and \(q\ge p+2\). Indeed, the difference is
\[
(p-3)q^2-6(p-1)q+3p-5,
\]
which is increasing in \(q\) in this range and at \(q=p+2\) equals
\[
p^3-5p^2-11p-5>0
\]
for \(p\ge7\). Equation (39) would therefore give \(r<q\), contradicting \(r>q\).

Hence \(p=5\). Equation (39) becomes
\[
r=\frac{12q-10}{2q-12}
  =6+\frac{31}{q-6}.
\]
Thus \(q-6\mid31\). Respecting \(5<q<r\), the only choice is
\[
q=7,\qquad r=37.
\]
Therefore
\[
A=5\cdot7\cdot37=1295.
\]

Its associated number in (36) is
\[
\frac{4A+1}{3}
=\frac{5181}{3}
=1727
=11\cdot157,
\]
which is not prime.

Thus:

**Proposition 4.** If a lag-\(2\) exceptional \(A\) has at most three distinct prime factors, then
\[
A\in\{5,35,1295\},
\]
and only \(A=5,35\) yield the required prime \(P\). Any new lag-\(2\) direct seed must arise from a squarefree \(A\) with at least four distinct prime factors.

This is still not enough to eliminate all exceptional \(A\).

---

### 7. A quantitative but nondecisive restriction on longer chains

For every odd \(n>1\),
\[
\phi(n)>\sqrt n. \tag{40}
\]
Indeed, for a prime power \(p^e\) with odd \(p\),
\[
\frac{\phi(p^e)^2}{p^e}
=p^{e-2}(p-1)^2>1,
\]
and the corresponding ratios multiply over coprime prime powers.

For a chain in Theorem 2,
\[
P^a-u_0
=\sum_{i=0}^{r-2}\frac{\phi(u_i)}2.
\]
Since \(u_i\ge u_0\), (40) gives
\[
P^a-u_0>\frac{r-1}{2}\sqrt{u_0}.
\]
Therefore
\[
r-1<
\frac{2(P^a-u_0)}{\sqrt{u_0}}
=
\frac{P^{a-1}(P+1)}{2\sqrt{u_0}}. \tag{41}
\]
This bounds \(r\) for each fixed \(P,a\), but does not force \(r=2\).

For \(a=1\), write \(u_0=A\). If \(r\ge3\), then
\[
u_1=A+\frac{\phi(A)}2<P
\]
and
\[
P-u_1
=\frac{2A+2-3\phi(A)}6.
\]
Since the remaining chain contains at least the increment \(\phi(u_1)/2\),
\[
\frac{2A+2-3\phi(A)}6
\ge\frac{\phi(u_1)}2
>\frac{\sqrt{u_1}}2.
\]
Hence every longer chain must satisfy
\[
2A+2-3\phi(A)>3\sqrt{u_1}. \tag{42}
\]
This excludes cases in which the first step nearly reaches \(P\), but it is not a global classification.

---

### 8. The proposed eventual-start classification is false

Consider
\[
n=18.
\]
The exact orbit segment is
\[
18\longmapsto24\longmapsto32\longmapsto48.
\]
The required totients are
\[
18=2\cdot3^2,\qquad \phi(18)=6,
\]
\[
24=2^3\cdot3,\qquad \phi(24)=8,
\]
\[
32=2^5,\qquad \phi(32)=16.
\]
Thus
\[
F(18)=24,\qquad F(24)=32,\qquad F^2(24)=48=2\cdot24.
\]
Since \(24\) is even, the doubling identity propagates this:
\[
F^{j+2}(24)=2F^j(24)\qquad(j\ge0).
\]
Putting \(j=k-1\), for every \(k\ge1\),
\[
F^{k+2}(18)=2F^k(18).
\]
Therefore
\[
(18,2)
\]
is a valid eventual solution with \(K=1\).

But \(18\) is not of the form
\[
2^\ell q,\qquad q\in\{2,3,5,7,35,47\},
\]
because its odd part is \(9\). Hence the conjectural classification (C), interpreted as a classification of all eventual starting values, is false.

Moreover, scaling gives an infinite off-list family. For every \(j\ge0\),
\[
F(2^j\cdot18)=2^jF(18)=2^j\cdot24,
\]
and \(2^j\cdot24\) is a direct lag-\(2\) seed. Thus
\[
\boxed{n=2^{j+1}\cdot9,\quad r=2,\quad j\ge0}
\]
are all eventual solutions, none belonging to (C).

Other one-step examples include
\[
\begin{array}{c|c|c|c}
n&F(n)=x&F(x)&F^2(x)=2x\\ \hline
22&32&48&64\\
38&56&80&112\\
86&128&192&256\\
98&140&188&280\\
214&320&448&640\\
502&752&1120&1504\\
1366&2048&3072&4096.
\end{array}
\]
For example, \(683\) is prime and
\[
F(2\cdot683)=3\cdot683-1=2048.
\]

More generally, if \(Q=P^a\) with \(P\equiv3\pmod4\) prime and
\[
P^{a-1}(3P-1)=2^b s,
\qquad
s\in\{1,3,5,7,35,47\},
\]
where \(2^bs\) is one of the known direct families, then
\[
F(2Q)=2^bs
\]
and \(2Q\) is an eventual lag-\(2\) starting value. This demonstrates that the backward-preimage problem is an essential, not cosmetic, part of the original classification.

## Self-Audit

1. **The treatment of powers of two in Theorem 2 is the most delicate point.**  
   In general, \(2\)-adic valuation can decrease along \(T\), as \(T(8)=12\) shows. The proof does not assume unrestricted monotonicity: it isolates the invariant exceptional set \(\mathcal E\) containing pure powers and their \(3\)-multiples. Outside that set, writing \(z=2^ew\) with odd \(w>1\) gives the exact identity \(T(z)=2^eT(w)\), which makes the valuation nondecreasing.

2. **The concatenation producing the \(r\)-term odd chain is indexing-sensitive.**  
   The segment after the first parity transition, divided by \(2\), runs from \(u_0\) to \(q\); the original odd segment runs from \(q\) to \(P^a\). Their total number of transitions is \((r-h)+(h-1)=r-1\), so there are exactly \(r\) odd chain members. The converse was checked separately using \(T(2y)=2T(y)\).

3. **The lag-\(2\) arithmetic classification is deliberately incomplete.**  
   I prove only that every exceptional \(A\) is squarefree and classify \(\omega(A)\le3\). I do not claim that no solution with four or more prime factors exists. This is precisely the unresolved block, not a hidden assumption in the argument.

## Computations To Verify

```python
from math import isqrt

def factor(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        p = 3 if p == 2 else p + 2
    if n > 1:
        out.append((n, 1))
    return out

def phi(n):
    if n == 1:
        return 1
    ans = n
    for p, e in factor(n):
        ans = ans // p * (p - 1)
    return ans

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

def F(n):
    return n + phi(n)

def T(y):
    assert y >= 2
    z = F(2 * y)
    assert z % 2 == 0
    return z // 2

# Verify normalization and equivariance.
for y in range(2, 10000):
    assert F(2 * y) == 2 * T(y)
    assert T(2 * y) == 2 * T(y)

# Verify the six primitive direct seeds.
for x in [4, 6, 10, 14, 70, 94]:
    assert F(F(x)) == 2 * x

# Exact counterexample to the proposed eventual classification.
assert factor(18) == [(2, 1), (3, 2)]
assert phi(18) == 6
assert F(18) == 24
assert factor(24) == [(2, 3), (3, 1)]
assert phi(24) == 8
assert F(24) == 32
assert factor(32) == [(2, 5)]
assert phi(32) == 16
assert F(32) == 48 == 2 * 24

# Check many terms of the eventual identity for n=18.
a = [18]
for _ in range(30):
    a.append(F(a[-1]))
for k in range(1, 28):
    assert a[k + 2] == 2 * a[k]

# Check the other listed transient examples.
transients = {
    22: 32,
    38: 56,
    86: 128,
    98: 140,
    214: 320,
    502: 752,
    1366: 2048,
}
for n, x in transients.items():
    assert F(n) == x
    assert F(F(x)) == 2 * x

# Exhaustive primitive direct-seed search up to B.
def primitive_direct_seeds(B):
    hits = []
    for x in range(4, B + 1, 2):
        if not (x == 4 or x % 4 == 2):
            continue
        y = x
        r = 0
        while y < 2 * x:
            y = F(y)
            r += 1
        if y == 2 * x:
            hits.append((x, r))
    return hits

print(primitive_direct_seeds(10**6))

# Search the exact chain reduction for P^a.
def search_chains(Pmax, amax):
    hits = []
    for P in range(7, Pmax + 1, 8):
        if not is_prime(P):
            continue
        for a in range(1, amax + 1):
            target = P ** a
            u0 = P ** (a - 1) * ((3 * P - 1) // 4)
            u = u0
            steps = 0
            all_odd = True
            while u < target:
                if u % 2 == 0:
                    all_odd = False
                    break
                u = T(u)
                steps += 1
            if all_odd and u == target:
                # chain has steps = r-1
                r = steps + 1
                assert T(target) == 2 * u0
                hits.append((P, a, r, u0))
    return hits

print(search_chains(100000, 5))

# Search the lag-2 shifted-totient equation.
def search_lag2_exception(Amax):
    hits = []
    for A in range(5, Amax + 1, 2):
        if 3 * phi(A) != 2 * A + 2:
            continue
        numerator = 4 * A + 1
        if numerator % 3:
            continue
        P = numerator // 3
        hits.append({
            "A": A,
            "factor_A": factor(A),
            "P": P,
            "factor_P": factor(P),
            "P_prime": is_prime(P),
        })
    return hits

print(search_lag2_exception(10**7))

# Complete backward-preimage search for known direct targets up to B.
def odd_part(n):
    while n % 2 == 0:
        n //= 2
    return n

S = {1, 3, 5, 7, 35, 47}

def known_direct(x):
    return x >= 4 and x % 2 == 0 and odd_part(x) in S

def search_off_family_predecessors(B):
    hits = []
    for y in range(4, B + 1, 2):
        z = F(y)
        if known_direct(z) and not known_direct(y):
            hits.append((y, z, factor(y), factor(z)))
    return hits

print(search_off_family_predecessors(10**6)[:200])
```

## Route Diagnosis

**What worked.**

- Powers-of-two normalization is exact after passing to
  \[
  T(y)=F(2y)/2.
  \]
- Every direct seed reduces to either the special cycle \(2\leftrightarrow3\) modulo doubling or an all-odd chain associated with \(P^a\), \(P\equiv7\pmod8\).
- The reduction recovers Cambie’s equation in a precise, fully quantified form.
- For \(r=2\), exponents \(a\ge2\) are impossible.
- The remaining lag-\(2\) equation forces squarefree \(A\), and all cases with at most three prime factors can be settled.
- Investigating backward collisions exposed a superior immediate observation: the proposed classification of eventual starting values is false, beginning with \(18\mapsto24\).

**Precise block.**

The direct-seed problem is now equivalent to classifying
\[
T^{r-1}\left(P^{a-1}\frac{3P-1}{4}\right)=P^a
\]
with all intermediate values odd. For \(r=2\), this already contains
\[
\phi(A)=\frac{2(A+1)}3,
\qquad
\frac{4A+1}{3}\ \text{prime},
\]
which is an unresolved shifted/inverse-totient problem of comparable strength to the original direct-seed question. Route 1 therefore cannot presently be completed.

The original eventual problem has an additional independent block: classify every solution of
\[
y+\phi(y)=z
\]
where \(z\) lies on a direct solution ray, and then iterate this backward. The collision
\[
F(18)=F(16)=24
\]
shows that no injectivity or naive backward-rigidity statement is available.

**Ledger.**

- **Proved:** normalization by \(T\); exact primitive-chain theorem; \(P\equiv7\pmod8\); exclusion of \(a\ge2\) for \(r=2\); squarefreeness of exceptional \(A\); classification for \(\omega(A)\le3\); explicit infinite off-list eventual family \(2^{j+1}9\).
- **Plausible but unproved:** the only primitive chains are the two lag-\(2\) chains \(5\to7\) and \(35\to47\), together with the pure cycle.
- **Dead end:** global injectivity or restricted even injectivity of \(F\), refuted by \(F(16)=F(18)=24\).
- **Dead end:** a purely \(2\)-adic proof forcing \(r=2\); after normalization, valuations leave an unrestricted all-odd totient chain.
- **Insufficient:** the lower bound \(\phi(n)>\sqrt n\), which gives only parameter-dependent lag bounds.

A fresh attempt should first correct the conjectural statement to include backward trees, then pursue two problems separately: classify the primitive chains (especially squarefree solutions of (35) with prime associated \(P\)), and compute/prove the structure of backward preimages of the known direct rays.