STATUS: BLOCKED

## Result

Route 1 does not presently yield a complete solution. I proved several rigorous structural results explaining the obstruction. Arbitrarily many rational rows can be parametrized over any two prescribed columns, but imposing a third distinct column produces a smooth genus-one curve. More generally, the curves governing new rows and columns have genera
\[
1+2^{r-2}(r-3),\qquad 1+2^{r-1}(r-2),
\]
respectively. Consequently, every fixed rational \(r\times r\) grid with \(r\ge3\) has only finitely many nondegenerate rational one-step extensions. Moreover, its two-dimensional extension variety contains no nonconstant rational curves when \(r\ge3\), despite having smooth rational points corresponding to duplicated rows and columns. I also prove that no nontrivial separated rational-function identity \(H(u,v)^2=F(u)+G(v)^2\) exists; hence every bounded-degree two-parameter ansatz eventually degenerates. These results sharply block the most direct parametric induction, but they do not rule out exceptional moving families whose grids and extension points vary together.

## Complete Argument

### 1. Rational grids suffice

Suppose
\[
T_i>0,\qquad E_j\ge0,\qquad X_{ij}\in\mathbb Q,
\qquad X_{ij}^2=T_i+E_j^2
\]
with the \(T_i\) pairwise distinct and the \(E_j\) pairwise distinct.

Choose a positive integer \(L\) divisible by every denominator occurring among the \(T_i,E_j,X_{ij}\). Set
\[
N_i=L^2T_i,\qquad d_j=2LE_j,\qquad x_{ij}=2LX_{ij}.
\]
Then all these quantities are integers and
\[
x_{ij}^2=4L^2X_{ij}^2
=4L^2T_i+4L^2E_j^2
=4N_i+d_j^2.
\]
Positivity and distinctness are preserved. Thus a rational construction of unbounded size would solve the original problem.

---

### 2. Two prescribed columns admit arbitrarily many rational rows

#### Lemma 2.1

Let \(0\le E_1<E_2\) be rational and put
\[
C=E_2^2-E_1^2>0.
\]
For every rational \(q\) satisfying
\[
0<q<E_2-E_1,
\]
define
\[
X_1(q)=\frac{C/q-q}{2},\qquad
X_2(q)=\frac{C/q+q}{2},
\]
and
\[
T(q)=X_1(q)^2-E_1^2.
\]
Then
\[
T(q)>0,\qquad
X_j(q)^2=T(q)+E_j^2\quad(j=1,2).
\]
Distinct choices of \(q\) in this interval give distinct values of \(T(q)\).

#### Proof

First,
\[
X_2(q)^2-X_1(q)^2
=(X_2-X_1)(X_2+X_1)
=q\frac Cq=C.
\]
Hence
\[
X_2(q)^2-E_2^2
=X_1(q)^2+C-E_2^2
=X_1(q)^2-E_1^2=T(q).
\]

The inequality \(X_1(q)>E_1\) is equivalent to
\[
\frac{C/q-q}{2}>E_1,
\]
or
\[
q^2+2E_1q-C<0.
\]
The positive root of the left-hand side is
\[
-E_1+\sqrt{E_1^2+C}=E_2-E_1,
\]
so the assumed range on \(q\) gives \(X_1(q)>E_1\), hence \(T(q)>0\).

Finally,
\[
\frac{dX_1}{dq}=-\frac{C}{2q^2}-\frac12<0.
\]
Because \(X_1(q)>0\), the function \(T(q)=X_1(q)^2-E_1^2\) is strictly decreasing on this interval. Thus distinct \(q\)'s give distinct rows. ∎

Therefore rational \(m\times2\) grids exist for every \(m\). The first genuine obstruction is the third column.

---

### 3. A third prescribed column produces an elliptic curve

Let \(E_1,E_2,E_3\) be distinct nonnegative rationals. Put
\[
C=E_2^2-E_1^2,\qquad A=E_3^2-E_1^2.
\]
Using the parametrization in Lemma 2.1, the third-column condition is
\[
Y^2=T(q)+E_3^2=X_1(q)^2+A.
\]
Multiplying by \(4q^2\) and writing \(W=2qY\) gives
\[
W^2=(C-q^2)^2+4Aq^2
=q^4+(4A-2C)q^2+C^2. \tag{3.1}
\]

#### Lemma 3.1

The quartic on the right of (3.1) is squarefree. Its smooth projective model therefore has genus one.

#### Proof

Write
\[
f(q)=q^4+Bq^2+C^2,\qquad B=4A-2C.
\]
Because \(E_1,E_2,E_3\) are distinct, one has
\[
A\ne0,\qquad C\ne0,\qquad A\ne C.
\]
Now
\[
f'(q)=2q(2q^2+B).
\]
Since \(f(0)=C^2\ne0\), a repeated root would have to satisfy
\[
q^2=-B/2.
\]
At such a point,
\[
f(q)=C^2-\frac{B^2}{4}.
\]
But
\[
B^2-4C^2
=(4A-2C)^2-4C^2
=16A(A-C)\ne0.
\]
Thus \(f\) is squarefree. A double cover of \(\mathbb P^1\) branched at four distinct points has genus one by Riemann–Hurwitz. ∎

This shows exactly why the elementary two-column parametrization does not induct: the third square condition is already elliptic rather than rational.

---

### 4. The row and column curves and their genera

Fix distinct rational columns \(E_1,\dots,E_r\). A possible new row is a rational point of
\[
\mathcal R_E:\qquad Y_j^2=T+E_j^2,\quad 1\le j\le r. \tag{4.1}
\]

Likewise, for fixed distinct positive rational rows \(T_1,\dots,T_r\), a possible new column is a rational point of
\[
\mathcal C_T:\qquad Z_i^2=E^2+T_i,\quad 1\le i\le r. \tag{4.2}
\]

#### Lemma 4.1: genus of the row curve

For \(r\ge2\), the smooth projective model of \(\mathcal R_E\) has genus
\[
g_R(r)=1+2^{r-2}(r-3).
\]

#### Proof

Work over an algebraic closure \(k\) of \(\mathbb Q\). The function field is
\[
k(T)\bigl(\sqrt{T+E_1^2},\dots,\sqrt{T+E_r^2}\bigr).
\]
The square classes of the \(r\) linear polynomials \(T+E_j^2\) are independent: each has odd valuation at its own zero \(T=-E_j^2\), where every other factor has valuation zero. Hence the cover of \(\mathbb P^1_T\) has degree \(2^r\).

There is ramification of index \(2\) over each of the \(r\) finite points
\[
T=-E_j^2.
\]
There is also index-two ramification over infinity. Locally at infinity, all \(T+E_j^2\) have the same nonsquare class because their pairwise ratios tend to \(1\) and are local squares. Thus each of the \(r+1\) branch points contributes
\[
2^r\left(1-\frac12\right)=2^{r-1}
\]
to the ramification divisor.

Riemann–Hurwitz gives
\[
2g_R-2=-2\cdot2^r+(r+1)2^{r-1}
=2^{r-1}(r-3),
\]
hence
\[
g_R=1+2^{r-2}(r-3).
\]
∎

In particular,
\[
g_R(2)=0,\qquad g_R(3)=1,\qquad g_R(4)=5.
\]

#### Lemma 4.2: genus of the column curve

The smooth projective model of \(\mathcal C_T\) has genus
\[
g_C(r)=1+2^{r-1}(r-2).
\]

#### Proof

Its function field is
\[
k(E)\bigl(\sqrt{E^2+T_1},\dots,\sqrt{E^2+T_r}\bigr).
\]
The square classes are independent because the quadratic polynomials have disjoint simple zero sets when the \(T_i\) are distinct and nonzero. The covering degree is therefore \(2^r\).

Each polynomial \(E^2+T_i\) has two simple roots, giving \(2r\) branch points, all with inertia order \(2\). There is no ramification at infinity: \(E^2+T_i=E^2(1+T_i/E^2)\), and \(1+T_i/E^2\) is a local square.

Thus
\[
2g_C-2=-2\cdot2^r+2r\cdot2^{r-1}
=2^r(r-2),
\]
which gives
\[
g_C=1+2^{r-1}(r-2).
\]
∎

In particular,
\[
g_C(1)=0,\qquad g_C(2)=1,\qquad g_C(3)=5,\qquad g_C(4)=17.
\]

The asymmetry between the two formulas comes from the extra requirement that the column coordinate itself be \(E\), rather than an arbitrary square root of a translated parameter.

---

### 5. Every fixed grid of size at least three has only finitely many nondegenerate extensions

#### Theorem 5.1

Let
\[
(T_i,E_j,X_{ij})_{1\le i,j\le r}
\]
be a fixed rational \(r\times r\) grid with \(r\ge3\), distinct positive \(T_i\), and distinct nonnegative \(E_j\). Then there are only finitely many pairs
\[
(T_*,E_*)\in\mathbb Q_{>0}\times\mathbb Q_{\ge0}
\]
with
\[
T_*\notin\{T_1,\dots,T_r\},\qquad
E_*\notin\{E_1,\dots,E_r\},
\]
that extend the grid to an \((r+1)\times(r+1)\) rational grid.

#### Proof

Any possible new column \(E_*\) must give a rational point on \(\mathcal C_T\):
\[
Z_i^2=E_*^2+T_i,\qquad 1\le i\le r.
\]
By Lemma 4.2,
\[
g_C(r)=1+2^{r-1}(r-2)\ge5.
\]
Faltings’ theorem therefore implies that \(\mathcal C_T(\mathbb Q)\) is finite. In particular, there are only finitely many possible values of \(E_*\).

Fix one such \(E_*\) distinct from all old columns. A compatible new row \(T_*\) is then a rational point on the row curve for the \(r+1\) distinct columns
\[
E_1,\dots,E_r,E_*.
\]
By Lemma 4.1, this curve has genus
\[
g_R(r+1)=1+2^{r-1}(r-2)\ge5.
\]
Again, Faltings’ theorem gives only finitely many rational points, and therefore finitely many possible \(T_*\).

There are only finitely many candidate \(E_*\), and for each only finitely many candidate \(T_*\), proving the assertion. ∎

This theorem is non-effective: it proves finiteness but does not give a usable search bound. It nevertheless rules out an induction that extends one fixed \(r\ge3\) grid through a positive-dimensional rational family.

---

### 6. The extension variety is two-dimensional but has no rational curves

For a fixed \(r\times r\) grid, introduce the extension variety
\[
\mathcal S:
\begin{cases}
Y_j^2=T+E_j^2,&1\le j\le r,\\
Z_i^2=T_i+E^2,&1\le i\le r,\\
W^2=T+E^2.&
\end{cases} \tag{6.1}
\]
A desired extension is exactly a rational point of \(\mathcal S\) with
\[
T\notin\{T_i\},\qquad E\notin\{E_j\},
\]
and the required positivity.

For each old row \(a\) and old column \(b\), there is a degenerate rational point
\[
T=T_a,\qquad E=E_b,
\]
with
\[
Y_j=X_{aj},\qquad Z_i=X_{ib},\qquad W=X_{ab}.
\]

The variety has \(2r+3\) variables and \(2r+1\) equations. At a degenerate point, all \(Y_j,Z_i,W\) are nonzero. The Jacobian with respect to these \(2r+1\) square-root variables contains the diagonal entries
\[
2Y_1,\dots,2Y_r,\quad
2Z_1,\dots,2Z_r,\quad
2W,
\]
so it has full rank. Thus every degenerate point is smooth and lies on a local two-dimensional component.

This validates the naive dimension count but does not produce new rational points.

#### Theorem 6.1

If \(r\ge3\), the extension variety \(\mathcal S\) contains no nonconstant rational curve over \(\overline{\mathbb Q}\).

#### Proof

There are natural projections
\[
\mathcal S\longrightarrow\mathcal R_E,\qquad
\mathcal S\longrightarrow\mathcal C_T
\]
obtained by retaining \((T,Y_1,\dots,Y_r)\) and \((E,Z_1,\dots,Z_r)\), respectively.

Suppose a nonconstant rational map
\[
\phi:\mathbb P^1\dashrightarrow\mathcal S
\]
existed. Composing with the two projections and passing to smooth projective models would give rational maps
\[
\mathbb P^1\dashrightarrow\overline{\mathcal R}_E,\qquad
\mathbb P^1\dashrightarrow\overline{\mathcal C}_T.
\]
Since the targets are proper curves, these maps extend over the finitely many points of indeterminacy.

For \(r\ge3\),
\[
g(\overline{\mathcal R}_E)\ge1,\qquad
g(\overline{\mathcal C}_T)\ge5.
\]
There is no nonconstant morphism from \(\mathbb P^1\) to a positive-genus curve: Riemann–Hurwitz would give
\[
-2=\deg(\phi)(2g-2)+R,
\]
whose right side is nonnegative when \(g\ge1\). Hence both projections are constant.

It follows that \(T,E,Y_j,Z_i\) are all constant along \(\phi\). Then \(W^2=T+E^2\) is constant, so \(W\) is also constant. Thus \(\phi\) itself is constant, a contradiction. ∎

Therefore the smooth two-dimensional germ at a duplicated extension cannot be turned into a rational-curve deformation separating the duplicate row and column.

---

### 7. No separated rational-function square identity exists

A natural Route 1 ansatz is
\[
T_i=F(u_i),\qquad E_j=G(v_j),\qquad X_{ij}=H(u_i,v_j)
\]
for fixed rational functions \(F,G,H\), hoping for an identity
\[
H(u,v)^2=F(u)+G(v)^2. \tag{7.1}
\]

#### Theorem 7.1

There do not exist nonconstant rational functions
\[
F\in\mathbb Q(u),\qquad G\in\mathbb Q(v),\qquad
H\in\mathbb Q(u,v)
\]
satisfying (7.1) identically.

#### Proof

Assume such functions exist. Choose rational values \(u=a,b\) avoiding all poles and satisfying
\[
c_1=F(a)\ne0,\qquad c_2=F(b)\ne0,\qquad c_1\ne c_2.
\]
This is possible because \(F\) is nonconstant.

Set
\[
H_1(v)=H(a,v),\qquad H_2(v)=H(b,v).
\]
Then
\[
H_1(v)^2=G(v)^2+c_1,\qquad
H_2(v)^2=G(v)^2+c_2.
\]
Thus \(v\) defines a nonconstant rational map from \(\mathbb P^1\) to the projective curve
\[
C:\quad
X_1^2=Y^2+c_1W^2,\qquad
X_2^2=Y^2+c_2W^2
\]
in \(\mathbb P^3\). It is nonconstant because \(G\) is nonconstant.

The curve \(C\) is a smooth intersection of two quadrics. To check smoothness, suppose
\[
\alpha\nabla(X_1^2-Y^2-c_1W^2)
+\beta\nabla(X_2^2-Y^2-c_2W^2)=0
\]
at a point of \(C\), with \((\alpha,\beta)\ne(0,0)\). If \(\alpha=0\) or \(\beta=0\), the resulting equations force all projective coordinates to vanish. Thus \(\alpha\beta\ne0\), forcing \(X_1=X_2=0\). The defining equations then give
\[
-Y^2=c_1W^2=c_2W^2,
\]
and \(c_1\ne c_2\) forces \(W=Y=0\), again impossible. Hence \(C\) is smooth.

A smooth complete intersection of two quadrics in \(\mathbb P^3\) has genus one. But no nonconstant rational map \(\mathbb P^1\to C\) exists by Riemann–Hurwitz. This is the required contradiction. ∎

#### Corollary 7.2: bounded-degree ansätze cannot work for unbounded \(k\)

Let \(F,G,H\) be fixed rational functions as above, and let \(R(u,v)\) be the numerator, after clearing denominators, of
\[
H(u,v)^2-F(u)-G(v)^2.
\]
Suppose its bidegree is at most \((m,n)\). If sets \(U,V\subset\mathbb Q\), avoiding all poles, satisfy
\[
H(u,v)^2=F(u)+G(v)^2
\quad\text{for every }(u,v)\in U\times V
\]
and
\[
|U|>m,\qquad |V|>n,
\]
then \(R\) vanishes identically: for each \(u\in U\), it has more than \(n\) roots as a polynomial in \(v\), and then each coefficient has more than \(m\) roots as a polynomial in \(u\). Theorem 7.1 then forces \(F\) or \(G\) to be constant.

Consequently, any successful separated ansatz must have algebraic degree growing with the grid size or must use fundamentally nonseparated formulas.

---

### 8. No high-genus “addition law” can combine several rows

The following standard rigidity result further limits an inductive construction.

#### Lemma 8.1

Let \(C\) be a smooth projective curve of genus at least two over an algebraically closed field of characteristic zero. Every rational map
\[
\Phi:C^m\dashrightarrow C
\]
is either constant or has the form
\[
\Phi(P_1,\dots,P_m)=\alpha(P_i)
\]
for some coordinate \(i\) and some automorphism \(\alpha\in\operatorname{Aut}(C)\).

#### Proof

It suffices to consider \(m=2\) and then induct. Restrict \(\Phi\) to a generic slice \(C\times\{Q\}\). A rational map between smooth projective curves extends to a morphism. If the generic slice is nonconstant, it is a self-map \(C\to C\). Riemann–Hurwitz gives
\[
2g-2=d(2g-2)+R,
\]
so \(d=1\) and \(R=0\); it is an automorphism. Since \(\operatorname{Aut}(C)\) is finite, this automorphism cannot vary nontrivially with \(Q\). Thus \(\Phi\) depends only on the first coordinate. If the generic slice is constant, then \(\Phi\) factors rationally through the second coordinate. Induction proves the general case. ∎

For \(r\ge4\), the fixed-column row curve has genus at least five. Thus there is no chord-and-tangent-type rational operation combining several existing row points to produce a genuinely new row point, except through an automorphism of one existing point. This is a precise reason the elliptic method used at smaller sizes does not formally generalize.

---

### Ledger

#### Proved

1. Rational grids clear denominators to integral solutions.
2. Any two rational columns support arbitrarily many distinct positive rational rows.
3. A third distinct fixed column produces a smooth genus-one quartic.
4. Exact genus formulas for the row and column curves.
5. Every fixed \(r\times r\) rational grid with \(r\ge3\) has only finitely many nondegenerate one-step rational extensions.
6. The fixed-grid extension surface is two-dimensional and smooth at duplicated extensions but contains no nonconstant rational curves for \(r\ge3\).
7. No nontrivial identity \(H(u,v)^2=F(u)+G(v)^2\) with separated one-variable \(F,G\) exists.
8. Consequently, fixed bounded-degree separated ansätze cannot produce unbounded square grids.
9. A rational operation on a fixed genus-\(\ge2\) row curve cannot combine multiple points except by selecting one coordinate and applying an automorphism.

#### Plausible but unproved

1. For algebraically generic columns, the full automorphism group of the row curve is only the multiquadratic deck group, which preserves \(T\). If proved uniformly, Lemma 8.1 would imply that a generic rational row-extension rule merely duplicates an old \(T\).
2. The extendible members of natural low-degree families of \(r\times r\) grids may form a thin exceptional locus for \(r\ge4\).
3. Special branch configurations with extra elliptic quotients remain the most plausible source of exceptional moving families.

#### Dead ends

1. **Dimension-count induction:** the extension fiber is indeed two-dimensional, but its rational points are arithmetically sparse; for \(r\ge3\) it has no rational curves.
2. **Perturbing a duplicate row and column:** duplicated extensions are smooth, not singular points from which a rational parametrization is forced.
3. **Uniform separated formulas:** ruled out by Theorem 7.1.
4. **Keeping a fixed grid and parametrically extending it:** ruled out for \(r\ge3\) by Theorems 5.1 and 6.1.
5. **Using a group law on the fixed row curve:** possible at genus one, but Lemma 8.1 blocks an analogous construction once the genus is at least two.

## Self-Audit

1. **The genus calculations require careful treatment of infinity.**  
   This is the most technically delicate proved step. I explicitly accounted for the common index-two ramification at infinity on the row curve and the absence of ramification at infinity on the column curve. The formulas also recover the known values \(0,1,5\), which is a useful consistency check.

2. **The finiteness theorem is non-effective.**  
   Faltings proves that a fixed grid has finitely many extensions but supplies no computable height bound. Thus it does not make a finite search conclusive. The finiteness statement itself is nevertheless unconditional and follows directly from curves of genus at least five.

3. **The obstruction applies to fixed grids and bounded-degree/separated families, not all moving families.**  
   A family could vary the old columns, old rows, and extension point simultaneously along an exceptional arithmetic locus. None of the proved lemmas excludes that possibility. This limitation is why the status is BLOCKED rather than a disproof.

## Computations To Verify

The following code uses exact rational arithmetic.

```python
from fractions import Fraction
from math import isqrt
from itertools import product

def is_square_int(n):
    if n < 0:
        return False
    r = isqrt(n)
    return r*r == n

def is_square_Q(x):
    x = Fraction(x)
    return x >= 0 and is_square_int(x.numerator) and is_square_int(x.denominator)

def verify_rational_grid(Ts, Es):
    assert len(set(Ts)) == len(Ts)
    assert len(set(Es)) == len(Es)
    assert all(T > 0 for T in Ts)
    assert all(E >= 0 for E in Es)
    return all(is_square_Q(T + E*E) for T, E in product(Ts, Es))
```

Verify the two-column parametrization:

```python
def two_column_row(E1, E2, q):
    E1, E2, q = map(Fraction, (E1, E2, q))
    assert 0 <= E1 < E2
    assert 0 < q < E2 - E1
    C = E2*E2 - E1*E1
    X1 = (C/q - q) / 2
    X2 = (C/q + q) / 2
    T = X1*X1 - E1*E1
    assert T > 0
    assert X1*X1 == T + E1*E1
    assert X2*X2 == T + E2*E2
    return T, X1, X2

# Example: arbitrarily many rows over columns 0 and 12
qs = [Fraction(a, b)
      for b in range(1, 20)
      for a in range(1, 12*b)
      if Fraction(a, b) < 12]

rows = [two_column_row(0, 12, q)[0] for q in qs]
assert len(rows) == len(set(rows))
assert verify_rational_grid(rows[:20], [Fraction(0), Fraction(12)])
```

Verify the third-column quartic identity and discriminant:

```python
import sympy as sp

q, A, C = sp.symbols('q A C', nonzero=True)
B = 4*A - 2*C
f = q**4 + B*q**2 + C**2

# Repeated roots occur only if A = 0 or A = C
print(sp.factor(sp.discriminant(f, q)))
# Expected: a nonzero constant times C^2 * A^2 * (A-C)^2

X1 = (C/q - q)/2
print(sp.factor(4*q**2 * (X1**2 + A) - f))
# Expected: 0
```

An exact bounded-height search for extensions of a supplied rational grid:

```python
def rationals_nonnegative(height):
    vals = {Fraction(0)}
    for den in range(1, height + 1):
        for num in range(0, height + 1):
            vals.add(Fraction(num, den))
    return sorted(vals)

def positive_rationals_below(bound, height):
    vals = set()
    for den in range(1, height + 1):
        for num in range(1, height + 1):
            q = Fraction(num, den)
            if q < bound:
                vals.add(q)
    return sorted(vals)

def bounded_extension_search(Ts, Es, height):
    """
    Exact within the enumerated rational-height boxes.
    Not a global exhaustive search.
    """
    Ts = list(map(Fraction, Ts))
    Es = sorted(map(Fraction, Es))
    assert verify_rational_grid(Ts, Es)
    assert len(Es) >= 2

    new_columns = []
    for E in rationals_nonnegative(height):
        if E in Es:
            continue
        if all(is_square_Q(T + E*E) for T in Ts):
            new_columns.append(E)

    E1, E2 = Es[0], Es[1]
    C = E2*E2 - E1*E1
    extensions = []

    for Enew in new_columns:
        augmented = Es + [Enew]
        for q in positive_rationals_below(E2 - E1, height):
            X1 = (C/q - q)/2
            Tnew = X1*X1 - E1*E1
            if Tnew <= 0 or Tnew in Ts:
                continue
            if all(is_square_Q(Tnew + E*E) for E in augmented):
                extensions.append((Tnew, Enew))

    return sorted(set(extensions))
```

A SageMath test for a fixed-node polynomial ansatz
\[
T=F(u),\quad E=G(v),\quad X=H(u,v)
\]
at \(k=5\), saturated away from repeated row and column values:

```python
# SageMath pseudocode
k = 5
dF = dG = 2
dHu = dHv = 2

names = (
    [f"a{i}" for i in range(dF+1)] +
    [f"b{i}" for i in range(dG+1)] +
    [f"c{i}_{j}" for i in range(dHu+1) for j in range(dHv+1)] +
    ["z"]
)

P = PolynomialRing(QQ, names=names)
gens = list(P.gens())
ptr = 0

a = gens[ptr:ptr+dF+1]; ptr += dF+1
b = gens[ptr:ptr+dG+1]; ptr += dG+1
cflat = gens[ptr:ptr+(dHu+1)*(dHv+1)]
ptr += (dHu+1)*(dHv+1)
z = gens[ptr]

c = [[cflat[i*(dHv+1)+j] for j in range(dHv+1)]
     for i in range(dHu+1)]

def F(u):
    return sum(a[i]*u**i for i in range(dF+1))

def G(v):
    return sum(b[j]*v**j for j in range(dG+1))

def H(u, v):
    return sum(c[i][j]*u**i*v**j
               for i in range(dHu+1)
               for j in range(dHv+1))

U = list(range(1, k+1))
V = list(range(1, k+1))

eqs = [H(u,v)^2 - F(u) - G(v)^2 for u in U for v in V]

DeltaRows = prod(F(U[i]) - F(U[j])
                 for i in range(k) for j in range(i))
DeltaCols = prod(G(V[i]) - G(V[j])
                 for i in range(k) for j in range(i))
Delta = DeltaRows * DeltaCols

I = P.ideal(eqs + [z*Delta - 1])
print("dimension:", I.dimension())
print("unit ideal:", I == P.ideal(1))
```

For a serious \(k=5\) experiment, one should run this over several degree patterns, then let the nodes \(U_i,V_j\) vary and saturate by
\[
\prod_{i<i'}(U_i-U_{i'})
\prod_{j<j'}(V_j-V_{j'})
\prod_{i<i'}(F(U_i)-F(U_{i'}))
\prod_{j<j'}(G(V_j)-G(V_{j'})).
\]
Any surviving component must still be checked for rational points, positivity, and denominator clearing.

## Route Diagnosis

The successful part of Route 1 is the exact description of its obstruction. Two columns are rationally flexible, but the third column is elliptic; from four fixed columns onward the row curve has genus at least five. More decisively, a fixed \(r\ge3\) grid has only finitely many nondegenerate rational extensions, and its extension surface has no rational curves. Thus neither dimension counts, perturbation of duplicated rows, bounded-degree formulas, nor a fixed-grid rational induction can work.

The unresolved possibility is a moving exceptional family: the old grid and the new row and column could vary simultaneously so that each high-genus fiber acquires one additional rational point. Establishing such a family is essentially as hard as constructing the next grid and is the precise block.

A fresh attempt should therefore not search for a rational parametrization of a fixed extension fiber. The most promising continuation is a hybrid of Routes 1 and 4:

1. Start with a parametrized \(4\times4\) family, preferably one arising from Bremner’s elliptic construction.
2. Form its relative extension surface.
3. Search for special parameter loci where the generalized multiquadratic row and column curves acquire elliptic quotients or explicit rational multisections.
4. Verify lifts on the full covering curves, not merely on the quotients.
5. Allow algebraic degrees to grow with \(k\); Theorem 7.1 rules out any fixed bounded-degree separated mechanism.

At present this reduces the problem to finding rational points on exceptional moving high-genus covers, an unproved problem of comparable strength. Hence Route 1 is blocked rather than solved.