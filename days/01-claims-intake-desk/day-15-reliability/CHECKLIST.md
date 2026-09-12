# P01 day 15 — definition of done

`python p.py done 01 15` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-asking-again/1.1-honest-retry.md` — read · ran its check · answered its question out
      loud
- [ ] `parts/01-asking-again/1.2-write-that-must-not-happen-twice.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/02-what-not-to-do/2.1-answer-you-must-not-fabricate.md` — read · ran its check ·
      answered its question out loud
- [ ] `parts/03-holding-it/3.1-what-the-tests-hold.md` — read · ran its check · answered its question
      out loud

## Build

- [ ] `claims_desk/reliability.py` — `ATTEMPTS`, `WAITS`, `LONGEST_HONOURED_WAIT`, `Unavailable`,
      `wait_for`, `with_retry`, `idempotency_key`, `already_written`
- [ ] Tested `wait_for` on its own **before** writing anything that retries
- [ ] `claims_desk/scripted.py` — `ScriptedTransient`, announcing itself like every other double
- [ ] `claims_mcp/tools.py` — the marked diff: `idempotency_key`, the repeat, and the refusal for a
      different decision
- [ ] `claims_desk/boundary.py` — the wrapper carries the key
- [ ] `claims_desk/desk.py` — the marked diff: the key built from what is about to be written
- [ ] `claims_desk/desk.py` — the marked diff: `UNAVAILABLE`, the retry around triage, and the
      escalation
- [ ] `tests/test_desk.py` — the `record_decision` stub updated **after** the gate told you
- [ ] `tests/test_reliability.py` — nineteen tests, none of which sleeps
- [ ] `claims_desk/reliability.py` — `TODO(me)`: the circuit breaker, with what it counts
- [ ] `claims_mcp/tools.py` — `TODO(me)`: the conditional write, and what it costs
- [ ] `claims_mcp/tools.py` — `TODO(me)`: the backfill for keyless claims, or the reason not to
- [ ] `tests/test_reliability.py` — `TODO(me)`: the one test that uses the real `asyncio.sleep`
- [ ] Your own notes — `TODO(me)`: the shape that replaces a six-parameter `record_decision`

## Check

- [ ] The day's check is green: `./run check` — `All checks passed!`, `200 passed`, four `ok` lines
- [ ] Printed the waiting policy and confirmed a provider asking for 900 seconds waits 30
- [ ] Ran a busy provider that recovers, and confirmed the waits were the provider's and not day 1's
- [ ] Ran a provider that never answers and read all four log lines
- [ ] Ran a retry with an empty budget and confirmed **one** attempt and **no** waits
- [ ] Wrote the same decision twice and confirmed one claim file and a `repeat: True`
- [ ] Wrote a **different** decision under a new key and read the refusal
- [ ] Wrote twice with **no** key and watched the second write win silently
- [ ] Ran an escalating claim and confirmed the claims directory is empty afterwards
- [ ] **Break it on purpose, watch it go red, fix it.** Default the classification on
      `Unavailable` — `peril_not_covered`, the conservative choice — and run the whole queue with the
      provider down. Twelve claims decided, twelve records, every one defensible, and FNOL-4477's
      record says its policy does not cover an escape of water on a policy that does. Say out loud
      which of this project's two hundred tests would have caught it. Put it back.
- [ ] Made `Watch` actually sleep, timed the file, and put it back
- [ ] `python p.py depth 01 15` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path — and the changes to
      earlier files are marked diffs naming the day of THIS project that printed each original
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own earlier days
- [ ] Nothing anywhere returns a substitute answer when a provider is unavailable
- [ ] No log line carries a count of attempts that were not made

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the six rows in
      the hub §10, the restated definition included
- [ ] No `docs/PINS.md` row is owed — nothing was installed today
- [ ] No `docs/SOURCES.md` row is owed — nothing with a citation identifier was cited
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
