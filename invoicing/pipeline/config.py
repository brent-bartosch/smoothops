"""Shared configuration and date helpers for the invoicing automation.

Secrets are referenced, never copied:
- Google Sheets: EZO/.secrets/google-token.json (+ google-oauth-client.json)
  via EZO/scripts/google_auth.py.
- Linear: LINEAR_API_KEY in ~/Development/api-toolkit/.env
  via services/linear/api.py.
- OpenRouter: OPEN_ROUTER_API_KEY in EZO/.env.
"""
from datetime import date, timedelta
from pathlib import Path

SMOOTHOPS_ROOT = Path(__file__).resolve().parents[2]
INVOICING_ROOT = SMOOTHOPS_ROOT / "invoicing"
EZO_ROOT = Path.home() / "Development" / "EZO"
API_TOOLKIT_ROOT = Path.home() / "Development" / "api-toolkit"

# Google Sheets — "Consulting Milestones - Brent Bartosch"
SHEET_ID = "1ALnHW0qVxaH4OwqXnm_YFrXtzx0nXs11MfTNONJZrgM"
SHEET_NAME = "Sheet1"

# Linear
LINEAR_TEAM = "EZO"
LINEAR_PROJECT = "Client Admin"
LINEAR_ASSIGNEE = "brent@smoothed.io"

# OpenRouter (weekly drafting)
OPENROUTER_MODEL = "google/gemini-3.1-pro-preview"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# Engagement calendar. Milestone weeks are Mon-Sun and labelled by their Monday.
ENGAGEMENT_START = date(2026, 7, 20)   # "Week 1" = Jul 20
RETAINER_START = date(2026, 8, 24)     # "Week 6" = Aug 24 (Agreement B effective)
INVOICE_AMOUNT = "9,000.00"
# Invoices 0001-0005 were the trial weeks; retainer period N -> invoice N+5.
TRIAL_INVOICE_COUNT = 5


def monday_of(d: date) -> date:
    return d - timedelta(days=d.weekday())


def week_label(d: date) -> str:
    """Milestone row label, e.g. 'Oct 12'."""
    return d.strftime("%b") + " " + str(d.day)


def week_number(d: date) -> int:
    """Engagement week number (Jul 20 == 1). d is assumed to be a Monday."""
    return (d - ENGAGEMENT_START).days // 7 + 1


def fmt_day(d: date) -> str:
    """'25 Sep 2026'."""
    return f"{d.day} {d.strftime('%b')} {d.year}"


def fmt_range(start: date, end: date) -> str:
    """'24 Aug – 6 Sep 2026'."""
    return f"{start.day} {start.strftime('%b')} – {end.day} {end.strftime('%b')} {end.year}"


def retainer_period(period_number: int):
    """Return (start, end) for a 1-based two-week retainer period."""
    start = RETAINER_START + timedelta(days=14 * (period_number - 1))
    return start, start + timedelta(days=13)
