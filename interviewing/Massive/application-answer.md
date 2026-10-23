# Massive — "the workflow you've built most often, how many times, what breaks it"

Paste the text below the rule. Brackets are Brent's to confirm before sending.

---

The system I've built most is full outbound: pull leads from several sources, enrich them, score against the client's ICP, route each one to a sequence, a rep or a hold, send, classify replies, and sync the result into the CRM. Dozens of times since 2023, for B2B SaaS, wholesale retail and residential solar, plus a few hundred campaign-level reconfigurations. It ran at 150+ mailboxes and 20–50 campaigns a week for 18 months. Failure is the normal state of this work; what I have instead of a perfect edge-case list is a rule for every break I've hit. These are the ones that taught me:

1. A failure recorded as done. An enrichment step added a record to its "completed" checkpoint even when the API call failed, to avoid retrying. During an SSL outage, 551 brands were marked complete with zero data and would have been skipped forever. Now "tried and failed" and "done" are different states, and the checkpoint is reconciled against what actually landed.
2. Retrying a write that already succeeded. My client library retried every call on a 429 or 5xx, writes included. A 502 came back after the write had already gone through, and the retry made a second one that nothing downstream knew about. The same bug double-pays an invoice. Writes are now never retried blind; an intent record goes down first and the retry checks it.
3. Silent field mapping between tools. Moving replies from Smartlead into Close, custom fields came back null or under different names, and state codes came in mixed formats. Nothing errored; leads just landed with blanks. Every mapping now has a test on a real export.
4. Output that arrives later and gets lost. Bulk scrape jobs return asynchronously; if the run dies between trigger and fetch, the data is paid for and gone. I write a ledger row before triggering, and every run starts by reconciling unfinished rows.
5. The rule nobody mentioned. Subsequence campaigns had to be excluded from the CRM import, and existing customers and prior repliers had to be suppressed from new sends. Both surfaced after launch. I now ask for suppression and exclusion rules in the first meeting.
6. A later build undoing an earlier safeguard. I build with coding agents, and the context that gets lost is at build time, not run time. One session establishes that every send checks the sends table; a fresh session weeks later adds a re-engagement sequence with a new send path that skips the check, and reports done. Unless a test pins the invariant, a prospect gets the duplicate before I do. Every safeguard I care about is now a test, not a note.

Where a person comes in: I design the hold paths first. A step whose credentials are missing refuses to run rather than act as a human; a contradicted fact holds a page for a reviewer; a send has a kill switch; nothing publishes without a person's click. The AI failures I design review around: invented field values from extraction, retries that loop, and rules applied to the wrong segment.
