# Invoicing

Invoice generation + weekly milestone-tracker automation for Smoothed LLC consulting engagements.

## Structure

```
invoicing/
  README.md
  invoice-template.html            # trial-week invoice template ($5k, "accepted on" wording)
  invoice-template-retainer.html   # Agreement B retainer template ($9k/2-week, Net 7)
  gen_retainer.py                  # manual retainer invoice generator
  approval-log.md                  # 1:1 evidence cross-reference for invoices
  clients/
    ezo.yml                        # EZO client profile
    cyara.yml                      # Cyara placeholder
  output/                          # generated HTML + PDFs (gitignored)
  pipeline/                        # automation (below)
    config.py                      # paths + constants + date helpers
    sheets.py                      # Google Sheets read/upsert (EZO OAuth, by reference)
    linear.py                      # Linear 'Client Admin' issue posting (api-toolkit client)
    evidence.py                    # gather a week's evidence from the EZO repo
    llm.py                         # OpenRouter drafting (honest-first), with fallback
    weekly.py                      # weekly tracker update (Friday EOD)
    period_close.py                # invoice generation + Linear ping at period close
```

## The automated pipeline

Two jobs, both run **Friday end of day** (cron below):

- **`weekly.py`** — determines the current milestone week (Mon–Sun), gathers evidence
  from the EZO repo (deliverables/ + meetings/ mtimes, git commits), drafts Focus /
  Deliverables / Results via OpenRouter, **auto-writes the Google Sheet**, and posts a
  Linear `Client Admin` review issue.
- **`period_close.py`** — if the next two-week retainer period has closed, generates
  the $9,000 invoice (PDF) and posts a Linear `Client Admin` issue: *"Invoice NNNN
  ready — review & send."*

Both run under the **EZO venv python** (it has `googleapiclient`, `google-auth`,
`dotenv`, `requests`).

```bash
PY=/Users/brentbartosch/Development/EZO/.venv/bin/python
cd /Users/brentbartosch/Development/Smoothed/smoothops

# preview (no write, no Linear)
$PY invoicing/pipeline/weekly.py --dry-run
$PY invoicing/pipeline/period_close.py --dry-run

# real runs
$PY invoicing/pipeline/weekly.py
$PY invoicing/pipeline/period_close.py
```

### Honest-first drafting

The `llm.py` prompt tells the model to state only what the evidence supports, lead
with real wins, and mark partial/blocked work "in progress" / "carried forward" —
never fabricate completion (e.g., no "pages went live" unless the evidence says so).
If OpenRouter is unreachable, it falls back to a verbatim evidence listing, so the
sheet is still filled with something accurate.

### Credential separation (do not copy secrets)

- **Google** — referenced via `EZO/scripts/google_auth.py` + `EZO/.secrets/*`.
- **Linear** — referenced via `~/Development/api-toolkit/services/linear/api.py`
  (`LINEAR_API_KEY` lives in that repo's `.env`).
- **OpenRouter** — `OPEN_ROUTER_API_KEY` loaded from `EZO/.env` by `llm.py`.

## Manual invoice generation

```bash
python3 invoicing/gen_retainer.py          # writes HTML
node generate-pdf.mjs invoicing/output/<html> invoicing/output/<pdf> --format=letter
```

Naming: `Smoothed_Invoice_{NNNN}_{CLIENT}.pdf`. `NNNN` is sequential across all
clients; invoices 0001–0005 were EZO trial weeks, 0006+ are the Agreement B retainer.

## Remit / ACH (baked into the retainer template)

| Field | Value |
|-------|-------|
| Account name | Smoothed Accounts Receivable |
| Account number | 400114868088 |
| Routing (ACH) | 124303243 |
| Account type | Business checking |

## Cron

Add to `scripts/crontab` (or `crontab -e`), run Friday EOD:

```cron
0 17 * * 5 cd /Users/brentbartosch/Development/Smoothed/smoothops && /Users/brentbartosch/Development/EZO/.venv/bin/python invoicing/pipeline/weekly.py >> /tmp/smoothops-invoicing-weekly.log 2>&1
30 17 * * 5 cd /Users/brentbartosch/Development/Smoothed/smoothops && /Users/brentbartosch/Development/EZO/.venv/bin/python invoicing/pipeline/period_close.py >> /tmp/smoothops-invoicing-period.log 2>&1
```

(Adjust the time/path to taste; `weekly.py` is idempotent — re-running it the same
week overwrites that week's row, it does not duplicate.)

## Sender identity

```
Smoothed LLC
5419 S Sherbourne Dr, Los Angeles, CA 90056
brent@smoothed.io · 310-743-3616
EIN 99-3181387
```
