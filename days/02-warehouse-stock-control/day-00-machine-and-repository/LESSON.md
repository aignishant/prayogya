---
project: "P02"
day: 0
title: "The machine and the repository"
spine: 0
kind: setup
deploy_tier: D3
plan_version: "v4.1.0"
parts: 8
files_printed: [PACKAGES.md, .python-version, PROJECT.md, .gitignore, .env.example, check.py, SETUP.md]
generated: "2026-09-12"
status: written
commit: ""
---

> **Yesterday:** nothing. This is day 0 of this project, and it assumes a machine with nothing on
> it — no interpreter chosen, no repository, no key.
> **Today:** the stock desk gets a machine it can prove, a record of what the world looked like on
> the day it started, a history that begins with its own brief and its own twenty-day map, a rule
> that exists before the first secret does, and a check that asks five questions and goes red when
> any answer stops being yes.
> **Tomorrow:** the folder becomes a package with a driver — `./run check` — and the five
> questions written today become the first thing it asks.

## §1 The scene

A company opens a warehouse in another town, and the night before the doors open somebody walks
it. The racking is up, the bins are labelled, the terminals are on. The walk is about none of
that. It is about whether the place can be *explained*: which software the terminals are running,
and where that is written down; where the ledger is and who is allowed to write in it; that the
cage's rule is on the door before the first pallet goes in and the combination is in a pocket
rather than in the ledger's notes column; and that the walk itself is a form somebody can fill in
tomorrow without having been here tonight.

Today builds that walk for the Warehouse Stock Control desk, and it builds it in the order the
rules can still be written cheaply: the machine first, because a desk that runs on whichever
interpreter your path finds first is a desk that answers differently on two terminals six feet
apart; then a record of the world on the day the project started — the framework's latest version,
the protocol's current revision — because the day the desk installs them is not the day to find
out they moved; then the repository, with the brief and this project's own twenty-day map as its
first commit; then the rule on the cage door, written while the cage is empty; then the tag on the
key that carries a name and never a value; and finally the walk itself, as a program, asking five
questions of the machine rather than of the reader.

Five questions, where a first version of this walk would ask four. The fifth is *is this folder's
repository this folder's?* — because a project cloned under somebody else's repository answers
every other git question reassuringly and wrongly, and the only way to know is to ask git where it
thinks the root is. There is no model call today and no framework. There is a folder, seven files,
a history that records them one decision at a time, and a check that can go red six different
ways — and by the end of it, a stranger with an empty folder can reach the same green line you did,
which this day proves by handing the listing to an empty folder and watching.

## §2 The map

Three sections, in the order the walk is built. **Section 1 is what runs the desk** — the machine,
and how to stop it being whichever machine you happen to be standing at. **Section 2 is what
remembers the desk** — the repository, the brief that goes into it first, and the two files that
decide what git may and may not hold. **Section 3 is what proves it** — the walk, written down,
broken on purpose, and handed to somebody who was not here.

### 1 · The machine — what runs the desk

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-machine/1.1-version-you-can-prove.md) | The version you can prove | What is this machine actually running, what did the world look like today, and where is that written down? | foundation |
| [1.2](parts/01-the-machine/1.2-interpreter-you-actually-get.md) | The interpreter you actually get | Why does `python` mean a different program on two machines, and how do you stop it — and what happens when the pin is in the wrong folder? | foundation |

### 2 · The repository — what remembers the desk

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-repository/2.1-brief-and-first-commit.md) | The brief, and the first commit | What is this desk for, which twenty days build it, and why is that the first thing in the history? | foundation |
| [2.2](parts/02-the-repository/2.2-rule-before-the-secret.md) | The rule written before the secret | Why must `.gitignore` exist before `.env` does, and how do you ask git about a file that is already committed? | working |
| [2.3](parts/02-the-repository/2.3-names-without-the-values.md) | The names without the values | How does a clone learn which key it needs without ever being told the key, and which of two names does the provider prefer? | working |

### 3 · The check — what proves it

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-the-check/3.1-five-questions-a-machine-can-answer.md) | Five questions a machine can answer | How do you assert a setup instead of remembering it, and why is "is this my repository?" one of the questions? | working |
| [3.2](parts/03-the-check/3.2-secret-that-was-already-tracked.md) | The secret that was already tracked · **failure** | What happens when the ignore rule arrives after the file — and what actually fixes it? | production |
| [3.3](parts/03-the-check/3.3-listing-a-stranger-can-follow.md) | The listing a stranger can follow | How do you know your setup document is true today? | production |

## §3 Setup — run this

Everything today needs. There is nothing to install for this project beyond the two tools, and no
environment yet — day 1 creates that.

```bash
uv --version
git --version
python --version
uv python list | head -8

mkdir warehouse-stock-control
cd warehouse-stock-control

uv python pin 3.12.13
cat .python-version
uv run python -V

git init
git config user.name "your name"
git config user.email "you@example.com"
git rev-parse --show-toplevel
```

Expect `uv python pin 3.12.13` to download about twenty megabytes the first time, and `uv run
python -V` to print `Python 3.12.13`. On most machines `python --version` prints something else;
if yours agrees, run `uv python list` and pin a version you do not already have. That gap is part
1.2, and it is the reason the pin exists. Expect `git rev-parse --show-toplevel` to print the
folder you just made; if it prints a folder above it, stop and read part 2.1's failure.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `PACKAGES.md` | part 1.1 |
| `.python-version` | part 1.2 |
| `PROJECT.md` | part 2.1 |
| `.gitignore` | part 2.2 |
| `.env.example` | part 2.3 |
| `check.py` | part 3.1 |
| `SETUP.md` | part 3.3 |

Every one of them is printed whole, at the path it goes to. You type them; nothing arrives
pre-built.

## §5 Build brief

Type the seven files above from the parts that print them, in that order, committing as you go —
`.gitignore` before `.env` exists is not a preference. Then the reps, which are left unsolved on
purpose and are marked `TODO(me)` in the files themselves:

| File | What it must do |
| --- | --- |
| `check.py` | `TODO(me)`: a sixth check. A value left in `.env.example` is a secret published on purpose, and nothing in the file would notice. |
| `check.py` | `TODO(me)`: `check_key` accepts any non-empty value, including `your key here` typed from a tutorial. Decide what a value that is obviously not a key should do, and why the file must still never print it. |
| `check.py` | `TODO(me)`: part 2.2's swapped negation makes `.env.example` unreachable by a clone, and no check notices. Decide whether a seventh question — `git check-ignore --no-index .env.example` must exit 1 — belongs here, and what it would print. |
| `PACKAGES.md` | `TODO(me)`: replace the four machine rows with what **your** machine printed, with today's date, and open the three URLs in the last three rows and write what they say *today*. The values in part 1.1 are one machine's observations on one date, not a target. |
| `SETUP.md` | `TODO(me)`: section 1 sends a reader to the tool's install page. On a machine you can wipe, follow it and paste what the install printed under section 1, dated. |

## §6 The check that must be able to fail

```bash
uv run python check.py
```

Green is five `ok` lines and `stock desk: ready`, exit status 0.

Six ways to make it go red, and you should see at least the second one yourself:

1. **Run it with a bare `python`** instead of `uv run python`. The interpreter line goes red and
   names both versions.
2. **Force the secret into git** — `git add -f .env`, commit, run the check. Two lines go red at
   once, for two different reasons, and part 3.2 is the whole arc: cause it, read it, fix it with
   `git rm --cached`, and then rotate the key, because the value stays readable in the history.
3. **Blank the value in `.env`** and the fifth line names the variable that is empty — without
   printing anything that was in it.
4. **Copy the folder somewhere without its `.git`.** Two lines go red — `repository` and, for the
   wrong reason, `ignore rule` — and part 3.1 says why the first line is the one to read.
5. **Copy the folder, without its `.git`, into a folder that is a repository.** The `repository`
   line names the other root.
6. **Move `.python-version` up one folder.** `uv run python -V` still prints a version — the
   parent's — and the check says `no .python-version`, which is part 1.2's trap arriving as a red
   line.

A check nobody has watched fail is not evidence. Do at least one of these before ticking the box.

## §7 Request budget

**Zero.** No model is called today, by any agent, on any provider. There is no cast yet, no
framework installed and no network request in anything this day prints — `check.py` runs `git`
and reads two text files. The three lookups part 1.1 records were pages opened by a person, once.

The key is obtained and stored today so that day 1 can pin a model and day 8 can call one. What
the free tier allows is not published as a number; AI Studio shows the limits for your own
account, and part 2.3 says where.

## §8 Traps

- **`uv python pin` accepts a version that does not exist.** It prints a warning, writes the pin,
  and exits 0. The failure surfaces later as a different command's error. Read the line it prints,
  and run `uv run python -V` straight after pinning.
- **A `.python-version` in a parent folder governs this one when this one has none.** `uv`
  searches the working directory and every directory above it, silently. The check's first line
  is what notices.
- **Pin the newest patch the tool offers, not the one already installed.** The one already
  installed was somebody else's choice; a project that starts today starts on today's
  interpreter, and the `Downloading` line is the proof it was chosen rather than found.
- **Record what the world looked like on day 0** — the framework, the SDK, the protocol revision
  — as *observed, not installed*. The day that installs them reads the row first.
- **`git add -A` is the enemy of this day.** Every `git add` in this day names its paths. The habit
  is what stops the accident in part 3.2 from being an accident you actually have.
- **The folder you build in may sit inside another repository.** `git init` here creates a
  separate repository for this project; `git rev-parse --show-toplevel` is how you know which
  repository a `git` command is talking to, and the check asks it for you.
- **On Windows, `git add` warns that CRLF will be replaced by LF.** It is about line endings, it
  appears on almost every file you add, and it has nothing to do with what you are adding.
- **`!.env.example` must sit below `.env.*`.** Within one ignore file the last matching line
  decides, so a negation above the pattern it is excepting does nothing and the example file
  silently never reaches a clone.
- **A tracked path is never asked about.** `git check-ignore` on a committed `.env.example` is
  silent whatever the rules say; ask with `--no-index` to test the rules themselves.
- **Silence plus exit 1 means two opposite things** — *not ignored, correctly* for the example
  file and *not ignored, because tracked* for a leaked `.env`. Read the exit status, and let the
  check print its own sentence.
- **The provider reads two variable names and prefers one.** Set `GOOGLE_API_KEY` and nothing
  else, and say why in the comment.
- **Never paste the key into a terminal.** Open `.env` in an editor. A shell history is a file too.
- **A listing written from memory is missing the step you never think about.** Write it from a
  run in an empty folder, and paste the run under the last section.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| Where the free key comes from | `https://ai.google.dev/gemini-api/docs/api-key` | 2026-09-12 | Keys are created at `https://aistudio.google.com/apikey`. Both `GEMINI_API_KEY` and `GOOGLE_API_KEY` are read; "If both are set, `GOOGLE_API_KEY` takes precedence." The page states: "Never check API keys into source control systems like Git." |
| Whether free-tier limits are published as numbers | `https://ai.google.dev/gemini-api/docs/rate-limits` | 2026-09-12 | No numeric per-model free-tier limits are published. "Rate limits depend on a variety of factors (such as your usage tier) and can be viewed in Google AI Studio." This is why no number appears in this day. |
| What `uv python pin` writes, and how it is found | `https://docs.astral.sh/uv/concepts/python-versions/` | 2026-09-12 | `uv python pin` creates `.python-version` in the current directory; uv "searches for a `.python-version` file in the working directory and each of its parents" — the behaviour behind part 1.2's failure; "Python versions are automatically downloaded as needed". |
| The framework's latest release | `https://pypi.org/pypi/google-adk/json` | 2026-09-12 | `2.9.0`, released 2026-09-10; `requires_python >=3.10`; the `mcp` extra requires `mcp<2,>=1.24`. Recorded in `PACKAGES.md` as observed, not installed. |
| The framework's release notes since 2.8.0 | `https://github.com/google/adk-python/releases` | 2026-09-12 | `v2.9.0` (2026-09-10) lists changes to workflow resume, session-service errors, and MCP 2.x field handling; `v2.8.0` lists none. Nothing in this project's plan text depends on either version; the day that installs the framework reads these notes and pins with them in front of it. |
| The SDK's latest release | `https://pypi.org/pypi/mcp/json` | 2026-09-12 | `2.2.0`; `requires_python >=3.10`. |
| The protocol's current revision | `https://modelcontextprotocol.io/docs/learn/versioning` | 2026-09-12 | "The **current** protocol version is **2026-07-28**." Every request declares its version in `_meta`; `server/discover` is the up-front alternative. |
| The provider's Flash models today | `https://ai.google.dev/gemini-api/docs/models` | 2026-09-12 | `gemini-3.8-flash` "New Stable", `gemini-3.7-flash`, `gemini-3.6-flash`, `gemini-3.5-flash` "legacy". A `-latest` alias "will get hot-swapped with every new release". Day 1 pins from this list. |
| The toolchain on this machine | `uv --version`, `git --version`, `python --version`, `uv python list`, `uv run python -V` | 2026-09-12 | uv 0.12.3 · git 2.54.0.windows.1 · bare `python` 3.12.10 · `3.12.13` offered for download and pinned; `3.12.12` already present from elsewhere and not chosen. Every transcript in this day was produced with these. |
| The pin that does not exist | this project, `uv python pin 3.12.99` | 2026-09-12 | A warning, `Updated .python-version from 3.12.13 -> 3.12.99`, and exit 0. |
| The pin in the parent folder | this project | 2026-09-12 | With no pin here and `3.12.12` one folder up, `uv run python -V` prints `Python 3.12.12` and the check prints `no .python-version`. |
| The ignore question, four ways | this project, `git check-ignore -v` | 2026-09-12 | `.env` → `.gitignore:8:.env`, exit 0, before the file existed; `.env.local` → line 9; `.env.example` → silent, exit 1 (tracked), and with `--no-index` → `.gitignore:10:!.env.example`, exit 0; with lines 9 and 10 swapped and `--no-index` → `.gitignore:10:.env.*`, exit 0. |
| The check, green and red | this project, `uv run python check.py` | 2026-09-12 | Five `ok` lines and exit 0; red on the bare interpreter (`pinned 3.12.13, running 3.12.10`), on a force-added `.env` (two lines), on a blank value, on no repository (two lines), on a nested repository (`rooted at .../outer`), and on a missing pin. |
| The secret in the history | this project, `git show HEAD~1:.env` | 2026-09-12 | The value printed back from the commit that added it, after the commit that stopped tracking it. |
| The listing, handed over | an empty folder, `SETUP.md` alone | 2026-09-12 | Sections 1 to 6 typed cold; `Python 3.12.13`; the toplevel is the new folder; five `ok` lines and `stock desk: ready`. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block, which is the only region read:

```text
| 02 | 0 | 2026-09-12 | The machine and the repository | 8 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — one row per term this day defined. Fifteen re-anchor definitions the
glossary already carries to this project's own address, defined the same way; the last two are new:

```text
| Interpreter | The program that runs your code — one `python` executable at a real path, of one exact version. | P02 day 0 part 1.1 | the interpreter |
| Pin | A written-down exact version, recorded in a file so that a machine and not a memory decides what gets used. | P02 day 0 part 1.1 | the pin |
| Observation | A value read off this machine today, together with the command that printed it and the date it was run — or a page opened today, with its URL. The only kind of value a pin ledger accepts; anything else is a guess wearing a number. | P02 day 0 part 1.1 | an observed value |
| Search order | The list of places a machine walks to turn a name like `python` into one program on disk. First match wins, and nothing announces that there was a choice. | P02 day 0 part 1.2 | discovery order |
| Pin file | The file a pin lives in, read by a tool rather than by a person — here `.python-version`, whose entire contents are one version and a newline. Found by searching the working directory and each of its parents, which is why one written a level up governs everything beneath it. | P02 day 0 part 1.2 | `.python-version` |
| Repository | A folder plus a complete record of every change ever made inside it. Created by `git init`, held in `.git`, and indistinguishable from an ordinary folder until you ask. | P02 day 0 part 2.1 | the repo |
| Working tree | The folder as it exists on disk right now, as against the staging area, which is what git will record next, and the history, which is what it has already recorded. | P02 day 0 part 2.1 | the working copy |
| Staging area | The list of paths git is holding for the next commit — what `git add` writes into and `git rm --cached` removes from. A path in it is tracked, whatever any ignore rule says. | P02 day 0 part 2.1 | git's index, the cache |
| Commit | A permanent, named snapshot of everything that was staged, with a message saying why. Named by a hash computed from its contents, so the same change made twice is two different commits. | P02 day 0 part 2.1 | a revision, a snapshot |
| Tracked | A path git has been told to hold, from a `git add` onward. Ignore rules do not reach it: they speak only about paths git has never been told to hold. | P02 day 0 part 2.1 | under version control |
| Ignore source | One of the six places git reads exclude patterns from for a single path. Four are files in the repository; two are per-machine and invisible to review. | P02 day 0 part 2.2 | exclude source |
| Negated pattern | An ignore line beginning `!`, which takes a path back out of the ignore list. It only works below the pattern it is excepting, because within one file the last match decides. | P02 day 0 part 2.2 | a negation, an exception |
| Process environment | The set of name-to-string pairs the operating system handed a program when it started, which Python exposes as `os.environ`. It is built by whatever launched the program and has never heard of any file. | P02 day 0 part 2.3 | the environment block, env vars |
| Exit status | The single number a process hands back when it ends, and the only channel through which a check reports its verdict to another program. Zero means success; everything printed to the screen is for humans. | P02 day 0 part 3.1 | exit code, return code, `$?` |
| Check that can go red | A check somebody has actually watched fail. One nobody has seen fail is a green light with no wire behind it, and it is not evidence of anything. | P02 day 0 part 3.1 | a check with a wire behind it |
| Freshness row | A version recorded at the start of a project as observed and not installed — the framework, the SDK, the protocol revision — so that the day that installs it decides against what the world looked like when the project began, not against whatever a registry says that morning. | P02 day 0 part 1.1 | observed, not installed |
| Top level | The folder git treats as a repository's root, printed by `git rev-parse --show-toplevel`. When it is not the folder you are standing in, every git question you ask is being answered about somebody else's repository. | P02 day 0 part 2.1 | the repository root |
```

**`docs/PINS.md`** — no row is owed. Every version observed today is a fact about *this project's*
machine or its day-0 world and belongs in the project's own `PACKAGES.md`, which part 1.1 prints.
The authoring repository's ledger already carries uv, git and Python at the same values; the new
interpreter patch is a project pin.

**`docs/SOURCES.md`** — no row is owed. This day cites no record with an identifier. The eight
pages it read are in §9 with the date they were fetched, which is where a documentation URL
belongs.

**`docs/CHANGELOG_PLAN.md`** — no amendment. The freshness check found the framework one minor
version ahead of the last project's pin and the protocol revision unchanged; nothing in the plan's
text depends on the framework's version, and the pin is the installing day's decision.

**Commit:**

```text
P02 day 0: The machine and the repository
```
