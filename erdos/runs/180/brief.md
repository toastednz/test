# Problem Brief: Erdős Problem #180

## 0. Executive status

Under the standard meaning of extremal number and non-induced subgraph containment, the statement as written is **false**. The database commentary itself contains a valid finite counterexample.

The smallest clean example is
\[
\mathcal F=\{P_3,\,2K_2\},
\]
where \(P_3=K_{1,2}\) is the two-edge path and \(2K_2\) is a matching of size two. For every \(n\ge 2\),
\[
\operatorname{ex}(n;\mathcal F)=1,
\]
whereas
\[
\operatorname{ex}(n;P_3)=\left\lfloor\frac n2\right\rfloor
\quad\text{and}\quad
\operatorname{ex}(n;2K_2)=n-1\qquad(n\ge4).
\]
Thus neither member \(G\in\mathcal F\) satisfies
\[
\operatorname{ex}(n;G)=O_{\mathcal F}(\operatorname{ex}(n;\mathcal F)).
\]

Consequently, the database status “OPEN” cannot be reconciled with the literal statement. Presumably, the intended open question is a repaired version excluding this bounded-extremal-number obstruction, but no precise repaired formulation is supplied.

---

# 1. Precise statement

## 1.1 Graph conventions

Unless explicitly stated otherwise:

- All graphs are finite, simple, and undirected.
- A graph \(H\) is a subgraph of a graph \(X\), written \(H\subseteq X\), if there is an injective map
  \[
  \varphi:V(H)\to V(X)
  \]
  such that
  \[
  uv\in E(H)\implies \varphi(u)\varphi(v)\in E(X).
  \]
  Nonedges of \(H\) need not map to nonedges of \(X\). Thus containment is **not induced containment**.
- Isolated vertices of \(H\) must be represented by distinct vertices of \(X\), but may map to vertices that have additional incident edges in \(X\).

Let \(\mathcal F\) be a finite, nonempty set of finite graphs. To avoid degenerate definitional issues, one normally assumes every \(H\in\mathcal F\) has at least one edge.

A graph \(X\) is **\(\mathcal F\)-free** if no \(H\in\mathcal F\) occurs as a subgraph of \(X\).

For \(n\in\mathbb N\), define
\[
\operatorname{ex}(n;\mathcal F)
=
\max\{e(X): |V(X)|=n,\ X\text{ is }\mathcal F\text{-free}\}.
\]
For a single graph \(G\),
\[
\operatorname{ex}(n;G):=\operatorname{ex}(n;\{G\}).
\]

Because every \(\mathcal F\)-free graph is \(G\)-free for each \(G\in\mathcal F\),
\[
\operatorname{ex}(n;\mathcal F)\le \operatorname{ex}(n;G)
\qquad\text{for every }G\in\mathcal F.
\]

## 1.2 Formal universal assertion

The question asks whether the following assertion is true:

> For every finite nonempty family \(\mathcal F\) of finite graphs, there exist a graph \(G\in\mathcal F\), a constant \(C_{\mathcal F}>0\), and an integer \(n_0\) such that
> \[
> \operatorname{ex}(n;G)\le
> C_{\mathcal F}\operatorname{ex}(n;\mathcal F)
> \]
> for every \(n\ge n_0\).

Equivalently, does every finite family \(\mathcal F\) contain a member \(G\) such that
\[
\operatorname{ex}(n;G)=\Theta_{\mathcal F}(\operatorname{ex}(n;\mathcal F))?
\]
The lower comparison is automatic.

The notation \(\ll_{\mathcal F}\) is normally asymptotic: the inequality is required for all sufficiently large \(n\), with a constant depending only on \(\mathcal F\), not on \(n\).

## 1.3 Degenerate alternatives

Several conventions must be kept separate:

1. **Empty family.** If \(\mathcal F=\varnothing\), there is no \(G\in\mathcal F\), so the existential conclusion is automatically false. The intended problem must therefore assume \(\mathcal F\ne\varnothing\).

2. **Edgeless forbidden graphs.** If \(H\) is edgeless, then every graph on at least \(v(H)\) vertices contains \(H\) as a non-induced subgraph. Depending on convention, the maximum defining \(\operatorname{ex}(n;H)\) is then over an empty class. Standard extremal graph theory generally excludes such forbidden graphs.

3. **A one-edge graph with isolated vertices.** If \(H\) consists of one edge and some isolated vertices, then for all sufficiently large \(n\),
   \[
   \operatorname{ex}(n;H)=0.
   \]
   Such a member trivially controls the family.

4. **Connected forbidden graphs.** The standard problem does not require members of \(\mathcal F\) to be connected. Indeed, the database’s matching counterexample explicitly confirms that disconnected forbidden graphs are allowed.

---

# 2. What counts as a solution

## 2.1 What a proof of the universal assertion would have to establish

A complete affirmative proof would have to show:

For every finite nonempty family \(\mathcal F\), there is one **fixed** member \(G\in\mathcal F\) and one constant \(C_{\mathcal F}\), both independent of \(n\), such that
\[
\operatorname{ex}(n;G)\le
C_{\mathcal F}\operatorname{ex}(n;\mathcal F)
\]
for all sufficiently large \(n\).

It would not be enough to choose \(G=G_n\) depending on \(n\).

However, no such proof can exist under the standard reading because the assertion has an explicit counterexample.

## 2.2 What a complete disproof must establish

Because the assertion is universal over finite families, a disproof requires one finite nonempty family \(\mathcal F\) such that for every \(G\in\mathcal F\),
\[
\sup_{n\ge n_0}
\frac{\operatorname{ex}(n;G)}
{\operatorname{ex}(n;\mathcal F)}
=\infty
\]
for every \(n_0\) for which the denominator is positive.

Equivalently, for every \(G\in\mathcal F\) and every constant \(C>0\), there must be arbitrarily large \(n\) satisfying
\[
\operatorname{ex}(n;G)>
C\operatorname{ex}(n;\mathcal F).
\]

An explicit counterexample must verify:

1. \(\mathcal F\) is finite and nonempty.
2. Every member is a finite graph.
3. There is a uniform upper bound, or another sufficiently strong estimate, on \(\operatorname{ex}(n;\mathcal F)\).
4. Each singleton extremal number \(\operatorname{ex}(n;G)\), \(G\in\mathcal F\), is asymptotically larger by an unbounded factor.

## 2.3 Complete disproof

Take
\[
\mathcal F=\{P_3,2K_2\}.
\]

### Joint extremal number

A graph is \(P_3\)-free if and only if it has maximum degree at most one. Indeed, two edges incident to the same vertex form a non-induced copy of \(P_3\). Hence every \(P_3\)-free graph is a matching together with isolated vertices.

If the graph is also \(2K_2\)-free, it can contain at most one edge. Therefore
\[
\operatorname{ex}(n;\{P_3,2K_2\})=1
\qquad(n\ge2).
\]

### Singleton \(P_3\)

A \(P_3\)-free graph has maximum degree at most one, so it is a matching. Thus
\[
\operatorname{ex}(n;P_3)=\left\lfloor\frac n2\right\rfloor.
\]

### Singleton \(2K_2\)

A \(2K_2\)-free graph has matching number at most one, so every two edges intersect. A pairwise-intersecting family of two-element subsets is either:

- contained in a star, giving at most \(n-1\) edges; or
- the three edges of a triangle.

Hence
\[
\operatorname{ex}(n;2K_2)=
\begin{cases}
0,&n=1,\\
1,&n=2,\\
3,&n=3,\\
n-1,&n\ge4.
\end{cases}
\]

Therefore, for \(n\ge4\),
\[
\frac{\operatorname{ex}(n;P_3)}
{\operatorname{ex}(n;\mathcal F)}
=
\left\lfloor\frac n2\right\rfloor\to\infty
\]
and
\[
\frac{\operatorname{ex}(n;2K_2)}
{\operatorname{ex}(n;\mathcal F)}
=n-1\to\infty.
\]

This is a complete disproof of the literal statement.

---

# 3. What does not count

The following would not resolve the stated problem:

1. **Reproving the trivial inequality**
   \[
   \operatorname{ex}(n;\mathcal F)\le\operatorname{ex}(n;G).
   \]
   The desired inequality is in the opposite direction up to a constant.

2. **Choosing a different \(G\in\mathcal F\) for each \(n\).**  
   One fixed member must work for all sufficiently large \(n\).

3. **Proving only an exponent comparison**, for example
   \[
   \operatorname{ex}(n;G)\le
   n^{o(1)}\operatorname{ex}(n;\mathcal F)
   \]
   or
   \[
   \operatorname{ex}(n;G)\le
   n^\varepsilon\operatorname{ex}(n;\mathcal F).
   \]
   The required loss is a constant depending only on \(\mathcal F\).

4. **Proving the result for nonbipartite families only.**  
   That case is already settled by Erdős–Stone–Simonovits.

5. **Proving it for connected forbidden graphs only.**  
   That is a different, potentially meaningful variant, but does not resolve the original statement.

6. **Proving it after excluding the star–matching example without precisely defining the exclusion.**  
   “All other families” is not a formal conjecture.

7. **Conditional results.**  
   A theorem conditional on a conjectural Turán exponent, supersaturation theorem, or algebraic construction does not resolve the unconditional question.

8. **Finite computational verification.**  
   Checking all families up to a bounded number of vertices cannot prove a universal asymptotic assertion.

9. **Using induced-subgraph containment.**  
   This changes the problem. For example, a triangle contains \(P_3\) as a non-induced subgraph but not as an induced subgraph.

---

# 4. Known results and context

## 4.1 Families with no bipartite member

Suppose every \(H\in\mathcal F\) is nonbipartite, and let
\[
r=\min_{H\in\mathcal F}\chi(H).
\]
Then \(r\ge3\). Choose \(H_*\in\mathcal F\) with \(\chi(H_*)=r\).

The Turán graph \(T_{r-1}(n)\) is \(H\)-free for every \(H\in\mathcal F\), so
\[
\operatorname{ex}(n;\mathcal F)\ge e(T_{r-1}(n)).
\]
On the other hand,
\[
\operatorname{ex}(n;\mathcal F)\le\operatorname{ex}(n;H_*).
\]
By the Erdős–Stone–Simonovits theorem,
\[
\operatorname{ex}(n;H_*)
=
\left(1-\frac1{r-1}+o(1)\right)\binom n2
=
\left(\frac{r-2}{r-1}+o(1)\right)\binom n2.
\]
Thus
\[
\operatorname{ex}(n;\mathcal F)
=
\operatorname{ex}(n;H_*)
+o(n^2)
=
\left(\frac{r-2}{r-1}+o(1)\right)\binom n2.
\]
Hence \(H_*\) controls the family up to a constant.

The database’s phrase “\(r\ge2\)” should read \(r\ge3\) in the no-bipartite-member case. For \(r=2\), the Erdős–Stone leading coefficient is zero and gives no constant-factor comparison.

## 4.2 Infinite families

Finiteness of \(\mathcal F\) was intended to be essential.

Let \(\mathcal F\) be the family of all cycles. Then an \(\mathcal F\)-free graph is a forest, so
\[
\operatorname{ex}(n;\mathcal F)=n-1.
\]
For every fixed cycle \(C_\ell\),
\[
\frac{\operatorname{ex}(n;C_\ell)}n\to\infty.
\]
For odd \(\ell\), this follows from complete bipartite graphs, which are \(C_\ell\)-free and have \(\Theta(n^2)\) edges. For even \(\ell\), standard high-girth constructions or probabilistic constructions give superlinear lower bounds; Bondy–Simonovits gives the classical corresponding upper-bound framework.

Thus no fixed cycle controls the infinite family.

## 4.3 General star–matching counterexample

Let
\[
H_1=K_{1,s},\qquad H_2=M_t=tK_2,
\]
where \(s,t\ge2\).

If a graph is \(K_{1,s}\)-free, then
\[
\Delta(X)\le s-1.
\]
If it is \(M_t\)-free, then
\[
\nu(X)\le t-1,
\]
where \(\nu(X)\) is the matching number.

Let \(M\) be a maximal matching. Its endpoint set \(S\) is a vertex cover, and
\[
|S|\le2(t-1).
\]
Therefore
\[
e(X)\le\sum_{v\in S}\deg(v)
\le2(t-1)(s-1).
\]
Thus
\[
\operatorname{ex}(n;\{K_{1,s},M_t\})=O_{s,t}(1).
\]

Individually,
\[
\operatorname{ex}(n;K_{1,s})=\Theta_s(n)
\]
by the degree bound and bounded-degree constructions, while the Erdős–Gallai matching theorem gives
\[
\operatorname{ex}(n;M_t)=\Theta_t(n).
\]
More precisely, for sufficiently large \(n\),
\[
\operatorname{ex}(n;M_t)
=
\max\left\{
\binom{2t-1}{2},
\binom{t-1}{2}+(t-1)(n-t+1)
\right\}.
\]

Hence this entire class of finite families disproves the literal assertion.

## 4.4 Elementary classification of the bounded obstruction

For a graph \(H\), let \(H^+\) be the graph obtained by deleting all isolated vertices.

Assume every member of \(\mathcal F\) has at least one edge. Then
\[
\operatorname{ex}(n;\mathcal F)=O_{\mathcal F}(1)
\]
if and only if:

1. some \(H_s\in\mathcal F\) has all edges incident with one common vertex, i.e. \(H_s^+\subseteq K_{1,a}\) for some \(a\); and
2. some \(H_m\in\mathcal F\) has maximum degree at most one, i.e. \(H_m^+\) is a matching.

### Necessity

If \(\operatorname{ex}(n;\mathcal F)\le C\), then a sufficiently large star, having more than \(C\) edges, cannot be \(\mathcal F\)-free. Hence some member of \(\mathcal F\) embeds into a star, forcing its edge-support to be star-like.

Likewise, a sufficiently large matching cannot be \(\mathcal F\)-free, so some member embeds into a matching.

### Sufficiency

For all sufficiently large \(n\), avoiding \(H_s\) bounds the maximum degree, while avoiding \(H_m\) bounds the matching number. The endpoint set of a maximal matching is then a bounded vertex cover, giving a uniform bound on the number of edges.

Moreover, every fixed graph \(H\) with at least two edges satisfies
\[
\operatorname{ex}(n;H)=\Omega_H(n):
\]

- If \(H\) has two adjacent edges, an \(n\)-vertex matching avoids \(H\).
- If all edges of \(H\) are pairwise disjoint and \(e(H)\ge2\), an \(n\)-vertex star avoids \(H\).

Therefore, every finite family with bounded joint extremal number and with at least two edges in every member is automatically a counterexample to the literal assertion.

This precisely explains the folklore obstruction at the bounded level. It does **not** prove that no unbounded counterexample exists.

## 4.5 Sparse bipartite context

Once bipartite forbidden graphs are present, Erdős–Stone–Simonovits no longer supplies the required comparison. Relevant general tools include:

- the Kővári–Sós–Turán theorem for complete bipartite graphs;
- the Bondy–Simonovits theorem for even cycles;
- the Erdős–Gallai theorem for matchings and paths;
- tree embedding bounds, including the Erdős–Sós theorem;
- supersaturation and hypergraph-container methods;
- random and algebraic constructions for sparse bipartite Turán problems.

Even singleton bipartite Turán numbers are unknown in many important cases. Thus any repaired unbounded version would lie in a genuinely difficult part of extremal graph theory.

The supplied reference “[575]” is not described in enough detail to extract a further theorem safely.

---

# 5. Traps and edge cases

1. **The literal problem is already disproved.**  
   Do not spend effort attempting to prove the universal statement without first changing it.

2. **Subgraph is not induced subgraph.**  
   A triangle contains \(P_3\), because any two adjacent triangle edges form a copy.

3. **A matching is disconnected.**  
   Any variant requiring all forbidden graphs to be connected excludes the folklore example and is a different problem.

4. **The empty family.**  
   Without the nonempty-family convention, the statement is trivially false because no \(G\in\mathcal F\) exists.

5. **Edgeless forbidden graphs.**  
   These can make the admissible class empty. They should be excluded or handled by an explicit convention.

6. **One-edge forbidden graphs.**  
   If \(K_2\in\mathcal F\), then
   \[
   \operatorname{ex}(n;\mathcal F)=\operatorname{ex}(n;K_2)=0,
   \]
   so the conclusion holds trivially.

7. **Isolated vertices in a forbidden graph.**  
   They affect small \(n\), though for sufficiently large \(n\) they do not alter the edge-structure obstruction. They must not simply be discarded in exact finite-\(n\) claims.

8. **Pairwise-intersecting edge sets have a triangle exception.**  
   A graph with matching number one need not be a star: it may be a triangle. This affects the exact value of \(\operatorname{ex}(3;2K_2)\).

9. **The Erdős–Stone argument requires positive density.**  
   Substituting \(r=2\) into
   \[
   \left(1-\frac1{r-1}\right)\binom n2
   \]
   yields zero and gives no multiplicative comparison.

10. **A constant-factor result is stronger than exponent equality.**  
    Even proving
    \[
    \log_n\operatorname{ex}(n;G)
    -
    \log_n\operatorname{ex}(n;\mathcal F)\to0
    \]
    would not suffice.

11. **Finite minima may switch with \(n\).**  
    Even though
    \[
    \operatorname{ex}(n;\mathcal F)\le
    \min_{H\in\mathcal F}\operatorname{ex}(n;H),
    \]
    one cannot automatically choose a single minimizer independent of \(n\), and the joint extremal number may be much smaller than this minimum.

12. **Deleting copies can destroy too many edges.**  
    A naive argument that starts with an extremal \(G\)-free graph and deletes one edge from each copy of the remaining forbidden graphs may lose almost all edges.

---

# 6. Verification hooks

## 6.1 Exhaustive check of the minimal counterexample

For \(n\le7\), enumerate all labeled graphs on vertex set \([n]\) by a bit mask of length \(\binom n2\).

For each graph \(X\), compute:

- \(e(X)\);
- \(\Delta(X)\);
- whether \(X\) has two disjoint edges.

Then verify:

- \(X\) is \(P_3\)-free iff \(\Delta(X)\le1\);
- \(X\) is \(2K_2\)-free iff no two edges are disjoint;
- \(X\) is both-free iff \(e(X)\le1\).

Expected outputs:
\[
\operatorname{ex}(n;\{P_3,2K_2\})=
0,1,1,1,1,\dots
\]
for \(n=1,2,3,4,\dots\),
\[
\operatorname{ex}(n;P_3)=\lfloor n/2\rfloor,
\]
and
\[
\operatorname{ex}(n;2K_2)=0,1,3,3,4,5,\dots.
\]

## 6.2 Integer-programming formulation

Introduce binary variables \(x_{ij}\) for \(1\le i<j\le n\), with objective
\[
\max \sum_{i<j}x_{ij}.
\]

To forbid a graph \(H\), for every injective map
\[
\varphi:V(H)\to[n],
\]
add the constraint
\[
\sum_{uv\in E(H)}
x_{\varphi(u)\varphi(v)}
\le e(H)-1.
\]

For \(P_3\), these reduce to
\[
x_{uv}+x_{uw}\le1
\]
for every three distinct \(u,v,w\).

For \(2K_2\), they reduce to
\[
x_{uv}+x_{wz}\le1
\]
for every four distinct \(u,v,w,z\).

This ILP can verify the exact extremal values for moderate \(n\).

## 6.3 General star–matching family

For fixed \(s,t\):

- impose degree constraints
  \[
  \sum_{u\ne v}x_{uv}\le s-1
  \]
  for every \(v\);
- impose matching constraints for every set of \(t\) pairwise-disjoint potential edges:
  \[
  \sum_{e\in M}x_e\le t-1.
  \]

Compare the optimum against the theoretical bound
\[
2(t-1)(s-1).
\]
The exact optimum may be smaller, but it must stabilize at a bounded value as \(n\) grows.

## 6.4 Testing the bounded-obstruction classification

For each forbidden graph \(H\), delete isolated vertices and compute:

- whether all edges have a common endpoint;
- whether \(\Delta(H)\le1\);
- whether \(e(H)=1\).

A family is predicted to have bounded joint extremal number exactly when it contains both a star-supported member and a matching-supported member. This can be tested on all small forbidden families.

## 6.5 Search for an unbounded counterexample

Generate connected and disconnected forbidden graphs on at most \(h\) vertices, preferably using an unlabeled graph generator such as `nauty`.

For each small family \(\mathcal F\), compute
\[
\operatorname{ex}(n;\mathcal F)
\quad\text{and}\quad
\operatorname{ex}(n;H),\ H\in\mathcal F,
\]
for \(n\le8\) or \(9\), and inspect
\[
R_{\mathcal F}(n)
=
\frac{\min_{H\in\mathcal F}\operatorname{ex}(n;H)}
{\operatorname{ex}(n;\mathcal F)}.
\]

Exclude bounded-obstruction families using the structural test above. Rapid growth of \(R_{\mathcal F}(n)\) may suggest a candidate, but finite data alone is not evidence of an asymptotic separation.

---

# 7. Attack routes

Because the literal assertion is already false, Route 1 completes the stated problem. Routes 2–6 concern the likely intended repaired question, for example:

> If \(\operatorname{ex}(n;\mathcal F)\) is unbounded, must some \(G\in\mathcal F\) satisfy  
> \(\operatorname{ex}(n;G)=O_{\mathcal F}(\operatorname{ex}(n;\mathcal F))\)?

That formulation is natural but is not explicitly given by the database.

## Route 1: Minimal explicit disproof

### Key lemma

A graph is \(P_3\)-free iff it has maximum degree at most one, and a graph that is both \(P_3\)-free and \(2K_2\)-free has at most one edge.

### Why it works

It produces a finite two-member family with constant joint extremal number and linear singleton extremal numbers.

### Most likely failure point

Only a convention change:

- induced rather than non-induced containment;
- a requirement that forbidden graphs be connected;
- an unstated exclusion of bounded \(\operatorname{ex}(n;\mathcal F)\).

None of these is part of the standard statement, and the database commentary itself endorses the example.

### Quick test

Exhaustively enumerate graphs for \(n\le6\) and recover
\[
\operatorname{ex}(n;\{P_3,2K_2\})=1.
\]

**Status:** This route succeeds and fully disproves the literal statement.

---

## Route 2: Classify and remove all bounded obstructions

### Key lemma needed

Prove formally, including isolated vertices, that
\[
\operatorname{ex}(n;\mathcal F)=O(1)
\]
if and only if \(\mathcal F\) contains:

- a member whose nonisolated edge-support is contained in a star; and
- a member whose nonisolated edge-support is a matching.

### Why it might work

This identifies exactly the mechanism behind all bounded joint extremal numbers. It yields a precise replacement for the vague phrase “all other \(\mathcal F\)”:

- either exclude all families with bounded joint extremal number; or
- explicitly exclude star-supported/matching-supported pairs.

This is the first necessary reduction before studying a repaired conjecture.

### Most likely failure point

The classification does not address families for which
\[
\operatorname{ex}(n;\mathcal F)\to\infty
\]
but grows much more slowly than every singleton extremal number. Isolated vertices and one-edge members must also be handled separately.

### Quick test

For all graph families with members on at most five vertices:

1. identify star-supported and matching-supported members;
2. compute \(\operatorname{ex}(n;\mathcal F)\) for small \(n\);
3. verify stabilization precisely in the predicted cases.

---

## Route 3: Component-packing reduction

### Core mechanism

Analyze disconnected forbidden graphs through vertex-disjoint packing and transversal arguments.

### Key lemma needed

A useful lemma would say that if a disconnected graph
\[
H=H_1\sqcup\cdots\sqcup H_k
\]
is absent, then either:

- one component type \(H_i\) is globally sparse in a controlled sense; or
- all copies of some component can be hit by a bounded vertex set.

One would then seek an induction reducing a family of disconnected forbidden graphs to connected components plus an \(O(n)\) error term.

### Why it might work

The known counterexample arises from incompatible packing constraints:

- forbidding a star bounds degree;
- forbidding a matching bounds the number of disjoint edges.

A systematic packing theory may show that this is the only way disconnected members can create an unbounded multiplicative gap.

### Most likely failure point

A bounded vertex transversal can still meet a linear or superlinear number of edges. In the linear regime, an \(O(n)\) error is not negligible. Copies of different component types may concentrate around different small vertex sets.

### Quick test

Work out exact or asymptotic extremal numbers for families built from:

- paths plus matchings;
- stars plus disjoint unions of paths;
- \(H_1\sqcup H_2\) where \(H_1,H_2\) are small connected bipartite graphs.

Check whether every unbounded example is controlled by one connected component or one original family member.

---

## Route 4: Copy-hypergraph deletion and edge retention

### Core mechanism

Start with an extremal \(G\)-free graph \(X\), for a candidate \(G\in\mathcal F\). Encode copies of every other \(H\in\mathcal F\setminus\{G\}\) as hyperedges in a hypergraph whose vertices are the edges of \(X\).

### Key lemma needed

For some \(G\in\mathcal F\), every sufficiently large extremal or near-extremal \(G\)-free graph \(X\) should contain an \(\mathcal F\)-free subgraph \(Y\subseteq X\) satisfying
\[
e(Y)\ge c_{\mathcal F}e(X).
\]

Equivalently, the copy hypergraph should have an independent set containing a constant fraction of its vertices.

### Why it might work

If such a retention lemma holds, then
\[
\operatorname{ex}(n;\mathcal F)
\ge c_{\mathcal F}\operatorname{ex}(n;G),
\]
which is exactly the required comparison.

Possible tools include:

- hypergraph containers;
- random sparsification;
- bounded-codegree independent-set theorems;
- balanced supersaturation.

### Most likely failure point

The copy hypergraph may be extremely dense with highly overlapping hyperedges, forcing every independent set to contain only \(o(e(X))\) edges. This is exactly what happens in the star–matching example: a large matching is \(P_3\)-free, but avoiding \(2K_2\) leaves only one edge.

Unbounded joint extremal number does not automatically prevent the same phenomenon at a slower scale.

### Quick test

For known extremal constructions \(X_n\) for small forbidden graphs, solve the secondary optimization problem:

> What is the largest \(\mathcal F\)-free subgraph of \(X_n\)?

Track the retained edge ratio as \(n\) increases.

---

## Route 5: Sparse Turán exponents and simultaneous constructions

### Core mechanism

Restrict first to structured classes of bipartite graphs for which singleton Turán numbers and constructions are reasonably understood: cycles, theta graphs, complete bipartite graphs, subdivisions, or bounded-radius graphs.

### Key lemma needed

For a finite family in such a class, construct a single graph avoiding every member and having
\[
\Omega_{\mathcal F}\!\left(
\min_{H\in\mathcal F}\operatorname{ex}(n;H)
\right)
\]
edges.

Potential mechanisms include:

- random high-girth constructions;
- algebraic incidence graphs;
- norm graphs;
- generalized polygons;
- random deletion coupled with balanced supersaturation.

### Why it might work

For many familiar finite cycle families, avoiding all short cycles appears to achieve the scale associated with the “hardest” individual cycle. Similar common constructions may simultaneously avoid several forbidden configurations.

A theorem of this form for broad structured classes would be meaningful progress toward an unbounded repaired conjecture.

### Most likely failure point

Singleton extremal numbers themselves may be unknown even up to a constant or exponent. Different forbidden graphs can require incompatible algebraic constructions. Equal Turán exponents do not imply constant-factor comparability, and logarithmic gaps would already defeat the desired conclusion.

### Quick test

Begin with families such as
\[
\{C_4,C_6\},\quad
\{C_6,C_8\},\quad
\{C_4,K_{2,3}\},
\]
and compare known constructions and upper bounds. Determine whether one member already gives the strongest known upper bound at the scale of the best simultaneous construction.

---

## Route 6: Search for an unbounded counterexample

### Core mechanism

Seek a finite family \(\mathcal F\) such that
\[
\operatorname{ex}(n;\mathcal F)\to\infty
\]
but
\[
\operatorname{ex}(n;\mathcal F)
=
o\!\left(\operatorname{ex}(n;H)\right)
\qquad\text{for every }H\in\mathcal F.
\]

This would disprove the most natural repaired conjecture.

### Key lemma needed

For a candidate family, one needs both:

1. a joint upper bound
   \[
   \operatorname{ex}(n;\mathcal F)\le f(n);
   \]
2. for each \(H\in\mathcal F\), an individual construction with
   \[
   \operatorname{ex}(n;H)\ge g_H(n),
   \qquad \frac{g_H(n)}{f(n)}\to\infty.
   \]

Promising candidates would combine forbidden graphs whose extremal constructions have incompatible local geometries—degree concentration, incidence geometry, high girth, large codegrees, or component packing.

### Why it might work

The star–matching example demonstrates that finite forbidden conditions can interact much more strongly than either does alone. There is no a priori reason that all such interactions must collapse to bounded extremal number.

### Most likely failure point

Random high-girth graphs simultaneously avoid every fixed finite collection of short cyclic configurations while retaining polynomially many edges. More generally, one family member may always end up controlling the same density scale, even if known constructions look different.

Small-\(n\) numerical gaps may also be caused entirely by finite-size effects.

### Quick test

Enumerate all two- and three-member families of small bipartite graphs, excluding the bounded-obstruction class. Compute exact extremal numbers for \(n\le8\) or \(9\), rank families by the growth of
\[
R_{\mathcal F}(n)
=
\frac{\min_{H\in\mathcal F}\operatorname{ex}(n;H)}
{\operatorname{ex}(n;\mathcal F)},
\]
and then seek structural proofs only for candidates with a persistent, interpretable gap.

---

# 8. Verdict on difficulty

## Literal statement

**Resolved: false, by an elementary counterexample.**

The family
\[
\{P_3,2K_2\}
\]
is a complete and easily verifiable disproof. The “OPEN” database label is inconsistent with the displayed statement and commentary unless an unstated revised conjecture is intended.

## Likely intended revised problem

A natural repaired question is:

> If \(\mathcal F\) is finite and \(\operatorname{ex}(n;\mathcal F)\) is unbounded, must some \(G\in\mathcal F\) satisfy
> \[
> \operatorname{ex}(n;G)=O_{\mathcal F}(\operatorname{ex}(n;\mathcal F))?
> \]

Another possible repair is to restrict to connected forbidden graphs, but that is different and may not be equivalent.

These repaired versions appear genuinely difficult. They sit in sparse extremal graph theory, where even singleton bipartite Turán problems are often unresolved. No equivalence to a specific famous conjecture follows from the supplied material, but any broad positive theorem would require substantial new structural control over simultaneous forbidden-subgraph conditions.

The correct immediate research action is therefore:

1. record the literal problem as **disproved**;
2. determine from the original Erdős–Simonovits source or reference [575] the exact intended revised formulation;
3. only then investigate the unbounded or connected-family variant.