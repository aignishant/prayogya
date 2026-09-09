# evals/harness.py
"""The smallest eval that can go red, and the reason it can.

An eval is a test whose subject is a model's behaviour rather than a function's return value. This
one asks a question that has exactly one defensible answer — *did the desk look the fact up, or did
it produce one?* — and it can answer that without judging prose, because looking something up
leaves a trace: a tool call in the event stream.

Two decisions make this honest rather than decorative.

**It runs against a scripted model** (`ask_desk/scripted.py`), so the same input produces the same
events every time. An eval against a live model is a coin toss with a bill attached: it goes red on
a Tuesday for reasons nobody can reproduce, and a check that goes red at random gets muted. Here a
red result means the code changed.

**It asserts on the trajectory, not only on the text.** `expects_tools` is the load-bearing field.
A desk that answers "the VPN is degraded" without having called `check_service_status` produced the
right words by accident, and an eval that scored only the words would pass it — which is the
failure this file exists to catch.

All cases and all data are synthetic.
"""

from __future__ import annotations

import asyncio
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from google.genai import types

from ask_desk import agent, scripted
from google.adk.sessions import InMemorySessionService

CASES_FILE = Path(__file__).with_name("cases.json")

#: The scripts a case may name, by the key it uses. A case never constructs a model itself, so the
#: set of behaviours the evalset can express is visible in one place.
SCRIPTS = {
    "looks_it_up": scripted.LOOKS_IT_UP,
    "guesses": scripted.GUESSES,
}


@dataclass
class Result:
    """What one case produced, and why it passed or failed."""

    name: str
    passed: bool
    reasons: list[str]
    tools_called: list[str]
    answer: str
    inverted: bool = False


async def run_case(case: dict[str, Any]) -> Result:
    """Run one case and score it against what it declared it expects."""
    model = scripted.ScriptedModel(SCRIPTS[case["script"]], name=case["script"].replace("_", "-"))
    desk = agent.build_desk(model)
    sessions = InMemorySessionService()
    await sessions.create_session(app_name=agent.APP_NAME, user_id="eval", session_id=case["name"])
    runner = agent.build_runner(sessions, desk)

    message = types.Content(role="user", parts=[types.Part(text=case["question"])])
    tools_called: list[str] = []
    answer = ""
    async for event in runner.run_async(
        user_id="eval", session_id=case["name"], new_message=message,
        run_config=agent.run_config(),
    ):
        tools_called.extend(call.name for call in event.get_function_calls())
        if event.is_final_response() and event.content and event.content.parts:
            answer = "".join(part.text for part in event.content.parts if part.text)

    reasons = []
    for tool in case.get("expects_tools", []):
        if tool not in tools_called:
            reasons.append(
                f"expected the desk to call {tool!r} and it did not. It answered anyway, which "
                f"means the answer was not grounded in anything this system knows."
            )
    for phrase in case.get("expects_text", []):
        if phrase.lower() not in answer.lower():
            reasons.append(f"expected {phrase!r} in the answer; got {answer!r}")
    for phrase in case.get("forbids_text", []):
        if phrase.lower() in answer.lower():
            reasons.append(f"{phrase!r} must not appear in the answer; got {answer!r}")

    # An `expect_fail` case is the evalset checking itself. Its subject is not the desk but the
    # assertion above it: the scripted model deliberately answers without looking anything up, so
    # the case *must* produce a reason. If it stops producing one, the grounding check has been
    # weakened and every other case built on it is now worth less than it looks.
    if case.get("expect_fail"):
        if reasons:
            return Result(case["name"], True,
                          [f"failed as intended: {reasons[0]}"], tools_called, answer, True)
        return Result(case["name"], False, [
            "this case is supposed to fail and it passed. The desk answered without calling "
            f"{case.get('expects_tools')} and the grounding assertion did not object, so that "
            "assertion is no longer protecting any of the other cases."], tools_called, answer, True)

    return Result(case["name"], not reasons, reasons, tools_called, answer)


def main() -> int:
    """Run every case. Exit non-zero if any failed — the status is the verdict, as day 3 said."""
    cases = json.loads(CASES_FILE.read_text(encoding="utf-8"))["cases"]
    results = [asyncio.run(run_case(case)) for case in cases]

    for result in results:
        label = "green" if result.passed else "RED  "
        note = " (inverted)" if result.inverted else ""
        print(f"{label}  {result.name}{note}  tools={result.tools_called or '[]'}")
        if not result.passed or result.inverted:
            for reason in result.reasons:
                print(f"       {reason}")

    failed = [r for r in results if not r.passed]
    print(f"\n{len(results) - len(failed)}/{len(results)} case(s) passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
