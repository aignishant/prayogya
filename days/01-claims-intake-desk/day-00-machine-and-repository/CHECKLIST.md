# P01 day 0 — definition of done

`python p.py done 01 0` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-the-machine/1.1-version-you-can-prove.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/01-the-machine/1.2-interpreter-you-actually-get.md` — read · ran its check · answered
      its question out loud
- [ ] `parts/02-the-repository/2.1-brief-and-first-commit.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/02-the-repository/2.2-rule-before-the-secret.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/02-the-repository/2.3-names-without-the-values.md` — read · ran its check · answered
      its question out loud
- [ ] `parts/03-the-check/3.1-four-questions-a-machine-can-answer.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/03-the-check/3.2-secret-that-was-already-tracked.md` — read · ran its check · answered
      its question out loud
- [ ] `parts/03-the-check/3.3-listing-a-stranger-can-follow.md` — read · ran its check · answered
      its question out loud

## Build

Every file typed by hand, at its real path, in this order. Nothing copied from a finished tree,
because there is no finished tree.

- [ ] `PACKAGES.md` — the four rows, with **your** machine's values and today's date
- [ ] `.python-version` — written by `uv python pin`, read back with `uv run python -V`
- [ ] `PROJECT.md` — the brief, committed first
- [ ] `.gitignore` — committed **before** `.env` exists on disk
- [ ] `.env.example` — names, no values, `!.env.example` sitting below `.env.*`
- [ ] `.env` — copied from the example, key pasted in an editor, never in a terminal
- [ ] `check.py` — the four checks, run green
- [ ] `SETUP.md` — the listing, with the green block that matches what your machine prints
- [ ] `check.py` — `TODO(me)`: make `secret untracked` red when there is no repository at all
- [ ] `check.py` — `TODO(me)`: a fifth check, for a value left in `.env.example`

## Check

- [ ] The day's check is green: `uv run python check.py` — four `ok` lines, `claims desk: ready`
- [ ] **Break it on purpose, watch it go red, fix it.** `git add -f .env`, commit, run the check —
      expect **two** red lines and exit 1. Fix with `git rm --cached .env`, commit, run it again.
      Then say out loud why the key in the history still has to be rotated.
- [ ] Ran it once with a bare `python` and watched the interpreter line go red
- [ ] `SETUP.md` followed **cold**, in a second empty folder, reaching `claims desk: ready` without
      consulting the folder you built today
- [ ] `python p.py depth 01 0` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path — no `...`, no
      "the rest is unchanged" without naming the day of THIS project that printed the original
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own earlier days — and
      day 0 assumes nothing at all: a bare machine, no interpreter chosen, no key

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the fifteen
      rows in the hub §10, restated definitions included
- [ ] Every version observed today has a row in this project's own `PACKAGES.md`, dated. No
      `docs/PINS.md` row is owed today, and the hub §10 says why
- [ ] No `docs/SOURCES.md` row is owed today — nothing with a citation identifier was cited, and
      the three documentation pages read are in the hub §9 with their dates
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
