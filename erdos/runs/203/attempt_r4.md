STATUS: BLOCKED
## Result

I did not resolve Erdős Problem #203. I obtained several rigorous obstructions to the most direct Route 4 constructions. In particular: (i) an ordinary Sierpiński covering lifts to two dimensions only under an explicit finite compatibility condition on its slopes; (ii) the classical covering for \(78557\) cannot lift, even after arbitrary retargeting of its odd covering primes, because its total two-dimensional covering mass is only \(11/18\); (iii) all the principal small primes and affine-line primes highlighted in the brief—even after adding \(61\) and the exceptional prime \(89\)—fail a necessary parity-projected covering inequality; (iv) common-slope lifting cannot work with the supplied affine-line primes; and (v) primes with a single common equal order \(q\) can never by themselves provide the \(q\) lines needed to cover \(\mathbb Z_q^2\). The remaining possibility is a genuinely mixed-slope, mixed-period hierarchical cover using additional primes. Constructing or excluding such a cover remains an unresolved finite-cover problem of comparable strength to the original affirmative route.

## Complete Argument

### 1. Every prime predicate is an affine cyclic line

Let \(p\ge 5\), let
\[
H_p=\langle 2,3\rangle\leq \mathbb F_p^\times,
\qquad |H_p|=h_p,
\]
and choose a generator \(g\) of \(H_p\). Write
\[
2=g^a,\qquad 3=g^b.
\]
Because \(2\) and \(3\) generate \(H_p\),
\[
\gcd(a,b,h_p)=1.
\]
For a target \(t=g^c\in H_p\),
\[
2^k3^\ell=t
\quad\Longleftrightarrow\quad
ak+b\ell\equiv c\pmod{h_p}.
\]
Thus every prime covers one affine cyclic line
\[
C_p(c)=\{(k,\ell)\in\mathbb Z^2:ak+b\ell\equiv c\pmod{h_p}\}.
\]
On \(\mathbb Z_{h_p}^2\), the homomorphism
\[
(k,\ell)\longmapsto ak+b\ell
\]
is surjective, so its kernel has \(h_p\) elements. Consequently every such line has density \(1/h_p\).

This includes primes for which \(3\notin\langle2\rangle\); the special Route 4 form occurs when \(2\) generates \(H_p\).

---

### 2. Exact criterion for lifting a one-dimensional covering

Suppose \(3\in\langle2\rangle\pmod p\), and put
\[
n_p=\operatorname{ord}_p(2)=h_p.
\]
There is a unique \(d_p\pmod{n_p}\) such that
\[
3\equiv 2^{d_p}\pmod p.
\]
Writing the target as \(2^{c_p}\), the prime predicate becomes
\[
k+d_p\ell\equiv c_p\pmod{n_p}. \tag{2.1}
\]

Consider finitely many such primes, indexed by \(i\), with data
\[
(n_i,d_i,c_i).
\]
Let
\[
N=\operatorname{lcm}_i n_i.
\]

#### Lemma 2.1: finite lift criterion

The lines
\[
k+d_i\ell\equiv c_i\pmod{n_i}
\]
cover \(\mathbb Z^2\) if and only if, for every \(\ell\pmod N\), the one-dimensional residue classes
\[
k\equiv c_i-d_i\ell\pmod{n_i}
\]
cover all integers \(k\).

#### Proof

For fixed \(\ell\), equation (2.1) is precisely
\[
k\equiv c_i-d_i\ell\pmod{n_i}.
\]
Every predicate is periodic in \(\ell\) modulo \(n_i\), hence the complete collection is periodic modulo \(N\). Therefore checking \(\ell\pmod N\) is necessary and sufficient. ∎

In particular, an ordinary covering at \(\ell=0\) is necessary but not sufficient.

#### Corollary 2.2: common-slope lift

If there is an integer \(D\) such that
\[
d_i\equiv D\pmod{n_i}
\]
for every \(i\), then any one-dimensional covering
\[
\mathbb Z=\bigcup_i\{x:x\equiv c_i\pmod{n_i}\}
\]
lifts to the two-dimensional covering
\[
\mathbb Z^2
=
\bigcup_i
\{(k,\ell):k+d_i\ell\equiv c_i\pmod{n_i}\}.
\]

Indeed, set \(x=k+D\ell\).

Moreover, every selected prime then divides
\[
2^D-3,
\]
after replacing \(D\) by a sufficiently large positive representative modulo \(\operatorname{lcm}_i n_i\). Conversely, every prime \(p\ge5\) dividing \(2^D-3\) satisfies
\[
3\equiv2^D\pmod p.
\]

Thus a common-slope search for fixed \(D\) reduces exactly to factoring \(2^D-3\) and asking whether one residue class for each order \(\operatorname{ord}_p(2)\) can cover \(\mathbb Z\).

---

### 3. An exact compatibility test for exact one-dimensional coverings

Suppose the one-dimensional residue classes
\[
c_i\pmod{n_i}
\]
form an exact covering: every integer lies in exactly one class. Then
\[
\sum_i\frac1{n_i}=1.
\]

#### Lemma 3.1

The lifted lines
\[
k+d_i\ell\equiv c_i\pmod{n_i}
\]
cover \(\mathbb Z^2\) if and only if, for every \(i\ne j\),
\[
\gcd\!\bigl(d_i-d_j,\gcd(n_i,n_j)\bigr)
\nmid c_i-c_j. \tag{3.1}
\]

#### Proof

Put \(g_{ij}=\gcd(n_i,n_j)\). Lines \(i\) and \(j\) intersect if and only if there is an \(\ell\) such that the two congruences in \(k\),
\[
k\equiv c_i-d_i\ell\pmod{n_i},
\qquad
k\equiv c_j-d_j\ell\pmod{n_j},
\]
are compatible. By the generalized CRT, this is equivalent to
\[
(d_i-d_j)\ell\equiv c_i-c_j\pmod{g_{ij}}.
\]
This congruence is solvable exactly when
\[
\gcd(d_i-d_j,g_{ij})\mid c_i-c_j.
\]

On the common torus \(\mathbb Z_N^2\), line \(i\) has density \(1/n_i\). Since the one-dimensional covering is exact,
\[
\sum_i\frac1{n_i}=1.
\]
Hence the total number of line memberships equals the number of points in the torus. The lines cover the torus if and only if every point has exactly one membership, which is equivalent to pairwise disjointness. Applying the intersection criterion proves (3.1). ∎

A useful consequence is that two lifted lines with coprime moduli always intersect, because then \(g_{ij}=1\). Thus an exact lift cannot contain two coprime moduli.

This criterion is sharp, but most promising two-dimensional constructions will need covering mass strictly greater than \(1\), so it does not settle the general case.

---

### 4. The classical covering for \(78557\) does not lift

The standard covering for \(78557\) uses the following classes on the \(k\)-axis:

\[
\begin{array}{c|c|c}
p&\operatorname{ord}_p(2)& k\text{-class}\\ \hline
3&2&0\pmod2\\
5&4&1\pmod4\\
7&3&1\pmod3\\
13&12&11\pmod{12}\\
19&18&15\pmod{18}\\
37&36&27\pmod{36}\\
73&9&3\pmod9
\end{array}
\]

For example, these classes follow from
\[
78557\bmod(3,5,7,13,19,37,73)
=(2,2,3,11,11,6,9)
\]
and the corresponding target residues \(-78557^{-1}\).

To verify the cover, reduce modulo \(36\). The prime \(3\) covers all even residues. Among the odd residues:

- \(1\pmod4\) covers
  \[
  1,5,9,13,17,21,25,29,33;
  \]
- \(1\pmod3\) additionally covers
  \[
  7,19,31;
  \]
- \(11\pmod{12}\) covers
  \[
  11,23,35;
  \]
- \(15\pmod{18}\) covers \(15\);
- \(27\pmod{36}\) covers \(27\);
- \(3\pmod9\) covers \(3\).

Hence every \(k\) is covered.

For the two-dimensional problem, however, \(3\) covers no point with \(\ell\ge1\). The two-dimensional masses of the remaining primes are

\[
\frac14,\quad \frac16,\quad \frac1{12},\quad
\frac1{18},\quad\frac1{36},\quad\frac1{36}.
\]
Their sum is
\[
\frac14+\frac16+\frac1{12}+\frac1{18}+\frac1{36}+\frac1{36}
=\frac{11}{18}<1.
\]
Therefore these odd primes cannot cover \(\mathbb Z^2\), regardless of how their targets are chosen.

For the targets specifically induced by \(m=78557\), the pair
\[
(k,\ell)=(3,1)
\]
is not covered by any of these primes. Indeed,
\[
2^3\cdot3\cdot78557+1=1\,885\,369,
\]
and direct reduction gives nonzero residues modulo
\[
3,5,7,13,19,37,73.
\]
This only shows failure of the classical covering primes; it makes no claim that this term is prime.

---

### 5. A parity-projection obstruction

The affine character has a useful coarse projection modulo \(2\).

Let
\[
ak+b\ell\equiv c\pmod h,
\qquad \gcd(a,b,h)=1.
\]

- If \(h\) is odd, then inside each of the four parity cells
  \[
  (k\bmod2,\ell\bmod2)\in\mathbb F_2^2
  \]
  the conditional density of the coset remains \(1/h\).

- If \(h\) is even, reducing modulo \(2\) gives one affine line
  \[
  (a\bmod2)k+(b\bmod2)\ell=c\bmod2.
  \]
  This contains two parity cells. In each of those cells the conditional density is \(2/h\), and in the other two it is \(0\).

To prove the second assertion, fix a compatible parity pair
\[
k=\epsilon+2x,\qquad \ell=\delta+2y.
\]
After dividing the congruence by \(2\), one obtains a surjective homomorphism on
\(\mathbb Z_{h/2}^2\), because
\[
\gcd(a,b,h/2)=1.
\]
It has \(h/2\) solutions among \((h/2)^2\) pairs, giving conditional density \(2/h\).

The parity of \(a\) can be read from the order of \(2=g^a\):
\[
\operatorname{ord}(2)=\frac h{\gcd(a,h)}.
\]
When \(h\) is even, \(a\) is odd exactly when \(h/\operatorname{ord}(2)\) is odd. The analogous statement holds for \(b\).

#### Proposition 5.1: a natural 20-prime Route 4 pool cannot cover

Consider
\[
\begin{aligned}
\mathcal P=\{&
5,7,11,13,17,19,23,29,31,37,41,43,47,61,71,73,\\
&89,167,431,601\}.
\end{aligned}
\]
This consists of all primes highlighted in the two order tables, together with \(61\) from the suggested dense stage and the exceptional \(89\).

No choice of one target coset for each prime in \(\mathcal P\) covers \(\mathbb Z^2\).

#### Proof

The odd-\(h\) primes are
\[
23,47,71,431,601,167
\]
with
\[
h=11,23,35,43,75,83.
\]
Their uniform conditional contribution to every parity cell is
\[
O=\frac1{11}+\frac1{23}+\frac1{35}
+\frac1{43}+\frac1{75}+\frac1{83}. \tag{5.1}
\]

The even-\(h\) primes divide into three parity directions.

1. Normal vector \((1,1)\), so they select one of the two diagonals:
   \[
   5,19,29,43.
   \]
   Their conditional weights \(2/h\) are
   \[
   \frac12,\quad\frac19,\quad\frac1{14},\quad\frac1{21}.
   \]

2. Normal vector \((0,1)\), so they select one value of \(\ell\bmod2\):
   \[
   7,17,31,73,41,89.
   \]

3. Normal vector \((1,0)\), so they select one value of \(k\bmod2\):
   \[
   11,13,37,61.
   \]

The corresponding order data are those in the brief, supplemented by
\[
\operatorname{ord}_{61}(2)=60,\qquad
\operatorname{ord}_{61}(3)=10,
\]
and
\[
\operatorname{ord}_{89}(2)=11,\qquad
\operatorname{ord}_{89}(3)=88.
\]
For \(61\),
\[
2^{30}\equiv-1,\quad 2^{20}\equiv47,\quad 2^{12}\equiv9\pmod{61},
\]
which certifies order \(60\), while \(3^5\equiv-1\pmod{61}\), giving order \(10\).
For \(89\),
\[
2^{11}\equiv1\pmod{89},
\]
and
\[
3^8\equiv64,\qquad 3^{44}\equiv-1\pmod{89},
\]
which certifies order \(88\).

The prime \(5\) chooses one parity diagonal. Let \(D_*\) be the opposite diagonal. The other diagonal primes have total conditional weight
\[
A=\frac19+\frac1{14}+\frac1{21}
=\frac{29}{126}.
\]
Thus their total contribution, summed over the two cells of \(D_*\), is at most
\[
2A=\frac{29}{63}.
\]

Every vertical parity line contains exactly one of the two cells of \(D_*\). Excluding \(89\) temporarily, the total vertical conditional weight is
\[
B=\frac13+\frac18+\frac1{15}+\frac1{18}+\frac1{20}
=\frac{227}{360}.
\]
Similarly, the total horizontal conditional weight is
\[
C=\frac15+\frac16+\frac1{18}+\frac1{30}
=\frac{41}{90}.
\]
Hence
\[
B+C=\frac{391}{360}.
\]
The prime \(89\) contributes an additional summed weight
\[
\frac2{88}=\frac1{44}.
\]

If both parity cells in \(D_*\) were completely covered, the sum of the conditional covering masses in those two cells would have to be at least \(2\). The union bound gives the necessary inequality
\[
2O+\frac{29}{63}+\frac{391}{360}+\frac1{44}\ge2. \tag{5.2}
\]
But
\[
\frac{29}{63}+\frac{391}{360}=\frac{433}{280}.
\]

We now bound \(O\) rationally. First,
\[
\frac1{23}+\frac1{35}
=\frac{58}{805}<\frac{13}{180}.
\]
Also
\[
\frac1{43}+\frac1{75}+\frac1{83}
<
\frac7{300}+\frac1{75}+\frac1{80}
=\frac{59}{1200}<\frac1{20}.
\]
Therefore
\[
O<\frac1{11}+\frac{13}{180}+\frac1{20}
=\frac{211}{990}.
\]
Moreover,
\[
\frac{211}{990}<\frac{1327}{6160}
=\frac12\left(2-\frac{433}{280}-\frac1{44}\right),
\]
as is seen by cross-multiplication:
\[
211\cdot6160=1\,299\,760
<
1\,313\,730=1327\cdot990.
\]
It follows that
\[
2O+\frac{433}{280}+\frac1{44}<2,
\]
contradicting the necessary inequality (5.2). Hence the pool cannot cover. ∎

Numerically, the upper bound using the exact value of \(O\) is approximately
\[
1.99235.
\]
Thus the parity obstruction is real but narrow: a few well-chosen additional primes could remove this particular obstruction.

---

### 6. Common-slope lifting cannot use the supplied affine-line primes efficiently

For the seven smallest highlighted primes satisfying \(3\in\langle2\rangle\), the data are

\[
\begin{array}{c|c|c}
p&n_p=\operatorname{ord}_p(2)&d_p,\quad 3\equiv2^{d_p}\pmod p\\ \hline
5&4&3\\
11&10&8\\
13&12&4\\
19&18&13\\
23&11&8\\
29&28&5\\
37&36&26
\end{array}
\]

A common slope \(D\) can include two entries only if
\[
d_i\equiv d_j\pmod{\gcd(n_i,n_j)}. \tag{6.1}
\]

Among the six primes other than \(23\):

- If \(5\) is included, it is compatible only with \(19\). Their mass is
  \[
  \frac14+\frac1{18}=\frac{11}{36}.
  \]

- If \(5\) is omitted and \(11\) is included, then \(11\) is incompatible with \(19\) and \(29\). It is compatible with both \(13\) and \(37\), but \(13\) and \(37\) are mutually incompatible because
  \[
  4\not\equiv26\pmod{12}.
  \]
  The largest resulting mass is
  \[
  \frac1{10}+\frac1{12}=\frac{11}{60}.
  \]

- If both \(5\) and \(11\) are omitted, then \(13\) is incompatible with \(19,29,37\), while \(19\) and \(29\) are compatible with one another but incompatible with \(37\). The maximum is less than \(11/60\).

Thus the maximum mass among these six is \(11/36\). Since \(11\) is coprime to all their moduli, \(23\) may always be added, giving at most
\[
\frac{11}{36}+\frac1{11}
=\frac{157}{396}<\frac25. \tag{6.2}
\]

The other supplied equal-order affine-line primes have orders
\[
23,35,43,75,83
\]
for \(p=47,71,431,601,167\), respectively. Even if all of them, and also \(61\), were compatible with the same slope, their additional mass would be less than
\[
\frac1{20}+\frac1{30}+\frac1{40}+\frac1{70}+\frac1{80}+\frac1{60}
<\frac15.
\]
Combining this with (6.2), every common-slope subfamily drawn from these highlighted primes has total mass less than
\[
\frac25+\frac15=\frac35<1.
\]
Therefore no common-slope one-dimensional covering can be made from this pool.

This does not rule out common-slope constructions using many additional prime divisors of some \(2^D-3\).

---

### 7. One equal-order family can never cover its own affine plane

#### Proposition 7.1

Fix \(n\ge2\). The primes satisfying
\[
\operatorname{ord}_p(2)=\operatorname{ord}_p(3)=n
\]
cannot, with one target per prime, cover \(\mathbb Z_n^2\).

#### Proof

Every such prime divides \(2^n-1\), and \(n\mid p-1\), so
\[
p\ge n+1.
\]
If there were \(n\) distinct such primes, their product would divide \(2^n-1\), but it would be at least
\[
(n+1)^n>2^n>2^n-1,
\]
a contradiction. Hence there are fewer than \(n\) such primes.

Each corresponding affine line contains exactly \(n\) points of \(\mathbb Z_n^2\). Fewer than \(n\) lines therefore cover fewer than
\[
n\cdot n=n^2
\]
points, even before accounting for overlaps. ∎

Thus every equal-order family, such as the \(q=11,23,43,83\) families in Route 4, necessarily needs substantial help from primes of different orders.

For \(q=11\), this can be made completely explicit:
\[
2^{11}-1=2047=23\cdot89.
\]
Now \(23\mid3^{11}-1\), while
\[
3^{11}-1\equiv36\pmod{89}.
\]
Hence
\[
\gcd(2^{11}-1,3^{11}-1)=23.
\]
The only prime with both orders equal to \(11\) is therefore \(23\), giving the single line
\[
k+8\ell\equiv c\pmod{11},
\]
since \(3\equiv2^8\pmod{23}\).

The prime \(89\) is genuinely different. Since
\[
3^{16}\equiv2\pmod{89}
\]
and \(3\) has order \(88\), its character is
\[
16k+\ell\equiv c\pmod{88}.
\]
It does not descend to a line on \(\mathbb Z_{11}^2\).

---

### 8. Running ledger

#### Proved

1. Every prime predicate is one affine cyclic equation
   \[
   ak+b\ell\equiv c\pmod h.
   \]

2. For primes with \(3\in\langle2\rangle\), an ordinary covering lifts exactly when every shifted covering at \(\ell\pmod N\) remains complete.

3. For exact one-dimensional coverings, the pairwise criterion (3.1) is necessary and sufficient for lifting.

4. A common-slope construction for slope \(D\) uses only prime divisors of \(2^D-3\).

5. The classical \(78557\) covering primes have only \(11/18\) two-dimensional mass after \(p=3\) is removed, so they cannot lift.

6. The 20-prime pool \(\mathcal P\) above fails a rigorous parity-projected covering inequality.

7. The supplied affine-line primes cannot furnish a common-slope covering.

8. An equal-order family can never alone cover its corresponding \(n\times n\) torus.

#### Plausible but unproved

1. A larger mixed-slope pool may admit a finite covering.

2. Parity and higher \(2\)-adic projections may provide useful LP dual certificates for pruning candidate pools.

3. Some \(D\) may have enough compatible prime divisors of \(2^D-3\) to support a one-dimensional covering, though the small heavy primes are strongly incompatible.

#### Dead ends

1. Directly lifting the classical \(78557\) covering: impossible by density.

2. Using only one equal-order family: impossible by Proposition 7.1.

3. Using a single common slope with the highlighted primes: impossible by density and slope incompatibility.

4. Using only the natural small-prime pool from the brief, even with \(61\) and \(89\): impossible by the parity certificate.

## Self-Audit

1. **The parity obstruction depends on finite multiplicative-order data.**  
   The order values for the displayed primes come from the brief, while I supplied explicit checks only for \(61\) and \(89\). I believe the result holds because every remaining order is certified by the deterministic code below and by the standard order criterion; there is no probabilistic computation involved.

2. **The common-slope obstruction only treats the highlighted affine-line primes.**  
   It does not exclude a large prime factorization of some \(2^D-3\) with total reciprocal-order mass at least \(1\). The stated conclusion is deliberately limited to the supplied pool, where the compatibility analysis and density bound are exact.

3. **The route diagnosis is not a proof that Route 4 is globally impossible.**  
   Mixed slopes and additional primes evade all proved obstructions above. I regard the route as blocked, rather than disproved, because finishing it now requires an exact large finite-cover search or a new structural theorem; neither has been supplied.

## Computations To Verify

The following code verifies the order data, the parity obstruction, the classical covering, and the \(q=11\) calculations.

```python
from math import gcd, lcm
from fractions import Fraction
from sympy import factorint, isprime

def multiplicative_order(a, p):
    assert isprime(p) and a % p
    n = p - 1
    for q in factorint(p - 1):
        while n % q == 0 and pow(a, n // q, p) == 1:
            n //= q
    return n

primes = [
    5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
    41, 43, 47, 61, 71, 73, 89, 167, 431, 601
]

data = {}
for p in primes:
    o2 = multiplicative_order(2, p)
    o3 = multiplicative_order(3, p)
    h = lcm(o2, o3)
    data[p] = (o2, o3, h)
    print(p, o2, o3, h)

expected = {
    5:(4,4,4), 7:(3,6,6), 11:(10,5,10),
    13:(12,3,12), 17:(8,16,16), 19:(18,18,18),
    23:(11,11,11), 29:(28,28,28), 31:(5,30,30),
    37:(36,18,36), 41:(20,8,40), 43:(14,42,42),
    47:(23,23,23), 61:(60,10,60), 71:(35,35,35),
    73:(9,12,36), 89:(11,88,88), 167:(83,83,83),
    431:(43,43,43), 601:(75,75,75)
}
assert data == expected

# For even h, parity of the exponent coefficient a is odd exactly
# when h/o2 is odd; similarly for b.
def parity_signature(o2, o3, h):
    assert h % 2 == 0
    return ((h // o2) % 2, (h // o3) % 2)

groups = {"diag": [], "vertical": [], "horizontal": [], "odd": []}
for p, (o2, o3, h) in data.items():
    if h % 2:
        groups["odd"].append(p)
    else:
        sig = parity_signature(o2, o3, h)
        if sig == (1, 1):
            groups["diag"].append(p)
        elif sig == (0, 1):
            groups["vertical"].append(p)
        elif sig == (1, 0):
            groups["horizontal"].append(p)
        else:
            raise AssertionError((p, sig))

print(groups)
assert set(groups["diag"]) == {5,19,29,43}
assert set(groups["vertical"]) == {7,17,31,41,73,89}
assert set(groups["horizontal"]) == {11,13,37,61}
assert set(groups["odd"]) == {23,47,71,167,431,601}

O = sum(Fraction(1, data[p][2]) for p in groups["odd"])
A = sum(Fraction(2, data[p][2])
        for p in groups["diag"] if p != 5)
B_without_89 = sum(Fraction(2, data[p][2])
                   for p in groups["vertical"] if p != 89)
C = sum(Fraction(2, data[p][2])
        for p in groups["horizontal"])
W89 = Fraction(2, data[89][2])

upper_two_opposite_cells = 2*O + 2*A + B_without_89 + C + W89
print("Parity upper bound:", upper_two_opposite_cells,
      float(upper_two_opposite_cells))
assert upper_two_opposite_cells < 2

# Classical 78557 covering on the k-axis.
m = 78557
classic = [
    (3, 2, 0),
    (5, 4, 1),
    (7, 3, 1),
    (13, 12, 11),
    (19, 18, 15),
    (37, 36, 27),
    (73, 9, 3),
]
for k in range(36):
    assert any(k % n == c and (pow(2, k, p)*m + 1) % p == 0
               for p, n, c in classic)

N = 2**3 * 3 * m + 1
assert all(N % p != 0 for p, _, _ in classic)
print("Uncovered classical-lift term:", N)

mass = (
    Fraction(1,4) + Fraction(1,6) + Fraction(1,12)
    + Fraction(1,18) + Fraction(1,36) + Fraction(1,36)
)
assert mass == Fraction(11,18)

# q = 11 equal-order check and p = 89 warning.
G = gcd(2**11 - 1, 3**11 - 1)
assert G == 23
assert pow(2, 8, 23) == 3
assert pow(3, 16, 89) == 2
assert multiplicative_order(2, 89) == 11
assert multiplicative_order(3, 89) == 88
```

A concrete common-slope search can be run as follows. A successful output would already be a genuine two-dimensional finite cover.

```python
from math import lcm
from sympy import factorint
from ortools.sat.python import cp_model

def common_slope_instance(D, period_cap=2_000_000):
    """
    Factor 2^D - 3.  For every prime factor p >= 5, use
    n_p = ord_p(2). Search for at most one class c mod n_p
    per prime that covers every residue modulo N = lcm(n_p).
    """
    factors = [int(p) for p in factorint(2**D - 3) if p >= 5]
    orders = {p: multiplicative_order(2, p) for p in factors}

    if sum(Fraction(1, n) for n in orders.values()) < 1:
        return None

    N = 1
    for n in orders.values():
        N = lcm(N, n)
        if N > period_cap:
            return "PERIOD_TOO_LARGE"

    model = cp_model.CpModel()
    x = {}
    for p, n in orders.items():
        for c in range(n):
            x[p, c] = model.NewBoolVar(f"x_{p}_{c}")
        model.Add(sum(x[p, c] for c in range(n)) <= 1)

    for r in range(N):
        model.Add(sum(x[p, r % n] for p, n in orders.items()) >= 1)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 300
    status = solver.Solve(model)
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return None

    selected = []
    for p, n in orders.items():
        for c in range(n):
            if solver.Value(x[p, c]):
                selected.append((p, n, c))
    return D, N, selected

for D in range(3, 500):
    ans = common_slope_instance(D)
    if ans not in (None, "PERIOD_TOO_LARGE"):
        print("FOUND COMMON-SLOPE COVER:", ans)
        break
```

If this returns a cover \((p,n,c)\), use targets \(t_p=2^c\bmod p\), solve
\[
m\equiv-t_p^{-1}\pmod p,
\]
and verify the resulting CRT class as in the brief.

## Route Diagnosis

Route 4 works cleanly at the structural level: every eligible Sierpiński congruence becomes a line \(k+d\ell=c\), and both general lifting and exact lifting have complete finite criteria. What fails is the supply and organization of lines. Classical coverings lose the density-\(1/2\) contribution of \(p=3\); same-order families contain fewer than the \(q\) lines needed to cover their own plane; common slopes cannot combine the main heavy primes; and the most natural mixed pool fails already after projection to \(\mathbb F_2^2\).

The route is blocked precisely at the following problem: find targets for a substantially larger collection of mixed-slope primes whose affine cyclic cosets cover every class in the relevant intersection quotient. None of the proved obstructions excludes this, and resolving it is essentially the desired finite-cover construction.

A fresh attempt should therefore switch from hand-designed equal-order families to an exact hierarchical SAT/column-generation search:

1. enumerate many primes and compute their affine characters \(ak+b\ell=c\pmod h\);
2. impose parity and higher \(2\)-adic projections first, using LP duals to reject pools;
3. retain primes specifically selected to repair the hard diagonal identified above;
4. represent residuals in Smith-normal-form coordinates rather than a huge rectangular period;
5. only after a coarse feasible solution is found, lift and solve the finer residual exactly.

The common-slope factor search over \(2^D-3\) is worth running in parallel because any success reduces the two-dimensional problem to a one-dimensional covering certificate, but the compatibility data above make it unlikely that small \(D\) or the currently highlighted primes suffice.