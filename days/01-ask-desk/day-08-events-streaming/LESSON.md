---
project: "P01 Ask Desk"
day: 8
phase: P01
title: "P01 Ask Desk · 5 — Events and streaming: the 2.x event model"
ids: [AG-03]
kind: mechanism
deploy_tier: D1
plan_version: "v3.1.0"
parts: 5
files_printed:
  - "projects/01-ask-desk/ask_desk/scripted.py"
  - "projects/01-ask-desk/ask_desk/agent.py"
  - "projects/01-ask-desk/run.py"
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** the declarations ADK derives from your functions, an honest ledger of what the
> framework took and what it left, and a bound you found on `RunConfig` but could not make fire.
> **Today:** stop keeping one event and dropping the rest — read the whole stream, find out which
> event is the answer, turn streaming on and watch three events become nineteen, then watch the
> bound fire.
> **Tomorrow:** sessions across more than one question, and errors that surface instead of hiding.

## §1 The scene

You are following a race you cannot see. Somebody at the track has a phone to their ear and is
telling you what is happening, and your one job is to write the result down correctly.

Three things reach you. Somebody says they are going to check the timing board. Somebody reads out
what the board said. And then there is the sentence you actually rang up for. Only the last one is
the result — and the first two are not noise, they are the reason the third one is trustworthy
rather than invented. Up to now you have been listening for the sentence and letting the rest go
past, which works fine until you are the one running a screen in the shop, and everybody watching it
sees nothing at all for the whole time the work is being done.

So you ask the commentator to talk *while* it happens rather than only at the end. Now the words
arrive one at a time, sixteen of them for one sentence, and the screen moves and nobody thinks the
line has gone dead. But two new problems arrive with the arrangement. At the end, being a
professional, the commentator reads the whole result back cleanly — and if you have been writing
down every single thing that came down the line, your page now has the result on it twice, joined
with nothing, and every word of it was genuinely said. And somewhere behind all of this there is an
operator at the exchange with a rule: after three connections to the track, the line comes down. The
operator counts connections. You have been counting messages. Those are different numbers, and the
day you find out how different is the day one of them is set wrongly.

One more thing about today, and it is the part that makes the rest possible. You cannot rehearse any
of this against a real race, because there is no rerun and every one is different. So the whole day
runs against a colleague in another room reading a written commentary down the line: the same words
every time, no key, no cost, and two rules nailed to the wall so that nobody ever files a rehearsal
as a result.

## §2 The map

Two sections, and the order is a widening. The first watches a single ordinary run and works out
what the pieces of it are — the stand-in that makes watching possible at all, and then the three
events one question produces. The second turns the stream on and reads what changes: the shape of
it, the failure hiding in the obvious way to consume it, and the ceiling that decides how long any
of it may go on for.

### 1 · Watching

*The mental model: setting up so you can listen to the same commentary twice, and then listening to
it once, carefully.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-watching/1.1-the-stand-in-that-lets-you-watch.md) | The stand-in that lets you watch | Why does this project carry a fake model, and what stops it being mistaken for a real one? | foundation |
| [1.2](parts/01-watching/1.2-what-an-event-is-and-which-one-is-the-answer.md) | What an event is, and which one is the answer | One question produces three events — what are the other two, and what do they carry? | working |

### 2 · The stream

*The mental model: the same line, now carrying a word at a time — more messages, the same race, and
two things at the end that catch people.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-stream/2.1-nineteen-events-for-one-sentence.md) | Nineteen events for one sentence | What does the streaming switch change, and what does `partial` actually mark? | working |
| [2.2](parts/02-the-stream/2.2-the-answer-that-arrived-twice.md) | The answer that arrived twice | Why does the obvious accumulator produce exactly double the answer? | production |
| [2.3](parts/02-the-stream/2.3-the-bound-seen-firing.md) | The bound, seen firing | What does `max_llm_calls` actually count, and what does it look like when it fires? | production |

## §3 Setup — run this

No new dependency. `google-adk==2.8.0` has been in `pyproject.toml` since day 6, and today adds one
new file, two marked diffs and no third-party package. Every command below was run on this machine
on 2026-09-10 and what each reported is in §9. Run them in order, from the project folder.

```bash
cd projects/01-ask-desk

# part 1.1 — the new file. Create it empty; the part prints it whole.
touch ask_desk/scripted.py

# part 1.1 — the double identifies itself, by construction
uv run --frozen python -c "
from ask_desk import scripted
m = scripted.ScriptedModel(scripted.LOOKS_IT_UP, name='looks-it-up')
print(m.model, '| calls so far:', m.calls)
"

# part 1.2 — three events for one question, no key and no network
uv run --frozen python run.py events

# part 2.1 — the same question with the switch thrown
uv run --frozen python run.py events --stream

# part 2.1 — the three positions of the switch, read off the enum itself
uv run --frozen python -c "
from google.adk.agents.run_config import StreamingMode
for mode in StreamingMode:
    print(f'{mode.name:5} {mode.value!r}')
"

# the project's gate, unchanged since day 6 — and it must stay green through today
uv run --frozen python run.py check
echo $?
```

`--frozen` is on every `uv run` for the reason `PRIMER.md` §3 gives: plain `uv run` updates the
lockfile before your command starts, and a command that repairs the repository before inspecting it
is not an observation.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `projects/01-ask-desk/ask_desk/scripted.py` | part 1.1, whole, full depth — new today |
| `projects/01-ask-desk/ask_desk/agent.py` | part 1.1, marked diff (`build_desk`, `build_runner`'s agent seam) · part 2.1, marked diff (`run_config`) — the whole file was printed by day 06 part 1.1 |
| `projects/01-ask-desk/run.py` | part 1.2, marked diff (the `events` subcommand) — the whole file was printed by day 04 part 2.1, and day 06 part 2.1 added `adk` |

`CODEMAP.md` gains one row for `ask_desk/scripted.py` and two amendments; the exact text is in §10.
Note that `ask_desk/agent.py` is diffed twice today, in two different parts, and that is deliberate
rather than an oversight: the two changes have different subjects and arrived for different reasons,
and merging them into one block would hide that the streaming switch and the seam for a stand-in
model are unrelated decisions.

## §5 Build brief

Type `ask_desk/scripted.py` yourself from part 1.1 rather than pasting it — it is the only new file
today and it is the one that makes every other command in this day runnable. Everything else is two
small diffs and a set of experiments. Leave every `TODO(me)` unsolved.

| File | What it must do |
| --- | --- |
| `ask_desk/scripted.py` | `TODO(me)`: type it whole from part 1.1. Before running anything, predict what `ScriptedModel(LOOKS_IT_UP).model` returns and how many `LlmResponse` objects one non-streaming `Say` step yields. Then check both. |
| `ask_desk/agent.py` | `TODO(me)`: apply part 1.1's diff — the `BaseLlm` import, the sessions import, `build_desk`, and `build_runner`'s `agent` parameter. Then say why `model if model is not None else ...` is written that way rather than `model or ...`, and construct the one argument value that makes the difference visible. |
| `ask_desk/agent.py` | `TODO(me)`: apply part 2.1's diff — `run_config()` and the `run_config=` argument in `ask()`. Day 7's hub §5 asked you for the `max_llm_calls` half of this. If you did it then, reconcile what you wrote with what part 2.1 prints and say which you prefer and why. |
| `run.py` | `TODO(me)`: apply part 1.2's diff, then run `uv run --frozen python run.py events` and `--stream`. Predict the event count of the second before you run it, from the sentence alone. |
| `run.py`, the import | `TODO(me)`: move `from google.adk.sessions import InMemorySessionService` out of `events` and up to the top of `run.py`, where an editor would have put it. Confirm that everything still works and that nothing goes red. Then prove what it cost: run `python -c "import sys, importlib; importlib.import_module('run'); print('google.adk' in sys.modules)"` before and after. Put it back, and say what would have to exist in this repository for that change to have gone red on its own rather than needing somebody to know the rule. |
| a probe you write | `TODO(me)`: write the two-accumulator experiment from part 2.2 yourself, then extend it with a **third** accumulator that is correct — the one that ends up holding 84 characters and would still hold 84 if the final event carried only the last word. Say what you had to assume, and how you would find out whether the assumption holds against a different model. |
| `ask_desk/agent.py`, read only | `TODO(me)`: `ask()` calls `run_config()` with no arguments, so the desk's own answer path never streams. Decide whether that is right for this project and say what would have to change about `ask`'s signature for streaming to be worth turning on there. |
| the drift check | `TODO(me)`: `build_desk` repeats the four arguments of the module-level `desk`, so the instruction and the tool list now exist twice in one file. Write a check that fails when the two disagree, make it part of `run.py check`, and make it go red by changing one of the two. Day 3 part 2.2 is why "fails" has to mean a non-zero exit. |
| the bound | `TODO(me)`: run part 2.3's probe, then again with `max_llm_calls=6`. Record both event counts. Then say — without running it — what event count you would expect at the inherited default of 500, and why you would rather not find out. |
| the behavioural half | `TODO(me): run uv run --frozen python run.py adk "Is the VPN down?"` with a working `GOOGLE_API_KEY`, and record whether a real model's stream also repeats the whole answer in its final event. There is no valid key on this machine, so nothing in this day's documents claims an answer to that. |

## §6 The check that must be able to fail

```text
cd projects/01-ask-desk
uv run --frozen python run.py check        # the project's gate — five green since day 6
echo $?                                    # 0 green, 1 red, 2 you typed it wrong
uv run --frozen python run.py events       # three events; the classification must read correctly
uv run --frozen python run.py events --stream   # nineteen
cd ../.. && python p.py depth 8            # this day against the plan §5 contract
```

**Make it go red on purpose, three ways, one edit each — and the first two are the important pair,
because one of them the gate catches and the other it cannot.**

The first is caught. Delete `name="ask_desk"` from `build_desk` in `ask_desk/agent.py` and run
`run.py events`: the agent is a pydantic model with a required field, and it refuses before a single
event exists. That is the gate working.

The second is not caught, and it is the day's point. In the `events` function, change
`if event.partial: ...` reasoning at the call site — or, more simply, take part 2.2's accumulator and
drop the `if e.partial` clause. Every command in this project stays green. `run.py check` reports
five green and exits `0`. The answer is now stored twice and nothing in this repository objects,
because this project has no check whose subject is the *content* of an answer. That check arrives
with the evals on this project's last day, and until then the honest description of this desk is
that it cannot tell a doubled answer from a correct one.

The third breaks the count rather than the content. Set `max_llm_calls=0` in `run_config()` and run
part 2.3's runaway probe: the bound is disabled entirely — zero means no limit, not no calls — and
the run does not stop. Put the six back.

For the document itself: delete a `## In production` heading from any part and run
`python p.py depth 8`; it names the file and the missing section.

## §7 Request budget

**Zero model calls. Every command in this day runs against the scripted stand-in from part 1.1.**

`run.py events`, `run.py events --stream`, part 2.2's two-accumulator probe and part 2.3's runaway
all build a `ScriptedModel` and hand it to `build_desk`. Nothing in any of them constructs a
provider client, reads a key or opens a socket. The tool that runs during those streams —
`check_service_status` — is this project's own function reading this project's own synthetic notes.
The exception in part 2.3 is raised by ADK's own cost manager inside the process. The count for the
whole day, across the whole cast, is **0**.

Stating the zero is what makes the day's last `TODO(me)` honest. The one question this day cannot
answer — whether a real model's stream also repeats the entire answer in its final event — is the
only thing here that would cost requests, and it is marked unrun rather than guessed at. Everything
this day *does* claim about the stream is a claim about this project's own double, and part 1.1 says
so in the file itself.

For the days that do call out, the ceiling remains unknown and is not invented. Plan §9 and this
project's `PACKAGES.md` both record that the provider's rate-limit page publishes no RPM, TPM or RPD
figure and directs you to Google AI Studio instead. That `TODO(me)` stands: read this project's live
limits there and paste them, with the date. Until then the hubs state the request count, which is a
fact about this project's own code, and no number for the ceiling, which is not.

## §8 Traps

- **One question is not one reply.** `run_async` yields a sequence. Day 6's `agent.ask` kept exactly
  one event and dropped the others, which made the desk look like a thing that returns a string. It
  is a thing that emits a stream, and returning a string is what you do with the stream afterwards.
- **The tool-call and tool-result events carry no text — `''`, not a placeholder.** A client that
  renders `event.content.parts[].text` and nothing else shows a blank screen for the entire working
  period. Two of three events on the simplest possible run.
- **`event.partial` has three states, not two.** It prints as `None` when unset. The documented
  condition is *`partial` is not `True`*, and `if event.partial == False` rejects the final event.
- **`is_final_response()` is a method, not a field.** It computes a rule with clauses for function
  calls, function responses, partial chunks, code-execution results, `skip_summarization` and
  long-running tools. Any hand-written substitute is a subset of it that will be wrong later.
- **`StreamingMode.NONE` has the value `None`, not the string `'none'`.** A comparison against a
  string is false in every case, including the one it was aimed at.
- **Streaming changes the number and shape of events, never the answer.** Three to nineteen for the
  same sentence, with the model-call count unmoved at two. Anything downstream that was sized
  against the event count has just been resized without being told.
- **The final event repeats the whole answer.** It is not the last fragment. Accumulating over every
  event therefore produces exactly double, joined with no separator, and every character of it was
  genuinely sent.
- **The framework's own documented accumulation pattern adds the final event's text to the
  accumulated partials.** That is correct for a stream whose final event carries only the remainder
  and wrong for one that repeats. The documentation cannot decide which you have; running it can.
- **Reset the accumulator after a final response.** Otherwise the second question in a session
  starts with the first question's answer already in the buffer.
- **The bound counts model calls; your logs count events.** Seven events for three calls in part 2.3,
  three events for two calls in part 1.2, nineteen for two in part 2.1. There is no fixed ratio, so
  sizing `max_llm_calls` from an event count is guesswork.
- **`max_llm_calls` is on by default at 500, and `0` disables it rather than forbidding calls.** Day
  07 part 2.2 owns that; part 2.3 is where you watch the enforcement raise.
- **`LlmCallsLimitExceededError` arrives as a raised exception out of `run_async`,** not as an event
  and not as a return value. A consumer that only handles events never sees it.
- **A stand-in model proves things about your code and nothing about a model.** Every green result in
  this day is a statement about the runner, the events and your consumption of them. None of it is
  evidence that the desk answers well.
- **The obvious way to add `events` walks back day 06's boundary.** A `from google.adk.sessions
  import InMemorySessionService` at the top of `run.py` is what an editor's auto-import will write,
  and it makes `run.py check` load the framework before it checks anything — undoing the reason day
  06 part 2.1 put `from ask_desk import agent` *inside* `adk()`. The import goes inside `events()`
  instead. Nothing warns you: the module-scope version works perfectly and only costs you the
  property that `check` runs on a machine where the framework is broken.
- **`build_desk` duplicates the instruction and the tool list** already given to the module-level
  `desk`. Nothing keeps the two in step, and the day they diverge every transcript in this document
  describes a different agent from the one that answers.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| Three events for one question, and which is final | `uv run --frozen python run.py events` | 2026-09-10 | rows 1 and 2 `final=False` with text `''`; row 3 `final=True`; footer `3 events, 2 model call(s)` — part 1.2 |
| The tool-call and tool-result events carry no text | the same run | 2026-09-10 | `''` in both rows, printed with `!r` so an empty string is visible rather than an empty column |
| Streaming changes the event count and not the answer | `uv run --frozen python run.py events --stream` | 2026-09-10 | `19 events, 2 model call(s)` — sixteen `partial=True` rows, one per word, all `final=False`; row 19 `partial=None final=True` — part 2.1 |
| The final event repeats the whole sentence | the same run, rows 18 and 19 | 2026-09-10 | row 18 is `'up.'`; row 19 begins `'The VPN is degraded: there is a known split tunn'` |
| Accumulating over every event doubles the answer | the two-accumulator probe in part 2.2 | 2026-09-10 | `every event : 168 chars`, `partials only: 84 chars`, and the naive text showing the sentence twice joined with no separator |
| The bound fires, and what it counts | part 2.3's probe with `RunConfig(max_llm_calls=3)` against `scripted.NEVER_STOPS` | 2026-09-10 | `raised after 7 events` and `google.adk.agents.invocation_context.LlmCallsLimitExceededError: Max number of llm calls limit of \`3\` exceeded` — seven events for three model calls |
| The three streaming modes | `google.adk.agents.run_config.StreamingMode` under google-adk 2.8.0 | 2026-09-10 | `NONE = None`, `SSE = 'sse'`, `BIDI = 'bidi'` — `NONE`'s value is the Python `None`, not a string |
| The non-streaming contract of a model call | docstring of `BaseLlm.generate_content_async` in `google/adk/models/base_llm.py`, google-adk 2.8.0 | 2026-09-10 | "**Non-streaming mode (stream=False):** Yields exactly one LlmResponse containing the complete model output (text, function calls, bytes, etc.). This response has `partial=False`." |
| What `is_final_response()` means | `https://adk.dev/tutorials/agent-team/` | 2026-09-09 | "Key Concept: `is_final_response()` marks the concluding message for the turn." |
| The rule `is_final_response()` computes | `https://adk.dev/events/` | 2026-09-09 | true when `get_function_calls()` is empty, `get_function_responses()` is empty, `partial` is not `True`, and the event does not end with a code execution result — plus the `skip_summarization` and long-running-tool cases |
| The fields an event carries | `https://adk.dev/events/`, conceptual structure | 2026-09-09 | `author: str  # 'user' or agent name`, `invocation_id`, `id`, `partial: Optional[bool]`, `actions`, `branch` — `Event` shown as extending `LlmResponse` |
| The documented way to accumulate a stream | `https://adk.dev/events/` | 2026-09-09 | accumulation guarded by `if event.partial`, then `final_text = full_response_text + (event.content.parts[0].text if not event.partial else "")`, then the accumulator reset — quoted in part 2.2 |
| Rate limits are still unpublished | `https://ai.google.dev/gemini-api/docs/rate-limits` | 2026-09-10 | "Rate limits depend on a variety of factors (such as your usage tier) and can be viewed in Google AI Studio" — no RPM, TPM or RPD figure; §7's `TODO(me)` stands |
| Toolchain versions | `uv --version`, `python --version`, `import google.adk` inside the project | 2026-09-10 | uv 0.12.3, CPython 3.12.12, google-adk 2.8.0 — re-observed, not assumed |

## §10 Ledger & commit

**`docs/PROGRESS.md`:**

```text
| 8 | 2026-09-10 | AG-03 | 5 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the terms this day defined for the first time. Check the file before
appending. **Turn** (day 4 part 1.3), **Session** and **Runner** (day 6 part 2.1), **Tool call** and
**Tool-result turn** (day 5 part 2.1) are already there and are linked by this day's parts rather
than restated.

```text
| Event | One thing a runner emits while it works a question through an agent — a tool being asked for, a tool answering, a fragment of text, the finished text. Smaller than a turn: several events make one. Each says who produced it and whether it concludes the turn. | day 8 part 1.2 | a run event |
| Partial event | An event marked as a fragment of something still arriving rather than as a thing you may act on, flagged by `partial`. The field has three states, because unset reads as `None` — which is why the condition is written "not `True`" rather than "`False`". | day 8 part 2.1 | a streaming chunk, a partial |
| Streaming mode | The field on `RunConfig` that decides whether a run emits one complete text event or a fragment per word. Its enum has three values and the off position is `None` itself, not a string. It changes the number and shape of the events and never the answer. | day 8 part 2.1 | `StreamingMode`, SSE |
| Test double | An object that stands in for a real dependency so a run can be reproduced exactly — same shape, none of the work. It proves things about your own code and nothing whatever about the thing it replaces, which is why the one here names itself in every transcript it produces. | day 8 part 1.1 | a stand-in, a fake |
```

**`projects/01-ask-desk/CODEMAP.md`** — one new row and two amendments, so that every line this
project contains still traces to the day that printed it:

```text
| `ask_desk/scripted.py` | day 08 part 1.1, whole, full depth — synthetic scripts |
```

```text
| `run.py` | day 04 part 2.1, whole · the `adk` subcommand added as a marked diff on day 06 part 2.1 · the `events` subcommand added as a marked diff on day 08 part 1.2 |
| `ask_desk/agent.py` | day 06 part 1.1, whole · `build_desk` and `build_runner`'s agent seam added as a marked diff on day 08 part 1.1 · `run_config()` added as a marked diff on day 08 part 2.1 |
```

**`docs/PINS.md`** — nothing to add. Today observed no version this repository does not already
record: `projects/01-ask-desk/PACKAGES.md` carries google-adk 2.8.0 from day 4, and uv 0.12.3 and
CPython 3.12.12 are already in `docs/PINS.md` from days 1 and 3. The re-observations are dated in
§9, which is what that table is for.

**`docs/SOURCES.md`** — nothing to add. This day cites two framework documentation pages and one
provider rate-limit page, none of which is a record with a resolvable identifier. All three are
dated in §9. Same call days 1 to 7 made.

**Commit:**

```text
day 08: P01 Ask Desk · 5 — Events and streaming: the 2.x event model — closes AG-03
```
