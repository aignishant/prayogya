# triage_room/util/models.py
"""This project's model registry. One exact ID per **role**, and nothing chooses for us.

Every agent and every raw call in this project names a model from here. Nothing anywhere calls a
provider with a model string typed inline, and nothing relies on a framework default.

Recap depth on the pin itself — a floor is not a pin, and `-latest` is a floor wearing a version's
clothes — taught in full at
`days/00-foundry/day-03-keys-pinning-refusing-check/parts/02-the-pin-and-the-refusal/2.1-a-floor-is-not-a-pin.md`.
`PRIMER.md` §6 has the self-contained version.

**What is new here is `CAST`, and it exists because this project has three agents.**

P02 had one agent and one constant. Three agents means three chances to leave `model=` off, and in
ADK 2.8.0 leaving it off does not do what it did with one agent. From the shipped source:

    model: Union[str, BaseLlm] = ''
    \"\"\"The model to use for the agent.

    When not set, the agent will inherit the model from its ancestor. If no
    ancestor provides a model, the agent uses the default model configured via
    LlmAgent.set_default_model. The built-in default is gemini-3.5-flash.
    \"\"\"
        -- google/adk/agents/llm_agent.py, google-adk 2.8.0, read 2026-09-10

Read that twice. A sub-agent with no `model=` does not fall to the documented default; it **inherits
its parent's**. That is worse than a stale default, because the result looks deliberate: the whole
cast runs on one model, every answer is plausible, and nothing anywhere says a choice was skipped.
`run.py check`'s `roles` check exists for that sentence.

The three roles all name the same ID today. That is not a redundancy waiting to be simplified — it
is three decisions that happen to have agreed this week, kept separate so that changing one is one
edit rather than a hunt. **Deliberately not built yet 🅿️:** giving the cheap role a cheaper model
and measuring what it costs in quality is P05 Bench Runner day 5, and guessing at it here would be
an unmeasured trade-off dressed as a configuration.

Verified against https://ai.google.dev/gemini-api/docs/models and the installed google-adk 2.8.0
source on 2026-09-10.
"""

from __future__ import annotations

from typing import Final

# The one ID this project is prepared to be billed for, checked on the provider's models page on
# the date in `PINNED` below. Documented Stable, and described there as "Our most intelligent Flash
# model, engineered for long-horizon software engineering, autonomous agents, and complex
# enterprise workflows".
ANSWERING: Final[str] = "gemini-3.8-flash"

#: One entry per agent this project builds, mapping the **role** to the model that plays it.
#:
#: A role is not a model. `run.py roles` prints this, `run.py check` refuses a role naming anything
#: unpinned, and every agent constructor in `triage_room/` reads its model from exactly one of
#: these keys — never from a literal, and never by omission.
CAST: Final[dict[str, str]] = {
    # Reads the ticket and decides who should handle it. Nothing else.
    "routing": ANSWERING,
    # Puts a category and a severity on a ticket, using the desk's own vocabulary.
    "classifying": ANSWERING,
    # Writes the reply the person will actually read.
    "writing": ANSWERING,
}

# Every model this project is allowed to name, mapped to the date the ID was read off the
# provider's models page. `run.py check` asserts every role's model is in here.
PINNED: Final[dict[str, str]] = {
    ANSWERING: "2026-09-10",
}

# The API version segment of every endpoint URL. Kept here so that moving off v1beta is one edit.
API_VERSION: Final[str] = "v1beta"

BASE_URL: Final[str] = "https://generativelanguage.googleapis.com"


class UnpinnedModel(RuntimeError):
    """Raised when code is about to call a model this project never wrote down."""


def require_pinned(model: str) -> str:
    """Return `model`, or refuse if it is not in `PINNED`.

    The alias check is separate and comes first, because `gemini-flash-latest` would otherwise be
    refused with a message about the registry when the real objection is that it is not a version.
    """
    if model.endswith("-latest"):
        raise UnpinnedModel(
            f"{model!r} is an alias, not a pin. The provider documents `-latest` as hot-swapped "
            f"with every release, so two runs a week apart can reach different models with no "
            f"change here. Name an exact ID from the models page and add it to PINNED."
        )
    if model not in PINNED:
        raise UnpinnedModel(
            f"{model!r} is not in this project's registry. Add it to PINNED with the date you "
            f"read it off https://ai.google.dev/gemini-api/docs/models, or use one of: "
            f"{', '.join(sorted(PINNED))}."
        )
    return model


def for_role(role: str) -> str:
    """The pinned model for one role, refusing a role this project never declared.

    Agents call this rather than reading `CAST` directly, so that a typo in an agent module is a
    named error at construction instead of a `KeyError` halfway through a turn.
    """
    if role not in CAST:
        raise UnpinnedModel(
            f"{role!r} is not a role in this project's cast. The roles are "
            f"{', '.join(sorted(CAST))}, and they are declared in one place so that three agents "
            f"cannot each invent a fourth."
        )
    return require_pinned(CAST[role])
