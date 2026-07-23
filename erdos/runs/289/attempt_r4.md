STATUS: BLOCKED

## Result

Route 4 yields an exceptionally strong exact reservoir: for every \(m\ge1\), there are exactly \(m\) admissible separated dimers whose sum is
\[
1-\frac1{Q_m},
\qquad
Q_0=1,\quad Q_{j+1}=2Q_j(2Q_j+1).
\]
The residual is therefore exact, is a unit fraction, and decreases doubly exponentially. This reduces the problem to finitely completing the special residuals \(1/Q_m\). I prove precise denominator and \(p\)-adic constraints on any such completion, and I show that two natural forms of the proposed completion theorem cannot work: a bounded number of blocks cannot cover a fixed-width interval of the full common-denominator lattice, and no fixed affine-in-\(Q_m\) block template can complete infinitely many residuals. I did not obtain a finite completion of \(1/Q_m\), so the route remains blocked at the exact-arithmetic step.

## Complete Argument

### 1. An exact separated reservoir with arbitrary block count

Define
\[
Q_0=1,\qquad Q_{j+1}=2Q_j(2Q_j+1)
\]
and
\[
I_j=[2Q_j,\,2Q_j+1]_{\mathbb N}.
\]

#### Lemma 1
For every \(j\ge0\),
\[
\sum_{n\in I_j}\frac1n
=\frac1{Q_j}-\frac1{Q_{j+1}}.
\]

#### Proof
For any positive integer \(Q\),
\[
\frac1{2Q}+\frac1{2Q+1}
=\frac{4Q+1}{2Q(2Q+1)}.
\]
On the other hand,
\[
\frac1Q-\frac1{2Q(2Q+1)}
=\frac{2(2Q+1)-1}{2Q(2Q+1)}
=\frac{4Q+1}{2Q(2Q+1)}.
\]
Putting \(Q=Q_j\) and using \(Q_{j+1}=2Q_j(2Q_j+1)\) proves the identity. ∎

#### Lemma 2
The intervals \(I_0,I_1,\dots\) have length \(2\) and are pairwise separated by at least one omitted integer.

#### Proof
Each \(I_j\) has length \(2\). The left endpoint of \(I_{j+1}\) is
\[
2Q_{j+1}=4Q_j(2Q_j+1).
\]
The right endpoint of \(I_j\) is \(2Q_j+1\). Hence
\[
2Q_{j+1}-(2Q_j+1)
=8Q_j^2+2Q_j-1\ge9
\]
because \(Q_j\ge1\). In particular,
\[
2Q_{j+1}\ge (2Q_j+1)+2.
\]
Thus the required gap condition holds. ∎

#### Proposition 3: exact reservoir
For every \(m\ge1\),
\[
\sum_{j=0}^{m-1}\sum_{n\in I_j}\frac1n
=1-\frac1{Q_m}.
\]

#### Proof
By Lemma 1, the sum telescopes:
\[
\sum_{j=0}^{m-1}
\left(\frac1{Q_j}-\frac1{Q_{j+1}}\right)
=\frac1{Q_0}-\frac1{Q_m}
=1-\frac1{Q_m}.
\]
The geometric conditions follow from Lemma 2. ∎

The first values are
\[
Q_0=1,\quad Q_1=6,\quad Q_2=156,\quad Q_3=97656,
\]
and the first intervals are
\[
[2,3],\quad[12,13],\quad[312,313],\quad
[195312,195313].
\]
For example,
\[
\left(\frac12+\frac13\right)
+\left(\frac1{12}+\frac1{13}\right)
=1-\frac1{156}.
\]

The approximation is extremely rapid.

#### Lemma 4
For every \(m\ge1\),
\[
Q_m>4^{\,2^m-1},
\qquad
0<1-\sum_{j=0}^{m-1}w(I_j)
<4^{1-2^m}.
\]

#### Proof
We have \(Q_1=6>4\). Also
\[
Q_{j+1}=2Q_j(2Q_j+1)>4Q_j^2.
\]
If \(Q_j>4^{2^j-1}\), then
\[
Q_{j+1}>4\left(4^{2^j-1}\right)^2
=4^{2^{j+1}-1}.
\]
The residual estimate follows from Proposition 3. ∎

Thus the analytic part of Route 4 can be made completely exact: for every prescribed reservoir count \(m\), the error is not merely small but is exactly the explicitly controlled unit fraction \(1/Q_m\).

---

### 2. The exact completion problem isolated

The following is sufficient to solve the original problem.

#### Proposition 5: fixed-count completion criterion
Suppose there exist integers \(c\ge1\) and \(m_0\) such that, for every \(m\ge m_0\), there are exactly \(c\) admissible pairwise separated intervals \(J_{m,1},\dots,J_{m,c}\), mutually separated and all lying to the right of \(I_{m-1}\), satisfying
\[
\sum_{\ell=1}^c w(J_{m,\ell})=\frac1{Q_m}.
\]
Then \(P(k)\) holds for every \(k\ge m_0+c\).

#### Proof
Given \(k\ge m_0+c\), put \(m=k-c\). Take the \(m\) reservoir intervals
\[
I_0,\dots,I_{m-1}
\]
and the \(c\) correction intervals \(J_{m,1},\dots,J_{m,c}\). By assumption all \(k\) intervals satisfy the separation and length conditions. Proposition 3 gives
\[
\sum_{j=0}^{m-1}w(I_j)
+\sum_{\ell=1}^c w(J_{m,\ell})
=
\left(1-\frac1{Q_m}\right)+\frac1{Q_m}
=1.
\]
Thus \(P(k)\) holds. ∎

This is the exact point where Route 4 is blocked: no such finite completion family is known here.

---

### 3. Arithmetic restrictions on a completion

The residual denominators have substantial structure.

#### Lemma 6
For every \(m\ge0\),
\[
v_2(Q_m)=m.
\]
Moreover,
\[
Q_m=2^m\prod_{j=0}^{m-1}(2Q_j+1),
\]
and the odd integers \(2Q_j+1\) are pairwise coprime.

#### Proof
Since \(2Q_j+1\) is odd,
\[
v_2(Q_{j+1})=1+v_2(Q_j).
\]
Starting with \(v_2(Q_0)=0\) proves the first assertion. Iterating the recurrence gives the displayed factorization.

If \(i<j\), then \(2Q_i+1\mid Q_j\). Therefore
\[
2Q_j+1\equiv1\pmod{2Q_i+1},
\]
so
\[
\gcd(2Q_i+1,2Q_j+1)=1.
\]
∎

Any completion must carry all prime-power factors of \(Q_m\) in its least common multiple.

#### Lemma 7: denominator inheritance
Let \(S\) be any finite set of positive integers and suppose
\[
\sum_{n\in S}\frac1n=\frac AQ
\]
in lowest terms. Then
\[
Q\mid \operatorname{lcm}(S).
\]

#### Proof
Let \(L=\operatorname{lcm}(S)\). Then
\[
\sum_{n\in S}\frac1n
=\frac{1}{L}\sum_{n\in S}\frac Ln.
\]
After reducing this fraction, its denominator divides \(L\). Since \(A/Q\) is in lowest terms, \(Q\mid L\). ∎

There is also a sharpened version of the maximal-valuation congruence for a unit-fraction target.

#### Lemma 8: local congruence for \(1/Q\)
Suppose
\[
\sum_{n\in S}\frac1n=\frac1Q.
\]
Let
\[
L=\operatorname{lcm}(S),\quad
e=v_p(L),\quad f=v_p(Q),
\]
and write
\[
L=p^eU,\qquad Q=p^fV,
\qquad p\nmid UV.
\]
For each \(n\in S\) with \(v_p(n)=e\), write \(n=p^eu_n\). Then \(f\le e\), and
\[
\sum_{\substack{n\in S\\v_p(n)=e}}u_n^{-1}
\equiv
\begin{cases}
0\pmod p,&e>f,\\[4pt]
V^{-1}\pmod p,&e=f.
\end{cases}
\]

#### Proof
Lemma 7 gives \(Q\mid L\), so \(f\le e\). Clearing denominators gives
\[
\sum_{n\in S}\frac Ln=\frac LQ.
\]
If \(v_p(n)<e\), then \(L/n\) is divisible by \(p\). If \(v_p(n)=e\), then
\[
\frac Ln=\frac U{u_n}\equiv Uu_n^{-1}\pmod p.
\]
Thus the left side, modulo \(p\), is
\[
U\sum_{v_p(n)=e}u_n^{-1}.
\]

If \(e>f\), then \(L/Q\) is divisible by \(p\), giving the first congruence. If \(e=f\), then
\[
\frac LQ=\frac UV\equiv UV^{-1}\pmod p.
\]
Since \(U\) is invertible modulo \(p\), division by \(U\) gives the second congruence. ∎

For a completion of \(1/Q_m\), Lemma 6 and Lemma 8 imply:

- the maximal selected \(2\)-adic valuation is at least \(m\);
- if it is exactly \(m\), the number of selected denominators attaining it is odd;
- if it is greater than \(m\), that number is even.

These conditions do not produce a contradiction, but they are exact pruning conditions for any completion search.

---

### 4. A broad bounded correction library cannot cover the full lattice

The strongest natural interpretation of the Route 4 completion lemma would ask a bounded number of blocks to represent every rational in a fixed real interval belonging to the full common-denominator lattice. That is impossible by counting.

#### Proposition 9
Fix \(C\in\mathbb N\) and \(\delta>0\). Let
\[
L_N=\operatorname{lcm}(1,2,\dots,N).
\]
For all sufficiently large \(N\), no real interval \(J\) of length \(\delta\) has the property that every point of
\[
J\cap \frac1{L_N}\mathbb Z
\]
is representable as a sum of reciprocals of at most \(C\) integer intervals contained in \([1,N]_{\mathbb N}\).

This remains true without imposing separation or minimum interval length.

#### Proof
There are at most \(N^2\) choices for one ordered pair of endpoints. Hence the number of collections of at most \(C\) intervals is at most
\[
\sum_{c=0}^C N^{2c}\le (C+1)N^{2C}.
\]
Consequently, at most this many distinct rational sums can be produced.

We next give an exponential lower bound on \(L_N\). Every binomial coefficient \(\binom Nk\) divides \(L_N\). Indeed, for each prime \(p\),
\[
v_p\binom Nk
=
\sum_{r\ge1}
\left(
\left\lfloor\frac N{p^r}\right\rfloor
-\left\lfloor\frac k{p^r}\right\rfloor
-\left\lfloor\frac{N-k}{p^r}\right\rfloor
\right).
\]
Each summand is either \(0\) or \(1\), and there are at most
\(\lfloor\log_p N\rfloor=v_p(L_N)\) potentially nonzero summands. Thus
\[
v_p\binom Nk\le v_p(L_N)
\]
for every \(p\).

Since the \(N+1\) binomial coefficients sum to \(2^N\), at least one is at least \(2^N/(N+1)\). Therefore
\[
L_N\ge\frac{2^N}{N+1}.
\]

Every interval of length \(\delta\) contains at least \(\delta L_N-1\) points of \((1/L_N)\mathbb Z\). For sufficiently large \(N\),
\[
\delta L_N-1>(C+1)N^{2C}.
\]
There are then more lattice points in \(J\) than possible bounded-block sums, so not all can be represented. ∎

This does not exclude a completion theorem for the single special sequence \(1/Q_m\), nor one for intervals whose width shrinks exponentially with \(N\). It does show that a bounded correction library cannot provide uniform coverage of a fixed-width interval of the full denominator lattice.

---

### 5. Fixed affine block templates cannot complete the reservoir

The simplest possible parameterized completion would use a fixed number of fixed-length blocks whose endpoints are affine functions of \(Q_m\). Such a template is impossible.

#### Proposition 10
Let
\[
D_t(q)=A_tq+B_t
\]
be finitely many positive affine functions with \(A_t>0\). There is no identity
\[
\sum_{t=1}^T\frac1{D_t(q)}=\frac1q
\]
holding for infinitely many positive integers \(q\), unless every \(B_t=0\).

Consequently, no fixed collection of fixed-length intervals with affine-in-\(q\) endpoints can represent \(1/q\) for infinitely many \(q\).

#### Proof
If the identity holds for infinitely many \(q\), the two rational functions are identical.

Suppose some \(B_t\ne0\), and let
\[
\rho=-\frac{B_t}{A_t}\ne0.
\]
Group all denominators having the same zero \(\rho\). Each such denominator has the form
\[
A_s(q-\rho),
\]
and the sum of their residues at \(q=\rho\) is
\[
\sum_s\frac1{A_s}>0.
\]
Thus the left side has a nonremovable pole at \(\rho\). The function \(1/q\) is regular there, a contradiction. Hence every \(B_t=0\).

Now consider a fixed-length interval beginning at \(Aq+B\). It contains both denominators
\[
Aq+B,\qquad Aq+B+1.
\]
The constants \(B\) and \(B+1\) cannot both be zero. Therefore such an interval necessarily introduces a nonzero pole and cannot occur in an identity valid for infinitely many \(q\). ∎

In particular, a completion of \(1/Q_m\), if it exists uniformly in \(m\), must use genuinely nonlinear endpoint formulas, changing combinatorial templates, or both.

---

### 6. Ledger

**Proved**

1. The exact reservoir identity
   \[
   1-\frac1{Q_m}
   =\sum_{j=0}^{m-1}
   \left(\frac1{2Q_j}+\frac1{2Q_j+1}\right).
   \]
2. All reservoir intervals are admissible and separated.
3. The residual tends to zero doubly exponentially.
4. A fixed-count completion of every \(1/Q_m\) would prove the eventual assertion.
5. Every completion denominator lcm must be divisible by \(Q_m\).
6. Exact maximal-\(p\)-adic congruences for a unit-fraction target.
7. A bounded number of blocks cannot cover a fixed-width interval of the full \(1/L_N\) lattice.
8. No fixed affine, fixed-length block template can complete infinitely many residuals.

**Plausible but unproved**

1. Some \(1/Q_m\), beginning with \(1/6\) or \(1/156\), may admit finite separated-block completions far to the right.
2. There may be nonlinear completion identities adapted to
   \[
   Q_{m+1}=2Q_m(2Q_m+1).
   \]
3. Exact subset sums in an exponentially narrow residual window might behave much better than Proposition 9 permits for a fixed-width interval.

**Dead ends**

1. The infinite dimer expansion alone does not solve the problem: every finite prefix leaves the positive residual \(1/Q_m\).
2. A universal bounded correction library covering every full-lattice rational in a fixed-width interval is impossible by Proposition 9.
3. Fixed affine endpoint formulas cannot cap the reservoir by Proposition 10.
4. First-order \(p\)-adic conditions do not currently contradict a completion; the maximal terms can cancel in permitted configurations.

## Self-Audit

1. **The exact reservoir is only an approximation mechanism, not an exact representation of \(1\).**  
   This is the central weakness. I have explicitly retained the residual \(1/Q_m\) and have not treated its smallness as completion. The telescoping identity itself is exact.

2. **Proposition 9 rules out only a broad version of the completion theorem.**  
   It does not address the sparse residual sequence \(1/Q_m\) or exponentially narrow intervals. Its stated conclusion nevertheless follows rigorously from a polynomial-versus-exponential counting argument.

3. **Proposition 10 only excludes fixed affine, fixed-length templates.**  
   Nonlinear formulas, growing interval lengths, or templates changing with \(m\) remain possible. The restricted claim is secure because any nonzero affine shift creates an uncancellable pole.

## Computations To Verify

The following Python uses exact rational arithmetic.

```python
from fractions import Fraction
from math import gcd, lcm

def verify(intervals, target=Fraction(1, 1)):
    intervals = sorted(intervals)
    for a, b in intervals:
        assert isinstance(a, int) and isinstance(b, int)
        assert 1 <= a < b
    for (_, b1), (a2, _) in zip(intervals, intervals[1:]):
        assert a2 >= b1 + 2
    total = sum(
        (Fraction(1, n) for a, b in intervals for n in range(a, b + 1)),
        Fraction(0, 1)
    )
    return total == target, total

def reservoir(m):
    q = 1
    intervals = []
    for _ in range(m):
        intervals.append((2*q, 2*q + 1))
        q = 2*q*(2*q + 1)
    return q, intervals

for m in range(1, 8):
    q, intervals = reservoir(m)
    ok, total = verify(intervals, Fraction(1, 1) - Fraction(1, q))
    print(m, q, intervals[-1], ok, total)
```

Expected initial output includes
```text
1 6 (2, 3)
2 156 (12, 13)
3 97656 (312, 313)
```

A complete bounded search for a correction by exactly `c` blocks with endpoints at most `N`:

```python
from fractions import Fraction

def find_block_completion(target, c, lo, N):
    """
    Search all ordered separated blocks [a,b], lo <= a < b <= N,
    for exactly c blocks summing to target.
    Exact but exponential.
    """

    def rec(min_a, remaining_blocks, residual):
        if remaining_blocks == 0:
            return [] if residual == 0 else None
        if residual <= 0:
            return None

        # Minimal room: each future block needs two positions,
        # and consecutive blocks need at least one omitted position.
        if min_a + 3*remaining_blocks - 2 > N:
            return None

        for a in range(min_a, N):
            weight = Fraction(0, 1)
            for b in range(a, N + 1):
                weight += Fraction(1, b)

                if weight > residual:
                    break
                if b == a:
                    continue

                tail = rec(b + 2, remaining_blocks - 1,
                           residual - weight)
                if tail is not None:
                    return [(a, b)] + tail
        return None

    return rec(lo, c, target)

def test_residual(level, c, N):
    q, prefix = reservoir(level)
    lo = prefix[-1][1] + 2
    correction = find_block_completion(Fraction(1, q), c, lo, N)
    if correction is None:
        return None
    full = prefix + correction
    assert verify(full, Fraction(1, 1))[0]
    return full

# Suggested tests:
# for level in (1, 2, 3):
#     for c in range(1, 8):
#         ans = test_residual(level, c, N=<chosen bound>)
#         if ans:
#             print(level, c, ans)
```

A faster dimer-only correction search:

```python
def find_dimer_completion(q, c, lo, N):
    target = Fraction(1, q)

    def rec(next_start, left, residual):
        if left == 0:
            return [] if residual == 0 else None
        if residual <= 0:
            return None
        if next_start + 3*(left - 1) + 1 > N:
            return None

        for n in range(next_start, N):
            w = Fraction(1, n) + Fraction(1, n + 1)
            if w > residual:
                continue
            tail = rec(n + 3, left - 1, residual - w)
            if tail is not None:
                return [(n, n + 1)] + tail
        return None

    return rec(lo, c, target)
```

The \(p\)-adic completion congruence can be checked as follows:

```python
def vp(n, p):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e

def check_unit_target_congruence(intervals, Q, p):
    S = [n for a, b in intervals for n in range(a, b + 1)]
    L = 1
    for n in S:
        L = lcm(L, n)

    if L % Q:
        return False

    e = vp(L, p)
    f = vp(Q, p)
    if f > e:
        return False

    U = L // (p**e)
    V = Q // (p**f)

    lhs = 0
    for n in S:
        if vp(n, p) == e:
            u = n // (p**e)
            lhs = (lhs + pow(u % p, -1, p)) % p

    rhs = 0 if e > f else pow(V % p, -1, p)
    return lhs == rhs % p
```

The most informative finite experiments would be:

1. Search for completions of \(1/6\), then \(1/156\), with \(2\)–\(8\) blocks.
2. Search both dimer-only and unrestricted block models.
3. Record endpoint patterns relative to \(Q_m\), especially nonlinear patterns.
4. Test whether any completion count \(c\) recurs for both \(Q_1\) and \(Q_2\).
5. Apply Lemma 8 for every prime dividing \(Q_m\) before exact meet-in-the-middle search.

## Route Diagnosis

The analytic reservoir portion of Route 4 works better than expected: it produces arbitrary numbers of legal blocks and an exact, doubly exponentially small residual. The route is nevertheless blocked at the arithmetic completion problem
\[
\frac1{Q_m}=\sum_{\ell=1}^c w(J_{m,\ell}).
\]
A fixed-count solution of this special problem would settle the original problem, but no such completion was obtained. Broad full-lattice coverage and affine parameterized templates are now rigorously excluded, so a successful continuation must exploit the special nonlinear factorization of \(Q_m\).

A fresh attempt should prioritize exact searches for caps of \(1/6\) and \(1/156\), looking for nonlinear identities that persist under \(Q\mapsto2Q(2Q+1)\). If no such pattern emerges, Route 1—searching for reusable replacement gadgets—appears more promising than a general-purpose correction library.