# Phase 1: Initial Release

## Entry 1: Plugin extraction from plinth (2026-03-15)

**What**: Created the handoff plugin by extracting three skills from plinth (project-tracking, session-pickup, session-wrapup) into a standalone Claude Code plugin.

**Why**: The tracking system is cohesive enough to stand alone, and decoupling it from plinth lets both evolve independently.

**How**:

- Scaffolded plugin structure with .claude-plugin/plugin.json
- Copied skill files verbatim, then updated plinth: prefixes to handoff:
- Removed all legacy/backward-compat references — this is the first version
- Rewrote PROJECT-TRACKING-REFERENCE.md to remove migration and "old system" content
- Bootstrapped docs/ using the system itself

**Decisions**:

- DEC-001: Extract as standalone plugin
- DEC-002: No legacy templates or migration commands

**Files**: All files in skills/, docs/, README.md, CHANGELOG.md

## Entry 2: Fix session-wrapup grep usage (2026-03-17)

**What**: Fixed session-wrapup skill to use the Grep tool instead of bash grep for finding chronicle entry numbers.

**Why**: Claude Code conventions require using dedicated tools (Grep, Read, etc.) instead of bash equivalents. The skill was using bash grep which bypasses the tool layer.

**How**: Updated the chronicle entry number detection step to use the Grep tool with pattern `^## Entry [0-9]` across `docs/chronicles/*.md`.

**Files**: commit b92a670
