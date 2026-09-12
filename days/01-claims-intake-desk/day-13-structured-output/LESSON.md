---
project: "P01"
day: 13
title: "Structured output"
spine: 12
kind: mechanism
deploy_tier: D3
plan_version: "v4.1.0"
parts: 4
files_printed: [claims_desk/schemas.py, tests/test_schemas.py]
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** the difference between remembering and looking up — a handbook with an identifier
> per rule, a retriever you can recompute by hand, and the memory service this desk refuses.
> **Today:** the shape of an answer stops being a sentence in a prompt and becomes a type. The
> framework validates it, the rules receive a dict instead of a string, day 10's parser loses most of
> its job, and a refusal arrives as an exception that would have stopped the queue.
> **Tomorrow:** the decision record — why this claim was fast-tracked, in a form an auditor accepts.

## §1 The scene

The list of perils this desk recognises was written down three times.

Once in the classifier's instruction, as a sentence. Once in `PHOTO_REQUIRED_FOR`, as four of the
six. And once in `data/policies.json`, spread across eight policies — which is where the list is
actually *true*, because a peril is covered when a policy says so.

Three copies of a list is a list that disagrees with itself, and it disagrees on the day somebody
adds a peril to the policy data and not to the instruction. Then the classifier cannot name a peril
the desk covers, the rules refuse the claim as not covered, and a policyholder gets a letter saying
their loss is not covered by their policy. Every individual file is correct.

A schema is where that stops — not because validation is virtuous, but because **a schema is the one
artefact every party reads**: the model is given it, the framework enforces it, the rules receive
what it produced, and the tests argue with it in milliseconds.

So today the six perils become a `StrEnum` in `domain.py`, the shape the classifier may return
becomes a pydantic model in `schemas.py`, and the agent gets `output_schema=Reading`. What follows is
mostly consequences. The framework writes a **validated dict** into state, so day 10's fourteen-line
parser becomes four lines and loses the `json` import. And the refusal it could never make — a peril
that is well-typed, present and not a thing this desk recognises — arrives as a `ValidationError`
raised **inside** the turn, which would have stopped the morning's queue on one unreadable
description if nobody caught it.

Then the part that is not about today at all: what happens when a schema gains a field. A default
accepts every answer written before it existed; the same field without one refuses all of them; and
`extra="forbid"` means an old reader refuses the new answer too. A schema change is two migrations,
in opposite directions, and the order is readers first.

## §2 The map

Three sections. **Section 1 is the shape and what enforcing it does.** **Section 2 is what happens
when the shape changes.** **Section 3 is what holds it.**

### 1 · The shape on the way out

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-shape-on-the-way-out/1.1-shape-is-a-value.md) | The shape, as a value | What is a schema for, beyond validation? | working |
| [1.2](parts/01-shape-on-the-way-out/1.2-validator-that-refuses-a-guess.md) | The validator that refuses a confident guess | What changes once the framework validates? | production |

### 2 · When it changes

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-when-it-changes/2.1-field-that-appeared-on-tuesday.md) | The field that appeared on Tuesday | What does adding one field to a schema actually cost? | production |

### 3 · Holding it

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-holding-it/3.1-what-the-tests-hold.md) | What the tests hold | How do you test a shape, and how do you test that two files agree? | production |

## §3 Setup — run this

Nothing new is installed — pydantic arrived with `google-adk` on day 7 and is now imported directly,
which is worth noticing rather than glossing over.

```bash
./run check
```

Expect `141 passed` before you start — day 12's total — and `157 passed` at the end. Six tests from
days 7, 10 and 11 go red partway through and every one of them is the change working: the classifier's
answer is a dict now, not a string, and a bad answer raises where it used to be returned.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `claims_desk/schemas.py` | part 1.1 |
| `tests/test_schemas.py` | part 3.1 |

Three earlier files change and each is printed as a marked diff naming the day that printed the
original: `claims_desk/domain.py` (day 2 part 2.1) and `claims_desk/agents/classifier.py` (day 7 part
1.1) in part 1.1, and `claims_desk/workflow.py` (day 10 part 1.1) in part 1.2 — twice, once for the
parser and once for the catch. Six assertions in `tests/test_agent.py` and `tests/test_workflow.py`
are updated, and part 1.2 says what each of them was measuring.

## §5 Build brief

Write the enum first, then the schema, then put `output_schema` on the agent and let the gate tell you
what the change did. The parser shrinks last. Then the reps:

| File | What it must do |
| --- | --- |
| `claims_desk/workflow.py` | `TODO(me)`: the desk collapses `refused_shape` into `waiting_for='needs_classification'`, so the verdict loses a distinction the log has. Give it its own `waiting_for`, and say what else has to change for that to be useful. |
| `claims_desk/schemas.py` | `TODO(me)`: the refused answer is logged by field and type and then thrown away. Write it to the claim's own record instead, and say why the log is the wrong place. |
| `claims_desk/domain.py` | `TODO(me)`: `Cover.perils` is still `frozenset[str]` built out of JSON, and agrees with `Peril` only because a test says so. Type the store's side, and say what breaks first. |
| `claims_desk/schemas.py` | `TODO(me)`: `Peril`'s docstring now crosses to a provider on every call, inside the JSON schema. Move the reasoning to a comment, confirm with `model_json_schema()`, and say how many characters you saved per request. |
| Your own notes | `TODO(me)`: part 1.2 catches `ValidationError` around the whole turn, which would also catch one from a tool argument. Write down how you would narrow it and what you would need to know first. |

## §6 The check that must be able to fail

```bash
./run check
```

Green is `All checks passed!`, `157 passed`, and day 0's four `ok` lines.

Ways to make it red:

1. **Add a peril to one policy in `data/policies.json`.** `test_the_enum_is_the_only_list_of_perils`
   fails and names it — a class of failure where every individual file is correct.
2. **Drop `use_enum_values=True`.** The validated object holds `Peril.FIRE` instead of `"fire"`, and
   every comparison in `assess` against the policy's peril set silently stops matching.
3. **Reword the peril sentence in `INSTRUCTION`.** `test_the_instruction_lists_exactly_the_enum`
   fails, because that sentence is load-bearing and generated from the enum.
4. **Remove the `except ValidationError` from `run_triage`.** Nothing goes red in the suite — and one
   description the classifier cannot read stops the whole queue. That is part 1.2 and it is the day's
   deliberate failure.

## §7 Request budget

**Five model calls allowed per notification**, unchanged, and **seventeen spent across the queue** —
unchanged. A schema does not change how often the desk asks; it changes what it will accept back.

What it does change is the size of a request. The JSON schema pydantic generates crosses to the
provider on every call, and it carries every `description` in the model — including `Peril`'s
two-paragraph docstring, which was written for maintainers and is now read by a model several hundred
times a morning. That is a real cost, it was found by printing the schema rather than by reasoning
about it, and shortening it is a `TODO(me)` with the measurement attached.

## §8 Traps

- **A convention is a sentence somebody has to obey; a schema is a value.** That is the whole
  difference, and everything else today follows from it.
- **A fact written in three files is a fact that will disagree with itself**, and the day it does,
  every individual file is still correct.
- **`extra="forbid"` is a decision, not a default.** Pydantic drops unknown keys silently; forbidding
  them is how you find out a model started inventing fields.
- **`use_enum_values=True` or every comparison against your data silently stops matching.**
- **Every `Field(description=...)` crosses to the provider** inside the JSON schema. So does a type's
  docstring. A schema is a prompt whether you think of it as one or not.
- **With `output_schema`, `output_key` receives a dict, not a string.** Anything downstream that
  parsed it will break, and that is the change working.
- **Validation happens inside the turn, so a refusal is an exception**, not a returned value. Day 11's
  lesson from the other direction.
- **Catch it once, at the boundary that already reports failures**, and give it its own constant so a
  claim pending for a bad answer is distinguishable from one pending for no budget.
- **Log the field and the error type, never `input_value`** — that is a fragment of what a model said
  about somebody's claim.
- **A schema change is two migrations**: old data under a new reader, and new data under an old one.
  A default fixes the first and nothing on the writing side fixes the second.
- **Deploy readers before writers**, and the migration cost is proportional to how many copies of the
  schema exist.
- **Pydantic coerces `"true"` to `True`.** Not a bug, and not necessarily what you wanted.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| What crosses to a provider | this project, `Reading.model_json_schema()` | 2026-09-10 | The six-member `enum`, `"additionalProperties": false`, `"required": ["loss_type", "injury_reported"]`, every field description, and `Peril`'s whole docstring. |
| What lands in state | this project | 2026-09-10 | `type: dict`, `value: {'loss_type': 'fire', 'injury_reported': False, 'scripted': True}` — where day 12 put a JSON string. |
| The confident guess | this project | 2026-09-10 | `water damage` → `loss_type` / `enum`; a `confidence` field → `extra_forbidden`; a missing field → `missing`. |
| A schema refusal raises | this project | 2026-09-10 | `ValidationError: 3 validation errors for Reading`, with `error` refused as `extra_forbidden` — the stand-in's own error object, refused by the schema. |
| And the queue survives it, caught | this project | 2026-09-10 | `workflow.refused_shape` with `"detail": "error: extra_forbidden; loss_type: missing; injury_reported: missing"`, then `desk.classification_failed`, then `waiting_for='needs_classification'`. |
| A missing brace in an f-string prompt | this project, deliberately broken | 2026-09-10 | `ValueError: Invalid format specifier ...` at **import time**, with the line number pointing at the JSON example. |
| An optional new field | this project | 2026-09-10 | Accepts every answer written before it existed; `police_reference is None`. |
| The same field, required | this project | 2026-09-10 | Refuses all of them, `loc == ("police_reference",)`. |
| An old reader, a new answer | this project | 2026-09-10 | `Extra inputs are not permitted [type=extra_forbidden, input_value='CR/2026/118', input_type=str]` |
| A peril in the data and not the enum | this project, deliberately broken | 2026-09-10 | One test red: `Extra items in the left set: 'subsidence'`. |
| The gate | this project, `./run check` | 2026-09-10 | ruff clean, `157 passed`, day 0's four checks green. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 01 | 13 | 2026-09-10 | Structured output | 4 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — all new:

```text
| Output schema | A declared type an agent's final answer must satisfy. The framework validates against it inside the turn and writes the validated object into `output_key`, so what reaches the next stage is a parsed value rather than text. | P01 day 13 part 1.1 | `output_schema`, response schema |
| JSON schema | The serialised form of a declared shape, which is what actually crosses to a provider. It carries every field description and every type docstring, so a schema is part of the prompt. | P01 day 13 part 1.1 | the generated schema |
| Extra-forbidden | A schema setting that refuses an undeclared field instead of dropping it. The difference between finding out a model started returning something new and never finding out. | P01 day 13 part 1.1 | `extra="forbid"`, strict mode |
| Validation error | What a schema raises when an answer does not satisfy it. It arrives inside the turn, so it is an exception where a bad answer used to be a returned value, and it has to be caught at the boundary that reports every other failure. | P01 day 13 part 1.2 | `ValidationError` |
| Schema evolution | Changing a declared shape after answers have been written against it. Two migrations in opposite directions — old data under a new reader, new data under an old one — and only the first is fixed by a default. | P01 day 13 part 2.1 | versioning a schema |
| Agreement test | A test that asserts two artefacts which must say the same thing still do — an enum against its data source, a prompt against a type. It exercises no code path and catches the failure where every individual file is correct. | P01 day 13 part 3.1 | a consistency test |
```

**`docs/PINS.md`** — no row is owed. Nothing was installed today; pydantic arrived with `google-adk`
on day 7 and is now imported directly.

**`docs/SOURCES.md`** — no row is owed. Nothing with a citation identifier was cited.

**Commit:**

```text
P01 day 13: Structured output
```
