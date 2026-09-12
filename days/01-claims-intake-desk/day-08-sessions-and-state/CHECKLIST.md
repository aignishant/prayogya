# P01 day 8 — definition of done

`python p.py done 01 8` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-the-conversation/1.1-one-conversation-per-claim.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/01-the-conversation/1.2-what-a-session-must-never-hold.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/02-the-run/2.1-two-events-one-yielded.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/03-holding-it/3.1-what-the-tests-hold.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/03-holding-it/3.2-failure-that-did-both.md` — read · ran its check · answered its
      question out loud

## Build

- [ ] `claims_desk/sessions.py` — the address, the one service, `check_state`, `turn`, `stored`
- [ ] `claims_desk/agents/classifier.py` — the marked diff: sixteen lines of runner machinery gone,
      `claim_id` as the first argument
- [ ] `claims_desk/desk.py` — the one call site updated
- [ ] `tests/test_sessions.py` — twelve tests, with the `_fresh_sessions` fixture
- [ ] `tests/test_agent.py` — five call sites updated **after** the gate told you to
- [ ] `claims_desk/sessions.py` — `TODO(me)`: the allow-list version, and what it costs
- [ ] `claims_desk/sessions.py` — `TODO(me)`: the service passed in rather than global; run both
- [ ] `claims_desk/sessions.py` — `TODO(me)`: three questions this desk cannot answer about
      yesterday's batch
- [ ] `claims_desk/agents/classifier.py` — `TODO(me)`: what would change if it saw a previous turn
- [ ] Your own notes — `TODO(me)`: the stand-in never streams; add it to day 7's list

## Check

- [ ] The day's check is green: `./run check` — `All checks passed!`, `78 passed`, four `ok` lines
- [ ] Asked twice about one claim and watched the session go from 2 events to 4
- [ ] Asked about a claim nobody had asked about and got `None` rather than an empty session
- [ ] Ran the same lookup in two processes and watched the second find nothing
- [ ] **Break it on purpose, watch it go red, fix it.** Remove `and event.content` from the loop in
      `sessions.turn`. Every test still passes. Then run a turn against a failing stand-in and read
      `AttributeError: 'NoneType' object has no attribute 'parts'` — and say out loud what a person
      debugging that would look at first. Put it back.
- [ ] Disabled the `_fresh_sessions` fixture, saw `assert 4 == 2`, then ran that same test alone
      with `-k` and saw it pass
- [ ] Tried `check_state({"caller_ref": ...})` and `check_state({"notes": ...})` and confirmed both
      are allowed
- [ ] `python p.py depth 01 8` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path — and the two changes to
      earlier files are marked diffs naming the day of THIS project that printed each original
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own earlier days
- [ ] Session state carries a reference and no contents; nothing personal and no secret is in it

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the eight rows
      in the hub §10, restated definitions included
- [ ] No `docs/PINS.md` row is owed — nothing was installed today
- [ ] No `docs/SOURCES.md` row is owed — nothing with a citation identifier was cited
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
