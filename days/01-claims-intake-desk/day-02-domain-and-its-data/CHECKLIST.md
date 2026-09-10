# P01 day 2 — definition of done

`python p.py done 01 2` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-the-record/1.1-every-byte-invented.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/01-the-record/1.2-call-as-it-was-taken-down.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/02-shape-in-code/2.1-record-as-a-type.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/02-shape-in-code/2.2-only-code-that-opens-a-file.md` — read · ran its check · answered
      its question out loud
- [ ] `parts/03-the-contract/3.1-twelve-four-and-eight.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/03-the-contract/3.2-word-the-scan-cannot-read.md` — read · ran its check · answered
      its question out loud

## Build

- [ ] `data/policies.json` — eight policies, the `_synthetic` line first, one `lapsed` and one
      `cancelled`
- [ ] `data/notifications.json` — twelve notifications, four fast-track, eight distinct deficiency
      reasons, every `expected` block written by hand
- [ ] `claims_desk/domain.py` — the two frozen records, the two enumerations, the eight ordered
      checks, and the stand-in named as one
- [ ] `claims_desk/store.py` — the only code in the project that opens a file
- [ ] `tests/test_domain.py` — ten tests, including the inverted one
- [ ] `claims_desk/domain.py` — `TODO(me)`: write the all-reasons version of `assess`, then argue
      yourself out of it in three sentences
- [ ] `claims_desk/store.py` — `TODO(me)`: measure the repeated parse over twelve notifications,
      write the number down, and change nothing
- [ ] `tests/test_domain.py` — `TODO(me)`: every `policy_number` either exists or is the one
      deliberate unknown
- [ ] `tests/test_domain.py` — `TODO(me)`: prove the temporary file is gone when the write **fails**
- [ ] Your own notes — `TODO(me)`: what a real desk would do about a caller-supplied estimate

## Check

- [ ] The day's check is green: `./run check` — `All checks passed!`, `19 passed`, four `ok` lines
- [ ] **Break it on purpose, watch it go red, fix it.** Change `assess` to call
      `mentions_injury_keyword_scan(notification.description)` instead of taking `injury_reported`.
      Expect `AssertionError: FNOL-4471`, `fast-track` against `deficiency`. Read the description
      before you fix it, and say out loud why a longer word list is not the fix.
- [ ] Ran the scan against all twelve and saw exactly one disagreement
- [ ] Dropped a leading zero in a fixture date and saw `Invalid isoformat string` rather than a
      wrong answer
- [ ] `python p.py depth 01 2` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path — no `...`, no
      "the rest is unchanged" without naming the day of THIS project that printed the original
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own earlier days
- [ ] **All data is synthetic**, and both fixture files say so in their own first line

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the seven rows
      in the hub §10, restated definitions included
- [ ] No `docs/PINS.md` row is owed — nothing was installed today
- [ ] No `docs/SOURCES.md` row is owed — nothing with a citation identifier was cited
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
