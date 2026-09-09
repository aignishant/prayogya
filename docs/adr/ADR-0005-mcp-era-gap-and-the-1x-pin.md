# ADR-0005 — P02 teaches the handshake era, and names the revision that deleted it

- **Date:** 2026-09-10
- **Day:** 13
- **Phase:** P02
- **Status:** accepted
- **Amends:** nothing in v3.1.0. §5.1's worked example, §12's P02 map and §17's day titles all stand
  exactly as written. This ADR records a **toolchain constraint** and the honesty rule it forces.
- **Related:** ADR-0004

## Context

Before writing day 13 the P02 freshness check required by the plan §10 was run against the live MCP
specification and the shipped SDKs on 2026-09-10. It found a gap between **what the specification
now says** and **what the toolchain this curriculum runs can speak**, and the gap is wide enough
that a day written carelessly would be teaching a protocol no reader could execute.

### 1 · The specification has completed the reframe the plan predicted

The current revision is **`2026-07-28`**. From
`https://modelcontextprotocol.io/docs/learn/versioning`, verbatim:

> The **current** protocol version is [**2026-07-28**](/specification/2026-07-28/).

Its own front page, `https://modelcontextprotocol.io/specification/2026-07-28`, describes the base
protocol as, verbatim:

> * [JSON-RPC](https://www.jsonrpc.org/) message format
> * Stateless, self-contained requests
> * Per-request capability negotiation

And its changelog, `https://modelcontextprotocol.io/specification/2026-07-28/changelog`, states two
changes that matter to every day in this phase, verbatim:

> 1. Remove protocol-level sessions and the `Mcp-Session-Id` header from the Streamable HTTP
>    transport. […]

> 2. Make MCP stateless: remove the `initialize`/`notifications/initialized` handshake. Every
>    request now carries its protocol version and client capabilities in `_meta` […] Version
>    mismatches return `UnsupportedProtocolVersionError` […]

The lifecycle page is gone: `…/2026-07-28/basic/lifecycle` now resolves to
`…/2026-07-28/basic/versioning`, whose opening line is, verbatim:

> **There is no negotiation handshake.** Every request carries its protocol version, and the server
> accepts or rejects each request independently:

That page defines the two eras the rest of this ADR uses, verbatim:

> * **Modern**: protocol versions that convey version, identity, and capabilities as per-request
>   metadata (revision `2026-07-28` and later).
> * **Legacy**: protocol versions that establish a session with an `initialize` handshake
>   (`2025-11-25` and earlier).

**None of this contradicts the plan.** §12 gives P02 day 3 as *"MCP 2026 — the stateless core; the
phone-call → web reframe"* and day 5 as *"Lifecycle, stateless-first — the old handshake as
history"*. Those titles describe exactly what the specification has now done. The plan anticipated
the direction correctly and does not need amending.

### 2 · The toolchain cannot speak the modern era

`google-adk` 2.8.0 declares, verbatim from its PyPI metadata:

    mcp<2,>=1.24 ; extra == "mcp"

So the MCP SDK this curriculum can use is the 1.x line, currently **1.30.0**. That line is a
**legacy-era** implementation: `mcp.types` declares `LATEST_PROTOCOL_VERSION = "2025-11-25"` and
`DEFAULT_NEGOTIATED_VERSION = "2025-03-26"`, both read on this machine on 2026-09-10, and its
servers open every connection with the `initialize` handshake.

The `mcp` 2.x line exists — 2.2.0 was released 2026-09-07, the same day as 1.30.0 — and is not
usable here. Two independent breaks:

- `from mcp.server.fastmcp import FastMCP` raises `ModuleNotFoundError` in 2.x; the class is now
  `mcp.server.mcpserver.MCPServer`, and `stateless_http` has moved off the constructor onto
  `run(transport="streamable-http", …)` and `streamable_http_app()`.
- `google-adk` 2.8.0's own MCP client does `from mcp.shared.session import ProgressFnT`, a module
  2.x does not have. The failure is **silent**: `google/adk/tools/mcp_tool/__init__.py` wraps its
  imports in a bare `try` and leaves `__all__ = []`, so the eventual error names `McpToolset` and
  says nothing about a version mismatch.

The second one deserves its own sentence, because it is the trap: `google-adk`'s bound sits behind
an **extra**. Installing plain `google-adk` does not install `mcp` and does not apply `mcp<2`, so
`uv add "mcp==2.2.0"` beside it **resolves cleanly** and breaks at import instead.

## Decision

**1. P02 depends on `google-adk[mcp]==2.8.0` and `mcp==1.30.0`, and says why in `PACKAGES.md`.**
The extra is named explicitly so the `mcp<2` bound is real and a future move to 2.x fails at
resolution — loudly, in a resolver — rather than at runtime in a bare `try`.

**2. P02 teaches the era it can run, and never pretends it is the current one.** Days 13 to 17
build and execute a legacy-era server: an `initialize` handshake, `2025-11-25` on the wire, and
`Mcp-Session-Id` present or absent according to `stateless_http`. Every transcript in those days is
real because the stack really speaks that.

**3. Every day in P02 that teaches a legacy mechanism states, on the same page, that the current
revision removed it, and quotes the specification saying so.** Not as a footnote — in the body,
where the reader meets the mechanism. Day 15 is the sharpest case and its plan title already says
it: *the old handshake as history*. That day teaches the handshake by running it and then shows the
changelog line that deleted it.

**4. Day 13's reframe is taught from the current specification, not from the SDK.** The
phone-call-to-web argument is the spec's own, it is quoted from `2026-07-28`, and the runnable
demonstration is `stateless_http=True` against `stateless_http=False` on mcp 1.30.0 — which shows
the same idea one era early, because that flag is the 1.x way of asking for the behaviour 2.x made
mandatory.

**5. Nothing in P02 prints a `2026-07-28` message shape as if it were runnable here.** No
`resultType`, no `_meta.io.modelcontextprotocol/protocolVersion`, no `server/discover`. Those are
quoted from the specification as what comes next, clearly labelled, and never pasted into this
project's code.

## Consequences

**What this costs.** A reader who opens the specification first will find a protocol without a
handshake and a project that performs one. Days 13 and 15 have to spend a paragraph each on why,
and that paragraph is unavoidable: the alternative is a phase whose checks cannot run.

**What it buys.** Every command in P02 executes. The handshake is not a diagram — it is a transcript
the reader produced. And the reader ends the phase having watched a protocol change underneath a
working system, which is the single most useful thing this phase can teach about depending on a
specification that is still moving.

**What is now owed.** When `google-adk` widens its bound to admit `mcp` 2.x, P02's server moves
`FastMCP` → `MCPServer`, `mcp.server.fastmcp` → `mcp.server.mcpserver`, and `stateless_http` from
the constructor to the serve call — and days 13 and 15 lose their "the current revision removed
this" paragraphs and gain the modern shapes instead. `PACKAGES.md` carries that as a `TODO(me)`
with the exact moves. This ADR is the record of why the day was written the way it was, so the
person making that change knows what they are undoing.

**What was checked, and when.** Every URL quoted above was fetched on 2026-09-10 and its text
copied from the page. Every version and constant was read on this machine on the same date, from
the installed wheels: `google-adk` 2.8.0, `mcp` 1.30.0, CPython 3.12.12.
