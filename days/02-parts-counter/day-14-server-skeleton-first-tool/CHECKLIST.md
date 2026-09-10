# Day 14 — definition of done

`python p.py done 14` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-the-move/1.1-the-file-changes-owner.md` — read · ran its check · answered its question out loud
- [ ] `parts/01-the-move/1.2-four-tools-on-the-far-side.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-what-the-wire-carries/2.1-the-tool-object-and-the-envelope.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-what-the-wire-carries/2.2-the-error-the-model-can-fix.md` — read · ran its check · answered its question out loud

## Build

- [ ] `parts_mcp/store.py` — typed, and I named the two lines the critical section in `adjust` spans
- [ ] I can say which of day 12's two failures the **lock** fixes and which `_write_atomically` fixes, and which would still happen with only one of them
- [ ] I wrote one sentence each on who `_LOCK` excludes and who `_replace_with_retry` survives — and named one interferer neither can do anything about
- [ ] `tempfile.mkstemp(dir=DATA_DIR, ...)` — I changed it to `mkstemp()` with no `dir`, predicted what would change, ran `run.py race`, and found out whether I was right. Restored, and `git status --porcelain` is empty.
- [ ] `parts_mcp/server.py` — the four tools typed, and for each I wrote down every declaration field a model receives and which source line produced it
- [ ] I can say where a note about `delta` being negative for issuing stock has to live, and why there is nowhere else for it
- [ ] `@mcp.tool()` — I removed the parentheses from one, imported the module, read the `TypeError` in full, and identified the traceback line proving it failed at **import** rather than at call time. Restored.
- [ ] The four declarations printed: I listed the fields that come back `null`, and for each wrote the source change that would fill it in — and said which I would insist on before letting a model call `adjust_stock`
- [ ] `tests/test_boundary.py` — typed, fourteen green
- [ ] I can say how `test_a_reader_never_sees_a_half_written_file` would **hang** rather than fail if the writer thread died, and what change would make it go red instead
- [ ] I wrote the case for and against reporting an unknown part as `{"error": ...}` inside a result with `isError: false`, and said which I would ship

## Check

- [ ] The day's check is green: `cd projects/02-parts-counter && uv run --frozen python run.py check` — six green, `0 problem(s)`
- [ ] `echo $?` after it prints `0`, and I ran it rather than assuming it
- [ ] `uv run --frozen python -m pytest tests -q` — fourteen passed
- [ ] `uv run --frozen python run.py race` — `parts unaccounted : 0` and `reads that crashed : []`, three times running
- [ ] **Break it on purpose, watch it go red, fix it.** Delete `with _LOCK:` from `store.adjust`, run `test_two_writers_lose_nothing`, and record the number in the assertion. Run it twice more and record those too — they differ. Restore and confirm fourteen green.
- [ ] **Break it on purpose, watch it go red, fix it.** Remove the parentheses from one `@mcp.tool()` and import the module. Read the real `TypeError`. Restore.
- [ ] `python p.py depth 14` — green
- [ ] `python p.py check` — green across the whole repository
- [ ] `git status --porcelain projects/` is empty, and `parts_mcp/data/parts.json` is byte-identical to how the day started

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — atomic replace, tool object, tool result envelope, protocol error, tool execution error
- [ ] `projects/02-parts-counter/CODEMAP.md` records the move: `parts_counter/data/parts.json` to `parts_mcp/data/`, and `parts_counter/store.py` and `tools.py` deleted
- [ ] `docs/PINS.md` — nothing to add today, and I can say why a project's own pins live in its `PACKAGES.md`
- [ ] `docs/SOURCES.md` — nothing to add today, and I can say why a living specification page is dated in the hub §9 instead
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10
- [ ] Committed with the message from the hub §10
