"""Invoice generation + Linear ping at two-week period close.

Run on the same Friday-EOD cadence as weekly.py. If the next retainer period
has closed and its PDF doesn't exist yet, generate it and post a Linear
'Client Admin' issue so Brent knows it's ready to review and send.

Usage:
    /Users/brentbartosch/Development/EZO/.venv/bin/python \
        invoicing/pipeline/period_close.py [--dry-run]
"""
import argparse
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from gen_retainer import OUT, render  # noqa: E402
from pipeline import linear, sheets  # noqa: E402
from pipeline.config import (  # noqa: E402
    INVOICE_AMOUNT,
    INVOICING_ROOT,
    SMOOTHOPS_ROOT,
    TRIAL_INVOICE_COUNT,
    fmt_day,
    fmt_range,
    retainer_period,
    week_label,
    week_number,
)


def _highest_existing_invoice() -> int:
    nums = []
    for p in OUT.glob("Smoothed_Invoice_*_EZO.pdf"):
        num_part = p.stem.split("_")[2]  # "0006"
        digits = "".join(ch for ch in num_part if ch.isdigit())
        if digits:
            nums.append(int(digits))
    return max(nums, default=TRIAL_INVOICE_COUNT)


def _pdf_path(invoice_num: str) -> Path:
    return OUT / f"Smoothed_Invoice_{invoice_num}_EZO.pdf"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="print the invoice plan; do not write files or Linear")
    args = ap.parse_args()

    today = date.today()
    highest = _highest_existing_invoice()
    next_invoice_num = f"{highest + 1:04d}"
    next_period = highest - TRIAL_INVOICE_COUNT + 1  # invoice N = period (N-5)

    start, end = retainer_period(next_period)
    if end > today:
        print(
            f"Next period {next_period} ({fmt_range(start, end)}) is still open "
            f"(closes {fmt_day(end)}). Nothing to invoice yet."
        )
        return

    inv = {
        "invoice_num": next_invoice_num,
        "issued": fmt_day(today),
        "due": fmt_day(today + timedelta(days=7)),
        "period_label": f"Weeks {week_number(start)}–{week_number(start + timedelta(days=7))}",
        "period": fmt_range(start, end),
        "amount": INVOICE_AMOUNT,
        "sub_desc": (
            "Deliverables for the two-week period as recorded in the Milestone "
            "Tracker. Fee of USD 9,000 per two-week period per Agreement B, Exhibit A §6."
        ),
    }

    print(f"Period {next_period} closed. Invoice {next_invoice_num}:")
    for k, v in inv.items():
        print(f"  {k}: {v}")

    if args.dry_run:
        print("\n[dry-run] not writing files or Linear.")
        return

    html_path = OUT / f"smoothed-invoice-{next_invoice_num}-ezo.html"
    html_path.write_text(render(inv))
    pdf_path = _pdf_path(next_invoice_num)
    subprocess.run(
        [
            "node", str(SMOOTHOPS_ROOT / "generate-pdf.mjs"),
            str(html_path), str(pdf_path), "--format=letter",
        ],
        cwd=str(SMOOTHOPS_ROOT),
        check=True,
    )
    print(f"Wrote {pdf_path}")

    description = (
        f"Invoice {next_invoice_num} is ready for period {next_period} "
        f"({inv['period']}).\n\n"
        f"PDF: `{pdf_path.name}` (in `invoicing/output/`)\n\n"
        "Review, attach, and send to finance (Shawn approves)."
    )
    issue = linear.post_issue(f"Invoice {next_invoice_num} ready — review & send", description)
    print(f"Linear issue: {issue.get('identifier')} — {issue.get('url')}")


if __name__ == "__main__":
    main()
