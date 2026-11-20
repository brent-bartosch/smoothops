# Massive intro call — prep (2026-10-22)

## Your 30-second opener
I run Smoothed, a GTM engineering practice. The system I've built most is full outbound: enrichment, scoring, routing, sending, reply handling, CRM sync, dozens of times since 2023. I build in code with coding agents, under tests I write, and I design the hold-for-a-human paths first. Before that, seven years selling enterprise SaaS, which is where I learned to ask for the rule the client forgets to mention.

## Ask first (decides whether this is worth it)
1. When it's done, can I say publicly that I worked with the lab, and name it?
2. Which lab, and does Massive contract with it directly?
3. Is $300/hr the W-2 rate, not "up to"? Are 10–20 hrs/week committed? How often is payroll?
4. Is there a GTM / lead-routing track, or is it mostly AP, claims, and intake?
5. IP: what do I assign? I want a prior-inventions carve-out for my existing frameworks and tooling. Any outside-work restriction? (Send me the agreement before I sign.)
6. How many experts in the cohort, and who is the researcher?

## Stories (say the number, the break, the rule)
- **551 records marked done with no data.** Enrichment checkpoint recorded API failures as "completed" to avoid retries; an SSL outage skipped 551 brands forever. Rule: "tried and failed" ≠ "done"; reconcile against rows that landed.
- **Silent field mapping, Smartlead → Close (Feb 2026).** Null custom fields, names that varied by campaign, mixed state codes. No errors, just blanks. Rule: every mapping tested on a real export; subsequence campaigns excluded.
- **Async jobs lost between trigger and fetch (5 builds, May–Aug 2026).** Paid for, never fetched; 404 read as "empty"; retried trigger doubled the job; API-key name drift made a dead run look like a quiet day. Rule: ledger row before the trigger, reconcile first, unique job key, only "ready" counts as done, auth failure aborts loudly.
- **Retried write after a 502 (Sep 2026).** The write had already landed; the retry made a second one nothing downstream knew about. Same bug double-pays an invoice. Rule: never blind-retry a write; intent record first.
- **Solar routing (Jul–Aug 2026).** 11 permit portals, each different; rank within market, not across; banned-claims gate, test-send path, kill switch.

## Where AI fails inside these processes (your thesis)
- Context loss happens at build time, not run time. A later session adds a new send path that skips the duplicate check and reports "done." Only a test pinning the invariant catches it. (Use as "the failure I design against" unless it really happened.)
- Extraction invents values (vendor IDs, field values) → never trust an extracted ID that isn't matched to a record that exists.
- Agents loop on retries → cap retries; terminal "failed" state.
- Rules applied to the wrong segment/entity → the rule carries its scope as data, and a test per scope.

## If they hand you the JD's AP scenario live
Vendor changed bank details 3 days before the invoice; US + EU entities.
- Hold: bank details changed within N days (e.g. 30) of a payment, or changed via email rather than the vendor portal.
- Record: the reason code, old vs new details, who changed them and when.
- Route: the AP lead for that entity (not a global queue); a backup approver if they're out.
- Instruction: call the vendor on the number already on file, never the one in the change request; release only after the call is logged.
- End-state assertions: no payment sent; invoice status "held"; reason recorded; one task to the right person; no duplicate task on re-run; the EU entity's threshold and currency used, not the US one.

## n8n stance
Haven't built in it much; spent time with it before the call [only say this if you did]. You can see why they chose it: JSON export you can diff and grade, self-hostable sandboxes, execution logs. Your patterns carry over: a ledger step (Postgres / Data Table) before an external trigger, error workflows that fail loud, idempotency keys on writes.

## Don't
- Don't claim AP/invoice work. You have a QuickBooks customer + invoice sync, nothing more.
- Don't argue the "built it 100 times" premise. Bridge: failure is normal, so every break became a permanent rule.
- Don't knock n8n or no-code. One line on why you work in code, if asked.
- Don't share hub-and-spoke detail or name a client (EZO, Cyara, Sunko, Blithe).
- Don't lead with the sales career; the JD screens against "strategy decks or team leadership."
- Don't commit hours before you've seen the IP and outside-work terms.

## Close
"What does the first unit look like, and what would make me a fit for the GTM slice?" Ask for the agreement in writing and the next step with a date.
