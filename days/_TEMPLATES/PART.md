---
project: "PNN <name>"
day: NN
part: "S.T"
title: "<what this part teaches, as a phrase — not 'Part 3'>"
spine: NN                # the plan §12 spine slot this part serves
level: foundation        # foundation | working | production — a day climbs
prerequisites: ["<the part OF THIS PROJECT that must be read first, or none>"]
prev: "S.T-<slug>.md"    # relative to this folder; "" on the first part
next: "S.T-<slug>.md"    # relative to this folder; "" on the last part
prints: []               # the real file paths this part prints whole
# cites: []              # citation identifiers; each needs a dated row in docs/SOURCES.md
# failure: true          # uncomment on the day's deliberate-failure part
---

<!--
  The plan §5 part contract. Seven headings, in this order, plus frontmatter:

    One-line answer · The idea · The mechanism · [Line by line] · When it breaks ·
    In production · Check yourself

  "Line by line" is a bolded lead-in after EVERY code block that carries logic, not a heading in
  a fixed place. It is required whenever the part carries code and never asked for otherwise.

  TWO RULES THAT OUTRANK THE SHAPE:

  1. REPETITION (plan §0 rule 2). Everything this part uses is taught HERE, at full depth. There
     is no recap table, no "covered elsewhere", no pointer out. If this concept has been written
     thirty-nine times before in this curriculum, write it a fortieth time — better, because this
     industry gives it consequences the other thirty-nine did not have.

  2. NOTHING LEAVES THE PROJECT (plan §6). No path into another project, no project name, no
     "as we saw". `python p.py check` greps for it and fails the day.

  No duration, no estimate, no pace — anywhere in this file. The sitting budget lives in the plan
  header and §3, and nowhere else in this repository.

  Delete every one of these comments before the part is finished.
-->

## One-line answer

<!-- The claim in one sentence, before anything else. A reader who stops here has still learned
     something true. If you cannot write this sentence, the part is not one idea yet. -->

## The idea

<!-- Story and plain language, merged — that is the plan §5 shape.

     Open with a concrete scene you could have stood in, TAKEN FROM THIS PROJECT'S INDUSTRY: a
     loss adjuster who cannot remember which claim yesterday's call was about, a night supervisor
     with a jammed line, a caller who says "make that two". NO JARGON IN THE FIRST PARAGRAPH.

     Then the concept, terms defined on first use — including terms an earlier day of THIS
     project defined, with a link back and a row in docs/GLOSSARY.md. The scene must still be
     holding the failure this part teaches when you reach the end of it.

     NO CODE in this section. One metaphor family per day: grep the day's other parts first.
     Plan §14: a scene that would work unchanged in another project has failed its contract. -->

## The mechanism

<!-- REAL CODE FROM THIS PROJECT. Five constraints (plan §5.1):

     1. Real path, real project. Head the block with the file's actual path in THIS project —
        `claims_mcp/server.py`, never `server.py` and never `# in your MCP server`.
     2. Whole file, or a marked diff against a version this project already printed.
        `# ── unchanged from day 03 part 1.2 ──` is legal. `# ... rest of implementation ...`
        is not.
     3. No import from outside this project. If it needs a helper, this project printed it.
     4. Runnable as printed. Imports at the top, no invented API, verified live on the day.
     5. The output is real. If you have not run it, the block is `TODO(me): run <exact command>`
        — NEVER an invented transcript. A missing output is fixed by one run; a fabricated one is
        undetectable.
-->

```text
<!-- the code, at its real path -->
```

**Line by line:**

<!-- REQUIRED immediately after every code block that carries logic, and there is only ONE depth
     now: full. Every non-obvious token, and WHY THAT LINE AND NOT ANOTHER, as prose bullets.

     v4 deleted recap depth along with the Depth Rule (plan §5.2, ADR-0006). A table naming the
     failure each line prevents is still welcome — but AFTER the prose, as a summary, never
     instead of it. -->

- `<token>` — <what it does, and why this and not the obvious alternative>

## When it breaks

<!-- Short and story-shaped, two to four sentences. The REAL error text, verbatim — the traceback,
     the status line, the message body — then plain words: someone shipped this on a Friday, this
     is what they saw at 11pm, this is the smallest fix.

     The error must come from THIS project's code, on THIS project's data. If you have not seen
     it, go and cause it. A reconstructed traceback is a fabricated result, and the plan forbids
     those in the same breath as it forbids inventing a version. -->

```text
<!-- the real, pasted error -->
```

## In production

<!-- NOT OPTIONAL. Four beats, short and story-shaped:
       - what a senior writes INSTEAD of the teaching version
       - what degrades at scale, WITH A NUMBER THAT BELONGS TO THIS INDUSTRY
       - the review comment
       - the interview question
     One real example. This is the section that gets dropped, and dropping it halves the part. -->

## Check yourself

- **Run:** `<command>` — expect `<what>`.
- **Say out loud:** <the question>

---

**Next:** [<title>](<S.T-slug>.md)
