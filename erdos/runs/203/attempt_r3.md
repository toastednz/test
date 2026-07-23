STATUS: BLOCKED

## Result

Route 3 yields useful exact obstructions but not a covering certificate. I prove: (i) for fixed \(A\), the maximum possible covering mass obtainable from any product grid with \(o_2(p)\mid A\) is an explicitly computable quantity \(C_2(A)\); (ii) \(C_2(60)=4529/6600<1\), so no choice of \(B\) can make \(A=60\) support a cover; and (iii) any candidate pool containing \(5,7,11\) with total mass below \(43/40\) is impossible, because the three corresponding cosets necessarily lose at least \(3/40\) of mass through forced overlap. Consequently, a fully factored torus with \(60\mid A,B\) and mass below \(1.075\) cannot work. This rigorously explains why the reported \(5040\)-smooth pools of mass about \(1.02\)–\(1.03\) cannot cover, provided that quoted mass is for the complete specified pool. No proof or disproof of the original Erdős problem is obtained.

## Complete Argument

### 1. Exact capacity of a product grid

For positive integers \(A,B\), define the available prime set
\[
S(A,B)=
\left\{
p\ge 5:\ p\text{ prime},\ 
o_2(p)\mid A,\ 
o_3(p)\mid B
\right\}.
\]
Equivalently,
\[
S(A,B)=
\left\{
p\ge5:\ p\mid \gcd(2^A-1,3^B-1)
\right\},
\]
where only distinct prime divisors matter.

Indeed, for \(p\ge5\),
\[
p\mid2^A-1\iff o_2(p)\mid A,
\qquad
p\mid3^B-1\iff o_3(p)\mid B.
\]

Let
\[
h_p=\operatorname{lcm}(o_2(p),o_3(p)).
\]
If \(p\in S(A,B)\), the homomorphism
\[
\phi_p:\mathbb Z_A\times\mathbb Z_B\longrightarrow H_p,
\qquad
(k,\ell)\longmapsto 2^k3^\ell\pmod p
\]
is well-defined and surjective. Since \(|H_p|=h_p\), every fiber has size
\[
\frac{AB}{h_p}.
\]
Thus every target coset supplied by \(p\) occupies exactly the fraction \(1/h_p\) of the grid.

It follows from the union bound that a necessary condition for a product-grid covering is
\[
W(A,B):=\sum_{p\in S(A,B)}\frac1{h_p}\ge1.
\tag{1}
\]

This remains necessary if the desired cover is initially stated only for \(k,\ell\ge1\): every residue pair modulo \(A,B\) has a representative with both coordinates positive.

For fixed \(A\), define the one-sided capacity
\[
C_2(A)=
\sum_{\substack{p\ge5\\p\mid2^A-1}}
\frac1{\operatorname{lcm}(o_2(p),o_3(p))}.
\tag{2}
\]
Then
\[
W(A,B)\le C_2(A)
\tag{3}
\]
for every \(B\). Moreover, equality is attained for some \(B\): take \(B\) to be the least common multiple of \(o_3(p)\) over the finitely many primes \(p\ge5\) dividing \(2^A-1\).

Thus \(C_2(A)<1\) conclusively rules out that value of \(A\), regardless of how \(B\) is enlarged. There is an analogous quantity \(C_3(B)\).

---

### 2. The entire \(A=60\) branch is impossible

The complete factorization is
\[
2^{60}-1
=
3^2\cdot5^2\cdot7\cdot11\cdot13\cdot31\cdot41
\cdot61\cdot151\cdot331\cdot1321.
\tag{4}
\]
Multiplication gives \(2^{60}-1\), and all displayed factors are prime; the largest is \(1321\), whose primality is checked by trial division by primes at most \(36\).

The relevant order table is
\[
\begin{array}{c|c|c|c}
p&o_2(p)&o_3(p)&h_p\\ \hline
5&4&4&4\\
7&3&6&6\\
11&10&5&10\\
13&12&3&12\\
31&5&30&30\\
41&20&8&40\\
61&60&10&60\\
151&15&50&150\\
331&30&330&330\\
1321&60&55&660
\end{array}
\tag{5}
\]

For completeness, the following residues certify the asserted orders. In each entry of order \(n\), the full congruence \(a^n\equiv1\pmod p\) holds, and the listed values are \(a^{n/q}\not\equiv1\) for every prime \(q\mid n\):

\[
\begin{array}{c|l|l}
p&\text{checks for }2&\text{checks for }3\\ \hline
5&2^2=-1&3^2=-1\\
7&2^1=2&3^3=-1,\ 3^2=2\\
11&2^5=-1,\ 2^2=4&3^1=3\\
13&2^6=-1,\ 2^4=3&3^1=3\\
31&2^1=2&3^{15}=-1,\ 3^{10}=25,\ 3^6=16\\
41&2^{10}=-1,\ 2^4=16&3^4=-1\\
61&2^{30}=-1,\ 2^{20}=47,\ 2^{12}=9&
3^5=-1,\ 3^2=9\\
151&2^5=32,\ 2^3=8&
3^{25}=-1,\ 3^{10}=8\\
331&2^{15}=-1,\ 2^{10}=31,\ 2^6=64&
3^{165}=-1,\ 3^{110}=299,\ 3^{66}=64,\ 3^{30}=270\\
1321&2^{30}=-1,\ 2^{20}=1023,\ 2^{12}=133&
3^{11}=133,\ 3^5=243
\end{array}
\]
All residues are modulo the prime in the first column. For \(p=1321\), direct repeated squaring gives
\[
3^{60}\equiv243\equiv3^5\pmod{1321},
\]
so \(3^{55}\equiv1\); the two displayed non-unit powers then prove that the order is exactly \(55\).

Therefore
\[
\begin{aligned}
C_2(60)
&=
\frac14+\frac16+\frac1{10}+\frac1{12}+\frac1{30}
+\frac1{40}+\frac1{60}+\frac1{150}+\frac1{330}+\frac1{660}\\
&=\frac{4529}{6600}<1.
\end{aligned}
\tag{6}
\]

By (3), for every \(B\),
\[
W(60,B)\le\frac{4529}{6600}<1.
\]
Hence:

> **Proposition 1.** No product-grid covering exists with \(o_2(p)\mid60\) for every covering prime, irrespective of the chosen \(\ell\)-period \(B\).

For the symmetric choice \(A=B=60\), only
\[
5,7,11,13,31,61
\]
remain, and their total mass is
\[
\frac14+\frac16+\frac1{10}+\frac1{12}+\frac1{30}+\frac1{60}
=\frac{13}{20}.
\]

---

### 3. A forced-overlap obstruction beyond the density bound

The density condition \(W\ge1\) is not sufficient. The three highest-density primes \(5,7,11\) already have unavoidable overlap.

Choose generators so that their predicates are written as
\[
\begin{aligned}
f_5(k,\ell)&=k+3\ell\pmod4,\\
f_7(k,\ell)&=2k+\ell\pmod6,\\
f_{11}(k,\ell)&=k+8\ell\pmod{10}.
\end{aligned}
\tag{7}
\]
These follow from
\[
3\equiv2^3\pmod5,\qquad
2\equiv3^2\pmod7,\qquad
3\equiv2^8\pmod{11}.
\]

Consider
\[
F:\mathbb Z^2\longrightarrow
\mathbb Z_4\times\mathbb Z_6\times\mathbb Z_{10},
\qquad
F=(f_5,f_7,f_{11}).
\]
Modulo \(2\),
\[
f_5\equiv k+\ell,\qquad f_7\equiv\ell,\qquad f_{11}\equiv k.
\]
Consequently every point of the image satisfies
\[
c_5\equiv c_7+c_{11}\pmod2.
\tag{8}
\]
The subgroup defined by (8) has cardinality
\[
\frac{4\cdot6\cdot10}{2}=120.
\]

The map \((f_5,f_7)\) is surjective. Explicitly, given \(c\pmod4\) and \(d\pmod6\), write
\[
k=c-3\ell+4x.
\]
The second equation becomes
\[
-5\ell+2x\equiv d-2c\pmod6,
\]
which is solvable because
\[
\gcd(5,2,6)=1.
\]
Moreover,
\[
(12,0)\in\ker(f_5,f_7),
\qquad
f_{11}(12,0)\equiv2\pmod{10}.
\]
Thus, over each prescribed pair \((c_5,c_7)\), the \(f_{11}\)-coordinate runs through all five residues having the parity forced by (8). Hence the image of \(F\) is exactly the \(120\)-element subgroup defined by (8).

It follows that:

- every chosen \(5\)-coset and \(7\)-coset intersect, with intersection density \(1/24\);
- every chosen \(5\)-coset and \(11\)-coset intersect, with density \(1/40\);
- every chosen \(7\)-coset and \(11\)-coset intersect, with density \(1/60\);
- the triple intersection is either empty or has density \(1/120\).

Therefore, by inclusion-exclusion, the union of any three chosen target cosets for \(5,7,11\) has density at most
\[
\begin{aligned}
&\frac14+\frac16+\frac1{10}
-\frac1{24}-\frac1{40}-\frac1{60}
+\frac1{120}\\
&=\frac{53}{120}.
\end{aligned}
\tag{9}
\]
Their nominal mass is
\[
\frac14+\frac16+\frac1{10}=\frac{62}{120},
\]
so at least
\[
\frac{62-53}{120}=\frac3{40}
\tag{10}
\]
is always lost through overlap.

Let \(S\) be any finite candidate pool containing \(5,7,11\), and write
\[
W(S)=\sum_{p\in S}\frac1{h_p}.
\]
After choosing at most one target for every prime, the union of all selected cosets has density at most
\[
\frac{53}{120}
+
\left(W(S)-\frac{62}{120}\right)
=
W(S)-\frac3{40}.
\tag{11}
\]
Thus:

> **Proposition 2.** If \(S\) contains \(5,7,11\) and
> \[
> W(S)<\frac{43}{40},
> \]
> then no assignment of one target coset per prime in \(S\) covers \(\mathbb Z^2\).

For a product grid, \(5,7,11\in S(A,B)\) whenever
\[
60\mid A,\qquad 60\mid B.
\]
Consequently:

> **Corollary.** If \(60\mid A,B\) and
> \[
> W(A,B)<\frac{43}{40}=1.075,
> \]
> then the common-divisor pool of \((A,B)\) cannot furnish a cover.

This is strictly stronger than the basic condition \(W(A,B)\ge1\). In particular, a specified \(5040\)-smooth candidate pool containing \(5,7,11\) and having exact total mass around \(1.02\)–\(1.03\) is conclusively inadequate. This conclusion applies only to the precisely enumerated pool; unenumerated prime factors of
\[
\gcd(2^{5040}-1,3^{5040}-1)
\]
could increase the full mass.

---

### 4. Why primitive-divisor theory does not complete Route 3

One may organize the available primes by exact order pairs
\[
(a,b)=\bigl(o_2(p),o_3(p)\bigr).
\]
If \(n(a,b)\) denotes the number of primes with that order pair, then
\[
W(A,B)=
\sum_{\substack{a\mid A\\b\mid B}}
\frac{n(a,b)}{\operatorname{lcm}(a,b)}.
\tag{12}
\]
The relevant primes are common prime divisors of appropriate cyclotomic values, subject to the standard caveats when the prime divides a cyclotomic index.

Bang–Zsigmondy theory separately supplies primitive divisors for \(2^a-1\) and \(3^b-1\), but supplies no common prime. For example,
\[
\Phi_5(2)=31,\qquad \Phi_5(3)=121=11^2,
\]
so
\[
\gcd(\Phi_5(2),\Phi_5(3))=1,
\]
even though both sides possess primitive prime divisors. Likewise,
\[
\Phi_3(2)=7,\qquad \Phi_3(3)=13.
\]
Thus the theorem needed to manufacture many simultaneous exact-order primes is not a consequence of ordinary Zsigmondy theory.

Furthermore, even a sufficiently large value of (12) would not settle the set-cover problem: primes with the same order pair can induce highly correlated exponent lattices. Their discrete-log slopes and intersection profiles must also be controlled.

## Self-Audit

1. **The \(A=60\) calculation is arithmetic-heavy.**  
   A single wrong factor or order would corrupt \(C_2(60)\). I believe it is sound because the factorization is complete by direct multiplication and small-prime primality checks, while every order is accompanied by the standard prime-divisor witness tests. The code below independently reproduces all entries.

2. **The \(43/40\) obstruction depends on exact image cardinalities.**  
   The delicate point is that the triple image has size \(120\), not merely at most \(120\). This is proved explicitly: \((f_5,f_7)\) is surjective, the parity relation is necessary, and adding \((12,0)\) cycles through all five allowed \(f_{11}\)-values.

3. **These results concern finite product-grid covers, not arbitrary everywhere-composite families.**  
   They do not rule out a different period pair, a larger prime pool, or a solution using infinitely many varying prime divisors. I have not inferred anything stronger. The block is therefore one of scope, not a hidden claimed solution.

## Computations To Verify

```python
from fractions import Fraction
from math import gcd, lcm
from sympy import factorint, isprime, n_order

# ------------------------------------------------------------
# 1. Verify the A=60 factorization, orders, and capacity
# ------------------------------------------------------------

expected_factorization = {
    3: 2,
    5: 2,
    7: 1,
    11: 1,
    13: 1,
    31: 1,
    41: 1,
    61: 1,
    151: 1,
    331: 1,
    1321: 1,
}

assert factorint(2**60 - 1) == expected_factorization
assert all(isprime(p) for p in expected_factorization)

expected_orders = {
    5:    (4, 4),
    7:    (3, 6),
    11:   (10, 5),
    13:   (12, 3),
    31:   (5, 30),
    41:   (20, 8),
    61:   (60, 10),
    151:  (15, 50),
    331:  (30, 330),
    1321: (60, 55),
}

for p, (a, b) in expected_orders.items():
    assert n_order(2, p) == a
    assert n_order(3, p) == b

C60 = sum(
    Fraction(1, lcm(a, b))
    for a, b in expected_orders.values()
)
assert C60 == Fraction(4529, 6600)
assert C60 < 1
print("C_2(60) =", C60, float(C60))


# ------------------------------------------------------------
# 2. Compute a complete product-grid pool and its mass
# ------------------------------------------------------------

def product_grid_pool(A, B):
    g = gcd(2**A - 1, 3**B - 1)
    fac = factorint(g)  # Must complete for a rigorous pool.
    primes = sorted(p for p in fac if p >= 5)

    data = []
    mass = Fraction(0, 1)
    for p in primes:
        a = n_order(2, p)
        b = n_order(3, p)
        h = lcm(a, b)
        assert A % a == 0
        assert B % b == 0
        data.append((p, a, b, h))
        mass += Fraction(1, h)
    return g, data, mass

g60, pool60, W60 = product_grid_pool(60, 60)
assert {p for p, _, _, _ in pool60} == {5, 7, 11, 13, 31, 61}
assert W60 == Fraction(13, 20)
print("W(60,60) =", W60, float(W60))
print(pool60)


# ------------------------------------------------------------
# 3. Exhaustively verify the 5,7,11 forced-overlap calculation
# ------------------------------------------------------------

def f5(k, ell):
    return (k + 3*ell) % 4

def f7(k, ell):
    return (2*k + ell) % 6

def f11(k, ell):
    return (k + 8*ell) % 10

image = {
    (f5(k, ell), f7(k, ell), f11(k, ell))
    for k in range(60)
    for ell in range(60)
}
assert len(image) == 120
assert all((a - b - c) % 2 == 0 for a, b, c in image)

assert len({(a, b) for a, b, c in image}) == 4*6
assert len({(a, c) for a, b, c in image}) == 4*10
assert len({(b, c) for a, b, c in image}) == 6*10

best = 0
best_targets = None

for c5 in range(4):
    for c7 in range(6):
        for c11 in range(10):
            covered = sum(
                f5(k, ell) == c5
                or f7(k, ell) == c7
                or f11(k, ell) == c11
                for k in range(60)
                for ell in range(60)
            )
            if covered > best:
                best = covered
                best_targets = (c5, c7, c11)

assert Fraction(best, 60*60) == Fraction(53, 120)
print("Best 5,7,11 union:", Fraction(best, 3600), best_targets)


# ------------------------------------------------------------
# 4. Exact CP-SAT solver for a moderate product grid
# ------------------------------------------------------------

def solve_product_grid(A, B, time_limit=300):
    """
    Requires:
        pip install ortools sympy

    This is exact provided factorint completely factors the gcd and
    CP-SAT returns OPTIMAL or INFEASIBLE.
    """
    from ortools.sat.python import cp_model

    _, data, mass = product_grid_pool(A, B)
    print("candidate mass =", mass, float(mass))

    model = cp_model.CpModel()
    variables = {}
    targets_by_prime = {}

    for p, a, b, h in data:
        H = {
            (pow(2, k, p) * pow(3, ell, p)) % p
            for k in range(a)
            for ell in range(b)
        }
        assert len(H) == h
        targets_by_prime[p] = sorted(H)

        for t in H:
            variables[p, t] = model.NewBoolVar(f"x_{p}_{t}")

        # One prime can supply at most one target.
        model.Add(sum(variables[p, t] for t in H) <= 1)

    powers2 = {
        p: [pow(2, k, p) for k in range(A)]
        for p, _, _, _ in data
    }
    powers3 = {
        p: [pow(3, ell, p) for ell in range(B)]
        for p, _, _, _ in data
    }

    for k in range(A):
        for ell in range(B):
            covering_literals = []
            for p, _, _, _ in data:
                t = (powers2[p][k] * powers3[p][ell]) % p
                covering_literals.append(variables[p, t])
            if not covering_literals:
                return "INFEASIBLE", None
            model.Add(sum(covering_literals) >= 1)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    status = solver.Solve(model)

    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        chosen = {
            p: t
            for p, targets in targets_by_prime.items()
            for t in targets
            if solver.Value(variables[p, t])
        }

        # Independent exhaustive verification.
        for k in range(A):
            for ell in range(B):
                assert any(
                    (pow(2, k, p) * pow(3, ell, p)) % p == t
                    for p, t in chosen.items()
                )
        return "SAT", chosen

    if status == cp_model.INFEASIBLE:
        return "INFEASIBLE", None
    return "UNKNOWN", None
```

For larger periods, the main finite checks should be:

1. Completely factor or certify the relevant part of
   \[
   \gcd(2^A-1,3^B-1).
   \]
2. Compute \(W(A,B)\).
3. Reject immediately if \(W<1\), or if \(60\mid A,B\) and \(W<43/40\).
4. Compute exact pair/triple intersection profiles of the highest-density primes before invoking SAT.
5. Use Smith normal form or a lazy constraint-generation solver when \(AB\) is too large for direct enumeration.

## Route Diagnosis

The useful part of Route 3 is the capacity formalism: fixing one period makes the complete candidate universe finite, and \(C_2(A)\) or \(C_3(B)\) can eliminate an entire branch before a set-cover search. The forced-overlap calculation also shows that “barely more than unit mass” is insufficient; in particular, a \(5040\)-compatible restricted pool of mass \(1.02\)–\(1.03\) is structurally doomed if it contains \(5,7,11\).

The route is blocked at the simultaneous cyclotomic-divisor step. Bang–Zsigmondy does not produce common primitive divisors of \(2^A-1\) and \(3^B-1\), nor does it control the discrete-log slopes of those that happen to occur. If one first chooses arbitrary useful primes and then defines \(A,B\) as the least common multiples of their orders, Route 3 collapses back to the general finite-cover search and gains no existence theorem.

A fresh attempt should therefore avoid pools with mass only slightly above \(1\). It should seek a completely certified pool with substantial slack—probably at least \(1.2\)–\(1.3\)—then use exact intersection-aware SAT or a hierarchical lattice decomposition. Before any full search, the low-prime union capacity should be computed exactly and used as an upper bound, not merely the nominal sum \(\sum1/h_p\).