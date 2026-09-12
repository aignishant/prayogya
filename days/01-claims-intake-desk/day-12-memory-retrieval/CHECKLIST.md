# P01 day 12 — definition of done

`python p.py done 01 12` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-the-corpus/1.1-handbook-on-the-counter.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/01-the-corpus/1.2-index-you-can-recompute.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/02-citations-and-score/2.1-citations-that-resolve.md` — read · ran its check · answered
      its question out loud
- [ ] `parts/02-citations-and-score/2.2-recall-at-k.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/03-session-versus-memory/3.1-what-the-desk-refuses-to-remember.md` — read · ran its
      check · answered its question out loud
- [ ] `parts/04-holding-it/4.1-what-the-tests-hold.md` — read · ran its check · answered its
      question out loud

## Build

- [ ] `data/handbook.md` — eight rules, one identifier each, and read it before writing any code
- [ ] `claims_desk/recall.py` — `Chunk`, `words`, `chunks`, `Index`, `cited`, `resolves`
- [ ] `data/handbook_questions.json` — ten questions in a handler's words, each with its `why`
- [ ] `claims_desk/recall.py` — `recall_at_k`, added **after** the evalset exists
- [ ] `tests/test_recall.py` — fifteen functions, eighteen tests
- [ ] `claims_desk/recall.py` — `TODO(me)`: the stemmer, with all ten questions measured before and
      after
- [ ] `claims_desk/recall.py` — `TODO(me)`: a second measurement that tells a wrong answer from no
      answer
- [ ] `data/handbook.md` — `TODO(me)`: a ninth rule about police references, and what it did to the
      idf of `theft`
- [ ] `claims_desk/recall.py` — `TODO(me)`: the index as a singleton, and what it costs a test
- [ ] Your own notes — `TODO(me)`: which two questions an embedding would fix, and how you would know

## Check

- [ ] The day's check is green: `./run check` — `All checks passed!`, `141 passed`, four `ok` lines
- [ ] Listed the chunks and confirmed eight, with sizes that vary because the document varies
- [ ] Asked the three questions and read the scores — including the one where the wrong answer wins
      at `0.406`
- [ ] Asked something the handbook has nothing to say about and got `found: 0`
- [ ] Measured `recall@1`, `recall@2` and `recall@3` and read every miss by name
- [ ] Printed the shared terms for the escalation question and confirmed **zero** with HB-08
- [ ] Ran the memory demonstration and confirmed the search took no claim reference
- [ ] **Break it on purpose, watch it go red, fix it.** Add `"about"` to `STOPWORDS`. Predict first,
      then run: exactly one test goes red, all three recall numbers stay exactly where they were, and
      the escalation question stops returning a wrong section and starts returning nothing. Say out
      loud why the score could not see the difference. Put it back.
- [ ] Deleted the ` · ` from one heading, saw seven chunks, and noticed which section grew
- [ ] Removed the zero filter and read three resolving citations on a question about xylophones
- [ ] `python p.py depth 01 12` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path — and no earlier file
      changed today
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own earlier days
- [ ] `data/handbook.md` is synthetic, names no real insurer, and contains no claim reference,
      policy number, telephone number or address
- [ ] No memory service is registered anywhere in this project

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the eight rows in
      the hub §10
- [ ] No `docs/PINS.md` row is owed — nothing was installed today
- [ ] No `docs/SOURCES.md` row is owed — the handbook is written for this project
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
