# ADR-0007 — The eighteen v3 days are archived unedited, and the curriculum restarts at P01 day 0

- **Date:** 2026-09-10
- **Day:** between v3 day 17 and v4 P01 day 0
- **Phase:** repository-wide
- **Status:** accepted
- **Amends:** nothing in the plan's contract. This ADR records what happened to work already done.
- **Related:** ADR-0006 (the reason), ADR-0002 (day zero and the authoring repo — superseded in
  effect, see below), ADR-0005 (the MCP era gap — still true and still owed)

## Context

Eighteen days were written under v3.1.0 and have rows in `docs/PROGRESS.md`: day 0 (the authoring
repository), days 1–3 (P00 Foundry), days 4–10 (P01 Ask Desk), days 11–17 (P02 Parts Counter,
through the client side). Three project trees were built alongside them — `01-ask-desk`,
`02-parts-counter` and a partial `03-triage-room` — and P01 and P02 both had green `./run check`
gates.

That work is not bad work. Much of it is the most verifiable material in the repository: P01's
`ask_desk/scripted.py` produces real ADK events with no key and no cost, and days 13–17 drive the
MCP handshake by hand over stdio and need no provider at all. The ledger notes on those days record
five real defects the writing process caught, and one left in place on purpose as a lesson.

But every one of those days is written to a contract v4 deletes. They carry curriculum IDs in their
frontmatter (`AG-03`, `MC-06`). They are numbered on a global spine that no longer exists — day 15
is meaningless once P02 starts again at day 0. Days 11 and after teach at *recap depth* and point
into P01 for the deep version. P01 and P02 each ship a `PRIMER.md`, which v4 abolishes. And P01 has
no MCP boundary at all, because v3 §11 says its second leg "arrives P02" — under the Full-Stack
Rule that is a project missing a subsystem.

Rewriting them in place was offered and declined. The learner's instruction on 2026-09-10 was
explicit: **"as of now we are creating all project from scratch everytime"**, and **"after that we
will start from project 1."**

## Decision

**The v3 work is moved, unedited, to two archive folders, and nothing in it is rewritten.**

```
days/_archive-v3/       00-foundry · 01-ask-desk · 02-parts-counter · _authoring
projects/_archive-v3/   00-foundry · 01-ask-desk · 02-parts-counter · 03-triage-room
                        _foundry-scratch  (the top-level foundry/ scratch file)
```

The move was made with `git mv`, so `git log --follow` still reaches every one of those days.

**`docs/PROGRESS.md` keeps its v3 table and every note under it, verbatim.** The ledger is
append-only and that rule does not bend for a restructure — least of all for one that supersedes
the rows, because a superseded row is the only evidence of what was superseded. A heading marks
where v3 ends, and the v4 ledger begins below it inside
`<!-- granth:ledger:start -->` markers, which is the only region `p.py` reads.

**The curriculum restarts at P01 day 0.** Not P00: under the From-Scratch Rule every project builds
its own machine, so a Foundry project that other projects lean on is exactly the shape v4 removes.
P00 survives as an **optional** five-sitting primer for a reader who has never set up a Python
toolchain, and plan §11 marks it clearly: *no project may reference it, and no project needs it.*

**The archive is quarantined from every check.** `p.py` ignores any folder under `days/` whose name
starts with `_`, so the archived days are never depth-checked against a contract they were not
written to, never counted in the tracker, and never reported as stale. They are read-only history.

**Nothing is carried forward automatically.** When P01 day 4 needs the ADK event model, it is
written fresh from the live documentation, not lifted from archived day 8. Two things may be reused
deliberately, and both must be re-run before use: a **verified transcript** (real command output
observed on a dated machine) and a **pinned version** already recorded in `docs/PINS.md`. Reusing a
transcript without re-running it would fabricate an observation, which Principle 7 forbids
regardless of where the text came from.

## Options considered

| Option | Why not |
| --- | --- |
| **Leave the eighteen days where they are and start v4 alongside** | Two contracts live in one `days/` tree. Every `p.py check` has to know which day obeys which rules, and the first reader to open `days/01-ask-desk/day-08-…` gets a document written to a deleted standard with no sign saying so. |
| **Delete them** | Offered and declined, correctly. They contain observations that cost real time to produce — a live `400 INVALID_ARGUMENT`, a Windows `Access is denied` from `uv sync` inside `uv run`, the `RunConfig.max_llm_calls` correction that day 7 got wrong and day 8 caught. Deleting the folder does not delete the git history, but it does delete the chance of anyone reading it. |
| **Rewrite the three projects in place to the v4 contract** | Offered and declined. It is not an edit: P01 gains a boundary, a cast, memory, security, observability and evals it never had, and grows from 7 days to 20. That is writing P01 from scratch while carrying the burden of matching old folder names and old numbering. |
| **Keep day 0, the authoring-repo day, live** | It teaches building the v3 `p.py` — the ID parser, the global day map, the traceability generator. v4's driver has none of those. The day is now a description of a program that no longer exists, which is worse than no day. It is archived, and ADR-0002 stands as the record of why day 0 existed. |

## Consequences

**Better.** One contract governs everything `p.py` checks. The v4 tree starts empty, so the first
green `check` is a real signal rather than a negotiated one. The archive is honest about its own
status: superseded, unedited, dated.

**Worse.** Eighteen sittings of finished teaching no longer count toward the curriculum, and the
tracker will read 0 of 816 on the day this lands. The learner rebuilds Ask Desk from day 0, and
will type things they have typed before. That is the second time the same material has been
written, and the ADR-0006 bill is what makes it worth it — but the sunk work is real and should not
be described as anything else.

**The new failure mode is quiet reuse.** The archived days are right there, and lifting a paragraph
or a transcript out of one is a two-second operation that leaves no trace. What catches it: only
the writing procedure — `.claude/skills/day-prayoga/SKILL.md` step 2 requires every fact, version
and transcript to be verified live on the day it is written, and a transcript that was not re-run
is a fabricated observation whatever its provenance. There is no mechanical check for this and
claiming one would be the same kind of dishonesty.

**What is still owed, and survives the archiving.** ADR-0005's finding is unaffected by any of
this: the current MCP specification revision is `2026-07-28`, it removed the `initialize`
handshake and protocol-level sessions, and `google-adk` 2.8.0 declares `mcp<2`, so the stack this
curriculum can run cannot speak the current revision. Every v4 project has a boundary, so every v4
project inherits that gap, and plan §10's freshness check is where each project re-reads it rather
than assuming this ADR is still current.

**What would have to be true to revisit this.** If v4 is itself superseded, the same procedure
applies and this ADR is the precedent: move, do not delete; keep the ledger; quarantine from the
checks; carry nothing forward that was not re-verified.
