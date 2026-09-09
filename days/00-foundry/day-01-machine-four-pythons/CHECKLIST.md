# Day 1 — definition of done

`python p.py done 1` refuses to commit while any box below is unticked. That refusal is the point:
a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [x] `parts/01-the-name/1.1-four-things-called-python.md` — read · ran its check · answered its question out loud
- [x] `parts/01-the-name/1.2-an-environment-is-a-place.md` — read · ran its check · answered its question out loud
- [x] `parts/02-the-project/2.1-the-project-that-owns-its-interpreter.md` — read · ran its check · answered its question out loud
- [x] `parts/02-the-project/2.2-the-two-commands-that-disagree.md` — read · ran its check · answered its question out loud

## Build

- [x] `projects/00-foundry/` exists, was created with `uv init --name foundry --python 3.12 --bare`, and contains nothing I cannot account for
- [x] `projects/00-foundry/foundry/whoami.py` — typed, run with the bare name, and I named which interpreter would answer **before** reading the path it printed
- [x] `projects/00-foundry/pyproject.toml` — read back; I can say what `requires-python` does and does not promise
- [x] `projects/00-foundry/uv.lock` — I found the line that catches a right-version, wrong-contents package and can say what it compares
- [x] `uv add platformdirs` run, and I can name the three things it changed

## Check

- [x] `uv python list` — I can point at every row ending in a path and say where that interpreter came from
- [x] `where python` (or `which -a python`) and `uv python find` — run both, and I can say whether they agree on *my* machine and why that is not a fault
- [x] `uv run foundry/whoami.py` — reports `in_venv True` and a `prefix` inside `.venv`
- [x] `uv run --python 3.11 foundry/whoami.py` — refused, cites `requires-python`, exits `2`
- [x] **Break it on purpose, watch it go red, fix it.** With `platformdirs` a dependency, run `python foundry/whoami.py` and watch it exit `1` with `ModuleNotFoundError`, then `uv run foundry/whoami.py` and watch it exit `0`. Same file, same directory
- [x] **Second break.** Move `.venv/pyvenv.cfg` aside, re-run the import against `.venv/Scripts/python.exe` directly, watch the *same* error arrive from a different cause, then put it back
- [x] **Third break — the document.** Delete a `## In production` heading from any part, run `python p.py depth 1`, see it named, restore it
- [x] `python p.py depth 1` — green
- [x] `python p.py check` — green across the whole repository

## Record

- [x] Every term defined for the first time today has a row in `docs/GLOSSARY.md`
- [x] Every version observed today has a dated row in `docs/PINS.md`
- [x] `docs/SOURCES.md` — nothing to add; the three uv pages are dated in the hub §9, and I checked rather than assumed
- [x] The `docs/PROGRESS.md` row is pasted from the hub §10
- [x] Committed with the message from the hub §10
