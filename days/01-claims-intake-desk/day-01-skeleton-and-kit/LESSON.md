---
project: "P01"
day: 1
title: "The skeleton and the kit"
spine: 1
kind: mechanism
deploy_tier: D3
plan_version: "v4.1.0"
parts: 9
files_printed: [pyproject.toml, claims_desk/__init__.py, claims_desk/util/__init__.py, claims_desk/util/keys.py, claims_desk/util/logging.py, claims_desk/util/backoff.py, claims_desk/util/budget.py, claims_desk/models.py, run, tests/test_kit.py]
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** a folder with a pinned interpreter, a history that starts with the brief, a rule
> that exists before the first secret, and a four-question check that goes red.
> **Today:** that folder becomes a project — one declared environment, one importable package, one
> door to operate it through, and the four pieces of kit every later day will reach for.
> **Tomorrow:** the desk gets something to work on — the synthetic policy store, the twelve
> notifications, and the shape of the record an insurer actually keeps.

## §1 The scene

A loss adjuster leaves the office with a kit bag. Camera, damp meter, moisture probe, forms. It is
standard issue and it is checked before it goes out, and both of those facts are doing work: the
readings two adjusters take are comparable because the instruments are the same, and they are
trustworthy because somebody put the meter on a dry block before it left.

Today this desk gets its bag. Not the claims logic — none of that exists yet, and it would be the
wrong thing to build first. What gets built is the four things every later day is going to reach
for without thinking: the key, read in one place and never printed; the log line, machine-readable
and redacted at the writer; the retry that waits what the provider asked for and escalates rather
than inventing an answer; and the ceiling that refuses when a claim has cost more model calls than
it was allowed.

Around the bag goes the frame that makes it reproducible: a `pyproject.toml` that says which
versions, a package so every import starts with the same name, a registry naming the exact model
this desk may use, and a driver so that operating this project is one word rather than four
remembered commands. Then nine tests, and a deliberate break to prove they can fail.

None of it calls a model. Everything it will do to a model call is decided today.

## §2 The map

Three sections. **Section 1 is the frame** — the declared environment, the importable name, and
the one door. **Section 2 is the kit** — four modules, each holding one promise the whole desk
will lean on. **Section 3 is what makes both trustworthy** — the model registry that refuses
anything but an exact ID, and the gate that goes red when a promise stops being true.

### 1 · The skeleton — the frame around the work

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-skeleton/1.1-one-project-declared-once.md) | One project, declared once | What decides which versions this desk runs, and where is that written? | foundation |
| [1.2](parts/01-the-skeleton/1.2-package-every-import-starts-with.md) | The package, and the name every import starts with | Why a package rather than a folder of scripts? | foundation |
| [1.3](parts/01-the-skeleton/1.3-one-door-into-the-desk.md) | One door into the desk | How does anybody find out what this project can do? | working |

### 2 · The kit — four promises, four modules

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-the-kit/2.1-key-read-once.md) | The key, read once | How does a secret reach the desk without reaching a log? | working |
| [2.2](parts/02-the-kit/2.2-one-line-one-record.md) | One line, one record | How do you write a log a person can still use in six months? | working |
| [2.3](parts/02-the-kit/2.3-wait-what-you-were-told-to-wait.md) | Wait what you were told to wait | What does a retry do when the provider says how long to wait — and when it runs out of attempts? | working |
| [2.4](parts/02-the-kit/2.4-ceiling-that-refuses.md) | The ceiling that refuses | What stops five agents spending an unbounded number of model calls on one claim? | production |

### 3 · The registry and the gate — what makes the rest trustworthy

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-the-registry/3.1-registry-that-refuses-an-alias.md) | The registry that refuses an alias | Which model decides a claim, and how is that enforced rather than promised? | production |
| [3.2](parts/03-the-registry/3.2-gate-that-goes-red.md) | The gate that goes red | How do you know the tests test anything? | production |

## §3 Setup — run this

The folder from day 0, with the pinned interpreter and the ignore rule already in it. Everything
below is run from the project root.

```bash
mkdir -p claims_desk/util tests

uv sync
uv run ruff --version
uv run pytest --version
```

Write `pyproject.toml` first — `uv sync` reads it, and reading nothing is how you get an empty
environment and a confusing error. Expect `ruff 0.16.6` and `pytest 9.1.1`.

If `uv sync` fails part-way with a message about hardlinks and `os error 396`, your project sits in
a cloud-synced folder; re-run it as `uv sync --link-mode=copy`. Part 1.1 carries the whole error.

Once `run` exists, mark it executable in git so a clone on another operating system can use it:

```bash
git update-index --chmod=+x run
git ls-files -s run
```

Expect `100755`. On this machine the working copy was already `rwxr-xr-x` and git had still
recorded `100644`, which is a mode that only bites the person who clones your repository.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `pyproject.toml` | part 1.1 |
| `claims_desk/__init__.py` | part 1.2 |
| `claims_desk/util/__init__.py` | part 1.2 |
| `claims_desk/util/keys.py` | part 2.1 |
| `claims_desk/util/logging.py` | part 2.2 |
| `claims_desk/util/backoff.py` | part 2.3 |
| `claims_desk/util/budget.py` | part 2.4 |
| `claims_desk/models.py` | part 3.1 |
| `run` | part 1.3 |
| `tests/test_kit.py` | part 3.2 |

**`uv.lock` is written, committed, and not printed by any day.** It is over a hundred lines of
tool-written hashes that no person should edit, and the thing a reader actually needs is the
command that produces it: `uv sync`, in §3 above and in part 1.1.

## §5 Build brief

Type the ten files above, in the order the parts print them, then append today's two pinned
versions to `PACKAGES.md`. The reps are marked `TODO(me)` and are left unsolved:

| File | What it must do |
| --- | --- |
| `PACKAGES.md` | `TODO(me)`: append a dated row for `ruff` and one for `pytest`, with the version **your** `uv sync` installed and the command you read it from. |
| `claims_desk/util/logging.py` | `TODO(me)`: `redact` recurses into dictionaries and walks straight past lists. A secret inside a list of dictionaries reaches the page. Fix it, and add the test first. |
| `claims_desk/util/backoff.py` | `TODO(me)`: add jitter — a small random fraction on each wait — without breaking `test_delays_double_and_stop_one_short_of_the_attempts`. Decide where the randomness has to live for the schedule to stay assertable. |
| `claims_desk/util/budget.py` | `TODO(me)`: `spend` refuses the call that would exceed the limit. Add a way for a caller to ask "may I?" without spending, and say why the answer can go stale. |
| `run` | `TODO(me)`: `./run check` stops at the first failing step. Add `--keep-going` so a person fixing a broken machine sees every failure at once, and keep the exit status honest. |

## §6 The check that must be able to fail

```bash
./run check
```

Green is three steps: `All checks passed!` from ruff, `9 passed` from pytest, and day 0's four
`ok` lines, ending in `OK check` and exit status 0.

Three ways to make it red, and part 3.2 does the second one in full:

1. **Break the pin.** Change `PRIMARY` in `claims_desk/models.py` to `"gemini-flash-latest"` and
   run the gate. Expect `DID NOT RAISE UnpinnedModel`.
2. **Weaken the retry.** Make `retry` use the doubling schedule even when `retry_after` is set, and
   watch `test_retry_prefers_the_interval_the_provider_asked_for` fail with `[1.0, 2.0]` instead of
   `[7.5, 7.5]`.
3. **Take the recursion out of `redact`.** The nested `auth_token` assertion goes red, and the
   top-level one does not — which is the difference the test was written for.

## §7 Request budget

**Zero.** Nothing today calls a model. `claims_desk/models.py` names two of them and never contacts
either; `budget.py` counts calls that no code has yet made.

That is the point of the day. The ceiling, the retry policy and the model choice are all decided
before the first call, because each of them is a decision that is cheap now and expensive once
five agents have been written against the absence of one. Day 7 makes the first call, and it will
make it through this kit.

## §8 Traps

- **`uv sync` in a cloud-synced folder.** OneDrive, Dropbox and iCloud refuse the hardlinks `uv`
  installs with, and it fails half-way with `os error 396`. Use `uv sync --link-mode=copy`, or set
  `UV_LINK_MODE=copy` once in your environment.
- **`package = false` and pytest.** With the project not installed into `.venv`, `pytest` cannot
  import `claims_desk` — the tests fail with `ModuleNotFoundError` while `uv run python` imports it
  perfectly. The fix is `pythonpath = ["."]` under `[tool.pytest.ini_options]`, and it is already
  in the printed `pyproject.toml`.
- **The driver's executable bit.** `./run` works on this machine because the working copy is
  executable; git may still have recorded `100644`, and then a clone on Linux cannot run it.
  `git update-index --chmod=+x run`, and check with `git ls-files -s run`.
- **Anything this project prints is ASCII.** Day 0 learned it from a check message; `run` had to
  learn it again in its list of unbuilt commands. A Windows console turns an em dash into a
  replacement character, and a person reading a message about a missing command should not have a
  second mystery.
- **Ruff will ask for syntax your pin allows.** `target-version = "py312"` is what makes `UP047`
  suggest `def retry[T](...)` over a `TypeVar`. That is the setting working, not a linter being
  fussy — but it means lint output is specific to the pinned version, which is another reason the
  pin is exact.
- **`.venv/` is never committed and never copied.** It is ignored from day 0. Rebuild it with
  `uv sync` on every machine; moving one between machines is how you get an environment nobody can
  explain.
- **A test file that stops being collected reports `0 passed` and exits zero.** Read the count, not
  just the colour, whenever the number of tests should have changed.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| ruff's latest release | `https://pypi.org/pypi/ruff/json` | 2026-09-10 | `0.16.6`, pinned with `==` in the `dev` group and installed by `uv sync` as `ruff==0.16.6`. |
| pytest's latest release | `https://pypi.org/pypi/pytest/json` | 2026-09-10 | `9.1.1`, pinned the same way; `uv run pytest --version` reported `pytest 9.1.1`. |
| The model IDs this desk may pin | `https://ai.google.dev/gemini-api/docs/models` | 2026-09-10 | `gemini-3.8-flash` — "New Stable", "Our most intelligent Flash model…"; `gemini-3.7-flash` — "Stable", "Our previous-generation Flash model…"; `gemini-3.5-flash` — "Stable", "Our legacy Flash model…". `gemini-3.6-flash` also listed. |
| What a `-latest` alias means | `https://ai.google.dev/gemini-api/docs/models` | 2026-09-10 | "This alias will get hot-swapped with every new release of a specific model variation." Quoted in `claims_desk/models.py` and the reason `pinned()` refuses one. |
| Every transcript in this day | this project, run in a throwaway directory | 2026-09-10 | `./run check` green with 9 tests; the `os error 396` hardlink failure; the `ModuleNotFoundError` from pytest; the em-dash mojibake; the four kit error messages; the red gate after the registry was broken on purpose. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 01 | 1 | 2026-09-10 | The skeleton and the kit | 9 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — the first seven restate definitions the glossary already carries,
re-anchored to this project; the rest are new:

```text
| Floor | A dependency or interpreter requirement written as `>=`, which states what is too old and leaves the choice to whichever machine resolves it. Correct for a library, never sufficient for an application. | P01 day 1 part 1.1 | a lower bound, a range |
| Lockfile | The tool-written record of what a resolution actually produced — exact versions and content hashes — as against `pyproject.toml`, which records what was asked for. | P01 day 1 part 1.1 | the lock, `uv.lock` |
| Virtual environment | A directory holding a link back to a real interpreter and its own installed packages, marked as one by a `pyvenv.cfg` beside the executable. Not a shell mode and not a variable. | P01 day 1 part 1.1 | venv, the environment |
| Dev dependency | A package the project needs to be checked but not to run — declared in its own group so it is installed for the gate and left out of the container that ships. | P01 day 1 part 1.1 | a development dependency, the dev group |
| Driver | The one script a repository is operated through, so a command is found by reading one file rather than by remembering. `./run` here. | P01 day 1 part 1.3 | the runner |
| Structured logging | Writing one machine-readable object per line — here one JSON object — rather than a sentence assembled for a human, so a run's log can be filtered, counted and diffed months later without a parser anybody maintains. | P01 day 1 part 2.2 | JSON lines, structured logs |
| Redaction | Removing a value from a log record before it is written, decided by the field's name rather than by its contents, and done at the writer so that no call site has to remember. | P01 day 1 part 2.2 | masking, scrubbing |
| Request budget | A written-down ceiling on how many model calls a unit of work may make, enforced by code that refuses rather than by a paragraph in a document, and counted across the whole cast rather than per agent. | P01 day 1 part 2.4 | a call budget, the bound |
| Model alias | A model name that stands in for whichever model currently holds a role rather than for a model — `-latest`, documented as hot-swapped on every release. A floor wearing a version's clothes. | P01 day 1 part 3.1 | a moving name, `-latest` |
| Package (Python) | A directory Python treats as one importable thing, marked by an `__init__.py` inside it. The directory's name becomes the name you import, which is what stops a helper being found by accident because it happened to be nearby. | P01 day 1 part 1.2 | an import package |
| Fingerprint | A short, one-way tag derived from a secret — here twelve hex characters of its SHA-256 — safe to write in a log and able to answer exactly one question: is this the same key as before? | P01 day 1 part 2.1 | a key tag, a digest prefix |
| Transient failure | A failure worth trying again — the other side was busy, a connection dropped, a rate limit was hit — as against a permanent one, which will fail identically forever. Telling them apart is the caller's job, not the retry loop's. | P01 day 1 part 2.3 | a retryable error |
| Exponential backoff | Doubling the wait between attempts, so that a service under load is not hit by every client at the same cadence. The fallback schedule, used only when the other side did not say how long to wait. | P01 day 1 part 2.3 | the doubling schedule |
| `Retry-After` | The interval a provider states it wants before the next attempt. Not advice: when it is present it beats any local arithmetic, because the service knows something about its own recovery that a doubling schedule does not. | P01 day 1 part 2.3 | the retry interval |
| Model registry | The one file naming every model a project may use, as exact IDs, with a function that refuses anything else — so the pin is enforced by code rather than promised by a comment. | P01 day 1 part 3.1 | the allowed models |
| Gate | A check whose exit status decides whether work proceeds. The same command guards a commit today and a deployment later; only the reader of the exit status changes. | P01 day 1 part 3.2 | the check, CI |
```

**`docs/PINS.md`** — no row is owed. `ruff` and `pytest` are pins belonging to *this project* and
go in its own `PACKAGES.md`, dated, as the build brief says.

**`docs/SOURCES.md`** — no row is owed. Nothing with a citation identifier was cited; the three
pages read are in §9 with their dates.

**Commit:**

```text
P01 day 1: The skeleton and the kit
```
