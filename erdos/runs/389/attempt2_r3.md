STATUS: BLOCKED

## Result

Route 3 yields a sharp exact description of every large-prime bad event. For odd \(p>m\), conditional on \(p^t\Vert X-j\) at one of the endpoint positions \(0\le j<\lceil m/2\rceil\), the compensating positive levels form a stationary two-state Markov chain with transition probability \(1/p\) bias; this gives an exact transfer-matrix formula for the bad residue classes modulo \(p^L\). It also shows that the idealized local bad-event mass already exceeds \(1\) per endpoint, so a union bound cannot work. More decisively, on an actual dyadic interval the top-prime events at each endpoint have total probability \(\log 2+o(1)\), while their atomic lopsided dependency graph is asymptotically almost complete. Grouping by endpoint avoids that defect but then a lopsided nonedge requires lower bounds for correlations of shifted large-prime-factor events, reducing to averaged systems \(ap-bq=l-j\) with both \(p,q\) prime and, for the full problem, additional prime-power digit restrictions. No unconditional theorem strong enough to supply those lower correlations is available here. Thus the local \(p\)-adic side of Route 3 can be made exact, but its archimedean interval-transference step remains blocked by a shifted-friable/prime-correlation problem of comparable strength to the original problem.

## Complete Argument

### 1. Exact normal form of a bad large-prime chain

Fix \(m>0\), put

\[
H=\left\lceil\frac m2\right\rceil,\qquad Y=2X-m,
\]

and let \(p>m\) be prime. Define

\[
L=L_p(X)=\max\{a:p^a\le Y\}.
\]

For \(q=p^a>m\), writing \(r_a=X\bmod p^a\),

\[
E_{p^a}(m,X)
=
\left\lfloor\frac{2r_a-m}{p^a}\right\rfloor.
\]

Since \(0\le r_a<p^a\),

\[
E_{p^a}=-1
\iff
0\le r_a<H,
\]

and

\[
E_{p^a}=1
\iff
r_a\ge \left\lceil\frac{p^a+m}{2}\right\rceil.
\]

#### Lemma 1: Endpoint-chain normal form

Suppose \(p>m\). If \(D_p(m,X)<0\), there is a unique \(j\in\{0,\ldots,H-1\}\) such that \(p\mid X-j\). Put

\[
t=v_p(X-j).
\]

Then \(1\le t\le L\), and

\[
\boxed{
D_p(m,X)
=
-t+
\#\left\{
a:t<a\le L,\ 
X\bmod p^a\ge
\left\lceil\frac{p^a+m}{2}\right\rceil
\right\}.
}
\]

In particular,

\[
D_p(m,X)<0
\iff
\#\{\text{positive levels above }t\}<t.
\]

**Proof.**

If \(D_p<0\), at least one level is negative. If \(E_{p^a}=-1\), then

\[
X\bmod p^a=j
\]

for some \(0\le j<H\), hence \(p\mid X-j\). Since \(p>m>H-1\), a prime \(p\) cannot divide two distinct numbers among

\[
X,\ X-1,\ldots,X-H+1.
\]

Thus \(j\) is unique.

For \(a\le t\), we have \(X\bmod p^a=j\). Since \(j<H\), every such level contributes \(-1\).

For \(a>t\), suppose another negative level occurred. Then

\[
r_a=X\bmod p^a\in\{0,\ldots,H-1\}.
\]

But \(r_a\equiv j\pmod{p^t}\), while \(r_a,j<H<p^t\). Therefore \(r_a=j\), implying \(p^a\mid X-j\), contrary to \(a>t\). Thus every level above \(t\) is either \(0\) or \(1\), with the displayed criterion for being \(1\). Summing the levels proves the formula. ∎

This lemma completely localizes every bad event for \(p>m\): it belongs to one endpoint and consists of too few higher-level compensations.

---

### 2. The positive levels form an exact Markov chain

Assume now that \(p>m\) is odd and write

\[
p=2h+1.
\]

Suppose \(p^t\Vert X-j\), with \(0\le j<H\). Write the base-\(p\) expansion above the \(t\)-th place as

\[
X\bmod p^a=j+\sum_{\nu=t}^{a-1}d_\nu p^\nu.
\]

Here \(d_t\in\{1,\ldots,p-1\}\), while the later digits range over \(\{0,\ldots,p-1\}\).

Let \(Z_a\in\{0,1\}\) indicate whether \(E_{p^a}=1\).

#### Lemma 2: Two-state transition rule

For every \(a>t\),

\[
Z_a=
\begin{cases}
0,&d_{a-1}<h,\\
Z_{a-1},&d_{a-1}=h,\\
1,&d_{a-1}>h.
\end{cases}
\]

At the first level \(a=t+1\), \(Z_t=0\), and among the \(p-1=2h\) possible nonzero values of \(d_t\), exactly \(h\) produce \(Z_{t+1}=0\) and exactly \(h\) produce \(Z_{t+1}=1\).

**Proof.**

Let \(r_a=d_{a-1}p^{a-1}+r_{a-1}\). Positivity means

\[
2r_a-m\ge p^a.
\]

If \(d_{a-1}\le h-1\), then

\[
2r_a-m
\le
2(h-1)p^{a-1}+2(p^{a-1}-1)-m
<
(2h+1)p^{a-1}=p^a.
\]

If \(d_{a-1}\ge h+1\), then, because \(p^{a-1}\ge p>m\),

\[
2r_a-m
\ge
2(h+1)p^{a-1}-m
\ge p^a.
\]

If \(d_{a-1}=h\), then

\[
2r_a-m-p^a
=
2r_{a-1}-m-p^{a-1}.
\]

Thus positivity at level \(a\) is exactly positivity at level \(a-1\).

At \(a=t+1\), the middle digit \(d_t=h\) inherits the false state \(Z_t=0\). Among \(d_t=1,\ldots,2h\), the values \(1,\ldots,h\) therefore give state \(0\), and \(h+1,\ldots,2h\) give state \(1\). ∎

Conditional on \(p^t\Vert X-j\) and a uniformly chosen residue modulo \(p^L\), the sequence

\[
Z_{t+1},\ldots,Z_L
\]

is consequently a stationary Markov chain with transition matrix

\[
P_p=
\begin{pmatrix}
\dfrac{p+1}{2p}&\dfrac{p-1}{2p}\\[2mm]
\dfrac{p-1}{2p}&\dfrac{p+1}{2p}
\end{pmatrix},
\]

and initial distribution \((1/2,1/2)\). Its nontrivial eigenvalue is \(1/p\).

This is stronger than a heuristic independence statement: it is an exact finite combinatorial identity.

---

### 3. Exact transfer-matrix enumeration

Let \(s=L-t\). Define

\[
M_p(z)=
\begin{pmatrix}
h+1&hz\\
h&(h+1)z
\end{pmatrix},
\]

and, for \(s\ge1\),

\[
F_{p,s}(z)
=
(h,hz)M_p(z)^{s-1}
\binom11.
\]

The coefficient of \(z^r\) counts the choices of the \(s\) relevant digits that produce exactly \(r\) positive levels.

Set

\[
A_p(s,t)=\sum_{r=0}^{t-1}[z^r]F_{p,s}(z).
\]

#### Corollary 3: Number of bad residue classes

For one fixed endpoint \(j\), the number of residues modulo \(p^L\) giving \(D_p<0\) is

\[
\boxed{
b_{p,L}
=
1+\sum_{t=1}^{L-1}A_p(L-t,t).
}
\]

The initial \(1\) is the residue class \(X\equiv j\pmod{p^L}\), corresponding to \(t=L\). Consequently, because the \(H\) endpoint classes are disjoint modulo \(p\),

\[
\boxed{
\#\{x\bmod p^L:D_p(m,x)<0\}=H\,b_{p,L}.
}
\]

Thus the local bad density per endpoint is

\[
\beta_{p,L}=\frac{b_{p,L}}{p^L}.
\]

For example,

\[
\beta_{p,1}=\frac1p,
\]

\[
\beta_{p,2}=\frac{p+1}{2p^2},
\]

and

\[
\beta_{p,3}=\frac{p^2+4p-1}{4p^3}.
\]

The Markov description also gives the rigorous tail bound

\[
\Pr\left(\sum_{\nu=1}^{s}Z_\nu<t\right)
\le
2^{-s}\left(1+\frac1p\right)^{s-1}
\sum_{r=0}^{t-1}\binom sr.
\]

Indeed, every state path of length \(s\) has probability at most

\[
2^{-s}\left(1+\frac1p\right)^{s-1}.
\]

This quantifies the fact that, when there are many levels above \(t\), uncompensated chains become exponentially rare.

---

### 4. The exceptional case \(p=2>m\)

This occurs only when \(m=1\), with endpoint \(j=0\).

If \(2^t\Vert X\), then the level \(t+1\) is never positive: its residue is \(2^t\), and

\[
2\cdot2^t-1<2^{t+1}.
\]

At every subsequent level \(a\ge t+2\), positivity occurs exactly when the new binary digit is \(1\). Hence the number of bad residue classes per endpoint modulo \(2^L\) is

\[
\boxed{
b_{2,L}
=
1+
\sum_{t=1}^{L-1}
\sum_{r=0}^{t-1}
\binom{L-t-1}{r}.
}
\]

For instance \(b_{2,3}=3\): the bad residues modulo \(8\) are \(0,2,4\), while \(6\) has the compensating positive \(2^3\)-level. This agrees with the success \(m=1,X=6\).

---

### 5. Exact local masses already defeat a union bound

For fixed \(L\) and odd \(p\to\infty\), the dominant contribution comes from \(t=1\). To be bad, every one of the \(L-1\) possible compensating states must be \(0\). Its exact count is

\[
h(h+1)^{L-2}
\]

for \(L\ge2\). All \(t\ge2\) contributions are \(O_L(p^{L-2})\). Therefore

\[
\boxed{
\beta_{p,L}
=
\frac{2^{-(L-1)}}p+O_L\left(\frac1{p^2}\right).
}
\]

For an external scale \(z\), primes satisfying

\[
z^{1/(L+1)}<p\le z^{1/L}
\]

have cutoff \(L\) when \(p^L\le z<p^{L+1}\). Mertens’ theorem gives

\[
\sum_{z^{1/(L+1)}<p\le z^{1/L}}\frac1p
=
\log\left(1+\frac1L\right)+o(1).
\]

Thus the idealized local bad mass from the \(L\)-th prime-power scale is

\[
2^{-(L-1)}
\log\left(1+\frac1L\right).
\]

Already the first five scales have total

\[
\begin{aligned}
C_5={}&
\log2
+\frac12\log\frac32
+\frac14\log\frac43
+\frac18\log\frac54
+\frac1{16}\log\frac65\\
={}&1.007088\ldots>1.
\end{aligned}
\]

The full convergent series is approximately

\[
\sum_{L\ge1}2^{-(L-1)}
\log\left(1+\frac1L\right)
=
1.01566\ldots.
\]

This is not an interval-density theorem—the cutoff and the residue distribution cannot be separated that way on a short interval—but it is a rigorous diagnosis of the local model. Even for a single endpoint, a union bound over the exact bad residue densities is insufficient. With \(H\) endpoints the formal first moment is multiplied by \(H\).

---

### 6. Why independent-prime LLL merely reproduces CRT

Fix an external cutoff \(z\), and for each \(p\le z\) set

\[
L_p=\lfloor\log_p z\rfloor.
\]

If one chooses the residues modulo \(p^{L_p}\) independently, bad events belonging to distinct primes are independent. The local lemma is then trivial: choose an allowed coordinate for every prime and combine them by CRT.

The resulting period is

\[
Q_z=\prod_{p\le z}p^{L_p}
=\operatorname{lcm}(1,2,\ldots,\lfloor z\rfloor),
\]

and

\[
\log Q_z=\psi(z)\sim z.
\]

Thus the natural CRT representative can be of size \(e^{(1+o(1))z}\), not \(O(z)\). At that size, the cutoff \(z\) is no longer relevant and exponentially many new primes and prime powers are uncontrolled.

This is the precise archimedean obstruction: prime coordinates are independent on a complete residue system of exponential length, whereas the problem asks for a representative in an interval whose length is only comparable to the prime-power cutoff. A profinite or CRT solution does not yield a natural-number solution at the required scale.

---

### 7. Top-prime events on an actual interval

Let

\[
\Omega_T=\{X\in\mathbb Z:T\le X<2T\},
\]

with \(m\) fixed and \(T\to\infty\). Consider the prime band

\[
\mathcal P_T=\left\{p\text{ prime}:3\sqrt T<p\le \frac T3\right\}.
\]

For \(0\le j<H\), define

\[
A_{p,j}=\{X\in\Omega_T:p\mid X-j\}.
\]

For \(T\) sufficiently large, every \(p\in\mathcal P_T\) satisfies \(p>m\), and

\[
p^2>9T>2X-m=Y.
\]

Therefore every \(X\in A_{p,j}\) has

\[
D_p(m,X)=-1.
\]

For fixed \(j\), the events \(A_{p,j}\), \(p\in\mathcal P_T\), are pairwise disjoint. Indeed, if distinct \(p,q\in\mathcal P_T\) both divided \(X-j\), then

\[
pq>9T>X-j,
\]

which is impossible.

Moreover,

\[
\frac{|A_{p,j}|}{|\Omega_T|}
=
\frac1p+O\left(\frac1T\right).
\]

Hence, by Mertens’ theorem and the prime number theorem,

\[
\begin{aligned}
\Pr_{\Omega_T}\left(\bigcup_{p\in\mathcal P_T}A_{p,j}\right)
&=
\sum_{p\in\mathcal P_T}\frac1p+o(1)\\
&=
\log\log(T/3)-\log\log(3\sqrt T)+o(1)\\
&=
\boxed{\log2+o(1)}.
\end{aligned}
\]

Thus a single endpoint carries a grouped top-prime bad event of probability asymptotic to \(0.693\), even after all small primes have been removed.

---

### 8. The atomic lopsided graph is almost complete

Use the standard definition of a lopsided dependency graph: if \(A\) and \(B\) are nonadjacent, one must at least have

\[
\Pr(A\mid \overline B)\le \Pr(A).
\]

#### Lemma 4: Disjoint bad events must be adjacent

If \(A\) and \(B\) are disjoint events of positive probability, they must be adjacent in every such lopsided dependency graph.

**Proof.**

Since \(A\cap B=\varnothing\),

\[
\Pr(A\mid\overline B)
=
\frac{\Pr(A)}{1-\Pr(B)}
>
\Pr(A).
\]

Thus the required nonedge inequality fails. ∎

It follows immediately that, for each fixed endpoint \(j\), all the atomic events \(A_{p,j}\) form a clique.

The cross-endpoint situation is almost as bad. Fix \(j\ne l\) and one event \(A_{p,j}\). For each \(X\in A_{p,j}\), the integer \(X-l<2T\) can be divisible by at most one prime \(q>3\sqrt T\). Therefore at most

\[
|A_{p,j}|\le \frac Tp+2=O(\sqrt T)
\]

events \(A_{q,l}\) can intersect \(A_{p,j}\). But

\[
|\mathcal P_T|\sim \frac{T}{3\log T}.
\]

Hence \(A_{p,j}\) is disjoint from, and therefore forced to be adjacent to,

\[
|\mathcal P_T|-O(\sqrt T)
\]

events at every other endpoint. The mandatory lopsided graph is asymptotically almost complete.

In particular, the standard symmetric LLL criterion fails strongly. Events with \(p\asymp\sqrt T\) have probability \(\asymp T^{-1/2}\), while their forced degree is \(\asymp HT/\log T\). Thus

\[
e\,\Pr(A_{p,j})(d+1)
\gg
\frac{\sqrt T}{\log T}\longrightarrow\infty.
\]

This does not disprove every asymmetric or specially grouped local lemma, but it rigorously rules out the naive atomic implementation.

---

### 9. Endpoint grouping requires hard lower-correlation estimates

One can group all top-prime events at endpoint \(j\) into

\[
A_j=\bigcup_{p\in\mathcal P_T}A_{p,j},
\]

where

\[
\Pr(A_j)=\log2+o(1).
\]

A complete dependency graph on the \(H\) grouped events gives no LLL conclusion once \(H\ge2\), because

\[
\sum_{j=0}^{H-1}\Pr(A_j)
=
H\log2+o(1)>1.
\]

To omit even one edge between \(A_j\) and \(A_l\), the pairwise lopsided inequality requires

\[
\Pr(A_j\mid\overline{A_l})\le\Pr(A_j).
\]

This is equivalent to the lower-correlation estimate

\[
\boxed{
\Pr(A_j\cap A_l)
\ge
\Pr(A_j)\Pr(A_l).
}
\]

Thus an endpoint-grouped lopsided LLL does not merely need upper bounds for intersections. It needs lower bounds showing that shifted large-prime-factor events occur together at least as often as independence predicts.

Any point in \(A_{p,j}\cap A_{q,l}\) has representations

\[
X-j=ap,\qquad X-l=bq,
\]

where \(p,q\) are prime and \(a,b=O(\sqrt T)\). Consequently,

\[
\boxed{
ap-bq=l-j.
}
\]

For fixed \(a,b\), this is a two-prime linear problem. Summing over \(a,b\) gives an averaged shifted-semiprime correlation. Higher grouped intersections produce systems

\[
a_i p_i-a_r p_r=j_r-j_i.
\]

The full valuation events add constraints on the base-\(p_i\) digits of the cofactors, dictated by the Markov chain above.

Upper-bound sieve estimates may control such intersections from above, but the lopsided nonedge condition demands lower bounds. Establishing those lower bounds uniformly through all endpoint subsets is essentially the missing multidimensional shifted-friable/Buchstab theorem. Merely calling the events “approximately independent” does not prove the needed inequalities.

---

### 10. A sanity check: top smoothness alone is not the obstruction

For any fixed \(m\), take \(X=u^2\). Every prime factor of \(X\) is at most \(u\), while

\[
X-1=(u-1)(u+1)
\]

has every prime factor at most \(u+1\). For sufficiently large \(u\),

\[
(u+1)^2\le 2u^2-m=Y.
\]

Thus the first two endpoints \(X\) and \(X-1\) have no prime factor exceeding \(\sqrt Y\).

This supplies deterministic avoidance of the top obstruction at two endpoints, but it does not solve the valuation problem. The example \(m=3,X=16=4^2\) has both endpoints \(16,15\) below the top-factor threshold, yet

\[
D_2(3,16)=-4.
\]

Therefore even a successful local lemma for the grouped top events would still have to handle the exact lower prime-power chains.

---

### 11. Precise point of blockage

The exact \(p\)-adic part of Route 3 is now reduced to explicit finite-state weights. What remains is an interval theorem of the form:

> In \([T,2T]\), the union of all weighted endpoint prime-chain deficit events does not cover every integer.

The two natural LLL implementations fail for different rigorous reasons:

1. **Prime-coordinate/product implementation:** distinct primes are independent only modulo the exponential period \(Q_z\), so it gives a CRT/profinite point with no representative at the correct archimedean scale.

2. **Actual-interval atomic implementation:** mutually exclusive residue events are forced lopsided neighbors, making the dependency graph almost complete and defeating the standard LLL criteria.

3. **Endpoint-grouped implementation:** each event has probability \(\log2+o(1)\), and removing dependency edges requires lower correlation estimates for shifted large-prime factors and their prime-power digit refinements.

No proof of the required lower correlations, no valid entropy-compression map preserving an actual representative in \([T,2T]\), and no substitute covering-radius theorem is presently obtained. This is a block of comparable strength, not a routine omitted step.

## Self-Audit

1. **The Markov-chain enumeration applies only to \(p>m\), with \(p=2,m=1\) handled separately.** It does not analyze the finitely many small primes. I believe the stated result is complete because every use explicitly retains the hypothesis \(p>m\), and the binary exceptional case is proved separately. Small primes can be pre-sieved but are not claimed solved by this lemma.

2. **The scale sum \(1.01566\ldots\) is not asserted to be an actual interval expectation.** Treating it as such would be an unjustified equidistribution step when \(p^L\) is comparable with \(T\). I believe the limited claim is sound because it is stated only as the sum of exact complete-residue local densities over prime scales; the failure to transfer it to \([T,2T]\) is precisely identified as the main obstruction.

3. **The analysis proves failure of naive atomic and complete-grouped LLL criteria, not impossibility of every conceivable entropy-compression argument.** A new probability space or a strong arithmetic correlation theorem could evade the diagnosis. I nevertheless believe the route is correctly marked BLOCKED because no such construction is supplied, and the exact nonedge condition demonstrably requires currently unproved lower correlations of shifted factorization events.

## Computations To Verify

```python
from math import comb, isqrt, e
from collections import defaultdict

def primes_upto(n):
    if n < 2:
        return []
    isprime = bytearray(b"\x01") * (n + 1)
    isprime[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if isprime[p]:
            for q in range(p * p, n + 1, p):
                isprime[q] = 0
    return [p for p in range(2, n + 1) if isprime[p]]

def D_value(m, X, p):
    """Exact D_p(m,X), using Python floor division."""
    Y = 2 * X - m
    q = p
    ans = 0
    while q <= Y:
        ans += (2 * (X % q) - (m % q)) // q
        q *= p
    return ans

def is_good_mX(m, X):
    Y = 2 * X - m
    return all(D_value(m, X, p) >= 0 for p in primes_upto(Y))

# Mandatory regression tests.
assert D_value(1, 30, 3) == -1
assert D_value(3, 16, 2) == -4
assert is_good_mX(1, 6)
assert is_good_mX(2, 6)

def brute_bad_residues(m, p, L):
    """Artificial fixed-cutoff bad residues modulo p^L."""
    mod = p ** L
    bad = []
    powers = [p ** a for a in range(1, L + 1)]
    for x in range(mod):
        d = sum((2 * (x % q) - (m % q)) // q for q in powers)
        if d < 0:
            bad.append(x)
    return bad

def endpoint_bad_count_odd(p, L):
    """
    Number b_{p,L} of bad residue classes for one endpoint,
    for odd p>m. Independent of m and endpoint j in that range.
    """
    assert p % 2 == 1
    h = (p - 1) // 2
    total = 1  # t = L

    for t in range(1, L):
        s = L - t

        # Key: (current state, number of positive levels) -> count.
        dp = {(0, 0): h, (1, 1): h}

        for _ in range(s - 1):
            ndp = defaultdict(int)
            for (state, ones), count in dp.items():
                if state == 0:
                    transitions = [(0, h + 1), (1, h)]
                else:
                    transitions = [(0, h), (1, h + 1)]
                for newstate, multiplicity in transitions:
                    ndp[(newstate, ones + newstate)] += count * multiplicity
            dp = ndp

        total += sum(
            count for (state, ones), count in dp.items()
            if ones < t
        )
    return total

def endpoint_bad_count_binary(L):
    """The exceptional p=2,m=1 count."""
    total = 1  # t=L
    for t in range(1, L):
        n = L - t - 1
        total += sum(comb(n, r) for r in range(min(t, n + 1)))
    return total

def verify_transfer_formula(limit_mod=2_000_000):
    ps = primes_upto(100)
    for m in range(1, 20):
        H = (m + 1) // 2
        for p in ps:
            if p <= m:
                continue
            for L in range(1, 7):
                if p ** L > limit_mod:
                    break
                brute = len(brute_bad_residues(m, p, L))
                if p == 2:
                    predicted = H * endpoint_bad_count_binary(L)
                else:
                    predicted = H * endpoint_bad_count_odd(p, L)
                assert brute == predicted, (m, p, L, brute, predicted)

verify_transfer_formula()

# Check the displayed small-L formulas for odd primes.
for p in [3, 5, 7, 11, 13]:
    assert endpoint_bad_count_odd(p, 1) == 1
    assert endpoint_bad_count_odd(p, 2) == (p + 1) // 2
    assert endpoint_bad_count_odd(p, 3) == (p * p + 4 * p - 1) // 4

def top_band_events(m, T):
    """
    Build A_{p,j} for 3 sqrt(T) < p <= T/3.
    Intended for moderate T, e.g. 10^4 to 10^6.
    """
    H = (m + 1) // 2
    ps = [
        p for p in primes_upto(T // 3)
        if p * p > 9 * T
    ]
    events = {}

    for j in range(H):
        for p in ps:
            low = T - j
            high = 2 * T - j
            first = ((low + p - 1) // p) * p
            xs = {n + j for n in range(first, high, p)}
            assert xs
            assert all(T <= X < 2 * T for X in xs)
            assert all(p * p > 2 * X - m for X in xs)
            events[(p, j)] = xs

    # Same-endpoint top events must be pairwise disjoint.
    for j in range(H):
        keys = [(p, j) for p in ps]
        for a in range(len(keys)):
            for b in range(a):
                assert events[keys[a]].isdisjoint(events[keys[b]])

    return ps, events

def mandatory_lopsided_statistics(m, T):
    ps, events = top_band_events(m, T)
    keys = list(events)
    degree = {key: 0 for key in keys}

    # Every disjoint pair is a mandatory lopsided edge.
    for a in range(len(keys)):
        for b in range(a):
            ka, kb = keys[a], keys[b]
            if events[ka].isdisjoint(events[kb]):
                degree[ka] += 1
                degree[kb] += 1

    pmax = max(len(events[k]) / T for k in keys)
    dmax = max(degree.values())
    grouped_prob = {}
    H = (m + 1) // 2
    for j in range(H):
        union = set()
        for p in ps:
            union |= events[(p, j)]
        grouped_prob[j] = len(union) / T

    return {
        "number_of_primes": len(ps),
        "pmax": pmax,
        "mandatory_dmax": dmax,
        "symmetric_LLL_quantity": e * pmax * (dmax + 1),
        "grouped_endpoint_probabilities": grouped_prob,
    }

# Suggested runs:
# for T in [10_000, 30_000, 100_000]:
#     print(T, mandatory_lopsided_statistics(m=7, T=T))

def bad_prime_ledger(m, X):
    """Exact list of all witness primes and their level sequences."""
    Y = 2 * X - m
    out = {}
    for p in primes_upto(Y):
        levels = []
        q = p
        while q <= Y:
            levels.append((q, (2 * (X % q) - (m % q)) // q))
            q *= p
        if sum(v for q, v in levels) < 0:
            out[p] = levels
    return out

# Search after a finite small-prime presieve and classify the surviving failures.
def presieved_interval(m, T, P0):
    small = [p for p in primes_upto(P0)]
    survivors = []
    for X in range(T, 2 * T):
        if all(D_value(m, X, p) >= 0 for p in small):
            survivors.append((X, bad_prime_ledger(m, X)))
    return survivors
```

The most important finite experiments are:

1. Verify the transfer-matrix formula for many \(m,p,L\).
2. Measure the mandatory disjointness graph and confirm that its degree is \(\asymp T/\log T\).
3. After small-prime pre-sieving, group failures by endpoint and compare actual pair and triple intersections against products of marginal probabilities.
4. For every intersection \(A_{p,j}\cap A_{q,l}\), record the cofactors \(a,b\) in
   \[
   ap-bq=l-j
   \]
   to determine whether any structured averaged correlation is visible.

## Route Diagnosis

**Proved ledger**

- Every bad event for \(p>m\) belongs to a unique endpoint.
- Conditional on \(p^t\Vert X-j\), its exact deficit is \(-t\) plus the number of higher positive levels.
- For odd \(p>m\), those positive levels form an exact stationary two-state Markov chain.
- The bad residue classes modulo \(p^L\) have an explicit transfer-matrix enumeration.
- Their large-\(p\), fixed-\(L\) density is
  \[
  2^{-(L-1)}/p+O_L(p^{-2}).
  \]
- The resulting idealized first-moment mass exceeds \(1\) even at one endpoint.
- On a dyadic interval, one endpoint’s top-prime subevent has probability \(\log2+o(1)\).
- Atomic top-prime events force an almost-complete lopsided graph.
- Endpoint grouping requires lower shifted-factorization correlations, not merely upper bounds.
- Independent-prime resampling works only on an exponentially long CRT period.

**Plausible but unproved**

- For every fixed \(m\), the exact good \(X\) may have a positive but extremely small density.
- Shifted endpoint bad events may be asymptotically independent after suitable Buchstab decomposition.
- A weighted cluster expansion using the exact Markov factors may converge if one can prove the necessary interval correlation estimates.

**Dead ends**

- Standard symmetric LLL on atomic prime events fails by a factor \(\gg\sqrt T/\log T\).
- Treating distinct primes as independent gives only a profinite/CRT representative.
- Grouping solely by endpoint leaves events of probability \(\log2+o(1)\) and requires hard lower correlations.
- A union bound fails even in the exact local residue model.
- Top-factor control alone misses examples such as \((m,X)=(3,16)\).

**Sharp block**

The missing ingredient is an interval-level lower-correlation theorem for shifted endpoint factorization events, refined by prime-power digit states. Without it, Route 3 cannot prove that the exact bad events fail to cover \([T,2T]\). Supplying such a theorem appears comparable to a multidimensional shifted-friable/Buchstab problem with additional \(p\)-adic constraints.

A fresh attempt should either:

1. prove those averaged lower correlations using dispersion or spectral methods beyond ordinary sieve theory;
2. construct a genuinely new random model mapping independent local variables to an integer \(X=O(T)\) while preserving prime-power residues;
3. or abandon pure Route 3 and combine the exact Markov ledger with a deterministic endpoint-factorization construction that removes the top-prime events before probabilistic treatment.