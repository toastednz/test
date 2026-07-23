STATUS: BLOCKED

## Result

I found a genuine count-changing exact gadget and, more generally, an arbitrarily remote family of equal-weight admissible configurations whose interval counts differ by any prescribed integer. In particular,
\[
\begin{aligned}
&w(4,10)+w(17,18)+w(34,35)+w(82,83)+w(85,87)\\
&\qquad=w(2,3)+w(6,8)+w(82,84)+w(86,87),
\end{aligned}
\]
so four admissible intervals can be replaced by five. I also prove a general “padding lemma” which converts any equal-sum Egyptian-fraction identity with unequal term counts into an arbitrarily remote admissible block identity. Applied to
\[
\frac1{2s}=\sum_{j=1}^m\frac1{3^js}+\frac1{2\cdot3^ms},
\]
this yields admissible identities with interval-count difference exactly \(m\), for every \(m\ge1\). However, these gadgets cannot presently be inserted repeatedly into a representation of \(1\): their common padding has positive weight, and no exact admissible completion theorem is available. Establishing such a completion would be comparable in strength to the original problem. Thus Route 1 remains blocked at the compatibility/seed stage.

## Complete Argument

### 1. A useful defective representation of \(1\)

Write
\[
d(n):=w(n,n+1)=\frac1n+\frac1{n+1}.
\]

The Hickerson–Montgomery identity is
\[
2=w(2,7)+d(9)+d(17)+d(34)+d(84).
\]
Now
\[
w(2,7)-\left(d(4)+\frac17\right)
 =\frac12+\frac13+\frac16=1.
\]
Subtracting this equality from the Hickerson–Montgomery identity gives
\[
\boxed{
1=d(4)+\frac17+d(9)+d(17)+d(34)+d(84).
}
\tag{1}
\]
All terms except \(1/7\) already form valid separated dimers. Thus the supplied target-\(2\) example comes within one singleton defect of a representation of \(1\).

Removing \(1/7\) from (1) gives
\[
d(4)+d(9)+d(17)+d(34)+d(84)=\frac67.
\tag{2}
\]

Since
\[
d(84)=\frac1{84}+\frac1{85}
      =\frac1{42}-\frac1{84\cdot85}
      =\frac1{42}-\frac1{7140},
\]
equation (2) yields
\[
\begin{aligned}
d(4)+d(9)+d(17)+d(34)
 &=\frac67-\frac1{42}+\frac1{7140}\\
 &=\frac56+\frac1{7140}\\
 &=d(2)+\frac1{7140}.
\end{aligned}
\]
Because
\[
\frac1{7140}=\frac1{84}-\frac1{85},
\]
we obtain the signed endpoint identity
\[
\boxed{
d(4)+d(9)+d(17)+d(34)+\frac1{85}
=d(2)+\frac1{84}.
}
\tag{3}
\]

### 2. An exact four-to-five admissible replacement gadget

Add the same reciprocal sum
\[
C:=\frac16+\frac17+\frac18+\frac1{82}+\frac1{83}
       +\frac1{86}+\frac1{87}
\]
to both sides of (3).

On the left, the denominators \(4,5\), \(6,7,8\), and \(9,10\) merge into the single interval \([4,10]\). The remaining denominators form the intervals
\[
[17,18],\quad[34,35],\quad[82,83],\quad[85,87].
\]
Thus the left side becomes
\[
w(4,10)+w(17,18)+w(34,35)+w(82,83)+w(85,87).
\]

On the right, the denominators form
\[
[2,3],\quad[6,8],\quad[82,84],\quad[86,87].
\]
Consequently,
\[
\boxed{
\begin{aligned}
&w(4,10)+w(17,18)+w(34,35)+w(82,83)+w(85,87)\\
&\qquad=w(2,3)+w(6,8)+w(82,84)+w(86,87).
\end{aligned}}
\tag{4}
\]

Every interval in (4) has length at least \(2\). Consecutive intervals on either side have at least one omitted integer between them. The left side has five intervals and the right side four.

This is therefore a rigorous increment-one replacement gadget. Its limitation is that it is fixed: the five-block output does not contain another copy of the four-block input, so (4) cannot simply be iterated.

### 3. A general blockification lemma for equal reciprocal sums

The following gives arbitrarily movable count-changing gadgets.

**Lemma.**  
Let \(X,Y\subset\mathbb N\) be finite disjoint sets satisfying
\[
\sum_{x\in X}\frac1x=\sum_{y\in Y}\frac1y.
\tag{5}
\]
For every integer \(t\ge6\), there are admissible denominator sets \(S_X(t)\) and \(S_Y(t)\) such that

1. their reciprocal sums are equal;
2. every denominator is at least \(t-2\);
3. \(S_X(t)\) has \(|X|+2|Y|\) runs;
4. \(S_Y(t)\) has \(2|X|+|Y|\) runs.

Hence their run counts differ by \(|Y|-|X|\).

**Proof.**  
For each \(z\in X\cup Y\), put \(c_z=tz\) and define the common frame
\[
F_z:=\{c_z-2,c_z-1,c_z+1,c_z+2\}.
\]
Let
\[
T:=\bigcup_{z\in X\cup Y}F_z
\]
and define
\[
S_X(t):=T\cup\{tx:x\in X\},\qquad
S_Y(t):=T\cup\{ty:y\in Y\}.
\]

Because \(X\cap Y=\varnothing\), at each center \(c_z\) exactly one of the two sets contains \(c_z\).

If a side contains \(c_z\), the local selected set is
\[
[c_z-2,c_z+2]_{\mathbb N},
\]
one run of length \(5\).

If a side does not contain \(c_z\), the local selected set is
\[
[c_z-2,c_z-1]_{\mathbb N}
\cup[c_z+1,c_z+2]_{\mathbb N},
\]
two runs, each of length \(2\), separated by the omitted center.

Distinct centers differ by at least \(t\ge6\). Therefore, if \(c<c'\) are successive centers, then
\[
c'-2\ge c+4=(c+2)+2.
\]
Thus neighboring framed configurations remain separated by at least one omitted integer.

It follows that \(S_X(t)\) has one run for each \(x\in X\) and two for each \(y\in Y\):
\[
r(S_X(t))=|X|+2|Y|.
\]
Similarly,
\[
r(S_Y(t))=2|X|+|Y|.
\]

Finally, the frame contribution is identical on both sides, while (5) gives
\[
\sum_{x\in X}\frac1{tx}
=\frac1t\sum_{x\in X}\frac1x
=\frac1t\sum_{y\in Y}\frac1y
=\sum_{y\in Y}\frac1{ty}.
\]
Hence the total reciprocal sums of \(S_X(t)\) and \(S_Y(t)\) are equal. ∎

Taking \(t\) sufficiently large places the entire identity beyond any prescribed finite forbidden set.

### 4. Arbitrarily large count differences

For every \(m\ge1\) and \(s\ge1\),
\[
\boxed{
\frac1{2s}
=\sum_{j=1}^{m}\frac1{3^js}
 +\frac1{2\cdot3^ms}.
}
\tag{6}
\]

Indeed,
\[
\sum_{j=1}^{m}\frac1{3^js}
=\frac1s\cdot\frac{\frac13(1-3^{-m})}{1-\frac13}
=\frac1{2s}(1-3^{-m}),
\]
and adding \(1/(2\cdot3^ms)\) gives \(1/(2s)\).

Apply the lemma to
\[
X=\{2\},\qquad
Y_m=\{3,3^2,\ldots,3^m,2\cdot3^m\},
\]
and then scale by any \(s\ge6\). These sets are disjoint and
\[
|X|=1,\qquad |Y_m|=m+1.
\]
The resulting two admissible sides therefore have respectively
\[
1+2(m+1)=2m+3
\]
and
\[
2+(m+1)=m+3
\]
runs. Their difference is exactly \(m\).

Thus:

> For every \(m\ge1\), every sufficiently distant denominator range contains two finite admissible interval collections of exactly equal reciprocal weight whose interval counts differ by \(m\).

For \(m=1\), this already supplies arbitrarily remote increment-one identities, based on
\[
\frac1{2s}=\frac1{3s}+\frac1{6s}.
\]

### 5. Why these results do not solve the problem

The padding lemma adds the same positive frame weight to both sides. Its two sides therefore represent some rational
\[
R=C+\frac1{2s}>0,
\]
not zero and not generally \(1\).

To use such an identity in a representation of \(1\), one must already have one complete side as a subconfiguration of that representation, or else represent the complementary rational \(1-R\) by admissible intervals disjoint from the gadget. No argument above provides such a completion.

In particular:

- The fixed identity (4) can be applied only if its four-block side occurs in a representation of \(1\).
- Its five-block output does not contain another copy of the four-block input.
- The remote identities supplied by the lemma occupy different denominator sets for different scale parameters.
- Adding one of these identities to a representation is impossible because all terms are positive; it would increase the total above \(1\).
- Producing an admissible representation of the exact residual \(1-R\), with prescribed forbidden denominators, is essentially a remote blockification theorem and is comparable to the original unresolved difficulty.

Thus the count-control portion of Route 1 succeeds strongly, but the seed/compatibility portion remains unproved.

## Self-Audit

1. **The derivation of the fixed gadget depends on the supplied Hickerson–Montgomery identity.**  
   If that identity were misstated, equations (1)–(4) would fail. I believe this point is secure because every subsequent step is an elementary exact rational manipulation, and the code below independently verifies all resulting identities.

2. **The padding lemma relies on there being no accidental merging between neighboring framed centers.**  
   This is the most delicate geometric point. It holds because distinct centers are at least \(t\ge6\) apart: one framed neighborhood ends at \(c+2\), while the next begins at least at \(c+4\), leaving \(c+3\) omitted.

3. **Calling (4) a replacement gadget could suggest more reusability than has been proved.**  
   It is only a valid four-to-five equal-weight swap. I have not proved that its input side can occur in a target-\(1\) seed, nor that it regenerates itself. This limitation is precisely why the status is BLOCKED rather than SOLVED.

## Computations To Verify

```python
from fractions import Fraction

def d(n):
    return Fraction(1, n) + Fraction(1, n + 1)

def interval_weight(a, b):
    return sum((Fraction(1, n) for n in range(a, b + 1)), Fraction(0))

def interval_set(intervals):
    S = set()
    for a, b in intervals:
        assert 1 <= a < b
        for n in range(a, b + 1):
            assert n not in S
            S.add(n)
    return S

def runs(S):
    S = sorted(S)
    if not S:
        return []
    ans = []
    a = b = S[0]
    for n in S[1:]:
        if n == b + 1:
            b = n
        else:
            ans.append((a, b))
            a = b = n
    ans.append((a, b))
    return ans

def verify_intervals(intervals, target=None):
    S = interval_set(intervals)
    R = runs(S)
    assert R == intervals
    assert all(b - a + 1 >= 2 for a, b in R)
    assert all(R[i+1][0] >= R[i][1] + 2
               for i in range(len(R) - 1))
    value = sum((Fraction(1, n) for n in S), Fraction(0))
    if target is not None:
        assert value == target
    return value

# Hickerson–Montgomery identity.
hm = (interval_weight(2, 7) + d(9) + d(17)
      + d(34) + d(84))
assert hm == 2

# Defective target-1 identity.
defective = d(4) + Fraction(1, 7) + d(9) + d(17) + d(34) + d(84)
assert defective == 1

# Near identity.
A = d(4) + d(9) + d(17) + d(34)
assert A == d(2) + Fraction(1, 7140)
assert A + Fraction(1, 85) == d(2) + Fraction(1, 84)

# Fixed four-to-five gadget.
left = [(4, 10), (17, 18), (34, 35), (82, 83), (85, 87)]
right = [(2, 3), (6, 8), (82, 84), (86, 87)]

WL = verify_intervals(left)
WR = verify_intervals(right)
assert WL == WR
assert len(left) == 5
assert len(right) == 4

print("fixed gadget weight =", WL)
print("left runs =", left)
print("right runs =", right)
```

Verification of the general padding lemma and the arbitrary count-gap family:

```python
from fractions import Fraction

def reciprocal_sum(S):
    return sum((Fraction(1, n) for n in S), Fraction(0))

def blockify_equal_sets(X, Y, t):
    X, Y = set(X), set(Y)
    assert X.isdisjoint(Y)
    assert t >= 6
    assert reciprocal_sum(X) == reciprocal_sum(Y)

    centers = {t*z for z in X | Y}
    T = set()
    for c in centers:
        T.update([c-2, c-1, c+1, c+2])

    SX = T | {t*x for x in X}
    SY = T | {t*y for y in Y}

    RX = runs(SX)
    RY = runs(SY)

    assert all(b-a+1 >= 2 for a, b in RX)
    assert all(b-a+1 >= 2 for a, b in RY)
    assert all(RX[i+1][0] >= RX[i][1] + 2
               for i in range(len(RX)-1))
    assert all(RY[i+1][0] >= RY[i][1] + 2
               for i in range(len(RY)-1))

    assert reciprocal_sum(SX) == reciprocal_sum(SY)
    assert len(RX) == len(X) + 2*len(Y)
    assert len(RY) == 2*len(X) + len(Y)

    return SX, SY, RX, RY

for m in range(1, 9):
    X = {2}
    Y = {3**j for j in range(1, m+1)}
    Y.add(2 * 3**m)

    assert reciprocal_sum(X) == reciprocal_sum(Y)

    SX, SY, RX, RY = blockify_equal_sets(X, Y, t=20)
    assert len(RX) == 2*m + 3
    assert len(RY) == m + 3
    assert len(RX) - len(RY) == m

print("general count-gap identities verified")
```

A finite search worth running is whether the canonical padded family ever happens to have weight \(1/7\), which would combine directly with the valid \(6/7\) configuration from (2):

```python
def canonical_gap_gadget(m, s):
    X = {2*s}
    Y = {3**j * s for j in range(1, m+1)}
    Y.add(2 * 3**m * s)

    centers = X | Y
    T = set()
    for c in centers:
        T.update([c-2, c-1, c+1, c+2])

    SX = T | X
    SY = T | Y
    assert reciprocal_sum(SX) == reciprocal_sum(SY)
    return reciprocal_sum(SX), runs(SX), runs(SY)

hits = []
for m in range(1, 30):
    for s in range(6, 5000):
        W, RX, RY = canonical_gap_gadget(m, s)
        if W == Fraction(1, 7):
            hits.append((m, s, RX, RY))

print("canonical weight-1/7 hits:", hits)
```

A hit would not automatically settle all geometric compatibility issues with the \(6/7\) base, but it would be highly significant. No conclusion should be drawn from a bounded absence of hits.

## Route Diagnosis

### Proved ledger

1. The Hickerson–Montgomery example implies the exact defective identity
   \[
   1=d(4)+\frac17+d(9)+d(17)+d(34)+d(84).
   \]
2. It also implies the near-replacement identity
   \[
   d(4)+d(9)+d(17)+d(34)+\frac1{85}
   =d(2)+\frac1{84}.
   \]
3. Padding that identity gives the exact four-to-five admissible gadget (4).
4. Any disjoint equal-sum Egyptian-fraction identity can be converted, arbitrarily far out, into an admissible block identity. The run-count difference equals the difference in the original term counts.
5. Consequently, admissible equal-weight configurations with any prescribed count difference \(m\) exist arbitrarily far out.

### Plausible but unproved claims

- A remote exact-completion theorem: every sufficiently small rational residual in an appropriate denominator lattice can be represented by admissible blocks while avoiding a finite forbidden set.
- A seed representation of \(1\) containing the low-count side of one of the movable gadgets.
- A self-reproducing padded unit-fraction gadget whose output contains a compatible copy of its own input.

Any one of these, in sufficiently strong form, could finish Route 1, but none has been established.

### Dead ends

- The identity
  \[
  \frac1q=d(2q)+\frac1{2q(2q+1)}
  \]
  only moves a singleton defect to a much larger denominator. Iteration gives an infinite expansion, not a finite admissible representation.
- Scaling an exact block identity preserves reciprocal equality but destroys consecutiveness. Common padding repairs the geometry but adds positive weight, creating the unresolved completion problem.
- The fixed four-to-five gadget cannot be iterated because its output does not regenerate its input.
- Arbitrarily large count gaps alone do not address the target \(1\): equal-weight gadgets cannot be inserted “for free” into a positive reciprocal sum.

### Sharp block

The count-semigroup aspect of Route 1 is no longer the main obstacle: increment \(1\), and indeed every increment, is available in exact admissible equal-weight identities with arbitrary location freedom. The unresolved obstacle is:

> Construct a target-\(1\) seed containing a compatible side of arbitrarily many such gadgets, or construct a one-sided/self-reproducing gadget that can be applied without adding positive common padding.

At present that exact completion problem is of comparable strength to the original problem. A fresh attempt should therefore focus on blockifying a single unit fraction—especially the explicit defect \(1/7\) in (1)—or on designing padding whose total weight is paid for by an exact telescoping part of the source block rather than added equally to both sides.