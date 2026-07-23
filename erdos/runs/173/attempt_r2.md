STATUS: BLOCKED

## Result

Route 2 yields a rigorous conditional propagation calculus and a finite “completion-star” obstruction. This proves the pairwise assertion for an explicit continuum of pairs of noncongruent, non-right triangles, including the concrete pair with side lengths
\[
T:\left(\frac{\sqrt5}{2},\frac{\sqrt{13}}2,2\right),
\qquad
U:\left(\frac1{\sqrt2},\frac{\sqrt{10}}2,2\right).
\]
However, the propagation is activated only by monochromatic base edges. For generic pairs—already for two equilateral triangles whose side-length ratio is not \(\sqrt3\) or \(1/\sqrt3\)—the elementary reflection process stops after one generation. Moreover, the most direct proposed odd color-flip cycle, obtained by repeatedly replacing a base with its two reflected apexes, cannot close in odd length because every step rotates the supporting line by \(90^\circ\). Thus Route 2 does not presently resolve the general problem.

## Complete Argument

### 1. Exact NAE and reflection propagation

Write the coloring in spin notation:
\[
s(P)=(-1)^{\chi(P)}\in\{-1,1\}.
\]

#### Lemma 1: Spin identity

A triple \(\{P,Q,R\}\) is nonmonochromatic if and only if
\[
s(P)s(Q)+s(Q)s(R)+s(R)s(P)=-1.
\]

#### Proof

If all three spins agree, every pair product is \(1\), so the sum is \(3\). Otherwise two spins agree and the third is opposite; the three pair products are \(1,-1,-1\), whose sum is \(-1\). These are the only possibilities. ∎

Suppose \(R\) and \(R'\) are the two reflected apexes completing the same prescribed triangle over the base \(PQ\). If the coloring avoids that triangle, Lemma 1 applied to \(PQR\) and \(PQR'\) gives
\[
s(P)s(Q)+(s(P)+s(Q))s(R)=-1,
\]
\[
s(P)s(Q)+(s(P)+s(Q))s(R')=-1.
\]
Subtracting,
\[
\bigl(s(P)+s(Q)\bigr)\bigl(s(R)-s(R')\bigr)=0.
\]

Consequently:

- If \(P,Q\) have the same color, then \(s(P)+s(Q)\ne0\), so
  \[
  s(R)=s(R').
  \]
  Substitution into the NAE identity gives
  \[
  s(R)=s(R')=-s(P).
  \]
- If \(P,Q\) have opposite colors, then \(s(P)+s(Q)=0\), and the two triangle constraints impose no relation between \(R\) and \(R'\).

Thus the exact propagation rule is:

> A monochromatic base forces every admissible completion apex to have the opposite color. A bichromatic base gives no local propagation at all.

The second assertion is not merely a deficiency of the calculation. The local assignment
\[
\chi(P)=0,\quad \chi(Q)=1,\quad \chi(R)=0,\quad \chi(R')=1
\]
makes both triples \(PQR\) and \(PQR'\) nonmonochromatic, while \(R,R'\) have different colors.

---

### 2. Exact complex-coordinate form of the reflection step

Let an oriented base be \(z,z+v\), where \(|v|=d\). Suppose the desired apex distances are
\[
|R-z|=r,\qquad |R-(z+v)|=s.
\]
Set
\[
\alpha=\frac{r^2-s^2+d^2}{2d^2},
\qquad
\beta=\sqrt{\frac{r^2}{d^2}-\alpha^2}>0.
\]
The reflected apexes are
\[
R_\pm=z+(\alpha\pm i\beta)v.
\]
Their difference is
\[
R_+-R_-=2i\beta v.
\]
Thus the segment joining the reflected apexes is perpendicular to the original base and has length
\[
2\beta d=2h,
\]
where \(h\) is the altitude over that base.

When the original base is monochromatic and the triangle is avoided, \(R_+\) and \(R_-\) form a monochromatic segment of the opposite color.

For a scalene triangle one must also allow the assignment \(r,s\) to the base endpoints to be interchanged. This replaces \(\alpha\) by \(1-\alpha\), producing two further apexes. All such apexes are forced to the same opposite color when the base is monochromatic.

---

### 3. Every prescribed length occurs monochromatically

#### Lemma 2

For every \(d>0\), every two-coloring of the plane has a monochromatic pair at distance \(d\).

#### Proof

Take the three vertices of an equilateral triangle of side \(d\). Two have the same color, and their distance is \(d\). ∎

This supplies a monochromatic base for any side length of either target triangle, although it does not control the location or direction of that base.

---

### 4. A completion-star obstruction

The preceding propagation gives the following finite criterion.

#### Lemma 3: Completion-star criterion

Let \(\mathcal F\) be a finite collection of triangle classes. Suppose there are distinct points
\[
P,Q,R_1,R_2,R_3
\]
such that:

1. \(|P-Q|=d>0\);
2. for each \(i\), the triangle \(\{P,Q,R_i\}\) belongs to \(\mathcal F\);
3. the triangle \(\{R_1,R_2,R_3\}\) also belongs to \(\mathcal F\).

Then no two-coloring of the plane can avoid every triangle in \(\mathcal F\).

#### Proof

By Lemma 2, choose a monochromatic pair \(P',Q'\) at distance \(d\). Apply an isometry sending \(P,Q\) to \(P',Q'\), and use the same notation for the images of \(R_1,R_2,R_3\).

Let the common color of \(P,Q\) be \(c\). Since every triangle \(PQR_i\) is assumed avoided, its third vertex must have color \(1-c\). Hence \(R_1,R_2,R_3\) are monochromatic. But their triangle belongs to \(\mathcal F\), a contradiction. ∎

This is a genuine finite propagation gadget, not an argument using regularity or limiting placements.

---

### 5. An explicit continuum of non-right pairs settled by Route 2

For a parameter
\[
-1<x<0,
\]
define
\[
P=(-1,0),\qquad Q=(1,0),
\]
\[
A_+=(x,1),\qquad A_-=(x,-1),
\qquad B=(x+1,-x).
\]
Let
\[
T_x=[\{P,Q,A_+\}],
\qquad
U_x=[\{P,Q,B\}].
\]

The squared side lengths of \(T_x\) are
\[
|P-Q|^2=4,
\]
\[
|P-A_+|^2=(x+1)^2+1,
\]
\[
|Q-A_+|^2=(x-1)^2+1.
\]

The squared side lengths of \(U_x\) are
\[
|P-Q|^2=4,
\]
\[
|P-B|^2=(x+2)^2+x^2=2x^2+4x+4,
\]
\[
|Q-B|^2=x^2+x^2=2x^2.
\]

All these triangles are nondegenerate because the altitudes of \(A_+\) and \(B\) over \(PQ\) are \(1\) and \(-x>0\), respectively.

#### The triangles are non-right and noncongruent

For \(T_x\), the three strict acute-angle inequalities in squared-side form are:

\[
4<\bigl((x+1)^2+1\bigr)+\bigl((x-1)^2+1\bigr)
=2x^2+4,
\]
which holds because \(x\ne0\);

\[
(x-1)^2+1<4+(x+1)^2+1,
\]
which is equivalent to \(x>-1\);

and
\[
(x+1)^2+1<4+(x-1)^2+1,
\]
which is equivalent to \(x<1\).

Thus \(T_x\) is acute.

For \(U_x\),
\[
|P-B|^2+|Q-B|^2
=4x^2+4x+4
<4=|P-Q|^2,
\]
because \(x(x+1)<0\) on \((-1,0)\). Hence \(U_x\) is obtuse. In particular, both triangles are non-right and they are noncongruent.

#### The apex triangle closes the gadget

Direct calculation gives
\[
|A_+-A_-|^2=4,
\]
\[
|A_+-B|^2=1+(x+1)^2,
\]
\[
|A_--B|^2=1+(1-x)^2.
\]
These are exactly the three squared side lengths of \(T_x\). Therefore
\[
\{A_+,A_-,B\}\cong T_x.
\]

Now apply Lemma 3 with
\[
R_1=A_+,\qquad R_2=A_-,\qquad R_3=B,
\qquad \mathcal F=\{T_x,U_x\}.
\]
Indeed,

- \(PQA_+\) is a copy of \(T_x\);
- \(PQA_-\) is its reflected copy;
- \(PQB\) is a copy of \(U_x\);
- \(A_+A_-B\) is another copy of \(T_x\).

It follows that every two-coloring contains a monochromatic copy of \(T_x\) or of \(U_x\).

#### A concrete rational-coordinate instance

Taking \(x=-\tfrac12\), one obtains
\[
A_+=\left(-\frac12,1\right),\quad
A_-=\left(-\frac12,-1\right),\quad
B=\left(\frac12,\frac12\right).
\]
The sorted side lengths are
\[
T:\left(\frac{\sqrt5}{2},\frac{\sqrt{13}}2,2\right),
\]
\[
U:\left(\frac1{\sqrt2},\frac{\sqrt{10}}2,2\right).
\]
Thus the pairwise assertion is rigorously established for this explicit pair of non-right, noncongruent triangles.

---

### 6. Why the most direct odd reflection cycle cannot work

Consider a chain of monochromatic segments
\[
S_0,S_1,\dots,S_n
\]
where \(S_{i+1}\) is the segment joining two reflected apexes over \(S_i\) for one of the avoided triangles.

Every step has two properties:

1. the color of the segment flips;
2. its supporting line becomes perpendicular to the preceding supporting line.

Therefore, after \(n\) steps, the supporting line has rotated by
\[
n\frac{\pi}{2}\pmod{\pi}.
\]
If \(S_n=S_0\) as an unordered segment, their supporting lines agree, so
\[
n\frac{\pi}{2}\equiv0\pmod{\pi}.
\]
Hence \(n\) is even. The inferred color has then flipped an even number of times, so there is no contradiction.

More generally, if two such paths from the same starting segment reach the same final segment, their lengths have the same parity. Thus the simplest proposed mechanism—returning to one segment by an odd number of reflected-apex replacements—is geometrically impossible.

This does not rule out:

- two paths of opposite parity meeting at a single endpoint;
- branching completion clouds whose vertices form a monochromatic target triangle;
- propagation using pairs other than the reflected-apex pair.

The completion-star construction above is an example of branching rather than a simple closed chain.

---

### 7. A flexible-angle propagation theorem

The following result shows that odd translation cycles can work when one forbids a much larger family of shapes.

#### Lemma 4: Monochromatic flexible hinge

For every \(a,b>0\), every two-coloring of the plane contains distinct, noncollinear monochromatic points \(X,Y,Z\) such that
\[
|X-Y|=a,\qquad |X-Z|=b.
\]
The angle \(YXZ\) is not prescribed.

#### Proof

By Lemma 2, take a monochromatic pair \(P_0,Q_0\) at distance \(a\), with common color \(c_0\).

Choose vectors \(v_1,v_2,v_3\), each of length \(b\), such that
\[
v_1+v_2+v_3=0
\]
and none is parallel to \(Q_0-P_0\). For example, take three vectors separated by \(120^\circ\), rotated to avoid the finitely many forbidden directions.

Set
\[
P_i=P_0+v_1+\cdots+v_i,\qquad
Q_i=Q_0+v_1+\cdots+v_i.
\]
Suppose no monochromatic hinge of the asserted kind exists.

If \(P_{i-1},Q_{i-1}\) are monochromatic of color \(c\), then
\[
P_{i-1},Q_{i-1},P_i
\]
is a noncollinear hinge with side lengths \(a,b\) from \(P_{i-1}\). Hence \(P_i\) must have color \(1-c\). Similarly,
\[
Q_{i-1},P_{i-1},Q_i
\]
is such a hinge centered at \(Q_{i-1}\), so \(Q_i\) also has color \(1-c\).

Thus every translation by \(v_i\) flips the color of the whole monochromatic \(a\)-segment. After three steps,
\[
P_3=P_0,\qquad Q_3=Q_0,
\]
but the inferred color has flipped three times, a contradiction. ∎

This lemma does not settle any fixed triangle: it gives no control over the hinge angle. In particular, setting \(a=b=s\) does not force a monochromatic equilateral triangle of side \(s\), consistent with the alternating-strip example.

---

### 8. Precise activation block for generic pairs

For a fixed side \(d\), place a canonical base \(P,Q\) of length \(d\). Let \(C_d\) be the set of all apexes obtained by completing every occurrence of \(d\) as a side of \(T\) or \(U\), allowing:

- both reflections across the base line;
- both assignments of adjacent side lengths to the base endpoints.

If \(P,Q\) are monochromatic and both target triangles are avoided, every point of \(C_d\) has the opposite color.

The elementary reflection route can continue from this seed only if at least one of the following occurs:

1. three points of \(C_d\) form a copy of \(T\) or \(U\), immediately giving a contradiction;
2. two points of \(C_d\) are separated by a side length of \(T\) or \(U\), giving a new monochromatic base;
3. a forced point coincides with a point reached by a different path with opposite forced color.

None of these incidences is automatic for a generic pair.

For example, for an equilateral triangle of side \(s\), the completion cloud over a monochromatic side consists of only two points, separated by
\[
\sqrt3\,s.
\]
Consequently, for two equilateral side lengths \(s,t\) satisfying
\[
t\ne\sqrt3\,s,\qquad s\ne\sqrt3\,t,
\]
the one-generation reflected-apex rule from either target side produces no new segment whose length is a side of either target. Thus the most basic propagation mechanism already stalls on the main benchmark for generic scale ratios.

This is not a proof that richer Route 2 constructions cannot work. It is the exact point where the present deterministic propagation ceases to produce further information.

---

### 9. Ledger

**Proved lemmas and results**

1. The exact spin identity for an avoided triangle.
2. A monochromatic base forces all completion apexes to the opposite color.
3. A bichromatic base gives no relation between reflected apexes from the two local NAE constraints.
4. Every prescribed distance occurs as a monochromatic pair.
5. The completion-star obstruction criterion.
6. A continuum of explicit non-right, noncongruent pairs \((T_x,U_x)\) satisfying the pairwise assertion.
7. A direct reflected-apex chain cannot return to the same segment in odd length.
8. Every coloring has a monochromatic flexible hinge with any two prescribed arm lengths.

**Plausible but unproved**

1. Branching completion paths for two sufficiently different triangle geometries may eventually force endpoint collisions or a monochromatic target triangle.
2. Shader’s right-triangle seed may allow one to control the missing hinge angle.
3. The two-equilateral-scale benchmark is likely true, but no proof was obtained.

**Dead ends**

1. **Simple odd reflected-apex cycle:** impossible because each step turns the segment line by \(90^\circ\), so a return has even length.
2. **Independent monochromatic side seeds:** Lemma 2 supplies seeds for every side length, but their locations and relative directions cannot be coordinated.
3. **Flexible-hinge theorem as a direct solution:** the angle is uncontrolled, and exact congruence requires that angle.
4. **One-generation propagation for generic equilateral scales:** it stops unless the scale ratio is \(\sqrt3\) or \(1/\sqrt3\).

## Self-Audit

1. **The completion-star theorem uses a monochromatic base selected after seeing the coloring.** This is legitimate for an existence proof. If a fixed finite obstruction is desired, start with an equilateral triangle of side \(d\) and attach one copy of the star gadget to each of its three sides; one side is necessarily monochromatic.

2. **The explicit family could fail if the apex triangle only looked similar rather than congruent.** The three squared distances of \(A_+A_-B\) were computed exactly and coincide term-by-term with those of \(PQA_+\), so no scaling or approximate argument is involved.

3. **The Route 2 obstruction analysis is not a theorem that all reflection methods are hopeless.** It only rules out simple same-segment odd cycles and diagnoses one-generation stalling. Branching paths, endpoint collisions, and more elaborate NAE deductions remain possible and are explicitly not excluded.

## Computations To Verify

The following exact Python/SymPy code verifies the concrete geometry and the full abstract finite obstruction.

```python
import sympy as sp
from itertools import product

def dsq(A, B):
    return sp.expand(sum((A[i] - B[i])**2 for i in range(2)))

# Concrete x = -1/2 instance
P  = (sp.Rational(-1), 0)
Q  = (sp.Rational(1), 0)
Ap = (sp.Rational(-1, 2), 1)
Am = (sp.Rational(-1, 2), -1)
B  = (sp.Rational(1, 2), sp.Rational(1, 2))

T_sq = sorted([dsq(P, Q), dsq(P, Ap), dsq(Q, Ap)])
U_sq = sorted([dsq(P, Q), dsq(P, B), dsq(Q, B)])
closure_T_sq = sorted([dsq(Ap, Am), dsq(Ap, B), dsq(Am, B)])

assert T_sq == [
    sp.Rational(5, 4),
    sp.Rational(13, 4),
    sp.Rational(4)
]
assert U_sq == [
    sp.Rational(1, 2),
    sp.Rational(5, 2),
    sp.Rational(4)
]
assert closure_T_sq == T_sq

# T is acute; U is obtuse
assert T_sq[2] < T_sq[0] + T_sq[1]
assert U_sq[2] > U_sq[0] + U_sq[1]

# Abstract finite obstruction:
# seed vertices 0,1,2 form an equilateral triangle of side 2.
# Attach a separate star gadget to each seed edge.
hyperedges = []
next_vertex = 3

for p, q in [(0, 1), (1, 2), (2, 0)]:
    ap = next_vertex
    am = next_vertex + 1
    b  = next_vertex + 2
    next_vertex += 3

    # T on (p,q,ap), reflected T on (p,q,am),
    # U on (p,q,b), and T on (ap,am,b).
    hyperedges.extend([
        (p, q, ap),
        (p, q, am),
        (p, q, b),
        (ap, am, b),
    ])

def nae(bits, edge):
    vals = [bits[v] for v in edge]
    return not (vals[0] == vals[1] == vals[2])

solutions = []
for bits in product([0, 1], repeat=next_vertex):
    if all(nae(bits, e) for e in hyperedges):
        solutions.append(bits)

assert solutions == []
print("Exact geometry verified; finite NAE obstruction is UNSAT.")
```

The symbolic one-parameter identities can be checked as follows:

```python
x = sp.symbols('x', real=True)

P  = (-1, 0)
Q  = (1, 0)
Ap = (x, 1)
Am = (x, -1)
B  = (x + 1, -x)

assert sp.simplify(dsq(Ap, Am) - dsq(P, Q)) == 0
assert sp.simplify(dsq(Ap, B) - dsq(P, Ap)) == 0
assert sp.simplify(dsq(Am, B) - dsq(Q, Ap)) == 0

T_other_sum_minus_base = sp.expand(
    dsq(P, Ap) + dsq(Q, Ap) - dsq(P, Q)
)
U_other_sum_minus_base = sp.expand(
    dsq(P, B) + dsq(Q, B) - dsq(P, Q)
)

assert sp.factor(T_other_sum_minus_base) == 2*x**2
assert sp.factor(U_other_sum_minus_base) == 4*x*(x + 1)
# For -1 < x < 0: first is positive, second is negative.
```

A useful next computation is:

```text
For exact algebraic T,U:
1. For each side d of T or U, put a canonical base at (0,0),(d,0).
2. Generate all apexes for both endpoint assignments and both reflections.
3. Mark every apex as forced opposite to the base.
4. Enumerate:
   a. all pairwise apex distances equal to a target side;
   b. all apex triples congruent to T or U;
   c. all coincidences between independently generated branches.
5. Iterate these forced monochromatic-base rules.
6. Encode every discovered T/U copy as NAE clauses.
7. Search for UNSAT cores, retaining exact algebraic incidence proofs.
```

## Route Diagnosis

Reflection propagation works decisively when several target copies share a monochromatic base and their forced apexes close into another target copy. The completion-star family demonstrates this mechanism with two genuinely non-right triangles.

The route is blocked for general pairs at the activation stage. A monochromatic side exists, but generic completion clouds do not contain another target side or target triangle. A bichromatic side provides no deterministic relation, and independent monochromatic sides of different lengths cannot be placed in a controlled relative position. Simple odd return cycles are additionally ruled out by the perpendicular-line parity argument.

A fresh attempt should therefore seek one of:

1. a finite branching gadget producing endpoint collisions rather than a same-segment cycle;
2. a theorem furnishing a monochromatic connected seed with controlled angle, possibly using Shader’s right-triangle theorem;
3. an exact SAT search for recurring completion-star or multi-level collision patterns;
4. a new algebraic invariant that extracts information from bichromatic bases, since pure same-base propagation is too sparse for generic triangle parameters.