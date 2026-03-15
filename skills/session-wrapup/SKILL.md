---
name: session-wrapup
description: Update project documentation and commit changes after a work session
allowed-tools: Read, Write, Bash, Glob, AskUserQuestion
---

# Session Wrap-up

Update project documentation to prepare to clear context or start a new session.

## Documentation System

This command supports the **token-efficient documentation system**:
- `docs/CONTEXT.md` - Current session state
- `docs/IMPLEMENTATION.md` - Phase progress tracker
- `docs/DECISIONS.md` - Architectural decisions
- `docs/chronicles/phase-N.md` - Session history

## Tasks to complete:

NOTE: Some of these tasks may have been completed already.

### 1. Update CONTEXT.md (Required)

**File**: `docs/CONTEXT.md`

- Update frontmatter:
  - `updated`: today's date
  - `last_commit`: latest git commit hash
  - `phase` and `phase_name`: current phase info

- Update sections:
  - **Current Focus**: 1-2 sentences on what we're working on now
  - **Active Tasks**: Current task list with status
  - **Blockers**: Any impediments (empty if none)
  - **Context**: 3-5 bullet points of key things to remember
  - **Next Session**: 1-2 sentences on where to pick up

- **Keep total file under 50 lines**

### 2. Update Task Status in IMPLEMENTATION.md

**File**: `docs/IMPLEMENTATION.md`

- Update checkboxes in current phase section only
- Mark completed tasks as ✅
- Add new tasks discovered during work
- Keep current phase section detailed, compress completed phases

### 3. Add Chronicle Entry (if significant work done)

**File**: `docs/chronicles/phase-N-name.md`

- **Determine next entry number** by scanning all chronicle files:
  ```bash
  grep -h "^## Entry [0-9]" docs/chronicles/*.md 2>/dev/null | sed 's/## Entry \([0-9]*\).*/\1/' | sort -n | tail -1
  ```
  Use that number + 1 for the new entry (or 1 if no entries exist).

- Use **slim template** (15-20 lines):
  - Entry number, title, date
  - What/Why/How (brief)
  - Decisions (reference only)
  - Files (key files or commit hash)

- Only create entry if:
  - Meaningful work completed
  - Something worth recording for future reference
  - NOT for trivial updates

### 4. Update DECISIONS.md (if decisions made)

**File**: `docs/DECISIONS.md`

- Add new decision as heading-based entry:
  - `### DEC-XXX: Title (YYYY-MM-DD)`
  - Status, Context, Decision, Alternatives, Consequences
  - All detail goes here, chronicle just references it

- Update existing decision status if superseded

### 5. Commit Changes

- Stage all documentation changes
- Create comprehensive commit message
- Follow conventional commit format

---

## Pattern Examples

### Good wrap-up:
```
Updated docs/CONTEXT.md with current focus and next session info
Updated task checkboxes in docs/IMPLEMENTATION.md Phase 3 section
Added Entry 12 to docs/chronicles/phase-3-production.md
Added DEC-008 to docs/DECISIONS.md
Committed: "feat: implement caching layer with Redis"
```

### Avoid:
- Making CONTEXT.md exceed 50 lines
- Adding detailed history to IMPLEMENTATION.md (goes in chronicle files)
- Creating chronicle entries for trivial changes
- Duplicating decision details (full details in DECISIONS.md, reference in chronicle)

---

$ARGUMENTS
