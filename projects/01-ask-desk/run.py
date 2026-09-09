# run.py
"""This project's own driver. It depends on nothing above this folder.

    python run.py check          the gate: config, pins, and the registry
    python run.py plan "..."     print the request a question would send, and send nothing
    python run.py ask "..."      ask the desk one question, hand-rolled (needs a working key)
    python run.py adk "..."      the same question through the ADK agent (needs a working key)
"""

from __future__ import annotations

import asyncio
import json
import subprocess
import sys
import tomllib
from pathlib import Path

from ask_desk import loop, provider
from ask_desk.util import keys, models

HERE = Path(__file__).parent


def check_keys() -> list[str]:
    """Every name `.env.example` declares must be wired. Wired is all this can prove."""
    problems = []
    names = keys.names_this_project_reads()
    if not names:
        return [".env.example declares no key names: the committed file is the list of names"]
    for name in names:
        try:
            keys.require(name)
        except keys.MissingKey as exc:
            problems.append(str(exc))
    return problems


def check_interpreter() -> list[str]:
    """The interpreter actually running must be the one `.python-version` pins."""
    pin_file = HERE / ".python-version"
    if not pin_file.exists():
        return [".python-version is missing: requires-python is a floor, not a pin"]
    pinned = pin_file.read_text(encoding="utf-8").strip()
    running = ".".join(str(n) for n in sys.version_info[:3])
    if running != pinned:
        return [f".python-version pins {pinned}; this interpreter is {running}"]
    return []


def check_pins_are_pins() -> list[str]:
    """A dependency written with `>=` is a floor. Two machines can honour it differently."""
    data = tomllib.loads((HERE / "pyproject.toml").read_text(encoding="utf-8"))
    return [f"{d!r} is a floor, not a pin: one machine gets a version another never saw"
            for d in data["project"]["dependencies"] if "==" not in d]


def check_lock_is_obeyed() -> list[str]:
    """`uv lock --check` proves the lockfile still answers pyproject, and writes nothing."""
    result = subprocess.run(["uv", "lock", "--check"], cwd=HERE, capture_output=True, text=True)
    if result.returncode != 0:
        lines = [ln.strip() for ln in result.stderr.splitlines() if ln.startswith("error:")]
        return [f"uv lock --check exited {result.returncode}: "
                f"{lines[0] if lines else 'uv printed no error line'}"]
    return []


def check_model_is_registered() -> list[str]:
    """The model every call will name must be an exact ID this project wrote down."""
    try:
        models.require_pinned(models.ANSWERING)
    except models.UnpinnedModel as exc:
        return [str(exc)]
    return []


CHECKS = {
    "keys": check_keys,
    "interpreter": check_interpreter,
    "pins": check_pins_are_pins,
    "lock": check_lock_is_obeyed,
    "model": check_model_is_registered,
}


def check() -> int:
    failures = 0
    for name, run_check in CHECKS.items():
        problems = run_check()
        failures += len(problems)
        for problem in problems:
            print(f"RED    {name}: {problem}")
        if not problems:
            print(f"green  {name}")
    print(f"\n{failures} problem(s)")
    return 1 if failures else 0


def plan(question: str) -> int:
    """Print the exact JSON a question would send. Contacts nothing and needs no key."""
    url, body = loop.Conversation().next_request(question)
    print(f"POST {url}\n")
    print(json.dumps(body, indent=2))
    return 0


def ask(question: str) -> int:
    try:
        print(loop.ask_once(question))
    except provider.ProviderError as exc:
        print(f"the provider refused this request: {exc}", file=sys.stderr)
        return 1
    except keys.MissingKey as exc:
        print(f"{exc}", file=sys.stderr)
        return 1
    return 0


def adk(question: str) -> int:
    """The same desk, driven by ADK's Agent and Runner instead of by loop.py."""
    from ask_desk import agent  # imported here so `check` needs no framework import

    try:
        print(asyncio.run(agent.ask(question)))
    except keys.MissingKey as exc:
        print(f"{exc}", file=sys.stderr)
        return 1
    return 0


def main(argv: list[str]) -> int:
    match argv[1:]:
        case ["check"]:
            return check()
        case ["plan", question]:
            return plan(question)
        case ["ask", question]:
            return ask(question)
        case ["adk", question]:
            return adk(question)
        case _:
            print(__doc__, file=sys.stderr)
            return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
