# Scannable Docs: Examples

Before-and-after pairs for each transformation in `SKILL.md`.

## Bold-label bullets to a table

Before:

```markdown
- **Plain scrolling:** 60 to 75 characters per line, 18 to 20px type
- **Short pages:** one chapter per page
- **Saved position:** scroll offset per chapter in localStorage
```

After:

```markdown
| Technique | Setting |
|:----------|:--------|
| Plain scrolling | 60–75 characters per line, 18–20px type |
| Short pages | One chapter per page |
| Saved position | Scroll offset per chapter in `localStorage` |
```

## Trivial bullets to a sentence

Before:

```markdown
### Dependencies
- **Runtime**: Node.js (built-in modules only)
- **Modules**: `fs`, `path`
- **External**: None
```

After:

```markdown
### Dependencies
Plain Node.js with no external dependencies; uses only the built-in `fs` and `path` modules.
```

## Pseudo-headings to prose

Before:

```markdown
**Purpose**: Statistical analysis and report generation

**Usage**:
    node analyze-history.js [history-file]

**Features**:
- Session detection
- Command categorization
```

After:

```markdown
Statistical analysis and report generation.

    node analyze-history.js [history-file]

Detects session boundaries from exit commands, groups commands into categories, and writes a report.
```

## Repeated code blocks to a task table

Before:

````markdown
### Generate the report
```bash
node analyze-history.js history.txt
```

### Find Docker usage
```bash
node query-history.js history.txt search "docker"
```
````

After:

```markdown
| Task | Command | Result |
|:-----|:--------|:-------|
| Generate the report | `node analyze-history.js history.txt` | Writes `history-analysis.md` |
| Find Docker usage | `node query-history.js history.txt search "docker"` | Lists every command containing "docker" |
```

## Mixed table to grouped tables

Before: one table mixing distribution, totals, and workflows.

```markdown
| Metric | Value | Details |
|:-------|:------|:--------|
| Git commands | 28.9% | Version control |
| File operations | 24.0% | ls, cd, rm, cp, mv |
| Total commands | 16,006 | Full history |
| Unique commands | 15,660 | 97.8% unique |
```

After: one table per kind, identical headers.

```markdown
### Command distribution

| Metric | Value | Details |
|:-------|:------|:--------|
| Git commands | 28.9% | Version control |
| File operations | 24.0% | ls, cd, rm, cp, mv |

### Volume

| Metric | Value | Details |
|:-------|:------|:--------|
| Total commands | 16,006 | Full history |
| Unique commands | 15,660 | 97.8% unique |
```

## Redundant hierarchy

Before:

```markdown
## Analysis tools
### Shell utility
#### fish-query.sh
Fast command-line queries.
### JavaScript tools
#### analyze-history.js
Statistical analysis.
```

After:

```markdown
## Analysis tools
### fish-query.sh
Fast command-line queries.
### analyze-history.js
Statistical analysis.
```

## Step list to a diagram

Before:

```markdown
1. Notes are read by the build script
2. The script validates them
3. It writes derived fields back
4. It emits JSON for the site and the Base reads the notes
```

After:

```
      notes (Markdown + frontmatter)
                  │
                  ▼
       build script: validate
                  │
                  ▼
   build script: write derived fields
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
   Obsidian Base       events.json → site
```

## Decisions as a table

Before:

```markdown
- **Record types:** one `event` type with a `kind` field, because evidence and narratives share date handling.
- **Relations:** top-level properties, because Obsidian only tracks top-level wikilinks.
```

After:

```markdown
| Decision | Choice | Reason |
|:---------|:-------|:-------|
| Record types | One `event` type with a `kind` field | Evidence and narratives share date handling |
| Relations | Top-level properties, one per type | Obsidian tracks wikilinks only in top-level properties |
```
