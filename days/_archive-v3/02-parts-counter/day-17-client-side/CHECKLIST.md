# Day 17 — definition of done

`python p.py done 17` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-a-list-you-no-longer-write/1.1-the-toolset-that-asks.md` — read · ran its check · answered its question out loud
- [ ] `parts/01-a-list-you-no-longer-write/1.2-a-call-that-leaves-the-process.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-the-agent-on-this-side/2.1-one-toolset-not-four-functions.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-the-agent-on-this-side/2.2-the-tools-that-were-not-there.md` — read · ran its check · answered its question out loud

## Build

- [ ] `parts_counter/util/mcp.py` — typed, and I said which connection shape launches a process and which assumes one is running **before** running either
- [ ] I can say why `command=sys.executable` and not `command="python"`, and I broke it to find out what fails
- [ ] `parts_counter/agent.py` — typed, and I diffed it by eye against `projects/01-ask-desk/ask_desk/agent.py`
- [ ] For every line that is the *same* as P01's agent, I named the earlier day that decided it
- [ ] I traced `max_llm_calls` back to the constant it comes from, and said what number would take over if the argument were dropped
- [ ] `run.py probe` — run, and run again with day 16's stray `print()` reinstated; I said which failure I would rather debug
- [ ] I wrote down what a seventh check in `run.py check` would have to do for a missing boundary to go red — what it calls, what it asserts, and whether it belongs in `check` or in a readiness endpoint. I did **not** implement it; day 8 of this project owes it.

## Check

- [ ] `cd projects/02-parts-counter && uv run --frozen python run.py probe` — four tools listed, one call returned
- [ ] `uv run --frozen python run.py check` — six green, `0 problem(s)`
- [ ] `echo $?` after it prints `0`, and I ran it rather than assuming it
- [ ] **Break it on purpose, watch it go red, fix it.** Point `over_stdio`'s `args` at a module that does not exist. `get_tools()` raises `ConnectionError … Connection closed`, and the real reason appears only on the subprocess's stderr. Restore.
- [ ] **Break it on purpose, watch it go red, fix it.** Point `over_http` at a port with nothing listening. Same exception type, message ends `All connection attempts failed`, and there is no stderr to help. Restore.
- [ ] **Break it on purpose and watch nothing go red.** With the boundary unreachable, run `run.py check` and confirm it is still green at exit `0`. I can say why that is the honest state of this project today and which day owes the fix.
- [ ] `python p.py depth 17` — green
- [ ] `python p.py check` — green across the whole repository

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — toolset, MCP client, connection params
- [ ] `projects/02-parts-counter/CODEMAP.md` attributes `parts_counter/util/mcp.py` and `parts_counter/agent.py` to this day, and `run.py`'s `probe` subcommand
- [ ] `docs/PINS.md` — nothing to add today, and I can say why a project's pins live in its own `PACKAGES.md`
- [ ] `docs/SOURCES.md` — nothing to add today, and I can say why
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10
- [ ] Committed with the message from the hub §10
