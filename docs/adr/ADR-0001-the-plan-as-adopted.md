# ADR-0001 — The v3.0.0 plan is adopted whole, and made machine-readable rather than rewritten

- **Date:** 2026-09-08
- **Day:** before day 0
- **Phase:** 0
- **Status:** accepted
- **Amends:** v3.0.0 to v3.1.0, adding sections 14 to 18 and removing one frontmatter field from 4.1
- **Related:** ADR-0002

## Context

`00_MASTER_PLAN_v3.0.0.md` existed and nothing else did. One file, 705 lines, in a folder with no
git history, no ledgers, no driver, and no day.

The plan is unusually complete for a document written before any of the work: it has a
completeness rule, a depth rule, a primer rule, an eight-section part contract in section 5, a
ten-section hub contract in section 4.1, forty project maps in section 12, and a verification
story in section 7. What it does not have is any way to *check* a single one of those.

Concretely: section 5 says a part carries eight sections in a fixed order, and nothing would have
noticed a part with six. Section 8 says a day closes exactly its assigned IDs, and there were no
IDs. Section 6 says `./p check` enforces the depth contract, and `./p` did not exist. Section 11
lists forty projects and section 12 lists their days, but no table anywhere gives a sitting a
number, so "is day 137 next?" was a question only a human counting could answer — across 296 rows.

That gap compounds. Every project written against an unchecked contract is a project whose parts
have to be re-read by hand later to find out whether they met it, and there are forty of them.

## Decision

**Adopt v3.0.0 whole. Add to it; rewrite none of it.**

Sections 0 to 13 are byte-for-byte what the author wrote. The original file is kept at
`docs/archive/00_MASTER_PLAN_v3.0.0.original.md` so the claim is checkable rather than trusted.

Four additions, all after section 13:

1. **Section 15, the tracks** — ten threads with a prefix each, between `granth:tracks` markers.
2. **Section 16, the phases** — a phase is a project, between `granth:phases` markers.
3. **Section 17, the day map** — one row per sitting, 0 to 296, each with its title and the IDs it
   closes, between `granth:day-map` markers.
4. **Section 14 and section 18** — what changed, and the amendment record.

**The load-bearing half is the markers, not the tables.** A heading can be reworded by accident
and a table can be moved; a marker comment cannot be either, without meaning to. `p.py` reads only
what is between them, so a person editing the plan and a script parsing it cannot drift apart.

The depth contract is **not** replaced by the granth default. `granth.toml` is configured to
enforce the plan section 5 part contract — seven headings plus frontmatter — and the plan section
4.1 hub contract, ten numbered sections. The checker was bent to the plan, not the plan to the
checker.

**One removal:** `sitting_minutes: 60` from the section 4.1 hub frontmatter. The sitting budget
stays in the plan header and section 3. It must not sit in a day document, where it quietly
licenses the one edit section 3 already forbids — cutting an explanation because the day is
running long.

## Options considered

| Option | Why not |
| --- | --- |
| **Do nothing — keep the plan as prose and write days by hand** | The contract stays unenforceable across 297 sittings and forty repositories. The first project to quietly drop an *In production* section would not be found until someone re-read it, and by then there would be six more like it. |
| **Rewrite the plan into the granth master-plan template** | The template is a good default and this plan is better than the default: the completeness rule and the primer are specific to a curriculum of independent repositories, and no generic template has them. Rewriting would have cost the plan its actual content to gain a familiar shape. |
| **Adopt the granth eleven-section part contract instead of the plan section 5 eight** | It would have invalidated section 5 on day 0, before a single part had been written against it, and forced a real amendment to a rule that has not yet been tried. The plan contract is configured in and can be revisited once there is evidence. |
| **Number days per project rather than globally** | Matches section 12 exactly and reads well. But then day numbers repeat forty times, the order guard has nothing to guard, and progress across the curriculum cannot be stated in one number. Section 17 keeps both: a global number, with the project and its own day number in the title. |

## Consequences

- **Better:** the depth contract is now checked. `python p.py doctor` proves every ID lands on
  exactly one day; `depth` refuses a part missing a section or carrying a clock; `index` builds
  traceability from the days themselves rather than from a claim.
- **Worse:** section 12 and section 17 both carry day titles. That is real duplication, and an
  edit to a project map has to reach the day map too. It was accepted because section 12 is how a
  project is *designed* and section 17 is how a sitting is *ordered*, and collapsing them would
  have meant rewriting section 12 — which is exactly what this ADR refuses to do.
- **Also worse:** the plan is now 1386 lines, and the part a reader needs on any given day is
  still sections 3, 4, 5 and 12. Section 14 says so at the top of the addition.
- **New failure mode:** the tables inside the markers can drift from sections 11 and 12 without
  anything noticing, because no checker reads prose. What catches it is that `doctor` reads the
  day map and every hub is checked against it, so a drifted row surfaces the day it is written.
- **Revisit if:** a project is written and the section 5 contract turns out to produce padding —
  sections filled to satisfy the checker rather than the reader. That is evidence the contract is
  wrong for this subject, and it gets its own ADR rather than a quiet exception.
