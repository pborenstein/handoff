---
name: project-repo
description: Initialize a meta-repo that coordinates a collection of related projects, each with its own independent git history.
allowed-tools: Read, Write, Bash, Glob, AskUserQuestion
---

# Project Repo Setup

Initialize a meta-repo: a git repository that tracks shared documentation and conventions for a collection of related projects. Each member project lives in a subdirectory with its own independent git history; this repo tracks only the coordination layer.

**Model**: `/Users/philip/projects/mimeo-sites/TEMPLATES` — a repo that manages seven site templates, each an independent git repo, with a shared `CLAUDE.md` and `docs/` tracking structure.

## When to Use This Skill

- You have a directory containing multiple related projects (each with their own repos)
- You want shared documentation, conventions, and session tracking across all of them
- The subdirectory repos should remain independent — not submodules, just co-located

## Step-by-Step Process

### Step 1: Inventory the Directory

List immediate subdirectories and ask the user which ones are member projects to be excluded from the meta-repo:

```bash
ls -1d */
```

If the user hasn't specified, use AskUserQuestion to confirm:
- Which subdirs are member projects (to exclude via `.gitignore`)
- What the meta-repo is for (used in `CLAUDE.md`)

### Step 2: Initialize the Git Repo

Check if a git repo already exists:

```bash
git rev-parse --git-dir 2>/dev/null && echo "exists" || echo "none"
```

If none: `git init`

If exists: note it and continue.

### Step 3: Create or Update `.gitignore`

Add a trailing `/` to each member project name so git ignores the entire directory tree:

```
# Member project repos (each has its own independent git history)
project-one/
project-two/
project-three/
```

List each member dir explicitly — do not use `*/` (that would also catch future utility dirs).

Also add standard ignores:
```
.DS_Store
```

If `.gitignore` already exists, read it first and append only what's missing.

### Step 4: Create `CLAUDE.md`

Create a `CLAUDE.md` at the repo root using this template (fill in project-specific details):

```markdown
# [Collection Name]

[One paragraph describing what this collection is and its purpose.]

## Member Projects

- **project-one** — brief description
- **project-two** — brief description
- **project-three** — brief description

## Shared Conventions

[Any conventions that apply across all member projects — naming, tooling, workflows, deployment, etc. Leave blank and add as they emerge.]

## Development Notes

[Any operational notes: how to work with the member repos, common commands, etc.]
```

If `CLAUDE.md` already exists, read it before writing — update rather than overwrite.

### Step 5: Create the `docs/` Tracking Structure

Create `docs/chronicles/` and the three tracking files. Use the project-tracking skill's assets as templates.

**File order**:
1. `docs/IMPLEMENTATION.md` — Phase 0: Foundation (current setup work)
2. `docs/DECISIONS.md` — empty, ready for first decision
3. `docs/chronicles/` — directory (create with a `.gitkeep` if empty)
4. `docs/CONTEXT.md` — current state after setup

See the `project-tracking` skill for detailed file formats and size guidelines.

**CONTEXT.md** for a fresh project-repo should reflect:
- Phase 0 / Foundation
- Current Focus: setting up meta-repo structure
- No blockers
- Next Session: start documenting member projects

### Step 6: Initial Commit

Stage only meta-repo files (not member project dirs — they're gitignored):

```bash
git add .gitignore CLAUDE.md docs/
git status  # verify no member project files are staged
git commit -m "Initialize project-repo structure"
```

Confirm the commit contains only `.gitignore`, `CLAUDE.md`, and `docs/`.

## File Size Guidelines

Same as project-tracking:

| File | Target | Maximum |
|------|--------|---------|
| CONTEXT.md | 30-50 lines | 50 lines |
| IMPLEMENTATION.md | 400-600 lines | 600 lines |
| DECISIONS.md | grows naturally | — |
| Chronicle entry | 15-20 lines | 30 lines |

## What to Tell the User

After setup:
1. Files created and their purpose
2. Which subdirs are excluded via `.gitignore`
3. Where to start next session: read `docs/CONTEXT.md`
4. Suggest running `project-tracking` skill if the project already has history to document

## References

- `project-tracking` skill — creates the same `docs/` structure for single-project repos; use it for guidance on filling out IMPLEMENTATION.md phases and DECISIONS.md
- `session-pickup` / `session-wrapup` skills — work the same way once the meta-repo is set up
- `PROJECT-TRACKING-REFERENCE.md` — complete system explanation
