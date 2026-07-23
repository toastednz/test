STATUS: BLOCKED

## Result

I reconstructed the order-type-\(\omega\) mechanism behind the DEGS three-term theorem and strengthened it substantially: for every permutation, every anchor \(r\), and every \(d>0\), there are infinitely many \(j\) such that
\[
p(r)<p(r+2^jd)<p(r+2^{j+1}d).
\]
If no increasing four-term progression exists, each such triple is necessarily capped by
\[
p(r)<p(r+3\cdot2^jd)<p(r+2^{j+1}d).
\]
I also obtained an affine suffix-record formulation: every arithmetic ray has infinitely many right-to-left position minima; three such records in arithmetic progression force an increasing four-term progression. Thus a counterexample would require the record set on every affine ray to be three-AP-free. However, the DEGS iteration does not preserve the common difference needed for concatenation, and the forced cap produces no descending chain of positions. I also prove that unrestricted finite forcing is impossible: a least-significant-bit lexicographic order avoids even monotone three-term progressions on every finite interval. The route therefore remains blocked at a genuinely new simultaneous affine-record or scale-alignment statement.

## Complete Argument

### 1. The minimal DEGS forcing mechanism

A strictly decreasing infinite sequence of positive integers cannot exist. Consequently:

**Lemma 1.** Every sequence of distinct positive integers \(z_0,z_1,\dots\) has infinitely many indices \(j\) for which
\[
z_j<z_{j+1}.
\]

**Proof.** If there were only finitely many such indices, then for all sufficiently large \(j\), distinctness would force
\[
z_j>z_{j+1}.
\]
This would be an infinite strictly decreasing sequence in \(\mathbb N\), impossible. \(\square\)

Let \(m=x_1\), so \(p(m)=1\). Fix \(d>0\) and set
\[
z_j=p(m+2^jd).
\]
If there were no increasing three-term progression anchored at \(m\), then for every \(j\),
\[
p(m+2^jd)>p(m+2^{j+1}d),
\]
because
\[
m,\quad m+2^jd,\quad m+2^{j+1}d
\]
is a three-term arithmetic progression and \(p(m)=1\). This contradicts Lemma 1. Thus the DEGS three-term conclusion follows, and in fact the progression may always be taken increasing in position.

The first-element assumption can be removed.

### 2. A controlled three-term theorem at every anchor and scale family

**Lemma 2 (controlled DEGS lemma).** Let \(p\) be any permutation of \(\mathbb N\). For every \(r,d\geq 1\), there are infinitely many \(j\geq0\) such that
\[
p(r)<p(r+2^jd)<p(r+2^{j+1}d).
\]

**Proof.** Put
\[
z_j=p(r+2^jd).
\]
The values \(z_j\) are distinct. Only \(p(r)-1\) positions are smaller than \(p(r)\), so
\[
z_j>p(r)
\]
for all sufficiently large \(j\). By Lemma 1, there are infinitely many \(j\) with \(z_j<z_{j+1}\). Discarding finitely many small \(j\), both \(z_j\) and \(z_{j+1}\) exceed \(p(r)\), giving
\[
p(r)<z_j<z_{j+1}.
\]
The corresponding values form the arithmetic progression
\[
r,\quad r+2^jd,\quad r+2^{j+1}d.
\]
\(\square\)

This is a genuine strengthening of the bare three-term theorem: the first term \(r\) and the dyadic scale family \(2^jd\) may be prescribed.

### 3. What four-term avoidance forces around these triples

First record the general isolation rule.

**Lemma 3 (isolation of monotone three-APs).** Suppose \(p\) avoids both increasing and decreasing monotone four-term arithmetic progressions.

If
\[
p(a)<p(a+d)<p(a+2d),
\]
then
\[
p(a+3d)<p(a+2d),
\]
and, when \(a>d\),
\[
p(a-d)>p(a).
\]

If instead
\[
p(a)>p(a+d)>p(a+2d),
\]
then
\[
p(a+3d)>p(a+2d),
\]
and, when \(a>d\),
\[
p(a-d)<p(a).
\]

**Proof.** For the increasing case, \(p(a+3d)>p(a+2d)\) would extend the triple to an increasing four-AP. Likewise, if \(a>d\) and \(p(a-d)<p(a)\), then
\[
p(a-d)<p(a)<p(a+d)<p(a+2d)
\]
would be increasing. The decreasing case follows by reversing all inequalities. \(\square\)

Combining Lemmas 2 and 3 gives the strongest direct output of the DEGS iteration.

**Proposition 4 (infinitely many forced caps).** Suppose \(p\) has no increasing monotone four-term arithmetic progression. For every \(r,d\geq1\), there are infinitely many \(j\) such that, with \(q=2^jd\),
\[
p(r)<p(r+q)<p(r+2q)
\]
and
\[
p(r)<p(r+3q)<p(r+2q).
\]

**Proof.** Lemma 2 gives infinitely many \(j\) with
\[
p(r)<p(r+q)<p(r+2q).
\]
The values \(r+3\cdot2^jd\) are all distinct, so only finitely many of them can precede \(r\). Hence, after discarding finitely many further indices,
\[
p(r)<p(r+3q).
\]
Lemma 3 gives
\[
p(r+3q)<p(r+2q).
\]
\(\square\)

Thus every anchor and dyadic direction has infinitely many rank patterns of the form
\[
p(r)<\{p(r+q),p(r+3q)\}<p(r+2q),
\]
with no forced comparison between \(p(r+q)\) and \(p(r+3q)\).

This is exactly where straightforward concatenation fails. Reapplying Lemma 2 at \(r+3q\) produces another increasing three-AP at a generally much larger dyadic scale; it does not produce another point below \(p(r+3q)\), nor does it preserve the difference \(q\). Therefore the inequality
\[
p(r+3q)<p(r+2q)
\]
does not iterate into an infinite descending chain.

There can also be no universal bound on the scale \(j\). For any \(K\), choose \(r,d\) and begin a permutation with
\[
r,\ r+2^{K+1}d,\ r+2^Kd,\ \ldots,\ r+2d,\ r+d,
\]
then list all unused integers arbitrarily. For \(0\leq j\leq K\),
\[
p(r+2^jd)>p(r+2^{j+1}d).
\]
Thus the first forced ascent can be delayed past any prescribed finite collection of scales.

### 4. Affine suffix records

Fix an arithmetic ray
\[
L=\{b+qn:n\in\mathbb N_0\},
\qquad b,q\geq1.
\]
Call \(n\) a record coefficient if
\[
p(b+qn)<p(b+qm)\qquad\text{for every }m>n.
\]
Let \(\mathcal R_{b,q}\) be the set of record coefficients.

**Lemma 5.** The set \(\mathcal R_{b,q}\) is infinite. Moreover, if
\[
\alpha<\beta,\qquad \alpha,\beta\in\mathcal R_{b,q},
\]
then
\[
p(b+q\alpha)<p(b+q\beta).
\]

**Proof.** For each \(N\), the nonempty set
\[
\{p(b+qn):n\geq N\}\subseteq\mathbb N
\]
has a least element. Let its unique coefficient be \(n_N\). Then \(n_N\geq N\) and \(n_N\) is a record coefficient. Hence the record coefficients are unbounded and infinite.

If \(\alpha<\beta\) are records, the defining property of \(\alpha\), applied to \(m=\beta\), gives the stated inequality. \(\square\)

Two records already recover the three-term theorem.

**Corollary 6.** If \(\alpha<\beta\) are record coefficients on a ray, then
\[
b+q\alpha,\quad b+q\beta,\quad b+q(2\beta-\alpha)
\]
is an increasing monotone three-term arithmetic progression.

**Proof.** The first inequality follows from \(\alpha\) being a record. Since \(2\beta-\alpha>\beta\), the second follows from \(\beta\) being a record. \(\square\)

For four terms, one needs three records in arithmetic progression.

**Proposition 7 (affine-record criterion).** If \(\mathcal R_{b,q}\) contains a nontrivial three-term arithmetic progression
\[
\alpha,\quad \alpha+h,\quad \alpha+2h,
\]
then \(p\) contains an increasing monotone four-term arithmetic progression.

**Proof.** Since the first three coefficients are records,
\[
p(b+q\alpha)
 <p(b+q(\alpha+h))
 <p(b+q(\alpha+2h)).
\]
The last of these is a record and \(\alpha+3h>\alpha+2h\), so
\[
p(b+q(\alpha+2h))
 <p(b+q(\alpha+3h)).
\]
These are the four terms of an arithmetic progression with difference \(qh\). \(\square\)

Consequently, any counterexample must satisfy:

\[
\boxed{\text{For every affine ray }L,\ \mathcal R_L\text{ is three-AP-free}.}
\]

There is also an exact four-point order forced by any pair of records.

**Proposition 8.** Suppose \(p\) has no increasing monotone four-AP. If \(\alpha<\beta\) are record coefficients on a ray, put
\[
\gamma=2\beta-\alpha,\qquad \delta=3\beta-2\alpha.
\]
Then
\[
p(b+q\alpha)
<
p(b+q\beta)
<
p(b+q\delta)
<
p(b+q\gamma).
\]

**Proof.** Recordhood gives
\[
p(b+q\alpha)<p(b+q\beta)<p(b+q\gamma)
\]
and also
\[
p(b+q\beta)<p(b+q\delta).
\]
The four coefficients \(\alpha,\beta,\gamma,\delta\), in that numerical order, form a four-term progression. Avoidance therefore requires
\[
p(b+q\delta)<p(b+q\gamma).
\]
Combining the inequalities proves the assertion. \(\square\)

Thus every pair of records forces the order pattern \(0,1,3,2\) on the corresponding four-AP.

### 5. Why the global record set alone cannot finish the proof

The suffix-record set of a permutation can be an arbitrarily sparse prescribed infinite set.

**Lemma 9.** Let
\[
R=\{r_1<r_2<\cdots\}\subseteq\mathbb N,\qquad r_1=1.
\]
There is a permutation whose global suffix-record set is exactly \(R\).

**Proof.** Form the word
\[
r_1,\quad
r_2,\ (r_1+1,\ldots,r_2-1),\quad
r_3,\ (r_2+1,\ldots,r_3-1),\quad\ldots,
\]
with the elements inside each displayed gap listed in any order.

Every positive integer occurs exactly once. When \(r_i\) is listed, every integer greater than \(r_i\) is still unlisted, so
\[
p(r_i)<p(n)\qquad(n>r_i).
\]
Thus every \(r_i\) is a suffix record.

If \(r_i<n<r_{i+1}\), then \(r_{i+1}>n\) was listed before \(n\), so \(n\) is not a suffix record. Hence the record set is exactly \(R\). \(\square\)

Taking
\[
R=\{1,2,4,8,16,\dots\}
\]
gives a three-AP-free suffix-record set. Indeed, if
\[
2^i,2^j,2^k
\]
with \(i<j<k\) formed a three-AP, then
\[
1+2^{k-i}=2^{j-i+1},
\]
whose left side is odd and right side even.

This is not a counterexample to the original problem—the constructed permutation may have many monotone four-APs—but it proves that infinitude of the global suffix-record set, by itself, is insufficient. A proof must use the simultaneous record structure on many affine rays or the additional \(0,1,3,2\) constraints of Proposition 8.

### 6. A finite-predecessor/divisor lemma

The order-type-\(\omega\) property yields another useful multiscale fact.

Call \(q\) good for \(n\) if
\[
p(n)<p(n+kq)\qquad\text{for every }k\geq1.
\]
Equivalently, \(n\) is the first record on the ray \(n+q\mathbb N_0\).

**Lemma 10.** For every fixed \(n\), all but finitely many \(q\) are good for \(n\).

**Proof.** Let
\[
E_n=\{v>n:p(v)<p(n)\}.
\]
This is finite because only \(p(n)-1\) values precede \(n\).

If \(q\) is not good for \(n\), then for some \(k\geq1\),
\[
v=n+kq\in E_n.
\]
Thus \(q\mid(v-n)\) for some \(v\in E_n\). Hence every bad \(q\) belongs to the finite union
\[
\bigcup_{v\in E_n}\{q:q\mid(v-n)\}.
\]
\(\square\)

For any fixed finite set of anchors, a common sufficiently large \(q\) is therefore good for all of them. The unresolved difficulty is that an intended progression has moving anchors
\[
n,\quad n+q,\quad n+2q;
\]
the exceptional sets of the latter two depend on \(q\) itself. Showing that some \(q\) is simultaneously good for these three moving anchors would immediately give
\[
p(n)<p(n+q)<p(n+2q)<p(n+3q),
\]
but no argument establishing this self-referential alignment was found.

### 7. Unrestricted finite forcing is impossible

Define a total order \(\prec_2\) on the nonnegative integers by comparing binary digits from least significant to most significant. Explicitly, for \(u\ne v\), let
\[
k=\min\{i:\operatorname{bit}_i(u)\ne\operatorname{bit}_i(v)\},
\]
and declare
\[
u\prec_2 v
\quad\Longleftrightarrow\quad
\operatorname{bit}_k(u)=0,\ \operatorname{bit}_k(v)=1.
\]

This is a total order: it is ordinary lexicographic order on the binary digit strings, read from right to left.

**Lemma 11.** The order \(\prec_2\) contains no monotone nontrivial three-term arithmetic progression.

**Proof.** Consider
\[
a,\quad a+d,\quad a+2d
\]
and put \(k=v_2(d)\). Modulo \(2^{k+1}\),
\[
d\equiv 2^k,\qquad 2d\equiv0.
\]
Thus \(a\) and \(a+2d\) have identical binary digits in positions \(0,\dots,k\), while \(a+d\) has the same digits below \(k\) and the opposite digit at position \(k\).

Therefore the least significant differing bit between the middle term and either endpoint is \(k\). Depending on its bit at \(k\), the middle term precedes both endpoints or follows both endpoints. It never lies between them in the order, so the three terms cannot occur in increasing or decreasing numerical order. \(\square\)

Restricting \(\prec_2\) to any finite interval \([N]\) gives a finite avoiding order. Hence:

\[
\boxed{\text{There is no finite }N\text{ that forces even a monotone three-AP, and therefore none that forces a four-AP.}}
\]

This abstract order does not come from a permutation sequence. Indeed,
\[
2^{j+1}\prec_2 2^j
\]
for every \(j\), so it has an infinite descending chain; for example, \(1\) has the infinitely many predecessors \(2,4,8,\dots\). This pinpoints exactly why the order-type-\(\omega\) hypothesis is indispensable.

## Self-Audit

1. **The strongest new statement is Lemma 2, especially the word “infinitely.”** The only subtlety is that an infinite sequence of ranks might have sporadic ascents while many terms precede the anchor. This is handled because only finitely many ranks are below \(p(r)\), while Lemma 1 gives infinitely many ascents; deleting finitely many indices preserves infinitely many usable ascents.

2. **The affine-record criterion might appear to use recordhood beyond the chosen ray.** It does not: all four extrapolated coefficients lie farther along the same ray, so the defining comparisons of the three records apply directly. No density, global suffix-minimum, or compactness assumption is used.

3. **The diagnosis that DEGS iteration is blocked is not a theorem that no clever iteration can work.** What is rigorously established is narrower: the current inequalities do not themselves create a descending rank chain, bounded scale control is false, and global suffix-record infinitude is insufficient. A more sophisticated argument exploiting interactions among translated affine rays could still complete Route 4.

## Computations To Verify

The following code checks finite words, the binary least-significant-bit construction, affine record sets, and forced caps.

```python
from itertools import permutations

def ap_violations(order, length=4):
    """Return all monotone length-term APs supported by the finite word."""
    pos = {v: i for i, v in enumerate(order)}
    S = set(order)
    M = max(order)
    out = []
    for d in range(1, M // (length - 1) + 1):
        for a in range(1, M - (length - 1) * d + 1):
            vals = [a + i*d for i in range(length)]
            if not all(v in S for v in vals):
                continue
            ranks = [pos[v] for v in vals]
            inc = all(ranks[i] < ranks[i+1] for i in range(length-1))
            dec = all(ranks[i] > ranks[i+1] for i in range(length-1))
            if inc or dec:
                out.append((a, d, vals, ranks))
    return out

def lsb_lex_order(N):
    """Restriction of least-significant-bit lexicographic order to [N]."""
    L = N.bit_length()
    key = lambda n: tuple((n >> i) & 1 for i in range(L))
    return sorted(range(1, N+1), key=key)

# This should pass for any tested N.
for N in range(1, 300):
    w = lsb_lex_order(N)
    assert not ap_violations(w, length=3)
    assert not ap_violations(w, length=4)
```

Affine suffix records and Proposition 7 can be checked as follows.

```python
def finite_ray_records(order, b, q):
    """
    Record coefficients in the finite ray b+q*k contained in the word.
    Recordhood is relative to the available finite tail.
    """
    pos = {v: i for i, v in enumerate(order)}
    coeffs = []
    k = 0
    while b + q*k in pos:
        coeffs.append(k)
        k += 1

    best = float('inf')
    records = []
    for k in reversed(coeffs):
        rank = pos[b + q*k]
        if rank < best:
            records.append(k)
            best = rank
    return list(reversed(records))

def verify_record_criterion(order, b, q):
    pos = {v: i for i, v in enumerate(order)}
    R = set(finite_ray_records(order, b, q))
    if not R:
        return True
    K = max(R)
    for a in R:
        for h in range(1, K + 1):
            if a+h in R and a+2*h in R and b+q*(a+3*h) in pos:
                ranks = [pos[b+q*(a+i*h)] for i in range(4)]
                assert ranks[0] < ranks[1] < ranks[2] < ranks[3]
    return True
```

The local cap implication can be regression-tested on any finite avoiding order:

```python
def verify_caps(order):
    pos = {v: i for i, v in enumerate(order)}
    S = set(order)
    M = max(order)

    assert not ap_violations(order, length=4)

    for r in S:
        for d in range(1, M+1):
            q = d
            while r + 3*q <= M:
                vals = [r, r+q, r+2*q, r+3*q]
                if all(v in S for v in vals):
                    p0, p1, p2, p3 = map(pos.get, vals)
                    if p0 < p1 < p2:
                        assert p3 < p2
                q *= 2
    return True
```

A finite SAT model can be used to inspect avoiding orders and dyadic delay profiles:

```python
# Requires: pip install z3-solver
import z3

def finite_avoider(N):
    rank = {v: z3.Int(f"r_{v}") for v in range(1, N+1)}
    s = z3.Solver()

    for v in range(1, N+1):
        s.add(0 <= rank[v], rank[v] < N)
    s.add(z3.Distinct([rank[v] for v in range(1, N+1)]))

    for d in range(1, N//3 + 1):
        for a in range(1, N - 3*d + 1):
            vals = [a+i*d for i in range(4)]
            inc = z3.And(*[
                rank[vals[i]] < rank[vals[i+1]] for i in range(3)
            ])
            dec = z3.And(*[
                rank[vals[i]] > rank[vals[i+1]] for i in range(3)
            ])
            s.add(z3.Not(inc), z3.Not(dec))

    assert s.check() == z3.sat  # lsb_lex_order supplies an explicit model
    m = s.model()
    return sorted(range(1, N+1), key=lambda v: m[rank[v]].as_long())
```

Finally, the finite bad-step sets from Lemma 10 can be computed explicitly:

```python
def divisors(t):
    ans = set()
    for d in range(1, int(t**0.5) + 1):
        if t % d == 0:
            ans.add(d)
            ans.add(t // d)
    return ans

def bad_steps_in_finite_permutation(order, n):
    pos = {v: i for i, v in enumerate(order)}
    bad = set()
    for v in order:
        if v > n and pos[v] < pos[n]:
            bad |= divisors(v - n)
    return bad
```

Useful searches would measure:

1. how long dyadic descents can be made while maintaining finite four-AP avoidance;
2. the growth and additive structure of affine record sets in large structured avoiders;
3. whether finite fair-prefix constraints force interactions absent from unrestricted finite orders;
4. whether hierarchical perturbations of `lsb_lex_order` can repair its non-\(\omega\) order type while preserving four-term avoidance.

## Route Diagnosis

**Proved ledger.**

- Every anchor \(r\) and direction \(d\) supports infinitely many dyadically scaled increasing three-APs.
- In a four-AP avoider, every such triple is capped by the fourth term occurring before its third term.
- Every affine ray has infinitely many suffix records.
- Three record coefficients in arithmetic progression force an increasing four-AP.
- Every pair of affine records forces an exact \(0,1,3,2\) order on the associated four-AP.
- Each fixed integer is the first record on \(n+q\mathbb N_0\) for all but finitely many \(q\).
- The global suffix-record set can be an arbitrary prescribed infinite set.
- Least-significant-bit lexicographic order gives nested finite orders avoiding even monotone three-APs, so no unrestricted finite forcing threshold exists.

**Plausible but unproved targets.**

- Some affine ray of every permutation has a suffix-record set containing a three-AP.
- There exist \(n,q\) such that \(q\) is simultaneously good for \(n,n+q,n+2q\).
- The forced dyadic caps on translated rays cannot all coexist in an order of type \(\omega\).

Each would imply the desired theorem, but none follows from the DEGS descent argument; the first two are likely of comparable additive-ordering difficulty to the original problem.

**Dead ends.**

- Merely iterating a blocker does not create an infinite descending chain of positions.
- The dyadic scale of the forced three-AP cannot be bounded.
- The forced differences generally become larger than the anchor, so the left-extension half of Lemma 3 becomes unavailable.
- The global suffix-record set may be arbitrarily sparse and three-AP-free.
- Purely finite SAT obstruction extraction cannot prove unavoidability, because explicit finite avoiders exist for every \(N\).

The most promising continuation is no longer a direct repetition of the DEGS argument. It should either attack the simultaneous affine-record condition using the finite divisor structure of bad steps, or pursue a disproof by starting from the least-significant-bit order and designing a fair, order-type-\(\omega\) repair scheme whose inevitable three-term “repairs” remain isolated.