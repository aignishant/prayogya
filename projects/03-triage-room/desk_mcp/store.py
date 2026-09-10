# desk_mcp/store.py
"""The ticket queue, and the only code in this system that touches the file.

Recap depth. One writer behind a lock, and a whole-file write finished by an atomic rename rather
than a truncating write, are taught in full at
`days/02-parts-counter/day-14-server-skeleton-first-tool/parts/01-the-file-behind-the-line/1.2-one-writer-and-an-atomic-rename.md`.
`PRIMER.md` §2 has the self-contained version.

**What is different here, and it is not the file handling:** this project's cast is three agents,
and two of them may be running at the same time. In P02 the two writers in the demonstration were
threads somebody wrote on purpose. Here they arrive by themselves — a classifier and a writer both
recording their part of the same ticket is the normal case, not the stress test — so the same lock
is doing a job the earlier project had to arrange to need.

All data is synthetic: no real customer, product, person or incident appears anywhere in it.
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
TICKETS_FILE = DATA_DIR / "tickets.json"

#: How many times to retry the final rename, and how long to wait between attempts.
#:
#: `os.replace` is atomic, and on Windows it can still be *refused*: if any other process holds a
#: handle on the destination — a sync client, an antivirus scanner, a file indexer — the call
#: raises `PermissionError: [WinError 5] Access is denied`. That is somebody else's handle, it is
#: transient, and the right answer is to wait a moment and try again rather than to fail a write
#: that was going to succeed.
_RENAME_ATTEMPTS = 8
_RENAME_BACKOFF_SECONDS = 0.02

#: One lock for **all** file access, reads included, because every write rewrites the whole file.
#: `RLock`, not `Lock`, because `record_triage` reads while already holding it.
_LOCK = threading.RLock()


class TicketNotFound(KeyError):
    """No ticket with that id. Never guess at a near match on somebody's support queue."""


class InvalidTriage(ValueError):
    """A category or severity the desk does not use. Raised rather than coerced.

    This is the boundary refusing a value, and it is here rather than in an agent on purpose: the
    agents are three, the vocabulary is one, and a rule enforced in three places is a rule that
    disagrees with itself by the end of the month.
    """


def _read() -> dict[str, Any]:
    """Read the whole document. Always called with `_LOCK` held."""
    return json.loads(TICKETS_FILE.read_text(encoding="utf-8"))


def _write_atomically(payload: dict[str, Any]) -> None:
    """Write to a temporary file in the same directory, then move it over the target.

    Same directory matters: `os.replace` is only atomic within one filesystem, and a temporary file
    in the system temp directory can easily be on another one.
    """
    fd, temp_path = tempfile.mkstemp(dir=DATA_DIR, prefix=".tickets-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2)
            handle.write("\n")
            handle.flush()
            # Force the bytes to disk before the rename. Without this the rename can be durable
            # while the contents behind it are not, and a crash leaves a valid name over an empty
            # file — a torn read arriving after a power cut instead of during a write.
            os.fsync(handle.fileno())
        _replace_with_retry(temp_path, TICKETS_FILE)
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


def categories() -> list[str]:
    """The only categories this desk uses. The list lives with the data, not in an agent."""
    with _LOCK:
        return list(_read()["categories"])


def severities() -> list[str]:
    """The only severities this desk uses, from least to most urgent."""
    with _LOCK:
        return list(_read()["severities"])


def all_tickets() -> list[dict[str, Any]]:
    """Every ticket, open and closed."""
    with _LOCK:
        return _read()["tickets"]


def open_tickets() -> list[dict[str, Any]]:
    """The queue: tickets nobody has triaged yet, oldest first."""
    return sorted((t for t in all_tickets() if t["status"] == "open"),
                  key=lambda t: (t["opened"], t["ticket_id"]))


def get(ticket_id: str) -> dict[str, Any]:
    """One ticket by its exact id, or `TicketNotFound`."""
    for ticket in all_tickets():
        if ticket["ticket_id"].lower() == ticket_id.strip().lower():
            return ticket
    raise TicketNotFound(ticket_id)


def _words(text: str) -> set[str]:
    """Lowercase words of three letters or more. Deliberately crude, and said so out loud.

    This is word overlap, not similarity: it cannot tell that "handset" and "phone" are the same
    complaint. Embeddings are P18's subject, and a half-built version here would be the thing that
    project has to unpick first.
    """
    return {word.strip(".,:;!?()'\"").lower()
            for word in text.split() if len(word.strip(".,:;!?()'\"")) >= 3}


def similar(text: str, k: int = 3) -> list[dict[str, Any]]:
    """The `k` closed tickets sharing the most words with `text`. An empty list is a valid answer."""
    needle = _words(text)
    if not needle:
        return []
    scored = []
    for ticket in all_tickets():
        if ticket["status"] != "closed":
            continue
        overlap = needle & _words(f"{ticket['subject']} {ticket['body']}")
        if overlap:
            scored.append((len(overlap), ticket))
    scored.sort(key=lambda pair: (-pair[0], pair[1]["ticket_id"]))
    return [ticket for _, ticket in scored[:k]]


def record_triage(ticket_id: str, category: str, severity: str, reply: str) -> dict[str, Any]:
    """Write a triage decision onto a ticket and close it. Serialised, and durable or not at all."""
    category, severity = category.strip().lower(), severity.strip().lower()
    with _LOCK:
        payload = _read()
        if category not in payload["categories"]:
            raise InvalidTriage(
                f"{category!r} is not a category this desk uses. The categories are "
                f"{', '.join(payload['categories'])}, and they live in the queue rather than in "
                f"an agent's instruction so that three agents cannot each have their own list."
            )
        if severity not in payload["severities"]:
            raise InvalidTriage(
                f"{severity!r} is not a severity this desk uses. The severities are "
                f"{', '.join(payload['severities'])}."
            )
        if not reply.strip():
            raise InvalidTriage(
                "a triage with an empty reply closes a ticket without answering it, which is the "
                "one outcome worse than leaving it open"
            )
        for ticket in payload["tickets"]:
            if ticket["ticket_id"].lower() == ticket_id.strip().lower():
                ticket.update(status="closed", category=category, severity=severity,
                              reply=reply.strip())
                _write_atomically(payload)
                return dict(ticket)
        raise TicketNotFound(ticket_id)


def reopen(ticket_id: str) -> dict[str, Any]:
    """Undo a triage, so a demonstration can be run twice. Not a desk feature; a test fixture."""
    with _LOCK:
        payload = _read()
        for ticket in payload["tickets"]:
            if ticket["ticket_id"].lower() == ticket_id.strip().lower():
                ticket.update(status="open", category=None, severity=None, reply=None)
                _write_atomically(payload)
                return dict(ticket)
        raise TicketNotFound(ticket_id)
