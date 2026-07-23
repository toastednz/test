STATUS: BLOCKED

## Result

I did not obtain an \(m\) or a finite covering certificate. I did establish a stronger and fully rigorous version of the cohort mechanism: in any inclusion-minimal finite cover, for every prime \(q\) dividing a selected index, the \(q\)-shadows of all \(q\)-divisible selected cosets must themselves cover \(\mathbb F_q^2\). I also derived exact recursive lift formulas and pointwise weighted capacity inequalities on every \(q\)-cell. These yield a proof-producing recursive verifier and a complete counterexample-guided search procedure for any fixed finite prime pool. A significant obstruction to Route 3 as originally phrased is that forcing candidates into complete parallel \(q\)-pencils is not lossless: \(q+1\) concurrent lines, one in each direction, also form a minimal shadow cover and contain no complete pencil. Thus the correct basic objects are arbitrary lift-compatible affine-plane line covers, not only pencils. The remaining block is computational and arithmetic: no concrete pool and target assignment surviving all lift conditions has been found, and failure for any bounded pool would not resolve the original problem.

## Complete Argument

### 1. Mixed-alphabet code formulation

For each selected prime \(p_i\), fix a generator of \(H_{p_i}\) and write its character as

\[
\chi_i(k,\ell)=a_i k+b_i\ell\pmod{h_i},
\qquad
h_i=h_{p_i},
\]

where

\[
\gcd(a_i,b_i,h_i)=1.
\]

A target is an intercept \(c_i\pmod{h_i}\), and its covering coset is

\[
C_i=\{(k,\ell)\in\mathbb Z^2:\chi_i(k,\ell)=c_i\}.
\]

Define

\[
D=\prod_{i=1}^s \mathbb Z/h_i\mathbb Z
\]

and the diagonal homomorphism

\[
\chi:\mathbb Z^2\longrightarrow D,\qquad
z\longmapsto (\chi_1(z),\ldots,\chi_s(z)).
\]

Let \(G=\chi(\mathbb Z^2)\le D\).

#### Lemma 1: code-avoidance equivalence

The cosets \(C_1,\ldots,C_s\) cover \(\mathbb Z^2\) if and only if

\[
G\cap \prod_{i=1}^s
\left((\mathbb Z/h_i\mathbb Z)\setminus\{c_i\}\right)
=\varnothing.
\]

Equivalently, every \(x=(x_i)\in G\) agrees with the target vector \(c=(c_i)\) in at least one coordinate.

Moreover, replacing \(c\) by \(c+g_0\), where \(g_0\in G\), does not change whether a cover exists.

#### Proof

A point \(z\in\mathbb Z^2\) is uncovered precisely when

\[
\chi_i(z)\ne c_i\qquad\text{for every }i.
\]

Since \(\chi(\mathbb Z^2)=G\), an uncovered point exists exactly when the displayed intersection is nonempty.

If \(c'=c+g_0\), translation \(x\mapsto x-g_0\) is a bijection of \(G\), and

\[
x_i=c'_i
\iff
(x-g_0)_i=c_i.
\]

Thus \(c\) and \(c+g_0\) have the same covering status. ∎

This makes the problem a mixed-alphabet covering-radius problem for the two-generator subgroup \(G\).

---

### 2. Exact restriction to a \(q\)-cell

Fix a prime \(q\), and partition the exponent lattice into the \(q^2\) cells

\[
P_v=v+q\mathbb Z^2,
\qquad
v=(r,s)\in\{0,\ldots,q-1\}^2.
\]

Consider one primitive character congruence

\[
a k+b\ell\equiv c\pmod h,
\qquad
\gcd(a,b,h)=1.
\]

Substitute

\[
(k,\ell)=v+q(x,y).
\]

The resulting condition is

\[
q(ax+by)\equiv c-ar-bs\pmod h.
\]

#### Lemma 2: exact \(q\)-cell restriction

Let \(d=c-ar-bs\).

1. If \(q\nmid h\), the restriction to \(P_v\), under the parameterization
   \((x,y)\mapsto v+q(x,y)\), is

   \[
   ax+by\equiv q^{-1}d\pmod h.
   \]

   It is therefore a primitive cyclic-character coset of index \(h\).

2. If \(q\mid h\) and \(d\not\equiv0\pmod q\), the original coset does not meet \(P_v\).

3. If \(q\mid h\) and \(d\equiv0\pmod q\), the restriction is

   \[
   ax+by\equiv d/q\pmod{h/q}.
   \]

   It is a primitive cyclic-character coset of index \(h/q\). If \(h=q\), it is the whole cell.

#### Proof

If \(q\nmid h\), multiplication by \(q\) is invertible modulo \(h\), proving the first assertion.

If \(q\mid h\), the left side is divisible by \(q\) modulo \(h\), so no solution exists unless \(q\mid d\). When \(q\mid d\), division of

\[
q(ax+by)\equiv d\pmod h
\]

by \(q\) gives exactly

\[
ax+by\equiv d/q\pmod{h/q}.
\]

Finally,

\[
\gcd(a,b,h/q)=1
\]

follows from \(\gcd(a,b,h)=1\), so the reduced character is still surjective. ∎

This is the exact lift rule required by Route 3. It controls the full congruence, not merely its shadow.

---

### 3. Pointwise weighted shadow inequalities

For a selected family of character cosets, fix a prime \(q\). Let

\[
J_q=\{i:q\nmid h_i\},
\qquad
I_q=\{i:q\mid h_i\}.
\]

For \(i\in I_q\), its \(q\)-shadow is the affine line

\[
L_i=\{(r,s)\in\mathbb F_q^2:
a_i r+b_i s\equiv c_i\pmod q\}.
\]

Because \(\gcd(a_i,b_i,h_i)=1\), the pair \((a_i,b_i)\) is not zero modulo \(q\), so this is genuinely a line.

#### Proposition 3: weighted \(q\)-cell capacity

If the selected cosets cover \(\mathbb Z^2\), then for every \(v\in\mathbb F_q^2\),

\[
\boxed{
\sum_{i\in J_q}\frac1{h_i}
+
\sum_{\substack{i\in I_q\\v\in L_i}}
\frac q{h_i}
\ge 1.
}
\]

#### Proof

Restrict the cover to \(P_v\) and parameterize the cell by \(\mathbb Z^2\).

By Lemma 2:

- each \(i\in J_q\) restricts to one coset of index \(h_i\), hence has relative density \(1/h_i\);
- each \(i\in I_q\) whose shadow misses \(v\) has empty restriction;
- each \(i\in I_q\) whose shadow contains \(v\) restricts to a coset of index \(h_i/q\), hence has relative density \(q/h_i\).

The restricted sets cover the parameter lattice. The density of a finite union is at most the sum of the densities of its members. Therefore the displayed sum is at least \(1\). ∎

This is stronger than the global mass condition. Averaging it over all \(q^2\) cells recovers

\[
\sum_i\frac1{h_i}\ge1,
\]

but the pointwise inequalities can fail even when global mass is ample.

---

### 4. Strong shadow-cover theorem

The cohort lemma can be sharpened from a cardinality assertion to a complete geometric assertion.

#### Theorem 4: every essential \(q\)-cohort covers the whole shadow plane

Let

\[
\mathbb Z^2=\bigcup_{i=1}^s C_i
\]

be an inclusion-minimal finite cover by primitive cyclic-character cosets. Fix a prime \(q\) dividing at least one selected index. Then the affine lines

\[
\{L_i:i\in I_q\}
\]

cover all of \(\mathbb F_q^2\).

Consequently,

\[
|I_q|\ge q.
\]

If \(|I_q|=q\), these \(q\) lines are precisely the \(q\) distinct lines in one parallel class.

#### Proof

Let \(J_q\) denote the indices not divisible by \(q\). By inclusion-minimality, the subfamily \(\{C_j:j\in J_q\}\) cannot itself cover \(\mathbb Z^2\), since otherwise every \(q\)-divisible member would be redundant.

Let

\[
K_J=\bigcap_{j\in J_q}\ker\chi_j,
\qquad
Q=\mathbb Z^2/K_J.
\]

The quotient \(Q\) embeds in

\[
\prod_{j\in J_q}\mathbb Z/h_j\mathbb Z,
\]

so \(|Q|\) is coprime to \(q\). Hence multiplication by \(q\) is an automorphism of \(Q\).

Suppose, for contradiction, that some \(v\in\mathbb F_q^2\) lies on none of the lines \(L_i\), \(i\in I_q\). Then every \(q\)-divisible coset is disjoint from

\[
P_v=v+q\mathbb Z^2.
\]

Since the full family covers, the \(q\)-free subfamily must cover \(P_v\).

But the image of \(P_v\) in \(Q\) is

\[
v+qQ=Q,
\]

because multiplication by \(q\) is surjective on \(Q\). Membership in the union of the \(q\)-free cosets depends only on the image in \(Q\). Thus, if that union contains \(P_v\), it contains every residue in \(Q\), and therefore covers all of \(\mathbb Z^2\). This contradicts the preceding paragraph.

Hence the lines \(L_i\), \(i\in I_q\), cover \(\mathbb F_q^2\).

Each affine line has \(q\) points, so at least \(q\) lines are required to cover \(q^2\) points. If exactly \(q\) lines cover, their total cardinality is exactly \(q^2\); therefore they must be pairwise disjoint. Distinct affine lines in \(\mathbb F_q^2\) are disjoint exactly when they are parallel. Thus the lines form a complete parallel pencil. ∎

This theorem yields a stronger pruning rule than mere cohort counting: the available slopes and chosen intercepts must support an actual affine-plane line cover.

---

### 5. Exact lift obligation for a cohort of size \(q\)

Assume the setting of Theorem 4 and that exactly \(q\) selected indices are divisible by \(q\). Their shadows form a parallel pencil. Thus every \(q\)-cell lies on exactly one of these shadows.

Let

\[
S_0=\sum_{j\in J_q}\frac1{h_j}.
\]

#### Corollary 5

For every \(i\in I_q\),

\[
S_0+\frac q{h_i}\ge1.
\]

Therefore

\[
S_0\ge 1-\min_{i\in I_q}\frac q{h_i}
=1-\frac q{\max_{i\in I_q}h_i}.
\]

More strongly, in every cell on \(L_i\), the restrictions of all \(q\)-free cosets together with the single reduced coset of index \(h_i/q\) must cover the parameter lattice \(\mathbb Z^2\).

#### Proof

Choose any point \(v\in L_i\). Since the \(q\) lines form a parallel pencil, no other line from \(I_q\) contains \(v\). Proposition 3 gives

\[
S_0+\frac q{h_i}\ge1.
\]

The exact covering statement follows directly from Lemma 2 after restricting the original cover to \(P_v\). ∎

This exposes the principal lifting obstruction. A pencil whose members have large quotients \(h_i/q\) contributes only a small amount inside each corresponding parent cell; nearly unit \(q\)-free capacity is then required.

---

### 6. Why complete-pencil grouping is not a lossless search rule

Route 3 proposed grouping candidates into complete \(q\)-cohorts, with special emphasis on parallel pencils. That is valid when exactly \(q\) \(q\)-divisible members occur, but it is false as a general structural restriction.

#### Proposition 6: star counterexample

For every prime \(q\), the \(q+1\) lines

\[
L_\infty=\{x=0\},
\qquad
L_t=\{y=tx\}\quad(t\in\mathbb F_q)
\]

cover \(\mathbb F_q^2\). They form an inclusion-minimal line cover and contain no complete parallel pencil.

#### Proof

If \(x=0\), the point lies on \(L_\infty\). If \(x\ne0\), it lies on the unique line

\[
L_{y/x}.
\]

Thus the lines cover.

Each line contains nonzero points belonging to no other line in the family, so removing any line leaves uncovered points. Hence the cover is inclusion-minimal.

There is only one line in each projective direction, so no parallel class contains \(q\) lines. ∎

For \(q=2\), this is already the three-line cover

\[
x=0,\qquad y=0,\qquad x+y=0
\]

of \(\mathbb F_2^2\).

Therefore a search restricted to parallel pencils can reject genuine possibilities. The correct shadow gadgets are arbitrary affine-line covers compatible with the available slopes, followed by exact lift checking via Lemma 2.

---

### 7. A complete recursive verifier for fixed targets

The restriction lemma gives a finite proof-producing verification algorithm that never needs to enumerate a rectangular period.

Represent every set by a primitive tuple

\[
(a,b,c,h)
\]

meaning

\[
ak+b\ell\equiv c\pmod h.
\]

The recursive procedure is:

1. If a tuple has \(h=1\), the current cell is covered.
2. If there are no tuples, the current cell is uncovered.
3. Choose any prime \(q\) dividing one of the current moduli.
4. For every \(v=(r,s)\in\mathbb F_q^2\), replace each tuple using Lemma 2:
   - if \(q\nmid h\), retain modulus \(h\) and replace the target by
     \[
     q^{-1}(c-ar-bs)\pmod h;
     \]
   - if \(q\mid h\) and \(c-ar-bs\not\equiv0\pmod q\), discard it in that child;
   - otherwise replace it by
     \[
     (a,b,(c-ar-bs)/q,h/q).
     \]
5. The current family covers if and only if every child covers.

#### Theorem 7: correctness and termination

The recursive procedure terminates and returns “covered” exactly when the original family covers \(\mathbb Z^2\).

If it returns “uncovered”, it can return an explicit integer point not lying in any selected coset.

#### Proof

At each node, the \(q^2\) cells

\[
v+q\mathbb Z^2
\]

partition the current parameter lattice. Lemma 2 gives the exact restriction of every selected coset to every child. Therefore the current family covers if and only if all child restrictions cover.

For termination, define

\[
M=\sum_i \Omega(h_i),
\]

where \(\Omega\) counts prime factors with multiplicity. At a node, \(q\) divides at least one modulus. In each child, every \(q\)-divisible tuple is either discarded or has its modulus divided by \(q\). Thus \(M\) strictly decreases along every recursive edge. Hence recursion depth is finite.

If a child contains an uncovered parameter point \(y\), then

\[
v+qy
\]

is uncovered in the parent. Iterating this reconstruction gives an explicit uncovered point in the original lattice. ∎

A successful run can be recorded as a finite decision tree. Every leaf is certified covered by a tuple whose modulus has reduced to \(1\). Such a tree is an independently checkable finite covering certificate.

---

### 8. Complete target search for a fixed prime pool

For a fixed pool with characters \((a_i,b_i,h_i)\), introduce Boolean variables

\[
X_{i,c}\qquad(0\le c<h_i)
\]

with constraints

\[
\sum_{c=0}^{h_i-1}X_{i,c}=1.
\]

Thus every prime receives exactly one target. Using every prime entails no loss: if a subset covers, arbitrary targets may be assigned to the unused primes.

A counterexample-guided search is complete:

1. Obtain a target assignment from a SAT/SMT solver.
2. Run the recursive verifier.
3. If it certifies coverage, stop.
4. If it returns an uncovered point \(z=(k,\ell)\), add the valid clause
   \[
   \bigvee_i X_{i,\chi_i(z)}.
   \]
5. Repeat.

The clause is necessary for every covering assignment, because \(z\) must be covered by at least one selected prime.

There are only

\[
\prod_i h_i
\]

target assignments. Each uncovered-point clause excludes the current assignment. Therefore the process terminates, in principle, with either:

- a rigorously verifiable target assignment; or
- an exhaustive proof that the fixed pool has no covering assignment.

The weighted inequalities of Proposition 3 can be inserted before the loop as exact rational cutting planes. This is substantially stronger than generic SAT over a rectangular torus, but it remains a finite-pool method only.

## Self-Audit

1. **Theorem 4 uses inclusion-minimality essentially.**  
   Without minimality, the \(q\)-free members might already cover and the \(q\)-divisible shadows need not cover \(\mathbb F_q^2\). This does not invalidate its use: every finite cover has an inclusion-minimal subcover. The proof explicitly passes through the quotient generated by the \(q\)-free characters and uses that multiplication by \(q\) is an automorphism there.

2. **The weighted inequalities are only necessary, not sufficient.**  
   They ignore overlaps inside each \(q\)-cell. I use them only as rejection cuts, never as a covering proof. Exact sufficiency is supplied only by the recursive restriction verifier.

3. **The fixed-pool search procedure is mathematically complete but may be computationally infeasible.**  
   Its termination bound is essentially \(\prod h_i\), and no useful global bound on the primes in a possible certificate is known. Thus an UNSAT result for a finite pool cannot settle the original problem. The correctness claim is nevertheless secure because every generated clause is necessary and the target space is finite.

## Computations To Verify

The following exact Python implements character extraction and the recursive verifier.

```python
from functools import cache
from itertools import product
from math import gcd, lcm
from sympy import factorint, n_order, primitive_root, primerange

def prime_signature(p):
    """Return (p, o2, o3, h, g, a, b) with 2=g^a and 3=g^b in H_p."""
    o2 = int(n_order(2, p))
    o3 = int(n_order(3, p))
    h = lcm(o2, o3)

    z = int(primitive_root(p))
    g = pow(z, (p - 1) // h, p)

    table = {}
    x = 1
    for e in range(h):
        assert x not in table
        table[x] = e
        x = x * g % p

    assert x == 1
    assert len(table) == h
    a = table[2 % p]
    b = table[3 % p]
    assert gcd(gcd(a, b), h) == 1
    return (p, o2, o3, h, g, a, b)

def canonical(items):
    """Duplicate congruences may be removed without changing their union."""
    out = set()
    for a, b, c, h in items:
        if h == 1:
            return ((0, 0, 0, 1),)
        a %= h
        b %= h
        c %= h
        assert gcd(gcd(a, b), h) == 1
        out.add((a, b, c, h))
    return tuple(sorted(out))

@cache
def uncovered_witness(state):
    """
    Return None iff the union covers Z^2.
    Otherwise return an explicit uncovered pair (k,l).
    """
    if any(h == 1 for a, b, c, h in state):
        return None
    if not state:
        return (0, 0)

    prime_factors = set()
    for a, b, c, h in state:
        prime_factors.update(factorint(h).keys())

    # A heuristic choice only; correctness is independent of this choice.
    q = max(prime_factors,
            key=lambda r: sum(1 for a, b, c, h in state if h % r == 0))

    for r, s in product(range(q), repeat=2):
        child = []
        for a, b, c, h in state:
            d = c - a*r - b*s

            if h % q:
                c2 = (d * pow(q, -1, h)) % h
                child.append((a, b, c2, h))
            else:
                if d % q:
                    continue
                h2 = h // q
                if h2 == 1:
                    child.append((0, 0, 0, 1))
                else:
                    child.append((a, b, (d // q) % h2, h2))

        child = canonical(child)
        w = uncovered_witness(child)
        if w is not None:
            return (r + q*w[0], s + q*w[1])

    return None

def covers(congruences):
    return uncovered_witness(canonical(congruences)) is None

def brute_covers(congruences):
    """Only for small lcm; cross-checks the recursive verifier."""
    if any(h == 1 for a, b, c, h in congruences):
        return True
    L = 1
    for a, b, c, h in congruences:
        L = lcm(L, h)
    for k in range(L):
        for ell in range(L):
            if not any((a*k + b*ell - c) % h == 0
                       for a, b, c, h in congruences):
                return False
    return True
```

The verifier should first be exhaustively cross-checked on random small primitive congruence families:

```python
import random

for trial in range(10000):
    fam = []
    for _ in range(random.randint(0, 7)):
        h = random.randint(2, 12)
        while True:
            a = random.randrange(h)
            b = random.randrange(h)
            if gcd(gcd(a, b), h) == 1:
                break
        c = random.randrange(h)
        fam.append((a, b, c, h))

    assert covers(fam) == brute_covers(fam)
```

The pointwise \(q\)-layer inequality can be checked exactly as follows:

```python
from fractions import Fraction

def q_layer_values(congruences, q):
    """
    Return the exact conditional mass upper bound in every q-cell.
    Every value must be >= 1 for a genuine cover.
    """
    base = sum(Fraction(1, h)
               for a, b, c, h in congruences if h % q)

    values = {}
    for r, s in product(range(q), repeat=2):
        value = base
        for a, b, c, h in congruences:
            if h % q == 0 and (a*r + b*s - c) % q == 0:
                value += Fraction(q, h)
        values[(r, s)] = value
    return values

def verify_all_layer_cuts(congruences):
    qs = set()
    for a, b, c, h in congruences:
        qs.update(factorint(h).keys())
    return {
        q: min(q_layer_values(congruences, q).values())
        for q in sorted(qs)
    }
```

A complete counterexample-guided target search for a fixed pool can be implemented with Z3:

```python
import z3

def add_q_layer_cuts(solver, X, signatures):
    """
    signatures[i] = (a_i, b_i, h_i).
    Adds Proposition 3 for every prime q dividing an index.
    """
    D = 1
    qs = set()
    for a, b, h in signatures:
        D = lcm(D, h)
        qs.update(factorint(h).keys())

    for q in sorted(qs):
        constant = sum(D // h for a, b, h in signatures if h % q)

        for r, t in product(range(q), repeat=2):
            terms = []
            for i, (a, b, h) in enumerate(signatures):
                if h % q == 0:
                    needed = (a*r + b*t) % q
                    coeff = q * D // h
                    for c in range(h):
                        if c % q == needed:
                            terms.append(coeff * z3.If(X[i][c], 1, 0))

            lhs = z3.IntVal(constant)
            if terms:
                lhs += z3.Sum(terms)
            solver.add(lhs >= D)

def cegis_targets(signatures):
    """
    Return target intercepts c_i if a cover is found.
    Return None if the fixed pool is proved incapable of covering.
    """
    solver = z3.Solver()
    X = []

    for i, (a, b, h) in enumerate(signatures):
        row = [z3.Bool(f"x_{i}_{c}") for c in range(h)]
        X.append(row)
        solver.add(z3.PbEq([(v, 1) for v in row], 1))

    add_q_layer_cuts(solver, X, signatures)

    while solver.check() == z3.sat:
        model = solver.model()
        targets = []
        for i, (a, b, h) in enumerate(signatures):
            chosen = [
                c for c in range(h)
                if z3.is_true(model.evaluate(X[i][c],
                                             model_completion=True))
            ]
            assert len(chosen) == 1
            targets.append(chosen[0])

        congruences = [
            (a, b, targets[i], h)
            for i, (a, b, h) in enumerate(signatures)
        ]

        w = uncovered_witness(canonical(congruences))
        if w is None:
            return targets

        k, ell = w
        # Every valid cover must cover this exact point.
        solver.add(z3.Or([
            X[i][(a*k + b*ell) % h]
            for i, (a, b, h) in enumerate(signatures)
        ]))

    return None
```

Concrete runs that should be made:

1. Enumerate all primes \(p<10^5\), compute \((a_p,b_p,h_p)\), and verify every supplied order datum.
2. For each \(q\), normalize the slope \([a_p:b_p]\in\mathbb P^1(\mathbb F_q)\) for every \(p\) with \(q\mid h_p\).
3. Enumerate:
   - available complete pencils;
   - available \(q+1\)-direction stars;
   - all other inclusion-minimal line covers for small \(q\).
4. For every such shadow gadget, enumerate target lifts \(c_p\bmod h_p\) and invoke the recursive verifier immediately. Reject a gadget as soon as a child violates Proposition 3.
5. Run `cegis_targets` first on cohort-closed pools with moderate \(h_p\), then enlarge the pool. Any purported positive output must be independently rechecked by `covers`.
6. If targets are found, compute
   \[
   t_p=g_p^{c_p}\pmod p,\qquad
   m\equiv -t_p^{-1}\pmod p,\qquad m\equiv1\pmod6,
   \]
   and choose the CRT representative above all selected primes.

## Route Diagnosis

**Proved ledger**

- The finite-cover problem is exactly a mixed-alphabet code-avoidance problem.
- Restriction to every \(q\)-cell has an explicit exact formula.
- Every finite cover obeys pointwise weighted \(q\)-cell capacity inequalities.
- In an inclusion-minimal cover, the \(q\)-divisible shadows cover all of \(\mathbb F_q^2\), strengthening the cohort lemma.
- An exact \(q\)-cohort must be a parallel pencil and has severe conditional lift requirements.
- Fixed targets can be verified by a terminating recursive decision tree without enumerating a large torus.
- Target search over any fixed pool admits a complete counterexample-guided algorithm.

**Dead end**

- Requiring every \(q\)-layer to decompose into complete parallel pencils is unsound. Concurrent \(q+1\)-line stars are minimal covers and contain no pencil. More general affine-line covers must be admitted.

**Plausible but unproved**

- A sufficiently large cohort-closed prime pool may contain lift-compatible shadow gadgets with enough conditional mass.
- Recursive witness generation plus weighted cuts may be computationally effective on such a pool.
- A hybrid algebraic mask may reduce the residual enough for the same recursive machinery to succeed.

**Precise block**

The full character of a prime constrains all quotient layers simultaneously. A valid shadow line generally reduces only to a thin coset of index \(h_p/q\) in its parent cell. The q-free sets are replicated into every child with correlated shifted targets, so independently good shadow gadgets need not have compatible lifts. No concrete collection of arithmetic signatures and intercepts overcoming these correlations has been produced.

A fresh attempt should therefore enumerate general minimal affine-plane shadow covers, not just pencils, and feed each directly into the exact recursive lift verifier. The weighted cell inequalities should be installed as solver cuts before any global target search. If pure prime pools continue to fail, the same recursion should be extended to the \(m=x^{60}\) algebraic mask; that changes leaf coverage while retaining the exact lift architecture developed here.