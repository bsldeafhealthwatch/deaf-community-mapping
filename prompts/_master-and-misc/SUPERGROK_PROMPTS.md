# SuperGrok Research Prompt Pack (original — Categories A/B/C)

**⚠️ This is the file commonly referred to elsewhere as "the original 19 prompts" (Categories A1–A5 + B1–B11 + C1–C3 = 19). It was never numbered 1–19 sequentially — that shorthand describes it, it isn't a section title inside it.** The master running index of every numbered prompt batch in this project (including this file's place in the sequence, and the next free number for a new batch) lives in `SuperGrok_Research_Prompt_Pack.md` — check there before adding a new batch anywhere, so numbering never collides or restarts at 1 by mistake.

**Purpose:** Ready-to-paste prompts for SuperGrok to generate sourced, structured data for the remaining pending domains and the new charities/business audience section. This extends the same "Grok cross-check pass" discipline already used to verify the stakeholder matrix (v7→v10).

**How to use this pack:**
1. Paste a prompt into SuperGrok as-is, or fill in the `[bracketed]` placeholders first
2. **Never paste Grok's output straight into the dossier or a domain briefing.** Review every figure against the source it cites — this pack asks Grok to cite sources, but citing a source and citing it *correctly* are different things
3. Once verified, add figures to the relevant domain briefing (`BSL_DOMAIN_<name>.md`) and, if it's a headline figure, to the live dossier via the edit-in-place forms
4. If Grok returns a figure with no traceable source, or a source that turns out not to say what Grok claims, log it as a **gap**, not a fact — the framework's source hierarchy treats an unsourced AI-generated claim as the lowest tier, below even news reporting

---

## Standard output format to request

Append this to every prompt below so results come back ready to slot into the site's data model:

> Format your answer as a table with these exact columns: **Label | Value | Source name | Source URL | Publication date | Confidence (Verified/Contested/No reliable figure found)**. For any figure you cannot trace to a specific, named, dateable source, write "No reliable figure found" in the Value column rather than estimating. Where UK sources conflict with each other, list both with their respective sources rather than picking one. Prioritise England-specific data; note clearly if a figure is UK-wide, England-only, or from another nation, since devolved policy differs.

---

## Category A — Verification of currently contested figures

### A1. RADF deadline resolution
> I need the current, final conformance deadline for NHS England's Reasonable Adjustment Digital Flag (DAPB4019 / Amd 41/2025), specifically for the health sector. NHS England's own standards page has shown a conformance date change from 30 September 2026 back to 30 September 2026 within the three weeks before 4 September 2026, with a note that a further change requires Data Assurance Board approval. Search for the most recent confirmation of this date, including any NHS England press releases, board papers, or trade press coverage from August–September 2026. State clearly if the date is still unresolved as of today.

### A2. NHS audiology waiting times — primary source check
> Find NHS England's own primary statistical release (not a commercial or third-party summary) for audiology waiting times in England, most recent quarter available. I specifically need: the percentage of patients waiting 6+ weeks for a hearing assessment, and the percentage waiting for fitting once assessed. A commercial source claims "38% waited six weeks or more" citing March 2025 NHS England data — verify or correct this against NHS England's actual published statistics.

### A3. Deaf/DeafBlind prisoner headcount
> Search for any official UK government, HMPPS, or Ministry of Justice statistic on the number of Deaf or DeafBlind prisoners in England and Wales, in any year. Also check whether HMPPS publishes prisoner communication-needs data broken down by need type (BSL vs. other). If no such figure has ever been published, state that explicitly and note the most recent public criticism of this data gap (e.g. from the British Deaf Association).

### A4. NHS cost of Deaf healthcare accessibility failures
> RNID and SignHealth's "Still Ignored" report (April 2025) is associated with a figure of £80–100 million per year as the cost to the NHS of accessibility gaps for Deaf people. Locate this figure's exact origin — is it in the "Still Ignored" report itself, an earlier RNID report, or a different source entirely? Quote the exact sentence/context where the figure appears and provide a direct link or citation.

### A5. Cochlear implant NHS waiting times
> Find current UK NHS data (England specifically) on adult cochlear implant referral-to-surgery waiting times, and the number or proportion of clinically eligible adult referrals that go unfunded or unactioned per year. Distinguish NHS England data from NICE guidance eligibility criteria, which are different things.

---

## Category B — Filling remaining domains

### B1. Access to Work (Domain 5)
> I'm researching the UK's Access to Work scheme specifically as it affects Deaf and DeafBlind BSL users. Find current (2025–2026) data on: (1) average processing/waiting time for a new Access to Work application, (2) the current annual funding cap per claimant if one exists, (3) the proportion of Access to Work spending that goes to communication support (interpreters, notetakers) vs. equipment, (4) any recent reported backlogs, cuts, or policy changes to the scheme, and (5) criticism from Deaf advocacy organisations (RNID, BDA, NDCS) specifically about how well the scheme serves BSL users.

### B2. PIP and DLA (Domain 4)
> Research how the UK's Personal Independence Payment (PIP) and Disability Living Allowance (DLA) assessment processes specifically affect Deaf and DeafBlind BSL users. I need: (1) whether BSL interpretation is guaranteed at PIP assessments, (2) any documented pattern of Deaf claimants being under-awarded due to assessors misunderstanding BSL-related needs, (3) appeal/tribunal success rates for Deaf claimants if such data is broken out anywhere, and (4) any recent (2025–2026) DWP policy changes to PIP/DLA that affect sensory or communication-related eligibility criteria.

### B3. Neurodivergence overlap (Domain 6)
> Research the intersection of Deafness/BSL use and neurodivergence in the UK — sometimes referred to as "DeafDisabled" or having dual/multiple needs. Find: (1) any UK prevalence data on neurodivergent Deaf BSL users, (2) specific service gaps documented for this group (e.g. autism assessment services that aren't BSL-accessible), and (3) any organisations specifically serving this intersection.

### B4. Legislation (Domain 7)
> Give me a precise, current summary of what legal rights the BSL Act 2022 does and does not create for individual BSL users in the UK, distinct from the Equality Act 2010. I specifically need to know: does the BSL Act 2022 create any enforceable individual service right, or is it a recognition-only statute? Cite the Act's actual text/sections, not secondary commentary, and note any 2025–2026 developments (e.g. the BSL Advisory Board's activity, government reports required under the Act).

### B5. Interpreter regulation & agencies (Domain 8)
> Compare NRCPD and RBSLI as UK sign language interpreter regulators — current registered interpreter numbers for each if published, how NHS/government procurement guidance specifies which register(s) are acceptable, and whether there's any indication of qualification-shopping (agencies using RBSLI-only registrants to access a larger interpreter pool when NRCPD-registered interpreters are scarce). Also find current data on total number of qualified BSL/English interpreters in the UK vs. estimated need.

### B6. History of BSL & Deaf community in the UK (Domain 9)
> Give me a factual timeline of BSL's legal and social recognition in the UK: key dates from 19th-century oralism-era education policy through to the BSL Act 2022. Include: the 2003 UK government recognition of BSL as a language (non-statutory), the BSL (Scotland) Act 2015, and the BSL Act 2022 (England/Wales/NI-relevant provisions). Note where oralism-era policy is still cited by Deaf advocacy organisations as shaping present-day language deprivation outcomes.

### B7. Charities & third sector (Domain 10)
> Compare the current remit, annual income, and reported proportion of spending on direct service delivery vs. overhead/fundraising for RNID, SignHealth, British Deaf Association, and Action Deafness (post its April 2026 absorption of deafPLUS). Use each charity's most recently filed Charity Commission accounts. Present this neutrally as a factual comparison, not as an accusation — the goal is transparency, not implying wrongdoing.

### B8. Public spending & contracts (Domain 11)
> Find any published UK government or NHS contract data for BSL interpreting services — specifically looking for contract values, competitive tender records, or Freedom of Information disclosures relating to companies like DA Languages or similar commercial BSL interpreting providers. Check gov.uk's Contracts Finder and any NHS procurement transparency data.

### B9. Waste vs. grassroots delivery (Domain 12)
> This is a cross-cutting question: find any UK examples (National Audit Office reports, Public Accounts Committee findings, investigative journalism) that specifically examine whether public money intended for Deaf/disability accessibility services reaches frontline delivery vs. being absorbed by administrative overhead, agency margins, or ineffective national programmes. I'm looking for comparative evidence, not opinion pieces.

### B10. Mental health services (Domain 2)
> Research BSL/Deaf-specific NHS mental health provision in the UK, particularly the British Society for Mental Health and Deafness (BSMHD) and any specialist Deaf mental health units (e.g. SWLSTG National Deaf Services already known to this project). Find current waiting times, bed/service capacity, and any documented gaps in crisis mental health support specifically for BSL users (e.g. access to crisis lines, 111/999 BSL access).

### B11. DeafBlind-specific provision (Domain 3)
> Research UK-specific (not US) support and equipment provision for DeafBlind people: intervenor/guide-communicator availability and funding, any national DeafBlind equipment scheme (note: the US has a National Deaf-Blind Equipment Distribution Program via the FCC — I need to know if there is a genuine UK equivalent, or confirm there isn't one), and current NRCPD Deafblind interpreter registration numbers to verify a previously logged figure of 19 nationally registered, 1 in London, against a funded target of 68.

---

## Category C — Audience gap: charities & businesses

### C1. Employer awareness and compliance
> Find any UK survey or research data on employer awareness of their Equality Act 2010 obligations toward Deaf employees, and awareness/uptake of the Access to Work scheme among UK employers. I'm looking for a business-facing statistic — e.g. "X% of UK employers are unaware Access to Work exists" — that could be used to make a business case for better voluntary compliance.

### C2. Charity funding landscape and gaps
> Building on Disability Rights UK's "Funding Justice" analysis, find current (2025–2026) data on UK government/NHS funding allocated to Deaf-specific charitable and third-sector services, and how this compares to funding for other disability groups proportionally. I'm looking for evidence of whether Deaf-specific services are under-funded relative to need, to support charity funding bids.

### C3. Business case data — cost of inaction vs. cost of provision
> Find any UK-specific cost-benefit data comparing the cost to an employer of properly accommodating a Deaf employee (interpreter costs, mostly covered by Access to Work) against the cost of an Equality Act discrimination claim, tribunal case, or reputational damage from a documented failure to accommodate. This is for a business-facing "why this is worth doing" argument, so needs to be defensible and specific, not vague.

---

## Notes on using Grok effectively for this project

- **Ask for primary sources explicitly, every time.** Grok has real-time web/X access, which is valuable for catching very recent changes (like the RADF deadline instability found this session) — but that same recency means it will also surface unverified claims circulating on social media. Push back if a response cites "reports suggest" without a named source.
- **Cross-check anything Grok presents as settled if this project has already flagged it as contested.** If Grok gives a confident single answer for something in Category A, that's a sign either the contradiction has resolved (good — verify and update) or Grok hasn't found the same primary-source discrepancy this team already found (in which case, tell it what you found and ask it to reconcile).
- **Run Category B prompts even for domains that feel low-priority** — a "No reliable figure found" result is itself useful data for the framework's gap-tracking, not a wasted query.
