---
day: NN
part: "S.T"
title: "<what this part teaches, as a phrase — not 'Part 3'>"
ids: [XX-00]
level: foundation        # foundation | working | production — a day climbs
prerequisites: ["<the part that must be read first, or none>"]
prev: "S.T-<slug>.md"    # relative to this folder; "" on the first part
next: "S.T-<slug>.md"    # relative to this folder; "" on the last part
prints: []               # the real file paths this part prints whole
# sources: []            # identifiers this part leans on; add the key only if there are any
# failure: true          # uncomment on the day's deliberate-failure part
---

<!--
  The plan section 5 part contract. Seven headings, in this order, plus frontmatter:

    One-line answer · The idea · The mechanism · [Line by line] · When it breaks ·
    In production · Check yourself

  "Line by line" is a bolded lead-in after EVERY code block that carries logic, not a heading in
  a fixed place. It is required whenever the part carries code and never asked for otherwise.

  No duration, no estimate, no pace — anywhere in this file. The sitting budget lives in the plan
  header and section 3, and nowhere else in this repository.

  Delete every one of these comments before the part is finished.
-->

## One-line answer

<!-- The claim in one sentence, before anything else. A reader who stops here has still learned
     something true. If you cannot write this sentence, the part is not one idea yet. -->

## The idea

<!-- Story and plain language, merged — that is the plan section 5 shape.

     Open with a concrete scene you could have stood in: a courier, a job card, a spare key left
     with a neighbour. NO JARGON IN THE FIRST PARAGRAPH. Then the concept, terms defined on first
     use — including terms from earlier days, with a link back and a row in docs/GLOSSARY.md.
     The scene must still be holding the failure this part teaches when you reach the end of it.

     NO CODE in this section. One metaphor family per day: grep the day's other parts first. -->

## The mechanism

<!-- REAL CODE FROM THIS PROJECT. Five constraints (plan section 5.1):

     1. Real path, real project. Head the block with the file's actual path in THIS project —
        `archive_mcp/server.py`, never `server.py` and never `# in your MCP server`.
     2. Whole file, or a marked diff against a version this project already printed.
        `# ── unchanged from day-02 part 1.2 ──` is legal. `# ... rest of implementation ...`
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

<!-- REQUIRED immediately after every code block that carries logic.

     FULL DEPTH if this part is where the code is taught first: every non-obvious token, and WHY
     THAT LINE AND NOT ANOTHER, as prose bullets.

     RECAP DEPTH if the code is borrowed and taught deeply elsewhere: a table, one row per line
     that carries a decision, each stating THE FAILURE IT PREVENTS — then the PRIMER.md section
     and the deep pointer. A pointer may never stand alone (plan section 6). -->

- `<token>` — <what it does, and why this and not the obvious alternative>

## When it breaks

<!-- Short and story-shaped, two to four sentences. The REAL error text, verbatim — the traceback,
     the status line, the message body — then plain words: someone shipped this on a Friday, this
     is what they saw at 11pm, this is the smallest fix.

     If you have not seen this error, go and cause it. A reconstructed traceback is a fabricated
     result, and the plan forbids those in the same breath as it forbids inventing a version. -->

```text
<!-- the real, pasted error -->
```

## In production

<!-- NOT OPTIONAL. Four beats, short and story-shaped:
       - what a senior writes INSTEAD of the teaching version
       - what degrades at scale, WITH A NUMBER
       - the review comment
       - the interview question
     One real example. This is the section that gets dropped, and dropping it halves the part. -->

## Check yourself

- **Run:** `<command>` — expect `<what>`.
- **Say out loud:** <the question>

---

**Next:** [<title>](<S.T-slug>.md)
