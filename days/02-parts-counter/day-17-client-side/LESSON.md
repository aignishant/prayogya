---
project: "PNN <name>"    # "—" on day 0, which belongs to no project
day: NN
phase: PNN
title: "<the day's subject as a phrase — this is where the folder slug comes from>"
ids: [XX-00, XX-01]
kind: concept            # concept | mechanism | setup | gate
deploy_tier: D3          # D1..D5, or "—"
plan_version: "v3.1.0"
parts: 0                 # must equal the number of documents in parts/
files_printed: []        # every file this day prints whole; feeds CODEMAP.md
generated: "YYYY-MM-DD"
status: draft            # draft | written | complete
commit: ""               # filled in from the ledger row, after the commit exists
---

<!--
  THE HUB ORIENTS AND ASSEMBLES. IT NEVER TEACHES.

  No `**Line by line:**` in this file — a walkthrough here means a subtopic has been explained in
  the one document meant to be readable in a single pass. `python p.py depth` rejects it.

  Ten numbered sections, in order, exactly as the plan section 4.1 lists them. No duration, no
  estimate, no pace, anywhere. Delete every one of these comments before finishing.
-->

> **Yesterday:** <what day N-1 left you holding.>
> **Today:** <the one-sentence version of this day.>
> **Tomorrow:** <what this unlocks.>

## §1 The scene

<!-- The day's whole idea as one scene, in plain words. No jargon, no code. This is the only
     section allowed to be purely orienting — use it. Pick the day's one metaphor family here;
     the parts must not collide with it. -->

## §2 The map

<!-- One line saying what each SECTION means — the mental model its parts share — then the table.
     No minutes column, ever. -->

### 1 · <what this section is about>

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-<slug>/1.1-<slug>.md) | <title> | <the question> | foundation |

## §3 Setup — run this

<!-- Every mkdir, touch and pinned install this day needs, runnable as written, verified today. -->

```bash
<!-- the setup commands -->
```

## §4 Files this day prints

<!-- The paths, and which part prints each. This table feeds CODEMAP.md, and a file with no day
     is what makes the completeness rule mechanical instead of aspirational. -->

| File | Printed by |
| --- | --- |
| `<path>` | part 1.1 |

## §5 Build brief

<!-- What you type. Leave every `TODO(me)` UNSOLVED — teach, do not do the reps. -->

| File | What it must do |
| --- | --- |
| `<path>` | `TODO(me)`: <the rep> |

## §6 The check that must be able to fail

<!-- RED before the build brief is done, GREEN after. Say how to make it go red on purpose — a
     check nobody has seen fail is a check nobody has tested. -->

## §7 Request budget

<!-- Per-turn model calls per provider, counted across the WHOLE cast, against the plan section 9
     policy. `0` is an answer; state it. -->

## §8 Traps

<!-- The mistakes that eat the sitting, including any named 1.x to 2.x breaking change, placed
     exactly where the reader would otherwise take the wrong turn. -->

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |

## §10 Ledger & commit

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
