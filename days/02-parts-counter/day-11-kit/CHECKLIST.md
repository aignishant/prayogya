# Day 11 — definition of done

`python p.py done 11` refuses to commit while any box below is unticked. That refusal is the point:
a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-what-a-project-owes-itself/1.1-the-four-hundred-lines-you-type-again.md` — read · ran its check · answered its question out loud
- [ ] `parts/01-what-a-project-owes-itself/1.2-the-two-you-have-met-before.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-the-two-that-are-new/2.1-a-budget-that-refuses.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-the-two-that-are-new/2.2-redaction-at-the-writer.md` — read · ran its check · answered its question out loud

## Build

- [ ] The scaffold from hub §3 exists: `pyproject.toml` with both pins exact, `.python-version`, `.gitignore`, `.env.example`, the two empty `__init__.py` files, and the four project documents
- [ ] I can say why `pytest` is in `[dependency-groups] dev` rather than in `dependencies`, and what would be wrong with the other placement
- [ ] `parts_counter/util/models.py` — typed, and I checked the date in `PINNED` against this project's `PACKAGES.md` model row **before** accepting it
- [ ] I can say what would have to be true for this project's model ID matching P01's to be a *shared setting* rather than a coincidence, and name every file I would have to find
- [ ] `parts_counter/util/keys.py` — typed, at `parts_counter/util/`, and I can say which `PRIMER.md` section its docstring should name in **this** project and why the wrong number got there
- [ ] `parts_counter/util/budget.py` — typed, and I predicted `spent_this_turn` after a refusal **before** running it, for both orderings of the check and the increment
- [ ] I found the day `CODEMAP.md` owes `parts_counter/agent.py` to, and I can say what would have to be written there to make `budget.py`'s docstring true
- [ ] `parts_counter/util/logging.py` — typed, and I named a field that would carry a credential past all six entries in `SECRET_NAMES`
- [ ] `tests/test_kit.py` — typed, and for each of the nine I said in one sentence what breaks if I delete it
- [ ] I identified the one assertion whose failure is invisible in the returned record and visible only in the written stream
- [ ] `run.py` — typed, and I predicted which of the six checks would be red on my machine **before** the first run
- [ ] I ran the honest-gap rep, or I wrote down that I could not because there is no working provider key on this machine

## Check

- [ ] The day's check is green: `cd projects/02-parts-counter && uv run --frozen python run.py check` — six green, `0 problem(s)`
- [ ] `echo $?` after it prints `0`, and I ran it rather than assuming it
- [ ] `uv run --frozen python -m pytest tests -q` — nine passed
- [ ] `uv lock --check` exits `0`
- [ ] **Break it on purpose, watch it go red, fix it.** Remove `"key"` from `SECRET_NAMES` in `parts_counter/util/logging.py`. Watch **two** tests go red — the top-level one and the nested one — read the secret sitting in the assertion output, then run `run.py check` and confirm `RED    tests` with pytest's summary line and exit `1`. Restore the entry and confirm nine green and exit `0`.
- [ ] **Break it on purpose, watch it go red, fix it.** In `Budget.charge`, move the two `+=` lines above the two `if` statements. Watch `test_a_refused_call_is_not_also_a_spent_one` go red and nothing else notice. Restore the order and say why that test carries that name.
- [ ] **Break it on purpose, watch it go red, fix it.** Set `models.ANSWERING` to `"gemini-flash-latest"`; watch `model` **and** `tests` both go red, and say why each one did. Set it to `"gemini-3.7-flash"` and read the other refusal message. Restore it.
- [ ] **Break it on purpose, watch it go red, fix it.** Edit `pyproject.toml` so `google-adk` reads `>=2.8.0`; watch `pins` and `lock` both go red, and say why each one did. Restore the `==`.
- [ ] **Break it on purpose and watch nothing go red.** Add a log call that passes a settings object under a field name with none of the six markers in it. Confirm the suite is still nine green and the gate is still six green, and say what I would add to this project so that it could not stay green.
- [ ] `git status --porcelain projects/` is empty — every break above was undone
- [ ] `python p.py depth 11` — green
- [ ] `python p.py check` — green across the whole repository

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — request budget, structured logging, redaction, dev dependency
- [ ] I checked `docs/GLOSSARY.md` first and linked rather than redefined *pin*, *floor*, *exit status*, *model alias*, *turn*, *stateless* and *process environment*
- [ ] `projects/02-parts-counter/PACKAGES.md` exists and carries the freshness check, the pins, the model pins and the rate-limit section from the hub §10
- [ ] The MCP specification revision is **not** stated anywhere in this day, and `PACKAGES.md` carries the `TODO(me)` for it with the exact page to open
- [ ] `docs/PINS.md` — nothing added today, and I can say which rule decides that
- [ ] `docs/SOURCES.md` — nothing added today, and I can say why the pages this day cites do not qualify
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10
- [ ] Committed with the message from the hub §10
