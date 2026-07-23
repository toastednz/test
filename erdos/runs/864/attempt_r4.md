STATUS: BLOCKED

## Result

I did not prove Erdős Problem #864. Pursuing labeled hypergraph supersaturation leads, already in the fully reflected case, to a sharp “forbidden Golomb ruler” inequality that appears comparable in difficulty to the original problem. I established three rigorous partial results: an exact description of the collision hypergraph and of all duplicated differences; a uniform improved upper bound
\[
F(N)\le \sqrt{2N}+O(N^{1/4});
\]
and an exact reduction of the fully reflected case to a one-dimensional packing problem. The latter asks whether
\[
2R+G\ge 3m^2-o(m^2)
\]
whenever a Golomb ruler \(B\subseteq[0,R]\) has its positive differences disjoint from a shifted reflected sumset. Ordinary supersaturation or additive-energy estimates do not retain enough label information to prove this inequality.

## Complete Argument

### 1. The collision hypergraph and duplicated differences

Let \(A\subseteq[N]\) be admissible, let \(k=|A|\), and suppose \(s\) is its exceptional sum. Put
\[
t=r_A(s).
\]
If no exceptional sum exists, then \(A\) is a genuine Sidon set and the classical bound already gives
\[
k\le \sqrt N+O(N^{1/4}).
\]

Define the scalar collision count
\[
Q(A):=\sum_n \binom{r_A(n)}2.
\]

#### Lemma 1

For an admissible \(A\) with exceptional sum \(s\):

1. The \(t\) representations of \(s\) form a matching, with possibly one loop at \(s/2\).
2. Consequently,
   \[
   Q(A)=\binom t2,\qquad t\le \left\lceil\frac k2\right\rceil.
   \]
3. If
   \[
   \delta=
   \begin{cases}
   1,&s\text{ even and }s/2\in A,\\
   0,&\text{otherwise},
   \end{cases}
   \]
   then the number of positive differences \(d\) with \(m_A(d)=2\) is exactly
   \[
   q=(t-1)(t-\delta).
   \]

#### Proof

A vertex \(a\in A\) can occur in at most one representation of \(s\), namely with \(s-a\). Thus the off-diagonal representations are vertex-disjoint, and the only possible loop is \((s/2,s/2)\). This proves the first assertion and \(t\le\lceil k/2\rceil\).

Since \(s\) is the only repeated sum,
\[
Q(A)=\binom{r_A(s)}2=\binom t2.
\]

It remains to count duplicated differences. First, \(m_A(d)\le2\) for every \(d>0\). Indeed, if \(x<y\) are two bases with
\[
x,x+d,y,y+d\in A,
\]
then
\[
(x+d)+y=x+(y+d).
\]
The two unordered representations are distinct, so their common sum is \(s\). If a third base \(z\) existed, applying this to \(x,y\) and \(x,z\) would give
\[
x+y+d=s=x+z+d,
\]
hence \(y=z\).

Now take two distinct off-diagonal representations
\[
\{a,s-a\},\qquad \{c,s-c\},
\]
where, without loss of generality,
\[
a<c<s/2.
\]
They generate the two duplicated positive differences
\[
c-a=(s-a)-(s-c)
\]
and
\[
s-a-c=(s-c)-a=(s-a)-c.
\]
These two differences are distinct because \(c<s/2\).

A loop \(\{s/2,s/2\}\) together with an off-diagonal representation \(\{a,s-a\}\) generates exactly one duplicated difference:
\[
s/2-a=(s-a)-s/2.
\]

Conversely, every duplicated difference arises this way. If
\[
x,x+d,y,y+d\in A,\qquad x<y,
\]
then the two representations
\[
\{x+d,y\},\qquad \{x,y+d\}
\]
have common sum \(x+y+d\), hence that sum is \(s\). Thus the duplicated difference determines a pair of representations of \(s\).

Therefore every pair of off-diagonal representations contributes exactly two duplicated difference labels, while a pair consisting of the loop and an off-diagonal representation contributes exactly one. Hence
\[
q=2\binom{t-\delta}{2}+\delta(t-\delta).
\]
For \(\delta=0\), this is \(t(t-1)\); for \(\delta=1\), it is \((t-1)^2\). Both cases equal
\[
q=(t-1)(t-\delta).
\]
∎

This precisely describes the labeled collision hypergraph: its vertices at the representation level are the \(t\) matching edges of sum \(s\), and every pair of these edges forms a collision hyperedge labeled \(s\).

In particular, a supersaturation argument using only the number \(Q(A)\) would have to force
\[
Q(A)>\binom{\lceil k/2\rceil}{2}
\]
in order by itself to imply two labels. At the conjectured extremal construction,
\[
t\sim k/2,\qquad Q(A)\sim \frac{k^2}{8},
\]
so such an energy-only result would have to be asymptotically sharp.

---

### 2. Sidon extraction

The matching description also gives the familiar extraction estimate in a form useful for the hypergraph interpretation.

#### Lemma 2

For every admissible \(A\) with exceptional multiplicity \(t\),
\[
k-t+1\le S(N).
\]

#### Proof

Choose one representation of \(s\) to retain. From each of the other \(t-1\) mutually disjoint representations, delete one participating element. The resulting set \(B\) has at most one representation of \(s\), and no other sum has gained a representation. Therefore \(B\) is a genuine Sidon set and
\[
|B|=k-t+1\le S(N).
\]
∎

Thus
\[
k\le \sqrt N+t+O(N^{1/4}).
\]
This handles small \(t\), but when \(t\) is close to \(k/2\), it gives only the constant \(2\).

---

### 3. A self-contained Sidon interval estimate

I will use the following standard estimate.

#### Lemma 3

If \(B\) is a genuine Sidon set contained in an interval of \(M\) consecutive integers, then
\[
|B|\le \sqrt M+O(M^{1/4}),
\]
with an absolute implied constant.

#### Proof

Translate the interval and write
\[
B=\{b_1<\cdots<b_p\},\qquad R=b_p-b_1\le M-1.
\]
All positive differences \(b_j-b_i\), \(i<j\), are distinct. Indeed, an equality
\[
b_j-b_i=b_\ell-b_h
\]
gives
\[
b_j+b_h=b_\ell+b_i,
\]
and the Sidon property forces the two difference pairs to be identical.

Choose an integer \(q\) with \(1\le q<p\). The differences
\[
b_{i+r}-b_i,\qquad 1\le r\le q,\quad 1\le i\le p-r,
\]
are all distinct. Their number is
\[
L=qp-\frac{q(q+1)}2.
\]
Hence their sum is at least
\[
1+2+\cdots+L=\frac{L(L+1)}2.
\]

On the other hand, for each \(r\),
\[
\sum_{i=1}^{p-r}(b_{i+r}-b_i)
=
\sum_{j=p-r+1}^{p}b_j-\sum_{j=1}^{r}b_j
\le rR.
\]
Summing over \(1\le r\le q\),
\[
\frac{L(L+1)}2\le R\frac{q(q+1)}2.
\]
Thus
\[
R\ge \frac{L(L+1)}{q(q+1)}.
\]
Taking \(q=\lfloor\sqrt p\rfloor\) gives
\[
R\ge p^2-O(p^{3/2}).
\]

The distinct-difference bound \(\binom p2\le M-1\) first gives \(p=O(\sqrt M)\). Therefore
\[
p^2\le M+O(p^{3/2})=M+O(M^{3/4}),
\]
which implies
\[
p\le \sqrt M+O(M^{1/4}).
\]
∎

---

### 4. A uniform \(\sqrt2\) upper bound

#### Theorem 4

Every admissible \(A\subseteq[N]\) satisfies
\[
|A|\le \sqrt{2N}+O(N^{1/4}).
\]

#### Proof

If \(A\) has no exceptional sum, apply Lemma 3 directly.

Otherwise let \(s\) be the exceptional sum and partition
\[
L=\{a\in A:2a<s\},\qquad
H=\{a\in A:2a>s\},
\]
with possibly the single central element \(s/2\).

Every pair sum from \(L\) is strictly less than \(s\). Therefore a repeated pair sum inside \(L\) would be a second repeated label, which is impossible. Hence \(L\) is a genuine Sidon set. Similarly, every pair sum from \(H\) is strictly greater than \(s\), so \(H\) is also a genuine Sidon set.

The available interval for \(L\) has length
\[
X=\left\lfloor\frac{s-1}{2}\right\rfloor,
\]
and the available interval for \(H\) has length
\[
Y=N-\left\lfloor\frac s2\right\rfloor.
\]
Since \(2\le s\le2N\), these are nonnegative, and
\[
X+Y\le N.
\]
Indeed, the sum equals \(N-1\) when \(s\) is even and \(N\) when \(s\) is odd.

Lemma 3 gives
\[
|L|\le \sqrt X+O(N^{1/4}),\qquad
|H|\le \sqrt Y+O(N^{1/4}).
\]
There is at most one central element. Consequently,
\[
|A|\le \sqrt X+\sqrt Y+O(N^{1/4}).
\]
By Cauchy–Schwarz,
\[
\sqrt X+\sqrt Y\le \sqrt{2(X+Y)}\le\sqrt{2N}.
\]
This proves the theorem. ∎

This is still well above the conjectured constant \(2/\sqrt3\), but it improves the elementary constant \(2\).

---

### 5. Exact reduction of the fully reflected case

The sharp obstruction becomes visible when every element belongs to an exceptional representation.

Assume first that there is no central loop and that
\[
A=\{b_1,\dots,b_m,s-b_1,\dots,s-b_m\},
\qquad
b_1<\cdots<b_m<s/2.
\]
Thus \(|A|=2m\) and \(r_A(s)=m\).

Normalize by setting
\[
X=\{b_i-b_1:1\le i\le m\}\subseteq[0,R],
\qquad R=b_m-b_1,
\]
and let
\[
C=R-X=\{R-x:x\in X\},
\qquad
G=s-2b_m.
\]
Since \(b_m<s/2\), we have \(G\ge1\). Moreover,
\[
2R+G=s-2b_1.
\]
Because \(b_1\) and \(s-b_1\) both lie in \([N]\),
\[
2R+G\le N-1.
\]

Write
\[
D^+(X)=\{x_j-x_i:1\le i<j\le m\}.
\]

#### Proposition 5

Under the above hypotheses:

1. All elements of \(D^+(X)\) are distinct.
2. All unordered sums in \(C+C\) are distinct.
3. The following disjointness condition holds:
   \[
   D^+(X)\cap\bigl(G+(C+C)\bigr)=\varnothing.
   \tag{1}
   \]

Conversely, if \(X\subseteq[0,R]\) contains \(0,R\), has distinct positive differences, and satisfies (1) for some integer \(G\ge1\), then
\[
s=2R+G+2,\qquad
A=\{1+x:x\in X\}\cup\{s-(1+x):x\in X\}
\]
is admissible in
\[
[N],\qquad N=2R+G+1,
\]
and its only repeated sum is \(s\), with multiplicity \(|X|\).

#### Proof

The lower half \(\{b_1,\dots,b_m\}\) is a genuine Sidon set because all its pair sums are less than \(s\). Therefore its positive differences are distinct, and so are those of \(X\). The reflected set \(C\) has the same property, hence its unordered sums are distinct.

Suppose
\[
d=b_q-b_p\in D^+(\{b_i\}),\qquad p<q.
\]
The cross pair
\[
\{b_p,s-b_q\}
\]
has sum
\[
s-d<s.
\]
A collision with a lower-lower sum would be
\[
b_i+b_j=s-d,
\]
or
\[
d=s-b_i-b_j.
\]
After normalization,
\[
s-b_i-b_j
=s-2b_1-(b_i-b_1)-(b_j-b_1)
=2R+G-x_i-x_j.
\]
Since \(c_i=R-x_i\), this is
\[
G+c_i+c_j.
\]
Therefore admissibility gives (1).

For the converse, divide all pair sums into the following classes:

- lower-lower sums \(b_i+b_j<s\);
- upper-upper sums \(2s-(b_i+b_j)>s\);
- cross sums
  \[
  b_i+(s-b_j)=s+(b_i-b_j).
  \]

Distinct positive differences guarantee uniqueness among nonzero cross sums. Every pair with \(i=j\) has sum \(s\). Lower-lower sums are unique, and upper-upper sums are their reflections. The only possible collision between a lower-lower sum and a cross sum below \(s\) is precisely excluded by (1). Reflecting about \(s\) excludes the corresponding upper collision. The ranges below and above \(s\) otherwise do not interact.

Hence the only repeated sum is \(s\), and it has exactly \(|X|\) representations. The asserted value of \(N\) follows because the smallest element is \(1\) and the largest is \(s-1=2R+G+1\). ∎

A central element \(s/2\), if present, can be deleted, leaving the same reduction for the off-diagonal pairs. Thus it affects only \(O(1)\) in this fully reflected setting.

---

### 6. The precise blocked inequality

Proposition 5 reduces the fully reflected case to the following statement.

> **Forbidden-ruler inequality.**  
> Let \(X\subseteq[0,R]\) have \(m\) elements, contain \(0,R\), and have all positive differences distinct. Let \(C=R-X\). If
> \[
> D^+(X)\cap\bigl(G+(C+C)\bigr)=\varnothing
> \]
> for an integer \(G\ge1\), then
> \[
> 2R+G\ge 3m^2-o(m^2).
> \tag{FR}
> \]

If (FR) held, then Proposition 5 would give
\[
N\ge 2R+G+1\ge 3m^2-o(m^2),
\]
and therefore
\[
|A|=2m\le\left(\frac2{\sqrt3}+o(1)\right)\sqrt N
\]
for fully reflected sets.

Conversely, every triple \((X,R,G)\) satisfying Proposition 5 constructs a fully reflected admissible set of size \(2m\) in an interval of length \(2R+G+1\). Thus (FR) is exactly the conjectured asymptotic estimate for this special class.

The inequality is sharp if true: choosing any asymptotically optimal Golomb ruler \(X\subseteq[0,R]\), with
\[
m=(1+o(1))\sqrt R,
\]
and taking \(G=R+1\) makes disjointness automatic because
\[
D^+(X)\subseteq[1,R]
\]
while
\[
G+(C+C)\subseteq[R+1,3R+1].
\]
Then
\[
2R+G=3R+1=(3+o(1))m^2.
\]

What is presently provable is only
\[
R\ge m^2-O(m^{3/2})
\]
from Lemma 3, hence
\[
2R+G\ge 2m^2-O(m^{3/2}).
\]
Pure label counting is even weaker: the disjoint union has
\[
\binom m2+\binom{m+1}2=m^2
\]
elements, all lying in \([1,G+2R]\), so it gives only
\[
G+2R\ge m^2.
\]

The missing extra \(m^2\) must therefore come from the internal geometry of the difference and sum labels, not merely their number.

A tempting pointwise claim such as \(G\ge R\) is false. For example,
\[
X=\{0,2\},\qquad R=2,\qquad G=1
\]
has
\[
D^+(X)=\{2\},\qquad
G+((R-X)+(R-X))=\{1,3,5\},
\]
which are disjoint. Proposition 5 constructs
\[
A=\{1,3,4,6\}\subseteq[6],
\]
whose only repeated sum is \(7\).

Thus even the fully reflected case cannot be finished by a simple central-gap estimate.

## Self-Audit

1. **The exact duplicated-difference count is delicate around diagonals.**  
   I handled the loop separately: two off-diagonal representations produce exactly two duplicated differences, while a loop/off-diagonal pair produces exactly one. The converse map from a duplicated difference to two representations of \(s\) proves no labels have been omitted or overcounted.

2. **The \(\sqrt2\) bound relies on a uniform Sidon estimate for variable subinterval lengths.**  
   I included a self-contained Erdős–Turán/Golomb-ruler proof giving \(\sqrt M+O(M^{1/4})\) with an absolute constant. Since the two interval lengths sum to at most \(N\), the final error is uniform over \(A\) and \(s\).

3. **The crucial forbidden-ruler inequality (FR) is unproved.**  
   I do not claim that it holds. It is plausible because \(G=R+O(1)\) reproduces the known sharp construction, but the displayed finite counterexample shows that no pointwise \(G\ge R\) theorem is available. This unproved statement is the precise reason for the BLOCKED status.

## Computations To Verify

```python
from collections import Counter
from itertools import combinations

def admissible_stats(A):
    A = sorted(A)
    S = Counter()
    for i, a in enumerate(A):
        for b in A[i:]:
            S[a + b] += 1

    repeated = sorted(n for n, v in S.items() if v >= 2)

    D = Counter()
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            D[A[j] - A[i]] += 1

    out = {
        "A": tuple(A),
        "repeated_labels": repeated,
        "sum_counts": S,
        "difference_counts": D,
        "admissible": len(repeated) <= 1,
    }

    if len(repeated) == 1:
        s = repeated[0]
        t = S[s]
        delta = int(s % 2 == 0 and (s // 2) in A)
        q_observed = sum(v == 2 for v in D.values())
        q_predicted = (t - 1) * (t - delta)

        out.update({
            "s": s,
            "t": t,
            "delta": delta,
            "q_observed": q_observed,
            "q_predicted": q_predicted,
            "max_difference_multiplicity": max(D.values(), default=0),
        })

    return out


# Exact g_N(k): minimum number of repeated sum labels
# among all k-subsets of [N].
def g_N_k(N, k):
    best = None
    witnesses = []
    for A in combinations(range(1, N + 1), k):
        st = admissible_stats(A)
        value = len(st["repeated_labels"])
        if best is None or value < best:
            best = value
            witnesses = [A]
        elif value == best:
            witnesses.append(A)
    return best, witnesses


# Exact F(N), feasible only for small N.
def exact_F(N):
    for k in range(N, -1, -1):
        for A in combinations(range(1, N + 1), k):
            if admissible_stats(A)["admissible"]:
                return k, A
    return 0, ()


def is_golomb(B):
    B = sorted(B)
    diffs = [
        B[j] - B[i]
        for i in range(len(B))
        for j in range(i + 1, len(B))
    ]
    return len(diffs) == len(set(diffs))


def forbidden_ruler_ok(B, G):
    """
    B is normalized with min(B)=0, max(B)=R.
    Tests D^+(B) disjoint from G + ((R-B)+(R-B)).
    """
    B = sorted(B)
    R = B[-1]
    C = sorted(R - b for b in B)

    D = {
        B[j] - B[i]
        for i in range(len(B))
        for j in range(i + 1, len(B))
    }
    CS = {
        C[i] + C[j]
        for i in range(len(C))
        for j in range(i, len(C))
    }
    return D.isdisjoint({G + x for x in CS})


def construct_from_forbidden_ruler(B, G):
    B = sorted(B)
    R = B[-1]
    s = 2 * R + G + 2
    A = sorted(
        {1 + b for b in B}
        | {s - (1 + b) for b in B}
    )
    N = 2 * R + G + 1
    return N, s, A, admissible_stats(A)


def search_forbidden_rulers(m, Rmax):
    """
    Returns the best 2R+G found for normalized m-point Golomb rulers.
    Since G=R+1 always works, only G=1,...,R+1 need be checked.
    """
    best = None

    if m == 1:
        B = (0,)
        return {
            "L": 1,
            "R": 0,
            "G": 1,
            "B": B,
            "construction": construct_from_forbidden_ruler(B, 1),
        }

    for R in range(m - 1, Rmax + 1):
        for interior in combinations(range(1, R), m - 2):
            B = (0,) + interior + (R,)
            if not is_golomb(B):
                continue

            for G in range(1, R + 2):
                if forbidden_ruler_ok(B, G):
                    L = 2 * R + G
                    if best is None or L < best["L"]:
                        best = {
                            "L": L,
                            "ratio_L_over_m2": L / (m * m),
                            "R": R,
                            "G": G,
                            "B": B,
                            "construction":
                                construct_from_forbidden_ruler(B, G),
                        }
                    break
    return best


# Sanity checks for the proved formulas.
examples = [
    {1, 2, 3},       # exceptional sum 4, with a diagonal
    {1, 3, 4, 6},    # exceptional sum 7, no diagonal
]

for A in examples:
    st = admissible_stats(A)
    print(st)
    if st["admissible"] and len(st["repeated_labels"]) == 1:
        assert st["max_difference_multiplicity"] <= 2
        assert st["q_observed"] == st["q_predicted"]

# Test the explicit G < R counterexample.
N, s, A, st = construct_from_forbidden_ruler((0, 2), 1)
assert N == 6
assert s == 7
assert A == [1, 3, 4, 6]
assert st["admissible"]
assert st["repeated_labels"] == [7]
```

The most useful experiment is to compute
\[
L_m:=\min(2R+G)
\]
over normalized forbidden rulers of size \(m\), and plot \(L_m/m^2\). A scalable counterexample to (FR) with limiting ratio below \(3\) would disprove the conjecture already in the fully reflected class.

## Route Diagnosis

**What worked.**

- The labeled collision hypergraph has a completely rigid shape: a clique on the matching representations of the exceptional sum.
- This rigidity yields the exact duplicated-difference count
  \[
  q=(t-1)(t-\delta).
  \]
- Splitting at \(s/2\) gives two genuine Sidon subsets and the unconditional improvement
  \[
  F(N)\le\sqrt{2N}+O(N^{1/4}).
  \]
- In the fully reflected case, the second-label obstruction is exactly
  \[
  D^+(X)\cap\bigl(G+(R-X+R-X)\bigr)=\varnothing.
  \]

**What is blocked.**

- Standard hypergraph supersaturation counts collision hyperedges but not their labels. The allowed exceptional matching already supports
  \[
  \binom t2=\Theta(k^2)
  \]
  hyperedges under one label, so “many additive quadruples” does not suffice.
- Scalar additive energy has the same defect. At the conjectured construction,
  \[
  Q(A)\sim k^2/8,
  \]
  so an energy-only proof would require an extremely sharp lower bound and still would not directly control label concentration.
- Even after assuming the entire set is reflected, the route stops at (FR), which is itself the sharp asymptotic assertion for that special case.
- A simple gap estimate fails: \(G<R\) is possible even for admissible reflected examples.

**Ledger.**

- **Proved:** Lemmas 1–3, the \(\sqrt2\) upper bound, and Proposition 5.
- **Plausible but unproved:** the forbidden-ruler inequality (FR).
- **Dead ends:** total hyperedge counting, unweighted additive energy, pure label counting, and pointwise central-gap bounds.

A fresh attempt should attack (FR) directly, probably with a weighted Erdős–Turán argument that simultaneously uses the short-index differences of \(X\) and the shifted reflected sums \(G+(C+C)\). If that succeeds, the next challenge is incorporating the unpaired part \(A\setminus C_s\); ordinary exceptional-core extraction is too lossy there.