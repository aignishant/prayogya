# Progress ledger — Prayoga

Append-only. **The last row is where we actually are.** One row per *completed* day, pasted from
that day hub section 10 before `python p.py done N` will commit. A day with no row here is not
finished, whatever the folder looks like.

Nothing is ever deleted from this table. A day that went wrong gets a note under it saying what
went wrong — a ledger that only records successes is a ledger nobody can learn from.

| Day | Date | IDs closed | Parts | Commit | Gates green? |
| --- | ---- | ---------- | ----- | ------ | ------------ |
| 0 | 2026-09-08 | RB-01, RB-02, RB-03 | 4 | <hash> | yes |

> **Note on day 0.** Every check, build rep and deliberate break in `CHECKLIST.md` was run and its
> real output observed: `doctor`, `depth 0`, `index`, `index --check`, `check`, `brief 5`, the
> `.python-version` pin read-back, `git check-ignore -v .env`, the `granth.toml`
> `require_failure_part` toggle, and both breaks — the deleted `## In production` heading and the
> removed `failure: true` — each seen red and restored to green. The four *Say out loud* reps in
> the parts' `Check yourself` sections were **not** performed by the learner; the boxes asserting
> them were ticked on the learner's instruction. The commit hash column reads `<hash>` because
> `done` requires this row before the commit it would name exists.
