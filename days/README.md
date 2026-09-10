# `days/` — the teaching

One folder per project, and inside it one folder per sitting: `day-DD-<slug>/`. **The day number is
scoped to its project and starts at 0.** P01 runs day 0 to day 19; P02 starts again at day 0. The
number is the identity and the slug is a label on it, so either can be renamed with a `git mv` and
nothing downstream notices.

```text
days/<NN-project-slug>/day-DD-<day-slug>/
├── LESSON.md      # the hub — orients and assembles; it never teaches
├── CHECKLIST.md   # the definition of done
├── parts/         # THE TEACHING — one document per subtopic
│   └── 01-<slug>/1.1-<slug>.md
└── lab/           # your own work — gitignored
```

**The project folders mirror `projects/`** — `01-claims-intake-desk`, `02-warehouse-stock-control`,
and so on — named from the project's name in the plan §11, so a project renamed in the plan is
renamed here too. `python p.py new NN D` picks the folder for you.

**A day document prints the files; the project holds them.** Code lives under
`projects/<NN-name>/`, never here.

**Nothing in a day may reference another project.** Not a path, not a project name, not a sentence
that assumes the reader has read one. Each of the forty projects teaches everything it uses, at
full depth, from zero — that is the plan §0 and §6, and `python p.py check` greps for every form of
escape.

**Read a day in this order:** the hub §1 and §2, then every part in number order. Write one with
`/day-prayoga NN D`, or scaffold an empty folder with `python p.py new NN D <slug>`. The standard
every day is held to is the plan §5, and `python p.py depth NN D` checks the half of it a script
can.

**A folder whose name starts with `_` is never a project.** `_TEMPLATES/` holds the blank documents
`python p.py new` copies from. `_archive-v3/` holds the eighteen days written under the previous
plan — unedited, superseded, and quarantined from every check, because they were written to a
contract that no longer exists. Do not read them for material: see
`docs/adr/ADR-0007-v3-days-archived-and-the-restart.md`.
