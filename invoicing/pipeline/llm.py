"""Draft a week's tracker entry using EZO's corporate OpenRouter key.

Honest-first: the prompt instructs the model to state only what the evidence
supports, lead with real wins, and mark partial work "in progress" rather than
complete. If the key is missing or the call fails, it falls back to a verbatim
evidence listing so the sheet is still filled with something accurate.
"""
import json
import os
import re

from dotenv import load_dotenv

from .config import EZO_ROOT, OPENROUTER_MODEL, OPENROUTER_URL

_PROMPT = """You are filling in a weekly consulting milestone tracker for an AI content-pipeline engagement.

Week: {week_label}

Evidence of what was actually done this week (from the consultant's repo — deliverable files, meeting notes, git commits):
{evidence}

Write three fields:
1. "focus" — a short (2-8 word) label for the week's theme.
2. "deliverables" — a bullet list (one per line, each starting with "• ") of what was delivered or committed this week.
3. "results" — a 3-6 sentence paragraph summarizing what actually landed, leading with the wins.

Rules (IMPORTANT):
- Be ACCURATE: state only what the evidence supports.
- Lead with what was actually delivered. Frame partial or blocked work as "in progress" or "carried forward" — never as complete.
- Do NOT invent outcomes (for example, do not claim pages "went live" unless the evidence says so).
- Keep it concise and professional; no markdown headings.

Return ONLY valid JSON in this shape: {"focus": "...", "deliverables": "...", "results": "..."}
"""


def _key():
    load_dotenv(EZO_ROOT / ".env")
    return os.getenv("OPEN_ROUTER_API_KEY")


def _extract_json(text: str):
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None


def _fallback(week_label: str, evidence: str):
    items = [ln.strip() for ln in evidence.splitlines() if ln.strip() and not ln.startswith("Week starting")]
    bullets = "\n".join("• " + ln.lstrip("- ").strip() for ln in items[:8]) or "• No evidence captured this week."
    results = "Evidence captured this week:\n" + "\n".join("- " + ln for ln in items[:8])
    return {"focus": "Weekly deliverables", "deliverables": bullets, "results": results}


def draft_week(week_label: str, evidence: str):
    key = _key()
    if not key:
        return _fallback(week_label, evidence)

    try:
        import requests
        payload = {
            "model": OPENROUTER_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": _PROMPT.replace("{week_label}", week_label).replace("{evidence}", evidence),
                }
            ],
            "temperature": 0.3,
        }
        r = requests.post(
            OPENROUTER_URL,
            headers={"Authorization": f"Bearer {key}"},
            json=payload,
            timeout=90,
        )
        r.raise_for_status()
        content = r.json()["choices"][0]["message"]["content"]
        data = _extract_json(content)
        if not data:
            return _fallback(week_label, evidence)
        return {
            "focus": str(data.get("focus", "")).strip(),
            "deliverables": str(data.get("deliverables", "")).strip(),
            "results": str(data.get("results", "")).strip(),
        }
    except Exception:
        return _fallback(week_label, evidence)
