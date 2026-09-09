# projects/00-foundry/run.py
"""This project's own driver. `python run.py check` is the only verdict that counts.

Every project in this curriculum carries one of these and depends on nothing above it. This is
the reference version: four checks, each of which can go red on its own, and an exit status that
is the answer rather than a decoration on it.
"""

from __future__ import annotations

import subprocess
import sys
import tomllib
from pathlib import Path

import keys

HERE = Path(__file__).parent


def check_keys() -> list[str]:
    """Every name `.env.example` declares must be wired. Wired is all this can prove."""
    problems = []
    names = keys.names_this_project_reads()
    if not names:
        return [".env.example declares no key names: the committed file is the list of names"]
    for name in names:
        try:
            value = keys.require(name)
        except keys.MissingKey as exc:
            problems.append(str(exc))
            continue
        if keys.looks_like_a_placeholder(value):
            print(f"warn   keys: {name} looks like a placeholder. This check cannot tell a bad "
                  f"key from a good one; only a request to the provider can.")
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
    loose = [d for d in data["project"]["dependencies"] if "==" not in d]
    return [f"{d!r} is a floor, not a pin: one machine gets a version another never saw"
            for d in loose]


def check_lock_is_obeyed() -> list[str]:
    """`uv lock --check` proves the lockfile still answers pyproject, and writes nothing.

    It has to write nothing. A check that repairs what it is inspecting reports on a repository
    that no longer exists, and the drift it was built to catch is gone before anyone sees it.
    """
    result = subprocess.run(
        ["uv", "lock", "--check"],
        cwd=HERE, capture_output=True, text=True,
    )
    if result.returncode != 0:
        lines = [ln.strip() for ln in result.stderr.splitlines() if ln.startswith("error:")]
        detail = lines[0] if lines else "uv printed no error line"
        return [f"uv lock --check exited {result.returncode}: {detail}"]
    return []


CHECKS = {
    "keys": check_keys,
    "interpreter": check_interpreter,
    "pins": check_pins_are_pins,
    "lock": check_lock_is_obeyed,
}


def check() -> int:
    """Run every check, report all of them, and return the verdict as an exit status."""
    failures = 0
    for name, run_check in CHECKS.items():
        problems = run_check()
        failures += len(problems)
        if problems:
            for problem in problems:
                print(f"RED    {name}: {problem}")
        else:
            print(f"green  {name}")
    print(f"\n{failures} problem(s)")
    return 1 if failures else 0


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[1] != "check":
        print("usage: python run.py check", file=sys.stderr)
        return 2
    return check()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
