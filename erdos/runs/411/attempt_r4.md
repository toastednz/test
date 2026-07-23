STATUS: BLOCKED

## Result

Under the stated “for all sufficiently large \(k\)” interpretation, Cambie’s proposed classification is false: \(n=18,r=2,K=1\) is a counterexample, since \(18\mapsto24\mapsto32\mapsto48\) and \(F^2(24)=48=2\cdot24\). More generally, every \(n=2^b3^t\) with \(b,t\ge1\) eventually satisfies the lag-\(2\) relation, giving transient solutions of arbitrarily large backward depth. I give an exact odd-core reformulation in terms of a weighted map \(T\), prove that eventual solutions are precisely basins of weight-one cycles of \(T\), derive Cambie’s \(p\equiv7\pmod8\) reduction, and completely classify all immediate preimages of values on the six conjectured rays. The full problem remains blocked because one must still classify all weight-one cycles of \(T\) and their complete backward basins.

## Complete Argument

### 1. A finite counterexample to the conjectured classification

Take
\[
n=18,\qquad r=2,\qquad K=1.
\]
The exact orbit segment is
\[
18\longmapsto24\longmapsto32\longmapsto48.
\]
Indeed,
\[
18=2\cdot3^2,\qquad \phi(18)=6,
\]
so \(F(18)=24\). Also
\[
24=2^3\cdot3,\qquad \phi(24)=2^2(3-1)=8,
\]
so \(F(24)=32\). Finally,
\[
32=2^5,\qquad \phi(32)=2^4=16,
\]
so \(F(32)=48\). Therefore
\[
F^2(24)=48=2\cdot24.
\]

Since \(24\) is even and at least \(4\), the standard propagation identity gives
\[
F^{j+2}(24)=2F^j(24)\qquad(j\ge0).
\]
As \(24=F(18)\), this is
\[
F^{k+2}(18)=2F^k(18)\qquad(k\ge1).
\]

But \(18\) is not of the form
\[
2^\ell q,\qquad q\in\{2,3,5,7,35,47\}.
\]
Its maximal odd factor is \(9\). Thus the conjectured classification is false under the eventual interpretation in the brief.

The simplest proposed collision-rigidity lemma is also false:
\[
F(16)=24=F(18).
\]
Both \(16\) and \(18\) are even, but only \(16\) lies in the proposed family.

---

### 2. Exact odd-core dynamics

Every even integer \(n\ge4\) has a unique representation
\[
n=2^b a,
\]
where \(b\ge1\), \(a\) is odd, and \(b\ge2\) if \(a=1\).

For odd \(a>1\), define
\[
H(a):=a+\frac{\phi(a)}2,
\]
which is an integer because \(\phi(a)\) is even. Put
\[
\delta(a):=v_2(H(a)),\qquad
T(a):=\frac{H(a)}{2^{\delta(a)}}.
\]
Thus \(T(a)\) is the odd part of \(H(a)\).

For the exceptional odd core \(a=1\), define
\[
T(1):=3,\qquad \delta(1):=-1.
\]

#### Lemma 1: weighted odd-core formula

For every admissible \(n=2^b a\),
\[
F(2^b a)=2^{b+\delta(a)}T(a). \tag{18}
\]

#### Proof

If \(a>1\), multiplicativity of \(\phi\) gives
\[
\phi(2^b a)=\phi(2^b)\phi(a)=2^{b-1}\phi(a).
\]
Hence
\[
F(2^b a)
=2^b a+2^{b-1}\phi(a)
=2^b\left(a+\frac{\phi(a)}2\right)
=2^{b+\delta(a)}T(a).
\]

If \(a=1\), then \(b\ge2\) and
\[
F(2^b)=2^b+2^{b-1}=3\cdot2^{b-1}
      =2^{b+\delta(1)}T(1).
\]
This proves (18). ∎

Let
\[
a_j=T^j(a),\qquad
D_r(a):=\sum_{j=0}^{r-1}\delta(a_j).
\]
Iterating Lemma 1 gives
\[
F^r(2^b a)=2^{b+D_r(a)}T^r(a). \tag{19}
\]

All intermediate states are admissible automatically because they are the odd-core decompositions of even integers at least \(4\).

---

### 3. Exact weighted-cycle criterion

#### Theorem 2

Let \(n=2^b a\ge4\) be even. Then
\[
F^r(n)=2n
\]
if and only if
\[
T^r(a)=a
\quad\text{and}\quad
D_r(a)=1. \tag{20}
\]

Consequently, \((n,r)\) satisfies the eventual relation if and only if the forward \(T\)-orbit of \(a\) eventually reaches a cycle whose total \(\delta\)-weight is \(1\). In that event, \(r\) is the least period of that cycle.

#### Proof

By (19),
\[
F^r(2^b a)=2^{b+D_r(a)}T^r(a).
\]
Unique decomposition into a power of \(2\) and an odd factor shows that this equals
\[
2n=2^{b+1}a
\]
if and only if (20) holds.

Suppose now that \(a\) lies on a \(T\)-cycle of least period \(d\) and total weight
\[
W=\sum_{j=0}^{d-1}\delta(T^j(a)).
\]
If \(T^r(a)=a\), then \(r=qd\) for some positive integer \(q\), and
\[
D_r(a)=qW.
\]
The equality \(D_r(a)=1\), with \(q,W\in\mathbb Z\), forces
\[
q=1,\qquad W=1.
\]
Thus \(r=d\).

If the original relation holds eventually, choose an iterate
\[
x=F^K(n)
\]
for which \(F^r(x)=2x\). Its odd core therefore lies on a weight-one cycle.

Conversely, if the odd core reaches a weight-one cycle after \(K\) iterations, then \(x=F^K(n)\) satisfies \(F^r(x)=2x\). Since \(x\) and all its iterates are even,
\[
F^j(2x)=2F^j(x)\qquad(j\ge0),
\]
by repeated use of \(F(2m)=2F(m)\) for even \(m\). Hence
\[
F^{j+r}(x)=2F^j(x)\qquad(j\ge0),
\]
which is exactly the eventual relation for \(n\). ∎

This gives a precise description of the backward-orbit problem: starting exponents \(b\) are irrelevant; what matters is whether the odd core belongs to the basin of a weight-one \(T\)-cycle.

---

### 4. Structure of all possible weight-one cycles

For odd \(a>1\), write
\[
a=\prod_{i=1}^s p_i^{e_i}.
\]
Then
\[
v_2(\phi(a))=\sum_{i=1}^s v_2(p_i-1). \tag{21}
\]

#### Lemma 3

For odd \(a>1\),
\[
\delta(a)>0
\]
if and only if
\[
a=p^t
\]
for a prime \(p\equiv3\pmod4\).

Moreover:

- if \(\delta(a)=0\), then \(T(a)>a\);
- if \(\delta(a)>0\), then
  \[
  T(a)<\frac34a.
  \]

#### Proof

Since \(a\) is odd,
\[
H(a)=a+\frac{\phi(a)}2
\]
is even exactly when \(\phi(a)/2\) is odd, namely when
\[
v_2(\phi(a))=1.
\]
By (21), this occurs exactly when \(a\) has one distinct prime divisor \(p\), with
\[
v_2(p-1)=1,
\]
i.e. \(a=p^t\) and \(p\equiv3\pmod4\).

If \(\delta(a)=0\), then
\[
T(a)=H(a)=a+\frac{\phi(a)}2>a.
\]
If \(\delta(a)>0\), then
\[
T(a)\le\frac{H(a)}2
<\frac{a+a/2}{2}
=\frac34a,
\]
because \(\phi(a)<a\) for \(a>1\). ∎

Thus every nontrivial cycle alternates between strictly increasing stretches and sharp drops occurring only at prime powers \(p^t\), \(p\equiv3\pmod4\).

#### Proposition 4

Every weight-one cycle is of one of the following two forms.

1. The cycle
   \[
   1\longmapsto3\longmapsto1,
   \]
   of period \(2\) and weights
   \[
   \delta(1)=-1,\qquad \delta(3)=2.
   \]

2. A cycle not containing \(1\), having exactly one drop state
   \[
   p^t,\qquad p\equiv7\pmod8,
   \]
   at which \(\delta(p^t)=1\). Every other state on the cycle has weight \(0\) and is strictly increased by \(T\).

#### Proof

If a cycle contains \(1\), then determinism gives
\[
1\mapsto3.
\]
Since
\[
H(3)=3+\frac{\phi(3)}2=4,
\]
we have
\[
T(3)=1,\qquad\delta(3)=2.
\]
Thus the entire cycle is \(\{1,3\}\), with total weight \(-1+2=1\).

Now consider a cycle not containing \(1\). All its weights are nonnegative. It cannot have every weight equal to zero, since then \(T\) would strictly increase at every step. A total weight of \(1\) therefore forces exactly one positive weight, equal to \(1\).

By Lemma 3 the corresponding state is \(p^t\) with \(p\equiv3\pmod4\). Here
\[
H(p^t)
=p^{t-1}\frac{3p-1}{2},
\]
so
\[
\delta(p^t)=v_2\!\left(\frac{3p-1}{2}\right).
\]
If \(p\equiv3\pmod8\), then \(3p-1\) is divisible by \(8\), and this valuation is at least \(2\). If \(p\equiv7\pmod8\), then
\[
\frac{3p-1}{2}\equiv2\pmod4,
\]
so the valuation is exactly \(1\). Thus \(p\equiv7\pmod8\). ∎

This rigorously recovers the structural core of Cambie’s reduction. Excluding all \(r\ge3\) is equivalent to proving that no longer cycle of this specified form exists.

---

### 5. The period-\(2\) branch

Suppose a non-\(\{1,3\}\) weight-one cycle has period \(2\). Its unique drop state is \(p^t\), where \(p\equiv7\pmod8\). Put
\[
c=\frac{3p-1}{4}.
\]
Then
\[
T(p^t)=p^{t-1}c.
\]

#### Proposition 5

For such a period-\(2\) cycle, necessarily \(t=1\), and
\[
\phi(c)=\frac{p+1}{2}. \tag{22}
\]
Writing \(p=8m+7\), this becomes
\[
c=6m+5,\qquad \phi(6m+5)=4m+4. \tag{23}
\]

#### Proof

Let
\[
A=p^{t-1}c=T(p^t).
\]
The second state has weight \(0\), so the return condition is
\[
H(A)=p^t. \tag{24}
\]

Suppose \(t\ge2\). Since \(\gcd(p,c)=1\),
\[
\phi(A)=p^{t-2}(p-1)\phi(c).
\]
On the other hand, (24) implies
\[
\phi(A)=2(p^t-A)
       =2p^{t-1}(p-c)
       =p^{t-1}\frac{p+1}{2}.
\]
Therefore
\[
2(p-1)\phi(c)=p(p+1).
\]
Since \(\gcd(p,2(p-1))=1\), this implies \(p\mid\phi(c)\). But
\[
1<c=\frac{3p-1}{4}<p,
\]
so
\[
0<\phi(c)<p,
\]
a contradiction.

Hence \(t=1\). Now \(A=c\), and \(H(c)=p\) gives
\[
\phi(c)=2(p-c)=\frac{p+1}{2}.
\]
Substituting \(p=8m+7\) gives (23). ∎

The known solutions are
\[
p=7,\quad c=5,
\]
and
\[
p=47,\quad c=35.
\]
Eliminating all other solutions of (23) is the hard shifted-totient branch.

---

### 6. Transient solutions of arbitrarily large backward depth

For every \(t\ge1\),
\[
\phi(3^t)=2\cdot3^{t-1},
\]
and therefore
\[
H(3^t)=3^t+3^{t-1}=4\cdot3^{t-1}.
\]
Thus
\[
T(3^t)=3^{t-1},\qquad \delta(3^t)=2. \tag{25}
\]

Consequently, for \(b,t\ge1\),
\[
F^j(2^b3^t)=2^{b+2j}3^{t-j}
\qquad(0\le j\le t). \tag{26}
\]
In particular,
\[
F^{t-1}(2^b3^t)=2^{b+2t-2}3,
\]
whose odd core \(3\) lies on the weight-one cycle
\[
3\mapsto1\mapsto3.
\]
Therefore
\[
F^{k+2}(2^b3^t)=2F^k(2^b3^t)
\qquad(k\ge t-1). \tag{27}
\]

Thus every
\[
n=2^b3^t,\qquad b,t\ge1,
\]
is an eventual lag-\(2\) solution. For \(t\ge2\), these are absent from the proposed classification.

The backward depths \(t-1\) are unbounded. Hence no finite-depth backward-tree computation can establish the original classification.

There is also an infinite family of explicit collisions:
\[
F(2^{b+3})=3\cdot2^{b+2}=F(2^b3^2)
\qquad(b\ge1). \tag{28}
\]

---

### 7. A complete immediate-preimage theorem

The odd-core inverse problem has a useful exact form.

#### Lemma 6

Let \(a>1\) and \(c\) be odd. Then \(T(a)=c\) if and only if, for some \(d\ge0\),
\[
H(a)=2^dc,
\]
with one of the following alternatives:

1. \(d=0\) and
   \[
   a+\frac{\phi(a)}2=c;
   \]
2. \(d\ge1\), and
   \[
   a=p^t,\qquad p\equiv3\pmod4,
   \]
   with
   \[
   p^{t-1}\frac{3p-1}{2}=2^dc. \tag{29}
   \]

If \(t=1\), equation (29) is
\[
p=\frac{2^{d+1}c+1}{3}, \tag{30}
\]
and it suffices that the displayed quotient be prime. If \(t\ge2\), then
\[
p^{t-1}\mid c. \tag{31}
\]

#### Proof

The only claim not already proved is (31). From (29),
\[
p^{t-1}\mid 2^dc.
\]
But \(p\) is odd, so \(p\nmid2^d\), and
\[
\gcd\left(p,\frac{3p-1}{2}\right)=1.
\]
Thus \(p^{t-1}\mid c\). Conversely, every solution of the displayed equations gives \(T(a)=c\) directly from the definitions. ∎

Applying this lemma gives all immediate preimages of the six listed odd cores. In the table, each pair \((a,d)\) means
\[
T(a)=c,\qquad \delta(a)=d.
\]

\[
\begin{array}{c|l}
c&\text{all pairs }(a,d)\\ \hline
1&
\left(\dfrac{2^{d+1}+1}{3},d\right),
\quad d\ge2\text{ even, quotient prime}\\[2mm]
3&(1,-1),\ (9,2)\\[1mm]
5&
\left(\dfrac{5\cdot2^{d+1}+1}{3},d\right),
\quad d\ge1\text{ odd, quotient prime}\\[2mm]
7&
(5,0),\quad
\left(\dfrac{7\cdot2^{d+1}+1}{3},d\right),
\quad d\ge2\text{ even, quotient prime}\\[2mm]
35&
(25,0),\ (49,1),\quad
\left(\dfrac{35\cdot2^{d+1}+1}{3},d\right),
\quad d\ge1\text{ odd, quotient prime}\\[2mm]
47&
(35,0),\quad
\left(\dfrac{47\cdot2^{d+1}+1}{3},d\right),
\quad d\ge1\text{ odd, quotient prime}.
\end{array} \tag{32}
\]

For completeness, the \(d=0\) assertions follow by checking \(H(a)=c\) for odd \(a<c\). The needed values are
\[
\begin{array}{c|rrrrrrrrrrr}
a&3&5&7&9&11&13&15&17&19&21&23\\
H(a)&4&7&10&12&16&19&19&25&28&27&34
\end{array}
\]
and
\[
\begin{array}{c|rrrrrrrrrrr}
a&25&27&29&31&33&35&37&39&41&43&45\\
H(a)&35&36&43&46&43&47&55&51&61&64&57.
\end{array}
\]
Thus the only relevant \(d=0\) solutions are
\[
T(5)=7,\qquad T(25)=35,\qquad T(35)=47.
\]

For \(t\ge2\), condition \(p^{t-1}\mid c\) leaves only
\[
T(9)=3,\qquad T(49)=35
\]
among the six cores. The remaining entries are the prime case (30); divisibility by \(3\) yields exactly the parity restrictions on \(d\) shown in the table.

Now let
\[
z=2^B c
\]
be a listed ray value. Every even preimage \(y\) of \(z\) is obtained from a table entry \((a,d)\) by setting
\[
b=B-d,\qquad y=2^b a,
\]
subject to \(b\ge1\). Conversely, every such entry gives a preimage. This is a complete immediate-preimage classification for all listed rays.

Examples include
\[
T(9)=3,\quad T(11)=1,\quad T(19)=7,\quad
T(25)=35,\quad T(49)=35,
\]
and
\[
T(107)=5,\qquad T(251)=47.
\]
Accordingly,
\[
18\mapsto24,\quad 22\mapsto32,\quad
38\mapsto56,\quad 50\mapsto70,\quad
98\mapsto140,\quad 214\mapsto320,\quad
502\mapsto752.
\]
Every target on the right lies on one of the known weight-one cycles or its power-of-two scaling ray.

The appearance of primes of the form
\[
\frac{2^{d+1}c+1}{3}
\]
shows that even the first inverse layer is tied to unbounded primality questions.

## Self-Audit

1. **The odd-core map has an exceptional negative weight at \(a=1\).**  
   This is the most delicate bookkeeping point. It is handled separately by the exact identity \(F(2^b)=3\cdot2^{b-1}\), valid for \(b\ge2\). No actual orbit from an even integer at least \(4\) reaches the inadmissible state \(2^1\cdot1\).

2. **The immediate-preimage table uses a finite hand enumeration for the \(d=0\) cases.**  
   The enumeration is explicitly displayed for every odd \(a<47\), and Lemma 6 proves that no other kind of \(d=0\) solution is possible. The supplied code below independently checks the table.

3. **The weighted-cycle reformulation is exact but not an exhaustive arithmetic classification.**  
   It does not prove that the three known cycles are the only weight-one cycles, nor does it classify their entire basins. I believe the reformulation itself is correct because it follows directly from unique odd-core decomposition and the exact iterate formula (19), but it exposes rather than resolves the remaining open problems.

## Computations To Verify

```python
from sympy import totient, isprime, factorint

def F(n):
    return n + int(totient(n))

def v2(n):
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e

def T_delta(a):
    assert a % 2 == 1
    if a == 1:
        return 3, -1
    h = a + int(totient(a)) // 2
    d = v2(h)
    return h >> d, d

# Exact counterexample certificate.
orbit = [18]
for _ in range(3):
    orbit.append(F(orbit[-1]))
assert orbit == [18, 24, 32, 48]
assert F(F(24)) == 48 == 2 * 24

for x in [18, 24, 32]:
    print(x, factorint(x), int(totient(x)), F(x))

# Large finite verification of the eventual identity for n=18.
x = 18
vals = [x]
for _ in range(200):
    vals.append(F(vals[-1]))
for k in range(1, 198):
    assert vals[k + 2] == 2 * vals[k]

# Verify the family 2^b 3^t and formula (26).
for b in range(1, 20):
    for t in range(1, 15):
        n = (2**b) * (3**t)
        x = n
        for j in range(t + 1):
            assert x == (2**(b + 2*j)) * (3**(t-j))
            if j < t:
                x = F(x)

# Candidate table for T^{-1}(c).
def listed_core_preimages(c, dmax):
    ans = set()

    if c == 3:
        ans.add((1, -1))
        ans.add((9, 2))
    if c == 7:
        ans.add((5, 0))
    if c == 35:
        ans.add((25, 0))
        ans.add((49, 1))
    if c == 47:
        ans.add((35, 0))

    for d in range(1, dmax + 1):
        num = c * (2**(d + 1)) + 1
        if num % 3 == 0:
            p = num // 3
            if isprime(p):
                ans.add((p, d))
    return ans

# Check the complete immediate-preimage description for bounded ray values.
cores = [1, 3, 5, 7, 35, 47]

for c in cores:
    Bmin = 2 if c == 1 else 1
    for B in range(Bmin, 16):
        z = (2**B) * c

        actual = {y for y in range(1, z) if F(y) == z}

        predicted = set()
        for a, d in listed_core_preimages(c, B + 2):
            b = B - d
            if b >= 1:
                y = (2**b) * a
                if y < z:
                    predicted.add(y)

        assert actual == predicted, (c, B, z, actual, predicted)

# Direct-seed search, exhaustive up to MAX_X.
def direct_seeds(MAX_X):
    out = []
    for x in range(4, MAX_X + 1, 2):
        y = x
        r = 0
        while y < 2*x:
            y = F(y)
            r += 1
            if y == 2*x:
                out.append((x, r))
                break
    return out

print(direct_seeds(10**6))

# Search odd-core trajectories and detect bounded cycles.
def search_T_cycles(Amax, step_cap=10000, value_cap=10**12):
    cycles = set()
    for start in range(1, Amax + 1, 2):
        seen = {}
        a = start
        for j in range(step_cap):
            if a in seen:
                cyc = []
                x = a
                while True:
                    nxt, d = T_delta(x)
                    cyc.append((x, d))
                    x = nxt
                    if x == a:
                        break
                # canonical rotation
                reps = [tuple(cyc[i:] + cyc[:i]) for i in range(len(cyc))]
                cycles.add(min(reps))
                break
            if a > value_cap:
                break
            seen[a] = j
            a, _ = T_delta(a)
    return cycles

for cyc in sorted(search_T_cycles(10**5)):
    weight = sum(d for _, d in cyc)
    print("cycle =", cyc, "weight =", weight)
```

A particularly important search is for any weight-one cycle other than
\[
(1,3),\qquad(5,7),\qquad(35,47).
\]
Such a cycle would produce a new lag, or a new direct lag-\(2\) family.

## Route Diagnosis

The proposed backward rigidity is decisively false: \(18\) is an off-family predecessor of \(24\), and the branch \(2^b3^t\) has unbounded backward depth. What worked was replacing \(F\) by the weighted odd-core map \(T\). This gives an exact separation between two tasks:

1. classify all weight-one cycles of \(T\);
2. classify their full backward basins.

The first task is already of comparable strength to Cambie’s unresolved direct-seed problem. Every nontrivial weight-one cycle has one drop state \(p^t\) with \(p\equiv7\pmod8\); proving there are no longer cycles remains open. Even period \(2\) reduces to
\[
\phi(6m+5)=4m+4,\qquad 8m+7\ \text{prime}.
\]

The second task is substantially larger than the proposed list. Even immediate inverse layers contain primes of the form
\[
\frac{2^{d+1}c+1}{3},
\]
and recursive preimages generate arbitrarily deep trees. A fresh attempt should work directly with \(T\), focusing on the monotone segment between the unique drop \(p^t\) and its return. A theorem excluding return after two or more increasing steps would settle all \(r\ge3\); a separate inverse-totient analysis would still be needed to describe the complete basins.