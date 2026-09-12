# P01 day 18 — definition of done

`python p.py done 01 18` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-the-set/1.1-set-with-a-declared-answer.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/01-the-set/1.2-trajectory-not-just-the-answer.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/02-the-marking/2.1-judge-and-its-rubric.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/02-the-marking/2.2-baseline-that-makes-a-score-mean-something.md` — read · ran its
      check · answered its question out loud
- [ ] `parts/03-the-gate/3.1-gate-that-goes-red.md` — read · ran its check · answered its question
      out loud
- [ ] `parts/03-the-gate/3.2-what-the-framework-ships.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/04-holding-it/4.1-what-the-tests-hold.md` — read · ran its check · answered its question
      out loud

## Build

- [ ] `claims_desk/evals.py` — `DESK`, `SETTLED_BY_FIELDS`, `BEFORE_IN_FORCE`, `RUBRIC`, `Mark`,
      `CaseResult`, `run_desk`, `records`, `by_claim`, `expected_tools`, `expected_calls`, `judge`,
      `mark`, `evaluate`, `baseline`, `report`, `main`
- [ ] `run` — the marked diff: `eval` moves from `PLANNED` to `COMMANDS`
- [ ] **Ran `./run eval` before reading part 1.2's failure section**, and read what your own first
      marking scheme said
- [ ] `uv add "google-adk[eval]==2.8.0"` — and confirmed `mcp 2.2.0` and `rouge-score 0.1.2` after it
- [ ] `pyproject.toml` — the one-line marked diff the install made
- [ ] `.gitignore` — the marked diff: `.adk/`
- [ ] `claims_desk/evalset/__init__.py` and `claims_desk/evalset/agent.py` — `root_agent`, and the
      `as agent` re-export
- [ ] `data/evalset/classifier.evalset.json` — twelve cases, `intermediate_data.tool_uses` empty on
      every one
- [ ] `data/evalset/test_config.json` — the two local metrics at the framework's defaults
- [ ] `tests/test_evals.py` — thirty-three tests, and `the_desk_marked` reads `tools.store`
- [ ] `claims_desk/evals.py` — `TODO(me)`: the mark comparing `desk.decided` with the claim file's
      `outcome`
- [ ] `claims_desk/evals.py` — `TODO(me)`: the overlap assertion in `by_claim`
- [ ] `claims_desk/evals.py` — `TODO(me)`: the smarter baseline, and what the two numbers did
- [ ] `claims_desk/evals.py` — `TODO(me)`: the lenient route mark, the desk that records before it
      drafts, and the strict mark put back
- [ ] `claims_desk/evals.py` and `tests/test_evals.py` — `TODO(me)`: `desk.letter_failed` beside
      four letter crosses, with its test
- [ ] Your own notes — `TODO(me)`: the fifth rubric row as a model judge, with the call left as a
      `TODO(me)` naming the key
- [ ] `data/evalset/classifier.evalset.json` — `TODO(me)`: bare or quarantined descriptions, decided
      and written into the file's `description`
- [ ] Your own notes — `TODO(me)`: the field-equality custom metric, written and not run
- [ ] Your own notes — `TODO(me)`: whether `NUM_RUNS = 2` doubles the classifier's bill, counted
      from `hooks.model` lines

## Check

- [ ] The fast gate is green: `./run check` — `All checks passed!`, `283 passed` (or `280`, hub §3),
      four `ok` lines
- [ ] The slow gate is green: `./run eval` — twelve `ok`, `desk     12/12`, `eval: green`, `OK eval`
- [ ] Counted the marks per claim yourself — 5, 5, 8, 8, 5, 8, 9, 9, 9, 5, 5, 8 — and said why each
      number is what it is
- [ ] Ran the eight-letter rubric table and read thirty-two ticks
- [ ] Ran the baseline detail and named the three claims the model earns and the three it is right
      about for the wrong reason
- [ ] Ran the text-judge measurement and read `0.889`, `0.889`, `0.625`
- [ ] Ran `adk eval` from the project root once without `PYTHONPATH=.` and once with, and found the
      `.adk/` folder it wrote
- [ ] **Break it on purpose, watch it go red, fix it.** Disable the in-force check and read ten
      `RED` lines, one on its verdict. Give the photograph letter `within 14 days` and read `calls:
      expected 2, got 4`. Rewrite `expected_calls` in three branches and read four `expected 0, got
      1`. Change FNOL-4474's answer in the key and read four marks. Put all four back.
- [ ] **The failure that is green.** Loosen the route mark to a subset check, confirm the in-force
      edit still goes red, and say what no longer does. Put it back.
- [ ] **The audit misread.** Put `Store().claim` back in `the_desk_marked`, empty `data/claims/`,
      run the file, and read seven claims failing every letter row. Put it back.
- [ ] Raised `response_match_score`'s threshold to 0.9 and watched the *correct* answer fail. Put it
      back.
- [ ] `python p.py depth 01 18` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path — and the changes to
      earlier files are marked diffs naming the day of THIS project that printed each original
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own earlier days
- [ ] No number in any part is quoted from this document rather than from your own run — the
      baseline, the marks, the judge's scores, the fifty-two packages
- [ ] Nothing added today changes what the desk decides — twelve claims, four fast-tracked, seven
      recorded, one held, exactly as day 17 left them
- [ ] The audit imports `claims_desk.domain` and `claims_desk.store` and nothing else from this
      desk — and the desk imports nothing from `claims_desk.evals`

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the nine rows
      in the hub §10, three of them re-anchoring terms the archive defined
- [ ] The project's `PACKAGES.md` has the two rows from the hub §10, dated
- [ ] No `docs/PINS.md` row is owed — the extra is a project pin
- [ ] No `docs/SOURCES.md` row is owed — nothing with a citation identifier was cited
- [ ] Noted honestly that the marking scheme was wrong twice today, and said what found it each time
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block, with
      the note under the table about the debts the rebuild found in days 11, 13, 14, 15 and 17
- [ ] Committed with the message from the hub §10
