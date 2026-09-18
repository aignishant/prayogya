---
day: NN
part: "S.T"
title: "<what this part teaches, as a phrase — not 'Part 3'>"
ids: [XX-00]
level: foundation        # foundation | working | production — a day climbs
prerequisites: ["<the part that must be read first, or none>"]
prev: "S.T-<slug>.md"    # relative to this folder; "" on the first part
next: "S.T-<slug>.md"    # relative to this folder; "" on the last part
sources: []              # identifiers this part leans on; drop the key if none
# failure: true          # uncomment on the day's deliberate-failure part
---

<!--
  Eleven sections, in this order. Three are conditional:
    "The source behind it"    — required exactly when `sources:` above is non-empty
    "Line by line"            — required after every code block that carries logic
    "The source in one demo"  — source documents only; delete it here

  No duration field, no time estimate, no pace — anywhere in this file.
  Delete every one of these comments before the part is finished.
-->

## One-line answer

<!-- The claim in one sentence, before anything else. A reader who stops here has still learned
     something true. If you cannot write this sentence, the part is not one idea yet. -->

## The story

<!-- A concrete scene FIRST: a person, a machine, a failure, a decision. NO JARGON AT ALL.

     Four rules:
     1. A scene the reader has plausibly LIVED. A parcel and a courier. A repair-shop job card.
        A used car checked by a mechanic. Not a nautical chart, not a model railway. Test: could
        the reader have been standing in this scene themselves?
     2. Simple words. If a twelve-year-old could not follow the first sentence, rewrite it.
     3. Load-bearing. The scene must contain the ACTUAL failure or decision this part teaches —
        not a pretty image the part then abandons.
     4. One metaphor family per day. Grep the day's other parts before choosing. -->

## The idea in plain language

<!-- The concept assuming zero prior knowledge. Every term defined on first use — INCLUDING terms
     from earlier days, with a link to the part that introduced them and a row in
     docs/GLOSSARY.md. No code in this section. -->

## Why Prahari needs it

<!-- The concrete later day that breaks without this, named and linked. Never "this is
     important" — that sentence carries no information. -->

## The source behind it

<!-- CONDITIONAL: present exactly when `sources:` in the frontmatter is non-empty; delete the
     heading otherwise. An ADDRESS, not an explanation:

       > **<Exact title>** · `<identifier>` · <year>
       > <url>

     One sentence of what it claimed, then a link to the source document that teaches it — in
     this day's sources/ or an earlier day's. Nothing more; the teaching happens there. -->

## The mechanism

<!-- How it ACTUALLY works: runnable code, the exchange written out, or the diagram. Nothing
     skipped as "obvious". A diagram whenever the concept is spatial, sequential or a state
     machine. -->

```
<!-- the code, the command, or the exchange -->
```

**Line by line:**

<!-- REQUIRED immediately after every code block that carries logic. Every non-obvious token, and
     WHY THAT LINE AND NOT ANOTHER. An unexplained line is a bug in this document: the reader can
     copy it but cannot change it. -->

- `<token>` — <what it does, and why this and not the obvious alternative>

## When it breaks

<!-- The REAL error text, verbatim — the traceback, the status code, the message body. Never a
     paraphrase, never a reconstruction from memory. Then: what it means, and the smallest fix.

     If you have not seen this error yet, go and cause it. -->

```text
<!-- the real, pasted error -->
```

## In production

<!-- NOT OPTIONAL. This is the section that makes the document professional rather than
     introductory, and it is the one that gets dropped.

     Cover: what a professional writes instead of the teaching version · what degrades at scale or
     under pressure · the failure that only shows with real traffic · the review comment a senior
     engineer leaves on the teaching version · the interview question that finds out whether you
     have actually used this. -->

## Check yourself

<!-- One thing to RUN right now, and one question to answer OUT LOUD. Not a quiz — a check that
     can go red, and a sentence you either can or cannot say. -->

- **Run:** `<command>` — expect `<what>`.
- **Say out loud:** <the question>

---

**Next:** [<title>](<S.T-slug>.md)
