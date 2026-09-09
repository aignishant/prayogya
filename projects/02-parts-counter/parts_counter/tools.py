# parts_counter/tools.py
"""The four things the counter can do — and one of them writes.

Three reads and a write, and the write is why this project has a boundary day. A tool that only
answers questions is a tool whose worst failure is a wrong answer. A tool that changes the
inventory can be wrong in a way that outlives the conversation, and there is nothing in this file
to stop it: no record of who asked, no second opinion, and no way for anything outside this process
to know it happened.

Nothing here is a mistake. Every function is short, typed and documented, and the whole file would
pass review. Day 2 is about what is missing rather than what is wrong.

ADK derives each declaration from the signature and the docstring (P01 day 4), so the docstrings
below are written for the model and not for us.

All data is synthetic.
"""

from __future__ import annotations

from typing import Any

from parts_counter import store
from parts_counter.util.logging import log


def find_part(query: str) -> dict[str, Any]:
    """Find parts whose number or name matches a query. An empty list is a valid answer."""
    hits = store.find(query)
    return {"query": query, "count": len(hits),
            "hits": [{"part_no": p["part_no"], "name": p["name"]} for p in hits]}


def stock_level(part_no: str) -> dict[str, Any]:
    """Return how many of one part are on hand, and whether that is below its reorder point."""
    try:
        part = store.get(part_no)
    except store.PartNotFound:
        return {"error": f"no part numbered {part_no!r}",
                "known": [p["part_no"] for p in store.all_parts()]}
    return {"part_no": part["part_no"], "on_hand": part["on_hand"], "unit": part["unit"],
            "reorder_at": part["reorder_at"], "below_reorder": part["on_hand"] <= part["reorder_at"]}


def bin_location(part_no: str) -> dict[str, Any]:
    """Return the bin a part is stored in, so somebody can walk to it."""
    try:
        part = store.get(part_no)
    except store.PartNotFound:
        return {"error": f"no part numbered {part_no!r}",
                "known": [p["part_no"] for p in store.all_parts()]}
    return {"part_no": part["part_no"], "bin": part["bin"], "name": part["name"]}


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
    # The only trace this write leaves anywhere, and it goes to this process's stderr. Day 2 is
    # about who else needed to know and had no way of finding out.
    log("stock.adjusted", part_no=part["part_no"], delta=delta,
        before=before, after=part["on_hand"])
    return {"part_no": part["part_no"], "before": before, "after": part["on_hand"],
            "unit": part["unit"]}


REGISTRY = {f.__name__: f for f in (find_part, stock_level, bin_location, adjust_stock)}
