# How Recruiters Use AI on LinkedIn — Research Brief (2026-10)

> Sources: LinkedIn Engineering blog on Hiring Assistant (fetched 2026-10-12, published 2025-10-21), AIHR "AI Agents for Recruiting" (fetched, published 2026-05-05), DDG search sweep 2026-10-12, plus the two-machines finding already in this folder's README. Labeled inference where I'm reasoning, not quoting.

## The short version

Recruiting has split into two machines, and your profile has to pass both:

1. **Retrieval** — getting INTO the candidate set the recruiter (or their agent) sees
2. **Reasoning** — surviving the LLM evaluation that ranks and annotates you for the recruiter

The cat-and-mouse has shifted: keyword stuffing is mostly dead (semantic search + LLM evaluation see through it), but **evidence density is more valuable than ever**, because the evaluation layer literally quotes your profile back to the recruiter as justification.

## What LinkedIn itself runs now

LinkedIn's **Hiring Assistant** (globally available since late 2025) is a plan-and-execute agent, not a search box. From the engineering post:

- **Sub-agents**: intake (turns a vague req into structured qualifications), sourcing, evaluation, outreach, screening, learning, memory. Each recruiter gets a personalized instance that learns from their shortlists and InMails.
- **Sourcing agent**: takes natural language ("find me a GTM engineer who's shipped production AI agents"), generates multiple queries — classic Boolean AND LLM-generated — runs them at scale, then *iteratively refines the queries based on results*. It also uses Economic Graph signals: talent flows, fast-growing skills, layoff companies, "recently hired" activity.
- **Evaluation agent**: "reads through each candidate's LinkedIn profile, resume, and other relevant data to search for supporting evidence demonstrating how the candidate meets each qualification. It surfaces the evidence it finds to the recruiter." Custom fine-tuned models, evaluates in seconds.
- **"Source while you sleep"**: pipelines refresh daily; new applicants evaluated continuously; outreach and follow-ups drafted/sent agentically with human-in-the-loop on decisions.

**Inference for us:** when the evaluation agent's output is "here's the evidence this candidate meets qualification X," the winning profile bullet is one that *survives being quoted out of context*. "Cut client CAC ~90% by rebuilding the trial-to-revenue motion end to end" is quotable evidence. "I build growth systems" is not.

## The third-party agent layer

AIHR (May 2026): **52% of TA leaders plan to use autonomous AI agents** for sourcing/outreach/screening/scheduling; 13% actively using, 50% exploring. The tools doing this: hireEZ, SeekOut, Gem, Juicebox (PeopleGPT), Beam, Workable, Eightfold, iCIMS Coalesce, Braintrust Nexus, plus Mercor-style AI interview/screening platforms.

What they share:

- **Semantic matching beyond keywords** — AIHR explicitly notes agents "find candidates whose backgrounds don't match keyword searches but align with underlying requirements." Good news for a non-linear background (seller → builder); bad news if your profile is adjective soup.
- **Open-web enrichment** — they pull GitHub, personal sites, conference talks, publications, and attach them to your candidate record. **Your website is now a sourcing surface, not just a brochure.**
- **Always-on outbound** — agents draft and send the InMails. This is part of why raw recruiter query volume can fall while hiring continues: fewer, better-targeted, agent-written touches replace the spray.

## Why inbound fell off a cliff (and why it's not all you)

Two structural things, layered on the post-Labor-Day market:

1. Agent-mediated sourcing means **fewer, sharper queries** — the spray-and-pray InMail era is declining. A recruiter with Hiring Assistant runs 3 refined searches instead of 30 manual ones.
2. The white-collar slowdown is real, but **AI-native GTM roles are the growth exception** — and those searches are evidence-hungry: they look for production systems, not tool familiarity.

**Inference:** passive inbound is structurally weaker now. The counter-move for someone who literally builds outbound engines is obvious: run your own motion against the 20–30 companies you actually want, and let the profile/website do the diligence work when they look you up. Being findable still matters — it's the second click, not the first.

## The visibility playbook (what actually moves the needle)

Ordered by leverage:

1. **Title fields (headline + current title + OTW titles)** — still the heaviest retrieval signals. LinkedIn's own search infrastructure and the agent's generated queries filter on these. The target titles must physically appear.
2. **Evidence-dense experience bullets** — the reasoning layer quotes you. Lead with numbers and shipped systems; mechanism second.
3. **Skills section** — structured data the queries run against. Pin the role-level skills, not the languages.
4. **Open-to-Work settings** — recruiter-only visibility is fine; the title list gates agent filters. (Not in the PDF export — verify in settings.)
5. **External artifacts** — website case studies, GitHub. Agents crawl and attach them. A case study with real numbers is machine-readable proof; a landing page with formulas is noise.
6. **Feed activity — the OTHER machine** (per this folder's README): posting drives inbound DMs and human attention, not search rank. Worth doing for the frontier-AI credibility narrative, but it's a separate machine from search visibility. Don't confuse the two.
7. **Consistency across documents** — the Crealytics title/date mismatch between resume and LinkedIn is exactly the kind of thing an evaluation agent (or a diligent human) flags as a diligence risk. Fix first.

## What does NOT matter (cat-and-mouse myths)

- Keyword-stuffing the About with 40 tool names — semantic search discounts it; evaluation agents read it as noise.
- "Open to Work" green banner paranoia — recruiter-only OTW is invisible to your network and feeds the filters. The banner itself is optional.
- Posting frequency as an SEO substitute — different machine (see #6).
- Endorsement farming — near-zero weight in retrieval or reasoning.

## Bottom line for the repositioning

The July 2026 insight still holds (don't get sorted into the $175–200K IC pool), but the market moved: senior GTM-engineering seats now exist ("Head of GTM Engineering," "GTM Engineering Lead," "AI GTM"), and the searches for them are *smarter* — they screen for production evidence, not Clay-certification badges. Brent's actual record (enterprise revenue + deployed multi-agent systems with QA gates and human-approval hinges) is precisely the evidence those queries are looking for. See `repositioning-2026-10.md` for the applied strategy.
