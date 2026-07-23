STATUS: BLOCKED

## Result

I did not obtain a finite covering certificate, so Erdős Problem #203 remains unresolved here. I established an exact SAT formulation, proved that its ordinary LP relaxation contains no information beyond the density inequality, developed a target-independent Hunter-type overlap obstruction, and used it to rule out every choice of target cosets from an 18-prime benchmark pool containing the principal small and equal-order primes in the brief. I also proved that a flat SAT encoding for that pool already has at least \(270{,}887{,}100\) distinct quotient classes. Finally, I found a correction to the supplied data: \(\operatorname{ord}_{601}(2)=25\), not \(75\), although \(h_{601}=75\) remains correct.

## Complete Argument

### 1. Exact finite SAT formulation

Let \(S=\{p_1,\dots,p_r\}\) be a fixed finite set of primes \(p_i\ge 5\). For each \(i\), choose a generator \(g_i\) of
\[
H_{p_i}=\langle 2,3\rangle,
\qquad |H_{p_i}|=h_i,
\]
and write
\[
2=g_i^{\alpha_i},\qquad 3=g_i^{\beta_i}.
\]
Then
\[
\gcd(\alpha_i,\beta_i,h_i)=1,
\]
and every prime predicate has the form
\[
f_i(k,\ell):=\alpha_i k+\beta_i\ell\equiv c_i\pmod{h_i}
\]
for one selected target exponent \(c_i\in\mathbb Z/h_i\mathbb Z\).

Define
\[
F:\mathbb Z^2\longrightarrow \prod_{i=1}^r\mathbb Z/h_i\mathbb Z,
\qquad
F(k,\ell)=\bigl(f_i(k,\ell)\bigr)_{i=1}^r,
\]
and let \(G=F(\mathbb Z^2)\).

For every \(i\) and \(c\in\mathbb Z/h_i\mathbb Z\), introduce a Boolean variable \(x_{i,c}\), interpreted as “prime \(p_i\) is assigned target exponent \(c\).” The exact finite-cover instance is
\[
\sum_{c\bmod h_i}x_{i,c}=1 \qquad (1\le i\le r),
\]
together with the clauses
\[
\bigvee_{i=1}^r x_{i,g_i}
\qquad
\text{for every }g=(g_1,\dots,g_r)\in G.
\]

This SAT instance is satisfiable if and only if the selected prime cosets cover \(\mathbb Z^2\).

Indeed, a point \((k,\ell)\) is covered precisely when at least one selected target equals its corresponding coordinate \(f_i(k,\ell)\). Every element of \(G\) arises from some exponent pair, and pairs with the same image in \(G\) satisfy exactly the same prime predicates.

Requiring exactly one target per candidate prime causes no loss: if a cover uses only a subset of the candidate primes, arbitrary targets may be assigned to the unused primes, which can only enlarge the covered set.

---

### 2. The ordinary LP relaxation is exactly the density test

Consider the relaxation
\[
0\le x_{i,c}\le1,\qquad
\sum_c x_{i,c}=1,
\]
with
\[
\sum_i x_{i,g_i}\ge1\qquad(g\in G).
\]

#### Lemma 1
This LP is feasible if and only if
\[
\sum_{i=1}^r\frac1{h_i}\ge1.
\]

#### Proof

Each projection \(G\to\mathbb Z/h_i\mathbb Z\) is surjective, because \(f_i\) is surjective. Consequently, under the uniform measure on the finite group \(G\), each coordinate \(g_i\) is uniformly distributed.

Averaging all covering inequalities gives
\[
1
\le
\sum_i\frac1{h_i}\sum_{c\bmod h_i}x_{i,c}
=
\sum_i\frac1{h_i}.
\]
This proves necessity.

Conversely, if the reciprocal sum is at least \(1\), set
\[
x_{i,c}=\frac1{h_i}}
\]
for every \(i,c\). Then each target-selection equality holds, and every point constraint has left side
\[
\sum_i\frac1{h_i}\ge1.
\]
Thus the LP is feasible. ∎

There is a typographical issue in the displayed assignment above: the intended value is, of course,
\[
x_{i,c}=\frac1{h_i}.
\]

Therefore a standard fractional set-cover solve cannot reveal any obstruction beyond total mass. Stronger relaxations or genuinely integral search are necessary.

---

### 3. A target-independent overlap bound

All cosets in a finite candidate pool are periodic on a common finite quotient, so their natural densities may be treated as probabilities.

#### Lemma 2: Hunter forest bound

Let \(E_1,\dots,E_r\) be events in a finite probability space, and let \(T\) be any spanning tree on \(\{1,\dots,r\}\). Then
\[
\Pr\left(\bigcup_{i=1}^r E_i\right)
\le
\sum_{i=1}^r\Pr(E_i)
-
\sum_{\{i,j\}\in E(T)}\Pr(E_i\cap E_j).
\]

#### Proof

Root the tree and order vertices so that every parent precedes its children. When a non-root event \(E_v\) is added, the newly covered part is contained in
\[
E_v\setminus E_{\operatorname{parent}(v)}.
\]
Its measure is therefore at most
\[
\Pr(E_v)-\Pr(E_v\cap E_{\operatorname{parent}(v)}).
\]
Summing these bounds, together with the root event, proves the result. ∎

For two prime predicates
\[
f_i(k,\ell)=c_i,\qquad f_j(k,\ell)=c_j,
\]
if the combined homomorphism
\[
(f_i,f_j):\mathbb Z^2\to
\mathbb Z/h_i\mathbb Z\times\mathbb Z/h_j\mathbb Z
\]
is surjective, then every pair of targets has an intersection of density exactly
\[
\frac1{h_ih_j}.
\]
Thus such intersections are unavoidable, independently of the selected targets.

A useful surjectivity criterion is the following.

#### Lemma 3

Suppose both row maps
\[
(\alpha,\beta):\mathbb Z^2\to\mathbb Z/m\mathbb Z,
\qquad
(\gamma,\delta):\mathbb Z^2\to\mathbb Z/n\mathbb Z
\]
are surjective. If, for every prime \(q\mid\gcd(m,n)\),
\[
\alpha\delta-\beta\gamma\not\equiv0\pmod q,
\]
then the combined map to
\[
\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z
\]
is surjective.

#### Proof

Decompose the target into its \(q\)-primary components. If \(q\) divides only one of \(m,n\), surjectivity follows from the corresponding row map. If \(q\) divides both, the coefficient matrix is invertible modulo \(q\). It is therefore invertible over \(\mathbb Z_q\), and its reduction maps onto
\[
\mathbb Z/q^{v_q(m)}\mathbb Z
\times
\mathbb Z/q^{v_q(n)}\mathbb Z.
\]
Combining the primary solutions by CRT proves surjectivity. ∎

In particular, coprime indices always give a surjective combined map.

---

### 4. An 18-prime benchmark pool is conclusively inadequate

Consider
\[
\mathcal P=
\{5,7,11,13,17,19,23,29,31,37,41,43,47,73,71,431,601,167\}.
\]

The relevant order data are:

\[
\begin{array}{c|c|c|c}
p&\operatorname{ord}_p(2)&\operatorname{ord}_p(3)&h_p\\ \hline
5&4&4&4\\
7&3&6&6\\
11&10&5&10\\
13&12&3&12\\
17&8&16&16\\
19&18&18&18\\
23&11&11&11\\
29&28&28&28\\
31&5&30&30\\
37&36&18&36\\
41&20&8&40\\
43&14&42&42\\
47&23&23&23\\
73&9&12&36\\
71&35&35&35\\
431&43&43&43\\
601&25&75&75\\
167&83&83&83
\end{array}
\]

For the even-index primes needed below, convenient coordinate maps are

\[
\begin{array}{c|c}
p&f_p(k,\ell)\pmod{h_p}\\ \hline
5&k+3\ell\pmod4\\
7&2k+\ell\pmod6\\
11&k+8\ell\pmod{10}\\
13&k+4\ell\pmod{12}\\
17&14k+\ell\pmod{16}\\
19&k+13\ell\pmod{18}\\
29&k+5\ell\pmod{28}\\
31&24k+\ell\pmod{30}\\
37&k+26\ell\pmod{36}\\
41&26k+15\ell\pmod{40}\\
43&27k+\ell\pmod{42}\\
73&4k+3\ell\pmod{36}.
\end{array}
\]

For example, the generators used here may be taken as
\[
2,3,2,2,3,2,2,3,2,6,3,25
\]
respectively. In the last case,
\[
25^4\equiv2\pmod{73},\qquad 25^3\equiv3\pmod{73},
\]
and \(25\) has order \(36\).

The correction at \(p=601\) is explicit:
\[
2^{25}=33\,554\,432=601\cdot55\,831+1,
\qquad 2^5=32\not\equiv1\pmod{601},
\]
so
\[
\operatorname{ord}_{601}(2)=25.
\]
On the other hand,
\[
3^{15}\equiv32,\qquad 3^{25}\equiv24,\qquad
3^{75}\equiv24^3\equiv1\pmod{601},
\]
so \(\operatorname{ord}_{601}(3)=75\) and \(h_{601}=75\).

For the other large odd indices:

- Modulo \(71\),
  \[
  2^5=32,\quad2^7=57,\quad2^{35}=1,
  \]
  and
  \[
  3^5=30,\quad3^7=57,\quad3^{35}=1,
  \]
  proving both orders are \(35\).

- Modulo \(431\),
  \[
  2^{43}\equiv1,\qquad3^{43}\equiv1,
  \]
  and \(43\) is prime, so both nontrivial elements have order \(43\).

- Modulo \(167\),
  \[
  2^{83}\equiv1,\qquad3^{83}\equiv1,
  \]
  and \(83\) is prime, proving both orders are \(83\).

Now use the following spanning tree.

Connect \(p=5\) to
\[
7,11,13,17,23,31,37,41,47,73,71,431,601,167,
\]
and connect \(p=7\) to
\[
19,29,43.
\]

All these paired maps are surjective:

- The edges from \(5\) to odd indices are surjective because those indices are coprime to \(4\).
- For the even-index neighbors of \(5\), the row for \(p=5\) is \((1,3)\equiv(1,1)\pmod2\), while the other rows reduce to either \((1,0)\) or \((0,1)\). The determinants are odd.
- For the remaining three edges from \(7\), the determinants are
  \[
  \det\begin{pmatrix}2&1\\1&13\end{pmatrix}=25,
  \]
  \[
  \det\begin{pmatrix}2&1\\1&5\end{pmatrix}=9,
  \]
  and
  \[
  \det\begin{pmatrix}2&1\\27&1\end{pmatrix}=-25.
  \]
  These are units modulo every prime dividing the corresponding common index factors.

Thus the unavoidable tree-overlap weight is

\[
\begin{aligned}
W={}&
\frac1{24}+\frac1{40}+\frac1{48}+\frac1{64}
+\frac1{44}+\frac1{120}+\frac1{144}+\frac1{160}\\
&+\frac1{92}+\frac1{144}+\frac1{140}+\frac1{172}
+\frac1{300}+\frac1{332}\\
&+\frac1{108}+\frac1{168}+\frac1{252}.
\end{aligned}
\]

Direct rational comparison gives
\[
W>0.203.
\]

The total covering mass is

\[
\begin{aligned}
S={}&
\frac14+\frac16+\frac1{10}+\frac1{12}+\frac1{16}
+\frac1{18}+\frac1{11}+\frac1{28}+\frac1{30}\\
&+\frac1{36}+\frac1{40}+\frac1{42}+\frac1{23}
+\frac1{36}+\frac1{35}+\frac1{43}+\frac1{75}+\frac1{83}\\
={}&
\frac{4493}{5040}
+\frac1{11}+\frac1{23}+\frac1{35}
+\frac1{43}+\frac1{75}+\frac1{83}.
\end{aligned}
\]

For a simple exact upper estimate,
\[
\frac{4493}{5040}<0.892,
\]
and
\[
\frac1{11}<0.091,\quad
\frac1{23}<0.044,\quad
\frac1{35}<0.029,\quad
\frac1{43}<0.024,\quad
\frac1{75}<0.014,\quad
\frac1{83}<0.013.
\]
Hence
\[
S<1.107.
\]

By the Hunter tree bound, for every possible assignment of targets,
\[
\operatorname{dens}\left(\bigcup_{p\in\mathcal P}E_p\right)
\le S-W
<1.107-0.203
=0.904<1.
\]

Therefore:

> No choice of one target coset for each prime in \(\mathcal P\), nor for any subset of \(\mathcal P\), covers \(\mathbb Z^2\).

Using the exact fractions gives
\[
S\approx1.103064375,\qquad
W\approx0.203676146,
\]
and therefore the sharper bound
\[
\operatorname{dens}\left(\bigcup_{p\in\mathcal P}E_p\right)
\le 0.89938823\ldots.
\]

As a corollary, any cover augmented from this pool needs outside primes of total mass at least
\[
1-S+W\approx0.10061177.
\]

This does not preclude such an augmentation.

---

### 5. The flat quotient is already too large for a naive encoding

Inside the benchmark pool, consider the six indices
\[
4,11,23,43,75,83,
\]
coming respectively from
\[
5,23,47,431,601,167.
\]
They are pairwise coprime.

Each coordinate map onto the corresponding cyclic group is surjective. By CRT, their combined map is surjective onto the product. Therefore the common image quotient for the full benchmark pool has at least

\[
4\cdot11\cdot23\cdot43\cdot75\cdot83
=
270\,887\,100
\]
elements.

Thus a flat SAT formulation with one clause for every quotient class has at least \(270{,}887{,}100\) distinct point clauses for this pool alone. Adding further incommensurate primes can only increase the quotient size.

This is a practical obstruction, not a mathematical impossibility result for SAT or for the existence of a cover.

---

### 6. Exact symbolic subtraction of lattice cosets

There is an exact alternative to enumerating the entire quotient.

Let \(C=a+L\) be a coset of a finite-index lattice \(L\le\mathbb Z^2\), and let
\[
E=\{x:f(x)=c\pmod h\}
\]
be a prime predicate, where \(f:\mathbb Z^2\to\mathbb Z/h\mathbb Z\) is surjective.

Set
\[
L'=L\cap\ker f,
\qquad d=|f(L)|=[L:L'].
\]

Then:

1. If \(c-f(a)\notin f(L)\), the intersection \(C\cap E\) is empty.
2. Otherwise, \(C\cap E\) is exactly one coset of \(L'\).
3. The coset \(C\) partitions into \(d\) cosets of \(L'\), so
   \[
   C\setminus E
   \]
   is the disjoint union of the other \(d-1\) cosets.

This follows because the restriction
\[
f|_L:L\to f(L)
\]
has kernel \(L'\), and every nonempty fiber is one coset of that kernel.

Hence a proposed target assignment can be verified by starting from \(\mathbb Z^2\) and repeatedly subtracting selected prime cosets, representing the residual exactly as lattice cosets in Hermite or Smith normal form. The obstruction is that the number of residual cosets can grow multiplicatively; I did not prove a bound making this procedure tractable for a sufficiently rich prime pool.

---

### 7. Running ledger

#### Proved lemmas and results

1. The finite-cover problem for a fixed prime pool has the exact SAT formulation above.
2. Its ordinary LP relaxation is feasible exactly when the reciprocal mass is at least \(1\).
3. The Hunter spanning-tree overlap bound applies to prime cosets on the common finite quotient.
4. Surjective pair maps force target-independent overlap \(1/(h_ih_j)\).
5. The specified 18-prime benchmark pool cannot cover \(\mathbb Z^2\), regardless of target choices.
6. Its common quotient has at least \(270{,}887{,}100\) classes.
7. Symbolic subtraction of a lattice coset by a prime coset has the exact fiber decomposition described above.
8. The supplied order \(\operatorname{ord}_{601}(2)=75\) is incorrect; the correct value is \(25\), while \(h_{601}=75\).

#### Plausible but unproved

1. A richer prime pool may still admit a finite covering.
2. A lazy SAT/CEGAR search using exact Smith-normal-form residual separation may avoid full quotient enumeration.
3. Hierarchical choice of primes based on local character diversity may substantially outperform a flat smooth-period pool.

#### Dead ends

1. The basic LP relaxation is provably no stronger than the density test.
2. Flat enumeration is already too large for the benchmark pool and becomes worse after adding incommensurate primes.
3. A single common-slope reduction \(k+D\ell\) cannot simultaneously use several of the heaviest small primes. For example, \(3\equiv2^D\pmod5\) requires
   \[
   D\equiv3\pmod4,
   \]
   whereas \(3\equiv2^D\pmod{11}\) requires
   \[
   D\equiv8\pmod{10},
   \]
   and these conditions are incompatible modulo \(2\).

## Self-Audit

1. **The modular order table is compressed rather than accompanied by every repeated-squaring step.** The key large cases and the \(p=601\) correction were calculated explicitly, and the code below independently verifies every entry, primality assertion, coordinate map, and pair-surjectivity claim using exact integer arithmetic.

2. **The Hunter obstruction rules out only one finite benchmark pool.** This is a genuine limitation: it says nothing directly about primes outside the pool. The bounded conclusion itself is rigorous because it uses only exact densities and unavoidable pair intersections.

3. **The claim that flat SAT is “blocked” is computational rather than a complexity theorem.** A specialized solver might handle hundreds of millions of implicit clauses. The quotient lower bound is nevertheless exact, and no compressed separation method with a proven manageable state bound was obtained.

## Computations To Verify

The following pure Python code verifies the order data, corrects the \(p=601\) entry, computes cyclic coordinates, checks every edge in the Hunter tree, and reproduces the exact density bound.

```python
from math import gcd, lcm, isqrt
from fractions import Fraction
from collections import deque

P = [
    5, 7, 11, 13, 17, 19, 23, 29, 31,
    37, 41, 43, 47, 73, 71, 431, 601, 167
]

expected_orders = {
    5:   (4, 4),
    7:   (3, 6),
    11:  (10, 5),
    13:  (12, 3),
    17:  (8, 16),
    19:  (18, 18),
    23:  (11, 11),
    29:  (28, 28),
    31:  (5, 30),
    37:  (36, 18),
    41:  (20, 8),
    43:  (14, 42),
    47:  (23, 23),
    73:  (9, 12),
    71:  (35, 35),
    431: (43, 43),
    601: (25, 75),   # correction to the supplied brief
    167: (83, 83),
}

def prime_factors(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        ans.append(n)
    return ans

def is_prime_trial(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True

def multiplicative_order(a, p):
    assert gcd(a, p) == 1
    n = p - 1
    for q in prime_factors(p - 1):
        while n % q == 0 and pow(a, n // q, p) == 1:
            n //= q
    return n

def coordinates(p):
    """
    Return h, generator g of H=<2,3>, and exponents alpha,beta:
       2 = g^alpha, 3 = g^beta mod p.
    """
    o2 = multiplicative_order(2, p)
    o3 = multiplicative_order(3, p)
    h = lcm(o2, o3)

    g = None
    for z in range(2, p):
        if multiplicative_order(z, p) == h:
            g = z
            break
    assert g is not None

    log = {}
    x = 1
    for e in range(h):
        log[x] = e
        x = (x * g) % p
    assert len(log) == h
    assert 2 in log and 3 in log

    alpha, beta = log[2], log[3]
    assert gcd(gcd(alpha, beta), h) == 1
    return h, g, alpha, beta

data = {}

for p in P:
    assert is_prime_trial(p)
    got = (multiplicative_order(2, p),
           multiplicative_order(3, p))
    assert got == expected_orders[p], (p, got, expected_orders[p])

    h, g, a, b = coordinates(p)
    assert h == lcm(*expected_orders[p])
    assert pow(g, a, p) == 2
    assert pow(g, b, p) == 3
    data[p] = (h, g, a, b)
    print(p, expected_orders[p], "h =", h,
          "g =", g, "map =", (a, b))

def pair_image_size(p, q):
    hp, _, ap, bp = data[p]
    hq, _, aq, bq = data[q]

    gens = [
        (ap % hp, aq % hq),  # image of (1,0)
        (bp % hp, bq % hq),  # image of (0,1)
    ]

    seen = {(0, 0)}
    todo = deque([(0, 0)])
    while todo:
        x, y = todo.popleft()
        for u, v in gens:
            z = ((x + u) % hp, (y + v) % hq)
            if z not in seen:
                seen.add(z)
                todo.append(z)
    return len(seen)

tree_edges = [
    (5, 7), (5, 11), (5, 13), (5, 17), (5, 23),
    (5, 31), (5, 37), (5, 41), (5, 47), (5, 73),
    (5, 71), (5, 431), (5, 601), (5, 167),
    (7, 19), (7, 29), (7, 43),
]

assert len(tree_edges) == len(P) - 1

for p, q in tree_edges:
    hp = data[p][0]
    hq = data[q][0]
    size = pair_image_size(p, q)
    assert size == hp * hq, (p, q, size, hp * hq)

S = sum(Fraction(1, data[p][0]) for p in P)
W = sum(Fraction(1, data[p][0] * data[q][0])
        for p, q in tree_edges)

print("S =", S, float(S))
print("W =", W, float(W))
print("Hunter upper bound =", S - W, float(S - W))
print("Required outside mass =", 1 - S + W, float(1 - S + W))

assert S - W < 1

lower_quotient = 4 * 11 * 23 * 43 * 75 * 83
assert lower_quotient == 270_887_100
print("Quotient lower bound:", lower_quotient)
```

A direct exact SAT implementation for a moderate candidate pool is:

```python
from math import gcd, lcm
from pysat.formula import CNF, IDPool
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver

def solve_flat_sat(primes, max_cells=20_000_000):
    """
    Uses coordinates(p) from the preceding code.
    Exact, but only practical when the rectangular quotient is moderate.
    """
    rows = []
    for p in primes:
        h, g, a, b = coordinates(p)
        period_k = h // gcd(h, a)
        period_l = h // gcd(h, b)
        rows.append((p, h, g, a, b, period_k, period_l))

    A = 1
    B = 1
    for _, _, _, _, _, ak, bl in rows:
        A = lcm(A, ak)
        B = lcm(B, bl)

    print("Rectangular period:", A, B, "cells:", A * B)
    if A * B > max_cells:
        raise RuntimeError("Exact flat quotient too large")

    pool = IDPool()
    cnf = CNF()

    def X(i, c):
        return pool.id(("target", i, c))

    # Exactly one target for each prime.
    for i, (_, h, _, _, _, _, _) in enumerate(rows):
        lits = [X(i, c) for c in range(h)]
        enc = CardEnc.equals(
            lits=lits, bound=1, vpool=pool,
            encoding=EncType.seqcounter
        )
        cnf.extend(enc.clauses)

    # One covering clause per residue pair.
    seen_clauses = set()
    for k in range(A):
        for ell in range(B):
            clause = tuple(
                X(i, (a * k + b * ell) % h)
                for i, (_, h, _, a, b, _, _) in enumerate(rows)
            )
            if clause not in seen_clauses:
                seen_clauses.add(clause)
                cnf.append(list(clause))

    print("Distinct point clauses:", len(seen_clauses))

    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as solver:
        if not solver.solve():
            return None

        model = set(x for x in solver.get_model() if x > 0)
        answer = []
        for i, (p, h, g, _, _, _, _) in enumerate(rows):
            choices = [c for c in range(h) if X(i, c) in model]
            assert len(choices) == 1
            c = choices[0]
            target = pow(g, c, p)
            answer.append((p, c, target))
        return answer
```

For large pools, the next computation should replace the rectangular enumeration by:

1. a master SAT instance containing only sampled point clauses;
2. exact separation of a proposed target assignment using HNF/SNF lattice-coset subtraction;
3. addition of an uncovered witness clause;
4. iteration until either the master becomes UNSAT or the residual lattice-coset list is empty.

Any eventual positive result must retain the final target list and an independently checkable exact residual-empty certificate.

## Route Diagnosis

Route 1 yielded two useful conclusions. First, the ordinary LP relaxation should be abandoned: it is mathematically equivalent to the reciprocal-mass test. Second, unavoidable pair overlaps provide a cheap and rigorous pre-SAT obstruction; maximum-spanning-tree Hunter bounds should be computed for every candidate pool before expensive search.

The route is blocked at the integral search stage. Pools confined to compatible small periods have too little effective mass after forced overlaps, while adding the useful odd and diagonal periods makes the exact quotient enormous—the benchmark pool already forces at least \(270{,}887{,}100\) classes and still cannot cover. Symbolic lattice subtraction avoids explicit enumeration but presently has uncontrolled fragmentation.

A fresh attempt should:

1. Generate a much larger prime database with certified \((h_p,\alpha_p,\beta_p)\), correcting the \(p=601\) order.
2. Use maximum-spanning-tree and stronger higher-order overlap bounds to discard inadequate pools before SAT.
3. Optimize for **adjusted mass and character diversity**, not raw \(\sum1/h_p\).
4. Run lazy CP-SAT with exact HNF/SNF separation and retain proof traces.
5. If residual splitting repeatedly aligns into a few lattice fibers, switch deliberately to Route 2 and finish those fibers hierarchically; otherwise the flat finite-cover route remains computationally blocked.