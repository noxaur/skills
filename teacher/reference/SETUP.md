# Setup: learn about the learner

Run once per learner, or when memory is missing or stale. Ask few questions, one at a time. Skip anything memory already answers.

## Ask

1. Goal: what do you want to build or be able to do?
2. Level: what have you built or used before?
3. Style: do you start with a video, with theory, or by building?
4. World: what do you know well (sport, music, game)? Use it for analogies.
5. Pace: how much help do you want when stuck: hints only, or direct answers?

## Save

One file per learner at `~/.claude/teacher/learners/<name>.md`. This path is outside any project and worktree, so deleting a worktree does not delete it. Create the directory if it is missing. Never save it in the repo or in a worktree.

Do not put secrets in it. Keep to learning facts.

Keep these fields, one line each:
- Goal
- Level
- Style
- World (for analogies)
- Help level
- Known gaps (from explain tests)
- Misreadings (claims that did not match their code)

## Keep current

- After each explain test, update Known gaps.
- When you fight back on a claim, add it to Misreadings.
- Edit the existing file. Do not create duplicates.
- Read the file at the start of each session.
