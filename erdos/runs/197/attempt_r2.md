STATUS: BLOCKED

## Result

Route 2 yields a sharp structural diagnosis but not a two-color solution. I prove: (i) an exact criterion for concatenating naturally ordered finite monochromatic intervals; (ii) every two-color decomposition into alternating finite intervals necessarily has a monochromatic 3-term progression crossing interval boundaries, so a two-state block construction cannot isolate all progressions inside finite blocks; and (iii) a complete scale-separated three-color construction, recovering the known relaxation and explaining geometrically why three states work. For two colors, ternary shells reduce the problem to an explicit family of independent finite constrained-ordering problems. The unresolved point is whether those finite constraints are always satisfiable; the ordinary finite permutation lemma does not preserve the required precedence relations.

## Complete Argument

### 1. Exact criterion for naturally concatenated interval blocks

Let
\[
1=s_0<s_1<s_2<\cdots
\]
be integers, and put
\[
I_k=[s_k,s_{k+1}-1]\cap\mathbb N.
\]
Color every element of \(I_k\) by \(k\bmod 2\). For every \(k\), let \(\pi_k\) be a permutation of \(I_k\). Enumerate color \(c\) by concatenating
\[
\pi_c,\pi_{c+2},\pi_{c+4},\ldots.
\]
Because every block is finite, these concatenations are genuine \(\omega\)-enumerations: every element occurs exactly once and after only finitely many earlier blocks.

For \(u\in I_k\), write \(r_k(u)\) for its rank inside \(\pi_k\).

**Lemma 1.** The two concatenated enumerations avoid monotone 3-term arithmetic progressions if and only if all three of the following hold.

1. Every \(\pi_k\) internally avoids monotone 3-term progressions.
2. There is no monochromatic progression \(x<y<z\) whose terms lie in three distinct blocks.
3. For every monochromatic progression meeting exactly two blocks \(I_i,I_j\), with \(i<j\):
   - if \(x,y\in I_i\) and \(z\in I_j\), then
     \[
     r_i(y)<r_i(x);
     \]
   - if \(x\in I_i\) and \(y,z\in I_j\), then
     \[
     r_j(z)<r_j(y).
     \]

**Proof.**

Since the blocks are numerical intervals and \(x<y<z\), their block indices are nondecreasing.

If all three terms lie in one block, avoidance is exactly condition 1.

If they lie in three distinct blocks \(I_i,I_j,I_\ell\), then \(i<j<\ell\). In the concatenated color order, every element of \(I_i\) precedes every element of \(I_j\), and every element of \(I_j\) precedes every element of \(I_\ell\). Thus \(y\) is positionally between \(x\) and \(z\), independently of the internal block orders. Such a progression is always forbidden, proving condition 2 is necessary and sufficient for this case.

If the progression meets exactly two blocks, convexity of the intervals leaves only the distributions \((i,i,j)\) and \((i,j,j)\).

In the first case, \(z\) occurs after both \(x\) and \(y\). Therefore \(y\) is between \(x\) and \(z\) exactly when \(x\) precedes \(y\), so avoidance is equivalent to \(y\) preceding \(x\).

In the second case, \(x\) occurs before both \(y\) and \(z\). Hence \(y\) lies between \(x\) and \(z\) exactly when \(y\) precedes \(z\), so avoidance is equivalent to \(z\) preceding \(y\). ∎

Thus cross-block progressions cannot merely be ignored: those occupying three blocks are fatal, while those occupying two blocks impose directed precedence constraints inside one block.

---

### 2. Two alternating interval states cannot isolate all progressions

A natural scale-separated plan would be to choose the intervals so that every monochromatic progression is wholly contained in one block. The next theorem proves this is impossible with two alternating finite interval states, irrespective of how rapidly or irregularly the block sizes grow.

**Theorem 2.** Let
\[
\mathbb N=I_0\sqcup I_1\sqcup I_2\sqcup\cdots
\]
be consecutive nonempty finite intervals, colored alternately. Then some monochromatic nonconstant 3-term arithmetic progression meets at least two intervals.

**Proof.**

Write
\[
I_k=[s_k,s_{k+1}-1],\qquad h_k=s_{k+1}-s_k.
\]
Assume for contradiction that every monochromatic 3-term progression is contained in one interval.

For \(k\ge2\), the intervals \(I_{k-2}\) and \(I_k\) have the same color. Set
\[
x=s_{k-1}-1\in I_{k-2},\qquad y=s_k\in I_k,
\]
and
\[
z=2y-x=2s_k-s_{k-1}+1.
\]
If \(z\le s_{k+1}-1\), then \(z\in I_k\), and \(x,y,z\) form a monochromatic progression crossing two intervals. Therefore
\[
2s_k-s_{k-1}+1\ge s_{k+1}.
\]
Equivalently,
\[
h_k=s_{k+1}-s_k\le s_k-s_{k-1}+1=h_{k-1}+1. \tag{1}
\]

Let
\[
H_K=\max_{0\le j<K}h_j.
\]
We claim
\[
H_K=o(s_K).
\]

Choose \(j<K\) with \(h_j=H_K=:H\). Reversing (1) gives
\[
h_{j-r}\ge H-r
\]
whenever \(0\le r\le j\). Also, iterating (1) forward gives
\[
H=h_j\le h_0+j.
\]
If \(H\ge2h_0\), then \(j\ge H-h_0\ge H/2\). Consequently,
\[
s_K-1=\sum_{i=0}^{K-1}h_i
 \ge \sum_{r=0}^{\lfloor H/2\rfloor}(H-r)
 \ge \frac{H^2}{4}.
\]
Thus
\[
\frac{H_K}{s_K-1}\le \frac{2}{\sqrt{s_K-1}}
\]
whenever \(H_K\ge2h_0\). If \(H_K<2h_0\), the ratio also tends to zero because \(s_K\to\infty\). Hence indeed
\[
H_K=o(s_K). \tag{2}
\]

We now count monochromatic progressions in
\[
[1,N],\qquad N=s_K-1.
\]

There are
\[
L_N=\sum_{d=1}^{\lfloor(N-1)/8\rfloor}(N-8d)
\]
nine-term arithmetic progressions in \([1,N]\). For \(N\ge32\), restricting to \(d\le N/16\) gives
\[
L_N\ge \frac{N^2}{64}. \tag{3}
\]

By \(W(2,3)=9\), each colored nine-term progression contains a monochromatic three-term progression.

A fixed three-term progression can be contained in at most \(16\) nine-term progressions. Indeed, if its terms occupy positions
\[
i,\ i+r,\ i+2r
\]
inside a nine-term progression, then \(1\le r\le4\) and \(0\le i\le8-2r\). Hence the number of possible position triples is
\[
\sum_{r=1}^4(9-2r)=7+5+3+1=16.
\]
Once the positions are chosen, the containing nine-term progression is determined, if it exists.

It follows from (3) that \([1,N]\) contains at least
\[
\frac{N^2}{1024} \tag{4}
\]
distinct monochromatic three-term progressions.

Under our assumption, all these progressions lie inside individual intervals. An interval of length \(h\) contains fewer than \(h^2\) three-term progressions, so their total number is at most
\[
\sum_{j<K}h_j^2
 \le H_K\sum_{j<K}h_j
 =H_KN.
\]
By (2), this is \(o(N^2)\), contradicting (4) for sufficiently large \(K\). ∎

This theorem rules out the cleanest two-state block theorem: unlike the three-color construction below, two alternating finite interval types cannot make all cross-block progressions disappear.

The same conclusion applies after merging adjacent blocks of the same color into maximal monochromatic runs, provided there are infinitely many finite runs.

---

### 3. Recovery of the scale-separated three-color construction

The previous obstruction is genuinely a two-state phenomenon. Three cyclic interval states allow enough geometric separation to eliminate all cross-block monochromatic progressions.

Let
\[
q=\frac32,\qquad s_k=\left\lceil16q^k\right\rceil\quad(k\ge1).
\]
Define
\[
I_0=[1,s_1-1],
\qquad
I_k=[s_k,s_{k+1}-1]\quad(k\ge1),
\]
and color \(I_k\) by \(k\bmod3\).

**Theorem 3.** Every monochromatic three-term progression is contained in one block \(I_k\).

**Proof.**

Fix \(k\ge3\). All earlier blocks of the same color as \(I_k\) are contained in
\[
[1,M],\qquad M=s_{k-2}-1.
\]

First,
\[
M<16q^{k-2},
\]
while
\[
s_k\ge16q^k=36q^{k-2}>2M. \tag{5}
\]
Thus no progression can have \(x,y\le M\) and \(z\in I_k\), because then
\[
z=2y-x<2y\le2M<s_k.
\]

It remains to exclude \(x\le M\) and \(y,z\in I_k\). In that case
\[
x=2y-z\ge2s_k-(s_{k+1}-1).
\]
Using
\[
s_k\ge16q^k,\qquad s_{k+1}<16q^{k+1}+1,
\]
we get
\[
2s_k-s_{k+1}+1
>32q^k-16q^{k+1}
=16q^k(2-q)
=8q^k
=18q^{k-2}.
\]
Since \(M<16q^{k-2}\), it follows that \(x>M\), a contradiction.

Now take any monochromatic progression meeting multiple blocks and consider its largest-index block. Since the blocks are numerical intervals, that block contains either only \(z\), or both \(y,z\). Both possibilities were just excluded. Therefore every monochromatic progression is internal to one block. ∎

By the finite permutation lemma, choose an avoiding permutation \(\pi_k\) of every finite \(I_k\). For each color \(c\), concatenate
\[
\pi_c,\pi_{c+3},\pi_{c+6},\ldots.
\]
Every earlier block is finite, so this is an \(\omega\)-enumeration. Theorem 3 excludes cross-block monochromatic progressions, and the finite lemma handles internal ones. This proves the three-color relaxation completely.

The relevant numerical margins are
\[
q^2>2,\qquad q^2(2-q)>1.
\]
They hold at \(q=3/2\). With only two cyclic states, the analogous geometric requirements would be
\[
q>2,\qquad q(2-q)>1,
\]
which are incompatible. Theorem 2 shows that this incompatibility is not merely an artifact of assuming geometric block sizes.

---

### 4. A precise two-color finite-extension reduction

Although cross-block progressions cannot all be eliminated, scale separation can reduce them to one directed type.

Let
\[
I_k=[3^k,3^{k+1}-1],\qquad \chi(I_k)=k\bmod2.
\]
For each color, plan to concatenate its block permutations in increasing \(k\).

For \(k\ge2\), define the earlier same-color set
\[
E_k=\bigcup_{\substack{0\le j\le k-2\\j\equiv k\pmod2}}I_j.
\]

**Proposition 4.** In any monochromatic progression crossing block boundaries, if \(I_k\) is the largest-index occupied block, then
\[
x\in E_k,\qquad y,z\in I_k.
\]

**Proof.**

The largest earlier block of the same color is \(I_{k-2}\), whose maximum is
\[
3^{k-1}-1.
\]
If only \(z\) lay in \(I_k\), then
\[
y\le3^{k-1}-1
\]
and hence
\[
z=2y-x<2\cdot3^{k-1}<3^k,
\]
contradicting \(z\in I_k\). Therefore \(y,z\in I_k\), and \(x\) lies in an earlier same-color block. ∎

It follows from Lemma 1 that this fixed coloring and block schedule solves the original problem if and only if, for every \(k\), there is a permutation \(\pi_k\) of \(I_k\) satisfying:

1. every progression wholly inside \(I_k\) has its midpoint outside its endpoints positionally;
2. whenever
   \[
   x\in E_k,\qquad y,z\in I_k,\qquad x+z=2y,
   \]
   one has
   \[
   r_k(z)<r_k(y). \tag{6}
   \]

These are independent finite problems: choosing \(\pi_k\) does not change the constraints for any other block.

There is additional scale separation in (6). Put \(L=3^k\). Since
\[
x\le\frac L3-1,\qquad L\le y<z\le3L-1,
\]
we obtain
\[
z=2y-x>\frac{5L}{3},
\]
and, conversely,
\[
y=\frac{x+z}{2}<\frac{5L}{3}.
\]
Thus all required directed edges in (6) point from the upper portion of \(I_k\) to its lower portion:
\[
z>\frac{5L}{3}>y.
\]

This is the strongest concrete Route 2 reduction I obtained. The unresolved finite statement is:

> For every \(k\), can the internal non-betweenness constraints on \(I_k\) be satisfied simultaneously with all directed edges \(z\prec y\) from (6)?

The finite permutation lemma alone does not answer this, because it gives no control over prescribed pairwise precedences.

A warning against the obvious parity recursion is already visible in dyadic shells. For
\[
I_4=[16,31],
\]
the previous same-colored shell contains \(4,5,6,7\). The progressions
\[
5,16,27
\quad\text{and}\quad
6,17,28
\]
force
\[
27\prec16,\qquad 28\prec17.
\]
Any parity-recursive order whose top-level parity classes are contiguous must place either all evens before all odds or all odds before all evens. The first choice violates \(27\prec16\), and the second violates \(28\prec17\). Thus the standard finite parity construction cannot simply be inserted as the shell order.

No proof or counterexample for the constrained finite statement is presently established here. Consequently the route is blocked at a genuine, explicitly formulated extension lemma.

## Self-Audit

1. **Theorem 2 uses a supersaturation count derived from \(W(2,3)=9\).**  
   The delicate point is the multiplicity bound. It is valid because the positions of a numerical 3-AP inside a nine-term AP must themselves form a 3-AP; there are exactly at most \(7+5+3+1=16\) such position triples.

2. **The ceiling errors in the three-color construction could invalidate scale inequalities.**  
   They do not: the proof uses the strict estimates \(\lceil t\rceil-1<t\) and \(\lceil t\rceil<t+1\), and both geometric margins are larger than the rounding error.

3. **The ternary-shell reduction may look close to a solution, but its finite extension assertion is unproved.**  
   I do not claim it holds. What is proved is only the exact equivalence for that fixed block ansatz and the upper-to-lower localization of all additional precedence constraints. This unresolved point is precisely why the status is BLOCKED.

## Computations To Verify

The principal finite question can be tested directly with Z3.

```python
from z3 import Int, Solver, Distinct, And, Or, sat

def block(k):
    return list(range(3**k, 3**(k+1)))

def earlier_same_color(k):
    E = []
    for j in range(k - 1):
        if j % 2 == k % 2:
            E.extend(block(j))
    return E

def solve_ternary_block(k, timeout_ms=None):
    B = block(k)
    Bset = set(B)
    E = earlier_same_color(k)

    r = {n: Int(f"r_{k}_{n}") for n in B}
    s = Solver()
    if timeout_ms is not None:
        s.set(timeout=timeout_ms)

    m = len(B)
    for n in B:
        s.add(0 <= r[n], r[n] < m)
    s.add(Distinct([r[n] for n in B]))

    # Internal non-betweenness constraints.
    for a in B:
        d = 1
        while a + 2*d <= B[-1]:
            y = a + d
            z = a + 2*d
            s.add(Or(
                And(r[y] < r[a], r[y] < r[z]),
                And(r[y] > r[a], r[y] > r[z])
            ))
            d += 1

    # Incoming constraints: x old, y,z current => z must precede y.
    for x in E:
        for y in B:
            z = 2*y - x
            if z in Bset and y < z:
                s.add(r[z] < r[y])

    ans = s.check()
    if ans != sat:
        return ans, None

    model = s.model()
    order = sorted(B, key=lambda n: model[r[n]].as_long())
    return ans, order

def check_avoiding(order):
    pos = {x: i for i, x in enumerate(order)}
    S = set(order)
    for x in order:
        for z in order:
            if x >= z or (x + z) % 2:
                continue
            y = (x + z) // 2
            if y in S:
                if min(pos[x], pos[z]) < pos[y] < max(pos[x], pos[z]):
                    return False, (x, y, z)
    return True, None

def check_incoming(k, order):
    pos = {x: i for i, x in enumerate(order)}
    Bset = set(order)
    for x in earlier_same_color(k):
        for y in order:
            z = 2*y - x
            if z in Bset and y < z and not (pos[z] < pos[y]):
                return False, (x, y, z)
    return True, None

for k in range(5):
    ans, order = solve_ternary_block(k, timeout_ms=600_000)
    print("k =", k, "status =", ans)
    if order is not None:
        print("internal:", check_avoiding(order))
        print("incoming:", check_incoming(k, order))
        print("order:", order)
```

A solver should first test \(k=2\), where \(I_2=[9,26]\), and then \(k=3\), where \(I_3=[27,80]\). If an instance is unsatisfiable, an unsatisfiable core or a minimized subset of progressions should be extracted.

The exact natural-block criterion can be checked as follows.

```python
def check_two_color_blocks(block_orders):
    # block_orders[k] is a permutation of consecutive interval I_k
    sequences = [[], []]
    color_of = {}
    for k, order in enumerate(block_orders):
        c = k % 2
        sequences[c].extend(order)
        for x in order:
            if x in color_of:
                return False, ("duplicate", x)
            color_of[x] = c

    for c in (0, 1):
        ok, witness = check_avoiding(sequences[c])
        if not ok:
            return False, (c, witness)
    return True, None
```

The three-color construction can be verified on any finite collection of blocks.

```python
from math import ceil

def three_color_blocks(K):
    q = 1.5
    s = {k: ceil(16 * q**k) for k in range(1, K + 2)}
    blocks = [[*range(1, s[1])]]
    for k in range(1, K + 1):
        blocks.append([*range(s[k], s[k+1])])
    return blocks

def find_cross_block_ap(blocks, colors):
    owner = {}
    for k, B in enumerate(blocks):
        for x in B:
            owner[x] = k
    N = max(owner)

    for x in range(1, N + 1):
        for d in range(1, (N - x)//2 + 1):
            y, z = x + d, x + 2*d
            if colors[owner[x]] == colors[owner[y]] == colors[owner[z]]:
                if len({owner[x], owner[y], owner[z]}) > 1:
                    return (x, y, z), (owner[x], owner[y], owner[z])
    return None

blocks = three_color_blocks(12)
colors = [k % 3 for k in range(len(blocks))]
print(find_cross_block_ap(blocks, colors))  # Expected: None
```

Finally, the cross-block theorem for two alternating intervals can be stress-tested on random block lengths.

```python
import random

def first_cross_ap(lengths):
    blocks = []
    start = 1
    owner = {}
    for k, h in enumerate(lengths):
        B = list(range(start, start + h))
        blocks.append(B)
        for x in B:
            owner[x] = k
        start += h

    N = start - 1
    for x in range(1, N + 1):
        for d in range(1, (N - x)//2 + 1):
            y, z = x + d, x + 2*d
            ix, iy, iz = owner[x], owner[y], owner[z]
            if ix % 2 == iy % 2 == iz % 2 and len({ix, iy, iz}) > 1:
                return (x, y, z), (ix, iy, iz)
    return None

for _ in range(1000):
    lengths = [random.randint(1, 100) for _ in range(30)]
    witness = first_cross_ap(lengths)
    if witness is None:
        print("No finite witness yet:", lengths)
```

Finite truncations can lack a witness near the end, so this last test supports but cannot prove Theorem 2.

## Route Diagnosis

**Proved ledger**

- Exact necessary and sufficient conditions for natural concatenation of finite monochromatic interval blocks.
- No two-color alternating finite-interval decomposition can make every monochromatic 3-AP internal to one block.
- A complete three-color scale-separated construction using cyclic blocks with ratio \(3/2\).
- An explicit two-color ternary-shell reduction in which every cross-block constraint is a directed edge from the upper portion of one finite shell to its lower portion.

**Plausible but unproved**

- The constrained finite ternary-shell instances may all be satisfiable.
- There may be a recursive low/middle/high substitution rule visible in satisfying models.
- A weaker version may require changing the shell ratio or splitting each shell into two internal states before assigning its final color.

**Dead ends**

- Purely eliminating cross-block progressions with two interval states is impossible by Theorem 2.
- Direct insertion of the parity-recursive finite order fails because incoming constraints can demand both parity orientations simultaneously.
- Merely increasing scale separation does not solve the issue: it removes progressions with only the largest term in the new block but leaves many constraints with the midpoint and largest term together in that block.

**Precise block**

The route now requires a finite extension theorem of the form:

> Every ternary shell \(I_k\) admits an internally avoiding order satisfying all incoming edges \(z\prec y\) generated by earlier same-colored shells.

This statement is not implied by the finite permutation lemma, and I have no proof of it. A failure at one finite \(k\) would kill this particular ansatz but not disprove the original problem.

A fresh attempt should first run the finite solver above. If the first several shells are satisfiable, the models should be mined for a recursive substitution pattern, especially around the threshold \(5\cdot3^{k-1}\). If an instance is unsatisfiable, one should extract a minimal obstruction and use it to determine whether splitting each shell between the two colors can remove exactly the conflicting precedence cycle.