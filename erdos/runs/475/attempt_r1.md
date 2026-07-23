STATUS: BLOCKED

## Result

I did not obtain a complete proof or disproof. I proved an explicit range-stitching lemma showing exactly which numerical constants and overlap moduli must be extracted from the cited asymptotic papers, and I gave a rigorous certificate architecture for the remaining finite verification, including the exact scaling-orbit count and a complete backtracking algorithm. The supplied asymptotic summaries do not determine any numerical threshold \(P_0\): the constants hidden in \(c\), \(1\ll_\alpha t\), “sufficiently large,” and the two independent \(o(1)\) terms are indispensable. Moreover, no finite certificate database was generated or checked here. Thus Route 1 is blocked at the two required deliverables: an explicit theorem-derived \(P_0\) and the corresponding exhaustive certificate set.

## Complete Argument

### 1. An effective range-stitching lemma

The following isolates precisely what must be obtained from the cited papers.

#### Lemma 1: Integer-safe stitching

Suppose there are explicit constants and functions with the following properties.

1. **Small range.** There are \(c_S>0\) and \(P_S\) such that, for every prime \(p\ge P_S\), validity holds whenever
   \[
   1\le t\le X(p):=\exp\!\bigl(c_S(\log p)^{1/3}\bigr).
   \]

2. **Medium range.** For some fixed \(\alpha\in(0,1)\), there are explicit integers \(C_\alpha,P_M(\alpha)\) such that, for every prime \(p\ge P_M(\alpha)\), validity holds whenever
   \[
   C_\alpha\le t\le Y(p):=p^{1-\alpha}.
   \]

3. **Large range.** There are explicit \(c_L>0,P_L\) and an explicit real-valued upper cutoff \(U_L(p)\) such that, for every prime \(p\ge P_L\), validity holds whenever
   \[
   Z(p):=p^{1-c_L}\le t\le U_L(p).
   \]

4. **Very large range.** There are an explicit \(P_V\) and explicit real-valued lower cutoff \(W_V(p)\) such that, for every prime \(p\ge P_V\), validity holds whenever
   \[
   W_V(p)\le t\le p-1.
   \]

Assume that \(\alpha<c_L\), and that there is an explicit \(P_{LV}\) such that
\[
\lfloor U_L(p)\rfloor+1\ge \lceil W_V(p)\rceil
\qquad(p\ge P_{LV}).
\]
Then every subset of \(\mathbb F_p^\times\) has a valid ordering for every prime
\[
p\ge P_0,
\]
where one may take
\[
P_0=
\max\left\{
P_S,\,
P_M(\alpha),\,
P_L,\,
P_V,\,
P_{LV},\,
\left\lceil
\exp\!\left(
\left(\frac{\log \max(C_\alpha,1)}{c_S}\right)^3
\right)
\right\rceil
\right\}.
\]

#### Proof

Fix a prime \(p\ge P_0\) and an integer \(1\le t\le p-1\).

The definition of \(P_0\) gives \(X(p)\ge C_\alpha\), hence
\[
\lfloor X(p)\rfloor+1\ge C_\alpha.
\]
Thus either \(t\le X(p)\), in which case the small-range theorem applies, or
\[
t\ge \lfloor X(p)\rfloor+1\ge C_\alpha.
\]

In the latter case, if \(t\le Y(p)\), the medium-range theorem applies. Otherwise,
\[
t\ge \lfloor Y(p)\rfloor+1.
\]
Since \(\alpha<c_L\) and \(p>1\),
\[
Y(p)=p^{1-\alpha}>p^{1-c_L}=Z(p).
\]
It follows that
\[
\lfloor Y(p)\rfloor+1\ge \lceil Z(p)\rceil,
\]
so \(t\ge Z(p)\).

If \(t\le U_L(p)\), the large-range theorem applies. Otherwise,
\[
t\ge \lfloor U_L(p)\rfloor+1
   \ge \lceil W_V(p)\rceil,
\]
and the very-large-range theorem applies. These cases cover every integer \(t\in[1,p-1]\). ∎

### 2. Why the supplied asymptotic statements do not yield \(P_0\)

The preceding lemma cannot be numerically instantiated from the brief alone.

First, a statement
\[
t\le \exp\!\bigl(c(\log p)^{1/3}\bigr)
\quad\text{for some }c>0
\]
does not specify \(c\) or the lower threshold on \(p\). For any proposed numerical bound \(M\), the same qualitative statement is compatible with a proof whose declared threshold exceeds \(M\), or whose admissible \(c\) is too small to reach \(C_\alpha\) before \(M\).

Second, \(1\ll_\alpha t\) does not give \(C_\alpha\), nor necessarily the prime threshold \(P_M(\alpha)\). Since the small-to-medium threshold contains
\[
\exp\!\left(\left(\frac{\log C_\alpha}{c_S}\right)^3\right),
\]
even moderate changes in \(C_\alpha\) or \(c_S\) can change the resulting \(P_0\) drastically.

Third, two independent statements involving \(1-o(1)\) do not by themselves imply overlap. For example, the ranges
\[
t\le \left(1-\frac1{\sqrt{\log p}}\right)p
\]
and
\[
t\ge \left(1-\frac1{\log p}\right)p
\]
both have endpoints of the form \((1-o(1))p\), but leave a nonempty gap for large \(p\). Therefore an explicit parameterized version of the large and very-large theorems is needed to prove
\[
\lfloor U_L(p)\rfloor+1\ge\lceil W_V(p)\rceil.
\]

Consequently, no explicit \(P_0\) is logically recoverable merely from the asymptotic notation quoted in the brief. The complete proofs, including all parameter hierarchies and all occurrences of “sufficiently large,” must be audited.

### 3. Exact finite certificate theorem

Once an explicit \(P_0\) is available, the finite part can be certified using scaling alone.

For a subset \(A\subseteq\mathbb F_p^\times\), define
\[
\operatorname{can}(A):=
\min_{\lambda\in\mathbb F_p^\times}\lambda A,
\]
where subsets are compared by any fixed total ordering, for example their integer bitmasks.

#### Lemma 2: A certificate per scaling orbit suffices

Assume:

1. the conjecture is proved theoretically for every prime \(p\ge P_0\);
2. for every prime \(p<P_0\), every integer
   \[
   13\le t\le p-4,
   \]
   and every canonical scaling representative \(C\subseteq\mathbb F_p^\times\) of size \(t\), a valid ordering of \(C\) is supplied and checked.

Then the conjecture holds for every prime and every subset of \(\mathbb F_p^\times\).

#### Proof

Let \(A\subseteq\mathbb F_p^\times\).

If \(p\ge P_0\), apply the assumed theoretical theorem.

Suppose \(p<P_0\). The known results in the brief cover \(|A|\le12\) and \(|A|\ge p-3\). It remains only to consider
\[
13\le |A|\le p-4.
\]

Let \(C=\operatorname{can}(A)\). Then \(C=\lambda A\) for some \(\lambda\ne0\). By hypothesis, \(C\) has a valid ordering
\[
(c_1,\dots,c_t).
\]
Then
\[
(\lambda^{-1}c_1,\dots,\lambda^{-1}c_t)
\]
is an ordering of \(A\), and its partial sums are \(\lambda^{-1}\) times those of the ordering of \(C\). Multiplication by \(\lambda^{-1}\) is injective, so the partial sums remain pairwise distinct. ∎

This certificate design does not use translation, complementation, reversal, or any other unproved symmetry.

### 4. Exact number of scaling orbits

The finite workload can be counted before any search.

#### Lemma 3: Orbit-count formula

Let \(n=p-1\). The number \(\mathcal O_p(t)\) of scaling orbits of \(t\)-element subsets of \(\mathbb F_p^\times\) is
\[
\boxed{
\mathcal O_p(t)
=
\frac1{p-1}
\sum_{d\mid\gcd(p-1,t)}
\varphi(d)
\binom{(p-1)/d}{t/d}
}.
\]

#### Proof

Apply Burnside’s lemma to the action of \(\mathbb F_p^\times\) on its \(t\)-element subsets by multiplication.

If \(\lambda\) has multiplicative order \(d\), then multiplication by \(\lambda\) partitions \(\mathbb F_p^\times\) into \((p-1)/d\) cycles, each of length \(d\). A subset is invariant under \(\lambda\) exactly when it is a union of these cycles. Hence the number of invariant \(t\)-subsets is zero unless \(d\mid t\), and otherwise is
\[
\binom{(p-1)/d}{t/d}.
\]
There are \(\varphi(d)\) elements of order \(d\) in the cyclic group \(\mathbb F_p^\times\). Burnside’s lemma gives the formula. ∎

The first unresolved workloads are:

\[
\begin{array}{c|c|r}
p&t&\mathcal O_p(t)\\ \hline
17&13&35\\
19&13&476\\
19&14&172\\
19&15&46\\
23&13&22610\\
23&14&14550\\
23&15&7752\\
23&16&3399\\
23&17&1197\\
23&18&335\\
23&19&70
\end{array}
\]

Thus there are \(694\) relevant orbits for \(p=19\), but already \(49{,}913\) for \(p=23\). For comparison,
\[
\mathcal O_{29}(14)=1{,}432{,}860.
\]
Scaling therefore provides only a roughly linear reduction of an intrinsically exponential subset space.

### 5. Completeness of the exact search

For a fixed \(A\), a state is
\[
(U,V),
\]
where \(U\subseteq A\) is the set of used elements and \(V\subseteq\mathbb F_p\) is the set of partial sums already encountered. The current sum is determined by \(U\):
\[
s(U)=\sum_{a\in U}a.
\]

A successor obtained by appending \(a\in A\setminus U\) is legal exactly when
\[
s(U)+a\notin V.
\]

#### Lemma 4: Exact DFS is complete

A depth-first search that explores every legal successor from every state \((U,V)\), memoizing failed states by the full pair \((U,V)\), returns an ordering if and only if \(A\) has a valid ordering.

#### Proof

Every path from the root \((\varnothing,\varnothing)\) corresponds to a sequence of distinct elements of \(A\). By induction on the path length, \(V\) is exactly the set of partial sums of that sequence. Therefore a transition is accepted exactly when the new partial sum differs from all earlier partial sums.

Consequently, every root-to-depth-\(|A|\) path is a valid ordering, and every valid ordering determines such a path. Exploring all legal successors is therefore complete.

Memoization by \((U,V)\) is sound because all possible future transitions depend only on the unused elements \(A\setminus U\), the current sum \(s(U)\), and the forbidden partial sums \(V\). Both the unused set and current sum are determined by \(U\). ∎

If a search finds no ordering for a candidate \(A\), an independently checkable dynamic-programming UNSAT certificate can consist of a finite family \(\mathcal F\) of states such that:

1. \((\varnothing,\varnothing)\in\mathcal F\);
2. no terminal state belongs to \(\mathcal F\);
3. every legal successor of every state in \(\mathcal F\) also belongs to \(\mathcal F\).

Any successful path would remain in \(\mathcal F\) and end at a terminal state, a contradiction. This is an alternative to an LRAT certificate.

### 6. Ledger

**Proved here**

- The integer-safe effective range-stitching lemma.
- The sufficiency of one checked ordering per scaling orbit.
- The exact Burnside orbit-count formula.
- Completeness of DFS memoized by \((U,V)\).
- Correctness of the proposed positive and negative certificate formats.

**Plausible but unproved**

- That all constants in the cited asymptotic proofs are effectively extractable without adding new arguments.
- That the resulting \(P_0\) is small enough for exhaustive subset verification.
- That every finite candidate is positive; no exhaustive computation was performed here.

**Dead ends**

- Inferring a numerical \(P_0\) from the qualitative asymptotic statements: impossible because the necessary constants and convergence moduli are absent.
- Inferring overlap from two independent \(1-o(1)\) cutoffs: false in general.
- Relying on scaling to make a large threshold computationally feasible: orbit counts remain exponential.
- Using complementation as a search reduction: no such symmetry has been proved.

## Self-Audit

1. **The actual asymptotic papers were not normalized into the hypotheses of Lemma 1.** The lemma is conditional and does not itself establish that the papers provide cutoffs of precisely that form. I believe the stitching argument is correct once such data are supplied, but I do not claim the required data have been extracted.

2. **The finite-search code below has not been executed here, and there is no certificate archive.** Its correctness follows from Lemmas 2 and 4 and can be inspected independently, but source code without completed output is not a finite verification.

3. **The orbit counts are not evidence that the search is practically feasible.** They accurately measure the number of scaling orbits, and the formula is proved, but runtime depends heavily on how difficult individual ordering searches are. No benchmark justifies extrapolating feasibility beyond the smallest primes.

## Computations To Verify

The following Python uses exact integer and modular arithmetic. The first part verifies the orbit counts.

```python
from math import comb, gcd

def divisors(n):
    out = []
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            out.append(d)
            if d*d != n:
                out.append(n // d)
    return sorted(out)

def phi(n):
    result = n
    q = n
    r = 2
    while r*r <= q:
        if q % r == 0:
            while q % r == 0:
                q //= r
            result -= result // r
        r += 1
    if q > 1:
        result -= result // q
    return result

def orbit_count(p, t):
    n = p - 1
    total = 0
    for d in divisors(gcd(n, t)):
        total += phi(d) * comb(n // d, t // d)
    assert total % n == 0
    return total // n

for p in [17, 19, 23]:
    print("p =", p)
    total = 0
    for t in range(13, p - 3):  # 13 <= t <= p-4
        x = orbit_count(p, t)
        total += x
        print(t, x)
    print("total", total)

print("p=29, t=14:", orbit_count(29, 14))
```

Expected output:

```text
p = 17
13 35
total 35

p = 19
13 476
14 172
15 46
total 694

p = 23
13 22610
14 14550
15 7752
16 3399
17 1197
18 335
19 70
total 49913

p=29, t=14: 1432860
```

An exact solver for a fixed set is:

```python
from functools import lru_cache

def find_valid_order(p, A):
    elems = tuple(sorted(A))
    n = len(elems)
    full = (1 << n) - 1

    @lru_cache(maxsize=None)
    def dfs(used, seen):
        if used == full:
            return ()

        # Current sum is determined by the used subset.
        s = sum(elems[i] for i in range(n)
                if (used >> i) & 1) % p

        for i, a in enumerate(elems):
            if (used >> i) & 1:
                continue
            z = (s + a) % p
            if (seen >> z) & 1:
                continue

            tail = dfs(used | (1 << i), seen | (1 << z))
            if tail is not None:
                return (a,) + tail

        return None

    return dfs(0, 0)
```

The empty partial sum is correctly excluded because the initial `seen` mask is zero, not `1 << 0`.

A standalone checker for a JSON-lines certificate database is:

```python
import itertools
import json

def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def mask_of(A):
    m = 0
    for a in A:
        m |= 1 << a
    return m

def set_of_mask(mask, p):
    return {a for a in range(1, p) if (mask >> a) & 1}

def scale_mask(mask, lam, p):
    out = 0
    for a in range(1, p):
        if (mask >> a) & 1:
            out |= 1 << ((lam * a) % p)
    return out

def canonical_mask(mask, p):
    return min(scale_mask(mask, lam, p) for lam in range(1, p))

def valid_order(p, A, order):
    if len(order) != len(A) or set(order) != set(A):
        return False
    if any(a <= 0 or a >= p for a in order):
        return False

    seen = set()  # Do not insert 0 here.
    s = 0
    for a in order:
        s = (s + a) % p
        if s in seen:
            return False
        seen.add(s)
    return True

def verify_database(P0, filename):
    """
    This checks the finite part only.
    A separate mathematical proof must certify that p >= P0 is covered.
    """
    certs = {}

    with open(filename, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, 1):
            rec = json.loads(line)
            p = int(rec["p"])
            mask = int(rec["mask"])
            order = tuple(map(int, rec["order"]))
            key = (p, mask)

            assert key not in certs, ("duplicate", line_number, key)
            assert is_prime(p) and p < P0
            A = set_of_mask(mask, p)
            assert 13 <= len(A) <= p - 4
            assert mask == canonical_mask(mask, p)
            assert valid_order(p, A, order)
            certs[key] = order

    found = set()

    for p in range(2, P0):
        if not is_prime(p):
            continue
        for t in range(13, p - 3):
            for tup in itertools.combinations(range(1, p), t):
                mask = mask_of(tup)
                if mask != canonical_mask(mask, p):
                    continue
                key = (p, mask)
                assert key in certs, ("missing certificate", key)
                found.add(key)

    assert found == set(certs), "extra or missing certificate records"
    print("finite certificate database verified")
```

Each record has the form

```json
{"p":17,"mask":123456,"order":[1,4,7,2, ...]}
```

where the mask must represent a canonical scaling representative. A complete Route 1 proof would publish:

1. the explicit derivation of \(P_0\);
2. this or an equivalent independent checker;
3. the certificate database;
4. a cryptographic hash of the checked database;
5. the checker’s complete output and software environment.

## Route Diagnosis

The abstract range stitching works cleanly, and the finite certification problem has a rigorous, simple format. The decisive block is upstream: the brief omits the numerical constants and parameter dependencies needed to calculate \(P_0\). Even the large/very-large overlap cannot be certified from the displayed \(o(1)\) notation. After that extraction, a second potential block is computational: scaling reduces the subset count only by about \(p-1\), and already one size at \(p=29\) has over \(1.4\) million orbits.

A fresh Route 1 attempt should first obtain the complete cited proofs and create a line-by-line constants ledger recording \(c_S\), \(C_\alpha\), every prime threshold, and explicit large/very-large cutoff functions. The value of \(P_0\) should be calculated before substantial exhaustive computation begins. In parallel, the \(35\), \(694\), and \(49{,}913\) orbit workloads for \(p=17,19,23\) should be searched immediately with independent certificate generation and checking; this would test for a small exceptional counterexample and benchmark the solver. If the extracted \(P_0\) exceeds the low tens, naive Route 1 is likely computationally blocked and should be supplemented by a new structural reduction or proof-producing SAT search rather than unsupported brute force.