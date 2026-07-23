import json, re, html as ihtml, os, time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

SP = os.path.dirname(os.path.abspath(__file__))
probs = json.load(open(f'{SP}/open_problems.json'))
os.makedirs(f'{SP}/pages', exist_ok=True)

def fetch(pid):
    fn = f'{SP}/pages/{pid}.html'
    if os.path.exists(fn) and os.path.getsize(fn) > 5000:
        return pid, 'cached'
    for attempt in range(3):
        try:
            req = urllib.request.Request(f'https://www.erdosproblems.com/{pid}',
                                         headers={'User-Agent': 'research-pipeline (contact: user)'})
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
            open(fn, 'wb').write(data)
            return pid, 'ok'
        except Exception as e:
            time.sleep(2 * (attempt + 1))
    return pid, 'fail'

with ThreadPoolExecutor(max_workers=10) as ex:
    results = list(ex.map(fetch, [p['id'] for p in probs]))
fails = [pid for pid, s in results if s == 'fail']
print('fetched:', len(results), 'fails:', fails)

def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return ihtml.unescape(re.sub(r'\s+', ' ', s)).strip()

out = []
for p in probs:
    pid = p['id']
    fn = f'{SP}/pages/{pid}.html'
    if not os.path.exists(fn):
        continue
    h = open(fn, encoding='utf-8').read()
    m = re.search(r'id="content">(.*?)</div>\s*<div id="problem_id">', h, re.S)
    stmt = clean(m.group(1)) if m else p['statement']
    mt = re.search(r'<div id="tags">(.*?)</div>', h, re.S)
    tags = re.findall(r'/tags/([^"]+)"', mt.group(1)) if mt else []
    # additional commentary blocks (skip the LaTeX-source/footer p tags)
    adds = re.findall(r'<div class="problem-additional-text"[^>]*>(.*?)</div>', h, re.S)
    comm = []
    for a in adds:
        a = re.sub(r'<p style="text-align: center.*?</p>', ' ', a, flags=re.S)
        c = clean(a)
        if c:
            comm.append(c)
    med = re.search(r'This page was last edited (\d+ \w+ \d+)', h)
    out.append({
        'id': pid, 'status': p['status'], 'tip': p['tip'], 'prize': p['prize'],
        'statement': stmt, 'tags': tags, 'commentary': ' || '.join(comm),
        'last_edited': med.group(1) if med else '',
    })

json.dump(out, open(f'{SP}/problems_full.json', 'w'), indent=1)
print('extracted:', len(out))
comm_have = sum(1 for o in out if o['commentary'])
print('with commentary:', comm_have)
