---
name: scannable-docs
description: Format technical and reference writing so it scans fast and stays dense — tables for data, bullets for discrete items, short paragraphs for context, top-down diagrams for flow. Use when writing or restyling a spec, schema, README, project note, reference note, or comparison, or when asked for something "scannable", "dense", or "tables and lists".
compatibility: Designed for Claude Code with filesystem access
allowed-tools: Bash, Read, Edit, Write, Glob, Grep
---

# Scannable Docs

A reader should find any fact in a few seconds, and nothing on the page should be filler. Form follows the shape of the content: data goes in tables, discrete items in lists, reasoning in short paragraphs.

Adapted from [Technical Documentation Principles](https://gist.github.com/pborenstein/80b6e1a9011b4a02ad13dfbc06874141), written before current models. The principles hold; this version adds the formatting habits models now overproduce.

## Scope

Use it for specs, schemas, READMEs, project notes, reference notes, comparisons, and how-tos.

Do not use it for writing that has its own voice: essays, personal notes, narrative memos, or conversational replies. Another skill or the author's own prose sets their form.

## Choose the form

| Content | Form | Test |
|:--------|:-----|:-----|
| Items that share attributes: fields, options, commands, comparisons | Table | Can you name the columns? |
| Discrete items with nothing in common to tabulate: caveats, open items | Bulleted list | Would they read naturally as a list aloud? |
| Steps where order matters | Numbered list | Does step 3 fail if done before step 2? |
| Context, reasoning, transitions | Paragraph of 1–3 short sentences | Does each sentence depend on the one before? |
| Flow, dependency, hierarchy | Diagram, top-down | Are there arrows in your head? |
| Exact syntax someone will copy | Code block | Would anyone paste it? |

When content fits two forms, prefer the denser one that still reads without effort. Three trivial label-value bullets are a sentence, not a table.

## Tables

- Left-align every column: `|:-----|:-----|`.
- The first column is the key (name, term, field), and rows are in a meaningful order: by sequence, by importance, or alphabetical.
- Column headers are descriptive nouns: "Command", not "Syntax"; "Meaning", not "Info".
- Every cell carries information. Drop a column that is mostly blank, `—`, or a restatement of the first column.
- Cells hold phrases, not paragraphs. A cell that needs two sentences means the content wants prose or its own section.
- Split a table past about 12 rows, or one mixing kinds of rows, into several tables under `###` subheadings. Parallel tables use identical headers.
- Identifiers, paths, and values in backticks. No bold inside cells.

## Lists

- A blank line before every list (CommonMark and Obsidian both need it).
- Parallel grammar: every item starts the same way (all verbs, or all nouns).
- One level of nesting at most. Deeper nesting is a table or a new section.
- No bold label at the start of an item (`- **Speed:** fast`). If items have labels, they have attributes: make a table. Otherwise write the item as a plain sentence.

## Headings

- No skipped levels: `##` then `###`, never `##` then `####`.
- No wrapper heading with one child. Remove the intermediate level.
- Parallel sections use the same heading level and the same internal structure.
- A heading names its content as a noun phrase. "Dates", "Layer types", "Open decisions" — not "Overview", "Details", or "Key takeaways".
- No bold line standing in for a heading (`**Usage:**` alone on a line). Use a real heading, or fold it into the sentence that follows.

## Prose

- Short sentences, one idea each.
- Describe mechanisms and measurable facts, not quality: what it does, not how impressive it is.
- Use the same term for the same thing everywhere. Define a term once, at first use.
- No opening paragraph that restates the title, and no closing summary. The document is the summary.
- No signposting ("It's worth noting", "Let's look at"), no stacked hedges ("may potentially"), no rhythm triplets ("fast, simple, and reliable") unless each item is measured.
- No jargon: leverage, utilize, robust, seamless, powerful, elegant, sophisticated, innovative, comprehensive.
- No emoji. No em-dash chains that string three clauses together; split them into sentences.

## Diagrams

- ASCII boxes and arrows, drawn top-down, for pipelines, data flow, and relationships between records.
- Label arrows with the relation name when it is not obvious.
- Keep a diagram under about 20 lines. A larger one is two diagrams.
- Mermaid `flowchart TD` is acceptable when the target renders it (Obsidian does); ASCII renders everywhere.

## Code and examples

- Several commands become a table: Task | Command | Result.
- A full example stays whole when it is the substance, such as a complete schema record. Do not trim it to fit a table.
- One code block per language per example; label the language on the fence.

## Docs about a codebase

- Open with one paragraph on what it does and for whom.
- Mention supporting files (sample data, fixtures) in context, not as top-level sections.
- Do not treat agent configuration files as content sources: `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `SKILL.md`, `.claude/`, `.cursor/`. They are written for models, not readers.

## Workflow

1. Read the source material, or the existing document if restyling.
2. Sort the content by shape using the form table above, before writing anything.
3. Write the document.
4. Run the checker and fix what it reports:

   ```bash
   python3 <this skill's directory>/scripts/scannable_check.py "path/to/doc.md"
   ```

   It flags bold-label bullets, pseudo-headings, non-left-aligned tables, skipped heading levels, lists without a blank line before them, emoji, and banned jargon. It skips YAML frontmatter and code fences. It is a report; it never edits the file.
5. Read it once more for what the checker cannot see: columns that carry nothing, lists that should be tables, parallel sections with different structure.

For before-and-after pairs of each transformation, read `references/examples.md` in this skill's directory.

## Constraints

- Restyling changes form, not facts. Do not drop information to make a table fit; add a column or a section.
- Project conventions win where they conflict with these rules: a repo's own style guide, a vault's link or frontmatter rules, a house diagram direction.
