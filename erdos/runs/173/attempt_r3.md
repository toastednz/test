STATUS: PARTIAL
## Result

Assuming Shader’s theorem in the unrestricted form stated in the brief, I obtained a parameter-uniform right-seed gadget proving the following substantial special case: for every nondegenerate triangle \(T\), every 2-coloring of the plane contains a monochromatic congruent copy of \(T\) or of its dilation \(\sqrt2\,T\). The proof uses a monochromatic isosceles right triangle whose legs equal one chosen side of \(T\), followed by five exact triangle attachments. I also give a nonhomothetic pair of non-right triangles handled by a one-layer right-seed gadget, and prove that the most elementary deterministic version of Route 3 stalls for generic pairs of equilateral scales.

## Complete Argument

### 1. External input and the forcing rule

I use the following reported theorem.

> **Shader’s theorem (as reported).**  
> For every fixed nondegenerate right triangle \(R\), every arbitrary 2-coloring of \(\mathbb R^2\) contains a monochromatic congruent copy of \(R\).

No regularity of the coloring is used below.

The elementary forcing rule is:

> **Forcing rule.**  
> Suppose a coloring avoids a triangle \(V\). If \(\{x,y,z\}\) is congruent to \(V\) and
> \[
> \chi(x)=\chi(y)=c,
> \]
> then
> \[
> \chi(z)=1-c.
> \]

This follows immediately: otherwise \(\{x,y,z\}\) would be a monochromatic copy of \(V\).

---

### 2. A finite right-seed principle

Let \(T,U\) be fixed triangles. Suppose a finite geometric configuration contains:

1. a distinguished right triangle \(R\);
2. finitely many congruent copies of \(T\) and \(U\);

and suppose that no coloring of the configuration can simultaneously make \(R\) monochromatic and make every displayed copy of \(T,U\) nonmonochromatic.

Then, by Shader’s theorem, every plane coloring contains a monochromatic \(T\) or \(U\): take a monochromatic copy of \(R\), map the entire finite attachment configuration onto it by the same isometry, and restrict the plane coloring to its vertices.

The theorem below gives such a configuration uniformly for \(U=\sqrt2\,T\).

---

### 3. Main partial theorem: \(T\) versus \(\sqrt2\,T\)

> **Theorem.**  
> Let \(T\) be any nondegenerate triangle, and let \(\sqrt2\,T\) denote the triangle obtained by multiplying all three side lengths of \(T\) by \(\sqrt2\). Assuming Shader’s theorem, every 2-coloring of \(\mathbb R^2\) contains a monochromatic congruent copy of \(T\) or of \(\sqrt2\,T\).

#### Proof

Choose any side of \(T\), and use its length as the unit of length. After choosing an orientation and possibly reflecting, write a representative of \(T\) in complex coordinates as
\[
T=\{0,1,p\},
\qquad p\in\mathbb C\setminus\mathbb R.
\]
Thus the side lengths of \(T\) are
\[
1,\quad |p|,\quad |1-p|.
\]

Suppose, for contradiction, that a coloring \(\chi\) avoids both \(T\) and \(\sqrt2\,T\).

By Shader’s theorem, there is a monochromatic isosceles right triangle with legs of length \(1\). After applying an isometry and choosing labels, write its vertices as
\[
O=0,\qquad A=1,\qquad B=i,
\]
and let their common color be \(c\).

Define five attachment points:
\[
\begin{aligned}
P&=1-p,\\
Q&=ip,\\
S&=1-p+ip,\\
X&=S-i,\\
W&=S-1.
\end{aligned}
\]

We now verify all required congruences exactly.

#### First three attachments

For \(\{O,A,P\}\),
\[
|O-A|=1,\qquad |O-P|=|1-p|,\qquad |A-P|=|p|.
\]
Hence
\[
\{O,A,P\}\cong T.
\]

For \(\{O,B,Q\}\),
\[
|O-B|=1,\qquad |O-Q|=|p|,\qquad |B-Q|=|i-ip|=|1-p|.
\]
Hence
\[
\{O,B,Q\}\cong T.
\]

For \(\{A,B,S\}\), note that
\[
S-A=(i-1)p
\]
and
\[
S-B=(1-i)(1-p).
\]
Therefore
\[
|A-B|=\sqrt2,\qquad
|A-S|=\sqrt2\,|p|,\qquad
|B-S|=\sqrt2\,|1-p|.
\]
Thus
\[
\{A,B,S\}\cong \sqrt2\,T.
\]

Because \(O,A,B\) all have color \(c\), and because both target triangles are assumed avoided, the forcing rule gives
\[
\chi(P)=\chi(Q)=\chi(S)=1-c.
\]

#### Second layer

For \(\{P,S,X\}\), we have
\[
S-P=ip,\qquad S-X=i,\qquad X-P=i(p-1).
\]
Consequently its side lengths are
\[
|p|,\quad 1,\quad |1-p|,
\]
so
\[
\{P,S,X\}\cong T.
\]
Since \(P,S\) both have color \(1-c\), avoidance of \(T\) forces
\[
\chi(X)=c.
\]

Similarly,
\[
S-Q=1-p,\qquad S-W=1,\qquad W-Q=-p.
\]
Thus
\[
\{Q,S,W\}\cong T,
\]
and therefore
\[
\chi(W)=c.
\]

#### Final contradiction

Finally,
\[
W=(i-1)p,
\qquad
X=(1-i)(1-p),
\qquad
X-W=1-i.
\]
Hence
\[
|O-W|=\sqrt2\,|p|,
\qquad
|O-X|=\sqrt2\,|1-p|,
\qquad
|X-W|=\sqrt2.
\]
Therefore
\[
\{O,X,W\}\cong \sqrt2\,T.
\]

But
\[
\chi(O)=\chi(X)=\chi(W)=c,
\]
so this is a monochromatic copy of \(\sqrt2\,T\), contradicting the hypothesis.

All displayed triangles are nondegenerate because they have exactly the side lengths of the nondegenerate triangle \(T\) or its dilation. If two point names from different stages happen to denote the same point for a special \(T\), the forced color equalities either remain consistent or produce an earlier contradiction; no step requires distinctness except within each displayed triangle.

This proves the theorem. \(\square\)

#### Combinatorial core

The corresponding finite NAE gadget has the six hyperedges
\[
OAP,\quad OBQ,\quad ABS,\quad PSX,\quad QSW,\quad OXW,
\]
where \(OAB\) is the monochromatic right seed. Its color propagation is
\[
O=A=B=c
\Longrightarrow
P=Q=S=1-c
\Longrightarrow
X=W=c,
\]
after which \(OXW\) is monochromatic.

Thus the result is genuinely finite and uses no limiting, measurable, or topological argument.

---

### 4. A nonhomothetic pair of non-right triangles

The same seed method also handles pairs not related by scaling.

Let \(E\) be the equilateral triangle of side \(1\), and set
\[
h=\frac{\sqrt3}{2}.
\]
Use the monochromatic right seed
\[
O=(0,0),\qquad A=(1,0),\qquad B=(0,1).
\]

Define
\[
P=\left(\frac12,h\right),\qquad
P'=\left(\frac12,-h\right),\qquad
Q=\left(-h,\frac12\right).
\]
Then
\[
\{O,A,P\}\cong E,\qquad
\{O,A,P'\}\cong E,\qquad
\{O,B,Q\}\cong E.
\]

Therefore, if the coloring avoids \(E\), all three points \(P,P',Q\) have the color opposite to the right seed.

Their pairwise distances are
\[
|P-P'|=\sqrt3,
\]
\[
|P-Q|=\sqrt2,
\]
and
\[
|P'-Q|=\sqrt{2+\sqrt3}.
\]
Indeed,
\[
|P-Q|^2
 =\left(\frac12+h\right)^2+\left(h-\frac12\right)^2
 =2,
\]
while
\[
|P'-Q|^2
 =2\left(\frac12+h\right)^2
 =2+\sqrt3.
\]

Let \(U\) be the triangle with sorted side lengths
\[
\boxed{\sqrt2,\quad \sqrt3,\quad \sqrt{2+\sqrt3}}.
\]
Then \(P,P',Q\) form a monochromatic copy of \(U\).

The triangle \(U\) is non-right because
\[
2+\sqrt3\ne 2+3,
\]
and it is clearly noncongruent to \(E\). Therefore:

> Every 2-coloring contains a monochromatic equilateral triangle of side \(1\), or a monochromatic copy of the non-right triangle with side lengths
> \[
> \sqrt2,\sqrt3,\sqrt{2+\sqrt3}.
> \]

Scaling gives the analogous assertion at every base scale.

---

### 5. A rigorous limitation of elementary deterministic right-seed propagation

The success above depends on exact metric identities. For generic independent triangle parameters, the most direct form of Route 3 stops after one round.

This can be demonstrated sharply for two equilateral scales.

Let
\[
0<a<b,\qquad r=\frac ba.
\]
Suppose a monochromatic right seed is chosen, and we perform only the following deterministic operation:

- whenever a known same-colored pair is at distance \(a\) or \(b\), attach both equilateral completion points, which are forced to have the opposite color.

Call the points forced directly from seed edges the first layer.

> **Lemma.**  
> Unless
> \[
> r\in
> \left\{
> \sqrt2,\,
> \sqrt{\frac73},\,
> \sqrt3,\,
> \sqrt{2+\sqrt3}
> \right\},
> \]
> no pair of first-layer points is at distance \(a\) or \(b\). Consequently this deterministic same-colored-base propagation cannot continue past the first layer.

#### Proof

For perpendicular active legs of lengths \(x,y\), place their common endpoint at the origin and write the equilateral completion points as
\[
P_\sigma=\left(\frac x2,\sigma\frac{\sqrt3 x}{2}\right),
\qquad
Q_\tau=\left(\tau\frac{\sqrt3 y}{2},\frac y2\right),
\qquad \sigma,\tau\in\{\pm1\}.
\]
The cross-distances satisfy
\[
|P_\sigma-Q_\tau|^2
=x^2+y^2-\frac{\sqrt3}{2}xy(\sigma+\tau).
\]
Thus the three possible squared cross-distances are
\[
x^2+y^2-\sqrt3xy,\qquad
x^2+y^2,\qquad
x^2+y^2+\sqrt3xy.
\]
The two completions over a single edge of length \(x\) are at distance \(\sqrt3x\).

The possibilities for two active edges of a right seed are exhausted by:

\[
\begin{array}{c|c}
\text{Active seed edges} &
\text{Ratios }r=b/a\text{ allowing a new distance }a\text{ or }b\\
\hline
a,a\text{ as legs}
&
\sqrt2,\ \sqrt3,\ \sqrt{2+\sqrt3}\\[2mm]
b,b\text{ as legs}
&
\sqrt{2+\sqrt3}\\[2mm]
a,b\text{ as legs}
&
\sqrt3
\end{array}
\]

For example, with \(x=y=a\), the cross-distances are
\[
a\sqrt{2-\sqrt3},\qquad
a\sqrt2,\qquad
a\sqrt{2+\sqrt3},
\]
and the same-edge distance is \(\sqrt3a\).

It remains to consider the case where the active side of length \(a\) is a leg and the active side of length \(b\) is the hypotenuse. Put
\[
d=\sqrt{b^2-a^2}.
\]
Use seed vertices
\[
O=(0,0),\qquad A=(a,0),\qquad B=(0,d),
\]
so \(AB=b\). The \(a\)-equilateral completion points over \(OA\) are
\[
P_\sigma=
\left(\frac a2,\sigma\frac{\sqrt3a}{2}\right),
\]
and the \(b\)-equilateral completion points over \(AB\) are
\[
Q_\tau=
\left(
\frac a2+\tau\frac{\sqrt3d}{2},
\frac d2+\tau\frac{\sqrt3a}{2}
\right).
\]
Their possible squared cross-distances are
\[
d^2
\]
and
\[
b^2+2a^2\pm\sqrt3ad.
\]

Now:

- \(d=a\) gives \(b/a=\sqrt2\);
- \(\sqrt3a=b\) gives \(b/a=\sqrt3\);
- \(b^2+2a^2-\sqrt3ad=b^2\) gives
  \[
  d=\frac{2a}{\sqrt3},
  \qquad
  \frac{b^2}{a^2}=1+\frac43=\frac73;
  \]
- the equation
  \[
  b^2+2a^2-\sqrt3ad=a^2
  \]
  has no real solution, because after dividing by \(a^2\), setting \(z=b^2/a^2>1\), and squaring, one obtains
  \[
  z^2-z+4=0.
  \]

A seed with only one active edge can continue only when its two completion points, at distance \(\sqrt3a\), activate the other scale, again giving \(r=\sqrt3\).

These cases exhaust the relative positions of active edges in a right triangle. Hence outside the displayed four ratios, no unprocessed same-colored first-layer pair has target distance \(a\) or \(b\). Seed-to-first-layer pairs have opposite colors, so the forcing rule cannot be applied to them. The deterministic closure therefore stops. \(\square\)

This lemma does **not** show that Route 3 fails in general. It shows only that a successful general proof must use more than repeated application of the forcing rule to already-known same-colored bases. In particular, it may need genuinely branching NAE gadgets involving vertices whose colors are not initially forced.

---

### Running ledger

#### Proved, conditional only on Shader’s reported theorem

1. The finite right-seed obstruction principle.
2. For every nondegenerate \(T\),
   \[
   \boxed{\text{every coloring realizes }T\text{ or }\sqrt2\,T.}
   \]
3. A nonhomothetic non-right pair:
   \[
   E_1
   \quad\text{versus}\quad
   \left(\sqrt2,\sqrt3,\sqrt{2+\sqrt3}\right).
   \]
4. The one-round equilateral propagation obstruction outside the four ratios listed above.

#### Plausible but unproved

1. Deeper right-seed gadgets may handle further homothetic factors and perhaps some of the exceptional equilateral ratios.
2. A parameter-uniform mixed gadget using both triangle coordinate parameters may exist, but it will have to employ non-deterministic NAE constraints rather than only same-colored-base propagation.
3. The \(\sqrt2\)-gadget suggests that complex-linear identities associated with right-angle multipliers may generate a larger family of solvable parameter relations.

#### Dead ends encountered

1. Attaching \(T\) and \(U\) independently to perpendicular seed legs generally produces opposite-colored apexes whose mutual distances are not sides of either target.
2. Trying to prove every non-equilateral \(T\) unavoidable by attaching \(T\) to two edges of a right seed fails even for an isosceles example with sides \(1,1,1.5\); the first forced points do not reproduce \(T\).
3. Repeated independent uses of Shader’s theorem do not help: the monochromatic right triangles occur at unrelated locations and possibly in unrelated colors.
4. For equilateral scales \(1\) and \(\sqrt3\), elementary propagation generates a triangular-lattice-like pattern without an immediate finite contradiction. No conclusion about that pair was obtained.

## Self-Audit

1. **Dependence on the precise Shader theorem.**  
   I have not independently verified the original 1976 paper. The main theorem is therefore formally conditional on Shader’s result having exactly the unrestricted scope stated in the brief. I believe the use is legitimate because Route 3 explicitly supplies that theorem as its seed mechanism. If the source imposed regularity assumptions, the geometric gadget would remain correct but the plane-wide conclusion would not follow.

2. **Possible coincidences among constructed vertices.**  
   For special triangles, points from different stages can coincide; for example the right-isosceles case can make \(S\) coincide with a seed vertex. This does not create a gap: each displayed hyperedge has the exact nondegenerate side lengths of \(T\) or \(\sqrt2T\), and any collision producing contradictory forced colors gives an earlier contradiction. The final forcing argument is valid with all such identifications.

3. **The blockage lemma concerns only a restricted propagation model.**  
   It does not exclude larger right-seed NAE gadgets with unforced intermediate vertices. I believe the stated limitation is exact because all possible placements of two active edges in a right triangle are enumerated and all first-layer distances are computed, but it must not be interpreted as evidence that the full pairwise assertion fails for generic equilateral ratios.

## Computations To Verify

The main coordinate identities can be checked symbolically:

```python
import sympy as sp

x, y = sp.symbols("x y", real=True)

O = sp.Matrix([0, 0])
A = sp.Matrix([1, 0])
B = sp.Matrix([0, 1])

# p = x + i y
P = sp.Matrix([1-x, -y])       # 1-p
Q = sp.Matrix([-y, x])         # i p
S = P + Q                      # 1-p+i p
X = S - B                      # S-i
W = S - A                      # S-1

def d2(U, V):
    D = U - V
    return sp.expand(D.dot(D))

r2 = x**2 + y**2
s2 = (1-x)**2 + y**2

checks = [
    d2(O, A) - 1,
    d2(O, P) - s2,
    d2(A, P) - r2,

    d2(O, B) - 1,
    d2(O, Q) - r2,
    d2(B, Q) - s2,

    d2(A, B) - 2,
    d2(A, S) - 2*r2,
    d2(B, S) - 2*s2,

    d2(P, S) - r2,
    d2(S, X) - 1,
    d2(P, X) - s2,

    d2(Q, S) - s2,
    d2(S, W) - 1,
    d2(Q, W) - r2,

    d2(O, X) - 2*s2,
    d2(O, W) - 2*r2,
    d2(X, W) - 2,
]

assert all(sp.simplify(z) == 0 for z in checks)
print("All symbolic distance identities verified.")
```

The abstract NAE contradiction can be exhaustively checked:

```python
from itertools import product

names = ["O", "A", "B", "P", "Q", "S", "X", "W"]
edges = [
    ("O", "A", "P"),   # T
    ("O", "B", "Q"),   # T
    ("A", "B", "S"),   # sqrt(2) T
    ("P", "S", "X"),   # T
    ("Q", "S", "W"),   # T
    ("O", "X", "W"),   # sqrt(2) T
]

def nae(vals, e):
    return len({vals[v] for v in e}) > 1

models = []
for bits in product([0, 1], repeat=len(names)):
    vals = dict(zip(names, bits))
    if not (vals["O"] == vals["A"] == vals["B"]):
        continue
    if all(nae(vals, e) for e in edges):
        models.append(vals)

assert models == []
print("No NAE coloring with monochromatic right seed.")
```

The nonhomothetic equilateral attachment can be verified exactly:

```python
h = sp.sqrt(3)/2

P  = sp.Matrix([sp.Rational(1,2),  h])
Pm = sp.Matrix([sp.Rational(1,2), -h])
Q  = sp.Matrix([-h, sp.Rational(1,2)])

assert sp.simplify(d2(P, Pm) - 3) == 0
assert sp.simplify(d2(P, Q) - 2) == 0
assert sp.simplify(d2(Pm, Q) - (2 + sp.sqrt(3))) == 0
print("Nonhomothetic companion triangle verified.")
```

For deeper Route 3 searches, an exact closure/SAT experiment should use the following structure:

```python
# Pseudocode
points = vertices_of_chosen_right_seed()
forced_color = {seed_vertex: 0 for seed_vertex in points}
hyperedges = []

repeat for depth rounds:
    for each known same-colored pair (P,Q):
        for V in [T,U]:
            for each assignment of a side of V to |P-Q|:
                for each exact completion R:
                    add R exactly
                    add hyperedge (P,Q,R)
                    force color(R) = 1-color(P)
                    if R already has the other forced color:
                        return CONTRADICTION
    enumerate every exact T/U copy among current points
    if one has three equal forced colors:
        return CONTRADICTION

# Separately encode all discovered hyperedges as NAE clauses,
# prescribe the seed monochromatic, and use SAT to detect
# contradictions that do not arise by deterministic propagation.
```

Coordinates should be represented in exact algebraic number fields, and any UNSAT claim should be accompanied by an LRAT certificate.

## Route Diagnosis

The successful idea was to use all three sides of a monochromatic isosceles right seed simultaneously: its two unit legs support two copies of \(T\), while its hypotenuse supports a copy of \(\sqrt2T\). The complex identities
\[
S=1-p+ip,\qquad X=S-i,\qquad W=S-1
\]
then close a six-edge NAE gadget uniformly for every triangle parameter \(p\). This is a genuine Route 3 mechanism and handles arbitrary shape, including scalene acute and obtuse triangles.

The route remains blocked for two independent generic triangles. A right seed has only three pairwise distances, constrained by one Pythagorean relation. Generically only two of those distances can be chosen from the six target side lengths, and first-layer attachment distances do not land back in that finite side set. The equilateral calculation makes this obstruction explicit. Thus purely deterministic propagation from same-colored bases is not a plausible universal proof.

A fresh attempt should preserve the right seed but search for **branching** NAE gadgets rather than only forced-color closures. In complex coordinates, write
\[
T=\{0,1,p\},\qquad
U=\{0,\lambda,\lambda q\}
\]
after one global normalization, place selected sides on two edges of a symbolic right triangle, and synthesize small abstract NAE gadgets whose geometric realization is an identity in the independent parameters \(p,q,\lambda\). Exact SAT searches should first test whether recurring seed-UNSAT cores exist for the remaining exceptional equilateral ratios
\[
\sqrt{\frac73},\quad \sqrt3,\quad \sqrt{2+\sqrt3},
\]
then move to generic algebraic pairs. If those searches only succeed when additional algebraic relations among side lengths are imposed, Route 3 is likely intrinsically non-uniform and Route 1 or a structural classification approach will be necessary.