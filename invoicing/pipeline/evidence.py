"""Gather a week's worth of evidence from the EZO repo (deterministic).

Reads file mtimes under deliverables/ and meetings/, plus git commits, for the
given Monday-Sunday window. The output is a plain-text block the drafter turns
into a tracker entry.
"""
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

from .config import EZO_ROOT

_IGNORED = {"node_modules", ".git", ".venv", "__pycache__", ".DS_Store"}


def _in_window(f: Path, start: datetime, end: datetime) -> bool:
    try:
        return start <= datetime.fromtimestamp(f.stat().st_mtime) <= end
    except OSError:
        return False


def _visible(rel: Path) -> bool:
    return not any(part.startswith(".") or part in _IGNORED for part in rel.parts)


def gather(week_start):
    """week_start: datetime.date (Monday). Returns a plain-text evidence block."""
    start = datetime.combine(week_start, datetime.min.time())
    end = start + timedelta(days=7)

    files = []
    for sub in ("deliverables", "meetings"):
        base = EZO_ROOT / sub
        if not base.exists():
            continue
        for f in base.rglob("*"):
            if f.is_file() and _in_window(f, start, end) and _visible(f.relative_to(EZO_ROOT)):
                files.append(f.relative_to(EZO_ROOT).as_posix())
    files.sort()

    commits = []
    try:
        out = subprocess.run(
            [
                "git", "-C", str(EZO_ROOT), "log",
                "--since", start.isoformat(),
                "--until", end.isoformat(),
                "--oneline", "--no-merges",
            ],
            capture_output=True, text=True, check=False,
        )
        commits = [ln for ln in out.stdout.splitlines() if ln.strip()]
    except Exception:
        commits = []

    lines = [f"Week starting {week_start.isoformat()}"]
    if files:
        lines.append("\nFiles landed this week:")
        lines.extend(f"- {p}" for p in files)
    if commits:
        lines.append("\nGit commits this week:")
        lines.extend(f"- {c}" for c in commits[:40])
    if not files and not commits:
        lines.append("(no repo files or commits found in this window)")
    return "\n".join(lines)
