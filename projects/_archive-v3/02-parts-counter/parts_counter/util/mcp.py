# parts_counter/util/mcp.py
"""The client side: how this project reaches tools that now live in another process.

Days 1 and 2 had `parts_counter/tools.py` — plain Python functions the agent called in its own
process. Those functions are gone. The same four tools are now behind `parts_mcp/`, and what stands
in their place is a **toolset**: an object the agent is given that fetches the tool list from the
server at run time and forwards each call across the boundary.

The difference that matters is not the syntax. It is that this project no longer knows what tools
it has until it asks. `tools=[find_part, stock_level, ...]` was a list decided when the file was
written; `tools=[toolset]` is a question answered when the agent runs. That buys a boundary whose
tools can change without this project being edited, and it costs a startup failure mode that a
list of imported functions does not have — if the server is not there, there are no tools, and the
agent will answer from nothing rather than refuse.

Two connection shapes are offered because days 6 and 7 need both, and they are the same server:

  * **stdio** — the client launches the server as a subprocess and speaks over its pipes. One
    client, one server, same machine, no port and no network.
  * **Streamable HTTP** — the server is already running and reachable at a URL. Many clients, many
    replicas, and the shape a container is deployed in.

Verified against mcp 1.30.0 and google-adk 2.8.0 on 2026-09-10.
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

#: Where the server listens when it is run over HTTP. `/mcp` is the SDK's default path, and it is
#: written out here rather than assumed, because a client that guesses the path fails with a 404
#: that says nothing about what it was looking for.
DEFAULT_HTTP_URL = "http://127.0.0.1:8090/mcp"


def over_stdio() -> McpToolset:
    """A toolset that launches `parts_mcp` as a subprocess and speaks over its pipes.

    `sys.executable` rather than the string `"python"`: the interpreter running this code is the
    one with this project's dependencies installed, and the bare name resolves through PATH to
    whatever a shell happens to find — which is the P00 day 1 failure, arriving here as a server
    that starts and immediately cannot import `mcp`.
    """
    return McpToolset(
        connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(
                command=sys.executable,
                args=["-m", "parts_mcp.server"],
                # The subprocess inherits neither the working directory nor the environment by
                # accident; both are stated, so the server starts the same way from anywhere.
                cwd=str(PROJECT_ROOT),
            ),
            timeout=20,
        ),
    )


def over_http(url: str = DEFAULT_HTTP_URL) -> McpToolset:
    """A toolset that connects to an already-running server at `url`.

    Nothing here launches anything. If the server is not up, this fails at the first tool listing
    rather than at import, which is why `run.py check` does not build one.
    """
    return McpToolset(
        connection_params=StreamableHTTPConnectionParams(url=url, timeout=20),
    )
