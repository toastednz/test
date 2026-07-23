"""Targeted #1212 run: hand gpt-5.6-sol the orchestrator's construction skeleton
and ask for a complete rigorous proof (route 5)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orclient import chat
from solve_loop import ATTEMPT_SYS, sv, ld

SP = os.path.dirname(os.path.abspath(__file__))
brief = open(f"{SP}/runs/1212/brief.md").read()
skel = open(f"{SP}/notes1212_skeleton.md").read()

user = f"""PROBLEM BRIEF:

{brief}

YOUR ASSIGNMENT (ROUTE 5): An orchestrating researcher has developed the following
construction skeleton with computationally verified negative results and a concrete
staircase design. Your job: turn it into a COMPLETE, rigorous, self-contained proof that the
answer to #1212 is YES — or find a genuine fatal obstruction in the skeleton and repair the
design. Fill every gap: exact dodge templates with parity case analysis, the CRT/Dirichlet
choices with full justification, span/wall-avoidance bookkeeping, corner admissibility,
initial segment, and simplicity. Write for a hostile referee.

ORCHESTRATOR'S SKELETON AND NOTES:

{skel}
"""

r = chat("openai/gpt-5.6-sol",
         [{"role": "system", "content": ATTEMPT_SYS.replace("{route_id}", "5")},
          {"role": "user", "content": user}],
         effort="xhigh", max_tokens=150000, tag="attempt-1212-r5")
sv(1212, "attempt_r5.md", r["content"])
print("saved attempt_r5.md:", r["content"][:120])
