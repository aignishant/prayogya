# Day 13 — definition of done

`python p.py done 13` refuses to commit while any box below is unticked. That refusal is the point:
a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-the-reframe/1.1-the-call-you-had-to-keep-open.md` — read · ran its check · answered its question out loud
- [ ] `parts/01-the-reframe/1.2-one-flag-two-protocols.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-the-era-you-are-standing-in/2.1-the-revision-that-deleted-the-handshake.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-the-era-you-are-standing-in/2.2-the-pin-that-had-to-be-argued-for.md` — read · ran its check · answered its question out loud

## Build

- [ ] `pyproject.toml` — I ran `uv add "google-adk[mcp]==2.8.0" "mcp==1.30.0"`, diffed the file against day 11's version, and can say in one sentence each what the brackets do and what the second line adds that the brackets alone would not
- [ ] `parts_mcp/server.py` — I wrote down my prediction for the stateless `initialize` result **before** running it, then ran it, and can name the field that surprised me and the header that is absent
- [ ] the two servers — I served the same file both ways and sent the identical `tools/call` to each with no session header, recorded both responses verbatim, and can say what a load balancer in front of two stateful replicas would have to do
- [ ] the two servers — I handed a made-up `mcp-session-id` to each server, can say what each did with it, and have found the sentence in the `2026-07-28` transports page that says which behaviour is now required
- [ ] the transport — I caused the `406` by dropping `Accept`, read the whole message, and can say why the transport cannot guess and what that means for an ordinary uptime checker
- [ ] the era — I sent `MCP-Protocol-Version: 2026-07-28`, counted the revisions the server offered back, and can say which one the specification currently calls current
- [ ] the pin — **the day's deliberate failure**, done in a throwaway project: `uv add "google-adk==2.8.0" "mcp==2.2.0"` resolved cleanly, both imports failed, and I wrote down which of the three messages I would rather receive and why
- [ ] the record — I wrote the three costs of a session in my own words without looking, each with the operational thing it forbids, and put the list where day 18 will find it

## Check

- [ ] The day's check is green: `cd projects/02-parts-counter && uv run --frozen python run.py check` — six green, `0 problem(s)`, exit `0`
- [ ] **Break it on purpose, watch it go red, fix it.** In a throwaway project, `uv add "google-adk==2.8.0" "mcp==2.2.0"`; watch it resolve with no conflict; watch `from mcp.server.fastmcp import FastMCP` fail with the message that names the rename, and `from google.adk.tools.mcp_tool import McpToolset` fail without ever mentioning `mcp`. Then add the brackets and watch the resolver refuse the pair. Delete the throwaway project.
- [ ] **Break it on purpose, watch it go red, fix it.** Serve `parts_mcp/server.py` with `mcp.settings.stateless_http = False` and call a tool with no session header: `Bad Request: Missing session ID`, HTTP 400. Then quote a session id the server never issued: `Session not found`, HTTP 404. Restore the flag by killing the process — nothing on disk changed.
- [ ] Both servers are killed, and `git status --porcelain` inside `projects/02-parts-counter` is empty
- [ ] `python p.py depth 13` — green
- [ ] `python p.py check` — green across the whole repository

## Record

- [ ] The five terms in the hub §10 have rows in `docs/GLOSSARY.md`, and neither `Stateless` nor `Session` was redefined
- [ ] The `spec:mcp-2026-07-28` row from the hub §10 is in `docs/SOURCES.md`, with the date it was fetched
- [ ] `docs/PINS.md` — nothing owed today, and I can say why (project pins live in `PACKAGES.md`, plan §9)
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10
- [ ] Committed with the message from the hub §10
