# Program Documentation

How the pieces of this repository fit together, and the conventions they follow.

---

## 1. Structure

| Layer | Path | Role | Changes often? |
|---|---|---|---|
| Plan | `docs/Goals-Summary.md` | weekly objectives, topics, deadlines | rarely |
| Plan | `docs/curriculum/week-NN.md` | 7 daily lesson plans per week | rarely |
| Content | `docs/study-notes/` | the material itself | rarely |
| Practice | `docs/hands-on/` | tests, drills, mock protocol | rarely |
| Journal | `docs/logs/daily/week-NN/` | 42 daily entries | **daily** |
| Journal | `docs/logs/weekly/` | weekly reports | weekly |
| Journal | `Daily-Logs.md` | master journal, newest first | daily |
| Evidence | `progress/score-tracker.md` | every score | on assessment days |
| Evidence | `progress/error-log.md` | every mistake, with a reason | **daily** |
| Support | `support/learning-support-plan.md` | study-access plan, goals and review | on review dates |
| Ops | `docs/study-setup-guide.md` | environment setup | once |
| Ops | `docs/logs/Important Dates.md` | non-study dates and deadlines | as needed |
| Tooling | `tools/generate_daily_logs.py` | regenerates the 42 entries | rarely |

## 2. Conventions

**File naming**

- Study notes and tests: `[DD-Mon] Name.md` — e.g. `[06-Oct] S01 - Subject-Verb Agreement.md`.
  The bracketed date is the day the material is scheduled, so the folder reads as a timeline.
- Daily logs: `DD-MM-YYYY.md` inside `docs/logs/daily/week-NN/`.
- Weekly reports: `YYYY-MM-DD-to-YYYY-MM-DD.md`.

**Links**

- Paths containing spaces are written in angle-bracket form: `[label](<path with spaces.md>)`.
  This is what renders reliably on GitHub. (That example is illustrative, not a real link.)
- All internal links are **relative**, so the repository works on any branch or fork.

**Checkboxes**

- `- [ ]` in `README.md`, `Goals-Summary.md` and the daily logs means *not yet done*.
- Tick them as you go — the checkboxes in the README are the end-of-program report.

**Status lines**

- Every daily-log line carries `(_Status:_ )`. Fill it the same day.
- Status should contain a number where a number exists: `(_Status:_ Done - 32/40 on S01 drill)`.

## 3. Daily loop

1. Open today's file in `docs/logs/daily/week-NN/`.
2. Read the **Plan** table — priorities, expected deliverable, estimated time, evidence.
3. Open the linked **Material** in `docs/study-notes/`.
4. Run the **Drill** from `docs/hands-on/`, timed.
5. Log every miss in `progress/error-log.md`.
6. Fill in the **Score**, **Errors** and **Reflection** blocks.
7. Add a line to `Daily-Logs.md` for the week.
8. Commit: `git commit -m "day NN: <section> drill <score>"`.

## 4. Assessment schedule

| Day | Date | Assessment | Pass mark |
|---:|---|---|---|
| 1 | 2026-10-05 | Diagnostic | record baseline |
| 13 | 2026-10-17 | Structure Test 01 | 26 / 40 |
| 19 | 2026-10-23 | Reading Test 01 | 20 / 25 |
| 25 | 2026-10-29 | Listening Test 01 | 14 / 20 |
| 27 | 2026-10-31 | Mock exam 1 | 520 |
| 32 | 2026-11-05 | Mock exam 2 | 545 |
| 41 | 2026-11-14 | **Real exam** | **550** |

## 5. Rules that make it work

1. **Commit daily.** The streak is the motivation system.
2. **Never leave a wrong answer unexplained.** One line: rule → why → fix.
3. **Timed or it doesn't count.** No untimed drills after week 01.
4. **No new material in the last five days.**
5. **Never leave a bubble empty on the real test.** No guessing penalty.

## 6. Regenerating the logs

```bash
python tools/generate_daily_logs.py          # fills in missing files only
python tools/generate_daily_logs.py --force  # rewrites everything from scratch
```

The generator holds the full 42-day schedule: objective, material, drill, time budget and
expected evidence per day. Editing the schedule there and re-running with `--force` is the
fastest way to re-plan.
