# `days/` — the teaching

One folder per day, `day-NN-<slug>/`. The number is the identity; the slug is a label on it, so a
folder can be renamed to a better slug at any time and nothing downstream notices.

```text
days/day-NN-<day-slug>/
├── LESSON.md      # the hub — orients and assembles; it never teaches
├── CHECKLIST.md   # the definition of done
├── parts/         # THE TEACHING — one document per subtopic
│   └── 01-<slug>/1.1-<slug>.md
├── sources/       # one document per primary source (only on days that have one)
└── lab/           # your own work — gitignored
```

**Read a day in this order:** the hub's §1 and §2, then every part in number order, then the
sources. That last step is deliberate: you build the mechanism by hand first and read the original
proposal afterwards, so "what survived and what did not" lands on something you have built.

**Write a day** with `/day-prahari N`, or scaffold an empty one with
`python granth.py new N <slug>`. The standard every day is held to is the plan's §11.

`_TEMPLATES/` holds the blank documents `python granth.py new` copies from. It is not a day and no tool
treats it as one.
