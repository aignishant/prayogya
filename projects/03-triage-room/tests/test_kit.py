# tests/test_kit.py
"""What the kit promises, asserted. These run in `python run.py check` and can all go red."""

from __future__ import annotations

import io
import json

import pytest

from triage_room.util import models
from triage_room.util.budget import Budget, BudgetExceeded
from triage_room.util.logging import REDACTED, log


def test_every_role_in_the_cast_is_pinned() -> None:
    """The check `run.py roles` reads. Three agents means three chances to inherit a default."""
    for role, model in models.CAST.items():
        assert models.require_pinned(model) == model, role


def test_the_cast_names_every_agent_this_project_will_build() -> None:
    assert set(models.CAST) == {"routing", "classifying", "writing"}


def test_registry_refuses_an_alias() -> None:
    with pytest.raises(models.UnpinnedModel, match="alias, not a pin"):
        models.require_pinned("gemini-flash-latest")


def test_registry_refuses_an_unregistered_id() -> None:
    with pytest.raises(models.UnpinnedModel, match="not in this project's registry"):
        models.require_pinned("gemini-3.7-flash")


def test_budget_refuses_the_call_that_would_break_the_turn() -> None:
    budget = Budget(max_per_turn=2)
    budget.charge(agent="router")
    budget.charge(agent="classifier")
    with pytest.raises(BudgetExceeded, match="ceiling is 2"):
        budget.charge(agent="writer")


def test_a_refused_call_is_not_also_a_spent_one() -> None:
    """Check before the counter moves. The other order is off by one, and costs money."""
    budget = Budget(max_per_turn=1)
    budget.charge(agent="router")
    with pytest.raises(BudgetExceeded):
        budget.charge(agent="writer")
    assert budget.spent_this_turn == 1
    assert "writer" not in budget.by_agent


def test_the_tally_says_which_agent_spent_the_turn() -> None:
    """The line that did not exist with one agent: six calls, and now you know whose."""
    budget = Budget()
    budget.charge(3, agent="classifier")
    budget.charge(2, agent="writer")
    budget.charge(agent="router")
    assert budget.by_agent == {"classifier": 3, "writer": 2, "router": 1}
    assert budget.spend_report() == "classifier 3, writer 2, router 1"


def test_an_unlabelled_call_still_lands_in_the_tally() -> None:
    budget = Budget()
    budget.charge()
    assert budget.by_agent == {"unattributed": 1}


def test_the_turn_ceiling_is_the_whole_cast_not_each_agent() -> None:
    """Three agents at four calls each is twelve, and twelve is over the ceiling."""
    budget = Budget()
    with pytest.raises(BudgetExceeded):
        for agent in ("router", "classifier", "writer"):
            budget.charge(4, agent=agent)
    assert budget.spent_this_turn <= budget.max_per_turn


def test_the_log_line_says_which_agent_wrote_it() -> None:
    stream = io.StringIO()
    record = log("classified", agent="classifier", ticket="TR-0004", stream=stream)
    assert record["agent"] == "classifier"
    assert json.loads(stream.getvalue())["agent"] == "classifier"


def test_the_agent_name_is_not_optional() -> None:
    """A label that can be omitted is a label that is missing on the lines you want to read."""
    with pytest.raises(TypeError):
        log("classified", ticket="TR-0004")  # type: ignore[call-arg]


def test_a_credential_never_reaches_the_log_whatever_it_is_called() -> None:
    stream = io.StringIO()
    record = log("call", agent="router", GOOGLE_API_KEY="AIza-not-real",
                 nested={"auth_token": "also-not-real", "ticket": "TR-0001"}, stream=stream)
    assert record["GOOGLE_API_KEY"] == REDACTED
    assert record["nested"]["auth_token"] == REDACTED
    assert record["nested"]["ticket"] == "TR-0001"
    assert "not-real" not in stream.getvalue()
