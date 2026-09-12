---
project: "P02"
day: 2
title: "The domain and its data"
spine: 2
kind: mechanism
deploy_tier: D3
plan_version: "v4.1.0"
parts: 6
files_printed: [data/ledger.json, data/counts.json, stock_desk/domain.py, stock_desk/store.py, tests/test_domain.py]
generated: "2026-09-12"
status: written
commit: ""
---

> **Yesterday:** a declared environment, an importable package, one door to operate the project
> through, and four pieces of kit — keys, logging, backoff, budget — plus a registry that refuses
> an alias, with seventeen tests around them.
> **Today:** the desk gets something to work on. Sixty invented bins, sixty invented cycle counts
> with their answers written by hand, the records as types, the one class that opens a file, and
> the discovery that a keyword scan cannot be patched into reading a counter's own words.
> **Tomorrow:** the store leaves this process. The ledger file and the count queue go behind a
> boundary, and nothing above it is allowed to open a path again.

## §1 The scene

A counter walks bin A-10-2 at ten to eleven and finds four more units of ball bearings than the
ledger says should be there. Nothing about the shelf is confusing — a supplier dropped stock this
week that has not been booked in yet, and the counter writes exactly that down, in their own words,
because the count sheet has a note field and nothing smarter to offer them.

Today builds both halves of that. The record, first: what a warehouse's stock system actually
keeps about a bin, narrowed to the fields some rule in this desk reads, and sixty cycle counts
carrying what counters wrote — including the one that used a word the system cannot recognise, and
the one where nobody on shift could explain the gap at all. All of it invented, and each count
carrying, written by hand, the answer the desk is supposed to reach.

Then the rule. Four ordered checks that turn a bin and a count into one of four outcomes: matched,
explained, needing replenishment, or an overage nobody has accounted for. Three of those checks are
comparisons: is the delta zero, is the delta negative, is there a reason on file.

And one of them is not, which is what this day is really about. *Why does this bin disagree with
the ledger?* is a question about a sentence a counter wrote. The first version of the rules tried
to answer it by looking for words, and it decided that a delivery described as "the supplier's
Wednesday drop" was not a receipt at all — on the most explainable variance in the queue. Widen the
word list to catch it, and a different note breaks instead: the scan cannot get more correct, only
differently wrong. That failure is why there is a model in this project at all, and it happened
here, on this data, before any model existed.

## §2 The map

Three sections. **Section 1 is the data** — what the desk knows about a bin, and what sixty counts
carry. **Section 2 is the shape in code** — the two records as types, and the one class allowed to
open a file. **Section 3 is the contract** — the fixture set asserted as a promise that can go red,
and the day the promise gets found out about a keyword scan.

### 1 · The record — what the desk knows

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-record/1.1-every-unit-of-this-is-invented.md) | Every unit of this is invented | What does the desk need to know about a bin, and where does that data come from? | foundation |
| [1.2](parts/01-the-record/1.2-the-count-as-it-was-called-in.md) | The count, as it was called in | What does a cycle count look like, and how do we know what the right answer is? | foundation |

### 2 · The shape in code — records and the one file-opener

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-shape-in-code/2.1-the-record-as-a-type.md) | The record as a type | How does JSON become something that cannot be compared wrongly? | working |
| [2.2](parts/02-shape-in-code/2.2-only-code-that-opens-a-file.md) | The only code that opens a file | Who is allowed to touch the data, and what does it promise? | working |

### 3 · The contract — the promise, and the one word the scan cannot read

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-the-contract/3.1-sixty-fifty-one-and-nine.md) | Sixty, fifty-one and nine | How does a fixture set stop being examples and become a contract? | production |
| [3.2](parts/03-the-contract/3.2-the-word-the-scan-cannot-read.md) | The word the scan cannot read · **failure** | Why does this desk need a model at all? | production |

## §3 Setup — run this

The folder from day 1, with the kit and the registry already in it. Everything below is run from
the project root.

```bash
mkdir -p data tests
```

Nothing new is installed today; the environment day 1 built is the one this day runs on.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `data/ledger.json` | part 1.1 |
| `data/counts.json` | part 1.2 |
| `stock_desk/domain.py` | part 2.1 |
| `stock_desk/store.py` | part 2.2 |
| `tests/test_domain.py` | part 3.1 |

Every one of them is printed whole, at the path it goes to. You type them; nothing arrives
pre-built.

## §5 Build brief

Type the two fixture files first, then `domain.py`, then `store.py`, then the test file — in that
order, because each later file assumes the one before it exists. Commit as you go. Then the reps,
left unsolved on purpose and marked `TODO(me)` where they belong:

| File | What it must do |
| --- | --- |
| `stock_desk/domain.py` | `TODO(me)`: part 2.1's check yourself asks why `Outcome.OVER_COUNTED` exists when this project's own sixty counts never reach it. Write the sentence down. |
| `stock_desk/domain.py` | `TODO(me)`: part 3.2's rep. Find a fourth word that could be added to one of the three word lists without breaking any of the other eight notes, and explain why "safer today" is not the same claim as "safe". |
| `stock_desk/store.py` | `TODO(me)`: part 2.2's review comment. `write_reconciliation` fsyncs the file but not the directory. Decide whether this project needs that guarantee, and write down why or why not. |

## §6 The check that must be able to fail

```bash
./run check
```

Green is `All checks passed!`, `24 passed`, and day 0's five `ok` lines.

Ways to make it red, every one of them run today:

1. **Reorder the checks in `reconcile`** so the sign of the delta is asked about before the
   reason. `test_the_rules_reproduce_every_declared_outcome` fails on bin B-04-4, with
   `Outcome.REPLENISH` where `explained` was declared.
2. **Delete one of the nine planted variances** by turning bin C-18-2 back into a match.
   `test_nine_variances_are_planted` fails: `assert 52 == 51`.
3. **Widen `RECEIPT_WORDS` to catch A-10-2's note.** `test_the_keyword_scan_is_still_wrong_
   about_a_real_variance` fails — not because the scan started working, but because it started
   being wrong about a different bin: `assert 'A-10-2' in ['C-05-1']`.

And the one that is easy to miss: run only the test you are trying to fix after an edit like
break 3, and every other test in the file still passes. The full suite is what catches it.

## §7 Request budget

**Zero.** No model is called today. `reconcile` takes a reason as a given fact and decides nothing
about what the reason should be; `guess_reason_from_note` is a function nothing in this desk's own
decision path calls. The first model call in this project is day 8's.

What today fixes is the *shape* of the fact a model will eventually supply: one value, drawn from
three, given to `reconcile` as an argument rather than derived inside it — so the day a model
arrives, it replaces one function call and nothing about `reconcile` changes.

## §8 Traps

- **A dictionary will let you misspell a key and fail three functions away from the mistake.** A
  frozen dataclass built once, at `from_record`, fails at the point of the typo instead.
- **`bin` shadows a builtin, on purpose.** The warehouse's own word for the thing outranks a
  rarely-used function that turns an integer into a binary string.
- **Check the zero-delta case first.** A reason attached to a matched count is a reason for
  nothing, and checking it first would ask a pointless question of fifty-one counts a night.
- **Check "is there a reason" before the sign of the delta.** An accepted cause ends the question
  whichever direction the shelf disagreed; checking the sign first can misfile an explained
  shortfall as an unexplained one before the reason is ever looked at.
- **`None` rather than an exception, for a bin the ledger has never heard of.** A count against a
  bin that does not exist is an ordinary night, not a bug in this project.
- **The write goes to a temporary file in the same directory, never straight to the target.** A
  process killed mid-write leaves the old file, or the new one, never a half-written third thing.
- **`os.replace` is atomic only within one filesystem.** The temporary file has to be created in
  the target's own directory, or the final step stops being a rename and starts being a copy.
- **`except BaseException`, not `except Exception`, around the write.** A `KeyboardInterrupt`
  deserves the same cleanup as a `ValueError`.
- **A fixture-contract test checks the fixture, not the code.** `test_nine_variances_are_planted`
  would fail if a fixture were deleted even if `reconcile` were never touched.
- **A word list cannot become more correct, only differently wrong.** Widening it to catch a false
  negative can create a false positive somewhere the list is checked first.
- **Run the whole suite after a one-word fix, not just the test you were aiming at.** The test
  that would catch the new mistake is not the test you were looking at when you made it.

## §9 Verified today

Nothing was looked up live today. Every fact this day depends on — the file formats, the type
system, the atomic-write pattern — was established on day 1 or is a property of the standard
library checked by running it, not by reading documentation about it. The four commands under
"When it breaks" in parts 2.1 and 2.2, and the classification tables in part 3.2, are transcripts
from this machine, on this date.

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 02 | 2 | 2026-09-12 | The domain and its data | 6 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — new rows:

```text
| Type (domain) | A class that fixes what a value is allowed to be, so a typo in a field name fails at the one place a record is built rather than three functions later where the message is about something else. | P02 day 2 part 2.1 | a record type |
| Frozen dataclass | A record built once and never edited in place; a change to the truth goes through the store that owns the file, not through an attribute assignment on an object already in memory. | P02 day 2 part 2.1 | an immutable record |
| Given fact | A value a decision function receives as an argument rather than derives itself, because deriving it requires reading a sentence a person wrote — the one thing the function refuses to guess at until a model is wired in to supply it. | P02 day 2 part 2.1 | a supplied fact |
| Atomic write | A write that a reader either sees complete or does not see at all, achieved by writing to a temporary file in the target's own directory and renaming it over the target in one indivisible step. | P02 day 2 part 2.2 | a crash-safe write |
| Fixture contract | A test that asserts a number stated in a project's own brief, so a promise written in prose becomes something that goes red the moment the data it describes no longer matches it. | P02 day 2 part 3.1 | a promise, checked |
| Inverted case | A test that asserts a stand-in is still wrong, on a specific input, so nobody promotes it to a decision by accident and so its wrongness is caught the moment it moves rather than merely the moment it disappears. | P02 day 2 part 3.2 | a negative test |
```

**`docs/PINS.md`** — no row is owed. Nothing was installed today.

**`docs/SOURCES.md`** — no row is owed. Nothing with a citation identifier was cited.

**Commit:**

```text
P02 day 2: The domain and its data
```
