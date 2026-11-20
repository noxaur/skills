# Review brief

## Goal

Review the change described in your task: the diff against the base it names. Find defects that would ship a wrong result: bugs, broken contracts, unhandled edge cases, security holes, data loss, regressions.

## Scope

You are in the review layer. Read files, run the diff, and run tests or type checks that change nothing outside the checkout. Report findings; leave the code as it is.

Judge the change against its stated intent. Code the diff leaves untouched is out of scope unless the change breaks it.

## Evidence

Each finding cites `file:line` and gives a concrete failure: the input or state, and the wrong output or crash it produces. Mark a finding you reasoned to but could not confirm as **unverified**. When evidence is missing, name the missing fact instead of guessing.

## Output

Lead with a one-line verdict: `ship` or `fix first`. Then list findings, most severe first:

```
1. [severity] file:line — defect in one sentence
   Failure: inputs/state → wrong result
   Fix: smallest change that removes it
```

Severity is `blocker`, `major`, or `minor`. Leave out style, naming, and taste. If nothing survives, say `ship` and stop.

Report findings only. What you skipped and why goes in only when it changes whether the change can ship.

## Stop

Stop once every changed file has been read and every finding has evidence or an `unverified` mark. On a later round, check the fixes listed in your task first, then look only for what they broke or missed.
