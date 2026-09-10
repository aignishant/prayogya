# P01 day 3 — definition of done

`python p.py done 01 3` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-why-a-boundary/1.1-clerk-and-the-file-room.md` — read · ran its check · answered
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

- [ ] `uv add "mcp==2.2.0"` — and it landed in `dependencies`, not in the `dev` group
- [ ] `claims_mcp/__init__.py` — the package, and the docstring that says what it costs and buys
- [ ] `claims_mcp/server.py` — one server object, one declared tool, cover and no paths in the reply
- [ ] `claims_mcp/__main__.py` — four lines, and nothing else in the file
- [ ] `run` — the marked diff from part 2.2: `mcp` added to `COMMANDS`, removed from `PLANNED`
- [ ] `tests/test_boundary.py` — six tests, five in-process and one over a real subprocess
- [ ] `PACKAGES.md` — a dated row for `mcp==2.2.0` with the command you read the version from
- [ ] `claims_mcp/server.py` — `TODO(me)`: delete every returned field no rule reads
- [ ] `claims_mcp/server.py` — `TODO(me)`: decide whether the boundary should log who asked
- [ ] `tests/test_boundary.py` — `TODO(me)`: assert the `instructions` are true
- [ ] `tests/test_boundary.py` — `TODO(me)`: the smell that would have caught `holder_ref`
- [ ] Your own notes — `TODO(me)`: is `tests/test_domain.py` importing `Store` a breach or a
      legitimate test of the far side?

## Check

- [ ] The day's check is green: `./run check` — `All checks passed!`, `25 passed`, four `ok` lines
- [ ] **Break it on purpose, watch it go red, fix it.** Add a second tool to the boundary — any
      tool — and run `./run test`. Expect `Left contains one more item`. Delete it.
- [ ] **The break that does not go red.** Put `print(f"looking up {number}")` in `fetch_policy`, run
      the subprocess round trip and find `input_value='looking up SYN-POL-1001\r'` in the client's
      traceback. Then run `./run check`, watch it pass, and compare the suite's reported duration
      with the run before. Take the print out.
- [ ] Ran `./run mcp` and understood why nothing appears to happen
- [ ] Measured the blast radius in your own project and wrote the number down — day 16 asks for it
- [ ] `python p.py depth 01 3` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path — and the one change to
      an earlier file, `run`, is a marked diff naming day 1 part 1.3 as the day that printed it
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own earlier days
- [ ] `claims_mcp` imports `claims_desk`, and `claims_desk` imports nothing from `claims_mcp`

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the eight rows
      in the hub §10, restated definitions included
- [ ] `docs/PINS.md` has the dated MCP specification row from the hub §10, and this project's
      `PACKAGES.md` has the `mcp==2.2.0` row
- [ ] No `docs/SOURCES.md` row is owed — the specification was read as a live page, recorded in the
      hub §9 with its date, and nothing was cited by identifier
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
