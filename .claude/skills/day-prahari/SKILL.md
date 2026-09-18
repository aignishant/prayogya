---
name: day-prahari
description: Write day N of the Prahari curriculum — the hub, the parts/ sub-documents, any source documents, the lab scaffold and the checklist — against the depth contract in docs/00_MASTER_PLAN.md §11. Use when asked to write, generate, draft or continue a day of this curriculum, or when the user types a bare day number.
argument-hint: "[day-number]"
---

# Write day $ARGUMENTS of Prahari

> **Read `docs/00_MASTER_PLAN.md` §11 in full before writing a single line.** It is the depth
> contract this skill implements. This file is the *procedure*; §11 is the *standard*, and the
> standard wins wherever the two seem to disagree.

## The three commitments (§11.1 — everything below follows from these)

1. **One idea per document.** If it needs "also" to introduce its second half, it is two documents.
2. **No clocks.** Never a time estimate, a duration, an "estimated hours" field or a pace — not in
   frontmatter, not in prose, not in the checklist. **Never trim an explanation because the day is
   getting long; split it into another part instead.**
3. **Zero to production, in one document.** Open where a reader who has never heard of the idea
   can stand. End where a professional stands.

---

## Step 1 — gather

1. Run `python granth.py brief $ARGUMENTS`. **If it exits non-zero, stop and report why.** It carries the
   assignment, the phase gate, the IDs that should already be closed, the sources already taught,
   and the order guard. Do not argue with the guard: skipping, merging or reordering a day needs
   an ADR, written first.
2. Read the plan: **§2** (the principles — including 13, every model call is a request against a
   quota, and 14, nothing acts without a trail), **§4** (the constraints every command must
   respect: free-tier providers, a CPU, SQLite, `uv`), **§5** (the baseline and how it is
   verified), **§8** (the day map — the authoritative ID list for day $ARGUMENTS), **§11** (the
   depth contract), **§12** (the style guide).
3. Read `docs/GLOSSARY.md`. Any term already defined there is **linked, not redefined**. Two
   nearly-identical definitions are worse than one bad one.
4. Read the previous day's `LESSON.md` and `CHECKLIST.md`. If the checklist has unticked boxes,
   say so and ask before proceeding. Build on what earlier days told the learner to make; never
   duplicate it and never rewrite it.
5. Read `docs/wiki/ENTITIES.md` before deciding this day teaches a source. **A source is taught
   once in the whole curriculum.** If it is already there, cite and link it instead.

## Step 2 — verify reality before you write (Principle 6)

6. **Never invent an interface.** For every symbol, flag, endpoint or field the day will use,
   fetch the live official page and note the URL and the date. The part that uses it names the
   page checked, and the hub's §8 tabulates them. If the live documentation disagrees with the
   plan, **stop and propose an amendment** — do not silently adapt.
7. **Never invent a version or a limit.** Read it live before pinning it, and record what, the
   value, the date, the day and why in `docs/PINS.md`. A failed lookup leaves `TODO(<the exact
   command>)` — never a guess. On this project a **rate limit is a version**: a day that spends
   requests re-reads the provider's limits page and says so.
8. **Never invent a citation.** For every source the day will teach or cite, **open the record
   live** and copy the title from it rather than from memory. Record identifier, exact title,
   year, URL and the date checked in `docs/SOURCES.md`. This is the rule that bites hardest: a
   wrong version pin fails loudly on the next install, while a plausible identifier attached to
   the wrong title fails **silently, for years**. Cite by **title and identifier, never by author**.

## Step 3 — plan the split (before writing any prose)

9. List the day's subtopics. Group them into **sections that share one mental model** — usually
   one curriculum ID, one stage of a pipeline, or one phase of a mechanism. State the grouping;
   an unexplained numbering is a bug.
10. Split by **idea boundary, never by length or pace** (§11.7). There is no target part count:
    four if the subject needs four, twenty-two if it needs twenty-two.
11. **Ask what the day's ideas came from.** Is there a public, citable origin document — a
    research paper, a numbered specification revision, a standard, a formal report? If so the day
    gets **one document per source in `sources/`**, beside `parts/` and not inside it, and every
    part leaning on that idea carries *The source behind it*. A subtopic about a tool, a command
    or a repository convention has no source; **do not manufacture one**. Phase 2 and the MCP
    days are where sources are expected; a runtime or ops day usually has none.
12. **Every day gets at least one part whose subject is a deliberate failure** — break it on
    purpose, read the real error, fix it. That part declares `failure: true` in its frontmatter
    and is usually `level: production`. `python granth.py depth` fails the day without one.
13. Assign each part a `level` — `foundation`, `working`, `production`. A day climbs. A day that
    is all `foundation` is a tutorial; a day opening at `production` has skipped the reader.
14. Apply the **one-idea test**, the **standalone test** and the **no-shortcut test** to every
    planned part *before* writing it.
15. **Choose one metaphor family for the whole day.** Two parts reaching for the same family read
    as one idea repeated; two parts reaching for unrelated exotic families read as noise.
16. **Print the planned part list before writing.** If it looks thin, the user will say so, and
    that conversation is cheap now and expensive after twenty documents exist.

## Step 4 — write the parts

Path: `days/day-NN-<day-slug>/parts/<NN>-<section-slug>/<section>.<subtopic>-<slug>.md`

17. **Name the day folder `day-NN-<slug>`** — the number zero-padded, then a kebab-case slug of
    1–4 words from the hub's `title` with articles dropped. A number alone is an address, not an
    answer. A bare `days/day-NN/` is rejected by `python granth.py depth`.
18. **One folder per section**: two digits, then a kebab-case slug of 1–3 words saying what the
    section is about, taken from its heading in the hub's map. Every part lives inside its
    section's folder; none is ever loose in `parts/`, and the folder number must match the number
    before the dot.
19. **Links are relative to the part's own folder**: a sibling is `1.2-<slug>.md`, another section
    is `../01-<slug>/1.5-<slug>.md`, the hub is `../../LESSON.md`. `prev` and `next` use the same
    form. The hub's map links from the day folder: `parts/01-<slug>/1.1-<slug>.md`.
20. Every part carries **all eleven sections of §11.4, in order**. Three are conditional — *The
    source behind it*, *Line by line*, *The source in one demo* — each required exactly when its
    trigger is present and never otherwise. Start from `days/_TEMPLATES/PART.md`.
21. **The story is the section that gets written badly.** Four rules, and the first is the one
    that gets broken:
    1. **A scene the reader has plausibly lived.** A parcel and a courier, a repair-shop job card,
       a bus route map, a used car checked by a mechanic, a monthly generator test. **Not** a
       nautical chart, a model railway, a theatre programme, a projection booth. Test: *could the
       reader have been standing in this scene themselves?* If they must first be told what the
       setting **is**, the analogy is carrying the explanation instead of hooking it.
    2. **Simple words.** If a twelve-year-old could not follow the first sentence, rewrite it.
    3. **Load-bearing.** The scene contains the actual failure or decision the part teaches, and
       every later section that reaches back for it must still fit.
    4. **No metaphor collision inside a day.** Grep the day's other parts before choosing.
22. **`In production` is not optional and is not a paragraph of encouragement.** What a
    professional writes instead of the teaching version · what degrades at scale or under pressure
    · the failure that only shows with real traffic · the review comment · the interview question.
23. **`When it breaks` carries the real error text, verbatim.** If you have not seen the error,
    cause it. A reconstructed traceback is a fabricated result (Principle 7).
24. **Every code block is followed by `**Line by line:**`** — every non-obvious token, and why
    that line and not another.
25. A diagram whenever the concept is spatial, sequential or a state machine.
26. **Every command respects the constraints.** No GPU. No paid provider. A live model request in
    a test where a cassette could exist is a defect. The request count goes in the hub's §6.

## Step 5 — write the sources last, and say they are read last

27. Path: `days/day-NN-<slug>/sources/NN-<source-slug>.md`, numbered from `01` with no gaps.
    Start from `days/_TEMPLATES/SOURCE.md`. Frontmatter is a part's **minus `part`** and **plus
    `source:`** (one identifier). Links run one level up: a part is
    `../parts/01-<slug>/1.1-<slug>.md`, the hub is `../LESSON.md`.
28. They are *read* after the parts too — the hub's map says so and the last part's *Next* points
    at them. That order is Principle 3 at the scale of a day: build the mechanism by hand, then
    read the proposal, so "what survived and what did not" lands on something the reader built.
29. **The demo is the section that makes a source document worth reading.** Only that source's
    contribution · end to end and actually runnable, with **real pasted output** (a `TODO` naming
    the exact command if it has not been run — **never an invented transcript**) · **an ablation
    switch** with both runs shown · inside the project's constraints.

## Step 6 — write the hub

30. `days/day-NN-<slug>/LESSON.md`, from `days/_TEMPLATES/LESSON.md`. **The hub never teaches** —
    no `**Line by line:**` anywhere in it. Eleven numbered sections in order (§11.5), ending at
    §11 Ledger & commit with the verbatim rows to paste and the commit message.
31. `frontmatter.parts` must equal the number of documents actually in `parts/`. The checker
    compares them.
32. §6 Budget is a **count of model requests per provider**, and `0` is the usual answer once
    cassettes exist. State it.

## Step 7 — write the checklist

33. `days/day-NN-<slug>/CHECKLIST.md`, from `days/_TEMPLATES/CHECKLIST.md`: one box per part
    document (read it · run its check · answer its question out loud), one per source document,
    the build-brief boxes, **at least one "break it, watch it go red, fix it"**, the ledger rows,
    the budget box, and the commit box. No time estimates.

## Step 8 — verify

34. Run `python granth.py depth $ARGUMENTS`. **Fix every failure; never hand-wave past one.**
35. Run `python granth.py index`, then `python granth.py check`.
36. Finish by printing: the IDs closed, the part count, the day's check command, the budget, and
    the live pages you actually fetched.

---

## Always

- Honour `CLAUDE.md`: doc-first · build-first-compare-after · never invent a fact · at least one
  check that can go red · every command inside the plan's §4 constraints.
- **Grammar and punctuation are part of the deliverable, in every section — not just the story.**
  Full stops and commas where they belong, no run-on sentences, and no long chain of dashes where
  two ordinary sentences would read better. A sentence the reader has to parse twice has failed.
- **Do not solve the `TODO(me)` sections, and do not do the learner's work.** Teach; don't do the
  reps. The exception is a source document's demo, which is given complete because it is teaching
  material rather than an exercise.
- **Never name a person, instructor, author, channel, academy, bootcamp or training company** —
  not in a lesson, a checklist, a docstring or a commit message. Tool and library names are
  required and unaffected, as is citing a specification by its revision and a work by its exact
  title and identifier.
- The eight failure modes this format exists to prevent (§11.8): splitting without deepening ·
  summary in place of explanation · **stopping at the toy example** · assuming the previous day ·
  code without failure · **trimming to fit** · solved reps · a carried-over clock. If a part
  gained no story, no mechanism, no real failure text and no production section, it is not done.
