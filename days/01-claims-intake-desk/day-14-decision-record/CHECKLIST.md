# P01 day 14 — definition of done

`python p.py done 01 14` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-what-a-record-is/1.1-facts-a-rule-reads.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/01-what-a-record-is/1.2-provenance-and-citation.md` — read · ran its check · answered
      its question out loud
- [ ] `parts/02-does-it-replay/2.1-replay-and-what-it-cannot-prove.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/03-holding-it/3.1-what-the-tests-hold.md` — read · ran its check · answered its question
      out loud

## Build

- [ ] `claims_desk/record.py` — `Facts`, `Provenance`, `DecisionRecord`, `facts_from`, `replay`,
      `defensible`, `which_rule`, `as_stored`, `CITES`, `cites`, `peril_is_known`
- [ ] Replayed a hand-built record **before** wiring anything into the desk
- [ ] `claims_desk/workflow.py` — `run_triage` returns the facts it decided on
- [ ] `claims_desk/desk.py` — `Verdict.record`, `built` for the early-exit path, and the record
      passed to the boundary
- [ ] `claims_mcp/tools.py` — `decision_record`, and the refusal for a record filed against the
      wrong claim
- [ ] `claims_desk/boundary.py` — the wrapper carries it across
- [ ] `tests/test_desk.py` — the `record_decision` stub updated **after** the gate told you
- [ ] `tests/test_record.py` — eighteen functions, twenty-four tests
- [ ] `tests/test_record.py` — `TODO(me)`: a checked-in fixture of records, replayed on every run
- [ ] `claims_desk/record.py` — `TODO(me)`: the test that fails when `assess` moves and the version
      does not
- [ ] `claims_desk/record.py` — `TODO(me)`: what a hash over the stored record would cost, and who
      would hold it
- [ ] `claims_desk/desk.py` — `TODO(me)`: `calls` under-reports the letter's drafts
- [ ] Your own notes — `TODO(me)`: which copy of the letter is authoritative

## Check

- [ ] The day's check is green: `./run check` — `All checks passed!`, `181 passed`, four `ok` lines
- [ ] Printed one record whole and named the rule in `assess` that reads each of its eleven facts
- [ ] Printed the record for a claim no model read, and said why three of its fields are empty
- [ ] Replayed all twelve records and confirmed every one is defensible
- [ ] Edited a stored verdict, watched `defensible` go false, and read what the facts actually produce
- [ ] Edited a stored **fact**, watched it go false in the other direction
- [ ] Edited **both** consistently and watched `defensible` stay true — then said out loud what that
      means the replay is worth
- [ ] **Break it on purpose, watch it go red, fix it.** With records already on disk, take `fire` out
      of `PHOTO_REQUIRED_FOR`. One record stops being defensible and one test goes red. Then put that
      back and instead **swap two checks in `assess`** — predict what fails before you run it, and
      then explain why nothing does. Put both back.
- [ ] Added a field to `Facts` that no rule reads, and read the failure
- [ ] `python p.py depth 01 14` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path — and the four changes to
      earlier files are additions, each named in the hub §4
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own earlier days
- [ ] No record holds the policyholder's description, and no record holds a summary of anything
- [ ] Every citation in `CITES` resolves to a section of `data/handbook.md`

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the six rows in
      the hub §10
- [ ] No `docs/PINS.md` row is owed — nothing was installed today
- [ ] No `docs/SOURCES.md` row is owed — nothing with a citation identifier was cited
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
