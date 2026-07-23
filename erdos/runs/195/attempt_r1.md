STATUS: BLOCKED

## Result

Route 1 does not presently yield a complete solution. I proved that all constraints coming solely from four-term progressions containing the first element—and even a substantially larger family of overlapping dilates—are compatible with an actual order of type \(\omega\). Thus the hoped-for descent cannot be forced from the triples \((a+d,a+2d,a+3d)\), even when all scales and aligned translates are combined. I also obtained a stronger forced-comparison lemma using successive suffix minima on the positive ray, but its conclusions do not assemble into an infinite descent without additional additive structure of essentially the original difficulty.

## Complete Argument

### 1. Exact information supplied by the first element

Translate values so that
\[
\pi(0)=0.
\]
Write \(p(n)=p_\pi(n)\), so \(p(0)=0\).

For every \(d>0\), the progression
\[
0,d,2d,3d
\]
cannot occur in decreasing positional order because \(p(0)\) is the least possible position. Therefore, if there is no monotone four-term AP,
\[
\neg\bigl(p(d)<p(2d)<p(3d)\bigr).
\]
Equivalently,
\[
\boxed{p(2d)<p(d)\quad\text{or}\quad p(3d)<p(2d).}\tag{1}
\]

The progression
\[
-3d,-2d,-d,0
\]
similarly gives
\[
\boxed{p(-2d)<p(-d)\quad\text{or}\quad p(-3d)<p(-2d).}\tag{2}
\]

If \(0\) is one of the two interior terms of a four-term AP, that AP is automatically nonmonotone in position: a strictly increasing sequence of positions has its minimum at its first term, and a strictly decreasing sequence has its minimum at its last term, whereas \(p(0)=0\) occurs internally.

Thus (1) and (2) are exactly all restrictions obtained directly from four-term APs containing the first element.

---

### 2. These first-element restrictions do not force an infinite descent

I give an order of type \(\omega\) satisfying much more than (1).

Define a generating relation \(\triangleleft\) on \(\mathbb N=\{1,2,\ldots\}\) by
\[
(2k-1)d\triangleleft 2kd,
\qquad
(2k+1)d\triangleleft 2kd
\tag{3}
\]
for every \(k,d\ge1\). Let \(P\) be its transitive closure.

In words, among consecutive multiples of \(d\), each odd-indexed multiple is required to occur before both neighboring even-indexed multiples.

#### Lemma 2.1

The partial order \(P\) is acyclic, and every element has only finitely many \(P\)-predecessors.

#### Proof

Let \(\nu_2(n)\) denote the exponent of \(2\) in \(n\). Every generating relation in (3) satisfies
\[
\nu_2((2k\pm1)d)=\nu_2(d)
<
\nu_2(2kd).
\]
Thus \(\nu_2\) strictly increases along every \(P\)-edge, proving acyclicity.

For a fixed \(v\), an immediate predecessor has the form
\[
(q-1)\frac vq
\quad\text{or}\quad
(q+1)\frac vq,
\]
where \(q\) is an even divisor of \(v\). Hence \(v\) has finitely many immediate predecessors.

Moreover, every path ending at \(v\) has length at most \(\nu_2(v)\), since \(\nu_2\) increases by at least one along every edge. Finite branching and bounded depth imply that the entire principal ideal below \(v\) is finite. ∎

#### Lemma 2.2

The partial order \(P\) has a linear extension of order type \(\omega\).

#### Proof

Construct an enumeration recursively. At each stage, among all unused elements having no unused \(P\)-predecessor, output the numerically least one.

There is always an available element: starting from any unused \(x\), its finite principal ideal contains an unused \(P\)-minimal element.

It remains to prove that no integer is postponed forever. Proceed by induction on \(\nu_2(n)\). If \(\nu_2(n)=0\), then \(n\) has no predecessors and is available from the beginning. Once \(n\) is available, the algorithm cannot output an integer larger than \(n\) before outputting \(n\), and there are only finitely many smaller integers.

For general \(n\), every proper predecessor has smaller \(2\)-adic valuation and therefore is eventually output by induction. Since the predecessor set of \(n\) is finite, there is a finite stage after which all of it has appeared. Then \(n\) is available and, as above, can be delayed only by the finitely many smaller unused integers.

Thus every positive integer is eventually output exactly once. The resulting linear extension has order type \(\omega\). ∎

Let
\[
\sigma=(\sigma(0),\sigma(1),\ldots)
\]
be this enumeration.

#### Lemma 2.3

For every \(d,k\ge1\), the progression
\[
kd,(k+1)d,(k+2)d,(k+3)d
\]
is not monotone in \(\sigma\).

#### Proof

If \(n\) is odd, relation (3) gives
\[
nd\triangleleft(n+1)d.
\]
If \(n\) is even, it gives
\[
(n+1)d\triangleleft nd.
\]
Consequently, the three adjacent position comparisons along
\[
kd,(k+1)d,(k+2)d,(k+3)d
\]
alternate:
\[
<,>,<
\quad\text{or}\quad
>,<,>.
\]
They therefore cannot all point in the same direction. ∎

In particular,
\[
d\triangleleft2d
\quad\text{and}\quad
3d\triangleleft2d,
\]
so
\[
p_\sigma(d)<p_\sigma(2d)
\quad\text{and}\quad
p_\sigma(3d)<p_\sigma(2d).
\]
Hence all the first-element disjunctions (1) can consistently be resolved by their second branch.

The relations \(3d\triangleleft2d\) create arbitrarily long finite chains, for example
\[
3^k d
\triangleleft
2\cdot3^{k-1}d
\triangleleft
2^2\cdot3^{k-2}d
\triangleleft\cdots\triangleleft
2^k d.
\]
But these chains lie below different endpoints \(2^k d\); each endpoint still has only finitely many predecessors. This is precisely why rapidly growing forced position bounds do not produce a contradiction.

---

### 3. A genuine permutation of \(\mathbb Z\) satisfying all first-element constraints

Using the enumeration \(\sigma\), define
\[
\Pi(0)=0,\qquad
\Pi(2m+1)=\sigma(m),\qquad
\Pi(2m+2)=-\sigma(m).
\]
This is plainly a bijection \(\mathbb N_0\to\mathbb Z\).

#### Proposition 3.1

No monotone four-term AP containing \(0=\Pi(0)\) occurs in \(\Pi\).

#### Proof

If \(0\) is an interior term, its position is the unique minimum and hence the four positions cannot be monotone.

For
\[
0,d,2d,3d,
\]
the positive-side order gives
\[
p_\Pi(d)<p_\Pi(2d)
\quad\text{and}\quad
p_\Pi(3d)<p_\Pi(2d),
\]
so the positions are not increasing; they cannot be decreasing because \(p_\Pi(0)=0\).

For
\[
-3d,-2d,-d,0,
\]
the negative-side order gives
\[
p_\Pi(-3d)<p_\Pi(-2d),
\]
which rules out the decreasing positional order
\[
p_\Pi(-3d)>p_\Pi(-2d)>p_\Pi(-d)>p_\Pi(0).
\]
The increasing orientation is impossible because it would end at position \(0\). ∎

The same construction also avoids every positive aligned progression
\[
kd,(k+1)d,(k+2)d,(k+3)d
\]
and every negative reflection of such a progression.

Therefore neither the first-element constraints at all scales nor these aligned translated overlaps can force an infinite positional descent.

This is not a counterexample to the original problem. For the specified least-available linear extension, the first positive outputs are
\[
1,3,2,5,7,\ldots,
\]
so
\[
1,3,5,7
\]
already occurs in increasing positional order. This progression is “unaligned”: its common difference \(2\) does not divide its first term \(1\).

---

### 4. A stronger consequence using suffix minima

The preceding obstruction shows that one must use APs not containing the global first term. The following is the strongest descent statement I obtained in that direction.

Set
\[
x_n=p_\pi(n),\qquad n\ge0,
\]
after the normalization \(\pi(0)=0\). Define recursively
\[
r_0=0,\qquad
r_{j+1}=\operatorname*{arg\,min}_{n>r_j}x_n.
\]
This minimum exists because the nonempty set
\[
\{x_n:n>r_j\}
\]
is a subset of \(\mathbb N_0\).

#### Lemma 4.1

The sequence satisfies
\[
r_0<r_1<r_2<\cdots,
\qquad
x_{r_0}<x_{r_1}<x_{r_2}<\cdots,
\]
and each \(r_j\) is a suffix minimum:
\[
x_{r_j}<x_n\qquad(n>r_j).
\]

#### Proof

The index inequalities follow from the definition. Since \(r_{j+1}>r_j\) and \(r_j\) is the minimum on its suffix,
\[
x_{r_j}<x_{r_{j+1}}.
\]
The definition of \(r_{j+1}\) also directly gives
\[
x_{r_{j+1}}<x_n\qquad(n>r_{j+1}).
\]
Induction proves all claims. ∎

#### Lemma 4.2

If the permutation has no monotone four-term AP, then for every \(i<j\),
\[
\boxed{
x_{\,3r_j-2r_i}<x_{\,2r_j-r_i}.
}
\tag{4}
\]

#### Proof

Put
\[
h=r_j-r_i>0.
\]
The four indices
\[
r_i,\quad r_i+h=r_j,\quad r_i+2h=2r_j-r_i,\quad
r_i+3h=3r_j-2r_i
\]
form a four-term arithmetic progression.

By Lemma 4.1,
\[
x_{r_i}<x_{r_j}.
\]
Since \(2r_j-r_i>r_j\) and \(r_j\) is a suffix minimum,
\[
x_{r_j}<x_{2r_j-r_i}.
\]
Thus the first three positions are increasing. Avoidance of an increasing four-term AP forces the final comparison to be a descent:
\[
x_{3r_j-2r_i}<x_{2r_j-r_i}.
\]
∎

#### Corollary 4.3

The set
\[
R=\{r_0,r_1,r_2,\ldots\}
\]
contains no four-term arithmetic progression.

#### Proof

Positions are strictly increasing along the numerically increasing sequence \(R\). Four elements of \(R\) forming an AP would therefore give an increasing monotone four-term AP in the values. ∎

Lemma 4.2 produces infinitely many genuine forced descents. The unresolved problem is that their upper endpoints
\[
2r_j-r_i
\]
vary with \(i,j\). No fixed element is thereby shown to have infinitely many predecessors, and no nested infinite descent follows without substantial additive structure in \(R\). Corollary 4.3 allows \(R\) to be very sparse; for example, powers of \(2\) contain no three-term AP, let alone a four-term one.

This is the precise point at which Route 1 becomes blocked.

## Self-Audit

1. **Fairness of the linear-extension construction.**  
   An infinite topological sort can easily omit elements. Here it does not because every element has a finite principal ideal, and once those predecessors have appeared, numerical least-priority allows only finitely many smaller distractions. This is proved explicitly in Lemma 2.2.

2. **The orientation on the negative ray.**  
   Reversal errors are a common trap. For \(-3d,-2d,-d,0\), the forbidden decreasing orientation would require
   \[
   p(-3d)>p(-2d)>p(-d)>0.
   \]
   The construction instead has \(p(-3d)<p(-2d)\), so that orientation is genuinely excluded.

3. **Scope of the blockage claim.**  
   The construction does not prove that every sophisticated first-term argument must fail. It proves only that the direct dilation constraints, and even all aligned translated constraints, have an \(\omega\)-model. A successful Route 1 proof could still use unaligned APs in an essential way; Lemma 4.2 is one such attempt. I therefore report BLOCKED rather than claiming Route 1 is impossible.

## Computations To Verify

The following generates the linear extension used above and checks finite prefixes.

```python
from math import isqrt

def divisors(n):
    out = set()
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.add(d)
            out.add(n // d)
    return out

def immediate_predecessors(v):
    """
    u precedes v when v = q*d with q even and
    u = (q-1)*d or (q+1)*d.
    """
    out = set()
    for q in divisors(v):
        if q % 2 == 0:
            d = v // q
            out.add((q - 1) * d)
            out.add((q + 1) * d)
    return out

def sigma_prefix(M):
    used = set()
    out = []
    for _ in range(M):
        n = 1
        while n in used or not immediate_predecessors(n).issubset(used):
            n += 1
        out.append(n)
        used.add(n)
    return out

def integer_prefix(M):
    s = sigma_prefix(M)
    out = [0]
    for x in s:
        out.extend([x, -x])
    return out

def four_ap_violations(word):
    pos = {x: i for i, x in enumerate(word)}
    vals = set(word)
    hi = max(vals)
    violations = []

    for a in vals:
        for d in range(1, (hi - a) // 3 + 1):
            xs = [a + i*d for i in range(4)]
            if all(x in vals for x in xs):
                ps = [pos[x] for x in xs]
                inc = all(ps[i] < ps[i+1] for i in range(3))
                dec = all(ps[i] > ps[i+1] for i in range(3))
                if inc or dec:
                    violations.append((a, d, xs, ps))
    return violations

s = sigma_prefix(30)
print(s)
assert s[:5] == [1, 3, 2, 5, 7]

# Verify every completed generating relation.
p = {x: i for i, x in enumerate(s)}
for v in s:
    for u in immediate_predecessors(v):
        if u in p:
            assert p[u] < p[v]

# The construction is deliberately not a global counterexample.
w = integer_prefix(30)
pw = {x: i for i, x in enumerate(w)}
assert pw[1] < pw[3] < pw[5] < pw[7]
print(four_ap_violations(w)[:20])
```

A finite SAT test separating the first-element constraints from the full problem can be run with Z3:

```python
from z3 import Int, Distinct, And, Or, Not, Solver, sat

def finite_order_instance(N, full_constraints=False):
    S = list(range(-N, N + 1))
    rank = {x: Int(f"r_{x}") for x in S}
    sol = Solver()

    sol.add(Distinct(*[rank[x] for x in S]))
    for x in S:
        sol.add(0 <= rank[x], rank[x] < len(S))
    sol.add(rank[0] == 0)

    for a in S:
        d = 1
        while a + 3*d <= N:
            xs = [a + i*d for i in range(4)]
            if all(x in rank for x in xs):
                if full_constraints or 0 in xs:
                    inc = And(*[
                        rank[xs[i]] < rank[xs[i+1]]
                        for i in range(3)
                    ])
                    dec = And(*[
                        rank[xs[i]] > rank[xs[i+1]]
                        for i in range(3)
                    ])
                    sol.add(Not(Or(inc, dec)))
            d += 1

    # Select the consistent branch used in the proof.
    for d in range(1, N // 3 + 1):
        sol.add(rank[d] < rank[2*d])
        sol.add(rank[3*d] < rank[2*d])
        sol.add(rank[-d] < rank[-2*d])
        sol.add(rank[-3*d] < rank[-2*d])

    return sol, rank

for N in range(3, 20):
    sol, rank = finite_order_instance(N, full_constraints=False)
    assert sol.check() == sat
```

For further Route 1 searches, the SAT instance should use `full_constraints=True` and affine sets containing primitive progressions with coprime start and difference, rather than only multiplicative sets generated by \(2\) and \(3\).

## Route Diagnosis

**Proved ledger**

- Four-APs containing the first element yield exactly the disjunctions (1) and (2).
- Those disjunctions at every scale are compatible with an order of type \(\omega\).
- Even all aligned progressions
  \[
  kd,(k+1)d,(k+2)d,(k+3)d
  \]
  can simultaneously be made nonmonotone in such an order.
- Successive suffix minima force the comparisons (4), and their index set is four-AP-free.

**Dead ends**

- Selecting one descent from each anchored triple does not force an infinite path. A \(2\)-adic finite-ideal order realizes all selections without any infinite descent.
- Arbitrarily long chains such as
  \[
  2^k d\succ2^{k-1}3d\succ\cdots\succ3^k d
  \]
  only force the starting positions to grow with \(k\); they do not lie below a fixed element.
- Hierarchical parity ordering handles APs crossing valuation levels but leaves APs entirely inside the odd numbers. The affine map \(n\mapsto2n+1\) identifies that odd layer with another copy of the original one-sided problem. This is a reduction to an unproved statement of comparable strength.
- The suffix-minimum method generates many descents, but sparse record sets prevent them from automatically concatenating.

**Plausible but unproved**

- A successful proof may show that consistently handling primitive, cross-residue APs forces the hierarchical residue construction to give some element infinitely many predecessors.
- There may be a finite affine configuration, involving coprime start and difference rather than only dilates of \(0,d,2d,3d\), that forces several descents below one fixed target.

**Recommended fresh attempt**

The most promising continuation is Route 6 feeding into Route 3: use SAT on affine grids containing primitive APs such as \(1,3,5,7\) together with several overlapping translates and dilates, and search specifically for certified implications forcing many distinct predecessors of one designated vertex. Multiplicatively closed sets \(\{2^i3^j\}\) alone should be avoided—the finite-ideal construction above explains why they can exhibit arbitrarily long but harmless finite descent patterns.