STATUS: PARTIAL

## Result

I did not resolve Erdős Problem #203. I proved a general necessary condition for any finite exponent-lattice covering: in an inclusion-minimal cover, if a prime \(q\) divides the lattice index \(h_p\) of one selected covering prime, then at least \(q\) selected indices must be divisible by \(q\); if there are exactly \(q\), their reductions modulo \(q\) must be parallel affine lines. This “\(q\)-cohort obstruction” rigorously rules out the entire 20-prime pool explicitly suggested in Route 2, even after adjoining \(p=89\). I then constructed natural complete projective shadow pencils modulo \(5\) and \(7\), but an exact density/intersection argument proves that the resulting 22-prime hierarchical pool still cannot cover \(\mathbb Z^2\), despite having total nominal mass greater than \(1\).

## Complete Argument

### 1. Affine equations and their prime shadows

For a prime \(p\ge 5\), fix an isomorphism
\[
H_p=\langle 2,3\rangle \simeq \mathbb Z/h_p\mathbb Z.
\]
Under this isomorphism there are \(\alpha_p,\beta_p\in\mathbb Z/h_p\mathbb Z\) such that
\[
2^k3^\ell\longmapsto \alpha_pk+\beta_p\ell.
\]
Since \(2,3\) generate \(H_p\),
\[
\gcd(\alpha_p,\beta_p,h_p)=1.
\]
A target coset for \(p\) therefore has the form
\[
C_p(c)=\{(k,\ell)\in\mathbb Z^2:
\alpha_pk+\beta_p\ell\equiv c\pmod{h_p}\}.
\]
It has density \(1/h_p\).

If a rational prime \(q\mid h_p\), reduction modulo \(q\) gives a nonzero linear functional
\[
\lambda_{p,q}(k,\ell)
=\bar\alpha_pk+\bar\beta_p\ell\in\mathbb F_q.
\]
The full coset \(C_p(c)\) is contained in the affine line
\[
\lambda_{p,q}(k,\ell)=\bar c
\]
in \(\mathbb F_q^2\). I call this the \(q\)-shadow of the coset.

The projective direction
\[
[\bar\alpha_p:\bar\beta_p]\in\mathbb P^1(\mathbb F_q)
\]
is independent of the chosen isomorphism \(H_p\simeq\mathbb Z/h_p\mathbb Z\), because changing the isomorphism multiplies both coefficients by a unit.

---

### 2. The \(q\)-cohort theorem

**Theorem 1.**  
Let
\[
\mathbb Z^2=\bigcup_{i=1}^r (a_i+L_i)
\]
be an inclusion-minimal finite cover, where every \(L_i\) has cyclic quotient and index
\[
h_i=[\mathbb Z^2:L_i].
\]
For a rational prime \(q\), put
\[
I_q=\{i:q\mid h_i\}.
\]
If \(I_q\ne\varnothing\), then:

1. \(|I_q|\ge q\).
2. If \(|I_q|=q\), the \(q\)-shadows of these \(q\) cosets are \(q\) distinct parallel affine lines. In particular, all their projective normal directions are equal.

**Proof.**

Let
\[
J_q=\{1,\dots,r\}\setminus I_q.
\]
Because the cover is inclusion-minimal and \(I_q\ne\varnothing\), the subfamily indexed by \(J_q\) cannot cover \(\mathbb Z^2\). Choose
\[
x\notin\bigcup_{j\in J_q}(a_j+L_j).
\]
Set
\[
M=\bigcap_{j\in J_q}L_j,
\]
with \(M=\mathbb Z^2\) if \(J_q=\varnothing\).

Every coset indexed by \(J_q\) is periodic under \(M\), so the whole translate \(x+M\) avoids all those cosets. Consequently,
\[
x+M\subseteq\bigcup_{i\in I_q}(a_i+L_i).
\]

Each index \([\mathbb Z^2:L_j]\), \(j\in J_q\), is coprime to \(q\). Hence
\[
[\mathbb Z^2:M]
\]
is coprime to \(q\). If a basis matrix for \(M\) has determinant \([\mathbb Z^2:M]\), it is invertible modulo \(q\). Thus inclusion induces an isomorphism
\[
M/qM\simeq \mathbb Z^2/q\mathbb Z^2\simeq\mathbb F_q^2.
\]

For \(i\in I_q\), the condition \(x+y\in a_i+L_i\) implies one nonzero affine linear equation in \(y\bmod qM\). Thus each \(i\in I_q\) contributes an affine line in the two-dimensional affine plane \(M/qM\). These lines cover \(M/qM\), which has \(q^2\) points.

Each affine line has exactly \(q\) points. Therefore at least \(q\) lines are required, proving \(|I_q|\ge q\).

If exactly \(q\) lines cover \(q^2\) points, their total cardinality \(q\cdot q=q^2\) leaves no room for overlap. Hence they are pairwise disjoint. Distinct nonparallel affine lines in \(\mathbb F_q^2\) intersect, so all \(q\) lines must be parallel. They must also be distinct. ∎

**Corollary 2.**  
In any inclusion-minimal finite cover, every prime divisor \(q\) occurring in any selected index \(h_i\) must occur in at least \(q\) selected indices.

This is a substantial restriction on the proposed use of isolated line primes such as \(23,47,167,\) or \(431\).

---

### 3. The explicitly suggested Route 2 pool cannot cover

Consider the enlarged pool
\[
\begin{aligned}
\mathcal P=\{&
5,7,11,13,17,19,23,29,31,37,41,43,47,61,\\
&71,73,89,167,431,601\}.
\end{aligned}
\]
This contains all primes explicitly proposed in Route 2, together with \(89\).

Their indices are
\[
\begin{array}{c|rrrrrrrrrr}
p&5&7&11&13&17&19&23&29&31&37\\ \hline
h_p&4&6&10&12&16&18&11&28&30&36
\end{array}
\]
and
\[
\begin{array}{c|rrrrrrrrrr}
p&41&43&47&61&71&73&89&167&431&601\\ \hline
h_p&40&42&23&60&35&36&88&83&43&75.
\end{array}
\]

The value \(h_{61}=60\), not explicitly tabulated in the brief, follows as follows:
\[
2^{30}\equiv-1,\qquad
2^{20}\equiv47,\qquad
2^{12}\equiv9\pmod{61},
\]
so \(\operatorname{ord}_{61}(2)=60\). Also
\[
3\equiv2^6\pmod{61},
\]
so \(\operatorname{ord}_{61}(3)=60/\gcd(60,6)=10\).

Suppose a subfamily of this pool covers \(\mathbb Z^2\), and take an inclusion-minimal subcover.

- The only indices divisible by \(7\) are
  \[
  h_{29}=28,\qquad h_{43}=42,\qquad h_{71}=35.
  \]
  There are only three, fewer than \(7\). By Theorem 1, none of \(29,43,71\) can occur in the minimal cover.

- After \(71\) is removed, the only indices divisible by \(5\) are those belonging to
  \[
  11,31,41,61,601.
  \]
  There are exactly five. If any occurs, Theorem 1 forces all five to occur and their mod-\(5\) shadow lines to be parallel.

  But modulo \(11\), with \(2\) as generator,
  \[
  3=2^8,
  \]
  so the normal for \(p=11\), reduced modulo \(5\), is
  \[
  (1,8)\equiv(1,3).
  \]
  Modulo \(31\), \(3\) has order \(30\), and
  \[
  3^9=-2,\qquad 3^{15}=-1,
  \]
  whence
  \[
  3^{24}=2.
  \]
  Thus the normal for \(p=31\) is
  \[
  (24,1)\equiv(4,1)\pmod5.
  \]
  These two vectors are not proportional because
  \[
  \det\begin{pmatrix}1&3\\4&1\end{pmatrix}
  =1-12\equiv4\not\equiv0\pmod5.
  \]
  Hence their shadows are not parallel. Therefore none of
  \[
  11,31,41,61,601
  \]
  can occur.

- The only indices divisible by \(11\) are \(h_{23}=11\) and \(h_{89}=88\). Since \(2<11\), neither can occur.

- The only index divisible by \(23\) is \(h_{47}=23\), so \(47\) cannot occur.

- The only index divisible by \(43\) is \(h_{431}=43\), so \(431\) cannot occur.

- The only index divisible by \(83\) is \(h_{167}=83\), so \(167\) cannot occur.

Thus any minimal cover supported on \(\mathcal P\) would have to use only
\[
\{5,7,13,17,19,37,73\}.
\]
Their total mass is
\[
\frac14+\frac16+\frac1{12}+\frac1{16}
+\frac1{18}+\frac1{36}+\frac1{36}
=\frac{97}{144}<1.
\]
A finite union of periodic sets whose densities sum to less than \(1\) cannot cover \(\mathbb Z^2\). This is a contradiction.

Therefore:

**Proposition 3.**  
No finite exponent-lattice cover can be constructed using only the 20-prime pool \(\mathcal P\).

---

### 4. Complete shadow pencils modulo \(5\) and \(7\)

The cohort theorem suggests that primes should be assembled in aligned batches rather than added individually.

#### A complete mod-\(5\) pencil

Consider
\[
\mathcal Q_5=\{11,31,41,61,241,601\}.
\]
Their mod-\(5\) projective normal directions are
\[
\begin{array}{c|c}
p&\text{normal direction in }\mathbb P^1(\mathbb F_5)\\ \hline
41&(1,0)\\
61&(1,1)\\
601&(1,2)\\
11&(1,3)\\
31&(1,4)\\
241&(0,1).
\end{array}
\]
Thus they realize all six points of \(\mathbb P^1(\mathbb F_5)\).

The identities establishing these directions are:

- \(p=11\): \(3=2^8\), giving \((1,8)\equiv(1,3)\).
- \(p=31\): \(2=3^{24}\), giving \((24,1)\sim(1,4)\).
- \(p=41\):
  \[
  2^8\equiv10\ne1,\qquad 3^8\equiv1\pmod{41},
  \]
  giving \((1,0)\).
- \(p=61\): \(3=2^6\), giving \((1,6)\equiv(1,1)\).
- \(p=241\):
  \[
  \operatorname{ord}_{241}(2)=24,\qquad
  \operatorname{ord}_{241}(3)=120,
  \]
  so only \(3\) has nontrivial \(5\)-component, giving \((0,1)\).
- \(p=601\): since both orders are \(75\), write \(3=2^d\). Directly,
  \[
  2^{15}\equiv314,\qquad
  3^{15}\equiv32,\qquad
  314^2\equiv32\pmod{601},
  \]
  so \(d\equiv2\pmod5\).

Choosing all six mod-\(5\) intercepts to be zero gives all six lines through the origin in \(\mathbb F_5^2\), which cover that affine plane.

#### A complete mod-\(7\) pencil

Likewise, let
\[
\mathcal Q_7=\{29,43,71,113,127,211,631,757\}.
\]
Their directions are
\[
\begin{array}{c|c}
p&\text{normal direction in }\mathbb P^1(\mathbb F_7)\\ \hline
757&(1,0)\\
211&(1,1)\\
71&(1,2)\\
113&(1,3)\\
127&(1,4)\\
29&(1,5)\\
43&(1,6)\\
631&(0,1).
\end{array}
\]
Hence they realize all eight points of \(\mathbb P^1(\mathbb F_7)\).

Relevant identities are:

- \(p=29\): \(3=2^5\).
- \(p=43\): \(3^6=-2\), \(3^{21}=-1\), hence \(2=3^{27}\).
- \(p=71\):
  \[
  2^5=32,\qquad 3^5=30,\qquad 32^2=30\pmod{71},
  \]
  giving exponent ratio \(2\bmod7\).
- \(p=113\):
  \[
  3^{16}=49,\qquad 2^{16}=109,\qquad49^5=109\pmod{113},
  \]
  giving normal \((5,1)\sim(1,3)\).
- \(p=127\):
  \[
  3^9=-2,\qquad3^{63}=-1,
  \]
  so \(2=3^{72}\), and \((72,1)\equiv(2,1)\sim(1,4)\).
- \(p=211\):
  \[
  2^{30}=3^{30}=171,
  \]
  giving exponent ratio \(1\bmod7\).
- \(p=631\):
  \[
  \operatorname{ord}_{631}(2)=45,\qquad
  \operatorname{ord}_{631}(3)=630,
  \]
  so only \(3\) has a nontrivial \(7\)-component.
- \(p=757\):
  \[
  \operatorname{ord}_{757}(2)=756,\qquad
  \operatorname{ord}_{757}(3)=9,
  \]
  so only \(2\) has a nontrivial \(7\)-component.

Again, choosing zero mod-\(7\) intercepts yields all eight lines through the origin, covering \(\mathbb F_7^2\).

These pencils satisfy the necessary prime-shadow geometry, but they do not themselves give a full cover: a shadow condition modulo \(q\) is only a necessary part of the full congruence modulo \(h_p\).

---

### 5. Order certificates for the added primes

The required new orders are
\[
\begin{array}{c|c|c|c}
p&\operatorname{ord}_p(2)&\operatorname{ord}_p(3)&h_p\\ \hline
97&48&48&48\\
113&28&112&112\\
127&7&126&126\\
211&210&210&210\\
241&24&120&120\\
631&45&630&630\\
757&756&9&756.
\end{array}
\]

For an asserted order \(n\), it is enough to verify \(a^n=1\) and
\[
a^{n/r}\ne1
\]
for each prime \(r\mid n\). The following residues provide such certificates:

\[
\begin{array}{c|l|l}
p&2\text{-power checks}&3\text{-power checks}\\ \hline
97&
2^{24}=-1,\ 2^{16}=61&
3^{24}=-1,\ 3^{16}=61\\
113&
2^{14}=-1,\ 2^4=16&
3^{56}=-1,\ 3^{16}=49\\
127&
2^7=1,\ 2\ne1&
3^{63}=-1,\ 3^{42}=107,\ 3^{18}=4\\
211&
2^{105}=-1,\ 2^{70}=196,\ 2^{42}=107,\ 2^{30}=171&
3^{105}=-1,\ 3^{70}=196,\ 3^{42}=188,\ 3^{30}=171\\
241&
2^{12}=-1,\ 2^8=15&
3^{60}=-1,\ 3^{40}=15,\ 3^{24}=91\\
631&
2^{45}=1,\ 2^{15}=587,\ 2^9=512&
3^{315}=-1,\ 3^{210}=587,\ 3^{126}=242,\ 3^{90}=269\\
757&
2^{378}=-1,\ 2^{252}=27,\ 2^{108}=232&
3^9=1,\ 3^3=27.
\end{array}
\]
All congruences are modulo the prime in the first column. Primality of these small numbers is verified by trial division through their square roots.

---

### 6. A 22-prime hierarchical pool with mass \(>1\) still fails

Let
\[
\mathcal B=\{5,7,13,17,19,37,73\}
\]
and consider
\[
\mathcal S=\mathcal B\cup\mathcal Q_5\cup\mathcal Q_7\cup\{97\}.
\]
This is a 22-prime pool incorporating complete mod-\(5\) and mod-\(7\) shadow pencils.

Its masses are
\[
\sum_{p\in\mathcal B}\frac1{h_p}
=\frac{97}{144},
\]
\[
\sum_{p\in\mathcal Q_5}\frac1{h_p}
=
\frac1{10}+\frac1{30}+\frac1{40}+\frac1{60}
+\frac1{120}+\frac1{75}
=\frac{59}{300},
\]
and
\[
\sum_{p\in\mathcal Q_7}\frac1{h_p}
=
\frac1{28}+\frac1{42}+\frac1{35}+\frac1{112}
+\frac1{126}+\frac1{210}+\frac1{630}+\frac1{756}
=\frac{1703}{15120}.
\]
Including \(p=97\), the total is
\[
T=\frac{97}{144}+\frac{59}{300}
+\frac{1703}{15120}+\frac1{48}
=\frac{75883}{75600}>1.
\]

Nevertheless, this pool cannot cover.

For \(p=5\), using \(2\) as generator,
\[
3=2^3,
\]
so its cosets are
\[
k+3\ell\equiv a\pmod4.
\]
For \(p=7\), using \(3\) as generator,
\[
2=3^2,
\]
so its cosets are
\[
2k+\ell\equiv b\pmod6.
\]

For every \(a\bmod4\) and \(b\bmod6\), these two equations have joint density \(1/24\). Indeed, the first equation gives
\[
k=\ell+a+4u.
\]
Substitution into the second gives
\[
3\ell+2a+2u\equiv b\pmod6.
\]
As the parity of \(\ell\) and \(u\bmod3\) vary, the expression \(3\ell+2u\) assumes all six residues modulo \(6\). Thus the combined map to
\[
\mathbb Z/4\mathbb Z\times\mathbb Z/6\mathbb Z
\]
is surjective and every pair of target cosets intersects with density \(1/24\).

Now consider any subfamily of \(\mathcal S\).

- If it contains both \(5\) and \(7\), its union has density at most
  \[
  T-\frac1{24}
  =\frac{75883-3150}{75600}<1.
  \]
- If it omits \(5\), its total mass is at most
  \[
  T-\frac14<1.
  \]
- If it omits \(7\), its total mass is at most
  \[
  T-\frac16<1.
  \]

Therefore no subfamily covers \(\mathbb Z^2\).

Equivalently:

**Proposition 4.**  
The 22-prime hierarchical pool \(\mathcal S\), despite total mass \(>1\) and complete mod-\(5\) and mod-\(7\) shadow pencils, admits no finite coset covering.

More generally, any finite candidate pool containing \(5\) and \(7\) and having total mass
\[
T<\frac{25}{24}
\]
cannot contain a covering subfamily. This criterion would rule out any rigorously enumerated smooth-period pool with reported mass around \(1.02\)–\(1.03\).

## Self-Audit

1. **This only obstructs finite covering constructions, not the original everywhere-composite problem.**  
   A hypothetical valid \(m\) might use infinitely many distinct prime divisors. I have not proved any finite-subcover principle, so this is genuinely partial.

2. **The shadow theorem depends on passing to an inclusion-minimal finite cover.**  
   This is legitimate because every finite cover has an inclusion-minimal subcover. The lattice \(M\) has index coprime to \(q\), so its reduction modulo \(q\) really is all of \(\mathbb F_q^2\); this is the crucial point preventing a loss of dimension.

3. **The mod-\(5\) and mod-\(7\) pencils cover only prime shadows, not full lattice cosets.**  
   I make no claim that they furnish a cover. Their directions and order computations are independently checkable, and Proposition 4 in fact proves that this particular hierarchical attempt fails.

## Computations To Verify

```python
from fractions import Fraction
from math import gcd, lcm
from sympy import (
    isprime, n_order, primitive_root, factorint
)

P0 = [
    5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
    41, 43, 47, 61, 71, 73, 89, 167, 431, 601
]

expected_h = {
    5: 4, 7: 6, 11: 10, 13: 12, 17: 16, 19: 18,
    23: 11, 29: 28, 31: 30, 37: 36, 41: 40,
    43: 42, 47: 23, 61: 60, 71: 35, 73: 36,
    89: 88, 167: 83, 431: 43, 601: 75,
    97: 48, 113: 112, 127: 126, 211: 210,
    241: 120, 631: 630, 757: 756,
}

def order_data(p):
    assert isprime(p)
    o2 = n_order(2, p)
    o3 = n_order(3, p)
    return o2, o3, lcm(o2, o3)

for p, h in expected_h.items():
    o2, o3, hp = order_data(p)
    assert hp == h, (p, o2, o3, hp, h)

# Obtain coefficients alpha,beta in a cyclic H_p.
def exponent_vector(p):
    g = primitive_root(p)
    logs = {}
    x = 1
    for e in range(p - 1):
        logs[x] = e
        x = x * g % p

    A = logs[2]
    B = logs[3]
    d = gcd(gcd(A, B), p - 1)
    h = (p - 1) // d
    alpha = (A // d) % h
    beta = (B // d) % h
    assert gcd(gcd(alpha, beta), h) == 1
    assert h == lcm(n_order(2, p), n_order(3, p))
    return h, (alpha, beta)

def projective_direction(p, q):
    h, (a, b) = exponent_vector(p)
    assert h % q == 0
    a %= q
    b %= q
    assert (a, b) != (0, 0)
    if a:
        z = pow(a, -1, q)
        return (1, b * z % q)
    return (0, 1)

Q5 = [11, 31, 41, 61, 241, 601]
Q7 = [29, 43, 71, 113, 127, 211, 631, 757]

assert {projective_direction(p, 5) for p in Q5} == (
    {(1, a) for a in range(5)} | {(0, 1)}
)
assert {projective_direction(p, 7) for p in Q7} == (
    {(1, a) for a in range(7)} | {(0, 1)}
)

# Iterative q-cohort pruning. Each deletion is justified by Theorem 1.
def qcore(candidate_primes):
    active = set(candidate_primes)

    while True:
        changed = False
        qs = set()
        for p in active:
            h = exponent_vector(p)[0]
            qs.update(factorint(h).keys())

        for q in sorted(qs):
            cohort = [p for p in active if exponent_vector(p)[0] % q == 0]
            if 0 < len(cohort) < q:
                active.difference_update(cohort)
                changed = True
                break

            if len(cohort) == q:
                directions = {
                    projective_direction(p, q) for p in cohort
                }
                if len(directions) > 1:
                    active.difference_update(cohort)
                    changed = True
                    break

        if not changed:
            return active

active0 = qcore(P0)
assert active0 == {5, 7, 13, 17, 19, 37, 73}

mass0 = sum(
    Fraction(1, exponent_vector(p)[0]) for p in active0
)
assert mass0 == Fraction(97, 144)

# The 22-prime hierarchical pool.
B = {5, 7, 13, 17, 19, 37, 73}
S22 = B | set(Q5) | set(Q7) | {97}

mass22 = sum(
    Fraction(1, exponent_vector(p)[0]) for p in S22
)
assert mass22 == Fraction(75883, 75600)
assert 1 < mass22 < Fraction(25, 24)

# Verify that every p=5 target intersects every p=7 target
# in density exactly 1/24, using a safe 12 x 12 period.
for a in range(4):
    for b in range(6):
        count = 0
        for k in range(12):
            for ell in range(12):
                if ((k + 3*ell - a) % 4 == 0 and
                    (2*k + ell - b) % 6 == 0):
                    count += 1
        assert count == 6
        assert Fraction(count, 144) == Fraction(1, 24)

print("Suggested 20-prime q-core:", sorted(active0))
print("Its mass:", mass0)
print("22-prime hierarchical mass:", mass22)
print("All checks passed.")
```

A next search should enumerate primes by their \(q\)-shadow directions before solving any set-cover instance:

```python
from collections import defaultdict
from sympy import primerange

def shadow_inventory(bound, qs=(5, 7, 11, 23)):
    out = {q: defaultdict(list) for q in qs}
    for p in primerange(5, bound):
        h, _ = exponent_vector(p)
        for q in qs:
            if h % q == 0:
                d = projective_direction(p, q)
                out[q][d].append((p, h))
    return out

inventory = shadow_inventory(100000)
for q in inventory:
    print("q =", q)
    for direction, items in sorted(inventory[q].items()):
        print(direction, items[:20])
```

This directly tests whether complete parallel classes or projective pencils exist with enough actual reciprocal mass.

## Route Diagnosis

The hierarchical idea is not hopeless, but the originally suggested implementation is structurally blocked. A large-index line prime cannot be used as an isolated residual patch: selecting \(p=47\), for example, forces a cohort of at least \(23\) selected indices divisible by \(23\); selecting \(p=431\) forces at least \(43\) indices divisible by \(43\). The explicitly suggested pool fails this test decisively.

What worked was organizing primes into complete projective shadow pencils. The sets \(\mathcal Q_5\) and \(\mathcal Q_7\) give exact coarse geometries on \(\mathbb F_5^2\) and \(\mathbb F_7^2\). What remains blocked is lifting those shadows to full congruences without wasting mass. The 22-prime attempt has total mass only
\[
\frac{75883}{75600}\approx1.00374,
\]
while the unavoidable \(p=5,p=7\) overlap already costs \(1/24\). Any continuation retaining this pool must add at least
\[
\frac{25}{24}-\frac{75883}{75600}
=\frac{2867}{75600}\approx0.037923
\]
of nominal reciprocal mass merely to clear that first rigorous obstruction.

A fresh attempt should therefore be cohort-first rather than prime-first:

1. Enumerate a substantially larger smooth-index pool.
2. Apply iterative \(q\)-cohort pruning before SAT or greedy selection.
3. Build complete parallel classes or projective pencils for every prime factor \(q\) introduced.
4. Add exact pairwise-overlap inequalities, beginning with the forced \(1/24\) overlap of \(p=5\) and \(p=7\), to the LP/SAT model.
5. Only then compute the exact residual in Smith-normal-form coordinates.

No finite covering certificate, and hence no valid \(m\), has been obtained.