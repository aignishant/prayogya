---
project: "P02 Parts Counter"
day: 12
phase: P02
title: "P02 Parts Counter · 2 — Why the data goes behind a boundary, and what breaks when it does not"
ids: [MC-01]
kind: concept
deploy_tier: D2
plan_version: "v3.1.0"
parts: 4
files_printed:
  - "projects/02-parts-counter/parts_counter/data/parts.json"
  - "projects/02-parts-counter/parts_counter/store.py"
  - "projects/02-parts-counter/parts_counter/tools.py"
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** this project's own kit — the model registry, the key reader, the budget that
> refuses and the logger that redacts — and a green `run.py check` on a system that does nothing yet.
> **Today:** the counter's data and its four tools, printed whole, then broken on purpose by two
> writers at once — so that the boundary arriving on day 14 is something you asked for.
> **Tomorrow:** MCP 2026 and the stateless core — what a request has to carry when the thing
> answering it remembers nothing between calls.

## §1 The scene

A small workshop keeps its parts in a stockroom at the back, and the door has been propped open
since before anybody now working there was hired. It is not carelessness. Everyone is honest,
everyone knows everyone, and walking to the shelf yourself is quicker than finding somebody to fetch
for you. On the edge of each shelf there is a card with a number on it. You take what you need, cross
out the number, write the new one, and go back to work. For years this has been right every single
day.

Then one Friday the count is wrong. Nine spark plugs are gone from the shelf and still present in the
book, and nobody stole anything and nobody lied. Two people were at the same shelf within a few
seconds of each other. Both read the card, both took ten, both wrote down what they honestly believed
the new total to be, and only one of those numbers survived. Somebody else walked past mid-scribble
and read a card that said neither the old number nor the new one. And next Friday it is eight, and
the Friday after that it is ten, which is why nobody has ever been able to write a useful complaint
about it.

The fix is not better people. It is a hatch in the wall, a book on the counter beside it, and one
person whose job is both — and it costs somebody's whole day to staff, it puts a queue in the
corridor at half past eight, and every single request now takes longer than reaching for a shelf
yourself. Today is the argument for the hatch, made by living in the room without one. **Nothing is
built today.** The server arrives on day 14, and it arrives to a reader who already wants it.

## §2 The map

Two sections. The first is the shape you have: the data and the four functions that reach it,
printed whole and defended, because the code is genuinely good and the argument only works if that
is admitted first. The second is what the shape costs — one demonstration you can run yourself and
watch parts disappear, and then the argument assembled, with its price attached.

### 1 · The shape with no boundary

*The mental model: an open stockroom. Everyone walks in, everyone reads the card, everyone writes on
it, and every individual act is correct.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-shape-with-no-boundary/1.1-the-store-that-reaches-the-disk.md) | The store that reaches the disk | Where does the inventory actually live, and what exactly does changing one number do? | foundation |
| [1.2](parts/01-the-shape-with-no-boundary/1.2-four-tools-and-the-one-that-writes.md) | Four tools, and the one that writes | Why is the write different in kind from the three reads, and what does it leave behind? | working |

### 2 · What it costs

*The mental model: two people at the same shelf at the same moment — and then the hatch, the book,
and the person who owns both.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-what-it-costs/2.1-two-writers-and-a-half-written-file.md) | Two writers and a half-written file | What actually happens when two callers adjust the same file at once? | production |
| [2.2](parts/02-what-it-costs/2.2-the-five-things-a-boundary-buys.md) | The five things a boundary buys | What does one owner in front of the data give you, and what does it take? | production |

## §3 Setup — run this

Nothing new to install. This project's pins have not moved since day 11 and today adds no dependency,
no package and no file to the project. Every command below runs from `projects/02-parts-counter`,
was run on this machine today, and what it reported is in §9.

```bash
cd projects/02-parts-counter

# the kit day 11 left green — confirm it still is, before changing your reading of anything
uv run --frozen python run.py check

# part 1.1 — the store, read-only
uv run --frozen python -c "
from parts_counter import store
print(store.PARTS_FILE.name)
print(store.get('SPK-0055'))
print([p['part_no'] for p in store.all_parts()])
"

# part 1.2 — the three reads, then the driver's own subcommand
uv run --frozen python -c "
import json
from parts_counter import tools
print(json.dumps(tools.find_part('filter')))
print(json.dumps(tools.stock_level('BRK-0143')))
print(json.dumps(tools.bin_location('BLT-0310')))
"
uv run --frozen python run.py parts filter

# part 2.1 — the day's deliberate failure. Run it three times.
uv run --frozen python run.py race
uv run --frozen python run.py race
uv run --frozen python run.py race

# and confirm the fixture is exactly as it was
git status --porcelain parts_counter/data/parts.json
```

`--frozen` is on every `uv run` for the reason `PRIMER.md` §2 gives: plain `uv run` repairs the
lockfile before running your command, and a check invoked that way reports on a repository its own
invocation created. `run.py race` restores the inventory itself, and the last command is how you
confirm it rather than assume it.

## §4 Files this day prints

Three files, all of them this project's own, and all three of them new to the curriculum today.
`run.py` is **not** reprinted: day 11 printed it whole, and its `parts` and `race` subcommands appear
here only as marked diffs against that version, which is what the plan §5.1 rule 2 allows. Nothing
from `parts_counter/util/` is reprinted either — `models.py`, `keys.py`, `budget.py` and `logging.py`
were all printed whole by day 11, and part 1.2 says so where it imports one of them.

| File | Printed by |
| --- | --- |
| `projects/02-parts-counter/parts_counter/data/parts.json` | part 1.1, whole — the synthetic fixture |
| `projects/02-parts-counter/parts_counter/store.py` | part 1.1, whole, full depth |
| `projects/02-parts-counter/parts_counter/tools.py` | part 1.2, whole, full depth |
| `projects/02-parts-counter/run.py` — the `parts` subcommand | part 1.2, marked diff against day 11 |
| `projects/02-parts-counter/run.py` — the `race` subcommand | part 2.1, marked diff against day 11 |

Part 2.2 declares `prints: []` and that is correct rather than an omission. It is the day's argument,
assembled; it builds nothing, and inventing a fragment of day 14's server so that the part would have
something to print would be exactly the kind of scaffolding this curriculum refuses. The shape it
needs is drawn as a diagram, not printed as code.

## §5 Build brief

Nothing here creates a file. The project already contains everything today prints — day 11 built the
kit and this project's reference implementation carries the store and the tools — so today's reps are
about reading, predicting and breaking rather than typing. Leave every `TODO(me)` unsolved.

| File | What it must do |
| --- | --- |
| `parts_counter/store.py` | `TODO(me)`: read `adjust` and name, out loud, the two lines the window sits between. Then say what would have to be true about the rest of the program for the sequence between them to be safe, and whether anything in the file makes it true. |
| `parts_counter/store.py` | `TODO(me)`: `DATA_DIR` is built from `__file__`. Predict what happens if it is built from a relative path instead, then cause that error deliberately from one directory up — without editing the file — and read the message. |
| `parts_counter/tools.py` | `TODO(me)`: for each of the four tools, write down what its worst failure costs and whether the next question can undo it. Then say which of the four you would let a model call unsupervised. |
| `parts_counter/tools.py` | `TODO(me)`: call `adjust_stock` with a string delta and read the traceback. Say which line raised it, which line **should** have caught it, and why the inventory was untouched. |
| `run.py race` | `TODO(me)`: predict `parts unaccounted` before the first run. Run it three times, record all three numbers, and say what those three numbers do to a bug report. |
| `run.py race` | `TODO(me)`: add a `time.sleep(0.002)` in `store.adjust` immediately after `payload = _read()`, run `race` twice, and say what changed and what did not. **Remove it afterwards and confirm `git status --porcelain` is empty.** |
| the argument | `TODO(me)`: write the five things a boundary buys in your own words, each with the transcript that made you want it, then write the four costs. Bring the list to day 14 and check it against what the server actually gives you. |

## §6 The check that must be able to fail

```text
cd projects/02-parts-counter
uv run --frozen python run.py check    # six green, 0 problem(s), exit 0
echo $?
uv run --frozen python run.py race     # the day's deliberate failure — parts vanish
git status --porcelain                 # must be empty: the demonstration restores itself
cd ../.. && python p.py depth 12       # this day against the plan §5 contract
```

**How to make it go red on purpose — and the first one is the day's real failure.**

The first is `run.py race` itself, and it is unusual in that it does not go red — it goes *wrong*,
quietly, which is the entire lesson. Twenty spark plugs are issued and the count moves by eight, or
nine, or ten. No exception is raised for the missing ones, nothing is logged, and no check in this
project turns red. Watch it, then watch it again and get a different number, and then say out loud
what a bug report about it would look like.

The second is the crash hiding inside the same run. `reads that crashed` is not always empty:
somewhere in those twenty adjustments a read lands while the other thread has truncated the file, and
`json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)` comes back about a file
that is perfectly valid by the time you open it.

The third makes the project's own gate go red, so that you have seen it refuse: break the model pin
by editing `parts_counter/util/models.py`'s answering model to `gemini-flash-latest` and run
`run.py check`. The `model` check refuses an alias by name. Put it back.

The fourth is for the document rather than the code: delete a `## In production` heading from any
part and run `python p.py depth 12`. It names the file and the missing section.

## §7 Request budget

**Zero model calls. Not "few" — zero.**

Every transcript in this day runs the store and the tools **directly, with no model anywhere in the
path**: `python -c` imports, and the driver's `parts` and `race` subcommands. There is no agent in
this project yet — `parts_counter/agent.py` is owed by day 17, once there is a boundary for it to
reach through — so there is nothing today that could make a request even by accident.

That matters for reading part 1.2 correctly. The docstrings there are written for a model, and the
tool declarations ADK would derive from them are real, but nothing in this day hands them to one. The
asymmetry between a read tool and a write tool is a property of the tools, and it is demonstrated
without a provider being involved at all.

The plan §9 counts requests **across the whole cast**, and from day 17 this project's number stops
being zero. The provider's own ceiling is not stated here and is not stated anywhere in this project:
the rate-limit page directs you to Google AI Studio rather than publishing a number, so
`PACKAGES.md` carries `TODO(me): read this project's live limits in Google AI Studio and paste them
here, with the date.` A number nobody can verify is worse than an honest gap.

## §8 Traps

- **Read-modify-write assumes one writer, and never says so.** `adjust` loads the whole document,
  changes one value and writes the whole document back. Nothing in the file records that assumption,
  so the person who adds a second worker cannot see it.
- **`write_text` truncates before it writes.** There is a moment when the file on disk is empty. Any
  reader that arrives in it gets `''`, and `json.loads('')` raises.
- **`Expecting value: line 1 column 1 (char 0)` means the file was empty**, not corrupt. People open
  the file, find it valid, and conclude the error is impossible.
- **The count being wrong raises nothing.** A lost update is silent by construction: both writes
  succeeded and both were honest. The only evidence is a total that disagrees with reality.
- **The number is different every run.** Ten, then eight, then nine. Any document — including a bug
  report — that quotes one number as *the* answer is describing a run, not the bug.
- **A `threading.Lock` fixes this demonstration completely and fixes almost nothing.** The
  demonstration uses threads because threads are easy to run. Two processes have no shared lock, and
  two containers have no shared memory to put one in.
- **An atomic replace fixes the torn read and returns no lost part.** The two failures have two
  separate windows; quieting one tells you nothing about the other.
- **Starting and joining the threads one at a time makes the race disappear.** `left.start();
  left.join(); right.start()` runs them in sequence and produces a perfect count — the commonest way
  this demonstration is written wrongly.
- **`Path("data/parts.json")` resolves against the working directory.** It works from inside the
  project and fails from anywhere else with a `FileNotFoundError` naming a path nobody wrote.
  `Path(__file__).with_name(...)` does not care where you were standing.
- **A type hint is a description, not a guard.** `delta: int` shapes the schema the model is given
  and checks nothing at runtime; a string `"-1"` gets all the way to the arithmetic in `store.py`,
  which is three frames from where it should have been rejected.
- **The tool's error dictionary is not an exception, on purpose** — and `store.get`'s exception is
  not an error dictionary, also on purpose. A tool returns facts the model can act on; a store raises
  so that a caller cannot ignore it.
- **stderr and stdout arrive out of order.** The log record of a write and the answer returned to the
  caller travel by different streams, and in a terminal you see all the records and then all the
  answers.
- **A record on stderr is not an audit trail.** It has no identity in it, no second reader, and no
  life after the terminal scrolls.
- **`uv run` without `--frozen` repairs the lockfile before your command runs.** Every command in
  this day carries the flag; `PRIMER.md` §2 says why.
- **Do not quote an MCP specification revision today.** It has not been looked up. `PACKAGES.md`
  carries the `TODO(me)` and it is owed before day 13 prints anything.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| The kit is still green | `uv run --frozen python run.py check` | 2026-09-10 | six green — keys, interpreter, pins, lock, model, tests — `0 problem(s)`, exit `0` |
| The store answers from any directory | `store.PARTS_FILE.name`, `store.get('SPK-0055')`, `store.all_parts()` | 2026-09-10 | `parts.json`, on hand `240`, six part numbers in file order |
| One adjustment is three whole-file operations | `Path.read_text` / `Path.write_text` wrapped, `tools.adjust_stock` twice | 2026-09-10 | `['read', 'read', 'write', 'read', 'read', 'write']` — `store.get` then `store.adjust` |
| A store-level adjustment is read then write | the same instrumentation, `store.adjust` twice | 2026-09-10 | `['read', 'write', 'read', 'write']`, and **1161 bytes** rewritten to change one integer |
| A relative data path fails from one directory up | `json.loads(Path('parts_counter/data/parts.json').read_text(...))` from the repository root | 2026-09-10 | `FileNotFoundError: [Errno 2] No such file or directory: 'parts_counter\\data\\parts.json'` |
| The three read tools answer | `tools.find_part('filter')`, `stock_level('BRK-0143')`, `bin_location('BLT-0310')` | 2026-09-10 | two hits matched on name not number; `below_reorder: true` at 4 against 6; bin `C-07-2` |
| The driver's `parts` subcommand | `uv run --frozen python run.py parts filter` | 2026-09-10 | the same two hits, indented — driver → tool → store, no model in the path |
| The write leaves one line on stderr | `tools.adjust_stock('BLT-0310', 2)` then `-2` | 2026-09-09 | two `stock.adjusted` records on stderr, two results on stdout, **arriving out of order**; no identity in either record |
| A string delta reaches the arithmetic | `tools.adjust_stock('BLT-0310', '-1')` | 2026-09-10 | `TypeError: unsupported operand type(s) for +: 'int' and 'str'`, raised in `store.adjust` before any write |
| Two writers lose parts | `uv run --frozen python run.py race`, four runs | 2026-09-09 / 2026-09-10 | 10, 8, 9 and 9 parts unaccounted for out of 20 issued; 2, 2, 1 and 3 crashed reads |
| The crashed read is a torn read | the traceback from the same demonstration | 2026-09-09 | `json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)` at `_read`, from a file `write_text` had truncated |
| The two failures have separate windows | `time.sleep(0.002)` after `payload = _read()` in `store.adjust`, two runs, then removed | 2026-09-10 | 9 lost both times and **zero** crashed reads both times — the loss unchanged, the tear gone |
| The inventory is not reachable from outside | `python -c "from parts_counter import store"` from the repository root | 2026-09-10 | `ModuleNotFoundError: No module named 'parts_counter'` |
| The gate can still refuse | `models.require_pinned('gemini-flash-latest')` | 2026-09-10 | `UnpinnedModel: 'gemini-flash-latest' is an alias, not a pin.` — day 11's `model` check goes red on an alias, checked rather than assumed before §6 tells you to break it |
| The blast radius, counted | `find . -type f` under the repository root, `.git` excluded | 2026-09-10 | **10,442** files the process can open, against the **one** file the tools need |
| The fixture survives every transcript | `diff` against a copy taken before the day's first command, then `git status --porcelain projects/` | 2026-09-10 | `parts.json` byte-identical, `projects/` clean — every run restored what it moved |

## §10 Ledger & commit

**`docs/PROGRESS.md`:**

```text
| 12 | 2026-09-10 | MC-01 | 4 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the terms this day defined for the first time:

```text
| Read-modify-write | Editing stored data by loading all of it, changing part of the loaded copy, and writing all of it back. Correct while exactly one writer exists, and it never says so anywhere. | day 12 part 1.1 | load-edit-save |
| Audit trail | A durable, ordered record of every change, kept where a reader other than the writer can get at it. A line on one process's standard error is not one. | day 12 part 1.2 | the log, the record |
| Lost update | Two callers read the same value, both compute a new one from it, and the second write erases the first. Nothing errors and nothing is logged; the only evidence is a total that disagrees with reality. | day 12 part 2.1 | write-write conflict |
| Torn read | A read that lands while a write is in progress and returns neither the old contents nor the new. Writing a file truncates it first, so the value returned is often nothing at all. | day 12 part 2.1 | a dirty read, reading mid-write |
| Data boundary | A process that owns the data and is the only thing that touches it; everything else asks it. It buys one writer, a readable record, reuse, containment and a home for policy, and it costs a process, a protocol, a failure mode and latency. | day 12 part 2.2 | the boundary, the owner |
| Blast radius | How much a failure or a misuse can reach. For a tool it is not the data it was written for but everything the process it runs in can open. | day 12 part 2.2 | reachable surface, containment |
```

**`docs/PINS.md`** — nothing to add. This day installs nothing, adds no dependency and moves no
version; the pins day 11 recorded in this project's `PACKAGES.md` are unchanged and were re-confirmed
only by `run.py check` passing its `pins` and `lock` checks.

**`docs/SOURCES.md`** — nothing to add. This day cites no external record. The one external fact it
would need — the current MCP specification revision — was deliberately **not** looked up and not
stated, and `projects/02-parts-counter/PACKAGES.md` carries the `TODO(me)` naming the page, owed
before day 13.

**Commit:**

```text
day 12: P02 Parts Counter · 2 — Why the data goes behind a boundary, and what breaks when it does not — closes MC-01
```
