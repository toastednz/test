STATUS: BLOCKED

## Result

A complete determination is blocked by the unresolved identity \(f(n,2)=\binom n2-\operatorname{ex}(n,C_4)\). Pursuing Route 4 nevertheless yields several rigorous results. I derive the optimal universal two-moment certificate-overlap inequality and an exact formula for pairwise certificate intersections, then give an explicit graph showing that even this strengthened relaxation is insufficient. A dual certificate-covering argument, combined with hereditary deletion, proves an exact formula near the diagonal \(n=k+2+a\) whenever \(k\) is sufficiently large in terms of fixed \(a\). In particular, the entire first off-diagonal is determined:
\[
f(k+3,k)=
\begin{cases}
0,&k=0,\\
2,&k=1,\\
4,&k=2,\\
2k+1,&k\ge3.
\end{cases}
\]

## Complete Argument

### 1. Certificate families and the degree-only relaxation

Fix \(k\ge1\), put
\[
m=k+2,
\]
and let \(G\) be an \(n\)-vertex graph satisfying the required property.

For each \(v\in V(G)\), define
\[
\mathcal A_v=\left\{S\in\binom{V(G)}m:
v\in S,\ d_{G[S]}(v)\ge k\right\}.
\]
Thus the desired property is exactly
\[
\bigcup_{v\in V(G)}\mathcal A_v=\binom{V(G)}m.
\]

If \(d(v)=d\), then \(v\) certifies a set \(S\) precisely when, among the \(k+1\) vertices of \(S\setminus\{v\}\), either all are neighbors of \(v\), or exactly \(k\) are neighbors. Hence
\[
|\mathcal A_v|
=h_{n,k}(d):=
\binom d{k+1}+(n-1-d)\binom dk.
\]
Consequently,
\[
\sum_v h_{n,k}(d(v))\ge \binom n{k+2}.
\]

Define
\[
\alpha_{n,k}=\max_{1\le d\le n-1}\frac{h_{n,k}(d)}d,
\]
with \(\binom ab=0\) outside its usual range. Since
\[
h_{n,k}(d(v))\le \alpha_{n,k}d(v),
\]
the handshake lemma gives the rigorous degree-only bound
\[
\boxed{
e(G)\ge
\left\lceil
\frac{\binom n{k+2}}{2\alpha_{n,k}}
\right\rceil.
}
\]

For fixed \(k\ge2\), if \(d/n\to p\), then
\[
\frac{h_{n,k}(d)}{d\,n^k}
\longrightarrow
\frac1{k!}p^{k-1}
\left(1-\frac{k}{k+1}p\right).
\]
The function
\[
g_k(p)=p^{k-1}\left(1-\frac{k}{k+1}p\right)
\]
is maximized on \([0,1]\) at
\[
p_k=1-\frac1{k^2},
\]
because
\[
g_k'(p)=p^{k-2}
\left((k-1)-\frac{k^2}{k+1}p\right).
\]
At this point,
\[
g_k(p_k)=\frac1k\left(1-\frac1{k^2}\right)^{k-1}.
\]
It follows that
\[
\alpha_{n,k}
=
\left(
\frac1{k\,k!}
\left(1-\frac1{k^2}\right)^{k-1}
+o(1)
\right)n^k.
\]
Therefore Route 4 without overlap information gives only
\[
\boxed{
f(n,k)\ge
\left(
\frac{k}
{2(k+1)(k+2)(1-k^{-2})^{k-1}}
+o(1)
\right)n^2.
}
\]
For example, when \(k=2\), this gives \(f(n,2)\ge(1/9+o(1))n^2\), while the truth is \((1/2+o(1))n^2\). Thus degree data alone loses the main extremal phenomenon.

For \(k=1\), direct simplification gives
\[
\frac{h_{n,1}(d)}d=n-\frac32-\frac d2,
\]
so \(\alpha_{n,1}=n-2\), again producing only a weak bound.

---

### 2. Exact pairwise certificate overlap

For distinct vertices \(u,v\), let
\[
I_{uv}=|\mathcal A_u\cap\mathcal A_v|.
\]

#### Lemma 1: Exact pair-intersection formula

Let \(W=V(G)\setminus\{u,v\}\).

If \(uv\notin E(G)\), put
\[
c=|N(u)\cap N(v)|.
\]
Then
\[
\boxed{I_{uv}=\binom ck.}
\]

If \(uv\in E(G)\), partition \(W\) into four classes:

- \(C\): adjacent to both \(u,v\), with \(|C|=c\);
- \(A\): adjacent to \(u\) but not \(v\), with \(|A|=a\);
- \(B\): adjacent to \(v\) but not \(u\), with \(|B|=b\);
- \(D\): adjacent to neither, with \(|D|=q\).

Then
\[
\boxed{
I_{uv}
=
\binom ck
+(a+b+q)\binom c{k-1}
+ab\binom c{k-2}.
}
\]

#### Proof

Every set in \(\mathcal A_u\cap\mathcal A_v\) has the form
\[
S=\{u,v\}\cup T,\qquad |T|=k.
\]

If \(uv\notin E(G)\), then \(u\) has degree at least \(k\) in \(S\) only if every member of \(T\) is adjacent to \(u\). The same holds for \(v\). Thus \(T\subseteq N(u)\cap N(v)\), giving \(\binom ck\) choices.

Suppose \(uv\in E(G)\). The edge \(uv\) contributes one neighbor to each endpoint. Thus \(u\) and \(v\) are both witnesses precisely when \(T\) contains at most one nonneighbor of \(u\) and at most one nonneighbor of \(v\).

The possible non-common-neighbor patterns in \(T\) are exactly:

1. no vertex outside \(C\);
2. one vertex from exactly one of \(A,B,D\);
3. one vertex from \(A\) and one from \(B\).

All other patterns give at least two nonneighbors to \(u\) or to \(v\). Counting the three cases gives the stated formula. ∎

---

### 3. The optimal universal two-moment overlap inequality

For each \(m\)-set \(S\), let
\[
t(S)=|\{v\in S:S\in\mathcal A_v\}|
\]
be its number of witnesses. Then
\[
\sum_v|\mathcal A_v|=\sum_S t(S)
\]
and
\[
\sum_{u<v}I_{uv}=\sum_S\binom{t(S)}2.
\]

For every integer \(1\le t\le m\),
\[
t-\frac2m\binom t2
=\frac{t(m-t+1)}m\ge1.
\]
Therefore every graph satisfying the required property obeys
\[
\boxed{
\binom nm
\le
\sum_v|\mathcal A_v|
-\frac2m\sum_{u<v}I_{uv}.
}
\]

The coefficient \(2/m\) is best possible among inequalities of the form
\[
\mathbf 1_{\{t\ge1\}}\le t-\lambda\binom t2
\qquad(0\le t\le m),
\]
because substituting \(t=m\) forces
\[
1\le m-\lambda\binom m2,
\]
or \(\lambda\le2/m\).

Thus this is the strongest graph-independent correction obtainable from only the first two certificate moments in that linear form.

---

### 4. Pairwise overlap is still insufficient

The preceding inequality does not characterize the desired property.

Take \(k=3\), so \(m=5\), and let \(G\) have vertex set
\[
U\cup W,\qquad |U|=2,\quad |W|=5,
\]
where:

- the two vertices in \(U\) are adjacent;
- every vertex of \(U\) is adjacent to every vertex of \(W\);
- \(W\) is independent.

Thus \(G\) is the join \(K_2\vee \overline{K_5}\).

The set \(W\) itself has maximum degree \(0<3\), so \(G\) fails the required property.

Nevertheless, consider its five-element subsets:

- There is one set containing no vertex of \(U\); it has \(t(S)=0\).
- There are
  \[
  \binom21\binom54=10
  \]
  sets containing exactly one vertex of \(U\). The unique such vertex has induced degree \(4\), so \(t(S)=1\).
- There are
  \[
  \binom22\binom53=10
  \]
  sets containing both vertices of \(U\). The two vertices of \(U\) are witnesses, while each vertex of \(W\) has degree \(2<3\), so \(t(S)=2\).

Hence
\[
I_1:=\sum_S t(S)=10+2\cdot10=30
\]
and
\[
I_2:=\sum_S\binom{t(S)}2=10.
\]
The pair-corrected right-hand side is
\[
I_1-\frac25I_2=30-4=26,
\]
whereas
\[
\binom75=21.
\]
Thus the strengthened inequality is satisfied even though the graph fails the property.

This is a concrete obstruction to closing Route 4 with only degrees and pairwise overlaps.

---

### 5. The full overlap hierarchy

For \(1\le j\le m\), define
\[
I_j=
\sum_{\substack{Q\subseteq V(G)\\|Q|=j}}
\left|\bigcap_{v\in Q}\mathcal A_v\right|.
\]
Double counting gives
\[
I_j=\sum_{S\in\binom Vm}\binom{t(S)}j.
\]
Consequently, inclusion-exclusion gives the exact identity
\[
\left|\bigcup_v\mathcal A_v\right|
=
\sum_{j=1}^m(-1)^{j+1}I_j.
\]
Thus the desired property is equivalent to
\[
\binom nm
=
\sum_{j=1}^m(-1)^{j+1}I_j.
\]

The higher intersections genuinely depend on higher-order neighborhood geometry. For example, if \(Q\) is a \(j\)-set, put
\[
\eta_v=
|\{w\in Q\setminus\{v\}:vw\notin E(G)\}|.
\]
If some \(\eta_v\ge2\), then
\[
\bigcap_{v\in Q}\mathcal A_v=\varnothing.
\]
Otherwise, a set in the intersection is \(Q\cup T\), where \(|T|=m-j\) and
\[
\eta_v+
|\{x\in T:vx\notin E(G)\}|
\le1
\qquad\text{for every }v\in Q.
\]
This count depends on the complete joint nonadjacency patterns of vertices outside \(Q\) toward \(Q\), not merely on degrees or pairwise codegrees. At order \(m\), the hierarchy is exact but is essentially a restatement of the original covering problem.

---

### 6. A dual certificate argument near the diagonal

The certificate method becomes more effective when \(n-m\) is fixed. Let
\[
M_m(n)=\operatorname{ex}(n,\mathcal F_m).
\]
Thus
\[
f(n,k)=\binom n2-M_{k+2}(n).
\]

Write
\[
n=m+a,\qquad a\ge0.
\]
For an \(\mathcal F_m\)-free graph \(H\), deleting any \(a\)-set leaves an \(m\)-vertex graph of minimum degree at most one. One may therefore regard a surviving low-degree vertex as a certificate for the deleted \(a\)-set.

#### Theorem 2: Eventual exact formula for every fixed diagonal

Let \(m\ge3\) and \(a\ge0\). Suppose that, for every \(1\le s\le a\),
\[
\boxed{
(m+s)(m+s-1)(m-2)
\ge
s(s+1)^2m(2m+s-4).
}
\tag{1}
\]
Then
\[
\boxed{
M_m(m+a)=\binom{m-1}2+a+1.
}
\tag{2}
\]

Equivalently, for \(m=k+2\),
\[
\boxed{
f(k+a+2,k)=\frac{(a+1)(2k+a)}2.
}
\tag{3}
\]

#### Construction

Take a clique \(K_{m-1}\) and add \(a+1\) vertices, each of degree one, with their unique neighbors in the clique. This graph has
\[
\binom{m-1}2+a+1
\]
edges.

Every \(m\)-vertex subset omits only \(a\) of the \(a+1\) pendant vertices. It therefore contains at least one pendant vertex, whose degree within the subset is at most one. Hence the graph is \(\mathcal F_m\)-free.

#### Upper bound

We prove by induction on \(s\) that every \(\mathcal F_m\)-free graph \(H\) on
\[
N=m+s
\]
vertices has at most
\[
B_s:=\binom{m-1}2+s+1
\]
edges.

For \(s=0\), the whole \(m\)-vertex graph has minimum degree at most one. Choosing a vertex of degree at most one gives
\[
e(H)\le\binom{m-1}2+1=B_0.
\]

Now let \(1\le s\le a\), and assume the result for \(s-1\).

If \(\delta(H)\le1\), delete a vertex \(v\) of degree at most one. The remaining graph is still \(\mathcal F_m\)-free, so
\[
e(H)\le B_{s-1}+1=B_s.
\]

It remains to treat \(\delta(H)\ge2\).

For every \(s\)-set \(T\subseteq V(H)\), the graph \(H-T\) has \(m\) vertices and minimum degree at most one. Choose
\[
v\in V(H)\setminus T
\]
with
\[
d_{H-T}(v)\le1.
\]
Since \(\delta(H)\ge2\),
\[
2\le d_H(v)\le s+1,
\]
and \(T\) contains at least one neighbor of \(v\).

Let
\[
L=\{v:2\le d_H(v)\le s+1\},\qquad r=|L|.
\]
Every \(s\)-set \(T\) is certified by some \(v\in L\).

For a fixed \(v\in L\), the number of \(s\)-sets \(T\) which omit \(v\) and contain at least one neighbor of \(v\) is at most
\[
d_H(v)\binom{N-2}{s-1}
\le
(s+1)\binom{N-2}{s-1}.
\]
Thus
\[
\binom Ns
\le
r(s+1)\binom{N-2}{s-1}.
\]
Since \(N-s=m\), this gives
\[
r\ge
\frac{N(N-1)}{s(s+1)m}.
\tag{4}
\]

The degree sum is at most
\[
2e(H)
\le
r(s+1)+(N-r)(N-1)
=
N(N-1)-r(m-2).
\]
Using (4),
\[
2e(H)
\le
N(N-1)-
\frac{N(N-1)(m-2)}{s(s+1)m}.
\]
Condition (1) implies that the subtracted term is at least
\[
(s+1)(2m+s-4).
\]
A direct expansion gives
\[
N(N-1)-(s+1)(2m+s-4)
=
(m-1)(m-2)+2(s+1)
=
2B_s.
\]
Therefore \(e(H)\le B_s\), completing the induction and proving (2).

Finally, substituting \(m=k+2\) gives
\[
\begin{aligned}
f(k+a+2,k)
&=\binom{k+a+2}2-\binom{k+1}2-(a+1)\\
&=\frac{(a+1)(2k+a)}2.
\end{aligned}
\]
∎

A simpler, although crude, sufficient condition for (1) is
\[
\boxed{
m\ge4a(a+1)^2+a+2.
}
\]
Indeed, put \(A=a(a+1)^2\). For \(s\le a\), it suffices that
\[
(m-1)(m-2)\ge A(2m+a).
\]
Writing \(x=m-2\), the stated hypothesis gives \(x\ge4A+a\). Then
\[
x(x+1)\ge4Ax\ge A(2x+a+4)=A(2m+a).
\]

Thus for every fixed \(a\), formula (3) holds for all sufficiently large \(k\).

---

### 7. Exact solution of the first off-diagonal

The preceding threshold is very crude when \(a=1\). This case can be solved completely.

#### Theorem 3

For \(k\ge0\),
\[
\boxed{
f(k+3,k)=
\begin{cases}
0,&k=0,\\
2,&k=1,\\
4,&k=2,\\
2k+1,&k\ge3.
\end{cases}
}
\]

#### Proof for \(k\ge3\)

Put
\[
n=k+3,\qquad m=k+2=n-1.
\]
We prove that
\[
M_{n-1}(n)=\binom{n-2}2+2
\qquad(n\ge6).
\tag{5}
\]

The lower construction is a clique on \(n-2\) vertices together with two degree-one vertices. Every \((n-1)\)-set contains at least one of those two vertices, which has induced degree at most one. Hence the graph is \(\mathcal F_{n-1}\)-free and has the edge count in (5).

For the upper bound, let \(H\) be \(\mathcal F_{n-1}\)-free.

If \(\delta(H)\le1\), delete a vertex \(v\) with \(d(v)\le1\). The remaining graph has \(n-1\) vertices and minimum degree at most one, so it has at most
\[
\binom{n-2}2+1
\]
edges. Therefore
\[
e(H)\le\binom{n-2}2+2.
\]

Now suppose \(\delta(H)\ge2\). For every vertex \(x\), the graph \(H-x\) has a vertex \(y\) of degree at most one. Thus
\[
d_H(y)-\mathbf 1_{\{xy\in E(H)\}}\le1.
\]
Since \(d_H(y)\ge2\), necessarily \(xy\in E(H)\) and \(d_H(y)=2\).

Let
\[
L=\{v:d_H(v)=2\},\qquad r=|L|,
\]
and let \(U=V(H)\setminus L\), with \(|U|=s=n-r\). The preceding argument shows that every vertex has a neighbor in \(L\). In particular:

- every vertex of \(U\) has a neighbor in \(L\);
- every vertex of \(L\) has a neighbor in \(L\).

Hence
\[
\delta(H[L])\ge1,
\qquad e(H[L])\ge\frac r2,
\]
and, writing \(e(L,U)\) for the number of crossing edges,
\[
2r=2e(H[L])+e(L,U).
\]
Therefore
\[
e(H[L])+e(L,U)
=2r-e(H[L])
\le\frac{3r}{2}.
\]
Also \(s\le e(L,U)\le r\), so \(s\le n/2\).

If \(s=0\), then \(H\) is 2-regular and \(e(H)=n\), which is at most \(\binom{n-2}2+2\) for \(n\ge6\).

If \(1\le s\le n/2\), then
\[
e(H)
\le
\binom s2+\frac{3(n-s)}2
=:F(s).
\]
The function \(F\) is convex, so its maximum on \([1,n/2]\) occurs at an endpoint. At \(s=1\),
\[
\binom{n-2}2+2-F(1)
=
\frac{n^2-8n+13}{2}\ge0
\qquad(n\ge6).
\]
At \(s=n/2\),
\[
\binom{n-2}2+2-F(n/2)
=
\frac{3n^2-24n+40}{8}\ge0
\qquad(n\ge6).
\]
Thus (5) follows.

Consequently, for \(k\ge3\),
\[
\begin{aligned}
f(k+3,k)
&=\binom{k+3}2-\left(\binom{k+1}2+2\right)\\
&=2k+1.
\end{aligned}
\]

For \(k=1\), the known Mantel formula gives \(f(4,1)=2\).

For \(k=2\), one needs \(\operatorname{ex}(5,C_4)\). The graph consisting of two triangles sharing one vertex has six edges and no \(C_4\). Conversely, in a \(C_4\)-free graph on five vertices,
\[
\sum_v\binom{d(v)}2\le\binom52=10.
\]
If there were at least seven edges, the degree sum would be at least \(14\), and convexity would give
\[
\sum_v\binom{d(v)}2\ge13,
\]
a contradiction. Hence \(\operatorname{ex}(5,C_4)=6\), and
\[
f(5,2)=\binom52-6=4.
\]

The case \(k=0\) is automatic. ∎

## Self-Audit

1. **The eventual diagonal theorem has a very crude threshold.**  
   The union bound counts every deleted set once for each included neighbor of a certifying vertex, so substantial overcount is discarded. This affects only sharpness, not validity: every inequality is used in the safe direction, and condition (1) explicitly compensates for the loss.

2. **The \(\delta(H)\ge2\) analysis in the first off-diagonal is the most delicate structural step.**  
   The possible concern is whether every vertex really has a degree-two neighbor. It does: applying the defining property to \(H-x\), global minimum degree at least two forces its low-degree witness to be adjacent to \(x\) and to have global degree exactly two. The cases \(L=V(H)\) and \(L\ne V(H)\) are treated separately.

3. **The pair-intersection formula is vulnerable to an off-by-one error because the threshold is \(k=m-2\).**  
   The edge \(uv\) supplies one neighbor when present, so the remaining \(k\)-set may contain at most one nonneighbor of each endpoint. The five allowed category patterns listed in the proof exhaust exactly those possibilities. The formula can also be checked exhaustively by the code below.

## Computations To Verify

```python
from itertools import combinations
from math import comb

def C(n, r):
    return comb(n, r) if 0 <= r <= n else 0

def graph_from_mask(n, mask):
    pairs = list(combinations(range(n), 2))
    adj = [set() for _ in range(n)]
    for bit, (u, v) in enumerate(pairs):
        if (mask >> bit) & 1:
            adj[u].add(v)
            adj[v].add(u)
    return adj

def complement(adj):
    n = len(adj)
    out = [set() for _ in range(n)]
    for u in range(n):
        for v in range(u + 1, n):
            if v not in adj[u]:
                out[u].add(v)
                out[v].add(u)
    return out

def is_Fm_free(adj, m):
    """True iff every m-set has an induced vertex of degree at most 1."""
    n = len(adj)
    for S in combinations(range(n), m):
        SS = set(S)
        if all(len(adj[v] & SS) >= 2 for v in S):
            return False
    return True

def satisfies_original(adj, k):
    n = len(adj)
    m = k + 2
    for S in combinations(range(n), m):
        SS = set(S)
        if max(len(adj[v] & SS) for v in S) < k:
            return False
    return True

def extremal_M(n, m):
    """Brute force; practical only for n <= 7 or so."""
    E = n * (n - 1) // 2
    best = -1
    witnesses = []
    for mask in range(1 << E):
        e = mask.bit_count()
        if e < best:
            continue
        adj = graph_from_mask(n, mask)
        if is_Fm_free(adj, m):
            if e > best:
                best = e
                witnesses = [mask]
            elif e == best:
                witnesses.append(mask)
    return best, witnesses

def certificate_stats(adj, k):
    n = len(adj)
    m = k + 2
    I = [0] * (m + 1)
    covered = 0

    for S in combinations(range(n), m):
        SS = set(S)
        t = sum(len(adj[v] & SS) >= k for v in S)
        covered += (t > 0)
        for j in range(1, t + 1):
            I[j] += C(t, j)

    degree_formula = 0
    for v in range(n):
        d = len(adj[v])
        degree_formula += C(d, k + 1) + (n - 1 - d) * C(d, k)

    assert I[1] == degree_formula
    inclusion_exclusion = sum(
        ((-1) ** (j + 1)) * I[j] for j in range(1, m + 1)
    )
    assert inclusion_exclusion == covered

    return covered, I

def pair_formula(adj, u, v, k):
    n = len(adj)
    W = [x for x in range(n) if x not in (u, v)]

    if v not in adj[u]:
        c = sum(x in adj[u] and x in adj[v] for x in W)
        return C(c, k)

    c = a = b = q = 0
    for x in W:
        xu = x in adj[u]
        xv = x in adj[v]
        if xu and xv:
            c += 1
        elif xu:
            a += 1
        elif xv:
            b += 1
        else:
            q += 1

    return (
        C(c, k)
        + (a + b + q) * C(c, k - 1)
        + a * b * C(c, k - 2)
    )

def pair_intersection_bruteforce(adj, u, v, k):
    n = len(adj)
    m = k + 2
    ans = 0
    for S in combinations(range(n), m):
        if u not in S or v not in S:
            continue
        SS = set(S)
        if len(adj[u] & SS) >= k and len(adj[v] & SS) >= k:
            ans += 1
    return ans

def verify_pair_formula_all_graphs(n, k):
    E = n * (n - 1) // 2
    for mask in range(1 << E):
        adj = graph_from_mask(n, mask)
        for u, v in combinations(range(n), 2):
            assert pair_formula(adj, u, v, k) == \
                   pair_intersection_bruteforce(adj, u, v, k)

def split_counterexample():
    # G = K_2 join independent K_5, for k=3.
    n = 7
    U = {0, 1}
    adj = [set() for _ in range(n)]
    for u, v in combinations(range(n), 2):
        if u in U or v in U:
            adj[u].add(v)
            adj[v].add(u)

    covered, I = certificate_stats(adj, 3)
    assert covered == 20
    assert I[1] == 30
    assert I[2] == 10
    assert 30 - (2 / 5) * 10 == 26
    assert C(7, 5) == 21
    assert not satisfies_original(adj, 3)

def diagonal_condition(m, a):
    return all(
        (m+s)*(m+s-1)*(m-2)
        >= s*(s+1)**2*m*(2*m+s-4)
        for s in range(1, a+1)
    )

# Exhaustive checks suggested:
#
# assert extremal_M(4, 3)[0] == 4
# assert extremal_M(5, 4)[0] == 6
# assert extremal_M(6, 5)[0] == 8
# assert extremal_M(7, 6)[0] == 12
#
# For every exhaustively feasible m,a:
# if diagonal_condition(m, a):
#     assert extremal_M(m+a, m)[0] == C(m-1, 2) + a + 1
#
# verify_pair_formula_all_graphs(5, 2)
# split_counterexample()
```

For larger instances, the most useful SAT check is:

1. Fix \(m,a\) and set
   \[
   E_0=\binom{m-1}2+a+2.
   \]
2. Encode an \((m+a)\)-vertex \(\mathcal F_m\)-free graph with at least \(E_0\) edges.
3. Ask for satisfiability. Under the theorem’s hypothesis, the instance must be UNSAT.
4. For values below the theorem’s threshold, SAT models would identify exceptional denser constructions.

## Route Diagnosis

**Proved ledger**

- Exact single-certificate count \(h_{n,k}(d)\).
- A rigorous degree-only lower bound and its fixed-\(k\) asymptotic optimization.
- Exact pairwise certificate-intersection formulas.
- The optimal universal inequality using the first two certificate moments.
- An explicit \(K_2\vee\overline{K_5}\) counterexample showing that this pairwise relaxation is not sufficient.
- The full higher-intersection identity, together with a precise description of the higher-order neighborhood data it requires.
- The eventual exact formula
  \[
  f(k+a+2,k)=\frac{(a+1)(2k+a)}2
  \]
  under the explicit finite condition (1), hence for every fixed \(a\) and all sufficiently large \(k\).
- The exact first off-diagonal \(n=k+3\) for every \(k\).

**Plausible but unproved**

- The near-diagonal formula likely holds under thresholds much smaller than the crude sufficient bound \(k\ge4a(a+1)^2+a\).
- For fixed \(a\), exceptional extremizers below the eventual range may admit a finite structural classification in terms of minimum-degree-two certificate covers.
- No such conjecture is used in any proof above.

**Dead ends**

- Degree-only optimization has a quadratic-scale gap from the truth for fixed \(k\).
- Pairwise overlap remains insufficient; the explicit seven-vertex example passes the strongest universal two-moment inequality.
- Continuing to all overlap orders becomes exact inclusion-exclusion and requires the full joint neighborhood geometry, effectively reproducing the original problem.
- For fixed \(k\) and large \(n\), the dual deletion argument becomes weak because the deleted set has size \(n-m\), rather than fixed size.

**Decisive block**

For \(k=2\),
\[
f(n,2)=\binom n2-\operatorname{ex}(n,C_4).
\]
Thus an exact all-\((n,k)\) solution would determine \(\operatorname{ex}(n,C_4)\) for every \(n\). Route 4 does not bypass this barrier: degree certificates lose codegree geometry, pair overlaps are insufficient, and the complete overlap hierarchy is equivalent in complexity to detecting all relevant configurations.

A fresh attempt should either:

1. sharpen the dual deletion-cover argument to classify all fixed near-diagonals with practical thresholds; or
2. explicitly confront the \(C_4\) extremal problem using codegrees, finite geometry, and computer-assisted stability.

Without a breakthrough on the latter, the full exact Erdős problem remains blocked.