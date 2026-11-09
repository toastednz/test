"""Download a corpus of public-domain novels from Project Gutenberg.

Writes one cleaned .txt per book into data/ (headers/licence text stripped).
"""
import os
import re
import sys
import time
import urllib.request

# (Gutenberg ID, title) -- classic English fiction, roughly 20 MB in total.
BOOKS = [
    (1342, "Pride and Prejudice"), (161, "Sense and Sensibility"), (158, "Emma"),
    (141, "Mansfield Park"), (105, "Persuasion"), (121, "Northanger Abbey"),
    (1400, "Great Expectations"), (98, "A Tale of Two Cities"), (766, "David Copperfield"),
    (730, "Oliver Twist"), (580, "The Pickwick Papers"), (1023, "Bleak House"),
    (768, "Wuthering Heights"), (1260, "Jane Eyre"), (145, "Middlemarch"),
    (2701, "Moby Dick"), (84, "Frankenstein"), (345, "Dracula"),
    (174, "The Picture of Dorian Gray"), (1661, "Adventures of Sherlock Holmes"),
    (2852, "The Hound of the Baskervilles"), (11, "Alice in Wonderland"),
    (74, "Tom Sawyer"), (76, "Huckleberry Finn"), (1184, "The Count of Monte Cristo"),
    (2600, "War and Peace"), (1399, "Anna Karenina"), (135, "Les Miserables"),
    (64317, "The Great Gatsby"), (36, "The War of the Worlds"), (35, "The Time Machine"),
    (120, "Treasure Island"), (215, "The Call of the Wild"), (110, "Tess of the d'Urbervilles"),
    (4300, "Ulysses"), (514, "Little Women"),
]

START = re.compile(r"\*\*\*\s*START OF (THE|THIS) PROJECT GUTENBERG.*?\*\*\*", re.I | re.S)
END = re.compile(r"\*\*\*\s*END OF (THE|THIS) PROJECT GUTENBERG", re.I)


def clean(text: str) -> str:
    m = START.search(text)
    if m:
        text = text[m.end():]
    m = END.search(text)
    if m:
        text = text[:m.start()]
    return text.strip()


def main(out_dir: str = os.path.join(os.path.dirname(__file__), "data")) -> None:
    os.makedirs(out_dir, exist_ok=True)
    total = 0
    for gid, title in BOOKS:
        path = os.path.join(out_dir, f"{gid}.txt")
        if not os.path.exists(path):
            url = f"https://www.gutenberg.org/cache/epub/{gid}/pg{gid}.txt"
            try:
                with urllib.request.urlopen(url, timeout=60) as r:
                    raw = r.read().decode("utf-8", errors="ignore")
            except Exception as e:  # keep going if one book fails
                print(f"  ! {title}: {e}", file=sys.stderr)
                continue
            with open(path, "w", encoding="utf-8") as f:
                f.write(clean(raw))
            time.sleep(0.5)  # be polite to Gutenberg
        size = os.path.getsize(path)
        total += size
        print(f"{title:40s} {size/1e6:6.2f} MB")
    print(f"\nTotal corpus: {total/1e6:.1f} MB in {out_dir}")


if __name__ == "__main__":
    main(*sys.argv[1:])
