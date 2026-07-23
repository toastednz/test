STATUS: BLOCKED

## Result

Using the hypergraph-transversal formulation, I prove a new elementary covering bound valid for every \(0<c<1\). If \(h=\lceil 1/c\rceil\), then
\[
M_c(n)\le \lfloor cn\rfloor-\frac12\left\lfloor\frac nh\right\rfloor+O(h),
\]
and hence
\[
M_c(n)\le \left(c-\frac1{2h}\right)n+O_c(1).
\]
At every reciprocal point \(c=1/h\), this matches the parity construction along odd \(n\):
\[
\boxed{\lim_{\substack{n\to\infty\\ n\ {\rm odd}}}\frac{M_{1/h}(n)}n=\frac1{2h}}.
\]
The proof uses two overlapping systems of complementary pairs, of sums \(\lfloor n/h\rfloor\) and \(\lfloor n/h\rfloor+1\). I also exhibit, for \(n=hN\) with fixed odd \(h\) and odd \(N\), an asymptotic integrality gap of factor \(h\) between the true transversal number and its standard fractional relaxation. Thus a purely fractional-transversal attack is decisively insufficient. The full all-\(n\), all-\(c\) problem remains blocked because the present argument leaves a linear tail uncontrolled when \(c\) lies strictly between consecutive reciprocals, and because no matching half-density construction is known for even targets at reciprocal points.

## Complete Argument

### 1. Hypergraph formulation

Let
\[
\mathcal H_{N,n}
=
\left([N],
\{S\subseteq[N]:\sigma(S)=n\}\right).
\]
A set \(A\subseteq[N]\) is admissible precisely when it is independent in \(\mathcal H_{N,n}\). Equivalently, \(C=[N]\setminus A\) is a transversal. Therefore
\[
M(N,n)=N-\tau(\mathcal H_{N,n}).
\]

The following covering lemma is the main result.

---

### 2. Mixed complementary-pair lemma

#### Lemma 1

Let \(h\ge2\), \(q\ge1\), \(0\le r<h\), and put
\[
T=hq+r.
\]
If \(B\subseteq[q]\) satisfies
\[
|B|>\frac q2+2h+2,
\]
then \(B\) contains a subset with sum \(T\).

#### Proof

Consider the two matchings on subsets of \([q]\):
\[
\mathcal Q_0
=
\bigl\{\{a,q-a\}:1\le a<q-a\bigr\},
\]
whose edges have sum \(q\), and
\[
\mathcal Q_1
=
\bigl\{\{a,q+1-a\}:1\le a<q+1-a\le q\bigr\},
\]
whose edges have sum \(q+1\).

For \(i=0,1\), let \(t_i\) be the number of edges in \(\mathcal Q_i\), let \(u_i=q-2t_i\) be the number of vertices not covered by that matching, and let \(f_i\) be the number of edges of \(\mathcal Q_i\) whose two endpoints both belong to \(B\).

A matching edge not fully contained in \(B\) contains at most one element of \(B\). Consequently,
\[
|B|\le t_i+f_i+u_i,
\]
and hence
\[
f_i\ge |B|-t_i-u_i.
\]

For \(\mathcal Q_0\), direct inspection gives
\[
t_0+u_0\le \frac q2+1.
\]
Indeed, if \(q=2k\), then \(t_0=k-1,u_0=2\); if \(q=2k+1\), then \(t_0=k,u_0=1\).

Similarly,
\[
t_1+u_1\le\frac q2+1.
\]
Therefore, under the assumed lower bound on \(|B|\),
\[
f_0>2h+1,\qquad f_1>2h+1.
\]

Choose \(h-r\) full edges from \(\mathcal Q_0\). These edges are mutually disjoint. Each chosen \(\mathcal Q_0\)-edge has two vertices and therefore intersects at most two edges of the matching \(\mathcal Q_1\). Thus the selected \(h-r\) edges eliminate at most \(2(h-r)\) full \(\mathcal Q_1\)-edges.

The number of full \(\mathcal Q_1\)-edges disjoint from all selected \(\mathcal Q_0\)-edges is therefore greater than
\[
2h+1-2(h-r)=2r+1\ge r.
\]
Choose \(r\) of them. All selected pairs are now mutually disjoint, and their union is a subset of \(B\) having sum
\[
(h-r)q+r(q+1)=hq+r=T.
\]
This proves the lemma. ∎

The constants are intentionally loose; only the \(O(h)\) error is relevant below.

---

### 3. A universal hypergraph upper bound

#### Theorem 2

Let \(N<n\), let \(h\ge2\), and set
\[
q=\left\lfloor\frac nh\right\rfloor.
\]
If \(q\le N\), then
\[
\boxed{
M(N,n)\le N-\frac q2+2h+2.
}
\]

#### Proof

Write
\[
n=hq+r,\qquad 0\le r<h.
\]
Let \(A\subseteq[N]\) be admissible, and put
\[
B=A\cap[q].
\]
Since \(q\le N\), at most \(N-q\) elements of \(A\) lie outside \([q]\), so
\[
|A|\le (N-q)+|B|.
\]

If \(|B|>q/2+2h+2\), Lemma 1 would give a subset of \(B\), and hence of \(A\), summing to \(n\). Thus
\[
|B|\le\frac q2+2h+2,
\]
and consequently
\[
|A|
\le
N-q+\frac q2+2h+2
=
N-\frac q2+2h+2.
\]
Taking the maximum over admissible \(A\) proves the theorem. ∎

#### Corollary 3

Fix \(0<c<1\), and define
\[
h=\left\lceil\frac1c\right\rceil.
\]
Then
\[
\boxed{
M_c(n)
\le
\lfloor cn\rfloor
-\frac12\left\lfloor\frac nh\right\rfloor
+2h+2.
}
\]
In particular,
\[
\boxed{
M_c(n)
\le
\left(c-\frac1{2h}\right)n+O_c(1).
}
\]

#### Proof

Since \(1/h\le c\),
\[
\left\lfloor\frac nh\right\rfloor\le\lfloor cn\rfloor.
\]
Apply Theorem 2 with \(N=\lfloor cn\rfloor\). ∎

For \(c>1/2\), the elementary pair bound from the brief additionally gives
\[
M_c(n)\le\frac n2+O(1).
\]
Thus in this range one may take the better of
\[
\frac12
\quad\text{and}\quad
c-\frac14
\]
as the upper coefficient.

---

### 4. Sharp asymptotics at reciprocal points along odd targets

#### Theorem 4

For every fixed integer \(h\ge2\),
\[
\boxed{
M_{1/h}(n)=\frac{n}{2h}+O_h(1)
\qquad(n\to\infty,\ n\text{ odd}).
}
\]
Equivalently,
\[
\boxed{
\lim_{\substack{n\to\infty\\ n\ {\rm odd}}}
\frac{M_{1/h}(n)}n
=
\frac1{2h}.
}
\]

#### Proof

Put
\[
N=\left\lfloor\frac nh\right\rfloor.
\]

For the lower bound, because \(n\) is odd, the set
\[
A=2\mathbb Z\cap[N]
\]
is admissible: every subset sum of \(A\) is even. Hence
\[
M_{1/h}(n)\ge\left\lfloor\frac N2\right\rfloor
=\frac{n}{2h}+O_h(1).
\]

For the upper bound, Corollary 3 with \(c=1/h\) gives
\[
M_{1/h}(n)
\le
N-\frac12\left\lfloor\frac nh\right\rfloor+2h+2
=
\frac N2+2h+2
=
\frac{n}{2h}+O_h(1).
\]
The two estimates match. ∎

This is a sharp first-order answer, but only on the odd subsequence and only for reciprocal \(c\).

---

### 5. Equal-sum blocks and integral amplification

The mechanism behind Theorem 2 is more general.

#### Lemma 5

Suppose \(d,h\ge1\), \(hd=n\), and
\[
B_1,\dots,B_t\subseteq[N]
\]
are pairwise disjoint sets, each satisfying
\[
\sigma(B_i)=d.
\]
If \(t\ge h\), then every transversal \(C\) of \(\mathcal H_{N,n}\) satisfies
\[
|C|\ge t-h+1.
\]
Equivalently,
\[
M(N,n)\le N-t+h-1.
\]

#### Proof

If \(C\) missed \(h\) of the blocks, say
\[
C\cap B_{i_1}=\cdots=C\cap B_{i_h}=\varnothing,
\]
then their pairwise disjoint union would be an edge of \(\mathcal H_{N,n}\), since its sum is
\[
hd=n.
\]
Thus at most \(h-1\) blocks can be missed by \(C\). At least \(t-h+1\) blocks are hit, and because the blocks are disjoint, hitting them requires at least \(t-h+1\) distinct vertices. ∎

For \(n=hN\), use the complementary pairs
\[
B_a=\{a,N-a\},
\qquad 1\le a<N-a.
\]
There are
\[
t=\left\lfloor\frac{N-1}{2}\right\rfloor
\]
such disjoint blocks, each of sum \(N\). Lemma 5 gives
\[
M(N,hN)
\le
N-\left\lfloor\frac{N-1}{2}\right\rfloor+h-1.
\]
If \(N\) is odd, this is
\[
M(N,hN)\le\frac{N-1}{2}+h.
\]

When \(h\) and \(N\) are both odd, \(hN\) is odd, so the even-number construction yields
\[
\frac{N-1}{2}
\le
M(N,hN)
\le
\frac{N-1}{2}+h.
\]

---

### 6. A factor-\(h\) integrality gap

Let \(\tau^*(\mathcal H_{N,n})\) denote the fractional transversal number. Its dual is the fractional matching problem:
\[
\max\sum_{E\in\mathcal H}w_E
\]
subject to
\[
w_E\ge0,\qquad
\sum_{E\ni a}w_E\le1
\quad(a\in[N]).
\]

Take \(n=hN\), and let
\[
t=\left\lfloor\frac{N-1}{2}\right\rfloor
\]
be the number of complementary pair blocks \(B_1,\dots,B_t\), each of sum \(N\).

Every union of \(h\) distinct blocks is a hyperedge. Give each such edge weight
\[
\binom{t-1}{h-1}^{-1}.
\]
A vertex lying in one of the pair blocks belongs to exactly
\[
\binom{t-1}{h-1}
\]
of these edges, so its total load is exactly \(1\). Vertices outside the pair blocks have load \(0\). This is therefore a feasible fractional matching of total weight
\[
\frac{\binom th}{\binom{t-1}{h-1}}
=
\frac th.
\]
Hence
\[
\tau^*(\mathcal H_{N,hN})\ge\frac th.
\]

On the other hand, the weights
\[
y_a=\frac{a}{n}
\]
form a feasible fractional transversal, because every hyperedge \(E\) satisfies
\[
\sum_{a\in E}y_a
=
\frac{\sigma(E)}n
=
1.
\]
Thus
\[
\tau^*(\mathcal H_{N,hN})
\le
\sum_{a=1}^N\frac{a}{hN}
=
\frac{N+1}{2h}.
\]
Therefore
\[
\boxed{
\frac1h\left\lfloor\frac{N-1}{2}\right\rfloor
\le
\tau^*(\mathcal H_{N,hN})
\le
\frac{N+1}{2h}.
}
\]

Now fix odd \(h\) and let \(N\to\infty\) through odd integers. The integral bound above and the parity construction give
\[
\left\lfloor\frac{N-1}{2}\right\rfloor-h+1
\le
\tau(\mathcal H_{N,hN})
\le
\frac{N+1}{2}.
\]
Consequently,
\[
\tau(\mathcal H_{N,hN})=\frac N2+O_h(1),
\qquad
\tau^*(\mathcal H_{N,hN})=\frac{N}{2h}+O_h(1),
\]
and hence
\[
\boxed{
\frac{\tau(\mathcal H_{N,hN})}
{\tau^*(\mathcal H_{N,hN})}
\longrightarrow h.
}
\]

Thus the basic fractional relaxation loses a factor \(h\), even at instances where the leading asymptotic of the integral problem is known.

---

### 7. Stability of the equal-sum-block subhypergraph

For \(n=hN\), retain only the hyperedges that are unions of \(h\) complementary pair blocks. Let \(C\) hit all these edges.

Write:

- \(f\): number of pair blocks disjoint from \(C\);
- \(e\): number of pair blocks containing both endpoints in \(C\);
- \(c_0\): number of elements of \(C\) outside all pair blocks.

The covering condition is exactly
\[
f\le h-1.
\]
Moreover,
\[
|C|=(t-f-e)+2e+c_0=t-f+e+c_0.
\]
Therefore
\[
|C|-(t-h+1)
=
(h-1-f)+e+c_0.
\]

In particular, if
\[
|C|\le t-h+1+s,
\]
then
\[
h-1-s\le f\le h-1,\qquad e\le s,\qquad c_0\le s.
\]
Thus a near-minimal transversal for this subhypergraph chooses one endpoint from almost every complementary pair and leaves approximately \(h-1\) pairs completely unhit.

However, the number of exact minimum transversals of this subhypergraph is
\[
\binom{t}{h-1}2^{\,t-h+1}.
\]
Indeed, choose the \(h-1\) unhit blocks, then choose one endpoint from every other block. This exponential family is the main stability obstruction: most such orientations need not hit the other partitions of \(n\).

### Ledger

**Proved:**

1. The mixed complementary-pair Lemma 1.
2. The universal upper bound
   \[
   M_c(n)\le\left(c-\frac1{2\lceil1/c\rceil}\right)n+O_c(1).
   \]
3. Sharp odd-subsequence asymptotics at every reciprocal \(c=1/h\).
4. A factor-\(h\) asymptotic integrality gap at \(n=hN\), for odd fixed \(h\) and odd \(N\).
5. Stability and exact enumeration of minimum transversals for the complementary-pair block subhypergraph.

**Plausible but unproved:**

1. Several shifted pair-block systems used simultaneously may control the linear tail left by Theorem 2.
2. At reciprocal \(c=1/h\), the even-\(n\) leading term may depend on arithmetic structure; no matching lower bound is proved.
3. Near-extremizers may be classifiable by orientations of several complementary-pair matchings, but one matching alone leaves exponentially many possibilities.

**Dead ends:**

1. Pure fractional-transversal or fractional-matching arguments: the factor-\(h\) gap proves they cannot reach the integral answer at reciprocal instances.
2. A single equal-sum block system away from reciprocal points: it leaves all vertices above \(\lfloor n/h\rfloor\) essentially uncharged.
3. Disjoint-edge matchings alone: they lose the integral amplification obtained by requiring the transversal to hit every union of \(h\) equal-sum blocks.

## Self-Audit

1. **The mixed-pair constant \(2h+2\) is loose.**  
   This does not affect any stated leading asymptotic. The proof explicitly counts full edges in two genuine matchings and then greedily chooses cross-disjoint pairs; there is no probabilistic or asymptotic step hidden in the argument.

2. **The sharp lower bound at \(c=1/h\) only applies to odd \(n\).**  
   This restriction is essential: the construction uses the parity obstruction. I have not inferred anything about even \(n\) beyond the universal upper bound.

3. **The LP obstruction only rules out the standard fractional relaxation, not all hypergraph methods.**  
   Entropy, containers, or a strong integral stability theorem could still succeed. The stated factor-\(h\) integrality gap is nevertheless rigorous and shows exactly why an LP-only implementation of Route 4 cannot solve the problem.

## Computations To Verify

The following code enumerates all distinct-part partitions, computes the exact optimum by MILP, computes the fractional transversal number, and checks the explicit constructions.

```python
from itertools import combinations
from math import floor, ceil, comb
import numpy as np
from scipy.optimize import milp, linprog, Bounds, LinearConstraint
from scipy.sparse import csr_matrix

def distinct_partitions(n, N):
    """All increasing tuples from [N] with sum n."""
    out = []

    def rec(lo, rem, cur):
        if rem == 0:
            out.append(tuple(cur))
            return
        hi = min(N, rem)
        for a in range(lo, hi + 1):
            cur.append(a)
            rec(a + 1, rem - a, cur)
            cur.pop()

    rec(1, n, [])
    return out

def incidence_matrix(edges, N):
    rows, cols, data = [], [], []
    for i, E in enumerate(edges):
        for a in E:
            rows.append(i)
            cols.append(a - 1)
            data.append(1.0)
    return csr_matrix((data, (rows, cols)),
                      shape=(len(edges), N))

def exact_M(N, n):
    edges = distinct_partitions(n, N)
    A = incidence_matrix(edges, N)
    ub = np.array([len(E) - 1 for E in edges], dtype=float)
    con = LinearConstraint(A, -np.inf, ub)

    res = milp(
        c=-np.ones(N),
        integrality=np.ones(N),
        bounds=Bounds(np.zeros(N), np.ones(N)),
        constraints=con,
        options={"time_limit": 600}
    )
    if not res.success:
        raise RuntimeError(res.message)
    return int(round(-res.fun)), res.x

def fractional_tau(N, n):
    edges = distinct_partitions(n, N)
    A = incidence_matrix(edges, N)
    # Minimize sum y_a subject to A y >= 1 and y_a >= 0.
    res = linprog(
        c=np.ones(N),
        A_ub=-A,
        b_ub=-np.ones(len(edges)),
        bounds=[(0, None)] * N,
        method="highs"
    )
    if not res.success:
        raise RuntimeError(res.message)
    return res.fun, res.x

def avoids_target(A, n):
    bits = 1
    mask = (1 << (n + 1)) - 1
    for a in sorted(A):
        bits |= bits << a
        bits &= mask
    return ((bits >> n) & 1) == 0

def mixed_pair_bound(N, n, h):
    q = n // h
    assert q <= N
    return N - q / 2 + 2 * h + 2

def pair_matchings(q):
    Q0 = [(a, q - a)
          for a in range(1, q)
          if a < q - a]
    Q1 = [(a, q + 1 - a)
          for a in range(1, q + 1)
          if a < q + 1 - a <= q]
    return Q0, Q1

def verify_mixed_pair_lemma(q, h, r):
    """
    Exhaustive verification, practical only for q <= about 25.
    """
    target = h * q + r
    threshold = q / 2 + 2 * h + 2

    for mask in range(1 << q):
        if mask.bit_count() <= threshold:
            continue
        B = [a + 1 for a in range(q) if (mask >> a) & 1]
        assert not avoids_target(B, target), (q, h, r, B)

def reciprocal_block_check(h, N):
    n = h * N
    blocks = [(a, N - a)
              for a in range(1, N)
              if a < N - a]
    t = len(blocks)
    assert t == floor((N - 1) / 2)

    # Verify all h-block unions are partitions of n for small t.
    if t <= 20 and t >= h:
        for J in combinations(range(t), h):
            E = []
            for j in J:
                E.extend(blocks[j])
            assert len(E) == len(set(E)) == 2 * h
            assert sum(E) == n

    integral_tau_lower = t - h + 1
    fractional_lower = t / h
    fractional_upper = (N + 1) / (2 * h)

    return {
        "N": N,
        "n": n,
        "t": t,
        "integral_tau_lower": integral_tau_lower,
        "fractional_tau_lower": fractional_lower,
        "fractional_tau_upper": fractional_upper,
    }

def test_odd_reciprocal_instances():
    for h in range(2, 8):
        for n in range(21, 101, 2):
            N = n // h
            if N == 0:
                continue
            evens = list(range(2, N + 1, 2))
            assert avoids_target(evens, n)

            upper = mixed_pair_bound(N, n, h)
            assert len(evens) <= upper + 1e-9

def compare_exact_and_fractional():
    """
    Keep N modest: partition enumeration grows quickly.
    """
    for h in (3, 5):
        for N in range(2 * h + 1, 18, 2):  # odd N
            n = h * N
            M, x = exact_M(N, n)
            tau = N - M
            tau_star, y = fractional_tau(N, n)

            formulas = reciprocal_block_check(h, N)
            assert tau >= formulas["integral_tau_lower"] - 1e-7
            assert tau_star >= formulas["fractional_tau_lower"] - 1e-7
            assert tau_star <= formulas["fractional_tau_upper"] + 1e-7

            evens = list(range(2, N + 1, 2))
            assert avoids_target(evens, n)
            assert M >= len(evens)

            print({
                "h": h,
                "N": N,
                "n": n,
                "M": M,
                "tau": tau,
                "tau_star": tau_star,
                "gap_ratio": tau / tau_star,
                "predicted_limit": h
            })
```

Particularly useful finite experiments are:

1. Determine whether \(M(N,hN)=\lfloor N/2\rfloor\) eventually for odd \(h,N\), or whether the \(O(h)\) slack is genuinely attained.
2. For \(c=1/h\) and even \(n\), compare \(M_c(n)/n\) across highly divisible, prime-power, and semiprime targets.
3. For \(1/h<c<1/(h-1)\), inspect whether extremizers use the uncontrolled tail \((\lfloor n/h\rfloor,N]\), and whether adding shifted complementary-pair systems closes the gap.

## Route Diagnosis

The successful hypergraph idea was not a large matching of partitions of \(n\), but an overlapping family: construct many pair blocks of sums \(q\) and \(q+1\), and observe that every suitable union of \(h\) blocks is an edge. This amplifies a fractional requirement into an integral one and yields a linear transversal bound.

The route is blocked in two precise places:

1. If
   \[
   \frac1h<c<\frac1{h-1},
   \]
   the theorem controls only \([\,\lfloor n/h\rfloor\,]\) and leaves a tail of length
   \[
   \left(c-\frac1h\right)n+O(1).
   \]
   For odd \(n\), this produces the remaining leading-order gap
   \[
   \frac12\left(c-\frac1h\right)n.
   \]

2. Near-minimal transversals of a single pair-block system admit exponentially many orientations. Determining which orientations also meet every other partition of \(n\) is another dense subset-sum problem of comparable strength.

A fresh attempt should use several overlapping block systems simultaneously—especially shifted pairings and partitions involving one tail vertex together with complementary pairs. The natural auxiliary problem is to prove a simultaneous stability theorem for these pair-matchings. Pure LP or fractional matching should not be pursued further without an additional integral amplification mechanism, because the explicit factor-\(h\) integrality gap rules it out.