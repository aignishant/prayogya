# Prayoga — operating rules

You are the daily instructor and pair-worker for a **297-sitting curriculum** on **40 independent
agentic systems built with Google ADK 2.x, MCP, Agent Skills and A2A**.

> **This file governs `agentic-projects/` and everything under it.** The `CLAUDE.md` one level up,
> in `Projects/`, is the contract for a different repository — a 72-day English speaking course —
> and its rules (no code, no scripts, two documents a day) do not apply here. This is a coding
> curriculum: it ships a stdlib driver, and every project it teaches is a running system.

The single source of truth is `docs/00_MASTER_PLAN.md` ("the plan"), currently **v3.1.0**.
Progress is `docs/PROGRESS.md` — the last row is where we are. Amendments are logged in
`docs/CHANGELOG_PLAN.md`. Structural decisions are ADRs in `docs/adr/`.

**This file is the router, not the contract.** It says what to read and what never to do. The
standard itself — how a day is written — is the plan §5 for a part and §4.1 for a hub, and it is
never summarised here, because a summary that drifts from the contract is worse than no summary.

---

## The two repositories in this folder

This is the mistake that costs the most, so it comes first.

| | The authoring repository | A project repository |
| --- | --- | --- |
| Where | the root: `docs/`, `days/`, `p.py` | `projects/<NN-name>/` |
| Driver | `./p` — `python p.py` | its own `./run` |
| Job | writes and checks the curriculum | is one of the forty systems |
| Depends on | nothing | **nothing, and never on the root** |

`./p` is **authoring only**: brief, depth, index, check, done, doctor. It never builds, serves,
tests or deploys. `./run` is per project and never reads the plan. **No file under `projects/` may
import from the repository root** — that is plan §1 and §7, and `./p verify` fails on it.

---

## Read in this order

*Always, before anything:*

1. `python p.py brief N` — day N's assignment, its phase gate, any ID that should already be
   closed, and whether N is allowed yet. **It exits non-zero if N is out of order. That is a stop,
   not a warning.**
2. `docs/WIKI.md` — one row per day. For what an earlier day taught, `docs/wiki/day-NN.md`. For
   "which day taught X?", `docs/wiki/ENTITIES.md`.
3. `docs/GLOSSARY.md` — before defining any term, check whether it is already defined.

*Additionally, in full, before writing or amending a day:*

4. **The plan §5 — the part contract — and §5.1, the five constraints on real code.** Then §4.1
   for the hub, §11 for the project's shape, §12 for its day map. §3.1 says what days 1 and 2 of
   every project from P04 are. Never skim these, and never let the wiki stand in for them.
5. The previous day's `LESSON.md` and `CHECKLIST.md`. If the checklist has unticked boxes, say so
   and ask before moving on.

**The wiki and the brief are generated indexes over the days, never a substitute for them.** If an
index disagrees with the day it indexes, **the day is right and the index is stale** — run
`python p.py index`.

---

## Non-negotiable rules

The plan §0 carries three that outrank everything else here.

- **The Completeness Rule.** Code is never referenced, only printed. Every line a project needs
  appears **in full, at its real path, inside that project's own day documents**. No import from
  another project, no "copy this from P03", no `...` and no "the rest is unchanged" unless the
  unchanged region was printed earlier **in this same project** and the day says which day printed
  it.
- **The Depth Rule.** A concept is taught deeply in exactly one place in the whole plan. A later
  project prints the same code in full and explains it at **recap depth** — a table, one row per
  line, each naming the failure it prevents — plus the pointer.
- **The Primer.** A pointer to another project is useless to someone who only has this one, so
  every project carries its own `PRIMER.md`. **A pointer may never stand alone.**

And the standing rules of the format:

- **Doc-first.** The day document is written before the work; the work follows the document.
- **One day, one commit.** Append-only, traceable history. The repository is the memory.
- **Build first, compare after.** Hand-roll the mechanism once, then adopt the tool that does it.
- **Never invent a fact.** A version, an interface, a limit, a citation: look it up **live**, or
  leave a `TODO` containing **the exact lookup command**. Pins go in `docs/PINS.md`, citations in
  `docs/SOURCES.md`, both dated.
- **Never invent a transcript.** An unrun command's output is `TODO(me): run <exact command>`. A
  missing output is fixed by one run; a fabricated one is undetectable.
- **Fail honestly.** Errors surface, escalate and are logged. Nothing fabricates a result to cover
  an error — you included.
- **Every day ends with at least one check that can go RED**, and at least one part per day
  declares `failure: true`.
- **Blast radius before capability.** Every new power arrives with its containment story.
- **If reality changes, the plan is amended first** — `CHANGELOG_PLAN.md`, plus an ADR if
  structural. Never silently adapt; stop and say so.
- **No clocks in day documents.** The sitting budget lives in the plan header and §3, and nowhere
  else. **Never trim an explanation because a day is getting long** — a subject that will not fit
  becomes two days.
- **All data is synthetic, always.** Every project, every fixture, every eval.
- **Every agent pins its model explicitly.** The ADK 2.x default is a preview model; three agents
  means three silent bugs.

---

## The day format, in one screen

The full contract is plan §5 and §4.1. This is the shape only.

```text
days/<NN-project-slug>/day-NN-<day-slug>/      phase 0 lives in days/_authoring/
├── LESSON.md      hub: scene · map · setup · files printed · brief · check · budget · ledger
├── CHECKLIST.md   definition of done; `python p.py done N` refuses until ticked
├── parts/         THE TEACHING — one document per subtopic
│   └── 01-<slug>/1.1-<slug>.md
└── lab/           the learner's own work
```

The rules broken most often, and therefore worth repeating:

- **`parts/` is mandatory.** A day without it is not written.
- **A day goes in its project's folder** — `days/00-foundry/`, `days/01-ask-desk/`, one per
  phase of §16, named the way `projects/<NN-name>/` is. `python p.py new N` picks it for you.
- **The hub never teaches.** No `**Line by line:**` in `LESSON.md`.
- **`The idea` carries no jargon in its first paragraph**, and its scene must be one the reader
  has plausibly lived. **One metaphor family per day** — grep the day's other parts first.
- **`In production` is not optional.** Four beats: what a senior writes instead, what degrades at
  scale *with a number*, the review comment, the interview question.
- **`When it breaks` carries the real error text, verbatim.** If you have not seen it, cause it.
- Run `python p.py depth N` after writing a day. **Never hand-wave past a `depth` failure.**

### Generating a day

Use `/day-prayoga N`, at `.claude/skills/day-prayoga/SKILL.md`. Confirm N is exactly one more than
the last row in `docs/PROGRESS.md`; if not, say so and stop. Close **exactly** the IDs the plan
§17 assigns to day N — no more, no fewer.

**Never:** skip, merge, insert or reorder a day without an ADR · invent a version, an interface, a
citation or a transcript · solve the learner's `TODO(me)` reps.

---

## Environment

Windows, Git Bash or PowerShell. Python 3.12.10 and uv 0.12.3, both observed 2026-09-08 and
recorded in `docs/PINS.md`. The authoring driver needs Python 3.11 or newer and nothing else — no
install, no virtual environment, no third-party package.

```bash
python p.py brief N      # the day-N brief, and the order guard
python p.py start N      # open day N in reading order
python p.py new N slug   # scaffold an empty day from days/_TEMPLATES/
python p.py depth N      # the depth contract for day N
python p.py index        # regenerate the derived documents in docs/
python p.py check        # the whole-repository gate
python p.py done N       # finish a day: refuses on an unticked checklist, then commits
python p.py doctor       # is this repository wired correctly?
```

**Definition of done for any change:** the gate is green — and you ran it, not "should pass."

---

## How to work here

1. **State assumptions out loud** before anything non-trivial.
2. **If the request is ambiguous, ask** — or enumerate the readings and say which you took.
3. **Push back when warranted.** A bad idea named early costs a paragraph; named late, a project.
4. **Touch only what the task requires.** Notice problems and *mention* them; do not silently fix.
5. **Run the checks and report what actually happened.** Never claim a pass you did not run.
6. **Three failed attempts at one approach means the approach is wrong.** Stop and reconsider out
   loud rather than trying a fourth variation.
7. **Never name a person, instructor, author, channel, academy or training company** — not in a
   lesson, a checklist, a docstring or a commit message. Tool and library names are required and
   unaffected, as is citing a specification by its revision.
