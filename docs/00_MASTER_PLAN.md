---
plan: prayoga
version: "v4.0.0"
topic: "40 independent agentic systems with Google ADK 2.x, MCP, Agent Skills and A2A"
projects: 40
optional_projects: 1
days: 816
doc_architecture: "hub + parts/ (see §4 and §5)"
amended: "2026-09-10"
---

| plan | prayoga |
| --- | --- |
| version | **v4.0.0** |
| supersedes | v3.1.0 — same subject, opposite rule about repetition |
| projects | 40 · **each one a standalone repository, taught from zero** |
| optional | P00 Foundry, 5 sittings · no project references it, no project needs it |
| days | 811 project sittings + 5 optional = **816** |
| sitting budget | 60 minutes |
| rule 1 | **every project is complete alone — code *and* teaching** |
| rule 2 | **every concept a project uses is taught in that project, at full depth** |
| rule 3 | **every project starts on a bare machine, at day 0** |
| rule 4 | **every project ships the whole agent feature set** |
| doc architecture | 4 project documents + hub + RECALL + `parts/` |

# MASTER PLAN v4.0.0 — **Prayoga**

## 40 independent agentic systems with **Google ADK 2.x · MCP · Agent Skills · A2A**

---

## §0 · The four rules, and why v3 was wrong

v3 deleted the shared code library and thought that made projects independent. It made the *code*
independent and left the *teaching* dependent, which is the half that matters to a reader. v3's own
Depth Rule said a concept is taught deeply in exactly one place and everywhere else gets "recap
depth — a short table, one line per function". A table is not a teaching. v3 then invented
`PRIMER.md`, six to ten lines per borrowed idea, to patch the hole; the patch's existence was the
proof of the hole. And the scaffolding that decides whether a stranger's clone runs at all — git,
the `.gitignore` written before `.env` exists, the interpreter pin, the key handling — lived in a
project nobody was required to read.

**v4 makes independence mean what it says.** Four rules, in this order of precedence.

> ### 1. The Completeness Rule — code is never referenced, only printed
> Every line of code a project needs appears **in full, at its real path, inside that project's own
> day documents.** That includes `.gitignore`, `pyproject.toml`, `.env.example`, `Dockerfile`,
> `compose.yaml`, the CI workflow and the `run` driver — the files that decide whether a clone runs
> at all. No `...`, and no "the rest is unchanged" unless the unchanged region was printed earlier
> **in this same project** and the day says which day printed it. **If a file exists in the
> finished project, some day in that project printed it whole.**

> ### 2. The Repetition Rule — every concept is taught here, in full
> Every concept a project uses is taught in **that project**, at full depth: the scene, the
> mechanism, the line-by-line walkthrough, the real failure text, the production note. **There is
> no recap depth and no "taught deeply elsewhere."** If forty projects need honest 429 handling,
> honest 429 handling is taught forty times — and the fortieth telling is the better one, because
> it has thirty-nine domains of evidence behind it. Repetition between projects is **required**,
> not tolerated.

> ### 3. The From-Scratch Rule — every project starts on a bare machine
> Day 0 of every project assumes nothing: it checks the toolchain, pins the interpreter, runs
> `git init`, writes `.gitignore` **before** any secret exists, handles the keys, and reaches a
> green check on an empty system. Day 1 builds the skeleton and the kit. **No project may assume a
> machine another project prepared**, and no project's setup step may read "as in the foundry
> project".

> ### 4. The Full-Stack Rule — every project ships the whole feature set
> Tools, its own MCP boundary, a multi-agent cast, callbacks and plugins, sessions and memory,
> structured output, reliability, security, observability, evals, deploy. A project that omits a
> subsystem because another project covers it is the v3 failure wearing a new costume. **§12 fixes
> the eighteen subsystems as a spine every project builds.**

**And the rule that makes the four checkable: nothing leaves the project.** No day document,
checklist, docstring, README or commit message inside `projects/<NN-name>/` may reference another
project — not by path, not by name, not as "as we saw in P03". `python p.py check` fails on it. See
§6.

The test that decides whether a project is finished: **`python p.py verify NN` copies only that
project's folder to a directory outside this repository and runs its own `./run check` there.** It
is isolation from the curriculum, not from the machine — the stronger test is the cold clone that
ends every project (§7). A project that fails either is not written, however good its prose is.

What this costs is in §16, stated as a number. It was shown and accepted before the rewrite began.

---

## §1 · What a project folder contains

A project is a repository. It is complete on its own, it has its own git history, and it has no
parent.

```
projects/05-contract-review-bench/     ← take this folder anywhere; it runs, and it teaches
│
├── README.md              # a stranger's entry point: what it is, how to run it, what it needs
├── PROJECT.md             # the brief, the triad, the feature-set table (§2.2)
├── SETUP.md               # bare machine to green check, copy-pasteable, nothing assumed (§2.3)
├── CODEMAP.md             # every file in the finished project → the day that prints it (§2.4)
│
├── day-00-machine-and-repository/     # THE TEACHING — numbered inside this project, from 0
│   ├── LESSON.md · RECALL.md · CHECKLIST.md
│   ├── parts/01-<slug>/1.1-<slug>.md …
│   └── lab/
├── day-01-skeleton-and-kit/
├── … day-20-ship/
│
├── run                    # this project's own driver: ./run check | serve | mcp | eval | up
├── pyproject.toml         # its own pins. Not shared, not inherited.
├── uv.lock · .python-version
├── .env.example · .gitignore
├── Dockerfile · compose.yaml · .github/workflows/   # its own deploy and CI files
│
├── clause_desk/           # the agents, tools, cast — every line typed from this project's days
│   ├── agents/ · tools/ · util/       #   util/ holds THIS project's backoff, budget, logging
│   └── main.py
├── clause_mcp/            # this project's own MCP server. Not a library. Its own code.
└── tests/ · evals/
```

**There is no `_shared/`, no `adk_kit`, no `PRIMER.md`, no parent `pyproject.toml`, and no root
driver a project depends on.** The top-level `python p.py` is an **authoring tool only** (§7): it
writes, checks and verifies the documents. Nothing inside a project imports it, reads it, or needs
it to exist.

`clause_desk/util/backoff.py` and `field_desk/util/backoff.py` are the same idea and separate
files with separate lives. Improving one does not change the other. That is the price of
independence and it is the correct price.

---

## §2 · The four project documents

v3 had five. `PRIMER.md` is gone: it existed only to make a pointer into another project
survivable, and there are no such pointers now (ADR-0006).

### 2.1 `README.md` — the stranger's entry point

Written for someone who has this folder and nothing else, and has never heard of this curriculum.
Six sections: what this system does · what you need installed · the four commands to run it · the
architecture in one Mermaid diagram · where the teaching starts (`day-00-…/LESSON.md`) · what is
deliberately not built 🅿️.

### 2.2 `PROJECT.md` — the brief, the triad and the feature-set table

```markdown
# P05 · Contract Review Bench
**Industry.** Legal — commercial contract review.
**What it is.** A bench that reads a synthetic master services agreement, finds the clauses that
depart from a house playbook, drafts redlines with citations back to the source paragraph, and
fails its own eval when a citation points at a paragraph that does not contain the quoted text.
**Days.** 21 · **Deploy tier.** D3 · **Depends on nothing, and references nothing.**

## The triad
| Leg | This project |
| --- | --- |
| **Tools** | `fetch_clause(id)` · `search_playbook(query, k)` · `score_departure(clause, rule)` · `draft_redline(clause, rule)` |
| **MCP boundary** | `clause_mcp/` — owns the document store and the playbook index; no agent touches a file |
| **Cast** | `router` → `retriever` ‖ `clause_finder` → `redliner` → `critic` |

## The feature set — every one taught here, in full (§12)
| Subsystem | Where this project teaches it | The failure it prevents here |
| --- | --- | --- |
| Toolchain & secrets | day 0 | a key in git history, and a clone that will not start |
| The kit | day 1 | four call sites each retrying differently |
| … one row per spine slot … | | |

**Done when.** A cold clone reviews a twelve-clause agreement, flags the four planted departures,
cites each one to a paragraph that really contains the quoted words, and `citation_precision`
goes red the moment quote-checking is disabled.
```

There is **no "borrowed concepts" table**. Nothing is borrowed. The feature-set table is its
replacement, and it points *inward* — every row names a day in this project.

### 2.3 `SETUP.md` — bare machine to green check

Every command from a machine with nothing on it to a green `./run check`: install `uv`, pin Python,
`git init`, `uv init`, the exact `uv add pkg==version` lines with the date each was verified,
`cp .env.example .env`, which free keys are needed and where to get them, `./run check`.
**No step may reference another project, and no step may be "as you did before".** Roughly 50 lines,
mostly commands. It is a listing; day 0 is the lesson behind it, in the same folder.

### 2.4 `CODEMAP.md` — the completeness proof

Generated by `python p.py codemap NN`. Every file in the finished project, and the day and part
that prints it whole.

```
clause_desk/util/backoff.py         day-01-skeleton-and-kit/parts/03-resilience/3.1-backoff.md
clause_mcp/server.py                day-03-boundary-server/parts/01-server/1.2-server.md
clause_mcp/index.py                 day-11-memory-and-retrieval/parts/02-building/2.2-index.md
clause_desk/agents/critic.py        day-16-evals/parts/01-rubric/1.3-critic.md
.gitignore                          day-00-machine-and-repository/parts/02-secrets/2.1-gitignore.md
```

**A file with no day fails `python p.py check`.** This one table is what makes rule 1 mechanical
instead of aspirational, and it is why `.gitignore` and `Dockerfile` are on it.

---

## §3 · What a day is

**One sitting of about sixty minutes:**

| Slice | What |
| --- | --- |
| Read | 2–5 parts, one idea each |
| Build | type the code the parts printed; `TODO(me)` markers stay unsolved |
| Break it | the day's deliberate failure; watch the check go red |
| Close | tick the checklist, write `RECALL.md`, commit |

A subject that will not fit in one sitting **becomes two days**. It is never compressed, and the
clock never appears in a day document (§15).

Every day has at least one deliberate failure. A day whose check never went red is not finished.

**Days are numbered inside their project, from 0.** P01 runs day 0 to day 19. P02 starts again at
day 0. There is no global sitting number, because there is no global reading order: a reader may
start at project 27. See §15.

---

## §4 · The three documents in a day

### 4.1 `LESSON.md` — the hub

| § | Section | Contains |
| --- | --- | --- |
| fm | frontmatter | `project`, `day`, `title`, `spine`, `parts`, `deploy_tier`, `files_printed`, `plan_version`, `status`, `commit` |
| — | yesterday / today / tomorrow | one line each, inside this project only |
| §1 | The scene | the day's whole idea as one scene from **this project's industry**, plain words, no jargon |
| §2 | The map | every part: number, linked title, what it answers, `level` |
| §3 | Setup — run this | every `mkdir`, `touch`, `uv add pkg==exact`, verified that day |
| §4 | Files this day prints | the paths, and which part prints each. Feeds `CODEMAP.md` |
| §5 | Build brief | what you type; `TODO(me)` unsolved |
| §6 | The check that must be able to fail | RED before the TODOs are done |
| §7 | Request budget | per-turn model calls per provider, **counted across the whole cast** |
| §8 | Traps | the mistakes that eat the sitting, including the named 1.x→2.x traps |
| §9 | Verified today | live documentation URLs actually fetched, with the date |
| §10 | Ledger & commit | the `PROGRESS.md` row and the commit message, verbatim |

**The hub never teaches.** No `**Line by line:**` anywhere in it.

### 4.2 `RECALL.md` — one page, written last

One-line summary · what I built · three things worth remembering · the failure I caused, with the
real error string · the command that proves it still works · the interview paragraph · what it
depends on. Never longer than a screen.

### 4.3 `CHECKLIST.md`

The definition of done. `python p.py done NN D` refuses until every box is ticked, the ledger row
exists and the checks are green.

---

## §5 · The part contract — 8 sections

| # | Section | The rule |
| --- | --- | --- |
| 1 | **frontmatter** | `project`, `day`, `part`, `title`, `spine`, `level`, `prints` (file paths), `failure`, `prev`, `next` |
| 2 | **One-line answer** | The claim in one sentence. |
| 3 | **The idea** | A concrete scene you could have stood in, **from this project's industry** — a loss adjuster with a photograph, a night-shift supervisor with a jammed line. **No jargon in the first paragraph.** Then the concept, terms defined on first use, the scene still holding the failure the part teaches. **No code.** One metaphor family per day. |
| 4 | **The mechanism** | **Real code from this project.** See §5.1. |
| 5 | **Line by line** | Follows every code block. **Full depth, always** — see §5.2. |
| 6 | **When it breaks** | The real error text **verbatim**, then two to four sentences: someone shipped this on a Friday, here is what they saw at 11pm, here is the smallest fix. |
| 7 | **In production** | Four beats: what a senior writes **instead** · what degrades at scale, **with a number** · the review comment · the interview question. One real example. Not optional. |
| 8 | **Check yourself** | One command to run now, plus one question answered **out loud**. |

### 5.1 The mechanism section — the rule, stated hard

**Real code, and these five constraints are what make that mean something:**

1. **Real path, real project.** The block is headed with the file's actual path in *this* project —
   `clause_mcp/server.py`, never `server.py` and never `# in your MCP server`.
2. **Whole file, or a marked diff against a version this project already printed.**
   `# ── unchanged from day 03 part 1.2 ──` is legal. `# ... rest of implementation ...` is not.
3. **No import from outside this project.** If it needs a helper, this project printed the helper.
4. **Runnable as printed.** Imports at the top, no invented API, verified against the live
   documentation on the day. If it needs a key, the `.env.example` line is in the same day.
5. **The output is real.** The block showing what it prints was actually run. If it could not be
   run, the block is `TODO(me): run <exact command>` — **never an invented transcript.** A missing
   output is fixed by one run; a fabricated one is undetectable.

### 5.2 `Line by line` has one depth, and it is full

v3 had two depths and the shallow one is deleted. **Every code block in every project gets the full
walkthrough**: every non-obvious token, and *why that line and not another*, as prose bullets under
the block. The recap table — one row per line, naming the failure it prevents — survives only as an
**additional summary a part may offer after the prose**, never as a substitute for it.

`python p.py depth` fails a part whose code block has no walkthrough under it. It no longer fails a
part for teaching deeply what another part teaches deeply. **That is now the point.**

### 5.3 The three unnumbered rules

- **One idea per document.** If the part needs "also" to introduce its second half, split it.
- **Standalone.** Readable cold. It names and links its prerequisite **inside this project**, and
  never says "as we saw".
- **No shortcut.** "For now, just accept that" is banned unless it links forward to the part in
  this project that explains it.

**Levels:** `foundation` → `working` → `production`. A day climbs.

---

## §6 · Nothing leaves the project

There is no pointer format, because there are no pointers out.

Inside a project, a part may link freely to any other document in the same project, by relative
path. Outside it, nothing:

- no path containing `projects/<other>/` or `days/<other>/`;
- no "see P03", "as taught in Parts Counter", "the deep version is in";
- no import, in any file, that resolves outside the project;
- no `SETUP.md` step that references another project;
- no commit message naming another project.

`python p.py check` greps for all of it and fails. **This is the load-bearing half of ADR-0006:**
without the mechanical check the rule is a preference, and preferences drift by project six.

The one document allowed to know the whole curriculum is this plan, plus the generated indexes in
`docs/`. They are authoring tools. **No project needs any of them to be buildable or readable.**

---

## §7 · Verification — how independence is proved, not claimed

The authoring driver is `python p.py`, and it never builds, serves, tests or deploys a project.

```
python p.py brief NN D     # the day-D-of-project-NN assignment, and the order guard
python p.py new NN D slug  # scaffold an empty day from days/_TEMPLATES/
python p.py depth NN [D]   # the depth contract for one day, or the whole project
python p.py codemap NN     # regenerate that project's CODEMAP.md from the day hubs
python p.py index          # regenerate the derived documents in docs/
python p.py check          # the whole-repository gate, including the no-escape grep of §6
python p.py verify NN      # independence: copy the project out on its own, run its own check
python p.py done NN D      # finish a day: refuses on an unticked checklist, then commits
python p.py doctor         # is this repository wired correctly?
```

**What `verify` proves, and what it does not.** It copies only `projects/<NN-name>/` to a directory
outside this repository, greps every file in the copy for a reference that leaves the project (§6),
and runs the copy's own `./run check`. So it fails on:

- any reference leaving the project — a path, a project name, a phrase that assumes another folder;
- a project with no `run` driver of its own;
- `./run check` red once the project stands alone.

It shares this machine's interpreter, its caches and its network, so it **does not** prove the
project builds on a machine that has nothing. Only the cold clone does, and that is why every
project ends with one:

**Every project's last day is the cold-clone day**: wipe the working copy, clone the folder alone,
follow the README on a machine that has nothing, and record the real output in the day document. A
project whose cold clone was never run is not finished. The two gaps `verify` cannot see —
a `SETUP.md` step that assumes a prepared machine, and a file in the tree that no day printed —
are what the cold clone and `CODEMAP.md` are for.

Inside a project the driver is `./run`, and it has no dependency outside the project:

```
./run check     # ruff + format + tests + evals at current scope
./run serve     # the agent API on :8080
./run mcp       # the boundary server
./run up        # compose: agents + boundary together
./run eval      # the evalset
./run done      # refuses unless the day's checklist is ticked and check is green, then commits
```

---

## §8 · Deploy — per project, no shared folder

Each project carries its own `Dockerfile`, `compose.yaml`, CI workflow and, at D4, its own `k8s/`.
All of them are **printed in full** in that project's own ship day.

Under the Full-Stack Rule every project reaches **at least D3 and a CI eval gate**. The tier column
in §11 says how much further a project goes, and it goes further only when its subject demands it —
a project that teaches contention needs replicas to contend.

| Tier | What it is | Which projects |
| --- | --- | --- |
| **D3** | `api_server` + `/healthz`, a stateless container, compose with the **MCP sidecar**, CI running the evalset | every project — the floor |
| **D4** | kind/k3d: deployment, service, secret, CronJob, and a pod killed mid-run | the projects whose subject is scale, durability, isolation or scheduled work |
| **D5** | eval-gated CI with cost and latency guards, blue/green with auto-rollback | the projects whose subject is release, observability, judgement or interop |

**The D5 test the capstone defends:** a prompt change must be blocked by the pipeline when it makes
the system worse, and must reach a live endpoint when it does not, without a human deciding which
of those two happened.

Cloud walkthroughs are **written and configured, never billed** — the config file is the
deliverable, marked 🅿️.

---

## §9 · Model & budget policy — $0, by construction

- **Gemini Flash-class** on a free AI Studio key is the primary brain. The AI Studio path is
  configured by `GOOGLE_API_KEY` alone; no day writes `GOOGLE_GENAI_USE_VERTEXAI`, which is absent
  from the framework's current documentation (ADR-0004).
- **Groq** is the speed lane; **OpenRouter models ending in `:free`** are the breadth lane (the
  suffix is linted per project); **Ollama** is the offline baseline.
- **Every agent pins its model explicitly**, as an exact ID and never a `-latest` alias, which the
  provider documents as hot-swapped on every release. ADK 2.x's built-in default is
  `gemini-3.5-flash` — Stable, and the provider's own "legacy Flash model", four generations behind
  the current one. An unpinned agent is silently stale rather than silently experimental, and with
  three agents that is three silent bugs (ADR-0004).
- **Each project pins independently**, in its own `PACKAGES.md`: package, version, date verified,
  and the day that pinned it. Two projects may legitimately sit on different pins; that is what
  independence means, and §10 is where the newer one wins.
- **Multi-agent multiplies quota.** A three-agent turn is at least three requests; a writer↔critic
  loop is unbounded until you bound it. Every hub's §7 states the per-turn count **across the whole
  cast**. It does not state the provider's RPM/TPM/RPD: those were withdrawn from publication, so
  the ceiling is a `TODO(me)` naming where to read it rather than a number nobody can verify
  (ADR-0004).
- **Every call path handles HTTP 429 honestly:** `Retry-After`, back off, escalate. Never fabricate
  a result to cover an error.
- **All data is synthetic, always** — every project, every fixture, every eval.
- **A stand-in model is legal and must announce itself.** A scripted `BaseLlm` subclass that
  replays a fixed script makes a day reproducible with no key and no cost. It says so in its own
  docstring and names itself `scripted/...` in every transcript it produces, so nothing it emits
  can be mistaken for a provider response.

---

## §10 · Freshness — at the start of a project, not daily

Projects are independent, so the check moved to the front: you pin at the start and live with it
for sixteen to twenty-two sittings.

1. `google-adk` release notes since your last project — breaking change? **Amend this plan first.**
2. MCP specification revision moved? Every project has a boundary, so this always matters. ADR-0005
   records the standing gap: the current revision is `2026-07-28`, which removed the `initialize`
   handshake and protocol-level sessions, and `google-adk` 2.8.0 declares `mcp<2`. Re-read it; do
   not assume the ADR is still current.
3. Provider free lists re-checked; anything that lost its free tier is repinned before day 0.
4. **Write this project's full day map** — expand §12's spine with §13's inserts, adjust the titles
   to this project's domain, and record it in the project's own `PROJECT.md`. A change to the
   *number* of days is a plan amendment (§13); a change to a title is not.
5. Record all of it in this project's `PACKAGES.md`, dated.

---

## §11 · The forty projects

Eight tracks of five. **Every project has the whole feature set, its own repository, its own deploy
files, and its own teaching from zero.** The Days column is authoritative and equals 18 spine days
(§12) plus that project's inserts (§13).

<!-- granth:projects:start -->

| # | Project | Industry | Days | Tier |
| --- | --- | --- | --- | --- |
| 00 | Foundry *(optional primer — no project references it, no project needs it)* | — | 5 | — |
| **A** | **Intake, classification and the decision that must be defensible** | | | |
| 01 | Claims Intake Desk | Insurance — first notice of loss | 20 | D3 |
| 02 | Warehouse Stock Control | Logistics — warehouse management | 20 | D3 |
| 03 | Clinical Triage Room | Healthcare — symptom triage and escalation | 21 | D3 |
| 04 | Loan Underwriting Desk | Retail finance — credit decisions | 20 | D3 |
| 05 | Contract Review Bench | Legal — commercial contract review | 21 | D3 |
| **B** | **The data boundary as a system of record** | | | |
| 06 | Plant Floor Supervisor | Manufacturing — line supervision | 20 | D4 |
| 07 | Field Service Inspector | Utilities — field inspection and reporting | 20 | D3 |
| 08 | Fleet Dispatch Yard | Road transport — dispatch and routing | 21 | D3 |
| 09 | Grid Watch Room | Energy — grid telemetry and alarms | 20 | D4 |
| 10 | Patient Records Abstractor | Healthcare — clinical coding and privacy | 20 | D4 |
| **C** | **Documents, knowledge and retrieval you can cite** | | | |
| 11 | Tender Bid Assembler | Procurement — public tender response | 20 | D3 |
| 12 | Research Librarian | Pharmaceutical R&D — literature search | 21 | D3 |
| 13 | Invoice Reconciliation Clerk | Accounts payable — three-way match | 20 | D4 |
| 14 | Fraud Watch Floor | Payments — real-time fraud review | 21 | D4 |
| 15 | Tax Filing Assistant | Accounting — return preparation | 19 | D3 |
| **D** | **Judgement, disagreement and the human in the loop** | | | |
| 16 | Market Research Analyst | Capital markets — research synthesis | 20 | D3 |
| 17 | Collections Outreach Desk | Consumer lending — arrears contact | 19 | D3 |
| 18 | Employee Onboarding Coordinator | Human resources — onboarding | 20 | D3 |
| 19 | Shift Roster Planner | Workforce operations — rostering | 20 | D3 |
| 20 | Recruiting Screener | Human resources — candidate screening | 20 | D5 |
| **E** | **Operations, incidents and things that run unattended** | | | |
| 21 | IT Helpdesk Night Shift | IT service management — unattended triage | 19 | D4 |
| 22 | Incident Commander | Site reliability — incident response | 21 | D5 |
| 23 | Retail Personal Shopper | E-commerce — assisted selling | 19 | D3 |
| 24 | Hotel Front Desk | Hospitality — booking and rebooking | 20 | D3 |
| 25 | Restaurant Order Line | Food service — voice ordering | 20 | D3 |
| **F** | **Identity, adversaries and least privilege** | | | |
| 26 | Bank Branch Concierge | Retail banking — authenticated service | 20 | D4 |
| 27 | Airline Rebooking Desk | Air travel — disruption recovery | 21 | D4 |
| 28 | Content Moderation Bench | Trust and safety — moderation and appeals | 21 | D4 |
| 29 | Prompt Injection Range | Application security — adversarial testing | 22 | D4 |
| 30 | Vendor Risk Assessor | Third-party risk — supply chain review | 20 | D4 |
| **G** | **Governance, code and the release you can defend** | | | |
| 31 | Privacy Request Handler | Data protection — subject access and erasure | 20 | D4 |
| 32 | Code Migration Crew | Software engineering — automated migration | 21 | D4 |
| 33 | Model Release Gate | ML governance — release approval | 21 | D5 |
| 34 | Multi-Region Server Farm | Platform infrastructure — stateless scale | 21 | D4 |
| 35 | Quota and Cost Router | Platform economics — provider routing | 19 | D4 |
| **H** | **Observability, interop and the capstone** | | | |
| 36 | Observability Glass Box | Platform observability — tracing | 20 | D5 |
| 37 | Blue Green Release Desk | Release engineering — safe deploys | 20 | D5 |
| 38 | Partner Agent Network | Cross-company interop — A2A | 21 | D5 |
| 39 | Municipal Grievance Office | Public services — citizen grievances | 20 | D3 |
| 40 | The Enterprise Desk *(capstone)* | Cross-industry — six agents, three boundaries | 22 | D5 |

<!-- granth:projects:end -->

**811 project sittings, plus the 5 optional Foundry sittings — 816.** §16 has the levers if that is
the wrong size.

---

## §12 · The spine — the eighteen subsystems every project builds

This is the Full-Stack Rule made concrete. **Every project builds all eighteen, in this order,
from zero, at full depth.** A project may not skip a slot; a project whose subject deepens a slot
adds days *after* it (§13).

Day numbers below are the spine positions. A project with inserts renumbers accordingly — its own
map in `PROJECT.md`, written at the freshness check (§10), is what the learner reads.

<!-- granth:spine:start -->

| Slot | Title | What it must contain, at full depth |
| --- | --- | --- |
| 0 | The machine and the repository | The toolchain checked live · the interpreter pinned and the pin read back · `git init` and the first commit · `.gitignore` written **before** `.env` exists, and why that order · `.env.example` · where the free key comes from · a green check on an empty system |
| 1 | The skeleton and the kit | The package layout · `pyproject.toml` with exact pins · the `run` driver · the model registry, every ID pinned · `util/backoff.py` · `util/logging.py` · `util/budget.py` · `util/keys.py` · the check that can go red before anything exists |
| 2 | The domain and its data | The synthetic fixture set and why every byte of it is invented · the store · the shape of the record this industry actually keeps · the read and write contract the boundary will enforce |
| 3 | The boundary, part one | Why the data goes behind MCP and what breaks when it does not · the server skeleton · its first tool · the tool called across a real process line |
| 4 | The boundary, part two | Transports — stdio and Streamable HTTP · lifecycle and the era gap (ADR-0005) · capabilities · resources and prompts · the client wiring, and the tool that now lives elsewhere |
| 5 | Tools | The description **is** the API · typed parameters and the schema the model sees · the tool-result turn · docstrings that stop the model inventing · the tool that returns nothing, honestly |
| 6 | The first agent | `Agent` plus runner · the model pinned explicitly · instructions · the loop: think, act, observe · events and streaming · the 2.x event model |
| 7 | Sessions and state | What a session is and what it is not · what survives a turn · what must never be written into it · the run, and errors that surface instead of hiding |
| 8 | The cast | One agent is a function, two is an architecture · the specialist with three tools and no opinions · delegation, transfer and the handback · the request budget across the whole cast |
| 9 | The workflow runtime | Nodes and edges · sequential, parallel and loop · shared state between nodes · **the bound that stops a loop**, and `max_llm_calls` |
| 10 | Callbacks and plugins | Before and after the model · before and after the tool · the plugin that sees every agent · structured logging three agents deep · what a callback must never do |
| 11 | Memory and retrieval | Session versus memory · what to remember and what to look up · embeddings, chunking and top-k · citations that resolve · `recall@k` as a test that can fail |
| 12 | Structured output | Schemas on the way out · the validator that refuses the model's confident guess · schema evolution: the field that appeared last Tuesday · the decision record this industry has to defend |
| 13 | Reliability | Honest 429 — `Retry-After`, 1/2/4/8, escalate · the fallback chain · the budget guard that refuses · checkpoints, idempotency keys and replay · **the answer you must not fabricate** |
| 14 | Security and privilege | The threat model for *this* system · injection arriving through a tool result · per-agent tool allowlists · scoped credentials · PII at the boundary · the approval gate and its audit trail |
| 15 | Observability | Structured logs with a correlation id · one trace across every agent and every hop · the span that is missing and how you find it · what you page a human about |
| 16 | Evals | The evalset · the judge and its rubric · the trajectory, not just the answer · the baseline that makes a score mean something · **the gate that goes red** |
| 17 | Ship | `Dockerfile` and the stateless container · secrets injected, never baked · `compose.yaml` with the MCP sidecar · the CI workflow running the evalset · **the cold clone**, run for real, output pasted in · what I would change if I wrote this again |

<!-- granth:spine:end -->

**Slot 17 is always the last day of a project**, whatever the inserts do to the numbering.

---

## §13 · The day maps — each project's brief and its extra days

Every project runs the eighteen spine days. This section says **what those days are about in that
project's industry**, and lists the **inserts** — the extra sittings its subject earns. An insert
is placed after a spine slot and takes the next day number.

Changing a project's insert list is a **plan amendment**: it changes the Days column in §11 and
`python p.py doctor` fails when the two disagree.

<!-- granth:day-map:start -->

#### P00 · Foundry — optional primer, 5 days

*Not a project. No project may reference it and no project needs it — every project's day 0 and
day 1 teach this material again, from zero, in its own words. This exists only for a reader who
has never set up a Python toolchain and wants to do it once, slowly, before starting P01.*

| Day | Title |
| --- | --- |
| 0 | The machine — uv, Python 3.12, and the four Pythons that ruin a Monday |
| 1 | The skeleton — `.gitignore` before `.env` exists, and why that order |
| 2 | Keys — where a free key comes from, and the three-state probe |
| 3 | Pinning — exact versions, the lockfile, and `uv lock --check` |
| 4 | The check that refuses a half-finished day |

#### P01 · Claims Intake Desk — 20 days · D3

**The problem.** A synthetic insurer's first-notice-of-loss queue. Free-text notifications arrive,
each with a policy number, a description and sometimes a photograph reference. The desk classifies
the loss type, checks the policy was in force on the date of loss, decides whether the claim can be
fast-tracked, and writes either a fast-track confirmation or a deficiency letter naming exactly
what is missing.
**Tools.** `fetch_policy(number)` · `check_in_force(number, date)` · `classify_loss(text)` ·
`draft_letter(claim_id, kind)`
**Boundary.** `claims_mcp/` — owns the policy store and the claim file; no agent touches a file.
**Cast.** `intake` → `classifier` ‖ `policy_checker` → `adjuster` → `letter_writer`
**Done when.** A cold clone processes twelve synthetic notifications, fast-tracks the four that
qualify, writes eight deficiency letters that each name a real missing field, and the eval goes red
the moment the policy in-force check is disabled.

| After spine day | Extra day |
| --- | --- |
| 5 | The tool that must refuse — a deficiency is an answer, not an error |
| 12 | The decision record: why this claim was fast-tracked, in a form an auditor accepts |

#### P02 · Warehouse Stock Control — 20 days · D3

**The problem.** A synthetic three-aisle warehouse whose counted stock disagrees with its recorded
stock. The desk reconciles cycle counts against the ledger, explains each discrepancy, and raises
replenishment only where the explanation does not cover it.
**Tools.** `read_bin(bin_id)` · `record_count(bin_id, qty)` · `explain_variance(sku, window)` ·
`raise_replenishment(sku, qty)`
**Boundary.** `stock_mcp/` — the stock ledger, the only writer.
**Cast.** `supervisor` → `counter` ‖ `reconciler` → `replenisher`
**Done when.** A cold clone reconciles sixty bins, explains every one of the nine planted variances,
and the eval goes red when the ledger is allowed a second writer.

| After spine day | Extra day |
| --- | --- |
| 3 | One writer, one truth — what two writers do to a stock ledger |
| 4 | The boundary under a second replica, and the call that must be idempotent |

#### P03 · Clinical Triage Room — 21 days · D3

**The problem.** A synthetic out-of-hours line. The room takes a symptom description, asks the
questions its protocol requires, assigns an urgency band, and **refuses to answer** anything that
crosses into diagnosis or prescription — escalating instead, with the transcript attached.
**Tools.** `lookup_protocol(complaint)` · `record_answer(case_id, q, a)` · `assign_band(case_id)` ·
`escalate(case_id, reason)`
**Boundary.** `triage_mcp/` — the protocol set and the case file.
**Cast.** `greeter` → `symptom_taker` → `triager` → `safety_reviewer` → `escalator`
**Done when.** A cold clone bands twenty synthetic cases, escalates all four planted red flags,
refuses the three prescription requests with the same wording every time, and the safety eval goes
red when the reviewer is removed from the cast.

| After spine day | Extra day |
| --- | --- |
| 14 | The refusal that must not be negotiable, and the eval that proves it |
| 14 | Guardrails as code, not as instructions |
| 16 | The safety evalset: twenty ways to ask for a prescription |

#### P04 · Loan Underwriting Desk — 20 days · D3

**The problem.** A synthetic consumer lender. The desk verifies an application against declared
income and bureau data, scores it against a written policy, and issues either an approval or a
decline **with the specific policy clauses that caused it** — because an unexplained decline is a
regulatory problem, not a UX problem.
**Tools.** `fetch_application(id)` · `pull_bureau(subject)` · `score_policy(app, policy)` ·
`draft_notice(app_id, decision)`
**Boundary.** `credit_mcp/` — the application store, the policy text and the bureau fixture.
**Cast.** `intake` → `verifier` ‖ `scorer` → `underwriter` → `notice_writer`
**Done when.** A cold clone decides thirty synthetic applications, every decline cites at least one
real policy clause by id, and the eval goes red when a clause id that does not exist is accepted.

| After spine day | Extra day |
| --- | --- |
| 12 | The adverse-action notice — a structured output with legal consequences |
| 15 | The audit trail: replaying a decision six months later |

#### P05 · Contract Review Bench — 21 days · D3

**The problem.** A synthetic master services agreement against a house playbook. The bench finds
clauses that depart from the playbook, drafts redlines, and cites every claim back to the paragraph
it came from — then fails itself when a citation does not contain the quoted words.
**Tools.** `fetch_clause(id)` · `search_playbook(query, k)` · `score_departure(clause, rule)` ·
`draft_redline(clause, rule)`
**Boundary.** `clause_mcp/` — the document store and the playbook index.
**Cast.** `router` → `retriever` ‖ `clause_finder` → `redliner` → `critic`
**Done when.** A cold clone reviews a twelve-clause agreement, flags the four planted departures,
cites each to a paragraph that really contains the quoted words, and `citation_precision` goes red
the moment quote-checking is disabled.

| After spine day | Extra day |
| --- | --- |
| 11 | Chunking a legal document without cutting a clause in half |
| 11 | The citation that must resolve — quote checking as a hard gate |
| 16 | `citation_precision` and the baseline that makes it mean something |

#### P06 · Plant Floor Supervisor — 20 days · D4

**The problem.** A synthetic production line with three stations. The supervisor watches station
telemetry, diagnoses stoppages, and instructs line agents — each of which may reach for **only** the
tools its station owns. The interesting failure is an agent reaching across.
**Tools.** six, filtered per agent · `read_station(id)` · `read_oee(line, window)` ·
`log_stoppage(...)` · `request_maintenance(...)` · `adjust_setpoint(...)` · `halt_line(reason)`
**Boundary.** `floor_mcp/` — telemetry, the stoppage log and the setpoint store.
**Cast.** `supervisor` → three line agents, three tool sets
**Done when.** A cold clone diagnoses eight synthetic stoppages, and the eval goes red when any line
agent successfully calls `halt_line`, which only the supervisor may call.

| After spine day | Extra day |
| --- | --- |
| 5 | Tool filtering and allowlists — who may call what, enforced where |
| 14 | The failure lab: the agent that reached for the halt |

#### P07 · Field Service Inspector — 20 days · D3

**The problem.** A synthetic utility's pole inspections. Each job produces photographs and readings
that must survive the turn, be attached to the job, and end as a report file a supervisor opens.
The tool that generates the report does not return in the same turn.
**Tools.** `fetch_job(id)` · `attach_photo(job_id, ref)` · `read_meter(asset_id)` ·
`generate_report(job_id)` *(long-running)*
**Boundary.** `field_mcp/` — the job store, the photo store and the report artifacts.
**Cast.** `dispatcher` → `inspector` → `reporter`
**Done when.** A cold clone completes six synthetic jobs, produces six real report files, and the
eval goes red when an artifact reference is allowed to outlive the job it belongs to.

| After spine day | Extra day |
| --- | --- |
| 5 | Long-running tools — the turn that does not return yet |
| 5 | Artifacts — files that survive the turn and cross the boundary |

#### P08 · Fleet Dispatch Yard — 21 days · D3

**The problem.** A synthetic haulage yard. Loads arrive with windows and constraints; the yard plans
an assignment, dispatches it, and **replans** when a driver reports late — which is the whole
subject, because the first plan is never the one that runs.
**Tools.** `list_loads(day)` · `driver_hours(driver_id)` · `assign(load_id, driver_id)` ·
`report_delay(load_id, minutes)`
**Boundary.** `fleet_mcp/` — the load board, the driver roster and the hours ledger.
**Cast.** `planner` → `dispatcher` → N driver agents → `replanner`
**Done when.** A cold clone plans a twenty-load day, absorbs four injected delays without violating
an hours rule, and the eval goes red when the replanner is allowed to exceed driver hours.

| After spine day | Extra day |
| --- | --- |
| 9 | The plan as data — decomposition a human can read and edit |
| 9 | Replanning: what to keep when the world moved |
| 9 | The plan that never ends, and the bound that stops it |

#### P09 · Grid Watch Room — 20 days · D4

**The problem.** A synthetic distribution grid emitting telemetry and alarms, the same alarm often
four times. The watch room deduplicates, correlates, decides what is actually one event, and pages a
human only for the ones that earn it. It runs unattended overnight.
**Tools.** `ingest_event(payload)` · `correlate(window)` · `open_case(...)` · `page(oncall, case_id)`
**Boundary.** `grid_mcp/` — the event store, the case store and the dedup index.
**Cast.** `intake` → `deduper` → `analyst` → `notifier`
**Done when.** A cold clone ingests four hundred synthetic events including forty duplicates, opens
exactly the eleven real cases, and the eval goes red when the same event id is allowed to open two.

| After spine day | Extra day |
| --- | --- |
| 13 | Idempotent intake — the same event arriving four times |
| 15 | The unattended run: a CronJob, and a digest someone would act on |

#### P10 · Patient Records Abstractor — 20 days · D4

**The problem.** Synthetic clinical notes that must be abstracted into coded fields — and must never
leave the boundary carrying an identifier. Every field the system emits is either coded or redacted,
and the system has to prove which.
**Tools.** `fetch_note(id)` · `abstract_fields(note)` · `redact(text, policy)` ·
`prove_redaction(record_id)`
**Boundary.** `record_mcp/` — the note store, the redaction policy and the proof log.
**Cast.** `classifier` → `abstractor` → `redactor` → `keeper`
**Done when.** A cold clone abstracts forty synthetic notes, and the redaction eval goes red on a
single leaked identifier anywhere in any log, prompt or trace.

| After spine day | Extra day |
| --- | --- |
| 14 | PII at the boundary — the field that must never reach a prompt |
| 14 | Retention and deletion, and proving a thing is gone |

#### P11 · Tender Bid Assembler — 20 days · D3

**The problem.** A synthetic public tender with a hundred-question response schema that changed
between the draft and the final issue. The assembler fills it, validates it against the *current*
schema, and refuses to submit a confident guess.
**Tools.** `fetch_question(id)` · `search_library(query, k)` · `fill_answer(qid, text)` ·
`validate_response(bundle)`
**Boundary.** `tender_mcp/` — the question set, the answer library and the schema versions.
**Cast.** `reader` → `assembler` → `validator` → `pricer`
**Done when.** A cold clone fills a hundred-question response, the validator rejects the six planted
guesses, and the eval goes red when the old schema version is silently accepted.

| After spine day | Extra day |
| --- | --- |
| 12 | Schema evolution — the field that appeared last Tuesday |
| 12 | Elicitation: the server that asks the human a question mid-turn |

#### P12 · Research Librarian — 21 days · D3

**The problem.** A synthetic corpus of study abstracts. The librarian answers "has anything like
this been tried?", finds the three real precedents, misses the two it should miss, and says so —
because a librarian that invents a citation is worse than no librarian.
**Tools.** `search_corpus(query, k)` · `fetch_study(id)` · `summarise(id)` · `check_claim(claim, id)`
**Boundary.** `library_mcp/` — the index and the study store.
**Cast.** `router` → `retriever` ‖ `scout` → `writer` → `critic`
**Done when.** A cold clone finds three of five known precedents, reports the two misses honestly,
and `recall@5` goes red when the chunker is disabled.

| After spine day | Extra day |
| --- | --- |
| 11 | Embeddings and what a vector actually compares |
| 11 | Chunking, overlap, and the answer cut in half |
| 16 | `recall@k` against an honest baseline, and the miss you must report |

#### P13 · Invoice Reconciliation Clerk — 20 days · D4

**The problem.** A synthetic accounts-payable queue doing three-way match between invoice, purchase
order and goods receipt. The run is killed halfway on purpose, restarted, and must not post a single
payment twice.
**Tools.** `fetch_invoice(id)` · `match_three_way(inv, po, grn)` · `flag_exception(...)` ·
`post_payment(inv_id, key)`
**Boundary.** `ledger_mcp/` — the invoice store and the payment ledger.
**Cast.** `matcher` → `exception_handler` → `poster`
**Done when.** A cold clone reconciles two hundred synthetic invoices, is killed at invoice 97 and
resumed, and the eval goes red on any duplicate payment.

| After spine day | Extra day |
| --- | --- |
| 13 | Idempotency keys — the payment that must happen exactly once |
| 13 | Checkpoints and replay: killed at 97, resumed at 97 |

#### P14 · Fraud Watch Floor — 21 days · D4

**The problem.** A synthetic card-payment stream under review. Six workers score in parallel against
shared state, an adjudicator decides, and a case file is written. The subject is what parallel
agents do to shared state when they all want it at once.
**Tools.** `score_txn(id)` · `rules_hit(id)` · `hold(card, reason)` · `open_case(txn_id)`
**Boundary.** `signal_mcp/` — the transaction stream, the rules and the case store.
**Cast.** `intake` → six scorers ‖ `rules` → `adjudicator` → `case_writer`
**Done when.** A cold clone reviews five thousand synthetic transactions, holds the twenty-three
planted frauds, and the eval goes red when two workers are allowed to hold the same card twice.

| After spine day | Extra day |
| --- | --- |
| 9 | Six workers and one piece of shared state |
| 9 | Contention: the swarm that would not stop |
| 13 | Backpressure — what to do when the stream outruns the cast |

#### P15 · Tax Filing Assistant — 19 days · D3

**The problem.** A synthetic self-assessment return. The assistant collects, prepares and reviews —
and then **stops**, because filing is a human's signature. The interesting work is the gate: what
needs a human, what the human sees, and what the trail records when the gate is bypassed.
**Tools.** `fetch_document(id)` · `extract_figures(doc)` · `compute_return(figures)` ·
`submit_for_signature(return_id)`
**Boundary.** `filing_mcp/` — the document store and the return draft.
**Cast.** `collector` → `preparer` → `reviewer` → human gate
**Done when.** A cold clone prepares eight synthetic returns, none reaches submission without a
recorded human approval, and the eval goes red when the gate is bypassed without a trail entry.

| After spine day | Extra day |
| --- | --- |
| 14 | The approval gate — what needs a human, and what the trail must show |

#### P16 · Market Research Analyst — 20 days · D3

**The problem.** Two synthetic sources that disagree — a filings archive and a news feed. The
analyst must not average them. It has to notice the disagreement, adjudicate it against a stated
rule, and log why the loser lost.
**Tools.** `search_filings(query, k)` · `search_feed(query, k)` · `compare(a, b)` ·
`write_note(topic)`
**Boundary.** `market_mcp/` — the filings archive and the feed fixture.
**Cast.** `router` → two source agents → `adjudicator` → `writer`
**Done when.** A cold clone answers twelve synthetic questions, logs an adjudication for each of the
five planted disagreements, and the eval goes red when a disagreement is silently resolved.

| After spine day | Extra day |
| --- | --- |
| 11 | Grounding versus retrieval — two ways to be right, one way to be wrong |
| 16 | LLM-as-judge, and the baseline that stops it flattering you |

#### P17 · Collections Outreach Desk — 19 days · D3

**The problem.** A synthetic arrears book. Every message the desk drafts is bound by conduct rules
about time, tone, frequency and what may not be said. The desk's real product is a message that
passes a compliance reviewer, and the reviewer is part of the cast.
**Tools.** `fetch_account(id)` · `contact_history(id)` · `draft_message(id, channel)` ·
`check_conduct(draft)`
**Boundary.** `account_mcp/` — the arrears book and the contact log.
**Cast.** `planner` → `messenger` → `compliance_reviewer`
**Done when.** A cold clone drafts forty messages, the reviewer rejects the six planted breaches,
and the eval goes red when a rejected draft can still be sent.

| After spine day | Extra day |
| --- | --- |
| 14 | Policy as a guardrail the model cannot talk its way past |

#### P18 · Employee Onboarding Coordinator — 20 days · D3

**The problem.** A synthetic joiner's first week: accounts, equipment, training, a manager
introduction — a procedure repeated for every joiner with small variations. The subject is packaging
that procedure as an Agent Skill the cast loads, rather than as a prompt someone maintains by hand.
**Tools.** `fetch_joiner(id)` · `provision(system, joiner)` · `check_status(joiner)` ·
`notify(manager, joiner)`
**Boundary.** `hr_mcp/` — the joiner record and the provisioning fixture.
**Cast.** `coordinator` → `provisioner` → `checker`
**Done when.** A cold clone onboards ten synthetic joiners, the skill fires on the right requests and
not the wrong ones, and skills lint inside `./run check`.

| After spine day | Extra day |
| --- | --- |
| 5 | `SKILL.md` anatomy, and loading a skill into the cast |
| 5 | Progressive disclosure — the skill that does not blow the window |

#### P19 · Shift Roster Planner — 20 days · D3

**The problem.** A synthetic four-week roster with hard constraints — coverage, rest, certification —
and soft preferences. The planner is a graph: nodes that generate, evaluate, repair and re-evaluate,
with a loop that must be bounded.
**Tools.** `list_shifts(window)` · `staff_available(shift)` · `place(staff, shift)` ·
`score_roster(draft)`
**Boundary.** `roster_mcp/` — the shift board, the staff record and the constraint set.
**Cast.** a six-node graph over three agents
**Done when.** A cold clone produces a legal four-week roster, and the eval goes red when the repair
loop is allowed to run without a bound.

| After spine day | Extra day |
| --- | --- |
| 9 | State that flows along an edge, and state that must not |
| 9 | The repair loop, and the bound that makes it terminate |

#### P20 · Recruiting Screener — 20 days · D5

**The problem.** Synthetic applications screened against a stated rubric. The system is only
defensible if the *rubric* is the thing being applied, and the way you find out is an eval suite
that measures consistency across matched pairs.
**Tools.** `fetch_application(id)` · `score_rubric(app, rubric)` · `explain_score(app_id)` ·
`flag_review(app_id)`
**Boundary.** `ats_mcp/` — the application store and the rubric.
**Cast.** `screener` → `scorer` → `auditor`
**Done when.** A cold clone screens sixty synthetic applications, matched pairs score within
tolerance, and CI blocks the build when consistency regresses.

| After spine day | Extra day |
| --- | --- |
| 16 | Rubrics, judges, and scoring the trajectory instead of the answer |
| 16 | The consistency suite, and the regression that must block a merge |

#### P21 · IT Helpdesk Night Shift — 19 days · D4

**The problem.** A synthetic ticket queue between 22:00 and 06:00 with nobody watching. The shift
triages, resolves what it can, escalates what it must, and leaves a morning digest that a human
would actually act on.
**Tools.** `list_tickets(since)` · `classify(ticket)` · `apply_runbook(ticket, runbook)` ·
`escalate(ticket, reason)`
**Boundary.** `ticket_mcp/` — the ticket store and the runbook set.
**Cast.** `scheduler` → `triager` → `resolver` → `digester`
**Done when.** A cold clone runs a synthetic night unattended, resolves the eleven runbook-covered
tickets, escalates the rest, and the eval goes red when the digest omits an escalation.

| After spine day | Extra day |
| --- | --- |
| 15 | The unattended run — scheduling, and what to page a human about at 3am |

#### P22 · Incident Commander — 21 days · D5

**The problem.** A synthetic outage. The commander runs the incident: investigates against runbooks,
searches past incidents, keeps a comms timeline, and hands over. The subject is **tracing** — when
the answer is wrong you must be able to see which agent and which hop made it wrong.
**Tools.** `fetch_alert(id)` · `search_incidents(query, k)` · `run_check(name)` ·
`post_update(incident_id, text)`
**Boundary.** `runbook_mcp/` — runbooks, the incident archive and the timeline.
**Cast.** `commander` → `investigator` ‖ `historian` → `comms`
**Done when.** A cold clone runs a synthetic incident end to end, one trace tree covers every agent
and every boundary hop, and the eval goes red when a span is missing.

| After spine day | Extra day |
| --- | --- |
| 15 | One trace across three agents and two processes |
| 15 | The missing span, and the instrumented boundary |
| 15 | Reading a trace when the answer was wrong |

#### P23 · Retail Personal Shopper — 19 days · D3

**The problem.** A synthetic catalogue and a shopper who asks four near-identical questions in a
row. Every repeat is a request you already paid for. The subject is the cache: the key, the
invalidation, and the staleness you can defend.
**Tools.** `search_catalogue(query, k)` · `fetch_item(sku)` · `check_stock(sku)` ·
`compare(skus)`
**Boundary.** `catalogue_mcp/` — the catalogue, the stock fixture and the cache layer.
**Cast.** `router` → two specialists, behind a cache
**Done when.** A cold clone answers a forty-turn synthetic session, the savings report is stated in
**requests, not dollars**, and the eval goes red when a stale price is served after a stock change.

| After spine day | Extra day |
| --- | --- |
| 13 | Cache keys, invalidation, and the staleness you can defend |

#### P24 · Hotel Front Desk — 20 days · D3

**The problem.** A synthetic property. A booking touches inventory, payment and a confirmation, and
a failure halfway through must leave nothing behind. The subject is the compensating action: what to
undo, in what order, when step three fails.
**Tools.** `search_rooms(dates, type)` · `hold_room(room, dates)` · `take_payment(booking, amount)` ·
`confirm(booking)`
**Boundary.** `booking_mcp/` — the room inventory and the booking ledger.
**Cast.** `concierge` → `booker` → `rollback_keeper`
**Done when.** A cold clone completes thirty synthetic bookings with payment failing on six, and the
eval goes red when a held room survives a failed payment.

| After spine day | Extra day |
| --- | --- |
| 13 | The compensating action — undoing step two after step three failed |
| 13 | The failure lab: the room nobody can book and nobody is in |

#### P25 · Restaurant Order Line — 20 days · D3

**The problem.** A synthetic phone line taking orders by voice. The conversation must not freeze
while a tool checks stock, and it must handle being interrupted mid-sentence, because people do
that.
**Tools.** `read_menu()` · `check_availability(item)` · `add_to_order(item, qty)` ·
`confirm_order(order_id)` *(non-blocking)*
**Boundary.** `order_mcp/` — the menu, the stock fixture and the kitchen queue.
**Cast.** `voice` → `order_taker` → `queue_reader` → `confirmer`
**Done when.** A cold clone takes fifteen synthetic voice orders, no turn blocks while a tool runs,
and the eval goes red when a tool call freezes the conversation.

| After spine day | Extra day |
| --- | --- |
| 6 | The Live API — a conversation instead of a request |
| 6 | Non-blocking tools, and being interrupted mid-sentence |

#### P26 · Bank Branch Concierge — 20 days · D4

**The problem.** A synthetic branch where nothing is answerable until the customer is authenticated,
and the token belongs to the customer rather than to the agent. The auditor agent can read
everything and write nothing, and that is enforced by credentials, not by instructions.
**Tools.** scoped per agent · `whoami(token)` · `fetch_accounts(token)` · `transfer(token, ...)` ·
`write_audit(entry)`
**Boundary.** `vault_mcp/` — accounts behind OAuth2, with issuer validation.
**Cast.** `requester` → `approver` → `auditor`
**Done when.** A cold clone serves twenty authenticated sessions, a token expires mid-run and the
run fails honestly, and the eval goes red when the auditor successfully writes.

| After spine day | Extra day |
| --- | --- |
| 14 | OAuth2 at the boundary, and the token that is not yours |
| 14 | Scoped credentials per agent — the auditor that cannot write |

#### P27 · Airline Rebooking Desk — 21 days · D4

**The problem.** A synthetic cancellation stranding two hundred passengers with forty seats
available. Six workers rebook in parallel against the same seat map. Every seat must go to exactly
one passenger, and the desk must stop when the seats run out rather than inventing them.
**Tools.** `list_stranded(flight)` · `search_seats(route, window)` · `hold_seat(seat, pax)` ·
`rebook(pax, seat)`
**Boundary.** `rebook_mcp/` — the seat map and the passenger list, under contention.
**Cast.** `dispatcher` → six rebooking workers → `reducer`
**Done when.** A cold clone rebooks forty of two hundred synthetic passengers, no seat is
double-allocated, and the eval goes red when two workers hold the same seat.

| After spine day | Extra day |
| --- | --- |
| 9 | Six agents, one seat map — coordination and its cost |
| 9 | The reducer, and what to do with the hundred and sixty |
| 13 | The swarm that would not stop, and the bound that stopped it |

#### P28 · Content Moderation Bench — 21 days · D4

**The problem.** Synthetic user content, including content written to talk the moderator out of its
own policy. The bench decides, explains, and survives a red-team evalset it did not write.
**Tools.** `fetch_item(id)` · `check_policy(text, policy)` · `decide(item_id, verdict)` ·
`open_appeal(item_id)`
**Boundary.** `moderation_mcp/` — the item store, the policy set and the appeal log.
**Cast.** `reader` → `guard` → `adjudicator` → `appeals`
**Done when.** A cold clone moderates three hundred synthetic items, the red-team suite finds no
policy bypass, and the eval goes red when the guard is removed.

| After spine day | Extra day |
| --- | --- |
| 14 | Content that argues with its moderator |
| 16 | Writing a red-team evalset against your own system |
| 16 | The adversarial baseline, and what "no bypass" is allowed to mean |

#### P29 · Prompt Injection Range — 22 days · D4

**The problem.** A range whose MCP boundary is **deliberately hostile**: the tool results carry
instructions. Everything the system believes arrives through a channel an attacker controls. The
project's subject is the boundary as attack surface, and its deliverable is a system that reads
hostile data without obeying it.
**Tools.** least-privilege by construction · `fetch_feed(id)` · `summarise(id)` ·
`write_note(text)` · `escalate(reason)`
**Boundary.** `feed_mcp/` — hostile by design, documented as such.
**Cast.** `reader` → `guard` → `writer`
**Done when.** A cold clone processes a hundred hostile synthetic feed items, executes none of the
embedded instructions, and the eval goes red when the guard is bypassed by any of the forty
planted attacks.

| After spine day | Extra day |
| --- | --- |
| 4 | A tool result is untrusted input, and always was |
| 14 | Forty ways in: the attack catalogue for this system |
| 14 | Least privilege as containment, not as prevention |
| 16 | The red-team evalset that must be allowed to win sometimes |

#### P30 · Vendor Risk Assessor — 20 days · D4

**The problem.** Third-party components — including Agent Skills — arriving from a registry. The
assessor reads them the way an attacker would, records provenance, and blocks the unvetted. The
lesson underneath is that `@latest` is not a version.
**Tools.** `fetch_component(ref)` · `read_manifest(ref)` · `score_risk(manifest)` ·
`record_provenance(ref, decision)`
**Boundary.** `registry_mcp/` — the component registry fixture and the provenance ledger.
**Cast.** `fetcher` → `auditor` → `gatekeeper`
**Done when.** A cold clone assesses twenty-five synthetic components, blocks the four planted
malicious ones, and the eval goes red when a component with no pinned version is admitted.

| After spine day | Extra day |
| --- | --- |
| 14 | Reading a third-party skill like an attacker |
| 14 | The provenance ledger, and why `@latest` is not a version |

#### P31 · Privacy Request Handler — 20 days · D4

**The problem.** A synthetic subject access and erasure queue. Find every record about one person
across four stores, produce a package, erase on request, and **prove** the erasure — because
"we deleted it" is a claim, and a claim is not evidence.
**Tools.** `find_subject(identifier)` · `collect_records(subject)` · `erase(record_id)` ·
`prove_erasure(subject)`
**Boundary.** `subject_mcp/` — four stores, one index and the proof log.
**Cast.** `classifier` → `finder` → `redactor` → `prover`
**Done when.** A cold clone handles fifteen synthetic requests, every erasure is provable, and the
eval goes red when a record survives in any store, log or trace.

| After spine day | Extra day |
| --- | --- |
| 14 | Erasure across four stores, and the one that forgot |
| 14 | Proof of deletion — evidence, not assertion |

#### P32 · Code Migration Crew — 21 days · D4

**The problem.** A synthetic repository to be migrated across a breaking library version. The crew
plans, **executes code in a sandbox**, and verifies. Executing generated code is the most dangerous
capability in this curriculum, and it arrives with its containment story.
**Tools.** `read_tree(path)` · `propose_patch(file, change)` · `run_sandbox(cmd)` ·
`verify(test_cmd)`
**Boundary.** `repo_mcp/` — the working tree and the sandbox controller.
**Cast.** `planner` → sandboxed `executor` → `verifier`
**Done when.** A cold clone migrates a synthetic twelve-file repository, its tests pass, and the
eval goes red when sandboxed code reaches the host filesystem or the network.

| After spine day | Extra day |
| --- | --- |
| 5 | Code execution as a tool, and what it may reach |
| 14 | The sandbox — isolation, quotas, and the runaway contained |
| 14 | The failure lab: the patch that tried to leave |

#### P33 · Model Release Gate — 21 days · D5

**The problem.** A synthetic release pipeline for prompt and model changes. The gate blocks a change
that makes the system worse and passes one that does not, **with no human deciding which happened**.
Cost and latency are gates too, not dashboards.
**Tools.** `run_evalset(ref)` · `compare_to_baseline(run)` · `measure_cost(run)` ·
`decide_release(run)`
**Boundary.** `evalset_mcp/` and `metrics_mcp/` — two boundaries, one pipeline.
**Cast.** `gate` → `cost_guard` → `latency_guard`
**Done when.** A cold clone runs a synthetic release train, blocks the two regressions, admits the
three improvements, and the eval goes red when a regression is admitted.

| After spine day | Extra day |
| --- | --- |
| 16 | The baseline, and what a score means without one |
| 16 | Cost and latency as gates, with numbers |
| 17 | The pipeline that blocks a merge, and the override that is logged |

#### P34 · Multi-Region Server Farm — 21 days · D4

**The problem.** The same desk, three replicas, one Kubernetes cluster. A pod is deleted mid-turn on
purpose. Statelessness stops being a design preference and becomes the thing that decides whether
the turn completes.
**Tools.** unchanged from the desk it scales · plus `health()` and `drain()`
**Boundary.** `farm_mcp/` — three replicas behind one service.
**Cast.** `router` → two workers
**Done when.** A cold clone scales to three, a pod is killed mid-turn, the turn completes, and the
eval goes red when any request needs the replica that started it.

| After spine day | Extra day |
| --- | --- |
| 4 | State handles in the payload, not connections a server holds |
| 17 | kind/k3d: deployment, service, secret, and the pod you delete |
| 17 | Rolling a replica set without dropping a turn |

#### P35 · Quota and Cost Router — 19 days · D4

**The problem.** Four providers, four free tiers, four different ways to run out. The router keeps a
ledger of headroom, routes by it, and reroutes when a provider is exhausted on purpose — without
fabricating an answer to cover the exhaustion.
**Tools.** `check_headroom(provider)` · `route(request)` · `record_usage(provider, tokens)` ·
`fallback(request)`
**Boundary.** `quota_mcp/` — the usage ledger.
**Cast.** `router` → three provider-bound agents
**Done when.** A cold clone runs a hundred synthetic turns, a provider is exhausted deliberately, the
cast reroutes, and the eval goes red when an error is answered with an invented result.

| After spine day | Extra day |
| --- | --- |
| 13 | The ledger, the headroom, and the fallback chain that must not lie |

#### P36 · Observability Glass Box — 20 days · D5

**The problem.** A cast that works and cannot be explained. This project instruments it: spans
across agents, across the boundary, across the retry — until one trace answers "why did it say
that?" without anyone reading a log by hand.
**Tools.** the desk's own, instrumented · plus `trace_query(id)`
**Boundary.** its own, fully instrumented.
**Cast.** the full cast under one trace tree
**Done when.** A cold clone answers a synthetic question, its trace explains every model call and
boundary hop, and the eval goes red when any span is unparented.

| After spine day | Extra day |
| --- | --- |
| 15 | Spans, parents, and the trace that lost its root |
| 15 | Instrumenting the boundary you own |

#### P37 · Blue Green Release Desk — 20 days · D5

**The problem.** Two deployments, one service. Roll forward into a deliberately bad build and watch
it roll back automatically. The subject is that the rollback is a property of the system, not a
person who was awake.
**Tools.** `health(colour)` · `shift_traffic(colour, pct)` · `rollback()` · `report(release_id)`
**Boundary.** `desk_mcp/` × two colours.
**Cast.** the full cast × two deployments
**Done when.** A cold clone deploys green, shifts traffic, detects the planted regression, rolls
back without a human, and the eval goes red when a bad build holds traffic.

| After spine day | Extra day |
| --- | --- |
| 17 | Two colours, one service, and the health check that decides |
| 17 | Automatic rollback, and the release report afterwards |

#### P38 · Partner Agent Network — 21 days · D5

**The problem.** Your desk talks to another company's agent. Identity stops being an implementation
detail: a peer presents a signed card, and a peer whose card fails verification is refused. Your own
desk is also **served** as a peer, which is where the interesting failure lives.
**Tools.** `discover(peer)` · `verify_card(card)` · `ask_peer(peer, question)` ·
`serve_as_peer()`
**Boundary.** its own, plus a signed-card registry.
**Cast.** your desk ↔ peer ↔ critic
**Done when.** A cold clone exchanges twelve synthetic tasks with a peer, refuses the three
unverifiable cards, and the eval goes red when a served agent calls back into its own caller.

| After spine day | Extra day |
| --- | --- |
| 4 | Serving your own agent as a boundary others call |
| 14 | Signed cards, agent identity, and the peer you refuse |
| 14 | The callback loop: the served agent that called home |

#### P39 · Municipal Grievance Office — 20 days · D3

**The problem.** A synthetic citizen grievance queue with statutory clocks. Every case has a
deadline that is law, arrives in one of three languages, and must be answered in the one it arrived
in. Long-running work has to survive across days, not turns.
**Tools.** `file_grievance(payload)` · `route(case_id)` · `request_info(case_id, question)` ·
`close(case_id, outcome)`
**Boundary.** `grievance_mcp/` — the case store and the statutory clock.
**Cast.** `intake` → `router` → `caseworker` → `sla_watcher`
**Done when.** A cold clone handles fifty synthetic grievances across three languages, misses no
statutory deadline, and the eval goes red when a case is answered in the wrong language.

| After spine day | Extra day |
| --- | --- |
| 9 | Work that outlives a turn — submit, poll, and the task handle |
| 13 | The statutory clock, and the deadline that is not negotiable |

#### P40 · The Enterprise Desk — capstone, 22 days · D5

**The problem.** One desk, six agents, three boundaries, every subsystem in this curriculum,
defended in an interview. It answers cross-industry questions by routing to the right specialist,
crossing three boundaries, under a budget, under a trace, behind an eval gate, with a human gate on
anything that writes.
**Tools.** everything this curriculum has built, in one place.
**Boundary.** three: a record store, a knowledge index, and a hostile external feed.
**Cast.** six agents.
**Done when.** A **recorded cold run with no edits and no retries**, followed by the interview drill
over every ADR in the project — the ADRs written during it, not before.

| After spine day | Extra day |
| --- | --- |
| 8 | Six agents: the org chart that is also an architecture |
| 13 | Three boundaries, one budget |
| 16 | The eval gate over everything, and what it costs to run |
| 17 | The recorded cold run, and the interview drill |

<!-- granth:day-map:end -->

---

## §14 · Style — and the defence against forty identical documents

The register: write as if explaining to a competent colleague who has not seen this system. Short
sentences. Concrete nouns. No hedging, no throat-clearing, no "let's dive in".

Repetition is required between projects and **must not be visible inside one**. The Repetition Rule
says every project teaches sessions; it does not say every project teaches sessions with the same
sentences. Four constraints keep the fortieth telling from being the first one pasted:

1. **The scene comes from this project's industry.** A part about sessions in P01 opens on a loss
   adjuster who took a call yesterday and cannot remember which claim it was. In P25 it opens on a
   phone order where the customer said "make that two". **A scene that would work unchanged in
   another project has failed its own contract**, and that is a review criterion, not a suggestion.
2. **The failure is this project's failure.** `When it breaks` carries the real error text from this
   project's code, caused on this project's data. Not a generic traceback.
3. **The production note is this industry's.** What degrades at scale, with a number that belongs to
   this domain — sixty bins, five thousand transactions, two hundred stranded passengers.
4. **One metaphor family per day**, chosen from the project's world, and grepped for across the
   day's other parts before it is used.

The rest of the standing rules:

- **Never write a rule the reader cannot see fail.** If a rule has no observable consequence in this
  project, it does not belong in this project's documents.
- **Model lines and file contents are code blocks; quotations are blockquotes.**
- **Grammar and punctuation are part of the deliverable.** A sentence the reader parses twice failed.
- **Never name a person, instructor, author, channel, academy, bootcamp or training company** — not
  in a lesson, a checklist, a docstring or a commit message. Tool and library names are required and
  unaffected, as is citing a specification by its revision.
- **Never solve the learner's `TODO(me)` reps.** Teach; do not do their work.

---

## §15 · Numbering, addressing and the ledger

**A day is addressed by its project and its day number:** project `01`, day `7`. The driver takes
them as two arguments — `python p.py brief 01 7` — and the folder is
`days/01-claims-intake-desk/day-07-<slug>/`.

**There is no global sitting number**, no curriculum ID scheme and no traceability matrix. v3 had
all three; they encoded a single global reading order, which is exactly the assumption v4 removes.
A reader may start at project 27, and nothing in the repository should imply otherwise.

**Order inside a project is strict.** Day D of project NN may be written only when days 0…D−1 of
that same project have rows in `docs/PROGRESS.md`. `python p.py brief` exits non-zero otherwise, and
that is a stop, not a warning. Skipping, merging, inserting or reordering a day inside a project
needs an ADR, written first.

**Order between projects is free.** Starting a new project is always allowed. Projects are
independent; a guard that pretended otherwise would be enforcing a fiction.

**The ledger.** `docs/PROGRESS.md` is append-only. Its v3 table and the notes under it stay verbatim
as history (ADR-0007); the v4 ledger lives below, inside `<!-- granth:ledger:start -->` markers,
which is the only region the driver reads. One row per **completed** day:

```
| Project | Day | Date | Title | Parts | Commit | Gates green? |
```

A day with no row here is not finished, whatever the folder looks like. A day that went wrong gets a
note under the table saying what went wrong — a ledger that records only successes teaches nothing,
and the notes under the v3 table are the proof of that.

**No clocks in a day document.** Not in frontmatter, not in prose, not in a checklist. The sitting
budget lives in this plan's header and §3 and nowhere else, because a duration in a day document
silently authorises the worst edit in technical writing: cutting an explanation because the day is
running long. **A subject that will not fit becomes two days.**

---

## §16 · What v4 costs, and the levers if it is the wrong size

**The bill, stated plainly.** v3 was 297 sittings. v4 is **816**. Roughly 400 lines of scaffolding
are typed forty times, and every core concept is written forty times at full depth instead of once
at full depth and thirty-nine times as a table. At five sittings a week that is a little over three
years.

That is the price of the property the learner asked for: **any one of the forty folders, on any
machine, teaches its system from zero.** It was quoted before the rewrite and accepted (ADR-0006).

**The levers, if the size turns out to be wrong.** Each is a plan amendment, and none of them
requires abandoning the four rules:

1. **Trim the spine from eighteen slots to fourteen** by merging slots 3+4 (the boundary), 6+7
   (agent and sessions), 10 into 8 (callbacks into the cast) and 15 into 16 (observability into
   evals). Every project loses four days. **−160 sittings**, and the Full-Stack Rule survives
   because nothing is dropped, only combined.
2. **Cut the insert budget to one per project.** **−49 sittings**, and every project keeps its
   subject but loses its second and third day of depth on it.
3. **Drop a track.** Eight tracks of five; removing one is **−100 sittings** and five industries.
   Track G is the most self-contained if one has to go.
4. **Keep forty projects but build twenty**, and treat the other twenty as maps to build later. The
   plan is a curriculum, not a commitment: an unbuilt project costs nothing but a table row.

**What is not a lever: writing a project without its whole feature set, or discharging a concept
with a pointer.** Both are v3, and v3 is the thing this version exists to correct.

---

## §17 · Amendment record

Every amendment to this plan is logged in `docs/CHANGELOG_PLAN.md` with the date, what moved, what
the plan now says and what it cost. Structural amendments additionally get an ADR in `docs/adr/`,
and ADRs are never rewritten.

| Version | Date | What changed |
| --- | --- | --- |
| v3.0.0 | 2026-09-08 | `_shared/` deleted; forty independent project repositories (ADR-0001) |
| v3.1.0 | 2026-09-09 | Machine-readable blocks, the ID scheme, day 0 (ADR-0002) |
| **v4.0.0** | **2026-09-10** | **The Repetition Rule replaces the Depth Rule; From-Scratch and Full-Stack rules added; `PRIMER.md`, the ID scheme, the track table and global day numbering deleted; days numbered per project from 0; projects renamed to their industry and resized to 16–22 days (ADR-0006, ADR-0007)** |
