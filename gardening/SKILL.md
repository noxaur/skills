---
name: gardening
description: Use for any codebase maintenance task.
---

## The codebase is a garden

Agents grow the code; you tend the environment it grows in. Agents copy what they see, so every pattern in the repo is a seed, and slop spreads faster than weeds. Maintenance means making the right thing easy and leaving no examples of the wrong thing. Judge each change by one question: will the next agent working here do better without being told?

You own the part of the codebase you maintain. Its health is your responsibility, not someone else's backlog. When you see a weed, pull it or flag it. Don't step around it.

## Kill the root, not the weed

A bad change is a symptom. Ask what made it the likely output, usually a misleading doc, a bad example to copy, or a missing check. Fix that cause everywhere, then fix the instance. If an agent wrote it, ask that agent why.

## Fix at the widest layer

An inverted triangle ranks where a fix can live, widest first:

1. **Codebase**: API design, architecture, refactoring. Make the wrong thing impossible to write.
2. **Static analysis**: lints, types, compilers, tests, CI. Make it fail fast with a fix-it message.
3. **Verification**: formal or empirical. Prove or observe that it holds.
4. **Prose**: rules, skills, AGENTS.md. Tell agents and hope they read it.
5. **Human review**: catch it by eye, one change at a time.

Width is how much each layer should carry. Upper layers steer every future change without being read. Lower layers get skimmed, forgotten, and don't scale. Drop a layer only when the one above can't express the fix. What you measure tells agents what you care about, and slow feedback loops stall agents far worse than people, so keep checks fast.

## Weed continuously

Delete what misleads: dead code, stale docs, useless tests, half-finished migrations that leave two patterns to copy. Big cleanups are cheap now, so finish them. Keep each change small and scoped to one cause.
