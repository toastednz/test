STATUS: BLOCKED

## Result

Route 3 yields a rigorous but subcritical construction: for some absolute \(c>0\), every sufficiently large cutoff \(N\) admits two disjoint prime-residue covers of an interval of length
\[
L=\left\lfloor \frac{cN}{\sqrt{\log N}}\right\rfloor.
\]
Equivalently, \(Q_N\) can be split as \(uv\) with \(\min(j(u),j(v))\gg N/\sqrt{\log N}\). I also prove an exact characterization of cleanup by primes in \((N/2,N]\), and show rigorously that a sieve using only primes up to \(O(\log N)\), followed by such terminal cleanup, cannot solve the problem. The unresolved step is a genuinely stronger, structured medium-prime sieve capable of reducing both residual sets from their natural \(N/\sqrt{\log N}\) scale to \(O(N/\log N)\). Terminal matching can improve capacity by at most a factor of two, so it cannot bridge this gap.

## Complete Argument

Throughout, all logarithms are natural.

### 1. A deterministic greedy sieve lemma

For a prime \(p\), residue \(r\pmod p\), and interval \([L]\), write
\[
C_{p,r}:=\{n\in[L]:n\equiv r\pmod p\}.
\]

**Lemma 1.**  
Let \(S\) be a finite set of primes. There are residues \(a_p\pmod p\), \(p\in S\), such that the uncovered set
\[
U=\{n\in[L]: n\not\equiv a_p\pmod p\text{ for every }p\in S\}
\]
satisfies
\[
|U|\le L\prod_{p\in S}\left(1-\frac1p\right).
\]

**Proof.** Start with \(U_0=[L]\). Process the primes of \(S\) in any order. If the current uncovered set is \(U\), its elements are partitioned among the \(p\) residue classes modulo \(p\). Hence some residue class contains at least \(|U|/p\) elements. Select such a residue. The new uncovered set \(U'\) therefore satisfies
\[
|U'|\le |U|-\frac{|U|}{p}
       =|U|\left(1-\frac1p\right).
\]
Iteration gives the result. \(\square\)

This is completely deterministic; no independence assertion is involved.

---

### 2. Splitting the multiplicative sieve density evenly

Put
\[
w_p=-\log\left(1-\frac1p\right)>0.
\]

**Lemma 2.**  
Any finite prime set \(S\) can be partitioned as \(S=S_A\sqcup S_B\) so that
\[
\left|\sum_{p\in S_A}w_p-\sum_{p\in S_B}w_p\right|\le \log 2.
\]
Consequently, writing
\[
\delta_i=\prod_{p\in S_i}\left(1-\frac1p\right),
\qquad
D=\prod_{p\in S}\left(1-\frac1p\right),
\]
one has
\[
\delta_A,\delta_B\le \sqrt{2D}.
\]

**Proof.** Assign the weights one at a time, always putting the next weight into the currently lighter bin. If the discrepancy before assigning a weight \(w\) is \(d\), the new discrepancy is \(|d-w|\), hence at most \(\max(d,w)\). Inductively the final discrepancy is at most the largest weight, namely \(w_2=\log 2\).

Let
\[
W_i=\sum_{p\in S_i}w_p,\qquad W=W_A+W_B.
\]
Then \(W_i\ge (W-\log2)/2\), so
\[
\delta_i=e^{-W_i}
 \le e^{(\log2)/2}e^{-W/2}
 =\sqrt{2D}.
\]
\(\square\)

---

### 3. A rigorous two-cover theorem at length \(N/\sqrt{\log N}\)

**Theorem 3.**  
There is an absolute constant \(c>0\) such that, for every sufficiently large integer \(N\), the primes at most \(N\) can be partitioned into two nonempty sets \(A,B\), with one residue chosen for each prime, so that both colors cover
\[
\left[\,\left\lfloor \frac{cN}{\sqrt{\log N}}\right\rfloor\,\right].
\]
Equivalently, if
\[
Q_N=\prod_{p\le N}p,
\]
there is a factorization \(Q_N=uv\), \(\gcd(u,v)=1\), \(u,v>1\), such that
\[
\min\{j(u),j(v)\}\ge
\left\lfloor \frac{cN}{\sqrt{\log N}}\right\rfloor+1.
\]

**Proof.** Let
\[
S=\{p:p\le N/2\},\qquad
T=\{p:N/2<p\le N\}.
\]
Use Lemma 2 to partition \(S=S_A\sqcup S_B\). By Mertens’ product theorem,
\[
D:=\prod_{p\le N/2}\left(1-\frac1p\right)
\le \frac{C_0}{\log N}
\]
for some absolute \(C_0\) and all sufficiently large \(N\). Hence
\[
\delta_i:=\prod_{p\in S_i}\left(1-\frac1p\right)
\le \sqrt{2D}
\le \frac{C_1}{\sqrt{\log N}},
\qquad i\in\{A,B\},
\]
for an absolute \(C_1\).

Split \(T=T_A\sqcup T_B\) into two sets whose cardinalities differ by at most one. The prime number theorem gives
\[
|T|=\pi(N)-\pi(N/2)\sim \frac{N}{2\log N}.
\]
Thus there is an absolute \(c_0>0\) such that, for sufficiently large \(N\),
\[
|T_A|,|T_B|\ge c_0\frac{N}{\log N}.
\]

Choose
\[
c\le \frac{c_0}{2C_1}
\]
and put
\[
L=\left\lfloor \frac{cN}{\sqrt{\log N}}\right\rfloor.
\]

Apply Lemma 1 independently to \(S_A\) and \(S_B\). This produces residues for the small primes and residual sets \(U_A,U_B\subseteq[L]\) with
\[
|U_i|\le L\delta_i
\le \frac{cC_1N}{\log N}
\le \frac{c_0N}{2\log N}
\le |T_i|.
\]

For each color \(i\), inject \(U_i\) into \(T_i\). If \(n\in U_i\) is assigned to \(p\in T_i\), choose
\[
a_p\equiv n\pmod p.
\]
Then \(p\) covers \(n\). There are enough distinct primes because \(|U_i|\le |T_i|\). Any unused terminal primes receive arbitrary residues. Thus every element of \([L]\) is covered by both colors.

Since a cover of \([L]\) by a prime set \(A\) is equivalent to \(j(P_A)\ge L+1\), the Jacobsthal assertion follows. \(\square\)

The theorem falls short of the Erdős problem by the factor \(\sqrt{\log N}\).

---

### 4. Exact geometry of terminal cleanup

Singleton cleanup is not always optimal: a prime \(p>L/2\) can sometimes cover two residual points differing by \(p\). The following gives the exact criterion.

Let \(T\subseteq\{p:L/2<p\le L\}\) and \(U\subseteq[L]\). A **\(T\)-rainbow matching** in \(U\) is a family of vertex-disjoint pairs
\[
\{u,v\}\subseteq U
\]
such that \(|u-v|\in T\), with different pairs having different prime differences.

**Lemma 4.**  
The set \(U\) can be covered by choosing one residue class modulo every prime in \(T\) if and only if \(U\) has a \(T\)-rainbow matching of size at least
\[
|U|-|T|.
\]

**Proof.**

Suppose first that \(U\) is covered. Assign every \(u\in U\) to one prime whose selected class covers it. Since \(p>L/2\), a residue class modulo \(p\) contains at most two points of \([L]\). If it contains two assigned points, their difference is exactly \(p\). The primes with two assigned points therefore give a \(T\)-rainbow matching. If there are \(d\) double fibers and \(s\) single fibers, then
\[
|U|=2d+s,\qquad d+s\le |T|.
\]
Thus
\[
d=|U|-(d+s)\ge |U|-|T|.
\]

Conversely, suppose there is such a matching of size \(d\). Use its \(d\) distinct prime labels to cover the matched pairs. There remain \(|U|-2d\) points and \(|T|-d\) unused primes. Since
\[
d\ge |U|-|T|,
\]
we have
\[
|U|-2d\le |T|-d.
\]
Assign the remaining points injectively to unused primes and cover them as singletons. \(\square\)

**Corollary 5.**  
Terminal primes in \((L/2,L]\) can cover at most \(2|T|\) residual points. Thus pair cleanup improves terminal capacity by at most a factor of two.

For the target \(L=N\),
\[
\#\{p:N/2<p\le N\}\asymp \frac{N}{\log N}.
\]
Therefore terminal cleanup, even under perfect pairing, can handle only \(O(N/\log N)\) residual points.

---

### 5. A rigorous failure theorem for “tiny sieve plus terminal cleanup”

The natural objection to the density barrier is that carefully chosen residues might leave far fewer points than the multiplicative estimate. For primes only up to \(O(\log N)\), this is impossible uniformly.

**Lemma 6.**  
Let \(S\) be a finite prime set, and choose arbitrary residues \(a_p\pmod p\). Then the number of elements of \([N]\) avoiding all selected classes is
\[
N\prod_{p\in S}\left(1-\frac1p\right)+O(2^{|S|}),
\]
where the implied constant is \(1\), uniformly in the residues.

**Proof.** By inclusion-exclusion,
\[
|U|
=\sum_{E\subseteq S}(-1)^{|E|}
 \#\{n\in[N]:n\equiv a_p\pmod p\text{ for every }p\in E\}.
\]
For \(E\subseteq S\), the CRT turns the simultaneous congruences into one residue class modulo
\[
d_E=\prod_{p\in E}p.
\]
The number of elements of \([N]\) in that class is
\[
\frac{N}{d_E}+O(1),
\]
with absolute error at most \(1\). Hence
\[
|U|
=N\sum_{E\subseteq S}\frac{(-1)^{|E|}}{d_E}
 +O(2^{|S|})
=N\prod_{p\in S}\left(1-\frac1p\right)+O(2^{|S|}).
\]
\(\square\)

**Theorem 7.**  
Fix \(C>0\). For all sufficiently large \(N\), the following architecture cannot produce two covers of \([N]\):

1. partition the primes \(p\le z\), where \(z\le C\log N\), between two colors and choose arbitrary residues;
2. use only primes \(N/2<p\le N\) for cleanup.

**Proof.** Let the small-prime sets be \(S_A,S_B\), and put
\[
\delta_i=\prod_{p\in S_i}\left(1-\frac1p\right).
\]
Because they partition the primes up to \(z\),
\[
\delta_A\delta_B
=\prod_{p\le z}\left(1-\frac1p\right).
\]
By Mertens’ theorem, for some absolute \(c_1>0\),
\[
\delta_A\delta_B\ge \frac{c_1}{\log(z+2)}.
\]
Thus one color, say \(i\), satisfies
\[
\delta_i\ge \frac{\sqrt{c_1}}{\sqrt{\log(z+2)}}.
\]

By Lemma 6, its residual set after the small-prime stage has size at least
\[
N\delta_i-2^{\pi(z)}.
\]
Since \(z\le C\log N\), the prime number theorem or Chebyshev’s bound gives
\[
\pi(z)=O\left(\frac{\log N}{\log\log N}\right),
\]
and hence
\[
2^{\pi(z)}=N^{o(1)}.
\]
Meanwhile,
\[
N\delta_i\gg \frac{N}{\sqrt{\log\log N}}.
\]
Therefore this color has
\[
|U_i|\gg \frac{N}{\sqrt{\log\log N}}.
\]

Every class modulo a prime \(p>N/2\) contains at most two points of \([N]\). Even granting this color every terminal prime, those classes cover at most
\[
2\bigl(\pi(N)-\pi(N/2)\bigr)
=O\left(\frac{N}{\log N}\right)
\]
points. Since
\[
\frac{N}{\sqrt{\log\log N}}\gg \frac{N}{\log N},
\]
the terminal primes cannot cover \(U_i\). \(\square\)

This theorem does not rule out medium primes; instead, it proves that medium scales are indispensable.

---

### 6. A capacity obstruction to a simple asymmetric size split

One tempting alternative is to give one color all small primes and the other all primes above \(N^\alpha\).

**Lemma 8.**  
Fix \(\alpha>e^{-1}\). For sufficiently large \(N\), no set of primes contained in
\[
(N^\alpha,N]
\]
can cover \([N]\), regardless of the chosen residues.

**Proof.** A class modulo \(p\) contains at most \(\lceil N/p\rceil\) points, so its total possible capacity is at most
\[
\sum_{N^\alpha<p\le N}\left\lceil\frac Np\right\rceil
\le
N\sum_{N^\alpha<p\le N}\frac1p+\pi(N).
\]
Mertens’ reciprocal-prime theorem gives
\[
\sum_{N^\alpha<p\le N}\frac1p
=\log\log N-\log\log(N^\alpha)+o(1)
=-\log\alpha+o(1).
\]
Also \(\pi(N)=o(N)\). Since \(\alpha>e^{-1}\), we have \(-\log\alpha<1\). Thus the displayed capacity is \(<N\) for all sufficiently large \(N\), making a cover impossible. \(\square\)

Hence, for example, giving one color only primes above \(\sqrt N\) is ruled out even before overlap is considered. Thresholds at or below \(N^{1/e}\) are not resolved by this argument.

---

### 7. The precise unresolved lemma

Let
\[
S=\{p:p\le N/2\},\qquad
T=\{p:N/2<p\le N\}.
\]
A sufficient statement for Route 3 would be:

> **Structured two-sieve lemma.** Partition \(S=S_A\sqcup S_B\) and choose one class for each small prime so that the two residual sets satisfy
> \[
> |U_A|+|U_B|\le |T|.
> \]

Indeed, one could allocate \(|U_A|\) terminal primes to color \(A\), \(|U_B|\) to color \(B\), and cover all residual points as singletons.

However,
\[
|T|\sim \frac{N}{2\log N},
\]
whereas balanced multiplicative sieving naturally gives
\[
|U_A|+|U_B|\asymp \frac{N}{\sqrt{\log N}}.
\]
Thus the needed lemma must beat the density-product scale by a factor of order \(\sqrt{\log N}\). Lemma 4 shows that terminal pairing changes this only by a constant factor.

No argument obtained here proves this structured lemma. Proving it would constitute a substantial new two-channel sieve theorem, not a routine matching refinement.

## Self-Audit

1. **The subcritical construction uses Mertens’ theorem and the prime number theorem without reproving them.** These are standard unconditional theorems, and they are used only for coarse inequalities with unspecified absolute constants. No conjectural distribution of primes in progressions is used.

2. **The failure theorem applies only to small primes \(p\le O(\log N)\) followed directly by primes \(p>N/2\).** It does not rule out Route 3 with a broad medium-prime stage. I believe the theorem itself is correct because the uniform inclusion-exclusion error is explicit, but its scope must not be overstated.

3. **The terminal matching characterization is restricted to \(p>L/2\).** For smaller cleanup primes, one class may cover three or more points, so the rainbow-matching model no longer applies. Within the stated range the proof is exact: any two points in one class differ by \(p\), and three points cannot fit into \([L]\).

## Computations To Verify

The following code constructs and verifies the \(N/\sqrt{\log N}\)-scale witness. For practical experiments, one supplies \(L\) and checks whether the available terminal primes suffice.

```python
from math import log

def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\x00" * (((n - p*p)//p) + 1)
    return [p for p in range(2, n + 1) if sieve[p]]

def balanced_small_partition(S):
    bins = [[], []]
    mass = [0.0, 0.0]
    # Descending weights are convenient, though not necessary.
    for p in sorted(S):
        c = 0 if mass[0] <= mass[1] else 1
        bins[c].append(p)
        mass[c] += -log(1.0 - 1.0/p)
    return bins

def greedy_sieve(L, prime_set):
    U = set(range(1, L + 1))
    residues = {}
    for p in prime_set:
        counts = [0] * p
        for n in U:
            counts[n % p] += 1
        r = max(range(p), key=lambda x: counts[x])
        residues[p] = r
        U = {n for n in U if n % p != r}
    return U, residues

def route3_witness(N, L):
    ps = primes_upto(N)
    S = [p for p in ps if 2*p <= N]
    T = [p for p in ps if 2*p > N]

    SA, SB = balanced_small_partition(S)
    UA, resA = greedy_sieve(L, SA)
    UB, resB = greedy_sieve(L, SB)

    # Adaptive singleton allocation is at least as strong as a fixed equal split.
    if len(UA) + len(UB) > len(T):
        return None, (len(UA), len(UB), len(T))

    color = {}
    residue = {}

    for p in SA:
        color[p] = 0
        residue[p] = resA[p]
    for p in SB:
        color[p] = 1
        residue[p] = resB[p]

    pos = 0
    for n in sorted(UA):
        p = T[pos]
        pos += 1
        color[p] = 0
        residue[p] = n % p

    for n in sorted(UB):
        p = T[pos]
        pos += 1
        color[p] = 1
        residue[p] = n % p

    # Distribute unused terminal primes arbitrarily.
    turn = 0
    while pos < len(T):
        p = T[pos]
        pos += 1
        color[p] = turn
        residue[p] = 0
        turn ^= 1

    # Direct verification.
    for n in range(1, L + 1):
        hit = [False, False]
        for p in ps:
            if n % p == residue[p]:
                hit[color[p]] = True
        assert hit == [True, True]

    return (color, residue), (len(UA), len(UB), len(T))

# Suggested experiments:
# for N in [1000, 3000, 10000, 30000, 100000]:
#     for scale in [0.02, 0.05, 0.1, 0.2]:
#         L = int(scale * N / (log(N)**0.5))
#         witness, data = route3_witness(N, L)
#         print(N, L, witness is not None, data)
```

The central unproved structured lemma can be tested exactly with CP-SAT by minimizing the total residual after primes at most \(m/2\):

```python
# Requires: pip install ortools
from ortools.sat.python import cp_model

def optimum_two_stage_residual(m):
    small = [p for p in primes_upto(m) if 2*p <= m]

    model = cp_model.CpModel()

    # x[p,c,r] means p is assigned color c and residue r.
    x = {}
    for p in small:
        for c in range(2):
            for r in range(p):
                x[p, c, r] = model.NewBoolVar(f"x_{p}_{c}_{r}")
        model.Add(
            sum(x[p, c, r] for c in range(2) for r in range(p)) == 1
        )

    # u[n,c] is forced to 1 if n has no small-prime hit in color c.
    u = {}
    for n in range(1, m + 1):
        for c in range(2):
            u[n, c] = model.NewBoolVar(f"u_{n}_{c}")
            hits = [x[p, c, n % p] for p in small]
            model.Add(u[n, c] + sum(hits) >= 1)

    model.Minimize(sum(u.values()))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 3600
    solver.parameters.num_search_workers = 8
    status = solver.Solve(model)

    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return None

    residual = [set(), set()]
    choices = {}
    for p in small:
        for c in range(2):
            for r in range(p):
                if solver.Value(x[p, c, r]):
                    choices[p] = (c, r)

    for n in range(1, m + 1):
        for c in range(2):
            if solver.Value(u[n, c]):
                residual[c].add(n)

    terminal_count = len([p for p in primes_upto(m) if 2*p > m])
    return {
        "objective": len(residual[0]) + len(residual[1]),
        "terminal_count": terminal_count,
        "singleton_completion_possible":
            len(residual[0]) + len(residual[1]) <= terminal_count,
        "residual": residual,
        "choices": choices,
    }
```

Terminal pair cleanup can be checked via the exact rainbow-matching ILP:

```python
from ortools.sat.python import cp_model

def terminal_pair_test(L, U, T):
    U = set(U)
    T = [p for p in T if L/2 < p <= L]

    model = cp_model.CpModel()
    edge = {}

    for p in T:
        for n in U:
            if n + p in U:
                edge[p, n] = model.NewBoolVar(f"e_{p}_{n}")

    # At most one pair uses each prime.
    for p in T:
        model.Add(sum(edge[p, n] for q, n in edge if q == p) <= 1)

    # Matching condition on residual vertices.
    for v in U:
        incident = []
        for (p, n), var in edge.items():
            if v == n or v == n + p:
                incident.append(var)
        model.Add(sum(incident) <= 1)

    model.Maximize(sum(edge.values()))
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return None

    matching_size = round(solver.ObjectiveValue())
    required = max(0, len(U) - len(T))
    return {
        "matching_size": matching_size,
        "required_size": required,
        "cover_possible": matching_size >= required,
    }
```

The most informative finite diagnostic is the ratio
\[
\frac{|U_A|+|U_B|}{\pi(m)-\pi(m/2)}
\]
after exact optimization over the small-prime stage. Values persistently near \(\sqrt{\log m}\) would support the diagnosed barrier; values trending below \(1\) would reveal a route to a proof.

## Route Diagnosis

**Proved ledger.**

1. Greedy private sieving leaves at most \(L\prod_{p\in S}(1-1/p)\) points.
2. The small primes can be split so both products are \(O((\log N)^{-1/2})\).
3. This gives two disjoint covers of length \(\gg N/\sqrt{\log N}\).
4. Cleanup by primes in \((N/2,N]\) has an exact rainbow-matching characterization and capacity at most twice the number of primes.
5. A sieve restricted to \(p\le O(\log N)\), followed by terminal cleanup, is rigorously impossible.
6. A color receiving only primes above \(N^\alpha\) cannot cover when \(\alpha>e^{-1}\).

**Plausible but unproved.**

- Medium primes may create highly nonrandom concentration on the residual sets and beat the multiplicative density estimate.
- A two-reservoir Erdős–Rankin theorem robust under positive-density thinning of every prime scale would likely solve the problem.
- An asymmetric allocation with one color using very small primes and the other using primes above \(N^\alpha\), with \(\alpha\le e^{-1}\), remains conceivable but requires a new finite covering theorem for large moduli.

**Dead ends.**

- Balanced greedy sieving plus singleton cleanup stops at \(N/\sqrt{\log N}\).
- Pairing with terminal primes changes capacity by at most a factor of two.
- Tiny-prime sieving followed directly by terminal cleanup is impossible by uniform inclusion-exclusion.
- The simple split “small primes versus primes \(>\sqrt N\)” fails even the total-capacity condition.

**Precise block.** Route 3 now requires a theorem showing that medium-prime residue classes can simultaneously reduce two complementary residual sets to total size \(O(N/\log N)\), despite their multiplicative-density scale being \(N/\sqrt{\log N}\). Establishing this is comparable in difficulty to the original problem, so the route is blocked rather than solved. A fresh attempt should focus either on a robust two-reservoir Erdős–Rankin construction or on exact computation of the structured two-sieve optimization above, especially the occupancy of residual sets by medium-prime arithmetic progressions.