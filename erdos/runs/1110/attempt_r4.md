STATUS: BLOCKED

## Result

Route 4 yields an exact and useful recursive characterization of representability through bounded-exponent classes. It exposes precisely why the \((3,2)\) induction fails for \((5,2),(9,2),(5,3)\): a recursively represented remainder need not admit a representation with the exponent ceiling required to adjoin the new boundary power. I prove exact scaling and boundary-peeling lemmas, give primitive non-representable examples defeating cap-free induction, and exhibit infinite families on which the elementary size-based versions of both boundary recursions fail. I also prove that a successful eventual-coprime-representability theorem would force density \(0\) of non-representables for \((5,2),(5,3)\), and density exactly \(1/4\) for \((9,2)\); unconditionally, the latter pair has lower non-representable density at least \(1/4\). The remaining obstruction is an exponent-cap coverage theorem essentially equivalent to eventual coprime representability, and no finite-state invariant proving it was found.

## Complete Argument

### 1. Exact bounded-exponent recursion

It is convenient to allow the empty antichain, representing \(0\).

For \(L\ge 0\), let \(\mathcal U_L\) be the set of sums of finite antichains all of whose \(q\)-exponents satisfy \(\ell<L\), together with \(0\). Thus
\[
\mathcal U_0=\{0\}.
\]
Similarly, let \(\mathcal V_K\) be the corresponding set with all \(p\)-exponents satisfying \(k<K\).

#### Lemma 1: Exact boundary-peeling identities

For every \(L,K\ge0\),
\[
\boxed{\mathcal U_L
=
p\mathcal U_L
\;\cup\!
\bigcup_{0\le j<L}\left(q^j+p\mathcal U_j\right)}
\tag{1}
\]
and symmetrically
\[
\boxed{\mathcal V_K
=
q\mathcal V_K
\;\cup\!
\bigcup_{0\le i<K}\left(p^i+q\mathcal V_i\right).}
\tag{2}
\]

Here \(cS=\{cs:s\in S\}\).

#### Proof

Take an antichain \(A\) contributing to \(\mathcal U_L\).

If \(A\) contains no point with \(k=0\), then every point has \(k\ge1\). Subtracting \(1\) from every first coordinate gives an antichain with the same \(q\)-exponent cap \(L\), and its sum is the original sum divided by \(p\). Thus the original sum lies in \(p\mathcal U_L\).

Otherwise, \(A\) has exactly one point \((0,j)\), since two points in row \(k=0\) would be comparable. Every other point \((k,\ell)\) must satisfy \(k\ge1\) and \(\ell<j\); otherwise \((0,j)\le_{\mathrm{prod}}(k,\ell)\). Removing \((0,j)\), subtracting \(1\) from the remaining first coordinates, and dividing the remaining sum by \(p\) produces an element of \(\mathcal U_j\). Hence the original sum lies in \(q^j+p\mathcal U_j\).

Conversely, scaling an antichain in \(\mathcal U_L\) by \(p\) gives the first set on the right. If \(m\in\mathcal U_j\), shift a representing antichain for \(m\) one row to the right and adjoin \((0,j)\). Every shifted point has first coordinate at least \(1\) and second coordinate less than \(j\), so it is incomparable with \((0,j)\). This proves (1). Equation (2) follows by interchanging the two coordinates and bases. ∎

Define the minimum \(q\)-exponent cap
\[
h_q(0)=0,\qquad
h_q(n)=\min\{L:n\in\mathcal U_L\},
\]
with \(h_q(n)=\infty\) if \(n\) is non-representable.

Equation (1) gives a well-founded exact recurrence:

\[
h_q(n)=
\begin{cases}
h_q(n/p),&p\mid n,\\[4mm]
1+\displaystyle\min_{\substack{j\ge0,\ q^j\le n\\
q^j\equiv n\pmod p\\
h_q((n-q^j)/p)\le j}}j,
& p\nmid n,
\end{cases}
\tag{3}
\]
where the minimum of the empty set is \(\infty\).

Every argument on the right concerns a smaller integer. Thus (3) is both a proof tool and an exact \(O(X\log X)\)-type decision algorithm up to \(X\).

The symmetric height \(h_p(n)\), measuring the minimum cap on \(p\)-exponents, obeys the analogous recurrence obtained from (2).

---

### 2. Exact scaling invariance

#### Lemma 2: Scaling by either base is reversible

If \(p\mid n\), then
\[
n\in\mathcal R_{p,q}
\quad\Longleftrightarrow\quad
n/p\in\mathcal R_{p,q}.
\tag{4}
\]
Likewise, if \(q\mid n\),
\[
n\in\mathcal R_{p,q}
\quad\Longleftrightarrow\quad
n/q\in\mathcal R_{p,q}.
\tag{5}
\]

#### Proof

Multiplication of every summand by \(p\) preserves incomparability, proving the reverse implication in (4).

Conversely, suppose \(p\mid n\) and \(n\) has an antichain representation. If it contained a point \((0,\ell)\), that point would be unique in row \(0\), and all other summands would be divisible by \(p\). Reduction modulo \(p\) would give
\[
n\equiv q^\ell\not\equiv0\pmod p,
\]
contradicting \(p\mid n\). Hence every selected point has \(k\ge1\), and subtracting \(1\) from all first coordinates gives a representation of \(n/p\). The proof of (5) is identical. ∎

In particular, non-representability is preserved in both directions under multiplication by \(p\) and \(q\).

---

### 3. The valid size-based induction and its limitation

#### Lemma 3: Safe boundary adjunction

If \(m\in\mathcal R_{p,q}\) and \(m<p^K\), then
\[
q m+p^K\in\mathcal R_{p,q}.
\tag{6}
\]
If \(m\in\mathcal R_{p,q}\) and \(m<q^L\), then
\[
p m+q^L\in\mathcal R_{p,q}.
\tag{7}
\]

#### Proof

Every summand \(p^kq^\ell\) in a representation of \(m<p^K\) satisfies \(p^k\le m<p^K\), hence \(k<K\). Multiplying the representation by \(q\) raises every \(\ell\) by \(1\). The new points have \(k<K\) and \(\ell\ge1\), so adjoining \((K,0)\) preserves the antichain property. This proves (6). The proof of (7) is symmetric. ∎

For \((p,q)=(3,2)\), if \(n\) is odd and \(3^K\le n<3^{K+1}\), then
\[
m=\frac{n-3^K}{2}<3^K,
\]
so Lemma 3 closes the induction. For \(p=5\) or \(9\) with \(q=2\), this only works in
\[
p^K\le n<3p^K,
\]
leaving a genuine multiplicative gap before \(p^{K+1}\).

The failure is not merely an artifact of choosing the wrong nearby power.

Let
\[
d=\operatorname{ord}_p(q),\qquad
e=\operatorname{ord}_q(p)
\]
for the three unresolved coprime pairs. Their values are
\[
\begin{array}{c|cc}
(p,q)&d&e\\ \hline
(5,2)&4&1\\
(9,2)&6&1\\
(5,3)&4&2.
\end{array}
\]

#### Lemma 4: Infinite failure families for the automatic size criterion

For every sufficiently large \(L\), put
\[
n_L=q^{L+d}-p.
\]
Then \(n_L\) is coprime to \(pq\), and the largest \(j\) satisfying
\[
q^j\le n_L,\qquad q^j\equiv n_L\pmod p
\]
is \(j=L\). Its recursive remainder is
\[
\frac{n_L-q^L}{p}
=
\frac{q^d-1}{p}\,q^L-1
\ge q^L.
\tag{8}
\]
Consequently, no residue-compatible boundary choice for \(n_L\) satisfies the automatic cap condition \(m<q^j\) from Lemma 3.

Similarly, for every sufficiently large \(K\), put
\[
N_K=p^{K+e}-q.
\]
The largest \(i\) satisfying
\[
p^i\le N_K,\qquad p^i\equiv N_K\pmod q
\]
is \(i=K\), and
\[
\frac{N_K-p^K}{q}
=
\frac{p^e-1}{q}\,p^K-1
\ge p^K.
\tag{9}
\]

#### Proof

Since \(q^d\equiv1\pmod p\),
\[
n_L\equiv q^L\pmod p.
\]
As \(d\) is the exact order, \(q^j\equiv q^L\pmod p\) exactly when \(j\equiv L\pmod d\). The next such power is \(q^{L+d}=n_L+p>n_L\), while \(q^L\le n_L\) once \(L\) is sufficiently large. Formula (8) follows algebraically. For the three pairs, the coefficient \((q^d-1)/p\) is respectively \(3,7,16\), so the final inequality holds.

Also,
\[
n_L\equiv-p\pmod q,\qquad n_L\equiv q^L\pmod p,
\]
so \(n_L\) is coprime to both bases. The symmetric argument proves (9); its coefficients are \(2,4,8\), respectively. ∎

This lemma does **not** prove that these integers are non-representable. It proves that a size-only version of Route 4 cannot cover them.

---

### 4. Why ordinary strong induction is invalid

The recursive remainder must belong to a bounded class \(\mathcal U_j\) or \(\mathcal V_i\), not merely to \(\mathcal R_{p,q}\).

This distinction already causes failure at very small primitive examples:

\[
\begin{array}{c|c|c}
(p,q)&n&(n-p)/q\\ \hline
(5,2)&19&7=5+2\\
(9,2)&31&11=9+2\\
(5,3)&29&8=5+3.
\end{array}
\]

Each remainder is representable, but every displayed representation has maximum \(p\)-exponent \(1\), so it cannot be scaled by \(q\) and then combined with the boundary point \((1,0)\).

Moreover, the three target integers are themselves non-representable.

- For \(19\) in the \((5,2)\) grid, a coprime representation must have a pure \(5^K\) endpoint. Since \(25>19\), necessarily \(K=1\). With only rows \(0\) and \(1\), the representation would have to be
  \[
  19=5+2^L,
  \]
  impossible because \(14\) is not a power of \(2\).

- For \(31\) in the \((9,2)\) grid, similarly \(81>31\), so a representation would have to be
  \[
  31=9+2^L,
  \]
  impossible because \(22\) is not a power of \(2\).

- For \(29\) in the \((5,3)\) grid, its pure \(5\)-power endpoint must satisfy
  \[
  5^K\equiv29\equiv2\pmod3.
  \]
  Thus \(K\) is odd. Since \(5^3>29\), necessarily \(K=1\), and one would need
  \[
  29=5+3^L,
  \]
  impossible because \(24\) is not a power of \(3\).

Therefore the unbounded assertion “the smaller remainder is representable by induction” is insufficient.

---

### 5. Consequences if Route 4 were successful

Let
\[
\mathcal E_{p,q}
=
\{n:\gcd(n,pq)=1,\ n\notin\mathcal R_{p,q}\}.
\]

#### Proposition 5: Prime-base cases

For \((p,q)=(5,2)\) or \((5,3)\), if \(\mathcal E_{p,q}\) is finite, then
\[
N_{p,q}(X)=O_{p,q,\mathcal E}\bigl((\log X)^2\bigr).
\]
Consequently,
\[
\frac{N_{p,q}(X)}X\longrightarrow0,
\qquad
\frac{R_{p,q}(X)}X\longrightarrow1.
\]

#### Proof

Because both bases are prime, every positive integer has a unique decomposition
\[
n=p^a q^b m,\qquad \gcd(m,pq)=1.
\]
Repeated use of Lemma 2 shows
\[
n\in\mathcal R_{p,q}
\quad\Longleftrightarrow\quad
m\in\mathcal R_{p,q}.
\]
Thus every non-representable integer is of the form
\[
e p^a q^b,\qquad e\in\mathcal E_{p,q}.
\]
For fixed \(e\), the number of pairs \((a,b)\) satisfying \(ep^aq^b\le X\) is
\[
O((\log X)^2).
\]
Summing over the finite set \(\mathcal E_{p,q}\) proves the result. ∎

Thus eventual representability in the reduced residue classes for either prime pair would not merely disprove coprime infinitude: it would force non-representables to have density \(0\).

#### Proposition 6: The composite pair \((9,2)\)

Every integer \(n\) with odd \(3\)-adic valuation is \((9,2)\)-non-representable. Hence
\[
\underline d(\mathcal N_{9,2})\ge\frac14.
\tag{10}
\]

If \(\mathcal E_{9,2}\) is finite, then the natural density exists and equals
\[
d(\mathcal N_{9,2})=\frac14.
\tag{11}
\]

#### Proof

Suppose \(3\mid n\) but \(9\nmid n\). If a representation had a point in row \(k=0\), its unique such summand would be \(2^\ell\), which is a unit modulo \(3\); every other term would be divisible by \(9\), so the total could not be divisible by \(3\). If there were no row-\(0\) point, every term would be divisible by \(9\), contrary to \(9\nmid n\). Thus such \(n\) is non-representable.

If \(v_3(n)=2a+1\), repeated division by \(9\), justified by Lemma 2, reduces to the preceding case. Hence every odd \(3\)-adic valuation is forbidden.

The density of integers with \(v_3(n)=2a+1\) is
\[
\frac{2}{3^{2a+2}},
\]
so their total density is
\[
\sum_{a\ge0}\frac{2}{3^{2a+2}}
=
\frac{2/9}{1-1/9}
=
\frac14.
\]

If \(v_3(n)\) is even, repeated division by \(9\), followed by division by every factor \(2\), reduces \(n\) to an integer coprime to \(18\). Under finiteness of \(\mathcal E_{9,2}\), the additional non-representables form finitely many sets
\[
\{e\,2^a9^b:a,b\ge0\},
\]
whose counting function is \(O((\log X)^2)\). They have density zero, proving (11). ∎

---

### 6. The precise unresolved cap problem

By recurrence (3), eventual coprime representability for one of the three pairs is equivalent to finding \(N\) such that every \(n>N\) with \(\gcd(n,pq)=1\) admits an exponent \(j\) satisfying
\[
q^j\le n,\qquad q^j\equiv n\pmod p,
\qquad
h_q\!\left(\frac{n-q^j}{p}\right)\le j.
\tag{12}
\]

The first two conditions are easy because the relevant power orbit contains every unit. The third is the unresolved exponent-cap condition.

Writing a capped state as \((n,L)\), and choosing \(j=L-s\), the normalized ratio
\[
y=\frac n{q^L}
\]
changes to
\[
y'
=
\frac{(n-q^j)/p}{q^j}
=
\frac{q^s y-1}{p}.
\tag{13}
\]
The potentially occurring expansion factors include
\[
\frac{2^4}{5},\qquad
\frac{2^6}{9},\qquad
\frac{3^4}{5},
\]
all greater than \(1\). Thus the most direct one-interval contraction invariant cannot work. A more elaborate finite collection of states might still succeed, but it must control these expanding transitions and the exact integer residue information. Establishing such a state system is currently the block.

## Self-Audit

1. **The exact recurrence contains the self-referential term \(p\mathcal U_L\).**  
   This might look non-well-founded as a set equation. However, recurrence (3) is well-founded numerically because division by \(p\), or subtraction followed by division by \(p\), always produces a smaller nonnegative integer. The antichain decomposition proves both directions.

2. **The density conclusions in Propositions 5 and 6 are conditional on finite coprime exception sets.**  
   They do not prove that such sets are finite. The orbit counting and the \(1/4\) valuation computation are nevertheless unconditional implications of Lemma 2, and I have explicitly separated them from the unresolved hypothesis.

3. **The failure families only rule out size-based and cap-free inductions, not every conceivable finite-state induction.**  
   A sophisticated state system could encode more than normalized size and first-level residues. I do not claim impossibility of Route 4; the route is marked BLOCKED because the missing exponent-cap coverage theorem is of essentially the same strength as eventual coprime representability.

## Computations To Verify

The following dynamic program implements recurrence (3) exactly.

```python
from math import gcd

INF = 10**30

def powers_up_to(base, X):
    ans = []
    v = 1
    e = 0
    while v <= X:
        ans.append((e, v))
        e += 1
        v *= base
    return ans

def minimum_boundary_cap(scale_base, boundary_base, X):
    """
    Returns h[n], the minimum L such that n has an antichain
    representation with every boundary_base exponent < L.

    For the original q-exponent cap, call:
        hq = minimum_boundary_cap(p, q, X)
    For the symmetric p-exponent cap, call:
        hp = minimum_boundary_cap(q, p, X)
    """
    p = scale_base
    q = boundary_base
    qpows = powers_up_to(q, X)

    h = [INF] * (X + 1)
    parent = [None] * (X + 1)
    h[0] = 0

    for n in range(1, X + 1):
        if n % p == 0:
            h[n] = h[n // p]
            parent[n] = ("scale", n // p)
            continue

        best = INF
        best_parent = None
        for j, qj in qpows:
            if qj > n:
                break
            if (n - qj) % p != 0:
                continue
            m = (n - qj) // p
            if h[m] <= j and j + 1 < best:
                best = j + 1
                best_parent = ("boundary", j, m)

        h[n] = best
        parent[n] = best_parent

    return h, parent
```

Cross-check the two coordinate recurrences:

```python
def cross_check_heights(p, q, X):
    hq, _ = minimum_boundary_cap(p, q, X)
    hp, _ = minimum_boundary_cap(q, p, X)

    for n in range(1, X + 1):
        assert (hq[n] < INF) == (hp[n] < INF)

for pair in [(5,2), (9,2), (5,3), (3,2)]:
    cross_check_heights(*pair, X=100000)
```

Check the primitive examples and exact scaling:

```python
def regression_checks(p, q, X):
    h, _ = minimum_boundary_cap(p, q, X)

    for n in range(1, X + 1):
        if p * n <= X:
            assert (h[p*n] < INF) == (h[n] < INF)
        if q * n <= X:
            assert (h[q*n] < INF) == (h[n] < INF)

for p, q, bad in [(5,2,19), (9,2,31), (5,3,29)]:
    h, _ = minimum_boundary_cap(p, q, 1000)
    assert h[bad] == INF

h, _ = minimum_boundary_cap(3, 2, 100000)
assert all(h[n] < INF for n in range(1, 100001))
```

Independent exact antichain DFS for small \(X\):

```python
def represented_by_dfs(p, q, X):
    K = 0
    while p**(K + 1) <= X:
        K += 1
    L = 0
    while q**(L + 1) <= X:
        L += 1

    represented = [False] * (X + 1)

    def dfs(k, ell_cap, total):
        if total > 0:
            represented[total] = True
        if k > K:
            return

        # Skip row k.
        dfs(k + 1, ell_cap, total)

        # Choose exactly one point in row k.
        for ell in range(ell_cap):
            term = (p**k) * (q**ell)
            if total + term <= X:
                dfs(k + 1, ell, total + term)

    dfs(0, L + 1, 0)
    return represented

for p, q in [(5,2), (9,2), (5,3), (3,2)]:
    X = 500
    dfs = represented_by_dfs(p, q, X)
    h, _ = minimum_boundary_cap(p, q, X)
    for n in range(1, X + 1):
        assert dfs[n] == (h[n] < INF)
```

Search directly for persistence or stabilization of primitive exceptions:

```python
def primitive_bad_statistics(p, q, X):
    h, _ = minimum_boundary_cap(p, q, X)
    bad = [
        n for n in range(1, X + 1)
        if gcd(n, p*q) == 1 and h[n] == INF
    ]
    return {
        "count": len(bad),
        "largest": max(bad) if bad else None,
        "last_100": bad[-100:],
    }

for p, q in [(5,2), (9,2), (5,3)]:
    for X in [10**3, 10**4, 10**5, 10**6]:
        print((p,q), X, primitive_bad_statistics(p,q,X))
```

Measure the cap slack that a finite-state induction would need to control:

```python
def integer_log(n, base):
    e = -1
    v = 1
    while v <= n:
        e += 1
        v *= base
    return e

def cap_slack_statistics(p, q, X):
    h, _ = minimum_boundary_cap(p, q, X)
    data = []
    for n in range(1, X + 1):
        if gcd(n, p*q) == 1 and h[n] < INF:
            # Since h is one plus the maximum q-exponent,
            # this is the amount below the trivial size cap.
            slack = integer_log(n, q) + 1 - h[n]
            data.append((slack, n, h[n]))
    data.sort()
    return data[:100]

for pair in [(5,2), (9,2), (5,3)]:
    print(pair, cap_slack_statistics(*pair, X=10**6))
```

Verify the infinite size-failure families:

```python
def multiplicative_order(a, m):
    assert gcd(a, m) == 1
    x = a % m
    d = 1
    while x != 1:
        x = (x * a) % m
        d += 1
    return d

for p, q in [(5,2), (9,2), (5,3)]:
    d = multiplicative_order(q, p)
    e = multiplicative_order(p, q)

    for L in range(1, 20):
        n = q**(L+d) - p
        candidates = [
            j for j, qj in powers_up_to(q, n)
            if qj % p == n % p
        ]
        assert max(candidates) == L
        for j in candidates:
            m = (n - q**j) // p
            assert m >= q**j

    for K in range(1, 20):
        n = p**(K+e) - q
        candidates = [
            i for i, pi in powers_up_to(p, n)
            if pi % q == n % q
        ]
        assert max(candidates) == K
        for i in candidates:
            m = (n - p**i) // q
            assert m >= p**i
```

For \((9,2)\), verify the valuation obstruction:

```python
def vprime(n, r):
    v = 0
    while n % r == 0:
        n //= r
        v += 1
    return v

X = 10**6
h, _ = minimum_boundary_cap(9, 2, X)
for n in range(1, X + 1):
    if vprime(n, 3) % 2 == 1:
        assert h[n] == INF
```

## Route Diagnosis

**Proved ledger**

- Exact reversible scaling by \(p\) and \(q\).
- Exact bounded-cap set recurrences (1) and (2).
- Exact well-founded height recurrence (3).
- Safe boundary adjunction under a strict size bound.
- Primitive non-representability of \(19\), \(31\), and \(29\) for the three target pairs.
- Infinite families on which the automatic size-cap test fails in either recursion direction.
- If the coprime exception set is finite, then the non-representable density is \(0\) for \((5,2),(5,3)\), and exactly \(1/4\) for \((9,2)\).
- Unconditionally, \(\underline d(\mathcal N_{9,2})\ge1/4\).

**Plausible but unproved**

- The primitive non-representable sets may be infinite in all three cases.
- A multi-state induction using normalized cap ratios and deeper congruence data might still prove eventual primitive representability for one pair.
- The exact height recurrence may admit a useful statistical or automata-theoretic analysis.

**Dead ends**

- Ordinary strong induction on representability: false because it loses the exponent cap.
- Choosing the largest residue-compatible boundary power and using size alone: fails on the infinite families in Lemma 4.
- A single bounded normalized-ratio invariant: obstructed by expanding transitions \(16/5\), \(64/9\), and \(81/5\).
- Finite computation alone: recurrence (3) decides every bounded range but provides no stabilization theorem.

The sharp block is condition (12): one needs a uniform theorem that sufficiently large unit integers have a recursively represented predecessor with a sufficiently small exponent cap. That statement is essentially the desired eventual-coprime-representability assertion expressed in exact recursive form. A fresh Route 4 attempt should first run the height dynamic program to very large bounds, measure primitive exception growth and cap slack, and then attempt automatic synthesis of several normalized cap states. If primitive exceptions visibly continue to proliferate, the more promising direction is to use recurrence (3) to count the distribution of finite heights and pursue density zero rather than eventual representability.