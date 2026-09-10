---
project: "P02 Parts Counter"
day: 14
phase: P02
title: "P02 Parts Counter · 4 — The server skeleton and its first tool"
ids: [MC-03]
kind: mechanism
deploy_tier: D2
plan_version: "v3.1.0"
parts: 4
files_printed:
  - "projects/02-parts-counter/parts_mcp/store.py"
  - "projects/02-parts-counter/tests/test_boundary.py"
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** MCP's stateless core, and the reframe from a phone call to a web request — plus
> `parts_mcp/server.py` printed whole, the file this day's tools live in.
> **Today:** the hatch is open. The inventory changes owner, one lock and one atomic write pay off
> day 12's two failures, four ordinary Python functions become four declared tools, and the
> boundary's two regression tests go red on purpose.
> **Tomorrow:** the lifecycle — what has to be agreed before anything may be asked, and the
> specification revision that deleted the whole ceremony.

## §1 The scene

Day 12 left you in a workshop with the stockroom door propped open, and left it open on purpose. It
is the same building today. The door is bricked up and there is a hatch in the wall where it used to
be — a shelf at chest height, a counter on the far side, one storeman behind it, and a book at their
elbow.

Everything about that is worse for you personally. You do not walk in and take a box any more. You
wait. There is a queue at half past eight. What you get in exchange is the one thing the shop was
losing every Friday: the book is right. Not right most of the time — right, because one pair of
hands writes in it and that pair is never writing two entries at once. And the storeman does not
scribble over the old number while you watch; they write a clean page at their elbow and swap it
into the book in one movement, so anybody glancing at the book sees the old page or the new page,
never a page halfway through being changed.

Above the hatch there is a sign with four services on it, and nobody wrote that sign separately.
Somebody watched the storeman work and wrote down what they actually do. That is the whole shape of
today: the file changes owner, the four things you may ask for are declared by writing four ordinary
functions, what crosses the counter in each direction has a fixed form — a docket going out, a tray
coming back — and then you take the lock away yourself and watch ten spark plugs go missing again,
this time with something red to say so.

## §2 The map

Two sections. The first is the move — the file's new owner and the four functions on the far side of
the wall. The second is what actually crosses the counter, in both directions, and what happens when
the answer is no.

### 1 · The move

*The mental model: the door is bricked up and a hatch is cut in its place. One storeman, one book,
and a sign that was written by watching them rather than by anybody's imagination.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-move/1.1-the-file-changes-owner.md) | The file changes owner | What did moving the store behind a boundary actually buy, and why could neither fix have been made before the move? | foundation |
| [1.2](parts/01-the-move/1.2-four-tools-on-the-far-side.md) | Four tools on the far side | How does an ordinary Python function become something a model across a process line can ask for? | working |

### 2 · What the wire carries

*The mental model: the printed docket that goes out, and the tray the answer comes back on — with a
stamp saying whether it went through.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-what-the-wire-carries/2.1-the-tool-object-and-the-envelope.md) | The Tool object, and the envelope its answer travels in | What exactly does a client receive for one tool, and what shape does its return value come back in? | working |
| [2.2](parts/02-what-the-wire-carries/2.2-the-error-the-model-can-fix.md) | The error the model can fix | What are the two ways to say no, which one is a model told about, and what stops day 12's failures coming back? | production |

## §3 Setup — run this

Nothing new to install. This project's pins have not moved since day 11, and today adds no
dependency and no package. What today adds is a folder and a test file, and what it removes is two
modules.

The move itself, for the record. This project's reference implementation already carries it, so read
these as the diff rather than as something to type into a repository that has already done it:

```bash
cd projects/02-parts-counter

# the boundary's own package, and the inventory moving into it
mkdir -p parts_mcp/data
touch parts_mcp/__init__.py
git mv parts_counter/data/parts.json parts_mcp/data/parts.json
git mv parts_counter/store.py parts_mcp/store.py

# the two modules that have no reason to exist once the boundary owns the data
git rm parts_counter/tools.py
```

Then everything today actually runs. Every command is from `projects/02-parts-counter`, was run on
this machine today, and what it reported is in §9:

```bash
cd projects/02-parts-counter

# the kit and the boundary, both green, before you touch anything
uv run --frozen python run.py check
uv run --frozen python -m pytest tests -q

# part 1.1 — day 12's race, re-run against the store the boundary owns. Three times.
uv run --frozen python run.py race
uv run --frozen python run.py race
uv run --frozen python run.py race

# part 1.1 — what the two fixes cost, measured
uv run --frozen python -c "
import time, warnings; warnings.filterwarnings('ignore')
from parts_mcp import store
n = 50
t0 = time.perf_counter()
for _ in range(n):
    store.all_parts()
t1 = time.perf_counter()
for _ in range(n):
    store.adjust('BLT-0310', 1); store.adjust('BLT-0310', -1)
t2 = time.perf_counter()
print(f'{n} reads under the lock      : {(t1-t0)*1000/n:.2f} ms each')
print(f'{n*2} writes, temp+fsync+replace: {(t2-t1)*1000/(n*2):.2f} ms each')
print('belt kit back to            :', store.get('BLT-0310')['on_hand'])
"

# parts 1.2 and 2.1 — the four tools, and one whole Tool object
uv run --frozen python -c "
import asyncio, json, warnings; warnings.filterwarnings('ignore')
from parts_mcp.server import mcp
async def main():
    tools = await mcp.list_tools()
    for t in tools:
        print(f'{t.name:16} {t.description[:52]!r}')
    print(json.dumps(tools[0].model_dump(exclude_none=True), indent=2))
asyncio.run(main())
"

# part 2.2 — the two error classes, from this server
uv run --frozen python -c "
import asyncio, json, warnings; warnings.filterwarnings('ignore')
from parts_mcp.server import mcp
async def main():
    print(json.dumps((await mcp.call_tool('stock_level', {'part_no':'NOPE-0000'}))[1], indent=2))
    await mcp.call_tool('stock_levl', {'part_no':'BRK-0143'})
asyncio.run(main())
"

# and confirm the fixture is exactly as it was
git status --porcelain parts_mcp/
```

`--frozen` is on every `uv run` for the reason `PRIMER.md` §2 gives: plain `uv run` repairs the
lockfile before running your command, and a check invoked that way reports on a repository its own
invocation created.

## §4 Files this day prints

Two files, both of them this project's own, and both new to the curriculum today.

| File | Printed by |
| --- | --- |
| `projects/02-parts-counter/parts_mcp/store.py` | part 1.1, whole, full depth |
| `projects/02-parts-counter/tests/test_boundary.py` | part 2.2, whole, full depth |

Three things are deliberately **not** reprinted, and each is a rule rather than an omission.

`parts_mcp/server.py` was printed whole by **day 13**, at
`days/02-parts-counter/day-13-mcp-stateless-core/`. Part 1.2 quotes its four tool regions as marked
regions of that file — `# ── unchanged from day 13 ──` — which is what the plan §5.1 rule 2 allows,
and prints nothing else of it. `parts_mcp/data/parts.json` is the fixture **day 12** printed whole,
at a new path; a file printed twice in one project is a bug. And `parts_counter/util/mcp.py`, which
holds the other end of the wire in part 2.1's transcript, belongs to **day 17** and is printed there.

`parts_mcp/__init__.py` is empty and is created by §3 above. Parts 1.2 and 2.1 declare `prints: []`
and that is correct: 1.2's subject is four regions of a file another day printed, and 2.1's subject
is two structures the protocol defines, neither of which is a file in this repository.

`CODEMAP.md` records the two deletions — `parts_counter/store.py` and `parts_counter/tools.py` — and
the data file's new path, so that a line of this project that stopped existing says so rather than
falling quietly off the list.

## §5 Build brief

The project already contains everything today prints, so today's reps are reading, predicting,
measuring and breaking rather than typing. Leave every `TODO(me)` unsolved.

| File | What it must do |
| --- | --- |
| `parts_mcp/store.py` | `TODO(me)`: name the two lines the critical section in `adjust` now spans. Then say, out loud, which of day 12's two failures the lock fixes and which one `_write_atomically` fixes, and which of them would still happen if you kept only one. |
| `parts_mcp/store.py` | `TODO(me)`: `_replace_with_retry` and `_LOCK` fix different causes. Write down, in one sentence each, who the lock excludes and who the retry survives — and then name one interferer that neither of them can do anything about. |
| `parts_mcp/store.py` | `TODO(me)`: change `tempfile.mkstemp(dir=DATA_DIR, ...)` to `tempfile.mkstemp()` with no `dir`, predict what changes, then run `run.py race` and see whether you were right. Put it back and confirm `git status --porcelain` is empty. |
| `parts_mcp/server.py` | `TODO(me)`: remove the parentheses from one `@mcp.tool()`, import the module, read the `TypeError` in full, and say which line of the traceback tells you the failure happened at import rather than at call time. Put them back. |
| `parts_mcp/server.py` | `TODO(me)`: for each of the four tools, write down every field of its declaration a model receives and which line of the source produced it. Then say where a note about `delta` being negative for issuing stock would have to live, and why there is nowhere else. |
| the `Tool` object | `TODO(me)`: print all four declarations. List the fields that come back `null`, and for each one write the change to the source that would fill it in. Say which of them you would insist on before letting a model call `adjust_stock`. |
| `tests/test_boundary.py` | `TODO(me)`: remove the `with _LOCK:` from `store.adjust`, run only `test_two_writers_lose_nothing`, and record the number in the assertion. Run it twice more and record those too. Restore, and confirm fourteen green. |
| `tests/test_boundary.py` | `TODO(me)`: `test_a_reader_never_sees_a_half_written_file` hangs rather than fails if the writer thread dies. Write down the change that would make it go red instead — you do not have to make it, but you have to be able to say it. |
| the argument | `TODO(me)`: this server reports an unknown part as `{"error": ...}` inside a result with `isError: false`. Write the case for that choice and the case against it, then say which you would ship and what you would put in `PROJECT.md` either way. |

## §6 The check that must be able to fail

```text
cd projects/02-parts-counter
uv run --frozen python run.py check    # six green, 0 problem(s), exit 0
echo $?
uv run --frozen python -m pytest tests -q            # 14 passed
uv run --frozen python run.py race                   # 0 unaccounted, no crashed reads
git status --porcelain                               # must be empty
cd ../.. && python p.py depth 14                     # this day against the plan §5 contract
```

**How to make it go red on purpose — and the first one is the day's deliberate failure.**

The first is the lock. Open `parts_mcp/store.py`, delete the `with _LOCK:` line from `adjust` and
unindent its body, then run `uv run --frozen python -m pytest
tests/test_boundary.py::test_two_writers_lose_nothing -q`. It fails on `assert 230 == (240 - 20)` —
ten spark plugs, day 12's exact number, now with something red to say so. Note that `errors == []`
still passes: one fix removed, one failure back, the other still held. Restore the line, re-indent,
and confirm fourteen green.

Run **only** that test while the lock is out. Two neighbouring edits do not work as a break and both
were checked rather than assumed: swapping `RLock` for `Lock` leaves all five green, and removing the
lock from `all_parts()` instead makes the reader test **hang** rather than fail. Part 2.2 says why.

The second is the decorator. Remove the parentheses from one `@mcp.tool()` and import the module:
`TypeError: The @tool decorator was used incorrectly. Did you forget to call it? Use @tool() instead
of @tool`. It refuses at import, which is the good case.

The third is the schema. Tighten `stock_level`'s return annotation to a five-key `TypedDict` and call
it with `NOPE-0000`. The tool runs, the store is fine, and the SDK rejects the answer on the way out
with five validation errors. Restore the annotation.

The fourth is for the documents rather than the code: delete an `## In production` heading from any
part and run `python p.py depth 14`. It names the file and the missing section.

## §7 Request budget

**Zero model calls. Not "few" — zero.**

Every transcript in this day runs the store, the server and its tools **directly, with no model
anywhere in the path**: `python -c` imports, `mcp.list_tools()`, `mcp.call_tool(...)`, the driver's
`race` subcommand, and pytest. Part 2.1's envelope transcript crosses a real process line over stdio
and still involves no provider, because a client fetching and calling tools is not a model doing
anything. There is no agent in this project yet — `parts_counter/agent.py` is owed by day 17 — so
there is nothing today that could make a request even by accident.

The plan §9 counts requests **across the whole cast**, and from day 17 this project's number stops
being zero. The provider's own ceiling is not stated here and is not stated anywhere in this
project: the rate-limit page directs you to Google AI Studio rather than publishing a number, so
`PACKAGES.md` carries `TODO(me): read this project's live limits in Google AI Studio and paste them
here, with the date.` A number nobody can verify is worse than an honest gap.

## §8 Traps

- **`@mcp.tool` and `@mcp.tool()` are different things.** The first hands your function to a method
  as an argument; only the second is a decorator. The SDK refuses at import and names the fix in the
  message, which is the only reason this costs a minute rather than an evening.
- **The temporary file must be in the same directory as the target.** `os.replace` is atomic only
  within one filesystem, and the system temporary directory is very often on another one. A rename
  across filesystems is a copy and a delete, which has a middle — and a middle is exactly what you
  are paying to remove.
- **`os.fsync` is not the same as closing the file.** Without it the rename can be durable while the
  bytes behind it are not, and a power cut leaves a valid filename over an empty file — day 12's torn
  read, arriving later.
- **The lock and the rename retry fix different causes.** The lock excludes our own threads; the
  retry survives another process holding the file open — a sync client, an indexer, a backup agent —
  which no lock of ours can exclude. Quieting one tells you nothing about the other.
- **`PermissionError: [WinError 5] Access is denied` from `os.replace` is usually not a permissions
  problem.** On Windows the call fails if any handle is open on the destination. People spend an
  evening on file ACLs before finding that out.
- **Readers have to hold the lock too.** An unguarded read does not merely see stale data here; it
  keeps a handle open on the file the writer is about to replace, and makes the *writer* fail.
- **`RLock` is guarding an edit that has not happened yet.** Nothing in the module re-enters the lock
  today — `adjust` calls the private `_read`, not the public `all_parts` — so swapping it for `Lock`
  leaves the tests green. Keep the `RLock`; do not believe a comment that says it is load-bearing
  right now.
- **A test that hangs is not a test that failed.** `test_a_reader_never_sees_a_half_written_file`
  loops for ever if its writer thread dies, because `stop.set()` never runs. That is why the day's
  break names one specific line.
- **`left.start(); left.join(); right.start()` makes the concurrency test pass against a completely
  unlocked store.** Both threads start before either is joined, or the test proves nothing.
- **The tool name on the wire is `__name__`.** Renaming the function is a public interface change
  wearing the clothes of a tidy-up, and it breaks every client with the old name saved.
- **The docstring is the description, all of it.** The blank line, the second paragraph and the
  trailing indentation all reach the model. Reflowing a docstring is editing an interface.
- **A derived declaration cannot carry a per-argument description.** There is no property
  `description` and nowhere for one to come from, so guidance about an argument goes in the
  docstring or nowhere.
- **`-> dict[str, Any]` derives an `outputSchema` that promises nothing** —
  `{"type": "object", "additionalProperties": true}`. Tighten it and you must include the error
  branch, or the tool starts failing only for inputs that do not exist.
- **`isError: false` does not mean the tool was happy.** This server returns an `error` key inside a
  perfectly successful result. A client branching on `isError` sees every call succeed.
- **Do not print a `2026-07-28` message shape as runnable here.** `resultType`, `ttlMs`, `_meta`
  protocol versions and `server/discover` are the current revision's shapes and this stack cannot
  produce them. ADR-0005 is the record of why.
- **`uv run` without `--frozen` repairs the lockfile before your command runs.** Every command in
  this day carries the flag.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| The whole suite is green | `uv run --frozen python -m pytest tests -q` | 2026-09-10 | `14 passed` — nine kit tests from day 11, five boundary tests from today |
| The project gate is green | `uv run --frozen python run.py check` | 2026-09-10 | six green — keys, interpreter, pins, lock, model, tests — `0 problem(s)`, exit `0` |
| The race is over | `uv run --frozen python run.py race`, three runs | 2026-09-10 | `parts unaccounted : 0` and `reads that crashed : []` every time, against day 12's 10, 8, 9 and 9 lost |
| …and at double the contention | the same, forty issues per thread, three runs | 2026-09-10 | `expected 160, actual 160, lost 0, errors []` each time |
| What the fixes cost | fifty reads and one hundred writes, timed | 2026-09-10 | **0.10 ms** per read under the lock, **2.48 ms** per write with temp file, `fsync` and rename; **1161** bytes rewritten per write |
| The lock is not re-entered today | `_LOCK = threading.Lock()`, then the boundary tests, then restored | 2026-09-10 | `5 passed` — `RLock` is insurance for the next edit, not a fix for anything current |
| Day 12's lost update, pinned | `with _LOCK:` removed from `adjust`, then `pytest tests/test_boundary.py::test_two_writers_lose_nothing -q` | 2026-09-10 | `E assert 230 == (240 - 20)` — ten lost, `errors == []` still passing; restored, fourteen green |
| Removing the lock from `all_parts` instead | the same file, the reader test | 2026-09-10 | the suite **hangs** rather than fails: the writer dies on `PermissionError`, `stop.set()` never runs, the reader loops for ever |
| The decorator needs its parentheses | `@mcp.tool` on `find_part`, then `python -c "from parts_mcp.server import mcp"` | 2026-09-10 | `TypeError: The @tool decorator was used incorrectly. Did you forget to call it? Use @tool() instead of @tool`, raised at `server.py` line 33, at import |
| Four tools, and their descriptions | `await mcp.list_tools()` | 2026-09-10 | `find_part`, `stock_level`, `bin_location`, `adjust_stock` in declaration order, each description the function's docstring |
| One whole `Tool` object | `t.model_dump(exclude_none=True)` for `find_part` | 2026-09-10 | `inputSchema` `{"query": {"type": "string"}}` with `required: ["query"]`; `outputSchema` `{"type": "object", "additionalProperties": true}` |
| Which fields this SDK emits | `list(mcp.types.Tool.model_fields)` and a dump with nothing excluded | 2026-09-10 | nine declared fields; `name`, `description`, `inputSchema`, `outputSchema` filled from the function, and `title`, `icons`, `annotations`, `meta`, `execution` all `null` |
| The description carries the whole docstring | the same dump, `adjust_stock` | 2026-09-10 | the blank line, the second paragraph and the trailing indentation are all present as literal `\n` and spaces |
| Arguments are validated against the derived schema | `mcp.call_tool('adjust_stock', {'delta': 'two'})` and with `delta` missing | 2026-09-10 | `Input should be a valid integer, unable to parse string as an integer` and `Field required` — both before the function body runs; `'2'` is coerced and goes through |
| An unknown part is an answer, not an exception | `mcp.call_tool('stock_level', {'part_no': 'NOPE-0000'})` | 2026-09-10 | a normal result carrying `{"error": "no part numbered 'NOPE-0000'", "known": [six part numbers]}` |
| An unknown tool is not | `mcp.call_tool('stock_levl', ...)` | 2026-09-10 | `mcp.server.fastmcp.exceptions.ToolError: Unknown tool: stock_levl` |
| A tightened `outputSchema` is enforced | `stock_level` annotated with a five-key `TypedDict`, called with `NOPE-0000`, then restored | 2026-09-10 | the good part answers; the error branch fails with `5 validation errors for StockLevel`, raised after the tool ran |
| Tool object fields, in the specification | `https://modelcontextprotocol.io/specification/2026-07-28/server/tools` | 2026-09-10 | `name`, `title`, `description`, `icons`, `inputSchema`, `outputSchema`, `annotations` |
| The two error classes, in the specification | the same page | 2026-09-10 | protocol errors versus tool execution errors, and clients **MAY** give the first to a model but **SHOULD** give the second |
| The fixture survives every transcript | `git status --porcelain projects/02-parts-counter/parts_mcp/` after each run | 2026-09-10 | empty — `parts.json` byte-identical, every demonstration restored what it moved |

## §10 Ledger & commit

**`docs/PROGRESS.md`:**

```text
| 14 | 2026-09-10 | MC-03 | 4 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the terms this day defined for the first time:

```text
| Atomic replace | Making a change visible in one indivisible step: write the new contents to a temporary file in the same directory, force them to disk, then move that file over the target. A reader sees the old contents or the new ones and never the gap. Only atomic within one filesystem, which is why the temporary file's directory matters. | day 14 part 1.1 | atomic rename, write-and-swap |
| Tool object | The protocol's structure for one declared tool — a name, an optional title, a description, an input schema, an optional output schema, optional icons and optional behavioural annotations. Everything a client and a model know about a tool, and here every filled-in field is derived from the Python function. | day 14 part 2.1 | the tool declaration, the docket |
| Tool result envelope | The structure a tool's answer arrives in: a list of typed content blocks, an optional structured copy of the same value, and a flag saying whether the call failed. Your function returns a value; the envelope is added around it on the way out. | day 14 part 2.1 | the tool result, `CallToolResult` |
| Protocol error | A failure of the request itself — an unknown tool, a request the server cannot parse — reported as a JSON-RPC error rather than as a result. The specification says a client **may** show one to a model, because a model is unlikely to be able to fix it. | day 14 part 2.2 | a transport-level error, a JSON-RPC error |
| Tool execution error | A tool that ran and failed, reported inside a normal result with `isError: true`. The specification says a client **should** hand these to the model, because they carry feedback it can act on. | day 14 part 2.2 | a recoverable tool failure |
```

**`docs/SOURCES.md`** — one row, if day 13 has not already added it. Both quotations in parts 2.1
and 2.2 come from the same page of the same revision, opened live today:

```text
| spec:mcp-2026-07-28 | Model Context Protocol specification, revision 2026-07-28 | 2026 | https://modelcontextprotocol.io/specification/2026-07-28/server/tools | 2026-09-10 | day 13 | day 14 parts 2.1, 2.2 |
```

**`docs/PINS.md`** — nothing to add. This day installs nothing and moves no version; the pins day 11
recorded in this project's `PACKAGES.md` are unchanged and were re-confirmed only by `run.py check`
passing its `pins` and `lock` checks.

**`projects/02-parts-counter/CODEMAP.md`** — the row for `parts_mcp/server.py` must say **day 13**,
which is the day that prints it whole. Today owns `parts_mcp/store.py`, `parts_mcp/data/parts.json`
at its new path, `parts_mcp/__init__.py` and `tests/test_boundary.py`, and records the deletion of
`parts_counter/store.py` and `parts_counter/tools.py`.

**Commit:**

```text
day 14: P02 Parts Counter · 4 — The server skeleton and its first tool — closes MC-03
```
