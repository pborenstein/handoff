# handoff

A Claude Code plugin for token-efficient project tracking across sessions. It keeps a small set of files in `docs/` so a new session can resume work by reading about 50 lines instead of the whole history.

## Skills

| Skill | Purpose |
|:------|:--------|
| `handoff:project-tracking` | Create the `docs/` tracking structure in a project |
| `handoff:project-repo` | Initialize a meta-repo that coordinates related projects, each with its own git history |
| `handoff:session-pickup` | Read context from the previous session before new work |
| `handoff:session-wrapup` | Update tracking docs and commit at the end of a session |
| `handoff:scannable-docs` | Format specs, schemas, READMEs, and reference notes for scanning; includes a checker script |

## Installation

If you've cloned the repository to a directory of your choice, run Claude Code with `--plugin-dir` pointing to it:

```bash
claude --plugin-dir /path/to/handoff/
```

Or clone the repository to a standard location and add it to your Claude Code plugins:

```bash
git clone https://github.com/pborenstein/handoff.git ~/.claude/plugins/handoff
```

Or add it as a dependency in your project's `.claude/settings.json`:

```json
{
  "plugins": ["~/.claude/plugins/handoff"]
}
```

## Usage

### Set up tracking in a project

```
/handoff:project-tracking
```

Creates the four files described in [Tracking files](#tracking-files).

### Set up tracking for a collection of projects

```
/handoff:project-repo
```

Use this for a directory of related projects, each with its own independent git history. It creates a meta-repo at the parent level that tracks shared docs and conventions without coupling the member repos: no submodules, no monorepo merge.

The meta-repo:

- gitignores all member subdirectories
- creates `CLAUDE.md` describing the collection and its members
- creates the same `docs/` tracking structure as `project-tracking`

After that, use `session-pickup` and `session-wrapup` as usual.

### Start a session

```
/handoff:session-pickup
```

First fetches and compares local `HEAD` to its upstream, and warns if the checkout is behind or diverged. Then reads `docs/CONTEXT.md`, falling back to `docs/IMPLEMENTATION.md` if CONTEXT.md is missing or stale.

### End a session

```
/handoff:session-wrapup
```

1. Update CONTEXT.md with the current focus and tasks.
2. Update task checkboxes in IMPLEMENTATION.md.
3. Add a chronicle entry, if the session did significant work.
4. Add to DECISIONS.md, if architectural decisions were made.
5. Commit the documentation changes.

Both pickup and wrapup stop if neither `docs/CONTEXT.md` nor `docs/IMPLEMENTATION.md` exists, and point you to `project-tracking` or `project-repo`.

### Format a document for scanning

```
/handoff:scannable-docs
```

Restyles or writes technical and reference docs: tables for data, lists for discrete items, short paragraphs, top-down diagrams. The bundled checker reports formatting problems without editing the file:

```bash
python3 skills/scannable-docs/scripts/scannable_check.py path/to/doc.md
```

## Tracking files

Hot state, read every session, is kept separate from cold history, read on demand. A new session should be able to start in under 2 minutes by reading only CONTEXT.md.

| File | Question it answers | Shape |
|:-----|:--------------------|:------|
| `docs/CONTEXT.md` | Where did I leave off? | 30-50 lines, rewritten each session |
| `docs/IMPLEMENTATION.md` | What are we doing? | Current phase in detail, completed phases compressed; 400-600 lines |
| `docs/DECISIONS.md` | What did we decide? | Heading-based entries, grep-friendly, single source of truth |
| `docs/chronicles/phase-X.md` | What happened? | Slim 15-20 line entries, one per session |

See [PROJECT-TRACKING-REFERENCE.md](skills/project-tracking/references/PROJECT-TRACKING-REFERENCE.md) for the complete guide.

## License

MIT License. See [LICENSE](LICENSE).
