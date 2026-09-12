# P01 day 9 — definition of done

`python p.py done 01 9` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-two-agents/1.1-second-specialist.md` — read · ran its check · answered its question
      out loud
- [ ] `parts/01-two-agents/1.2-letters-it-writes.md` — read · ran its check · answered its question
      out loud
- [ ] `parts/02-delegation/2.1-transfer-and-why-not.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/03-holding-it/3.1-what-a-session-shares.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/03-holding-it/3.2-bill-for-two.md` — read · ran its check · answered its question out
      loud
- [ ] `parts/03-holding-it/3.3-what-the-tests-hold.md` — read · ran its check · answered its
      question out loud

## Build

- [ ] `claims_desk/agents/letter_writer.py` — the instruction, `build`, and `write` asking the
      boundary before spending the budget
- [ ] `claims_desk/scripted.py` — the marked diff: `LETTERS`, the eight of them, and
      `ScriptedLetterWriter` with its own model name
- [ ] `claims_mcp/tools.py` — the marked diff: `record_decision` gains `letter`, the new refusal,
      and the version at `0.5.0`
- [ ] `tests/test_transports.py` — the version assertion updated **after** the gate told you to
- [ ] `tests/test_desk.py` — the `record_decision` stub given its `letter` parameter, likewise
- [ ] `claims_desk/desk.py` — the marked diff: the ceiling at 3, the letter written for a
      deficiency, and the letter passed to `record_decision`
- [ ] `claims_desk/sessions.py` — the marked diff: `thread` on `address`, `turn` and `stored`
- [ ] `claims_desk/agents/letter_writer.py` — `thread=NAME` on the turn, added **after** you have
      reproduced part 3.1's leak
- [ ] `tests/test_cast.py` — eleven functions, eighteen tests
- [ ] `claims_desk/agents/letter_writer.py` — `TODO(me)`: keep the duplicated rules or delete one
      copy, and what you would check first
- [ ] `claims_desk/scripted.py` — `TODO(me)`: the letters are hand-written; add the line to day 7's
      list of what this project cannot measure
- [ ] `claims_desk/sessions.py` — `TODO(me)`: the version where a thread is derived from the agent
      rather than passed
- [ ] `claims_desk/desk.py` — `TODO(me)`: the argument for refusing to record a deficiency with no
      letter
- [ ] Your own notes — `TODO(me)`: the two numbers you would need before choosing delegation

## Check

- [ ] The day's check is green: `./run check` — `All checks passed!`, `96 passed`, four `ok` lines
- [ ] Asked for one letter and read it: three sentences, the claim reference, and no figure
- [ ] Asked for a letter about `no_photo` and confirmed `budget spent: 0`
- [ ] Ran the transfer demonstration and named which of the three events is the decision, which the
      handover, and which the work
- [ ] Ran the spy with `thread=''` and counted **four** blocks, then with `thread='letter_writer'`
      and counted one
- [ ] **Break it on purpose, watch it go red, fix it.** Delete `thread=NAME` from
      `letter_writer.write`. Exactly one test goes red. Run the spy again and read the
      policyholder's own words in the letter writer's input, then find
      `Event from an unknown agent: classifier` in the output and say out loud why nobody would act
      on it. Put it back.
- [ ] Gave the letter writer its own `Budget(limit=CALLS_PER_NOTIFICATION)` and watched
      `test_a_deficiency_costs_two_calls_across_the_cast` fail on the breakdown rather than the
      total
- [ ] Ran the queue and confirmed `claim files: 12 | with a letter: 8`, with every letter on a
      deficiency
- [ ] `python p.py depth 01 9` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path — and the four changes
      to earlier files are marked diffs naming the day of THIS project that printed each original
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own earlier days
- [ ] No letter contains a policy number, an excess, an estimate or anything the policyholder said

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the five rows in
      the hub §10, the restated definition included
- [ ] No `docs/PINS.md` row is owed — nothing was installed today
- [ ] No `docs/SOURCES.md` row is owed — nothing with a citation identifier was cited
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
