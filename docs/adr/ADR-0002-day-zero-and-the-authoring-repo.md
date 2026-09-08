# ADR-0002 — Day zero builds the authoring repository, and sits outside every project

- **Date:** 2026-09-08
- **Day:** 0
- **Phase:** 0
- **Status:** accepted
- **Amends:** v3.1.0 — inserts day 0 ahead of P00, so the curriculum runs 0 to 296
- **Related:** ADR-0001

## Context

The plan section 6 says `./p check` enforces the depth contract. Section 7 says `./p verify` proves
a project independent. Section 13 recommends keeping `./p` as an authoring tool with five
commands. Three sections depend on a driver, and no day in section 12 builds one.

The same is true of everything around it. Section 10 says the freshness check is recorded in a
ledger; no day creates the ledger. Section 8 says a day map assigns IDs; no day writes the day map.
Section 1 says the top-level `./p` exists but that no project depends on it — which is correct and
also means no project day can be the one that builds it, because that would make P00 a dependency
of the authoring layer and invert the whole arrangement.

Read literally, the plan starts at P00 day 1: *The machine — uv, Python 3.12, and the four Pythons
that ruin a Monday.* That is a **project** day. It sets up the Foundry reference project. It does
not create `docs/PROGRESS.md`, and P00 cannot be closed without one, because closing a day means
appending a row to a ledger that does not exist.

The plan forbids inserting a day without an ADR. This is that ADR.

## Decision

**Day 0 is the authoring repository: the toolchain, the repository skeleton, and the `./p` driver.**

It sits in phase 0, which is the only phase that is not a project. It closes `RB-01`, `RB-02` and
`RB-03` — the only IDs on the repository track that are not the final day of the capstone. P00
Foundry now begins at day 1, and the curriculum runs 0 to 296: **296 project sittings, 297 total.**

**No project day moved.** P00 always began at the first sitting after a repository existed to hold
it; that sitting simply had no number before.

The load-bearing half is the boundary between the two drivers, and it is stated in day 0 part 3.1:

- **`./p` is authoring only.** It reads the plan, checks the depth contract, regenerates the
  indexes, guards the order of days, and refuses to close a day whose checklist is unticked. It
  never builds, serves, tests or deploys anything.
- **`./run` is per project.** Every project carries its own. It lints, tests, serves the agent,
  runs the boundary, runs the evalset. It never reads the plan and never imports `p.py`.

Nothing in `projects/` may import from the repository root. That is the section 1 rule and day 0
is where it is first enforceable, because day 0 is where the root gets code in it at all.

## Options considered

| Option | Why not |
| --- | --- |
| **Do nothing — fold the toolchain into P00 Foundry day 1** | P00 is a project, and section 1 says the top-level `./p` is a tool no project depends on. Building `./p` inside P00 makes the authoring layer a product of a project, which is exactly backwards, and it breaks the Foundry cold-clone: a stranger taking `projects/00-foundry/` would get a driver for a plan they do not have. |
| **Number it day 1 and shift every project day by one** | Renumbers 296 rows to avoid a zero. Section 12 and every "on day 137 we will" reference would move, and the ADR would be recording a renumbering rather than an insertion. A day 0 that closes setup IDs and no subject IDs is the honest shape, and it is what the numbering-from-zero rule exists for. |
| **Leave the toolchain unversioned and outside the curriculum entirely** | Tempting: it is infrastructure, not subject matter. But then the one repository that checks forty others is the only thing here with no day document, no ledger row and no deliberate failure — and the first person to change `p.py` would have nothing to read. The layer that enforces the standard has to meet it. |
| **Call the driver `granth.py`, matching the sibling curricula** | Muscle memory across repositories is worth something. But sections 6 and 13 of this plan name `./p` and give it five commands, and a plan that names a tool the repository does not have is the drift this whole adoption exists to prevent. The file is `p.py`; the plan was right first. |

## Consequences

- **Better:** every claim in sections 6, 7 and 13 is now backed by a file that exists. The order
  guard works from the first sitting, so P00 day 1 cannot be written before day 0 is in the
  ledger. The forty projects still depend on nothing.
- **Worse:** the curriculum is one sitting longer, and the plan header number 296 now needs the
  qualifier "project sittings". A reader who remembers 296 and counts 297 has to be told why —
  section 14 tells them.
- **Also worse:** day 0 teaches a script the reader did not write and will not extend. It is the
  only day in the curriculum where the code being read is infrastructure rather than subject, and
  that is a genuine oddity in a practice-first plan. It is accepted because the alternative is a
  reader who runs `p.py depth` for 296 days without ever having seen inside it.
- **New failure mode:** `p.py` and the plan can disagree — a contract knob changed in
  `granth.toml` that section 5 does not mention. What catches it is that `depth --list` prints the
  contract as configured, and day 0 part 3.3 makes reading that output a step.
- **Revisit if:** the five-command surface in section 13 grows product commands. That would mean
  `./p` had started doing a project's job, and the boundary this ADR draws would need redrawing
  rather than quietly widening.
