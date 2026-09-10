---
project: "PNN <name>"
day: NN
title: "<the day's subject as a phrase — this is where the folder slug comes from>"
spine: NN                # the plan §12 spine slot this day is, or the slot an extra day follows
kind: concept            # concept | mechanism | setup | gate
deploy_tier: D3          # D1..D5
plan_version: "v4.1.0"
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

  NOTHING IN THIS FILE MAY REFERENCE ANOTHER PROJECT (plan §6). Not a path, not a name, not
  "as we saw". `python p.py check` greps for it and fails. Everything this day needs was built by
  an earlier day OF THIS PROJECT, or is built today.

  Ten numbered sections, in order, exactly as the plan §4.1 lists them. No duration, no estimate,
  no pace, anywhere. Delete every one of these comments before finishing.
-->

> **Yesterday:** <what day N-1 of this project left you holding.>
> **Today:** <the one-sentence version of this day.>
> **Tomorrow:** <what this unlocks.>

## §1 The scene

<!-- The day's whole idea as one scene, in plain words, FROM THIS PROJECT'S INDUSTRY. No jargon,
     no code. Pick the day's one metaphor family here; the parts must not collide with it.

     Plan §14: a scene that would work unchanged in another project has failed its own contract.
     That is the whole defence against forty projects reading like one project pasted forty
     times, so it is a hard test, not a suggestion. -->

## §2 The map

<!-- One line saying what each SECTION means — the mental model its parts share — then the table.
     No minutes column, ever. -->

### 1 · <what this section is about>

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-<slug>/1.1-<slug>.md) | <title> | <the question> | foundation |

## §3 Setup — run this

<!-- Every mkdir, touch and pinned install this day needs, runnable as written, verified today.
     No step may read "as you did before" or name another project. -->

```bash
<!-- the setup commands -->
```

## §4 Files this day prints

<!-- The paths, and which part prints each. This table feeds CODEMAP.md, and a file with no day
     is what makes the Completeness Rule mechanical instead of aspirational. `.gitignore`,
     `pyproject.toml`, `Dockerfile` and the `run` driver are files too (plan §0 rule 1). -->

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

<!-- Per-turn model calls per provider, counted across the WHOLE cast, against the plan §9
     policy. `0` is an answer; state it. -->

## §8 Traps

<!-- The mistakes that eat the sitting, including any named 1.x to 2.x breaking change, placed
     exactly where the reader would otherwise take the wrong turn. -->

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block, which is the only region read:

```text
| NN | D | YYYY-MM-DD | <title> | <parts> | <hash> | yes |
```

**`docs/GLOSSARY.md`** — one row per term this day defined for the first time:

```text
| <term> | <plain-language definition> | PNN day D part S.T | <also called> |
```

<!-- Add PINS.md / SOURCES.md / PROVENANCE.md rows here if this day earned any. -->

**Commit:**

```text
PNN day DD: <title>
```
