#!/usr/bin/env python3
"""readcheck: measurable checks for casual, readable prose (blog style).

Usage: python3 readcheck.py FILE [FILE ...]   (plain text or markdown)

Each check has a target band taken from plain-language guidance
(Cutts / Plain English Campaign, Australian Style Manual, Hemingway-style
linters). Passing all checks does not prove the text is good. Failing
several is a strong signal that it is hard to read.
"""
import re
import sys

PASSIVE_AUX = r"\b(?:is|are|was|were|be|been|being|get|got|gets)\b"
IRREGULAR_PP = (
    "built done made known seen shown taken given written run found sent "
    "kept left held told thought brought bought caught taught set put read "
    "chosen driven broken spoken stolen frozen hidden"
).split()
PASSIVE_RE = re.compile(
    PASSIVE_AUX + r"\s+(?:\w+ly\s+)?(?:\w+ed|" + "|".join(IRREGULAR_PP) + r")\b",
    re.I,
)
FILLER = [
    "very", "really", "basically", "actually", "quite", "rather", "simply",
    "extremely", "literally", "in order to", "utilize", "utilise", "leverage",
    "facilitate", "it is important to note", "it should be noted",
    "a number of", "due to the fact that", "in terms of", "with respect to",
    "moreover", "furthermore", "thus", "hence", "aforementioned", "whereby",
    "robust", "seamless", "delve", "paradigm",
]
NOMINAL_RE = re.compile(r"\b\w{4,}(?:tion|sion|ment|ance|ence|ity|ness|ization)s?\b", re.I)
PERSON_RE = re.compile(r"\b(?:i|i'm|i've|i'd|me|my|we|we're|we've|us|our|you|you're|you've|your)\b", re.I)
CONTRACTION_RE = re.compile(r"\b\w+'(?:t|s|re|ve|ll|d|m)\b", re.I)


def strip_markup(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)       # code blocks
    text = re.sub(r"`[^`]*`", "X", text)                       # inline code
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)          # images
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)       # links
    text = re.sub(r"https?://\S+", "URL", text)
    text = re.sub(r"^\s*#+\s.*$", "", text, flags=re.M)        # headings
    text = re.sub(r"^\s*(?:[-*+]|\d+\.)\s+", "", text, flags=re.M)
    return text.replace("’", "'")


def syllables(word):
    w = word.lower()
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:es|ed|e)$", "", w)
    n = len(re.findall(r"[aeiouy]+", w))
    return max(1, n)


def sentences_of(paragraph):
    parts = re.split(r"(?<=[.!?])[\"')\]]*\s+(?=[A-Z0-9\"'(\[])", paragraph.strip())
    return [p for p in parts if re.search(r"[A-Za-z]", p)]


def words_of(s):
    return re.findall(r"[A-Za-z][A-Za-z'-]*", s)


def analyze(raw):
    text = strip_markup(raw)
    paragraphs = [p for p in re.split(r"\n\s*\n", text) if words_of(p)]
    sents = [s for p in paragraphs for s in sentences_of(p)]
    words = [w for s in sents for w in words_of(s)]
    nw, ns = len(words), max(1, len(sents))
    if nw == 0:
        return None
    lens = [len(words_of(s)) for s in sents]
    syl = sum(syllables(w) for w in words)
    lower = " ".join(sents).lower()
    per100 = lambda n: 100.0 * n / nw
    filler_hits = sum(len(re.findall(r"\b" + re.escape(f) + r"\b", lower)) for f in FILLER)
    m = {
        "words": nw,
        "sentences": len(sents),
        "avg_sentence_words": nw / ns,
        "pct_sentences_over_25": 100.0 * sum(l > 25 for l in lens) / ns,
        "longest_sentence": max(lens) if lens else 0,
        "flesch_reading_ease": 206.835 - 1.015 * (nw / ns) - 84.6 * (syl / nw),
        "fk_grade": 0.39 * (nw / ns) + 11.8 * (syl / nw) - 15.59,
        "pct_long_words_3plus_syll": per100(sum(syllables(w) >= 3 for w in words)),
        "passive_per_100_sentences": 100.0 * len(PASSIVE_RE.findall(" ".join(sents))) / ns,
        "nominalizations_per_100w": per100(len(NOMINAL_RE.findall(lower))),
        "filler_per_100w": per100(filler_hits),
        "you_i_we_per_100w": per100(len(PERSON_RE.findall(lower))),
        "contractions_per_100w": per100(len(CONTRACTION_RE.findall(lower))),
        "avg_paragraph_sentences": len(sents) / max(1, len(paragraphs)),
    }
    return m


# (metric, low, high): target band for casual technical blog prose.
TARGETS = [
    ("avg_sentence_words", 8, 20),
    ("pct_sentences_over_25", 0, 15),
    ("flesch_reading_ease", 50, 1000),
    ("fk_grade", -100, 10),
    ("pct_long_words_3plus_syll", 0, 15),
    ("passive_per_100_sentences", 0, 10),
    ("nominalizations_per_100w", 0, 3),
    ("filler_per_100w", 0, 1.5),
    ("you_i_we_per_100w", 1.5, 100),
    ("contractions_per_100w", 0.3, 100),
    ("avg_paragraph_sentences", 1, 5),
]


def report(path, m):
    print(f"\n== {path}  ({m['words']} words, {m['sentences']} sentences, longest {m['longest_sentence']})")
    passed = 0
    for key, lo, hi in TARGETS:
        ok = lo <= m[key] <= hi
        passed += ok
        band = f"<= {hi}" if lo <= -100 else (f"{lo}-{hi}" if hi < 100 else f">= {lo}")
        print(f"  {'PASS' if ok else 'FAIL'}  {key:28s} {m[key]:6.1f}   target {band}")
    print(f"  SCORE {passed}/{len(TARGETS)}")
    return passed


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for p in sys.argv[1:]:
        with open(p, encoding="utf-8", errors="replace") as f:
            m = analyze(f.read())
        if m is None:
            print(f"{p}: no prose found")
        else:
            report(p, m)
