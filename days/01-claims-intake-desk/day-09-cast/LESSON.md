---
project: "P01"
day: 9
title: "The cast"
spine: 8
kind: mechanism
deploy_tier: D3
plan_version: "v4.1.0"
parts: 6
files_printed: [claims_desk/agents/letter_writer.py, tests/test_cast.py]
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** conversations got an address, a service that outlives a call, a rule about what may
> never be written into them, and a look at how a failure actually arrives.
> **Today:** a second agent, the eight letters it writes, the delegation this desk refuses to use, a
> leak that every existing test passed, and a bill that two agents share.
> **Tomorrow:** the workflow runtime — the order these two are called in stops being a `for` loop
> and becomes a thing you can name, inspect and change.

## §1 The scene

There are two people behind the counter now.

One takes the call: listens, writes down what happened, hands the sheet across. The other writes the
letter that goes out — and they work from the sheet, not from the call. They did not hear the
policyholder. They do not have the policy in front of them. If the sheet says *photograph required*
then the letter asks for a photograph and says nothing about excesses, because a letter goes out on
the company's paper and a figure in one is a figure the company can be held to.

That second person is not junior. They are **differently constrained**, and the constraint is the
job.

So the questions that arrive with a second pair of hands are all about the seam between them. Who is
given what. Who decides which of them speaks. What the two of them cost together.

The middle one has an answer that is not the framework's. ADK will let an agent hand the conversation
to a colleague and take it back — three events, driven here for real — and this desk calls its two
agents in a fixed order in ordinary Python instead. The argument is in part 2.1 and it is short: *why
did this claim go to correspondence* should be answered by reading a rule, not by asking a model what
it decided that Tuesday.

And the first question turned out to have a wrong answer while this day was being written. Part 1.1
says the letter writer is given three labelled lines and nothing else. It was not. Day 8's one
session per claim meant the second agent was replayed the first agent's whole exchange — the
policyholder's own words included — and every test in this project passed while it happened. That is
part 3.1, in full, with what the letter writer was actually sent.

## §2 The map

Three sections. **Section 1 is the second agent** — what it is given, what it must not be given, and
the eight letters the department wrote for it. **Section 2 is delegation** — the mechanism this desk
declines, demonstrated working so that declining it is a decision. **Section 3 is holding it** — the
leak, the bill, and the tests.

### 1 · Two agents

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-two-agents/1.1-second-specialist.md) | The second specialist | What do you give an agent that writes text a customer will read? | working |
| [1.2](parts/01-two-agents/1.2-letters-it-writes.md) | The letters it writes | Where does the wording come from, and who is allowed to change it? | working |

### 2 · Delegation

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-delegation/2.1-transfer-and-why-not.md) | Transfer, and why this desk does not use it | What does one agent handing work to another look like, and when should it not? | production |

### 3 · Holding it

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-holding-it/3.1-what-a-session-shares.md) | What a session shares | What does the second agent in a session actually receive? | production |
| [3.2](parts/03-holding-it/3.2-bill-for-two.md) | The bill for two | Is the ceiling per claim or per agent, and how do you tell? | production |
| [3.3](parts/03-holding-it/3.3-what-the-tests-hold.md) | What the tests hold | What changes about testing when there are two of them? | production |

## §3 Setup — run this

Nothing new is installed. One module is added, three files gain a parameter, and the boundary learns
to keep a letter with a decision.

```bash
./run check
```

Expect `78 passed` before you start — day 8's total — and `96 passed` at the end. Two tests from
earlier days go red partway through and both are the change working: `test_the_server_says_who_it_is`
in `tests/test_transports.py`, because the boundary's version moves to `0.5.0`, and a stub in
`tests/test_desk.py` that stands in for `record_decision` and now needs the `letter` parameter.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `claims_desk/agents/letter_writer.py` | part 1.1 |
| `tests/test_cast.py` | part 3.3 |

Four earlier files change and each is printed as a marked diff naming the day that printed the
original: `claims_desk/scripted.py` (day 7 part 1.2) and `claims_mcp/tools.py` (day 5 part 1.1) in
part 1.2, `claims_desk/sessions.py` (day 8 part 1.1) in part 3.1, and `claims_desk/desk.py` (day 7
part 2.1) in part 3.2.

## §5 Build brief

Write `claims_desk/agents/letter_writer.py`, then the eight letters and the boundary's new field,
then let the gate tell you which earlier tests need updating. Add the threads last — the leak in part
3.1 is worth reproducing before you fix it. Then the reps:

| File | What it must do |
| --- | --- |
| `claims_desk/agents/letter_writer.py` | `TODO(me)`: the instruction restates five rules the boundary's `deficiency_letter` prompt already carries. Decide whether to keep the duplication, and write down what you would have to check before deleting either copy. |
| `claims_desk/scripted.py` | `TODO(me)`: `LETTERS` is a table of eight hand-written letters, so this project cannot learn anything about how a provider words them. Add a line to the list day 7 started of things this desk cannot measure about itself. |
| `claims_desk/sessions.py` | `TODO(me)`: `address` now takes a thread, and nothing stops a caller passing one agent's name into another agent's turn. Write the version where an agent's thread is derived from the agent rather than passed, and say what it costs a test that wants to fake one. |
| `claims_desk/desk.py` | `TODO(me)`: a failed letter is logged and the decision is still recorded. Write down the argument for the other choice — refuse to record a deficiency without a letter — and say which an insurer would want. |
| Your own notes | `TODO(me)`: part 2.1's demonstration shows a transfer costing an uncached prompt on every hop. This project cannot measure that. Name the two numbers you would need before choosing delegation for real work. |

## §6 The check that must be able to fail

```bash
./run check
```

Green is `All checks passed!`, `96 passed`, and day 0's four `ok` lines.

Ways to make it red:

1. **Give both agents the same stand-in.** Point `ScriptedLetterWriter.model` at the classifier's
   name and `test_the_cast_is_two_agents_with_different_remits` fails with `assert
   'scripted/claims-classifier' != 'scripted/claims-classifier'`.
2. **Let a fast-track carry a letter.** Delete the boundary's new refusal and
   `test_a_fast_track_may_not_carry_a_letter` goes red.
3. **Give the letter writer its own budget** — `Budget(limit=CALLS_PER_NOTIFICATION)` instead of the
   one it was passed — and `test_a_deficiency_costs_two_calls_across_the_cast` fails on the
   breakdown.
4. **Delete `thread=NAME`** from `letter_writer.write`. Exactly one test goes red —
   `test_the_two_agents_do_not_share_a_conversation` — and nothing else in the project notices. That
   is part 3.1 and it is the day's deliberate failure.

## §7 Request budget

**Three model calls allowed per notification, across the whole cast**, and **sixteen calls actually
spent across the queue** — eight classifications and eight letters.

The ceiling moved from two to three today, and the change is smaller than it looks: the number of
agents doubled and the allowance went up by one, because the allowance is per claim and the claim did
not change. A fast-track spends one call or none; a deficiency spends two; the third is headroom for
day 15's retry.

The boundary is busier than the models. The queue makes **42 subprocess launches** — a policy fetch,
an in-force check, a letter draft and a decision record, each over a fresh stdio boundary — and the
run that produced this day's transcripts took **43.3 seconds** end to end, almost all of it process
startup. That number belongs to this machine on this day and is here as an order of magnitude, not a
benchmark.

## §8 Traps

- **A session is a shared context, not a filing label.** Everything already in it is replayed to
  whoever runs there next, including another agent's questions and answers.
- **The framework's warning for that arrangement is `Event from an unknown agent`**, it is a log
  line rather than an error, and it says nothing about what was shared.
- **A guard against obeying quoted text is not a guard against receiving it.** ADK fences another
  agent's output in injection markers; the words are still in the request.
- **An agent's input is not the string you passed it.** If the input is a design decision, assert on
  `llm_request.contents`, not on the code that builds the question.
- **Two doubles need two names.** One shared stand-in makes a two-agent transcript unreadable and
  every test still passes.
- **A transfer is an ordinary tool call**, `transfer_to_agent`, provided because the agent has
  `sub_agents`. The handover appears as a second event carrying `actions.transfer_to_agent`.
- **Every transfer changes the prompt prefix**, so the whole request is re-sent uncached. The
  framework says so itself when an app can transfer and has no cache configured.
- **A budget is per unit of work or it is not a budget.** Give each agent its own and the ceiling
  silently multiplies by the size of the cast.
- **A shared budget is first-come, first-served**, so the agent that runs later is the one that gets
  refused when the ceiling is too low.
- **Refuse the shape, not just the value.** A fast-track with a letter is a well-formed record that
  should never exist, and only the boundary can say so.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| Two agents, one letter | this project | 2026-09-10 | `We have opened claim FNOL-4477 and need to see the damage. Please send a photograph of the damage. We will continue as soon as we have it.` |
| A refused reason costs nothing | this project | 2026-09-10 | `{'error': "unknown reason 'no_photo'"}` and `budget spent: 0`. |
| A fast-track may not carry a letter | this project, over the boundary | 2026-09-10 | `{"recorded": false, "refused": "a fast-track has no letter"}` |
| Delegation works | this project, two stand-ins with `sub_agents` | 2026-09-10 | Three events: `author='front' calls=['transfer_to_agent']`, then `author='front' transfer_to='specialist'`, then `author='specialist' text='the specialist answered'`. |
| What a transfer costs | the framework's own warning | 2026-09-10 | *"Every transfer swaps the system instruction and the tool set, so the request prefix changes and the whole prompt is re-sent uncached after each transfer."* |
| What the second agent was sent | this project, a spy on the stand-in | 2026-09-10 | With no thread: four blocks — the description `the flexible hose let go overnight`, the framework's quoted-agent guard, `[classifier] said: {"scripted": true, "loss_type": "escape-of-water", …}`, and only then the question. With a thread: one block. |
| The framework's only signal for it | this project | 2026-09-10 | `Event from an unknown agent: classifier, event id: …`, at WARNING, from `runners.py`. |
| The bill for two | this project | 2026-09-10 | `one shared budget : limit=3 spent=2 by={'classifier': 1, 'letter_writer': 1}` against `a budget each : limits=3+3=6 spent=2 by={'classifier': 1}, {'letter_writer': 1}`. |
| What a low ceiling refuses | this project | 2026-09-10 | `refused: letter_writer asked for call 2 of 1 for FNOL-4477; already spent: {'classifier': 1}` |
| One double for two agents | this project, deliberately broken | 2026-09-10 | `AssertionError: assert 'scripted/claims-classifier' != 'scripted/claims-classifier'` |
| Deleting the thread | this project, deliberately broken | 2026-09-10 | `1 failed, 17 passed` — only `test_the_two_agents_do_not_share_a_conversation`. |
| The queue, end to end | this project, over the real stdio boundary | 2026-09-10 | `{'fast-track': 4, 'deficiency': 8, 'pending': 0}`, `claim files: 12 | with a letter: 8`, 16 model calls, 42 boundary launches, 43.3 seconds. |
| The gate | this project, `./run check` | 2026-09-10 | ruff clean, `96 passed`, day 0's four checks green. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 01 | 9 | 2026-09-10 | The cast | 6 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the first restates a definition the glossary already carries; the rest are
new:

```text
| Request budget | A written-down ceiling on how many model calls a unit of work may make, enforced by code that refuses rather than by a paragraph in a document, and counted across the whole cast rather than per agent. Per claim, not per agent: otherwise the ceiling multiplies by the size of the cast without anyone deciding to raise it. | P01 day 9 part 3.2 | a call budget, the bound |
| Cast | The set of agents that work one unit of work. Naming it is what makes "per notification" a different number from "per agent", and what makes a budget breakdown readable. | P01 day 9 part 1.1 | the agents, the team |
| Sub-agent | An ordinary agent listed in another agent's `sub_agents`. Listing it is the whole of the wiring: the parent gains a `transfer_to_agent` tool and chooses between colleagues by reading their `description`. | P01 day 9 part 2.1 | a child agent |
| Delegation | One agent handing the conversation to another and, if needed, getting it back. It arrives as an ordinary function call named `transfer_to_agent`, and the handover appears as an event carrying `actions.transfer_to_agent`. Use it for work; keep decisions in rules, where they can be read. | P01 day 9 part 2.1 | transfer, handover |
| Session thread | A second session under the same claim reference, so that two agents working one claim do not read each other's turns. The reference stays the prefix, so a claim's whole exchange is still found by asking for the claim. | P01 day 9 part 3.1 | a sub-session |
```

**`docs/PINS.md`** — no row is owed. Nothing was installed today.

**`docs/SOURCES.md`** — no row is owed. Nothing with a citation identifier was cited.

**Commit:**

```text
P01 day 9: The cast
```
