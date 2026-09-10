# parts_mcp/store.py
"""The inventory, and the only code in this system that touches the file.

This is `parts_counter/store.py` moved behind the boundary, and two things changed on the way. Both
are fixes for failures day 2 caused on purpose, and neither was available before the move — that is
the point of the move.

**One writer.** A lock serialises every read-modify-write, so two callers issuing stock cannot each
read `240` and each write `239`. Day 2 lost ten parts out of twenty to exactly that, and a lock in
`parts_counter/` would have fixed it only for callers inside that one process. Here there is only
one process that opens the file at all, so the lock is the whole answer rather than half of it.

**Whole-file writes, or nothing.** The old version truncated the file and wrote into it, so a
reader arriving mid-write got an empty file and a `JSONDecodeError`. Here the new contents go to a
temporary file in the same directory and are then moved over the old one. `os.replace` is atomic:
a reader sees the old file or the new one, and there is no instant at which it sees neither.

All data is synthetic.
"""

from __future__ import annotations

import json
import os
import tempfile
import threading
import time
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).with_name("data")
PARTS_FILE = DATA_DIR / "parts.json"

#: How many times to retry the final rename, and how long to wait between attempts.
#:
#: `os.replace` is atomic, and on Windows it can still be *refused*: if any other process holds a
#: handle on the destination — a sync client, an antivirus scanner, a file indexer — the call
#: raises `PermissionError: [WinError 5] Access is denied`. That is not a bug in this code and not
#: a race between our own threads; the lock above already excludes those. It is somebody else's
#: handle, it is transient, and the correct response is to wait a moment and try again rather than
#: to fail a write that was going to succeed.
_RENAME_ATTEMPTS = 8
_RENAME_BACKOFF_SECONDS = 0.02

#: One lock for **all** file access, reads included, because every write rewrites the whole file.
#: A per-part lock would be finer-grained and wrong: two writers to two different parts still write
#: the same document. And readers have to hold it too — on Windows, replacing a file another handle
#: has open raises `PermissionError`, so an unguarded read does not merely see stale data, it makes
#: the writer fail. `RLock`, not `Lock`, because `adjust` reads while already holding it.
_LOCK = threading.RLock()


class PartNotFound(KeyError):
    """No part with that number. Never guess at a near match on an inventory."""


def _read() -> dict[str, Any]:
    """Read the whole document. Always called with `_LOCK` held."""
    return json.loads(PARTS_FILE.read_text(encoding="utf-8"))


def _write_atomically(payload: dict[str, Any]) -> None:
    """Write to a temporary file in the same directory, then move it over the target.

    Same directory matters: `os.replace` is only atomic within one filesystem, and a temporary file
    in the system temp directory can easily be on another one.
    """
    fd, temp_path = tempfile.mkstemp(dir=DATA_DIR, prefix=".parts-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2)
            handle.write("\n")
            handle.flush()
            # Force the bytes to disk before the rename. Without this the rename can be durable
            # while the contents behind it are not, and a crash leaves a valid name over an empty
            # file — the same torn read, arriving after a power cut instead of during a write.
            os.fsync(handle.fileno())
        _replace_with_retry(temp_path, PARTS_FILE)
    except BaseException:
        Path(temp_path).unlink(missing_ok=True)
        raise


def _replace_with_retry(source: str, destination: Path) -> None:
    """`os.replace`, retried while Windows says another process holds the destination."""
    for attempt in range(1, _RENAME_ATTEMPTS + 1):
        try:
            os.replace(source, destination)
            return
        except PermissionError:
            if attempt == _RENAME_ATTEMPTS:
                # Give up loudly. A write that silently did not happen is the failure mode this
                # whole module exists to prevent.
                raise
            time.sleep(_RENAME_BACKOFF_SECONDS * attempt)


def all_parts() -> list[dict[str, Any]]:
    """Every part in the inventory."""
    with _LOCK:
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
    """Add `delta` to a part's on-hand count. Serialised, and durable or not at all."""
    with _LOCK:
        payload = _read()
        for part in payload["parts"]:
            if part["part_no"].lower() == part_no.strip().lower():
                part["on_hand"] = part["on_hand"] + delta
                _write_atomically(payload)
                return dict(part)
        raise PartNotFound(part_no)
