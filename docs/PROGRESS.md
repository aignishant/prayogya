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
| 3 | 2026-09-09 | FN-03 | 4 | <hash> | yes |
| 4 | 2026-09-09 | AG-01 | 5 | <hash> | yes |
| 5 | 2026-09-09 | TL-01 | 4 | <hash> | yes |
| 6 | 2026-09-09 | AG-02 | 4 | <hash> | yes |
| 7 | 2026-09-09 | TL-02 | 4 | <hash> | yes |


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

> **Note on day 2.** The row above was appended when the day was written, and its 27
> `CHECKLIST.md` boxes stayed unticked afterwards. On 2026-09-09, before day 3 was written, the
> learner confirmed the day was done and instructed that the boxes be ticked; they were ticked on
> that instruction rather than observed one by one. What that means precisely: the day-2
> document's own transcripts were run and observed when it was written — the two `.gitignore`
> writes, `git check-ignore -v` from both the project and the repository root, the `-v` against
> plain exit-status disagreement, the `git add .env` refusal and the silent `-f` override, the
> negation moved above `.env.*`, the appended `!.env` overruling the root file, the staged
> `service-account.json` that `check-ignore` would not report, `--no-index` naming line 10,
> `git rm --cached`, and the `fatal: pathspec` exit `128` — and all of them are dated in that
> hub's §9. The *learner's* reps in §5 and the four *Say out loud* questions were not separately
> witnessed here. The same caveat as days 0 and 1 therefore applies to this row.

> **Note on day 3.** Every transcript in this day's documents was run on this machine on
> 2026-09-09 and its real output pasted: the `os.environ` / `.env` disagreement and the shell
> override, the default-argument bug that made the first draft of part 1.2 print three identical
> rows, the three-state probe, the unstripped-quote failure, the `if not os.environ.get(...)`
> misreport, the live `400 INVALID_ARGUMENT` from the Gemini endpoint with the synthetic key, the
> two floors resolving to 3.12.12 and 4.11.8, `uv python pin`, `uv add` with an exact specifier,
> `uv lock --check` refusing a stale lock, the four-green check at exit `0`, the `sys.exit`
> removal printing `1 problem(s)` at exit `0`, the `uv run` lockfile rewrite against `--frozen`,
> and the Windows `Access is denied` from `uv sync` inside `uv run`. The learner's `TODO(me)` reps
> in §5 and the four *Say out loud* questions were not performed; this row was appended when the
> day was written, as days 1 and 2 were, and its `CHECKLIST.md` boxes are unticked at the time of
> writing.

> **Note on days 4 to 7 — P01 Ask Desk.** These four were written in one sitting, in parallel, and
> that is a deviation from the one-day-at-a-time rhythm worth recording rather than smoothing over.
> What made it safe: the project's whole reference implementation was built and run **first**, so
> the four documents describe code that already existed and already passed `python run.py check`,
> and every day's printed code was afterwards checked byte-for-byte against the files on disk.
> Day 4's printed files were additionally lifted verbatim out of the document into a clean tree and
> run there — five checks green, exit `0` — which is what plan §5.1 rule 4 means by "runnable as
> printed". `python p.py depth` is green on all four, and `python p.py check` is green across the
> repository.
>
> **What was NOT observed, and it is a real gap.** There is no working provider key on this
> machine. Every transcript in these four days is either offline — request construction, tool
> dispatch, `FunctionTool` introspection, the model registry — or a genuine provider rejection
> (`400 INVALID_ARGUMENT`, "API key not valid"). **No model answer appears anywhere in these
> documents**, and every place one would go carries `TODO(me)` naming the exact command. That
> includes: what the model does when handed two consecutive `user` turns (day 4), the `role` the
> tool-result turn must actually carry and the `finishReason` of a successful function call (day
> 5), and what a model does when told a tool's purpose is "Call self as a function." (day 7).
> The days are complete as teaching; the live half is owed and is marked as owed.
>
> As with days 0 to 3, these rows were appended when the days were written, and their
> `CHECKLIST.md` boxes are unticked at the time of writing.
