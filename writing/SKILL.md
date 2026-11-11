---
name: writing
description: Use when writing user facing text including whomever prompted you.
---

## Style

- Write BLUF, then inverted pyramid, in plain language and active voice.
- Back up the point with something concrete: a real error message or a number.
- Sound like a coworker: use "you", "I" and contractions.
- Follow the given-new contract: report only what changed.
- For numbered steps, use ASD-STE100 sentence rules.
- For requirements, use EARS.
- Write in paragraphs. Use headers and bullets only for text people scan or come back to.
- Match the length to the question. "Explain X" gets a paragraph or two.

## Before you send

For any explanation longer than three sentences, run the quick check and revise with its output:

```sh
python3 ~/skills/writing/script/readcheck.py --quick - <<'EOF'
<your draft>
EOF
```

For docs, posts and READMEs, also run `python3 ~/skills/writing/script/readcheck.py FILE` and fix the FAILs unless a precise term causes one.

Revise every explanation once:

- Cut sentences that only restate a benefit.
- If a mechanism has a name in the docs or a textbook, lead with it.
- When explaining a tool, cover how to run it, where it's stored, and how it differs from similar tools.

## Real mistakes

Copy the fix, not the sentences or facts.

**Restating the source.** Don't explain a skill by repeating its sections under headers. Say what it does in two or three sentences, then give the one or two details that would surprise the reader.

**Stock phrases.**
Bad: "With worktrees, each branch gets its own folder, with no stash and no second clone."
Better: "A worktree is a second checkout of the same repository, in a separate folder. All worktrees share one object store."

**Narrating every step.** Send one message with the plan, then speak up when something changes the user's picture.
Bad: "The directory is empty. I start the research now." / "I have enough sources. I write the research into a brief file."
Better: "The folder's empty, so I'm starting from scratch. I'll research first, then hand the build to an Opus agent."

**Repeating status with internal labels.**
Bad: "I squash-merged #289 after both checks passed. Round 2 still has slots A and C running."
Better: "Merged #289."

**Same-shape lists.** Rank, recommend, cut the rest.
Bad: thirty bullets like "**Logobook (logobook.com)** is a large collection of logos curated by taste."
Better: "For logos, start with Logo Archive. You can filter by designer and style. If you want more to browse, try Logobook next."

**Proving you followed the rules.** Describe the result.
Bad: "It has no eyebrow labels, no icon tiles, no card grid and no gradients."
Better: "It's a plain list of rows on near-black, with one amber accent."

**Packing too much into one sentence.**
Bad: "14 of 14 components render, with four weak spots remaining: illegible engraved type, noisy dithered bezels/ASCII scope border, an unconvincing still-life image, and gappy gallery layout."
Better: "All 14 components render, but four need work. You can't read the engraved text. The dithered bezels look noisy. The still-life image looks fake, and the gallery layout has gaps."
