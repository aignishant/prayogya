# Codemap — P01 Ask Desk

**The completeness proof.** Every file in the finished project, and the day and part that prints it
whole. A file with no day is a bug: it means some line of this project exists that no document
taught, and a reader following the days alone could never have produced it.

Plan §0 rule 1: code is never referenced, only printed. This table is what makes that mechanical
instead of aspirational.

Day numbers are the curriculum's global sitting numbers. P01 runs from day 4 to day 10, so this
project's own day 1 is sitting 4.

| File | Printed by |
| --- | --- |
| `pyproject.toml` | day 04 hub §3, scaffold listing · `google-adk==2.8.0` added as a marked diff on day 06 part 1.1 |
| `.python-version` | day 04 hub §3, scaffold listing |
| `.gitignore` | day 04 hub §3, scaffold listing |
| `.env.example` | day 04 hub §3, scaffold listing |
| `README.md` | day 04 hub §3, scaffold listing |
| `PROJECT.md` | day 04 hub §3, scaffold listing |
| `PRIMER.md` | day 04 hub §3, scaffold listing |
| `SETUP.md` | day 04 hub §3, scaffold listing |
| `PACKAGES.md` | day 04 hub §10, with the freshness check |
| `CODEMAP.md` | this file — day 04 hub §4 |
| `ask_desk/__init__.py` | empty; day 04 hub §3, scaffold listing |
| `ask_desk/util/__init__.py` | empty; day 04 hub §3, scaffold listing |
| `ask_desk/util/models.py` | day 04 part 1.1, whole, full depth |
| `ask_desk/util/keys.py` | day 04 part 1.2, whole, **recap depth** — taught deeply in P00 day 03 part 1.2; `PRIMER.md` §1 |
| `ask_desk/provider.py` | day 04 part 1.3, whole · the tool helpers added as a marked diff on day 05 part 2.1 |
| `ask_desk/loop.py` | day 04 part 2.1, whole · the tool branch and the bound added as a marked diff on day 05 part 2.1 |
| `run.py` | day 04 part 2.1, whole · the `adk` subcommand added as a marked diff on day 06 part 2.1 |
| `ask_desk/tools.py` | day 05 part 1.2, whole |
| `ask_desk/data/notes.json` | day 05 part 1.2, whole — synthetic |
| `ask_desk/agent.py` | day 06 part 1.1, whole |

## Files this project does not have yet

Listed so their absence is a decision on the record rather than an oversight. Each is owed by a day
that has not been written.

| File | Owed by |
| --- | --- |
| `evals/` | day 10 — Ship D1, the first eval that can go red |
| `tests/` | day 10 |
| `Dockerfile` | not owed. P01 is deploy tier D1: `api_server` run locally. The container arrives with P02 at D2. |

## Day 07 prints nothing

That is correct and not a gap. Day 07 is `FunctionTool`, and its whole subject is reading what the
framework derived from code that days 05 and 06 already printed. A day that added a file in order to
have something in this table would be a worse day.
