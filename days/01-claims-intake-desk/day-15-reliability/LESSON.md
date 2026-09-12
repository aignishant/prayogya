---
project: "P01"
day: 15
title: "Reliability"
spine: 13
kind: mechanism
deploy_tier: D3
plan_version: "v4.1.0"
parts: 4
files_printed: [claims_desk/reliability.py, tests/test_reliability.py]
generated: "2026-09-11"
status: written
commit: ""
---

> **Yesterday:** the decision record — the facts a rule read, replayed from the record alone, and the
> limit that a replay proves consistency rather than truth.
> **Today:** what the desk does when the provider is not there. Three attempts on day 1's schedule,
> the provider's own `Retry-After` beating it, a cap past which waiting is a refusal, an idempotency
> key so a retried write lands once — and an escalation instead of every graceful degradation on
> offer.
> **Tomorrow:** security and privilege — the threat model for this desk, and what a tool result is
> allowed to talk you into.

## §1 The scene

Day 1 built `util/backoff.py` before this project had anything to retry.

That looked odd at the time. The reason is in its own docstring: *a claims desk that invents an
in-force date because the provider was busy has not degraded gracefully; it has made something up
about a policy.* It was written early because the temptation it defends against arrives on the first
bad afternoon, and by then nobody is writing careful code.

Today is that afternoon. Three attempts have failed, eleven claims are waiting, and every option that
feels like engineering is a way of deciding a claim without an answer. Assume a safe default — and
write into a decision record that a policy does not cover a loss, which nobody established. Fall back
to a cheaper model — and two claims with identical facts get different verdicts depending on what was
up. Reuse a similar claim's reading — a classification by analogy, recorded as a classification by
reading, from a retriever whose own `recall@1` is 0.7.

So the desk asks again, carefully, and then stops. Three attempts, day 1's waits of 1 and 2 seconds,
the provider's own interval winning whenever it gives one, capped at thirty seconds because past that
"wait" is really "stop". A retry the budget cannot pay for is not attempted at all. And when the
attempts run out the claim is marked pending with `provider_unavailable` — a different wait from
`needs_classification`, because one wants the run repeated and the other wants a person.

The other half of the day is the write. A read may be repeated; recording a decision may not. Every
decision now carries an **idempotency key** derived from the decision's own content, so the same
write twice lands once, and a *different* decision about the same claim is refused rather than
silently replacing the first — which, as it turns out, is what used to happen.

## §2 The map

Three sections. **Section 1 is asking again** — the retry, and the write that must not repeat.
**Section 2 is what not to do** when the answer never comes. **Section 3 is what holds it.**

### 1 · Asking again

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-asking-again/1.1-honest-retry.md) | Honest retry: wait what you were told to wait | How many times, how long, and who decides? | working |
| [1.2](parts/01-asking-again/1.2-write-that-must-not-happen-twice.md) | The write that must not happen twice | What stops a retried write from landing twice? | production |

### 2 · What not to do

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-what-not-to-do/2.1-answer-you-must-not-fabricate.md) | The answer you must not fabricate | The attempts ran out. Now what? | production |

### 3 · Holding it

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-holding-it/3.1-what-the-tests-hold.md) | What the tests hold | How do you test a waiting policy without waiting? | production |

## §3 Setup — run this

Nothing new is installed. One module is added, one stand-in joins `scripted.py`, and three files gain
a parameter so a key can reach the store.

```bash
./run check
```

Expect `181 passed` before you start — day 14's total — and `200 passed` at the end. One test from
day 6 goes red partway through: the `record_decision` stub needs the new argument, which is the fifth
time that stub has changed and is now a `TODO(me)` about the shape of that tool.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `claims_desk/reliability.py` | part 1.1 |
| `tests/test_reliability.py` | part 3.1 |

Four earlier files change, each printed as a marked diff naming the day that printed the original:
`claims_desk/scripted.py` (day 7 part 1.2, extended day 9 part 1.2) gains `ScriptedTransient` in
part 1.1; `claims_mcp/tools.py` (day 5 part 1.1) and `claims_desk/desk.py` (day 7 part 2.1) change
in part 1.2; `claims_desk/desk.py` again in part 2.1 for the escalation; and
`claims_desk/boundary.py` passes the key across.

## §5 Build brief

Write `reliability.py` and test the waiting policy before wiring anything — `wait_for` is six lines
and every branch of it is one assertion. Then the retry, then the key, then the escalation. Then the
reps:

| File | What it must do |
| --- | --- |
| `claims_desk/reliability.py` | `TODO(me)`: a circuit breaker. Three attempts per claim across a queue of several hundred is several hundred calls at a provider that is already struggling. Write it, and say what it needs to count and for how long. |
| `claims_mcp/tools.py` | `TODO(me)`: the idempotency check is a read followed by a write, so two workers can both read "nothing there". Make it conditional at the storage layer, and say what that costs. |
| `claims_mcp/tools.py` | `TODO(me)`: a claim written before today has no key, so it can still be silently replaced once. Write the backfill, or write down why you would not. |
| `tests/test_reliability.py` | `TODO(me)`: no test exercises the real `asyncio.sleep`. Add the one that does — a single retry with a tiny interval and no `sleep` argument. |
| Your own notes | `TODO(me)`: `record_decision` now takes six parameters and five of them are optional. Sketch the shape you would replace it with, and say what breaks for every earlier day's tests. |

## §6 The check that must be able to fail

```bash
./run check
```

Green is `All checks passed!`, `200 passed`, and day 0's four `ok` lines.

Ways to make it red:

1. **Widen `except Transient` to `except Exception`.** `test_only_a_transient_is_retried` fails —
   a defect retried three times is three defects and a slower failure.
2. **Drop the budget guard.** `test_a_retry_the_budget_cannot_pay_for_is_not_attempted` fails on both
   assertions: an attempt was made, and a wait happened.
3. **Generate the idempotency key per attempt** instead of from the content.
   `test_the_same_intended_write_has_the_same_key` fails, and the retry it was meant to protect
   becomes a second write.
4. **Make `Watch` actually sleep.** Nothing fails and the file goes from 2.25 seconds to 10.12. That
   is part 3.1, and the point is that a green suite four times slower is a suite that stops being
   run.

And the one that is red for no test at all, which is part 2.1's failure: **default the classification
when the provider is down.** Twelve claims decided, twelve records, every one defensible — and
FNOL-4477's says its policy does not cover an escape of water on a policy that does.

## §7 Request budget

**Five model calls allowed per notification**, unchanged, and **seventeen spent across the queue** on
a good day — unchanged, because nothing retried.

What changes is the worst case. A claim whose provider is flaky can now spend up to three calls on
one classification, which is why day 9's ceiling had headroom and why the retry asks the budget
before each attempt. A claim that has already spent its allowance does not retry at all: one attempt,
no waits, straight to escalation.

The other cost is time rather than money. Twelve claims each waiting 1 and then 2 seconds before
escalating adds about 36 seconds to a queue that takes 42 — and produces the same escalation it would
have reached immediately. At a morning's several hundred notifications a full outage turns a
three-minute queue into a twenty-minute one, spent almost entirely asleep. That number is the
argument for the circuit breaker in §5.

## §8 Traps

- **A retry that cannot fail honestly is worse than no retry.** Everything here exists to make the
  giving-up path correct.
- **The provider's `Retry-After` beats your schedule** — it is not advice.
- **Except past a cap**, where "wait" has become "stop" and the honest response is to escalate.
- **A retry is another model call.** Ask the budget before attempting, not after.
- **Only retry the exception that means *try again*.** Retrying a defect three times is three
  defects.
- **The last attempt is not followed by a wait**, which is why day 1's schedule is one shorter than
  the attempt count.
- **Take `sleep` as a parameter**, or every test of your waiting policy is a test that waits.
- **A read may be repeated; a write may not.**
- **Derive the idempotency key from the write's content**, never per attempt and never per claim.
  Same write, same key; different decision, different key.
- **Check the key at the receiver, against the store** — a sender's memory answers for this process,
  and a retry is most likely running after a restart.
- **A repeat is a success**, and says so. A different decision under a new key is refused, not
  overwritten.
- **Log the count you made, not the count you allowed.** A line reporting a constant is
  indistinguishable from a correct one.
- **An agent may be unavailable. It may not be approximate.**
- **A default is only safe where the record can say it was a default** — and if there is nowhere to
  record that, the design is refusing the default.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| The waiting policy | this project | 2026-09-11 | `attempts: 3`, `waits: (1.0, 2.0)`, cap `30.0`; provider asking `None`/`0.5`/`5`/`900` waits `1.0`/`0.5`/`5`/`30.0`. |
| A busy provider, recovered | this project, `ScriptedTransient(fail_times=2, retry_after=0.5)` | 2026-09-11 | Two `reliability.retrying` lines with `"waiting": 0.5, "asked_for": 0.5`, then `escape-of-water` — the classifier's real answer. |
| A provider that never answers | this project | 2026-09-11 | Two retries, then `reliability.unavailable` with `"attempts": 3, "allowed": 3`, then `Unavailable: triage FNOL-4477 failed after 3 attempts`. |
| A retry the budget cannot pay for | this project | 2026-09-11 | `reliability.no_budget_to_retry` at attempt 1, then `"attempts": 1, "allowed": 3` — one attempt, no waits. |
| The same write twice | this project, over the boundary | 2026-09-11 | `{'recorded': True, ...}` then `{'recorded': True, 'repeat': True, ...}`; a different decision `{'recorded': False, 'refused': 'this claim already carries a different decision'}`; **one** claim file. |
| Two writes with no key | this project, deliberately | 2026-09-11 | `{'claim_id': 'FNOL-4471', 'outcome': 'deficiency', 'reason': 'injury_reported'}` — the second write silently won. |
| The escalation, end to end | this project | 2026-09-11 | `desk.provider_unavailable`, then `Verdict(..., outcome='pending', waiting_for='provider_unavailable', record=None)`, and an empty claims directory. |
| The fabricated default | this project, deliberately broken | 2026-09-11 | `claims decided: 12`, `all defensible: True`, and `FNOL-4477 reason: peril_not_covered` on a policy that covers escape of water. |
| A suite that waits | this project, `Watch` made to sleep | 2026-09-11 | `19 passed in 10.12s` against `2.25s` — green, and four and a half times slower. |
| The gate | this project, `./run check` | 2026-09-11 | ruff clean, `200 passed`, day 0's four checks green. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 01 | 15 | 2026-09-11 | Reliability | 4 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the first restates a definition the glossary already carries; the rest are
new:

```text
| Transient | A failure worth trying again, carrying the interval the other side asked for. Day 1 gave it that field; day 15 is the first code that sets it, and the provider's interval beats the local schedule. | P01 day 15 part 1.1 | a retryable error |
| Retry-After | The interval a provider asks you to wait. An instruction rather than advice — honoured up to a cap, past which it is a refusal and the honest response is to escalate. | P01 day 15 part 1.1 | the backoff hint |
| Budget guard | A check before a retry that refuses to attempt what the unit of work cannot pay for, so an allowance is not spent discovering it is gone. | P01 day 15 part 1.1 | a spend check |
| Idempotency key | A name for one intended write, derived from the write's own content so the same write twice lands once and a different decision produces a different key. Checked at the receiver against the store, never at the sender against a cache. | P01 day 15 part 1.2 | a dedupe key |
| Escalation | Marking work as pending with a named reason rather than producing an answer nobody established. The only honest end to a failed retry in a system that has to defend its decisions. | P01 day 15 part 2.1 | giving up honestly |
| Fabricated answer | Any value a system supplies in place of one it could not obtain — a default, a fallback model, an analogous case. It replays correctly and asserts something nobody established, which is what makes it dangerous. | P01 day 15 part 2.1 | graceful degradation, misapplied |
```

**`docs/PINS.md`** — no row is owed. Nothing was installed today.

**`docs/SOURCES.md`** — no row is owed. Nothing with a citation identifier was cited.

**Commit:**

```text
P01 day 15: Reliability
```
