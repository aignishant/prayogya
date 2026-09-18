---
day: 0
phase: 0
phase_name: "Setup"
title: "The machine and the repository — uv, the Python pin, git, the secrets rule"
ids: []
kind: setup
plan_version: "v1.0.0"
parts: 7
generated: "2026-09-18"
status: written
commit: ""
---

> **Yesterday:** nothing — the plan was adopted (ADR-0001), the ledgers were scaffolded, and no
> day exists yet.
> **Today:** pin the Python, let `uv` own the environment, learn to write in git, and prove that a
> planted secret cannot be committed.
> **Tomorrow:** day 1 adds `ruff`, `mypy` and `pytest` and makes `python granth.py check` green
> on an empty package.

## §1 Where we are

You are moving into a rented house. Before you unpack a single box, four things happen at the
handover. You and the owner sign a sheet saying what the house contains, model numbers and all,
so that when something breaks you are not arguing about what it was. You buy what the house
still needs and keep the receipts, because the receipts — not the shopping list — are what let
you set up a second house exactly like this one. You start a notebook where every change to the
house is written down, dated, and never crossed out. And you put a drawer in the hallway for the
keys, with one rule: keys go in the drawer, never on the table.

That is day 0. The house is this repository. The signed sheet is the Python pin. The receipts are
`uv.lock`. The notebook is git. The drawer is `.env`, and the front door that will not lock while
a window is open is the pre-commit hook that refuses a commit carrying a key.

This day closes no concept IDs. The plan's §8 assigns it none, and ADR-0001 records why: a setup
day that claimed IDs would make every later count wrong. What it produces instead is the ground
the other 136 days stand on.

## §2 The map

### 1 · The machine

The interpreter, the tool that owns it, and the habit of writing down what you actually have.
These three parts share one mental model: *a version is an observation with a date, not a wish*.

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-machine/1.1-the-python-pin.md) | The Python pin — why "the same machine" has to be written down | Which Python runs this project, and how do two machines agree on it? | foundation |
| [1.2](parts/01-machine/1.2-uv-project-and-lockfile.md) | uv — the project file, the lockfile, and the environment | What are `pyproject.toml`, `uv.lock` and `.venv/`, and which get committed? | working |
| [1.3](parts/01-machine/1.3-recording-what-you-have.md) | Recording what you actually have — the pin ledger | The machine's `uv` disagrees with the plan's pin. What do you write down, and where? | working |

### 2 · The repository

git as the project's memory, and the one moment where a rule can be enforced before it enters
that memory. Both parts share the model: *history is append-only, so guard the door, not the
archive*.

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-repository/2.1-git-as-memory.md) | git as the memory — init, identity, one day one commit | What is a commit, why one per day, and what does git refuse? | foundation |
| [2.2](parts/02-repository/2.2-the-pre-commit-hook.md) | The pre-commit hook — a check that runs before anything lands | How does a script refuse a commit, and why does it live in `.githooks/`? | working |

### 3 · The secrets rule

Where a key may live, and the proof that the rule is enforced rather than hoped for. The model:
*one drawer, one card, and a door you have watched refuse*.

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-secrets/3.1-the-secrets-rule.md) | The secrets rule — `.env`, `.gitignore`, and the one file that is allowed through | Where do keys live, what hides them, and why is `.env.example` committed? | working |
| [3.2](parts/03-secrets/3.2-planting-a-secret.md) | Plant a secret and watch the commit refused — then find the hole | Does the guard actually work, how is it bypassed, and why is a deleted secret still there? | production · **failure** |

This day has no `sources/`. Every subtopic is a tool or a repository convention; there is no
primary document to read after the parts, and none is manufactured.

## §3 Setup

Run at the repository root — the folder that holds `granth.py` — in PowerShell. Each command is
explained in the part that owns it.

```powershell
# 1.1 / 1.2 — the machine
uv --version
uv init --vcs none --name prahari .
uv python pin 3.12
uv sync
uv run python -c "import sys; print(sys.version); print(sys.executable)"

# 2.1 — who is writing
git config user.name
git config user.email

# 2.2 — the hook (write .githooks/pre-commit first; see §4)
git config core.hooksPath .githooks
git update-index --chmod=+x .githooks/pre-commit

# 3.1 — the drawer
Copy-Item .env.example .env
git check-ignore -v .env .env.example
```

If `uv sync` warns about hardlinks, set `$env:UV_LINK_MODE = "copy"` and run it again (part 1.2,
*When it breaks*).

## §4 Build brief

| File | What it must do |
| --- | --- |
| `pyproject.toml`, `.python-version`, `uv.lock`, `src/prahari/__init__.py` | `TODO(me)`: created by `uv init` and `uv sync` as in §3. Open each. Delete or keep the `authors` line `uv init` copied from your git identity. Confirm `requires-python` is `>=3.12` and `.python-version` is `3.12`. |
| `.githooks/pre-commit` | `TODO(me)`: create the file with the script from part 2.2's mechanism, wire it with the two commands in §3, and confirm `git ls-files -s .githooks/pre-commit` reports mode `100755`. |
| `.githooks/pre-commit` — extend | `TODO(me)`: the hook refuses `.env` files and key-shaped assignments. Add a third check that refuses any staged file ending in `.pem` or `.key`, mirroring the `.gitignore` patterns, and plant one to prove it. |
| `.env` | `TODO(me)`: copy from `.env.example`, fill in whichever keys you already hold, leave the rest empty. Confirm `git status --short` never lists it. |
| `docs/PINS.md` | `TODO(me)`: append the three rows from §11 — after running the three commands in part 1.3 yourself and checking the values match what you see. If your machine's `uv` prints a different version, the row records **yours**. |
| `docs/GLOSSARY.md` | `TODO(me)`: append the rows from §11. Before pasting, search the file for each term; today it is empty, so every term is new. |

## §5 The check that must be able to fail

The day's check is the phase 0 gate's second half: **a planted secret cannot be committed.**

```powershell
"GROQ_API_KEY=planted-secret-value-do-not-commit" | Set-Content -Encoding utf8 .env
git add -f .env
git commit -m "oops"
git reset HEAD .env
```

GREEN is `git commit` exiting `1` with `pre-commit: refusing '.env' — a secrets file never enters
git.` and no new line in `git log`. RED is the commit landing.

To make it go red on purpose: `git config --unset core.hooksPath`, run the four lines again, and
watch the commit land silently. Then `git reset --hard HEAD~1`, re-create `.env` from
`.env.example`, and `git config core.hooksPath .githooks`. Part 3.2 walks this in full, including
the second bypass and reading the "deleted" secret back out of history.

The documents themselves are checked by `python granth.py depth 0`, which must be green, and
`python granth.py index --check`, which must report every generated document current.

## §6 Budget

**0 model requests**, on every provider. Nothing today calls a model. The `.env` you create may
hold real keys; nothing reads them until day 24.

## §7 Traps

- **`python granth.py check` is red today, and that is correct.** The gate runs
  `uv run ruff check .` first, and `ruff` is not installed until day 1, so it fails with
  `error: Failed to spawn: ruff / Caused by: program not found`. Day 1's title is the fix. Do not
  install `ruff` today to make it green — that is day 1's subject and would leave day 1 with
  nothing to build. Because `python granth.py done 0` runs the same gate, **day 0 is committed by
  hand** with the message in §11; from day 1 onward `done N` does it.
- **`core.hooksPath` is per clone.** It is one line in `.git/config`, which is not committed.
  A fresh clone has the hook in its tree and does not run it. §3 has the command; put it in every
  clone before the first commit.
- **The executable bit is not recorded on Windows.** Without `git update-index --chmod=+x`, git
  stores the hook as `100644` and a clone on macOS or Linux ignores it silently.
- **A placeholder value in `.env.example` is a value.** `GROQ_API_KEY=your-key-here` is refused
  by the hook's second check, and rightly. Leave the value empty; put the instruction in the
  comment.
- **`.gitignore` does not affect a file already tracked.** If `.env` was ever committed, ignoring
  it afterwards does nothing; `git rm --cached .env` is the fix, and the history still holds it.
- **`--no-verify` skips the hook by design.** It is not a bug to be closed; it is the reason the
  same check runs again in CI on day 110.
- **A cloud-synced folder and `.venv/`.** This repository lives in one. The environment is
  thousands of small files; exclude `.venv/` from syncing rather than fighting the client.
- **The hook's known gaps** — the path loop breaks on a filename with a space, and the pattern
  misses lowercase names like `api_key`. Named here so the next reader knows they were seen, not
  missed.
- **`git reset --hard` deletes tracked files from disk.** After the `landed` commit in part 3.2,
  the reset removes `.env`; re-create it from `.env.example`.

## §8 Verify before you build

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| `uv init` default files and flags | https://docs.astral.sh/uv/concepts/projects/init/ | 2026-09-18 | Default `init` creates `.python-version`, `README.md`, `pyproject.toml`, `src/<name>/__init__.py`; `--bare`, `--lib`, `--package`, `--app` semantics |
| `uv python pin`, `.python-version`, automatic downloads | https://docs.astral.sh/uv/concepts/python-versions/ | 2026-09-18 | `pin` writes `.python-version`, searched in cwd and parents; `requires-python` interaction; uv downloads managed builds by default |
| `uv lock`, `uv sync`, `uv run` | https://docs.astral.sh/uv/concepts/projects/sync/ | 2026-09-18 | `uv run` locks and syncs before running; `sync` is exact by default |
| `uv.lock` and `.venv/` in version control | https://docs.astral.sh/uv/concepts/projects/layout/ | 2026-09-18 | Lockfile *"should be checked into version control"*, is managed by uv and not hand-edited; `.venv` is not committed and carries its own `.gitignore` |
| `uv sync --locked`, `--link-mode`, `UV_LINK_MODE` | https://docs.astral.sh/uv/reference/cli/ | 2026-09-18 | `--locked` errors if the lockfile is stale; link mode defaults to `hardlink` on Windows; options `clone`, `copy`, `hardlink`, `symlink`; `uv self update` exists; `--vcs git|none` |
| Newest published `uv` | https://pypi.org/pypi/uv/json | 2026-09-18 | `0.12.16` — the plan's pin. The machine has `0.12.3`; both recorded in §11 |
| pre-commit hook contract, hooks directory, executable bit | https://git-scm.com/docs/githooks | 2026-09-18 | Runs before the commit message is obtained; non-zero aborts; `--no-verify` bypasses; hooks dir is `$GIT_DIR/hooks` or `core.hooksPath`; non-executable hooks are ignored |
| `.gitignore` negation, trailing `/`, tracked files unaffected | https://git-scm.com/docs/gitignore | 2026-09-18 | `!` re-includes unless a parent directory is excluded; already-tracked files are not affected; `git rm --cached` to stop tracking |
| Installed tool versions | `uv --version`, `uv python list 3.12 --only-installed`, `git --version` on the development machine | 2026-09-18 | `uv 0.12.3`; CPython `3.12.13` (managed), `3.12.12` (managed), `3.12.10` (installer); `git 2.54.0.windows.1` |

Every error message pasted in the parts was produced on the development machine on 2026-09-18,
in a throwaway repository, and copied verbatim. None is reconstructed.

## §9 Say it out loud

Today I set up the machine so that nothing about it has to be remembered. The Python version is
pinned in a committed file, so every command runs on 3.12 whatever my shell would have found.
`uv` owns the environment: `pyproject.toml` says what I want, `uv.lock` says exactly what I got
and is committed, `.venv/` is where it lives and is not. I wrote down the versions I actually
observed, including the one that disagrees with the plan, in an append-only ledger. I learned
what a commit is and why this project makes one per day. And I wrote a pre-commit hook that
refuses a commit carrying a key — then planted a fake one and watched it refuse, then bypassed
it two ways and read the "deleted" key straight back out of history. So I know the hook is a
seatbelt, not a vault: it stops the accident, and a leaked key is handled by rotating it, never by
deleting the file.

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Defined by understanding and green checks, never by effort
spent.

## §11 Ledger & commit

**`docs/PROGRESS.md`:**

```text
| 0 | 2026-09-18 | — | 7 | <hash> | depth: yes · secret refused: yes · toolchain gate: day 1 |
```

**`docs/PINS.md`** — the observations from part 1.3. If your machine prints different values,
record yours:

```text
| `uv` (installed) | 0.12.3 (`uv 0.12.3 (507230998 2026-08-07 x86_64-pc-windows-msvc)`) | 2026-09-18 | 0 | `uv --version` on the development machine. Does not supersede the plan's `0.12.16` row: that row read the package index, this one read the machine. Upgrading is a decision, not a correction; the `[build-system]` line `uv init` wrote pins `uv_build>=0.12.3,<0.13.0` to this value. |
| CPython (managed by `uv`) | 3.12.13 | 2026-09-18 | 0 | `uv python list 3.12 --only-installed`; the build `uv run` selects under the `3.12` pin. Newer than the plan's `3.12.10 observed`, which is the installer build under `Programs\Python\Python312`; both are present. |
| `git` | 2.54.0.windows.1 | 2026-09-18 | 0 | `git --version`. Not in the plan's §5; added because the pre-commit hook and `core.hooksPath` depend on it. |
```

**`docs/GLOSSARY.md`** — one row per term this day defined for the first time:

```text
| interpreter | The program that reads `.py` files and runs them; Python has many versions of it, and which one runs is decided by the pin. | day 0 part 1.1 | Python runtime |
| version pin | A version written into a committed file so every machine uses the same one; here `.python-version` holding `3.12`. | day 0 part 1.1 | pin |
| pyproject.toml | The project file: name, `requires-python`, and the libraries the project wants with loose version rules. Edited on purpose. | day 0 part 1.2 | project file |
| lockfile | `uv.lock`: the exact resolved version of every library, the whole tree, written by the tool and committed. | day 0 part 1.2 | uv.lock |
| virtual environment | `.venv/`: a private copy of the interpreter and installed libraries for one project, never committed, rebuilt from the lockfile. | day 0 part 1.2 | venv |
| pin ledger | `docs/PINS.md`: every version observed, with date, day and how it was read. Append-only; a disagreement gets a new row, never an edit. | day 0 part 1.3 | — |
| repository | A folder git watches, with its history in the hidden `.git/` directory. | day 0 part 2.1 | repo |
| working tree | The files as you see and edit them on disk. | day 0 part 2.1 | — |
| staging area | The holding place for changes chosen for the next commit; `git add` moves changes into it. | day 0 part 2.1 | index |
| commit | A snapshot of the staging area with author, date and message, chained to the one before it and named by a fingerprint of its content, so it cannot be silently changed. | day 0 part 2.1 | — |
| hook | A script git runs at a fixed moment, such as just before a commit. | day 0 part 2.2 | git hook |
| pre-commit hook | The hook that runs before a commit is written; a non-zero exit aborts the commit. Lives in `.githooks/`, wired by `core.hooksPath`. | day 0 part 2.2 | — |
| secret | Any string that grants access — an API key, a password, a token. | day 0 part 3.1 | credential |
| .env | The one gitignored file at the root where every secret lives, one `NAME=value` per line. | day 0 part 3.1 | dotenv file |
| .env.example | The committed twin of `.env`: same names, empty values, a comment per variable. | day 0 part 3.1 | — |
| gitignore | The `.gitignore` file listing patterns git treats as absent; a `!` prefix re-includes a file an earlier pattern excluded. | day 0 part 3.1 | ignore file |
| deliberate failure | Making a check go red on purpose and reading what it says, so that the check is trusted because it was seen to work. | day 0 part 3.2 | — |
| rotation | Issuing a new secret and revoking the old one at the provider; the response to a leak, before any file is deleted. | day 0 part 3.2 | key rotation |
```

**Commit** — by hand today (see §7), staged with `git add -A` after `git status --short` has been
read:

```text
day 00: The machine and the repository — uv, the Python pin, git, the secrets rule
```
