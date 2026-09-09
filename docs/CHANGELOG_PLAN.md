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
