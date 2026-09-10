# Day 5 — definition of done

`python p.py done 5` refuses to commit while any box below is unticked. That refusal is the point:
a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [x] `parts/01-the-docket/1.1-the-declaration-is-the-whole-interface.md` — read · ran its check · answered its question out loud
- [x] `parts/01-the-docket/1.2-the-three-things-this-desk-can-do.md` — read · ran its check · answered its question out loud
- [x] `parts/02-the-round-trip/2.1-call-run-hand-back.md` — read · ran its check · answered its question out loud
- [x] `parts/02-the-round-trip/2.2-the-call-you-could-not-serve.md` — read · ran its check · answered its question out loud

## Build

- [x] `ask_desk/data/notes.json` — typed, and I predicted **before** running anything which query word would match a note it has nothing to do with, and which note
- [x] `ask_desk/tools.py` (the three functions) — typed, and I can name the exact line in `search_notes` that produced the wrong third hit
- [x] `ask_desk/tools.py` (`DECLARATIONS`) — the three declarations written by hand, and every `properties` key checked against the parameter name in the signature above it
- [x] I can say what happens when a `properties` key and a parameter name disagree, and name the line in `dispatch` where it surfaces
- [x] `ask_desk/tools.py` (`dispatch`) — typed, and I predicted which of the three bad calls would raise and which would return **before** running them
- [x] `ask_desk/provider.py` — `function_calls` and `function_response_message` added below `text_of`, and I can say why the first returns a list
- [x] `ask_desk/loop.py` — `MAX_CALLS_PER_QUESTION`, `LoopExhausted`, `use_tools`, `tools=` in `next_request`, and the tool branch in `ask`
- [x] I ran `run.py plan` with `use_tools` both ways and can say exactly which key appears and which does not
- [x] I read both quotations in part 2.1 about the tool-result turn's role, can say that they contradict each other, which one this project sends, and what evidence would settle it
- [x] I can say why `MAX_CALLS_PER_QUESTION` is a module constant rather than a parameter, and why `LoopExhausted` raises instead of returning the last text

## Check

- [x] The day's check is green: `cd projects/01-ask-desk && uv run --frozen python run.py check` — five green, `0 problem(s)`
- [x] `echo $?` after it prints `0`, and I ran it rather than assuming it
- [x] `uv run --frozen python run.py plan "Is the VPN down?"` prints a `"tools"` key holding all three declarations
- [x] **Break it on purpose, watch it go red, fix it.** Delete a comma in `notes.json`; watch every tool call fail at `_load` with `json.decoder.JSONDecodeError` naming the line and column. Restore it.
- [x] **Break it on purpose, watch it go red, fix it.** Rename `search_notes` to `find_notes` in the function and in `REGISTRY`, leave `DECLARATIONS` alone, and dispatch the name the declaration still promises. Watch `UnknownTool` name the drift you just created. Restore both.
- [x] **Break it on purpose, watch it fail to go red, fix it.** Dispatch `search_notes` with `{'q': 'vpn'}`. It returns a dictionary with an `error` key, exits normally, raises nothing and logs nothing. That is the day's deliberate failure — a wrong call with no traceback anywhere. Then dispatch with `{'query': 'vpn'}` and watch the same call succeed.
- [x] `python p.py depth 5` — green
- [x] `python p.py check` — green across the whole repository

## Record

- [x] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — function declaration, JSON Schema, tool call, tool-result turn
- [x] `docs/PINS.md` — nothing to add today, and I can say why re-recording an unchanged version would make the ledger worse
- [x] `docs/SOURCES.md` — nothing to add today, and I can say why provider documentation quoted with a URL and a date belongs in the hub §9 instead
- [x] The two `TODO(me)` items that need a working key are still open and unsolved: the tool-result turn's role, and the `finishReason` of a successful function call
- [x] The `docs/PROGRESS.md` row is pasted from the hub §10
- [x] Committed with the message from the hub §10
