# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[Unreleased]: https://github.com/pborenstein/handoff/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/pborenstein/handoff/releases/tag/v1.0.0
