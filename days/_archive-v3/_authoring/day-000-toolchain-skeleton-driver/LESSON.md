---
project: "— (the authoring repository belongs to no project)"
day: 0
phase: 0
title: "Day zero — the toolchain, the skeleton, and the ./p driver"
ids: [RB-01, RB-02, RB-03]
kind: setup
deploy_tier: "—"
plan_version: "v3.1.0"
parts: 4
files_printed: [".python-version", ".gitignore", "granth.toml"]
generated: "2026-09-08"
status: written
commit: ""
---

> **Yesterday:** nothing. This is the first sitting, and the repository does not exist yet.
> **Today:** build the workshop — the tools, the benches, and the foreman who holds the job cards.
> **Tomorrow:** P00 Foundry day 1, the first project, on a machine that can now check its own work.

## §1 The scene

A workshop opens on its first morning. There are no jobs yet. What there is instead is a decision
about how the shop will run, and it gets made now whether or not anyone notices making it.

Three things go up before the first job comes through the door. **The tool board**, so that a
spanner is a fact about the shop rather than about whoever is holding it. **The benches**, one per
job, each with its own drawer — and the office, which holds the book but does not own the benches.
And **the foreman**, whose whole job is the job-card book: which job is next, what it needs,
whether the one before it was signed off.

None of that builds anything. That is the point of it. Forty systems are going to be built here
over the next 296 sittings, and every one of them has to be finishable by someone who arrives with
only that bench and no access to this office. The arrangement that makes that possible is decided
today, in an empty shop, when it is free.

The last thing that goes up is an inspection stamp — and the last thing anyone does today is check
that the stamp can actually reject a job. A shop that has never seen its inspection say no does not
have an inspection. It has a stamp.

## §2 The map

Two sections. The first is the physical setup: what has to exist on the machine and in the folder
before any curriculum work can begin. The second is the driver: the one program this repository is
operated through, and the proof that its checks are connected to anything.

### 1 · The workbench

*The mental model: what must be true of the machine and the folders before day 1 is possible.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-workbench/1.1-one-tool-owns-the-environment.md) | One tool owns the environment | Which Python is *this* Python, and how does a file decide rather than a habit? | foundation |
| [1.2](parts/01-the-workbench/1.2-two-repositories-one-folder.md) | Two repositories in one folder | What is the authoring repository, what is a project, and why can one never import the other? | working |

### 2 · The driver

*The mental model: `./p` holds the book and checks the work; it never does the work.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-driver/2.1-the-foreman-and-the-order-guard.md) | The foreman that never turns a spanner | How does the plan become something a script can read, and what stops day 5 being written first? | working |
| [2.2](parts/02-the-driver/2.2-the-inspection-that-inspected-nothing.md) | The inspection that inspected nothing | How do you know a green check is checking anything? | production |

## §3 Setup — run this

Every command below was run on this machine today, and the versions it reported are in
`docs/PINS.md`. Run them in order; stop at the first one that surprises you.

```bash
python --version
python3 --version
uv --version
git --version

uv python pin 3.12
cat .python-version

mkdir -p docs/adr docs/wiki docs/archive days/_TEMPLATES projects .claude/skills/day-prayoga

python p.py doctor
python p.py brief 0
```

## §4 Files this day prints

`p.py` is the exception on this day and is called out here rather than buried: it is given
complete rather than typed, and parts 2.1 and 2.2 print and walk the four functions that carry its
decisions. The Completeness Rule in the plan §0 binds a *project*, and the authoring repository is
not one — but a reader who never opens the file they run 297 times has been shortchanged, so the
walk is not optional.

| File | Printed by |
| --- | --- |
| `.python-version` | part 1.1 |
| `.gitignore` | part 1.2 |
| `granth.toml` | part 2.1 |
| `p.py` — `marked_block`, `plan_days` | part 2.1 |
| `p.py` — `unexplained_code_blocks` | part 2.2 |

## §5 Build brief

| File | What it must do |
| --- | --- |
| `.python-version` | `TODO(me)`: pin it, then read the file back and say what would happen if the interpreter it names were not installed. |
| `.gitignore` | `TODO(me)`: prove the `.env` rule works with `git check-ignore -v`, then explain why the same rule added tomorrow would not protect a file committed today. |
| `granth.toml` | `TODO(me)`: change `require_failure_part` to `false`, run `python p.py depth 0`, and say in one sentence what the repository has just lost. Put it back. |
| any part of this day | `TODO(me)`: delete one required heading, watch `depth` name it, restore it. Do not skip this because you believe it will work. |

## §6 The check that must be able to fail

```text
python p.py doctor     # wiring: config, plan markers, ledgers, no ID on two days
python p.py depth 0    # this day against the plan §5 contract
python p.py check      # depth for every written day + the generated documents are current
```

**How to make it go red on purpose.** Delete the `## In production` heading from any part and run
`python p.py depth 0`; it names the file and the missing section. Or comment out `failure: true` in
part 2.2 and watch the day be refused for having no deliberate failure in it. Both were seen red
before this day was called finished, and part 2.2 pastes the real output.

## §7 Request budget

**Zero model calls.** No agent runs today, no provider is contacted, and no API key is needed —
`.env` does not exist yet and part 1.2 is about the file that will hide it when it does.

This is worth stating rather than omitting, because from day 1 onward the number is never zero and
every hub says what it is. The plan §9 counts requests **across the whole cast**: a three-agent
turn is at least three requests, and a writer-critic loop is unbounded until you bound it.

## §8 Traps

- **`python` and `python3` are not the same interpreter.** On this machine they are 3.12.10 and
  3.11.9. Every command in this curriculum uses the bare name, so the bare name is the one that has
  to be right.
- **`uv python pin` writes a pin it has not verified.** It warns that no interpreter was found and
  pins the version anyway, exiting `0`. Read the file back; do not trust the exit code.
- **`.gitignore` only governs files git has not seen yet.** Adding a rule does not un-track a file
  already committed. This is why the ignore file is written before the first secret rather than
  after the first scare.
- **A `bash` block followed by its output block breaks the walkthrough check.** The scan stops at
  the next opening fence. Put the command and its real output in one `console` block. This trap was
  found by the checker while this day was being written, and part 2.2 shows the red.
- **A malformed `granth.toml` gives a raw traceback, not a message.** `load_config` does not guard
  the parse. The line and column in `TOMLDecodeError` are accurate; the fault is always in the
  config, never in the plan.
- **Never edit anything under `docs/wiki/`, or `TRACKER.md`, `TRACEABILITY.md`,
  `CURRICULUM_INDEX.md`, `WIKI.md`.** They are generated. The next `index` overwrites you without
  asking.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| Python interpreter | `python --version` on this machine | 2026-09-08 | 3.12.10 — satisfies the 3.11+ that `tomllib` requires |
| A second interpreter | `python3 --version` on this machine | 2026-09-08 | 3.11.9 — the two names resolve differently here |
| uv | `uv --version` | 2026-09-08 | 0.12.3, `x86_64-pc-windows-msvc` |
| git | `git --version` | 2026-09-08 | 2.54.0.windows.1 |
| The pin is written, not verified | `uv python pin 3.13.99` | 2026-09-08 | warns no interpreter found, pins anyway, exits 0 |
| The ignore rule bites | `git check-ignore -v .env` | 2026-09-08 | `.gitignore:2:.env` — and `git status` reports nothing |
| The order guard refuses | `python p.py brief 5` | 2026-09-08 | STOP, lists every open earlier ID, exits 1 |
| The contract as configured | `python p.py depth --list` | 2026-09-08 | seven part sections and ten hub sections, matching the plan §5 and §4.1 |

## §10 Ledger & commit

**`docs/PROGRESS.md`:**

```text
| 0 | 2026-09-08 | RB-01, RB-02, RB-03 | 4 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the terms this day defined for the first time are already in the file:
authoring repository, project repository, driver, depth contract, generated document, marker block.

**`docs/PINS.md`** — Python 3.12.10, uv 0.12.3 and git 2.54.0.windows.1, each with the command that
observed it. Already appended.

**Commit:**

```text
day 00: Day zero — the toolchain, the skeleton, and the ./p driver — closes RB-01, RB-02, RB-03
```
