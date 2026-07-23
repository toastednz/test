STATUS: BLOCKED

## Result

I did not resolve whether every \(\omega\)-order on \(\mathbb Z\) contains a monotone four-term arithmetic progression. I proved several structural lemmas relevant to Route 3. Most importantly: (i) any hypothetical counterexample can be normalized, by passing to an affine sublattice, so that \(0\) and \(1\) are its first two elements; (ii) the first two elements of every affine sublattice force a specific later inversion; and (iii) constraints coming only from progressions containing the least element cannot prove the theorem—I construct an explicit order of type \(\omega\) satisfying all of those constraints. A two-anchor six-point configuration gives a genuine additional forcing rule, but I could not iterate it to force infinitely many predecessors below one fixed element. Thus Route 3 is blocked precisely at predecessor amplification across overlapping affine sublattices.

## Complete Argument

### 1. Order-type reformulation

Let \(\prec\) be a total order on \(\mathbb Z\), and write
\[
D_\prec(x):=\{y\in\mathbb Z:y\prec x\}.
\]

#### Lemma 1
A total order \(\prec\) on \(\mathbb Z\) is induced by a one-sided permutation
\[
\pi:\mathbb N_0\to\mathbb Z
\]
if and only if every \(D_\prec(x)\) is finite.

#### Proof

If \(\prec\) is induced by \(\pi\), then
\[
D_\prec(x)=\{\pi(0),\ldots,\pi(p_\pi(x)-1)\},
\]
so it is finite.

Conversely, suppose every \(D_\prec(x)\) is finite. Define
\[
r(x):=\#D_\prec(x).
\]
If \(x\prec y\), then
\[
D_\prec(x)\subsetneq D_\prec(y),
\]
so \(r(x)<r(y)\). Hence \(r\) is injective.

If \(r(x)=m\), then the finite totally ordered set \(D_\prec(x)\) has \(m\) elements. Listed increasingly, its elements have respectively \(0,1,\ldots,m-1\) predecessors in the full order. Thus whenever \(m\) lies in the range of \(r\), so do all integers \(0,\ldots,m-1\).

Since \(\mathbb Z\) is infinite and \(r\) is injective, its range is unbounded. Therefore its range is all of \(\mathbb N_0\). The unique element \(x_n\) satisfying \(r(x_n)=n\) gives an enumeration
\[
x_0\prec x_1\prec x_2\prec\cdots
\]
of \(\mathbb Z\). Hence the order has type \(\omega\). ∎

Thus Route 3 asks us to prove that every four-AP-avoiding total order has an infinite predecessor set.

For an \(\omega\)-order, the rank function
\[
p(x):=\#D_\prec(x)
\]
is proper in the sense that
\[
|x|\to\infty\quad\Longrightarrow\quad p(x)\to\infty.
\]
Indeed, for each \(M\), only \(M+1\) integers can have rank at most \(M\).

---

### 2. Normalizing the first two elements

An important strengthening of “put the first element at \(0\)” is available.

#### Lemma 2
If a four-AP-avoiding order of type \(\omega\) on \(\mathbb Z\) exists, then one exists whose first two elements are \(0\) and \(1\), in that order.

#### Proof

Let \(a\) and \(b\) be the first and second elements of a hypothetical avoiding order, and put
\[
h=b-a\ne0.
\]
Consider the affine sublattice
\[
L=a+h\mathbb Z.
\]
The order induced on \(L\) has type \(\omega\): every element of \(L\) still has only finitely many predecessors in \(L\). Its first two elements are \(a,b\), because no element of the full order other than \(a\) precedes \(b\).

Pull this order back to \(\mathbb Z\) through
\[
\phi(n)=a+hn.
\]
If \(h>0\), \(\phi\) preserves numerical orientations of arithmetic progressions. If \(h<0\), it reverses them, but monotonicity in either orientation is part of the forbidden condition. Thus the pullback remains four-AP-avoiding. Its first two elements are \(0,1\). ∎

In particular, any hypothetical counterexample has a normalized restriction satisfying
\[
0\prec1.
\]

#### Corollary 3
In such a normalized order,
\[
0\prec1\prec3\prec2.
\]

#### Proof

Both \(2\) and \(3\) occur after \(1\). If \(2\prec3\), then
\[
0\prec1\prec2\prec3
\]
would be a monotone four-term progression. Therefore \(3\prec2\). ∎

This already forces three predecessors below \(2\), but I found no valid way to force infinitely many.

---

### 3. First-two extrapolation in every affine sublattice

The normalization argument applies internally to every affine sublattice.

#### Lemma 4: first-two extrapolation
Let \(\prec\) be a four-AP-avoiding order of type \(\omega\), and let
\[
L=u+q\mathbb Z,\qquad q\ne0.
\]
Let \(r\) and \(s\) be the first and second elements of \(L\) under \(\prec\), and put
\[
\delta=s-r.
\]
Then
\[
r\prec s\prec r+3\delta\prec r+2\delta.
\]

#### Proof

The four distinct values
\[
r,\quad r+\delta=s,\quad r+2\delta,\quad r+3\delta
\]
all belong to \(L\). Since \(r,s\) are the first two elements of \(L\), both \(r+2\delta\) and \(r+3\delta\) occur after \(s\).

If
\[
r+2\delta\prec r+3\delta,
\]
then
\[
r\prec r+\delta\prec r+2\delta\prec r+3\delta.
\]
If \(\delta>0\), this is a numerically increasing four-term AP in occurrence order. If \(\delta<0\), it is the same AP in numerically decreasing order. Both are forbidden. Therefore
\[
r+3\delta\prec r+2\delta.
\]
The remaining displayed inequalities follow from \(r,s\) being the first two elements of \(L\). ∎

This is a genuine recursive constraint: every affine sublattice begins, relative to the gap between its first two elements, with the pattern
\[
0,\ 1,\ 3,\ 2.
\]

The obstruction is that the forced edge
\[
r+3\delta\prec r+2\delta
\]
does not feed into another first-two configuration. In the lattice generated by those two points, the old points \(r,s\) are already earlier, so the same lemma cannot simply be reapplied to continue a descending chain.

---

### 4. Why the least-element constraints alone are insufficient

For the elementary three-term theorem, APs containing the least element already force an infinite descent. That strategy fails decisively at length four.

#### Lemma 5
There is an explicit order of type \(\omega\) on \(\mathbb Z\), with least element \(0\), such that no four-term AP containing \(0\) is monotone.

#### Construction

Every nonzero integer has a unique representation
\[
x=s2^i3^j,
\]
where \(i,j\ge0\) and \(s\ne0\) is relatively prime to \(6\). For each such \(s\) and each \(n\ge0\), define the finite chain
\[
C_{s,n}:=
\bigl(s3^n,\ s2\cdot3^{n-1},\ldots,s2^n\bigr).
\]
Thus the entries are indexed by \(i=0,\ldots,n\):
\[
s2^i3^{n-i}.
\]

Order the pairs \((s,n)\) first by increasing \(|s|+n\), with any fixed finite tie-breaking rule, and list the finite blocks \(C_{s,n}\) in that order. Put \(0\) before every block.

This is a one-sided enumeration: every block is finite, only finitely many pairs precede any given pair, and the unique factorization above shows that every nonzero integer appears exactly once.

For every \(x=s2^i3^j\), the numbers \(3x\) and \(2x\) lie in the same block \(C_{s,i+j+1}\). Within that block, \(3x\) has \(2\)-adic exponent \(i\), while \(2x\) has exponent \(i+1\). Hence
\[
3x\prec2x. \tag{1}
\]

Now consider a four-term AP containing \(0\).

- If \(0\) is one of its two interior terms, its rank is the minimum rank at an interior position. A strictly monotone rank sequence has its minimum at an endpoint, so the AP cannot be monotone.
- If \(0\) is a numerical endpoint, the progression can be written, in one of its numerical orientations, as
  \[
  0,x,2x,3x.
  \]
  Since \(0\) is the least order element, the only possible monotone occurrence would require
  \[
  0\prec x\prec2x\prec3x,
  \]
  contradicting (1).

Thus every four-AP containing \(0\) is nonmonotone. ∎

This construction is not a counterexample to the full problem. For the indicated ordering of blocks,
\[
1\prec3\prec5\prec7,
\]
so \(1,3,5,7\) is a monotone four-term AP.

Nevertheless, Lemma 5 proves that any argument using only progressions through the global least element is incapable of resolving the problem. Translated and overlapping APs are essential.

---

### 5. A model of the desired non-\(\omega\) obstruction

There are simple avoiding total orders with a least element, but their non-\(\omega\) character is visible through infinitely many predecessors.

#### Lemma 6
There is a total order on \(\mathbb Z\) with least element \(0\) that avoids even monotone three-term APs, and every nonzero element has infinitely many predecessors.

#### Proof

Write the \(2\)-adic binary digits of \(n\in\mathbb Z\) as
\[
b_0(n),b_1(n),\ldots,\qquad b_i(n)\in\{0,1\},
\]
where \(b_i(n)\) is determined by \(n\bmod 2^{i+1}\). Order integers lexicographically from the least significant digit: for \(m\ne n\), let
\[
t=v_2(m-n),
\]
the first digit at which they differ, and declare
\[
m\prec_2 n
\quad\Longleftrightarrow\quad
b_t(m)=0,\ b_t(n)=1.
\]
This is the restriction of lexicographic order on binary sequences, hence is a total order.

For \(n\ne0\), let \(t=v_2(n)\). The digits of \(0\) and \(n\) agree below \(t\), while
\[
b_t(0)=0,\qquad b_t(n)=1.
\]
Thus \(0\prec_2n\), so \(0\) is least.

Consider a three-term AP
\[
a,\ a+d,\ a+2d
\]
and put \(t=v_2(d)\). The endpoints \(a,a+2d\) have the same digit at position \(t\), while \(a+d\) has the opposite digit. At all lower positions the three integers agree. Consequently, under \(\prec_2\), the middle term lies either before both endpoints or after both endpoints. It cannot lie between them. Hence the three terms are never monotone.

Finally, let \(n\ne0\), with \(t=v_2(n)\). For every \(k>t\), the integers \(2^k\) and \(n\) first differ at digit \(t\), where
\[
b_t(2^k)=0,\qquad b_t(n)=1.
\]
Therefore
\[
2^k\prec_2 n.
\]
The infinitely many integers \(2^k\), \(k>t\), are all predecessors of \(n\). ∎

This is exactly the kind of obstruction Route 3 seeks to force for four-AP-avoiding orders. The missing step is to prove that every such order must behave similarly.

---

### 6. A genuine two-anchor forcing configuration

Constraints from two early numerical endpoints interact more strongly than those from one.

#### Lemma 7: six-point forcing
Let
\[
x_i=a+id,\qquad 0\le i\le5,\quad d>0.
\]
Suppose a four-AP-avoiding order satisfies
\[
x_0\prec x_i,\qquad x_5\prec x_i
\quad(1\le i\le4).
\]
Then
\[
x_2\prec x_1
\quad\text{or}\quad
x_3\prec x_4. \tag{2}
\]

#### Proof

From the AP
\[
x_0,x_1,x_2,x_3
\]
and the fact that \(x_0\) precedes the other three, avoidance gives
\[
x_2\prec x_1
\quad\text{or}\quad
x_3\prec x_2. \tag{3}
\]

From the AP
\[
x_2,x_3,x_4,x_5
\]
and the fact that \(x_5\) precedes the other three, avoidance of the reverse numerical order gives
\[
x_3\prec x_4
\quad\text{or}\quad
x_2\prec x_3. \tag{4}
\]

If neither alternative in (2) held, then \(x_1\prec x_2\) and \(x_4\prec x_3\). Equations (3) and (4) would then force both
\[
x_3\prec x_2
\quad\text{and}\quad
x_2\prec x_3,
\]
a contradiction. ∎

This rules out the simplest strategy of always satisfying an endpoint constraint by putting the term farther from the early endpoint before the nearer one. With early endpoints separated by \(5d\), the two resulting “outward” choices point in opposite directions along the central edge.

However, the surviving alternatives in (2) point toward different numerical endpoints:
\[
x_2\prec x_1
\quad\text{or}\quad
x_3\prec x_4.
\]
I found no mechanism forcing repeated applications to remain below one fixed order element.

---

### 7. Necessary oscillation on every large dyadic ray

The first-element descent argument does leave a rigorous trace.

#### Lemma 8
Let \(\prec\) be a four-AP-avoiding \(\omega\)-order with rank function \(p\). For every fixed \(x\in\mathbb Z\), there are infinitely many \(j\) such that
\[
p(x+2^j)<p(x+2^{j+1})
\]
and, for each sufficiently large such \(j\),
\[
p(x+3\cdot2^j)<p(x+2^{j+1}). \tag{5}
\]

#### Proof

Properness gives
\[
p(x+2^j)\to\infty.
\]
If only finitely many adjacent ascents occurred, then for all sufficiently large \(j\),
\[
p(x+2^{j+1})<p(x+2^j),
\]
producing an infinite strictly decreasing sequence of nonnegative integers. Hence there are infinitely many adjacent ascents.

For sufficiently large \(j\), all three values
\[
x+2^j,\quad x+2^{j+1},\quad x+3\cdot2^j
\]
occur after \(x\). If
\[
p(x+2^j)<p(x+2^{j+1}),
\]
then the first three terms of
\[
x,\quad x+2^j,\quad x+2^{j+1},\quad x+3\cdot2^j
\]
occur in increasing numerical order. Avoidance forces the fourth term to occur before the third, proving (5). ∎

The obstruction is again non-composability: the upper elements \(x+2^{j+1}\) vary with \(j\), so (5) does not give infinitely many predecessors of one fixed integer.

---

### 8. Ledger

#### Proved

1. An order on \(\mathbb Z\) is of type \(\omega\) exactly when every element has finitely many predecessors.
2. Any hypothetical counterexample has an affine restriction whose first two elements are \(0,1\).
3. The first two elements \(r,s\) of every affine sublattice force
   \[
   r+3(s-r)\prec r+2(s-r).
   \]
4. There is an explicit \(\omega\)-order satisfying every avoidance constraint coming from APs containing its least element.
5. The \(2\)-adic lexicographic order avoids monotone three-APs and illustrates the infinite-predecessor obstruction.
6. The six-point two-anchor forcing Lemma 7.
7. The dyadic-ray oscillation Lemma 8.

#### Plausible but unproved

The first-two extrapolation rules from all affine sublattices, supplemented by two-anchor rules such as Lemma 7, may force a composable descending chain. I do not have such an amplification theorem. In its present form, this is of comparable strength to the original Route 3 target and cannot be treated as a reduction.

#### Dead ends

1. **Using only APs through the least element:** disproved by Lemma 5.
2. **Always choosing the outward endpoint inversion:** incompatible for two early endpoints separated by five common-difference units, but the alternative inversions do not iterate.
3. **Iterating first-two extrapolation directly:** the forced pair lies in a lattice whose original first two elements are still earlier, so the hypothesis does not regenerate.
4. **Following dyadic ascents:** gives predecessors below moving targets, not a fixed target.
5. **Compactness from finite avoiding orders:** can produce orders like the \(2\)-adic order, but does not preserve finite predecessor sets.

## Self-Audit

1. **The central predecessor-amplification theorem is missing.**  
   This is not a complete solution, and I have marked the route BLOCKED rather than presenting the lemmas as sufficient. The individual forcing statements are proved directly, but none establishes an infinite down-set.

2. **Lemma 5 only blocks least-element-only arguments.**  
   It does not show Route 3 itself is hopeless, because translated APs and first elements of affine sublattices impose additional constraints. Its claimed scope is nevertheless exact: the constructed \(\omega\)-order satisfies every four-AP constraint involving its least element.

3. **The computational program below supplies searches, not verified large-scale results.**  
   No mathematical claim above depends on an unreported SAT run. The small order
   \[
   0,1,3,2,-1,-3,-2
   \]
   can be checked by hand to avoid all four-APs in \([-3,3]\), showing at least that the forced bound \(3\prec2\) does not immediately amplify on that finite set.

## Computations To Verify

The following Z3 code searches finite affine configurations with \(0,1\) designated first and second, and tests whether a fixed target is forced to have many predecessors.

```python
from z3 import *
from itertools import count

def four_aps(S):
    S = sorted(set(S))
    T = set(S)
    lo, hi = min(S), max(S)
    out = []
    for a in S:
        for d in range(1, (hi - lo) // 3 + 1):
            q = (a, a+d, a+2*d, a+3*d)
            if all(x in T for x in q):
                out.append(q)
    return out

def avoiding_solver(S, first_two=None):
    S = sorted(set(S))
    m = len(S)
    r = {x: Int(f"r_{x}") for x in S}
    sol = Solver()

    for x in S:
        sol.add(0 <= r[x], r[x] < m)
    sol.add(Distinct([r[x] for x in S]))

    for a, b, c, d in four_aps(S):
        sol.add(Not(And(r[a] < r[b], r[b] < r[c], r[c] < r[d])))
        sol.add(Not(And(r[a] > r[b], r[b] > r[c], r[c] > r[d])))

    if first_two is not None:
        u, v = first_two
        sol.add(r[u] == 0)
        sol.add(r[v] == 1)

    return sol, r

# Search for a bounded number of predecessors of a target.
def target_with_at_most(S, target, cap):
    sol, r = avoiding_solver(S, first_two=(0, 1))
    pred_count = Sum([
        If(r[y] < r[target], 1, 0)
        for y in S if y != target
    ])
    sol.add(pred_count <= cap)
    return sol, r

# Basic experiment: does the minimum number of predecessors of 2 grow?
for N in range(3, 31):
    S = list(range(-N, N+1))
    minimum = None
    witness = None
    for cap in range(len(S)):
        sol, r = target_with_at_most(S, 2, cap)
        if sol.check() == sat:
            minimum = cap
            model = sol.model()
            witness = sorted(S, key=lambda x: model[r[x]].as_long())
            break
    print("N =", N, "minimum predecessors of 2 =", minimum)
    print("initial witness terms:", witness[:20])
```

A fixed-target Route 3 certificate would be indicated if, for some target \(t\), the minimum predecessor count grew without bound as \(N\) increased. Stable bounded values would refute that particular amplification strategy, though not Route 3 itself.

The six-point lemma can be machine-checked as follows:

```python
S = list(range(6))
sol, r = avoiding_solver(S)

# Both endpoints precede all four interior points.
for i in range(1, 5):
    sol.add(r[0] < r[i])
    sol.add(r[5] < r[i])

# Negate the claimed conclusion:
# not (2 before 1), and not (3 before 4).
sol.add(r[1] < r[2])
sol.add(r[4] < r[3])

print(sol.check())  # Expected: unsat
```

The small finite witness mentioned in the audit can be checked directly:

```python
def check_word(word):
    pos = {x: i for i, x in enumerate(word)}
    assert len(pos) == len(word)
    S = set(word)
    bad = []
    for a, b, c, d in four_aps(S):
        q = [pos[a], pos[b], pos[c], pos[d]]
        if q[0] < q[1] < q[2] < q[3]:
            bad.append((a, b-a, "increasing"))
        if q[0] > q[1] > q[2] > q[3]:
            bad.append((a, b-a, "decreasing"))
    return bad

print(check_word([0, 1, 3, 2, -1, -3, -2]))  # Expected: []
```

A finite checker for the \(2\)-adic order is:

```python
def v2_nonzero(z):
    z = abs(z)
    return (z & -z).bit_length() - 1

def before_2adic(m, n):
    assert m != n
    t = v2_nonzero(m - n)
    bm = (m // (1 << t)) % 2
    bn = (n // (1 << t)) % 2
    return bm < bn

def check_2adic_three_aps(N):
    for a in range(-N, N+1):
        for d in range(1, N+1):
            q = (a, a+d, a+2*d)
            if not all(-N <= x <= N for x in q):
                continue
            inc = before_2adic(q[0], q[1]) and before_2adic(q[1], q[2])
            dec = before_2adic(q[2], q[1]) and before_2adic(q[1], q[0])
            if inc or dec:
                return q
    return None

print(check_2adic_three_aps(100))  # Expected: None
```

Finally, the endpoint-only \(\omega\)-order from Lemma 5 can be generated and stress-tested:

```python
from math import gcd

def endpoint_model_prefix(K):
    out = [0]
    W = 1
    while len(out) < K:
        # Enumerate pairs with |s| + n = W.
        for n in range(W):
            abs_s = W - n
            if gcd(abs_s, 6) != 1:
                continue
            for s in (abs_s, -abs_s):
                block = [s * (2**i) * (3**(n-i)) for i in range(n+1)]
                out.extend(block)
                if len(out) >= K:
                    return out[:K]
        W += 1
    return out

w = endpoint_model_prefix(10000)
print(check_word(w)[:10])  # Should eventually include (1, 2, "increasing")
```

## Route Diagnosis

Route 3 remains conceptually appropriate, but its simplest form is decisively blocked. The global least element gives only the constraints
\[
3x\prec2x
\]
as one consistent way to defeat all anchored progressions, and Lemma 5 realizes those constraints inside a genuine \(\omega\)-order. The stronger and genuinely relevant structure is that every affine sublattice has its own first two elements, forcing the local pattern \(0,1,3,2\). The unresolved issue is to make these local inversions compose below one fixed element. Two-anchor overlaps produce additional alternatives, but currently allow the forced edge to escape toward different targets.

A fresh attempt should therefore combine Route 3 with Route 6: use SAT/SMT on affine sets with \(0,1\) first, not merely to find unsatisfiability, but to minimize predecessor counts of fixed small targets and extract recursive implication certificates. Promising configurations are nested affine lattices together with six-point overlaps at scale factors \(2,3,5\). If every fixed target retains a bounded predecessor count in large instances, the search should instead look for a dynamically selected target or pivot to a priority construction; finite compactness by itself will only recover non-\(\omega\) orders such as the \(2\)-adic example.