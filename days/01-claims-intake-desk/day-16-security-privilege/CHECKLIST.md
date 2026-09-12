# P01 day 16 — definition of done

`python p.py done 01 16` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-what-reaches-a-model/1.1-threat-model-as-a-table.md` — read · ran its check · answered
      its question out loud
- [ ] `parts/01-what-reaches-a-model/1.2-quarantining-what-a-caller-said.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/01-what-reaches-a-model/1.3-injection-through-a-tool-result.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/02-what-a-model-reaches/2.1-allowlist-that-says-none.md` — read · ran its check · answered
      its question out loud
- [ ] `parts/02-what-a-model-reaches/2.2-two-processes-two-sets-of-powers.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/03-what-leaves-the-boundary/3.1-record-the-desk-never-sees.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/04-who-signs/4.1-gate-and-a-signature-that-can-be-traced.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/05-holding-it/5.1-what-the-tests-hold.md` — read · ran its check · answered its question
      out loud
- [ ] `parts/05-holding-it/5.2-five-tests-five-earlier-days.md` — read · ran its check · answered its
      question out loud

## Build

- [ ] `claims_desk/security.py` — the module docstring, including the paragraph saying what this
      project **cannot** show about quarantine markers
- [ ] `claims_desk/security.py` — `THREATS`, six rows, five keys each
- [ ] `claims_desk/security.py` — the marked diff: `LOOKS_LIKE_AN_INSTRUCTION`, `QUARANTINE_OPEN`,
      `QUARANTINE_CLOSE`, `QUARANTINE_NOTE`, `quarantine`, `is_quarantined`
- [ ] `claims_desk/workflow.py` — the marked diff: `security.quarantine` at the one call site in
      `run_triage`, and **not** inside `sessions.turn`
- [ ] `claims_desk/security.py` — the marked diff: `TOOLS_ALLOWED`, both entries empty
- [ ] `claims_desk/security.py` — the marked diff: `APPROVAL_ABOVE`, `needs_approval`, `approval_note`
- [ ] `claims_desk/desk.py` — the marked diff: the gate, **above** the write and above the letter
- [ ] `tests/test_security.py` — twenty-five tests
- [ ] `tests/test_agent.py` — the marked diff, with the comment naming the claim and the figure
- [ ] `tests/test_cast.py` — the marked diff
- [ ] `tests/test_desk.py` — the marked diff
- [ ] `tests/test_hooks.py` — the marked diff
- [ ] `tests/test_record.py` — the marked diff
- [ ] Wired the gate **last**, and watched those five go red before editing any of them
- [ ] `claims_desk/security.py` — `TODO(me)`: the experiment that would prove a marker is obeyed
- [ ] `claims_desk/security.py` — `TODO(me)`: where `approval_note` should be called from
- [ ] `claims_mcp/tools.py` — `TODO(me)`: the safe version of part 1.3's change
- [ ] `claims_desk/agents/classifier.py` — `TODO(me)`: `build()` reading `TOOLS_ALLOWED`
- [ ] `tests/test_security.py` — `TODO(me)`: the test that would pass on an empty quarantined body
- [ ] Your own notes — `TODO(me)`: the shared queue expectation the five suites want

## Check

- [ ] The day's check is green: `./run check` — `All checks passed!`, `225 passed`, four `ok` lines
- [ ] Printed what the classifier actually receives and confirmed the note, the markers, and the
      description **unaltered**
- [ ] Ran an instruction-shaped description and confirmed it is **logged and not blocked**
- [ ] Confirmed *the system prompted me to call back* is **not** flagged
- [ ] Printed both agents' tool lists and the live docket
- [ ] Printed what the letter writer is sent and confirmed the description is not in it
- [ ] Moved `.env` away, started the boundary, listed its tools, and read the desk's `MissingKey`
- [ ] Printed the policy record against the boundary's answer and named the two withheld fields
- [ ] Ran `./run desk` and read `desk.awaiting_approval` with the estimate on it
- [ ] Confirmed eleven claim files and **no** `FNOL-4481.json`
- [ ] **Break it on purpose, watch it go red, fix it.** Blank one `defence` in `THREATS` and read
      `assert ''`. Then take the quarantine off `run_triage` and read the policyholder's raw sentence
      in the failure message. Then give the classifier a tool. Then import `claims_desk.util.keys`
      into `claims_mcp/tools.py`. Then move the approval gate below the write and notice that
      `awaiting_approval` is still logged. Put all five back.
- [ ] **The failure with no symptom.** Return the whole policy record from `fetch_policy`. Run
      `uv run pytest -q -p no:warnings --ignore=tests/test_security.py` and confirm **200 green**.
      Grep the claim files and the logs for `Kiln Row` and find nothing. Then run today's file and read
      the address in the failure message. Say out loud which function made the leak invisible. Put it
      back.
- [ ] **The failure that fails closed and still does harm.** Append the caller's words to `needed` in
      `draft_letter`. Run the queue, count the `desk.letter_failed` lines, and confirm the queue still
      reports seven deficiencies and records seven claims with no letter. Say out loud what day 11
      predicted and what actually happened. Put it back.
- [ ] Set `APPROVAL_ABOVE = 25_000`, ran the queue, and confirmed the gate never fires against this
      project's own data. Put it back.
- [ ] `python p.py depth 01 16` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path — and the changes to
      earlier files are marked diffs naming the day of THIS project that printed each original
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own earlier days
- [ ] Both deliberate-failure diffs were **reverted**; neither is in the tree at the end of the day
- [ ] No claim is made anywhere that a model **obeys** a quarantine marker — only that the marker is
      present, and the experiment that would test obedience is a `TODO(me)`
- [ ] No log line added today carries a policyholder's description, address or reference
- [ ] The five reddened tests were updated to the **actual numbers**, not weakened into comparisons
      that cannot fail

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the eight rows in
      the hub §10
- [ ] No `docs/PINS.md` row is owed — nothing was installed today
- [ ] No `docs/SOURCES.md` row is owed — nothing with a citation identifier was cited
- [ ] Noted honestly that the day-0 brief's *eight letters* is now *seven*, and said which of the two
      you think should change
- [ ] Noted that `test_every_decided_claim_reaches_the_claim_file` now has a name that is no longer
      strictly true, and said whether you renamed it
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
