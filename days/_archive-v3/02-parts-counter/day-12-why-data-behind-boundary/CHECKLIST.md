# Day 12 — definition of done

`python p.py done 12` refuses to commit while any box below is unticked. That refusal is the point:
a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [x] `parts/01-the-shape-with-no-boundary/1.1-the-store-that-reaches-the-disk.md` — read · ran its check · answered its question out loud
- [x] `parts/01-the-shape-with-no-boundary/1.2-four-tools-and-the-one-that-writes.md` — read · ran its check · answered its question out loud
- [x] `parts/02-what-it-costs/2.1-two-writers-and-a-half-written-file.md` — read · ran its check · answered its question out loud
- [x] `parts/02-what-it-costs/2.2-the-five-things-a-boundary-buys.md` — read · ran its check · answered its question out loud

## Build

- [x] `parts_counter/store.py` — I can name the two lines of `adjust` the window sits between, and say what would have to be true for the sequence between them to be safe
- [x] `parts_counter/store.py` — I caused the relative-path `FileNotFoundError` from one directory up **without editing the file**, and can say why `Path(__file__).with_name(...)` does not have it
- [x] `parts_counter/tools.py` — for each of the four tools I wrote down what its worst failure costs and whether the next question can undo it
- [x] `parts_counter/tools.py` — I called `adjust_stock` with a string delta, read the traceback, and can say which line raised it, which line should have caught it, and why the inventory was untouched
- [x] I can say why the two `stock.adjusted` records and the two results arrived out of order, without re-reading part 1.2
- [x] I predicted `parts unaccounted` before the first `race`, and recorded all three numbers from three runs
- [x] I wrote the five things a boundary buys in my own words, each paired with the transcript that made me want it, and the four costs beside them

## Check

- [x] The day's check is green: `cd projects/02-parts-counter && uv run --frozen python run.py check` — six green, `0 problem(s)`
- [x] `echo $?` after it prints `0`, and I ran it rather than assuming it
- [x] **Break it on purpose, watch parts vanish, watch it restore itself.** `uv run --frozen python run.py race`, three times. Parts go missing on every run, the number is different, and `restored to` says `240` every time. Then `git status --porcelain` is empty.
- [x] I saw `reads that crashed` come back non-empty on at least one run, and can say what `Expecting value: line 1 column 1 (char 0)` means about the state of the file at that instant
- [x] **Break it on purpose, watch which failure moves.** Add `time.sleep(0.002)` in `store.adjust` immediately after `payload = _read()`, run `race` twice, and say what changed and what did not. **Remove it and confirm `git status --porcelain` is empty.**
- [x] **Break it on purpose, watch it go red, fix it.** Set the answering model in `parts_counter/util/models.py` to `gemini-flash-latest` and run `run.py check`; the `model` check refuses an alias by name. Put the pin back and watch it go green.
- [x] **Break the document on purpose.** Delete a `## In production` heading from any part, run `python p.py depth 12`, watch it name the file and the section, and restore it.
- [x] `python p.py depth 12` — green
- [x] `python p.py check` — green across the whole repository
- [x] `git status --porcelain projects/` is empty — this day changed no project file, and that is a property worth checking rather than assuming

## Record

- [x] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — read-modify-write, audit trail, lost update, torn read, data boundary, blast radius
- [x] `docs/PINS.md` — nothing to add today, and I can say why: this day installs nothing and moves no version
- [x] `docs/SOURCES.md` — nothing to add today, and I can say why the MCP specification revision is deliberately absent and where the `TODO(me)` for it lives
- [x] The `docs/PROGRESS.md` row is pasted from the hub §10
- [x] Committed with the message from the hub §10
