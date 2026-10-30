## Writing skill

### With

#### What is a skill file?

A skill file is a markdown file named `SKILL.md` that teaches Claude how to do one kind of task. It starts with YAML frontmatter holding a `name` and a `description`. The body is plain instructions, like the writing skill I read for this reply.

Skills load by progressive disclosure. At the start of a session, Claude sees only each skill's name and description. The body loads when a task matches the description, or when you type `/skill-name`. The description therefore has to say when the skill applies, or Claude won't reach for it.

To make one, create a folder with a `SKILL.md` in it. Personal skills go in `~/.claude/skills/<name>/`. Project skills go in `.claude/skills/<name>/`, so they ship with the repo. The folder can also hold scripts and reference files that the body points to. Your writing skill does this with `readcheck.py`.

A skill differs from `CLAUDE.md` in when it loads. `CLAUDE.md` loads in full every session, so it suits rules that always apply. A skill suits a procedure you need only sometimes, and it costs almost no context until it's used. A subagent differs again: it runs in a separate context, while a skill's instructions are read into the current one.

### Without

#### What is a skill file?

A skill file is a Markdown file, named `SKILL.md`, that gives an AI coding agent a reusable set of instructions for one kind of task. It lives in its own folder, and the folder name matches the skill name. This repo has three: `pr/`, `teacher/` and `writing/`.

The agent doesn't carry every instruction in its context all the time. It sees only each skill's name and a one-line description. When a task matches a description, it loads the full file and follows it. This keeps the agent's context small and still lets it pick up detailed, task-specific behavior on demand.

##### Structure

A skill file has two parts.

**Frontmatter** is a short YAML block at the top:

```markdown
---
name: pr
description: Use when user indicates that you should create a pr; ship, mr/merge request etc
---
```

- `name` identifies the skill and matches its folder name.
- `description` tells the agent when to use the skill. It works as the trigger, so write it to say when the skill applies, not only what it does.

**Body** is plain Markdown with the instructions. Anything that helps the agent do the job can go here:

- rules and conventions to follow
- worked examples and code snippets
- a process to walk through
- links to supporting files, such as `reference/SETUP.md`, that the agent reads only when needed

##### Examples from this repo

| Skill | Triggers when | What the file does |
| --- | --- | --- |
| `pr` | The user asks to create a PR or ship a change | Sets rules for branch names, commit titles and PR descriptions. It requires before and after evidence for visual changes, and tells the agent to keep watching the PR until it merges. |
| `teacher` | The user asks to learn something or seems unsure | Sets the agent's teaching stance: guide the learner without holding their hand, ask questions before answering, and have them explain the result back. It also points to per-learner memory files. |
| `writing` | The agent writes text that people will read | Sets how the agent writes prose. |

##### Why use one

- **Consistency.** The agent follows the same conventions every time instead of guessing.
- **Reuse.** You write the instructions once and use them across projects and sessions.
- **Lean context.** Only the skills that matter for the current task get loaded.
- **Easy to edit.** A skill is a text file, so you can review it, version it in git and change it like any other file.

##### Writing a good one

- Write the description as a trigger: "Use when...".
- Keep one skill to one job.
- Say what to do and, where it matters, what not to do.
- Include a short example when a rule is easy to misread.
- Move long reference material into separate files and link to it.
