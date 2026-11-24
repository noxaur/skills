---
name: agents-md
description: Use when a repo has no AGENTS.md or CLAUDE.md, or only a bare one.
---

Start from [reference/AGENTS.md](reference/AGENTS.md). Keep its general lines and fill every `<placeholder>` from the repo.

Write the vision first with [reference/vision/vision.md](reference/vision/vision.md). It decides what the rest of the file defends. While the board waits on the user, draft the other sections.

## Sections

Skip all preambles and keep prose brief. Use the repo's domain words. Write only what reading the code can't teach: the reason, the trap, the taste.

### How it works

Pick the smallest view.

- One project: a dense paragraph naming the core loop, who owns state and where the boundaries sit.

```markdown
The engine has no GUI; the app wraps it and draws. One object owns all state. Every event triggers one refresh, which reconciles the window list, asks the layout for slots and animates windows into them.
```

- Several areas: a table pointing to what to read before changing each.

```markdown
| Directory  | What it is                  | Read first                  |
| ---------- | --------------------------- | --------------------------- |
| `mod/`     | The client mod, in Kotlin   | `mod/AGENTS.md`             |
| `backend/` | The REST service, in Effect | `docs/internals/backend.md` |
```

### Hazards

Traps no check can catch: killing the wrong process, writing to live data, baking in config. Name the trap, then the safe path.

```markdown
1. **Writing to the live install.** `~/.app/data` is the user's real database, in use while you work. Read or copy from it; never open it read-write.
```

### Checks

Only what looking can't find, such as where tests must run from or which suite CI owns. The commands themselves live in the repo.

## Examples

AGENTS.md in `pingdotgg/t3code`, `noxaur/catwm`, `noxaur/ds-mod` and `anomalyco/opencode`.
