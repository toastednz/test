STATUS: BLOCKED

## Result

I did not resolve Erdős Problem #197. I developed an exact append-only formulation of Route 3 and proved several sharp obstructions. In particular, the natural finite extension lemma is false even for locally well-prepared states: there are two disjoint finite avoiding prefixes, satisfying the obvious “no currently stranded integer” invariant, which admit no covering continuation at all. Moreover, an affine copy of this dead-prefix gadget can be appended after any finite collision-free state while preserving all local safety conditions. Thus large reservoirs, appendability, finite insertion, and the most natural collision invariant are insufficient. A successful priority construction would need a substantially stronger global extendibility certificate, apparently comparable in difficulty to the original problem.

## Complete Argument

### 1. Append calculus

For a finite sequence \(P=(p_1,\dots,p_m)\) of distinct positive integers, define its positive forbidden-append set by
\[
F(P)=\{2p_j-p_i:1\le i<j\le m\}\cap\mathbb N.
\]

#### Lemma 1: Append criterion

Suppose \(P\) avoids monotone three-term arithmetic progressions and \(x\notin P\). Then \(P^\frown x\) avoids them if and only if
\[
x\notin F(P).
\]

Moreover,
\[
F(P^\frown x)
=
F(P)\cup \{2x-p_i:1\le i\le m\}\cap\mathbb N.
\]

#### Proof

Every forbidden triple already contained in \(P\) is absent by hypothesis. Any new forbidden triple must use the newly appended \(x\), necessarily as its final temporal term. Thus it has the form
\[
p_i,p_j,x,\qquad i<j,
\]
and is forbidden precisely when
\[
p_i+x=2p_j,
\]
equivalently
\[
x=2p_j-p_i\in F(P).
\]

The formula for \(F(P^\frown x)\) follows because the new ordered pairs are exactly \((p_i,x)\), producing reflected values \(2x-p_i\). ∎

A crucial consequence is monotonicity:
\[
F(P)\subseteq F(P^\frown x).
\]
Therefore, once a target is forbidden from being appended to a sequence, auxiliary appends can never make it appendable there.

---

### 2. The necessary collision invariant

For disjoint finite avoiding sequences \(P_0,P_1\), let
\[
U=P_0\cup P_1.
\]
Call the state **collision-free** if
\[
F(P_0)\cap F(P_1)\subseteq U.
\tag{1}
\]

#### Lemma 2: Collision-freeness is necessary for any covering continuation

If \(P_0,P_1\) are initial prefixes of two avoiding enumerations whose color classes together cover \(\mathbb N\), then (1) holds.

#### Proof

Suppose instead that some unused \(x\notin U\) belongs to both forbidden sets. In the eventual partition, \(x\) belongs to one color, say color \(c\). Since \(P_c\) remains an initial prefix, \(x\) occurs after every member of \(P_c\). But \(x\in F(P_c)\), so Lemma 1 gives a forbidden progression in the eventual color-\(c\) sequence. ∎

If \(x\) is appended to color \(c\), collision-freeness is preserved exactly when

1. \(x\notin F(P_c)\), and
2. for every \(u\in P_c\),
   \[
   2x-u\in F(P_{1-c})\cap\mathbb N
   \quad\Longrightarrow\quad
   2x-u\in U.
   \tag{2}
   \]

Indeed, the only new forbidden values in color \(c\) are \(2x-u\).

#### Proposition 3: Exact fair-path reformulation

The original problem has an affirmative solution if and only if there is an infinite chain of finite states
\[
(P_0^{(s)},P_1^{(s)})\qquad (s=0,1,2,\ldots)
\]
such that:

1. both sequences are initially empty;
2. each step appends one previously unused integer to exactly one sequence;
3. every finite sequence remains avoiding;
4. every integer is eventually appended.

Every such chain is automatically collision-free at every stage.

#### Proof

Given a solution, interleave the two enumerations, always appending the next unused member of one of them. Every finite prefix avoids progressions, every integer eventually appears, and Lemma 2 gives collision-freeness.

Conversely, the limiting sequences produced by a fair chain enumerate two disjoint sets covering \(\mathbb N\). Any forbidden triple in a limiting sequence would already occur at a finite stage, contradicting condition 3. ∎

Thus Route 3 is precisely the problem of finding a fair path through the tree of collision-free finite states.

---

### 3. Reservoir elements always exist, but do not solve coverage

#### Lemma 4: Arbitrarily large safe padding moves

From every finite collision-free state and for either color \(c\), there are arbitrarily large integers that can be appended to color \(c\) while preserving collision-freeness.

#### Proof

Let
\[
H>\max\bigl(U\cup F(P_0)\cup F(P_1)\bigr),
\qquad
M=\max(P_c),
\]
with \(M=0\) if \(P_c\) is empty. Choose \(x\) so large that
\[
x>H,\qquad 2x-M>H.
\]
Then \(x\notin U\cup F(P_c)\), so it is appendable. For every \(u\in P_c\),
\[
2x-u\ge 2x-M>H>\max F(P_{1-c}).
\]
Consequently no new forbidden value in color \(c\) lies in the other forbidden set, and collision-freeness is preserved. ∎

This proves that the extension tree has no terminal vertices. It does not prove the existence of a fair branch: one may append larger and larger safe values while starving a fixed omitted target.

---

### 4. Arbitrary insertion does not give a universal repair

Suppose \(P\) is an avoiding permutation of a subset of \([n-1]\), and we try to insert the new maximum \(n\) without changing the relative order of \(P\). Let a cut \(t\in\{0,\dots,|P|\}\) mean that \(n\) is inserted after exactly \(t\) old entries.

For every progression
\[
z,m,n,\qquad z+n=2m,
\]
contained in \(P\cup\{n\}\):

- if \(z\) precedes \(m\) in \(P\), then \(n\) must be inserted before \(m\), hence
  \[
  t<p_P(m);
  \]
- if \(m\) precedes \(z\), then \(n\) must be inserted after \(m\), hence
  \[
  t\ge p_P(m).
  \]

These conditions are also sufficient, because every new progression must contain \(n\).

For example,
\[
P=(1,4,5,3)
\]
is avoiding. Its only internal progressions are \(1,3,5\) and \(3,4,5\), and their numerical midpoints occur outside the corresponding positional intervals.

Nevertheless, \(7\) cannot be inserted anywhere while preserving this order:

- from \(1,4,7\), since \(1\) precedes \(4\), one needs \(7\) before \(4\), so \(t<2\);
- from \(3,5,7\), since \(5\) precedes \(3\), one needs \(7\) after \(5\), so \(t\ge3\).

No cut satisfies both conditions. Thus even insertion at an arbitrary cut is not a universal finite extension operation.

---

### 5. Prefix-induced precedence graphs

Let \(P\) be a fixed avoiding prefix, and let \(B\) be a finite set disjoint from \(P\), all of whose elements are intended to occur later in the same sequence.

Define a directed graph \(D_P(B)\) on \(B\) by putting
\[
t\longrightarrow m
\]
whenever there exists \(e\in P\) such that
\[
e+t=2m.
\tag{3}
\]
Here \(e,t\) are the numerical endpoints and \(m\) is the numerical midpoint.

#### Lemma 5: Prefix precedence

In every avoiding extension of \(P\) containing all of \(B\) later in the same color, every edge \(t\to m\) of \(D_P(B)\) must satisfy
\[
p(t)<p(m).
\]
In particular, \(D_P(B)\) must be acyclic.

#### Proof

The old endpoint \(e\) occurs before both \(t\) and \(m\). If \(m\) occurred before \(t\), the temporal order would be
\[
e,m,t,
\]
and (3) would make this a forbidden progression. Therefore \(t\) must precede \(m\). A directed cycle would impose a cyclic strict ordering, which is impossible. ∎

There is also a useful special converse.

#### Lemma 6: Finite AP-free suffix criterion

Suppose \(B\) is setwise free of three-term arithmetic progressions. Then an ordering of \(B\) can be appended after \(P\) while preserving avoidance if and only if

1. \(B\cap F(P)=\varnothing\);
2. \(D_P(B)\) is acyclic.

If these conditions hold, any topological ordering of \(D_P(B)\) works.

#### Proof

Necessity follows from Lemmas 1 and 5.

For sufficiency, append a topological ordering of \(D_P(B)\). Consider a progression in \(P\cup B\).

- All three terms in \(P\): safe by hypothesis.
- All three terms in \(B\): impossible because \(B\) is setwise 3-AP-free.
- Exactly one term in \(P\):
  - if the old term is the numerical midpoint, it occurs before both endpoints and is safe;
  - if it is an endpoint, Lemma 5’s edge forces the future endpoint to precede the future midpoint, so the midpoint is not positionally between the endpoints.
- Exactly two terms in \(P\):
  - if the new term is the numerical midpoint, it occurs after both endpoints and is safe;
  - if the new term is an endpoint, the only bad case is that the old endpoint precedes the old midpoint, exactly the condition that the new endpoint belongs to \(F(P)\), excluded by condition 1.

All cases are safe. ∎

The directed-cycle obstruction below is therefore not merely an append artifact; it prevents every ordering of the proposed suffix.

---

### 6. A collision-free state with no covering continuation

Consider
\[
P_0=(5,20),\qquad P_1=(2,6,7,11).
\tag{4}
\]

Both are avoiding. The second underlying set is itself 3-AP-free.

Their forbidden sets are
\[
F(P_0)=\{35\}
\]
and
\[
\begin{aligned}
F(P_1)
&=\{2\cdot6-2,\ 2\cdot7-2,\ 2\cdot11-2,\\
&\qquad 2\cdot7-6,\ 2\cdot11-6,\ 2\cdot11-7\}\\
&=\{10,12,20,8,16,15\}.
\end{aligned}
\]
Thus
\[
F(P_0)\cap F(P_1)=\varnothing,
\]
so this state satisfies the necessary collision invariant.

#### Theorem 7: Dead-prefix gadget

No two avoiding sequences extending the prefixes in (4) can cover both \(10\) and \(15\).

#### Proof

The value \(10\) cannot be assigned to color 1 after \(P_1\), because
\[
2,6,10
\]
would occur in that temporal order and is an arithmetic progression.

Likewise, \(15\) cannot be assigned to color 1 because
\[
7,11,15
\]
would occur in temporal and numerical progression order.

Hence any covering continuation must assign both \(10\) and \(15\) to color 0, after the prefix \((5,20)\).

There are only two possible relative orders.

- If \(10\) occurs before \(15\), then
  \[
  5,10,15
  \]
  occurs in temporal progression order, since \(5\) is already in the prefix.
- If \(15\) occurs before \(10\), then
  \[
  20,15,10
  \]
  occurs in decreasing temporal progression order, since \(20\) is already in the prefix.

Both cases are forbidden. ∎

In terms of the precedence graph,
\[
15\longrightarrow10
\]
is forced by the old endpoint \(5\), while
\[
10\longrightarrow15
\]
is forced by the old endpoint \(20\). Thus \(D_{P_0}(\{10,15\})\) is a directed 2-cycle.

This state is reachable from the empty state using only legal appends and while remaining collision-free throughout. Therefore the collision invariant is not sufficient even locally.

---

### 7. The dead gadget can be placed after any finite state

The obstruction is not confined to small numbers. Let
\[
\phi(t)=Q+Lt,\qquad Q,L\in\mathbb N.
\]
Affine maps preserve arithmetic progressions.

Use the base gadget
\[
S_0=(5,20),\qquad S_1=(2,6,7,11),
\]
with reserved targets \(10,15\).

#### Theorem 8: Ubiquity of locally safe dead ends

Let \(P_0,P_1\) be any disjoint finite avoiding sequences. There are positive integers \(Q,L\) such that appending
\[
\phi(5),\phi(20)
\]
to \(P_0\), and
\[
\phi(2),\phi(6),\phi(7),\phi(11)
\]
to \(P_1\), gives disjoint avoiding prefixes with no covering continuation.

If the original state is collision-free, \(Q,L\) may additionally be chosen so that every intermediate append preserves collision-freeness.

#### Proof

Write
\[
A=\phi(10),\qquad B=\phi(15).
\]
Once the indicated gadget entries have been appended, the same argument as in Theorem 7 applies:

- in color 1,
  \[
  \phi(2),\phi(6),A
  \]
  and
  \[
  \phi(7),\phi(11),B
  \]
  are arithmetic progressions, so neither \(A\) nor \(B\) can occur later in color 1;
- if both are later assigned color 0, then the order \(A\prec B\) creates
  \[
  \phi(5),A,B,
  \]
  while \(B\prec A\) creates
  \[
  \phi(20),B,A.
  \]

It remains to choose \(Q,L\) so that the gadget can be appended safely.

At any gadget append, a forbidden equality involving old entries has one of the forms
\[
Q+tL=C
\]
or
\[
Q+tL=2(Q+sL)-p,
\]
where \(C\) is a forbidden value of an old prefix and \(p\) is an old entry. Each is a proper affine equation in \(Q,L\).

An equality involving only gadget entries reduces to
\[
t=2s-r.
\]
No such equality occurs at an illegal temporal position because \(S_0\) and \(S_1\) are avoiding; indeed \(S_1\) is setwise 3-AP-free.

Disjointness from old values and from the reserved targets likewise excludes only finitely many proper affine equations.

For collision-freeness, newly created forbidden values have one of the forms
\[
2Q+2sL-p
\]
from an old–new pair, or
\[
Q+(2s-r)L
\]
from a new–new pair. The gadget-only reflection sets are
\[
\{35\}
\]
for \(S_0\), and
\[
\{8,10,12,15,16,20\}
\]
for \(S_1\), which are disjoint. Also, the base-coordinate sets \(S_0\) and \(S_1\) are disjoint. Consequently, an unwanted equality between a new forbidden value in one color and a forbidden value in the other color is again a proper affine equation, not an identity.

There are only finitely many such equations. First choose \(L\) avoiding those exceptional equations whose coefficient of \(Q\) is zero. Then choose \(Q\) sufficiently large and outside the finitely many remaining exceptional values. All required inequalities hold simultaneously.

With this choice, every append is legal. In the collision-free case, no newly introduced forbidden value in one color equals a forbidden value in the other, so the original collision intersection is unchanged at every intermediate step. The resulting prefixes nevertheless have no covering continuation by the first part of the proof. ∎

Thus from every collision-free finite state, there are finite sequences of completely locally safe choices leading to a dead end. Local appendability and collision avoidance do not encode extendibility.

---

### 8. Consequence for bounded terminal injury

For every fixed \(K\), no theorem of the form

> every pair of avoiding sequences can be repaired by changing only its last \(K\) entries

can hold.

Indeed, start from the dead prefixes in (4). Recursively append \(K\) very large legal dummy values to each sequence; this is possible by Lemma 4, or simply by avoiding each finite forbidden set. If only the last \(K\) entries may subsequently be altered, the prefixes \((5,20)\) and \((2,6,7,11)\) remain frozen. Theorem 7 then still prevents coverage of \(10\) and \(15\).

Unbounded finite injury is not ruled out, but proving that every element is injured only finitely often would require a new global mechanism.

## Self-Audit

1. **These results do not prove that the original problem has a negative answer.**  
   A successful constructor controls the choices and can avoid the displayed dead prefixes. The affine theorem shows that locally safe bad choices are always available, not that they are unavoidable.

2. **The generic affine argument is the most technical partial result.**  
   Its validity rests on every unwanted condition being a proper affine equation in \(Q,L\). The proof lists all possible types of new forbidden values, and the two gadget reflection sets are explicitly disjoint, ruling out identities. A symbolic finite check is included below.

3. **The append-chain formulation applies only after positions have become genuine prefixes.**  
   A finite-injury construction may temporarily rearrange unfrozen tails. Nevertheless, every eventual \(\omega\)-enumeration has fixed finite prefixes, so the dead-prefix theorem applies once the relevant entries are frozen. What remains unproved is whether an injury strategy can systematically avoid freezing any fatal configuration while still stabilizing every position.

## Computations To Verify

```python
from itertools import product, permutations

def avoids(seq):
    """Check absence of i<j<k with seq[i]+seq[k] == 2*seq[j]."""
    n = len(seq)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if seq[i] + seq[k] == 2 * seq[j]:
                    return False
    return True

def forbidden(seq):
    """Positive forbidden append values."""
    return {
        2 * seq[j] - seq[i]
        for i in range(len(seq))
        for j in range(i + 1, len(seq))
        if 2 * seq[j] - seq[i] > 0
    }

def collision_free(P0, P1):
    U = set(P0) | set(P1)
    return forbidden(P0).intersection(forbidden(P1)) <= U

P0 = [5, 20]
P1 = [2, 6, 7, 11]

assert avoids(P0)
assert avoids(P1)
assert forbidden(P0) == {35}
assert forbidden(P1) == {8, 10, 12, 15, 16, 20}
assert collision_free(P0, P1)
```

Brute-force verification that the targets \(10,15\) cannot be appended in any color assignment or relative order:

```python
targets = [10, 15]
successes = []

for colors in product([0, 1], repeat=2):
    B0 = [targets[i] for i in range(2) if colors[i] == 0]
    B1 = [targets[i] for i in range(2) if colors[i] == 1]

    for q0 in permutations(B0):
        for q1 in permutations(B1):
            if avoids(P0 + list(q0)) and avoids(P1 + list(q1)):
                successes.append((colors, q0, q1))

assert successes == []
```

Insertion-cut example:

```python
P = [1, 4, 5, 3]
assert avoids(P)

possible = []
for cut in range(len(P) + 1):
    Q = P[:cut] + [7] + P[cut:]
    if avoids(Q):
        possible.append(Q)

assert possible == []
```

Prefix precedence graph and cycle test:

```python
def precedence_graph(P, B):
    B = set(B)
    G = {x: set() for x in B}
    for e in P:
        for t in B:
            for m in B:
                if t != m and e + t == 2 * m:
                    G[t].add(m)
    return G

def acyclic(G):
    indeg = {v: 0 for v in G}
    for v in G:
        for w in G[v]:
            indeg[w] += 1
    stack = [v for v in G if indeg[v] == 0]
    seen = 0
    while stack:
        v = stack.pop()
        seen += 1
        for w in G[v]:
            indeg[w] -= 1
            if indeg[w] == 0:
                stack.append(w)
    return seen == len(G)

G = precedence_graph([5, 20], [10, 15])
assert G[15] == {10}
assert G[10] == {15}
assert not acyclic(G)
```

Search for an affine dead gadget after an arbitrary collision-free state:

```python
def try_affine_trap(P0, P1, Lmax=1000, Qmax=10000):
    assert avoids(P0) and avoids(P1)
    assert set(P0).isdisjoint(P1)

    for L in range(1, Lmax + 1):
        for Q in range(1, Qmax + 1):
            phi = lambda t: Q + L * t
            steps = [
                (0, phi(5)),
                (0, phi(20)),
                (1, phi(2)),
                (1, phi(6)),
                (1, phi(7)),
                (1, phi(11)),
            ]

            A, B = phi(10), phi(15)
            q0, q1 = list(P0), list(P1)
            used = set(q0) | set(q1)
            if A in used or B in used:
                continue

            okay = True
            for c, x in steps:
                if x in used:
                    okay = False
                    break
                if c == 0:
                    q0.append(x)
                else:
                    q1.append(x)
                used.add(x)

                if not avoids(q0) or not avoids(q1):
                    okay = False
                    break
                if not set(q0).isdisjoint(q1):
                    okay = False
                    break
                if collision_free(P0, P1) and not collision_free(q0, q1):
                    okay = False
                    break

            if okay:
                # Direct finite target check.
                target_success = False
                for colors in product([0, 1], repeat=2):
                    C0 = [x for x, c in zip([A, B], colors) if c == 0]
                    C1 = [x for x, c in zip([A, B], colors) if c == 1]
                    for r0 in permutations(C0):
                        for r1 in permutations(C1):
                            if avoids(q0 + list(r0)) and avoids(q1 + list(r1)):
                                target_success = True
                assert not target_success
                return Q, L, q0, q1, A, B

    return None

assert try_affine_trap([], []) is not None
```

A bounded search for fair-path strategies should represent a state by two tuples and prune at least by collision-freeness and prefix-graph cycles:

```python
def safe_children(state, value_bound):
    P0, P1 = state
    used = set(P0) | set(P1)

    for x in range(1, value_bound + 1):
        if x in used:
            continue

        for c in (0, 1):
            Q0, Q1 = list(P0), list(P1)
            if c == 0:
                if x in forbidden(Q0):
                    continue
                Q0.append(x)
            else:
                if x in forbidden(Q1):
                    continue
                Q1.append(x)

            if collision_free(Q0, Q1):
                yield (tuple(Q0), tuple(Q1))
```

Useful computational questions are:

1. What is the smallest collision-free dead prefix pair?
2. Under the requirement that all of \([N]\) have appeared, how small can a forced precedence cycle on two omitted targets be?
3. Can one maintain acyclicity of all bounded prefix-precedence graphs while forcing the least omitted integer to appear within a prescribed delay?
4. Do digital or block constructions naturally prevent the affine four-term trap?

## Route Diagnosis

**Proved ledger**

- Exact append criterion and monotonicity of forbidden sets.
- Collision-freeness is necessary for every viable pair of frozen prefixes.
- The original problem is equivalent to finding a fair infinite path through the tree of avoiding prefix pairs.
- Arbitrarily large locally safe reservoir moves always exist.
- Relative-order-preserving insertion can fail even for the new numerical maximum.
- Frozen prefixes impose a directed precedence graph on future same-color elements.
- A directed cycle is an absolute extension obstruction.
- The explicit collision-free prefixes
  \[
  (5,20),\qquad(2,6,7,11)
  \]
  have no covering continuation.
- Affine copies of this dead gadget can be safely installed after any finite collision-free state.
- No uniformly bounded terminal-injury lemma is possible.

**Plausible but unproved**

- A viable priority construction may need to maintain well-foundedness of an infinite family of forced-color precedence graphs, not merely absence of current common forbidden values.
- Multiscale or digital structure might provide such a well-foundedness certificate.
- Recovering the known three-color construction may reveal how a third state prevents the two-cycle gadget and whether that protection can be compressed to two colors.

**Dead ends**

- Appending auxiliary numbers to unblock a target: impossible because forbidden sets only grow.
- Arbitrary insertion while preserving old relative order: explicitly false.
- Collision-freeness as the sole preparation invariant: explicitly insufficient.
- Universal finite extension from every avoiding prefix pair: explicitly false.
- Fixed-size terminal repair: explicitly false.
- Mere existence of arbitrarily large safe moves: gives infinite injective paths but no coverage.

The Route 3 block is now precise. A successful priority proof must identify a class of “prepared” states that excludes not only immediate collisions but every forced precedence cycle, prove that the class is preserved while meeting the next coverage requirement, and prove stabilization. No such invariant emerged; formulating it without essentially encoding the existence of a full continuation appears comparable in strength to the original problem.

A fresh attempt should therefore either:

1. recover the three-color construction and interpret it through these prefix-precedence graphs, looking for the exact role of the third state; or
2. search computationally for digital/block rules that provably forbid the affine two-cycle gadget at every scale while retaining order type \(\omega\).

Without such additional structure, Route 3 is blocked.