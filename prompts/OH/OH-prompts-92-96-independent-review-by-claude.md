# Feedback for Claude — Occupational Health / working patterns (independent review, after Grok 92–96)

Use this to decide what goes on any public work / adjustments page, what stays internal, and what becomes a line in the existing FOI companion log. It is research constraint, not page copy.

**Date:** 13 September 2026
**Files behind this:**
- prompts/OH-prompt-92-legal-basis-oh-scope.md
- prompts/OH-prompt-93-office-hybrid-typical-oh-recommendations.md
- prompts/OH-prompt-94-night-shift-lone-working-gap.md
- prompts/OH-prompt-95-international-comparative.md
- prompts/OH-prompt-96-lived-experience-case-for-change.md
- prompts/OH-prompts-92-96-claude-feedback.md (Grok's own self-review — read and largely endorsed by this pass)

Re-open before publish — ACAS OH assessments page, HSE INDG73, RNID employer H&S page, NHS Employers deaf-staff article, Home Office disabled-escape guide. Those pages move.

This is Claude's own independent read of the OH/working-patterns batch, not a re-statement of Grok's self-review. Two of the most load-bearing claims were spot-checked live against primary sources rather than trusted from the quote (see "Spot-check" below). Grok's self-review is unusually disciplined for this batch — it already carries a correct Don't list, a correct FOI plan, and a correct cross-batch map — so this review's job is chiefly to verify, tighten two points Grok left soft, and confirm nothing should change before publish.

**Proposed domain:** stub under the existing Welfare & Employment cluster. Do **not** stand up a new Domain off this batch. Agreed with Grok's own verdict.

---

## Spot-check — the two most load-bearing claims, verified live

1. **"The employer decides whether to implement OH recommendations" (ACAS).** Fetched `acas.org.uk/using-occupational-health-at-work/using-occupational-health-to-help-someone-at-work` live on this pass. The sentence holds verbatim: *"It's up to the employer to decide whether to put in place the recommendations from the occupational health assessment."* Page still shows no BSL/Deaf/hearing-impairment content. Last-updated date confirmed as **17 December 2025**, matching the findings file exactly.
2. **HSE's INDG73 does not name Deaf/BSL.** Fetched both the HSE landing page and the INDG73 PDF live. Confirmed absence of any Deaf/BSL/hearing-impairment mention. The PDF's keep-in-touch wording is verbatim as quoted in prompt 94: *"pre-agreed intervals of regular contact between the lone worker and employer, using phones, radios, email etc, bearing in mind the worker's understanding of English"*, plus *"other devices designed to raise the alarm in an emergency which can be operated manually or automatically"* and a return-to-base check. This is the finding the whole batch's headline rests on (94 is explicitly the load-bearing file), and it is accurate: the leaflet's own language already leaves room for a non-phone channel without ever naming who it's for.

Both claims verified. No correction needed to the headline of either prompt 92 or prompt 94.

---

## Verdict for any public page

**Curate first. Draft almost nothing.**

The sentence a page is allowed to lead with, if it leads at all:

> Occupational Health advises; the Equality Act duty to make reasonable adjustments sits with the employer. The official UK lone-working leaflet (HSE INDG73) does not mention BSL or Deaf staff. Flashing alarms and vibrating pagers are the named kit in fire-safety and RNID employer guidance — whether they're issued to someone on a night or lone shift is an individual PEEP / adjustment question, not something any published national protocol answers.

What already exists and should be linked, not rewritten:

| Need | Point at |
|---|---|
| What OH is, who consents, who decides | ACAS, Occupational health assessments (updated 17 Dec 2025) |
| Employer checklist incl. pagers for lone workers | RNID, Provide health and safety support (updated 26 May 2026) |
| NHS employer-facing list | NHS Employers, Employing deaf and hard of hearing staff in the NHS (9 Jun 2025) |
| Fire / PEEP questions incl. "alone" and "out of hours" | Home Office, Fire safety risk assessment: means of escape for disabled people (updated 12 Sep 2023) |
| Generic lone-working leaflet (silent on Deaf/BSL) | HSE INDG73 |
| AtW as payer for interpreters/alerting kit | Existing 52–54 pages. Do not rewrite the cap here |
| Employee rights language | RNID, Your right to reasonable adjustments at work |

Thin original drafts worth doing *later*, after a human signs this file off:

1. A short "cover every pattern I work" note the employee can hand HR before the OH appointment — office, home, night/late, lone/mobile. Cite ACAS (employer decides) + Equality Act s.20. Must not say "OH must" or "unlawful if omitted."
2. A one-screen "who holds which duty" box: employer = s.20; responsible person = Fire Safety Order/PEEP; AtW = grant; OH = advice only. The thinness of that map *is* the prompt-92 finding, not a reason to avoid stating it plainly.

Nothing beyond those two. No OH report template, no lone-working SOP, no pager spec — RNID and the Home Office guide already own that ground.

---

## Don't list (print near any work / OH / adjustments page)

- Do not print that OH itself carries the Equality Act s.20 duty. The duty-holder is the employer; OH advice can put the employer on notice, nothing more.
- Do not print "OH must assess night / lone / home working." No FOM, SOM or ACAS product creates that requirement. A silent OH report is a practice gap, not an automatic breach.
- Do not print "duty of care breach," "non-compliant OH report," "unlawful lone-working practice," or "non-compliant with the Act" from this batch — no named statute, regulation or judgment supports any of those phrasings here.
- Do not print INDG73 as forbidding text/app check-in. It already lists email and "other devices designed to raise the alarm." The finding is that it doesn't name Deaf/BSL, not that HSE has banned accessible methods.
- Do not print a national rate of Deaf staff on night/lone rotas, or a fulfilment rate for vibrating pagers. Neither exists in the sourced material.
- Do not present *Iqbal v Home Office* (2200324/2016) as a win, a night-shift case, or a home-working-transfer case. It is an office-hours BSL-interpreter-hours dispute; the claimant lost.
- Do not present *Sheikh v CIS Security*, the BBC late-shift EAT commentary, or *Mahoro v Northern Care Alliance* as Deaf cases — they concern other impairments.
- Do not collapse AtW into the employer's s.20 duty. Cap/freeze/processing figures live in prompts 52–54; do not re-derive them here.
- Do not cite PAS 79:2007 as the live fire-risk product — the housing part (PAS 79-2) was withdrawn 6 August 2021.
- Do not paste MCA/seafarer Approved Doctor hearing standards, or any US/Australian/Canadian material (OSHA 1910.165, EEOC, ADA §215, JobAccess, *Strudwick* 2015 ONSC), into a UK data cell. International is context only.
- Do not treat Northern Ireland as covered by the Equality Act for employment — it remains on the DDA 1995 (as amended).
- Do not recycle Rimmer, Clarke, Bussey, Elliott or Thomas into this batch — they belong to other domains.
- Do not hold any of this out as advice on a named individual's live OH referral.

---

## What to do with this finding

| Scenario | Action |
|---|---|
| "Is my employer breaking the law if OH only flagged a visual fire alarm?" | Not a legal verdict. Point at ACAS (employer decides), RNID rights page, Home Office PEEP guide. State plainly that the official lone-working leaflet doesn't name BSL. Do not print "breach." |
| Someone wants "the number" of Deaf night/lone workers or pager coverage | No reliable figure found. Offer the FOI questions below rather than deriving one from Census BSL-main-language counts or AtW's interpreter-customer count — those are different denominators. |
| Someone wants a letter/template | Link RNID + ACAS. The only original draft worth doing later is the short pre-OH note, after sign-off. |
| Someone wants a new domain page | No — one stub paragraph under Welfare & Employment, linking the resources above. |

---

## What actually closes the gap (ranked)

1. **FOI, folded into the existing companion log** (not a new tracker) — ask employers (the six SWL councils, ICB, named trusts already on cycle) whether their PEEP template asks if an employee works alone or out of hours, how many vibrating/critical-alert pagers or visual-alarm devices have been issued to *staff* (not patients) who are Deaf/DeafBlind/hearing-loss in the last 3 years, whether the lone-working SOP names a non-phone check-in option, and whether a BSL interpreter is routinely offered for *staff* OH appointments (as distinct from patient AIS bookings). Frame every question yes/no/number/attach-the-clause — do not ask a body to invent a Deaf protocol on the form.
2. **Link the live resource** — RNID H&S page, Home Office PEEP guide, ACAS OH page, NHS Employers 2025 article. A rewritten version of any of these is wasted labour.
3. **A dated stub sentence** on the existing Welfare & Employment page, along the lines already drafted in Grok's own review, dated to this compile window and flagged for re-check before the next publish.
4. **A new draft** — only the short pre-OH note and the duty-map box, and only once a human has signed off this file.

---

## Cross-batch rules

- Distinct from prompts 20–26 / 27–33 / 52–54 (all DWP-facing) — this batch is the employer/OH/premises-safety layer once someone is already in post. Do not re-derive the AtW cap (£69,260, frozen through 2026/27) or the 3,210 BSL-interpreter AtW customer count here; those live in 52–54.
- Distinct from 85–91 (neurodivergence) — a Deaf autistic employee's OH report is still an Equality Act s.20 object, not a NICE diagnostic pathway.
- Distinct from 78–80 (VRS/Telecoms) — video relay in the office or at home is an item on the prompt-93 list and an AtW product, not a lone-worker emergency pager.
- Distinct from AIS 34–37 — AIS governs NHS patient information, not staff-side OH appointments. Do not write "AIS requires a BSL interpreter at Occupational Health."
- Held-back leg: no NHS-vs-security sector split should be spent as a future prompt number unless a source is later found naming a protocol specific to one sector — 94 tested for this and found nothing in either.
- Held-back prompt number: 97 onward continues the Welfare & Employment stub sequence (already issued for HR/IT SLA, 97–102) — nothing further is owed to this batch specifically.

---

## What this pass adds beyond Grok's own review

Grok's self-review (`OH-prompts-92-96-claude-feedback.md`) already correctly flagged the same Don't-list items, the same FOI plan, and the same "nice to add" PEEP-layer material (Kent County Council PEEP standard HS S 012, commercial PEEP templates asking about BSL, the BMJ 17 Sep 2025 letter — still paywalled, title-only). This review does not repeat that material in full; it stands as read and endorsed. The value added here is the live re-verification of the two load-bearing primary sources (ACAS "employer decides" sentence + date; HSE INDG73 Deaf/BSL silence + exact keep-in-touch wording), both of which held without correction, and confirmation that the "curate first" verdict is the right call — nothing in this batch supports drafting new guidance beyond the two thin items both reviews independently converge on.

**Still to re-open before anything public:** FOM Ethics Guidance 9th edition (never opened end-to-end), BS 5839-1:2025 clause 17 (paywalled, sourced only from industry extracts), the BMJ 17 September 2025 letter (title only).
