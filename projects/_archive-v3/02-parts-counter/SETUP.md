# Setup — P02 Parts Counter

Every command from a bare machine to a green check. No step refers to another project.
This is a listing, not a lesson: day 1 explains the parts that matter.

Verified on this machine on 2026-09-10 — uv 0.12.3, CPython 3.12.12, git 2.54.0.windows.1.

## 1 · The toolchain

```bash
# Windows (PowerShell):  irm https://astral.sh/uv/install.ps1 | iex
# macOS / Linux:         curl -LsSf https://astral.sh/uv/install.sh | sh
uv --version              # expect 0.12.3 or newer
```

## 2 · The project

```bash
cd projects/02-parts-counter
uv python pin 3.12.12     # writes .python-version; requires-python is a floor, not a pin
uv sync --frozen          # builds .venv from uv.lock exactly, resolving nothing
```

## 3 · The key

One free Google AI Studio API key, from `https://aistudio.google.com/apikey`:

```bash
cp .env.example .env
# then edit .env so the line reads GOOGLE_API_KEY=<your key>
```

`.env` is covered by this project's `.gitignore`. `.env.example` is committed and holds the *names*
with no values after the `=`. There is no `GOOGLE_GENAI_USE_VERTEXAI` line and there should not be:
the AI Studio path is configured by `GOOGLE_API_KEY` alone. Checked against
`https://adk.dev/agents/models/google-gemini/` on 2026-09-10.

Days 1 and 2 make **no model calls at all**, so you can reach a green check with the placeholder
still in place.

## 4 · The check

```bash
uv run --frozen python run.py check
echo $?                   # 0 green, 1 red, 2 you typed the command wrong
```

Six checks, all of which must be green: `keys`, `interpreter`, `pins`, `lock`, `model`, `tests`.

`--frozen` is not optional. Without it `uv run` updates the lockfile before your command starts, and
the `lock` check then reports on a repository the invocation just repaired.

## 5 · Running it

```bash
uv run --frozen python run.py parts filter   # find parts, no model in the way
uv run --frozen python run.py race           # day 2's concurrent-write demonstration
uv run --frozen python run.py mcp            # the boundary server on stdio
uv run --frozen python run.py mcp --http     # the same server on Streamable HTTP at :8090/mcp
uv run --frozen python run.py probe          # list and call its tools across a process boundary
```

None of those needs a key. `probe` starts the server itself as a subprocess, so it is the quickest
way to confirm the boundary works after a fresh clone.

`race` writes to the synthetic inventory and restores it. From day 3 onward it should report
`parts unaccounted : 0` and no crashed reads; on days 1 and 2 it did neither, and that difference is
what the boundary bought.

## What you do not need

No database, no Docker on day 1, no cloud project, no billing account. The container arrives on
day 8 (tier D2). All data is synthetic and lives in `parts_counter/data/parts.json`.
