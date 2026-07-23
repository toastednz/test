STATUS: BLOCKED

## Result

Route 3 yields a strong unconditional finite-scale result: at every prescribed scale, a positive density of translated boxes contain explicit connected meshes of admissible horizontal and vertical crossings, with arbitrarily many ports and disjoint crossings. This follows from a finite gcd-pattern sieve combined with CRT-enforced composite row and column anchors. However, these good boxes are unrooted and need not concatenate. Conversely, CRT constructs arbitrarily large translated boxes containing no visible point at all, so no uniform all-translates crossing theorem is possible. Positive density—even density arbitrarily close to one—does not force an infinite connected chain in a deterministic planar environment. Thus the route remains blocked precisely at a rooted or compatible block-extension theorem, which is essentially comparable in strength to the original problem.

## Complete Argument

### 1. Reduction to a coarse graph on odd-odd junctions

Let
\[
J=\{(x,y)\in A:x,y\text{ are odd}\}.
\]
Define a graph \(K\) on \(J\) by joining \((x,y)\) to \((x+2,y)\) when the midpoint \((x+1,y)\) is visible, and similarly joining \((x,y)\) to \((x,y+2)\) when \((x,y+1)\) is visible.

#### Lemma 1
The graph \(H\) has an infinite component if and only if \(K\) has an infinite component.

#### Proof
A horizontal edge of \(H\) can only lie in an odd row. Indeed, if \(y\) is even, then among two consecutive \(x\)-coordinates one is even, so one endpoint has both coordinates even and is not visible. Similarly, a vertical edge can only lie in an odd column.

Consequently:

- a visible vertex with even \(x\) and odd \(y\) has only horizontal incident edges;
- a visible vertex with odd \(x\) and even \(y\) has only vertical incident edges;
- a path can turn only at an odd-odd vertex.

Thus every even-coordinate vertex of \(H\) is merely a possible subdivision vertex between two odd-odd vertices distance two apart, or is a leaf or isolated vertex. The midpoint of two odd-odd vertices has an even coordinate at least \(4\), so if it is visible it is automatically admissible.

Compressing every two-edge collinear segment through an even-coordinate vertex therefore gives a walk in \(K\). Conversely, every edge of \(K\) expands to a two-edge path in \(H\).

If an \(H\)-component contained only finitely many odd-odd vertices, it would be finite because each such vertex has degree at most four and every remaining vertex is adjacent to one of them. Hence an infinite \(H\)-component produces an infinite \(K\)-component. The converse follows by expanding edges. ∎

This reduction isolates the real turning vertices: odd coprime pairs at which at least one coordinate is an odd composite.

---

### 2. A finite gcd-pattern sieve

The following elementary sieve is the main arithmetic tool behind the block construction.

#### Lemma 2
Let
\[
\mathcal D=\{(a_s,b_s):1\le s\le S\}\subset\mathbb Z^2
\]
be finite. Let \(M\) be squarefree, and prescribe residues
\[
X\equiv A\pmod M,\qquad Y\equiv B\pmod M
\]
such that
\[
\gcd(A+a_s,B+b_s,M)=1
\]
in the prime-by-prime sense: no prime \(p\mid M\) divides both \(A+a_s\) and \(B+b_s\).

For \(p\nmid M\), let
\[
\nu(p)=\#\{(-a_s,-b_s)\pmod p:1\le s\le S\}.
\]
If \(\nu(p)<p^2\) for every \(p\nmid M\), then the set of positive pairs \((X,Y)\) satisfying the prescribed congruences and
\[
\gcd(X+a_s,Y+b_s)=1\qquad(1\le s\le S)
\]
has natural density
\[
\frac1{M^2}\prod_{p\nmid M}\left(1-\frac{\nu(p)}{p^2}\right)>0.
\]

#### Proof
For a finite set of primes \(p\le z\), \(p\nmid M\), the Chinese remainder theorem gives density
\[
\frac1{M^2}
\prod_{\substack{p\le z\\p\nmid M}}
\left(1-\frac{\nu(p)}{p^2}\right).
\]

It remains to control primes \(p>z\). For one offset pair \((a_s,b_s)\), the number of \(1\le X,Y\le N\) for which some \(p>z\) divides both \(X+a_s\) and \(Y+b_s\) is at most
\[
\sum_{z<p\le N+O(1)}
\left(\frac Np+O(1)\right)^2.
\]
Bounding the sum over primes by the sum over all integers gives
\[
O\left(
N^2\sum_{n>z}\frac1{n^2}
+N\sum_{n\le N}\frac1n
+N
\right)
=
O\left(\frac{N^2}{z}+N\log N\right).
\]
After summing over the finitely many offsets and dividing by \(N^2\), the upper density of pairs affected by a prime \(p>z\) is \(O_{\mathcal D}(1/z)\).

Letting first \(N\to\infty\) and then \(z\to\infty\) proves the density formula. Since \(\nu(p)\le S\), the Euler product converges to a positive number once all local factors are positive. ∎

---

### 3. Local density and edge density

Lemma 2 gives exact local statistics.

For horizontal visible edges, the relevant conditions are
\[
\gcd(x,y)=\gcd(x+1,y)=1.
\]
Modulo every prime \(p\), exactly two pairs of residues are forbidden:
\[
y\equiv0,\qquad x\equiv0\text{ or }-1\pmod p.
\]
Hence the number of horizontal edges in \([2,N]^2\), before deleting prime-prime endpoints, is
\[
\left(C_2+o(1)\right)N^2,
\qquad
C_2=\prod_p\left(1-\frac2{p^2}\right).
\]
Deleting prime-prime vertices removes only \(o(N^2)\) edges, because there are \(O(N^2/\log^2N)\) such vertices and each has degree at most four. The same asymptotic therefore holds in \(H\).

Similarly,
\[
|A\cap[2,N]^2|
=
\left(\frac6{\pi^2}+o(1)\right)N^2.
\]
Thus the average degree in \(H[2,N]^2\) tends to
\[
\frac{4C_2}{6/\pi^2},
\]
numerically about \(2.12\).

For the coarse graph \(K\), a horizontal coarse edge requires
\[
\gcd\bigl(y,x(x+1)(x+2)\bigr)=1,
\]
with \(x,y\) odd. For every odd prime \(p\), exactly three residue pairs are forbidden. Relative to the odd lattice, the coarse horizontal-edge density is therefore
\[
C_3=\prod_{p\text{ odd}}\left(1-\frac3{p^2}\right),
\]
while the coarse vertex density, before the zero-density prime-prime deletion, is
\[
\prod_{p\text{ odd}}\left(1-\frac1{p^2}\right)=\frac8{\pi^2}.
\]

These statistics support a percolation analogy but do not imply an infinite component.

---

### 4. Positive-density robust block crossings

For \(R\ge1\), let \(I=\{0,1,\ldots,R\}\). Let \(U,V\subseteq I\). For a translation \((X,Y)\), define the mesh
\[
\Sigma_{X,Y}(U,V)
=
\bigcup_{v\in V}\{(X+t,Y+v):t\in I\}
\;\cup\;
\bigcup_{u\in U}\{(X+u,Y+s):s\in I\}.
\]

Thus each \(v\in V\) gives a complete left-right row crossing, and each \(u\in U\) gives a complete bottom-top column crossing.

#### Theorem 3: Robust arithmetic mesh theorem
Suppose that for every prime \(r\le R+1\),
\[
U\bmod r\ne\mathbb Z/r\mathbb Z,
\qquad
V\bmod r\ne\mathbb Z/r\mathbb Z.
\]
Then a positive natural density of translations \((X,Y)\) have the following properties:

1. every point of \(\Sigma_{X,Y}(U,V)\) belongs to \(A\);
2. each fixed column \(X+u\), \(u\in U\), is composite;
3. each fixed row \(Y+v\), \(v\in V\), is composite.

Consequently, the box \([X,X+R]\times[Y,Y+R]\) contains \(|V|\) vertex-disjoint left-right admissible crossings and \(|U|\) vertex-disjoint bottom-top admissible crossings, all belonging to one connected mesh.

#### Proof

For each \(v\in V\), choose a distinct prime
\[
P_v>R+1.
\]
For each \(u\in U\), choose a distinct prime
\[
Q_u>R+1,
\]
with all \(P_v,Q_u\) mutually distinct.

We impose congruences as follows.

**Small primes.**  
For every prime \(r\le R+1\), choose
\[
\alpha_r\notin -U\pmod r,
\qquad
\beta_r\notin -V\pmod r,
\]
which is possible by hypothesis, and impose
\[
X\equiv\alpha_r\pmod r,\qquad
Y\equiv\beta_r\pmod r.
\]
Thus no fixed column \(X+u\) and no fixed row \(Y+v\) is divisible by \(r\).

**Row-forcing primes.**  
For each \(v\in V\), impose
\[
Y\equiv-v\pmod{P_v}.
\]
Also choose \(A_v\pmod{P_v}\) outside
\[
-I=\{0,-1,\ldots,-R\}\pmod{P_v}
\]
and impose
\[
X\equiv A_v\pmod{P_v}.
\]
This is possible because \(P_v>R+1\). Hence \(P_v\mid Y+v\), but \(P_v\nmid X+t\) for every \(t\in I\).

If \(v'\ne v\), then
\[
0<|v'-v|\le R<P_v,
\]
so \(P_v\nmid Y+v'\). Also, because \(U\subseteq I\), \(P_v\) divides no fixed column.

**Column-forcing primes.**  
Symmetrically, for each \(u\in U\), impose
\[
X\equiv-u\pmod{Q_u}
\]
and choose
\[
Y\pmod{Q_u}
\]
outside \(-I\).

All these moduli are pairwise coprime, so the CRT gives a residue pair
\[
X\equiv X_0\pmod M,\qquad Y\equiv Y_0\pmod M
\]
for their product \(M\).

Every prime dividing \(M\) is now locally harmless for all pairs in the mesh. For a prime \(r\nmid M\), necessarily \(r>R+1\). The forbidden residue pairs are contained in
\[
(-I)\times(-V)\;\cup\;(-U)\times(-I).
\]
This set is not all of \((\mathbb Z/r\mathbb Z)^2\): choose both residues outside \(-I\), which is possible because \(|I|=R+1<r\).

Lemma 2 therefore shows that a positive density of pairs in the prescribed class satisfy
\[
\gcd(X+t,Y+v)=1
\quad(t\in I,\ v\in V),
\]
and
\[
\gcd(X+u,Y+s)=1
\quad(u\in U,\ s\in I).
\]

For sufficiently large such translations, every \(Y+v\) is a multiple of \(P_v\) strictly larger than \(P_v\), and is therefore composite. Similarly every \(X+u\) is composite. Hence all mesh points are admissible. The claimed crossings are the full rows and columns of the mesh. ∎

#### Corollary 4
For every \(R\), a positive density of \(R\times R\) translated boxes contain an admissible horizontal and vertical crossing.

Take \(U=V=\{0\}\), or singleton interior offsets if a central cross is desired.

#### Corollary 5
For every \(k\), a positive density of boxes contain \(k\) disjoint horizontal and \(k\) disjoint vertical admissible crossings in one connected mesh.

Let
\[
W=\prod_{\substack{p\le k\\p\text{ prime}}}p,
\qquad
R=kW,
\qquad
U=V=\{0,W,\ldots,(k-1)W\}.
\]
If \(r\le k\), then every element of \(U\) is \(0\pmod r\), so \(U\) does not cover all residues modulo \(r\). If \(k<r\le R+1\), then \(|U|=k<r\), so again it cannot cover all residue classes. Theorem 3 applies.

In particular, for every \(R\) there is a positive-density set of roots lying in components of diameter at least \(R\). The root set, however, depends on \(R\).

---

### 5. Arbitrarily large completely blocked boxes

The preceding positive-density theorem cannot be upgraded to a theorem asserting that every sufficiently large translate is good.

#### Lemma 6
For every \(L\) and every lower bound \(B\), there are \(X,Y>B\) such that every point of
\[
\{X,\ldots,X+L-1\}\times\{Y,\ldots,Y+L-1\}
\]
is invisible.

#### Proof
Choose \(L^2\) distinct primes \(p_{ij}\), \(0\le i,j<L\). Impose
\[
X\equiv-i\pmod{p_{ij}},
\qquad
Y\equiv-j\pmod{p_{ij}}
\]
for every \(i,j\). Since all the primes are distinct, the CRT gives simultaneous solutions for \(X\) and \(Y\). Adding sufficiently large multiples of their common product makes \(X,Y>B\).

For every cell,
\[
p_{ij}\mid X+i,\qquad p_{ij}\mid Y+j,
\]
so
\[
\gcd(X+i,Y+j)\ge p_{ij}>1.
\]
Thus the whole square contains no vertex of \(G\), and hence none of \(H\). ∎

The construction is periodic for each fixed \(L\), so such empty \(L\times L\) boxes themselves occur with a positive, though extremely small, density.

---

### 6. The precise concatenation obstruction

Theorem 3 proves the finite-scale crossing statement sought by Route 3 in a strong form. It does not produce a ray for three separate reasons.

1. **The translations depend on the scale.**  
   For each \(R\), the roots lying in large crossed boxes form a different set. There is no fixed root known to belong to such boxes for all \(R\).

2. **Positive density does not imply a connected chain.**  
   In the coarse square lattice, the set
   \[
   \{(m,n):m\not\equiv0\pmod K,\ n\not\equiv0\pmod K\}
   \]
   has density \((1-1/K)^2\), arbitrarily close to one, but all of its connected components are finite \((K-1)\times(K-1)\) squares.

3. **The CRT freedom is lost after fixing a port.**  
   Theorem 3 uses both translation variables freely and imposes new congruences on them. Once a port is prescribed by a previously constructed path, these variables are partially or entirely fixed. Small prime factors can then create genuine local obstructions; for example, an even fixed row admits no horizontal edge.

Thus an additional theorem of the following kind is needed:

> From one of a controlled family of already-reached ports, at least one compatible robust block can be reached farther out, uniformly in the accumulated congruence history.

No such theorem has been established here. Proving it would already give a rooted infinite component by iterating the extension, so it is comparable in force to the original problem.

---

### 7. A finite periodic certificate as an alternative target

The coarse analysis suggests a finite, machine-searchable alternative.

#### Lemma 7: Periodic diagonal certificate
Let \(T\) be even, and let \(P\) be a monotone north-east unit path from
\[
(a,b)\quad\text{to}\quad(a+T,b+T).
\]
For a vertex \((x_i,y_i)\) of \(P\), write \(d_i=y_i-x_i\). Suppose:

1. \(d_i\ne0\);
2. every prime divisor of \(d_i\) divides \(T\);
3. \(\gcd(x_i,d_i)=1\);
4. if \(d_i\) is even, some prime \(p_i\mid T\) divides \(x_i\) or \(y_i\).

Then, after translating \(P\) far enough by \(K(T,T)\), its repeated diagonal translates form a monotone admissible ray.

#### Proof
For every \(k\ge0\),
\[
\gcd(x_i+kT,y_i+kT)
=
\gcd(x_i+kT,d_i).
\]
Any prime dividing \(d_i\) divides \(T\), so
\[
x_i+kT\equiv x_i\pmod p.
\]
Condition 3 therefore proves coprimality for every translate.

If \(d_i\) is odd, the coordinates have opposite parity. Since \(T\) is even, their parities are unchanged by translation, and after a sufficiently large initial translation the even coordinate is at least \(4\), hence composite.

If \(d_i\) is even, condition 4 gives a fixed prime divisor of one coordinate throughout all diagonal translates. A sufficiently large initial translation makes that coordinate strictly larger than its divisor, hence composite.

Finally, monotonicity places one copy inside
\[
[a+KT,a+(K+1)T]\times[b+KT,b+(K+1)T].
\]
Consecutive copies intersect only at the common endpoint, so their concatenation is simple. ∎

A search for such a finite certificate would settle the problem, and in fact its stronger monotone variant.

There is a genuine narrow-strip obstruction.

#### Lemma 8
There is no infinite monotone visible path contained in
\[
1\le y-x\le4.
\]

#### Proof
At a vertex with even \(d=y-x\), visibility implies \(x\) is odd. Between consecutive even-\(d\) vertices there are exactly two steps. If those two steps consist of one north and one east step, then \(x\) increases by one and becomes even at the next even-\(d\) vertex, contradicting visibility. Therefore the steps occur in blocks \(NN\) or \(EE\).

Within the strip, an \(NN\) block is possible only from \(d=2\) to \(d=4\), and an \(EE\) block only from \(d=4\) to \(d=2\). Hence the blocks must alternate.

Starting at \((x,x+2)\), one such four-step portion is
\[
(x,x+2)\to(x,x+3)\to(x,x+4)
\to(x+1,x+4)\to(x+2,x+4).
\]
The two vertices of difference \(3\) require
\[
3\nmid x,\qquad 3\nmid x+1,
\]
so \(x\equiv1\pmod3\). The next four-step portion starts with \(x+2\), and would require \(x+2\equiv1\pmod3\), impossible. ∎

Thus any periodic-certificate search must allow a wider strip.

## Self-Audit

1. **The passage from finite-prime CRT counts to an infinite Euler product is the most technical point.**  
   Large common prime factors could in principle invalidate a naive local-density product. The explicit tail estimate
   \[
   O(N^2/z+N\log N)
   \]
   controls them uniformly, so the sieve lemma does not rely on heuristic independence.

2. **The mesh construction contains many potentially conflicting congruences.**  
   The forcing primes are chosen mutually distinct and larger than the line length. At each such prime, the varying coordinate is explicitly placed outside the entire forbidden interval; at small primes, none of the fixed anchors is divisible. The remaining accidental common factors are exactly what Lemma 2 removes.

3. **Calling the route “blocked” is a diagnosis, not a theorem that Route 3 can never work.**  
   A sufficiently strong arithmetic Peierls estimate or rooted conditional block-extension theorem could revive it. The present method is blocked because all proved statements are unrooted, while the missing compatible-chain statement would itself immediately yield the required ray.

## Computations To Verify

The following code constructs \(H_N\), computes components, and can be adapted for translated-box crossing rates.

```python
from math import gcd
from collections import deque

def prime_table(n):
    isp = [True] * (n + 1)
    if n >= 0:
        isp[0] = False
    if n >= 1:
        isp[1] = False
    p = 2
    while p * p <= n:
        if isp[p]:
            for m in range(p * p, n + 1, p):
                isp[m] = False
        p += 1
    return isp

def allowed(x, y, isp):
    return (
        x >= 2 and y >= 2 and gcd(x, y) == 1
        and (not isp[x] or not isp[y])
    )

def component_data(N):
    isp = prime_table(N)
    V = {
        (x, y)
        for x in range(2, N + 1)
        for y in range(2, N + 1)
        if allowed(x, y, isp)
    }
    seen = set()
    comps = []

    for root in V:
        if root in seen:
            continue
        q = deque([root])
        seen.add(root)
        comp = []
        while q:
            x, y = q.popleft()
            comp.append((x, y))
            for w in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if w in V and w not in seen:
                    seen.add(w)
                    q.append(w)
        comps.append(comp)

    comps.sort(key=len, reverse=True)
    return [len(c) for c in comps], comps
```

The CRT empty-box construction can be checked exactly:

```python
def is_prime_trial(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def next_primes(count, start=2):
    ans = []
    n = max(2, start)
    while len(ans) < count:
        if is_prime_trial(n):
            ans.append(n)
        n += 1
    return ans

def crt(residues, moduli):
    x, M = 0, 1
    for a, m in zip(residues, moduli):
        t = ((a - x) * pow(M, -1, m)) % m
        x += M * t
        M *= m
        x %= M
    return x, M

def empty_box(L, lower_bound=2):
    primes = next_primes(L * L, L + 2)
    mods, rx, ry = [], [], []
    z = 0
    for i in range(L):
        for j in range(L):
            p = primes[z]
            z += 1
            mods.append(p)
            rx.append((-i) % p)
            ry.append((-j) % p)

    X0, M = crt(rx, mods)
    Y0, M2 = crt(ry, mods)
    assert M == M2

    X = X0
    Y = Y0
    while X <= lower_bound:
        X += M
    while Y <= lower_bound:
        Y += M

    assert all(
        gcd(X+i, Y+j) > 1
        for i in range(L)
        for j in range(L)
    )
    return X, Y, M
```

A verifier for the meshes from Theorem 3 is:

```python
def mesh_ok(X, Y, R, U, V, column_factors, row_factors):
    for u, q in zip(U, column_factors):
        if (X + u) % q != 0 or X + u <= q:
            return False
        for s in range(R + 1):
            if gcd(X + u, Y + s) != 1:
                return False

    for v, p in zip(V, row_factors):
        if (Y + v) % p != 0 or Y + v <= p:
            return False
        for t in range(R + 1):
            if gcd(X + t, Y + v) != 1:
                return False

    return True
```

Finally, this dynamic program searches for the sufficient periodic certificates of Lemma 7 in a strip \(1\le y-x\le D\):

```python
from math import gcd

def prime_factors(n):
    n = abs(n)
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out

def certified_state(x, d, T, D):
    if not (1 <= d <= D):
        return False
    if gcd(x, d) != 1:
        return False
    if any(T % p != 0 for p in prime_factors(d)):
        return False
    if d % 2 == 1:
        return T % 2 == 0
    return gcd(x, T) > 1 or gcd(x + d, T) > 1

def search_periodic_certificate(T, D):
    assert T % 2 == 0

    for a in range(T):
        for d0 in range(1, D + 1):
            if not certified_state(a, d0, T, D):
                continue

            parent = {(0, 0): None}

            for total in range(2 * T + 1):
                lo = max(0, total - T)
                hi = min(T, total)
                for e in range(lo, hi + 1):
                    n = total - e
                    if (e, n) not in parent:
                        continue

                    if e < T:
                        ne, nn = e + 1, n
                        x = a + ne
                        d = d0 + nn - ne
                        if certified_state(x, d, T, D):
                            parent.setdefault(
                                (ne, nn), ((e, n), "E")
                            )

                    if n < T:
                        ne, nn = e, n + 1
                        x = a + ne
                        d = d0 + nn - ne
                        if certified_state(x, d, T, D):
                            parent.setdefault(
                                (ne, nn), ((e, n), "N")
                            )

            if (T, T) in parent:
                word = []
                cur = (T, T)
                while cur != (0, 0):
                    prev, step = parent[cur]
                    word.append(step)
                    cur = prev
                word.reverse()
                return {
                    "T": T,
                    "D": D,
                    "x_residue": a,
                    "initial_difference": d0,
                    "word": "".join(word),
                }

    return None

# Suggested tests:
# search_periodic_certificate(30, 6)
# search_periodic_certificate(210, 8)
# search_periodic_certificate(210, 10)
```

A returned certificate must then be independently expanded, diagonally shifted to positive coordinates, and checked against all conditions of Lemma 7.

## Route Diagnosis

**Proved ledger**

- Rays in \(H\) are equivalent to rays in the odd-odd coarse junction graph.
- Exact Euler-product densities exist for visible edges and coarse edges.
- Every finite scale admits a positive density of robust, fully admissible crossing meshes.
- For every \(R\), a positive density of roots lie in components of diameter at least \(R\).
- Arbitrarily large completely invisible translated boxes exist by CRT.
- A finite periodic diagonal certificate would solve the problem.
- No monotone visible ray can remain in the strip \(1\le y-x\le4\).

**Plausible but unproved**

- A wider-strip periodic certificate may exist.
- Robust good boxes may form an infinite compatible chain.
- A rooted frontier with sufficiently many ports may admit a uniform conditional sieve extension.
- Arithmetic dual barriers might have sufficiently small averaged probability for a Peierls-type argument.

**Dead ends**

- Local density or average degree alone cannot imply a ray.
- A uniform crossing theorem for all large translates is false.
- Positive density of good boxes, even near one, does not force deterministic percolation.
- Arbitrarily large unrooted meshes do not permit König’s lemma.
- The narrow diagonal periodic-template approach fails already in width four.

A fresh attempt should either search aggressively for a finite periodic certificate, or replace the unrooted block theorem by a genuinely rooted conditional extension theorem. For Route 3 specifically, the missing ingredient is not another first- or second-moment count of good boxes; it is quantitative control of compatibility after conditioning on a previously reached port and all accumulated congruence information.