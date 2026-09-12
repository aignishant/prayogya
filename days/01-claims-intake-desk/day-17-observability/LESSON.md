---
project: "P01"
day: 17
title: "Observability"
spine: 15
kind: mechanism
deploy_tier: D3
plan_version: "v4.1.0"
parts: 7
files_printed: [claims_desk/util/trace.py, claims_desk/alerts.py, tests/test_observability.py]
generated: "2026-09-12"
status: written
commit: ""
---

> **Yesterday:** security and privilege — the threat model as data, a quarantined description,
> injection through a tool result, an allowlist that says none, two processes with different powers,
> and a gate that holds a large claim until a person signs.
> **Today:** one id across every module and both processes, a span around everything that takes time,
> the span that was not there and what it found, and a table saying which single event wakes a person.
> **Tomorrow:** evals — a set with a declared right answer, a score that can fall, and the gate that
> goes red when the desk gets worse.

## §1 The scene

A claim file has a reference number on the front, and the reason is not filing. It is what lets a
handler, the policy department, correspondence and an adjuster all work on the same claim without ever
meeting: everything any of them produces goes into one folder, and six months later one person pulls
one folder and has the whole story.

This desk has no folder. It produces three hundred log lines a run, from nine modules and two
operating-system processes, interleaved across twelve claims because the queue does not pause between
them. Some lines carry a `claim` field and some cannot — `boundary.connected` does not know which claim
opened it, and `hooks.model` does not know which claim it answered for. The story is all there and
there is no way to collect it.

And nobody has ever timed any of it. Thirteen days of careful work, and asked which part of this desk
is slow, the honest answer was that nobody knew. Not suspected-and-unconfirmed. Unknown.

Today puts a reference number on every line and a stopwatch round every region — and then does the
thing that instrumentation is for, which is **read the output**. Two of this project's log lines turn
out to have been printing `<redacted>` for a fortnight. And the queue turns out to spend **ninety-eight
per cent of its time launching Python subprocesses**, which was true every day since day 4 and which no
amount of reasoning would have produced.

## §2 The map

Seven parts in four sections: the id, the clock, the telephone, and the tests.

### 1 · One id

The correlation id, where it lives, and how it crosses a process line.

| Part | Title | Level |
| --- | --- | --- |
| 1.1 | One id for one piece of work | working |
| 1.2 | Carrying it across a process line | working |

### 2 · Where the time went

Spans — and the discipline of noticing that a number is unexplained.

| Part | Title | Level |
| --- | --- | --- |
| 2.1 | The span that was not there · **failure** | production |
| 2.2 | Reading a queue you have never timed | production |

### 3 · Who gets woken

The paging rules, and the log line that had stopped saying anything.

| Part | Title | Level |
| --- | --- | --- |
| 3.1 | What wakes a person | production |
| 3.2 | The log line nobody read · **failure** | production |

### 4 · Holding it

| Part | Title | Level |
| --- | --- | --- |
| 4.1 | What the tests hold | production |

## §3 Setup — run this

Nothing new is installed. Two modules are added, one test file, and four earlier files change.

```bash
./run check
```

Expect `225 passed` before you start — day 16's total — and `250 passed` at the end. **One test from
day 4 goes red partway through**: `test_the_desk_reaches_the_boundary_over_stdio_by_default` asserts
`boundary.target() is boundary.LAUNCH`, and once the launch parameters carry a trace id they are no
longer the same object. It is right to notice and the fix is in part 1.2.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `claims_desk/util/trace.py` | part 1.1 |
| `claims_desk/alerts.py` | part 3.1 |
| `tests/test_observability.py` | part 4.1 |

Four earlier files change, each as a marked diff naming the day of this project that printed the
original: `claims_desk/util/logging.py` (day 1) in part 1.1 — nine lines, and every log line in the
project gained two fields; `claims_desk/boundary.py` (day 4) in parts 1.2 and 2.1;
`claims_desk/workflow.py` (day 10) and `claims_desk/desk.py` (day 6, last changed day 16) in part 2.2;
and `tests/test_transports.py` (day 4) in part 1.2.

## §5 Build brief

Write `trace.py` and the `logging.py` diff first, and print a trace before adding a single span — the
point of part 2.1 is lost if the spans are all there from the beginning. Then the boundary's spans, then
the queue's, then read the numbers. `alerts.py` last, because its rules are a judgement about events the
rest of the day taught you to read. Then the reps:

| File | What it must do |
| --- | --- |
| `claims_desk/util/trace.py` | `TODO(me)`: `current()` reads `os.environ` on every log line for a value that cannot change after start-up. Decide whether to cache it, and say why the argument is about honesty rather than speed. |
| `claims_desk/boundary.py` | `TODO(me)`: the connection cost, with **your own machine's number** in it — the pool's size, what happens when a pooled connection dies mid-claim, and the test for the concurrent case day 10 created. |
| `claims_desk/boundary.py` | `TODO(me)`: the version that carries the trace in the protocol's `meta` rather than the child's environment. What it costs, what it buys over HTTP, and whether the boundary changes. |
| `claims_desk/alerts.py` | `TODO(me)`: `summarise` has no call site. Wire it into `run_queue`, or say in the docstring that it is for whatever reads the log afterwards — and defend the choice. |
| `claims_desk/alerts.py` | `TODO(me)`: the rule for today's own finding, the 1.7-second connection. Which level, what threshold, against what — and whether it belongs in this table at all. |
| `tests/test_observability.py` | `TODO(me)`: the well-formed-tree test — every span's `parent` was open when the span closed. Run it against a queue and say whether this project's spans pass. |
| Your own notes | `TODO(me)`: the `<redacted>` assertion over the whole queue rather than one boundary call. Say whether it found a third line, and whether the name or the redactor is at fault. |

## §6 The check that must be able to fail

```bash
./run check
```

Green is `All checks passed!`, `250 passed`, and day 0's four `ok` lines.

Ways to make it red:

1. **Pass only the trace id to the boundary subprocess** instead of the whole environment.
   `KeyError: 'PATH'` — and without that assertion, the boundary silently fails to start and every
   claim escalates as `provider_unavailable`.
2. **Rename the span's `fields` back to `keys`.** `AssertionError: span.keys says nothing` — day 1's
   redactor matches `key` as a substring.
3. **Promote `desk.provider_unavailable` to `PAGE`.** `test_exactly_one_event_pages_on_its_own` fails,
   which is not a claim that the rule is wrong — only that changing who gets woken is a conversation.
4. **Remove the `reset` from `span`'s `finally`.** `test_the_span_stack_survives_a_failure` fails, and
   in a real run a failed span leaves its name on every later line in the process.
5. **Make `log` write `"trace": None` instead of omitting it.** `test_an_untraced_line_carries_no_empty_fields`
   fails.

And the two that are green while being wrong, which are this day's deliberate failures:

- **Part 2.1** — take the `boundary.connect` and `boundary.tool` spans out. **250 tests pass.** The
  trace reports `boundary.call: 1863ms` with nothing inside it, and the only available conclusion —
  that the boundary is slow — sends somebody to optimise a file that answers in twelve milliseconds.
- **Part 3.2** — this project shipped a log line that said `<redacted>` for six days, through every
  green check, because no test asserted that a log line says anything.

## §7 Request budget

**Five model calls allowed per notification**, unchanged, and **fifteen spent across the queue**,
unchanged — today adds no agent, no turn and no call. Nothing in this day touches a provider.

What today adds is measurement of what those calls cost, and the answer is the day's most useful
number: `triage` totals 0.6 seconds across eight calls and `correspondence` 0.1 seconds across seven.
**Seven tenths of a second in a sixty-eight second run.** That is a property of the scripted stand-in
rather than of agent systems — with a real provider those two rows would be the largest in the table —
and it is exactly why the boundary's 67.1 seconds was invisible until something measured it.

The other cost is the log itself. A traced run of the queue writes 302 lines, of which **108 are
`span` records** — the instrument is now the most frequent single event in the file. Part 2.2's production note has what
that becomes at an intake desk taking thousands of notifications a day, and the rule that survives:
sample the traces, never the lines.

## §8 Traps

- **A log line with no reader is not instrumentation.** It is a comment that costs disk.
- **Ambient context, not a parameter.** Fifty call sites is fifty chances to forget, forever.
- **A `ContextVar`, not a global** — the sequential case passes either way, and the concurrent case
  labels every line with another claim's id.
- **`ContextVar` values should be immutable.** A list appended to by two tasks is two corrupted stacks.
- **Adopt an arriving id, never replace it**, or two processes produce two unrelated traces.
- **An environment variable set to the empty string is not an id.**
- **An API that replaces a whole environment must be handed the whole environment.**
- **A trace with a gap tells you where the time is not.** Ask of every span: what is inside this that I
  have not named?
- **The tell is in the timestamps** — a span whose first internal line is half a second after its own
  start has half a second of unnamed work at the front.
- **Put spans either side of every boundary the code crosses** — a process, a network, a disk — not
  only around the functions that felt important.
- **A span that raises must still be logged**, and must still pop its own stack.
- **Record what you only learned at the end** on the span's own line, so nobody has to join two records.
- **A measurement tells you what to work on, never what to do.**
- **Optimising the biggest number is not the same as optimising the biggest number you can act on.**
- **The page you add today is paid for on the night of the page you needed.**
- **The bar for a page is that there is an action and waiting makes it worse** — not that the event is
  serious.
- **A burst threshold is a share, never a count**, or it pages more as the system gets busier.
- **An unclassified event is a ticket, not silence.**
- **A page carries the numbers it was decided from.**
- **A safety net that grows exceptions stops being a safety net** — fix the field name, not the
  redactor.
- **An `autouse` fixture disarms the test whose subject is the precondition it establishes.**

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| One id across two processes | this project, `./run desk` | 2026-09-12 | 302 lines, `traces: {'t-c1de696d9398'}` — every line the desk wrote and every line 40 boundary subprocesses wrote. |
| A boundary line carrying the desk's trace | this project | 2026-09-12 | `"trace": "t-c1de696d9398", "event": "boundary.draft_letter"` — written by the child process, with no `span`, because spans do not cross. |
| `StdioServerParameters` accepts an environment | this project, `mcp` 2.2.0 | 2026-09-12 | `model_fields` includes `env: dict[str, str] | None`, default `None`. |
| MCP has a metadata channel | this project, `mcp` 2.2.0 | 2026-09-12 | `Client.call_tool(..., meta: RequestParamsMeta | None = None)` — separate from the tool's own arguments. |
| The trace with a gap | this project, spans removed deliberately | 2026-09-12 | `boundary.call: 1863.4ms` containing nothing, with the enclosed work finishing 362ms before the span closed. |
| The span that was missing | this project | 2026-09-12 | `boundary.tool: 12.5ms` inside `boundary.connect: 2078.9ms` inside `boundary.call: 2079.2ms`. |
| Where the queue's time goes | this project, one traced run | 2026-09-12 | queue 67.8s · `boundary.call` 67.1s · `boundary.connect` 67.1s · `boundary.tool` 0.6s · `triage` 0.6s · `correspondence` 0.1s. |
| The connection cost, distributed | this project | 2026-09-12 | 40 connects, `min=1218 max=2288 mean=1677ms`; 40 tool calls, `min=6.7 max=90.9 mean=14.8ms`; **98.1%** of the run. |
| The cheapest claim in the queue | this project | 2026-09-12 | FNOL-4481 at 4387.3ms, `spent=1` — day 16's gate, measured as time from the other side. |
| The redactor eating a field name | this project | 2026-09-12 | `"keys": "<redacted>"` on `hooks.tool_result` and `"key": "<redacted>"` on `boundary.record_decision.repeat`. |
| The whole queue's paging decision | this project | 2026-09-12 | `level: ticket`, `reasons: []`, one `desk.awaiting_approval` — nobody woken. |
| The gate | this project, `./run check` | 2026-09-12 | ruff clean, `250 passed`, day 0's four checks green. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 01 | 17 | 2026-09-12 | Observability | 7 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — new rows:

```text
| Correlation id | One value generated per unit of work and attached to every line that work produces, so a story spread across modules and processes can be collected by a single query. Ambient rather than passed, or the one function that forgets it produces lines nobody can find. | P01 day 17 part 1.1 | a trace id |
| Ambient context | A value attached to the current execution that anything can read without being handed it. A `ContextVar` in Python, and never a module-level global in a concurrent program, where a global labels every line with whichever value was set last. | P01 day 17 part 1.1 | implicit per-task state |
| Span | A named region with an elapsed time and a parent, logged whether it returned or raised. A claim about where time goes — and one with unexplained time inside it is a claim that is false in a way nobody notices. | P01 day 17 part 1.1 | a timed block |
| Trace propagation | Carrying a correlation id across a process line, so two programs' log lines join up. Here the child's environment, which works because this desk launches the boundary and does nothing at all over HTTP. | P01 day 17 part 1.2 | passing the id along |
| Missing span | Time inside a span that no smaller span accounts for. It appears as nothing at all rather than as a gap, so the trace stays green and supports a wrong conclusion. | P01 day 17 part 2.1 | untimed work |
| Page | An alert that wakes a person. Justified only when there is an action and waiting makes it worse — never by severity, because paging for a designed behaviour teaches a rota to acknowledge without reading. | P01 day 17 part 3.1 | a call-out |
| Burst threshold | A rule that promotes a counted event to a page when enough of them arrive. Expressed as a share of the work rather than a count, or it fires more as the system grows busier. | P01 day 17 part 3.1 | a rate-based alert |
| Alert fatigue | What a rota develops after enough pages it could not act on: acknowledging without reading. The cost is paid on the night the page is real. | P01 day 17 part 3.1 | pager blindness |
```

**`docs/PINS.md`** — no row is owed. Nothing was installed today.

**`docs/SOURCES.md`** — no row is owed. Nothing with a citation identifier was cited.

**Commit:**

```text
P01 day 17: Observability
```
