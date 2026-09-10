---
project: "P02 Parts Counter"
day: 15
phase: P02
title: "P02 Parts Counter · 5 — Lifecycle, stateless-first: the old handshake as history"
ids: [MC-04]
kind: concept
deploy_tier: D2
plan_version: "v3.1.0"
parts: 4
files_printed: []
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** a server with four tools, a store that survives two writers, and a result envelope
> you can read.
> **Today:** the conversation that happens *before* any of those tools can be reached — and the
> specification revision that deleted that conversation entirely.
> **Tomorrow:** transports — the same server over stdio and over Streamable HTTP, and what standard
> error is really for.

## §1 The scene

There is a hut by the gate of every building site. You do not walk past it. You give your name, you
say what trade you are, and the person behind the desk tells you what is in force today: hot work
suspended, the east stair closed, the scaffold on the north face tagged. Then you sign the book and
go to work. Nothing was built during that exchange, and the exchange is the reason the rest of the
day works, because afterwards neither of you has to guess.

Your parts server has a hut. Before any tool is reachable, three messages cross the pipe: the client
gives its name and says what it can do, the server answers with what *it* can do and which edition
of the rules will govern the connection, and the client says it has read the reply. Today you type
all three by hand, with no client library anywhere, and read the answers with your own eyes.

And then, one year, the site replaces the sign-in book with a badge you carry — a card that states
who you are and which permits you hold, read at every door instead of once at the gate. The hut is
not made quieter. It is removed, and the sign that pointed at it now points at the badge office.
That happened to this protocol on 2026-07-28, and the honest half of today is looking straight at
it: you will learn a mechanism by running it, and then read the line that deleted it. The reason
this project still performs the handshake is a package bound, not a belief, and the reason is
written down.

## §2 The map

Two sections, and they follow the two things the specification says the handshake is *for*. The
first section is the exchange itself and the promises made in it. The second is the one promise that
is a date — which edition are we both reading — and what happened when the protocol decided the
whole arrangement was the wrong shape.

### 1 · The conversation before the conversation

*The mental model: the hut by the gate. Nothing is built there, and everything afterwards depends on
what was said.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-conversation-before-the-conversation/1.1-three-messages-before-any-work.md) | Three messages before any work | What actually crosses the pipe before a tool can be called, and why one of the three expects no reply? | foundation |
| [1.2](parts/01-the-conversation-before-the-conversation/1.2-what-each-side-admits-to.md) | What each side admits to | What is a capability, what does `listChanged: false` promise, and why can a stateless protocol not hold one? | working |

### 2 · Negotiation, and its retirement

*The mental model: the edition date on the board — and then the badge that replaced the board.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-negotiation-and-its-retirement/2.1-the-version-both-sides-can-speak.md) | The version both sides can speak | What happens when the client asks for a version the server does not know — and who is responsible for noticing? | working |
| [2.2](parts/02-negotiation-and-its-retirement/2.2-the-handshake-as-history.md) | The handshake as history | The current revision removed all of this. What breaks when you skip the handshake, and what does that tell you it was for? | production |

## §3 Setup — run this

**Nothing to install.** Every command today runs against the server day 14 already built, with the
packages day 11 and day 13 already pinned: `google-adk[mcp]==2.8.0`, `mcp==1.30.0`. No file in
`projects/` is created, edited or deleted by this day.

Run everything from the project folder, and keep `--frozen` on every `uv run` for the reason day 3
gave — a check invoked through a tool that repairs the repository reports on a repository the
invocation just created.

```bash
cd projects/02-parts-counter

# part 1.1 — the whole handshake, by hand
printf '%s\n%s\n%s\n' \
 '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"by-hand","version":"0"}}}' \
 '{"jsonrpc":"2.0","method":"notifications/initialized"}' \
 '{"jsonrpc":"2.0","id":2,"method":"tools/list"}' \
 | uv run --frozen python -m parts_mcp.server

# part 2.1 — what the pinned SDK speaks
uv run --frozen python -c "
import mcp.types as t
print('LATEST_PROTOCOL_VERSION    =', t.LATEST_PROTOCOL_VERSION)
print('DEFAULT_NEGOTIATED_VERSION =', t.DEFAULT_NEGOTIATED_VERSION)
"

# part 2.2 — the deliberate failure: no handshake at all
printf '%s\n' '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' \
 | uv run --frozen python -m parts_mcp.server

# and the day against the contract
cd ../.. && python p.py depth 15
```

Every stdio server started today exits when its standard input closes, which the pipe does at the
end of each command. Nothing is left listening, and no port is opened.

## §4 Files this day prints

**None. This table is deliberately empty, and the emptiness is the day's shape.**

| File | Printed by |
| --- | --- |
| — | — |

`parts_mcp/server.py` was printed whole by **day 13**, at
`days/02-parts-counter/day-13-mcp-stateless-core/`, which owns the stateless core and the
phone-call-to-web reframe. Its tool bodies, its store, the `Tool` object and the result envelope
belong to **day 14**, at `days/02-parts-counter/day-14-server-skeleton-first-tool/`. Today's subject
is not a file at all: it is the **conversation that happens before any of that code is reached**, and
the artefacts of that conversation are JSON messages on a pipe, not lines in a module.

That is why every part carries `prints: []`. Reprinting a file this project has already printed would
break the completeness rule's other edge — a file printed twice in one project is a bug unless the
second is a marked diff — and there is no diff to mark, because nothing in `projects/` changes today.
`CODEMAP.md` gains no row from this day, and that is correct.

## §5 Build brief

Nothing is typed into `projects/` today. The reps are all *drive it and read it*, and the file they
write to is `days/02-parts-counter/day-15-lifecycle-handshake-history/lab/`.

| File | What it must do |
| --- | --- |
| `lab/handshake-notes.md` | `TODO(me)`: run the three-message handshake, then run it again with the notification and `tools/list` **swapped**, and again with an `"id"` added to the notification. Record what changed in each and what did not. |
| `lab/handshake-notes.md` | `TODO(me)`: send `resources/read` for any URI after a good handshake. Predict `-32601` or a result **before** running it, then say which flag in the `initialize` result should have told you. |
| `lab/version-notes.md` | `TODO(me)`: offer `2025-03-26` and `2025-11-25` in turn. Predict echo or counter-offer before each run, and say what the pair tells you about which revisions this SDK implements as against which one it prefers. |
| `lab/version-notes.md` | `TODO(me)`: write the one `if` that the `2025-06-18` rule *"the client SHOULD disconnect"* reduces to, as pseudocode against the `initialize` result. Do not wire it into the project — day 17 owns the client. |
| `lab/era-notes.md` | `TODO(me)`: skip the handshake, read both streams separately, and write down in one sentence what your client would have to do differently to survive a modern (`2026-07-28`) server. |

## §6 The check that must be able to fail

```text
cd projects/02-parts-counter
uv run --frozen python run.py check     # unchanged today, and must stay green
uv run --frozen python -m pytest tests -q
cd ../.. && python p.py depth 15        # this day against the plan §5 contract
```

**How to make it go red on purpose — and today the interesting one is not `run.py`.**

The day's deliberate failure is part 2.2 and it needs no edit to any file: send `tools/list` into the
server with no handshake in front of it. The server answers
`{"code":-32602,"message":"Invalid request parameters","data":""}` on standard output, writes
`Failed to validate request: Received request before initialization was complete` on standard error,
and **exits `0`**. That last fact is the one to sit with: nothing in the process's verdict says a
request was refused.

Two more, both real. Leave `protocolVersion` out of the `initialize` params and the server logs
twenty-eight validation errors for one missing field, of which the useful one is second. Send
`protocolVersion` as `null` and it logs two — one for `str`, one for `int` — which is how you learn
the field accepts either, and therefore that an unquoted `20250618` is silently accepted and
countered.

For the document itself: delete a `## In production` heading from any part and run
`python p.py depth 15`; it names the file and the missing section.

## §7 Request budget

**Zero model calls. No provider is contacted by any command in this day.**

Every command here speaks to a Python subprocess over a pipe. No agent runs, no `Runner` is
constructed, no `google-genai` client is built, and `GOOGLE_API_KEY` is never read. The whole day
lives below the model: this is the protocol layer, and the protocol has never heard of a model.

Stating the zero is not a formality. Plan §9 counts requests **across the whole cast**, and the habit
of writing the number down on a day that spends nothing is what makes the number credible on a day
that spends a lot. From day 17, when the agent is wired to the boundary, the count stops being zero
and the budget in `parts_counter/util/budget.py` starts doing work.

The provider's per-model ceiling is still **not published**: the rate-limit page directs you to
Google AI Studio and states that specified limits are not guaranteed. So the ceiling here is not a
number — it is `TODO(me): read this project's live limits in Google AI Studio and paste them into
PACKAGES.md, with the date.` See `docs/adr/ADR-0004-generatecontent-by-hand-and-unpublished-limits.md`.

## §8 Traps

- **`serverInfo.version` is not your version.** This project never declares one, so the SDK fills the
  field with its own — `1.30.0`. Every log line that quotes it as "the parts server version" is
  quoting `mcp`.
- **A notification has no `id`, and that is not an omission.** No `id` means no reply is possible.
  Anything that must be acknowledged cannot be a notification.
- **`listChanged: false` does not mean the list never changes.** It means you will not be told when it
  does. The correct response is to decide whether staleness matters and poll if it does.
- **An empty list is not an error.** `{"prompts":[]}` means *I do this and have none*; `-32601` means
  *I do not do this*. A client that treats both as failure refuses to work with a healthy server.
- **The server does not refuse an unknown version — it counters.** Offer `2024-01-01` or `9999-12-31`
  and you get `2025-11-25` and a working connection. The only protection is a client-side check that
  the specification writes as **SHOULD**.
- **`2025-11-25` is the SDK's ceiling, not the current revision.** The current revision is
  `2026-07-28`. Three dates float around this project — the one you offer, the one the SDK tops out
  at, and the one the specification is on — and nothing checks any of them against another.
- **`protocolVersion` accepts a string *or* an integer.** An unquoted `20250618` validates, matches
  nothing, and is answered with the usual counter-offer. The error you would want never arrives.
- **`-32602 Invalid request parameters` is the SDK's catch-all.** A skipped handshake, a missing
  `protocolVersion` and a `null` one all produce it, all with `data: ""`. The sentence that
  distinguishes them is on standard error, which the stdio transport tells clients they may ignore.
- **The 1.x to 2.x break is still live and still silent.** `google-adk` 2.8.0 requires `mcp>=1.24,<2`
  behind an extra, so `uv add "mcp==2.2.0"` beside a bare `google-adk` resolves cleanly and fails at
  import naming `McpToolset` rather than the version. This project depends on `google-adk[mcp]`
  precisely so the bound is real. See `PACKAGES.md` and ADR-0005.
- **Do not copy a `2026-07-28` shape into this project.** `_meta`, `server/discover`,
  `subscriptions/listen`, `resultType`, `-32022` — quoted as what comes next, never pasted in. This
  stack cannot produce any of them.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| The whole handshake, by hand | three messages piped into `python -m parts_mcp.server` | 2026-09-10 | `initialize` answered with `protocolVersion 2025-06-18`, four capability keys, `serverInfo.name parts-mcp`, `serverInfo.version 1.30.0`; `tools/list` answered after it |
| A notification draws no reply | `initialize` + `notifications/initialized`, stdout line count | 2026-09-10 | `1` line of stdout for two messages sent |
| `subscribe: false` is real | `resources/subscribe` after a good handshake | 2026-09-10 | `{"id":4,"error":{"code":-32601,"message":"Method not found"}}`, and `prompts/list` answered normally straight afterwards |
| A declared feature with nothing in it | `prompts/list` on this server | 2026-09-10 | `{"prompts":[]}` — an empty list, not an error |
| Version negotiation, three offers | `2025-06-18`, `2024-01-01`, `9999-12-31` | 2026-09-10 | echoed `2025-06-18`; countered `2025-11-25` for both of the others |
| Where `2025-11-25` comes from | `mcp.types.LATEST_PROTOCOL_VERSION` on this machine | 2026-09-10 | `LATEST_PROTOCOL_VERSION = 2025-11-25`, `DEFAULT_NEGOTIATED_VERSION = 2025-03-26` |
| Ignoring the counter-offer still works | offered `2024-01-01`, then `tools/call stock_level` | 2026-09-10 | a full, correct tool result; nothing warned, nothing logged a downgrade |
| `protocolVersion` accepts a number | `"protocolVersion":20250618` | 2026-09-10 | accepted, countered with `2025-11-25`, connection proceeded; `null` fails with a `str` error *and* an `int` error |
| A missing `protocolVersion` | `initialize` with the field omitted | 2026-09-10 | `28 validation errors for ClientRequest`; the useful line is second, the rest are union alternatives being ruled out |
| **The deliberate failure** | `tools/list` alone, no handshake | 2026-09-10 | stderr `Failed to validate request: Received request before initialization was complete`; stdout `{"code":-32602,"message":"Invalid request parameters","data":""}`; **exit `0`** |
| The notification is not enforced here | `initialize` then `tools/list`, notification omitted | 2026-09-10 | the tool list came back — the `SHOULD NOT` in the `2025-06-18` lifecycle constrains the *server*, not the client |
| Legacy lifecycle phases | `https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle` | 2026-09-10 | the three phases, the version-negotiation rule and the two `SHOULD NOT` bullets, all quoted verbatim in parts 1.1, 1.2 and 2.1 |
| The handshake was removed | `https://modelcontextprotocol.io/specification/2026-07-28/changelog` | 2026-09-10 | major change 2, verbatim; also the `-32004` → `-32022` renumbering in minor change 12 |
| There is no negotiation handshake | `https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning` | 2026-09-10 | the opening line, the Modern / Legacy / Dual-era terminology, the `UnsupportedProtocolVersionError` block with `code -32022` and `data.supported`, and the compatibility matrix |
| The lifecycle page is gone | `https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle` | 2026-09-10 | resolves to `.../2026-07-28/basic/versioning`, titled *Versioning and Compatibility*. There is no lifecycle page at this revision |
| Rate limits are still unpublished | `https://ai.google.dev/gemini-api/docs/rate-limits`, via `PACKAGES.md` | 2026-09-10 | no RPM, TPM or RPD number to record; the ceiling stays a `TODO(me)` naming Google AI Studio |

## §10 Ledger & commit

**`docs/PROGRESS.md`:**

```text
| 15 | 2026-09-10 | MC-04 | 4 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the terms this day defined for the first time. **Check the file before
pasting**: days 13 and 14 are being written alongside this one, and if either has already defined a
term, keep theirs and drop the row here rather than adding a second, slightly different definition.
The last row is the likeliest collision — `Protocol revision` is a term day 13 may reasonably own.

```text
| Handshake | An exchange of messages that carries no work and exists only so the messages after it can assume something. Paid once per connection to avoid paying a smaller cost on every message afterwards. | day 15 part 1.1 | the opening exchange |
| Notification (JSON-RPC) | A message with a `method` and no `id`. No id means no reply is possible, so it is a statement rather than a question, and the sender can never learn whether it was acted on. | day 15 part 1.1 | a fire-and-forget message |
| Capability negotiation | Each side declaring, in the handshake and before either asks for anything, which optional features it supports — so neither has to probe, guess, or discover by failure. Scoped to the connection, which is why a stateless protocol cannot have it. | day 15 part 1.2 | the capabilities exchange |
| Version negotiation | The client naming the protocol revision it wants and the server naming the one that will actually govern the connection. The two may differ: a legacy server counters with its own latest rather than refusing, so detecting the mismatch is the client's job alone. | day 15 part 2.1 | protocol version agreement |
| Protocol revision | One dated, published edition of the MCP rules — `2025-06-18`, `2025-11-25`, `2026-07-28`. Not a package version: the SDK you install has its own, and the two move independently. | day 15 part 2.1 | the spec revision, the protocol version |
```

**`docs/PINS.md`** — nothing to add. Every version this day observed belongs to a project rather than
to the authoring repository, and both are already recorded in
`projects/02-parts-counter/PACKAGES.md`: `mcp` 1.30.0 and the wire revision `2025-11-25`, both dated
2026-09-10 by day 13.

**`docs/SOURCES.md`** — nothing to add. The specification revisions quoted today are dated web pages
rather than records with resolvable identifiers, and every one of them is dated in §9, which is what
that table is for. This is the same call days 1 to 3 made.

**Commit:**

```text
day 15: P02 Parts Counter · 5 — Lifecycle, stateless-first: the old handshake as history — closes MC-04
```
