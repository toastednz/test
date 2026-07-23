STATUS: BLOCKED

## Result

I did not solve Erdős Problem #1212. Route 4 can be reduced exactly to a rooted extension problem on a “coarse” graph of odd-odd vertices, but uniform local branching is false: there are admissible isolated vertices, and CRT can place completely invisible square walls of any prescribed radius around specially chosen admissible roots. I proved a finite-state periodic criterion whose satisfaction would yield a monotone admissible ray; thus a finite directed-cycle certificate could solve the problem. A complete hand check shows that the first natural modulus-\(30\), narrow-strip automaton has no such cycle. The remaining block is to prove that some larger finite automaton contains a cycle, or to find a genuinely rooted branching invariant that survives the CRT obstructions.

## Complete Argument

### 1. Exact parity reduction

Let
\[
O=\{(x,y)\in A:x\ \text{and}\ y\ \text{are odd}\}.
\]

Define a graph \(K\) with vertex set \(O\), joining two vertices when they differ by \(2\) in exactly one coordinate and their midpoint belongs to \(A\). Thus, for example,
\[
(x,y)\sim_K(x+2,y)
\]
if and only if
\[
(x,y),\ (x+1,y),\ (x+2,y)\in A.
\]

#### Lemma 1
The graph \(H\) contains a ray if and only if \(K\) contains a ray.

#### Proof

No visible point has both coordinates even. If a visible point has parity even-odd, then changing its odd coordinate produces an even-even point, so all its possible neighbors lie in the horizontal direction and are odd-odd. Similarly, a point of parity odd-even can only have vertical odd-odd neighbors.

Consequently, every edge of \(H\) joins an odd-odd vertex to a mixed-parity vertex, and every mixed-parity vertex has at most two neighbors, namely the two odd-odd points for which it is the midpoint.

Expanding every edge of a ray in \(K\) through its midpoint gives a ray in \(H\). The expanded path is simple because a midpoint uniquely determines the corresponding coarse edge.

Conversely, a ray in \(H\) alternates between odd-odd and mixed-parity vertices. It therefore contains infinitely many odd-odd vertices. Contracting each pair of consecutive edges through a mixed-parity vertex gives a ray in \(K\). Simplicity is preserved because the original ray does not repeat vertices. ∎

This reduction removes the forced straight movement through mixed-parity vertices. All genuine branching occurs at odd-odd vertices.

For an odd-odd point write
\[
d=y-x.
\]
For north-east coarse moves, where all intermediate even coordinates are at least \(4\), the arithmetic is exact:

- A north move
  \[
  (x,y)\longrightarrow (x,y+2)
  \]
  is legal if and only if the endpoint is admissible and
  \[
  \gcd(x,d+1)=\gcd(x,d+2)=1.
  \]

- An east move
  \[
  (x,y)\longrightarrow (x+2,y)
  \]
  is legal if and only if the endpoint is admissible and
  \[
  \gcd(x+1,d-1)=\gcd(x+2,d-2)=1.
  \]

Indeed,
\[
\gcd(x,y+1)=\gcd(x,d+1),\qquad
\gcd(x,y+2)=\gcd(x,d+2),
\]
and similarly for the horizontal move.

Thus Route 4 may be implemented on the finitely branching tree of self-avoiding paths in \(K\). However, the next results show that no extension theorem can apply to all sufficiently large admissible vertices without additional hypotheses.

---

### 2. A concrete admissible isolated vertex

#### Lemma 2
The point
\[
(1581,35)
\]
is an isolated vertex of \(H\).

#### Proof

We have
\[
1581=3\cdot17\cdot31,\qquad 35=5\cdot7,
\]
and
\[
1581\equiv 6\pmod {35},
\]
so \(\gcd(1581,35)=1\). Both coordinates are composite, hence the point belongs to \(A\).

Its four grid neighbors are all invisible:
\[
\gcd(1580,35)=5,
\]
\[
\gcd(1582,35)=7,
\]
\[
\gcd(1581,34)=17,
\]
and
\[
\gcd(1581,36)=3.
\]
Therefore it has degree zero in \(H\). ∎

This is a direct counterexample to any proposed lemma asserting that every admissible vertex has an admissible continuation.

---

### 3. CRT walls around specially chosen roots

The preceding isolated point is not exceptional: arbitrary finite-radius traps can be placed at sufficiently favorable translations.

#### Theorem 3
For every \(R\geq 1\) and every \(B\geq1\), there exist \(X,Y>B\) such that:

1. \((X,Y)\in A\);
2. every lattice point
   \[
   (X+i,Y+j),\qquad \max(|i|,|j|)=R,
   \]
   is invisible;
3. consequently, the component of \((X,Y)\) in \(H\) is finite.

#### Proof

Let
\[
S_R=\{(i,j)\in\mathbb Z^2:\max(|i|,|j|)=R\}.
\]
For every \(s=(i,j)\in S_R\), choose a distinct odd prime
\[
p_s>2R.
\]
Choose one further odd prime \(q\), distinct from all the \(p_s\).

Apply the Chinese remainder theorem to the congruences
\[
X\equiv-i\pmod {p_s},\qquad
Y\equiv-j\pmod {p_s}
\]
for every \(s=(i,j)\in S_R\), together with
\[
X\equiv0\pmod q,\qquad Y\equiv1\pmod q.
\]
Let \(M=q\prod_{s\in S_R}p_s\), and let \(a,b\) be the resulting residue classes for \(X,Y\) modulo \(M\).

For every prime \(\ell\mid M\), the two residues \(a,b\) are not both zero modulo \(\ell\). This is clear for \(\ell=q\). If \(\ell=p_s\) for \(s=(i,j)\), then simultaneous vanishing would imply
\[
i\equiv j\equiv0\pmod {p_s}.
\]
Since \(|i|,|j|\leq R<p_s\), this would force \(i=j=0\), contrary to \(s\in S_R\).

Choose
\[
X=a+kM
\]
so large that
\[
X>B+R+2,\qquad X>q.
\]
Then \(q\mid X\), so \(X\) is composite.

It remains to choose \(Y=b+lM\) coprime to this fixed \(X\). Let \(\ell\) run over the distinct prime divisors of \(X\).

- If \(\ell\mid M\), then \(\ell\mid X\) implies \(a\equiv0\pmod\ell\), and hence \(b\not\equiv0\pmod\ell\). Therefore no choice of \(l\) makes \(\ell\mid Y\).

- If \(\ell\nmid M\), exactly one residue class of \(l\pmod\ell\) satisfies
  \[
  b+lM\equiv0\pmod\ell.
  \]
  Choose any different residue.

There are only finitely many prime divisors of \(X\), so CRT supplies an integer \(l\) simultaneously avoiding all the forbidden residue classes. Adding a sufficiently large multiple of their product, if necessary, makes
\[
Y=b+lM>B+R+2.
\]
Then \(\gcd(X,Y)=1\). Since \(X\) is composite, \((X,Y)\in A\).

For \(s=(i,j)\in S_R\), the prime \(p_s\) divides both
\[
X+i\quad\text{and}\quad Y+j.
\]
Thus every point of the translated square boundary is invisible.

A nearest-neighbor path from \((X,Y)\) to outside
\[
\{(X+i,Y+j):\max(|i|,|j|)<R\}
\]
must first meet the boundary \(\max(|i|,|j|)=R\), which contains no visible points. Hence the component of \((X,Y)\) is contained in a finite box. ∎

This theorem does not disprove the problem, because the trapped root depends on \(R\). It does show that arbitrarily large coordinates and arbitrarily large local boxes do not by themselves imply future extendability.

For comparison, arbitrarily long admissible paths with varying roots are elementary. Given \(L\), choose a prime \(P>L+2\). Then
\[
(2,P^2),(3,P^2),\ldots,(L+2,P^2)
\]
is an admissible path of length \(L\): every \(x<P\) is coprime to \(P^2\), and the fixed coordinate \(P^2\) is composite. This emphasizes why the root must remain fixed.

---

### 4. A finite-state periodic criterion for a ray

The most promising concrete realization of Route 4 is to quotient a family of frontier states by congruence classes.

For an even integer \(T\), define
\[
\mathcal S_T
=
\{n\in\mathbb Z\setminus\{0\}:
\text{every prime divisor of }n\text{ divides }T\}.
\]

#### Lemma 4
Let \(T\geq2\), \(n\neq0\), and \(\gcd(a,n)=1\). Then
\[
\gcd(a+kT,a+kT+n)=1
\quad\text{for every }k\geq0
\]
if and only if every prime divisor of \(n\) divides \(T\).

#### Proof

Since
\[
\gcd(a+kT,a+kT+n)=\gcd(a+kT,n),
\]
suppose first that every prime divisor \(p\mid n\) also divides \(T\). Then
\[
a+kT\equiv a\not\equiv0\pmod p
\]
for every \(p\mid n\), so the gcd is \(1\).

Conversely, if some prime \(p\mid n\) does not divide \(T\), then \(T\) is invertible modulo \(p\). Hence
\[
a+kT\equiv0\pmod p
\]
has a solution \(k\pmod p\), and therefore infinitely many nonnegative solutions. For such \(k\), the gcd is divisible by \(p\). ∎

Now fix a finite set \(D\) of nonzero even integers. Define a finite directed graph \(Q(T,D)\).

A state is a pair
\[
(r,d),\qquad r\in\mathbb Z/T\mathbb Z,\quad r\ \text{odd},\quad d\in D,
\]
satisfying:

1. \(d\in\mathcal S_T\);
2. \(\gcd(r,d)=1\);
3. for some odd prime \(p\mid T\),
   \[
   p\mid r\quad\text{or}\quad p\mid r+d.
   \]

The third condition certifies that one of the two odd coordinates is always composite under translation by a multiple of \(T\).

There is a directed north edge
\[
(r,d)\longrightarrow(r,d+2)
\]
when the target is a state and
\[
d+1\in\mathcal S_T,\qquad \gcd(r,d+1)=1.
\]

There is a directed east edge
\[
(r,d)\longrightarrow(r+2,d-2)
\]
when the target is a state and
\[
d-1\in\mathcal S_T,\qquad \gcd(r+1,d-1)=1.
\]

All residues in these conditions are taken modulo \(T\). The smoothness assumptions make the coprimality conditions independent of the choice of representative.

#### Theorem 5
If \(Q(T,D)\) contains a directed cycle, then \(H\) contains a monotone ray. In fact, the ray can be chosen periodic up to diagonal translation.

#### Proof

Let \(C\) be a directed cycle. A north edge increases \(d\) by \(2\), while an east edge decreases \(d\) by \(2\). Since the cycle returns to the same exact value of \(d\), it contains equally many north and east edges; denote this number by \(q\geq1\).

Only east edges change \(r\), each by \(2\). Since the residue returns to its initial value,
\[
2q\equiv0\pmod T.
\]
Thus
\[
2q=mT
\]
for some positive integer \(m\).

Choose an odd integer \(x_0\) in the initial residue class and sufficiently large that every coordinate encountered is positive and every coordinate divisible by a certifying prime is strictly larger than that prime. Put
\[
y_0=x_0+d_0.
\]

Lift each north edge to the two unit steps
\[
(x,y)\to(x,y+1)\to(x,y+2),
\]
and each east edge to
\[
(x,y)\to(x+1,y)\to(x+2,y).
\]

At every odd-odd waypoint, the state condition supplies an odd prime \(p\mid T\) dividing one coordinate. That coordinate is larger than \(p\), hence composite.

At an intermediate point, one coordinate is even and at least \(4\), hence composite.

For a north edge, the three differences between the two coordinates are \(d,d+1,d+2\). The state and edge conditions assert that all their prime divisors divide \(T\) and that the appropriate coordinate residues are coprime to them. Lemma 4 therefore proves visibility, both in the first lifted cycle and after any diagonal translation by \(mT\). The east case is identical, using \(d,d-1,d-2\).

After one traversal of the cycle, both coordinates have increased by
\[
2q=mT.
\]
Thus the same finite path can be repeated after translation by \((mT,mT)\).

Every unit step is east or north, so the resulting infinite path is simple: the sum of the coordinates strictly increases at every step. It is therefore a monotone admissible ray. ∎

The theorem is useful because a positive answer can now be certified by one finite directed cycle. It is only a sufficient criterion, not an equivalence: it restricts the ray to a periodic modular form and requires compositeness to be certified by fixed divisors of \(T\).

---

### 5. The first natural finite automaton fails

I checked the smallest useful composite-certifying modulus in a narrow positive strip.

Take
\[
T=30,\qquad D=\{2,4,6,8,10\}.
\]
Because all relevant coordinates are odd, reducing \(r\) modulo \(15\) is equivalent to retaining an odd residue modulo \(30\).

The state residues are:

\[
\begin{array}{c|c}
d & \text{admissible residues }r\pmod {15}\\ \hline
2 & (\mathbb Z/15\mathbb Z)\setminus\{2,11,14\}\\
4 & (\mathbb Z/15\mathbb Z)\setminus\{4,7,13\}\\
6 & \{4,5,10,14\}\\
8 & (\mathbb Z/15\mathbb Z)\setminus\{8,11,14\}\\
10& \{2,3,6,8,9,11,12,14\}.
\end{array}
\]

Applying the midpoint coprimality conditions gives the following possible edge sources:

\[
\begin{array}{c|c}
\text{edge} & \text{source residues }r\pmod {15}\\ \hline
2\to4\ \text{(north)} & \{1,5,8,10\}\\
4\to2\ \text{(east)} & \{1,3,6,10\}\\
4\to6\ \text{(north)} & \{14\}\\
6\to4\ \text{(east)} & \{10\}\\
8\to10\ \text{(north)}& \{2\}\\
10\to8\ \text{(east)}& \{3\}.
\end{array}
\]

There are no edges between levels \(6\) and \(8\), because the intermediate difference would be \(7\notin\mathcal S_{30}\).

These data contain no directed cycle:

- A transition \(4\to6\) enters level \(6\) with residue \(14\), but a transition \(6\to4\) requires residue \(10\).
- A transition \(8\to10\) enters level \(10\) with residue \(2\), but a transition \(10\to8\) requires residue \(3\).
- Any cycle confined to levels \(2,4\) must contain a north edge \(2\to4\) followed eventually by the only possible return \(4\to2\) at the same residue. The source residue must therefore lie in
  \[
  \{1,5,8,10\}\cap\{1,3,6,10\}=\{1,10\}.
  \]
  The east move then changes the low-level residue to \(3\) or \(12\), neither of which can start a north edge \(2\to4\).

Therefore \(Q(30,\{2,4,6,8,10\})\) has no directed cycle.

This failure is limited to this modulus and strip. It does not rule out \(T=210,2310,\ldots\), larger difference sets, negative differences, or nonperiodic rooted branching.

## Self-Audit

1. **The periodic automaton is only a sufficient ansatz.**  
   Failure to find a cycle does not imply that \(H\) has no ray. The theorem itself is rigorous because every visibility and compositeness condition is preserved by a fixed diagonal translation, but the imposed periodicity and fixed-divisor certificates are strong restrictions.

2. **The coprimality step in the CRT wall construction is delicate.**  
   After fixing \(X\), I choose \(Y=b+lM\) to avoid every prime divisor of \(X\). This works because there are finitely many such primes; primes dividing \(M\) are automatically avoided, and every other prime forbids exactly one residue class for \(l\). Thus the final CRT application is valid.

3. **The modulus-\(30\) calculation is narrow and vulnerable to transcription errors.**  
   It covers only \(D=\{2,4,6,8,10\}\). The residue sets and transition sets follow directly from divisibility by \(3,5\) and the midpoint formulas, and the code below independently regenerates them.

## Computations To Verify

```python
from math import gcd
from sympy import isprime, factorint, nextprime
from sympy.ntheory.modular import crt
import networkx as nx

def allowed(x, y):
    return (
        x >= 2 and y >= 2
        and gcd(x, y) == 1
        and not (isprime(x) and isprime(y))
    )

# 1. Verify the explicit isolated vertex.
v = (1581, 35)
assert allowed(*v)
for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
    assert not allowed(v[0] + dx, v[1] + dy)

def prime_factors(n):
    return set(factorint(abs(n)).keys())

def smooth_over_T(n, T):
    return n != 0 and prime_factors(n) <= prime_factors(T)

def certified_state(r, d, T):
    if d == 0 or d % 2:
        return False
    if not smooth_over_T(d, T):
        return False
    if gcd(r, abs(d)) != 1:
        return False
    return any(
        p != 2 and (r % p == 0 or (r + d) % p == 0)
        for p in prime_factors(T)
    )

def build_Q(T, D):
    D = set(D)
    states = {
        (r, d)
        for r in range(T) if r % 2 == 1
        for d in D
        if certified_state(r, d, T)
    }

    G = nx.DiGraph()
    G.add_nodes_from(states)

    for r, d in states:
        # North: (x,y) -> (x,y+2)
        target = (r, d + 2)
        if (
            target in states
            and smooth_over_T(d + 1, T)
            and gcd(r, abs(d + 1)) == 1
        ):
            G.add_edge((r, d), target, move="N")

        # East: (x,y) -> (x+2,y)
        target = ((r + 2) % T, d - 2)
        if (
            target in states
            and smooth_over_T(d - 1, T)
            and gcd(r + 1, abs(d - 1)) == 1
        ):
            G.add_edge((r, d), target, move="E")

    return G

# 2. Reproduce the modulus-30 narrow-strip check.
G30 = build_Q(30, [2, 4, 6, 8, 10])
assert nx.is_directed_acyclic_graph(G30)

# Print the source residues modulo 15 for each transition type.
for d1, d2, move in [
    (2,4,"N"), (4,2,"E"), (4,6,"N"),
    (6,4,"E"), (8,10,"N"), (10,8,"E")
]:
    src = sorted({
        r % 15
        for (r,d), (r2,e), data in G30.edges(data=True)
        if d == d1 and e == d2 and data["move"] == move
    })
    print((d1, d2, move), src)

# 3. Search larger periodic quotients.
def search(T, Dmax, include_negative=False):
    if include_negative:
        D = [d for d in range(-Dmax, Dmax + 1)
             if d != 0 and d % 2 == 0]
    else:
        D = list(range(2, Dmax + 1, 2))

    G = build_Q(T, D)
    for component in nx.strongly_connected_components(G):
        H = G.subgraph(component).copy()
        if len(component) > 1 or any(H.has_edge(v, v) for v in component):
            cycle = nx.find_cycle(H)
            return G, cycle
    return G, None

for T, Dmax in [(210, 100), (2310, 300), (30030, 500)]:
    G, cycle = search(T, Dmax, include_negative=False)
    print(T, len(G), G.number_of_edges(), cycle)

# Any returned cycle is a finite certificate for a monotone ray.
def verify_cycle(T, G, cycle):
    # networkx.find_cycle returns a list of directed edges.
    assert cycle
    e_count = 0
    n_count = 0

    for u, v in cycle:
        assert G.has_edge(u, v)
        move = G[u][v]["move"]
        if move == "E":
            e_count += 1
            assert v == ((u[0] + 2) % T, u[1] - 2)
        else:
            n_count += 1
            assert v == (u[0], u[1] + 2)

    assert e_count == n_count
    assert (2 * e_count) % T == 0
    return 2 * e_count  # diagonal translation length

# 4. Construct and verify CRT walls.
def construct_wall(R, B=100):
    offsets = [
        (i, j)
        for i in range(-R, R + 1)
        for j in range(-R, R + 1)
        if max(abs(i), abs(j)) == R
    ]

    p = nextprime(2 * R)
    ps = []
    for _ in offsets:
        ps.append(p)
        p = nextprime(p)

    q = p
    mods = ps + [q]
    xres = [(-i) % p for (i,j), p in zip(offsets, ps)] + [0]
    yres = [(-j) % p for (i,j), p in zip(offsets, ps)] + [1]

    a, M = map(int, crt(mods, xres))
    b, M2 = map(int, crt(mods, yres))
    assert M == M2

    k = max(1, (B + R + 3 - a + M - 1) // M)
    X = a + k * M
    if X <= q:
        X += M

    external = [ell for ell in factorint(X) if M % ell != 0]
    if external:
        residues = []
        for ell in external:
            bad = (-b * pow(M, -1, ell)) % ell
            residues.append(0 if bad != 0 else 1)
        l0, L = map(int, crt(external, residues))
    else:
        l0, L = 0, 1

    t = max(0, (B + R + 3 - (b + l0*M) + L*M - 1) // (L*M))
    l = l0 + t * L
    Y = b + l * M

    assert X > B and Y > B
    assert allowed(X, Y)

    for (i,j), p in zip(offsets, ps):
        assert (X + i) % p == 0
        assert (Y + j) % p == 0
        assert gcd(X + i, Y + j) > 1

    return X, Y

for R in range(1, 8):
    X, Y = construct_wall(R)
    print(R, X, Y)
```

The most important computation is the search for a directed cycle in \(Q(T,D)\). Any cycle found should be printed explicitly as a list of \((r,d)\)-states and independently checked by `verify_cycle`; Theorem 5 then converts it into a complete finite proof of a ray.

## Route Diagnosis

### Proved ledger

- \(H\) has a ray exactly when the coarse odd-odd graph \(K\) has a ray.
- The north/east coarse extension conditions are explicit gcd conditions involving \(d,d\pm1,d\pm2\).
- Admissible isolated vertices exist; \((1581,35)\) is explicit.
- CRT constructs invisible square barriers of arbitrary prescribed radius around specially chosen admissible roots.
- Arbitrarily long admissible finite paths with varying roots are elementary.
- A directed cycle in the finite graph \(Q(T,D)\) gives a periodic monotone admissible ray.
- The natural modulus-\(30\), positive strip \(D=\{2,4,6,8,10\}\) contains no such cycle.

### Plausible but unproved

- For a larger primorial modulus such as \(210,2310\), and a sufficiently wide difference set, \(Q(T,D)\) may contain a directed cycle.
- A nonperiodic version might maintain a family of residue states and avoid sink configurations even when every individual state lacks a uniform extension.
- Sink strongly connected components in larger automata may expose a usable invariant or, conversely, a systematic obstruction to this periodic ansatz.

### Dead ends

- “Every sufficiently large admissible vertex extends” is false, even at arbitrarily large coordinates.
- A positive average branching factor is insufficient; CRT walls can correlate all branches within a specially placed finite region.
- Certification using only divisibility by \(3\) is too rigid, and the first combined \(3,5\) automaton in a narrow strip dies.
- Arbitrarily long paths with varying roots do not address the rooted compactness requirement.

### Precise block

Route 4 still lacks a rooted branching theorem. Proving merely that many frontier states are arithmetically good does not ensure that one compatible branch survives every future bottleneck, and the CRT constructions rule out any theorem based only on coordinate size or bounded local data.

The best immediate next step is an exhaustive SCC search in \(Q(T,D)\) for \(T=210,2310,\ldots\), followed by extraction of an explicit cycle if one exists. Such a cycle would settle the problem positively by a finite, independently checkable certificate. If these searches systematically fail, the sink configurations should be analyzed for a modular invariant; without either a cycle or a new rooted invariant, Route 4 remains blocked.