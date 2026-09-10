# P01 day 5 — definition of done

`python p.py done 01 5` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-the-docket/1.1-description-is-the-api.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/01-the-docket/1.2-wiring-now-there-are-four.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/02-a-parameter/2.1-parameter-that-is-not-a-string.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/03-the-answer/3.1-two-copies-of-every-answer.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/03-the-answer/3.2-tool-that-returns-nothing-honestly.md` — read · ran its check ·
      answered its question out loud

## Build

- [ ] `claims_mcp/tools.py` — four functions, the `store`, and `DECLARED` at the bottom
- [ ] `claims_mcp/server.py` — wiring only: the server, the registration loop, the resource, the
      prompt, and `version="0.3.0"`
- [ ] `tests/test_tools.py` — fourteen tests from ten functions, with the autouse isolation fixture
- [ ] `tests/test_boundary.py` — the docket assertion removed, the identity test renamed, the
      version updated **after** the gate told you to
- [ ] `claims_mcp/tools.py` — `TODO(me)`: refuse a date of loss in the future, as data
- [ ] `claims_mcp/tools.py` — `TODO(me)`: decide about `annotations=` on the tool that writes
- [ ] `claims_mcp/server.py` — `TODO(me)`: the log lines the split dropped
- [ ] `tests/test_tools.py` — `TODO(me)`: make the two-copies assertion actually fail once
- [ ] `tests/test_tools.py` — `TODO(me)`: a bad description that passes the first-line check

## Check

- [ ] The day's check is green: `./run check` — `All checks passed!`, `45 passed`, four `ok` lines
- [ ] **Break it on purpose, watch it go red, fix it.** Change `read_decision` to raise
      `KeyError(f"no decision recorded for {claim_id}")`. Call it through a client and confirm you
      get `Error executing tool read_decision` with `structured_content` of `None` — the exception's
      own message is gone. Run `./run check` and see the single test that objects. Put it back.
- [ ] Shortened a description to two words, read the docket, and watched one test go red
- [ ] Sent `'2026-3-14'` as a date of loss and compared the refusal with day 2 part 1.1, where the
      same string produced a wrong answer and no error
- [ ] Added a function to `tools.py` without adding it to `DECLARED` and confirmed `Unknown tool`
- [ ] `python p.py depth 01 5` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path — and the change to
      `tests/test_boundary.py` is a marked diff naming the day of THIS project that printed it
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own earlier days
- [ ] The tools validate against `claims_desk.domain`'s own enumerations rather than a second list

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the eight rows
      in the hub §10, restated definitions included
- [ ] No `docs/PINS.md` row is owed — nothing was installed today
- [ ] No `docs/SOURCES.md` row is owed — nothing with a citation identifier was cited
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
