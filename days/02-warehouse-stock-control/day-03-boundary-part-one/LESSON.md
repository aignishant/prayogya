---
project: "P02"
day: 3
title: "The boundary, part one"
spine: 3
kind: mechanism
deploy_tier: D3
plan_version: "v4.1.0"
parts: 5
files_printed: [stock_mcp/__init__.py, stock_mcp/server.py, stock_mcp/__main__.py, tests/test_boundary.py]
generated: "2026-09-12"
status: written
commit: ""
---

> **Yesterday:** sixty invented bins, sixty invented cycle counts with their answers written by
> hand, the records as types, and one class — `Store` — allowed to open a file.
> **Today:** that class moves to the far side of a process line. The desk stops holding data and
> starts asking for it, across a real protocol, through one declared tool.
> **Tomorrow:** what a second writer does to this same ledger when nobody has told it about the
> first one.

## §1 The scene

A cycle-count cage at a distribution centre has a wire mesh gate and a scanner mounted beside it.
You do not walk in and pull stock off the racking to check a number — you scan the bin label, the
terminal on the wall tells you what the ledger thinks is there, and you write down what you
actually see. If you want a different bin's number, you scan again.

Yesterday's `Store` was a terminal by agreement. Nothing stopped the next module importing `json`
and `pathlib` and reading the ledger file directly, and agreements hold until a deadline. Today the
agreement becomes a wall, and the first thing this day does is measure what the wall is worth:
**forty-five files** are reachable by a tool-shaped function in the desk's process right now,
`.env` among them.

So the ledger moves into `stock_mcp/`, a second top-level package that runs as its own program. It
declares one tool. The tool's own signature and docstring become the entire interface — nobody
writes a schema, and nothing but cover crosses the line: no path, no filename, no `_synthetic`
marker. A client launches `python -m stock_mcp`, asks a question down the process's standard input,
and gets a bin back.

That last sentence carries the day's trap in it. On this transport the protocol **is** the child's
standard output, so a single `print` in a tool is a message on the wire. The last part causes
exactly that, and the result is the uncomfortable one: the client logs a parse failure, skips the
line, answers correctly, **all thirty tests still pass**, and — on this machine, today — even the
suite's timing does not give the corruption away.

## §2 The map

Three sections. **Section 1 is the argument** — what the desk can reach today, as a number, and why
that is the thing a boundary changes. **Section 2 is the server** — one object, one tool, and the
four lines that make it a program. **Section 3 is the line itself** — what is allowed to cross it,
and what happens when something else does.

### 1 · Why a boundary — the number, not the principle

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-why-a-boundary/1.1-the-counter-and-the-cage.md) | The counter and the cage | What can a tool in this process actually reach, and why does that change everything? | foundation |

### 2 · The server — the docket, and the program behind it

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-server/2.1-server-and-the-tool-it-declares.md) | The server, and the tool it declares | How does a function become an interface a model can read? | working |
| [2.2](parts/02-the-server/2.2-run-it-as-a-process.md) | Run it as a process | How does a client launch the boundary and get an answer out of it? | working |

### 3 · The line — what may cross, and what must not

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-the-line/3.1-what-crosses-the-line.md) | What crosses the line | How do you hold a boundary to its docket? | production |
| [3.2](parts/03-the-line/3.2-print-that-corrupted-the-protocol.md) | The print that corrupted the protocol · **failure** | What does a corrupted wire look like when nothing goes red? | production |

## §3 Setup — run this

One package to create and one dependency to add — this project's first.

```bash
mkdir -p stock_mcp

uv add "mcp==2.2.0"
uv run python -c "import mcp; from mcp.server import MCPServer; print('mcp ok')"
```

`mcp==2.2.0` was observed on `https://pypi.org/pypi/mcp/json` on day 0, 2026-09-12, and confirmed
still current before this day was written. It is a **runtime** dependency, not a dev one: the
boundary needs it to run, so it goes in `dependencies` rather than in the `dev` group, and `uv add`
puts it there.

Two things to know before the first run:

- **Do not install `google-adk[mcp]`.** Its `mcp` extra requires `mcp<2`, which cannot coexist with
  the version above — recorded on day 0's `PACKAGES.md`. The agent days install `google-adk`
  without that extra and this project writes its own client.
- **`UV_LINK_MODE=copy` may be needed on Windows.** Installing `mcp` pulls in enough transitive
  packages that `uv add` can hit a cross-filesystem hardlink error between the cache and the
  project's `.venv` — `error: Failed to install: ... The cloud operation cannot be performed on a
  file with incompatible hardlinks.` If that happens, set `UV_LINK_MODE=copy` and run `uv add`
  again; it falls back to copying instead of hardlinking.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `stock_mcp/__init__.py` | part 1.1 |
| `stock_mcp/server.py` | part 2.1 |
| `stock_mcp/__main__.py` | part 2.2 |
| `tests/test_boundary.py` | part 3.1 |

`run` gains two lines and loses one — the `mcp` command moves from "not built yet" to a real
command. That is printed as a **marked diff** in part 2.2 against the whole file from day 1.

## §5 Build brief

Create `stock_mcp/`, add the dependency, then type the four files. The tests last, and run them
before you believe anything. Then the reps:

| File | What it must do |
| --- | --- |
| `stock_mcp/server.py` | `TODO(me)`: `fetch_bin` returns the reorder point on every call, though no rule in `stock_desk/domain.py` reads it yet. Decide whether that is a field ahead of its day or a field that should not have crossed the line until the day that reads it exists. |
| `stock_mcp/server.py` | `TODO(me)`: the boundary logs the bin id and whether it was found. Decide whether it should also log **who scanned it**, and say what would have to exist first for that to be possible. |
| `tests/test_boundary.py` | `TODO(me)`: add a test that the boundary's `instructions` are true — that there is no tool which lists every bin. Decide whether you are asserting on prose or on the docket, and say why that matters. |
| `tests/test_boundary.py` | `TODO(me)`: the smell list in `test_nothing_the_tool_returns_carries_a_file_path` has four entries chosen by hand. Add the one that would have caught a `reconciliations` folder name leaking, and say why that is a different kind of smell. |
| `stock_desk/store.py` | `TODO(me)`: `tests/test_domain.py` still imports `Store` directly. Decide whether that is a breach of the boundary or a legitimate test of the far side, and write down the rule you used to decide. |

## §6 The check that must be able to fail

```bash
./run check
```

Green is `All checks passed!`, `30 passed`, and day 0's five `ok` lines.

Three ways to make it red, and one that stays green in a way the gate cannot see — the day's
deliberate failure:

1. **Add a tool.** Any tool. `assert tools == ["fetch_bin"]` goes red with `Left contains one more
   item`, which is a new capability arriving without a signature on it.
2. **Return a path.** Add `"file": "data/ledger.json"` to the tool's reply and watch
   `test_nothing_the_tool_returns_carries_a_file_path` name the smell that crossed.
3. **Rename the module.** Point `StdioServerParameters` at `stock_mcp_typo` and watch the
   subprocess test fail with `MCPError: Connection closed` — the client cannot tell you why, and
   the answer is in the child's own standard error.
4. **The one that does not go red:** put a `print` in `fetch_bin`. The wire is corrupted, the
   client logs a parse failure, the call succeeds, **all thirty tests pass**, and on this run the
   suite's own timing did not even move. That is part 3.2, and it is why this day's failure part is
   the last one.

## §7 Request budget

**Zero.** Still no model call. The boundary declares a tool for a model to use and no model has
been introduced; `fetch_bin` is called today only by a test and by a hand-written client.

What has changed is that the budget now has somewhere to be spent from. The first agent's first
call will reach this boundary, and every call it makes will be one this desk can count — because
they all go through one process that logs them.

## §8 Traps

- **Do not add `google-adk[mcp]`.** The extra pins `mcp<2` and this project runs `mcp==2.2.0`.
- **The SDK's Python names are snake_case; the wire format is camelCase.** It is
  `tool.input_schema`, `result.structured_content`, `result.is_error`. The camelCase spellings
  raise `AttributeError: 'Tool' object has no attribute 'inputSchema'. Did you mean:
  'input_schema'?` — which is a good error, and it is the reason to read the installed package
  rather than the specification when writing Python.
- **Nothing may print to standard output in the boundary process.** Not a debug line, not a banner,
  not a library's deprecation warning. `log()` goes to standard error; that is what it is for.
- **`mcp` is a runtime dependency.** It belongs in `dependencies`, not in the `dev` group.
- **`./run mcp` blocks and looks like nothing is happening.** That is correct: the boundary is
  waiting for a client on its standard input. It is deliberately not part of `./run check`, because
  a gate that never finishes is not a gate.
- **The boundary imports the desk, and the desk never imports the boundary.** One arrow. Reversing
  it "just for a test" removes the process line and leaves the package names.
- **An unknown tool comes back as a failed result, not an exception**, because `Client` is
  constructed with `raise_exceptions=False` by default. Read `is_error`; do not rely on a `try`.
- **A corrupted wire's cost is not reliably visible in wall-clock time.** Do not treat "the suite
  got slower" as the signal that catches this failure — on some runs it does, on others it does
  not, and part 3.2 shows both.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| The `mcp` package | `https://pypi.org/pypi/mcp/json`, and day 0's `PACKAGES.md` | 2026-09-12 | `mcp==2.2.0`, unchanged since day 0's observation. Pinned with `==` in `dependencies`. |
| The blast radius before the boundary | this project, throwaway build tree | 2026-09-12 | 45 files reachable from the desk's process, `.env` among them; a tool-shaped function returned the key in its result. |
| The round trip | this project, over a subprocess | 2026-09-12 | `protocol version: 2026-07-28`, `server: stock-boundary 0.1.0`, schema derived from the function, bin returned as structured content, unknown bin `{"found": false}` with `is_error: False`. |
| The corrupted wire | this project, with a `print` in the tool | 2026-09-12 | `Invalid JSON: expected value at line 1 column 1 [type=json_invalid, input_value='looking up A-10-2\r']` — and then `30 passed in 1.72s`, against `1.71s` clean. Nothing went red, and the timing did not move either. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 02 | 3 | 2026-09-12 | The boundary, part one | 6 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — new rows, defined here at full depth as this project's own day 3 requires:

```text
| MCP | The Model Context Protocol: a JSON-RPC protocol by which a program exposes tools, resources and prompts to a model's client, so the tool lives in its own process instead of inside the agent. Its versions are dated revisions, and which one you speak is a fact about your installed SDK. | P02 day 3 part 2.1 | the protocol, Model Context Protocol |
| Protocol revision | A dated version of a specification's rules — named by date rather than by number. The *current* revision is the one the maintainers say is current, which is not necessarily the newest one that exists. | P02 day 3 part 2.1 | the spec version, the revision |
| Blast radius | How much a failure or a misuse can reach. For a tool it is not the data it was written for but everything the process it runs in can open. | P02 day 3 part 1.1 | reachable surface, containment |
| stdio transport | The binding in which a client launches the server as a child process and the protocol is that process's standard input and output — one JSON message per line, and nothing else on `stdout`, ever. | P02 day 3 part 2.2 | over stdio, the pipe transport |
| Tool (MCP) | One entry on a server's docket: a name, a description in prose, and a JSON Schema for its arguments. From the moment a model is choosing, the description **is** the API — it is the only thing the model has to go on. | P02 day 3 part 2.1 | a declared tool |
| Derived schema | A tool's argument schema built by the SDK from the function itself — name, annotations, docstring — rather than written by hand beside it. It cannot drift from the function, and it can carry only what the function already contains. | P02 day 3 part 2.1 | the generated schema |
| Structured content | The machine-readable copy of a tool's return value carried in the result envelope, alongside the human-readable content blocks. What a caller parses; the blocks are what a model reads. | P02 day 3 part 2.2 | `structured_content` |
| In-process client | A client handed the server object directly rather than a transport, so the whole protocol runs inside one process. Fast, complete except for the pipe, and never sufficient on its own: it cannot prove the server is runnable. | P02 day 3 part 3.1 | direct connection |
```

**`docs/PINS.md`** — no row is owed. `mcp==2.2.0` was already recorded at day 0 as an
observed-not-installed row; today's `uv add` confirms the same number rather than pinning a new
one, and the project's own `PACKAGES.md` carries the install row.

**`docs/SOURCES.md`** — no row is owed. Nothing with a citation identifier was cited today.

**Commit:**

```text
P02 day 3: The boundary, part one
```
