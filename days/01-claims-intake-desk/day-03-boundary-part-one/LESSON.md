---
project: "P01"
day: 3
title: "The boundary, part one"
spine: 3
kind: mechanism
deploy_tier: D3
plan_version: "v4.1.0"
parts: 5
files_printed: [claims_mcp/__init__.py, claims_mcp/server.py, claims_mcp/__main__.py, tests/test_boundary.py]
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** eight invented policies, twelve notifications with their answers written by hand,
> the records as types, and one class — `Store` — allowed to open a file.
> **Today:** that class moves to the far side of a process line. The desk stops holding data and
> starts asking for it, across a real protocol, through one declared tool.
> **Tomorrow:** the second transport — the boundary as a URL rather than a subprocess — and the
> client wiring that lets the desk reach it either way.

## §1 The scene

The file room at a branch office has a hatch. You do not walk in among the shelves: you give the
clerk a reference, the clerk fetches, the folder comes back through the hatch. Somebody proposes
removing it — the clerk is a bottleneck, everybody is trustworthy — and what the hatch actually
bought only becomes sayable once it is gone.

Yesterday's `Store` was a clerk by agreement. Nothing stopped the next module importing `json` and
`pathlib` and going to the shelves directly, and agreements hold until a deadline. Today the
agreement becomes a wall, and the first thing this day does is measure what the wall is worth:
**fifty-six files** are reachable by a tool-shaped function in the desk's process right now,
`.env` among them.

So the policy store moves into `claims_mcp/`, a second top-level package that runs as its own
program. It declares one tool. The tool's own signature and docstring become the entire interface —
nobody writes a schema, and nothing but cover crosses the line: no path, no filename, no record id.
A client launches `python -m claims_mcp`, asks a question down the process's standard input, and
gets a policy back.

That last sentence carries the day's trap in it. On this transport the protocol **is** the child's
standard output, so a single `print` in a tool is a message on the wire. The last part causes
exactly that, and the result is the uncomfortable one: the client logs a parse failure, skips the
line, answers correctly, and **all twenty-five tests still pass.**

## §2 The map

Three sections. **Section 1 is the argument** — what the desk can reach today, as a number, and why
that is the thing a boundary changes. **Section 2 is the server** — one object, one tool, and the
four lines that make it a program. **Section 3 is the line itself** — what is allowed to cross it,
and what happens when something else does.

### 1 · Why a boundary — the number, not the principle

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-why-a-boundary/1.1-clerk-and-the-file-room.md) | The clerk and the file room | What can a tool in this process actually reach, and why does that change everything? | foundation |

### 2 · The server — the docket, and the program behind it

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-server/2.1-server-and-the-tool-it-declares.md) | The server, and the tool it declares | How does a function become an interface a model can read? | working |
| [2.2](parts/02-the-server/2.2-run-it-as-a-process.md) | Run it as a process | How does a client launch the boundary and get an answer out of it? | working |

### 3 · The line — what may cross, and what must not

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-the-line/3.1-what-crosses-the-line.md) | What crosses the line | How do you hold a boundary to its docket? | production |
| [3.2](parts/03-the-line/3.2-print-that-corrupted-the-protocol.md) | The print that corrupted the protocol | What does a corrupted wire look like when nothing goes red? | production |

## §3 Setup — run this

One package to create and one dependency to add — this project's first.

```bash
mkdir -p claims_mcp

uv add "mcp==2.2.0"
uv run python -c "import mcp; from mcp.server import MCPServer; print('mcp ok')"
```

`mcp==2.2.0` was read from `https://pypi.org/pypi/mcp/json` on 2026-09-10. It is a **runtime**
dependency, not a dev one: the boundary needs it to run, so it goes in `dependencies` rather than
in the `dev` group, and `uv add` puts it there.

Two things to know before the first run:

- **Do not install `google-adk[mcp]`.** Its `mcp` extra requires `mcp<2`, which cannot coexist with
  the version above. The agent days install `google-adk` without that extra and this project writes
  its own client. Why, and what it costs, is `docs/adr/ADR-0009`.
- **Keep the project's path short on Windows.** Installing `mcp` creates deep paths inside
  `.venv`, and a project folder nested far enough down puts some of them past the 260-character
  limit — at which point the shell can read a file and Python reports `FileNotFoundError` for the
  same path. §8 has the symptom.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `claims_mcp/__init__.py` | part 1.1 |
| `claims_mcp/server.py` | part 2.1 |
| `claims_mcp/__main__.py` | part 2.2 |
| `tests/test_boundary.py` | part 3.1 |

`run` gains two lines and loses one — the `mcp` command moves from "not built yet" to a real
command. That is printed as a **marked diff** in part 2.2 against the whole file from day 1 part
1.3, which is the day that printed it.

## §5 Build brief

Create `claims_mcp/`, add the dependency, then type the four files. The tests last, and run them
before you believe anything. Then the reps:

| File | What it must do |
| --- | --- |
| `claims_mcp/server.py` | `TODO(me)`: `fetch_policy` returns nine fields. Go through them one at a time and delete every one that no rule in `claims_desk/domain.py` reads. Say what you deleted and why the rest survived. |
| `claims_mcp/server.py` | `TODO(me)`: the boundary logs the number and whether it was found. Decide whether it should also log **who asked**, and say what would have to exist first for that to be possible. |
| `tests/test_boundary.py` | `TODO(me)`: add a test that the boundary's `instructions` are true — that there is no tool which lists policies. Decide whether you are asserting on prose or on the docket, and say why that matters. |
| `tests/test_boundary.py` | `TODO(me)`: the smell list in `test_nothing_the_tool_returns_carries_a_file_path` has four entries chosen by hand. Add the one that would have caught a `holder_ref` leaking, and say why that is a different kind of smell. |
| `claims_desk/store.py` | `TODO(me)`: the desk still imports `Store` directly in `tests/test_domain.py`. Decide whether that is a breach of the boundary or a legitimate test of the far side, and write down the rule you used to decide. |

## §6 The check that must be able to fail

```bash
./run check
```

Green is `All checks passed!`, `25 passed`, and day 0's four `ok` lines.

Three ways to make it red — and one that is red in a way the gate cannot see, which is the day's
deliberate failure:

1. **Add a tool.** Any tool. `assert tools == ["fetch_policy"]` goes red with `Left contains one
   more item`, which is a new capability arriving without a signature on it.
2. **Return a path.** Add `"file": "data/policies.json"` to the tool's reply and watch
   `test_nothing_the_tool_returns_carries_a_file_path` name the smell that crossed.
3. **Rename the module.** Point `StdioServerParameters` at `claims_mcp_typo` and watch the
   subprocess test fail with `MCPError: Connection closed` — the client cannot tell you why, and
   the answer is in the child's own standard error.
4. **The one that does not go red:** put a `print` in `fetch_policy`. The wire is corrupted, the
   client logs a parse failure, the call succeeds, and **all twenty-five tests pass**. The only
   visible difference is the suite's reported duration. That is part 3.2, and it is why this day's
   failure part is the last one.

## §7 Request budget

**Zero.** Still no model call. The boundary declares a tool for a model to use and no model has
been introduced; `fetch_policy` is called today only by a test and by a hand-written client.

What has changed is that the budget now has somewhere to be spent from. Day 7's first agent will
reach this boundary, and every call it makes will be one this desk can count — because they all go
through one process that logs them.

## §8 Traps

- **Do not add `google-adk[mcp]`.** The extra pins `mcp<2` and this project runs `mcp==2.2.0`. The
  agent days install `google-adk` plain. `docs/adr/ADR-0009` is the record.
- **The SDK's Python names are snake_case; the wire format is camelCase.** It is
  `tool.input_schema`, `result.structured_content`, `result.is_error`. The camelCase spellings
  raise `AttributeError: 'Tool' object has no attribute 'inputSchema'. Did you mean: 'input_schema'?`
  — which is a good error, and it is the reason to read the installed package rather than the
  specification when writing Python.
- **Windows' 260-character path limit.** A deep project folder plus `.venv/Lib/site-packages/...`
  can exceed it, and the symptom is bizarre: `ls` prints the file, Python raises
  `FileNotFoundError` for the same path. Keep the project near the root of a drive, or enable long
  paths.
- **Nothing may print to standard output in the boundary process.** Not a debug line, not a banner,
  not a library's deprecation warning. `log()` goes to standard error; that is what it is for.
- **`mcp` is a runtime dependency.** It belongs in `dependencies`, not in the `dev` group — the
  container on day 19 needs it and does not get the dev group.
- **`./run mcp` blocks and looks like nothing is happening.** That is correct: the boundary is
  waiting for a client on its standard input. It is deliberately not part of `./run check`, because
  a gate that never finishes is not a gate.
- **The boundary imports the desk, and the desk never imports the boundary.** One arrow. Reversing
  it "just for a test" removes the process line and leaves the package names.
- **An unknown tool comes back as a failed result, not an exception**, because `Client` is
  constructed with `raise_exceptions=False` by default. Read `is_error`; do not rely on a `try`.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| The current MCP revision | `https://modelcontextprotocol.io/docs/learn/versioning` | 2026-09-10 | "The **current** protocol version is **2026-07-28**." Every request declares its version in `io.modelcontextprotocol/protocolVersion` inside `_meta`; `server/discover` is "a mandatory RPC that returns the server's supported protocol versions, capabilities, and identity in a single request". |
| The `mcp` package | `https://pypi.org/pypi/mcp/json` | 2026-09-10 | Latest `2.2.0`, `requires_python >=3.10`. Pinned with `==` in `dependencies`. |
| Why `google-adk[mcp]` is not used | `https://pypi.org/pypi/google-adk/json` | 2026-09-10 | `google-adk` 2.8.0 declares `mcp<2,>=1.24; extra == "mcp"`. Recorded in `docs/adr/ADR-0009`. |
| The SDK's real API | the installed package, by introspection | 2026-09-10 | `MCPServer(name, title, version, instructions, ...)`, `@server.tool()`, `server.run("stdio")`; `Client(server_or_params)`, `client.protocol_version`, `client.server_info`, `list_tools()`, `call_tool()`; fields `input_schema`, `structured_content`, `is_error`. |
| The blast radius before the boundary | this project | 2026-09-10 | 56 files reachable from the desk's process, `.env` among them; a tool-shaped function returned the key in its result. |
| The round trip | this project, over a subprocess | 2026-09-10 | `protocol version: 2026-07-28`, `server: claims-boundary 0.1.0`, schema derived from the function, policy returned as structured content, unknown policy `{"found": false}` with `is_error: False`. |
| The corrupted wire | this project, with a `print` in the tool | 2026-09-10 | `Invalid JSON: expected value at line 1 column 1 [type=json_invalid, input_value='looking up SYN-POL-1001\r']` — and then `25 passed in 8.30s`, against `1.66s` clean. Nothing went red. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 01 | 3 | 2026-09-10 | The boundary, part one | 5 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the first four restate definitions the glossary already carries; the rest
are new:

```text
| MCP | The Model Context Protocol: a JSON-RPC protocol by which a program exposes tools, resources and prompts to a model's client, so the tool lives in its own process instead of inside the agent. Its versions are dated revisions, and which one you speak is a fact about your installed SDK. | P01 day 3 part 2.1 | the protocol, Model Context Protocol |
| Protocol revision | A dated version of a specification's rules — `2025-06-18`, `2025-11-25`, `2026-07-28` — named by date rather than by number. The *current* revision is the one the maintainers say is current, which is not necessarily the newest one that exists. | P01 day 3 part 2.1 | the spec version, the revision |
| Blast radius | How much a failure or a misuse can reach. For a tool it is not the data it was written for but everything the process it runs in can open. | P01 day 3 part 1.1 | reachable surface, containment |
| stdio transport | The binding in which a client launches the server as a child process and the protocol is that process's standard input and output — one JSON message per line, and nothing else on `stdout`, ever. | P01 day 3 part 2.2 | over stdio, the pipe transport |
| Tool (MCP) | One entry on a server's docket: a name, a description in prose, and a JSON Schema for its arguments. From the moment a model is choosing, the description **is** the API — it is the only thing the model has to go on. | P01 day 3 part 2.1 | a declared tool |
| Derived schema | A tool's argument schema built by the SDK from the function itself — name, annotations, docstring — rather than written by hand beside it. It cannot drift from the function, and it can carry only what the function already contains. | P01 day 3 part 2.1 | the generated schema |
| Structured content | The machine-readable copy of a tool's return value carried in the result envelope, alongside the human-readable content blocks. What a caller parses; the blocks are what a model reads. | P01 day 3 part 2.2 | `structured_content` |
| In-process client | A client handed the server object directly rather than a transport, so the whole protocol runs inside one process. Fast, complete except for the pipe, and never sufficient on its own: it cannot prove the server is runnable. | P01 day 3 part 3.1 | direct connection |
```

**`docs/PINS.md`** — one row is owed, because the MCP revision is a fact about the world rather
than about a project:

```text
| MCP specification | 2026-07-28 | 2026-09-10 | P01 day 3 | Re-read at `https://modelcontextprotocol.io/docs/learn/versioning` before P01's boundary was written. Confirms the revision recorded earlier is still current, and — new since then — `mcp` 2.2.0 on PyPI speaks it, so a project can now execute the current revision. `google-adk` 2.8.0 still declares `mcp<2` under its `mcp` extra. See `docs/adr/ADR-0009`. |
```

`mcp==2.2.0` itself is a **project** pin and goes in this project's own `PACKAGES.md`, dated.

**`docs/SOURCES.md`** — no row is owed. The specification was read as a live page and is recorded
in §9 with its date; nothing was cited by identifier.

**Commit:**

```text
P01 day 3: The boundary, part one
```
