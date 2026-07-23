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

Wave-1 targets:

| # | Problem | Round-1 outcome |
|---|---------|-----------------|
| 1212 | Infinite path in coprime lattice avoiding prime-prime pairs | 5 routes + orchestrator staircase: all BLOCKED with strong negative lemmas (bounded-coordinate impossibility; periodic monotone certificates impossible — proved here; CRT barrier circuits kill barrier-exclusion strategies) |
| 389 | n(n+1)…(n+k−1) divides (n+k)…(n+2k−1) for some k | BLOCKED ×4; orchestrator found clean reformulation C(x+2k,k)/C(x+k,k) ∈ ℤ + minimal-k data (OEIS A375071 extended to n=11) with shared-boundary structure; round 2 in flight |
| 196 | Every permutation of ℕ contains a monotone 4-term AP? | BLOCKED ×4 with substantial structure (U³-uniformity criterion; digitwise constructions provably fail) |
| 289 | 1 as a sum of k interval harmonic sums (all large k) | BLOCKED ×4 but rich exact machinery: count-changing equal-weight gadgets, near-solution off by 1/7140; round 2 in flight |
| 203 | m with 2^k3^ℓm+1 composite for all k,ℓ ≥ 0 | PARTIAL: q-cohort obstruction (sharp necessary condition on covering pools); orchestrator added Sophie-Germain/Izotov algebraic coset covering (m an odd fourth power kills k≡2, ℓ≡0 mod 4 for free) + smooth-index pool data; round 2 in flight |
| 273 | Covering system with all moduli p−1, p ≥ 5 prime | Computational: greedy/annealing insufficient; exact CP-SAT on the N=332640 universe (71 usable moduli, mass 1.083) running |
| 617 | Erdős–Gyárfás balanced-coloring conjecture (falsification at r=5) | SAT instance (K₂₆, 5 colors, 1.15M clauses) — suspended, low priority |

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
