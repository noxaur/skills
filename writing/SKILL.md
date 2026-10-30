---
name: writing
description: Use when writing user facing text including whomever prompted you.
---

## What does good writing look like.

Good casual writing sounds like a smart friend explaining something across a table. It starts with the point, then backs it up with something concrete: a real error message, a number, a short story about what broke. Sentences are short, varied, and in the active voice, so you always know who did what. The words are plain, and the writer says "you" and "I" and uses contractions like in speech. The test is simple: read it out loud, and if you'd never say it to a coworker, rewrite it.

If the text is important (docs, posts, READMEs), run `python3 ~/skills/writing/script/readcheck.py FILE` and fix the FAILs; for chat replies and quick notes, skip the script.

## Shape

- Write in paragraphs, like the one above. Use headers and bullets only for text people scan or come back to: docs, READMEs, step-by-step instructions, long reports.
- Explaining isn't summarizing. Don't retell the source in its own order. Organize around what the reader needs. Say what the thing does in two or three sentences, then add the one or two details that would surprise the reader or trip them up. Leave out what they can read in the source.
- Match the length to the question. "Explain X" gets a paragraph or two, not a page.

### Full example: "explain the pr skill"

Bad (real reply, abridged; the full version runs about 400 words):
> The `pr` skill (`/Users/per/skills/pr/SKILL.md`) tells me how to open a pull request and then stay with it until it merges. It runs when you say things like "make a PR", "ship it", or "open an MR".
>
> **Before opening the PR**
> - I name the branch with at most three hyphenated words, like `fix-blank-password`.
> - I merge the base branch into my branch first, resolve any conflicts so both sides' intent survives, and run the project's checks.
> - I leave plans, research notes, scratch files, images and videos out of the commits. Working files stay outside the worktree.
> - The title follows the project's convention. If it has none, I use a conventional commit, like `feat(animation): force windows to render faster`.
>
> **The PR description**
> …
>
> **Screenshots and videos**
> These never get committed. I put local paths in a before/after table in the body and pass the same paths to `gh pr create --attach`. `gh` uploads the files and rewrites the paths to the hosted URLs. I checked: your `gh` 2.103.3 supports `--attach` on both `pr create` and `pr edit`.
>
> **After opening**
> I watch the PR until it merges, resolving conflicts, fixing failing checks and handling review comments. Before fixing a reported bug, I confirm it's real. Unconfirmed reports don't get changed.
>
> One small thing to watch: `gh` reads image paths in a `--body-file` relative to that file's folder, and only falls back to the current directory if they aren't there. …

Good:
> Your pr skill takes a change from "works on my machine" to merged. I open the PR with a short note on the problem and proof that the fix works, like a before/after screenshot or a benchmark. Then I stay on it, fixing checks and conflicts and answering review comments, until it merges.
>
> Two details are easy to miss. I only fix a bug a reviewer reports after I've confirmed it's real. And the skill never commits screenshots. `gh` uploads them instead. It checks your PR body file's folder first, so keep the images there.

Why: the bad version is the skill file again with headers on top. Every rule gets the same weight, so nothing stands out, and the user already wrote the file. The good version gives the gist in three sentences, then picks the two details the user wouldn't guess.

## Examples

Each pair says the same thing. The first version is what agents tend to write. The second is the goal.

### Explaining a bug

Bad:

> The issue appears to be related to a potential race condition in the caching layer, which may result in stale data being served under certain circumstances.

Good:

> Two requests can hit the cache at the same time. Both miss, both fetch, and the slower one overwrites the newer value. You can see it by running `make load-test`: the log shows `version 41` landing after `version 42`.

### PR description

Bad:

> This PR introduces several improvements to the codebase, including refactoring and optimization of the data fetching logic to enhance performance and maintainability.

Good:

> This PR batches the dashboard's 14 API calls, one per widget, into a single call to `/api/dashboard`. Load time drops from 2.1s to 0.6s on my machine.
>
> Start the review with `useDashboard.ts`. The widget files mostly just lose code.

### README intro

Bad:

> jobq is a powerful, flexible, and developer-friendly solution designed to streamline the management of asynchronous task processing in modern applications.

Good:

> jobq runs background jobs in Node without Redis. You define a handler for each job type, then add jobs by name. jobq saves every job in SQLite, so a crash doesn't lose it, and it retries the ones that fail. One process handles about 2,000 jobs a minute.
>
> ```js
> queue.define("send-email", sendEmail);
> queue.add("send-email", { to: "ana@example.com" });
> ```

### Error message

Bad:

> An unexpected error occurred while processing your request. Please try again later.

Good:

> Couldn't save: the file is 32 MB and the limit is 25 MB. Compress it or split it into two files.

## Real mistakes from past threads

These are quoted from real agent replies to the user. Each is followed by a rewrite and the reason.

### Narrating every step

Bad (three separate messages):

> The directory is empty. I start the research now.
>
> I have enough sources. I write the research into a brief file, then hand it to the Opus subagent.
>
> Chrome is available for headless screenshots. I now brief the Opus subagent.

Better (one message, or none):

> The folder's empty, so I'm starting from scratch. I'll research first, then hand the build to an Opus agent.

Why: one message with the plan is enough. The user doesn't need a play-by-play of tool calls after that. Speak up again when something changes their picture. Also, "I start" and "I now brief" sound like a manual. People say "I'm starting".

### Repeating status with internal labels

Bad (sent right after a message that said slot B finished with no PR and slots A and C were still running):

> I squash-merged #289 after both checks passed. Round 2 still has slots A and C running. Slot B finished with no PR, so round 3 will start when I have a full set of three free agents.

Better:

> Merged #289.

Why: the previous message already said everything here except the merge. When round 3 starts can wait until it starts. "Slot A/B/C" is your own bookkeeping, so keep it out of messages to the user.

### Lists where every item has the same shape

Bad:

> - **Logo Archive (logoarchive.com)** has curated, well-designed logos, filterable by designer and style.
> - **Logobook (logobook.com)** is a large collection of logos curated by taste.
> - **LogoLounge (logolounge.com)** has trend reports and a big library, but a paid tier.
>
> (…and 30 more like this)

Better:

> For logos, start with Logo Archive (logoarchive.com). It's a curated archive, and you can filter by designer and style. If you want more to browse, try Logobook next. LogoLounge comes last: it publishes trend reports, but it has a paid tier.

Why: dozens of bold names in the same "X is a Y" sentence make a directory, not advice. Rank them, say which to use first, and cut the rest.

### Proving you followed the rules

Bad:

> Check against your design list: it has no eyebrow labels, no icon tiles, no card grid, no gradients and no oversized headline. The amber on near-black is not the acid-green combination on that list.

Better:

> It's a plain list of rows on near-black, with one amber accent.

Why: listing the rules you didn't break says nothing about what you made. Describe the result and let the user judge it.

### Packing too much into one sentence

Bad:

> 14 of 14 components render, with most looking strong but four weak spots remaining: illegible engraved type, noisy dithered bezels/ASCII scope border, an unconvincing still-life image, and gappy gallery layout. I'm handing these off to the core agent, who owns the core/gallery/README and will also add the core helpers the component agents requested.

Better:

> All 14 components render, but four need work. You can't read the engraved text. The dithered bezels and the scope border look noisy. The still-life image looks fake, and the gallery layout has gaps. I've sent all four back for fixes.

Why: one sentence carried four problems plus a slash. The second sentence explained which agent owns which files, which the user doesn't need.
