# ask_desk/provider.py
"""One turn against the provider: build a request, send it, read the reply. No framework.

This is the whole surface this project uses on day 1, written with the standard library only, so
that nothing between your code and the wire is hidden.

The endpoint is `generateContent`, which is **stateless**: it holds no memory of previous calls, so
every turn resends the entire conversation. That is not a limitation to work around — it is the
reason the loop in `loop.py` is visible code rather than something the server does for you.

The provider now recommends a newer, stateful Interactions API for new development. Its migration
page says, on 2026-09-09, that `generateContent` "remains fully supported"; the endpoint's own
reference page is live and it is absent from the deprecations list. This project uses it
deliberately, and `PROJECT.md` says why.

Verified against https://ai.google.dev/api/generate-content on 2026-09-09.
"""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any

from ask_desk.util import keys, models


class ProviderError(RuntimeError):
    """A request reached the provider and the provider refused it.

    Carries the HTTP status and the parsed body, because code that retries needs the status and a
    human reading the log needs the message, and collapsing them loses one or the other.
    """

    def __init__(self, status: int, body: dict[str, Any]) -> None:
        error = body.get("error", {})
        self.status = status
        self.code = error.get("code")
        self.message = error.get("message", "")
        self.body = body
        super().__init__(f"HTTP {status}: {self.message or body!r}")


def build_request(
    contents: list[dict[str, Any]],
    *,
    model: str = models.ANSWERING,
    system_instruction: str | None = None,
    tools: list[dict[str, Any]] | None = None,
) -> tuple[str, dict[str, Any]]:
    """Return the (url, body) this turn would send. Sends nothing.

    Split out from `send` on purpose: a function that builds a request and a function that performs
    one are two different things to test, and only one of them needs the network or a key.
    """
    models.require_pinned(model)
    url = f"{models.BASE_URL}/{models.API_VERSION}/models/{model}:generateContent"
    body: dict[str, Any] = {"contents": contents}
    if system_instruction is not None:
        body["system_instruction"] = {"parts": [{"text": system_instruction}]}
    if tools:
        body["tools"] = [{"function_declarations": tools}]
    return url, body


def send(url: str, body: dict[str, Any], *, timeout: int = 60) -> dict[str, Any]:
    """POST the body and return the parsed response, or raise `ProviderError`."""
    request = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            # The key travels in a header, never in the query string: a key in a URL is a key in
            # the server's access log, in your shell history, and in every proxy in between.
            "x-goog-api-key": keys.require("GOOGLE_API_KEY"),
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            parsed = {"error": {"message": raw}}
        raise ProviderError(exc.code, parsed) from exc


def first_candidate(response: dict[str, Any]) -> dict[str, Any]:
    """The one candidate this project ever asks for, or a clear failure saying there was none.

    A response with no candidates is a real outcome — the prompt was blocked, or generation stopped
    before anything was produced — and `response["candidates"][0]` would meet it with an IndexError
    that names nothing.
    """
    candidates = response.get("candidates") or []
    if not candidates:
        feedback = response.get("promptFeedback", {})
        raise ProviderError(200, {"error": {
            "message": f"the response carried no candidates; promptFeedback={feedback!r}"}})
    return candidates[0]


def text_of(candidate: dict[str, Any]) -> str:
    """Join every text part of a candidate. Parts that are not text are skipped, not stringified."""
    parts = candidate.get("content", {}).get("parts", [])
    return "".join(part["text"] for part in parts if "text" in part)


# ── added on day 2, for tools ──────────────────────────────────────────────────────────────────

def function_calls(candidate: dict[str, Any]) -> list[dict[str, Any]]:
    """Every `functionCall` part in a candidate, in the order the model produced them.

    A list, not an optional single call: one turn may ask for several tools at once, and code that
    reads `parts[0]` runs the first and silently discards the rest.
    """
    parts = candidate.get("content", {}).get("parts", [])
    return [part["functionCall"] for part in parts if "functionCall" in part]


def function_response_message(calls_and_results: list[tuple[dict[str, Any], dict[str, Any]]],
                              ) -> dict[str, Any]:
    """Build the turn that hands tool results back to the model.

    One message carrying one part per call, in the order they were requested. The provider matches
    a result to its call by `name`, and by `id` when the call carried one, so both are echoed back
    exactly as received rather than reconstructed.
    """
    parts = []
    for call, result in calls_and_results:
        response_part: dict[str, Any] = {"name": call["name"], "response": result}
        if "id" in call:
            response_part["id"] = call["id"]
        parts.append({"functionResponse": response_part})
    return {"role": "user", "parts": parts}
