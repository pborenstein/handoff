# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.0] - 2026-06-21

### Added

- `session-pickup` and `session-wrapup` now guard against running in an uninitialized directory: if neither `docs/CONTEXT.md` nor `docs/IMPLEMENTATION.md` exists, they report that no tracking system is present and stop, rather than improvising an empty plan or scattering `docs/` files ([6373f66](https://github.com/pborenstein/handoff/commit/6373f66))

### Changed

- `PROJECT-TRACKING-REFERENCE.md` synced with v1.1.0 skills: documents the session-pickup checkout-currency check and points to the `project-repo` skill for meta-repos ([e2083b7](https://github.com/pborenstein/handoff/commit/e2083b7))

## [1.1.0] - 2026-06-21

### Added

- `project-repo` skill: initialize a meta-repo that coordinates a collection of related projects, each with its own independent git history ([2cbad82](https://github.com/pborenstein/handoff/commit/2cbad82))

### Changed

- `session-pickup` now verifies the checkout is current (git fetch + HEAD/upstream comparison) before trusting tracking files, since frontmatter can look fresh while the checkout is behind ([f56150c](https://github.com/pborenstein/handoff/commit/f56150c))

## [1.0.0] - 2026-03-15

### Added

- `project-tracking` skill: establish token-efficient documentation structure
- `session-pickup` skill: read CONTEXT.md to resume work in under 2 minutes
- `session-wrapup` skill: update docs and commit at end of session
- Templates: CONTEXT.md, DECISIONS.md, chronicle-entry-template.md, chronicle-entry-full.md, decision-entry-template.md
- PROJECT-TRACKING-REFERENCE.md: complete system documentation
- `--plugin-dir` installation option documented in README

### Fixed

- Use Grep tool instead of bash grep in session-wrapup to avoid permission prompts

[Unreleased]: https://github.com/pborenstein/handoff/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/pborenstein/handoff/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/pborenstein/handoff/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/pborenstein/handoff/releases/tag/v1.0.0
