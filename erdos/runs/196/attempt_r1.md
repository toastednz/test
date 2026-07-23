STATUS: BLOCKED

## Result

I did not solve Erdős Problem #196. Route 1 yields exact lower bounds on the number and type of local extrema required in every finite value interval, together with rank-sensitive upper bounds on how many constraints one vertex can witness. However, these bounds do not approach a contradiction. The decisive obstruction is an explicit least-significant-bit lexicographic total order on \(\mathbb N\) in which the midpoint of every three-term arithmetic progression is a local extremum. Consequently, every finite restriction avoids even monotone three-term progressions, so no argument based only on a single finite interval and its induced ranks can work. Exploiting order type \(\omega\) would require a genuinely multiscale estimate involving the global ranks \(p(n)\); the elementary rank-moment estimates are far too weak, and bijectivity supplies no useful upper bound for them.

## Complete Argument

### 1. The finite local-extrema ledger

Let \(\rho:[N]\to[N]\) be the rank function of an arbitrary linear order on \([N]\). Thus
\[
\rho(u)<\rho(v)
\]
means that \(u\) occurs before \(v\).

For \(d\ge1\) and \(d<n\le N-d\), call \((n,d)\)

- a local maximum if
  \[
  \rho(n)>\rho(n-d),\qquad \rho(n)>\rho(n+d);
  \]
- a local minimum if both inequalities are reversed;
- a local extremum if it is either.

Fix \(d\), and partition \([N]\) into the residue-class paths
\[
r,r+d,r+2d,\dots,\qquad 1\le r\le d.
\]
If a path has vertices \(v_0,\dots,v_{L-1}\), let
\[
s_i=\operatorname{sgn}\bigl(\rho(v_{i+1})-\rho(v_i)\bigr),
\qquad 0\le i<L-1.
\]

If the order avoids monotone four-term arithmetic progressions, then no three consecutive \(s_i\)'s are equal.

#### Lemma 1: Required number of extrema on one path

Define
\[
H(L)=\max\left(0,\left\lfloor\frac{L-2}{2}\right\rfloor\right),
\qquad
G(L)=\left\lfloor\frac{H(L)}2\right\rfloor.
\]
On every length-\(L\) path in an avoiding order:

1. there are at least \(H(L)\) local extrema;
2. there are at least \(G(L)\) local maxima;
3. there are at least \(G(L)\) local minima.

#### Proof

The sign word has length \(m=L-1\). If it has \(C\) sign changes, it is partitioned into \(C+1\) constant runs. Every run has length at most two, so
\[
m\le 2(C+1).
\]
Therefore
\[
C\ge \left\lceil\frac m2\right\rceil-1
 =\left\lfloor\frac{m-1}{2}\right\rfloor
 =\left\lfloor\frac{L-2}{2}\right\rfloor.
\]
Each sign change is precisely a local extremum.

The two possible transition types are
\[
+\to- \quad\text{and}\quad -\to+,
\]
corresponding respectively to a local maximum and a local minimum. Successive transitions alternate in type. Hence each type occurs at least \(\lfloor C/2\rfloor\) times, which is at least \(G(L)\). ∎

Write
\[
N=q_dd+s_d,\qquad 0\le s_d<d.
\]
There are \(s_d\) residue paths of length \(q_d+1\) and \(d-s_d\) paths of length \(q_d\). Consequently, if \(E_d,M_d,m_d\) denote respectively the numbers of local extrema, maxima, and minima in direction \(d\), then
\[
E_d\ge
s_dH(q_d+1)+(d-s_d)H(q_d),
\]
and
\[
M_d,m_d\ge
s_dG(q_d+1)+(d-s_d)G(q_d).
\]

These are sharp at the level of abstract sign words.

---

### 2. Exact progression-extremum incidence count

The number of four-term arithmetic progressions in \([N]\) is
\[
Q_N=\sum_{d=1}^{\lfloor (N-1)/3\rfloor}(N-3d).
\]

For a local extremum \((n,d)\), define its multiplicity
\[
\mu_N(n,d)
 =
 \mathbf 1_{\,n+2d\le N}
 +
 \mathbf 1_{\,n-2d\ge1}.
\]
The first indicator says that \(n\) can be the first internal term of
\[
n-d,n,n+d,n+2d,
\]
and the second says it can be the second internal term of
\[
n-2d,n-d,n,n+d.
\]

Let \(e_N(n,d)\) be the indicator that \((n,d)\) is a local extremum, and put
\[
I_N=\sum_{n,d}e_N(n,d)\mu_N(n,d).
\]

#### Lemma 2: Incidence identity

For every order on \([N]\),
\[
I_N=\sum_P \bigl(\text{number of internal local extrema of }P\bigr),
\]
where \(P\) ranges over all four-term arithmetic progressions in \([N]\).

In particular, an avoiding order satisfies
\[
Q_N\le I_N\le 2Q_N.
\]

#### Proof

A progression
\[
P=(a,a+d,a+2d,a+3d)
\]
has exactly two possible internal extrema, at \(a+d\) and \(a+2d\). The multiplicity definition counts exactly these two incidences. The progression is monotone precisely when neither internal term is a local extremum. Thus an avoiding progression contributes either one or two to \(I_N\), proving the inequalities. ∎

This already diagnoses the failure of naive counting: one extremum can witness two adjacent progressions, and there is room for all constraints to have two witnesses.

---

### 3. Rank-sensitive capacity bounds

Let
\[
D_n=\min(n-1,N-n).
\]
There are \(D_n\) possible symmetric pairs
\[
\{n-d,n+d\}\subseteq[N].
\]
For different \(d\), these endpoint pairs are disjoint.

#### Lemma 3: Unweighted rank capacity

If \(r=\rho(n)\), then
\[
\#\{\text{local-maximum directions at }n\}
 \le \min\left(D_n,\left\lfloor\frac{r-1}{2}\right\rfloor\right),
\]
and
\[
\#\{\text{local-minimum directions at }n\}
 \le \min\left(D_n,\left\lfloor\frac{N-r}{2}\right\rfloor\right).
\]

#### Proof

Each local-maximum direction consumes two distinct vertices preceding \(n\). There are \(r-1\) such vertices, and endpoint pairs belonging to different directions are disjoint. Hence there can be at most \(\lfloor(r-1)/2\rfloor\) such directions. The proof for minima is identical using the \(N-r\) later vertices. ∎

There is also a weighted version adapted to \(\mu_N\). Put
\[
A_n=\left\lfloor\frac{D_n}{2}\right\rfloor,
\]
and
\[
B_n=
\min\left(
D_n,
\max\left(
\left\lfloor\frac{n-1}{2}\right\rfloor,
\left\lfloor\frac{N-n}{2}\right\rfloor
\right)
\right).
\]
Among directions \(1\le d\le D_n\),

- the first \(A_n\) have \(\mu_N(n,d)=2\);
- the next \(B_n-A_n\) have \(\mu_N(n,d)=1\);
- the remaining directions have multiplicity zero.

Define
\[
W_n(k)
 =
2\min(k,A_n)
+\min\bigl(\max(k-A_n,0),B_n-A_n\bigr).
\]
This is the largest total multiplicity obtainable from at most \(k\) directions.

It follows from Lemma 3 that
\[
I_N\le
\sum_{n=1}^N
\left[
 W_n\!\left(\min\left(D_n,\left\lfloor\frac{\rho(n)-1}{2}\right\rfloor\right)\right)
+
 W_n\!\left(\min\left(D_n,\left\lfloor\frac{N-\rho(n)}{2}\right\rfloor\right)\right)
\right].
\]
This is a valid rank-sensitive upper bound, but it is not small enough to contradict \(I_N\ge Q_N\).

---

### 4. Separate lower bounds for maxima and minima

The preceding path argument also forces quadratically many extrema of each type.

For every integer \(L\ge1\),
\[
G(L)\ge \frac{L-5}{4}.
\]
Indeed, for \(L\ge2\),
\[
G(L)=\max\left(0,\left\lfloor\frac{L-2}{4}\right\rfloor\right),
\]
and the displayed inequality follows by checking \(L\bmod 4\); it is immediate for \(L=1\).

Let
\[
m=\left\lfloor\frac{N-1}{5}\right\rfloor.
\]
For each \(1\le d\le m\), summing over all \(d\) residue paths gives
\[
M_d,m_d
 \ge \sum_{r=1}^d \frac{L_{r,d}-5}{4}
 =\frac{N-5d}{4}.
\]
Therefore every avoiding order satisfies
\[
M_N,m_N
\ge
\frac14\left(
mN-\frac{5m(m+1)}2
\right)
=
\frac{N^2}{40}+O(N),
\]
where \(M_N,m_N\) count all local maxima and minima, respectively, in symmetric triples contained in \([N]\).

For an actual permutation rank function \(p\), a local maximum at \(n\) uses two of the \(p(n)-1\) global predecessors of \(n\). Hence the following is a necessary condition for a counterexample:
\[
\boxed{
\sum_{n=1}^N
\min\left(
D_n,\left\lfloor\frac{p(n)-1}{2}\right\rfloor
\right)
\ge
\frac14\left(
mN-\frac{5m(m+1)}2
\right).
}
\]

Unfortunately, after discarding the minimum, this yields only
\[
\sum_{n=1}^N p(n)\ge \frac{N^2}{20}+O(N),
\]
whereas distinctness alone gives the much stronger bound
\[
\sum_{n=1}^N p(n)\ge \frac{N(N+1)}2.
\]
Thus the basic rank-capacity estimate does not extract meaningful information from bijectivity.

---

### 5. A decisive obstruction to finite local counting

Define a total order \(\prec\) on the positive integers as follows. Write
\[
n=\sum_{j\ge0}b_j(n)2^j,\qquad b_j(n)\in\{0,1\}.
\]
For distinct \(u,v\), let
\[
k=\min\{j:b_j(u)\ne b_j(v)\}.
\]
Set
\[
u\prec v\quad\Longleftrightarrow\quad b_k(u)<b_k(v).
\]
This is lexicographic order starting from the least significant bit.

It is a total order. For transitivity, suppose \(u\prec v\) and \(v\prec w\), and let \(i,j\) be the respective first differing bit positions. If \(i<j\), then \(u\) and \(w\) first differ at \(i\), with bit pattern \(0,1\), so \(u\prec w\). The case \(j<i\) is symmetric. The case \(i=j\) is impossible, because it would require the bit of \(v\) at that position to be simultaneously \(1\) and \(0\).

#### Lemma 4: Every three-term arithmetic progression turns in \(\prec\)

For every \(a,d\ge1\), the middle element \(a+d\) is either earlier than both \(a,a+2d\), or later than both.

#### Proof

Let
\[
k=\nu_2(d).
\]
Modulo \(2^{k+1}\), adding \(d\) preserves the bits below \(k\) and flips the \(k\)-th bit. Adding \(2d\) preserves all bits through position \(k\). Therefore:

- \(a,a+d,a+2d\) have identical bits below \(k\);
- \(a\) and \(a+2d\) have the same \(k\)-th bit;
- \(a+d\) has the opposite \(k\)-th bit.

Thus, in least-significant-bit lexicographic order, both endpoints are on the same side of the middle term. ∎

Consequently:

1. \(\prec\) contains no monotone three-term arithmetic progression.
2. Its restriction to every finite \([N]\) contains no monotone three-term progression, hence no monotone four-term progression.
3. Every symmetric three-term progression has its midpoint as a local extremum.
4. For every four-term progression, both internal terms are local extrema, so
   \[
   I_N=2Q_N
   \]
   in every finite restriction.

This proves that there is no finite forcing threshold \(N\) for the problem. More importantly for Route 1, any estimate using only one finite interval, its induced ranks, and its local extrema must be compatible with an order in which every possible symmetric triple is extremal.

The order \(\prec\) is not the order of a permutation sequence. For any \(n\ge1\), choose a bit position \(h\) with \(b_h(n)=1\). For every \(H>h\), put
\[
m_H=(n\bmod 2^h)+2^H.
\]
Then \(m_H\) agrees with \(n\) below bit \(h\), has bit \(0\) at \(h\), and hence
\[
m_H\prec n.
\]
Thus every positive integer has infinitely many predecessors in \(\prec\). By contrast, in a permutation order each \(n\) has exactly \(p(n)-1\) predecessors.

The entire unresolved difficulty is therefore concentrated in converting the finite-predecessor condition into a quantitative obstruction.

---

### 6. Bijections have no useful upper rank-moment bound

One possible closure of the preceding inequalities would require an upper bound on
\[
\sum_{n\le N}p(n)
\]
along some sufficiently useful sequence of \(N\). No such elementary upper bound follows from bijectivity.

Let
\[
B=\{2^k:k\ge1\},\qquad A=\mathbb N\setminus B,
\]
and enumerate
\[
A=\{a_1<a_2<\cdots\}.
\]
Define an involution \(p\) by
\[
p(a_k)=2^k,\qquad p(2^k)=a_k.
\]
The disjoint pairs \(\{a_k,2^k\}\) partition \(\mathbb N\), so this is a bijection.

If
\[
K_N=|A\cap[N]|=N-\lfloor\log_2N\rfloor,
\]
then
\[
\sum_{n\le N}p(n)
\ge \sum_{k=1}^{K_N}2^k
=2^{K_N+1}-2.
\]
Thus even superpolynomial rank moments on every large prefix are consistent with bijectivity. This example is not claimed to avoid monotone four-term progressions; it shows only that a Route 1 argument cannot close by combining its rank lower bound with a general moment upper bound for permutations.

---

### 7. Check of the priority-construction alternative

A natural alternative was the proposed repair lemma:

> Given an avoiding prefix and an omitted target \(y\), append safe buffers until \(y\) can be appended.

This is false in the strongest possible way.

If \(y\) is already unsafe, it remains unsafe after every extension not containing \(y\). The witnessing three earlier values retain their relative order, and all remain earlier than \(y\) when \(y\) is eventually appended.

For example, the prefix
\[
1,2,3
\]
avoids four-term progressions, but \(4\) can never subsequently be appended: whenever it appears, the progression
\[
1,2,3,4
\]
will occur in increasing order. Thus append-only buffers cannot repair a postponed target.

## Self-Audit

1. **The bounds \(H(L)\) and \(G(L)\) are floor-sensitive.**  
   An off-by-one error here would alter the constants. The proof via constant sign runs and alternating transition types covers all path lengths, and the supplied code checks the formulas exhaustively on tested orders.

2. **The weighted capacity \(W_n(k)\) is not claimed to be optimal.**  
   It separately maximizes the maximum and minimum directions and therefore may overcount because those sets must be disjoint. This only makes it a weaker upper bound; it cannot invalidate the stated inequality. Improving this local optimization cannot by itself overcome the least-significant-bit finite orders.

3. **The diagnosis does not rule out every conceivable weighted-extrema argument.**  
   The explicit obstruction rules out finite-interval arguments and the involution rules out closure through general rank moments, but a sophisticated multiscale inequality coupling many \((N,T)\) rectangles in the permutation plot might still succeed. This is why the status is BLOCKED rather than a claim that Route 1 is impossible in principle.

## Computations To Verify

```python
def ap_violations(order, length):
    """order must be a permutation of [N]."""
    N = len(order)
    assert set(order) == set(range(1, N + 1))
    pos = {v: i for i, v in enumerate(order)}
    out = []
    max_d = (N - 1) // (length - 1)
    for d in range(1, max_d + 1):
        for a in range(1, N - (length - 1) * d + 1):
            vals = [a + j * d for j in range(length)]
            ranks = [pos[v] for v in vals]
            inc = all(ranks[i] < ranks[i + 1]
                      for i in range(length - 1))
            dec = all(ranks[i] > ranks[i + 1]
                      for i in range(length - 1))
            if inc or dec:
                out.append((a, d, vals, ranks))
    return out


def lsb_lex_order(N):
    """Restriction of least-significant-bit lexicographic order to [N]."""
    H = N.bit_length() + 1
    return sorted(
        range(1, N + 1),
        key=lambda n: tuple((n >> j) & 1 for j in range(H))
    )


# Verify that every finite restriction avoids monotone 3-APs and 4-APs.
for N in range(1, 501):
    order = lsb_lex_order(N)
    assert not ap_violations(order, 3)
    assert not ap_violations(order, 4)


def Hfun(L):
    return max(0, (L - 2) // 2)


def Gfun(L):
    return Hfun(L) // 2


def top_weight(k, A, B):
    return 2 * min(k, A) + min(max(k - A, 0), B - A)


def extrema_ledger(order):
    N = len(order)
    assert set(order) == set(range(1, N + 1))
    rho = {v: i + 1 for i, v in enumerate(order)}

    max_count = [0] * (N + 1)
    min_count = [0] * (N + 1)
    max_weight = [0] * (N + 1)
    min_weight = [0] * (N + 1)

    I = 0
    Q = sum(N - 3 * d for d in range(1, (N - 1) // 3 + 1))

    # Enumerate all symmetric triples.
    for d in range(1, (N - 1) // 2 + 1):
        for n in range(d + 1, N - d + 1):
            is_max = rho[n] > rho[n - d] and rho[n] > rho[n + d]
            is_min = rho[n] < rho[n - d] and rho[n] < rho[n + d]

            mu = int(n + 2 * d <= N) + int(n - 2 * d >= 1)

            if is_max:
                max_count[n] += 1
                max_weight[n] += mu
                I += mu
            elif is_min:
                min_count[n] += 1
                min_weight[n] += mu
                I += mu

    # Verify all rank-capacity inequalities.
    for n in range(1, N + 1):
        D = min(n - 1, N - n)
        r = rho[n]

        kmax = min(D, (r - 1) // 2)
        kmin = min(D, (N - r) // 2)

        assert max_count[n] <= kmax
        assert min_count[n] <= kmin

        A = D // 2
        B = min(
            D,
            max((n - 1) // 2, (N - n) // 2)
        )
        assert max_weight[n] <= top_weight(kmax, A, B)
        assert min_weight[n] <= top_weight(kmin, A, B)

    avoids4 = not ap_violations(order, 4)

    # Verify the pathwise H and G lower bounds.
    if avoids4:
        for d in range(1, (N - 1) // 3 + 1):
            for r in range(1, d + 1):
                vals = list(range(r, N + 1, d))
                signs = [
                    1 if rho[vals[i + 1]] > rho[vals[i]] else -1
                    for i in range(len(vals) - 1)
                ]

                # No constant block of three signs.
                for i in range(len(signs) - 2):
                    assert not (
                        signs[i] == signs[i + 1] == signs[i + 2]
                    )

                mx = 0
                mn = 0
                for i in range(len(signs) - 1):
                    if signs[i] == 1 and signs[i + 1] == -1:
                        mx += 1
                    elif signs[i] == -1 and signs[i + 1] == 1:
                        mn += 1

                L = len(vals)
                assert mx + mn >= Hfun(L)
                assert mx >= Gfun(L)
                assert mn >= Gfun(L)

        assert Q <= I <= 2 * Q

    return {
        "N": N,
        "Q": Q,
        "I": I,
        "max_count": sum(max_count),
        "min_count": sum(min_count),
    }


# In the LSB order every symmetric triple should be extremal,
# hence every 4-AP has both internal terms extremal: I = 2Q.
for N in range(4, 201):
    data = extrema_ledger(lsb_lex_order(N))
    assert data["I"] == 2 * data["Q"]


def is_B_power(n):
    return n >= 2 and (n & (n - 1)) == 0


def transposition_moment(N):
    """
    Computes sum_{n <= N} p(n) for:
      p(a_k)=2^k, p(2^k)=a_k,
    where a_k enumerates positive non-powers of two
    and powers begin with 2=2^1.
    """
    A = [v for v in range(1, N + 1) if not is_B_power(v)]
    a_index = {v: k + 1 for k, v in enumerate(A)}

    def p(v):
        if is_B_power(v):
            k = v.bit_length() - 1
            return A[k - 1]
        k = a_index[v]
        return 1 << k

    return sum(p(v) for v in range(1, N + 1))


for N in [10, 20, 50, 100]:
    S = transposition_moment(N)
    print(N, S, "bit length:", S.bit_length())
```

A useful next computation would be to generate large finite SAT avoiders and record, for each \(n\),

```python
(max_count[n], min_count[n], rho[n], D_n, max_weight[n] + min_weight[n])
```

to determine whether extremum loads concentrate near a small collection of ranks or are distributed similarly to the least-significant-bit order.

## Route Diagnosis

### Proved ledger

- Exact pathwise lower bounds \(H(L)\) for all extrema and \(G(L)\) for each extremum type.
- The exact progression-extremum incidence identity \(Q_N\le I_N\le2Q_N\).
- Unweighted and multiplicity-weighted rank-capacity bounds for each center.
- Quadratic lower bounds \(N^2/40+O(N)\) for local maxima and minima separately.
- An explicit total order whose every finite restriction avoids monotone three-term, hence four-term, arithmetic progressions.
- Failure of append-only priority repair once a target becomes unsafe.

### Plausible but unproved claims

- A successful Route 1 argument may require a multiscale inequality coupling value cutoffs \(N\) with time cutoffs \(T\), forcing many required maxima to be centered among \(\{n:p(n)\le T\}\).
- The least-significant-bit order may be a useful scaffold for a counterexample if it can be modified to order type \(\omega\) while allowing only isolated failures of its “every midpoint is extremal” property. No such modification has been proved safe.

### Dead ends

1. **Unweighted extremum counting:** blocked because the LSB order has every possible symmetric triple extremal and \(I_N=2Q_N\).
2. **Finite rank-sensitive counting:** blocked because every finite \([N]\) has an avoiding rank assignment.
3. **Closing through \(\sum_{n\le N}p(n)\):** blocked because permutation rank moments have no useful upper bound.
4. **Priority buffers:** blocked because unsafe omitted targets remain permanently unsafe.

### Recommended next step

A fresh affirmative attempt should reconstruct the DEGS three-term proof and isolate exactly how finite predecessor sets defeat the LSB order. For Route 1 specifically, the needed object is a truncated predecessor mass-transport inequality on the permutation plot
\[
\{(n,p(n)):n\in\mathbb N\},
\]
not another count inside a single \([N]\). A fresh negative attempt should start from the LSB order but use a hierarchical scheduling rule that reserves endangered small integers before they become permanently unsafe.