# Background — Brent Bartosch (context file for agents)

**Written:** 2026-10-14 · **User layer** (never auto-updated; see `DATA_CONTRACT.md`) · Owner: Brent

Read this before drafting anything that describes Brent: job applications, vetting forms, expert-network intake, bios, proposals, LinkedIn/site copy. `cv.md` (April 2026) and `modes/_profile.md` predate the July–October 2026 client work and understate it; this file is the current picture. Canonical public-facing copy lives in `linkedin-profile/repositioning-2026-10.md` (v2.1) and `linkedin-profile/about-2026-10-12-paste.md`. Evidence paths for every claim below are in `linkedin-profile/research_notes/AI recruiter sourcing and visibility/local_profile_audit.md` §D.

## Identity, one paragraph

Founder and principal of Smoothed (smoothed.io), a one-principal GTM engineering practice in Los Angeles, running since Dec 2022. Designs, governs and operates production AI/agentic systems for B2B SaaS go-to-market teams. Not a software engineer by title: the code is written with agent tooling (Claude Code, Zed, several parallel sessions) under CI-enforced architecture contracts, test suites and eval gates that Brent writes and owns. Before Smoothed: seven years of enterprise SaaS quota (Sales Director at Skai, VP of Sales at Crealytics, Enterprise AE at Conversion Logic), and before that performance marketing and a 7-person sales team at a family QSR-products company (Wagner Bartosch). BA Business Administration, Loyola Marymount. AWS Cloud Practitioner (2023), MEDDPICC Masterclass (2023), one patent ("Advertising systems and methods").

## Honesty rules (apply to every sentence written about Brent)

- "Designs, governs, operates" production AI systems. Never "staff engineer", never "wrote 171K lines by hand".
- Every claim carries a number, a named mechanism, a date, or what happens when it fails.
- First person, one voice. No AI-tell constructions ("not X — Y", staccato triads, aphorism closers, "two worlds", "let's talk").
- No current client is named. Thor Data and Blingsting are already public on smoothed.io and may be named.

## Anonymization map (use the right-hand column in anything external)

| Real | Say |
|---|---|
| EZO (7vals; EZOfficeInventory, AssetSonar, EZRentOut, EZO EAM) | a multi-product B2B asset-management SaaS marketing team |
| Cyara (K1-backed, ~$80M ARR) | a PE-backed CX-assurance SaaS |
| Sunkco Solar (Marco) | a solar-permitting / residential-solar data company |
| Blithe Defense | a defense-contracting prospect |
| GovSignals | a FedRAMP-authorized AI platform (DoD/GovTech) — already described this way in cv.md |
| Client staff names, contract values, OpenRouter spend totals | never |

Open risk: EZO's CMO announced (Oct 9, 2026) a public series on their AI-first marketing motion. Once it runs, the anonymization above is trivially linkable. Written disclosure agreement with him is pending (see thread `2026-10-12-profile-refresh.md`, Linear OPS-72).

## Career timeline

| Dates | Role | Facts that may be quoted |
|---|---|---|
| Dec 2022 – present | Founder & Principal, Smoothed | see "What is running" |
| Jul 2022 – Feb 2023 | VP of Sales, Crealytics (retail-media SaaS) | $1.45M revenue in 5 months; ABM outbound motion, reply rate +157%; hired/onboarded a BDR. Decision 2026-10-12: title is VP of Sales (LinkedIn had Enterprise AE, Jul–Dec 2022; being corrected). |
| Jun 2020 – Jul 2022 | Sales Director, Skai (fka Kenshoo) | 143% and 111% to quota; $800K ACV HBO Max close, largest app sale in company history; PII/CCPA/GDPR compliance workflows in enterprise deals; coached SDRs through C-suite cycles |
| Sep 2017 – Jun 2020 | Enterprise AE, Conversion Logic (multi-touch attribution) | Led application-integration projects with Data Science/Engineering; set data-ingestion integration standards |
| 2010 – 2018 (overlapping) | Wagner Bartosch (QSR products; 7-person sales team), performance marketing | Team-leadership record; paid search, SEO, paid social, retail media, analytics; owned CAC/LTV/conversion numbers |

## What is running (as of 2026-10-14)

**Engagement 1 — multi-product B2B SaaS marketing team (since Jul 20, 2026; began as a 3-week trial; ~1,600 commits in 90 days; active daily).**
- Content pipeline: an 11-step, 16-day workflow collapsed to five stages (brief → draft → machine QA → one human review → publish). QA = deterministic SOP-derived rule checker + LLM judge (5 dimensions, accuracy floor) + human reviewer. FixPass find→fix→verify with journaled patches; eval: catch 100% / fix 86% / unjustified fixes 0%. Nothing publishes without a human click.
- Scale: ~369 pipeline modules + 288 operator scripts, Python stdlib-first, ~171K lines, ~458 test files / ~6,900–7,230 tests green. TDD and fail-loud are house rules.
- Multi-model ops: every LLM call through one OpenRouter transport; 15+ models routed by task (GPT-5.2, Claude Sonnet 4.6/5 and Opus 5.5, Gemini 3.1 Pro, GLM 5.2/5.3, DeepSeek V4 Pro, Qwen3 Max Thinking, Kimi K3/K2.6, Perplexity Sonar Pro, Qwen3 Embedding 8B). `tests/test_model_map.py` fails the build if a model id in code is missing from the model-map doc. Forbidden imports in CI: `pipeline/* → anthropic, openai, google.generativeai`.
- Cost engineering: traced ~$971 of OpenRouter spend to pipeline steps (64% Anthropic; checking, not writing, was two-thirds of the bill); showed a $181 blog check costs ~$21 on GLM 5.3; blind, pre-registered bake-offs (win rule committed before any draft, two judges, both orders; GLM $0.26–0.32/page vs Opus $1.18+, reviewer preferred Opus 2 of 3); ~4x per-page cost reduction where quality held. Model judges advisory; humans decide the switch.
- Knowledge library (RAG): 21,000+ documents, 3,000+ verified facts from help center, website, What's New, Google Drive, Redmine (~8,986 records, redacted), YouTube transcripts. SQLite FTS5 + vector index, reciprocal rank fusion, pick-then-confirm across model families with span check, detect-secrets redaction at capture, public/internal audience labels, eval-gated nightly refresh with rollback. $0.008 median per answered question. Claim checker returns SUPPORTED / CONTRADICTED / NOT IN LIBRARY with the deciding passage; every fact check routes through it.
- Observability: Railway runner; Healthchecks pings on every wrapper; Asana-based pager (once-per-situation, canary); morning systems report; run journal + generated status board; secrets guard that cannot be skipped; deploy script pauses checks → deploys → resumes → smoke-tests.
- Machine identity and access: a service account ("the machine") with per-step write credentials; read as Brent, write as the machine; each step is a Railway switch deploys cannot flip; a step that is on without credentials refuses to start rather than post as a human; Google OAuth narrowed to `drive.readonly` at mint; Slack DM writer with one 429 rule; Asana writes allowlisted by shape with a `writes.log` and a run lock (Marketing Calendar, Oct 13); people-guard and quiet rules on task sync.
- Architecture governance in CI: ~230KB ARCHITECTURE.md with 10+ dated amendments, per-module line budgets, acyclic dependency edges, `check_import_boundaries.py`, `check_file_size.sh`, `check_no_secrets.sh`, pre-push hook that refuses a red suite.
- Tier-gated planning with cross-LLM review: design doc → risk register → ADR → architecture contract → implementation plan, each reviewed by a different model provider until "no blockers" (e.g., marketplace watch 22-risk register, 3 rounds; machine identity 4 ADR rounds; Marketing Calendar 5 review rounds, Oct 13).
- Integrations in production: Asana (task sync, handback, 137-task machine tracker), Google Drive/Docs/Sheets, Slack (Cloudflare Worker + DM writer), WordPress staging (multi-blog CPT registry), Elementor, Figma, Redmine, HubSpot, SEMrush, GSC/GA4, Bright Data, Serper. Marketplace listing watch: 26 G2/Capterra/TrustRadius listings read for $0.89/run, gated on "no missed errors, ≤10% false alarms on two consecutive runs". Team docs site on Cloudflare Pages behind Cloudflare Access, CSP `script-src 'self'`. Runs the client PMMs' own Claude skills (74K-char brief skill, copy-review skill) inside the machine.
- Latest (Oct 13): Marketing Calendar — one Asana project per market moment, seeded from the team's export, weekly gap report, 104 tests, Tier 2 spec/risk register/ADR, built not yet run.

**Engagement 2 — PE-backed CX-assurance SaaS (since Sep 2026; Phase 1 invoiced, Phase 2 scoped).**
- Customer risk prediction: "risk intelligence, not a health score"; reasoning may be generated, facts never are; Day-30 backtest decision gate against the client's existing health score; sentiment held out as comparator; output = score + bullets.
- Data: Salesforce (Case Safe ID join), Zendesk (~1 GB JSON), Sigma/Pulse 28-day telemetry, tenant→ID crosswalk. Synthetic "book" generator (null/weak/medium/strong worlds, bootstrap power tables, ~$50/world on GLM-5.3). `uv`-managed Python with the same file-size/import/secret guards. No real customer data enters the repo; third-party model use restricted to no-training routes per the ICA.

**Earlier systems still in production or cited (client-reported numbers):**
- Autonomous outbound engine, 150+ mailboxes on Smartlead: launch 8 hours → 3 minutes; CAC ↓~90%; 5x volume; 18+ months. Campaign ops 5–10 → 20–50 campaigns/week; manual ops 40+ → <10 hrs/week.
- Signals pipeline: ~1,100 signals/day (Reddit/HN/Twitter/GitHub), 36% Tier 1, <$0.05/qualified lead; 910 signals → 332 Tier-1 prospects.
- 240,000+ retailers sourced from public data (20x the client's customer base) at 72% email discovery (Faire / Thor Data work).
- $81K/year misdirected Google Ads spend found for a FedRAMP AI platform (CPA $160 → $909 traced to a 217-change agency restructure); GA4 + Ads + GSC → BigQuery/Looker executive dashboard.
- Residential-solar lead-gen (Aug 2026): 148,759 parcels, 12 markets, permit scrapers across 11 jurisdictions (~28K permits), Google Solar roof-fit, BatchData skip-trace, Smartlead + Twilio attribution, 14-cell persona copy matrix with a deterministic banned-claims gate, 672 tests.
- CRM integrations built API-direct: HubSpot, Salesforce, Close (REST + webhooks), Day.ai (OAuth 2.0 + MCP, 3 days to production), Twenty (GraphQL), QuickBooks Desktop (SOAP→REST via Conductor). No Zapier/Make/iPaaS by policy.
- Internal: api-toolkit (~500–1,000 tokens/service vs ~90K for MCP; 34+ methods with rate limiting/backoff); Overwatch commitment-auditor agent (Node on Railway, reads session transcripts + Granola notes, reconciles against git and Linear, OAuth app identity so it never posts as Brent); smoothops LinkedIn jobs scanner (Bright Data, reconcile-first snapshot ledger, Railway cron, open agent-skill standard, 16-mode skill router).
- Pre-Smoothed PE research (Aug 2026): SoCal B2B SaaS PE-firm map in `private-equity/`.

## Platforms touched in the last 3 years (for intake forms)

Used in production / integrated: HubSpot, Salesforce (API + data joins), Asana, Slack, Google Workspace APIs, WordPress, Zendesk (data), Sigma, Smartlead, Close, Day.ai, Twenty, QuickBooks Desktop (Conductor), Linear, Supabase/Postgres, BigQuery, Railway, Vercel, Cloudflare (Workers/Pages/Access), Bright Data, Serper, SEMrush, GA4/GSC/Google Ads, Twilio, BatchData, OpenRouter, Anthropic (Claude API + Claude Code), OpenAI, Google Gemini, Zhipu GLM, DeepSeek, Qwen, Moonshot Kimi, Perplexity, MCP.
Evaluated and rejected: Zapier, Make (middleware policy). Clay: appears in the old LinkedIn headline; confirm with Brent before claiming hands-on use.
Not used: Salesforce Agentforce, Microsoft Dynamics 365, Zoho CRM, Gong. Say so plainly on forms.

## Architecture pattern language (most quotable, non-confidential)

Independent quality gate · confidence scoring at every AI stage · deterministic scaffolding around the LLM · calibrate before you automate · failure is a designed state · pre-registered blind evals · fail-loud, never silent degradation · model map pinned by a test · machine identity separate from human identity · nothing posts outward without a human's finger on it · architecture contract enforced in CI, not convention.

## Positioning and targets (decided 2026-10-12)

Position C: operator of production AI/agentic GTM systems, expressed in filterable titles (Director of GTM Engineering / Revenue Operations; Founder, Smoothed). Open-to-Work targets: Director/Senior Director/Head of Revenue Operations, Forward Deployed Engineer, GTM Engineer. Best fit: Series A–B or PE-backed B2B SaaS making AI-native GTM a priority, where the person owning revenue systems has to ship them too. Not pursuing: bare "GTM Engineer" IC seats ($135–150K band), pure SWE reqs, RevOps-leader-at-$250K framing (seats contracted 27% in Sept 2026).

## Operating style (how Brent works, for agents)

Runs 3–4 agent threads at once and reads them out of order; wants one orientation line and one complete close. Challenges to his thinking are welcome. YAGNI. Linear issues are promises to named people; everything smaller is a checklist bullet. Tier gate before any build (real users / real data or paid APIs / autonomous consequential actions). Answers every recruiter InMail. IDE is Zed.
