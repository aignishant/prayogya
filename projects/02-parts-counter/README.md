# Parts Counter

A workshop parts counter — find a part, read its stock, say which bin it is in, change the count —
built to argue for a data boundary rather than to assume one.

## What this system does

You ask it about a part. It finds it, tells you how many are on hand and whether that is below the
reorder point, and says which bin to walk to. It can also change the count, which is the operation
that makes the rest of this project necessary.

## What you need installed

`uv`, and a free Google AI Studio API key. Nothing else. Full steps in `SETUP.md`.

## The commands

```bash
uv run --frozen python run.py check          # the gate: config, pins, registry, tests
uv run --frozen python run.py parts filter   # find parts, straight through the tools
uv run --frozen python run.py race           # what a store with no boundary does under two writers
```

## The architecture

```mermaid
flowchart LR
    subgraph now["days 1-2 — no boundary"]
        T1["tools.py"] --> S1["store.py"] --> F1[("parts.json")]
    end
    subgraph later["days 3-8 — the boundary"]
        T2["tools.py"] --> C["util/mcp.py<br/>client"] -->|"MCP"| M["parts_mcp/<br/>server"] --> F2[("parts.json")]
    end
    now -.->|"day 2 is the argument<br/>for this move"| later
```

The left-hand shape works. Day 2 is about what it costs — `run.py race` issues twenty parts from two
threads and loses count of some of them, while a reader crashes on a half-written file.

## Where the teaching is

`days/02-parts-counter/day-11-.../LESSON.md` onwards, in the authoring repository. If you have only
this folder, `PRIMER.md` carries everything borrowed from elsewhere.

## What is deliberately not built 🅿️

- **No retry or backoff.** A 429 fails the run honestly rather than being smoothed over. Honest
  backoff is P05, and a retry loop written before you have watched a quota run out hides the thing
  it should surface.
- **No second agent.** One agent is a function; two is an architecture, and that is P03.
- **No boundary yet, on days 1 and 2.** That absence is the subject, not an oversight.
