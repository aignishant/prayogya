---
project: "P00 Foundry"
day: 3
phase: P00
title: "P00 Foundry · 3 — Keys, pinning, and the check that refuses a half-finished day"
ids: [FN-03]
kind: gate
deploy_tier: "—"
plan_version: "v3.1.0"
parts: 4
files_printed:
  - "projects/00-foundry/keys.py"
  - "projects/00-foundry/.python-version"
  - "projects/00-foundry/pyproject.toml"
  - "projects/00-foundry/run.py"
generated: "2026-09-09"
status: written
commit: ""
---

> **Yesterday:** two files that decide what the project hands out, and the habit of asking git
> rather than reading the rules and reasoning about them.
> **Today:** the project's first Python — the code that reads a secret, the two files that turn a
> floor into a pin, and a driver whose exit status is the verdict.
> **Tomorrow:** P01 Ask Desk day 1, where the loop is built by hand and the first real request goes
> out.

## §1 The scene

Stand at a locksmith's counter while they cut a key. They never measure your key by eye — they read
the code stamped on its shoulder, because the code is what the key *is* and the brass is only one
copy of it. They write that code in the book and never on the tag hanging off the ring, since a tag
with the code on it turns a lost keyring into a lost house. That split is yesterday's two files,
carried forward: the values in one place that never leaves, the names in another that anyone may
read.

Inside the lock there is a row of brass pins, each cut to an exact height, and the trade's word for
setting those heights is **pinning**. A pin stack that would accept anything from three millimetres
upward is not a loose lock; it is not a lock. That is the second thing today is about, because your
project currently asks for "any Python from 3.12 upward" and "any platformdirs from 4.11.8 upward",
and both of those are the three-millimetre version. The ledger already disagrees with the folder
about which version is installed, and nobody was told.

And then the last thing the locksmith does, which is the whole day. They do not hold the key against
the code sheet and nod. They turn it in a lock on the bench, because that produces an answer that
does not depend on anyone's opinion. Your project gets that too — one command, one verdict — and
then you break it in the way that matters most and least visibly: you make it print the word RED and
hand back the number that means everything is fine. A gate you have never watched refuse is not a
gate.

## §2 The map

Two sections. The first is the secret — where it actually is when the program runs, and how far a
check can honestly go in judging it. The second is the two words in the title that sound like
housekeeping and are not: pinning, which decides whether two machines run the same code, and
refusing, which decides whether any of it is enforced.

### 1 · The key

*The mental model: the code in the book and the brass on the ring are two different objects, and the
shop's whole trade is knowing which one it is holding.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-key/1.1-the-code-and-the-cut.md) | The code and the cut | When the program is running, where is the value — and what wins when it is in two places? | foundation |
| [1.2](parts/01-the-key/1.2-three-states-and-the-one-you-cannot-check.md) | Three states, and the one you cannot check | A key can be wrong three ways; which of them can a check on your own machine decide? | working |

### 2 · The pin and the refusal

*The mental model: a pin is cut to an exact height or it is not a pin, and the only honest test is
turning the key rather than looking at it.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-pin-and-the-refusal/2.1-a-floor-is-not-a-pin.md) | A floor is not a pin | What does `>=` actually promise, and which files make two machines agree? | working |
| [2.2](parts/02-the-pin-and-the-refusal/2.2-the-check-that-could-not-refuse.md) | The check that could not refuse | How does a check report its verdict, and what does one look like that cannot? | production |

## §3 Setup — run this

Nothing new to install: the toolchain has not moved since day 1, and today's code is standard
library plus the `uv` that is already here. Everything below was run on this machine today and what
it reported is in §9. Run them in order from the repository root.

```bash
cd projects/00-foundry

# part 1.1 writes keys.py; part 1.2 only exercises it
uv run --frozen python -c "import keys; print(keys.get('GOOGLE_API_KEY'))"

# part 2.1 writes .python-version and edits pyproject.toml
uv python pin 3.12.12
uv add "platformdirs==4.11.8"
uv lock --check

# part 2.2 writes run.py — the first check this project has had
uv run --frozen python run.py check
echo $?
```

`--frozen` is on every `uv run` in this day on purpose, and part 2.2 is where that stops looking
like a detail. The `.env` you are reading holds the synthetic value day 2 put there; no real
credential is needed today, and the first one arrives in P01.

## §4 Files this day prints

Four files, all of them the project's own, and two of them the first Python this project has
carried. Nothing here reprints anything from days 1 or 2: `.gitignore` and `.env.example` were
printed whole by day 2 and are untouched today, and `pyproject.toml` appears only as a marked
two-line diff against the version day 1 printed.

| File | Printed by |
| --- | --- |
| `projects/00-foundry/keys.py` | part 1.1, whole |
| `projects/00-foundry/.python-version` | part 2.1, whole — it is one line |
| `projects/00-foundry/pyproject.toml` | part 2.1, as a marked diff against day 1's version |
| `projects/00-foundry/run.py` | part 2.2, whole |

## §5 Build brief

| File | What it must do |
| --- | --- |
| `projects/00-foundry/keys.py` | `TODO(me)`: type it. Before running anything, say which of `os.environ` and `.env` you expect `get` to return for `GOOGLE_API_KEY`, and why. Then run it with `GOOGLE_API_KEY=x` in front of the command and say whether your answer changed. |
| `projects/00-foundry/keys.py` (the three states) | `TODO(me)`: drive `require` through absent, empty and present without editing the project's real `.env`. Say which two it refuses, which one it returns, and what would have to exist for it to judge the third. |
| `projects/00-foundry/.python-version` | `TODO(me)`: before running `uv python pin`, predict the exact string that will land in the file. Then say why `requires-python = ">=3.12"` stays in `pyproject.toml` rather than being replaced by it. |
| `projects/00-foundry/pyproject.toml` | `TODO(me)`: change the floor to a pin with `uv add`. Then open `docs/PINS.md`, find the platformdirs row day 1 wrote, and say what the difference between that row and the installed version tells you about `>=`. |
| `projects/00-foundry/run.py` | `TODO(me)`: type it. Predict which of the four checks will be red on your machine *before* the first run, then run it and see whether you were right. |
| the failure rep | `TODO(me)`: remove `sys.exit(` from the `__main__` block, empty the key, and run the check followed by `echo $?`. Then break the lock agreement and run the check once through plain `uv run` and once through `uv run --frozen`, checking `uv.lock` after each. |

## §6 The check that must be able to fail

```text
cd projects/00-foundry
uv run --frozen python run.py check    # the project's own gate
echo $?                                # 0 green, 1 red, 2 you typed it wrong
uv lock --check                        # the lockfile still answers pyproject
cd ../.. && python p.py depth 3        # this day against the plan §5 contract
```

**How to make it go red on purpose — four ways, and the third is the day's real one.**

The first is a key. Empty the value in `.env` and `keys` goes red with a message that says *present
with an empty value*, which is a different sentence from *not set* and points at a different fix.

The second is a pin. Change `platformdirs==4.11.8` back to `>=4.11.8` and `pins` goes red; change a
version without re-locking and `lock` goes red with uv's own error quoted back at you.

The third is the day's deliberate failure and it is part 2.2. Remove `sys.exit(` and its closing
bracket from the `__main__` block, then empty the key so the check has something to refuse. It
prints `RED`, it prints `1 problem(s)`, and it exits **`0`**. Every hook, pipeline and `done` command
downstream reads that as a pass. The screen is more convincing than usual and the only witness that
disagrees is `echo $?`.

The fourth is the ordering version of the same idea, and it needs no code change: make
`pyproject.toml` and `uv.lock` disagree, then run the check through plain `uv run` rather than
`uv run --frozen`. `uv` brings the lock up to date before your program starts, so the drift is
repaired before the check looks at it, and the check reports green — accurately, about a state its
own invocation created.

For the document itself: delete a `## In production` heading from any part and run
`python p.py depth 3`; it names the file and the missing section.

## §7 Request budget

**Zero model calls, with one deliberate exception, and the exception is the subject.**

P00 Foundry has no provider, no tier, no tools, no MCP boundary and no cast — the plan §11 gives it
none of those, because its subject is the machine. Every command in this day runs locally and
contacts nothing.

The exception is a **single** unauthenticated request in part 1.2, to
`https://generativelanguage.googleapis.com/v1beta/models`, made with the synthetic key day 2 wrote.
It is not a model call: it consumes no tokens, it is rejected before any model is reached, and its
entire purpose is to show that the third state of a key can only ever be settled by asking. One
request, no quota consumed, and it is the last thing this project sends anywhere.

From P01 onward the number is never zero, and the plan §9 counts requests **across the whole cast**:
a three-agent turn is at least three requests, and a writer-critic loop is unbounded until you bound
it. Stating the zero rather than omitting it is the habit that makes the non-zero number credible
later.

## §8 Traps

- **Nothing reads `.env` for you.** Not Python, not `uv run`, not the shell. The file is a convention
  among tools, and until this project contained code that opens it, it was decoration.
- **`Path(".env")` resolves against the working directory, not the file.** The same program then
  finds the file from inside the project folder and silently finds nothing from the repository root.
  `Path(__file__).with_name(".env")` is the version that does not care where you were standing.
- **A default argument is evaluated once, at `def` time.** `path: Path = ENV_FILE` freezes the
  module-level value into the function object, and reassigning `keys.ENV_FILE` afterwards changes
  nothing. This one was found by the transcript in part 1.2 printing three identical rows.
- **`split("=")` breaks on values containing `=`.** Base64 padding ends in `=` constantly. Use
  `partition`, which splits on the first occurrence only and always returns three parts.
- **`if not os.environ.get(NAME)` cannot tell absent from empty.** Both are falsy, so the error
  message has to cover both, and it ends up telling somebody a key is not set while they are looking
  at the line that sets it.
- **No local check can decide whether a credential is valid.** Only the provider holds the other
  half. A placeholder heuristic is a warning; making it a failure produces a check that goes red on
  good keys containing the wrong letters, and people stop reading it.
- **A rejected key is `400 INVALID_ARGUMENT`, not `401`.** Code branching on `401` to mean "bad
  credentials" misses it entirely and retries a request that can never succeed.
- **`>=` is a floor and floors are for libraries.** Applications pin. The tell is not whether there
  is a version number in the file; it is whether handing the folder to someone next March gets them
  what you have.
- **`requires-python` pins nothing.** It says what is too old. `.python-version` is the file that
  names the interpreter, and without it CI takes whatever its image happens to ship.
- **`uv run` updates the lockfile before running your command.** A check invoked that way inspects a
  repository the invocation just repaired. `--frozen` is what stops it.
- **`uv sync` inside `uv run` fails on Windows.** The interpreter holds its own files open and you
  get `Access is denied. (os error 5)`. A check must ask questions that write nothing —
  `uv lock --check`, not `uv sync --locked`.
- **A function that returns its verdict is not a function that reports it.** `sys.exit(main(...))`
  is the whole difference between a gate and a decoration, and the broken version prints *more*
  convincing output than the working one.
- **Exit `1` and exit `2` are different answers.** One means the checks ran and failed; the other
  means they never ran. A pipeline that conflates them reports a typo as a code failure.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| Nothing populates the environment from `.env` | `uv run --frozen python -c "import os; print(os.environ.get('GOOGLE_API_KEY'))"` | 2026-09-09 | `None`, with the file present and correct since day 2 — part 1.1 |
| The process environment wins over the file | the same command with `GOOGLE_API_KEY=from-the-shell` prefixed | 2026-09-09 | file returned `fake-not-a-real-key-000`, `keys.get` returned `from-the-shell` |
| The default-argument bug is real | the first draft of part 1.2's probe, with `path: Path = ENV_FILE` | 2026-09-09 | three identical `present` rows instead of absent / empty / present; fixed with a `None` sentinel |
| `require` separates absent from empty | the three-state probe against `.env.probe` | 2026-09-09 | two different `MissingKey` messages, then a returned value on the third |
| A wrapping quote survives an unstripped parser | `.strip('"')` removed, `GOOGLE_API_KEY="..."` in the file | 2026-09-09 | `'"fake-not-a-real-key-000"'` returned with the quotation marks attached |
| `if not os.environ.get(...)` misreports an empty value | `GOOGLE_API_KEY= uv run --frozen python -c ...` | 2026-09-09 | printed `GOOGLE_API_KEY is not set` with the variable set — exit `1` |
| A rejected key is 400, not 401 | `GET https://generativelanguage.googleapis.com/v1beta/models` with the synthetic key, `x-goog-api-key` header | 2026-09-09 | `HTTP 400`, `"API key not valid. Please pass a valid API key."`, `"status": "INVALID_ARGUMENT"` |
| Two floors resolved to two exact values | `grep` on `pyproject.toml`, then `importlib.metadata.version` | 2026-09-09 | asked `>=3.12` and `>=4.11.8`; got 3.12.12 and 4.11.8, neither named in the file |
| The ledger already disagreed with the folder | `docs/PINS.md` day-1 row against the installed version | 2026-09-09 | ledger says platformdirs 4.11.7; the project holds 4.11.8, unedited and unannounced |
| platformdirs release cadence | `https://pypi.org/pypi/platformdirs/json` | 2026-09-09 | 4.11.4 on 2026-08-24, 4.11.5 on 08-27, 4.11.6 and 4.11.7 on 09-01, 4.11.8 on 09-08 at 22:20 UTC — five releases in fifteen days |
| `uv python pin` writes the file | `uv python pin 3.12.12` | 2026-09-09 | `Pinned `.python-version` to `3.12.12``; the file is that one line |
| `uv add` edits both files in one action | `uv add "platformdirs==4.11.8"` | 2026-09-09 | `Resolved 2 packages`, `Checked 1 package`; `pyproject.toml` now `==`, lock unchanged |
| `uv lock --check` refuses a stale lock | `pyproject.toml` set to `==4.11.8` against a lock holding `4.11.7` | 2026-09-09 | exit `1`, `error: The lockfile at `uv.lock` needs to be updated, but `--check` was provided.` |
| The check reaches green from a bare state | `uv run --frozen python run.py check` after both pins | 2026-09-09 | four green, `0 problem(s)`, exit `0` — the phase gate's first half |
| A check without `sys.exit` cannot refuse | `main(sys.argv)` in place of `sys.exit(main(sys.argv))`, key emptied | 2026-09-09 | `RED`, `1 problem(s)`, **exit `0`**; restoring the one line gave identical output and exit `1` |
| `uv run` rewrites the lock before the command | `pyproject.toml` set to `>=4.11.0`, then `uv run python run.py check` | 2026-09-09 | `requires-dist` changed from `==4.11.8` to `>=4.11.0` with only the check having run; `--frozen` left the file byte-identical |
| `uv sync` inside `uv run` fails on Windows | the first draft of `check_lock_is_obeyed` | 2026-09-09 | `error: failed to remove directory ...\.venv\Lib\site-packages\platformdirs: Access is denied. (os error 5)` |
| uv, Python and git versions | `uv --version`, `python --version`, `git --version` | 2026-09-09 | uv 0.12.3, CPython 3.12.10 for the bare name, 3.12.12 inside the project, git 2.54.0.windows.1 — re-observed, not assumed |

## §10 Ledger & commit

**`docs/PROGRESS.md`:**

```text
| 3 | 2026-09-09 | FN-03 | 4 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the terms this day defined for the first time:

```text
| Process environment | The set of name-to-string pairs the operating system handed a program when it started, which Python exposes as `os.environ`. It is built by whatever launched the program and has never heard of any file. | day 3 part 1.1 | the environment block, env vars |
| Floor | A dependency or interpreter requirement written as `>=`, which states what is too old and leaves the choice to whichever machine resolves it. Correct for a library, never sufficient for an application. | day 3 part 2.1 | a lower bound, a range |
| Exit status | The single number a process hands back when it ends, and the only channel through which a check reports its verdict to another program. Zero means success; everything printed to the screen is for humans. | day 3 part 2.2 | exit code, return code, `$?` |
```

**`docs/PINS.md`** — one row, and it supersedes rather than corrects:

```text
| platformdirs | 4.11.8 | 2026-09-09 | 3 | Supersedes the 4.11.7 row day 1 wrote. Nothing was edited: `pyproject.toml` said `>=4.11.8`, 4.11.8 was published at 22:20 UTC on 2026-09-08, and the next resolution took it. Now pinned with `==` and the drift is what part 2.1 teaches. `importlib.metadata.version('platformdirs')`. |
| CPython (uv-managed) | 3.12.12 | 2026-09-09 | 3 | Re-observed, and now written down in `projects/00-foundry/.python-version` rather than left to `requires-python = ">=3.12"` to resolve. Does not supersede the day-1 row; it is the same value, now pinned in a file instead of chosen by a resolver. |
```

**`docs/SOURCES.md`** — nothing to add. This day cites the PyPI JSON API for a release history and
the Gemini endpoint for one error response; neither is a record with a resolvable identifier, and
both are dated in §9, which is what that table is for. This is the same call days 1 and 2 made.

**Commit:**

```text
day 03: P00 Foundry · 3 — Keys, pinning, and the check that refuses a half-finished day — closes FN-03
```
