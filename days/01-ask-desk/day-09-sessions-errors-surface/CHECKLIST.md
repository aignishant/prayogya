# Day 9 — definition of done

`python p.py done 9` refuses to commit while any box below is unticked. That refusal is the point:
a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-the-place-the-thread-lives/1.1-a-session-is-a-place-not-a-variable.md` — read · ran its check · answered its question out loud
- [ ] `parts/01-the-place-the-thread-lives/1.2-what-the-second-question-sees.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-when-it-goes-wrong/2.1-the-error-that-reached-the-caller.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-when-it-goes-wrong/2.2-the-except-that-ate-the-incident.md` — read · ran its check · answered its question out loud

## Build

- [ ] `run.py` — I typed the `session` subcommand, and I wrote down all four numbers it would print **before** running it
- [ ] `run.py session` — run, and the first block printed `4` then `8`, the second `4` then `4`
- [ ] `run.py session`, altered — I changed the first experiment's ids to `["s-1", "s-3"]`, predicted both numbers, ran it, and put the line back
- [ ] The stored-events probe — run, and I can name which of the four events per question `run_async` never yielded, and why the runner stored it before doing any work
- [ ] The invocation ids — I can say what an invocation is, and why two ids appeared across eight events rather than one or eight
- [ ] The three-outcomes probe — run, and I extended it so `s-2` **is** created before the run; I predicted what would change and I was right, or I know why not
- [ ] `ask_desk/agent.py` — I typed `export_key()`, and before running it I said which of `os.environ` and `.env` the guard lets win
- [ ] I can say what breaks in a container if that guard's test is reversed
- [ ] The failing-run probe — run, and I read `error_code`, `error_message` and `final` off the third event before reading my own notes
- [ ] The same probe with its `try`/`except` deleted — I predicted the last two lines of output before running it
- [ ] The swallowing probe — run, and I can name the single line that threw away what the run already knew
- [ ] **A check of my own** — I wrote a one-case check that drives `scripted.FAILS_AFTER_A_TOOL` and exits non-zero unless the run raises
- [ ] I can recite the two channels one failed run reports through, and say which one carries the invocation id

## Check

- [ ] The day's check is green: `cd projects/01-ask-desk && uv run --frozen python run.py check` — six green, `0 problem(s)`
- [ ] `echo $?` after it prints `0`, and I ran it rather than assuming it
- [ ] **Break it on purpose, watch it go red, fix it.** This is the day's deliberate failure. Wrap the event loop in `try/except Exception: return answer` and drive `scripted.FAILS_AFTER_A_TOOL` through it. Watch it return `''` with nothing raised. Run **my own check** against it and watch it go **red**, with `echo $?` non-zero. Remove the `except`, run both again, and watch the check go green
- [ ] **Break it on purpose, watch nothing go red.** With that same swallow still in place, run `uv run --frozen python run.py check` and `echo $?`. Six green at exit `0`, on a desk that answers every failed run with an empty string. I can say why each of the six checks is blind to it
- [ ] **Break the address, watch it go quiet.** Change `run.py session`'s first experiment to `["s-1", "s-3"]`. The second line reports `4 event(s)` instead of `8`, and **nothing errors**. Restore it
- [ ] **Break the refusal, watch it go loud.** Delete the `if await sessions.get_session(...) is None:` guard so `create_session` runs before every question. Watch the second question raise `AlreadyExistsError: Session with id s-1 already exists.` Restore the guard
- [ ] I can say why the previous two boxes are opposite kinds of failure, and which of the two I would rather ship
- [ ] `python p.py depth 9` — green
- [ ] `python p.py check` — green across the whole repository

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — session service, invocation, error event — and I checked that **Session** was already there from day 6 part 2.1 and linked it rather than redefining it
- [ ] `docs/PINS.md` — nothing to add today, and I can say why re-observing google-adk 2.8.0, uv 0.12.3 and CPython 3.12.12 does not earn a row
- [ ] `docs/SOURCES.md` — nothing to add today, and I can say why two documentation pages and an API reference do not qualify
- [ ] `projects/01-ask-desk/CODEMAP.md` — the three rows from the hub §10 are appended, so that every file printed twice says which day printed which half
- [ ] No RPM, TPM or RPD number appears anywhere in today's documents, and the ceiling is still a `TODO(me)` pointing at Google AI Studio
- [ ] No answer from a real model appears anywhere in today's documents
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10
- [ ] Committed with the message from the hub §10
