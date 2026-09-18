# ADR-0001 — The plan as adopted

- **Date:** 2026-09-18
- **Day:** before day 0
- **Phase:** —
- **Status:** accepted
- **Amends:** nothing — this is the founding record
- **Related:** `docs/00_MASTER_PLAN.md` v1.0.0

## Context

This repository teaches **building agentic AI systems in Python, from the transformer up to a
client-ready platform: models, agents, MCP, RAG, memory, multi-agent orchestration, trust, ops and
plugins** over 137 days, and it exists because the obvious alternatives do not work:

- **Following a course** produces something that runs and understanding that evaporates the moment
  the inputs change. There is no artifact to defend and no record of why anything is as it is.
- **Reading documentation** covers the surface in the order the documentation was written, which
  is the vendor's order and not a learner's. Nothing forces the ideas to connect.
- **Building a project with no plan** teaches whatever the project happened to need, leaves the
  gaps invisible, and cannot tell a thin subject from a missing one.

The plan answers all three: a fixed day-to-concept map, so gaps are visible; one artifact, so every
concept is load-bearing; and a depth contract, so a subject is either covered properly or
mechanically flagged as not covered at all.

The learner is a working Python developer on a security-orchestration product who is new to
generative and agentic AI, wants to be able to build agentic systems for clients afterwards, and
has free-tier model access and a CPU laptop. Each of those four facts shaped a decision below.

The decisions below were taken at the start, together, because each is expensive to change once
days exist.

## Decision

**v1.0.0 of `docs/00_MASTER_PLAN.md` is adopted as the single source of truth.** In
particular:

| Decision | As adopted | Why this and not the alternative |
| --- | --- | --- |
| **Scope** | 137 days, 18 phases, 145 concept IDs across 10 tracks | Two artifacts (an application, then the platform extracted from it) plus a second application as proof, on top of a foundations phase and a model-internals phase for a learner new to the field. Fewer days would mean either dropping the model internals — which a client will ask about — or merging the hand-rolled days into their library days, which is the tutorial ceiling this plan exists to avoid. |
| **The artifact** | Prahari, a security-operations desk built mechanism by mechanism; `neev`, the platform extracted from it; Sahayak, a support desk built on `neev` in eight days as the proof; and a tiny language model trained and specialised by hand first | One artifact makes Principle 4 checkable: delete a concept and see whether the artifact still works. The security domain is the learner's own, so every `In production` section can be checked against real experience. |
| **Order** | Foundations → model internals → the agent loop by hand → the domain → MCP → retrieval → memory → orchestration → trust → ops → plugins → extraction → the second vertical | Principle 3 at the scale of the whole curriculum. The platform is extracted *after* the application works, so it abstracts things that exist rather than things that were imagined. The model is built by hand *before* any API is called, so the API is never a black box. |
| **Day format** | A hub plus one document per subtopic (plan §11) | A single-file day silently becomes a wall of text under one heading. A reader cannot revisit one idea without re-reading four, and nothing distinguishes a thin subtopic from a missing one. |
| **No clocks** | No duration, estimate or pace in any document (Principle 11) | A duration field silently authorises the worst edit in technical writing: cutting an explanation because the day is running long. |
| **Verification** | Versions, interfaces and citations looked up live, with dated ledger rows (Principle 6) | Notes written from memory rot silently. A citation written from memory rots most silently of all. The MCP specification moved to revision 2026-07-28 and the `mcp` SDK to a reworked 2.x between when a plan from memory would have been written and today — found by looking, not by remembering. |
| **Constraints** | Free-tier Groq, Gemini and OpenRouter keys; a CPU laptop; SQLite for all state; `uv` + `ruff` + `mypy` + `pytest`; Windows with PowerShell | A constraint written down is a curriculum. A constraint discovered on day 40 is a rewrite. The request caps in particular moved two concepts — retry on 429 and recorded responses — from "later" to days 26 and 28. |
| **Numbering from 0** | Day 0 is setup and closes no IDs | A setup day that claims IDs makes every later count wrong. |
| **Failure days** | Each phase carries at least one whole day whose subject is a deliberate failure, over and above the failure part every day carries | In this domain the failure *is* the lesson: a poisoned alert, a lying tool, a remembered lie, two agents arguing forever, a plugin that reaches too far. A part is not enough room for them. |

## Options considered

| Option | Why not |
| --- | --- |
| **No plan — build and see what comes up** | Teaches whatever the project happened to need. Gaps stay invisible, and there is no way to tell a subject covered thinly from one skipped entirely. |
| **A topic list instead of a day map** | A list has no order and no gate, so nothing ever has to work. The day map is what makes "am I allowed to start day 27?" a mechanical question. |
| **One file per day** | The format this plan explicitly replaces — see the day-format row above. |
| **A shorter curriculum** | Fewer days helps only if the subject is smaller. Trimming days without trimming scope is Principle 11's failure mode with extra steps. |
| **A horizontal platform first, applications after** | Considered and rejected: a platform built before an application abstracts the wrong things. The extraction phase exists so the platform is pulled out of something that already works. |
| **A single vertical with no extraction** | Would teach the domain well and the reuse not at all; the learner's stated goal is to build for *any* client. |
| **Skip the model-internals phase** | The learner is new to the field, and a client's first hard question is usually "why not fine-tune?" A phase that trains, fine-tunes, distils and specialises a small model on a laptop is the cheapest possible way to have an earned answer. |
| **Paid model access** | Not available. The free tiers are a constraint the plan designs around rather than an inconvenience it ignores. |

## Consequences

- **Better:** every concept has exactly one address; a thin day is visible from the tracker alone;
  the repository can be picked up after three weeks away, because the last ledger row says where
  we are.
- **Worse:** the format has real overhead. Eleven sections per part is a lot of structure, and some
  days will be slower to write than the subject strictly requires. 137 days is long; the learner
  may not finish, and the plan accepts that a half-finished repository with honest ledgers is worth
  more than a finished one with none.
- **New failure mode:** the generated indexes can go stale and start disagreeing with the days.
  Caught by `python granth.py check`, which fails if any generated document is out of date.
- **New failure mode:** the free-tier caps can be lowered without notice, and a day designed for
  twenty requests may no longer fit. Caught by the freshness check at every phase gate, which
  re-opens each provider's limits page.
- **Revisit if:** the eleven-section contract starts producing padding — sections filled to satisfy
  the checker rather than the reader. That is a signal the contract is wrong for this subject, and
  it gets its own ADR rather than a quiet exception. Revisit also if the CPU-only constraint makes
  days 18–23 run so slowly that the learner skips them; the fix is a smaller model, recorded in an
  ADR, never a skipped day.
