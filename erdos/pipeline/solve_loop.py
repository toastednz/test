"""Research loop for one Erdos problem, following the Wang methodology:
  brief -> parallel independent attempts (strong model, max effort)
        -> adversarial audits (independent model families)
        -> repair rounds -> final verdict.
All transcripts persisted under runs/<pid>/.
"""
import json, os, re, sys, time
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orclient import chat, spend

SP = os.path.dirname(os.path.abspath(__file__))
SOLVER = "openai/gpt-5.6-sol"
BRIEF_MODEL = "openai/gpt-5.6-sol"
AUDITORS = [
    ("anthropic/claude-opus-4.8", "xhigh"),
    ("google/gemini-3.1-pro-preview", "high"),
    ("x-ai/grok-4.5", "high"),
]

def sv(pid, name, obj):
    d = f"{SP}/runs/{pid}"
    os.makedirs(d, exist_ok=True)
    fn = f"{d}/{name}"
    if isinstance(obj, str):
        open(fn, "w").write(obj)
    else:
        json.dump(obj, open(fn, "w"), indent=1)
    return fn

def ld(pid, name):
    fn = f"{SP}/runs/{pid}/{name}"
    if os.path.exists(fn):
        return open(fn).read()
    return None

BRIEF_SYS = """You are a research mathematician preparing a rigorous problem brief for an AI research system that will attempt to fully solve an open problem from the Erdős database. Write the brief with extreme care. It must contain:

1. PRECISE STATEMENT: restate the problem completely formally, defining every object and quantifier. If the database statement is ambiguous, give the most standard reading (and note alternatives).
2. WHAT COUNTS AS A SOLUTION: exactly what a complete proof must establish, and exactly what a complete disproof must establish (including what an explicit counterexample must satisfy and how it can be verified).
3. WHAT DOES NOT COUNT: weaker results that do NOT resolve the problem (partial ranges, asymptotic improvements, conditional results, heuristics).
4. KNOWN RESULTS AND CONTEXT: summarize the given commentary; add any theorems you are confident are relevant (with names). Flag any part of the problem already settled.
5. TRAPS AND EDGE CASES: problem-specific pitfalls (degenerate cases, small cases, off-by-one in definitions, standard fallacious arguments that seem to work).
6. VERIFICATION HOOKS: any finite computations or small-case checks that would support or refute intermediate claims, described concretely so they can be coded.
7. ATTACK ROUTES: 4-6 genuinely distinct routes (different core mechanisms, not variations). For each: the key lemma it needs, why it might work, the most likely failure point, and a quick test to see if it is blocked. Include at least one route aimed at DISPROOF if remotely plausible.
8. VERDICT ON DIFFICULTY: honest assessment; if the problem is equivalent to or implied by a famous hard conjecture, say so loudly.

Be concrete and technical throughout. This brief is the foundation for weeks of automated research."""

ATTEMPT_SYS = """You are an elite research mathematician with unlimited patience, working on an open Erdős problem. You have a complete problem brief. Your assignment: pursue ROUTE {route_id} from the brief (details repeated in the user message) as deeply as possible, while remaining alert to superior alternatives that emerge from your analysis.

Non-negotiable working rules:
- The goal is a COMPLETE, RIGOROUS solution (proof or disproof) meeting the brief's success criteria. Partial progress is only valuable as a stepping stone; never dress it up as a solution.
- Search aggressively for counterexamples to every lemma you formulate, BEFORE trying to prove it. Test small cases numerically (simulate the computation mentally with genuine care, or state precisely what should be computed).
- If a step only works "morally" or "should be routine", treat it as UNPROVED and attack it until it is a complete argument or dies.
- Mark your route BLOCKED if it reduces the problem to another unproved statement of comparable strength; diagnose the block precisely.
- Keep a running ledger of: proved lemmas (with full proofs), plausible-but-unproved claims, and dead ends with reasons.
- It is vastly better to return BLOCKED with a sharp diagnosis than a proof with a gap. A wrong proof is worthless and wastes everyone's time.

OUTPUT FORMAT (mandatory):
Start with exactly one line: STATUS: SOLVED-PROOF | SOLVED-DISPROOF | PARTIAL | BLOCKED
Then:
## Result
(one-paragraph summary of what you established)
## Complete Argument
(if SOLVED: the full proof/disproof written for a hostile referee, every step justified, all cases covered. If PARTIAL/BLOCKED: your best rigorous partial results.)
## Self-Audit
(the three weakest points of your argument, stated honestly; for each, why you believe it holds anyway)
## Computations To Verify
(concrete finite checks a computer could run to support/refute your key claims, as explicit pseudocode or Python)
## Route Diagnosis
(what worked, what is blocked and why, what a fresh attempt should try)"""

AUDIT_SYS = """You are a hostile referee for a mathematics journal, reviewing a claimed solution to an open Erdős problem. Your ONLY goal is to find a fatal error or gap. Assume the proof is wrong; your job is to locate the flaw. The authors' reputation means nothing.

Procedure:
1. Restate what must be proved (from the problem brief). Check the claimed result actually resolves the stated problem (right quantifiers, right direction, no weakening).
2. Go lemma by lemma, step by step. For each nontrivial claim: attempt to verify it independently; actively search for counterexamples (test small/degenerate cases CONCRETELY — do the arithmetic).
3. Check every 'clearly/obviously/standard' step — these hide most fatal errors.
4. Check edge cases and the brief's listed traps.
5. If a cited known theorem is used, verify the citation is real, correctly stated, and correctly applied (hypotheses satisfied!).

OUTPUT FORMAT (mandatory):
Start with exactly one line: VERDICT: VALID | FATAL | GAPS | UNSURE
- VALID = you tried hard to break it and failed; you would stake your reputation on it.
- FATAL = concrete error that kills the argument (exhibit it precisely, with a counterexample where possible).
- GAPS = incomplete steps that might be fixable (list each precisely).
- UNSURE = you could not decide within your effort budget (say exactly where you got stuck).
Then a numbered list of every issue found, ordered by severity, each with: location (quote the offending passage), the problem, and if possible a concrete counterexample or fix suggestion."""

REPAIR_SYS = """You are the same elite research mathematician, continuing work on the open Erdős problem. Your previous attempt produced the candidate argument below, and independent hostile referees have produced the audit reports below.

Rules:
- Address EVERY issue the referees raise. For each: either repair the argument rigorously, or concede the point and mark the route BLOCKED.
- Referees may themselves be wrong: if you believe an objection is mistaken, refute it with a complete argument and concrete verification (e.g. work the small case they claim fails).
- No patch-over-patch: if the fix requires a genuinely different mechanism, redesign the argument from that point.
- Same output format as before (STATUS line, Result, Complete Argument, Self-Audit, Computations To Verify, Route Diagnosis). The Complete Argument must be SELF-CONTAINED (fully rewritten, not a diff)."""

def make_brief(pid, problem):
    ex = ld(pid, "brief.md")
    if ex:
        return ex
    user = f"""Erdős Problem #{pid} (from erdosproblems.com, status: {problem['status']}, prize: ${problem['prize']}, tags: {', '.join(problem['tags'])})

STATEMENT:
{problem['statement']}

DATABASE COMMENTARY (known results, context):
{problem['commentary']}

Write the full problem brief now."""
    r = chat(BRIEF_MODEL, [{"role": "system", "content": BRIEF_SYS},
                           {"role": "user", "content": user}],
             effort="high", max_tokens=40000, tag=f"brief-{pid}")
    sv(pid, "brief.md", r["content"])
    return r["content"]

def run_attempt(pid, brief, route_id, tag_suffix=""):
    fn = f"attempt_r{route_id}{tag_suffix}.md"
    ex = ld(pid, fn)
    if ex:
        return ex
    user = f"""PROBLEM BRIEF:

{brief}

YOUR ASSIGNMENT: pursue ROUTE {route_id} (as numbered in the brief's ATTACK ROUTES section). If that route is manifestly hopeless after real effort, you may switch to the most promising alternative — but only after documenting the block. Work now. Take as long as you need."""
    r = chat(SOLVER, [{"role": "system", "content": ATTEMPT_SYS.replace("{route_id}", str(route_id))},
                      {"role": "user", "content": user}],
             effort="xhigh", max_tokens=150000, tag=f"attempt-{pid}-r{route_id}{tag_suffix}")
    sv(pid, fn, r["content"])
    if r.get("reasoning"):
        sv(pid, f"attempt_r{route_id}{tag_suffix}.reasoning.txt", r["reasoning"][-200000:])
    return r["content"]

def run_audit(pid, brief, candidate, auditor_i, cand_name):
    model, eff = AUDITORS[auditor_i % len(AUDITORS)]
    short = model.split("/")[1].replace(".", "")
    fn = f"audit_{cand_name}_{short}.md"
    ex = ld(pid, fn)
    if ex:
        return ex
    user = f"""PROBLEM BRIEF:

{brief}

CLAIMED SOLUTION TO AUDIT:

{candidate}

Audit it now. Remember: your only goal is to break it."""
    r = chat(model, [{"role": "system", "content": AUDIT_SYS},
                     {"role": "user", "content": user}],
             effort=eff, max_tokens=60000, tag=f"audit-{pid}-{cand_name}-{short}")
    sv(pid, fn, r["content"])
    return r["content"]

def run_repair(pid, brief, candidate, audits, round_i, cand_name):
    fn = f"repair_{cand_name}_round{round_i}.md"
    ex = ld(pid, fn)
    if ex:
        return ex
    audits_txt = "\n\n====== NEXT REFEREE REPORT ======\n\n".join(audits)
    user = f"""PROBLEM BRIEF:

{brief}

YOUR PREVIOUS CANDIDATE ARGUMENT:

{candidate}

HOSTILE REFEREE REPORTS:

{audits_txt}

Produce your revised, self-contained result now."""
    r = chat(SOLVER, [{"role": "system", "content": REPAIR_SYS},
                      {"role": "user", "content": user}],
             effort="xhigh", max_tokens=150000, tag=f"repair-{pid}-{cand_name}-{round_i}")
    sv(pid, fn, r["content"])
    return r["content"]

def status_of(text):
    m = re.search(r'STATUS:\s*(SOLVED-PROOF|SOLVED-DISPROOF|PARTIAL|BLOCKED)', text or "")
    return m.group(1) if m else "?"

def verdict_of(text):
    m = re.search(r'VERDICT:\s*(VALID|FATAL|GAPS|UNSURE)', text or "")
    return m.group(1) if m else "?"

def solve_problem(pid, n_routes=4, max_repair_rounds=2):
    problems = {p['id']: p for p in json.load(open(f'{SP}/problems_full.json'))}
    problem = problems[pid]
    log = lambda s: print(f"[{pid}] {s}", flush=True)
    log(f"spend so far: ${spend():.2f}")
    brief = make_brief(pid, problem)
    log("brief ready")

    with ThreadPoolExecutor(max_workers=n_routes) as ex:
        futs = {ex.submit(run_attempt, pid, brief, i + 1): i + 1 for i in range(n_routes)}
        attempts = {}
        for f in futs:
            rid = futs[f]
            try:
                attempts[rid] = f.result()
            except Exception as e:
                log(f"route {rid} attempt failed: {e}")
    for rid, a in sorted(attempts.items()):
        log(f"route {rid}: STATUS={status_of(a)}")

    # candidates claiming a full solution get audited; else best partial noted
    cands = {f"r{rid}": a for rid, a in attempts.items()
             if status_of(a) in ("SOLVED-PROOF", "SOLVED-DISPROOF")}
    summary = {"pid": pid, "routes": {str(r): status_of(a) for r, a in attempts.items()},
               "candidates": {}, "final": "NO-SOLUTION-CLAIMED"}
    for cname, cand in list(cands.items()):
        cur = cand
        for rnd in range(max_repair_rounds + 1):
            with ThreadPoolExecutor(max_workers=3) as ex:
                afuts = [ex.submit(run_audit, pid, brief, cur, i, f"{cname}_v{rnd}")
                         for i in range(len(AUDITORS))]
                audits = []
                for f in afuts:
                    try:
                        audits.append(f.result())
                    except Exception as e:
                        log(f"audit failed: {e}")
            verdicts = [verdict_of(a) for a in audits]
            log(f"{cname} round {rnd} verdicts: {verdicts}")
            summary["candidates"].setdefault(cname, []).append(verdicts)
            if verdicts and all(v == "VALID" for v in verdicts):
                summary["final"] = f"CANDIDATE-{cname}-SURVIVED-{status_of(cur)}"
                sv(pid, f"FINAL_{cname}.md", cur)
                sv(pid, "summary.json", summary)
                log(f"*** {cname} SURVIVED ALL AUDITS ({status_of(cur)}) ***")
                return summary
            if rnd == max_repair_rounds:
                break
            try:
                cur = run_repair(pid, brief, cur, audits, rnd + 1, cname)
            except Exception as e:
                log(f"repair failed: {e}")
                break
            if status_of(cur) in ("BLOCKED", "PARTIAL"):
                log(f"{cname} conceded after repair round {rnd+1}")
                break
    sv(pid, "summary.json", summary)
    log(f"done; final={summary['final']}; spend now ${spend():.2f}")
    return summary

if __name__ == "__main__":
    pid = int(sys.argv[1])
    n_routes = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    solve_problem(pid, n_routes=n_routes)
