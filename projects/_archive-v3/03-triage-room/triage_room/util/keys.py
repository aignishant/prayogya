# triage_room/util/keys.py
"""Read this project's secrets, and refuse — by name — when one of them is not wired.

Nothing loads a `.env` file for you. This project carries its own reader, as every project in this
curriculum does, because a project that borrowed one from a sibling would not run alone.

Recap depth. The deep version of this idea — the process environment against the file, the three
states of a key, and the one no local check can settle — is P00 Foundry day 3. `PRIMER.md` §3 has
the self-contained version, and you do not need either to use this file.

One thing is different here and it is not in the code: this project runs **three agents**, and all
three read the same key from the same place. A cast does not multiply the number of secrets; it
multiplies the number of places one missing secret can surface, which is why the refusal names the
key and the file rather than the agent that happened to ask first.
"""

from __future__ import annotations

import os
from pathlib import Path

# Anchored to this file, not to the working directory, so the answer does not depend on where the
# shell was standing. triage_room/util/keys.py -> triage_room/util -> triage_room -> the project root.
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
ENV_FILE = PROJECT_ROOT / ".env"
EXAMPLE_FILE = PROJECT_ROOT / ".env.example"


class MissingKey(RuntimeError):
    """Raised with the name of the key, where it was looked for, and what to do about it."""


def read_env_file(path: Path | None = None) -> dict[str, str]:
    """Parse `KEY=value` lines into a dict. Nothing is exported; the caller decides."""
    path = ENV_FILE if path is None else path
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        name, _, value = line.partition("=")
        values[name.strip()] = value.strip().strip('"').strip("'")
    return values


def names_this_project_reads(path: Path | None = None) -> list[str]:
    """Every key name `.env.example` declares. The committed file is the list of names."""
    return sorted(read_env_file(EXAMPLE_FILE if path is None else path))


def get(name: str) -> str | None:
    """The process environment wins; the file is the fallback. Absent is `None`, never `''`."""
    from_process = os.environ.get(name)
    if from_process is not None:
        return from_process
    return read_env_file().get(name)


def require(name: str) -> str:
    """Return the value, or raise `MissingKey` naming the key and the file it belongs in."""
    value = get(name)
    if value is None:
        raise MissingKey(
            f"{name} is not set. Add a line `{name}=...` to {ENV_FILE}, or export it in this "
            f"shell. `.env.example` lists every name this project reads."
        )
    if not value.strip():
        raise MissingKey(
            f"{name} is present in {ENV_FILE.name} with an empty value. An empty string is a "
            f"value, so a check written as `if not os.environ.get(...)` cannot tell this apart "
            f"from the key being absent, and will tell you it is not set."
        )
    return value
