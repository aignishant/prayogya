---
project: "P01"
day: 10
title: "The workflow runtime"
spine: 9
kind: mechanism
deploy_tier: D3
plan_version: "v4.1.0"
parts: 7
files_printed: [claims_desk/workflow.py, tests/test_workflow.py]
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** a second agent, the eight letters it writes, a leak that every existing test passed,
> and a bill that two agents share.
> **Today:** the order those agents run in stops being a `for` loop and becomes an object — stages
> you can print, a node that is code, a repair loop with a bound, and the deprecation notice that
> says all of it is going away.
> **Tomorrow:** callbacks and plugins — the hooks that run around every model call, and the place
> the budget should have been counted all along.

## §1 The scene

Ask a supervisor how a notification is handled and you get a procedure on one sheet: it is read, the
rules are applied, and if it cannot be fast-tracked a letter goes out — and nobody posts the first
draft, because a letter that names a figure is a number the company has now stated.

Ask day 9's desk the same question and the honest answer is *read `run_queue`*.

Every step was there and every step was right. What was missing is that **nothing but a person could
see them**. No log could say which stage a claim was in, no test could assert that the reading
happens before the rules, and nothing could ask how many stages there are — because the order lived
in the order of statements in a function, which is the one thing a program cannot inspect about
itself.

Today the order becomes a value. `claims_desk/workflow.py` holds three arrangements: the triage is a
`SequentialAgent` over the classifier and a **node that is code**, the correspondence is a
`LoopAgent` that drafts, checks and redrafts with the objection attached, and the queue-at-once is a
`ParallelAgent` this desk builds, measures and does not use.

Two files lose thirty-four and thirty-one lines respectively, both of them orchestration, and
neither agent changes. That is the day in one sentence: **the plan moved out of the modules that do
the work.**

And at the end of it, a line of stderr that has been there all along: *SequentialAgent is deprecated
in favor of Workflow*. Part 3.2 reads it properly, runs the successor, and writes down what this
project is going to do about it.

## §2 The map

Four sections. **Section 1 is the arrangement** — the object, and what flows between its nodes.
**Section 2 is the loop** — the repair cycle and the two bounds that stop it. **Section 3 is what it
costs and what replaces it** — the parallel version, measured, and the runtime that deprecates all
three. **Section 4 is what holds it.**

### 1 · The order as an object

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-order-as-object/1.1-order-as-an-object.md) | The order as an object | What do you get for turning a `for` loop into a workflow? | working |
| [1.2](parts/01-order-as-object/1.2-state-between-nodes.md) | State between nodes | How does one node's answer reach the next one? | working |

### 2 · The loop

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-loop/2.1-draft-objection-draft.md) | The draft, the objection, and the second draft | What ends a loop, and how does the objection reach the writer? | working |
| [2.2](parts/02-the-loop/2.2-the-bound.md) | The bound | Why does a loop need its own bound when the run already has a ceiling? | production |

### 3 · What it costs and what replaces it

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-cost-and-successor/3.1-queue-at-once.md) | The queue at once | What does a `ParallelAgent` actually fan out, and is it what you wanted? | production |
| [3.2](parts/03-cost-and-successor/3.2-runtime-that-replaces-this-one.md) | The runtime that replaces this one | The library says this API is deprecated. Now what? | production |

### 4 · Holding it

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [4.1](parts/04-holding-it/4.1-what-the-tests-hold.md) | What the tests hold | What can you test about a pipeline without running it? | production |

## §3 Setup — run this

Nothing new is installed. One module is added, two agent modules lose their orchestration, and the
desk is rewired onto the workflow.

```bash
./run check
```

Expect `96 passed` before you start — day 9's total — and `110 passed` at the end. Twenty tests from
days 8 and 9 go red partway through and all of them are the change working: `classifier.classify`
and `letter_writer.write` no longer exist, so the tests that used them move to the thing that
replaced them. Part 4.1 is where they are updated.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `claims_desk/workflow.py` | part 1.1 |
| `tests/test_workflow.py` | part 4.1 |

Five earlier files change and each is printed as a marked diff naming the day that printed the
original: `claims_desk/agents/classifier.py` (day 7 part 1.1), `claims_desk/agents/letter_writer.py`
(day 9 part 1.1) and `claims_desk/sessions.py` (day 8 part 1.1) in part 1.2; `claims_desk/scripted.py`
(day 9 part 1.2) and `claims_desk/desk.py` (day 7 part 2.1) in part 2.1. Three test files gain
updates, printed as marked diffs in part 4.1: `tests/test_sessions.py` (day 8 part 3.1),
`tests/test_agent.py` (day 7 part 3.1) and `tests/test_cast.py` (day 9 part 3.3).

## §5 Build brief

Write `claims_desk/workflow.py` first and run its stages before wiring anything. Then rewire the desk
and let the gate tell you which tests must move. Then the reps:

| File | What it must do |
| --- | --- |
| `claims_desk/workflow.py` | `TODO(me)`: the loop as a `Workflow` graph. Part 3.2 got the triage working and could not get a conditional edge to route. Find out how a node emits a route — start from `uv run python -c "import inspect, google.adk.workflow as w; print(inspect.getsource(w.Edge)); print([n for n in dir(w) if not n.startswith('_')])"` — and write down what you find. |
| `claims_desk/workflow.py` | `TODO(me)`: `charge` counts events, not calls. Say what a streaming provider would do to that number, and what you would count instead if you could hook the call itself. |
| `claims_desk/workflow.py` | `TODO(me)`: `morning()` gives every branch the same message. Write the version that runs twelve invocations concurrently with `asyncio.gather` instead, and say which one you would ship and why. |
| `tests/test_workflow.py` | `TODO(me)`: `test_the_bound_is_what_stops_a_loop_that_cannot_converge` builds its own loop and therefore defends nothing about `correspondence()`. Rewrite it to swap only the writer's model, and confirm it goes red when `max_iterations` is removed. |
| Your own notes | `TODO(me)`: the deprecation. Re-read part 3.2's ADR, check whether *"Workflow cannot yet be used as an LlmAgent sub-agent"* is still true in the version you have, and say what you would do if it were not. |

## §6 The check that must be able to fail

```bash
./run check
```

Green is `All checks passed!`, `110 passed`, and day 0's four `ok` lines.

Ways to make it red:

1. **Remove `max_iterations` from `correspondence()`.** Exactly one test fails —
   `test_the_correspondence_workflow_is_a_bounded_loop` — and every test that runs the loop stays
   green, because an unbounded loop behaves identically on inputs that converge.
2. **Remove `escalate=accepted` from `HouseStyle`.** The loop runs three times for every letter and
   the letters are all still correct.
3. **Drop `output_key="reading"`** from the triage's classifier and the rules node reports
   `the classifier did not answer with an object` for every claim.
4. **Un-namespace the parallel queue's state keys** — let every branch write `outcome` — and eleven
   of twelve verdicts vanish with no error at all. That is part 3.1 and it is the day's deliberate
   failure.

## §7 Request budget

**Five model calls allowed per notification**, up from three, and **seventeen calls actually spent
across the queue** — eight classifications and nine drafts, because one claim's first draft named a
figure and was written again.

The ceiling moved because the letter became a loop. Five is one classification plus three drafts plus
one for day 15's retry, and part 2.2 is about why the loop needs its own bound of three as well:
`max_iterations` shapes the work, `max_llm_calls` stops a runaway, and the second is not a substitute
for the first.

The boundary is still the expensive part. The queue makes **42 subprocess launches** and the run that
produced this day's transcripts took **42.2 seconds**, almost all of it process startup — which is
why part 3.1's parallel version, which parallelises the model calls, does not address this desk's
actual bottleneck.

## §8 Traps

- **A workflow agent has no conditional edge.** It runs its children. Everything conditional stays
  in Python, and the file says where.
- **A node does not have to be a model.** A `BaseAgent` subclass with no model is a first-class
  stage, and in this desk it is the only stage that decides anything.
- **A custom node must `yield`.** Return instead and you get `AttributeError: 'coroutine' object has
  no attribute 'aclose'`, which names a method nobody wrote.
- **State is changed by a `state_delta` on an event**, not by assigning to `ctx.session.state`.
  Assigning appears to work and leaves nothing in the record.
- **`{feedback}` raises on the first pass; `{feedback?}` does not.** A template read from state is a
  dependency on another node having run.
- **A `LoopAgent` with no `escalate` runs to `max_iterations` every time**, including when the first
  pass was already right, and nothing goes red.
- **An outer call ceiling is a safety net, not a bound.** If the only thing stopping a loop is the
  budget for the whole claim, the loop is unbounded.
- **`ParallelAgent` fans out the invocation, not the input.** Every branch gets the same message.
- **Shared state plus parallelism is a data race**, and a dictionary never complains about being
  written twice.
- **Branches built from one factory share their nodes' names**, so a per-author budget breakdown
  collapses to one entry.
- **The three arrangements are deprecated in the version this project pins.** Read the notice; it
  has two sentences and the second one is the one that matters.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| The arrangement, as data | this project | 2026-09-10 | `triage SequentialAgent` over `classifier LlmAgent` and `rules Rules`; `correspondence LoopAgent` over `letter_writer LlmAgent` and `house_style HouseStyle`. |
| A node that returns instead of yielding | this project, deliberately broken | 2026-09-10 | `AttributeError: 'coroutine' object has no attribute 'aclose'` and `RuntimeWarning: coroutine 'NoYield._run_async_impl' was never awaited`. |
| What triage leaves in state | this project | 2026-09-10 | `claim`, `error`, `outcome`, `reading`, `reason` — five keys, each with one writer. |
| A template with no `?` | this project | 2026-09-10 | ``KeyError: 'Context variable not found: `feedback`.'`` |
| The loop, clean and repaired | this project | 2026-09-10 | `FNOL-4477 | drafts: 1`; `FNOL-4480 | drafts: 2`, the first refused on `"found": "2"` at 180 characters, the second accepted at 165. |
| A loop with nothing to stop it | this project, `escalate` removed | 2026-09-10 | Three identical `house_style` lines with `"accepted": true`, `"yielded": 6`, `"drafts": 3`. |
| A writer that cannot take the objection | this project | 2026-09-10 | Three drafts, `escalate=None` on every writer event and `escalate=False` on every checker event, then it stops. |
| The framework's ceiling | this project | 2026-09-10 | `LlmCallsLimitExceededError: Max number of llm calls limit of \`1\` exceeded`; and `limit of \`5\` exceeded` for an unbounded loop on the desk's real budget. |
| The queue at once | this project | 2026-09-10 | `nodes: 37 | model nodes: {'classifier'} | events: 24 in 0.22 seconds | readings: 12 | distinct perils: ['escape-of-water']`. |
| Shared state under parallelism | this project, namespacing removed | 2026-09-10 | Twelve correct `workflow.rules` log lines, and a session holding one verdict: `outcome: deficiency | reason: missing_contact`. |
| The deprecation | the installed package | 2026-09-10 | `DeprecationWarning: SequentialAgent is deprecated in favor of Workflow and will be removed in a future version. Workflow cannot yet be used as an LlmAgent sub-agent.` |
| The successor, running | this project | 2026-09-10 | `Workflow(edges=[(START, reader), (reader, rules)])` with a plain function as a node: two events, `author=classifier` then `author=triage`. |
| The successor's conditional edge | this project | 2026-09-10 | `Node 'house_style' has conditional/DEFAULT edges but none were matched by the emitted route(s): None. The branch will end.` — a `TODO(me)`, not a conclusion. |
| Removing the loop's bound | this project | 2026-09-10 | `1 failed, 15 passed` — only the shape test. |
| The queue, end to end | this project, over the real stdio boundary | 2026-09-10 | `{'fast-track': 4, 'deficiency': 8, 'pending': 0} in 42.2 seconds`; `claim files: 12 | with a letter: 8`; 17 model calls; 42 boundary launches. |
| The gate | this project, `./run check` | 2026-09-10 | ruff clean, `110 passed`, day 0's four checks green. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 01 | 10 | 2026-09-10 | The workflow runtime | 6 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the first restates a definition the glossary already carries; the rest are
new:

```text
| Session state | A dictionary that travels with a conversation, is written into the store and survives every turn. From day 10 it is also the edge between two workflow nodes: one writes a key, the next reads it, and neither knows the other exists. | P01 day 10 part 1.2 | the state dict |
| Workflow agent | An agent whose job is not to answer but to run other agents in a stated arrangement — sequential, parallel or looping. The order stops being statements in a function and becomes a value that can be printed, tested and built from data. | P01 day 10 part 1.1 | the pipeline, the graph |
| Node | One stage of a workflow. It may be a model-backed agent or ordinary code; the arrangement cannot tell the difference, and a code node costs nothing. | P01 day 10 part 1.1 | a stage, a step |
| Output key | A field on a model-backed agent that tells the framework to write that agent's final text into session state under a given name. The agent is not aware of it, and it is how one node's answer reaches the next. | P01 day 10 part 1.2 | `output_key` |
| State delta | The way a node changes state: a dictionary declared on an event it yields, rather than an assignment to the state object. Assigning changes memory and records nothing. | P01 day 10 part 1.2 | the delta |
| Escalate | A flag a node sets on an event to say *stop*. A `LoopAgent` breaks when one goes past; without it the loop runs to its iteration bound every time. | P01 day 10 part 2.1 | the exit flag |
| Iteration bound | The maximum number of times a loop may go round, declared on the loop itself. It shapes the work, and it is not the same thing as a ceiling on model calls. | P01 day 10 part 2.2 | `max_iterations` |
| Call ceiling | A limit on model calls for one whole invocation, set on the run's configuration and enforced by the framework, which raises rather than returning a partial answer. A safety net, not a bound. | P01 day 10 part 2.2 | `max_llm_calls` |
```

**`docs/PINS.md`** — no row is owed. Nothing was installed today.

**`docs/SOURCES.md`** — no row is owed. Nothing with a citation identifier was cited; the
deprecation notice is quoted from the installed package and recorded in
`docs/adr/ADR-0010-p01-stays-on-the-composition-workflow-agents.md`.

**Commit:**

```text
P01 day 10: The workflow runtime
```
