import json, re, os, sys, threading
from concurrent.futures import ThreadPoolExecutor, as_completed
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from orclient import chat

SP = os.path.dirname(os.path.abspath(__file__))
probs = json.load(open(f'{SP}/problems_full.json'))
probs.sort(key=lambda p: p['id'])

WANG_SIX = {390, 486, 536, 788, 1002, 1038}
probs = [p for p in probs if p['id'] not in WANG_SIX]

SYS = """You are an expert research mathematician helping select target problems from the Erdős problems database (erdosproblems.com) for a serious solution attempt by a strong AI research system with weeks of effort available.

The selection philosophy (following a recently successful methodology):
- AVOID problems that are famous, heavily attacked, carry significant prize money, or are closely tied to major open conjectures (e.g. anything within reach of sunflower/union-closed/Erdos-Straus/happy-ending/Ramsey-growth folklore, additive combinatorics barriers, etc.).
- AVOID problems asking for asymptotics/estimates of a hard function ("determine the order of f(n)") — these rarely admit clean complete solutions.
- PREFER obscure, recently-digitized, little-studied problems, especially clean yes/no questions or exact statements which might yield to: a clever explicit construction; a short elementary proof; a finite computation; induction; a generating-function or counting identity; a known-technique transfer from a neighboring area.
- PREFER problems where the commentary shows NO serious partial results by strong mathematicians (empty or thin commentary is a good sign), and problems that smell "unattempted" rather than "resistant".
- FLAG problems that you suspect are already solved in the published literature (the database may be out of date) — these are valuable easy wins via literature search.

For EACH problem in the user message output a JSON object with fields:
 "id": int,
 "verdict": "TARGET" | "MAYBE" | "AVOID",
 "tract": 0-10 (probability-weighted tractability for a top AI system with weeks of effort; 10 = very likely solvable),
 "fame": 0-10 (fame/attention/prior attack intensity; 0 = obscure),
 "conj": "name of major linked conjecture" or "",
 "littsolved": true|false (you suspect it is already solved in existing literature),
 "attack": "one concise sentence: most promising route",
 "why": "one concise sentence: main reason for verdict"

Output ONLY a JSON array of these objects, one per problem given, in the same order. No prose."""

def batch_prompt(batch):
    items = []
    for p in batch:
        c = p['commentary'][:900]
        items.append(f"### Problem {p['id']} [{p['status']}] (prize=${p['prize']}) tags={','.join(p['tags'])}\nSTATEMENT: {p['statement'][:1200]}\nCOMMENTARY: {c}")
    return "\n\n".join(items)

def parse_json_array(text):
    m = re.search(r'\[.*\]', text, re.S)
    if not m:
        return None
    t = m.group(0)
    try:
        return json.loads(t)
    except Exception:
        t2 = re.sub(r',\s*([\]}])', r'\1', t)
        try:
            return json.loads(t2)
        except Exception:
            return None

def run_model(model, tagname, effort):
    out_fn = f'{SP}/triage_{tagname}.json'
    done = {}
    if os.path.exists(out_fn):
        done = {int(k): v for k, v in json.load(open(out_fn)).items()}
    lock = threading.Lock()
    B = 10
    batches = [probs[i:i+B] for i in range(0, len(probs), B)]
    batches = [b for b in batches if any(p['id'] not in done for p in b)]
    print(f'[{tagname}] {len(batches)} batches to do')

    def do_batch(bi, batch):
        prompt = batch_prompt(batch)
        try:
            r = chat(model, [{"role": "system", "content": SYS},
                             {"role": "user", "content": prompt}],
                     effort=effort, max_tokens=30000, tag=f'triage-{tagname}-{bi}')
            arr = parse_json_array(r['content'])
            if not arr:
                return bi, None
            res = {}
            for obj in arr:
                if isinstance(obj, dict) and 'id' in obj:
                    res[int(obj['id'])] = obj
            return bi, res
        except Exception as e:
            print(f'[{tagname}] batch {bi} error: {e}', flush=True)
            return bi, None

    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(do_batch, bi, b): bi for bi, b in enumerate(batches)}
        for fut in as_completed(futs):
            bi, res = fut.result()
            if res:
                with lock:
                    done.update(res)
                    json.dump({str(k): v for k, v in done.items()}, open(out_fn, 'w'))
            print(f'[{tagname}] batch {bi} done ({len(done)} total)', flush=True)
    print(f'[{tagname}] FINISHED with {len(done)} problems scored')

if __name__ == '__main__':
    which = sys.argv[1]
    cfg = {
        'terra': ('openai/gpt-5.6-terra', 'medium'),
        'sonnet': ('anthropic/claude-sonnet-5', 'medium'),
        'deepseek': ('deepseek/deepseek-v4-pro', 'high'),
    }[which]
    run_model(cfg[0], which, cfg[1])
