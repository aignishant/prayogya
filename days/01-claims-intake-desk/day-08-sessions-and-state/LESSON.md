---
project: "P01"
day: 8
title: "Sessions and state"
spine: 7
kind: mechanism
deploy_tier: D3
plan_version: "v4.1.0"
parts: 5
files_printed: [claims_desk/sessions.py, tests/test_sessions.py]
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** the desk got an agent, and the queue produced the numbers `PROJECT.md` promised —
> with a session id that was a placeholder and a new session service on every single call.
> **Today:** conversations get an address, a service that outlives a call, a rule about what may
> never be written into them, and a look at how a failure actually arrives.
> **Tomorrow:** one agent becomes a cast. A second specialist, delegation and the handback, and a
> budget that has to hold across all of them.

## §1 The scene

A handler taking a call writes on a running sheet, and it is filed under the claim. Two calls about
the same claim end up on one sheet; a call about a different claim goes in a different file. And
there is a rule they are told twice, because the first time it sounds like fussiness: you write what
the caller said, you do not write the code they read out from the letter — because the sheet is
kept, copied and disclosed, and the person writing it is the only one in that chain who can prevent
anything.

Yesterday's agent had neither of those. Its session id was `"one-notification"` and its session
service was built fresh on every call, so every conversation was discarded the moment it ended.

Today the desk chooses an address — **the claim reference** — and keeps one service for the process.
Two questions about a claim accumulate; a question about another claim finds nothing at all. State
carries the claim reference and **refuses** a key whose name says it holds a secret or a person's
contact details, because a log line can be redacted and a session's state cannot be un-kept.

Then the run itself. One question yields one event and stores two, because the record includes the
question. And when the model fails, the exception reaches the caller **and** an error event goes
into the conversation — a final response with no content at all, which is why every read of
`event.content` in this project has a guard on it.

## §2 The map

Three sections. **Section 1 is the conversation** — where it lives, how it is addressed, and what it
must never hold. **Section 2 is the run** — the two accounts of one turn and why they are different
lengths. **Section 3 is what holds it**, including the failure that does both things at once.

### 1 · The conversation

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-conversation/1.1-one-conversation-per-claim.md) | One conversation per claim | Where does a conversation live, and what should it be filed under? | working |
| [1.2](parts/01-the-conversation/1.2-what-a-session-must-never-hold.md) | What a session must never hold | What is the difference between redacting and refusing? | working |

### 2 · The run

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-run/2.1-two-events-one-yielded.md) | Two events, one yielded | Why do the runner and the session disagree about how much happened? | working |

### 3 · Holding it

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-holding-it/3.1-what-the-tests-hold.md) | What the tests hold | How do you test something that keeps state between calls? | production |
| [3.2](parts/03-holding-it/3.2-failure-that-did-both.md) | The failure that did both | What shape does an error arrive in, and what breaks if you only read the successful one? | production |

## §3 Setup — run this

Nothing new is installed. One module is added and the classifier stops building its own runner.

```bash
./run check
```

Expect `66 passed` before you start — day 7's total — and `78 passed` at the end. Five tests from
day 7 will go red partway through, because `classify` gains a claim reference as its first
argument; that is the change working, and part 3.1 is where they are updated.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `claims_desk/sessions.py` | part 1.1 |
| `tests/test_sessions.py` | part 3.1 |

Two earlier files change and each is printed as a marked diff:
`claims_desk/agents/classifier.py` in part 1.1 — sixteen lines of runner machinery deleted and a
claim reference added — and `tests/test_agent.py` in part 3.1, where five call sites gain that
argument. `claims_desk/desk.py` gains the reference at its one call site.

## §5 Build brief

Write `claims_desk/sessions.py`, rewire the classifier through it, then the tests. Let the gate tell
you which day-7 tests need the new argument. Then the reps:

| File | What it must do |
| --- | --- |
| `claims_desk/sessions.py` | `TODO(me)`: `FORBIDDEN_IN_STATE` is a **deny**-list, and part 1.2 shows two keys that walk straight past it — `caller_ref` and `notes`. Write the allow-list version, where only agreed keys are permitted, and say what it costs the next person who needs a new key. |
| `claims_desk/sessions.py` | `TODO(me)`: `service` is a module-level global, and part 3.1's fixture exists to defend the tests against it. Write the version where the service is passed in, run the suite against both, and decide which you would ship. |
| `claims_desk/sessions.py` | `TODO(me)`: the session store does not survive the process. Write down the three questions this desk currently **cannot** answer about yesterday's batch, and which of them you would want a durable store for. |
| `claims_desk/agents/classifier.py` | `TODO(me)`: every notification gets a fresh session, so the classifier never sees a previous turn. Say what would change if it did — and whether you want that for a classifier. |
| Your own notes | `TODO(me)`: the stand-in never streams, so every event count in this project is one. Against a provider it would be many. Add that to the list day 7 started of things this project cannot learn from its own transcripts. |

## §6 The check that must be able to fail

```bash
./run check
```

Green is `All checks passed!`, `78 passed`, and day 0's four `ok` lines.

Ways to make it red:

1. **Change the session address.** Make `address` return a constant and
   `test_one_claims_conversation_is_not_in_another_claims_session` fails — one sheet with every
   claim on it.
2. **Drop a word from `FORBIDDEN_IN_STATE`.** Remove `contact` and one of the four parametrised
   refusals goes green when it should not.
3. **Stop recording the question.** Anything that leaves the user's event out of the session takes
   `(2, 4)` down to `(1, 2)`.
4. **Remove the content guard** — `and event.content` — in `sessions.turn`. Every test passes, and
   the next provider failure arrives as `AttributeError: 'NoneType' object has no attribute
   'parts'` instead of the real error. That is part 3.2 and it is the day's deliberate failure.

And one that is red for the right reason and easy to misread: **disable the `_fresh_sessions`
fixture** and `test_a_failure_also_arrives_as_an_event_in_the_conversation` fails with `assert 4 ==
2` — while passing when run on its own.

## §7 Request budget

**Two model calls per notification**, unchanged from day 7, and eight calls across the queue.

Sessions do not change the budget and they change what a call carries. Every turn now goes into a
conversation addressed by the claim, and a second question about the same claim is **appended to the
first** — which means that from day 9, when a cast asks several questions about one notification,
the conversation grows and every later call carries more history with it.

This project does not yet pay for that: the stand-in ignores the conversation entirely. Against a
provider, history is tokens, and tokens are the bill. That is one more line for the list of things
this project cannot measure about itself.

## §8 Traps

- **A session is addressed by three things**: app name, user and session id. Getting any of them
  wrong silently addresses a different conversation rather than failing.
- **File a conversation under the thing it is about.** A session id that is a run timestamp cannot
  answer "what did we say about this claim" and cannot answer a deletion request at all.
- **State is refused, not redacted.** A log line with a hole in it is still useful; state with a
  hole in it is a caller who thinks they stored something.
- **The deny-list is about names, so it protects against forgetting and not against deciding.**
  `caller_ref` and `notes` both walk past it.
- **The runner yields fewer events than the session stores.** The question is an event too. Name the
  count for what it counted.
- **`partial` has three states** and unset reads as `None`. Check for *not `True`*, never for
  `False`.
- **An error event is `is_final_response()` with `content` of `None`.** Guard every read of
  `event.content`, or a provider outage arrives as an `AttributeError` in your parser.
- **A failing model stand-in still needs a `yield`** after the `raise`, or it is not a generator and
  the framework fails on the wrong thing.
- **`InMemorySessionService` does not survive the process.** Nothing evicts it and no restart keeps
  it; what survives a run is the claim file and the log.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| The framework's session API | the installed package, by introspection | 2026-09-10 | `Session` carries `id, app_name, user_id, state, events, last_update_time`; `create_session(*, app_name, user_id, state=None, session_id=None)`; `get_session(*, app_name, user_id, session_id)`. |
| A session accumulates | this project | 2026-09-10 | `after one turn : events in session = 2 | state = {'claim': 'FNOL-4471'}`, then `= 4` after a second question, with state unchanged. |
| Claims are isolated | this project | 2026-09-10 | `a different claim: None` — not an empty session, no session. |
| The store does not survive | this project, two processes | 2026-09-10 | `this process: found`, `a new process: none`. |
| State refuses by name | this project | 2026-09-10 | `'contact_ref' ... 'contact' names something that should not be`; `'api_key' ... 'key' ...`; and `{'claim': ...}` allowed. |
| And what it lets through | this project | 2026-09-10 | `{'caller_ref': 'C-3301'}` and `{'notes': 'ring back on 0000 000000'}` both pass. `{'e_mail': 'x'}` passes too. |
| Yielded against stored | this project | 2026-09-10 | `runner yielded: 1` (`author='classifier'`, `partial=None`); `session holds: 2`, the extra being `author='user'`, both stamped with the same `invocation_id`. |
| How a failure arrives | this project, with a failing stand-in | 2026-09-10 | `RuntimeError: the provider was unreachable` raised **and** an event with `author='classifier'`, `error_code='RuntimeError'`, `error_message='the provider was unreachable'`, `content=None`, `is_final_response()=True`. |
| What happens without the guard | this project | 2026-09-10 | `AttributeError: 'NoneType' object has no attribute 'parts'`. |
| Order-dependent tests | this project, fixture disabled | 2026-09-10 | `assert 4 == 2` in the full file; the same test passes alone with `-k`. |
| The gate | this project, `./run check` | 2026-09-10 | ruff clean, `78 passed`, day 0's four checks green. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 01 | 8 | 2026-09-10 | Sessions and state | 5 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the first four restate definitions the glossary already carries; the rest
are new:

```text
| Session | One stored conversation, identified by an app name, a user and a session id, held by a session service rather than by your code. | P01 day 8 part 1.1 | the stored conversation |
| Session service | The object that owns stored sessions and hands them out by address. Your code stops holding the conversation and holds only the address; an in-memory one is a dictionary in your process that nothing evicts and no restart survives. | P01 day 8 part 1.1 | the session store |
| Invocation | One call to the runner for one user message, and the unit every event in it is stamped with. A session is the thread; an invocation is one exchange inside it. | P01 day 8 part 2.1 | one run, a turn's run |
| Error event | The final event of a failed run: `is_final_response()` is true, `content` is `None`, and `error_code` and `error_message` carry the exception's class name and its text. It is emitted **in addition to** the exception being raised, not instead of it. | P01 day 8 part 3.2 | the failure event |
| Session state | A dictionary that travels with a conversation, is written into the store and survives every turn. Retained, therefore refused rather than redacted: it carries references, never contents. | P01 day 8 part 1.2 | the state dict |
| Partial event | An event marked as a fragment of something still arriving rather than as a thing you may act on, flagged by `partial`. The field has three states, because unset reads as `None` — which is why the condition is written "not `True`" rather than "`False`". | P01 day 8 part 2.1 | a streaming chunk |
| Deny-list | A rule that names what is forbidden and permits everything else. Cheap, catches the ordinary mistake, and cannot say what a system *does* contain — as against an allow-list, which can and costs a decision per new entry. | P01 day 8 part 1.2 | a blocklist |
| Order-dependent test | A test whose result depends on which other tests ran first, produced by shared mutable state. It fails in CI and passes alone, and its message never mentions the cause. | P01 day 8 part 3.1 | a flaky test |
```

**`docs/PINS.md`** — no row is owed. Nothing was installed today.

**`docs/SOURCES.md`** — no row is owed. Nothing with a citation identifier was cited.

**Commit:**

```text
P01 day 8: Sessions and state
```
