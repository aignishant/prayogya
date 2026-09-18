---
plan: prahari
version: "v1.0.0"
topic: "Building agentic AI systems in Python, from the transformer up to a client-ready platform: models, agents, MCP, RAG, memory, multi-agent orchestration, trust, ops and plugins"
tracks: 10
ids: 145
days: 137
phases: 18
doc_architecture: "hub + parts/ (see §11)"
amended: "2026-09-18"
---

# MASTER PLAN v1.0.0 — Prahari

## Building agentic AI systems in Python, from the transformer up to a client-ready platform: models, agents, MCP, RAG, memory, multi-agent orchestration, trust, ops and plugins

> **Prahari** — प्रहरी, *the watchman*: the one who stays awake so that others do not have to. The
> artifact is a security-operations desk that watches alerts; the curriculum is the discipline of
> building one you can trust with the keys.
>
> **Purpose: this is the single source of truth.** Every other document in this repository points
> back here. When a day document and this plan disagree, this plan is right and the day is a bug.
> When *reality* and this plan disagree, the plan is amended first (Principle 8) — never patched
> around in silence.

---

## Table of contents

| § | Section |
| --- | --- |
| 1 | The vision — what exists at the end |
| 2 | Core principles — the rules that are never broken |
| 3 | The artifact — what actually gets built |
| 4 | Constraints & budget |
| 5 | The baseline — what this plan is pinned to, and how it is verified |
| 6 | The tracks and the ID scheme |
| 7 | The phases |
| 8 | The day map — day to IDs closed |
| 9 | Phase gates and the freshness check |
| 10 | Ledgers and traceability |
| **11** | **The depth contract — how a day is written** |
| 12 | The style guide |
| 13 | Amendment record |

---

## 1 · The vision — what exists at the end

By day 136 you will have **two working agentic applications — Prahari, a security-operations desk,
and Sahayak, a customer-support desk — both running on `neev`, a reusable agent platform you
extracted from the first and proved with the second, plus a tiny language model you trained and
specialised yourself so that nothing inside the bigger ones is a mystery**, and you will be able to
defend every decision inside it.

The measure is not how many days were finished. It is whether, handed the finished thing and a
sceptical reviewer, you can explain each part, say what it costs, name what breaks it, and show
the check that catches the breakage.

Three things this plan is trying to prevent:

1. **The tutorial ceiling.** Following steps produces something that runs and understanding that
   evaporates the moment the inputs change. Every subtopic here therefore ends at the real-system
   version, not the toy one (Principle 10).
2. **The forgotten middle.** In a curriculum this long, day 3 is forgotten by day 66. Every term
   is defined on first use, *including terms from earlier days, with a link back*, and the
   glossary is a ledger rather than an afterthought.
3. **The unverifiable claim.** Notes written from memory rot silently. Every version, interface
   and citation is looked up on the day it is used, and the document names what was checked
   (Principle 6).

### 1.1 Stated non-goals

These are decisions, not blind spots. Writing them down stops each of them being re-litigated on
a day when the real subject is something else.

- **No real SIEM, ticketing or CRM integration.** Prahari and Sahayak talk to behaving fakes, plus
  exactly one real third-party MCP server so that "a stranger's tools" is experienced and not
  imagined. A client integration is a plugin written on the client's day, not here.
- **No large-scale training and no GPU-cluster tooling.** Every model trained in this repository
  runs on a CPU laptop: a character-level model from scratch, and adapters on small open-weight
  models. The lesson is the mechanism; the scale is somebody else's bill.
- **No user interface beyond a minimal approval queue, and no Kubernetes.** Serving stops at a
  container image and a compose file. A dashboard and an orchestrator are products, not concepts.

---

## 2 · Core principles — the rules that are never broken

<!-- granth:principles:start -->

1. **Doc-first.** The day document is written before the work; the work follows the document. A
   thing built first and explained afterwards gets explained in the shape it happened to take,
   which is not the same as the shape it should have.
2. **One day, one commit.** Append-only, traceable history. The repository is the memory.
3. **Build first, compare after.** Hand-roll the mechanism once, then adopt the tool that does it
   for you — so the tool is a convenience and never a mystery. A tool adopted before the
   mechanism is understood becomes a thing you cannot debug.
4. **Every concept is load-bearing.** If removing it would not change the artifact, it does not
   get a day. Coverage is not the goal; a working understanding is.
5. **Depth over density.** A day is a hub plus one document per subtopic, never one long page. If
   a subtopic cannot be read on its own, understood without scrolling past a different subtopic,
   and explained back out loud, it has not been split finely enough. A wall of text is not depth —
   it is depth's disguise. The full contract is §11.
6. **Never invent a fact.** A version, an interface, a limit, a citation: look it up **live on the
   day it is used**, or leave a `TODO` containing **the exact lookup command**. The document names
   what was checked and when. A guess that happens to be right is still a guess, and the next
   reader cannot tell which kind they are holding.
7. **Fail honestly.** Errors surface, escalate and are logged. Nothing fabricates a result to
   cover an error — and this applies to the writer as much as to anything that is built. An
   unrun command's output is a `TODO`, never a plausible transcript.
8. **If reality changes, the plan is amended first.** A moved specification, a renamed interface,
   a changed limit: amend via `docs/CHANGELOG_PLAN.md` and, for anything structural, an ADR —
   *then* continue. Days are never silently patched. Stop and say so.
9. **Every day ends with a check that can go RED.** A check that cannot fail has verified nothing.
   At least one per day, and at least one day per phase whose subject is a deliberate failure.
10. **Assume no prior knowledge, finish at production.** Every subtopic opens where a reader who
    has never met the idea can stand, defines its jargon on first use — including jargon from
    earlier days, with a link back — and does not stop at the toy example. It ends with how the
    idea is used in a real system: what a professional does instead of the teaching version, what
    breaks at scale or under pressure, the review comment, the interview question. Strong basics
    and advanced technique are the same document, in that order.
11. **A day is a unit of subject, not a unit of time.** No document carries a time estimate, a
    duration, an "estimated hours" field or a suggested pace — not in frontmatter, not in prose,
    not in a checklist. A topic is finished when it is understood, in one sitting or in five.
    **Nothing is ever trimmed to fit a clock**; a day that runs long gets another part, not a
    shorter explanation.
12. **Blast radius before capability.** Every new power arrives together with its containment
    story: what it can reach, what stops it, and what the blast looks like when the stop fails.
13. **Every model call is a request against a quota.** The providers this project runs on are
    free tiers with hard daily request caps. A day states its request budget in §6 of its hub, a
    test never calls a live model when a recorded response exists, and a loop with no step cap is
    a bug before it is a design.
14. **Nothing acts without a trail.** An agent that can change the world writes what it did, why,
    and who allowed it, before the change lands. An action with no audit row did not happen, and
    an approval that cannot be found was never given.

<!-- granth:principles:end -->

> Principles 5, 10 and 11 are made concrete by **§11, the depth contract**, and are enforced
> mechanically by `granth.py` (`python granth.py depth N`) — and, for everything a script
> cannot judge, by reading.

---

## 3 · The artifact — what actually gets built

**Three things, in a deliberate order, and a fourth that is the proof.**

**A tiny language model you trained yourself** (phases 1–2). Before a single agent is written,
you build a transformer in plain numpy and then in PyTorch: one attention head by hand, the block,
the stack, a byte-pair tokenizer trained on your own text, a training loop whose loss curve you
watched. Then you do the four things a client will ask about — fine-tune an existing small model
with LoRA, turn a base model into an instruction-following one, tune it on preferences with DPO,
and distil a bigger model into a smaller one — and finish by specialising a base model into a
coding model and *measuring* whether it got better at code without getting worse at everything
else. None of this is production-scale. All of it is the reason the rest of the curriculum is not
magic.

**Prahari, a security-operations desk** (phases 3–14). Alerts arrive at a webhook and become
cases. A *triage* agent classifies them. An *investigator* agent enriches them through tools served
over MCP — a fake SIEM, a fake ticket desk, one real third-party server — and asks a corpus of
runbooks and past incidents through a retrieval pipeline you built chunk by chunk. A *responder*
proposes an action that cannot land without a human's approval. A *reviewer* audits the whole run.
Every agent remembers: what was said this session, what happened last time to this asset, what is
known about this user — with tenants kept apart and a leak test that proves it. Every action leaves
an audit row. Every run is traced, costed, evaluated offline against a golden set, and served from
a container. Every mechanism — the tool loop, JSON-RPC, retrieval, the orchestrator — is written by
hand first and only then replaced by the library that does it, so that the library is a convenience
you can debug rather than a box you cannot.

**`neev`, the platform** (phases 15–16). Once Prahari works, its reusable half is extracted:
runtime, tools and MCP, knowledge, memory, orchestration, trust, ops — with a plugin architecture so
that a connector is something you drop in rather than something you fork. The extraction is done
with the eval report as the referee: Prahari on `neev` must produce the same numbers as Prahari
alone, or the extraction changed behaviour and is not done.

**Sahayak, a customer-support desk** (phase 17) — the proof. A second, unrelated vertical built on
`neev` in eight days: its own domain, its own tools over MCP, its own knowledge and memory, its own
approval rule (refunds), deployed beside Prahari as a second tenant with no leak between them. The
number of days it takes is the evidence you put in front of a client. The hand-off — onboarding
checklist, runbook, what a client actually receives — is the last thing written.

The artifact is what makes Principle 4 checkable. "Is this concept load-bearing?" has a mechanical
answer: delete it and see whether the artifact still works. Nothing here is learned in the
abstract and hoped to be useful later.

---

## 4 · Constraints & budget

| Constraint | Value | What it implies |
| --- | --- | --- |
| **Model access** | Free-tier API keys for Groq, Gemini and OpenRouter. No paid plan. | All three speak the OpenAI chat-completions wire format, so one provider interface covers all of them (day 25). Groq is the default development loop; Gemini is the second provider; OpenRouter's `:free` models are reserved for the portability days because of their daily cap. **Every day states its request budget** (Principle 13). |
| **Request caps, not token caps** | OpenRouter `:free`: 20 requests/minute, **50 requests/day** without purchased credits. Groq: per-model daily caps, `retry-after` on 429. Gemini free-tier: `TODO(open https://aistudio.google.com/rate-limit and record the numbers in docs/PINS.md)`. | Retry with backoff on 429 is day 26, not an afterthought. **Recorded responses (day 28) are mandatory from that day on**: a test that calls a live model when a cassette exists is a defect. Evals run offline. |
| **Hardware** | One CPU laptop. No GPU. | Models trained from scratch are character-level and small. Fine-tuning uses adapters on open-weight models in the ~100M–500M range. Distillation and preference tuning run at toy scale. Any step that would need a GPU is designed to run on CPU with a smaller model and *say so*, never to be skipped. |
| **Embeddings** | Local, via `fastembed`. | Retrieval costs zero requests. The corpus is small enough that indexing on a laptop is the normal case. |
| **Storage** | SQLite for everything stateful — vectors (`sqlite-vec`), keyword search (FTS5), memory, checkpoints, the audit log. | No database server to run. One file per tenant is a legitimate isolation strategy and is taught as one. |
| **Language and toolchain** | Python 3.12 pinned by `uv`; `ruff` for lint and format; `mypy` strict on the package; `pytest`. | `python granth.py check` runs all four before the depth contract. A red lint is a red day. |
| **Platform** | Windows 11, PowerShell as the primary shell. Commands are written to run there and under a POSIX shell where the difference matters. | A command that only works on one shell says which. |
| **Secrets** | `.env` at the root, gitignored from day 0, loaded explicitly. | A key that reaches a log, a cassette or a commit is a failure day's subject (day 101), not an accident. |
| **Spend** | ₹0 / $0 on model APIs. | The budget in every hub's §6 is a count of requests, and `0` is the usual answer once cassettes exist. |

A constraint written down is a curriculum. A constraint discovered on day 40 is a rewrite.

---

## 5 · The baseline — what this plan is pinned to, and how it is verified

| What | Pinned to | Verified how | Re-checked |
| --- | --- | --- | --- |
| Model Context Protocol specification | revision `2026-07-28` — transports: stdio and Streamable HTTP; extensions: Tasks, Skills over MCP, MCP Apps | `https://modelcontextprotocol.io/specification/latest`, opened 2026-09-18 | every phase gate from phase 5 onward |
| `mcp` Python SDK | 2.2.0 (Python ≥ 3.10) | `https://pypi.org/pypi/mcp/json`, opened 2026-09-18 | at the phase 5 and 6 gates |
| Python and the toolchain | Python 3.12 · uv 0.12.16 · ruff 0.16.8 · pytest 9.1.1 · mypy 2.3.1 | PyPI JSON records, opened 2026-09-18; `uv --version` on day 0 | every phase gate |
| Provider wire format | OpenAI chat-completions shape via `openai` 3.15.0; Gemini's compatibility endpoint at `https://generativelanguage.googleapis.com/v1beta/openai/` (documented as beta) | provider documentation, opened 2026-09-18 | at the phase 3 gate and whenever a provider returns a shape the day did not expect |
| Model and training libraries | torch 2.14.0 · numpy 2.5.3 · transformers 5.17.0 · peft 0.21.0 · trl 1.13.0 | PyPI JSON records, opened 2026-09-18 | at the phase 2 gate |
| Retrieval, orchestration, serving, observability | fastembed 0.8.0 · sqlite-vec 0.1.9 · langgraph 1.2.11 · fastapi 0.141.1 · pydantic 2.13.5 · opentelemetry-sdk 1.44.0 | PyPI JSON records, opened 2026-09-18 | at the gate of the phase that first uses each |

Every row above is repeated in `docs/PINS.md` with its date. The day that first installs a package
re-reads the version live and records what it actually got.

**The verification rule (Principle 6), in three faces:**

- **Versions.** Read the version live before pinning it. Record package, version, the date it was
  observed, the day that added it and why, in `docs/PINS.md`. A failed lookup leaves
  `TODO(<the exact command>)`, never a guess.
- **Interfaces.** Every symbol, flag, endpoint or field a day uses is checked against the official
  documentation **on the day it is used**, and the document names the page checked. If the live
  documentation disagrees with this plan, **stop and propose an amendment** — do not adapt
  silently.
- **Citations.** Every source a day teaches or cites is opened live and its title copied from the
  record, never from memory, with a dated row in `docs/SOURCES.md`. This is the strictest of the
  three, because it fails the most quietly: a wrong version pin breaks the next install, while a
  plausible identifier attached to the wrong title survives for years. **Cite by title and
  identifier, never by author** (§12.5).

---

## 6 · The tracks and the ID scheme

Every concept in this plan has an ID. A day **closes** an ID when the concept is built into the
artifact — or demonstrably exercised against it — and the day's gates are green.
`docs/TRACEABILITY.md` is regenerated from the day hubs; **an open ID from a completed phase is a
bug**, not a backlog item.

<!-- granth:tracks:start -->

| Track | Prefix | Count | What runs through it |
| --- | --- | --- | --- |
| Foundations | `FND` | 8 | what a language model does and does not do: text in and out, tokens, the context window, sampling, hallucination, prompting, and what makes a model in a loop an agent |
| Model | `MDL` | 16 | the transformer built by hand, a tokenizer and a tiny model trained from scratch, then fine-tuning, instruction tuning, preference tuning, distillation and specialisation on small open models — all on a CPU |
| Runtime | `RT` | 10 | the agent loop: the wire format, providers, the 429, request budgets, structured output, the tool loop, streaming, the system prompt as code |
| Tools & MCP | `MCP` | 16 | a tool as a schema, a registry by hand, JSON-RPC and stdio by hand, then the SDK: server, client, resources, prompts, Streamable HTTP, authorisation, elicitation, tasks, versioning, a stranger's server |
| Knowledge | `RAG` | 14 | ingestion, chunking, local embeddings, a vector store, keyword search, hybrid fusion, reranking, query rewriting, grounding, evaluation, retrieval as a tool |
| Memory | `MEM` | 10 | working, episodic and semantic memory; summarisation, write policies, isolation, forgetting, poisoning, evaluation |
| Orchestration | `ORC` | 14 | shared state, a supervisor by hand, handoff, fan-out, the reviewer, loop guards, checkpoints, human in the loop, then the graph library; an agent as a tool |
| Trust | `TR` | 17 | the audit log, injection done on purpose, the threat model, input and output guardrails, the approval gate, least privilege, secrets, sandboxing, red-teaming, isolation |
| Ops | `OPS` | 16 | request accounting, recorded responses, tracing, structured logs, the eval harness, the model as judge, CI, the service, containers, backpressure, health, chaos |
| Product & platform | `PLT` | 24 | Prahari's domain and fakes, plugins, the extraction into `neev`, Sahayak, multi-tenancy, the hand-off |

<!-- granth:tracks:end -->

**Total: 145 concept IDs.**

> Some IDs are **parked** — awareness-level, deliberately not built. You learn the map, you do not
> build the thing. A parked ID is marked in its day document and still closes normally. Parking is
> a decision recorded in the open, which is the opposite of a gap.

The authoritative statement of what an ID *means* is the row that assigns it in §8. This section
gives the shape; §8 gives the contract.

---

## 7 · The phases

A phase is a run of days that share one theme and end at one gate. The gate is the point: it is
where the work stops being a set of documents and has to behave.

<!-- granth:phases:start -->

| Phase | Days | Theme | The gate |
| --- | --- | --- | --- |
| 0 | 0–1 | Setup | `python granth.py check` is green on an empty package, and a planted secret cannot be committed |
| 1 | 2–8 | What a model is | you can say out loud, and draw, the difference between a chatbot, a workflow and an agent, and the token-count check predicts the provider's bill |
| 2 | 9–23 | Inside the model | your specialised model beats the base model on your task eval and is not worse on the general one — measured, not felt |
| 3 | 24–35 | The loop by hand | the triage agent runs the hand-rolled tool loop on all three providers, under a request budget, with every test green offline |
| 4 | 36–41 | The domain | a webhook alert becomes a case with an audit trail, and the poisoned alert is logged rather than obeyed |
| 5 | 42–46 | The protocol by hand | the hand-rolled MCP client talks to the hand-rolled server *and* to the SDK server over stdio |
| 6 | 47–56 | MCP in full | every Prahari enrichment is reachable over stdio and Streamable HTTP from two clients, and one third-party server is plugged in |
| 7 | 57–63 | Retrieval by hand | hybrid retrieval beats vector-only and keyword-only on the golden set |
| 8 | 64–70 | Retrieval you can trust | the investigator cites the right runbook, and the retrieval-off ablation goes red |
| 9 | 71–80 | Memory | the same alert twice is recognised from memory, and the cross-tenant leak test is green |
| 10 | 81–88 | Orchestration by hand | four agents, one case, and a checkpoint on disk |
| 11 | 89–94 | Orchestration under pressure | the end-to-end run survives a kill mid-run and resumes from its checkpoint |
| 12 | 95–104 | Trust | an injected alert cannot act without approval, and the red-team set is green |
| 13 | 105–110 | Observing and evaluating | an eval report produced by CI, offline, that can fail the build |
| 14 | 111–116 | Serving | `docker compose up` serves Prahari, and chaos day was recovered from |
| 15 | 117–121 | Plugins | the ticket-desk connector loads as a plugin, and a bad one is refused |
| 16 | 122–128 | Extraction | Prahari on `neev` produces the identical eval report |
| 17 | 129–136 | The second vertical and the hand-off | Sahayak is green on `neev` in eight days, two tenants share one deployment with no leak, and the onboarding checklist is complete |

<!-- granth:phases:end -->

Every phase gate also includes the freshness check (§9).

---

## 8 · The day map — day to IDs closed

> **The authoritative day-to-ID assignment.** A day document closes **exactly** these IDs — no
> more, no fewer. A day that wants to close a different ID is asking for a plan amendment, and the
> amendment is written before the day is.
>
> The table below is read by `granth.py` as well as by people, which is why it sits between
> markers. Keep the three columns and keep one row per day; everything else about it is free.

<!-- granth:day-map:start -->

### Phase 0 — Setup (days 0–1)

| Day | Title | IDs closed |
| --- | --- | --- |
| 0 | The machine and the repository — uv, the Python pin, git, the secrets rule | — |
| 1 | The toolchain gate — ruff, mypy, pytest, and `check` green on an empty package | — |

### Phase 1 — What a model is (days 2–8)

| Day | Title | IDs closed |
| --- | --- | --- |
| 2 | Text in, text out — what a language model actually does, and what it does not | FND-01 |
| 3 | Tokens — why the model does not see words, and why that costs money | FND-02 |
| 4 | The context window — the only memory the model has, and why it runs out | FND-03 |
| 5 | Sampling — temperature, top-p, and why the same question gets two answers | FND-04 |
| 6 | Hallucination — why a model invents, and why confidence is not evidence | FND-05 |
| 7 | Prompting — instructions, examples, roles, and the limits of asking nicely | FND-06 |
| 8 | What an agent is — a model in a loop with tools, and why that changes everything | FND-07, FND-08 |

### Phase 2 — Inside the model (days 9–23)

| Day | Title | IDs closed |
| --- | --- | --- |
| 9 | Numbers for words — embeddings, and why similar words land near each other | MDL-01 |
| 10 | Attention by hand — query, key, value, one head in plain numpy | MDL-02 |
| 11 | Many heads and position — multi-head attention, positional encoding, why order needs help | MDL-03 |
| 12 | The transformer block — attention, feed-forward, residuals, normalisation, stacked | MDL-04 |
| 13 | Three shapes of model — decoder-only, encoder-only, encoder–decoder, and what each is for | MDL-05 |
| 14 | A tokenizer from scratch — byte-pair encoding, trained on your own text | MDL-06 |
| 15 | Train a tiny language model from scratch — the loop, the loss, the curve | MDL-07 |
| 16 | Sampling from your own model — greedy, temperature, top-k and top-p, the KV cache | MDL-08 |
| 17 | Scaling laws — compute, data, parameters, and why a client never trains from scratch | MDL-09 |
| 18 | Fine-tuning an existing model — full fine-tune against LoRA and QLoRA, on a small open model | MDL-10 |
| 19 | Instruction tuning — base model to chat model, and the shape of SFT data | MDL-11 |
| 20 | Preference tuning — RLHF as the idea, DPO as the practice | MDL-12 |
| 21 | Distillation — a big model teaches a small one; synthetic data and its risks | MDL-13 |
| 22 | Specialising — base model to coding model or domain model, and the eval that proves it | MDL-14 |
| 23 | The model that forgot — catastrophic forgetting, over-fitting, the benchmark that dropped | MDL-15, MDL-16 |

### Phase 3 — The loop by hand (days 24–35)

| Day | Title | IDs closed |
| --- | --- | --- |
| 24 | One call over raw HTTP — the chat-completions wire format | RT-01 |
| 25 | Three providers, one shape — Groq, Gemini, OpenRouter behind one interface | RT-02 |
| 26 | The 429 — rate limits, retry-after, backoff, jitter | RT-03 |
| 27 | The request budget — counting calls and refusing past the cap | RT-04, OPS-01 |
| 28 | Recorded responses — cassettes so tests run offline and free | OPS-02 |
| 29 | Structured output — JSON schema, pydantic, the repair loop | RT-05 |
| 30 | A tool is a schema — describing a function to a model | MCP-01 |
| 31 | The tool loop by hand — call, execute, return, repeat | RT-06 |
| 32 | Streaming — deltas, and what breaks mid-stream | RT-07 |
| 33 | The model that lied — malformed tool calls, invented arguments, refusals | RT-08 |
| 34 | The system prompt as code — versioned, tested, diffed | RT-09 |
| 35 | Gate — the triage agent as a unit under test, on all three providers | RT-10 |

### Phase 4 — The domain (days 36–41)

| Day | Title | IDs closed |
| --- | --- | --- |
| 36 | Alerts, incidents, cases — Prahari's domain model as typed data | PLT-01 |
| 37 | The fake SIEM and the fake ticket desk — test doubles that behave | PLT-02 |
| 38 | A playbook is data — steps, conditions, the executor | PLT-03 |
| 39 | Intake — the webhook that turns a raw alert into a case | PLT-04 |
| 40 | The audit log, version zero — append-only, every decision recorded | TR-01 |
| 41 | The poisoned alert — an alert body that talks to the model | TR-02 |

### Phase 5 — The protocol by hand (days 42–46)

| Day | Title | IDs closed |
| --- | --- | --- |
| 42 | A tool registry by hand — discovery, validation, dispatch | MCP-02 |
| 43 | JSON-RPC 2.0 by hand — requests, notifications, errors, ids | MCP-03 |
| 44 | stdio by hand — newline-framed messages over a subprocess | MCP-04 |
| 45 | The MCP server, hand-rolled — tools/list, tools/call, capabilities | MCP-05 |
| 46 | Adopt the SDK — the same server in `mcp`, and what it hides | MCP-06 |

### Phase 6 — MCP in full (days 47–56)

| Day | Title | IDs closed |
| --- | --- | --- |
| 47 | Resources and prompts — context and templates as primitives | MCP-07 |
| 48 | The MCP client — Prahari consumes its own enrichment server | MCP-08 |
| 49 | Streamable HTTP — the endpoint, the SSE stream, request metadata | MCP-09 |
| 50 | Authorisation over HTTP — who may call, and how the token travels | MCP-10 |
| 51 | Elicitation — the server asks the human a question | MCP-11 |
| 52 | Long-running tools — the Tasks extension, polling, durable handles | MCP-12 |
| 53 | A stranger's server — a third-party MCP server, trusting nothing it says | MCP-13, TR-03 |
| 54 | The tool that lies — untrusted annotations, description injection | TR-04 |
| 55 | Versioning and backward compatibility — era detection, old clients | MCP-14 |
| 56 | Gate — every enrichment over both transports, from two clients | MCP-15 |

### Phase 7 — Retrieval by hand (days 57–63)

| Day | Title | IDs closed |
| --- | --- | --- |
| 57 | Why retrieval — the context window is not a database | RAG-01 |
| 58 | Ingestion — runbooks and past incidents into a corpus with provenance | RAG-02 |
| 59 | Chunking — by structure, by size, by overlap | RAG-03 |
| 60 | Embeddings, locally — vectors and similarity with fastembed | RAG-04 |
| 61 | The vector store — sqlite-vec, indexing, nearest neighbours | RAG-05 |
| 62 | Keyword search — FTS5, BM25, what vectors miss | RAG-06 |
| 63 | Hybrid retrieval — reciprocal rank fusion, and the golden set that proves it | RAG-07 |

### Phase 8 — Retrieval you can trust (days 64–70)

| Day | Title | IDs closed |
| --- | --- | --- |
| 64 | Reranking — a second pass, cost against recall | RAG-08 |
| 65 | Query rewriting — multi-query, HyDE, the question the model should have asked | RAG-09 |
| 66 | Grounding and citations — answers that point at their chunk | RAG-10 |
| 67 | Retrieval evaluation — recall@k, MRR, a set that can go red | RAG-11, OPS-03 |
| 68 | Retrieval as a tool — the investigator asks the corpus | RAG-12 |
| 69 | The confident wrong chunk — stale runbook, near-duplicate, the ablation | RAG-13 |
| 70 | Gate — the right runbook, cited; retrieval-off goes red | RAG-14 |

### Phase 9 — Memory (days 71–80)

| Day | Title | IDs closed |
| --- | --- | --- |
| 71 | Working memory — the context window as a budget, compaction | MEM-01 |
| 72 | Summarisation — rolling summaries, and what gets lost | MEM-02 |
| 73 | Episodic memory — past incidents as retrievable episodes | MEM-03 |
| 74 | Semantic memory — facts about assets and users, extracted and stored | MEM-04 |
| 75 | Write policies — what gets remembered, by whom, when | MEM-05 |
| 76 | Isolation — per tenant, per user, and the leak test | MEM-06, TR-05 |
| 77 | Forgetting — TTL, decay, deletion on request | MEM-07 |
| 78 | Memory poisoning — a remembered lie | MEM-08 |
| 79 | Evaluating memory — is the second incident recognised? | MEM-09 |
| 80 | Gate — the same alert twice, recognised; isolation green | MEM-10 |

### Phase 10 — Orchestration by hand (days 81–88)

| Day | Title | IDs closed |
| --- | --- | --- |
| 81 | Why more than one agent — the single-prompt ceiling | ORC-01 |
| 82 | Shared state — the case as the blackboard | ORC-02 |
| 83 | The supervisor by hand — route, delegate, return | ORC-03 |
| 84 | Handoff — one agent passes the case, context travels with it | ORC-04 |
| 85 | Fan-out — parallel enrichment with asyncio, gathering results | ORC-05 |
| 86 | The reviewer — an agent that audits another agent's run | ORC-06 |
| 87 | Loop and deadlock guards — step caps, cycle detection | ORC-07 |
| 88 | Checkpoints — persist the run, resume after a crash | ORC-08 |

### Phase 11 — Orchestration under pressure (days 89–94)

| Day | Title | IDs closed |
| --- | --- | --- |
| 89 | Human in the loop — interrupt, wait, resume | ORC-09 |
| 90 | Adopt the graph library — LangGraph over the hand-rolled orchestrator | ORC-10 |
| 91 | An agent as a tool — one agent exposed over MCP to another | ORC-11, MCP-16 |
| 92 | Two agents arguing forever | ORC-12 |
| 93 | Kill it mid-run — crash on purpose, resume from the checkpoint | ORC-13 |
| 94 | Gate — triage to investigator to responder to reviewer, end to end, survives a kill | ORC-14 |

### Phase 12 — Trust (days 95–104)

| Day | Title | IDs closed |
| --- | --- | --- |
| 95 | Threat model of an agent — what can reach what | TR-06 |
| 96 | Prompt injection via tool output — done on purpose | TR-07 |
| 97 | Input guardrails — classify, strip, refuse | TR-08 |
| 98 | Output guardrails — schema, policy, PII | TR-09 |
| 99 | The approval gate — no action without a human, and the trail it leaves | TR-10 |
| 100 | Least privilege — tool allow-lists per agent, scopes | TR-11 |
| 101 | Secrets — the vault, rotation, the log that must never see them | TR-12 |
| 102 | Sandboxing execution — containers, timeouts, network off | TR-13 |
| 103 | Red-team evaluation — an adversarial golden set | TR-14, OPS-04 |
| 104 | Gate — an injected alert cannot act without approval; red-team green | TR-15 |

### Phase 13 — Observing and evaluating (days 105–110)

| Day | Title | IDs closed |
| --- | --- | --- |
| 105 | Tracing — OpenTelemetry spans across agent, tool and model | OPS-05 |
| 106 | Structured logs — correlation ids, what to log, what never to | OPS-06 |
| 107 | Cost and request accounting — per run, per tenant, per provider | OPS-07 |
| 108 | The eval harness — golden set, scoring, the report | OPS-08 |
| 109 | The model as judge — rubric, bias, a judge you can distrust | OPS-09 |
| 110 | Regression in CI — cassettes, offline evals, thresholds that fail the build | OPS-10 |

### Phase 14 — Serving (days 111–116)

| Day | Title | IDs closed |
| --- | --- | --- |
| 111 | The service — FastAPI, the run endpoint, background jobs | OPS-11 |
| 112 | Containers — Dockerfile, compose, config that differs per environment | OPS-12 |
| 113 | Backpressure at the edge — queue, shed, return 429 outward | OPS-13 |
| 114 | Health, readiness, graceful shutdown | OPS-14 |
| 115 | Chaos day — provider down, disk full, quota exhausted | OPS-15 |
| 116 | Gate — `docker compose up` serves Prahari; CI runs evals offline | OPS-16 |

### Phase 15 — Plugins (days 117–121)

| Day | Title | IDs closed |
| --- | --- | --- |
| 117 | What a plugin is — manifest, contract, lifecycle | PLT-05 |
| 118 | Discovery — entry points, importlib, the registry | PLT-06 |
| 119 | A connector as a plugin — the ticket desk moved out | PLT-07 |
| 120 | Versioning — semver, compatibility ranges, the plugin that no longer loads | PLT-08 |
| 121 | Plugin sandboxing — what a plugin may touch, and the one that reaches further | PLT-09, TR-16 |

### Phase 16 — Extraction (days 122–128)

| Day | Title | IDs closed |
| --- | --- | --- |
| 122 | Finding the seams — dependency direction, what belongs to the platform | PLT-10 |
| 123 | Extract the runtime — loop, providers, budgets into `neev` | PLT-11 |
| 124 | Extract tools, MCP and knowledge | PLT-12 |
| 125 | Extract memory and orchestration | PLT-13 |
| 126 | Extract trust and ops | PLT-14 |
| 127 | Prahari on the platform — the same evals, the same numbers | PLT-15 |
| 128 | Gate — zero behaviour change, measured by the eval report | PLT-16 |

### Phase 17 — The second vertical and the hand-off (days 129–136)

| Day | Title | IDs closed |
| --- | --- | --- |
| 129 | Sahayak — a support desk's domain model in one day | PLT-17 |
| 130 | Its tools over MCP — the CRM and order fakes | PLT-18 |
| 131 | Its knowledge — policies and past tickets | PLT-19 |
| 132 | Its memory and orchestration — per customer, router to specialists | PLT-20 |
| 133 | Its trust and deployment — approval on refunds, compose up | PLT-21 |
| 134 | Multi-tenancy — two clients, one deployment, no leak | PLT-22, TR-17 |
| 135 | The hand-off — onboarding checklist, runbook, what a client receives | PLT-23 |
| 136 | Final gate — both apps green, the portfolio, the day-count as evidence | PLT-24 |

<!-- granth:day-map:end -->

---

## 9 · Phase gates and the freshness check

A phase is **green** only when all six hold:

1. Every day in the phase has its row in `docs/PROGRESS.md`, with gates green.
2. `docs/TRACEABILITY.md` shows **no open IDs** from this or any earlier phase.
3. `python granth.py check` passes on the whole repository — the local toolchain, the depth contract for
   every written day, and the generated documents being current.
4. Every day in the phase has a `parts/` directory. A day with no `parts/` is not written (§11.2),
   so a phase containing one cannot be green.
5. The **freshness check** passes:
   - The MCP specification's `latest` page is re-opened and its revision string compared with §5.
     A new revision is an amendment before it is a day.
   - Each provider's rate-limit page is re-opened and the caps compared with `docs/PINS.md`. A
     lowered daily cap changes every hub's §6 that follows.
   - Anything this plan pinned in §5 is re-read at its source. Moved? Amend first (Principle 8).
6. Every deviation is recorded: an ADR for anything structural, `docs/CHANGELOG_PLAN.md` for plan
   text. A deviation that is written down is a decision; one that is not is a defect.

**Never** skip a day, merge two days, or reorder days without an ADR.

> A gate is never passed because time ran out (Principle 11). `python granth.py done N` is gated on a
> ticked checklist, a ledger row and green checks, and on nothing else.

---

## 10 · Ledgers and traceability

All ledgers live in `docs/`.

| File | Nature | The rule |
| --- | --- | --- |
| `docs/PROGRESS.md` | append-only | One row per completed day. **The last row is where we actually are.** |
| `docs/PINS.md` | append-only | Every version, tool or limit this project depends on: what, which value, the date observed, the day that added it, why. No invented values (Principle 6). |
| `docs/SOURCES.md` | append-only | Every source a document teaches or cites: exact title, identifier, year, URL, the date the record was checked, and which documents cite it. |
| `docs/GLOSSARY.md` | append-only | Every term, defined once, with the part that introduced it. This is what stops day 66 redefining a day 3 word slightly differently. |
| `docs/PROVENANCE.md` | append-only | Every third-party thing this project runs or vendors: source, licence, version, who audited it and when, and what it is permitted to touch — recorded **before** it first runs (Principle 12). |
| `docs/CHANGELOG_PLAN.md` | append-only | Every amendment to this plan (Principle 8). Newest last. |
| `docs/adr/` | append-only | One file per structural decision, numbered, never rewritten. Superseded, not deleted. |
| `docs/TRACEABILITY.md` | **generated** | Every ID, its planned day, whether it is closed. |
| `docs/CURRICULUM_INDEX.md` | **generated** | The reverse lookup: where do I learn `XX-14`? |
| `docs/TRACKER.md` | **generated** | What is written, how thick each day is, what is pending. |
| `docs/WIKI.md` + `docs/wiki/` | **generated** | One row per day, one page per day, plus the entity index. |

**Four are written by hand and five are generated — do not confuse them.** Editing a generated
file only means the next `python granth.py index` silently overwrites you. The generated files are an
index *over* the days; every line in them is copied from a day document, and nothing in them is
written by a model. **If an index ever disagrees with the day it indexes, the day is right and the
index is stale** — regenerate it.

The append-only ledgers are written by the day you are finishing. Every hub ends with the exact
rows to paste (§11.5, section 11).

---

## 11 · The depth contract — how a day is written

> **Read this section in full before writing a single line of any day.** It carries the judgement
> no checker can make for you: the one-idea test, the standalone test, and whether a story is one
> the reader has plausibly lived.

### 11.1 The three commitments

Everything below follows from three sentences.

**One idea per document.** A subtopic that cannot be read alone, understood without scrolling past
a different subtopic, and explained back out loud is not one subtopic — it is several, badly
stacked. If a document needs the word "also" to introduce its second half, it is two documents.

**No clocks.** Nothing in a day folder carries a time estimate, a duration, an "estimated hours"
field or a pace. A reader may spend five sittings on one part. An explanation is **never** trimmed
because a day is getting long; the day gets another part instead.

**Zero to production, in one document.** Each part opens where a reader who has never heard of the
idea can stand, and ends where a professional stands: the real-system version, what breaks at
scale or under pressure, what a senior reviewer says, what an interviewer probes.

### 11.2 The folder shape

```text
days/day-NN-<day-slug>/
├── LESSON.md      # the hub: story · part map · setup · build brief · check · budget · ledger
├── CHECKLIST.md   # the definition of done; `python granth.py done N` refuses until it is ticked
├── parts/         # THE TEACHING — one document per subtopic, numbered <section>.<subtopic>
│   ├── 01-<slug>/
│   │   ├── 1.1-<slug>.md
│   │   └── 1.2-<slug>.md
│   └── 02-<slug>/
│       └── 2.1-<slug>.md
├── sources/       # one document per primary source the day's ideas came from (§11.4.2)
│   └── 01-<source-slug>.md
└── lab/           # the learner's own work
```

**Line by line:**

- `days/day-NN-<day-slug>/` — the number zero-padded, then a kebab-case slug of **1–4 words** taken
  from the hub's `title` with articles dropped. A number alone is an address, not an answer, and
  137 of them are indistinguishable in a file tree, a tab strip or a `git log --stat`.
- `LESSON.md` — the hub. It orients and assembles; **it never teaches** (§11.5).
- `CHECKLIST.md` — the definition of done. Without it a day has no way to be finished.
- `parts/` — **mandatory**. A day without it is not written, and a phase containing such a day
  cannot be green.
- `parts/01-<slug>/` — a section folder: two digits, then a kebab-case slug of **1–3 words** taken
  from the section's heading in the hub's map. A bare `parts/01/` is rejected by the checker.
- `sources/` — beside `parts/`, never inside it. Present only on days whose ideas come from a
  citable primary document.
- `lab/` — the learner's own work. Usually gitignored; the teaching is in `parts/`, not here.

**The number is the identity; the slug is a label on it.** Every tool resolves a day by number and
accepts any slug, so a folder can be renamed to a better slug at any time with a `git mv` and
nothing downstream notices. Part *filenames* never change — they already carry a full slug, and
renaming them would break every cross-part link for no gain.

### 11.3 The numbering rule — what `1.1` and `2.3` mean

A part filename is `<section>.<subtopic>-<kebab-slug>.md`.

- The **section** number groups subtopics that share **one mental model** — usually one curriculum
  ID, one stage of a pipeline, or one phase of a mechanism. The hub's map states what each section
  means. An unexplained grouping is a bug.
- The **subtopic** number is reading order inside that section.
- Sections run `1..N` with no gaps, and so do the subtopics inside each section. A gap means a
  document was deleted or never written, and nothing else in the repository would say so.
- The section folder's number and the number before the dot must agree.
- **Every part lives in its section's folder.** Never loose in `parts/`.
- **Links between parts are relative to the part's own folder**: a sibling is `1.2-<slug>.md`,
  another section is `../01-<slug>/1.5-<slug>.md`, the hub is `../../LESSON.md`. From a source
  document one level up: a part is `../parts/01-<slug>/1.1-<slug>.md`, the hub is `../LESSON.md`.

### 11.4 What a part document must contain

Eleven sections, **in this order**. Three are conditional — each is required exactly when its
trigger is present, and never asked for otherwise.

| # | Section | Required | What it is |
| --- | --- | --- | --- |
| 0 | **frontmatter** | always | `day`, `part`, `title`, `ids`, `level`, `prerequisites`, `prev`, `next`. Optionally `sources`, and `failure: true` on the day's deliberate-failure part. **No duration field of any kind.** |
| 1 | **One-line answer** | always | The claim in one sentence, before anything else. A reader who stops here has still learned something true. |
| 2 | **The story** | always | A concrete scene first: a person, a machine, a failure, a decision. **No jargon at all.** Four rules — see §12.2. |
| 3 | **The idea in plain language** | always | The concept assuming zero prior knowledge; every term defined on first use, *including terms from earlier days*, with a link to the part that introduced them. No code. |
| 4 | **Why Prahari needs it** | always | The concrete later day that breaks without this. Never "this is important". |
| 5 | **The source behind it** | when `sources:` is declared | An **address, not an explanation**: the citation block (exact title · identifier · year · URL, **no authors**), **one sentence** of the claim, and a **link to the source document that teaches it**. Nothing more. |
| 6 | **The mechanism** | always | How it actually works: runnable code, the exchange written out, or the diagram. Nothing skipped as "obvious". |
| 7 | **Line by line** | when the part carries code | A `**Line by line:**` list **immediately after each code block**: every non-obvious token, and *why that line and not another*. |
| 8 | **The source in one demo** | source documents only | The source made runnable and stripped to nothing but itself. See §11.4.2. |
| 9 | **When it breaks** | always | The **real** error text, verbatim — the traceback, the status code, the message body — never a paraphrase. What it means, and the smallest fix. |
| 10 | **In production** | always | The real-system version: what a professional writes instead of the teaching version, what degrades at scale or under pressure, the failure that only shows with real traffic, the review comment, the interview question. **Not optional.** |
| 11 | **Check yourself** | always | One thing to run now, one question to answer out loud. |

**Section 10 is the one that gets dropped, and dropping it halves the document.** A part that
shows the idea working on one small case and never says what happens at ten thousand has taught
half the subject.

#### 11.4.1 Five additional rules on every part

1. **Name what you checked.** The documentation page, the specification revision, the record — with
   the date. "Verified" without an address is not verified.
2. **State the version, or leave the lookup command.** Never a remembered number (Principle 6).
3. **Respect the constraints in §4** in every command a reader is told to run.
4. **Name the trap.** If the part touches a known breaking change, a deprecated form or a common
   wrong turn, say so where the reader would otherwise take it.
5. **Never invent a citation.** Look the record up live, copy the title from the record and not
   from memory, and add a dated row to `docs/SOURCES.md`. Cite by **title and identifier, never by
   author** (§12.5).

#### 11.4.2 Source documents — one per primary source

When a day's ideas come from public primary documents — a research paper, a numbered specification
revision, a standard, a formal technical report — the day gets **one document per source**, in
`days/day-NN-<slug>/sources/`, **beside `parts/` and not inside it**, named `NN-<source-slug>.md`
and numbered from `01` in reading order.

A source document is written to the same eleven-section contract as any other part, with a part's
frontmatter **minus `part`** — it is not a subtopic of anything — and **plus `source:`
(singular)**, the one identifier it teaches. Its `level` is almost always `production`. On a source
document the sections mean:

- **The story** — the problem the field had *before this document existed*. A scene, plain words,
  no jargon, no equations. Someone was stuck; this is what stuck looked like.
- **The idea in plain language** — the claim, stated so a reader who has never opened a document
  like this can hold it and repeat it. Define the terms the title itself uses.
- **The mechanism** — the method itself, written out at the depth the rest of the day is written
  at. **Not the abstract, paraphrased.**
- **When it breaks** — where the claim does **not** hold: what it assumed, what it was measured
  on, the scale it was never tried at, the follow-up that narrowed it. A source document with no
  limits section has taught a press release.
- **In production** — **what survived and what did not**: which half of this document is in
  shipped systems today, which half the field quietly dropped, and what replaced it. This is the
  section that makes a source document worth reading rather than citing.
- **The source in one demo** — the source made runnable and stripped to nothing but itself. Four
  rules, and the third is the one that makes it honest:
  1. **Only this source's contribution.** Not a small project that uses the idea — a small project
     whose entire reason to exist *is* the idea. Subtractive test: if a file could be deleted and
     the claim still lands, delete it. Two or three files is normal.
  2. **End to end and actually runnable.** The whole file tree, every file's contents, the one
     command, and its **real pasted output**. If you have not run it, leave the output block as a
     `TODO(<the exact command>)` — **never an invented transcript**. Principle 7 outranks the
     document's shape: a missing output is fixed by one run; a fabricated one is undetectable.
  3. **An ablation switch** — one flag that turns the contribution **off**, with **both runs'
     output shown**. A demo that cannot be switched off has proved that code ran, not that this
     idea mattered. It is also a check that can go RED (Principle 9).
  4. **Inside the constraints of §4**, like everything else.

  It lands in `lab/sources/<source-slug>/` and is given **complete**. It is teaching material, not
  an exercise: the unsolved `TODO(me)` exercises stay in the hub's build brief.

**Read source documents after the parts.** The hub's map says so and the last part's *Next* points
at them. That order is Principle 3 at the scale of a day: build the mechanism by hand, *then* read
the proposal, so "what survived and what did not" lands on something the reader has built rather
than on nothing.

**A source is taught once in the whole curriculum.** The day that first needs it carries the
document; every later day cites it and links back. Two documents declaring the same identifier is
a checker failure, not a style preference.

### 11.5 What the hub (`LESSON.md`) must contain

The hub orients and assembles. **It never teaches** — no walkthrough lives here.

| # | Section | What it carries |
| --- | --- | --- |
| 0 | frontmatter | `day`, `phase`, `title`, `ids`, `kind`, `plan_version`, `parts`, `generated`, `status`, and whatever else the project tracks. No duration field. |
| 0 | blockquote | Yesterday / today / tomorrow, in three lines. No time estimate. |
| §1 | **Where we are** | A scene and an analogy. Plain language, no code, no jargon. |
| §2 | **The map** | A table of every part: number, linked title, what it answers, `level` — grouped by section, with one line saying what each *section* means. **No minutes column, ever.** If the day has `sources/`, the map ends with a table of those, marked read-after-the-parts. |
| §3 | **Setup** | Every command the day needs, pinned and runnable. |
| §4 | **Build brief** | What to make, with `TODO(me)` markers left **unsolved**. |
| §5 | **The check that must be able to fail** | The check that is RED before the build brief is done and GREEN after. State how to make it go red on purpose. |
| §6 | **Budget** | What the day spends against the §4 constraints. `0` is an answer; state it. |
| §7 | **Traps** | The mistakes that eat an evening, including any named breaking change. |
| §8 | **Verify before you build** | The live URLs actually fetched today, with what each confirmed. |
| §9 | **Say it out loud** | One paragraph, spoken voice — the answer you would give an interviewer. |
| §10 | **Done when** | A pointer to `CHECKLIST.md`. Defined by understanding and green checks, never by elapsed effort. |
| §11 | **Ledger & commit** | The verbatim `PROGRESS.md` row, any `PINS.md` / `SOURCES.md` / `GLOSSARY.md` / `PROVENANCE.md` rows, and the commit message. **The hub ends here.** |

The ritual in §11 is the point: the repository is the memory, and a memory that depends on
remembering to write it down is not one.

### 11.6 The `level` field — how a day climbs

Every part declares one:

| Level | The reader afterwards |
| --- | --- |
| `foundation` | knows what the thing is and can recognise it |
| `working` | can use it on their own problem, unaided |
| `production` | knows what changes in a real system, and what breaks |

**A day climbs.** A day that is all `foundation` is a tutorial. A day that opens at `production`
has skipped the reader.

### 11.7 How finely to split

Split by **idea boundary, never by length or pace**. There is no target part count: four parts if
the subject needs four, twenty-two if it needs twenty-two.

Three tests, applied *before* writing:

- **The one-idea test.** If the part needs "also" to introduce its second half, it is two parts.
- **The standalone test.** A part must be readable cold. Name and link its prerequisite part.
- **The no-shortcut test.** "For now, just accept that" is banned unless it links forward to the
  part that explains it. A deferred explanation must have an address.

Useful default shapes:

| Day kind | Split by |
| --- | --- |
| setup | one part per tool or file |
| mechanism | mechanism → behaviour → edge case → failure mode → production use |
| concept | one claim per part |
| gate | one acceptance criterion per part |

**Every day carries at least one part whose subject is a deliberate failure** — break it on
purpose, read the real error, fix it. That part declares `failure: true` in its frontmatter, and
is usually `level: production`.

### 11.8 What "in depth" is not

The eight failure modes this format exists to prevent. If a part shows one, it is not done.

1. **Splitting without deepening** — the same wall of text, now in six files.
2. **Summary in place of explanation** — a description of the mechanism instead of the mechanism.
3. **Stopping at the toy example** — no `In production`, so the reader learned a demo.
4. **Assuming the previous day** — an undefined term from day 12 used on day 51.
5. **Code without failure** — a happy path with no real error text anywhere.
6. **Trimming to fit** — an explanation cut because the day was getting long. Add a part instead.
7. **Solved exercises** — the `TODO(me)` reps done for the reader, who then does none.
8. **A carried-over clock** — a duration field copied from an older draft.

### 11.9 Enforcement

Run `python granth.py depth N` after writing a day. It fails on: a missing or misordered section, a
numbering gap, a bare numeric folder, a part loose in `parts/`, a code block with no walkthrough,
a malformed or unledgered citation, a source taught twice, a smuggled-in clock, a missing
deliberate-failure part, a hub that carries teaching, and a hub whose IDs disagree with §8.

**Never hand-wave past a `depth` failure.** The checker only knows the things a script can know;
everything it cannot check — whether the story is lived, whether the explanation is any good,
whether `In production` is true — is checked by reading, and a repository that argues with its
own checker will not survive the reading either.

---

## 12 · The style guide

### 12.1 The register

**Storytelling is the default.** A scene before an abstraction, every time. The reader is learning
this in order to do real work, so no idea stops at the toy example.

**Simple language first.** Plain words → a concrete example → *only then* the terminology. If a
twelve-year-old could not follow the first sentence, rewrite the first sentence.

**Define every term on first use, including terms from earlier days**, with a link back to the
part that introduced them, and a row in `docs/GLOSSARY.md`. 137 days is long enough
that day 3 is forgotten by day 66.

**Grammar and punctuation are part of the deliverable**, in every section of every document.
Correct full stops and commas, no run-on sentences, and no long chain of dashes where two ordinary
sentences would read better. A sentence the reader has to parse twice has failed.

### 12.2 The story rules

The story is the hook the definition hangs on, not decoration. Four rules, and the first is the
one that gets broken:

1. **A scene the reader has plausibly lived.** A parcel and a courier. A repair-shop job card. A
   bus route map. A used car checked by a mechanic. A monthly generator test. A tailor taking
   measurements. **Not** a nautical chart, a model railway, a theatre programme, a projection
   booth or a mediaeval siege. Test: *could the reader have been standing in this scene
   themselves?* If they must first be told what the setting **is**, the analogy is carrying the
   explanation instead of hooking it.
2. **Simple words.** Short sentences beat clever ones here.
3. **Realistic and load-bearing.** The scene must contain the actual failure or decision the part
   teaches, not a pretty image the part then abandons. Every later section that reaches back for
   the metaphor must still fit it.
4. **One metaphor family per day.** Before choosing, grep the day's other parts and the hub's §1.
   Two parts reaching for the same family — two restaurants, two receptionists — read as one idea
   repeated.

### 12.3 The scene format

For failures and motivations, four beats:

> **The scene** — what someone was doing.
> **The naive fix** — what they reached for first, and why it was reasonable.
> **Why it fails** — the real failure, with the real message.
> **The insight** — the thing that actually solves it.

### 12.4 Code and commands

- **Every code block is followed by a `**Line by line:**` walkthrough** of each non-obvious token,
  and why it is that line and not another. An unexplained line is a bug in the document.
- **Every mechanism has a matching "When it breaks"** with the **real error text, verbatim**.
- **Commands are runnable as written**, in the shell this project actually uses.
- **Diagrams whenever the concept is spatial, sequential or a state machine** — a lifecycle, a
  handshake, a retry ladder, an approval gate.
- **Tables for enumerable facts, prose for reasoning.** Never a table of one row.
- **Leave `TODO(me)` exercises unsolved.** Teach; do not do the reps for the reader.

### 12.5 Facts

- Never invent a version, an interface, a limit or a citation (Principle 6).
- **Cite by title and identifier, never by author** — `arXiv:1706.03762`, `doi:10.1145/…`,
  `RFC 9110`. The identifier is the stricter attribution anyway: it resolves to exactly one
  document, and it is what a reader types.
- An unrun command's output is a `TODO` naming the exact command. **Never a plausible transcript.**

### 12.6 The two things that are never written

1. **No clocks.** No duration, no "estimated hours", no "this should take about", no pace —
   anywhere, in any document, in any field (Principle 11).
2. **No person names, no course or creator brand names.** This curriculum is self-contained and
   promotes nobody: never name an instructor, author, channel, academy, bootcamp or training
   company — in a lesson, a checklist, a docstring or a commit message. Naming the **tools** you
   actually use is required and unaffected, as is citing a specification by its revision and a
   work by its exact title and identifier.

### 12.7 The ritual

Every day ends the same way: paste the ledger rows, tick the checklist, run the gate, commit. Not
because ritual is virtuous, but because a repository that records itself is a repository you can
return to after three weeks away and still trust.

---

## 13 · Amendment record

This plan is amended, never quietly edited. Every amendment lands in `docs/CHANGELOG_PLAN.md`
before any day or any code changes, and anything structural gets an ADR in `docs/adr/`.

| Version | Date | What changed |
| --- | --- | --- |
| v1.0.0 | 2026-09-18 | Plan adopted. See `docs/adr/ADR-0001-the-plan-as-adopted.md`. |
