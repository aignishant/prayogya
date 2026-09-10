# Day 2 — definition of done

`python p.py done 2` refuses to commit while any box below is unticked. That refusal is the point:
a day is finished when it is understood and the checks are green, and by nothing else.

No box here carries a time estimate, and none ever will.

## Read

- [x] `parts/01-the-order/1.1-the-rule-before-the-file.md` — read · ran its check · answered its question out loud
- [x] `parts/01-the-order/1.2-the-example-that-carries-the-shape.md` — read · ran its check · answered its question out loud
- [x] `parts/02-asking-git/2.1-the-line-that-decided.md` — read · ran its check · answered its question out loud
- [x] `parts/02-asking-git/2.2-the-file-git-had-already-seen.md` — read · ran its check · answered its question out loud

## Build

- [x] `projects/00-foundry/.gitignore` — typed **before** creating anything it names, and I can say what each of its four secret patterns is there to catch that the others are not
- [x] `projects/00-foundry/.env` — created with a synthetic value, and I predicted which line git would name **before** running the check
- [x] `projects/00-foundry/.env.example` — typed, and there are zero characters after the `=`
- [x] The negation line added, and I can say why it sits below `.env.*` rather than above it — without re-reading part 1.2
- [x] I can point at the one file in `projects/00-foundry/` that is committed and holds key *names*, and the one that is never committed and holds key *values*

## Check

- [x] `git status --short .` in `projects/00-foundry` — `.env.example` listed, `.env` absent, both on disk
- [x] `git check-ignore -v .env` — names `projects/00-foundry/.gitignore`, not the repository root's file, and I can say why
- [x] `git add .env` — refused, exit `1`, and I read both hint lines rather than the first
- [x] `git check-ignore -v .env.example` and `git check-ignore .env.example` — run both, and I can say why the exit statuses differ on the same file
- [x] The same two paths asked from the repository root — a different source file and different line numbers, and I can say which rule governs which subtree
- [x] **Break it on purpose, watch it go red, fix it.** Move `!.env.example` above `.env.*`, run `git check-ignore -v .env.example` and `git status --short .`, watch the example file leave the output with no error anywhere, then put the line back
- [x] **Second break.** Append `!.env` to `projects/00-foundry/.gitignore`, watch `git status` start offering the real secret, and say which documented rule made a lower-level file overrule the root one. Remove the line
- [x] **Third break — the day's own failure.** Park the ignore file, create `service-account.json`, `git add .`, restore the ignore file, then run `git check-ignore -v` on it: **no output, exit `1`**. Run it again with `--no-index` and watch line 10 appear. Fix with `git rm --cached`, and confirm the file is still on disk
- [x] I ran the wrong-order sequence through to a **commit** in a throwaway repository outside this one, then `git rm --cached`, then found the file in `git log -p` — and I can say why rotation is the fix and not a git command
- [x] **Fourth break — the document.** Delete a `## In production` heading from any part, run `python p.py depth 2`, see it named, restore it
- [x] `python p.py depth 2` — green
- [x] `python p.py check` — green across the whole repository

## Record

- [x] Every term defined for the first time today has a row in `docs/GLOSSARY.md` — tracked, staging area, ignore source, negated pattern
- [x] `docs/PINS.md` — nothing to add; git's version was re-observed today with the same value day 0 recorded, and the re-check is dated in the hub §9
- [x] `docs/SOURCES.md` — nothing to add; the two git documentation pages are dated in the hub §9, and I checked rather than assumed
- [x] `projects/00-foundry/.env` is on my disk and in **no** commit — I verified with `git log --all -- projects/00-foundry/.env` rather than by remembering
- [x] The `docs/PROGRESS.md` row is pasted from the hub §10
- [x] Committed with the message from the hub §10
