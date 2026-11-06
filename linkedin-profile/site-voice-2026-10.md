# smoothed.io voice and posture — 2026-10-14 (proposed, awaiting Brent's call)

## The decision

Position Smoothed as a **practice**, not a solo consultant and not an agency: a named principal, a named method, and a bench that scales under the method. Buyers at Series A–B and PE-backed SaaS are not choosing between "one person" and "a team"; they are choosing between "someone accountable who understands my system" and "an account manager." The practice framing keeps the first and makes room to hire.

What scales is not Brent's hands; it is the operating system the work runs under (architecture contract, CI gates, eval sets, machine identity, runbooks, handoff docs). That is the thing to make visible. A forward-deployed engineer or a QA engineer later slots into that system without a word of the site changing.

## Three subjects, three pronouns

The "I, I, I" problem is a subject problem, not a pronoun problem. Give each kind of sentence its proper subject.

| Sentence is about | Subject | Example |
|---|---|---|
| Judgment, commitment, accountability | **I** | "I set the constraint with the team: a faster pipeline that could publish a false claim was not an option." / "I hold the last click." |
| The method, the controls, the infrastructure | **Smoothed** / **the practice** / the system itself | "Every Smoothed engagement runs under an architecture contract enforced in CI." / "The pipeline refuses to start a step whose credentials are missing." |
| The engagement: Brent + the client's team | **we** (and only then) | "We collapsed an 11-step workflow into five stages." / "We found checking, not writing, was two-thirds of the bill." |

Rules:
- "We" is never Smoothed alone. It is always Brent plus the client's people. This is true today (the EZO CMO's own posts say "we"), it reads as collaboration rather than agency, and it stays true when hires join.
- "Smoothed" is the subject when the sentence would still be true if Brent were on vacation.
- "I" is the subject when the sentence is a promise or a judgment call. Keep these; they are the reason someone hires a practice over an agency.
- Never the royal we, never "our team" until there is one, never a Team page with one headshot.

## How scale shows without agency smell

- **Method, not headcount.** "Engagements run under a written architecture contract, a test suite, and an eval gate. The system does not depend on my memory." That is the scale claim.
- **Concurrency as a fact, not a boast.** "Two production engagements running" in the About; the stat strip can carry "2 production engagements · 7 systems in production".
- **Ownership at the end.** "You own the code, the data and the infrastructure" is the anti-agency promise. Keep it everywhere.
- **Staffing as a sentence, not a page.** In "How an engagement works": "When a build needs more hands than mine, I bring in a forward-deployed or QA engineer under the same contract and tests. I stay the principal on the engagement." That is honest today (it is the plan) and it answers "can you scale" without pretending.
- **Principal on every engagement** is the sell. Say it once, plainly, on About and on the contact page.

## What this changes on the branch

- Hero: one sentence of what runs, then the practice line. Draft: "Smoothed is a GTM engineering practice. I design the controls; the systems run under them in production." Cut the four-sentence paragraph.
- About, first paragraph: keep "I'm Brent Bartosch"; add the practice line and the principal promise; move the personal history after "What is running."
- Case studies: engagement narrative in "we" (Brent + their team); controls and infrastructure as the system or Smoothed; constraints and sign-offs as "I".
- Systems pages: subject is the system. "The outbound engine refuses a launch that fails the banned-claims gate." No pronoun needed.
- Stat strip: add "2 production engagements".
- Contact page: "You work with me directly. I am the principal on every engagement."

## Not doing

- No Team page, no "our engineers," no invented bench.
- No "no project is too big." Replace with the specific claim that is true: "no engagement runs unsupervised."
