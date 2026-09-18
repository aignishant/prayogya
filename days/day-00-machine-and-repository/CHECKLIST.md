# Day 0 — definition of done

`python granth.py done 0` refuses to commit while any box below is unticked. That refusal is the point:
a day is finished when it is understood and the checks are green, and by nothing else.

Today `done 0` will also refuse for a second reason — the whole-repository gate runs `uv run ruff`,
which day 1 installs — so day 0's commit is made by hand with the message in the hub's §11. The
boxes still have to be ticked first.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-machine/1.1-the-python-pin.md` — read · ran its check · answered its question out loud
- [ ] `parts/01-machine/1.2-uv-project-and-lockfile.md` — read · ran its check · answered its question out loud
- [ ] `parts/01-machine/1.3-recording-what-you-have.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-repository/2.1-git-as-memory.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-repository/2.2-the-pre-commit-hook.md` — read · ran its check · answered its question out loud
- [ ] `parts/03-secrets/3.1-the-secrets-rule.md` — read · ran its check · answered its question out loud
- [ ] `parts/03-secrets/3.2-planting-a-secret.md` — read · ran all four steps · answered its question out loud

## Build

- [ ] `pyproject.toml`, `.python-version`, `uv.lock`, `src/prahari/__init__.py` — created by `uv init` and `uv sync`; `requires-python` is `>=3.12`, the pin is `3.12`; `uv run python -c "import sys; print(sys.executable)"` prints a path inside `.venv\`
- [ ] `.githooks/pre-commit` — written from part 2.2, `core.hooksPath` set, `git ls-files -s .githooks/pre-commit` shows `100755`
- [ ] `.githooks/pre-commit` — a third check refuses staged `.pem` and `.key` files, and a planted one was refused
- [ ] `.env` — copied from `.env.example`, filled in as far as you can, and absent from `git status --short`
- [ ] `docs/PINS.md` — the three rows from the hub's §11 appended, with the values *your* machine printed
- [ ] `docs/GLOSSARY.md` — the rows from the hub's §11 appended, after searching the file for each term

## Check

- [ ] The day's check is green: a planted `.env` staged with `-f` is refused by `git commit` with exit `1` and no new commit
- [ ] **Break it on purpose, watch it go red, fix it.** `git config --unset core.hooksPath`, commit the planted `.env`, watch it land; `git reset --hard HEAD~1`, re-create `.env`, re-set `core.hooksPath`
- [ ] Bypass two: `--no-verify` lands a planted key in `src/prahari/config.py`; `git reset --hard HEAD~1` removes it
- [ ] Read a "deleted" secret back: after `git rm --cached .env` and a commit, `git show HEAD~1:.env` prints it; then `git reset --hard HEAD~2` and re-create `.env`
- [ ] `git config core.hooksPath` prints `.githooks` and `git log --oneline -3` shows no planted commits
- [ ] `python granth.py depth 0` — green
- [ ] `python granth.py index --check` — every generated document current
- [ ] `python granth.py check` — **red** with `Failed to spawn: ruff`, and you have read why (hub §7); green is day 1's gate

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md`
- [ ] Every version observed today has a dated row in `docs/PINS.md` — including the `uv` that disagrees with the plan's row
- [ ] No source was cited today, so `docs/SOURCES.md` gains no row — confirmed by reading the parts' frontmatter
- [ ] The request budget in the hub's §6 was not exceeded: **0 requests**, and the count is written next to it
- [ ] The `docs/PROGRESS.md` row is pasted from the hub's §11
- [ ] Committed by hand with the message from the hub's §11, after `git status --short` was read and no secret was on it
