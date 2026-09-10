---
project: "P01 Ask Desk"
day: 5
phase: P01
title: "P01 Ask Desk · 2 — Tools by hand: JSON schemas and the tool-result turn"
ids: [TL-01]
kind: mechanism
deploy_tier: D1
plan_version: "v3.1.0"
parts: 4
files_printed:
  - "projects/01-ask-desk/ask_desk/tools.py"
  - "projects/01-ask-desk/ask_desk/data/notes.json"
generated: "2026-09-09"
status: written
commit: ""
---

> **Yesterday:** a loop you wrote yourself, a conversation you carry in a list, and a model that can
> only ever answer in words.
> **Today:** three things this desk can actually do, the JSON that tells a model they exist, and the
> second half of the round trip — running the tool and handing the result back.
> **Tomorrow:** the first ADK agent, where a framework holds the loop you have now written twice.

## §1 The scene

A waiter who cannot cook takes your order, writes a docket, puts it through a slot in the wall, and
some time later carries out a plate. Two journeys through the same doorway for one order, and there
is no arrangement that removes them: the waiter cannot cook and the kitchen has never seen your
table. Everything that crosses the wall crosses on the docket.

Which makes the docket format the whole relationship between the two rooms. If it says *soup* and
there are three soups, one gets made and nobody has made a mistake. If the menu describes a dish in
words that read well and are wrong about what is in it, the docket will be written correctly, the
kitchen will cook exactly what was written, and the plate will be wrong — with no moment in the
chain where anything could have been raised.

That is today. Your model is the waiter: it holds the conversation, it decides when a tool is
wanted, and it has never seen your code and never will. What it gets is a short JSON object per
function — a name, a description, and a schema for the arguments — and that object is not
documentation about your interface, it *is* your interface. Your Python functions are in the
kitchen, and the only thing that reaches them is what the model wrote on the docket.

Two rooms, one docket format, and nothing anywhere that compares the menu by the pass with the menu
on the table. Today builds both halves by hand and puts them in one file, because keeping them
together is the only defence there is. Then it sends a docket for a dish this kitchen does not
make, and watches what happens.

## §2 The map

Two sections, and they are the two directions through the slot. The first is the docket itself —
what the model is handed, and what the desk can actually do when it comes back. The second is the
round trip, which is the part day 4 could not have: a reply that is a request, a function that runs
in your process, and a result carried back to the table.

### 1 · The docket

*The mental model: the model never crosses the wall. One small JSON object per function is
everything it will ever know about your code, and nothing checks that the object is telling the
truth.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-docket/1.1-the-declaration-is-the-whole-interface.md) | The declaration is the whole interface | What exactly does a model receive about a tool, and which fields can be wrong without anything raising? | foundation |
| [1.2](parts/01-the-docket/1.2-the-three-things-this-desk-can-do.md) | The three things this desk can do | What is in the two halves of a tool, and what stops them drifting apart? | working |

### 2 · The round trip

*The mental model: the order and the plate are two journeys through the same doorway, and the
restaurant — not the waiter — decides how many trips one order may take.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-round-trip/2.1-call-run-hand-back.md) | Call, run, hand back | How does a tool call travel, and why does one question now cost at least two provider calls? | working |
| [2.2](parts/02-the-round-trip/2.2-the-call-you-could-not-serve.md) | The call you could not serve | Which failures should raise, which should be handed to the model, and what bounds the loop? | production |

## §3 Setup — run this

**Nothing new to install.** Today adds no package, moves no pin and touches no configuration: the
project's toolchain is exactly as day 4 left it, and everything below is standard library plus the
`uv` already here. Every command was run on this machine today; what each one reported is in §9. Run
them in order, from the repository root.

```bash
cd projects/01-ask-desk

# the gate day 4 left green — run it first, so a red here is not confused with today's work
uv run --frozen python run.py check
echo $?

# part 1.2 writes ask_desk/tools.py and ask_desk/data/notes.json
uv run --frozen python -c "
import json
from ask_desk import tools
print(json.dumps(tools.search_notes('vpn file share'), indent=2))
"

# parts 2.1 and 2.2 add to ask_desk/provider.py and ask_desk/loop.py
uv run --frozen python -c "
import json
from ask_desk import provider, tools
call = {'name': 'check_service_status', 'args': {'service': 'vpn'}}
print(json.dumps(provider.function_response_message([(call, tools.dispatch(call['name'], call['args']))]), indent=2))
"

# the declarations now riding in every request — sends nothing, needs no key
uv run --frozen python run.py plan "Is the VPN down?"
```

`--frozen` is on every `uv run` here for the reason `PRIMER.md` §3 gives: plain `uv run` brings the
lockfile up to date before your command starts, so a check invoked that way inspects a repository
its own invocation just repaired. Today's commands need no key and reach no network.

## §4 Files this day prints

Two files printed whole, both new to the project, both in part 1.2. Two more are changed rather than
printed: `provider.py` and `loop.py` were printed whole by **day 4**, and today's parts show only
what is added, marked against those versions and headed with the real path. Nothing day 4 printed is
reprinted here except as diff context.

| File | Printed by |
| --- | --- |
| `projects/01-ask-desk/ask_desk/tools.py` | part 1.2, whole |
| `projects/01-ask-desk/ask_desk/data/notes.json` | part 1.2, whole |
| `projects/01-ask-desk/ask_desk/provider.py` | part 2.1, as a marked addition below `text_of`; day 4 printed the file whole |
| `projects/01-ask-desk/ask_desk/loop.py` | part 2.1, as marked diffs and one replaced method; day 4 printed the file whole |

## §5 Build brief

| File | What it must do |
| --- | --- |
| `projects/01-ask-desk/ask_desk/data/notes.json` | `TODO(me)`: type it. Before writing `tools.py`, say which single query word you expect to match a note it has nothing to do with, and which note. |
| `projects/01-ask-desk/ask_desk/tools.py` (the three functions) | `TODO(me)`: type them. Run `search_notes('vpn file share')` and say, out loud, why the third hit is what it is — naming the exact line in `search_notes` that produced it. |
| `projects/01-ask-desk/ask_desk/tools.py` (`DECLARATIONS`) | `TODO(me)`: write the three declarations by hand, then check each `properties` key against the parameter name in the signature above it. Say what would happen if one of them disagreed, and at which line the disagreement would surface. |
| `projects/01-ask-desk/ask_desk/tools.py` (`dispatch`) | `TODO(me)`: type it. Before running anything, predict which of `dispatch('lookup_ticket', ...)`, `dispatch('fetch_note', {})` and `dispatch('search_notes', {'q': 'vpn'})` raises and which return. Then run all three and say whether you were right. |
| `projects/01-ask-desk/ask_desk/provider.py` | `TODO(me)`: add `function_calls` and `function_response_message`. Say why `function_calls` returns a list rather than an optional single call, and what breaks on the day the model asks for two tools at once. |
| `projects/01-ask-desk/ask_desk/loop.py` | `TODO(me)`: add `MAX_CALLS_PER_QUESTION`, `LoopExhausted`, `use_tools`, the `tools=` argument in `next_request`, and the tool branch in `ask`. Run `run.py plan` before and after adding `use_tools`, with the flag both ways, and say exactly which key appears. |
| the round trip | `TODO(me)`: `provider.function_response_message` sends `"role": "user"`, and the provider's own page says two different things about that role. Read part 2.1's two quotations, then say which you would send and what evidence would settle it. |
| the failure rep | `TODO(me)`: rename `search_notes` to `find_notes` in the function definition and in `REGISTRY`, leave `DECLARATIONS` alone, and run `dispatch('search_notes', {'query': 'vpn'})`. Then put it back and do the reverse — rename the declaration's `query` property to `q` and dispatch with what the declaration now promises. |

## §6 The check that must be able to fail

```text
cd projects/01-ask-desk
uv run --frozen python run.py check    # the project's own gate — five checks, exit 0 or 1
echo $?
uv run --frozen python run.py plan "Is the VPN down?"   # the request, built and not sent
cd ../.. && python p.py depth 5        # this day against the plan §5 contract
```

**How to make it go red on purpose — four ways, and the third is the day's real one.**

The first is the store. Delete a comma in `notes.json` and every tool call fails at `_load` with
`json.decoder.JSONDecodeError`, naming the line and column. That is the cheapest possible proof that
the data file is code as far as this project is concerned.

The second is the registry. Rename `search_notes` to `find_notes` in the function and in `REGISTRY`,
leave `DECLARATIONS` alone, and dispatch the name the declaration still promises. `UnknownTool` is
raised, and the message tells you the declarations and the registry have drifted — which is exactly
what you just did to them, deliberately, for the first time.

The third is the day's deliberate failure and it is part 2.2. Dispatch a real tool with an argument
name the declaration says is right and the function has never heard of. It **does not raise**. It
returns a dictionary with an `error` key, the run continues, the model reads it, and if you are not
looking at the tool log the only thing you see is a polite answer that could not do what was asked.
Watch a failure that produces no traceback and no red line anywhere.

The fourth needs a key and is therefore a `TODO(me)` in part 2.2: set `MAX_CALLS_PER_QUESTION` to
`1`, ask a question that needs a tool, and watch `LoopExhausted` refuse a run that was going fine.

For the document itself: delete a `## In production` heading from any part and run
`python p.py depth 5`; it names the file and the missing section.

## §7 Request budget

**With tools, a question costs at least two provider calls, and at most six.**

Day 4's answer was one call per question and it was exact. Today it is a range, and the range is the
subject: the model replies with a tool call instead of an answer, you run the tool, you hand the
result back, and the model is asked again. That is two calls for the simplest tool-using question.
A question that searches, then fetches a note, then answers costs three. Search, fetch, status,
answer costs four.

The ceiling is `MAX_CALLS_PER_QUESTION = 6`, enforced in `ask_desk/loop.py` by code the model cannot
reach, and reaching it raises `LoopExhausted` rather than returning a partial answer. The cast is one
agent — the plan §11 gives P01 no second one — so six is the whole per-question count across the
whole cast, not a per-agent figure to be multiplied.

Two things about size rather than count. Every one of those calls resends the **entire**
conversation, because the endpoint is stateless, so the sixth request is several times the payload of
the first. And every request now carries all three declarations, whether or not any tool is used.

**The provider's own ceiling is not stated here, because it is not published.** The rate-limit page
says the numbers live in your account rather than on the page, so this document names where to read
them instead of printing a figure nobody can verify — see
`docs/adr/ADR-0004-generatecontent-by-hand-and-unpublished-limits.md`.

```text
TODO(me): read this project's actual free-tier request and token limits for gemini-3.8-flash in
Google AI Studio, and record them with today's date in projects/01-ask-desk/PACKAGES.md. Do not copy
a number from any blog, answer or cached page.
```

## §8 Traps

- **The model never sees your code.** Not the function, not the docstring, not the type hints —
  only the declaration you send. Every instinct that says "it can tell from the signature" is wrong
  today and becomes true on day 7, which is why the comparison is worth waiting for.
- **A wrong description raises nothing, ever.** It produces a tool called at the wrong moment, or a
  result used as though it contained something it does not. This is the only interface in the
  project where the documentation and the contract are the same object.
- **`required` is a list of names, and optional is spelled by absence.** There is no
  `"optional": true`. A parameter left out of `required` is optional; a parameter added to it that
  has a Python default is now compulsory for the model and nothing will point that out.
- **A Python default is invisible to the schema.** `limit: int = 3` puts nothing in the JSON. The
  declaration mentions the default in prose, so the model has to read English to learn it — and day
  7 shows a derived schema that carries `"default": 3` properly.
- **`function_declarations` in the request, `functionCall` in the response.** Snake case going out,
  camel case coming back. Normalising either one for tidiness produces a key the provider does not
  recognise.
- **`tools` is a list of tool objects, each holding a `function_declarations` array.** Two levels of
  nesting where one would seem to do, because the provider's own built-in tools are siblings of that
  array rather than entries in it.
- **A turn may carry several `functionCall` parts.** Code that reads `parts[0]` works for months and
  then silently drops the second call on the day the model asks for two.
- **The model's tool-call turn is part of the conversation.** File it before the result. A
  `functionResponse` sitting in the thread with nothing above it is a result nobody asked for, and
  the model reads the thread exactly as literally as it looks.
- **The documentation contradicts itself about the tool-result turn's role.** `Content.role` is
  documented as "either 'user' or 'model'", and the prose beside `Tool.functionDeclarations` uses
  `"function"`. Part 2.1 quotes both. We send `"user"`; the observed behaviour is a `TODO(me)`,
  because there is no working key on this machine.
- **Do not assume `finishReason` for a successful function call.** The enum documents
  `MALFORMED_FUNCTION_CALL`, `UNEXPECTED_TOOL_CALL` and `TOO_MANY_TOOL_CALLS` and no value for the
  ordinary case. Branch on the presence of a `functionCall` part, record the finish reason, trust it
  for nothing.
- **An unknown tool name must raise, and a nearest-match is the worst available fix.** It runs code
  nobody asked for, labels the result with a tool that was never called, and writes no log line that
  would show it.
- **Bad arguments must not raise.** They come back as an `error` result, which the provider
  documents as a legitimate response, so the model can correct itself inside the same question. Echo
  the arguments that arrived, or it will send them again.
- **`except TypeError` is wider than argument binding.** A genuine `TypeError` from inside a tool
  gets dressed up as a friendly message to the model and never reaches your logs.
- **A loop that ends when the model stops asking for tools ends when the model chooses to.** The
  bound belongs in code, not in the system instruction — anything expressed in the conversation is a
  request, not a limit.
- **`LoopExhausted` must raise rather than return the last partial text.** A run that hit its limit
  and a run that answered are then indistinguishable to the caller and to the log.
- **Substring scoring matches inside words.** `share` matches `shared`, which is why a mail note
  ranks against a VPN question in part 1.2's transcript. Nothing raises; only a retrieval eval
  catches it, and that is P18.
- **A tool must return JSON-serialisable values.** Your own objects work perfectly in a test and
  fail at the moment the result crosses the wall.
- **The project's day numbers are not the curriculum's.** `# ── added on day 2, for tools ──` in
  `provider.py` means this project's day 2, which is curriculum day 5. Every project counts its own
  days, because a project copied elsewhere has no idea what curriculum it came from.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| The declarations now ride in the request | `uv run --frozen python run.py plan "Is the VPN down?"` | 2026-09-09 | a `"tools"` key holding `function_declarations`; everything above it byte-identical to day 4's request — part 1.1 |
| The name constraint on a function call | `https://ai.google.dev/api/generate-content` | 2026-09-09 | verbatim: "Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 128." |
| `Content.role` is documented as two values | `https://ai.google.dev/api/generate-content` | 2026-09-09 | verbatim: "The producer of the content. Must be either 'user' or 'model'." |
| The same page uses a third value for the tool-result turn | `https://ai.google.dev/api/generate-content`, `Tool.functionDeclarations` | 2026-09-09 | verbatim: "The next conversation turn may contain a FunctionResponse with the `Content.role` \"function\" generation context for the next model turn." **Contradicts the row above; part 2.1 names it and does not resolve it silently.** |
| An `error` key is a documented response shape | `https://ai.google.dev/api/generate-content`, `FunctionResponse.response` | 2026-09-09 | verbatim: "if the function call failed to execute, the response can have an \"error\" key to return error details to the model." |
| No `finishReason` is documented for a successful function call | `https://ai.google.dev/api/generate-content`, `FinishReason` | 2026-09-09 | the enum carries `MALFORMED_FUNCTION_CALL`, `UNEXPECTED_TOOL_CALL` and `TOO_MANY_TOOL_CALLS`; nothing for the ordinary case. Not asserted anywhere in this day — it is a `TODO(me)` in part 2.1 |
| The three tools run with no model and no key | `uv run --frozen python -c "... tools.search_notes('vpn file share') ..."` | 2026-09-09 | three hits, `count: 3`, `limit` defaulted to 3 — part 1.2 |
| Substring scoring returns a wrong third hit | the same command | 2026-09-09 | KB-311, a `mail` note, ranked against a VPN query because "share" is inside "shared mailbox". Named in part 1.2 rather than hidden; P18 is where retrieval evals catch it |
| A missing note returns rather than raises | `tools.fetch_note('KB-999')` | 2026-09-09 | `{"error": "no note with id 'KB-999'", "known_ids": [...five ids...]}`, exit normal |
| `check_service_status` reads the store | `tools.check_service_status('vpn')` | 2026-09-09 | `degraded`, since `2026-09-09T06:40:00Z`, with the gateway note — all synthetic |
| An unknown tool name raises | `tools.dispatch('lookup_ticket', {'id': 'T-1'})` | 2026-09-09 | `UnknownTool`, naming the three known tools and diagnosing drift — part 2.2 |
| A missing required argument returns an error dict | `tools.dispatch('fetch_note', {})` | 2026-09-09 | `fetch_note() missing 1 required positional argument: 'note_id'`, carried verbatim into the `error` string |
| A wrong argument name returns an error dict | `tools.dispatch('search_notes', {'q': 'vpn'})` | 2026-09-09 | `search_notes() got an unexpected keyword argument 'q'`, with `arguments_received` echoed |
| The tool-result turn is built as documented | `provider.function_response_message([(call, result)])` | 2026-09-09 | `{"role": "user", "parts": [{"functionResponse": {"name": ..., "response": {...}}}]}` — the `functionCall` in that command is a stand-in written in the command, and part 2.1 says so |
| The hand-rolled path against a bad key is 400 | `uv run --frozen python run.py ask "Is the VPN down?"` | 2026-09-09 | `the provider refused this request: HTTP 400: 'API key not valid. Please pass a valid API key.'`, exit `1`. The provider's error table lists an invalid key as 401; the observation disagrees, and the observation is what is recorded |
| `generateContent` is still supported | `https://ai.google.dev/gemini-api/docs/migrate-to-interactions` | 2026-09-09 | verbatim: "While `generateContent` remains fully supported, we recommend the Interactions API for all new development." — the choice is ADR-0004's |
| No rate-limit number is publishable | `https://ai.google.dev/gemini-api/docs/rate-limits` | 2026-09-09 | verbatim: "Rate limits depend on a variety of factors (such as your usage tier) and can be viewed in Google AI Studio." and "Specified rate limits are not guaranteed and actual capacity may vary." No RPM, TPM or RPD figure appears; §7 states none |
| The toolchain has not moved | `uv --version`, `python --version` inside the project | 2026-09-09 | uv 0.12.3, CPython 3.12.12 — re-observed, not assumed |

## §10 Ledger & commit

**`docs/PROGRESS.md`:**

```text
| 5 | 2026-09-09 | TL-01 | 4 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the terms this day defined for the first time:

```text
| Function declaration | The JSON object a model is given for one of your functions: a name, a prose description, and a JSON Schema for the arguments. It is the entire interface — the model never sees the code — and nothing checks that it describes the function correctly. | day 5 part 1.1 | tool declaration, the schema |
| JSON Schema | A standard vocabulary for describing the shape of a JSON value: its type, its named properties, and which of them are required. Used here to tell a model what an argument bag must look like, and it says nothing about defaults. | day 5 part 1.1 | the parameters schema |
| Tool call | A part of a model's reply that names a tool and carries an object of arguments, in place of the text it would otherwise have written. It is a request made of your program: the model cannot run anything itself. | day 5 part 2.1 | function call, `functionCall` |
| Tool-result turn | The message you append after running a tool, carrying one `functionResponse` part per call with the tool's return value verbatim. It is what makes one question cost at least two provider calls. | day 5 part 2.1 | the function response, the result turn |
```

**`docs/PINS.md`** — nothing to add. No package, interpreter or model version moved today; the pins
are as day 4 left them, and re-recording an unchanged value would make the ledger's rows stop
meaning "something changed".

**`docs/SOURCES.md`** — nothing to add. Everything cited today is provider documentation quoted with
its URL and the date it was read, which §9 is for; none of it is a record with a resolvable
identifier. This is the same call days 1 to 4 made.

**`projects/01-ask-desk/PACKAGES.md`** — no row yet, and one is owed. Both `TODO(me)` items in §7
and part 2.1 end by recording an observation there once a working key exists.

**Commit:**

```text
day 05: P01 Ask Desk · 2 — Tools by hand: JSON schemas and the tool-result turn — closes TL-01
```
