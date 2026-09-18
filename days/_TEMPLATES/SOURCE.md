---
day: NN
source: "<one identifier — arXiv:2401.12345 | doi:10.1145/… | RFC 9110 | spec:name-revision>"
title: "<the source's exact title, copied from the record and never from memory>"
ids: [XX-00]
level: production        # a source document is almost always production
prerequisites: ["../parts/01-<slug>/1.1-<slug>.md"]
prev: ""                 # relative to sources/
next: ""
---

<!--
  A source document carries a part's frontmatter MINUS `part` — it is not a subtopic of anything —
  and PLUS `source:` (singular), the one identifier it teaches.

  It carries the same eleven sections, but four of them mean something different here, and one
  more becomes required. Read the guidance in each section below.

  A SOURCE IS TAUGHT ONCE IN THE WHOLE CURRICULUM. Before writing this file, check
  docs/wiki/ENTITIES.md. If the identifier is already there, do not write this document — cite the
  existing one and link it.

  Before writing a single line: OPEN THE RECORD LIVE and copy the title from it. Then add a dated
  row to docs/SOURCES.md. Never a remembered citation.

  Delete every one of these comments before the document is finished.
-->

> **<Exact title>** · `<identifier>` · <year>
> <url> — record checked <YYYY-MM-DD>

## One-line answer

<!-- What this source claimed, in one sentence a reader can repeat. -->

## The story

<!-- The problem the field had BEFORE this document existed. A scene, plain words, no jargon and
     no equations. Someone was stuck; this is what stuck looked like.

     The four story rules still apply: a setting the reader has lived in, simple words,
     load-bearing, and no collision with another story in the same day. -->

## The idea in plain language

<!-- The claim, stated so a reader who has never opened a document like this can hold it and
     repeat it. Define the terms the title itself uses. -->

## Why Prahari needs it

<!-- The part of THIS day, linked, that runs on this idea. -->

## The mechanism

<!-- The method itself, written out at the depth the rest of the day is written at.

     NOT THE ABSTRACT, PARAPHRASED. If this section could have been written without reading past
     the first page, it has not been written. -->

## The source in one demo

<!-- REQUIRED on a source document: the source made runnable and stripped to nothing but itself.

     Four rules, and the third is the one that makes it honest:

     1. ONLY this source's contribution. Not a small project that uses the idea — a small project
        whose entire reason to exist IS the idea. Subtractive test: if a file could be deleted and
        the claim still lands, delete it. Two or three files is normal.
     2. END TO END and actually runnable: the whole file tree, every file's contents, the one
        command, and its REAL PASTED OUTPUT. If you have not run it, leave the output block as a
        TODO naming the exact command — NEVER AN INVENTED TRANSCRIPT.
     3. AN ABLATION SWITCH — one flag that turns the contribution OFF, with BOTH runs' output
        shown. A demo that cannot be switched off has proved that code ran, not that this idea
        mattered. It is also a check that can go RED.
     4. Inside the project's constraints, like everything else — on this project that means a CPU
        and zero model requests unless the hub's §6 says otherwise.

     It lands in lab/sources/<source-slug>/ and is given COMPLETE. This is teaching material, not
     an exercise — the unsolved TODO(me) reps stay in the hub's build brief. -->

```text
lab/sources/<source-slug>/
├── <file>
└── <file>
```

**Line by line:**

- `<file>` — <why this file exists, and why nothing else does>

### With the idea on

```text
<!-- the real, pasted output -->
```

### With the idea off (the ablation)

```text
<!-- the real, pasted output of the same command with the switch flipped -->
```

<!-- Then one sentence: what changed between the two runs, and why that is the source's claim. -->

## When it breaks

<!-- Where the claim does NOT hold: what it assumed, what it was measured on, the scale it was
     never tried at, the follow-up that narrowed it.

     A source document with no limits section has taught a press release. -->

## In production

<!-- WHAT SURVIVED AND WHAT DID NOT. Which half of this document is in shipped systems today,
     which half the field quietly dropped, and what replaced it.

     This is the section that makes a source document worth reading rather than citing. -->

## Check yourself

- **Find:** <one thing to locate in the source itself — a figure, a limit, a caveat>.
- **Say out loud:** what did this source actually claim, and what do we do differently now?
