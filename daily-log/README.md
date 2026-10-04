# Daily Log

Internship-style journal. **42 entries, 5 Oct → 15 Nov 2026.** One file per day, one commit per day.

```
daily-log/
├── README.md        ← you are here
├── TEMPLATE.md      ← blank entry, copy it if you need an extra day
├── 2026-10-05.md    ← Day 1, the diagnostic
├── 2026-10-06.md
├── …
└── 2026-11-15.md    ← Day 42, the retro
```

---

## Why bother

Three reasons, in order of importance:

1. **It forces the error review.** The single highest-value 20 minutes of any study day is
   writing down *why* you got something wrong. If you skip the log, you'll skip that too.
2. **It makes progress visible.** Motivation collapses around day 18 because grammar feels
   endless. Scrolling back through 18 committed days is the antidote.
3. **It's evidence.** If you need to retake, or to show anyone how you prepared, it's all here.

---

## The daily routine (5 minutes, at the end)

1. Open today's file. It's already pre-filled with the plan — objective, material links, drill.
2. Fill **Actual** times. Be honest; if you did 40 minutes, write 40.
3. Tick **Done**.
4. Fill **Score** with whatever number the day produced.
5. Add every miss to the **Errors today** table — and copy them into
   [progress/error-log.md](../progress/error-log.md).
6. Write the **Reflection**. Three lines. Not more.
7. Commit:

```bash
git add daily-log/2026-10-06.md progress/error-log.md
git commit -m "day 02: S01 subject-verb agreement — 17/20"
git push origin main
```

---

## What a good entry looks like

| Field | Bad | Good |
|---|---|---|
| Reflection | "Good session." | "S01 decoy 5 still trips me — *the number of* vs *a number of*. Made 3 cards, will drill tomorrow." |
| Why (errors) | "careless" | "chose *was* because 'study' was nearest to the verb" |
| Score | "ok" | "17/20 (target 16)" |
| Actual time | 90 | 45 — and a note: "cut short, commuting" |

> **The only unforgivable entry is a fake one.** If you did nothing, write "did nothing" and say
> why. A log with honest zeros is far more useful than one with invented numbers.

---

## Scoring your streak

| Streak | Meaning |
|---|---|
| 1–3 days | Starting |
| 7 days | One full week — the habit is forming |
| 14 days | You're past the drop-out point |
| 21 days | Automatic |
| 42 days | **You sat the exam.** |

---

## Templates by day type

| Day type | Focus of the reflection |
|---|---|
| Instruction day (Mon–Fri, weeks 0–1) | Which rule still isn't automatic? |
| Drill day (Thu, Sat) | Where did the clock hurt? |
| Test day (D13, D19, D25, D27, D32) | Which module/type is worst? |
| Review day (Sun) | What's the pattern across the week? |
| Rest day (D35, D40) | One line. Rest is part of the work. |
| Exam day (D41) | What surprised you? Write it while it's fresh. |
