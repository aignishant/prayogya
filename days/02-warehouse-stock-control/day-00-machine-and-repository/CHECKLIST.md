# P02 day 0 — definition of done

`python p.py done 02 0` refuses to commit while any box below is unticked. That refusal is the
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
- [ ] `parts/03-the-check/3.1-five-questions-a-machine-can-answer.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/03-the-check/3.2-secret-that-was-already-tracked.md` — read · ran its check · answered
      its question out loud
- [ ] `parts/03-the-check/3.3-listing-a-stranger-can-follow.md` — read · ran its check · answered
      its question out loud

## Build

- [ ] `PACKAGES.md` — seven rows: four from your machine, three from the pages, all dated today
- [ ] `.python-version` — `3.12.13`, or the newest 3.12 patch `uv python list` offered you, and
      the `Downloading` line seen
- [ ] `PROJECT.md` — the brief, the triad, the twenty-day map with days 4 and 6, the feature-set
      table, done-when, synthetic — committed first and alone
- [ ] `.gitignore` — written and committed **before** `.env` exists, `!.env.example` below `.env.*`
- [ ] `.env.example` — one name, no value, the provider's URL, the reason for the name
- [ ] `.env` — copied, filled in with an editor, never mentioned by `git status`
- [ ] `check.py` — five questions, `repository` before the two git questions that depend on it
- [ ] `SETUP.md` — six sections, `git rev-parse --show-toplevel` in section 3, the green run under
      section 6
- [ ] `check.py` — `TODO(me)`: the sixth check, a value in `.env.example`
- [ ] `check.py` — `TODO(me)`: what `check_key` should do with a value that is obviously not a key
- [ ] `check.py` — `TODO(me)`: whether the swapped-negation case deserves a seventh question
- [ ] `PACKAGES.md` — `TODO(me)`: your machine's rows and today's page values, not this document's
- [ ] `SETUP.md` — `TODO(me)`: section 1's install, followed on a machine you can wipe, pasted and
      dated

## Check

- [ ] The day's check is green: `uv run python check.py` — five `ok` lines, `stock desk: ready`,
      exit status 0
- [ ] Ran `uv python list` and said which line your pin came from, and whether it downloaded
- [ ] Ran `git rev-parse --show-toplevel` and read your own folder
- [ ] Ran `git check-ignore -v .env` before `.env` existed and read `.gitignore:8:.env`
- [ ] Ran `git check-ignore -v --no-index .env.example` and read line 10's negation
- [ ] Ran `git show HEAD~1:.env` after the untracking commit and read the value come back
- [ ] **Break it on purpose, watch it go red, fix it.** Bare `python check.py`. `git add -f .env`,
      commit, two red lines, `git rm --cached .env`, green. A blank value. A copy with no `.git`.
      A copy inside another repository. The pin moved up one folder. Put every one back.
- [ ] **The failure that stays quiet.** Swap lines 9 and 10 of `.gitignore`, ask with
      `--no-index`, read `.env.*` deciding, and confirm `check.py` stays green. Swap them back.
- [ ] **The handing-over.** An empty folder, `SETUP.md`, nothing else — and your screen diffed
      against section 6
- [ ] `python p.py depth 02 0` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but on this machine, today — the interpreter
      was downloaded, not found; the repository is this folder's, not a parent's
- [ ] No number in any part is quoted from this document rather than from your own run — the
      versions, the commit hashes, the line numbers in `.gitignore`, the download size
- [ ] No file in this project carries a key, a key's value, or a placeholder that the check would
      accept as one

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the seventeen
      rows in the hub §10, fifteen of them re-anchoring terms the glossary already carries
- [ ] No `docs/PINS.md` row is owed — every version today is a project pin, in `PACKAGES.md`
- [ ] No `docs/SOURCES.md` row is owed — the eight pages are in the hub §9 with the date
- [ ] No `docs/CHANGELOG_PLAN.md` amendment is owed — the freshness check moved no plan text
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10 — the first commit of this project's day 0 was
      the brief, alone
