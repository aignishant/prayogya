# ADR-0009 — P01 runs the current MCP revision, and writes its own client

- **Date:** 2026-09-10
- **Day:** P01 day 3, before the boundary was written
- **Phase:** P01 Claims Intake Desk, spine slots 3 and 4
- **Status:** accepted
- **Amends:** nothing in the plan. §12 slot 4 already says "lifecycle and the era gap"; this
  records which side of the gap **this project** stands on, and why that differs from the earlier
  decision recorded in ADR-0005.
- **Related:** ADR-0005 (the era gap and the 1.x pin), ADR-0006 (every project teaches everything
  it uses)

## Context

The freshness check for P01's boundary days was run on 2026-09-10 and found that one of the facts
ADR-0005 was built on has moved.

Observed live, that day:

| What | Where | Value |
| --- | --- | --- |
| MCP current protocol revision | `https://modelcontextprotocol.io/docs/learn/versioning` | `2026-07-28` |
| `mcp` Python package, latest | `https://pypi.org/pypi/mcp/json` | `2.2.0`, `requires_python >=3.10` |
| `google-adk`, latest | `https://pypi.org/pypi/google-adk/json` | `2.8.0` |
| `google-adk`'s MCP requirement | the same record | `mcp<2,>=1.24; extra == "mcp"` |

ADR-0005 recorded that the current revision could not be executed, because the only usable SDK was
the 1.x line and that line performs an `initialize` handshake the current revision removed. **That
is no longer true.** `mcp` 2.2.0 exists, it speaks `2026-07-28`, and the revision's own page
describes what replaced the handshake: every request declares its version in
`io.modelcontextprotocol/protocolVersion` inside `_meta`, the same value rides in the
`MCP-Protocol-Version` header on Streamable HTTP, and a client that wants to know up front calls
`server/discover`, "a mandatory RPC that returns the server's supported protocol versions,
capabilities, and identity in a single request".

So P01 has a choice its predecessor did not have, and the two halves of it cannot both be taken:
`google-adk`'s `mcp` extra pins `mcp<2`, and `mcp==2.2.0` is what speaks the current revision. One
environment cannot hold both.

## Decision

**P01 pins `mcp==2.2.0` and teaches the current revision.** Its boundary is built against the
2.x SDK, its client is written by hand in this project, and `google-adk` is installed **without**
its `[mcp]` extra — so there is no version conflict to resolve, because the constraint only applies
to an extra this project never asks for.

What this buys: a reader following P01 builds a boundary that matches the specification they will
find if they go and look. No day in this project teaches a mechanism the specification has removed.

What it costs: **ADK's `McpToolset` is never used here.** The agent reaches the boundary through a
client this project writes and prints in full. Plan §12 slot 4 asks for "the client wiring, and the
tool that now lives elsewhere", which this satisfies; it does not ask for a particular class from a
particular framework, and this ADR is the record that the difference was noticed rather than
skipped.

**This is a per-project decision and it does not supersede ADR-0005.** That ADR recorded a true
observation about a different project on a different date, and the ledger rule applies: a dated
observation superseding a dated observation is the record working, not an amendment. A later
project may reasonably choose the other side — if its subject is the framework's own integration
rather than the protocol, the 1.x pin is the better teacher.

## Options considered

| Option | Why not |
| --- | --- |
| **Pin `mcp<2` and use `google-adk[mcp]`** | It is the safe copy of what came before, and it means every one of P01's boundary days teaches a handshake the current revision deleted, while quoting the line that deleted it. Defensible when nothing else can run; indefensible now that something can. |
| **Both: modern boundary, plus a legacy day** | The most complete answer, and it costs an extra sitting — which changes P01's insert list, its Days column in §11, and therefore the plan. A plan amendment to buy a demonstration is the wrong trade at project one; the gap is already documented here and in ADR-0005. |
| **Two environments in one project** | `uv` can express it and a reader cannot hold it. A project whose boundary runs on one SDK and whose agent runs on another has a seam nobody can see, and the From-Scratch Rule means a reader has to be able to build the whole thing from nothing. |

## Consequences

**Better.** The boundary a reader builds is the boundary the specification describes today: no
handshake, a version on every request, `server/discover` when a client wants one. The hand-written
client is nine lines of this project's own code rather than a framework object, which suits the
Repetition Rule — the mechanism is taught here, at full depth, rather than delegated to a class
whose behaviour has to be described second-hand.

**Worse.** P01 does not exercise `google-adk`'s MCP integration at all, which is a real part of the
framework's surface and a thing a reader might expect from a curriculum that names ADK in its
title. That gap is this decision's price and it is named here so it is not discovered as an
omission later.

**What would have to be true to revisit this.** If `google-adk` relaxes its `mcp<2` pin — the
record to re-read is `https://pypi.org/pypi/google-adk/json`, the field is `requires_dist` — then
both halves become available at once and there is no trade to make. That check belongs in the next
project's freshness pass, not in a rewrite of this one.

**One thing to watch.** The 2.x SDK is new, and its Python model names are snake_case where the
wire format is camelCase: `tool.input_schema` for `inputSchema`, `result.structured_content` for
`structuredContent`, `result.is_error` for `isError`. Both spellings were tried while writing day 3
and the camelCase ones raise `AttributeError` from pydantic. Every day in this project that names a
field must have had it read off the installed package, not off the specification.
