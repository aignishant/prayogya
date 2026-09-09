# Day 6 — definition of done

`python p.py done 6` refuses to commit while any box below is unticked. That refusal is the point:
a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-the-brief/1.1-the-agent-is-a-configuration.md` — read · ran its check · answered its question out loud
- [ ] `parts/01-the-brief/1.2-the-model-nobody-chose.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-the-one-who-runs-it/2.1-the-runner-the-session-and-the-await.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-the-one-who-runs-it/2.2-the-runner-with-nowhere-to-put-it.md` — read · ran its check · answered its question out loud

## Build

- [ ] `projects/01-ask-desk/pyproject.toml` — `google-adk==2.8.0` added with `uv add`, and I can say which two files it wrote and why `>=` would turn the `pins` check red
- [ ] `projects/01-ask-desk/ask_desk/agent.py` — typed, and I predicted `desk.model` and `desk.canonical_model.model` **before** running the probe
- [ ] I predicted both of those again for an agent with the `model=` line deleted, and was right about which one changes
- [ ] `agent.py` — I changed the name to `"ask desk"`, predicted whether the failure would arrive at import or at the first question, ran it, and put the name back
- [ ] For each of the five rows in `agent.py`'s docstring table, I found the hand-rolled code it names in `loop.py` or `tools.py` and said what would break if nothing had replaced it
- [ ] `projects/01-ask-desk/run.py` — the `adk` subcommand is in, and I can say why `from ask_desk import agent` sits inside the function rather than at the top
- [ ] I can say where `MAX_CALLS_PER_QUESTION` is enforced, what enforces it on the `adk` path, and I wrote what I would add — in `lab/`, not in `agent.py`
- [ ] I sketched the sixth check that would catch an unpinned agent, and can say why it must read `canonical_model` rather than `model` or the source text

## Check

- [ ] The day's check is green: `cd projects/01-ask-desk && uv run --frozen python run.py check` — five green, `0 problem(s)`
- [ ] `echo $?` after it prints `0`, and I ran it rather than assuming it
- [ ] The agent probe runs with no key: `model (set)` and `canonical` agree, three `FunctionTool` rows, `runner agent   ask_desk`
- [ ] **Break it on purpose, watch it go red, fix it.** Change `google-adk==2.8.0` to `>=2.8.0`; watch the `pins` check go red. Restore it with `uv add`.
- [ ] **Break it on purpose, watch it go red, fix it.** Point `models.ANSWERING` at an ID not in `PINNED`; watch the `model` check go red *and* the import of `agent.py` fail. Restore it.
- [ ] **Break it on purpose, watch the framework refuse.** Delete `session_service=` from `build_runner` and run the probe: `TypeError: Runner.__init__() missing 1 required keyword-only argument: 'session_service'`. Restore it.
- [ ] **Break it on purpose, watch nothing go red.** Delete the `model=` line from `agent.py`, run `run.py check`, confirm all five rows are still green, then run the probe and read `what it will call`. Restore the line.
- [ ] **Break it on purpose and paste the real output.** Delete the `await` before `create_session`, run `uv run --frozen python run.py adk "Is the VPN down?"`, and paste what Python actually says into part 2.1's `TODO(me)` block. Restore the `await`.
- [ ] I ran `run.py adk "Is the VPN down?"` with the synthetic key, saw the `400 INVALID_ARGUMENT`, and found `tenacity` in the stack myself
- [ ] `python p.py depth 6` — green
- [ ] `python p.py check` — green across the whole repository

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — Agent (ADK), Runner, Session
- [ ] I can say why **Event** is not one of those rows
- [ ] `projects/01-ask-desk/PACKAGES.md` — nothing to append today, and I can say why the `google-adk` and `gemini-3.8-flash` rows were already there
- [ ] `docs/PINS.md` and `docs/SOURCES.md` — nothing to add today, and I can say why for each
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10
- [ ] Committed with the message from the hub §10
