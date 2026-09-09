# ask_desk/loop.py
"""Think, act, observe — the loop, written out, with nothing hidden.

The provider is stateless. It remembers nothing between calls, so the conversation is a list that
lives here, in this process, and every turn resends all of it. There is no session on the server to
attach to and no identifier to quote back. If this list is dropped, the model meets the next
question with no idea that the previous one happened.

That is the entire mechanism a framework will later perform for you, and on day 1 it is about
thirty lines and one list.

Day 1 has no tools, so `act` has nothing to do and the model's first reply is the answer. Day 2
puts the tool branch inside `Conversation.ask`, and that is where a bound on the number of provider
calls per question becomes necessary — a loop that stops when the model says it is finished is a
loop the model can decline to end.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ask_desk import provider, tools
from ask_desk.util import models

# The desk's standing orders. Sent on every single turn, because the provider is stateless and an
# instruction given once is an instruction forgotten immediately.
SYSTEM_INSTRUCTION = (
    "You are an internal IT ask desk. Answer from the notes you are given and nothing else. "
    "If the notes do not cover the question, say so plainly and do not guess."
)

# ── added on day 2, with tools ─────────────────────────────────────────────────────────────────
#
# The bound. Not a timeout and not a token budget: a count of provider calls for a single question,
# enforced here, by code the model cannot reach. A loop that ends "when the model stops asking for
# tools" ends when the model chooses to, and one that never chooses runs until the quota does.
MAX_CALLS_PER_QUESTION = 6


class LoopExhausted(RuntimeError):
    """The bound was reached before the model produced a final answer.

    Raised, never swallowed. Returning the last partial text here would turn a run that failed into
    a run that looks like it worked, and the conversation would carry no sign of it.
    """


@dataclass
class Turn:
    """One exchange, kept so that a run can be read back after it has finished."""

    number: int
    request: dict[str, Any]
    response: dict[str, Any]
    finish_reason: str | None
    text: str


def user_message(text: str) -> dict[str, Any]:
    """A `Content` with the `user` role. The provider accepts only 'user' and 'model' here."""
    return {"role": "user", "parts": [{"text": text}]}


@dataclass
class Conversation:
    """The thread, and the only place it exists.

    `contents` is the memory. It is an ordinary Python list on an ordinary Python object, and the
    provider has no copy of it.
    """

    model: str = models.ANSWERING
    system_instruction: str = SYSTEM_INSTRUCTION
    contents: list[dict[str, Any]] = field(default_factory=list)
    turns: list[Turn] = field(default_factory=list)

    #: Whether the model is offered this desk's tools. False reproduces day 1 exactly, which is
    #: how day 2 shows what changed.
    use_tools: bool = True

    #: When False, the model's replies are never appended to `contents`. That is the deliberate
    #: failure of day 1: every turn then arrives as if it were the first. It is a flag here rather
    #: than an edit you make and undo, so the broken behaviour can be run beside the working one.
    remember: bool = True

    @property
    def request_count(self) -> int:
        """Provider calls this conversation has made. The number the hub's budget section states."""
        return len(self.turns)

    def next_request(self, question: str) -> tuple[str, dict[str, Any]]:
        """Build the request this question would send, without sending it.

        Separated from `ask` so the shape of a turn can be read, diffed and asserted on with no
        key, no network and no cost — which is also how the day's failure is shown.
        """
        pending = self.contents + [user_message(question)]
        return provider.build_request(
            pending,
            model=self.model,
            system_instruction=self.system_instruction,
            tools=tools.DECLARATIONS if self.use_tools else None,
        )

    def ask(self, question: str) -> str:
        """Answer one question, running whatever tools the model asks for along the way.

        One question may take several provider calls: the model asks for a tool, we run it, hand
        the result back, and it asks again or answers. Every one of those calls resends the entire
        conversation, because the provider still remembers nothing.
        """
        self.contents.append(user_message(question))

        for _ in range(MAX_CALLS_PER_QUESTION):
            # THINK — the whole thread, plus the tools it is allowed to reach for.
            url, body = provider.build_request(
                self.contents,
                model=self.model,
                system_instruction=self.system_instruction,
                tools=tools.DECLARATIONS if self.use_tools else None,
            )
            response = provider.send(url, body)

            candidate = provider.first_candidate(response)
            text = provider.text_of(candidate)
            self.turns.append(Turn(
                number=len(self.turns) + 1,
                request=body,
                response=response,
                finish_reason=candidate.get("finishReason"),
                text=text,
            ))

            # OBSERVE — file the model's turn, whatever it was. A turn asking for a tool is part
            # of the conversation exactly as an answer is, and omitting it leaves the tool results
            # in the thread with nothing explaining why they are there.
            reply = candidate.get("content")
            if self.remember and reply is not None:
                self.contents.append(reply)

            # ACT — run every tool this turn asked for, then hand the results back and go round.
            calls = provider.function_calls(candidate)
            if not calls:
                return text
            results = [(call, tools.dispatch(call["name"], dict(call.get("args") or {})))
                       for call in calls]
            self.contents.append(provider.function_response_message(results))

        raise LoopExhausted(
            f"reached {MAX_CALLS_PER_QUESTION} provider calls for one question without a final "
            f"answer. The full conversation is in `contents` and every turn is in `turns`; the "
            f"bound stopped this, and nothing else was going to."
        )


def ask_once(question: str, *, model: str = models.ANSWERING) -> str:
    """The whole desk, for a single question with no follow-up."""
    return Conversation(model=model).ask(question)
