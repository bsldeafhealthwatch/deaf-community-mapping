# SuperGrok Research Prompt Pack

**Purpose:** Ready-to-paste prompts for SuperGrok to generate sourced, structured data for the remaining pending domains and audience gaps. This extends the same "Grok cross-check pass" discipline already used to verify the stakeholder matrix (v7→v10).

**⚠️ NEXT PROMPT NUMBER TO USE: 38.** The highest prompt number issued anywhere in this project so far is **37** (see the index below). Before adding a new section to this file, check this line, confirm it against the index table, then start your new prompts at the next free number and update this line and the index in the same edit. Never start a new batch back at 1 — see "Numbering discipline" below for why this matters.

**How to use this pack:**
1. Paste a prompt into SuperGrok as-is, or fill in the `[bracketed]` placeholders first
2. **Never paste Grok's output straight into the dossier or a domain briefing.** Review every figure against the source it cites — this pack asks Grok to cite sources, but citing a source and citing it *correctly* are different things
3. Once verified, add figures to the relevant domain briefing (`BSL_DOMAIN_<name>.md`) and, if it's a headline figure, to the live dossier via the edit-in-place forms
4. If Grok returns a figure with no traceable source, or a source that turns out not to say what Grok claims, log it as a **gap**, not a fact — the framework's source hierarchy treats an unsourced AI-generated claim as the lowest tier, below even news reporting

### Numbering discipline (added 8 September 2026, after a near-miss)

A previous attempt to reconstruct "the original prompts 1–19" from memory of an unsaved chat produced a confident-looking but fabricated tracker — plausible section titles, invented "resolved" statuses, no traceable source. It was caught only because the claims contradicted what the domain files actually say. The root cause: this file's numbering implied a single sequential 1–19 document existed somewhere. It didn't (see the index below for what actually exists). Going forward:

- **Every batch of prompts added to this project states its own starting number explicitly**, cross-checked against the index table below, not assumed or reconstructed from memory.
- **This file is the index.** If a prompt exists anywhere in the project (this file or any other `prompts/*.md`), it gets a row here before it's considered numbered. If it's not in the table, treat it as unnumbered rather than guessing where it fits.
- **Never ask Grok (or anyone) to "reconstruct" past prompts from memory of a conversation that wasn't saved.** If a prompt file is genuinely lost, that's a gap to log, not a gap to fill by confident guessing — same rule this project already applies to figures.

---

## Prompt index (all batches, across all files)

| # range | Batch | File | Status |
|---|---|---|---|
| A1–A5 | Contested-figure verification (RADF deadline, audiology waits, prisoner headcount, £80–100m NHS cost origin, cochlear implant waits) | `SUPERGROK_PROMPTS.md` | Lettered, not numbered 1–5 — do not renumber retroactively |
| B1–B11 | Remaining domain gaps (AtW, PIP/DLA, neurodivergence, legislation, interpreter regulation, history, charities, public spending, waste vs. grassroots, mental health, DeafBlind) | `SUPERGROK_PROMPTS.md` | Lettered, not numbered 6–16 — do not renumber retroactively |
| C1–C3 | Charity/business audience gap | `SUPERGROK_PROMPTS.md` | Lettered, not numbered 17–19 — do not renumber retroactively |
| 20–26 | DWP / Welfare & Employment (national) | This file | Prompt text below |
| 27–33 | Jobcentre Plus (local/in-person) | This file | Prompt text below |
| 34–37 | Accessible Information Standard (AIS): legal status/enforcement, data findings on flag/interpreter-booking failures, comparative practice, lived experience | Claude project doc `claude/grok-prompts-ais.md` (Deaf Network Health Group project) | Prompt text in that doc, not this file |
| 38+ | *(not yet issued)* | — | Next available |

**Note on A1–C3:** these are commonly referred to elsewhere in this project as "the original 19 prompts" (5+11+3=19), but the source file itself never numbered them sequentially — it used Category A/B/C with sub-numbers. Do not create a "Prompts 1–19" section reproducing invented text; if the original prompt wording is needed, read it from `SUPERGROK_PROMPTS.md` directly.

---

## Standard output format to request

Append this to every prompt in this pack so results come back ready to slot into the site's data model:

> Format your answer as a table with these exact columns: **Label | Value | Source name | Source URL | Publication date | Confidence (Verified/Contested/No reliable figure found)**.

---

## Prompts 20–26 — DWP / Welfare & Employment: Deaf & DeafBlind specificity

**Added:** 8 September 2026. Covers the DWP gap in the Welfare & Employment cluster.

> Reminder for this section specifically: DWP does not operate under the NHS/social care Accessible Information Standard. Any equivalent obligation would come from the Equality Act reasonable adjustment duty instead — if Grok imports AIS language by analogy for DWP, treat that as a citation error, not a finding.

**20. PIP and Access to Work — BSL/Deaf-specific data**
> Find current UK data on Personal Independence Payment (PIP) and Access to Work claims, awards, and processing times specifically for BSL-using Deaf people and DeafBlind people. Include: number of BSL-users receiving Access to Work support for interpreters, average approval/renewal time, and any documented backlog or funding cap issues (e.g. the Access to Work support cap and its effect on Deaf employees needing interpreters). Distinguish DWP's own published statistics from charity-sourced figures.

**21. DWP assessment accessibility — BSL interpreter provision**
> Find documented evidence on whether DWP contracts BSL interpreters for PIP/ESA/Universal Credit assessments (telephone or in-person), including which contractor(s) provide this, any known failures or complaints (e.g. assessments proceeding without an interpreter, video relay issues), and whether DWP has a published accessibility/reasonable adjustments policy specific to BSL-users. Include any Ombudsman or tribunal findings.

**22. Universal Credit journal and DWP digital services — Deaf/DeafBlind accessibility**
> Find evidence on the accessibility of the DWP's Universal Credit online journal and telephone service for Deaf BSL-users and DeafBlind people, including use of BSL video relay, textphone/Next Generation Text, and whether DWP's digital services meet WCAG 2.1 AA. Confirm there is no AIS-equivalent obligation for DWP and note what duty (if any) applies instead.

**23. Employment rate and employment support — Deaf and DeafBlind specific**
> Find the most recent UK employment rate data specifically for d/Deaf people and separately for DeafBlind people (not combined "hearing loss" or general disability figures), and any DWP employment support programme (e.g. Work and Health Programme, Disability Confident) outcomes data broken down by these groups if it exists. Flag if no disaggregated DWP data exists — this is expected and should be logged as a gap, not filled with a general-disability proxy figure.

**24. DWP FOI responses already on record — cross-check**
> Search for any published FOI responses, DWP transparency releases, or National Audit Office/Work and Pensions Select Committee reports from the last 3 years specifically mentioning BSL, Deaf, or DeafBlind claimants. Include committee inquiry names, dates, and any recommendations made to DWP.

**25. Benefit sanctions and DeafBlind-specific communication failures**
> Find any documented cases, charity reports (e.g. Sense, RNID, SignHealth), or Ombudsman findings where DWP communication failures (missed calls, letters not in accessible format, no interpreter at assessment) led to sanctions, missed appointments, or benefit stoppage for Deaf or DeafBlind claimants. This is likely to surface advocacy-sourced rather than DWP-sourced figures — flag confidence accordingly.

**26. DWP's own equality/accessibility strategy — current status**
> Find DWP's current published equality objectives, accessibility action plan, or disability strategy documents, and check whether BSL or Deaf/DeafBlind people are named specifically anywhere in them, or only referenced under general "disabled people" or "hearing impairment" language. Note the exact wording used — terminology choice is itself evidence for the Contested Figures/gaps framing.

---

### Notes for this section specifically

- Prompts 22 and 26 are the most likely to come back thin or with Grok inventing an AIS-style DWP obligation by analogy — reject that if it appears, per the reminder above.
- For anything cited as coming from a specific named DWP, NAO, or Select Committee document (prompt 24 especially), fetch the primary source directly before it goes into the domain briefing — same standard applied after the DAPB4019 catch.

---

## Prompts 27–33 — Jobcentre Plus: Deaf & DeafBlind specificity

**Added:** 8 September 2026. Covers in-person Jobcentre Plus service delivery, distinct from DWP's national claims/assessment processes covered in prompts 20–26. Where possible, prioritise findings relevant to the SWL ICB footprint (Croydon, Kingston, Merton, Richmond, Sutton, Wandsworth Jobcentres) alongside any national picture.

> Reminder for this section specifically: Jobcentre Plus is DWP's frontline in-person service — distinguish clearly between national DWP policy (already covered above) and what actually happens at a local Jobcentre appointment. Grok may conflate the two; treat a national policy document as evidence of local practice only if it explicitly says so.

**27. BSL interpreter booking at Jobcentre appointments**
> Find documented evidence on how a Deaf BSL-user requests and receives a BSL interpreter for a Jobcentre Plus work coach appointment (Universal Credit claimant commitment meetings, work search reviews). Include: the booking process, advance notice required, any published service standard or target, and whether interpreters are routinely present or the claimant must request one each time. Include named contractor(s) if any.

**28. Video Relay Service (VRS) / SignLive or equivalent availability in Jobcentres**
> Find evidence on whether Jobcentre Plus offices provide on-site video relay or remote BSL interpreting technology (e.g. SignVideo, SignLive, InterpretersLive!) for Deaf claimants, versus requiring an in-person interpreter to be booked separately. Include any pilot schemes, borough-specific rollouts, or documented gaps in provision.

**29. Work coach training on Deaf/DeafBlind awareness**
> Find evidence on whether Jobcentre Plus work coaches receive mandatory or optional training on Deaf awareness, BSL basics, or DeafBlind communication methods (e.g. deafblind manual, hands-on signing). Include training provider if named, and any DWP staff training strategy or Freedom of Information disclosure on this topic.

**30. Claimant commitment flexibility and sanctions risk for Deaf/DeafBlind claimants at Jobcentres**
> Find documented cases, charity reports, or FOI disclosures on Jobcentre-level failures specific to in-person appointments — for example, a claimant marked as failing to attend or engage because a booked interpreter did not arrive, or a work coach proceeding without one. Distinguish this from prompt 25 (which covers DWP communication failures generally, e.g. letters/calls) — this prompt is specifically about the in-person appointment failure point.

**31. Physical/environmental accessibility of Jobcentre Plus offices for DeafBlind claimants**
> Find evidence on physical accessibility provisions at Jobcentre Plus offices relevant to DeafBlind claimants specifically — e.g. guided support, tactile signing space, quiet/low-visual-noise rooms, or any published accessibility audit of Jobcentre premises. This is likely to return little to no DWP-sourced data; if so, log as "no reliable figure found" rather than substituting a general disability-access figure.

**32. Local SWL borough Jobcentre-specific provision or partnership**
> Find any evidence of a specific Jobcentre Plus office within Croydon, Kingston, Merton, Richmond, Sutton, or Wandsworth having a named partnership, pilot, or documented practice for supporting Deaf or DeafBlind claimants (e.g. with a local deaf charity, RAD Croydon, Richmond AID, or a co-location arrangement). Search each borough separately if a combined search returns nothing — this is a plausible gap.

**33. Escalation/complaints route specific to Jobcentre interpreter failures**
> Find the correct DWP/Jobcentre Plus complaints escalation route for a Deaf or DeafBlind claimant when an interpreter fails to attend or a reasonable adjustment is refused at appointment level, including whether this differs from the general DWP complaints process, and any published data on complaint volumes or outcomes in this category (likely to be unpublished/FOI-only — flag accordingly).

---

### Notes for this section specifically

- Prompts 28, 31, and 32 are the most likely to return "no reliable figure found" — Jobcentre-level (as opposed to national DWP-level) accessibility data is rarely published proactively. That's an expected and useful gap for the site, not a failed search.
- Prompt 32 should be run as six separate borough searches if the combined version returns nothing — don't let a null combined result stand in for six unchecked boroughs.
- Anything found here that overlaps with prompts 20–26 (e.g. a national interpreter contractor also confirmed as serving Jobcentres specifically) should be cross-referenced rather than treated as a fresh, separate fact.

---

**Adding a new batch after this one?** The next free number is **34** (see the index near the top of this file and the ⚠️ line under the title). Update both when you add prompts, in the same edit that adds the prompt text — don't add prompts first and index them "later."
