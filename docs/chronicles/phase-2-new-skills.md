# Phase 2: New Skills

## Entry 3: Add project-repo skill (2026-04-11)

**What**: Added `project-repo` skill for initializing a meta-repo that coordinates a collection of related projects, each with its own independent git history.

**Why**: Real use against `/Users/philip/projects/mimeo-sites/TEMPLATES` revealed a pattern not covered by `project-tracking`: a parent directory with multiple independent repos that needs shared documentation and conventions without submodules or monorepo coupling.

**How**:

- Created `skills/project-repo/SKILL.md` — inventories subdirs, git init if needed, writes `.gitignore` with explicit member dir entries, creates `CLAUDE.md` and `docs/` structure
- Tested against nahuatl-PROJECTS (apantli, nahuatl-frontmatter, tagex, temoa, tequitl) — commit bd5b3de in that repo
- Updated README: added to skills list, added usage section
- Updated plugin.json: description and keywords
- Moved session notes (FOODLYGOODLY.md) to docs/archives/

**Files**: `skills/project-repo/SKILL.md`, `README.md`, `.claude-plugin/plugin.json`, `docs/archives/FOODLYGOODLY.md`
