---
phase: 3
phase_name: Plinth Cleanup
updated: 2026-06-21
last_commit: 6373f66
---

## Current Focus

Released v1.1.0. Hardened pickup/wrapup: both now guard against running in directories with no tracking system.

## Active Tasks

- [x] Release v1.1.0 (project-repo + session-pickup currency check)
- [x] Sync PROJECT-TRACKING-REFERENCE with v1.1.0 skills
- [x] Guard pickup/wrapup against uninitialized projects

## Blockers

None

## Context

- Four skills: project-tracking, project-repo, session-pickup, session-wrapup
- session-pickup does a git fetch + HEAD/upstream check before trusting CONTEXT.md
- pickup and wrapup both bail out early if neither docs/CONTEXT.md nor docs/IMPLEMENTATION.md exists, pointing the user at project-tracking/project-repo
- v1.1.0 released; the guard feat is unreleased and pending the next bump

## Next Session

Run releaserator for v1.2.0 (the guard feat + reference docs are unreleased).
