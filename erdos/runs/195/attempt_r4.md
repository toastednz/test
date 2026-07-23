STATUS: BLOCKED

## Result

Route 4 produces very clean \(2\)-adic and \(3\)-adic total orders avoiding the required patterns, but these orders necessarily fail to have order type \(\omega\). I proved two broader obstructions: a natural “opposite sibling comparisons” relaxation still forces every integer to have infinitely many predecessors, and every construction obtained by concatenating rapidly growing finite annuli ordered internally by a binary residue hierarchy necessarily contains a monotone four-term AP. I also analyzed a genuinely fair self-similar residue interleaving and exhibited an explicit forbidden progression. Thus the standard convex residue-class, finite-shell truncation, and simplest fair substitution implementations of Route 4 are rigorously ruled out. I did not resolve whether a substantially nonconvex, state-dependent residue interleaving can work, so Erdős Problem #195 remains unsolved here.

## Complete Argument

### 1. \(p\)-adic lexicographic orders give the desired local avoidance

For a prime \(p\), write every integer \(x\) in its \(p\)-adic digit expansion
\[
x=\sum_{j\ge 0}\delta_j(x)p^j,\qquad \delta_j(x)\in\{0,\ldots,p-1\}.
\]
For negative integers this is the usual infinite \(p\)-adic expansion.

Fix, at every finite digit prefix, a total order of its \(p\) children. Define \(x\prec_p y\) by looking at the least index \(t\) for which
\[
\delta_t(x)\ne\delta_t(y)
\]
and comparing those two children in the prescribed order at their common lower-digit prefix.

This is a total order: it is simply lexicographic order on the \(p\)-adic digit strings, read from least significant to most significant digit. Every cylinder
\[
\{x:x\equiv r\pmod {p^t}\}
\]
is convex, and its \(p\) subclasses modulo \(p^{t+1}\) are convex subblocks.

#### Lemma 1: Every \(2\)-adic lexicographic order avoids monotone three-term APs.

Let
\[
x_0=a,\qquad x_1=a+d,\qquad x_2=a+2d,
\]
and put \(t=v_2(d)\). The three terms have the same digits below level \(t\). If
\[
u=d/2^t
\]
is odd and \(r=\delta_t(a)\), their level-\(t\) digits are
\[
r,\quad r+1,\quad r\pmod 2.
\]
Thus \(x_0,x_2\) lie in one child block and \(x_1\) lies in the other. Because the two child blocks are convex, \(x_1\) occurs either before both endpoints or after both endpoints. Hence
\[
x_0,x_1,x_2
\]
cannot be increasing or decreasing in \(\prec_2\). ∎

In particular, these orders avoid monotone four-term APs.

#### Lemma 2: Every \(3\)-adic lexicographic order avoids monotone four-term APs.

Let
\[
x_i=a+id,\qquad 0\le i\le3,
\]
and put \(t=v_3(d)\). With \(u=d/3^t\not\equiv0\pmod3\), the level-\(t\) digits are
\[
r,\quad r+u,\quad r+2u,\quad r\pmod3.
\]
The first three digits are the three distinct residue classes, while the first and last terms lie in the same child block.

If \(x_0\prec_3 x_1\prec_3 x_2\prec_3 x_3\), the sequence of child blocks would have to be nondecreasing in the child-block order. It starts and ends in the same block but visits two other blocks in between, which is impossible. The same argument with “nonincreasing” rules out the reverse order. ∎

Thus Route 4 has an ideal local rule: at the first \(p\)-adic scale where an AP splits, convex residue blocks destroy monotonicity.

---

### 2. The convex \(p\)-adic orders cannot be enumerations

#### Lemma 3: No \(p\)-adic lexicographic order above has order type \(\omega\).

At the top level, the \(p\) residue classes modulo \(p\) are nonempty, infinite, convex blocks. Choose any element in a block other than the first block. Every integer in the preceding block is a predecessor of that element. It therefore has infinitely many predecessors.

In an order induced by a permutation
\[
\pi:\mathbb N_0\to\mathbb Z,
\]
every integer has only finitely many predecessors, namely its position. Hence a \(p\)-adic lexicographic order cannot arise from a one-sided permutation. ∎

More generally, any total order in which two infinite sets form consecutive convex blocks fails to have order type \(\omega\).

This is the fundamental defect in the direct residue-class construction.

---

### 3. A natural weakening of convexity still cannot be fair

For a four-term AP
\[
a,\ a+d,\ a+2d,\ a+3d,
\]
one sufficient way to prevent monotonicity is to require that the comparisons of the two same-parity pairs
\[
(a,a+2d),\qquad (a+d,a+3d)
\]
have opposite orientations.

Formally, consider the condition
\[
a\prec a+2d
\quad\Longleftrightarrow\quad
a+3d\prec a+d
\tag{O}
\]
for every \(a\in\mathbb Z\) and \(d>0\).

#### Lemma 4: Condition (O) excludes every monotone four-term AP.

In an increasing occurrence order, both comparisons
\[
a\prec a+2d,\qquad a+d\prec a+3d
\]
hold. In a decreasing occurrence order, both fail. Condition (O) says that exactly one holds, so neither monotone orientation is possible. ∎

Unfortunately, this sufficient rule is itself incompatible with order type \(\omega\).

#### Lemma 5: Under condition (O), every integer has infinitely many predecessors.

Fix \(d>0\), put \(h=2d\), and define
\[
E(n)=
\begin{cases}
1,&n\prec n+h,\\
0,&n+h\prec n.
\end{cases}
\]
Condition (O) gives
\[
E(n+d)=1-E(n).
\]
Applying this again after translating by \(d\),
\[
E(n+h)=E(n+2d)=E(n).
\tag{1}
\]

Fix \(a\).

- If \(E(a)=1\), then by (1),
  \[
  E(a-kh)=1\qquad(k\ge1).
  \]
  Hence
  \[
  \cdots\prec a-3h\prec a-2h\prec a-h\prec a,
  \]
  so \(a\) has infinitely many predecessors.

- If \(E(a)=0\), then
  \[
  E(a+kh)=0\qquad(k\ge0),
  \]
  giving
  \[
  \cdots\prec a+3h\prec a+2h\prec a+h\prec a.
  \]
  Again \(a\) has infinitely many predecessors.

Thus every element has infinitely many predecessors. ∎

This rules out a broad natural attempt to retain only the pairwise comparisons supplied by the binary residue split. A successful construction must choose its witnessing inversions in a substantially more asymmetric and AP-dependent manner.

---

### 4. Finite-shell truncations of the binary hierarchy also fail

A standard way to repair the order-type problem is to replace infinite residue blocks by finite annuli, order each annulus \(2\)-adically, and concatenate the annuli in some fair order. The following theorem rules out this entire scheme when parity remains convex within each annulus.

Let
\[
1\le R_0<R_1<R_2<\cdots
\]
satisfy, for all sufficiently large \(m\),
\[
R_m>2R_{m-1},
\qquad
R_{m+1}\ge3R_m.
\tag{2}
\]
Define finite annuli
\[
S_0=[-R_0,R_0]\cap\mathbb Z,
\]
and, for \(m\ge1\),
\[
S_m=\{x\in\mathbb Z:R_{m-1}<|x|\le R_m\}.
\]

#### Theorem 6: There is no four-AP-avoiding \(\omega\)-order satisfying both:

1. every \(S_m\) is a convex block;
2. inside every \(S_m\), its even and odd elements are convex subblocks.

#### Proof

Because all shells are finite convex blocks in an \(\omega\)-order, their induced block order is itself of type \(\omega\). Let
\[
q(m)\in\mathbb N_0
\]
be the position of the block \(S_m\) among the shell blocks.

There are infinitely many \(m\) such that
\[
q(m)<q(m+1).
\tag{3}
\]
Indeed, otherwise \(q(m)>q(m+1)\) for all sufficiently large \(m\), yielding an infinite strictly decreasing sequence of nonnegative integers.

Also \(q(m)\to\infty\), since \(q\) is a permutation of \(\mathbb N_0\). We may therefore choose a sufficiently large \(m\) satisfying (2), (3), and
\[
q(0)<q(m)<q(m+1).
\tag{4}
\]

Inside \(S_{m+1}\), either the even subblock precedes the odd subblock or vice versa. Let \(e\in\{0,1\}\) be the parity of the earlier subblock, and put
\[
a=e.
\]
Thus \(a\in S_0\).

Choose an odd integer \(d\) with
\[
\frac{R_m}{2}<d\le R_m-1.
\tag{5}
\]
Such an odd integer exists for every sufficiently large \(R_m\).

Now define
\[
x_i=a+id,\qquad 0\le i\le3.
\]

First,
\[
x_1=a+d>R_m/2>R_{m-1},
\]
while, using \(a\le1\) and \(d\le R_m-1\),
\[
x_1\le R_m.
\]
Hence \(x_1\in S_m\).

Next, (5) gives
\[
x_2=a+2d>R_m.
\]
Also
\[
x_3=a+3d\le 1+3(R_m-1)=3R_m-2\le R_{m+1}.
\]
Thus \(x_2,x_3\in S_{m+1}\).

By (4), the shell ordering gives
\[
x_0=a\prec x_1\prec x_2,x_3.
\]
Because \(d\) is odd,
\[
x_2\equiv a\equiv e\pmod2,\qquad
x_3\equiv 1-e\pmod2.
\]
The parity-\(e\) subblock of \(S_{m+1}\) was chosen to be earlier, so
\[
x_2\prec x_3.
\]
Consequently
\[
a\prec a+d\prec a+2d\prec a+3d,
\]
a monotone four-term AP. ∎

#### Consequence

Ordering every finite annulus by truncated binary digit reversal, with arbitrary reversals at deeper nodes and with the annuli themselves placed in any \(\omega\)-order, cannot solve the problem. The obstruction already occurs at the top parity split.

The proof also explains why merely alternating the orientation of consecutive shells does not work: at an outward shell boundary, the parity of the small initial term selects whichever orientation makes the final pair increasing.

---

### 5. A fair self-similar interleaving still fails

One can avoid all infinite convex blocks by interleaving the even and odd residue classes at every stage. The following natural signed binary substitution is genuinely fair.

Define \(F:\mathbb N_0\to\mathbb Z\) recursively by
\[
F(0)=0,
\]
\[
F(2k)=2F(k)\quad(k\ge1),
\]
and
\[
F(2k+1)=1-2F(k)\quad(k\ge0).
\tag{6}
\]

Its first terms are
\[
0,1,2,-1,4,-3,-2,3,8,-7,-6,7,-4,5,6,-5,\ldots
\]

#### Lemma 7: \(F\) is a bijection \(\mathbb N_0\to\mathbb Z\).

For \(m\ge1\), let
\[
I_m=\{-(2^{m-1}-1),\ldots,2^{m-1}\}.
\]
I claim
\[
F([0,2^m))=I_m.
\tag{7}
\]

For \(m=1\), the image is \(\{0,1\}=I_1\).

Assume (7). In the first \(2^{m+1}\) indices, the even positions have image
\[
2I_m,
\]
which consists of all even integers from \(-2^m+2\) to \(2^m\). The odd positions have image
\[
1-2I_m,
\]
which consists of all odd integers from \(1-2^m\) to \(2^m-1\). These sets are disjoint and together form
\[
\{-(2^m-1),\ldots,2^m\}=I_{m+1}.
\]
This proves (7) inductively. The intervals \(I_m\) exhaust \(\mathbb Z\), so \(F\) is bijective. ∎

Nevertheless,
\[
F(0)=0,\quad F(1)=1,\quad F(2)=2,\quad F(7)=3.
\]
Thus
\[
0,1,2,3
\]
occurs in increasing order at positions
\[
0<1<2<7.
\]
So this fair signed interleaving contains a forbidden four-term AP.

This example shows that fairness and exact residue-class self-similarity are not enough: the interleaving rule must also encode substantially more information than a single sign reversal between the two children.

---

### 6. Ledger

#### Proved

1. Binary \(2\)-adic lexicographic orders avoid every monotone three-term AP.
2. Ternary \(3\)-adic lexicographic orders avoid every monotone four-term AP.
3. Such orders are not of type \(\omega\).
4. The global opposite-pair rule (O), although sufficient for four-AP avoidance, forces every integer to have infinitely many predecessors.
5. Any rapidly growing annular construction with convex shell blocks and convex parity subblocks contains a monotone four-term AP, regardless of shell order and deeper residue reversals.
6. The explicit fair signed binary substitution (6) is a permutation of \(\mathbb Z\), but contains \(0,1,2,3\) monotonically.

#### Plausible but unproved

1. Any finite-state residue substitution strong enough to certify avoidance solely at the first splitting digit may necessarily recreate either an infinite convex block or a periodic comparison rule of the kind ruled out by Lemma 5.
2. A sufficiently state-dependent nonconvex interleaving of residue cylinders might still work; no contradiction was found for the entire class.
3. Base \(3\) appears better adapted than base \(2\), because a four-term AP has first-splitting digit pattern
   \[
   r,\ r+u,\ r+2u,\ r,
   \]
   but a fair merge rule preserving this obstruction remains unknown.

#### Dead ends

1. Full \(2\)-adic or \(3\)-adic lexicographic order: wrong order type.
2. Opposite orientations on the two same-parity pairs: forces infinitely many predecessors.
3. Finite annuli with internal bit reversal: killed by Theorem 6.
4. Alternating annular orientations: the parity of the inner term defeats either orientation.
5. The simplest fair signed self-similar binary merge: contains \(0,1,2,3\).

## Self-Audit

1. **The shell obstruction has restrictive hypotheses.**  
   It assumes convex annuli and convex parity subblocks, so it does not exclude all hierarchical residue constructions. The theorem itself is sound: the selected AP has one term in the core, one in the lower shell, and two in the upper shell, and every required inequality follows directly from block convexity.

2. **Lemma 5 rules out only one sufficient comparison scheme, not all possible witness assignments.**  
   A four-AP-avoiding order need not orient the two distance-\(2d\) pairs oppositely. The periodicity and infinite-predecessor conclusion nevertheless follow rigorously whenever condition (O) is imposed.

3. **The main remaining block is genuinely comparable to the original problem.**  
   I have not characterized all fair nonconvex residue interleavings. Producing one with a finite invariant would give a counterexample, while proving none can work would likely require a new global theorem. I therefore do not claim that Route 4 itself is impossible—only that its standard implementations are.

## Computations To Verify

```python
from functools import lru_cache

def monotone_aps(order, k=4):
    """Return all monotone k-APs completed inside a finite order."""
    pos = {x: i for i, x in enumerate(order)}
    S = set(order)
    lo, hi = min(S), max(S)
    out = []
    for d in range(1, (hi - lo) // (k - 1) + 1):
        for a in range(lo, hi - (k - 1) * d + 1):
            ap = [a + i*d for i in range(k)]
            if all(x in S for x in ap):
                pp = [pos[x] for x in ap]
                inc = all(pp[i] < pp[i+1] for i in range(k-1))
                dec = all(pp[i] > pp[i+1] for i in range(k-1))
                if inc or dec:
                    out.append((a, d, pp))
    return out


def padic_key(x, p, depth):
    # Python's modulo convention gives the p-adic digits also for x < 0.
    return tuple((x // (p**j)) % p for j in range(depth))

def finite_padic_order(S, p):
    maxdiff = max(abs(x-y) for x in S for y in S)
    depth = 1
    while p**depth <= maxdiff:
        depth += 1
    return sorted(S, key=lambda x: padic_key(x, p, depth))

# Verify the finite forms of Lemmas 1 and 2.
for N in range(2, 40):
    S = list(range(-N, N+1))

    order2 = finite_padic_order(S, 2)
    assert monotone_aps(order2, k=3) == []

    order3 = finite_padic_order(S, 3)
    assert monotone_aps(order3, k=4) == []


@lru_cache(None)
def F(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return 2 * F(n // 2)
    return 1 - 2 * F(n // 2)

# Verify the fair substitution and its first forbidden AP.
for m in range(1, 12):
    vals = [F(n) for n in range(2**m)]
    expected = set(range(-(2**(m-1)-1), 2**(m-1)+1))
    assert set(vals) == expected
    assert len(vals) == len(set(vals))

prefix = [F(n) for n in range(32)]
assert prefix[0] == 0
assert prefix[1] == 1
assert prefix[2] == 2
assert prefix[7] == 3
assert (0, 1, [0, 1, 2, 7]) in monotone_aps(prefix, 4)


def shell_boundary_witness(R_prev, R, R_next, earlier_parity):
    """
    Construct the AP used in Theorem 6.
    earlier_parity = 0 if evens precede odds in the upper shell,
                     1 otherwise.
    """
    assert R > 2 * R_prev
    assert R_next >= 3 * R

    a = earlier_parity
    for d in range(R // 2 + 1, R):
        if d % 2 == 1:
            ap = [a + i*d for i in range(4)]
            if (R_prev < ap[1] <= R and
                    R < ap[2] <= R_next and
                    R < ap[3] <= R_next):
                return ap
    raise AssertionError("No witness found")

for R in range(10, 200):
    for parity in (0, 1):
        shell_boundary_witness(R // 3, R, 3*R, parity)
```

A useful finite SAT test for the remaining nonconvex substitution problem is:

```python
# Z3-style pseudocode

S = range(-N, N+1)
pos[x] = Int(f"p_{x}") for x in S

solver.add(Distinct([pos[x] for x in S]))
for x in S:
    solver.add(0 <= pos[x], pos[x] < len(S))

for every a,d with a,a+d,a+2*d,a+3*d in S:
    x0,x1,x2,x3 = ...
    solver.add(Not(And(pos[x0] < pos[x1],
                       pos[x1] < pos[x2],
                       pos[x2] < pos[x3])))
    solver.add(Not(And(pos[x0] > pos[x1],
                       pos[x1] > pos[x2],
                       pos[x2] > pos[x3])))

# Test exact self-similarity on the even copy.
for x,y with x,y,2*x,2*y in S:
    solver.add((pos[2*x] < pos[2*y]) == (pos[x] < pos[y]))

# Add candidate finite-state merge constraints for residue classes.
# Increase N and extract either models or minimal unsatisfiable cores.
```

The most informative computation would synthesize merge rules with a small number of states, then use an automaton over the base-\(3\) digits of \((a,d)\) to search for a monotone four-AP at arbitrary scale.

## Route Diagnosis

The local residue mechanism works exceptionally well: binary lexicographic order already destroys three-term APs, and ternary lexicographic order destroys exactly the four-term pattern under study. The obstruction is entirely the conversion from an infinite convex residue hierarchy to an \(\omega\)-order. Convex classes give infinitely many predecessors; retaining only opposite sibling comparisons still gives infinite predecessor chains; truncating into finite shells creates unavoidable boundary APs; and the simplest fair self-similar merge fails explicitly.

The unresolved possibility is a nonconvex, state-dependent merge of the residue-class copies in which each AP receives a local inversion witness but no fixed pair comparison repeats periodically along an infinite arithmetic chain. A fresh Route 4 attempt should synthesize such merges in base \(3\), not base \(2\), and demand an automaton-verifiable invariant covering all digit/carry patterns. If small-state searches are repeatedly unsatisfiable, Route 6 should extract their cores into a finite forcing calculus aimed at proving \(K=4\).