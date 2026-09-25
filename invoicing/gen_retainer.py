#!/usr/bin/env python3
"""Generate EZO retainer invoices (Agreement B: $9,000 per two-week period).

Add a dict to INVOICES for each new period, then run:
    python3 invoicing/gen_retainer.py
to write HTML files, and:
    node generate-pdf.mjs invoicing/output/<html> invoicing/output/<pdf> --format=letter
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TPL = (ROOT / "invoice-template-retainer.html").read_text()
OUT = ROOT / "output"

# Two-week periods under Agreement B (effective 24 Aug 2026). Weeks are Mon-Sun,
# matching the "Consulting Milestones - Brent Bartosch" sheet.
INVOICES = [
    {
        "invoice_num": "0006",
        "issued": "25 Sep 2026",
        "due": "2 Oct 2026",
        "period_label": "Weeks 6\u20137",
        "period": "24 Aug \u2013 6 Sep 2026",
        "amount": "9,000.00",
        "sub_desc": (
            "Two-week period per the Milestone Tracker: brief generation scheduled "
            "Monday and Thursday, the Elementor bridge completed and verified, "
            "competitive research automated, the engineering walkthrough delivered, "
            "and the outbound/email fork scoped."
        ),
    },
    {
        "invoice_num": "0007",
        "issued": "25 Sep 2026",
        "due": "2 Oct 2026",
        "period_label": "Weeks 8\u20139",
        "period": "7 Sep \u2013 20 Sep 2026",
        "amount": "9,000.00",
        "sub_desc": (
            "Two-week period per the Milestone Tracker: keyword research running "
            "unattended end-to-end, the reviewer comment loop live, the blog path "
            "rebuilt against the fix list, and the keyword benchmark completed."
        ),
    },
]


def render(inv: dict) -> str:
    html = TPL
    for key, val in inv.items():
        html = html.replace("{{" + key.upper() + "}}", val)
    return html


def main():
    OUT.mkdir(exist_ok=True)
    for inv in INVOICES:
        path = OUT / f"smoothed-invoice-{inv['invoice_num']}-ezo.html"
        path.write_text(render(inv))
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
