---
project: "P02 Parts Counter"
day: 16
phase: P02
title: "P02 Parts Counter · 6 — Transports: stdio and Streamable HTTP"
ids: [MC-05]
kind: mechanism
deploy_tier: "D2"
plan_version: "v3.1.0"
parts: 4
files_printed:
  - "projects/02-parts-counter/run.py"
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** the lifecycle — the `initialize` exchange run by hand, the version the server
> counters with when it does not know yours, and the changelog line at the current revision that
> deleted the whole ceremony.
> **Today:** the same server, carried two completely different ways, without editing one line of it —
> a subprocess and two pipes, or one URL that takes a POST per message.
> **Tomorrow:** the client side — the agent stops importing four functions and starts asking another
> process what tools it has.

## §1 The scene

A restaurant on two floors has a dumbwaiter. The kitchen loads a tray into the car in the shaft,
pulls the rope, and the tray arrives upstairs. There is one shaft, one car, and two hatches, and
that is its entire charm: nothing needs an address, because there is nowhere else a tray could have
come from and nowhere else it could go.

Later the same kitchen starts sending food out to the unit next door, and there is no shaft. There
is a roller door onto the yard and a numbered bay. Each order leaves on its own trip. The bay has no
memory of what went out before, and it asks one question before it loads anything — what can you
carry — because a sealed box and an open pallet are packed differently and there is no undoing it
once the door is shut.

Nothing about the cooking changed. Same dish, same plate, same note under the rim. What changed is
who can be at the other end, how you know something arrived, and what happens to a tray that is
halfway there when the power goes off.

That is today. Your boundary server speaks a protocol; a transport is only the arrangement that
carries those messages from one process to another, and the file day 13 printed has not one line
that differs between the two. What *does* differ is everything around it. The shaft will accept
anything you drop into it, including things you never meant to send — and you will watch six
characters of debugging output eat a complete tool result. The bay turns away a van that has not
said what it can carry, and that refusal reads like a bug in your JSON when it is nothing of the
kind. And bolted to the wall at the far end of the yard there is an older goods lift that still
works, that nobody should be using, and that your toolchain will happily start for you without a
word of complaint.

## §2 The map

Two sections, split by the thing the reader has to hold in their head. The first is the shaft: what a
transport actually is, and then the one that runs between two processes on one machine, whose single
hard rule you will break on purpose. The second is the yard: the transport that is an address rather
than a process, and then the one in the corner with the sign on it.

### 1 · Two ways to carry the same messages

*The mental model: the kitchen does not change when the shaft is replaced by a bay, and everything
else does.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-two-ways-to-carry-the-same-messages/1.1-the-transport-is-a-binding.md) | The transport is a binding | If the protocol is identical on every transport, what is left for a transport to decide? | foundation |
| [1.2](parts/01-two-ways-to-carry-the-same-messages/1.2-stdio-a-subprocess-and-two-pipes.md) | stdio — a subprocess and two pipes | Why is one `print()` in your server not noise on the channel but a protocol violation? | working |

### 2 · Over HTTP

*The mental model: a doorway is not a queue of one, and the paperwork happens before the loading.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-over-http/2.1-one-endpoint-one-post-per-message.md) | One endpoint, one POST per message | What does a message actually look like on the wire, and why must the client declare `Accept` first? | working |
| [2.2](parts/02-over-http/2.2-the-transport-that-is-already-history.md) | The transport that is already history | The SDK still accepts a deprecated transport and it still starts — so what goes wrong, and where? | production |

## §3 Setup — run this

Nothing new to install. Today adds two subcommands to a driver this project already has, and runs a
server this project already has over two bindings the pinned SDK already implements. Every command
below was run on this machine today; what each one reported is in §9.

```bash
cd projects/02-parts-counter

# part 1.2 adds serve_mcp() and the two `mcp` arms of main() to run.py, then:
uv run --frozen python run.py mcp            # the dumbwaiter — reads stdin, writes stdout
uv run --frozen python run.py mcp --http     # the loading bay — 127.0.0.1:8090/mcp

# part 1.1 — the three strings the SDK accepts, read out of the installed wheel
uv run --frozen python -c "import inspect; from mcp.server.fastmcp import FastMCP; print(inspect.getsource(FastMCP.run))"

# part 2.1 — the endpoint's own settings, rather than an assumption about them
uv run --frozen python -c "from parts_mcp.server import mcp; print(mcp.settings.streamable_http_path, mcp.settings.json_response)"
```

`--frozen` is on every `uv run` for the reason P00 day 3 established and `PRIMER.md` §2 recaps: plain
`uv run` brings the lockfile up to date before it runs your command, and a check invoked that way
inspects a repository its own invocation repaired.

**Two terminals from part 2.1 onward.** The HTTP server holds the one it is started in. Stop it with
Ctrl+C when the day is done — §8's last trap is about what happens if you do not.

## §4 Files this day prints

One file, as a marked diff. `parts_mcp/server.py` is **not** reprinted today: day 13 printed it whole
and today's entire argument is that it does not change. Nothing else in the project is touched.

| File | Printed by |
| --- | --- |
| `projects/02-parts-counter/run.py` | part 1.2, as a marked diff against the whole file day 11 part 2.2 printed — the module docstring, `serve_mcp()`, and two new arms of `main()` |

The other differences between day 11's `run.py` and the finished one belong to **day 14** (`parts`
and `race` repointed at `parts_mcp`) and **day 17** (`probe`). Part 1.2 says so on the page, so that
`CODEMAP.md` and the day documents cannot disagree about who printed what.

## §5 Build brief

| File | What it must do |
| --- | --- |
| `run.py` — `serve_mcp()` | `TODO(me)`: type the diff from part 1.2. Before running it, say why the import of `parts_mcp.server` is inside the function rather than at the top of the file, then check your answer against what `run.py check` has to be able to do. |
| `run.py` — the two `main()` arms | `TODO(me)`: type them, then run `python run.py mcp --htp` (note the typo) and say which exit status you get and why that is the right one. |
| the framing rep | `TODO(me)`: pipe the three-message handshake from part 1.2 into `run.py mcp` and count the lines that come back. Say why it is not three before you look it up. |
| the stdout rep | `TODO(me)`: add `print("hello")` to a tool body in `parts_mcp/server.py`, run the handshake, and confirm nothing appears. Re-run with `PYTHONUNBUFFERED=1`. Then change it to `print("hello", end="", flush=True)` and run `python run.py probe`. Remove the line and re-run the clean handshake before moving on. |
| the `Accept` rep | `TODO(me)`: with `run.py mcp --http` up, send `tools/list` with no `Accept` header, then with both media types, then with `text/event-stream` alone. Predict the third before you send it. |
| the deprecation rep | `TODO(me)`: start the server with `transport="sse"` on port 8092 as part 2.2 shows. Write down which of `/mcp`, `/sse` and `/messages/` you expect to exist, and what status each returns, before you probe them. Stop the server afterwards. |

## §6 The check that must be able to fail

```text
cd projects/02-parts-counter
uv run --frozen python run.py check    # the project's own gate — six checks, unchanged today
echo $?                                # 0 green, 1 red, 2 you typed it wrong
cd ../.. && python p.py depth 16       # this day against the plan §5 contract
```

Today adds no check to `run.py`, and that is worth stating rather than hiding: the gate covers
configuration and the boundary's own tests, and neither of the two transports is exercised by it. The
things that go red today go red in your terminal, on purpose, and there are three of them.

**How to make it go red on purpose — three ways, and the second is the day's real one.**

The first is a typo. Run the server with `transport="http"` and it raises
`ValueError: Unknown transport: http` before anything binds. That is the cheap failure: loud,
immediate, and at the moment of the mistake.

The second is the day's deliberate failure and it is part 1.2's. Put `print("hello")` in a tool body
and run the by-hand handshake: **nothing happens**, because buffering swallowed it. Add
`PYTHONUNBUFFERED=1` and the same file now emits a junk line into the middle of the protocol stream.
Change it to `print("hello", end="", flush=True)` and the junk stops being its own line and becomes a
prefix on the next real one — which eats a complete tool result and costs the caller a full client
timeout. One source file, three behaviours, and the only thing that changed was how the output
happened to be connected.

The third is part 2.2's, and it is the one with no error at all. Start the server with
`transport="sse"`, watch it report `Application startup complete`, and then send it a Streamable HTTP
request and read the `404`. Nothing in the server's logs will ever mention the transport.

For the document itself: delete a `## In production` heading from any part and run
`python p.py depth 16`; it names the file and the missing section.

## §7 Request budget

**Zero model calls. Not "few" — zero.**

Nothing today reaches a provider. Both transports are exercised against this project's own boundary,
which holds a synthetic inventory in a JSON file and answers from it. `curl`, a shell pipe and the
SDK's own client are the only things sending anything anywhere, and the furthest any of it travels is
`127.0.0.1`. No agent runs, so the plan §9 rule that a turn's cost is counted **across the whole
cast** has nothing to count today — the first non-zero number in this project arrives on day 17, when
the agent is wired to the boundary.

The free-tier ceiling this project would be spending against is **not stated here and is not stated
anywhere in this repository**: per-model RPM, TPM and RPD were withdrawn from publication, so
`TODO(me)`: read the current limits for your key in Google AI Studio and write down what you find
rather than trusting a number from a document. That is ADR-0004's rule, and it applies to a day that
spends nothing exactly as much as to one that spends a lot.

## §8 Traps

- **A transport is a binding, not a dialect.** If any code in your server branches on which transport
  is in use, something has gone wrong in the design — the protocol is identical on all of them.
- **`http` is not a transport name.** The string is `streamable-http`. `ValueError: Unknown transport:
  http` is what you get, at start-up, which is the good case.
- **The SDK's accepted-values list is a compatibility promise, not advice.** `"sse"` is in it and has
  been deprecated for two protocol revisions.
- **On stdio, `stdout` is the protocol.** Not "mostly the protocol". One non-message line corrupts it,
  and that includes anything printed by a library you imported.
- **A stray `print()` usually does nothing — until it does.** Under a pipe, Python block-buffers, and
  the SDK re-wraps `sys.stdout.buffer` in its own writer, so your five characters are commonly
  discarded. `PYTHONUNBUFFERED=1`, a terminal, or `flush=True` turns the same source file into a
  protocol violation with no code change.
- **A `print` without a trailing newline is far worse than one with.** With a newline you lose a log
  line; without one you lose the *next message*, and the caller gets a timeout that names nothing.
- **`stderr` is not the error channel.** The specification says clients **SHOULD NOT** assume `stderr`
  output indicates an error, and this server logs `Processing request of type ListToolsRequest` there
  on every healthy request.
- **Three messages in does not mean three messages out.** A notification has no `id` and gets no
  reply. Client code that pairs counts rather than ids will hang.
- **`Accept` must carry both media types.** `application/json, text/event-stream`. One of the two is
  a `406`, refused before your body is parsed, reported with JSON-RPC code `-32600` — which is
  "Invalid Request" and will send you hunting through perfectly good JSON.
- **The MCP endpoint path is a default, not a law.** `/mcp` here, readable from
  `mcp.settings.streamable_http_path`. A guessed path is a `404` that explains nothing.
- **A `404` from the deprecated transport looks like a healthy server.** It is: the server is
  answering correctly, on the two paths it serves, and neither of them is the one your client wants.
- **A readiness probe that only opens a socket proves nothing.** The `sse` server passes it. Probe
  with something that speaks the protocol.
- **Leave nothing running.** The HTTP server holds its terminal and its port; part 2.2's experiment
  binds a second one. A later `run.py mcp --http` on a port that is still held fails with
  `[Errno 10048] ... only one usage of each socket address ... is normally permitted`, and the
  server it prints that from exits while an *older* server keeps answering your requests.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| The three accepted transport strings | `inspect.getsource(FastMCP.run)`, `mcp` 1.30.0 in this project's `.venv` | 2026-09-10 | `transport: Literal["stdio", "sse", "streamable-http"] = "stdio"`, and a hand-written check raising `ValueError(f"Unknown transport: {transport}")` — part 1.1 |
| An unknown transport is refused at start-up | `mcp.run(transport='http')` | 2026-09-10 | `ValueError: Unknown transport: http`, raised at `fastmcp/server.py` line 308, nothing bound — part 1.1 |
| `run.py mcp` serves the protocol on stdio | the three-message handshake piped into `uv run --frozen python run.py mcp` | 2026-09-10 | two newline-delimited JSON-RPC replies on `stdout`, exit `0`; `wc -l` says 2 for 3 messages in — part 1.2 |
| `stderr` carries logs, not errors | the same run with `2>&1 >/dev/null` | 2026-09-10 | `Processing request of type ListToolsRequest` on `stderr` during a run in which nothing failed — part 1.2 |
| A stray `print()` is silently swallowed under a pipe | `print("hello")` in `stock_level`, handshake piped | 2026-09-10 | two clean protocol lines, no `hello` anywhere on `stdout` or `stderr` — part 1.2 |
| The SDK re-wraps the output file | `grep "TextIOWrapper(sys.std" .venv/.../mcp/server/stdio.py` | 2026-09-10 | line 49: `TextIOWrapper(sys.stdout.buffer, encoding="utf-8")` — a second text wrapper on the same file — part 1.2 |
| One environment variable turns it into a violation | the same server with `PYTHONUNBUFFERED=1` | 2026-09-10 | `hello` on its own line between two protocol messages, source file unchanged — part 1.2 |
| A newline-less `print` eats the next message | `print("hello", end="", flush=True)`, called through this project's stdio toolset | 2026-09-10 | `Invalid JSON: expected value at line 1 column 1 [type=json_invalid, input_value='hello{"jsonrpc":"2.0","i...ue},"isError":false}}\r'...]`, then `McpError: Timed out while waiting for response to ClientRequest` and a failed tool result — part 1.2 |
| The endpoint path and answer shape are settings | `mcp.settings.streamable_http_path`, `mcp.settings.json_response` | 2026-09-10 | `/mcp` and `False` — this server always answers as an event stream — part 2.1 |
| The transport refuses a request whose `Accept` is wrong | `POST /mcp` with `Content-Type` only | 2026-09-10 | `406 Not Acceptable`, body `{"jsonrpc":"2.0","id":"server-error","error":{"code":-32600,"message":"Not Acceptable: Client must accept both application/json and text/event-stream"}}` — part 2.1 |
| A served message is JSON-RPC inside SSE framing | `POST /mcp` with both media types, headers dumped | 2026-09-10 | `content-type: text/event-stream`, `Transfer-Encoding: chunked`, `x-accel-buffering: no`, then `event: message` / `data: {...}` carrying `serverInfo` `parts-mcp` `1.30.0` — **and no `mcp-session-id` header** — part 2.1 |
| Two tool calls on fresh connections, no `initialize` | two separate `curl` POSTs, `stock_level` then `bin_location` | 2026-09-10 | both answered, `isError: false`, ids echoed — part 2.1 |
| The deprecated transport still starts | `mcp.run(transport='sse')` on `127.0.0.1:8092` | 2026-09-10 | `Application startup complete`, `Uvicorn running on http://127.0.0.1:8092` — no warning of any kind — part 2.2 |
| …and serves nothing a Streamable HTTP client wants | `POST /mcp`, `POST /messages/`, `GET /sse` against it | 2026-09-10 | `404 Not Found` in `text/plain`; `400` with the server logging `Received request without session_id`; `200` and a stream that does not end — part 2.2 |
| …and this project's own client cannot connect | `over_http('http://127.0.0.1:8092/mcp')` | 2026-09-10 | `ConnectionError: Failed to create MCP session: Failed to create MCP session: Session terminated`, with no `404` anywhere in the traceback — part 2.2 |
| The era gap, visible in status codes | `DELETE /mcp` and `GET /mcp` against the stateless Streamable HTTP server | 2026-09-10 | `DELETE` → `405 Method Not Allowed`, `Method Not Allowed: Session termination not supported`, matching the current revision's rule; `GET` → `200` and an open stream, where the current revision says `405` — part 2.2 |
| A made-up session id is ignored, not echoed | `POST /mcp` with `Mcp-Session-Id: 000…0` | 2026-09-10 | the call was answered normally and no session header came back — part 2.2 |
| stdio framing, stderr, the `stdout` rule and restart behaviour | `https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio` | 2026-09-10 | the four passages quoted verbatim in part 1.2, all labelled with the revision |
| The Streamable HTTP shape, the replacement, and the deprecation block | `https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http` | 2026-09-10 | the endpoint description quoted in part 2.1; "introduced in protocol version 2025-03-26 as a replacement for the HTTP+SSE transport", the **Deprecated** block, and the legacy-traffic rules quoted in part 2.2 |
| A transport is a binding | `https://modelcontextprotocol.io/specification/2026-07-28/basic/transports` | 2026-09-10 | "Protocol semantics are identical on every transport. A transport is a **binding**…" — part 1.1 |

## §10 Ledger & commit

**`docs/PROGRESS.md`:**

```text
| 16 | 2026-09-10 | MC-05 | 4 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the terms this day defined for the first time. Check the file before
appending: days 13 to 15 are being written alongside this one and a term already there is linked,
never redefined.

```text
| Transport | The arrangement that carries protocol messages from one process to another. The specification calls it a binding: it decides how messages are framed and delivered and how termination is signalled, and never what a message means. | day 16 part 1.1 | a binding |
| stdio transport | The binding in which a client launches the server as a child process and the protocol is that process's standard input and output — one JSON message per line, and nothing else on `stdout`, ever. | day 16 part 1.2 | over stdio, the pipe transport |
| Streamable HTTP | The binding in which the server is a URL rather than a process: one endpoint that accepts POST, one HTTP request per message, and an answer that is either a single JSON object or an event stream scoped to that request. | day 16 part 2.1 | the HTTP transport, the MCP endpoint |
| Server-Sent Events | An HTTP response whose body is a sequence of small blocks — an `event:` line and a `data:` line, separated by blank lines — rather than one document, so the server can keep sending after it has begun answering. | day 16 part 2.1 | SSE, `text/event-stream` |
| Deprecated | Of a feature: still present, still working, and no longer what you should choose — with a successor named and usually a revision attached. Its failure mode is not an error but success, for a while, followed by a cost nobody attributed to the choice. | day 16 part 2.2 | superseded, legacy |
```

**`docs/PINS.md`** — nothing to add. Today observes no version that day 13 did not already record;
`mcp` 1.30.0 and the `2026-07-28` specification revision both have rows in this project's
`PACKAGES.md` with the same date.

**`docs/SOURCES.md`** — nothing to add. The specification pages quoted today are living documentation
rather than records with resolvable identifiers, and each is listed with its URL and the date it was
read in §9, which is what that table is for. This is the same call days 1 to 3 made.

**Commit:**

```text
day 16: P02 Parts Counter · 6 — Transports: stdio and Streamable HTTP — closes MC-05
```
