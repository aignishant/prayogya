| plan | prayoga |
| --- | --- |
| version | v3.0.0 |
| supersedes | v2.0.0 (40 projects sharing `_shared/`) |
| projects | 40 · **each one a standalone repository** |
| days | 296 · one sitting each |
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
