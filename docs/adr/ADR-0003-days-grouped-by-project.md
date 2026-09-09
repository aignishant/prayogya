# ADR-0003 — Day folders are grouped by the project that owns them

- **Date:** 2026-09-09
- **Day:** between days 2 and 3
- **Phase:** P00
- **Status:** accepted
- **Amends:** nothing — the plan never named a path under `days/`
- **Related:** ADR-0002

## Context

`days/` is a flat list. Three days in, that is three folders:

```text
days/
├── _TEMPLATES/
├── day-000-toolchain-skeleton-driver/
├── day-01-machine-four-pythons/
└── day-02-skeleton-gitignore-before-env/
```

Finished, it is **298 entries** — 297 days and `_TEMPLATES/` — in one directory listing, sorted by
a number that says nothing about what the day is for. The plan section 16 already says what the
grouping is: *a phase is a project*. Forty-one phases, and the day numbers of each are a
contiguous run. That structure exists in the plan and is thrown away on disk.

It costs more the longer it is left, and the cost is not linear. Every day document written before
the move contains relative links to its neighbours, and every day moved after that is a day whose
links have to be re-checked. Three days is a `git mv` and one broken link. Fifty days is an
afternoon and a risk of a silently wrong path in a document nobody opens for a year.

The second cost is `projects/`, which is already grouped this way — `projects/00-foundry/` exists
today. Two folders describing the same forty projects with two different shapes is a question
every reader has to answer once.

## Decision

**Every day folder lives inside the folder of the project it teaches**, named for the phase in the
plan section 16 and matching the name that project uses under `projects/`:

```text
days/
├── _TEMPLATES/
├── _authoring/            phase 0 — the days about this repository
│   └── day-000-toolchain-skeleton-driver/
└── 00-foundry/
    ├── day-01-machine-four-pythons/
    └── day-02-skeleton-gitignore-before-env/
```

Phase 0 is the only phase that is not a project (ADR-0002), so its days go in `_authoring/`. The
underscore marks it as not-a-project, the way `_TEMPLATES/` already marks not-a-day, and it cannot
collide with a numbered project folder.

**The day folder name does not change.** It is still `day-NN-<kebab-slug>`, still checked by the
same rule, and every existing document that names one is still correct.

The load-bearing half is that **the group is derived, never stored.** `group_dir_name` in `p.py`
builds `00-foundry` from the phase row `P00 | 1–3 | Foundry — reference only …`, so a phase
renamed in the plan is renamed here, and there is no second list to drift from the first. A day is
still found by its number alone, wherever it sits, so moving a day between groups breaks nothing —
including the ledgers, which record numbers and not paths.

`python p.py new N` puts the day in the right group without being told. `day_dirs` still finds a
day left directly under `days/`, so a repository part-way through the move does not go dark.

## Options considered

| Option | Why not |
| --- | --- |
| **Leave `days/` flat** | It works, and it is what a 297-entry listing looks like at the end. The grouping already exists in the plan; refusing to write it down means every reader reconstructs it from the day map. Cost of the move only rises. |
| **Group, but store the mapping in `granth.toml`** | A second list of forty-one project names, next to the one in the plan section 16, with nothing keeping them equal. The first phase renamed in the plan is the first silent divergence. |
| **Rename day folders to `day_NN_<slug>` at the same time** | Two changes in one move. The folder regex, the scaffolder, the checker's error text and every document that names the convention would all change, to gain nothing the grouping does not already give. |
| **Group by phase number only (`P00/`, `P01/`)** | Compact, and unreadable. `days/P17/` does not say Forget Me; `projects/` does not name itself that way either. |

## Consequences

**Better.** `days/` is a list of forty-one things. It is the same list as `projects/`, in the same
order, with the same names. A day's project is visible from its path, which is what a `git log`
line and a review diff both show first.

**Worse.** Every path under `days/` is one level deeper, so a link from one project's day to
another project's day needs one more `../` — and there is now a class of relative link that can be
silently wrong. Today there was exactly one such link, from day 1 to day 0, and it was fixed by
hand. `p.py` does not check relative links, so nothing catches the next one. That is the new
failure mode, and it is not yet caught.

**Left alone on purpose.** Day 0 part 2.2 quotes a real `python p.py check` run, and its output
names the pre-move paths. It stays exactly as recorded — a transcript edited to match today is a
transcript that can no longer be trusted. Day 0 part 1.2 draws the skeleton rather than quoting a
run, so the drawing was updated and says so.

**Revisit if** the plan's phases stop being projects — if a project ever spans two phases or a
phase covers two projects, the derivation in `group_dir_name` is the thing that breaks, and it
breaks loudly rather than silently, because the folder name it produces will not match any
project.
