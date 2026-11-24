# Vision

Write the identity line and `## What makes <Project> special` at the top of AGENTS.md: an acceptance policy grounded in what the repo actually builds, sharpened by hypotheticals the user answers on a review board.

The section is the only committed alignment surface. A reviewer who never saw the board must be able to accept or resist a change from it alone.

## Host requirement

- Read merged PR history with `gh`. If PRs are not accessible, read `git log` on the default branch. With no history yet, read the repo's files and ask the user what the project refuses to become.
- If none of these gives evidence, **stop** and say so. A vision built on invented evidence is worse than none.
- The review loop runs on lavish-axi through `npx -y lavish-axi`. Launch it; report a blocker only if the launch fails.

## Hard rules

1. **Evidence over vibes.** Every value traces to named PRs, commits, files or reasoning the user approved. Generic virtues ("we value quality") are banned unless the history shows them specifically.
2. **The user owns the vision.** Draft, stress-test, fold in their verdicts. Never approve, never soften a hypothetical, never add a value they did not state or show.
3. **An acceptance policy.** Each value is a testable commitment that refuses a trade. When two values collide, name the winner.
4. **No softball hypotheticals.** Each sits on a fault line where yes and no are both defensible, both sides steelmanned. If you can predict the answer, replace it.
5. **The board ships as-is.** Build it with `build-board.mjs`: black ink on white paper set like literature, the full draft always visible on the left, one hypothetical at a time in a card stack on the right, the steelman in full view, one queued verdict per card. Never restyle, restructure or substitute another surface.
6. **Trace every edit.** Each verdict maps to a named edit in a changelog, so the user sees how their answer changed the text.
7. **Light.** Two to four values, one line each; the section fits on one screen. A value names a refusal, not how the product behaves: where a window shows or how settings open belongs in How it works, if anywhere. No roadmap, feature list or marketing voice. Plain hyphens, never em dashes.
8. **Nothing else.** Never commit hypotheticals, board transcripts or an answers file. Every byte of AGENTS.md outside the section stays unchanged.

## Pipeline

### 1. Mine the evidence

- README identity claims, architecture, stated non-goals, refusal paths, test discipline.
- 30-100 merged PR titles (`gh pr list --state merged --limit 100`), 8-15 full bodies spread across the range. Fall back to `git log`.
- Extract revealed values: what gets built, what gets refused, what class of bug gets fixed at the root.
- Keep a private evidence sheet: value -> PRs, commits or files. It is the source of truth for every drafted line.

### 2. Draft

Follow the output template. Every line maps to the evidence sheet.

### 3. Design the hypotheticals

5-8 concrete change proposals aimed at the draft's fault lines:

- tempting off-mission features the user will plausibly be asked for;
- value collisions (simplicity vs capability, speed vs safety, focus vs generality);
- slippery slopes, where one reasonable step normalizes the next;
- scope expansions (new users, platforms, content types);
- identity questions the draft leaves open.

Per hypothetical: id, title, the proposal (2-4 sentences), the value it tests (quoted from the draft), and why the answer is not obvious (both sides steelmanned).

### 4. Review loop

- Write the round as `round.json` (`project`, `runNote`, `draft`, `cards`) in a scratch directory that survives a restart (not `/tmp`), never the target repo. Run `node build-board.mjs round.json <dir>` (the script sits next to this file); it fills the template, escapes the text and fails on a broken slot.
- Launch `npx -y lavish-axi <board.html>`, report the URL, then wait on `npx -y lavish-axi poll <board.html>`. Verdicts arrive queued.
- Per batch: read each verdict's notes, not just its label. Fold the reasoning in by sharpening the value it tests, never by appending detail; if the value only grows, rewrite it shorter. Keep the hypothetical, card id and transcript out of the draft.
- When a note contradicts its label or opens a new question, ask it back as a new card instead of guessing.
- Rebuild the board into the same directory with the new draft and remaining cards, so the session URL stays. Reply through `poll --agent-reply` with one changelog line per verdict ("H-3 off mission -> Fast now names the winner over Simple").
- Continue until the user approves or ends the session. Silence is not approval.

### 5. Write

Write the approved text at the top of AGENTS.md. If the vision now runs ahead of the code, leave How it works describing the code and tell the user where the two differ.

## Output template

```markdown
# <Project>

<Project> is <what it is, for whom, in one or two sentences>.

## What makes <Project> special

We can't compromise on these.

- **<Value>:** <the commitment, and the trade it refuses>.
```

## Before approval

- [ ] Every line traces to the evidence sheet or approved reasoning
- [ ] 5-8 hypotheticals, none predictable, both sides steelmanned
- [ ] Every verdict is reflected in the draft, with a changelog line
- [ ] The section alone settles an accept/resist call
- [ ] Two to four values, one line each, one screen
