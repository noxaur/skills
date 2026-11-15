---
name: reviewer
description: Use before opening a PR for any change, including config, docs and skills.
---

Use the model specificied by the user as a reviewer model in a loop, default to codex sol 6.1 high.
Ask sol to relentlessly review your implementation and take in the feedback.
Be critical to the feedback sol gives, it should be verified before attempting a fix.
The loop can not be longer then 3 times.
Do not address nitpicks and stop if you only get nitpicks.
Don't scope creep.

## Briefing the reviewer

Start the reviewer with T3 `delegate_task`. Each model below has a brief written for how it reads prompts. Pass the brief's absolute path in the task and tell the reviewer to read it before anything else.

| Model | Target | Brief |
| --- | --- | --- |
| GPT-6.1 Sol (Codex) | `gpt-6.1-sol`, effort high | [`briefs/gpt-6.1-sol.md`](briefs/gpt-6.1-sol.md) |
| Grok 4.7 (Cursor) | `grok-4.7`, effort high | [`briefs/grok-4.7.md`](briefs/grok-4.7.md) |

The brief carries the review rules. The task itself only adds:

- the base branch or commit range to diff against
- one line on what the change is meant to do
- on rounds 2 and 3, the findings you fixed and the ones you rejected, with your reason

For a model with no brief, send the Sol brief.
