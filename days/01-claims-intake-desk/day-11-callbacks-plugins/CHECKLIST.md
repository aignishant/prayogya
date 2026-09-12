# P01 day 11 — definition of done

`python p.py done 01 11` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-around-every-call/1.1-plugin-that-sees-every-agent.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/01-around-every-call/1.2-where-the-budget-belongs.md` — read · ran its check · answered
      its question out loud
- [ ] `parts/01-around-every-call/1.3-three-agents-deep.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/02-one-agents-rule/2.1-second-lock.md` — read · ran its check · answered its question
      out loud
- [ ] `parts/03-what-it-must-not-do/3.1-exception-that-never-arrives.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/04-holding-it/4.1-what-the-tests-hold.md` — read · ran its check · answered its
      question out loud

## Build

- [ ] `claims_desk/hooks.py` — the two context variables, `DeskPlugin` with its five hooks, and
      `refuse_the_description`
- [ ] `claims_desk/sessions.py` — the marked diff: `plugins=[DeskPlugin()]` on the runner
- [ ] `claims_desk/workflow.py` — the marked diff: `charge` deleted, the budget registered in a
      `try`/`finally`, `OVER_BUDGET`, and `turned_away` in the return
- [ ] `claims_desk/desk.py` — the marked diff: the `except BudgetExceeded` replaced by a check on
      the returned value
- [ ] `claims_desk/workflow.py` — the marked diff: `before_model_callback` on the loop's writer and
      the forbidden phrase in state
- [ ] `tests/test_hooks.py` — thirteen tests, with the `budgeted` fixture
- [ ] `tests/test_cast.py` and `tests/test_workflow.py` — the two assertions updated **after** the
      gate told you they were red
- [ ] `claims_desk/hooks.py` — `TODO(me)`: the version that ends the loop on a refused leak
- [ ] `claims_desk/hooks.py` — `TODO(me)`: the claim reference in the plugin's lines
- [ ] `claims_desk/hooks.py` — `TODO(me)`: three ways a description slips past a substring check
- [ ] `claims_desk/util/logging.py` — `TODO(me)`: the allow-list logger
- [ ] `tests/conftest.py` — `TODO(me)`: the `_in_process` fixture, now duplicated five times

## Check

- [ ] The day's check is green: `./run check` — `All checks passed!`, `124 passed`, four `ok` lines
- [ ] Ran one turn with a budget registered and read the `hooks.model` line
- [ ] Ran the same turn with no budget registered and confirmed it still works
- [ ] Ran a claim with `Budget(limit=0)` and read `waiting_for='over_budget'`
- [ ] Ran one claim's decision and letter together and grouped the log lines by `invocation`
- [ ] Tripped the leak guard on purpose and read `spent: 3` — then said out loud why three
- [ ] **Break it on purpose, watch it go red, fix it.** Make the plugin `raise refused` instead of
      returning a refusal. Read
      `RuntimeError: Error in plugin 'claims-desk' during 'before_model_callback' callback: ...`,
      confirm `except BudgetExceeded` no longer fires, and note that only two tests object and
      neither is the desk's dead branch. Put it back.
- [ ] Logged the response text instead of its length, watched exactly one test go red, and put it
      back
- [ ] Returned a response from `on_model_error_callback` and watched the outage become an answer
- [ ] `python p.py depth 01 11` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path — and the changes to
      earlier files are marked diffs naming the day of THIS project that printed each original
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own earlier days
- [ ] Nothing the plugin writes contains what a model said, and nothing the leak guard writes
      contains the phrase it refused

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the six rows in
      the hub §10
- [ ] No `docs/PINS.md` row is owed — nothing was installed today
- [ ] No `docs/SOURCES.md` row is owed — nothing with a citation identifier was cited
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
