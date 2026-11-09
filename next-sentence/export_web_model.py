"""Export a pruned copy of the n-gram model as compact JSON for the web page.

Keeps the top continuations of every context seen often enough, and maps words
to integer ids so the file stays small enough to load in a browser.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from predict import load_or_train  # noqa: E402

TOP_K = 10
MIN_COUNT = {1: 3, 2: 5, 3: 6}  # min total count of a context to keep it, by context length


def main(out_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)), "web")):
    model = load_or_train(4)
    tables = []
    used = set()
    for n, table in enumerate(model.tables):
        kept = {}
        for ctx, cnt in table.items():
            if n and sum(cnt.values()) < MIN_COUNT[n]:
                continue
            top = cnt.most_common(TOP_K if n else 3000)
            if n >= 2 and len(top) < 2:
                continue  # one-way contexts just copy the book verbatim; back off instead
            kept[ctx] = top
            used.update(ctx)
            used.update(w for w, _ in top)
        tables.append(kept)
    vocab = sorted(used, key=lambda w: -model.tables[0][()].get(w, 0))
    idx = {w: i for i, w in enumerate(vocab)}
    enc = []
    for n, kept in enumerate(tables):
        enc.append({
            " ".join(str(idx[w]) for w in ctx): [x for w, c in top for x in (idx[w], c)]
            for ctx, top in kept.items()
        })
        print(f"order {n}: {len(kept):,} contexts", file=sys.stderr)
    # Two files, each under the 16 MB limit for a published artifact file.
    os.makedirs(out_dir, exist_ok=True)
    parts = {"model-a.json": {"vocab": vocab, "tables": enc[:3]}, "model-b.json": {"tables": enc[3:]}}
    for name, obj in parts.items():
        path = os.path.join(out_dir, name)
        with open(path, "w") as f:
            json.dump(obj, f, separators=(",", ":"))
        print(f"wrote {path}: {os.path.getsize(path)/1e6:.1f} MB", file=sys.stderr)
    print(f"vocabulary: {len(vocab):,} words", file=sys.stderr)


if __name__ == "__main__":
    main(*sys.argv[1:])
