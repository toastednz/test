STATUS: BLOCKED

## Result

I did not solve Erdős Problem #1212. I proved that the literal local-repair version of Route 1 cannot work: immediate neighbors of a prime-prime corner force backward motion, twin prime gaps can create isolated Stewart-segment vertices, and a natural \(2\times2\) detour already fails at the genuine consecutive-prime triple \(19,23,29\). More substantially, for every fixed radius \(R\), there are comparable odd primes \(p<q<\tfrac32p\) for which no admissible path inside the radius-\(R\) box can connect the south and east arms of \((p,q)\). Thus no absolute-radius detour theorem, and no finite catalogue of bounded local templates, can repair arbitrary prime-prime corners. This does not rule out detours specialized to consecutive-prime pairs or grouped repairs spanning several Stewart cells; that is the precise unresolved block.

## Complete Argument

### 1. Parity forces the geometry of every detour

**Lemma 1.** Let \((x,y)\in V\).

1. If \(y\) is even, then \((x,y)\) has no horizontal neighbor in \(V\).
2. If \(x\) is even, then \((x,y)\) has no vertical neighbor in \(V\).
3. Consequently, a path can change direction only at a vertex with both coordinates odd.

**Proof.** If \(y\) is even and \(\gcd(x,y)=1\), then \(x\) is odd. Both \(x-1\) and \(x+1\) are even, so whenever positive,
\[
\gcd(x\pm1,y)\ge 2.
\]
Thus neither horizontal neighbor is visible. The second assertion is symmetric. A turn requires both a horizontal and a vertical incident edge, so neither coordinate can be even. ∎

This makes the immediate geometry around an odd prime-prime point completely rigid.

**Lemma 2 (forced neighbors at a prime corner).** Let \(p,q>2\) be primes, and set
\[
S=(p,q-1),\qquad E=(p+1,q).
\]
Assume \(S,E\in A\). Then:

1. any path in \(H\) leaving \(S\) without using \((p,q)\) must begin
   \[
   (p,q-1)\longrightarrow (p,q-2);
   \]
2. any path in \(H\) arriving at \(E\) without using \((p,q)\) must end
   \[
   (p+2,q)\longrightarrow(p+1,q);
   \]
3. there is no north-east monotone path in \(H\) from \(S\) to \(E\);
4. if \(q-2\) is prime, or if \(p+2\) is prime, then there is no path at all in \(H\) from \(S\) to \(E\).

There is a symmetric statement for
\[
W=(p-1,q),\qquad N=(p,q+1):
\]
any detour must first use \((p-2,q)\) and finally use \((p,q+2)\).

**Proof.** The four possible neighbors of \(S\) are
\[
(p,q),\quad (p,q-2),\quad (p-1,q-1),\quad (p+1,q-1).
\]
The first is forbidden because it is prime-prime. The last two have both coordinates even and are not visible. Hence only \((p,q-2)\) can remain.

Similarly, the neighbors of \(E\) other than \((p,q)\) are
\[
(p+2,q),\quad(p+1,q-1),\quad(p+1,q+1).
\]
The last two are even-even, so only \((p+2,q)\) can be used.

A north-east path from \(S\) to \(E\) has net displacement \((1,1)\), hence exactly two steps. The two possible intermediate vertices are \((p,q)\), which is forbidden, and \((p+1,q-1)\), which is even-even. Thus no such path exists.

If \(q-2\) is prime, then \((p,q-2)\) is either prime-prime or, when \(q-2=p\), is not visible. Thus \(S\) has no admissible exit. The case \(p+2\) prime is symmetric. ∎

Hence a repair cannot literally replace the deleted corner while retaining its two immediate incident arms. It must retreat along both arms, and it necessarily sacrifices local monotonicity unless entry and exit points are changed.

---

### 2. Twin gaps can make Stewart-segment vertices isolated

Write
\[
p=p_k,\qquad r=p_{k+1},\qquad q=p_{k+2}.
\]
For \(k\ge4\), the Stewart inequality \(q<2p\) ensures that the vertical segment
\[
(p,r),(p,r+1),\ldots,(p,q)
\]
and horizontal segment
\[
(p,q),(p+1,q),\ldots,(r,q)
\]
are visible. Their interior varying coordinates are composite because the relevant primes are consecutive.

**Lemma 3.**

1. If \(q-r=2\), then the sole interior point
   \[
   (p,r+1)
   \]
   of the vertical Stewart segment is an isolated vertex of \(H\).
2. If \(r-p=2\), then the sole interior point
   \[
   (p+1,q)
   \]
   of the horizontal Stewart segment is an isolated vertex of \(H\).

**Proof.** Suppose \(q=r+2\). The point \((p,r+1)\) is visible by the Stewart argument and is admissible because \(r+1\) is even and composite. Its two vertical neighbors are
\[
(p,r),\qquad(p,q),
\]
both forbidden prime-prime points. Its two horizontal neighbors have the form
\[
(p\pm1,r+1),
\]
and both coordinates are even, so they are not visible. Thus its degree in \(H\) is zero.

The horizontal assertion follows by interchanging the coordinates. ∎

Twin gaps cannot occur twice consecutively after \(3\), but this does not rescue a pointwise repair.

**Lemma 4.** If \(p_i>3\), then it is impossible that
\[
p_{i+1}-p_i=p_{i+2}-p_{i+1}=2.
\]

**Proof.** Among \(p_i,p_i+2,p_i+4\), exactly one is divisible by \(3\). If all three were primes larger than \(3\), that would be impossible. ∎

Thus twin cells can be grouped with neighboring non-twin cells, but any valid repair theorem must explicitly do this.

---

### 3. A positive bounded template and an actual failure

Suppose \(p<r<q\) are consecutive primes with
\[
r-p\ge4,\qquad q-r\ge4,\qquad q<2p.
\]
Then \(p+2\) and \(q-2\) are odd composites. Consider the five-point path
\[
\begin{aligned}
&(p,q-2),\\
&(p+1,q-2),\\
&(p+2,q-2),\\
&(p+2,q-1),\\
&(p+2,q).
\end{aligned}
\tag{1}
\]

**Lemma 5.** Path (1) lies in \(H\) provided
\[
\gcd(p+1,q-2)=
\gcd(p+2,q-2)=
\gcd(p+2,q-1)=1.
\tag{2}
\]

**Proof.** The endpoints are visible: \(p<q-2<2p\), so the prime \(p\) does not divide \(q-2\), while \(p+2<q\), so the prime \(q\) does not divide \(p+2\). The three other visibility conditions are exactly (2).

Every point is admissible. At the first point \(q-2\) is composite; at the second \(p+1\) is even composite; at the third both coordinates are composite; at the fourth \(q-1\) is even composite; and at the last \(p+2\) is composite. Consecutive listed points differ by one unit. ∎

The coprimality conditions cannot be discarded.

**Example 6.** The consecutive primes
\[
19<23<29
\]
satisfy both gap conditions. The corresponding entry and exit points are
\[
(19,27),\qquad(21,29).
\]
There is no admissible path between them inside
\[
[19,21]\times[27,29].
\]

**Proof.** The relevant points are:

- \((19,27)\), \((19,28)\), \((20,27)\), \((20,29)\), and \((21,29)\), which are admissible;
- \((19,29)\), which is prime-prime;
- \((20,28)\), blocked by \(4\);
- \((21,27)\), blocked by \(3\);
- \((21,28)\), blocked by \(7\).

From \((19,27)\), the only admissible moves within the rectangle lead to \((19,28)\) or \((20,27)\), and both are dead ends within the rectangle. Similarly, \((21,29)\) connects only to the dead end \((20,29)\). Hence the two endpoints are disconnected there. ∎

So even when both adjacent prime gaps are non-twin, the first natural coarse-square repair fails for genuine Stewart data.

---

### 4. Absolute-radius local detours are impossible

The following is the strongest rigorous obstruction obtained.

**Theorem 7 (arbitrarily large locally blocked prime corners).** For every integer \(R\ge1\), there exist odd primes
\[
p<q<\frac32p
\]
such that:

1. the points
   \[
   S=(p,q-1),\qquad E=(p+1,q)
   \]
   belong to \(A\);
2. there is no path in \(H\), contained in
   \[
   Q_R=[p-R,p+R]\times[q-R,q+R],
   \]
   from \(S\) to \(E\).

**Proof.** Let
\[
I_R=\{(a,b):1\le |a|\le R,\ 1\le |b|\le R\}.
\]
For each \((a,b)\in I_R\), choose a distinct odd prime
\[
\ell_{a,b}>R.
\]
Set
\[
M=2\prod_{(a,b)\in I_R}\ell_{a,b}.
\]

By the Chinese remainder theorem there are residue classes \(A_0,B_0\pmod M\) satisfying
\[
A_0\equiv B_0\equiv1\pmod2
\]
and, for every \((a,b)\in I_R\),
\[
A_0\equiv-a\pmod{\ell_{a,b}},
\qquad
B_0\equiv-b\pmod{\ell_{a,b}}.
\tag{3}
\]
Because \(0<|a|,|b|<\ell_{a,b}\), both residues in (3) are nonzero modulo the corresponding prime. Hence
\[
\gcd(A_0,M)=\gcd(B_0,M)=1.
\]

By Dirichlet’s theorem, there are arbitrarily large primes
\[
p\equiv A_0\pmod M.
\]
For the fixed reduced class \(B_0\pmod M\), the prime number theorem in arithmetic progressions gives
\[
\pi(3x/2;M,B_0)-\pi(x;M,B_0)
 \sim \frac{x}{2\varphi(M)\log x}>0.
\]
Choose \(p\) sufficiently large in its prescribed class. Then there is a prime
\[
q\equiv B_0\pmod M,\qquad p<q<\frac32p.
\]
We may also ensure \(p,q>R+2\).

For every off-axis offset \((a,b)\in I_R\), congruences (3) give
\[
\ell_{a,b}\mid p+a,\qquad
\ell_{a,b}\mid q+b.
\]
Therefore
\[
\gcd(p+a,q+b)\ge\ell_{a,b}>1.
\tag{4}
\]
Thus every visible vertex in \(Q_R\) must lie on one of the two central coordinate lines
\[
x=p\quad\text{or}\quad y=q.
\]

The central intersection \((p,q)\) is forbidden because both coordinates are prime. Consequently, the induced graph in \(Q_R\) is contained in the central cross with its intersection removed. Its vertical and horizontal parts are disconnected.

It remains to check that \(S,E\in A\). Since \(p<q<\frac32p\),
\[
p<q-1<2p.
\]
As \(p\) is prime, this implies \(\gcd(p,q-1)=1\). Also \(q-1\) is an even composite. Hence \(S\in A\). Since
\[
p+1<q
\]
and \(q\) is prime, \(\gcd(p+1,q)=1\); moreover \(p+1\) is an even composite, so \(E\in A\).

The two points lie on different arms of the cross, and any path switching arms would have to use either the deleted center or an off-axis point prohibited by (4). Therefore no such path exists in \(Q_R\). ∎

**Corollary 8.** There is no absolute constant \(R\) such that every comparable odd prime-prime corner admits an admissible south-to-east detour inside its radius-\(R\) box. More generally, no finite catalogue of bounded templates can handle every prime-prime pair.

This theorem does **not** produce consecutive primes \(p,q\). It therefore rules out the broad uniform local lemma proposed by Route 1, but not a theorem exploiting the special fact that Stewart corners involve consecutive or next-to-consecutive primes.

---

### 5. A precise grouped-repair target

Let
\[
g_i=p_{i+1}-p_i,\qquad
J=\{i:g_i\ge4\}.
\]
Lemma 4 shows that \(J\) is infinite. For every sufficiently large \(i\in J\), define
\[
c_i=(p_i+2,p_{i+2}).
\]
Because \(p_i+2\) lies strictly between the consecutive primes \(p_i,p_{i+1}\), it is composite. Also
\[
p_i+2<p_{i+2},
\]
so
\[
\gcd(p_i+2,p_{i+2})=1.
\]
Thus \(c_i\in A\), and it lies on the horizontal portion of the \(i\)-th Stewart connector.

Therefore the following would suffice:

> Prove that an infinite subsequence of the vertices \(c_i\) lies in one connected component of \(H\).

That component would be unbounded and hence infinite; local finiteness would then supply a ray. I was unable to prove the required connectivity. The twin-gap analysis shows that connectors must sometimes span several consecutive Stewart cells, while Theorem 7 shows that a proof cannot come from a finite universal library of local prime-corner templates.

---

### 6. A rigorous finite-certificate alternative

The analysis exposed a potentially stronger alternative: search for a path periodic under diagonal translation and force compositeness by fixed divisors.

For a nonzero integer \(d\), let
\[
\operatorname{rad}(d)=\prod_{\ell\mid d}\ell
\]
over its distinct prime divisors.

**Lemma 9 (periodic lifting criterion).** Suppose \(M\ge2\) and
\[
z_0,z_1,\ldots,z_L,\qquad z_j=(a_j,b_j)\in\mathbb Z^2,
\]
satisfy:

1. consecutive \(z_j\) are grid-neighbors;
2. \(z_L=z_0+(M,M)\);
3. \(a_j\ne b_j\);
4. \(\gcd(a_j,b_j)=1\);
5. \(\operatorname{rad}(a_j-b_j)\mid M\);
6. for every \(j\),
   \[
   \gcd(a_j,M)>1\quad\text{or}\quad\gcd(b_j,M)>1.
   \]

Then \(H\) contains a ray.

**Proof.** For every integer \(n\), consider
\[
z_{j,n}=(a_j+nM,b_j+nM).
\]
Let \(d_j=b_j-a_j\ne0\). Any prime divisor \(\ell\) of both coordinates of \(z_{j,n}\) divides their difference \(d_j\). By condition 5, \(\ell\mid M\). Hence
\[
a_j+nM\equiv a_j\pmod\ell.
\]
But condition 4 gives \(\gcd(a_j,d_j)=1\), so \(\ell\nmid a_j\), a contradiction. Thus
\[
\gcd(a_j+nM,b_j+nM)=1
\]
for every \(j,n\).

By condition 6, at least one coordinate is divisible by a fixed prime factor of \(M\). For all sufficiently large \(n\), that coordinate is positive and larger than that prime, hence composite. Taking one common sufficiently large \(n_0\) for the finite list of vertices, every translated vertex with \(n\ge n_0\) belongs to \(A\).

The translated paths concatenate because
\[
z_{L,n}=z_{0,n+1}.
\]
Their union is therefore an unbounded connected subgraph of \(H\). Since \(H\) is locally finite, it contains a ray. ∎

No finite certificate satisfying Lemma 9 was found here. Its existence is an explicit finite-search question and may be a more promising alternative than repairing actual prime corners one at a time.

## Self-Audit

1. **Theorem 7 does not concern consecutive-prime pairs.** This is the principal limitation. Its proof is exact for arbitrary comparable prime pairs, but it does not show that Stewart’s specially structured corners have unbounded detour radius. I have not inferred that stronger claim.

2. **Theorem 7 invokes the prime number theorem in arithmetic progressions.** This is a standard unconditional theorem, and the modulus is fixed once \(R\) is fixed, so the interval count in \((p,3p/2)\) is valid for all sufficiently large \(p\). No unproved short-interval or prime-tuple assertion is being used.

3. **The canonical-port and periodic-certificate sections are reductions, not existence proofs.** Their implications follow directly from coprimality calculations and König’s lemma, but neither the required port connectivity nor a periodic certificate has been established. This is why the status is BLOCKED rather than PARTIAL toward a claimed solution.

## Computations To Verify

```python
from collections import deque
from math import gcd, isqrt

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d <= isqrt(n):
        if n % d == 0:
            return False
        d += 2
    return True

def allowed(x, y):
    return (
        x >= 2 and y >= 2
        and gcd(x, y) == 1
        and not (is_prime(x) and is_prime(y))
    )

def path_in_rect(start, target, rect):
    """rect = (xmin, xmax, ymin, ymax). Returns a path or None."""
    xmin, xmax, ymin, ymax = rect
    if not allowed(*start) or not allowed(*target):
        return None

    parent = {start: None}
    Q = deque([start])

    while Q:
        x, y = Q.popleft()
        if (x, y) == target:
            out = []
            cur = target
            while cur is not None:
                out.append(cur)
                cur = parent[cur]
            return out[::-1]

        for w in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            a, b = w
            if not (xmin <= a <= xmax and ymin <= b <= ymax):
                continue
            if w not in parent and allowed(a, b):
                parent[w] = (x, y)
                Q.append(w)
    return None

# Verify Example 6.
assert allowed(19, 27)
assert allowed(21, 29)
assert path_in_rect(
    (19, 27), (21, 29), (19, 21, 27, 29)
) is None

def min_SE_radius(p, q, Rmax):
    """Immediate south-to-east detour radius around (p,q)."""
    s = (p, q-1)
    t = (p+1, q)
    if not allowed(*s) or not allowed(*t):
        return None
    for R in range(1, Rmax+1):
        rect = (max(2,p-R), p+R, max(2,q-R), q+R)
        path = path_in_rect(s, t, rect)
        if path is not None:
            return R, path
    return None

def sieve(N):
    mark = bytearray(b"\x01") * (N+1)
    mark[:2] = b"\x00\x00"
    for p in range(2, isqrt(N)+1):
        if mark[p]:
            mark[p*p:N+1:p] = b"\x00" * (((N-p*p)//p)+1)
    return [n for n in range(2, N+1) if mark[n]]

def stewart_corner_ports(primes, i):
    """
    p=primes[i], r=primes[i+1], q=primes[i+2].
    Return odd turn-capable ports on the vertical and horizontal arms.
    """
    p, r, q = primes[i:i+3]
    vertical = [
        (p, y) for y in range(r+1, q)
        if y % 2 == 1 and allowed(p, y)
    ]
    horizontal = [
        (x, q) for x in range(p+1, r)
        if x % 2 == 1 and allowed(x, q)
    ]
    return vertical, horizontal

# Suggested experiment:
# for each actual consecutive-prime triple, use multi-source BFS to determine
# the least expanded rectangle connecting vertical to horizontal port sets.
# Twin gaps will make one of these sets empty, so also test blocks of 2 or 3
# consecutive Stewart cells.

# CRT obstruction search for small R; this uses sympy and may become enormous.
def construct_crt_obstruction(R, search_steps=100000):
    from sympy import nextprime, isprime
    from sympy.ntheory.modular import crt

    pairs = [
        (a, b)
        for a in range(-R, R+1) if a != 0
        for b in range(-R, R+1) if b != 0
    ]

    ell = R + 1
    moduli = [2]
    Ares = [1]
    Bres = [1]

    for a, b in pairs:
        ell = int(nextprime(ell))
        moduli.append(ell)
        Ares.append((-a) % ell)
        Bres.append((-b) % ell)

    A, M = crt(moduli, Ares)
    B, _ = crt(moduli, Bres)
    A, B, M = int(A % M), int(B % M), int(M)

    # Search p=A mod M and q=B mod M with p<q<3p/2.
    for kp in range(1, search_steps+1):
        p = A + kp*M
        if p <= 2*R+3 or not isprime(p):
            continue

        kmin = (p - B)//M + 1
        kmax = ((3*p - 1)//2 - B)//M
        for kq in range(max(0, kmin), kmax+1):
            q = B + kq*M
            if not isprime(q):
                continue

            assert allowed(p, q-1)
            assert allowed(p+1, q)
            for a, b in pairs:
                assert gcd(p+a, q+b) > 1
            assert path_in_rect(
                (p, q-1), (p+1, q),
                (p-R, p+R, q-R, q+R)
            ) is None
            return p, q, M
    return None

def prime_factors(n):
    n = abs(n)
    out = set()
    d = 2
    while d*d <= n:
        if n % d == 0:
            out.add(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out

def periodic_certified(a, b, M):
    d = a - b
    if d == 0 or gcd(abs(a), abs(b)) != 1:
        return False
    if any(M % p != 0 for p in prime_factors(d)):
        return False
    return gcd(abs(a), M) > 1 or gcd(abs(b), M) > 1

def search_monotone_periodic_certificate(M, D):
    """
    Search for Lemma 9 certificates using only east/north steps,
    with |x-y| <= D. Try M=30, 210, 2310 and increasing D.
    """
    for a0 in range(M):
        for d0 in range(-D, D+1):
            if d0 == 0:
                continue
            b0 = a0 + d0
            start = (a0, b0)
            target = (a0+M, b0+M)

            if not periodic_certified(*start, M):
                continue

            parent = {start: None}
            Q = deque([start])

            while Q:
                x, y = Q.popleft()
                if (x, y) == target:
                    path = []
                    cur = target
                    while cur is not None:
                        path.append(cur)
                        cur = parent[cur]
                    return path[::-1]

                for w in ((x+1, y), (x, y+1)):
                    u, v = w
                    if u > target[0] or v > target[1]:
                        continue
                    if abs(u-v) > D:
                        continue
                    if w not in parent and periodic_certified(u, v, M):
                        parent[w] = (x, y)
                        Q.append(w)
    return None
```

The most informative Route 1 experiment is not the immediate-arm search—twin gaps often make that trivially impossible—but a grouped search connecting all turn-capable ports across two or three consecutive Stewart cells. The periodic-certificate search is a concrete test of the alternative supplied by Lemma 9.

## Route Diagnosis

**Proved ledger**

- Parity forces straight motion whenever one coordinate is even.
- Immediate south/east or west/north neighbors of a prime-prime point cannot be joined monotonically and have forced outward neighbors.
- Twin Stewart gaps produce isolated interior vertices.
- Consecutive twin gaps cannot occur beyond \(3,5,7\).
- A natural \(2\times2\) coarse detour has explicit coprimality conditions and fails for \(19,23,29\).
- Absolute-radius detours for arbitrary comparable prime pairs are impossible by CRT plus primes in arithmetic progressions.
- A finite diagonal-periodic certificate satisfying Lemma 9 would give a ray.

**Plausible but unproved**

- Grouped detours spanning a bounded number of consecutive Stewart cells might exploit the prohibition on consecutive twin gaps.
- Actual consecutive-prime corners may have substantially better detour behavior than arbitrary prime pairs.
- A periodic modular certificate may exist for a primorial modulus such as \(210\) or \(2310\).

**Dead ends**

- One-cell square detours: destroyed by even-even corners.
- Literal replacement of each forbidden Stewart vertex: immediate arms can be isolated.
- The first coarse \(2\times2\) template: defeated by ordinary gcd obstructions.
- Any fixed finite library of bounded templates for arbitrary prime pairs: ruled out by Theorem 7.

**Precise block**

Route 1 now requires a theorem specific to the sequence of consecutive primes: one must connect an unbounded sequence of turn-capable Stewart ports while grouping twin-gap cells and controlling gcd obstructions in rectangles whose required size may grow. No known elementary property of consecutive primes supplies that connectivity, and replacing it by “there is always some sufficiently large detour” is essentially the original infinite-component problem.

A fresh attempt should either:

1. computationally classify grouped detours for actual consecutive-prime triples and look for a finite-state invariant unavailable to the CRT counterexamples; or
2. abandon prime-corner repair and search directly for a finite periodic certificate under Lemma 9, thereby forcing compositeness by congruences and eliminating primality from the path verification altogether.