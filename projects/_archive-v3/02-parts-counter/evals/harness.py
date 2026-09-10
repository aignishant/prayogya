# evals/harness.py
"""The first check in this project whose subject is the boundary rather than the code.

`run.py check` proves things about this folder: the interpreter, the pins, the lockfile, the
registry, the tests. Every one of them passes on a machine where the boundary has been deleted,
because none of them crosses a process line. That gap was written down at the end of day 7 as owed
rather than tidied away, and this file is what settles it.

Three decisions, all of which are about what a failure is allowed to look like.

**A boundary that is not there is RED, never SKIP.** The most tempting line in a suite like this is
`if not reachable: return 0`, and it turns the only check that can see the boundary into one that
reports on its own absence. So an unreachable server is a failing suite with the transport's own
exception text printed underneath, and the exit status says 1.

**The same cases run over either transport.** `--stdio` launches the server as a subprocess;
`--http` speaks to one that is already listening — a container, usually. Nothing in `cases.json`
knows which, and that is the claim day 6 made about transports being a property of how you serve
rather than of what you wrote, asserted rather than repeated.

**One case is a canary.** It asserts something known to be false, and the suite fails if that case
*passes*. A suite whose assertions have quietly stopped running is green for the same reason a
correct one is, and the canary is the only line that can tell the two apart. The idea is P01's, in
`days/01-ask-desk/day-10-ship-d1-healthz-eval/parts/02-the-check-that-can-go-red/2.2-the-eval-that-checks-its-own-detector.md`;
`PRIMER.md` §6 is the self-contained version, and you do not need either to read this file.

There are no model calls here and there is no key. Every assertion is about what the boundary
returned, which is a question with one right answer — a model's wording is not, and P05 is where
this project's successors learn to score that.

All data is synthetic.

Verified against google-adk 2.8.0 and mcp 1.30.0 on 2026-09-10.
"""

from __future__ import annotations

import asyncio
import json
from pathlib import Path
from typing import Any

from parts_counter.util import mcp as client

CASES_FILE = Path(__file__).with_name("cases.json")


class BoundaryUnreachable(RuntimeError):
    """The server did not answer. Distinguished from a failing case, and fatal to the suite."""


def load_cases(path: Path | None = None) -> list[dict[str, Any]]:
    """Read the cases. A suite with no cases is an error, not an empty green run."""
    document = json.loads((path or CASES_FILE).read_text(encoding="utf-8"))
    cases = document.get("cases", [])
    if not cases:
        raise ValueError(f"{(path or CASES_FILE).name} declares no cases: a suite that asserts "
                         f"nothing exits 0 and means nothing")
    return cases


def payload(result: Any) -> dict[str, Any]:
    """Pull the answer out of what MCP returns, without pretending the wrapper is not there.

    A tool call comes back as a dict with `content` — the text a model would read — and
    `structuredContent`, the same answer as data. The assertions in `cases.json` are about the
    data, because asserting on the rendered text is how a suite starts failing on whitespace.
    """
    if isinstance(result, dict) and isinstance(result.get("structuredContent"), dict):
        return result["structuredContent"]
    return result if isinstance(result, dict) else {"value": result}


def is_error(result: Any) -> bool:
    """MCP's own flag for *the tool raised*, which is not the same as *the answer was no*."""
    return bool(result.get("isError")) if isinstance(result, dict) else False


def judge(case: dict[str, Any], result: Any) -> list[str]:
    """Return one complaint per unmet expectation. An empty list is a pass.

    Four assertion kinds, deliberately few. Every one of them is decidable by looking at the
    answer, so a case that fails names the field it failed on rather than reporting a score.
    """
    expect, data, complaints = case.get("expect", {}), payload(result), []

    if "is_error" in expect and is_error(result) != expect["is_error"]:
        complaints.append(f"isError is {is_error(result)}, expected {expect['is_error']}")

    for key in expect.get("present", []):
        if key not in data:
            complaints.append(f"{key!r} is missing from the answer; got {sorted(data)}")

    for key in expect.get("absent", []):
        if key in data:
            complaints.append(f"{key!r} is present and should not be: {data[key]!r}")

    for key, wanted in expect.get("fields", {}).items():
        if key not in data:
            complaints.append(f"{key!r} is missing; expected {wanted!r}")
        elif data[key] != wanted:
            complaints.append(f"{key} is {data[key]!r}, expected {wanted!r}")

    return complaints


async def call(tools: dict[str, Any], case: dict[str, Any]) -> Any:
    """Run one case's tool across the boundary, or say which tool the boundary does not have."""
    name = case["tool"]
    if name not in tools:
        raise BoundaryUnreachable(
            f"the boundary answered but has no tool named {name!r}. It offers "
            f"{sorted(tools)}, so this is a version disagreement rather than an outage."
        )
    return await tools[name].run_async(args=case["args"], tool_context=None)


async def run(cases: list[dict[str, Any]], *, http: bool = False,
              url: str | None = None) -> tuple[int, int]:
    """Run every case over one transport. Returns (passed, failed)."""
    toolset = client.over_http(url or client.DEFAULT_HTTP_URL) if http else client.over_stdio()
    passed = failed = 0
    try:
        try:
            tools = {tool.name: tool for tool in await toolset.get_tools()}
        except Exception as exc:  # noqa: BLE001 - every transport failure lands here, by design
            raise BoundaryUnreachable(
                f"could not reach the boundary over {'HTTP' if http else 'stdio'}: "
                f"{type(exc).__name__}: {exc}"
            ) from exc

        for case in cases:
            complaints = judge(case, await call(tools, case))
            # A canary is scored inverted: it is written to fail, so a canary with no complaints
            # means the assertions stopped running and the suite is reporting on nothing.
            if case.get("canary"):
                if complaints:
                    passed += 1
                    print(f"green  canary  {case['name']}")
                    print(f"       it failed as designed: {complaints[0]}")
                else:
                    failed += 1
                    print(f"RED    canary  {case['name']}")
                    print("       the canary PASSED. The assertions are not running, and every "
                          "green line above this one is meaningless.")
                continue
            if complaints:
                failed += 1
                print(f"RED    {case['name']}")
                for complaint in complaints:
                    print(f"       {complaint}")
            else:
                passed += 1
                print(f"green  {case['name']}")
    finally:
        await toolset.close()
    return passed, failed


def main(*, http: bool = False, url: str | None = None,
         path: Path | None = None) -> int:
    """The suite. Exit 0 only if every case passed and the canary failed."""
    cases = load_cases(path)
    try:
        passed, failed = asyncio.run(run(cases, http=http, url=url))
    except BoundaryUnreachable as exc:
        print(f"RED    the boundary is unreachable, so nothing was evaluated\n       {exc}")
        print(f"\n0 of {len(cases)} case(s) passed")
        return 1
    print(f"\n{passed} of {passed + failed} case(s) passed")
    return 1 if failed else 0
