# Next-sentence predictor

Type a sentence; a next-word predictor trained on ~38 MB of classic novels
(36 public-domain books from Project Gutenberg, ~7M words) predicts one word at a
time and writes out the **next three sentences**. If your sentence has no final
`. ! ?`, it finishes your sentence first.

```bash
python download_corpus.py                     # ~38 MB into data/ (one-off)
python predict.py "It was a dark and stormy night."
python predict.py                             # interactive mode
python predict.py --temperature 0.7 --seed 42 "She opened the letter"
```

The first run trains a 4-gram model (~1 min) and caches it as `model_4gram.pkl`;
later runs load in a few seconds. Only the Python standard library is needed.

**How it works:** for every 1-, 2- and 3-word context in the books it counts which
word came next. To predict, it looks up the last 3 words you have; if that context
was never seen (or had only one continuation) it backs off to the last 2 words,
then 1, and samples from the top 20 candidates. `--temperature` below 1 picks
common words more often; above 1 gets wilder. `--order 5` copies longer phrases
from the books, `--order 3` is more random.

The output is grammatical in short stretches but drifts in meaning—that's the
limit of n-gram models. For coherent multi-sentence output you'd train a small
neural language model (e.g. a GPT-style transformer) on the same `data/` corpus.
