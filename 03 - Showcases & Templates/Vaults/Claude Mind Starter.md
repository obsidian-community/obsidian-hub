---
aliases: 
- 
tags:
- seedling
publish: true
---

# Claude Mind Starter

A starter vault for using Obsidian as a persistent memory for Claude. Most starter kits give you folders; this one gives you a protocol — a `CLAUDE.md` that tells Claude how to read the vault, where to write tasks and open loops, and how to close out a session so the next one starts from context instead of from scratch.

Useful if you work with an AI assistant that can read and write local files (Claude Code, or Claude Desktop with a connected folder) and you are tired of re-explaining your projects every session.

Where to start: open the vault, then ask Claude to "read CLAUDE.md and tell me what I'm working on." At the end of a session, say "update your mind" — Claude closes out finished tasks, archives them, and records what changed.

What's in it:

- `CLAUDE.md` — the instruction file. This is the actual content of the kit; the folders exist to serve it.
- `HOME.md` and `START HERE.md` — entry points.
- `Tasks/` — `TASKS.md` (active work), `Open Loops.md` (what you are waiting on, date-stamped), `Someday.md` (parked ideas), each with the conventions the protocol expects.
- `Notes/` and `Archive/` — left empty on purpose.

No plugins are required, and there is no custom CSS or theme. It is plain markdown with `[[wikilinks]]`, so it also works fine outside Obsidian.

## Download 

Link: https://github.com/Adam13y/claude-mind-starter-lite

Free and MIT-licensed. Clone or download the repo and open the folder as a vault.
