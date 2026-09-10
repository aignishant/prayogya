# triage_room/util/logging.py
"""One line per event, in a shape a machine can read, with credentials removed before writing.

Recap depth. JSON lines rather than prose, and redaction at the writer rather than at the call
site, are taught in full at
`days/02-parts-counter/day-11-kit/parts/02-what-a-call-costs/2.2-a-log-that-cannot-leak.md`.
`PRIMER.md` §4 has the self-contained version.

**What is new here:** every record carries `agent`. With one agent that field was noise; with three
it is the difference between a log you can read and a log you can only scroll. `log()` therefore
takes the agent's name as a required keyword — not as an optional one, because an optional label is
a label that is missing exactly on the lines you most want to read back.

**Deliberately not built yet 🅿️.** Correlating those lines: one identifier threaded through a whole
turn so a router's line and its writer's line can be pulled out together, and the nesting that makes
a three-agent turn legible as a tree. That is P04 Trip Ledger day 5, and a half-built version here
would be the thing P04 has to unpick first.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from typing import Any, TextIO

#: Field names whose values never reach the log, whatever they contain. Matched on substring and
#: case-insensitively, because the field will be called `api_key` in one place and `GOOGLE_API_KEY`
#: in the next.
SECRET_NAMES = ("key", "token", "secret", "password", "authorization", "credential")

#: What a redacted value is replaced with. A fixed string rather than the value's length, because
#: a length is information about a secret.
REDACTED = "<redacted>"


def _redact(key: str, value: Any) -> Any:
    """Replace a value whose field name suggests it is a credential."""
    if any(marker in key.lower() for marker in SECRET_NAMES):
        return REDACTED
    if isinstance(value, dict):
        return {k: _redact(k, v) for k, v in value.items()}
    return value


def log(event: str, *, agent: str, stream: TextIO | None = None, **fields: Any) -> dict[str, Any]:
    """Write one JSON object and return it, so a caller can assert on what was logged.

    Returning the record is what makes this testable without capturing stdout, and a logger nobody
    can write a test against is a logger whose redaction nobody has ever checked.
    """
    record = {
        # Explicit UTC with an offset, never a naive local timestamp. A log line whose timezone
        # depends on the machine that wrote it cannot be ordered against one from another machine.
        "at": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
        "agent": agent,
        "event": event,
        **{key: _redact(key, value) for key, value in fields.items()},
    }
    print(json.dumps(record, default=str), file=stream or sys.stderr)
    return record
