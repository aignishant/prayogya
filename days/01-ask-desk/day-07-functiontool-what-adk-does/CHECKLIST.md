# Day 7 — definition of done

`python p.py done 7` refuses to commit while any box below is unticked. That refusal is the point:
a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-what-the-wrapper-reads/1.1-the-function-is-the-tool.md` — read · ran its check · answered its question out loud
- [ ] `parts/01-what-the-wrapper-reads/1.2-the-type-hints-are-the-schema.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-what-it-reads-that-you-did-not-mean-to-write/2.1-the-docstring-is-the-description.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-what-it-reads-that-you-did-not-mean-to-write/2.2-what-it-did-and-what-it-did-not.md` — read · ran its check · answered its question out loud

## Build

- [ ] `ask_desk/agent.py` — I predicted what `desk.canonical_tools()` would return **before** running it, and I was right or I know why not
- [ ] `grep -n search_notes ask_desk/agent.py` — run, and I can say where the name the model receives actually comes from
- [ ] `ask_desk/tools.py` — all three declarations derived, and I predicted which would carry a `default` key before looking
- [ ] The untyped probe — I copied `search_notes`'s signature without its annotations, derived the schema, and can name every key that disappeared and every key that survived
- [ ] **The declaration audit** — I wrote the command that walks `desk.canonical_tools()` and prints `RED` for any description that is empty or equal to `'Call self as a function.'`, and for any schema property with no `type` key
- [ ] The audit **exits non-zero** when it finds one, and I ran `echo $?` rather than assuming it
- [ ] I can say why `_get_declaration()` is used in probes and never in `ask_desk/`
- [ ] I can recite the last column of part 2.2's arc table — the three things the framework did not take over — without looking

## Check
- [ ] I found `RunConfig.max_llm_calls` myself, read its default back as `500`, and can say why that is a runaway ceiling rather than a budget
- [ ] I can say what `max_llm_calls=0` does, and why that is the wrong way round from how it reads

- [ ] The day's check is green: `cd projects/01-ask-desk && uv run --frozen python run.py check` — five green, `0 problem(s)`
- [ ] `echo $?` after it prints `0`, and I ran it rather than assuming it
- [ ] **Break it on purpose, watch it go red, fix it.** Delete the one-line docstring from `check_service_status` in `ask_desk/tools.py`, leaving the function otherwise untouched. Derive all three descriptions and watch `check_service_status   'Call self as a function.'` appear beside two correct rows. Run my audit against it and watch it go **red**. Put the docstring back, re-derive, and confirm the description returns
- [ ] **Break it on purpose, watch nothing go red.** With that same docstring still deleted, run `uv run --frozen python run.py check` and `echo $?`. Five green at exit `0`, on a desk whose status tool has stopped describing itself. I can say why each of the five checks is blind to it
- [ ] **Break it on purpose, watch it go red, fix it.** Change `limit: int = 3` to `limit=3` in `search_notes`, derive the schema, and confirm the `type` key is gone. Run my audit against it. Restore the annotation
- [ ] **Break it on purpose, watch the two halves disagree.** Rename `fetch_note` and leave day 5's `DECLARATIONS` untouched. Derive the tool names and read them against `tools.DECLARATIONS`. Restore the name
- [ ] `python p.py depth 7` — green
- [ ] `python p.py check` — green across the whole repository

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — `FunctionTool`, derived declaration — and I checked whether day 5 already added a row for the hand-written function declaration before appending
- [ ] `docs/PINS.md` — nothing to add today, and I can say why re-observing google-adk 2.8.0, uv 0.12.3 and CPython 3.12.12 does not earn a row
- [ ] `docs/SOURCES.md` — nothing to add today, and I can say why two documentation pages and an API reference do not qualify
- [ ] `projects/01-ask-desk/CODEMAP.md` — unchanged, and its *Day 07 prints nothing* note still says the truth
- [ ] The behavioural half of part 2.1 is still marked `TODO(me)` and nothing in today's documents claims what the model does
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10
- [ ] Committed with the message from the hub §10
