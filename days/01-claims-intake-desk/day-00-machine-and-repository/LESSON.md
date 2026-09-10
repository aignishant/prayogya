---
project: "P01"
day: 0
title: "The machine and the repository"
spine: 0
kind: setup
deploy_tier: D3
plan_version: "v4.1.0"
parts: 8
files_printed: [PACKAGES.md, .python-version, PROJECT.md, .gitignore, .env.example, check.py, SETUP.md]
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** nothing. This is day 0 of this project, and it assumes a machine with nothing on
> it — no interpreter chosen, no repository, no key.
> **Today:** the claims desk gets a machine it can prove, a history that starts with its own brief,
> a rule that exists before the first secret does, and a check that goes red when any of that stops
> being true.
> **Tomorrow:** the folder becomes a package with a driver — `./run check` — and the four questions
> written today become the first thing it asks.

## §1 The scene

An intake counter opens on a Monday. Before the first notification arrives, somebody walks the
counter: the till has its float, the blank forms are on the shelf, the drawer with the claim notes
is locked, the register is open at today's date. None of that is the work. All of it is what makes
the work reproducible by the next person on the counter, and by the branch office that opens next
month, and by the auditor who asks in six months what the desk was running when it fast-tracked a
particular claim.

Today builds that counter for the Claims Intake Desk, and it builds it in the order that the
rules can still be written cheaply: the machine first, because a desk that runs on whichever
interpreter your path finds first is a desk that answers differently on two laptops; then the
repository, because a system nobody can describe in one page is a system nobody can call finished;
then the card on the drawer — the ignore rule — written while the drawer is still empty, because
once a secret is in git's hands the rule has nothing left to say about it; then the blank form,
which is the example file that carries names and never values; and finally the walk itself, as a
program, so the round is done by a machine rather than remembered by a person.

There is no model call today and no framework. There is a folder, seven files, a history that
records them one decision at a time, and a check that can go red — and by the end of it, a stranger
with an empty folder can reach the same green line you did.

## §2 The map

Three sections, in the order the counter is built. **Section 1 is what runs the desk** — the
machine, and how to stop it being whichever machine you happen to be standing at. **Section 2 is
what remembers the desk** — the repository, the brief that goes into it first, and the two files
that decide what git may and may not hold. **Section 3 is what proves it** — the round, written
down, broken on purpose, and handed to somebody who was not here.

### 1 · The machine — what runs the desk

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-machine/1.1-version-you-can-prove.md) | The version you can prove | What is this machine actually running, and where is that written down? | foundation |
| [1.2](parts/01-the-machine/1.2-interpreter-you-actually-get.md) | The interpreter you actually get | Why does `python` mean a different program on two machines, and how do you stop it? | foundation |

### 2 · The repository — what remembers the desk

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-repository/2.1-brief-and-first-commit.md) | The brief, and the first commit | What is this desk for, and why is that the first thing in the history? | foundation |
| [2.2](parts/02-the-repository/2.2-rule-before-the-secret.md) | The rule written before the secret | Why must `.gitignore` exist before `.env` does? | working |
| [2.3](parts/02-the-repository/2.3-names-without-the-values.md) | The names without the values | How does a clone learn which key it needs without ever being told the key? | working |

### 3 · The check — what proves it

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-the-check/3.1-four-questions-a-machine-can-answer.md) | Four questions a machine can answer | How do you assert a setup instead of remembering it? | working |
| [3.2](parts/03-the-check/3.2-secret-that-was-already-tracked.md) | The secret that was already tracked | What happens when the ignore rule arrives after the file — and what actually fixes it? | production |
| [3.3](parts/03-the-check/3.3-listing-a-stranger-can-follow.md) | The listing a stranger can follow | How do you know your setup document is true today? | production |

## §3 Setup — run this

Everything today needs. There is nothing to install for this project beyond the two tools, and no
environment yet — day 1 creates that.

```bash
uv --version
git --version
python --version

mkdir claims-intake-desk
cd claims-intake-desk

uv python pin 3.12.12
cat .python-version
uv run python -V

git init
git config user.name "your name"
git config user.email "you@example.com"
```

Expect `uv run python -V` to print `Python 3.12.12`. On most machines `python --version` prints
something else; if yours agrees, run `uv python list` and pin a version you do not already have.
That gap is part 1.2, and it is the reason the pin exists.

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
| `check.py` | `TODO(me)`: `check_untracked` reports `ok` both when git is not holding `.env` and when there is no repository at all. Only one of those is good news. Make the second one red. |
| `check.py` | `TODO(me)`: add a fifth check. A value left in `.env.example` is a secret published on purpose, and nothing in the file would notice. |
| `PACKAGES.md` | `TODO(me)`: replace the four rows with what **your** machine printed, with today's date. The values in part 1.1 are one machine's observations, not a target. |

## §6 The check that must be able to fail

```bash
uv run python check.py
```

Green is four `ok` lines and `claims desk: ready`, exit status 0.

Three ways to make it go red, and you should see at least the second one yourself:

1. **Run it with a bare `python`** instead of `uv run python`. The interpreter line goes red and
   names both versions.
2. **Force the secret into git** — `git add -f .env`, commit, run the check. Two lines go red at
   once, for two different reasons, and part 3.2 is the whole arc: cause it, read it, fix it with
   `git rm --cached`, and then rotate the key, because the value stays readable in the history.
3. **Blank the value in `.env`** and the fourth line names the variable that is empty — without
   printing anything that was in it.

A check nobody has watched fail is not evidence. Do at least one of these before ticking the box.

## §7 Request budget

**Zero.** No model is called today, by any agent, on any provider. There is no cast yet, no
framework installed and no network request in anything this day prints — `check.py` runs `git` and
reads two text files.

The key is obtained and stored today so that day 1 can pin a model and day 7 can call one. What the
free tier allows is not published as a number; AI Studio shows the limits for your own account, and
part 2.3 says where.

## §8 Traps

- **`uv python pin` accepts a version that does not exist.** It prints a warning, writes the pin,
  and exits 0. The failure surfaces later as a different command's error. Read the line it prints,
  and run `uv run python -V` straight after pinning.
- **A `.python-version` in a parent folder governs this one.** `uv` searches the working directory
  and every directory above it. If `uv run python -V` disagrees with your pin, look one level up
  before looking anywhere else.
- **`git add -A` is the enemy of this day.** Every `git add` in this day names its paths. The habit
  is what stops the accident in part 3.2 from being an accident you actually have.
- **The folder you build in may sit inside another repository.** `git init` here creates a separate
  repository for this project; check `git rev-parse --show-toplevel` if you are not sure which
  repository a `git` command is talking to.
- **On Windows, `git add` warns that CRLF will be replaced by LF.** It is about line endings, it
  appears on almost every file you add, and it has nothing to do with what you are adding. Do not
  go looking for a problem it is not reporting.
- **`!.env.example` must sit below `.env.*`.** Within one ignore file the last matching line
  decides, so a negation above the pattern it is excepting does nothing and the example file
  silently never reaches a clone.
- **`git check-ignore` answers about a path, not a file.** It works before the file exists — which
  is what lets the rule be written first — and it stops answering `ignored` the moment the path is
  tracked, without `.gitignore` changing at all.
- **Never paste the key into a terminal.** Open `.env` in an editor. A shell history is a file too.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| Where the free key comes from | `https://ai.google.dev/gemini-api/docs/api-key` | 2026-09-10 | Keys are created at `https://aistudio.google.com/apikey`. Both `GEMINI_API_KEY` and `GOOGLE_API_KEY` are read, with `GOOGLE_API_KEY` taking precedence when both are set. The page states: "Never check API keys into source control systems like Git." |
| Whether free-tier limits are published as numbers | `https://ai.google.dev/gemini-api/docs/rate-limits` | 2026-09-10 | No numeric per-model free-tier limits are published. The page says limits "can be viewed in Google AI Studio" and links to a per-account rate-limit page. This is why no number appears in this day. |
| What `uv python pin` writes, and how it is found | `https://docs.astral.sh/uv/concepts/python-versions/` | 2026-09-10 | `uv python pin` creates `.python-version` in the current directory, and uv "searches for a `.python-version` file in the working directory and each of its parents" — the behaviour behind the second trap in §8. |
| The toolchain on this machine | `uv --version`, `git --version`, `python --version`, `uv run python -V` | 2026-09-10 | uv 0.12.3 · git 2.54.0.windows.1 · bare `python` 3.12.10 · pinned interpreter 3.12.12. Every transcript in this day was produced with these. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block, which is the only region read:

```text
| 01 | 0 | 2026-09-10 | The machine and the repository | 8 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — one row per term this day defined. The first nine restate definitions the
glossary already carries, re-anchored to this project's own address; the rest are new:

```text
| Interpreter | The program that runs your code — one `python` executable at a real path, of one exact version. | P01 day 0 part 1.1 | the interpreter |
| Pin | A written-down exact version, recorded in a file so that a machine and not a memory decides what gets used. | P01 day 0 part 1.1 | the pin |
| Search order | The list of places a machine walks to turn a name like `python` into one program on disk. First match wins, and nothing announces that there was a choice. | P01 day 0 part 1.2 | discovery order |
| Tracked | A path git has been told to hold, from a `git add` onward. Ignore rules do not reach it: they speak only about paths git has never been told to hold. | P01 day 0 part 2.1 | under version control |
| Staging area | The list of paths git is holding for the next commit — what `git add` writes into and `git rm --cached` removes from. A path in it is tracked, whatever any ignore rule says. | P01 day 0 part 2.1 | git's index, the cache |
| Ignore source | One of the six places git reads exclude patterns from for a single path. Four are files in the repository; two are per-machine and invisible to review. | P01 day 0 part 2.2 | exclude source |
| Negated pattern | An ignore line beginning `!`, which takes a path back out of the ignore list. It only works below the pattern it is excepting, because within one file the last match decides. | P01 day 0 part 2.2 | a negation, an exception |
| Process environment | The set of name-to-string pairs the operating system handed a program when it started, which Python exposes as `os.environ`. It is built by whatever launched the program and has never heard of any file. | P01 day 0 part 2.3 | the environment block, env vars |
| Exit status | The single number a process hands back when it ends, and the only channel through which a check reports its verdict to another program. Zero means success; everything printed to the screen is for humans. | P01 day 0 part 3.1 | exit code, return code, `$?` |
| Observation | A value read off this machine today, together with the command that printed it and the date it was run. The only kind of value a pin ledger accepts; anything else is a guess wearing a number. | P01 day 0 part 1.1 | an observed value |
| Pin file | The file a pin lives in, read by a tool rather than by a person — here `.python-version`, whose entire contents are one version and a newline. Found by searching the working directory and each of its parents, which is why one written a level up governs everything beneath it. | P01 day 0 part 1.2 | `.python-version` |
| Repository | A folder plus a complete record of every change ever made inside it. Created by `git init`, held in `.git`, and indistinguishable from an ordinary folder until you ask. | P01 day 0 part 2.1 | the repo |
| Working tree | The folder as it exists on disk right now, as against the staging area, which is what git will record next, and the history, which is what it has already recorded. | P01 day 0 part 2.1 | the working copy |
| Commit | A permanent, named snapshot of everything that was staged, with a message saying why. Named by a hash computed from its contents, so the same change made twice is two different commits. | P01 day 0 part 2.1 | a revision, a snapshot |
| Check that can go red | A check somebody has actually watched fail. One nobody has seen fail is a green light with no wire behind it, and it is not evidence of anything. | P01 day 0 part 3.1 | a check with a wire behind it |
```

**`docs/PINS.md`** — no row is owed. Every version observed today is a fact about *this project's*
machine and belongs in the project's own `PACKAGES.md`, which part 1.1 prints; the authoring
repository's ledger already carries uv, git and Python from the day it was set up, at the same
values.

**`docs/SOURCES.md`** — no row is owed. This day cites no record with an identifier. The three
documentation pages it read are in §9 with the date they were fetched, which is where a
documentation URL belongs.

**Commit:**

```text
P01 day 0: The machine and the repository
```
