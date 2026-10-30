import sys

sys.path.insert(0, "/Users/brentbartosch/Development/api-toolkit")
from services.linear.api import LinearAPI  # noqa: E402

api = LinearAPI()

DESC = """Public-profile refresh so recruiter agents (LinkedIn Hiring Assistant 2, Juicebox, hireEZ) and buyers find current, quotable evidence. Strategy: `smoothops/linkedin-profile/repositioning-2026-10.md` (v2.1). Research: `smoothops/linkedin-profile/reports/AI recruiter sourcing and visibility.md`. Apply wizard: `smoothops/linkedin-profile/apply-linkedin-2026-10.sh`.

## LinkedIn
- [x] Crealytics → VP of Sales, Jul 2022–Feb 2023
- [x] Open to Work: five "Specialist" titles replaced; remote = United States; actively looking
- [x] Headline (Director GTM Engineering & Revenue Operations | …) — tail without numbers still to pick
- [ ] About — paste cleaned version from `linkedin-profile/about-2026-10-12-paste.md`
- [ ] Smoothed title → Founder & Principal, GTM Engineering
- [ ] Skills: unpin Rust / Open Source / GPUI; pin Revenue Operations, GTM Strategy, AI
- [ ] Smoothed description — five anonymized bullets
- [ ] Skai description — add 143%/111%, $800K HBO Max
- [ ] Verify identity
- [ ] **Add Featured section: smoothed.io + best case study + public repo** (Brent asked to be reminded; do after the site refresh ships)
- [ ] Re-export profile PDF to ~/Downloads as the new baseline

## smoothed.io (branch `content/profile-refresh-2026-10` in GTM_Services_Site)
- [ ] Review agent commits: About-as-person + Person/ProfilePage JSON-LD, server-rendered stats, hero, two anonymized case studies, voice pass, journal noindex, sitemap/FAQ hygiene
- [ ] Decide on the thinly anonymized mid-market SaaS case study
- [ ] Merge + deploy

## Disclosure
- [ ] Written agreement with the EZO CMO on what Brent may say publicly before his "real story" series runs; ask whether Brent can be credited as the builder
"""

issue = api.create_issue(
    team="OPS",
    title="Public profile refresh: LinkedIn + smoothed.io for agentic recruiter search",
    description=DESC,
    priority=2,
    project="Personal Brand",
    state="In Progress",
)
print(issue.get("identifier"), issue.get("url"))
