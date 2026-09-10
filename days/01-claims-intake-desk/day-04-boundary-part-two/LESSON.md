---
project: "P01"
day: 4
title: "The boundary, part two"
spine: 4
kind: mechanism
deploy_tier: D3
plan_version: "v4.1.0"
parts: 5
files_printed: [claims_mcp/__main__.py, claims_mcp/server.py, claims_desk/boundary.py, tests/test_transports.py]
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** the policy store moved behind a process line. One tool, reachable over stdio, with
> nothing but cover crossing the boundary.
> **Today:** the same server gains a second transport, a resource and a prompt; the desk gets a
> client of its own; and the protocol era turns out to be a property of the exchange rather than of
> the server.
> **Tomorrow:** the docket fills up — the tools this desk actually needs, and what a typed parameter
> is worth once a parameter stops being a string.

## §1 The scene

There are two ways to get something out of the branch office: walk in and stand at the hatch, or
ring the office. The hatch is right when you are the only person who needs the file room and would
like it to exist for exactly as long as you do. The phone is right when the office serves a
department, when it should survive one caller hanging up, and when somebody other than the caller
decides when it opens.

Today the boundary learns to answer the phone. The same server object, one extra branch in the file
that runs it, and it is a URL instead of a subprocess — with the desk's own code unable to tell
which one it got, because the choice is one environment variable and no `if` anywhere above it.

While the counter is open, two more things go on it. A **resource**: the peril vocabulary, which is
the same for every claim and is read rather than asked for. And a **prompt**: the house style for a
deficiency letter, which lives with the department that owns the claim file rather than with
whoever happens to be writing.

Then the day ends somewhere unexpected. Driving the HTTP endpoint by hand with `curl` shows this
boundary answering a modern client with `2026-07-28` and a handshake-shaped client with
`2025-11-25` — in the same run, both honestly. And the transport's **default** is the older
behaviour: one keyword argument in this project's own code is all that stands between the two, with
no test anywhere that would notice if it were removed.

## §2 The map

Three sections. **Section 1 is the server's other half** — a second transport, and the two shapes on
the docket that are not tools. **Section 2 is the desk's half** — one module that knows how to
reach the boundary, and the tests that hold both halves to their promises. **Section 3 is the wire
itself**, driven by hand, where the era gap stops being a paragraph in an ADR.

### 1 · Two transports — and the other two shapes

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-two-transports/1.1-server-as-a-url.md) | The server as a URL | What changes when the boundary stops being a subprocess? | working |
| [1.2](parts/01-two-transports/1.2-resources-and-prompts.md) | Resources and prompts | A boundary offers three kinds of thing. Which is which, and why? | working |

### 2 · The client — the desk's side, and what holds it

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-client/2.1-desks-side-of-the-line.md) | The desk's side of the line | How does the desk reach the boundary without learning which wire it used? | working |
| [2.2](parts/02-the-client/2.2-what-crosses-tested-twice.md) | What crosses, tested twice | How do you prove a transport change was configuration and not a rewrite? | production |

### 3 · The era — what the wire actually says

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-the-era/3.1-two-eras-one-server.md) | Two eras, one server | Which protocol revision is this boundary really speaking? | production |

## §3 Setup — run this

Nothing new is installed today. Two terminals are useful: one to run the boundary, one to talk to
it.

```bash
./run mcp --http
```

```text
--- uv run python -m claims_mcp --http
INFO:     Started server process [12072]
INFO:     Waiting for application startup.
StreamableHTTP session manager started
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8931 (Press CTRL+C to quit)
```

Then, in the other terminal:

```bash
curl -s -o /dev/null -w "%{http_code}\n" -X POST http://127.0.0.1:8931/mcp
```

Expect `400` — a status code rather than a connection refusal, which means something is listening.
The body is an error, and which error it is turns out to be the whole of §3.1.

`curl` is used for one part of this day and nothing depends on it. If you do not have it, the same
requests can be made with any HTTP client; the headers are what matter.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `claims_mcp/__main__.py` | part 1.1 |
| `claims_mcp/server.py` | part 1.2 |
| `claims_desk/boundary.py` | part 2.1 |
| `tests/test_transports.py` | part 2.2 |
| `run` | part 1.1, as a marked diff against day 1 part 1.3 |

`tests/test_boundary.py` also changes by one line — the boundary's version assertion moves from
`0.1.0` to `0.2.0`. That is printed as a marked diff in part 2.2 against day 3 part 3.1, which is
the day that printed the file.

## §5 Build brief

Extend `claims_mcp/__main__.py` and `claims_mcp/server.py`, then write `claims_desk/boundary.py` and
its tests. Update the version assertion when the gate tells you to, not before. Then the reps:

| File | What it must do |
| --- | --- |
| `tests/test_transports.py` | `TODO(me)`: **this project has no test that speaks HTTP.** Write one that starts the boundary on a port, POSTs a bare `tools/list`, and asserts a 200. It is the only thing that would notice `stateless_http` being dropped — which is §3.1's whole point. |
| `claims_desk/boundary.py` | `TODO(me)`: `Client` accepts `read_timeout_seconds` and this file does not set one, so a boundary that accepts a connection and never answers hangs the desk forever. Add a timeout, then say why a timeout without a retry policy is half an answer — and leave the other half for day 15. |
| `claims_desk/boundary.py` | `TODO(me)`: a connection per call means an interpreter start per lookup on stdio. Measure the twelve notifications both ways, write both numbers down, and say what would have to exist before a connection could be held open. |
| `claims_mcp/server.py` | `TODO(me)`: the server advertises `listChanged: true` for resources and never sends the notification. Either send it when the peril vocabulary changes, or say in a comment why advertising a capability you do not implement is acceptable here. |
| `claims_mcp/__main__.py` | `TODO(me)`: `HOST` is loopback and the comment says day 16 makes it a decision. Write down now, in your own notes, what would have to be true before you would bind anything else. |

## §6 The check that must be able to fail

```bash
./run check
```

Green is `All checks passed!`, `31 passed`, and day 0's four `ok` lines.

Ways to make it red:

1. **Leak the policy numbers into the resource** — add them alongside the perils rather than
   instead of them — and `assert not any("SYN-POL" in key ...)` catches it. Replacing the peril
   keys instead fails earlier and less usefully, which part 2.2 shows.
2. **Change the boundary's surface without moving its version**, or move the version without
   updating the assertion. Either way `test_the_server_declares_one_tool_and_says_who_it_is` goes
   red — and today it did, before this day was finished.
3. **Soften a line in the prompt.** `assert "Do not promise a decision" in text` is a test on prose,
   and it is there because prompts get edited more casually than code.

And the one that **cannot** go red, which is why §3.1 is this day's failure part: remove
`stateless_http=True` from `claims_mcp/__main__.py`. The boundary silently reverts to the
session-based transport the current revision removed, every test in this project still passes, and
the Python client still reports `2026-07-28`. Nothing in this repository would tell you.

## §7 Request budget

**Zero.** Four days in, still no model call. The boundary now offers a prompt — wording intended for
a model — and nothing has sent it anywhere.

Worth stating plainly, because it is about to change: the desk's request budget from day 1 counts
model calls, not boundary calls. `fetch_policy` over a process line costs latency and a subprocess,
and it costs nothing against the ceiling that day 9 will enforce.

## §8 Traps

- **`stateless_http=True` is not the default.** Without it the HTTP transport mints an
  `Mcp-Session-Id` and refuses requests that arrive without one. This project passes it explicitly;
  the day it is dropped, nothing in the test suite notices.
- **`Accept: application/json, text/event-stream` — both, or the request is refused.** The
  Streamable HTTP binding may answer either way and the client must accept both.
- **The wire is camelCase and the Python is snake_case.** `inputSchema` on the wire,
  `input_schema` in the object; `structuredContent` and `structured_content`. Neither is wrong;
  they are the same field in two places.
- **A resource URI is a name, not a directory.** `claims://cover/perils` exists and
  `claims://cover/policies` gives `Unknown resource`. Guessing a sibling gets you nothing, which is
  what makes the boundary's `instructions` true.
- **`str(resource.uri)` when comparing.** The SDK returns a URI object; comparing it to a string
  without converting gives a false negative that looks exactly like a missing resource.
- **"Application startup complete" is printed before the bind is checked.** A second server on a
  taken port announces itself as started and then fails four lines later — and a script that waits
  for that line will happily talk to the *older* server.
- **On HTTP, the boundary can be down.** That failure mode does not exist on stdio, where the
  server is started on demand. `httpx2.ConnectError: All connection attempts failed` is what it
  looks like, and it mentions nothing about claims.
- **Only one module in the desk may construct a `Client`.** The second one is the one that will
  still be pointing at stdio after the boundary moves into a container.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| The HTTP transport's default | this project, `curl -i` against `./run mcp --http` | 2026-09-10 | Without `stateless_http=True`: `400 Bad Request`, header `mcp-session-id`, body `Bad Request: Missing session ID`. With it: `200 OK`, `content-type: text/event-stream`, no session header. |
| The legacy handshake still answers | this project, `initialize` by hand | 2026-09-10 | Returns `"protocolVersion":"2025-11-25"` — **not** the `2026-07-28` the request asked for — with capabilities and `serverInfo` at the top level. |
| What the modern era requires per request | this project, three refusals in a row | 2026-09-10 | `params._meta` must carry `io.modelcontextprotocol/protocolVersion` **and** `io.modelcontextprotocol/clientCapabilities`, and an `mcp-method` header must match the body's method. Each refusal names exactly what is missing. |
| `server/discover` | this project, with the full envelope | 2026-09-10 | Answers only in the modern era. Returns `"supportedVersions": ["2026-07-28"]`, capabilities with `listChanged`/`subscribe` true, `cacheScope`, `ttlMs`, `resultType`, and identity under `_meta.io.modelcontextprotocol/serverInfo`. Without the envelope: `Method not found`. |
| Resources and prompts | this project, in-process and by hand | 2026-09-10 | `claims://cover/perils` returns the vocabulary with the photograph rule; `claims://cover/policies` gives `MCPError: Unknown resource`. The prompt comes back with its arguments already substituted by the server. |
| One desk, two transports | this project, with and without `CLAIMS_BOUNDARY` | 2026-09-10 | Identical code, identical answer, one log field different: `"transport": "stdio"` against `"transport": "http"`, both `"protocol": "2026-07-28"`. |
| The gate | this project, `./run check` | 2026-09-10 | ruff clean, `31 passed`, day 0's four checks green. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 01 | 4 | 2026-09-10 | The boundary, part two | 5 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the first six restate definitions the glossary already carries; the rest
are new:

```text
| Transport | The arrangement that carries protocol messages from one process to another. The specification calls it a binding: it decides how messages are framed and delivered and how termination is signalled, and never what a message means. | P01 day 4 part 1.1 | a binding |
| Streamable HTTP | The binding in which the server is a URL rather than a process: one endpoint that accepts POST, one HTTP request per message, and an answer that is either a single JSON object or an event stream scoped to that request. | P01 day 4 part 1.1 | the HTTP transport, the MCP endpoint |
| Server-Sent Events | An HTTP response whose body is a sequence of small blocks — an `event:` line and a `data:` line, separated by blank lines — rather than one document, so the server can keep sending after it has begun answering. | P01 day 4 part 3.1 | SSE, `text/event-stream` |
| Protocol session | Connection-scoped state a server keeps about one client, minted by the transport and quoted back on every later request. Removed at protocol level by the `2026-07-28` revision and still the SDK's HTTP default. | P01 day 4 part 3.1 | `Mcp-Session-Id`, the session header |
| Protocol era | MCP's own name for the two sides of the `2026-07-28` line. **Modern** revisions carry version, identity and capabilities as per-request metadata; **legacy** revisions establish a session with an `initialize` handshake. Which one governs is a property of the exchange, not of the server. | P01 day 4 part 3.1 | modern and legacy |
| MCP client | The near side of the boundary: the code that launches or connects to a server, asks for what it offers, and forwards each call. In this project it is one context manager and two functions. | P01 day 4 part 2.1 | the client side |
| Resource (MCP) | Something a caller reads rather than asks for, addressed by a URI and taking no arguments. Reference data that is the same for every request, so it is fetched once instead of being a decision a model makes per turn. | P01 day 4 part 1.2 | a read, a URI |
| Prompt (MCP) | A named piece of wording a server offers for asking a model about the things that server owns, with arguments substituted server-side. It lives with the data it is about, so the wording and the data version together. | P01 day 4 part 1.2 | a server-supplied template |
| Version negotiation | The client naming the protocol revision it wants and the server naming the one that will actually govern the connection. The two may differ: a legacy handshake is answered with a legacy revision whatever was asked for. | P01 day 4 part 3.1 | protocol version agreement |
| Capability negotiation | Each side declaring which optional features it supports before either asks for anything. In the legacy era it happens once, in the handshake; in the modern era the client's half rides on every request in `_meta`. | P01 day 4 part 3.1 | the capabilities exchange |
```

**`docs/PINS.md`** — no row is owed. Nothing was installed today, and the specification row from
day 3 is unchanged.

**`docs/SOURCES.md`** — no row is owed. Nothing with a citation identifier was cited.

**Commit:**

```text
P01 day 4: The boundary, part two
```
