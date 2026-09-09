# Primer — P01 Ask Desk

Three ideas this project uses and does not teach. Each section is self-contained: you can build and
understand this project having read only this page, and the pointer at the end of each is for depth
rather than for sufficiency.

## §1 Reading a key, and the three ways one can be wrong

Nothing loads a `.env` file for you — not Python, not `uv run`, not the shell. A running program
has an *environment*: name-to-string pairs the operating system gave it at startup, which Python
exposes as `os.environ`. A `.env` file is inert until some code opens it, and in this project that
code is `ask_desk/util/keys.py`.

Two places can hold the same name, so precedence has to be decided once: **the process environment
wins, the file is the fallback.** That is the right way round because every deployment target
injects secrets as environment variables and none of them write a `.env` for you; letting the file
win would make your laptop behave unlike everywhere the code actually runs.

A key can be wrong three ways, and only two are decidable here. **Absent** — nobody set it; Python
gives `None`. **Present and empty** — somebody tried and failed; Python gives `''`, and this is the
more dangerous case because it is usually a CI secret that was never populated. Those two need
different sentences said back, which is why `require` tests `is None` and `not value.strip()`
separately rather than writing `if not os.environ.get(...)` — that one condition is true for both
and its error message has to lie to one of them. The third way is **present, non-empty and not
accepted by the provider**, and nothing running on your machine can decide it: a credential is
valid because a server holding the other half says so. Only a request settles it.

Deeper: `days/00-foundry/day-03-keys-pinning-refusing-check/parts/01-the-key/1.2-three-states-and-the-one-you-cannot-check.md`

## §2 A floor is not a pin

`platformdirs>=4.11.8` and `requires-python = ">=3.12"` do not name a version. They say what is
*too old* and hand the choice to whichever machine resolves them, on whichever day. That is correct
for a library — a library that pinned exactly would be uninstallable beside anything else — and it
is never sufficient for an application, which is deployed rather than imported.

Three files answer three different questions, and only the last two make two machines agree.
`pyproject.toml` records what you **asked for**, and is allowed to be a range. `uv.lock` records
what the asking **produced** — exact versions and hashes, for packages you never named. And
`.python-version` records **which interpreter**, because `requires-python` is a floor like any
other. The test of whether you have pinned anything is not whether a version number appears
somewhere; it is whether handing this folder to somebody next March gets them what you have.

The same idea reaches models. `gemini-flash-latest` is documented as hot-swapped on every release,
so it is a floor wearing a version's clothes. `ask_desk/util/models.py` refuses it by name.

Deeper: `days/00-foundry/day-03-keys-pinning-refusing-check/parts/02-the-pin-and-the-refusal/2.1-a-floor-is-not-a-pin.md`

## §3 The exit status is the verdict

A check has two audiences and only one of them can be fooled. A person reads the terminal; every
other consumer — a commit hook, a pipeline step, a `done` command — reads exactly one number, the
process's **exit status**. Zero means success. Everything printed is decoration.

So a check that prints `RED`, counts the problems, and then exits `0` is green everywhere it
matters, and it looks *more* convincing than a working one because all the human-readable parts are
correct. The line that makes the difference is `sys.exit(main(sys.argv))`: `main` returns the
verdict as an integer, and without that wrapper Python discards it and exits 0.

There is a second way to build a check that cannot refuse, and it needs no bug. If you invoke a
check through a tool that **repairs** what is being checked, the repair happens first. `uv run`
updates the lockfile before running your command, so a lockfile-drift check invoked that way always
passes — accurately, about a state its own invocation created. `uv run --frozen` is the fix, which
is why every command in this project's documents carries it.

Deeper: `days/00-foundry/day-03-keys-pinning-refusing-check/parts/02-the-pin-and-the-refusal/2.2-the-check-that-could-not-refuse.md`
