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
| MCP spec revision moved? | **Yes, and a long way.** The current revision is `2026-07-28`, which removed the `initialize` handshake, removed protocol-level sessions and the `Mcp-Session-Id` header, and made every request self-describing. This project cannot speak it: `google-adk` 2.8.0 pins `mcp<2`, and the 1.x SDK is a legacy-era implementation whose `LATEST_PROTOCOL_VERSION` is `2025-11-25` and whose `DEFAULT_NEGOTIATED_VERSION` is `2025-03-26`, both read from `mcp/types.py` here. A handshake offering `2025-06-18` is echoed back unchanged; one offering an unrecognised string is answered with `2025-11-25` rather than refused. Days 13 to 17 teach the era they can run and quote, in the body of each day, the specification line that removed the mechanism being taught. See `docs/adr/ADR-0005-mcp-era-gap-and-the-1x-pin.md`. | 2026-09-10 |
| Provider free lists re-checked — anything lost its free tier? | Flash-class models are listed free of charge on the free tier. Per-model RPM/TPM/RPD remains **unpublished** — see below. | 2026-09-10 |
| Anything the plan assumed that has since moved? | Nothing new since `docs/adr/ADR-0004-generatecontent-by-hand-and-unpublished-limits.md`, which still holds. | 2026-09-10 |

## Pins

| Package / tool | Version | Date observed | Day | Why, and how it was observed |
| --- | --- | --- | --- | --- |
| Python | 3.12.12 | 2026-09-10 | 11 | Written into this project's own `.python-version` by `uv python pin 3.12.12`, because `requires-python = ">=3.12"` is a floor and names no interpreter. `run.py check`'s `interpreter` check compares it against `sys.version_info`. |
| google-adk | 2.8.0 | 2026-09-10 | 11 | Read from `https://pypi.org/pypi/google-adk/json` (uploaded 2026-08-26T23:26:17Z, `requires_python >=3.10`). The same version P01 pinned, re-checked rather than inherited. |
| pytest | 9.1.1 | 2026-09-10 | 11 | A dev dependency: `run.py check` runs the kit's tests, and a check with no tests behind it is a check that inspects nothing. Latest on PyPI, `requires_python >=3.10`. |
| uv | 0.12.3 | 2026-09-10 | 11 | The one binary `SETUP.md` requires. `uv --version`. |
| mcp | 1.30.0 | 2026-09-10 | 13 | The Python MCP SDK, and **deliberately not the newest release**. See the note below; this is the constraint `google-adk` itself declares. Latest 1.x on PyPI, uploaded 2026-09-07T14:34:14Z, `requires_python >=3.10`. |
| MCP protocol, on the wire here | 2025-11-25 | 2026-09-10 | 13 | What the pinned SDK speaks. `mcp.types.LATEST_PROTOCOL_VERSION`, read on this machine; `DEFAULT_NEGOTIATED_VERSION` is `2025-03-26`. **This is not the current specification revision** — that is `2026-07-28`, which removed the handshake this SDK performs. See ADR-0005. |
| MCP specification, current | 2026-07-28 | 2026-09-10 | 13 | Read from `https://modelcontextprotocol.io/docs/learn/versioning`: "The **current** protocol version is 2026-07-28." This project cannot run it; `google-adk` 2.8.0 pins `mcp<2` and the 1.x line is legacy-era. |

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

## Why `mcp` is pinned to 1.30.0 and not to 2.2.0

`mcp` 2.2.0 exists — it was released on 2026-09-07, the same day as 1.30.0 — and this project does
not use it, because **google-adk 2.8.0 does not support it**. The constraint is `google-adk`'s own:

    mcp>=1.24,<2 ; extra == "mcp"

Two things about that are worth writing down, because both cost time to find.

**The constraint lives behind an extra.** Installing `google-adk` alone does not install `mcp` at
all and does not apply that bound, so `uv add "mcp==2.2.0"` beside a bare `google-adk` **succeeds** —
the resolver has no conflict to find. This project depends on `google-adk[mcp]` precisely so that
the bound is real and a future attempt to move to 2.x fails at resolution rather than at runtime.

**The failure it prevents is silent.** With `mcp` 2.2.0 installed, `google/adk/tools/mcp_tool/`
raises `ModuleNotFoundError: No module named 'mcp.shared.session'` on import — and the package
catches it in a bare `try`, leaving `__all__ = []`. `from google.adk.tools.mcp_tool import
McpToolset` then fails with an `ImportError` that names the toolset rather than the version
mismatch, and nothing anywhere says the two packages disagree.

The SDK's own 2.x error message is the clearest statement of the break, and it is quoted here
because a reader on 2.x will meet it first:

    ModuleNotFoundError: No module named 'mcp.server.fastmcp'. This is mcp 2.x, where FastMCP was
    renamed to MCPServer (from mcp.server.mcpserver import MCPServer) and other APIs changed; see
    the migration guide at
    https://py.sdk.modelcontextprotocol.io/v2/migration/#fastmcp-renamed-to-mcpserver or pin
    'mcp<2' to keep running v1 code.

`TODO(me): re-check this at the start of P03. When google-adk widens its bound to allow mcp 2.x,
the move is FastMCP -> MCPServer, mcp.server.fastmcp -> mcp.server.mcpserver, and stateless_http
moves off the constructor onto run_streamable_http_async() / streamable_http_app().`
