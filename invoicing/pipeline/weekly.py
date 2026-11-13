"""Weekly milestone-tracker update — run Friday end of day.

1. Determine the current milestone week (Mon-Sun).
2. Gather evidence from the EZO repo.
3. Draft Focus / Deliverables / Results (OpenRouter, honest fallback otherwise).
4. Auto-write the Google Sheet.
5. Post a Linear 'Client Admin' review note.

Usage:
    /Users/brentbartosch/Development/EZO/.venv/bin/python \
        invoicing/pipeline/weekly.py [--dry-run] [--date YYYY-MM-DD]
"""
import argparse
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipeline import evidence, linear, llm, sheets  # noqa: E402
from pipeline.config import monday_of, week_label  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="draft only; do not write sheet or Linear")
    ap.add_argument("--date", help="override 'today' (YYYY-MM-DD)")
    args = ap.parse_args()

    today = date.fromisoformat(args.date) if args.date else date.today()
    mon = monday_of(today)
    label = week_label(mon)

    evidence_text = evidence.gather(mon)
    draft = llm.draft_week(f"Week starting {label}", evidence_text)

    print(f"Week: {label}")
    print(f"Focus: {draft['focus']}")
    print(f"Deliverables:\n{draft['deliverables']}")
    print(f"Results:\n{draft['results']}")

    if args.dry_run:
        print("\n[dry-run] not writing sheet or Linear.")
        return

    action, row = sheets.upsert_week(label, draft["focus"], draft["deliverables"], draft["results"])
    print(f"\nSheet: {action} row {row}")

    description = (
        f"Tracker updated for week starting {label}.\n\n"
        f"**Focus:** {draft['focus']}\n\n"
        f"**Deliverables:**\n{draft['deliverables']}\n\n"
        f"**Results:**\n{draft['results']}\n\n"
        "Review the Google Sheet and correct anything before invoices go out."
    )
    issue = linear.post_issue(f"Tracker: week {label} filled — review", description)
    print(f"Linear issue: {issue.get('identifier')} — {issue.get('url')}")


if __name__ == "__main__":
    main()
