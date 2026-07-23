STATUS: BLOCKED

## Result

I obtained sharp extension criteria for Route 4, both when old residue classes are frozen and when only the old prime factors are retained while the shifts may be reoptimized. The key invariant is not the ordinary Jacobsthal gap \(R(N)\), but a hierarchy \(J_r(N)\) measuring intervals containing at most \(r\) integers coprime to \(N\). Adding \(r\) new primes can always absorb \(r\) such survivors, and—when the target interval is no longer than the new primes—this criterion is exact. For a frozen two-color extension from \(m\) to \(M\le 2m\), extension is possible exactly when the combined number of old-color misses in the tail is at most the number of new primes. These results show that the hoped-for generic recursive extension theorem does not follow from the existence of two length-\(m\) gaps: large new primes can increase \(R\) by only a bounded amount, and extending across a prime gap requires an exceptionally sparse survivor interval for each color. Establishing such intervals simultaneously for complementary prime products is essentially the original two-reservoir problem, so Route 4 is blocked rather than completed.

## Complete Argument

Throughout, the stronger all-real interpretation is targeted. Thus at integer cutoff \(m\), each factor must satisfy \(R(N)\ge m\), equivalently \(j(N)\ge m+1\).

### 1. Changing representatives gives freedom only at new primes

Let \(N\ge 1\), let \(t\) be an old CRT shift modulo \(N\), and let \(T\) be a finite set of primes not dividing \(N\).

**Lemma 1.** For arbitrary residues \(b_p\pmod p\), \(p\in T\), there exists \(t'\) such that
\[
t'\equiv t\pmod N,\qquad t'\equiv b_p\pmod p\quad(p\in T).
\]
Moreover,
\[
\gcd(t'+n,N)=\gcd(t+n,N)
\]
for every integer \(n\).

**Proof.** The moduli \(N\) and \(p\in T\) are pairwise coprime, so the first assertion is the Chinese remainder theorem. The congruence \(t'\equiv t\pmod N\) gives \(t'+n\equiv t+n\pmod N\), proving the second assertion. ∎

Thus choosing another representative of an old shift does permit arbitrary choices at newly introduced primes, but it does not change which tail positions are missed by the old primes. There is no additional hidden freedom.

---

### 2. Exact extension criterion when old residue classes are frozen

Suppose classes for all primes up to \(m\) have been fixed and partitioned into two nonempty colors \(A,B\), and both colors cover \([m]\). Let \(m<M\le 2m\). For \(C\in\{A,B\}\), define
\[
U_C=\{n\in\{m+1,\ldots,M\}:n\text{ is not covered by an old prime of color }C\}.
\]
Let
\[
\mathcal N=\{p:m<p\le M,\ p\text{ prime}\}.
\]

**Theorem 2 (exact frozen-tail extension).** Keeping all old colors and residue classes fixed, the assignment can be extended to all primes up to \(M\), with both colors covering \([M]\), if and only if
\[
|U_A|+|U_B|\le |\mathcal N|.
\]

**Proof.**

For every \(p\in\mathcal N\), one has \(p>m\). The tail has length \(M-m\le m<p\). Therefore a single residue class modulo \(p\) contains at most one point of the tail.

Each labeled miss \((C,n)\), where \(n\in U_C\), must consequently be covered by a distinct new prime assigned color \(C\). A new prime has only one color and can hit at most one tail point, proving necessity.

Conversely, suppose the inequality holds. Inject the disjoint union
\[
(\{A\}\times U_A)\sqcup(\{B\}\times U_B)
\]
into \(\mathcal N\). If \((C,n)\) is assigned to \(p\), color \(p\) by \(C\) and choose the residue \(n\pmod p\). Assign all remaining new primes arbitrarily. The old interval remains covered, and every old tail miss is covered by its assigned new prime. ∎

Two immediate consequences are worth isolating.

**Corollary 2.1.** To extend frozen classes from \(m\) to \(m+1\):

- if \(m+1\) is composite, the old classes of both colors must already cover \(m+1\);
- if \(m+1\) is prime, at least one old color must already cover \(m+1\).

Indeed, there are respectively zero or one new primes.

**Corollary 2.2.** Let \(p\) be prime and \(q\) the next prime. Suppose residue classes using primes below \(p\) are frozen and cover \([p-1]\). Extending through \([q-1]\) after adding the single prime \(p\) is possible if and only if
\[
|U_A|+|U_B|\le 1
\]
on the tail \(\{p,\ldots,q-1\}\).

Bertrand’s postulate gives \(q<2p\), hence \(q-1\le 2(p-1)\), so Theorem 2 applies.

This is a stringent obstruction: throughout the whole next prime gap, the old classes must already give both colors except for at most one labeled miss in total.

---

### 3. Generalized Jacobsthal profiles

Let
\[
\cdots<z_{-1}<z_0<z_1<\cdots
\]
be the increasing bi-infinite sequence of integers coprime to \(N\). Define, for \(r\ge 0\),
\[
J_r(N):=\max_i\bigl(z_{i+r+1}-z_i-1\bigr).
\]
The sequence is periodic modulo \(N\), so the maximum may be taken over any \(\varphi(N)\) consecutive indices.

Thus
\[
J_0(N)=R(N).
\]

The interpretation of \(J_r\) is exact.

**Lemma 3.** For \(L\ge1\),
\[
J_r(N)\ge L
\]
if and only if there is an interval of \(L\) consecutive integers containing at most \(r\) integers coprime to \(N\).

**Proof.**

If \(J_r(N)\ge L\), the open interval
\[
(z_i,z_{i+r+1})
\]
for a maximizing \(i\) has length \(J_r(N)\) and contains exactly the \(r\) coprime integers
\[
z_{i+1},\ldots,z_{i+r}.
\]
Any \(L\)-point subinterval has at most those \(r\) coprime integers.

Conversely, let \(I=\{a+1,\ldots,a+L\}\) contain \(s\le r\) integers coprime to \(N\). Let \(z_i\) be the largest coprime integer at most \(a\). The first coprime integer after \(I\) is then \(z_{i+s+1}\), so
\[
z_{i+s+1}-z_i-1\ge L.
\]
Since \(r\ge s\),
\[
z_{i+r+1}-z_i-1\ge z_{i+s+1}-z_i-1\ge L.
\]
Therefore \(J_r(N)\ge L\). ∎

---

### 4. Exact absorption theorem for new prime factors

Let \(T\) be a finite set of primes not dividing \(N\), and put
\[
P_T=\prod_{p\in T}p.
\]

**Theorem 4 (general residual absorption criterion).** One has
\[
R(NP_T)\ge L
\]
if and only if there is an interval \(I\) of \(L\) consecutive integers such that its \(N\)-coprime elements can be labeled by primes in \(T\) with the following property:

> For each \(p\in T\), all elements labeled \(p\) are congruent to one another modulo \(p\).

Labels need not all be used.

**Proof.**

Suppose first that \(R(NP_T)\ge L\), witnessed by an interval \(I\). Every \(x\in I\) coprime to \(N\) must be divisible by some \(p\in T\). Label \(x\) by one such \(p\). All elements labeled \(p\) are divisible by \(p\), hence congruent modulo \(p\).

Conversely, suppose such an interval \(I\) and labeling are given. For each used \(p\), let \(r_p\pmod p\) be the common residue of the elements labeled \(p\). Since \(N\) is invertible modulo every \(p\in T\), the CRT gives an integer \(K\) such that
\[
KN\equiv-r_p\pmod p
\]
for every used \(p\). Translate \(I\) by \(KN\).

If \(x\in I\) is not coprime to \(N\), then \(x+KN\equiv x\pmod N\), so it remains noncoprime to \(N\). If \(x\) was labeled \(p\), then
\[
x+KN\equiv r_p-r_p\equiv0\pmod p.
\]
Thus every translated point has a divisor in \(N P_T\), giving a run of length \(L\). ∎

When the new primes are at least as large as the target interval, this becomes a purely numerical criterion.

**Theorem 5 (exact singleton absorption).** Let \(|T|=r\) and suppose
\[
L\le\min_{p\in T}p.
\]
Then
\[
R(NP_T)\ge L
\quad\Longleftrightarrow\quad
J_r(N)\ge L.
\]

**Proof.**

In an interval of \(L\) consecutive integers, a single residue class modulo any \(p\ge L\) contains at most one point. Thus the labeling in Theorem 4 exists exactly when the interval contains at most \(r\) integers coprime to \(N\). Apply Lemma 3. ∎

There are two useful corollaries.

**Corollary 5.1.** Without any size condition on \(T\),
\[
R(NP_T)\ge J_r(N),\qquad r=|T|.
\]

**Proof.** The open interval between \(z_i\) and \(z_{i+r+1}\) contains exactly \(r\) \(N\)-coprime integers. Assign them injectively to the \(r\) primes of \(T\) and use the CRT construction in Theorem 4. ∎

**Corollary 5.2.** If
\[
J_r(N)<\min_{p\in T}p,
\]
then
\[
R(NP_T)=J_r(N).
\]

**Proof.** Corollary 5.1 gives the lower bound. If \(R(NP_T)\ge J_r(N)+1\), then Theorem 5, applied with \(L=J_r(N)+1\), would imply
\[
J_r(N)\ge J_r(N)+1,
\]
a contradiction. ∎

For one new prime this says:

\[
R(Np)\ge p
\quad\Longleftrightarrow\quad
J_1(N)\ge p.
\]

More generally, Theorem 4 gives the exact statement
\[
R(Np)\ge L
\]
if and only if there is an \(L\)-term interval in which all \(N\)-coprime elements are congruent modulo \(p\). If \(L\le 2p\), there can be at most two such elements; if there are two, they must differ by exactly \(p\).

---

### 5. Large new primes need not give large extensions

Let \(d_i=z_{i+1}-z_i\) be the cyclic gaps between reduced residues modulo \(N\). Then
\[
R(N)=\max_i d_i-1
\]
and
\[
J_1(N)=\max_i(d_i+d_{i+1}-1).
\]

Consequently,
\[
J_1(N)\ge R(N)+1.
\]
If \(2\mid N\), all reduced residues are odd, so every \(d_i\ge2\), and hence
\[
J_1(N)\ge R(N)+2.
\]

These universal increments are sharp in scale.

- For \(N=2\), all reduced-residue gaps are \(2\), so
  \[
  R(2)=1,\qquad J_1(2)=3.
  \]
  Therefore, for every prime \(p>3\),
  \[
  R(2p)=3.
  \]

- For \(N=3\), the reduced-residue gaps alternate between \(1\) and \(2\), so
  \[
  R(3)=1,\qquad J_1(3)=2.
  \]
  Therefore, for every prime \(p>3\),
  \[
  R(3p)=2.
  \]

- For \(N=6\), the gaps alternate between \(4\) and \(2\), so
  \[
  R(6)=3,\qquad J_1(6)=5.
  \]
  Therefore, for every prime \(p>5\),
  \[
  R(6p)=5<2R(6)+1.
  \]

Thus neither the magnitude of the newly added prime nor the old value \(R(N)\) alone controls the new gap. In particular, a universal doubling or prime-sized extension lemma is false.

The difference between \(N=2\) and \(N=3\) also shows that even products with the same old Jacobsthal value can behave differently after adjoining the same arbitrarily large prime. The adjacent-gap profile is essential.

---

### 6. Consequence for a nested factorization induction

Suppose a Route 4 construction fixes a global coloring of primes, so the two factors grow by adjoining each new prime to one side. Shifts may be reoptimized at every stage.

Let \(q\) be a new prime, and suppose immediately before adjoining \(q\) the factors are \(N_A,N_B\). If \(q\) is assigned to \(A\), then the all-real target at \(q\) is exactly
\[
R(N_Aq)\ge q,\qquad R(N_B)\ge q.
\]
By Theorem 5, the first condition is equivalent to
\[
J_1(N_A)\ge q.
\]
Hence the exact prime-step condition is
\[
J_1(N_A)\ge q,\qquad R(N_B)\ge q.
\]

If both old factors already satisfy \(R\ge q-1\), then \(J_1\ge R+1\ge q\). Thus the receiving factor can always be raised by the one needed point. The nonreceiving factor, however, must already have one point of slack.

The more serious issue is the composite interval following \(q\). Let \(q'\) be the next prime. Since no factors change for
\[
q\le m<q',
\]
a fixed nested partition must already satisfy
\[
R(N_Aq)\ge q'-1,\qquad R(N_B)\ge q'-1.
\]
The inactive factor must have anticipated the entire next prime gap. For the receiving factor, Theorem 4 says that \(N_A\) must have an interval of length \(q'-1\) whose \(N_A\)-coprime elements all lie in one residue class modulo \(q\). Since \(q'<2q\), there are at most two such survivors, and if there are two they differ by exactly \(q\).

There is no implication of this strength from merely
\[
R(N_A)\ge q-1.
\]
This is the precise point at which the recursive argument requires a new sparse-survivor theorem.

---

### 7. Why averaging cannot supply the missing sparse windows

The gap distances satisfy
\[
\sum_{i=1}^{\varphi(N)}d_i=N.
\]
Averaging all sums of \(r+1\) consecutive gaps gives
\[
J_r(N)\ge
\left\lceil (r+1)\frac{N}{\varphi(N)}\right\rceil-1.
\]

This is rigorous but quantitatively inadequate for two complementary factors. Let
\[
D_C=\frac{N_C}{\varphi(N_C)}.
\]
For disjoint base products using primes up to \(m\),
\[
D_A D_B\le \prod_{p\le m}\left(1-\frac1p\right)^{-1}\ll\log m.
\]
Trying to make the mean-spacing bound itself reach \(m\) would require approximately
\[
r_A+1>\frac{m}{D_A},\qquad
r_B+1>\frac{m}{D_B}.
\]
Therefore
\[
r_A+r_B+2
>
m\left(\frac1{D_A}+\frac1{D_B}\right)
\ge
\frac{2m}{\sqrt{D_AD_B}}
\gg \frac{m}{\sqrt{\log m}}.
\]
But only
\[
\pi(m)\asymp\frac{m}{\log m}
\]
primes are available in total. Hence a proof using only average reduced-residue spacing misses by a factor of order \(\sqrt{\log m}\).

One must prove that both complementary products possess intervals with far fewer coprime survivors than their mean density predicts. That is precisely the nonrandom sparse-window phenomenon underlying the original problem.

---

### 8. Ledger

**Proved lemmas**

1. Changing an old CRT representative preserves the complete old coverage pattern while allowing arbitrary congruences at new primes.
2. For frozen old classes and \(M\le2m\), extension is possible exactly when
   \[
   |U_A|+|U_B|\le\pi(M)-\pi(m).
   \]
3. \(J_r(N)\ge L\) exactly characterizes an \(L\)-interval with at most \(r\) \(N\)-coprime points.
4. The general residual absorption criterion, Theorem 4.
5. When \(L\le\min T\),
   \[
   R(NP_T)\ge L\iff J_{|T|}(N)\ge L.
   \]
6. If \(J_r(N)<\min T\), then
   \[
   R(NP_T)=J_r(N).
   \]
7. Exact nested prime-step condition:
   \[
   q\text{ assigned to }A
   \quad\Longrightarrow\quad
   J_1(N_A)\ge q,\ R(N_B)\ge q.
   \]

**Plausible but unproved claims**

1. Optimized complementary products may have generalized gaps \(J_r\) much larger than the mean-spacing bound.
2. A carefully chosen nested factorization might maintain enough look-ahead slack across all prime gaps.
3. Modern Erdős–Rankin sparse-survivor technology might be adaptable to prove the required simultaneous \(J_r\) bounds.

All three are currently unsupported at the needed quantitative level.

**Dead ends**

1. **Using different representatives of the old shifts to alter the tail:** false; Lemma 1 shows the old coverage pattern is unchanged.
2. **A large new prime automatically creates a long extension:** false; for every prime \(p>3\),
   \[
   R(3p)=2.
   \]
3. **A universal doubling inequality:** false; for every prime \(p>5\),
   \[
   R(6p)=5<2R(6)+1.
   \]
4. **Induction based only on \(R(N)\):** insufficient; adjoining a prime is controlled by \(J_1(N)\), and extension across the following prime gap requires an even more structured survivor set.
5. **Mean-gap cleanup:** quantitatively short by a factor \(\sqrt{\log m}\).

## Self-Audit

1. **The most delicate proof is Theorem 4, especially the use of one common translation.** It holds because for each new prime \(p\), the desired condition is a single congruence for the common coefficient \(K\), namely \(KN\equiv-r_p\pmod p\); these congruences are compatible by CRT. Translation by \(KN\) simultaneously preserves every divisibility relation modulo \(N\).

2. **The frozen-tail criterion applies only when old colors and residues are genuinely frozen and all remaining resources are new primes.** It does not obstruct the original problem, where old primes may be recolored and their classes redesigned for each \(m\). I believe the theorem itself is exact because the tail length is strictly smaller than every new prime, forcing one new prime per labeled old miss.

3. **The route diagnosis is not an impossibility theorem for every conceivable recursive construction.** It proves that the natural extension inputs \(R(N_A),R(N_B)\) are insufficient and reduces successful extension to simultaneous exceptional \(J_r\)-type gaps. A stronger structural invariant or a nonnested reoptimization could still solve the problem; no claim to the contrary is made.

## Computations To Verify

The following code computes \(J_r(N)\) exactly by enumerating one wheel period and checks Theorem 5 on small cases.

```python
from math import gcd, prod
from itertools import combinations, product
from functools import lru_cache

def primes_upto(n):
    out = []
    for x in range(2, n + 1):
        if all(x % p for p in out if p * p <= x):
            out.append(x)
    return out

@lru_cache(None)
def wheel_J(N, r):
    """
    J_r(N) = max_i (z_{i+r+1} - z_i - 1),
    where z_i are the integers coprime to N.
    Exact, but period enumeration is practical only for small N.
    """
    if N == 1:
        return r  # all integers are coprime

    rr = [a for a in range(N) if gcd(a, N) == 1]
    h = len(rr)

    # Enough periodic extension for i=0,...,h-1.
    ext = []
    for k in range(h + r + 1):
        cycles, idx = divmod(k, h)
        ext.append(rr[idx] + cycles * N)

    return max(ext[i + r + 1] - ext[i] - 1 for i in range(h))

def R(N):
    return wheel_J(N, 0)

# Basic exact examples from the argument.
assert R(2) == 1 and wheel_J(2, 1) == 3
assert R(3) == 1 and wheel_J(3, 1) == 2
assert R(6) == 3 and wheel_J(6, 1) == 5

for p in primes_upto(100):
    if p > 3:
        assert R(2 * p) == 3
        assert R(3 * p) == 2
    if p > 5:
        assert R(6 * p) == 5

# Exhaustive verification of Theorem 5 on modest inputs.
test_primes = primes_upto(13)

for N in range(2, 31):
    candidates = [p for p in test_primes if N % p != 0]
    for r in (1, 2):
        for T in combinations(candidates, r):
            P = prod(T)
            jr = wheel_J(N, r)
            rt = R(N * P)

            for L in range(1, min(T) + 1):
                assert (rt >= L) == (jr >= L)

            if jr < min(T):
                assert rt == jr

print("All generalized-gap checks passed.")
```

A checker and constructor for the frozen-tail theorem:

```python
def check_cover(L, witness):
    """
    witness[p] = ('A' or 'B', residue modulo p)
    """
    for n in range(1, L + 1):
        for color in ('A', 'B'):
            if not any(c == color and n % p == a
                       for p, (c, a) in witness.items()):
                return False
    return True

def extend_frozen(m, M, witness):
    """
    Returns an extension if Theorem 2's condition holds,
    otherwise returns None.
    Assumes witness contains every prime <= m and covers [m].
    """
    assert m < M <= 2 * m
    assert check_cover(m, witness)

    old_primes = primes_upto(m)
    assert set(witness) == set(old_primes)

    new_primes = [p for p in primes_upto(M) if p > m]
    demands = []

    for n in range(m + 1, M + 1):
        for color in ('A', 'B'):
            old_hit = any(
                c == color and n % p == a
                for p, (c, a) in witness.items()
            )
            if not old_hit:
                demands.append((color, n))

    if len(demands) > len(new_primes):
        return None

    ans = dict(witness)

    for p, (color, n) in zip(new_primes, demands):
        ans[p] = (color, n % p)

    for p in new_primes[len(demands):]:
        ans[p] = ('A', 0)

    assert check_cover(M, ans)
    return ans
```

For small cutoffs, this enumerates globally nested prime colorings while allowing fresh shifts at each stage. It directly tests the more flexible factor-nested version of Route 4.

```python
def nested_factor_chains(M, lower=2):
    """
    Global color of each prime is fixed.
    At every m, shifts may be reoptimized, so the test is via R.
    Practical only for very small M because wheel periods grow rapidly.
    """
    ps = primes_upto(M)
    good = []

    for bits in product((0, 1), repeat=len(ps)):
        ok = True

        for m in range(lower, M + 1):
            A = [p for p, b in zip(ps, bits) if b == 0 and p <= m]
            B = [p for p, b in zip(ps, bits) if b == 1 and p <= m]

            if not A or not B:
                ok = False
                break

            NA, NB = prod(A), prod(B)
            if R(NA) < m or R(NB) < m:
                ok = False
                break

        if ok:
            good.append(dict(zip(ps, bits)))

    return good

# Suggested small runs:
for M in range(5, 14):
    chains = nested_factor_chains(M, lower=5)
    print(M, len(chains))
```

To test the stricter frozen-residue recursion with a SAT solver, use variables
\[
y_{p,c,r}
\]
with exactly one choice for each prime \(p\le M\), and impose for every stage \(m\), every \(n\le m\), and both colors \(c\),
```text
OR(y[p,c,n mod p] for prime p <= m).
```
Unlike the ordinary single-\(m\) SAT encoding, imposing these clauses simultaneously for all stages tests whether one fixed coloring and one fixed residue per prime can form a recursive chain.

## Route Diagnosis

The CRT component of Route 4 works cleanly: new prime residues can be prescribed independently while preserving an old shift modulo the old product. What fails is the expected extension mechanism. With frozen classes, the exact tail criterion demands that old classes already cover almost the whole new tail in both colors. With reoptimized shifts, adjoining new primes is governed by generalized gaps \(J_r(N)\), not merely by the old Jacobsthal gap. Large primes do not intrinsically create large slack, and average reduced-residue spacing is far too weak.

The route is therefore blocked at the following precise statement: one would need, for complementary prime products, simultaneous intervals of length about \(m\) containing only as many coprime survivors as can be absorbed by disjoint reservoirs of remaining primes, with additional congruence structure when one new prime must absorb multiple survivors. Proving that is a two-channel sparse-sieve theorem of comparable strength to the original problem.

A fresh attempt should computationally optimize and record the full profiles \(J_r(N_A),J_r(N_B)\), not only \(R(N_A),R(N_B)\), and determine whether globally nested colorings survive beyond small cutoffs. If they do not, Route 4 should be abandoned in favor of a nonnested two-reservoir Erdős–Rankin construction that permits recoloring and complete reoptimization at each prime cutoff.