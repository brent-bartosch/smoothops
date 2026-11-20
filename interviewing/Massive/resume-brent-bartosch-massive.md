---
title: "Brent Bartosch"
---

**Business process automation builder · Founder & Principal, Smoothed**\
Los Angeles, CA · 310-743-3616 · brent.bartosch@gmail.com · linkedin.com/in/brent-bartosch · github.com/brent-bartosch

## Summary

I build and run production workflow automation for B2B companies across the funnel: programmatic SEO and content at the top, full outbound in the middle, churn-risk prediction at renewal, with document intake, CRM and finance-system sync, and human review designed in from the start. The system I have built most is full outbound (enrichment, scoring, routing, sequencing, sending, CRM sync), dozens of times since 2023, run at 150+ mailboxes and 20–50 campaigns a week. I build in code (Python, TypeScript, Postgres) using coding agents, under test cases and failure paths I write myself, and I am glad to build in n8n. Before this I sold enterprise SaaS for seven years, which is where I learned to ask for the rule the client forgets to mention.

## Selected builds — Smoothed, Dec 2022 – present

**Outbound systems: enrichment, scoring, routing, sending**

- Outbound lead engine: multi-source collection → enrichment → qualification → personalized send → reply classification → CRM status. 150+ mailboxes; campaign launch cut from about 8 hours to 3 minutes; 20–50 campaigns a week; 18+ months in production. (Smartlead, Supabase, Close, HubSpot)
- Smartlead → Close CRM sync: every reply category mapped to a CRM status, subsequence campaigns excluded, field-name and null-field normalization, request timeouts added after imports stalled.
- Buying-signal pipeline: about 1,100 signals a day from Reddit, Hacker News and GitHub; LLM tiering; 36% Tier 1; under $0.05 per qualified lead.
- Wholesale retailer prospecting: 240,000+ retailers sourced from public data at 72% email discovery; checkpoint/resume with reconciliation after an outage marked 551 records "done" with no data.
- Residential-solar lead routing: 148,759 parcels across 12 markets, permit data from 11 jurisdictions, tiered scoring per market, skip-trace, sending with a kill switch and tracked-number attribution; deterministic banned-claims gate on every message; 672 tests.

**Document intake and AI with human review**

- Content workflow for a B2B SaaS marketing team (Jul 2026 – present): an 11-step, 16-day process collapsed to five stages. Rule checker + LLM judge + one human review; nothing publishes without a person's click; about 7,000 automated tests.
- Document intake into a knowledge library: 21,000+ documents from the help center, Drive, ticketing system and video transcripts; secrets redacted at capture; a claim checker returns SUPPORTED / CONTRADICTED / NOT IN LIBRARY with the source passage, and a contradicted fact holds the page for a person.
- Marketplace listing watch: diffs 26 review-site listings against verified facts; goes live only after two consecutive runs with no missed errors and at most 10% false alarms; raises one approval task per change.
- Customer risk prediction for a PE-backed SaaS (Sep 2026 – present): Salesforce, Zendesk and product-usage joins; reasoning may be generated, facts never are; a Day-30 backtest gate before anyone relies on it.

**Finance and system sync**

- QuickBooks Desktop → Postgres customer and invoice sync through Conductor (SOAP → REST), with referential integrity (an invoice only lands against a valid customer), scheduled on GitHub Actions.
- CRM and work-tool integrations: Close (REST + webhooks), Day.ai (OAuth + MCP, three days to production), Twenty (GraphQL), HubSpot, Salesforce, Asana, Slack, Google Workspace.

**Write safety, across every build**

- External writes answered 429 or 5xx are never retried blind: a retry after a 502 once duplicated a write that had already succeeded. Intent records before writes, allowlisted write paths, a write log per run.
- Automations write under a service account with per-step credentials; a step switched on without credentials refuses to start rather than act as a person.

## Earlier

- **VP of Sales, Crealytics** (retail-media SaaS), Jul 2022 – Feb 2023: $1.45M in five months; ran the ABM outbound motion.
- **Sales Director, Skai** (fka Kenshoo), Jun 2020 – Jul 2022: 143% and 111% to quota; $800K ACV close; custom API integrations with the technical team; PII/CCPA/GDPR workflows in enterprise deals.
- **Enterprise AE, Conversion Logic** (attribution), Sep 2017 – Jun 2020: led integration projects with Data Science and Engineering; set data-ingestion standards.

## Tools

Python, TypeScript, SQL/Postgres (Supabase), Railway, Cloudflare Workers, GitHub Actions · Smartlead, Close, HubSpot, Salesforce, Asana, Slack, Google Workspace APIs, QuickBooks (Conductor), Bright Data · OpenRouter (15+ models), Claude Code, MCP · Zapier and Make evaluated; n8n willing.

## Education and certifications

BA, Business Administration, Loyola Marymount University · AWS Certified Cloud Practitioner (2023) · MEDDPICC (2023)
