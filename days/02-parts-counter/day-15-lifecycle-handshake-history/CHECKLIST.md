# Day 15 — definition of done

`python p.py done 15` refuses to commit while any box below is unticked. That refusal is the point:
a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-the-conversation-before-the-conversation/1.1-three-messages-before-any-work.md` — read · ran its check · answered its question out loud
- [ ] `parts/01-the-conversation-before-the-conversation/1.2-what-each-side-admits-to.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-negotiation-and-its-retirement/2.1-the-version-both-sides-can-speak.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-negotiation-and-its-retirement/2.2-the-handshake-as-history.md` — read · ran its check · answered its question out loud

## Build

Nothing is typed into `projects/` today. Every rep is drive-it-and-read-it, and the notes go in
`lab/`.

- [ ] `lab/handshake-notes.md` — ran the three-message handshake, then again with the notification and `tools/list` swapped, then again with an `"id"` added to the notification; recorded what changed and what did not
- [ ] `lab/handshake-notes.md` — sent `resources/read` after a good handshake, **predicted the outcome before running it**, and named the flag in the `initialize` result that should have told me
- [ ] `lab/version-notes.md` — offered `2025-03-26` and `2025-11-25`, predicted echo or counter-offer before each, and said what the pair reveals about this SDK's revisions
- [ ] `lab/version-notes.md` — wrote the one `if` that *"the client SHOULD disconnect"* reduces to, as pseudocode against the `initialize` result, and did **not** wire it into the project
- [ ] `lab/era-notes.md` — skipped the handshake, read both streams separately, and wrote one sentence on what a client would need to do differently to survive a `2026-07-28` server

## Check

- [ ] The project is unchanged: `git status --porcelain projects/` is empty
- [ ] The project's gate is still green: `cd projects/02-parts-counter && uv run --frozen python run.py check`
- [ ] The boundary's tests still pass: `uv run --frozen python -m pytest tests -q`
- [ ] **Break it on purpose, watch it go red, fix it.** Send `tools/list` into the server with no handshake in front of it. Read the `-32602` on standard output, read `Received request before initialization was complete` on standard error, and run `echo $?` — confirm the process exited **`0`**. Then put the two handshake messages back in front of it and watch the same request succeed.
- [ ] Caused the second failure too: `initialize` with `protocolVersion` omitted, then with it set to `null` — and found the one useful line in each wall of validation errors
- [ ] `python p.py depth 15` — green
- [ ] `python p.py check` — green across the whole repository

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — and I checked days 13 and 14 first, so no term is defined twice
- [ ] Every version or limit observed today has a dated row in `PACKAGES.md` or `docs/PINS.md` (today: none new — `mcp` 1.30.0 and the wire revision `2025-11-25` were recorded by day 13)
- [ ] Every source cited today has a dated row in `docs/SOURCES.md` (today: none — the specification revisions are dated in the hub §9)
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10
- [ ] Committed with the message from the hub §10
