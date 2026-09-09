# Codemap — P02 Parts Counter

**The completeness proof.** Every file in the finished project, and the day and part that prints it
whole. A file with no day is a bug: it means a line of this project exists that no document taught.

Day numbers are the curriculum's global sitting numbers. P02 runs from day 11 to day 18, so this
project's own day 1 is sitting 11.

| File | Printed by |
| --- | --- |
| `pyproject.toml` | day 11 hub §3, scaffold listing |
| `.python-version` | day 11 hub §3, scaffold listing |
| `.gitignore` | day 11 hub §3, scaffold listing |
| `.env.example` | day 11 hub §3, scaffold listing |
| `README.md` · `PROJECT.md` · `PRIMER.md` · `SETUP.md` | day 11 hub §3, scaffold listing |
| `PACKAGES.md` | day 11 hub §10, with the freshness check |
| `CODEMAP.md` | this file — day 11 hub §4 |
| `parts_counter/__init__.py` · `parts_counter/util/__init__.py` | empty; day 11 hub §3 |
| `parts_counter/util/models.py` | day 11, **recap depth** — taught deeply in P01 day 04 part 1.1; `PRIMER.md` §1 |
| `parts_counter/util/keys.py` | day 11, **recap depth** — taught deeply in P00 day 03 part 1.2; `PRIMER.md` §3 |
| `parts_counter/util/budget.py` | day 11, whole, **full depth** — new here |
| `parts_counter/util/logging.py` | day 11, whole, **full depth** — new here |
| `run.py` | day 11, whole |
| `tests/test_kit.py` | day 11, whole |
| `parts_counter/data/parts.json` | day 12, whole — synthetic |
| `parts_counter/store.py` | day 12, whole — the version with no boundary, printed on purpose |
| `parts_counter/tools.py` | day 12, whole |

## Owed by days that are not written yet

Listed so their absence is a decision on the record rather than an oversight.

| File | Owed by |
| --- | --- |
| `parts_mcp/server.py` and its tools | day 14 — the server skeleton and its first tool |
| `parts_counter/util/mcp.py` — the client side | day 17 |
| `parts_counter/agent.py` | day 17, when there is a boundary for the agent to reach through |
| `evals/` | day 17-18 |
| `Dockerfile` | day 18 — Ship D2, the stateless container |
