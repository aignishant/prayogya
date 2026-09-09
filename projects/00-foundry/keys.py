# projects/00-foundry/keys.py
"""Read this project's secrets, and refuse — by name — when one of them is not wired.

Nothing loads a `.env` file for you. Python does not, `uv run` does not, and the shell does not.
This module is the thing that does it, and it is deliberately small enough to read in one pass.

It settles two of the three ways a key can be wrong. The third — present, non-empty and not
accepted by the provider — is not decidable here, and `looks_like_a_placeholder` is a guess that
says so out loud rather than a check that pretends otherwise.
"""

from __future__ import annotations

import os
from pathlib import Path

ENV_FILE = Path(__file__).with_name(".env")
EXAMPLE_FILE = Path(__file__).with_name(".env.example")

# Strings that are almost certainly not credentials. This is a hint, never a verdict: a real key
# is not on this list either, and only the provider can tell the two apart.
PLACEHOLDER_MARKERS = ("fake", "changeme", "change-me", "your-", "todo", "tbd", "xxx", "example")


class MissingKey(RuntimeError):
    """Raised with the name of the key, where it was looked for, and what to do about it."""


def read_env_file(path: Path | None = None) -> dict[str, str]:
    """Parse `KEY=value` lines into a dict. Nothing is exported; the caller decides.

    The default is resolved on every call, not bound at import. A default argument is evaluated
    once, when Python reads the `def`, so `path: Path = ENV_FILE` would freeze the module-level
    value and quietly ignore anyone who reassigned it afterwards.
    """
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
            f"{name} is not set. Add a line `{name}=...` to {ENV_FILE.name} in "
            f"{ENV_FILE.parent}, or export it in this shell. `.env.example` lists every name "
            f"this project reads."
        )
    if not value.strip():
        raise MissingKey(
            f"{name} is present in {ENV_FILE.name} with an empty value. An empty string is a "
            f"value, so every `if not os.environ.get(...)` upstream of here will disagree about "
            f"whether this key is set."
        )
    return value


def looks_like_a_placeholder(value: str) -> bool:
    """A guess, reported as a warning. Only a request to the provider settles this one."""
    return any(marker in value.lower() for marker in PLACEHOLDER_MARKERS)
