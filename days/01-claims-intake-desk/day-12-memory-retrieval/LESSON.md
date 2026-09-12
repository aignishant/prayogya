---
project: "P01"
day: 12
title: "Memory and retrieval"
spine: 11
kind: mechanism
deploy_tier: D3
plan_version: "v4.1.0"
parts: 6
files_printed: [data/handbook.md, claims_desk/recall.py, data/handbook_questions.json, tests/test_recall.py]
generated: "2026-09-10"
status: written
commit: ""
---

> **Yesterday:** the hooks that run around every model call — the budget charged before the call,
> a second lock on the letter writer, and a plugin that raised turning out to raise something else.
> **Today:** the difference between remembering and looking up. A handbook with an identifier per
> rule, a retriever you can recompute by hand, citations that resolve, a recall score that can fall,
> and the memory service this desk refuses to register.
> **Tomorrow:** structured output — the classifier stops answering in prose that has to be parsed
> and starts answering in a shape the framework enforces.

## §1 The scene

There is a folder on the counter that nobody files anything into.

It is the handbook: which perils need a photograph, what the fast-track is for, how many sentences a
deficiency letter may be. A handler reaches for it several times a morning, and what they are doing
when they reach for it is the opposite of remembering. The answer is the same for every claim, it
was written by the people who answer for it, and a handler working from memory would be working
from the wrong copy.

That is the distinction the whole day turns on. **Memory** is what a system keeps from one piece of
work into the next: per-person, growing, and forbidden here by the department's own rule. **Retrieval**
is looking something up in a body of text that does not change per claim: shared, versioned, and
belonging to nobody.

So today builds the corpus first — eight rules, one identifier each, split at their own headings —
and then a retriever made of arithmetic: term frequencies weighted by how rare each word is, and a
cosine between the question and each section. No provider, no embedding, no network. Every number in
this day can be recomputed by anyone holding the file.

Then the two things that make it honest. **Citations that resolve**, and an answer that hands back
sections rather than prose, because a summary is the thing a citation stops being able to check. And
**recall@k**, measured against ten questions somebody wrote by hand: 0.7 at k=1, 0.9 at k=3, with one
question it fails at every k and a named reason.

And the refusal. The framework offers a memory service and taking it is one keyword argument. Hand it
two claims and a single query — needing no claim reference — returns a policyholder's exact words.
That is HB-07, and this desk registers no memory service at all.

## §2 The map

Four sections. **Section 1 is the corpus and the index.** **Section 2 is what makes an answer
checkable** — citations, and the score that can fall. **Section 3 is the refusal.** **Section 4 is
what holds it.**

### 1 · The corpus

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [1.1](parts/01-the-corpus/1.1-handbook-on-the-counter.md) | The handbook on the counter | What goes in a corpus, and what is a chunk? | foundation |
| [1.2](parts/01-the-corpus/1.2-index-you-can-recompute.md) | The index you can recompute by hand | How does a retriever decide two things are similar? | working |

### 2 · Citations and the score

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [2.1](parts/02-citations-and-score/2.1-citations-that-resolve.md) | Citations that resolve | What makes a citation worth printing? | working |
| [2.2](parts/02-citations-and-score/2.2-recall-at-k.md) | recall@k, and the question it still gets wrong | How do you know your retrieval is any good? | production |

### 3 · Session versus memory

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [3.1](parts/03-session-versus-memory/3.1-what-the-desk-refuses-to-remember.md) | What the desk refuses to remember | What is the actual difference between a session and a memory? | production |

### 4 · Holding it

| Part | Title | What it answers | Level |
| --- | --- | --- | --- |
| [4.1](parts/04-holding-it/4.1-what-the-tests-hold.md) | What the tests hold | How do you test a retriever, and what does a score not tell you? | production |

## §3 Setup — run this

Nothing new is installed. Two data files and one module are added, and nothing that already exists
changes.

```bash
./run check
```

Expect `124 passed` before you start — day 11's total — and `141 passed` at the end. No earlier test
goes red today: this is the first day since day 7 that adds without rewiring.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `data/handbook.md` | part 1.1 |
| `claims_desk/recall.py` | part 1.2 |
| `data/handbook_questions.json` | part 2.2 |
| `tests/test_recall.py` | part 4.1 |

No earlier file changes. Part 3.1 quotes one line of `claims_desk/sessions.py` — printed in full on
day 8 part 1.1 — to show what is *not* on it.

## §5 Build brief

Write the handbook first and read it before writing any code; the corpus decides more about the
result than the retriever does. Then the index, then the evalset, then the tests. Then the reps:

| File | What it must do |
| --- | --- |
| `claims_desk/recall.py` | `TODO(me)`: add a stemmer so `sure`/`unsure` and `photograph`/`photographs` collapse. Measure **all ten** questions before and after, not the one you are fixing, and write both sets of numbers down. |
| `claims_desk/recall.py` | `TODO(me)`: part 4.1 shows a wrong answer and no answer scoring identically under `recall@k`. Design a second measurement that tells them apart, and say what it would cost to keep. |
| `data/handbook.md` | `TODO(me)`: add a ninth rule about police references for theft claims, then run `recall_at_k` again. Say what happened to the idf of `theft` and why one existing question moved. |
| `claims_desk/recall.py` | `TODO(me)`: `cited()` builds an `Index` when none is passed, re-reading the handbook off disk each time. Make it a module-level singleton, and say what that costs a test that wants a different corpus. |
| Your own notes | `TODO(me)`: this project cannot run an embedding model. Write down the two questions from part 2.2 you believe an embedding would fix, and what you would measure to find out whether it did. |

## §6 The check that must be able to fail

```bash
./run check
```

Green is `All checks passed!`, `141 passed`, and day 0's four `ok` lines.

Ways to make it red:

1. **Delete the ` · ` from one handbook heading.** That section is absorbed into the one **above**
   it, seven chunks come back instead of eight, and
   `test_the_handbook_splits_at_its_own_headings` names the missing identifier.
2. **Drop `re.MULTILINE` from `HEADING`.** The corpus loads as an empty list, every recall is `0.0`,
   and nothing anywhere says the handbook did not load.
3. **Return `scored[:k]` without the zero filter.** A question about xylophones comes back with three
   sections, three resolving citations and three scores of `0.0`.
4. **Add `"about"` to `STOPWORDS`.** Exactly one test goes red, the three recall numbers do not move
   at all, and the escalation question changes from a confidently wrong answer to no answer — an
   improvement the score cannot see. That is part 4.1 and it is the day's deliberate failure.

## §7 Request budget

**No model calls at all.** Nothing in `claims_desk/recall.py` contacts a provider, and the desk's
per-notification ceiling is untouched at five.

That is the point rather than an omission. Retrieval over a corpus this size is arithmetic — eight
cosines per question — and a project that reaches for a model to compare two pieces of text before
trying `log(N/n)` has bought a dependency, a bill and an outage mode for a similarity it could have
computed. The place a model belongs is writing prose from the sections that come back, and day 9
already built that.

Two tests in `tests/test_recall.py` do run a real agent turn, through the stand-in, because part
3.1's demonstration needs two real sessions to hand to a memory service.

## §8 Traps

- **A retrieval system is mostly its corpus.** The chunk boundary and the identifier decide more
  about the answer than the similarity function does.
- **Split on the document's structure, not on a character count.** Half a rule can say the opposite
  of the rule.
- **A heading that stops matching does not lose its own section** — it dissolves into the section
  above it, and the rule that disappears is not the one you edited.
- **An identifier is a name, not a position.** `HB-02`, never "the second heading".
- **A citation that resolves is not a citation that is relevant.** Two properties, two tests, and the
  easy one to write is the one that does not matter alone.
- **A retriever must be able to return nothing.** One that always returns `k` results always cites
  something.
- **A confident score is not a correct answer.** This desk's highest score on the page — `0.406` —
  is on a wrong answer.
- **No stemming means `sure` and `unsure` are unrelated words**, and a question can share *zero*
  terms with the section that answers it.
- **`recall@k` cannot tell a wrong answer from no answer.** Both score the same and they are not the
  same thing.
- **An evalset written out of the corpus is an exam the retriever cannot fail.** Write questions in
  the words a person would use.
- **Editing the stop list until the score improves is tuning the measurement**, not the retriever.
- **The difference between a session and a memory is not the data.** It is whether the events can be
  reached without knowing which claim they belong to.
- **Before adding memory, say what the deletion path is.** If the answer is "search for their words",
  there is no deletion path.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| The corpus splits at its headings | this project | 2026-09-10 | Eight chunks, `HB-01` to `HB-08`, 242 to 412 characters — a seventy per cent spread, which is the document's own. |
| A heading that stops matching | this project, deliberately broken | 2026-09-10 | `HB-02` gone and `HB-01` at 790 characters: the section is absorbed by the one **above** it. |
| The index answers | this project | 2026-09-10 | `HB-02` at `0.32` for the photograph question; `HB-03` at `0.15` against `HB-02` at `0.132` for the injury question. |
| And gets one wrong at the top | this project | 2026-09-10 | *"May I tell the policyholder the fast track limit"* → `HB-01` at `0.406`, `HB-04` at `0.194`. The highest score on the page is a wrong answer. |
| An empty corpus is silent | this project, `re.MULTILINE` removed | 2026-09-10 | `[]`, `index over 0 chunks`, `recall@3 -> 0.0`, and no error anywhere. |
| Nothing to match | this project | 2026-09-10 | `{'question': 'xylophone quantum bassoon', 'found': 0, 'sections': []}` |
| Without the zero filter | this project, deliberately broken | 2026-09-10 | Three sections at `score: 0.0`, all three citations resolving, `resolves('handbook.md#HB-01') = True`. |
| recall@k | this project | 2026-09-10 | `0.700` at k=1, `0.800` at k=2, `0.900` at k=3, with every miss named. |
| Why the escalation question fails | this project | 2026-09-10 | The question shares **no terms at all** with HB-08; it shares one with HB-07 — `about`, idf `1.39`. At k=8 only `['HB-07', 'HB-01']` ever score. |
| Removing that one word | this project, deliberately broken | 2026-09-10 | `1 failed, 17 passed`; all three recall numbers unchanged; the miss becomes `('HB-08', [])` — no answer instead of a wrong one. |
| What a memory service does | this project, `InMemoryMemoryService` | 2026-09-10 | `FNOL-4472 mentions the hose: False`, then a query with no claim reference returns `author=user  the flexible hose let go overnight`. |
| The gate | this project, `./run check` | 2026-09-10 | ruff clean, `141 passed`, day 0's four checks green. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 01 | 12 | 2026-09-10 | Memory and retrieval | 6 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — all new:

```text
| Retrieval | Looking something up in a corpus that does not change per unit of work. Shared, versioned, belonging to nobody — as against memory, which is kept per person and grows. | P01 day 12 part 1.1 | lookup, search |
| Chunk | One unit a retriever can return: here, one section of the handbook, split at the document's own heading rather than at a character count, because half a rule can say the opposite of the rule. | P01 day 12 part 1.1 | a passage, a segment |
| Inverse document frequency | How rare a term is across a corpus, `log(N / n)`, used to weight it. A word in every section scores zero, which is arithmetic saying what a reader already knows: common words do not tell two documents apart. | P01 day 12 part 1.2 | idf |
| Cosine similarity | The angle between two weighted term vectors, from 0 to 1, which ignores length — so the longest section does not win every question by containing more words. | P01 day 12 part 1.2 | the cosine |
| Top-k | The `k` best-scoring chunks for a question. A maximum and not a quota: a retriever that always returns `k` results always cites something. | P01 day 12 part 2.1 | the top k |
| Citation | An identifier an answer prints so a reader can go and check it. Two properties, both testable and independent: it **resolves** to a section that exists, and it is **relevant** to the question. | P01 day 12 part 2.1 | a source, a reference |
| recall@k | The share of a written-down set of questions whose expected chunk is somewhere in the top `k`. A number that can go down, and one that cannot tell a wrong answer from no answer. | P01 day 12 part 2.2 | recall |
| Memory service | A store of past conversations searchable by content rather than by the unit of work they belong to. That last property is the whole difference from a session, and it is what makes a deletion request unanswerable. | P01 day 12 part 3.1 | long-term memory |
```

**`docs/PINS.md`** — no row is owed. Nothing was installed today.

**`docs/SOURCES.md`** — no row is owed. `data/handbook.md` is synthetic and written for this project.

**Commit:**

```text
P01 day 12: Memory and retrieval
```
