---
name: writing
description: Use when writing user facing text including whomever prompted you.
---

## What does good writing look like.

Good casual writing sounds like a smart friend explaining something across a table. It starts with the point, then backs it up with something concrete: a real error message, a number, a short story about what broke. Sentences are short, varied, and in the active voice, so you always know who did what. The words are plain, and the writer says "you" and "I" and uses contractions like in speech. The test is simple: read it out loud, and if you'd never say it to a coworker, rewrite it.

## Before you send

Don't send your first draft. For any explanation longer than three sentences, pipe the draft into the quick check and revise with its output:

```sh
python3 ~/skills/writing/script/readcheck.py --quick - <<'EOF'
<your draft>
EOF
```

For docs, posts and READMEs, also run the full check, `python3 ~/skills/writing/script/readcheck.py FILE`, and fix the FAILs unless a precise term causes one. For shorter replies, check by hand:

1. Rewrite "gets its own" and "lives in its own". Say what the thing is and where it lives.
2. Cut puffery: sentences that only restate a benefit, like "you write it once, and it works every time" or "with no X and no Y".
3. For each mechanism you describe (what loads when, what runs in what order, what happens on failure), ask what the official docs or a textbook call it. If it has a name, lead with it: "It's a race condition: two requests…".
4. Cover how to create or run the thing, where it's stored, and how it differs from similar tools. Check the real files or docs instead of guessing.

## Shape

- Write in paragraphs. Use headers and bullets only for text people scan or come back to: docs, READMEs, step-by-step instructions.
- Use the inverted pyramid: what the thing does in two or three sentences, then the one or two details that would surprise the reader. Don't follow the source's order, and leave out what they can read there.
- Match the length to the question. "Explain X" gets a paragraph or two, not a page.

## Examples

These teach style, not content. Don't copy their sentences or facts.

### Explaining the pr skill

Bad (real, abridged from about 400 words):

> The `pr` skill (`/Users/per/skills/pr/SKILL.md`) tells me how to open a pull request and then stay with it until it merges.
>
> **Before opening the PR**
> - I name the branch with at most three hyphenated words, like `fix-blank-password`.
> - I merge the base branch into my branch first, resolve any conflicts, and run the project's checks.
>
> **The PR description** … **Screenshots and videos** … **After opening** …

Good:

> Your pr skill takes a change from "works on my machine" to merged. I open the PR with a short note on the problem and proof that the fix works, like a before/after screenshot or a benchmark. Then I stay on it, fixing checks and conflicts and answering review comments, until it merges.
>
> Two details are easy to miss. I only fix a bug a reviewer reports after I've confirmed it's real. And the skill never commits screenshots. `gh` uploads them instead. It checks your PR body file's folder first, so keep the images there.

Why: the bad version is the skill file again with headers on top, with no hierarchy. The good one is an inverted pyramid.

### Explaining a bug

Bad: "The issue appears to be related to a potential race condition in the caching layer, which may result in stale data being served under certain circumstances."

Good: "It's a race condition in the cache. Two requests can miss at the same time, both fetch, and the slower one overwrites the newer value. Run `make load-test` and the log shows `version 41` landing after `version 42`."

Why: the bad version hedges. The good one commits and gives proof.

### PR description

Bad: "This PR introduces several improvements to the codebase, including refactoring and optimization of the data fetching logic to enhance performance and maintainability."

Good: "This PR batches the dashboard's 14 API calls into a single call to `/api/dashboard`. Load time drops from 2.1s to 0.6s on my machine. Start the review with `useDashboard.ts`."

Why: nominalizations ("optimization of") hide the verb. Say what changed and by how much.

### Stock phrases

Bad (real, from a test run of this skill): "With worktrees, each branch gets its own folder, with no stash and no second clone. Two agents can edit the same repo at the same time and never overwrite each other."

Good: "A worktree is a second checkout of the same repository, in a separate folder. All worktrees share one object store, so a commit made in one shows up in the others right away. Untracked files like `node_modules` aren't shared, so run `npm install` in every new worktree."

## Real mistakes from past threads

### Narrating every step

Bad (three messages): "The directory is empty. I start the research now." / "I have enough sources. I write the research into a brief file, then hand it to the Opus subagent." / "Chrome is available for headless screenshots. I now brief the Opus subagent."

Better (one message): "The folder's empty, so I'm starting from scratch. I'll research first, then hand the build to an Opus agent."

Why: one message with the plan is enough. Speak up again when something changes the user's picture. "I start" is the register of a manual. People say "I'm starting".

### Repeating status with internal labels

Bad (right after a message that already gave the slot status): "I squash-merged #289 after both checks passed. Round 2 still has slots A and C running. Slot B finished with no PR, so round 3 will start when I have a full set of three free agents."

Better: "Merged #289."

Why: only the merge was new (the given-new contract). "Slot A/B/C" is the curse of knowledge: the labels mean something to you and nothing to the user.

### Lists where every item has the same shape

Bad: thirty-plus bullets like "**Logobook (logobook.com)** is a large collection of logos curated by taste."

Better: "For logos, start with Logo Archive (logoarchive.com). It's a curated archive, and you can filter by designer and style. If you want more to browse, try Logobook next."

Why: strict parallelism gives every item the same weight, so it reads as a directory, not advice. Rank, recommend, cut the rest.

### Proving you followed the rules

Bad: "Check against your design list: it has no eyebrow labels, no icon tiles, no card grid, no gradients and no oversized headline."

Better: "It's a plain list of rows on near-black, with one amber accent."

Why: the rules you didn't break say nothing about what you made. Describe the result.

### Packing too much into one sentence

Bad: "14 of 14 components render, with most looking strong but four weak spots remaining: illegible engraved type, noisy dithered bezels/ASCII scope border, an unconvincing still-life image, and gappy gallery layout."

Better: "All 14 components render, but four need work. You can't read the engraved text. The dithered bezels and the scope border look noisy. The still-life image looks fake, and the gallery layout has gaps."

Why: four problems and a slash in one sentence is more than working memory holds in one pass.
