# Primer — P02 Parts Counter

Five ideas this project uses and does not teach. Each section is self-contained: you can build and
understand this project having read only this page. The pointer at the end of each is for depth, not
for sufficiency.

## §1 A floor is not a pin

`platformdirs>=4.11.8` and `requires-python = ">=3.12"` name no version. They say what is *too old*
and hand the choice to whichever machine resolves them, on whichever day. That is right for a
library, which must install beside other people's constraints, and never enough for an application,
which is deployed rather than imported.

Three files answer three questions. `pyproject.toml` records what you **asked for** and may be a
range. `uv.lock` records what the asking **produced** — exact versions and hashes, including
packages you never named. `.python-version` records **which interpreter**. The test of whether you
have pinned anything: hand this folder to somebody next March and ask whether they get what you
have.

The same idea reaches models. `gemini-flash-latest` is documented as hot-swapped on every release,
so it is a floor wearing a version's clothes. `parts_counter/util/models.py` refuses it by name.

Deeper: `days/00-foundry/day-03-keys-pinning-refusing-check/parts/02-the-pin-and-the-refusal/2.1-a-floor-is-not-a-pin.md`

## §2 The exit status is the verdict

A check has two audiences and only one can be fooled. A person reads the terminal; a commit hook, a
pipeline step and a `done` command read one number — the process's **exit status**. Zero means
success and everything printed is decoration. A check that prints `RED`, counts the problems and
exits `0` is green everywhere it matters, and it looks *more* convincing than a working one because
every human-readable part is correct. The line that makes the difference is
`sys.exit(main(sys.argv))`.

There is a second way to build a check that cannot refuse, and it needs no bug: invoke it through a
tool that **repairs** what is being checked. `uv run` updates the lockfile before running your
command, so a lockfile-drift check invoked that way always passes — accurately, about a state its
own invocation created. `uv run --frozen` is why every command in this project's documents carries
that flag.

Deeper: `days/00-foundry/day-03-keys-pinning-refusing-check/parts/02-the-pin-and-the-refusal/2.2-the-check-that-could-not-refuse.md`

## §3 Reading a key, and the three states of one

Nothing loads a `.env` file for you — not Python, not `uv run`, not the shell. A running program has
an *environment*: name-to-string pairs the operating system gave it at start-up, exposed as
`os.environ`. The file is inert until code opens it, and here that code is
`parts_counter/util/keys.py`. **The process environment wins and the file is the fallback**, because
every deployment target injects secrets as variables and none of them writes a `.env`.

A key can be wrong three ways and only two are decidable locally. **Absent** — Python gives `None`.
**Present and empty** — usually a CI secret that was never populated; Python gives `''`. Those need
different sentences said back, which is why `require` tests `is None` and `not value.strip()`
separately: `if not os.environ.get(...)` is true for both and its message has to lie to one of them.
The third — **present, non-empty and not accepted** — no local check can settle, because a
credential is valid only because a server holding the other half says so.

One more thing this project needs and P00 did not: the framework does not use your key reader.
`google-genai` builds its client from `os.environ` directly, so a project that reads its own file
and never exports the value gets `ValueError: No API key was provided.` while the key sits on disk.

Deeper: `days/00-foundry/day-03-keys-pinning-refusing-check/parts/01-the-key/1.2-three-states-and-the-one-you-cannot-check.md`

## §4 A tool declaration is derived, not written

The model never sees your code. It sees a JSON declaration — a name, a description, and a JSON
Schema for the arguments — and that declaration is the entire interface. ADK builds it from the
function object: the **name** from `__name__`, the **schema** from the type hints and defaults, and
the **description** from the docstring.

Three consequences worth carrying into this project. A parameter with no type hint produces a schema
property with no `type`, which constrains nothing. A function with no docstring gets the description
`'Call self as a function.'` — `__call__.__doc__`, leaking — and nothing warns. And a per-parameter
`description`, which a hand-written declaration can carry, has nowhere to live in a derived one, so
guidance about an argument belongs in the docstring where the derivation will read it.

That is why the docstrings in `parts_counter/tools.py` are written for the model rather than for us.

Deeper: `days/01-ask-desk/day-07-functiontool-what-adk-does/parts/01-what-the-wrapper-reads/1.2-the-type-hints-are-the-schema.md`

## §5 The framework's bound is not your bound

ADK does bound the loop: `RunConfig.max_llm_calls`, **defaulted to 500**, overridable outside the
repository by the `ADK_MAX_LLM_CALLS` environment variable, and enforced by raising
`LlmCallsLimitExceededError`. A value of zero or less disables it, which reads like the opposite of
what it does.

500 is a runaway ceiling — sized so no legitimate run trips it. That is a different job from
answering "what may one question cost?", and this project answers the second question itself, in
`parts_counter/util/budget.py`, with a number it chose. Both are set from the same constants, so
there is one place to change and no chance of the two disagreeing.

Deeper: `days/01-ask-desk/day-07-functiontool-what-adk-does/parts/02-what-it-reads-that-you-did-not-mean-to-write/2.2-what-it-did-and-what-it-did-not.md`
