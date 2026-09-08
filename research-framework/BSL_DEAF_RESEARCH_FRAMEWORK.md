# BSL & Deaf/DeafBlind UK Research Framework

**Document type:** Methodology & source map (living document)
**Parent project:** GeometricMind
**Related sub-project:** Deaf Network Health Group
**Status:** All 16 domains have a first-pass briefing (Domain 16, end-of-life & palliative care, added 8 September 2026 from a four-prompt Grok research batch); direct primary-source verification is now underway (see `VERIFICATION_STATUS.md` Section 19 for the first completed pass, covering AIS/NHS commissioning/SWL-specific GP data/DeafBlind population figures — closing gaps identified against `prompts/supergrok-prompt-deaf-health-access.md`)
**Last updated:** 8 September 2026 (Domain 1 / NHS interpreter provision extended same day with prompts 34-37 findings on AIS legal enforcement, flag/booking-failure data, comparative practice and lived experience — see that domain file's new dated subsection; one contested claim on CQC's assurance role logged, pending re-read)

---

## 1. Purpose

This document defines a repeatable research methodology for building an accurate, sourced evidence base across the full landscape that shapes Deaf and DeafBlind BSL users' lives in the UK — health, welfare, employment, education, law, and public spending. It is the framework other domain briefings (starting with NHS interpreter provision) plug into.

**What this is:** a structured way to identify primary sources, verify facts, track FOI targets, and flag contested or stale figures, per domain — extending the accuracy-first, verify-before-canonising approach already used on the stakeholder matrix (v7→v10) and FOI tracker.

**What this is not:** an autonomous, continuously-running data collection system. Every domain briefing below is produced through live, sourced research in conversation, then reviewed before being treated as source of truth. There is no persistent background scraping — each briefing has a "last verified" date and a re-check cadence, the same discipline already applied to the stakeholder matrix's organisational status flags.

---

## 2. Domain Map

Sixteen domains, grouped into five clusters. Each will eventually get its own briefing document (`BSL_DOMAIN_<name>.md`) following the template in Section 4.

### Cluster A — Health & Communication Access
| # | Domain | Status |
|---|--------|--------|
| 1 | **NHS interpreter provision & BSL health access** | 🟢 In progress |
| 2 | Mental health services & Deaf/DeafBlind access (incl. BSMHD) | 🟢 In progress |
| 3 | DeafBlind-specific provision (guide-communicators, intervenors) | 🟢 In progress |
| 14 | Devices & technology, including AI (hearing aids, cochlear implants, AI sign-language translation, assistive/alerting tech) | 🟢 In progress |
| 16 | End-of-life & palliative care (BSL and DeafBlind access to hospice/last-days care; DWP Special Rules for End of Life) | 🟢 In progress |

### Cluster B — Welfare, Benefits & Employment
| # | Domain | Status |
|---|--------|--------|
| 4 | DWP: PIP & DLA (assessment, award rates, appeals, Deaf-specific issues) | 🟢 In progress |
| 5 | Access to Work (funding caps, delays, interpreter budget, employer awareness) | 🟢 In progress |
| 6 | Neurodivergence overlap (DeafDisabled, Deaf+ dual/multiple needs) | 🟢 In progress |

### Cluster C — Law, Rights & Governance
| # | Domain | Status |
|---|--------|--------|
| 7 | Legislation (BSL Act 2022, Equality Act 2010, Human Rights Act, Care Act 2014) | 🟢 In progress |
| 8 | Interpreter regulation & agencies (NRCPD, RBSLI, VRI, procurement models) | 🟢 In progress |
| 9 | History of BSL & Deaf community in the UK (linguistic recognition, education, oralism) | 🟢 In progress |
| 13 | Victims & prisoners (Deaf/DeafBlind access to justice — as victims/witnesses and as prisoners) | 🟢 In progress |

### Cluster D — Money & Accountability
| # | Domain | Status |
|---|--------|--------|
| 10 | Charities & third sector (RNID, SignHealth, BDA, Action Deafness — remit, funding, overlap) | 🟢 In progress |
| 11 | Public spending & contracts (interpreting agency spend, ICB commissioning, procurement) | 🟢 In progress |
| 12 | Waste vs. grassroots delivery (where taxpayer money is lost to overhead/agencies vs. reaching frontline/community services) | 🟢 In progress |

### Cluster E — Education
| # | Domain | Status |
|---|--------|--------|
| 15 | Education, early years to higher education (Teacher of the Deaf workforce, BSL GCSE, SEND/EHCP system, Disabled Students' Allowance) | 🟢 In progress |

**Note on Cluster E:** added after an initial gap in the framework — education access sits upstream of nearly every other domain. The language deprivation cited as a root cause in Domain 1's own health-access statistics traces directly back to early-years and school-age education failures, making this less a standalone topic than the foundation several other domains already assume.

**Note on Domain 18:** deliberately split out from Domain 5 (Access to Work), which now also carries the national-DWP-level assessment/UC-digital/equality-wording material (PIP/AtW interpreter provision, DWP's own strategy documents). Domain 18 covers only what happens at a named local Jobcentre — a national policy document is evidence of capability, not of local practice, unless it names the specific office or booking.

**Note on Domain 12:** this is explicitly a cross-cutting lens applied *within* each other domain (e.g., "how much of Access to Work's interpreter budget goes to agency margin vs. interpreter pay" is a Domain 5 + Domain 12 question), not a standalone pot of facts. Each domain briefing should include a "money trail" subsection addressing it directly.

---

## 3. Source Hierarchy

Applied consistently across all domains, ranked by reliability:

1. **Primary legal/government sources** — legislation.gov.uk, gov.uk statistical releases, NHS Digital/NHS England publications, DWP official statistics, Hansard, select committee reports, ICB board papers
2. **Regulatory & professional bodies** — NRCPD (National Registers of Communication Professionals working with Deaf and Deafblind people), CQC reports, Ofcom (broadcast access), Ofqual (BSL qualifications)
3. **Named research reports with methodology** — *Still Ignored* (RNID/SignHealth, Apr 2025), *Locked Out* (BSL Advisory Board, Nov 2025), *Funding Justice* (Disability Rights UK), SignHealth's "Sick of It" series, university/academic studies
4. **FOI responses** — highest value when cross-referenced against official statistics; always log via WhatDoTheyKnow first per existing FOI workstream discipline
5. **Charity/advocacy publications** — useful for lived-experience data and advocacy framing, but flag as advocacy-sourced rather than independently audited
6. **News reporting** — useful for recency and specific incidents, cite outlet and date, treat single-source claims with caution
7. **Community/anecdotal sources** — valuable for identifying where to look further, never used as a standalone citation for a factual claim in a canonical document

**Never treat as sourced:** unattributed statistics circulating on social media, AI-generated summaries without a traceable citation trail (this document included — every figure must trace to something in tiers 1–4 before going into a domain briefing).

---

## 4. Domain Briefing Template

Each `BSL_DOMAIN_<name>.md` should follow this structure so briefings are consistent and scannable:

```
# Domain: [Name]

**Last verified:** [date]
**Re-check cadence:** [e.g., quarterly / on policy change]
**Confidence level:** [High / Medium / Contested]

## Summary (3-5 sentences)

## Key Figures (with source + date for each)

## Key Organisations & Actors

## Current Policy / Legal Position

## Known Gaps & Contested Figures
(anything found in circulation but not verifiable from a tier 1-4 source)

## Money Trail
(spend, contracts, where funding goes vs. where it's meant to go)

## FOI Targets Arising
(bodies to approach, what to ask, cost-limit considerations per S.12)

## Sources
(full citations)
```

---

## 5. Verification Discipline (carried over from stakeholder matrix workflow)

- **Cross-check before canonising.** The stakeholder matrix used a Grok cross-check pass before accepting new content into v10; the same discipline applies here — a second-pass verification search before a figure goes from "found" to "trusted."
- **Flag staleness explicitly.** Any organisational status, policy deadline, or figure older than 12 months gets flagged for re-verification, not assumed current (this caught the deafPLUS/Action Deafness merger and the RADF deadline correction).
- **Distinguish contested from confirmed.** Where public/circulated figures conflict with primary sources (as happened with the NRCPD Deafblind interpreter count), both figures are recorded with their source, not silently resolved.
- **Distinguish VCSE from commercial actors.** As already applied to DA Languages — money-trail and engagement-strategy conclusions differ depending on whether an actor is a charity, statutory body, or commercial contractor.

---

## 6. Relationship to Existing Project Assets

| Existing asset | How it connects |
|---|---|
| Stakeholder matrix (v10, 29 orgs) | Domains 1, 10, 11 draw directly on organisations already mapped there |
| `BSL-request-data-gap-tracker.docx` | FOI targets identified per domain feed into this tracker |
| `BSL-FOI-companion-log.xlsx` | Tracks FOI requests arising from each domain briefing |
| `bsl-access-register-status.md` (Claude project doc, not in this folder) | Domain 1 (NHS interpreter provision) is the direct evidence base underpinning that project's health-access focus. Supersedes an earlier reference to a `DEAF_NETWORK_HEALTH_SUMMARY.md` file that was never created in this folder. |
| `prompts/SuperGrok_Research_Prompt_Pack.md` | The master prompt-numbering index for every SuperGrok research batch across this project (see that file's own index table) — check it before issuing a new numbered batch of prompts for any domain. |

---

## 7. Next Steps

1. ✅ Framework established (this document)
2. 🟢 **In progress:** Domain 1 — NHS interpreter provision & BSL health access
3. 🟢 **In progress:** Domain 2 — Mental health services & Deaf/DeafBlind access
4. 🟢 **In progress:** Domain 3 — DeafBlind-specific provision
5. 🟢 **In progress:** Domain 4 — PIP & DLA
6. 🟢 **In progress:** Domain 5 — Access to Work
7. 🟢 **In progress:** Domain 6 — Neurodivergence overlap
8. 🟢 **In progress:** Domain 7 — Legislation
9. 🟢 **In progress:** Domain 8 — Interpreter regulation & agencies
10. 🟢 **In progress:** Domain 9 — History of BSL & the Deaf community
11. 🟢 **In progress:** Domain 10 — Charities & third sector
12. 🟢 **In progress:** Domain 11 — Public spending & contracts
13. 🟢 **In progress:** Domain 12 — Waste vs. grassroots delivery
14. 🟢 **In progress:** Domain 13 — Victims & prisoners (Deaf/DeafBlind access to justice)
15. 🟢 **In progress:** Domain 14 — Devices & technology, including AI
16. 🟢 **In progress:** Domain 15 — Education, early years to higher education
17. 🟢 **In progress, added 8 September 2026:** Domain 18 — Jobcentre Plus (in-person/local service delivery). Built from a dedicated research pass (prompts 27-33). The two named legal/complaint cases (Rimmer, Clarke) and the DWP BSL 5-year plan were independently confirmed against primary sources the same day; several individual Parliamentary Questions cited in that pass were not yet re-verified (see the domain file's own Verification note).
18. 🟢 **Verification work is well underway, not a future priority.** Updated 7 Sep 2026. `VERIFICATION_STATUS.md` has grown from its original state to 50 numbered sections (Sections 19-50 added since this item was last written), covering direct primary-source verification across most domains, a new Domain 17 (Video Relay Service & Telecoms Equity, added 6 Sep 2026 and now the single most-verified domain in the project at 12+ research rounds plus multiple follow-up passes), corrections to fabricated or uncorroborated figures where found, and several genuine negative results (confirmed absences, not unresearched gaps) logged with the same discipline as positive findings. Two companion outputs — `bsl_dossier.html` and the published "BSL Access Register" artifact — are kept in sync with VERIFICATION_STATUS.md as each section lands, not just the domain files themselves. Remaining verification work is tracked as specific, dated follow-ups inside `VERIFICATION_STATUS.md`'s own sections (e.g. Section 44's ~Dec 2026 BSL GCSE re-check, Section 43's unconfirmed South East/South West Deaf CAMHS waiting-time data) rather than as a single undifferentiated backlog — check the tracker's own header line for the current running summary before assuming a domain is unverified.
19. 🔴 Build `GEOMETRICMIND_PROJECT_INDEX.md` (previously flagged gap, still outstanding)

## 8. Audience Map & Communications Strategy

The evidence base only creates pressure if it reaches the people who can act on it — and different audiences need the same underlying facts reframed differently. A dense evidence table that works for an FOI officer will not land with an employer deciding whether to hire a Deaf candidate.

| Audience | What they need from this project | Currently served? |
|---|---|---|
| **Team (internal)** | Sourced evidence, FOI targets, contested-figure tracking | ✅ Yes — domain briefings, FOI list |
| **Grassroots Deaf/DeafBlind individuals** | Plain-language rights, what to do if those rights aren't met | ✅ Yes — Know Your Rights section |
| **NHS bodies, agencies, government** | Implicitly the pressure target — held accountable via published gaps and contested figures | ✅ Yes — Contested Figures, FOI Targets |
| **Charities & third sector** | A shared, cross-referenced evidence base for funding bids and campaigns; coordination to avoid duplicated asks | 🔴 Was missing — closed via "For Charities & Businesses" site section |
| **Businesses & employers** | Their legal duty, how Access to Work actually works for them, the business case for getting this right | 🔴 Was missing — closed via "For Charities & Businesses" site section |
| **Policymakers & media** | Quotable, sourced figures; a clear "who's accountable for what" map | 🔴 Still missing — not yet built, flagged for a future pass |

**Design principle for closing an audience gap:** don't just duplicate the evidence tables with a new label. Each audience needs (a) why this matters *to them specifically*, (b) the smallest set of figures that make the case, and (c) one concrete action — not the full domain briefing. The full evidence stays one click away for anyone who wants to go deeper.

---

*This is a living document. Update the domain status table as each briefing is completed, and log the "last verified" date at the top of each domain file so staleness is visible at a glance.*


