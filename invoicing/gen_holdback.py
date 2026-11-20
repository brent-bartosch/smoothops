#!/usr/bin/env python3
"""Generate the EZO holdback invoice (Agreement B section 9.5), issued after the
section 10 handover once EZO terminated effective 30 Oct 2026.

Built from invoice-template-retainer.html, with the retainer-only wording swapped
for holdback wording and one line per month (pro rata by calendar day, 9.5).

    python3 invoicing/gen_holdback.py
    node generate-pdf.mjs invoicing/output/smoothed-invoice-0011-ezo.html \
        invoicing/output/Smoothed_Invoice_0011_EZO.pdf --format=letter
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "output"

INV = {
    "invoice_num": "0011",
    "issued": "16 Nov 2026",
    "due": "23 Nov 2026",
}
# (description, service period, amount). $2,000/month, partial months pro rata.
LINES = [
    ("Holdback &mdash; August (8 of 31 days)", "24 Aug &ndash; 31 Aug 2026", 2000 * 8 / 31),
    ("Holdback &mdash; September", "1 Sep &ndash; 30 Sep 2026", 2000.0),
    ("Holdback &mdash; October (30 of 31 days)", "1 Oct &ndash; 30 Oct 2026", 2000 * 30 / 31),
]


def money(x: float) -> str:
    return f"{x:,.2f}"


def must_replace(html: str, old: str, new: str) -> str:
    # Fail loud: a template edit that moves this text must break the build,
    # not ship an invoice that still says "not included in this invoice".
    if html.count(old) != 1:
        raise SystemExit(f"template text not found exactly once: {old[:60]!r}")
    return html.replace(old, new)


def render() -> str:
    html = (ROOT / "invoice-template-retainer.html").read_text()
    cents = [round(a, 2) for _, _, a in LINES]
    total = money(sum(cents))

    html = must_replace(
        html,
        "<div><dt>Terms</dt><dd>Net 7 from receipt</dd></div>",
        "<div><dt>Terms</dt><dd>Payable on handover completion</dd></div>",
    )
    html = must_replace(
        html,
        "<div><dt>Reference</dt><dd>Exhibit A &sect;6</dd></div>",
        "<div><dt>Reference</dt><dd>&sect;9.5 &middot; &sect;10</dd></div>",
    )
    html = must_replace(
        html,
        "Deliverables per the Milestone Tracker &mdash; &ldquo;Consulting Milestones &ndash; Brent Bartosch&rdquo;<br>",
        "Terminated by Client for convenience, effective 30 Oct 2026 (&sect;9.1)<br>",
    )
    html = must_replace(
        html,
        "Holdback USD 2,000/month accrues separately &mdash; not included in this invoice (Agreement B &sect;9.5)",
        "All two-week periods through 1 Nov 2026 invoiced and paid (invoices 0006&ndash;0010)",
    )
    html = must_replace(
        html,
        """Payable within seven (7) days after receipt of this invoice, upon
        Client&rsquo;s written approval in the Milestone Tracker of the Deliverables
        completed for this two-week period, per Agreement B Exhibit A &sect;6.""",
        """Holdback vested on termination and payable promptly following
        completion of the handover and transition obligations under Section 10,
        per Agreement B &sect;9.5. Pro rata by calendar day for partial months.""",
    )
    row_tpl = """      <tr>
        <td class="desc">
          Consulting services &mdash; {{PERIOD_LABEL}}
          <span class="sub">{{SUB_DESC}}</span>
        </td>
        <td>{{PERIOD}}</td>
        <td class="num">{{AMOUNT}}</td>
      </tr>"""
    rows = "\n".join(
        f"""      <tr>
        <td class="desc">{desc}</td>
        <td>{period}</td>
        <td class="num">{money(amt)}</td>
      </tr>"""
        for (desc, period, _), amt in zip(LINES, cents)
    )
    html = must_replace(html, row_tpl, rows)
    # No expenses line on a holdback invoice; dropping it also keeps the page to one.
    html = must_replace(
        html,
        """      <tr>
        <td colspan="2" class="label">Reimbursable expenses <span style="font-size:11.5px">(none &mdash; LLM &amp; tooling costs run through EZO accounts)</span></td>
        <td class="num">0.00</td>
      </tr>
""",
        "",
    )
    html = must_replace(html, "<caption>Services</caption>", "<caption>Holdback (&sect;9.5)</caption>")
    html = html.replace("{{AMOUNT}}", total)
    for key, val in INV.items():
        html = html.replace("{{" + key.upper() + "}}", val)
    if "{{" in html:
        raise SystemExit("unfilled placeholder left in the invoice")
    return html


def main():
    OUT.mkdir(exist_ok=True)
    path = OUT / f"smoothed-invoice-{INV['invoice_num']}-ezo.html"
    path.write_text(render())
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
