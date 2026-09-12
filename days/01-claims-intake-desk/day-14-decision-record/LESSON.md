---
project: "P01"
day: 14
title: "The decision record: why this claim was fast-tracked, in a form an auditor accepts"
spine: 12
kind: mechanism
deploy_tier: D3
plan_version: "v4.1.0"
parts: 4
files_printed: [claims_desk/record.py, tests/test_record.py]
generated: "2026-09-11"
status: written
commit: ""
---

> **Yesterday:** the shape of an answer became a type — validated by the framework, refused when it
> named something this desk does not recognise.
> **Today:** why. Every decided claim gets a record holding exactly the facts the rules read, and a
> function that re-derives the verdict from that record alone — twelve claims, twelve replays that
> agree, and one edit that shows what a replay cannot prove.
> **Tomorrow:** reliability — what happens when the provider is not there, and how many times this
> desk is willing to ask.

## §1 The scene

An auditor does not ask what the desk decided. The claim file has said that since day 6.

They ask **why**, and the question has a shape that is easy to miss. It is not *tell me your
reasoning*. It is: **show me that this outcome follows from your own rules and the facts you had.**
Two things in front of them, and a conclusion they reach themselves without taking anybody's word.

Most of what this desk already keeps fails that test. A trace says what happened in order and
re-derives nothing. A log records how much and never what — correct for a log, useless as evidence.
A model's own explanation is prose that may or may not describe what the rules did, which is day 9's
argument about delegation arriving again.

What passes is narrow. **The inputs to the rule, the rule that fired, and the outcome**, written so
that `replay()` can take the record and nothing else — no store, no boundary, no model — and produce
the same verdict.

That gives the record a hard test for its contents, and the test is subtractive. It holds the eleven
facts `assess` reads. Not the description: no rule reads it, and a field in a decision record is read
by an auditor as having mattered. The letter is stored beside the record because a policyholder
received it, and its own schema description says it is not evidence.

Then the limit, stated rather than discovered. `defensible` compares a record's facts against its
verdict. Edit both consistently — the estimate and the outcome, two fields — and it passes. This desk
is **inconsistency-evident**, not tamper-evident, and the difference is a hash this project does not
have.

## §2 The map

Three sections. **Section 1 is what goes in a record and what stays out.** **Section 2 is the replay
and its limit.** **Section 3 is what holds it.**

### 1 · What a record is

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-what-a-record-is/1.1-facts-a-rule-reads.md) | The facts a rule reads, and nothing else | What belongs in a decision record? | working |
| [1.2](parts/01-what-a-record-is/1.2-provenance-and-citation.md) | Provenance, and the citation a handler can follow | Who decided, at what cost, and under which written rule? | working |

### 2 · Does it replay

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-does-it-replay/2.1-replay-and-what-it-cannot-prove.md) | The replay, and what it cannot prove | What does re-deriving a verdict actually establish? | production |

### 3 · Holding it

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-holding-it/3.1-what-the-tests-hold.md) | What the tests hold | How do you test a record, and what can a self-built test never find? | production |

## §3 Setup — run this

Nothing new is installed. One module is added, and three files gain a parameter each so a record can
reach the claim file.

```bash
./run check
```

Expect `157 passed` before you start — day 13's total — and `181 passed` at the end. One test from
day 6 goes red partway through, because the stub that stands in for `record_decision` needs the new
argument; that is the fourth time that stub has changed and it is the cost of a growing tool
signature.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `claims_desk/record.py` | part 1.1 |
| `tests/test_record.py` | part 3.1 |

Four earlier files change and each is a small addition rather than a rewrite: `claims_desk/desk.py`
gains `Verdict.record` and two builders, `claims_desk/workflow.py` returns the facts it decided on,
`claims_mcp/tools.py` takes a `decision_record` and refuses one filed against the wrong claim, and
`claims_desk/boundary.py` passes it across. Part 1.2 shows what reaches the claim file.

## §5 Build brief

Write `record.py` first and replay a hand-built record before wiring anything. Then thread the facts
out of the workflow, and let the gate tell you which stub needs updating. Then the reps:

| File | What it must do |
| --- | --- |
| `tests/test_record.py` | `TODO(me)`: the queue test writes the records it then replays, so it cannot see a rule change. Check in a fixture of records as JSON, written under today's rules, and replay those too. |
| `claims_desk/record.py` | `TODO(me)`: `RULES_VERSION` is a hand-bumped string nothing forces. Write the test that fails when `assess` changes and the version does not — and say what it has to hash to do that. |
| `claims_desk/record.py` | `TODO(me)`: `defensible` is inconsistency-evident and not tamper-evident. Write down what a hash over the stored record would cost operationally, and who would hold it. |
| `claims_desk/desk.py` | `TODO(me)`: `calls` is the budget breakdown at the moment of the verdict, so every deficiency record under-reports its letter drafts. Build the record after the letter, or rename the field. |
| Your own notes | `TODO(me)`: part 1.2 shows the letter stored twice — once at the top level from day 9 and once inside the record. Decide which copy is authoritative and what you would do about the other. |

## §6 The check that must be able to fail

```bash
./run check
```

Green is `All checks passed!`, `181 passed`, and day 0's four `ok` lines.

Ways to make it red:

1. **Add a field to `Facts` that no rule reads** — the policyholder's description, say.
   `test_the_facts_are_exactly_what_assess_reads` fails with a one-item difference, and the failure
   is the review conversation.
2. **Delete a handbook section that a reason cites.** `test_every_citation_on_every_reason_resolves`
   fails and names the reason, because a record with a citation nobody can follow is a footnote.
3. **Store `which_rule`'s answer as a field.** `test_the_rule_that_fired_is_derived_rather_than_stored`
   fails — a stored rule name is a second field written by the same code that wrote the outcome.
4. **Take `fire` out of `PHOTO_REQUIRED_FOR`** with records already on disk. One record stops being
   defensible: filed as `missing_photo_reference`, now replaying as `fast-track`. That is part 3.1 and
   it is the day's deliberate failure — and swapping two checks in `assess` instead breaks **nothing**,
   which is the more useful half.

## §7 Request budget

**Five model calls allowed per notification**, unchanged, and **seventeen spent across the queue** —
unchanged. A record is assembled from what the desk already had; nothing is asked of a model to
produce one, and nothing about the record is generated.

That is worth saying because the tempting version of this day is a model that writes an explanation.
It would read better and it would be a summary — a thing that has to be believed rather than checked
— which is the one property a decision record cannot have.

The record costs storage instead: roughly 700 bytes of JSON beside a claim file of about 200, so the
store is about four times larger. At a morning's several hundred notifications that is a few hundred
kilobytes a day.

## §8 Traps

- **A trace is not a decision record.** It says what happened in order and re-derives nothing.
- **A log is not one either**, and for the right reason: day 11's rule is that a log records how much
  and never what.
- **A model's explanation is the worst of the three** — fluent prose that may not describe what the
  rules did.
- **A record is defined by subtraction.** What the rule reads, and nothing else, including things
  that are true and relevant.
- **An auditor reads every field as having mattered.** That is the only reasonable way to read a
  document called a decision record.
- **Separate the facts from the provenance structurally**, not in prose. `replay` ignores provenance,
  and the sections are the claim about what was decisive.
- **Replay against the same `assess` the desk called**, never a copy — a copy would prove that two
  copies agree.
- **Derive the rule that fired; do not store it.** A stored rule name is a second field written by
  the same code, so comparing them proves nothing.
- **A replay is inconsistency-evident, not tamper-evident.** Edit two fields consistently and it
  passes.
- **A record read back later must still load** even when an enum has moved — so store the peril as a
  string and ask `peril_is_known` separately.
- **Hand-write the reason-to-citation mapping.** Day 12's retriever is 0.9 at `recall@3`, and a
  record is not the place for a one-in-ten chance.
- **Promising replayability means keeping every rule set you have decided under**, and that cost
  arrives about two rule changes in.
- **A test that creates its own evidence can only find bugs in the thing it did not create.**

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| One record, whole | this project | 2026-09-11 | `FNOL-4481`: eleven facts, provenance with `"model": "scripted/claims-classifier"` and `"rules_version": "2026-09-11.a"`, two citations, the letter, nested under `decision` beside day 6's three fields. |
| A record with no model in it | this project | 2026-09-11 | `FNOL-4473`: `loss_type: ''`, `model: ''`, `calls: {}` — day 7's ordering, visible in the record. |
| Every claim replays | this project, over the real boundary | 2026-09-11 | Twelve records, all eight reasons plus four fast-tracks, every one defensible from its own file. |
| An edited verdict is caught | this project | 2026-09-11 | `as edited : fast-track None defensible=False`, and the replay names what the facts actually produce. |
| An edited fact is caught | this project | 2026-09-11 | `limit edited to 9000 : ('fast-track', None) defensible=False`. |
| Both edited together is **not** caught | this project | 2026-09-11 | `estimate 4800 -> 400, outcome deficiency -> fast-track` → `defensible : True`. Two fields. |
| A rule change breaks history | this project, `fire` removed from `PHOTO_REQUIRED_FOR` | 2026-09-11 | `no longer defensible: 1` — `FNOL-4477` filed as `missing_photo_reference`, now replaying as `fast-track`. |
| And the suite cannot see a reordering | this project, two checks in `assess` swapped | 2026-09-11 | `24 passed`. The queue test writes its records with the same rules it replays them against. |
| A record for the wrong claim | this project, over the boundary | 2026-09-11 | `{"recorded": false, "refused": "the decision record is for a different claim"}` |
| The gate | this project, `./run check` | 2026-09-11 | ruff clean, `181 passed`, day 0's four checks green. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 01 | 14 | 2026-09-11 | The decision record: why this claim was fast-tracked, in a form an auditor accepts | 4 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — all new:

```text
| Decision record | The inputs a rule read, the rule that fired and the outcome, written so the verdict can be re-derived from the record alone. Not a trace, not a log, and never a summary. | P01 day 14 part 1.1 | an audit record |
| Replay | Re-deriving a decision from its record with no store, no boundary and no model, using the same rule function the system called rather than a copy of it. | P01 day 14 part 2.1 | re-derivation |
| Defensible | A record whose own facts, run through the system's own rules, produce the verdict it states. It is a claim about internal consistency and says nothing about whether the facts were edited. | P01 day 14 part 2.1 | internally consistent |
| Provenance | Who produced an input, at what cost, and against which version of the rules. Necessary for an audit and deliberately not part of the derivation — a replay ignores every field of it. | P01 day 14 part 1.2 | attribution |
| Rules version | An identifier for the rule set a decision was made under. Without it, replaying an old record against today's rules answers a question nobody asked. | P01 day 14 part 1.1 | `RULES_VERSION` |
| Tamper-evident | A property this desk does **not** have. A replay catches a record that stopped agreeing with itself; it cannot catch an edit made consistently, which needs a hash or a signature held somewhere the editor cannot reach. | P01 day 14 part 2.1 | inconsistency-evident, by contrast |
```

**`docs/PINS.md`** — no row is owed. Nothing was installed today.

**`docs/SOURCES.md`** — no row is owed. Nothing with a citation identifier was cited; the handbook
sections cited by records are this project's own synthetic file.

**Commit:**

```text
P01 day 14: The decision record
```
