---
project: "P02 Parts Counter"
day: 17
phase: P02
title: "P02 Parts Counter · 7 — The client side: connecting the agent to a tool that now lives elsewhere"
ids: [MC-06]
kind: mechanism
deploy_tier: D2
plan_version: "v3.1.0"
parts: 4
files_printed:
  - "projects/02-parts-counter/parts_counter/util/mcp.py"
  - "projects/02-parts-counter/parts_counter/agent.py"
  - "projects/02-parts-counter/run.py"
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** the same server over two transports, and the rule that a stray `print()` on stdout
> corrupts the protocol stream.
> **Today:** the near side. The agent stops importing its tools and starts asking for them, and the
> asking is a thing that can fail.
> **Tomorrow:** Ship D2 — the stateless container, secrets injected and not baked, and the cold
> clone.

## §1 The scene

For two projects your tools were functions you could open. `find_part` was a name your editor could
jump to, and if you deleted it the program said so before it ran a line. Today you swap that for a
telephone number.

You are no longer walking the aisles. You do not know what is on the shelves, and you are not
supposed to — that is the whole point of the hatch day 14 built. You know how to ring the parts
desk, and you find out what they stock by asking. That is better every single day, for the reasons
day 12 spent a sitting on: one owner, one writer, a record anybody can read, and a boundary you can
deploy on its own.

It is better every day **until the phone is engaged**, and the interesting thing is what that does
to you rather than to the phone. An empty shelf used to be a fact you tripped over. Now the shelves
belong to somebody else and your only symptom is a line that rings out. Nothing tells you the
stockroom is shut; you simply get no answer, and — this is the part worth staying with — an agent
that gets no answer does not stop. It has been told it is a parts counter. It will count parts.

## §2 The map

Two sections. The first is the mechanism: what replaces the import, and what a call looks like when
it leaves the process. The second is the agent that now sits on this side of the line, and the
failure that a list of imported functions could never have had.

### 1 · A list you no longer write

*The mental model: the tool list stopped being a decision made when the file was written and became
a question answered when the agent runs.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-a-list-you-no-longer-write/1.1-the-toolset-that-asks.md) | The toolset that asks | What replaces `tools=[find_part, ...]`, and what does that buy and cost? | foundation |
| [1.2](parts/01-a-list-you-no-longer-write/1.2-a-call-that-leaves-the-process.md) | A call that leaves the process | What actually happens between asking for a tool and getting a value back? | working |

### 2 · The agent on this side

*The mental model: the agent barely changed. What changed is what has to be true elsewhere for it to
work, and nothing in this project checks that.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-agent-on-this-side/2.1-one-toolset-not-four-functions.md) | One toolset, not four functions | Which line of P01's agent changed, and which lines deliberately did not? | working |
| [2.2](parts/02-the-agent-on-this-side/2.2-the-tools-that-were-not-there.md) | The tools that were not there | When does a missing boundary become your problem, and who finds out? | production |

## §3 Setup — run this

Nothing new to install: `google-adk[mcp]` and `mcp` were pinned on day 13 and the boundary was built
on day 14. Everything below was run on this machine today and what it reported is in §9.

```bash
cd projects/02-parts-counter

# part 1.2 — the client launches the server itself, so this needs nothing running
uv run --frozen python run.py probe

# part 2.1 — the agent, built but not run. Contacts nothing.
uv run --frozen python -c "
import warnings; warnings.filterwarnings('ignore')
from parts_counter.agent import build_counter
a = build_counter()
print(a.name, [type(t).__name__ for t in a.tools])
"

# the gate, unchanged
uv run --frozen python run.py check
```

No key is needed for any of it. The one command in this project that would contact a provider is
`parts_counter.agent.ask`, and this day does not run it.

## §4 Files this day prints

Three, and one of them is a two-line addition to a file day 11 printed whole.

| File | Printed by |
| --- | --- |
| `projects/02-parts-counter/parts_counter/util/mcp.py` | part 1.1, whole |
| `projects/02-parts-counter/run.py` | part 1.2, as a marked diff adding `probe` against the file day 11 printed |
| `projects/02-parts-counter/parts_counter/agent.py` | part 2.1, whole |

Part 2.2 prints nothing. Its subject is what these three do when the thing on the other side of the
boundary is absent, and adding a file to it would have made the day worse.

## §5 Build brief

| File | What it must do |
| --- | --- |
| `parts_counter/util/mcp.py` | `TODO(me)`: type it. Before running anything, say which of the two connection shapes launches a process and which assumes one is already there — and what each implies about who is responsible for the server being up. |
| `parts_counter/util/mcp.py` (the interpreter) | `TODO(me)`: say why `command=sys.executable` and not `command="python"`. Then break it — set it to `"python"` — and say what would have to be true on a machine for that to work and what would have to be true for it to fail. |
| `parts_counter/agent.py` | `TODO(me)`: type it, then diff it by eye against `projects/01-ask-desk/ask_desk/agent.py`. List every line that is the same and the one that is not, and for each *same* line say which earlier day decided it. |
| the bound | `TODO(me)`: find where `max_llm_calls` gets its value in this project and trace it back to the constant it comes from. Then say what would happen if that argument were dropped, and what number would take over. |
| `run.py probe` | `TODO(me)`: run it. Then run it again with the server's `print()` from day 16 reinstated, and say which of the two failures you would rather debug. |
| the failure rep | `TODO(me)`: cause both failures from part 2.2 — a stdio command that cannot start, and an HTTP URL with nothing behind it. Record the exception type and message for each. Say which one you could diagnose *without* reading the subprocess's stderr, and what that implies about a client that discards it. |
| the gap | `TODO(me)`: `run.py check` has six checks and none goes red when the boundary is down. Write down what a seventh would have to do — what it would call, what it would assert, and whether it belongs in `check` at all or in a readiness endpoint. Do not implement it; day 8 of this project owes it. |

## §6 The check that must be able to fail

```text
cd projects/02-parts-counter
uv run --frozen python run.py probe        # must list four tools and return one result
uv run --frozen python run.py check        # six checks, all green
echo $?                                    # 0
cd ../.. && python p.py depth 17           # this day against the plan §5 contract
```

**How to make it go red on purpose — three ways, and the third is the day's real one.**

The first is the launcher. Change `args` in `over_stdio` to name a module that does not exist and
run `probe`: `get_tools()` raises `ConnectionError: Failed to create MCP session: Failed to create
MCP session: Connection closed`, and the actual reason — `No module named …` — appears only on the
subprocess's stderr.

The second is the address. Point `over_http` at a port nothing is listening on. The same
`ConnectionError`, a different message ending `All connection attempts failed`, and this time no
stderr to rescue you, because nothing was ever launched.

The third is not a way to make anything go red, and that is the point. **Delete the boundary
entirely and `run.py check` stays green.** Six checks, `0 problem(s)`, exit `0`, with the tools this
agent depends on unreachable. Part 2.2 is about that gap; §5's last rep asks you to write down what
would close it; day 8 of this project owes the eval that does.

For the document itself: delete an `## In production` heading from any part and run
`python p.py depth 17`; it names the file and the missing section.

## §7 Request budget

**Zero model calls.** Every command in this day runs against the boundary or constructs objects
without contacting anything: `probe` launches the server as a subprocess and speaks MCP to it,
`build_counter()` touches nothing at all, and both failure reps fail before any model is reached.

The one path that would call a provider is `parts_counter.agent.ask`, and it is not run here.
There is no working `GOOGLE_API_KEY` on this machine, so **no model answer appears anywhere in this
day**; the places one would go are marked `TODO(me)` with the exact command.

When it is run, the count is what `run_config()` sets: at most `Budget.max_per_turn` model calls
for one question, which is **6**, passed to ADK's `max_llm_calls` rather than inheriting its default
of 500. The provider's own ceiling is not stated because it is not published —
`TODO(me): read this project's live rate limits in Google AI Studio and record them in PACKAGES.md,
with the date.`

## §8 Traps

- **Three moments, and only the third touches anything.** Import succeeds, construction succeeds,
  and `get_tools()` is where a missing server becomes your problem. Every check that stops before
  the third moment passes on a machine with no boundary at all.
- **`ConnectionError` covers two very different causes.** *The server exited on startup* and *there
  is no server* raise the same type; the only signal separating them is prose inside the message —
  `Connection closed` against `All connection attempts failed`.
- **The message nests inside itself.** `Failed to create MCP session: Failed to create MCP session:
  …` is a wrapped-and-re-raised prefix. Cosmetic, and the fastest way to recognise this failure in
  an old log.
- **The real reason is on the subprocess's stderr.** Day 16 quoted the stdio transport telling
  clients they "SHOULD NOT assume `stderr` output indicates error conditions". That is the same
  stream carrying `No module named …`. A client that discards it turns a one-line diagnosis into an
  afternoon.
- **The failure is retried before it is surfaced**, so one bad server produces two of every line in
  the log.
- **`connection_params` is keyword-only.** `McpToolset(StdioConnectionParams(...))` is a `TypeError`;
  the `*` in the signature is deliberate.
- **`MCPToolset` is a deprecated alias.** Python uses `McpToolset`; the capitalised spelling emits a
  `DeprecationWarning`, and the version in the framework's own documentation is from its TypeScript
  SDK.
- **`StdioServerParameters` is not an ADK class.** It comes from the `mcp` SDK, and mixing that up
  produces an import error that names the wrong package.
- **`command="python"` is the P00 day 1 failure, one process removed.** The bare name resolves
  through `PATH` to whatever a shell finds; `sys.executable` is the interpreter that has this
  project's dependencies. A server that starts and cannot import `mcp` is this trap.
- **`over_http` does not validate its URL.** A typo in the port is invisible until the first
  `get_tools()`, and then reports as *nothing is listening*, which is true and unhelpful.
- **An agent with no tools still answers.** It has an instruction; it will follow it. The number it
  reports will look exactly like a correct one.
- **`get_tools()` succeeding is not the same claim as getting the tools you expected.** A boundary
  at the wrong version can return a renamed tool and nothing anywhere objects.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| Tools cross a real process boundary | `uv run --frozen python run.py probe` | 2026-09-10 | four tools listed, one call returned; the server's own `Processing request of type ListToolsRequest` on stderr proves a separate process answered |
| A tool call, including a write, returns through the client | `stock_level`, then `adjust_stock` ±2 on `BLT-0310` over stdio | 2026-09-10 | `before`/`after` moved 0→2 and back; the value came back wrapped in `content` / `structuredContent` / `isError` |
| The agent builds against the boundary | `build_counter()` | 2026-09-10 | `parts_counter`, model `gemini-3.8-flash`, `tools: ['McpToolset']`, bound `6` |
| Building the agent contacts nothing | the same call with no server running | 2026-09-10 | returned normally; nothing was launched and no port was opened |
| A stdio server that cannot start | `args=['-m','parts_mcp.no_such_module']` | 2026-09-10 | import and construction fine; `get_tools()` raised `builtins.ConnectionError: Failed to create MCP session: Failed to create MCP session: Connection closed`, with `No module named parts_mcp.no_such_module` on the subprocess's stderr, twice |
| An HTTP server that is not there | `over_http('http://127.0.0.1:8099/mcp')` | 2026-09-10 | same type, different tail: `… All connection attempts failed`, and no stderr at all |
| `MCPToolset` is deprecated in Python | `google-adk` 2.8.0 source, `mcp_toolset.py` | 2026-09-10 | `class MCPToolset(McpToolset): """Deprecated name, use \`McpToolset\` instead."""`, emitting `DeprecationWarning` |
| `connection_params` is keyword-only | the same source, `McpToolset.__init__` | 2026-09-10 | `def __init__(self, *, connection_params: (StdioServerParameters \| StdioConnectionParams \| SseConnectionParams \| StreamableHTTPConnectionParams), …)` |
| The framework's MCP docs moved | `https://adk.dev/tools/mcp-tools/` | 2026-09-10 | redirects to `https://adk.dev/tools-custom/mcp-tools/` |
| The project gate is unaffected by all of it | `uv run --frozen python run.py check` | 2026-09-10 | six green, `0 problem(s)`, exit `0` — with no boundary running |

## §10 Ledger & commit

**`docs/PROGRESS.md`:**

```text
| 17 | 2026-09-10 | MC-06 | 4 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the terms this day defined for the first time:

```text
| Toolset | An object given to an agent in place of a list of functions, which fetches the available tools from a server when the agent runs. The tool list stops being a decision made when the file was written and becomes a question answered at run time. | day 17 part 1.1 | a tool provider, `McpToolset` |
| MCP client | The near side of the boundary: the code that launches or connects to a server, performs the handshake, asks for the tool list, and forwards each call. In this project it is nine lines and two functions. | day 17 part 1.1 | the client side |
| Connection params | The object that says how to reach a server — a command and arguments to launch, or a URL to connect to — and nothing about what the server can do. Validated when constructed; not tested until the first call. | day 17 part 1.1 | `StdioConnectionParams`, `StreamableHTTPConnectionParams` |
```

**`projects/02-parts-counter/CODEMAP.md`** — three rows, already present from day 14's correction:
`parts_counter/util/mcp.py` and `parts_counter/agent.py` are attributed to this day, and `run.py`
gains the `probe` subcommand. `evals/` remains owed by day 18, and part 2.2 is the argument for why
that debt is real rather than tidy-up.

**`docs/PINS.md`** — nothing to add. The two packages this day exercises were pinned on day 13 and
are recorded in this project's own `PACKAGES.md`, which is where a project's pins live.

**`docs/SOURCES.md`** — nothing to add. This day cites the framework's documentation and its shipped
source; neither is a record with a resolvable identifier, and both are dated in §9.

**Commit:**

```text
day 17: P02 Parts Counter · 7 — The client side: connecting the agent to a tool that now lives elsewhere — closes MC-06
```
