# parts_counter/util/budget.py
"""Count model calls, and refuse the one that would break the promise.

Every hub in this curriculum has stated a request budget since day 4, and until now that number
lived only in prose. This file is where it becomes arithmetic.

Two things are counted, and they are different questions:

  * **Per turn** — how many model calls one question may cost. This is the number the hub states,
    and it is the one a runaway loop breaks.
  * **Per run** — how many this process may make in total before it stops. This is the one that
    protects a quota you cannot see, because the provider stopped publishing its limits (see
    `PACKAGES.md`), so the only ceiling anybody can be sure of is the one you impose.

Both refuse by raising. A budget that logs a warning and carries on is a budget that has already
been spent by the time anybody reads the log.

The framework has a bound of its own — ADK's `RunConfig.max_llm_calls`, default 500 — and it is
not a substitute for this one. It stops an infinite loop; it does not answer "what may one
question cost?". Both are set, from the same constants, in `parts_counter/agent.py`.
"""

from __future__ import annotations

from dataclasses import dataclass, field


class BudgetExceeded(RuntimeError):
    """Raised when a call would exceed a limit this project set for itself."""


@dataclass
class Budget:
    """A counter with two ceilings and no opinions about time.

    Deliberately not a rate limiter. Rate limiting is about requests per second and belongs at the
    provider boundary; this is about requests per unit of *work*, which is a question about your
    own design and is answerable without a clock.
    """

    max_per_turn: int = 6
    max_per_run: int = 60
    spent_this_turn: int = 0
    spent_this_run: int = 0
    #: One entry per turn that has ended: how many calls it cost. Cheap, and it turns "the budget
    #: feels tight" into a number somebody can look at.
    history: list[int] = field(default_factory=list)

    def start_turn(self) -> None:
        """Close the previous turn and open a new one."""
        if self.spent_this_turn:
            self.history.append(self.spent_this_turn)
        self.spent_this_turn = 0

    def charge(self, calls: int = 1) -> None:
        """Record `calls` model calls, or refuse if either ceiling would be passed.

        The check happens **before** the counter moves, so a refused call is not also a spent one.
        Charging first and checking after is the bug that makes a budget off by one in the
        direction that costs money.
        """
        if self.spent_this_turn + calls > self.max_per_turn:
            raise BudgetExceeded(
                f"this turn has spent {self.spent_this_turn} model call(s) and the ceiling is "
                f"{self.max_per_turn}. A turn that wants more is a loop that is not ending, not a "
                f"question that is hard."
            )
        if self.spent_this_run + calls > self.max_per_run:
            raise BudgetExceeded(
                f"this run has spent {self.spent_this_run} model call(s) of {self.max_per_run}. "
                f"The provider no longer publishes its free-tier limits, so this ceiling is the "
                f"only one this project can be sure of."
            )
        self.spent_this_turn += calls
        self.spent_this_run += calls

    @property
    def turns(self) -> int:
        """Turns that have ended. The open turn is not counted until `start_turn` closes it."""
        return len(self.history)

    def report(self) -> str:
        """One line, for the end of a run. States the numbers rather than describing them."""
        worst = max(self.history, default=self.spent_this_turn)
        return (f"{self.spent_this_run} model call(s) across {self.turns} completed turn(s); "
                f"worst turn {worst} of {self.max_per_turn}; run ceiling {self.max_per_run}")
