# Phase 4: Writing Skills

## Entry 7: scannable-docs skill and chronicle numbering fix (2026-10-15)

**What**: Added the `scannable-docs` skill: rules for choosing tables, lists, paragraphs, and diagrams by content shape, before/after pairs in `references/examples.md`, and `scripts/scannable_check.py`, a report-only checker (bold-label bullets, pseudo-headings, table alignment, heading skips, list blank lines, emoji, banned jargon). Also changed session-wrapup to compute the next chronicle entry as the true max across files and to check for duplicate numbers before appending.

**Why**: The gist's documentation principles predate current models; the skill adds rules against the formatting habits models now overproduce. The numbering change addresses entries that sit out of physical order, where eyeballing the tail gives the wrong next number.

**How**: Checker skips code fences and frontmatter, exits 1 on findings. Verified against README.md: 4 bold-label hits.

**Files**: `skills/scannable-docs/`, `skills/session-wrapup/SKILL.md`, `README.md`, `CHANGELOG.md`
