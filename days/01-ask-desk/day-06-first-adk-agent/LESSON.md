---
project: "P01 Ask Desk"
day: 6
phase: P01
title: "P01 Ask Desk · 3 — The first ADK agent: `Agent` plus runner, model pinned explicitly"
ids: [AG-02]
kind: mechanism
deploy_tier: D1
plan_version: "v3.1.0"
parts: 4
files_printed:
  - "projects/01-ask-desk/pyproject.toml"
  - "projects/01-ask-desk/ask_desk/agent.py"
  - "projects/01-ask-desk/run.py"
generated: "2026-09-09"
status: written
commit: ""
---

> **Yesterday:** three tools, their hand-written declarations, and a desk that can run one of them
> and hand the result back — every line of it yours.
> **Today:** the same desk as a framework agent — a configuration object, a runner, a session
> service — and a careful account of which of your pieces went where, including the one that did not.
> **Tomorrow:** `FunctionTool` — what the framework derived from your three plain functions, set
> beside the declarations you wrote yesterday.

## §1 The scene

You have been answering the desk phone yourself, and today you hire an agency. You do not teach
anybody the job. You write a **brief**: who they are, in one word, so anything they file can be found
under it; what they answer, and from what; which three drawers they are allowed to open. That is the
whole of it — a page, not a manual, and nothing on it is a procedure.

What comes back is a person and a way of working. They keep the file, so the second call about the
same thing does not start from nothing. They chase the callbacks while you get on with something
else. Those are real jobs you have stopped doing, and stopping is the point of hiring anyone. Today's
work is mostly a careful inventory of exactly that: five things you built by hand over the last two
days, four of which the agency has taken over, and one of which it has not.

The one it has not is the money. Nobody at the agency is watching your budget — they will make as
many calls as the job seems to need. Your hand-rolled desk had a hard stop in it for precisely this,
a count of provider calls past which one question is refused rather than continued. That number is
still in the repository, still correct, and no longer on the path that runs. Nothing tells you so,
and by the end of today you will be able to say exactly why.

And there is the line on the brief you might leave blank without thinking about it — the one naming
who the work goes to. Leave it out and nothing refuses, nothing warns, and the desk answers. It is
answered by whoever has been on the agency's books longest, which is neither a trainee nor a
mistake, and is four generations behind the one you would have chosen.

## §2 The map

Two sections. The first is the brief itself: what an agent *is* as an object, what each field on it
prevents, and what the one field nobody fills in quietly does. The second is the half of the
framework that actually does work — the runner, the store it will not run without, and what happens
when a request that cannot succeed is sent anyway.

### 1 · The brief

*The mental model: an agent is configuration, not code. You are filling in a form, and every blank
you leave is a decision somebody else makes for you.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-brief/1.1-the-agent-is-a-configuration.md) | The agent is a configuration | What is an `Agent` actually made of, and which of my hand-rolled pieces did it replace? | foundation |
| [1.2](parts/01-the-brief/1.2-the-model-nobody-chose.md) | The model nobody chose | What does an agent call when I never say which model, and why does nothing complain? | working |

### 2 · The one who runs it

*The mental model: the brief does nothing on its own. Somebody has to take the question in, open a
file for it, and stay with the job — and everything they do is waiting on something.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-one-who-runs-it/2.1-the-runner-the-session-and-the-await.md) | The runner, the session and the await | Who carries the conversation now, and why is all of this `async`? | working |
| [2.2](parts/02-the-one-who-runs-it/2.2-the-runner-with-nowhere-to-put-it.md) | The runner with nowhere to put it | Why is `session_service` the only argument with no default — and what is `tenacity` doing in a 400? | production |

## §3 Setup — run this

One dependency, added with the pin, and then four commands that need no key. Run them from the
project folder. Everything here was run on this machine today; what it reported is in §9.

```bash
cd projects/01-ask-desk

# part 1.1 — the framework, pinned. Writes pyproject.toml and uv.lock.
uv add "google-adk==2.8.0"

# part 1.1 — the agent, and the tools it derived. No key, no network.
uv run --frozen python -c "
import asyncio, warnings
warnings.filterwarnings('ignore')
from ask_desk.agent import desk, build_runner

async def main():
    print('name       ', desk.name)
    print('model (set)', repr(desk.model))
    print('canonical  ', desk.canonical_model.model)
    for tool in await desk.canonical_tools():
        print(f'{type(tool).__name__:14} {tool.name}')
    print('runner agent  ', build_runner().agent.name)

asyncio.run(main())
"

# parts 1.2 and 2.2 — the three refusals, in one run
uv run --frozen python -c "
import warnings
warnings.filterwarnings('ignore')
from google.adk.agents import Agent
from google.adk.runners import Runner
from ask_desk.agent import desk

a = Agent(name='unpinned')
print('model field      :', repr(a.model))
print('what it will call:', a.canonical_model.model)

try:
    Agent(name='ask desk', model='gemini-3.8-flash')
except Exception as e:
    print(type(e).__name__, '->', str(e).strip().splitlines()[2].strip())

try:
    Runner(app_name='ask_desk', agent=desk)
except TypeError as e:
    print('TypeError ->', e)
"

# the gate, unchanged since day 4 and still green
uv run --frozen python run.py check
echo $?

# part 2.2 — the real provider refusal. Needs no working key; that is the point.
uv run --frozen python run.py adk "Is the VPN down?"
```

`--frozen` is on every `uv run` for the reason day 3 gave: plain `uv run` brings the lockfile up to
date before your command starts, so a check invoked that way reports on a repository its own
invocation just repaired. `PRIMER.md` §3 has the self-contained version.

## §4 Files this day prints

Three files, one of them new. Nothing from days 4 and 5 is reprinted: `loop.py`, `tools.py`,
`provider.py`, `util/keys.py`, `util/models.py` and `data/notes.json` are untouched today, and the two
files that do change appear only as marked diffs against the versions those days printed whole.

| File | Printed by |
| --- | --- |
| `projects/01-ask-desk/pyproject.toml` | part 1.1, as a marked diff against the version day 4 printed |
| `projects/01-ask-desk/ask_desk/agent.py` | part 1.1, whole — new today |
| `projects/01-ask-desk/run.py` | part 2.1, as a marked diff against the version day 4 printed |

## §5 Build brief

| File | What it must do |
| --- | --- |
| `projects/01-ask-desk/pyproject.toml` | `TODO(me)`: add the framework with `uv add "google-adk==2.8.0"`. Then say which two files changed, and why `run.py check`'s `pins` check stays green when it would have gone red for `>=2.8.0`. |
| `projects/01-ask-desk/ask_desk/agent.py` | `TODO(me)`: type it. Before running the probe, predict what `desk.model` and `desk.canonical_model.model` will print, and then predict both again for an agent with the `model=` line deleted. |
| `agent.py` (the name field) | `TODO(me)`: change `name="ask_desk"` to `"ask desk"` and say, *before* running anything, whether the failure arrives at import or at the first question. Then run it and see. Put it back. |
| `agent.py` (the five-row table) | `TODO(me)`: find, in `loop.py` and `tools.py`, the code each row of the docstring's table names. Say out loud, for each, what would go wrong if nothing had replaced it. |
| `projects/01-ask-desk/run.py` | `TODO(me)`: add the `adk` subcommand. Say why `from ask_desk import agent` is inside the function rather than at the top of the file, and what `run.py check` would start depending on if you moved it. |
| the bound | `TODO(me)`: find where `MAX_CALLS_PER_QUESTION` is enforced, and say what enforces it on the `adk` path. Write down — in `lab/`, not in `agent.py` — what you would add to get a ceiling back. |
| the check that would catch a default | `TODO(me)`: sketch a sixth check for `run.py` that would catch an unpinned agent. Say why it has to read `desk.canonical_model.model` rather than `desk.model`, and why reading the source text instead would not work. |
| the failure rep | `TODO(me)`: delete `session_service=` from `build_runner`, run the probe, and read the `TypeError`. Restore it, then delete the `await` before `create_session`, run `run.py adk "..."`, and paste the real output into part 2.1's `TODO` block. |

## §6 The check that must be able to fail

```text
cd projects/01-ask-desk
uv run --frozen python run.py check    # five checks: keys, interpreter, pins, lock, model
echo $?                                # 0 green, 1 red, 2 you typed it wrong
cd ../.. && python p.py depth 6        # this day against the plan §5 contract
```

**How to make it go red on purpose — and the one that will not.**

The first is the pin. Change `google-adk==2.8.0` to `>=2.8.0` in `pyproject.toml` and the `pins` check
goes red, naming the dependency and saying that one machine gets a version another never saw. Restore
it with `uv add`.

The second is the model registry, which is now guarding a framework call as well as a hand-rolled one.
Point `models.ANSWERING` at an ID that is not in `PINNED` and the `model` check goes red with the
registry's own sentence — and so does the construction of `desk` itself, at import, because part 1.1's
`model=` argument goes through `require_pinned` rather than taking the string.

The third is the framework refusing at construction, and it is red without any check being involved:
`Runner(app_name=..., agent=...)` with no `session_service` is a `TypeError` from the interpreter, and
`Agent(name="ask desk")` is a `ValidationError` from pydantic. Both are part 2.2.

**And the one that will not go red, which is the day's real lesson.** Delete the `model=` line from
`agent.py` entirely and run the check again. All five rows stay green, because `check_model_is_registered`
asks the registry about `models.ANSWERING` — a constant — and an unpinned agent never asks the registry
anything. The desk still answers; it just answers on a model nobody in this project chose. Writing the
check that *would* catch it is the rep in §5, and it is deliberately not written for you.

For the document itself: delete an `## In production` heading from any part and run
`python p.py depth 6`; it names the file and the missing section.

## §7 Request budget

**One agent, so the cast is one — and the count per question is at least one and not bounded by
anything you wrote.**

The plan §9 counts requests across the whole cast. This project's cast is a single agent, so a
question that needs no tool is **one** provider call: the question goes out, the answer comes back.
A question that uses a tool is **at least two** — one call in which the model asks for the tool, and
one after the result is handed back — and a question that needs two lookups before it can answer is
three, and so on.

Day 4 put a ceiling on that: `MAX_CALLS_PER_QUESTION = 6`, enforced inside `loop.Conversation.ask`,
which raises rather than returning a partial answer. **The ADK path does not go through that code and
therefore has no ceiling**, which is the last row of part 1.1's table and the reason it is worth
reading twice. Today's runs cannot spend anything — there is no working key on this machine, so every
call is refused before a model is reached — and that is exactly the state in which to notice a missing
bound, rather than the state in which to discover it.

Two things were still sent today, and both were rejected: the hand-rolled `run.py ask` and the
`run.py adk` run in part 2.2. The second one was sent more than once, because `tenacity` is in its
traceback and a 400 was retried; how many times is not visible in the captured tail and no number is
invented for it here.

The provider's ceiling is **not printed in this repository**, because it is no longer published. The
rate-limit page, checked 2026-09-09, says only that limits "can be viewed in Google AI Studio" and
that "Specified rate limits are not guaranteed and actual capacity may vary" — no RPM, TPM or RPD
figure appears for any model.

`TODO(me): read this project's live limits in Google AI Studio and paste them into PACKAGES.md with
the date.`

See `docs/adr/ADR-0004-generatecontent-by-hand-and-unpublished-limits.md` for why a number that cannot
be verified is not written down here at all.

## §8 Traps

- **`Agent` and `LlmAgent` are the same class object.** Not a subclass, not a wrapper — `Agent is
  LlmAgent` is `True`. Two names in the documentation, one thing; do not go looking for the
  difference.
- **An agent with no `model` does not raise.** It gets ADK's `DEFAULT_MODEL`, `gemini-3.5-flash`,
  which the provider ships as Stable and calls its legacy Flash model. Not experimental — old, which
  is quieter.
- **`agent.model` is not what the agent will call.** It is what you typed. `agent.canonical_model.model`
  is the resolved value, and on an unpinned agent the two disagree.
- **`run.py check` cannot see an unpinned agent.** Its `model` check asks the registry about a
  constant. Nothing that never calls the registry can be caught by it.
- **An agent's name must be a valid Python identifier.** A space raises `ValidationError`, and the
  message calls it a *node* name, which is the framework telling you how it addresses agents.
- **`desk` is built at module scope**, so every validation error in it arrives on *import*. That is
  why `run.py` imports `ask_desk.agent` inside the `adk` function and not at the top: otherwise
  `run.py check` would need the framework installed and the agent valid before it could report that
  they were not.
- **`session_service` is the only required argument on `Runner`.** Everything else — `agent`
  included — defaults to `None`, so a misspelt keyword is a missing argument and not a `TypeError`.
- **`create_session` is a coroutine.** No `await`, no session; the statement completes, the store
  stays empty, and the failure arrives later from `run_async`, about a session id, nowhere near the
  line that caused it.
- **`app_name` must match between the runner and the session.** `run_async` takes `user_id` and
  `session_id` and no app name, so nothing reconciles them for you — which is why `APP_NAME` is a
  module constant.
- **`asyncio.run` belongs at the edge and nowhere else.** One per process, in the synchronous
  function the CLI calls. Async is contagious upwards, and the fix for that is one entry point, not
  many.
- **`is_final_response()` is a filter, not a summary.** Everything else in the stream is the middle of
  the work — a tool being asked for, a tool answering — and today it is thrown away on purpose.
- **The bound did not come across.** `MAX_CALLS_PER_QUESTION` guards `loop.Conversation.ask` and
  nothing else. Reading the constant and assuming it applies to the ADK path is the mistake this day
  exists to prevent.
- **ADK retries a 400.** `tenacity` is in the traceback of an invalid-key error, and the provider's
  own guidance says not to retry client errors. Honest backoff is P05's subject; knowing it happens
  is today's.
- **A rejected key is `400 INVALID_ARGUMENT` here, not `401`** — the documented table and the observed
  status disagree, and the observed one is what your code has to handle.
- **Do not add `google-genai` to `pyproject.toml`.** It arrives with `google-adk`. A second pin on the
  same package is a second thing to keep in step, and nothing will.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| `Agent` is `LlmAgent` | `uv run --frozen python -c "from google.adk.agents import Agent, LlmAgent; print(Agent is LlmAgent)"` | 2026-09-09 | `True`, and `Agent.__qualname__` is `LlmAgent` in `google.adk.agents.llm_agent`, under google-adk 2.8.0 |
| The agent resolves to the pinned model | the `desk` probe in §3 | 2026-09-09 | `model (set) 'gemini-3.8-flash'` and `canonical gemini-3.8-flash` — the two agree only because the field is filled |
| Plain functions become `FunctionTool`s | the same probe, `await desk.canonical_tools()` | 2026-09-09 | three `FunctionTool` rows — `search_notes`, `fetch_note`, `check_service_status` — from three plain functions in `tools=[...]` |
| The runner holds this agent | the same probe, `build_runner().agent.name` | 2026-09-09 | `ask_desk` |
| An unpinned agent calls the legacy model | the three-refusal probe in §3 | 2026-09-09 | `model field : ''` and `what it will call: gemini-3.5-flash` — nothing raised, nothing warned |
| An agent name must be an identifier | the same probe | 2026-09-09 | `ValidationError -> Value error, Node name 'ask desk' must be a valid Python identifier.` |
| `session_service` has no default | the same probe | 2026-09-09 | `TypeError -> Runner.__init__() missing 1 required keyword-only argument: 'session_service'` |
| ADK's default model | `https://adk.dev/api-reference/python/google-adk.html` | 2026-09-09 | "`DEFAULT_MODEL : ClassVar[str] = 'gemini-3.5-flash'`" and "The built-in default is `gemini-3.5-flash`." |
| `Runner`, `run_async`, `create_session` signatures | the same page | 2026-09-09 | every argument keyword-only; `session_service` alone has no default; `create_session` is `abstractmethod async` |
| ADK wraps plain functions | `https://adk.dev/tools-custom/function-tools/` | 2026-09-09 | "When you assign a function to an agent's `tools` list, the framework automatically wraps it as a `FunctionTool`." |
| `is_final_response`, and why async | `https://adk.dev/tutorials/agent-team/` | 2026-09-09 | "Key Concept: `is_final_response()` marks the concluding message for the turn." and the I/O-bound justification for asyncio |
| The two models' status and wording | `https://ai.google.dev/gemini-api/docs/models`, last updated 2026-09-04 | 2026-09-09 | both **Stable**; 3.5-flash is "Our legacy Flash model…", 3.8-flash is "Our most intelligent Flash model, engineered for … autonomous agents…" |
| An invalid key through ADK | `uv run --frozen python run.py adk "Is the VPN down?"` with the synthetic key | 2026-09-09 | `google.genai.errors.ClientError: 400 INVALID_ARGUMENT`, `'API key not valid. Please pass a valid API key.'`, with `tenacity` in the stack |
| The documented status for a bad key | `https://ai.google.dev/gemini-api/docs/api-errors` | 2026-09-09 | tabulated as `authentication` / 401 Unauthorized — which disagrees with the 400 observed twice on this machine |
| Retry guidance | `https://ai.google.dev/gemini-api/docs/troubleshooting` | 2026-09-09 | "Only retry on transient errors (like 429, 408, or 5xx). Do not retry on client errors (like 400 or 403)" |
| Rate limits are unpublished | `https://ai.google.dev/gemini-api/docs/rate-limits` | 2026-09-09 | limits "can be viewed in Google AI Studio"; "Specified rate limits are not guaranteed and actual capacity may vary"; no RPM/TPM/RPD figure for any model |
| google-adk 2.8.0 | `https://pypi.org/pypi/google-adk/json` | 2026-09-09 | 2.8.0, uploaded 2026-08-26T23:26:17Z, `requires_python >=3.10` — already the row `PACKAGES.md` carries |

## §10 Ledger & commit

**`docs/PROGRESS.md`:**

```text
| 6 | 2026-09-09 | AG-02 | 4 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the terms this day defined for the first time. **Event** is deliberately not
here: today's code filters events and does not read them, and day 8 is where the term is earned.

```text
| Agent (ADK) | A configuration object describing one agent — its name, its model, its description, its instruction and its tools. It is filled in, never subclassed, and it does no work on its own. `Agent` and `LlmAgent` are the same class. | day 6 part 1.1 | LlmAgent, the brief |
| Runner | The object that executes one turn for an agent: it holds the agent and the session service, and it produces the turn's events as they happen. The agent is the configuration; the runner is what runs it. | day 6 part 2.1 | the runner |
| Session | One stored conversation, identified by an app name, a user and a session id, held by a session service rather than by your code. It is where the list you resent by hand on day 4 now lives. | day 6 part 2.1 | the stored conversation, an ADK session |
```

**`projects/01-ask-desk/PACKAGES.md`** — nothing new to append. The `google-adk` 2.8.0 row and the
`gemini-3.8-flash` model row were both written when the project's freshness check was run, and both
name day 3 of this project — today — as the day that adopts them. Today's job was to make the rows
true, not to add more.

**`docs/PINS.md`** — nothing to add. That ledger holds what the *authoring* repository depends on;
`google-adk` is a project dependency and its pin lives in the project's own `PACKAGES.md`, which is
what the plan §9 means by every project pinning independently.

**`docs/SOURCES.md`** — nothing to add. Everything cited today is a documentation page or a package
index, dated in §9; neither is a record with a resolvable identifier, which is what that ledger is
for. This is the same call days 1 to 3 made.

**Commit:**

```text
day 06: P01 Ask Desk · 3 — The first ADK agent: Agent plus runner, model pinned explicitly — closes AG-02
```
