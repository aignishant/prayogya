---
project: "P01"
day: 16
title: "Security and privilege"
spine: 14
kind: mechanism
deploy_tier: D3
plan_version: "v4.1.0"
parts: 9
files_printed: [claims_desk/security.py, tests/test_security.py]
generated: "2026-09-11"
status: written
commit: ""
---

> **Yesterday:** reliability — three attempts on day 1's schedule, the provider's own `Retry-After`
> beating it, an idempotency key so a retried write lands once, and an escalation instead of a
> fabricated default.
> **Today:** the threat model for this desk, written as data a test can read. What reaches a model
> and what a model reaches: a quarantined description, injection arriving through a tool result, an
> allowlist that says none, two processes holding different powers, a policy record the desk never
> sees, and a gate that holds a large claim until a person signs.
> **Tomorrow:** observability — one correlation id across every agent and every hop, the span that is
> missing and how you find it, and what you page a human about.

## §1 The scene

Look at what is on a claims handler's desk: the notification form somebody typed, the policy schedule
off the policy system, a page of the caller's own words taken down during the call, and the
departmental handbook with a version on its spine.

Four pieces of paper, and a handler with ten years on the floor treats all four differently. The
schedule is as near fact as this floor gets. The form is somebody's typing. The handbook is authority.
And the page of notes is not information about the loss at all — it is a record that somebody said
something, which is a different kind of object, and the day you forget that is the day a caller talks
you into writing *urgent* on a form because they said it in a confident voice.

That is the whole of today. There is no separate security subject here; there is one question asked
twice — **what can reach a model, and what can a model reach** — and every part of this day answers one
half or the other.

The uncomfortable thing about this day is how little code it adds. The boundary has returned cover
rather than policy records since day 3. Neither agent has had a tool since day 7. Day 9 gave each
agent its own conversation, day 11 put a second lock on the letter writer's request, day 13's schema
has refused anything outside its enum since it was written. Those are security controls, and none of
them was called one. So most of today is the act of **naming what was already true** — because a
control nobody wrote down is one refactor from disappearing, and a control with no test is a sentence
in a wiki.

Two things today are genuinely new. The description is now wrapped and labelled on its way to a model.
And above an estimate of 2500 the desk decides and then **holds**, which is the first time this project
has built something that deliberately refuses to finish its own work.

## §2 The map

Nine parts in five sections, and the sections are the two halves of the question plus what follows from
them.

### 1 · What reaches a model

The threat model as data, then the two routes untrusted text takes into a prompt — the user message,
which everybody wraps, and the tool result, which nobody does.

| Part | Title | Level |
| --- | --- | --- |
| 1.1 | The threat model, as a table the tests read | foundation |
| 1.2 | Quarantining what a caller said | working |
| 1.3 | Injection arriving through a tool result · **failure** | production |

### 2 · What a model reaches

The other half. What an agent may call, and what the process it runs in is allowed to hold.

| Part | Title | Level |
| --- | --- | --- |
| 2.1 | The allowlist that says none | working |
| 2.2 | Two processes, two sets of powers | working |

### 3 · What leaves the boundary

One tool, one projection, and a leak with no symptoms.

| Part | Title | Level |
| --- | --- | --- |
| 3.1 | The record the desk never sees · **failure** | production |

### 4 · Who signs

The gate, where it sits, and what an approval has to say to be worth anything.

| Part | Title | Level |
| --- | --- | --- |
| 4.1 | The gate, and a signature that can be traced | production |

### 5 · Holding it

The suite, and the bill the gate sent to five earlier days.

| Part | Title | Level |
| --- | --- | --- |
| 5.1 | What the tests hold | production |
| 5.2 | Five tests, five earlier days | production |

## §3 Setup — run this

Nothing new is installed. One module is added, one test file, and seven earlier files change.

```bash
./run check
```

Expect `200 passed` before you start — day 15's total — and `225 passed` at the end. **Five tests from
earlier days go red partway through**, when the approval gate arrives: one each from days 6, 7, 9, 11
and 14, all of them asserting the queue's totals. That is not breakage and it is not a surprise to be
worked around; it is part 5.2, and reading those five failures before editing them is the exercise.

## §4 Files this day prints

| File | Printed by |
| --- | --- |
| `claims_desk/security.py` | part 1.1 |
| `tests/test_security.py` | part 5.1 |

`claims_desk/security.py` is printed whole in part 1.1 holding the threat model, and then grows by
marked diff as the day's argument does: the quarantine in part 1.2, the tool allowlist in part 2.1, the
threshold and the two approval functions in part 4.1.

Seven earlier files change, each as a marked diff naming the day of this project that printed the
original: `claims_desk/workflow.py` (day 10) in part 1.2, `claims_desk/desk.py` (day 6) in part 4.1,
and in part 5.2 the five test files from days 6, 7, 9, 11 and 14. Part 1.3 and part 3.1 each print a
diff against `claims_mcp/tools.py` (day 5) that is applied, observed and **reverted** — those are the
day's two deliberate failures and neither one ships.

## §5 Build brief

Write `security.py` in the order the day argues it: the threat table first and its two tests, then the
quarantine and its call site in `run_triage`, then the allowlist, then the threshold and the gate. Wire
the gate last, because that is when the five earlier tests go red and you want to be able to see that
it was the gate that did it. Then the reps:

| File | What it must do |
| --- | --- |
| `claims_desk/security.py` | `TODO(me)`: nothing here proves a model *obeys* a quarantine marker — the stand-in reads no instructions. Write down what the experiment would be: which model, how many adversarial descriptions, and how you would choose the passing number. |
| `claims_desk/security.py` | `TODO(me)`: `approval_note` has no call site. Say where it should be called from, which field of day 14's `DecisionRecord` it lands in, and what `record.defensible` should do with an approval. |
| `claims_mcp/tools.py` | `TODO(me)`: the safe version of part 1.3's change — the caller's words in their own key, quarantined at the prompt. Name the test of today's you would have to change, and why that change is honest. |
| `claims_desk/agents/classifier.py` | `TODO(me)`: make `build()` read its tool list from `security.TOOLS_ALLOWED` rather than being described by it. Say what breaks, and whether the breakage is a cost or the feature. |
| `tests/test_security.py` | `TODO(me)`: one test here would still pass if `quarantine` wrapped an **empty** body. Find it and write the assertion that catches it. |
| Your own notes | `TODO(me)`: five suites assert the queue's totals independently. Sketch the shared expectation that would make the next control a one-line change, and say which suites would still need their own assertions. |

## §6 The check that must be able to fail

```bash
./run check
```

Green is `All checks passed!`, `225 passed`, and day 0's four `ok` lines.

Ways to make it red:

1. **Blank a `defence` in `THREATS`.** `test_every_untrusted_source_has_a_named_defence` fails with
   `assert ''` — somebody called a source untrusted and wrote nothing about it.
2. **Take the quarantine off the call site in `run_triage`.** One test fails, and the policyholder's
   raw sentence appears in the failure message where the wrapped string should be.
3. **Give the classifier a tool.** `test_no_agent_in_this_desk_has_a_tool` fails — and note that the
   `TOOLS_ALLOWED` half of it is still perfectly true, which is the point of asserting both.
4. **Import `claims_desk.util.keys` anywhere in `claims_mcp/`.** The failure names the file.
5. **Move the approval gate below the write.** `test_a_held_claim_is_not_recorded` fails — and the
   `awaiting_approval` log line still appears, which is what makes a misplaced gate so convincing.

And the two that are green for two hundred tests, which are this day's deliberate failures:

- **Part 1.3** — have `draft_letter` append the caller's words to `needed`. Day 11's request hook
  catches it and fails closed, so no letter goes out; and `run_queue` still reports seven deficiencies,
  records seven of them, and sends nobody a letter.
- **Part 3.1** — return the whole policy record from `fetch_policy`. **200 tests pass**, nothing is
  logged, nothing reaches disk, no behaviour changes, and a policyholder's home address is in the
  process that runs models and holds the provider key.

## §7 Request budget

**Five model calls allowed per notification**, unchanged. **Fifteen spent across the queue**, down
from seventeen, and the gate is the whole difference. Measured both ways: with the gate, eight
classifications and seven letters; with `APPROVAL_ABOVE` raised out of range, eight classifications and
**nine** letters — because eight letters cost nine calls, one of them having needed a second draft, and
that one was FNOL-4481. So the held claim was costing two drafting calls and now costs none.

The quarantine is the other cost, and it is tokens rather than calls. The note is about four hundred
characters and it is prepended to every classification — twelve times here, and part 1.2's production
note works out what that figure looks like at an intake desk taking thousands of notifications a day,
which is where somebody starts arguing for moving it into the system instruction.

Part 1.3's failure is worth a line in this section too, because it is a budget event as well as a
security one: a guaranteed refusal still pays. Day 11 established that the plugin charges before the
request hook runs, so each held-back draft costs its call, and a poisoned tool result burns three calls
per deficiency to produce no letter.

## §8 Traps

- **There is no security subject here.** There is *what can reach a model* and *what a model can
  reach*, and everything else is an answer to one of them.
- **A threat model in a document decays.** Keep it where a test can read it and a diff has to change
  it.
- **A row that says "untrusted" and names no defence is a worry, not a control.**
- **Instructions and data arrive in the same channel.** That is the shape of the technology, not a bug
  somebody introduced, and it is why marking the boundary of a quotation is the best available move.
- **A pattern list is a signal, never a filter.** One people believe is complete is worse than none.
- **Log the phrase that matched, not the text it was in.** A log line is not the place for a
  policyholder's account of a fire.
- **The dangerous input is the tool result**, because it arrives on letterhead and nobody wraps it.
- **Assert equality against a trusted constant, not containment.** An injection that *appends* passes a
  containment check.
- **Test the boundary crossing, not the helper.** A green test of `quarantine()` proves a function
  concatenates strings.
- **An absent capability should be absent on purpose, in writing.** An empty allowlist is a sentence;
  no allowlist is a shrug, and a shrug is what the next person fills in.
- **A model that cannot call a tool cannot be talked into calling one.**
- **When a process needs a new kind of power, ask whether it should be a new process.**
- **One place turns a credential into a value in memory.** Everything downstream is arithmetic.
- **Test an absence by reading the source**, because there is no behaviour to exercise — and make the
  pattern as specific as the claim, or the next person loosens the assertion instead of the pattern.
- **The boundary answers questions; it does not hand over records.**
- **Assert that the sensitive field is in the store as well as absent from the answer**, or the test
  passes because the data was never there.
- **A control whose violation produces no symptom can only be held by a test.**
- **An authority limit restricts what may be acted on, not what may be assessed.** Hand a human the
  verdict, not a blank file.
- **An approval records what the approver was shown.** A signature on a blank page is worth nothing.
- **A gate that logs and does not stop anything is theatre** — and it produces exactly the evidence
  that makes people believe the control exists.
- **Choose the threshold from the data.** A gate that never fires against your own fixtures is
  indistinguishable from one that does not work.
- **A reddened test is a witness.** Read what it says before editing it, and never widen a comparison
  to make it green.

## §9 Verified today

| What | Where it was checked | Date | What it confirmed |
| --- | --- | --- | --- |
| The quarantine, as the model receives it | this project, spying on `generate_content_async` | 2026-09-11 | The note, then `<<<BEGIN_UNTRUSTED_CLAIM_TEXT>>>`, then the description unaltered, then the close marker — in the first user message. |
| ADK's own fencing wording | this project, day 9's transfer transcript | 2026-09-11 | `<<<BEGIN_QUOTED_AGENT_CONTENT>>>` with a sentence saying the contents are data and never instructions — the precedent the marker wording follows. |
| The instruction-shaped signal | this project | 2026-09-11 | `security.instruction_shaped_input` with `"matched": "ignore your instructions", "chars": 109`, and the claim **not** blocked. |
| A false positive that does not fire | this project | 2026-09-11 | *the system prompted me to call back* — ordinary English containing "system prompt", not flagged. |
| Every agent's tool list | this project | 2026-09-11 | `classifier tools=[] allowed=()` and `letter_writer tools=[] allowed=()`. |
| The docket | this project, live server | 2026-09-11 | `fetch_policy, check_in_force, record_decision, read_decision, draft_letter` — five, in `DECLARED` order. |
| What the letter writer is sent | this project, spying on the stand-in | 2026-09-11 | `'Claim: FNOL-4477\nReason: missing_photo_reference\nThe policyholder must send or confirm: a photograph of the damage'` — and the description **not** present. |
| The boundary with no key on disk | this project, `.env` moved away | 2026-09-11 | All five tools listed and `fetch_policy` answering normally; the desk in the same state raised `MissingKey: GOOGLE_API_KEY is not set`. |
| What crosses the boundary | this project | 2026-09-11 | Ten fields on disk, nine across the wire, `withheld: ['holder_ref', 'risk_address']`. |
| The PII leak, unobserved | this project, `asdict` applied deliberately | 2026-09-11 | `200 passed` with every pre-today test green; nothing in `data/claims/` or the logs; `'risk_address': '12 Kiln Row, Barrowfield'` visible only in today's failure message. |
| The tool-result injection | this project, `draft_letter` poisoned deliberately | 2026-09-11 | Three `hooks.refused_leak` lines per deficiency, then `desk.letter_failed`; `queue_finished` still reporting `deficiency: 7`; seven records on disk with no letter; four tests red. |
| The approval gate | this project, `./run desk` | 2026-09-11 | `desk.decided` with `above_fast_track_limit`, then `desk.awaiting_approval` with `"estimate": 4800`, then `fast-track: 4, deficiency: 7, pending: 1` and eleven claim files with no `FNOL-4481.json`. |
| The threshold against the data | this project | 2026-09-11 | Every `fast_track_limit` is 2500 or under; the only notification above 2500 is FNOL-4481 at 4800. |
| A gate below the write | this project, moved deliberately | 2026-09-11 | `awaiting_approval` logged, and `FNOL-4481` in the claims directory — the log line appears either way. |
| The gate | this project, `./run check` | 2026-09-11 | ruff clean, `225 passed`, day 0's four checks green. |

## §10 Ledger & commit

**`docs/PROGRESS.md`** — pasted into the `granth:ledger` block:

```text
| 01 | 16 | 2026-09-11 | Security and privilege | 9 | <hash> | yes |
```

**`docs/GLOSSARY.md`** — new rows:

```text
| Threat model | The list of what can reach a model in a system and what a model can reach from it, with a trust level and a named defence per source. Kept as data in the source tree so a test can refuse a row that has no defence. | P01 day 16 part 1.1 | what you are defending against |
| Prompt injection | Text that arrives as data and is read as instruction, because instructions and data travel in the same channel. Not an exploit: a property of how these systems are built. | P01 day 16 part 1.2 | talking a model into something |
| Quarantine | Wrapping untrusted text in distinctive markers behind a sentence saying what it is, so a model is told which text is a quotation rather than left to guess. Present and testable; obedience is a separate question needing a real model. | P01 day 16 part 1.2 | fencing off untrusted text |
| Tool allowlist | A written statement of which tools each agent may call, kept where a diff has to change it. "None" is a value, and recording it is what stops an absence being filled in by the next person. | P01 day 16 part 2.1 | which tools an agent gets |
| Scoped credentials | Each process holding only the powers its own job needs, enforced by what it imports and what it runs rather than by policy — so a compromise of one does not carry the other's capability. | P01 day 16 part 2.2 | least privilege, per process |
| Projection at the boundary | Returning named fields that answer the question asked instead of the record that contains the answer, so data nothing reads never enters the calling process. | P01 day 16 part 3.1 | data minimisation |
| Approval gate | A threshold above which a decision is reached and then held, unrecorded and unacted on, until a person agrees. It restricts what may be acted on, never what may be assessed. | P01 day 16 part 4.1 | a human in the loop, with a limit |
| Audit trail | A record of who approved what and which fact they were shown, stored with the decision. An approval that does not say what the approver was looking at is a signature on a blank page. | P01 day 16 part 4.1 | who signed, and for what |
```

**`docs/PINS.md`** — no row is owed. Nothing was installed today.

**`docs/SOURCES.md`** — no row is owed. Nothing with a citation identifier was cited.

**Commit:**

```text
P01 day 16: Security and privilege
```
