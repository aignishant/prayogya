# desk_mcp/server.py
"""This project's data boundary. It owns the ticket queue; nothing else opens the file.

Four tools, three of which read and one of which writes, and the write is the reason this process
exists as a separate thing at all.

Recap depth on the protocol. The stateless core, the lifecycle, the transports and the client side
are taught across P02 Parts Counter days 3 to 7, beginning at
`days/02-parts-counter/day-13-mcp-stateless-core/parts/01-the-reframe/1.1-the-phone-call-and-the-web.md`.
`PRIMER.md` §1 has the self-contained version, and you do not need to have read P02 to use this
file.

**What this boundary has that P02's did not: more than one caller.** Three agents will reach it,
two of them possibly at once, and none of them knows about the others. That changes nothing in the
code below — which is the claim worth checking rather than repeating — and it changes a great deal
about what the tool docstrings have to say, because a docstring is the only instruction a
classifier and a writer both read.

The tool docstrings are written for a model, because they are what a model is shown: the MCP tool
declaration takes its `description` from the docstring and its `inputSchema` from the type hints.

All data is synthetic.

Verified against mcp 1.30.0 on 2026-09-10.
"""

from __future__ import annotations

import os
from typing import Any

from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

from desk_mcp import store

# The bind is read from the environment **at construction**, under this project's own names.
#
# Recap depth: the SDK's own `FASTMCP_HOST` is ignored, because `FastMCP.__init__` passes `host=`
# into its settings explicitly and an init argument outranks the environment; and the host cannot
# be reassigned afterwards, because `transport_security` is derived from it inside the
# constructor. Both were measured, and the deep version is
# `days/02-parts-counter/day-18-ship-d2-container/parts/02-the-address-nobody-checked/2.1-the-bind-that-is-decided-once.md`.
# `PRIMER.md` §3 has the self-contained version.
BIND_HOST = os.environ.get("DESK_MCP_HOST", "127.0.0.1")
BIND_PORT = int(os.environ.get("DESK_MCP_PORT", "8091"))
ALLOWED_HOSTS = [value.strip()
                 for value in os.environ.get("DESK_MCP_ALLOWED_HOSTS", "").split(",")
                 if value.strip()]


def _transport_security(host: str, allowed: list[str]) -> TransportSecuritySettings | None:
    """Return `None` on loopback, where the SDK's own default is right; refuse a silent gap."""
    if host in ("127.0.0.1", "localhost", "::1"):
        return None
    if not allowed:
        raise RuntimeError(
            f"DESK_MCP_HOST is {host!r}, which is not loopback, and DESK_MCP_ALLOWED_HOSTS is "
            f"empty. A non-loopback host skips the SDK's automatic DNS-rebinding protection "
            f"entirely, so an empty allowlist means no Host or Origin checking at all."
        )
    return TransportSecuritySettings(
        enable_dns_rebinding_protection=True,
        allowed_hosts=allowed,
        allowed_origins=[f"http://{value}" for value in allowed],
    )


mcp = FastMCP("desk-mcp", stateless_http=True, host=BIND_HOST, port=BIND_PORT,
              transport_security=_transport_security(BIND_HOST, ALLOWED_HOSTS))


@mcp.tool()
def list_queue() -> dict[str, Any]:
    """List the tickets waiting to be triaged, oldest first. An empty queue is a valid answer."""
    queue = store.open_tickets()
    return {
        "count": len(queue),
        "categories": store.categories(),
        "severities": store.severities(),
        "tickets": [{"ticket_id": t["ticket_id"], "opened": t["opened"],
                     "channel": t["channel"], "subject": t["subject"]} for t in queue],
    }


@mcp.tool()
def fetch_ticket(ticket_id: str) -> dict[str, Any]:
    """Return one ticket in full, including its text. Use this before deciding anything about it."""
    try:
        ticket = store.get(ticket_id)
    except store.TicketNotFound:
        return {"error": f"no ticket numbered {ticket_id!r}",
                "open_now": [t["ticket_id"] for t in store.open_tickets()]}
    return dict(ticket)


@mcp.tool()
def similar_tickets(text: str, k: int = 3) -> dict[str, Any]:
    """Return up to k closed tickets whose wording overlaps this text, with how each was answered.

    These are precedents, not answers. An empty list means the desk has not seen this before, which
    is a fact worth reporting rather than a reason to invent a precedent.
    """
    hits = store.similar(text, k=k)
    return {"count": len(hits),
            "matches": [{"ticket_id": t["ticket_id"], "subject": t["subject"],
                         "category": t["category"], "severity": t["severity"],
                         "reply": t["reply"]} for t in hits]}


@mcp.tool()
def record_triage(ticket_id: str, category: str, severity: str, reply: str) -> dict[str, Any]:
    """Record a category, a severity and a reply on a ticket, and close it.

    This is the only tool that changes anything. Call it once, when the category, the severity and
    the reply are all decided. The category must be one of the ones list_queue reports and so must
    the severity; anything else is refused rather than corrected, and the refusal names the list.
    """
    try:
        ticket = store.record_triage(ticket_id, category, severity, reply)
    except store.TicketNotFound:
        return {"error": f"no ticket numbered {ticket_id!r}",
                "open_now": [t["ticket_id"] for t in store.open_tickets()]}
    except store.InvalidTriage as exc:
        return {"error": str(exc), "categories": store.categories(),
                "severities": store.severities()}
    return {"ticket_id": ticket["ticket_id"], "status": ticket["status"],
            "category": ticket["category"], "severity": ticket["severity"],
            "reply": ticket["reply"]}


if __name__ == "__main__":
    # stdio is the default and the one a local client launches as a subprocess. The same server
    # runs over Streamable HTTP without a line above this changing, which is what makes the
    # transport a property of how you serve rather than of what you wrote.
    mcp.run(transport="stdio")
