# <Project>

<Project> is <what it is, for whom, in one or two sentences>.

## What makes <Project> special

We can't compromise on these.

- **<Value>:** <the commitment, and the trade it refuses>.

## General principles

- Channel your inner DRY, YAGNI, KISS and SOLID.
- Build on the shared layer each area already has. If it can't do what you need, extend it there.
- Write real fixes, not bypasses.
- Keep code in one function unless a part is reused or composable. Extract a helper only when it names a real concept.
- Validate unknown values once, at the boundary that owns them, and pass typed values inward.
- Before adding complexity for a speculative or vanishingly unlikely race or edge case, explain the concrete failure mode, likelihood and complexity cost to the user and get their buy-in.
- If a short request has two possible meanings, ask one question before you start.
- Call a bug fixed only when a test, log or recording shows it.

## How it works

<the map no single file shows>

## Hazards

<optional: traps that hurt the user's machine or the project, each with its safe path>

## Docs

- Agents read the code, so most changes need no doc.
- Record a decision only when it is hard to reverse, surprising without context and the result of a real trade-off. If any of the three is missing, skip it.
- A decision record is one concise paragraph: the context, the decision and why.
- State each fact once, in the doc that owns it. Delete what a change makes stale in the same change.

## Checks

- Test the real implementation instead of copying its logic into the test or mocking it.

## Branches and pull requests

- Use a short branch name of at most three hyphenated words, such as `session-recovery` or `fix-scroll-state`.
- Use conventional commit titles: `type(scope): summary`.
- Make a PR only when asked.

## Code and residue

- Add comments only where the code can't speak for itself.
- Keep plans, research notes and scratch files outside the worktree.
