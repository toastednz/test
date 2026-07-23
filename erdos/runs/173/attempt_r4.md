STATUS: BLOCKED

## Result

I did not solve Erdős Problem #173. I proved a complete rigidity theorem for the motivating alternating-strip construction: for strips of equal width \(w\), the unique exceptional triangle is the equilateral triangle of altitude \(w\). Thus the standard sharpness example has exceptional set exactly one, not merely at least one. I also derived exact structural constraints for arbitrary one-dimensional colorings, several general propagation lemmas for arbitrary triangle-avoiding colorings, and rigorous high-entropy constructions showing why local or single-orientation classification does not extend directly to arbitrary plane colorings. The global Route 4 classification remains blocked at the step of extracting unconditional translation symmetries from conditional NAE constraints.

## Complete Argument

### 1. General pointwise consequences of avoiding a triangle

Let \(T=\{p_1,p_2,p_3\}\), and write
\[
\sigma(x)=(-1)^{\chi(x)}\in\{-1,1\}.
\]

#### Lemma 1.1: Exact Boolean identity

A coloring avoids monochromatic congruent copies of \(T\) if and only if, for every isometry \(g\),
\[
\sigma(gp_1)\sigma(gp_2)
+\sigma(gp_2)\sigma(gp_3)
+\sigma(gp_3)\sigma(gp_1)=-1.
\]

**Proof.**
If the three signs are equal, all three pairwise products are \(1\), so the sum is \(3\). Otherwise exactly two signs are equal and the third is opposite; the three products are then \(1,-1,-1\), with sum \(-1\). These are the only possibilities. ∎

This identity is exact but nonlinear: it does not itself give a global period or antiperiod.

#### Lemma 1.2: Forced completion over a monochromatic side

Suppose \(a\) is a side length of \(T\), and \(P,Q\) are same-colored points with \(|P-Q|=a\). Let \(R_+\) and \(R_-\) be the two completions of \(PQ\) to copies of \(T\) using that side assignment. Then
\[
\chi(R_+)=\chi(R_-)=1-\chi(P).
\]
In particular, if \(h_a\) is the altitude of \(T\) to the side \(a\), then \(R_+,R_-\) form a monochromatic pair of the opposite color at distance \(2h_a\).

**Proof.**
Each of \(\{P,Q,R_+\}\) and \(\{P,Q,R_-\}\) is a copy of \(T\). Since \(P,Q\) have the same color and a monochromatic copy is forbidden, each completion point must have the other color. Reflection across \(PQ\) interchanges the two completions, whose separation is \(2h_a\). ∎

There is always some same-colored pair at every prescribed distance \(d\): take an equilateral triangle of side \(d\), and use pigeonhole. Thus Lemma 1.2 always produces at least one forced kite for every side of an avoided triangle. The obstruction is that it does not control which color occurs on the initial base.

#### Lemma 1.3: Both color classes are relatively dense

If \(\chi\) avoids a triangle \(T\) of circumradius \(R\), then every closed disk of radius \(R\) contains both colors.

**Proof.**
Given a center \(x\), place a copy of \(T\) on the circle of radius \(R\) centered at \(x\). Its three vertices are not monochromatic, so both colors occur in the disk. ∎

This is genuine global structure, but it is far weaker than periodicity or one-dimensionality.

---

### 2. Complete classification for alternating equal-width strips

For \(w>0\), define
\[
\chi_w(x,y)=\left\lfloor \frac{y}{w}\right\rfloor\pmod 2.
\]

#### Theorem 2.1: Exact exceptional set of the standard strip coloring

A nondegenerate triangle is avoided by \(\chi_w\) if and only if it is equilateral with altitude \(w\), equivalently with side length
\[
\frac{2w}{\sqrt3}.
\]
Consequently,
\[
E(\chi_w)
=
\left\{
\left[\text{equilateral triangle of side }2w/\sqrt3\right]
\right\}.
\]

#### Proof

By scaling, it suffices to take \(w=1\).

---

#### Step 1: An exact projection criterion

Define
\[
\delta(t)=\operatorname{dist}(t,2\mathbb Z)\in[0,1].
\]
For three projected heights \(y_1,y_2,y_3\), set
\[
D(y_1,y_2,y_3)
=
\sum_{1\le i<j\le3}\delta(y_i-y_j).
\]

We claim:

> There is no vertical translation \(t\) for which
> \[
> \lfloor y_1+t\rfloor,\quad
> \lfloor y_2+t\rfloor,\quad
> \lfloor y_3+t\rfloor
> \]
> have the same parity if and only if \(D(y_1,y_2,y_3)=2\).

Regard the residues of the \(y_i\) as points on the circle \(\mathbb R/2\mathbb Z\), and let their cyclic gaps be \(g_1,g_2,g_3\ge0\), with
\[
g_1+g_2+g_3=2.
\]

A common color after translation exists exactly when all three residues fit into a rotated half-open interval of length \(1\). For a finite set, that happens exactly when one cyclic gap is strictly larger than \(1\).

If every \(g_i\le1\), each cyclic gap is also the geodesic distance between the corresponding pair, so
\[
D=g_1+g_2+g_3=2.
\]
If, say, \(g_1>1\), then \(q=g_2+g_3=2-g_1<1\). The three pairwise geodesic distances are \(g_2,g_3,q\), and hence
\[
D=g_2+g_3+q=2q<2.
\]
This proves the criterion, including boundary cases where a gap equals exactly \(1\).

Let \(P_1,P_2,P_3\) be fixed coordinates for the triangle. Under an arbitrary rigid placement, its vertical coordinates have the form
\[
t+n\cdot P_i,\qquad |n|=1.
\]
Reflections introduce no additional projected triples because \(n\) still ranges over the entire unit circle. Therefore the triangle is avoided exactly when
\[
F(n):=
\sum_{i<j}\delta\bigl(n\cdot(P_i-P_j)\bigr)=2
\tag{2.1}
\]
for every unit vector \(n\).

---

#### Step 2: Every altitude must be an odd integer

Fix a side \(P_iP_j\), and take \(n\) perpendicular to that side. The endpoints then have equal projections, while the third vertex differs from them by the altitude \(h\) to that side. Hence
\[
F(n)=2\delta(h).
\]
Equation (2.1) gives \(\delta(h)=1\), which is equivalent to
\[
h\in 2\mathbb Z+1.
\tag{2.2}
\]
Thus all three altitudes are positive odd integers.

---

#### Step 3: The triangle must be acute

Take a side in coordinates
\[
P=(0,0),\qquad Q=(L,0),\qquad R=(x,H),
\]
where \(H\) is an odd integer by Step 2. For small \(\varepsilon>0\), put
\[
n_\varepsilon=(\varepsilon,\sqrt{1-\varepsilon^2}).
\]
Near an odd integer \(H\),
\[
\delta(H+s)=1-|s|
\]
for sufficiently small \(s\), while \(\delta(L\varepsilon)=L\varepsilon\). Thus
\[
F(n_\varepsilon)
=
2+L\varepsilon
-\left|x\varepsilon+O(\varepsilon^2)\right|
-\left|(x-L)\varepsilon+O(\varepsilon^2)\right|.
\]
Since \(F(n_\varepsilon)=2\), division by \(\varepsilon\) and passage to the limit gives
\[
L=|x|+|x-L|.
\]
Hence
\[
0\le x\le L.
\]
Applying this to every side shows that the triangle is nonobtuse.

It cannot be right. Indeed, in a right triangle with legs \(L,H\), the altitudes to the two legs are \(H,L\), while the altitude to the hypotenuse \(C\) is
\[
k=\frac{LH}{C}.
\]
All three would be odd integers. Then \(C=LH/k\) would be rational. Since
\[
C^2=L^2+H^2\in\mathbb Z,
\]
a rational \(C\) must be an integer. But \(L,H\) odd gives
\[
C^2\equiv1+1\equiv2\pmod4,
\]
impossible for an integer square. Therefore the triangle is acute, and in the above coordinates
\[
0<x<L.
\tag{2.3}
\]

---

#### Step 4: Every side longer than \(2\) must be an axis of symmetry

Suppose \(L>2\), and set
\[
s=\sqrt{1-\frac4{L^2}},\qquad
n_\pm=\left(\frac2L,\pm s\right).
\]
Then
\[
n_\pm\cdot(Q-P)=2,
\]
so \(P,Q\) have the same residue modulo \(2\). Equation (2.1) therefore forces \(R\) to be antipodal to that residue:
\[
\frac{2x}{L}\pm Hs\in2\mathbb Z+1.
\tag{2.4}
\]
Averaging the two odd integers in (2.4) shows that
\[
\frac{2x}{L}\in\mathbb Z.
\]
By (2.3), \(0<2x/L<2\), and hence
\[
x=\frac L2.
\tag{2.5}
\]
Thus the triangle is isosceles over every side whose length exceeds \(2\).

Moreover,
\[
B:=Hs
\]
is an integer, because it is half the difference of the two integers in (2.4).

---

#### Step 5: Classify the odd altitude triples

Let the altitudes be \(h_a,h_b,h_c\), and let \(\Delta\) be the area. Since
\[
a h_a=b h_b=c h_c=2\Delta,
\]
the side lengths are inversely proportional to their altitudes.

Let
\[
m=\min\{h_a,h_b,h_c\},
\]
and choose \(a\) corresponding to \(m\), so \(a\) is a longest side.

##### Case 1: \(m=1\)

If only one altitude were \(1\), the other two would be at least \(3\), and the triangle inequality would give
\[
1<\frac1{h_b}+\frac1{h_c}\le\frac23,
\]
after dividing the side lengths by their common factor. This is impossible. Thus at least two altitudes equal \(1\).

If all three equal \(1\), all side lengths are equal, giving the desired equilateral triangle.

Otherwise the altitudes are, after relabeling,
\[
1,1,M,\qquad M\ge3\text{ odd}.
\]
The corresponding sides are
\[
K,K,\frac K M
\]
for some \(K>0\). The altitude \(M\) is drawn to the short side \(K/M\), so in this acute isosceles triangle \(K>M\ge3\). In particular \(K>2\).

Apply Step 4 to one of the long sides \(K\). It says the other two sides must be equal. Those other sides have lengths \(K\) and \(K/M\), a contradiction.

##### Case 2: \(m\ge3\)

The longest side \(a\) is longer than its altitude \(m\), so \(a>2\). By Step 4, the triangle is isosceles over \(a\). Write the other two sides as equal and let their common altitude be \(n\). Then
\[
n\ge m.
\]

Put the base length \(a=L\), its altitude \(m\), and coordinates
\[
P=(0,0),\quad Q=(L,0),\quad R=(L/2,m).
\]
If \(S\) is either equal side, then
\[
S^2=m^2+\frac{L^2}{4}.
\]
The altitude \(n\) to \(S\) satisfies
\[
n=\frac{Lm}{S}.
\]
Consequently
\[
L^2=\frac{4m^2n^2}{4m^2-n^2}.
\tag{2.6}
\]

From Step 4,
\[
B=m\sqrt{1-\frac4{L^2}}
\]
is an integer. Using (2.6),
\[
B^2
=m^2+1-\frac{4m^2}{n^2}.
\tag{2.7}
\]
Thus \(4m^2/n^2\) is an integer. Since \(n\) is odd,
\[
n^2\mid m^2,
\]
so \(n\mid m\). Together with \(n\ge m\), this gives \(n=m\).

Equation (2.7) now becomes
\[
B^2=m^2-3.
\]
But an odd square is \(1\pmod8\), so
\[
B^2\equiv1-3\equiv6\pmod8,
\]
which is impossible for an integer square.

Therefore Case 2 cannot occur.

We have proved that an avoided triangle must be equilateral with altitude \(1\).

---

#### Step 6: The matching equilateral triangle is indeed avoided

Let the equilateral triangle have altitude \(1\), hence side
\[
s=\frac2{\sqrt3}.
\]
For any projection direction, sort the projected coordinates and write the adjacent gaps as \(A,B\ge0\). The three pairwise projected differences are
\[
A,\quad B,\quad A+B.
\]

The sum of their squares is
\[
\frac32s^2=2,
\]
so
\[
A^2+B^2+(A+B)^2=2,
\]
equivalently
\[
A^2+AB+B^2=1.
\]
It follows that
\[
A,B\le1,\qquad
1\le A+B\le\frac2{\sqrt3}<2.
\]
Therefore
\[
\delta(A)=A,\quad
\delta(B)=B,\quad
\delta(A+B)=2-(A+B),
\]
and hence
\[
F(n)=A+B+2-(A+B)=2.
\]
By the projection criterion, no translate is monochromatic. This completes the proof of Theorem 2.1. ∎

---

### 3. Arbitrary one-dimensional colorings

The preceding theorem used the special alternating profile, but one structural fact survives for every coloring of the form
\[
\chi(x,y)=f(y),\qquad f:\mathbb R\to\mathbb Z/2\mathbb Z.
\]

#### Proposition 3.1: Altitudes are global antiperiods

If \(\chi(x,y)=f(y)\) avoids a triangle whose altitudes are \(h_1,h_2,h_3\), then
\[
f(t+h_i)=1-f(t)
\tag{3.1}
\]
for every \(t\in\mathbb R\) and every \(i\).

**Proof.**
Place the side corresponding to \(h_i\) horizontally at height \(t\). Its two endpoints both have color \(f(t)\). The third vertex has height \(t+h_i\), and must have the opposite color. Since \(t\) is arbitrary, (3.1) follows. ∎

#### Corollary 3.2: Parity obstruction among the altitudes

For every integer relation
\[
n_1h_1+n_2h_2+n_3h_3=0,
\]
one must have
\[
n_1+n_2+n_3\equiv0\pmod2.
\tag{3.2}
\]

**Proof.**
Translation by each \(h_i\) flips \(f\). Translation by an integer combination therefore flips \(f\) according to the parity of \(n_1+n_2+n_3\), including negative coefficients. Translation by zero cannot flip every value of \(f\), so the parity must be even. ∎

For example, if \(h_i/h_j=p/q\) in lowest terms, then \(p,q\) must both be odd.

The condition is sharp for the side-parallel constraints alone. Let
\[
H=\langle h_1,h_2,h_3\rangle_{\mathbb Z}\subset\mathbb R.
\]
If every integer relation satisfies (3.2), then
\[
\varphi\left(\sum n_i h_i\right)=\sum n_i\pmod2
\]
is a well-defined homomorphism \(H\to\mathbb Z/2\mathbb Z\). Choosing one representative from every coset of \(H\) and an arbitrary base color on every coset, define
\[
f(r+h)=b_r+\varphi(h).
\]
Then every \(h_i\) is an antiperiod. This construction may be highly nonmeasurable when \(H\) is dense.

It does not guarantee avoidance in non-side-parallel orientations, but it shows that arbitrary one-dimensional profiles need not become periodic even when several exact antiperiods are forced.

---

### 4. Why local classification does not presently globalize

#### Proposition 4.1: All translates of one orientation have many avoiding colorings

Write a triangle as
\[
T=\{0,u,v\}
\]
with \(u,v\) linearly independent, and let
\[
H=\mathbb Zu+\mathbb Zv.
\]
Choose arbitrary base colors \(b_C\) for the cosets \(C\) of \(H\) in \(\mathbb R^2\), and define
\[
\chi(r+mu+nv)=b_{r+H}+m\pmod2.
\]
Then every translated copy
\[
\{x,x+u,x+v\}
\]
is nonmonochromatic.

**Proof.**
Its colors have the form
\[
c,\quad c+1,\quad c.
\]
Thus it contains both colors. ∎

Hence the continuum of translation constraints for a single orientation has \(2^{\mathfrak c}\) solutions. Rigidity, if true, must use interactions among different rotations.

#### Proposition 4.2: A single circumcircle generally has high entropy

Fix a circumcircle of \(T\), parameterized by \(\mathbb R/2\pi\mathbb Z\), and write one inscribed copy as
\[
\{0,\alpha,\beta\}.
\]
Let
\[
H=\langle\alpha,\beta\rangle
\]
inside the circle group. If there is a homomorphism
\[
\varphi:H\to\mathbb Z/2\mathbb Z
\]
with
\[
(\varphi(\alpha),\varphi(\beta))\ne(0,0),
\]
then one can color each coset of \(H\) independently and extend by
\[
c(r+h)=b_r+\varphi(h).
\]
Every rotated copy
\[
\{t,t+\alpha,t+\beta\}
\]
and every reflected copy
\[
\{t,t-\alpha,t-\beta\}
\]
is nonmonochromatic.

For generic \(\alpha,\beta\), the group \(H\cong\mathbb Z^2\), so such a nonzero character exists, and the circle constraint has \(2^{\mathfrak c}\) solutions.

Even the equilateral case has high entropy: every orbit
\[
\{\theta,\theta+2\pi/3,\theta+4\pi/3\}
\]
can independently receive any nonmonochromatic coloring.

Thus restrictions to individual circumcircles do not force strip-like behavior.

## Self-Audit

1. **The half-open strip boundaries are the most delicate technical point.** The proof uses a strict cyclic-gap criterion: a common color phase exists exactly when a cyclic gap is \(>1\), not merely \(\ge1\). I believe this is correct because three points lying in a half-open interval of length \(1\) have actual span strictly less than \(1\); antipodal endpoints cannot both lie in the same half-open color interval.

2. **The “long side implies isosceles” step depends on exact, not approximate, modular coincidences.** I used directions satisfying \(n\cdot(Q-P)=2\), available only when \(L>2\), and then used \(F(n)=2\) to force the third projection to be an odd integer. Every later application has \(L>3\), so there is no omitted \(L=2\) boundary case.

3. **The partial structural results do not justify any classification of arbitrary plane colorings.** The antiperiod argument applies only when the coloring already factors through one linear coordinate, while the circumcircle and fixed-orientation constructions are diagnostic examples rather than global counterexamples. I have made no inference from them to the full conjecture.

## Computations To Verify

The following code numerically checks the strip theorem over odd altitude triples and samples all orientations. It is only a verification aid; the proof above is exact.

```python
import math
from itertools import combinations_with_replacement

def triangle_from_altitudes(h):
    """
    Given desired altitudes h=(ha,hb,hc), reconstruct the unique
    side lengths a,b,c if their reciprocals satisfy triangle inequalities.
    """
    a0, b0, c0 = (1.0 / x for x in h)
    if not (a0 < b0 + c0 and b0 < a0 + c0 and c0 < a0 + b0):
        return None

    s0 = (a0 + b0 + c0) / 2.0
    area0 = math.sqrt(s0 * (s0-a0) * (s0-b0) * (s0-c0))

    # Scaling by lam makes altitude to a equal ha, etc.
    lam = 1.0 / (2.0 * area0)
    return lam*a0, lam*b0, lam*c0

def coordinates(sides):
    a, b, c = sides
    # |P0P1|=a, |P0P2|=b, |P1P2|=c
    x = (a*a + b*b - c*c) / (2.0*a)
    y2 = b*b - x*x
    if y2 <= 0:
        raise ValueError("Degenerate")
    return [(0.0, 0.0), (a, 0.0), (x, math.sqrt(y2))]

def delta2(t):
    r = t % 2.0
    return min(r, 2.0-r)

def strip_F(points, theta):
    n = (math.cos(theta), math.sin(theta))
    vals = [n[0]*x + n[1]*y for x, y in points]
    return sum(delta2(vals[i]-vals[j])
               for i in range(3) for j in range(i+1, 3))

def sampled_min_F(h, samples=200000):
    sides = triangle_from_altitudes(h)
    if sides is None:
        return None
    pts = coordinates(sides)
    return min(strip_F(pts, math.pi*k/samples)
               for k in range(samples))

# Only (1,1,1) should have sampled minimum numerically equal to 2.
for h in combinations_with_replacement(range(1, 16, 2), 3):
    val = sampled_min_F(h, samples=20000)
    if val is not None:
        print(h, val)
```

The arithmetic obstruction in the \(m\ge3\) isosceles case can be checked exactly:

```python
from fractions import Fraction
from math import isqrt

def is_integer_square(q):
    if q.denominator != 1 or q.numerator < 0:
        return False
    r = isqrt(q.numerator)
    return r*r == q.numerator

for m in range(3, 101, 2):
    for n in range(m, 2*m, 2):  # odd n with m <= n < 2m
        B2 = Fraction(m*m + 1, 1) - Fraction(4*m*m, n*n)
        assert not is_integer_square(B2), (m, n, B2)
```

The high-entropy triangular-lattice family can be checked finitely as follows:

```python
from itertools import product

def color(m, n, row_bits):
    return (m + row_bits[n]) & 1

def check_rows(N=6, M=6):
    # Rows n=0,...,N. Every choice of row bits works.
    for bits in product([0, 1], repeat=N+1):
        b = dict(enumerate(bits))

        for n in range(N):
            for m in range(-M, M):
                # Upward elementary triangle:
                tri1 = [
                    color(m,   n,   b),
                    color(m+1, n,   b),
                    color(m,   n+1, b),
                ]
                assert len(set(tri1)) == 2

                # Downward elementary triangle:
                tri2 = [
                    color(m,   n+1, b),
                    color(m+1, n+1, b),
                    color(m+1, n,   b),
                ]
                assert len(set(tri2)) == 2

check_rows()
```

A useful next computation would generate exact completion closures for an equilateral triangle and test whether adding several rotated triangular lattices rapidly destroys the row-sequence entropy.

## Route Diagnosis

**Proved ledger.**

- Avoidance is equivalent to the exact sign identity of Lemma 1.1.
- A monochromatic side forces both completion apexes to the opposite color.
- Both color classes are relatively dense at the circumradius scale.
- The alternating equal-width strip coloring has exactly one exceptional triangle class: the matching equilateral triangle.
- Any arbitrary one-dimensional avoiding coloring has every altitude as a global antiperiod, with the exact parity obstruction (3.2).
- Translation constraints from one orientation and constraints on one circumcircle can have extremely many pathological solutions.

**Plausible but unproved.**

- Interactions among a sufficiently rich finite collection of rotations may force global translation or antitranslation relations.
- For equilateral avoidance, overlapping rotated triangular lattices might eliminate the row-by-row entropy and leave only strip-like models. I found no proof or even a precise finite statement that guarantees this.
- The projection functional used for strip colorings may have an analogue built from color-equivalence relations, but no unconditional way to define such a functional is known.

**Dead ends.**

- Classifying restrictions to a single orientation fails: there are \(2^{\mathfrak c}\) avoiding colorings.
- Classifying restrictions to one circumcircle also fails generically for the same reason.
- Extrapolating from equal-width strips is unjustified. In an arbitrary coloring, endpoints of a side aligned with a chosen direction need not have equal colors, so the antiperiod mechanism does not activate.
- The sign identity is exact but remains conditional in effect: when a base is bichromatic, the apex color is unrestricted.

**Precise block.**

Route 4 requires deriving a global relation such as
\[
\chi(x+v)=\chi(x)
\quad\text{or}\quad
\chi(x+v)=1-\chi(x)
\]
from triangle avoidance. The available propagation rule gives such information only over a base already known to be monochromatic. There is no mechanism controlling the color of a prescribed base pair, and finite/fixed-orientation models retain substantial entropy. Establishing the missing global relation appears comparable in strength to classifying all proper 2-colorings of the full rotated triangle hypergraph, so Route 4 is presently blocked rather than reduced to a demonstrably simpler theorem.

A fresh attempt should likely combine the exact forced-kite rule with finite SAT searches over several carefully chosen rotations, looking specifically for gadgets that turn the color-unspecified monochromatic pair supplied by an equilateral triangle into a color-independent period or antiperiod.