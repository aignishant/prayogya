# parts_counter/util/logging.py
"""One line per event, in a shape a machine can read, with the values a secret would sit in
removed before they are written.

Two decisions, both of which are about what happens months later.

**JSON lines, not prose.** One object per line, so a run's log can be filtered, counted and diffed
without a parser anybody has to maintain. Prose logging is readable exactly once — by the person
who wrote it, on the day they wrote it.

**Values are redacted at the writer, not at the call site.** A logger that trusts every caller to
remember not to log a key is a logger that will log a key. So the redaction lives here, it runs on
every field of every record, and the call sites are free to be careless — which they will be.

This is the whole logging story for this project. There is no log level, no handler configuration
and no rotation: those are real needs and they arrive with a real deployment, and adding them now
would be scaffolding nobody has a use for yet.
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


def log(event: str, *, stream: TextIO | None = None, **fields: Any) -> dict[str, Any]:
    """Write one JSON object and return it, so a caller can assert on what was logged.

    Returning the record is what makes this testable without capturing stdout, and a logger nobody
    can write a test against is a logger whose redaction nobody has ever checked.
    """
    record = {
        # Explicit UTC with an offset, never a naive local timestamp. A log line whose timezone
        # depends on the machine that wrote it cannot be ordered against one from another machine.
        "at": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
        "event": event,
        **{key: _redact(key, value) for key, value in fields.items()},
    }
    print(json.dumps(record, default=str), file=stream or sys.stderr)
    return record
