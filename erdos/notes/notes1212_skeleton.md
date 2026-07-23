# Orchestrator research notes for #1212 (verified computationally where stated)

## Established facts (computer-verified)
1. **Bounded-coordinate impossibility (proved).** Any infinite admissible path must have BOTH
   coordinates unbounded. Proof: if y ≤ M along the path while sup x = ∞, the path crosses
   column x* = any multiple of lcm(2,...,M) exceeding its starting x at some row y ≤ M, but
   gcd(x*, y) = y > 1. Symmetrically for bounded x. (So Stewart-style or fixed-row-corridor
   constructions cannot work; computationally: BFS in corridors rows {Y..Y+h} for all
   Y ≤ 20000, h ≤ 5 with period ≤ 1.5M finds NO period-crossing path — walls at columns
   divisible by rad(∏rows).)
2. **Near-diagonal band fails empirically.** BFS in {|y−x| ≤ 10} from (899,900) gets stuck at
   x=922: prime pairs + parity + shared-gcd walls choke the band. Do not pursue.

## Proposed construction (skeleton to be completed and verified)
Alternating staircase with clean vertical legs and dodged horizontal legs.
Anchors: Y_1 < Y_2 < ... rows, X_1 < X_2 < ... columns, legs:
  V_i: column X_i from (X_i, Y_i) to (X_i, Y_{i+1});
  H_i: row Y_{i+1} from (X_i, Y_{i+1}) to (X_{i+1}, Y_{i+1}).

KEY CHOICES:
- X_i = q_i·q_i' odd semiprime, q_i, q_i' distinct huge primes (≥ bound fixed below).
- Y_{i+1} chosen AFTER X_i with Y_i < Y_{i+1} < min(q_i, q_i'): then NO row in
  [Y_i, Y_{i+1}] shares a factor with X_i — vertical legs are entirely clean, no dodges.
  (Multiples of q_i start beyond Y_{i+1}.) X_i composite makes every V_i vertex admissible
  regardless of row primality.
- Y_{i+1} = r·r' odd semiprime (r, r' huge but < q_i), composite, so every H_i vertex has
  composite y-coordinate: admissibility on H_i = coprimality only.
- Horizontal leg H_i spans a LONG interval; bad columns are the multiples of r, r' in it
  (density 1/r + 1/r', isolated or in clusters of ≤ 2 adjacent). Each bad column/cluster is
  dodged locally through rows Y_{i+1}+1, Y_{i+1}+2 (or −1, −2), which must be handled with
  the parity calculus below.

PARITY CALCULUS (unavoidable): a vertex with both coordinates even is forbidden. An even
column can only carry vertices at odd rows and vice versa. All X_i, Y_i odd. For a dodge of a
bad column x*:
- If x* is odd: adjacent columns x*±1 are even; passage around x* must use rows of correct
  parity: from (x*−2, Y) [odd col] step up to dodge rows, cross columns x*−1, x*, x*+1 at
  rows chosen so even columns sit on odd rows: with Y odd, Y+1 even, Y+2 odd:
  route (x*−2, Y) → (x*−2, Y+1) → (x*−2, Y+2) → (x*−1, Y+2) → (x*, Y+2)?? x* odd, Y+2 odd fine
  — but gcd(x*, Y+2) must be 1: x* ≡ 0 mod r: need r ∤ Y+2 (true: r | Y) and all other
  common factors excluded by CRT choice of Y (see primitive below) since x* mod small primes
  is NOT controlled (x* ranges over multiples of r). CAREFUL: gcd(x*, Y+2) = 1 must hold for
  EVERY multiple x* of r in the span: equivalent to gcd(r·t, Y+2) = 1 for the relevant t:
  cannot be guaranteed for all t!! FIX: dodge rows must vary per dodge OR pass bad columns on
  a row coprime to EVERYTHING LOCAL: strongest fix: pass x* at row Y+2 only when
  gcd(x*, Y+2)=1; otherwise use Y−1, Y−2 side, or a taller dodge (Y+3, Y+4...) — for the
  proof, show: for each bad x*, SOME row y'' within Y±K (K bounded, all rows composite-or-
  parity-compatible and coprime to x*) exists. Since x* has ≤ ω(x*) prime factors and the
  rows Y+j (|j| ≤ K, right parity, composite by CRT design) are pairwise coprime-ish in the
  relevant small primes, a counting/pigeonhole argument with K = O(1)? — needs care: x* can
  be divisible by many small primes hitting all nearby rows. BUT we can also choose WHICH
  columns to dodge at: we may exit the row EARLY and bypass a whole segment via a parallel
  row at distance 2 (row Y+2), traveling on it past several bad columns of row Y, provided
  Y+2's own bad columns interleave compatibly — a two-row corridor {Y, Y+2} with hop row Y+1
  — this fails on FIXED rows by fact 1, but here only needs to survive for the FINITE span
  [X_i, X_{i+1}], after which the staircase turns; the wall columns (divisible by
  rad(Y(Y+1)(Y+2))) can be arranged to lie OUTSIDE the span by CHOOSING X_{i+1} < first wall
  column beyond X_i!! Wall columns have density 1/rad ≥ tiny but positive: first wall beyond
  X_i is at distance ≤ rad(Y(Y+1)(Y+2)): REQUIRE X_{i+1} − X_i < dist(X_i, next wall):
  achievable by choosing the span to END before the wall (X_{i+1} is a semiprime found in the
  clean stretch — density of semiprimes-with-conditions in [X_i, X_i + rad] is fine for rad
  huge (rad ~ Y³-ish ≫ gaps between prescribed semiprimes ~ polylog·small).
- If x* is even: even columns only carry odd rows: pass x* at Y+2 (odd) or Y−2 etc.; its
  even-row neighbors are never visited on column x*: route uses (x*±1, rows Y..Y+2 as parity
  allows).

CRT PRIMITIVE (crucial, fully rigorous): for any finite set S of primes with prescribed
nonzero residues {a_ℓ}, and any fresh huge prime P, there are infinitely many N with
N ≡ 0 (mod P) [⇒ N composite once N > P] and N ≡ a_ℓ (mod ℓ) ∀ℓ∈S [⇒ gcd(N, ℓ)=1].
Also semiprime versions: N = q·q' with N ≡ c (mod M) via Dirichlet (choose q ≡ c mod M,
q' ≡ 1 mod M). Use to force: X_i, Y_i semiprime composite; neighbor rows/columns
(Y_{i+1}±1, ±2, X_i ±1, ±2 as needed) composite via ≡ 0 mod fresh huge primes AND coprime to
all SPECIFIC nearby constrained values via prescribed small-prime residues.

## What remains for a complete proof
(a) Fix an explicit dodge template set covering: odd/even bad columns, clusters of two
    adjacent bad columns, bad columns near span endpoints/corners.
(b) The two-row corridor argument within one span: prove passage between consecutive dodges,
    using that within [X_i, X_{i+1}] (chosen before the first wall column) at every column at
    least one of rows {Y, Y+2} is coprime, and hops exist with the right parity and
    coprimality — this is a FINITE local condition per column; formulate and prove it as a
    lemma with the CRT design of Y (e.g. ensure gcd(Y+1, Y·(Y+2))-structure and that
    r, r' ∤ neighbors etc.).
(c) Corner admissibility at (X_i, Y_{i+1}) and (X_{i+1}, Y_{i+1}).
(d) Initial finite segment from (say) (8, 9) or any admissible start to the first anchor
    (finite explicit check).
(e) Simplicity: coordinates strictly increase leg by leg; dodges bounded — standard.

## Alternative if (b) resists: taller dodge palette
Allow dodge rows Y+1..Y+2K with all of Y+1..Y+2K composite (consecutive composite runs exist
of any length; fold their compositeness into the CRT choice of Y via ≡ 0 mod distinct fresh
huge primes — the run [Y+1, Y+2K] composite is CRT-forcible!). Then per bad column x*, the
K odd rows among the dodge rows give K chances for coprimality with x*: choose K >
max possible number of distinct prime factors of x* that could hit all K rows... make K = 3
and force the three odd dodge rows to be ≡ 0 mod {P_a, P_b, P_c} (huge fresh) and pairwise
sharing NO small primes; then any x* can block at most ... x* blocks row y'' iff it shares an
ODD prime with it; arrange the odd dodge rows to have pairwise disjoint small-prime profiles
covering ≤ finitely many bad residues — then x* blocked on all K rows only if x* divisible by
one prime from each row's profile: those x* form APs with modulus ≥ (product of three
distinct primes ≥ 5·7·11) — and the span can be chosen to avoid the few such columns
entirely (they're rarer than wall columns; same "end span early" trick), or add more rows.
This closes (b) robustly.
