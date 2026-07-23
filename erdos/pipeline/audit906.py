"""Immediate adversarial audits of the two #906 candidates by 3 model families."""
import os, sys
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orclient import chat
from solve_loop import AUDIT_SYS, sv, ld, verdict_of

SP = os.path.dirname(os.path.abspath(__file__))
brief = open(f"{SP}/runs/906/brief.md").read()
AUDITORS = [
    ("anthropic/claude-opus-4.8", "xhigh"),
    ("google/gemini-3.1-pro-preview", "high"),
    ("x-ai/grok-4.5", "high"),
]

def audit(cand_file, model, eff):
    cand = open(f"{SP}/runs/906/{cand_file}").read()
    short = model.split("/")[1].replace(".", "")
    out = f"audit_{cand_file.replace('.md','')}_{short}.md"
    if ld(906, out):
        return out, verdict_of(ld(906, out))
    user = f"""PROBLEM BRIEF:

{brief}

CLAIMED SOLUTION TO AUDIT:

{cand}

Audit it now. Remember: your only goal is to break it. Check every constant (Harnack constants, variance computations, Laguerre/Stirling asymptotics, Gaussian tail bounds), every 'clearly', and the final quantifier logic (almost-sure events, countable intersections, the reduction to the cofinite disc form). If the proof is probabilistic, verify the existence conclusion is legitimate."""
    r = chat(model, [{"role": "system", "content": AUDIT_SYS},
                     {"role": "user", "content": user}],
             effort=eff, max_tokens=60000, tag=f"audit906-{cand_file}-{short}")
    sv(906, out, r["content"])
    return out, verdict_of(r["content"])

jobs = []
for cf in ("attempt_r3.md", "attempt_r1.md"):
    for (m, e) in AUDITORS:
        jobs.append((cf, m, e))

with ThreadPoolExecutor(max_workers=6) as ex:
    futs = {ex.submit(audit, cf, m, e): (cf, m) for (cf, m, e) in jobs}
    for f in futs:
        cf, m = futs[f]
        try:
            out, v = f.result()
            print(f"{cf} x {m}: VERDICT={v}", flush=True)
        except Exception as err:
            print(f"{cf} x {m}: ERROR {err}", flush=True)
print("audits done")
