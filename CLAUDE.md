# Prayoga — operating rules

You are the daily instructor and pair-worker for a curriculum of **40 independent agentic systems**
built with **Google ADK 2.x, MCP, Agent Skills and A2A**. Every project is a standalone repository,
taught from zero, carrying the whole agent feature set.

> **This file governs `agentic-projects/` and everything under it.** The `CLAUDE.md` one level up,
> in `Projects/`, is the contract for a different repository — a 72-day English speaking course —
> and its rules (no code, no scripts, two documents a day) do not apply here. This is a coding
> curriculum: it ships a stdlib driver, and every project it teaches is a running system.

The single source of truth is `docs/00_MASTER_PLAN.md` ("the plan"), currently **v4.0.0**.
Progress is `docs/PROGRESS.md` — the last row of its **v4 ledger**. Amendments are logged in
`docs/CHANGELOG_PLAN.md`. Structural decisions are ADRs in `docs/adr/`.

**This file is the router, not the contract.** It says what to read and what never to do. The
standard itself — how a day is written — is the plan §5 for a part and §4.1 for a hub, and it is
never summarised here, because a summary that drifts from the contract is worse than no summary.

---

## Read this first: v4 inverted the rule about repetition

If you have seen this repository before, the thing that changed is the thing that matters.

**v3 taught each concept deeply once and pointed at it from everywhere else.** v4 deletes that.
**Every project teaches everything it uses, at full depth, in its own documents.** Repetition
between projects is *required*. `PRIMER.md`, the curriculum ID scheme (`AG-01`, `MC-04`), the track
table and global day numbering are all gone. Days are numbered **inside their project, from 0**.

The eighteen v3 days are archived unedited in `days/_archive-v3/` and `projects/_archive-v3/`.
**Do not read them for material and never lift a transcript out of one** — every fact is verified
live on the day it is written. See `docs/adr/ADR-0006` and `ADR-0007`.

---

## The two repositories in this folder

This is the mistake that costs the most, so it comes first.

| | The authoring repository | A project repository |
| --- | --- | --- |
| Where | the root: `docs/`, `days/`, `p.py` | `projects/<NN-name>/` |
| Driver | `python p.py` | its own `./run` |
| Job | writes and checks the curriculum | is one of the forty systems |
| Depends on | nothing | **nothing, and never on the root** |

`python p.py` is **authoring only**: brief, depth, index, codemap, check, verify, done, doctor. It
never builds, serves, tests or deploys. `./run` is per project and never reads the plan. **No file
under `projects/` may import from the repository root** — that is plan §1 and §7.

---

## Read in this order

*Always, before anything:*

1. `python p.py brief NN D` — day D of project NN: its assignment, its spine slot, what this
   project has already printed, and whether D is allowed yet. **It exits non-zero if D is out of
   order inside its project. That is a stop, not a warning.**
2. `docs/WIKI.md` — one row per written day, grouped by project. For a day's parts,
   `docs/wiki/PNN-day-DD.md`.
3. `docs/GLOSSARY.md` — before defining any term, check whether it is already defined.

*Additionally, in full, before writing or amending a day:*

4. **The plan §5 — the part contract — and §5.1, the five constraints on real code.** Then §4.1 for
   the hub, §12 for the spine slot this day is, §13 for this project's brief and its extra days,
   and §14 for the style rules that stop forty projects reading like one project pasted forty
   times. Never skim these, and never let the wiki or the brief stand in for them.
5. The previous day **of this same project** — its `LESSON.md` and `CHECKLIST.md`. If the checklist
   has unticked boxes, say so and ask before moving on.

**The wiki and the brief are generated indexes over the days, never a substitute for them.** If an
index disagrees with the day it indexes, **the day is right and the index is stale** — run
`python p.py index`.

---

## Non-negotiable rules

The plan §0 carries four that outrank everything else here.

- **The Completeness Rule.** Every line of code a project needs appears **in full, at its real
  path, inside that project's own day documents** — `.gitignore`, `pyproject.toml`, `Dockerfile`
  and the `run` driver included. No `...` and no "the rest is unchanged" unless the unchanged
  region was printed earlier **in this same project** and the day says which day printed it.
- **The Repetition Rule.** Every concept a project uses is taught **in that project, at full
  depth** — scene, mechanism, line-by-line, real failure, production note. There is no recap depth
  and no "taught deeply elsewhere". Writing it for the fortieth time is the job, not a failure.
- **The From-Scratch Rule.** Day 0 assumes nothing: toolchain, `git init`, `.gitignore` before
  `.env` exists, keys, green check. **No project may assume a machine another project prepared.**
- **The Full-Stack Rule.** Every project ships the whole feature set — the eighteen spine slots of
  plan §12. A project that omits one because another project covers it is the v3 failure again.
- **Nothing leaves the project.** No day document, checklist, docstring, README or commit message
  inside a project may reference another project — not by path, not by name, not as "as we saw".
  `python p.py check` greps for it and fails.

And the standing rules of the format:

- **Doc-first.** The day document is written before the work; the work follows the document.
- **One day, one commit.** Append-only, traceable history. The repository is the memory.
- **Build first, compare after.** Hand-roll the mechanism once, then adopt the tool that does it.
- **Never invent a fact.** A version, an interface, a limit, a citation: look it up **live**, or
  leave a `TODO` containing **the exact lookup command**. Pins go in `docs/PINS.md`, citations in
  `docs/SOURCES.md`, both dated.
- **Never invent a transcript.** An unrun command's output is `TODO(me): run <exact command>`. A
  missing output is fixed by one run; a fabricated one is undetectable. **This applies to text
  copied out of the v3 archive**: if it was not re-run today, it was not observed today.
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
- **Every agent pins its model explicitly.** The ADK 2.x default is four generations old; three
  agents means three silent bugs.

---

## The day format, in one screen

The full contract is plan §5 and §4.1. This is the shape only.

```text
days/<NN-project-slug>/day-DD-<day-slug>/       DD is the day number INSIDE its project, from 0
├── LESSON.md      hub: scene · map · setup · files printed · brief · check · budget · ledger
├── CHECKLIST.md   definition of done; `python p.py done NN D` refuses until ticked
├── parts/         THE TEACHING — one document per subtopic
│   └── 01-<slug>/1.1-<slug>.md
└── lab/           the learner's own work
```

The rules broken most often, and therefore worth repeating:

- **`parts/` is mandatory.** A day without it is not written.
- **The hub never teaches.** No `**Line by line:**` in `LESSON.md`.
- **`The scene` and `The idea` open on a scene from *this project's industry*.** Plan §14: a scene
  that would work unchanged in another project has failed its own contract. This is the whole
  defence against forty near-identical documents, so treat it as a hard test.
- **One metaphor family per day** — grep the day's other parts first.
- **`In production` is not optional.** Four beats: what a senior writes instead, what degrades at
  scale *with a number from this industry*, the review comment, the interview question.
- **`When it breaks` carries the real error text, verbatim**, from this project's code. If you have
  not seen it, cause it.
- Run `python p.py depth NN D` after writing a day. **Never hand-wave past a failure.**

### Generating a day

Use `/day-prayoga NN D`, at `.claude/skills/day-prayoga/SKILL.md`. Confirm D is exactly one more
than the last day of project NN in the v4 ledger; if not, say so and stop. Order **inside** a
project is strict; order **between** projects is free — starting a new project is always allowed.

**Never:** skip, merge, insert or reorder a day inside a project without an ADR · invent a version,
an interface, a citation or a transcript · reference another project · solve the learner's
`TODO(me)` reps.

---

## Environment

Windows, Git Bash or PowerShell. Python 3.12.10 and uv 0.12.3, both observed 2026-09-08 and
recorded in `docs/PINS.md`. The authoring driver needs Python 3.11 or newer and nothing else — no
install, no virtual environment, no third-party package.

```bash
python p.py brief NN D     # the brief for day D of project NN, and the order guard
python p.py start NN D     # open that day in reading order
python p.py new NN D slug  # scaffold an empty day from days/_TEMPLATES/
python p.py depth NN [D]   # the depth contract for one day, or a whole project
python p.py codemap NN     # regenerate that project's CODEMAP.md
python p.py index          # regenerate the derived documents in docs/
python p.py check          # the whole-repository gate
python p.py verify NN      # copy that project alone outside the repo and run its own check
python p.py done NN D      # finish a day: refuses on an unticked checklist, then commits
python p.py doctor         # is this repository wired correctly?
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
