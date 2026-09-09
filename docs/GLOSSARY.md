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
| Interpreter | The program that runs your code — one `python` executable at a real path, of one exact version. | day 0 part 1.1 | the interpreter |
| Environment | An interpreter together with a particular set of installed packages. Two environments on one machine can hold the same package at different versions and never see each other. | day 0 part 1.1 | — |
| Pin | A written-down exact version, recorded in a file so that a machine and not a memory decides what gets used. | day 0 part 1.1 | the pin |
| Search order | The list of places a machine walks to turn a name like `python` into one program on disk. First match wins, and nothing announces that there was a choice. | day 1 part 1.1 | discovery order |
| Virtual environment | A directory holding a link back to a real interpreter and its own installed packages, marked as one by a `pyvenv.cfg` beside the executable. Not a shell mode and not a variable. | day 1 part 1.2 | venv, the environment |
| Lockfile | The tool-written record of what a resolution actually produced — exact versions and content hashes — as against `pyproject.toml`, which records what was asked for. | day 1 part 2.1 | the lock, `uv.lock` |
| Tracked | A path git has been told to hold, from a `git add` onward. Ignore rules do not reach it: they speak only about paths git has never been told to hold. | day 2 part 1.1 | under version control |
| Staging area | The list of paths git is holding for the next commit — what `git add` writes into and `git rm --cached` removes from. A path in it is tracked, whatever any ignore rule says. | day 2 part 2.2 | git's index, the cache |
| Ignore source | One of the six places git reads exclude patterns from for a single path. Four are files in the repository; two are per-machine and invisible to review. | day 2 part 2.1 | exclude source |
| Negated pattern | An ignore line beginning `!`, which takes a path back out of the ignore list. It only works below the pattern it is excepting, because within one file the last match decides. | day 2 part 1.2 | a negation, an exception |
| Process environment | The set of name-to-string pairs the operating system handed a program when it started, which Python exposes as `os.environ`. It is built by whatever launched the program and has never heard of any file. | day 3 part 1.1 | the environment block, env vars |
| Floor | A dependency or interpreter requirement written as `>=`, which states what is too old and leaves the choice to whichever machine resolves it. Correct for a library, never sufficient for an application. | day 3 part 2.1 | a lower bound, a range |
| Exit status | The single number a process hands back when it ends, and the only channel through which a check reports its verdict to another program. Zero means success; everything printed to the screen is for humans. | day 3 part 2.2 | exit code, return code, `$?` |
