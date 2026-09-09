---
project: "P00 Foundry"
day: 1
phase: P00
title: "P00 Foundry · 1 — The machine: uv, Python 3.12, and the four Pythons that ruin a Monday"
ids: [FN-01]
kind: setup
deploy_tier: "—"
plan_version: "v3.1.0"
parts: 4
files_printed:
  - "projects/00-foundry/pyproject.toml"
  - "projects/00-foundry/uv.lock"
  - "projects/00-foundry/foundry/whoami.py"
generated: "2026-09-08"
status: written
commit: ""
---

> **Yesterday:** the authoring repository — the plan, the ledgers, and a driver whose checks you
> have watched go red.
> **Today:** the first project folder, and the reason it has to own its own interpreter rather than
> borrow the machine's.
> **Tomorrow:** P00 Foundry day 2, the skeleton — and the ignore file that has to exist before the
> thing it protects.

## §1 The scene

You need a plumber. You scroll to **Plumber** in your phone, tap the first one, and reach somebody
who has never been to your house. Four numbers, one label, saved over five years. Nothing went
wrong: you asked for a label, the phone found several matches and rang the first, and it never
promised you which.

That is this whole day, and the word in the middle of it is `python`. On the machine this was
written on there are six real Python programs installed, several answering to that one word, and
the shell will start one of them without ever mentioning that there was a choice. It usually works.
It works right up until the package you installed a minute ago is not there, and by then the
evidence of which one answered has scrolled off the screen.

The fix is not tidying up the machine — you cannot tidy someone else's, and every project here has
to be finishable by someone whose machine you will never see. The fix is to stop asking by label.
Today you build the first project folder in `projects/`, and it carries the answer in two files that
travel with the code, so the requirement outlives the shell it was typed in. Then you prove it, in
the only way that counts: by running the same file two ways in the same directory and watching one
of them fail.

## §2 The map

Two sections. The first is about the machine as you found it — what is actually installed, what a
name resolves to, and what an environment turns out to be. The second is about replacing all of that
guessing with a project that states its own requirement and refuses anything that does not meet it.

### 1 · The name, and what answers it

*The mental model: `python` is a label, not a program. Something walks a list and picks.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-name/1.1-four-things-called-python.md) | Four things called python | How many are really here, and which one does the name reach? | foundation |
| [1.2](parts/01-the-name/1.2-an-environment-is-a-place.md) | An environment is a place, not a setting | What is a virtual environment made of, and how do I ask whether I am in one? | working |

### 2 · The project that answers for itself

*The mental model: a requirement written in a file can be enforced; a requirement in your head cannot.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-project/2.1-the-project-that-owns-its-interpreter.md) | The project that owns its interpreter | What do `pyproject.toml` and `uv.lock` each decide, and what does the project refuse? | working |
| [2.2](parts/02-the-project/2.2-the-two-commands-that-disagree.md) | The two commands that disagree | Why do `python x.py` and `uv run x.py` stop being the same thing? | production |

## §3 Setup — run this

Everything below was run on this machine today, and what it reported is in §9. Run them in order and
stop at the first one that surprises you — particularly if the last two agree, because on this
machine they do not.

```bash
uv --version
uv python list
where python          # `which -a python` on macOS and Linux
uv python find

mkdir -p projects/00-foundry/foundry
cd projects/00-foundry
uv init --name foundry --python 3.12 --bare
uv sync
```

## §4 Files this day prints

P00 Foundry is the first entry in `projects/`, and it is reference only — nothing later depends on
it. That is exactly why it is the right place to build a project folder slowly enough to read every
file in it.

| File | Printed by |
| --- | --- |
| `projects/00-foundry/foundry/whoami.py` | part 1.2, whole; part 2.2 adds a marked diff |
| `projects/00-foundry/pyproject.toml` | part 2.1, whole; part 2.2 adds a marked diff |
| `projects/00-foundry/uv.lock` | part 2.1, whole; part 2.2 adds a marked diff |

## §5 Build brief

| File | What it must do |
| --- | --- |
| `projects/00-foundry/foundry/whoami.py` | `TODO(me)`: type it, run it with the bare name, and say which of the interpreters in your own `uv python list` answered — before you look at the path it printed. |
| `projects/00-foundry/pyproject.toml` | `TODO(me)`: after `uv sync`, read the `Using CPython ...` line and say whether it matches what `uv python find` told you. If it does not, say why not. |
| `projects/00-foundry/uv.lock` | `TODO(me)`: find the one line in it that would catch a package that has the right version number but the wrong contents, and say what it would fail on. |
| any part of this day | `TODO(me)`: run `uv run --python 3.11 foundry/whoami.py` and read the refusal. Say which file and which key it cites, then say what it would have done instead if `requires-python` were absent. |

## §6 The check that must be able to fail

```text
python p.py depth 1                       # this day against the plan §5 contract
uv run foundry/whoami.py                  # must report in_venv True
python foundry/whoami.py                  # must fail once the dependency exists
```

**How to make it go red on purpose.** This day's check is unusual and better for it: the red is not
a broken thing, it is the *correct* behaviour of the wrong command. Once `platformdirs` is a
dependency, `python foundry/whoami.py` exits `1` with a `ModuleNotFoundError` while
`uv run foundry/whoami.py` exits `0` — same file, same directory, same moment. Part 2.2 pastes both.
If both of your commands succeed, the dependency was never added, and the day has proved nothing.

For the document itself: delete a `## In production` heading from any part and run
`python p.py depth 1`; it names the file and the missing section. Both reds were seen before this
day was called finished.

## §7 Request budget

**Zero model calls.** P00 Foundry contacts no provider, has no agent and needs no key — the plan's
§11 gives it no tier, no tools, no MCP boundary and no cast, because its subject is the machine.

Stating the zero rather than omitting it is the habit that matters, because from P01 onward the
number is never zero and every hub carries it. The plan §9 counts requests **across the whole cast**:
a three-agent turn is at least three requests, and a writer-critic loop is unbounded until you bound
it.

## §8 Traps

- **`uv python list` shows what you could have, not what you have.** Rows ending
  `<download available>` are not installed. Count only the rows ending in a path.
- **One installation can appear as four rows.** The Microsoft Store Python is listed once per name it
  answers to. Four rows at the same version are usually one interpreter, not four.
- **`where python` and `uv python find` answer different questions and may name different files.**
  On this machine they do: the installer's 3.12.10 and uv's managed 3.12.12. Neither is wrong.
- **`requires-python` is a floor, not a pin.** `>=3.12` is satisfied by 3.13. It states what the code
  needs, never what it was tested on, and the exact pin is day 3's subject.
- **`uv add` changes three files at once** — `pyproject.toml`, `uv.lock` and `.venv`. That is a
  feature: doing it as three commands is the ordinary way a lock goes stale.
- **`ModuleNotFoundError` has more than one cause.** Part 1.2 produces it by removing `pyvenv.cfg`;
  part 2.2 produces it by using the wrong command. The message is identical and names neither. Print
  `sys.executable` rather than guessing.
- **`.venv` is a build output, not source.** uv writes a `.gitignore` containing `*` inside it as it
  is created. Never copy it between machines and never edit inside it.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| uv's interpreter search order | `https://docs.astral.sh/uv/concepts/python-versions/` | 2026-09-08 | Managed installations, then `PATH`, then the Windows registry and Store — quoted in part 1.1 |
| `uv.lock` is committed and cross-platform | `https://docs.astral.sh/uv/concepts/projects/layout/` | 2026-09-08 | "should be checked into version control"; "a universal or cross-platform lockfile"; managed by uv, not hand-edited |
| What `uv run` guarantees | `https://docs.astral.sh/uv/concepts/projects/run/` | 2026-09-08 | "uv will ensure that the project environment is up-to-date before running the given command" |
| Interpreters actually installed | `uv python list` on this machine | 2026-09-08 | **Six** real interpreters: uv-managed 3.12.12, installer 3.12.10, and Store 3.11.9 under four names |
| The two commands disagree | `where python` and `uv python find` | 2026-09-08 | Different files *and* different patch versions — 3.12.10 against 3.12.12 |
| The project refuses a bad interpreter | `uv run --python 3.11 foundry/whoami.py` | 2026-09-08 | Cites `` `>=3.12` (from `project.requires-python`) `` and exits 2 |
| An unsatisfiable floor stops the sync | `uv sync` with `requires-python = ">=3.99"` | 2026-09-08 | `error: No interpreter found for Python >=3.99 in managed installations, search path, or registry` |
| `pyvenv.cfg` is what makes an environment | removing it, then re-importing | 2026-09-08 | Same executable, same directory: `ModuleNotFoundError` for an installed package |
| The dependency resolved today | `uv add platformdirs` | 2026-09-08 | `platformdirs==4.11.7`, from `https://pypi.org/simple`, with sha256 hashes in the lock |

## §10 Ledger & commit

**`docs/PROGRESS.md`:**

```text
| 1 | 2026-09-08 | FN-01 | 4 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the terms this day defined for the first time:

```text
| Search order | The list of places a machine walks to turn a name like `python` into one program on disk. First match wins, and nothing announces that there was a choice. | day 1 part 1.1 | discovery order |
| Virtual environment | A directory holding a link back to a real interpreter and its own installed packages, marked as one by a `pyvenv.cfg` beside the executable. Not a shell mode and not a variable. | day 1 part 1.2 | venv, the environment |
| Lockfile | The tool-written record of what a resolution actually produced — exact versions and content hashes — as against `pyproject.toml`, which records what was asked for. | day 1 part 2.1 | the lock, `uv.lock` |
```

Three rows are also appended for terms **day 0 part 1.1 defined first** and never recorded —
interpreter, environment and pin — attributed to the part that introduced them, so that this day can
link them instead of defining them again.

**`docs/PINS.md`** — the uv-managed interpreter and this project's one dependency, both observed
today, with the caveat that P00 Foundry is reference-only and carries no `PACKAGES.md` of its own
yet.

**`docs/SOURCES.md`** — nothing to add. This day cites three uv documentation pages, which are
living documentation rather than records with resolvable identifiers; they are dated in §9, which is
what that table is for.

**Commit:**

```text
day 01: P00 Foundry · 1 — The machine: uv, Python 3.12, and the four Pythons that ruin a Monday — closes FN-01
```
