---
name: pr
description: Use when user indicates that you should create a pr; ship, mr/merge request etc
---

## Pre

Merge target branch into your branch. Resolve merge conflicts yourself. Keep intent of both sides and run the project checks.

## Template

Branch: short name at most three words, separated by hyphens.
Title: project standards, else conventional plain english: `type(optional scope): description`.

```text
Explain the problem in a sentence or two. Then.

<summary>

<evidence> (before/after grid)

<merge danger>

`...{model name} for {role > 1 ? roles : role}.
```

## Summary

Choose the smallest view that keeps the pr clear.

- Show logic or an algorithm as pseudocode.
- Show runtime control flow as a call tree.
- Show UI structure as a component tree, including state and module boundaries that matter.
- Show file responsibility or a broad refactor as a shallow file tree.
- Show component interaction, control flow, or data flow with Mermaid.
- Use diff when the point is what changes and the surrounding shape already exists. Match the diff shape to the topic.

## Evidence

Concrete evidence that this change works.

For visual changes include before and after screenshots, if its motion include video.

## Merge Danger

Describe whether it's a one-way or two-way door 2 and blast danger.
Consider all possibilities. Examples are layout shift, breakages for consumers, mobile responsiveness, etc.

## gh attach media

Upload images and videos with `gh` `--attach`. Do not commit them. Put the local paths in the table and pass those same paths to `--attach`, so `gh` rewrites them in place.

```shell
gh pr create --body-file pr.md --attach ./before.png --attach ./after.png
```

`gh pr edit` without `--body` appends the file. Pass the full body when the image belongs in the table.

## Until merged

Watch the pull request until it is merged. Resolve conflicts, fix failing checks and address review comments. Verify each reported bug or review issue before you fix it. Fix only a bug that you verified and that does not change the pr scope.
