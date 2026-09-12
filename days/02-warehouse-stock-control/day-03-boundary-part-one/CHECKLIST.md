# P02 day 3 — definition of done

`python p.py done 02 3` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-why-a-boundary/1.1-the-counter-and-the-cage.md` — read · ran its check · answered
      its question out loud
- [ ] `parts/02-the-server/2.1-server-and-the-tool-it-declares.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/02-the-server/2.2-run-it-as-a-process.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/03-the-line/3.1-what-crosses-the-line.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/03-the-line/3.2-print-that-corrupted-the-protocol.md` — read · ran its check ·
      answered its question out loud

## Build

- [ ] `stock_mcp/__init__.py` — the boundary's own docstring, naming what it costs and what it buys
- [ ] `stock_mcp/server.py` — `server`, `store`, `fetch_bin`
- [ ] `stock_mcp/__main__.py` — `server.run("stdio")`, nothing else
- [ ] `run` — gains `mcp`, loses the `PLANNED` row for it
- [ ] `tests/test_boundary.py` — six tests, five in-process and one over a real subprocess
- [ ] `stock_mcp/server.py` — `TODO(me)`: whether `fetch_bin`'s `reorder_at` field belongs on the
      wire before a rule reads it
- [ ] `stock_mcp/server.py` — `TODO(me)`: whether the boundary should log who scanned a bin, and
      what would have to exist first
- [ ] `tests/test_boundary.py` — `TODO(me)`: a test asserting the `instructions` promise — no tool
      lists every bin
- [ ] `tests/test_boundary.py` — `TODO(me)`: the fifth smell for the path-leak test, and why it
      differs from the other four
- [ ] `stock_desk/store.py` — `TODO(me)`: is `tests/test_domain.py`'s direct `Store` import a
      boundary breach, and what rule decides

## Check

- [ ] The day's check is green: `./run check` — `All checks passed!`, `30 passed`, five `ok` lines
- [ ] Ran `uv run pytest tests/test_boundary.py -v` and read all six test names
- [ ] Ran the round trip in part 2.2 and confirmed the protocol version, server identity, derived
      schema, and both the found and not-found replies
- [ ] **Break it on purpose, watch it go red, fix it.** Add a second tool and watch
      `assert tools == ["fetch_bin"]` fail. Add a `"file"` key to the reply and watch the path-leak
      test name it. Point `StdioServerParameters` at a misspelled module and read
      `MCPError: Connection closed`. Put every one back.
- [ ] **The failure that stays quiet.** Add the `print` from part 3.2, run `./run check`, confirm
      it is green, and compare the suite's reported duration against a clean run. Take the print
      out.
- [ ] `python p.py depth 02 3` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own days 0 through 2
- [ ] `stock_mcp` imports from `stock_desk`; `stock_desk` never imports `stock_mcp`

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the eight rows
      in the hub §10
- [ ] The `docs/PINS.md` supersession row is written, correcting the earlier "P02 cannot run it"
      claim now that day 3 has
- [ ] No `docs/SOURCES.md` row is owed — nothing with a citation identifier was cited
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
