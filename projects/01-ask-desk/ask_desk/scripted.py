# ask_desk/scripted.py
"""A local stand-in model that replays a fixed script. No network, no key, no cost.

This is a **test double**, and saying so plainly is the point of the file. It is not a model, it
does not think, and nothing it produces is evidence about what a real model would do. What it is
good for is everything downstream of the model: the events the runner emits, the order they arrive
in, which of them is final, what a tool call and its result look like going past, whether a bound
fires, and whether an eval scores the run correctly.

Those are the parts you have to be able to reproduce exactly, and a real model is the wrong
instrument for studying them — every run differs, every run costs quota, and a run needs a key.
Here the script is written by you, so a test that goes red went red because your code changed.

Two rules that keep it honest:

  * **It never appears in an answer.** `run.py ask` and `run.py adk` always use the pinned real
    model from `util/models.py`. Only `run.py events`, `run.py eval` and the tests reach for this.
  * **Its `model` string starts with `scripted/`**, so any transcript, log line or event that came
    from it says so on its face and cannot be mistaken for a provider response.

All scripts here are synthetic, as all data in this curriculum is.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, AsyncGenerator, Literal

from google.adk.models.base_llm import BaseLlm
from google.adk.models.llm_request import LlmRequest
from google.adk.models.llm_response import LlmResponse
from google.genai import types


@dataclass
class Say:
    """One scripted turn: answer with this text."""

    text: str
    kind: Literal["say"] = "say"


@dataclass
class Fail:
    """One scripted turn: raise, the way a provider outage or a refusal reaches your code.

    Day 6 uses this to ask what a runner does with an exception raised inside a model call, and
    whether the failure reaches the caller or is quietly turned into an answer.
    """

    message: str
    kind: Literal["fail"] = "fail"


@dataclass
class CallTool:
    """One scripted turn: ask for this tool with these arguments."""

    name: str
    args: dict[str, Any] = field(default_factory=dict)
    kind: Literal["call"] = "call"


class ScriptedModel(BaseLlm):
    """Replays `script` one step per model call. The last step repeats if the run goes further."""

    # BaseLlm is a pydantic model, so state declared here has to be declared as a field. The
    # underscore name keeps it out of the schema ADK serialises for a model.
    _script: list[Say | CallTool | Fail] = []
    _calls: int = 0

    def __init__(self, script: list[Say | CallTool | Fail], *, name: str = "demo") -> None:
        super().__init__(model=f"scripted/{name}")
        # `object.__setattr__` because pydantic guards attribute assignment on the model; these two
        # are bookkeeping for the double and are deliberately not part of its schema.
        object.__setattr__(self, "_script", list(script))
        object.__setattr__(self, "_calls", 0)

    @property
    def calls(self) -> int:
        """How many times the runner has asked this model for a turn."""
        return self._calls

    async def generate_content_async(
        self, llm_request: LlmRequest, stream: bool = False
    ) -> AsyncGenerator[LlmResponse, None]:
        """Yield the next scripted turn.

        Non-streaming yields exactly one complete response. Streaming yields one partial response
        per word and then one complete one, which is the shape ADK documents and the shape day 5
        of this project needs in order to show what `partial` means.
        """
        step = self._script[min(self._calls, len(self._script) - 1)]
        object.__setattr__(self, "_calls", self._calls + 1)

        if isinstance(step, Fail):
            raise RuntimeError(step.message)

        if isinstance(step, CallTool):
            yield LlmResponse(content=types.Content(role="model", parts=[
                types.Part(function_call=types.FunctionCall(name=step.name, args=dict(step.args)))
            ]))
            return

        if not stream:
            yield LlmResponse(
                content=types.Content(role="model", parts=[types.Part(text=step.text)]))
            return

        words = step.text.split(" ")
        for index, word in enumerate(words):
            chunk = word if index == len(words) - 1 else word + " "
            yield LlmResponse(
                content=types.Content(role="model", parts=[types.Part(text=chunk)]),
                partial=True,
            )
        yield LlmResponse(
            content=types.Content(role="model", parts=[types.Part(text=step.text)]),
            turn_complete=True,
        )


#: The script the event walkthrough and the eval both run against: look the service up, then answer
#: from what came back. Two model calls, one tool call, one final answer.
LOOKS_IT_UP = [
    CallTool("check_service_status", {"service": "vpn"}),
    Say("The VPN is degraded: there is a known split tunnelling issue, and the gateway is up."),
]

#: A model that asks for the same tool for ever. Nothing here stops; the bound has to.
NEVER_STOPS = [CallTool("check_service_status", {"service": "vpn"})]

#: A model that answers without looking anything up — the ungrounded answer an eval must catch.
GUESSES = [Say("Yes, the VPN is completely down and engineering is aware.")]

#: A model that fails on the second call, after a tool has already run. The interesting case: some
#: work succeeded, and the question is what the caller is told about the part that did not.
FAILS_AFTER_A_TOOL = [
    CallTool("check_service_status", {"service": "vpn"}),
    Fail("the provider closed the connection"),
]
