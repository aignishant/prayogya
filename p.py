#!/usr/bin/env python3
"""p — the whole authoring toolchain for this curriculum repository, in one file.

    python p.py status | brief NN D | start NN D | parts NN D | new NN D [slug]
                depth NN [D] [--list] | codemap NN | index [--check]
                check | verify NN | done NN D | doctor

Stdlib only, Python 3.11+ (tomllib). A repository that teaches you something should not need a
package install before it can check itself.

Addressing is a **project and a day**: `python p.py brief 01 7` is day 7 of project 01. There is no
global sitting number and no curriculum ID scheme — v4 deleted both, because both encoded a single
global reading order and a reader may start at project 27 (plan §15, ADR-0006).

The master plan is the single source of truth for *what the curriculum is*: the project list, the
eighteen-slot spine and each project's extra days live there between `<!-- granth:...:start -->`
markers, so a person reading the plan and this script parsing it cannot disagree. A project's day
map is **expanded** here from the spine plus that project's inserts, so the two can never drift.
granth.toml holds only what the plan cannot express.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

if sys.version_info < (3, 11):  # pragma: no cover
    sys.exit("granth: needs Python 3.11 or newer (tomllib is stdlib from 3.11).")

import tomllib

ROOT = Path(__file__).resolve().parent

# Day titles carry em dashes and non-Latin words, and a Windows console still defaults to a legacy
# code page. Line buffering keeps this script's own output in order with its subprocesses'.
for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        try:
            _s.reconfigure(encoding="utf-8", line_buffering=True)
        except (ValueError, OSError):  # pragma: no cover
            pass

# =============================================================================================
# Configuration
# =============================================================================================

# The seven part sections. The order is the pedagogy — claim, scene, real code, walkthrough,
# failure, production, rep. Changing it is a plan amendment, not a preference (plan §5).
PART_SECTIONS = [
    "one-line answer",
    "the idea",
    "the mechanism",
    "line by line",
    "when it breaks",
    "in production",
    "check yourself",
]
SECTION_PATTERNS = {
    "one-line answer": r"one[- ]line answer",
    "the idea": r"the idea",
    "the mechanism": r"mechanism",
    "line by line": r"line by line",
    "when it breaks": r"when it breaks",
    "in production": r"in production",
    "check yourself": r"check yourself",
}
# "Line by line" is a bolded lead-in after each code block, not a heading in a fixed place, so it
# is excluded from the order comparison; unexplained_code_blocks() enforces it per fence instead.
ORDER_EXEMPT = {"line by line"}
CONDITIONAL = {"line by line"}

# The hub's ten sections, plan §4.1. Matched by their number, so these titles are labels for the
# error messages and for `depth --list`.
HUB_SECTIONS = [
    "The scene", "The map", "Setup — run this", "Files this day prints", "Build brief",
    "The check that must be able to fail", "Request budget", "Traps", "Verified today",
    "Ledger & commit",
]
LEVELS = ["foundation", "working", "production"]
NO_WALKTHROUGH_LANGS = ["", "text", "console", "output", "traceback", "mermaid", "diff",
                        "json", "toml", "yaml", "ini", "csv"]
EXEMPT_HEADINGS = (r"when it breaks|check yourself|verified|verify|budget|ledger|the map|setup"
                   r"|files this day prints")

# A day is a unit of subject, not of time. A duration field silently authorises the worst edit in
# technical writing: cutting an explanation because the day is running long (plan §15).
TIME_BANS = [
    (r"^\s*(reading_minutes|duration|time_estimate|minutes|est_time|estimated_hours"
     r"|estimated hours|effort|pace)\s*:", "a duration field in frontmatter"),
    (r"\b\d+\s*[-–]?\s*\d*\s*(minutes?|mins?|hours?|hrs?)\b(?!\s*(of |the |per ))",
     "a time estimate in the prose"),
    (r"\*\*(Time|Duration|Estimated hours):?\*\*", "a bolded time line"),
    (r"should take (about |around |roughly )?\w+", "a 'should take ...' pace"),
]

PART_KEYS = ["project", "day", "part", "title", "spine", "level", "prints", "prev", "next"]
HUB_KEYS = ["project", "day", "title", "spine", "parts", "deploy_tier", "files_printed",
            "plan_version", "status"]

# A citation is an identifier, never a person: an identifier resolves to exactly one document and
# is what a reader types.
SOURCE_ID_RE = re.compile(
    r"arXiv:\d{4}\.\d{4,5}(?:v\d+)?"
    r"|arXiv:[a-z-]+(?:\.[A-Z]{2})?/\d{7}"
    r"|doi:10\.\d{4,9}/[^\s)\]|,;\"'`>*<]+"
    r"|RFC\s?\d{3,5}"
    r"|ISO[/ ]?(?:IEC[/ ]?)?\d{3,5}(?:-\d+)?(?::\d{4})?"
    r"|spec:[a-z0-9][a-z0-9.\-/]*", re.I)
SOURCE_ID_LOOSE_RE = re.compile(r"\b(?:arxiv|doi)\s*:\s*\S+", re.I)

PART_NAME_RE = re.compile(r"^(\d+)\.(\d+)-([a-z0-9]+(?:-[a-z0-9]+)*)\.md$")
SECTION_DIR_RE = re.compile(r"^(\d{2})-([a-z0-9]+(?:-[a-z0-9]+)*)$")
PROJECT_DIR_RE = re.compile(r"^(\d{2})-([a-z0-9]+(?:-[a-z0-9]+)*)$")
DAY_DIR_RE = re.compile(r"^day-(\d{2})-([a-z0-9]+(?:-[a-z0-9]+)*)$")
ANY_DAY_DIR_RE = re.compile(r"^day-(\d{1,3})(?:-([a-z0-9-]*))?$")


@dataclass
class Config:
    name: str = "Project"
    slug: str = "project"
    topic: str = "the subject"
    plan_version: str = "v1.0.0"
    driver: str = "python p.py"
    plan: Path = field(default_factory=lambda: ROOT / "docs" / "00_MASTER_PLAN.md")
    docs: Path = field(default_factory=lambda: ROOT / "docs")
    days: Path = field(default_factory=lambda: ROOT / "days")
    projects: Path = field(default_factory=lambda: ROOT / "projects")
    parts_dir: str = "parts"
    levels: list[str] = field(default_factory=lambda: list(LEVELS))
    part_sections: list[str] = field(default_factory=lambda: list(PART_SECTIONS))
    section_patterns: dict[str, str] = field(default_factory=lambda: dict(SECTION_PATTERNS))
    hub_sections: list[str] = field(default_factory=lambda: list(HUB_SECTIONS))
    no_walkthrough_langs: list[str] = field(default_factory=lambda: list(NO_WALKTHROUGH_LANGS))
    exempt_headings: str = EXEMPT_HEADINGS
    require_failure_part: bool = True
    require_sources: bool = True
    lint: str = ""
    format_check: str = ""
    test: str = ""

    @property
    def sources_ledger(self) -> Path:
        return self.docs / "SOURCES.md"

    @property
    def progress(self) -> Path:
        return self.docs / "PROGRESS.md"

    def rel(self, path: Path) -> str:
        try:
            return path.resolve().relative_to(ROOT).as_posix()
        except ValueError:
            return path.as_posix()


def load_config() -> Config:
    """Read granth.toml. Every key is optional; the constants above are the standing contract."""
    cfg = Config()
    path = ROOT / "granth.toml"
    if not path.exists():
        return cfg
    with path.open("rb") as handle:
        raw = tomllib.load(handle)
    p, paths = raw.get("project", {}), raw.get("paths", {})
    c, t = raw.get("contract", {}), raw.get("toolchain", {})
    for key in ("name", "slug", "topic", "plan_version", "driver"):
        setattr(cfg, key, p.get(key, getattr(cfg, key)))
    for key, default in (("plan", "docs/00_MASTER_PLAN.md"), ("docs", "docs"), ("days", "days"),
                         ("projects", "projects")):
        value = Path(paths.get(key, default))
        setattr(cfg, key, value if value.is_absolute() else ROOT / value)
    for key in ("parts_dir", "levels", "part_sections", "hub_sections", "no_walkthrough_langs",
                "exempt_headings", "require_failure_part", "require_sources"):
        setattr(cfg, key, c.get(key, getattr(cfg, key)))
    cfg.section_patterns = {**cfg.section_patterns, **c.get("section_patterns", {})}
    for key in ("lint", "format_check", "test"):
        setattr(cfg, key, t.get(key, ""))
    return cfg


# =============================================================================================
# Reading the plan
# =============================================================================================

def marked_block(text: str, marker: str) -> str:
    """Text between `<!-- granth:<marker>:start -->` and its `:end`.

    Markers rather than heading names: a heading can be reworded freely, a marker cannot be
    reworded by accident.
    """
    name = re.escape(marker)
    hit = re.search(rf"<!--\s*granth:{name}:start\s*-->(.*?)<!--\s*granth:{name}:end\s*-->",
                    text, re.S)
    return hit.group(1) if hit else ""


def _sep(cells: list[str]) -> bool:
    real = [c for c in cells if c.strip()]
    return bool(real) and all(re.fullmatch(r":?-{2,}:?", c.strip()) for c in real)


def _cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def tables(block: str) -> list[tuple[list[str], list[list[str]]]]:
    """Every Markdown table in `block`, as (header cells, data rows).

    The header is what tells two tables apart when a project may carry either an explicit day map
    or a list of inserts, so it is returned rather than skipped.
    """
    out: list[tuple[list[str], list[list[str]]]] = []
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        if not lines[i].strip().startswith("|"):
            i += 1
            continue
        header = _cells(lines[i])
        if i + 1 >= len(lines) or not _sep(_cells(lines[i + 1])):
            i += 1
            continue
        rows, i = [], i + 2
        while i < len(lines) and lines[i].strip().startswith("|"):
            cells = _cells(lines[i])
            if not _sep(cells):
                rows.append(cells)
            i += 1
        out.append((header, rows))
    return out


def table_rows(block: str) -> list[list[str]]:
    return [row for _, rows in tables(block) for row in rows]


def plain(text: str) -> str:
    """A table cell with its Markdown emphasis and its parenthetical aside removed."""
    text = re.sub(r"\*\(.*?\)\*", "", text)
    return re.sub(r"[`*_]", "", text).strip()


@dataclass
class PlanDay:
    day: int
    title: str
    spine: int | None          # the spine slot this day is, or the slot an insert follows
    insert: bool = False


@dataclass
class Project:
    number: str                # "01" — a string, because the leading zero is part of the address
    name: str
    industry: str
    days: int
    tier: str
    optional: bool = False

    @property
    def slug(self) -> str:
        return slugify(self.name)

    @property
    def dirname(self) -> str:
        return f"{self.number}-{self.slug}"

    @property
    def label(self) -> str:
        return f"P{self.number} {self.name}"


def read_plan(cfg: Config) -> str:
    if not cfg.plan.exists():
        sys.exit(f"granth: no plan at {cfg.rel(cfg.plan)}.")
    return cfg.plan.read_text(encoding="utf-8")


def plan_projects(cfg: Config) -> dict[str, Project]:
    block = marked_block(read_plan(cfg), "projects")
    if not block:
        sys.exit("granth: the plan carries no <!-- granth:projects:start --> block.\n"
                 "        Every project is checked against it — add the markers and re-run.")
    out: dict[str, Project] = {}
    for cells in table_rows(block):
        if len(cells) < 5 or not re.fullmatch(r"\d{2}", cells[0].strip()):
            continue          # a track heading row, not a project
        number = cells[0].strip()
        raw = cells[1]
        days = int(m.group(0)) if (m := re.search(r"\d+", cells[3])) else 0
        out[number] = Project(number, plain(raw), plain(cells[2]), days, plain(cells[4]),
                              optional="optional" in raw.lower())
    return out


def plan_spine(cfg: Config) -> list[tuple[int, str]]:
    block = marked_block(read_plan(cfg), "spine")
    if not block:
        sys.exit("granth: the plan carries no <!-- granth:spine:start --> block.")
    slots = []
    for cells in table_rows(block):
        if len(cells) >= 2 and re.fullmatch(r"\d{1,2}", cells[0].strip()):
            slots.append((int(cells[0]), plain(cells[1])))
    return sorted(slots)


def plan_day_maps(cfg: Config) -> dict[str, list[PlanDay]]:
    """Every project's day map, expanded from the spine plus that project's inserts.

    A project may instead carry an explicit `| Day | Title |` table, which wins — P00 does, because
    it is a primer rather than a project and does not run the spine. Expanding rather than storing
    is what stops the spine and forty copies of it from drifting apart.
    """
    block = marked_block(read_plan(cfg), "day-map")
    if not block:
        sys.exit("granth: the plan carries no <!-- granth:day-map:start --> block.")
    spine = plan_spine(cfg)
    out: dict[str, list[PlanDay]] = {}
    chunks = re.split(r"^#{2,5}\s*P(\d{2})\b", block, flags=re.M)
    for number, chunk in zip(chunks[1::2], chunks[2::2]):
        explicit: list[PlanDay] = []
        inserts: dict[int, list[str]] = {}
        for header, rows in tables(chunk):
            head = " ".join(header).lower()
            if head.startswith("day"):
                for cells in rows:
                    if len(cells) >= 2 and re.fullmatch(r"\d{1,2}", cells[0]):
                        explicit.append(PlanDay(int(cells[0]), plain(cells[1]), None))
            elif "after" in head:
                for cells in rows:
                    if len(cells) >= 2 and re.fullmatch(r"\d{1,2}", cells[0]):
                        inserts.setdefault(int(cells[0]), []).append(plain(cells[1]))
        if explicit:
            out[number] = sorted(explicit, key=lambda d: d.day)
            continue
        days, n = [], 0
        for slot, title in spine:
            days.append(PlanDay(n, title, slot))
            n += 1
            for extra in inserts.get(slot, []):
                days.append(PlanDay(n, extra, slot, insert=True))
                n += 1
        out[number] = days
    return out


def project_map(cfg: Config, number: str) -> list[PlanDay]:
    return plan_day_maps(cfg).get(number, [])


def slugify(text: str) -> str:
    """A 1-4 word kebab-case label from a plan title.

    Titles read `<subject> — <the elaboration>`, so the slug comes from the head phrase: truncating
    the whole title at four words lands mid-clause.
    """
    head = re.split(r"\s+[-–—:]\s+", plain(text).strip(), maxsplit=1)[0]
    words = re.sub(r"[^a-z0-9]+", " ", head.lower()).split()
    dropped = {"a", "an", "the", "and", "of", "to", "in", "for", "with", "on", "by", "its"}
    return "-".join(([w for w in words if w not in dropped] or words)[:4]) or "day"


# =============================================================================================
# Reading the days on disk
# =============================================================================================

def project_dirs(cfg: Config) -> dict[str, Path]:
    """Every days/<NN>-<slug>/ keyed by project number.

    A folder whose name starts with `_` is never a project: that is how `days/_TEMPLATES/` and the
    quarantined `days/_archive-v3/` stay out of every check (ADR-0007).
    """
    found: dict[str, Path] = {}
    if not cfg.days.is_dir():
        return found
    for entry in sorted(cfg.days.iterdir()):
        if entry.is_dir() and not entry.name.startswith("_"):
            if m := PROJECT_DIR_RE.match(entry.name):
                found[m.group(1)] = entry
    return found


def day_dirs(cfg: Config, number: str) -> dict[int, Path]:
    """Project `number`'s days, keyed by day number. The slug is a label, the number is identity."""
    found: dict[int, Path] = {}
    folder = project_dirs(cfg).get(number)
    if folder is None:
        return found
    for entry in sorted(folder.iterdir()):
        if entry.is_dir() and (m := ANY_DAY_DIR_RE.match(entry.name)):
            found[int(m.group(1))] = entry
    return found


def all_days(cfg: Config) -> list[tuple[str, int, Path]]:
    return [(n, d, p) for n in sorted(project_dirs(cfg))
            for d, p in sorted(day_dirs(cfg, n).items())]


def find_day(cfg: Config, number: str, day: int) -> Path | None:
    return day_dirs(cfg, number).get(day)


def part_files(folder: Path, cfg: Config) -> list[Path]:
    d = folder / cfg.parts_dir
    return sorted(d.rglob("*.md")) if d.is_dir() else []


def is_written(folder: Path, cfg: Config) -> bool:
    """A day is *written* only when it has a hub and a non-empty parts directory."""
    return (folder / "LESSON.md").exists() and bool(part_files(folder, cfg))


def frontmatter(text: str) -> dict[str, str] | None:
    """The leading `---` block as flat key to value. Not a YAML parser, and does not need to be."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    meta = {}
    for line in text[3:end].splitlines():
        if line.strip() and not line.lstrip().startswith("#"):
            key, sep, value = line.partition(":")
            if sep:
                meta[key.strip()] = _scalar(value)
    return meta


def _scalar(value: str) -> str:
    """One frontmatter value, with a trailing `# comment` removed.

    The templates ship their guidance as trailing comments — `level: foundation  # a day climbs`
    — and an author who leaves one in has not made a mistake worth failing a day for. A quoted
    value is taken whole, because a `#` inside quotes is content.
    """
    value = value.strip()
    if value[:1] in {'"', "'"}:
        end = value.find(value[0], 1)
        return value[1:end] if end != -1 else value[1:]
    return re.split(r"\s+#", value, maxsplit=1)[0].strip()


def body(text: str) -> str:
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    return text if end == -1 else text[end + 4:]


def progress_rows(cfg: Config) -> set[tuple[str, int]]:
    """(project, day) pairs with a row in the v4 ledger — the ledger is what 'complete' means.

    Only the region inside `<!-- granth:ledger:start -->` is read. The v3 table above it is kept
    verbatim as history and must never be counted (ADR-0007).
    """
    if not cfg.progress.exists():
        return set()
    block = marked_block(cfg.progress.read_text(encoding="utf-8"), "ledger")
    done = set()
    for cells in table_rows(block):
        if len(cells) >= 2 and re.fullmatch(r"\d{2}", cells[0]) and re.fullmatch(r"\d{1,2}",
                                                                                cells[1]):
            done.add((cells[0], int(cells[1])))
    return done


def project_done(cfg: Config, number: str) -> set[int]:
    return {d for n, d in progress_rows(cfg) if n == number}


# =============================================================================================
# The depth contract, checked by a machine
# =============================================================================================

@dataclass
class Report:
    project: str
    day: int
    failures: list[str] = field(default_factory=list)
    parts: int = 0

    def fail(self, where: str, message: str) -> None:
        self.failures.append(f"{where}: {message}")

    @property
    def ok(self) -> bool:
        return not self.failures


def source_ids(value: str) -> list[str]:
    return [h.group(0) for h in SOURCE_ID_RE.finditer(value or "")]


def malformed_source_ids(text: str) -> list[str]:
    """Citation-shaped strings no accepted form matches.

    Compares by start position rather than trimming punctuation: a real citation in prose is
    followed by a backtick or a bracket, and guessing what to strip is how this produces false
    failures.
    """
    valid = {h.start() for h in SOURCE_ID_RE.finditer(text)}
    return [h.group(0).strip() for h in SOURCE_ID_LOOSE_RE.finditer(text) if h.start() not in valid]


def ledger_ids(cfg: Config) -> frozenset[str]:
    if not cfg.sources_ledger.exists():
        return frozenset()
    text = cfg.sources_ledger.read_text(encoding="utf-8")
    return frozenset(m.group(0).lower() for m in SOURCE_ID_RE.finditer(text))


def _fences(cfg: Config, text: str):
    """Yield (start, lang, heading, end) per fence.

    A fence may be longer than three backticks so it can contain a shorter one — which is how a
    lesson shows the contents of a Markdown file.
    """
    lines, heading, i = text.splitlines(), "", 0
    while i < len(lines):
        if lines[i].startswith("#"):
            heading, i = lines[i], i + 1
            continue
        fence = re.match(r"^(`{3,})([\w+-]*)\s*$", lines[i])
        if not fence:
            i += 1
            continue
        closing = re.compile(rf"^`{{{len(fence.group(1))},}}\s*$")
        start, i = i, i + 1
        while i < len(lines) and not closing.match(lines[i]):
            i += 1
        i += 1
        yield start, fence.group(2).lower(), heading, i


def _needs_walkthrough(cfg: Config, lang: str, heading: str) -> bool:
    return lang not in cfg.no_walkthrough_langs and not re.search(
        cfg.exempt_headings, heading, re.I)


def unexplained_code_blocks(cfg: Config, text: str) -> list[int]:
    """Fences no walkthrough follows.

    An unexplained line is a bug in the document: the reader can copy it but cannot change it. v4
    made this stricter by deleting recap depth — every block gets the full walkthrough (plan §5.2).
    """
    lines, out = text.splitlines(), []
    for start, lang, heading, after in _fences(cfg, text):
        if not _needs_walkthrough(cfg, lang, heading):
            continue
        j, explained = after, False
        while j < len(lines):
            if re.search(r"line by line", lines[j], re.I):
                explained = True
                break
            if re.match(r"^`{3,}[\w+-]", lines[j]) or lines[j].startswith("## "):
                break
            j += 1
        if not explained:
            out.append(start + 1)
    return out


def has_explainable_code(cfg: Config, text: str) -> bool:
    return any(_needs_walkthrough(cfg, lg, h) for _, lg, h, _ in _fences(cfg, text))


def visible(text: str) -> str:
    """The document with its HTML comments removed.

    A comment is authoring scaffolding: the templates carry their instructions in comments, and
    the reader never sees one. So the content checks run on what the reader gets. The cost is
    that a violation hidden inside a comment is not caught — which is acceptable precisely
    because a comment cannot mislead a reader who cannot see it.
    """
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)


def check_no_clocks(cfg: Config, text: str, where: str, report: Report) -> None:
    prose = re.sub(r"^```.*?^```", "", visible(text), flags=re.S | re.M)
    for pattern, description in TIME_BANS:
        hit = re.search(pattern, prose, re.I | re.M)
        if hit:
            snippet = hit.group(0).strip().replace("\n", " ")
            report.fail(where, f"{description} ({snippet!r}) — a day carries no clock")


# --- plan §6: nothing leaves the project -----------------------------------------------------
#
# Without a mechanical check this rule is a preference, and preferences drift by project six.
# That sentence is ADR-0006's, and this function is what makes it true.

ESCAPE_PHRASES = [
    (r"\brecap depth\b", "'recap depth' — v4 has one depth and it is full (plan §5.2)"),
    (r"\btaught deeply (?:elsewhere|in)\b", "'taught deeply elsewhere' — it is taught here"),
    (r"\bdeep(?:er)? version\b", "'deep version' — there is no deeper version outside this project"),
    (r"\bas we saw\b", "'as we saw' — a part is readable cold (plan §5.3)"),
    (r"\bas taught in\b", "'as taught in' — a pointer out of the project"),
    (r"\bPRIMER\.md\b", "PRIMER.md — deleted in v4 (ADR-0006)"),
    (r"\bborrowed concepts?\b", "'borrowed concept' — nothing is borrowed in v4"),
]


def check_no_escape(cfg: Config, text: str, number: str, where: str, report: Report) -> None:
    """Fail on any reference that leaves this project (plan §6)."""
    prose = visible(text)
    for pattern, message in ESCAPE_PHRASES:
        if hit := re.search(pattern, prose, re.I):
            report.fail(where, f"{hit.group(0)!r} leaves the project: {message}")
    for hit in re.finditer(r"(?:projects|days)/(\d{2})-[a-z0-9-]+", prose):
        if hit.group(1) != number:
            report.fail(where, f"{hit.group(0)!r} points into another project (plan §6)")
    for hit in re.finditer(r"\bP(\d{2})\b", prose):
        if hit.group(1) != number:
            report.fail(where, f"{hit.group(0)!r} names another project (plan §6)")


# --- plan §0 rule 1: the Completeness Rule, made mechanical ----------------------------------
#
# "No `...` and no 'the rest is unchanged'." Without a check this is a rule people keep by hand,
# and a rebuild of P01 from its own documents in 2026-09 found 22 places where it had not been:
# a bare `...` standing for an unchanged region inside a marked diff, which is a diff a learner
# cannot apply. See docs/PROGRESS.md for that pass.

#: A fenced block that is really a marked diff, whatever it is tagged. `+` at column zero is not
#: valid Python, TOML or JSON, so it is the reliable tell.
FENCED = re.compile(r"^```([a-zA-Z0-9]*)\n(.*?)^```", re.M | re.S)

#: Fence languages that are output rather than source, where an ellipsis is an honest abbreviation
#: of repeated lines and a `+` is just a character.
NOT_SOURCE = {"bash", "text", "console"}


def check_completeness(cfg: Config, content: str, where: str, report: Report) -> None:
    """No unmarked elision inside a marked diff, and no diff tagged as source (plan §0 rule 1).

    A `...` on a context line of a diff means "an unchanged region sits here", which is exactly
    what `@@` says in unified-diff syntax — and unlike `...` it is a thing a reader can act on and
    a tool can apply. A diff tagged ```python is worse: a learner copying that block gets a file
    with `-` and `+` down the left margin.
    """
    for hit in FENCED.finditer(content):
        language, block = hit.group(1), hit.group(2)
        if language in NOT_SOURCE:
            continue
        lines = block.split("\n")
        added = [line for line in lines if line.startswith("+")]
        if language != "diff" and not added:
            continue
        if language != "diff":
            line_number = content[: hit.start()].count("\n") + 1
            report.fail(
                where,
                f"code block at line {line_number} is a marked diff tagged ```{language or 'none'}"
                " — tag it ```diff, or a reader copies the markers into the file",
            )
        for offset, line in enumerate(lines):
            if line.strip() == "..." and not line.startswith(("+", "-")):
                line_number = content[: hit.start()].count("\n") + 1 + offset
                report.fail(
                    where,
                    f"line {line_number}: a bare '...' stands for an unchanged region inside a "
                    "diff — use '@@ ... @@' and say what is unchanged (plan §0 rule 1)",
                )


def section_regex(cfg: Config, name: str) -> re.Pattern[str]:
    pattern = cfg.section_patterns.get(name, re.escape(name))
    if name == "line by line":
        return re.compile(rf"^#{{2,4}}\s.*{pattern}|^\*\*Line by line:?\*\*", re.I | re.M)
    return re.compile(rf"^#{{2,4}}\s.*{pattern}", re.I | re.M)


def check_sections(cfg: Config, content: str, where: str, report: Report) -> None:
    """Required sections present, unconditional ones in the contract's order."""
    triggers = {"line by line": has_explainable_code(cfg, content)}
    positions: list[tuple[int, str]] = []
    for name in cfg.part_sections:
        hit = section_regex(cfg, name).search(content)
        if hit is None:
            if triggers.get(name, True):
                report.fail(where, f"missing section '{name}'")
            continue
        if name not in ORDER_EXEMPT:
            positions.append((hit.start(), name))
    found = {n for _, n in positions}
    ordered = [n for _, n in sorted(positions)]
    expected = [n for n in cfg.part_sections if n in found]
    if ordered != expected:
        report.fail(where, "sections are out of order — the sequence is the pedagogy. "
                           f"found {ordered}, expected {expected}")
    for token in malformed_source_ids(content):
        report.fail(where, f"{token!r} is citation-shaped but matches no accepted identifier form")


def check_citations(cfg: Config, meta: dict[str, str], where: str, report: Report) -> None:
    if not cfg.require_sources:
        return
    known = ledger_ids(cfg)
    for i in source_ids(meta.get("cites", "")) + source_ids(meta.get("sources", "")):
        if i.lower() not in known:
            report.fail(where, f"{i} is not in {cfg.rel(cfg.sources_ledger)} — look the record up "
                               "live and add a dated row before citing it")


@dataclass
class PartResult:
    section: int
    subtopic: int
    declares_failure: bool = False


def check_part(cfg: Config, path: Path, number: str, day: int, report: Report) -> PartResult | None:
    where = cfg.rel(path)
    name = PART_NAME_RE.match(path.name)
    if not name:
        report.fail(where, "filename must be <section>.<subtopic>-<kebab-slug>.md")
        return None
    section, subtopic = int(name.group(1)), int(name.group(2))
    folder = SECTION_DIR_RE.match(path.parent.name)
    if not folder:
        report.fail(cfg.rel(path.parent),
                    "a section folder is NN-<kebab-slug> — a bare number is an address, "
                    "not an answer")
    elif int(folder.group(1)) != section:
        report.fail(where, f"sits in {path.parent.name} but its number says section {section}")

    text = path.read_text(encoding="utf-8")
    meta = frontmatter(text)
    if meta is None:
        report.fail(where, "no YAML frontmatter")
        return PartResult(section, subtopic)
    for key in PART_KEYS:
        if key not in meta:
            report.fail(where, f"frontmatter is missing '{key}'")
    if meta.get("level") and meta["level"] not in cfg.levels:
        report.fail(where, f"level {meta['level']!r} is not one of {cfg.levels}")
    if meta.get("day") and meta["day"].strip() != str(day):
        report.fail(where, f"frontmatter says day {meta['day']} but it sits in day {day}")
    if meta.get("project") and meta["project"].strip().lstrip("P") != number:
        report.fail(where, f"frontmatter says project {meta['project']} but it sits in {number}")

    content = body(text)
    check_sections(cfg, content, where, report)
    check_citations(cfg, meta, where, report)
    check_no_clocks(cfg, text, where, report)
    check_no_escape(cfg, text, number, where, report)
    check_completeness(cfg, content, where, report)
    for line in unexplained_code_blocks(cfg, content):
        report.fail(where, f"code block at line {line} has no 'Line by line' walkthrough after it")
    return PartResult(section, subtopic,
                      meta.get("failure", "").strip().lower() in {"true", "yes"})


def check_hub(cfg: Config, folder: Path, number: str, part_count: int, report: Report) -> None:
    hub = folder / "LESSON.md"
    where = cfg.rel(hub)
    if not hub.exists():
        report.fail(cfg.rel(folder), "no LESSON.md — the hub is what assembles the day")
        return
    text = hub.read_text(encoding="utf-8")
    meta = frontmatter(text)
    if meta is None:
        report.fail(where, "no YAML frontmatter")
        return
    for key in HUB_KEYS:
        if key not in meta:
            report.fail(where, f"frontmatter is missing '{key}'")
    if meta.get("plan_version") and meta["plan_version"] != cfg.plan_version:
        report.fail(where, f"plan_version {meta['plan_version']!r} but granth.toml says "
                           f"{cfg.plan_version!r}")
    if meta.get("parts", "").strip().isdigit() and int(meta["parts"]) != part_count:
        report.fail(where, f"frontmatter claims {meta['parts']} parts; {part_count} are on disk")

    content = body(text)
    if not re.search(r"^>\s", content, re.M):
        report.fail(where, "no yesterday / today / tomorrow blockquote")
    positions = []
    for index, title in enumerate(cfg.hub_sections, start=1):
        hit = re.search(rf"^#{{2,3}}\s*(?:§\s*)?{index}\b.*", content, re.M)
        if hit is None:
            report.fail(where, f"missing hub section {index} — {title}")
        else:
            positions.append((hit.start(), index))
    if [n for _, n in sorted(positions)] != [n for _, n in positions]:
        report.fail(where, "hub sections are out of order")
    # The hub orients and assembles; the parts teach.
    if re.search(r"\*\*Line by line:?\*\*", visible(content), re.I):
        report.fail(where, "the hub carries a 'Line by line' walkthrough — teaching belongs "
                           "in a part")
    check_no_clocks(cfg, text, where, report)
    check_no_escape(cfg, text, number, where, report)
    checklist = folder / "CHECKLIST.md"
    if not checklist.exists():
        report.fail(cfg.rel(folder), "no CHECKLIST.md — a day has no definition of done without it")
    else:
        check_no_clocks(cfg, checklist.read_text(encoding="utf-8"), cfg.rel(checklist), report)
        check_no_escape(cfg, checklist.read_text(encoding="utf-8"), number, cfg.rel(checklist),
                        report)


def check_numbering(numbers: list[tuple[int, int]], where: str, report: Report) -> None:
    """Sections run 1..N with no gaps, and so do subtopics inside each.

    A gap means a document was deleted or never written, and nothing else in the repository would
    say so — the reader would simply never learn that 2.3 was meant to exist.
    """
    if not numbers:
        return
    sections = sorted({s for s, _ in numbers})
    if sections != list(range(1, len(sections) + 1)):
        report.fail(where, f"section numbers {sections} — they must run 1..N with no gaps")
    for section in sections:
        subs = sorted(sub for sec, sub in numbers if sec == section)
        if subs != list(range(1, len(subs) + 1)):
            report.fail(where, f"section {section} subtopics {subs} — must run 1..N with no gaps")


def check_day(cfg: Config, number: str, day: int) -> Report:
    report = Report(project=number, day=day)
    folder = find_day(cfg, number, day)
    if folder is None:
        report.fail(f"P{number} day {day}", f"no folder in {cfg.rel(cfg.days)}")
        return report
    where = cfg.rel(folder)
    if not DAY_DIR_RE.match(folder.name):
        report.fail(where, "a day folder is day-NN-<kebab-slug> — a number alone is "
                           "indistinguishable from every other day in a file tree or a git log")
    parts_dir = folder / cfg.parts_dir
    if not parts_dir.is_dir():
        report.fail(where, f"no {cfg.parts_dir}/ — a day without it is not written")
        return report
    for path in sorted(parts_dir.glob("*.md")):
        report.fail(cfg.rel(path),
                    f"loose in {cfg.parts_dir}/ — every part lives in its section folder")

    numbers, failure_declared = [], False
    for path in sorted(parts_dir.rglob("*.md")):
        if path.parent == parts_dir:
            continue
        result = check_part(cfg, path, number, day, report)
        if result:
            numbers.append((result.section, result.subtopic))
            failure_declared = failure_declared or result.declares_failure
    report.parts = len(numbers)
    check_numbering(numbers, where, report)
    if report.parts == 0:
        report.fail(where, f"{cfg.parts_dir}/ holds no part documents")
    if cfg.require_failure_part and not failure_declared:
        report.fail(where, "no part declares 'failure: true' — every day carries at least one "
                           "part whose subject is a deliberate failure")
    check_hub(cfg, folder, number, report.parts, report)

    plan = {d.day: d for d in project_map(cfg, number)}
    if day not in plan:
        report.fail(where, f"the plan's map for P{number} has no day {day}")
    return report


def cmd_depth(cfg: Config, args: list[str]) -> int:
    if "--list" in args:
        print(f"granth depth contract for {cfg.name} ({cfg.plan_version})\n")
        print("A part document carries, in order:")
        for n in cfg.part_sections:
            print(f"  - {n}{' (conditional)' if n in CONDITIONAL else ''}")
        print("\nA hub carries, in order:")
        for i, t in enumerate(cfg.hub_sections, start=1):
            print(f"  {i:>2}. {t}")
        print(f"\nLevels: {', '.join(cfg.levels)}   Parts: {cfg.parts_dir}/")
        print("\nEvery code block gets the FULL walkthrough. v4 deleted recap depth (plan §5.2),")
        print("and nothing in a day document may reference another project (plan §6).")
        return 0

    positional = [a for a in args if not a.startswith("-")]
    if positional:
        number = f"{int(positional[0]):02d}"
        days = ([int(positional[1])] if len(positional) > 1
                else sorted(d for d, f in day_dirs(cfg, number).items() if is_written(f, cfg)))
        targets = [(number, d) for d in days]
    else:
        targets = [(n, d) for n, d, f in all_days(cfg) if is_written(f, cfg)]
    if not targets:
        print("granth: no written days yet — nothing to check.")
        return 0

    reports = [check_day(cfg, n, d) for n, d in targets]
    failed = 0
    for r in reports:
        head = f"P{r.project} day {r.day:>2}  {r.parts} parts"
        if r.ok:
            print(f"OK    {head}")
        else:
            failed += 1
            print(f"FAIL  {head}")
            for line in r.failures:
                print(f"        {line}")
    if failed:
        print(f"\n{failed} of {len(reports)} day(s) fail the depth contract.")
        return 1
    print(f"\nOK all {len(reports)} day(s) meet the depth contract.")
    return 0


# =============================================================================================
# The generated indexes
# =============================================================================================

BANNER = "> **Do not edit this file by hand.** It is regenerated by `{d} index`."


def truncate(text: str, width: int) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= width else text[:width - 1].rstrip() + "…"


def one_line_answer(text: str) -> str:
    """The first paragraph under the one-line-answer heading, flattened."""
    hit = re.search(r"^#{2,4}\s.*one[- ]line answer.*$", text, re.I | re.M)
    if not hit:
        return ""
    out: list[str] = []
    for line in text[hit.end():].splitlines():
        s = line.strip().lstrip("> ").strip()
        if s.startswith("#") or s.startswith("```"):
            break
        if not s:
            if out:
                break
            continue
        out.append(s)
    return re.sub(r"\s+", " ", " ".join(out))


class DayFacts:
    def __init__(self, cfg: Config, number: str, day: int, folder: Path) -> None:
        self.project, self.day, self.folder = number, day, folder
        self.written = is_written(folder, cfg)
        self.hub = frontmatter((folder / "LESSON.md").read_text(encoding="utf-8")) or {}
        self.title = self.hub.get("title", "")
        self.prints = [p.strip() for p in self.hub.get("files_printed", "").strip(
            "[]").split(",") if p.strip()]
        self.parts: list[dict[str, str]] = []
        for path in part_files(folder, cfg):
            if path.parent == folder / cfg.parts_dir:
                continue
            text = path.read_text(encoding="utf-8")
            meta = frontmatter(text) or {}
            self.parts.append({"part": meta.get("part", ""),
                               "title": meta.get("title", path.stem),
                               "level": meta.get("level", ""),
                               "answer": one_line_answer(body(text)),
                               "path": f"{cfg.parts_dir}/{path.parent.name}/{path.name}"})

    @staticmethod
    def key(part: dict[str, str]) -> tuple[float, float]:
        bits = re.findall(r"\d+", part["part"])
        return (float(bits[0]) if bits else 0.0, float(bits[1]) if len(bits) > 1 else 0.0)


def gather(cfg: Config) -> dict[tuple[str, int], DayFacts]:
    return {(n, d): DayFacts(cfg, n, d, f) for n, d, f in all_days(cfg)
            if (f / "LESSON.md").exists()}


def build_all(cfg: Config) -> dict[Path, str]:
    projects, maps = plan_projects(cfg), plan_day_maps(cfg)
    complete, facts = progress_rows(cfg), gather(cfg)
    today, d = date.today().isoformat(), cfg.driver
    head = [f"_Generated {today} by `p.py`._", BANNER.format(d=d), ""]
    total = sum(p.days for p in projects.values())

    # --- tracker ------------------------------------------------------------------------------
    written = [k for k, f in facts.items() if f.written]
    pct = lambda c: f"{(100 * c / total):.1f}%" if total else "-"  # noqa: E731
    lines = [f"# Tracker — {cfg.name}", "", *head,
             "A day is **written** with a hub and a non-empty parts directory, and **complete**",
             "only when it also has a row in the ledger. A thin day is visible from the parts",
             "column. Projects are independent, so they may be built in any order (plan §15).", "",
             "| | Count | Of plan |", "| --- | --- | --- |",
             f"| Sittings in the plan | **{total}** | 100% |",
             f"| Days written | **{len(written)}** | {pct(len(written))} |",
             f"| Days complete | **{len(complete)}** | {pct(len(complete))} |",
             f"| Subtopic documents | **{sum(len(f.parts) for f in facts.values())}** | — |", "",
             "## Every project", "",
             "| # | Project | Industry | Days | Tier | Written | Complete |",
             "| --- | --- | --- | --- | --- | --- | --- |"]
    for number, project in sorted(projects.items()):
        w = len([1 for (n, _), f in facts.items() if n == number and f.written])
        c = len([1 for n, _ in complete if n == number])
        lines.append(f"| {number} | {project.name} | {truncate(project.industry, 40)} "
                     f"| {project.days} | {project.tier} | {w}/{project.days} "
                     f"| {c}/{project.days} |")
    for number, project in sorted(projects.items()):
        if not any(n == number for n, _ in facts):
            continue
        lines += ["", f"### P{number} · {project.name}", "",
                  "| Day | Title | Status | Parts |", "| --- | --- | --- | --- |"]
        for entry in maps.get(number, []):
            f_ = facts.get((number, entry.day))
            status = ("complete" if (number, entry.day) in complete and f_ and f_.written
                      else "written" if f_ and f_.written else "hub only" if f_
                      else "not started")
            title = truncate(f_.title if f_ and f_.title else entry.title, 72)
            cell = (f"[{title}](../days/{f_.folder.relative_to(cfg.days).as_posix()}/LESSON.md)"
                    if f_ else title)
            lines.append(f"| {entry.day} | {cell} | {status} | {len(f_.parts) if f_ else 0} |")
    tracker = "\n".join(lines + [""])

    # --- wiki ---------------------------------------------------------------------------------
    lines = [f"# {cfg.name} wiki — one row per written day", "", *head,
             "For a day's parts open `wiki/PNN-day-DD.md`; open the day folder itself only to",
             "write it.", ""]
    for number, project in sorted(projects.items()):
        rows = sorted((d, f) for (n, d), f in facts.items() if n == number)
        if not rows:
            continue
        lines += [f"## P{number} · {project.name} — {project.industry}", "",
                  "| Day | Subject | Parts |", "| --- | --- | --- |"]
        lines += [f"| [{day:02d}](wiki/P{number}-day-{day:02d}.md) | {truncate(f.title, 90)} "
                  f"| {len(f.parts)} |" for day, f in rows]
        lines.append("")
    wiki = "\n".join(lines + [""])

    out = {cfg.docs / "TRACKER.md": tracker, cfg.docs / "WIKI.md": wiki}

    # --- one page per written day --------------------------------------------------------------
    for (number, day), f_ in facts.items():
        rel = f"../../days/{f_.folder.relative_to(cfg.days).as_posix()}"
        project = projects.get(number)
        lines = [f"# P{number} day {day:02d} — {f_.title}", "", *head,
                 f"Project: **{project.name if project else number}**"
                 f"{f' — {project.industry}' if project else ''}",
                 f"Hub: [`LESSON.md`]({rel}/LESSON.md)", "",
                 "| Part | Title | Level | One-line answer |", "| --- | --- | --- | --- |"]
        for p in sorted(f_.parts, key=DayFacts.key):
            lines.append(f"| {p['part']} | [{truncate(p['title'], 60)}]({rel}/{p['path']}) "
                         f"| {p['level']} | {truncate(p['answer'], 120)} |")
        if f_.prints:
            lines += ["", "## Files this day prints", "", "| Path |", "| --- |"]
            lines += [f"| `{p}` |" for p in f_.prints]
        out[cfg.docs / "wiki" / f"P{number}-day-{day:02d}.md"] = "\n".join(lines + [""])
    return out


def cmd_index(cfg: Config, args: list[str]) -> int:
    docs = build_all(cfg)
    if "--check" in args:
        stale = [cfg.rel(p) for p, t in docs.items()
                 if not p.exists() or p.read_text(encoding="utf-8") != t]
        if stale:
            print("granth: these generated documents are stale —")
            for name in stale:
                print(f"        {name}")
            print(f"        run `{cfg.driver} index`.")
            return 1
        print(f"OK {len(docs)} generated document(s) are current.")
        return 0
    (cfg.docs / "wiki").mkdir(parents=True, exist_ok=True)
    keep = {p.name for p in docs if p.parent.name == "wiki"}
    for stale in (cfg.docs / "wiki").glob("*.md"):
        if stale.name not in keep:
            stale.unlink()
    for path, text in docs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    print(f"OK wrote {len(docs)} generated document(s) under {cfg.rel(cfg.docs)}/.")
    return 0


def cmd_codemap(cfg: Config, args: list[str]) -> int:
    """A project's completeness proof: every file, and the day that printed it whole (plan §2.4).

    Prints by default and writes only with `--write`, because the authoring side never puts a file
    into `projects/` (plan §0 rule 5). `--write` is for the learner, run against the tree they
    built themselves.
    """
    number = need_project(cfg, args, "codemap")
    projects = plan_projects(cfg)
    if number not in projects:
        print(f"the plan has no project {number}.")
        return 1
    project = projects[number]
    rows: list[tuple[str, str]] = []
    for day, folder in sorted(day_dirs(cfg, number).items()):
        hub = folder / "LESSON.md"
        if not hub.exists():
            continue
        facts = DayFacts(cfg, number, day, folder)
        for printed in facts.prints:
            rows.append((printed, folder.name))
    width = max((len(p) for p, _ in rows), default=8) + 2
    lines = [f"# CODEMAP — {project.name}", "",
             f"> **Do not edit this file by hand.** Regenerate it with "
             f"`{cfg.driver} codemap {number} --write`.", "",
             "Every file in this project, and the day document that prints it **in full**.",
             "A file with no day is a Completeness Rule violation and fails the gate.", "", "```"]
    lines += [f"{path:<{width}}{day}" for path, day in sorted(rows)] or ["(nothing printed yet)"]
    lines += ["```", ""]
    text = "\n".join(lines)
    if "--write" not in args:
        print(text)
        print(f"# {len(rows)} file(s) printed across {len(day_dirs(cfg, number))} day(s). "
              f"Add --write to save this into your own project tree.")
        return 0
    target = cfg.projects / project.dirname / "CODEMAP.md"
    if not target.parent.is_dir():
        print(f"no {cfg.rel(target.parent)}/ yet — you build the project tree; the days say how.")
        return 1
    target.write_text(text, encoding="utf-8")
    print(f"OK wrote {cfg.rel(target)} — {len(rows)} file(s) printed across "
          f"{len(day_dirs(cfg, number))} day(s).")
    return 0


# =============================================================================================
# The day brief, and the order guard
# =============================================================================================

def cmd_brief(cfg: Config, args: list[str]) -> int:
    number, day = need_day(cfg, args, "brief")
    projects, maps = plan_projects(cfg), plan_day_maps(cfg)
    if number not in projects:
        print(f"**STOP.** The plan has no project {number}. It has "
              f"{', '.join(sorted(projects))}.")
        return 1
    project, entries = projects[number], {e.day: e for e in maps.get(number, [])}
    complete = project_done(cfg, number)
    out: list[str] = [f"# {cfg.name} — brief for P{number} {project.name}, day {day}", ""]
    status = 0

    if day not in entries:
        last = max(entries) if entries else 0
        print("\n".join(out + [
            f"**STOP.** P{number} has no day {day}. It runs 0 to {last}.",
            "Adding, merging or reordering a day inside a project is a plan amendment:",
            "write the ADR first (plan §15)."]))
        return 1
    entry = entries[day]

    expected = (max(complete) + 1) if complete else 0
    if day != expected:
        status = 1
        if day in complete:
            out += [f"**STOP.** P{number} day {day} already has a row in the ledger.",
                    f"The next unwritten day of this project is **{expected}**."]
        elif day < expected:
            out.append(f"**STOP.** Day {day} is behind the ledger. Next is **{expected}**.")
        else:
            missing = ", ".join(str(n) for n in range(expected, day) if n not in complete)
            out += [f"**STOP.** Day {day} is out of order — day **{expected}** is next.", "",
                    f"Not yet in the ledger: {missing}.",
                    "Order inside a project is strict; order between projects is free (plan §15).",
                    "Never skip, merge or reorder a day without an ADR."]
        out += ["", "---", ""]

    out += ["## The assignment", "", f"**Title (from the plan):** {entry.title}", "",
            f"**Project:** P{number} {project.name} — {project.industry}",
            f"**Deploy tier:** {project.tier} · **Days in this project:** 0 to "
            f"{max(entries)} ({project.days} sittings)", ""]
    if entry.insert:
        out.append(f"This is an **extra day**, placed after spine slot {entry.spine} because this "
                   "project's subject earns it (plan §13).")
    elif entry.spine is not None:
        out.append(f"This is **spine slot {entry.spine}** (plan §12). Every project builds it, "
                   "from zero, at full depth.")
    out.append("")

    out += ["## The five rules that outrank everything (plan §0)", "",
            "1. **Completeness** — every line printed in full, at its real path, in THIS project.",
            "2. **Repetition** — every concept used here is taught here, at full depth. There is",
            "   no recap depth and no pointer to another project.",
            "3. **From scratch** — nothing is assumed that this project did not build.",
            "4. **Full stack** — this project ships the whole feature set (plan §12).",
            "5. **The document is the deliverable** — every file in full at its real path, every",
            "   command in order, every real output. The learner types all of it, and you never",
            "   create, edit or scaffold anything under `projects/`.", "",
            f"Nothing in this day may reference another project. `{cfg.driver} check` greps for it.",
            ""]

    if day > 0:
        folder = find_day(cfg, number, day - 1)
        out += [f"## Where P{number} day {day - 1} left off", ""]
        if folder is None:
            out.append(f"No folder for day {day - 1} — it was never written.")
        else:
            hub = folder / "LESSON.md"
            meta = frontmatter(hub.read_text(encoding="utf-8")) if hub.exists() else None
            if meta:
                out += [f"- Hub: `{cfg.rel(hub)}`", f"- Title: {meta.get('title', '?')}",
                        f"- Status: {meta.get('status', '?')}"]
            checklist = folder / "CHECKLIST.md"
            boxes = ([ln.strip() for ln in checklist.read_text(encoding="utf-8").splitlines()
                      if ln.strip().startswith("- [ ]")] if checklist.exists() else [])
            if boxes:
                out.append(f"- **{len(boxes)} unticked checklist box(es)** — ask before moving on:")
                out += [f"    {b}" for b in boxes[:8]]
                if len(boxes) > 8:
                    out.append(f"    ... and {len(boxes) - 8} more")
            elif checklist.exists():
                out.append("- Checklist: fully ticked.")
        out.append("")

    printed = [(p, f"day {d:02d}") for (n, d), f in sorted(gather(cfg).items())
               if n == number and d < day for p in f.prints]
    if printed:
        out += [f"## Files P{number} has already printed", "",
                "Reprinting one of these is a bug unless it is a **marked diff** and this day says",
                "which day printed the original (plan §5.1 rule 2).", "",
                "| File | Printed by |", "| --- | --- |"]
        out += [f"| `{p}` | {d} |" for p, d in printed] + [""]

    out += ["## The rest of this project's map", "", "| Day | Title |", "| --- | --- |"]
    out += [f"| {e.day}{' ←' if e.day == day else ''} | {truncate(e.title, 88)} |"
            for e in maps.get(number, [])]
    out += ["", "## Before you write a line", "",
            f"1. `{cfg.rel(cfg.plan)}` §5 and §5.1 — the part contract and the six constraints",
            "   on real code. Then §4.1 for the hub, §12 for the spine slot, §13 for this project.",
            "2. §14 — the style guide, and the four constraints that stop forty projects reading",
            "   like one project pasted forty times.",
            f"3. `{cfg.rel(cfg.docs / 'GLOSSARY.md')}` — so a term is defined the same way twice.",
            "4. Verify every fact live. A version, an interface, a citation: look it up today, or",
            "   leave a TODO carrying the exact lookup command. Never a remembered answer.", ""]
    if status == 0:
        out.append(f"**P{number} day {day} is next. Go.**")
    print("\n".join(out))
    return status


# =============================================================================================
# The rest of the driver
# =============================================================================================

def need_project(cfg: Config, args: list[str], command: str) -> str:
    args = [a for a in args if not a.startswith("-")]
    if not args or not re.fullmatch(r"P?\d{1,2}", args[0], re.I):
        sys.exit(f"usage: {cfg.driver} {command} <project-number>")
    return f"{int(args[0].lstrip('Pp')):02d}"


def need_day(cfg: Config, args: list[str], command: str) -> tuple[str, int]:
    """Accepts `01 7` and `01/7` — the second is what a person types after reading a path."""
    flat = [bit for a in args for bit in str(a).split("/") if bit]
    if len(flat) < 2 or not re.fullmatch(r"P?\d{1,2}", flat[0], re.I) or not flat[1].isdigit():
        sys.exit(f"usage: {cfg.driver} {command} <project-number> <day-number>   "
                 f"(e.g. {cfg.driver} {command} 01 7)")
    return f"{int(flat[0].lstrip('Pp')):02d}", int(flat[1])


def cmd_status(cfg: Config, args: list[str]) -> int:
    projects = plan_projects(cfg)
    complete = progress_rows(cfg)
    written = [1 for _, _, f in all_days(cfg) if is_written(f, cfg)]
    total = sum(p.days for p in projects.values())
    print(f"{cfg.name} ({cfg.plan_version}): {len(complete)}/{total} sittings complete, "
          f"{len(written)} written, across {len(projects)} projects.")
    for number, project in sorted(projects.items()):
        done = project_done(cfg, number)
        if not done and number not in project_dirs(cfg):
            continue
        nxt = (max(done) + 1) if done else 0
        state = "finished" if len(done) >= project.days else f"next: day {nxt}"
        print(f"  P{number} {project.name:<32} {len(done)}/{project.days}  {state}")
    if not complete:
        first = min(projects, key=lambda n: (projects[n].optional, n))
        print(f"  nothing started. `{cfg.driver} brief {first} 0` is the first sitting.")
    return 0


def cmd_start(cfg: Config, args: list[str]) -> int:
    number, day = need_day(cfg, args, "start")
    folder = find_day(cfg, number, day)
    if folder is None:
        print(f"no P{number} day {day} on disk yet — `{cfg.driver} brief {number} {day}` says "
              "what it must cover.")
        return 1
    if not is_written(folder, cfg):
        print(f"P{number} day {day} has a folder but no parts — it is not written.")
        return 1
    print(f"-> open {cfg.rel(folder / 'LESSON.md')}   (read its map, then the parts in order)")
    for path in part_files(folder, cfg):
        print(f"     {path.relative_to(folder).as_posix()}")
    return 0


def cmd_parts(cfg: Config, args: list[str]) -> int:
    number, day = need_day(cfg, args, "parts")
    folder = find_day(cfg, number, day)
    if folder is None or not (folder / cfg.parts_dir).is_dir():
        print(f"P{number} day {day} has no {cfg.parts_dir}/ — it is not written.")
        return 1
    for path in part_files(folder, cfg):
        print(path.relative_to(folder / cfg.parts_dir).as_posix())
    return 0


def cmd_new(cfg: Config, args: list[str]) -> int:
    number, day = need_day(cfg, args, "new")
    projects, maps = plan_projects(cfg), plan_day_maps(cfg)
    if number not in projects:
        print(f"the plan has no project {number} — amend the plan first.")
        return 1
    entries = {e.day: e for e in maps.get(number, [])}
    if day not in entries:
        print(f"the plan's map for P{number} has no day {day} — amend the plan first.")
        return 1
    if find_day(cfg, number, day):
        print(f"P{number} day {day} already exists at {cfg.rel(find_day(cfg, number, day))}.")
        return 1
    templates = cfg.days / "_TEMPLATES"
    if not templates.is_dir():
        print(f"no templates at {cfg.rel(templates)} — nothing to scaffold from.")
        return 1
    rest = [a for a in args if not re.fullmatch(r"P?\d{1,2}", a, re.I)]
    slug = slugify(rest[0]) if rest else slugify(entries[day].title)
    folder = cfg.days / projects[number].dirname / f"day-{day:02d}-{slug}"
    (folder / cfg.parts_dir / "01-rename-me").mkdir(parents=True, exist_ok=True)
    (folder / "lab").mkdir(exist_ok=True)
    for name in ("LESSON.md", "CHECKLIST.md"):
        if (templates / name).exists():
            shutil.copy(templates / name, folder / name)
    if (templates / "PART.md").exists():
        shutil.copy(templates / "PART.md",
                    folder / cfg.parts_dir / "01-rename-me" / "1.1-rename-me.md")
    print(f"-> {cfg.rel(folder)}")
    print(f"   the plan assigns: {entries[day].title}")
    print("   rename the section folder and the part file to say what they teach, then write.")
    return 0


def cmd_check(cfg: Config, args: list[str]) -> int:
    for command, label in ((cfg.lint, "lint"), (cfg.format_check, "format"), (cfg.test, "tests")):
        if command:
            print(f"--- {label}: {command}", flush=True)
            if subprocess.call(command, shell=True, cwd=ROOT) != 0:
                print(f"FAIL {label}")
                return 1
    print("--- plan and project folders", flush=True)
    if cmd_doctor(cfg, []) != 0:
        return 1
    print("--- depth contract", flush=True)
    if cmd_depth(cfg, []) != 0:
        return 1
    print("--- generated documents", flush=True)
    if cmd_index(cfg, ["--check"]) != 0:
        return 1
    print("\nOK all green")
    return 0


def cmd_verify(cfg: Config, args: list[str]) -> int:
    """Independence, proved rather than claimed (plan §7).

    Copies ONLY this project's folder to a directory outside the repository and runs its own
    check there. It is not a container: it shares this machine's interpreter and its network, and
    it says so rather than implying an isolation it does not provide.
    """
    number = need_project(cfg, args, "verify")
    projects = plan_projects(cfg)
    if number not in projects:
        print(f"the plan has no project {number}.")
        return 1
    project = projects[number]
    source = cfg.projects / project.dirname
    if not source.is_dir():
        print(f"no {cfg.rel(source)}/ — the project tree does not exist yet.")
        return 1

    problems: list[str] = []
    for path in sorted(source.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in {
                ".py", ".md", ".toml", ".yaml", ".yml", ".txt", ".cfg", ".sh"}:
            continue
        if any(part in {".venv", "__pycache__", "node_modules"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        report = Report(project=number, day=-1)
        check_no_escape(cfg, text, number, cfg.rel(path), report)
        problems += report.failures

    with tempfile.TemporaryDirectory(prefix=f"verify-{project.dirname}-") as tmp:
        target = Path(tmp) / project.dirname
        shutil.copytree(source, target,
                        ignore=shutil.ignore_patterns(".venv", "__pycache__", "*.pyc"))
        runner = next((target / n for n in ("run", "run.py") if (target / n).exists()), None)
        print(f"--- copied {cfg.rel(source)} to a directory outside the repository")
        if problems:
            print("FAIL references that leave the project:")
            for line in problems:
                print(f"      {line}")
            return 1
        if runner is None:
            print("FAIL no ./run or run.py in the copy — a project drives itself (plan §7).")
            return 1
        cmd = ([sys.executable, str(runner), "check"] if runner.suffix == ".py"
               else [str(runner), "check"])
        print(f"--- {' '.join(cmd[-2:])} inside the copy", flush=True)
        code = subprocess.call(cmd, cwd=target)
    if code != 0:
        print(f"FAIL P{number} does not pass its own check in isolation.")
        return 1
    print(f"OK P{number} {project.name} builds and checks with nothing but its own folder.")
    print("   Note: this shares the host interpreter and network. It is isolation, not a container.")
    return 0


def cmd_done(cfg: Config, args: list[str]) -> int:
    number, day = need_day(cfg, args, "done")
    folder = find_day(cfg, number, day)
    if folder is None:
        print(f"no folder for P{number} day {day}.")
        return 1
    checklist = folder / "CHECKLIST.md"
    if not checklist.exists():
        print(f"FAIL no {cfg.rel(checklist)} — a day has no definition of done without it.")
        return 1
    boxes = [ln for ln in checklist.read_text(encoding="utf-8").splitlines()
             if ln.strip().startswith("- [ ]")]
    if boxes:
        print(f"FAIL {len(boxes)} unticked box(es) in {cfg.rel(checklist)}:")
        for line in boxes:
            print(f"      {line.strip()}")
        return 1
    if (number, day) not in progress_rows(cfg):
        print(f"FAIL P{number} day {day} has no row in the v4 ledger of "
              f"{cfg.rel(cfg.progress)}.")
        print("      Paste the row from the hub's ledger section first — the ledger is the record,")
        print("      and a commit is not one.")
        return 1
    # Regenerate BEFORE checking: the ledger row this command just insisted on is itself an input
    # to the indexes, so checking first would fail on a staleness the day created.
    if cmd_index(cfg, []) != 0 or cmd_check(cfg, []) != 0:
        return 1
    meta = frontmatter((folder / "LESSON.md").read_text(encoding="utf-8")) or {}
    message = f"P{number} day {day:02d}: {meta.get('title', folder.name)}"
    if subprocess.call(["git", "add", "-A"], cwd=ROOT) != 0:
        return 1
    if subprocess.call(["git", "commit", "-m", message], cwd=ROOT) != 0:
        return 1
    print(f"OK P{number} day {day} committed.")
    return 0


def cmd_doctor(cfg: Config, args: list[str]) -> int:
    """The repository's own wiring, checked before blaming a day for a tool's failure."""
    problems = []
    if not (ROOT / "granth.toml").exists():
        problems.append("no granth.toml at the repository root")
    if not cfg.plan.exists():
        problems.append(f"no plan at {cfg.rel(cfg.plan)}")
    else:
        text = cfg.plan.read_text(encoding="utf-8")
        problems += [f"the plan has no <!-- granth:{m}:start --> block"
                     for m in ("projects", "spine", "day-map") if not marked_block(text, m)]
    problems += [f"no {cfg.rel(cfg.docs / n)}" for n in
                 ("PROGRESS.md", "CHANGELOG_PLAN.md", "GLOSSARY.md", "SOURCES.md")
                 if not (cfg.docs / n).exists()]
    if (cfg.progress.exists()
            and not marked_block(cfg.progress.read_text(encoding="utf-8"), "ledger")):
        problems.append(f"{cfg.rel(cfg.progress)} has no <!-- granth:ledger:start --> block — "
                        "the v4 ledger is the only region read (ADR-0007)")
    if not (cfg.docs / "adr").is_dir():
        problems.append(f"no {cfg.rel(cfg.docs / 'adr')}/")
    if not cfg.days.is_dir():
        problems.append(f"no {cfg.rel(cfg.days)}/")
    if not (ROOT / ".gitignore").exists():
        problems.append("no .gitignore — secrets discipline starts with the file that enforces it")

    projects = plan_projects(cfg) if cfg.plan.exists() else {}
    maps = plan_day_maps(cfg) if projects else {}
    spine = plan_spine(cfg) if projects else []
    for number, project in sorted(projects.items()):
        entries = maps.get(number, [])
        if not entries:
            problems.append(f"P{number} has no day map in the plan's day-map block")
            continue
        if len(entries) != project.days:
            problems.append(f"P{number} says {project.days} days in §11 but its map expands to "
                            f"{len(entries)} — fix the inserts table or the Days column")
        if [e.day for e in entries] != list(range(len(entries))):
            problems.append(f"P{number}'s day numbers are not 0..{len(entries) - 1}")
    for number, folder in sorted(project_dirs(cfg).items()):
        if number not in projects:
            problems.append(f"{cfg.rel(folder)} is not a project in the plan")
        elif folder.name != projects[number].dirname:
            problems.append(f"{cfg.rel(folder)} should be named "
                            f"{projects[number].dirname} after the plan's project name")

    if problems:
        print("granth doctor found:")
        for line in problems:
            print(f"  - {line}")
        return 1
    total = sum(p.days for p in projects.values())
    print(f"OK {cfg.name}: config, plan markers, ledger and every project map check out.")
    print(f"   {len(projects)} projects, {len(spine)} spine slots, {total} sittings planned.")
    return 0


COMMANDS = {"status": cmd_status, "brief": cmd_brief, "start": cmd_start, "parts": cmd_parts,
            "new": cmd_new, "depth": cmd_depth, "codemap": cmd_codemap, "index": cmd_index,
            "check": cmd_check, "verify": cmd_verify, "done": cmd_done, "doctor": cmd_doctor}

USAGE = """usage: {d} <command> [args]

A day is addressed by its project and its day: `{d} brief 01 7` is day 7 of project 01.

  status              every project: how many days written, how many complete, what is next
  brief NN D          what day D of project NN must cover, and whether it is allowed yet
  start NN D          point at that day's hub and list its documents in reading order
  parts NN D          list that day's subtopic documents
  new NN D [slug]     scaffold an empty day folder from days/_TEMPLATES/
  depth NN [D]        check one day, one project, or (with no argument) every written day
  depth --list        print the contract as configured
  codemap NN          print that project's CODEMAP.md from its day hubs (--write saves it)
  index [--check]     regenerate the derived documents in docs/ (or fail if stale)
  check               doctor + depth contract + generated documents
  verify NN           copy that project alone outside the repository and run its own check
  done NN D           refuse unless the checklist is ticked and the ledger row exists, then commit
  doctor              this repository's wiring: config, plan markers, ledger, project maps
"""


def main(argv: list[str]) -> int:
    cfg = load_config()
    command = argv[0] if argv else "help"
    handler = COMMANDS.get(command)
    if handler is None:
        print(USAGE.format(d=cfg.driver))
        return 0 if command in {"help", "-h", "--help"} else 2
    return handler(cfg, argv[1:])


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
