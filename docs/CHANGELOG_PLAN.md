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

- 2026-09-09 — **v3.1.0, P01 hand-rolls `generateContent`; the Interactions API is named, not
  taught.** *What moved:* the provider's guides. The quickstart and function-calling pages now
  teach a stateful Interactions API at `POST /v1beta/interactions`; the migration page says
  `generateContent` "remains fully supported" but is no longer recommended for new development.
  Checked live 2026-09-09. *What the plan now says:* section 12's P01 map is unchanged — days 4 and
  5 hand-roll the stateless endpoint, because that is the version in which think → act → observe is
  the learner's own loop rather than server-side state. Both days say so in their own text, with the
  dated quotation. *What it costs:* P01 teaches an endpoint the provider does not recommend for new
  work, and the Interactions API now has no home in the curriculum — a further amendment owes it
  one. See `docs/adr/ADR-0004-generatecontent-by-hand-and-unpublished-limits.md`.

- 2026-09-09 — **v3.1.0, hub section 7 states the count and refuses to state the limit.** *What
  moved:* the free-tier RPM/TPM/RPD table has been removed from the provider's rate-limit page,
  which now says limits "can be viewed in Google AI Studio" and that "specified rate limits are not
  guaranteed". Checked live 2026-09-09; the pricing page publishes no numbers either. *What the
  plan now says:* section 4.1's hub section 7 keeps the per-turn request count across the whole
  cast, which is a fact about our own code and stays mandatory, and replaces the provider limit with
  a `TODO(me)` naming where to read it. *What it costs:* no hub can state a quota ceiling, so
  "will this fit in the free tier" stops being answerable from the document. What it buys is that no
  hub prints a number nobody can verify.

- 2026-09-09 — **v3.1.0, section 9: `GOOGLE_GENAI_USE_VERTEXAI=FALSE` removed.** *What moved:* the
  variable does not appear on the framework's current Gemini model page, checked 2026-09-09. The
  documented AI Studio path is `GOOGLE_API_KEY` alone; the enterprise path uses
  `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_LOCATION` and `GOOGLE_GENAI_USE_ENTERPRISE=True`. That the
  old and new flags are aliases is claimed only in discussion threads and on no documentation page.
  *What the plan now says:* the AI Studio path is configured by `GOOGLE_API_KEY` alone, and no day
  writes `GOOGLE_GENAI_USE_VERTEXAI` anywhere until a page says what it does. *What it costs:*
  nothing observed; the flag was never exercised, since day 0 through day 3 make no model calls.

- 2026-09-09 — **v3.1.0, section 9: the default-model claim corrected, and the rule kept.** *What
  moved:* the plan said ADK 2.x's default is "a preview model". It is not. The framework's API
  reference documents `DEFAULT_MODEL : ClassVar[str] = 'gemini-3.5-flash'`, confirmed by
  constructing an agent under google-adk 2.8.0 on this machine on 2026-09-09, and the provider's
  models page lists that ID as **Stable** while describing it as "our legacy Flash model" — four
  generations behind `gemini-3.8-flash`. *What the plan now says:* every agent still pins its model
  explicitly, and the reason is stated accurately: an unpinned agent silently gets the oldest
  supported model, not a preview one. P01 pins `gemini-3.8-flash`; no `-latest` alias is used
  anywhere, since the models page documents those as hot-swapped on every release. *What it costs:*
  nothing. The rule is unchanged and now has a citation instead of an assertion behind it.

- 2026-09-10 — **v3.1.0, P02 teaches the MCP handshake era and names the revision that deleted
  it. No section amended.** *What moved:* the specification. The current revision is `2026-07-28`,
  which removed the `initialize`/`notifications/initialized` handshake, removed protocol-level
  sessions and the `Mcp-Session-Id` header, and made every request carry its own version and
  capabilities. Checked live 2026-09-10. *What the plan says:* unchanged, and it reads correctly —
  §12 already gives P02 day 3 as "the stateless core; the phone-call → web reframe" and day 5 as
  "Lifecycle, stateless-first — the old handshake as history", which is what the specification has
  now done. §5.1's `FastMCP(..., stateless_http=True)` worked example also stands, because it is
  correct for the SDK line the toolchain pins. *What it costs:* `google-adk` 2.8.0 declares
  `mcp<2,>=1.24`, so P02 runs a legacy-era stack and cannot execute the modern shapes. Days 13 to
  17 therefore teach the era they can run, and every day that teaches a legacy mechanism quotes,
  in its body, the specification line that removed it. See
  `docs/adr/ADR-0005-mcp-era-gap-and-the-1x-pin.md`.

- 2026-09-10 — **v3.1.0 → v4.0.0. The Depth Rule is deleted and repetition replaces it; every
  project is taught from zero, ships the whole feature set, and numbers its own days from 0.**
  *What moved:* almost everything structural. §0 now carries **four** rules — Completeness
  (widened to include `.gitignore`, `pyproject.toml`, `Dockerfile`, CI and the `run` driver),
  **Repetition** (every concept a project uses is taught *in that project, at full depth* — recap
  depth is gone), **From-Scratch** (day 0 begins on a bare machine, in every project), and
  **Full-Stack** (every project ships all eighteen subsystems of the new §12 spine). §6 was the
  pointer format and is now *"nothing leaves the project"*, enforced by a grep in
  `python p.py check`. `PRIMER.md` and the *Borrowed concepts* table are deleted, because both
  existed only to make an out-of-project pointer survivable. §15's ID scheme, the ten-track table
  and the global day map are deleted; days are numbered inside their project from 0 and addressed
  as `NN D`. §11 renames all forty projects to their real-world industry and resizes them to 16–22
  days. §12 is new — the eighteen-slot spine. §13 is new — each project's brief plus the extra days
  its subject earns, which `p.py` expands against the spine so the two cannot drift. §14 is new —
  the style rules, including the test that stops forty projects reading like one pasted forty
  times: *a scene that would work unchanged in another project has failed its contract.*
  *Why:* v3 claimed independence and delivered it for code only. Its own Depth Rule sent a reader
  with one folder to a folder they did not have, and the scaffolding that decides whether a clone
  runs at all lived in P00, which nothing required anyone to read. The learner named this on
  2026-09-10. *What it costs:* the curriculum roughly triples, 297 sittings to **816**, and every
  core concept is now written forty times at full depth. That number was quoted and accepted before
  the rewrite began. *What else changed:* the eighteen v3 days and their project trees are archived
  unedited under `days/_archive-v3/` and `projects/_archive-v3/`, the v3 ledger is kept verbatim
  with the v4 ledger below it inside `granth:ledger` markers, and `docs/TRACEABILITY.md` and
  `docs/CURRICULUM_INDEX.md` are deleted with the ID scheme they indexed. `p.py` was rewritten for
  project-local addressing. See `docs/adr/ADR-0006-repetition-replaces-depth-once.md` and
  `docs/adr/ADR-0007-v3-days-archived-and-the-restart.md`.

- 2026-09-10 — **v4.0.0 → v4.1.0. Rule 5: the day document is the deliverable, and nothing is ever
  written into `projects/`.** *What moved:* §0 gains a fifth rule. The author writes day documents;
  **the learner types every file and runs every command from them.** A day must therefore carry
  every file in full at its real path, every command in the order it is run, and what each command
  actually printed. §5.1 gains a sixth constraint on real code — *typed, not received*. §1's opening
  and §2's preamble now say who builds the tree, and §2 names the day that prints each of the four
  project documents: `PROJECT.md` and `SETUP.md` on day 0, `README.md` and `CODEMAP.md` on the ship
  day. `python p.py codemap NN` now prints rather than writes; `--write` is a command the learner
  runs against their own tree. *Why:* the plan never said who types the code, and on the first day
  written under v4 that ambiguity resolved the wrong way — a complete, working
  `projects/01-claims-intake-desk/` was built before the day document was written, which is the
  answer key next to the exercise. The learner named it immediately. *What it costs:* longer day
  documents, and strictly more authoring work — build it, verify it, transcribe it, throw the build
  away. There is no mechanical check for the rule; the cold clone and `CODEMAP.md` are what catch a
  day that omitted a file. *What did not change:* Principle 7. The author still runs every command,
  now in a throwaway directory outside the repository — only the transcripts ship. See
  `docs/adr/ADR-0008-the-document-is-the-deliverable.md`.
