STATUS: BLOCKED

## Result

I reduced Route 1 to a concrete sparse-reservoir covering lemma and proved that the primes can be partitioned into two reservoirs that are asymptotically equal in every prime interval and have equal reciprocal-prime mass. However, the elementary/random Erdős–Rankin sieve available for either reservoir leaves about \(m/\sqrt{\log m}\) points, whereas a terminal large-prime cleanup has only \(O(m\log\log m/\log m)\) total capacity, or \(O(m/\log m)\) singleton capacity. Closing this factor of roughly \(\sqrt{\log m}/\log\log m\) requires a genuinely new covering lemma; I could neither prove it nor find a counterexample. Thus Route 1 is blocked at exactly the density barrier identified in the brief.

## Complete Argument

### 1. A canonical scale-balanced partition of the primes

Write the primes in increasing order as
\[
p_1=2<p_2=3<p_3=5<\cdots
\]
and define
\[
A:=\{p_i:i\ \text{odd}\},\qquad
B:=\{p_i:i\ \text{even}\}.
\]

This fixed partition is balanced much more strongly than merely in total cardinality.

#### Lemma 1: Interval balance

For every real interval \(I\),
\[
\left|\#(A\cap I)-\#(B\cap I)\right|\le 1.
\]

Consequently, uniformly for sufficiently large \(y\),
\[
\#(A\cap(y,2y]),\ \#(B\cap(y,2y])
   =\frac12\bigl(\pi(2y)-\pi(y)\bigr)+O(1)
   \sim \frac{y}{2\log y}.
\]

#### Proof

The primes lying in \(I\) form a consecutive block
\[
p_r,p_{r+1},\dots,p_s.
\]
In any consecutive block of integers, the numbers of odd and even indices differ by at most one. This proves the first assertion. The second follows from the prime number theorem,
\[
\pi(2y)-\pi(y)\sim \frac{y}{\log y}.
\]
\(\square\)

Thus each reservoir has positive relative density in every sufficiently large dyadic prime scale.

#### Lemma 2: Reciprocal-mass balance

For \(C=A\) or \(B\),
\[
\sum_{\substack{p\le z\\p\in C}}\frac1p
  =\frac12\log\log z+O(1),
\]
and hence
\[
\prod_{\substack{p\le z\\p\in C}}\left(1-\frac1p\right)
  \asymp \frac1{\sqrt{\log z}}.
\]

#### Proof

Because \(1/p_i\) is decreasing,
\[
\sum_{i=r}^{s}\frac{(-1)^i}{p_i}
\]
is a finite alternating sum whose absolute value is at most \(1/p_r\). In particular, its partial sums are bounded. Therefore
\[
\sum_{\substack{p\le z\\p\in A}}\frac1p
-\sum_{\substack{p\le z\\p\in B}}\frac1p=O(1).
\]
Mertens' theorem gives
\[
\sum_{p\le z}\frac1p=\log\log z+O(1),
\]
so each color has half of this mass up to \(O(1)\).

Finally,
\[
\log\prod_{\substack{p\le z\\p\in C}}
  \left(1-\frac1p\right)
=
-\sum_{\substack{p\le z\\p\in C}}\frac1p
+O\left(\sum_p\frac1{p^2}\right)
=
-\frac12\log\log z+O(1).
\]
Exponentiating proves the product estimate. \(\square\)

---

### 2. The exact robust lemma that would complete Route 1

Consider the following assertion.

> **Robust half-density covering lemma.**  
> There are constants \(\eta>0\) and \(M_0\) such that whenever \(M\ge M_0\) and \(S\subseteq\mathcal P(M)\) satisfies
> \[
> \#(S\cap(y,2y])\ge
> \eta\bigl(\pi(2y)-\pi(y)\bigr)
> \]
> for every sufficiently large \(y\le M/2\), one can choose one residue class modulo each \(p\in S\) whose union covers \([M]\).

This would immediately solve the problem.

#### Proposition 3: The robust lemma implies Erdős Problem #467

If the robust half-density covering lemma holds for any \(\eta<1/2\), then the all-real formulation of the problem is true.

#### Proof

By Lemma 1, for all sufficiently large \(y\),
\[
\#(A\cap(y,2y]),\#(B\cap(y,2y])
\ge \frac13\bigl(\pi(2y)-\pi(y)\bigr).
\]
Apply the robust lemma separately to
\[
A_M=A\cap\mathcal P(M),\qquad B_M=B\cap\mathcal P(M).
\]
This gives independent covers of \([M]\) using the two disjoint reservoirs.

Now let \(x\) be sufficiently large and set \(M=\lfloor x\rfloor\). Every prime used is at most \(M\le x\). If \(x\notin\mathbb Z\), the positive integers below \(x\) are exactly \([M]\); if \(x=M\in\mathbb Z\), they are \([M-1]\), which is also covered. Hence the all-real statement follows. \(\square\)

The proposition is rigorous, but the robust lemma is unproved and is essentially the core open difficulty.

---

### 3. What the elementary Erdős–Rankin sieve gives in one reservoir

Fix \(C=A\) or \(B\), and independently choose a uniformly random residue \(a_p\bmod p\) for every \(p\in C\), \(p\le z\). Let
\[
U_C=\{n\in[m]: n\not\equiv a_p\pmod p
                     \text{ for every }p\in C,\ p\le z\}.
\]

#### Lemma 4: Expected residual size

One has
\[
\mathbb E|U_C|
=
m\prod_{\substack{p\le z\\p\in C}}\left(1-\frac1p\right)
\asymp \frac{m}{\sqrt{\log z}}.
\]

#### Proof

For fixed \(n\), the probability that \(a_p\not\equiv n\pmod p\) is \(1-1/p\). Independence over distinct primes gives
\[
\Pr(n\in U_C)
=
\prod_{\substack{p\le z\\p\in C}}\left(1-\frac1p\right).
\]
Sum over \(n\in[m]\) and apply Lemma 2. \(\square\)

The same numerical bound is obtainable deterministically by greedy selection.

#### Lemma 5: Elementary greedy sieve bound

There are choices of residues for \(p\in C\), \(p\le z\), leaving at most
\[
m\prod_{\substack{p\le z\\p\in C}}\left(1-\frac1p\right)
\ll \frac{m}{\sqrt{\log z}}
\]
uncovered points.

#### Proof

Suppose the current uncovered set has size \(u\). Its elements are distributed among the \(p\) residue classes modulo \(p\), so one class contains at least \(u/p\) uncovered elements. Choose that class. The new uncovered size is at most
\[
u\left(1-\frac1p\right).
\]
Iteration over the primes gives the asserted product bound. \(\square\)

This is an upper bound, not a lower bound. It therefore does not prove that better choices are impossible; it only records the limit of the straightforward averaging argument.

---

### 4. Terminal cleanup capacity

Let \(T\) be a set of primes in \((z,m]\). For arbitrary residues \(a_p\bmod p\), a class modulo \(p\) contains at most \(\lceil m/p\rceil\) elements of \([m]\).

#### Lemma 6: General terminal capacity bound

The number of points of \([m]\) covered by the classes belonging to \(T\) is at most
\[
\sum_{p\in T}\left\lceil\frac mp\right\rceil
\le
m\sum_{p\in T}\frac1p+|T|.
\]

In particular, for fixed \(K>0\) and
\[
z=\frac{m}{(\log m)^K},
\]
all primes in \((z,m]\), even without splitting them between reservoirs, have total capacity
\[
O_K\left(\frac{m\log\log m}{\log m}\right)=o(m).
\]

#### Proof

The first assertion is the union bound together with
\[
\#\{n\in[m]:n\equiv a_p\pmod p\}\le \left\lceil\frac mp\right\rceil.
\]

Put \(L=\log m\). Standard PNT estimates and partial summation give
\[
\sum_{z<p\le m}\frac1p
=
\log\log m-\log\log z+O(e^{-c\sqrt{\log z}}).
\]
Since
\[
\log z=L-K\log L,
\]
we have
\[
\log\log m-\log\log z
=
-\log\left(1-\frac{K\log L}{L}\right)
=
O_K\left(\frac{\log L}{L}\right).
\]
Also \(\pi(m)=O(m/\log m)\). Hence
\[
\sum_{z<p\le m}\left\lceil\frac mp\right\rceil
=
O_K\left(\frac{m\log\log m}{\log m}\right).
\]
\(\square\)

Comparing Lemmas 4 and 6 with \(z=m/(\log m)^K\),
\[
\frac{m/\sqrt{\log m}}
     {m\log\log m/\log m}
=
\frac{\sqrt{\log m}}{\log\log m}\longrightarrow\infty.
\]

Thus the standard random or greedy half-reservoir sieve produces only an
\[
O\left(\frac{m}{\sqrt{\log m}}\right)
\]
guarantee, while the entire terminal range has only
\[
O\left(\frac{m\log\log m}{\log m}\right)
\]
capacity. This is a gap in the method, not a proof of impossibility.

There is also a simpler singleton-cleanup criterion.

#### Lemma 7: Singleton cleanup

Let \(S_0\) and \(T\) be disjoint prime sets. If residue classes for \(S_0\) leave an uncovered set \(U\subseteq[m]\) satisfying
\[
|U|\le |T|,
\]
then residue classes for \(S_0\cup T\) can cover all of \([m]\).

#### Proof

Choose an injection \(n\mapsto p_n\) from \(U\) into \(T\), and set
\[
a_{p_n}\equiv n\pmod {p_n}.
\]
Each \(n\in U\) is then covered. Assign arbitrary residues to unused primes in \(T\). \(\square\)

For the alternating reservoirs,
\[
\#\bigl(C\cap(m/2,m]\bigr)\sim \frac{m}{4\log m}.
\]
Consequently, Route 1 would be completed by the following particularly concrete statement:
\[
\min_{\{a_p:p\in C,\ p\le m/2\}}
\#\left\{n\in[m]:
 n\not\equiv a_p\pmod p\ \forall p\in C,\ p\le m/2
\right\}
\le
\#\bigl(C\cap(m/2,m]\bigr)
\]
for both \(C=A,B\) and all sufficiently large \(m\).

The random/greedy estimate is larger than this target by a factor of order \(\sqrt{\log m}\).

---

### 5. Why an ordinary one-family construction cannot simply be duplicated

Suppose one attempted to give essentially all primes up to
\[
z=\frac{m}{(\log m)^K}
\]
to the first cover, as in a standard one-reservoir construction. The second cover would then have only primes exceeding \(z\). By Lemma 6 those primes have total capacity \(o(m)\), so they cannot cover \([m]\).

Therefore any successful Route 1 proof must genuinely divide the small and medium primes. It cannot run a usual construction for one color first and hope that the abundance of large unused primes is enough for the other color.

## Self-Audit

1. **The central robust covering lemma is unproved.**  
   This is not concealed: it is exactly why the status is BLOCKED. The conditional reduction to it is nevertheless rigorous and shows precisely what Route 1 must supply.

2. **The \(m/\sqrt{\log m}\) estimate is only an expectation and a greedy upper bound.**  
   It does not rule out rare or highly structured residue choices leaving \(O(m/\log m)\) points. I use it only to diagnose why random selection and elementary averaging do not close the argument.

3. **The terminal estimate uses standard quantitative PNT/Mertens estimates.**  
   The estimate is valid for fixed \(K\) and \(z=m/(\log m)^K\). It does not obstruct cleanup using substantially smaller primes or a structured matching in which medium primes cover many correlated survivors.

## Computations To Verify

The following program tests the alternating reservoirs, greedy residuals, and cleanup capacities.

```python
from math import ceil, log

def primes_upto(n):
    isprime = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        isprime[0] = 0
    if n >= 1:
        isprime[1] = 0
    for p in range(2, int(n**0.5) + 1):
        if isprime[p]:
            isprime[p*p:n+1:p] = b"\x00" * (((n - p*p)//p) + 1)
    return [p for p in range(2, n + 1) if isprime[p]]

def alternating_reservoirs(m):
    ps = primes_upto(m)
    A = ps[0::2]
    B = ps[1::2]
    return A, B

def greedy_residual(m, S):
    """
    Choose, for each p in S, a residue covering the largest number
    of currently uncovered points.
    """
    uncovered = set(range(1, m + 1))
    residues = {}

    for p in sorted(S):
        buckets = [[] for _ in range(p)]
        for n in uncovered:
            buckets[n % p].append(n)
        r = max(range(p), key=lambda x: len(buckets[x]))
        residues[p] = r
        uncovered.difference_update(buckets[r])

    return uncovered, residues

def terminal_capacity(m, T):
    return sum(ceil(m / p) for p in T)

def singleton_capacity(T):
    return len(T)

def diagnostics(m):
    A, B = alternating_reservoirs(m)

    for name, C in [("A", A), ("B", B)]:
        small = [p for p in C if p <= m // 2]
        terminal = [p for p in C if p > m // 2]

        U, residues = greedy_residual(m, small)

        log_expected = 0.0
        for p in small:
            log_expected += log(1.0 - 1.0 / p)
        expected = m * pow(2.718281828459045, log_expected)

        print({
            "m": m,
            "color": name,
            "small_primes": len(small),
            "terminal_primes": len(terminal),
            "greedy_uncovered": len(U),
            "random_expected_uncovered": expected,
            "singleton_capacity": singleton_capacity(terminal),
            "full_terminal_capacity": terminal_capacity(m, terminal),
            "singleton_ratio": len(U) / max(1, len(terminal)),
        })

for m in [100, 300, 1000, 3000, 10000, 30000]:
    diagnostics(m)
```

For exact testing of whether a fixed reservoir covers \([m]\), one can use `python-sat`:

```python
from pysat.solvers import Cadical153

def fixed_reservoir_sat(m, S):
    """
    Decide whether one class modulo each p in S can cover [m].
    Returns a residue witness or None.
    """
    next_var = 1
    var = {}

    for p in S:
        for r in range(p):
            var[p, r] = next_var
            next_var += 1

    solver = Cadical153()

    # Exactly one residue per prime.
    for p in S:
        solver.add_clause([var[p, r] for r in range(p)])
        for r in range(p):
            for s in range(r + 1, p):
                solver.add_clause([-var[p, r], -var[p, s]])

    # Cover every n in [m].
    for n in range(1, m + 1):
        solver.add_clause([var[p, n % p] for p in S])

    if not solver.solve():
        solver.delete()
        return None

    model = set(x for x in solver.get_model() if x > 0)
    witness = {}
    for p in S:
        for r in range(p):
            if var[p, r] in model:
                witness[p] = r
                break

    solver.delete()
    return witness

def test_alternating_partition(limit):
    for m in range(2, limit + 1):
        A, B = alternating_reservoirs(m)
        wa = fixed_reservoir_sat(m, A)
        wb = fixed_reservoir_sat(m, B)
        print(m, wa is not None, wb is not None)

# Pairwise exactly-one clauses make this suitable only for modest m.
# test_alternating_partition(100)
```

The most informative optimization is to minimize the residual after primes up to \(m/2\), then compare it with the number of reservoir primes in \((m/2,m]\). A MaxSAT implementation should add the coverage clause for each \(n\) as a unit-weight soft clause while retaining exactly-one-residue constraints as hard clauses.

## Route Diagnosis

**Proved ledger**

- A fixed alternating partition gives two reservoirs with discrepancy at most one in every prime interval.
- Each reservoir has reciprocal-prime mass
  \[
  \frac12\log\log z+O(1)
  \]
  and random-sieve density \(\asymp(\log z)^{-1/2}\).
- Elementary greedy selection leaves at most \(O(m/\sqrt{\log z})\) points.
- Primes in \((m/(\log m)^K,m]\) have only
  \[
  O_K(m\log\log m/\log m)
  \]
  total interval capacity.
- A robust positive-density covering lemma would solve the all-real problem directly.
- Giving essentially all small primes to one standard construction leaves the other color with insufficient total capacity.

**Plausible but unproved**

- A highly structured choice of residues from a half-density reservoir might reduce the survivor set from \(m/\sqrt{\log m}\) to \(O(m/\log m)\).
- Modern hypergraph-covering methods might exploit correlations among survivors strongly enough to beat the random-density prediction.
- Conversely, a lower-bound sieve might prove that such an improvement is impossible, but no available lower-bound argument reaches primes close enough to \(m\).

**Dead ends**

- Independent random residues: expected survivor count is too large.
- Elementary greedy residues: gives the same scale as the random expectation.
- Reserving only a terminal interval for the second cover: total capacity is \(o(m)\).
- Running an ordinary one-family Erdős–Rankin construction first and splitting unused primes afterward: the first construction monopolizes the reciprocal mass of the small primes.

**Precise block**

For a balanced reservoir \(C\), prove or refute
\[
\rho_C(m):=
\min_{\{a_p:p\in C,\ p\le m/2\}}
\#\{n\in[m]:n\not\equiv a_p\pmod p
          \ \forall p\in C,\ p\le m/2\}
\ll \frac{m}{\log m}.
\]
An upper bound with a sufficiently small constant would complete Route 1 by singleton cleanup. A lower bound
\[
\rho_C(m)\gg \frac{m}{\sqrt{\log m}}
\]
for at least one side of every partition would instead point toward disproof. Present methods establish neither statement.