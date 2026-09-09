# Plan changelog — Prayoga

Principle 8: *if reality changes, the plan is amended first.* Every amendment lands here
**before** any day or any work changes. **Append-only. Newest last.**

An entry answers three questions in this order: **what moved in the world**, **what this plan now
says instead**, and **what that costs** — which days are affected, which IDs move, what has to be
rewritten. An entry that names the change but not its cost is a note, not an amendment.

Anything structural also gets an ADR in `docs/adr/`, and the entry here links it.

---

- 2026-09-07 — **v3.0.0 adopted.** `_shared/` deleted, forty independent repositories, 296
  sittings. The plan as written; sections 0 to 13 are unchanged by everything below.

- 2026-09-08 — **v3.1.0, the toolchain adoption.** *What moved:* nothing in the world. The plan
  described `./p`, a day map and a depth contract in prose no script could read, so the standard
  was stated and never checked. *What the plan now says:* sections 14 to 18 are added. Tracks,
  phases and the day map sit between marker comments; 310 concept IDs are assigned across ten
  tracks, each to exactly one day; a phase is a project. *What it costs:* nothing is rewritten,
  but section 12 and section 17 now both carry day titles, so an edit to one has to reach the
  other. See `docs/adr/ADR-0001-the-plan-as-adopted.md`.

- 2026-09-08 — **v3.1.0, day 0 inserted.** *What moved:* the plan named `./p` in sections 6 and 13
  and never said which sitting builds it, so the first project would have been written by a
  toolchain that did not exist. *What the plan now says:* day 0 is the authoring repository —
  toolchain, skeleton, driver — outside every project, closing `RB-01`, `RB-02` and `RB-03`. P00
  Foundry starts at day 1 and the curriculum runs 0 to 296. *What it costs:* one sitting. No
  project day moved. See `docs/adr/ADR-0002-day-zero-and-the-authoring-repo.md`.

- 2026-09-08 — **v3.1.0, `sitting_minutes` removed from the section 4.1 hub frontmatter.** *What
  moved:* nothing external. Section 3 sets a sitting budget, and section 4.1 then asked every hub
  to carry it as a field. *What the plan now says:* the budget stays in the plan header and in
  section 3, and no day document carries a clock in any form. *What it costs:* a hub can no longer
  state its own budget, which was never information — every hub carried the same number. What it
  buys is that no day can be trimmed to fit one, which section 3 demanded and nothing enforced.

- 2026-09-09 — **v3.1.0, day folders grouped by project.** *What moved:* nothing in the plan. The
  plan never named a path under `days/`, so section 16's "a phase is a project" existed as a
  statement and not as a shape on disk — 297 day folders were headed for one flat listing.
  *What the plan now says:* unchanged. A day now lives at `days/<NN-project-slug>/day-NN-<slug>/`,
  the project folder named from the section 16 phase row and derived by `p.py`, never stored;
  phase 0 is not a project, so its days sit in `days/_authoring/`. *What it costs:* every path
  under `days/` is one level deeper, so a link from one project's day into another's needs one
  more `../`, and nothing checks relative links. Three days moved; one link was fixed by hand. See
  `docs/adr/ADR-0003-days-grouped-by-project.md`.
