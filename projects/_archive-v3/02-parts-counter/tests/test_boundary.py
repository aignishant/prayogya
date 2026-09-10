# tests/test_boundary.py
"""What the boundary's store promises, asserted. These run in `python run.py check`."""

from __future__ import annotations

import json
import threading

import pytest

from parts_mcp import store


@pytest.fixture
def inventory():
    """Restore the synthetic inventory after any test that writes to it."""
    before = store.PARTS_FILE.read_text(encoding="utf-8")
    yield
    store.PARTS_FILE.write_text(before, encoding="utf-8")


def test_get_refuses_an_unknown_part() -> None:
    with pytest.raises(store.PartNotFound):
        store.get("NOPE-0000")


def test_find_is_case_insensitive_on_number_and_name() -> None:
    assert [p["part_no"] for p in store.find("brk")] == ["BRK-0142", "BRK-0143"]
    assert [p["part_no"] for p in store.find("TIMING BELT")] == ["BLT-0310"]


def test_adjust_changes_the_count_and_persists_it(inventory) -> None:
    before = store.get("FLT-0071")["on_hand"]
    store.adjust("FLT-0071", -3)
    assert store.get("FLT-0071")["on_hand"] == before - 3
    assert json.loads(store.PARTS_FILE.read_text(encoding="utf-8"))


def test_two_writers_lose_nothing(inventory) -> None:
    """Day 2's failure, as a test. Twenty issues from two threads; twenty come off the count."""
    part = "SPK-0055"
    start = store.get(part)["on_hand"]
    errors: list[str] = []

    def issue() -> None:
        for _ in range(10):
            try:
                store.adjust(part, -1)
            except Exception as exc:  # noqa: BLE001 - the assertion is that there are none
                errors.append(type(exc).__name__)

    left, right = threading.Thread(target=issue), threading.Thread(target=issue)
    left.start(); right.start(); left.join(); right.join()

    assert errors == []
    assert store.get(part)["on_hand"] == start - 20


def test_a_reader_never_sees_a_half_written_file(inventory) -> None:
    """The torn read from day 2. Readers run while a writer rewrites the whole document."""
    part = "SPK-0055"
    failures: list[str] = []
    stop = threading.Event()

    def write() -> None:
        for _ in range(30):
            store.adjust(part, 1)
            store.adjust(part, -1)
        stop.set()

    def read() -> None:
        while not stop.is_set():
            try:
                store.all_parts()
            except Exception as exc:  # noqa: BLE001
                failures.append(type(exc).__name__)

    writer, reader = threading.Thread(target=write), threading.Thread(target=read)
    writer.start(); reader.start(); writer.join(); reader.join()

    assert failures == []
