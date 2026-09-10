# P01 day 4 — definition of done

`python p.py done 01 4` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-two-transports/1.1-server-as-a-url.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/01-two-transports/1.2-resources-and-prompts.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/02-the-client/2.1-desks-side-of-the-line.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/02-the-client/2.2-what-crosses-tested-twice.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/03-the-era/3.1-two-eras-one-server.md` — read · ran its check · answered its question
      out loud

## Build

- [ ] `claims_mcp/__main__.py` — the transport switch, with `stateless_http=True` **explicit**
- [ ] `claims_mcp/server.py` — the resource, the prompt, and `version="0.2.0"`
- [ ] `run` — the marked diff from part 1.1: argument forwarding for single-step commands
- [ ] `claims_desk/boundary.py` — `target()`, `connected()`, `fetch_policy()`, and nothing else
- [ ] `tests/test_transports.py` — six tests
- [ ] `tests/test_boundary.py` — the version assertion updated to `0.2.0`, **after** the gate told
      you to
- [ ] `tests/test_transports.py` — `TODO(me)`: a test that actually speaks HTTP
- [ ] `claims_desk/boundary.py` — `TODO(me)`: a read timeout, and why that is half an answer
- [ ] `claims_desk/boundary.py` — `TODO(me)`: measure a connection per call, both transports
- [ ] `claims_mcp/server.py` — `TODO(me)`: `listChanged` is advertised and never sent
- [ ] Your own notes — `TODO(me)`: what would have to be true before binding anything but loopback

## Check

- [ ] The day's check is green: `./run check` — `All checks passed!`, `31 passed`, four `ok` lines
- [ ] **Break it on purpose, watch it go red, fix it.** Add the policy numbers to the peril resource
      **alongside** the perils, and expect `assert not True` from the containment assertion. Then
      try replacing the peril keys instead, and notice the failure is a `KeyError` that reads like a
      broken resource rather than a leak. Put it back.
- [ ] **The break that cannot go red.** Remove `stateless_http=True`, run `./run check`, and watch
      it pass. Then `curl` the endpoint and read `Bad Request: Missing session ID`. Put it back, and
      write the missing test — it is the first rep in the hub §5.
- [ ] Drove the wire by hand: a bare `tools/list`, an `initialize`, and `server/discover` with the
      full `_meta` envelope. Read the two different protocol versions this server reported.
- [ ] Ran the desk with and without `CLAIMS_BOUNDARY` and saw one log field differ
- [ ] `python p.py depth 01 4` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path — and the two changes to
      earlier files, `run` and `tests/test_boundary.py`, are marked diffs naming the day of THIS
      project that printed each original
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own earlier days
- [ ] `claims_desk/boundary.py` imports nothing from `claims_mcp`, and opens no file

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the ten rows in
      the hub §10, restated definitions included
- [ ] No `docs/PINS.md` row is owed — nothing was installed today
- [ ] No `docs/SOURCES.md` row is owed — nothing with a citation identifier was cited
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
