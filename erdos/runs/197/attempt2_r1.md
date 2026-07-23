STATUS: BLOCKED

## Result

I did not resolve Erdős Problem #197 or the satisfiability of all ternary shell instances. I obtained an exact ternary renormalization of both internal AP constraints and incoming edges: only carries in \(\{-1,0,1\}\), together with one alternating base-shell anomaly, occur. However, finite carry does not by itself give a finite-state substitution. I also proved that three natural coarse substitution mechanisms are impossible: the residue children cannot be contiguous, the three siblings \(3q,3q+1,3q+2\) cannot be emitted as contiguous packets, and a most-significant-digit decomposition into three contiguous numerical thirds cannot work. Thus any successful Route-1 construction must use genuine, overlapping interleavings of the three residue children.

## Complete Argument

### 1. Exact ternary carry recursion

Write
\[
X_k=[M,3M-1],\qquad M=3^k.
\]
Then
\[
X_{k+1}=[3M,9M-1]
       =\bigsqcup_{r=0}^2 C_r,
\qquad
C_r=\{3q+r:q\in X_k\}.
\]

#### Lemma 1: Internal AP carries

Let
\[
A=3a+r,\qquad B=3b+s,\qquad C=3c+t,
\]
where \(r,s,t\in\{0,1,2\}\). Then
\[
A+C=2B
\]
if and only if
\[
a+c-2b=\frac{2s-r-t}{3}.
\]
Consequently the quotient defect belongs to
\[
a+c-2b\in\{-1,0,1\}.
\]

Moreover, the possible residue patterns are exactly:

1. \(r=s=t\), with quotient defect \(0\);
2. \(s=0\), \(\{r,t\}=\{1,2\}\), with quotient defect \(-1\);
3. \(s=1\), \(\{r,t\}=\{0,2\}\), with quotient defect \(0\);
4. \(s=2\), \(\{r,t\}=\{0,1\}\), with quotient defect \(1\).

**Proof.**
Substitution gives
\[
3(a+c-2b)+(r+t-2s)=0.
\]
Since \(r+t-2s\in[-4,4]\) and is divisible by \(3\), it belongs to \(\{-3,0,3\}\). This gives the three possible quotient defects. Direct enumeration of the residues gives the stated list. ∎

Thus cross-residue APs project not merely to APs of quotients but also to the two near-AP relations
\[
a+c=2b-1,\qquad a+c=2b+1.
\]

#### Lemma 2: Exact recursion for the old-root sets

Let
\[
L(S)=\{3x+r:x\in S,\ r\in\{0,1,2\}\}.
\]
Then
\[
U_{k+1}=
\begin{cases}
L(U_k),&k\ \text{even},\\[1mm]
L(U_k)\cup I_0,&k\ \text{odd},
\end{cases}
\qquad I_0=\{1,2\}.
\]

**Proof.**
Multiplication by \(3\) with all three residues maps \(I_j\) bijectively onto \(I_{j+1}\):
\[
I_{j+1}=L(I_j).
\]
If \(k\) is even, then
\[
U_k=I_{k-2}\cup I_{k-4}\cup\cdots\cup I_0,
\]
and hence
\[
L(U_k)=I_{k-1}\cup I_{k-3}\cup\cdots\cup I_1=U_{k+1}.
\]
If \(k\) is odd, then \(U_k\) ends with \(I_1\), so \(L(U_k)\) ends with \(I_2\), whereas \(U_{k+1}\) also contains \(I_0\). ∎

#### Lemma 3: Incoming-edge carries

Let
\[
Y=3b+s,\qquad Z=3c+t.
\]
Write uniquely
\[
2s-t=3\lambda+u,\qquad
\lambda\in\{-1,0,1\},\quad u\in\{0,1,2\}.
\]
Then
\[
2Y-Z=3(2b-c+\lambda)+u.
\]
Consequently,
\[
2Y-Z\in U_{k+1}
\]
if and only if either

\[
2b-c+\lambda\in U_k,
\]
or
\[
k\ \text{is odd},\qquad
2b-c+\lambda=0,\qquad u\in\{1,2\}.
\]

**Proof.**
The identity is immediate:
\[
2Y-Z=3(2b-c)+(2s-t).
\]
The membership characterization follows from Lemma 2 and uniqueness of quotient and remainder modulo \(3\). The second alternative is exactly the exceptional contribution \(I_0=\{1,2\}\). ∎

In particular, the arithmetic carries themselves are finite-state. What is not yet finite-state is the order information needed to handle all quotient triples and all predicates
\[
2b-c+\lambda\in U_k.
\]

#### Corollary 4: Necessary child states

If a permutation solves \(\mathcal F_{k+1}\), then its restriction to each residue child \(C_r\), mapped back by
\[
3q+r\longmapsto q,
\]
solves \(\mathcal F_k\).

When \(k\) is odd and \(r\in\{1,2\}\), the restriction also satisfies the extra incoming relations corresponding to quotient root \(0\).

**Proof.**
An internal AP contained in one \(C_r\) maps to an AP of quotients by Lemma 1. If \(2b-c\in U_k\), then
\[
3(2b-c)+r\in L(U_k)\subseteq U_{k+1},
\]
so the corresponding incoming edge is inherited. The exceptional root-zero relations are precisely those described in Lemma 3. ∎

Thus any valid state library needs at least an alternating base flag; one unadorned child state is insufficient.

---

### 2. Incoming edges have only one generation of forced continuation

The incoming edge \(z\triangleleft y\) can force one additional internal edge.

#### Lemma 5: Ray propagation

Let \(k\ge2\), \(x\in U_k\), and
\[
t_j=x+jd.
\]
Suppose \(t_1,t_2\in X_k\). Every solution of \(\mathcal F_k\) satisfies
\[
t_2\triangleleft t_1.
\]
If \(t_3\in X_k\), it must also satisfy
\[
t_2\triangleleft t_3.
\]
Moreover,
\[
t_4\notin X_k.
\]

**Proof.**
The first relation is exactly the incoming constraint arising from the old-root AP
\[
(x,t_1,t_2).
\]
If \(t_3\in X_k\), then
\[
(t_1,t_2,t_3)
\]
is an internal AP. Its midpoint \(t_2\) already precedes the endpoint \(t_1\); hence it cannot be after both endpoints and therefore must be before both. Thus \(t_2\triangleleft t_3\).

Finally,
\[
x\le \max U_k=\frac M3-1.
\]
Since \(t_1=x+d\ge M\),
\[
d\ge M-x.
\]
Therefore
\[
t_4=x+4d
   \ge x+4(M-x)
   =4M-3x
   \ge4M-3\left(\frac M3-1\right)
   =3M+3.
\]
But \(X_k\) ends at \(3M-1\), so \(t_4\notin X_k\). ∎

This bounded propagation is favorable for a finite-state approach, but interactions between different old-root rays remain uncontrolled.

---

### 3. The residue children cannot be contiguous

#### Lemma 6: No residue-block substitution

No AP-avoiding permutation of \(X_{k+1}\) can make all three residue children
\[
C_0,\ C_1,\ C_2
\]
contiguous blocks.

**Proof.**
Choose \(q\in[M,3M-2]\). The following three APs all lie in \(X_{k+1}\):
\[
(3q,3q+1,3q+2),
\]
\[
(3q+1,3q+2,3q+3),
\]
\[
(3q+2,3q+3,3q+4).
\]
Their midpoint residues are respectively
\[
1,\quad2,\quad0.
\]

If each residue class is a contiguous block, then for a triple using all three residue blocks, the temporal betweenness of its entries is determined entirely by the order of the blocks. Therefore the three displayed APs require each of \(C_0,C_1,C_2\) to be an extremal block relative to the other two.

A linear order of three blocks has only two extremal blocks. Contradiction. ∎

Hence the permission to interleave the residue children is not optional.

---

### 4. Contiguous sibling packets are also impossible

A different natural template is to process quotient values \(q\) one at a time, emitting the packet
\[
P_q=\{3q,3q+1,3q+2\}
\]
contiguously. This also cannot work.

#### Lemma 7: Packet contiguity induces rounded-midpoint avoidance

Let \(Q\) be an interval of quotient values. Suppose an AP-avoiding parent permutation makes every packet \(P_q\), \(q\in Q\), contiguous. Then the induced order \(\prec_Q\) of the packets has the following property:

For every
\[
a<b<c\quad\text{in }Q
\]
such that
\[
|a+c-2b|\le1,
\]
the packet \(P_b\) is not temporally between \(P_a\) and \(P_c\).

**Proof.**
The disjoint contiguous packets induce a total order.

If \(a+c-2b=0\), use the lifted AP
\[
(3a,3b,3c).
\]

If \(a+c-2b=-1\), then
\[
(3a+1,\ 3b,\ 3c+2)
\]
is an AP, since
\[
(3a+1)+(3c+2)-2(3b)=3(a+c-2b)+3=0.
\]

If \(a+c-2b=1\), then
\[
(3a,\ 3b+2,\ 3c+1)
\]
is an AP, since
\[
3(a+c-2b)+(0+1-4)=0.
\]

Because \(a<b<c\), these three values lie in increasing numerical order and in three distinct packets. Thus the middle packet cannot be temporally between the endpoint packets. ∎

#### Lemma 8: Five consecutive quotient packets already make this impossible

There is no total order on \(\{0,1,2,3,4\}\) such that for every
\[
a<b<c,\qquad |a+c-2b|\le1,
\]
the element \(b\) is not between \(a\) and \(c\).

**Proof.**
Let \(e\) be the first element of the putative order. Reflection \(i\mapsto4-i\) preserves the condition, so it suffices to consider \(e=0,1,2\).

If \(e=0\), the triples \(012,013,023,024\) force
\[
2\prec1,\qquad3\prec1,\qquad3\prec2,\qquad4\prec2.
\]
Thus
\[
3\prec2\prec1,
\]
which places the midpoint \(2\) between the endpoints \(1,3\) in the required triple \(123\).

If \(e=1\), the triples \(123,124,134\) force
\[
3\prec2,\qquad4\prec2,\qquad4\prec3.
\]
Thus
\[
4\prec3\prec2,
\]
contradicting the required triple \(234\).

If \(e=2\), the triples \(012\) and \(234\) force
\[
0\prec1,\qquad4\prec3.
\]
In the required triple \(013\), the relation \(0\prec1\) forces
\[
3\prec1.
\]
In the required triple \(134\), the relation \(4\prec3\) forces
\[
1\prec3.
\]
This is a contradiction.

The cases \(e=3,4\) follow by reflection. ∎

#### Corollary 9: No packet substitution

If \(Q\) contains five consecutive quotient values, no AP-avoiding permutation can emit every packet \(P_q\) contiguously.

In particular, this fails for every ternary parent shell in the proposed induction.

This rules out a broad class of natural element-by-element substitutions, even when the internal ordering of each packet is allowed to depend arbitrarily on \(q\) and on a finite state.

---

### 5. Most-significant ternary blocks cannot be substituted contiguously either

One possible alternative to residue children is to divide a ternary interval into three consecutive numerical thirds. This also fails.

#### Lemma 10: No contiguous numerical-thirds order

Let \(M\ge2\), and partition
\[
[0,3M-1]=B_0\sqcup B_1\sqcup B_2,
\qquad
B_i=[iM,(i+1)M-1].
\]
No AP-avoiding permutation can make all three \(B_i\) contiguous.

**Proof.**
The AP
\[
(0,M,2M)
\]
uses one element of each block. Therefore \(B_1\) must occur either before both \(B_0,B_2\), or after both.

Set
\[
d=\left\lceil\frac M2\right\rceil,\qquad x=M-d.
\]
Then
\[
x,\quad u=M,\quad v=M+d,\quad z=M+2d
\]
is a four-term AP with
\[
x\in B_0,\qquad u,v\in B_1,\qquad z\in B_2.
\]

If \(B_1\) occurs before both other blocks, the AP \((x,u,v)\) requires
\[
u\triangleleft v,
\]
whereas \((u,v,z)\) requires
\[
v\triangleleft u.
\]

If \(B_1\) occurs after both other blocks, the first AP requires
\[
v\triangleleft u,
\]
while the second requires
\[
u\triangleleft v.
\]

Both cases are impossible. ∎

Thus switching from least-significant residue children to contiguous most-significant ternary blocks does not repair the construction.

---

### 6. Precise remaining obstruction

Lemmas 1–3 show that ternary renormalization has only finitely many arithmetic carries. Nevertheless, Lemmas 6–10 show that this finite carry cannot be represented by any of the following coarse states:

1. a total order of the three residue children;
2. a quotient order with each sibling packet contiguous;
3. a total order of three consecutive numerical thirds.

A successful substitution must therefore allow the spans of many sibling packets to overlap and must retain enough information to decide the cross-track constraints
\[
a+c-2b\in\{-1,0,1\}
\]
and
\[
2b-c+\lambda\in U_k,\qquad \lambda\in\{-1,0,1\}.
\]
I have not found a finite state set closed under these requirements. Proving that such a set exists is essentially the unproved key lemma of Route 1, rather than a reduced statement of demonstrably smaller strength.

## Self-Audit

1. **The no-go theorems concern only coarse substitutions.**  
   They do not show that a genuinely interleaved finite-state construction is impossible, nor that any \(\mathcal F_k\) is unsatisfiable. I believe the stated scope is exact because each proof explicitly assumes contiguity and uses nothing beyond it.

2. **The base-shell anomaly in Lemma 3 is an easy place for an indexing error.**  
   The formula was checked directly from
   \[
   U_{k+1}=L(U_k)
   \quad\text{or}\quad
   L(U_k)\cup\{1,2\},
   \]
   according to the parity of \(k\). It agrees with the initial examples
   \[
   U_1=\varnothing,\quad U_2=\{1,2\},\quad
   U_3=[3,8],\quad U_4=[1,2]\cup[9,26].
   \]

3. **Ray propagation is only a necessary closure rule.**  
   It does not capture interactions among different APs, so it is not a satisfiability criterion. The local implication itself is rigorous: it follows directly from midpoint non-betweenness, and the assertion that \(t_4\) lies outside the shell follows from the exact upper bound on \(U_k\).

## Computations To Verify

The following script generates and solves exact shell instances with OR-Tools, independently verifies witnesses, checks the packet obstruction, and checks the extra ray-propagation relations.

```python
from itertools import combinations, permutations
from ortools.sat.python import cp_model


def shell_data(k):
    M = 3 ** k
    X = list(range(M, 3 * M))

    U = set()
    for j in range(0, k - 1):
        if j % 2 == k % 2:
            U.update(range(3 ** j, 3 ** (j + 1)))

    aps = []
    for d in range(1, M):
        for a in range(M, 3 * M - 2 * d):
            aps.append((a, a + d, a + 2 * d))

    edges = set()
    edge_roots = {}
    for x in U:
        for y in X:
            z = 2 * y - x
            if y < z < 3 * M:
                edges.add((z, y))
                edge_roots[(z, y)] = x

    return M, X, U, aps, sorted(edges), edge_roots


def verify_shell(k, perm, verbose=True):
    M, X, U, aps, edges, edge_roots = shell_data(k)

    if len(perm) != len(X) or set(perm) != set(X):
        if verbose:
            print("Not a permutation of the shell.")
        return False

    pos = {v: i for i, v in enumerate(perm)}

    for z, y in edges:
        if not pos[z] < pos[y]:
            if verbose:
                print("Incoming edge failed:", z, "->", y,
                      "root", edge_roots[(z, y)])
            return False

    for a, b, c in aps:
        if not (pos[b] < min(pos[a], pos[c])
                or pos[b] > max(pos[a], pos[c])):
            if verbose:
                print("Internal AP failed:", (a, b, c),
                      "positions", (pos[a], pos[b], pos[c]))
            return False

    # Check the forced continuation from Lemma 5.
    for (z, y), x in edge_roots.items():
        d = y - x
        assert z == x + 2 * d
        t3 = x + 3 * d
        if M <= t3 < 3 * M:
            if not pos[z] < pos[t3]:
                if verbose:
                    print("Propagation failed:", z, "->", t3,
                          "from root", x)
                return False

        t4 = x + 4 * d
        assert t4 >= 3 * M

    if verbose:
        print("Verified shell", k)
    return True


def solve_shell(k, time_limit=3600, workers=8):
    M, X, U, aps, edges, edge_roots = shell_data(k)
    n = len(X)

    print("k =", k, "M =", M, "|X| =", n,
          "|U| =", len(U), "APs =", len(aps),
          "edges =", len(edges))

    assert len(aps) == M * (M - 1)

    model = cp_model.CpModel()
    p = {v: model.NewIntVar(0, n - 1, f"p_{v}") for v in X}
    model.AddAllDifferent(list(p.values()))

    for z, y in edges:
        model.Add(p[z] < p[y])

    for idx, (a, b, c) in enumerate(aps):
        midpoint_first = model.NewBoolVar(f"mf_{idx}")

        model.Add(p[b] < p[a]).OnlyEnforceIf(midpoint_first)
        model.Add(p[b] < p[c]).OnlyEnforceIf(midpoint_first)

        model.Add(p[a] < p[b]).OnlyEnforceIf(midpoint_first.Not())
        model.Add(p[c] < p[b]).OnlyEnforceIf(midpoint_first.Not())

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = workers
    solver.parameters.log_search_progress = True

    status = solver.Solve(model)
    print("status:", solver.StatusName(status))

    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        perm = sorted(X, key=lambda v: solver.Value(p[v]))
        assert verify_shell(k, perm)
        print("witness =", perm)
        print("residue word =", "".join(str(v % 3) for v in perm))
        return perm

    return None


def check_balanced_quotient_obstruction():
    vals = range(5)
    required = [
        (a, b, c)
        for a, b, c in combinations(vals, 3)
        if abs(a + c - 2 * b) <= 1
    ]

    witnesses = []
    for perm in permutations(vals):
        pos = {v: i for i, v in enumerate(perm)}
        ok = all(
            pos[b] < min(pos[a], pos[c])
            or pos[b] > max(pos[a], pos[c])
            for a, b, c in required
        )
        if ok:
            witnesses.append(perm)

    print("Required rounded-midpoint triples:", required)
    print("Number of valid orders:", len(witnesses))
    assert len(witnesses) == 0


def check_carry_table():
    for r in range(3):
        for s in range(3):
            for t in range(3):
                numerator = 2 * s - r - t
                if numerator % 3 == 0:
                    defect = numerator // 3
                    assert defect in (-1, 0, 1)
                    print((r, s, t), "quotient defect", defect)


if __name__ == "__main__":
    check_balanced_quotient_obstruction()
    check_carry_table()

    # Run in increasing order. No outcome is assumed here.
    for k in [2, 3, 4]:
        perm = solve_shell(k, time_limit=3600)
        if perm is None:
            break
```

For Route-1 witness mining, the most important additional statistics are:

```python
def packet_spans(perm):
    pos = {v: i for i, v in enumerate(perm)}
    qs = sorted(set(v // 3 for v in perm))
    spans = {}
    for q in qs:
        locations = sorted(pos[3 * q + r] for r in range(3))
        spans[q] = (locations[0], locations[-1], tuple(locations))
    return spans


def packet_overlap_depth(perm):
    spans = packet_spans(perm)
    depth = 0
    for i in range(len(perm)):
        active = sum(lo <= i <= hi for lo, hi, _ in spans.values())
        depth = max(depth, active)
    return depth
```

If the minimum packet-overlap depth grows rapidly with \(k\), bounded-width packet transducers are unlikely. If it stabilizes, the overlapping packet patterns should be canonicalized and used as candidate finite states.

## Route Diagnosis

**Proved ledger**

- Exact quotient defects for cross-residue APs are \(-1,0,1\).
- Exact incoming-edge carries are \(-1,0,1\), with one parity-dependent root-\(0\) anomaly.
- Every parent residue child inherits a valid smaller shell state, sometimes with extra root-\(0\) constraints.
- Incoming rays force at most one additional shell edge.
- Contiguous residue-child substitution is impossible.
- Contiguous sibling-packet substitution is impossible; the obstruction already occurs on five quotient values.
- Contiguous most-significant ternary thirds are impossible.

**Plausible but unproved**

- Individual shell instances \(\mathcal F_k\) may all remain satisfiable.
- A finite library based on overlapping packet spans or bounded-width three-track interleavings may exist.
- The bounded depth of incoming-ray propagation may help keep the required state library finite.

**Dead ends**

- Ordering the three residue children as blocks.
- Processing quotient values through contiguous triples \((3q,3q+1,3q+2)\).
- Replacing residue recursion by contiguous numerical thirds.
- Treating the finite carry alphabet alone as proof of finite-state closure.

**Precise block**

The missing theorem is an element-level interleaving substitution handling all near-AP quotient relations and all incoming carry predicates while preserving transitivity. I have neither a template library nor a proof that only finitely many boundary signatures suffice. This is of essentially the same strength as the Route-1 key lemma, so the route is presently blocked.

A fresh attempt should first solve \(\mathcal F_2,\ldots,\mathcal F_5\), then measure packet-overlap depth and extract canonical three-track schedules. Any candidate state must explicitly encode the alternating root-\(0\) anomaly and must not collapse the shell to a single quotient order, since Lemmas 7–8 prove that such a collapse is impossible.