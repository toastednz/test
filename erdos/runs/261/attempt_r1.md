STATUS: BLOCKED

## Result

I did not prove Q2. I obtained an exact compression of Route 1: after adjoining the complementary residual, every nonterminal admissible path is forced except at perfectly central states. Up to orientation, all admissible paths follow one deterministic nonautonomous folded-doubling orbit
\[
x_{s+1}=\min(2x_s,s+1-2x_s).
\]
A finite representation occurs exactly at a favorably oriented adjacent-central state. Consequently, finite-horizon reachability from a fixed \(n\) has at most two distinct nonterminal residual states at every level, rather than \(O(j)\). I also derive an exact binary-word criterion
\[
(n+L)(q+1)+2=2^{L+1}+B(q)
\]
for finite representations. The remaining universal favorable-central-hitting statement appears to retain the full difficulty of Q2; I found neither a descent invariant nor a counterexample.

## Complete Argument

### 1. Residual and complementary residual

It suffices to treat \(n\ge2\), since \(w(1)=w(2)\). For a choice sequence \(\varepsilon_k\in\{0,1\}\), define at level \(j\ge n\)
\[
r_j
=
2^j\left(
\frac n{2^n}
-\sum_{n<k\le j}\varepsilon_k\frac{k}{2^k}
\right).
\]
Then
\[
r_n=n,\qquad r_{j+1}=2r_j-(j+1)\varepsilon_{j+1}.
\]

The total unused tail beyond \(j\), scaled by \(2^j\), is
\[
2^j\sum_{k>j}\frac{k}{2^k}=j+2.
\]
Define the complementary residual
\[
c_j:=j+2-r_j.
\]

Thus an admissible state satisfies
\[
r_j\ge0,\qquad c_j\ge0,\qquad r_j+c_j=j+2.
\]
At the initial level,
\[
(r_n,c_n)=(n,2).
\]

Every finite representation gives admissible states at all intermediate levels: after any prefix, its residual is exactly the sum of the still-unselected terms of that finite representation, and hence lies between zero and the full remaining tail.

Conversely, if an admissible path reaches \(r_M=0\), then
\[
\frac n{2^n}=\sum_{n<k\le M}\varepsilon_k\frac{k}{2^k},
\]
so it gives the desired finite representation. Therefore Q2 is exactly a reachability problem inside the admissible strip.

### 2. The two-coordinate transition

Put
\[
s:=j+2,
\]
so \(r_j+c_j=s\), and the next index is \(j+1=s-1\). Direct calculation gives:

- If \(\varepsilon_{j+1}=0\), then
  \[
  (r_{j+1},c_{j+1})
  =
  (2r_j,s+1-2r_j).
  \]
  Thus the residual coordinate \(r_j\) is doubled.

- If \(\varepsilon_{j+1}=1\), then
  \[
  (r_{j+1},c_{j+1})
  =
  (s+1-2c_j,2c_j).
  \]
  Thus the complementary coordinate \(c_j\) is doubled.

In either case the new coordinates sum to \(s+1\).

Let
\[
u=\min(r_j,c_j),\qquad v=\max(r_j,c_j),
\]
so \(u+v=s\).

The operation doubling \(u\) is always admissible, because
\[
2u\le s<s+1.
\]
The operation doubling \(v\) is admissible exactly when
\[
2v\le s+1.
\]
Since \(v=s-u\), this is equivalent to
\[
2u\ge s-1.
\]

There are therefore only two exceptional configurations.

#### Even central state

If \(s=2k\), then \(u\le k\), while \(2u\ge2k-1\) forces \(u=k\). Hence both choices are admissible only when
\[
(r_j,c_j)=(k,k).
\]
The two outputs are
\[
(2k,1)\quad\text{and}\quad(1,2k).
\]

#### Odd adjacent-central state

If \(s=2k+1\), then \(u\le k\), while \(2u\ge2k\) forces \(u=k\). Hence both choices are admissible only when
\[
\{r_j,c_j\}=\{k,k+1\}.
\]

Doubling the smaller component gives
\[
\{r_{j+1},c_{j+1}\}=\{2,s-1\}.
\]
Doubling the larger component gives
\[
\{r_{j+1},c_{j+1}\}=\{0,s+1\}.
\]

We have proved:

> **Forced-choice lemma.** Away from equal or adjacent-central states, every admissible path is forced to double the smaller of \(r_j,c_j\). At an equal-central state there are two complementary nonterminal outputs. At an adjacent-central state, doubling the larger coordinate reaches an endpoint, while doubling the smaller coordinate is the unique nonterminal continuation.

### 3. Deterministic unsigned folding

For a nonendpoint state of total \(s\), define
\[
x_s:=\min(r_j,c_j),\qquad s=j+2.
\]
Then
\[
0<x_s\le \left\lfloor\frac s2\right\rfloor.
\]

Every nonterminal continuation has
\[
\boxed{
x_{s+1}=F_s(x_s):=\min(2x_s,s+1-2x_s).
}
\]
Indeed, away from the central states only the smaller component can be doubled. At an even-central state either choice gives the unordered pair \(\{1,s\}\), and at an odd adjacent-central state the unique nonterminal choice gives \(\{2,s-1\}\). Thus the same formula holds in every nonterminal case.

For Q2 the initial unsigned state is
\[
s_0=n+2,\qquad x_{s_0}=\min(n,2)=2
\]
for \(n\ge2\).

Hence all nonterminal admissible paths from a fixed \(n\), regardless of their earlier choices, have the same unsigned orbit
\[
x_{n+2}=2,\qquad
x_{s+1}=\min(2x_s,s+1-2x_s).
\]

The only remaining information is which of the two coordinates is the residual \(r\).

### 4. Exact terminal criterion

Suppose a positive path first reaches \(r_{j+1}=0\). The transition cannot have \(\varepsilon_{j+1}=0\), since then \(r_{j+1}=2r_j\) would imply \(r_j=0\) already. Thus \(\varepsilon_{j+1}=1\), and
\[
2r_j-(j+1)=0.
\]
Consequently \(j+1\) is even and
\[
r_j=\frac{j+1}{2}.
\]

In terms of \(s=j+2\), this says that \(s\) is odd and
\[
r_j=\frac{s-1}{2},\qquad c_j=\frac{s+1}{2}.
\]
Thus the residual must be the smaller coordinate and the complement must be the larger coordinate at an odd adjacent-central state.

Conversely, from precisely such a state, selecting the next index gives \(r_{j+1}=0\).

Therefore:

> **Favorable-central criterion.** For \(n\ge2\), a finite representation exists if and only if the oriented process starting from
> \[
> (s,r,c)=(n+2,n,2)
> \]
> can reach an odd total \(s\) satisfying
> \[
> (r,c)=\left(\frac{s-1}{2},\frac{s+1}{2}\right).
> \]
> The next selected index \(s-1\) then terminates the representation.

This also reproves the parity condition: the largest selected exponent is \(s-1\), which is even.

The opposite orientation,
\[
(r,c)=\left(\frac{s+1}{2},\frac{s-1}{2}\right),
\]
allows an endpoint exit with \(c'=0\). That path then remains at the full-tail endpoint and corresponds to a cofinite, rather than finite, representation.

At an even-central state \(r=c=s/2\), the two choices give the complementary states
\[
(r',c')=(1,s)\quad\text{or}\quad(s,1).
\]
Consequently an even-central visit gives complete control over the orientation of the ensuing unsigned orbit. More precisely, the two continuations are complements of one another; at any later odd adjacent-central state, exactly one orientation is favorable for finite termination.

### 5. Width-two reachability

The forced-choice lemma gives a substantial state-space reduction.

> **Width-two corollary.** At any level \(j\), after merging prefixes with the same residual and discarding the full-tail endpoint \(r_j=j+2\), there are at most two nonterminal residual states reachable from \((n,n)\) while remaining admissible.

Proof: all nonterminal states have the same value
\[
x_{j+2}=\min(r_j,j+2-r_j).
\]
Thus the residual can only be
\[
r_j=x_{j+2}
\quad\text{or}\quad
r_j=j+2-x_{j+2}.
\]
There are at most two such values. ∎

Discarding the full-tail endpoint is safe: if \(r_j=j+2\), then \(c_j=0\); the only admissible next move doubles \(c_j\), leaving \(c_{j+1}=0\). Such a path can never reach \(r=0\).

Thus finite-horizon Route 1 search can be performed in linear time in the horizon, with at most two active nonterminal states per level.

### 6. Recovery of the Borwein–Loring family

Let
\[
n=2^{m+1}-m-2.
\]
Starting from \((r,c)=(n,2)\), select the next \(m-1\) indices. After \(t\) such selections,
\[
c_{n+t}=2^{t+1},
\qquad
r_{n+t}=n+t+2-2^{t+1}.
\]
For \(t=m-1\),
\[
r_{n+m-1}=2^m-1,\qquad c_{n+m-1}=2^m.
\]
This is a favorable odd adjacent-central state. Selecting the next index \(n+m\) gives residual zero. Hence
\[
\frac n{2^n}=\sum_{k=n+1}^{n+m}\frac{k}{2^k}.
\]

Thus the known family is exactly the case where the initial complementary coordinate reaches a favorable central state before any nontrivial fold.

For example, the folded dynamics for \(n=2\) gives the representation
\[
\frac12=\frac3{2^3}+\frac6{2^6}+\frac8{2^8}.
\]

### 7. Exact binary-word criterion

Let \(L\ge1\), and let \(\varepsilon_t\in\{0,1\}\) indicate whether \(n+t\) is selected for \(1\le t\le L\). Iterating the residual recurrence gives
\[
r_{n+L}
=
2^L n-\sum_{t=1}^{L}(n+t)\varepsilon_t2^{L-t}.
\]
Define
\[
E:=\sum_{t=1}^{L}\varepsilon_t2^{L-t},
\qquad
C:=\sum_{t=1}^{L}t\varepsilon_t2^{L-t}.
\]
Then
\[
r_{n+L}=n(2^L-E)-C.
\]
Therefore the word terminates exactly when
\[
\boxed{n(2^L-E)=C.}
\]

There is a useful complementary reformulation. Put
\[
\delta_t:=1-\varepsilon_t,\qquad
q:=\sum_{t=1}^{L}\delta_t2^{L-t}.
\]
Since
\[
E=(2^L-1)-q,
\]
we have
\[
2^L-E=q+1.
\]

Write the binary expansion
\[
q=\sum_{p\ge0}b_p2^p
\]
and define
\[
B(q):=\sum_{p\ge0}p\,b_p2^p.
\]
Also,
\[
\sum_{t=1}^{L}t2^{L-t}=2^{L+1}-L-2.
\]
Because \(p=L-t\),
\[
\sum_{t=1}^{L}t\delta_t2^{L-t}
=
Lq-B(q).
\]
Thus
\[
C=2^{L+1}-L-2-Lq+B(q).
\]
Substitution into \(n(q+1)=C\) yields
\[
\boxed{
(n+L)(q+1)+2=2^{L+1}+B(q).
}
\]

If \(L\) is chosen minimally, so that \(n+L\) is the largest selected index, then \(\varepsilon_L=1\), equivalently the least significant bit of \(q\) is zero. Hence \(q\) is even.

We obtain the exact arithmetic characterization:

> **Binary criterion.** For \(n\ge2\), \(\mathcal F(n)\) holds if and only if there are \(L\ge1\) and an even integer \(q\), \(0\le q<2^L\), such that
> \[
> (n+L)(q+1)+2=2^{L+1}+B(q).
> \]

Given such \(L,q\), use the \(L\)-bit expansion of \(q\) for the omission digits \(\delta_t\), and select precisely those \(n+t\) for which \(\delta_t=0\).

There cannot be only one selected index: for \(a>n\ge2\), strict decrease of \(r/2^r\) gives \(w(a)<w(n)\). Thus the resulting representation automatically has at least two terms.

For the Borwein–Loring family, \(q=0\), and the criterion becomes
\[
n+L+2=2^{L+1}.
\]

### 8. The unresolved core

The reduction leaves the following deterministic-orientation problem.

Starting with
\[
s=n+2,\qquad (r,c)=(n,2),\qquad x=2,
\]
iterate
\[
x_{s+1}=\min(2x_s,s+1-2x_s).
\]
Away from even-central states the orientation is forced; at an even-central state it may be chosen freely. One must prove that eventually an odd adjacent-central state occurs with the residual as the smaller coordinate.

This remains unproved. It is not susceptible to the most obvious descent arguments. For example,
\[
(s,x)=(12,2)\longmapsto(13,4)\longmapsto(14,6)\longmapsto(15,3),
\]
so neither \(x_s\) nor \(x_s/s\) is monotone, and even a folding step can increase \(x\).

A stronger claim that every admissible state finitely terminates is false: the endpoint \(r_j=j+2\) has the unique continuation selecting every later index and never reaches zero.

The arithmetic reformulation also did not yield a monotonic search in \(q\). If \(q\) has \(a\) trailing binary ones, then
\[
B(q+1)-B(q)=2^{a+1}-2.
\]
Consequently
\[
(n+L)(q+1)+2-B(q)
\]
can jump either upward or downward as \(q\) increases, defeating a direct intermediate-value argument.

## Self-Audit

1. **The universal favorable-central theorem is missing.** This is the decisive weakness and the reason for `BLOCKED`. The known verification through \(10000\) supports it for the required initial states, but I have no invariant excluding a nonterminating or perpetually unfavorably oriented orbit.

2. **The folding compression depends on pruning by the full remaining-tail capacity.** This pruning is exact, not heuristic: any finite completion has residual equal to a subset of the remaining tail, so \(0\le r_j\le j+2\). The two-coordinate formulas then exhaust both digit choices algebraically.

3. **The binary criterion is indexing-sensitive.** I believe it is correct because it was derived independently from the closed residual formula, with \(q\) explicitly encoding omitted indices. It also specializes correctly to \(q=0\) for the Borwein–Loring family and to the known \(n=2\) representation.

## Computations To Verify

```python
def verify(n, A):
    """Exact checker for a proposed representation."""
    A = sorted(A)
    assert n >= 1
    assert len(A) >= 2
    assert len(A) == len(set(A))
    assert all(a >= 1 for a in A)

    M = max([n] + A)
    lhs = n * (1 << (M - n))
    rhs = sum(a * (1 << (M - a)) for a in A)
    return lhs == rhs


def finite_representation(n0, max_index):
    """
    Exact width-two dynamic search.
    Returns a representation with maximum <= max_index, or None.

    A failure is not a proof of nonexistence beyond max_index.
    """
    n = 2 if n0 == 1 else n0
    if max_index <= n:
        return None

    # residual -> binary word epsilon_{n+1},...,epsilon_j
    states = {n: 0}

    for j in range(n + 1, max_index + 1):
        nxt = {}
        L = j - n

        for r, word in states.items():
            for eps in (0, 1):
                rp = 2 * r - j * eps
                new_word = (word << 1) | eps

                if not (0 <= rp <= j + 2):
                    continue

                if rp == 0:
                    A = [
                        n + t
                        for t in range(1, L + 1)
                        if (new_word >> (L - t)) & 1
                    ]
                    assert verify(n0, A)
                    return A

                # Full-tail endpoint: it can never later reach residual zero.
                if rp == j + 2:
                    continue

                # Prefixes with the same residual have identical futures.
                nxt.setdefault(rp, new_word)

        states = nxt

        # Verify the width-two theorem during the computation.
        if states:
            s = j + 2
            unsigned = {min(r, s - r) for r in states}
            assert len(unsigned) == 1
            assert len(states) <= 2

    return None


def folded_events(n, steps):
    """
    The deterministic unsigned orbit. Records central events.
    """
    n = 2 if n == 1 else n
    s = n + 2
    x = min(n, 2)
    events = []

    for _ in range(steps):
        if s % 2 == 0 and x == s // 2:
            events.append((s, x, "equal-central"))
        if s % 2 == 1 and x == (s - 1) // 2:
            events.append((s, x, "adjacent-central"))

        x = min(2 * x, s + 1 - 2 * x)
        s += 1

    return events


def B(q):
    """B(q) = sum p*b_p*2^p over the binary digits b_p of q."""
    ans = 0
    p = 0
    z = q
    while z:
        if z & 1:
            ans += p * (1 << p)
        z >>= 1
        p += 1
    return ans


def criterion_to_representation(n0, L, q):
    """
    Reconstruct a representation from the binary criterion, if valid.
    """
    n = 2 if n0 == 1 else n0

    if L < 1 or not (0 <= q < (1 << L)) or q % 2:
        return None

    if (n + L) * (q + 1) + 2 != (1 << (L + 1)) + B(q):
        return None

    A = []
    for t in range(1, L + 1):
        delta_t = (q >> (L - t)) & 1
        if delta_t == 0:
            A.append(n + t)

    assert A[-1] == n + L
    assert verify(n0, A)
    return A


def q_from_representation(n0, A):
    """
    Verify the binary criterion for an already known localized representation.
    """
    n = 2 if n0 == 1 else n0
    A = set(A)
    L = max(A) - n
    assert L >= 1
    assert all(n < a <= n + L for a in A)

    q = 0
    for t in range(1, L + 1):
        if n + t not in A:
            q |= 1 << (L - t)

    assert q % 2 == 0
    assert (n + L) * (q + 1) + 2 == (1 << (L + 1)) + B(q)
    assert criterion_to_representation(n0, L, q) is not None
    return L, q


# Basic exact checks.
assert verify(1, [3, 6, 8])
assert verify(2, [3, 6, 8])
assert verify(3, [4, 6, 8])
assert verify(4, [5, 6])

for n in range(2, 200):
    A = finite_representation(n, n + 20000)
    if A is None:
        print("No termination within finite horizon:", n)
    else:
        L, q = q_from_representation(n, A)
        assert criterion_to_representation(n, L, q) == sorted(A)


# Exhaustively cross-check the binary criterion for small L.
for n in range(2, 30):
    for L in range(1, 13):
        for q in range(0, 1 << L, 2):
            A = criterion_to_representation(n, L, q)
            if A is not None:
                assert max(A) == n + L
                assert verify(n, A)


# Search for unusually long nonterminating prefixes.
# Increase H substantially; failure within H is never a disproof.
H = 1_000_000
for n in range(2, 1001):
    A = finite_representation(n, n + H)
    if A is None:
        print("Candidate requiring further investigation:", n)
```

A particularly useful large-scale computation would record, for each \(n\):

1. the first equal-central total;
2. the first adjacent-central total;
3. the orientation at each adjacent-central visit;
4. the first terminating total;
5. return maps from an unfavorable adjacent-central state, whose continuation restarts with unsigned coordinate \(x=2\).

Any apparent infinite corridor would then need an exact invariant, not merely a large finite survival time.

## Route Diagnosis

### Proved ledger

- The residual/complement pair always sums to the scaled remaining-tail capacity.
- Away from equal or adjacent-central states, exactly one admissible move exists: double the smaller coordinate.
- All nonterminal paths share the deterministic folded orbit
  \[
  x_{s+1}=\min(2x_s,s+1-2x_s).
  \]
- Finite termination occurs exactly at a favorably oriented odd adjacent-central state.
- At most two nonterminal residual states need be retained at any level.
- The binary-word criterion
  \[
  (n+L)(q+1)+2=2^{L+1}+B(q)
  \]
  is necessary and sufficient.
- The Borwein–Loring construction is the no-fold central-hit family \(q=0\).

### Plausible but unproved

- Every initial state \((n+2,n,2)\) eventually reaches a favorable odd adjacent-central state after suitable choices at even ties.
- A finite collection of return-map funnels from states with unsigned coordinate \(1\) or \(2\) may suffice.
- Greedy termination may hold much more broadly than currently proved, but the reduction does not establish it.

### Dead ends

- **Monotone residual descent:** false; both residuals and the unsigned coordinate can increase.
- **Monotone normalized descent:** false; \(x_s/s\) oscillates.
- **All interior states terminate by the same argument:** no proof, and the endpoint version is explicitly false.
- **Intermediate value in the binary parameter \(q\):** blocked by large nonmonotone jumps in \(B(q)\).
- **A fixed finite-state quotient:** the changing total \(s\) remains essential, and no modulus tested by the algebra removes that dependence.

A fresh Route 1 attempt should study exact return maps between successive central visits. In particular, after an unfavorable odd adjacent-central visit, the unique nonterminal continuation restarts with residual coordinate \(2\) at a later total. A theorem forcing one such return eventually to have favorable orientation, or to pass through an even-central state, would solve Q2. Conversely, a counterexample would require proving that this return process avoids favorable orientation forever.