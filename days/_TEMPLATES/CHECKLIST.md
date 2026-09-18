# Day NN — definition of done

`python granth.py done NN` refuses to commit while any box below is unticked. That refusal is the point:
a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

<!-- One box per part document. Reading it is not enough — run its check and answer its question
     out loud, because "I followed that" and "I could explain that" are different states. -->

- [ ] `parts/01-<slug>/1.1-<slug>.md` — read · ran its check · answered its question out loud
- [ ] `parts/01-<slug>/1.2-<slug>.md` — read · ran its check · answered its question out loud

<!-- Sources come after the parts, deliberately. -->

- [ ] `sources/01-<slug>.md` — read · ran the demo · ran the ablation and saw the difference

## Build

<!-- One box per `TODO(me)` in the hub's §4. -->

- [ ] `<path>` — <the rep>

## Check

- [ ] The day's check is green: `<command>`
- [ ] **Break it on purpose, watch it go red, fix it.** <what to break>
- [ ] `python granth.py depth NN` — green
- [ ] `python granth.py check` — green across the whole repository

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md`
- [ ] Every version or limit observed today has a dated row in `docs/PINS.md`
- [ ] Every source cited today has a dated row in `docs/SOURCES.md`
- [ ] The request budget in the hub's §6 was not exceeded — and the count is written next to it
- [ ] The `docs/PROGRESS.md` row is pasted from the hub's §11
- [ ] Committed with the message from the hub's §11
