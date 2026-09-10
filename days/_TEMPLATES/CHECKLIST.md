# PNN day DD — definition of done

`python p.py done NN D` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

<!-- One box per part document. Reading it is not enough — run its check and answer its question
     out loud, because "I followed that" and "I could explain that" are different states. -->

- [ ] `parts/01-<slug>/1.1-<slug>.md` — read · ran its check · answered its question out loud

## Build

<!-- One box per `TODO(me)` in the hub §5. -->

- [ ] `<path>` — <the rep>

## Check

- [ ] The day's check is green: `<command>`
- [ ] **Break it on purpose, watch it go red, fix it.** <what to break>
- [ ] `python p.py depth NN D` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

<!-- The four rules, checked on the day rather than at the end of the project, because a breach
     found on day 3 is an edit and a breach found on day 19 is a rewrite. -->

- [ ] Every file this day printed was printed **in full**, at its real path — no `...`, no
      "the rest is unchanged" without naming the day of THIS project that printed the original
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own earlier days

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md`
- [ ] Every version or limit observed today has a dated row in `docs/PINS.md`
- [ ] Every source cited today has a dated row in `docs/SOURCES.md`
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
