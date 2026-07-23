STATUS: BLOCKED

## Result

For Route 3, let \(B_k=[\lceil(3/2)^k\rceil,\lceil(3/2)^{k+1}\rceil-1]\), retain the class \(k\equiv0\pmod3\), and merge the adjacent classes
\[
A=\bigcup_{k\equiv1,2\pmod3}B_k.
\]
I proved that no merge in which every \(B_k\subset A\) remains a contiguous atomic block can work, even if the blocks are scheduled in an arbitrary \(\omega\)-order. I also proved a positive “far-interaction” theorem: all progressions \(x<y<z\) in \(A\) with \(x\le (2/3)^9y\) can simultaneously be oriented with the midpoint last in a genuine \(\omega\)-order. The remaining progressions lie in at most twelve consecutive \(3/2\)-scale blocks. Thus the genuine long-memory obstruction can be removed by a bounded-depth potential, reducing this merge attempt to a bounded-scale but still unproved local scheduling problem. Finally, I exhibited an asymptotic family of mixed-track progressions showing that orienting every mixed progression with its midpoint last is impossible; any successful merge must use a nontrivial alternating finite-state rule. I do not have the required theorem solving the residual twelve-block CSP, so Route 3 remains blocked.

## Complete Argument

### 1. Notation and elementary scale geometry

Put
\[
q=\frac32,\qquad a_k=\lceil q^k\rceil,\qquad
B_k=[a_k,a_{k+1}-1]\cap\mathbb N.
\]
For \(n\ge1\), define
\[
\kappa(n)=\left\lfloor\log_q n\right\rfloor .
\]

For integer \(n\),
\[
n\in B_k
\iff q^k\le n<q^{k+1}
\iff \kappa(n)=k.
\]
Thus the three original colors are exactly the residue classes of \(\kappa(n)\pmod3\).

We focus on
\[
A=\{n\in\mathbb N:\kappa(n)\equiv1\text{ or }2\pmod3\}.
\]
The complementary class \(\kappa(n)\equiv0\pmod3\) already has the avoiding order from the known three-color construction.

#### Lemma 1: The midpoint and largest term are scale-local

If \(x<y<z\) and \(x+z=2y\), then
\[
\kappa(z)-\kappa(y)\le2.
\]

**Proof.**
Since \(z<2y\),
\[
\log_q z-\log_q y<\log_q2<2
\]
because \(2<q^2=9/4\). Hence the difference of the floors is at most \(2\). ∎

Consequently, after merging residues \(1\) and \(2\), the high pair \(y,z\) of any cross-block progression lies in consecutive selected blocks:
\[
B_{3t+1}\to B_{3t+2}
\quad\text{or}\quad
B_{3t+2}\to B_{3t+4}.
\]
The smallest term \(x\), however, may be arbitrarily far below them.

---

### 2. Atomic block merging is impossible

Here “atomic” means that every selected block \(B_k\), \(k\equiv1,2\pmod3\), occupies a finite contiguous interval of positions. The blocks may otherwise be placed in any order, and their internal permutations may be arbitrary.

The integer \(2\) is the sole element of \(B_1\), hence \(2\in A\).

#### Lemma 2: Fixed-anchor progressions occur across every sufficiently high pair of consecutive selected blocks

1. If \(j\ge4\), then there are
   \[
   y\in B_j,\qquad z\in B_{j+1}
   \]
   with
   \[
   2+z=2y.
   \]

2. If \(j\ge5\), then there are
   \[
   y\in B_j,\qquad z\in B_{j+2}
   \]
   with
   \[
   2+z=2y.
   \]

**Proof.**

For the first statement, let \(t=q^j\), put
\[
y=a_j=\lceil t\rceil,\qquad z=2a_j-2.
\]
Certainly \(y\in B_j\). For \(j\ge5\), \(t\ge q^5>6\), and
\[
z\ge2t-2\ge \frac32t+1\ge \left\lceil\frac32t\right\rceil=a_{j+1}.
\]
Also, for \(j\ge4\), \(t>4\), and
\[
z<2t\le \frac94t-1\le a_{j+2}-1.
\]
The remaining case \(j=4\) is direct:
\[
a_4=6,\quad z=10,\quad B_5=[8,11].
\]
Thus \(z\in B_{j+1}\).

For the second statement, put
\[
y=a_{j+1}-1,\qquad z=2y-2=2a_{j+1}-4.
\]
Then \(y\in B_j\). Since \(j\ge5\), \(t=q^j>20/3\), and
\[
z\ge3t-4\ge\frac94t+1\ge a_{j+2}.
\]
Moreover,
\[
z<3t-2\le\frac{27}{8}t-1\le a_{j+3}-1.
\]
Therefore \(z\in B_{j+2}\). ∎

The selected block indices in increasing numerical order are
\[
1,2,4,5,7,8,\dots.
\]
Lemma 2 therefore supplies a progression
\[
(2,y,z)
\]
across every sufficiently high consecutive pair in this list.

#### Proposition 3: No atomic-block merge of \(A\) is an avoiding \(\omega\)-order

**Proof.**
Suppose all selected \(B_k\) are contiguous in an \(\omega\)-enumeration of \(A\). The block \(B_1=\{2\}\) has a finite position, so only finitely many other blocks can occur before it. Hence all sufficiently high selected blocks occur after \(2\).

Let \(B_j,B_\ell\) be a sufficiently high consecutive pair of selected blocks, where \(\ell=j+1\) or \(j+2\). By Lemma 2 there are \(y\in B_j\), \(z\in B_\ell\) such that
\[
(2,y,z)
\]
is a numerical progression. Since \(2\) occurs before both \(y\) and \(z\), avoidance forces the midpoint \(y\) to occur after \(z\). As the two blocks are contiguous and disjoint, the entire block \(B_\ell\) must occur before \(B_j\).

Thus, for all sufficiently large consecutive selected block indices \(s_n<s_{n+1}\),
\[
B_{s_{n+1}}\triangleleft B_{s_n}.
\]
This is an infinite strictly descending chain of finite block positions in an \(\omega\)-order, which is impossible. ∎

Therefore any successful Route-3 merge must interleave elements of neighboring blocks; merely rescheduling whole blocks cannot work.

---

### 3. The merged set has no elementary affine-copy obstruction

This does not prove orderability, but it confirms that the merged class avoids the immediate obstruction responsible for the one-color theorem.

#### Lemma 4: \(A\) contains no infinite affine copy of \(\mathbb N_0\)

There are no \(a,d\in\mathbb N\) such that
\[
a+dm\in A\qquad(m\ge0).
\]

**Proof.**
Fix \(0<\varepsilon<1/2\). For every sufficiently large \(r\), the interval
\[
J_r=\left(q^{3r+\varepsilon},q^{3r+1-\varepsilon}\right)
\]
has length greater than \(d\). Hence it contains an integer congruent to \(a\pmod d\), necessarily of the form \(a+dm\) for some \(m\ge0\).

Every integer in \(J_r\) has \(\kappa(n)\equiv0\pmod3\), contrary to \(a+dm\in A\). ∎

A slightly stronger sparse check is also available.

#### Lemma 5: No dyadic affine ray lies entirely in \(A\)

There are no \(a,d\in\mathbb N\) such that
\[
a+2^m d\in A\qquad(m\ge0).
\]

**Proof.**
Let
\[
\alpha=\log_q2.
\]
Then \(\alpha/3\) is irrational: otherwise \(2^s=q^{3r}\) for some nonzero integers \(r,s\), contradicting unique prime factorization.

Moreover,
\[
\log_q(a+2^m d)
 =m\alpha+\log_qd+o(1).
\]
The sequence \(m\alpha\pmod3\) is dense, and an \(o(1)\) perturbation still enters every fixed open subinterval infinitely often. In particular it enters an interval strictly inside \((0,1)\pmod3\), where \(\kappa\equiv0\pmod3\). ∎

---

### 4. A rigorous far-interaction merge theorem

Call an arithmetic progression
\[
x<y<z,\qquad x+z=2y,
\]
in \(A\) **far** if
\[
x\le q^{-9}y=\left(\frac23\right)^9y.
\]

For each far progression, orient both endpoint-to-midpoint arcs
\[
x\longrightarrow y,\qquad z\longrightarrow y.
\]
If these arcs admit a proper topological order, then every far progression has its midpoint after both endpoints and is therefore avoided.

Let \(H\) be only the collection of high-to-midpoint arcs
\[
z\longrightarrow y
\]
arising from far progressions.

#### Lemma 6: Every directed path in \(H\) has length at most \(5\)

**Proof.**
Reverse a directed \(H\)-path and write its vertices as
\[
y_0<y_1<\cdots<y_m.
\]
For each \(n<m\), there is \(x_n\in A\) such that
\[
x_n+y_{n+1}=2y_n,\qquad x_n\le q^{-9}y_n.
\]
Therefore
\[
2-q^{-9}\le\frac{y_{n+1}}{y_n}<2.
\]
Put
\[
t_n=\log_q y_n,\qquad \delta_n=t_{n+1}-t_n.
\]
We claim
\[
\frac53<\delta_n<2.
\]

The upper bound follows from \(y_{n+1}<2y_n<q^2y_n\). For the lower bound, note
\[
q^{5/3}<\frac{197}{100}
\]
because, after cubing,
\[
q^5=\frac{243}{32}<\left(\frac{197}{100}\right)^3.
\]
Also
\[
q^{-9}=\left(\frac23\right)^9<\frac3{100}.
\]
Hence
\[
2-q^{-9}>\frac{197}{100}>q^{5/3}.
\]

Write
\[
k_n=\lfloor t_n\rfloor,\qquad \theta_n=t_n-k_n.
\]
Since \(1<\delta_n<2\),
\[
k_{n+1}-k_n\in\{1,2\}.
\]
All \(y_n\) lie in \(A\), so \(k_n\bmod3\in\{1,2\}\). Consequently:

- from residue \(1\), the increment must be \(1\);
- from residue \(2\), the increment must be \(2\).

Thus every two consecutive increments of the \(k_n\)'s sum to \(3\). It follows that
\[
\theta_{n+2}-\theta_n
 =\delta_n+\delta_{n+1}-3
 >\frac13.
\]
A path with six edges would give
\[
\theta_6>\theta_0+1,
\]
impossible because both fractional parts lie in \([0,1)\). Hence \(m\le5\). ∎

For \(v\in A\), define \(d(v)\) to be the maximum length of a directed \(H\)-path ending at \(v\). Lemma 6 gives
\[
0\le d(v)\le5.
\]
This maximum is well-defined: the graph is locally finite, since a predecessor \(z\) of \(v\) satisfies \(v<z<2v\).

For every high arc \(z\to y\),
\[
d(y)\ge d(z)+1.
\]

Define
\[
\Phi(v)=\frac9{16}\log_qv+d(v).
\]

#### Proposition 7: Every oriented far-progression arc strictly increases \(\Phi\)

**Proof.**

For a high arc \(z\to y\),
\[
\begin{aligned}
\Phi(y)-\Phi(z)
&=\frac9{16}\log_q\frac yz+d(y)-d(z)\\
&>1-\frac9{16}\log_q2.
\end{aligned}
\]
Now
\[
\log_q2<\frac{16}{9},
\]
because this is equivalent, after raising to the ninth power, to
\[
2^{25}<3^{16},
\]
and indeed
\[
33\,554\,432<43\,046\,721.
\]
Thus \(\Phi(y)>\Phi(z)\).

For the low arc \(x\to y\), far-ness gives
\[
\log_q\frac yx\ge9.
\]
Since \(d(y)-d(x)\ge-5\),
\[
\Phi(y)-\Phi(x)
\ge\frac9{16}\cdot9-5
=\frac1{16}>0.
\]
∎

#### Theorem 8: The merged set \(A\) has an \(\omega\)-order avoiding every far progression

**Proof.**
Order \(A\) by increasing \(\Phi(v)\), breaking ties by increasing numerical value.

This order has type \(\omega\): since \(d(v)\ge0\),
\[
\Phi(v)\ge\frac9{16}\log_qv,
\]
so every bounded \(\Phi\)-sublevel is finite. Hence every element has finitely many predecessors, and every element is eventually listed.

For each far progression, Proposition 7 places both endpoints before the midpoint. Thus its midpoint is not temporally between its endpoints. ∎

This is a genuine covering order on \(A\), but it controls only the far progressions.

#### Corollary 9: Every uncontrolled progression lies in twelve consecutive scale blocks

If \(x<y<z\) is not far, then
\[
\kappa(z)-\kappa(x)\le11.
\]

**Proof.**
Non-far means \(x>q^{-9}y\), so
\[
\frac yx<q^9.
\]
Also \(z<2y<q^2y\), hence
\[
\frac zx<q^{11}.
\]
Therefore
\[
\log_qz-\log_qx<11,
\]
and the difference of floors is at most \(11\). ∎

Thus the chosen far orientation removes all genuinely unbounded scale memory. What remains is a non-betweenness problem whose hyperedges span at most twelve consecutive \(B_k\)'s.

This does **not** by itself produce a finite-state proof: the blocks have unbounded cardinalities, and reordering the local progressions can create cycles with the already oriented far arcs.

---

### 5. Why “put every mixed midpoint last” fails

One might try to preserve the original increasing block orders on the two tracks
\[
A_1=\bigcup_{k\equiv1\pmod3}B_k,
\qquad
A_2=\bigcup_{k\equiv2\pmod3}B_k,
\]
and orient every progression using both tracks with its midpoint after both endpoints. The following construction rules this out and identifies a forced alternating state.

Put
\[
r=q^{3/2}=\sqrt{\frac{27}{8}},\qquad c=2-r.
\]
Let
\[
C=q^{6/5},\qquad y_n=\lfloor Cr^n\rfloor,
\qquad z_n=y_{n+1},\qquad x_n=2y_n-y_{n+1}.
\]
For all sufficiently large \(n\), these are positive distinct integers and
\[
x_n+z_n=2y_n.
\]

We require the scale location of \(x_n\). Let
\[
s=\log_qc.
\]
Then
\[
-\frac92<s<-\frac{22}{5}.
\]

Indeed, \(c>q^{-9/2}=r^{-3}\) is equivalent to
\[
(2-r)r^3>1.
\]
Using \(r=3\sqrt6/4\), this becomes
\[
324\sqrt6>793,
\]
which follows after squaring from
\[
629856>628849.
\]
Also \(c<1/6\), since \(9\sqrt6>22\), while
\[
\frac16<q^{-22/5}
\]
because \(q^{22/5}<6\), equivalently
\[
3^{17}<2^{27}.
\]

Since floor errors are relatively \(o(1)\),
\[
\log_qy_n=\frac65+\frac32n+o(1).
\]
Consequently, for all sufficiently large \(m\),

- \(y_{2m}\in B_{3m+1}\), hence \(y_{2m}\in A_1\);
- \(y_{2m+1}\in B_{3m+2}\), hence \(y_{2m+1}\in A_2\).

Moreover,
\[
\log_qx_n=\log_qy_n+s+o(1).
\]
The bounds on \(s\) give, eventually,
\[
\begin{array}{c|c|c|c}
n&\kappa(y_n)&\kappa(x_n)&\kappa(z_n)\\ \hline
2m&3m+1&3m-4&3m+2\\
2m+1&3m+2&3m-2&3m+4.
\end{array}
\]
Thus \(x_n\) and \(z_n\) lie in the same original track, with \(x_n\) six block indices before \(z_n\). Also \(x_n\) lies three block indices before \(y_{n-1}\), in that same track.

Suppose a merged order preserves the increasing block order on each original track. Let
\[
e_n:\quad y_{n+1}\triangleleft y_n.
\]
The endpoints \(x_n,z_n\) occur in that order within their track. Therefore avoidance of
\[
(x_n,y_n,z_n)
\]
forces
\[
y_n\triangleleft x_n
\quad\text{or}\quad
z_n\triangleleft y_n.
\]
In the first case,
\[
y_n\triangleleft x_n\triangleleft y_{n-1},
\]
so \(e_{n-1}\) holds. In the second case, \(e_n\) holds. Hence
\[
e_{n-1}\lor e_n
\]
for every sufficiently large \(n\).

On the other hand, \(e_n\) and \(e_{n+1}\) cannot both hold, because that would give
\[
y_{n+2}\triangleleft y_{n+1}\triangleleft y_n,
\]
whereas \(y_n,y_{n+2}\) are in the same track and increasing block order requires
\[
y_n\triangleleft y_{n+2}.
\]
Therefore the \(e_n\)'s must eventually alternate:
\[
e_n,\neg e_{n+1},e_{n+2},\neg e_{n+3},\dots
\]
or the opposite parity.

This has two consequences:

1. Orienting every mixed progression with its midpoint last would require every \(e_n\), which is impossible.
2. The obstruction is not itself a disproof of merging: an alternating pair-swap schedule is compatible with the two track orders. It is evidence that at least two scheduling states are genuinely necessary.

---

### 6. Ledger

#### Proved

1. In every progression, the midpoint and largest term differ by at most two \(3/2\)-scale block indices.
2. No arbitrary \(\omega\)-schedule of contiguous selected blocks can merge the two adjacent tracks.
3. The merged class \(A\) contains neither a full infinite arithmetic progression nor a dyadic affine ray.
4. All far progressions \(x\le(2/3)^9y\) admit a simultaneous midpoint-last orientation with a proper, explicit bounded-depth potential.
5. Every remaining progression lies in at most twelve consecutive scale blocks.
6. A critical asymptotic family forces an alternating two-state rule in any merge preserving the original track block orders.

#### Plausible but unproved

A finite-state scheduler should combine the far-poset potential with orders solving all residual twelve-block interactions. No proof is known that the required states are finite or that all local transition instances are satisfiable.

#### Dead ends established here

1. Treating each \(B_k\) as an atomic block.
2. Assigning one temporal rank to each whole block.
3. Orienting every mixed progression with its midpoint last.
4. Assuming that bounded scale span alone automatically implies an \(\omega\)-order.

## Self-Audit

1. **The far-interaction theorem controls only a restricted family of progressions.**  
   This is the central limitation, not a hidden proof gap. The potential argument is complete for the stated family, but arbitrary local reordering can conflict with its oriented arcs.

2. **The critical-chain construction is asymptotic rather than giving a closed formula for the first valid index.**  
   The scale phases have fixed positive margins from every block boundary, while all floor errors are \(o(1)\). Therefore a finite threshold exists rigorously. The computation below can locate it explicitly.

3. **The twelve-block residual problem has not been converted into a finite library of states.**  
   Although the interaction radius is bounded, each block grows without bound and can carry increasingly complicated precedence patterns. I do not believe bounded radius alone is enough; this is precisely why the route is marked BLOCKED rather than solved.

## Computations To Verify

```python
from functools import lru_cache
from decimal import Decimal, getcontext

# ---------- Exact block arithmetic ----------

def a(k):
    # ceil((3/2)^k)
    return (3**k + 2**k - 1) // 2**k

def block(k):
    return range(a(k), a(k+1))

def kappa(n):
    k = 0
    while 3**(k+1) <= n * 2**(k+1):
        k += 1
    return k

def in_merged(n):
    return kappa(n) % 3 in (1, 2)

# Sanity check n in B_k iff kappa(n) == k
for k in range(20):
    for n in block(k):
        assert kappa(n) == k

# ---------- Lemma 2: fixed-anchor witnesses ----------

# Gap-one selected transitions j ≡ 1 mod 3
for j in range(4, 100):
    y = a(j)
    z = 2*y - 2
    assert y in block(j)
    assert z in block(j+1)

# Gap-two selected transitions j ≡ 2 mod 3
for j in range(5, 100):
    y = a(j+1) - 1
    z = 2*y - 2
    assert y in block(j)
    assert z in block(j+2)

# Restrict to actual consecutive selected pairs
selected = [k for k in range(1, 100) if k % 3 in (1, 2)]
for j, ell in zip(selected[2:], selected[3:]):
    assert ell - j in (1, 2)

# ---------- Exact far-edge predicate ----------

# lambda = (2/3)^9
def is_far(x, y):
    return x * 3**9 <= y * 2**9

def high_predecessors(y):
    """
    z -> y when x = 2y-z is in A and x <= (2/3)^9 y.
    """
    out = []
    for z in range(y + 1, 2*y):
        x = 2*y - z
        if in_merged(x) and in_merged(y) and in_merged(z) and is_far(x, y):
            out.append(z)
    return out

@lru_cache(None)
def depth_with_budget(v, budget):
    if budget == 0:
        return 0
    best = 0
    for z in high_predecessors(v):
        best = max(best, 1 + depth_with_budget(z, budget - 1))
    return best

# The proof says no path of length 6 exists.
for v in range(1, 5000):
    if in_merged(v):
        assert depth_with_budget(v, 6) <= 5

# Verify the potential inequalities on a finite range.
# Floating logs are used only for this numerical check.
import math
q = 1.5

def depth(v):
    return depth_with_budget(v, 6)

def Phi(v):
    return (9/16) * math.log(v, q) + depth(v)

N = 5000
A = [n for n in range(1, N+1) if in_merged(n)]
Aset = set(A)

for y in A:
    for z in range(y+1, min(2*y, N+1)):
        x = 2*y-z
        if x in Aset and z in Aset and is_far(x, y):
            assert Phi(x) < Phi(y) - 1e-10
            assert Phi(z) < Phi(y) - 1e-10

# Verify the residual twelve-block bound.
for y in A:
    for z in range(y+1, min(2*y, N+1)):
        x = 2*y-z
        if x in Aset and z in Aset and not is_far(x, y):
            assert kappa(z) - kappa(x) <= 11

# ---------- Critical alternating chain ----------

getcontext().prec = 100
Q = Decimal(3) / Decimal(2)
r = (Decimal(27) / Decimal(8)).sqrt()
C = ((Q.ln() * Decimal(6) / Decimal(5)).exp())

def floor_decimal(x):
    return int(x.to_integral_value(rounding="ROUND_FLOOR"))

ys = [floor_decimal(C * (r ** n)) for n in range(200)]

first_valid = None
for start in range(10, 150):
    ok = True
    for n in range(start, 190):
        y = ys[n]
        z = ys[n+1]
        x = 2*y-z
        if not (0 < x < y < z):
            ok = False
            break
        if not all(in_merged(v) for v in (x, y, z)):
            ok = False
            break
        if kappa(x) % 3 != kappa(z) % 3:
            ok = False
            break
        if kappa(z) - kappa(x) != 6:
            ok = False
            break
        if kappa(ys[n-1]) - kappa(x) != 3:
            ok = False
            break
    if ok:
        first_valid = start
        break

print("critical-chain threshold found:", first_valid)

# ---------- Exact finite merge CSP preserving original track block order ----------
#
# Requires OR-Tools. Increase K gradually.
#
# This asks for an avoiding order on all merged values in B_0,...,B_{K-1},
# while preserving increasing block order separately on tracks 1 and 2.

def solve_merge_prefix(K, force_far_midpoint_last=False):
    from ortools.sat.python import cp_model

    upper = a(K)
    vals = [n for n in range(1, upper) if in_merged(n)]
    V = set(vals)

    model = cp_model.CpModel()
    p = {v: model.NewIntVar(0, len(vals)-1, f"p_{v}") for v in vals}
    model.AddAllDifferent(list(p.values()))

    # Preserve increasing block order on each original track.
    blocks = {}
    for v in vals:
        blocks.setdefault(kappa(v), []).append(v)

    selected_blocks = sorted(blocks)
    for rclass in (1, 2):
        ks = [k for k in selected_blocks if k % 3 == rclass]
        for k1, k2 in zip(ks, ks[1:]):
            for u in blocks[k1]:
                for v in blocks[k2]:
                    model.Add(p[u] < p[v])

    # Every AP gets midpoint first or midpoint last.
    for x in vals:
        for z in range(x+2, upper):
            if z not in V or (x+z) % 2:
                continue
            y = (x+z)//2
            if y not in V or not (x < y < z):
                continue

            if force_far_midpoint_last and is_far(x, y):
                model.Add(p[x] < p[y])
                model.Add(p[z] < p[y])
                continue

            first = model.NewBoolVar(f"first_{x}_{y}_{z}")
            last = model.NewBoolVar(f"last_{x}_{y}_{z}")

            model.Add(p[y] < p[x]).OnlyEnforceIf(first)
            model.Add(p[y] < p[z]).OnlyEnforceIf(first)
            model.Add(p[x] < p[y]).OnlyEnforceIf(last)
            model.Add(p[z] < p[y]).OnlyEnforceIf(last)
            model.AddBoolOr([first, last])

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 600
    status = solver.Solve(model)

    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        order = sorted(vals, key=lambda v: solver.Value(p[v]))
        return order
    return None

# Suggested runs:
# for K in (9, 12, 15, 18, 21, 24):
#     print(K, solve_merge_prefix(K, False) is not None)
#     print("with far orientation:", solve_merge_prefix(K, True) is not None)
```

## Route Diagnosis

The useful feature of Route 3 is stronger than initially apparent: although an old smallest term can interact with arbitrarily large values, those long-range constraints form a bounded-depth directed graph. The explicit potential
\[
\Phi(v)=\frac9{16}\log_{3/2}v+d(v),\qquad 0\le d(v)\le5,
\]
handles all interactions with \(x\le(2/3)^9y\). This leaves a residual radius of only twelve narrow blocks.

What failed:

- whole-block scheduling is rigorously impossible;
- a single “all mixed midpoints last” state is impossible;
- bounded interaction radius does not automatically imply finitely many boundary signatures.

The precise block is now:

> Can the far-poset orientation be extended by source/sink choices for all progressions spanning at most twelve consecutive \(B_k\)'s, while retaining a proper \(\omega\)-linear extension?

This is still an unproved non-betweenness CSP with unboundedly large windows, so it is not a solution. A fresh attempt should run the finite merge CSP both with and without the far orientation, extract minimal cycle cores, and classify them by:

1. the depth label \(d\in\{0,\dots,5\}\);
2. block residue modulo \(3\);
3. the twelve-block normalized position;
4. the alternating state forced by the critical chain.

If these data close under finitely many transition signatures, they would supply the missing two-track merge lemma. If imposing the far orientation becomes UNSAT at a finite prefix, that would kill this particular orientation but not Route 3 generally; the next step would be to orient only a smaller far subfamily or add several far-orientation states.