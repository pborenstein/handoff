---
name: session-pickup
description: Read context from previous session to prepare for new work
allowed-tools: Read, Write, Bash, Glob, AskUserQuestion
---

# Session Pick-up

Read context from previous session to prepare for new work.

## Tasks to complete:

1. **Check for CONTEXT.md first** (token-efficient system):
   - Try to read `docs/CONTEXT.md`
   - If it exists:
     - Check the `updated` date in frontmatter
     - If older than 7 days, warn user it may be stale
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


