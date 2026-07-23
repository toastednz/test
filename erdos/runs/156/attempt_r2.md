STATUS: BLOCKED

## Result

I did not solve Erdős Problem #156. I established a rigorous obstruction to the most natural degree-three Bose–Chowla implementation of Route 2. For every fixed scalar quotient of the multiplicative group of \(\mathbb F_{q^3}\), the resulting \(q\)-element Sidon set leaves a positive proportion of the quotient group outside \(B+B-B\); the midpoint set, having only \(O(q^2)\) elements, cannot repair these \(\Omega(q^3)\) holes. Thus this canonical finite-field construction is not saturated. I also verified that a \(q\)-element Sidon set cannot saturate the full additive group \(\mathbb F_q^3\) by counting, and that even perfect modular saturation has no automatic interval lift.

## Complete Argument

I use multiplicative notation for finite abelian groups in the main construction. Thus the Sidon condition means uniqueness of unordered pair products, and
\[
B+B-B
\quad\text{becomes}\quad
BB B^{-1}.
\]

### 1. The naive moment-curve ambient group is too large

Let \(G\) be an abelian group of odd order, and let \(B\subseteq G\) be a Sidon set of size \(q\). Then
\[
|B+B|=\binom{q+1}{2}.
\]
Consequently,
\[
|B+B-B|
 \le q\binom{q+1}{2}
 =\frac{q^2(q+1)}2.
\]
Because multiplication by \(2\) is bijective on an odd-order group,
\[
|\operatorname{Mid}(B)|=|B+B|=\frac{q(q+1)}2.
\]
Hence
\[
|(B+B-B)\cup\operatorname{Mid}(B)|
 \le \frac{q(q+1)^2}{2}.
\]
For \(q\ge 3\),
\[
\frac{q(q+1)^2}{2}<q^3.
\]
Therefore no \(q\)-element Sidon set can saturate an odd-order group of order \(q^3\). In particular, a \(q\)-point moment curve in the additive group \(\mathbb F_q^3\) cannot possibly work, independently of its algebraic properties.

This forces one either to enlarge the Sidon set by a constant factor or to quotient the ambient group by a constant factor.

---

### 2. A canonical scalar quotient of the degree-three Bose–Chowla construction

Fix an integer \(d\ge1\). Let \(q\) be an odd prime power such that
\[
3\mid q-1,\qquad d\mid q-1.
\]
Choose a noncube \(\rho\in\mathbb F_q^\times\). Then
\[
X^3-\rho
\]
has no root in \(\mathbb F_q\), hence is irreducible. Put
\[
K=\mathbb F_q(\theta),\qquad \theta^3=\rho.
\]
Thus \(K\cong\mathbb F_{q^3}\).

Let \(H\le \mathbb F_q^\times\) be the subgroup of order \(d\), and let
\[
G=K^\times/H.
\]
Define
\[
B=\{[\theta+t]:t\in\mathbb F_q\}\subseteq G,
\]
where brackets denote classes modulo \(H\).

The group has order
\[
|G|=\frac{q^3-1}{d}=\Theta_d(q^3),
\]
while \(|B|=q\).

#### Lemma 2.1: \(B\) is Sidon in \(G\)

Suppose
\[
[\theta+a][\theta+b]=[\theta+c][\theta+e]
\]
for \(a,b,c,e\in\mathbb F_q\). Then for some \(h\in H\),
\[
(\theta+a)(\theta+b)=h(\theta+c)(\theta+e).
\]
Therefore the polynomial
\[
(T+a)(T+b)-h(T+c)(T+e)
\]
vanishes at \(\theta\). Its degree is at most \(2\), while the minimal polynomial of \(\theta\) has degree \(3\). The polynomial must therefore vanish identically.

Comparison of leading coefficients gives \(h=1\), and then
\[
(T+a)(T+b)=(T+c)(T+e).
\]
Unique factorization gives
\[
\{a,b\}=\{c,e\}
\]
as multisets. Hence \(B\) is Sidon. \(\square\)

This argument works for every fixed scalar quotient \(H\): quotienting does not introduce pair-product collisions because the leading coefficient detects the scalar.

---

### 3. Exact characterization of triple coverage

Write an arbitrary element \(z\in K\) as
\[
z=x+y\theta+w\theta^2,
\qquad x,y,w\in\mathbb F_q.
\]
Assume \(w\ne0\).

The class \([z]\) lies in \(BB B^{-1}\) precisely when there are
\[
a,b,c\in\mathbb F_q,\qquad h\in H
\]
such that
\[
z(\theta+a)=h(\theta+b)(\theta+c).
\tag{1}
\]

Using \(\theta^3=\rho\), the left side is
\[
z(\theta+a)
=(w\rho+ax)+(x+ay)\theta+(y+aw)\theta^2.
\]
Comparison of the \(\theta^2\)-coefficients in (1) gives
\[
y+aw=h,
\]
so for each \(h\in H\), the value of \(a\) is forced:
\[
a=\frac{h-y}{w}.
\tag{2}
\]

After division by \(h\), the remaining quadratic must be
\[
T^2+u_hT+v_h=(T+b)(T+c),
\]
where
\[
u_h=\frac{x+ay}{h},
\qquad
v_h=\frac{w\rho+ax}{h}.
\]

Set
\[
U=\frac yw,\qquad V=\frac xw.
\]
Substitution of (2) gives
\[
u_h
 =U+\frac wh(V-U^2),
\]
and
\[
v_h
 =V+\frac wh(\rho-UV).
\]
Therefore the quadratic splits over \(\mathbb F_q\) if and only if its discriminant
\[
D_h(U,V,w)
 =
\left(U+\frac wh(V-U^2)\right)^2
 -
4\left(V+\frac wh(\rho-UV)\right)
\tag{3}
\]
is a square or zero in \(\mathbb F_q\).

Thus
\[
[z]\notin BB B^{-1}
\]
if and only if
\[
D_h(U,V,w)
\quad\text{is a nonsquare for every }h\in H.
\tag{4}
\]

---

### 4. The discriminant tests are asymptotically independent

Let \(\chi\) denote the quadratic character of \(\mathbb F_q\), extended by \(\chi(0)=0\). Define
\[
F(U,V,t)
 =
\bigl(U+t(V-U^2)\bigr)^2
 -
4\bigl(V+t(\rho-UV)\bigr).
\]
Then
\[
D_h(U,V,w)=F(U,V,w/h).
\]

We need the following standard character-sum estimate.

#### Lemma 4.1

For fixed \(d\), as \(q\to\infty\) through the above prime powers,
\[
\#\left\{
(U,V,w)\in\mathbb F_q^2\times\mathbb F_q^\times:
\chi(F(U,V,w/h))=-1\ \forall h\in H
\right\}
=
\frac{q^3}{2^d}+O_d(q^{5/2}).
\tag{5}
\]

#### Proof

For \(h\in H\), put
\[
f_h(U,V,w)=F(U,V,w/h).
\]

We first show that for every nonempty \(J\subseteq H\),
\[
P_J(U,V,w):=\prod_{h\in J}f_h(U,V,w)
\]
is squarefree as a polynomial in \(w\) over the rational function field
\[
\overline{\mathbb F_q}(U,V).
\]

Each \(f_h\) is squarefree generically. Indeed, for \(U=0\),
\[
F(0,V,t)=V^2t^2-4\rho t-4V,
\]
whose discriminant as a polynomial in \(t\) is
\[
16(\rho^2+V^3),
\]
which is not identically zero.

Distinct \(f_h\) are generically coprime. Let \(h\ne k\) and put \(c=h/k\ne1\). If \(t=w/h\), then a common root would satisfy
\[
F(0,V,t)=F(0,V,ct)=0.
\]
Their difference is
\[
F(0,V,ct)-F(0,V,t)
=(c-1)t\bigl(V^2(c+1)t-4\rho\bigr).
\]
If \(c=-1\), a common root would force \(t=0\), which is impossible when \(V\ne0\), since \(F(0,V,0)=-4V\).

If \(c\ne-1\), a common nonzero root is forced to be
\[
t=\frac{4\rho}{V^2(c+1)}.
\]
Substitution into \(F(0,V,t)=0\) gives a nonzero algebraic condition on \(V\), so it cannot hold identically. Hence the resultant of \(f_h\) and \(f_k\), viewed as polynomials in \(w\), is nonzero.

It follows that \(P_J\) is generically squarefree and in particular is not a square.

Consequently, outside \(O_d(q)\) exceptional pairs \((U,V)\), the specialization \(P_J(U,V,w)\) is a nonconstant squarefree polynomial in \(w\) of degree at most \(2|J|\). For each such pair, the Weil bound for quadratic character sums gives
\[
\left|
\sum_{w\in\mathbb F_q}\chi(P_J(U,V,w))
\right|
\le (2|J|-1)\sqrt q.
\]
The exceptional pairs contribute at most \(O_d(q^2)\). Thus, for every nonempty \(J\subseteq H\),
\[
\sum_{U,V\in\mathbb F_q}
\sum_{w\in\mathbb F_q^\times}
\chi(P_J(U,V,w))
=O_d(q^{5/2}).
\tag{6}
\]

Away from the zeros of the \(f_h\), the indicator that all \(f_h\) are nonsquares is
\[
2^{-d}\prod_{h\in H}(1-\chi(f_h)).
\]
The union of the zero sets \(f_h=0\) has \(O_d(q^2)\) points, by the bounded degree of the polynomials. Expanding the product, the empty subset contributes
\[
q^2(q-1)=q^3+O(q^2),
\]
and every nonempty subset contributes \(O_d(q^{5/2})\) by (6). This proves (5). \(\square\)

---

### 5. Positive-density holes in the Bose–Chowla quotient

The map
\[
(U,V,w)\longmapsto
z=wV+wU\theta+w\theta^2
\]
is a bijection from
\[
\mathbb F_q^2\times\mathbb F_q^\times
\]
onto the elements of \(K\) whose \(\theta^2\)-coefficient is nonzero.

By (4) and Lemma 4.1, the number of such \(z\) whose class is outside \(BB B^{-1}\) is
\[
\frac{q^3}{2^d}+O_d(q^{5/2}).
\]
The property of being outside \(BB B^{-1}\) is invariant under multiplication by \(H\), and every quotient class has exactly \(d\) representatives. Therefore
\[
\#\{[z]\in G:[z]\notin BB B^{-1},\ w(z)\ne0\}
=
\frac{q^3}{d\,2^d}+O_d(q^{5/2}).
\tag{7}
\]
In particular, for fixed \(d\) and all sufficiently large \(q\), there are \(\Omega_d(q^3)\) triple-uncovered classes.

It remains to check that midpoints cannot fill all of these holes. Since \(B\) is Sidon,
\[
|BB|=\binom{q+1}{2}.
\]
The group \(G\) is cyclic, so the squaring map has kernel of size at most \(2\). Hence
\[
|\{x\in G:x^2\in BB\}|
\le 2|BB|
=q(q+1)
=O(q^2).
\]
This is negligible compared with the \(\Omega_d(q^3)\) classes in (7). Therefore, for every fixed \(d\) and sufficiently large admissible \(q\),
\[
G\ne BB B^{-1}\cup\{x:x^2\in BB\}.
\]

We have proved:

#### Theorem 5.1

For every fixed \(d\), the degree-three Bose–Chowla set
\[
B=\{[\theta+t]:t\in\mathbb F_q\}
\subseteq \mathbb F_{q^3}^\times/H,
\qquad |H|=d,
\]
is Sidon but is not saturated for all sufficiently large admissible \(q\). Indeed, it leaves a positive proportion, asymptotic to \(2^{-d}\), of the scalar representatives outside \(BB B^{-1}\).

Thus quotienting by any fixed number of scalar normalizations does not remove the quadratic-residue obstruction. Taking \(d\) on the order of \(\log q\) would suppress the expected holes, but then
\[
|G|\asymp \frac{q^3}{\log q},
\]
and \(q\asymp (|G|\log |G|)^{1/3}\), reproducing rather than removing the logarithmic loss.

---

### 6. Modular saturation does not automatically lift to an interval

There is a very small exact example showing the lifting obstruction.

In \(\mathbb Z/4\mathbb Z\), let
\[
B=\{0,1\}.
\]
Its unordered pair sums are \(0,1,2\), so it is Sidon. Moreover,
\[
B+B-B=\mathbb Z/4\mathbb Z:
\]
the residue \(3\), for example, is represented by
\[
0+0-1\equiv3\pmod4.
\]
Thus \(B\) is modularly saturated.

Take the integer representatives and translate them into \([4]\):
\[
A=\{1,2\}.
\]
This is an integer Sidon set, but
\[
A+A-A=\{0,1,2,3\},
\qquad
\operatorname{Mid}(A)=\{1,2\}.
\]
The point \(4\) is not blocked. The modular witness is a wrap-around equality and does not become an integer equality.

Therefore even a successful finite cyclic construction would still require a separate, nontrivial interval-lifting theorem.

## Self-Audit

1. **The character-sum argument is the most technical point.**  
   Its delicate step is that every nonempty product of the discriminant polynomials is generically squarefree. I supplied explicit generic squarefreeness and pairwise-coprimality checks, after which the standard one-variable Weil bound applies outside an algebraic exceptional set of \(O_d(q)\) parameter pairs. This is a standard and robust argument, but explicit numerical constants were not tracked.

2. **The negative theorem concerns one canonical algebraic family, not all finite-field constructions.**  
   It rules out fixed scalar quotients of the degree-three Bose–Chowla set. It does not rule out unions of compatible curves, additive quotients with specially aligned fibers, or entirely different finite geometries. I have therefore not inferred any lower bound for \(\sigma(N)\).

3. **The interval-lifting example diagnoses failure but proves no universal impossibility theorem.**  
   It shows that choosing ordinary representatives is invalid. A more elaborate bounded-lift or carry-correcting construction might still exist. No such theorem was found here.

## Computations To Verify

The following SageMath code checks the finite construction exactly for small admissible \(q,d\).

```python
def bose_quotient_check(q, d):
    """
    q should be an odd prime power with 3 | q-1 and d | q-1.
    Returns Sidon status and exact uncovered classes.
    """
    q = Integer(q)
    assert (q - 1) % 3 == 0
    assert (q - 1) % d == 0

    F = GF(q)
    rho = next(a for a in F if a != 0 and
               a^((q - 1)//3) != 1)

    R.<T> = PolynomialRing(F)
    assert (T^3 - rho).is_irreducible()
    K.<theta> = F.extension(T^3 - rho)

    g = K.multiplicative_generator()
    M = (q^3 - 1)//d

    def quotient_log(z):
        # K^*/H is cyclic of order M.
        return Integer(z.log(g)) % M

    B = sorted({
        quotient_log(theta + K(t))
        for t in F
    })
    assert len(B) == q

    pair_sums = set()
    sidon = True
    for i, a in enumerate(B):
        for b in B[i:]:
            s = (a + b) % M
            if s in pair_sums:
                sidon = False
            pair_sums.add(s)

    triple_blocked = {
        (s - a) % M
        for s in pair_sums
        for a in B
    }

    midpoint_blocked = {
        x for x in range(M)
        if (2*x) % M in pair_sums
    }

    blocked = triple_blocked | midpoint_blocked
    missing = sorted(set(range(M)) - blocked)

    return {
        "q": q,
        "d": d,
        "group_order": M,
        "B": B,
        "sidon": sidon,
        "triple_coverage": len(triple_blocked),
        "midpoint_coverage": len(midpoint_blocked),
        "total_coverage": len(blocked),
        "missing_count": len(missing),
        "missing": missing,
    }
```

The discriminant-hole count from Lemma 4.1 can be checked without discrete logarithms:

```python
def discriminant_hole_count(q, d):
    q = Integer(q)
    assert q % 2 == 1
    assert (q - 1) % 3 == 0
    assert (q - 1) % d == 0

    F = GF(q)
    rho = next(a for a in F if a != 0 and
               a^((q - 1)//3) != 1)

    zeta = F.multiplicative_generator()^((q - 1)//d)
    H = [zeta^j for j in range(d)]
    assert len(set(H)) == d

    def chi(a):
        if a == 0:
            return 0
        return 1 if a.is_square() else -1

    count = 0
    for U in F:
        for V in F:
            for w in F:
                if w == 0:
                    continue

                all_nonsquare = True
                for h in H:
                    t = w/h
                    D = (U + t*(V - U^2))^2 \
                        - F(4)*(V + t*(rho - U*V))
                    if chi(D) != -1:
                        all_nonsquare = False
                        break

                if all_nonsquare:
                    count += 1

    expected = (q^2 * (q - 1)) / (2^d)
    return {
        "exact_representative_holes": count,
        "expected_main_term": expected,
        "ratio": RR(count) / RR(q^2 * (q - 1)),
        "predicted_ratio": RR(1) / RR(2^d),
        "quotient_hole_count": count // d,
    }
```

The modular-lifting counterexample can be checked by:

```python
def interval_check(N, A):
    A = sorted(A)

    sums = {}
    sidon = True
    for i, a in enumerate(A):
        for b in A[i:]:
            s = a + b
            if s in sums:
                sidon = False
            sums[s] = (a, b)

    blocked = set(A)
    for s in sums:
        for a in A:
            x = s - a
            if 1 <= x <= N:
                blocked.add(x)
        if s % 2 == 0 and 1 <= s//2 <= N:
            blocked.add(s//2)

    return sidon, sorted(set(range(1, N + 1)) - blocked)

print(interval_check(4, {1, 2}))
# Expected: (True, [4])
```

Further useful experiments would:

1. Test whether unions of two or more algebraic curves can remain Sidon in groups of order \(\Theta(q^3)\).
2. Search additive quotients in characteristic \(3\), where linearized-polynomial fibers might align with the square-discriminant condition.
3. For every modularly saturated candidate, optimize integer lifts \(b\mapsto b+n_bM\) and check whether any bounded family of lift patterns yields an interval blocker.

## Route Diagnosis

**Proved lemmas**

- A \(q\)-element Sidon set cannot saturate an odd-order group of order \(q^3\).
- Fixed scalar quotients of the degree-three Bose–Chowla set remain Sidon.
- For every fixed quotient order \(d\), those sets leave
  \[
  \frac{q^3}{d\,2^d}+O_d(q^{5/2})
  \]
  quotient classes outside \(BB B^{-1}\).
- Their \(O(q^2)\) midpoint sets cannot repair the holes.
- Modular saturation does not transfer by simply choosing integer representatives.

**Plausible but unproved**

- Any construction in which each target receives only a bounded number of essentially independent quadratic-splitting tests will retain a positive density of holes.
- Characteristic-\(3\) additive quotients may offer a way around independent residue tests by making every quotient fiber intersect the valid discriminant locus.
- A bounded union of algebraic curves might have enough triple capacity, but preserving Sidonicity across different components is a severe unresolved constraint.

**Dead ends**

- The basic moment curve in \(\mathbb F_q^3\): impossible by counting.
- Constant scalar quotients of degree-three Bose–Chowla sets: positive-density discriminant holes.
- Letting the scalar quotient grow like \(\log q\): restores the known logarithmic loss.
- Naive modular-to-integer lifting: destroyed by wrap-around.

**Precise block**

Route 2 now requires two new results, either of which is substantial:

1. A fundamentally different algebraic Sidon set of \(O(q)\) elements in a group of order \(\Theta(q^3)\) whose triple map has exact, structured coverage rather than finitely many independent residue tests.
2. An interval-transfer theorem that preserves both Sidonicity and complete domination with only constant-factor loss.

No such construction or transfer theorem was obtained. The current route is therefore blocked rather than merely missing a routine lemma.