"""Next-word predictor that continues your sentence with three more sentences.

Model: word-level n-gram (default 4-gram) with backoff, trained on the
Gutenberg corpus in data/. It predicts one word at a time from the previous
words, sampling from what followed that context in the books, and stops once
three full sentences have been written.

Usage:
    python predict.py                       # interactive prompt
    python predict.py "It was a dark and stormy night."
    python predict.py --order 5 --temperature 0.8 "She opened the letter"
"""
import argparse
import glob
import os
import pickle
import random
import re
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(HERE, "data")
SENT_END = {".", "!", "?"}
# Titles like "Mr." are kept as one token so their period doesn't end a sentence.
TOKEN_RE = re.compile(r"(?:Mr|Mrs|Dr|St|Messrs|Mme|Mlle)\.|[A-Za-z]+(?:'[A-Za-z]+)*|[0-9]+|[.,!?;:]")
NO_SPACE_BEFORE = {".", ",", "!", "?", ";", ":"}


def tokenize(text: str) -> list[str]:
    text = text.replace("’", "'").replace("‘", "'")
    text = re.sub(r"\s+", " ", text)
    toks = TOKEN_RE.findall(text)
    # Drop chapter headings / roman numerals glued into the stream.
    return [t for t in toks if t not in {"CHAPTER", "Chapter"}]


def detokenize(tokens: list[str], capitalize_first: bool = True) -> str:
    out = ""
    cap_next = capitalize_first
    for t in tokens:
        w = t.capitalize() if cap_next and t[0].islower() else t
        out += w if (not out or t in NO_SPACE_BEFORE) else " " + w
        cap_next = t in SENT_END
    return out


class NGramModel:
    def __init__(self, order: int = 4):
        self.order = order
        # tables[n][context tuple of length n] -> Counter(next word)
        self.tables = [defaultdict(Counter) for _ in range(order)]

    def train(self, files: list[str]) -> None:
        for i, path in enumerate(files, 1):
            with open(path, encoding="utf-8") as f:
                toks = tokenize(f.read())
            for j in range(len(toks)):
                nxt = toks[j]
                for n in range(self.order):
                    if j - n < 0:
                        break
                    self.tables[n][tuple(toks[j - n:j])][nxt] += 1
            print(f"\r  trained on {i}/{len(files)} books", file=sys.stderr, end="")
        print(file=sys.stderr)
        # Prune rare contexts at the top orders to keep memory/file size sane.
        for n in range(2, self.order):
            self.tables[n] = {c: cnt for c, cnt in self.tables[n].items() if sum(cnt.values()) > 1}
        self.tables = [dict(t) for t in self.tables]

    def next_word_distribution(self, history: list[str]) -> Counter:
        """Longest matching context wins; back off when it's unseen or too sparse."""
        for n in range(self.order - 1, -1, -1):
            if n > len(history):
                continue
            ctx = tuple(history[len(history) - n:]) if n else ()
            cnt = self.tables[n].get(ctx)
            if cnt and (len(cnt) >= 2 or n <= 1):
                return cnt
        return self.tables[0][()]

    def predict_next(self, history, temperature=1.0, top_k=20, rng=random) -> str:
        cnt = self.next_word_distribution(history)
        items = cnt.most_common(top_k)
        words = [w for w, _ in items]
        weights = [c ** (1.0 / temperature) for _, c in items]
        return rng.choices(words, weights=weights)[0]

    def continue_text(self, prompt: str, sentences=3, max_words=200, **kw) -> str:
        history = tokenize(prompt)
        if history and history[-1] not in SENT_END:
            # Finish the user's sentence first, then write 3 new ones.
            while history[-1] not in SENT_END and len(history) < max_words:
                history.append(self.predict_next(history, **kw))
        start = len(history)
        generated, done = [], 0
        while done < sentences and len(generated) < max_words:
            w = self.predict_next(history, **kw)
            history.append(w)
            generated.append(w)
            if w in SENT_END:
                done += 1
        if generated and generated[-1] not in SENT_END:
            generated.append(".")
        completion = history[len(tokenize(prompt)):start]
        sents, cur = [], []
        for w in generated:
            cur.append(w)
            if w in SENT_END:
                sents.append(detokenize(cur))
                cur = []
        return detokenize(completion, capitalize_first=False), sents


def load_or_train(order: int) -> NGramModel:
    cache = os.path.join(HERE, f"model_{order}gram.pkl")
    if os.path.exists(cache):
        with open(cache, "rb") as f:
            return pickle.load(f)
    files = sorted(glob.glob(os.path.join(DATA_DIR, "*.txt")))
    if not files:
        sys.exit("No corpus found. Run:  python download_corpus.py")
    print(f"Training {order}-gram model on {len(files)} books (first run only)...", file=sys.stderr)
    model = NGramModel(order)
    model.train(files)
    with open(cache, "wb") as f:
        pickle.dump(model, f, protocol=pickle.HIGHEST_PROTOCOL)
    return model


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("prompt", nargs="*", help="your sentence (omit for interactive mode)")
    ap.add_argument("--order", type=int, default=4, help="n-gram order (default 4)")
    ap.add_argument("--sentences", type=int, default=3)
    ap.add_argument("--temperature", type=float, default=1.0, help="<1 = safer, >1 = wilder")
    ap.add_argument("--top-k", type=int, default=20)
    ap.add_argument("--seed", type=int)
    args = ap.parse_args()

    rng = random.Random(args.seed)
    model = load_or_train(args.order)
    kw = dict(temperature=args.temperature, top_k=args.top_k, rng=rng)

    def run(prompt: str) -> None:
        finish, sents = model.continue_text(prompt, sentences=args.sentences, **kw)
        print()
        if finish:
            sep = "" if finish[0] in NO_SPACE_BEFORE else " "
            print(f"Your sentence, completed: {prompt.strip()}{sep}{finish}")
        print(f"Next {args.sentences} sentences:")
        for i, s in enumerate(sents, 1):
            print(f"  {i}. {s}")
        print()

    if args.prompt:
        run(" ".join(args.prompt))
        return
    print("Type a sentence (Ctrl-D to quit).")
    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            break
        if line:
            run(line)


if __name__ == "__main__":
    main()
