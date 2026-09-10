# parts_counter/agent.py
"""The counter, as an ADK agent, with its tools on the far side of a boundary.

The only line here that differs in shape from P01's agent is `tools=[...]`. P01 passed plain Python
functions and ADK wrapped each one; this passes a **toolset**, and the tools are discovered by
asking the server when the agent runs.

The model is pinned explicitly, as it is in every project (the plan section 9): ADK 2.8.0's
built-in default is `gemini-3.5-flash`, which the provider lists as Stable and calls its legacy
Flash model, so an agent that omits `model=` is quietly four generations old.

Verified against google-adk 2.8.0 and mcp 1.30.0 on 2026-09-10.
"""

from __future__ import annotations

import os

from google.adk.agents import Agent
from google.adk.agents.run_config import RunConfig
from google.adk.runners import Runner
from google.adk.sessions import BaseSessionService, InMemorySessionService
from google.adk.tools.mcp_tool import McpToolset
from google.genai import types

from parts_counter.util import keys, mcp, models
from parts_counter.util.budget import Budget

APP_NAME = "parts_counter"

INSTRUCTION = (
    "You are a workshop parts counter. Answer only from the tools you are given. "
    "Read a stock level before changing it, and never change a count unless the person has "
    "clearly asked you to. If a part is not in the inventory, say so and do not guess a number."
)


def export_key() -> None:
    """Copy this project's key into the process environment, because the framework reads it there.

    `google-genai` builds its client from `os.environ` and has never heard of this project's
    `.env`. Without this, a project that reads its own file gets `ValueError: No API key was
    provided.` while the key sits on disk. The environment wins if it already has one.
    """
    if os.environ.get("GOOGLE_API_KEY") is None:
        value = keys.get("GOOGLE_API_KEY")
        if value is not None:
            os.environ["GOOGLE_API_KEY"] = value


def build_counter(toolset: McpToolset | None = None) -> Agent:
    """The agent. Its tools live in another process and are fetched when it runs."""
    return Agent(
        name="parts_counter",
        model=models.require_pinned(models.ANSWERING),
        description="A workshop parts counter that answers from an inventory behind a boundary.",
        instruction=INSTRUCTION,
        tools=[toolset if toolset is not None else mcp.over_stdio()],
    )


def run_config(budget: Budget | None = None) -> RunConfig:
    """Run settings, with ADK's bound set from this project's own budget rather than its default.

    `max_llm_calls` defaults to 500 in ADK 2.8.0 — a ceiling sized to stop an infinite loop, not to
    budget one question. `Budget.max_per_turn` is the number this project chose for that job.
    """
    return RunConfig(max_llm_calls=(budget or Budget()).max_per_turn)


def build_runner(session_service: BaseSessionService | None = None,
                 agent: Agent | None = None) -> Runner:
    """A runner for the counter. `session_service` is ADK's one required keyword argument."""
    return Runner(
        app_name=APP_NAME,
        agent=agent or build_counter(),
        session_service=session_service or InMemorySessionService(),
    )


async def ask(question: str, *, user_id: str = "local", session_id: str = "s-1") -> str:
    """Ask the counter one question and return its final answer. Needs a working key."""
    keys.require("GOOGLE_API_KEY")
    export_key()

    sessions = InMemorySessionService()
    await sessions.create_session(app_name=APP_NAME, user_id=user_id, session_id=session_id)
    runner = build_runner(sessions)

    message = types.Content(role="user", parts=[types.Part(text=question)])
    answer = ""
    async for event in runner.run_async(
        user_id=user_id, session_id=session_id, new_message=message,
        run_config=run_config(),
    ):
        if event.is_final_response() and event.content and event.content.parts:
            answer = "".join(part.text for part in event.content.parts if part.text)
    return answer
