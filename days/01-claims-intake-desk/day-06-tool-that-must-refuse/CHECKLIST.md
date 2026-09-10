# P01 day 6 — definition of done

`python p.py done 01 6` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-an-answer/1.1-four-decided-eight-pending.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/01-an-answer/1.2-tool-that-will-not-write-the-letter.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/02-the-queue/2.1-twelve-in-one-command.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/03-holding-it/3.1-what-the-tests-hold.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/03-holding-it/3.2-refusal-nobody-read.md` — read · ran its check · answered its
      question out loud

## Build

- [ ] `claims_desk/desk.py` — `Verdict`, the four rules, `decide`, `run_queue` with the refusal check
- [ ] `claims_mcp/tools.py` — `WHAT_IS_NEEDED`, `draft_letter`, and `draft_letter` in `DECLARED`
- [ ] `claims_mcp/server.py` — `version="0.4.0"`
- [ ] `claims_desk/__main__.py` — the entry point
- [ ] `run` — `desk` added to `COMMANDS` and to the docstring
- [ ] `tests/test_desk.py` — eleven tests, with the in-process fixture
- [ ] `tests/test_boundary.py` and `tests/test_tools.py` — the two assertions updated **after** the
      gate told you to
- [ ] `claims_desk/desk.py` — `TODO(me)`: what breaks if the rule order diverges from day 2's
- [ ] `claims_desk/desk.py` — `TODO(me)`: where a pending notification goes, and running twice
- [ ] `.gitignore` — `TODO(me)`: is a claim file an output or a fixture?
- [ ] `claims_desk/__main__.py` — `TODO(me)`: the exit rule you would want
- [ ] `claims_mcp/tools.py` — `TODO(me)`: the three entries that ask for nothing

## Check

- [ ] The day's check is green: `./run check` — `All checks passed!`, `56 passed`, four `ok` lines
- [ ] `./run desk` run at least once end to end, over a real subprocess boundary, and the time it
      took noted
- [ ] **Break it on purpose, watch it go red, fix it.** Replace `verdict.reason` in the
      `record_decision` call with `"no_date"` and run the desk. Expect
      `RuntimeError: boundary refused to record FNOL-4473: unknown reason 'no_date'`.
- [ ] **The break that goes green.** Now also remove the `if not written.get("recorded")` check and
      run it again. Expect `{"deficiency": 4, ...}` with an **empty** claims directory and no error
      anywhere. Put both back and say out loud what the summary was claiming.
- [ ] Deleted an entry from `WHAT_IS_NEEDED` and watched the totality test name the reason code
- [ ] `python p.py depth 01 6` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path — and the three changes
      to earlier files are marked diffs naming the day of THIS project that printed each original
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own earlier days
- [ ] `claims_desk/desk.py` opens no file; every fact it uses about a policy came over the boundary

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the four rows in
      the hub §10
- [ ] No `docs/PINS.md` row is owed — nothing was installed today
- [ ] No `docs/SOURCES.md` row is owed — nothing with a citation identifier was cited
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
