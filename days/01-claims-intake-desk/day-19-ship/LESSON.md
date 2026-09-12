---
project: "P01"
day: 19
title: "Ship"
spine: 17
kind: gate
deploy_tier: D3
plan_version: "v4.1.0"
parts: 7
files_printed: [Dockerfile, .dockerignore, claims_desk/serve.py, compose.yaml, .github/workflows/check.yml, README.md, CODEMAP.md, tests/test_ship.py]
generated: "2026-09-12"
status: written
commit: ""
---

> **Yesterday:** evals — the whole desk run as a person runs it and marked against the answer key,
> on its verdicts, its route, its letters and its bill; a baseline that said what the model is
> worth; and the gate that went red when the in-force check was disabled.
> **Today:** ship — the desk as a sealed kit that travels: a stateless image on the interpreter day
> 0 pinned, a service with a health route that asks before it answers, the boundary beside it as a
> sidecar on a private network, a pipeline that runs both gates on an empty machine, the cold clone
> run for real, and the two documents a stranger reads first.
> **Tomorrow:** nothing. This is day 19 of 19. The next thing to open is a different project's
> day 0, on a bare machine, with none of this assumed.

## §1 The scene

The insurer opens a branch office in another town, and the desk has to travel.

What travels is a kit. The forms, the handbook, the counter software on a sealed drive, and a card
that says exactly which version of each — so the branch runs the desk that was audited and not
whatever its own machines happened to have. What does not travel is the safe key: the branch manager
is handed that in person, on the morning, because the kit goes through a courier and a warehouse and
gets copied for the next branch, and every copy would carry the key. Beside the counter goes a line
to the policy department, on a private exchange nobody outside the branch can dial. And the regional
inspector audits the branch on every change, on a schedule the branch does not control.

Then the test that decides whether any of it was real: the branch opens with the kit and nothing
else. Nobody from head office goes along. If the card assumes a step only head office ever did, the
branch does not open, and the person who finds out is the one least able to fix it.

Nineteen days of this desk ran on one machine that was set up over nineteen days. Today packs it —
and then clones it into an empty folder with an empty cache and runs both gates from the README
alone. `292 passed`, `eval: green`, and day 0's four `ok` lines on a tree that inherited nothing.
Then the clone that forgot its lockfile, which is the failure every hand-over meets, stopped by one
flag with the fix in the message.

Two honest limits run through the day. This machine has no Docker, so the image was never built and
the sidecar never ran: those transcripts are marked `TODO(me)` with the exact commands, and every
line of the files they would run was checked against the tool's own reference today. And the
pipeline has no service to run on from a throwaway repository: its file was parsed and its actions
looked up live, and its first run is a `TODO(me)` too. What did run is everything a machine without
Docker can run — the service, the driver, the gates, and the clone.

## §2 The map

Seven parts in five sections: the container, the sidecar, the pipeline, the clone, and the tests.

### 1 · The container

The kit: the image, what stays out of it, and the process that keeps it running.

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-container/1.1-stateless-container.md) | The stateless container | What goes in the image, what is kept out, and why the order of two files matters? | working |
| [1.2](parts/01-the-container/1.2-desk-as-a-service.md) | The desk as a service | How does the desk stay up, and what does an honest health check actually ask? | working |

### 2 · Together

The line to the policy department, on a private exchange.

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-together/2.1-boundary-beside-the-desk.md) | The boundary beside the desk | How do two containers share a network nobody else can join, and where does the key enter? | production |

### 3 · The pipeline

The inspector who audits on every change.

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-the-pipeline/3.1-pipeline-that-runs-both-gates.md) | The pipeline that runs both gates | What does a bare machine need, in what order, to run day 18's gates? | production |

### 4 · The cold clone

The branch opens with the kit and nothing else.

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [4.1](parts/04-the-cold-clone/4.1-cold-clone-run-for-real.md) | The cold clone, run for real · **failure** | Does a stranger's clone start, and what stops the one that forgot its lockfile? | production |
| [4.2](parts/04-the-cold-clone/4.2-strangers-entry-point.md) | The stranger's entry point | What do the README and the CODEMAP have to say, and what does the CODEMAP prove? | production |

### 5 · Holding it

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [5.1](parts/05-holding-it/5.1-what-the-tests-hold.md) | What the tests hold | What can a test hold about an image nobody built? | production |

## §3 Setup — run this

Nothing is installed. Two folders are made, and the day's first command is the one that proves the
gate is where day 18 left it.

```bash
./run check

mkdir -p .github/workflows
docker --version
```

Expect `280 passed` from the first command — day 18's total on a tree built from the printed files
(`283` if yours carries day 13's three unprinted assertions) — and `292` at the end of the day,
twelve more. The third command tells you which of the day's transcripts you can reproduce: on this
machine it printed `docker: command not found`, and every block marked `TODO(me)` below is one
that needs it.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `Dockerfile` | part 1.1 |
| `.dockerignore` | part 1.1 |
| `claims_desk/serve.py` | part 1.2 |
| `compose.yaml` | part 2.1 |
| `.github/workflows/check.yml` | part 3.1 |
| `README.md` | part 4.2 |
| `CODEMAP.md` | part 4.2 |
| `tests/test_ship.py` | part 5.1 |

Three earlier files change, each as a marked diff naming the day of this project that printed the
original: `claims_mcp/__main__.py` (day 4) in part 1.1 — the boundary's host becomes a variable;
`run` (day 1, last changed day 18) in part 1.2 — the last two planned commands, the `eval` line day
18 forgot to document, and a one-line answer for a program the machine does not have; and
`.gitignore` (day 0, last changed day 18) in part 4.2 — `data/claims/`, so a clone carries no
decisions.

## §5 Build brief

Write `.dockerignore` before `Dockerfile`, for the reason day 0 wrote `.gitignore` before `.env`.
Then `serve.py` and the driver, and run the service before touching compose — the health route is
what compose's health check will call, and part 1.2's port failure is worth meeting on a laptop
rather than in a container. Then compose, the workflow, and the clone. The README and CODEMAP last,
because they describe a finished system. Then the reps:

| File | What it must do |
| --- | --- |
| `Dockerfile` | `TODO(me)`: the three build commands on a machine with Docker, pasted into part 1.1; the image's size recorded in `PACKAGES.md` with the date. |
| `Dockerfile` | `TODO(me)`: the review comment — a health check that proves the desk is up, separate from the readiness question that asks the boundary. Say what compose can and cannot do with the difference. |
| `claims_desk/serve.py` | `TODO(me)`: the review comment — a shared secret on `POST /queue`, or the port unpublished. Decide, change `compose.yaml` or `serve.py`, and write the decision into the README. |
| `compose.yaml` | `TODO(me)`: `./run up` on a machine with Docker, with the queue's wall time beside day 17's sixty-eight seconds. |
| `compose.yaml` | `TODO(me)`: a named volume for the claim files, or a sentence in the README saying they are not persistent. |
| `.github/workflows/check.yml` | `TODO(me)`: the first run on the service, with `gh run list --workflow check --limit 3` pasted into part 3.1. |
| `.github/workflows/check.yml` | `TODO(me)`: both actions pinned by commit hash with the version in a comment, and where you read each hash. |
| Your own clone | `TODO(me)`: the cold clone on a Linux machine — the pipeline runner counts — with its `uv sync --locked` transcript beside part 4.1's, and the packages that differ named. |
| `README.md` | `TODO(me)`: the last section, *what I would change*, rewritten in your own words after your own twenty days. The four bullets printed are one author's; yours may not match. |

## §6 The check that must be able to fail

Two gates, and the clone:

```bash
./run check
./run eval
```

Green for the first is `All checks passed!`, `292 passed`, and day 0's four `ok` lines. Green for
the second is unchanged from day 18: twelve `ok`, `desk     12/12`, `eval: green`.

Ways to make `./run check` red:

1. **Return `True, {"ok": True}` from `health()`** without asking the boundary. Three tests red,
   and the one that matters is `test_healthz_is_503_when_the_boundary_is_gone` reading `200`.
2. **Change `FROM python:3.12.12-slim` to `FROM python:3.12-slim`.** The test that greps the
   `Dockerfile` for the version in `.python-version` goes red.
3. **Add `ports:` to the `boundary` service.** `compose.count("ports:") == 1` fails — the invariant
   that the boundary is never published.
4. **Move `!.env.example` above `.env.*` in `.dockerignore`.** The order assertion fails, for day
   0's reason.
5. **Write `uv sync` without `--locked` in the workflow.** `"uv sync --locked" in workflow` fails.
6. **Put `serve` back into `PLANNED`.** The driver test fails on the empty map.

And the two the day is built around, neither of which a test can hold:

- **Part 4.1** — clone the branch that forgot `uv.lock` and read `Unable to find lockfile`. Bump a
  pin without relocking and read `needs to be updated`. Both real, both from `--locked`.
- **Part 1.2** — the first `./run serve` on this machine did not listen at all:
  `PermissionError: [WinError 10013]`, because another process held port 8080. The port became a
  variable.

## §7 Request budget

**Five model calls allowed per notification, unchanged. `POST /queue` and `./run eval` each spend
fifteen across the queue, unchanged** — the service runs the same `run_queue`, and the health route
makes a boundary call and no model call. Nothing in this day touches a provider.

What this day changes is *where* the calls would be made. The pipeline runs `./run check` — which
includes day 18's framework evaluator at `num_runs=1`, twelve classifier calls — and `./run eval`
on every push. Against the stand-ins that is free and it is what the workflow's `env` block relies
on. Against a real provider it would be twenty-seven requests per push, from a machine whose key
would have to be in the service's secrets; that is the production note in part 3.1, and it is why
the pipeline's key is a string that says it is not one.

The health check is the other new cost, and it is not a model cost: one boundary call every thirty
seconds, forever. On stdio that is a subprocess launch, 1.7 seconds by day 17's measurement, every
thirty seconds. In compose it is one HTTP request to the sidecar. Part 1.2's production note has
what the launch does to a busy `/queue`.

## §8 Traps

- **`.dockerignore` before the first build**, as `.gitignore` before `.env`. A layer that once held
  a secret holds it in every image built from it.
- **`--locked`, in all three places** — the image, the pipeline, the clone — or the lock is a
  suggestion.
- **Bind-mount the lock and the project for the dependency layer**, or every code change reinstalls
  a hundred and twenty packages.
- **`UV_PYTHON_DOWNLOADS=0` in the image.** The base image is the interpreter; a download is a
  second one nobody pinned.
- **Not root.** Create the user before the copy, so `--chown` has someone to give the files to.
- **A health check that cannot fail is not a check.** Ask the boundary something it cannot get
  wrong, and treat `found: false` as the pass.
- **Report the leaf, not the wrapper.** `ExceptionGroup` tells nobody anything; `ConnectError`
  does.
- **503, not 500, for *not now*.** A load balancer reads the first and ignores the second.
- **The port is a variable** because the first port you pick is held by something that is not
  yours, and killing it is not a fix.
- **`0.0.0.0` in a container is one interface**, on a network compose made for two services. It is
  day 4's decision, not a reversal of it, and only while the port stays unpublished.
- **`depends_on` with `condition: service_healthy`**, or the desk's first health check finds nothing
  listening and the `503` is true for four seconds and confusing for an hour.
- **`env_file` on the desk and not on the boundary.** The key goes where it is used, and nowhere
  else.
- **A key that says it is not a key** in the pipeline, so day 0's check passes and a provider's
  `401` would quote it back.
- **Actions by major tag are pointers somebody else moves.** The hash form is the production one.
- **An empty folder, an empty cache, the README's commands verbatim** — or the clone is not cold.
- **`uv.lock` is committed.** It was in `.gitignore` in half the templates you learned from.
- **`FileNotFoundError` from `subprocess` names a file in Python, not the program that is missing.**
  Catch it in the driver and say the program's name.
- **The README is written last** because it describes a finished system; the CODEMAP is generated,
  never typed.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| The build tool's Dockerfile reference | `https://docs.docker.com/reference/dockerfile/` | 2026-09-12 | `# syntax=docker/dockerfile:1` is the directive "most users will want"; `HEALTHCHECK [OPTIONS] CMD <command>` with `--interval`, `--timeout`, `--start-period`, `--retries`; `USER <user>[:<group>]`; `COPY --from=<image|stage>`; `RUN --mount=type=cache,target=/path`; `EXPOSE <port>`; `CMD ["executable","param1"]` exec form. |
| uv's own image guidance | `https://docs.astral.sh/uv/guides/integration/docker/` | 2026-09-12 | `COPY --from=ghcr.io/astral-sh/uv:0.12.13 /uv /uvx /bin/` is the documented pinned form ("best practice to pin to a specific uv version"); the two-`uv sync` pattern with bind mounts on `uv.lock` and `pyproject.toml` and `--no-install-project`; `ENV PATH="/app/.venv/bin:$PATH"`; `UV_COMPILE_BYTECODE=1` and `UV_LINK_MODE=copy`; `--no-dev` disables development dependencies. Python-based derived tags are `trixie` and `alpine` only, so the desk takes `python:3.12.12-slim` and copies uv in. |
| uv 0.12.3 exists as a release | `https://github.com/astral-sh/uv/releases/tag/0.12.3` | 2026-09-12 | Released 2026-08-07 — the version `PACKAGES.md` recorded on day 0, so the image and the pipeline pin the version the desk was built with. |
| `python:3.12.12-slim` exists | `https://hub.docker.com/v2/repositories/library/python/tags?name=3.12.12-slim` | 2026-09-12 | `3.12.12-slim`, `3.12.12-slim-trixie` and `3.12.12-slim-bookworm`, last updated 2026-02-25 to 2026-02-27. |
| The compose file reference | `https://docs.docker.com/reference/compose-file/services/` | 2026-09-12 | `depends_on: <service>: condition: service_healthy`; `healthcheck: test: ["CMD", ...]` with `interval`, `timeout`, `retries`, `start_period`; `env_file: .env`; `environment:` as a map; `build: context:`; `ports: - "127.0.0.1:8001:8001"`; `command:`; `read_only: true`; `user:`. No top-level `version` key is documented. |
| The workflow syntax reference | `https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax` | 2026-09-12 | `on: push: branches:` and `pull_request: branches:`; `jobs.<id>.runs-on`; `steps` with `uses` and `run`; job-level `env`; `permissions: contents: read`. |
| The runner label | `https://docs.github.com/en/actions/reference/runners/github-hosted-runners` | 2026-09-12 | `ubuntu-latest` is a standard label and maps to Ubuntu 24.04. |
| The checkout action's current major | `https://github.com/actions/checkout/releases` | 2026-09-12 | Latest release `v7.0.1`, 2026-07-20; `v5.1.0` and `v6.1.0` also current on their majors. |
| The uv action's current major and inputs | `https://github.com/astral-sh/setup-uv` | 2026-09-12 | README recommends `astral-sh/setup-uv@bec219d24cd3e171d82865faccec33120bb574f4 # v10.1.0`; inputs `version`, `enable-cache`, `python-version`. |
| The framework's own server | the installed `google-adk` 2.8.0, `adk --help` | 2026-09-12 | `api_server  Starts a FastAPI server for agents.` — for a root agent, which this desk has not; named in part 1.2, not used. |
| Docker on this machine | `docker --version` | 2026-09-12 | `docker: command not found`. Every image and compose transcript is a `TODO(me)` with its exact command. |
| The dependency layer's flags | this project, `uv sync --locked --no-dev --dry-run` | 2026-09-12 | `Resolved 125 packages`; `Would uninstall 5 packages` — pytest, ruff, and pytest's three. |
| The service | this project, `CLAIMS_DESK_PORT=8090 ./run serve` | 2026-09-12 | `/healthz` 200 with `"boundary": "stdio"`; `/decide` 404; `POST /queue` `{"deficiency": 7, "fast-track": 4, "pending": 1}` sixty-four seconds later; with the boundary at a dead port, 503 and `"error": "ConnectError"`. |
| The port that was taken | this project, `./run serve` on 8080 | 2026-09-12 | `PermissionError: [WinError 10013]`; `netstat` shows process 15664 listening on `127.0.0.1:8080`, not this project's. |
| The driver on a missing program | this project, `./run up` | 2026-09-12 | Before the diff, a traceback ending `FileNotFoundError: [WinError 2]`; after it, `docker is not installed on this machine` and exit 127. |
| Both new files are the YAML they appear to be | this project, `ruamel.yaml` | 2026-09-12 | compose: `['boundary', 'desk']`, the health condition, one loopback port; workflow: `check ['push', 'pull_request']` and seven named steps. |
| The cold clone | an empty folder, `UV_CACHE_DIR` empty | 2026-09-12 | 74 files, no `.env`, no `.venv`; `Resolved 125 packages in 1ms`, 123 downloaded and installed in 25.51s; `292 passed`; four `ok` lines; `eval: green`. |
| The clone that forgot its lockfile | a branch with `uv.lock` removed | 2026-09-12 | `error: Unable to find lockfile at `uv.lock`, but `--locked` was provided.` |
| A pin moved without the lock | the clone, `ruff==0.16.7` in `pyproject.toml` | 2026-09-12 | `error: The lockfile at `uv.lock` needs to be updated, but `--locked` was provided.` |
| The gate | this project, `./run check` | 2026-09-12 | ruff clean, `292 passed`, day 0's four checks green. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 01 | 19 | 2026-09-12 | Ship | 8 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — new rows:

```text
| Image | The desk packed as a sealed kit: an interpreter, the packages a lockfile names, the code, and a user — built in layers that are each a snapshot, so a file a layer once held stays readable in it whatever a later layer deletes. | P01 day 19 part 1.1 | a container image |
| Stateless | Of a container: nothing in it outlives a request — no session, no cache, no counter — so a second copy answers as the first would and killing either loses nothing. A property of the code, not of the packaging. | P01 day 19 part 1.1 | share-nothing |
| Health check | A route or command that says whether a process can do its job right now, by asking the one thing it depends on a question it cannot get wrong. One that cannot fail is a sign that says open with nobody to turn it round. | P01 day 19 part 1.2 | liveness probe, `/healthz` |
| Sidecar | A second container started beside the first, from the same image or another, reached over a private network by service name and outliving any single request. Here the boundary, so the desk's container launches nothing. | P01 day 19 part 2.1 | a companion container |
| Private network | A network a compose file creates for the services it names, on which a service is reached by its name and nothing outside can route. The substitute for authentication a boundary does not have, and only while its port stays unpublished. | P01 day 19 part 2.1 | the compose network |
| Pipeline | The gates, run by a machine nobody prepared, on every change, with a change landing only if they are green. Not a new check — the checks made non-optional. | P01 day 19 part 3.1 | CI, the workflow |
| Cold clone | A fresh clone into a folder that never held the project, with a package cache that never held its packages, following the README verbatim, with what it printed recorded. The only test that a stranger's machine starts. | P01 day 19 part 4.1 | the from-nothing test |
| Lockfile | The exact versions of every package, written down once and installed with a flag that refuses to run if the project disagrees with it. In the image, the pipeline and the clone alike; or it is a suggestion. | P01 day 19 part 4.1 | `uv.lock`, the lock |
| Code map | Every file in the finished project and the day that prints it, generated from the day hubs rather than typed, so that a file no day printed is a red line and not a surprise. | P01 day 19 part 4.2 | `CODEMAP.md`, the completeness proof |
```

**This project's `PACKAGES.md`** — appended rows, in the project:

```text
| python (image base) | 3.12.12-slim | 2026-09-12 | 19 | The registry's tag list, read live. The same 3.12.12 as `.python-version`; `slim` because the desk needs no compiler. |
| uv (image and pipeline) | 0.12.3 | 2026-09-12 | 19 | `ghcr.io/astral-sh/uv:0.12.3` in the Dockerfile and `version: "0.12.3"` in the workflow — the version day 0 observed on this machine, so all three places agree. |
| actions/checkout | v7 | 2026-09-12 | 19 | The current major on the action's releases page (v7.0.1). |
| astral-sh/setup-uv | v10 | 2026-09-12 | 19 | The current major in the action's README (v10.1.0, recommended by commit hash). |
```

**`docs/PINS.md`** — no row is owed. Every version above is a project pin.

**`docs/SOURCES.md`** — no row is owed. Nothing with a citation identifier was cited; the eight
reference pages are in §9 with their URLs and the date.

**Commit:**

```text
P01 day 19: Ship
```
