---
project: "P01"
day: 18
title: "Evals"
spine: 16
kind: gate
deploy_tier: D3
plan_version: "v4.1.0"
parts: 7
files_printed: [claims_desk/evals.py, claims_desk/evalset/__init__.py, claims_desk/evalset/agent.py, data/evalset/classifier.evalset.json, data/evalset/test_config.json, tests/test_evals.py]
generated: "2026-09-12"
status: written
commit: ""
---

> **Yesterday:** observability — one id across every module and both processes, a span around
> everything that takes time, the span that was missing and what it found, and a table saying which
> single event wakes a person.
> **Today:** the file audit — the whole desk run as a person runs it and marked against the answer
> key it has carried since day 2, on its verdicts, its route, its letters and its bill; a baseline
> that says what the model is worth; the framework's evaluator beside it; and the gate that goes red
> the moment the policy in-force check is disabled.
> **Tomorrow:** ship — the container, the secrets that are injected and never baked, compose with
> the boundary beside the desk, the CI workflow that runs today's gate, and the cold clone.

## §1 The scene

Every claims department has a file audit, and every handler dreads the week it lands.

A senior handler pulls twelve closed files from last month and goes through each one with a marking
sheet. Not a vague read — a sheet. Was the policy checked, and is the query in the file to prove it?
Does the reason on the file match the reason on the letter? Does the letter quote the reference, name
no figure, run to four sentences, tell the person what to send? Each file gets a row of ticks and
crosses, and a file with one cross is a failed file however many ticks sit beside it, because the
cross is the thing that reached a policyholder. The total goes on a chart, next to the score a
handler who did the bare minimum would get, and if the gap has closed somebody has a meeting.

This desk has 250 tests and no sheet. Every one of those tests asks a function a question. None of
them runs the desk the way a person does, reads what it left behind, and marks it — and the
project's brief has said since day 0 what that sheet must catch: *the eval goes red the moment the
policy in-force check is disabled.* Today the sentence is tested by doing the thing it describes.
Four lines make the desk faster and leave 273 tests green. The sheet fails ten files out of twelve —
nine for a query that was never sent, and one for a claim fast-tracked on a policy that lapsed the
May before the loss.

And the sheet is marked too. Twice today the marking scheme was wrong — once about what a letter
costs, once about which directory it was reading — and both times the only thing that found it was
running it and reading the result. That is the shape of the day: build the audit, audit the audit,
then look at the tool that ships with the framework and find out, with a number, what it can and
cannot see.

## §2 The map

Seven parts in four sections: the set, the marking, the gate, and the tests.

### 1 · The set

What is marked, against what, and how the route is read back from the log.

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-set/1.1-set-with-a-declared-answer.md) | The set with a declared answer | What is an evalset, and why does it run the desk as a subprocess? | working |
| [1.2](parts/01-the-set/1.2-trajectory-not-just-the-answer.md) | The trajectory, not just the answer | How is "which tools, in what order, at what cost" read from day 17's spans? | working |

### 2 · The marking

The rows a program can judge, and the number a score has to be compared against.

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-marking/2.1-judge-and-its-rubric.md) | The judge and its rubric | How is a letter marked when there is no correct letter? | production |
| [2.2](parts/02-the-marking/2.2-baseline-that-makes-a-score-mean-something.md) | The baseline that makes a score mean something | What would a desk with no model score, and what does that make the model worth? | production |

### 3 · The gate

The check that goes red, and the framework's evaluator beside it.

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-the-gate/3.1-gate-that-goes-red.md) | The gate that goes red · **failure** | What happens when the in-force check is disabled, and what catches it? | production |
| [3.2](parts/03-the-gate/3.2-what-the-framework-ships.md) | What the framework ships, and why this desk's audit stays its own | What do `adk eval` and `AgentEvaluator` evaluate, and what can their text judge not see? | production |

### 4 · Holding it

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [4.1](parts/04-holding-it/4.1-what-the-tests-hold.md) | What the tests hold | Who audits the auditor? | production |

## §3 Setup — run this

One extra is installed, two folders are made, and one earlier file changes by one line.

```bash
./run check

uv add "google-adk[eval]==2.8.0"
uv run python -c "import importlib.metadata as m; print('mcp', m.version('mcp'))"
uv run python -c "import importlib.metadata as m; print('rouge-score', m.version('rouge-score'))"

mkdir -p claims_desk/evalset data/evalset
```

Expect `250 passed` from the first command — day 17's total — and `283 passed` at the end of the day,
thirty-three more. The `uv add` prints `Resolved 125 packages` and `Installed 52 packages`; the two
checks after it must print `mcp 2.2.0` and `rouge-score 0.1.2`. The first is the one that matters:
the `[eval]` extra does not carry the `mcp<2` bound that day 7 kept out of this project, and the
check is how you know rather than assume.

**If your tree was built strictly from the printed files and day 17 ended at `247 passed`, today
ends at `280`.** Three assertions that day 13's hub says it added to `tests/test_agent.py` and
`tests/test_workflow.py` were never printed in any part, and a tree typed from the documents does not
have them. That is day 13's debt, not yours; it is recorded under the ledger row.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `claims_desk/evals.py` | part 1.1 |
| `claims_desk/evalset/__init__.py` | part 3.2 |
| `claims_desk/evalset/agent.py` | part 3.2 |
| `data/evalset/classifier.evalset.json` | part 3.2 |
| `data/evalset/test_config.json` | part 3.2 |
| `tests/test_evals.py` | part 4.1 |

Three earlier files change, each as a marked diff naming the day of this project that printed the
original: `run` (day 1, last changed day 6) in part 1.1 — the `eval` command that day 1's `PLANNED`
table promised for today; `pyproject.toml` (day 1, last changed day 7) in part 3.2 — one line, made by
the `uv add` above; and `.gitignore` (day 0) in part 3.2 — the framework's evaluation history.

## §5 Build brief

Write `evals.py` first and run `./run eval` before reading part 1.2's failure section — the first
run of a marking scheme is the one that marks the scheme, and it is worth seeing your own version go
red before seeing why this one did. Then the extra, the evalset package and the framework's set,
then the tests. Then the reps:

| File | What it must do |
| --- | --- |
| `claims_desk/evals.py` | `TODO(me)`: a mark that compares `desk.decided` with the claim file's own `outcome` for every recorded claim. Run it and say whether any of the ten disagree. |
| `claims_desk/evals.py` | `TODO(me)`: the assertion in `by_claim` that refuses to attribute when two `claim` spans overlap, using the `span` field on the lines inside them. |
| `claims_desk/evals.py` | `TODO(me)`: the smarter baseline — the book's most common peril, computed from `data/policies.json` — and whether the two numbers moved, and what that means about the model. |
| `claims_desk/evals.py` | `TODO(me)`: the lenient route mark from part 3.1. Build a desk that records before it drafts, confirm the gate stays green, put the strict mark back and watch the order alone go red. |
| `claims_desk/evals.py` | `TODO(me)`: `report` says `desk.letter_failed` beside four letter crosses when the claim's own bucket holds that line — and the test for it in `tests/test_evals.py`. |
| Your own notes | `TODO(me)`: the fifth rubric row, *courteous and does not blame the policyholder*, as a model judge — the instruction, the model that would hold it and why not the writer's, and the call left as a `TODO(me)` naming the key. |
| `data/evalset/classifier.evalset.json` | `TODO(me)`: the set sends the bare description; the desk sends it quarantined. Decide whether they should match, change the twelve fields or leave them, and write the reason into the file's `description`. |
| Your own notes | `TODO(me)`: `custom_metric_evaluator` in the installed package, and the field-equality metric it would take for the classifier — written, not run. |
| Your own notes | `TODO(me)`: `NUM_RUNS` is 2 by default. Run `adk eval` with a count of `hooks.model` lines and say whether the framework really doubles the classifier's bill, or whether the summary's `Tests passed: 12` hides twenty-four calls. |

## §6 The check that must be able to fail

Two gates today, at two speeds:

```bash
./run check
./run eval
```

Green for the first is `All checks passed!`, `283 passed` (or `280`, see §3), and day 0's four `ok`
lines. Green for the second is twelve `ok` lines, `desk     12/12 claims right on every mark`,
`baseline 6/12 ... or 9/12`, `eval: green` and `OK eval`.

Ways to make `./run eval` red:

1. **Disable the in-force check** — part 3.1's four lines. Ten claims red, one on its verdict and
   nine on their route, `desk     2/12`, `exited 1`.
2. **Give a scripted letter a figure** — `within 14 days` on the photograph letter. FNOL-4477 fails
   all four letter rows and `calls: expected 2, got 4`, because day 10's loop ran to its bound
   refusing it.
3. **Rewrite `expected_calls` in three branches**, the way its first draft was. Four field-settled
   deficiencies red on `calls: expected 0, got 1`.
4. **Change the answer key** — say FNOL-4474 should be fast-tracked. Four marks red on that claim,
   and `calls` is not one of them.

Ways to make `./run check` red that `./run eval` cannot see:

5. **Read the claim files from a fresh `Store()` in `the_desk_marked`** with `data/claims/` empty.
   Seven claims fail every letter row for a run that wrote every letter.
6. **Raise `response_match_score`'s threshold to 0.9** in the judge test. The *correct* answer
   fails, because the stand-in's `scripted: true` costs a ninth of the overlap.

And the one that is green while being wrong, which is part 3.1's second failure: **loosen the route
mark to a subset check.** The in-force edit still goes red, so nobody notices; a desk that records
before it drafts does not.

## §7 Request budget

**Five model calls allowed per notification, unchanged. `./run eval` spends fifteen across the
queue, unchanged** — it is one run of the desk, and the audit, the baseline and the marking spend
nothing: the baseline is day 2's rules with a guessed peril, and the marks are comparisons.

What today adds is a second consumer of the classifier. The framework's evalset runs the classifier
once per case — **twelve calls at `num_runs=1`**, which is what the test in `./run check` asks for,
and **twenty-four at the framework's default of two**, which is what `adk eval` on the command line
uses unless told otherwise. Against the stand-in that is free. Against a real provider, `./run check`
now costs twelve requests per run and `adk eval` twenty-four, before the desk's own fifteen — which is
why the test pins `num_runs=1` and why the provider's ceiling is still a `TODO(me)` naming where to
read it rather than a number.

The judge that reads prose — part 2.1's fifth row, the framework's rubric-based metrics — is not
run today and would cost one call per letter per row. Part 2.1's production note has the arithmetic
for a desk that sends eleven hundred letters a month.

## §8 Traps

- **A handler marking their own files gets full marks.** The audit imports the domain and the
  store, and never the desk.
- **A file passes or it does not.** Partial credit hides the cross that reached a policyholder.
- **Mark the route, not only the answer** — a right verdict by the wrong route is the next wrong
  verdict.
- **Derive the expected route from the answer**, or twelve hand-written routes are wrong in the
  same way the desk is.
- **A field-settled deficiency still costs its letter.** The first draft of the bill said zero.
- **Attribution by the closing span is only right because the queue is sequential.** Say so where
  it is done, and assert it.
- **Clear the claim files before the run.** Day 15's idempotency makes a stale file look like the
  same write.
- **Read the files the run wrote, not the directory the last run left.** A fresh `Store()` in a
  test is a test that depends on what ran before it.
- **A rule a program can read is a rule a program should judge.** Save the model judge for the row
  code cannot read, and never let it see the answer key.
- **Strip the reference before counting figures**, or every letter fails the figure row.
- **Two checkers with the same rule disagree about where the failure is.** The loop sees a figure;
  the audit sees no letter. Carry enough of the route to join them.
- **A score without a baseline is a number.** Compute the cheapest alternative, print it beside the
  score, every run.
- **Right for the wrong reason is a second number**, and it is the one that moves when a baseline
  is "improved".
- **A baseline tuned until it looks good is a ceiling somebody built by hand.** Choose it once,
  write the reason, stop.
- **A loosened gate does not go red. It goes quiet.** The inverted case is what notices.
- **The framework evaluates an agent, one turn at a time.** Give it the agent that is a
  conversation; audit the desk yourself.
- **Word overlap on JSON cannot see one word.** `0.889` for the right answer and `0.889` for the
  inverted flag; no threshold separates them.
- **`NUM_RUNS` is two.** Pin it to one against a stand-in, and know what the default costs against a
  provider.
- **`adk eval` puts the agent folder's parent on the path, not the project root.** `PYTHONPATH=.`
  for the CLI; the pytest route needs nothing.
- **The `[eval]` extra is fifty-two packages.** Check `mcp` is still 2.2.0 after installing it, and
  keep `.adk/` out of git.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| The framework's evaluation guide | `https://adk.dev/evaluate/` (reached by redirect from `https://google.github.io/adk-docs/evaluate/`) | 2026-09-12 | `.evalset.json` with `eval_set_id`, `eval_cases`, `conversation`, `user_content`, `final_response`, `intermediate_data.tool_uses`; `test_config.json` with `tool_trajectory_avg_score` defaulting to 1.0 and `response_match_score` to 0.8; `adk eval <AGENT_MODULE_FILE_PATH> <EVAL_SET_FILE_PATH_OR_ID> [--config_file_path]`; `AgentEvaluator.evaluate(agent_module=..., eval_dataset_file_path_or_dir=...)` from pytest; the LLM-judged metrics named. |
| The evaluator's real API | the installed `google-adk` 2.8.0, by reading its source | 2026-09-12 | `AgentEvaluator.evaluate(agent_module, eval_dataset_file_path_or_dir, num_runs=NUM_RUNS, ...)`; `NUM_RUNS = 2`; the loader accepts a module with an `agent` attribute or a name ending `.agent`, then wants `root_agent` or `get_agent_async`; it ends in `assert not failures, failure_message`. |
| The thirteen prebuilt metrics | the installed package, `PrebuiltMetrics` | 2026-09-12 | `tool_trajectory_avg_score`, `response_evaluation_score`, `response_match_score`, `safety_v1`, `final_response_match_v2`, `rubric_based_final_response_quality_v1`, `hallucinations_v1`, `rubric_based_tool_use_quality_v1`, `per_turn_user_simulator_quality_v1`, `multi_turn_task_success_v1`, `multi_turn_trajectory_quality_v1`, `multi_turn_tool_use_quality_v1`, `rubric_based_multi_turn_trajectory_quality_v1`. |
| The evalset's shape | the installed package, `EvalSet` and `EvalCase` | 2026-09-12 | `EvalSet(eval_set_id, name, description, eval_cases, creation_timestamp)`; `EvalCase` requires exactly one of `conversation` and `conversation_scenario`; `Invocation(user_content, final_response, intermediate_data, ...)`; `IntermediateData.tool_uses`. |
| The trajectory metric's comparisons | the installed package, `TrajectoryEvaluator` | 2026-09-12 | `EXACT`, `IN_ORDER`, `ANY_ORDER`; score 1.0 or 0.0 per invocation, averaged. |
| The extra's dependencies | `importlib.metadata.requires("google-adk")` | 2026-09-12 | `[eval]` requires `rouge-score>=0.1.2`, `pandas>=2.2.3`, `nltk!=3.10.1`, `tabulate>=0.9`, `jinja2`, `openpyxl`, `xlrd`, `gepa`, `google-cloud-texttospeech`, `google-cloud-aiplatform[evaluation]>=1.148`; the `mcp<2` bound is on `[all]`, `[mcp]` and `[test]` only. |
| The extra, installed | this project, `uv add "google-adk[eval]==2.8.0"` | 2026-09-12 | `Resolved 125 packages`, `Installed 52 packages in 16.75s`; lockfile 73 → 125 packages; `mcp 2.2.0` unchanged; `rouge-score 0.1.2`, `google-cloud-aiplatform 2.1.0`, `pandas 3.0.5`, `nltk 3.10.3`. |
| Without the extra | this project, `uv run adk eval ...` | 2026-09-12 | `Error: Eval module is not installed, please install via `pip install "google-adk[eval]"`.` |
| The CLI's import path | this project, `uv run adk eval claims_desk/evalset ...` | 2026-09-12 | `ModuleNotFoundError: No module named 'claims_desk'`; with `PYTHONPATH=.`, `Tests passed: 12`, and `claims_desk/evalset/.adk/eval_history/evalset_classifier_<timestamp>.evalset_result.json` written. |
| The evaluator pointed at the desk | this project, `adk eval claims_desk ...` | 2026-09-12 | `ValueError: Agent module should have either `root_agent` or `get_agent_async`.` |
| The text judge on structured answers | this project, `RougeEvaluator` | 2026-09-12 | right `0.889 PASSED`, wrong injury flag `0.889 PASSED`, wrong peril `0.625 FAILED`. |
| The audit, green | this project, `./run eval` | 2026-09-12 | twelve `ok`, eighty-four marks, `desk 12/12`, `baseline 6/12 ... or 9/12`, `eval: green`. |
| The baseline's detail | this project | 2026-09-12 | `9 6 of 12`; wrong verdicts FNOL-4475, 4478, 4479; right for the wrong peril FNOL-4471, 4472, 4480; with `fire` guessed everywhere, `9 5 of 12` and FNOL-4481 joins the second list. |
| The eight scripted letters against the rubric | this project | 2026-09-12 | thirty-two ticks, no crosses. |
| The gate, red | this project, in-force check disabled | 2026-09-12 | ten claims `RED`, FNOL-4474 on `outcome`, `reason`, `tools` and four letter rows, nine others on `tools` alone, `desk 2/12`, `exited 1`; `./run test` `7 failed, 273 passed`, none naming `check_in_force`. |
| The first marking scheme, red | this project, `expected_calls` in branches | 2026-09-12 | FNOL-4473, 4474, 4476, 4482 on `calls: expected 0, got 1`; `desk 8/12`. |
| A letter with a figure | this project, `within 14 days` | 2026-09-12 | FNOL-4477 `calls: expected 2, got 4` and four letter rows. |
| The in-process audit, misread | this project, `Store().claim` with `data/claims/` empty | 2026-09-12 | `Left contains 7 more items, first extra item: 'FNOL-4473'`. |
| The gate | this project, `./run check` | 2026-09-12 | ruff clean, `280 passed` on a tree built from the printed files, day 0's four checks green. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 01 | 18 | 2026-09-12 | Evals | 7 | <hash> | yes |
```

And the note under the table, because the reconstruction this day was verified on found debts in
earlier days that a reader typing the project will meet:

> **Day 18 was verified on a tree rebuilt strictly from days 0–17's printed files and marked
> diffs.** That tree reached `247 passed`, not day 17's `250`: three assertions day 13's hub says it
> added to `tests/test_agent.py` and `tests/test_workflow.py` were never printed. The same rebuild
> found four other changes that a hub or checklist names and no part prints — day 14's diffs to
> `claims_desk/desk.py`, `claims_desk/workflow.py`, `claims_desk/boundary.py` and
> `claims_mcp/tools.py` (the decision record threaded through to the claim file), day 15's diff to
> `boundary.py` and `tools.py` (the idempotency key), day 11's two test updates, and day 17's
> `tests/test_transports.py` diff — plus five earlier tests that later days' changes made stale
> without a printed update. Each was reconstructed from the transcripts the days do print. They are
> Completeness Rule debts of days 11, 13, 14, 15 and 17, and they are owed as marked diffs to those
> days, not as edits to this one.

**`docs/GLOSSARY.md`** — new rows:

```text
| Answer key | The declared correct output for every case in an evalset, written by hand by somebody who read the cases, kept beside them, and never readable by the system under evaluation. | P01 day 18 part 1.1 | expected outcomes, the `expected` block |
| Mark | One thing checked on one case: what was expected, what was found, and whether they agree. A case passes only if every mark does; there is no partial credit on a file. | P01 day 18 part 1.1 | a check, a criterion |
| Evalset | A collection of cases with declared answers, run together against the system as a person runs it, reporting one verdict as an exit status. Re-anchored: it now also marks the route and the letter, not only the answer. | P01 day 18 part 1.1 | the eval suite |
| Trajectory | Which tools the system called, in what order, and what it spent, before it answered — reconstructed here from the spans in the log rather than returned. A right answer by the wrong route fails on it. Re-anchored. | P01 day 18 part 1.2 | the route, the tool path |
| Rubric | A marking scheme for output that has no reference answer: separate rows, each one thing a reader can check, each carrying the reason it exists, so a letter can fail one and pass three and the failure names which. | P01 day 18 part 2.1 | a marking sheet |
| Judge | Whatever applies the rubric. Code, for every row a program can read; a model, for the rows it cannot — which must never see the answer key and must be a different model or prompt from the one it is judging. | P01 day 18 part 2.1 | model-as-judge, LLM-as-judge |
| Baseline | The score of the cheapest plausible alternative to the system, computed the same way and printed beside the score every run. Without it a score is a number; with it, the difference is what the system is worth. | P01 day 18 part 2.2 | the floor |
| Gate | A check that goes red when the system gets worse, in a way that names what got worse, and that stops the change going further — an exit status a pipeline refuses on, not a chart. | P01 day 18 part 3.1 | the red build |
| Inverted case | An eval case whose declared answer has been deliberately changed so the audit must object; it goes red when a loosened mark stops objecting. It tests the detector rather than the system. Re-anchored. | P01 day 18 part 4.1 | the negative case |
```

**This project's `PACKAGES.md`** — appended rows, in the project (the learner's tree, not the
authoring repository):

```text
| google-adk[eval] | 2.8.0 | 2026-09-12 | 18 | `uv add "google-adk[eval]==2.8.0"`. The evaluation extra: 52 packages, lockfile 73 → 125. Installed for `AgentEvaluator` and the local metrics; the cloud-judged metrics it also pulls are not used. `mcp` stayed at 2.2.0, checked. |
| rouge-score | 0.1.2 | 2026-09-12 | 18 | `importlib.metadata.version("rouge-score")`. The word-overlap judge behind `response_match_score`, and the one package of the fifty-two this desk exercises. |
```

**`docs/PINS.md`** — no row is owed. The extra is a project pin and goes in the project's own
`PACKAGES.md` above.

**`docs/SOURCES.md`** — no row is owed. Nothing with a citation identifier was cited; the framework's
guide is a live page, recorded in §9 with its URL and the date.

**Commit:**

```text
P01 day 18: Evals
```
