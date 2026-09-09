# P01 · Ask Desk

**What it is.** An internal IT ask desk that answers questions from a synthetic knowledge base, at
$0, built twice — once by hand with the standard library and no framework, then again with Google
ADK — so that the second version is understood rather than merely copied.

**Days.** 7 · **Deploy tier.** D1 (`api_server`, `/healthz`, run locally) · **Depends on nothing.**

## Triad

| Leg | This project |
| --- | --- |
| **Tools** | `search_notes(query, limit)` · `fetch_note(note_id)` · `check_service_status(service)` |
| **MCP boundary** | *none — leg 2 arrives in P02.* The tools read this project's own synthetic JSON directly, and day 1 of P02 is about why that is a problem worth solving. |
| **Cast** | one agent. Two is an architecture, and that is P03. |

## Borrowed concepts — taught deeply elsewhere, recapped here

| Concept | Recap in | Deep version (optional reading) |
| --- | --- | --- |
| Reading a key, and the three states of one | `PRIMER.md` §1 | `days/00-foundry/day-03-keys-pinning-refusing-check/parts/01-the-key/1.2-three-states-and-the-one-you-cannot-check.md` |
| A floor is not a pin | `PRIMER.md` §2 | `days/00-foundry/day-03-keys-pinning-refusing-check/parts/02-the-pin-and-the-refusal/2.1-a-floor-is-not-a-pin.md` |
| The exit status is the verdict | `PRIMER.md` §3 | `days/00-foundry/day-03-keys-pinning-refusing-check/parts/02-the-pin-and-the-refusal/2.2-the-check-that-could-not-refuse.md` |

**New here:** the stateless request/response turn · the conversation you carry yourself · JSON
function declarations · the tool-result turn · a bound on provider calls · ADK `Agent`, `Runner`
and `SessionService` · `FunctionTool` and what it derives from a plain function.

## Why this project uses `generateContent` and not the Interactions API

The provider recommends a newer, stateful Interactions API for new development, and says in the
same sentence that `generateContent` "remains fully supported" — checked 2026-09-09 at
`https://ai.google.dev/gemini-api/docs/migrate-to-interactions`. This project deliberately uses the
older, **stateless** endpoint, because the stateless one is the version in which the agent loop is
your own code: you hold the conversation, you resend it, and you can watch what happens when you
do not. The stateful API does that part for you, which is excellent for shipping and useless for
learning it.

Build first, compare after. The comparison is owed, and
`docs/adr/ADR-0004-generatecontent-by-hand-and-unpublished-limits.md` records that it has not been
scheduled yet.

**Done when.** `python run.py check` is green on a bare machine; the hand-rolled desk and the ADK
desk answer the same question the same way; and the first eval goes red on purpose.
