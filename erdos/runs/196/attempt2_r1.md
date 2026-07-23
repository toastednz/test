STATUS: BLOCKED

## Result

Route A’s proposed simultaneous good-step lemma is false, even for genuine permutation orders of type \(\omega\). Explicitly, listing each block \([3^j,3^{j+1}-1]\) in decreasing order, while listing the blocks in increasing order, gives a permutation with no increasing positional four-term arithmetic progression and hence no simultaneous good step. It does contain decreasing progressions, so this is not a disproof of Erdős #196. I also establish an exact mass-transport consequence: every permutation avoiding increasing four-term progressions has, arbitrarily far out, vertices with arbitrarily many larger numerical values preceding them. Finally, I show that divisor normalization cannot by itself close the argument: one inversion can certify arbitrarily many bad steps, and common bad-step thresholds for finitely many anchors can be arbitrarily large even when those anchors arrive early. Exploiting the additional prohibition on decreasing progressions remains blocked at an affine edge-alignment theorem essentially comparable to Route C.

## Complete Argument

### 1. The simultaneous good-step lemma is false

For an integer base \(b\ge 3\), partition \(\mathbb N\) into blocks
\[
I_j=[b^j,b^{j+1}-1],\qquad j\ge 0.
\]
Define a permutation by listing the blocks in increasing \(j\), but listing the elements of each block in decreasing numerical order.

If \(n\in I_j\), its position is
\[
p_b(n)=(b^j-1)+(b^{j+1}-n)
      =(b+1)b^j-n-1.
\tag{1}
\]
Indeed, there are \(b^j-1\) values in preceding blocks, and \(b^{j+1}-n\) values from the top of \(I_j\) down through \(n\). Thus \(p_b\) maps \(I_j\) bijectively onto \(I_j\), so \(p_b:\mathbb N\to\mathbb N\) is a bijection.

#### Proposition 1

The permutation \(p_b\) contains no increasing positional four-term arithmetic progression.

#### Proof

Suppose, toward a contradiction, that
\[
y_i=a+id,\qquad 0\le i\le 3,
\]
satisfies
\[
p_b(y_0)<p_b(y_1)<p_b(y_2)<p_b(y_3).
\tag{2}
\]

If two of the \(y_i\) lie in the same block, then because \(y_i<y_j\) for \(i<j\), the reversal inside that block gives
\[
p_b(y_i)>p_b(y_j),
\]
contradicting (2). Hence the four terms must lie in four distinct blocks.

In particular, \(y_1,y_2,y_3\) lie in three distinct blocks. If \(y_1\in I_j\), then \(y_3\) must lie in \(I_{j+2}\) or a later block. Therefore
\[
y_1\le b^{j+1}-1,\qquad y_3\ge b^{j+2},
\]
and consequently
\[
\frac{y_3}{y_1}
\ge \frac{b^{j+2}}{b^{j+1}-1}
>b\ge 3.
\tag{3}
\]
On the other hand,
\[
\frac{y_3}{y_1}
=\frac{a+3d}{a+d}<3,
\tag{4}
\]
because \(a>0\). This contradiction proves the proposition. ∎

For \(n\in I_j\), the larger values preceding \(n\) are exactly
\[
P^+(n)=\{n+1,n+2,\dots,b^{j+1}-1\}.
\]
Hence
\[
B(n)
=\bigcup_{h=1}^{b^{j+1}-1-n}\operatorname{Div}(h)
=\{1,2,\dots,b^{j+1}-1-n\}.
\tag{5}
\]

Every four-term progression has two adjacent terms in the same block by the preceding proof. Thus, for every \(n,q\), at least one of
\[
q\in B(n),\qquad q\in B(n+q),\qquad q\in B(n+2q)
\]
holds. Therefore this permutation has no simultaneous good step.

This also refutes the more flexible Route A target seeking three suffix-record coefficients in arithmetic progression: such three records would, by the three-record criterion, produce an increasing positional four-term progression, and Proposition 1 excludes all of those.

The example does not resolve the original problem. For example, with \(b=3\), the values
\[
3,4,5,6
\]
are all in \(I_1=[3,8]\), so
\[
p_3(3)>p_3(4)>p_3(5)>p_3(6).
\]
Thus the example contains a decreasing four-term progression.

---

### 2. An exact mass-transport theorem that survives

Although simultaneous good steps cannot be forced, Route A does yield an exact adjacent-inversion count.

Define the forward inversion outdegree
\[
\delta(u)=\#\{v>u:p(v)<p(u)\}.
\tag{6}
\]
This is finite, and
\[
\delta(u)\le p(u)-1.
\tag{7}
\]

#### Proposition 2

Let \(p\) be a permutation containing no increasing positional four-term arithmetic progression. Let \(A\subset\mathbb N\) and \(S\subset\mathbb N\) be finite sets such that
\[
q\notin B(a)\qquad\text{for all }a\in A,\ q\in S.
\tag{8}
\]
Then there are at least
\[
\frac{|A||S|}{2}
\]
distinct forward inversion edges \((u,u+q)\), with \(q\in S\), whose sources have one of the forms
\[
u=a+q\quad\text{or}\quad u=a+2q.
\]

#### Proof

Fix \((a,q)\in A\times S\). Since \(q\notin B(a)\),
\[
p(a)<p(a+kq)\qquad\text{for every }k\ge1.
\]
In particular,
\[
p(a)<p(a+q).
\tag{9}
\]

If both
\[
p(a+q)<p(a+2q)
\quad\text{and}\quad
p(a+2q)<p(a+3q)
\]
held, then the four positions would be strictly increasing, contrary to the hypothesis. Hence at least one of
\[
p(a+2q)<p(a+q),
\tag{10}
\]
or
\[
p(a+3q)<p(a+2q)
\tag{11}
\]
holds.

Choose one such inversion. In case (10), charge \((a,q)\) to the edge
\[
(a+q,a+2q).
\]
In case (11), charge it to
\[
(a+2q,a+3q).
\]

A fixed edge \((u,u+q)\) can receive at most two charges: a first-type charge can only come from
\[
a=u-q,
\]
while a second-type charge can only come from
\[
a=u-2q.
\]
The edge difference determines \(q\), so there are no further possibilities. Thus \(|A||S|\) charges produce at least \(|A||S|/2\) distinct edges. ∎

#### Corollary 3

If \(p\) avoids increasing positional four-term progressions, then for every \(D\ge1\), infinitely many \(u\) satisfy
\[
\delta(u)\ge D.
\tag{12}
\]

#### Proof

Set \(K=8D\) and \(A=[K]\). Since every \(B(a)\) is finite, there exists \(Q_0\) such that
\[
q\notin B(a)
\qquad
(a\le K,\ q>Q_0).
\tag{13}
\]

Choose \(Q>\max(Q_0,K)\) and let
\[
S=[Q,2Q].
\]
Proposition 2 gives at least
\[
\frac{K(Q+1)}2
\tag{14}
\]
distinct inversion edges.

Every source of such an edge lies in
\[
[Q+1,K+4Q],
\]
an interval containing \(K+3Q\) integers. Therefore
\[
\sum_{u=Q+1}^{K+4Q}\delta(u)
\ge \frac{K(Q+1)}2.
\tag{15}
\]
Since \(Q\ge K\),
\[
K+3Q\le4Q,
\]
and the average outdegree over this source interval is at least
\[
\frac{K(Q+1)}{2(K+3Q)}
\ge \frac{KQ}{8Q}
=\frac K8
=D.
\]
Thus some source in the interval has \(\delta(u)\ge D\).

Now choose such \(Q\)'s successively so that
\[
Q_{j+1}>K+4Q_j.
\]
The corresponding source intervals are disjoint, so this produces infinitely many distinct \(u\) satisfying (12). ∎

Consequently, every hypothetical counterexample to Erdős #196 must have arbitrarily large forward inversion outdegrees, occurring infinitely often. This is necessary but not contradictory to order type \(\omega\): every individual outdegree remains finite.

---

### 3. Exact limits of divisor normalization

Each \(B(n)\) is a finite divisor-downset: if \(q\in B(n)\) and \(r\mid q\), then \(r\in B(n)\). There is essentially no stronger single-anchor restriction.

#### Proposition 4

Every finite divisor-downset \(S\subset\mathbb N\) occurs as \(B(n)\) for some \(n\) in some permutation.

#### Proof

Arrange the finite set
\[
\{n+h:h\in S\}
\]
before \(n\), arrange no other value larger than \(n\) before \(n\), and then complete the resulting finite prefix arbitrarily to a permutation of \(\mathbb N\). Then
\[
P^+(n)=\{n+h:h\in S\}.
\]
Therefore
\[
B(n)=\bigcup_{h\in S}\operatorname{Div}(h)=S,
\]
where the last equality follows from divisor-downward closure and the fact that every \(h\in S\) divides itself. ∎

The proposed divisor normalization is valid but insufficient. For \(q\in B(n)\), let \(w(n,q)>n\) be the element of the ray
\[
n+q,n+2q,\dots
\]
with least position. Then \(p(w(n,q))<p(n)\). For any finite collection \(\mathcal C\) of bad pairs,
\[
\sum_{(n,q)\in\mathcal C}
\frac1{\tau(w(n,q)-n)}
\le
\#\{(n,w(n,q)):(n,q)\in\mathcal C\}.
\tag{16}
\]
Indeed, after grouping by a fixed witness pair \((n,m)\), every associated \(q\) divides \(m-n\), so there are at most \(\tau(m-n)\) such \(q\)'s.

However, one inversion can absorb arbitrarily many bad steps. Let
\[
H=\operatorname{lcm}(1,2,\dots,Q).
\]
Construct a permutation beginning with
\[
n+H,\ n,
\]
and then list all remaining values. For every \(q\le Q\), one has \(q\mid H\), so \(n+H\) is a predecessor witness showing
\[
q\in B(n).
\]
It is also the canonical least-position witness for every such \(q\). Since the \(Q\) integers \(1,\dots,Q\) are all divisors of \(H\),
\[
\tau(H)\ge Q,
\]
and their total \(1/\tau(H)\)-normalized charge is at most \(1\). Thus the normalization controls congestion per inversion precisely by making the total demand correspondingly too small.

There is also no bound on common bad-step thresholds in terms of the arrival ranks of finitely many anchors. Given \(K,Q\), choose a multiple \(H>K\) of \(\operatorname{lcm}(1,\dots,Q)\), and begin a permutation with
\[
H+1,H+2,\dots,H+K,1,2,\dots,K.
\tag{17}
\]
Then
\[
p(b)=K+b\le2K\qquad(1\le b\le K),
\]
but for every \(b\le K\) and \(q\le Q\), the value \(H+b\) precedes \(b\) and
\[
q\mid (H+b)-b=H.
\]
Hence
\[
[Q]\subseteq B(b)
\qquad\text{for every }b\le K.
\tag{18}
\]
This construction is not claimed to avoid monotone progressions. Its role is to prove that well-foundedness and bounded anchor ranks alone give no same-scale bound on the sets \(B(b)\).

## Self-Audit

1. **The reverse-block construction only avoids the increasing orientation.**  
   It explicitly contains decreasing four-term progressions, so it is not a counterexample to the original problem. I use it only to refute Route A’s simultaneous good-step lemma and any universal theorem forcing an increasing progression through suffix records.

2. **The mass-transport theorem does not contradict order type \(\omega\).**  
   Corollary 3 forces unbounded outdegrees at moving vertices, not infinite outdegree at a fixed vertex. Every individual \(\delta(u)\) may remain finite. The counting statement itself is reliable because each affine clause is charged to an actual adjacent inversion and every edge has at most two preimages.

3. **The LCM congestion examples are not avoiding permutations.**  
   They therefore do not prove that a hypothetical full avoider can exploit congestion arbitrarily. They prove only that divisor structure, bounded predecessor ranks, and bijectivity do not independently prevent it. The reverse-block permutation supplies a genuine increasing-avoider exhibiting the main simultaneous-good-step failure.

## Computations To Verify

```python
from math import lcm
from collections import defaultdict

BASE = 3

def block_data(n, base=BASE):
    """Return j,s with s=base**j and s <= n < base*s."""
    s = 1
    j = 0
    while base * s <= n:
        s *= base
        j += 1
    return j, s

def p_block(n, base=BASE):
    j, s = block_data(n, base)
    return (base + 1) * s - n - 1

def block_upper(n, base=BASE):
    _, s = block_data(n, base)
    return base * s - 1

def B_block(n, base=BASE):
    """Exact B(n) for the infinite reverse-block permutation."""
    return set(range(1, block_upper(n, base) - n + 1))

def check_reverse_blocks(J=7, base=BASE):
    N = base**J - 1
    inc = []
    dec = []

    for d in range(1, (N - 1)//3 + 1):
        for a in range(1, N - 3*d + 1):
            vals = [a + i*d for i in range(4)]
            pos = [p_block(v, base) for v in vals]
            if pos[0] < pos[1] < pos[2] < pos[3]:
                inc.append((a, d, vals, pos))
            if pos[0] > pos[1] > pos[2] > pos[3]:
                dec.append((a, d, vals, pos))

    assert not inc
    assert dec                    # e.g. (3,1) when base=3
    print("N =", N, "decreasing witnesses =", len(dec))
    print("first decreasing witness:", dec[0])

def check_B_formula(J=6, base=BASE):
    N = base**J - 1
    for n in range(1, N + 1):
        U = block_upper(n, base)
        brute = set()
        for m in range(n + 1, U + 1):
            assert p_block(m, base) < p_block(n, base)
            h = m - n
            for q in range(1, h + 1):
                if h % q == 0:
                    brute.add(q)
        assert brute == B_block(n, base)

def check_no_simultaneous_good(J=6, base=BASE):
    N = base**J - 1
    for q in range(1, (N - 1)//3 + 1):
        for n in range(1, N - 3*q + 1):
            covered = (
                q in B_block(n, base)
                or q in B_block(n + q, base)
                or q in B_block(n + 2*q, base)
            )
            assert covered

def check_mass_bound(K=20, Q=100, base=BASE):
    max_bad = max(
        block_upper(a, base) - a
        for a in range(1, K + 1)
    )
    assert Q > max(max_bad, K)

    edges = set()
    for a in range(1, K + 1):
        for q in range(Q, 2*Q + 1):
            assert q not in B_block(a, base)
            assert p_block(a, base) < p_block(a + q, base)

            if p_block(a + 2*q, base) < p_block(a + q, base):
                edges.add((a + q, a + 2*q))
            elif p_block(a + 3*q, base) < p_block(a + 2*q, base):
                edges.add((a + 2*q, a + 3*q))
            else:
                raise AssertionError("Increasing four-term progression found")

    assert 2 * len(edges) >= K * (Q + 1)

    outdegree_in_charged_edges = defaultdict(int)
    for u, v in edges:
        outdegree_in_charged_edges[u] += 1

    assert max(outdegree_in_charged_edges.values()) >= K / 8
    print("distinct charged edges:", len(edges))
    print("maximum charged outdegree:", max(outdegree_in_charged_edges.values()))

def check_lcm_congestion(n=10, Q=30):
    H = 1
    for q in range(1, Q + 1):
        H = lcm(H, q)

    witness = n + H
    # Permutation prefix is [witness, n], so witness precedes n.
    for q in range(1, Q + 1):
        assert H % q == 0
        assert witness == n + (H // q) * q

    print("One inversion certifies", Q, "bad steps.")
    print("difference H =", H)

check_reverse_blocks()
check_B_formula()
check_no_simultaneous_good()
check_mass_bound()
check_lcm_congestion()
```

A useful next finite search would impose simultaneously:

```text
1. Forward edges only: u -> v implies u < v.
2. Transitive closure.
3. For several anchors b and all q in a prescribed range:
       b+q -> b+2q OR b+2q -> b+3q.
4. No chain:
       a -> a+q -> a+2q -> a+3q.
5. Explicit outdegree/deadline bounds for selected fixed anchors.
```

Minimal unsatisfiable cores, if they exist uniformly as the range grows, would identify the missing affine edge-alignment theorem.

## Route Diagnosis

**Proved ledger**

- The simultaneous good-step lemma is false for genuine permutations.
- The stronger “three record coefficients in arithmetic progression on some ray” target is also false as a universal increasing-progression mechanism.
- Increasing-four-term avoidance gives exact adjacent inversion clauses outside the finite sets \(B(a)\).
- These clauses force infinitely many vertices of arbitrarily large forward inversion outdegree.
- Every finite divisor-downset can occur as a single \(B(n)\).
- One inversion can certify arbitrarily many bad steps, and common bad thresholds for finitely many early anchors can be arbitrarily large.

**Plausible but unproved**

- Combining the cofinite adjacent-inversion clauses with transitivity and the prohibition on decreasing four-term progressions may force an affine descending chain.
- A possible sharpened target is an alignment theorem saying that the inversion edges supplied by many overlapping anchors cannot all be dispersed among finite outdegrees without producing
  \[
  a\to a+d\to a+2d\to a+3d.
  \]
  No proof is available.

**Dead ends**

- Forcing a simultaneous good step: explicitly false.
- Replacing consecutive good anchors by three record coefficients in arithmetic progression: explicitly false in the same example.
- Pure \(1/\tau\)-normalized divisor charging: an LCM witness absorbs arbitrary demand.
- Averaging over a fixed finite anchor set: the resulting large outdegrees escape to moving, arbitrarily distant vertices and do not violate order type \(\omega\).

Route A therefore does not close. Once the false record lemma is removed, the remaining task is to align the forced inversion edges while using transitive closure and the absence of decreasing progressions. That is essentially the affine descent-graph problem of Route C, of comparable strength to the original problem. A fresh attempt should focus on finite unsatisfiable affine clause systems with explicit predecessor deadlines, rather than further single-anchor divisor estimates.