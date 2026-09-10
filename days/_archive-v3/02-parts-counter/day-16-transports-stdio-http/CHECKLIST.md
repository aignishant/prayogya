# Day 16 — definition of done

`python p.py done 16` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-two-ways-to-carry-the-same-messages/1.1-the-transport-is-a-binding.md` — read · ran its check · answered its question out loud
- [ ] `parts/01-two-ways-to-carry-the-same-messages/1.2-stdio-a-subprocess-and-two-pipes.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-over-http/2.1-one-endpoint-one-post-per-message.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-over-http/2.2-the-transport-that-is-already-history.md` — read · ran its check · answered its question out loud

## Build

- [ ] `run.py` — `serve_mcp()` typed, and I said why `parts_mcp.server` is imported **inside** the function before checking my answer against what `run.py check` has to be able to do
- [ ] The two `main()` arms typed, and I ran `python run.py mcp --htp` (the typo) and can say which exit status it gives and why that is the right one
- [ ] I piped the three-message handshake into `run.py mcp`, counted the lines that came back, and said why it is not three **before** looking it up
- [ ] I can say, without re-reading, which line of `parts_mcp/server.py` differs between the two transports — and that the answer is none
- [ ] The `Accept` rep: `tools/list` sent with no `Accept` header, with both media types, and with `text/event-stream` alone — and I predicted the third before sending it
- [ ] The deprecation rep: server started with `transport="sse"` on port 8092, and I wrote down which of `/mcp`, `/sse` and `/messages/` I expected to exist and what each would return **before** probing. Server stopped afterwards.

## Check

- [ ] The day's check is green: `cd projects/02-parts-counter && uv run --frozen python run.py check` — six green, `0 problem(s)`
- [ ] `echo $?` after it prints `0`, and I ran it rather than assuming it
- [ ] `uv run --frozen python run.py probe` — four tools listed, one call returned
- [ ] **Break it on purpose, watch it go red, fix it.** Run the server with `transport="http"` and read the real `ValueError`. Restore.
- [ ] **Break it on purpose, watch it go red, fix it.** *(the day's deliberate failure)* Put `print("hello")` in a tool body in `parts_mcp/server.py`, run the handshake, and confirm what happens. Re-run with `PYTHONUNBUFFERED=1`. Then `print("hello", end="", flush=True)` and `run.py probe`. **Remove the line and re-run the clean handshake before moving on.**
- [ ] **Break it on purpose and watch nothing go red.** Start the server on the deprecated `sse` transport. It works. I can say why "still works" and "still a good idea" are different claims, and what the specification says about adopting it now.
- [ ] `python p.py depth 16` — green
- [ ] `python p.py check` — green across the whole repository
- [ ] Every server I started is stopped, and `git status --porcelain projects/` is empty

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — transport, stdio transport, Streamable HTTP, Server-Sent Events, deprecated
- [ ] `docs/PINS.md` — nothing to add today, and I can say why a project's own pins live in its `PACKAGES.md`
- [ ] `docs/SOURCES.md` — nothing to add today, and I can say why a living specification page is dated in the hub §9 instead
- [ ] Every specification quotation in this day names the revision it came from, and I checked rather than assumed
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10
- [ ] Committed with the message from the hub §10
