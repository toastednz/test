STATUS: BLOCKED

## Result

Route 2 yields strong finite constructions but not an infinite ray. I prove: (i) an exact local extension criterion in terms of the first forbidden residue modulo a prime factor of the fixed coordinate; (ii) all recurrent staircase anchors must be odd and coprime to \(6\), with segment lengths strictly smaller than their least prime factors; (iii) for every \(r\), there exists a monotone admissible composite-anchor staircase with \(r\) L-shaped connectors, constructed rigorously by CRT; (iv) the natural prime-square version of Route 2 is impossible; and (v) a diagonally periodic staircase needs at least three L-connectors per period. The decisive unresolved issue is rooted compatibility: the CRT construction changes the starting point with \(r\), and extending a prescribed state requires finding rough composite numbers inside two mutually constrained short intervals. I do not have a uniform extension theorem, so this does not solve Erdős #1212.

## Complete Argument

### 1. Exact local extension criterion

For an integer \(m>1\) and \(s\) with \(\gcd(s,m)=1\), define
\[
\rho_m(s)=\min_{p\mid m}\rho_p(s),
\]
where \(\rho_p(s)\in\{1,\dots,p-1\}\) is the least positive integer such that
\[
s+\rho_p(s)\equiv 0\pmod p.
\]

#### Lemma 1
For \(d\ge 0\),
\[
\gcd(s+j,m)=1\quad(0\le j\le d)
\]
if and only if
\[
d<\rho_m(s).
\]

#### Proof
If \(d\ge \rho_m(s)\), choose a prime \(p\mid m\) attaining the minimum. Then
\[
p\mid s+\rho_m(s),
\]
so the interval is not entirely coprime to \(m\).

Conversely, suppose \(d<\rho_m(s)\). If some \(s+j\), \(0\le j\le d\), were not coprime to \(m\), some prime \(p\mid m\) would divide \(s+j\). By the definition of \(\rho_p(s)\), this implies
\[
j\ge \rho_p(s)\ge \rho_m(s)>d,
\]
a contradiction. ∎

For a Route 2 staircase, write
\[
d_n=a_{n+1}-a_n,\qquad e_n=b_{n+1}-b_n.
\]
Assuming the initial corner \((a_n,b_n)\) is visible, Lemma 1 says that the horizontal segment is visible exactly when
\[
d_n<\rho_{b_n}(a_n).
\]
Once its endpoint is visible, the vertical segment is visible exactly when
\[
e_n<\rho_{a_{n+1}}(b_n).
\]

Thus a prescribed state \((a_n,b_n)\) can be extended only by finding a composite \(a_{n+1}\) in the short interval
\[
a_n<a_{n+1}<a_n+\rho_{b_n}(a_n),
\]
followed by a composite \(b_{n+1}\) in
\[
b_n<b_{n+1}<b_n+\rho_{a_{n+1}}(b_n).
\]
This is the precise arithmetic bottleneck.

---

### 2. Necessary parity and roughness conditions

#### Lemma 2
In any infinite strictly increasing composite-anchor staircase:

1. every \(b_n\) is odd;
2. every \(a_n\) for \(n\ge 1\) is odd;
3. none of these recurrent anchors is divisible by \(3\);
4. consequently, their least prime factors are at least \(5\).

Moreover, once both endpoints of a segment are recurrent anchors,
\[
d_n\le \operatorname{lpf}(b_n)-3,\qquad
e_n\le \operatorname{lpf}(a_{n+1})-3,
\]
where \(\operatorname{lpf}(m)\) denotes the least prime factor of \(m\).

#### Proof
A horizontal segment has positive length. If its fixed coordinate \(b_n\) were even, two consecutive varying \(x\)-coordinates would include an even number, producing a point whose two coordinates are both even. Thus \(b_n\) is odd. The same argument applied to the positive vertical segment with fixed coordinate \(a_{n+1}\) shows that \(a_{n+1}\) is odd.

Therefore the differences \(d_n,e_n\) between recurrent anchors are positive even integers, hence at least \(2\).

If \(3\mid b_n\), then the horizontal interval contains at least three consecutive integers because \(d_n\ge2\). One is divisible by \(3\), contradicting visibility. Hence \(3\nmid b_n\). The same argument gives \(3\nmid a_{n+1}\).

Let \(p=\operatorname{lpf}(b_n)\). By Lemma 1,
\[
d_n<\rho_{b_n}(a_n)\le p-1.
\]
Thus \(d_n\le p-2\). Since \(d_n\) is even and \(p-2\) is odd, in fact \(d_n\le p-3\). The vertical estimate is identical. ∎

This rules out anchors having small least prime factor whenever the opposite increment is long.

---

### 3. Arbitrarily long finite composite-anchor staircases

The following shows that there is no finite local obstruction to Route 2.

#### Theorem 3
For every \(r\ge1\), there exists a monotone admissible path consisting of \(r\) successive L-shaped composite-anchor connectors
\[
(a_n,b_n)\longrightarrow(a_{n+1},b_n)
\longrightarrow(a_{n+1},b_{n+1}),
\qquad 0\le n<r.
\]

All anchors may be chosen odd, composite, and with arbitrarily large least prime factor.

#### Proof

Set
\[
M=2r+4
\]
and let
\[
Q=\prod_{p\le M}p,
\]
the product being over primes. Put
\[
D=(M-1)Q,
\]
and choose an integer \(L>D\).

Consider the offsets
\[
s_i=iQ,\qquad 0\le i<M.
\]

For every prime \(\ell\le L\), choose a residue \(u_\ell\pmod\ell\) such that
\[
u_\ell+s_i\not\equiv0\pmod\ell
\qquad(0\le i<M).
\]
Such a residue exists:

- If \(\ell\le M\), then \(\ell\mid Q\), so all \(s_i\equiv0\pmod\ell\); take \(u_\ell=1\).
- If \(M<\ell\le L\), then \(Q\) is invertible modulo \(\ell\), and the \(M\) residues \(s_i\pmod\ell\) are distinct. Since \(M<\ell\), they do not exhaust all residue classes, so some \(u_\ell\) avoids all their negatives.

Next choose distinct primes
\[
q_0,\dots,q_{M-1}>L.
\]
The Chinese remainder theorem gives an integer \(N\) satisfying simultaneously
\[
N\equiv u_\ell\pmod\ell\qquad(\ell\le L,\ \ell\text{ prime})
\]
and
\[
N\equiv-s_i\pmod{q_i}\qquad(0\le i<M).
\]
By adding a sufficiently large multiple of the combined modulus, assume
\[
N+s_i>q_i
\]
for every \(i\).

Define
\[
c_i=N+s_i=N+iQ.
\]
Then:

- \(q_i\mid c_i\) and \(c_i>q_i\), so \(c_i\) is composite;
- no prime \(\ell\le L\) divides \(c_i\), by the choice of \(u_\ell\);
- hence
  \[
  \operatorname{lpf}(c_i)>L;
  \]
- since \(2\le L\), all \(c_i\) are odd;
- and
  \[
  0<c_j-c_i\le D<L
  \qquad(i<j).
  \]

Now define
\[
a_n=c_{2n}\qquad(0\le n\le r)
\]
and
\[
b_n=c_{2n+3}\qquad(0\le n\le r).
\]
For each \(0\le n<r\), traverse
\[
(c_{2n},c_{2n+3})
\longrightarrow
(c_{2n+2},c_{2n+3})
\longrightarrow
(c_{2n+2},c_{2n+5}).
\]

Consider a point \((t,c_{2n+3})\) on the horizontal segment. We have
\[
c_{2n}\le t\le c_{2n+2}<c_{2n+3}.
\]
If \(g=\gcd(t,c_{2n+3})>1\), some prime \(p\mid g\) divides the nonzero difference
\[
c_{2n+3}-t.
\]
But
\[
0<c_{2n+3}-t<D<L<p,
\]
because every prime factor of \(c_{2n+3}\) exceeds \(L\). This is impossible. Hence every point on the horizontal segment is visible.

Similarly, on the vertical segment,
\[
c_{2n+3}\le t\le c_{2n+5}
\]
and the fixed coordinate is \(c_{2n+2}<t\). A common prime divisor would exceed \(L\) while dividing the positive difference
\[
t-c_{2n+2}<L,
\]
again impossible.

Every horizontal segment has fixed composite coordinate \(c_{2n+3}\), and every vertical segment has fixed composite coordinate \(c_{2n+2}\). Thus every visited point satisfies the compositeness disjunction. All coordinates exceed \(1\), and the path is monotone, hence simple. ∎

#### Limitation
The starting vertex depends on \(r\). The theorem therefore establishes arbitrarily long paths somewhere in \(H\), not paths of arbitrary length from one fixed root. It cannot by itself invoke König’s lemma.

---

### 4. Prime-square anchors cannot work

A particularly natural attempt is
\[
a_n=p_n^2,\qquad b_n=q_n^2
\]
for strictly increasing odd primes \(p_n,q_n\). This fails immediately.

#### Proposition 4
There is no Route 2 connector
\[
(p_n^2,q_n^2)\to(p_{n+1}^2,q_n^2)
\to(p_{n+1}^2,q_{n+1}^2)
\]
with both prime sequences strictly increasing.

#### Proof
The horizontal visibility condition and Lemma 2 imply
\[
p_{n+1}^2-p_n^2<q_n.
\]
But distinct odd primes differ by at least \(2\), so
\[
p_{n+1}^2-p_n^2
=(p_{n+1}-p_n)(p_{n+1}+p_n)>p_{n+1}.
\]
Consequently,
\[
q_n>p_{n+1}.
\]

On the other hand, vertical visibility gives
\[
q_{n+1}^2-q_n^2<p_{n+1}.
\]
Again,
\[
q_{n+1}^2-q_n^2>q_n,
\]
so
\[
p_{n+1}>q_n.
\]
This is a contradiction. ∎

Thus prime squares, despite their large least prime factors, are too sparsely spaced in both coordinates simultaneously.

---

### 5. A restriction on periodic staircases

One possible way to turn a finite template into a ray would be to repeat it after diagonal translation.

#### Proposition 5
Suppose that, after some initial part, a Route 2 staircase is periodic in the sense that for some \(m,T>0\),
\[
a_{n+m}=a_n+T,\qquad b_{n+m}=b_n+T.
\]
Then \(m\ge3\).

#### Proof
All recurrent anchors are odd by Lemma 2. Since both \(b_n\) and \(b_n+T\) are odd, \(T\) is even.

Fix one phase \(j\). Every number
\[
b_j+kT,\qquad k\ge0,
\]
is composite. If \(\gcd(b_j,T)=1\), Dirichlet’s theorem on primes in arithmetic progressions would imply that this progression contains infinitely many primes, a contradiction. Hence
\[
\gcd(b_j,T)>1.
\]
Because \(b_j\) is odd and \(T\) is even, there is an odd prime
\[
q_j\mid \gcd(b_j,T).
\]
The horizontal segment at phase \(j\), of length
\[
d_j=a_{j+1}-a_j,
\]
must avoid multiples of \(q_j\). Therefore, by Lemma 1,
\[
d_j<q_j.
\]
Since \(q_j\) is an odd prime divisor of the even number \(T\),
\[
q_j\le \frac T2.
\]
Thus
\[
d_j<\frac T2.
\]

Over a full period,
\[
\sum_{j=0}^{m-1}d_j=T.
\]
If \(m=1\), this is impossible because \(d_0<T/2\). If \(m=2\), then
\[
d_0+d_1<T,
\]
again impossible. Hence \(m\ge3\). ∎

This does not exclude longer periodic templates, but it eliminates the simplest one- and two-phase constructions.

---

### 6. A finite-state certificate that would solve the problem

A related alternative emerged from the analysis. It is not restricted to composite fixed coordinates, but it would give a stronger monotone ray.

Fix \(C\ge2\) and let
\[
T=\prod_{p\le C}p.
\]
Represent a point above the diagonal as
\[
(x,x+\delta),\qquad 1\le\delta\le C,
\]
and reduce \(x\) modulo \(T\). Call \((x,\delta)\) robustly admissible if
\[
\gcd(x,\delta)=1
\]
and
\[
\gcd(x,T)>1\quad\text{or}\quad \gcd(x+\delta,T)>1.
\]

Use directed edges
\[
(x,\delta)\to(x,\delta+1)
\]
for north steps and
\[
(x,\delta)\to(x+1,\delta-1)
\]
for east steps, whenever the target is robustly admissible.

#### Lemma 6
A directed cycle in this finite state graph produces a monotone admissible ray in \(H\).

#### Proof
Every prime divisor of \(\delta\le C\) divides \(T\). Hence for every integer \(k\),
\[
\gcd(x+kT,x+kT+\delta)
=\gcd(x+kT,\delta)
=\gcd(x,\delta)=1.
\]
Thus visibility persists under diagonal translation by \(T\).

If \(\gcd(x,T)>1\), some prime \(p\mid T\) divides every \(x+kT\); after choosing the initial translate sufficiently large, that coordinate is composite. The same applies to \(x+\delta\) if \(\gcd(x+\delta,T)>1\).

On a directed cycle, the number of north and east moves is equal because \(\delta\) returns to its initial value. The number of east moves is a positive multiple of \(T\), because \(x\bmod T\) also returns. Therefore one traversal translates the actual path by \((sT,sT)\) for some \(s\ge1\). Repeating it gives a monotone simple admissible ray. ∎

I have not established that such a cycle exists.

## Self-Audit

1. **The CRT theorem only gives paths with varying roots.**  
   This is the central deficiency, not a cosmetic issue. Arbitrarily long components or paths do not imply a ray. The theorem is nevertheless correct because every finite path is certified uniformly by explicit congruences and least-prime-factor bounds.

2. **Proposition 5 uses Dirichlet’s theorem.**  
   This is the strongest external input. Its application is standard: a progression with positive modulus and coprime initial residue contains infinitely many primes. The proposition is only an obstruction to simple periodic constructions and is not used to claim a solution.

3. **The finite-state cycle criterion guarantees compositeness only after a sufficiently large diagonal translate.**  
   This is enough: a common prime divisor of the coordinate and \(T\) persists under every translation, and choosing the first lift larger than all primes dividing \(T\) makes that coordinate genuinely composite rather than equal to a prime. No unproved cycle-existence claim is being made.

## Computations To Verify

### 1. Verify the CRT finite staircase construction

```python
from math import gcd, prod
from sympy import primerange, nextprime
from sympy.ntheory.modular import crt
from sympy import isprime

def allowed(x, y):
    return (
        x >= 2 and y >= 2
        and gcd(x, y) == 1
        and not (isprime(x) and isprime(y))
    )

def crt_staircase(r):
    # Need c_0,...,c_{M-1}.
    M = 2*r + 4
    small_primes = list(primerange(2, M + 1))
    Q = prod(small_primes)
    offsets = [i*Q for i in range(M)]

    D = offsets[-1] - offsets[0]
    L = D + 1

    moduli = []
    residues = []

    # Avoid every prime <= L at every offset.
    for ell in primerange(2, L + 1):
        bad = {(-s) % ell for s in offsets}
        u = next(a for a in range(ell) if a not in bad)
        moduli.append(ell)
        residues.append(u)

    # Give each c_i an explicit prime factor q_i > L.
    qs = []
    z = L
    for i in range(M):
        z = int(nextprime(z))
        qs.append(z)
        moduli.append(z)
        residues.append((-offsets[i]) % z)

    N0, total_modulus = crt(moduli, residues)
    N = int(N0)
    total_modulus = int(total_modulus)

    target = max(qs) + 10
    if N <= target:
        N += ((target - N) // total_modulus + 1) * total_modulus

    c = [N + s for s in offsets]

    # Arithmetic certificates.
    for i, ci in enumerate(c):
        assert ci % qs[i] == 0
        assert ci > qs[i]
        assert not isprime(ci)
        for ell in primerange(2, L + 1):
            assert ci % ell != 0

    # Build the path.
    path = [(c[0], c[3])]
    for n in range(r):
        for x in range(c[2*n] + 1, c[2*n + 2] + 1):
            path.append((x, c[2*n + 3]))
        for y in range(c[2*n + 3] + 1, c[2*n + 5] + 1):
            path.append((c[2*n + 2], y))

    assert len(path) == len(set(path))
    for v in path:
        assert allowed(*v)
    for u, v in zip(path, path[1:]):
        assert abs(u[0] - v[0]) + abs(u[1] - v[1]) == 1

    return c, qs, path
```

Suggested first checks: `r = 1, 2, 3`. The integers grow rapidly, but the proof does not require complete factorization.

---

### 2. Exhaustive Route 2 transition search in a finite box

```python
from math import gcd
from sympy import isprime

def anchor(n):
    return n > 1 and not isprime(n)

def safe_interval(lo, hi, fixed):
    return all(gcd(t, fixed) == 1 for t in range(lo, hi + 1))

def route2_transitions(B):
    anchors = [n for n in range(2, B + 1) if anchor(n)]
    states = [
        (a, b) for a in anchors for b in anchors
        if gcd(a, b) == 1
    ]

    out = {s: [] for s in states}

    for a, b in states:
        for ap in anchors:
            if ap <= a:
                continue
            if not safe_interval(a, ap, b):
                continue

            for bp in anchors:
                if bp <= b:
                    continue
                if not safe_interval(b, bp, ap):
                    continue
                out[(a, b)].append((ap, bp))

    return out
```

For each fixed root, compute directed reachability and longest depth before hitting the boundary. Record:

- least prime factors of successful anchors;
- the values of \(\rho_b(a)\) and \(\rho_{a'}(b)\);
- whether long paths remain in a bounded strip \(|a-b|\le C\);
- whether states appear to repeat modulo a possible translation.

---

### 3. Search for a robust periodic cycle

```python
from math import gcd, prod
from sympy import primerange
import networkx as nx

def robust_cycle(C):
    T = prod(primerange(2, C + 1))

    def good(x, delta):
        return (
            1 <= delta <= C
            and gcd(x, delta) == 1
            and (gcd(x, T) > 1 or gcd((x + delta) % T, T) > 1)
        )

    G = nx.DiGraph()

    for x in range(T):
        for d in range(1, C + 1):
            if good(x, d):
                G.add_node((x, d))

    for x, d in list(G.nodes):
        # North
        if d < C and good(x, d + 1):
            G.add_edge((x, d), (x, d + 1), move="N")

        # East
        xp = (x + 1) % T
        if d > 1 and good(xp, d - 1):
            G.add_edge((x, d), (xp, d - 1), move="E")

    for S in nx.strongly_connected_components(G):
        H = G.subgraph(S)
        if len(S) > 1:
            cycle = nx.find_cycle(H, orientation="original")
            return T, cycle

    return T, None

for C in range(2, 14):
    T, cycle = robust_cycle(C)
    print(C, T, cycle is not None)
```

Any returned cycle should then be lifted to actual coordinates and checked directly. Because \(T\) grows as a primorial, a more efficient implementation should generate states lazily and use a custom SCC search.

## Route Diagnosis

### Proved ledger

- Exact first-obstruction formula \(d<\rho_m(s)\) for traversable intervals.
- Recurrent composite anchors must be odd and coprime to \(6\).
- Segment lengths are bounded by the least prime factor of the fixed anchor.
- Arbitrarily long finite monotone Route 2 staircases exist by CRT.
- Prime-square anchors cannot support even one full increasing connector.
- A diagonally periodic Route 2 staircase cannot have only one or two connectors per period.
- A finite robust-state cycle would give a complete monotone solution.

### Plausible but unproved

- A periodic template with at least three phases may exist.
- The robust finite-state graph may contain a directed cycle for some moderate strip width \(C\).
- A branching argument may allow one to avoid states where the two short rough-composite windows are simultaneously empty.

### Dead ends

- **Prime powers / prime squares:** their gaps are already larger than the least prime factor needed to protect the opposite segment.
- **Naive CRT induction:** CRT can create an excellent finite block, but its solution spacing is roughly a product of many primes. A previously fixed anchor permits movement only up to its first forbidden residue, far too short to jump to a newly manufactured CRT block.
- **Arbitrarily long unrooted paths:** Theorem 3 falls exactly into the compactness trap identified in the brief; the roots vary.

### Precise block

Given a prescribed visible composite-anchor state \((a,b)\), Route 2 requires a composite \(a'\) before the first integer sharing a prime factor with \(b\), and then a composite \(b'\) before the first integer sharing a prime factor with \(a'\):
\[
a<a'<a+\rho_b(a),\qquad
b<b'<b+\rho_{a'}(b).
\]
Both \(a'\) and \(b'\) must themselves have sufficiently favorable prime factors for later continuation. CRT proves that arbitrarily long compatible finite configurations exist when the entire configuration may be chosen at once, but it gives no control after the initial state is fixed. Establishing such rooted extensions is essentially the unresolved global problem.

A fresh attempt should first run the robust-cycle search and a dedicated SAT search for a diagonally periodic Route 2 template with at least three phases. A finite successful template would be a complete, checkable proof; repeated failure should be analyzed for a modular invariant before returning to nonperiodic sieve methods.