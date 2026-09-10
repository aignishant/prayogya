# run.py
"""This project's own driver. It depends on nothing above this folder.

    python run.py check          the gate: config, pins, and the registry
    python run.py plan "..."     print the request a question would send, and send nothing
    python run.py ask "..."      ask the desk one question, hand-rolled (needs a working key)
    python run.py adk "..."      the same question through the ADK agent (needs a working key)
    python run.py events [--stream]   every event one question produces, against a scripted model
    python run.py session             two questions in one session, and what the second one sees
    python run.py eval                the evalset; exits non-zero when a case fails
    python run.py serve               the D1 API on :8080
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


def check_evals_go_green() -> list[str]:
    """The evalset must pass, and it runs against a scripted model so it can say that honestly.

    This is what makes `check` a gate rather than a config linter: it is the only check here whose
    subject is the desk's behaviour. It needs no key and contacts nothing.
    """
    import evals

    if evals.main() != 0:
        return ["the evalset has a failing case — see the output above"]
    return []


CHECKS = {
    "keys": check_keys,
    "interpreter": check_interpreter,
    "pins": check_pins_are_pins,
    "lock": check_lock_is_obeyed,
    "model": check_model_is_registered,
    "evals": check_evals_go_green,
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


def events(stream: bool) -> int:
    """Print every event one question produces, against a scripted model. No key, no network."""
    import asyncio

    from google.adk.sessions import InMemorySessionService
    from google.genai import types

    from ask_desk import agent, scripted

    async def go() -> None:
        model = scripted.ScriptedModel(scripted.LOOKS_IT_UP, name="looks-it-up")
        desk = agent.build_desk(model)
        sessions = InMemorySessionService()
        await sessions.create_session(app_name=agent.APP_NAME, user_id="u", session_id="s")
        runner = agent.build_runner(sessions, desk)
        message = types.Content(role="user", parts=[types.Part(text="Is the VPN down?")])
        n = 0
        async for event in runner.run_async(
            user_id="u", session_id="s", new_message=message,
            run_config=agent.run_config(stream=stream),
        ):
            n += 1
            calls = [c.name for c in event.get_function_calls()]
            responses = [r.name for r in event.get_function_responses()]
            text = ""
            if event.content and event.content.parts:
                text = "".join(p.text for p in event.content.parts if p.text)
            if calls:
                kind = "call:" + ",".join(calls)
            elif responses:
                kind = "result:" + ",".join(responses)
            else:
                kind = "text"
            print(f"{n:3}. partial={str(event.partial):5} "
                  f"final={str(event.is_final_response()):5} {kind:34} {text[:48]!r}")
        print()
        print(f"{n} events, {model.calls} model call(s)")

    asyncio.run(go())
    return 0


def session() -> int:
    """Two questions down one session, and the same two down two sessions. No key, no network."""
    import asyncio

    from google.adk.sessions import InMemorySessionService
    from google.genai import types

    from ask_desk import agent, scripted

    async def turns(session_ids: list[str], label: str) -> None:
        sessions = InMemorySessionService()
        model = scripted.ScriptedModel(
            scripted.LOOKS_IT_UP + scripted.LOOKS_IT_UP, name="looks-it-up")
        desk = agent.build_desk(model)
        runner = agent.build_runner(sessions, desk)
        print(f"--- {label} ---")
        for i, sid in enumerate(session_ids, start=1):
            # `create_session` raises AlreadyExistsError on a second call with the same id, so a
            # session is created once and then reused. That refusal is the right one: silently
            # returning the existing session would hide a caller who thought they were starting
            # fresh and was not.
            if await sessions.get_session(
                    app_name=agent.APP_NAME, user_id="u", session_id=sid) is None:
                await sessions.create_session(
                    app_name=agent.APP_NAME, user_id="u", session_id=sid)
            message = types.Content(
                role="user", parts=[types.Part(text=f"question {i}")])
            async for _ in runner.run_async(
                user_id="u", session_id=sid, new_message=message,
                run_config=agent.run_config(),
            ):
                pass
            stored = await sessions.get_session(
                app_name=agent.APP_NAME, user_id="u", session_id=sid)
            print(f"  after question {i}: session {sid!r} holds {len(stored.events)} event(s)")

    asyncio.run(turns(["s-1", "s-1"], "one session, two questions"))
    print()
    asyncio.run(turns(["s-1", "s-2"], "two sessions, one question each"))
    return 0


def evaluate() -> int:
    """Run the evalset. Non-zero exit when a case fails — that is the whole point of it."""
    import evals

    return evals.main()


def serve() -> int:
    """The D1 surface: the agent behind HTTP, with a health endpoint that means something."""
    import uvicorn

    from ask_desk import api

    uvicorn.run(api.app, host="127.0.0.1", port=8080, log_level="warning")
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
        case ["events"]:
            return events(stream=False)
        case ["events", "--stream"]:
            return events(stream=True)
        case ["session"]:
            return session()
        case ["eval"]:
            return evaluate()
        case ["serve"]:
            return serve()
        case _:
            print(__doc__, file=sys.stderr)
            return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
