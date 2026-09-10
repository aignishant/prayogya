---
project: "P01"
day: 6
title: "The tool that must refuse — a deficiency is an answer, not an error"
spine: 5
kind: mechanism
deploy_tier: D3
plan_version: "v4.1.0"
parts: 5
files_printed: [claims_desk/desk.py, claims_desk/__main__.py, tests/test_desk.py]
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** the docket grew to four tools, a typed date parameter, and a read that answers
> `found: false` rather than raising.
> **Today:** the desk runs for the first time over all twelve notifications, decides four of them,
> and refuses to decide the other eight — with a field saying what it is waiting for.
> **Tomorrow:** the first model call. The eight pending notifications get a classification, and this
> project finds out what it costs to let something read a sentence.

## §1 The scene

There are two trays behind the intake counter. One is decided and gone. The other has a card on it
saying *awaiting information*, and on most days it is the larger of the two. It is not a failure
tray: an incomplete claim arriving is the ordinary state of an intake desk, and the work of the desk
is mostly writing to ask for what is missing.

Today the desk discovers it has a tray of its own. Four of day 2's eight rules read fields — is
there a date of loss, a contact, a policy, was it in force — and the desk can apply those with
nothing but the boundary. The other four need somebody to have read the sentence the caller spoke,
and day 2 part 3.2 already proved that a keyword scan is not that somebody.

So the desk decides four and returns `pending` for eight, with `waiting_for:
needs_classification` — **the same shape as a deficiency, pointed at itself instead of at the
policyholder.** And `draft_letter`, asked to write a letter, returns the claim, the reason, the
thing to ask for and the house style, with `drafted: false`, because this boundary has no model and
will not put prose on an insurer's paper.

Then the day's own mistake. Because refusals are data rather than exceptions, somebody has to read
the data — and for about an hour this project's desk did not. It reported four deficiencies while
the boundary had refused every write and the claims directory was empty.

## §2 The map

Three sections. **Section 1 is the answer** — what the desk decides, what it refuses to decide, and
the tool that refuses to write. **Section 2 is the run** — one command over the whole queue.
**Section 3 is what holds it** — the tests, and the refusal that nobody read.

### 1 · A deficiency is an answer

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-an-answer/1.1-four-decided-eight-pending.md) | Four decided, eight pending | How far do the desk's rules actually reach, and what does it say about the rest? | working |
| [1.2](parts/01-an-answer/1.2-tool-that-will-not-write-the-letter.md) | The tool that will not write the letter | What should a tool return when it cannot do the thing it is named for? | working |

### 2 · The queue — one command, one line

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-queue/2.1-twelve-in-one-command.md) | Twelve in, one command | How do you run the desk, and what should it say when it finishes? | working |

### 3 · Holding it — the tests, and the day's own bug

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-holding-it/3.1-what-the-tests-hold.md) | What the tests hold | How do you test a process line without paying for it on every run? | production |
| [3.2](parts/03-holding-it/3.2-refusal-nobody-read.md) | The refusal nobody read | If refusals are data, who reads the data? | production |

## §3 Setup — run this

Nothing new is installed. Two new modules and one new command.

```bash
./run check
./run desk
```

Expect `56 passed` from the first once the day is built. Expect the second to take long enough to be
uncomfortable — around a minute and a half — and to print one line:
`{"deficiency": 4, "fast-track": 0, "pending": 8}`.

`./run desk` **writes claim files** into `data/claims/`, which is created on demand and is not in
`.gitignore` yet. Deciding whether it should be is a rep in §5.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `claims_desk/desk.py` | part 1.1 |
| `claims_mcp/tools.py` | part 1.2, as a marked diff against day 5 part 1.1 |
| `claims_desk/__main__.py` | part 2.1 |
| `tests/test_desk.py` | part 3.1 |
| `run` | part 2.1, as a marked diff against day 1 part 1.3 |

`tests/test_boundary.py` and `tests/test_tools.py` each change by one assertion, because the docket
grew to five tools and the boundary's version moved to `0.4.0`. Both are printed as marked diffs in
part 3.1 against the days that printed them.

## §5 Build brief

Write `claims_desk/desk.py`, add `draft_letter` and `WHAT_IS_NEEDED` to the boundary, add the entry
point and the driver command, then the tests. Let the gate tell you when to update the two
assertions. Then the reps:

| File | What it must do |
| --- | --- |
| `claims_desk/desk.py` | `TODO(me)`: the order of the four rules is duplicated from day 2's `assess`, and the docstring admits it. Write down what would go wrong if somebody reordered one and not the other, and which test would catch it. Then check whether that test exists. |
| `claims_desk/desk.py` | `TODO(me)`: eight claims are pending and nothing schedules them to be looked at again. Decide where a pending notification should go, and write the sentence you would put in `run_queue`'s docstring about running it twice. |
| `.gitignore` | `TODO(me)`: `data/claims/` is written by the desk and is not ignored. Decide whether a claim file is an output or a fixture, and act on the answer — it is a one-line change either way and the argument is the point. |
| `claims_desk/__main__.py` | `TODO(me)`: `sys.exit(0 if counts else 1)` always exits zero and the part says so. Write the exit rule you would want, in words, and name the day that makes it possible. |
| `claims_mcp/tools.py` | `TODO(me)`: three of the eight `WHAT_IS_NEEDED` entries ask the policyholder for nothing. Decide whether those should be deficiency letters at all, or a different kind of letter — and say what would have to change in `Reason` if you are right. |

## §6 The check that must be able to fail

```bash
./run check
```

Green is `All checks passed!`, `56 passed`, and day 0's four `ok` lines.

Ways to make it red:

1. **Reorder the four rules** in `rules_that_need_no_reading` — put the policy check first — and
   `test_the_four_rules_run_in_the_order_day_two_fixed` names the reason it got instead.
2. **Write a pending verdict to the claim file** — drop the `if verdict.decided` guard — and
   `test_only_decided_claims_reach_the_claim_file` lists twelve names where four belong.
3. **Delete an entry from `WHAT_IS_NEEDED`** and the totality test names the reason code that has
   nothing to ask for.
4. **Make `draft_letter` write prose.** Return a `letter` field with a sentence in it, and
   `test_the_letter_tool_refuses_to_write_the_letter` goes red on `drafted`.

And the day's deliberate failure, which had to be caused before the check that catches it existed:
send the boundary a reason code it does not know and **do not read the answer**. The desk reports
four deficiencies, the claims directory is empty, and nothing anywhere is red. Part 3.2 is that, and
the fix, and the test that now holds it.

## §7 Request budget

**Zero, and this is the last day it will be.**

Everything today is the desk operating at the limit of what field comparisons can decide. Eight of
twelve notifications are pending precisely because deciding them needs something that can read
English, and the whole point of the pending verdict is to say so without guessing.

Day 7 makes the first model call. When it does, the budget from day 1 — `claims_desk/util/budget.py`,
written on a day with nothing to count — starts counting, and the eight pending notifications are
what it will be spent on.

## §8 Traps

- **A pending verdict is not written to the claim file.** The absence of a claim file is the correct
  representation of "not decided"; a file saying `pending` is a record of a decision nobody made.
- **`in_force` has three states.** `True`, `False`, and `None` for "never asked", which is why the
  rule is `if in_force is False` rather than `if not in_force`.
- **Read the answer to every boundary call.** Refusals are data by design, and data that nobody
  reads is worse than an exception nobody catches.
- **A refusal about a claim is data; a refusal about your own request is a bug.** The first is an
  outcome, the second stops the batch.
- **`./run desk` takes about a minute and a half for twelve notifications.** Nothing is broken: it
  is a connection — and on stdio, a subprocess — per boundary call. Day 9 is where that changes.
- **Do not put `desk` in `check`.** It is slow and it writes files; a gate must be fast and leave
  nothing behind.
- **Patch `boundary.connected` in tests, never `boundary.call`.** The first swaps the transport; the
  second swaps the result envelope, the `is_error` handling and the unwrapping — which are the parts
  that have actually broken in this project.
- **The desk still opens one file for itself.** `data/notifications.json`, through `Store`. It is the
  only path the desk knows, and moving it behind the boundary is unfinished business.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| The whole queue, end to end | this project, `./run desk` over a real subprocess boundary | 2026-09-10 | `{"deficiency": 4, "fast-track": 0, "pending": 8}`, and `data/claims/` holding exactly `FNOL-4473`, `FNOL-4474`, `FNOL-4476`, `FNOL-4482`. |
| What it costs | this project, timed | 2026-09-10 | **91.4 seconds** for twelve notifications — about twenty-eight boundary calls, each one a fresh connection and therefore a fresh interpreter. |
| The letter tool refusing | this project | 2026-09-10 | `{"drafted": false, "why": "this boundary has no model; the letter is written by the caller", ..., "needed": "a photograph of the damage"}`, with `is_error: false`. |
| An unknown reason code | this project | 2026-09-10 | `{"drafted": false, "refused": "unknown reason 'no_photo'"}` — the rejected value is named. |
| The refusal nobody read | this project, with a bad reason code and no check | 2026-09-10 | `desk reports: {"deficiency": 4, ...}` and `claim files written: []`. No error, no warning, no red test. |
| The same break, after the fix | this project | 2026-09-10 | `RuntimeError: boundary refused to record FNOL-4473: unknown reason 'no_date'`. |
| A missing queue file | this project | 2026-09-10 | `FileNotFoundError` for `data/notifications.json`, and the driver's own `FAIL desk: ... exited 1`. |
| The tests | this project | 2026-09-10 | `11 passed in 5.08s` for `tests/test_desk.py` in-process; the same eleven over subprocesses take about a minute and a half. |
| The gate | this project, `./run check` | 2026-09-10 | ruff clean, `56 passed`, day 0's four checks green. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 01 | 6 | 2026-09-10 | The tool that must refuse — a deficiency is an answer, not an error | 5 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — one row per term this day defined for the first time:

```text
| Pending verdict | A decision the system declines to make, returned as a result with a field saying what it is waiting for. The same shape as a deficiency, pointed at the system rather than at the customer, and distinct from an error because nothing went wrong. | P01 day 6 part 1.1 | awaiting information |
| Unread refusal | A failure that is returned as data and never inspected by the caller. The obligation created by preferring refusals to exceptions: an exception forces a caller to deal with it, a returned refusal forces nothing. | P01 day 6 part 3.2 | a discarded result |
| Reconciliation | Comparing two independent records of the same work — a count of decisions against a count of stored records — so that a system which believes it did something can be caught not having done it. | P01 day 6 part 3.2 | the daily check |
| Transport substitution | Replacing only the thing that carries protocol messages, so that a test exercises the client, the envelope and the server for real and pays nothing for the pipe. Done at the one function whose job is choosing a transport. | P01 day 6 part 3.1 | in-process testing |
```

**`docs/PINS.md`** — no row is owed. Nothing was installed today.

**`docs/SOURCES.md`** — no row is owed. Nothing with a citation identifier was cited.

**Commit:**

```text
P01 day 6: The tool that must refuse
```
