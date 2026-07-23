"""Round 2 for a problem: fresh brief (enriched commentary), plus synthesis of
round-1 route diagnoses, then N targeted attempts continuing from that state."""
import json, os, re, sys, glob
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orclient import chat
from solve_loop import ATTEMPT_SYS, BRIEF_SYS, sv, ld, status_of

SP = os.path.dirname(os.path.abspath(__file__))
pid = int(sys.argv[1])
n_att = int(sys.argv[2]) if len(sys.argv) > 2 else 2

problems = {p['id']: p for p in json.load(open(f'{SP}/problems_full.json'))}
problem = problems[pid]

# gather round-1 diagnoses
diags = []
for fn in sorted(glob.glob(f"{SP}/runs/{pid}/attempt_r*.md")):
    txt = open(fn).read()
    m = re.search(r'## Route Diagnosis\s*(.*?)\s*(?:\Z)', txt, re.S)
    stat = status_of(txt)
    name = os.path.basename(fn)
    if m:
        diags.append(f"### {name} [{stat}]\n{m.group(1)[:4000]}")
    res = re.search(r'## Result\s*(.*?)\s*##', txt, re.S)
    if res:
        diags.append(f"(result summary of {name}: {res.group(1)[:1500]})")
diag_txt = "\n\n".join(diags)[:60000]

brief2 = ld(pid, "brief2.md")
if not brief2:
    user = f"""Erdős Problem #{pid} (status: {problem['status']}, prize: ${problem['prize']}, tags: {', '.join(problem['tags'])})

STATEMENT:
{problem['statement']}

DATABASE COMMENTARY AND ORCHESTRATOR RESEARCH NOTES (includes computed data — treat computed data as reliable):
{problem['commentary']}

ROUND-1 ROUTE DIAGNOSES (previous independent deep attempts, all honest about failure points):
{diag_txt}

Write the full problem brief for ROUND 2. Fold in everything learned: which routes are dead (and the precise obstruction), which sub-lemmas were PROVED (reusable), and design 4 NEW attack routes that are genuinely responsive to the diagnoses (not rehashes)."""
    r = chat("openai/gpt-5.6-sol", [{"role": "system", "content": BRIEF_SYS},
                                    {"role": "user", "content": user}],
             effort="xhigh", max_tokens=60000, tag=f"brief2-{pid}")
    brief2 = r["content"]
    sv(pid, "brief2.md", brief2)
print(f"[{pid}] round-2 brief ready", flush=True)

def attempt(i):
    fn = f"attempt2_r{i}.md"
    ex = ld(pid, fn)
    if ex:
        return ex
    user = f"""ROUND-2 PROBLEM BRIEF (includes everything learned in round 1):

{brief2}

YOUR ASSIGNMENT: pursue ROUTE {i} from the round-2 brief with full force. Round-1 attempts are summarized in the brief — do not repeat their dead ends. Work now."""
    r = chat("openai/gpt-5.6-sol",
             [{"role": "system", "content": ATTEMPT_SYS.replace("{route_id}", str(i))},
              {"role": "user", "content": user}],
             effort="xhigh", max_tokens=150000, tag=f"attempt2-{pid}-r{i}")
    sv(pid, fn, r["content"])
    return r["content"]

with ThreadPoolExecutor(max_workers=n_att) as ex:
    futs = {ex.submit(attempt, i): i for i in range(1, n_att + 1)}
    for f in futs:
        try:
            a = f.result()
            print(f"[{pid}] round2 r{futs[f]}: {status_of(a)}", flush=True)
        except Exception as e:
            print(f"[{pid}] round2 r{futs[f]} failed: {e}", flush=True)
print("round2 done for", pid, flush=True)
