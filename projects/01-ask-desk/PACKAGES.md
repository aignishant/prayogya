# Packages — P01 Ask Desk

Append-only. **This project pins independently** (plan §9). Two projects in this curriculum may
legitimately sit on different versions of the same package; that is what independence means, and
the freshness check (§10) at the start of each project is where the newer one wins.

Every row records the value **actually observed**, the date it was observed, and the day that added
it. A value that could not be looked up is written `TODO(<the exact lookup command>)`, never a
guess.

## The freshness check — run once, at the start of this project

Plan §10 puts this at the front of a project rather than on every day, because you pin once and
live with it for seven sittings.

| Question | Answer | Checked |
| --- | --- | --- |
| `google-adk` release notes since the last project — breaking change? | P00 used no framework, so there is no previous pin to compare against. 2.8.0 is the current release. | 2026-09-09 |
| MCP spec revision moved? | Not applicable: P01 has no MCP boundary. Leg 2 arrives in P02, which runs its own check. | 2026-09-09 |
| Provider free lists re-checked — anything lost its free tier? | The pricing page lists Flash-class models as free of charge on the free tier. The per-model RPM/TPM/RPD table has been **withdrawn** and now directs you to Google AI Studio, so no ceiling is recorded here. | 2026-09-09 |
| Anything the plan assumed that has since moved? | Three things. See `docs/adr/ADR-0004-generatecontent-by-hand-and-unpublished-limits.md`. | 2026-09-09 |

## Pins

| Package | Version | Date observed | Day | Why, and how it was observed |
| ---- | ----- | ------------- | --- | ---------------------------- |
| Python | 3.12.12 | 2026-09-09 | 4 | Written into `.python-version`, not left to `requires-python = ">=3.12"` to resolve. `uv python pin 3.12.12`, then confirmed by `run.py check`'s `interpreter` check comparing `sys.version_info` against the file. |
| google-adk | 2.8.0 | 2026-09-09 | 4 | The framework this project adopts on day 3. Latest release on PyPI, uploaded 2026-08-26T23:26:17Z, `requires_python >=3.10`. Read from `https://pypi.org/pypi/google-adk/json`; confirmed installed by `import google.adk; google.adk.__version__`. |
| uv | 0.12.3 | 2026-09-09 | 4 | The one binary that owns this project's environment. `uv --version`. |

## Model pins

Models are pinned the same way packages are, and for the same reason. The registry that enforces
this is `ask_desk/util/models.py`, and `run.py check`'s `model` check refuses a call to anything not
listed here.

| Model ID | Role | Status when read | Date observed | Day | Why |
| --- | --- | --- | --- | --- | --- |
| `gemini-3.8-flash` | the desk's one brain | **Stable** | 2026-09-09 | 4 | Read off `https://ai.google.dev/gemini-api/docs/models`, which describes it as "Our most intelligent Flash model, engineered for long-horizon software engineering, autonomous agents, and complex enterprise workflows." Named explicitly on every agent and every raw call. |

**Not used, and recorded so the choice is visible:**

- `gemini-3.5-flash` — ADK 2.8.0's built-in default (`DEFAULT_MODEL`). Listed **Stable**, and described
  by the provider as "Our legacy Flash model". An agent that omits `model=` gets this one and says
  nothing about it, which is the reason plan §9 requires an explicit pin and the subject of day 3
  part 1.2.
- `gemini-flash-latest` — the alias the framework's own examples use. Rejected: the models page
  documents `-latest` as "hot-swapped with every new release of a specific model variation", so it
  is a floor rather than a pin. `models.require_pinned` refuses it by name.

## Rate limits

**Not recorded, deliberately, because they are not published.**
`https://ai.google.dev/gemini-api/docs/rate-limits`, checked 2026-09-09, says: "Rate limits depend
on a variety of factors (such as your usage tier) and can be viewed in Google AI Studio" and
"Specified rate limits are not guaranteed and actual capacity may vary." No RPM, TPM or RPD number
appears on that page or on the pricing page for any model.

`TODO(me): read this project's live limits in Google AI Studio and paste them here, with the date.`

Until that row exists, every hub's §7 states the **request count** — a fact about this project's own
code, which is knowable — and marks the ceiling as unknown rather than printing a number nobody can
verify. See ADR-0004.
