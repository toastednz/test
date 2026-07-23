STATUS: BLOCKED

## Result

I did not solve Erdős Problem #156. Pursuing direct covering Golomb rulers led to three rigorous conclusions. First, a route-1 construction must produce a consecutive component of the blocker set containing the entire ruler, not merely \(\Theta(k^3)\) distinct blockers; I give a precise interpolation theorem sufficient for all \(N\). Second, any construction whose Sidonicity is certified after reduction modulo a modulus \(m\ll k^3\) cannot work: its blocker set contains only the original point in each selected residue class, so it has no blocked interval of length \(2m\). This rules out the most natural finite-field lift and no-carry digit constructions. Third, I construct explicit \(B_3\)-rulers with \(\frac12k^3+O(k^2)\) distinct triple blockers but longest blocked interval only \(O(k^2)\), showing that near-optimal blocker cardinality alone gives no useful interval coverage. A second natural stretched quadratic ruler is also proved to have longest blocked interval \(O(k^2)\). The remaining block is exactly the hard design problem: construct a carry-rich Sidon ruler whose blocker set has a cubic-length consecutive component containing the ruler.

## Complete Argument

Write
\[
\mathcal B(A):=(A+A-A)\cup\operatorname{Mid}(A).
\]
It is convenient to work in arbitrary integer intervals; translation returns everything to \([N]\).

### 1. What a route-1 construction actually has to provide

#### Lemma 1: Geometric range of the blocker set

Let \(A\subset\mathbb Z\) be nonempty, with
\[
u=\min A,\qquad v=\max A,\qquad h=v-u+1.
\]
Then
\[
\mathcal B(A)\subseteq[2u-v,\,2v-u].
\]
Consequently, every consecutive interval contained in \(\mathcal B(A)\) has length at most
\[
3h-2.
\]

**Proof.**
For \(a,b,c\in A\),
\[
2u-v\le b+c-a\le 2v-u.
\]
Every midpoint of two elements of \(A\) lies in \([u,v]\), which is contained in the same larger interval. Its number of integers is
\[
(2v-u)-(2u-v)+1=3(v-u)+1=3h-2.
\]
∎

Thus if a \(k\)-element ruler blocks an interval of length \(ck^3\), its own hull automatically has length at least \((c/3)k^3+O(1)\). Cubic interval coverage necessarily requires a genuinely cubic-span ruler.

#### Lemma 2: Trimming a blocked interval

Suppose \(A\) is Sidon and
\[
A\subseteq I\subseteq\mathcal B(A)
\]
for some consecutive integer interval \(I\). Let \(H=[\min A,\max A]\), with \(|H|=h\), and let \(|I|=L\). Then for every integer \(n\) with
\[
h\le n\le L
\]
there is a consecutive interval \(J\) such that
\[
A\subseteq J\subseteq I,\qquad |J|=n.
\]
After translating \(J\) to \([n]\), the translated copy of \(A\) is a maximal Sidon subset of \([n]\).

**Proof.**
Write
\[
I=[u-\ell,v+r],\qquad H=[u,v],
\]
where \(\ell,r\ge0\). Thus \(L=h+\ell+r\).

For \(n=h+s\), where \(0\le s\le\ell+r\), choose nonnegative \(\ell'\le\ell\) and \(r'\le r\) with \(\ell'+r'=s\); for example,
\[
\ell'=\max(0,s-r),\qquad r'=s-\ell'.
\]
Then
\[
J=[u-\ell',v+r']
\]
has the required properties. Since \(J\subseteq\mathcal B(A)\), every point of \(J\) is blocked by \(A\). The exact maximality criterion therefore says that \(A\) is maximal Sidon in \(J\). Translation preserves Sidonicity and all blocker equations. ∎

This corrects an insufficiency in the route-1 key lemma as stated in the brief: it is not enough that \(A_k\subseteq[Ck^3]\) while some possibly smaller interval is blocked. The blocked interval must contain the whole ruler.

#### Proposition 3: A sufficient uniform interpolation theorem

Suppose there are constants \(c>d>0\) such that, for every sufficiently large \(k\), there are:

- a \(k\)-element Sidon set \(A_k\);
- a consecutive interval \(I_k\) with
  \[
  A_k\subseteq I_k\subseteq\mathcal B(A_k);
  \]
- bounds
  \[
  |I_k|\ge ck^3,\qquad
  \max A_k-\min A_k+1\le dk^3.
  \]

Then
\[
\sigma(N)=O(N^{1/3})
\]
uniformly for every sufficiently large \(N\).

**Proof.**
Let \(h_k\) be the hull length and \(L_k=|I_k|\). By Lemma 2, every integer length in \([h_k,L_k]\) is attainable by a maximal Sidon set of size \(k\).

Since \(d<c\), for all sufficiently large \(k\),
\[
h_{k+1}\le d(k+1)^3\le ck^3\le L_k.
\]
Thus the intervals of attainable lengths \([h_k,L_k]\) overlap successively and cover all sufficiently large integers.

If \(N\in[h_k,L_k]\), Lemma 1 gives
\[
ck^3\le L_k\le 3h_k-2\le 3N.
\]
Hence
\[
k\le (3N/c)^{1/3}.
\]
The translated set supplied by Lemma 2 is maximal Sidon in \([N]\), proving the required uniform bound. ∎

The unproved part is the existence of such \(A_k,I_k\). Proposition 3 is a transfer theorem, not the missing construction.

---

### 2. A modular obstruction to natural stretched constructions

The most tempting route-1 architecture is to place one point in each residue class of a modular Sidon set and use higher digits to stretch the span from \(k^2\) to \(k^3\). This cannot work.

#### Lemma 4: Selected fibers are completely unblocked

Let \(m\ge1\), and let \(\pi:\mathbb Z\to\mathbb Z/m\mathbb Z\) be reduction modulo \(m\). Suppose:

1. \(\pi\) is injective on \(A\);
2. \(\pi(A)\) is an ordinary Sidon set in \(\mathbb Z/m\mathbb Z\), including repeated summands.

Then
\[
\mathcal B(A)\cap\pi^{-1}(\pi(A))=A.
\]

**Proof.**
The inclusion \(A\subseteq\mathcal B(A)\cap\pi^{-1}(\pi(A))\) is immediate.

Conversely, let \(y\in\mathcal B(A)\) and suppose
\[
\pi(y)=\pi(x)
\]
for some \(x\in A\).

First suppose \(y=b+c-a\) for \(a,b,c\in A\). Modulo \(m\),
\[
\pi(b)+\pi(c)=\pi(a)+\pi(x).
\]
Since \(\pi(A)\) is Sidon,
\[
\{\pi(b),\pi(c)\}=\{\pi(a),\pi(x)\}
\]
as multisets. Injectivity of \(\pi\) on \(A\) implies
\[
\{b,c\}=\{a,x\}.
\]
Therefore \(b+c-a=x\), so \(y=x\in A\).

Now suppose \(2y=b+c\) for \(b,c\in A\). Reducing modulo \(m\),
\[
\pi(b)+\pi(c)=2\pi(x).
\]
Sidonicity forces
\[
\{\pi(b),\pi(c)\}=\{\pi(x),\pi(x)\}.
\]
Injectivity gives \(b=c=x\), and the integer equality \(2y=2x\) gives \(y=x\).

Thus no point outside \(A\) lying in a selected residue class is blocked. ∎

#### Corollary 5: No long blocked interval under a small Sidon projection

Under the hypotheses of Lemma 4, \(\mathcal B(A)\) contains no consecutive interval of length \(2m\). In particular, \(A\) cannot be maximal Sidon in any interval of length at least \(2m\).

**Proof.**
Every interval of \(2m\) consecutive integers contains exactly two representatives of each residue class modulo \(m\). Choose any residue in the nonempty set \(\pi(A)\). By Lemma 4, at most one integer in that entire residue class belongs to \(\mathcal B(A)\), namely the corresponding member of \(A\). Hence the interval cannot be contained in \(\mathcal B(A)\). ∎

Consequently, if \(A\) is maximal in an interval of length \(N\), then for every \(m\le N/2\), either reduction modulo \(m\) is not injective on \(A\), or the reduced set is not modular Sidon. Any successful cubic construction must therefore create abundant modular pair-sum collisions at every relevant lower scale, while retaining exact integer Sidonicity. Standard no-carry finite-field lifts have precisely the opposite property.

---

### 3. Collision-free blockers do not imply interval coverage

A natural idea is to strengthen Sidonicity to the \(B_3\) property, thereby eliminating almost all collisions in \(A+A-A\).

Call \(A\) a \(B_3\)-set if all unordered sums of three elements, with repetitions allowed, are distinct.

#### Lemma 6: Exact blocker cardinality for \(B_3\)-sets

If \(A\) is a \(B_3\)-set of size \(k\), then
\[
|A+A-A|=\frac{k^3-k^2+2k}{2}.
\]

Moreover, every point of \((A+A-A)\setminus A\) has exactly one representation
\[
b+c-a
\]
when \(\{b,c\}\) is treated as unordered.

**Proof.**
A \(B_3\)-set is Sidon: from \(a+b=c+d\), adding any fixed \(e\in A\) gives equality of two three-element sums, and cancellation of one copy of \(e\) yields
\[
\{a,b\}=\{c,d\}.
\]

Consider the domain
\[
\mathcal D=\{(a,\{b,c\}):a,b,c\in A\}.
\]
It has size
\[
|\mathcal D|=k\binom{k+1}{2}=\frac{k^2(k+1)}2.
\]

For each fixed \(x\in A\), the equation
\[
b+c-a=x
\]
is equivalent to
\[
b+c=x+a.
\]
By Sidonicity, the unique unordered pair is \(\{b,c\}=\{x,a\}\). Thus exactly \(k\) members of \(\mathcal D\) map to \(x\), one for each \(a\in A\). Altogether, exactly \(k^2\) domain points map into \(A\).

Suppose two domain points have the same image:
\[
b+c-a=b'+c'-a'.
\]
Then
\[
b+c+a'=b'+c'+a.
\]
The \(B_3\) property gives
\[
\{b,c,a'\}=\{b',c',a\}
\]
as multisets. If \(a=a'\), Sidonicity gives \(\{b,c\}=\{b',c'\}\), so the domain points coincide. If \(a\ne a'\), the multiset identity forces \(a\) to occur among \(b,c\); cancelling that occurrence shows that the common value \(b+c-a\) is an element of \(A\). Hence every value outside \(A\) has a unique domain preimage.

There are therefore
\[
|\mathcal D|-k^2=\frac{k^3-k^2}{2}
\]
distinct outputs outside \(A\), together with the \(k\) outputs in \(A\). This gives
\[
|A+A-A|
=\frac{k^3-k^2}{2}+k
=\frac{k^3-k^2+2k}{2}.
\]
∎

Thus \(B_3\)-sets use the nominal \(\frac12k^3\) blocker capacity essentially perfectly. Nevertheless, they can have no long blocked interval.

#### Proposition 7: Explicit cubic-span \(B_3\)-rulers with only quadratic blocked runs

Let \(p\ge5\) be prime and put \(B=3p\). For \(t\in\{0,\dots,p-1\}\), let
\[
r_2(t)\in\{0,\dots,p-1\},\qquad
r_3(t)\in\{0,\dots,p-1\}
\]
be the least residues of \(t^2,t^3\pmod p\). Define
\[
a_t=t+B r_2(t)+B^2r_3(t),
\qquad
A_p=\{a_t:0\le t<p\}.
\]

Then:

1. \(A_p\) is a \(B_3\)-set of size \(p\) and span \(O(p^3)\);
2. 
   \[
   |A_p+A_p-A_p|=\frac{p^3-p^2+2p}{2};
   \]
3. \(\mathcal B(A_p)\) contains no consecutive interval of length \(2B^2=18p^2\).

**Proof.**

For the \(B_3\) property, suppose
\[
a_x+a_y+a_z=a_u+a_v+a_w.
\]
Every base-\(B\) digit lies in \([0,p-1]\), and a sum of three such digits is at most
\[
3p-3<B.
\]
Thus there are no carries. Uniqueness of base-\(B\) expansion gives equality of the sums of the corresponding first, second and third digits. Reducing these equalities modulo \(p\), the two triples have the same first three power sums
\[
P_1=\sum t,\qquad P_2=\sum t^2,\qquad P_3=\sum t^3
\]
in \(\mathbb F_p\).

Because \(p>3\), Newton's identities recover the elementary symmetric functions:
\[
e_1=P_1,\qquad
e_2=\frac{P_1^2-P_2}{2},\qquad
e_3=\frac{P_3-e_1P_2+e_2P_1}{3}.
\]
Therefore the two triples are the roots, with multiplicity, of the same monic cubic
\[
X^3-e_1X^2+e_2X-e_3.
\]
They are equal as multisets. Hence \(A_p\) is \(B_3\). Its largest element is less than
\[
p+Bp+B^2p=O(p^3).
\]

The cardinality formula follows from Lemma 6.

It remains to rule out long blocked intervals. Reduce modulo
\[
m=B^2=9p^2.
\]
The reduced set is
\[
D=\{t+B r_2(t):0\le t<p\}.
\]
This reduction is injective.

We claim \(D\) is modular Sidon. Every pair sum of representatives is less than
\[
2(p-1)(B+1)<B^2,
\]
so a congruence of pair sums modulo \(B^2\) is an integer equality. There are no base-\(B\) carries in pair sums because \(2p-2<B\). Equality therefore gives equal first and second power sums modulo \(p\). Since \(p\) is odd, these determine
\[
xy=\frac{(x+y)^2-(x^2+y^2)}2,
\]
and hence determine the unordered pair \(\{x,y\}\). Thus \(D\) is modular Sidon.

Lemma 4 and Corollary 5 now apply, proving that \(\mathcal B(A_p)\) contains no interval of length \(2B^2=18p^2\). ∎

This is a sharp warning for Route 1: these rulers have \(\Theta(p^3)\) distinct blockers and cubic span, yet their longest consecutive blocked interval is \(O(p^2)\).

---

### 4. A natural stretched quadratic ruler also fails

The preceding example failed because a low modulus already certified Sidonicity. One can avoid that architecture, but simple scale separation still produces holes.

#### Proposition 8: A stretched quadratic family has only quadratic blocked runs

For \(k\ge2\), put
\[
Q=20k^2,\qquad
A_k=\{Qi+i^2:0\le i<k\}.
\]
Then \(A_k\) is Sidon, has span \(\Theta(k^3)\), but every consecutive interval contained in \(\mathcal B(A_k)\) has length at most
\[
3\binom{k+1}{2}+1=O(k^2).
\]

**Proof.**

For \(j>i\),
\[
(Qj+j^2)-(Qi+i^2)
=Q(j-i)+(j-i)(i+j).
\]
Let \(d=j-i\). The error term satisfies
\[
0<d(i+j)<2k^2<Q.
\]
If two positive differences are equal, their coefficients of \(Q\) must therefore agree, so their \(d\)'s agree. The remaining equality then gives equality of \(i+j\); together with \(j-i\), this determines \(i,j\). Hence all positive differences are distinct, and \(A_k\) is Sidon.

Consider a triple blocker
\[
x=(Qj+j^2)+(Q\ell+\ell^2)-(Qi+i^2).
\]
Set
\[
t=j+\ell-i,\qquad p=j-i,\qquad q=\ell-i.
\]
Then
\[
j^2+\ell^2-i^2=t^2-2pq,
\]
so
\[
x=Qt+t^2-2pq.
\]
Here
\[
-(k-1)\le t\le2(k-1),\qquad |p|,|q|\le k-1.
\]
Writing \(s=(k-1)^2\), every triple value with parameter \(t\) therefore lies in
\[
C_t=[Qt-2s,\,Qt+6s].
\]
The gaps between successive such intervals contain at least
\[
Q-8s-1>12k^2
\]
integers.

Furthermore, since \(Q\) is even,
\[
x\equiv t^2\equiv t\pmod2.
\]
Thus all triple blockers lying in a given \(C_t\) have one fixed parity.

Let \(M=\operatorname{Mid}(A_k)\). Then
\[
|M|\le\binom{k+1}{2}.
\]
No blocked consecutive interval can meet two different \(C_t\)'s: to do so, it would have to contain an intervening gap of more than \(12k^2>|M|\) points, none of which is a triple blocker, while all would have to belong to \(M\).

Suppose a blocked interval \(J\) meets one \(C_t\). Within \(J\cap C_t\), every integer of the parity opposite to \(t\) must belong to \(M\), so
\[
|J\cap C_t|\le2|M|+1.
\]
Every point of \(J\setminus C_t\) must also belong to \(M\), since \(J\) meets no other triple-blocker band. Hence
\[
|J|\le3|M|+1
\le3\binom{k+1}{2}+1.
\]
If \(J\) meets no \(C_t\), then \(J\subseteq M\), giving an even smaller bound. ∎

The choice \(Q=20k^2\) deliberately makes the bands disjoint. The unresolved near-threshold regime \(Q\asymp2k^2\), where the bands overlap heavily, remains a reasonable computational target but no proof of cubic coverage emerged.

## Self-Audit

1. **The central construction is missing.**  
   Proposition 3 gives a sufficient interpolation mechanism, but none of the sets constructed here satisfies its hypotheses. I therefore make no claim to have solved even the subsequence version. The route is marked BLOCKED precisely at this point.

2. **The modular obstruction uses the strong, ordinary modular Sidon convention.**  
   Lemma 4 would not follow from a weak Sidon condition omitting repeated pairs. In Proposition 7 the reduced set is checked under the strong convention: equal first two power sums determine the full unordered pair, including doubletons. Thus the application is valid.

3. **The quadratic-band bound is intentionally limited to a widely separated scale.**  
   It does not rule out \(A=\{Qi+i^2\}\) when \(Q\) is close to the minimum needed for Sidonicity. For \(Q=20k^2\), however, the band separation, parity restriction and midpoint count are explicit, so the stated \(O(k^2)\) bound is rigorous.

## Computations To Verify

```python
from itertools import combinations, combinations_with_replacement
from math import comb

def is_sidon(A):
    A = sorted(A)
    seen = {}
    for i, a in enumerate(A):
        for b in A[i:]:
            s = a + b
            if s in seen and seen[s] != (a, b):
                return False
            seen[s] = (a, b)
    return True

def is_B3(A):
    seen = {}
    for tri in combinations_with_replacement(sorted(A), 3):
        s = sum(tri)
        if s in seen and seen[s] != tri:
            return False
        seen[s] = tri
    return True

def blocker(A):
    A = sorted(A)
    T = set()
    Mid = set()
    for i, b in enumerate(A):
        for c in A[i:]:
            s = b + c
            for a in A:
                T.add(s - a)
            if s % 2 == 0:
                Mid.add(s // 2)
    return T | Mid, T, Mid

def longest_run(S):
    if not S:
        return 0, None
    vals = sorted(S)
    best_len = cur_len = 1
    best = cur_start = vals[0]
    prev = vals[0]
    for x in vals[1:]:
        if x == prev + 1:
            cur_len += 1
        else:
            if cur_len > best_len:
                best_len, best = cur_len, cur_start
            cur_start, cur_len = x, 1
        prev = x
    if cur_len > best_len:
        best_len, best = cur_len, cur_start
    return best_len, (best, best + best_len - 1)

def modular_sidon(A, m):
    R = [a % m for a in A]
    if len(set(R)) != len(R):
        return False
    seen = {}
    for i, a in enumerate(R):
        for b in R[i:]:
            s = (a + b) % m
            pair = tuple(sorted((a, b)))
            if s in seen and seen[s] != pair:
                return False
            seen[s] = pair
    return True

def digit_B3(p):
    B = 3 * p
    A = [
        t + B * pow(t, 2, p) + B * B * pow(t, 3, p)
        for t in range(p)
    ]
    return A

def quadratic_ruler(k):
    Q = 20 * k * k
    return [Q*i + i*i for i in range(k)]

# Verify Proposition 7 for small primes.
for p in [5, 7, 11, 13]:
    A = digit_B3(p)
    B = 3 * p
    S, T, M = blocker(A)

    assert is_B3(A)
    assert modular_sidon(A, B*B)
    assert len(T) == (p**3 - p**2 + 2*p)//2

    L, interval = longest_run(S)
    assert L < 2 * B * B
    print("B3", p, len(T), L, interval)

# Verify Proposition 8.
for k in range(2, 30):
    A = quadratic_ruler(k)
    S, T, M = blocker(A)

    assert is_sidon(A)
    L, interval = longest_run(S)
    assert L <= 3 * comb(k+1, 2) + 1
    print("quadratic", k, L, interval)
```

A direct Route-1 search should optimize the consecutive component of \(\mathcal B(A)\) containing the whole hull, rather than \(|\mathcal B(A)|\):

```python
def components(S):
    vals = sorted(S)
    if not vals:
        return []
    out = []
    lo = hi = vals[0]
    for x in vals[1:]:
        if x == hi + 1:
            hi = x
        else:
            out.append((lo, hi))
            lo = hi = x
    out.append((lo, hi))
    return out

def hull_containing_blocked_interval(A):
    S, _, _ = blocker(A)
    amin, amax = min(A), max(A)
    for lo, hi in components(S):
        if lo <= amin and amax <= hi:
            return hi - lo + 1, (lo, hi)
    return 0, None

def exhaustive_search(k, max_coordinate):
    # Normalize min(A)=0; translation is irrelevant.
    best = None
    for tail in combinations(range(1, max_coordinate + 1), k - 1):
        A = (0,) + tail
        if not is_sidon(A):
            continue
        L, I = hull_containing_blocked_interval(A)
        score = (L, -max(A))
        if best is None or score > best[0]:
            best = (score, A, I)
    return best

# Feasible only for small parameters.
for k in range(2, 7):
    print(k, exhaustive_search(k, max_coordinate=80))
```

Important diagnostics for every optimized candidate:

```python
def modular_aliasing_profile(A, max_m):
    """
    A maximal candidate blocking an interval of length N must fail
    injective modular Sidonicity for every m <= N//2.
    """
    profile = []
    for m in range(2, max_m + 1):
        injective = len({a % m for a in A}) == len(A)
        mod_sidon = modular_sidon(A, m) if injective else False
        profile.append((m, injective, mod_sidon))
    return profile
```

The most useful unresolved experiment is to test
\[
A_{k,Q}=\{Qi+i^2:0\le i<k\}
\]
for \(Q\) just large enough to make it Sidon, rather than \(Q=20k^2\), and plot the hull-containing blocked interval divided by \(k^3\).

## Route Diagnosis

**Proved ledger**

- A cubic blocked interval forces a cubic ruler span.
- A blocked interval containing the ruler can be trimmed to every intermediate length.
- A family with a constant-factor blocker margin beyond its hull would interpolate to all sufficiently large \(N\).
- If a modulus \(m\) injectively maps \(A\) to a modular Sidon set, selected residue fibers contain no blockers outside \(A\); hence no blocked run has length \(2m\).
- A \(B_3\)-set has exactly
  \[
  \frac{k^3-k^2+2k}{2}
  \]
  triple blockers, with unique representation outside \(A\).
- Explicit cubic-span \(B_3\)-rulers can nevertheless have longest blocked run only \(O(k^2)\).
- A natural widely separated quadratic ruler also has longest blocked run only \(O(k^2)\).

**Plausible but unproved**

- The near-minimal quadratic family \(A=\{Qi+i^2\}\) with \(Q\approx2k^2\) may have substantially better coverage because adjacent triple bands overlap. No evidence yet shows a positive \(k^3\)-scale interval.
- A successful construction may require deliberately engineered carries so that no modulus \(m\ll k^3\) certifies Sidonicity.
- Controlled blocker collisions may be beneficial or necessary: maximizing the number of distinct blockers, as \(B_3\)-sets do, does not organize them into an interval.

**Dead ends**

- **Single lifts of modular or finite-field Sidon sets:** rigorously killed by Lemma 4.
- **No-carry moment-curve digit constructions:** their low digits form a modular Sidon projection, so their blocked runs are only quadratic.
- **Using \(B_3\)-sets solely to eliminate triple collisions:** explicit counterexamples have \(\Theta(k^3)\) blockers but \(O(k^2)\) longest runs.
- **Widely separated polynomial scales:** rigorous band gaps and parity holes prevent cubic coverage.
- **Counting total blockers:** it does not control contiguity and is therefore the wrong optimization objective.

The route is blocked at the genuinely open design lemma: produce, for every large \(k\), a carry-rich \(k\)-element Sidon ruler whose blocker set has a consecutive component of length \(\Theta(k^3)\) containing the entire ruler, with enough margin to interpolate between successive \(k\). A fresh attempt should search directly for that hull-containing component and reject candidates with any small modular Sidon projection.