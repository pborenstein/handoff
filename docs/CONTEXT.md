---
phase: 4
phase_name: Writing Skills
updated: 2026-10-15
last_commit: 1eefa9d
---

## Current Focus

Added the `scannable-docs` skill (formatting rules for technical/reference writing plus a report-only checker script) and hardened wrapup's chronicle entry numbering.

## Active Tasks

- [x] Release v1.2.0 (uninitialized-project guard)
- [x] Add `scannable-docs` skill with examples and `scannable_check.py`
- [x] session-wrapup: compute next chronicle entry as true max, check for duplicate numbers
- [ ] Release v1.3.0 (scannable-docs + numbering fix are unreleased)
- [x] Restyle README with scannable-docs (checker clean)

## Blockers

None

## Context

- Five skills: project-tracking, project-repo, session-pickup, session-wrapup, scannable-docs
- scannable-docs is adapted from the Technical Documentation Principles gist; checker is report-only, exit 1 when it finds problems
- README restyled with scannable-docs; documents the currency check, uninitialized-project guard, and scannable-docs usage
- Wrapup numbering now uses a grep/sort pipeline and refuses to append on top of duplicate entry numbers

## Next Session

Run releaserator for v1.3.0.
