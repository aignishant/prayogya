# triage_room/util/mcp.py
"""The client side: how this project reaches tools that live in another process.

Recap depth. What a toolset is, why the tool list stops being a decision made when the file was
written and becomes a question answered when the agent runs, and what a call looks like when it
leaves the process, are taught in full at
`days/02-parts-counter/day-17-client-side/parts/01-a-list-you-no-longer-write/1.1-the-toolset-that-asks.md`.
`PRIMER.md` §1 has the self-contained version.

**What is new here is `for_agent`, and it is the reason this file is not P02's file renamed.**

P02 had one agent, so "the toolset" and "this agent's tools" were the same object and the question
never came up. Three agents share one boundary, and they must not share one toolset:

  * The **classifier** should be able to read the queue, read a ticket and look up precedents. It
    must not be able to close anything.
  * The **writer** should be able to read a ticket and look up precedents. It writes prose, not
    records.
  * The **router** should be able to read the queue and nothing else. A router that can answer is a
    router that will.

So `for_agent` returns a toolset filtered to the names one role is allowed to call. Filtering is not
security — the tools are still there, still on the far side, and anything holding the URL can call
all four. It is **blast radius**: the smallest set of things one confused agent can do. The real
control belongs at the boundary and arrives in P10 and P29; a filter here is the honest version of
what a project this size can enforce, and saying so is part of the lesson.

Verified against google-adk 2.8.0 and mcp 1.30.0 on 2026-09-10.
"""

from __future__ import annotations

import sys
from pathlib import Path

from google.adk.tools.mcp_tool import (
    McpToolset,
    StdioConnectionParams,
    StreamableHTTPConnectionParams,
)
from mcp import StdioServerParameters

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

#: Where the boundary listens when it is run over HTTP. `/mcp` is the SDK's default path, written
#: out rather than assumed, because a client that guesses the path fails with a 404 that says
#: nothing about what it was looking for.
DEFAULT_HTTP_URL = "http://127.0.0.1:8091/mcp"

#: Which of the boundary's four tools each role may call. The keys are the roles in
#: `triage_room/util/models.py`; a role missing from here is a role that gets nothing, which is a
#: louder failure than a role that quietly gets everything.
TOOLS_FOR_ROLE: dict[str, tuple[str, ...]] = {
    "routing": ("list_queue",),
    "classifying": ("list_queue", "fetch_ticket", "similar_tickets"),
    "writing": ("fetch_ticket", "similar_tickets"),
}


class UnknownRole(RuntimeError):
    """Raised when code asks for the tools of a role this project never declared."""


def over_stdio(tool_filter: list[str] | None = None) -> McpToolset:
    """A toolset that launches `desk_mcp` as a subprocess and speaks over its pipes.

    `sys.executable` rather than the string `"python"`: the interpreter running this code is the
    one with this project's dependencies installed, and the bare name resolves through PATH to
    whatever a shell happens to find — arriving here as a server that starts and immediately
    cannot import `mcp`.
    """
    return McpToolset(
        connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(
                command=sys.executable,
                args=["-m", "desk_mcp.server"],
                # Neither the working directory nor the environment is inherited by accident;
                # both are stated, so the server starts the same way from anywhere.
                cwd=str(PROJECT_ROOT),
            ),
            timeout=20,
        ),
        tool_filter=tool_filter,
    )


def over_http(url: str = DEFAULT_HTTP_URL, tool_filter: list[str] | None = None) -> McpToolset:
    """A toolset that connects to an already-running server at `url`.

    Nothing here launches anything. If the server is not up, this fails at the first tool listing
    rather than at import, which is why `run.py check` does not build one at import time.
    """
    return McpToolset(
        connection_params=StreamableHTTPConnectionParams(url=url, timeout=20),
        tool_filter=tool_filter,
    )


def for_agent(role: str, *, http: bool = False, url: str | None = None) -> McpToolset:
    """The toolset one role is allowed to hold, over whichever transport is asked for.

    Every agent constructor in this project goes through here rather than calling `over_stdio`
    directly, so "what may the writer touch?" is answered by one dictionary at the top of this
    file instead of by reading three agent modules.
    """
    if role not in TOOLS_FOR_ROLE:
        raise UnknownRole(
            f"{role!r} has no tool list. The roles with one are "
            f"{', '.join(sorted(TOOLS_FOR_ROLE))}. A role that is not here would be given every "
            f"tool on the boundary, which is the opposite of what this function is for."
        )
    allowed = list(TOOLS_FOR_ROLE[role])
    if http:
        return over_http(url or DEFAULT_HTTP_URL, tool_filter=allowed)
    return over_stdio(tool_filter=allowed)
