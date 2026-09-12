# P01 day 17 — definition of done

`python p.py done 01 17` refuses to commit while any box below is unticked. That refusal is the
point: a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [ ] `parts/01-one-id/1.1-one-id-for-one-piece-of-work.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/01-one-id/1.2-carrying-it-across-a-process-line.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/02-where-the-time-went/2.1-span-that-was-not-there.md` — read · ran its check · answered
      its question out loud
- [ ] `parts/02-where-the-time-went/2.2-reading-a-queue-you-have-never-timed.md` — read · ran its
      check · answered its question out loud
- [ ] `parts/03-who-gets-woken/3.1-what-wakes-a-person.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/03-who-gets-woken/3.2-log-line-nobody-read.md` — read · ran its check · answered its
      question out loud
- [ ] `parts/04-holding-it/4.1-what-the-tests-hold.md` — read · ran its check · answered its question
      out loud

## Build

- [ ] `claims_desk/util/trace.py` — `TRACE_ENV`, `trace_id`, `span_stack`, `new_id`, `start`,
      `current`, `where`, `span`
- [ ] `claims_desk/util/logging.py` — the marked diff: `trace` and `span` read from the context, both
      omitted when empty, both overridable by an explicit field
- [ ] **Printed a trace before adding a single span**, so part 2.1's gap is something you saw rather
      than something you read about
- [ ] `claims_desk/boundary.py` — the marked diff: the trace id in the child's environment, with the
      whole environment beside it
- [ ] `tests/test_transports.py` — the marked diff: day 4's identity assertion, replaced by command
      and args
- [ ] `claims_desk/boundary.py` — the marked diff: `boundary.call`, `boundary.connect`,
      `boundary.tool`, and `timing["fields"]` — **not** `keys`
- [ ] `claims_desk/workflow.py` — the marked diff: a span round each agent turn, with `events` on it
- [ ] `claims_desk/desk.py` — the marked diff: `trace.start()`, the `queue` span, the `claim` span,
      the `continue` restructured into `elif`, and `desk.boundary_refused`
- [ ] `claims_desk/alerts.py` — `PAGE`, `TICKET`, `COUNT`, `RULES`, `BURSTS`, `UNCLASSIFIED`,
      `level_for`, `summarise`
- [ ] `tests/test_observability.py` — twenty-five tests, and `fresh` is **not** `autouse`
- [ ] `claims_desk/util/trace.py` — `TODO(me)`: whether to cache the environment read
- [ ] `claims_desk/boundary.py` — `TODO(me)`: the connection pool, with your own machine's number
- [ ] `claims_desk/boundary.py` — `TODO(me)`: the trace in the protocol's `meta` instead
- [ ] `claims_desk/alerts.py` — `TODO(me)`: where `summarise` should be called from
- [ ] `claims_desk/alerts.py` — `TODO(me)`: the rule for the connection cost, or the reason there is
      none
- [ ] `tests/test_observability.py` — `TODO(me)`: the well-formed-tree test
- [ ] Your own notes — `TODO(me)`: the `<redacted>` assertion over the whole queue

## Check

- [ ] The day's check is green: `./run check` — `All checks passed!`, `250 passed`, four `ok` lines
- [ ] Ran `./run desk`, picked a `trace` value, and grepped it — lines from **both** processes came
      back
- [ ] Confirmed the boundary's lines carry the trace and **no** `span`, and said why
- [ ] Totalled the `span` lines by name yourself and compared with the hub §9 table
- [ ] Wrote down **your own machine's** mean `boundary.connect` and mean `boundary.tool`
- [ ] Ran the two-line reproduction and read `"keys": "<redacted>"`
- [ ] Ran the whole queue through `alerts.summarise` and got `ticket` with no reasons
- [ ] **Break it on purpose, watch it go red, fix it.** Pass only the trace id to the subprocess and
      read `KeyError: 'PATH'`. Rename `fields` back to `keys` and read `span.keys says nothing`.
      Promote `desk.provider_unavailable` to `PAGE`. Remove the `reset` from `span`'s `finally`. Make
      `log` write `"trace": None`. Put all five back.
- [ ] **The failure that is green.** Remove the `boundary.connect` and `boundary.tool` spans, run the
      whole suite, and confirm **250 passed**. Read the trace, name the conclusion a reasonable person
      would draw, and name the file they would go and optimise. Put them back.
- [ ] **The fixture that disarms a test.** Make `fresh` `autouse=True` — still green. Then make `log`
      write `"trace": None` and confirm it is **still** green. Put both back and watch the second one
      go red.
- [ ] Created one `Client` at module level, reused it for the whole queue, and timed the run — then
      listed every property days 3, 10, 15 and 16 relied on that you gave up. Put it back.
- [ ] `python p.py depth 01 17` — green
- [ ] `python p.py check` — green across the whole repository

## Independence

- [ ] Every file this day printed was printed **in full**, at its real path — and the changes to
      earlier files are marked diffs naming the day of THIS project that printed each original
- [ ] Every concept this day used was **taught here**, at full depth — nothing discharged with a
      summary or a pointer
- [ ] Nothing in this day references another project — not a path, not a project name, and no
      sentence that assumes the reader has read one
- [ ] Nothing this day assumes was set up anywhere but in this project's own earlier days
- [ ] No timing in any part is quoted from this document rather than from your own run
- [ ] Nothing added today changes what the desk decides — twelve claims, four fast-tracked, seven
      recorded, one held, exactly as day 16 left them
- [ ] No log line added today carries a policyholder's description, address or reference

## Record

- [ ] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — the eight rows in
      the hub §10
- [ ] No `docs/PINS.md` row is owed — nothing was installed today
- [ ] No `docs/SOURCES.md` row is owed — nothing with a citation identifier was cited
- [ ] Noted honestly that `hooks.tool_result` shipped a redacted field for six days, and said what
      assertion would have caught it on day 11
- [ ] The `docs/PROGRESS.md` row is pasted from the hub §10, inside the `granth:ledger` block
- [ ] Committed with the message from the hub §10
