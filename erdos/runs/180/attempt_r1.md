STATUS: SOLVED-DISPROOF

## Result

Under the stated conventions—ordinary non-induced subgraph containment, with disconnected forbidden graphs allowed—the universal assertion is false. The finite family
\[
\mathcal F=\{P_3,2K_2\}
\]
satisfies \(\operatorname{ex}(n;\mathcal F)=1\) for every \(n\ge2\), while
\[
\operatorname{ex}(n;P_3)=\left\lfloor\frac n2\right\rfloor
\quad\text{and}\quad
\operatorname{ex}(n;2K_2)=n-1\quad(n\ge4).
\]
Thus neither member of \(\mathcal F\) has singleton extremal number within a constant factor of the joint extremal number.

## Complete Argument

Let \(P_3\) denote the path with two edges and three vertices, and let \(2K_2\) denote two vertex-disjoint edges. Set
\[
\mathcal F=\{P_3,2K_2\}.
\]
This is a finite, nonempty family of finite graphs, each having at least one edge.

### 1. The joint extremal number

We first characterize \(P_3\)-free graphs.

**Lemma 1.** A graph \(X\) is \(P_3\)-free if and only if \(\Delta(X)\le1\).

**Proof.** If some vertex \(v\) has two distinct neighbors \(u,w\), then the edges \(uv\) and \(vw\) form a copy of \(P_3\). The possible presence of the edge \(uw\) is irrelevant because containment is not required to be induced.

Conversely, every copy of \(P_3\) has a middle vertex incident with two distinct edges, so its presence forces a vertex of degree at least two. Hence \(X\) is \(P_3\)-free exactly when \(\Delta(X)\le1\). \(\square\)

Consequently, every \(P_3\)-free graph is a matching together with isolated vertices. If it is also \(2K_2\)-free, that matching has size at most one. Thus every \(\mathcal F\)-free graph has at most one edge.

For every \(n\ge2\), the graph consisting of one edge and \(n-2\) isolated vertices contains neither \(P_3\) nor \(2K_2\). Therefore
\[
\boxed{\operatorname{ex}(n;\mathcal F)=1\qquad(n\ge2).}
\]

In particular, the denominator in the desired comparison is positive and constant, so no convention concerning division by zero is involved.

### 2. The singleton extremal number for \(P_3\)

By Lemma 1, a \(P_3\)-free graph has maximum degree at most one. The degree-sum formula gives
\[
2e(X)=\sum_{v\in V(X)}\deg(v)\le n,
\]
and hence
\[
e(X)\le\left\lfloor\frac n2\right\rfloor.
\]
A matching of size \(\lfloor n/2\rfloor\) attains this bound and is \(P_3\)-free. Therefore
\[
\boxed{\operatorname{ex}(n;P_3)=\left\lfloor\frac n2\right\rfloor.}
\]

### 3. The singleton extremal number for \(2K_2\)

A graph is \(2K_2\)-free exactly when every two of its edges intersect.

We use the following elementary classification.

**Lemma 2.** If every two edges of a graph \(X\) intersect, then either all edges of \(X\) share a common vertex, or \(X\) has at most the three edges of a triangle.

**Proof.** The assertion is immediate if \(X\) has at most one edge. Otherwise choose two distinct edges. Since they intersect, label them \(ab\) and \(ac\).

If every edge contains \(a\), all edges have the common endpoint \(a\).

Otherwise, let \(e\) be an edge not containing \(a\). To intersect both \(ab\) and \(ac\), it must be the edge \(bc\). Once \(bc\) is present, any edge containing \(a\) must also intersect \(bc\), so it can only be \(ab\) or \(ac\). Any edge not containing \(a\) that intersects both \(ab\) and \(ac\) can only be \(bc\). Hence all edges lie in the triangle on \(\{a,b,c\}\). \(\square\)

It follows that an \(n\)-vertex \(2K_2\)-free graph has at most
\[
\max\{n-1,3\}
\]
edges. Both possibilities are attained: a full star has \(n-1\) edges, and for \(n\ge3\), a triangle together with isolated vertices has three edges. Consequently,
\[
\operatorname{ex}(n;2K_2)=
\begin{cases}
0,&n=1,\\
1,&n=2,\\
3,&n=3,\\
n-1,&n\ge4.
\end{cases}
\]

In particular,
\[
\boxed{\operatorname{ex}(n;2K_2)=n-1\qquad(n\ge4).}
\]

### 4. Failure of every possible controlling member

For \(n\ge4\),
\[
\frac{\operatorname{ex}(n;P_3)}
{\operatorname{ex}(n;\mathcal F)}
=
\left\lfloor\frac n2\right\rfloor
\longrightarrow\infty,
\]
and
\[
\frac{\operatorname{ex}(n;2K_2)}
{\operatorname{ex}(n;\mathcal F)}
=
n-1
\longrightarrow\infty.
\]

Thus, for each \(G\in\mathcal F\) and every constant \(C>0\), there are arbitrarily large \(n\) such that
\[
\operatorname{ex}(n;G)>
C\,\operatorname{ex}(n;\mathcal F).
\]
No fixed member \(G\in\mathcal F\) can satisfy the proposed \(O_{\mathcal F}\)-comparison. This disproves the universal assertion.

## Self-Audit

1. **Dependence on the containment convention.**  
   The equivalence “\(P_3\)-free iff \(\Delta\le1\)” would fail for induced containment, since a triangle has no induced \(P_3\). It holds here because the brief explicitly specifies ordinary non-induced subgraphs.

2. **Classification of \(2K_2\)-free graphs.**  
   The triangle exception is easy to overlook. Lemma 2 includes it explicitly: after choosing intersecting edges \(ab,ac\), the only edge avoiding their common endpoint is \(bc\), and its presence prevents every further edge outside that triangle.

3. **Asymptotic quantifiers.**  
   The conclusion requires ruling out every constant and every sufficiently-large-\(n\) threshold. This is justified because both displayed ratios tend to infinity, not merely because they exceed a constant at selected small values.

## Computations To Verify

The following exhaustive search verifies the exact extremal values for all \(n\le6\). Increasing `MAX_N` to \(7\) is feasible but substantially slower in pure Python.

```python
from itertools import combinations

def brute_extremal(n):
    possible_edges = list(combinations(range(n), 2))
    m = len(possible_edges)

    best_P3 = -1
    best_2K2 = -1
    best_both = -1

    for mask in range(1 << m):
        selected = [
            possible_edges[i]
            for i in range(m)
            if (mask >> i) & 1
        ]
        edge_count = len(selected)

        # Direct test for a non-induced P3:
        # some vertex is incident with two selected edges.
        degrees = [0] * n
        for u, v in selected:
            degrees[u] += 1
            degrees[v] += 1
        has_P3 = any(d >= 2 for d in degrees)

        # Direct test for 2K2: two selected edges with disjoint endpoints.
        has_2K2 = any(
            len({a, b, c, d}) == 4
            for (a, b), (c, d) in combinations(selected, 2)
        )

        if not has_P3:
            best_P3 = max(best_P3, edge_count)
        if not has_2K2:
            best_2K2 = max(best_2K2, edge_count)
        if not has_P3 and not has_2K2:
            best_both = max(best_both, edge_count)

    return best_P3, best_2K2, best_both


MAX_N = 6
results = []

for n in range(1, MAX_N + 1):
    p3, m2, both = brute_extremal(n)

    expected_p3 = n // 2
    expected_m2 = {1: 0, 2: 1, 3: 3}.get(n, n - 1)
    expected_both = 0 if n == 1 else 1

    assert p3 == expected_p3, (n, p3, expected_p3)
    assert m2 == expected_m2, (n, m2, expected_m2)
    assert both == expected_both, (n, both, expected_both)

    results.append((n, p3, m2, both))

print("n, ex(n;P3), ex(n;2K2), ex(n;{P3,2K2})")
for row in results:
    print(row)
```

Expected output:

```text
n, ex(n;P3), ex(n;2K2), ex(n;{P3,2K2})
(1, 0, 0, 0)
(2, 1, 1, 1)
(3, 1, 3, 1)
(4, 2, 3, 1)
(5, 2, 4, 1)
(6, 3, 5, 1)
```

## Route Diagnosis

Route 1 succeeds completely. The decisive interaction is that forbidding \(P_3\) forces all edges to form a matching, while forbidding \(2K_2\) then restricts that matching to one edge. Individually, however, each forbidden graph permits linearly many edges.

**Ledger:**

- **Proved:** \(P_3\)-free graphs are exactly graphs of maximum degree at most one.
- **Proved:** \(\operatorname{ex}(n;\{P_3,2K_2\})=1\) for \(n\ge2\).
- **Proved:** \(\operatorname{ex}(n;P_3)=\lfloor n/2\rfloor\).
- **Proved:** the exact formula for \(\operatorname{ex}(n;2K_2)\).
- **Plausible but unproved claims used:** none.
- **Dead ends or blocks:** none.

A connected-family or unbounded-joint-extremal-number variant would be a different problem and is not addressed by this counterexample. Under the literal formulation supplied, no alternative route is needed.