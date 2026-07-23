STATUS: BLOCKED

## Result

Route 4 yields several rigorous refinements of the first-moment method, including a stronger conditioning-on-the-first-element criterion, a general random-completion criterion from any valid prefix, and a second-order Hunter bound computable from joint zero-sum profiles. However, the route encounters a genuine dense-case obstruction: for \(A=\mathbb F_p^\times\), the expected number of forbidden intervals is exactly
\[
\frac{(p-1)(p-3)}{2(p+1)}\sim \frac p2,
\]
and choosing the first element optimally does not improve it. Moreover, the natural interval-overlap asymmetric local lemma cannot certify this known-positive family for \(p\ge13\). I also give an exact transposition identity useful for switching arguments, but no monotone switching potential is established. Thus no proof or counterexample to the original problem is obtained.

## Complete Argument

### 1. A uniform point-mass bound for subset sums

For \(0\le k\le t\) and \(x\in\mathbb F_p\), write
\[
N_k(A;x):=\#\{B\subseteq A:|B|=k,\ \sum_{b\in B}b=x\}.
\]
Thus \(N_k(A)=N_k(A;0)\).

#### Lemma 1
For \(1\le k\le t\),
\[
N_k(A;x)\le \frac1k\binom{t}{k-1}.
\]
Consequently,
\[
\frac{N_k(A;x)}{\binom tk}\le \frac1{t-k+1}.
\]
If \(1\le k\le t-1\), then also
\[
\frac{N_k(A;x)}{\binom tk}\le \frac1{k+1},
\]
and hence
\[
\frac{N_k(A;x)}{\binom tk}
\le
\min\left\{\frac1{t-k+1},\frac1{k+1}\right\}.
\]

#### Proof
Count pairs \((C,b)\) where \(C\subseteq A\), \(|C|=k-1\), \(b\in A\setminus C\), and
\[
\sum_{c\in C}c+b=x.
\]
Every \(k\)-element set \(B\) of sum \(x\) produces exactly \(k\) such pairs, by choosing which \(b\in B\) to remove. For a fixed \(C\), there is at most one possible value
\[
b=x-\sum_{c\in C}c.
\]
Therefore
\[
kN_k(A;x)\le\binom{t}{k-1}.
\]
Dividing by \(k\binom tk\) gives the first probability bound.

Let \(\sigma=\sum_{a\in A}a\). Complementation within \(A\) gives
\[
N_k(A;x)=N_{t-k}(A;\sigma-x).
\]
Applying the first bound with \(t-k\) in place of \(k\) gives
\[
\frac{N_k(A;x)}{\binom tk}\le\frac1{k+1}.
\]
∎

The first bound is sharp in order and sometimes exactly sharp. For example, if \(t\) is even and \(A\) is a union of \(t/2\) opposite pairs, then
\[
N_2(A;0)=\frac t2,\qquad
\frac{N_2(A;0)}{\binom t2}=\frac1{t-1}.
\]
Thus distinctness and nonzeroness alone do not give substantially better uniform anti-concentration even at length \(2\).

---

### 2. Conditioning on the exceptional first element

The first position can be separated exactly.

For \(a\in A\), let
\[
B_a:=A\setminus\{a\},\qquad n=t-1,
\]
and define
\[
E_a:=
\sum_{\ell=1}^{n}
(n-\ell+1)
\frac{N_\ell(B_a)}{\binom n\ell}.
\]

#### Lemma 2
If \(E_a<1\) for some \(a\in A\), then \(A\) has a valid ordering beginning with \(a\).

Moreover,
\[
\frac1t\sum_{a\in A}E_a=E(A)
=
\sum_{\ell=1}^{t-1}
(t-\ell)\frac{N_\ell(A)}{\binom t\ell}.
\]

#### Proof
Fix \(a\in A\) and take a uniformly random ordering
\[
b_1,\dots,b_n
\]
of \(B_a\). Put
\[
T_0=0,\qquad T_j=b_1+\cdots+b_j.
\]
The ordering
\[
a,b_1,\dots,b_n
\]
is valid exactly when \(T_0,T_1,\dots,T_n\) are pairwise distinct: the corresponding partial sums of \(A\) are
\[
a,\ a+T_1,\dots,a+T_n.
\]

For every interval \(b_i+\cdots+b_j\) of length \(\ell\), its underlying set is uniformly distributed over the \(\ell\)-element subsets of \(B_a\). There are \(n-\ell+1\) such intervals. Therefore the expected number of zero-sum intervals in the \(b\)-sequence is exactly \(E_a\). If \(E_a<1\), some ordering has none.

For the averaging identity, every zero-sum \(\ell\)-subset \(C\subseteq A\) is contained in \(B_a\) for exactly \(t-\ell\) choices of \(a\). Hence
\[
\sum_{a\in A}N_\ell(B_a)=(t-\ell)N_\ell(A).
\]
Since
\[
\binom{t-1}{\ell}=\frac{t-\ell}{t}\binom t\ell,
\]
the average contribution at length \(\ell\) is
\[
\frac1t\sum_{a\in A}
(t-\ell)\frac{N_\ell(B_a)}{\binom{t-1}{\ell}}
=
(t-\ell)\frac{N_\ell(A)}{\binom t\ell}.
\]
Summing over \(\ell\) proves the identity. ∎

Thus
\[
\min_{a\in A}E_a<1
\]
is a strictly stronger computable criterion than \(E(A)<1\), although their averages agree.

---

### 3. Random completion from an arbitrary valid prefix

The same idea extends to a partially constructed ordering.

Suppose
\[
a_1,\dots,a_m
\]
is a valid prefix, where \(m\ge1\). Let
\[
S_i=a_1+\cdots+a_i,\qquad
V=\{S_1,\dots,S_m\},\qquad s=S_m,
\]
and let
\[
B=A\setminus\{a_1,\dots,a_m\},\qquad n=|B|.
\]

#### Lemma 3
For \(x\in\mathbb F_p\), let
\[
N_\ell(B;x)=\#\{C\subseteq B:|C|=\ell,\ \sum C=x\}.
\]
If
\[
\begin{aligned}
R(a_1,\dots,a_m):={}&
\sum_{\ell=1}^{n}
(n-\ell+1)\frac{N_\ell(B;0)}{\binom n\ell}\\
&+
\sum_{v\in V\setminus\{s\}}\ \sum_{\ell=1}^{n}
\frac{N_\ell(B;v-s)}{\binom n\ell}
<1,
\end{aligned}
\]
then the prefix has a valid completion using all of \(B\).

#### Proof
Take a uniformly random ordering \(b_1,\dots,b_n\) of \(B\), and put
\[
T_j=b_1+\cdots+b_j,\qquad T_0=0.
\]
The future partial sums are \(s+T_j\).

A collision among \(s,s+T_1,\dots,s+T_n\) is precisely a zero-sum interval in the \(b\)-sequence. The expected number of such intervals is the first double sum.

For each old partial sum \(v\in V\setminus\{s\}\), a future collision
\[
s+T_\ell=v
\]
occurs with probability
\[
\frac{N_\ell(B;v-s)}{\binom n\ell}.
\]
The second double sum is therefore the expected number of collisions between future partial sums and earlier partial sums other than \(s\).

If the total expectation is below \(1\), there is a completion with no collision of either kind. Since the original prefix was valid, the completed ordering is valid. ∎

This is a rigorous randomized-completion theorem, but no uniform argument was found forcing \(R<1\) after a suitably chosen prefix.

---

### 4. A second-order probabilistic criterion

The first moment ignores overlap among bad events. Some of that overlap can be exploited exactly.

Let \(\mathcal I\) be the set of intervals
\[
I=[r,s]\subseteq\{1,\dots,t\},\qquad 2\le r\le s\le t,
\]
and let \(B_I\) be the event that the sum on \(I\) is zero in a uniformly random permutation of \(A\).

#### Lemma 4: Hunter bound
Let \(T\) be any spanning tree on \(\mathcal I\). Then
\[
\Pr\left(\bigcup_{I\in\mathcal I}B_I\right)
\le
\sum_{I\in\mathcal I}\Pr(B_I)
-
\sum_{\{I,J\}\in E(T)}\Pr(B_I\cap B_J).
\]
Consequently, if the right-hand side is strictly less than \(1\), then \(A\) has a valid ordering.

#### Proof
Root \(T\), and order its vertices so that every parent precedes its children. Let the events in that order be \(E_1,\dots,E_M\), and let \(p(i)<i\) be the parent of \(E_i\), except for the root.

For \(i>1\),
\[
\begin{aligned}
\Pr\left(E_i\setminus\bigcup_{j<i}E_j\right)
&=\Pr(E_i)-\Pr\left(E_i\cap\bigcup_{j<i}E_j\right)\\
&\le \Pr(E_i)-\Pr(E_i\cap E_{p(i)}).
\end{aligned}
\]
Adding these inequalities and the root contribution proves the bound. If the union has probability below \(1\), its complement is nonempty. ∎

The pair probabilities are themselves exact finite subset-counting quantities. For intervals \(I,J\), put
\[
\alpha=|I\setminus J|,\qquad
\beta=|I\cap J|,\qquad
\gamma=|J\setminus I|.
\]
Let \(M_{\alpha,\beta,\gamma}(A)\) count ordered triples \((X,Y,Z)\) of pairwise disjoint subsets of \(A\) such that
\[
|X|=\alpha,\quad |Y|=\beta,\quad |Z|=\gamma,
\]
and
\[
\sum X+\sum Y=0,\qquad
\sum Y+\sum Z=0.
\]
Then
\[
\Pr(B_I\cap B_J)
=
\frac{M_{\alpha,\beta,\gamma}(A)}
{\binom t\alpha
 \binom{t-\alpha}{\beta}
 \binom{t-\alpha-\beta}{\gamma}}.
\]
Indeed, the sets of values occupying the three disjoint position regions
\[
I\setminus J,\quad I\cap J,\quad J\setminus I
\]
are uniformly distributed over all ordered disjoint triples of the prescribed sizes.

Thus the optimal Hunter certificate is obtained by taking a maximum-weight spanning tree, with edge weight \(\Pr(B_I\cap B_J)\). This is stronger than the first moment and is exactly computable for a fixed \(A\), but no universal bound making it less than \(1\) was found.

---

### 5. Exact stress test: \(A=\mathbb F_p^\times\)

Let \(p\) be odd and put
\[
A=\mathbb F_p^\times,\qquad n=p-1.
\]

#### Lemma 5
For \(0\le \ell\le n\),
\[
N_\ell(A)
=
\frac1p\left(\binom n\ell+n(-1)^\ell\right).
\]
Consequently,
\[
E(\mathbb F_p^\times)
=
\frac{(p-1)(p-3)}{2(p+1)}.
\]

#### Proof
Let \(\zeta=e^{2\pi i/p}\). Additive-character orthogonality gives
\[
N_\ell(A)
=
\frac1p\sum_{u\in\mathbb F_p}
[y^\ell]\prod_{a\in\mathbb F_p^\times}(1+y\zeta^{ua}).
\]
The \(u=0\) term is \(\binom n\ell\).

For \(u\ne0\), multiplication by \(u\) permutes \(\mathbb F_p^\times\), so all nonzero \(u\) give the same polynomial. Since \(p\) is odd,
\[
\prod_{a\in\mathbb F_p}(1+y\zeta^a)=1+y^p.
\]
Removing the factor corresponding to \(a=0\) gives
\[
\prod_{a\in\mathbb F_p^\times}(1+y\zeta^a)
=
\frac{1+y^p}{1+y}
=
\sum_{\ell=0}^{p-1}(-1)^\ell y^\ell.
\]
There are \(p-1=n\) nonzero characters, proving the formula for \(N_\ell(A)\).

Set
\[
q_\ell=\frac{N_\ell(A)}{\binom n\ell}
=
\frac1{n+1}
+
\frac n{n+1}\frac{(-1)^\ell}{\binom n\ell}.
\]
Therefore
\[
E(A)=\sum_{\ell=1}^{n-1}(n-\ell)q_\ell.
\]

We use the reciprocal-binomial identity
\[
\sum_{\ell=0}^{n}\frac{(-1)^\ell}{\binom n\ell}
=
\frac{n+1}{n+2}\bigl(1+(-1)^n\bigr).
\]
For completeness,
\[
\frac1{\binom n\ell}
=
(n+1)\int_0^1x^\ell(1-x)^{n-\ell}\,dx,
\]
and summing the finite geometric series under the integral proves the identity.

Since \(n\) is even,
\[
\sum_{\ell=1}^{n-1}\frac{(-1)^\ell}{\binom n\ell}
=
-\frac2{n+2}.
\]
Also, by pairing \(\ell\) with \(n-\ell\),
\[
\sum_{\ell=1}^{n-1}
(n-\ell)\frac{(-1)^\ell}{\binom n\ell}
=
-\frac n{n+2}.
\]
Hence
\[
\begin{aligned}
E(A)
&=
\frac1{n+1}\frac{n(n-1)}2
-\frac{n^2}{(n+1)(n+2)}\\
&=\frac{n(n-2)}{2(n+2)}
=\frac{(p-1)(p-3)}{2(p+1)}.
\end{aligned}
\]
∎

This is already greater than \(1\) for every \(p\ge7\), and it grows like \(p/2\), despite the known existence of valid orderings for \(\mathbb F_p^\times\).

Furthermore, all conditional expectations \(E_a\) from Lemma 2 are equal in this example. Indeed, multiplication by \(b/a\) maps
\[
\mathbb F_p^\times\setminus\{a\}
\quad\text{to}\quad
\mathbb F_p^\times\setminus\{b\}
\]
and preserves zero-sum subset counts. Since their average is \(E(A)\),
\[
E_a=\frac{(p-1)(p-3)}{2(p+1)}
\]
for every \(a\). Thus optimizing the first element does not repair the first-moment failure.

---

### 6. Failure of the natural interval-overlap local lemma

This does not rule out every possible lopsided or resampling argument, but it rules out the most direct asymmetric local lemma on aggregate interval events.

The standard asymmetric local lemma criterion asks for numbers \(x_I\in[0,1)\) such that
\[
\Pr(B_I)
\le
x_I\prod_{J\in\Gamma(I)}(1-x_J).
\]

#### Lemma 6
If a clique \(\mathcal C\) is contained in the dependency graph, then the asymmetric criterion implies
\[
\sum_{I\in\mathcal C}\Pr(B_I)\le1.
\]

#### Proof
For \(I\in\mathcal C\),
\[
\Pr(B_I)
\le
x_I\prod_{\substack{J\in\mathcal C\\J\ne I}}(1-x_J).
\]
Put \(y_I=x_I/(1-x_I)\). Summing gives
\[
\sum_{I\in\mathcal C}\Pr(B_I)
\le
\left(\prod_{J\in\mathcal C}(1-x_J)\right)
\sum_{I\in\mathcal C}\frac{x_I}{1-x_I}
=
\frac{\sum_Iy_I}{\prod_I(1+y_I)}
\le1.
\]
The last inequality follows from
\[
\prod_I(1+y_I)\ge\sum_Iy_I.
\]
∎

Now take \(A=\mathbb F_p^\times\), \(n=p-1\), and \(k=n/2\). Consider all allowed intervals containing position \(k\):
\[
\mathcal C=\{[r,s]:2\le r\le k\le s\le n\}.
\]
These intervals form a clique in the natural overlap graph.

There are
\[
(k-1)(k+1)=k^2-1
\]
such intervals. One has length \(1\), and one, namely \([2,n]\), has length \(n-1\); both have zero probability of summing to zero. Every remaining interval has length \(2\le\ell\le n-2\).

From Lemma 5,
\[
q_\ell
\ge
\frac1{n+1}-\frac{n}{(n+1)\binom n\ell}
\ge
\frac1{2(n+1)}
\]
for \(n\ge5\). Therefore
\[
\sum_{I\in\mathcal C}\Pr(B_I)
\ge
\frac{k^2-3}{2(n+1)}.
\]
For \(n\ge12\), this is greater than \(1\). Hence, for every prime \(p\ge13\), the asymmetric local lemma criterion cannot hold on any dependency graph retaining this natural clique.

There are two important qualifications:

1. For random permutations, disjoint interval events are still globally dependent, so the naive overlap graph is not itself automatically a valid dependency graph.
2. A finer decomposition into canonical partial assignments may have a different lopsided graph.

Thus this is a rigorous obstruction to the standard aggregate-event LLL, not to every conceivable local-lemma method.

---

### 7. Exact switching identity for transpositions

For an ordering \(a_1,\dots,a_t\), let
\[
S_i=\sum_{h=1}^ia_h
\]
and define the collision count
\[
X(a_1,\dots,a_t)
=
\#\{(u,v):1\le u<v\le t,\ S_u=S_v\}.
\]
Thus the ordering is valid exactly when \(X=0\).

#### Lemma 7
Swap \(a_i\) and \(a_j\), where \(i<j\), and put
\[
d=a_j-a_i\ne0.
\]
Then the new partial sums are
\[
S'_k=
\begin{cases}
S_k,&k<i,\\
S_k+d,&i\le k<j,\\
S_k,&k\ge j.
\end{cases}
\]
Consequently, all collisions whose two indices both lie in
\[
K=\{i,\dots,j-1\}
\]
or both lie outside \(K\) are unchanged. Only cross-collisions between \(K\) and its complement can change.

#### Proof
Before position \(i\), the prefix is unchanged. Between \(i\) and \(j-1\), the prefix contains \(a_j\) instead of \(a_i\), changing its sum by \(d\). From position \(j\) onward, both \(a_i\) and \(a_j\) have been included, so the prefix sum is again unchanged. The collision statement follows immediately. ∎

This reduces a transposition switching to translating one contiguous block of partial-sum vertices by an allowed difference \(a_j-a_i\). A proof that every nonvalid ordering admits a collision-decreasing transposition would solve the problem by descent, but I did not prove this statement and it should be tested aggressively for small counterexamples.

A simpler attempt to improve the first moment by proving that every invalid permutation has many bad intervals is impossible.

#### Lemma 8
For every \(t\ge3\), there are a prime \(p\), a set \(A\subseteq\mathbb F_p^\times\) of size \(t\), and an ordering of \(A\) having exactly one forbidden zero-sum interval.

#### Proof
Choose a prime
\[
p>2^{t-1}
\]
and consider the integer sequence
\[
2,\ 1,\ -1,\ 4,\ 8,\dots,2^{t-2},
\]
reduced modulo \(p\).

All entries are distinct nonzero residues. Among intervals starting at position at least \(2\):

- intervals beginning at position \(4\) or later have positive integer sum;
- an interval beginning with \(-1\) has sum \(-1\) if it has length \(1\), and positive sum if it includes \(4\);
- an interval beginning with \(1\) has sum \(1\), \(0\), or a positive sum according as it ends at position \(2\), \(3\), or later.

Thus the unique zero-sum interval is the block \(1,-1\) in positions \(2,3\). All nonzero integer interval sums have absolute value less than \(p\), so reduction modulo \(p\) introduces no additional zero sums. ∎

Therefore no replacement of the union-bound threshold \(1\) by a universal multiplicity \(K>1\) is possible.

---

### 8. A useful zero-sum circular observation

Although it does not remove the block, the random-permutation formulation becomes cleaner for zero-total sets.

#### Lemma 9
If \(\sum_{a\in A}a=0\), validity is invariant under cyclic rotations of an ordering.

If \(\sigma=\sum_{a\in A}a\), \(x=-\sigma\ne0\), and \(x\notin A\), then any valid ordering of the zero-sum set
\[
A\cup\{x\}
\]
yields a valid ordering of \(A\).

#### Proof
For a zero-sum ordering \(a_1,\dots,a_t\), validity is equivalent to
\[
S_0,S_1,\dots,S_{t-1}
\]
being pairwise distinct, because \(S_t=S_0=0\). Under cyclic rotation, these circular vertices are merely translated by the negative of the new starting vertex, so distinctness is preserved.

For the second assertion, cyclically rotate a valid ordering of \(A\cup\{x\}\) so that it begins with \(x\):
\[
x,a_1,\dots,a_t.
\]
Its partial sums
\[
x,\ x+a_1,\dots,x+a_1+\cdots+a_t=0
\]
are distinct. Subtracting \(x\) from the last \(t\) of these shows that
\[
a_1,\ a_1+a_2,\dots,a_1+\cdots+a_t
\]
are distinct. Hence \(a_1,\dots,a_t\) is valid for \(A\). ∎

This suggests that zero-sum circular orderings plus an endpoint-flexibility theorem might be a useful alternative, but no such flexibility theorem is proved here.

## Self-Audit

1. **The local-lemma obstruction has deliberately limited scope.**  
   It rules out the natural aggregate interval-overlap asymmetric criterion, not canonical-event LLLs, cluster expansion, resampling or a specially proved lopsided graph omitting some overlap edges. The stated obstruction itself is sound because it follows from an explicit clique whose event probabilities sum to more than \(1\).

2. **The Hunter criterion is exact but may have little universal force.**  
   It incorporates only a spanning tree’s worth of pairwise intersections; in dense examples, higher-order overlap is probably essential. I believe the criterion and pair-intersection formula are correct because both follow from direct finite probability decompositions, but I make no claim that they settle any unresolved size range.

3. **No monotone switching theorem was obtained.**  
   Lemma 7 precisely describes transpositions, but the crucial assertion that some swap decreases the collision count remains unproved and may be false. I have not used it as a lemma. The supplied computation below is intended to search for local minima before any fresh proof attempt relies on it.

## Computations To Verify

The following exact Python checks the subset profiles, conditional expectations, full-set formula, valid-ordering fractions, Hunter bounds, and transposition local minima.

```python
from itertools import combinations, permutations
from fractions import Fraction
from math import comb, factorial

def zero_profile(A, p):
    """N[k] = number of k-subsets of A with sum 0 mod p."""
    A = list(A)
    t = len(A)
    D = [[0] * p for _ in range(t + 1)]
    D[0][0] = 1
    used = 0
    for a in A:
        for k in range(used, -1, -1):
            for r in range(p):
                c = D[k][r]
                if c:
                    D[k + 1][(r + a) % p] += c
        used += 1
    return [D[k][0] for k in range(t + 1)]

def first_moment_E(A, p):
    A = tuple(A)
    t = len(A)
    N = zero_profile(A, p)
    return sum(
        (Fraction((t - l) * N[l], comb(t, l))
         for l in range(1, t)),
        Fraction(0)
    )

def conditional_Es(A, p):
    """E_a for every possible first element a."""
    A = tuple(A)
    out = {}
    for a in A:
        B = tuple(x for x in A if x != a)
        n = len(B)
        N = zero_profile(B, p)
        out[a] = sum(
            (Fraction((n - l + 1) * N[l], comb(n, l))
             for l in range(1, n + 1)),
            Fraction(0)
        )
    return out

def partial_sums(perm, p):
    s = 0
    out = []
    for a in perm:
        s = (s + a) % p
        out.append(s)
    return out

def valid(perm, p):
    S = partial_sums(perm, p)
    return len(S) == len(set(S))  # Do not insert S_0=0.

def bad_intervals(perm, p):
    """Zero-sum intervals [r,s] with zero-based r >= 1."""
    t = len(perm)
    out = []
    for r in range(1, t):
        ssum = 0
        for s in range(r, t):
            ssum = (ssum + perm[s]) % p
            if ssum == 0:
                out.append((r, s))
    return out

def collision_count(perm, p):
    S = partial_sums(perm, p)
    counts = {}
    x = 0
    for s in S:
        x += counts.get(s, 0)
        counts[s] = counts.get(s, 0) + 1
    return x

def verify_average_identity(A, p):
    E = first_moment_E(A, p)
    Es = conditional_Es(A, p)
    avg = sum(Es.values(), Fraction(0)) / len(A) if A else Fraction(0)
    return E, avg, E == avg

def full_set_formula(p):
    A = tuple(range(1, p))
    measured = first_moment_E(A, p)
    formula = Fraction((p - 1) * (p - 3), 2 * (p + 1))
    return measured, formula, measured == formula

for p in [3, 5, 7, 11, 13, 17, 19]:
    print("full set", p, full_set_formula(p))
```

Exact brute-force valid fraction:

```python
def exact_valid_fraction(A, p):
    A = tuple(A)
    good = 0
    total = factorial(len(A))
    distribution = {}
    for perm in permutations(A):
        x = collision_count(perm, p)
        distribution[x] = distribution.get(x, 0) + 1
        if x == 0:
            good += 1
    return Fraction(good, total), distribution

# Small examples only:
# print(exact_valid_fraction(range(1, 7), 7))
```

Exact Hunter bound using a maximum-weight spanning tree:

```python
def hunter_bound_bruteforce(A, p):
    A = tuple(A)
    t = len(A)
    N = zero_profile(A, p)

    events = []
    for r in range(1, t):           # zero-based r>=1 means position >=2
        for s in range(r, t):
            l = s - r + 1
            if N[l] > 0:
                events.append((r, s))

    m = len(events)
    if m == 0:
        return Fraction(0), Fraction(1)

    event_count = [0] * m
    pair_count = [[0] * m for _ in range(m)]
    good = 0
    den = factorial(t)

    for perm in permutations(A):
        hits = []
        for r, s in events:
            hits.append(sum(perm[r:s+1]) % p == 0)

        if not any(hits):
            good += 1

        inds = [i for i, h in enumerate(hits) if h]
        for i in inds:
            event_count[i] += 1
        for u in range(len(inds)):
            for v in range(u + 1, len(inds)):
                i, j = inds[u], inds[v]
                pair_count[i][j] += 1
                pair_count[j][i] += 1

    # Maximum spanning tree in the complete graph.
    used = {0}
    mst_weight = 0
    while len(used) < m:
        best = None
        for i in used:
            for j in range(m):
                if j not in used:
                    candidate = (pair_count[i][j], i, j)
                    if best is None or candidate > best:
                        best = candidate
        w, i, j = best
        mst_weight += w
        used.add(j)

    hunter = Fraction(sum(event_count) - mst_weight, den)
    actual_good = Fraction(good, den)
    assert actual_good >= 1 - hunter
    return hunter, actual_good

# Suitable only for t roughly <= 9:
# print(hunter_bound_bruteforce(range(1, 7), 7))
```

Check the LLL clique obstruction exactly:

```python
def central_clique_sum_full_set(p):
    n = p - 1
    assert n % 2 == 0
    A = tuple(range(1, p))
    N = zero_profile(A, p)
    k = n // 2  # one-based central position

    total = Fraction(0)
    intervals = []
    for r in range(2, k + 1):
        for s in range(k, n + 1):
            l = s - r + 1
            q = Fraction(N[l], comb(n, l))
            total += q
            intervals.append((r, s, l, q))
    return total, intervals

for p in [7, 11, 13, 17, 19]:
    total, _ = central_clique_sum_full_set(p)
    print("clique", p, total, float(total))
```

Search for collision-count local minima under all transpositions:

```python
def swap_positions(perm, i, j):
    q = list(perm)
    q[i], q[j] = q[j], q[i]
    return tuple(q)

def is_transposition_local_minimum(perm, p):
    x = collision_count(perm, p)
    if x == 0:
        return False
    t = len(perm)
    for i in range(t):
        for j in range(i + 1, t):
            if collision_count(swap_positions(perm, i, j), p) < x:
                return False
    return True

def find_local_minima(A, p, limit=None):
    found = []
    for perm in permutations(tuple(A)):
        if is_transposition_local_minimum(perm, p):
            found.append((perm, collision_count(perm, p)))
            if limit is not None and len(found) >= limit:
                break
    return found

# Critical test before pursuing a transposition-descent proof:
# for p in [5, 7, 11]:
#     A = tuple(range(1, p))
#     print(p, find_local_minima(A, p, limit=5))
```

Verify Lemma 8’s unique-bad-interval construction:

```python
def unique_bad_construction(t, p):
    assert t >= 3 and p > 2**(t - 1)
    seq = [2, 1, p - 1]  # -1 mod p
    seq.extend(pow(2, i - 2, p) for i in range(4, t + 1))
    assert len(seq) == t
    assert len(set(seq)) == t
    bad = bad_intervals(seq, p)
    return tuple(seq), bad

# Example with a suitable prime:
# print(unique_bad_construction(6, 67))
# Expected bad interval: [(1, 2)] in zero-based indexing.
```

For a broader empirical study, enumerate subset orbits under scaling, compute \(E(A)\), \(\min_aE_a\), the exact valid fraction for manageable \(t\), and search for transposition local minima. The most important possible falsification is a small invalid ordering that is locally minimal under every transposition.

## Route Diagnosis

### Proved ledger

1. Uniform fixed-cardinality subset-sum point-mass bounds.
2. The exact first-element-conditioned criterion \(E_a<1\).
3. The averaging identity
   \[
   \frac1t\sum_aE_a=E(A).
   \]
4. A random-completion criterion from any valid prefix.
5. An exact second-order Hunter certificate and exact pair-event formulas.
6. The full-set identity
   \[
   E(\mathbb F_p^\times)=\frac{(p-1)(p-3)}{2(p+1)}.
   \]
7. Failure of first-element optimization for \(\mathbb F_p^\times\).
8. Failure of the natural aggregate interval-overlap asymmetric LLL for \(p\ge13\).
9. The exact effect of a transposition on partial sums.
10. Existence of invalid permutations with exactly one bad interval.
11. Cyclic-rotation invariance for zero-sum sets and the balancing-element reduction.

### Plausible but unproved

- A canonical-event permutation LLL might exploit finer incompatibility structure than the aggregate interval graph.
- A weighted switching potential more sophisticated than the raw collision count might admit descent.
- Zero-sum circular orderings with endpoint flexibility might reduce most nonzero-total cases.
- Hunter certificates may settle many finite instances even when \(E(A)\ge1\), but no universal estimate is known.

### Dead ends

- **Plain first moment:** fails by a factor of order \(p\) on \(\mathbb F_p^\times\).
- **Optimizing the first element:** gives exactly the same value on \(\mathbb F_p^\times\).
- **Uniform point-mass estimates alone:** sharp examples with opposite pairs prevent enough improvement.
- **Natural aggregate-event LLL:** blocked by a clique whose probabilities sum to more than \(1\).
- **Replacing the threshold \(1\) by bad-event multiplicity:** impossible because an invalid permutation may have exactly one bad interval.

### Precise block

A successful Route 4 proof now requires a genuinely global switching or high-order dependency theorem capable of proving that a family of \(\Theta(t^2)\) interval events does not cover all permutations even when their expected count is \(\Theta(t)\). The zero-sum profile \(N_\ell(A)\) and ordinary interval overlap do not provide enough information. Establishing such a theorem uniformly for adversarial \(A\) appears comparable in strength to the original valid-ordering problem, so this route is presently blocked.

A fresh attempt should first run the transposition-local-minimum search above. If local minima occur at small \(t\), raw exchange descent should be abandoned. The most promising remaining probabilistic direction is a canonical-assignment or cluster-expansion analysis for random permutations, tested first on \(A=\mathbb F_p^\times\) and on sets maximizing \(E(A)\); otherwise the problem likely needs a structural/absorption argument rather than a purely probabilistic one.