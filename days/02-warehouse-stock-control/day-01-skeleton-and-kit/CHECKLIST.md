# P02 day 1 — definition of done

`python p.py done 02 1` refuses to commit while any box below is unticked. That refusal is the
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

- [ ] `pyproject.toml` — the name, `==3.12.*`, the `dev` group with `ruff==0.16.7` and
      `pytest==9.1.1`, `package = false`, the ruff rules, `pythonpath = ["."]`
- [ ] `uv sync` — `Installed 7 packages`, and `uv.lock` committed
- [ ] `PACKAGES.md` — the two rows for ruff and pytest, dated
- [ ] `stock_desk/__init__.py` and `stock_desk/util/__init__.py` — docstrings only
- [ ] `run` — `COMMANDS`, `PLANNED` with five entries, the `FileNotFoundError` branch, and
      `100755` in git
- [ ] `stock_desk/util/keys.py` — `load_env`, `require`, `fingerprint`
- [ ] `stock_desk/util/logging.py` — `words_of`, `looks_secret`, `redact`, `log`, to standard error
- [ ] `stock_desk/util/backoff.py` — `Transient` with `retry_after`, `delays`, `retry`
- [ ] `stock_desk/util/budget.py` — `Budget` and `BudgetExceeded`
- [ ] `stock_desk/models.py` — `PRIMARY`, `FALLBACK`, `LEGACY`, `ALLOWED`, `pinned`
- [ ] `tests/test_kit.py` — seventeen tests, including the eight parametrised word cases
- [ ] `stock_desk/util/logging.py` — `TODO(me)`: two secret-carrying field names the six words miss
- [ ] `stock_desk/util/backoff.py` — `TODO(me)`: the `async` twin of `retry`, or why there is none
- [ ] `stock_desk/util/budget.py` — `TODO(me)`: a ceiling on characters sent
- [ ] `stock_desk/models.py` — `TODO(me)`: the framework's default model ID, confirmed on the day
      it is installed
- [ ] `run` — `TODO(me)`: stop at the first failure, or report every failure

## Check

- [ ] The day's check is green: `./run check` — `All checks passed!`, `17 passed`, five `ok`
      lines, `OK check`
- [ ] Ran `./run` and `./run mcp` and read the map of what is not built yet
- [ ] Ran the four demos — the fingerprint, the log line, the retry, the budget — and the registry's
      three refusals
- [ ] **Break it on purpose, watch it go red, fix it.** A line over a hundred characters. The
      substring redactor. `retry` ignoring `retry_after`. `pinned` returning unconditionally. The
      last line of `budget.py` deleted. Put every one back.
- [ ] **The failure that is green.** Disable only the `-latest` line and watch the alias still be
      refused — by a different line, with a different message. Put it back.
- [ ] `python p.py depth 02 1` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path — and the change to
      `PACKAGES.md` is a marked diff naming the day of THIS project that printed the original
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own day 0
- [ ] No number in any part is quoted from this document rather than from your own run — the
      package count, the fingerprint, the test count
- [ ] Nothing in the kit knows what a bin, a count or a variance is

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the thirteen
      rows in the hub §10
- [ ] The project's `PACKAGES.md` has the two rows from part 1.1, dated
- [ ] No `docs/PINS.md` row is owed — both packages are project pins
- [ ] No `docs/SOURCES.md` row is owed — nothing with a citation identifier was cited
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
