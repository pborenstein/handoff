# Adding the `project-repo` Skill to handoff

## What we did

We added a new skill to the handoff plugin called `project-repo`. Here's the context and the steps.

## The problem it solves

Sometimes a directory contains multiple related projects, each with its own independent git history. You want shared documentation and session tracking across the collection, but you don't want to couple the individual repos (no submodules, no monorepo merge). The pattern is: a meta-repo at the parent level that gitignores all the member subdirs and tracks only shared docs.

The concrete model for this is `/Users/philip/projects/mimeo-sites/TEMPLATES` — a git repo managing seven site templates, each an independent repo, with a shared `CLAUDE.md` and `docs/` structure.

The existing `project-tracking` skill handles per-project docs but assumes a normal single-project repo. `project-repo` handles the additional layer: git init at the meta level, `.gitignore` construction, and a `CLAUDE.md` shaped for describing a multi-project collection.

## What was created

One file: `/Users/philip/projects/handoff/skills/project-repo/SKILL.md`

No assets directory was needed — the skill reuses the existing project-tracking assets for CONTEXT.md, DECISIONS.md, etc.

## What the skill does

When invoked, the skill:

1. Lists immediate subdirectories and asks the user which are member projects to exclude
2. Checks whether a git repo exists; runs `git init` if not
3. Creates/updates `.gitignore` listing each member dir explicitly with a trailing `/` (not `*/` — that would catch future utility dirs)
4. Creates `CLAUDE.md` with a collection description, member project list, shared conventions, and dev notes
5. Creates the `docs/` tracking structure (CONTEXT.md, IMPLEMENTATION.md, DECISIONS.md, `docs/chronicles/`) using the same formats as project-tracking
6. Stages only meta-repo files, verifies nothing from member dirs is included, and makes the initial commit

## We tested it

We ran the skill against `/Users/philip/projects/nahuatl-PROJECTS`, which contains five projects: apantli, nahuatl-frontmatter, tagex, temoa, tequitl. It initialized the git repo, created all the files, and made the initial commit `bd5b3de` with only the six meta-repo files.

## One thing to know

The skill is loaded via `--plugin-dir`, not by reinstalling. Always start Claude Code as:

```
claude --plugin-dir ~/projects/handoff
```
