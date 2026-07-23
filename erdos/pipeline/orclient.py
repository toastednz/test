"""Minimal OpenRouter client with streaming, retries, and a cost ledger."""
import json, os, time, sys, threading
import urllib.request, urllib.error

BASE = "https://openrouter.ai/api/v1/chat/completions"
LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ledger.jsonl")
_ledger_lock = threading.Lock()

def _key():
    k = os.environ.get("OPENROUTER_API_KEY")
    if not k:
        # fall back to env file
        p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "or.env")
        for line in open(p):
            if "OPENROUTER_API_KEY" in line:
                k = line.split('"')[1]
    return k

def chat(model, messages, effort=None, max_tokens=None, temperature=None,
         timeout=7200, tag="", retries=5, providers_ignore=None):
    """Streaming chat completion. Returns dict with content, reasoning, usage, cost."""
    body = {
        "model": model,
        "messages": messages,
        "stream": True,
        "usage": {"include": True},
    }
    if effort:
        body["reasoning"] = {"effort": effort}
    if max_tokens:
        body["max_tokens"] = max_tokens
    if temperature is not None:
        body["temperature"] = temperature
    if providers_ignore:
        body["provider"] = {"ignore": providers_ignore}

    delay = 2.0
    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                BASE,
                data=json.dumps(body).encode(),
                headers={
                    "Authorization": f"Bearer {_key()}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://local.pipeline",
                    "X-Title": "erdos-pipeline",
                },
            )
            content, reasoning, usage, finish = [], [], None, None
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                buf = b""
                while True:
                    chunk = resp.read(65536)
                    if not chunk:
                        break
                    buf += chunk
                    while b"\n" in buf:
                        line, buf = buf.split(b"\n", 1)
                        line = line.strip()
                        if not line.startswith(b"data: "):
                            continue
                        data = line[6:]
                        if data == b"[DONE]":
                            continue
                        try:
                            j = json.loads(data)
                        except json.JSONDecodeError:
                            continue
                        if j.get("usage"):
                            usage = j["usage"]
                        for ch in j.get("choices", []):
                            d = ch.get("delta") or {}
                            if d.get("content"):
                                content.append(d["content"])
                            if d.get("reasoning"):
                                reasoning.append(d["reasoning"])
                            if ch.get("finish_reason"):
                                finish = ch["finish_reason"]
            out = {
                "model": model,
                "content": "".join(content),
                "reasoning": "".join(reasoning),
                "usage": usage or {},
                "finish": finish,
                "tag": tag,
            }
            cost = (usage or {}).get("cost")
            with _ledger_lock:
                with open(LEDGER, "a") as f:
                    f.write(json.dumps({
                        "ts": time.time(), "model": model, "tag": tag,
                        "cost": cost,
                        "pt": (usage or {}).get("prompt_tokens"),
                        "ct": (usage or {}).get("completion_tokens"),
                        "finish": finish,
                    }) + "\n")
            if not out["content"]:
                raise RuntimeError(f"no content (finish={finish}, reasoning_len={len(out['reasoning'])})")
            if finish is None:
                raise RuntimeError("stream truncated (no finish_reason)")
            return out
        except Exception as e:
            last_err = e
            body_err = ""
            if isinstance(e, urllib.error.HTTPError):
                try:
                    body_err = e.read().decode()[:500]
                except Exception:
                    pass
                # don't retry on 400/401/402/403 except 429
                if e.code in (400, 401, 402, 403, 404):
                    raise RuntimeError(f"HTTP {e.code}: {body_err}") from e
            sys.stderr.write(f"[orclient] attempt {attempt+1} failed ({e}) {body_err}\n")
            time.sleep(delay)
            delay = min(delay * 2, 60)
    raise RuntimeError(f"all retries failed: {last_err}")

def spend():
    tot = 0.0
    try:
        for line in open(LEDGER):
            j = json.loads(line)
            if j.get("cost"):
                tot += j["cost"]
    except FileNotFoundError:
        pass
    return tot

if __name__ == "__main__":
    # smoke test
    model = sys.argv[1] if len(sys.argv) > 1 else "openai/gpt-5.6-sol"
    effort = sys.argv[2] if len(sys.argv) > 2 else "high"
    r = chat(model, [{"role": "user", "content": "Reply with exactly: OK"}],
             effort=effort, max_tokens=8000, tag="smoke")
    print("content:", r["content"][:100])
    print("usage:", json.dumps(r["usage"]))
