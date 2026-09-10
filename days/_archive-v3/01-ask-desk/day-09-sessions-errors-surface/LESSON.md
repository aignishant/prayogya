---
project: "P01 Ask Desk"
day: 9
phase: P01
title: "P01 Ask Desk · 6 — Sessions, runs, and errors that surface instead of hiding"
ids: [AG-04, RS-01]
kind: mechanism
deploy_tier: D1
plan_version: "v3.1.0"
parts: 4
files_printed:
  - "projects/01-ask-desk/run.py"
  - "projects/01-ask-desk/ask_desk/agent.py"
  - "projects/01-ask-desk/ask_desk/scripted.py"
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** every event one question produces, read in order, with the difference between a
> partial chunk and the final response settled and the bound watched firing.
> **Today:** where those events go afterwards — the session that holds them, the address that
> decides which session you get — and what the same machinery does when a run fails instead of
> finishing.
> **Tomorrow:** Ship D1. The desk behind HTTP, a health endpoint that means something, and the first
> eval that can go red on purpose.

## §1 The scene

Walk onto a hospital ward at handover. Nobody tells the incoming nurse what happened; everything is
already written, and it is in a numbered slot on the trolley at the foot of each bed. The number is
the whole of the addressing system. Anyone on any shift who can read the number can pick up exactly
what was written, in order, and add the next line to it — and that is the entire reason the ward
works with people coming and going every shift.

It is also the entire reason it can go wrong in a way that produces no alarm. Quote the wrong bed
number and you get notes that are complete, careful, legible and about somebody else. Nothing failed.
The slot held notes, the notes were handed over, every part did its job. What is broken is the join
between a number and a person, and no one on the ward can see a join — they see a clinician being
confidently wrong about a patient.

Today the conversation you carried by hand on day 4 finishes moving into that trolley. You stop
holding the thread and start holding its address, and the second half of the day is about what
happens on that ward when something actually goes wrong. An incident gets recorded twice on purpose —
written in the notes for whoever reads them next week, and said out loud to whoever is standing there
now — and the trouble people have with this framework is that they expect it to have chosen one. It
has not. It does both, and reading only one of them is how a failed run gets filed as a successful
empty one. Because an incident that is not written up did not stop happening. It stopped being
findable.

## §2 The map

Two sections, and they close one curriculum ID each. The first is the place: what a session is, how
it is addressed, and what the second question down the same address can see. The second is what the
same run does when the model call raises instead of answering — where the failure surfaces, and the
two lines of code that make it disappear.

### 1 · The place the thread lives — closes `AG-04`

*The mental model: notes live in a numbered slot at the foot of a bed, not in the head of whoever is
on shift. The number is the whole of your control over which notes you get.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-place-the-thread-lives/1.1-a-session-is-a-place-not-a-variable.md) | A session is a place, not a variable | Where did day 4's `Conversation.contents` go, what names it, and why does one question leave four events behind? | foundation |
| [1.2](parts/01-the-place-the-thread-lives/1.2-what-the-second-question-sees.md) | What the second question sees | One session against two: what does a wrong `session_id` do, and how do you tell that apart from day 4's amnesia? | working |

### 2 · When it goes wrong — closes `RS-01`

*The mental model: an incident is written in the notes **and** said out loud, and the one that is
neither did not stop happening — it stopped being findable.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-when-it-goes-wrong/2.1-the-error-that-reached-the-caller.md) | The error that reached the caller | A model call raises mid-run: what does the event stream carry, what escapes the loop, and why is the answer both? | working |
| [2.2](parts/02-when-it-goes-wrong/2.2-the-except-that-ate-the-incident.md) | The except that ate the incident | What exactly does `except Exception: return answer` return for a failed run, and why is the friendlier version worse? | production |

## §3 Setup — run this

Nothing new to install. `google-adk==2.8.0` has been pinned since day 06 and the scripted stand-in
model has existed since day 08; today adds one subcommand to the driver and one function to
`agent.py`. Every command below was run on this machine today and what it reported is in §9.

```bash
cd projects/01-ask-desk

# part 1.1 and 1.2 — the session subcommand this day adds to run.py
uv run --frozen python run.py session

# part 1.1 — the stored events, their authors and their invocation ids
# part 1.2 — the three outcomes of a session id
# part 2.1 — the failing run, its error event and the exception that escapes it
# part 2.2 — the same run with the loop wrapped in try/except
# each of these is a `uv run --frozen python -c "..."` probe printed in full in its own part

# the gate, unchanged and still green
uv run --frozen python run.py check
echo $?
```

Every one of those contacts nothing and needs no key: `run.py session` and all four probes drive the
scripted stand-in from `ask_desk/scripted.py`, which day 08 printed whole. The `.env` on this machine
still holds the synthetic value P00 day 02 wrote, and §7 says what that means for today.

## §4 Files this day prints

Three files, none of them new, and none of them printed whole today — each appears as a marked
region or diff against the day in this project that printed it whole. Nothing day 08 printed is
reprinted here.

| File | Printed by |
| --- | --- |
| `projects/01-ask-desk/run.py` | part 1.1, as a marked diff against the whole file day 04 part 2.1 printed — the `session` subcommand only |
| `projects/01-ask-desk/ask_desk/scripted.py` | part 2.1, as three marked regions of the whole file day 08 printed — `Fail`, its branch, and `FAILS_AFTER_A_TOOL` |
| `projects/01-ask-desk/ask_desk/agent.py` | part 2.1, as a marked diff against the whole file day 06 part 1.1 printed — `export_key()` and the two lines in `ask` that call it |

`ask_desk/agent.py`'s `build_desk`, `run_config` and `build_runner` are used throughout today and are
printed with the event walkthrough in `days/01-ask-desk/day-08-events-streaming/`; they are not
reprinted here.

## §5 Build brief

| File | What it must do |
| --- | --- |
| `run.py` — the `session` subcommand | `TODO(me)`: type it. Before running it, predict all four numbers it prints, and write your predictions down where you cannot quietly revise them. |
| `run.py` — the same subcommand, altered | `TODO(me)`: change the first experiment's ids from `["s-1", "s-1"]` to `["s-1", "s-3"]`, predict both numbers, run it, and put the line back. |
| the stored-events probe | `TODO(me)`: run part 1.1's probe and say which of the four events per question is the one `run_async` never yielded, and why the runner stored it before doing any work. |
| the three-outcomes probe | `TODO(me)`: run part 1.2's probe. Then extend it so that `s-2` **is** created before the run, predict what changes, and say what an operator would see in their logs in that third case. |
| `ask_desk/agent.py` — `export_key()` | `TODO(me)`: type it. Before running anything, say which of `os.environ` and `.env` the guard lets win, and what would break in a container if you reversed the test. |
| the failing-run probe | `TODO(me)`: run part 2.1's probe, then delete its `try`/`except` and predict the last two lines of output before running it again. |
| the swallowing probe | `TODO(me)`: run part 2.2's probe and read the two output lines together. Say what the run knew, and name the single line that threw it away. |
| a check of your own | `TODO(me)`: write a one-case check that drives `scripted.FAILS_AFTER_A_TOOL` and exits **non-zero** unless the run raises. Run it against both versions and `echo $?` after each. |

## §6 The check that must be able to fail

```text
cd projects/01-ask-desk
uv run --frozen python run.py check      # the project gate: six checks
echo $?                                  # 0 green, 1 red, 2 you typed it wrong
uv run --frozen python run.py session    # 4, 8 — then 4, 4
cd ../.. && python p.py depth 9          # this day against the plan §5 contract
```

**How to make it go red on purpose — three ways, and the third is the day's real one.**

The first is the address. In `run.py session`, change the first experiment's ids from
`["s-1", "s-1"]` to `["s-1", "s-3"]`. The second line stops saying `8 event(s)` and starts saying
`4 event(s)`, and nothing errors — which is the point of part 1.2, seen as a number rather than as
an argument.

The second is the refusal. Delete the `if await sessions.get_session(...) is None:` guard so
`create_session` is called before every question. The first question passes and the second raises
`AlreadyExistsError: Session with id s-1 already exists.` — a loud failure, on the second turn, which
is the good kind.

The third is the day's deliberate failure and it is part 2.2. Wrap the event loop in
`try/except Exception: return answer` and drive `scripted.FAILS_AFTER_A_TOOL` through it. The run
fails, the tool has already run and cost something, the error event carries
`error_code='RuntimeError'` — and the function returns `''`, normally, with nothing raised and
nothing logged. Then write the check that catches it: one case that asserts the run **raises**, red
against the swallowing version and green against the honest one. A failure mode that no check can see
is a failure mode you will meet again.

For the documents themselves: delete a `## In production` heading from any part and run
`python p.py depth 9`; it names the file and the missing section.

## §7 Request budget

**Zero provider calls. Not "few" — zero.**

Everything today runs against `ask_desk/scripted.py`, the local stand-in day 08 printed whole. It
holds no network client, consumes no quota and needs no key: `run.py session` and all four probes
drive it, and the two model calls each question costs are two calls into a Python object in your own
process.

That is not the same as saying this day is free of the provider. Part 2.1 quotes two real refusals
observed on this machine — `ValueError: No API key was provided.` before `export_key()` existed, and
`400 INVALID_ARGUMENT` after it — and both were produced with the synthetic key P00 day 02 wrote.
Neither reached a model, and no answer from a real model appears anywhere in this day.

The ceiling those calls would count against is still `TODO(me)`: the provider's rate-limit page states
only that *"Rate limits depend on a variety of factors (such as your usage tier) and can be viewed in
Google AI Studio."* No RPM, TPM or RPD number is published, so none is printed here — read yours in
Google AI Studio when a real key arrives. Plan §9 counts requests across the whole cast; this project
has one agent, so one question is at most `MAX_CALLS_PER_QUESTION` calls, and from P03 that
multiplication starts to matter.

## §8 Traps

- **A session is addressed by three strings, not one.** `session_id` alone collides the moment two
  applications or two people pick the same one. `app_name` and `user_id` are part of the address, and
  a session hands all three back so a fetched session can always say what it is.
- **One question stores four events, not three.** Your own message is stored before any work is done.
  A count taken from `len(session.events)` and a count taken from what `run_async` yielded differ by
  exactly one per question, and neither is wrong.
- **`create_session` raises on a repeat id.** `AlreadyExistsError: Session with id s-1 already
  exists.` Do not wrap it in `try`/`except`; ask `get_session` first and create only on `None`, so
  that "start fresh" stays a decision your code makes rather than one it stumbles into.
- **An unknown `session_id` raises; a wrong one does not.** `SessionNotFoundError` is the loud, cheap
  case. An id that names a *different existing* session runs perfectly and answers from somebody
  else's thread, and it is indistinguishable from inside the process.
- **The `session_id` is the whole of your control over what the model remembers.** Same code, same
  model, same question, one character different: one conversation or two strangers.
- **`is_final_response()` is `True` on the error event.** It is final in the sense of "no more events
  are coming", not in the sense of "here is the answer". Anything branching on it takes the success
  branch on a failed run.
- **The error event has no `content` at all** — `content is None`, not an empty `parts` list. So the
  usual guard `if event.content and event.content.parts:` steps straight over it and leaves the
  accumulator holding whatever it was initialised to.
- **ADK emits the error event *and* re-raises.** Not one or the other. Read only the events and your
  process still dies; catch only the exception and you never see `error_code`, `error_message` or the
  invocation id that would let you find the session.
- **`error_code` is a Python class name, not a status.** `'RuntimeError'` here. Anything that wants
  to decide whether a failure is retryable cannot decide it from that string.
- **`export_key()` is not optional and its direction is a decision.** `google-genai` builds its
  client from `os.environ` and has never heard of this project's `.env`. The guard lets the
  environment win, so an injected production key is never overwritten by a stale file.
- **`ValueError: No API key was provided.` is true about `os.environ` while the key is on disk.** The
  hour people lose here is spent re-checking the file, which is the one place that was never wrong.
- **`except Exception: return answer` returns `''`, normally.** No exception, no non-zero exit, no log
  line, no metric. Behind a rotated key that is a hundred per cent failure rate reported as a hundred
  per cent availability.
- **A friendly sentence in place of the empty string is worse, not better.** `"I couldn't find
  anything"` asserts that a search happened and returned nothing. It did not. Plan §0 and §9 forbid
  fabricating a result to cover an error, by name.
- **Retrying is not today's fix.** The provider's guidance is to retry only transient errors — 429,
  408, 5xx — and never client errors like 400 or 403, and `error_code='RuntimeError'` does not tell
  you which you have. Honest backoff is P05 Bench Runner's subject.
- **`InMemorySessionService` is a dictionary in your process.** Nothing expires, nothing is evicted,
  nothing survives a restart. Sessions in a database are P16 Recall Desk.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| Sessions accumulate down one address | `uv run --frozen python run.py session` | 2026-09-10 | `s-1` holds `4 event(s)` after one question and `8 event(s)` after two, with nothing in the code appending anything |
| Two sessions do not see each other | the second block of the same command | 2026-09-10 | `s-1` and `s-2` each hold `4 event(s)` — two complete conversations, no error, no crossing |
| One question stores four events, not three | the stored-events probe, part 1.1 | 2026-09-10 | `author=user` first, then three from `ask_desk`; day 08's walkthrough of the same script yields three |
| Events group by invocation | the same probe, printing `invocation_id` | 2026-09-10 | two ids across eight events, four apiece — one per call to `run_async` |
| A session carries its own address | the same probe, printing `s.id`, `s.app_name`, `s.user_id` | 2026-09-10 | `s-1`, `ask_desk`, `u` — the triple is stored on the session, not only at the call site |
| `create_session` refuses a repeat id | two `create_session` calls with `session_id='s-1'` | 2026-09-10 | `google.adk.errors.already_exists_error.AlreadyExistsError: Session with id s-1 already exists.` |
| An unknown session id raises | `run_async` with `session_id='s-2'`, never created | 2026-09-10 | `google.adk.errors.session_not_found_error.SessionNotFoundError: Session not found: s-2`, before any model call |
| `get_session` answers rather than raising | the same probe | 2026-09-10 | returns `None` for the same id that made `run_async` raise |
| An error event is emitted **and** the exception escapes | the failing-run probe against `scripted.FAILS_AFTER_A_TOOL` | 2026-09-10 | three events, the third `error_code='RuntimeError'`, `error_message='the provider closed the connection'`, `final=True` — then `escaped after 3 events` |
| The error event carries no content | the swallowing probe, part 2.2 | 2026-09-10 | `final event: content is None \| error_code = RuntimeError` |
| The swallow returns an empty success | the same probe | 2026-09-10 | `the caller received: '' - length 0`, returned normally, nothing raised |
| `Event.error_code` and `error_message` are optional strings | `Event.model_fields` introspection, google-adk 2.8.0 | 2026-09-10 | both `typing.Optional[str]`, both defaulting to `None`; no error object and no traceback survives onto the event |
| `create_session`'s signature | `https://adk.dev/api-reference/python/google-adk.html` | 2026-09-09 | `abstractmethod async create_session(*, app_name, user_id, state=None, session_id=...)` — keyword-only, `session_id` defaulted |
| The key bridge, both messages | `agent.ask` with and without `export_key()` | 2026-09-10 | `ValueError: No API key was provided.` before; `400 INVALID_ARGUMENT` / `API key not valid.` after |
| Retry guidance | `https://ai.google.dev/gemini-api/docs/troubleshooting` | 2026-09-10 | "Only retry on transient errors (like 429, 408, or 5xx). Do not retry on client errors (like 400 or 403)" |
| Rate limits | `https://ai.google.dev/gemini-api/docs/rate-limits` | 2026-09-10 | "Rate limits depend on a variety of factors (such as your usage tier) and can be viewed in Google AI Studio." No number is published, so none is printed |
| Toolchain, re-observed | `uv --version`, the project interpreter, `google-adk` | 2026-09-10 | uv 0.12.3, CPython 3.12.12, google-adk 2.8.0 — unchanged since day 06, so no new `PINS.md` row |

## §10 Ledger & commit

**`docs/PROGRESS.md`:**

```text
| 9 | 2026-09-10 | AG-04, RS-01 | 4 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the terms this day defined for the first time. `Session` is **not** among
them: it was defined on day 6 part 2.1 and today links that row rather than restating it.

```text
| Session service | The object that owns stored sessions and hands them out by address. Your code stops holding the conversation and holds only `(app_name, user_id, session_id)`; the service decides which conversation that names, and an in-memory one is a dictionary in your process that nothing evicts and no restart survives. | day 9 part 1.1 | the session store, `SessionService` |
| Invocation | One call to the runner for one user message, and the unit every event in it is stamped with. A session is the thread; an invocation is one exchange inside it, which is why `invocation_id` is what you grep for when a session holds hundreds of events and one question went wrong. | day 9 part 1.1 | one run, a turn's run |
| Error event | The final event of a failed run: `is_final_response()` is true, `content` is `None`, and `error_code` and `error_message` carry the exception's class name and its text. It is emitted in addition to the exception being raised, not instead of it. | day 9 part 2.1 | the failure event |
```

**`docs/PINS.md`** — nothing to add. uv 0.12.3, CPython 3.12.12 and google-adk 2.8.0 were
re-observed today and are unchanged since day 06; re-observing a pin that has not moved does not earn
a row, and inventing one would make the ledger say something happened.

**`docs/SOURCES.md`** — nothing to add. Today leans on two provider documentation pages and one API
reference, all dated in §9; none is a record with a resolvable identifier, which is the same call
days 3 and 7 made.

**`projects/01-ask-desk/CODEMAP.md`** — three rows gain a clause, because a file printed twice in one
project is a bug unless the second is a marked diff and the table says so:

```text
| `run.py` | day 04 part 2.1, whole · the `adk` subcommand added as a marked diff on day 06 part 2.1 · the `session` subcommand added as a marked diff on day 09 part 1.1 |
| `ask_desk/agent.py` | day 06 part 1.1, whole · `export_key()` added as a marked diff on day 09 part 2.1 |
| `ask_desk/scripted.py` | day 08, whole · `Fail` and `FAILS_AFTER_A_TOOL` recapped as marked regions on day 09 part 2.1 |
```

**Commit:**

```text
day 09: P01 Ask Desk · 6 — Sessions, runs, and errors that surface instead of hiding — closes AG-04, RS-01
```
