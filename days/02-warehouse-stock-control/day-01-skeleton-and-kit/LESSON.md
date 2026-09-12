---
project: "P02"
day: 1
title: "The skeleton and the kit"
spine: 1
kind: setup
deploy_tier: D3
plan_version: "v4.1.0"
parts: 9
files_printed: [pyproject.toml, stock_desk/__init__.py, stock_desk/util/__init__.py, run, stock_desk/util/keys.py, stock_desk/util/logging.py, stock_desk/util/backoff.py, stock_desk/util/budget.py, stock_desk/models.py, tests/test_kit.py]
generated: "2026-09-12"
status: written
commit: ""
---

> **Yesterday:** a machine that can prove what it runs, a record of the world on the day the
> project began, a history that starts with the brief, a rule written before the secret, and a
> check with five questions.
> **Today:** the folder becomes a project — one file that declares every version, a package every
> import starts with, one door with every command behind it — and the kit the rest of the desk is
> built with: the key read once, one log line per record with secrets replaced by whole-word match,
> a retry that waits what it was told and then escalates, a ceiling that refuses, and a registry
> that refuses an alias. Then the gate, and four ways to watch it go red.
> **Tomorrow:** the domain — bins, part numbers, counts and variances, all invented — and the
> ledger's read and write contract, before anything is allowed to read it from across a process
> line.

## §1 The scene

Every counter on the night shift is handed the same kit at the goods-in desk: a scanner, a roll of
labels, a pad of count sheets and a radio. Not their own scanner from home, not whichever one was
left charging — the standard issue, numbered, signed out. The reason is not thrift. It is that when
two counters report different quantities for the same bin, the warehouse needs the difference to be
about the bin. If one scanner rounds inner packs and the other does not, the ledger fills with
disagreements that are about the equipment, and nobody can tell those from the ones that are about
the stock.

Software has that kit, and it is a file that declares every version this desk installs, a package
that every import starts with, and one script that is the door to every command. And it has the four
tools that go in every counter's bag whatever the shelf: a way to hold the key without ever showing
it, a way to write one line per event that a person can still read in six months and that never
carries a secret, a way to try again that waits what it was told to wait and then gives up honestly,
and a ceiling on how much a model may be asked before the desk stops and says so. None of the four
knows what a bin is. That is what makes them the kit and not the work.

Then the last item in the bag: the registry, which names the two models this desk may ever call and
refuses everything else by name — an alias that changes under you, the framework's own legacy
default, an ID nobody wrote down. And the gate: seventeen tests that hold the four promises, and the
day's first run of it was red on its own test file, which is the right way for a gate to introduce
itself.

## §2 The map

Three sections. **Section 1 is the skeleton** — the frame around the work: what declares the
versions, what declares the name, what declares the commands. **Section 2 is the kit** — four
modules, four promises, no opinions about stock. **Section 3 is the registry and the gate** — the
two things that make the rest trustworthy: which model, enforced; and a check that has been watched
going red.

### 1 · The skeleton — the frame around the work

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-skeleton/1.1-one-project-declared-once.md) | One project, declared once | What decides which versions this desk runs, and where is that written? | foundation |
| [1.2](parts/01-the-skeleton/1.2-package-every-import-starts-with.md) | The package, and the name every import starts with | Why a package rather than a folder of scripts? | foundation |
| [1.3](parts/01-the-skeleton/1.3-one-door-into-the-desk.md) | One door into the desk | How does anybody find out what this project can do, and what it cannot do yet? | working |

### 2 · The kit — four promises, four modules

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-kit/2.1-key-read-once.md) | The key, read once | How does a secret reach the desk without reaching a log? | working |
| [2.2](parts/02-the-kit/2.2-one-line-one-record.md) | One line, one record | How do you write a log a person can still use in six months — and that hides nothing it should not? | working |
| [2.3](parts/02-the-kit/2.3-wait-what-you-were-told-to-wait.md) | Wait what you were told to wait | What does a retry do when the ledger says how long to wait — and when it runs out of attempts? | working |
| [2.4](parts/02-the-kit/2.4-ceiling-that-refuses.md) | The ceiling that refuses | What stops four agents spending an unbounded number of model calls on one count? | production |

### 3 · The registry and the gate — what makes the rest trustworthy

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-the-registry/3.1-registry-that-refuses-an-alias.md) | The registry that refuses an alias | Which model explains a variance, and how is that enforced rather than promised? | production |
| [3.2](parts/03-the-registry/3.2-gate-that-goes-red.md) | The gate that goes red · **failure** | How do you know the tests test anything? | production |

## §3 Setup — run this

The folder from day 0, with the pinned interpreter and the ignore rule already in it. Everything
below is run from the project root.

```bash
mkdir -p stock_desk/util tests

uv sync
uv run ruff --version
uv run pytest --version
```

Write `pyproject.toml` first — `uv sync` reads it, and reading nothing is how you get an empty
environment and a confusing error. Expect `ruff 0.16.7` and `pytest 9.1.1`, and `Installed 7
packages`. On this machine `uv sync` printed a three-line warning that it had *fallen back to a
full copy* because the folder's filesystem refused hardlinks; that is a warning and not an error,
and part 1.1 carries it. If yours fails outright with `os error 396`, the folder is cloud-synced;
re-run as `uv sync --link-mode=copy`.

Once `run` exists, mark it executable in git so a clone on another operating system can use it:

```bash
git update-index --chmod=+x run
git ls-files -s run
```

Expect `100755`.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `pyproject.toml` | part 1.1 |
| `stock_desk/__init__.py` | part 1.2 |
| `stock_desk/util/__init__.py` | part 1.2 |
| `run` | part 1.3 |
| `stock_desk/util/keys.py` | part 2.1 |
| `stock_desk/util/logging.py` | part 2.2 |
| `stock_desk/util/backoff.py` | part 2.3 |
| `stock_desk/util/budget.py` | part 2.4 |
| `stock_desk/models.py` | part 3.1 |
| `tests/test_kit.py` | part 3.2 |

One earlier file changes: `PACKAGES.md` (day 0 part 1.1) gains two rows in part 1.1, for the two
packages this day installs.

## §5 Build brief

`pyproject.toml`, then `uv sync`, then the two `__init__.py` files and `run`, then the four kit
modules in the order the parts print them, then the registry, then the tests. Run `./run check`
after the tests and before the reps — it should be green, and if it is red on a line length, that
is what happened here too. Then the reps:

| File | What it must do |
| --- | --- |
| `stock_desk/util/logging.py` | `TODO(me)`: `SECRET_WORDS` is six words. Name two field names a stock desk will log that contain a secret and that this list misses, and decide whether to add words or to add a second mechanism. |
| `stock_desk/util/backoff.py` | `TODO(me)`: `retry` is synchronous. The desk from day 8 is `async`. Write the `async` twin beside it, with the same schedule and the same tests, or say why one function cannot serve both. |
| `stock_desk/util/budget.py` | `TODO(me)`: `Budget` counts calls. Add a second ceiling on *characters sent*, decide whether it is the same class or a second one, and say what a test for it asserts. |
| `stock_desk/models.py` | `TODO(me)`: the framework's default model when nothing is pinned. Confirm the ID on the day the framework is installed, by reading the installed source, and record the file and line in `PACKAGES.md`. |
| `run` | `TODO(me)`: `./run check` runs lint, tests and setup and stops at the first failure. Decide whether it should run all three and report every failure, and what that changes about the exit status. |

## §6 The check that must be able to fail

```bash
./run check
```

Green is `All checks passed!`, `17 passed`, day 0's five `ok` lines, and `OK check`.

Ways to make it red, every one of them run today:

1. **A line over a hundred characters** in any file. `E501 Line too long (101 > 100)` — the day's
   own first run, on its own test file.
2. **Match secret words by substring** in `looks_secret`. Three tests red on `keys`, `monkey` and
   `keyword`, and the demo line says `"keys": "<redacted>"`.
3. **Ignore `retry_after`** in `retry`. `assert [1.0, 2.0] == [7.5, 7.5]`.
4. **Return the name unconditionally** from `pinned`. `Failed: DID NOT RAISE UnpinnedModel`.
5. **Delete the last line of `budget.py`** — the return in `remaining` — which is what a careless
   one-line edit of the file's tail does. Part 3.2 has what the suite says.

And the one that is green while being different: disable only the `-latest` line in `pinned`, and
the alias is *still* refused — by the registry line, with a different message. Two lines of defence,
and part 3.1 says why the first one is kept anyway.

## §7 Request budget

**Zero.** No model is called today. The registry names two model IDs and calls neither; the budget
counts calls that nothing makes yet; the retry retries a function that raises on purpose. The first
model call in this project is day 8's, and it will go through every one of these four modules.

What today fixes is the *unit* of the budget: one count of one bin, across every agent that works
on it. Four agents is at least four calls, and part 2.4 is the ceiling that says so before any of
them exist.

## §8 Traps

- **A floor is not a pin.** `>=` says what is too old; `==` says what runs. `uv.lock` records what
  was resolved, and `--locked` refuses when the two disagree.
- **`uv sync` reads `pyproject.toml`.** Write the file first, or you get an empty environment and
  an error about something else.
- **The hardlink warning is a warning.** `Failed to hardlink files; falling back to full copy` is
  the tool coping with a filesystem; `os error 396` is the tool refusing one. Only the second needs
  `--link-mode=copy`.
- **`pythonpath = ["."]` is for pytest, not for you.** `uv run` from the project root puts the
  package on the path; from anywhere else, `import stock_desk` fails.
- **`run` needs the executable bit in git, not only on disk.** `git update-index --chmod=+x run`,
  then `git ls-files -s run` says `100755`.
- **A program the machine lacks is a `FileNotFoundError` from `subprocess`**, naming a file inside
  Python. The driver catches it and names the program.
- **Match secret words as words.** `api_key` is a secret; `keys` is a list of field names.
  Substring matching blanks the second, and a blank field is a log line that has stopped speaking.
- **Log to standard error.** From day 3 the boundary speaks a protocol on standard output, and a
  log line there is a corrupted message.
- **The provider's `Retry-After` beats your arithmetic.** A retry that ignores it is a retry that
  hammers a service that just asked you not to.
- **A budget raises.** A ceiling that clamps to zero and carries on is a desk that finishes a count
  it could not afford, with whatever answer it had.
- **Refuse the legacy ID by name.** It is what an unpinned agent ends up on, and it is a real
  model, so nothing else would notice.
- **An alias is refused twice.** By the `-latest` rule and by the registry. Keep both; the first
  gives the better message.
- **The first red check of a day is usually the day's own file.** Read the line it names before
  assuming the tool is wrong.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| The linter's latest release | `https://pypi.org/pypi/ruff/json` | 2026-09-12 | `0.16.7`, pinned as such. |
| The test runner's latest release | `https://pypi.org/pypi/pytest/json` | 2026-09-12 | `9.1.1`, `requires_python >=3.10`, pinned as such. |
| The provider's model list | `https://ai.google.dev/gemini-api/docs/models` | 2026-09-12 | `gemini-3.8-flash` "New Stable", `gemini-3.7-flash` "Stable", `gemini-3.5-flash` "Our legacy Flash model"; `-latest` aliases are hot-swapped on every release. The registry's three IDs and its refusals come from this page. |
| The framework's release notes since the version day 0 observed | `https://github.com/google/adk-python/releases/tag/v2.9.0` | 2026-09-12 | `v2.9.0` (2026-09-10) states it works "with MCP SDK 2.x servers as well as 1.x. Installs continue to resolve 1.x by default; install 2.x deliberately to opt in", raises `SessionNotFoundError` from `InMemorySessionService` on an unknown session, and re-runs a failed node on resume. Not installed today; recorded for the days that install and use it. |
| The environment | this project, `uv sync` | 2026-09-12 | `Using CPython 3.12.13`, `Resolved 8 packages`, `Installed 7 packages` with the hardlink fallback warning; `ruff 0.16.7`, `pytest 9.1.1`. |
| The gate | this project, `./run check` | 2026-09-12 | Red on `E501` at `tests\test_kit.py:68:101` on the first run; green after the rename — `All checks passed!`, `17 passed`, five `ok` lines. |
| The four breaks | this project | 2026-09-12 | Substring redaction: three red and `"keys": "<redacted>"`. Ignored `retry_after`: `[1.0, 2.0] == [7.5, 7.5]`. Unconditional `pinned`: `DID NOT RAISE UnpinnedModel`. Alias line alone disabled: still refused, by the registry line. |
| The executable bit | this project, `git ls-files -s run` | 2026-09-12 | `100755`. |
| The four demos | this project, `uv run python -c` | 2026-09-12 | `load_env` → `['GOOGLE_API_KEY']` and a twelve-character fingerprint; a log line with `api_key` and `auth_token` redacted and `keys` intact; two `ledger.retrying` lines then the answer; four `left` lines then `refused: reconciler asked for call 5 of 4`. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 02 | 1 | 2026-09-12 | The skeleton and the kit | 9 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — new rows:

```text
| Floor | A version requirement written as `>=`: what is too old, with the choice of what actually runs left to a resolver on the day. A floor drifts; a pin does not. | P02 day 1 part 1.1 | a lower bound |
| Lockfile (project) | The exact versions a resolver chose for every package, written once by `uv lock` and read by `uv sync --locked`, which refuses to run if the project and the lock disagree. | P02 day 1 part 1.1 | `uv.lock` |
| Dependency group | A named set of packages installed for a purpose — here `dev`, for the linter and the test runner — that a running desk never imports and an image leaves out. | P02 day 1 part 1.1 | the dev group |
| Package | A folder Python treats as one importable name because it holds an `__init__.py`; the name every import in the project starts with. | P02 day 1 part 1.2 | an importable name |
| Driver | The one script that is the door to every command a project has, so that a command is found by reading one file. Runs everything through `uv run`, on the pinned interpreter. | P02 day 1 part 1.3 | `./run` |
| Planned command | A command the driver names before it exists, with the day that builds it, so `./run` is the map of the whole desk from day 1. | P02 day 1 part 1.3 | not built yet |
| Fingerprint | Twelve hex characters of a secret's hash: enough to answer "is this the same key as before?" and useless for anything else. The only form in which a secret may reach a log. | P02 day 1 part 2.1 | a key's tag |
| Whole-word redaction | Replacing a field's value when one of the *words* of its name is a secret word — `api_key`, not `keys` — so that a log never carries a secret and never blanks a field that merely contains the letters. | P02 day 1 part 2.2 | redaction by name |
| Retry-After | The interval the other side asked for before the next attempt. A provider's own instruction, which always beats the caller's schedule. | P02 day 1 part 2.3 | the provider's interval |
| Escalation | What a retry does when the attempts run out: raise, so that a person or a later step decides — never a substitute answer. | P02 day 1 part 2.3 | honest failure |
| Budget | A ceiling on model calls for one unit of work, counted across every agent that works on it, that refuses by raising and records who spent what. | P02 day 1 part 2.4 | the call ceiling |
| Registry | The one file that names every model a project may call, as exact IDs, with a function that refuses an alias, the provider's legacy default and anything not on the list. | P02 day 1 part 3.1 | the model pins |
| Gate | A check that has been watched going red, run as one command, whose exit status is the verdict. Re-anchored: here `./run check`, lint then tests then setup. | P02 day 1 part 3.2 | the check |
```

**This project's `PACKAGES.md`** — the two rows part 1.1 appends, dated.

**`docs/PINS.md`** — no row is owed. `ruff` and `pytest` are project pins.

**`docs/SOURCES.md`** — no row is owed. Nothing with a citation identifier was cited.

**Commit:**

```text
P02 day 1: The skeleton and the kit
```
