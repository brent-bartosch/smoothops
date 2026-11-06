# Handoff: Massive / Frontier AI Lab Automation Engagement

**For:** the next agent helping Brent Bartosch with this opportunity
**Status as of Oct 19, 2026:** Brent replied to Dan's outreach; Dan sent the full JD and a role-page link with "next step." Brent has not yet completed the role-page application or had the intro call (unless he tells you otherwise; confirm first).

---

## 1. Who Brent is (relevant context)

- GTM Engineer and AI Systems Architect; runs Smoothed LLC (smoothed.io), an AI-native GTM consulting practice.
- Builds production systems in TypeScript/Python with Claude Code, Supabase, BigQuery, and direct API integrations.
- 7+ years of enterprise SaaS sales (Skai, Conversion Logic, Crealytics), plus 3 years building production AI/GTM systems.
- Has active client engagements; watch for conflicts (IP, outside work, confidentiality).

## 2. The opportunity

- **Recruiter:** Dan Vykhopen, founder of Massive (usemassive.com; outreach sent from danv@pullmassive.com). Brent verified Dan is real.
- **Role:** Senior Business Process Automation Expert (AI Training Project), for an unnamed frontier lab ("yes, that one").
- **Terms:** $300/hr, **W-2 contract** (not 1099), 10–20 hrs/week to start (up to 35), 6 months, remote US, starts immediately.
- **Role page:** https://experts.usemassive.com/prj-a1/senior-business-process-automation-expert (JavaScript-rendered; contents couldn't be read by fetch).
- **Process per JD:** first step is a 30-minute intro call with a real person.

### What the work actually is
1. **Build n8n workflows** for processes the expert has shipped many times (AP, lead routing, ticket triage, claims, document intake). Some from scratch, some fixing existing workflows.
2. **Invent 10+ test cases per workflow:** clean path, edge cases, and at least one that must stop and go to a human.
3. **Deliverables per unit:** workflow file, run logs, one-page plain-language process write-up, and 5–10 end-state assertions per case (what must / must not be true). These are effectively graders for RL environments/evals.
4. **Work with a researcher:** define "excellent automation," dissect AI attempts, review other experts' workflows.

### The researcher's bar (critical)
Every piece of advice is tested against: *"Could I have worked this out myself with an AI model in an afternoon?"* What clears it is hard-won specifics: the platform bug that drops records, the retry that double-pays, the rule the client forgot until month three. **Generic best practices (Git, branches, tests, logs) do NOT clear this bar.** Brent's answers must be concrete production incidents.

## 3. Research findings

- **Massive's origin:** usemassive.com is Dan's AI job-application product ("Tinder for jobs"), reportedly ~$200K/month revenue with a tiny team (Dan, one engineer, a few VAs/ops). "Expert Sourcing for AI" appears to be a new business line. Source: woshipm.com/?p=6418152
- **No public reviews** from experts who've worked through Massive. New, no track record on payment, project continuity, or hours.
- **Not the same company** as joinmassive.com (compute/proxy network); don't confuse them.
- **Replies are automated/templated.** Dan's follow-up arrived ~7 minutes after Brent's email, with generic personalization, a verbatim rate block, and no calendar link despite promising one. Treat the role-page application as the real screen.
- **Market context:** competitors include Mercor, Turing, micro1, Aligned, Outlier/Scale. Mercor's business-ops projects pay ~$50–$100+/hr, so $300/hr is premium. Confirm it's the actual rate, not "up to."
- **Multiple hires:** almost certainly a cohort (JD mentions reviewing "workflows other experts deliver"; spans several process domains).
- **Which lab:** unknown. Default read is OpenAI or Anthropic. The JD lists Google ADK experience as a "strong plus," which hints at Google DeepMind. Ask on the call. (Note: the prior assistant was Claude, made by Anthropic, and disclosed it has no inside knowledge.)
- **Why n8n:** workflows export as JSON (machine-readable, diffable, gradeable), it's self-hostable so the lab can run thousands of sandboxed reproducible instances, runs produce execution logs, and its graph format is a natural target for models to generate/repair. It's not a judgment on Brent's stack. JD says willingness to learn it is enough. Recommend Brent spend an hour in n8n before the call.

## 4. Brent's positioning and thesis

- **Most-built:** the full outbound system (enrichment, scoring, routing, sequencing, sending), dozens of times. Brent rejects "lead routing" alone as too basic; clients hire for the full system. Range spans the funnel: programmatic SEO (top, inbound) to churn-risk prediction (bottom, renewals), with lead gen in the middle.
- **Core thesis:** failure is inherent; success comes from building the structure a seasoned software engineer would (Git, branches, tests before main, docs, logs) so breaks get triaged fast and encoded as permanent fixes. Once one flow is in production, clients want the next; without structure they stack and you drown.
- **Precise AI failure mode (corrected version):** context loss happens at **build time**, not runtime. The database tracks runtime state. Example: session 3 establishes an invariant (every send checks the sends table); session 9, a fresh context, adds a re-engagement sequence with a new send path that skips the check; the model reports "done"; no test enforces the invariant; the regression ships and a prospect gets a duplicate email. (An earlier draft wrongly said "the model loses track of what's been sent"; Brent caught it. Don't repeat that error.)
- **Hub-and-spoke model (keep confidential until under contract):** every engagement takes the same shape. Right column = knowledge hub (product, client, how they use it, use cases). Left column = customer/prospect/ICP. Middle column = stack of owned inbound/outbound channels, each with its own rules. First project is the hub; later projects are spokes.
- **Brent is motivated mainly by the credential** (the lab badge) but must project hunger for the work, not the logo. He knows this; no need to remind him.

## 5. IP concerns (Brent raised these)

Brent worries the lab will extract his workflow/style and productize it. Agreed guidance:
- The general practices aren't his moat; judgment, client implementations, relationships, and delivery are.
- **Read the IP and outside-work clauses** (W-2 makes this more important). Seek a prior-inventions carve-out listing his existing frameworks/tooling. Recommend a lawyer review.
- **Teach principles, not his codebase.** Build fresh examples; never bring client code or data.
- **Hold back the hub-and-spoke detail** until there's a signed contract.
- Walking away is a legitimate outcome.

## 6. The email Brent sent (approximately)

The draft below was the latest version; confirm with Brent what he actually sent. It challenged the "edge cases from repetition" premise, then gave a concrete break:

> Dan, still interested.
>
> I'd push back gently on the premise. Nobody succeeds in this work by listing every edge case up front, because you can't. Production always finds a new one. You succeed by assuming failure and building the structure a seasoned engineer would: tests, branches, logs, and a loop where every break becomes a permanent fix.
>
> For proof: the system I've built most is full outbound, dozens of times. The classic break is a later change quietly undoing an earlier safeguard, like a new send path that skips the duplicate check. The model says it's done. Without that structure, a prospect finds it first.
>
> I've built across the funnel, from programmatic SEO to churn-risk prediction, and that framework is why every build takes the same shape. Happy to walk through it.
>
> Send the JD and your calendar.
>
> Brent

**Important:** the JD's researcher bar explicitly values "what you only learn by building the same thing 100 times." So on the application and call, **don't argue the premise**. Bridge it: "Failure is inherent, so every break I've hit became a permanent rule. Here are the ones that taught me."

## 7. Fit risks

1. JD domains skew finance ops (AP, claims, intake); lead routing is the only GTM one. Position Brent as the strongest in the GTM/outbound slice, not as an AP generalist.
2. JD filters against "strategy decks or team leadership." Lead with hands-on builds, not sales career.
3. Brent doesn't use n8n (fine per JD, but he should get hands-on before the call).

## 8. Next steps for you (the next agent)

1. **Confirm current status** with Brent: what he sent, whether he's started the role-page application, whether a call is booked.
2. **Help draft the role-page application answers** once Brent shares what the form asks. Use concrete incidents.
3. **Mine 3–4 production incident stories** from Brent's outbound builds. Each needs: what broke, how he found it, the rule/fix he encoded. Must pass the "afternoon test." JD-aligned prompts to jog memory:
   - Webhook retries without idempotency (duplicate sends/records)
   - Silent field-mapping failures between systems
   - Rate limits mid-batch
   - Hallucinated data from an extraction/enrichment step
   - Lead-to-account matching failures (subsidiary/alias domains routing an owned account to a new rep)
   - Ownership edge cases (rep OOO, departed, territory change)
   - Deliverability (volume scaled without warmup/caps, burned domains)
   - Human-handoff design: which conditions trigger a hold, who gets it, what they're told
4. **Prep questions for the intro call:**
   - Which lab? Does Massive contract directly with it or through another vendor?
   - Is $300/hr the actual W-2 rate? Are 10–20 hrs/week guaranteed?
   - IP assignment scope, prior-inventions carve-out, outside-work restrictions
   - NDA: can Brent publicly name the lab/engagement afterward? (The credential value depends on this.)
   - Which process domains are open (is there a GTM/lead routing track)?
5. **Optional, high value:** Brent could run a with/without-harness test (fresh model session without his rules files vs. with them, same scoped task, e.g., "add a follow-up send step") and see if the bare model checks for prior sends. That demo is essentially the engagement.

## 9. Working style notes

- Brent thinks out loud via voice transcription; messages may be fragmented. Wait for the full thought.
- He pushes back hard on vague or plausible-sounding-but-wrong sentences. Be precise; don't pad.
- He wants to see drafts on screen to judge them; give full drafts, not descriptions of drafts.
- Keep emails short; screeners skim.
