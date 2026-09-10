---
project: "P01"
day: 2
title: "The domain and its data"
spine: 2
kind: mechanism
deploy_tier: D3
plan_version: "v4.1.0"
parts: 6
files_printed: [data/policies.json, data/notifications.json, claims_desk/domain.py, claims_desk/store.py, tests/test_domain.py]
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** a declared environment, an importable package, one door to operate the project
> through, and four pieces of kit — keys, logging, backoff, budget — with nine tests around them.
> **Today:** the desk gets something to work on. Eight invented policies, twelve invented
> notifications with their answers written by hand, the records as types, the one class that opens
> a file, and the discovery that two of the eight rules cannot be written as comparisons at all.
> **Tomorrow:** the store leaves this process. The policy file and the claim file go behind a
> boundary, and nothing above it is allowed to open a path again.

## §1 The scene

Somebody rings a claims desk and says: *the flexible hose under the sink let go overnight, water's
across the kitchen, plumber's been, no one hurt.* Nothing in that sentence is a field. There is no
policy number in it, no date, no peril code, no amount — and yet by the end of the call all of
those exist on a form, because the person taking it turned speech into a record while the caller
was still talking.

Today builds both halves of that. The record, first: what an insurer actually keeps about a policy,
narrowed to the fields some rule in this desk reads, and twelve notifications carrying what callers
said — including the ones who did not know what day it happened and the one whose line went dead
before a number was taken. All of it invented, and each notification carrying, written by hand, the
answer the desk is supposed to reach.

Then the rules. Eight ordered checks that turn a notification and a policy into a fast-track or a
letter naming one thing that is missing. Six of them are comparisons: is this date inside that
period, is this peril in that list, is this amount over that limit.

And two of them are not, which is what this day is really about. *Which peril is this?* and *was
anyone hurt?* are questions about a sentence a person spoke. The first version of the rules tried
to answer the second one by looking for words, and it decided that a caller who said "no one hurt"
had reported an injury — on the most fast-trackable claim in the queue. That failure is why there
is a model in this project at all, and it happened here, on this data, before any model existed.

## §2 The map

Three sections. **Section 1 is the data** — what the desk knows about policies, and what twelve
callers said. **Section 2 is the shape in code** — the records as types that cannot be misread, and
the one class allowed to open a file. **Section 3 is the contract** — the fixture set asserted as
promises, and the rule that could not be written.

### 1 · The record — what the desk knows

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-record/1.1-every-byte-invented.md) | Every byte of this is invented | What does the desk need to know about a policy, and where does that data come from? | foundation |
| [1.2](parts/01-the-record/1.2-call-as-it-was-taken-down.md) | The call, as it was taken down | What does a notification look like, and how do we know what the right answer is? | foundation |

### 2 · The shape in code — records and the one file-opener

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-shape-in-code/2.1-record-as-a-type.md) | The record as a type | How does JSON become something that cannot be compared wrongly? | working |
| [2.2](parts/02-shape-in-code/2.2-only-code-that-opens-a-file.md) | The only code that opens a file | Who is allowed to touch the data, and what does it promise? | working |

### 3 · The contract — the promises, and the one that could not be kept

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-the-contract/3.1-twelve-four-and-eight.md) | Twelve, four and eight | How does a fixture set stop being examples and become a contract? | production |
| [3.2](parts/03-the-contract/3.2-word-the-scan-cannot-read.md) | The word the scan cannot read | Why does this desk need a model at all? | production |

## §3 Setup — run this

Nothing new is installed today. The desk gains a data directory and two modules.

```bash
mkdir -p data
./run check
```

Expect the gate to be green before you start — nine tests from yesterday — and green again at the
end with nineteen. `data/claims/` is **not** created by hand: `write_claim` makes it the first time
the desk writes a decision, and nothing today writes one.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `data/policies.json` | part 1.1 |
| `data/notifications.json` | part 1.2 |
| `claims_desk/domain.py` | part 2.1 |
| `claims_desk/store.py` | part 2.2 |
| `tests/test_domain.py` | part 3.1 |

## §5 Build brief

Type the five files above, in that order — the data before the types that parse it, the types
before the store that yields them, the store before the tests that exercise it. Then the reps:

| File | What it must do |
| --- | --- |
| `data/notifications.json` | `TODO(me)`: FNOL-4481's `estimate` of 4800 is the **caller's** figure and the desk treats it as a fact. Write down, in a comment in your own notes, what a real desk would do instead — and say which of the eight rules would have to move. |
| `claims_desk/domain.py` | `TODO(me)`: `assess` returns the **first** failing rule. Write the version that returns all of them, then argue yourself out of it in three sentences. Keep whichever you can defend. |
| `claims_desk/store.py` | `TODO(me)`: `policy()` re-reads and re-parses the whole store on every call. Measure it with `time.perf_counter` over the twelve notifications, write the number down, and then do **nothing** — day 3 moves this behind a boundary and a cache here would be thrown away. |
| `tests/test_domain.py` | `TODO(me)`: add a test that every `policy_number` in the queue either exists in the store or is the one deliberate unknown. Decide whether it should fail if somebody adds a second unknown. |
| `tests/test_domain.py` | `TODO(me)`: `test_a_claim_file_is_replaced_in_one_step` proves the temporary file is gone on success. Add the case where the write **fails** part way, and prove it is gone then too. |

## §6 The check that must be able to fail

```bash
./run check
```

Green is `All checks passed!`, `19 passed`, and day 0's four `ok` lines.

Three ways to make it red:

1. **Duplicate a deficiency reason.** Copy the last notification, give it a new id, and run
   `./run test`. Expect `9 == 8` from the variety assertion — and note that the *first* version of
   that assertion did not catch this, which is in part 3.1.
2. **Let the rules read English again.** Change `assess` to call `mentions_injury_keyword_scan` on
   the description instead of taking `injury_reported`, and watch FNOL-4471 go from fast-track to
   deficiency. That is part 3.2, and it is the day's deliberate failure.
3. **Drop a leading zero in a fixture date.** Change an `inception` to `2026-3-14` and expect
   `ValueError: Invalid isoformat string` at parse time — not a wrong answer later, which is what
   the same edit produces if the dates are compared as text.

## §7 Request budget

**Zero.** Still nothing calls a model. Every one of the twelve verdicts in this day was reached by
comparing fields, and the two facts that could not be — the loss type and whether anyone was hurt —
were read from the fixture's own answer key rather than derived.

Part 3.2 is the argument for the first non-zero budget in this project. Day 7 spends it.

## §8 Traps

- **JSON has no dates.** `"2026-3-14"` and `"2026-03-14"` are both strings, and one of them sorts
  after October. Parse at the edge with `date.fromisoformat`, which raises, and never compare date
  strings anywhere.
- **The answer key must never be read by the desk.** `Store.expectations()` exists for tests and
  for day 18's evalset. If it ever appears under `claims_desk/agents/`, the evals are measuring
  whether the system agrees with itself.
- **A fixture's expected outcome is written by a person, never generated.** Regenerating it from
  the current behaviour turns every past decision into "correct" by definition.
- **`len(set(x)) == 8` does not catch a duplicate.** Nine items with eight distinct values passes.
  Assert `len(x) == len(set(x))` as well — and the way this was found was by adding the duplicate
  and watching the test go green.
- **Opening a file for writing truncates it immediately.** Not when you write, not when you close.
  A process killed between the two leaves an empty file, and `write_claim` exists for that one
  instant.
- **`tempfile.mkstemp(dir=...)` matters.** The temporary file must be on the same filesystem as the
  target or `os.replace` is a copy and stops being atomic. Same directory is the reliable way.
- **`os.replace`, not `os.rename`.** On Windows, `os.rename` fails when the target exists.
- **A keyword scan over free text is right most of the time.** That is the problem, not the
  consolation: eleven of twelve looks like a working rule.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| String dates compare as text | this project, `uv run python -c ...` | 2026-09-10 | `'2025-11-01' <= '2026-3-14' <= '2026-10-31'` is `False`; with the leading zero it is `True`. The failure in part 1.1. |
| A malformed date raises at the edge | this project, `Policy.from_record` | 2026-09-10 | `ValueError: Invalid isoformat string: '2026-3-14'`, at `domain.py` line 68. |
| Opening for write truncates first | this project, `data/claims/FNOL-4471.json` | 2026-09-10 | File empty after an interrupted write; `JSONDecodeError: Expecting value: line 1 column 1 (char 0)` on read-back. |
| The keyword scan disagrees with the fixture | this project, all twelve notifications | 2026-09-10 | One disagreement: FNOL-4471, scan `True`, declared `False`, on "No one hurt." |
| Patching the negation does not fix it | this project, four sentences | 2026-09-10 | `Nobody was injured` and `No injuries to report` both still come out `True`. |
| The whole queue, decided | this project, `assess` over the twelve | 2026-09-10 | Four fast-track, eight deficiency, eight distinct reasons — the `Done when` numbers from `PROJECT.md`. |
| The gate | this project, `./run check` | 2026-09-10 | ruff clean, `19 passed`, day 0's four checks green. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 01 | 2 | 2026-09-10 | The domain and its data | 6 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the first two restate definitions the glossary already carries; the rest
are new:

```text
| Atomic replace | Making a change visible in one indivisible step: write the new contents to a temporary file in the same directory, force them to disk, then move that file over the target. A reader sees the old contents or the new ones and never the gap. Only atomic within one filesystem, which is why the temporary file's directory matters. | P01 day 2 part 2.2 | atomic rename, write-and-swap |
| Torn read | A read that lands while a write is in progress and returns neither the old contents nor the new. Writing a file truncates it first, so the value returned is often nothing at all. | P01 day 2 part 2.2 | a dirty read, reading mid-write |
| Domain record | A type whose fields are the facts the business reasons about, as against a row, which is how they happen to be stored. Built once at the edge, so nothing further in ever sees a string that might be a date. | P01 day 2 part 2.1 | an entity, the model (domain) |
| Synthetic data | Data invented for a project rather than derived from anything real, marked as such in the file itself. The only kind that is safe to print, commit, paste into a document and run over a thousand times. | P01 day 2 part 1.1 | invented fixtures |
| Answer key | The declared correct outcome for each case in a fixture set, written by hand before the code existed and never produced by the system under test. Read by tests and evals; never by the system being measured. | P01 day 2 part 1.2 | expected outcomes, the gold set |
| Stand-in | Code that occupies the place of the real thing so that its absence is visible, named for what it is and trusted with no decision. Distinct from a test double, which stands in for a dependency during a run. | P01 day 2 part 2.1 | a placeholder |
| Inverted case | A test or eval case whose declared expectation is its own subject's failure, so that it goes red when the thing it depends on stops being broken. It tests the detector rather than the system. | P01 day 2 part 3.1 | a negative test, `expect_fail` |
```

**`docs/PINS.md`** — no row is owed. Nothing was installed today.

**`docs/SOURCES.md`** — no row is owed. Nothing with a citation identifier was cited.

**Commit:**

```text
P01 day 2: The domain and its data
```
