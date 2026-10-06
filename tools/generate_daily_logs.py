#!/usr/bin/env python3
"""Generate the BMW-lab style daily logs for the TOEFL ITP preparation repo.

Layout produced:

    docs/logs/daily/week-NN/DD-MM-YYYY.md    42 entries, 5 Oct -> 15 Nov 2026
    docs/logs/daily/README.md                index of every entry by week
    docs/logs/daily/TEMPLATE.md              blank entry

Run from anywhere:

    python tools/generate_daily_logs.py

Files that already exist are never overwritten unless you pass --force, so it is
safe to re-run after you have filled in your own entries.
"""

from __future__ import annotations

import datetime as dt
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
DAILY = os.path.join(ROOT, "docs", "logs", "daily")

START = dt.date(2026, 10, 5)      # Day 1  - Monday
DAYS = 42                          # Day 42 - Sunday 15 Nov 2026

DOCS = "docs"
SN = "docs/study-notes"
HO = "docs/hands-on"

# (week, day_in_week, objective, material, drill, budget_minutes, evidence)
SCHEDULE = [
    (0, 1, "Establish an honest baseline before studying anything",
     "reference/Score Conversion.md",
     f"{HO}/[05-Oct] Diagnostic Test.md", 90,
     "three section numbers in the score tracker; five error-log rows"),
    (0, 2, "Learn to find the real subject in a sentence full of decoys",
     "[06-Oct] S01 - Subject-Verb Agreement.md",
     "S01 exercises (20) + Structure Test 01 Q1-15", 100,
     "five decoy patterns written on a card; per-item accuracy"),
    (0, 3, "Choose tense from the time marker, never from intuition",
     "[07-Oct] S02 - Verb Tenses and Time Markers.md",
     "S02 exercises (20) + Structure Test 01 Q16-30", 100,
     "marker to tense table; every miss tagged with its marker"),
    (0, 4, "Combine S01 and S02 under exam timing",
     "[06-Oct] S01 - Subject-Verb Agreement.md",
     "Structure Test 01, Q1-30 in 18 min", 90,
     "timed answer grid, 30 items in 18 minutes"),
    (0, 5, "Kill the -ed / -ing confusion and the to/-ing decision",
     "[09-Oct] S03 - Participles, Gerunds and Infinitives.md",
     "S03 exercises (20) + Structure Test 01 Q31-40", 100,
     "verb + to/-ing pairs added to flashcards"),
    (0, 6, "Learn the shape of Section 1 before spending a week on it",
     "listening/[10-Oct] L01 - Part A Strategy.md",
     "Idiom Bank items 1-40; ETS official Part A samples", 100,
     "40 idioms glossed in plain English"),
    (0, 7, "Move S01-S03 from short-term to working memory",
     "progress/error-log.md", "blank-page recall test of every rule", 60,
     "week-00 error-log sweep; week-01 preview notes"),

    (1, 8, "Use that/what/whether + subject + verb, never question order",
     "[12-Oct] S04 - Noun Clauses and Reported Speech.md",
     "S04 exercises (20) + mixed S01-S04 timed 25 items", 100,
     "20 of 25 accuracy; subjunctive items all correct"),
    (1, 9, "Choose the relative pronoun and reduce clauses correctly",
     "[13-Oct] S05 - Adjective Clauses and Reductions.md",
     "S05 exercises (20) + 10 reduction conversions", 100,
     "8 of 10 reductions correct"),
    (1, 10, "Match the connector to the meaning, and get the if-types right",
     "[14-Oct] S06 - Adverb Clauses and Conditionals.md",
     "S06 exercises (20) + mixed timed 25 items", 100,
     "conjunction vs preposition table completed"),
    (1, 11, "Invert after negative fronting; keep comparisons parallel",
     "[15-Oct] S07 - Inversion, Comparatives and Parallelism.md",
     "S07 exercises (20) + mixed timed 25 items", 100,
     "inversion trigger list memorised"),
    (1, 12, "Win Written Expression - vocabulary wearing a grammar costume",
     "[16-Oct] S08 - Word Forms, Articles and Prepositions.md",
     "S08 exercises (25) + Word Families (12 blocks)", 110,
     "30 word families on flashcards"),
    (1, 13, "Sit the full 40-question section at 25 minutes",
     f"{HO}/[17-Oct] Structure Test 01.md",
     "full section, then per-module accuracy table", 120,
     "40 scored, per-module table filled, tracker updated"),
    (1, 14, "Consolidate, then stop early - rest is the work today",
     "progress/error-log.md", "retest every D13 miss from scratch", 60,
     "80% of yesterday's misses now correct"),

    (2, 15, "Stop reading like a novel; read like a search engine",
     "reading/[19-Oct] R01 - Question Types.md",
     "type-identification drill + 1 passage in 11 min", 100,
     "18 of 20 questions labelled correctly"),
    (2, 16, "Answer vocabulary-in-context by supplying your own word first",
     "reading/[20-Oct] R02 - Vocabulary in Context.md",
     "Academic Word List words 1-40", 100,
     "40 new words with a sentence each"),
    (2, 17, "Two full passages at exam pace",
     "reading/[21-Oct] R03 - Practice Passages.md",
     "passages 1 and 2, 10 questions each in 11 min", 100,
     "14 of 20 combined"),
    (2, 18, "Master the two hardest question types",
     "reading/[19-Oct] R01 - Question Types.md",
     "15 inference + NOT/EXCEPT items", 100,
     "75% on inference and NOT/EXCEPT"),
    (2, 19, "Sit the 25-question reading test",
     f"{HO}/[23-Oct] Reading Test 01.md",
     "25 questions in 28 min + per-type table", 100,
     "20 of 25, no question type below 50%"),
    (2, 20, "Check grammar decay before it costs points",
     "vocabulary/[20-Oct] Academic Word List.md",
     "retest all week-01 misses + mixed drill", 100,
     "90% of week-01 misses correct on retest"),
    (2, 21, "Review and set up audio for week 03",
     "progress/error-log.md", "speed check: 1 passage in 9 min", 70,
     "score tracker updated; audio source ready"),

    (3, 22, "Half of Part A tests function, not fact",
     "listening/[10-Oct] L01 - Part A Strategy.md",
     "ETS official Part A samples - one pass only", 100,
     "question type named on 80% of items"),
    (3, 23, "Build the idiom vocabulary that carries Part A",
     "listening/[27-Oct] L02 - Idiom Bank.md",
     "20 Part A items, single pass + shadowing", 100,
     "80 idioms glossed in total"),
    (3, 24, "Capture a two-minute talk on paper in one pass",
     "listening/[28-Oct] L03 - Parts B and C Note-taking.md",
     "Audio Script Bank - 2 lectures, one pass", 100,
     "notes with at least 4 content points per talk"),
    (3, 25, "Sit the 20-question listening test",
     f"{HO}/[29-Oct] Listening Test 01.md",
     "20 questions, script audio, single pass", 90,
     "14 of 20"),
    (3, 26, "Final error sweep before the first mock",
     "https://www.ets.org/toefl/itp/prepare.html",
     "10 L + 15 S + 10 R in 30 min continuous", 100,
     "error log past 60 rows; top 3 mistakes known"),
    (3, 27, "Full 115-minute mock exam, straight through",
     f"{HO}/[31-Oct] Mock Exam Protocol.md",
     "L 35 / S 25 / R 55, no breaks", 180,
     "three section scores; estimated total; timing audit"),
    (3, 28, "Turn the mock into a retarget list",
     "progress/error-log.md", "build the week 04 retarget list", 90,
     "three named weaknesses with a drill for each"),

    (4, 29, "Attack weakness 1 and 2 from the retarget list",
     "progress/error-log.md", "2 x 25 targeted items, timed", 100,
     "80% on both drills"),
    (4, 30, "Reading under pressure - two sets back to back",
     f"{HO}/[23-Oct] Reading Test 01.md",
     "25 questions in 26 min, then passages 3-4 in 20 min", 100,
     "both sets above 75%, finished with time to spare"),
    (4, 31, "Listening double set plus a 22-minute structure sprint",
     "listening/[24-Oct] L04 - Audio Script Bank.md",
     "20 listening items + Structure Test 01 in 22 min", 100,
     "26 of 40 on the sprint even when rushed"),
    (4, 32, "Second full mock exam",
     f"{HO}/[31-Oct] Mock Exam Protocol.md",
     "L 35 / S 25 / R 55, no breaks", 180,
     "estimated total 545 or better"),
    (4, 33, "Final error sweep and whittle the deck",
     "progress/error-log.md", "top-5 pattern drill; flashcards down to 50", 100,
     "top-5 patterns card written"),
    (4, 34, "Half-mock, mental rehearsal, logistics confirmed",
     "reference/Test Day Playbook.md",
     "Structure 40 in 25 min + Reading 25 in 28 min", 90,
     "date, time, venue, ID, pencils, watch written down"),
    (4, 35, "Rest",
     "reference/Timing and Guessing.md", "30 flashcards only, then stop", 30,
     "one line in the log"),

    (5, 36, "Light structure review - no new material",
     "[06-Oct] S01 - Subject-Verb Agreement.md",
     "20 easy mixed items, untimed", 60, "nothing new learned; ended calm"),
    (5, 37, "Light reading and final vocabulary pass",
     "vocabulary/[20-Oct] Academic Word List.md",
     "1 passage untimed + final flashcard pass", 60,
     "final 50 cards reviewed"),
    (5, 38, "Light listening and pack the bag",
     "listening/[24-Oct] L04 - Audio Script Bank.md",
     "1 easy lecture + logistics checklist", 45,
     "bag packed, route checked"),
    (5, 39, "Rehearsal only",
     "reference/Test Day Playbook.md",
     "read the playbook once, read the top-5 card", 30,
     "early night"),
    (5, 40, "Day off",
     "progress/score-tracker.md", "sleep 8 hours", 0, "one line: ready"),
    (5, 41, "Exam day",
     "reference/Test Day Playbook.md", "L 35 / S 25 / R 55", 0,
     "official score recorded"),
    (5, 42, "Retro",
     "progress/score-tracker.md", "write what worked and what did not", 30,
     "retro entry and final push"),
]

WEEK_GOAL = {
    0: ("Establish a measured baseline and buy the first Structure points.", [
        "Sit the diagnostic and record three section numbers",
        "Reach 80% accuracy on S01, S02 and S03 exercises",
        "Gloss the first 40 idioms",
    ]),
    1: ("Finish the grammar code so every Section 2 item names its rule in 5 seconds.", [
        "Cover S04 through S08, one module per day",
        "Score 26 of 40 on the full structure test",
        "Build 30 word-family flashcards",
    ]),
    2: ("Make Reading fast rather than careful.", [
        "Label all 8 question types at speed",
        "Score 20 of 25 on the reading test with no type below 50%",
        "Add 80 academic words to active recall",
    ]),
    3: ("Build the single-pass listening reflex and survive a full mock.", [
        "Cover L01 to L04 with one-pass drills",
        "Score 14 of 20 on the listening test",
        "Finish Mock 1 at 520 or better",
    ]),
    4: ("Make it automatic at speed for two hours.", [
        "Attack the three retarget weaknesses",
        "Finish Mock 2 at 545 or better",
        "Write the top-5 patterns card",
    ]),
    5: ("Arrive sharp, not exhausted.", [
        "Review only - zero new material",
        "Confirm every logistical item in writing",
        "Sit the exam and record the official score",
    ]),
}

NOTE = {
    41: "**Exam day.** Nothing new. Read the playbook, then go and do it.",
    40: "**Day off.** One line and close the file. Rest is part of the work.",
    35: "**Rest day.** Twenty minutes of flashcards, then stop.",
    42: "**Retro day.** Record the official score, then write honestly what you would change.",
    27: "**Mock exam 1.** Full protocol: 15 min setup, 115 min straight through, 20 min marking, 45 min analysis.",
    32: "**Mock exam 2.** Same protocol. Also log your focus at minute 90 and what you ate beforehand.",
}

DAY_MATERIAL = {
    6: "listening/[27-Oct] L02 - Idiom Bank.md",
    12: "vocabulary/[16-Oct] Word Families.md",
    16: "vocabulary/[20-Oct] Academic Word List.md",
}


def fname(day: int) -> str:
    return (START + dt.timedelta(days=day - 1)).strftime("%d-%m-%Y.md")


def wdir(week: int) -> str:
    return f"week-{week:02d}"


def target_of(material: str) -> str:
    if material.startswith("http") or material.startswith(("progress/", "docs/")):
        return material
    if material.startswith(("study-notes/", "hands-on/")):
        return f"{DOCS}/{material}"
    return f"{SN}/{material}"


def rel_link(src_dir: str, target: str, label: str) -> str:
    if target.startswith("http"):
        return f"[{label}]({target})"
    rel = os.path.relpath(target, src_dir).replace("\\", "/")
    return f"[{label}](<{rel}>)"


def label_of(path: str) -> str:
    base = re.sub(r"\.md$", "", path.rsplit("/", 1)[-1])
    base = re.sub(r"^\[\d{2}-[A-Za-z]{3}\]\s*", "", base)
    return base


def plan_rows(material: str, drill: str, budget: int) -> str:
    if budget == 0:
        rows = [("P1", "Rest or sit the exam - no study", "Scheduled rest",
                 "one line in the log", "0 min", "this file")]
    elif budget <= 35:
        rows = [
            ("P1", "Light review of already-known material", "Confidence, not testing",
             "30 flashcards reviewed", f"{round(budget * 0.6)} min", "score tracker"),
            ("P2", "Update the score tracker", "Weekly roll-up",
             "week row filled", f"{round(budget * 0.4)} min", "score tracker"),
        ]
    elif budget >= 150:
        rows = [
            ("P1", "Full mock sitting in one continuous block", "Mock exam",
             "three section scores", "115 min", "answer grids"),
            ("P1", "Mark and convert the scores", "Mock exam",
             "estimated total", "20 min", "score tracker"),
            ("P2", "Per-module and per-type analysis", "Mock exam",
             "accuracy tables", "25 min", "error log"),
            ("P3", "Commit", "Streak", "commit", "5 min", "git log"),
        ]
    else:
        rows = [
            ("P1", f"Study {label_of(material)}", "Instruction block",
             "rule written in own words", "25 min", "error log"),
            ("P1", f"Timed drill: {drill}", "Timed block",
             "a score", "25 min", "score tracker"),
            ("P2", "Guided practice on the same material", "Practice block",
             "exercise set completed", "20 min", "exercise answers"),
            ("P1", "Error review - name every miss", "Review block",
             "error-log rows", "20 min", "error log"),
            ("P3", "Warm-up flashcards", "Warm-up block", "10 cards", "5 min", "-"),
            ("P3", "Commit the day", "Streak", "commit", "5 min", "git log"),
        ]
    out = ["| Priority | Task | Related Milestone or Action Item | Expected Deliverable "
           "| Estimated Time | Planned Evidence |", "|---|---|---|---|---|---|"]
    out += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(out)


def build(day: int, week: int, objective: str, material: str,
          drill: str, budget: int, evidence: str) -> str:
    date = START + dt.timedelta(days=day - 1)
    src_dir = f"docs/logs/daily/{wdir(week)}"
    goal, milestones = WEEK_GOAL[week]
    week_end = START + dt.timedelta(days=week * 7 + 6)

    prev = "../TEMPLATE.md" if day == 1 else fname(day - 1)
    nxt = "../README.md" if day == DAYS else fname(day + 1)
    if day in (8, 15, 22, 29, 36):
        prev = "../" + wdir(week - 1) + "/" + fname(day - 1)
    if day in (7, 14, 21, 28, 35):
        nxt = "../" + wdir(week + 1) + "/" + fname(day + 1)

    note = NOTE.get(day, "")
    note_line = f"\n> {note}\n" if note else ""
    ms = "\n".join(
        f"  * Milestone {i}: {m}, Due {week_end.strftime('%Y/%m/%d')}"
        for i, m in enumerate(milestones, 1))

    target = target_of(material)
    mat = rel_link(src_dir, target, label_of(target))

    return f"""### Date

**Date:** {date.strftime('%Y/%m/%d')}

### Short-term Goal

{goal}

* Goal 1: {milestones[0]}
* Goal 2: {milestones[1]}
* Goal 3: {milestones[2]}

**Milestones for this week (due {week_end.strftime('%Y/%m/%d')}):**

{ms}
{note_line}
---

### Plan

{plan_rows(material, drill, budget)}

**Objective for today:** {objective}

**Material:** {mat}

**Drill:** {drill}

**Budget:** {budget} min

**Evidence expected:** {evidence}

---

### Daily Log

1. 09:00 - 09:05: Warm-up - 10 flashcards from yesterday's misses
   (_Status:_ )
2. 09:05 - 09:30: Instruction - {label_of(material)}
   (_Status:_ )
3. 09:30 - 09:50: Guided practice - exercise set, checked as you go
   (_Status:_ )
4. 09:50 - 10:15: Timed drill - {drill}
   (_Status:_ )
5. 10:15 - 10:35: Error review - every miss named and logged
   (_Status:_ )
6. 10:35 - 10:40: Commit
   (_Status:_ )

### Score

| Item | Score | Target | Met? |
|---|---:|---:|---|
| | | | |

### Errors

| Src | Category | Why | Fix |
|---|---|---|---|
| | | | |

### Reflection

1. **What went well:**
2. **What didn't:**
3. **Tomorrow's first move:**

---

**Commit message:** `day {day:02d}: `

---

[← previous](<{prev}>) · [next →](<{nxt}>)
"""


def build_index() -> str:
    themes = {
        0: "Diagnostic and structure bootcamp",
        1: "Structure deep dive",
        2: "Reading comprehension",
        3: "Listening comprehension and mock 1",
        4: "Integration and mock 2",
        5: "Taper and exam",
    }
    out = ["# Daily Study Logs — TOEFL ITP Level 1, October to November 2026", "",
           "Weekdays use the planned budget of **1.5–2 hours**. Sundays are deliberately short. "
           "Days 35 and 40 record zero scheduled study time. Day 41 is the exam.", ""]
    for wk in range(6):
        out += [f"## Week {wk:02d} — {themes[wk]}", ""]
        for day in range(wk * 7 + 1, min(wk * 7 + 8, DAYS + 1)):
            d = START + dt.timedelta(days=day - 1)
            out.append(f"- [{d.strftime('%d %B')}](<{wdir(wk)}/{fname(day)}>) — day {day:02d}")
        out.append("")
    out += ["---", "",
            "Blank entry: [TEMPLATE.md](<TEMPLATE.md>) · "
            "Weekly reports: [../weekly/](<../weekly/>) · "
            "Tracker: [score-tracker](<../../../progress/score-tracker.md>)"]
    return "\n".join(out) + "\n"


def build_template() -> str:
    return """### Date

**Date:** YYYY/MM/DD

### Short-term Goal

* Goal 1:
  * Milestone 1: , Due YYYY/MM/DD

---

### Plan

| Priority | Task | Related Milestone or Action Item | Expected Deliverable | Estimated Time | Planned Evidence |
|---|---|---|---|---|---|
| P1 | | | | | |

---

### Daily Log

1. HH:MM - HH:MM:
   (_Status:_ )

### Score

| Item | Score | Target | Met? |
|---|---:|---:|---|
| | | | |

### Errors

| Src | Category | Why | Fix |
|---|---|---|---|
| | | | |

### Reflection

1. **What went well:**
2. **What didn't:**
3. **Tomorrow's first move:**

---

**Commit message:** `day NN: `
"""


def main() -> int:
    force = "--force" in sys.argv
    written = skipped = 0
    for idx, (week, diw, objective, material, drill, budget, evidence) in enumerate(SCHEDULE, 1):
        d = os.path.join(DAILY, wdir(week))
        os.makedirs(d, exist_ok=True)
        path = os.path.join(d, fname(idx))
        if os.path.exists(path) and not force:
            skipped += 1
            continue
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(build(idx, week, objective, material, drill, budget, evidence))
        written += 1

    for name, content in (("README.md", build_index()), ("TEMPLATE.md", build_template())):
        p = os.path.join(DAILY, name)
        if force or not os.path.exists(p):
            with open(p, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(content)

    print(f"daily logs: {written} written, {skipped} skipped")
    print(f"range: {START.isoformat()} -> {(START + dt.timedelta(days=DAYS - 1)).isoformat()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
