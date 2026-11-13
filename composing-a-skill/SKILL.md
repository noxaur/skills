---
name: composing-a-skill
description: Use when asked to work on a agent skill.
---

## Description

Only explain when an agent should use the skill, refrain from explaining what the skill is. Keep this step short.

## Goal

The goal of creating a skill is explain a concept to an forgetfull but widely intellegent person. This person understands the a ton of concepts and you need to activate that knowledge. Explain concepts shortly and concisely.

### Good:

---

## What a good test is

Tests verify behavior through public interfaces, not implementation details. Code can change entirely; tests shouldn't. A good test reads like a specification: "user can checkout with valid cart" tells you exactly what capability exists, and it survives refactors because it doesn't care about internal structure.

---

### Bad

---

## Overview

A test exists to catch a specific break. Two principles govern everything
here:

```

1. Every test names the break it catches
2. Every test exercises the real thing

```

## Principle 1: Name the Break

Before writing the test body, answer: **what production change should
make this test fail — and is that change a bug or a decision?** A test
earns its place by catching a wrong branch, missing side effect, wrong
argument, boundary case, or broken contract.

**Derive expectations independently.** Use literals and hand-checked
fixtures; table-driven tests with literal `want` values are the preferred
shape. An expectation computed by the code under test — or its helpers —
passes no matter what that code does:

```typescript
// ❌ Mirror assertion: the same builder computes both sides — always true
const expected = buildSearchQuery({ tag: "urgent" });
expect(buildSearchQuery({ tag: "urgent" })).toBe(expected);

// ✅ Hand-derived literal
expect(buildSearchQuery({ tag: "urgent" })).toBe('tag:"urgent"');
```

**No change detectors.** If only intentional decisions can fail a test —
a constant's value, exact message wording, private structure — it fires
on redesign and sleeps through bugs.

[...]

---
