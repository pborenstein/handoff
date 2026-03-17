# handoff

A Claude Code plugin for token-efficient project tracking across sessions.

## Skills Included

- `handoff:project-tracking` - Establish the documentation structure for tracking project progress
- `handoff:session-pickup` - Read context from the previous session to prepare for new work
- `handoff:session-wrapup` - Update project documentation and commit changes after a session

## Installation

If you've cloned the repository to a directory of your choice, run Claude Code with `--plugin-dir` pointing to it:

```bash
claude --plugin-dir /path/to/handoff/
```

Or clone the repository to a standard location and add it to your Claude Code plugins:

```bash
git clone https://github.com/pborenstein/handoff.git ~/.claude/plugins/handoff
```

Or add as a dependency in your project's `.claude/settings.json`:

```json
{
  "plugins": ["~/.claude/plugins/handoff"]
}
```

## Usage

### Set up tracking on a new or existing project

```
/handoff:project-tracking
```

Creates the documentation structure:

- `docs/CONTEXT.md` - Current session state (30-50 lines, hot state for instant pickup)
- `docs/IMPLEMENTATION.md` - Living todo list for current phase (400-600 lines)
- `docs/DECISIONS.md` - Registry of architectural decisions (heading-based, grep-friendly)
- `docs/chronicles/phase-X.md` - Session-by-session implementation notes

### Start a work session

```
/handoff:session-pickup
```

Reads `docs/CONTEXT.md` (30-50 lines) for fast pickup. Falls back to `docs/IMPLEMENTATION.md` if CONTEXT.md is missing or stale.

### End a work session

```
/handoff:session-wrapup
```

Updates project documentation:

- Update CONTEXT.md with current focus and tasks
- Update IMPLEMENTATION.md task checkboxes
- Add chronicle entry to `docs/chronicles/phase-X.md` (if significant work done)
- Update DECISIONS.md if architectural decisions were made
- Commit documentation changes

## Documentation System

The system separates **hot state** (current session) from **cold storage** (history):

- **CONTEXT.md** - "Where I left off" (30-50 lines, read every session)
- **IMPLEMENTATION.md** - "What we're doing" (current phase detailed, completed phases compressed)
- **DECISIONS.md** - "What we decided" (heading-based, grep-friendly, single source of truth)
- **chronicles/phase-X.md** - "What happened" (slim 15-20 line entries, session-by-session)

**Goal**: Start a new session in under 2 minutes by reading only CONTEXT.md.

See [PROJECT-TRACKING-REFERENCE.md](skills/project-tracking/references/PROJECT-TRACKING-REFERENCE.md) for the complete guide.

## License

MIT License - see [LICENSE](LICENSE) file for details
