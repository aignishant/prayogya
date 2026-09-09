---
project: "P01 Ask Desk"
day: 7
phase: P01
title: "P01 Ask Desk · 4 — `FunctionTool`, and what ADK does that you just did yourself"
ids: [TL-02]
kind: concept
deploy_tier: D1
plan_version: "v3.1.0"
parts: 4
files_printed: []
generated: "2026-09-09"
status: written
commit: ""
---

> **Yesterday:** an ADK agent that answers, with its model pinned explicitly and three plain
> functions handed to it in a list.
> **Today:** open the declarations that list produced, hold them against the ones you typed by hand
> on day 5, and find out which of the two is better and at what.
> **Tomorrow:** the event stream — where the tool call and the tool result actually go past, and
> where a bound can be counted.

## §1 The scene

You take your old paperwork to a counter and ask for a new form to be made up. The clerk does not
interview you. They lay your papers flat, read across them, and copy each box into the new form: the
name at the top, the entries, the note you scribbled in the margin years ago and meant nothing by.
It is quick and it is exact, and the form that comes back is neater than the one you brought in.

Then you read it properly. The name is right. The dates are right — better than right, because
things you had written as a sentence in the margin are now in the box the form has for them. But the
one thing that mattered, the thing you would have said out loud if anyone had asked, is not on the
form anywhere, because it was never on the paper. Nobody asked. And where you had left a box empty,
the form does not have an empty box: the clerk reached for the office's standard rubber stamp, and
the finished form now says something in that box about the office rather than about you.

That is this whole day. Day 6 handed three plain functions to an agent and three declarations came
out — you did not write them, you did not see them, and they went to the model. Today you open them.
Most of what the clerk copied is better than what you typed. One thing you typed has no equivalent
and is simply gone. And there is a box you can leave empty by deleting a single line, after which
your status tool tells the model that its purpose is to call itself, and every check in this
project stays green.

## §2 The map

Two sections, and the order is the argument. The first reads the boxes the clerk copied *from your
paperwork* — the ones that are facts about the function, where derivation is straightforwardly
better than typing. The second reads the boxes you did not know you were filling in, and then does
the accounting: what the framework took, what it lost, and what it never touched.

### 1 · What the wrapper reads

*The mental model: a clerk copying an existing form. Every box on the new form came from a box on
the old one, and nothing was invented on the way across.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-what-the-wrapper-reads/1.1-the-function-is-the-tool.md) | The function is the tool | Where does the name on the declaration come from, and when did day 6 start deriving it? | foundation |
| [1.2](parts/01-what-the-wrapper-reads/1.2-the-type-hints-are-the-schema.md) | The type hints are the schema | What does the signature give the model, and what does an unannotated parameter take away? | working |

### 2 · What it reads that you did not mean to write

*The mental model: the same clerk, now copying the margin note and stamping the empty box — and a
ledger written afterwards, in both directions.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-what-it-reads-that-you-did-not-mean-to-write/2.1-the-docstring-is-the-description.md) | The docstring is the description | What reaches the model from a docstring, and what reaches it from a missing one? | production |
| [2.2](parts/02-what-it-reads-that-you-did-not-mean-to-write/2.2-what-it-did-and-what-it-did-not.md) | What it did, and what it did not | Which of the six things days 4–6 built by hand does the framework now own? | production |

## §3 Setup — run this

Nothing to install. `google-adk==2.8.0` has been in `pyproject.toml` since day 6 and today adds no
dependency, no file and no line of project code. Everything below reads code this project already
has and prints what it found; every one of them was run on this machine today and what they reported
is in §9. Run them in order, from the project folder.

```bash
cd projects/01-ask-desk

# part 1.1 — the three FunctionTool objects day 6's `tools=[...]` list produced
uv run --frozen python -c "
import asyncio, warnings
warnings.filterwarnings('ignore')
from ask_desk.agent import desk
async def main():
    for tool in await desk.canonical_tools():
        print(f'{type(tool).__name__:14} {tool.name}')
asyncio.run(main())
"

# part 1.2 — the declaration derived from search_notes, in full
uv run --frozen python -c "
import json, warnings
warnings.filterwarnings('ignore')
from google.adk.tools import FunctionTool
from ask_desk import tools
d = FunctionTool(tools.search_notes)._get_declaration()
print('name       ', d.name)
print('description', repr(d.description))
print(json.dumps(d.parameters_json_schema, indent=2))
"

# part 2.1 — the three descriptions, side by side. Run before and after the break.
uv run --frozen python -c "
import warnings; warnings.filterwarnings('ignore')
from google.adk.tools import FunctionTool
from ask_desk import tools
for f in (tools.search_notes, tools.fetch_note, tools.check_service_status):
    print(f'  {f.__name__:22} {FunctionTool(f).description!r}')
"

# the project's own gate, unchanged since day 6 — and green through today's break
uv run --frozen python run.py check
echo $?
```

`--frozen` is on every `uv run` for the reason day 3 gave: without it, `uv run` updates the lockfile
before your command starts, and a command that repairs the repository before inspecting it is not an
observation.

## §4 Files this day prints

**None, and that is the day rather than a gap in it.**

| File | Printed by |
| --- | --- |
| — | — |

Everything this day examines was already printed whole, in this project, by the two days before it.
`ask_desk/tools.py` and `ask_desk/data/notes.json` were printed by **day 05 part 1.2**;
`ask_desk/agent.py` was printed by **day 06 part 1.1**. Today's subject is what the framework
*derived* from those files — objects that exist at runtime and are written down nowhere — so there
is nothing new to type and nothing to add to `CODEMAP.md`. That file already carries the note, under
the heading *Day 07 prints nothing*, so the absence is on the record rather than discovered later.

The parts do quote from `tools.py` and `loop.py`, in small excerpts marked `── unchanged from day 05
part 1.2 ──` and equivalents, which is the plan §5.1 form for referring to code this project has
already printed. A day that invented a file so this table would have a row in it would be a worse
day.

## §5 Build brief

Nothing to type into `ask_desk/`. The reps are experiments on code that is already there, and one of
them is the check this project does not yet have.

| What you act on | What it must do |
| --- | --- |
| `ask_desk/agent.py`, read only | `TODO(me)`: before running anything, predict what `desk.canonical_tools()` returns for a list of three plain functions — the objects and their names. Then run it. Then `grep -n search_notes ask_desk/agent.py` and say where the name the model receives actually comes from. |
| `ask_desk/tools.py`, read only | `TODO(me)`: derive the declaration for all three tools. Predict which will carry a `default` key before you look, and say what in each signature decides it. |
| a probe you write | `TODO(me)`: copy `search_notes`'s signature into a throwaway function with the annotations removed, derive its schema, and name every key that disappeared and every key that survived. |
| the declaration audit | `TODO(me)`: write a command that walks `desk.canonical_tools()`, derives each declaration, and prints `RED` plus a message for any tool whose description is empty or equal to `'Call self as a function.'`, and for any schema property with no `type` key. It must exit non-zero when it finds one — day 3 part 2.2 is why that sentence is not optional. This project has no such check today, which is why §6's failure is invisible. |
| the failure rep | `TODO(me)`: delete the one-line docstring from `check_service_status` in `ask_desk/tools.py`, derive all three descriptions, and watch `'Call self as a function.'` appear in the third row. Run `uv run --frozen python run.py check` and `echo $?` with the break still in place. Then run your audit against it. Put the docstring back and run all three again. |
| the behavioural half | `TODO(me): run uv run --frozen python run.py adk "Is the VPN down?"` with a working `GOOGLE_API_KEY`, once with the docstring deleted and once restored, and record what the model actually does. There is no valid key on this machine, so nothing in this day's documents claims an answer. |
| the arc | `TODO(me)`: from part 2.2's table, recite the three things in the last column without looking, and for each say what would happen on the day somebody assumed the framework had taken it over. |

## §6 The check that must be able to fail

```text
cd projects/01-ask-desk
uv run --frozen python run.py check    # the project's gate — five green since day 6
echo $?                                # 0 green, 1 red, 2 you typed it wrong
<your declaration audit>               # the sixth check, from §5. Does not exist yet.
cd ../.. && python p.py depth 7        # this day against the plan §5 contract
```

**The red state is where you are standing right now, and it is worth naming before you fix it.**
Delete the docstring from `check_service_status`, derive the three descriptions, and the third one
reads `'Call self as a function.'` Then run `run.py check`: five green, `0 problem(s)`, exit `0`.
Nothing in this project — not the gate, not a linter, not a type checker, not review, since the diff
is one deleted line — can see that one of three tools has stopped telling the model what it is for.
That was run today and the transcript is in part 2.1.

So the check that must be able to fail is the one §5 asks you to write, and until it exists the
honest description of this project is *unprotected against its own commonest tool bug*. Once it
exists, make it go red on purpose three ways, and all three are one edit each:

The first is the docstring, above. The second is an annotation: change `limit: int = 3` to
`limit=3` in `search_notes` and the derived property loses its `type` key entirely, which part 1.2
shows and which a schema validator would accept without comment. The third is a name: rename
`fetch_note` and leave day 5's `DECLARATIONS` untouched — the derived tool follows the rename, the
hand-written declaration does not, and the two halves of `tools.py` now disagree about what this desk
offers.

For the document itself: delete a `## In production` heading from any part and run
`python p.py depth 7`; it names the file and the missing section.

## §7 Request budget

**Zero model calls. Every command in this day is local introspection.**

Deriving a declaration reads a function object — its `__name__`, its signature, its `__doc__` — and
builds a JSON Schema in memory. It contacts nothing, needs no key, and consumes no quota. That is
true of all four parts: the `canonical_tools` walk, the `_get_declaration()` probes, the three-tool
description comparison, the untyped-signature comparison and the `run.py check` runs. The `TypeError`
in part 2.2 is raised by `run_async` before any request is constructed. A key is neither needed nor
present.

Stating the zero matters because it is exactly what makes the day's one `TODO(me)` honest. The
*behavioural* half of part 2.1's failure — what a model does when told a tool's purpose is to call
itself — is the only thing here that would cost requests, and it is marked as unrun rather than
guessed at.

For the days that do call out, the ceiling is still unknown and still not invented. Plan §9 and this
project's `PACKAGES.md` both record that the provider's rate-limit page publishes no RPM, TPM or RPD
figure and directs you to Google AI Studio instead. That `TODO(me)` stands: read this project's live
limits there and paste them, with the date. Until then the hubs state the request count, which is a
fact about this project's own code, and no number for the ceiling, which is not.

## §8 Traps

- **The declarations were already derived on day 6.** `tools=[tools.search_notes, ...]` wrapped each
  function the moment the agent was constructed. Nothing in `agent.py` says `FunctionTool` and three
  of them exist. If you were still picturing day 5's `DECLARATIONS` riding along, you were a day
  behind.
- **Day 5's `DECLARATIONS` is still in `tools.py` and is now unused by the agent.** It is kept
  deliberately, as the thing today compares against. Two descriptions of one tool in one file is a
  drift hazard the moment anybody forgets which is live.
- **The whole docstring is the description, not the summary line.** Blank line, warnings, the stale
  sentence about behaviour you removed last month — all of it, on every turn.
- **A missing docstring is not an empty description.** It is `'Call self as a function.'`, because
  `__call__.__doc__` is there when `__doc__` is not. Nothing raises and nothing warns.
- **No default linter configuration treats a missing docstring as an error.** This is why the failure
  survives review and CI: every gate you have agrees the diff is fine.
- **A parameter with no type annotation produces a schema property with no `type` key.** Not
  `"any"` — absent. The property constrains nothing, and the failure lands later, inside your
  function, as an `AttributeError` day 5's dispatcher does not catch.
- **`"title": "Query"` is not a description.** It is the parameter name with a capital letter. Every
  per-parameter `description` day 5 wrote has no counterpart in the derived schema.
- **`check_service_status`'s known-service list lived in a parameter description** — `"One of: vpn,
  printing, mail, identity."` — and derivation drops it. If the model needs those names, they now
  have to be in the docstring.
- **`_get_declaration()` has a leading underscore.** It is a fine window and a terrible door: use it
  in probes, never in `ask_desk/`.
- **`functools.partial` derives the name `partial`.** Two partials in one `tools` list produce two
  tools with the same name and no complaint. A lambda derives `<lambda>`, which contains characters
  the provider's documented name rule does not admit.
- **A name longer than the documented 128 characters is copied without comment.** 138 was observed
  here. Whatever happens to it happens at the far end of a request.
- **`tools=['search_notes']` is a pydantic `ValidationError`, three errors for one mistake.** The
  first line is the one that matters: *Input should be callable*. There is no registry to look a name
  up in any more.
- **The runner takes no bound.** `run_async(..., max_calls=6)` is a `TypeError`. ADK runs the loop; it
  does not cap it. `MAX_CALLS_PER_QUESTION` is still this project's own code and still the only
  ceiling that exists.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| Day 6's `tools=[...]` produced `FunctionTool` objects | `desk.canonical_tools()` under `asyncio.run` | 2026-09-09 | three rows, `FunctionTool` each, named `search_notes`, `fetch_note`, `check_service_status` — part 1.1 |
| The tool name is the function's `__name__` | `FunctionTool(fn).name == fn.__name__` over the three tools and a 138-character probe | 2026-09-09 | `True` on all four; lengths 12, 10, 20 and 138 — the last past the documented 128 maximum, with no exception, warning or truncation |
| A `functools.partial` and a lambda derive names anyway | `FunctionTool(lambda query: {}).name`, `FunctionTool(partial(search_notes, limit=1)).name` | 2026-09-09 | `'<lambda>'` and `'partial'`; two partials in one `tools` list gave `['partial', 'partial']` with no complaint |
| A tool name string is refused, a function is not | `Agent(name='by_name', model='gemini-3.8-flash', tools=['search_notes'])` | 2026-09-09 | `ValidationError: 3 validation errors for LlmAgent`, first being *Input should be callable* — part 1.1 |
| The derived schema for `search_notes` | `FunctionTool(tools.search_notes)._get_declaration()` | 2026-09-09 | `query` → `{"title": "Query", "type": "string"}`; `limit` → `{"default": 3, "title": "Limit", "type": "integer"}`; `required: ["query"]` — part 1.2 |
| ADK derives a `default` the hand version only had as prose | the same declaration against `tools.DECLARATIONS[0]` | 2026-09-09 | `"default": 3` is a field in the derived schema; day 5 carried the same fact as the sentence `"Maximum notes to return. Defaults to 3."` |
| An unannotated parameter yields a property with no `type` | the same signature retyped as `search_notes_untyped(query, limit=3)` | 2026-09-09 | both `type` keys absent; `default` and `required` still correct; nothing raised or warned |
| The unconstrained value fails inside the tool, not at the boundary | `tools.dispatch('search_notes', {'query': 3})` | 2026-09-09 | `AttributeError: 'int' object has no attribute 'lower'`, uncaught — day 5's dispatcher catches `TypeError` only |
| The whole docstring becomes the description | `FunctionTool(restart_service).description` on a probe with a two-sentence warning after a blank line | 2026-09-09 | `'Restart one service.\n\nOnly ever call this after check_service_status shows the service is degraded.\nRestarting an operational service drops every session on it.'` |
| A function with no docstring is described as calling itself | `FunctionTool(restart_service_2).description` | 2026-09-09 | `'Call self as a function.'` — and `f.__doc__` is `None` while `f.__call__.__doc__` is that same string |
| The same failure on this project's real tools | the one-line docstring deleted from `check_service_status` in `ask_desk/tools.py`, three descriptions derived together | 2026-09-09 | two correct rows and `check_service_status   'Call self as a function.'`; restoring the line brought the description straight back |
| No check in this project can see it | `uv run --frozen python run.py check` with the docstring still deleted | 2026-09-09 | `green keys / interpreter / pins / lock / model`, `0 problem(s)`, `echo $?` → `0` |
| Every per-parameter description is lost in derivation | hand-written `description` against the derived property keys, all three tools | 2026-09-09 | four parameters, four `description` strings, and `['title', 'type']` (plus `default` on `limit`) derived — the key `description` appears zero times |
| The runner accepts no bound | `run_async(..., max_calls=6)` on the runner `agent.py` builds | 2026-09-09 | `TypeError: Runner.run_async() got an unexpected keyword argument 'max_calls'` — part 2.2 |
| `FunctionTool`'s documented signature and purpose | `https://adk.dev/api-reference/python/google-adk.html` | 2026-09-09 | `class google.adk.tools.FunctionTool(func, *, require_confirmation=False)` — "A tool that wraps a user-defined Python function." |
| The framework wraps plain functions for you | `https://adk.dev/tools-custom/function-tools/` | 2026-09-09 | "When you assign a function to an agent's `tools` list, the framework automatically wraps it as a `FunctionTool`." |
| The provider's constraint on a tool name | `https://ai.google.dev/api/generate-content` | 2026-09-09 | "Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 128." |
| Rate limits are still unpublished | `https://ai.google.dev/gemini-api/docs/rate-limits` | 2026-09-09 | "Rate limits depend on a variety of factors (such as your usage tier) and can be viewed in Google AI Studio" — no RPM, TPM or RPD figure; §7's `TODO(me)` stands |
| Toolchain versions | `uv --version`, `python --version`, `import google.adk` | 2026-09-09 | uv 0.12.3, CPython 3.12.12 inside the project, google-adk 2.8.0 — re-observed, not assumed |

## §10 Ledger & commit

**`docs/PROGRESS.md`:**

```text
| 7 | 2026-09-09 | TL-02 | 4 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the terms this day defined for the first time. Check the file before
appending: day 5 is expected to add a row for the hand-written **function declaration**, and if it
is there, these two link to it rather than restating it.

```text
| FunctionTool | ADK's wrapper around a plain Python function, which derives the model-facing declaration from the function object itself — name from `__name__`, parameter schema from the signature, description from the docstring. Assigning a function to an agent's `tools` list creates one automatically. | day 7 part 1.1 | the wrapper |
| Derived declaration | A tool declaration the framework builds by reading a function, as against one written by hand beside it. It cannot drift from the function, and it can only carry what the function already contains — which is why a per-parameter description has nowhere to live in one. | day 7 part 1.2 | the derived schema |
```

**`docs/PINS.md`** — nothing to add. Today observed no version this repository does not already
record: `projects/01-ask-desk/PACKAGES.md` carries google-adk 2.8.0 from day 4, and uv 0.12.3 and
CPython 3.12.12 are already in `docs/PINS.md` from days 1 and 3. Re-observations are dated in §9,
which is what that table is for.

**`docs/SOURCES.md`** — nothing to add. This day cites two framework documentation pages and one
provider API reference page, none of which is a record with a resolvable identifier. All three are
dated in §9. Same call days 1, 2 and 3 made.

**Commit:**

```text
day 07: P01 Ask Desk · 4 — FunctionTool, and what ADK does that you just did yourself — closes TL-02
```
