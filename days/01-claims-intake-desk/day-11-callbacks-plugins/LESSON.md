---
project: "P01"
day: 11
title: "Callbacks and plugins"
spine: 10
kind: mechanism
deploy_tier: D3
plan_version: "v4.1.0"
parts: 6
files_printed: [claims_desk/hooks.py, tests/test_hooks.py]
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** the order became an object — stages you can print, a node that is code, a repair
> loop with a bound, and the deprecation notice that says all of it is going away.
> **Today:** the hooks that run around every model call. The budget stops being reconstructed from
> events and starts being charged before the call, the letter writer gets a lock of its own, and a
> plugin that raised turns out to raise something else entirely.
> **Tomorrow:** memory and retrieval — what the desk is allowed to remember between claims, and what
> it must look up instead.

## §1 The scene

Every claims department has a post room, and it is in nobody's job description.

Letters go out through it. Nobody writes *take it to the post room* at the bottom of a procedure; it
is simply where outgoing things pass. And because everything passes through it, it is the only place
in the building where a rule can be put that applies to everything — a machine that records what
left, a scale that refuses a package over the limit, a stamp saying which office sent it. Put that
rule inside each department instead and you have five copies of it, four of which are correct.

A **plugin** is the post room. Registered once on the runner, it runs around every model call and
every tool call in the process, for agents it has never heard of, in workflows that did not exist
when it was written.

That is where the budget belongs, and today it moves there. Day 10 counted calls by walking the
events after a workflow finished — accurate, cheap, and unable to stop anything. Charging in
`before_model_callback` is the same number observed rather than reconstructed, and because the hook
can replace the call, the budget stops being a record and becomes a limit.

The second half of the day is the other level. Day 9 stopped the policyholder's own words reaching
the letter writer by giving each agent its own conversation — a fix that works and is a *convention*,
enforced by two strings differing. Today the letter writer gets a second lock: a callback on that
agent alone, which refuses any request carrying the description. Two locks on different things, and
part 2.1 measures what the second one costs when it fires.

And in the middle of moving the budget, the day's failure appeared on its own. **A plugin that
raises does not raise your exception.** The framework wraps it, `except BudgetExceeded` stopped
catching anything, and a whole branch of `desk.decide` went dead while a hundred and eight tests
stayed green.

## §2 The map

Four sections. **Section 1 is the post room** — the plugin, what it charges, and what it writes.
**Section 2 is one agent's own rule** — the callback that belongs on the letter writer and nowhere
else. **Section 3 is what a callback must never do.** **Section 4 is what holds it.**

### 1 · Around every call

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-around-every-call/1.1-plugin-that-sees-every-agent.md) | The plugin that sees every agent | What is a plugin, and which hooks have teeth? | working |
| [1.2](parts/01-around-every-call/1.2-where-the-budget-belongs.md) | Where the budget belongs | Why charge before the call instead of counting after it? | production |
| [1.3](parts/01-around-every-call/1.3-three-agents-deep.md) | Three agents deep, one log line | What can a cross-cutting hook record that an agent cannot? | working |

### 2 · One agent's own rule

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-one-agents-rule/2.1-second-lock.md) | The second lock | When does a rule belong on one agent rather than in the plugin? | production |

### 3 · What it must not do

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-what-it-must-not-do/3.1-exception-that-never-arrives.md) | The exception that never arrives | What happens to an exception raised inside a framework hook? | production |

### 4 · Holding it

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [4.1](parts/04-holding-it/4.1-what-the-tests-hold.md) | What the tests hold | How do you test a hook, and how do you test that one did not do something? | production |

## §3 Setup — run this

Nothing new is installed. One module is added and four files gain a few lines each.

```bash
./run check
```

Expect `110 passed` before you start — day 10's total — and `124 passed` at the end. Two tests from
days 9 and 10 go red partway through and both are the change working: a budget refusal is no longer
an exception, and the desk's own limit now bites before the framework's ceiling.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `claims_desk/hooks.py` | part 1.1 |
| `tests/test_hooks.py` | part 4.1 |

Three earlier files change and each is printed as a marked diff naming the day that printed the
original: `claims_desk/sessions.py` (day 8 part 1.1) and `claims_desk/workflow.py` (day 10 part 1.1)
and `claims_desk/desk.py` (day 7 part 2.1) in part 1.2, and `claims_desk/workflow.py` again in part
2.1 for the callback and the forbidden phrase. Two tests from earlier days are updated, and both
updates are described in part 4.1's failure section rather than printed, because each is a single
assertion.

## §5 Build brief

Write `claims_desk/hooks.py`, register it in `sessions.turn`, then delete day 10's `charge`. Let the
gate tell you which two tests were asserting on an exception. Then the reps:

| File | What it must do |
| --- | --- |
| `claims_desk/hooks.py` | `TODO(me)`: a refused leak spins the loop three times for nothing. Write the version that ends the loop, decide whether a guard on one agent should be able to do that, and say what you would lose. |
| `claims_desk/hooks.py` | `TODO(me)`: the plugin's lines carry no claim reference. Pass it through the same context variable the budget uses, and say what that costs anything that runs an agent outside a claim. |
| `claims_desk/hooks.py` | `TODO(me)`: `refuse_the_description` is a case-insensitive substring. List three ways a description could reach the letter writer and slip past it. |
| `claims_desk/util/logging.py` | `TODO(me)`: day 8 opened the allow-list rep and day 11's part 1.3 shows why it matters for a log rather than for state. Write it, and say what it costs the next person who adds a field. |
| `tests/conftest.py` | `TODO(me)`: the `_in_process` fixture is now in five test files, character for character. Move it, run the whole suite, and say what a reader loses when a fixture stops being visible in the file that uses it. |

## §6 The check that must be able to fail

```bash
./run check
```

Green is `All checks passed!`, `124 passed`, and day 0's four `ok` lines.

Ways to make it red:

1. **Take `plugins=[DeskPlugin()]` off the runner.** The budget is never charged; `spent` is `0` on
   every claim and `test_the_plugin_charges_the_call_rather_than_counting_the_events` is the only
   thing that objects.
2. **Log the response text instead of its length** in `after_model_callback`. One test fails —
   `test_what_the_plugin_writes_never_contains_what_was_said` — and every letter this desk writes,
   including the refused drafts, is now in the log.
3. **Return a response from `on_model_error_callback`.** A provider outage becomes an answer, and
   `test_the_error_hook_records_the_failure_and_does_not_swallow_it` fails with "DID NOT RAISE".
4. **Raise `BudgetExceeded` from the plugin instead of returning a refusal.** Two tests fail and
   neither is the one that matters: `desk.decide`'s over-budget branch goes dead, and the queue stops
   on the first claim that runs out. That is part 3.1 and it is the day's deliberate failure.

## §7 Request budget

**Five model calls allowed per notification**, unchanged from day 10, and **seventeen calls actually
spent across the queue** — eight classifications and nine drafts.

What changed is who counts. Day 10 reconstructed the number from events after the fact; today the
plugin charges before the call, so the number is an observation, the refusal is a limit rather than a
record, and a call that fails is charged for the attempt.

Two costs are worth naming because they were measured rather than assumed. **A refused call is still
charged** — the plugin charges before the agent callback refuses, so a leak that never reaches a
provider costs three of a claim's five calls as the loop spins its bound. And **the desk's own budget
now bites before the framework's `max_llm_calls`**, because the ceiling is derived from the same
budget the plugin spends; day 10's outer net is still set and is no longer what stops anything.

The boundary is unchanged: **42 subprocess launches**, and the run that produced this day's
transcripts took **45.0 seconds**.

## §8 Traps

- **A plugin is registered on the runner and sees every agent**; an agent callback is a field on one
  agent. A rule that needs to ask which agent it is looking at is in the wrong file.
- **`before_model_callback` returning a value replaces the call.** No provider is contacted. That is
  the power and the hazard.
- **`after_model_callback` returning a value replaces the answer**, silently. This project only logs
  there.
- **A callback must not raise for an ordinary condition.** The framework wraps whatever comes out of
  a plugin in its own `RuntimeError`, so the exception your caller catches never arrives.
- **When an exception becomes a returned value, the thing you lose is that it cannot be ignored.**
  The check that replaces it needs a test of its own.
- **A plugin's hooks are keyword-only methods; an agent callback is a positional function.** Same
  hook name, two shapes.
- **A mutable default on a `ContextVar` is shared by every context that never set one.** `ruff`
  refuses it by rule `B039`, and it is right.
- **Reset a context variable in a `finally`**, or a run that raises leaves its budget registered for
  whatever runs next.
- **A cross-cutting hook sees everything, so what it records is a retention decision.** Log how much,
  not what.
- **The plugin runs before the agent callback**, so a request the agent refuses has already been
  charged.
- **`on_model_error_callback` returning a response turns an outage into an answer.** Log it and let
  it through.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| The plugin's own line | this project | 2026-09-10 | `{"event": "hooks.model", "agent": "classifier", "invocation": "e-40966bae-…", "parts": 1, "chars": 76, "partial": null}` and `spent: 1 {'classifier': 1}`. |
| A refusal is returned, not raised | this project | 2026-09-10 | `said: '' | refused: ['classifier'] | spent: 0`, with `hooks.refused` carrying day 7's message. |
| A claim with no allowance | this project | 2026-09-10 | `desk.over_budget` naming the agent, then `Verdict(claim_id='FNOL-4477', outcome='pending', reason=None, waiting_for='over_budget')`. |
| Without the `OVER_BUDGET` check | this project, deliberately broken | 2026-09-10 | `waiting_for='needs_classification'` — the wrong reason, silently. |
| A plugin that raises | this project, deliberately broken | 2026-09-10 | `RuntimeError: Error in plugin 'claims-desk' during 'before_model_callback' callback: classifier asked for call 1 of 0 for FNOL-4471; already spent: {}`, and `except BudgetExceeded` did not fire. |
| The suite under that version | this project | 2026-09-10 | `2 failed, 108 passed` — and neither failure was the dead branch in `desk.decide`. |
| Three agents deep | this project | 2026-09-10 | Three `hooks.model` lines, two invocation ids, `chars` 76 then 180 then 165, and `by: {'classifier': 1, 'letter_writer': 2}`. |
| Logging the text instead | this project, deliberately broken | 2026-09-10 | The whole first draft in one log line, and `1 failed, 12 passed`. |
| The second lock | this project | 2026-09-10 | Three `hooks.refused_leak` lines with `"chars": 10`, three `house_style` refusals at `"chars": 0`, and `letter: '' | spent: 3`. |
| The gate | this project, `./run check` | 2026-09-10 | ruff clean, `124 passed`, day 0's four checks green. |
| The queue, end to end | this project, over the real stdio boundary | 2026-09-10 | `{'fast-track': 4, 'deficiency': 8, 'pending': 0} in 45.0 seconds`; `claim files: 12 | with a letter: 8`. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 01 | 11 | 2026-09-10 | Callbacks and plugins | 6 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — all new:

```text
| Plugin | An object registered on the runner whose hooks run around every model call and every tool call in that runner, for every agent, including agents added later. The place a cross-cutting rule goes; a plugin that asks which agent it is looking at has stopped being one. | P01 day 11 part 1.1 | a middleware, an interceptor |
| Agent callback | A function passed as a field when one agent is built, called by the framework for that agent alone. Where a rule about one agent belongs, so that somebody reading the agent finds it. | P01 day 11 part 2.1 | a hook on the agent |
| Before-model hook | The hook that runs before a request goes to a provider. Returning `None` lets the call happen; returning a response **replaces** it, and the provider is never contacted. | P01 day 11 part 1.1 | `before_model_callback` |
| Context variable | Per-task storage, so concurrent units of work do not see each other's values. How a plugin — built once, shared by every run — reaches the budget for the run it is currently inside. Its default must not be mutable. | P01 day 11 part 1.1 | `ContextVar` |
| Extension point | Any place a framework calls your code inside its own control flow. It is a boundary: exceptions do not cross it unchanged, and branches reached only through it are branches your unit tests do not reach. | P01 day 11 part 3.1 | a hook, a callback site |
| Absence test | A test that asserts something does **not** appear — a field in a log, a phrase in a request. A tripwire rather than a proof: it is only ever as good as the string it looks for. | P01 day 11 part 4.1 | a negative test |
```

**`docs/PINS.md`** — no row is owed. Nothing was installed today.

**`docs/SOURCES.md`** — no row is owed. Nothing with a citation identifier was cited.

**Commit:**

```text
P01 day 11: Callbacks and plugins
```
