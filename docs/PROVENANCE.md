# Provenance ledger — Prayoga

Append-only. Every third-party thing this curriculum runs, vendors or depends on gets a row here
**before it is ever run** — source, licence, version, who audited it and when, and what it is
permitted to touch.

This is blast radius before capability, written as a table. A dependency you have not audited is a
capability you granted without deciding to. It matters more here than in most repositories,
because P12 audits third-party skills and P28 runs a deliberately hostile boundary: the discipline
being taught has to be visible in the repository doing the teaching.

| What | Source | Version | Licence | Audited on | Audited by | Permitted scope |
| ---- | ------ | ------- | ------- | ---------- | ---------- | --------------- |
| `p.py` | Written here on day 0. Standard library only; no third-party import. | day 0 | this repository | 2026-09-08 | the author | Reads and writes `docs/` and `days/`. Shells out only to `git`, only in `done`. |
