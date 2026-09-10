# run.py
"""This project's own driver. It depends on nothing above this folder.

    python run.py check          the gate: config, pins, the registry, and the tests
    python run.py parts <query>  find parts, through the boundary's own tool
    python run.py race           day 2's concurrent-write demonstration, re-run against the
                                 store the boundary owns
    python run.py mcp            run the boundary server on stdio
    python run.py mcp --http     run the same server on Streamable HTTP at :8090/mcp
    python run.py probe          list and call the boundary's tools across a real process line
    python run.py eval           the boundary evalset, over stdio
    python run.py eval --http    the same evalset, against a server already listening
"""

from __future__ import annotations

import json
import subprocess
import sys
import threading
import time
import tomllib
from pathlib import Path

from parts_counter.util import keys, models

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
    declared = list(data["project"]["dependencies"])
    declared += data.get("dependency-groups", {}).get("dev", [])
    return [f"{d!r} is a floor, not a pin: one machine gets a version another never saw"
            for d in declared if "==" not in d]


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


def check_tests_pass() -> list[str]:
    """The kit's own tests. This is the check that can go red for a reason worth knowing."""
    result = subprocess.run([sys.executable, "-m", "pytest", "tests", "-q"],
                            cwd=HERE, capture_output=True, text=True)
    if result.returncode != 0:
        tail = [ln for ln in result.stdout.splitlines() if ln.strip()][-1:]
        return [f"pytest exited {result.returncode}: {tail[0] if tail else 'no output'}"]
    return []


def check_the_boundary_answers() -> list[str]:
    """The seventh check, and the first that leaves this process.

    Day 7 ended by writing down that `check` was green on a machine with the boundary deleted:
    six checks, none of which crossed the process line the whole project is built around. This is
    the one that does. It runs the evalset over stdio, which launches the server itself, so it
    needs nothing running and no key — and it goes red when the boundary is gone, which is the
    entire point of adding it.
    """
    from evals import harness

    result = subprocess.run([sys.executable, "run.py", "eval"],
                            cwd=HERE, capture_output=True, text=True)
    if result.returncode != 0:
        red = [ln.strip() for ln in result.stdout.splitlines() if ln.startswith("RED")]
        return [f"{len(harness.load_cases())} case evalset failed: "
                f"{red[0] if red else 'run `python run.py eval` to see why'}"]
    return []


CHECKS = {
    "keys": check_keys,
    "interpreter": check_interpreter,
    "pins": check_pins_are_pins,
    "lock": check_lock_is_obeyed,
    "model": check_model_is_registered,
    "tests": check_tests_pass,
    "boundary": check_the_boundary_answers,
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


def parts(query: str) -> int:
    """Find parts. Straight through the tools, with no model in the way."""
    from parts_mcp import server

    print(json.dumps(server.find_part(query), indent=2))
    return 0


def race(part_no: str = "SPK-0055", each: int = 10) -> int:
    """Two threads issuing stock at once, against a store with no boundary in front of it.

    Day 2 ran this against a store with nothing in front of it and lost parts every time. It now
    runs against `parts_mcp/store.py`, which is the same twenty lines with a lock around the
    read-modify-write and an atomic rename instead of a truncating write. Nothing about the threads
    changed; the ownership did.
    """
    from parts_mcp import store

    start = store.get(part_no)["on_hand"]
    errors: list[str] = []

    def issue() -> None:
        for _ in range(each):
            try:
                store.adjust(part_no, -1)
            except Exception as exc:  # noqa: BLE001 - the point is that anything can happen
                errors.append(type(exc).__name__)
            time.sleep(0.001)

    left, right = threading.Thread(target=issue), threading.Thread(target=issue)
    left.start(); right.start(); left.join(); right.join()

    end = store.get(part_no)["on_hand"]
    print(f"start on hand      : {start}")
    print(f"issued by two staff: {each * 2}")
    print(f"expected on hand   : {start - each * 2}")
    print(f"actual on hand     : {end}")
    print(f"parts unaccounted  : {end - (start - each * 2)}")
    print(f"reads that crashed : {errors}")
    store.adjust(part_no, start - end)
    print(f"restored to        : {store.get(part_no)['on_hand']}")
    return 0


def serve_mcp(http: bool = False) -> int:
    """Run the boundary server. Same server, same tools; only the transport differs."""
    from parts_mcp.server import mcp

    if http:
        # ── changed on day 8 ──
        # Day 6 set host and port here, after the server object existed. That works for a bind
        # and quietly does not work for anything derived from one: `transport_security` is
        # decided inside `FastMCP.__init__` from the host it was given, so a host assigned
        # afterwards leaves a loopback allowlist in front of a server listening everywhere.
        # The bind is now read from the environment in `parts_mcp/server.py`, at construction.
        print(f"boundary listening on http://{mcp.settings.host}:{mcp.settings.port}"
              f"{mcp.settings.streamable_http_path}", file=sys.stderr)
        mcp.run(transport="streamable-http")
    else:
        mcp.run(transport="stdio")
    return 0


def probe() -> int:
    """List and call the boundary's tools over stdio. Proves the line is real, needs no key."""
    import asyncio

    from parts_counter.util import mcp as client

    async def go() -> None:
        toolset = client.over_stdio()
        try:
            tools = await toolset.get_tools()
            print(f"{len(tools)} tool(s) fetched from the server:")
            for tool in sorted(tools, key=lambda t: t.name):
                print(f"  {tool.name}")
            print()
            by_name = {tool.name: tool for tool in tools}
            if "stock_level" not in by_name:
                raise SystemExit("the boundary answered, but without a stock_level tool: "
                                 f"{sorted(by_name)}")
            result = await by_name["stock_level"].run_async(
                args={"part_no": "BRK-0143"}, tool_context=None)
            print("one call, returned across the boundary:")
            print(" ", json.dumps(result)[:200])
        finally:
            await toolset.close()

    asyncio.run(go())
    return 0


def main(argv: list[str]) -> int:
    match argv[1:]:
        case ["check"]:
            return check()
        case ["parts", query]:
            return parts(query)
        case ["race"]:
            return race()
        case ["mcp"]:
            return serve_mcp()
        case ["mcp", "--http"]:
            return serve_mcp(http=True)
        case ["probe"]:
            return probe()
        case ["eval"]:
            from evals import harness
            return harness.main()
        case ["eval", "--http"]:
            from evals import harness
            return harness.main(http=True)
        case ["eval", "--http", url]:
            from evals import harness
            return harness.main(http=True, url=url)
        case _:
            print(__doc__, file=sys.stderr)
            return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
