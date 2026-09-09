---
name: day-prayoga
description: Write day N of the Prayoga curriculum — the hub, the parts/ sub-documents, the lab scaffold and the checklist — against the depth contract in docs/00_MASTER_PLAN.md §5 and §4.1. Use when asked to write, generate, draft or continue a day of this curriculum, or when the user types a bare day number.
argument-hint: "[day-number]"
---

# Write day $1 of Prayoga

> **Read `docs/00_MASTER_PLAN.md` §5 in full before writing a single line**, and §5.1 with it —
> the five constraints that make "real code" mean something. This file is the *procedure*; §5 is
> the *standard*, and the standard wins wherever the two seem to disagree.

## The three rules that outrank everything (plan §0)

1. **Completeness.** Code is never referenced, only printed — in full, at its real path, inside
   this project's own day documents. No `...`, no "the rest is unchanged" unless this same project
   printed it earlier and the day says which day did.
2. **Depth once.** A concept is taught deeply in exactly one place in the whole plan. Everywhere
   else it is printed in full and explained at **recap depth**: a table, one row per line that
   carries a decision, each naming the failure it prevents.
3. **The primer.** A pointer to another project is useless to someone who only has this one. Every
   pointer is a pair — the in-project `PRIMER.md` section, then the out-of-project deep document.
   **A pointer may never stand alone.**

---

## Step 1 — gather

1. Run `python p.py brief $1`. **If it exits non-zero, stop and report why.** Skipping, merging,
   inserting or reordering a day needs an ADR, written first.
2. Read the plan: **§0** (the three rules), **§3 and §3.1** (what a day is; days 1 and 2 of every
   project from P04), **§4.1** (the hub), **§5 and §5.1** (the part contract and real code),
   **§5.2** (the two depths), **§6** (pointers), **§9** (model and budget policy), **§11 and §12**
   (this project's shape and its day map), **§17** (the IDs day $1 closes).
3. Read `docs/GLOSSARY.md`. A term already there is **linked, not redefined**.
4. Read the previous day's `LESSON.md` and `CHECKLIST.md`. Unticked boxes: say so and ask before
   proceeding. Build on what earlier days printed; never reprint it without saying which day did.
5. Read this project's `CODEMAP.md` if it exists. **A file printed twice in one project is a bug**
   unless the second is a marked diff against the first.

## Step 2 — verify reality before you write (Principle 6)

6. **Never invent an interface.** For every symbol, flag, endpoint or field the day uses, fetch the
   live official page and note the URL and the date. The hub §9 tabulates them. If the live
   documentation disagrees with the plan, **stop and propose an amendment** — do not adapt quietly.
7. **Never invent a version or a limit.** Read it live before pinning. Record it in this project's
   `PACKAGES.md`, and anything the authoring repository itself depends on in `docs/PINS.md`.
8. **Never invent a citation.** Open the record live, copy the title from the record. Cite by
   **title and identifier, never by author**, and add a dated row to `docs/SOURCES.md`.
9. **Never invent a transcript.** If you have not run the command, the output block is
   `TODO(me): run <exact command>`. A missing output is fixed by one run; a fabricated one is
   undetectable, and Principle 7 outranks the document's shape.

## Step 3 — plan the split, before writing any prose

10. List the day's subtopics. Group them into **sections that share one mental model** — one stage
    of a pipeline, one phase of a mechanism, one curriculum ID. State the grouping in the hub §2;
    an unexplained numbering is a bug.
11. Split by **idea boundary, never by length or pace**. There is no target part count. Three
    tests, applied *before* writing: **one idea** (if it needs "also" to introduce its second half,
    it is two parts) · **standalone** (readable cold; name and link its prerequisite) · **no
    shortcut** ("for now, just accept that" is banned unless it links forward to the part that
    explains it).
12. **Every day gets at least one part whose subject is a deliberate failure** — break it, read the
    real error, fix it. It declares `failure: true` and is usually `level: production`.
    `python p.py depth` fails a day without one.
13. Assign each part a `level`: `foundation`, `working`, `production`. **A day climbs.** All
    `foundation` is a tutorial; opening at `production` skipped the reader.
14. **Choose one metaphor family for the whole day.** Grep the day's other parts and the hub §1
    before choosing. Two parts reaching for the same family read as one idea repeated.
15. **Print the planned part list before writing.** If it looks thin, the user will say so, and
    that conversation is cheap now and expensive after twenty documents exist.

## Step 4 — write the parts

Path: `days/<NN-project-slug>/day-NN-<day-slug>/parts/<NN>-<section-slug>/<section>.<subtopic>-<slug>.md`

16. **Name the day folder `day-NN-<slug>`** — number zero-padded, then 1–4 kebab-case words from
    the hub `title` with articles dropped. A bare `day-NN/` is rejected. The project folder
    is the phase's, from the plan §16 — `python p.py new N` puts the day in the right one, so
    scaffold with it rather than by hand.
17. **One folder per section**: two digits, then 1–3 kebab-case words. Every part lives inside its
    section folder, never loose in `parts/`, and the folder number must match the number before
    the dot. Sections run 1..N with no gaps, and so do subtopics inside each.
18. **Links are relative to the part's own folder**: a sibling is `1.2-<slug>.md`, another section
    is `../01-<slug>/1.5-<slug>.md`, the hub is `../../LESSON.md`. `prev` and `next` use the same
    form.
19. Every part carries the **seven headings of §5, in order**, plus frontmatter: One-line answer ·
    The idea · The mechanism · [Line by line] · When it breaks · In production · Check yourself.
    Start from `days/_TEMPLATES/PART.md`.
20. **`The idea` is story and plain language merged.** Open with a concrete scene you could have
    stood in — a courier, a job card, a spare key with a neighbour. **No jargon in the first
    paragraph.** Then the concept, terms defined on first use. The scene must still be holding the
    failure the part teaches when you reach the end. **No code in this section.**
21. **`The mechanism` is real code from this project**, headed with its actual path, whole file or
    a marked diff, no import from outside this project, runnable as printed, real output.
22. **Every code block is followed by `**Line by line:**`** — full depth if the code is taught
    here first, recap depth if borrowed. Recap depth is a table whose every row names **the failure
    that line prevents**, then the primer section and the deep pointer.
23. **`When it breaks` carries the real error text, verbatim**, then two to four sentences of plain
    words: what someone saw, and the smallest fix. If you have not seen the error, cause it.
24. **`In production` is not optional.** Four beats: what a senior writes instead · what degrades
    at scale, **with a number** · the review comment · the interview question.
25. A diagram whenever the concept is spatial, sequential or a state machine.

## Step 5 — write the hub

26. `days/<NN-project-slug>/day-NN-<slug>/LESSON.md`, from `days/_TEMPLATES/LESSON.md`. **The hub never teaches** —
    no `**Line by line:**` anywhere in it. Ten numbered sections in order (§4.1), ending at §10
    with the verbatim ledger rows and the commit message.
27. `frontmatter.parts` must equal the number of documents actually in `parts/`; the checker
    compares them. `files_printed` lists every path this day prints whole — it feeds `CODEMAP.md`,
    and a file with no day is what makes the completeness rule mechanical.
28. §7 states the per-turn request count **across the whole cast**. A three-agent turn is at least
    three requests, and a writer-critic loop is unbounded until you bound it. `0` is an answer.

## Step 6 — write the checklist

29. From `days/_TEMPLATES/CHECKLIST.md`: one box per part (read it · run its check · answer its
    question out loud), the build-brief boxes, **at least one "break it, watch it go red, fix it"**,
    the ledger rows, and the commit box. No time estimates.

## Step 7 — verify

30. Run `python p.py depth $1`. **Fix every failure; never hand-wave past one.**
31. Run `python p.py index`, then `python p.py check`.
32. Finish by printing: the IDs closed, the part count, the day's check command, the request
    budget, and the live pages you actually fetched.

---

## Always

- **No clocks in a day document.** Not in frontmatter, not in prose, not in the checklist. The
  sitting budget lives in the plan header and §3. **Never trim an explanation because the day is
  getting long** — add a part.
- **Grammar and punctuation are part of the deliverable**, in every section. A sentence the reader
  has to parse twice has failed.
- **Do not solve the `TODO(me)` reps.** Teach; do not do the learner's work.
- **All data is synthetic**, every project, every fixture, every eval.
- **Never name a person, instructor, author, channel, academy, bootcamp or training company** — not
  in a lesson, a checklist, a docstring or a commit message. Tool and library names are required
  and unaffected.
- The failure modes this format exists to prevent: splitting without deepening · summary in place
  of explanation · **stopping at the toy example** · assuming the previous day · code without
  failure · **trimming to fit** · solved reps · a carried-over clock. If a part gained no scene, no
  real mechanism, no real failure text and no production section, it is not done.
