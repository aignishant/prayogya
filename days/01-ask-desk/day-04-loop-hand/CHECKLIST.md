# Day 4 — definition of done

`python p.py done 4` refuses to commit while any box below is unticked. That refusal is the point:
a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-what-a-turn-is-made-of/1.1-the-name-you-say-every-time.md` — read · ran its check · answered its question out loud
- [ ] `parts/01-what-a-turn-is-made-of/1.2-the-key-in-this-projects-own-hands.md` — read · ran its check · answered its question out loud
- [ ] `parts/01-what-a-turn-is-made-of/1.3-one-letter-one-reply.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-the-thread-you-carry/2.1-the-list-that-is-the-memory.md` — read · ran its check · answered its question out loud
- [ ] `parts/02-the-thread-you-carry/2.2-the-reply-you-never-filed.md` — read · ran its check · answered its question out loud

## Build

- [ ] The scaffold from hub §3 exists: `pyproject.toml` with `dependencies = []`, `.python-version`, `.gitignore`, `.env.example`, and the four project documents
- [ ] I can say why day 4 adds no dependency at all, and which day adds `google-adk` and why that one
- [ ] `ask_desk/util/models.py` — typed, and I predicted which refusal message each of `gemini-flash-latest` and `gemini-3.7-flash` would get **before** running it
- [ ] I can say why the alias branch comes first and is separate, without re-reading part 1.1
- [ ] `ask_desk/util/keys.py` — typed, as this project's own copy at `ask_desk/util/`, and I can say what a reader with only this folder would see if it imported from above
- [ ] `ask_desk/provider.py` — typed as far as `text_of`, and I wrote down the body's top-level keys **before** running `plan`
- [ ] I can say why `build_request` and `send` are two functions, and which of them a test can run
- [ ] `ask_desk/loop.py` — typed, and I predicted how many items `contents` holds when the third question is sent, then proved it with `next_request` and no network
- [ ] I can say why `contents` and `turns` are two lists, and why the `Turn` is recorded before the reply is filed
- [ ] `run.py` — typed, and I predicted which of the five checks would be red **before** the first run
- [ ] I ran the honest-gap rep, or I wrote down that I could not because there is no working key on this machine

## Check

- [ ] The day's check is green: `cd projects/01-ask-desk && uv run --frozen python run.py check` — five green, `0 problem(s)`
- [ ] `echo $?` after it prints `0`, and I ran it rather than assuming it
- [ ] `uv lock --check` exits `0`
- [ ] `uv run --frozen python run.py plan "Is the VPN down?"` prints a URL ending in `gemini-3.8-flash:generateContent`, a body with two top-level keys, and no credential anywhere
- [ ] **Break it on purpose, watch it go red, fix it.** Set `models.ANSWERING` to `"gemini-flash-latest"`; watch `model` go red with the *alias, not a pin* message. Set it to `"gemini-3.7-flash"`; watch it go red with the *not in this project's registry* message. Restore it.
- [ ] **Break it on purpose, watch it go red, fix it.** Empty the value in `.env`; watch `keys` go red with *present with an empty value* rather than *not set*. Restore it.
- [ ] **Break it on purpose, watch it go red, fix it.** Edit `pyproject.toml` so `dependencies` reads `["platformdirs>=4.11.8"]`; watch `pins` **and** `lock` both go red, and say why each one did. Restore `dependencies = []`.
- [ ] **Break it on purpose and watch nothing go red.** Run part 2.2's comparison command; confirm `3 contents, roles ['user', 'model', 'user']` against `2 contents, roles ['user', 'user']`, then run `run.py check` again and confirm it is still five green. I can say what check would have caught it.
- [ ] `python p.py depth 4` — green
- [ ] `python p.py check` — green across the whole repository

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — stateless, turn, candidate, model alias, conversation, system instruction
- [ ] `projects/01-ask-desk/PACKAGES.md` exists and carries the four rows from the hub §10
- [ ] `docs/PINS.md` — nothing added today, and I can say which rule decides that
- [ ] `docs/SOURCES.md` — nothing added today, and I can say why the pages this day cites do not qualify
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10
- [ ] Committed with the message from the hub §10
