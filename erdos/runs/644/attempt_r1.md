STATUS: BLOCKED

## Result

I did not resolve either asymptotic question. Pursuing minimum transversals and private edges yields several rigorous structural lemmas: every subset of a minimum transversal supports a localized subhypergraph with exactly that transversal number; selected private edges force a fourth-moment concentration inequality on external incidences; a high-incidence external vertex admits an exact purge-or-exchange dichotomy; and an edge-critical reduction gives a standard Bollobás set-pairs system. However, these facts do not imply \(4\tau(\mathcal H)\le 3k+o(k)\). The precise obstruction is that private edges alone may all share external vertices, while the purge-or-exchange operation produces another \(7\)-locally 2-coverable \(k\)-uniform instance without reducing \(k\). Thus the argument becomes self-similar rather than yielding a charge against the \(k\) vertices of an edge.

## Complete Argument

Throughout, \(\mathcal H=(V,E)\) is \(k\)-uniform and satisfies \((P_7)\). Let
\[
t=\tau(\mathcal H),
\]
and let \(T\subseteq V\) be a minimum transversal with \(|T|=t\).

For every \(x\in T\), the set \(T\setminus\{x\}\) is not a transversal. Hence there is an edge \(E_x\) disjoint from \(T\setminus\{x\}\). Since \(T\) is a transversal,
\[
E_x\cap T=\{x\}.
\tag{10}
\]
These selected private edges are distinct.

### 1. Exact localization inside a minimum transversal

For \(I\subseteq T\), define
\[
\mathcal H[I]
 =
 \{A\in E:A\cap(T\setminus I)=\varnothing\}.
\]

#### Lemma 1
For every \(I\subseteq T\),
\[
\tau(\mathcal H[I])=|I|.
\tag{11}
\]

#### Proof
Every \(A\in\mathcal H[I]\) meets \(T\), and it is disjoint from \(T\setminus I\). Therefore \(A\cap I\ne\varnothing\), so \(I\) is a transversal of \(\mathcal H[I]\). Thus
\[
\tau(\mathcal H[I])\le |I|.
\]

Suppose that \(S\) is a transversal of \(\mathcal H[I]\) with \(|S|<|I|\). Then
\[
S\cup(T\setminus I)
\]
hits every edge of \(\mathcal H\): an edge either meets \(T\setminus I\), or belongs to \(\mathcal H[I]\) and is hit by \(S\). Its cardinality is at most
\[
|S|+|T\setminus I|<|I|+t-|I|=t,
\]
contradicting the minimality of \(T\). Hence equality holds. ∎

A useful equivalent consequence is the following blocker statement.

#### Corollary 2
If \(I\subseteq T\) and \(X\subseteq V\) has \(|X|<|I|\), then there exists \(A\in E\) such that
\[
A\cap(T\setminus I)=\varnothing
\quad\text{and}\quad
A\cap X=\varnothing.
\tag{12}
\]

#### Proof
Otherwise \(X\) would be a transversal of \(\mathcal H[I]\), contrary to Lemma 1. ∎

In particular, every set of fewer than \(t\) vertices is avoided by some edge, as of course also follows directly from \(\tau(\mathcal H)=t\).

---

### 2. Incidence concentration among selected private edges

Put
\[
W=V\setminus T.
\]
For \(v\in W\), define its private-edge incidence neighborhood
\[
N(v)=\{x\in T:v\in E_x\},
\qquad d_v=|N(v)|.
\tag{13}
\]
Because \(E_x\cap T=\{x\}\), every \(E_x\) contains exactly \(k-1\) vertices of \(W\). Consequently,
\[
\sum_{v\in W}d_v=t(k-1).
\tag{14}
\]

#### Lemma 3: moment hierarchy
Let \(3\le s\le7\), put \(q=\lceil s/2\rceil\), and assume \(t\ge s\). Then
\[
\sum_{v\in W}\binom{d_v}{q}
\ge
\frac{\binom tq}{\binom sq}.
\tag{15}
\]

#### Proof
Take any \(s\)-element set \(J\subseteq T\). By \((P_7)\), the private edges
\[
\{E_x:x\in J\}
\]
are covered by at most two vertices, say \(a,b\).

A point of \(T\) belongs to at most one of these private edges, because \(E_x\cap T=\{x\}\). If both \(a,b\) lie in \(W\), one of them belongs to at least \(q=\lceil s/2\rceil\) of the selected edges. If one witness lies in \(T\), it hits at most one selected edge, so the other witness, necessarily in \(W\), hits at least \(s-1\ge q\) of them. Two points of \(T\) cannot cover \(s\ge3\) private edges.

Thus every \(s\)-set \(J\subseteq T\) contains a \(q\)-set \(Q\) for which
\[
Q\subseteq N(v)
\]
for some \(v\in W\).

Let \(\mathcal G_q\) be the family of all such \(q\)-sets. Counting pairs \((Q,J)\) with
\[
Q\in\mathcal G_q,\qquad Q\subseteq J\in\binom Ts,
\]
gives
\[
|\mathcal G_q|\binom{t-q}{s-q}\ge\binom ts.
\]
Therefore
\[
|\mathcal G_q|
\ge
\frac{\binom ts}{\binom{t-q}{s-q}}
=
\frac{\binom tq}{\binom sq}.
\]
Finally, every member of \(\mathcal G_q\) is counted at least once by
\[
\sum_{v\in W}\binom{d_v}{q}.
\]
This proves (15). ∎

For \(s=7\), this becomes the particularly useful fourth-moment inequality
\[
\boxed{\displaystyle
\sum_{v\in W}\binom{d_v}{4}
\ge \frac1{35}\binom t4.}
\tag{16}
\]

Let
\[
D=\max_{v\in W}d_v.
\]

#### Corollary 4: forced high external incidence
For \(k\ge2\) and \(t\ge7\),
\[
\binom{D-1}{3}
\ge
\frac{(t-1)(t-2)(t-3)}{210(k-1)}.
\tag{17}
\]

In particular, if \(t=\alpha k+o(k)\) with fixed \(\alpha>0\), then
\[
D\ge
\left(\frac{\alpha^3}{35}\right)^{1/3}k^{2/3}(1-o(1))
=
\frac{\alpha}{35^{1/3}}k^{2/3}(1-o(1)).
\tag{18}
\]

#### Proof
For every integer \(d\le D\),
\[
\binom d4=\frac d4\binom{d-1}{3}
\le \frac d4\binom{D-1}{3}.
\]
Using (14) and (16),
\[
\frac1{35}\binom t4
\le
\sum_{v\in W}\binom{d_v}{4}
\le
\frac{t(k-1)}4\binom{D-1}{3}.
\]
Rearranging gives (17). The asymptotic statement follows from
\[
\binom{D-1}{3}\sim \frac{D^3}{6}.
\]
∎

Thus any hypothetical example with \(t\) linear in \(k\) has an external vertex contained in at least order \(k^{2/3}\) selected private edges. This is genuine concentration, but it is not yet of linear order.

---

### 3. A one-edge anchored refinement

The following refinement records the fact that a witness for six private edges together with one fixed edge must use a point of that fixed edge.

Fix \(A\in E\), and let
\[
I_A=\{x\in T:E_x=A\}.
\]
Since the selected private edges are distinct, \(|I_A|\le1\). Put
\[
L=T\setminus I_A,\qquad n=|L|,
\]
and for \(v\in V\) define
\[
d_L(v)=|\{x\in L:v\in E_x\}|.
\]

#### Lemma 5
If \(n\ge6\), then
\[
\binom n6
\le
\binom{n-4}{2}\sum_{v\in W}\binom{d_L(v)}4
+
\binom{n-3}{3}\sum_{v\in A\cap W}\binom{d_L(v)}3.
\tag{19}
\]

#### Proof
Let \(J\in\binom L6\). The seven distinct edges
\[
A,\quad \{E_x:x\in J\}
\]
have a two-point transversal \(\{p,q\}\). At least one of the two points hits \(A\); label such a point \(p\in A\).

If \(q\) belongs to at least four of the six private edges, then \(J\) contains a four-set of indices whose private edges share \(q\).

Otherwise \(q\) belongs to at most three of those private edges. Since \(p\) and \(q\) together cover all six, \(p\) belongs to at least three of them. In this case \(J\) contains a triple whose private edges share a point \(p\in A\). Such a point must lie in \(W\), since a point of \(T\) belongs to at most one selected private edge.

A fixed common four-set lies in at most \(\binom{n-4}{2}\) six-sets \(J\), and a fixed common triple lies in at most \(\binom{n-3}{3}\) such six-sets. Summing over the possible common vertices, with overcounting allowed, gives (19). ∎

By Corollary 2, the anchored edge \(A\) may additionally be chosen to avoid any prescribed set of at most \(t-1\) vertices. The remaining difficulty is that the first, global fourth-moment term in (19) can still be dominated by a small collection of high-degree external vertices.

---

### 4. Exact purge-or-exchange dichotomy

The concentration in Corollary 4 cannot simply be declared impossible. Minimum transversality instead gives the following exact alternative.

Fix \(v\in W\), let
\[
N=N(v),\qquad d=|N|,
\]
and define
\[
\mathcal R_v
=
\{A\in E:
A\cap(T\setminus N)=\varnothing,\ v\notin A\}.
\tag{20}
\]

#### Lemma 6
For \(d\ge1\),
\[
d-1\le\tau(\mathcal R_v)\le d.
\tag{21}
\]
Moreover, exactly one of the following two numerical cases occurs.

1. **Purge case:** If \(\tau(\mathcal R_v)=d\), then for every \(x\in N\) there is a private edge \(F_x\) for \(x\), relative to the original \(T\), such that
   \[
   v\notin F_x.
   \tag{22}
   \]
   Thus all selected private edges containing \(v\) may simultaneously be replaced by private edges avoiding \(v\).

2. **Exchange case:** If \(\tau(\mathcal R_v)=d-1\), then there is another minimum transversal \(T'\) of \(\mathcal H\) with
   \[
   v\in T'.
   \tag{23}
   \]

#### Proof
Every edge of \(\mathcal R_v\) meets \(T\), avoids \(T\setminus N\), and hence meets \(N\). Thus
\[
\tau(\mathcal R_v)\le |N|=d.
\]

Conversely, let \(S\) be any transversal of \(\mathcal R_v\). Then
\[
(T\setminus N)\cup\{v\}\cup S
\tag{24}
\]
hits every edge of \(\mathcal H\). Indeed, an edge either meets \(T\setminus N\), contains \(v\), or belongs to \(\mathcal R_v\). Therefore
\[
t
\le
|(T\setminus N)\cup\{v\}\cup S|
\le
t-d+1+|S|,
\]
which gives \(|S|\ge d-1\) and proves (21).

Suppose first that \(\tau(\mathcal R_v)=d\). Then \(N\) is a minimum transversal of \(\mathcal R_v\). For every \(x\in N\), the set \(N\setminus\{x\}\) fails to hit \(\mathcal R_v\), so there is \(F_x\in\mathcal R_v\) with
\[
F_x\cap N=\{x\}.
\]
Because \(F_x\) also avoids \(T\setminus N\), it satisfies
\[
F_x\cap T=\{x\}.
\]
By the definition of \(\mathcal R_v\), it avoids \(v\). This is the purge case.

Now suppose that \(\tau(\mathcal R_v)=d-1\), and let \(S\) be a minimum transversal of \(\mathcal R_v\). Vertices in \((T\setminus N)\cup\{v\}\) lie in no edge of \(\mathcal R_v\), so \(S\) may be chosen disjoint from that set. Then
\[
T'=(T\setminus N)\cup\{v\}\cup S
\]
is a transversal of \(\mathcal H\), by the preceding argument, and
\[
|T'|=t-d+1+(d-1)=t.
\]
Hence \(T'\) is another minimum transversal, and it contains \(v\). ∎

This is the strongest concrete consequence I obtained from combining high private-edge degree with the global minimality of \(T\).

The obstruction to iteration is real: in the purge case, the replacement private edges may reintroduce vertices purged at earlier stages; in the exchange case, changing \(T\) changes all private-edge classes. There is no monotone quantity presently known that forces termination with bounded private-edge degrees.

---

### 5. Why private edges alone cannot yield the desired inequality

A direct inequality involving only a family of selected private edges is false, even if \(T\) is inclusion-minimal for that family.

Fix arbitrary \(t\) and \(k\ge2\). Let
\[
T=\{1,\dots,t\},
\]
let \(z\notin T\), and for each \(i\) introduce \(k-2\) private filler vertices \(p_{i,1},\dots,p_{i,k-2}\). Define
\[
E_i=\{i,z,p_{i,1},\dots,p_{i,k-2}\}.
\tag{25}
\]
Then:

- every \(E_i\) has size \(k\);
- \(E_i\cap T=\{i\}\);
- \(T\) is inclusion-minimal as a transversal, since \(T\setminus\{i\}\) misses \(E_i\);
- every subfamily is covered by the single point \(z\);
- nevertheless, \(t\) is arbitrary relative to \(k\).

Of course \(T\) is not a minimum transversal—the family has transversal number \(1\). Thus global minimum transversality is indispensable. In particular, any proposed charging lemma that uses only (10), uniformity, and local two-coverability is false.

---

### 6. What standard set-pairs inequalities provide

One can force a genuine set-pairs system by passing to an edge-minimal subfamily, but the resulting estimate is exponentially weaker than the desired linear bound.

First reduce to a finite family with transversal number \(t\). If no finite subfamily had transversal number \(t\), every finite subfamily would have a transversal of size at most \(t-1\). Compactness of \(\{0,1\}^V\), applied to the closed set of selections of size at most \(t-1\) and the clopen edge-hitting conditions, would then give a global transversal of size at most \(t-1\), a contradiction.

Choose a finite, inclusion-minimal edge subfamily
\[
\mathcal K=\{A_1,\dots,A_m\}
\]
with \(\tau(\mathcal K)=t\).

#### Lemma 7
For each \(i\), there is a \((t-1)\)-set \(C_i\) such that
\[
A_i\cap C_i=\varnothing
\tag{26}
\]
and
\[
A_j\cap C_i\ne\varnothing\qquad(j\ne i).
\tag{27}
\]
Consequently,
\[
m\le\binom{k+t-1}{k}.
\tag{28}
\]

#### Proof
By edge-minimality,
\[
\tau(\mathcal K\setminus\{A_i\})\le t-1.
\]
It cannot be at most \(t-2\), because adjoining one point of \(A_i\) would then give a transversal of \(\mathcal K\) of size at most \(t-1\). Hence
\[
\tau(\mathcal K\setminus\{A_i\})=t-1.
\]
Let \(C_i\) be a minimum transversal of \(\mathcal K\setminus\{A_i\}\). If \(C_i\) met \(A_i\), it would be a \((t-1)\)-element transversal of all of \(\mathcal K\), impossible. This proves (26)–(27).

For completeness, apply the permutation proof of Bollobás's set-pairs inequality. In a uniformly random ordering of the finite union of all \(A_i\) and \(C_i\), let \(\mathcal E_i\) be the event that every element of \(A_i\) precedes every element of \(C_i\). Since \(|A_i|=k\), \(|C_i|=t-1\), and they are disjoint,
\[
\Pr(\mathcal E_i)=\binom{k+t-1}{k}^{-1}.
\]

The events \(\mathcal E_i\) are pairwise disjoint. For \(i\ne j\), choose
\[
x\in A_i\cap C_j,\qquad y\in A_j\cap C_i.
\]
If both \(\mathcal E_i\) and \(\mathcal E_j\) occurred, then \(\mathcal E_i\) would force \(x\) before \(y\), while \(\mathcal E_j\) would force \(y\) before \(x\). Thus
\[
m\binom{k+t-1}{k}^{-1}\le1,
\]
which is (28). ∎

The local \(7\)-edge condition does not enter this standard inequality. Extracting a linear inequality such as \(4t\le3k+o(k)\) would require a substantial strengthening using \((P_7)\); no such strengthening emerged.

---

### 7. Ledger

**Proved lemmas**

1. Exact localization:
   \[
   \tau(\mathcal H[I])=|I|
   \quad(I\subseteq T).
   \]
2. Blockers against every \(X\) with \(|X|<|I|\).
3. Private-incidence moment hierarchy (15), especially
   \[
   \sum_v\binom{d_v}{4}\ge\binom t4/35.
   \]
4. Forced concentration
   \[
   D\ge \frac{\alpha}{35^{1/3}}k^{2/3}(1-o(1))
   \quad\text{when }t\sim\alpha k.
   \]
5. The anchored inequality (19).
6. The purge-or-exchange dichotomy of Lemma 6.
7. The edge-critical set-pairs reduction and bound (28).

**Plausible but unproved claims needed to continue**

- A monotone way to iterate Lemma 6 until all private-edge incidences are controlled.
- A theorem charging each concentration/exchange step against distinct vertices of a \(k\)-edge.
- A strengthening of Bollobás's set-pairs inequality exploiting that every seven \(A_i\)'s are two-point coverable.
- Ultimately, an inequality
  \[
  4t\le3k+o(k).
  \]

None of these has been proved here.

**Dead ends**

- Any argument using only selected private edges fails because of the common-\(z\) construction (25).
- The fourth-moment inequality forces only \(k^{2/3}\)-scale concentration, far short of the desired linear estimate.
- The purge-or-exchange reduction preserves edge size \(k\), so it does not yield a descending induction in the relevant parameter.
- Standard set-pairs inequalities give an exponential bound on the number of critical edges, not a linear bound on \(t/k\).

## Self-Audit

1. **The main quantitative result is far from \(3k/4\).**  
   Corollary 4 only forces a vertex lying in \(\Omega(k^{2/3})\) private edges when \(t=\Theta(k)\). I do not claim this is close to sufficient. The inequality itself is reliable because it follows from an exact double count and the exact identity \(\sum_v d_v=t(k-1)\).

2. **The purge-or-exchange lemma does not provide a terminating process.**  
   New private edges may reintroduce previously removed vertices, and exchanging the minimum transversal changes the whole incidence system. This is precisely the unresolved gap, not something being suppressed. The dichotomy itself follows from the exact covering relation (24), so its correctness does not depend on termination.

3. **The finite critical reduction invokes compactness.**  
   This could conceal a finiteness issue if stated carelessly. Here the relevant sets are closed in \(\{0,1\}^V\), edge-hitting conditions are clopen because edges are finite, and “support size at most \(t-1\)” is closed. Therefore the finite witness and subsequent edge-minimal reduction are valid.

## Computations To Verify

The following Python code checks local two-coverability, transversal number, the moment inequality, and the purge-or-exchange lemma for any finite example.

```python
from itertools import combinations, product
from math import comb

def C(n, r):
    return comb(n, r) if 0 <= r <= n else 0

def universe(edges):
    U = set()
    for A in edges:
        U |= set(A)
    return sorted(U)

def two_coverable(F):
    """Whether the nonempty finite edge family F has a transversal of size <= 2."""
    if not F:
        return True
    U = universe(F)
    for q in (1, 2):
        for Q in combinations(U, q):
            Q = set(Q)
            if all(Q & set(A) for A in F):
                return True
    return False

def locally_two_coverable(edges, r=7):
    m = len(edges)
    for s in range(1, min(r, m) + 1):
        for I in combinations(range(m), s):
            F = [edges[i] for i in I]
            if not two_coverable(F):
                return False
    return True

def tau(edges):
    if not edges:
        return 0
    U = universe(edges)
    for q in range(len(U) + 1):
        for Q in combinations(U, q):
            Q = set(Q)
            if all(Q & set(A) for A in edges):
                return q
    raise RuntimeError("unreachable")

def minimum_transversals(edges):
    U = universe(edges)
    t = tau(edges)
    out = []
    for Q in combinations(U, t):
        Q = set(Q)
        if all(Q & set(A) for A in edges):
            out.append(frozenset(Q))
    return out

def private_edge_options(edges, T):
    T = set(T)
    opts = {}
    for x in T:
        opts[x] = [
            frozenset(A) for A in edges
            if set(A) & T == {x}
        ]
        assert opts[x], ("No private edge for", x)
    return opts

def audit_private_choice(edges, T, chosen):
    """
    chosen[x] is one private edge for x.
    Checks sum_v C(d_v,4) >= C(t,4)/35.
    """
    T = set(T)
    U = set(universe(edges))
    W = U - T
    t = len(T)
    k = len(next(iter(edges)))

    for x, A in chosen.items():
        assert set(A) & T == {x}
        assert len(A) == k

    d = {
        v: sum(v in chosen[x] for x in T)
        for v in W
    }
    assert sum(d.values()) == t * (k - 1)

    if t >= 7:
        assert 35 * sum(C(a, 4) for a in d.values()) >= C(t, 4)

    return d

def audit_pivot(edges, T, chosen, v):
    """
    Verifies Lemma 6 for a selected external vertex v.
    """
    T = set(T)
    N = {x for x in T if v in chosen[x]}
    d = len(N)
    if d == 0:
        return None

    R = [
        frozenset(A) for A in edges
        if set(A).isdisjoint(T - N) and v not in A
    ]
    tr = tau(R)
    assert d - 1 <= tr <= d

    if tr == d:
        # Purge case: each x in N has a private edge in R avoiding v.
        for x in N:
            candidates = [
                A for A in R
                if set(A) & T == {x}
            ]
            assert candidates
    else:
        assert tr == d - 1
        # Find an exchanged minimum transversal explicitly.
        found = False
        for S in minimum_transversals(R):
            S = set(S) - ((T - N) | {v})  # remove useless vertices, if any
            Tp = (T - N) | {v} | S
            if len(Tp) == len(T) and all(Tp & set(A) for A in edges):
                found = True
                break
        assert found

    return tr, R

def private_only_counterexample(k, t):
    """
    Constructs E_i = {i,z} plus private fillers.
    T is inclusion-minimal but not minimum.
    """
    assert k >= 2
    z = ("z",)
    T = {("T", i) for i in range(t)}
    edges = []
    for i in range(t):
        A = {("T", i), z}
        for j in range(k - 2):
            A.add(("p", i, j))
        edges.append(frozenset(A))

    assert all(len(A) == k for A in edges)
    assert locally_two_coverable(edges, 7)
    assert tau(edges) == 1

    for i in range(t):
        assert edges[i] & T == {("T", i)}
        assert not all((T - {("T", i)}) & A for A in edges)

    return edges, T
```

A direct exhaustive search for very small \(n,k\) can record the smallest possible maximum private-edge degree over all minimum transversals and all private-edge choices:

```python
def best_private_load(edges):
    """
    Returns min over minimum T and private-edge choices
    of max_{v outside T} number of chosen private edges containing v.
    Exponential; intended only for very small examples.
    """
    best = None
    certificate = None

    for T in minimum_transversals(edges):
        opts = private_edge_options(edges, T)
        keys = list(T)

        for choice_tuple in product(*(opts[x] for x in keys)):
            chosen = dict(zip(keys, choice_tuple))
            d = audit_private_choice(edges, T, chosen)
            D = max(d.values(), default=0)
            if best is None or D < best:
                best = D
                certificate = (T, chosen, d)

    return best, certificate

def exhaustive_families(n, k, r=7):
    """
    Completely exhaustive only when binom(n,k) is tiny.
    Records admissible families and their transversal/private-load data.
    """
    V = list(range(n))
    candidates = [frozenset(A) for A in combinations(V, k)]
    records = []

    for mask in range(1, 1 << len(candidates)):
        edges = [
            candidates[i] for i in range(len(candidates))
            if (mask >> i) & 1
        ]
        if not locally_two_coverable(edges, r):
            continue

        t = tau(edges)
        load, cert = best_private_load(edges)
        records.append({
            "edges": edges,
            "tau": t,
            "ratio": t / k,
            "best_private_max_degree": load,
            "certificate": cert,
        })

    return records
```

The most informative computational experiment would be to enumerate or SAT-generate admissible families for \(k\le5\), then:

1. compute `best_private_load`;
2. classify every maximum-load vertex by the purge or exchange branch;
3. test whether repeated exchanges can cycle;
4. search for a potential function decreasing under either purge or exchange.

Such a potential function would be a concrete route toward completing Route 1.

## Route Diagnosis

Route 1 produced meaningful local structure, especially Lemma 6, but it is blocked at the concentration-management step. Seven private edges force external concentration, yet concentrated external vertices are compatible with local two-coverability. Global minimum transversality responds through blockers, but the exact response is another \(k\)-uniform \(7\)-locally 2-coverable subsystem with transversal number \(d\) or \(d-1\); there is no reduction in edge size and no known monotone charging budget. Standard Bollobás inequalities are much too coarse.

A fresh attempt should focus on the exchange graph of minimum transversals: choose a canonical minimum transversal and canonical private edges, then prove that high-load external vertices can be absorbed or purged with a strictly decreasing global potential. Reconstructing the EFKT proof for \(r=6\) is likely essential, since it may reveal the missing potential. Route 4 is currently only the dual reformulation of the same concentration problem, while Route 3 would additionally require an unproved near-integrality theorem.