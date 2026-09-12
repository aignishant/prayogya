---
project: "P01"
day: 7
title: "The first agent"
spine: 6
kind: mechanism
deploy_tier: D3
plan_version: "v4.1.0"
parts: 5
files_printed: [claims_desk/agents/classifier.py, claims_desk/scripted.py, claims_desk/desk.py, tests/test_agent.py]
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** the desk ran end to end for the first time, decided four of twelve notifications
> and put the other eight in a pending tray with a note saying what it was waiting for.
> **Today:** it gets the thing it was waiting for. One agent, asked two questions and forbidden five,
> against a stand-in model that announces itself three ways — and the queue produces the numbers
> `PROJECT.md` promised on day 0.
> **Tomorrow:** sessions and state. What survives a turn, what must never be written into one, and
> what the runner's events contain once there is more than one of them.

## §1 The scene

A caller who does not speak the handler's language is put through to an interpreter, and the
arrangement is narrow on purpose. The interpreter renders what was said. They do not advise the
caller, and they do not decide whether the claim is covered. The narrowness is what makes their
mistakes findable: a wrong sentence is a wrong sentence, and somebody can point at it.

The desk has been waiting six days for an interpreter. Day 2 proved that four of its eight rules
need somebody to have read a sentence, and that a keyword scan is not that somebody — it called
*"No one hurt"* an injury. Day 6 ran the desk and put two thirds of the queue in a tray for exactly
that reason.

Today it gets one. It is asked **which peril is this** and **was anyone hurt**, and it is forbidden
to decide the claim, mention money, or add commentary. Behind it sits a stand-in model that replays
a script, needs no key, costs nothing — and says so in its name, in every answer, and to the
registry that admits it.

Then the desk asks it **last**. Everything the fields can settle is settled first, so a notification
with no date of loss costs nothing at all. The queue comes out four fast-tracked and eight
deficiency letters with eight different reasons, nothing pending: the sentence `PROJECT.md`
committed to on day 0, checked against a run for the first time.

## §2 The map

Three sections. **Section 1 is the agent** — what it is, and the model that is not a model.
**Section 2 is the desk with a reader in it** — what changed, what it decides, and what it cost.
**Section 3 is what holds it**, including the day's own gate: a double that stops announcing itself
stops being allowed.

### 1 · The first agent

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-agent/1.1-agent-is-a-configuration.md) | An agent is a configuration | What is an agent, what runs one, and what should this one be allowed to do? | working |
| [1.2](parts/01-the-agent/1.2-model-that-is-not-a-model.md) | The model that is not a model | How do you run this project with no key, without producing evidence you have not got? | working |

### 2 · The desk with a reader

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-desk-with-a-reader/2.1-twelve-decided-and-what-it-cost.md) | Twelve decided, and what it cost | What does the desk decide now, and where in the order does the expensive question go? | production |

### 3 · Holding it

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-holding-it/3.1-what-the-tests-hold.md) | What the tests hold | What holds an agent to its remit, and what happens to the tests that came before it? | production |
| [3.2](parts/03-holding-it/3.2-double-that-stopped-announcing-itself.md) | The double that stopped announcing itself | Which of the double's three announcements is actually enforced? | production |

## §3 Setup — run this

One package to install, and it is this project's second runtime dependency.

```bash
uv add "google-adk==2.8.0"
uv run python -c "import google.adk; print('adk', google.adk.__version__)"
uv run python -c "import importlib.metadata as m; print('mcp', m.version('mcp'))"

mkdir -p claims_desk/agents
```

Expect `adk 2.8.0` and **`mcp 2.2.0`** — the second command matters as much as the first.

**Install `google-adk`, not `google-adk[mcp]`.** The `mcp` extra requires `mcp<2`, which cannot
coexist with the version this project's boundary runs on. Without the extra there is no conflict at
all: the constraint applies to an extra this project never asks for. That decision, its cost — this
project never uses ADK's own MCP integration — and what would make it worth revisiting are
`docs/adr/ADR-0009` in the authoring repository.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `claims_desk/agents/classifier.py` | part 1.1 |
| `claims_desk/scripted.py` | part 1.2 |
| `claims_desk/desk.py` | part 2.1 |
| `tests/test_agent.py` | part 3.1 |

`claims_desk/agents/__init__.py` is a docstring and nothing else; type it from part 1.1's setup.
Three earlier files change and each is printed as a marked diff: `claims_desk/models.py` in part
1.2, `claims_desk/domain.py` in part 2.1, and `tests/test_desk.py` with `tests/test_domain.py` in
part 3.1.

## §5 Build brief

Install ADK, write the stand-in, teach the registry the prefix, write the agent, then rewire the
desk and let the gate tell you which older tests have to change. Then the reps:

| File | What it must do |
| --- | --- |
| `claims_desk/agents/classifier.py` | `TODO(me)`: the peril vocabulary is written into the instruction **and** published by the boundary as `claims://cover/perils`. Fetch it instead of restating it, or write down why not — and say what breaks the day somebody adds a peril to one and not the other. |
| `claims_desk/agents/classifier.py` | `TODO(me)`: the instruction is sent in full on every call. Count its characters, multiply by twelve, and write the number down. Then decide whether any line of it can go. |
| `claims_desk/desk.py` | `TODO(me)`: `settled_without_reading` depends on knowing that `peril_not_covered` is the only verdict an empty loss type can produce. Write the test that would fail if day 2's rule order changed underneath it. |
| `tests/test_agent.py` | `TODO(me)`: the in-process fixture is now duplicated in two test files. Move it to a `conftest.py`, then argue the other side — a fixture visible in the file that depends on it is a fixture nobody has to go looking for. Keep whichever you can defend. |
| `docs` of your own | `TODO(me)`: **the honest gap.** Every transcript in this project came from a stand-in. Get a key, run one notification with a real model, and write down what differed — the event count, the shape of the answer, whether it obeyed the instruction. Until that exists, this project has proved its own code and nothing about a model. |

## §6 The check that must be able to fail

```bash
./run check
```

Green is `All checks passed!`, `66 passed`, and day 0's four `ok` lines.

Ways to make it red:

1. **Soften the instruction.** Remove `Do not decide whether the claim can be fast-tracked` and
   `test_the_agent_is_configured_with_a_pinned_model` objects. It is a substring assertion on prose
   and it is brittle on purpose.
2. **Let the double guess.** Make `_answer_for` fall back to a plausible peril instead of refusing,
   and `test_the_classifier_reports_rather_than_guesses` goes red — which is the test that stops a
   fake acquiring opinions.
3. **Move the classifier call above the field rules.** No verdict changes and
   `test_a_notification_settled_by_the_field_rules_costs_no_model_call` fails on `budget.spent == 0`.
   The only thing that changed was the bill.
4. **Take the prefix off the double** and the registry refuses it — part 3.2, and the day's
   deliberate failure. Several tests go red and the message names no doubles at all: it is the same
   refusal an unknown provider model would get.

## §7 Request budget

**Two model calls per notification**, and one is spent.

`CALLS_PER_NOTIFICATION = 2` in `claims_desk/desk.py`: one classification, and headroom for the
retry day 15 adds. The ceiling is per notification because that is the unit an insurer costs work
in, and because it contains a runaway — a shared budget would let one looping claim exhaust a
morning's allowance.

Across the queue: **eight calls for twelve notifications.** Four are settled by the field rules and
cost nothing, which is the ordering in part 2.1 and is visible as `budget.spent == 0` in a test.

**Every one of those calls went to a stand-in.** No provider was contacted, nothing was billed, and
no rate limit applies. What a real call costs — in tokens, in latency, in refusals — is the
`TODO(me)` in §5, and this project cannot answer it.

## §8 Traps

- **`google-adk`, never `google-adk[mcp]`.** The extra pins `mcp<2` and this project's boundary runs
  `mcp==2.2.0`. Check with `importlib.metadata.version("mcp")` after installing.
- **`Agent` and `LlmAgent` are the same class.** Two names for one thing; pick one and use it.
- **An agent does no work.** It is a configuration object. A `Runner` executes a turn, and
  `run_async` yields events rather than returning an answer.
- **`auto_create_session=True`, or the runner refuses** to run against a session nobody created.
- **Check `is_final_response()`, `event.content` and `event.content.parts`** — all three. Any one of
  them missing gives an `AttributeError` on the day something goes wrong rather than on a good day.
- **Spend the budget before the call, not after.** A call that fails still asked the provider.
- **Ask the model last.** Every rule that can be settled from fields is free; the model is a
  request, a bill, a rate limit and a wait.
- **A double that guesses is a liar.** A stand-in with no scripted answer must refuse, or the suite
  goes green on descriptions nobody has thought about.
- **The framework logs `Skipping missing token usage metadata`** on every stand-in call. That is
  true, it is useful, and it is a list of everything this project cannot learn from its own
  transcripts. Do not silence it.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| ADK installs without the MCP extra | this project, `uv add "google-adk==2.8.0"` | 2026-09-10 | `google-adk 2.8.0` installed and `mcp` still `2.2.0` — no conflict, because the `mcp<2` constraint applies only to the `[mcp]` extra. |
| The framework's real API | the installed package, by introspection | 2026-09-10 | `Agent is LlmAgent` is `True`; `Runner(*, app_name, agent, session_service, auto_create_session)`; `run_async(*, user_id, session_id, new_message)` yields events; `BaseLlm.generate_content_async(llm_request, stream=False)` is an async generator; `BaseLlm` has exactly one field, `model`. |
| The first model call | this project | 2026-09-10 | One event, 76 characters, `"model": "scripted/claims-classifier"`, answer `{"scripted": true, "loss_type": "escape-of-water", "injury_reported": false}`, budget `1 of 5`. |
| The day-2 failure, reversed | this project, FNOL-4471 and FNOL-4478 | 2026-09-10 | `injury_reported: false` for the description ending "No one hurt", and `true` for the one where a shoulder was hurt. |
| The double refusing to guess | this project | 2026-09-10 | `{"error": "the classifier's object is missing a field", "said": "{\"scripted\": true, \"error\": \"no scripted answer for this description\"}"}`. |
| The ordering saves calls | this project, five notifications | 2026-09-10 | `FNOL-4473 deficiency missing_date_of_loss calls=0`; the other four cost exactly one each. |
| The whole queue | this project, over the real subprocess boundary | 2026-09-10 | `{"deficiency": 8, "fast-track": 4, "pending": 0}`, twelve claim files, eight distinct reasons — `PROJECT.md`'s `Done when` numbers. |
| A double that stops announcing itself | this project | 2026-09-10 | `'claims-classifier' is not in this project's registry: ['gemini-3.7-flash', 'gemini-3.8-flash']` — refused by the general rule, not by a rule about doubles. |
| What the double cannot tell you | the framework, on every call | 2026-09-10 | `Skipping missing token usage metadata for agent classifier and model scripted/claims-classifier`. |
| The gate | this project, `./run check` | 2026-09-10 | ruff clean, `66 passed`, day 0's four checks green. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 01 | 7 | 2026-09-10 | The first agent | 5 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the first five restate definitions the glossary already carries; the rest
are new:

```text
| Agent (ADK) | A configuration object describing one agent — its name, its model, its description, its instruction and its tools. It is filled in, never subclassed, and it does no work on its own. `Agent` and `LlmAgent` are the same class. | P01 day 7 part 1.1 | LlmAgent, the brief |
| Runner | The object that executes one turn for an agent: it holds the agent and the session service, and it produces the turn's events as they happen. The agent is the configuration; the runner is what runs it. | P01 day 7 part 1.1 | the runner |
| Event | One thing a runner emits while it works a question through an agent — a tool being asked for, a tool answering, a fragment of text, the finished text. Smaller than a turn: several events make one. | P01 day 7 part 1.1 | a run event |
| Test double | An object that stands in for a real dependency so a run can be reproduced exactly — same shape, none of the work. It proves things about your own code and nothing whatever about the thing it replaces. | P01 day 7 part 1.2 | a stand-in, a fake |
| Session service | The object that owns stored sessions and hands them out by address. An in-memory one is a dictionary in your process that nothing evicts and no restart survives. | P01 day 7 part 1.1 | the session store |
| Instruction | The standing orders sent to a model beside the conversation — what the agent is for and what it must not do. Resent in full on every call, so every prohibition added to it is paid for on every call forever. | P01 day 7 part 1.1 | the system prompt |
| Announced double | A stand-in whose exemption depends on it declaring itself — here a `scripted/` prefix the registry matches on — so that removing the announcement removes the permission. Distinct from an exemption list, which somebody has to remember to remove. | P01 day 7 part 3.2 | a self-declaring fake |
| Cover | What the rules need to know about a policy and nothing else: in force, perils, limit. The shape that crosses a boundary, as against the record a store keeps. | P01 day 7 part 2.1 | the cover triple |
```

**`docs/PINS.md`** — no row is owed. `google-adk==2.8.0` is a **project** pin and goes in this
project's own `PACKAGES.md`, dated, with the note that it was installed **without** the `[mcp]`
extra.

**`docs/SOURCES.md`** — no row is owed. Nothing with a citation identifier was cited.

**Commit:**

```text
P01 day 7: The first agent
```
