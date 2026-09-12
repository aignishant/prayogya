# ADR-0010 — P01 stays on the composition workflow agents, and says so in the day

- **Date:** 2026-09-10
- **Day:** P01 day 10, while the workflow runtime was being built
- **Phase:** P01 Claims Intake Desk, spine slot 9
- **Status:** accepted
- **Amends:** nothing in the plan. §12 slot 9 says "Nodes and edges · sequential, parallel and loop
  · shared state between nodes · the bound that stops a loop, and `max_llm_calls`", and all five of
  those are taught. This records **which of two runtimes** the day builds on, and why.
- **Related:** ADR-0005 (the era gap and the 1.x pin), ADR-0009 (P01 runs the current MCP
  revision), ADR-0006 (every project teaches everything it uses)

## Context

`google-adk` 2.8.0 — the version pinned in P01's `PACKAGES.md` and installed while day 10 was being
written — ships **two** workflow runtimes, and deprecates the older one in favour of the newer.

Observed live on 2026-09-10, by constructing a `SequentialAgent` in the installed package:

```
DeprecationWarning: SequentialAgent is deprecated in favor of Workflow and will be removed in a
future version. Workflow cannot yet be used as an LlmAgent sub-agent.
```

The same notice is emitted by `ParallelAgent` and `LoopAgent`. The three of them are what the plan's
slot 9 names, and they are what every ADK tutorial and every existing example uses.

The successor is `google.adk.workflow.Workflow` — a different package from `google.adk.agents`. It
is a **graph** rather than a composition: `edges` is a list of pairs starting from `START`, its
public surface includes `Node`, `FunctionNode`, `JoinNode`, `Edge` and `DEFAULT_ROUTE`, and it
accepts a plain Python function as a node, binding that function's parameters from session state by
name.

Both were run against this project's own code on the day:

| What was tried | Result |
| --- | --- |
| Triage as `SequentialAgent[classifier, Rules]` | works; the desk's live path, 110 tests green |
| Correspondence as `LoopAgent[writer, HouseStyle]`, `max_iterations=3` | works; one claim in twelve takes two drafts |
| The queue as `ParallelAgent` of twelve branches | runs; all twelve branches receive the same message and read the same peril |
| Triage as `Workflow(edges=[(START, reader), (reader, rules)])` | **works**, with `rules` as a plain function |
| The loop as a `Workflow` with a conditional edge `{True: send, False: writer}` | **does not**: `Node 'house_style' has conditional/DEFAULT edges but none were matched by the emitted route(s): None. The branch will end.` |

So the successor runs, and the arrangement this desk depends on most is the one that could not be
built on it in the time the day had.

## Decision

**P01 builds its workflow runtime on `SequentialAgent`, `ParallelAgent` and `LoopAgent`, and day 10
teaches the deprecation as a first-class part rather than hiding it.**

Specifically:

1. `claims_desk/workflow.py` uses the three deprecated classes. They run the desk end to end.
2. Day 10 part 3.2, *The runtime that replaces this one*, quotes the notice verbatim, drives the
   successor for real against this project's own classifier, and states this decision with its
   reasons.
3. The part that could not be made to work is a `TODO(me)` carrying **the exact lookup command**,
   never a guess about how routes are emitted.
4. `PACKAGES.md` keeps the exact `google-adk` version, so a future reader can tell whether the
   notice they are reading is the one this decision was made against.

## Why

- **The deprecated three run this project today.** The successor could not express the loop, and a
  migration that leaves the hardest arrangement unmigrated is not a migration.
- **The notice's second sentence is a real constraint.** *"Workflow cannot yet be used as an
  LlmAgent sub-agent."* P01 day 9 deliberately taught delegation and argued about when to use it;
  moving to a runtime that cannot be a sub-agent would quietly close a door the curriculum keeps
  open on purpose.
- **A day that teaches a deprecated API without saying so is a bad day.** The alternative to
  migrating is not silence. Part 3.2 exists so that a reader who meets the warning in their own
  terminal has already been shown it, has run the successor once, and has seen the decision written
  down with its reasons.
- **This is the same shape as ADR-0005 and ADR-0009**, one layer up: teach what can be executed and
  quote, in the day itself, the notice that says the mechanism is going away.

## Consequences

- P01's day 10 carries a deprecation warning in every test run. `./run check` reports it among its
  warnings and the day says why.
- **This decision does not bind the other thirty-nine projects.** Slot 9 recurs in every project;
  the next one to reach it re-runs the checks in this ADR's table and decides again. If the
  conditional-edge question has an answer by then, the answer belongs in that project's day and a
  new ADR, not in an edit to this one.
- The `TODO(me)` in part 3.2 is owed. It is a rep for the learner and an open question for the
  curriculum, and it is not discharged by anything in this file.
- If a future `google-adk` removes the three classes, P01's day 10 stops running as printed. That
  is the risk this decision accepts, and the mitigation is that the day already contains a working
  demonstration of the successor.
