# Day 3 — definition of done

`python p.py done 3` refuses to commit while any box below is unticked. That refusal is the point:
a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-the-key/1.1-the-code-and-the-cut.md` — read · ran its check · answered its question out loud
- [ ] `parts/01-the-key/1.2-three-states-and-the-one-you-cannot-check.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-the-pin-and-the-refusal/2.1-a-floor-is-not-a-pin.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-the-pin-and-the-refusal/2.2-the-check-that-could-not-refuse.md` — read · ran its check · answered its question out loud

## Build

- [ ] `projects/00-foundry/keys.py` — typed, and I predicted which of `os.environ` and `.env` would win **before** running it
- [ ] `projects/00-foundry/keys.py` — I drove `require` through all three states without touching the project's real `.env`, and can say which two it refuses and why the third is not refusable here
- [ ] I can say why `read_env_file` takes `path: Path | None = None` and resolves the default inside the body, without re-reading part 1.1
- [ ] `projects/00-foundry/.python-version` — written with `uv python pin`, and I predicted the exact string first
- [ ] `projects/00-foundry/pyproject.toml` — the floor is now a pin, and I found the day-1 row in `docs/PINS.md` that disagrees with the installed version
- [ ] I can say why `requires-python = ">=3.12"` stays in `pyproject.toml` rather than being replaced by `.python-version`
- [ ] `projects/00-foundry/run.py` — typed, and I predicted which checks would be red **before** the first run
- [ ] I can say why every `check_*` returns `list[str]` rather than a bool, and why no check raises

## Check

- [ ] The day's check is green: `cd projects/00-foundry && uv run --frozen python run.py check` — four green, `0 problem(s)`
- [ ] `echo $?` after it prints `0`, and I ran it rather than assuming it
- [ ] `uv lock --check` exits `0`
- [ ] **Break it on purpose, watch it go red, fix it.** Empty the value in `.env`; watch `keys` go red with *present with an empty value* rather than *not set*. Restore it.
- [ ] **Break it on purpose, watch it go red, fix it.** Change `platformdirs==4.11.8` back to `>=4.11.8`; watch `pins` go red. Restore it with `uv add`.
- [ ] **Break it on purpose, watch it fail to go red, fix it.** Remove `sys.exit(` and its bracket from the `__main__` block, empty the key, run the check and then `echo $?`. It printed `RED` and `1 problem(s)` and exited `0`. Put the line back, run both again, and confirm identical output with exit `1`.
- [ ] **Break it on purpose, watch the check repair what it was checking.** Make `pyproject.toml` and `uv.lock` disagree, run the check through plain `uv run`, and confirm `uv.lock` changed. Repeat with `uv run --frozen` and confirm it did not.
- [ ] `python p.py depth 3` — green
- [ ] `python p.py check` — green across the whole repository

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — process environment, floor, exit status
- [ ] The two `docs/PINS.md` rows are appended, and the platformdirs row says it **supersedes** rather than corrects
- [ ] `docs/SOURCES.md` — nothing to add today, and I can say why the two things this day cited do not qualify
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10
- [ ] Committed with the message from the hub §10
