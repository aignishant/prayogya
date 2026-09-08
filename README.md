# Prayoga

> **prayoga** (प्रयोग) — application, experiment, putting into practice. The word for the moment a
> thing stops being described and starts being done.

**40 independent agentic systems** built with Google ADK 2.x, MCP, Agent Skills and A2A — 297
sittings, 42 phases, 310 concepts, and forty repositories that each stand up alone.

Most agent curricula teach a framework and leave you with one demo. This one is arranged the other
way round: every project carries all three legs — **tools**, an **MCP boundary**, and a
**multi-agent cast** — and every project is complete on its own. Four people can take four
different folders from `projects/` to four different machines and each build a running system with
nothing else. That costs deliberate duplication, roughly 400 lines of scaffolding typed forty
times, and the plan §0 and §13 state the bill rather than hiding it.

Everything runs at **zero cost, by construction**: free-tier models, synthetic data always, and a
request budget stated per turn and counted across the whole cast.

## Where to start

| You want | Open |
| --- | --- |
| The contract everything obeys | [`docs/00_MASTER_PLAN.md`](docs/00_MASTER_PLAN.md) |
| Where the work actually is | [`docs/PROGRESS.md`](docs/PROGRESS.md) — the last row |
| What each day teaches | [`docs/WIKI.md`](docs/WIKI.md) |
| Where a concept is taught | [`docs/CURRICULUM_INDEX.md`](docs/CURRICULUM_INDEX.md) |
| What is written and what is not | [`docs/TRACKER.md`](docs/TRACKER.md) |
| Why something is the way it is | [`docs/adr/`](docs/adr/) |

## The commands

```bash
python p.py status       # how many days are complete, and what is next
python p.py brief N      # what day N must cover, and whether N is allowed yet
python p.py start N      # open day N in reading order
python p.py depth N      # check day N against the depth contract
python p.py check        # the whole-repository gate
python p.py done N       # finish a day: refuses on an unticked checklist, then commits
python p.py doctor       # is this repository wired correctly?
```

`./p` writes and checks the curriculum. It never builds or runs a project — **every project
carries its own `./run`**, and nothing under `projects/` imports from this root.

## How a day is written

A day is a **hub plus one document per subtopic**, never one long page. Each subtopic opens where
a reader who has never met the idea can stand, and ends at the real-system version: what a senior
writes instead, what degrades at scale with a number, the review comment, the interview question.

Three rules make that more than an aspiration:

- **Code is printed, never referenced.** If a file exists in a finished project, some day in that
  project printed it whole, at its real path. `CODEMAP.md` is the proof, and a file with no day
  fails the check.
- **Never invent a fact.** Versions, interfaces and citations are looked up live on the day they
  are used, with a dated ledger row. A failed lookup leaves the exact command, never a guess — and
  an unrun command's output is a `TODO`, never a plausible transcript.
- **Every day ends with a check that can go RED**, and at least one part per day is a deliberate
  failure: break it, read the real error, fix it.

The full contract is [§5 of the plan](docs/00_MASTER_PLAN.md), and `python p.py depth` enforces
the half a script can check.

## Layout

```text
docs/       the plan, the ledgers, the ADRs, the generated indexes
days/       the teaching — one folder per sitting
projects/   the forty systems, each a repository of its own
p.py        the whole authoring toolchain, one file, standard library only
granth.toml this repository's identity and the depth contract's knobs
```

Start at [day 0](days/day-000-toolchain-skeleton-driver/LESSON.md).
