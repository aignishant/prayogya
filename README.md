# Prahari

**Building agentic AI systems in Python, from the transformer up to a client-ready platform:
models, agents, MCP, RAG, memory, multi-agent orchestration, trust, ops and plugins** — 137 days,
18 phases, 145 concepts, one artifact.

Prahari (प्रहरी, *the watchman*) is a curriculum that ends with something you can put in front of
a client. First you build a small transformer by hand and train, fine-tune, distil and specialise a
tiny language model on a laptop, so that nothing inside the bigger models is a mystery. Then you
build Prahari itself — a security-operations desk where alerts become cases, agents enrich them
through tools served over MCP, ask a retrieval pipeline you built chunk by chunk, remember what
happened last time, hand actions to a human for approval, and leave an audit trail — writing every
mechanism by hand before adopting the library that does it. Then you extract the reusable half into
a platform, `neev`, with the eval report as referee, and prove the platform by building a second,
unrelated application on it in eight days. Everything runs on free-tier model APIs and a CPU.

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
python granth.py status        # how many days are complete, and what is next
python granth.py brief N       # what day N must cover, and whether N is allowed yet
python granth.py start N       # open day N in reading order
python granth.py depth N       # check day N against the depth contract
python granth.py check         # the whole-repository gate
python granth.py done N        # finish a day: refuses on an unticked checklist, then commits
python granth.py doctor        # is this repository wired correctly?
```

## How a day is written

A day is a **hub plus one document per subtopic**, never one long page. Every subtopic document
opens where a reader who has never met the idea can stand and ends at the real-system version:
what breaks at scale, what a senior reviewer says, what an interviewer probes.

Three rules make that more than an aspiration:

- **No clocks.** No document carries a duration, an estimate or a pace. An explanation is never
  trimmed because a day is running long — the day gets another part instead.
- **Never invent a fact.** Versions, interfaces and citations are looked up live on the day they
  are used, with a dated ledger row. A failed lookup leaves the exact command, never a guess.
- **Every day ends with a check that can go RED**, and at least one part per day is a deliberate
  failure: break it, read the real error, fix it.

The full contract is [§11 of the plan](docs/00_MASTER_PLAN.md), and `python granth.py depth` enforces
the half of it a script can check.

## Layout

```text
docs/       the plan, the ledgers, the ADRs, the generated indexes
days/       the teaching — one folder per day
granth.py   the whole toolchain, one file, stdlib only
granth.toml this repository's identity and the contract's knobs
```

---

Scaffolded with [granth](https://github.com/aignishant/granth-skill).
