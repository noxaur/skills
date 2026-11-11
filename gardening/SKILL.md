---
name: gardening
description: Use for any codebase maintenance task.
---

## The codebase is a garden

Agents grow the code; you tend the environment it grows in. Agents copy what they see, so every pattern in the repo is a seed, and slop spreads faster than weeds. Maintenance means making the right thing easy and leaving no examples of the wrong thing. Judge each change by one question: will the next agent working here do better without being told?

You own the part of the codebase you maintain. Its health is your responsibility, not someone else's backlog. When you see a weed, pull it or flag it. Don't step around it.

## Kill the root, not the weed

A bad change is a symptom. Ask what made it the likely output, usually a misleading doc, a bad example to copy, or a missing check. Fix that cause everywhere, then fix the instance. If an agent wrote it, ask that agent why.

## Stakes over instructions

Guidance gets skimmed. A fast, deterministic check that fails with a fix-it message steers every future change, and what you measure tells agents what you care about. Speed is part of the garden too: slow feedback loops stall agents far worse than people.

## Weed continuously

Delete what misleads: dead code, stale docs, useless tests, half-finished migrations that leave two patterns to copy. Big cleanups are cheap now, so finish them. Keep each change small and scoped to one cause.
