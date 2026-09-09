# parts_counter/store.py
"""The parts inventory, read and written straight off the filesystem.

**This file is the version of the data layer that has no boundary, and it is written this way on
purpose.** Day 2 of this project is the argument for putting a boundary in front of it; you cannot
follow that argument without first having the thing the argument is about.

Everything here works. That is what makes it worth studying: the problems are not bugs, they are
consequences of an agent's tools reaching a filesystem directly, and every one of them survives
code review because each individual line is fine.

Day 3 onward moves this behind `parts_mcp/`, and this module keeps its shape while losing its
direct reach.

All data is synthetic.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).with_name("data")
PARTS_FILE = DATA_DIR / "parts.json"


class PartNotFound(KeyError):
    """No part with that number. Never guess at a near match on an inventory."""


def _read() -> dict[str, Any]:
    return json.loads(PARTS_FILE.read_text(encoding="utf-8"))


def _write(payload: dict[str, Any]) -> None:
    PARTS_FILE.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def all_parts() -> list[dict[str, Any]]:
    """Every part in the inventory."""
    return _read()["parts"]


def find(query: str) -> list[dict[str, Any]]:
    """Parts whose number or name contains `query`, case-insensitively."""
    needle = query.strip().lower()
    return [p for p in all_parts()
            if needle in p["part_no"].lower() or needle in p["name"].lower()]


def get(part_no: str) -> dict[str, Any]:
    """One part by its exact number, or `PartNotFound`."""
    for part in all_parts():
        if part["part_no"].lower() == part_no.strip().lower():
            return part
    raise PartNotFound(part_no)


def adjust(part_no: str, delta: int) -> dict[str, Any]:
    """Add `delta` to a part's on-hand count and write the file back.

    This is the write, and it is the reason day 2 exists. Read the sequence: read the whole file,
    change one number, write the whole file. Nothing here records who asked, nothing prevents two
    callers doing it at once, and nothing outside this process can see that it happened.
    """
    payload = _read()
    for part in payload["parts"]:
        if part["part_no"].lower() == part_no.strip().lower():
            part["on_hand"] = part["on_hand"] + delta
            _write(payload)
            return part
    raise PartNotFound(part_no)
