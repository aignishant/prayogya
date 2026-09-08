# `days/` — the teaching

One folder per sitting, `day-NN-<slug>/`. The number is the identity; the slug is a label on it,
so a folder can be renamed to a better slug at any time with a `git mv` and nothing downstream
notices.

```text
days/day-NN-<day-slug>/
├── LESSON.md      # the hub — orients and assembles; it never teaches
├── CHECKLIST.md   # the definition of done
├── parts/         # THE TEACHING — one document per subtopic
│   └── 01-<slug>/1.1-<slug>.md
└── lab/           # your own work — gitignored
```

**Day 0 is this repository.** Days 1 to 296 are the forty projects, and their code lives under
`projects/<NN-name>/`, never here. A day document prints the files; the project holds them.

**Read a day in this order:** the hub §1 and §2, then every part in number order. Write one with
`/day-prayoga N`, or scaffold an empty folder with `python p.py new N <slug>`. The standard every
day is held to is the plan §5, and `python p.py depth N` checks the half of it a script can.

`_TEMPLATES/` holds the blank documents `python p.py new` copies from. It is not a day and no tool
treats it as one.
