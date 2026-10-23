# Profile refresh — LinkedIn + smoothed.io vs AI-driven recruiting

**Started:** 2026-10-12 · **Repo:** smoothops · **Branch:** merge/tuning-to-main

## ORIGIN
I'm wondering if it's time to update my website and my LinkedIn. I feel like the industry is changing. People are getting smarter about how to search for go-to-market engineers, and I feel like also people are using more of an agentic approach to screening for candidates.

So I'd first like to do a little research on what have the smart people in recruiting and talent acquisition, how are they using AI with LinkedIn to find candidates? And what can I do in this cat and mouse race to improve visibility? Because how I was told was after Labor Day, there was a big hiring spree and the queries from recruiters has fallen off a cliff.

But here's the thing. I've got two high profile clients now and the work I've been doing has accelerated my expertise and my quality of work for going to that next level of go-to-market engineering. I would say now I am at the frontier level of AI usage.

I think what would help is if you query the EZO folder within the development folder, you're going to see just the level of work we're doing now. I believe that's my latest LinkedIn profile. I haven't changed it since June. We also need to go through the Smooth website and update it. https://smoothed.io/ It now has all the telltale signs that it was AI written. So a lot of my work has improved, my expertise has improved, but my public facing profile is stagnant. [Brent Bartosch Linkedin Profile.pdf]

## NOW
Research is done and delivered: `linkedin-profile/reports/AI recruiter sourcing and visibility.md` (+ PDF), ~3,800 words, 50 citations; source notes in `linkedin-profile/research_notes/AI recruiter sourcing and visibility/` (4 files: recruiter AI tools, candidate visibility, GTM-engineer market, local audit of LinkedIn PDF + EZO/Cyara/smoothops work + smoothed.io). README index updated. Core recommendation: drop the July "RevOps leader @ $250K" plan (that seat contracted 27% in Sept; median is $150K); go with Position C — operator of production AI/agentic GTM systems — spelled in standard filterable titles ("Founder & Principal, GTM Engineering"; OTW = Director of GTM Engineering / Revenue Operations / GTM Systems, FDE). Nothing has been applied to LinkedIn or smoothed.io yet. Blocker before any copy edit: the June 1 PDF headline ("GTM Systems Architect") contradicts the July audit's recorded live headline ("GTM Engineer & Systems Architect") — live profile must be checked.

**DRIFT:** ON TRACK — research phase complete; implementation not started.

## SITE REVIEW (2026-10-14)
Site-rewrite agent died silently after 5 commits (last 14:09 on 10-12); no completion notification ever arrived. Finished by hand in its worktree (`GTM_Services_Site/.claude/worktrees/agent-a1d102768fd149a68`, branch `content/profile-refresh-2026-10`, based on `main` 603ff04 = origin/main, which is what Vercel deploys): journal noindex + sitemap exclusion, /sitemap.xml redirect, FAQPage on About + both new case studies, `published` date on case studies (was `new Date()` every build), fixed a factual error in About (Wagner Bartosch was a QSR products company with a 7-person sales team, not a "performance-marketing shop"). Build passes. Review flags for Brent: (1) both new case studies name OpenRouter/model families/Asana/WordPress/Railway/"three-week trial"/"since July 2026" — pattern-publishable but EZO is identifiable to anyone who knows; publish only after the disclosure agreement with the CMO; (2) mid-market SaaS study names Unilever/Shell/JetBlue/Marriott/Chick-fil-A as customers, YC 2017, $50M raised, "mobile-first CMMS" — that is a named company to any reader; (3) hero paragraph is long for a hero.

## 2026-10-14 afternoon — 27 commits on the branch now
Voice pass (6), subject calls (1), specificity/AI-tell pass on the four older case studies (4), Refactoring UI pass (9; skill installed at ~/.claude/skills/refactoring-ui from github.com/s0xDk/refactoring-ui-skill). Build green. Not merged.
**Facts surfaced that affect LinkedIn too:** (1) Thor Data was never a client — Jan 2026 interview artifact for a US GTM lead role, unpaid, outbound never sent (source: ~/Archived Development/Thordata, thordata_comparison/Interview). Study rewritten honestly; recommend moving it off case studies to the lead-intelligence systems page. (2) "under $0.05 per qualified lead" has no source anywhere in the repos — it is on the homepage, About, the LinkedIn About paste, and the Smoothed bullets. (3) Blingsting "240,000 retailers" vs repo 92,555 / 163,343 / 46,226; "12,000 customers" vs QuickBooks 8,995; Faire still live in Feb 2026 docs. (4) Mid-market study: 6 IDENTIFIABLE markers in the file. Markers in MDX are `{/* VERIFY: */}` / `{/* NUMBER NEEDED: */}` / `{/* IDENTIFIABLE: */}`.

## NEXT
Brent reviews the 7 commits on `content/profile-refresh-2026-10` (run `npx astro dev` in the worktree, or ask for a Vercel preview deploy) and decides on the three flags; then merge to `main` → Vercel deploys. LinkedIn side: About paste + wizard stages 4–9 still open. **Reminder Brent asked for: add the Featured section (smoothed.io + case study + repo) after the site refresh ships** — Linear OPS-72, wizard stage 9.

## OPEN
- Collision resolved: Brent chose merge (v2 structure + report's titles/OTW/voice). `repositioning-2026-10.md` rewritten as canonical v2.1; `research-recruiter-ai-2026-10.md` left as-is.
- Decisions 2026-10-12: Position C; Crealytics → VP of Sales Jul 2022–Feb 2023; no client naming.
- Live profile verified from fresh export: headline is the July "GTM Engineer & Systems Architect"; OTW is ON, recruiters-only, but all five titles are "…Specialist"; top skills Rust/Open Source/GPUI. Brent answers all InMails (auto-disable ruled out).
- Reconcile "1,200+ claims" (v2, content pipeline claim store?) vs "21,000 docs / 3,000 facts" (audit, knowledge library, commit f8deb9a4) before either goes public.
- EZO CMO announced a public "real story" series on the AI-first marketing motion (Oct 9). Need written disclosure agreement with him; anonymization won't hold once the series runs.
- smoothed.io repo path still unconfirmed (audit: last commit 2026-06-03).

## LOG
- 2026-10-12 — thread opened; research dirs created under linkedin-profile/
- 2026-10-12 — 4 research agents + report writer complete; report + PDF delivered; README indexed
- 2026-10-12 — decisions in; live export read; repositioning-2026-10.md rewritten as canonical v2.1; README row updated
- 2026-10-12 — LinkedIn apply wizard written (linkedin-profile/apply-linkedin-2026-10.sh); site-rewrite agent running in worktree on GTM_Services_Site
- 2026-10-12 — wizard crash fixed (unescaped $800K under set -u); resume-on-rerun added; OTW stage rewritten for typeahead-accepted titles; stage 2 reset for redo
- 2026-10-12 — About cleaned (about-2026-10-12-paste.md), numberless headline tails drafted, Linear OPS-72 filed with Featured-section reminder
- 2026-10-12 — banner advice given (brand-text banner over LA stock); no files changed
- 2026-10-12 — LinkedIn banner generated from brand kit (linkedin-profile/banner/, copy in ~/Downloads)
- 2026-10-14 — site agent found dead; finished journal/sitemap/FAQ/published/About-fix by hand; 7 commits on content/profile-refresh-2026-10; build green; not merged
- 2026-10-14 — site voice/posture proposal written (linkedin-profile/site-voice-2026-10.md): practice framing, three-subject pronoun rule; awaiting Brent
- 2026-10-14 — voice pass done: 6 more commits (13 total on content/profile-refresh-2026-10); build green; not merged
- 2026-10-14 — specificity pass + UI pass done (27 commits); Thor Data found to be an interview artifact, not a client; $0.05/lead unsourced; Blingsting counts conflict with repo
- 2026-10-14 — Thor Data removed from site (30 commits); Blingsting big numbers kept; mid-market study de-identified — it is UpKeep, a Mar-2026 speculative build for a Sr Growth Manager process, not a client
