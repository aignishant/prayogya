# ask_desk/agent.py
"""The same desk, as an ADK agent — and the runner that drives it.

Days 1 and 2 built this by hand: a request builder, a conversation list, a tool registry, a
declaration for each tool, a dispatcher and a bound. This file replaces all of it with about twenty
lines, and the point of days 3 and 4 is knowing exactly which of those pieces went where.

What ADK takes over, and where the hand-rolled version of each lives:

    the conversation list  ->  the session, held by a SessionService   (loop.Conversation.contents)
    resending the thread   ->  the runner, on every call               (loop.Conversation.ask)
    the declarations       ->  derived from the functions themselves   (tools.DECLARATIONS)
    the dispatcher         ->  the runner, between events              (tools.dispatch)
    the bound              ->  NOT taken over. Still yours.            (loop.MAX_CALLS_PER_QUESTION)

The last row is the one worth remembering.

Verified against google-adk 2.8.0 and https://adk.dev/api-reference/python/google-adk.html
on 2026-09-09.
"""

from __future__ import annotations

import os

from google.adk.agents import Agent
from google.adk.agents.run_config import RunConfig, StreamingMode
from google.adk.models.base_llm import BaseLlm
from google.adk.runners import Runner
from google.adk.sessions import BaseSessionService, InMemorySessionService
from google.genai import types

from ask_desk import loop, tools
from ask_desk.util import keys, models

APP_NAME = "ask_desk"

#: The agent. `model` is passed explicitly and never left to be inherited: ADK 2.8.0's built-in
#: default is `gemini-3.5-flash`, which the provider lists as Stable and calls its legacy Flash
#: model. An agent that omits this line still runs, still answers, and is four generations old.
desk = Agent(
    name="ask_desk",  # must be a valid Python identifier — a space here is a ValidationError
    model=models.require_pinned(models.ANSWERING),
    description="An internal IT ask desk that answers from a synthetic knowledge base.",
    instruction=loop.SYSTEM_INSTRUCTION,
    # The plain functions from day 2. ADK wraps each one in a FunctionTool and derives its
    # declaration from the signature and the docstring — which is day 4's subject.
    tools=[tools.search_notes, tools.fetch_note, tools.check_service_status],
)


def build_desk(model: str | BaseLlm | None = None) -> Agent:
    """The desk, optionally against a stand-in model.

    Day 5 needs a model whose output is fixed so the event stream can be read the same way twice,
    and day 7's eval needs one so a red result means the code changed. Both pass a
    `ScriptedModel` here. Everything user-facing leaves this `None` and gets the pinned real one.
    """
    return Agent(
        name="ask_desk",
        model=model if model is not None else models.require_pinned(models.ANSWERING),
        description="An internal IT ask desk that answers from a synthetic knowledge base.",
        instruction=loop.SYSTEM_INSTRUCTION,
        tools=[tools.search_notes, tools.fetch_note, tools.check_service_status],
    )


def run_config(*, stream: bool = False) -> RunConfig:
    """This project's run settings, with the bound set from this project's own constant.

    `max_llm_calls` defaults to 500 in ADK 2.8.0 — a ceiling sized to stop an infinite loop, not to
    budget one question. Day 4 chose 6 for that job, so 6 is what goes here; inheriting 500 would
    mean the number that decides what a question may cost is one nobody in this project picked.
    """
    return RunConfig(
        max_llm_calls=loop.MAX_CALLS_PER_QUESTION,
        streaming_mode=StreamingMode.SSE if stream else StreamingMode.NONE,
    )


def build_runner(session_service: BaseSessionService | None = None,
                 agent: Agent | None = None) -> Runner:
    """A runner for `desk`.

    `session_service` has no default in ADK 2.8.0 — it is the one required keyword argument — and
    that is deliberate on ADK's part: an agent with nowhere to keep a conversation is an agent that
    forgets between turns, which is exactly the failure day 1 caused on purpose.
    """
    return Runner(
        app_name=APP_NAME,
        agent=agent or desk,
        session_service=session_service or InMemorySessionService(),
    )


def export_key() -> None:
    """Copy this project's key into the process environment, because the framework reads it there.

    Days 1 and 2 built `util/keys.py`, and every hand-rolled call goes through it. The framework
    does not: `google-genai` constructs its client from `os.environ` directly and has never heard
    of this project's `.env`. So a project that reads its own file and never exports the value gets
    a `ValueError: No API key was provided.` from inside a library that is looking in a different
    place from the one you filled in — and the key is right there on disk, which is what makes the
    message so confusing.

    This is the bridge, and it is deliberately one function with a name that says what it does. It
    never overwrites a value already in the environment: the precedence from day 1 is that the
    process environment wins, and a deployment that injected a real key must not have it replaced
    by whatever is in a stale `.env`.
    """
    if os.environ.get("GOOGLE_API_KEY") is None:
        value = keys.get("GOOGLE_API_KEY")
        if value is not None:
            os.environ["GOOGLE_API_KEY"] = value


async def ask(question: str, *, user_id: str = "local", session_id: str = "s-1") -> str:
    """Ask the desk one question and return its final answer.

    Async because the runner is: model calls and tool calls are I/O, and `run_async` yields events
    as they arrive rather than returning once at the end.
    """
    # `keys.require` raises MissingKey with a message naming the file, which is a better failure
    # than the library's, and it runs before any session or runner is built.
    keys.require("GOOGLE_API_KEY")
    export_key()

    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=APP_NAME, user_id=user_id, session_id=session_id)
    runner = build_runner(session_service)

    message = types.Content(role="user", parts=[types.Part(text=question)])
    answer = ""
    async for event in runner.run_async(
        user_id=user_id, session_id=session_id, new_message=message,
        run_config=run_config(),
    ):
        # `is_final_response()` marks the concluding message of the turn. Every other event is the
        # middle of the work — a tool being asked for, a tool answering, a partial chunk — and day
        # 5 is about reading those rather than skipping them.
        if event.is_final_response() and event.content and event.content.parts:
            answer = "".join(part.text for part in event.content.parts if part.text)
    return answer
