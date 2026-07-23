# Orchestrator audit notes — #289 (interval unit fractions)

Machine-verified facts (exact rational arithmetic):

1. **Telescoping dimer reservoir (r4 Lemma 1) — VERIFIED.**
   With Q_0 = 1, Q_{j+1} = 2Q_j(2Q_j+1), the dimer [2Q_j, 2Q_j+1] has weight
   exactly 1/Q_j − 1/Q_{j+1}; hence the m dimers [2,3], [12,13], [312,313], …
   sum to exactly 1 − 1/Q_m. Verified to depth 5.

2. **Four-to-five identity (r1 eq. (4)) — VERIFIED.**
   w(4,10)+w(17,18)+w(34,35)+w(82,83)+w(85,87)
   = w(2,3)+w(6,8)+w(82,84)+w(86,87), all blocks length ≥ 2, non-adjacent.

3. **No fixed-shape compensation (orchestrator).** Splitting a block [a,b] at j
   loses exactly 1/(j+1); compensating with a NEW dimer [x,x+1] requires
   (2j+2)²+1 to be a perfect square (never), and with a new trimer requires
   3x²+6x+2 | 2 (never). So "+1 block" padding cannot be done by local
   split-plus-small-block rewrites; count flexibility must come from global
   structure. This matches r2/r4's negative results and localizes the entire
   difficulty of #289 at: exact completions of the reservoir residual 1/Q_m
   with two (or all sufficiently large) consecutive block counts, OR a seed
   solution containing the right side of (2) plus remote equal-weight
   count-shifting families (r1 §4) made compatible.

State: round 2 in flight with all of the above folded into its brief.
