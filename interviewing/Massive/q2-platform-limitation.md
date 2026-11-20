# Massive role page — Q2 (2026-10-20)

> Pick the automation platform or framework you have used most. Describe one specific limitation, bug, or failure you hit again and again, and how you worked around it.

---

Code: Python and TypeScript on Supabase/Postgres, built with Claude Code and run on Railway and GitHub Actions. I moved off Make-style canvases early because a 40-step scenario couldn't be diffed, tested, or handed to another person; in code every workflow has a repo, tests, and a README.

The failure I hit again and again: async jobs from a third-party data API getting lost between "trigger" and "fetch." Bright Data, which I use for scraping, works like many enrichment and document APIs. You submit a job, get a snapshot ID, and come back later for the results. I hit the same family of bugs in five separate builds between May and August 2026:

- The run died after triggering but before fetching. The job was paid for, the data was sitting on their side, and nothing on mine remembered it existed.
- A poller treated "still running" and "404, never existed" the same as "finished, empty," so real data got recorded as no data.
- A retried trigger launched the same job twice, costing double and producing duplicate rows downstream.
- The API key's environment-variable name drifted between projects, so a run started, failed authentication on every call, and looked like an empty day.

The fix I now build first, before the scraping logic: a ledger table. A row is written before the job is triggered (job key, inputs, status "pending"), so a lost result is impossible. Every run starts by reconciling unfinished rows: adopt orphans, fetch what's ready, mark what failed as terminally failed instead of silently retrying. The job key is unique, so a retried trigger finds the existing row instead of launching a second job. Polling only accepts "ready" as done; anything else stays open. An auth or quota rejection aborts the whole run loudly rather than recording zeros.

The same shape exists in n8n: a Wait or webhook-resume step holding an external job. If that execution is lost, nothing outside it remembers the job. I'd carry the same ledger into an n8n build as a Postgres or Data Table step before the trigger node.
