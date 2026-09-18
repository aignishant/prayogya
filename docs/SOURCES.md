# Source ledger — Prahari

Append-only. **Never invent a citation** (plan §11.4.1, rule 5). Every primary source a document
teaches or cites gets a row here, and the row is written **only after the record was opened
live** and the title copied from it rather than from memory.

This is the strictest of the three verification rules because it fails the most quietly. A wrong
version pin breaks the next install. A plausible identifier attached to the wrong title survives
for years, gets copied into other people's notes, and is never caught.

**Cite by title and identifier, never by author.** The identifier resolves to exactly one
document, and it is what a reader types.

Accepted identifier forms: `arXiv:2401.12345` · `doi:10.1145/3597503` · `RFC 9110` ·
`ISO/IEC 9899:2018` · `spec:<name>-<revision>`. Anything citation-shaped that matches none of
these is rejected by `python granth.py depth`.

| Identifier | Exact title | Year | URL | Record checked | Taught on | Cited by |
| ---------- | ----------- | ---- | --- | -------------- | --------- | -------- |
| `spec:mcp-2026-07-28` | Model Context Protocol — Specification (revision 2026-07-28) | 2026 | https://modelcontextprotocol.io/specification/2026-07-28 | 2026-09-18 | planned: day 45 | plan §5; day 43 onward |
