# Prayoga

> **prayoga** (प्रयोग) — application, experiment, putting into practice. The word for the moment a
> thing stops being described and starts being done.

**40 independent agentic systems** built with Google ADK 2.x, MCP, Agent Skills and A2A — 816
sittings across forty repositories that each stand up alone, in forty different industries.

Most agent curricula teach a framework and leave you with one demo. This one is arranged the other
way round. Every project is a **complete system in a real domain** — insurance claims intake, a
warehouse stock ledger, clinical triage, contract review, fraud review, incident command — and
every project carries the **whole agent feature set**: its own tools, its own MCP boundary, its own
multi-agent cast, callbacks, sessions and memory, structured output, reliability, security,
observability, evals and deploy.

**And every project teaches all of it from zero, in its own documents.** Take one folder from
`projects/` to a machine that has nothing, and it will tell you how to install the toolchain, why
`.gitignore` is written before `.env` exists, and every line of code it needs — without ever
sending you to another folder. That costs enormous, deliberate repetition, and the plan §0 and §16
state the bill rather than hiding it.

Everything runs at **zero cost, by construction**: free-tier models, synthetic data always, and a
request budget stated per turn and counted across the whole cast.

## Where to start

| You want | Open |
| --- | --- |
| The contract everything obeys | [`docs/00_MASTER_PLAN.md`](docs/00_MASTER_PLAN.md) |
| The forty projects and their industries | [plan §11](docs/00_MASTER_PLAN.md) |
| What every project builds, in order | [plan §12 — the spine](docs/00_MASTER_PLAN.md) |
| Where the work actually is | [`docs/PROGRESS.md`](docs/PROGRESS.md) — the v4 ledger |
| What each written day teaches | [`docs/WIKI.md`](docs/WIKI.md) |
| What is written and what is not | [`docs/TRACKER.md`](docs/TRACKER.md) |
| Why something is the way it is | [`docs/adr/`](docs/adr/) |

## The commands

A day is addressed by **its project and its day** — `01 7` is day 7 of project 01. There is no
global sitting number, because there is no global reading order: start at project 27 if you like.

```bash
python p.py status         # every project: written, complete, what is next
python p.py brief 01 7     # what that day must cover, and whether it is allowed yet
python p.py start 01 7     # open that day in reading order
python p.py depth 01 7     # check it against the depth contract
python p.py check          # the whole-repository gate
python p.py verify 01      # copy that project alone outside the repo and run its own check
python p.py done 01 7      # finish a day: refuses on an unticked checklist, then commits
python p.py doctor         # is this repository wired correctly?
```

`p.py` writes and checks the curriculum. It never builds or runs a project — **every project
carries its own `./run`**, and nothing under `projects/` imports from this root.

## How a day is written

A day is a **hub plus one document per subtopic**, never one long page. Each subtopic opens on a
scene from that project's industry — a loss adjuster with a photograph, a night supervisor with a
jammed line — and ends at the real-system version: what a senior writes instead, what degrades at
scale with a number, the review comment, the interview question.

Four rules make that more than an aspiration:

- **Code is printed, never referenced.** If a file exists in a finished project, some day in that
  project printed it whole, at its real path — `.gitignore` and `Dockerfile` included. `CODEMAP.md`
  is the proof, and a file with no day fails the check.
- **Every concept is taught in the project that uses it, at full depth.** No summaries, no "covered
  in another project", no pointers out. `python p.py check` greps for every form of escape.
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
days/       the teaching — one folder per project, one folder per sitting inside it
projects/   the forty systems, each a repository of its own
p.py        the whole authoring toolchain, one file, standard library only
granth.toml this repository's identity and the depth contract's knobs
```

`days/_archive-v3/` and `projects/_archive-v3/` hold the eighteen days written under the previous
plan, unedited and quarantined from every check. They were written to a contract v4 deleted;
[ADR-0006](docs/adr/ADR-0006-repetition-replaces-depth-once.md) says why, and
[ADR-0007](docs/adr/ADR-0007-v3-days-archived-and-the-restart.md) says what happened to them.

Start with `python p.py brief 01 0`.
