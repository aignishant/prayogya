# ADR-0004 — P01 hand-rolls `generateContent`, and free-tier limits stop being printable

- **Date:** 2026-09-09
- **Day:** 4
- **Phase:** P01
- **Status:** accepted
- **Amends:** v3.1.0 — section 9 (model and budget policy) and section 4.1 (hub section 7). No day
  moved, no ID changed, no project renumbered.
- **Related:** ADR-0001

## Context

Before writing day 4 the P01 freshness check required by the plan section 10 was run against the
live provider and framework documentation on 2026-09-09. Three of the plan's standing assumptions
no longer match what the documentation says, and one is confirmed more strongly than it was
written. All four are recorded here because the plan forbids adapting to reality silently.

### 1 · The Gemini API's taught path moved to a stateful API

The plan section 12 gives P01 day 1 as *The loop by hand — think → act → observe, no framework* and
day 2 as *Tools by hand — JSON schemas and the tool-result turn*. Both describe hand-rolling
against a request/response API where the caller carries the conversation.

The provider's guides no longer teach that API. The quickstart, the function-calling guide and the
API-key page now all teach an **Interactions API** at `POST /v1beta/interactions`, checked on
2026-09-09 at `https://ai.google.dev/gemini-api/docs/quickstart` and
`https://ai.google.dev/gemini-api/docs/function-calling`. From
`https://ai.google.dev/gemini-api/docs/migrate-to-interactions`, verbatim:

> While `generateContent` remains fully supported, we recommend the Interactions API for all new
> development.

And from `https://ai.google.dev/api`, verbatim:

> Interactions (CreateInteraction) (Recommended): The recommended standard primitive for building
> with Gemini, optimized for agentic workflows, server-side state management, and complex
> multi-modal, multi-turn conversations.

`generateContent` is **not deprecated**. It remains fully documented at
`https://ai.google.dev/api/generate-content`, which returns HTTP 200 and carries the complete
request and response schema; the deprecations page at
`https://ai.google.dev/gemini-api/docs/deprecations` lists models only and does not mention the
endpoint.

The two are not interchangeable for teaching purposes, and the difference is the exact subject of
day 4. `generateContent` is **stateless**: the caller resends the whole conversation every turn, so
think → act → observe is a loop the learner writes and can watch. Interactions is **stateful**: it
carries the conversation server-side and the next turn references `previous_interaction_id`, so the
loop the plan wants taught is the part the API has taken over. Teaching the loop by hand on
Interactions would mean teaching a loop that is mostly not there.

The framework does not force the choice either way. ADK 2.x drives both — from
`https://adk.dev/agents/models/google-gemini/`, `use_interactions_api=True` on the `Gemini` model
selects the stateful path — so P02 and later are free to adopt it without anything in P01 becoming
wrong.

### 2 · Free-tier rate limits are no longer published

The plan section 9 asks every hub to state a per-turn request count against provider limits, and
section 4.1 gives hub section 7 as *"per-turn model calls per provider, RPM/RPD"*. The RPM/TPM/RPD
table has been removed from `https://ai.google.dev/gemini-api/docs/rate-limits`, checked
2026-09-09. What the page says instead, verbatim, appearing twice:

> Rate limits depend on a variety of factors (such as your usage tier) and can be viewed in Google
> AI Studio. As your tier and account status change over time, your rate limits will automatically
> update.

and:

> Specified rate limits are not guaranteed and actual capacity may vary.

The dimensions are still defined; no number is attached to any of them for any model.
`https://ai.google.dev/pricing` confirms flash models are free of charge on the free tier and
publishes no RPM/TPM/RPD either. There is therefore no number a day document could print without
inventing it, which the plan forbids in the same breath as inventing a version.

### 3 · `GOOGLE_GENAI_USE_VERTEXAI=FALSE` is not in the current framework documentation

The plan section 9 says the primary brain is *"Gemini Flash-class on a free AI Studio key,
`GOOGLE_GENAI_USE_VERTEXAI=FALSE`"*. That variable does not appear on
`https://adk.dev/agents/models/google-gemini/`, checked 2026-09-09. The documented pair is
`GOOGLE_API_KEY` alone for the AI Studio path, and `GOOGLE_CLOUD_PROJECT`,
`GOOGLE_CLOUD_LOCATION` and `GOOGLE_GENAI_USE_ENTERPRISE=True` for the enterprise path. That the
old and new flags are aliases is asserted only in project discussion threads and on no
documentation page, so it cannot be printed as fact.

### 4 · The model-pinning rule is confirmed, and sharpened

The plan section 9 says every agent pins its model explicitly because *"ADK 2.x's default is a
preview model"*. The default is not a preview model, and the real situation is worse. From
`https://adk.dev/api-reference/python/google-adk.html`, verbatim:

> `DEFAULT_MODEL : ClassVar[str] = 'gemini-3.5-flash'`

and, on the same page, the `model` field:

> When not set, the agent will inherit the model from its ancestor. If no ancestor provides a
> model, the agent uses the default model configured via `LlmAgent.set_default_model`. The built-in
> default is `gemini-3.5-flash`.

Confirmed by observation: constructing `Agent(name="probe")` under google-adk 2.8.0 on this machine
on 2026-09-09 gives `canonical_model` of `Gemini(model='gemini-3.5-flash', ...)`.

`https://ai.google.dev/gemini-api/docs/models` (last updated 2026-09-04) lists that model as
**Stable** and describes it verbatim as *"Our legacy Flash model, providing baseline speed and
foundational performance for routine, high-throughput workloads"* — four generations behind
`gemini-3.8-flash`, which the same page lists as Stable and describes as *"Our most intelligent
Flash model, engineered for long-horizon software engineering, autonomous agents, and complex
enterprise workflows."*

So an unpinned agent does not get a preview model; it silently gets the oldest supported one, which
is a quieter bug than the plan anticipated and a better argument for the rule.

The same page's advice on aliases rules out the shortcut the framework's own examples use:

> Latest — Points to the latest release for a specific model variation… This alias will get
> hot-swapped with every new release of a specific model variation.

`gemini-flash-latest` is therefore not a pin, whatever it looks like.

## Decision

**1. P01 hand-rolls `generateContent`, and the Interactions API is where P01 stops and a later
project begins.** Days 4 and 5 build the loop and the tool-result turn against the stateless
endpoint, exactly as the plan section 12 describes them, because that is the version in which the
loop is the learner's code. The curriculum's standing rule is build first and compare after; the
stateful API is the "after", and it is named in P01 as the thing that takes the loop over rather
than pretended out of existence.

No day title, ID or number changes. The plan section 12's P01 map stands as written.

**2. Hub section 7 states the request count and refuses to state the limit.** The per-turn count
across the cast is a fact about our own code, it is knowable, and it stays mandatory. The provider's
RPM/TPM/RPD is not published and becomes a `TODO(me)` naming where to read it — Google AI Studio —
in every hub from day 4 on. A budget document that prints an unverifiable number is worse than one
that says where the number lives.

**3. The AI Studio path is configured by `GOOGLE_API_KEY` alone.** No day writes
`GOOGLE_GENAI_USE_VERTEXAI`, in a `.env.example` or anywhere else, until a documentation page says
what it does.

**4. P01 pins `gemini-3.8-flash`.** Documented Stable on 2026-09-09, current, and described for
agentic workflows. It is pinned as an exact ID in this project's own model registry; no `-latest`
alias appears anywhere in the curriculum. The gap between this pin and ADK's `gemini-3.5-flash`
default is taught in P01 rather than merely avoided — an unpinned agent is four generations stale
and nothing says so, which is the plan section 9 rule with a receipt attached.

Every project pins independently, per the plan section 9, and re-runs the section 10 freshness check
at its own start. P02's pin is P02's decision.

## Consequences

**What this costs.** P01 teaches an endpoint the provider no longer recommends for new work, and a
reader who goes to the quickstart first will find a different API than the one day 4 builds. Day 4
therefore has to say so in its own text, with the dated quotation, rather than leaving the reader to
discover the mismatch and conclude the curriculum is stale. That is a paragraph of honesty in each
of two days, and it is cheaper than teaching a loop that the API hides.

**What it buys.** The loop stays visible. A learner who has resent a conversation by hand
understands what `previous_interaction_id` is doing for them, and can debug it; one who met the
stateful API first has a working system and no model of it.

**What is now owed.** The Interactions API needs a home. It is not in P01's seven days and this ADR
does not create one — that is a plan amendment in its own right, and it should be written when the
project that adopts it is chosen. Until then the curriculum teaches the stateless path and names the
stateful one; it does not claim to have taught it.

**What was checked, and when.** Every URL in the Context section was fetched on 2026-09-09 and its
quoted text copied from the page rather than from memory. The google-adk observations were made on
this machine against google-adk 2.8.0 under CPython 3.12.12 on the same date.
