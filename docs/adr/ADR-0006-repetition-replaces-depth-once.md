# ADR-0006 — Every project teaches everything it uses, in full, in its own documents

- **Date:** 2026-09-10
- **Day:** between v3 day 17 and the start of v4 P01
- **Phase:** repository-wide — this ADR is the reason v4.0.0 exists
- **Status:** accepted
- **Amends:** v3.1.0 → v4.0.0. Rewrites §0, §2, §3, §4, §5, §6, §8, §11, §12, §15, §16 and §17.
  Deletes the ID scheme, the track table, the global day map and `PRIMER.md`.
- **Related:** ADR-0001 (the plan as adopted), ADR-0003 (days grouped by project),
  ADR-0007 (the v3 days are archived and the curriculum restarts at P01)

## Context

v3.0.0 deleted `_shared/adk_kit/` so that no project would import from another. That fixed the
*code* half of independence and left the *teaching* half broken, and the learner said so on
2026-09-10, in the plainest possible terms: **"the project files which we setup on one project
that not have in other, like git setup or agent setup or any other file — so how i can say all
project are not related to each other."**

They are right, and the evidence is in the repository as it stands, not in an argument.

**One.** v3 §0 carries a rule called the Depth Rule: *"Deep teaching of a concept lives in exactly
one place in the whole plan. A later project prints the same code in full, explains it at recap
depth — a short table, one line per function, plus the failure it prevents — and gives the pointer
to the deep version."* Recap depth is a table. A table is not a teaching. Someone who opens
`projects/22-writer-and-critic/` and has never seen P02 gets four table rows and a path into a
folder they do not have.

**Two.** v3 invented `PRIMER.md` to patch exactly this hole — six to ten lines per borrowed concept,
"a self-contained working understanding". Six to ten lines is a definition, not an understanding.
The primer's own existence is the admission that the pointer does not carry.

**Three.** The scaffolding a project needs to exist at all was never in the project. v3 §2.4 says
`SETUP.md` is *"a listing, not a lesson — day 01 explains the parts that matter, and
`projects/00-foundry/` holds the deep version for anyone who wants it."* So the git setup, the
`.gitignore` written before `.env` exists, the Python pin, the key handling — the four things that
decide whether a stranger's clone runs at all — live in a project nobody is required to read.
`projects/02-parts-counter/PRIMER.md` currently points at `PRIMER.md` §1 of P01 because the file
was copied from P01 and the section numbers moved. That drift was caught, printed as a lesson, and
deliberately left in place on day 11. It is a small bug and a large symptom.

**Four.** The ID scheme bound days to a global spine — `MC-04` belongs to day 15 and to no other
day — which is the same idea as the Depth Rule wearing a different hat. An ID assigned to exactly
one day in a curriculum of forty independent repositories is a statement that the other
thirty-nine do not teach it.

Left alone, the cost compounds per project. Every project written under v3 adds one more repository
whose day documents cannot be read alone, and each one is six to nine sittings of work to unpick.
Eighteen days exist. Forty projects do not.

## Decision

**A project teaches, at full depth, in its own day documents, every concept it uses.** Repetition
between projects is required, not tolerated. Four rules replace v3's three, and they are stated in
plan §0 in this order because that is their precedence.

1. **The Completeness Rule** *(kept, and widened).* Every line of code a project needs appears in
   full, at its real path, inside that project's own day documents — and "code" now includes
   `.gitignore`, `pyproject.toml`, `.env.example`, `Dockerfile`, `compose.yaml`, the CI workflow
   and the `run` driver. If a file exists in the finished project, some day in that project printed
   it whole.

2. **The Repetition Rule** *(new — this replaces the Depth Rule).* Every concept a project uses is
   taught in that project at full depth: the scene, the mechanism, the line-by-line walkthrough,
   the real failure, the production note. There is no recap depth. There is no "taught deeply
   elsewhere". If forty projects need honest 429 handling, honest 429 handling is taught forty
   times, and the fortieth telling is better than the first because it has thirty-nine domains of
   evidence behind it.

3. **The From-Scratch Rule** *(new).* Every project begins on a bare machine and an empty
   directory. Day 0 installs the toolchain, pins the interpreter, runs `git init`, writes
   `.gitignore` before any secret exists, handles keys, and reaches a green check. Day 1 builds the
   skeleton and the kit. No project may assume a machine another project prepared.

4. **The Full-Stack Rule** *(new).* Every project ships the whole agent feature set — its own tools,
   its own MCP boundary, its own multi-agent cast, callbacks, sessions and memory, structured
   output, reliability, security, observability, evals and deploy. A project that omits a subsystem
   because "another project covers it" is the v3 failure in a new costume. Plan §12 fixes the
   eighteen subsystems as a spine every project builds.

**No pointer leaves a project.** No day document, checklist, docstring, README or commit message in
`projects/<NN-name>/` may reference another project — not by path, not by name, not as "as we saw
in P03". `python p.py check` fails on it. This is the load-bearing half of the decision: without a
mechanical check, the rule is a preference, and preferences drift by project six.

**`PRIMER.md` is deleted**, along with the *Borrowed concepts* table in `PROJECT.md`. Both existed
only to make an out-of-project pointer survivable. There are no out-of-project pointers now.

**Days are numbered inside their project, from 0.** P01 runs day 0 to day 19; P02 starts again at
day 0. The global sitting number, the phase table and the 310 curriculum IDs are deleted with it.
A day is addressed as a project and a day: `python p.py brief 01 7`.

**Projects are renamed to their real-world problem** and resized to 16–22 days, because a project
that carries the full feature set from scratch is not a seven-day project. Plan §11 lists the
forty; §13 gives each one its day map.

## Options considered

| Option | Why not |
| --- | --- |
| **Keep v3 — the Depth Rule plus `PRIMER.md`** | It is the thing that failed. The learner cannot take one project folder to one machine and learn from it, which is the property the whole plan claims. Keeping it means writing thirty-eight more repositories with the same hole. |
| **Keep the Depth Rule, make the primer longer** | A primer long enough to actually teach a concept *is* the full teaching, at which point it is a day document filed under the wrong name and outside the day sequence. This option is the decision, badly organised. |
| **A shared `_shared/` library again, honestly documented** | This is v2, and v3 §0 already recorded why it was wrong: `ModuleNotFoundError: adk_kit` for anyone with one folder. Reversing it would trade a teaching gap for a code gap. |
| **Fewer, larger projects — ten repositories of forty days** | Genuinely reduces repetition, and was offered. Rejected by the learner on 2026-09-10: forty domains is the point, because a reader picks the project whose industry is theirs. |
| **Repetition, but only for scaffolding; keep depth-once for deep concepts** | The line between "scaffolding" and "deep concept" has to be drawn by someone, per project, every time — and every drawing of it is a chance to leave a hole. A rule with a judgement call in the middle is not checkable, and an uncheckable rule is what produced the P02 primer drift. |

## Consequences

**Better.** A stranger with one project folder can build and understand the whole system from that
folder's documents. `python p.py check` can prove it, because "no reference leaves the project" is
a grep, not a review. The learner can pick project 27 first. Each retelling of a concept is
domain-specific — 429 backoff in a payments system and 429 backoff in a triage desk have different
consequences, and teaching it twice is teaching two things.

**Worse, and this is the real bill.** The curriculum roughly triples: v3 was 297 sittings, v4 is
816 across 41 folders. Roughly 400 lines of scaffolding get typed forty times, and every core
concept gets written forty times at full depth rather than once. Writing a day is more expensive
than it was, because nothing can be discharged with a pointer. **This is the cost the learner was
shown and accepted** on 2026-09-10, choosing 16–22 days per project over 9–12 and over twenty
larger projects.

**The new failure mode is drift between retellings.** By P30 the backoff teaching will be sharper
than P06's, and P06 will never get the improvement. v3 named this as a cost of code duplication;
v4 extends it to prose. What catches it: nothing automatic, and pretending otherwise would be
worse. What is done instead — each project's ship day carries a short *what I would change if I
wrote this again* note, which turns the drift into a dated record of the learner's own progress
rather than a defect nobody can see.

**The second new failure mode is boredom, and it is not hypothetical.** Forty tellings of the
session model is forty chances to write the same document. The defence is in plan §14: the scene,
the failure and the production note must come from *this project's domain*, and a part whose scene
would work unchanged in another project has failed its own contract.

**What would have to be true to revisit this.** If the learner ever wants the whole curriculum read
front to back in order, rather than sampled, the repetition becomes a cost with no matching
benefit, and the Depth Rule comes back for that reading order only. Nothing in v4 forecloses it:
each project remains a complete text, and a front-to-back reader is free to skim what they have
seen. The reverse — recovering independence from a plan built on pointers — is what this ADR is
paying for, and it is expensive.
