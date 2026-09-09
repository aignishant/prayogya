# Progress ledger — Prayoga

Append-only. **The last row is where we actually are.** One row per *completed* day, pasted from
that day hub section 10 before `python p.py done N` will commit. A day with no row here is not
finished, whatever the folder looks like.

Nothing is ever deleted from this table. A day that went wrong gets a note under it saying what
went wrong — a ledger that only records successes is a ledger nobody can learn from.

| Day | Date | IDs closed | Parts | Commit | Gates green? |
| --- | ---- | ---------- | ----- | ------ | ------------ |
| 0 | 2026-09-08 | RB-01, RB-02, RB-03 | 4 | <hash> | yes |
| 1 | 2026-09-08 | FN-01 | 4 | <hash> | yes |
| 2 | 2026-09-09 | FN-02 | 4 | <hash> | yes |


> **Note on day 0.** Every check, build rep and deliberate break in `CHECKLIST.md` was run and its
> real output observed: `doctor`, `depth 0`, `index`, `index --check`, `check`, `brief 5`, the
> `.python-version` pin read-back, `git check-ignore -v .env`, the `granth.toml`
> `require_failure_part` toggle, and both breaks — the deleted `## In production` heading and the
> removed `failure: true` — each seen red and restored to green. The four *Say out loud* reps in
> the parts' `Check yourself` sections were **not** performed by the learner; the boxes asserting
> them were ticked on the learner's instruction. The commit hash column reads `<hash>` because
> `done` requires this row before the commit it would name exists.

> **Note on day 1.** The row above was appended when the day was written, and its 23 `CHECKLIST.md`
> boxes stayed unticked afterwards. On 2026-09-09, before day 2 was written, the learner confirmed
> the day was done and instructed that the boxes be ticked; they were ticked on that instruction
> rather than observed one by one. What that means precisely: the day-1 document's own transcripts
> were run and observed when it was written — `uv python list`, `where python`, `uv python find`,
> `uv init --bare`, `uv sync`, `uv add platformdirs`, the `uv run --python 3.11` refusal, the
> `requires-python = ">=3.99"` sync error, the removed `pyvenv.cfg`, and the `python` against
> `uv run` disagreement — and the observations are dated in that hub's §9. The *learner's* reps in
> §5 and the four *Say out loud* questions were not separately witnessed here. The same caveat as
> day 0 therefore applies to this row, and it is recorded rather than smoothed over.
