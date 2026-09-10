---
project: "P02 Parts Counter"
day: 13
phase: P02
title: "P02 Parts Counter · 3 — MCP 2026: the stateless core, and the phone-call to web reframe"
ids: [MC-02]
kind: concept
deploy_tier: D2
plan_version: "v3.1.0"
parts: 4
files_printed:
  - "projects/02-parts-counter/parts_mcp/server.py"
  - "projects/02-parts-counter/pyproject.toml"
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** the stockroom door propped open — the store, the four tools, two writers losing
> parts on purpose, and the argument for one owner in front of the data, assembled with its costs
> attached.
> **Today:** the protocol that owner will speak. What a session is and what it costs, the one keyword
> argument that decides whether this boundary answers a stranger, and the honest paragraph about
> which era of MCP this project can actually run.
> **Tomorrow:** the server skeleton and its first tool — the four tools taken one at a time, and what
> a call looks like on the wire.

## §1 The scene

Before automatic dialling, a call was a physical object. You lifted the handset, a voice said *number
please*, and somebody took a cord from a shelf and pushed one end into your jack and the other into
the jack of the person you wanted. For as long as you talked, the two of you were joined by a piece
of copper. Nothing about the call was written down anywhere. It was in the cord.

Everything good and everything expensive about that arrangement comes from the same fact. It is
quick, because after the introduction you can just talk. And it means you must come back to the same
board every time, and somebody must keep your cord plugged in while you have gone to fetch a pen,
and nobody can wheel a new switchboard in at lunchtime without cutting off every conversation
running through the old one.

The other thing you can send is a postcard. It has the address on it, and who it is from, and what
it says, all on the same face. It refers to nothing. Whoever picks it up can act on it without
having been present for anything earlier, and if you write two and they arrive in different places,
both still work.

Today is that reframe, applied to the boundary day 12 argued for. It is not a stylistic preference
and it is not this curriculum's opinion: the current revision of the specification, `2026-07-28`,
deleted the introduction from the protocol outright, and its own front page now describes the base
protocol as *stateless, self-contained requests*. What complicates the day — and what an honest day
has to say out loud — is that the toolchain this project can install belongs to the era before that
change, and performs the introduction anyway. So you will build the postcard shape on purpose, watch
the switchboard shape fail in the way switchboards fail, and know exactly which of the two the
specification now requires.

## §2 The map

Two sections. The first is the idea and the code: what a session costs, and then this project's
boundary printed whole with one keyword argument doing all the work. The second is where you are
standing in time — the revision that deleted the handshake, and the dependency bound that is the
reason you are still on the wrong side of it.

### 1 · The reframe

*The mental model: a cord plugged into a switchboard, against a postcard that carries everything on
its face.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-reframe/1.1-the-call-you-had-to-keep-open.md) | The call you had to keep open | What is a session, and what does it cost you for ever? | foundation |
| [1.2](parts/01-the-reframe/1.2-one-flag-two-protocols.md) | One flag, two protocols | Which line of this project's boundary decides whether a stranger gets an answer? | working |

### 2 · The era you are standing in

*The mental model: the town's exchange went automatic; the works still has the board on the wall, and
somebody has to tell the new starter.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-era-you-are-standing-in/2.1-the-revision-that-deleted-the-handshake.md) | The revision that deleted the handshake | Which era of MCP does this project run, and which one is current? | working |
| [2.2](parts/02-the-era-you-are-standing-in/2.2-the-pin-that-had-to-be-argued-for.md) | The pin that had to be argued for | Why is `google-adk[mcp]` and not `google-adk`, and what breaks when it is not? | production |

## §3 Setup — run this

One dependency arrives today and it arrives with brackets on it. Everything runs from
`projects/02-parts-counter`. The two servers are started in separate terminals and **killed
afterwards** — they are for looking at, not for keeping.

```bash
cd projects/02-parts-counter

# today's dependency. The [mcp] extra is part 2.2's whole subject — it is what makes
# google-adk's own `mcp<2` bound apply to this project instead of sitting there inert.
uv add "google-adk[mcp]==2.8.0" "mcp==1.30.0"

# what the pinned SDK speaks — not what the specification currently says
uv run --frozen python -c "
import mcp.types as t
print('LATEST_PROTOCOL_VERSION    =', t.LATEST_PROTOCOL_VERSION)
print('DEFAULT_NEGOTIATED_VERSION =', t.DEFAULT_NEGOTIATED_VERSION)
"

# the bound, read out of the installed distribution rather than out of a changelog
uv run --frozen python -c "
from importlib.metadata import requires
for r in requires('google-adk'):
    if r.lower().startswith('mcp'): print(r)
"

# terminal 2 — the file as printed: stateless, on 8090
uv run --frozen python -c "
from parts_mcp.server import mcp
mcp.settings.port = 8090
mcp.run(transport='streamable-http')
"

# terminal 3 — the same file, one flag flipped: stateful, on 8091
uv run --frozen python -c "
from parts_mcp.server import mcp
mcp.settings.port = 8091
mcp.settings.stateless_http = False
mcp.run(transport='streamable-http')
"

# part 1.2 — the pair. No session header on either request.
curl -s -D - -X POST http://127.0.0.1:8090/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"curl","version":"0"}}}'

curl -s -X POST http://127.0.0.1:8090/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"stock_level","arguments":{"part_no":"BRK-0143"}}}'

curl -s -D - -X POST http://127.0.0.1:8091/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"curl","version":"0"}}}'

curl -s -w "\nHTTP %{http_code}\n" -X POST http://127.0.0.1:8091/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"stock_level","arguments":{"part_no":"BRK-0143"}}}'

# part 1.2 — the 406 you will meet before you meet anything else
curl -s -i -X POST http://127.0.0.1:8090/mcp \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'

# part 2.1 — the era gap, as an HTTP status code
curl -s -w "\nHTTP %{http_code}\n" -X POST http://127.0.0.1:8090/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -H 'MCP-Protocol-Version: 2026-07-28' \
  -d '{"jsonrpc":"2.0","id":8,"method":"tools/list"}'

# kill both servers, then confirm the project is exactly as you found it
git status --porcelain
```

`--frozen` is on every `uv run` for the reason `PRIMER.md` §2 gives: plain `uv run` repairs the
lockfile before running your command, so a check invoked that way reports on a repository its own
invocation created. `uv add` is the one command here that is *meant* to change the lockfile, which is
why it is not run with the flag.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `projects/02-parts-counter/parts_mcp/server.py` | part 1.2, whole, **full depth** — its first appearance in the curriculum |
| `projects/02-parts-counter/pyproject.toml` | part 2.2, as a marked diff against the version day 11 printed whole |

Two notes on what is deliberately **not** printed. Part 2.2 quotes a fragment of a dependency's own
source — `google/adk/tools/mcp_tool/__init__.py`, from this project's `.venv` — and that is evidence
rather than a file this project owns; it appears in no codemap and is never edited. And `server.py`
is printed **once**, here: day 14 takes its four tool bodies apart and does not reprint the file,
because a file printed twice in one project is a bug unless the second is a marked diff.

`CODEMAP.md` currently attributes `parts_mcp/server.py` to day 14. That row is now stale by one day
and is corrected when day 14 is written — the day is right and the index is behind it, which is the
standing rule for any disagreement between the two.

Parts 1.1 and 2.1 declare `prints: []` and that is correct rather than an omission. One is the
argument that makes the flag in 1.2 mean something, and the other is a statement about where the
specification currently stands; inventing a code fragment so that either would have something to
print is the kind of scaffolding this curriculum refuses.

## §5 Build brief

Nothing here creates a file in the project. `parts_mcp/server.py` already exists — this project's
reference implementation carries it — so today's reps are about serving it two ways, reading what
comes back, and breaking the dependency on purpose. Leave every `TODO(me)` unsolved.

| File | What it must do |
| --- | --- |
| `pyproject.toml` | `TODO(me)`: run `uv add "google-adk[mcp]==2.8.0" "mcp==1.30.0"`, then diff the file against what day 11 printed and say, in one sentence each, what the brackets do and what the second line does that the brackets alone would not. |
| `parts_mcp/server.py` | `TODO(me)`: before serving anything, predict what `initialize` returns on the stateless server. Write the prediction down. Then run it, and say which field surprised you and why the header you were looking for is absent. |
| the two servers | `TODO(me)`: serve the file both ways and send the *same* `tools/call` to both with no session header. Record both responses verbatim, then say what a load balancer in front of two stateful replicas would have to do to make the second one work. |
| the two servers | `TODO(me)`: hand a made-up `mcp-session-id` to **each** server. Say what each one does with it, and then find the sentence in the `2026-07-28` transports page that says which of those two behaviours is now required. |
| the transport | `TODO(me)`: cause the `406` by dropping the `Accept` header, read the whole message, and say why the transport cannot simply guess. Then say what it would take to monitor this endpoint from an ordinary uptime checker. |
| the era | `TODO(me)`: send `MCP-Protocol-Version: 2026-07-28` and read the list of versions the server offers back. Count them, and say which one of them the specification currently calls current. |
| the pin | `TODO(me)`: **the day's deliberate failure.** In a throwaway project — not this one — `uv add "google-adk==2.8.0" "mcp==2.2.0"`, then run both imports from part 2.2 and read both errors. Then add the brackets and watch the resolver refuse. Write down which of the three messages you would rather receive and why. |
| the record | `TODO(me)`: write, in your own words and without looking, the three costs of a session and the operational thing each one forbids. Bring the list to day 18, where "stateless container" is the D2 gate, and check it against what the container actually needs to be true. |

## §6 The check that must be able to fail

```text
cd projects/02-parts-counter
uv run --frozen python run.py check      # six green, 0 problem(s), exit 0
echo $?
git status --porcelain                   # must be empty once the servers are killed
cd ../.. && python p.py depth 13         # this day against the plan §5 contract
```

**How to make it go red on purpose — and the first one is the day's real failure.**

The first is the dependency, in a throwaway project so this one stays clean: `uv add
"google-adk==2.8.0" "mcp==2.2.0"` resolves without a murmur, and then
`from mcp.server.fastmcp import FastMCP` fails with a message that names the rename, the new import
line and the migration guide, while `from google.adk.tools.mcp_tool import McpToolset` fails saying
it cannot find a name you can see in the source. Two failures from one cause, one of them excellent
and one of them almost mute. Then add the brackets and watch a resolver refuse the same pair with
both bounds spelled out.

The second is the flag. Serve the same file with `mcp.settings.stateless_http = False` and send a
tool call with no session header: `{"code":-32600,"message":"Bad Request: Missing session ID"}` and
HTTP 400. Quote a session identifier the server has never issued and it is `Session not found` and
HTTP 404 instead. Both are the switchboard working exactly as designed.

The third is the header. Drop `Accept` and the transport answers `406 Not Acceptable` before it
parses anything, and says which two media types it wants.

The fourth is the era. Announce `MCP-Protocol-Version: 2026-07-28` — the revision the specification
calls current — and this boundary answers HTTP 400 and lists the four revisions it does know.

The fifth is for the document rather than the code: delete an `## In production` heading from any
part and run `python p.py depth 13`. It names the file and the missing section.

## §7 Request budget

**Zero model calls. Not "few" — zero.**

Nothing in this day goes anywhere near a provider. Every transcript is either an introspection of an
installed package, a `curl` at a local port, or a resolver refusing to build an environment. There is
still no agent in this project — `parts_counter/agent.py` is owed by day 17, once there is a boundary
for it to reach through — so there is nothing today that could make a request even by accident, and
`parts_counter/util/budget.py` is not exercised because nothing asks it for permission.

That matters for reading part 1.2 correctly. The four tool docstrings in `parts_mcp/server.py` are
written for a model, and the declarations MCP derives from them are real, and **nothing in this day
hands them to one.** The whole boundary is exercised by a command-line HTTP client. Keep that
separation in mind tomorrow, when the tool bodies get their sitting: a tool being *callable by a
model* and a tool *being called by a model* are different days.

The plan §9 counts requests **across the whole cast**, and from day 17 this project's number stops
being zero. The provider's own ceiling is not stated here and is not stated anywhere in this project:
the rate-limit page directs you to Google AI Studio rather than publishing a number, so
`PACKAGES.md` carries `TODO(me): read this project's live limits in Google AI Studio and paste them
here, with the date.` A number nobody can verify is worse than an honest gap.

## §8 Traps

- **`stateless_http` defaults to `False`.** Read from `FastMCP.__init__` today: `stateless_http: bool
  = False`. Omitting it is not neutrality — it silently chooses the switchboard, and the choice
  becomes visible for the first time on the day somebody runs two replicas.
- **The Accept header is not optional, and its absence is a `406`.** Every request to a Streamable
  HTTP endpoint needs `Accept: application/json, text/event-stream`. An ordinary uptime checker
  pointed at `/mcp` is red for ever and the server is perfectly well.
- **`serverInfo.version` is the SDK's version, not your project's.** `"version":"1.30.0"` in the
  `initialize` result is `mcp`'s. Nothing in `server.py` sets a version, and a client reading that
  field as a release of the parts server will be wrong in a way that is hard to unpick later.
- **A session identifier is minted per connection, not per server.** Two `initialize` calls against
  the same running process return two different identifiers. Nothing about one is derivable from the
  other or from anything you know.
- **`Missing session ID` is HTTP 400 and `Session not found` is HTTP 404, and they are different
  problems.** The first is a client that never introduced itself. The second is a client that
  introduced itself to a process that is now gone, or to the other replica.
- **`stateless_http` is inert under stdio.** A stdio server is one process per client, launched by
  that client. There is nothing for a session to be sticky to, so the flag changes nothing there; it
  is a property of the HTTP transport only.
- **The `[mcp]` extra is the whole pin.** `google-adk` 2.8.0 declares `mcp>=1.24,<2` three times and
  applies it zero times to a project that depends on plain `google-adk`. `uv add "mcp==2.2.0"` beside
  it resolves cleanly — sixty-seven packages, no warning — and breaks at import.
- **The ADK half of that break never mentions `mcp`.** `google/adk/tools/mcp_tool/__init__.py` wraps
  ten imports in one `try`, catches `ImportError`, logs the cause at `DEBUG`, and leaves
  `__all__ = []`. The error you see names `McpToolset`. To see the real cause, import the module by
  its full path: `google.adk.tools.mcp_tool.mcp_toolset`.
- **The SDK's own 2.x error is the good one — do not lose it.** `mcp/server/fastmcp.py` still exists
  in 2.x purely to raise a message naming the rename, the replacement import and the migration guide.
  If you meet it, you are one line from the answer.
- **`2025-11-25` is not the current specification revision.** It is `mcp.types.LATEST_PROTOCOL_VERSION`
  — the newest revision *this installed wheel* implements. The current revision is `2026-07-28`, and
  the two facts live in completely different places.
- **Do not write a `2026-07-28` message shape into this project.** `_meta`, `resultType`,
  `server/discover`, `UnsupportedProtocolVersionError` — none of them exist in `mcp` 1.30.0. Quoting
  them, labelled, is right; pasting them into code produces something that cannot run and a
  transcript that could only be invented. ADR-0005 decision 5.
- **Day 9's `Session` and today's session are not the same thing.** One is an ADK object holding a
  stored conversation, addressed by name. The other is a connection-scoped identity the transport
  mints. An agent can hold the first while talking to a boundary that has none of the second, and by
  day 17 that is exactly what this project does.
- **Kill the servers.** Two `uvicorn` processes left listening on 8090 and 8091 will make tomorrow's
  first command fail with `only one usage of each socket address … is normally permitted`, and the
  error will look like it is about tomorrow's code.

## §9 Verified today

Everything in this row set was observed on this machine on 2026-09-10 — uv 0.12.3, CPython 3.12.12,
google-adk 2.8.0, mcp 1.30.0 in the project and mcp 2.2.0 in a throwaway project built solely to
cause part 2.2's failure.

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| The current specification revision | `https://modelcontextprotocol.io/docs/learn/versioning` | 2026-09-10 | "The **current** protocol version is **2026-07-28**." |
| The reframe, in the specification's own words | `https://modelcontextprotocol.io/specification/2026-07-28` | 2026-09-10 | base protocol: "JSON-RPC message format · Stateless, self-contained requests · Per-request capability negotiation" |
| The handshake was removed | `…/2026-07-28/changelog` | 2026-09-10 | "Make MCP stateless: remove the `initialize`/`notifications/initialized` handshake." |
| Sessions and the header were removed | `…/2026-07-28/changelog` | 2026-09-10 | "Remove protocol-level sessions and the `Mcp-Session-Id` header from the Streamable HTTP transport. List endpoints … no longer vary per-connection." |
| There is no negotiation any more | `…/2026-07-28/basic/versioning` | 2026-09-10 | "**There is no negotiation handshake.** Every request carries its protocol version…" |
| The two eras, defined | same page | 2026-09-10 | Modern = per-request metadata, `2026-07-28` and later; Legacy = an `initialize` handshake, `2025-11-25` and earlier |
| The lifecycle page is gone | `…/2026-07-28/basic/lifecycle` | 2026-09-10 | resolves to `…/2026-07-28/basic/versioning`; there is no lifecycle page at this revision |
| What a modern server does with a session id | `…/2026-07-28/basic/transports/streamable-http` | 2026-09-10 | "An `Mcp-Session-Id` header on a request: ignore it, and do not mint or echo session IDs." |
| What the pinned SDK speaks | `mcp.types.LATEST_PROTOCOL_VERSION`, `DEFAULT_NEGOTIATED_VERSION` | 2026-09-10 | `2025-11-25` and `2025-03-26`, read from the installed wheel |
| The session flag's default | `inspect.signature(FastMCP.__init__)` | 2026-09-10 | `stateless_http: bool = False` — and `max_sessions: int \| None = 10000`, `session_idle_timeout: float \| None = 1800` |
| The transports this SDK accepts | `inspect.signature(FastMCP.run)` | 2026-09-10 | `transport: Literal['stdio', 'sse', 'streamable-http'] = 'stdio'` |
| Stateless `initialize` mints nothing | `curl -D -` against `127.0.0.1:8090/mcp` | 2026-09-10 | HTTP 200, `serverInfo` `parts-mcp` / `1.30.0`, and **no `mcp-session-id` header** |
| Two fresh connections, no session, both answered | two `tools/call` requests, no `initialize` | 2026-09-10 | `stock_level` for `BRK-0143` and `bin_location` for `BLT-0310` both returned results with `isError: false` |
| The stateless server ignores a session id it is handed | `mcp-session-id: 000…0` to `:8090` | 2026-09-10 | answered normally — exactly what the `2026-07-28` transports page requires |
| Stateful mints one, then demands it | the same file with `stateless_http = False`, on `:8091` | 2026-09-10 | `mcp-session-id: 8afe8ea126254dab906853bdfe33751b`, then `{"code":-32600,"message":"Bad Request: Missing session ID"}` with HTTP 400 |
| The identifier is per connection | a second `initialize` against the same process | 2026-09-10 | `mcp-session-id: 2a4c870a3a9740cb9e5c400bfe0d66bd` — a different value from the same server |
| An unknown session identifier | `mcp-session-id: 000…0` to `:8091` | 2026-09-10 | `{"code":-32600,"message":"Session not found"}` with HTTP 404 |
| The Accept header is required | POST with no `Accept` to `:8090` | 2026-09-10 | HTTP 406, `"Not Acceptable: Client must accept both application/json and text/event-stream"` |
| The era gap, as a status code | `MCP-Protocol-Version: 2026-07-28` to `:8090` | 2026-09-10 | HTTP 400, `"Unsupported protocol version: 2026-07-28. Supported versions: 2024-11-05, 2025-03-26, 2025-06-18, 2025-11-25"` |
| ADK's bound, and where it lives | `importlib.metadata.requires('google-adk')` | 2026-09-10 | `mcp>=1.24,<2` under `extra == "all"`, `"mcp"` and `"test"` — and nowhere in the base requirements |
| The bare pair resolves cleanly | `uv add "google-adk==2.8.0" "mcp==2.2.0"` in a throwaway project | 2026-09-10 | `Resolved 67 packages in 1.27s`, no conflict, no warning |
| The 2.x import error | `from mcp.server.fastmcp import FastMCP` under mcp 2.2.0 | 2026-09-10 | raised from `mcp/server/fastmcp.py` line 16 — the file exists solely to name the rename, the replacement import and the migration guide |
| The silent half | `from google.adk.tools.mcp_tool import McpToolset` under mcp 2.2.0 | 2026-09-10 | `ImportError: cannot import name 'McpToolset' from 'google.adk.tools.mcp_tool'`, naming `__init__.py` and never `mcp` |
| The real cause, by full path | `from google.adk.tools.mcp_tool.mcp_toolset import McpToolset` | 2026-09-10 | `mcp_toolset.py` line 39, `from mcp.shared.session import ProgressFnT` → `ModuleNotFoundError` |
| The swallow, in the source | `google/adk/tools/mcp_tool/__init__.py` in this project's `.venv` | 2026-09-10 | `__all__ = []` before a single `try` over ten imports, `except ImportError as e` logging the cause at `DEBUG` |
| The brackets make the resolver refuse | `uv add "google-adk[mcp]==2.8.0" "mcp==2.2.0"` | 2026-09-10 | "No solution found … we can conclude that your project's requirements are unsatisfiable", naming both bounds |
| The project survived every transcript | `git status --porcelain projects/` | 2026-09-10 | clean — every server was killed and the failure was caused in a throwaway project, never in this one |

## §10 Ledger & commit

**`docs/PROGRESS.md`:**

```text
| 13 | 2026-09-10 | MC-02 | 4 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the terms this day defined for the first time. `Stateless` is **not** among
them: it was defined on day 4 part 1.3 and is linked, not redefined. Nor is `Session` — day 6 part
2.1 and day 9 part 1.1 own the ADK object, and today's protocol-level thing is given its own term
precisely so the two are never confused:

```text
| MCP | The Model Context Protocol: a JSON-RPC protocol by which a program exposes tools, resources and prompts to a model's client, so the tool lives in its own process instead of inside the agent. Its versions are dated revisions, and which one you speak is a fact about your installed SDK. | day 13 part 1.1 | the protocol, Model Context Protocol |
| Protocol revision | A dated version of a specification's rules — `2025-06-18`, `2025-11-25`, `2026-07-28` — named by date rather than by number. The *current* revision is the one the maintainers say is current, which is not necessarily the newest one that exists. | day 13 part 2.1 | the spec version, the revision |
| Protocol session | Connection-scoped state a server keeps about one client, minted by the transport and quoted back on every later request. Distinct from an ADK Session, which is a stored conversation your code addresses by name; an agent can hold one while talking to a boundary that has none of the other. | day 13 part 1.1 | `Mcp-Session-Id`, the session header |
| Protocol era | MCP's own name for the two sides of the `2026-07-28` line. **Modern** revisions carry version, identity and capabilities as per-request metadata; **legacy** revisions establish a session with an `initialize` handshake. This project runs legacy, by one revision. | day 13 part 2.1 | modern and legacy |
| Extra (packaging) | An optional dependency set a distribution declares, switched on by naming it in brackets — `google-adk[mcp]`. Requirements declared under an extra you did not ask for are inert: published, correct, and applied to nothing. | day 13 part 2.2 | optional dependency, `[…]` |
```

**`docs/SOURCES.md`** — the specification is cited by revision throughout this day, so it earns a
row. Every URL below was fetched live on the date in the row:

```text
| `spec:mcp-2026-07-28` | Model Context Protocol specification, revision 2026-07-28 | 2026 | https://modelcontextprotocol.io/specification/2026-07-28 | 2026-09-10 | day 13 part 2.1 | day 13 parts 1.1, 1.2, 2.1 |
```

**`projects/02-parts-counter/PACKAGES.md`** — already carries today's rows, appended when the
freshness check was run: `mcp` 1.30.0, the wire revision `2025-11-25`, the current specification
revision `2026-07-28`, and the section explaining why the pin is 1.30.0 and not 2.2.0. Nothing to
add; part 2.2 is that section, taught.

**`docs/PINS.md`** — nothing to add. Every version today belongs to a project rather than to the
authoring repository, and `PACKAGES.md` is where a project's pins live (plan §9).

**`docs/adr/`** — nothing new. `ADR-0005-mcp-era-gap-and-the-1x-pin.md` was accepted for this day and
governs it; part 2.1 is its decision 3 and decision 4 carried out, and part 2.2 is its decision 1.

**Commit:**

```text
day 13: P02 Parts Counter · 3 — MCP 2026: the stateless core, and the phone-call to web reframe — closes MC-02
```
