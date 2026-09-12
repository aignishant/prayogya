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
| 01 | 7 | 2026-09-10 | The first agent | 5 | <hash> | yes |
| 01 | 8 | 2026-09-10 | Sessions and state | 5 | <hash> | yes |
| 01 | 9 | 2026-09-10 | The cast | 6 | <hash> | yes |
| 01 | 10 | 2026-09-10 | The workflow runtime | 7 | <hash> | yes |
| 01 | 11 | 2026-09-10 | Callbacks and plugins | 6 | <hash> | yes |
| 01 | 12 | 2026-09-10 | Memory and retrieval | 6 | <hash> | yes |
| 01 | 13 | 2026-09-10 | Structured output | 4 | <hash> | yes |
| 01 | 14 | 2026-09-11 | The decision record: why this claim was fast-tracked, in a form an auditor accepts | 4 | <hash> | yes |
| 01 | 15 | 2026-09-11 | Reliability | 4 | <hash> | yes |
| 01 | 16 | 2026-09-11 | Security and privilege | 9 | <hash> | yes |
| 01 | 17 | 2026-09-12 | Observability | 7 | <hash> | yes |
| 01 | 18 | 2026-09-12 | Evals | 7 | <hash> | yes |
| 01 | 19 | 2026-09-12 | Ship | 7 | <hash> | yes |
| 02 | 0 | 2026-09-12 | The machine and the repository | 8 | <hash> | yes |
| 02 | 1 | 2026-09-12 | The skeleton and the kit | 9 | <hash> | yes |
| 02 | 2 | 2026-09-12 | The domain and its data | 6 | <hash> | yes |
| 02 | 3 | 2026-09-12 | The boundary, part one | 5 | <hash> | yes |

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
> **P01 day 7.** Written 2026-09-10. Five parts, three sections. `./run check` green with 66 tests.
> **The first model call in this curriculum's fourth project-day of agent work**, and the day the
> project's day-0 promise came true: the queue now runs `{"deficiency": 8, "fast-track": 4,
> "pending": 0}` with twelve claim files and eight distinct reasons, which is `PROJECT.md`'s
> `Done when` paragraph minus the cold clone and the eval.
>
> **`google-adk==2.8.0` installs cleanly without its `[mcp]` extra and `mcp` stays at 2.2.0**, which
> is ADR-0009's plan working in practice rather than in principle. Every API fact in the day was
> read off the installed package: `Agent is LlmAgent`, the `Runner` keyword-only signature,
> `BaseLlm` having exactly one field.
>
> **Every model call went to a stand-in**, and the day is built around making that impossible to
> forget: the double announces itself in its name (`scripted/`), in every answer (`scripted: true`)
> and to the registry, which admits it *because* of the prefix rather than by an exemption. The
> framework's own `Skipping missing token usage metadata` warning is quoted rather than silenced,
> because it is the list of things this project cannot learn from its own transcripts. The honest
> gap is a `TODO(me)` in the build brief: **run one notification against a real model and write down
> what differed.** Until that exists, this project has proved its own code and nothing about a model.
>
> **Nine tests from days 2 and 6 went red and were meant to.** `assess` now takes a `Cover` rather
> than a `Policy` — the boundary decided that shape on day 3 and the domain caught up four days
> later — `decide` takes a budget, and two tests were **deleted rather than weakened** because their
> subject no longer exists. One count was wrong in a first draft and corrected against a run:
> `tests/test_agent.py` has twelve tests, not thirteen.
>
> The ordering that matters: the classifier is asked **last**, so four of twelve notifications cost
> no model call at all, and a test asserts `budget.spent == 0` for one of them.
>
> **P01 day 8.** Written 2026-09-10. Five parts, three sections. `./run check` green with 78 tests,
> and the suite got **faster** — 25s to 8.6s — because the classifier stopped building a new session
> service on every call.
>
> Conversations are now addressed by the claim reference and kept in one service for the process, so
> two questions about a claim accumulate (2 events, then 4) and a question about another claim finds
> `None`. Session state carries a reference and refuses, by key name, anything that looks like a
> secret or a person's contact details — **refused rather than redacted**, because a log line can be
> redacted and a retained record cannot be un-kept.
>
> **Two claims written before they were run were wrong and were corrected against real output.**
> `tests/test_sessions.py` has twelve tests, not eleven. And disabling the isolation fixture does
> **not** leave the suite passing as first written: it produces `assert 4 == 2` in
> `test_a_failure_also_arrives_as_an_event_in_the_conversation`, which passes when run alone with
> `-k`. That is a better demonstration than the one drafted, and the part now carries it.
>
> The day's deliberate failure is the guard nobody would think to write. A model failure arrives
> **twice** — as a raised `RuntimeError` and as an error event with `is_final_response()` true and
> `content` of `None` — and removing `and event.content` from the read loop leaves every test green
> while turning the next provider outage into `AttributeError: 'NoneType' object has no attribute
> 'parts'` inside the parser, with the real cause nowhere in the traceback.
>
> Part 1.2 is honest about its own limit: the deny-list is about key names, so `caller_ref` and
> `notes` both walk past it, and so does `e_mail`. All three were run. The allow-list version is a
> rep rather than a claim.
>
> **P01 day 9.** Written 2026-09-10. Six parts, three sections — one more than planned, because the
> day turned up a real defect that deserved its own part. `./run check` green with 96 tests, up from
> 78, eighteen of them in the new `tests/test_cast.py`.
>
> The desk has two agents. The letter writer is given a claim reference, one reason and the sentence
> the department wrote, and the eight letters come from a table in the stand-in rather than from a
> model — so this project still knows nothing about how a provider would word one, which is the same
> honest gap day 7 opened. The boundary now keeps the letter with the decision and **refuses a
> fast-track that carries one**: `{"recorded": false, "refused": "a fast-track has no letter"}`.
>
> **A claim written in part 1.1 was false, and the probe that disproved it is now part 3.1.** The
> part said the letter writer is given three labelled lines and nothing else. It was not. Day 8's
> one-session-per-claim meant the second agent was replayed the first agent's whole exchange — the
> policyholder's own words, then the classifier's verdict inside the framework's quoted-agent guard,
> and only then its own question. **Every test in the project passed while this happened.** The only
> signal the framework gives is a WARNING line, `Event from an unknown agent: classifier`, which says
> nothing about what was shared and which nobody would act on.
>
> The fix is a `thread` parameter on `sessions.address`, `turn` and `stored`, so each agent gets its
> own conversation under the same claim reference — printed as a marked diff against day 8, with day
> 8's module docstring corrected in the same hunk rather than left contradicting its own code. Part
> 1.1 was rewritten to print the corrected file and to point forward at the failure rather than to
> keep its original claim. The regression test asserts on both directions: the description **is** in
> the classifier's thread and **is not** in the letter writer's.
>
> **The day's deliberate failure is that leak**, and deleting `thread=NAME` takes exactly one test
> red — verified, `1 failed, 17 passed`. The lesson the part actually teaches is the one that
> generalises: an agent's input is not the string you passed it, and if the input is a design
> decision it has to be asserted on directly.
>
> Part 2.1 drives the framework's own delegation for real — three events, `transfer_to_agent` as an
> ordinary tool call, `actions.transfer_to_agent` on the handover — and then argues that this desk
> should not use it for a claim decision, because *why did this claim go to correspondence* must be
> answerable by reading a rule. The framework's own warning about the cost is quoted verbatim: every
> transfer changes the prompt prefix and re-sends the whole prompt uncached. A test keeps the
> demonstration green so the decision stays a decision rather than an absence.
>
> The ceiling moved from two calls per notification to three, and part 3.2 is about why that is the
> right shape: one shared budget of three, not a budget each, because two budgets of three is a
> ceiling of six that nobody agreed to. Measured over the whole queue: 16 model calls, 42 subprocess
> boundary launches, 43.3 seconds, `claim files: 12 | with a letter: 8`.
>
> As with every day so far, this row was appended when the day was written, and its `CHECKLIST.md`
> boxes are unticked at the time of writing.

> **P01 day 10.** Written 2026-09-10. Seven parts, four sections — two more than planned, because
> the day turned up a deprecation that deserved its own part and a parallel arrangement that deserved
> its own measurement. `./run check` green with 110 tests, up from 96.
>
> The order the desk works in stopped being a `for` loop and became `claims_desk/workflow.py`: triage
> as a `SequentialAgent` over the classifier and a node that is code, correspondence as a `LoopAgent`
> that drafts, checks and redrafts with the objection attached, and the queue-at-once as a
> `ParallelAgent`. **Two agent modules lost thirty-four and thirty-one lines of orchestration** and
> neither agent changed — `classify` and `write` are gone, and the four jobs they did belong to
> whoever owns the order.
>
> **Twenty tests across three files went red and every one of them was the change working.** None was
> deleted to make it green: the parsing tests followed the parser into the workflow, the session
> tests dropped a budget they never needed, and two tests about `classify` spending a call were
> deleted outright because their subject no longer exists — with the test that now covers that ground
> named in the day.
>
> The repair loop is real and cheap: eleven of twelve letters pass the house style on the first
> draft, and one — `above_fast_track_limit` — is refused on a `2`, told *write it again with no
> figure of any kind in it*, and accepted at 165 characters. The queue costs 17 model calls, and the
> ceiling moved from 3 to 5 because the letter can now take three attempts.
>
> **The day's deliberate failure is the parallel queue's shared state**, and it is the quietest one
> this project has produced. Un-namespace the keys and twelve rules nodes run, twelve verdicts are
> computed, twelve correct log lines are emitted — and the session ends holding **one** of them, with
> no error, no warning and no way to tell which claim's verdict survived. The fix is two fields on
> the node and a key built from the claim reference.
>
> Two defects in the parallel version were measured rather than argued about, and both are asserted
> by tests **named for the fact that they are defects**: every branch shares the agent's name, so a
> per-author budget breakdown collapses to one entry; and a `ParallelAgent` fans out the invocation
> rather than the input, so all twelve branches read the same message and returned the same peril.
> That decides it — this desk keeps its sequential queue.
>
> **The finding that changed the day's shape was a line of stderr.** `SequentialAgent`,
> `ParallelAgent` and `LoopAgent` are all deprecated in `google-adk` 2.8.0 — the version this project
> pins — in favour of a graph-based `google.adk.workflow.Workflow` with real edges, conditional
> routing and plain Python functions as nodes. The successor was driven for real against this
> project's own classifier and it works; the conditional edge needed for the loop did not, and that
> is a `TODO(me)` carrying the exact lookup command rather than a guess. The decision to stay on the
> deprecated three, and its reasons, are `docs/adr/ADR-0010-p01-stays-on-the-composition-workflow-agents.md`.
>
> Two claims drafted before they were run were wrong and were corrected against real output. Part
> 2.1 first transcribed `drafts: 1` where the run said `drafts: 2`, and then explained a defect that
> did not exist; the paragraph is gone. Part 4.1 first claimed that removing the loop's bound turns
> two tests red — it turns **one** red, because
> `test_the_bound_is_what_stops_a_loop_that_cannot_converge` builds its own `LoopAgent` and therefore
> defends nothing about `correspondence()`. That is now the part's failure section and a `TODO(me)`.
>
> As with every day so far, this row was appended when the day was written, and its `CHECKLIST.md`
> boxes are unticked at the time of writing.

> **P01 day 11.** Written 2026-09-10. Six parts, four sections. `./run check` green with 124 tests,
> up from 110.
>
> The budget moved out of day 10's event-counting and into a plugin's `before_model_callback`, which
> is the one place every agent's request passes through. `charge` is deleted and with it three
> assumptions, the worst of which was `event.partial is not True` — a guess about streaming written
> by somebody who had never seen this project stream. The number is now an observation rather than a
> reconstruction, and because the hook can replace a call, the budget stopped being a record and
> became a limit.
>
> **The day's deliberate failure was not planned: it happened while the budget was being moved.** The
> obvious code kept day 7's decision that `BudgetExceeded` raises. It does raise — and the framework
> catches whatever comes out of a plugin and re-raises its own
> `RuntimeError: Error in plugin 'claims-desk' during 'before_model_callback' callback: ...`, so
> `except BudgetExceeded` in `desk.decide` stopped catching anything and that whole branch went dead.
> An over-budget claim would have stopped the morning's queue instead of going pending.
>
> **Two tests failed and neither was the thing that broke.** `desk.decide`'s over-budget path had no
> test driving a real claim to its limit; it had only ever been reached by a unit test calling the
> budget directly. That test now exists — `test_a_refused_claim_goes_pending_and_names_the_reason`,
> four lines — and it is the day's most useful artefact. The general form is in part 3.1: a branch
> reached only through a framework's extension point is a branch unit tests do not reach.
>
> The refusal is now a returned `LlmResponse` and a name on a list, `run_triage` reports
> `OVER_BUDGET`, and the desk checks it **before** the general failure branch — because a claim that
> went pending for want of allowance should be re-run and a claim whose model answered badly should
> be looked at, and without the check both arrive as `needs_classification`. That was verified by
> deleting the check and watching the wrong reason appear silently.
>
> Day 9's leak got a second lock: `refuse_the_description`, an agent callback on the letter writer
> alone, which refuses any request carrying the policyholder's own words. Day 9's threads are a
> convention enforced by two strings differing; this is enforced on the request. **What it costs was
> measured rather than assumed** — a refused leak spins the repair loop its full three passes and
> charges three of the claim's five calls, because the plugin charges before the agent callback
> refuses. The function's docstring first said a leak costs nothing; it now says three drafts, and
> the test asserts `{"letter_writer": 3}`.
>
> Two smaller findings worth keeping. `ruff` rule `B039` refused a mutable `ContextVar` default,
> which would have leaked one run's refusals into the next — the second time a lint rule this project
> did not choose has caught a real bug. And the desk's own budget now bites **before** day 10's
> `max_llm_calls`, because the ceiling is derived from the same budget the plugin spends; the
> framework's net is still set and is no longer what stops anything, which is an improvement and is
> stated rather than left to be discovered.
>
> As with every day so far, this row was appended when the day was written, and its `CHECKLIST.md`
> boxes are unticked at the time of writing.

> **P01 day 12.** Written 2026-09-10. Six parts, four sections. `./run check` green with 141 tests,
> up from 124, and **no earlier test went red** — the first day since day 7 that adds without
> rewiring.
>
> **The build tree had to be reconstructed before this day could start.** The previous batch deleted
> it, as the rules require, so P01 was rebuilt from its own day documents — which is exactly what the
> learner does, and it found two Completeness Rule violations that the original build had hidden.
> `claims_desk/boundary.py` grew `call`, `check_in_force`, `record_decision` and `read_decision`
> across days 5 and 6 and **no day printed any of them**; and `claims_desk/agents/__init__.py` is
> never printed at all, although day 7's hub says to "type it from part 1.1's setup". Both are now
> fixed in the days that owed them: a marked diff of `boundary.py` in day 5 part 1.2, its `letter`
> parameter in day 9 part 1.2, and the agents package printed in day 7 part 1.1. The rebuilt tree
> reaches the same headline numbers — `{'fast-track': 4, 'deficiency': 8, 'pending': 0}`, twelve
> claim files, eight letters — which is what says the reconstruction is faithful.
>
> The day itself: a synthetic claims handbook of eight rules, one identifier each, split at its own
> headings; a retriever made of term frequencies, inverse document frequency and a cosine, with no
> provider and no embedding anywhere; citations that resolve; and `recall@k` measured against ten
> hand-written questions. **No model call at all**, which is the point rather than an omission.
>
> The numbers are honest and unflattering in places. `recall@1` is 0.700, `recall@2` 0.800,
> `recall@3` 0.900. The highest score anywhere in the day — `0.406` — is on a **wrong** answer, for
> the question about quoting the fast-track limit. And the one question that fails at every k was
> investigated rather than described: the question shares **no terms at all** with the section that
> answers it, and reaches the wrong section on the single word "about", idf 1.39.
>
> **The deliberate failure did not do what the draft said it would.** Adding "about" to the stop list
> was written up as turning two tests red and moving the recall numbers. It turns **one** test red
> and moves **none** of them: all three recalls stay at 0.7, 0.8 and 0.9, while the escalation
> question changes from a confidently wrong answer to no answer at all. That is an improvement
> `recall@k` cannot see, and the part now says so — a wrong answer and no answer score identically,
> and they are not the same thing.
>
> Three other drafted claims were corrected against real runs before shipping. A deleted heading
> separator absorbs its section into the one **above** it, not below, and takes HB-01 from 412 to 790
> characters. A question the draft called obvious — "what may a deficiency letter never contain" —
> reaches HB-01 rather than HB-05, and is now a named test of the retriever's weakness rather than an
> example of its strength. And the empty-corpus failure prints `[]`, `index over 0 chunks` and
> `recall@3 -> 0.0` with no error anywhere.
>
> Part 3.1 is the refusal. `InMemoryMemoryService` was driven for real: two claims stay isolated as
> sessions, and once both are handed to memory a query taking **no claim reference** returns one
> policyholder's exact words. The difference between a session and a memory is not the data, the
> retention or the storage — it is whether the events can be reached without knowing which claim they
> belong to. This desk registers no memory service, and a test greps `sessions.py` to keep it that
> way.
>
> As with every day so far, this row was appended when the day was written, and its `CHECKLIST.md`
> boxes are unticked at the time of writing.

> **P01 day 13.** Written 2026-09-10. Four parts, three sections. `./run check` green with 157 tests,
> up from 141, and six tests from days 7, 10 and 11 went red on the way — every one of them the
> change working.
>
> The six perils became a `StrEnum` in `domain.py`, because the same list was written out in three
> places and the third — `data/policies.json` — is where it is actually true. `claims_desk/schemas.py`
> declares what the classifier may return, the agent gets `output_schema=Reading`, and the
> consequences are most of the day.
>
> **The framework now writes a validated dict into state where day 12 wrote a JSON string**, so day
> 10's fourteen-line `parse_reading` becomes four lines and loses its `json` import. What is left is
> the one case a schema cannot cover: the key is absent because nothing ran.
>
> **The day's deliberate failure appeared while wiring it.** A schema refusal is raised **inside** the
> turn as a `ValidationError`, so an unreadable description came out of `run_triage`, out of
> `desk.decide`, out of `run_queue` — one claim stopping the morning. It is day 11's lesson from the
> opposite direction: there an exception was wrapped and never arrived, here one arrives at a caller
> that never expected any. Caught once, given its own constant `REFUSED_SHAPE`, and logged by field
> and error type with `input_value` deliberately excluded.
>
> The refusal that mattered was the stand-in's own. `{"scripted": true, "error": "..."}` is refused by
> `extra="forbid"` because `error` is not a declared field — which is exactly the setting working, and
> is why `scripted` had to be declared with a default rather than left to slip through.
>
> **Printing the generated JSON schema was worth doing.** `Peril`'s two-paragraph docstring — written
> for maintainers, explaining why the enum exists — crosses to a provider on every call, along with
> pydantic's invented titles. That is a real per-request cost found by looking rather than by
> reasoning, and shortening it is a `TODO(me)` with the measurement attached.
>
> Part 2.1 is schema evolution, and it is the part with no code in production: three models in the
> test file, and the finding that a schema change is **two** migrations in opposite directions. A
> default fixes old data under a new reader; nothing on the writing side fixes new data under an old
> one, because `extra="forbid"` refuses it. Readers before writers.
>
> Two drafted transcripts were corrected against real runs. A missing doubled brace in the f-string
> prompt raises `ValueError: Invalid format specifier ...` at import time, not the `KeyError` the
> draft claimed. And pytest truncates both sets when the peril-agreement test fails, so the useful
> line is `Extra items in the left set`, not the full comparison the draft printed.
>
> As with every day so far, this row was appended when the day was written, and its `CHECKLIST.md`
> boxes are unticked at the time of writing.

> **P01 day 14.** Written 2026-09-11. Four parts, three sections. `./run check` green with 181 tests,
> up from 157, and one day-6 stub went red on the way — the fourth time that stub has changed.
>
> Every decided claim now carries a `DecisionRecord`: the eleven facts `assess` reads, the provenance
> that says who read them and what it cost, the handbook citations a handler would follow, and the
> letter — stored beside the record because a policyholder received it, with its own schema
> description saying it is not evidence. `replay()` re-derives the verdict from the record alone, with
> no store, no boundary and no model, using the same `assess` the desk called rather than a copy.
>
> **All twelve claims replay to their own verdicts**, covering all eight deficiency reasons plus four
> fast-tracks — day 2's fixture set paying off five days later, because every rule has a claim that
> fires it. The four claims settled from their fields carry a record with `loss_type: ''`, `model:
> ''` and `calls: {}`, which is the strongest available answer to "was this decided by a model".
>
> **The limit is stated rather than discovered.** Editing a stored verdict is caught; editing a
> stored fact is caught; editing **both** consistently — the estimate and the outcome, two fields —
> passes with `defensible=True`, on a record whose own letter contradicts it. This desk is
> inconsistency-evident, not tamper-evident, and the difference is a hash it does not have. That is a
> `TODO(me)` with what it would cost, not a silent gap.
>
> **The deliberate failure turned out to be two failures, and the drafted one was wrong.** Swapping
> two checks in `assess` was written up as breaking the replay. It breaks **nothing** — twenty-four
> passed — because the queue test writes its records with the current rules and then replays them
> against the current rules. Both halves move together. The real demonstration keeps records from
> before the change: take `fire` out of `PHOTO_REQUIRED_FOR` and one stored record stops being
> defensible, filed as `missing_photo_reference` and now replaying as `fast-track`. The part now
> carries both, and the second is the more useful: **a test that creates its own evidence can only
> find bugs in the thing it did not create.**
>
> Two smaller decisions worth keeping. The rule that fired is **derived** from the reason rather than
> stored, because a stored rule name would be a second field written by the same code that wrote the
> outcome. And the reason-to-citation mapping is eight lines of hand-written dictionary rather than a
> call to day 12's retriever — whose own `recall@1` is 0.7, and which day 12 measured reaching HB-01
> instead of HB-04 for exactly the fast-track-limit phrasing a record would ask about.
>
> As with every day so far, this row was appended when the day was written, and its `CHECKLIST.md`
> boxes are unticked at the time of writing.

> **P01 day 15.** Written 2026-09-11. Four parts, three sections. `./run check` green with 200 tests,
> up from 181, and one day-6 stub went red — the fifth time, which is now a `TODO(me)` about the
> shape of `record_decision`.
>
> Day 1's `util/backoff.py` finally has something to defend. Three attempts, day 1's waits of 1 and
> 2, and the provider's own `Retry-After` beating that schedule whenever it gives one — capped at
> thirty seconds, past which "wait" is a refusal and the desk escalates. A retry the budget cannot
> pay for is **not attempted at all**: one attempt, no waits, straight to escalation, because
> spending the last call in an allowance to discover it is gone charges the next claim for the
> discovery.
>
> Writes got an idempotency key derived from the decision's own content. The same write twice lands
> once and returns `repeat: True`; a **different** decision about the same claim is refused rather
> than overwriting. Running two keyless writes showed what used to happen: `{'outcome':
> 'deficiency', 'reason': 'injury_reported'}` — the second write silently won, and that was true of
> any second write to a decided claim, not only a retried one.
>
> **The day's deliberate failure is the one this whole project has been pointed at since day 1.**
> Default the classification when the provider is down — `peril_not_covered`, the conservative
> choice — and run the queue during an outage: twelve claims decided, twelve decision records, and
> **every one of them defensible**. FNOL-4477's record asserts that its policy does not cover an
> escape of water, on a policy that covers escape of water, and day 14's replay confirms the record
> is internally consistent because the arithmetic is fine and the input was invented. Two hundred
> tests stay green. The only trace is `model: ''`, sitting in a field that legitimately means "no
> model was involved" on four claims in twelve.
>
> Two real defects were found by reading output rather than by a test. The `reliability.unavailable`
> log line reported `attempts` as the *constant* rather than the count, so a run stopped by the
> budget guard after one attempt printed `"attempts": 3` — fixed by tracking `made` and logging
> `allowed` beside it. And `test_a_provider_that_never_answers_leaves_the_claim_pending` recursed
> infinitely on the first attempt, because `desk.reliability` **is** the module and the replacement
> called the name it had just replaced; the original has to be captured first, and the test now says
> so in a comment.
>
> One drafted number was wrong and is corrected. Part 3.1 claimed a sleeping suite takes 23 seconds;
> measured, it is **10.12** against 2.25 — still four and a half times slower, still the argument for
> day 1's `sleep` parameter, and now a figure rather than a guess.
>
> As with every day so far, this row was appended when the day was written, and its `CHECKLIST.md`
> boxes are unticked at the time of writing.

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

> **P01 day 16 — Security and privilege.** Nine parts, and the day's honest shape is that most of it
> names controls this project already had: the boundary's projection (day 3), agents with no tools
> (day 7), per-agent conversations (day 9), the second lock on the letter writer's request (day 11),
> the schema that refuses a peril outside its enum (day 13). Two things are new — the quarantined
> description, and an approval gate that holds a decided claim.
>
> **Four things were got wrong while writing and corrected against real runs.** First, a test
> asserted that `GOOGLE_API_KEY` appears only in `keys.py`; the literal string is not in that file at
> all, because it works generically on names. Rewritten to assert what is true — that exactly two
> files name `.env`, and only one holds a value. Second, the naive version of that test searched for
> `.env` and accused `boundary.py`, because `os.environ` contains those four characters; the test now
> matches the quoted literal, and the mistake became part 2.2's and part 5.1's teaching. Third,
> `APPROVAL_ABOVE` was drafted at 10000 — above every estimate in the fixture, so **the gate could
> never fire against this project's own data**. It was set to 2500, the fast-track ceiling, which
> holds exactly one claim: FNOL-4481, the 4800 claim the rules already call too large to fast-track.
> Fourth, part 1.3 originally said day 11's hook compared the *draft* against the description; it
> compares the outgoing **request**, which is why it caught a route nobody predicted. Corrected.
>
> **Moving the threshold to 2500 reddened five tests from days 6, 7, 9, 11 and 14**, all asserting the
> queue's totals — twelve decided became eleven recorded and one held. Every one was updated to the
> actual numbers with a comment naming the claim and the figure, and part 5.2 is about that bill
> rather than hiding it. One earlier assertion was genuinely lost: `len(set(reasons)) == 8`, eight
> deficiencies with eight distinct reasons, is now seven, because the held claim's
> `above_fast_track_limit` is the reason that left the recorded set. That trade is written down.
> **The day-0 brief's "eight letters" is now false** — seven are written. The brief was not quietly
> edited; the checklist asks the learner which of the two should change.
>
> **The day's strongest transcript is a failure with no symptom.** Returning the whole policy record
> from `fetch_policy` leaves all 200 pre-today tests green, writes nothing to disk, logs nothing, and
> changes no behaviour — because `Cover.from_boundary` takes three fields and drops the rest. The
> policyholder's address reaches the process that runs models and holds the provider key, and the only
> thing that disagrees is a test written today. Both deliberate-failure diffs were reverted; the gate
> is green at `225 passed`.
>
> Request budget was measured both ways rather than reasoned about: fifteen model calls across the
> queue with the gate, seventeen without it, the difference being FNOL-4481's letter, which had needed
> two drafts.

> **P01 day 17 — Observability.** Seven parts. A correlation id in a `ContextVar` read by `log`
> itself, so fifty existing call sites across nine modules became correlated without one being
> edited; the id carried into the boundary subprocess's environment, so a line written by the server
> process shares the desk's trace; spans; and a table saying which single event wakes a person.
>
> **The day found two real defects in this project, and neither was found by a test.** First: putting
> a span round `boundary.call` and actually reading the trace showed `boundary.call: 1863ms`
> containing nothing. Two more spans found it — `boundary.tool` answers in 12.5ms and
> `boundary.connect` takes 2078.9ms, because every call launches a Python subprocess. Over the whole
> queue that is **98.1% of a 67.8-second run spent starting interpreters**, against 0.6s of actual
> tool work and 0.7s of model calls. Day 4's docstring had said "a connection per call, on purpose
> and only for now" for thirteen days; today is the first time it had a number. Not fixed today — a
> pool needs a lifetime owner and a failure story, and that is day 19.
>
> Second: `hooks.tool_result` has been emitting `"keys": "<redacted>"` since day 11, and
> `boundary.record_decision.repeat` the same for `key` since day 15. Day 1's redactor matches secret
> hints as substrings, and `keys` contains `key`. Six days, every check green, because **no test
> asserted that a log line says anything**. Fixed by naming today's field `fields` rather than by
> weakening the redactor, and there is now a test asserting no field of any line is the redaction
> marker — which catches the next collision rather than only this one.
>
> **Two things were got wrong while writing and corrected against real runs.** A drafted transcript
> showed `boundary.record_decision.repeat` printing its key unredacted; the real output redacts it,
> and the corrected passage makes the sharper point that the two lines are different cases — one a
> plain bug, one a defensible redaction of a non-secret. And `alerts.summarise` returned `TICKET` for
> any run containing any event at all, so a perfectly clean queue was a ticket; the level now comes
> from the rules, and `test_a_clean_run_wakes_nobody` is the test that caught it.
>
> One test from day 4 went red: `test_the_desk_reaches_the_boundary_over_stdio_by_default` asserted
> `target() is LAUNCH`, and the launch parameters now carry an environment. Rewritten to assert the
> command and args, with a comment naming today.
>
> Nothing today changes what the desk decides — twelve claims, four fast-tracked, seven recorded, one
> held, identical to day 16. `250 passed`, gate green.

> **P01 repair pass, 2026-09-12 — the Completeness Rule, checked mechanically for the first time.**
> No new day. Rebuilding P01's tree from its own day documents, the way the learner does, turned up
> three classes of defect in days already marked green, and all three are now fixed.
>
> **Twenty-two marked diffs used a bare `...` as a context line**, meaning "an unchanged region sits
> here". That is plan §0 rule 1 — *no `...`* — and its practical cost is that the diff cannot be
> applied: a learner reaching one has to guess what was elided. All twenty-two became `@@ ... @@`
> hunk separators, which say the same thing in the syntax a reader and a tool both understand.
>
> **Sixteen diff blocks were tagged ```python, ```toml or untagged** rather than ```diff. A learner
> copying one of those gets a source file with `-` and `+` down the left margin. Retagged.
>
> **Day 15 never printed `ScriptedTransient`.** Its checklist demanded the class, three of its
> transcripts used it, and no day in this project contained the code — a Completeness Rule violation
> that thirteen green gates did not notice. It is now printed in part 1.1 as a marked diff against
> `claims_desk/scripted.py`, written and run before being written down: it fails twice with
> `retry_after=0.5` and then returns `escape-of-water`, which is exactly what part 1.1's existing
> transcript claims. Two elisions in day 7's `domain.py` diff (`assess`'s docstring, and the
> photo-reference and injury checks) were also unmarked, and now carry `@@` markers saying what sits
> there unchanged.
>
> **`python p.py check` now enforces all of this.** `check_completeness` fails a part that carries a
> bare `...` on a context line of a diff, or a marked diff tagged as source. It was verified by
> reintroducing one deliberately and watching the gate go red. Before this, the Completeness Rule
> was a rule kept by hand, and by day 15 it had not been.
>
> The lesson for the days still to come: **a rule with no check is a preference.** The same is true
> of the four other rules in plan §0, and only two of them currently have one.

> **P01 day 18 — Evals.** Seven parts. The whole desk run as a subprocess and marked against the
> answer key `data/notifications.json` has carried since day 2 — outcome, reason, loss type, the
> boundary route and the model-call bill read back from day 17's spans, and the letter judged by a
> four-row rubric — with no partial credit on a claim. A baseline of day 2's rules with a guessed
> peril scores 9/12 on verdicts and 6/12 once a right verdict for the wrong peril stops counting, so
> the model's whole contribution is three claims. Disabling the in-force check turns ten of twelve
> claims red, one on its verdict and nine on their route; the unit suite goes red too, on seven tests
> that name FNOL-4474 and not the cause. The framework's evaluator was installed (`google-adk[eval]`,
> fifty-two packages, `mcp` still 2.2.0), given the classifier as a `root_agent`, run from pytest and
> from `adk eval`, and measured: its word-overlap judge scores an inverted injury flag 0.889, the same
> as the right answer, and a wrong peril 0.625. The marking scheme itself was wrong twice — a bill
> that forgot letters, and a test reading claim files from the wrong store — and both are kept as
> tests. Gate: `280 passed` on the rebuilt tree, `./run eval` green, `python p.py check` green.
>
> **Day 18 was verified on a tree rebuilt strictly from days 0–17's printed files and marked
> diffs**, because no earlier throwaway survived. That tree reached `247 passed`, not day 17's `250`:
> three assertions day 13's hub says it added to `tests/test_agent.py` and `tests/test_workflow.py`
> were never printed. The rebuild found four other changes that a hub or checklist names and no part
> prints — day 14's diffs to `claims_desk/desk.py`, `claims_desk/workflow.py`,
> `claims_desk/boundary.py` and `claims_mcp/tools.py` (the decision record threaded through to the
> claim file); day 15's diffs to `boundary.py` and `tools.py` (the idempotency key); day 11's two
> test updates; day 17's `tests/test_transports.py` diff — and five earlier tests that later days'
> changes made stale with no printed update (`test_the_server_says_who_it_is` at 0.4.0 after day 9
> moved the server to 0.5.0; `test_a_notification_the_rules_cannot_settle_is_pending_with_a_reason_why`
> still expecting FNOL-4471 to be pending after day 7; the refused-write stub in `test_desk.py` with
> day 6's three-argument signature; `test_the_classifier_reports_rather_than_guesses` without the
> `output_key` that makes day 13's schema run; `test_triage_leaves_its_verdict_in_state` asserting
> the wrong peril). Each was reconstructed from the transcripts those days do print. They are
> Completeness Rule debts of days 7, 9, 11, 13, 14, 15 and 17, owed as marked diffs to those days;
> `python p.py check` did not notice any of them, because the gate checks a diff's shape and not
> whether a change a hub announces was ever printed.

> **P01 day 19 — Ship.** Seven parts, and the last day of the project. A two-stage image on
> `python:3.12.12-slim` with uv 0.12.3 copied in, `--locked --no-dev`, a non-root user and a
> `HEALTHCHECK`; `.dockerignore` written before it; the boundary's HTTP host made a variable; a
> standard-library service with `GET /healthz` that asks the boundary for a policy no book has and
> reports the leaf exception, and `POST /queue`; `compose.yaml` with the boundary as a sidecar on a
> private network, no port published for it, `env_file` on the desk alone and a health condition;
> a workflow that runs both gates on `ubuntu-latest` with uv pinned and a key that says it is not one;
> the README and the generated CODEMAP; twelve tests that read the files as text. **The cold clone
> was run for real**: an empty folder, an empty `UV_CACHE_DIR`, 123 packages downloaded, `292
> passed`, `eval: green`; the clone that forgot `uv.lock` and the pin moved without it were both
> stopped by `--locked` with the fix in the message. **Not run on this machine, marked `TODO(me)`
> with exact commands:** the image build, `./run up`, and the workflow's first run — there is no
> Docker here and the throwaway repository has no remote. The first `./run serve` met a port held by
> a process that was not this project's, which is why the port became a variable. Gate: `292
> passed`, `./run eval` green, `python p.py check` green. P01 is complete: twenty days, seventy-two
> files, all eighteen spine slots plus two extra days.

> **P02 day 0 — The machine and the repository.** Eight parts, and the first day of the second
> project, started from a bare folder on the day P01 closed. The freshness check plan §10 asks for
> ran first: `google-adk` is at 2.9.0 (released 2026-09-10, two days ago) with breaking changes
> listed for workflow resume, the in-memory session service and MCP 2.x field handling; `mcp` is
> still 2.2.0; the protocol revision is still 2026-07-28; the provider's Flash list is unchanged.
> Nothing in the plan's text depends on the framework's version, so no amendment — the pin is day
> 1's decision, and the three facts are recorded in the project's `PACKAGES.md` as *observed, not
> installed*. The interpreter pinned is 3.12.13, the newest patch `uv python list` offered, and it
> was downloaded rather than found. The check asks five questions where P01's asked four — the
> fifth is `git rev-parse --show-toplevel`, so a folder with no repository or inside somebody
> else's goes red — and every one of six ways to make it red was run. Two things this day found
> that its predecessor's day 0 did not say: `git check-ignore` is silent on a *tracked*
> `.env.example` whatever the rules are, so the negation must be tested with `--no-index`; and a
> `.python-version` in a parent folder is obeyed silently when the project has none. `SETUP.md`
> was handed to an empty folder and followed cold to five green lines. Gate: `python p.py check`
> green.

> **P02 day 1 — The skeleton and the kit.** Nine parts. `pyproject.toml` declared `ruff==0.16.7`
> and `pytest==9.1.1` — both current on the day, checked live — with `dependencies = []` because
> the framework is not yet installed. `uv sync` fell back from hardlinks to a full copy on this
> filesystem, a warning and not an error. `stock_desk` and `stock_desk.util` were declared as
> packages, and `run` became the one door, refusing a missing program (`docker`) by name rather
> than with a Python traceback. The kit's four modules were built and tested: `keys` never prints
> a value, only a twelve-character fingerprint; `logging` redacts by whole word rather than
> substring, so a field named `keys` survives where `api_key` does not; `backoff` honours a
> provider's own `Retry-After` over its own schedule and escalates rather than inventing an
> answer; `budget` raises rather than clamping. The registry refuses an alias, the provider's
> legacy default, and any ID not on its list — and refuses the alias twice, by two independent
> lines, which was demonstrated by disabling one and watching the other still catch it. The day's
> own first `./run check` was red on its own test file's line length, which is the right way for a
> gate to introduce itself; three more failures were caused on purpose and read in full. Gate:
> `python p.py check` green.

> **P02 day 2 — The domain and its data.** Six parts. Sixty synthetic bins across three aisles
> (`data/ledger.json`) and sixty cycle counts (`data/counts.json`), generated deterministically
> and then hand-crafted with nine planted variances: three receipts not yet booked, three picks
> not yet confirmed, two known breakages, and one genuinely unexplained shortfall that must be
> replenished. `Bin`, `Count`, `Outcome` and `Reason` were built as frozen dataclasses and a
> `StrEnum`; `reconcile` decides between four outcomes from three given facts, checking a zero
> delta first, an accepted reason second, and the sign of the gap only once neither of those
> settles it. `Store` became the one class allowed to open a file, with an atomic
> `write_reconciliation` demonstrated against two real crash simulations — a naive straight-to-
> target write left a file that existed, was non-empty, and failed to parse; the same crash
> against the atomic version left no file at all. The fixture set was asserted as a contract in
> seven tests, one of which reproduces every declared outcome by running `reconcile` itself. The
> day's deliberate failure: `guess_reason_from_note`, a keyword-scan stand-in, misreads exactly
> one of the nine notes — the one describing a receipt as "the supplier's Wednesday drop" rather
> than using a recognised word. Widening its word list to catch that note was demonstrated to
> break a different, previously-correct note instead (`C-05-1`, "dropped in transit"), with the
> project's own inverted-case test catching the swap: `assert 'A-10-2' in ['C-05-1']`. Every
> transcript in this day, including all "When it breaks" failures, was run for real and verified
> against the actual command before being written down. Gate: `24 passed`, `python p.py check`
> green.

> **P02 day 3 — The boundary, part one.** Five parts. Measured the desk's blast radius before
> building anything: a tool-shaped function running in the desk's own process can reach
> forty-five files, `.env` among them, and a naive "helpful extra" tool was demonstrated leaking
> the synthetic key in its return value. `stock_mcp` was built as a second top-level package,
> importing from `stock_desk` in one direction only, declaring one tool — `fetch_bin` — whose
> schema was derived entirely from its own signature and docstring. `mcp==2.2.0` was added as a
> runtime dependency (installed directly, never through `google-adk[mcp]`'s `mcp<2` extra), the
> module was made runnable with `python -m stock_mcp`, and the `run` driver's `mcp` command moved
> from `PLANNED` to real. A real round trip over a subprocess was captured: protocol version
> `2026-07-28`, server identity `stock-boundary 0.1.0`, a found bin and a `{"found": false}` miss,
> neither carrying an error flag. Six tests hold the boundary to its docket — five in-process, one
> over a real subprocess — including an exact-list assertion on the tool docket and a smell test
> that a bin's reply carries no file path. Three ways to make the gate go red were caused and read
> in full: adding a tool, leaking a path, and pointing the client at a misspelled module
> (`MCPError: Connection closed`). The day's deliberate failure is the one that does not go red: a
> `print` inside `fetch_bin` corrupts one line of the stdio wire, the client logs a parse failure
> and skips it, the call still succeeds, and all thirty tests still pass — and on this run, unlike
> a prior observation of the same failure on a different project, the suite's own timing did not
> move either, which is written down as the harder and more honest version of the lesson. A stale
> `docs/PINS.md` row claiming this project "cannot run" the current MCP revision was superseded,
> not edited, with a new dated row. Gate: `30 passed`, `python p.py check` green.
