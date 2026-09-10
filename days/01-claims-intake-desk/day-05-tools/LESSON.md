---
project: "P01"
day: 5
title: "Tools"
spine: 5
kind: mechanism
deploy_tier: D3
plan_version: "v4.1.0"
parts: 5
files_printed: [claims_mcp/tools.py, claims_mcp/server.py, tests/test_tools.py]
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** the boundary gained a second transport, a resource and a prompt, and the desk gained
> a client that cannot tell which wire it used.
> **Today:** the docket goes from one tool to four — a lookup, a question about a date, a write and a
> read that usually finds nothing — and the description of each one turns out to be the whole of the
> interface.
> **Tomorrow:** the read that finds nothing becomes a whole day. At an intake desk, a deficiency is
> not a failure to process a claim; it is the claim being processed.

## §1 The scene

There is a pad of request slips at the claims desk, one per department, and the whole system rests
on the printed heading, because the person receiving it is in another building and has never met
you. Shorten the headings to save space and the slips start arriving in the wrong departments — not
often, and not in a way anybody can attribute to the headings.

In a fortnight that stops being a metaphor. From day 7 a model holds this docket and picks one
entry. It has no colleague to ask and no access to the code: it sees a name, a sentence and a
schema. **The description is the API.**

So today the docket is written as though that were true, because it is. Four tools, each with a
first line a stranger could act on. One of them has a box with squares in it rather than a ruled
line — `date_of_loss: date` — and that one annotation turns `2026-3-14` from a silent wrong answer
into a refusal that names the field. One of them writes, and refuses four shapes it does not
recognise, as data rather than as an exception. And one of them will usually find nothing, and says
so in three lines of docstring, because the last part of the day measures what happens when finding
nothing becomes an error instead: **the message is deleted on the way across the line.**

## §2 The map

Three sections. **Section 1 is the docket** — the four tools, and the split between writing one and
declaring one. **Section 2 is one parameter**, and what changes when it stops being a string.
**Section 3 is the answer** — the two copies every result carries, and what a tool destroys when it
raises instead of returning.

### 1 · The docket — four slips, and who prints the pad

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-docket/1.1-description-is-the-api.md) | The description is the API | What does a model actually have to choose on? | working |
| [1.2](parts/01-the-docket/1.2-wiring-now-there-are-four.md) | The wiring, now that there are four | Where does the docket get decided, once tools have their own file? | working |

### 2 · A parameter — the box with squares in it

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-a-parameter/2.1-parameter-that-is-not-a-string.md) | A parameter that is not a string | What is a type annotation worth when it is part of the wire? | working |

### 3 · The answer — what comes back, and what does not

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-the-answer/3.1-two-copies-of-every-answer.md) | Two copies of every answer | Why does one return value arrive twice, and what holds the docket to its promises? | production |
| [3.2](parts/03-the-answer/3.2-tool-that-returns-nothing-honestly.md) | The tool that returns nothing, honestly | What does a tool lose by raising? | production |

## §3 Setup — run this

Nothing new is installed today. One file is created and one is emptied out.

```bash
./run check
```

Expect `31 passed` before you start — day 4's total — and `45 passed` at the end. The boundary's
version moves to `0.3.0`, which will make a test from day 3 go red partway through; that is the
assertion working, and part 3.1 is where it is updated.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `claims_mcp/tools.py` | part 1.1 |
| `claims_mcp/server.py` | part 1.2 |
| `tests/test_tools.py` | part 3.1 |

`tests/test_boundary.py` also changes: the docket assertion moves out of it into
`tests/test_tools.py`, and what remains is the server's identity. That is printed as a marked diff
in part 3.1 against day 3 part 3.1, which is the day that printed the file.

## §5 Build brief

Move `fetch_policy` into a new `claims_mcp/tools.py`, add the other three, reduce `server.py` to
wiring, then write the tests. Then the reps:

| File | What it must do |
| --- | --- |
| `claims_mcp/tools.py` | `TODO(me)`: `check_in_force` accepts a date of loss in the future. That is well-formed and impossible. Add the refusal — as **data**, not an exception — and say why it belongs inside the tool rather than in the schema. |
| `claims_mcp/tools.py` | `TODO(me)`: `record_decision` is the only tool that writes and nothing marks it as such. Read what `server.tool()` accepts as `annotations=`, and decide whether to declare it. Whatever you decide, write down the sentence you would say in review. |
| `claims_mcp/server.py` | `TODO(me)`: day 4's `perils` and `deficiency_letter` logged their calls; after the split they do not. Put the lines back or justify their absence in a comment — day 17 wants one trace across every hop. |
| `tests/test_tools.py` | `TODO(me)`: `test_an_answer_arrives_twice_over` cannot currently fail, because every tool lets the SDK build both copies. Write the tool that makes it fail — build a text block by hand — see it go red, then delete the tool and keep the test. |
| `tests/test_tools.py` | `TODO(me)`: `test_every_tool_says_what_it_does_in_its_first_line` requires five words and a full stop. Name a bad description that passes it, then decide whether to make the check stricter or to accept that this one is a floor. |

## §6 The check that must be able to fail

```bash
./run check
```

Green is `All checks passed!`, `45 passed`, and day 0's four `ok` lines.

Four ways to make it red:

1. **Shorten a description.** Replace `check_in_force`'s first docstring line with `"""Cover
   check."""` and exactly one test objects. Read the docket afterwards and decide for yourself
   whether you could still tell the tools apart.
2. **Take an annotation off.** `date_of_loss` without `: date` still works, still accepts a string,
   and fails inside the function with `Error executing tool check_in_force` and nothing else.
3. **Write a tool and forget `DECLARED`.** The function exists and the docket does not change; a
   caller gets `Unknown tool`.
4. **Make the empty answer an error.** `read_decision` raising a `KeyError` takes exactly one test
   with it, and the clear message in that exception never reaches the caller. That is part 3.2 and
   it is the day's deliberate failure.

## §7 Request budget

**Zero.** Six days in and still no model call. Everything today is about what a model will be shown
when there is one: four descriptions, four schemas, and a result envelope with a text block in it
that exists solely to be read by something that cannot parse JSON reliably.

Day 7 spends the first request. Every tool it can call was written today.

## §8 Traps

- **A docstring's first line is an interface.** Editing it in a tidy-up commit changes what a model
  chooses on, and no type checker, linter or test will mention it unless you write one.
- **A parameter description's job is to rule out the plausible mistake.** `date_of_loss` says "not
  the day it was reported" because every notification carries both and they differ.
- **An un-annotated parameter defaults to `string`.** It does not fail; it silently becomes the
  loosest possible declaration, and the failure moves inside your function where its message cannot
  escape.
- **`is_error` is for a malformed request, not for an unwelcome answer.** An unknown policy, an
  unknown reason code, a claim not yet decided: all results. A date that is not a date: an error.
- **An exception's message does not cross the boundary.** The SDK replaces it with `Error executing
  tool <name>`. Anything a caller needs to know has to be in the return value.
- **A function in `tools.py` is not a tool until it is in `DECLARED`.** That is deliberate: writing
  a tool and publishing one are different decisions.
- **`record_decision` writes, so tests that call it must be isolated.** The autouse fixture repoints
  the store at a temporary directory; without it the suite's result depends on previous runs.
- **The boundary's version moves when its docket changes**, and a day-3 test pins it. Update the
  assertion in the same commit as the change, never before.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| The docket a model is shown | this project, `list_tools` in-process | 2026-09-10 | Four tools in `DECLARED` order, each with a one-sentence first line; `date_of_loss` carries `"format": "date"`; `reason` carries `anyOf: [string, null]`, `default: null`, and is absent from `required`. |
| A typed date on the way in | this project, three malformed values | 2026-09-10 | `'14/03/2026'` → `invalid character in year`; `'2026-3-14'` → `input is too short`; `'last Tuesday'` → `invalid character in year`. All `is_error: true`, all naming `date_of_loss`, none reaching the function. |
| The same date without the annotation | this project | 2026-09-10 | Accepted as a string, fails inside the tool, and the caller receives only `Error executing tool check_in_force`. |
| The write's refusals | this project, four shapes | 2026-09-10 | `unknown outcome 'fasttrack'`, `a deficiency must name a reason`, `unknown reason 'no_photo'`, `a fast-track has no reason` — every one of them `is_error: false` with `recorded: false`. |
| Read before and after a write | this project | 2026-09-10 | `{"found": false, "claim_id": "FNOL-4471"}`, then `{"found": true, ..., "outcome": "fast-track", "reason": null}`. |
| A tool that raises | this project, `read_decision` with a `KeyError` | 2026-09-10 | `is_error: true`, `structured_content: null`, text `Error executing tool read_decision`. The exception's own message — "no decision recorded for FNOL-4471" — does not cross the boundary. |
| A shortened description | this project | 2026-09-10 | The docket shows `check_in_force: Cover check.` and `test_every_tool_says_what_it_does_in_its_first_line` fails. |
| An undeclared function | this project | 2026-09-10 | The docket is unchanged and calling it returns `Unknown tool: draft_letter`. |
| The gate | this project, `./run check` | 2026-09-10 | ruff clean, `45 passed`, day 0's four checks green. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 01 | 5 | 2026-09-10 | Tools | 5 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the first four restate definitions the glossary already carries; the rest
are new:

```text
| Function declaration | The JSON object a model is given for one of your functions: a name, a prose description, and a JSON Schema for the arguments. It is the entire interface — the model never sees the code — and nothing checks that it describes the function correctly. | P01 day 5 part 1.1 | tool declaration, the schema |
| JSON Schema | A standard vocabulary for describing the shape of a JSON value: its type, its named properties, and which of them are required. Used here to tell a model what an argument bag must look like, and it says nothing about defaults. | P01 day 5 part 2.1 | the parameters schema |
| Derived declaration | A tool declaration the framework builds by reading a function, as against one written by hand beside it. It cannot drift from the function, and it can only carry what the function already contains. | P01 day 5 part 1.1 | the derived schema |
| Tool result envelope | The structure a tool's answer arrives in: a list of typed content blocks, an optional structured copy of the same value, and a flag saying whether the call failed. Your function returns a value; the envelope is added around it on the way out. | P01 day 5 part 3.1 | the tool result, `CallToolResult` |
| The docket | The set of tools a boundary declares, decided in one place and in one order. Writing a tool and declaring one are separate decisions, so that a new capability costs a visible line. | P01 day 5 part 1.2 | the declared tools, `DECLARED` |
| Schema format | A JSON Schema keyword naming which kind of string a string is — `date`, `date-time`, `uri`. Derived here from a Python annotation, and the difference between telling a model the format and hoping it guesses. | P01 day 5 part 2.1 | `format`, the string format |
| Refusal | A tool answering "no, and here is which rule you broke", returned as data with the call marked successful. Distinct from an error, which says the request itself was malformed and the caller must fix the request. | P01 day 5 part 1.1 | a declined call |
| Swallowed exception message | What happens to an exception raised inside a tool: the SDK replaces it with `Error executing tool <name>`, so the original text never reaches the caller. The reason anything a caller needs must be a return value. | P01 day 5 part 3.2 | `UnexpectedToolError` |
```

**`docs/PINS.md`** — no row is owed. Nothing was installed today.

**`docs/SOURCES.md`** — no row is owed. Nothing with a citation identifier was cited.

**Commit:**

```text
P01 day 5: Tools
```
