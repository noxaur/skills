---
name: pr
description: Use when user indicates that you should create a pr; ship, mr/merge request etc
---

## Before you open

Merge the target branch into yours. Resolve conflicts yourself, keep the intent of both sides and run the project checks.

One concern per PR. Split unrelated changes into separate PRs, and stack a PR on the branch it depends on.

A non-draft PR claims it is ready to merge. If the work is not ready, open it with `gh pr create --draft`, and run `gh pr ready` once it is.

## Template

Branch: a short name of at most three hyphenated words.
Title: the project's convention, else `type(optional scope): description` in plain English.

Fill every `<placeholder>`. Keep every heading, in this order.

```markdown
<opening>

## Summary

<the smallest view of the change>

## Evidence

<proof that it works>

## Merge danger

<One-way or Two-way> door, <blast radius>.

- <danger>

## Models

- <model> as <role>
```

## Sections

### Opening

No heading. One or two sentences a reader understands without the diff.

- Bug: what breaks, for whom and when, then the fix.

```markdown
CI failed pull requests on wall-clock timing from shared runners: in the last 60 runs every red job came from a time limit, none from a bug. Timing now only warns, and a timeout stops only a hang.
```

- Feature: what the user can now do, and what it looks like.

```markdown
Profile Management now counts down the 30-second profile switch cooldown beside its title, then shows **Ready** in green for 5 seconds.
```

### Summary

Choose the smallest view that keeps the change clear.

- Show logic or an algorithm as pseudocode.
- Show runtime control flow as a call tree.
- Show UI structure as a component tree, including state and module boundaries that matter.
- Show file responsibility or a broad refactor as a shallow file tree.
- Show component interaction, control flow, or data flow with Mermaid.
- Use diff when the point is what changes and the surrounding shape already exists. Match the diff shape to the topic.

### Evidence

Concrete proof that the change works: what ran, what it covers, and the capture or log behind it.

For a visual change, show before and after side by side. For motion, add a video.

```markdown
|       | Before                       | After                       |
| ----- | ---------------------------- | --------------------------- |
| Light | ![before](/tmp/before.png)   | ![after](/tmp/after.png)    |
```

Upload images and videos with `gh` `--attach`, never commit them. Put the local paths in the table and pass the same paths to `--attach`, so `gh` rewrites them in place. Keep the body and media outside the worktree.

```shell
gh pr create --body-file "$TMPDIR/pr.md" --attach "$TMPDIR/before.png" --attach "$TMPDIR/after.png"
```

`gh pr edit` without `--body` appends the file. Pass the full body when the image belongs in the table.

### Merge danger

Open with the door and the blast radius, then one bullet per danger. Consider every consumer: layout shift, breakage for consumers, mobile responsiveness, saved data, settings.

```markdown
Two-way door, small blast radius.

- The Wardrobe timer only moved, with the same pixels (see Evidence).
- `Theme` is an internal enum with no outside consumers.
```

### Models

One line per model that worked on the change: its short name and role, nothing more.

```markdown
- opus 5.5 as implementer
- sol-6.2 as reviewer
```

## Until merged

Watch the pull request until it is merged. Keep it up to date: whenever the target branch (usually main) moves, merge it into your branch and run the checks again. Resolve conflicts, fix failing checks and address review comments. Verify each reported bug or review issue before you fix it. Fix only a bug that you verified and that does not change the pr scope.
