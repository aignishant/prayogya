# tests/test_kit.py
"""What the kit promises, asserted. These run in `python run.py check` and can all go red."""

from __future__ import annotations

import io
import json

import pytest

from parts_counter.util import models
from parts_counter.util.budget import Budget, BudgetExceeded
from parts_counter.util.logging import REDACTED, log


def test_registry_accepts_only_a_pinned_id() -> None:
    assert models.require_pinned(models.ANSWERING) == models.ANSWERING


def test_registry_refuses_an_alias() -> None:
    with pytest.raises(models.UnpinnedModel, match="alias, not a pin"):
        models.require_pinned("gemini-flash-latest")


def test_registry_refuses_an_unregistered_id() -> None:
    with pytest.raises(models.UnpinnedModel, match="not in this project's registry"):
        models.require_pinned("gemini-3.7-flash")


def test_budget_refuses_the_call_that_would_break_the_turn() -> None:
    budget = Budget(max_per_turn=2, max_per_run=99)
    budget.charge()
    budget.charge()
    with pytest.raises(BudgetExceeded, match="ceiling is 2"):
        budget.charge()


def test_a_refused_call_is_not_also_a_spent_one() -> None:
    """The check happens before the counter moves. Off-by-one here costs money."""
    budget = Budget(max_per_turn=1, max_per_run=99)
    budget.charge()
    with pytest.raises(BudgetExceeded):
        budget.charge()
    assert budget.spent_this_turn == 1


def test_budget_refuses_on_the_run_ceiling_too() -> None:
    budget = Budget(max_per_turn=99, max_per_run=2)
    budget.charge(2)
    with pytest.raises(BudgetExceeded, match="only one this project can be sure of"):
        budget.charge()


def test_logging_redacts_by_field_name_not_by_caller_care() -> None:
    stream = io.StringIO()
    record = log("probe", stream=stream, GOOGLE_API_KEY="abc123", part_no="BRK-0142")
    assert record["GOOGLE_API_KEY"] == REDACTED
    assert record["part_no"] == "BRK-0142"
    assert "abc123" not in stream.getvalue()


def test_logging_redacts_nested_values() -> None:
    stream = io.StringIO()
    record = log("probe", stream=stream, config={"api_key": "abc123", "region": "eu"})
    assert record["config"]["api_key"] == REDACTED
    assert record["config"]["region"] == "eu"


def test_every_line_is_one_json_object() -> None:
    stream = io.StringIO()
    log("one", stream=stream, a=1)
    log("two", stream=stream, b=2)
    lines = [line for line in stream.getvalue().splitlines() if line]
    assert len(lines) == 2
    assert [json.loads(line)["event"] for line in lines] == ["one", "two"]
