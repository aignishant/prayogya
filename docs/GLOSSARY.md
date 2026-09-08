# Glossary — Prayoga

Append-only. One row per term, defined **once**, with the part that introduced it.

This file exists because 297 sittings is long enough that day 3 is forgotten by day 200. Its real
job is not to be read front to back; it is to be **checked before defining anything**, so a term
is never defined twice, slightly differently, in two places. Two nearly-identical definitions are
worse than one bad definition, because the reader cannot tell which is current.

Before you define a term in a day document, search this file. If it is here, link the part that
introduced it instead of redefining it.

| Term | Plain-language definition | Introduced in | Also called |
| ---- | ------------------------- | ------------- | ----------- |
| Authoring repository | The repository holding the plan, the ledgers and `./p`. It writes and checks the forty projects, and none of them depend on it. | day 0 part 2.1 | this repository |
| Project repository | One of the forty folders under `projects/`. Complete alone: its own pins, its own boundary, its own `./run`. | day 0 part 2.1 | a project |
| Driver | The one script a repository is operated through, so a command is found by reading one file rather than by remembering. `./p` here; `./run` inside every project. | day 0 part 3.1 | the runner |
| Depth contract | The plan section 5 rules on what a part document must contain, and the half of them `python p.py depth` can check by machine. | day 0 part 3.3 | the contract |
| Generated document | A file under `docs/` rebuilt from the days by `python p.py index`. Editing one only means the next run silently overwrites you. | day 0 part 3.4 | an index |
| Marker block | An HTML comment pair in the plan fencing a table `./p` parses. A heading can be reworded by accident; a marker cannot. | day 0 part 2.4 | the markers |
