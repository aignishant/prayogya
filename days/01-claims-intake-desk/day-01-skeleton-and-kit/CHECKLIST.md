# P01 day 1 — definition of done

`python p.py done 01 1` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-the-skeleton/1.1-one-project-declared-once.md` — read · ran its check · answered
      its question out loud
- [ ] `parts/01-the-skeleton/1.2-package-every-import-starts-with.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/01-the-skeleton/1.3-one-door-into-the-desk.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/02-the-kit/2.1-key-read-once.md` — read · ran its check · answered its question out
      loud
- [ ] `parts/02-the-kit/2.2-one-line-one-record.md` — read · ran its check · answered its question
      out loud
- [ ] `parts/02-the-kit/2.3-wait-what-you-were-told-to-wait.md` — read · ran its check · answered
      its question out loud
- [ ] `parts/02-the-kit/2.4-ceiling-that-refuses.md` — read · ran its check · answered its question
      out loud
- [ ] `parts/03-the-registry/3.1-registry-that-refuses-an-alias.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/03-the-registry/3.2-gate-that-goes-red.md` — read · ran its check · answered its
      question out loud

## Build

Every file typed by hand, at its real path. `pyproject.toml` before `uv sync`, and the tests last.

- [ ] `pyproject.toml` — the two pins with `==`, `requires-python`, the ruff and pytest tables
- [ ] `uv sync` run, `.venv/` created, `uv.lock` committed, `.venv/` **not** committed
- [ ] `claims_desk/__init__.py` and `claims_desk/util/__init__.py`
- [ ] `claims_desk/util/keys.py`
- [ ] `claims_desk/util/logging.py`
- [ ] `claims_desk/util/backoff.py`
- [ ] `claims_desk/util/budget.py`
- [ ] `claims_desk/models.py`
- [ ] `run`, and `git update-index --chmod=+x run` — `git ls-files -s run` shows `100755`
- [ ] `tests/test_kit.py`
- [ ] `PACKAGES.md` — `TODO(me)`: a dated row for ruff and one for pytest, with your own observed
      versions and the command that printed them
- [ ] `claims_desk/util/logging.py` — `TODO(me)`: `redact` walks past lists; fix it, test first
- [ ] `claims_desk/util/backoff.py` — `TODO(me)`: add jitter without breaking the schedule test
- [ ] `claims_desk/util/budget.py` — `TODO(me)`: a way to ask "may I?" without spending
- [ ] `run` — `TODO(me)`: `--keep-going`, with an honest exit status

## Check

- [ ] The day's check is green: `./run check` — `All checks passed!`, `9 passed`, four `ok` lines,
      `OK check`
- [ ] **Break it on purpose, watch it go red, fix it.** Set `PRIMARY` to `"gemini-flash-latest"` in
      `claims_desk/models.py` and run `./run check`. Expect `DID NOT RAISE UnpinnedModel`, expect
      the driver to stop before the machine check, and expect a non-zero exit. Put it back.
- [ ] Ran `./run` with no argument and read the four commands that do not exist yet
- [ ] `python p.py depth 01 1` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path — no `...`, no
      "the rest is unchanged" without naming the day of THIS project that printed the original
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own earlier days — day 0
      is the only thing it stands on, and it stands on all of it

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the sixteen
      rows in the hub §10, restated definitions included
- [ ] `ruff` and `pytest` have dated rows in this project's own `PACKAGES.md`. No `docs/PINS.md`
      row is owed today, and the hub §10 says why
- [ ] No `docs/SOURCES.md` row is owed today — nothing with a citation identifier was cited, and
      the pages read are in the hub §9 with their dates
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
