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
| 8 | 2026-09-10 | AG-03 | 5 | <hash> | yes |
| 9 | 2026-09-10 | AG-04, RS-01 | 4 | <hash> | yes |
| 10 | 2026-09-10 | DP-01, EV-01 | 5 | <hash> | yes |
| 11 | 2026-09-10 | FN-04 | 4 | <hash> | yes |
| 12 | 2026-09-10 | MC-01 | 4 | <hash> | yes |


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

> **Note on ticking days 4 to 7.** On 2026-09-10, before day 8 was written, the learner confirmed
> the standing policy set on 2026-09-09 — tick on instruction, and record that it was on
> instruction — and the 118 boxes across those four checklists were ticked on that basis rather
> than observed one by one. The same caveat as days 0 to 3 applies, and the distinction is the one
> those notes already draw: **the documents' own transcripts were run and observed** when the days
> were written, and are dated in each hub's §9; the *learner's* `TODO(me)` reps in §5 and the
> *Say out loud* questions were not separately witnessed.
>
> **One correction was made after the fact, and it is the reason this note is worth reading.** Day
> 7 closed by stating that ADK never took the loop's bound over. That was wrong. `RunConfig` has
> `max_llm_calls`, defaulting to **500**, overridable by the `ADK_MAX_LLM_CALLS` environment
> variable, enforced by raising `LlmCallsLimitExceededError`, and disabled entirely by a
> non-positive value. The day was corrected on 2026-09-10 in commit `329653e` rather than patched,
> and the corrected lesson is sharper than the original: the framework owns a bound, sized to stop
> an infinite loop rather than to budget a question, and setting it is still yours. Day 8 causes
> the exception on purpose. The error was found by probing `RunConfig` while building day 8's
> material — which is the argument for building the code before writing the document, and also
> the argument for not trusting a day that has only been read.

> **Note on days 8 to 12.** Written in one sitting, in parallel, against implementations built and
> verified first — the same arrangement as days 4 to 7, recorded again because it is a deviation
> from the one-day rhythm and not a thing to get used to silently. Every printed block was checked
> byte-for-byte against the files on disk afterwards, and both projects' gates are green: P01 six
> checks, P02 six checks, `python p.py check` green across thirteen days.
>
> **What made these days unusually verifiable.** P01 gained `ask_desk/scripted.py`, a stand-in
> model subclassing ADK's `BaseLlm`. It replays a fixed script, so days 8 to 10 produce **real ADK
> events** — real streaming, real tool dispatch, a real bound firing, a real error propagating —
> with no key, no cost and exact reproducibility. It is labelled a test double in its own docstring
> and names itself `scripted/...` in every transcript it produces, so nothing it emits can be
> mistaken for a provider response. The still-missing half is unchanged: **no model answer appears
> anywhere in these five days**, and every place one would go carries `TODO(me)` with the exact
> command.
>
> **Five defects in the project code were found by writing the days, and that is the argument for
> this order.** Days 8 and 10 caught them; they are recorded here because a ledger that only lists
> what went well teaches nothing. (1) `run.py` had grown a module-scope `google.adk` import, undoing
> day 6's rule that `run.py check` must not load the framework — fixed, and day 8 now teaches the
> lazy import as the rule rather than the regression as a trap. (2) `api.py` imported `pydantic`
> and `google.genai` while `pyproject.toml` declared neither, both arriving transitively through
> `google-adk` — both now declared, and day 10 gained the lesson: if a file writes `import x`, `x`
> is in `pyproject.toml`. (3) `SETUP.md` said five checks and (4) `README.md` said four commands;
> both stale, both corrected. (5) `CODEMAP.md` still listed `evals/` as owed. A sixth was found in
> P02 and deliberately **left in place**: `parts_counter/util/keys.py` points at `PRIMER.md` §1,
> which is the right section in P01, where the file was copied from, and the wrong one here. Day 11
> prints the file with the stale pointer, names it on the same page, and makes correcting it a rep
> — because it is the exact drift that day's opening part argues the independence rule will cause.
>
> As with every day so far, these rows were appended when the days were written and their
> `CHECKLIST.md` boxes are unticked at the time of writing.

> **Note on ticking days 8 to 12.** On 2026-09-10, under the standing policy the learner set on
> 2026-09-09, the 168 boxes across those five checklists were ticked on instruction rather than
> observed one by one. The distinction those earlier notes draw still holds: **the documents' own
> transcripts were run and observed** when the days were written and are dated in each hub's §9;
> the learner's `TODO(me)` reps and *Say out loud* questions were not separately witnessed.
>
> Days 8 to 12 are unusual in how little of that caveat bites, and it is worth saying why. Those
> days introduced `ask_desk/scripted.py`, a stand-in model, so almost everything they teach runs
> with no key and reproduces exactly — the event stream, the streaming duplication, the bound
> firing, the error propagating, the evalset going red. The part still owed is unchanged and small:
> what a **real model** does. That remains `TODO(me)` in 84 places across days 4 to 12.
