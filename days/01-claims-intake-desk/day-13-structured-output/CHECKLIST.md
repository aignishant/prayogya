# P01 day 13 — definition of done

`python p.py done 01 13` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-shape-on-the-way-out/1.1-shape-is-a-value.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/01-shape-on-the-way-out/1.2-validator-that-refuses-a-guess.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/02-when-it-changes/2.1-field-that-appeared-on-tuesday.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/03-holding-it/3.1-what-the-tests-hold.md` — read · ran its check · answered its question
      out loud

## Build

- [ ] `claims_desk/domain.py` — the marked diff: `Peril` as a `StrEnum`, and `PHOTO_REQUIRED_FOR`
      naming its members from it
- [ ] `claims_desk/schemas.py` — `Reading`, with `extra="forbid"`, `use_enum_values=True` and a
      description on every field
- [ ] `claims_desk/agents/classifier.py` — the marked diff: the f-string prompt, the generated peril
      sentence, and `output_schema=Reading`
- [ ] Printed `Reading.model_json_schema()` and read what actually crosses to a provider
- [ ] `claims_desk/workflow.py` — the marked diff: `parse_reading` down to four lines, and the `json`
      import gone
- [ ] `claims_desk/workflow.py` — the marked diff: `REFUSED_SHAPE` and the `except ValidationError`,
      added **after** watching an unreadable description stop the queue
- [ ] `tests/test_schemas.py` — thirteen tests, no fixture, no runner
- [ ] `tests/test_agent.py` and `tests/test_workflow.py` — the six assertions updated **after** the
      gate told you which
- [ ] `claims_desk/workflow.py` — `TODO(me)`: give `refused_shape` its own `waiting_for`
- [ ] `claims_desk/schemas.py` — `TODO(me)`: the refused answer onto the claim's record, not the log
- [ ] `claims_desk/domain.py` — `TODO(me)`: type the store's side of `Cover.perils`
- [ ] `claims_desk/schemas.py` — `TODO(me)`: `Peril`'s docstring out of the schema, with the saving
      measured
- [ ] Your own notes — `TODO(me)`: how you would narrow the `ValidationError` catch

## Check

- [ ] The day's check is green: `./run check` — `All checks passed!`, `157 passed`, four `ok` lines
- [ ] Ran a triage and confirmed state holds a **dict**, not a string
- [ ] Fed the schema three wrong answers and read the field and error type for each
- [ ] Ran the unreadable description and read `workflow.refused_shape` in the log
- [ ] Ran the three evolution tests and said out loud which direction each one is about
- [ ] **Break it on purpose, watch it go red, fix it.** Remove the `except ValidationError` from
      `run_triage`, then run the whole queue with one notification whose description the stand-in
      cannot read. Nothing in the suite goes red and the queue stops. Say out loud how many of the
      remaining claims were decided. Put it back.
- [ ] Added a peril to one policy in `data/policies.json`, saw one test name it, and put it back
- [ ] Dropped `use_enum_values=True` and watched how many tests it takes down
- [ ] Removed a doubled brace from `INSTRUCTION` and read the import-time `ValueError`
- [ ] `python p.py depth 01 13` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path — and the three changes to
      earlier files are marked diffs naming the day of THIS project that printed each original
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own earlier days
- [ ] No log line and no exception message carries `input_value` — the field and the error type only

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the six rows in
      the hub §10
- [ ] No `docs/PINS.md` row is owed — pydantic arrived with `google-adk` on day 7
- [ ] No `docs/SOURCES.md` row is owed — nothing with a citation identifier was cited
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
