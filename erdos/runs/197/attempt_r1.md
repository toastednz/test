STATUS: BLOCKED

## Result

I did not solve Erdős Problem #197. I proved that the most direct 2-adic implementation of the finite parity recursion cannot work—not merely with two colors, but with any finite number of colors—because restrictions of oriented least-significant-bit lexicographic orders cannot all have order type \(\omega\). Valuation colorings such as \(v_2(n)\bmod 2\) also fail to simplify the problem: each color contains an affine copy of all nonnegative integers, so such a construction would already imply a one-set solution. A more promising digital construction colors dyadic shells alternately and reduces the problem exactly to a family of finite constrained-permutation problems. I obtained a simple stronger finite “boundary lemma” which would imply a complete solution and verified it by hand through shell size \(8\), but I could not prove it for all powers of two. The natural parity-recursive induction is rigorously ruled out for this lemma and already fails the exact shell constraints at shell \([16,31]\).

## Complete Argument

### 1. The direct 2-adic lexicographic construction avoids progressions locally

It is convenient here to use \(\mathbb N_0=\{0,1,2,\dots\}\).

For \(n\in\mathbb N_0\), write
\[
n=\sum_{j\ge 0}\varepsilon_j(n)2^j,
\qquad \varepsilon_j(n)\in\{0,1\},
\]
with all but finitely many digits zero.

At every finite binary word \(w\), choose one of its two children \(w0,w1\) to come first. This defines an oriented lexicographic order read from the least significant bit: two distinct integers are compared at their first differing binary digit, using the chosen orientation at their common lower-bit prefix.

#### Lemma 1: First differing bit of an arithmetic progression

Let
\[
x<y<z,\qquad y-x=z-y=d>0,
\]
and let \(q=v_2(d)\). Then:

1. \(x,y,z\) have identical binary digits below position \(q\);
2. at position \(q\), \(x\) and \(z\) have the same digit;
3. at position \(q\), \(y\) has the opposite digit.

**Proof.**
Because \(2^q\mid d\), the three numbers are congruent modulo \(2^q\), proving the first assertion. Since \(d/2^q\) is odd,
\[
y=x+d\not\equiv x\pmod{2^{q+1}},
\]
so the \(q\)-th digit is toggled. On the other hand,
\[
z=x+2d\equiv x\pmod{2^{q+1}},
\]
so \(x\) and \(z\) have the same \(q\)-th digit. ∎

#### Lemma 2: Every oriented 2-adic lexicographic order avoids monotone 3-APs

In any such order, the numerical midpoint \(y\) of a progression \(x,y,z\) is not positionally between \(x\) and \(z\).

**Proof.**
Use \(q=v_2(y-x)\) from Lemma 1. The three numbers have the same lower-bit prefix of length \(q\). At the next split, \(x,z\) lie in one child cylinder and \(y\) lies in the other.

Every element of one child cylinder precedes every element of the other child cylinder in an oriented lexicographic order. Hence \(x,z\) are both on the same side of \(y\). ∎

This exactly recovers the mechanism behind the finite parity-recursive lemma.

---

### 2. No finite partition can turn these 2-adic lexicographic orders into enumerations

The local success above cannot be upgraded to order type \(\omega\) by splitting into finitely many colors.

For a finite binary word \(w\), let
\[
C_w=\{n\in\mathbb N_0:\text{the low-order digits of }n\text{ begin with }w\}.
\]
Equivalently, \(C_w\) is a residue class modulo \(2^{|w|}\).

#### Lemma 3: At most one child of any cylinder can contain infinitely many elements

Let \(A\subseteq\mathbb N_0\), and suppose the restriction to \(A\) of an oriented 2-adic lexicographic order has the property that every element has only finitely many predecessors. Then, for every word \(w\), at most one of
\[
A\cap C_{w0},\qquad A\cap C_{w1}
\]
is infinite.

**Proof.**
One of the two child cylinders is ordered entirely before the other. If both intersections were infinite, every element of the later child would have all infinitely many elements of the earlier child as predecessors. ∎

#### Corollary 4: At each depth, \(A\) is infinite in at most one residue class

For every \(k\), there is at most one word \(w\in\{0,1\}^k\) for which \(A\cap C_w\) is infinite.

**Proof.**
At depth one this is Lemma 3. Inductively, finite cylinders have only finite descendants, while the unique possible infinite cylinder has at most one infinite child. ∎

#### Theorem 5: No finite partition works through oriented 2-adic lexicographic orders

There is no finite partition
\[
\mathbb N_0=A_1\sqcup\cdots\sqcup A_r
\]
such that, for every \(i\), some oriented 2-adic lexicographic order restricts to an order on \(A_i\) in which every element has finitely many predecessors.

The orientations may be different for different colors.

**Proof.**
Choose \(k\) with \(2^k>r\). There are \(2^k\) residue classes modulo \(2^k\), each infinite. Since each such class is the union of its intersections with the finitely many \(A_i\), at least one of those intersections must be infinite.

Thus the \(2^k\) residue classes must collectively account for at least \(2^k\) color–residue pairs having infinite intersection. But Corollary 4 says that each color can have infinite intersection with at most one residue class at depth \(k\). There can therefore be at most \(r\) such residue classes, contradicting \(2^k>r\). ∎

This is a complete obstruction to the most literal infinite version of the finite parity recursion.

---

### 3. Why coloring by \(v_2(n)\) does not simplify the problem

Consider any coloring which places an entire exact valuation layer
\[
L_r=\{2^r(2m+1):m\in\mathbb N_0\}
\]
inside one color class. This includes the natural coloring \(v_2(n)\bmod 2\).

#### Lemma 6: Sequenceability of one valuation layer implies a one-set solution

If a color class containing \(L_r\) has an avoiding enumeration, then \(\mathbb N_0\) itself has an avoiding enumeration.

**Proof.**
Restrict the color enumeration to \(L_r\). This subsequence still has order type \(\omega\), lists every element of \(L_r\) once, and remains progression-avoiding.

The affine bijection
\[
f(m)=2^r(2m+1)
\]
preserves 3-term arithmetic progressions:
\[
f(a)+f(c)=2f(b)
\iff
a+c=2b.
\]
Transporting the induced order on \(L_r\) through \(f\) gives an avoiding enumeration of \(\mathbb N_0\). ∎

Thus valuation coloring does not use the two colors to divide the difficult affine structure: every exact valuation layer retains the entire one-set problem.

---

### 4. An exact dyadic-shell reduction

The preceding obstruction applies only to full least-significant-bit lexicographic orders. A different digital construction can retain finite blocks and therefore automatically have order type \(\omega\).

For \(L\ge 0\), define the dyadic shell
\[
D_L=[2^L,2^{L+1})\cap\mathbb N.
\]
Color the entire shell by
\[
\chi(n)=L\bmod 2,\qquad n\in D_L.
\]
For each color, enumerate its shells in increasing \(L\), using some finite permutation \(\pi_L\) inside each shell.

This automatically gives two genuine enumerations: every shell is finite, and every integer lies in exactly one shell.

Define
\[
E_L=D_{L-2}\cup D_{L-4}\cup\cdots,
\]
omitting shells with negative indices.

#### Proposition 7: Exact characterization of the required shell permutations

The resulting two enumerations avoid monotone 3-term progressions if and only if every \(\pi_L\) satisfies:

1. \(\pi_L\) avoids every 3-term progression lying wholly in \(D_L\);
2. whenever \(y<z\) lie in \(D_L\) and
   \[
   x=2y-z\in E_L,
   \]
   the element \(z\) precedes \(y\) in \(\pi_L\).

**Proof.**

Let \(x<y<z\) be monochromatic, with \(x+z=2y\). Let \(L_y,L_z\) be the shell indices of \(y,z\). Since
\[
z=2y-x<2y,
\]
we have
\[
L_z\le L_y+1.
\]
Also \(L_z\ge L_y\) because \(z>y\). Monochromaticity gives
\[
L_z\equiv L_y\pmod 2.
\]
Hence
\[
L_z=L_y=:L.
\]

If \(x\in D_L\), all three terms lie in \(D_L\), and condition 1 is exactly what is required.

Otherwise the shell index of \(x\) is congruent to \(L\) modulo \(2\) and at most \(L-2\), so \(x\in E_L\). In the global color enumeration, \(x\) precedes every member of \(D_L\). Thus the midpoint \(y\) avoids lying between \(x,z\) exactly when \(z\) precedes \(y\). This is condition 2.

The same reasoning proves necessity. ∎

This converts the infinite problem, for this particular coloring, into a uniform family of finite constrained-ordering problems.

---

### 5. A stronger finite boundary lemma would solve the problem

Write \(M=2^L\), and identify \(D_L=[M,2M)\) with offsets \([0,M)\).

Suppose \(y=M+a\), \(z=M+b\), and
\[
x=2y-z=M+2a-b\in E_L.
\]
Since \(x<M/2\) and \(b\le M-1\),
\[
x=M+2a-b\ge 2a+1,
\]
so
\[
a<M/4.
\]
Also \(x<M/2\) gives
\[
b>M/2+2a\ge M/2.
\]
Therefore every required cross-shell comparison has
\[
y\in [M,5M/4),\qquad
z\in [3M/2,2M).
\]

Consequently, the following uniform finite statement would solve the original problem.

#### Candidate Boundary Lemma

For every power of two \(M\), there is an avoiding permutation \(P_M\) of
\[
\{0,1,\dots,M-1\}
\]
such that every element of
\[
U_M=[M/2,M)
\]
precedes every element of
\[
Q_M=[0,M/4).
\]

Indeed, translate \(P_M\) to the shell \(D_L\). The boundary condition implies condition 2 of Proposition 7, while avoidance inside \(P_M\) gives condition 1.

I have not proved this lemma.

It does hold for \(M\le 8\). Witnesses are:

\[
\begin{array}{c|l}
M & P_M\\ \hline
1 &(0)\\
2 &(1,0)\\
4 &(2,3,0,1)\\
8 &(2,6,4,5,7,0,1,3).
\end{array}
\]

For \(M=8\), the position map is
\[
p(0)=6,\ p(1)=7,\ p(2)=1,\ p(3)=8,\ 
p(4)=3,\ p(5)=4,\ p(6)=2,\ p(7)=5.
\]
The twelve progressions in \([0,7]\) have positional triples:

\[
\begin{array}{c|c}
(0,1,2)&(6,7,1)\\
(1,2,3)&(7,1,8)\\
(2,3,4)&(1,8,3)\\
(3,4,5)&(8,3,4)\\
(4,5,6)&(3,4,2)\\
(5,6,7)&(4,2,5)\\
(0,2,4)&(6,1,3)\\
(1,3,5)&(7,8,4)\\
(2,4,6)&(1,3,2)\\
(3,5,7)&(8,4,5)\\
(0,3,6)&(6,8,2)\\
(1,4,7)&(7,3,5).
\end{array}
\]
In each row the middle coordinate is outside the interval determined by the first and third. Also \(4,5,6,7\) all precede \(0,1\), as required.

These small witnesses are not meaningful evidence of a uniform theorem without an induction or other proof.

---

### 6. The natural parity recursion cannot prove the boundary lemma

A parity-recursive finite order begins with either all even elements or all odd elements.

For \(M\ge 8\), both \(U_M\) and \(Q_M\) contain even and odd elements. If the even block comes first, choose an odd \(u\in U_M\) and an even \(q\in Q_M\); then \(q\) precedes \(u\), contrary to the boundary condition. If the odd block comes first, choose an even \(u\in U_M\) and an odd \(q\in Q_M\), giving the same contradiction.

Thus no first-level parity-block recursion can establish the candidate boundary lemma for \(M\ge8\).

There is an even sharper failure for the exact shell constraints.

Take \(L=4\), so \(D_4=[16,31]\) and
\[
E_4=D_2\cup D_0=\{4,5,6,7\}\cup\{1\}.
\]
The progressions
\[
1,16,31
\quad\text{and}\quad
4,17,30
\]
force respectively
\[
31\prec 16,\qquad 30\prec17
\]
inside \(D_4\).

If the even elements of \(D_4\) form the first parity block, then \(16\prec31\), contradicting the first requirement. If the odd elements form the first block, then \(17\prec30\), contradicting the second. Therefore no parity-contiguous order of \(D_4\) satisfies even the exact constraints of Proposition 7.

---

### 7. Explicit failures of several natural digital formulas

Let shells be ordered increasingly and let each shell be ordered by the bit reversal of its offset.

Several obvious color/key combinations fail on very small explicit progressions:

- Color by shell parity, standard bit-reversal order:
  \[
  1,16,31
  \]
  is monochromatic and occurs positionally in that order.

- Color by shell parity, reversed bit-reversal order:
  \[
  4,17,30
  \]
  is monochromatic and occurs positionally in that order.

- Color by
  \[
  \lfloor\log_2 n\rfloor+v_2(n)\pmod2
  \]
  with standard bit reversal:
  \[
  5,17,29
  \]
  is a monochromatic positional progression.

- The same coloring with reversed bit reversal fails on
  \[
  4,19,34.
  \]

- Color by \(v_2(n)\bmod2\), standard bit reversal:
  \[
  1,16,31
  \]
  fails.

- Color by \(v_2(n)\bmod2\), reversed bit reversal:
  \[
  1,5,9
  \]
  fails because the three numbers lie in successively encountered shells.

These examples rule out the most immediate combinations of shell order, valuation, and bit reversal.

---

### Ledger

**Proved:**

1. Every oriented least-significant-bit lexicographic order avoids monotone 3-APs.
2. No finite partition can make restrictions of such orders all have finite predecessor sets.
3. A color containing an exact \(2\)-adic valuation layer would yield a one-set solution.
4. Proposition 7 exactly characterizes the alternating-dyadic-shell architecture.
5. The candidate boundary lemma implies a complete affirmative solution.
6. The boundary lemma holds for \(M\le8\).
7. Parity-contiguous recursion cannot prove it for \(M\ge8\), and fails the exact shell constraints at \(L=4\).

**Plausible but unproved:**

- The exact finite constraints in Proposition 7 may be satisfiable for every \(L\).
- The stronger candidate boundary lemma may hold for every power of two. The evidence \(M\le8\) is far too small to justify confidence.

**Dead ends:**

- Full 2-adic lexicographic orders: impossible for every finite number of colors.
- Pure valuation coloring: contains an unsimplified affine copy of the one-set problem.
- Alternating shells plus standard or reversed bit reversal: explicit counterexamples.
- Parity-recursive construction of the constrained shell permutations: impossible already at the first parity split.

## Self-Audit

1. **The 2-adic impossibility theorem concerns only genuine oriented lexicographic orders with dyadic cylinders as intervals.** More flexible digital rank functions may interleave the child cylinders and are not excluded. Within the stated model, however, the proof is exact: two infinite child cylinders immediately give infinitely many predecessors in the later child.

2. **The candidate boundary lemma is the main unresolved step and may be false.** I do not rely on it as a theorem; only the implication from it to the original problem is claimed. That implication follows rigorously from the shell-index argument and the inequalities locating \(y\) in the lower quarter and \(z\) in the upper half.

3. **The positive evidence for the boundary lemma stops at \(M=8\).** This is mathematically weak. The \(M=8\) witness itself is reliable because all twelve progressions are explicitly listed and checked, but it gives no induction and should not be extrapolated.

## Computations To Verify

The following Python first verifies finite permutations and the hand witnesses.

```python
def is_good_order(order):
    pos = {x: i for i, x in enumerate(order)}
    if len(pos) != len(order):
        return False
    S = set(order)

    for x in S:
        d = 1
        while x + 2*d <= max(S):
            y, z = x + d, x + 2*d
            if y in S and z in S:
                if min(pos[x], pos[z]) < pos[y] < max(pos[x], pos[z]):
                    return False
            d += 1
    return True


def boundary_ok(order):
    M = len(order)
    pos = {x: i for i, x in enumerate(order)}
    U = [x for x in range(M) if 2*x >= M]
    Q = [x for x in range(M) if 4*x < M]
    return all(pos[u] < pos[q] for u in U for q in Q)


witnesses = {
    1: [0],
    2: [1, 0],
    4: [2, 3, 0, 1],
    8: [2, 6, 4, 5, 7, 0, 1, 3],
}

for M, order in witnesses.items():
    assert sorted(order) == list(range(M))
    assert is_good_order(order)
    assert boundary_ok(order)
```

The most important computation is to test the exact shell constraints and the stronger boundary lemma for \(M=16,32,64,\dots\). Here is an OR-Tools CP-SAT model.

```python
from ortools.sat.python import cp_model

def add_nonbetween(model, px, py, pz, name):
    low = model.NewBoolVar(name + "_low")
    high = model.NewBoolVar(name + "_high")

    model.Add(py < px).OnlyEnforceIf(low)
    model.Add(py < pz).OnlyEnforceIf(low)

    model.Add(py > px).OnlyEnforceIf(high)
    model.Add(py > pz).OnlyEnforceIf(high)

    model.AddBoolOr([low, high])


def prior_same_color_shell(x, L):
    if x <= 0:
        return False
    lx = x.bit_length() - 1
    return lx < L and ((lx - L) % 2 == 0)


def solve_shell(L, impose_exact=True, impose_strong_boundary=False,
                time_limit=300):
    M = 1 << L
    vals = list(range(M, 2*M))

    model = cp_model.CpModel()
    p = {x: model.NewIntVar(0, M-1, f"p_{x}") for x in vals}
    model.AddAllDifferent([p[x] for x in vals])

    # Internal progression constraints.
    counter = 0
    for x in vals:
        d = 1
        while x + 2*d < 2*M:
            y, z = x + d, x + 2*d
            add_nonbetween(model, p[x], p[y], p[z], f"ap_{counter}")
            counter += 1
            d += 1

    # Exact constraints from Proposition 7.
    if impose_exact:
        for y in vals:
            for z in range(y + 1, 2*M):
                x = 2*y - z
                if prior_same_color_shell(x, L):
                    model.Add(p[z] < p[y])

    # Stronger boundary condition.
    if impose_strong_boundary:
        Q = [x for x in vals if 4*(x - M) < M]
        U = [x for x in vals if 2*(x - M) >= M]
        for u in U:
            for q in Q:
                model.Add(p[u] < p[q])

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = 8

    status = solver.Solve(model)
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        order = sorted(vals, key=lambda x: solver.Value(p[x]))
        return "SAT", order
    if status == cp_model.INFEASIBLE:
        return "UNSAT", None
    return "UNKNOWN", None


for L in range(1, 8):
    print("L =", L)
    print("exact:", solve_shell(L, impose_exact=True,
                                impose_strong_boundary=False))
    print("strong:", solve_shell(L, impose_exact=False,
                                 impose_strong_boundary=True))
```

A finite `UNSAT` result for the exact constraints would rigorously kill the alternating-shell architecture once independently certified. A `SAT` witness sequence should be checked using:

```python
def check_exact_shell_order(L, order):
    M = 1 << L
    assert sorted(order) == list(range(M, 2*M))
    assert is_good_order(order)

    pos = {x: i for i, x in enumerate(order)}
    for y in range(M, 2*M):
        for z in range(y + 1, 2*M):
            x = 2*y - z
            if prior_same_color_shell(x, L):
                assert pos[z] < pos[y]
    return True
```

The explicit counterexamples to the simple digital formulas can be checked with:

```python
def v2(n):
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r

def bit_reverse(x, bits):
    ans = 0
    for _ in range(bits):
        ans = (ans << 1) | (x & 1)
        x >>= 1
    return ans

def shell_key(n, reverse=False):
    L = n.bit_length() - 1
    M = 1 << L
    r = bit_reverse(n - M, L)
    return (L, -r if reverse else r)

def is_bad_triple(x, y, z, color, reverse=False):
    assert x + z == 2*y
    if not (color(x) == color(y) == color(z)):
        return False
    kx, ky, kz = shell_key(x, reverse), shell_key(y, reverse), shell_key(z, reverse)
    return min(kx, kz) < ky < max(kx, kz)

shell_parity = lambda n: (n.bit_length() - 1) & 1
valuation_parity = lambda n: v2(n) & 1
shell_plus_valuation = lambda n: ((n.bit_length() - 1) + v2(n)) & 1

assert is_bad_triple(1, 16, 31, shell_parity, reverse=False)
assert is_bad_triple(4, 17, 30, shell_parity, reverse=True)
assert is_bad_triple(5, 17, 29, shell_plus_valuation, reverse=False)
assert is_bad_triple(4, 19, 34, shell_plus_valuation, reverse=True)
assert is_bad_triple(1, 16, 31, valuation_parity, reverse=False)
assert is_bad_triple(1, 5, 9, valuation_parity, reverse=True)
```

## Route Diagnosis

The first-differing-bit mechanism works perfectly for local avoidance, but preserving full dyadic cylinder contiguity is fundamentally incompatible with finite-color \(\omega\)-enumerations. The best remaining digital route I found is the alternating-dyadic-shell construction. It removes starvation automatically and reduces the infinite problem to explicit finite constraints, but it is currently blocked at a uniform constrained finite-permutation theorem. That theorem is not supplied by the ordinary finite parity lemma, and the natural parity induction is provably incompatible with the constraints.

A fresh attempt should first run the exact and strong CP-SAT searches for \(M=16,32,64\). If the stronger boundary lemma survives, the witnesses should be mined for a finite-state recursive substitution allowing parity children to interleave. If the stronger lemma fails but the exact constraints survive, the correct induction will need several boundary states rather than a single upper-half-before-lower-quarter state. If the exact constraints fail at some finite shell, alternating shell coloring should be abandoned. Recovering the known three-color construction is also important: the emerging need for several recursive boundary states may explain why three colors are known while two remain difficult.