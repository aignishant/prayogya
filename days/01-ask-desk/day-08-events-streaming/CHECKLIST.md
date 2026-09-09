# Day 08 — definition of done

`python p.py done 8` refuses to commit while any box below is unticked. That refusal is the point: a
day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-watching/1.1-the-stand-in-that-lets-you-watch.md` — read · ran its check · answered its question out loud
- [ ] `parts/01-watching/1.2-what-an-event-is-and-which-one-is-the-answer.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-the-stream/2.1-nineteen-events-for-one-sentence.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-the-stream/2.2-the-answer-that-arrived-twice.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-the-stream/2.3-the-bound-seen-firing.md` — read · ran its check · answered its question out loud

## Build

- [ ] `ask_desk/scripted.py` — typed whole from part 1.1, not pasted; I predicted the `model` string and the number of responses one non-streaming `Say` step yields, and was right or know why not
- [ ] `ask_desk/agent.py` — part 1.1's diff applied, and I can say why `model if model is not None else ...` is not `model or ...`, with the argument value that makes the difference visible
- [ ] `ask_desk/agent.py` — part 2.1's diff applied, and I reconciled it with whatever I wrote for day 7's `max_llm_calls` rep
- [ ] `run.py` — part 1.2's diff applied; I predicted the streamed event count from the sentence alone before running it
- [ ] `run.py` — the top-level `google.adk.sessions` import moved inside `events`, and I can say what would have to exist here for that regression to have gone red instead of being noticed by reading
- [ ] a probe I wrote — the two accumulators from part 2.2, plus a third that is correct under either contract; I named the assumption it rests on
- [ ] `ask_desk/agent.py`, read only — I decided whether `ask()` should ever stream, and said what would have to change about its signature first
- [ ] the drift check — a check that fails when `build_desk` and the module-level `desk` disagree, wired into `run.py check`, seen going red and exiting non-zero
- [ ] the bound — part 2.3's probe run at `max_llm_calls=3` and at `6`, both event counts recorded, and my expectation at 500 stated without running it
- [ ] the behavioural half — recorded as unrun, with the exact command, because there is no working key on this machine

## Check

- [ ] The day's check is green: `cd projects/01-ask-desk && uv run --frozen python run.py check` and `echo $?` is `0`
- [ ] `uv run --frozen python run.py events` — three rows, footer `3 events, 2 model call(s)`
- [ ] `uv run --frozen python run.py events --stream` — nineteen rows, footer `19 events, 2 model call(s)`
- [ ] **Break it on purpose, watch it go red, fix it.** Delete `name="ask_desk"` from `build_desk` and run `run.py events`: it refuses before a single event exists. Put it back and watch it pass.
- [ ] **Break it on purpose and watch nothing go red.** Drop the `if e.partial` clause from part 2.2's accumulator, run the whole gate, and confirm five green and exit `0` over a doubled answer. Then say, out loud, which day of this project fixes that and what it will take.
- [ ] **Break the count.** Set `max_llm_calls=0` in `run_config()`, run part 2.3's runaway, and confirm the bound is gone rather than absolute. Put the six back.
- [ ] `python p.py depth 8` — green
- [ ] `python p.py check` — green across the whole repository

## Record

- [ ] `Event`, `Partial event`, `Streaming mode` and `Test double` appended to `docs/GLOSSARY.md` from the hub §10
- [ ] `projects/01-ask-desk/CODEMAP.md` — the `ask_desk/scripted.py` row added, and the `run.py` and `ask_desk/agent.py` rows amended, from the hub §10
- [ ] Every version or limit observed today has a dated row in `docs/PINS.md` — or the hub §10's statement that there is none is still true
- [ ] Every source cited today has a dated row in `docs/SOURCES.md` — or the hub §10's statement that there is none is still true
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10
- [ ] Committed with the message from the hub §10
