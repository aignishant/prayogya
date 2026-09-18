---
day: NN
phase: P
phase_name: "<the phase theme, from the plan's §7>"
title: "<the day's subject as a phrase — this is where the folder slug comes from>"
ids: [XX-00, XX-01]
kind: concept            # concept | mechanism | setup | gate
plan_version: "v1.0.0"
parts: 0                 # must equal the number of documents in parts/
generated: "YYYY-MM-DD"
status: draft            # draft | written | complete
commit: ""               # filled in by the ledger row, after the commit exists
---

<!--
  THE HUB ORIENTS AND ASSEMBLES. IT NEVER TEACHES.

  No `**Line by line:**` in this file — a walkthrough here means a subtopic has been explained in
  the one document meant to be readable in a single pass. No duration, estimate or pace anywhere.

  Eleven numbered sections, in order. Delete every one of these comments before finishing.
-->

> **Yesterday:** <what day N-1 left you holding.>
> **Today:** <the one sentence version of this day.>
> **Tomorrow:** <what this unlocks.>

## §1 Where we are

<!-- A scene and an analogy. Plain language, NO CODE, NO JARGON. This is the only place in the day
     that is allowed to be purely orienting — use it. One metaphor family for the whole day: what
     you pick here, the parts must not collide with. -->

## §2 The map

<!-- One line saying what each SECTION means — the mental model its parts share — then the table.
     No minutes column, ever. -->

### 1 · <what this section is about>

<!-- one line: the mental model these parts share -->

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-<slug>/1.1-<slug>.md) | <title> | <the question> | foundation |

### 2 · <what this section is about>

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-<slug>/2.1-<slug>.md) | <title> | <the question> | working |

<!-- If the day has sources/, add this table and mark it read-after-the-parts. Build the mechanism
     by hand first; read the original proposal afterwards. -->

### Sources — read these **after** the parts

| # | Source | Identifier |
| --- | --- | --- |
| [01](sources/01-<slug>.md) | <title> | `<identifier>` |

## §3 Setup

<!-- Every command this day needs, pinned and runnable as written, in the shell this project
     actually uses. A command that has not been run is a TODO, not a step. -->

```bash
<!-- the setup commands -->
```

## §4 Build brief

<!-- What to make. Leave every `TODO(me)` UNSOLVED — teach, do not do the reps. -->

| File | What it must do |
| --- | --- |
| `<path>` | `TODO(me)`: <the rep> |

## §5 The check that must be able to fail

<!-- The check that is RED before the build brief is done and GREEN after. State how to make it go
     red on purpose — a check nobody has seen fail is a check nobody has tested. -->

## §6 Budget

<!-- What this day spends against the constraints in the plan's §4. Count model requests per
     provider; `0` is an answer, and the usual one once cassettes exist. State it. -->

## §7 Traps

<!-- The mistakes that eat an evening. Name any breaking change, deprecated form or common wrong
     turn exactly where the reader would otherwise take it. -->

## §8 Verify before you build

<!-- The live URLs actually fetched TODAY, and what each one confirmed. Never from memory. -->

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |

## §9 Say it out loud

<!-- One paragraph, spoken voice — the answer you would give an interviewer who asked what you did
     today and why it was done this way. -->

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Defined by understanding and green checks, never by effort
spent.

## §11 Ledger & commit

<!-- The verbatim rows to paste, and the commit message. The hub ends here. -->

**`docs/PROGRESS.md`:**

```text
| NN | YYYY-MM-DD | XX-00, XX-01 | <parts> | <hash> | yes |
```

**`docs/GLOSSARY.md`** — one row per term this day defined for the first time:

```text
| <term> | <plain-language definition> | day NN part S.T | <also called> |
```

<!-- Add PINS.md / SOURCES.md / PROVENANCE.md rows here if this day earned any. -->

**Commit:**

```text
day NN: <title> — closes XX-00, XX-01
```
