---
name: day-prayoga
description: Write one day of the Prayoga curriculum — the hub, the parts/ sub-documents, the lab scaffold and the checklist — against the contract in docs/00_MASTER_PLAN.md §5 and §4.1. Days are addressed as project and day, e.g. "01 7". Use when asked to write, generate, draft or continue a day of this curriculum, or when the user types a project and day number.
argument-hint: "[project-number] [day-number]"
---

# Write day $2 of project $1

> **Read `docs/00_MASTER_PLAN.md` §5 in full before writing a single line**, and §5.1 with it —
> the six constraints that make "real code" mean something. This file is the *procedure*; §5 is
> the *standard*, and the standard wins wherever the two seem to disagree.

## The five rules that outrank everything (plan §0)

1. **Completeness.** Code is never referenced, only printed — in full, at its real path, inside
   this project's own day documents. That includes `.gitignore`, `pyproject.toml`, `Dockerfile`
   and the `run` driver. No `...`, no "the rest is unchanged" unless this same project printed it
   earlier and the day says which day did.
2. **Repetition.** Every concept this day uses is taught **here, at full depth** — scene,
   mechanism, line-by-line, real failure, production note. **There is no recap depth**, no "taught
   deeply elsewhere", no pointer to another project. If you have written this concept before in
   another project, write it again, better, with this industry's consequences.
3. **From scratch.** Nothing is assumed that this project did not build. Day 0 starts on a bare
   machine.
4. **Full stack.** The project ships all eighteen spine slots (plan §12). This day is one of them,
   or an extra day deepening one.
5. **The document is the deliverable.** **Never create, edit or scaffold anything under
   `projects/`.** The learner types every file and runs every command from this document. So the
   document must carry: every file **in full at its real path**, every command **in the order it is
   run**, and **what each command actually printed**. If a reader following the day top to bottom
   would reach a point where they do not know what to type, the day is not finished.

**And: nothing leaves the project.** No path into another project, no project name, no "as we
saw", no `PRIMER.md`. `python p.py check` greps for all of it and fails the day.

---

## Step 1 — gather

1. Run `python p.py brief $1 $2`. **If it exits non-zero, stop and report why.** Skipping,
   merging, inserting or reordering a day inside a project needs an ADR, written first. Order
   *between* projects is free — starting a new project is always allowed.
2. Read the plan: **§0** (the five rules), **§3** (what a day is), **§4.1** (the hub), **§5 and
   §5.1** (the part contract and real code), **§6** (nothing leaves the project), **§9** (model and
   budget policy), **§12** (the spine slot this day is), **§13** (this project's brief, cast,
   boundary, tools and done-when), **§14** (style, and the four constraints against sameness).
3. Read `docs/GLOSSARY.md`. A term already there is **defined the same way**, not redefined
   differently.
4. Read the previous day of **this same project** — its `LESSON.md` and `CHECKLIST.md`. Unticked
   boxes: say so and ask before proceeding. Build on what this project's earlier days printed.
5. Read this project's `CODEMAP.md` if it exists. **A file printed twice in one project is a bug**
   unless the second is a marked diff against the first, naming the day that printed the original.
6. **Do not open `days/_archive-v3/` or `projects/_archive-v3/` for material.** They were written
   to a deleted contract, and lifting a transcript out of one fabricates an observation (ADR-0007).

## Step 2 — verify reality before you write (Principle 6)

7. **Never invent an interface.** For every symbol, flag, endpoint or field the day uses, fetch the
   live official page and note the URL and the date. The hub §9 tabulates them. If the live
   documentation disagrees with the plan, **stop and propose an amendment** — do not adapt quietly.
8. **Never invent a version or a limit.** Read it live before pinning. Record it in this project's
   `PACKAGES.md`, and anything the authoring repository itself depends on in `docs/PINS.md`.
9. **Never invent a citation.** Open the record live, copy the title from the record. Cite by
   **title and identifier, never by author**, and add a dated row to `docs/SOURCES.md`.
10. **Never invent a transcript.** If you have not run the command, the output block is
    `TODO(me): run <exact command>`. A missing output is fixed by one run; a fabricated one is
    undetectable, and Principle 7 outranks the document's shape.
11. **Run the day before you write it — in a throwaway directory, then delete it.** Build the
    whole day's slice somewhere outside this repository, capture every real transcript, and remove
    the directory when the day is written. Every time this curriculum has written first and run
    second, the day shipped a claim the code contradicted. **The tree never ships and never lands
    in `projects/`** (plan §0 rule 5) — only the transcripts do. Where a provider key is missing, a
    scripted stand-in model is legal (plan §9); it must announce itself as a test double in its own
    docstring and in every transcript it produces.

## Step 3 — plan the split, before writing any prose

12. List the day's subtopics. Group them into **sections that share one mental model** — one stage
    of a pipeline, one phase of a mechanism. State the grouping in the hub §2; an unexplained
    numbering is a bug.
13. Split by **idea boundary, never by length or pace**. There is no target part count. Three
    tests, applied *before* writing: **one idea** (if it needs "also" to introduce its second half,
    it is two parts) · **standalone** (readable cold; name and link its prerequisite *in this
    project*) · **no shortcut** ("for now, just accept that" is banned unless it links forward to
    the part in this project that explains it).
14. **Every day gets at least one part whose subject is a deliberate failure** — break it, read the
    real error, fix it. It declares `failure: true` and is usually `level: production`.
    `python p.py depth` fails a day without one.
15. Assign each part a `level`: `foundation`, `working`, `production`. **A day climbs.** All
    `foundation` is a tutorial; opening at `production` skipped the reader.
16. **Choose one metaphor family for the whole day, from this project's industry.** Grep the day's
    other parts and the hub §1 before choosing. Two parts reaching for the same family read as one
    idea repeated.
17. **Print the planned part list before writing.** If it looks thin, the user will say so, and
    that conversation is cheap now and expensive after twenty documents exist.

## Step 4 — write the parts

Path: `days/<NN-project-slug>/day-DD-<day-slug>/parts/<SS>-<section-slug>/<S>.<T>-<slug>.md`

18. **Name the day folder `day-DD-<slug>`** — the day number **inside its project**, zero-padded,
    then 1–4 kebab-case words from the hub `title` with articles dropped. A bare `day-DD/` is
    rejected. `python p.py new $1 $2` puts it in the right project folder, so scaffold with it
    rather than by hand.
19. **One folder per section**: two digits, then 1–3 kebab-case words. Every part lives inside its
    section folder, never loose in `parts/`, and the folder number must match the number before the
    dot. Sections run 1..N with no gaps, and so do subtopics inside each.
20. **Links are relative to the part's own folder**: a sibling is `1.2-<slug>.md`, another section
    is `../01-<slug>/1.5-<slug>.md`, the hub is `../../LESSON.md`. `prev` and `next` use the same
    form. **A link that leaves the project is a failure, not a convenience.**
21. Every part carries the **seven headings of §5, in order**, plus frontmatter: One-line answer ·
    The idea · The mechanism · [Line by line] · When it breaks · In production · Check yourself.
    Start from `days/_TEMPLATES/PART.md`.
22. **`The idea` is story and plain language merged, and its scene comes from this project's
    industry.** A loss adjuster, a night supervisor, a caller who says "make that two". **No jargon
    in the first paragraph.** Then the concept, terms defined on first use. The scene must still be
    holding the failure the part teaches when you reach the end. **No code in this section.**
    Plan §14: *a scene that would work unchanged in another project has failed its contract.*
23. **`The mechanism` is real code from this project**, headed with its actual path, whole file or
    a marked diff, no import from outside this project, runnable as printed, real output.
24. **Every code block is followed by `**Line by line:**`, at full depth** — every non-obvious
    token, and why that line and not another, as prose bullets. A summary table naming the failure
    each line prevents may follow the prose; it may never replace it.
25. **`When it breaks` carries the real error text, verbatim**, from this project's code on this
    project's data, then two to four sentences of plain words: what someone saw, and the smallest
    fix. If you have not seen the error, cause it.
26. **`In production` is not optional.** Four beats: what a senior writes instead · what degrades
    at scale, **with a number that belongs to this industry** · the review comment · the interview
    question.
27. A diagram whenever the concept is spatial, sequential or a state machine.

## Step 5 — write the hub

28. `days/<NN-project-slug>/day-DD-<slug>/LESSON.md`, from `days/_TEMPLATES/LESSON.md`. **The hub
    never teaches** — no `**Line by line:**` anywhere in it. Ten numbered sections in order (§4.1),
    ending at §10 with the verbatim ledger row and the commit message.
29. `frontmatter.parts` must equal the number of documents actually in `parts/`; the checker
    compares them. `files_printed` lists every path this day prints whole — it feeds `CODEMAP.md`,
    and a file with no day is what makes the Completeness Rule mechanical.
30. §7 states the per-turn request count **across the whole cast**. A three-agent turn is at least
    three requests, and a writer-critic loop is unbounded until you bound it. `0` is an answer.

## Step 6 — write the checklist

31. From `days/_TEMPLATES/CHECKLIST.md`: one box per part (read it · run its check · answer its
    question out loud), the build-brief boxes, **at least one "break it, watch it go red, fix it"**,
    the four independence boxes, the ledger rows, and the commit box. No time estimates.

## Step 7 — verify

32. Run `python p.py depth $1 $2`. **Fix every failure; never hand-wave past one.**
33. Run `python p.py index`, then `python p.py check`.
34. Run `python p.py codemap $1` and confirm every file this day printed appears in it. Do not
    pass `--write` — that is the learner's command, against the learner's tree.
35. **Delete the throwaway build directory**, and confirm `git status` shows nothing added under
    `projects/`.
36. Finish by printing: the part count, the day's check command, the request budget, the files this
    day printed, and the live pages you actually fetched.

---

## Always

- **No clocks in a day document.** Not in frontmatter, not in prose, not in the checklist. The
  sitting budget lives in the plan header and §3. **Never trim an explanation because the day is
  getting long** — add a part, or make it two days.
- **Repetition across projects is the design, sameness inside one is the defect.** You will write
  the session model forty times. Each one opens on a different industry, breaks with a different
  error, and degrades with a different number. If you find yourself pasting, you are writing the
  wrong document.
- **Grammar and punctuation are part of the deliverable**, in every section. A sentence the reader
  has to parse twice has failed.
- **Do not solve the `TODO(me)` reps, and do not build the project.** Teach; do not do the
  learner's work. The whole point of this curriculum is that they type it.
- **All data is synthetic**, every project, every fixture, every eval.
- **Never name a person, instructor, author, channel, academy, bootcamp or training company** — not
  in a lesson, a checklist, a docstring or a commit message. Tool and library names are required
  and unaffected.
- The failure modes this format exists to prevent: splitting without deepening · summary in place
  of explanation · **stopping at the toy example** · assuming a project the reader does not have ·
  code without failure · **trimming to fit** · solved reps · a carried-over clock. If a part gained
  no scene, no real mechanism, no real failure text and no production section, it is not done.
