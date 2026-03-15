---
name: project-tracking
description: Establish the files used to track and manage progress.
allowed-tools: Read, Write, Bash, Glob
---

# Project Tracking Setup

This skill establishes a token-efficient project tracking system for software projects.

## System Overview

**Token-Efficient Design**: Separates hot state (current session) from cold storage (history).

**Core Files**:
- `CONTEXT.md` - Current session state (30-50 lines, read every session)
- `IMPLEMENTATION.md` - Phase progress tracker (400-600 lines)
- `DECISIONS.md` - Architectural decisions (heading-based, grep-friendly)
- `chronicles/phase-N.md` - Detailed session history

**Key Benefits**:
- 75% reduction in session pickup tokens (~200 lines → ~50 lines)
- 45% reduction in chronicle entry size
- Single file read for session pickup (CONTEXT.md only)

## When to Use This Skill

- **New codebases**: Set up tracking from day one
- **Existing codebases**: Retroactively document project history and establish tracking
- **Legacy projects**: Establish tracking on projects that predate this system

## Quick Start

[PROJECT-TRACKING-REFERENCE.md](./references/PROJECT-TRACKING-REFERENCE.md) describes the complete token-efficient documentation system.


### For New Projects

1. Create base structure (no git history to analyze)
2. Initialize Phase 0 in IMPLEMENTATION.md
3. Ready to document first session

### For Existing Projects (Retroactive)

1. **Use TodoWrite** to track setup progress
2. **Analyze project history** (see commands below)
3. **Identify phase boundaries** based on major milestones
4. **Create documentation structure** in order
5. **Document retroactively** with appropriate detail level

## Step-by-Step Process for Existing Projects

### Step 1: Analyze Project History

Run these commands to understand the codebase:

```bash
# Full git history
git log --all --oneline --decorate

# Identify major refactors/features
git log --all --oneline --grep="refactor\|feat\|major"

# Check existing documentation
find . -name "*.md" -type f | grep -v node_modules

# Review changelog if exists
cat CHANGELOG.md

# Get commit count and timeline
git log --oneline | wc -l
git log --reverse --format="%ai %s" | head -5
git log --format="%ai %s" | head -5
```

### Step 2: Identify Phase Boundaries

Look for natural breakpoints:

**Good phase boundaries**:
- Major architectural refactors ("legendary refactor", "restructure")
- Feature milestones (v1.0.0, v2.0.0 releases)
- Significant pivots (monolith → microservices)
- Technology changes (rewrite in new language)

**Aim for 3-6 phases** for most projects:
- Too few: Loses meaningful structure
- Too many: Fragmented, hard to navigate

**Example phase progressions**:
- Foundation → Architecture → Features → Production
- MVP → Scale → Polish → Maintenance
- Prototype → Refactor → Features → Optimization

### Step 3: Create Files in This Order

**Use TodoWrite to track**:
```
1. Create docs/IMPLEMENTATION.md
2. Create docs/DECISIONS.md
3. Create docs/chronicles/ directory
4. Create chronicle files for each phase
5. Create docs/CONTEXT.md (from current phase)
6. Update docs/README.md (if exists)
```

**Note**: There is no CHRONICLES.md index file. Use `ls docs/chronicles/` for navigation instead.

### Step 4: File Creation Details

#### IMPLEMENTATION.md

**For existing projects** (token-efficient format):
- Phase Overview table (all phases)
- Completed phases: **3-5 bullets each** + link to chronicles
  - High-level achievements only
  - Link to `chronicles/phase-N.md` for details
- Current phase: Detailed (200-300 lines)
  - Active tasks with checkboxes
  - What's completed so far
  - What's next
- Future phases: High-level plans (5-10 bullets)

**Target size**: 400-600 lines

#### DECISIONS.md

**For existing projects** (heading-based format):
- Use heading-based format
- Each decision is a `### DEC-XXX: Title (YYYY-MM-DD)` heading
- Include: Status, Context, Decision, Alternatives, Consequences
- **Aim for 5-10 decisions** for retroactive docs
  - Focus on decisions still relevant today
  - Don't document every minor choice

**Extract decisions from**:
- Commit messages mentioning "decision", "choose", "vs"
- Architecture changes (modular refactor, tech choices)
- Configuration format choices
- UI/UX pattern choices

**Decision Categories** to look for:
- Architecture (structure, modules, patterns)
- Configuration (formats, storage)
- Display/UX (interaction patterns, visual design)
- Technology (language, framework, library choices)

#### CONTEXT.md

**For existing projects**:
- Create from current phase section in IMPLEMENTATION.md
- Extract: current focus, active tasks, blockers
- Get latest commit hash and entry number
- Keep under 50 lines total

**Sections**:
- Frontmatter (phase, updated, last_commit, last_entry)
- Current Focus (1-2 sentences)
- Active Tasks (checkboxes)
- Blockers (if any)
- Context (3-5 bullets)
- Next Session (where to pick up)

**This file replaces reading ~200 lines from IMPLEMENTATION.md for session pickup.**

#### chronicles/phase-X-name.md

**For existing projects** (retroactive entries):

**Balance detail vs. effort**:
- **Older phases** (completed long ago):
  - One summary entry per phase
  - High-level "what and why"
  - Light on implementation details
  - Focus on decisions and outcomes

- **Recent phases** (last 3-6 months):
  - More detailed entries
  - Can document specific features
  - Include code examples if relevant

- **Current phase**:
  - Full detail from this point forward
  - Document each session

**Retroactive entry format** (slim template):
```markdown
## Entry N: [Phase Name] (YYYY-MM-DD)

**What**: [1-2 sentences - what was accomplished in this phase]

**Why**: [1-2 sentences - context/motivation]

**How**: [Bullet points - key implementation details, max 5-7 bullets]

- Key change 1
- Key change 2
- Key change 3

**Decisions**: [Optional - only if DEC-XXX made]

- DEC-XXX: [one-line summary, detail in DECISIONS.md]

**Files**: [key files changed, or "see commits abc-def"]
```

**Target**: 15-20 lines per entry

**Full template available**: Use `chronicle-entry-full.md` for complex entries if needed.

### Step 5: Extract Decisions from Code/History

**Commands to find decisions**:
```bash
# Search commit messages
git log --all --grep="decide\|choose\|vs\|instead\|alternative" --oneline

# Find architectural changes
git log --all --grep="refactor\|architecture\|structure" --oneline

# Check for design docs
find . -name "*DESIGN*" -o -name "*ARCHITECTURE*" -o -name "*ADR*"

# Look for configuration choices
git log --all --grep="config\|yaml\|json\|toml" --oneline
```

**In code**, look for:
- Major abstraction choices (OOP vs functional, monolith vs modular)
- Technology selections (which library, which format)
- Pattern implementations (how errors handled, how config loaded)
- Interface designs (API structure, CLI commands)

### Step 6: Update Existing Documentation

If project has docs/README.md or similar:
- Add "Development Documentation" section
- Link to CONTEXT.md, IMPLEMENTATION.md, DECISIONS.md
- Add quick paths for contributors
- Explain session pickup workflow (read CONTEXT.md first)

## File Size Guidelines

| File | Target Size | Maximum | Purpose |
|------|-------------|---------|---------|
| CONTEXT.md | 30-50 lines | 50 lines | Session hot state |
| IMPLEMENTATION.md | 400-600 lines | 600 lines | Phase progress tracker |
| DECISIONS.md | Grows naturally | - | One heading per decision |
| Chronicle entry | 15-20 lines | 30 lines | Session history |
| chronicles/phase-X.md | No limit | - | Permanent record |

## Common Pitfalls for Existing Projects

- Don't try to document every commit — document major milestones and decisions
- Don't create 20+ phases for a 2-year project — aim for 3-6 meaningful phases
- Don't write novel-length retroactive entries — write summaries with links to code/commits
- Don't document every decision ever made — focus on architectural decisions still relevant
- Don't spend weeks on retroactive docs — spend 2-4 hours, then track going forward

## Success Criteria

After setup, you should have:
- CONTEXT.md with current session state (< 50 lines)
- Clear phase progression in IMPLEMENTATION.md (< 600 lines)
- Heading-based DECISIONS.md
- 5-10 key decisions documented
- One chronicle file per phase
- 1-2 entries per phase (more detail for recent/current)
- All files cross-referenced
- Current phase ready for ongoing tracking

## What to Tell the User

After setup, summarize:
1. Number of phases identified
2. Number of decisions documented
3. Number of chronicle entries created
4. **Where to start for next session**: Read CONTEXT.md (30-50 lines)
5. How to use the system going forward
6. Token savings achieved (session pickup now < 50 lines vs ~200 lines)


## Templates

See template files for detailed formats:
- `CONTEXT.md` - Hot state template
- `chronicle-entry-template.md` - Slim entry (15-20 lines)
- `chronicle-entry-full.md` - Full entry (optional, for complex sessions)
- `decision-entry-template.md` - Heading-based decision
- `DECISIONS.md` - Full decisions file template

## References

- See PROJECT-TRACKING-REFERENCE.md for complete token-efficient system explanation
