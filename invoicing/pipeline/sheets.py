"""Google Sheets read/write for the "Consulting Milestones" tracker.

Reuses EZO's OAuth token by reference — the secret stays in the EZO repo.
Run under the EZO venv python (has googleapiclient + google-auth).
"""
import sys

from .config import EZO_ROOT, SHEET_ID, SHEET_NAME


def _service():
    sys.path.insert(0, str(EZO_ROOT / "scripts"))
    from google_auth import get_creds  # noqa: E402
    from googleapiclient.discovery import build  # noqa: E402
    return build("sheets", "v4", credentials=get_creds())


def read_rows():
    svc = _service()
    return (
        svc.spreadsheets()
        .values()
        .get(spreadsheetId=SHEET_ID, range=f"'{SHEET_NAME}'")
        .execute()
        .get("values", [])
    )


def get_week(week_label: str):
    """Return the row (list of cells) for a given 'Week starting' label, or None."""
    for row in read_rows():
        if row and row[0] == week_label:
            while len(row) < 4:
                row.append("")
            return row
    return None


def upsert_week(week_label: str, focus: str, deliverables: str, results: str):
    """Update the row whose column A == week_label, else append a new row.

    Column order: A=Week starting, B=Focus, C=Deliverables, D=Results.
    Returns (action, row_number).
    """
    svc = _service()
    rows = read_rows()

    for i, row in enumerate(rows):
        if row and row[0] == week_label:
            svc.spreadsheets().values().update(
                spreadsheetId=SHEET_ID,
                range=f"'{SHEET_NAME}'!A{i + 1}:D{i + 1}",
                valueInputOption="USER_ENTERED",
                body={"values": [[week_label, focus, deliverables, results]]},
            ).execute()
            return "updated", i + 1

    svc.spreadsheets().values().append(
        spreadsheetId=SHEET_ID,
        range=f"'{SHEET_NAME}'!A:D",
        valueInputOption="USER_ENTERED",
        insertDataOption="INSERT_ROWS",
        body={"values": [[week_label, focus, deliverables, results]]},
    ).execute()
    return "appended", len(rows) + 1
