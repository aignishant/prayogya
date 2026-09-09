# Pin ledger — Prayoga

Append-only. **Never invent a fact** (plan section 2, Principle 6). Every version, tool, limit or
quota this curriculum depends on gets a row here with the value **actually observed**, the date it
was observed, the day that added it, and why.

If a value could not be looked up, the row says `TODO(<the exact lookup command>)` — never a
guess. A guess that happens to be right is still a guess, and the next reader cannot tell which
kind they are holding.

**Two ledgers, deliberately.** This one is the *authoring* repository: the tools that write and
check the curriculum. Every project pins independently in its own `PACKAGES.md`, and two projects
may legitimately sit on different pins — that is what independence means (plan section 9).

A later row may **supersede** an earlier one: a dated observation superseding a dated observation
is not an amendment, it is the ledger doing its job. Say so in the Why column.

| What | Value | Date observed | Day | Why, and how it was observed |
| ---- | ----- | ------------- | --- | ---------------------------- |
| Python | 3.12.10 | 2026-09-08 | 0 | The interpreter `p.py` runs under. `python --version`. Needs 3.11 or newer for `tomllib`. |
| uv | 0.12.3 | 2026-09-08 | 0 | The one binary that owns every project environment. `uv --version`. |
| git | 2.54.0.windows.1 | 2026-09-08 | 0 | The history is the memory; one day, one commit. `git --version`. |
| CPython (uv-managed) | 3.12.12 | 2026-09-08 | 1 | The interpreter `uv sync` and `uv run` select inside a project, and **not** the 3.12.10 the bare name `python` resolves to on this machine. `uv python find` / `uv python list`. Does not supersede the day-0 Python row: that one is the interpreter `p.py` runs under, and the two are different files. |
| platformdirs | 4.11.7 | 2026-09-08 | 1 | P00 Foundry's one dependency, added to make the wrong command fail visibly. `uv add platformdirs`. Recorded here rather than in a project `PACKAGES.md` because P00 is reference-only and has none yet; from P01 every project pins in its own. |
| platformdirs | 4.11.8 | 2026-09-09 | 3 | Supersedes the 4.11.7 row day 1 wrote. Nothing was edited: `pyproject.toml` said `>=4.11.8`, 4.11.8 was published at 22:20 UTC on 2026-09-08, and the next resolution took it. Now pinned with `==`, and the drift is what part 2.1 teaches. `importlib.metadata.version('platformdirs')`. |
| CPython (uv-managed) | 3.12.12 | 2026-09-09 | 3 | Re-observed, and now written into `projects/00-foundry/.python-version` rather than left to `requires-python = ">=3.12"` to resolve. Does not supersede the day-1 row: same value, now pinned in a file instead of chosen by a resolver. |
| MCP specification | 2026-07-28 | 2026-09-10 | 13 | The **current** revision, read from `https://modelcontextprotocol.io/docs/learn/versioning`. Recorded here because it is a fact about the world, not about a project. P02 cannot run it: `google-adk` 2.8.0 pins `mcp<2`, and the 1.x line is a legacy-era implementation speaking `2025-11-25`. That gap is ADR-0005, and P02's own `PACKAGES.md` carries the project-level pins. |

