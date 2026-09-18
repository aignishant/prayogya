# Pin ledger — Prahari

Append-only. **Never invent a fact** (plan §2, Principle 6). Every version, tool, limit or quota
this project depends on gets a row here with the value **actually observed**, the date it was
observed, the day that added it, and why.

If a value could not be looked up, the row says `TODO(<the exact lookup command>)` — never a
guess. A guess that happens to be right is still a guess, and the next reader cannot tell which
kind they are holding.

A later row may **supersede** an earlier one: a dated observation superseding a dated observation
is not an amendment, it is the ledger doing its job. Say so in the `Why` column.

| What | Value | Date observed | Day | Why, and how it was observed |
| ---- | ----- | ------------- | --- | ---------------------------- |
| MCP specification revision | `2026-07-28` | 2026-09-18 | plan | Baseline for the Tools & MCP track. Read from `https://modelcontextprotocol.io/specification/latest`, which links its schema at `schema/2026-07-28/schema.ts`. Transports: stdio, Streamable HTTP. Extensions: Tasks, Skills over MCP, MCP Apps. |
| `mcp` (PyPI) | 2.2.0, requires Python ≥ 3.10 | 2026-09-18 | plan | `https://pypi.org/pypi/mcp/json`. Described on the record as a major rework of the SDK; re-read on day 46 before the first install. |
| `openai` (PyPI) | 3.15.0 | 2026-09-18 | plan | `https://pypi.org/pypi/openai/json`. Used only as a client for the OpenAI-compatible endpoints of Groq, Gemini and OpenRouter after the raw-HTTP day. |
| `groq` (PyPI) | 1.7.0 | 2026-09-18 | plan | `https://pypi.org/pypi/groq/json`. Awareness only; the project speaks the compatible wire format directly. |
| `google-genai` (PyPI) | 2.24.0 | 2026-09-18 | plan | `https://pypi.org/pypi/google-genai/json`. Awareness only, for the day the compatibility layer silently ignores a parameter. |
| Gemini OpenAI-compatible base URL | `https://generativelanguage.googleapis.com/v1beta/openai/` | 2026-09-18 | plan | `https://ai.google.dev/gemini-api/docs/openai`. Documented as beta; unsupported parameters are silently ignored — day 25's trap. |
| OpenRouter `:free` model limits | 20 requests/minute; 50 requests/day without purchased credits (1000/day with ≥ $10 ever purchased); daily counter resets on UTC days | 2026-09-18 | plan | `https://openrouter.ai/docs/api-reference/limits`. This is why OpenRouter is not the default provider. |
| Groq free-tier limits | per-model RPM/RPD/TPM; 429 carries `retry-after`, and every response carries `x-ratelimit-limit-requests`, `x-ratelimit-remaining-requests`, `x-ratelimit-reset-requests`, `x-ratelimit-limit-tokens`, `x-ratelimit-remaining-tokens`, `x-ratelimit-reset-tokens` | 2026-09-18 | plan | `https://console.groq.com/docs/rate-limits`. The per-model numbers for the chat models this project uses are recorded on day 26 when the model is chosen. |
| Gemini free-tier limits | `TODO(open https://aistudio.google.com/rate-limit while signed in and copy the RPM / RPD / TPM for the flash model chosen on day 25)` | 2026-09-18 | plan | `https://ai.google.dev/gemini-api/docs/rate-limits` no longer lists the numbers; it points at the signed-in dashboard. Not guessed. |
| Python | 3.12 (3.12.10 observed on the machine) | 2026-09-18 | plan | `python --version` on the development machine. Pinned by `uv` on day 0. |
| `uv` (PyPI) | 0.12.16 | 2026-09-18 | plan | `https://pypi.org/pypi/uv/json`. Re-read with `uv --version` on day 0. |
| `ruff` (PyPI) | 0.16.8 | 2026-09-18 | plan | `https://pypi.org/pypi/ruff/json`. |
| `pytest` (PyPI) | 9.1.1 | 2026-09-18 | plan | `https://pypi.org/pypi/pytest/json`. |
| `mypy` (PyPI) | 2.3.1 | 2026-09-18 | plan | `https://pypi.org/pypi/mypy/json`. |
| `pydantic` (PyPI) | 2.13.5 | 2026-09-18 | plan | `https://pypi.org/pypi/pydantic/json`. |
| `fastapi` (PyPI) | 0.141.1 | 2026-09-18 | plan | `https://pypi.org/pypi/fastapi/json`. First used on day 111. |
| `fastembed` (PyPI) | 0.8.0 | 2026-09-18 | plan | `https://pypi.org/pypi/fastembed/json`. Local embeddings so retrieval costs zero requests. First used on day 60. |
| `sqlite-vec` (PyPI) | 0.1.9 | 2026-09-18 | plan | `https://pypi.org/pypi/sqlite-vec/json`. Record carries no summary; the extension is audited in `PROVENANCE.md` on day 61 before it first loads. |
| `langgraph` (PyPI) | 1.2.11 | 2026-09-18 | plan | `https://pypi.org/pypi/langgraph/json`. Adopted on day 90, after the hand-rolled orchestrator. |
| `opentelemetry-sdk` (PyPI) | 1.44.0 | 2026-09-18 | plan | `https://pypi.org/pypi/opentelemetry-sdk/json`. First used on day 105. |
| `torch` (PyPI) | 2.14.0 | 2026-09-18 | plan | `https://pypi.org/pypi/torch/json`. CPU build only; first used on day 12. |
| `numpy` (PyPI) | 2.5.3, requires Python ≥ 3.12 | 2026-09-18 | plan | `https://pypi.org/pypi/numpy/json`. Attention by hand on day 10 is written in numpy before torch. |
| `transformers` (PyPI) | 5.17.0 | 2026-09-18 | plan | `https://pypi.org/pypi/transformers/json`. Loads the small open-weight models on day 18. |
| `peft` (PyPI) | 0.21.0 | 2026-09-18 | plan | `https://pypi.org/pypi/peft/json`. LoRA and QLoRA on day 18. |
| `trl` (PyPI) | 1.13.0 | 2026-09-18 | plan | `https://pypi.org/pypi/trl/json`. SFT on day 19, DPO on day 20 — after each is done by hand first. |
