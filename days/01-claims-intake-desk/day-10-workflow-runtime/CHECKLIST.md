# P01 day 10 — definition of done

`python p.py done 01 10` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-order-as-object/1.1-order-as-an-object.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/01-order-as-object/1.2-state-between-nodes.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/02-the-loop/2.1-draft-objection-draft.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/02-the-loop/2.2-the-bound.md` — read · ran its check · answered its question out loud
- [ ] `parts/03-cost-and-successor/3.1-queue-at-once.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/03-cost-and-successor/3.2-runtime-that-replaces-this-one.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/04-holding-it/4.1-what-the-tests-hold.md` — read · ran its check · answered its
      question out loud

## Build

- [ ] `claims_desk/workflow.py` — the three arrangements, the two code nodes, `stages`,
      `model_nodes`, `charge`, and the two `run_` functions
- [ ] Ran `stages()` on `triage` and `correspondence` **before** wiring anything to them
- [ ] `claims_desk/agents/classifier.py` — the marked diff: `output_key`, four imports gone,
      `classify` deleted
- [ ] `claims_desk/agents/letter_writer.py` — the marked diff: `write` deleted, `build` untouched
- [ ] `claims_desk/sessions.py` — the marked diff: `BaseAgent`, `max_calls`, `RunConfig`
- [ ] `claims_desk/desk.py` — the marked diff: the ceiling at 5, `run_triage`, `write_letter`
- [ ] `claims_desk/scripted.py` — the first draft that names a figure, and the double that reads the
      objection out of its own system instruction
- [ ] `tests/test_workflow.py` — fifteen functions, sixteen tests
- [ ] `tests/test_sessions.py`, `tests/test_agent.py`, `tests/test_cast.py` — the marked diffs,
      written **after** the gate told you which twenty tests were red
- [ ] `claims_desk/workflow.py` — `TODO(me)`: the loop as a `Workflow` graph, starting from part
      3.2's exact command
- [ ] `claims_desk/workflow.py` — `TODO(me)`: what a streaming provider does to `charge`
- [ ] `claims_desk/workflow.py` — `TODO(me)`: the `asyncio.gather` version of the queue, and which
      you would ship
- [ ] `tests/test_workflow.py` — `TODO(me)`: rewrite the bound test so it swaps only the model
- [ ] Your own notes — `TODO(me)`: re-check the deprecation's second sentence in your own version

## Check

- [ ] The day's check is green: `./run check` — `All checks passed!`, `110 passed`, four `ok` lines
- [ ] Printed the stages of both workflows and named which node costs money
- [ ] Ran the loop on `FNOL-4477` and `FNOL-4480` and saw `drafts: 1` and `drafts: 2`
- [ ] Read the second draft and confirmed the figure is gone and the point is not
- [ ] Ran the letter loop with `Budget(limit=1)` and read
      `LlmCallsLimitExceededError: Max number of llm calls limit of \`1\` exceeded`
- [ ] Ran the parallel queue and saw `distinct perils: ['escape-of-water']` for twelve different
      claims
- [ ] **Break it on purpose, watch it go red, fix it.** Remove the namespacing from `morning()` —
      let every branch write `outcome`, `reason` and `reading`. Read the twelve correct
      `workflow.rules` log lines, then read the one verdict the session ends up holding, and say out
      loud how you would have found this in production. Put it back.
- [ ] Removed `max_iterations` from `correspondence()`, saw exactly one test fail, and said out loud
      why the tests that run the loop stayed green
- [ ] Removed `escalate=accepted` and counted the drafts
- [ ] Ran the successor `Workflow` from part 3.2 and saw the two events
- [ ] Found the deprecation warning in your own `./run check` output
- [ ] `python p.py depth 01 10` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path — and the eight changes
      to earlier files are marked diffs naming the day of THIS project that printed each original
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own earlier days
- [ ] No state key holds anything personal; day 8's `check_state` still refuses by name

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the eight rows
      in the hub §10, the restated definition included
- [ ] `docs/adr/ADR-0010-p01-stays-on-the-composition-workflow-agents.md` is read and understood —
      the decision it records is the one part 3.2 argues
- [ ] No `docs/PINS.md` row is owed — nothing was installed today
- [ ] No `docs/SOURCES.md` row is owed — nothing with a citation identifier was cited
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
