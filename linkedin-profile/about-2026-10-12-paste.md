# About — cleaned version of what Brent pasted 2026-10-12

Paste the block between the rules. ~2,170 chars, under the 2,600 limit.

---

I design and operate production AI systems for B2B SaaS go-to-market teams. The background behind that is seven years carrying enterprise SaaS quota as a Sales Director and VP of Sales, and before it, performance marketing: paid search, SEO, paid social, retail media, analytics. I have owned CAC, LTV and conversion numbers, so the systems I build start from the funnel and the measurement, then the tooling.

What is running today, selected:

• A content pipeline for a multi-product B2B SaaS marketing team. An 11-step, 16-day workflow now runs in five stages: brief, draft, machine QA, one human review, publish. QA is a deterministic rule checker plus an LLM judge; a human clicks before anything publishes. 15+ models routed through one transport, with a test that fails the build if the model map drifts. About 7,000 automated tests.

• A company knowledge library for the same team: 21,000+ documents and 3,000+ verified facts from the help center, website, Drive, ticketing system and YouTube, with a claim checker that returns SUPPORTED / CONTRADICTED / NOT IN LIBRARY and the deciding passage. Every nightly refresh is eval-gated and can roll back. $0.008 median per answered question.

• Model cost work: traced spend to pipeline steps (checking, not writing, was two-thirds of the bill), ran blind, pre-registered side-by-side bake-offs with the win rule committed before any draft, and cut per-page cost roughly 4x where quality held.

• Earlier systems still in use: a 150-mailbox outbound engine (campaign launch 8 hours to 3 minutes), 240,000+ retailers sourced from public data at 72% email discovery, a buying-signal pipeline that turned 910 signals into 332 Tier-1 prospects under $0.05 each, and an attribution audit that found $81K/year of misdirected ad spend.

I design the controls, write the architecture contract, enforce it in CI, and run the agents that write the code. It has not been a straight line; most of the work is scripting, workflows, and changing how people on the team operate.

Best fit: Series A–B or PE-backed B2B SaaS making AI-native GTM a priority, where the person owning revenue systems has to ship them too.

---

## What changed from the pasted version and why

- Paragraph 1 ended mid-sentence ("That means when I build infrastructure, automation, or systems.") and carried the old "two worlds" line. Rewritten to keep the performance-marketing and engineering background you wanted in, without the fragment.
- "I think in terms of funnels, not features" is the "not X, Y" construction the research flags as an AI tell; replaced with the plain claim it was making.
- "What is running today, selected." → "selected:" so the bullets read as the list it introduces.
- Triple blank lines collapsed to one; LinkedIn renders each blank line.
- Sales record kept as one sentence (Sales Director, VP of Sales) with no percentages, matching your call that the numbers read cheap in the headline. If you want the evaluation agent to be able to quote the quota record, the Skai and Crealytics experience entries (wizard stages 1 and 8) are where it belongs anyway.

## Headline — tails without the numbers (all ≤220 chars)

Your current: "Director GTM Engineering & Revenue Operations | Production AI agent systems for B2B SaaS GTM: 15+ models, evals, approval gates, observability, human-approved | ex-enterprise seller, 143% quota, $800K ACV"

1. "Director GTM Engineering & Revenue Operations | Production AI agent systems for B2B SaaS GTM: 15+ models, evals, approval gates, observability, human-approved | Founder, Smoothed · ex-enterprise SaaS sales director"
2. "Director GTM Engineering & Revenue Operations | Production AI agent systems for B2B SaaS GTM: 15+ models, evals, approval gates, observability, human-approved | 7 yrs enterprise SaaS quota before I built the systems"
3. "Director GTM Engineering & Revenue Operations | Production AI agent systems for B2B SaaS GTM: 15+ models, evals, approval gates, observability, human-approved | Founder, Smoothed"

Option 1 recommended: "Founder, Smoothed" is a searchable company string and "sales director" is a standardized title string, so the tail still does retrieval work without a number in it.
