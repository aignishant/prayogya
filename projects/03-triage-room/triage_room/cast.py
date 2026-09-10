# triage_room/cast.py
"""The three agents, and the tree they stand in.

P02 had one agent, and one agent is a function: you call it, it answers, and everything that
happened is on one stack. Three is an architecture, and an architecture has parts you did not
write. The moment `sub_agents=[...]` appears, ADK adds a tool to the parent that nothing here
declared, writes an instruction into the parent's prompt that nothing here wrote, and gives every
child a `parent_agent` back-pointer that changes what *the child* is allowed to do. None of that is
hidden — it is all readable, and `run.py cast` reads it — but none of it is in this file either.

Three agents, and the division is by **what each one is allowed to be wrong about**:

  * the **router** reads the queue and decides who should handle a ticket. It holds one tool and
    has no opinion about the answer.
  * the **classifier** puts a category and a severity on a ticket, using the desk's own vocabulary,
    which it reads from the boundary rather than carrying in its instruction.
  * the **writer** writes the reply a person will read. It sees the ticket and the precedents and
    nothing else.

**None of the three can close a ticket.** `record_triage` is on the boundary and is in no role's
tool list — the deciding is a model's job and the writing is not. What performs the write is a
plain Python node, and that is day 4's subject. This is blast radius before capability: the cast
gets exactly the reach its job needs, and the irreversible step stays in code somebody can read.

Every agent names its model from `triage_room/util/models.py`. Not one of them omits `model=`,
because in ADK 2.8.0 omitting it does not fall to the documented default — the sub-agent inherits
its parent's, and the whole cast quietly becomes one model with three names.

Verified against google-adk 2.8.0 on 2026-09-10.
"""

from __future__ import annotations

import os

from google.adk.agents import Agent
from google.adk.agents.run_config import RunConfig
from google.adk.runners import Runner
from google.adk.sessions import BaseSessionService, InMemorySessionService

from triage_room.util import keys, mcp, models
from triage_room.util.budget import Budget

APP_NAME = "triage_room"

ROUTER_INSTRUCTION = (
    "You are the front desk of a support queue. Read the open queue and say which ticket should "
    "be handled next and who should handle it: the classifier if the ticket needs a category and "
    "a severity, the writer if it only needs a reply drafting. Do not classify and do not write a "
    "reply yourself. If the queue is empty, say so."
)

CLASSIFIER_INSTRUCTION = (
    "You put a category and a severity on one support ticket. Read the ticket, then look at how "
    "similar tickets were handled before. Use only the categories and severities the queue "
    "reports — never invent one, and never use a word that is merely close. If the precedents "
    "disagree with each other, say which one you followed and why. Answer with the category, the "
    "severity, and one sentence of reasoning."
)

WRITER_INSTRUCTION = (
    "You write the reply a person will read. Read the ticket, then look at how similar tickets "
    "were answered before, and write one short reply in the same register: what happened, what "
    "has been done, and what the person should expect next. If no precedent exists, say plainly "
    "what you can and cannot confirm. Never promise a timescale the precedents do not support, "
    "and never invent a reference number."
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


def build_classifier(*, http: bool = False) -> Agent:
    """The specialist that decides what a ticket *is*.

    `output_key` is how one agent's answer reaches another's prompt: ADK writes the final text of
    this agent's turn into session state under that name, and any later instruction containing
    `{classification}` has it substituted in. It is the wire between two agents, and it is a
    string, not a schema — which is the sharp edge day 4 has to handle.
    """
    return Agent(
        name="classifier",
        model=models.for_role("classifying"),
        # The description is not documentation. It is the text a router is shown when it decides
        # whom to hand a ticket to, so it is written for that reader and no other.
        description="Assigns one of the desk's categories and severities to a ticket, using past "
                    "tickets as precedent.",
        instruction=CLASSIFIER_INSTRUCTION,
        tools=[mcp.for_agent("classifying", http=http)],
        output_key="classification",
    )


def build_writer(*, http: bool = False) -> Agent:
    """The specialist that only writes. It cannot read the queue and it cannot close anything."""
    return Agent(
        name="writer",
        model=models.for_role("writing"),
        description="Drafts the reply that will be sent to the person who opened the ticket.",
        instruction=WRITER_INSTRUCTION,
        tools=[mcp.for_agent("writing", http=http)],
        output_key="draft_reply",
    )


def build_router(*, http: bool = False, with_cast: bool = True) -> Agent:
    """The front desk.

    `with_cast=False` builds the same agent with no children, and it exists so that the difference
    between one agent and three is something you can print rather than something you are told.
    With children it runs ADK's `AutoFlow` and its prompt gains a `transfer_to_agent` tool and an
    instruction naming its two peers; without them it is `SingleFlow` and gains neither.
    """
    children = [build_classifier(http=http), build_writer(http=http)] if with_cast else []
    return Agent(
        name="router",
        model=models.for_role("routing"),
        description="Reads the open queue and decides which ticket is handled next, and by whom.",
        instruction=ROUTER_INSTRUCTION,
        tools=[mcp.for_agent("routing", http=http)],
        sub_agents=children,
    )


def run_config(budget: Budget | None = None) -> RunConfig:
    """Run settings, with ADK's bound set from this project's budget rather than its default.

    `max_llm_calls` defaults to 500 in ADK 2.8.0 — a ceiling sized to stop an infinite loop, not
    to budget one question. With three agents the distinction stops being academic: a router that
    hands to a classifier that hands back is a loop that costs two calls a lap and never trips 500.
    `Budget.max_per_turn` is the number this project chose for that job, and it is the whole cast's.
    """
    return RunConfig(max_llm_calls=(budget or Budget()).max_per_turn)


def build_runner(session_service: BaseSessionService | None = None,
                 agent: Agent | None = None) -> Runner:
    """A runner for the cast. `session_service` is ADK's one required keyword argument."""
    return Runner(
        app_name=APP_NAME,
        agent=agent or build_router(),
        session_service=session_service or InMemorySessionService(),
    )
