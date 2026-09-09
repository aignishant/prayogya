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

from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from ask_desk import loop, tools
from ask_desk.util import models

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


def build_runner(session_service: InMemorySessionService | None = None) -> Runner:
    """A runner for `desk`.

    `session_service` has no default in ADK 2.8.0 — it is the one required keyword argument — and
    that is deliberate on ADK's part: an agent with nowhere to keep a conversation is an agent that
    forgets between turns, which is exactly the failure day 1 caused on purpose.
    """
    return Runner(
        app_name=APP_NAME,
        agent=desk,
        session_service=session_service or InMemorySessionService(),
    )


async def ask(question: str, *, user_id: str = "local", session_id: str = "s-1") -> str:
    """Ask the desk one question and return its final answer.

    Async because the runner is: model calls and tool calls are I/O, and `run_async` yields events
    as they arrive rather than returning once at the end.
    """
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=APP_NAME, user_id=user_id, session_id=session_id)
    runner = build_runner(session_service)

    message = types.Content(role="user", parts=[types.Part(text=question)])
    answer = ""
    async for event in runner.run_async(
        user_id=user_id, session_id=session_id, new_message=message
    ):
        # `is_final_response()` marks the concluding message of the turn. Every other event is the
        # middle of the work — a tool being asked for, a tool answering, a partial chunk — and day
        # 5 is about reading those rather than skipping them.
        if event.is_final_response() and event.content and event.content.parts:
            answer = "".join(part.text for part in event.content.parts if part.text)
    return answer
