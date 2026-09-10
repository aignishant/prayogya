# tests/test_boundary.py
"""What the boundary promises, asserted. These run in `python run.py check`."""

from __future__ import annotations

import json
import threading

import pytest

from desk_mcp import server, store
from triage_room.util import mcp as client


@pytest.fixture
def queue():
    """Restore the synthetic queue after any test that writes to it."""
    before = store.TICKETS_FILE.read_text(encoding="utf-8")
    yield
    store.TICKETS_FILE.write_text(before, encoding="utf-8")


def test_the_queue_is_only_the_open_tickets() -> None:
    ids = [t["ticket_id"] for t in store.open_tickets()]
    assert ids == ["TR-0001", "TR-0002", "TR-0003", "TR-0004", "TR-0005", "TR-0006"]


def test_get_refuses_an_unknown_ticket() -> None:
    with pytest.raises(store.TicketNotFound):
        store.get("TR-9999")


def test_a_precedent_is_found_by_overlapping_words() -> None:
    """Crude on purpose. The assertion is that it finds *something*, not that it is clever."""
    hits = store.similar("Charged twice for the September plan duplicate charges", k=3)
    assert "TR-0900" in [t["ticket_id"] for t in hits]


def test_no_precedent_is_an_empty_list_not_an_error() -> None:
    assert store.similar("xylophone tessellation", k=3) == []


def test_a_precedent_is_never_an_open_ticket() -> None:
    """A queue that cites itself as evidence is a queue that agrees with its own guesses."""
    for hit in store.similar("sign-in code phone replaced", k=5):
        assert hit["status"] == "closed"


def test_the_vocabulary_lives_with_the_data(queue) -> None:
    """A category the desk does not use is refused, and the refusal names the list."""
    with pytest.raises(store.InvalidTriage, match="not a category this desk uses"):
        store.record_triage("TR-0001", "escalations", "high", "We will look into it.")


def test_a_severity_the_desk_does_not_use_is_refused(queue) -> None:
    with pytest.raises(store.InvalidTriage, match="not a severity this desk uses"):
        store.record_triage("TR-0001", "billing", "catastrophic", "We will look into it.")


def test_an_empty_reply_closes_nothing(queue) -> None:
    with pytest.raises(store.InvalidTriage, match="empty reply"):
        store.record_triage("TR-0001", "billing", "normal", "   ")


def test_recording_a_triage_closes_the_ticket_and_persists_it(queue) -> None:
    result = store.record_triage("TR-0004", "how-to", "low", "Billing history has an export.")
    assert result["status"] == "closed"
    assert store.get("TR-0004")["reply"] == "Billing history has an export."
    assert "TR-0004" not in [t["ticket_id"] for t in store.open_tickets()]
    assert json.loads(store.TICKETS_FILE.read_text(encoding="utf-8"))


def test_two_agents_writing_at_once_lose_nothing(queue) -> None:
    """The failure this project gets for free: a classifier and a writer closing tickets together."""
    errors: list[str] = []

    def close(ticket_ids: list[str]) -> None:
        for ticket_id in ticket_ids:
            try:
                store.record_triage(ticket_id, "how-to", "low", f"Handled {ticket_id}.")
            except Exception as exc:  # noqa: BLE001 - the assertion is that there are none
                errors.append(f"{type(exc).__name__}: {exc}")

    left = threading.Thread(target=close, args=(["TR-0001", "TR-0002", "TR-0003"],))
    right = threading.Thread(target=close, args=(["TR-0004", "TR-0005", "TR-0006"],))
    left.start(); right.start(); left.join(); right.join()

    assert errors == []
    assert store.open_tickets() == []


def test_the_server_reports_an_unknown_ticket_rather_than_raising() -> None:
    """A tool that raises gives the model a traceback. A tool that answers gives it a fact."""
    answer = server.fetch_ticket("TR-9999")
    assert "error" in answer
    assert "TR-0001" in answer["open_now"]


def test_every_role_has_a_tool_list_and_none_of_them_can_write() -> None:
    """The write is not an agent's to make. It belongs to a node, and that is day 4's subject."""
    for role, allowed in client.TOOLS_FOR_ROLE.items():
        assert allowed, role
        assert "record_triage" not in allowed, role


def test_a_role_the_project_never_declared_is_refused_by_name() -> None:
    with pytest.raises(client.UnknownRole, match="has no tool list"):
        client.for_agent("summarising")
