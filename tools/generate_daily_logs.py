#!/usr/bin/env python3
"""Generate the 42 daily-log entries for the TOEFL ITP preparation repo.

Run from anywhere:
    python tools/generate_daily_logs.py

It only writes files that don't already exist, so re-running it after you've
filled in your own entries will never overwrite your work. Pass --force to
regenerate everything from scratch.
"""

from __future__ import annotations

import datetime as dt
import os
import sys

START = dt.date(2026, 10, 5)   # Day 1  - Monday
DAYS = 42                       # Day 42 - Sunday 15 Nov 2026
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "daily-log")

M = "../materials/"
P = "../practice/"

# (week, day_in_week, objective, material_md, drill_md, budget_minutes)
SCHEDULE = [
    (0, 1, "Diagnostic — establish an honest baseline",
     f"{M}reference/score-conversion.md", f"{P}diagnostic/diagnostic-test.md", 90),
    (0, 2, "S01 — subject-verb agreement & word order",
     f"{M}structure/s01-subject-verb-agreement.md",
     "S01 exercises (20) + Structure Test 01 Q1-15", 100),
    (0, 3, "S02 — verb tenses & time markers",
     f"{M}structure/s02-verb-tenses.md",
     "S02 exercises (20) + Structure Test 01 Q16-30", 100),
    (0, 4, "Mixed drill — S01 + S02 under exam timing",
     f"{M}structure/s01-subject-verb-agreement.md",
     f"{P}section-tests/structure-test-01.md (Q1-30, 18 min)", 90),
    (0, 5, "S03 — participles, gerunds, infinitives",
     f"{M}structure/s03-participles-gerunds-infinitives.md",
     "S03 exercises (20) + Structure Test 01 Q31-40", 100),
    (0, 6, "Listening orientation + idiom bank set 1",
     f"{M}listening/l01-part-a-strategy.md + {M}listening/l02-idiom-bank.md (1-40)",
     "ETS official Level 1 listening samples", 100),
    (0, 7, "Weekly review — consolidate, then stop",
     "../progress/error-log.md", "Recall test from blank page", 60),

    (1, 8, "S04 — noun clauses & reported speech",
     f"{M}structure/s04-noun-clauses.md", "S04 exercises (20) + mixed S01-S04 timed (25/15min)", 100),
    (1, 9, "S05 — adjective clauses & reductions",
     f"{M}structure/s05-adjective-clauses.md", "S05 exercises (20) + 10 reductions", 100),
    (1, 10, "S06 — adverb clauses, conjunctions, conditionals",
     f"{M}structure/s06-adverb-clauses-conditionals.md", "S06 exercises (20) + mixed timed", 100),
    (1, 11, "S07 — inversion, comparatives, parallelism",
     f"{M}structure/s07-inversion-comparatives-parallelism.md", "S07 exercises (20) + mixed timed", 100),
    (1, 12, "S08 — word forms, articles, prepositions, pronouns",
     f"{M}structure/s08-word-forms-articles-prepositions.md + {M}vocabulary/word-families.md",
     "S08 exercises (25) + mixed timed", 110),
    (1, 13, "Structure Test 01 — full 40 questions / 25 min",
     f"{P}section-tests/structure-test-01.md", "Full section, then per-module analysis", 120),
    (1, 14, "Consolidation & rest",
     "../progress/error-log.md", "Retest every D13 miss", 60),

    (2, 15, "R01 — the 8 reading question types",
     f"{M}reading/r01-question-types.md", "Type-identification drill + 1 passage (11 min)", 100),
    (2, 16, "R02 — vocabulary in context + word attack",
     f"{M}reading/r02-vocabulary-in-context.md + {M}vocabulary/academic-word-list.md (1-40)",
     "2 passages, 12 questions (13 min)", 100),
    (2, 17, "Practice passages 1 & 2",
     f"{M}reading/r03-practice-passages.md", "Passages 1 & 2, 10 questions each (11 min each)", 100),
    (2, 18, "The two hard types — inference & NOT/EXCEPT",
     f"{M}reading/r01-question-types.md (§ 4, § 5)", "15 inference + NOT/EXCEPT items", 100),
    (2, 19, "Reading Test 01 — 25 questions",
     f"{P}section-tests/reading-test-01.md", "25 questions / 28 min + per-type table", 100),
    (2, 20, "Structure maintenance + vocabulary sets 3-4",
     f"{M}vocabulary/academic-word-list.md (41-80)", "Retest all Week-01 misses + mixed drill", 100),
    (2, 21, "Review & preview — set up audio for Week 03",
     "../progress/error-log.md", "Speed check: 1 passage / 10 questions / 9 min", 70),

    (3, 22, "L01 — Part A strategy (30 short dialogues)",
     f"{M}listening/l01-part-a-strategy.md", "ETS Part A samples — one pass only", 100),
    (3, 23, "L02 — idiom bank sets 2 & 3",
     f"{M}listening/l02-idiom-bank.md (41-120)", "20 Part A items, single pass + shadowing", 100),
    (3, 24, "L03 — Parts B & C, note-taking",
     f"{M}listening/l03-parts-b-c-note-taking.md",
     f"2 lectures from {M}listening/l04-audio-script-bank.md", 100),
    (3, 25, "Listening Test 01",
     f"{P}section-tests/listening-test-01.md", "20 questions, script audio, single pass", 90),
    (3, 26, "Official ETS samples + mixed timed set",
     "https://www.ets.org/toefl/itp/prepare.html",
     "10 L + 15 S + 10 R in 30 min continuous", 100),
    (3, 27, "MOCK EXAM #1 — full 115 minutes",
     f"{P}mock-exam-protocol.md", "L 35 / S 25 / R 55 — straight through", 180),
    (3, 28, "Mock analysis + recovery",
     "../progress/error-log.md", "Build the Week 04 retarget list", 90),

    (4, 29, "Retarget — weaknesses #1 and #2",
     "../progress/error-log.md", "2 x 25 targeted items, timed", 100),
    (4, 30, "Reading under pressure — double set",
     f"{P}section-tests/reading-test-01.md", "25 Q in 26 min, then passages 3-4 in 20 min", 100),
    (4, 31, "Listening double set + structure sprint",
     f"{M}listening/l04-audio-script-bank.md",
     "20 listening items + 40 structure in 22 min", 100),
    (4, 32, "MOCK EXAM #2 — full 115 minutes",
     f"{P}mock-exam-protocol.md", "L 35 / S 25 / R 55 — straight through", 180),
    (4, 33, "Final error sweep",
     "../progress/error-log.md", "Top-5 patterns drill + whittle flashcards to 50", 100),
    (4, 34, "Half-mock + mental rehearsal + logistics",
     f"{M}reference/test-day-playbook.md",
     "Structure 40 (25 min) + Reading 25 (28 min) back to back", 90),
    (4, 35, "REST — 30 minutes maximum",
     f"{M}reference/test-day-playbook.md", "30 flashcards only. Then stop.", 30),

    (5, 36, "Light structure review — no new material",
     f"{M}structure/s01-subject-verb-agreement.md", "20 easy mixed items, untimed", 60),
    (5, 37, "Light reading + vocabulary",
     f"{M}vocabulary/academic-word-list.md", "1 passage untimed + final flashcard pass", 60),
    (5, 38, "Light listening + pack the bag",
     f"{M}listening/l04-audio-script-bank.md",
     "1 easy lecture + confirm ID, pencils, watch, route", 45),
    (5, 39, "Rehearsal only — 30 minutes",
     f"{M}reference/test-day-playbook.md", "Read the playbook once. Read the top-5 card.", 30),
    (5, 40, "OFF — do nothing",
     "—", "Sleep 8 hours.", 0),
    (5, 41, "EXAM DAY",
     f"{M}reference/test-day-playbook.md", "L 35 / S 25 / R 55", 0),
    (5, 42, "Retro — record the result",
     "../progress/score-tracker.md", "Write what worked and what didn't", 30),
]

def linkify(spec: str) -> str:
    """Turn '../materials/structure/s01-foo.md (1-40)' into a tidy markdown link."""
    import re
    m = re.match(r"^(\S+)\s*(\(.*\))?$", spec.strip())
    if not m:
        return spec.strip()
    path, note = m.group(1), (m.group(2) or "")
    if not path.startswith(("..", "http")):
        return spec.strip()
    label = path.rsplit("/", 1)[-1].removesuffix(".md")
    return f"[{label}]({path}) {note}".strip()


SPECIAL = {
    41: "**EXAM DAY.** Nothing new today. Read the playbook, then go and do it.",
    40: "**Day off.** Fill in one line and close the file. Rest is part of the work.",
    35: "**Rest day.** Twenty minutes of flashcards, then stop. Consolidation is the work today.",
    42: "**Retro day.** Record the official score, then write honestly what you'd change.",
}


def blocks(budget: int) -> str:
    """Time-block table, scaled to the day's budget."""
    if budget == 0:
        return "| Block | Planned | Actual | Notes |\n|---|---:|---:|---|\n| (no session) | 0 | | |"
    if budget <= 35:
        rows = [("Light review", round(budget * 0.6)), ("Flashcards", round(budget * 0.4))]
    elif budget <= 70:
        rows = [("Error sweep", round(budget * 0.35)), ("Retest misses", round(budget * 0.35)),
                ("Preview / update", round(budget * 0.2)), ("Commit", 5)]
    elif budget >= 150:
        rows = [("Setup", 15), ("Listening 50 Q", 35), ("Structure 40 Q", 25),
                ("Reading 50 Q", 55), ("Mark + convert", 20), ("Analysis", 25), ("Commit", 5)]
    else:
        rows = [("Warm-up", 5), ("Instruction", 25), ("Guided practice", 20),
                ("Timed drill", 25), ("Error review", 20), ("Commit", 5)]
    total = sum(r[1] for r in rows)
    out = ["| Block | Planned | Actual | Notes |", "|---|---:|---:|---|"]
    for name, mins in rows:
        out.append(f"| {name} | {mins} | | |")
    out.append(f"| **Total** | **{total}** | | |")
    return "\n".join(out)


def build(day: int, date: dt.date, week: int, diw: int, objective: str,
          material: str, drill: str, budget: int) -> str:
    fname = date.strftime("%Y-%m-%d")
    pretty = date.strftime("%a, %d %b %Y")
    week_file = f"week-{week:02d}"
    note = SPECIAL.get(day, "")
    note_line = f"\n> {note}\n" if note else ""

    drill_md = f"[{drill}]({drill})" if drill.startswith(("..", "http")) else drill
    material_md = "\n".join(f"- {linkify(p)}" for p in material.split(" + "))

    return f"""# Day {day:02d} — {pretty}

**Week {week:02d} · Day {diw}** · [Week plan](../curriculum/{week_file}.md#d{diw}) · [Curriculum](../curriculum/README.md)
· [Score tracker](../progress/score-tracker.md) · [Error log](../progress/error-log.md)
{note_line}
---

## Plan

**Objective:** {objective}

**Material:**
{material_md}

**Drill:** {drill_md}

**Budget:** {budget} min

---

## Actual

{blocks(budget)}

---

## Done

- [ ] Warm-up done
- [ ] Material read
- [ ] Drill completed
- [ ] Errors logged
- [ ] Committed

---

## Score

| Item | Score | Target | Met? |
|---|---:|---:|---|
| | | | |

---

## Errors today

| Src | Category | Why | Fix |
|---|---|---|---|
| | | | |

---

## Reflection

1. **What went well:**
2. **What didn't:**
3. **Tomorrow's first move:**

---

**Commit message:** `day {day:02d}: `

---

[← previous]({fname_prev(day)}) · [next →]({fname_next(day)})
"""


def _shift(day: int, delta: int) -> dt.date:
    return START + dt.timedelta(days=day - 1 + delta)


def fname_prev(day: int) -> str:
    return "TEMPLATE.md" if day == 1 else _shift(day, -1).strftime("%Y-%m-%d.md")


def fname_next(day: int) -> str:
    return "README.md" if day == DAYS else _shift(day, 1).strftime("%Y-%m-%d.md")


def main() -> int:
    force = "--force" in sys.argv
    out = os.path.abspath(OUT_DIR)
    os.makedirs(out, exist_ok=True)
    written = skipped = 0

    for idx, (week, diw, objective, material, drill, budget) in enumerate(SCHEDULE, start=1):
        date = START + dt.timedelta(days=idx - 1)
        path = os.path.join(out, date.strftime("%Y-%m-%d.md"))
        if os.path.exists(path) and not force:
            skipped += 1
            continue
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(build(idx, date, week, diw, objective, material, drill, budget))
        written += 1

    print(f"daily-log: {written} written, {skipped} skipped (already exist)")
    print(f"range: {START.isoformat()} -> {(START + dt.timedelta(days=DAYS - 1)).isoformat()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
