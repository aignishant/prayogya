# Setup — P01 Ask Desk

Every command from a bare machine to a green check. No step refers to another project.
This is a listing, not a lesson: day 1 explains the parts that matter.

Verified on this machine on 2026-09-09 — uv 0.12.3, CPython 3.12.12, git 2.54.0.windows.1.

## 1 · The toolchain

```bash
# uv owns every environment. One binary, installed once, outside any project.
# Windows (PowerShell):  irm https://astral.sh/uv/install.ps1 | iex
# macOS / Linux:         curl -LsSf https://astral.sh/uv/install.sh | sh
uv --version              # expect 0.12.3 or newer
```

## 2 · The project

```bash
cd projects/01-ask-desk
uv python pin 3.12.12     # writes .python-version; requires-python is a floor, not a pin
uv sync --frozen          # builds .venv from uv.lock exactly, resolving nothing
```

## 3 · The key

You need one free Google AI Studio API key. Create it at `https://aistudio.google.com/apikey`
and put it in a `.env` that is never committed:

```bash
cp .env.example .env
# then edit .env so the line reads GOOGLE_API_KEY=<your key>
```

`.env` is already covered by this project's `.gitignore`. `.env.example` is committed and holds
the *names* with no values after the `=`.

There is no `GOOGLE_GENAI_USE_VERTEXAI` line and there should not be: the AI Studio path is
configured by `GOOGLE_API_KEY` alone. Checked against `https://adk.dev/agents/models/google-gemini/`
on 2026-09-09.

## 4 · The check

```bash
uv run --frozen python run.py check
echo $?                   # 0 green, 1 red, 2 you typed the command wrong
```

Five checks, all of which must be green: `keys`, `interpreter`, `pins`, `lock`, `model`.

`--frozen` is not optional. Without it `uv run` updates the lockfile before your command starts,
and the `lock` check then reports on a repository the invocation just repaired.

## 5 · Running the desk

```bash
uv run --frozen python run.py plan "Is the VPN down?"   # prints the request, sends nothing
uv run --frozen python run.py ask  "Is the VPN down?"   # the hand-rolled desk  (days 1-2)
uv run --frozen python run.py adk  "Is the VPN down?"   # the ADK agent        (days 3-4)
```

`plan` needs no key and no network. The other two need a working key.

## What you do not need

No database, no Docker, no cloud project, no billing account, and no MCP server — the data
boundary arrives in P02. All data in this project is synthetic and lives in
`ask_desk/data/notes.json`.
