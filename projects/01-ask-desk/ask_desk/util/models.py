# ask_desk/util/models.py
"""This project's model registry. One exact ID per role, and nothing chooses for us.

Every agent and every raw call in this project names a model from here. Nothing anywhere calls a
provider with a model string typed inline, and nothing relies on a framework default.

Two things this file refuses to do, both deliberate:

  * It never uses an alias like `gemini-flash-latest`. The provider documents those as hot-swapped
    on every release, so an alias is a floor and not a pin — the same distinction P00 day 3 drew
    about `>=` in `pyproject.toml`.
  * It never leaves a model unset. ADK 2.8.0's built-in default is `gemini-3.5-flash`, which the
    provider's models page lists as Stable and calls "our legacy Flash model" — four generations
    behind the one below. An agent that inherits that default is not broken and not experimental;
    it is quietly old, which is harder to notice than either.

Verified against https://ai.google.dev/gemini-api/docs/models on 2026-09-09.
"""

from __future__ import annotations

from typing import Final

# The desk's one brain. Documented Stable on 2026-09-09 and described by the provider as
# "engineered for long-horizon software engineering, autonomous agents, and complex enterprise
# workflows" — which is what this project is.
ANSWERING: Final[str] = "gemini-3.8-flash"

# Every model this project is allowed to name, mapped to the date the ID was read off the
# provider's models page. `run.py check` asserts the ID a call is about to use is in here.
PINNED: Final[dict[str, str]] = {
    ANSWERING: "2026-09-09",
}

# The API version segment of every endpoint URL. Kept here rather than spelled into provider.py so
# that moving off v1beta is one edit in one file.
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
