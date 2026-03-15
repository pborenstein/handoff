# Decisions

Architectural decisions for this project. Search with `grep -i "keyword" docs/DECISIONS.md`.

## Active Decisions

### DEC-001: Extract from plinth as standalone plugin (2026-03-15)

**Status**: Active

**Context**: The project-tracking, session-pickup, and session-wrapup skills in plinth form a cohesive system that is useful independently of plinth's other skills.

**Decision**: Extract these three skills into a standalone plugin named `handoff`, hosted at github.com/pborenstein/handoff.

**Alternatives considered**:
- Keep in plinth: Couples the tracking system to plinth's release cycle and scope
- Monorepo with plinth: More complex without clear benefit

**Consequences**: Projects that want session tracking can install handoff without installing all of plinth. Plinth's scope is reduced. The two plugins evolve independently.

---

### DEC-002: No legacy templates or migration commands (2026-03-15)

**Status**: Active

**Context**: The original plinth skills carried backward-compatibility references, migration commands, and legacy template variants from the evolution of the system.

**Decision**: Ship handoff with only the current system. No migration commands, no legacy templates, no "old system" comparisons.

**Alternatives considered**:
- Keep migration tooling: Useful for plinth users migrating existing projects, but that's plinth's concern, not handoff's

**Consequences**: Clean first-time experience. Users of the old plinth system who want to migrate will need to use plinth's migration tools before switching to handoff.
