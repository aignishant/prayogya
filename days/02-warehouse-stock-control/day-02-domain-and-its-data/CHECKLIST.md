# P02 day 2 — definition of done

`python p.py done 02 2` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-the-record/1.1-every-unit-of-this-is-invented.md` — read · ran its check · answered
      its question out loud
- [ ] `parts/01-the-record/1.2-the-count-as-it-was-called-in.md` — read · ran its check · answered
      its question out loud
- [ ] `parts/02-shape-in-code/2.1-the-record-as-a-type.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/02-shape-in-code/2.2-only-code-that-opens-a-file.md` — read · ran its check · answered
      its question out loud
- [ ] `parts/03-the-contract/3.1-sixty-fifty-one-and-nine.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/03-the-contract/3.2-the-word-the-scan-cannot-read.md` — read · ran its check ·
      answered its question out loud

## Build

- [ ] `data/ledger.json` — sixty bins, three aisles, `_synthetic` as the first key
- [ ] `data/counts.json` — sixty counts, fifty-one matched, nine carrying a note and an `expected`
      block
- [ ] `stock_desk/domain.py` — `Outcome`, `Reason`, `Bin`, `Count`, `reconcile`,
      `guess_reason_from_note`
- [ ] `stock_desk/store.py` — `bins`, `bin`, `counts`, `expectations`, `write_reconciliation`,
      `reconciliation`
- [ ] `tests/test_domain.py` — seven tests, all reading the fixtures and the rules, none calling a
      model
- [ ] `stock_desk/domain.py` — `TODO(me)`: why `Outcome.OVER_COUNTED` exists though nothing reaches
      it
- [ ] `stock_desk/domain.py` — `TODO(me)`: a fourth word for one of the three lists that would not
      break any of the other eight notes, and why "safer today" is not "safe"
- [ ] `stock_desk/store.py` — `TODO(me)`: whether `write_reconciliation` needs to fsync the
      directory too, and why

## Check

- [ ] The day's check is green: `./run check` — `All checks passed!`, `24 passed`, five `ok` lines
- [ ] Ran `uv run pytest -q tests/test_domain.py -v` and read all seven test names
- [ ] Ran the classification table in part 3.2 and confirmed exactly one `WRONG` line, on `A-10-2`
- [ ] **Break it on purpose, watch it go red, fix it.** Reorder the checks in `reconcile`. Delete
      one planted variance. Widen `RECEIPT_WORDS` to catch A-10-2 and watch the inverted-case test
      fail on `C-05-1` instead. Put every one back.
- [ ] **The failure that stays quiet.** After the word-list widening, run only the test you were
      aiming to fix — it is red. Run the whole suite and confirm it is the only thing that tells you
      a different note broke.
- [ ] `python p.py depth 02 2` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own days 0 and 1
- [ ] No number in any part is quoted from this document rather than from your own run — the
      bin count, the variance count, the classification table
- [ ] Nothing in `domain.py` or `store.py` calls a model, opens a network connection, or reads
      `expectations()`

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the six rows
      in the hub §10
- [ ] No `docs/PINS.md` row is owed — nothing was installed today
- [ ] No `docs/SOURCES.md` row is owed — nothing with a citation identifier was cited
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
