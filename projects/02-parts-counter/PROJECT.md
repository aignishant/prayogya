# P02 · Parts Counter

**What it is.** A workshop parts counter — find a part, read its stock, say which bin it is in, and
change the count — built first with its data reachable straight off the filesystem, and then moved
behind an MCP boundary, so the boundary is something you were argued into rather than told about.

**Days.** 8 · **Deploy tier.** D2 (stateless container, secrets injected not baked) ·
**Depends on nothing.**

## Triad

| Leg | This project |
| --- | --- |
| **Tools** | `find_part(query)` · `stock_level(part_no)` · `bin_location(part_no)` · `adjust_stock(part_no, delta)` |
| **MCP boundary** | `parts_mcp/` — owns the inventory. **This is the project that teaches it**, from day 3. Days 1 and 2 deliberately have no boundary, and day 2 is the demonstration of what that costs. |
| **Cast** | one agent. Two is an architecture, and that is P03. |

## Borrowed concepts — taught deeply elsewhere, recapped here

| Concept | Recap in | Deep version (optional reading) |
| --- | --- | --- |
| A floor is not a pin, and `-latest` is a floor | `PRIMER.md` §1 | `days/00-foundry/day-03-keys-pinning-refusing-check/parts/02-the-pin-and-the-refusal/2.1-a-floor-is-not-a-pin.md` |
| The exit status is the verdict | `PRIMER.md` §2 | `days/00-foundry/day-03-keys-pinning-refusing-check/parts/02-the-pin-and-the-refusal/2.2-the-check-that-could-not-refuse.md` |
| Reading a key, and the three states of one | `PRIMER.md` §3 | `days/00-foundry/day-03-keys-pinning-refusing-check/parts/01-the-key/1.2-three-states-and-the-one-you-cannot-check.md` |
| A tool declaration is derived from the function | `PRIMER.md` §4 | `days/01-ask-desk/day-07-functiontool-what-adk-does/parts/01-what-the-wrapper-reads/1.2-the-type-hints-are-the-schema.md` |
| The framework's bound is not your bound | `PRIMER.md` §5 | `days/01-ask-desk/day-07-functiontool-what-adk-does/parts/02-what-it-reads-that-you-did-not-mean-to-write/2.2-what-it-did-and-what-it-did-not.md` |

**New here:** a request budget that refuses rather than warns · structured logging with redaction at
the writer · the MCP boundary — the stateless core, lifecycle, transports, resources and the client
side · a data layer that survives two writers.

**Deliberately not built yet 🅿️.** Honest 429 backoff. This project's calls fail on a 429 rather
than retrying, and that is recorded rather than hidden: retry policy is P05's subject, and a retry
loop written before you have watched a quota run out is a retry loop that hides the thing it should
surface.

**Done when.** `python run.py check` is green on a bare machine; the inventory is reachable only
through `parts_mcp`; and `python run.py race` — the concurrent-write demonstration from day 2 —
stops losing parts once the boundary owns the file.
