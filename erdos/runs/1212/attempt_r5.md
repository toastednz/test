STATUS: BLOCKED

## Result

The proposed staircase does not currently yield a proof. Its crucial corridor assertion is false: even when every column has a visible point on one of two dodge rows, staggered gcd obstructions can form an uncrossable edge wall. More generally, every finite row palette has periodic fully invisible columns, and there are rough semiprime anchor columns for which the very next column is fully invisible throughout the palette. I also prove a stronger Route-5 obstruction: by CRT, for every radius \(L\) one can construct a closed square circuit consisting entirely of gcd-obstructed points and enclosing an admissible vertex. Thus any strategy asserting that sufficiently large arithmetic barriers cannot occur is false. These results do not disprove the existence of a ray, because the constructed barriers trap only specially chosen components.

## Complete Argument

### 1. Both coordinates of a ray would have to be unbounded

**Lemma 1.** Every infinite admissible path has unbounded \(x\)-coordinate and unbounded \(y\)-coordinate.

**Proof.** Suppose \(y\le M\) along such a path while \(x\) is unbounded. Let
\[
L=\operatorname{lcm}(2,3,\dots,M).
\]
Choose a multiple \(X=kL\) larger than the initial \(x\)-coordinate. Since the path has unit steps and its \(x\)-coordinate eventually exceeds \(X\), the discrete intermediate-value property implies that some visited vertex has \(x=X\). At that vertex \(2\le y\le M\), hence \(y\mid L\mid X\), and therefore
\[
\gcd(X,y)=y>1,
\]
contrary to visibility. The other coordinate is handled symmetrically. \(\square\)

---

### 2. Parity structure

**Lemma 2.** If \((x,y)\) is visible and \(x\) is even, then it has no visible vertical neighbor. If \(y\) is even, it has no visible horizontal neighbor.

**Proof.** If \(x\) is even and \((x,y)\) is visible, then \(y\) is odd. Both \(y-1\) and \(y+1\), when positive, are even, so
\[
\gcd(x,y\pm1)\ge2.
\]
The second assertion is symmetric. \(\square\)

Thus a finite-height corridor cannot be analyzed merely by checking that each column contains some visible vertex: those visible vertices must also be connected through parity-compatible horizontal edges.

---

### 3. The proposed two-row corridor lemma is false

Let \(Y\ge3\) be odd and consider the three rows
\[
Y,\quad Y+1,\quad Y+2.
\]

**Lemma 3 (staggered edge walls).** Let \(p\mid Y\) and \(q\mid Y+2\) be primes. There are infinitely many integers \(k\) such that no horizontal edge in these three rows crosses from column \(k\) to column \(k+1\).

**Proof.** Since
\[
\gcd(Y,Y+2)=1,
\]
we have \(p\ne q\). By CRT there are infinitely many \(k\) satisfying
\[
k\equiv -1\pmod p,\qquad k\equiv0\pmod q.
\]
At row \(Y\), the point \((k+1,Y)\) is invisible because \(p\mid k+1\) and \(p\mid Y\). At row \(Y+2\), the point \((k,Y+2)\) is invisible because \(q\mid k\) and \(q\mid Y+2\).

The middle row \(Y+1\) is even. One of \(k,k+1\) is even, so one endpoint of the corresponding horizontal edge has gcd at least \(2\) with \(Y+1\). Hence there is no horizontal edge across this boundary in any of the three rows.

Every path confined to these rows that passes from \(x\le k\) to \(x\ge k+1\) must use such a horizontal edge. Therefore no such path exists. \(\square\)

For example, take \(Y=15\), \(p=3\), \(q=17\), and \(k=17\). Then:

- \((17,15)\) is visible;
- \((18,17)\) is visible;
- nevertheless there is no crossing between columns \(17\) and \(18\) in rows \(15,16,17\).

Indeed:

- row \(15\) is blocked at column \(18\) by \(3\);
- row \(16\) is blocked at column \(18\) by \(2\);
- row \(17\) is blocked at column \(17\) by \(17\).

Thus the claim

> “at every column one of rows \(Y,Y+2\) is coprime, hence the strip can be crossed”

is false. The obstruction is an edge wall, not necessarily a fully blocked column.

It also shows why looking only for columns divisible by
\[
\operatorname{rad}(Y(Y+1)(Y+2))
\]
misses much earlier separators.

---

### 4. Every finite dodge palette has full arithmetic walls

**Lemma 4.** Let \(R\subset\{2,3,\dots\}\) be a finite nonempty collection of rows. There are infinitely many columns containing no visible point in any row of \(R\).

**Proof.** For every \(y\in R\), choose a prime \(p_y\mid y\), and put
\[
M=\prod_{p\in\{p_y:y\in R\}}p.
\]
If \(x\) is a multiple of \(M\), then for every \(y\in R\),
\[
\gcd(x,y)\ge p_y>1.
\]
Thus column \(x\) is completely invisible throughout \(R\). Every multiple of \(M\) is such a wall. \(\square\)

This does not prevent crossing a finite span if the endpoint is reached before the next wall. It does show that every fixed-height palette has only finite horizontal components.

There is also an adversarial version compatible with the skeleton’s “rough semiprime” columns.

**Lemma 5 (rough semiprime immediately before a wall).** Let \(R\) be a finite collection of rows and let \(B\ge\max R\). There are infinitely many odd semiprimes
\[
X=qq',
\]
where \(q,q'>B\) are distinct primes, such that
\[
\gcd(X,y)=1,\qquad \gcd(X+1,y)>1
\]
for every \(y\in R\).

**Proof.** Choose one prime divisor \(p_y\mid y\) for each \(y\), and define \(M\) as in Lemma 4. By Dirichlet’s theorem choose distinct primes \(q,q'>B\) with
\[
q\equiv-1\pmod M,\qquad q'\equiv1\pmod M.
\]
Then
\[
X=qq'\equiv-1\pmod M,
\]
so \(M\mid X+1\). Hence \(\gcd(X+1,y)>1\) for all \(y\in R\).

On the other hand, every prime factor of \(X\) exceeds \(B\ge y\), so \(\gcd(X,y)=1\) for every \(y\in R\). \(\square\)

For the concrete palette \(R=\{15,16,17\}\), take
\[
q=101,\qquad q'=103,\qquad X=10403.
\]
Then \(q,q'>17\), while
\[
X+1=10404
\]
is divisible by \(2\), \(3\), and \(17\). Therefore column \(X\) is clean in all three rows, but column \(X+1\) is entirely invisible.

This refutes any **uniform bounded-height dodge theorem** based only on the hypotheses that \(X\) is a semiprime with very large prime factors. A successful construction would have to choose the anchor residues so as to avoid these walls and prove that this avoidance can be continued indefinitely.

---

### 5. The taller-palette counting proposal does not work

The notes suggest choosing \(K\) candidate dodge rows with disjoint prime profiles and arguing that a bad column cannot block all of them.

That pigeonhole argument is invalid. If the candidate rows are
\[
z_1,\dots,z_K,
\]
choose a prime \(p_j\mid z_j\) for each \(j\). Every multiple of
\[
p_1p_2\cdots p_K
\]
is blocked on all \(K\) rows. A column can have \(K\) or more distinct prime factors; there is no uniform bound on \(\omega(x)\).

Increasing \(K\) merely makes the wall modulus potentially larger. It does not eliminate walls. One must still prove that a suitable next anchor occurs before the first actual separator.

---

### 6. Dirichlet does not place the next semiprime inside the reachable finite interval

The semiprime CRT primitive itself is valid in the following form.

**Lemma 6.** If \(\gcd(c,M)=1\) and \(B\) is given, there are distinct primes \(q,q'>B\) such that
\[
qq'\equiv c\pmod M.
\]

**Proof.** By Dirichlet’s theorem choose
\[
q\equiv c\pmod M,\qquad q'\equiv1\pmod M,
\]
with both primes larger than \(B\) and distinct. Then \(qq'\equiv c\pmod M\). \(\square\)

This gives semiprimes somewhere in an infinite arithmetic progression. It gives no semiprime in a prescribed finite interval before the next corridor wall.

Indeed, finite intervals can be arbitrarily long without any product of two distinct primes.

**Lemma 7.** For every \(L\), there is an interval of \(L\) consecutive integers containing no integer of the form \(qq'\) with \(q,q'\) distinct primes.

**Proof.** For each \(1\le j\le L\), choose three primes
\[
p_{j,1},p_{j,2},p_{j,3},
\]
all distinct as \(j\) varies, and put
\[
m_j=p_{j,1}p_{j,2}p_{j,3}.
\]
The moduli \(m_j\) are pairwise coprime. By CRT choose \(N\) satisfying
\[
N\equiv-j\pmod{m_j}
\]
for every \(j\). Then \(N+j\) is divisible by three distinct primes, so it cannot be the product of exactly two distinct primes. Taking a sufficiently large positive representative gives the desired interval. \(\square\)

This lemma does not prove that the specially designed corridor intervals in the skeleton are semiprime-free. It proves that the assertion “the interval is huge, so an appropriately constrained semiprime occurs there” is not a consequence of CRT or Dirichlet and requires a new quantitative theorem.

The unresolved extension statement is essentially:

> Given the current anchor and a finite admissible corridor component to its east, prove that this same component contains another rough semiprime anchor satisfying all congruences needed for the next stage.

No such theorem is supplied, and it is comparable in difficulty to the original construction problem.

---

### 7. The CRT compositeness primitive is valid

One part of the notes can be made rigorous.

**Lemma 8.** Given \(h,B\ge1\), there is an odd semiprime \(Y=rr'\), with distinct primes \(r,r'>B\), such that
\[
Y+1,Y+2,\dots,Y+h
\]
are all composite.

**Proof.** Choose distinct odd primes \(P_1,\dots,P_h>h\). By CRT choose \(c\) modulo
\[
M=P_1\cdots P_h
\]
such that
\[
c\equiv-j\pmod{P_j}\qquad(1\le j\le h).
\]
Because \(P_j>j\), each residue \(-j\) is nonzero modulo \(P_j\), so \(\gcd(c,M)=1\).

By Lemma 6 choose distinct primes \(r,r'>B\) with
\[
r\equiv c\pmod M,\qquad r'\equiv1\pmod M.
\]
Then \(Y=rr'\equiv c\pmod M\), and hence
\[
P_j\mid Y+j.
\]
Taking \(r,r'\) sufficiently large ensures \(Y+j>P_j\), so \(Y+j\) is composite. \(\square\)

Thus forcing finitely many dodge rows to be composite is not the principal difficulty.

---

### 8. Corner admissibility would work conditionally

Suppose
\[
X_i=q_iq_i'
\]
with \(q_i,q_i'>Y_{i+1}\). Then every \(t\le Y_{i+1}\) satisfies
\[
\gcd(X_i,t)=1.
\]
Consequently the proposed vertical leg is clean, and in particular
\[
\gcd(X_i,Y_{i+1})=1.
\]
Since \(X_i\) and \(Y_{i+1}\) are composite, the corner is admissible.

Similarly, if the next anchor \(X_{i+1}\) has all prime factors larger than
\[
Y_{i+2}>Y_{i+1},
\]
then
\[
\gcd(X_{i+1},Y_{i+1})=1,
\]
and the other corner is admissible.

So the corner checks are not the fatal issue. The missing step is the existence of \(X_{i+1}\) in the same finite corridor component.

Also, no initial connection from \((8,9)\) is required: the problem prescribes no starting vertex, so one may start at the first successfully constructed anchor.

---

### 9. Large closed arithmetic barriers really do exist

The broad Route-5 hope that sufficiently large closed disallowed circuits cannot occur is false.

**Theorem 9.** For every \(L\ge1\), there exist \(X,Y>L+2\) such that:

1. \(\gcd(X,Y)=1\);
2. \(X\) is composite;
3. for every pair \((u,v)\) with
   \[
   \max(|u|,|v|)=L,
   \]
   one has
   \[
   \gcd(X+u,Y+v)>1.
   \]

Hence \((X,Y)\) is an admissible vertex enclosed by a square circuit of invisible points, and its component in \(H\) is finite.

**Proof.** Let
\[
F_L=\{(u,v)\in\mathbb Z^2:\max(|u|,|v|)=L\}.
\]
For each \(f=(u,v)\in F_L\), choose a distinct prime
\[
p_f>2L+1.
\]
Put
\[
P=\prod_{f\in F_L}p_f.
\]
By CRT choose integers \(A,B\) satisfying, for every \(f=(u,v)\),
\[
A\equiv-u\pmod{p_f},\qquad
B\equiv-v\pmod{p_f}.
\]

Choose \(t\) so large that
\[
X=A+tP>L+2
\]
and \(X>p_{(0,L)}\). Since
\[
X\equiv0\pmod{p_{(0,L)}},
\]
the integer \(X\) is composite.

We now choose
\[
Y=B+sP
\]
so that \(\gcd(X,Y)=1\). Let \(\ell\) be a prime divisor of \(X\).

If \(\ell\mid P\), then \(\ell=p_f\) for a unique \(f=(u,v)\). Since
\[
X\equiv-u\pmod\ell
\]
and \(\ell\mid X\), we have \(u\equiv0\pmod\ell\). But \(|u|\le L<\ell\), so \(u=0\). Because \(f\in F_L\), this forces \(v=\pm L\). Thus
\[
B\equiv-v\not\equiv0\pmod\ell.
\]
As \(P\equiv0\pmod\ell\), every \(Y=B+sP\) is nonzero modulo \(\ell\).

If \(\ell\nmid P\), exactly one residue class of \(s\pmod\ell\) makes
\[
B+sP\equiv0\pmod\ell.
\]
Choose any other residue. Applying CRT over the finitely many prime divisors \(\ell\mid X\) with \(\ell\nmid P\), choose \(s\) avoiding all forbidden residues. Add a sufficiently large multiple of the resulting modulus so that \(Y>L+2\). Then no prime divisor of \(X\) divides \(Y\), and hence
\[
\gcd(X,Y)=1.
\]

For each \(f=(u,v)\in F_L\), we have
\[
p_f\mid X+u,\qquad p_f\mid Y+v.
\]
Therefore
\[
\gcd(X+u,Y+v)\ge p_f>1.
\]
Every lattice point on the square perimeter of radius \(L\) about \((X,Y)\) is invisible.

The center \((X,Y)\) is admissible because it is visible and \(X\) is composite. Any unit-step path from the center to outside the square must first visit a point with \(\max(|u|,|v|)=L\), but every such point is invisible. Thus the component of \((X,Y)\) is contained in the finite interior square and is finite. \(\square\)

This theorem gives barriers of arbitrarily large diameter and finite components. It is not a disproof: their centers depend on the CRT construction, and it does not place a barrier around every admissible vertex.

---

### 10. Ledger

**Proved lemmas**

- Every hypothetical ray has both coordinates unbounded.
- Parity forbids vertical motion in even columns and horizontal motion in even rows.
- Three consecutive rows have periodic staggered edge walls.
- Every finite row palette has periodic fully invisible columns.
- A rough semiprime column may be immediately followed by a fully invisible column throughout any prescribed finite palette.
- Arbitrarily long semiprime-free intervals exist.
- Finite composite dodge-row runs with a semiprime base can be forced by CRT and Dirichlet.
- The proposed anchor corners are admissible if the stated least-prime-factor inequalities hold.
- Closed gcd-obstructed square circuits of arbitrary radius can enclose admissible vertices.

**Plausible but unproved**

- One may adaptively choose each row and anchor so that the reachable corridor component always contains a suitable next rough semiprime.
- Increasing the corridor height with the stage might leave enough room to avoid all separators.
- Some specially chosen root might avoid every closed arithmetic barrier and lie in an infinite component.

**Dead ends**

- “One visible point in each column” does not imply strip connectivity.
- Avoiding only columns divisible by \(\operatorname{rad}(Y(Y+1)(Y+2))\) does not avoid staggered edge walls.
- A fixed finite dodge palette cannot guarantee a usable row at every column.
- Dirichlet does not put a semiprime before the next finite wall.
- A global theorem excluding all large arithmetic circuits is false by Theorem 9.

## Self-Audit

1. **The corridor obstructions do not prove that every adaptive staircase fails.** They rule out the stated uniform two-row and bounded-palette arguments, but a construction could choose anchor residues and corridor heights adaptively. I believe the stated conclusion because I only mark the route blocked; I do not claim impossibility of all repairs.

2. **Lemma 5 and Lemma 8 cite Dirichlet’s theorem rather than prove it.** Dirichlet is a standard unconditional theorem, and the exact coprimality hypotheses are included. The explicit example \(X=101\cdot103\) already demonstrates the immediate-wall phenomenon without relying on its full general form.

3. **Theorem 9 constructs barriers around specially selected centers, not arbitrary prescribed vertices.** Therefore it proves finite components and refutes a universal no-barrier lemma, but it cannot establish a negative answer. The distinction is explicit in the argument.

## Computations To Verify

```python
from math import gcd, isqrt
from collections import deque

def isprime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def allowed(x, y):
    return (
        x >= 2 and y >= 2
        and gcd(x, y) == 1
        and (not isprime(x) or not isprime(y))
    )

def distinct_prime_factors(n):
    out = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out

def odd_distinct_semiprime(n):
    fs = []
    m = n
    d = 2
    while d*d <= m:
        while m % d == 0:
            fs.append(d)
            m //= d
        d += 1
    if m > 1:
        fs.append(m)
    return len(fs) == 2 and fs[0] != fs[1] and fs[0] % 2 == 1

# Explicit immediate wall in rows 15,16,17.
X = 101 * 103
R = [15, 16, 17]
assert all(gcd(X, y) == 1 for y in R)
assert all(gcd(X + 1, y) > 1 for y in R)
assert odd_distinct_semiprime(X)

# BFS confirms that no path in the strip crosses from X to X+1.
lo, hi = X - 30, X + 30
start = (X, 15)
Q = deque([start])
seen = {start}

while Q:
    x, y = Q.popleft()
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        w = (x + dx, y + dy)
        if lo <= w[0] <= hi and w[1] in R and allowed(*w) and w not in seen:
            seen.add(w)
            Q.append(w)

assert max(x for x, y in seen) == X

# Verify staggered three-row walls for many odd Y.
def least_prime_factor(n):
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            return p
    return n

for Y in range(3, 1000, 2):
    p = least_prime_factor(Y)
    q = least_prime_factor(Y + 2)
    # Find one CRT solution by brute force.
    k = next(k for k in range(p*q)
             if (k + 1) % p == 0 and k % q == 0)
    for row in [Y, Y+1, Y+2]:
        assert gcd(k, row) > 1 or gcd(k+1, row) > 1

# Search whether a proposed finite corridor contains a suitable next anchor.
def reachable_anchor_columns(X, Y, height, width, future_row_bound):
    rows = range(Y, Y + height + 1)
    verts = {
        (x, y)
        for x in range(X, X + width + 1)
        for y in rows
        if allowed(x, y)
    }
    if (X, Y) not in verts:
        return []

    Q = deque([(X, Y)])
    seen = {(X, Y)}
    while Q:
        v = Q.popleft()
        x, y = v
        for w in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
            if w in verts and w not in seen:
                seen.add(w)
                Q.append(w)

    ans = []
    for x in range(X + 1, X + width + 1):
        if (x, Y) in seen and odd_distinct_semiprime(x):
            if min(distinct_prime_factors(x)) > future_row_bound:
                ans.append(x)
    return ans
```

For Route 5, a computer should additionally:

1. Construct the CRT barrier of Theorem 9 for \(L=1,2,3\).
2. Verify all perimeter gcd certificates.
3. BFS from the center and confirm that its component stays inside the ring.
4. Compute minimum vertex cuts in annuli using node-splitting and max-flow.
5. Search whether successful staircase stages systematically require avoiding a small set of anchor residue classes.

## Route Diagnosis

The valid parts of the skeleton are the clean vertical legs, conditional corner admissibility, and CRT forcing of finite composite runs. The central horizontal mechanism fails: actual separators include staggered edge walls and selected-factor columns much earlier than the proposed radical wall. Ending the span before a wall then creates a finite-window almost-prime problem that CRT and Dirichlet do not solve.

Route 5 in its strongest “exclude large barriers” form is also dead: arbitrary finite circuits can be translated by CRT to consist entirely of invisible points, and such circuits can enclose admissible vertices. A fresh positive attempt must therefore locate one specially structured component that escapes all barriers, rather than prove that barriers are absent. A staircase repair would require a genuinely new extension theorem guaranteeing a future rough composite anchor inside the current reachable corridor component; without that theorem, the construction has reduced the problem to an unproved statement of comparable strength.