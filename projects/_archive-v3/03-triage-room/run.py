# run.py
"""This project's own driver. It depends on nothing above this folder.

    python run.py check          the gate: config, pins, the registry, and the tests
    python run.py roles          print the cast's model registry, one line per role
    python run.py queue          the open queue, straight through the boundary's own tool
    python run.py mcp            run the boundary server on stdio
    python run.py mcp --http     run the same server on Streamable HTTP at :8091/mcp
    python run.py probe          list and call the boundary's tools across a real process line
    python run.py tools <role>   what one role is allowed to reach for, and what it is not
    python run.py cast           the agent tree, and what the framework added to it
"""

from __future__ import annotations

import json
import subprocess
import sys
import tomllib
from pathlib import Path

from triage_room.util import keys, models

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


def check_every_role_is_pinned() -> list[str]:
    """Not "the model" — **every role in the cast**. Three agents means three chances to slip.

    P02 checked one ID because it had one agent. Checking one of three is worse than checking
    none, because it reports green while two roles are free to be anything.
    """
    problems = []
    for role, model in sorted(models.CAST.items()):
        try:
            models.require_pinned(model)
        except models.UnpinnedModel as exc:
            problems.append(f"role {role!r}: {exc}")
    return problems


def check_tests_pass() -> list[str]:
    """The kit's own tests. This is the check that can go red for a reason worth knowing."""
    result = subprocess.run([sys.executable, "-m", "pytest", "tests", "-q"],
                            cwd=HERE, capture_output=True, text=True)
    if result.returncode != 0:
        tail = [ln for ln in result.stdout.splitlines() if ln.strip()][-1:]
        return [f"pytest exited {result.returncode}: {tail[0] if tail else 'no output'}"]
    return []


def check_the_boundary_answers() -> list[str]:
    """The check that leaves this process. Added on day 2, when there was a boundary to reach."""
    result = subprocess.run([sys.executable, "run.py", "probe"],
                            cwd=HERE, capture_output=True, text=True)
    if result.returncode != 0:
        lines = [ln.strip() for ln in result.stderr.splitlines() if ln.strip()]
        return [f"the boundary did not answer: {lines[-1] if lines else 'no output'}"]
    return []


CHECKS = {
    "keys": check_keys,
    "interpreter": check_interpreter,
    "pins": check_pins_are_pins,
    "lock": check_lock_is_obeyed,
    "roles": check_every_role_is_pinned,
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


def roles() -> int:
    """Print the registry. One line per role, so "who runs on what" is one command, not a grep."""
    width = max(len(role) for role in models.CAST)
    for role, model in sorted(models.CAST.items()):
        print(f"{role:<{width}}  {model}  (pinned {models.PINNED[model]})")
    distinct = len(set(models.CAST.values()))
    print(f"\n{len(models.CAST)} role(s) on {distinct} distinct model(s)")
    return 0


def queue() -> int:
    """The open queue. Straight through the boundary's tool, with no model in the way."""
    from desk_mcp import server

    print(json.dumps(server.list_queue(), indent=2))
    return 0


def serve_mcp(http: bool = False) -> int:
    """Run the boundary server. Same server, same tools; only the transport differs."""
    from desk_mcp.server import mcp

    if http:
        print(f"boundary listening on http://{mcp.settings.host}:{mcp.settings.port}"
              f"{mcp.settings.streamable_http_path}", file=sys.stderr)
        mcp.run(transport="streamable-http")
    else:
        mcp.run(transport="stdio")
    return 0


def probe() -> int:
    """List and call the boundary's tools over stdio. Proves the line is real, needs no key."""
    import asyncio

    from triage_room.util import mcp as client

    async def go() -> None:
        toolset = client.over_stdio()
        try:
            tools = {tool.name: tool for tool in await toolset.get_tools()}
            print(f"{len(tools)} tool(s) fetched from the server:")
            for name in sorted(tools):
                print(f"  {name}")
            print()
            if "list_queue" not in tools:
                raise SystemExit("the boundary answered, but without a list_queue tool: "
                                 f"{sorted(tools)}")
            result = await tools["list_queue"].run_async(args={}, tool_context=None)
            answer = result.get("structuredContent", result)
            print(f"one call, returned across the boundary: {answer.get('count')} open ticket(s)")
        finally:
            await toolset.close()

    asyncio.run(go())
    return 0


def tools_for(role: str) -> int:
    """What one role may reach for, and — the more interesting half — what it may not."""
    from triage_room.util import mcp as client

    try:
        allowed = client.TOOLS_FOR_ROLE[role]
    except KeyError:
        print(f"no such role: {role!r}. Roles: {', '.join(sorted(client.TOOLS_FOR_ROLE))}",
              file=sys.stderr)
        return 2
    every = sorted({name for names in client.TOOLS_FOR_ROLE.values() for name in names}
                   | {"record_triage"})
    for name in every:
        print(f"  {'yes' if name in allowed else ' no'}  {name}")
    return 0


def cast() -> int:
    """Print the tree, and the three things the framework added that nothing in cast.py wrote.

    No model is called. Everything here is read off the objects and off the request the flow would
    build, which is the point: an architecture you can only see by running it is one you will
    debug by guessing.
    """
    from google.adk.flows.llm_flows import agent_transfer

    from triage_room import cast as troupe

    alone = troupe.build_router(with_cast=False)
    router = troupe.build_router()

    print(f"router alone      flow: {type(alone._llm_flow).__name__}"
          f"   transfer targets: {[a.name for a in agent_transfer._get_transfer_targets(alone)]}")
    print(f"router with cast  flow: {type(router._llm_flow).__name__}"
          f"   transfer targets: {[a.name for a in agent_transfer._get_transfer_targets(router)]}")
    print()
    for child in router.sub_agents:
        peers = [a.name for a in agent_transfer._get_transfer_targets(child)]
        print(f"  {child.name:<11} model={child.model}  parent={child.parent_agent.name}  "
              f"mode={child.mode}")
        print(f"  {'':<11} can transfer to: {peers}")
        print(f"  {'':<11} tools declared here: "
              f"{[type(tool).__name__ for tool in child.tools]}")
    print()
    print("the instruction nothing in cast.py wrote, as the router will be shown it:")
    print("-" * 92)
    print(agent_transfer._build_transfer_instructions(
        "transfer_to_agent", router, agent_transfer._get_transfer_targets(router)).strip())
    print("-" * 92)
    return 0


def main(argv: list[str]) -> int:
    match argv[1:]:
        case ["check"]:
            return check()
        case ["roles"]:
            return roles()
        case ["queue"]:
            return queue()
        case ["mcp"]:
            return serve_mcp()
        case ["mcp", "--http"]:
            return serve_mcp(http=True)
        case ["probe"]:
            return probe()
        case ["tools", role]:
            return tools_for(role)
        case ["cast"]:
            return cast()
        case _:
            print(__doc__, file=sys.stderr)
            return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
