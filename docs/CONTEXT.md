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
- [ ] Decide whether to fix the README's own bold-label bullets flagged by the checker

## Blockers

None

## Context

- Five skills: project-tracking, project-repo, session-pickup, session-wrapup, scannable-docs
- scannable-docs is adapted from the Technical Documentation Principles gist; checker is report-only, exit 1 when it finds problems
- Running the checker on README.md flags 4 bold-label bullets (lines 92-95, the docs/ file list)
- Wrapup numbering now uses a grep/sort pipeline and refuses to append on top of duplicate entry numbers

## Next Session

Run releaserator for v1.3.0; optionally restyle the README file list to pass scannable_check.py first.
