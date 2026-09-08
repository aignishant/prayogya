---
plan: prayoga
version: "v3.1.0"
topic: "40 independent agentic systems with Google ADK 2.x, MCP, Agent Skills and A2A"
tracks: 10
ids: 310
days: 297
phases: 42
doc_architecture: "hub + parts/ (see §4 and §5)"
amended: "2026-09-08"
---

| plan | prayoga |
| --- | --- |
| version | v3.1.0 |
| supersedes | v3.0.0 (same curriculum, no machine-readable blocks) |
| projects | 40 · **each one a standalone repository** |
| days | 296 project sittings + day 0, the authoring repo = **297** |
| sitting budget | 60 minutes |
| rule 1 | **every project carries tools + MCP + multi-agent** |
| rule 2 | **every project is complete alone. No shared code. Nothing imported from another project.** |
| doc architecture | 5 project docs + hub + RECALL + parts/ |

# MASTER PLAN v3.0.0 — **Prayoga**

## 40 independent agentic systems with **Google ADK 2.x · MCP · Agent Skills · A2A**

---

## §0 · What v3.0.0 changed, and why v2 was wrong

v2 put the common code in `_shared/adk_kit/` and had later projects import it. That made the plan
cheap to write and **made every project after P03 unbuildable on its own.** A reader who takes
only `projects/22-writer-and-critic/` to a different machine gets `ModuleNotFoundError:
adk_kit`. The day document said `from adk_kit.cast import Orchestrator` — which is not real code
for that project, it is a pointer to a file the reader does not have.

**v3 deletes `_shared/` entirely.** Four people can take four different project folders to four
different machines and each build a complete, running system with nothing else.

That costs duplication, and the duplication is paid for deliberately. Three rules keep the cost
where it belongs:

> ### 1. The Completeness Rule — code is never referenced, only printed
> Every line of code a project needs appears **in full, at its real path, inside that project's
> own day documents**. No import from another project. No "copy this from P03". No `...` and no
> "the rest is unchanged" unless the unchanged region was printed earlier **in this same project**
> and the day says which day printed it. If a file exists in the finished project, some day in
> that project printed it whole.

> ### 2. The Depth Rule — explanation is written once
> Deep teaching of a concept lives in exactly one place in the whole plan. A later project prints
> the same code in full, explains it at **recap depth** — a short table, one line per function,
> plus the failure it prevents — and gives the pointer to the deep version.

> ### 3. The Primer — the bridge that keeps rule 2 from breaking rule 1
> A pointer to another project is useless to someone who only has this one. So **every project
> carries its own `PRIMER.md`**: one page, written inside the project, that gives a self-contained
> working understanding of every borrowed concept. The pointer is for depth. The primer is for
> sufficiency.

The test that decides whether a project is finished: **`./p verify P` copies only that project's
folder into a clean container, follows its own `SETUP.md`, builds it day by day from its own
documents, and runs its own checks.** A project that fails this is not written, however good its
prose is.

---

## §1 · What a project folder contains

A project is a repository. It is complete on its own, it has its own git history if you want one,
and it has no parent.

```
projects/18-archive-finder/            ← take this folder anywhere; it runs
│
├── README.md              # a stranger's entry point: what it is, how to run it, what it needs
├── PROJECT.md             # the brief + the triad block (§2.2)
├── PRIMER.md              # every borrowed concept, self-contained, one page (§2.3)
├── SETUP.md               # complete toolchain + skeleton, copy-pasteable (§2.4)
├── CODEMAP.md             # every file in the finished project → the day that prints it (§2.5)
│
├── day-01-the-kit/        # THE TEACHING
│   ├── LESSON.md · RECALL.md · CHECKLIST.md
│   ├── parts/01-<slug>/1.1-<slug>.md …
│   └── lab/
├── day-02-the-boundary/
├── … day-09-ship/
│
├── run                    # this project's own driver: ./run check | serve | eval | up
├── pyproject.toml         # its own pins. Not shared, not inherited.
├── uv.lock · .python-version
├── .env.example · .gitignore
├── Dockerfile · compose.yaml          # its own deploy files (k8s/ from tier D4)
│
├── archive_desk/          # the agents, tools, cast — every line typed from the day docs
│   ├── agents/ · tools/ · util/       #   util/ holds THIS project's backoff, budget, logging
│   └── main.py
├── archive_mcp/           # this project's own MCP server. Not a library. Its own code.
└── tests/ · evals/
```

**There is no `_shared/`, no `adk_kit`, no parent `pyproject.toml`, and no root driver that a
project depends on to run.** The top-level `./p` still exists, but it is an **authoring tool only**
(§6): it writes, checks and verifies the documents. Nothing in a project imports it or needs it.

`archive_desk/util/backoff.py` is the same idea as `field_desk/util/backoff.py`, and they are
separate files with separate lives. If you improve one later, the other does not change. That is
the price of independence and it is the correct price.

---

## §2 · The five project documents

### 2.1 `README.md` — the stranger's entry point

Written for someone who has this folder and nothing else. Six sections: what this system does ·
what you need installed · the four commands to run it · the architecture in one Mermaid diagram ·
where the teaching is (`day-01/LESSON.md`) · what is deliberately not built 🅿️.

### 2.2 `PROJECT.md` — the brief and the triad block

```markdown
# P18 · Archive Finder
**What it is.** A support desk that answers "has anything like this come in before?" over a
synthetic ticket archive, at $0, with a retrieval eval that goes red when chunking is disabled.
**Days.** 9 · **Deploy tier.** D3 (compose, MCP sidecar) · **Depends on nothing.**

## Triad
| Leg | This project |
| --- | --- |
| **Tools** | `search_archive(query, k)` · `fetch_ticket(id)` · `summarise_thread(id)` |
| **MCP boundary** | `archive_mcp/` — owns the index and the ticket store; no agent touches a file |
| **Cast** | `router` → `retriever` ‖ `scout` → `writer` → `critic` |

## Borrowed concepts — taught deeply elsewhere, recapped here
| Concept | Recap in | Deep version (optional reading) |
| --- | --- | --- |
| Stateless MCP core | `PRIMER.md` §1 | `projects/02-parts-counter/day-03-…/parts/01-…/1.2-stateless.md` |
| Delegation & handback | `PRIMER.md` §2 | `projects/03-triage-room/day-05-…/parts/01-…/1.2-transfer.md` |
| Honest 429 backoff | `PRIMER.md` §3 | `projects/05-bench-runner/day-04-…/parts/02-…/2.1-retry-after.md` |

**New here:** embeddings · chunking · top-k · citations · `recall@k` as a failing test
**Done when.** A cold run finds three known duplicates of five, misses two honestly and says so,
and `recall@5` fails when the chunker is disabled.
```

The **Borrowed concepts** table is the honest statement of what this project recaps rather than
teaches. The deep column is optional reading; the primer column is not.

### 2.3 `PRIMER.md` — one page, self-contained

One section per borrowed concept. Each section is **six to ten lines**: what the idea is in plain
words, the one failure it prevents, and how it shows up in this project's code. No code blocks —
the code is in the days. This is what makes a pointer safe.

```markdown
## §3 Honest 429 backoff
Free model APIs return HTTP 429 when you have used your allowance for the minute or the day.
The response usually carries a `Retry-After` header saying how long to wait. An agent that
retries immediately makes it worse; an agent that catches the error and returns "I couldn't find
anything" has lied to its user about why.
So: read `Retry-After` if present, otherwise wait 1s, 2s, 4s, 8s, and after four attempts stop
and surface the failure upward. Never substitute an answer for an error.
In this project: `archive_desk/util/backoff.py`, printed in full on day 01, wrapped around every
model call and every `archive_mcp` call.
Deeper: `projects/05-bench-runner/day-04-honest-429/parts/02-the-ladder/2.1-retry-after.md`
```

### 2.4 `SETUP.md` — complete and copy-pasteable

Every command from a bare machine to a green check: install `uv`, pin Python, `uv init`, the exact
`uv add pkg==version` lines with the date each was verified, `cp .env.example .env`, which free
keys are needed and where to get them, `./run check`. **No step is "as in the foundry project".**
Roughly 40 lines, mostly commands. It is a listing, not a lesson — day 01 explains the parts that
matter, and `projects/00-foundry/` holds the deep version for anyone who wants it.

### 2.5 `CODEMAP.md` — the completeness proof

Generated by `./p index P`. Every file in the finished project, and the day and part that prints
it whole.

```
archive_desk/util/backoff.py        day-01-the-kit/parts/03-resilience/3.1-backoff.md
archive_mcp/server.py               day-02-the-boundary/parts/01-server/1.2-server.md
archive_mcp/index.py                day-04-the-index/parts/02-building/2.2-index.md
archive_desk/agents/critic.py       day-08-the-critic/parts/01-rubric/1.3-critic.md
```

**A file with no day is a bug that fails `./p check`.** This one table is what makes rule 1
mechanical instead of aspirational.

---

## §3 · What a day is

**One sitting of about sixty minutes:**

| Slice | Minutes | What |
| --- | --- | --- |
| Read | 25–30 | 2–4 parts, one idea each |
| Build | 20–25 | type the code the parts printed; `TODO(me)` markers stay unsolved |
| Break it | 5 | the day's deliberate failure; watch the check go red |
| Close | 5 | tick the checklist, write `RECALL.md`, commit |

A subject that will not fit in sixty minutes becomes two days. It is never compressed.
Every day has at least one deliberate failure; a day whose check never went red is not finished.

### 3.1 The two standard front days

Because there is no shared code, every project starts by building its own foundation. From P04
onward these two days are the same **shape** every time, and they are cheap because they are
listing-plus-recap, not teaching:

**Day 01 — The kit.** Prints, in full: `pyproject.toml`, `.env.example`, `.gitignore`, `run`,
`<project>/util/models.py` (pinned model registry), `util/backoff.py`, `util/logging.py`,
`util/budget.py`, `evals/harness.py`. Each gets a recap table and a pointer. Ends with `./run check`
green on an empty system.

**Day 02 — The boundary.** Prints, in full, this project's own MCP server: `<project>_mcp/server.py`,
its tools, its transport, and the client wiring in `<project>/util/mcp.py`. Recap depth, pointer to
P02 for the deep protocol teaching. Ends with the agent calling one tool across the boundary.

By day 03 the project has a running triad and the rest of the days are its actual subject.
P01, P02 and P03 are the exception — they are where these two days are taught *deeply*, once.

---

## §4 · The three documents in a day

### 4.1 `LESSON.md` — the hub

| § | Section | Contains |
| --- | --- | --- |
| fm | frontmatter | `project`, `day`, `title`, `ids`, `parts`, `deploy_tier`, `sitting_minutes: 60`, `files_printed`, `status`, `commit` |
| — | yesterday / today / tomorrow | one line each |
| §1 | *(project-named)* | the day's whole idea as one scene, plain words, no jargon |
| §2 | The map | every part: number, linked title, what it answers, `level` |
| §3 | Setup — run this | every `mkdir`, `touch`, `uv add pkg==exact`, verified that day |
| §4 | Files this day prints | the paths, and which part prints each. Feeds `CODEMAP.md` |
| §5 | Build brief | what you type; `TODO(me)` unsolved |
| §6 | The check that must be able to fail | RED before the TODOs are done |
| §7 | Request budget | per-turn model calls per provider, RPM/RPD, **counted across the whole cast** |
| §8 | Traps | the mistakes that eat the hour, incl. the named 1.x→2.x trap |
| §9 | Verified today | live doc URLs actually fetched |
| §10 | Ledger & commit | the `PROGRESS.md` row, `PACKAGES.md` rows, the commit message |

### 4.2 `RECALL.md` — one page, written last

One line summary · what I built · three things worth remembering · the failure I caused, with the
real error string · the command that proves it still works · the interview paragraph · what it
depends on. Never longer than a screen. `./p recall P` prints a whole project's set in order.

### 4.3 `CHECKLIST.md`

The definition of done. `./run done` refuses until every box is ticked and checks are green.

---

## §5 · The part contract — 8 sections

| # | Section | The rule |
| --- | --- | --- |
| 1 | **frontmatter** | `project`, `day`, `part`, `title`, `ids`, `level`, `prints` (file paths), `prev`, `next` |
| 2 | **One-line answer** | The claim in one sentence. |
| 3 | **The idea** | *(story + plain language, merged.)* A concrete scene you could have stood in — a courier, a job card, a spare key with a neighbour. **No jargon in the first paragraph.** Then the concept, terms defined on first use, the scene still holding the failure the part teaches. **No code.** One metaphor family per day. |
| 4 | **The mechanism** | **Real code from this project.** See §5.1 — this is the section your question was about. |
| 5 | **Line by line** | *Conditional* — when there is code. Full depth for code taught here; recap depth for code borrowed (§5.2). |
| 6 | **When it breaks** | Short and story-shaped. The real error text verbatim, then plain words: someone shipped this on a Friday, here is what they saw at 11pm, here is the smallest fix. Two to four sentences. |
| 7 | **In production** | Short and story-shaped. Four beats: what a senior writes **instead** · what degrades at scale, with a number · the review comment · the interview question. One real example. Not optional. |
| 8 | **Check yourself** | One command to run now, plus one question answered **out loud**. |

### 5.1 The mechanism section — the rule, stated hard

**Yes, it is real code, and these five constraints make that mean something:**

1. **Real path, real project.** The block is headed with the file's actual path in *this* project — `archive_mcp/server.py`, not `server.py` and never `# in your MCP server`.
2. **Whole file, or a marked diff against a version this project already printed.** `# ── unchanged from day-02 part 1.2 ──` is legal. `# ... rest of implementation ...` is not.
3. **No import from outside this project.** If it needs a helper, this project printed the helper.
4. **Runnable as printed.** Imports at the top, no invented API, verified against adk.dev on the day. If it needs a key, the `.env.example` line is in the same day.
5. **The output is real.** The block showing what it prints was actually run. If it could not be run, the block is `TODO(me): run <exact command>` — never an invented transcript. A missing output is fixed by one run; a fabricated one is undetectable.

**Worked example** — P18 day 02, part 1.2, at recap depth because P02 taught this deeply:

````markdown
### The mechanism

`archive_mcp/server.py` — this project's data boundary, whole file:

```python
# archive_mcp/server.py
import os
from mcp.server.fastmcp import FastMCP
from archive_mcp.store import TicketStore

mcp = FastMCP("archive-mcp", stateless_http=True)
store = TicketStore(os.environ["ARCHIVE_DB"])

@mcp.tool()
def fetch_ticket(ticket_id: str) -> dict:
    """Return one ticket by id, or raise if it does not exist."""
    return store.get(ticket_id).as_dict()

@mcp.tool()
def search_archive(query: str, k: int = 5) -> list[dict]:
    """Return the k most similar past tickets. Empty list is a valid answer."""
    return [hit.as_dict() for hit in store.search(query, k=k)]

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
```
*Verified against `adk.dev/docs/mcp/servers` and the MCP 2026-07-28 revision on 2026-09-08.*

**Line by line — recap depth.** The stateless server pattern is taught in full at
`projects/02-parts-counter/day-03-the-server/parts/01-skeleton/1.2-server.md`; `PRIMER.md` §1 has
the self-contained version. What matters here:

| Line | What it does, and the failure it prevents |
| --- | --- |
| `stateless_http=True` | Every request carries everything it needs. Without it, a second replica cannot answer a call the first one started. |
| `store = TicketStore(...)` at module level | One connection per process, not per request. Per-request opens exhaust the pool at about 40 concurrent calls. |
| `k: int = 5` typed with a default | The type hint *is* the schema the agent sees. Untyped, the model passes `"5"` and the store raises. |
| `Empty list is a valid answer` in the docstring | The docstring is the tool description. Without this line the retriever agent invents a ticket rather than return nothing. |

**New here, so explained in full below:** `store.search`'s ranking — part 1.3.
````

### 5.2 The two depths of `Line by line`

| Depth | When | Shape |
| --- | --- | --- |
| **Full** | the code is taught here for the first time in the plan | every non-obvious token, and *why that line and not another*, as prose bullets under the block |
| **Recap** | the code is borrowed — printed whole, taught elsewhere | a table: one row per line that carries a decision, each stating **the failure it prevents**, then the `PRIMER.md` section and the deep pointer |

`./p depth` fails a part that gives **full** depth to a concept another part already owns — that is
the duplication rule — and fails a part that gives **recap** depth to a concept nothing owns.

### 5.3 The three unnumbered rules

- **One idea per document.** If the part needs "also" to introduce its second half, split it.
- **Standalone.** A borrowed idea gets its primer section and its pointer, never "as we saw".
- **No shortcut.** "For now, just accept that" is banned unless it links forward to the part that explains it.

**Levels:** `foundation` → `working` → `production`. A day climbs.

---

## §6 · The pointer format, and where pointers may go

A pointer is **always a pair**: the in-project primer section, then the out-of-project deep
document. The primer half is mandatory; that is what keeps the project independent.

```markdown
> **Recap — stateless MCP core.** Every request carries its own context, so any replica can
> answer it. Self-contained version: `PRIMER.md` §1.
> Deep version, if you have the full plan:
> `projects/02-parts-counter/day-03-the-server/parts/01-skeleton/1.2-stateless.md`
```

**A pointer may never stand alone**, and it may never be the only explanation of something the
reader must type. `./p depth` fails a part that links out without a primer section behind it.

The global `docs/CONCEPTS.md` maps every concept to the **one** project that teaches it deeply.
It is an authoring index. No project needs it to be buildable.

---

## §7 · Verification — how independence is proved, not claimed

Two commands, and the second is the important one.

```
./p check P        # authoring: depth contract, CODEMAP completeness, no external imports,
                   # no pointer without a primer section, no clock outside sitting_minutes
./p verify P       # independence: clean container, copy ONLY projects/<name>/,
                   # follow its own SETUP.md, build from its own days, run its own ./run check
```

`./p verify` fails on:

- any `import` in the project's code resolving outside the project;
- a file in the finished tree that no day prints (`CODEMAP.md` gap);
- a `SETUP.md` step that references another project;
- a primer section missing for any concept in the `Borrowed concepts` table;
- `./run check` red.

**Every project's last day is the cold-clone day**: wipe the working copy, clone the folder alone,
follow the README, and record the output. That output is pasted into the day document. A project
whose cold clone was never run is not finished.

Inside a project, the driver is `./run` and it has no dependencies outside the project:

```
./run check     # ruff + format + tests + evals at current scope
./run serve     # the agent API on :8080
./run mcp       # the boundary server
./run up        # compose: agents + boundary together
./run eval      # the evalset
./run done N    # refuses unless day N's checklist is ticked and check is green, then commits
```

---

## §8 · Deploy — per project, no shared folder

Each project carries its own `Dockerfile`, `compose.yaml` and, from D4, its own `k8s/`. They are
printed in full in that project's ship day at recap depth, with the pointer to the project that
teaches the tier.

| Tier | What it is | Taught deeply in | Printed in full by |
| --- | --- | --- | --- |
| **D1** | `api_server` / FastAPI, `/healthz`, run locally | P01 | 01 |
| **D2** | Docker: stateless container, env-injected secrets, Cloud-Run-shaped | P02 | 02 |
| **D3** | compose with the **MCP sidecar**: agents and boundary as separate containers | P03 | 03–12, 14, 16–24, 34 |
| **D4** | kind/k3d: deployment, service, secret, CronJob, a pod killed mid-run | P13 | 13, 15, 25–33 |
| **D5** | eval-gated CI, cost and latency guards, blue/green with auto-rollback | P36 | 35–40 |

**The D5 test the capstone defends:** a prompt change must be blocked by the pipeline when it makes
the system worse, and must reach a live endpoint when it does not, without a human deciding which
of those two happened.

Cloud walkthroughs are **written and configured, never billed** — the config file is the
deliverable, marked 🅿️.

---

## §9 · Model & budget policy — $0, by construction

- **Gemini Flash-class** on a free AI Studio key, `GOOGLE_GENAI_USE_VERTEXAI=FALSE`, is the primary brain.
- **Groq** is the speed lane; **OpenRouter models ending in `:free`** are the breadth lane (the suffix is linted per project); **Ollama** is the offline baseline.
- **Every agent pins its model explicitly.** ADK 2.x's default is a preview model. With three agents that is three silent bugs.
- **Each project pins independently.** Its `PACKAGES.md` records package, version, the date verified, and the day. Two projects may legitimately sit on different pins; that is what independence means, and the freshness check (§10) is where the newer one wins.
- **Multi-agent multiplies quota.** A three-agent turn is at least three requests; a writer↔critic loop is unbounded until you bound it. Every hub's §7 states the per-turn count.
- **Every call path handles HTTP 429 honestly:** `Retry-After`, back off, escalate. Never fabricate a result to cover an error.
- **All data is synthetic, always.**

---

## §10 · Freshness — at the start of a project, not daily

Because projects are independent, the check moved to the front: you pin at the start and live with
it for six to nine sittings.

1. `google-adk` release notes since your last project — breaking change? Amend the day map first.
2. MCP spec revision moved? Every project has a boundary, so this one always matters.
3. Provider free lists re-checked; anything that lost its free tier is repinned before day 01.
4. Record the check in this project's `PACKAGES.md` with the date.

---

# §11 · The 40 projects

Eight tracks of five. Every project has all three legs, its own repo, and its own deploy files.
**From P04, day 01 is The kit and day 02 is The boundary** (§3.1) — the maps in §12 list days
from 03.

| # | Project | Days | Tier | Tools | MCP boundary | Cast |
| --- | --- | --- | --- | --- | --- | --- |
| 00 | **Foundry** *(reference only — no project depends on it)* | 3 | — | — | — | — |
| **A** | **The triad — taught deeply here, recapped everywhere after** | | | | | |
| 01 | Ask Desk | 7 | D1 | 3 function tools | *(leg 2 arrives P02)* | 1 agent |
| 02 | Parts Counter | 8 | D2 | 4 | `parts_mcp` | 1 agent |
| 03 | Triage Room | 8 | D3 | 4 | `desk_mcp` | router → classifier ‖ writer |
| 04 | Trip Ledger | 7 | D3 | 4 + meter | `desk_mcp` + meter | router → 2 specialists |
| 05 | Bench Runner | 7 | D3 | 4 | `bench_mcp` (fixtures) | same cast, 4 providers |
| **B** | **Tools & the data boundary** | | | | | |
| 06 | Field Inspector | 7 | D3 | long-running + artifact tools | `field_mcp` (photos, reports) | intake → inspector → reporter |
| 07 | Form Filler | 7 | D3 | schema-driven tools | `schema_mcp` + elicitation | intake → filler → validator |
| 08 | Shop Floor | 8 | D3 | 6, filtered per agent | `floor_mcp` + resources & prompts | supervisor → 3 line agents |
| 09 | Long Haul | 8 | D3 | submit / poll | `haul_mcp` + Tasks extension | dispatcher → worker → notifier |
| 10 | Gatekeeper | 7 | D3 | scoped tools | `vault_mcp` w/ OAuth2 + CIMD | requester → approver → auditor |
| **C** | **Skills & MCP in production** | | | | | |
| 11 | Skill Forge | 8 | D3 | tools + 2 own Skills | `forge_mcp` | author → runner → reviewer |
| 12 | Skill Auditor | 7 | D3 | audit tools | `registry_mcp` | fetcher → auditor → gatekeeper |
| 13 | Server Farm | 8 | D4 | unchanged | `farm_mcp` × 3 replicas | router → 2 workers |
| 14 | Peer Desk | 7 | D3 | tools | **your agent served as** an MCP server | host ↔ served agent ↔ critic |
| 15 | Audit Room | 7 | D4 | audit tools | its own + a fixture boundary | scanner → analyst → reporter |
| **D** | **Memory & retrieval** | | | | | |
| 16 | Recall Desk | 7 | D3 | memory tools | `memory_mcp` (DB sessions) | greeter → recaller → responder |
| 17 | Forget Me | 6 | D3 | retention tools | `memory_mcp` + redactor | classifier → redactor → keeper |
| 18 | Archive Finder | 9 | D3 | search / fetch / summarise | `archive_mcp` (index + store) | router → retriever ‖ scout → writer → critic |
| 19 | Second Opinion | 7 | D3 | search + retrieve | `archive_mcp` + `web_mcp` | router → 2 sources → adjudicator |
| 20 | Cache Keeper | 6 | D3 | cached tools | `archive_mcp` + cache layer | router → 2 specialists |
| **E** | **Workflows & multi-agent depth** | | | | | |
| 21 | Graph Runner | 8 | D3 | graph-node tools | `desk_mcp` | 5-node graph, 3 agents |
| 22 | Writer & Critic | 7 | D3 | draft / score tools | `style_mcp` (guides, examples) | writer ↔ critic + arbiter |
| 23 | Dispatch Yard | 7 | D3 | routing tools | `roster_mcp` (specialist registry) | dispatcher → N specialists |
| 24 | Plan Room | 8 | D3 | plan / execute tools | `plan_mcp` (plan store) | planner → executor → replanner |
| 25 | Swarm Limits | 7 | D4 | shared-state tools | `desk_mcp` under contention | 1 → 6 workers → reducer |
| **F** | **Durability, humans, safety** | | | | | |
| 26 | Never Lose Work | 8 | D4 | idempotent tools | `job_mcp` (checkpoints) | dispatcher → worker → resumer |
| 27 | Approval Gate | 7 | D4 | write tools behind a gate | `desk_mcp` (write ops) | proposer → human → executor |
| 28 | Injection Range | 9 | D4 | least-privilege tools | **hostile** `feed_mcp` | reader → guard → writer |
| 29 | Least Privilege | 6 | D4 | per-agent tool sets | `vault_mcp`, scoped creds | 3 agents, 3 permission sets |
| 30 | Sandbox Yard | 7 | D4 | code exec + browser | `range_mcp` (local dummy site) | planner → sandboxed executor → verifier |
| 31 | Quota Router | 6 | D4 | tools | `quota_mcp` (the ledger) | router → 3 provider-bound agents |
| **G** | **Ambient, live, evals** | | | | | |
| 32 | Night Shift | 6 | D4 | index / eval / digest | `archive_mcp` + `report_mcp` | scheduler → indexer → evaluator → digester |
| 33 | Watch Tower | 6 | D4 | webhook + dedup tools | `event_mcp` | intake → deduper → triager |
| 34 | Voice Standup | 8 | D3 | non-blocking tools | `queue_mcp` | voice → queue reader → summariser |
| 35 | Eval Bench | 8 | D5 | eval tools | `evalset_mcp` | runner → judge → scorer |
| 36 | Regression Gate | 7 | D5 | CI tools | `evalset_mcp` + `metrics_mcp` | gate → cost guard → latency guard |
| **H** | **Ops, deploy, interop, capstone** | | | | | |
| 37 | Glass Box | 7 | D5 | traced tools | its boundary, instrumented | full cast under one trace tree |
| 38 | Blue Green | 7 | D5 | health tools | `desk_mcp` × 2 colours | full cast × 2 deployments |
| 39 | Peer Network | 7 | D5 | A2A tools | boundary + signed cards | your desk ↔ peer ↔ critic |
| 40 | **The Desk** | 11 | D5 | everything | three boundaries | six agents |

**296 sittings** — about ten months at five days a week. §13 has the levers.

---

# §12 · The day maps

For P04–P40, **day 01 is The kit and day 02 is The boundary**; the maps below start at day 03.
P00–P03 are listed in full because they are where the recapped material is taught deeply.

### P00 · Foundry — 3 days · reference only
| D | Title |
| --- | --- |
| 1 | The machine — uv, Python 3.12, and the four Pythons that ruin a Monday |
| 2 | The skeleton — `.gitignore` before `.env` exists, and why that order |
| 3 | Keys, pinning and the check that refuses a half-finished day |

### P01 · Ask Desk — 7 days · D1 · *teaches: the loop, tools, the ADK agent, events, sessions*
| D | Title |
| --- | --- |
| 1 | The loop by hand — think → act → observe, no framework |
| 2 | Tools by hand — JSON schemas and the tool-result turn |
| 3 | First ADK agent — `Agent` + runner, model pinned explicitly |
| 4 | `FunctionTool`, and what ADK does that you just did yourself |
| 5 | Events and streaming — the 2.x event model (**traps #2 and #3**) |
| 6 | Sessions, runs, and errors that surface instead of hiding (**trap #4**) |
| 7 | **Ship D1** — `api_server`, `/healthz`, the first eval that can go red; cold clone |

### P02 · Parts Counter — 8 days · D2 · *teaches: the MCP boundary, deeply*
| D | Title |
| --- | --- |
| 1 | The kit — this project's own utils, in full |
| 2 | Why the data goes behind a boundary, and what breaks when it doesn't |
| 3 | MCP 2026 — the stateless core; the phone-call → web reframe |
| 4 | The server skeleton and its first tool |
| 5 | Lifecycle, stateless-first — the old handshake as history |
| 6 | Transports — stdio and Streamable HTTP (SSE 🅿️ legacy) |
| 7 | The client side — connecting the agent; the tool that now lives elsewhere |
| 8 | **Ship D2** — stateless container, secrets injected not baked; cold clone |

### P03 · Triage Room — 8 days · D3 · *teaches: the cast, deeply*
| D | Title |
| --- | --- |
| 1 | The kit |
| 2 | The boundary — `desk_mcp`, printed whole |
| 3 | One agent is a function; two is an architecture |
| 4 | The Workflow Runtime — nodes and edges (**trap #1**) |
| 5 | The classifier — a specialist with three tools and no opinions |
| 6 | The writer — a specialist that only writes |
| 7 | Delegation, transfer and the handback |
| 8 | **Ship D3** — compose: agents and boundary as separate containers; cold clone |

---
*From here, day 01 = The kit, day 02 = The boundary.*

### P04 · Trip Ledger — 7 · D3
3 Callbacks before/after the model · 4 Callbacks before/after the tool; plugins · 5 Structured logging, three agents deep · 6 Token and quota accounting — a three-agent turn costs three · 7 **Ship D3** — the budget guard that refuses

### P05 · Bench Runner — 7 · D3
3 Models and providers; LiteLLM; Ollama offline · 4 Honest 429 — `Retry-After`, 1/2/4/8, escalate *(taught deeply here)* · 5 Different models for different agents — the cheap critic · 6 The fallback chain, and the answer you must not fabricate · 7 **Ship D3** — the benchmark report as an artifact

### P06 · Field Inspector — 7 · D3
3 Tool context and state inside a tool · 4 Long-running tools — the turn that doesn't return yet · 5 Artifacts — files that survive the turn and cross the boundary · 6 Toolsets and OpenAPI — wrapping a spec you didn't write · 7 **Ship D3** — the inspection that produces a real PDF

### P07 · Form Filler — 7 · D3
3 Structured output — schemas on the way out · 4 Schema evolution — the field that appeared last Tuesday · 5 Elicitation over MCP, incl. URL mode · 6 Resources and prompts — the server that ships its own instructions · 7 **Ship D3** — the validator that rejects the filler's confident guess

### P08 · Shop Floor — 8 · D3
3 Tool design — the description is the API · 4 Tool filtering and allowlists — who may call what · 5 Server capabilities — what a client can discover before it calls · 6 Cacheable lists and the `Mcp-Method` / `Mcp-Name` headers · 7 Failure lab — the agent that reached for a tool it shouldn't have · 8 **Ship D3**

### P09 · Long Haul — 8 · D3
3 Progress over a stateless protocol · 4 State handles in the payload — not a connection the server holds · 5 The Tasks extension — `tasks/get`, `update`, `cancel` · 6 Client hardening — timeouts, retries, no held connections · 7 Failure lab — two replicas, one poll, `unknown task id` · 8 **Ship D3** — the two-replica compose test

### P10 · Gatekeeper — 7 · D3
3 MCP auth — OAuth2 and the token that isn't yours · 4 RFC 9207 issuer validation; CIMD replacing dynamic registration · 5 Enterprise Managed Authorization and the extensions framework · 6 Scoped credentials per agent — the auditor that cannot write · 7 **Ship D3** — the token that expires mid-run

### P11 · Skill Forge — 8 · D3
3 The open spec — `SKILL.md` anatomy · 4 `SkillToolset` — loading skills into ADK · 5 Authoring skill one — a procedure your specialists repeat · 6 Progressive disclosure — the skill that doesn't blow the window · 7 Testing and versioning; the skill that fires on the wrong request · 8 **Ship D3** — skills lint in `./run check`

### P12 · Skill Auditor — 7 · D3
3 Sourcing third-party skills — the registry and its endpoints · 4 Reading a skill like an attacker · 5 The provenance ledger; `@latest` is not a version · 6 The audit report a reviewer will accept · 7 **Ship D3** — the gate blocks an unvetted skill

### P13 · Server Farm — 8 · D4
3 Stateless by default — any instance answers any request · 4 Deprecations — Roots/Sampling/Logging → `InputRequiredResult` · 5 Health, readiness, and the replica that lied · 6 Kubernetes on the laptop *(taught deeply here)* · 7 The sidecar pattern at three replicas · 8 **Ship D4** — scale to three, kill one mid-turn

### P14 · Peer Desk — 7 · D3
3 `to_mcp_server` — a whole agent served over MCP · 4 Agent-as-tool vs agent-as-peer — the choice that decides your architecture · 5 MCP Apps — sandboxed-iframe UIs · 6 Failure lab — the served agent that called back into its caller · 7 **Ship D3**

### P15 · Audit Room — 7 · D4
3 The MCP audit — what a reviewer checks, in order · 4 Security posture of a boundary you own · 5 The finding that isn't — false positives and reviewer trust · 6 Failure lab — the audit that passed a server it shouldn't have · 7 **Ship D4** — the audit as a CI job

### P16 · Recall Desk — 7 · D3
3 Sessions vs memory — two words for two different things · 4 Persistent sessions, database-backed · 5 Memory design — what to remember · 6 Memory in a multi-agent flow — who is allowed to remember · 7 **Ship D3** — the cross-session eval

### P17 · Forget Me — 6 · D3
3 What to forget, and when · 4 PII at the boundary — the thing that must not persist · 5 Retention windows and the deletion that must actually delete · 6 **Ship D3** — the redaction eval that goes red on a leaked field

### P18 · Archive Finder — 9 · D3
3 Embeddings, plainly — why "similar" is a number · 4 The local index at $0, owned by the boundary · 5 Chunking — where you cut decides what you find · 6 Top-k and thresholds — the confident wrong answer · 7 Citations — an answer that shows its source · 8 The retrieval eval: `recall@5` that goes red when chunking is off · 9 **Ship D3** — index rebuilt on container start

### P19 · Second Opinion — 7 · D3
3 Grounding vs retrieval — built-in search with brakes · 4 When RAG is the wrong tool · 5 The router that picks a source, and logs why · 6 The adjudicator — two answers that disagree · 7 **Ship D3**

### P20 · Cache Keeper — 6 · D3
3 What a cache key really is — and the one you got wrong · 4 Response caching and context caching — the quota lifeline · 5 Invalidation and staleness — the answer from last week · 6 **Ship D3** — the savings report, in requests not dollars

### P21 · Graph Runner — 8 · D3
3 State on the graph — who owns which key · 4 Sequential · 5 Parallel — and the two nodes that wrote the same key · 6 Loop, and how it terminates · 7 Conditional edges and routing · 8 **Ship D3** — the runaway graph, contained

### P22 · Writer & Critic — 7 · D3
3 The critique loop · 4 The critic's rubric — vague feedback is no feedback · 5 Stopping — when "good enough" is a rule, not a feeling · 6 The arbiter — breaking a deadlock without a human · 7 **Ship D3** — the loop that must not run forever

### P23 · Dispatch Yard — 7 · D3
3 Delegation vs transfer, the hard cases · 4 Agent-as-tool in ADK · 5 A specialist registry the dispatcher reads at runtime · 6 Reading a multi-agent trace when the wrong specialist answered · 7 **Ship D3**

### P24 · Plan Room — 8 · D3
3 Plan-and-execute · 4 The plan as data, not prose · 5 Decomposition — subgoals that are actually separable · 6 Replanning on failure · 7 What planning costs, in tokens · 8 **Ship D3** — the plan that never ends, and the bound that stops it

### P25 · Swarm Limits — 7 · D4
3 Shared state under concurrency — the last writer wins, and shouldn't · 4 The boundary under contention — six clients, one server · 5 The cost of coordination — when six agents are slower than one · 6 Containment — the swarm that wouldn't stop · 7 **Ship D4**

### P26 · Never Lose Work — 8 · D4
3 Durable execution, plainly · 4 Idempotency keys — the email sent twice · 5 Checkpoints · 6 Pause and resume · 7 Replay and determinism — the tool that isn't · 8 **Ship D4** — delete the pod mid-run; it finishes

### P27 · Approval Gate — 7 · D4
3 What needs a human; blast radius before capability · 4 Building the gate · 5 HITL resumption for standalone nodes; `NodeTool` · 6 The audit trail — who approved what, when · 7 **Ship D4** — the gate that got bypassed, and how

### P28 · Injection Range — 9 · D4
3 A threat model for agents · 4 Prompt injection — shown, not told · 5 **Injection through a tool result** — the boundary as attack surface · 6 The lethal trifecta · 7 Input guardrail callbacks · 8 Output guardrails — the exfiltration you didn't see · 9 **Ship D4** — the red-team evalset your desk survives

### P29 · Least Privilege — 6 · D4
3 Per-agent tool permissions · 4 Scoped MCP credentials and capability tokens · 5 The privilege review — what a reviewer asks · 6 **Ship D4** — the agent that escalated, caught by a test

### P30 · Sandbox Yard — 7 · D4
3 Code execution, and why it is a different kind of tool · 4 Sandboxing — the concept, then the boundary · 5 Execution isolation in practice; `e2b` / `daytona` 🅿️ · 6 Computer use against a range you own · 7 **Ship D4** — the runaway, contained

### P31 · Quota Router — 6 · D4
3 The quota ledger — requests remaining, per provider, per window · 4 The router plugin — send the cast to headroom · 5 Escalation and the runbook · 6 **Ship D4** — exhaust a provider on purpose

### P32 · Night Shift — 6 · D4
3 Ambient agents — nobody typed anything · 4 Scheduled runs; the CronJob · 5 Quota-aware scheduling — the job that ran at the wrong hour · 6 **Ship D4** — the digest someone would actually act on

### P33 · Watch Tower — 6 · D4
3 Event-driven intake — webhooks and the retry you didn't ask for · 4 Deduplication — the same event, four times · 5 Idempotent intake · 6 **Ship D4**

### P34 · Voice Standup — 8 · D3
3 Live API — the streaming architecture · 4 The bidi loop · 5 Audio in, audio out; free-quota check and fallback · 6 VAD events — knowing when they stopped talking · 7 Non-blocking tools — the conversation that must not freeze · 8 **Ship D3**

### P35 · Eval Bench — 8 · D5
3 Evals are tests — the change that made it worse · 4 Evalsets and metrics · 5 The eval workhorse — a cheap model judging a cheap model · 6 Trajectory evaluation — the right answer by the wrong route · 7 Rubric-based multi-turn trajectory evaluation · 8 **Ship D5** — LLM-as-judge and the honest baseline

### P36 · Regression Gate — 7 · D5
3 Evals in CI — the pipeline that says no · 4 Cost guards — the eval that passed and cost triple · 5 Latency guards — p95, not the mean · 6 Flaky evals and the threshold you'll be tempted to lower · 7 **Ship D5** — a regression blocked with nobody deciding

### P37 · Glass Box — 7 · D5
3 OTel and `AutoTracingPlugin` · 4 The trace tree across three agents and two MCP hops · 5 Debugging slow, not broken · 6 The span that was missing — instrumenting your own boundary · 7 **Ship D5**

### P38 · Blue Green — 7 · D5
3 The API surface — `api_server` and FastAPI endpoints · 4 The manifest set, whole · 5 Blue/green — two deployments, one service · 6 Auto-rollback — the health signal that decides · 7 **Ship D5** — roll forward into a bad build, watch it roll back

### P39 · Peer Network — 7 · D5
3 A2A v1.0 — signed Agent Cards, verified hands-on · 4 Agent-as-peer vs agent-as-tool, decided · 5 Agent identity and the registry · 6 The agent economy 🅿️ — AP2, x402, Trusted Agent Protocol · 7 **Ship D5** — the peer whose card fails verification

### P40 · The Desk — 11 · D5 · capstone
3 The cast — six agents, and why not four or nine · 4 The boundaries — three servers, and what each owns · 5 Memory and retrieval in the graph · 6 Durability and the gate on every external write · 7 The security pass — injection, privilege, PII, synthetic-only · 8 Evals: the full set, and the one that must be able to fail · 9 Traced, containerised, blue/green · 10 The cold run — no edits, no retries, recorded · 11 Repo public; demo script; the interview drill over every ADR

---

## §13 · What independence costs, and what I recommend removing

**The cost, stated plainly.** Removing `_shared/` adds one day to every project from P04 — the kit
day — and it means roughly 400 lines of near-identical scaffolding get typed forty times. v2 was
256 sittings; v3 is **296**. That is the bill for four people being able to build four projects on
four machines with nothing in common. I think it is worth paying, and you should know the number.

**Three things I recommend cutting, now that duplication has a price:**

1. **Papers.** v1 and v2 kept an optional `papers/` document with a runnable ablation demo, carried
   over from the source repo. Cut it entirely. It adds roughly eight days, and a paper document
   that cites another project's teaching is exactly the cross-reference this version exists to
   remove. Where a paper genuinely changes how you use something, the part's *In production*
   section names it in one sentence with its arXiv ID.
   **−8 days.**

2. **Four thin projects — 17, 20, 29, 33.** Each is five to six days, and now each of those days
   also carries a duplicated kit and boundary. A six-day project that spends two days on
   scaffolding is a poor trade. Fold **17 → 16**, **20 → 18**, **29 → 28**, **33 → 32**, adding two
   days to each host. **−24 days, and the count drops to 36.** If you want to hold at 40, I would
   replace them with four systems that genuinely deserve their own repo — a contract/document
   reader with multimodal tools, an incident commander over runbook skills, an onboarding desk,
   and a scheduling agent with constraint tools. Say which you prefer and I will write the maps.

3. **The global `./p` driver's product commands.** In v2 it could run and check projects. It can't
   any more and shouldn't pretend to — each project has `./run`. Keep `./p` as an authoring tool
   with five commands: `brief`, `depth`, `index`, `verify`, `recall`. Smaller surface, no illusion
   that a project needs it.

Applied together: **296 → 264**, or 272 if you hold at 40 with four replacements.

**Two open decisions:**

- **P01–P03 still break the independence rule slightly** — they are independent as *code*, but
  they are where the recapped concepts are taught deeply, so their day docs are longer than
  everyone else's and they are the natural starting point. That is fine if you do them first. If
  someone else picks up P22 cold, the primer carries them. Confirm that trade is acceptable.
- **The 400 duplicated lines will drift.** By P30 your `util/backoff.py` will be better than the
  one in P06, and P06 will never get the improvement. That is the honest consequence of
  independence, and I would not fight it — but if you want, each project's last day can carry a
  five-line *"what I would change if I wrote this again"* note, which costs nothing and turns the
  drift into a record of your own progress.

---

## §14 · What v3.1.0 added, and what it did not change

**Nothing above this line changed.** §0 to §13 are v3.0.0 as written: the same forty projects, the
same completeness rule, the same depth rule, the same primer, the same 296 project sittings.

v3.1.0 adds three things the plan described in prose but never expressed in a form a script could
read, and one day that did not exist:

1. **Machine-readable blocks.** §15, §16 and §17 restate the tracks, the phases and the day map
   between `<!-- granth:...:start -->` markers. A heading can be reworded by accident; a marker
   cannot. `./p` reads these and nothing else, so a person reading this plan and a script parsing
   it cannot drift apart. §11 and §12 remain the human-readable per-project view and are still
   where a project's shape is decided; §17 is the authoritative **numbering**.
2. **An ID scheme.** Every concept in the curriculum now has an address, so "where do I learn
   about idempotency keys?" has one answer, and "is anything from P09 still open?" is a query
   rather than a memory.
3. **Day 0 — the authoring repository itself.** v3.0.0 described `./p` in §6 and §13 and never
   said which sitting builds it. It is now day 0, it sits outside every project, and it closes
   `RB-01`, `RB-02` and `RB-03`. See `docs/adr/ADR-0002-day-zero-and-the-authoring-repo.md`.

**One thing was removed:** the `sitting_minutes: 60` field from the hub frontmatter in §4.1. The
sitting budget is real and it stays — it lives in this plan's header and in §3, and that is the
only place a clock appears in this repository. What it must not do is sit in a day document, where
it silently authorises the worst edit in technical writing: cutting an explanation because the day
is running long. A subject that will not fit becomes two days, exactly as §3 already said.

Every other field in §4.1 and every section in §5 is unchanged, and `./p depth` now enforces them.

---

## §15 · The tracks and the ID scheme

A **track** is a thread that runs the length of the curriculum. A **project** is a repository. The
two are deliberately different shapes: P18 Archive Finder is one project, and it advances the
memory track, the boundary track and the deploy track in the same nine sittings.

An ID is closed when the concept is built into that project's artifact and the day's gates are
green. `docs/TRACEABILITY.md` is regenerated from the day hubs; **an open ID from a finished
project is a bug**, not a backlog item.

<!-- granth:tracks:start -->

| Track | Prefix | Count | What runs through it |
| --- | --- | --- | --- |
| Repository & authoring | `RB` | 4 | The plan, the ledgers, `./p`, the depth contract — the layer that keeps forty independent repositories honest without any of them depending on it. |
| Foundations & the kit | `FN` | 42 | The machine, and the kit every project rebuilds from scratch: pins, backoff, logging, budget, the eval harness. Duplicated forty times on purpose (§0). |
| Agents, casts & workflows | `AG` | 39 | One agent is a function; two is an architecture. The loop, events, delegation, transfer, graphs, planning, arbitration, swarms. |
| Tools, schemas & skills | `TL` | 18 | What an agent can reach for: function tools, schemas, artifacts, long-running calls, OpenAPI toolsets, Agent Skills, code execution. |
| The MCP boundary | `MC` | 56 | The data boundary every project owns: the stateless core, transports, lifecycle, resources, elicitation, tasks, capabilities, and serving an agent as a server. |
| Memory & retrieval | `MR` | 16 | Sessions versus memory, what to remember, what to forget, embeddings, chunking, top-k, citations, caching. |
| Reliability & durability | `RS` | 29 | Honest 429s, budgets, fallback chains, checkpoints, idempotency, replay, contention, quota ledgers — everything that decides whether a run survives. |
| Security & privilege | `SC` | 31 | Threat modelling, injection through a tool result, guardrails, OAuth2 at the boundary, scoped credentials, PII, sandboxing, the approval gate. |
| Evals & observability | `EV` | 24 | The checks that can go red: evalsets, judges, trajectories, rubrics, CI gates, cost and latency guards, tracing across agents and hops. |
| Deploy, ops & interop | `DP` | 51 | D1 to D5: the API surface, containers, compose with a sidecar, Kubernetes, CronJobs, blue/green with auto-rollback, A2A, and the cold clone that ends every project. |

<!-- granth:tracks:end -->

**Total: 310 concept IDs across 297 sittings.**

The authoritative statement of what an ID *means* is the row that assigns it in §17. This table
gives the shape; §17 gives the contract.

---

## §16 · The phases

**A phase is a project.** That is the whole point of v3: a project is the unit that has to stand up
on its own, so it is also the unit that has to pass a gate. Phase 0 is the authoring repository,
and it is the only phase that is not a project.

Every project's gate is the sentence from §7: **`./p verify P` copies only that project's folder
into a clean container, follows its own `SETUP.md`, builds it day by day from its own documents,
and runs its own `./run check`.** The gate column below says what *else* that project must show,
on top of the verify they all share.

<!-- granth:phases:start -->

| Phase | Days | Theme | The gate |
| --- | --- | --- | --- |
| 0 | 0 | The authoring repository — the plan, the ledgers and `./p` | `python p.py doctor` and `python p.py check` both green on a repository with one day in it |
| P00 | 1–3 | Foundry — reference only; no project depends on it | A bare machine reaches a green check, and the check refuses a half-finished day |
| P01 | 4–10 | Ask Desk — the loop, tools, the ADK agent, events, sessions | D1: `api_server` answers `/healthz`, and the first eval goes red on purpose |
| P02 | 11–18 | Parts Counter — the MCP boundary, taught deeply | D2: a stateless container, secrets injected and not baked |
| P03 | 19–26 | Triage Room — the cast, taught deeply | D3: compose runs agents and boundary as separate containers |
| P04 | 27–33 | Trip Ledger — callbacks, plugins, and what a three-agent turn costs | The budget guard refuses a turn that would exceed the window |
| P05 | 34–40 | Bench Runner — providers, honest 429s, the cheap critic | Four providers benchmarked, and no fabricated answer covers an error |
| P06 | 41–47 | Field Inspector — long-running tools and artifacts | An inspection produces a real file that survives the turn |
| P07 | 48–54 | Form Filler — structured output, elicitation, resources | The validator rejects the filler's confident guess |
| P08 | 55–62 | Shop Floor — tool design, filtering and discovery | An agent is refused a tool it should not have reached for |
| P09 | 63–70 | Long Haul — progress over a stateless protocol | Two replicas, one poll, and no held connection |
| P10 | 71–77 | Gatekeeper — OAuth2, issuer validation, scoped credentials | A token expires mid-run and the run fails honestly |
| P11 | 78–85 | Skill Forge — authoring and loading Agent Skills | Skills lint inside `./run check` |
| P12 | 86–92 | Skill Auditor — reading a third-party skill like an attacker | The gate blocks an unvetted skill |
| P13 | 93–100 | Server Farm — stateless replicas on Kubernetes | Scale to three, kill one mid-turn, and the turn completes |
| P14 | 101–107 | Peer Desk — an agent served over MCP | A served agent that calls back into its caller is caught |
| P15 | 108–114 | Audit Room — auditing a boundary you own | The audit runs as a CI job and produces a report a reviewer accepts |
| P16 | 115–121 | Recall Desk — sessions versus memory | A cross-session eval proves something was remembered |
| P17 | 122–127 | Forget Me — retention, redaction and deletion | The redaction eval goes red on a leaked field |
| P18 | 128–136 | Archive Finder — embeddings, chunking, citations | `recall@5` goes red when the chunker is disabled |
| P19 | 137–143 | Second Opinion — grounding versus retrieval | Two sources disagree, and the adjudicator logs why |
| P20 | 144–149 | Cache Keeper — keys, invalidation, staleness | The savings report is stated in requests, not dollars |
| P21 | 150–157 | Graph Runner — state, parallelism, loops, edges | The runaway graph is contained by a bound, not by luck |
| P22 | 158–164 | Writer & Critic — the critique loop and its rubric | The loop that must not run forever, and does not |
| P23 | 165–171 | Dispatch Yard — delegation, transfer, a runtime registry | A trace explains why the wrong specialist answered |
| P24 | 172–179 | Plan Room — plan as data, decomposition, replanning | The plan that never ends meets the bound that stops it |
| P25 | 180–186 | Swarm Limits — shared state and the cost of coordination | Six agents under contention, and the swarm that would not stop |
| P26 | 187–194 | Never Lose Work — checkpoints, idempotency, replay | Delete the pod mid-run; the job finishes |
| P27 | 195–201 | Approval Gate — what needs a human, and the audit trail | The gate is bypassed on purpose, and the trail shows it |
| P28 | 202–210 | Injection Range — the boundary as attack surface | The desk survives a red-team evalset it did not write |
| P29 | 211–216 | Least Privilege — per-agent permissions and capability tokens | An escalating agent is caught by a test, not by review |
| P30 | 217–223 | Sandbox Yard — code execution and isolation | The runaway is contained inside the sandbox |
| P31 | 224–229 | Quota Router — the ledger and the headroom router | A provider is exhausted on purpose and the cast reroutes |
| P32 | 230–235 | Night Shift — ambient agents and scheduled runs | A digest someone would actually act on, produced unattended |
| P33 | 236–241 | Watch Tower — webhooks, deduplication, idempotent intake | The same event arrives four times and is handled once |
| P34 | 242–249 | Voice Standup — the Live API and non-blocking tools | The conversation does not freeze while a tool runs |
| P35 | 250–257 | Eval Bench — evalsets, judges, trajectories | LLM-as-judge, scored against an honest baseline |
| P36 | 258–264 | Regression Gate — evals, cost and latency in CI | A regression is blocked with nobody deciding |
| P37 | 265–271 | Glass Box — tracing across agents and hops | The missing span is found, and the boundary instrumented |
| P38 | 272–278 | Blue Green — two deployments, one service | Roll forward into a bad build and watch it roll back |
| P39 | 279–285 | Peer Network — A2A, signed cards, agent identity | A peer whose card fails verification is refused |
| P40 | 286–296 | The Desk — the capstone: six agents, three boundaries | A recorded cold run with no edits and no retries, then the interview drill over every ADR |

<!-- granth:phases:end -->

Every phase gate also includes the freshness check (§10), which for this plan runs **at the start
of a project**, not daily — you pin once and live with it for six to nine sittings.

---

## §17 · The day map — day to IDs closed

> **The authoritative day-to-ID assignment, and the authoritative numbering.** A day document
> closes **exactly** these IDs — no more, no fewer. A day that wants to close a different ID is
> asking for a plan amendment, and the amendment is written before the day is.
>
> §11 and §12 remain the per-project view: they are where a project's shape, tier and cast are
> decided, and they are what you read when choosing what to build. This table is that same
> curriculum with a global sitting number attached to every row, which is the form `./p` needs,
> and the form that makes "is day 137 allowed yet?" a mechanical question.
>
> **From P04 onward, day 1 of every project is The kit and day 2 is The boundary** (§3.1). They
> appear here because they are real sittings that close real IDs, even though the maps in §12
> start at day 3.

<!-- granth:day-map:start -->

### Phase 0 — the authoring repository (day 0)

| Day | Title | IDs closed |
| --- | --- | --- |
| 0 | Day zero — the toolchain, the skeleton, and the `./p` driver | RB-01, RB-02, RB-03 |

### Phase P00 — Foundry, reference only (days 1–3)

| Day | Title | IDs closed |
| --- | --- | --- |
| 1 | P00 Foundry · 1 — The machine: uv, Python 3.12, and the four Pythons that ruin a Monday | FN-01 |
| 2 | P00 Foundry · 2 — The skeleton: `.gitignore` before `.env` exists, and why that order | FN-02 |
| 3 | P00 Foundry · 3 — Keys, pinning, and the check that refuses a half-finished day | FN-03 |

### Phase P01 — Ask Desk · D1 (days 4–10)

| Day | Title | IDs closed |
| --- | --- | --- |
| 4 | P01 Ask Desk · 1 — The loop by hand: think, act, observe, no framework | AG-01 |
| 5 | P01 Ask Desk · 2 — Tools by hand: JSON schemas and the tool-result turn | TL-01 |
| 6 | P01 Ask Desk · 3 — The first ADK agent: `Agent` plus runner, model pinned explicitly | AG-02 |
| 7 | P01 Ask Desk · 4 — `FunctionTool`, and what ADK does that you just did yourself | TL-02 |
| 8 | P01 Ask Desk · 5 — Events and streaming: the 2.x event model | AG-03 |
| 9 | P01 Ask Desk · 6 — Sessions, runs, and errors that surface instead of hiding | AG-04, RS-01 |
| 10 | P01 Ask Desk · 7 — Ship D1: `api_server`, `/healthz`, the first eval that can go red; cold clone | DP-01, EV-01 |

### Phase P02 — Parts Counter · D2 (days 11–18)

| Day | Title | IDs closed |
| --- | --- | --- |
| 11 | P02 Parts Counter · 1 — The kit: this project's own utils, in full | FN-04 |
| 12 | P02 Parts Counter · 2 — Why the data goes behind a boundary, and what breaks when it does not | MC-01 |
| 13 | P02 Parts Counter · 3 — MCP 2026: the stateless core, and the phone-call to web reframe | MC-02 |
| 14 | P02 Parts Counter · 4 — The server skeleton and its first tool | MC-03 |
| 15 | P02 Parts Counter · 5 — Lifecycle, stateless-first: the old handshake as history | MC-04 |
| 16 | P02 Parts Counter · 6 — Transports: stdio and Streamable HTTP | MC-05 |
| 17 | P02 Parts Counter · 7 — The client side: connecting the agent to a tool that now lives elsewhere | MC-06 |
| 18 | P02 Parts Counter · 8 — Ship D2: stateless container, secrets injected not baked; cold clone | DP-02 |

### Phase P03 — Triage Room · D3 (days 19–26)

| Day | Title | IDs closed |
| --- | --- | --- |
| 19 | P03 Triage Room · 1 — The kit | FN-05 |
| 20 | P03 Triage Room · 2 — The boundary: `desk_mcp`, printed whole | MC-07 |
| 21 | P03 Triage Room · 3 — One agent is a function; two is an architecture | AG-05 |
| 22 | P03 Triage Room · 4 — The Workflow Runtime: nodes and edges | AG-06 |
| 23 | P03 Triage Room · 5 — The classifier: a specialist with three tools and no opinions | AG-07 |
| 24 | P03 Triage Room · 6 — The writer: a specialist that only writes | AG-08 |
| 25 | P03 Triage Room · 7 — Delegation, transfer and the handback | AG-09 |
| 26 | P03 Triage Room · 8 — Ship D3: compose, agents and boundary as separate containers; cold clone | DP-03 |

### Phase P04 — Trip Ledger · D3 (days 27–33)

| Day | Title | IDs closed |
| --- | --- | --- |
| 27 | P04 Trip Ledger · 1 — The kit | FN-06 |
| 28 | P04 Trip Ledger · 2 — The boundary: `desk_mcp` and the meter | MC-08 |
| 29 | P04 Trip Ledger · 3 — Callbacks before and after the model | AG-10 |
| 30 | P04 Trip Ledger · 4 — Callbacks before and after the tool; plugins | TL-03 |
| 31 | P04 Trip Ledger · 5 — Structured logging, three agents deep | EV-02 |
| 32 | P04 Trip Ledger · 6 — Token and quota accounting: a three-agent turn costs three | RS-02 |
| 33 | P04 Trip Ledger · 7 — Ship D3: the budget guard that refuses | RS-03, DP-04 |

### Phase P05 — Bench Runner · D3 (days 34–40)

| Day | Title | IDs closed |
| --- | --- | --- |
| 34 | P05 Bench Runner · 1 — The kit | FN-07 |
| 35 | P05 Bench Runner · 2 — The boundary: `bench_mcp`, fixtures behind it | MC-09 |
| 36 | P05 Bench Runner · 3 — Models and providers; LiteLLM; Ollama offline | AG-11 |
| 37 | P05 Bench Runner · 4 — Honest 429: `Retry-After`, 1/2/4/8, escalate | RS-04 |
| 38 | P05 Bench Runner · 5 — Different models for different agents: the cheap critic | AG-12 |
| 39 | P05 Bench Runner · 6 — The fallback chain, and the answer you must not fabricate | RS-05 |
| 40 | P05 Bench Runner · 7 — Ship D3: the benchmark report as an artifact | DP-05 |

### Phase P06 — Field Inspector · D3 (days 41–47)

| Day | Title | IDs closed |
| --- | --- | --- |
| 41 | P06 Field Inspector · 1 — The kit | FN-08 |
| 42 | P06 Field Inspector · 2 — The boundary: `field_mcp`, photos and reports | MC-10 |
| 43 | P06 Field Inspector · 3 — Tool context, and state inside a tool | TL-04 |
| 44 | P06 Field Inspector · 4 — Long-running tools: the turn that does not return yet | TL-05 |
| 45 | P06 Field Inspector · 5 — Artifacts: files that survive the turn and cross the boundary | TL-06 |
| 46 | P06 Field Inspector · 6 — Toolsets and OpenAPI: wrapping a spec you did not write | TL-07 |
| 47 | P06 Field Inspector · 7 — Ship D3: the inspection that produces a real PDF | DP-06 |

### Phase P07 — Form Filler · D3 (days 48–54)

| Day | Title | IDs closed |
| --- | --- | --- |
| 48 | P07 Form Filler · 1 — The kit | FN-09 |
| 49 | P07 Form Filler · 2 — The boundary: `schema_mcp` | MC-11 |
| 50 | P07 Form Filler · 3 — Structured output: schemas on the way out | TL-08 |
| 51 | P07 Form Filler · 4 — Schema evolution: the field that appeared last Tuesday | TL-09 |
| 52 | P07 Form Filler · 5 — Elicitation over MCP, including URL mode | MC-12 |
| 53 | P07 Form Filler · 6 — Resources and prompts: the server that ships its own instructions | MC-13 |
| 54 | P07 Form Filler · 7 — Ship D3: the validator that rejects the filler's confident guess | EV-03, DP-07 |

### Phase P08 — Shop Floor · D3 (days 55–62)

| Day | Title | IDs closed |
| --- | --- | --- |
| 55 | P08 Shop Floor · 1 — The kit | FN-10 |
| 56 | P08 Shop Floor · 2 — The boundary: `floor_mcp` | MC-14 |
| 57 | P08 Shop Floor · 3 — Tool design: the description is the API | TL-10 |
| 58 | P08 Shop Floor · 4 — Tool filtering and allowlists: who may call what | SC-01 |
| 59 | P08 Shop Floor · 5 — Server capabilities: what a client can discover before it calls | MC-15 |
| 60 | P08 Shop Floor · 6 — Cacheable lists, and the method and name headers | MC-16 |
| 61 | P08 Shop Floor · 7 — Failure lab: the agent that reached for a tool it should not have | SC-02 |
| 62 | P08 Shop Floor · 8 — Ship D3 | DP-08 |

### Phase P09 — Long Haul · D3 (days 63–70)

| Day | Title | IDs closed |
| --- | --- | --- |
| 63 | P09 Long Haul · 1 — The kit | FN-11 |
| 64 | P09 Long Haul · 2 — The boundary: `haul_mcp` | MC-17 |
| 65 | P09 Long Haul · 3 — Progress over a stateless protocol | MC-18 |
| 66 | P09 Long Haul · 4 — State handles in the payload, not a connection the server holds | MC-19 |
| 67 | P09 Long Haul · 5 — The Tasks extension: get, update, cancel | MC-20 |
| 68 | P09 Long Haul · 6 — Client hardening: timeouts, retries, no held connections | RS-06 |
| 69 | P09 Long Haul · 7 — Failure lab: two replicas, one poll, unknown task id | RS-07 |
| 70 | P09 Long Haul · 8 — Ship D3: the two-replica compose test | DP-09 |

### Phase P10 — Gatekeeper · D3 (days 71–77)

| Day | Title | IDs closed |
| --- | --- | --- |
| 71 | P10 Gatekeeper · 1 — The kit | FN-12 |
| 72 | P10 Gatekeeper · 2 — The boundary: `vault_mcp` | MC-21 |
| 73 | P10 Gatekeeper · 3 — MCP auth: OAuth2 and the token that is not yours | SC-03 |
| 74 | P10 Gatekeeper · 4 — Issuer validation, and CIMD replacing dynamic registration | SC-04 |
| 75 | P10 Gatekeeper · 5 — Enterprise Managed Authorization and the extensions framework | SC-05 |
| 76 | P10 Gatekeeper · 6 — Scoped credentials per agent: the auditor that cannot write | SC-06 |
| 77 | P10 Gatekeeper · 7 — Ship D3: the token that expires mid-run | DP-10 |

### Phase P11 — Skill Forge · D3 (days 78–85)

| Day | Title | IDs closed |
| --- | --- | --- |
| 78 | P11 Skill Forge · 1 — The kit | FN-13 |
| 79 | P11 Skill Forge · 2 — The boundary: `forge_mcp` | MC-22 |
| 80 | P11 Skill Forge · 3 — The open spec: the anatomy of a skill document | TL-11 |
| 81 | P11 Skill Forge · 4 — `SkillToolset`: loading skills into ADK | TL-12 |
| 82 | P11 Skill Forge · 5 — Authoring skill one: a procedure your specialists repeat | TL-13 |
| 83 | P11 Skill Forge · 6 — Progressive disclosure: the skill that does not blow the window | TL-14 |
| 84 | P11 Skill Forge · 7 — Testing and versioning; the skill that fires on the wrong request | EV-04 |
| 85 | P11 Skill Forge · 8 — Ship D3: skills lint inside the project check | DP-11 |

### Phase P12 — Skill Auditor · D3 (days 86–92)

| Day | Title | IDs closed |
| --- | --- | --- |
| 86 | P12 Skill Auditor · 1 — The kit | FN-14 |
| 87 | P12 Skill Auditor · 2 — The boundary: `registry_mcp` | MC-23 |
| 88 | P12 Skill Auditor · 3 — Sourcing third-party skills: the registry and its endpoints | TL-15 |
| 89 | P12 Skill Auditor · 4 — Reading a skill like an attacker | SC-07 |
| 90 | P12 Skill Auditor · 5 — The provenance ledger, and why `@latest` is not a version | SC-08 |
| 91 | P12 Skill Auditor · 6 — The audit report a reviewer will accept | SC-09 |
| 92 | P12 Skill Auditor · 7 — Ship D3: the gate blocks an unvetted skill | DP-12 |

### Phase P13 — Server Farm · D4 (days 93–100)

| Day | Title | IDs closed |
| --- | --- | --- |
| 93 | P13 Server Farm · 1 — The kit | FN-15 |
| 94 | P13 Server Farm · 2 — The boundary: `farm_mcp` | MC-24 |
| 95 | P13 Server Farm · 3 — Stateless by default: any instance answers any request | MC-25 |
| 96 | P13 Server Farm · 4 — Deprecations: roots, sampling and logging, and what replaced them | MC-26 |
| 97 | P13 Server Farm · 5 — Health, readiness, and the replica that lied | DP-13 |
| 98 | P13 Server Farm · 6 — Kubernetes on the laptop | DP-14 |
| 99 | P13 Server Farm · 7 — The sidecar pattern at three replicas | DP-15 |
| 100 | P13 Server Farm · 8 — Ship D4: scale to three, kill one mid-turn | DP-16 |

### Phase P14 — Peer Desk · D3 (days 101–107)

| Day | Title | IDs closed |
| --- | --- | --- |
| 101 | P14 Peer Desk · 1 — The kit | FN-16 |
| 102 | P14 Peer Desk · 2 — The boundary | MC-27 |
| 103 | P14 Peer Desk · 3 — `to_mcp_server`: a whole agent served over MCP | MC-28 |
| 104 | P14 Peer Desk · 4 — Agent-as-tool against agent-as-peer: the choice that decides your architecture | AG-13 |
| 105 | P14 Peer Desk · 5 — MCP Apps: sandboxed-iframe interfaces | MC-29 |
| 106 | P14 Peer Desk · 6 — Failure lab: the served agent that called back into its caller | AG-14 |
| 107 | P14 Peer Desk · 7 — Ship D3 | DP-17 |

### Phase P15 — Audit Room · D4 (days 108–114)

| Day | Title | IDs closed |
| --- | --- | --- |
| 108 | P15 Audit Room · 1 — The kit | FN-17 |
| 109 | P15 Audit Room · 2 — The boundary, plus a fixture boundary to audit | MC-30 |
| 110 | P15 Audit Room · 3 — The MCP audit: what a reviewer checks, in order | SC-10 |
| 111 | P15 Audit Room · 4 — The security posture of a boundary you own | SC-11 |
| 112 | P15 Audit Room · 5 — The finding that is not: false positives and reviewer trust | SC-12 |
| 113 | P15 Audit Room · 6 — Failure lab: the audit that passed a server it should not have | SC-13 |
| 114 | P15 Audit Room · 7 — Ship D4: the audit as a CI job | DP-18 |

### Phase P16 — Recall Desk · D3 (days 115–121)

| Day | Title | IDs closed |
| --- | --- | --- |
| 115 | P16 Recall Desk · 1 — The kit | FN-18 |
| 116 | P16 Recall Desk · 2 — The boundary: `memory_mcp` | MC-31 |
| 117 | P16 Recall Desk · 3 — Sessions against memory: two words for two different things | MR-01 |
| 118 | P16 Recall Desk · 4 — Persistent sessions, database-backed | MR-02 |
| 119 | P16 Recall Desk · 5 — Memory design: what to remember | MR-03 |
| 120 | P16 Recall Desk · 6 — Memory in a multi-agent flow: who is allowed to remember | MR-04 |
| 121 | P16 Recall Desk · 7 — Ship D3: the cross-session eval | EV-05, DP-19 |

### Phase P17 — Forget Me · D3 (days 122–127)

| Day | Title | IDs closed |
| --- | --- | --- |
| 122 | P17 Forget Me · 1 — The kit | FN-19 |
| 123 | P17 Forget Me · 2 — The boundary: `memory_mcp` with a redactor | MC-32 |
| 124 | P17 Forget Me · 3 — What to forget, and when | MR-05 |
| 125 | P17 Forget Me · 4 — PII at the boundary: the thing that must not persist | SC-14 |
| 126 | P17 Forget Me · 5 — Retention windows, and the deletion that must actually delete | MR-06 |
| 127 | P17 Forget Me · 6 — Ship D3: the redaction eval that goes red on a leaked field | EV-06, DP-20 |

### Phase P18 — Archive Finder · D3 (days 128–136)

| Day | Title | IDs closed |
| --- | --- | --- |
| 128 | P18 Archive Finder · 1 — The kit | FN-20 |
| 129 | P18 Archive Finder · 2 — The boundary: `archive_mcp`, index and store | MC-33 |
| 130 | P18 Archive Finder · 3 — Embeddings, plainly: why similar is a number | MR-07 |
| 131 | P18 Archive Finder · 4 — The local index at zero cost, owned by the boundary | MR-08 |
| 132 | P18 Archive Finder · 5 — Chunking: where you cut decides what you find | MR-09 |
| 133 | P18 Archive Finder · 6 — Top-k and thresholds: the confident wrong answer | MR-10 |
| 134 | P18 Archive Finder · 7 — Citations: an answer that shows its source | MR-11 |
| 135 | P18 Archive Finder · 8 — The retrieval eval: `recall@5`, red when chunking is off | EV-07 |
| 136 | P18 Archive Finder · 9 — Ship D3: the index rebuilt on container start | DP-21 |

### Phase P19 — Second Opinion · D3 (days 137–143)

| Day | Title | IDs closed |
| --- | --- | --- |
| 137 | P19 Second Opinion · 1 — The kit | FN-21 |
| 138 | P19 Second Opinion · 2 — The boundaries: `archive_mcp` and `web_mcp` | MC-34 |
| 139 | P19 Second Opinion · 3 — Grounding against retrieval: built-in search with brakes | MR-12 |
| 140 | P19 Second Opinion · 4 — When retrieval is the wrong tool | MR-13 |
| 141 | P19 Second Opinion · 5 — The router that picks a source, and logs why | AG-15 |
| 142 | P19 Second Opinion · 6 — The adjudicator: two answers that disagree | AG-16 |
| 143 | P19 Second Opinion · 7 — Ship D3 | DP-22 |

### Phase P20 — Cache Keeper · D3 (days 144–149)

| Day | Title | IDs closed |
| --- | --- | --- |
| 144 | P20 Cache Keeper · 1 — The kit | FN-22 |
| 145 | P20 Cache Keeper · 2 — The boundary, with a cache layer in front of it | MC-35 |
| 146 | P20 Cache Keeper · 3 — What a cache key really is, and the one you got wrong | MR-14 |
| 147 | P20 Cache Keeper · 4 — Response caching and context caching: the quota lifeline | RS-08 |
| 148 | P20 Cache Keeper · 5 — Invalidation and staleness: the answer from last week | MR-15 |
| 149 | P20 Cache Keeper · 6 — Ship D3: the savings report, in requests not dollars | DP-23 |

### Phase P21 — Graph Runner · D3 (days 150–157)

| Day | Title | IDs closed |
| --- | --- | --- |
| 150 | P21 Graph Runner · 1 — The kit | FN-23 |
| 151 | P21 Graph Runner · 2 — The boundary: `desk_mcp` | MC-36 |
| 152 | P21 Graph Runner · 3 — State on the graph: who owns which key | AG-17 |
| 153 | P21 Graph Runner · 4 — Sequential | AG-18 |
| 154 | P21 Graph Runner · 5 — Parallel, and the two nodes that wrote the same key | AG-19 |
| 155 | P21 Graph Runner · 6 — Loop, and how it terminates | AG-20 |
| 156 | P21 Graph Runner · 7 — Conditional edges and routing | AG-21 |
| 157 | P21 Graph Runner · 8 — Ship D3: the runaway graph, contained | RS-09, DP-24 |

### Phase P22 — Writer & Critic · D3 (days 158–164)

| Day | Title | IDs closed |
| --- | --- | --- |
| 158 | P22 Writer & Critic · 1 — The kit | FN-24 |
| 159 | P22 Writer & Critic · 2 — The boundary: `style_mcp`, guides and examples | MC-37 |
| 160 | P22 Writer & Critic · 3 — The critique loop | AG-22 |
| 161 | P22 Writer & Critic · 4 — The critic's rubric: vague feedback is no feedback | EV-08 |
| 162 | P22 Writer & Critic · 5 — Stopping: when good enough is a rule, not a feeling | AG-23 |
| 163 | P22 Writer & Critic · 6 — The arbiter: breaking a deadlock without a human | AG-24 |
| 164 | P22 Writer & Critic · 7 — Ship D3: the loop that must not run forever | RS-10, DP-25 |

### Phase P23 — Dispatch Yard · D3 (days 165–171)

| Day | Title | IDs closed |
| --- | --- | --- |
| 165 | P23 Dispatch Yard · 1 — The kit | FN-25 |
| 166 | P23 Dispatch Yard · 2 — The boundary: `roster_mcp`, the specialist registry | MC-38 |
| 167 | P23 Dispatch Yard · 3 — Delegation against transfer, the hard cases | AG-25 |
| 168 | P23 Dispatch Yard · 4 — Agent-as-tool in ADK | AG-26 |
| 169 | P23 Dispatch Yard · 5 — A specialist registry the dispatcher reads at runtime | AG-27 |
| 170 | P23 Dispatch Yard · 6 — Reading a multi-agent trace when the wrong specialist answered | EV-09 |
| 171 | P23 Dispatch Yard · 7 — Ship D3 | DP-26 |

### Phase P24 — Plan Room · D3 (days 172–179)

| Day | Title | IDs closed |
| --- | --- | --- |
| 172 | P24 Plan Room · 1 — The kit | FN-26 |
| 173 | P24 Plan Room · 2 — The boundary: `plan_mcp`, the plan store | MC-39 |
| 174 | P24 Plan Room · 3 — Plan and execute | AG-28 |
| 175 | P24 Plan Room · 4 — The plan as data, not prose | AG-29 |
| 176 | P24 Plan Room · 5 — Decomposition: subgoals that are actually separable | AG-30 |
| 177 | P24 Plan Room · 6 — Replanning on failure | AG-31 |
| 178 | P24 Plan Room · 7 — What planning costs, in tokens | RS-11 |
| 179 | P24 Plan Room · 8 — Ship D3: the plan that never ends, and the bound that stops it | RS-12, DP-27 |

### Phase P25 — Swarm Limits · D4 (days 180–186)

| Day | Title | IDs closed |
| --- | --- | --- |
| 180 | P25 Swarm Limits · 1 — The kit | FN-27 |
| 181 | P25 Swarm Limits · 2 — The boundary: `desk_mcp` | MC-40 |
| 182 | P25 Swarm Limits · 3 — Shared state under concurrency: the last writer wins, and should not | AG-32 |
| 183 | P25 Swarm Limits · 4 — The boundary under contention: six clients, one server | RS-13 |
| 184 | P25 Swarm Limits · 5 — The cost of coordination: when six agents are slower than one | RS-14 |
| 185 | P25 Swarm Limits · 6 — Containment: the swarm that would not stop | RS-15 |
| 186 | P25 Swarm Limits · 7 — Ship D4 | DP-28 |

### Phase P26 — Never Lose Work · D4 (days 187–194)

| Day | Title | IDs closed |
| --- | --- | --- |
| 187 | P26 Never Lose Work · 1 — The kit | FN-28 |
| 188 | P26 Never Lose Work · 2 — The boundary: `job_mcp`, the checkpoint store | MC-41 |
| 189 | P26 Never Lose Work · 3 — Durable execution, plainly | RS-16 |
| 190 | P26 Never Lose Work · 4 — Idempotency keys: the email sent twice | RS-17 |
| 191 | P26 Never Lose Work · 5 — Checkpoints | RS-18 |
| 192 | P26 Never Lose Work · 6 — Pause and resume | RS-19 |
| 193 | P26 Never Lose Work · 7 — Replay and determinism: the tool that is not | RS-20 |
| 194 | P26 Never Lose Work · 8 — Ship D4: delete the pod mid-run; it finishes | DP-29 |

### Phase P27 — Approval Gate · D4 (days 195–201)

| Day | Title | IDs closed |
| --- | --- | --- |
| 195 | P27 Approval Gate · 1 — The kit | FN-29 |
| 196 | P27 Approval Gate · 2 — The boundary: every write operation behind it | MC-42 |
| 197 | P27 Approval Gate · 3 — What needs a human: blast radius before capability | SC-15 |
| 198 | P27 Approval Gate · 4 — Building the gate | SC-16 |
| 199 | P27 Approval Gate · 5 — Human-in-the-loop resumption for standalone nodes | AG-33 |
| 200 | P27 Approval Gate · 6 — The audit trail: who approved what, and when | SC-17 |
| 201 | P27 Approval Gate · 7 — Ship D4: the gate that got bypassed, and how | DP-30 |

### Phase P28 — Injection Range · D4 (days 202–210)

| Day | Title | IDs closed |
| --- | --- | --- |
| 202 | P28 Injection Range · 1 — The kit | FN-30 |
| 203 | P28 Injection Range · 2 — The boundary: a deliberately hostile `feed_mcp` | MC-43 |
| 204 | P28 Injection Range · 3 — A threat model for agents | SC-18 |
| 205 | P28 Injection Range · 4 — Prompt injection, shown and not told | SC-19 |
| 206 | P28 Injection Range · 5 — Injection through a tool result: the boundary as attack surface | SC-20 |
| 207 | P28 Injection Range · 6 — The lethal trifecta | SC-21 |
| 208 | P28 Injection Range · 7 — Input guardrail callbacks | SC-22 |
| 209 | P28 Injection Range · 8 — Output guardrails: the exfiltration you did not see | SC-23 |
| 210 | P28 Injection Range · 9 — Ship D4: the red-team evalset your desk survives | EV-10, DP-31 |

### Phase P29 — Least Privilege · D4 (days 211–216)

| Day | Title | IDs closed |
| --- | --- | --- |
| 211 | P29 Least Privilege · 1 — The kit | FN-31 |
| 212 | P29 Least Privilege · 2 — The boundary: `vault_mcp` with scoped credentials | MC-44 |
| 213 | P29 Least Privilege · 3 — Per-agent tool permissions | SC-24 |
| 214 | P29 Least Privilege · 4 — Scoped MCP credentials and capability tokens | SC-25 |
| 215 | P29 Least Privilege · 5 — The privilege review: what a reviewer asks | SC-26 |
| 216 | P29 Least Privilege · 6 — Ship D4: the agent that escalated, caught by a test | DP-32 |

### Phase P30 — Sandbox Yard · D4 (days 217–223)

| Day | Title | IDs closed |
| --- | --- | --- |
| 217 | P30 Sandbox Yard · 1 — The kit | FN-32 |
| 218 | P30 Sandbox Yard · 2 — The boundary: `range_mcp`, a local dummy site | MC-45 |
| 219 | P30 Sandbox Yard · 3 — Code execution, and why it is a different kind of tool | TL-16 |
| 220 | P30 Sandbox Yard · 4 — Sandboxing: the concept, then the boundary | SC-27 |
| 221 | P30 Sandbox Yard · 5 — Execution isolation in practice | SC-28 |
| 222 | P30 Sandbox Yard · 6 — Computer use against a range you own | TL-17 |
| 223 | P30 Sandbox Yard · 7 — Ship D4: the runaway, contained | DP-33 |

### Phase P31 — Quota Router · D4 (days 224–229)

| Day | Title | IDs closed |
| --- | --- | --- |
| 224 | P31 Quota Router · 1 — The kit | FN-33 |
| 225 | P31 Quota Router · 2 — The boundary: `quota_mcp`, the ledger | MC-46 |
| 226 | P31 Quota Router · 3 — The quota ledger: requests remaining, per provider, per window | RS-21 |
| 227 | P31 Quota Router · 4 — The router plugin: send the cast to headroom | RS-22 |
| 228 | P31 Quota Router · 5 — Escalation and the runbook | RS-23 |
| 229 | P31 Quota Router · 6 — Ship D4: exhaust a provider on purpose | DP-34 |

### Phase P32 — Night Shift · D4 (days 230–235)

| Day | Title | IDs closed |
| --- | --- | --- |
| 230 | P32 Night Shift · 1 — The kit | FN-34 |
| 231 | P32 Night Shift · 2 — The boundaries: `archive_mcp` and `report_mcp` | MC-47 |
| 232 | P32 Night Shift · 3 — Ambient agents: nobody typed anything | AG-34 |
| 233 | P32 Night Shift · 4 — Scheduled runs, and the CronJob | DP-35 |
| 234 | P32 Night Shift · 5 — Quota-aware scheduling: the job that ran at the wrong hour | RS-24 |
| 235 | P32 Night Shift · 6 — Ship D4: the digest someone would actually act on | DP-36 |

### Phase P33 — Watch Tower · D4 (days 236–241)

| Day | Title | IDs closed |
| --- | --- | --- |
| 236 | P33 Watch Tower · 1 — The kit | FN-35 |
| 237 | P33 Watch Tower · 2 — The boundary: `event_mcp` | MC-48 |
| 238 | P33 Watch Tower · 3 — Event-driven intake: webhooks, and the retry you did not ask for | DP-37 |
| 239 | P33 Watch Tower · 4 — Deduplication: the same event, four times | RS-25 |
| 240 | P33 Watch Tower · 5 — Idempotent intake | RS-26 |
| 241 | P33 Watch Tower · 6 — Ship D4 | DP-38 |

### Phase P34 — Voice Standup · D3 (days 242–249)

| Day | Title | IDs closed |
| --- | --- | --- |
| 242 | P34 Voice Standup · 1 — The kit | FN-36 |
| 243 | P34 Voice Standup · 2 — The boundary: `queue_mcp` | MC-49 |
| 244 | P34 Voice Standup · 3 — The Live API: the streaming architecture | AG-35 |
| 245 | P34 Voice Standup · 4 — The bidirectional loop | AG-36 |
| 246 | P34 Voice Standup · 5 — Audio in, audio out; the free-quota check and the fallback | RS-27 |
| 247 | P34 Voice Standup · 6 — Voice activity events: knowing when they stopped talking | AG-37 |
| 248 | P34 Voice Standup · 7 — Non-blocking tools: the conversation that must not freeze | TL-18 |
| 249 | P34 Voice Standup · 8 — Ship D3 | DP-39 |

### Phase P35 — Eval Bench · D5 (days 250–257)

| Day | Title | IDs closed |
| --- | --- | --- |
| 250 | P35 Eval Bench · 1 — The kit | FN-37 |
| 251 | P35 Eval Bench · 2 — The boundary: `evalset_mcp` | MC-50 |
| 252 | P35 Eval Bench · 3 — Evals are tests: the change that made it worse | EV-11 |
| 253 | P35 Eval Bench · 4 — Evalsets and metrics | EV-12 |
| 254 | P35 Eval Bench · 5 — The eval workhorse: a cheap model judging a cheap model | EV-13 |
| 255 | P35 Eval Bench · 6 — Trajectory evaluation: the right answer by the wrong route | EV-14 |
| 256 | P35 Eval Bench · 7 — Rubric-based multi-turn trajectory evaluation | EV-15 |
| 257 | P35 Eval Bench · 8 — Ship D5: the judge, and the honest baseline | EV-16, DP-40 |

### Phase P36 — Regression Gate · D5 (days 258–264)

| Day | Title | IDs closed |
| --- | --- | --- |
| 258 | P36 Regression Gate · 1 — The kit | FN-38 |
| 259 | P36 Regression Gate · 2 — The boundaries: `evalset_mcp` and `metrics_mcp` | MC-51 |
| 260 | P36 Regression Gate · 3 — Evals in CI: the pipeline that says no | EV-17 |
| 261 | P36 Regression Gate · 4 — Cost guards: the eval that passed and cost triple | RS-28 |
| 262 | P36 Regression Gate · 5 — Latency guards: p95, not the mean | EV-18 |
| 263 | P36 Regression Gate · 6 — Flaky evals, and the threshold you will be tempted to lower | EV-19 |
| 264 | P36 Regression Gate · 7 — Ship D5: a regression blocked with nobody deciding | DP-41 |

### Phase P37 — Glass Box · D5 (days 265–271)

| Day | Title | IDs closed |
| --- | --- | --- |
| 265 | P37 Glass Box · 1 — The kit | FN-39 |
| 266 | P37 Glass Box · 2 — The boundary, instrumented | MC-52 |
| 267 | P37 Glass Box · 3 — OpenTelemetry and the auto-tracing plugin | EV-20 |
| 268 | P37 Glass Box · 4 — The trace tree across three agents and two boundary hops | EV-21 |
| 269 | P37 Glass Box · 5 — Debugging slow, not broken | EV-22 |
| 270 | P37 Glass Box · 6 — The span that was missing: instrumenting your own boundary | EV-23 |
| 271 | P37 Glass Box · 7 — Ship D5 | DP-42 |

### Phase P38 — Blue Green · D5 (days 272–278)

| Day | Title | IDs closed |
| --- | --- | --- |
| 272 | P38 Blue Green · 1 — The kit | FN-40 |
| 273 | P38 Blue Green · 2 — The boundary, in two colours | MC-53 |
| 274 | P38 Blue Green · 3 — The API surface: `api_server` and the endpoints around it | DP-43 |
| 275 | P38 Blue Green · 4 — The manifest set, whole | DP-44 |
| 276 | P38 Blue Green · 5 — Blue and green: two deployments, one service | DP-45 |
| 277 | P38 Blue Green · 6 — Auto-rollback: the health signal that decides | DP-46 |
| 278 | P38 Blue Green · 7 — Ship D5: roll forward into a bad build, watch it roll back | DP-47 |

### Phase P39 — Peer Network · D5 (days 279–285)

| Day | Title | IDs closed |
| --- | --- | --- |
| 279 | P39 Peer Network · 1 — The kit | FN-41 |
| 280 | P39 Peer Network · 2 — The boundary, plus signed cards | MC-54 |
| 281 | P39 Peer Network · 3 — A2A: signed agent cards, verified hands-on | DP-48 |
| 282 | P39 Peer Network · 4 — Agent-as-peer against agent-as-tool, decided | AG-38 |
| 283 | P39 Peer Network · 5 — Agent identity and the registry | SC-29 |
| 284 | P39 Peer Network · 6 — The agent economy, parked: payment and trust protocols | DP-49 |
| 285 | P39 Peer Network · 7 — Ship D5: the peer whose card fails verification | SC-30 |

### Phase P40 — The Desk · D5 · capstone (days 286–296)

| Day | Title | IDs closed |
| --- | --- | --- |
| 286 | P40 The Desk · 1 — The kit | FN-42 |
| 287 | P40 The Desk · 2 — The boundary day: three servers stood up | MC-55 |
| 288 | P40 The Desk · 3 — The cast: six agents, and why not four or nine | AG-39 |
| 289 | P40 The Desk · 4 — What each boundary owns, and the line between them | MC-56 |
| 290 | P40 The Desk · 5 — Memory and retrieval inside the graph | MR-16 |
| 291 | P40 The Desk · 6 — Durability, and the gate on every external write | RS-29 |
| 292 | P40 The Desk · 7 — The security pass: injection, privilege, PII, synthetic-only | SC-31 |
| 293 | P40 The Desk · 8 — Evals: the full set, and the one that must be able to fail | EV-24 |
| 294 | P40 The Desk · 9 — Traced, containerised, blue and green | DP-50 |
| 295 | P40 The Desk · 10 — The cold run: no edits, no retries, recorded | DP-51 |
| 296 | P40 The Desk · 11 — Repository public; the demo script; the interview drill over every ADR | RB-04 |

<!-- granth:day-map:end -->

---

## §18 · Amendment record

This plan is amended, never quietly edited. Every amendment lands in `docs/CHANGELOG_PLAN.md`
before any day or any code changes, and anything structural gets an ADR in `docs/adr/`.

| Version | Date | What changed |
| --- | --- | --- |
| v3.0.0 | 2026-09-07 | `_shared/` deleted; forty independent repositories; 296 sittings. Adopted as written. |
| v3.1.0 | 2026-09-08 | Adoption for the `./p` toolchain: §14 to §18 added, the tracks, phases and day map made machine-readable, 310 concept IDs assigned, day 0 inserted. `sitting_minutes` removed from the §4.1 hub frontmatter. See `docs/adr/ADR-0001-the-plan-as-adopted.md` and `docs/adr/ADR-0002-day-zero-and-the-authoring-repo.md`. |
