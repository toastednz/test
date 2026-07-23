STATUS: BLOCKED

## Result

Route 3 yields a rigorous “almost blockification” mechanism: every unit fraction \(1/q\) can be converted into any prescribed finite number of mutually separated dimers, together with one smaller residual unit fraction; in the limit this gives an infinite separated-dimer expansion. I also found exact packet identities that blockify certain pairs of unit fractions, proved that no unit fraction is itself a dimer, and exhaustively proved that the natural residual \(1/6\) cannot be closed using two dimers. Finally, I proved that a fixed scaled Egyptian-fraction template cannot be blockified for infinitely many scales merely by independently replacing each term with its nearest under- or over-approximating dimer. The unresolved step is a finite closure of the residual unit fraction—already for \(1/6\), or uniformly along a specific rapidly growing orbit. That closure statement remains comparable in difficulty to the original problem, so Route 3 is blocked rather than solved.

## Complete Argument

### 1. Two exact local thickening identities

Write
\[
d(n):=\frac1n+\frac1{n+1}=w(n,n+1).
\]

For every \(q\ge1\),
\[
d(2q)
=\frac1{2q}+\frac1{2q+1}
=\frac1q-\frac1{2q(2q+1)}.
\]
Thus
\[
\boxed{\frac1q=d(2q)+\frac1{2q(2q+1)}}. \tag{1}
\]

There is also an over-approximating identity:
\[
d(2q-1)
=\frac1{2q-1}+\frac1{2q}
=\frac1q+\frac1{2q(2q-1)},
\]
hence
\[
\boxed{\frac1q=d(2q-1)-\frac1{2q(2q-1)}}. \tag{2}
\]

Identity (1) is the basic positive blockification step: it replaces a singleton \(1/q\) by one admissible interval and a smaller singleton.

---

### 2. Arbitrarily long finite blockification with one residual singleton

Define recursively
\[
q_0=q,\qquad q_{j+1}:=2q_j(2q_j+1).
\]
Let
\[
I_j=[2q_j,2q_j+1]_{\mathbb N}.
\]

Iterating (1) gives, for every \(t\ge1\),
\[
\boxed{\frac1q=\sum_{j=0}^{t-1}w(2q_j,2q_j+1)+\frac1{q_t}}. \tag{3}
\]

This follows by induction. The case \(t=1\) is (1). If it holds for \(t\), applying (1) to \(1/q_t\) gives the case \(t+1\).

The intervals in (3) are mutually separated. Indeed,
\[
2q_{j+1}=4q_j(2q_j+1),
\]
whereas \(I_j\) ends at \(2q_j+1\). For \(q_j\ge1\),
\[
2q_{j+1}-(2q_j+1)
=8q_j^2+2q_j-1\ge9,
\]
so in particular
\[
2q_{j+1}\ge(2q_j+1)+2.
\]

Also \(q_{j+1}>q_j\), so \(q_t\to\infty\). Letting \(t\to\infty\) in (3) gives the exact infinite expansion
\[
\frac1q=\sum_{j=0}^{\infty}d(2q_j). \tag{4}
\]
The geometry is fully admissible, but the collection is infinite and therefore (4) does not solve the problem.

For the original target, use
\[
1=d(2)+\frac16,
\qquad d(2)=\frac12+\frac13=\frac56.
\]
Taking \(q_0=6\) in (3),
\[
\boxed{
1=w(2,3)+\sum_{j=0}^{t-1}w(2q_j,2q_j+1)+\frac1{q_t}.
} \tag{5}
\]
Here
\[
q_0=6,\qquad q_1=156,\qquad q_2=97656,\ldots,
\]
so the first few intervals are
\[
[2,3],\quad [12,13],\quad [312,313],\quad [195312,195313],\ldots.
\]
Every finite truncation has exactly one forbidden singleton residual.

There are noncanonical transitions as well. For example,
\[
\frac16-\left(\frac1{14}+\frac1{15}\right)
=\frac16-\frac{29}{210}
=\frac1{35},
\]
and hence
\[
\boxed{1=w(2,3)+w(14,15)+\frac1{35}}. \tag{6}
\]
Applying (1) to \(1/35\) gives
\[
1=w(2,3)+w(14,15)+w(70,71)+\frac1{4970}.
\]
This shows that the particular orbit in (5) is not forced, but the terminal-singleton problem persists.

---

### 3. No unit fraction is a single dimer

#### Lemma

There are no positive integers \(a,q\) such that
\[
d(a)=\frac1q.
\]

#### Proof

If
\[
\frac{2a+1}{a(a+1)}=\frac1q,
\]
then
\[
q(2a+1)=a(a+1).
\]
But
\[
\gcd(2a+1,a)=1,\qquad
\gcd(2a+1,a+1)=1,
\]
and therefore
\[
\gcd(2a+1,a(a+1))=1.
\]
The displayed equality would imply \(2a+1\mid a(a+1)\), which is impossible because \(2a+1>1\). ∎

Consequently, none of the residual unit fractions in (3) can be closed by one further dimer.

---

### 4. The residual \(1/6\) cannot be represented by two dimers

This rules out the simplest possible completion of
\[
1=w(2,3)+\frac16.
\]

#### Lemma

There are no positive integers \(a,b\) such that
\[
d(a)+d(b)=\frac16.
\]
In particular, \(1/6\) is not a sum of two separated dimers.

#### Proof

Order the starts so that \(a\le b\). Since \(d(b)>0\),
\[
d(a)<\frac16.
\]
The sequence \(d(n)\) is strictly decreasing because
\[
d(n)-d(n+1)=\frac1n-\frac1{n+2}>0.
\]
Now
\[
d(11)=\frac{23}{132}>\frac16,
\qquad
d(12)=\frac{25}{156}<\frac16,
\]
so \(a\ge12\).

Since \(d(b)\le d(a)\),
\[
\frac16=d(a)+d(b)\le2d(a),
\]
and equality cannot occur because a dimer is not \(1/12\). Thus \(d(a)>1/12\). But
\[
d(23)=\frac{47}{552}>\frac1{12},
\qquad
d(24)=\frac{49}{600}<\frac1{12}.
\]
Hence
\[
12\le a\le23.
\]

For each such \(a\), reduce
\[
r_a:=\frac16-d(a)=\frac{P_a}{Q_a}.
\]
If \(r_a=d(b)\), then \(b\) is an integral root of
\[
P_ab(b+1)=Q_a(2b+1),
\]
whose discriminant is
\[
\Delta_a=(P_a-2Q_a)^2+4P_aQ_a
=P_a^2+4Q_a^2.
\]
Thus \(\Delta_a\) must be a square.

The exact residuals and square bounds are:

\[
\begin{array}{c|c|c}
a&r_a=P_a/Q_a& m^2< P_a^2+4Q_a^2<(m+1)^2\\ \hline
12&1/156&312^2<\Delta<313^2\\
13&5/273&546^2<\Delta<547^2\\
14&1/35&70^2<\Delta<71^2\\
15&3/80&160^2<\Delta<161^2\\
16&37/816&1632^2<\Delta<1633^2\\
17&8/153&306^2<\Delta<307^2\\
18&10/171&342^2<\Delta<343^2\\
19&73/1140&2281^2<\Delta<2282^2\\
20&29/420&840^2<\Delta<841^2\\
21&17/231&462^2<\Delta<463^2\\
22&59/759&1519^2<\Delta<1520^2\\
23&15/184&368^2<\Delta<369^2
\end{array}
\]

Thus no \(\Delta_a\) is a square, and no such \(b\) exists. ∎

This argument does not exclude three or more dimers, nor intervals of length greater than two.

---

### 5. Exact cancellation packets

Although a singleton cannot be turned into one dimer, certain pairs of singletons can.

For \(q\ge2\), identity (2) rearranges to
\[
\boxed{
\frac1q+\frac1{2q(2q-1)}
=d(2q-1).
} \tag{7}
\]

There is a second packet identity. Put
\[
U(q):=2q(2q+1).
\]
Using (1),
\[
d(2q)=\frac1q-\frac1{U(q)},
\]
while
\[
d(U(q))=\frac1{U(q)}+\frac1{U(q)+1}.
\]
Therefore
\[
\boxed{
\frac1q+\frac1{U(q)+1}
=d(2q)+d(U(q)).
} \tag{8}
\]
The two dimers on the right are separated because
\[
U(q)>2q+2.
\]

These identities show precisely what a successful Route 3 construction could exploit: an Egyptian expansion of \(1\) whose singleton terms can be organized into packets of the forms on the left of (7) or (8), or into more complicated packets with cancelling local errors. I did not find a packet decomposition covering \(1\) with cofinally many block counts.

---

### 6. A no-go theorem for independent one-step blockification of a fixed scaled template

A natural attempt is to take a fixed Egyptian expansion
\[
C=\sum_{d\in D}\frac1d
\]
and scale it:
\[
\frac Cm=\sum_{d\in D}\frac1{md}.
\]
For each term, independently choose either the under-dimer \(d(2md)\) or the over-dimer \(d(2md-1)\). The following theorem shows that this cannot work for infinitely many scale factors \(m\).

#### Theorem

Let \(D\) be a fixed finite nonempty set of distinct positive integers. There are only finitely many positive integers \(m\) for which one can partition
\[
D=O\sqcup U
\]
so that replacing \(1/(md)\) by the over-dimer for \(d\in O\) and the under-dimer for \(d\in U\) preserves the total sum.

#### Proof

For a fixed partition \(D=O\sqcup U\), preservation of the total is equivalent, by (1) and (2), to
\[
F_O(m)=0,
\]
where
\[
F_O(x):=
\sum_{d\in O}\frac1{2xd(2xd-1)}
-
\sum_{d\in U}\frac1{2xd(2xd+1)}.
\]

We claim that \(F_O(x)\) is not the zero rational function.

If \(O=\varnothing\), then \(F_O(x)<0\) for every positive real \(x\), so it is certainly nonzero.

If \(O\ne\varnothing\), choose \(d_0\in O\). The summand
\[
\frac1{2xd_0(2xd_0-1)}
\]
has a pole at
\[
x=\frac1{2d_0}.
\]
No other over-summand has a pole there because the members of \(D\) are distinct. No under-summand has a positive nonzero pole: its nonzero pole is at \(-1/(2d)\). Thus the pole at \(1/(2d_0)\) cannot cancel, proving that \(F_O\) is nonzero.

A nonzero rational function has only finitely many zeros. There are only \(2^{|D|}\) partitions \(O\sqcup U\). Taking the union of their finite zero sets proves the theorem. ∎

Thus fixed-template scaling, followed by one independent local thickening per Egyptian term, cannot furnish a parameterized infinite family. More elaborate coupled replacements or templates depending essentially on the target denominator are necessary.

---

### 7. Concrete application to the Hickerson–Montgomery identity

Let
\[
D_{\rm HM}=
\{2,3,4,5,6,7,9,10,17,18,34,35,84,85\}.
\]
The supplied identity says
\[
\sum_{n\in D_{\rm HM}}\frac1n=2.
\]
Consequently,
\[
\boxed{
1=\sum_{n\in D_{\rm HM}}\frac1{2n}.
} \tag{9}
\]
The source denominators in (9) are
\[
4,6,8,10,12,14,18,20,34,36,68,70,168,170.
\]

For each source denominator \(q\), choose either the under-dimer \([2q,2q+1]\) or the over-dimer \([2q-1,2q]\). Because consecutive source denominators differ by at least \(2\), all fourteen resulting dimers are automatically separated, regardless of the choices.

The resulting dimers sum to \(1\) exactly if and only if
\[
\sum_{q\in O}\frac1{2q(2q-1)}
=
\sum_{q\notin O}\frac1{2q(2q+1)}. \tag{10}
\]
This is a concrete exact \(2^{14}\)-case computation. A solution of (10) would prove \(P(14)\), but it would still not establish eventual attainability. I have not claimed an outcome for this finite search without executing it.

---

### 8. Precise remaining block

The most economical completion of Route 3 would be either of the following.

1. Prove that \(1/6\) has admissible block representations with every sufficiently large block count, all beginning after \(4\). Combining such a representation with \([2,3]\) would solve the original problem.

2. More narrowly, for
   \[
   q_0=6,\qquad q_{t+1}=2q_t(2q_t+1),
   \]
   prove that there is a fixed \(c\) such that every \(1/q_t\), for all sufficiently large \(t\), is a sum of exactly \(c\) separated admissible blocks lying after the preceding dimer. Formula (5) would then give representations of \(1\) with exactly \(t+c+1\) blocks for every sufficiently large \(t\).

Neither statement has been proved. Both require the same missing phenomenon: exact finite closure of a remote unit fraction by positive separated harmonic blocks. The local identities above only push the residual farther away; they do not eliminate it.

## Self-Audit

1. **The exhaustive two-dimer exclusion for \(1/6\) relies on a twelve-row arithmetic table.**  
   This is the most error-prone calculation. The range \(12\le a\le23\) is rigorously forced, and each row is independently checkable by the discriminant criterion \(P^2+4Q^2\). Exact verification code is provided below.

2. **The scaled-template no-go theorem uses a rational-function pole argument.**  
   The pole \(x=1/(2d_0)\) lies outside the integer parameter set, but that is irrelevant: it proves the rational function is not identically zero, after which its numerator has only finitely many roots, including integer roots. Distinctness of the template denominators ensures uniqueness of the pole.

3. **The assertion that Route 3 is blocked is a diagnosis, not an impossibility theorem.**  
   I have not proved that finite blockification of \(1/6\) is impossible, nor that another coupled Egyptian-fraction construction cannot work. The block is that all obtained positive local procedures leave a residual singleton, while the finite closure needed to remove it remains unproved and is already a substantial special case of the original problem.

## Computations To Verify

```python
from fractions import Fraction
from math import isqrt
from itertools import product

def d(n):
    return Fraction(1, n) + Fraction(1, n + 1)

# 1. Verify the local identities.
for q in range(1, 1000):
    assert Fraction(1, q) == d(2*q) + Fraction(1, 2*q*(2*q+1))
    assert Fraction(1, q) == d(2*q-1) - Fraction(1, 2*q*(2*q-1))

# 2. Verify finite Engel blockification.
def orbit(q, t):
    qs = [q]
    for _ in range(t):
        qs.append(2*qs[-1]*(2*qs[-1]+1))
    return qs

for q in range(1, 30):
    for t in range(1, 8):
        qs = orbit(q, t)
        lhs = sum((d(2*qs[j]) for j in range(t)), Fraction(0))
        lhs += Fraction(1, qs[t])
        assert lhs == Fraction(1, q)
        blocks = [(2*qs[j], 2*qs[j]+1) for j in range(t)]
        assert all(blocks[j+1][0] >= blocks[j][1] + 2
                   for j in range(t-1))

# 3. Verify the noncanonical transition 1/6 -> [14,15] + 1/35.
assert Fraction(1, 6) == d(14) + Fraction(1, 35)

# 4. Verify the exact table excluding two dimers for 1/6.
rows = []
for a in range(12, 24):
    r = Fraction(1, 6) - d(a)
    P, Q = r.numerator, r.denominator
    Delta = P*P + 4*Q*Q
    s = isqrt(Delta)
    assert s*s < Delta < (s+1)*(s+1)
    rows.append((a, P, Q, Delta, s))
print(rows)

# Direct bounded confirmation using the forced range for a.
for a in range(12, 24):
    r = Fraction(1, 6) - d(a)
    # Any solution is detected by the discriminant test.
    Delta = r.numerator**2 + 4*r.denominator**2
    assert isqrt(Delta)**2 != Delta

# 5. Verify the packet identities.
for q in range(2, 1000):
    V = 2*q*(2*q-1)
    assert Fraction(1, q) + Fraction(1, V) == d(2*q-1)

    U = 2*q*(2*q+1)
    assert Fraction(1, q) + Fraction(1, U+1) == d(2*q) + d(U)

# 6. Test all one-step under/over blockifications of the
# doubled Hickerson-Montgomery Egyptian expansion.
hm = list(range(2, 8)) + [9, 10, 17, 18, 34, 35, 84, 85]
assert sum((Fraction(1, n) for n in hm), Fraction(0)) == 2

source = [2*n for n in hm]
assert sum((Fraction(1, q) for q in source), Fraction(0)) == 1

def compatible(blocks):
    blocks = sorted(blocks)
    return (
        all(a < b for a, b in blocks)
        and all(blocks[i+1][0] >= blocks[i][1] + 2
                for i in range(len(blocks)-1))
    )

hm_solutions = []
for bits in product([0, 1], repeat=len(source)):
    # bit 0 = under-dimer [2q,2q+1]
    # bit 1 = over-dimer  [2q-1,2q]
    blocks = []
    total = Fraction(0)
    for q, over in zip(source, bits):
        start = 2*q - 1 if over else 2*q
        blocks.append((start, start+1))
        total += d(start)
    assert compatible(blocks)
    if total == 1:
        hm_solutions.append(blocks)

print("HM one-step solutions:", hm_solutions)

# 7. Exact bounded search for k blocks representing 1/q.
# This cannot establish global nonexistence, but it can find examples.
def bounded_block_search(q, k, N, min_start=2):
    target = Fraction(1, q)

    def rec(next_a, blocks_left, residual, path):
        if blocks_left == 0:
            return path if residual == 0 else None
        if residual <= 0:
            return None

        for a in range(next_a, N):
            weight = Fraction(0)
            for b in range(a, N + 1):
                weight += Fraction(1, b)
                if b == a:       # singleton not allowed
                    continue
                if weight > residual:
                    break
                ans = rec(
                    b + 2,
                    blocks_left - 1,
                    residual - weight,
                    path + [(a, b)]
                )
                if ans is not None:
                    return ans
        return None

    return rec(min_start, k, target, [])

# Suggested searches:
# for k in range(3, 10):
#     print("1/6", k, bounded_block_search(6, k, 500, min_start=5))
#
# for k in range(2, 20):
#     print("target 1", k, bounded_block_search(1, k, 500, min_start=2))

# 8. Search for one-dimer-plus-unit transitions
# 1/q = d(a) + 1/r, looking for parameterized patterns.
def unit_residual_transitions(Qmax, Amax):
    out = []
    for q in range(2, Qmax + 1):
        for a in range(2, Amax + 1):
            r = Fraction(1, q) - d(a)
            if r > 0 and r.numerator == 1:
                out.append((q, a, r.denominator))
    return out

print(unit_residual_transitions(200, 5000))
```

## Route Diagnosis

**Proved lemmas**

- Exact under- and over-dimer identities (1) and (2).
- Arbitrarily long finite separated-dimer expansions of \(1/q\) with one residual singleton, and an exact infinite separated-dimer expansion.
- No unit fraction is a single dimer.
- \(1/6\) is not a sum of two dimers, even without imposing separation.
- Exact two-singleton packet identities (7) and (8).
- A fixed scaled Egyptian template cannot be made exact for infinitely many scales by one independent under/over replacement per term.

**Plausible but unproved claims**

- \(1/6\) may have a finite representation by three or more dimers, or by a few longer blocks.
- Some orbit denominators \(q_t\) may admit bounded-size finite closures, but no uniform family has been found.
- Coupled error cancellation among many Egyptian terms may succeed even though independent one-step thickening of a fixed template cannot.

**Dead ends**

- Pure iteration of the positive identity (1): it creates as many separated blocks as desired but never removes the final singleton.
- Closing \(1/6\) with one or two dimers: rigorously impossible.
- Scaling a fixed Egyptian expansion and independently thickening each term once: incapable of producing an infinite parameter family by the rational-function theorem.
- Grouping Egyptian terms into the simple packets (7) and (8): exact locally, but arranging a complete expansion of \(1\) into such packets restates a substantial dimer subset-sum problem.

**Recommended fresh direction**

The most useful immediate computation is the \(2^{14}\)-case Hickerson–Montgomery orientation test, followed by exact searches for three- and four-dimer representations of \(1/6\). More importantly, a fresh theoretical attempt should search for a *coupled, parameterized packet identity* that replaces several unit fractions simultaneously and leaves no residual, rather than thickening terms independently. If no such family appears, Route 1—reusable block-replacement gadgets—or a common-denominator additive construction is more promising than further iteration of the one-residual identity.