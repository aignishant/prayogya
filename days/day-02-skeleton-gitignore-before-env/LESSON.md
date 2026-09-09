---
project: "P00 Foundry"
day: 2
phase: P00
title: "P00 Foundry · 2 — The skeleton: `.gitignore` before `.env` exists, and why that order"
ids: [FN-02]
kind: setup
deploy_tier: "—"
plan_version: "v3.1.0"
parts: 4
files_printed:
  - "projects/00-foundry/.gitignore"
  - "projects/00-foundry/.env.example"
generated: "2026-09-09"
status: written
commit: ""
---

> **Yesterday:** a project folder that owns its own interpreter, and two files that state the
> requirement so a shell cannot get it wrong.
> **Today:** the two files that decide what the project hands out — written in the order that makes
> them work, and proved by asking git rather than by reading them.
> **Tomorrow:** P00 Foundry day 3, keys and pinning, and the check that refuses a half-finished day.

## §1 The scene

A sticker goes on a front door: *no leaflets*. It works for a year. Then they move house, and on
the first morning the slot goes twice before the sticker is up. The two leaflets on the mat do not
care about the sticker put up that afternoon, and nobody expected them to — the sticker is a fact
about the door, and the mat is inside the house.

Today the project gets its sticker, and it goes up on the first morning rather than the second. The
file that has to stay out is the one holding real values — a key, a password — and it does not
exist yet. That is the point. Writing the rule while there is nothing to protect feels like filing;
writing it afterwards is a different job entirely, because by then the thing you are protecting has
already been through the slot.

Then the sticker turns out to be too generous, in the way stickers are. It stops one file you
wanted — the one that tells a stranger which keys this project reads, without telling them any of
the values. So a second line goes on, underneath, and *underneath* is load-bearing: the postman
does what the last line he read told him.

And then the day's real lesson, which is not about either file. It is that "I know what my sticker
says" is not an answer to why a letter did or did not arrive. There is a sticker on the building's
street door too, and a list in the caretaker's office you have never seen. So you stop reading and
start asking, with a command that names the file and the line number that actually decided — and
you learn what its silence means, because on the one path where it stays quiet, quiet reads exactly
like *you are fine*.

## §2 The map

Two sections. The first is the pair of files and the order they have to be written in — that is the
day's title, and it is a claim about sequence, so both parts are about sequence. The second replaces
reading the files with interrogating them, and then breaks the interrogation on purpose, because a
tool that answers correctly and misleadingly at the same time is the thing worth an evening.

### 1 · The order

*The mental model: the rule is a fact about the door. It has no opinion about what is already in the
house, so it has to be standing before anything arrives.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-order/1.1-the-rule-before-the-file.md) | The rule before the file | What does `.gitignore` decide, and what can it never undo? | foundation |
| [1.2](parts/01-the-order/1.2-the-example-that-carries-the-shape.md) | The example that carries the shape | Why commit a second env file, and why does one line's position decide whether it survives? | working |

### 2 · Asking git instead of guessing

*The mental model: don't read the rules and reason about them — make git name the line it obeyed,
and learn what it means when it names nothing.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-asking-git/2.1-the-line-that-decided.md) | The line that decided | Which of the six possible sources held the rule, and why is the exit code not the answer? | working |
| [2.2](parts/02-asking-git/2.2-the-file-git-had-already-seen.md) | The file git had already seen | What does an ignore rule do for a file git is already holding, and how does it tell you? | production |

## §3 Setup — run this

Nothing to install today — the toolchain has not changed since day 1. Everything below was run on
this machine today and what it reported is in §9. Run them in order from the repository root.

```bash
cd projects/00-foundry
git status --short .

# part 1.1 writes .gitignore; part 1.2 writes .env.example and amends .gitignore
git check-ignore -v .env
git check-ignore -v .env.example

# part 2.1 — the same names, asked where a different ignore file is nearer
cd ../..
git check-ignore -v .env .env.example
```

The `.env` you create today holds a synthetic value and nothing else. There is no provider, no key
and no account in P00 Foundry — real keys arrive on day 3, behind a check that can refuse them.

## §4 Files this day prints

Two files, both of them the project's own. The repository root already has a `.gitignore`, printed
by **day 0 part 1.2**; nothing today reprints it, and part 2.1 uses the fact that there are now two
of them as its subject rather than as a footnote.

| File | Printed by |
| --- | --- |
| `projects/00-foundry/.gitignore` | part 1.1, whole; part 1.2 adds a marked diff |
| `projects/00-foundry/.env.example` | part 1.2, whole |

## §5 Build brief

| File | What it must do |
| --- | --- |
| `projects/00-foundry/.gitignore` | `TODO(me)`: type it before creating anything it names. Then create `.env` and say, before running anything, which line you expect git to name — and whether you expect `git add .env` to succeed. |
| `projects/00-foundry/.env.example` | `TODO(me)`: type it, then run `git status --short .` and explain why the file is not offered. Say which line of `.gitignore` you have to add, and where it has to go, before you add it. |
| `projects/00-foundry/.gitignore` (the diff) | `TODO(me)`: add the negation. Then move it above `.env.*`, run `git check-ignore -v .env.example`, and say why the output changed when the file's contents did not. Put it back. |
| any part of this day | `TODO(me)`: run `git check-ignore -v .env.example` and `git check-ignore .env.example` and read the two exit statuses. Say which of the two you would put in a script, and what the other one would do to it. |
| the failure rep | `TODO(me)`: in a scratch directory outside this repository, `git init`, create a file, `git add` it, *then* write the ignore rule. Compare plain `check-ignore` with `--no-index`, then commit, `git rm --cached`, commit again, and find the file in `git log -p`. |

## §6 The check that must be able to fail

```text
python p.py depth 2                                  # this day against the plan §5 contract
git check-ignore -v projects/00-foundry/.env         # must name the project's own file
git check-ignore --no-index projects/00-foundry/.env # must exit 0
git status --short projects/00-foundry               # must not list .env; must list .env.example
```

**How to make it go red on purpose — three ways, and the third is the day's real one.**

The first is the negation's position: move `!.env.example` above `.env.*` and the fourth command
stops listing `.env.example`. There is no error and no warning; the file simply leaves the output,
which is what makes it worth causing once.

The second is precedence. Append `!.env` to `projects/00-foundry/.gitignore` and the last command
starts offering the real secret as a new file, overruling the root ignore file exactly as the
documentation says a lower-level file may. Part 2.1 has the transcript.

The third is the wrong order, and it is part 2.2. Park the ignore file, create a credential file,
`git add .`, then put the ignore file back and run `git check-ignore -v` on it: **no output, exit
`1`** — indistinguishable from "no rule matches", while the path sits staged. `--no-index` names the
rule that was there all along. If your `check-ignore` prints a line, the file was never staged and
the day has proved nothing. Fix it with `git rm --cached`, and read what that does *not* fix.

For the document itself: delete a `## In production` heading from any part and run
`python p.py depth 2`; it names the file and the missing section.

## §7 Request budget

**Zero model calls.** P00 Foundry contacts no provider, has no agent and needs no key — the plan
§11 gives it no tier, no tools, no MCP boundary and no cast, because its subject is the machine.
Today it also has no `.env` worth reading: the file created here holds a synthetic value, and the
first real key arrives on day 3.

Stating the zero rather than omitting it is the habit that matters, because from P01 onward the
number is never zero and every hub carries it. The plan §9 counts requests **across the whole
cast**: a three-agent turn is at least three requests, and a writer-critic loop is unbounded until
you bound it.

## §8 Traps

- **An ignore rule has no opinion about a tracked file.** The documentation says so plainly, and
  the consequence is that adding the rule after `git add` accomplishes nothing at all.
- **`git check-ignore` says nothing about a tracked path** — no line, exit `1`, identical to "no
  rule matches". This is the day's most expensive silence. `--no-index` is the flag that separates
  the two cases.
- **`-v` changes what the exit status means.** With `-v` the command reports *matches*, so a negated
  pattern gives output and exit `0` on a path that is not ignored. Without `-v` the same path exits
  `1`. Read the output when you use `-v`; read the status when you do not.
- **Within one file, the last matching pattern wins** — so a negation must sit *below* the rule it
  is excepting. Above it, the negation is present, correct, and inert.
- **Between files, the nearer one wins.** `projects/00-foundry/.gitignore` overrides the repository
  root's file for paths beneath it, which is what makes a project's rules travel with it — and also
  means a stray `!` line there can un-protect a secret the root file was covering.
- **Two of the six sources are not in the repository.** `.git/info/exclude` and the file named by
  `core.excludesFile` cannot be seen by a reviewer, so "it's ignored on my machine" is a statement
  about a machine.
- **`git add -f` is silent.** The refusal in part 1.1 prints a hint naming the flag that defeats it,
  and using that flag produces no output at all.
- **`git rm` without `--cached` deletes the file from disk.** On a credential you have not saved
  anywhere else, that is a second incident stacked on the first.
- **`fatal: pathspec ... did not match any files` is not reassurance.** `git rm` looks in the index;
  that message means git is not holding the path you typed, not that there is nothing to fix.
- **A leaked value is not fixed by a git command.** `git rm --cached` changes the index and the next
  commit, and none of the commits already made. The fix is a new credential.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| Ignore rules do not reach tracked files | `https://git-scm.com/docs/gitignore` | 2026-09-09 | "Files already tracked by Git are not affected" — quoted in part 1.1 |
| The order of precedence between ignore sources | `https://git-scm.com/docs/gitignore` | 2026-09-09 | Command line, then per-directory files with lower levels overriding higher, then `$GIT_COMMON_DIR/info/exclude`, then `core.excludesFile` — quoted in full in part 2.1 |
| Last matching pattern decides, and what `!` buys | `https://git-scm.com/docs/gitignore` | 2026-09-09 | "the last matching pattern decides the outcome"; "any matching file excluded by a previous pattern will become included again" — parts 1.2 and 2.1 |
| The `-v` output format | `https://git-scm.com/docs/git-check-ignore` | 2026-09-09 | `<source> <COLON> <linenum> <COLON> <pattern> <HT> <pathname>`, with `!` and `/` preserved — the table in part 2.1 |
| What `-v` actually reports, and the exit statuses | `https://git-scm.com/docs/git-check-ignore` | 2026-09-09 | `-v` prints a line "for each path that matches an exclude pattern", negations included; `0` is documented as "One or more of the provided paths is ignored" and `1` as "None of the provided paths are ignored" |
| Tracked files are not reported at all | `https://git-scm.com/docs/git-check-ignore` | 2026-09-09 | "By default, tracked files are not shown at all since they are not subject to exclude rules; but see `--no-index`" — part 2.2's whole subject |
| `--no-index` exists for this exact diagnosis | `https://git-scm.com/docs/git-check-ignore` | 2026-09-09 | "can be used to debug why a path became tracked by e.g. `git add .` and was not ignored by the rules as expected by the user" |
| The project's own file overrides the root's | `git check-ignore -v .env .env.example .venv` in `projects/00-foundry` | 2026-09-09 | All three answers named `projects/00-foundry/.gitignore`, lines 5, 7 and 13 — never the root file |
| The same names resolve differently at the root | the same command run from the repository root | 2026-09-09 | `.gitignore:2:.env` and `.gitignore:4:!.env.example` — different source, different lines, same verdicts |
| `-v` exits 0 on a path that is not ignored | `git check-ignore -v .env.example` against `git check-ignore .env.example` | 2026-09-09 | `0` with `-v`, `1` without, on the same file in the same directory |
| `git add` refuses an ignored path by name | `git add .env` | 2026-09-09 | The two-line hint, exit `1`; and `git add -f .env` staged it with no output at all |
| A negation above its rule is inert | `!.env.example` moved to line 5, `.env.*` at line 7 | 2026-09-09 | `check-ignore` named line 7, and `.env.example` vanished from `git status --short .` |
| A lower-level `!` overrules the root file | `!.env` appended to the project's ignore file | 2026-09-09 | `projects/00-foundry/.gitignore:16:!.env`, and `git status` began offering `.env` |
| `check-ignore` is silent for a tracked path | staging `service-account.json` before writing its rule | 2026-09-09 | No output and exit `1` with the rule present on line 10; `--no-index` named line 10 and exited `0` |
| `git rm --cached` restores the rule's reach | the same file, unstaged | 2026-09-09 | `rm 'projects/00-foundry/service-account.json'`, then `check-ignore` named line 10 again; the file stayed on disk |
| `git rm` on an unheld path is fatal, not empty | `git rm --cached foundry.log` | 2026-09-09 | `fatal: pathspec 'foundry.log' did not match any files`, exit `128` |
| git version | `git --version` | 2026-09-09 | `git version 2.54.0.windows.1` — the same value day 0 recorded in `docs/PINS.md`, re-observed rather than assumed |

## §10 Ledger & commit

**`docs/PROGRESS.md`:**

```text
| 2 | 2026-09-09 | FN-02 | 4 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the terms this day defined for the first time:

```text
| Tracked | A path git has been told to hold, from a `git add` onward. Ignore rules do not reach it: they speak only about paths git has never been told to hold. | day 2 part 1.1 | under version control |
| Staging area | The list of paths git is holding for the next commit — what `git add` writes into and `git rm --cached` removes from. A path in it is tracked, whatever any ignore rule says. | day 2 part 2.2 | git's index, the cache |
| Ignore source | One of the six places git reads exclude patterns from for a single path. Four are files in the repository; two are per-machine and invisible to review. | day 2 part 2.1 | exclude source |
| Negated pattern | An ignore line beginning `!`, which takes a path back out of the ignore list. It only works below the pattern it is excepting, because within one file the last match decides. | day 2 part 1.2 | a negation, an exception |
```

**`docs/PINS.md`** — nothing to add. The one version this day depends on is git 2.54.0.windows.1,
already recorded by day 0; it was re-observed today rather than assumed, and that observation is in
§9 above, which is where a re-check with an unchanged value belongs.

**`docs/SOURCES.md`** — nothing to add. This day cites two git documentation pages, which are living
documentation rather than records with resolvable identifiers; they are dated in §9, which is what
that table is for. This is the same call day 1 made about the uv pages.

**Commit:**

```text
day 02: P00 Foundry · 2 — The skeleton: .gitignore before .env exists, and why that order — closes FN-02
```
