STATUS: BLOCKED

## Result

The open infinitude assertion is not resolved. Route 4 does yield two rigorous structural results: (i) for every fixed finite set of primes, there are arbitrarily large intervals of relative length arbitrarily close to a factor of \(2\) on which every one of those primes is harmless; and (ii) primes larger than about \(n/\log n\) cannot witness \(g_n>1\). These combine to isolate a precise missing “moving-cutoff survivor lemma”: one would need to find, for arbitrarily large \(z\), an integer \(n\ll z\log z\) avoiding all bad sets \(\mathcal B_p\) for \(p\le z\). The fixed-prime construction cannot do this, because its universal invariant—forcing every leading digit to be \(1\)—is incompatible with the required scale \(n\asymp z\log z\). A natural union-bound or local-lemma argument is exactly critical at the top prime scale \(p\asymp n/\log n\), with no quantitative slack.

## Complete Argument

Throughout, all logarithms are natural. I use the exact criterion from the brief:

\[
p\mid g_n\quad\Longleftrightarrow\quad d_p(n)\in S_p.
\]

### 1. Two elementary geometric facts about the bad digit sets

#### Lemma 1.1: Harmonic zeros are never consecutive

For every prime \(p\), no two consecutive integers belong to \(S_p\).

**Proof.** If \(1\le d\le p-2\), then modulo \(p\),

\[
H_{d+1}-H_d=\frac1{d+1}\not\equiv0.
\]

Thus \(H_d\) and \(H_{d+1}\) cannot both vanish modulo \(p\). ∎

For odd \(p\), since \(1\notin S_p\), \(p-1\in S_p\), and there are \(p-1\) possible digits, this implies

\[
|S_p|\le \frac{p-1}{2}.
\]

Consequently, within a full \(p\)-adic decade

\[
[p^e,p^{e+1}),
\]

the bad intervals belonging to \(p\) occupy at most half the ordinary Lebesgue measure. This porosity is not enough by itself: intersections of many half-density sets can be empty.

---

### 2. A strong finite-prime survivor theorem

The following is the main positive result obtained from Route 4.

#### Theorem 2.1: Thick intervals avoiding any fixed finite set of primes

Let \(P\) be a finite set of primes, and let \(0<c<\log 2\). There exist arbitrarily large real numbers \(T\) such that every integer \(n\) satisfying

\[
e^T\le n\le e^{T+c}
\]

has

\[
d_p(n)=1
\qquad\text{for every }p\in P.
\]

In particular, every such \(n\) avoids \(\mathcal B_p\) for all \(p\in P\). Thus there are arbitrarily large integer intervals, of relative length approaching \(e^c-1\), consisting entirely of survivors for the finite collection \(P\).

**Proof.**

First suppose \(|P|\ge2\), and fix \(p_0\in P\). Put

\[
M:=\max_{p\in P}\log p.
\]

For \(p\in P\setminus\{p_0\}\), define

\[
\alpha_p:=\frac{\log p_0}{\log p}.
\]

By simultaneous Dirichlet approximation, for every \(Q\ge1\) there are an integer

\[
1\le k\le Q^{|P|-1}
\]

and integers \(m_p\), \(p\ne p_0\), such that

\[
\left|k\frac{\log p_0}{\log p}-m_p\right|\le \frac1Q.
\]

Set \(m_{p_0}=k\). Multiplying by \(\log p\) gives

\[
\left|k\log p_0-m_p\log p\right|\le \frac{M}{Q}
\qquad(p\in P),
\]

where the left side is zero for \(p=p_0\).

Define

\[
T:=k\log p_0+\frac{2M}{Q}.
\]

Then for every \(p\in P\),

\[
\frac{M}{Q}
\le T-m_p\log p
\le \frac{3M}{Q}.
\]

Choose \(Q\) sufficiently large that

\[
\frac{3M}{Q}+c<\log2.
\]

For every \(u\in[0,c]\), it follows that

\[
0<T+u-m_p\log p<\log2.
\]

Exponentiating,

\[
p^{m_p}<e^{T+u}<2p^{m_p}\le p^{m_p+1}.
\]

For sufficiently large returned values of \(k\), all \(m_p\ge1\). Therefore every integer \(n\) with \(\log n=T+u\), \(0\le u\le c\), has largest power \(p^{m_p}\le n\) and

\[
1\le \frac{n}{p^{m_p}}<2.
\]

Hence \(d_p(n)=1\).

It remains to show that such \(k\) can be chosen arbitrarily large. If all Dirichlet approximants \(k\) remained bounded along a sequence \(Q\to\infty\), some fixed positive \(k\) would occur infinitely often and satisfy

\[
k\frac{\log p_0}{\log p}\in\mathbb Z
\]

for every \(p\in P\). Thus \(\log p_0/\log p\) would be rational for every \(p\in P\). For distinct primes this is impossible: a relation

\[
\frac{\log p_0}{\log p}=\frac ab
\]

would imply \(p_0^b=p^a\), contradicting unique factorization. Therefore \(k\), and hence \(T\), is unbounded.

If \(P=\{p_0\}\), simply take \(T=k\log p_0+\varepsilon\), with \(k\to\infty\) and \(0<\varepsilon<\log2-c\). The same argument applies. ∎

#### Corollary 2.2

No finite collection of primes can cover all sufficiently large integers:

\[
\mathbb N\not\subseteq_{\mathrm{eventually}}\bigcup_{p\in P}\mathcal B_p
\]

for every finite \(P\).

This conclusion does not require any rational independence among three or more reciprocal logarithms. Simultaneous recurrence to the origin is enough.

---

### 3. Why the fixed-prime theorem cannot be iterated directly

Theorem 2.1 forces the universal safe digit \(1\). That invariant is impossible at the moving cutoff needed for the original problem.

#### Lemma 3.1: The all-digit-\(1\) invariant forces a large scale gap

Suppose \(n>16\) and \(z\ge2\sqrt n\). Then there is a prime \(p\le z\) such that

\[
d_p(n)\ge2.
\]

**Proof.** Let \(m=\lfloor\sqrt n\rfloor\). By Bertrand’s postulate, there is a prime \(p\) with

\[
m<p<2m.
\]

Then \(p>\sqrt n\), so \(p^2>n\) and \(e_p(n)=1\). Also \(p<2\sqrt n\le z\). Since \(n>16\),

\[
p<2\sqrt n\le \frac n2,
\]

and therefore

\[
d_p(n)=\left\lfloor\frac np\right\rfloor\ge2.
\]

∎

Thus if \(d_p(n)=1\) for every prime \(p\le z\), necessarily

\[
n>\frac{z^2}{4}
\]

for all sufficiently large \(n\). The useful moving-cutoff scale below will be \(n\asymp z\log z\), which is much smaller than \(z^2/4\). Consequently, the thick finite-prime intervals from Theorem 2.1 cannot themselves supply the desired examples once \(P\) grows with \(n\).

This is a structural obstruction, not merely a poor quantitative bound in Dirichlet approximation.

---

### 4. Large-prime witnesses are automatically absent

Let \(H_d=U_d/V_d\) be reduced.

#### Lemma 4.1: Growth of harmonic numerators

As \(d\to\infty\),

\[
\log U_d\le (1+o(1))d.
\]

In particular, for every \(\varepsilon>0\), there is \(D_\varepsilon\) such that

\[
U_d\le e^{(1+\varepsilon)d}
\qquad(d\ge D_\varepsilon).
\]

**Proof.** Since \(V_d\mid L_d\),

\[
L_dH_d=\frac{L_d}{V_d}U_d
\]

is a positive integer, and hence

\[
U_d\le L_dH_d.
\]

Now

\[
\log L_d=\psi(d),
\]

where \(\psi\) is the second Chebyshev function. The prime number theorem gives

\[
\psi(d)=d+o(d).
\]

Also \(H_d\le1+\log d\), so

\[
\log H_d=O(\log\log(d+2))=o(d).
\]

Therefore

\[
\log U_d\le\log L_d+\log H_d=d+o(d).
\]

∎

Only the weaker elementary estimate \(\log U_d=O(d)\) is needed for a constant-factor cutoff; it follows from Chebyshev’s elementary bound \(\psi(d)=O(d)\).

#### Theorem 4.2: Sharp moving-cutoff reduction

Fix \(\delta\in(0,1)\). For all sufficiently large \(z\), the following holds.

If

\[
z\le n\le (1-\delta)z\log z
\]

and

\[
d_p(n)\notin S_p
\qquad\text{for every prime }p\le z,
\]

then \(g_n=1\).

**Proof.** Choose \(\varepsilon>0\) such that

\[
(1+\varepsilon)(1-\delta)<1.
\]

By Lemma 4.1, choose \(D\) such that

\[
\log U_d\le(1+\varepsilon)d
\qquad(d\ge D).
\]

Increase \(z\) so that

\[
z>\max_{1\le d<D}U_d
\]

and

\[
(1-\delta)z\log z<z^2.
\]

Suppose, for a contradiction, that some prime \(p>z\) witnesses \(p\mid g_n\). Since \(n<z^2<p^2\), one has \(e_p(n)=1\). Put

\[
d=d_p(n)=\left\lfloor\frac np\right\rfloor.
\]

The local criterion gives \(p\mid U_d\). Also

\[
d<\frac nz\le(1-\delta)\log z.
\]

If \(d<D\), then

\[
p\le U_d<z,
\]

contrary to \(p>z\). If \(d\ge D\), then

\[
\log p\le\log U_d
\le(1+\varepsilon)d
<(1+\varepsilon)(1-\delta)\log z
<\log z,
\]

again contradicting \(p>z\).

Thus no prime \(p>z\) witnesses non-coprimality. By hypothesis no prime \(p\le z\) does either. Hence \(g_n=1\). ∎

A useful reformulation is that any large witness with \(p^2>n\) must satisfy

\[
p\log p\le(1+o(1))n.
\]

In particular, all witnesses satisfy

\[
p\le(1+o(1))\frac n{\log n}
\]

apart from the smaller primes \(p\le\sqrt n\), which already obey this bound for large \(n\).

#### Precise missing lemma

Theorem 4.2 shows that an affirmative solution would follow from:

> For some fixed \(\delta>0\) and arbitrarily large \(z\), there exists an integer
> \[
> z\le n\le(1-\delta)z\log z
> \]
> such that \(n\notin\mathcal B_p\) for every prime \(p\le z\).

This is the required robust moving-cutoff survivor lemma. I do not have a proof of it.

---

### 5. Why a direct union bound is exactly critical

The obstruction already appears in the top prime shell.

Let \(C_0\) be an absolute constant such that

\[
\log U_d\le C_0d
\qquad(d\ge1),
\]

which follows from the elementary Chebyshev bound discussed above.

Consider \(n\in[X,2X]\) and primes

\[
P<p\le2P,
\qquad P>\sqrt{2X}.
\]

For such primes, \(e_p(n)=1\), and a bad interval has the form

\[
[dp,(d+1)p)
\]

with \(p\mid U_d\) and

\[
d\le \frac{2X}{P}.
\]

For fixed \(d\), the number of primes \(p\ge P\) dividing \(U_d\) is at most

\[
\frac{\log U_d}{\log P}\le\frac{C_0d}{\log P},
\]

because the product of \(k\) distinct such primes is at least \(P^k\) and divides \(U_d\).

Hence the sum of the lengths of all relevant bad intervals, counted with multiplicity, is at most

\[
2P\sum_{d\le 2X/P}\frac{C_0d}{\log P}
\ll
\frac{C_0X^2}{P\log P}.
\]

At the critical scale

\[
P\asymp\frac X{\log X},
\]

this bound is merely

\[
O(X),
\]

the full length of the ambient interval. Thus even the essentially optimal numerator-size estimate has no union-bound slack at precisely the largest possible witness scale.

This calculation does not prove that those intervals cover \([X,2X]\). It proves that numerator size and interval length alone cannot rule out coverage.

---

### 6. Why a standard Lovász local lemma does not currently apply

On a uniformly random integer \(n\) in a target interval, each event

\[
E_p=\{d_p(n)\in S_p\}
\]

is a function of the same scalar \(n\). There is no established sparse dependency graph: when \(n\) is represented by random binary digits, the event \(E_p\) is controlled primarily by an initial block of the most significant digits, and these blocks are nested rather than disjoint. A complete dependency graph is always valid, but then the local-lemma criterion is far too weak because some small-prime events have fixed positive probability and the degree grows like \(\pi(z)\).

A lopsided or resampling local lemma would require a new correlation theorem showing that conditioning on avoidance for many other primes does not substantially increase \(\Pr(E_p)\). Establishing such a theorem appears comparable to the missing logarithmic sieve.

---

### 7. The non-coprime set is infinite

For completeness, take

\[
n=2\cdot3^e,\qquad e\ge1.
\]

The largest power of \(3\) not exceeding \(n\) is \(3^e\), so

\[
d_3(n)=2.
\]

Since

\[
H_2=\frac32\equiv0\pmod3,
\]

one has \(2\in S_3\), and the local criterion gives

\[
3\mid g_n.
\]

Thus \(\{n:g_n>1\}\) is infinite.

## Self-Audit

1. **The central moving-cutoff survivor lemma is unproved.**  
   This is the decisive gap, and I do not claim otherwise. Theorem 4.2 proves rigorously that this lemma would suffice, but proving it still requires simultaneous avoidance for a growing number of primes. The \(x/\log x\) heuristic supports it, but that is not evidence of a proof.

2. **The large-prime cutoff invokes the prime number theorem.**  
   The only use is the standard unconditional theorem \(\psi(d)=d+o(d)\). The deduction \(\log U_d\le\psi(d)+\log H_d\) is exact. If one wishes to avoid PNT, Chebyshev’s elementary estimate gives a weaker but still rigorous window \(n\le c z\log z\) for some absolute \(c>0\).

3. **The “critical union bound” is only a route diagnosis.**  
   It does not prove that a more sophisticated deterministic construction or correlation argument is impossible. It only shows that the obvious product-size estimate gives an \(O(X)\) loss, rather than \(o(X)\), at \(p\asymp X/\log X\). A successful argument would need to exploit overlap, cancellation, or additional arithmetic structure of the prime divisors of \(U_d\).

## Computations To Verify

```python
from math import isqrt, log, exp, floor
from fractions import Fraction

def primes_upto(N):
    sieve = bytearray(b"\x01") * (N + 1)
    if N >= 0:
        sieve[0] = 0
    if N >= 1:
        sieve[1] = 0
    for q in range(2, isqrt(N) + 1):
        if sieve[q]:
            sieve[q*q:N+1:q] = b"\x00" * (((N - q*q) // q) + 1)
    return [q for q in range(2, N + 1) if sieve[q]]

def S_p(p):
    """Modular harmonic zero set."""
    h = 0
    out = []
    for d in range(1, p):
        h = (h + pow(d, -1, p)) % p
        if h == 0:
            out.append(d)
    return out

def check_local_geometry(Pmax):
    for p in primes_upto(Pmax):
        S = S_p(p)
        assert all(d + 1 not in set(S) for d in S)
        if p == 2:
            assert S == []
        else:
            assert p - 1 in S
            assert len(S) <= (p - 1) // 2
            for d in S:
                if d <= p - 2:
                    assert p - 1 - d in S

def harmonic_num(d):
    h = sum((Fraction(1, k) for k in range(1, d + 1)), Fraction(0, 1))
    return h.numerator

def test_numerator_growth(D):
    """
    Record log(U_d)/d. PNT predicts limsup <= 1.
    This is only an empirical check.
    """
    vals = []
    for d in range(1, D + 1):
        U = harmonic_num(d)
        vals.append((d, log(U) / d if U > 1 else 0.0, U))
    return vals

def mark_window(z, delta=0.25):
    """
    Sieve only with p <= z in the moving-cutoff window
        z <= n <= (1-delta) z log z.
    For sufficiently large z, Theorem 4.2 says every survivor is
    a genuine g_n = 1 example.
    """
    lo = z
    hi = int((1.0 - delta) * z * log(z))
    if hi < lo:
        return []

    bad = bytearray(hi - lo + 1)

    for p in primes_upto(z):
        S = S_p(p)
        q = p
        while q <= hi:
            for d in S:
                left = max(lo, d * q)
                right = min(hi, (d + 1) * q - 1)
                if left <= right:
                    a = left - lo
                    b = right - lo
                    bad[a:b+1] = b"\x01" * (b - a + 1)
            if q > hi // p:
                break
            q *= p

    return [lo + i for i, flag in enumerate(bad) if not flag]

def local_witnesses(n):
    """Direct local-criterion check, without constructing L_n."""
    witnesses = []
    for p in primes_upto(n):
        q = p
        while q <= n // p:
            q *= p
        d = n // q
        h = 0
        for j in range(1, d + 1):
            h = (h + pow(j, -1, p)) % p
        if h == 0:
            witnesses.append(p)
    return witnesses

def cross_check_survivors(z, delta=0.25, limit=None):
    survivors = mark_window(z, delta)
    if limit is not None:
        survivors = survivors[:limit]
    for n in survivors:
        assert local_witnesses(n) == []
    return survivors

def survivor_components(z, delta=0.25, block_edges=None):
    """
    Track component collapse after blocks of primes.
    Returns, after each block, the number and maximum length of
    connected survivor components.
    """
    lo = z
    hi = int((1.0 - delta) * z * log(z))
    alive = bytearray(b"\x01") * max(0, hi - lo + 1)
    ps = primes_upto(z)

    if block_edges is None:
        block_edges = [3, 10, 30, 100, 300, 1000, z]
    block_edges = sorted(set(min(z, b) for b in block_edges if b >= 2))

    stats = []
    used = set()

    for edge in block_edges:
        for p in ps:
            if p > edge or p in used:
                continue
            used.add(p)
            S = S_p(p)
            q = p
            while q <= hi:
                for d in S:
                    left = max(lo, d*q)
                    right = min(hi, (d+1)*q - 1)
                    if left <= right:
                        alive[left-lo:right-lo+1] = b"\x00" * (right-left+1)
                if q > hi // p:
                    break
                q *= p

        lengths = []
        i = 0
        while i < len(alive):
            if not alive[i]:
                i += 1
                continue
            j = i
            while j < len(alive) and alive[j]:
                j += 1
            lengths.append(j - i)
            i = j
        stats.append({
            "prime_cutoff": edge,
            "survivors": sum(lengths),
            "components": len(lengths),
            "max_component": max(lengths, default=0),
        })

    return stats
```

A numerical search for the finite-prime recurrence can be made with high-precision arithmetic:

```python
import mpmath as mp

def common_digit_one_return(P, c=0.5, K=10**7, dps=80):
    """
    Search for k such that an interval [T,T+c] forces digit 1
    for all p in P. Uses the proof of Theorem 2.1.
    """
    mp.mp.dps = dps
    P = list(P)
    p0 = P[0]
    lp0 = mp.log(p0)

    if len(P) == 1:
        k = K
        T = k * lp0 + (mp.log(2) - c) / 2
        return T

    best_E = mp.inf
    best_k = None

    for k in range(1, K + 1):
        errors = []
        for p in P[1:]:
            lp = mp.log(p)
            m = mp.nint(k * lp0 / lp)
            errors.append(abs(k * lp0 - m * lp))
        E = max(errors)
        if E < best_E:
            best_E = E
            best_k = k
            if 3 * E + c < mp.log(2):
                T = k * lp0 + 2 * E

                # Independent verification of the logarithmic remainders.
                for p in P:
                    lp = mp.log(p)
                    r = mp.fmod(T, lp)
                    if r < 0:
                        r += lp
                    assert r >= 0
                    assert r + c < mp.log(2)
                return T

    return None
```

The most informative computational experiment is to run `mark_window(z, delta)` for increasing \(z\), recording:

- whether the moving-cutoff window has any survivors;
- the number of survivors divided by \(z\);
- component lengths after successive prime blocks;
- which prime shell removes each candidate;
- whether the top shell \(p\asymp z\) removes a positive proportion or merely creates extensive overlap.

## Route Diagnosis

**Proved ledger**

1. \(S_p\) contains no consecutive digits, hence \(|S_p|\le(p-1)/2\).
2. Every fixed finite collection of primes has arbitrarily large survivor intervals of multiplicative width arbitrarily close to \(2\).
3. No finite collection of bad sets \(\mathcal B_p\) eventually covers the integers.
4. Harmonic numerators satisfy \(\log U_d\le(1+o(1))d\).
5. Primes larger than \((1+o(1))n/\log n\) cannot witness \(g_n>1\).
6. The moving-cutoff survivor assertion in Theorem 4.2 would solve the open half.
7. The non-coprime set is infinite via \(n=2\cdot3^e\).

**Plausible but unproved**

- For some fixed \(\delta>0\), every sufficiently large window
  \[
  [z,(1-\delta)z\log z]
  \]
  contains an integer avoiding all \(\mathcal B_p\) with \(p\le z\).
- A multiscale survivor set should have about sieve-dimension-one size, but no rigorous branching or correlation estimate establishes this.

**Dead ends**

1. **Force digit \(1\) for successive prime blocks.**  
   This works exceptionally well for any fixed block, but any number with digit \(1\) for all primes \(p\le z\) must satisfy \(n>z^2/4\). The large-prime tail requires \(n\ll z\log z\). The invariants are incompatible.

2. **Naive union bound.**  
   At \(p\asymp n/\log n\), the strongest available numerator-size estimate gives total bad-interval length \(O(n)\), not \(o(n)\). There is no guaranteed leftover.

3. **Standard Lovász local lemma.**  
   The events depend on nested initial information about one scalar integer, so no sparse exact dependency graph is available. Establishing a useful lopsided dependency estimate would itself amount to a new cross-prime correlation theorem.

**Final diagnosis**

Route 4 is blocked at a sharply identified point: fixed-prime recurrence is easy and even produces thick intervals, but controlling a prime set growing to \(n/\log n\) requires a genuinely new survivor theorem. A fresh attempt should combine the moving-cutoff reduction with arithmetic information about large prime divisors of \(U_d\) for \(d\asymp\log n\). In particular, the critical top shell translates the problem into understanding the placement of intervals associated with primes \(p\mid U_d\), where \(p\asymp e^d\). Any theorem showing substantial overlap among those intervals, or ruling out near-tilings by the largest prime divisors of consecutive harmonic numerators, would provide exactly the slack the deterministic construction currently lacks.