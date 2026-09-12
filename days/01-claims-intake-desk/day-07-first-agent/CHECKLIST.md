# P01 day 7 — definition of done

`python p.py done 01 7` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-the-agent/1.1-agent-is-a-configuration.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/01-the-agent/1.2-model-that-is-not-a-model.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/02-desk-with-a-reader/2.1-twelve-decided-and-what-it-cost.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/03-holding-it/3.1-what-the-tests-hold.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/03-holding-it/3.2-double-that-stopped-announcing-itself.md` — read · ran its check ·
      answered its question out loud

## Build

- [ ] `uv add "google-adk==2.8.0"` — **without** the `[mcp]` extra, and `mcp` still reports `2.2.0`
- [ ] `claims_desk/scripted.py` — the double, announcing itself three ways
- [ ] `claims_desk/models.py` — the marked diff: `SCRIPTED_PREFIX`, `name_of`, `pinned[T]`
- [ ] `claims_desk/agents/__init__.py` and `claims_desk/agents/classifier.py`
- [ ] `claims_desk/domain.py` — the marked diff: `Cover`, and `assess` taking one
- [ ] `claims_desk/desk.py` — `settled_without_reading`, the budget, the classifier asked last
- [ ] `tests/test_agent.py` — twelve tests
- [ ] `tests/test_desk.py` and `tests/test_domain.py` — updated **after** the gate told you to; two
      tests deleted rather than weakened
- [ ] `PACKAGES.md` — a dated row for `google-adk==2.8.0`, noting the extra was **not** installed
- [ ] `claims_desk/agents/classifier.py` — `TODO(me)`: fetch the peril vocabulary, or say why not
- [ ] `claims_desk/agents/classifier.py` — `TODO(me)`: count the instruction's characters × twelve
- [ ] `claims_desk/desk.py` — `TODO(me)`: the test for the rule-order assumption
- [ ] `tests/test_agent.py` — `TODO(me)`: `conftest.py`, or the argument against it
- [ ] Your own notes — `TODO(me)`: **run one notification against a real model and write down what
      differed.** Until that exists, this project has proved its own code and nothing about a model.

## Check

- [ ] The day's check is green: `./run check` — `All checks passed!`, `66 passed`, four `ok` lines
- [ ] Ran the queue end to end and compared the summary with `PROJECT.md`'s `Done when` paragraph
- [ ] **Break it on purpose, watch it go red, fix it.** Change `ScriptedClassifier`'s `model` to
      `"claims-classifier"` and call `models.pinned` on it. Expect
      `'claims-classifier' is not in this project's registry` — and notice the message says nothing
      about doubles. Put it back.
- [ ] Softened the instruction by deleting one prohibition and watched exactly one test object
- [ ] Moved the classifier call above the field rules, confirmed **no verdict changed**, and watched
      the budget test go red. Put it back.
- [ ] Read the framework's `Skipping missing token usage metadata` line and listed, out loud, three
      things this project cannot learn from its own transcripts
- [ ] `python p.py depth 01 7` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path — and the four changes
      to earlier files are marked diffs naming the day of THIS project that printed each original
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own earlier days
- [ ] Every agent's model goes through `models.pinned`, and the double announces itself in its name,
      in its answers, and to the registry

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the eight rows
      in the hub §10, restated definitions included
- [ ] `google-adk==2.8.0` has a dated row in this project's own `PACKAGES.md`. No `docs/PINS.md` row
      is owed, and the hub §10 says why
- [ ] No `docs/SOURCES.md` row is owed — nothing with a citation identifier was cited
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
