# Erdős-problem research pipeline

An autonomous research pipeline attacking open problems from
[erdosproblems.com](https://www.erdosproblems.com), following the methodology
publicized by Shouqiao Wang (July 2026): careful problem selection, precise
per-problem briefs defining exactly what counts as a solution, long
independent solver runs on a frontier reasoning model, adversarial audits by
independent model families, and repair loops — plus local computation
(SAT/CP-SAT/exact arithmetic) for machine-verifiable certificates.

## Status

**Headline: Erdős Problem #906 has a candidate affirmative solution** — two
independent probabilistic proofs (a planar Gaussian Entire Function argument
via summable hole probabilities, and an order-4 Gaussian Taylor series
argument via first/second moments of smooth zero statistics). The primary
proof passed a complete adversarial audit sweep (Claude Opus 4.8, Gemini 3.1
Pro, Grok 4.5 — all VALID, zero substantive objections), was verified
line-by-line by the orchestrating model, and its key identity/asymptotics
were machine-checked. See `solutions/906.md`. Fittingly, #906 is the problem
Erdős said had been solved before ~1972 by a proof that was subsequently
lost; these are independent reconstructions. **Human expert review is still
required before this counts as resolved.**

All other attempts self-reported BLOCKED or PARTIAL with precise diagnoses
(the intended behavior of the prompt design — a wrong proof is worthless);
several produced substantial reusable partial results, catalogued below.

## Problem selection

653 open problems scraped with commentary; triaged by three independent
models (GPT-5.6-Terra, Claude Sonnet 5, DeepSeek V4 Pro) for tractability /
fame / linkage to major conjectures, per the selection philosophy: obscure,
recently digitized, constructive/finite-flavored problems; avoid famous or
prize problems and asymptotic-estimate problems.

Targets and outcomes (round 1 + round 2):

| # | Problem | Outcome |
|---|---------|---------|
| **906** | Entire f with every derivative subsequence having dense zeros | **SOLVED (candidate)** — two independent probabilistic proofs; primary passed full 3/3 adversarial audit sweep; see `solutions/906.md` |
| 477 | Polynomial f, set A with unique representation n = a + f(k) | BLOCKED ×3 (degree-2 case was already settled in comments; general case resists) |
| 1212 | Infinite path in coprime lattice avoiding prime-prime pairs | BLOCKED ×5 + orchestrator staircase refuted: strong negative lemmas (bounded-coordinate impossibility; periodic monotone certificates impossible — proved here via wall argument; CRT barrier circuits kill barrier-exclusion strategies) |
| 389 | n(n+1)…(n+k−1) divides (n+k)…(n+2k−1) for some k | BLOCKED ×4 + ×3 (round 2 with clean reformulation C(x+2k,k)/C(x+k,k) ∈ ℤ, carry criterion, extended minimal-k data, shared-boundary structure) |
| 196 | Every permutation of ℕ contains a monotone 4-term AP? | BLOCKED ×4 + ×2 (U³-uniformity criterion; LSB-lex obstruction shows local arguments cannot work; strengthened DEGS mechanisms) |
| 289 | 1 as a sum of k interval harmonic sums (all large k) | BLOCKED ×4 + ×3; machine-verified telescoping reservoir (residual exactly 1/Q_m) and 4→5 identity; problem localized at count-flexible completions (orchestrator proved fixed-shape compensations impossible) |
| 203 | m with 2^k3^ℓm+1 composite for all k,ℓ ≥ 0 | PARTIAL ×2 + BLOCKED: q-cohort obstruction; Sophie-Germain fourth-power coset covering (verified); proofs that smooth-index pools + algebraic identities alone cannot cover (mass < 3/4 + 1/4 barrier); exact finite-state row-orbit formulation for future search |
| 273 | Covering system with all moduli p−1, p ≥ 5 prime | UNDECIDED: greedy/annealing insufficient; CP-SAT on N=332640 (mass 1.083) and N=55440 (mass 1.044) both timed out UNKNOWN; parity-split analysis and side-B infeasibility at lcm 360 proved |
| 617 | Erdős–Gyárfás balanced-coloring (falsification at r=5) | SAT instance (K₂₆, 5 colors, 1.15M clauses) ran without verdict — suspended |

## Layout

- `pipeline/` — OpenRouter client (streaming, retries, cost ledger), triage,
  solve loop (brief → parallel attempts → adversarial audits → repairs),
  round-2 loop (fresh brief folding in all route diagnoses).
- `runs/<pid>/` — briefs, attempts, audits, summaries per problem.
- `notes/` — orchestrator research notes (e.g. #1212 staircase skeleton and
  its refutation).
- `sat/` — local computational attacks (SAT/CP-SAT/BFS/exact searches).
- `data/` — scraped problem set, triage shortlist.

## Verification policy

A problem is only marked solved if: the argument survives hostile audits from
three independent model families with zero substantive objections, the
orchestrating model has line-by-line verified it, every finite claim is
machine-checked, and (for constructive results) an explicit certificate is
independently verified by a short standalone script. Literature checks are
performed before any claim (the erdosproblems.com database can lag published
results).

API keys are never committed; the cost ledger and page cache are gitignored.
