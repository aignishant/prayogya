# triage_room/util/budget.py
"""Count model calls, and refuse the one that would break the promise — across a whole cast.

Recap depth on the idea. A budget that refuses rather than warns, the split between a per-turn
ceiling and a per-run ceiling, and why the framework's own bound is a different job, are taught in
full at
`days/02-parts-counter/day-11-kit/parts/02-what-a-call-costs/2.1-a-budget-that-refuses.md`.
`PRIMER.md` §5 has the self-contained version.

**What is new here, and it is the reason this file is not P02's file copied:** P02 had one agent, so
"this turn spent four calls" named both the turn and the caller. This project has three, and a turn
that costs six calls is a different problem depending on whether one agent spent six or three agents
spent two each. So `charge` takes the agent's name and the tally is kept per agent as well as in
total. That is all it is — a label on a counter.

**Deliberately not built yet 🅿️.** What those calls *cost*: tokens in and tokens out, the quota
they draw down, and the report that turns "the cast is expensive" into a number per agent. That is
P04 Trip Ledger day 6, and writing it here would mean writing it twice. This file counts calls,
which is the unit a runaway loop is measured in and the unit this project's hubs state.
"""

from __future__ import annotations

from dataclasses import dataclass, field


class BudgetExceeded(RuntimeError):
    """Raised when a call would exceed a limit this project set for itself."""


@dataclass
class Budget:
    """A counter with two ceilings, no opinions about time, and one label per call.

    Deliberately not a rate limiter. Rate limiting is about requests per second and belongs at the
    provider boundary; this is about requests per unit of *work*, which is a question about your
    own design and is answerable without a clock.
    """

    #: One question, one turn — and in this project a turn passes through more than one agent, so
    #: this ceiling is the whole cast's, not each agent's. Three agents at two calls each is six.
    max_per_turn: int = 9
    max_per_run: int = 90
    spent_this_turn: int = 0
    spent_this_run: int = 0
    #: One entry per turn that has ended: how many calls it cost. Cheap, and it turns "the budget
    #: feels tight" into a number somebody can look at.
    history: list[int] = field(default_factory=list)
    #: Calls charged per agent name, for the whole run. This is the line that answers "which of
    #: the three spent the turn?", which with one agent was not a question.
    by_agent: dict[str, int] = field(default_factory=dict)

    def start_turn(self) -> None:
        """Close the previous turn and open a new one."""
        if self.spent_this_turn:
            self.history.append(self.spent_this_turn)
        self.spent_this_turn = 0

    def charge(self, calls: int = 1, *, agent: str = "unattributed") -> None:
        """Record `calls` model calls made by `agent`, or refuse if a ceiling would be passed.

        The check happens **before** the counter moves, so a refused call is not also a spent one.
        Charging first and checking after is the bug that makes a budget off by one in the
        direction that costs money.

        `agent` is keyword-only and defaults to `"unattributed"` rather than to the empty string:
        an unlabelled call still has to appear in the tally, because a cast whose spend does not
        add up is worse than one that is merely expensive.
        """
        if self.spent_this_turn + calls > self.max_per_turn:
            raise BudgetExceeded(
                f"this turn has spent {self.spent_this_turn} model call(s) across "
                f"{len(self.by_agent)} agent(s) and the ceiling is {self.max_per_turn}. A turn "
                f"that wants more is a cast handing work back and forth, not a question that is "
                f"hard. Spend so far: {self.spend_report()}."
            )
        if self.spent_this_run + calls > self.max_per_run:
            raise BudgetExceeded(
                f"this run has spent {self.spent_this_run} model call(s) of {self.max_per_run}. "
                f"The provider no longer publishes its free-tier limits, so this ceiling is the "
                f"only one this project can be sure of."
            )
        self.spent_this_turn += calls
        self.spent_this_run += calls
        self.by_agent[agent] = self.by_agent.get(agent, 0) + calls

    @property
    def turns(self) -> int:
        """Turns that have ended. The open turn is not counted until `start_turn` closes it."""
        return len(self.history)

    def spend_report(self) -> str:
        """Per-agent spend, heaviest first, as one readable clause."""
        if not self.by_agent:
            return "nothing charged yet"
        ordered = sorted(self.by_agent.items(), key=lambda pair: (-pair[1], pair[0]))
        return ", ".join(f"{name} {count}" for name, count in ordered)

    def report(self) -> str:
        """One line, for the end of a run. States the numbers rather than describing them."""
        worst = max(self.history, default=self.spent_this_turn)
        return (f"{self.spent_this_run} model call(s) across {self.turns} completed turn(s); "
                f"worst turn {worst} of {self.max_per_turn}; run ceiling {self.max_per_run}; "
                f"by agent: {self.spend_report()}")
