# Packages — P02 Parts Counter

Append-only. **This project pins independently** (plan §9). Two projects may legitimately sit on
different versions of the same package; that is what independence means, and the freshness check at
the start of each project is where the newer one wins.

A value that could not be looked up is written `TODO(<the exact lookup command>)`, never a guess.

## The freshness check — run once, at the start of this project

Plan §10 puts this at the front of a project, not on every day: you pin once and live with it for
eight sittings.

| Question | Answer | Checked |
| --- | --- | --- |
| `google-adk` release notes since the last project — breaking change? | P01 pinned 2.8.0 on 2026-09-09; 2.8.0 is still current. No change, so nothing to amend. | 2026-09-10 |
| MCP spec revision moved? | **This is the project with a boundary, so this one matters.** `TODO(me): open https://modelcontextprotocol.io/specification and record the current revision date here before day 3 prints a server.` Days 1 and 2 build no server, so this is owed by day 3 and not by day 1. | 2026-09-10 |
| Provider free lists re-checked — anything lost its free tier? | Flash-class models are listed free of charge on the free tier. Per-model RPM/TPM/RPD remains **unpublished** — see below. | 2026-09-10 |
| Anything the plan assumed that has since moved? | Nothing new since `docs/adr/ADR-0004-generatecontent-by-hand-and-unpublished-limits.md`, which still holds. | 2026-09-10 |

## Pins

| Package / tool | Version | Date observed | Day | Why, and how it was observed |
| --- | --- | --- | --- | --- |
| Python | 3.12.12 | 2026-09-10 | 11 | Written into this project's own `.python-version` by `uv python pin 3.12.12`, because `requires-python = ">=3.12"` is a floor and names no interpreter. `run.py check`'s `interpreter` check compares it against `sys.version_info`. |
| google-adk | 2.8.0 | 2026-09-10 | 11 | Read from `https://pypi.org/pypi/google-adk/json` (uploaded 2026-08-26T23:26:17Z, `requires_python >=3.10`). The same version P01 pinned, re-checked rather than inherited. |
| pytest | 9.1.1 | 2026-09-10 | 11 | A dev dependency: `run.py check` runs the kit's tests, and a check with no tests behind it is a check that inspects nothing. Latest on PyPI, `requires_python >=3.10`. |
| uv | 0.12.3 | 2026-09-10 | 11 | The one binary `SETUP.md` requires. `uv --version`. |

## Model pins

Enforced by `parts_counter/util/models.py`; `run.py check`'s `model` check refuses a call to
anything not listed.

| Model ID | Role | Status when read | Date observed | Day | Why |
| --- | --- | --- | --- | --- | --- |
| `gemini-3.8-flash` | the counter's one brain | **Stable** | 2026-09-10 | 11 | Read off `https://ai.google.dev/gemini-api/docs/models`, described as "Our most intelligent Flash model, engineered for long-horizon software engineering, autonomous agents, and complex enterprise workflows." Matching P01's pin is a coincidence of dates, not a shared setting. |

**Not used, and recorded so the choice is visible:**

- `gemini-3.5-flash` — ADK 2.8.0's built-in `DEFAULT_MODEL`. Listed **Stable** and described as "Our
  legacy Flash model". An agent that omits `model=` gets it silently.
- `gemini-flash-latest` — the alias ADK's own examples use. Documented as "hot-swapped with every
  new release", so it is a floor rather than a pin. `models.require_pinned` refuses it by name.

## Rate limits

**Not recorded, because they are not published.** `https://ai.google.dev/gemini-api/docs/rate-limits`,
re-checked 2026-09-10, says: "Rate limits depend on a variety of factors (such as your usage tier)
and can be viewed in Google AI Studio" and "Specified rate limits are not guaranteed and actual
capacity may vary." No RPM, TPM or RPD number appears there or on the pricing page.

`TODO(me): read this project's live limits in Google AI Studio and paste them here, with the date.`

This is why `parts_counter/util/budget.py` exists and why its run ceiling is set by this project
rather than derived from the provider: the only limit anybody here can be sure of is the one we
impose. See ADR-0004.
