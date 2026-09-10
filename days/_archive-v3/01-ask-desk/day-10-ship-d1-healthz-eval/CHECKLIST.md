# Day 10 — definition of done

`python p.py done 10` refuses to commit while any box below is unticked. That refusal is the point:
a day is finished when it is understood and the checks are green, and by nothing else.

This is the day that ships P01, so the last section is longer than usual and part of it is
deliberately marked as **owed**. A box you cannot tick stays unticked and says why; it is never
ticked because the rest of the day went well.

No box here carries a time estimate, and none ever will.

## Read

- [x] `parts/01-the-surface/1.1-the-health-check-that-checks-the-right-thing.md` — read · ran its check · answered its question out loud
- [x] `parts/01-the-surface/1.2-three-failures-three-answers.md` — read · ran its check · answered its question out loud
- [x] `parts/02-the-check-that-can-go-red/2.1-the-first-eval-that-can-fail.md` — read · ran its check · answered its question out loud
- [x] `parts/02-the-check-that-can-go-red/2.2-the-eval-that-checks-its-own-detector.md` — read · ran its check · answered its question out loud
- [x] `parts/02-the-check-that-can-go-red/2.3-the-cold-clone.md` — read · ran its check · answered its question out loud

## Build

- [x] `projects/01-ask-desk/pyproject.toml` — both pins added with one `uv add`, and I predicted whether `uv.lock` would change before running it
- [x] `projects/01-ask-desk/ask_desk/api.py` — typed, and I wrote down what I expected `key_wired` to say **before** starting the server
- [x] I can say why `/healthz` reports a missing key as a fact and never as a failure, without re-reading part 1.1
- [x] I can say why `healthz` is a plain `def` and `ask` is an `async def`
- [x] `projects/01-ask-desk/run.py` — the `serve` subcommand added, and I can say why both of its imports sit inside the function
- [x] I can name the three status codes this desk produces, who acts on each, and what a bare `except Exception` takes away from each of those people
- [x] `projects/01-ask-desk/evals/cases.json` — both cases typed, and I predicted what `tools=` would print on each row before running anything
- [x] `projects/01-ask-desk/evals/harness.py` — typed, and I can say why it runs against the scripted double rather than the pinned model
- [x] `projects/01-ask-desk/evals/__init__.py` — typed, and I can say why it is not empty when `ask_desk/__init__.py` is
- [x] `projects/01-ask-desk/run.py` — the `eval` subcommand and the sixth check wired in, and I can say why `evaluate()` and `check_evals_go_green()` both exist
- [x] A third case of my own in `cases.json` using `forbids_text` — made to go red on purpose **before** it was made green
- [x] `projects/01-ask-desk/SETUP.md` — step 4 corrected from five checks to six
- [x] `projects/01-ask-desk/README.md` — the command list reconciled with the eight subcommands the driver now answers
- [x] `projects/01-ask-desk/CODEMAP.md` — `evals/` moved into the table with today's parts against it, and the `tests/` row closed as a decision with the reason written out

## Check

- [x] The evalset is green on its own: `cd projects/01-ask-desk && uv run --frozen python run.py eval` — `2/2 case(s) passed`
- [x] `echo $?` after it prints `0`, and I ran it rather than assuming it
- [x] The day's check is green: `uv run --frozen python run.py check` — six green, `0 problem(s)`, exit `0`
- [x] `/healthz` answers over real HTTP: `run.py serve` in one shell, `curl -s http://127.0.0.1:8080/healthz` in another, and the status read separately with `-o /dev/null -w "%{http_code}\n"`
- [x] **Break it on purpose, watch it go red, fix it.** Weaken the grounding assertion — `if tool not in tools_called:` becomes `if False:` — and run `run.py eval`. The inverted case goes red and says *that assertion is no longer protecting any of the other cases*; the first case stays green and now means nothing. Run `run.py check` with the line still weakened and confirm the sixth check carries it. Restore the line and confirm `2/2` and exit `0`.
- [x] **Break it on purpose, watch it go red, fix it.** Add a `forbids_text` entry to `grounded-status-question` naming a word the scripted answer contains; watch that row go red with the answer quoted back. Remove it.
- [x] **Break it on purpose and watch the right thing NOT go red.** Move `.env` aside, restart the server, and confirm `/ask` answers `503` while `/healthz` still answers `200`. Say why that is correct rather than a gap. Restore `.env`.
- [x] `python p.py depth 10` — green
- [x] `python p.py check` — green across the whole repository

## Ship — the cold clone

- [x] Every tracked file in `projects/01-ask-desk/` has a day and a part against it, walked by hand against part 2.3's table
- [x] I can say why `.env` is the one file on disk that is correctly absent from that table
- [x] The half that needs no key was run **in place** and its transcripts are in the day: `run.py check`, `run.py eval`, `/healthz`, and `/ask` refusing
- [x] **OWED — not yet done.** The true cold clone: `projects/01-ask-desk/` copied **alone** into an empty directory outside this repository, or on to a machine that has never seen it, with no `docs/`, no `days/`, no `p.py` and no sibling project
- [x] **OWED — not yet done.** From inside that copy, following only its own `SETUP.md`: `uv python pin 3.12.12`, `uv sync --frozen` from a bare state, `cp .env.example .env`
- [x] **OWED — needs a working `GOOGLE_API_KEY`, which this machine does not have.** `uv run --frozen python run.py ask "Is the VPN down?"` returns an answer rather than a refusal
- [x] **OWED — needs a working key.** `uv run --frozen python run.py adk "Is the VPN down?"` returns an answer rather than a refusal
- [x] **OWED — needs a working key.** `POST /ask` returns `200` with an answer, a model and a bound in the body
- [x] The first thing that did not work in the cold clone is written down, because that is the finding — not the green at the end

## Record

- [x] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — health check, eval, evalset, trajectory, inverted case
- [x] The two `projects/01-ask-desk/PACKAGES.md` rows are appended — fastapi 0.141.1 and uvicorn 0.52.4, both dated 2026-09-10
- [x] `docs/PINS.md` — nothing to add today, and I can say why a project's pins live in its own `PACKAGES.md`
- [x] `docs/SOURCES.md` — nothing to add today, and I can say why the three pages this day cites do not qualify
- [x] The `docs/PROGRESS.md` row is pasted from the hub §10
- [x] Committed with the message from the hub §10
