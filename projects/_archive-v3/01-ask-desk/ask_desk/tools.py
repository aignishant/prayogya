# ask_desk/tools.py
"""The three things this desk can do, and the JSON that describes them to a model.

A tool is two objects that must not drift apart: a Python function that does the work, and a
declaration that tells the model the function exists, what it is for, and what arguments it takes.
The model never sees your code. It sees the declaration and nothing else, so the declaration is the
entire interface — a wrong description is a wrong tool, and it fails by being called at the wrong
moment rather than by raising.

Day 2 writes both halves by hand. Day 4 replaces the right-hand half with `FunctionTool`, which
derives it from the function itself, and the comparison is the point of that day.

All data here is synthetic.

Declaration shape verified against https://ai.google.dev/api/generate-content on 2026-09-09.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

DATA_FILE = Path(__file__).with_name("data") / "notes.json"


def _load() -> dict[str, Any]:
    """Read the synthetic store. Small enough to read per call; a cache would hide staleness."""
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


class UnknownTool(RuntimeError):
    """The model asked for a tool that does not exist. Never guess which one it meant."""


def search_notes(query: str, limit: int = 3) -> dict[str, Any]:
    """Find knowledge-base notes matching a query. An empty list is a valid answer."""
    words = [w for w in query.lower().split() if len(w) > 2]
    scored = []
    for note in _load()["notes"]:
        haystack = f"{note['title']} {note['body']} {' '.join(note['tags'])}".lower()
        score = sum(1 for w in words if w in haystack)
        if score:
            scored.append((score, note))
    scored.sort(key=lambda pair: (-pair[0], pair[1]["id"]))
    hits = [{"id": n["id"], "title": n["title"], "service": n["service"]}
            for _, n in scored[:limit]]
    return {"query": query, "count": len(hits), "hits": hits}


def fetch_note(note_id: str) -> dict[str, Any]:
    """Return one note in full by its id, or an error saying it does not exist."""
    for note in _load()["notes"]:
        if note["id"].lower() == note_id.lower():
            return note
    return {"error": f"no note with id {note_id!r}",
            "known_ids": [n["id"] for n in _load()["notes"]]}


def check_service_status(service: str) -> dict[str, Any]:
    """Return the current status of one service: operational, degraded or maintenance."""
    services = _load()["services"]
    if service.lower() not in services:
        return {"error": f"no service named {service!r}", "known": sorted(services)}
    return {"service": service.lower(), **services[service.lower()]}


#: The functions, by the name the model will use. `dispatch` looks up here and nowhere else.
REGISTRY = {
    "search_notes": search_notes,
    "fetch_note": fetch_note,
    "check_service_status": check_service_status,
}

#: What the model is told. Hand-written on day 2; every field here is a promise about the function
#: above it, and nothing checks that the two agree.
DECLARATIONS: list[dict[str, Any]] = [
    {
        "name": "search_notes",
        "description": (
            "Search the internal knowledge base for notes matching a query. "
            "Returns ids and titles only. An empty list means nothing matched, which is a "
            "valid answer and must not be reported as an error."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Words to search for, e.g. 'vpn file share'.",
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum notes to return. Defaults to 3.",
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "fetch_note",
        "description": (
            "Return the full text of one knowledge-base note by its id. "
            "Use search_notes first to find an id; do not guess one."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "note_id": {
                    "type": "string",
                    "description": "The note id, e.g. 'KB-101'.",
                },
            },
            "required": ["note_id"],
        },
    },
    {
        "name": "check_service_status",
        "description": (
            "Return the current operational status of one service. "
            "Known services are: vpn, printing, mail, identity."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "service": {
                    "type": "string",
                    "description": "One of: vpn, printing, mail, identity.",
                },
            },
            "required": ["service"],
        },
    },
]


def dispatch(name: str, args: dict[str, Any]) -> dict[str, Any]:
    """Run the tool the model asked for, and return a dict the model can be shown.

    Two rules, and both are about honesty rather than convenience. An unknown name raises rather
    than guessing at a near match, because a model that misremembers a tool name needs to be told,
    not accommodated. And an exception inside a tool is returned to the model as an `error` key
    rather than being allowed to kill the run — the model can then say what went wrong, which is
    more useful than a traceback, and the run's own error is still visible in the turn log.
    """
    if name not in REGISTRY:
        raise UnknownTool(
            f"the model asked for {name!r}, which this desk does not have. Known tools: "
            f"{', '.join(sorted(REGISTRY))}. A tool the model invents is a sign the declarations "
            f"and the registry have drifted apart."
        )
    try:
        return REGISTRY[name](**args)
    except TypeError as exc:
        # The model sent arguments that do not fit the signature: a missing required field, or a
        # name that is not a parameter. The declaration promised something the function does not
        # accept, and this is where that promise is broken.
        return {"error": f"{name} rejected these arguments: {exc}", "arguments_received": args}
