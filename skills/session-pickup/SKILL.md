---
name: session-pickup
description: Read context from previous session to prepare for new work
allowed-tools: Read, Write, Bash, Glob, AskUserQuestion
---

# Session Pick-up

Read context from previous session to prepare for new work.

## Tasks to complete:

0. **Verify the checkout is current** (do this BEFORE reading any tracking file):
   - If this is a git repo, run `git fetch`, then compare local HEAD to upstream:
     `git rev-list --left-right --count @{upstream}...HEAD` (left = behind, right = ahead)
   - **Behind** (left > 0): the tracking files may describe commits this checkout
     does not have. Warn the user, recommend reconciling, and offer to
     `git pull --rebase`. Do NOT trust CONTEXT.md's contents until reconciled.
   - **Diverged** (both > 0): local and remote have both moved. Warn the user,
     recommend reconciling (rebase is usually right), and offer to do it. Do not
     plan new work on top of a diverged tip.
   - Let the user decide; do not auto-reconcile without confirmation.
   - Rationale: CONTEXT.md's `updated`/`last_entry` are self-reported and can
     look fresh while the checkout is behind. Tracking files sometimes land via
     out-of-band pushes (including other projects' sessions), so a recent
     frontmatter date is NOT proof the local checkout is current.

1. **Check for CONTEXT.md** (token-efficient system):
   - Try to read `docs/CONTEXT.md`
   - If it exists:
     - Check the `updated` date in frontmatter
     - If older than 7 days, warn user it may be stale (in addition to the git
       check in step 0)
     - Read the entire file (~30-50 lines)
     - Summarize current focus, active tasks, and blockers
     - Report ready to work based on "Next Session" section
     - DONE - no need to read other files unless context is unclear

2. **Fall back to IMPLEMENTATION.md** (if CONTEXT.md missing):
   - Use Grep to search for "🔵" to find the current phase line number
   - Use Read with offset/limit to read ~200-300 lines starting from that marker
   - Understand from that section:
     - What phase/sub-phase is active
     - Task checkboxes and their status
     - Any notes about what to work on next
   - DO NOT read the entire IMPLEMENTATION.md file

3. Make a plan for what to do next based on the context

Note: CHRONICLES.md and DECISIONS.md are historical context. Only read them if
you need deeper background on a specific decision or past work.


