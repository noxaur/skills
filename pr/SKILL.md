---
name: pr
description: Use when user indicates that you should create a pr; ship, mr/merge request etc
---

Use a short branch name of at most three words, separated by hyphens.
Before creating pull request, merge base branch into your branch. Resolve merge conflicts yourself. Keep intent of both sides and run the project checks.
Do not commit implementation plans, research notes, agent scratch files, images or videos. Keep temporary working material outside the worktree.
Use project's standard. Otherwise write a conventional commit title in plain English: `type(optional scope): description`. Example: `feat(animation): force windows to render faster`.
You are creating the pr in order to explain why and what changes you made in a simple way without getting into implementation details. Explain what the problem was, attach before and after images or videos for visual and motion changes, benchmarks for performance changes etc. Your goal is to make the pr as easily ingestible as possible. short evidence section. End with `In collaboration with {model name} using {harness} for implementation and {model name} using {harness} for verification.`. If the same model was used for implementation and verification, shorten it ... `implementation and verification` ....

Upload images and videos with `gh` `--attach`. Do not commit them. Put the local paths in the table and pass those same paths to `--attach`, so `gh` rewrites them in place.

```markdown
The form accepts a blank password.

| Before                  | After                 |
| ----------------------- | --------------------- |
| ![Before](./before.png) | ![After](./after.png) |
```

```shell
gh pr create --body-file pr.md --attach ./before.png --attach ./after.png
```

`gh pr edit` without `--body` appends the file. Pass the full body when the image belongs in the table.

## Until merged

Watch the pull request until it is merged. Resolve conflicts, fix failing checks and address review comments. Verify each reported bug or review issue before you fix it. Fix only a bug that you verified.
