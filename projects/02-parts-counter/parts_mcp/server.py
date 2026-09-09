# parts_mcp/server.py
"""This project's data boundary. It owns the inventory; nothing else opens the file.

Four tools, three of which read and one of which writes, and the write is the reason this process
exists as a separate thing at all.

`stateless_http=True` is the shape this curriculum builds towards and the reason day 3 spends a
sitting on the reframe. It means every request carries everything needed to answer it, so a second
replica can answer a call the first one never saw, and a container can be killed between two calls
without losing anything. The alternative — a session established once and referred to afterwards —
is the phone call, and it is what makes a server a thing you cannot scale by adding another.

The tool docstrings are written for a model, because they are what a model is shown: the MCP tool
declaration takes its `description` from the docstring and its `inputSchema` from the type hints,
the same derivation P01 day 4 taught for ADK's own `FunctionTool`.

All data is synthetic.

Verified against mcp 1.30.0 on 2026-09-10.
"""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from parts_mcp import store

mcp = FastMCP("parts-mcp", stateless_http=True)


@mcp.tool()
def find_part(query: str) -> dict[str, Any]:
    """Find parts whose number or name matches a query. An empty list is a valid answer."""
    hits = store.find(query)
    return {"query": query, "count": len(hits),
            "hits": [{"part_no": p["part_no"], "name": p["name"]} for p in hits]}


@mcp.tool()
def stock_level(part_no: str) -> dict[str, Any]:
    """Return how many of one part are on hand, and whether that is below its reorder point."""
    try:
        part = store.get(part_no)
    except store.PartNotFound:
        return {"error": f"no part numbered {part_no!r}",
                "known": [p["part_no"] for p in store.all_parts()]}
    return {"part_no": part["part_no"], "on_hand": part["on_hand"], "unit": part["unit"],
            "reorder_at": part["reorder_at"], "below_reorder": part["on_hand"] <= part["reorder_at"]}


@mcp.tool()
def bin_location(part_no: str) -> dict[str, Any]:
    """Return the bin a part is stored in, so somebody can walk to it."""
    try:
        part = store.get(part_no)
    except store.PartNotFound:
        return {"error": f"no part numbered {part_no!r}",
                "known": [p["part_no"] for p in store.all_parts()]}
    return {"part_no": part["part_no"], "bin": part["bin"], "name": part["name"]}


@mcp.tool()
def adjust_stock(part_no: str, delta: int) -> dict[str, Any]:
    """Change the on-hand count of a part by delta. Use a negative delta to issue stock.

    Only call this when the person has clearly asked for the count to change. Reading a level is
    stock_level; this is the tool that alters the record.
    """
    try:
        before = store.get(part_no)["on_hand"]
        part = store.adjust(part_no, delta)
    except store.PartNotFound:
        return {"error": f"no part numbered {part_no!r}",
                "known": [p["part_no"] for p in store.all_parts()]}
    return {"part_no": part["part_no"], "before": before, "after": part["on_hand"],
            "unit": part["unit"]}


if __name__ == "__main__":
    # stdio is the default and the one a local client launches as a subprocess. Day 6 runs the
    # same server over Streamable HTTP without changing a line above this one, which is the
    # argument for transports being a property of how you serve rather than of what you wrote.
    mcp.run(transport="stdio")
