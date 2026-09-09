---
project: "P01 Ask Desk"
day: 10
phase: P01
title: "P01 Ask Desk · 7 — Ship D1: `api_server`, `/healthz`, the first eval that can go red; cold clone"
ids: [DP-01, EV-01]
kind: gate
deploy_tier: D1
plan_version: "v3.1.0"
parts: 5
files_printed:
  - "projects/01-ask-desk/ask_desk/api.py"
  - "projects/01-ask-desk/evals/harness.py"
  - "projects/01-ask-desk/evals/cases.json"
  - "projects/01-ask-desk/evals/__init__.py"
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** a desk that keeps its conversation in a session and lets its failures reach you
> instead of swallowing them.
> **Today:** the desk goes behind HTTP with a health endpoint that answers the right question, gains
> the first check in this curriculum whose subject is behaviour, and is walked file by file against
> the claim that it can be taken away and still run.
> **Tomorrow:** P02 Parts Counter day 1 — the kit: a new project's own utils, printed in full, and
> nothing borrowed from this one.

## §1 The scene

A lifeboat drill is not the emergency. It is a calm morning in harbour, and the only reason to do it
is that it produces evidence about equipment that will otherwise be tested for the first time on the
day it matters. The crew muster, the davits turn, the boat goes down, and somebody writes on a card
what actually happened. Nobody is rescued. That is the point.

Three things go wrong with drills, and today is all three. The first is a drill card with a line on
it the ship cannot tick without the harbour tug — so a seaworthy vessel is held at the quay because a
piece of equipment belonging to somebody else did not turn up. That is a health check that calls the
provider. The second is the drill card that gets signed from the bridge: same signature, same
outcome, and a davit nobody has turned in a year. That is an eval that scores the words a system
produced instead of what it did to produce them. The third is the quiet one — somebody pulls the fuse
on the muster alarm, and every subsequent drill runs beautifully, because a bell nobody can hear
never contradicts anybody.

And underneath all three, the ship that has never lowered a boat at all. Its certificate is honest
about everything that was inspected and silent about the thing that was never done, and the silence
reads exactly like a pass. This project's certificate currently says it runs standalone. Today it
gets asked to prove it, and the honest answer is that half the proof was run and half is owed — which
is written down here as owed rather than described as done.

## §2 The map

Two sections, and they are the two halves of shipping. The first is the **surface**: what this
project looks like from outside, once something other than your own shell can reach it, and the two
questions any HTTP surface has to answer well — *should I restart you* and *why did that fail*. The
second is the **check that can go red**: the first check in this curriculum whose subject is not
configuration but behaviour, the case that exists to prove the check can still fail, and the walk
that decides whether the whole project was ever really standalone.

### 1 · The surface

*The mental model: the drill card. What is on it decides what the ship is held for, and a line the
crew cannot fix by themselves does not belong there.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-surface/1.1-the-health-check-that-checks-the-right-thing.md) | The health check that checks the right thing | What question is `/healthz` actually being asked, and what may it therefore test? | foundation |
| [1.2](parts/01-the-surface/1.2-three-failures-three-answers.md) | Three failures, three answers | Why do 502, 503 and 422 exist, and what is lost when they all become 500? | working |

### 2 · The check that can go red

*The mental model: the drill itself, and the inspector who quietly tests the alarm rather than the
boat.*

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-check-that-can-go-red/2.1-the-first-eval-that-can-fail.md) | The first eval that can fail | How do you test something whose correct output is not a fixed string? | working |
| [2.2](parts/02-the-check-that-can-go-red/2.2-the-eval-that-checks-its-own-detector.md) | The eval that checks its own detector | How does a suite notice that one of its own assertions has stopped working? | production |
| [2.3](parts/02-the-check-that-can-go-red/2.3-the-cold-clone.md) | The cold clone | Is this folder actually standalone, and what was and was not run to find out? | production |

## §3 Setup — run this

Two packages, and they are the first this project has needed since the framework. Everything else
today is files. Run from the repository root; every command below was run on this machine on
2026-09-10 and what it reported is in §9.

```bash
cd projects/01-ask-desk

# part 1.1: the D1 surface needs a web framework and a server. Two names, two jobs.
uv add "fastapi==0.141.1" "uvicorn==0.52.4"
uv lock --check

# part 1.1 writes ask_desk/api.py; part 1.2 adds the `serve` subcommand to run.py
uv run --frozen python run.py serve            # blocks; leave it running
# ...and in a second shell:
curl -s http://127.0.0.1:8080/healthz
curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8080/healthz

# part 2.1 writes evals/ and wires it into the gate
uv run --frozen python run.py eval
echo $?
uv run --frozen python run.py check
echo $?
```

`--frozen` is on every `uv run` for the reason day 3 part 2.2 proved: without it `uv run` brings the
lockfile up to date before your command starts, and the `lock` check then reports on a repository the
invocation just repaired. The `.env` in place is the synthetic one; **no working provider key exists
on this machine**, and everything above runs without one.

## §4 Files this day prints

Four files whole, two as marked diffs. Nothing here reprints what an earlier day printed: `run.py`
was printed whole by day 4 and appears twice today only as marked additions, and `pyproject.toml`
appears as a three-line diff against the version day 6 left.

| File | Printed by |
| --- | --- |
| `projects/01-ask-desk/ask_desk/api.py` | part 1.1, whole — new today |
| `projects/01-ask-desk/pyproject.toml` | part 1.1, as a marked diff against day 6's version |
| `projects/01-ask-desk/run.py` | part 1.2, as a marked diff — the `serve` subcommand · part 2.1, as a marked diff — the `eval` subcommand and the sixth check |
| `projects/01-ask-desk/evals/harness.py` | part 2.1, whole — new today |
| `projects/01-ask-desk/evals/cases.json` | part 2.1, whole — new today, synthetic |
| `projects/01-ask-desk/evals/__init__.py` | part 2.1, whole — new today |

Part 2.2 prints no file: its subject is a two-word edit to `evals/harness.py` and what the evalset
does about it. Part 2.3 prints no file either; its subject is the twenty-six files that already
exist, and whether every one of them has a day against it.

## §5 Build brief

| File | What it must do |
| --- | --- |
| `projects/01-ask-desk/pyproject.toml` | `TODO(me)`: add both pins with one `uv add`. Before running it, predict whether `uv.lock` changes and whether `run.py check`'s `pins` check would have accepted `fastapi>=0.141`. |
| `projects/01-ask-desk/ask_desk/api.py` | `TODO(me)`: type it. Before starting the server, write down what you expect `key_wired` to say on your machine, and what status code `/healthz` returns when the key is absent. Then find out. |
| `projects/01-ask-desk/run.py` (`serve`) | `TODO(me)`: add the subcommand. Say why both of its imports are inside the function and not at the top of the file, and what breaks in `run.py check` if you move them up. |
| `projects/01-ask-desk/evals/cases.json` | `TODO(me)`: type both cases. Then add a third of your own that uses `forbids_text`, which nothing currently exercises — and make it go red on purpose before you make it green. |
| `projects/01-ask-desk/evals/harness.py` | `TODO(me)`: type it. Before running it, predict what `tools=` will print on each of the two rows, and which row will print a reason. |
| `projects/01-ask-desk/run.py` (`eval` and the sixth check) | `TODO(me)`: wire the evalset into `CHECKS`. Say why `evaluate()` and `check_evals_go_green()` both exist when both call `evals.main()`. |
| the failure rep | `TODO(me)`: weaken `if tool not in tools_called:` to `if False:`, run `run.py eval` and then `run.py check`, and watch the inverted case be the only thing that objects. Restore it. |
| `projects/01-ask-desk/SETUP.md` | `TODO(me)`: step 4 says *"Five checks"* and there are now six. Fix it, and say why the cold-clone day is where this was found rather than the day that added the sixth. |
| `projects/01-ask-desk/README.md` | `TODO(me)`: it offers *"The four commands"*; the driver now answers eight. Decide whether the fix is to list eight or to choose which four a stranger should meet first, and say why. |
| `projects/01-ask-desk/CODEMAP.md` | `TODO(me)`: move `evals/` out of "does not have yet" into the table with today's parts against it, and close the `tests/` row as a decision rather than filling it. Part 2.3 says which decision; you write the row. |
| the cold clone | `TODO(me)`: the true one — the folder alone, a working key, and every command in part 2.3's `Check yourself`. Record the first thing that does not work, because that is the finding. |

## §6 The check that must be able to fail

```text
cd projects/01-ask-desk
uv run --frozen python run.py eval     # the evalset alone
echo $?                                # 0 green, 1 a case failed
uv run --frozen python run.py check    # the gate: six checks, the last of which is the evalset
echo $?
cd ../.. && python p.py depth 10       # this day against the plan §5 contract
```

**How to make it go red on purpose — three ways, and the second is the day's real one.**

The first is a case. Add a `forbids_text` entry to `grounded-status-question` naming a word the
scripted answer contains, and watch the row go red with the answer quoted back at you.

The second is the day's deliberate failure and it is part 2.2. Change `if tool not in tools_called:`
to `if False:` in `evals/harness.py`. The grounding assertion can now never object — and the first
case still passes, greener than before, because the only thing left of it is a word in a string. The
inverted case is the only thing in the repository that notices, and it says so in a sentence naming
what was lost: *that assertion is no longer protecting any of the other cases.* Then run `run.py
check` with the line still weakened and watch the sixth check carry the same verdict up into the
gate.

The third is the surface. Stop the server and `curl` it: the request fails at the socket, which is a
different failure from a red `/healthz`, and it is worth seeing the difference once. Or move `.env`
aside and POST to `/ask`, which is `503` — while `/healthz` stays `200`, deliberately, because a
restart cannot produce a key.

For the document itself: delete a `## In production` heading from any part and run `python p.py depth
10`; it names the file and the missing section.

## §7 Request budget

**Zero model calls. Every demonstration in this day is offline, and that is a property of what is
being demonstrated rather than a limitation of this machine.**

`/healthz` calls nothing by design — that is part 1.1's entire subject, and a health check that made
a provider call would be the failure being taught. The evalset runs against `ask_desk/scripted.py`,
the local stand-in day 8 printed, so both cases in part 2.1 and both runs in part 2.2 contact
nothing. `run.py check` therefore costs zero requests, which is what makes it safe to run on every
edit.

The one path that would call out is `/ask`, and on this machine it does not succeed: there is no
working key, and part 1.2's transcript is the provider refusing. A successful `/ask` is a
`TODO(me)` in part 2.3, and the request count for it is unchanged from day 6 — **one question is at
least two model calls** when a tool is involved, bounded at `MAX_CALLS_PER_QUESTION`, which is `6`
and is published in the `/healthz` body.

The **ceiling** remains unknown and is not printed here. The provider's rate-limit page states that
limits "depend on a variety of factors (such as your usage tier) and can be viewed in Google AI
Studio" and publishes no RPM, TPM or RPD figure. `PACKAGES.md` carries the open
`TODO(me): read this project's live limits in Google AI Studio and paste them here, with the date.`
See ADR-0004. A number nobody can verify is worse than an acknowledged gap.

## §8 Traps

- **A health check that calls the model is worse than no health check.** It couples every replica's
  liveness to one external service, so they fail together, and the orchestrator's only response to
  all of them failing is to have none of them.
- **`key_wired` is a fact, never a verdict.** A missing key is a broken deployment. Restarting the
  process will not produce one, so failing the check on it produces an infinite restart loop and no
  key at the end of it.
- **Liveness and readiness are different probes with different consequences.** Readiness failing
  removes you from the load balancer and is reversible; liveness failing kills the process. If you
  only write one, write the liveness one and keep it dependency-free.
- **`from pydantic import BaseModel` is an undeclared direct dependency.** It resolves today because
  FastAPI depends on pydantic, and nothing in `pyproject.toml` says this project imports it. It is
  the sort of line that keeps working until a resolver changes its mind.
- **A bare `except Exception` returning 500 destroys routing, not detail.** Two of this desk's three
  failures are not application failures, so 500 for everything pages the wrong team for two of the
  three things that can go wrong.
- **`uvicorn.run` with a string enables the reloader and a second process.** Two processes means two
  agents and two of every model call you were carefully counting. Hand it the app object.
- **`host="0.0.0.0"` on a laptop binds every interface.** D1 is *run locally*; `127.0.0.1` is the
  address that says so, and the change belongs to the container in P02.
- **`Path("evals/cases.json")` resolves against the working directory.** From anywhere but the
  project root it finds nothing, the suite reports `0/0 case(s) passed`, and it exits `0`.
  `Path(__file__).with_name(...)` is the version that does not care where you were standing.
- **An eval against a live model is a check that will be muted.** It goes red on a Tuesday with no
  code change, twice, and the third time somebody marks the step as allowed to fail.
- **An eval that scores only the text passes an answer that was right by accident.** The trajectory —
  which tools were actually called — is the assertion that cannot be satisfied by wording.
- **An assertion that can no longer fail reports green, faster, and looks healthier.** Nothing in an
  ordinary suite says otherwise; only a case built to fail can.
- **Do not "fix" a red inverted case by deleting it.** The red row is the suite working. The fix is in
  the assertion it is complaining about.
- **A cold clone run in place is not a cold clone.** Everything the folder secretly depends on is
  still present, which is exactly the set of things being measured.
- **`.env` must never travel with a clone, and `uv.lock` must always.** One is a machine's file and
  one is the project's record of what a resolution produced.
- **The two documents a stranger reads first are the two nobody re-reads.** `README.md` and
  `SETUP.md` were both true when written and are both stale today; the cold-clone day is where that
  is found.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| `fastapi` current release | `https://pypi.org/pypi/fastapi/json` | 2026-09-10 | 0.141.1 — pinned with `==` in `pyproject.toml`, row added to this project's `PACKAGES.md` |
| `uvicorn` current release | `https://pypi.org/pypi/uvicorn/json` | 2026-09-10 | 0.52.4 — same treatment |
| `/healthz` answers over real HTTP | `run.py serve`, then `curl -s http://127.0.0.1:8080/healthz` | 2026-09-10 | `{"status":"ok","agent":"ask_desk","model":"gemini-3.8-flash","max_calls_per_question":6,"key_wired":true}` |
| `/healthz` returns 200 | the same URL with `-o /dev/null -w "%{http_code}\n"` | 2026-09-10 | `200`, with no provider call made to produce it |
| A provider refusal surfaces as 502 | `POST /ask` with a real question and this machine's synthetic key | 2026-09-10 | `HTTP 502`, body carrying the provider's own `400 INVALID_ARGUMENT ... API key not valid` |
| A malformed request is refused before any work | `POST /ask` with an empty question | 2026-09-10 | `422 string_too_short` — pydantic rejected it, `agent.ask` was never entered |
| The evalset is green | `uv run --frozen python run.py eval` | 2026-09-10 | `2/2 case(s) passed`, exit `0`, both cases against the scripted double |
| The inverted case explains itself when green | the same command | 2026-09-10 | `green ungrounded-answer-is-caught (inverted)` printing `failed as intended: ...` |
| The evalset catches its own weakened assertion | `if tool not in tools_called:` replaced with `if False:`, then `run.py eval` | 2026-09-10 | `RED ungrounded-answer-is-caught`, `1/2 case(s) passed`, exit `1` — and the first case still green |
| The full gate is green with the evalset in it | `uv run --frozen python run.py check` | 2026-09-10 | six checks green, the evalset's own rows inside the output, `0 problem(s)`, exit `0` |
| Every tracked file maps to a day | `git ls-files` in `projects/01-ask-desk` against `CODEMAP.md` and the day documents | 2026-09-10 | twenty-six files, none owed by no day; `evals/` closed today, `tests/` closed as a decision |
| `SETUP.md` is stale | reading `projects/01-ask-desk/SETUP.md` step 4 against `run.py`'s `CHECKS` | 2026-09-10 | the document says five checks; there are six |
| `README.md` is stale | reading `projects/01-ask-desk/README.md` against `run.py`'s `main` | 2026-09-10 | the document offers four commands; the driver answers eight |
| The provider's ceiling is still unpublished | `https://ai.google.dev/gemini-api/docs/rate-limits` | 2026-09-10 | "Rate limits depend on a variety of factors (such as your usage tier) and can be viewed in Google AI Studio" — no RPM, TPM or RPD figure; the `TODO(me)` in `PACKAGES.md` stands |
| No cold clone was run on a clean machine | this repository, and the absence of any such transcript | 2026-09-10 | everything above was run **in place**; the clean-machine half and every key-dependent command are recorded as owed in part 2.3 |

## §10 Ledger & commit

**`docs/PROGRESS.md`:**

```text
| 10 | 2026-09-10 | DP-01, EV-01 | 5 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the terms this day defined for the first time:

```text
| Health check | An endpoint a process answers so that another program can decide whether to send it traffic or restart it. It may only test things a restart can fix, because restarting is the only lever its caller has. | day 10 part 1.1 | liveness probe, readiness probe, `/healthz` |
| Eval | A test whose subject is a system's behaviour rather than a function's return value, written for a system whose correct output is not one fixed string. | day 10 part 2.1 | a behavioural test |
| Evalset | A collection of eval cases held as data rather than as code, run together, reporting one verdict as an exit status. | day 10 part 2.1 | the eval suite, `cases.json` |
| Trajectory | What an agent actually did during a run — which tools it called, in what order, before it answered. Assertable in a way prose is not, because a right answer nobody looked up leaves no tool call behind. | day 10 part 2.1 | the tool path, `expects_tools` |
| Inverted case | An eval case whose declared expectation is its own failure, so that it goes red when the assertion it depends on stops objecting. It tests the detector rather than the system. | day 10 part 2.2 | `expect_fail`, a negative test |
```

**`projects/01-ask-desk/PACKAGES.md`** — two rows, both read live today:

```text
| fastapi | 0.141.1 | 2026-09-10 | 10 | The D1 surface. Latest release, read from `https://pypi.org/pypi/fastapi/json`. Pinned with `==` because `run.py check`'s `pins` check refuses a floor. |
| uvicorn | 0.52.4 | 2026-09-10 | 10 | The server that holds the socket; fastapi does not serve anything on its own. Latest release, read from `https://pypi.org/pypi/uvicorn/json`. Pinned with `==` for the same reason. |
```

**`docs/PINS.md`** — nothing to add. Both versions above belong to a project, and this project's own
`PACKAGES.md` is where a project's pins live (plan §9); `docs/PINS.md` records only what the
authoring repository itself depends on, and that has not moved.

**`docs/SOURCES.md`** — nothing to add. This day cites two PyPI JSON endpoints for release versions
and one provider documentation page for the absence of a number; neither is a record with a
resolvable identifier, and both are dated in §9, which is what that table is for. Same call days 3
and 4 made.

**Commit:**

```text
day 10: P01 Ask Desk · 7 — Ship D1: api_server, /healthz, the first eval that can go red; cold clone — closes DP-01, EV-01
```
