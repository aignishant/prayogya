# Day 0 — definition of done

`python p.py done 0` refuses to commit while any box below is unticked. That refusal is the point:
a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [x] `parts/01-the-workbench/1.1-one-tool-owns-the-environment.md` — read · ran its check · answered its question out loud
- [x] `parts/01-the-workbench/1.2-two-repositories-one-folder.md` — read · ran its check · answered its question out loud
- [x] `parts/02-the-driver/2.1-the-foreman-and-the-order-guard.md` — read · ran its check · answered its question out loud
- [x] `parts/02-the-driver/2.2-the-inspection-that-inspected-nothing.md` — read · ran its check · answered its question out loud

## Build

- [x] `.python-version` — pinned, read back, and I can say what happens if the interpreter it names is missing
- [x] `.gitignore` — `git check-ignore -v .env` names the rule and its line, and I can say why a rule added tomorrow would not protect a file committed today
- [x] `granth.toml` — set `require_failure_part = false`, ran `depth 0`, said what the repository lost, put it back
- [x] I can state the one-way rule between the root and `projects/` without looking it up

## Check

- [x] `python p.py doctor` — green, and it reports 297 days and 310 IDs each on exactly one day
- [x] `python p.py depth 0` — green
- [x] `python p.py index` then `python p.py index --check` — green
- [x] `python p.py check` — green across the whole repository
- [x] **Break it on purpose, watch it go red, fix it.** Delete a `## In production` heading from any part, run `depth 0`, see it named, restore it
- [x] **Second break.** Comment out `failure: true` in part 2.2, run `depth 0`, watch the day be refused for having no deliberate failure, restore it
- [x] `python p.py brief 5` — exits 1 and lists the open IDs from earlier days

## Record

- [x] Every term defined for the first time today has a row in `docs/GLOSSARY.md`
- [x] Every version observed today has a dated row in `docs/PINS.md`
- [x] `docs/SOURCES.md` — nothing to add; day 0 cites no external record, and I checked rather than assumed
- [x] The `docs/PROGRESS.md` row is pasted from the hub §10
- [x] Committed with the message from the hub §10
