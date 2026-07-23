STATUS: BLOCKED

## Result

Route 4 yields substantial rigidity but not a resolution of either Q1 or Q2. I prove that any sequence of scales \(N_j\) with \(E_A(N_j)=o(\sqrt{N_j})\) forces the same universal lower-scale density profile
\[
A(tN_j)\sim \kappa\sqrt{tN_j},
\qquad
\kappa=\frac{2\sqrt2}{\sqrt\pi},
\qquad 0<t<1.
\]
Moreover, such good scales necessarily contain collision “reservoirs”:
\[
\max_{n\le N_j}(r_A(n)-1)
\gg \frac{\sqrt{N_j}}{E_A(N_j)}.
\]
Thus a counterexample to Q1 for exponent \(\epsilon\) would require representation multiplicities much larger than \(N_j^\epsilon\) along its good scales, while a hypothetical Q2 set would necessarily have unbounded representation function. The route is blocked because first-order multiscale block counts admit an exact continuum solution, and repeated representations can be concentrated on very few sums. A second-order dispersion theorem preventing that concentration is still missing and appears comparable in strength to the original problem.

## Complete Argument

Write
\[
A(x)=|A\cap[1,x]|,\qquad
R_A(N)=\sum_{n\le N}r_A(n),
\]
and
\[
\Delta_A(N)=\sum_{n\le N}(r_A(n)-1)_+.
\]

### 1. Two rigorous local extension inequalities

#### Lemma 1: block-pair capacity

Let \(X,Y\subseteq A\) be disjoint finite sets, with
\[
|X|=p,\qquad |Y|=q,
\]
and suppose all sums \(x+y\), \(x\in X,y\in Y\), lie in an integer interval \(K\subseteq[1,T]\) of length \(L\). Put
\[
e_K=\#\{n\in K:r_A(n)\ne1\}.
\]
Then
\[
pq\le L+e_K(\min(p,q)-1).
\]
Consequently, when \(\min(p,q)>1\),
\[
e_K\ge
\frac{(pq-L)_+}{\min(p,q)-1}.
\]

**Proof.** For a fixed sum \(n\), the pairs in \(X\times Y\) satisfying \(x+y=n\) form a matching: each \(x\) determines at most one \(y\), and conversely. Thus there are at most \(\min(p,q)\) such pairs.

If \(r_A(n)=1\), there is at most one such pair. Hence the \(L-e_K\) good values contribute at most one pair each, and the exceptional values contribute at most \(\min(p,q)\) pairs each. Therefore
\[
pq\le (L-e_K)+e_K\min(p,q),
\]
which is the stated inequality. ∎

For one block \(X\subseteq A\), \(|X|=p\), whose unordered self-sums lie in an interval \(K\) of length \(L\), the analogous inequality is
\[
\frac{p(p+1)}2
\le
L+e_K\left(\left\lceil\frac p2\right\rceil-1\right).
\]
Indeed, at a fixed sum the pairs from \(X\) form a matching, possibly with one diagonal loop, so there are at most \(\lceil p/2\rceil\) of them.

These are genuine extension inequalities. Their limitation is that their right-hand sides often have substantial first-order slack.

---

#### Lemma 2: repeated differences force local exceptional sums

Let \(S\subseteq A\cap[L,U]\), let \(d>0\), and define
\[
B_d=\{b:b,b+d\in S\},\qquad m_d=|B_d|.
\]
Then there are at least
\[
\max(0,2m_d-3)
\]
exceptional sums in
\[
[2L+d,\,2U-d].
\]

**Proof.** For distinct \(b,c\in B_d\),
\[
b+(c+d)=c+(b+d).
\]
The two unordered pairs are distinct, even if \(c=b+d\), in which case one of them may be diagonal. Thus
\[
b+c+d
\]
is multiply represented.

If \(B_d=\{b_1<\cdots<b_m\}\), the restricted pair-sum set contains the strictly increasing chain
\[
b_1+b_2< b_1+b_3<\cdots<b_1+b_m
< b_2+b_m<\cdots<b_{m-1}+b_m.
\]
It therefore has at least \(2m-3\) elements. Every corresponding sum lies between \(2L+d\) and \(2U-d\). ∎

A consequence is
\[
m_d\le \frac{E_A([2L+d,2U-d])+3}{2},
\]
where \(E_A(I)\) denotes the number of exceptional integers in \(I\).

This is useful for controlling any one repeated difference, but the same exceptional sum can account for repetitions of many different differences.

---

### 2. A basic prefix-size bound

#### Lemma 3

For every positive integer \(x\),
\[
A(x)\le E_A(2x)+2\sqrt{x}.
\]

**Proof.** Let \(S=A\cap[1,x]\), \(p=|S|\), and \(e=E_A(2x)\). Every unordered pair from \(S\) has sum at most \(2x\).

At a good sum there is at most one pair from \(S\). At an exceptional sum there are at most \(\lceil p/2\rceil\le(p+1)/2\) pairs from \(S\). Hence
\[
\frac{p(p+1)}2
\le
2x+\frac{e(p+1)}2.
\]
Thus
\[
(p-e)(p+1)\le4x.
\]
If \(p\le e\), the conclusion is immediate. If \(p>e\), then \(p+1\ge p-e\), so
\[
(p-e)^2\le4x.
\]
Therefore \(p\le e+2\sqrt{x}\). ∎

Also, for every \(n\),
\[
r_A(n)\le A(n/2),
\]
because every unordered representation has a distinct smaller summand \(a\le n/2\).

---

### 3. Rigidity at any exceptionally good sequence of scales

The following is the principal multiscale result.

#### Theorem 4: universal square-root profile at good scales

Suppose \(N_j\to\infty\) and
\[
e_j:=E_A(N_j)=o(\sqrt{N_j}).
\]
Then for every fixed \(0<t<1\),
\[
\frac{A(\lfloor tN_j\rfloor)}{\sqrt{N_j}}
\longrightarrow
\kappa\sqrt t,
\qquad
\kappa=\frac{2\sqrt2}{\sqrt\pi}.
\]

In addition, for every fixed \(0<s\le1\),
\[
R_A(\lfloor sN_j\rfloor)=sN_j+o(N_j).
\]

#### Proof

First consider \(m\le N_j\). By Lemma 3,
\[
A(m/2)\le E_A(m)+2\sqrt{m/2}
\le e_j+2\sqrt{N_j/2}
=O(\sqrt{N_j}).
\]
Therefore
\[
\max_{n\le N_j}r_A(n)=O(\sqrt{N_j}).
\]

For \(m=\lfloor sN_j\rfloor\), the missing terms contribute at most \(e_j\), while
\[
\Delta_A(m)
\le
E_A(m)\max_{n\le m}(r_A(n)-1)
=o(\sqrt{N_j})O(\sqrt{N_j})
=o(N_j).
\]
Using
\[
R_A(m)=m-Z_A(m)+\Delta_A(m),
\]
we obtain
\[
R_A(\lfloor sN_j\rfloor)=sN_j+o(N_j).
\]

Now introduce the scaled counting measures
\[
\mu_j=\frac1{\sqrt{N_j}}\sum_{a\in A}\delta_{a/N_j}.
\]

For \(0<t\le1/2\), Lemma 3 gives
\[
\mu_j([0,t])
=
\frac{A(tN_j)}{\sqrt{N_j}}
\le
\frac{e_j}{\sqrt{N_j}}+2\sqrt t+o(1).
\]
Thus the restrictions of \(\mu_j\) to every compact subinterval of \([0,1/2)\) have uniformly bounded mass.

Let
\[
C_A(m)=\#\{(a,b)\in A^2:a+b\le m\}
\]
be the ordered cumulative pair count. Since an off-diagonal unordered representation contributes twice and a diagonal representation once,
\[
C_A(m)=2R_A(m)-A(m/2).
\]
Consequently, for fixed \(0<s<1\),
\[
\frac{C_A(\lfloor sN_j\rfloor)}{N_j}\longrightarrow 2s.
\]
Equivalently,
\[
(\mu_j*\mu_j)([0,s])\longrightarrow2s.
\]

Take a vaguely convergent subsequence on \([0,T]\), initially with \(T<1/2\), and call its limit \(\mu\). The preceding convergence implies
\[
\mu*\mu=2\,dx
\quad\text{on }(0,T).
\]

Let
\[
d\nu(x)=\sqrt{\frac2\pi}\,x^{-1/2}\,dx,\qquad x>0.
\]
The beta integral gives
\[
\frac{d(\nu*\nu)}{dx}(u)
=
\frac2\pi\int_0^u\frac{dv}{\sqrt{v(u-v)}}=2.
\]
Thus
\[
\nu*\nu=2\,dx.
\]

It remains to note that the positive convolution square root is locally unique. Indeed,
\[
(\mu-\nu)*(\mu+\nu)=0
\quad\text{on }(0,T).
\]
The local Titchmarsh convolution theorem for distributions supported on \([0,\infty)\) says that if a convolution vanishes on \((0,T)\), then the lengths of the initial intervals on which its two factors vanish have sum at least \(T\). Since \(\mu+\nu\) is nonzero on every interval \((0,\delta)\), it follows that \(\mu-\nu\) vanishes on \((0,T)\). Hence
\[
\mu=\nu\quad\text{on }(0,T).
\]

Every subsequential limit is therefore \(\nu\), so for \(0<t<1/2\),
\[
\frac{A(tN_j)}{\sqrt{N_j}}
\longrightarrow
\nu([0,t])
=
2\sqrt{\frac2\pi}\sqrt t
=
\kappa\sqrt t.
\]

We extend this to every fixed \(T<1\). Choose
\[
0<\delta<\min(1/2,1-T).
\]
Set
\[
X_j=A\cap[1,\delta N_j],\qquad
Y_j=A\cap(\delta N_j,TN_j],
\]
and write \(p_j=|X_j|\), \(q_j=|Y_j|\). We already know
\[
p_j\sim\kappa\sqrt{\delta N_j}.
\]
All sums \(x+y\), \(x\in X_j,y\in Y_j\), are at most
\[
(T+\delta)N_j<N_j.
\]
Lemma 1 therefore gives the crude but sufficient bound
\[
p_jq_j\le N_j+e_j\min(p_j,q_j).
\]
If \(q_j\le p_j\), then \(q_j=O(\sqrt{N_j})\). If \(q_j>p_j\), then
\[
q_j\le \frac{N_j}{p_j}+e_j=O(\sqrt{N_j}).
\]
Thus \(\mu_j([0,T])=O(1)\). Repeating the preceding compactness and local convolution-square-root argument on \([0,T]\) proves
\[
\mu_j\longrightarrow\nu
\quad\text{locally on }[0,1).
\]
This gives the asserted profile for every \(0<t<1\). ∎

---

### 4. Consequences for Q1 and Q2

#### Corollary 5: rigidity under Q2

If
\[
E_A(N)=o(\sqrt N),
\]
then
\[
A(x)\sim \kappa\sqrt x,
\qquad
\kappa=\frac{2\sqrt2}{\sqrt\pi}.
\]

**Proof.** Apply Theorem 4 with \(N_j=3j\) and \(t=1/3\), or with any fixed dilation larger than one. ∎

Thus a Q2 construction cannot use arbitrary multiscale densities. Its density is forced, with the exact constant
\[
\kappa\approx1.595769.
\]

Similarly, if Q1 fails for some \(\epsilon>0\), there is a sequence \(N_j\) such that
\[
E_A(N_j)=o(N_j^{1/2-\epsilon}),
\]
hence certainly \(E_A(N_j)=o(\sqrt{N_j})\). The same universal profile then holds throughout every fixed lower fraction of those scales.

---

### 5. Good scales force collision reservoirs

We need a quantitative Sidon bound.

#### Lemma 6: elementary asymptotic Sidon bound

If \(S\subseteq[1,x]\) is Sidon and \(|S|=m\), then
\[
m\le\sqrt x+O(x^{1/4}).
\]

**Proof.** Write
\[
S=\{s_1<\cdots<s_m\}.
\]
All positive differences \(s_j-s_i\), \(j>i\), are distinct. Indeed, an equality
\[
s_j-s_i=s_\ell-s_k
\]
would give
\[
s_j+s_k=s_\ell+s_i,
\]
and the Sidon property forces the original difference pairs to coincide.

Fix \(u<m\). The
\[
M=\sum_{h=1}^u(m-h)=um-\frac{u(u+1)}2
\]
differences
\[
s_{i+h}-s_i,\qquad 1\le h\le u,\quad 1\le i\le m-h,
\]
are distinct positive integers. Hence their sum is at least \(M(M+1)/2\).

For each \(h\),
\[
\sum_{i=1}^{m-h}(s_{i+h}-s_i)
=
\sum_{i=m-h+1}^m s_i-\sum_{i=1}^h s_i
\le hx.
\]
Therefore
\[
\frac{M(M+1)}2\le x\frac{u(u+1)}2.
\]
Taking \(u=\lfloor x^{1/4}\rfloor\), unless \(m\le u\) already, yields
\[
m\le \sqrt x+O(x^{1/4}).
\]
∎

#### Lemma 7: deleting total excess produces a Sidon set

For finite \(S\), let \(q_S(n)\) be its unordered representation function and put
\[
\Delta_S=\sum_n(q_S(n)-1)_+.
\]
Then \(S\) contains a Sidon subset of size at least
\[
|S|-\Delta_S.
\]

**Proof.** For each \(n\) with \(q_S(n)\ge2\), designate one representing pair. For every other pair representing \(n\), select one of its endpoints for deletion. At most
\[
q_S(n)-1
\]
vertices are selected for that sum. After all selected vertices are deleted, every sum retains at most its designated pair. The resulting set is Sidon, and at most \(\Delta_S\) vertices were deleted. ∎

#### Theorem 8: reservoir lower bound at good scales

Under the assumptions of Theorem 4, there is an absolute \(c>0\) such that
\[
\max_{n\le N_j}(r_A(n)-1)
\ge
c\frac{\sqrt{N_j}}{E_A(N_j)}
\]
for all sufficiently large \(j\).

**Proof.** Fix \(t_0\in(0,1/2)\), for example \(t_0=1/3\), and put
\[
L_j=\lfloor t_0N_j\rfloor,\qquad S_j=A\cap[1,L_j].
\]
Theorem 4 gives
\[
|S_j|=\kappa\sqrt{L_j}+o(\sqrt{N_j}).
\]
All pair sums of \(S_j\) are at most \(2L_j<N_j\).

By Lemmas 6 and 7,
\[
\Delta_{S_j}
\ge
|S_j|-\sqrt{L_j}-O(L_j^{1/4})
=
(\kappa-1)\sqrt{L_j}+o(\sqrt{N_j}).
\]
Every sum counted by \(\Delta_{S_j}\) is globally multiply represented, and
\[
(q_{S_j}(n)-1)_+\le(r_A(n)-1)_+.
\]
Since there are at most \(e_j=E_A(N_j)\) exceptional sums up to \(N_j\),
\[
\Delta_{S_j}
\le
e_j\max_{n\le N_j}(r_A(n)-1).
\]
The result follows because \(\kappa-1>0\). ∎

Consequences:

1. If Q2 holds, then
   \[
   \max_{n\le N}r_A(n)\longrightarrow\infty
   \]
   along a sequence, and quantitatively
   \[
   \max_{n\le N}(r_A(n)-1)
   \gg\frac{\sqrt N}{E_A(N)}.
   \]

2. If Q1 fails for some \(\epsilon>0\), choose \(N_j\) with
   \[
   E_A(N_j)=o(N_j^{1/2-\epsilon}).
   \]
   Then
   \[
   \frac{\max_{n\le N_j}r_A(n)}{N_j^\epsilon}\longrightarrow\infty.
   \]
   Thus any counterexample to Q1 must create polynomially large collision reservoirs at its good scales.

This is a genuine restriction, but not a contradiction.

---

### 6. Why multiplicity concentration cannot be dismissed

The following finite construction rules out a tempting lemma.

#### Proposition 9: one sum can carry arbitrarily large multiplicity

Let \(X\subseteq[1,L]\) be Sidon and choose \(M>3L\). Set
\[
Y=M-X=\{M-x:x\in X\},\qquad S=X\cup Y.
\]
Then the only multiply represented pair sum of \(S\) is \(M\), and
\[
r_S(M)=|X|.
\]

**Proof.** The three types of sums lie in disjoint intervals:
\[
X+X\subseteq[2,2L],
\]
\[
X+Y\subseteq[M-L+1,M+L-1],
\]
\[
Y+Y\subseteq[2M-2L,2M-2].
\]
They are disjoint because \(M>3L\).

The \(X+X\) sums are unique because \(X\) is Sidon, and the same holds for \(Y+Y\).

A cross sum has the form
\[
x+(M-x')=M+(x-x').
\]
For a nonzero difference, uniqueness follows because all positive differences of a Sidon set are distinct. Difference zero occurs precisely when \(x=x'\), giving \(|X|\) representations of \(M\). ∎

This construction has many missing sums, so it is not close to solving Q2. It does, however, prove that “a highly represented sum forces many other multiply represented sums” is false without using the near-covering hypothesis in an essential way.

---

### 7. The exact first-order obstruction to Route 4

The forced profile from Theorem 4 has formal density
\[
f(t)=\sqrt{\frac2\pi}\,t^{-1/2}.
\]
Its ordered self-convolution is exactly
\[
(f*f)(u)
=
\frac2\pi\int_0^u\frac{dt}{\sqrt{t(u-t)}}=2.
\]
Thus its unordered off-diagonal convolution is exactly \(1\), with diagonal terms lower order.

Therefore the first-order dyadic or geometric block equations are perfectly consistent with near-unique representation. Coarse block counts cannot yield a contradiction: they converge to an exact continuum solution. Any successful extension inequality must detect a second-order, lattice-scale obstruction of order roughly \(\sqrt N\), while remaining insensitive to arbitrarily high multiplicity concentrated on a few sums.

That missing second-order theorem is the precise block.

## Self-Audit

1. **Use of the local Titchmarsh convolution theorem.**  
   This is the least elementary ingredient. The exact version used is standard for distributions supported on \([0,\infty)\): if \(f*g\) vanishes on an initial interval of length \(T\), then the lengths of initial vanishing intervals for \(f\) and \(g\) sum to at least \(T\). It applies to the signed locally finite measures \(\mu-\nu\) and \(\mu+\nu\). Since \(\nu\) gives positive mass to every initial interval, it forces \(\mu=\nu\) locally.

2. **Passage from discrete scaled measures to the continuum convolution equation.**  
   Boundary atoms and loss of compactness could in principle be problematic. Here compactness is supplied first by Lemma 3 and then by the block-pair inequality. The cumulative ordered convolution converges to the continuous function \(2s\), so no boundary atom remains in the limiting convolution. This justifies the vague-limit passage.

3. **The reservoir theorem does not bound exceptional support.**  
   It proves only
   \[
   E_A(N)\max_{n\le N}(r_A(n)-1)\gg\sqrt N.
   \]
   This is fully rigorous, but concentration can make the maximum multiplicity very large. Proposition 9 shows that such concentration is a real combinatorial phenomenon, not merely a weakness of the proof. Thus this point is a limitation, not a hidden claim that Q1 or Q2 has been solved.

## Computations To Verify

The following exact Python code checks representation functions, finite optima for small \(N\), the prefix bound, the repeated-difference lemma, and the central-reservoir example.

```python
from itertools import combinations, product
from math import sqrt, pi

KAPPA = 2 * sqrt(2 / pi)

def reps(S, N):
    """Exact unordered representation counts up to N."""
    S = sorted(a for a in set(S) if 1 <= a <= N)
    r = [0] * (N + 1)
    for i, a in enumerate(S):
        for b in S[i:]:
            s = a + b
            if s > N:
                break
            r[s] += 1
    return r

def stats(S, N):
    r = reps(S, N)
    Z = sum(r[n] == 0 for n in range(1, N + 1))
    M = sum(r[n] >= 2 for n in range(1, N + 1))
    E = Z + M
    Delta = sum(max(0, r[n] - 1) for n in range(1, N + 1))
    H = max(r[1:], default=0)
    return {"E": E, "Z": Z, "M": M, "Delta": Delta, "H": H, "r": r}

def exhaustive_D(N):
    """
    Exact D(N), feasible only for small N.
    Membership of N itself is irrelevant to sums <= N.
    """
    best_E = N + 1
    best_sets = []
    for mask in range(1 << (N - 1)):
        S = {a for a in range(1, N) if (mask >> (a - 1)) & 1}
        E = stats(S, N)["E"]
        if E < best_E:
            best_E = E
            best_sets = [S]
        elif E == best_E:
            best_sets.append(S)
    return best_E, best_sets

def check_prefix_bound(S, x):
    """
    Verifies A(x) <= E_A(2x) + 2 sqrt(x)
    in the exact squared form used in the proof.
    """
    p = sum(1 for a in S if a <= x)
    e = stats(S, 2 * x)["E"]
    if p > e:
        assert (p - e) ** 2 <= 4 * x
    return p, e

def check_difference_lemma(S, L, U):
    """
    Checks that every fixed repeated difference generates at least 2m-3
    exceptional sums in the stated interval.
    """
    S = set(S)
    r = reps(S, 2 * U)
    for d in range(1, U - L + 1):
        B = sorted(
            b for b in S
            if L <= b <= U - d and b + d in S
        )
        m = len(B)
        vals = {
            B[i] + B[j] + d
            for i in range(m)
            for j in range(i + 1, m)
        }
        assert len(vals) >= max(0, 2 * m - 3)
        for v in vals:
            assert 2 * L + d <= v <= 2 * U - d
            assert r[v] >= 2
    return True

def central_reservoir(m):
    """
    Powers of two form a Sidon set.
    The reflected union has only one multiply represented sum.
    """
    X = {1 << i for i in range(m)}
    L = max(X)
    M = 3 * L + 1
    Y = {M - x for x in X}
    S = X | Y

    r = reps(S, 2 * M)
    multi = {n: r[n] for n in range(1, 2 * M + 1) if r[n] >= 2}
    assert multi == {M: m}
    return X, Y, M, S

def nested_best(prefix_bits, N):
    """
    Exhaustive nested-extension search for small N.

    prefix_bits[a-1] fixes membership of a for 1 <= a <= p.
    Searches all choices in p+1,...,N-1.
    Objective: minimize the worst E(n)/sqrt(n) over p < n <= N,
    then minimize E(N).
    """
    p = len(prefix_bits)
    fixed = {a for a in range(1, p + 1) if prefix_bits[a - 1]}
    free = list(range(p + 1, N))

    best_obj = None
    best_S = None
    best_profile = None

    for choices in product([0, 1], repeat=len(free)):
        S = set(fixed)
        S.update(a for a, bit in zip(free, choices) if bit)

        profile = []
        for n in range(p + 1, N + 1):
            E = stats(S, n)["E"]
            profile.append((n, E, E / sqrt(n)))

        obj = (
            max(v for _, _, v in profile),
            profile[-1][1]
        )
        if best_obj is None or obj < best_obj:
            best_obj = obj
            best_S = S
            best_profile = profile

    return best_obj, best_S, best_profile

def report_profile(S, N, ts=(0.1, 0.2, 1/3, 0.4)):
    """
    Compare a candidate's lower-scale profile to kappa*sqrt(t).
    """
    out = []
    for t in ts:
        x = int(t * N)
        observed = sum(a <= x for a in S) / sqrt(N)
        predicted = KAPPA * sqrt(t)
        out.append((t, observed, predicted, observed - predicted))
    return out

# Suggested exact checks:
#
# for N in range(2, 23):
#     D, opts = exhaustive_D(N)
#     print(N, D, D / sqrt(N), len(opts))
#
# for m in range(1, 12):
#     X, Y, M, S = central_reservoir(m)
#     print("reservoir", m, M, stats(S, 2*M)["M"])
#
# for L in range(1, 11):
#     for mask in range(1 << L):
#         S = {a for a in range(1, L+1) if (mask >> (a-1)) & 1}
#         check_prefix_bound(S, L)
#         check_difference_lemma(S, 1, L)
```

For a more decisive Route 4 experiment, the nested search should record, for each fixed near-optimal prefix:

1. the minimum possible
   \[
   \max_{N_0<n\le N_1}\frac{E_A(n)}{\sqrt n};
   \]
2. the block counts
   \[
   |A\cap(\alpha N_1,\beta N_1]|;
   \]
3. the largest multiplicity \(\max_{n\le N_1}r_A(n)\);
4. the ratio
   \[
   \frac{\sqrt{N_1}}{E_A(N_1)\max_{n\le N_1}(r_A(n)-1)};
   \]
5. whether new exceptions are localized near block transitions or at a few high-multiplicity reservoir sums.

## Route Diagnosis

**Proved ledger**

- Exact block-pair and self-block extension inequalities.
- A local repeated-difference-to-exception lemma.
- The prefix bound
  \[
  A(x)\le E_A(2x)+2\sqrt x.
  \]
- Universal density rigidity at every scale sequence with \(E_A(N_j)=o(\sqrt{N_j})\):
  \[
  A(tN_j)\sim\frac{2\sqrt2}{\sqrt\pi}\sqrt{tN_j}.
  \]
- Linear cumulative representation count on such scales:
  \[
  R_A(tN_j)=tN_j+o(N_j).
  \]
- Collision-reservoir necessity:
  \[
  \max_{n\le N_j}(r_A(n)-1)
  \gg\frac{\sqrt{N_j}}{E_A(N_j)}.
  \]
- A finite reflected-Sidon example showing that one exceptional sum can carry arbitrarily large multiplicity without forcing other multiply represented sums.

**Plausible but unproved claim needed to continue**

A second-order dispersion/stability theorem of the following kind:
\[
A(tN)=\left(\frac{2\sqrt2}{\sqrt\pi}+o(1)\right)\sqrt{tN},
\quad
R_A(tN)=tN+o(N)
\]
for all fixed \(t<1\), together with exact integrality of the representation system, should force
\[
E_A(N)\ge N^{1/2-o(1)}.
\]
No proof is available. Without a quantitative mechanism preventing the excess multiplicity from living on a small number of reflected-Sidon-type reservoirs, this is essentially the original support problem in another form.

**Dead ends**

1. **First-order block recurrences.**  
   They cannot contradict a good configuration because the forced density
   \[
   \sqrt{2/\pi}\,t^{-1/2}
   \]
   has exactly constant self-convolution.

2. **Energy or total-excess arguments.**  
   They yield large \(\Delta_A(N)\), but only the product bound
   \[
   \Delta_A(N)
   \le
   E_A(N)\max_{n\le N}(r_A(n)-1).
   \]
   Reservoir multiplicities defeat conversion to support.

3. **“A large reservoir creates many other collisions.”**  
   Proposition 9 disproves this without an additional near-covering hypothesis.

**Best next direction**

A fresh attempt should combine Route 4 with Route 6: classify configurations that simultaneously have the universal square-root profile and a few very highly represented reservoir sums. The needed lemma should show that such a reservoir necessarily creates a comparable number of missing or multiply represented integers in a neighboring interval once the surrounding set also obeys the forced profile. That would be genuinely stronger than coarse Sidon counting and would target exactly the remaining obstruction.