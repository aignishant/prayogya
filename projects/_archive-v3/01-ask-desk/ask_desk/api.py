# ask_desk/api.py
"""The D1 surface: the desk behind HTTP, and a health endpoint that means something.

Two endpoints, and the small one is the one worth arguing about.

`/healthz` answers the question an orchestrator actually asks, which is **"should I send this
process traffic, or restart it?"** — not "is everything downstream well?". So it checks only what
this process can fix by restarting: that the module graph imported, that the agent was built, and
that the model it will call is one this project pinned. It does **not** call the provider, and it
does not read a key.

That restraint is the whole lesson. A health check that calls the model is a health check that goes
red when the provider has a bad minute, and the orchestrator responds by killing a process that was
working perfectly and starting a new one that will also fail — turning somebody else's blip into
your outage, and doing it at whatever rate your liveness probe runs. The rule: **a health check
must not depend on anything a restart cannot fix.**

`/ask` is the real work and needs a key. Its failures are reported as failures — a provider refusal
comes back as a 502 with the provider's own message, never as a cheerful answer with the error
swallowed.

Verified against fastapi 0.141.1 and uvicorn 0.52.4 on 2026-09-10.
"""

from __future__ import annotations

from fastapi import FastAPI, HTTPException
from google.genai import errors as genai_errors
from pydantic import BaseModel, Field

from ask_desk import agent, loop
from ask_desk.util import keys, models

app = FastAPI(title="Ask Desk", version="0.1.0")


class Question(BaseModel):
    """One question, and the session it belongs to."""

    question: str = Field(min_length=1, max_length=2000)
    session_id: str = "s-1"
    user_id: str = "local"


class Answer(BaseModel):
    """The answer, and the two numbers a caller needs to reason about cost."""

    answer: str
    model: str
    max_calls_per_question: int


@app.get("/healthz")
def healthz() -> dict[str, object]:
    """Liveness and readiness for this process only. No network, no key, no model call."""
    return {
        "status": "ok",
        "agent": agent.desk.name,
        # The pinned ID, read back through the registry, so a model this project never wrote down
        # cannot reach production behind a green health check.
        "model": models.require_pinned(agent.desk.model),
        "max_calls_per_question": loop.MAX_CALLS_PER_QUESTION,
        # Whether the key is *wired*, which is all a local check can decide (P00 day 3 part 1.2).
        # Reported as a fact, never as a reason to fail: a missing key is a broken deployment, and
        # restarting the process will not produce one.
        "key_wired": keys.get("GOOGLE_API_KEY") is not None,
    }


@app.post("/ask", response_model=Answer)
async def ask(request: Question) -> Answer:
    """Answer one question. Needs a working key; failures surface as failures."""
    try:
        answer = await agent.ask(
            request.question, user_id=request.user_id, session_id=request.session_id)
    except keys.MissingKey as exc:
        # 503, not 500: the process is fine and the deployment is not. The distinction is what
        # tells an operator whether to look at the code or at the environment.
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except genai_errors.ClientError as exc:
        raise HTTPException(status_code=502, detail=f"the provider refused this request: {exc}"
                            ) from exc
    return Answer(
        answer=answer,
        model=str(agent.desk.model),
        max_calls_per_question=loop.MAX_CALLS_PER_QUESTION,
    )
