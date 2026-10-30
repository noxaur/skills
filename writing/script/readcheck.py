#!/usr/bin/env python3
"""readcheck: measurable checks for casual, readable prose (blog style).

Usage: python3 readcheck.py FILE [FILE ...]   (plain text or markdown)
       python3 readcheck.py --quick FILE|-      (stock phrases + revision questions only)

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


STOCK_PHRASES = [
    (r"\bgets? (?:its|their) own\b", '"gets its own": say what the thing is and where it lives'),
    (r"\b(?:lives?|sits?|runs?|works?) in (?:its|their) own\b", '"lives in its own": say what the thing is and where it lives'),
    (r"\byou stop\b", 'pitch: "you stop ...". Explain the mechanism instead'),
    (r"\bonce\b[^.]*\bevery time\b", 'pitch: "once ... every time". Explain the mechanism instead'),
    (r"\bwith no \w+ and no\b", 'pitch: "with no X and no Y"'),
    (r"\band never\b", 'pitch: "and never Z"'),
]

QUESTIONS = """Revise before sending. Answer each question against your draft:
  1. Which sentences explain how something works? For each, what do the official docs or a
     textbook call that idea? If it has a name, lead with it: "It's <term>: <one-line why>".
  2. Which sentences only restate a benefit? Cut them.
  3. Did you cover how to create or run it, where it's stored, and how it differs from similar tools?"""


def stock_hits(raw):
    hits = []
    for n, line in enumerate(raw.splitlines(), 1):
        for pat, msg in STOCK_PHRASES:
            for mt in re.finditer(pat, line, re.I):
                hits.append(f"  line {n}: {msg}  [{mt.group(0)}]")
    return hits


def quick(path, raw):
    hits = stock_hits(raw)
    print(f"== {path}: {len(hits)} stock phrase(s)")
    print("\n".join(hits) if hits else "  none")
    print(QUESTIONS)


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
    if sys.argv[1] == "--quick":
        for p in sys.argv[2:] or ["-"]:
            raw = sys.stdin.read() if p == "-" else open(p, encoding="utf-8", errors="replace").read()
            quick(p, raw)
        sys.exit(0)
    for p in sys.argv[1:]:
        with open(p, encoding="utf-8", errors="replace") as f:
            raw = f.read()
        m = analyze(raw)
        for h in stock_hits(raw):
            print(h)
        if m is None:
            print(f"{p}: no prose found")
        else:
            report(p, m)
