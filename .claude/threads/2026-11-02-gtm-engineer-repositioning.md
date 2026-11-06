# GTM engineer title flood — repositioning for clients + inbound

**Started:** 2026-11-02 · **Repo:** smoothops · **Branch:** merge/tuning-to-main

## ORIGIN
We redid my LinkedIn to be more director level of go-to-market engineering. Now I need to run some research because it feels like the industry is being flooded by people claiming to be go-to-market engineers, and I need to be More strategic and get more clients.  Also, basically every day I get one or two people that want to connect with me on LinkedIn, and their title is just go-to-market engineer.  I need to figure out how I can reposition myself because the changes we made to my LinkedIn, all the job op people that would tap my shoulder, all the inbound is basically gone when I removed myself from go to market engineer.

## NOW
Research delivered: `linkedin-profile/reports/GTM engineer flood and repositioning.md` (+ PDF), ~5,000 words, 4 researcher notes in `linkedin-profile/research_notes/GTM engineer flood and repositioning/`. Verdict: the Oct-12 edit was right about the problem (bare title is commodity) and wrong about the mechanism — it deleted the literal "GTM Engineer" string from all three Recruiter-matched fields (position title, headline, OTW) and swapped in "GTM Engineering", which is not stemmed; "Director"/"Founder & Principal" at a one-person firm also likely re-buckets inferred seniority into Director/Owner. Demand has not collapsed (~250 roles/30 days, Oct 2026). Report prescribes a hybrid configuration (`Principal GTM Engineer` title, bigram-first headline, OTW = bare noun + step-ups) and a separate client-acquisition track (named method, two anonymized before/after case studies, 20–30 target accounts, expert price band). README indexed. Nothing applied to LinkedIn.

**DRIFT:** ON TRACK

## NEXT
Brent decides whether to apply the hybrid configuration (report §3 table); if yes, update `apply-linkedin-2026-10.sh` stages 2–4 to the new strings and run it in one sitting, then freeze for 6 weeks.

## OPEN
- Is "GTM Engineer" an accepted OTW typeahead string today? Must be checked live; fallback "Go-to-Market Engineer".
- Seniority-bucket inference (Director/Owner vs Senior) is unverified — ask a recruiter contact to run "GTM Engineer" + Seniority filter against the profile.
- Site branch `content/profile-refresh-2026-10` (30 commits) still unmerged; smoothed.io/about still shows placeholder — blocks the client-acquisition track's case-study step.

## LOG
- 2026-11-02 — thread opened; 4 researchers + report writer run; report + PDF delivered; README indexed; v2.1 §3–4 reversed by the new report
