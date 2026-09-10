# Progress ledger — Prayoga

Append-only. **The last row of the v4 table is where we actually are.** One row per *completed*
day, pasted from that day hub's §10 before `python p.py done NN D` will commit. A day with no row
here is not finished, whatever the folder looks like.

Nothing is ever deleted. A day that went wrong gets a note under its table saying what went wrong —
a ledger that only records successes is a ledger nobody can learn from, and the notes under the v3
table below are the proof of that.

---

## The v4 ledger — plan v4.0.0

Days are numbered **inside their project, from 0** (plan §15). Order inside a project is strict;
order between projects is free. This is the only region `python p.py` reads.

<!-- granth:ledger:start -->

| Project | Day | Date | Title | Parts | Commit | Gates green? |
| ------- | --- | ---- | ----- | ----- | ------ | ------------ |
| 01 | 0 | 2026-09-10 | The machine and the repository | 8 | <hash> | yes |
| 01 | 1 | 2026-09-10 | The skeleton and the kit | 9 | <hash> | yes |
| 01 | 2 | 2026-09-10 | The domain and its data | 6 | <hash> | yes |
| 01 | 3 | 2026-09-10 | The boundary, part one | 5 | <hash> | yes |
| 01 | 4 | 2026-09-10 | The boundary, part two | 5 | <hash> | yes |
| 01 | 5 | 2026-09-10 | Tools | 5 | <hash> | yes |
| 01 | 6 | 2026-09-10 | The tool that must refuse — a deficiency is an answer, not an error | 5 | <hash> | yes |

<!-- granth:ledger:end -->

> **Note on what a v4 row means, decided 2026-09-10.** The plan §15 says a row means a *completed*
> day. In practice, in this repository, rows have always been appended **when the day was written**,
> with the day's `CHECKLIST.md` boxes still unticked — that is what the notes under the v3 table
> below record, and it was confirmed as the convention before P01 day 1 was written. So: **a row
> here means the day document exists and its gates are green. The day's `CHECKLIST.md` is the
> record of what has actually been built and understood**, and `python p.py done NN D` still
> refuses on an unticked box. Where the two disagree, the checklist is the truthful one.
>
> **P01 day 0.** Written 2026-09-10. Eight parts, three sections. Every file it prints was built and
> run in a throwaway directory outside this repository and deleted afterwards (plan §0 rule 5); every
> transcript in it was observed on 2026-09-10, including the deliberate failure — the forced
> `git add -f .env`, the two red checks, the untracking, and the key still readable from history.
> `python p.py depth 01 0` and `python p.py check` are green. The commit hash is `<hash>` because the
> row was written before the commit existed; it is filled in from the commit that lands the day.
> **Its checklist is unticked at the time of writing**, and the day has no provider key involved at
> all — it makes no model call.
>
> **P01 day 1.** Written 2026-09-10. Nine parts, three sections. The whole tree — `pyproject.toml`,
> the package, the four kit modules, the model registry, the `run` driver and nine tests — was built
> and run in a throwaway directory outside this repository and deleted afterwards. `./run check` was
> green there (ruff, 9 passed, day 0's four checks), and every failure the day prints was caused on
> purpose and pasted verbatim: the `os error 396` hardlink failure in a cloud-synced folder, pytest's
> `ModuleNotFoundError` under `package = false`, the em-dash mojibake in the driver's output, the
> four kit error messages, the shared-dictionary budget leak, and the red gate after the model
> registry was broken. **One transcript in part 2.2 was written before it was run, caught on review,
> and replaced with the real output** — the nested-redaction example. It is recorded here because a
> ledger that only records successes teaches nothing.
>
> Still no provider key and still no model call: `claims_desk/models.py` names two models and
> contacts neither. **Its checklist is unticked at the time of writing.**
>
> **P01 day 2.** Written 2026-09-10. Six parts, three sections. The fixture set, the domain types,
> the store and ten tests were built and run in a throwaway directory outside this repository and
> deleted afterwards; `./run check` was green there with 19 tests.
>
> **Two mistakes were made writing this day and both are worth recording.** The rules originally
> decided injury by scanning the description, and the very first notification — "Plumber has been
> and capped it. No one hurt." — came out as a deficiency. That was found by the fixture set on the
> first run, and the fix was not a longer word list but a signature change: `assess` now takes the
> injury as a fact and reads no English at all. The failure became part 3.2, and it is the argument
> for a model existing in this project.
>
> The second was in the test file. `test_every_deficiency_names_a_reason_the_desk_can_produce`
> asserted `len(set(reasons)) == 8`, which **does not catch a duplicate**: nine deficiencies with
> eight distinct reasons passes it. It was found while trying to demonstrate the failure — the
> thirteenth notification was added and the test went green. The assertion now checks
> `len(reasons) == len(set(reasons))` as well, and both the printed file and the transcript in part
> 3.1 are the corrected ones.
>
> Still no provider key and still no model call. **Its checklist is unticked at the time of
> writing.**
>
> **P01 day 6.** Written 2026-09-10. Five parts, three sections. `./run check` green with 56 tests.
> This is the day the desk first runs end to end: `{"deficiency": 4, "fast-track": 0, "pending": 8}`
> over the real queue, writing exactly four claim files through the boundary.
>
> **Two real numbers came out of it.** The full pass takes **91.4 seconds** for twelve
> notifications — about twenty-eight boundary calls, each a fresh connection and therefore a fresh
> interpreter — which is day 9's argument made concrete rather than asserted. And the same eleven
> tests run in about five seconds in-process, because the fixture swaps `boundary.connected` and
> nothing else.
>
> **The day's deliberate failure was a real bug in this project's own code.** `run_queue` called
> `record_decision` and discarded the answer, so when the boundary refused all four writes — as
> data, correctly — the desk reported four deficiencies against an empty claims directory, with no
> error anywhere. It was found by running the queue with a deliberately wrong reason code. The fix
> reads the answer and escalates; a regression test now calls through to the real boundary with a
> bad argument and asserts on the escalation. That failure is the honest counterweight to days 5 and
> 6 both arguing that refusals should be data: **if refusals are data, somebody has to read the
> data.**
>
> One reference was corrected before it shipped: part 3.2 first quoted a throwaway `_probe.py` that
> the learner would not have, and now carries an inline command that was run as printed.
>
> This is the **last day with a zero request budget**. Day 7 makes the first model call, and the
> eight pending notifications are what it will be spent on.
>
> **P01 day 5.** Written 2026-09-10. Five parts, three sections. Built and run in the same throwaway
> directory and deleted afterwards; `./run check` green there with 45 tests, of which 14 are the new
> in-process tool tests running in about four seconds.
>
> The docket went from one tool to four and the tools moved into `claims_mcp/tools.py`, leaving
> `server.py` as wiring. **The boundary's version assertion went red for the second day running** —
> `0.2.0` to `0.3.0` — and this time the docket assertion was moved out of `tests/test_boundary.py`
> into `tests/test_tools.py` rather than updated, because the same claim in two files means one of
> them stops being maintained.
>
> **The day's strongest finding was not planned.** A tool that raises loses its message entirely:
> `read_decision` raising `KeyError("no decision recorded for FNOL-4471")` reaches the caller as
> `is_error: true`, `structured_content: null`, and the text `Error executing tool read_decision`.
> The SDK wraps arbitrary exceptions in `UnexpectedToolError` and forwards nothing — correct
> behaviour, since an exception may carry a path or another policyholder's data, and it means
> anything a caller needs must be a return value. That is the day's deliberate failure and it sets
> up day 6.
>
> **One invented claim was corrected before it shipped.** Part 3.1's `test_an_answer_arrives_twice_over`
> was described as a guard that could fail; running it showed it **cannot** currently fail, because
> every tool lets the SDK derive both copies from one return. The part now says so plainly and the
> rep is to make it fail once on purpose.
>
> Still no provider key and still no model call. **Its checklist is unticked at the time of
> writing.**
>
> **P01 day 4.** Written 2026-09-10. Five parts, three sections. Built and run in the same throwaway
> directory as day 3 and deleted afterwards; `./run check` green there with 31 tests. The suite is
> now noticeably slow — 19.43s against 1.66s on day 3 — and almost all of it is subprocess startup,
> which the day says out loud rather than hiding.
>
> **The day's finding was not planned.** Driving the HTTP endpoint by hand with `curl` showed that
> the SDK's Streamable HTTP transport **defaults to the session-based mode** the `2026-07-28`
> revision removed: without `stateless_http=True` a bare request gets `400 Bad Request`, an
> `mcp-session-id` header and `Missing session ID`. Worse, the same server answers an `initialize`
> handshake with `"protocolVersion":"2025-11-25"` while the Python client reports `2026-07-28`.
> Both are honest: the era is a property of the exchange. And **no test in this project would notice
> if `stateless_http=True` were deleted**, because every test connects in-process or over stdio.
> That gap is the day's deliberate failure and the first rep in its build brief.
>
> The modern per-request envelope was discovered the same way, one refusal at a time: `_meta` must
> carry both `io.modelcontextprotocol/protocolVersion` and `io.modelcontextprotocol/clientCapabilities`,
> and an `mcp-method` header must match the body's method. Only then does `server/discover` answer.
>
> **Day 3's version assertion went red, correctly.** Adding a resource and a prompt moved the
> boundary from `0.1.0` to `0.2.0`, and `tests/test_boundary.py` caught it — the first time that
> assertion could have earned its place, it did. Two invented claims were corrected against real
> output before they shipped: the connection-refused error is `httpx2.ConnectError`, not `httpx`,
> and a resource leak that *replaces* the peril keys fails with an unhelpful `KeyError` rather than
> the containment assertion, so the demonstration was changed to one that adds the leak alongside.
>
> Still no provider key and still no model call. **Its checklist is unticked at the time of
> writing.**
>
> **P01 day 3.** Written 2026-09-10. Five parts, three sections. The boundary was built and run in a
> throwaway directory outside this repository and deleted afterwards; `./run check` was green there
> with 25 tests, one of which launches `python -m claims_mcp` as a real subprocess.
>
> **The freshness check moved a fact.** `mcp` 2.2.0 now exists and speaks the current revision
> `2026-07-28`, which was not executable when the earlier boundary work was written. P01 therefore
> runs the current era and writes its own client, and `google-adk` is installed without its `[mcp]`
> extra so the `mcp<2` pin never applies. That decision, its cost — ADK's `McpToolset` is never used
> in this project — and what would make it worth revisiting are `docs/adr/ADR-0009`.
>
> **Three claims written before they were run turned out to be wrong**, and all three were corrected
> against real output rather than kept: an unknown tool comes back as a failed *result*
> (`Tool 'read_file' failed: ...`) rather than raising; a bad module name gives the client only
> `MCPError: Connection closed`, not a message about the module; and removing a parameter's type
> annotation does **not** produce a schema without a type — the SDK falls back to string, so that
> test still passes. The last one changed what part 3.1 teaches.
>
> **The day's deliberate failure is the one the gate cannot see.** A `print` inside a tool corrupts
> the stdio wire, the client logs `Invalid JSON: expected value at line 1 column 1`, skips the line,
> and answers correctly — and all twenty-five tests pass. The only visible difference was the
> suite's reported duration: `8.30s` against `1.66s`. That is in part 3.2 with both numbers.
>
> One environment problem is worth recording because it cost real time and is not a curriculum
> issue: the throwaway build was first placed at a path deep enough that `.venv` exceeded Windows'
> 260-character limit, and the symptom was `FileNotFoundError` from Python for a file the shell
> could read. The build was moved to a short path. It is in the day's traps because the learner's
> own repository sits under a similarly deep path.
>
> Still no provider key and still no model call. **Its checklist is unticked at the time of
> writing.**

---

## The v3 ledger — superseded, kept verbatim

Everything below this line was written under plan v3.1.0 and is **history, not progress**. Its
eighteen days were archived unedited to `days/_archive-v3/` and `projects/_archive-v3/` when v4
landed; the reasons are in `docs/adr/ADR-0007-v3-days-archived-and-the-restart.md`, and the reason
v4 exists at all is in `ADR-0006`. These rows are not counted by any tool and are never edited —
a superseded row is the only evidence of what was superseded.

The `IDs closed` column refers to the v3 curriculum ID scheme, which v4 deleted.

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
| 13 | 2026-09-10 | MC-02 | 4 | <hash> | yes |
| 14 | 2026-09-10 | MC-03 | 4 | <hash> | yes |
| 15 | 2026-09-10 | MC-04 | 4 | <hash> | yes |
| 16 | 2026-09-10 | MC-05 | 4 | <hash> | yes |
| 17 | 2026-09-10 | MC-06 | 4 | <hash> | yes |


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

> **Note on days 13 to 17 — the MCP boundary.** Written in one sitting, in parallel, against an
> implementation built and verified first. Every printed block was afterwards checked byte-for-byte
> against the files on disk, both project gates are green, and `python p.py check` is green across
> eighteen days.
>
> **These five days need no provider key at all**, which is new. Everything they teach runs against
> the boundary: the handshake driven by hand over stdio, the stateless and stateful servers
> answering four `curl`s, the transports, the tool declarations, and the client fetching tools
> across a real process line. The only path in P02 that would contact a provider is
> `parts_counter.agent.ask`, and no day runs it. **No model answer appears anywhere in P02.**
>
> **The era gap is the thing to remember about this phase.** The freshness check found that the
> current MCP specification revision is `2026-07-28`, which removed the `initialize` handshake,
> removed protocol-level sessions and the `Mcp-Session-Id` header, and made every request carry its
> own version and capabilities. The stack this curriculum can run cannot speak it: `google-adk`
> 2.8.0 declares `mcp<2`, and the 1.x line performs a handshake. So these days teach the era they
> can execute and quote, in the body of each day, the specification line that removed the mechanism
> being taught. That decision, its cost and what it owes are `docs/adr/ADR-0005-mcp-era-gap-and-the-1x-pin.md`.
> **The plan needed no amendment** — §12 already gives day 15 the title "the old handshake as
> history", which is exactly what happened.
>
> **Three of the five writing sessions were cut off by a rate limit** partway through, on
> 2026-09-10. Days 13 and 15 finished; days 14 and 16 had all four parts written but their
> `CHECKLIST.md` files were still templates; day 17 was missing its last part and its hub. Those
> gaps were finished by hand afterwards and are not a different standard of work — but the day-17
> part 2.2 transcripts were re-run from scratch rather than inherited, and the two checklists were
> written against each day's own §5 and §6 rather than reconstructed from memory. The interrupted
> agents left `projects/` clean, which was checked before anything else.
>
> As with every day so far, these rows were appended when the days were written, and their
> `CHECKLIST.md` boxes are unticked at the time of writing.
