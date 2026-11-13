# 02 — The case AGAINST leading with the mechanism-teardown angle

**Date:** 2026-11-09. **Role:** advocate against. Judged on the criteria in 00-frame.md.
Tags: [DATA] measured or verifiable, [FIRSTHAND] someone's real experience, [OPINION] commentary or marketing.
"OLD" marks a source older than 18 months (before about May 2025).

## Position in one paragraph

The teardown angle is a good proof format and a poor lead. Leading with it aims Smoothed's scarcest asset (one person's 3–5 posts a week) at the reader who can follow an HTTP request, and that reader is rarely the CMO, CRO or Head of RevOps who signs. The specific reference piece also sits on the frame's second dealbreaker: it explains how to automate a platform against its stated terms. The evidence is partly inferential (see "Weakest point"), but on criteria 1, 2 and 4 it points the same way.

## What the reference article actually is

- [DATA] The post names its readers as people using Expandi, HeyReach, Linked Helper and Dripify, and walks through the Voyager endpoint, `li_at` cookie, CSRF token, and how accounts get restricted (geography jumps, data-centre IPs, 403 cool-downs). It never mentions LinkedIn's terms. Its call to action is "freelance and agency work, specialising in MVPs and AI automations". No logos, testimonials or outcomes. (May 2026) https://simonbalfe.com/blog/connection-request-101/
- [OPINION] That is a builder-to-builder artefact with a services footer. There is no public evidence either way on whether it wins him executive clients. Nobody should cite it as a proven buyer-acquisition model, and I cannot cite it as a proven failure.

## Argument 1 — Buyers pick from people they already know, on proof and outcomes, before they talk to anyone

- [DATA] 6sense 2025 Buyer Experience Report (nearly 4,000 buyers, published Nov 2025): first vendor contact comes about 61% of the way through the process; 94% of buying groups rank their preferred vendors before first contact and buy from that early favourite about 77% of the time; buyers initiate the contact about 80% of the time. https://6sense.com/buyer-experience-report/ and https://www.businesswire.com/news/home/20251112018032/en/ (figures taken from the press release and secondary write-ups, not the full report)
- [DATA] Reddit/SurveyMonkey, 1,202 US decision-makers (fielded Dec 2025–Jan 2026): peer recommendations trusted by 73%, vendor websites 55%, social media 36%. Top obstacles: finding real user testimonials (48%) and wading through vendor-provided information (46%). https://www.surveymonkey.com/newsroom/surveymonkey-and-reddit-the-hidden-b2b-journey-2026/
- [OPINION] Forrester's 2026 State of Business Buying summary is titled "Risk-Averse Buyers Demand Proof, Not Promises" and says buyers validate through peers, experts and analysts. I could only read the headline and a secondary summary; the report is paywalled. https://www.forrester.com/blogs/state-of-business-buying-2026
- [DATA] Edelman–LinkedIn 2025 (1,934 respondents, fielded Mar–Apr 2025): thought leadership does move buyers, and what they credit is content that uncovers a challenge or need they had not recognised (91% of hidden decision-makers, 81% of target decision-makers, per secondary coverage; Edelman's own page returned 403 so I could not check the PDF). https://www.edelman.com/expertise/business-marketing/2025-b2b-thought-leadership-report and https://www.demandgenreport.com/industry-news/news-brief/marketers-need-to-gear-content-to-hidden-b2b-buyers-edelman-linkedin/49901/

What this means for the decision: the job of Smoothed's content is to be the pre-ranked favourite in a CRO's head, with proof attached. "Here is how a connection request works" tells a CRO nothing about their pipeline, CAC or forecast. Smoothed already holds outcome proof in buyer language (8 hours to 3 minutes, CAC down ~90%, $81K of misdirected spend). Leading with mechanism buries the strongest card. Note the honest limit: none of these surveys tested mechanism explainers against outcome content head to head.

## Argument 2 — The format selects for peers, and practitioners say so

- [FIRSTHAND] Jason Liu, an AI consultant who sells to executives: "Technical details are often the lowest pole of value", "clients care much more about business outcomes than technical implementations", LinkedIn works for "corporate/enterprise VP-level content" framed on outcomes, and broad how-to titles reach developers but convert worse. (Apr 2025, OLD by one month) https://jxnl.co/writing/2025/04/04/creating-content-that-converts-my-guide-for-ai-consultants/
- [OPINION] Consultant-marketing guides repeat the same failure mode: writing for peers builds admirers who do not hire, and "how do I do this myself?" content attracts do-it-yourselfers. These are marketing blogs, anecdotal. https://brycewatson.com/research/linkedin-for-consultants/ and https://567-labs.github.io/consulting/guide/06-owning-distribution
- [DATA/OPINION] The label is diluted. One trade blog reports GTM Engineer postings up 5,205% from early 2024 to early 2026, with about 45% of self-described GTM engineers working only in no-code tools; the figure is not clearly sourced in the article (Mar 2026). https://gtmepulse-com.pages.dev/blog/title-dilution/ A practitioner newsletter argues the title covers three different jobs and that companies cannot name which problem they have (Aug 2026). https://gtm-engineer.beehiiv.com/p/nobody-knows-what-gtm-engineering-problem-they-have
- [OPINION] On criterion 3, teardowns are the house style of that crowded field. Balfe is a working software engineer; competing on depth of technical explanation puts a sales-leader principal on the other side's home ground and hides the one thing few "GTM engineers" have: seven years carrying quota and running sales teams.

Counter-evidence I found and will not hide: [FIRSTHAND] ColdIQ's founder says posting about GTM tools on LinkedIn built the following that produced his first client and, later, an agency. https://cms.coldiq.com/blog/the-anatomy-of-a-7m-arr-lead-gen-agency That is a founder's own account, at tool-review level rather than HTTP level, now run by 20+ people posting 150+ times a month. It shows technical content can produce clients; it does not show it does so for a one-person practice selling multi-month engagements to CMOs and CROs.

## Argument 3 — The reference topic is a risk signal for exactly the buyers in the frame

- [DATA] LinkedIn's help page: "we don't permit the use of any third party software" that scrapes or automates activity; users "risk having their accounts restricted or shut down". https://www.linkedin.com/help/linkedin/answer/a1341387
- [DATA] Enforcement is real: Apollo.io and Seamless.ai company pages disappeared from LinkedIn on 6 March 2025 (LinkedIn gave no public reason; Apollo's page was later restored). (May 2025, borderline OLD) https://martech.org/a-pair-of-lead-gen-providers-have-disappeared-from-linkedin/ Proxycurl shut down after a LinkedIn suit; a consent judgment was entered against ProAPIs in September 2026. https://www.socialmediatoday.com/news/linkedin-wins-legal-case-data-scrapers-proxycurl/756101/ and https://digitalpolicyalert.org/event/43954-us-district-court-issued-final-judgment-in-linkedin-v-proapis-data-scraping-lawsuit
- [OPINION] I found no source on how PE operating partners screen outbound vendors for platform-terms exposure. The inference is mine: a compliance-aware buyer who reads a cookie-and-CSRF walkthrough on a vendor's site learns that the vendor is comfortable operating there. That is the frame's dealbreaker 2, and it attaches to the reference example specifically, not to every possible teardown (a teardown of Smoothed's own signals pipeline carries none of it).

## Positioning authorities

I searched for direct guidance from Baker, Enns, Dunford and Stark on how-to versus insight content and found nothing quotable beyond Enns's line that people "come for the content" but "hire you for the ideology" (undated podcast summary). I am not attributing a position to them. https://twobobs.squarespace.com/podcast/a-ten-year-retrospective-on-the-manifesto

## Best alternative found

**Option C, with one change: tear down the buyer's problem, not the platform's plumbing.** Lead every piece with a buyer-language claim or diagnosis ("where $81K a year of ad spend was leaking, and how we found it"; "why launch took 8 hours and what took it to 3 minutes"). Put the mechanism underneath as show-the-work, drawn from systems Smoothed built and governs. This keeps the genuine strength of the Balfe format (plain-English explanation that proves the author actually does the work) and matches the Edelman finding that buyers reward content that surfaces a problem they had not seen. It also puts the sales-leadership background in the headline, where it differentiates.

Option D (split channels) is weaker for one person: it doubles the content load and still spends half the output on people who cannot sign.

## Ranked: the three strongest arguments

1. **Buyer selection happens before contact and runs on proof and peers** (6sense, SurveyMonkey/Reddit). The lead message must be outcome and proof; mechanism cannot carry that job.
2. **The reference topic trips a stated dealbreaker.** LinkedIn's terms and enforcement record are verifiable; the article is a how-to for circumventing them.
3. **Audience selection and differentiation.** Firsthand consultant testimony and the dilution of the label say teardowns earn peer attention in a field where Smoothed's edge is not technical depth.

## Single weakest point in this case

There is no measured data showing that mechanism-level explainers fail to convert marketing, sales or RevOps executives. Argument 2 rests on one firsthand account, anecdotal marketing blogs and inference from general buyer surveys, and the one concrete counterexample I found (ColdIQ) cuts the other way. Many Heads of RevOps are semi-technical and may well read teardowns. If the other side produces named practitioners who won executive buyers this way, Argument 2 weakens considerably; Arguments 1 and 3 would still argue for mechanism as proof beneath a buyer-language lead, not as the lead itself.
